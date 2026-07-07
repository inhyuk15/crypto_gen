"""operation별 entry 함수 인자 규약 (SUPERCOP API 규약, 알고리즘 무관·공개).

PROTOTYPES.c의 이름없는 시그니처에 '표준 인자 의미'를 얹는다. 모든 알고리즘 공통이라
LLM에 줘도 알고리즘 정보는 0. planner/filegen 프롬프트에 삽입.
출처: HARNESS_CONTRACT.md §2.
"""

ARG_CONVENTIONS = {
'aead': """\
int crypto_aead_encrypt(unsigned char *c, unsigned long long *clen,
    const unsigned char *m, unsigned long long mlen,
    const unsigned char *ad, unsigned long long adlen,
    const unsigned char *nsec, const unsigned char *npub, const unsigned char *k);
int crypto_aead_decrypt(unsigned char *m, unsigned long long *mlen,
    unsigned char *nsec, const unsigned char *c, unsigned long long clen,
    const unsigned char *ad, unsigned long long adlen,
    const unsigned char *npub, const unsigned char *k);
// c=ciphertext+tag, m=plaintext, ad=associated data, npub=public nonce, k=key,
// nsec=secret nonce (usually unused/NULL). encrypt writes *clen. decrypt returns
// nonzero on authentication failure, 0 on success (and recovers plaintext).""",

'sign': """\
int crypto_sign_keypair(unsigned char *pk, unsigned char *sk);
int crypto_sign(unsigned char *sm, unsigned long long *smlen,
    const unsigned char *m, unsigned long long mlen, const unsigned char *sk);
int crypto_sign_open(unsigned char *m, unsigned long long *mlen,
    const unsigned char *sm, unsigned long long smlen, const unsigned char *pk);
// sm=signed message (signature||message). sign_open returns nonzero on invalid
// signature, 0 on success (and recovers the message).""",

'kem': """\
int crypto_kem_keypair(unsigned char *pk, unsigned char *sk);
int crypto_kem_enc(unsigned char *c, unsigned char *k, const unsigned char *pk);
int crypto_kem_dec(unsigned char *k, const unsigned char *c, const unsigned char *sk);
// c=ciphertext (encapsulation), k=shared secret (CRYPTO_BYTES). enc: from pk make
// (c,k). dec: from sk and c recover the same k.""",

'hash': """\
int crypto_hash(unsigned char *out, const unsigned char *in, unsigned long long inlen);
// out = CRYPTO_BYTES-byte digest of in[0..inlen-1].""",

'encrypt': """\
int crypto_encrypt_keypair(unsigned char *pk, unsigned char *sk);
int crypto_encrypt(unsigned char *c, unsigned long long *clen,
    const unsigned char *m, unsigned long long mlen, const unsigned char *pk);
int crypto_encrypt_open(unsigned char *m, unsigned long long *mlen,
    const unsigned char *c, unsigned long long clen, const unsigned char *sk);
// public-key encryption. encrypt_open returns nonzero on failure, 0 on success.""",

'stream': """\
int crypto_stream(unsigned char *out, unsigned long long outlen,
    const unsigned char *n, const unsigned char *k);
int crypto_stream_xor(unsigned char *out, const unsigned char *m,
    unsigned long long mlen, const unsigned char *n, const unsigned char *k);
// out=keystream (or m XOR keystream), n=nonce, k=key.""",

'onetimeauth': """\
int crypto_onetimeauth(unsigned char *out, const unsigned char *in,
    unsigned long long inlen, const unsigned char *k);
int crypto_onetimeauth_verify(const unsigned char *h, const unsigned char *in,
    unsigned long long inlen, const unsigned char *k);
// out/h = CRYPTO_BYTES authenticator. verify returns 0 iff h is valid for in,k.""",

'auth': """\
int crypto_auth(unsigned char *out, const unsigned char *in,
    unsigned long long inlen, const unsigned char *k);
int crypto_auth_verify(const unsigned char *h, const unsigned char *in,
    unsigned long long inlen, const unsigned char *k);
// out/h = CRYPTO_BYTES authenticator. verify returns 0 iff valid.""",

'core': """\
int crypto_core(unsigned char *out, const unsigned char *in,
    const unsigned char *k, const unsigned char *c);
// fixed-size core function: out from input in, key k, constant c.""",

'hashblocks': """\
int crypto_hashblocks(unsigned char *statebytes, const unsigned char *in,
    unsigned long long inlen);
// updates statebytes over as many full blocks of in as possible; returns leftover length.""",

'verify': """\
int crypto_verify(const unsigned char *x, const unsigned char *y);
// constant-time compare of CRYPTO_BYTES bytes; returns 0 iff equal.""",

'secretbox': """\
int crypto_secretbox(unsigned char *c, const unsigned char *m,
    unsigned long long mlen, const unsigned char *n, const unsigned char *k);
int crypto_secretbox_open(unsigned char *m, const unsigned char *c,
    unsigned long long clen, const unsigned char *n, const unsigned char *k);
// authenticated secret-key encryption with leading zero-byte padding convention.""",

'scalarmult': """\
int crypto_scalarmult(unsigned char *q, const unsigned char *n, const unsigned char *p);
int crypto_scalarmult_base(unsigned char *q, const unsigned char *n);
// q = n * p (group scalar multiplication); _base uses the standard base point.""",

'dh': """\
int crypto_dh_keypair(unsigned char *pk, unsigned char *sk);
int crypto_dh(unsigned char *out, const unsigned char *pk, const unsigned char *sk);
// out = shared secret from peer pk and own sk.""",
}


def for_operation(op):
    """op = 'aead' 등. 없으면 빈 문자열."""
    return ARG_CONVENTIONS.get(op, '')
