#!/usr/bin/env python3
"""[결정론, LLM 비개입] 입력번들 조립.

LLM에게 줄 전부 = A(설명) + entry 시그니처 + 인자규약 + 인터페이스 크기 상수.
raw api.h/params.h는 넣지 않음(내부 설계수치 누출 방지). 빌드용 flat api.h는 여기서 합성 가능.

  bundle(category, algorithm) -> dict
  flat_api_h(constants)       -> str   (impl 디렉토리에 넣을 자립 api.h)
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import config
from prompts.arg_conventions import for_operation

# entry 시그니처 verbatim (PROTOTYPES.c)
def _load_prototypes():
    proto = {}
    p = os.path.join(config.SUPERCOP, 'PROTOTYPES.c')
    for l in open(p):
        m = re.match(r'\s*extern\s+(?:int|void)\s+(crypto_\w+)\s*\(', l)
        if m:
            proto[m.group(1)] = l.strip()
    return proto
PROTO = _load_prototypes()


def _index(path, keyfields=('category', 'algorithm')):
    idx = {}
    for l in open(path):
        r = json.loads(l)
        idx[tuple(r[k] for k in keyfields)] = r
    return idx

_FUNCS = None
_DESC = None
def _load():
    # 원자적 세팅: 둘 다 로컬로 읽은 뒤 한 번에 대입 (스레드 병렬시 half-init race 방지).
    global _FUNCS, _DESC
    if _DESC is None:
        f = _index(config.FUNCS_JSONL)
        d = _index(config.DESC_JSONL)
        _FUNCS, _DESC = f, d


def flat_api_h(constants):
    """constants(해석된 CRYPTO_* 정수) → 자립 api.h 문자열. params.h 의존 없음."""
    lines = [f'#define {k} {v}' for k, v in constants.items()]
    return '\n'.join(lines) + '\n'


def bundle(category, algorithm):
    """(category, algorithm) → 입력번들 dict."""
    _load()
    key = (category, algorithm)
    if key not in _FUNCS:
        raise KeyError(f'{key} 가 algorithm_functions.jsonl 에 없음')
    f = _FUNCS[key]
    op = f['operation']
    # A(설명)
    desc = _DESC.get(key)
    if desc is None:
        raise KeyError(f'{key} 설명 없음(algorithm_descriptions.jsonl). '
                       f'pending/no_source 알고리즘일 수 있음.')
    desc_path = os.path.join(config.ROOT, desc['desc_file'])
    description_md = open(desc_path, errors='replace').read()
    # B: entry 프로토타입 verbatim
    entry_prototypes = [PROTO.get(fn, f'extern int {fn}(...);') for fn in f['required_functions']]
    return {
        'category': category,
        'algorithm': algorithm,
        'operation': op,
        'default_impl': f['default_impl'],           # 채점 대상 (op/prim 식별용, LLM엔 안 줌)
        'primitive': f['default_impl'].split('/')[1],
        'description_md': description_md,             # A
        'entry_functions': f['required_functions'],
        'entry_prototypes': entry_prototypes,         # B
        'arg_conventions': for_operation(op),         # B 인자의미
        'constants': f['constants'],                  # 인터페이스 크기(정수)
        'desc_file': desc['desc_file'],
        'desc_chars': len(description_md),
    }


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('category'); ap.add_argument('algorithm')
    a = ap.parse_args()
    b = bundle(a.category, a.algorithm)
    # 설명은 길어서 요약만
    view = dict(b); view['description_md'] = f"<{b['desc_chars']} chars from {b['desc_file']}>"
    print(json.dumps(view, ensure_ascii=False, indent=2))
    print('\n--- flat api.h ---')
    print(flat_api_h(b['constants']))
