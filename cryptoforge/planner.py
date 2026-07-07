#!/usr/bin/env python3
"""[LLM] 입력번들 → plan(파일·함수·의존순서).

planner 프롬프트에 A(설명)+entry+상수를 채워 LLM 호출 → JSON plan 파싱·검증.
파싱/검증 실패시 에러를 붙여 재시도.
"""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
from llm import LLM
from schema import validate_plan
import promptlib

TEMPLATE = promptlib.planner_system(None)


def build_user_prompt(bundle):
    return promptlib.planner_user(bundle)


def _extract_json(txt):
    """모델 출력에서 JSON 객체 추출 (코드펜스/잡음 허용)."""
    t = txt.strip()
    t = re.sub(r'^```(?:json)?\s*|\s*```$', '', t, flags=re.MULTILINE).strip()
    try:
        return json.loads(t)
    except Exception:
        pass
    a, b = t.find('{'), t.rfind('}')
    if a >= 0 and b > a:
        return json.loads(t[a:b + 1])
    raise ValueError('plan JSON 파싱 실패')


def make_plan(bundle, llm=None, max_tries=3):
    """(plan, meta). 실패시 예외."""
    llm = llm or LLM()
    user = build_user_prompt(bundle)
    feedback = ''
    for attempt in range(max_tries):
        u = user if not feedback else user + f'\n\n## Previous attempt was invalid, fix:\n{feedback}'
        txt, usage = llm.complete(TEMPLATE, u)
        try:
            plan = _extract_json(txt)
        except Exception as e:
            feedback = f'JSON 파싱 실패: {e}'; continue
        ok, errs = validate_plan(plan, bundle)
        if ok:
            return plan, {'attempt': attempt + 1, 'usage': usage}
        feedback = '검증 오류:\n' + '\n'.join(f'- {e}' for e in errs)
    raise RuntimeError(f'plan 생성 실패({bundle["algorithm"]}): {feedback}')


if __name__ == '__main__':
    import bundle as B
    b = B.bundle(sys.argv[1], sys.argv[2])
    plan, meta = make_plan(b)
    print(json.dumps(plan, ensure_ascii=False, indent=2))
    print('meta:', meta, file=sys.stderr)
