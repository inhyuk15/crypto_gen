#!/usr/bin/env python3
"""알고리즘별 프롬프트 찍어내기 → prompts/<algorithm>/.

템플릿(prompts/templates/*) + operation_notes + 번들(A/entry/상수)을 치환해
'실제로 모델에 보낼 프롬프트'를 디스크에 남긴다(검수·디버깅용). promptlib 를 그대로
쓰므로 런타임 프롬프트와 100% 동일.

산출물 prompts/<algorithm>/:
  planner.md        — planner 의 [SYSTEM]+[USER] 완성본 (plan 불필요, 완전본)
  filegen.md        — filegen [SYSTEM] + 모든 파일잡 공통 [CONTEXT]
                      (per-file TARGET 섹션은 런타임에 attempt/impl/.prompts/ 에 저장됨)
  meta.json         — operation/entry/constants/desc_file/크기 요약

사용:
  python3 render.py <category> <algorithm>      # 하나
  python3 render.py --pick pick10.json          # 목록(JSON: [{category,algorithm},...])
"""
import os, sys, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
import bundle as B
import promptlib

PROMPTS = os.path.join(config.HERE, 'prompts')


def render(category, algorithm):
    b = B.bundle(category, algorithm)
    out = os.path.join(PROMPTS, algorithm)
    os.makedirs(out, exist_ok=True)

    planner = f'[SYSTEM]\n{promptlib.planner_system(b)}\n\n[USER]\n{promptlib.planner_user(b)}'
    open(os.path.join(out, 'planner.md'), 'w').write(planner)

    filegen = (f'[SYSTEM]\n{promptlib.filegen_system(b)}\n\n'
               f'[USER — shared context prepended to every per-file job]\n'
               f'# Algorithm: {b["algorithm"]}  (operation: crypto_{b["operation"]})\n\n'
               f'{promptlib.filegen_context(b)}\n'
               f'(At runtime, a "TARGET FILE / dependency files" section for each planned '
               f'file is appended here — see runs/<algo>/attempt_*/impl/.prompts/.)\n')
    open(os.path.join(out, 'filegen.md'), 'w').write(filegen)

    meta = {
        'category': category, 'algorithm': algorithm,
        'operation': b['operation'], 'primitive': b['primitive'],
        'entry_functions': b['entry_functions'],
        'constants': b['constants'],
        'desc_file': b['desc_file'], 'desc_chars': b['desc_chars'],
        'planner_prompt_chars': len(planner),
    }
    json.dump(meta, open(os.path.join(out, 'meta.json'), 'w'),
              ensure_ascii=False, indent=1)
    return out, meta


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('category', nargs='?')
    ap.add_argument('algorithm', nargs='?')
    ap.add_argument('--pick', help='JSON list of {category,algorithm}')
    a = ap.parse_args()
    if a.pick:
        items = json.load(open(a.pick))
    elif a.category and a.algorithm:
        items = [{'category': a.category, 'algorithm': a.algorithm}]
    else:
        ap.error('give <category> <algorithm> or --pick file.json')
    for it in items:
        try:
            out, meta = render(it['category'], it['algorithm'])
            print(f"[ok] {it['algorithm']:32s} op={meta['operation']:5s} "
                  f"desc={meta['desc_chars']:>6}B  -> {os.path.relpath(out, config.ROOT)}")
        except Exception as e:
            print(f"[FAIL] {it.get('algorithm')}: {e}")
