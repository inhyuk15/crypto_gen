"""operation별 '구현시 고려사항' — SUPERCOP API/채점 레벨 사실만 (알고리즘 무관·공개).

arg_conventions 가 '인자 의미'라면, 여기는 그 operation을 do-part 채점에 통과시킬 때
반드시 지켜야 하는 '동작 규약'이다. 전부 알고리즘과 독립인 SUPERCOP 인터페이스 사실이라
LLM에 줘도 특정 알고리즘 로직 정보는 0 (출처: SUPERCOP try.c / do 스크립트 규약).

  for_operation(op) -> str   (planner/filegen 프롬프트의 {{OPERATION_NOTES}} 슬롯)
"""

# 모든 operation 공통 — do-part 채점의 근본 제약
COMMON = """\
- Determinism: the do-part test fixes all randomness and hashes every output byte into a
  checksum. Your output MUST be a reproducible function of the inputs only. No wall-clock
  time, no PID, no addresses, no uninitialized memory, no undefined behavior.
- All buffer sizes come from the CRYPTO_* interface constants (via "api.h"). Never hardcode
  a size that a constant already gives.
- Length outputs written through pointers (e.g. *clen, *smlen, *mlen) must be set exactly.
- In-place / overlap: the harness re-runs each function with an OUTPUT buffer that overlaps
  or is identical to an INPUT buffer (e.g. the same pointer passed for output and for the
  message, key, or associated data). Read every input byte you still need BEFORE you write
  over it — copy an input into a local buffer first if the algorithm reuses it after output
  starts. Wrong results under overlap fail the test even when the algorithm is otherwise correct.
- Stay within the declared output length: write only the bytes the size constants / length
  outputs permit. Writing past the end of an output buffer trips a memory-corruption check."""

# keyed operation (randombytes 를 링크해 줌) 공통
_RANDOMBYTES = """\
- Randomness source: the build links a deterministic `randombytes`. Declare and CALL it
  (`extern void randombytes(unsigned char *x, unsigned long long xlen);`) for any key/nonce/
  coin generation. Do NOT define it yourself and do NOT use any other RNG (rand/time/etc.).
  The checksum depends on consuming randombytes in the exact order the spec implies."""

