# 실험 설계: "최소 명세로 LLM이 암호 알고리즘을 구현할 수 있는가"

## 0. 큰 그림 (연구 목표)

LLM에게 어떤 암호 알고리즘을 구현하라고 시켰을 때, **정말로 구현해내는가**를 측정한다.
정답 판정은 SUPERCOP의 동작 테스트(do-part / checksum)로 한다.

최종적으로 LLM에게 전달되는 프롬프트 = **A + B** 의 조합.

- **A** — 그 알고리즘이 "무엇을 하는 알고리즘인지"에 대한 **원저자(사람)가 쓴 설명**.
  (지금까지 모아온 `target_crypto_documentation.jsonl` 의 `doc_link` 들이 A의 원천)
- **B** — do-part 테스트를 통과하기 위해 구현해야 하는 **인터페이스/함수 명세** (SUPERCOP에서 결정론적으로 추출 가능, **나중에** 다룸)

**지금 당장 할 것 = A.**

---

## 1. 절대 원칙: 데이터셋 생성 단계에 LLM 비개입

- A(설명)를 **LLM이 요약/작성하면 안 된다.** 그러면 "LLM이 스펙만 보고 구현할 수 있나?"라는
  실험 자체가 오염된다.
- 경계선: **데이터셋을 만드는 단계**에는 LLM이 들어가면 안 됨.
  (테스트 시점에 피험자 LLM이 원문/명세를 읽는 것은 실험 그 자체이므로 무방)
- 원칙 정련(v2): **LLM은 "추출/선별(어느 원문 구간이 어느 알고리즘의 스펙인가)"까지는 허용**하되,
  **"작성(요약·재서술·원문에 없는 내용 추가)"은 금지**한다. 즉 서브에이전트는 헤딩 경계(번호)만
  고르고, 최종 description은 그 경계로 **원문을 그대로(verbatim) 슬라이스**한 것이어야 한다.
  A의 실제 텍스트는 100% 원저자 문장이고, LLM은 "가위" 역할만 한다.

---

## 2. A를 "통째로 넣지 않는" 이유

- 스펙 문서엔 구현에 불필요한 내용(보안증명, 벤치마크, 동기, 관련연구 등)이 너무 많다 → 비효율.
- 애초에 full implementation에 필요한 **모든** 정보를 문서가 다 담지도 못한다.
- 다 준다고 되는 것도 아니다 — 결국 모델이 그 알고리즘(혹은 유사한 것)을
  **사전지식**으로 아느냐가 성패를 가른다.
- 그러므로 실험의 본질 = **핵심(진짜 필요한 최소 정보)만 주고 구현시켰을 때 만들어내는가.**

→ A의 목표는 "문서 전체"가 아니라 **"구현을 유도하는 핵심 명세만 추린 것"**,
그리고 그 선별을 **LLM 없이** 하는 것.

---

## 3. "핵심"의 세 갈래

### (1) Trivial하지만 필수인 구현 파라미터
- 예: fixed/floating point 여부, int 비트폭, endianness, 워드 크기 등.
- 알고리즘 로직은 아니지만, 안 주면 LLM이 제멋대로 가정해서 틀린다.
- **알고리즘별로 이게 무엇인지 확정해서 줘야 한다.**

### (2) 알고리즘 그 자체 (수도코드 또는 그에 준하는 설명)
- 논리: "C로 구현 가능 = 수도코드로 환원 가능".
- 이상적으론 수도코드, 없으면 그에 준하는 서술.
- 명시적 수도코드가 문서에 있는 경우는 많지 않을 것으로 예상.

### (3) 파트 분해 + 각 파트의 핵심도(criticality) 판정  *(아직 미결 — 나중에)*
- 알고리즘은 여러 파트로 나뉜다. 하나라도 안 주면 실패할 수 있다.
- 예) algorithm1 = {A, B, C}, B가 본질·A/C는 부차적 → **B만 구현해도 "구현했다" 주장 가능** (토큰↓, 난이도↓)
- 예) algorithm2 = {D, F, G}, 셋 다 본질 → **전부 구현해야 인정** (난이도↑)
- 즉 "어디까지가 필수 구현 범위인가"를 알고리즘별로 정하는 것이 실험의 핵심 변수.

---

## 4. 채점 구도: ref 대상 fill-in-the-blank

- 채점 하니스 = **ref의 default implementation을 그대로 두고, 도려낼 부분(B)만 제거한 것.**
- LLM은 그 빈칸(B)만 채운다. 나머지(A·C)는 원본 ref 코드가 채워준다.
- do-part checksum은 전체(A + LLM의 B + C)로 돌리므로, B만 맞으면 통과
  → "부분 구현 인정" 기준과 채점이 정합적.
- 도려내는 범위를 넓히면 난이도↑, 좁히면 난이도↓.

### 이 구도가 주는 이점
- **긴장① 완화**: 파트 A/B/C가 추상 개념이 아니라 **ref 코드 안의 실제 함수/블록**으로 구체화됨.
  → "무엇이 핵심인가"를 순수 판단이 아니라 **코드 구조**에 근거해 정할 여지가 생김
    (보일러플레이트=부차 / 알고리즘 심장부=핵심).
