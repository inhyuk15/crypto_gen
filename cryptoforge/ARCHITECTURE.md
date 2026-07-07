# cryptoforge — 아키텍처 개요

> **목적**: LLM이 암호 알고리즘의 **사람 설명(A)만** 보고 실제로 구현할 수 있는가를 측정.
> LLM이 만든 소스파일들을 SUPERCOP **do-part checksum**으로 채점 → **pass@k**.
> 첫 대상 모델 = **gpt-5.4mini** (나중에 qwen 등 교체 가능하게 설계).

---

## 0. 한 장 요약 — 파이프라인과 A/B/C/D

```
 알고리즘 하나(예: crypto_aead/ascon128v12)
   │
   ▼  [bundle.py] 결정론적 입력번들 조립 (LLM 비개입)
 ┌──────────────────────────────────────────────┐
 │ A = 설명(md)   B = entry 시그니처+인자규약     │  ← LLM에게 주는 전부
 │ + 인터페이스 크기 상수(정수)                    │
 └──────────────────────────────────────────────┘
   │
   ▼  [planner.py] (LLM 호출 1회)  = B, C
 ┌──────────────────────────────────────────────┐
 │ plan: 어떤 파일에 어떤 함수/매크로가 있어야 하나 │
 │        + 구현 순서(의존성 위상)                 │
 └──────────────────────────────────────────────┘
   │
   ▼  [generate.py] (LLM 서브에이전트 N개, 의존순서대로)
 ┌──────────────────────────────────────────────┐
 │ 각 파일을 구현 (그 파일의 함수 시그니처 + 이미  │
 │ 만든 의존파일들을 문맥으로 줌) → 파일 내용      │
 └──────────────────────────────────────────────┘
   │
   ▼  [generate.py] 조립 → impl 디렉토리 + flat api.h(합성)
   │
   ▼  [dopart_run.py] = D  ✅이미 완성·검증됨
 ┌──────────────────────────────────────────────┐
 │ 네임스페이스 컴파일 → try 실행 → checksum 대조 │
 │            → PASS / FAIL                       │
 └──────────────────────────────────────────────┘
   │
   ▼  [runner.py] k회 반복 → pass@k, 실패원인 분류, 로그
```

- **A** = 설명(입력). **B** = 필수 함수 시그니처(계약). **C** = 구현 계획/순서(planner 산출).
- **D** = 채점기(생성파일 경로들을 받아 컴파일+do-part). **이미 만들어 ref 4개로 검증 완료.**
- do-part 도착점 = "생성된 파일 경로들" — 정확히 사용자가 말한 구조.

---

## 1. 폴더 구조

```
cryptoforge/
├── ARCHITECTURE.md      ← 이 문서 (구현 전 개요)
├── api_key.txt          ← 사용자가 API 키 붙여넣기 (gitignore됨)
├── .gitignore           ← api_key.txt, runs/ 제외
│
├── config.py            ← 모델/엔드포인트/k/경로 설정 (gpt-5.4mini 기본)
├── llm.py               ← LLM 클라이언트 (OpenAI 호환; 모델 교체 지점)
│
├── bundle.py            ← [결정론] 입력번들 조립 (A + entry + 상수 + flat api.h)
├── schema.py            ← plan JSON 스키마 / 검증
├── planner.py           ← [LLM] 번들 → plan(파일·함수·순서)
├── generate.py          ← [LLM] 파일별 생성(의존순서) → impl 디렉토리 조립
├── dopart_run.py        ← [D] 채점기 (컴파일+do-part+checksum)   ✅완성
├── runner.py            ← 오케스트레이터: bundle→plan→generate→score, pass@k, 로깅
│
├── prompts/
│   ├── planner.md       ← planner 프롬프트 템플릿
│   ├── filegen.md       ← 파일 구현 서브에이전트 템플릿
│   └── arg_conventions.py ← operation→인자의미 매핑 (HARNESS_CONTRACT §2)
│
└── runs/                ← 산출물 (알고리즘/시도별 plan·생성소스·로그·verdict)
    └── <algorithm>/attempt_<k>/
        ├── bundle.json      # 이 시도에 준 입력
        ├── plan.json        # planner 산출
        ├── impl/            # 생성된 소스 + flat api.h  (D의 입력)
        ├── dopart.log       # 컴파일/실행 로그
        └── verdict.json     # PASS/FAIL + checksum + 실패원인
```

---

## 2. 각 모듈 책임 (입력 → 출력)

### `config.py`
- 모델명(`gpt-5.4mini`), API base_url, `api_key.txt` 경로, 동시성, k(샘플수), supercop 경로.
- 모델 교체는 여기 한 곳(+llm.py)만 바꾸면 qwen 등으로.

### `llm.py`  — LLM 클라이언트
- `complete(system, user, **opts) -> str` 단일 인터페이스. OpenAI 호환 chat completions.
- 재시도/타임아웃/토큰수 로깅. 모델-특화 부분 격리(gpt-5.4mini → 나중에 qwen 엔드포인트).

### `bundle.py`  — [결정론, LLM 비개입] 입력번들
- 입력: `(category, algorithm)`.
- 조인: `algorithm_descriptions.jsonl`(A) + `algorithm_functions.jsonl`(entry, constants) +
  `prompts/arg_conventions`(인자의미).
