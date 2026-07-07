#!/usr/bin/env python3
"""여러 알고리즘을 병렬로 pass@k 실행.

병렬 단위 = 알고리즘 (스레드 1개가 runner.run(algo, k) 통째로 담당). 각 스레드는
독립적(자체 LLM 클라이언트 + 자체 tempdir); bundle/dopart 는 스레드안전.

사용:
  python3 batch.py crypto_aead/ascon96v1 crypto_kem/ntruplus576   # 인자로 나열
  python3 batch.py --pick picks.json                              # JSON 목록
  옵션: -k 3  --workers 10  --model gpt-5.4-mini
picks.json 형식: [{"category":"crypto_aead","algorithm":"ascon96v1"}, ...]
              또는 ["crypto_aead/ascon96v1", ...]
"""
import os, sys, json, time, argparse, threading, traceback
from concurrent.futures import ThreadPoolExecutor, as_completed
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
import runner


def _parse_item(x):
    if isinstance(x, dict):
        return x['category'], x['algorithm']
    cat, algo = x.split('/', 1)          # "crypto_aead/ascon96v1"
    return cat, algo


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('items', nargs='*', help='<category>/<algorithm> ...')
    ap.add_argument('--pick', help='JSON 목록 파일')
    ap.add_argument('-k', type=int, default=None, help=f'시도 수 (기본 config.K={config.K})')
    ap.add_argument('--workers', type=int, default=10, help='동시 실행 알고리즘 수')
    ap.add_argument('--model', default=None, help=f'기본 config.MODEL={config.MODEL}')
    a = ap.parse_args()

    raw = json.load(open(a.pick)) if a.pick else a.items
    items = [_parse_item(x) for x in raw]
    if not items:
        ap.error('알고리즘을 인자나 --pick 로 주세요')
    K = a.k or config.K

    lock = threading.Lock()
    results = {}
    t0 = time.time()

    def work(i, cat, algo):
        s0 = time.time()
        try:
            s = runner.run(cat, algo, k=K, model=a.model)
            r = {'i': i, 'algorithm': algo, 'pass': s['pass_at_k'],
                 'pass_count': s['pass_count'], 'verdicts': s['verdicts'],
                 'tokens': s['tokens'], 'secs': round(time.time() - s0, 1)}
        except Exception as e:
            r = {'i': i, 'algorithm': algo, 'error': str(e)[:200],
                 'tb': traceback.format_exc()[-500:], 'secs': round(time.time() - s0, 1)}
        with lock:
            results[algo] = r
            tag = 'PASS' if r.get('pass') else ('ERR' if 'error' in r else 'fail')
            print(f"[{len(results)}/{len(items)}] {algo:32s} {tag} "
                  f"{r.get('pass_count','-')}/{K}  {r.get('verdicts', r.get('error',''))}", flush=True)

    print(f"### 병렬 pass@{K}  workers={a.workers}  model={a.model or config.MODEL}  "
          f"run-timeout={os.environ.get('CRYPTOFORGE_RUN_TIMEOUT','300')}s ###", flush=True)
    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = [ex.submit(work, i, c, al) for i, (c, al) in enumerate(items)]
        for _ in as_completed(futs):
            pass

    print(f"\n#### FINAL pass@{K}  total {round(time.time()-t0)}s ####")
    npass = 0
    for algo in sorted(results, key=lambda k: results[k]['i']):
        r = results[algo]
        if 'error' in r:
            print(f"  {algo:32s} ERROR {r['error'][:70]}")
        else:
            npass += bool(r['pass'])
            print(f"  {algo:32s} {'PASS' if r['pass'] else 'fail'} {r['pass_count']}/{K}  {r['verdicts']}")
    tin = sum(r.get('tokens', {}).get('in', 0) for r in results.values())
    tout = sum(r.get('tokens', {}).get('out', 0) for r in results.values())
    print(f"pass@{K}: {npass}/{len(items)} algorithms  |  tokens in={tin} out={tout}")


if __name__ == '__main__':
    main()