- **A의 범위 자동 축소**: LLM이 주변 ref 코드·시그니처·상수를 문맥으로 이미 보므로,
  A는 "전체 설명"이 아니라 **"도려낸 B를 채우는 데 필요한 명세"** 로 한정됨.
  trivial 파라미터도 상당수는 주변 코드에 이미 드러나 있음.

---

## 5. 남은 미결 문제 (open questions)

- **긴장① (핵심도 판정을 누가/무엇을 근거로 하나)**: 파트 분해와 핵심/부차 판단은 전문가 판단.
  LLM에게 시키면 비개입 원칙이 깨짐. 근거를 코드 구조/메트릭(콜그래프, 표준 라이브러리 의존도)로
  얼마나 결정론적으로 잡을 수 있는지 탐구 필요. → **3번과 함께 나중에.**
- **B의 경계(어디를 도려낼지)를 사람이 정할지, 규칙으로 자동화할지.** 실험 규모·난이도를 좌우.

---

## 6. 현재 진행 상태 / 다음 단계

- [x] 각 알고리즘의 설명 문서 링크 수집 → `target_crypto_documentation.jsonl` (1157행, 1150 success / 7 not_found)
- [x] **문서 → 마크다운 전수 변환** (LLM 없이, `pymupdf4llm`/trafilatura). 1150행 중 유니크 283문서
  - 결과: **1150행 전부 마크다운 확보(무효 0)**. 풀스펙 1146행(99.7%). 나머지 4행도 실질 커버: hector(짧지만 완전한 스펙), floppsy·discohash(형식 스펙 없는 비공식 해시라 README가 유일 문서). 문서 원문: `_docs_md/`
  - **얇은 꼬리 재검색**: README/랜딩/벤치마크/유료 페이지를 doc_link으로 잘못 갖던 22문서(78행)를 재조사 → 19문서/74행을 진짜 스펙으로 교체(github raw, NIST 제출 zip, 웨이백 SHA-3 제출본, minrank 무료판 등). 병렬 리서치 에이전트 3개 사용. 스크립트: `_fix_github.py` 등
  - 파이프라인: `_convert_pipeline.py`(전수) → arxiv `/pdf/`·github README 복구 → `_convert_manual2.py`(브라우저 차단 eprint 등 수동 PDF 21개) → 대체출처 복구 → `_regen_report.py`(리포트 재생성)
  - 대체출처 복구 사례(데이터셋 원래 링크가 죽거나 철회/차단된 경우): GeMSS=NIST `GeMSS-Round3.zip` 내부 spec.pdf(lip6 다운), ntruees=웨이백 EESS#1 v2(eprint 2008/361 철회), HERON=웨이백 NIST round-1 spec(csrc & 파일명 접속불가)
  - **수식 손실 없음** 확인. GARBLE 플래그(39행/11문서)는 합자(ligature) 손상=미관, 수식 무사
  - 결정론 스크리너 플래그: `TINY`(대부분 정상적으로 짧은 nacl 문서 + LSH/HERON 초록), `NO_ANCHOR`(범용/우산 문서 신호 → 아래 분류작업의 출발점), `GARBLE`(합자)
- [x] **알고리즘 → 필요문서 매핑 완결** → `algorithm_docs.jsonl` (1150행)
  - 방향1(한 문서→여러 알고리즘): 계열 공유(파라미터셋/변형/하위연산)로 정상. 문서 슬라이스로 처리
  - 방향2(한 알고리즘→여러 문서, 조합형): 검증 결과 **진짜 2차 문서 필요 = 3행뿐**(hmacsha256/hmacsha512256/salsa20hmacsha512 → SHA-256/512). 그 2차 문서는 **이미 코퍼스에 존재**(FIPS-180)해 링크만 하면 됨
  - `NO_ANCHOR`는 우산탐지기로 부적합 판명(파라미터 인코딩 숫자 때문 오탐). CAESAR 모드+암호 문서는 전부 자족적(present/twine/led/simon 정의 포함) 확인
  - 비공식 해시 2행(floppsy, bebb4185/discohash): 형식 스펙 부재, README가 유일 문서
- [ ] **A-(1)**: 알고리즘별 trivial-but-essential 구현 파라미터를 결정론적으로 추출
- [x] **A-(2)**: 문서에서 알고리즘 설명을 추출해 알고리즘별 description 생성 → `algorithm_descriptions.jsonl` (1074행)
  - 대상: spec 헤딩이 있는 254문서(bucket1). prose 26/no-spec 3은 별도(후속).
  - **(a) 규칙기반 삭제-절단**(`_spec_cut.py`): 헤딩 블랙리스트(intro/security/proof/benchmark/rationale/…)
    섹션만 통째 삭제, 나머지 보존. 기본값=보존. swallow 방지 위해 KEEP 헤딩에서 절단 중단.
    254문서 22.9M→13.5M자(58% 보존). 결과 `_spec_cut/<hash>.md`.
  - **P/M 분류**: 한 문서가 파라미터 변형뿐(P)이면 컷 통째 공유(612행). 별개 구성 의심(M, 56문서)은
    서브에이전트가 문서를 읽고 **알고리즘별 헤딩 경계만** 반환(작성 금지) → `_mslice.py`로 원문 verbatim
    슬라이스(462행). 예: deoxys-I/II, romulus-N/M/T, sphincs+ SHAKE/SHA2/Haraka, rainbow classic/cyclic/compressed.
  - **데이터품질**: 앵커체크(문서가 자기 알고리즘을 실제 언급하는가)로 오매핑 1건 격리 →
    mcssha4/5/6 (무관한 Dynamic SHA 공격논문). `description_exceptions.jsonl` (3행).
  - 정합성: 1074 description + 3 예외 = 1077 = bucket1 전체. 커버리지/헤딩/빈슬라이스 문제 0건.