- 출력: `bundle.json` = { description_md(A), entry_prototypes[], arg_conventions, constants{}, meta }.
- **raw api.h/params.h는 안 넣음** (내부 설계수치 누출 방지 — HARNESS_CONTRACT 참조).

### `planner.py`  — [LLM] plan 생성 (B, C)
- 입력: bundle. 프롬프트: `prompts/planner.md`.
- 출력: `plan.json` (schema.py로 검증). 구조:
  ```json
  {
    "files": [
      {"path":"params.h","kind":"header","role":"상수/매크로",
       "provides_macros":["..."],"provides_functions":[],"depends_on":[]},
      {"path":"permutation.h","kind":"header","role":"...",
       "provides_functions":[{"signature":"static void P(...)","purpose":"..."}],
       "depends_on":["params.h"]},
      {"path":"aead.c","kind":"source","role":"entry",
       "provides_functions":[{"signature":"int crypto_aead_encrypt(...)","purpose":"...","entry":true}],
       "depends_on":["params.h","permutation.h"]}
    ],
    "build_order": ["params.h","permutation.h","aead.c"]   // 위상정렬
  }
  ```
- **제약**: entry 함수 시그니처는 B 그대로(글자단위). 상수/매크로 헤더처럼 다수가 의존하는 파일은
  build_order 앞쪽. planner가 스스로 분해 설계(ref 안 봄).

### `generate.py`  — [LLM 서브에이전트] 파일 구현 + 조립
- `build_order` 순서로 각 파일 1개씩(의존 없는 것끼리는 병렬 가능).
- 각 서브에이전트 입력: A(설명) + plan 요약 + **이미 생성된 의존파일 전체 내용** + 이 파일의
  함수 시그니처/역할. 프롬프트: `prompts/filegen.md`. 출력: 그 파일의 완전한 소스.
- 전부 끝나면 `runs/.../impl/`에 파일들 배치 + **flat api.h 합성**(constants의 정수만).

### `dopart_run.py`  — [D] 채점기  ✅완성·검증
- 입력: `(op, primitive, impl_dir)`. impl_dir = generate가 만든 폴더.
- SUPERCOP 3층 네임스페이스로 컴파일 → try-small/try 실행 → checksumsmall/big 대조.
- 출력: verdict(PASS / IMPL_COMPILE_FAIL / LINK_FAIL / RUN_FAIL / CHECKSUM_MISMATCH) + checksum.
- **검증됨**: ascon128v12·acorn128v3·aegis128l·blake2b ref = 전부 PASS.

### `runner.py`  — 오케스트레이터
- `run(category, algorithm, k)`: bundle 1회 → (plan → generate → D) 를 k회 독립 샘플.
- 1회 이상 PASS면 pass@k 성공. 실패원인 카테고리 집계. `runs/`에 전부 저장.
- 배치 모드: 알고리즘 리스트 받아 반복.

---

## 3. 데이터 흐름 (한 시도)

```
bundle.py(cat,algo) → bundle.json
   → planner.py(bundle.json) → plan.json
      → generate.py(plan.json, bundle) → impl/ (+flat api.h)
         → dopart_run.py(op,prim,impl/) → verdict.json
runner.py 가 위를 k회 돌리고 pass@k 집계
```

---

## 4. 기존 산출물 재사용 (조인 소스)

| 필요 | 파일 | 필드 |
|---|---|---|
| A (설명) | `algorithm_descriptions.jsonl` | `desc_file` |
| entry 함수·상수 | `algorithm_functions.jsonl` | `required_functions`, `constants` |
| 인자 의미 | (신규) `prompts/arg_conventions` | operation별 표준 규약 |
| 정답 checksum | `supercop-.../<op>/<prim>/checksum{small,big}` | — |

계약 상세는 [HARNESS_CONTRACT.md](../HARNESS_CONTRACT.md).

---

## 5. 구현 상태 / 순서

| 모듈 | 상태 |
|---|---|
| `dopart_run.py` (D) | ✅ 완성·검증 |
| `config.py`, `llm.py` | ⬜ 다음 |
| `bundle.py`, `prompts/arg_conventions` | ⬜ |
| `prompts/planner.md`, `planner.py`, `schema.py` | ⬜ |
| `prompts/filegen.md`, `generate.py` | ⬜ |
| `runner.py` | ⬜ |

**파일럿 목표**: `ascon128v12`로 A만 주고 end-to-end 1회 → D가 채점. (D 검증 완료된 알고리즘이라
파이프라인이 옳으면 결과 해석이 깨끗함.)

---

## 6. 알려진 리스크

- **교차-primitive 의존**: 일부 ref(sha256 등)는 외부 primitive(`crypto_hashblocks_*`)를 include →
  자기완결 아님. D는 현재 자기완결만 통과. 파일럿은 자기완결 알고리즘부터.
- **A의 완전성**: 설명이 핵심값을 빠뜨리면 재구현 불가 — 실패원인에서 "LLM 실력"과 구분해 관측.
- **checksum이 스펙 밖 직렬화 규약 요구**: 표준화 덜 된 제출물은 실험 부적합으로 분류(파일럿 후 기준).
- 상세: [HARNESS_CONTRACT.md](../HARNESS_CONTRACT.md) §6.
```
