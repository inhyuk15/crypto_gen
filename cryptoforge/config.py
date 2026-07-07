#!/usr/bin/env python3
"""cryptoforge 설정 — 모델 선택 / 키 로딩 / 경로.

모델 교체는 여기 MODEL 한 줄만 바꾸면 됨. provider(키·base_url)는 자동 분기.
키는 api_key.txt(.env 스타일)에서 로드 (gitignore됨).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # repo 루트
HERE = os.path.dirname(os.path.abspath(__file__))                    # cryptoforge/
SUPERCOP = os.environ.get('CRYPTOFORGE_SUPERCOP', os.path.join(ROOT, 'supercop-20260330'))
KEYFILE = os.path.join(HERE, 'api_key.txt')
RUNS = os.path.join(HERE, 'runs')

# 데이터셋(기존 산출물)
DESC_JSONL  = os.path.join(ROOT, 'algorithm_descriptions.jsonl')
FUNCS_JSONL = os.path.join(ROOT, 'algorithm_functions.jsonl')
DOCS_JSONL  = os.path.join(ROOT, 'algorithm_docs.jsonl')

# ── 현재 실험 대상 모델 ─────────────────────────────────────────────
MODEL = 'gpt-5.4-mini'         # ← 교체 지점 (나중에 gemini/claude/qwen)

# 샘플링 / pass@k
K = 5                          # 시도 수 (pass@k)
TEMPERATURE = 1.0              # 다양성 위해 >0
MAX_OUTPUT_TOKENS = 16000
REQUEST_TIMEOUT = 300
MAX_RETRIES = 4
GEN_CONCURRENCY = 4            # 파일 생성 서브에이전트 동시성

# ── provider 레지스트리 ─────────────────────────────────────────────
# model 이름 → provider. provider → (키 이름, base_url[, base_url 환경키])
MODEL_PROVIDER = {
    'gpt-5.4-mini': 'openai',
    'gpt-5.4-nano': 'openai',
    'gpt-5.4':      'openai',
    # 나중에: 'gemini-2.x': 'gemini', 'claude-*': 'anthropic', 'qwen*': 'opensource'
}
PROVIDERS = {
    'openai':     {'key': 'OPENAI_API_KEY',     'base_url': None},  # 표준 OpenAI
    'gemini':     {'key': 'GEMINI_API_KEY',
                   'base_url': 'https://generativelanguage.googleapis.com/v1beta/openai/'},
    'anthropic':  {'key': 'ANTHROPIC_API_KEY',  'base_url': 'https://api.anthropic.com/v1/'},
    'opensource': {'key': 'OPENSOURCE_API_KEY',  'base_url_key': 'OPENSOURCE_BASE_URL'},
}


def load_keys(path=KEYFILE):
    """api_key.txt(.env 스타일) → dict. '#'·빈 줄 무시."""
    d = {}
    if not os.path.isfile(path):
        return d
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        d[k.strip()] = v.strip()
    return d


def resolve(model=None):
    """model → {model, provider, api_key, base_url}. 키 없으면 에러."""
    model = model or MODEL
    prov = MODEL_PROVIDER.get(model)
    if prov is None:
        raise ValueError(f'모델 {model!r}의 provider 미등록 (config.MODEL_PROVIDER에 추가).')
    spec = PROVIDERS[prov]
    keys = load_keys()
    api_key = keys.get(spec['key'], '')
    if not api_key:
        raise ValueError(f'{spec["key"]} 가 api_key.txt 에 비어있음.')
    base_url = spec.get('base_url')
    if 'base_url_key' in spec:
        base_url = keys.get(spec['base_url_key']) or base_url
    return {'model': model, 'provider': prov, 'api_key': api_key, 'base_url': base_url}
