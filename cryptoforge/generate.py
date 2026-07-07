#!/usr/bin/env python3
"""[LLM 서브에이전트] plan의 각 파일을 구현 → impl 디렉토리 조립.

build_order 순서로 파일 1개씩 생성. 각 잡 입력 = A(설명) + plan 요약 +
이미 생성된 의존파일 전체내용 + 이 파일이 제공할 함수/매크로. 출력 = 그 파일의 완전한 소스.
끝나면 flat api.h 합성해 함께 배치. impl 디렉토리 경로 반환.
"""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
from llm import LLM
from bundle import flat_api_h
import promptlib

FILEGEN = promptlib.filegen_system(None)


def _strip_code(txt):
    """모델 출력에서 코드펜스 제거, 순수 파일내용만."""
    t = txt.strip()
    m = re.match(r'^```[a-zA-Z0-9]*\n(.*)\n```$', t, flags=re.DOTALL)
    if m: return m.group(1).strip() + '\n'
    # 펜스가 중간에만 있으면 첫 펜스 블록 사용
    m = re.search(r'```[a-zA-Z0-9]*\n(.*?)\n```', t, flags=re.DOTALL)
    if m: return m.group(1).strip() + '\n'
    return t + ('\n' if not t.endswith('\n') else '')


def _file_user_prompt(bundle, plan, fmeta, generated):
    return promptlib.filegen_user(bundle, plan, fmeta, generated)


def generate(bundle, plan, out_dir, llm=None, log=None):
    """plan대로 파일 생성 → out_dir. 반환: (impl_dir, files[]).
    각 파일의 실제 프롬프트는 out_dir/.prompts/<path>.md 로도 저장(디버깅)."""
    llm = llm or LLM()
    os.makedirs(out_dir, exist_ok=True)
    pdir = os.path.join(out_dir, '.prompts')
    os.makedirs(pdir, exist_ok=True)
    fmap = {f['path']: f for f in plan['files']}
    order = [p for p in plan['build_order'] if p in fmap]
    generated = {}
    for path in order:
        fmeta = fmap[path]
        user = _file_user_prompt(bundle, plan, fmeta, generated)
        psafe = path.replace('/', '__') + '.md'
        open(os.path.join(pdir, psafe), 'w').write(
            f'[SYSTEM]\n{FILEGEN}\n\n[USER]\n{user}')
        txt, usage = llm.complete(FILEGEN, user)
        code = _strip_code(txt)
        generated[path] = code
        # 하위 디렉토리 경로 방어
        safe = path.replace('..', '_')
        dest = os.path.join(out_dir, safe)
        os.makedirs(os.path.dirname(dest), exist_ok=True) if os.path.dirname(dest) else None
        open(dest, 'w').write(code)
        if log is not None:
            log.append({'file': path, 'usage': usage, 'chars': len(code)})
    # flat api.h
    open(os.path.join(out_dir, 'api.h'), 'w').write(flat_api_h(bundle['constants']))
    return out_dir, list(generated.keys())


if __name__ == '__main__':
    import bundle as B
    from planner import make_plan
    cat, algo = sys.argv[1], sys.argv[2]
    b = B.bundle(cat, algo)
    llm = LLM()
    plan, _ = make_plan(b, llm=llm)
    out = os.path.join(config.RUNS, algo, 'manual', 'impl')
    log = []
    d, files = generate(b, plan, out, llm=llm, log=log)
    print('impl dir:', d)
    print('files:', files)
    print('gen log:', json.dumps(log, indent=1))
