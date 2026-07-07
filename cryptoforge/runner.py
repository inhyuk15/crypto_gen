#!/usr/bin/env python3
"""오케스트레이터 — bundle → (plan → generate → D 채점) 을 k회 → pass@k.

각 시도 산출물은 runs/<algorithm>/attempt_<i>/ 에 저장:
  bundle.json, plan.json, impl/(+api.h), verdict.json
집계는 runs/<algorithm>/summary.json.

사용: python3 runner.py <category> <algorithm> [-k K] [--model M]
"""
import os, sys, json, time, argparse, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
from llm import LLM
import bundle as B
from planner import make_plan
from generate import generate
import dopart_run


def _save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(obj, open(path, 'w'), ensure_ascii=False, indent=1)


def run_once(b, attempt_dir, llm):
    """1 시도: plan → generate → 채점. verdict dict 반환."""
    log = {'stage': None, 'usage': {}, 'gen': []}
    try:
        log['stage'] = 'plan'
        plan, pmeta = make_plan(b, llm=llm)
        _save(os.path.join(attempt_dir, 'plan.json'), plan)
        log['plan_meta'] = pmeta

        log['stage'] = 'generate'
        impl = os.path.join(attempt_dir, 'impl')
        genlog = []
        generate(b, plan, impl, llm=llm, log=genlog)
        log['gen'] = genlog

        log['stage'] = 'score'
        res = dopart_run.run(b['category'], b['primitive'], impl)
        verdict = {'verdict': res['verdict'], 'checksums': res['checksums'],
                   'error': (res['error'] or '')[:2000],
                   'n_files': len(plan['files']), 'log': log}
    except Exception as e:
        verdict = {'verdict': f'PIPELINE_ERROR@{log["stage"]}',
                   'error': f'{e}\n{traceback.format_exc()[-1500:]}', 'log': log}
    _save(os.path.join(attempt_dir, 'verdict.json'), verdict)
    return verdict


def run(category, algorithm, k=None, model=None):
    k = k or config.K
    llm = LLM(model)
    b = B.bundle(category, algorithm)
    base = os.path.join(config.RUNS, algorithm)
    _save(os.path.join(base, 'bundle.json'),
          {**{kk: b[kk] for kk in b if kk != 'description_md'},
           'desc_chars': b['desc_chars']})
    results = []
    for i in range(k):
        ad = os.path.join(base, f'attempt_{i}')
        t0 = time.time()
        v = run_once(b, ad, llm)
        v['secs'] = round(time.time() - t0, 1)
        results.append(v['verdict'])
        print(f"  attempt {i}: {v['verdict']}  ({v['secs']}s)")
    passed = sum(1 for r in results if r == 'PASS')
    summary = {'algorithm': algorithm, 'category': category, 'model': llm.model,
               'k': k, 'pass_count': passed, 'pass_at_k': passed > 0,
               'verdicts': results,
               'tokens': {'in': llm.total_in, 'out': llm.total_out}}
    _save(os.path.join(base, 'summary.json'), summary)
    print(f"\n{algorithm}: pass@{k} = {'PASS' if passed else 'FAIL'} "
          f"({passed}/{k})  tokens in={llm.total_in} out={llm.total_out}")
    return summary


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('category'); ap.add_argument('algorithm')
    ap.add_argument('-k', type=int, default=None)
    ap.add_argument('--model', default=None)
    a = ap.parse_args()
    run(a.category, a.algorithm, k=a.k, model=a.model)
