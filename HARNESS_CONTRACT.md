# B-(채점) 하네스 계약 — planner + 분할생성 + do-part 채점

> 이 문서는 "LLM이 암호 알고리즘을 실제로 구현할 수 있는가"를 측정하는 실행 하네스의 계약이다.
> 데이터셋(A, B) 생성은 결정론적·LLM 비개입이지만, **여기서의 planner/몸체생성은 측정 대상(LLM
> 그 자체)**이다. 즉 입력 번들은 사람/스크립트가 만들고, 구현은 피험 LLM이 만든다.

---

## 0. 절대 제약 (재확인)

1. **ref 구현은 블랙박스.** ref의 소스·함수 분해·내부 helper 시그니처·`_carve`/`_locate` 산출물은
   피험 LLM에게 **일절 주지 않는다.** (그 분해 자체가 알고리즘 힌트이므로.)
2. **피험 LLM에게 주는 것은 딱 세 종류** — 전부 "알고리즘 무관 계약" 또는 "스펙 공개값":
   - **A** = pdf→md 알고리즘 설명 (사람 저작, 완전). `algorithm_descriptions.jsonl`의 `desc_file`.
   - **B-entry** = 이 operation이 export해야 하는 필수 함수 시그니처 + **인자 규약**(§2 표).
     출처 = SUPERCOP `PROTOTYPES.c`/`trygen.py`. 같은 operation의 모든 알고리즘에 **동일**.
   - **B-const** = 그 알고리즘 `api.h`의 인터페이스 상수(값). 스펙 공개 파라미터.
     출처 = `algorithm_functions.jsonl`의 `constants`.
3. **판정 기준**: entry 시그니처는 "무엇을 만들면 pass인지"의 계약일 뿐 분해 힌트가 아니다.
   helper 이름·개수·구조는 피험 LLM이 A로부터 **스스로 도출**해야 한다(= 측정하려는 능력).

---

## 1. 입력 번들 (per algorithm, 결정론적 생성)

`algorithm_docs.jsonl` 1행마다 아래 번들 1개를 조립한다. 모두 기존 산출물에서 조인:

```
bundle = {
  category, algorithm, default_impl,            # 식별
  description_md,      # A  ← algorithm_descriptions.jsonl.desc_file 내용
  entry_prototypes,    # B-entry ← algorithm_functions.jsonl.required_functions + PROTOTYPES.c
  arg_conventions,     # B-entry 인자규약 ← §2 (operation당 고정 텍스트 1벌)
  constants,           # B-const ← algorithm_functions.jsonl.constants (해석된 CRYPTO_* 정수만)
                       # 예: {CRYPTO_PUBLICKEYBYTES:800, CRYPTO_CIPHERTEXTBYTES:768, CRYPTO_BYTES:32}
}
```

**raw api.h / params.h 는 주지 않는다.** 원본 api.h는 흔히 `#include "params.h"` 하고(655/1157개),
params.h엔 `KYBER_Q=3329`·`KYBER_N=256` 같은 **알고리즘 내부 설계수치**가 있다. 이는 A(설명)에서
LLM이 스스로 도출해야 할 값이라, ref params.h로 얹으면 "A만으로 재구현되는가"의 **측정 귀속이 오염**된다.
필요한 인터페이스 크기는 이미 전처리기로 해석해 `constants`에 정수로 있으므로 그것만 준다.

**빌드 시엔 "flat api.h"를 합성해 넣는다** (§5-1). 즉 원본 api.h(=`#include "params.h"` 의존) 대신
해석된 정수만 박은 자립 헤더를 생성:
```c
#define CRYPTO_PUBLICKEYBYTES 800
#define CRYPTO_SECRETKEYBYTES 1632
#define CRYPTO_CIPHERTEXTBYTES 768
#define CRYPTO_BYTES 32
```
→ params.h가 파이프라인에서 완전히 사라진다(입력·빌드 양쪽). 하네스가 보는 값은 원본과 숫자 동일.
`constants`(입력번들에 보여주는 상수)와 flat api.h(빌드에 넣는 헤더)는 **같은 정수 출처**를 공유한다.

---

## 2. Operation별 entry 시그니처 + 인자 규약 (알고리즘 무관·공개)

이름 없는 PROTOTYPES.c 시그니처에 **표준 인자 의미**를 얹은 것. 이 매핑은 SUPERCOP API 규약이라
모든 알고리즘 공통 — 흘려도 알고리즘 정보 0. (커버리지: aead+sign+kem+hash+encrypt ≈ 1010/1157.)

### crypto_aead (498)
```c
int crypto_aead_encrypt(unsigned char *c, unsigned long long *clen,
    const unsigned char *m, unsigned long long mlen,
    const unsigned char *ad, unsigned long long adlen,
    const unsigned char *nsec, const unsigned char *npub, const unsigned char *k);
int crypto_aead_decrypt(unsigned char *m, unsigned long long *mlen,
    unsigned char *nsec, const unsigned char *c, unsigned long long clen,
    const unsigned char *ad, unsigned long long adlen,
    const unsigned char *npub, const unsigned char *k);
// c=암호문+태그, m=평문, ad=연관데이터, npub=nonce(공개), k=키, nsec=비밀nonce(대개 미사용/NULL).
// encrypt: *clen에 출력길이. decrypt: 인증 실패시 nonzero 반환, 성공시 0.
```

