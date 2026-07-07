#!/usr/bin/env python3
"""plan.json 스키마 검증 (외부 의존 없음).

plan 구조:
{
  "files": [
    {"path": "params.h", "kind": "header", "role": "...",
     "provides_functions": [{"signature": "...", "purpose": "..."}],
     "provides_macros": ["NAME", ...],
     "depends_on": ["other.h", ...]}
  ],
  "build_order": ["params.h", ..., "aead.c"]     // files의 위상정렬(순열)
}
"""
import re


def _fn_name(sig):
    m = re.search(r'\b(crypto_\w+)\s*\(', sig)
    if m: return m.group(1)
    m = re.search(r'\b([A-Za-z_]\w*)\s*\(', sig)
    return m.group(1) if m else ''


def validate_plan(plan, bundle):
    """(ok: bool, errors: [str]). bundle의 entry 함수가 어느 파일엔가 있어야 함."""
    errs = []
    if not isinstance(plan, dict):
        return False, ['plan is not an object']
    files = plan.get('files')
    order = plan.get('build_order')
    if not isinstance(files, list) or not files:
        errs.append('files[] 없음/빈값')
        return False, errs
    if not isinstance(order, list):
        errs.append('build_order[] 없음')

    paths = []
    for i, f in enumerate(files):
        if not isinstance(f, dict):
            errs.append(f'files[{i}] object 아님'); continue
        p = f.get('path')
        if not p or not isinstance(p, str):
            errs.append(f'files[{i}].path 없음'); continue
        paths.append(p)
        if f.get('kind') not in ('header', 'source'):
            errs.append(f'{p}: kind 는 header|source')
        if not p.endswith(('.c', '.h', '.cc', '.cpp', '.inc')):
            errs.append(f'{p}: 확장자 이상')
        for d in f.get('depends_on', []) or []:
            pass  # 존재검사는 아래에서
        for pf in f.get('provides_functions', []) or []:
            if not isinstance(pf, dict) or 'signature' not in pf:
                errs.append(f'{p}: provides_functions 항목에 signature 필요')

    pathset = set(paths)
    if len(pathset) != len(paths):
        errs.append('중복 path 존재')

    # 빌드시스템이 제공하는 외부 헤더(=plan 파일 아님). 의존 선언 허용.
    external = {'api.h', f'crypto_{bundle["operation"]}.h'}

    # depends_on 참조 무결성 (외부 제공 헤더는 허용)
    for f in files:
        for d in f.get('depends_on', []) or []:
            if d not in pathset and d not in external:
                errs.append(f'{f.get("path")}: depends_on 미존재 파일 {d}')

    # build_order = paths 순열 + 위상 일관성 (외부 헤더는 양쪽에서 무시 — 모델이
    # api.h/crypto_<op>.h 를 files 에 넣어도 빌드가 제공하므로 관용)
    if isinstance(order, list):
        order = [x for x in order if x not in external]
        internal = pathset - external
        if set(order) != internal:
            errs.append('build_order 가 files 집합과 불일치')
        else:
            pos = {p: i for i, p in enumerate(order)}
            for f in files:
                for d in f.get('depends_on', []) or []:
                    if d in pos and pos[d] > pos[f['path']]:
                        errs.append(f'build_order 위상오류: {f["path"]} 가 의존 {d} 보다 앞')

    # 소스파일(.c/.cc/.cpp) 최소 1개
    if not any(p.endswith(('.c', '.cc', '.cpp')) for p in paths):
        errs.append('컴파일 소스(.c/.cc/.cpp)가 없음')

    # entry 함수 커버리지
    provided = set()
    for f in files:
        for pf in f.get('provides_functions', []) or []:
            provided.add(_fn_name(pf.get('signature', '')))
    for fn in bundle['entry_functions']:
        if fn not in provided:
            errs.append(f'entry 함수 {fn} 를 어느 파일도 제공하지 않음')

    return (len(errs) == 0), errs
