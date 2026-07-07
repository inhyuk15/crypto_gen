# cryptoforge

LLM이 **사람이 쓴 스펙 설명(A)** 과 **최소 인터페이스(B)** 만 보고 암호 알고리즘을
C로 구현할 수 있는지 **pass@k**로 측정하는 실험 프레임워크.
채점은 SUPERCOP `do`-part checksum(정답 구현과 출력 바이트가 정확히 일치해야 통과).

> 참조 구현(ref)은 **블랙박스**다. 함수 분해·소스·헤더 시그니처를 생성 파이프라인에
> 절대 넣지 않는다 — 그 분해 자체가 측정 대상이기 때문. LLM엔 A(설명) + B(entry
> 시그니처·인자규약·operation 규약·인터페이스 상수)만 준다.

## 파이프라인

```
bundle  → planner → generate(파일별) → dopart_run(D 채점) → verdict     (×k = pass@k)
[결정론]   [LLM]      [LLM 서브에이전트]   [빌드·실행·체크섬]
```

| 모듈 | 역할 |
|---|---|
| `bundle.py` | [결정론] A(설명)+entry 시그니처+인자규약+상수 조립. ref 소스 미포함 |
| `planner.py` + `prompts/templates/planner.*` | [LLM] 스펙→build plan(파일·함수 시그니처·의존순서) |
| `generate.py` + `prompts/templates/filegen.*` | [LLM] build_order대로 파일 1개씩 생성 |
| `dopart_run.py` | [D] 생성물 컴파일→try 실행→checksum 대조 (SUPERCOP do-part 재현) |
| `runner.py` | 한 알고리즘 bundle→(plan→generate→D)×k → pass@k |
| `batch.py` | 여러 알고리즘 **병렬** pass@k |
| `render.py` | 알고리즘별 실제 프롬프트를 `prompts/<algo>/`에 찍기(검수용) |
| `promptlib.py` | 템플릿 치환 단일 소스(런타임=렌더 동일 프롬프트) |
| `schema.py` | plan JSON 검증 |
| `config.py` | 모델 선택·키 로딩·경로 |

## 준비

1. **API 키** — `cryptoforge/api_key.txt` (.env 스타일, gitignore됨):
   ```
   OPENAI_API_KEY=sk-...
   # 필요시: GEMINI_API_KEY= / ANTHROPIC_API_KEY= / OPENSOURCE_API_KEY= / OPENSOURCE_BASE_URL=
   ```
2. **SUPERCOP 트리** — 기본 경로는 리포 루트의 `supercop-20260330/`.
   다른 위치면 `export CRYPTOFORGE_SUPERCOP=/path/to/supercop`.
3. **모델** — `config.py`의 `MODEL` 한 줄(기본 `gpt-5.4-mini`). provider는 자동 분기.
4. **데이터셋**(리포 루트) — 아래가 있어야 함:
   - `algorithm_functions.jsonl` (entry·상수·operation), `algorithm_descriptions.jsonl` (→스펙 경로)
   - `_spec_cut/`, `_desc/` — desc_file이 가리키는 **실제 스펙 md 본문**(=A/설명)
   - `supercop-20260330/` — SUPERCOP 트리
   - 불필요: `_docs_md`, `pdfs/`, `algorithm_docs.jsonl`(데이터 구축용 중간물)

## 실행

### 한 알고리즘 pass@k
```bash
cd cryptoforge
python3 runner.py crypto_aead ascon96v1 -k 3
python3 runner.py crypto_kem  ntruplus576 -k 3 --model gpt-5.4-mini
```

### 여러 알고리즘 병렬 (권장)
```bash
python3 batch.py crypto_aead/ascon96v1 crypto_kem/ntruplus576 -k 3 --workers 10
python3 batch.py --pick picks.json -k 3 --workers 10
```
`picks.json`: `[{"category":"crypto_aead","algorithm":"ascon96v1"}, ...]`
또는 `["crypto_aead/ascon96v1", ...]`

### 프롬프트만 찍어보기 (LLM 호출 없음)
```bash
python3 render.py crypto_aead ascon96v1     # → prompts/ascon96v1/{planner.md,filegen.md,meta.json}
python3 render.py --pick picks.json
```

### 채점기 단독 실행 / 검증 (ref로 정확성 확인)
```bash
# 생성된 impl 채점
python3 dopart_run.py crypto_aead ascon96v1 runs/ascon96v1/attempt_0/impl
# ref 소스로 known checksum 재현 → 채점기 자체 검증
python3 dopart_run.py crypto_kem hila5 ../supercop-20260330/crypto_kem/hila5/ref
```

### 번들 내용 확인
```bash
python3 bundle.py crypto_aead ascon96v1
```

## 산출물 (`runs/<algorithm>/`, gitignore됨)
```
bundle.json                     # LLM에 준 입력 요약
attempt_<i>/plan.json           # planner 출력
attempt_<i>/impl/*.c *.h api.h  # 생성된 소스
attempt_<i>/impl/.prompts/*.md  # 파일별 실제 프롬프트(디버깅)
attempt_<i>/verdict.json        # 채점 결과 + 에러
summary.json                    # pass@k 집계
```

## verdict 유형
| verdict | 의미 |
|---|---|
| `PASS` | 바이트까지 정확 (checksum 일치) |
| `IMPL_COMPILE_FAIL` | 생성 C가 컴파일 안 됨 |
| `LINK_FAIL` | 심볼 불일치(entry/헬퍼 함수 정의 누락 등) |
| `RUN_FAIL` | 컴·링크는 됐으나 자기정합 실패(enc/dec 왕복 등) |
| `RUN_TIMEOUT` | try가 제한시간 내 미종료(무한루프). 기본 300s, `CRYPTOFORGE_RUN_TIMEOUT`으로 조정 |
| `CHECKSUM_MISMATCH` | 돌지만 바이트가 정답과 다름(엔디안·패딩·상수 등) |
| `SUPPORT_FAIL`/`PIPELINE_ERROR` | 하네스/파이프라인 오류(모델 무관) |

## 환경변수
- `CRYPTOFORGE_SUPERCOP` — SUPERCOP 트리 경로 (기본 `<repo>/supercop-20260330`)
- `CRYPTOFORGE_RUN_TIMEOUT` — try 1회 실행 상한 초 (기본 300)

## 참고
- **키드 op**(kem/sign/encrypt/dh/box/scalarmult)은 결정적 `randombytes`(chacha20
  knownrandombytes 스택)를 자동 링크해 채점 — 이게 있어야 checksum이 재현된다.
- 데이터셋은 리포 루트의 `algorithm_functions.jsonl`, `algorithm_descriptions.jsonl` 사용.
