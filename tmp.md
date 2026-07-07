# 알고리즘 description 커버리지 현황

> **유니버스 = 1157개** (`target_crypto.jsonl` = `algorithm_docs.jsonl`의 category+algorithm 행 수).
> "1400+"로 기억하는 건 SUPERCOP의 **구현체(implementation) 수**이거나 파라미터셋을 더 잘게 센 집계일 수 있음 — 우리가 문서를 매핑한 타깃셋은 1157개.

## 1. 전체 상태 한눈에

| 상태 | 뜻 | 개수 | 비율 |
|---|---|---:|---:|
| ✅ **described (whole_doc)** | P: 파라미터 변형 → 문서 스펙컷 통째 공유 | 612 | 52.9% |
| ✅ **described (attributed)** | M: 한 문서 속 별개 구성 → 알고리즘별 슬라이스 | 462 | 39.9% |
| ⏳ prose_pending | spec 헤딩 없는 산문/RFC/코드 문서(26개) 소속 | 55 | 4.8% |
| ⏳ nospec_pending | 스펙 자체가 빈약한 문서(3개) 소속 | 18 | 1.6% |
| ❌ no_doc | 문서 링크 자체가 없음 | 7 | 0.6% |
| ❌ excluded_mismap | 오매핑(mcssha→무관한 공격논문) | 3 | 0.3% |
| | | | |
| **✅ 커버 합계** | | **1074** | **92.8%** |
| **⏳ 후속 대상** | prose + nospec | **73** | **6.3%** |
| **❌ 원천 없음** | no_doc + 오매핑 | **10** | **0.9%** |

## 2. 카테고리별

| category | ✅ covered | ⏳ pending | ❌ no_source | total | 커버율 |
|---|---:|---:|---:|---:|---:|
| crypto_aead | 487 | 11 | 0 | 498 | 97.8% |
| crypto_sign | 178 | 8 | 0 | 186 | 95.7% |
| crypto_kem | 157 | 0 | 1 | 158 | 99.4% |
| crypto_hash | 67 | 17 | 6 | 90 | 74.4% |
| crypto_core | 54 | 0 | 0 | 54 | 100% |
| crypto_encode | 41 | 0 | 0 | 41 | 100% |
| crypto_encrypt | 36 | 1 | 1 | 38 | 94.7% |
| crypto_decode | 35 | 0 | 0 | 35 | 100% |
| crypto_verify | 0 | 16 | 0 | 16 | 0% |
| crypto_stream | 5 | 7 | 1 | 13 | 38.5% |
| crypto_dh | 7 | 3 | 0 | 10 | 70.0% |
| crypto_auth | 0 | 3 | 1 | 4 | 0% |
| crypto_hashblocks | 3 | 1 | 0 | 4 | 75.0% |
| crypto_rng | 2 | 1 | 0 | 3 | 66.7% |
| crypto_box | 0 | 2 | 0 | 2 | 0% |
| crypto_secretbox | 0 | 2 | 0 | 2 | 0% |
| crypto_onetimeauth | 1 | 0 | 0 | 1 | 100% |
| crypto_scalarmult | 1 | 0 | 0 | 1 | 100% |
| crypto_xof | 0 | 1 | 0 | 1 | 0% |
| **합계** | **1074** | **73** | **10** | **1157** | **92.8%** |

## 3. 남은 것 해석

- **⏳ pending 73개**: 이번 작업(spec 헤딩 있는 254문서)에서 제외한 문서군. spec은 대부분 존재하지만 헤딩으로 구획이 안 돼(RFC 평문·산문 논문·코드 README) 자동 절단이 위험 → 다음 단계에서 "문서 통째 유지" 또는 사람 트림으로 처리.
  - `crypto_verify`(16), `crypto_box`/`crypto_secretbox`(각 2), `crypto_xof`(1) 등이 0%인 건 대부분 이 pending에 몰려있어서지 실패가 아님 (NaCl thin 문서·RFC 등).
- **❌ no_source 10개**: description을 만들 원천이 없음.
  - no_doc 7: auth/zero, encrypt/cargocult2048, hash/atelopus32·64, hash/clxhash, kem/timer, stream/amastrid
  - 오매핑 3: hash/mcssha4·5·6 (doc_link이 무관한 Dynamic SHA 공격논문 — **수집단계 링크 확인 필요**)

## 4. 산출물 파일 (A = description)
- `algorithm_descriptions.jsonl` — 1074행 인덱스 (알고리즘 → desc_file)
- `_spec_cut/` — 254문서 규칙기반 절단본 | `_desc/` — M문서 알고리즘별 슬라이스
- `_m_out/` — subagent 귀속결과 56 JSON (감사용) | `description_exceptions.jsonl` — 오매핑 3

---

## 5. B-(인터페이스): 알고리즘별 필수 함수 — **1157/1157 (100%)**

do-part 테스트가 돌려면 각 알고리즘 ref가 반드시 export해야 하는 함수 + 인터페이스 상수를
SUPERCOP 소스에서 **결정론적으로**(LLM 비개입) 추출. description(A)과 달리 문서가 아니라 SUPERCOP
구현에서 나오므로 **pending·no_source 포함 전 알고리즘 100% 커버**.

| operation | 필수 함수 | 알고리즘 수 |
|---|---|---:|
| aead | `crypto_aead_encrypt`, `crypto_aead_decrypt` | 498 |
| sign | `crypto_sign_keypair`, `crypto_sign`, `crypto_sign_open` | 186 |
| kem | `crypto_kem_keypair`, `crypto_kem_enc`, `crypto_kem_dec` | 158 |
| hash | `crypto_hash` | 90 |
| core | `crypto_core` | 54 |
| encode / decode | `crypto_encode` / `crypto_decode` | 41 / 35 |
| encrypt | `crypto_encrypt_keypair`, `crypto_encrypt`, `crypto_encrypt_open` | 38 |
| verify | `crypto_verify` | 16 |
| stream | `crypto_stream`, `crypto_stream_xor` | 13 |
| dh | `crypto_dh_keypair`, `crypto_dh` | 10 |
| auth / onetimeauth | `…`, `…_verify` | 4 / 1 |
| hashblocks / rng / xof / scalarmult | 각 operation 함수 | 4 / 3 / 1 / 1 |
| secretbox / box | `…`, `…_open` / 6개(keypair·box·open·beforenm·afternm·open_afternm) | 2 / 2 |

- 필수 함수 분포: **1함수 244 / 2함수 529 / 3함수 382 / 6함수 2**
- 인터페이스 상수(KEYBYTES·PUBLICKEYBYTES·BYTES·CIPHERTEXTBYTES 등): 각 `api.h`를 C 전처리기로 실제
  정수 해석 → **1157개 전부 해석 성공**(kyber params.h, gemss libkeccak, CROSS/fslwe sizeof·수식 포함).

### 산출물 (B)
- `algorithm_functions.jsonl` — 1157행 (category+algorithm → funcs_file, required_functions, constants)
- `_funcs/<category>__<algorithm>.md` — 알고리즘마다 필수 함수 시그니처 + api.h 상수(값+원문)
- `algorithm_docs.jsonl` — 기존 파일에 **`funcs_file` 컬럼 추가**(쉽게 조인)