### crypto_sign (186)
```c
int crypto_sign_keypair(unsigned char *pk, unsigned char *sk);
int crypto_sign(unsigned char *sm, unsigned long long *smlen,
    const unsigned char *m, unsigned long long mlen, const unsigned char *sk);
int crypto_sign_open(unsigned char *m, unsigned long long *mlen,
    const unsigned char *sm, unsigned long long smlen, const unsigned char *pk);
// sm=서명첨부메시지(sig||m), sign_open: 검증 실패시 nonzero, 성공시 0 + 원문복원.
```

### crypto_kem (158)
```c
int crypto_kem_keypair(unsigned char *pk, unsigned char *sk);
int crypto_kem_enc(unsigned char *c, unsigned char *k, const unsigned char *pk);
int crypto_kem_dec(unsigned char *k, const unsigned char *c, const unsigned char *sk);
// c=캡슐, k=공유비밀(CRYPTO_BYTES). enc: pk로 (c,k) 생성. dec: sk+c로 동일 k 복원.
```

### crypto_hash (90)
```c
int crypto_hash(unsigned char *out, const unsigned char *in, unsigned long long inlen);
// out=CRYPTO_BYTES 다이제스트.
```

### crypto_encrypt (38, 공개키 암호)
```c
int crypto_encrypt_keypair(unsigned char *pk, unsigned char *sk);
int crypto_encrypt(unsigned char *c, unsigned long long *clen,
    const unsigned char *m, unsigned long long mlen, const unsigned char *pk);
int crypto_encrypt_open(unsigned char *m, unsigned long long *mlen,
    const unsigned char *c, unsigned long long clen, const unsigned char *sk);
```

### 나머지 operation (core/encode/decode/verify/stream/dh/scalarmult/box/secretbox/auth/onetimeauth/hashblocks/rng/xof, ≈147)
`PROTOTYPES.c` 시그니처를 그대로 쓰고, 인자 규약은 SUPERCOP `doc/`의 operation 페이지 표현을
동일 형식으로 1벌씩 첨부한다(구현 필요시 확장). 이들은 소수라 파일럿 이후 채워도 됨.

---

## 3. planner 계약

**입력**: §1 번들 전체.
**임무**: A를 이해하고, 주어진 entry를 만족시키기 위해 **필요한 내부 분해를 스스로 설계**한 뒤
"컴파일 가능한 스켈레톤"을 낸다.

**출력 형식** (엄격):
- 하나 이상의 소스/헤더 파일. 각 파일은 완전한 `#include`·타입·매크로·**모든 함수의 시그니처**를 포함.
- **entry 함수 시그니처는 §2 그대로**(글자 단위 일치). 반환·인자 타입 변경 금지.
- 각 함수 몸체는 **단일 플레이스홀더 토큰**만: `{ /*@FILL:<함수식별자>@*/ }`.
  - `<함수식별자>` = `파일명::함수명` (중복 없는 유일 키).
- 전역상수/룩업테이블이 알고리즘상 필요하면 **값까지 planner가 채운다**(이건 몸체가 아니라 데이터
  선언이므로 FILL 대상 아님). 단 그 값도 A로부터 도출해야 함(ref 열람 금지).
- 파일 목록과 빌드 순서를 매니페스트로 함께 출력: `{files:[...], fill_targets:[함수식별자...]}`.

**검증(자동)**: 스켈레톤을 그대로(몸체=빈 플레이스홀더를 `{}` 또는 `{return 0;}`로 치환) 컴파일 →
링크 심볼에 네임스페이스된 entry가 존재하는지 확인. 실패시 planner 재시도(같은 k 예산 내).

---

## 4. 몸체 생성잡 계약 (분할생성 = 함수단위 FIM)

`fill_targets` 각 항목마다 독립 잡 1개:

**입력**:
- 스켈레톤 전체(모든 시그니처·타입·다른 함수의 플레이스홀더 유지) — **prefix/suffix 문맥**.
- A(설명) 재첨부.
- **타깃 함수식별자 1개** — 이 몸체만 채우라는 지시.

**출력**: 그 함수의 몸체 `{ ... }` 내용만. 다른 함수 수정 금지.

**조립**: 스켈레톤의 `/*@FILL:x@*/`를 각 잡 출력으로 치환. brace-match(`find_def`/`body_span`
재사용, **단 겨냥 대상은 planner 출력**)로 스팬 확정 → 문자열 치환.

**의존성**: 몸체끼리 서로의 구현을 볼 필요는 없음(시그니처만 있으면 호출 가능). 따라서 **전부 병렬**.
품질 위해 옵션: 라운드 1에서 모든 몸체 생성 → 컴파일 → 에러난 함수만 라운드 2 재생성(문맥에
컴파일러 에러 첨부). 이는 채점이 아니라 **생성 편의**(실제 개발자도 컴파일 피드백 받음)이나,
"컴파일 에러 피드백 허용 여부"는 실험 변수로 명시(§5 프로토콜 A/B).