- [ ] (나중) A-(3) / 긴장① : 파트 분해 및 핵심도 판정 기준
- [x] **B-(인터페이스)**: do-part 통과에 필수인 함수/인터페이스 명세를 SUPERCOP에서 결정론적 추출
      → `algorithm_functions.jsonl` (1157행, 전 알고리즘 100% 커버) + `_funcs/<cat>__<algo>.md`
  - **필수 함수 집합**: operation(카테고리)별로 SUPERCOP harness가 실제 호출하는 함수. 출처 = `trygen.py`의
    `function` 리스트(권위), 시그니처 = `PROTOTYPES.c` verbatim. 예) aead=encrypt/decrypt(2), kem=keypair/enc/dec(3),
    sign=keypair/sign/open(3), hash=hash(1), box=6개. 분포: 1함수 244 / 2함수 529 / 3함수 382 / 6함수 2.
  - **인터페이스 상수**: 각 알고리즘 `default_impl/api.h`를 C 전처리기로 실제 정수 해석(params.h·sizeof·libkeccak
    스텁까지 뚫음) → **1157/1157 전부 해석**. 예) kyber512 PK=800/SK=1632/CT=768/BYTES=32. api.h 원문도 verbatim 보존.
  - 추출기 `_func_extract.py`. LLM 비개입(전부 SUPERCOP 소스에서 결정론적). 기존 `algorithm_docs.jsonl`에
    `funcs_file` 컬럼 추가(조인 용이).
  - 남은 **B-(경계)**: fill-in-the-blank에서 ref 코드의 *어느 부분을 도려낼지*(난이도 변수)는 아직 미결(§5).
- [~] **B-(경계) v1**: fill-in-the-blank에서 도려낼 범위 = ref default 소스의 **파일단위 BLANK/KEEP 분류**.
      → `_carve.jsonl` (1157행). 분류기 `_carve.py`. LLM 비개입.
  - **기반조사**(`_locate_funcs.py` → `_locate_funcs.jsonl`): 각 필수함수의 정의 위치·본문크기 확보(1136/1157).
    발견: entry본문/전체코드 **중앙값 6.6%** — 위임형(kyber류 377개)은 entry만 blank하면 사소, 단일파일(338개)은
    entry=알고리즘 전체. 따라서 "entry만 blank"은 난이도 불균일 → 파일단위 알고리즘-로컬 carve로 결정.
  - **철학 = spec-cut과 동일**: 기본값=BLANK(구현 대상). KEEP(scaffolding으로 남길 '주어진 프리미티브')만 보수적으로.
    근거: over-keep(알고리즘 공짜 제공→실험 무효)이 over-blank(너무 어려움)보다 위험.
  - **KEEP 규칙**(파일명 stem, 부분문자열 금지): 표준해시/XOF(fips202·keccak*·sha256/512·shake·haraka·blake2b·thash_*),
    NIST DRBG/난수(rng·drbg·a_random·a_fixed), 글루(api.c·wrapper), 상수시간(verify·cmov).
    단 프리미티브가 **알고리즘 자체**이면(crypto_hash/verify/rng/core, 이름이 aes/sha/keccak…로 시작) KEEP 해제.
  - **감사·수정**: NO-blank 19건(rng/verify가 통째 KEEP돼 구현할 게 없던 버그) → operation-aware 억제+안전망으로 0건.
    over-keep 오분류 omdsha256/512(OMD 모드 알고리즘을 SHA 프리미티브로 오인) → stem 정확매칭으로 BLANK 복구. 최종 경고 0건.
  - 스팟체크 정상: kyber(ntt/poly/indcpa BLANK, fips202/shake KEEP), dilithium, sphincs(sha256 KEEP), sha256(hash.c BLANK).
  - 남은 것: **함수단위 carve**(한 파일에 알고리즘+프리미티브 혼재시, 예 aegis), **채점 하니스**(blank→stub 생성 후 SUPERCOP
    do-part 실행), KEEP 프리미티브 목록 반복 정련.
- [ ] (나중) B-(채점) : blank 파일을 stub로 만든 fill-in-the-blank 하니스 + do-part checksum 실행/채점.

**진행: 우산문서 분류 → A-(2) 완료 → B-(인터페이스) 완료 → B-(경계) v1 완료 → 다음은 B-(채점 하니스) 또는 A-(1).**
