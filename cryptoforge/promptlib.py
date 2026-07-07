#!/usr/bin/env python3
"""프롬프트 조립 단일 소스.

planner.py / generate.py(런타임) 와 render.py(prompts/<algo>/ 찍기)가 모두 여기를 쓴다.
=> 디스크에 렌더된 프롬프트 == 실제로 모델에 보내는 프롬프트 (불일치 원천 제거).

템플릿: prompts/templates/{planner,filegen}.{system,user}.md  (placeholder = {{NAME}})
operation별 고려사항: prompts/operation_notes.py
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prompts.operation_notes import for_operation as _op_notes

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPL = os.path.join(HERE, 'prompts', 'templates')


def _t(name):
    return open(os.path.join(TEMPL, name)).read()


def _fill(tpl, mapping):
    """{{NAME}} 치환. 미치환 placeholder 있으면 에러(오타/누락 조기검출)."""
    def rep(m):
        k = m.group(1)
        if k not in mapping:
            raise KeyError(f'template placeholder {{{{{k}}}}} 값 없음')
        return str(mapping[k])
    out = re.sub(r'\{\{(\w+)\}\}', rep, tpl)
    leftover = re.findall(r'\{\{(\w+)\}\}', out)
    if leftover:
        raise KeyError(f'미치환 placeholder: {leftover}')
    return out


def _constants_block(bundle):
    return '\n'.join(f'#define {k} {v}' for k, v in bundle['constants'].items())


# ── planner ────────────────────────────────────────────────────────────
def planner_system(bundle):
    return _t('planner.system.md')


def planner_user(bundle):
    return _fill(_t('planner.user.md'), {
        'ALGORITHM': bundle['algorithm'],
        'OPERATION': bundle['operation'],
        'ENTRY_PROTOTYPES': '\n'.join(bundle['entry_prototypes']),
        'ARG_CONVENTIONS': bundle['arg_conventions'] or '(none)',
        'OPERATION_NOTES': _op_notes(bundle['operation']),
        'CONSTANTS': _constants_block(bundle),
        'SPEC': bundle['description_md'],
    })


# ── filegen ────────────────────────────────────────────────────────────
def filegen_system(bundle):
    return _t('filegen.system.md')


def plan_summary(plan):
    lines = []
    for f in plan['files']:
        fns = '; '.join(pf['signature'] for pf in f.get('provides_functions', []) or [])
        mac = ', '.join(f.get('provides_macros', []) or [])
        lines.append(f"- {f['path']} ({f['kind']}): {f.get('role', '')}")
        if mac:
            lines.append(f"    macros: {mac}")
        if fns:
            lines.append(f"    functions: {fns}")
    return '\n'.join(lines)


def _dep_blocks(fmeta, generated):
    blocks = []
    for d in fmeta.get('depends_on', []) or []:
        if d in generated:
            blocks.append(f'### {d} (already implemented)\n```c\n{generated[d]}```')
    return '\n\n'.join(blocks) if blocks else '(none)'


def filegen_user(bundle, plan, fmeta, generated):
    fns = '\n'.join(f"- {pf['signature']}   // {pf.get('purpose', '')}"
                    for pf in fmeta.get('provides_functions', []) or [])
    return _fill(_t('filegen.user.md'), {
        'ALGORITHM': bundle['algorithm'],
        'OPERATION': bundle['operation'],
        'PLAN_SUMMARY': plan_summary(plan),
        'OPERATION_NOTES': _op_notes(bundle['operation']),
        'CONSTANTS': _constants_block(bundle),
        'DEP_FILES': _dep_blocks(fmeta, generated),
        'TARGET_PATH': fmeta['path'],
        'TARGET_KIND': fmeta['kind'],
        'TARGET_ROLE': fmeta.get('role', ''),
        'TARGET_MACROS': ', '.join(fmeta.get('provides_macros', []) or []) or '(none)',
        'TARGET_FUNCTIONS': fns or '(none — header/decls only as planned)',
        'SPEC': bundle['description_md'],
    })


def filegen_context(bundle):
    """plan 없이 렌더 가능한 filegen '공통 문맥' — prompts/<algo>/filegen.md 용.
    (실제 per-file user 는 여기에 TARGET/DEP 섹션이 런타임에 덧붙는다.)"""
    return _fill(
        "## Operation notes (I/O contract enforced by the checksum)\n{{OPERATION_NOTES}}\n\n"
        "## Interface constants (available via #include \"api.h\")\n{{CONSTANTS}}\n\n"
        "## Specification (source of algorithm logic)\n{{SPEC}}\n",
        {'OPERATION_NOTES': _op_notes(bundle['operation']),
         'CONSTANTS': _constants_block(bundle),
         'SPEC': bundle['description_md']})