---

## 5. 조립 → 빌드 → 채점 → pass@k

1. 완성된 파일들을 SUPERCOP 임시 impl 디렉토리에 배치:
   `crypto_<op>/<algorithm>/<gen_impl>/` + **flat api.h(합성)** + 생성 소스.
   - **flat api.h**: 원본 api.h를 그대로 쓰지 않는다(원본은 `#include "params.h"` 의존 →
     LLM이 안 만든 params.h를 찾아 빌드가 깨짐). 대신 `constants`의 해석된 정수를 그대로 박은
     자립 헤더(`#define CRYPTO_PUBLICKEYBYTES 800` …)를 생성해 넣는다. 숫자는 원본과 동일하므로
     하네스가 보는 크기는 불변. params.h는 파이프라인에 등장하지 않는다.
   - LLM 생성코드가 `#include "api.h"` 하면 이 flat 헤더를 참조한다.
2. SUPERCOP `do`(또는 `data-do`) 하네스로 빌드+테스트: try harness가 entry를 호출하고
   **do-part checksum**을 계산 → 기대 체크섬과 일치하면 pass.
3. **pass@k**: 같은 번들로 planner→분할생성을 k회 독립 샘플 → 1회 이상 pass면 성공.
   보고: operation별·알고리즘별 pass@1, pass@k, 그리고 실패 원인 분류
   (컴파일실패 / 링크실패 / 런타임크래시 / checksum불일치).

**실험 프로토콜 변수(명시)**:
- (A) **원샷**: planner 없이 한 번에 전체 구현 요구(토큰 되는 소형에만).
- (B) **planner+분할, 컴파일피드백 無**: 한 번에 몸체 생성, 재시도 없음.
- (C) **planner+분할, 컴파일피드백 有**: §4 라운드2 허용.
세 프로토콜 비교가 곧 "분할생성이 규모 문제를 푸는가"의 측정.

---

## 6. 알려진 위험 / 점검 필요

- **params.h 누출**: 해결됨(§1, §5-1). raw api.h/params.h를 안 주고 flat api.h를 합성하므로
  내부 설계수치가 새지 않고 params.h 의존도 사라진다.
- **A의 완전성**: 진짜 리스크. pdf→md 추출한 A가 핵심값(모듈러스·분포·인코딩 규약)을 빠뜨리면
  재구현 불가. ref params.h로 때우면 측정 오염 → **A를 보강**하는 게 정답. 파일럿에서 실패 원인이
  "LLM 실력"인지 "A 불완전"인지 구분해 관측.
- **checksum이 스펙 밖 규약을 요구하는 알고리즘**: do-part는 **바이트 정확 재현**을 요구(고정 난수 →
  출력 바이트 해시). Kyber/Dilithium/SHA처럼 표준화된 건 스펙이 인코딩까지 규정 → 공정. 그러나
  덜 표준화된 SUPERCOP 제출물은 ref가 임의 직렬화를 택했을 수 있어 스펙(=A)만으로 재현 불가 →
  그런 알고리즘은 **실험 부적합**으로 분류(파일럿 후 선별 기준 마련).
- **checksum 재현성**: 생성 impl이 flat api.h의 CRYPTO_* 값을 못 바꾸게 고정. planner가 버퍼크기를
  임의 변경하면 하네스가 다른 크기로 호출 → checksum 무의미. flat api.h는 우리가 넣고 planner는 못 건드림.
- **entry가 매크로/asm으로만 정의되는 소수(gemss 등)**: 시그니처 계약은 동일하나 빌드 특이.
  파일럿 대상에서 제외하고 tail로.
- **do-part vs try-part**: 우리가 쓰는 건 정확도용 `do`(checksum). 성능 `try`가 아님을 코드에서 확인.

---

## 7. 파일럿 (검증 1회)

- 대상: `crypto_kem/kyber512` (위임형 대표, 설명 A 풍부, 규모 중간).
- 절차: 번들 조립 → planner 스켈레톤 → 컴파일검증 → 몸체 분할생성(프로토콜 C) → 조립 →
  SUPERCOP do → checksum 비교.
- 성공기준: 파이프라인이 end-to-end로 돌고, pass/fail이 **결정적으로** 나옴(LLM 품질과 무관하게
  하네스 자체가 정확히 채점하는지). 이후 소형 원샷(예: 어떤 crypto_hash)로 프로토콜 A도 1회 검증.

---

## 부록: 조인 키 요약

| 산출물 | 키 | 제공 필드 |
|---|---|---|
| `algorithm_docs.jsonl` | (category, algorithm) | default_impl, primary_md, funcs_file |
| `algorithm_descriptions.jsonl` | (category, algorithm) | desc_file (= A) |
| `algorithm_functions.jsonl` | (category, algorithm) | required_functions, constants, funcs_file |
| `_funcs/<cat>__<algo>.md` | funcs_id | entry 프로토타입 + 상수 + api.h |

(ref-side: `_carve.jsonl`/`_locate_funcs.jsonl`은 **채점 파이프 비참여** — 사후 분석 오라클로만.)