NOTES = {
'aead': """\
- crypto_aead_encrypt writes ciphertext-then-tag into c and sets *clen = mlen + CRYPTO_ABYTES.
- crypto_aead_decrypt reads clen = mlen + CRYPTO_ABYTES bytes, recomputes/verifies the tag,
  and MUST return nonzero (e.g. -1) on authentication failure — writing nothing usable to m.
  On success it sets *mlen = clen - CRYPTO_ABYTES and returns 0.
- encrypt and decrypt must be exact inverses: the harness encrypts then decrypts and checks
  the recovered plaintext equals the original. A mismatch fails immediately (RUN_FAIL).
- Handle the empty cases: adlen == 0 and/or mlen == 0 must still produce the correct tag.
- npub is a CRYPTO_NPUBBYTES public nonce; k is CRYPTO_KEYBYTES. nsec has CRYPTO_NSECBYTES
  bytes (when 0, treat as unused / NULL). AEAD is fully deterministic — do NOT call randombytes.""",

'kem': """\
- crypto_kem_keypair(pk, sk): produce a keypair (CRYPTO_PUBLICKEYBYTES / CRYPTO_SECRETKEYBYTES).
- crypto_kem_enc(c, k, pk): produce a ciphertext c (CRYPTO_CIPHERTEXTBYTES) and the shared
  secret k (CRYPTO_BYTES) from pk.
- crypto_kem_dec(k, c, sk): recover the shared secret k (CRYPTO_BYTES) from c and sk. For an
  honestly-generated c it MUST equal the enc-side k. keypair/enc normally return 0; dec
  returns 0 (many KEMs use implicit rejection: on a bad c, derive a pseudo-random k and still
  return 0 — that behavior, if any, comes from the spec).
- The harness runs keypair→enc→dec and checks both k's match, so the FO/rejection details
  in the spec matter for the checksum.""" + "\n" + _RANDOMBYTES,

'sign': """\
- crypto_sign_keypair(pk, sk): produce a keypair (CRYPTO_PUBLICKEYBYTES / CRYPTO_SECRETKEYBYTES).
- crypto_sign(sm, smlen, m, mlen, sk): write a signed message to sm and set *smlen. The
  standard SUPERCOP convention is an attached signature (sm carries enough to recover m;
  commonly *smlen = mlen + CRYPTO_BYTES, but follow the spec's exact packing).
- crypto_sign_open(m, mlen, sm, smlen, pk): verify; on success recover m, set *mlen, return 0;
  on an invalid signature return nonzero and do not accept the message.
- The harness signs then opens and checks the message round-trips, so sign/sign_open must be
  exact inverses.""" + "\n" + _RANDOMBYTES,

'hash': """\
- crypto_hash(out, in, inlen): write exactly CRYPTO_BYTES digest bytes of in[0..inlen-1].
- Fully deterministic; must handle inlen == 0. No randombytes.""",

'stream': """\
- crypto_stream(out, outlen, n, k): fill out with outlen keystream bytes from nonce n, key k.
- crypto_stream_xor(out, m, mlen, n, k): out = m XOR keystream (same keystream as above).
- Deterministic; must handle length 0. Keystream indexing/counter order must match the spec
  byte-for-byte. No randombytes.""",

'encrypt': """\
- Public-key encryption. keypair(pk, sk); encrypt(c, clen, m, mlen, pk) sets *clen;
  encrypt_open(m, mlen, c, clen, sk) returns nonzero on failure, 0 on success (recovering m).
- encrypt/encrypt_open must round-trip.""" + "\n" + _RANDOMBYTES,

'auth': """\
- crypto_auth(out, in, inlen, k): write a CRYPTO_BYTES authenticator (MAC) of in under key k.
- crypto_auth_verify(h, in, inlen, k): return 0 iff h is the correct authenticator, else nonzero.
- Deterministic. Prefer a constant-time tag compare in verify. No randombytes.""",

'onetimeauth': """\
- crypto_onetimeauth(out, in, inlen, k): write a CRYPTO_BYTES one-time authenticator.
- crypto_onetimeauth_verify(h, in, inlen, k): return 0 iff valid, else nonzero.
- Deterministic. The key is one-time (never reuse across messages in the design). No randombytes.""",

'verify': """\
- crypto_verify(x, y): constant-time comparison of exactly CRYPTO_BYTES bytes.
- Return 0 iff all bytes equal, nonzero otherwise. Must not early-exit on the first difference
  (constant time). No randombytes.""",

'core': """\
- crypto_core(out, in, k, c): a fixed-size core permutation/function. Output size and the
  meaning of in/k/c are fixed by the spec; all lengths are constant (no length arguments).
- Fully deterministic. No randombytes.""",

'hashblocks': """\
- crypto_hashblocks(statebytes, in, inlen): absorb as many full blocks of in as possible into
  the serialized state `statebytes`, returning the number of leftover (unabsorbed) bytes.
- The state is passed in/out as bytes; its serialization must match the spec exactly.
  Deterministic. No randombytes.""",

'dh': """\
- crypto_dh_keypair(pk, sk); crypto_dh(out, pk, sk): out = shared secret from peer pk, own sk.
- The two parties must derive the identical shared secret. Sizes come from the constants.
""" + _RANDOMBYTES,

'scalarmult': """\
- crypto_scalarmult(q, n, p): q = n * p (group scalar mult). crypto_scalarmult_base(q, n):
  q = n * basepoint. Deterministic function of the inputs; clamping/encoding per spec.
- No randombytes (inputs are given).""",

'secretbox': """\
- NaCl secretbox convention: the caller zero-pads (crypto_secretbox_ZEROBYTES leading zeros on
  m, crypto_secretbox_BOXZEROBYTES on c). Preserve that padding convention exactly.
- secretbox_open returns nonzero on authentication failure. Deterministic. No randombytes.""",

'box': """\
- NaCl box convention (public-key authenticated encryption) with the same leading zero-byte
  padding as secretbox. box_open returns nonzero on failure. Follow the spec's key agreement +
  secretbox composition exactly.""" + "\n" + _RANDOMBYTES,
}


def for_operation(op):
    """op별 고려사항 문자열 (COMMON + op별). 미등록 op는 COMMON만."""
    specific = NOTES.get(op)
    if specific:
        return COMMON + "\n" + specific
    return COMMON + "\n- (No operation-specific notes; derive the exact I/O contract from the " \
                    "argument conventions and the specification.)"
