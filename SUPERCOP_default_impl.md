# SUPERCOP — `ref` 폴더가 없는 알고리즘의 default implementation 위치

- 데이터셋 루트: `supercop-20260330/`  (모든 경로는 이 폴더 기준 상대경로)
- 구현을 가진 알고리즘 총계: **1470**개
- `ref` 폴더 보유(표에서 제외): **1157**개
- `ref` 폴더 없음(아래 표 대상): **313**개

## 판별 규칙
- **구현 폴더** = `api.h` 를 포함한 디렉터리 (임의 깊이까지 탐색; 예: `algo/e/ref`, `algo/kcp/reference1600`)
- **`ref` 보유** = 구현 폴더 basename 중 정확히 `ref` 인 것이 하나라도 있으면 → 표 제외
- **ISA 전용 구현** = 다음 중 하나: ① `architectures` 파일 존재, ② 폴더명에 ISA 토큰(avx2/aarch64/armv7/amd64/asm 등), ③ 어셈블리(`.s/.S/.asm`) 포함
- **default(=portable) 구현** = 위 ISA 조건에 해당하지 않는 이식 가능 C 구현
- 경로 열은 reference 유사도 순으로 정렬(맨 앞이 가장 유력한 default). 후보가 여러 개면 모두 표기.

## 1. Default(portable) 구현이 `ref` 아닌 다른 폴더에 존재 — 249개

| Category | crypto_xxxx 의미 | Algorithm | default 구현 경로 (portable) |
|---|---|---|---|
| `crypto_aead` | Authenticated encryption with associated data | `romulusm1plusv13` | `crypto_aead/romulusm1plusv13/aadomn/opt32` |
| `crypto_aead` | Authenticated encryption with associated data | `romulusn1plusv13` | `crypto_aead/romulusn1plusv13/aadomn/opt32` |
| `crypto_aead` | Authenticated encryption with associated data | `skinnyaeadtk3128128plusv1` | `crypto_aead/skinnyaeadtk3128128plusv1/aadomn/opt32` |
| `crypto_auth` | Secret-key message authentication (MAC) | `pyrhash` | `crypto_auth/pyrhash/little` |
| `crypto_auth` | Secret-key message authentication (MAC) | `siphash24` | `crypto_auth/siphash24/ref_le`<br>`crypto_auth/siphash24/little`<br>`crypto_auth/siphash24/little2`<br>`crypto_auth/siphash24/sandy`<br>`crypto_auth/siphash24/sandy2` |
| `crypto_auth` | Secret-key message authentication (MAC) | `siphash48` | `crypto_auth/siphash48/ref_le`<br>`crypto_auth/siphash48/little`<br>`crypto_auth/siphash48/sandy` |
| `crypto_core` | Core building-block functions | `keccakf160032bits` | `crypto_core/keccakf160032bits/reference1600-32bits`<br>`crypto_core/keccakf160032bits/inplace1600bi` |
| `crypto_core` | Core building-block functions | `keccakf160064bits` | `crypto_core/keccakf160064bits/reference1600`<br>`crypto_core/keccakf160064bits/optimized1600lcu6`<br>`crypto_core/keccakf160064bits/optimized1600lcufull`<br>`crypto_core/keccakf160064bits/optimized1600lcufullshld`<br>`crypto_core/keccakf160064bits/optimized1600u6`<br>`crypto_core/keccakf160064bits/optimized1600ufull`<br>`crypto_core/keccakf160064bits/compact1600` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `claus` | `crypto_dh/claus/cryptopp`<br>`crypto_dh/claus/gmp`<br>`crypto_dh/claus/ntl`<br>`crypto_dh/claus/openssl`<br>`crypto_dh/claus/opensslnew` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `curve2251` | `crypto_dh/curve2251/mpfq` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `ed448goldilocks` | `crypto_dh/ed448goldilocks/32`<br>`crypto_dh/ed448goldilocks/64` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `gls254prot` | `crypto_dh/gls254prot/opt` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `sclaus1024` | `crypto_dh/sclaus1024/cryptopp`<br>`crypto_dh/sclaus1024/gmp` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `sclaus2048` | `crypto_dh/sclaus2048/cryptopp`<br>`crypto_dh/sclaus2048/gmp` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `surf127eps` | `crypto_dh/surf127eps/mpfq` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `surf2113` | `crypto_dh/surf2113/mpfq` |
| `crypto_encrypt` | Public-key encryption | `ledapkc1264` | `crypto_encrypt/ledapkc1264/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc12sl` | `crypto_encrypt/ledapkc12sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc1364` | `crypto_encrypt/ledapkc1364/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc13sl` | `crypto_encrypt/ledapkc13sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc1464` | `crypto_encrypt/ledapkc1464/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc14sl` | `crypto_encrypt/ledapkc14sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc3264` | `crypto_encrypt/ledapkc3264/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc32sl` | `crypto_encrypt/ledapkc32sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc3364` | `crypto_encrypt/ledapkc3364/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc33sl` | `crypto_encrypt/ledapkc33sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc3464` | `crypto_encrypt/ledapkc3464/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc34sl` | `crypto_encrypt/ledapkc34sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc5264` | `crypto_encrypt/ledapkc5264/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc52sl` | `crypto_encrypt/ledapkc52sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc5364` | `crypto_encrypt/ledapkc5364/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc53sl` | `crypto_encrypt/ledapkc53sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc5464` | `crypto_encrypt/ledapkc5464/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ledapkc54sl` | `crypto_encrypt/ledapkc54sl/portableopt` |
| `crypto_encrypt` | Public-key encryption | `ronald1024` | `crypto_encrypt/ronald1024/openssl`<br>`crypto_encrypt/ronald1024/opensslnew` |
| `crypto_encrypt` | Public-key encryption | `ronald1536` | `crypto_encrypt/ronald1536/openssl`<br>`crypto_encrypt/ronald1536/opensslnew` |
| `crypto_encrypt` | Public-key encryption | `ronald2048` | `crypto_encrypt/ronald2048/openssl`<br>`crypto_encrypt/ronald2048/opensslnew` |
| `crypto_encrypt` | Public-key encryption | `ronald3072` | `crypto_encrypt/ronald3072/openssl`<br>`crypto_encrypt/ronald3072/opensslnew` |
| `crypto_encrypt` | Public-key encryption | `ronald4096` | `crypto_encrypt/ronald4096/openssl`<br>`crypto_encrypt/ronald4096/opensslnew` |
| `crypto_hash` | Hashing (fixed-length output) | `bblake256` | `crypto_hash/bblake256/bswap`<br>`crypto_hash/bblake256/regs` |
| `crypto_hash` | Hashing (fixed-length output) | `blake3` | `crypto_hash/blake3/portable` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash161` | `crypto_hash/cubehash161/simple`<br>`crypto_hash/cubehash161/spec`<br>`crypto_hash/cubehash161/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash1616` | `crypto_hash/cubehash1616/simple`<br>`crypto_hash/cubehash1616/spec`<br>`crypto_hash/cubehash1616/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash162` | `crypto_hash/cubehash162/simple`<br>`crypto_hash/cubehash162/spec`<br>`crypto_hash/cubehash162/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash1632` | `crypto_hash/cubehash1632/simple`<br>`crypto_hash/cubehash1632/sphlib`<br>`crypto_hash/cubehash1632/sphlib-small`<br>`crypto_hash/cubehash1632/unrolled`<br>`crypto_hash/cubehash1632/unrolled2`<br>`crypto_hash/cubehash1632/unrolled3`<br>`crypto_hash/cubehash1632/unrolled4`<br>`crypto_hash/cubehash1632/unrolled5` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash164` | `crypto_hash/cubehash164/simple`<br>`crypto_hash/cubehash164/spec`<br>`crypto_hash/cubehash164/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash168` | `crypto_hash/cubehash168/simple`<br>`crypto_hash/cubehash168/spec`<br>`crypto_hash/cubehash168/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash512` | `crypto_hash/cubehash512/simple`<br>`crypto_hash/cubehash512/unrolled`<br>`crypto_hash/cubehash512/unrolled2`<br>`crypto_hash/cubehash512/unrolled3`<br>`crypto_hash/cubehash512/unrolled4`<br>`crypto_hash/cubehash512/unrolled5` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash81` | `crypto_hash/cubehash81/simple`<br>`crypto_hash/cubehash81/spec`<br>`crypto_hash/cubehash81/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash816` | `crypto_hash/cubehash816/simple`<br>`crypto_hash/cubehash816/spec`<br>`crypto_hash/cubehash816/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash82` | `crypto_hash/cubehash82/simple`<br>`crypto_hash/cubehash82/spec`<br>`crypto_hash/cubehash82/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash832` | `crypto_hash/cubehash832/simple`<br>`crypto_hash/cubehash832/spec`<br>`crypto_hash/cubehash832/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash84` | `crypto_hash/cubehash84/simple`<br>`crypto_hash/cubehash84/spec`<br>`crypto_hash/cubehash84/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `cubehash88` | `crypto_hash/cubehash88/simple`<br>`crypto_hash/cubehash88/spec`<br>`crypto_hash/cubehash88/unrolled` |
| `crypto_hash` | Hashing (fixed-length output) | `echo256` | `crypto_hash/echo256/generic/opt32`<br>`crypto_hash/echo256/generic/opt64`<br>`crypto_hash/echo256/ccalik/bitsliced`<br>`crypto_hash/echo256/powerpc/pp32cv1`<br>`crypto_hash/echo256/powerpc/pp32cv2`<br>`crypto_hash/echo256/sphlib`<br>`crypto_hash/echo256/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `echo512` | `crypto_hash/echo512/generic/opt32`<br>`crypto_hash/echo512/generic/opt64`<br>`crypto_hash/echo512/ccalik/bitsliced`<br>`crypto_hash/echo512/powerpc/pp32cv1`<br>`crypto_hash/echo512/powerpc/pp32cv2`<br>`crypto_hash/echo512/sphlib`<br>`crypto_hash/echo512/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `echosp256` | `crypto_hash/echosp256/generic/opt32`<br>`crypto_hash/echosp256/generic/opt64`<br>`crypto_hash/echosp256/powerpc/pp32cv1`<br>`crypto_hash/echosp256/powerpc/pp32cv2` |
| `crypto_hash` | Hashing (fixed-length output) | `echosp512` | `crypto_hash/echosp512/generic/opt32`<br>`crypto_hash/echosp512/generic/opt64`<br>`crypto_hash/echosp512/powerpc/pp32cv1`<br>`crypto_hash/echosp512/powerpc/pp32cv2` |
| `crypto_hash` | Hashing (fixed-length output) | `edonr256` | `crypto_hash/edonr256/optc`<br>`crypto_hash/edonr256/swpbe` |
| `crypto_hash` | Hashing (fixed-length output) | `edonr512` | `crypto_hash/edonr512/optc`<br>`crypto_hash/edonr512/swpbe` |
| `crypto_hash` | Hashing (fixed-length output) | `essence224` | `crypto_hash/essence224/gcc` |
| `crypto_hash` | Hashing (fixed-length output) | `essence256` | `crypto_hash/essence256/gcc` |
| `crypto_hash` | Hashing (fixed-length output) | `essence384` | `crypto_hash/essence384/gcc` |
| `crypto_hash` | Hashing (fixed-length output) | `essence512` | `crypto_hash/essence512/gcc` |
| `crypto_hash` | Hashing (fixed-length output) | `fugue2` | `crypto_hash/fugue2/cop_opt32` |
| `crypto_hash` | Hashing (fixed-length output) | `fugue256` | `crypto_hash/fugue256/ANSI_opt32`<br>`crypto_hash/fugue256/ANSI_opt64`<br>`crypto_hash/fugue256/sphlib` |
| `crypto_hash` | Hashing (fixed-length output) | `fugue512` | `crypto_hash/fugue512/sphlib` |
| `crypto_hash` | Hashing (fixed-length output) | `groestl256` | `crypto_hash/groestl256/opt32`<br>`crypto_hash/groestl256/opt64`<br>`crypto_hash/groestl256/32bit-2ktable`<br>`crypto_hash/groestl256/32bit-bytesliced-c-fast`<br>`crypto_hash/groestl256/32bit-bytesliced-c-small`<br>`crypto_hash/groestl256/8bit_c`<br>`crypto_hash/groestl256/sphlib`<br>`crypto_hash/groestl256/sphlib-adapted`<br>`crypto_hash/groestl256/sphlib-small`<br>`crypto_hash/groestl256/vperm-intr` |
| `crypto_hash` | Hashing (fixed-length output) | `groestl512` | `crypto_hash/groestl512/opt32`<br>`crypto_hash/groestl512/opt64`<br>`crypto_hash/groestl512/32bit-bytesliced-c-small`<br>`crypto_hash/groestl512/sphlib`<br>`crypto_hash/groestl512/sphlib-adapted`<br>`crypto_hash/groestl512/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `hamsi` | `crypto_hash/hamsi/simd-1`<br>`crypto_hash/hamsi/simd-2`<br>`crypto_hash/hamsi/sphlib`<br>`crypto_hash/hamsi/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `hamsi512` | `crypto_hash/hamsi512/sphlib`<br>`crypto_hash/hamsi512/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `jh224` | `crypto_hash/jh224/bitslice_opt32`<br>`crypto_hash/jh224/bitslice_opt64`<br>`crypto_hash/jh224/bitslice_ref32`<br>`crypto_hash/jh224/bitslice_ref64`<br>`crypto_hash/jh224/simple` |
| `crypto_hash` | Hashing (fixed-length output) | `jh256` | `crypto_hash/jh256/bitslice_opt32`<br>`crypto_hash/jh256/bitslice_opt64`<br>`crypto_hash/jh256/bitslice_ref32`<br>`crypto_hash/jh256/bitslice_ref64`<br>`crypto_hash/jh256/simple` |
| `crypto_hash` | Hashing (fixed-length output) | `jh384` | `crypto_hash/jh384/bitslice_opt32`<br>`crypto_hash/jh384/bitslice_opt64`<br>`crypto_hash/jh384/bitslice_ref32`<br>`crypto_hash/jh384/bitslice_ref64`<br>`crypto_hash/jh384/simple` |
| `crypto_hash` | Hashing (fixed-length output) | `jh512` | `crypto_hash/jh512/bitslice_opt32`<br>`crypto_hash/jh512/bitslice_opt64`<br>`crypto_hash/jh512/bitslice_ref32`<br>`crypto_hash/jh512/bitslice_ref64`<br>`crypto_hash/jh512/simple` |
| `crypto_hash` | Hashing (fixed-length output) | `k12` | `crypto_hash/k12/kcp/reference1600`<br>`crypto_hash/k12/kcp/reference1600-32bits`<br>`crypto_hash/k12/kcp/optimized1600lcu6`<br>`crypto_hash/k12/kcp/optimized1600lcufull`<br>`crypto_hash/k12/kcp/optimized1600lcufullshld`<br>`crypto_hash/k12/kcp/optimized1600u6`<br>`crypto_hash/k12/kcp/optimized1600ufull`<br>`crypto_hash/k12/kcp/compact1600`<br>`crypto_hash/k12/kcp/inplace1600bi` |
| `crypto_hash` | Hashing (fixed-length output) | `keccak` | `crypto_hash/keccak/opt32bi-rvku2`<br>`crypto_hash/keccak/opt32bi-s2lcu4`<br>`crypto_hash/keccak/opt32biT-s2lcu4`<br>`crypto_hash/keccak/opt64lcu24`<br>`crypto_hash/keccak/opt64lcu6`<br>`crypto_hash/keccak/opt64u6`<br>`crypto_hash/keccak/compact`<br>`crypto_hash/keccak/compact8`<br>`crypto_hash/keccak/inplace`<br>`crypto_hash/keccak/inplace32bi`<br>`crypto_hash/keccak/simple`<br>`crypto_hash/keccak/simple32bi` |
| `crypto_hash` | Hashing (fixed-length output) | `keccakc1024` | `crypto_hash/keccakc1024/opt32bi-rvku2`<br>`crypto_hash/keccakc1024/opt32bi-s2lcu4`<br>`crypto_hash/keccakc1024/opt32biT-s2lcu4`<br>`crypto_hash/keccakc1024/opt64lcu24`<br>`crypto_hash/keccakc1024/opt64lcu6`<br>`crypto_hash/keccakc1024/opt64u6`<br>`crypto_hash/keccakc1024/compact`<br>`crypto_hash/keccakc1024/compact8`<br>`crypto_hash/keccakc1024/inplace`<br>`crypto_hash/keccakc1024/inplace32bi`<br>`crypto_hash/keccakc1024/simple`<br>`crypto_hash/keccakc1024/simple32bi`<br>`crypto_hash/keccakc1024/sphlib`<br>`crypto_hash/keccakc1024/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `keccakc256` | `crypto_hash/keccakc256/opt32bi-rvku2`<br>`crypto_hash/keccakc256/opt32bi-s2lcu4`<br>`crypto_hash/keccakc256/opt32biT-s2lcu4`<br>`crypto_hash/keccakc256/opt64lcu24`<br>`crypto_hash/keccakc256/opt64lcu6`<br>`crypto_hash/keccakc256/opt64u6`<br>`crypto_hash/keccakc256/compact`<br>`crypto_hash/keccakc256/compact8`<br>`crypto_hash/keccakc256/inplace`<br>`crypto_hash/keccakc256/inplace32bi`<br>`crypto_hash/keccakc256/simple`<br>`crypto_hash/keccakc256/simple32bi` |
| `crypto_hash` | Hashing (fixed-length output) | `keccakc448` | `crypto_hash/keccakc448/opt32bi-rvku2`<br>`crypto_hash/keccakc448/opt32bi-s2lcu4`<br>`crypto_hash/keccakc448/opt32biT-s2lcu4`<br>`crypto_hash/keccakc448/opt64lcu24`<br>`crypto_hash/keccakc448/opt64lcu6`<br>`crypto_hash/keccakc448/opt64u6`<br>`crypto_hash/keccakc448/compact`<br>`crypto_hash/keccakc448/compact8`<br>`crypto_hash/keccakc448/inplace`<br>`crypto_hash/keccakc448/inplace32bi`<br>`crypto_hash/keccakc448/simple`<br>`crypto_hash/keccakc448/simple32bi` |
| `crypto_hash` | Hashing (fixed-length output) | `keccakc512` | `crypto_hash/keccakc512/opt32bi-rvku2`<br>`crypto_hash/keccakc512/opt32bi-s2lcu4`<br>`crypto_hash/keccakc512/opt32biT-s2lcu4`<br>`crypto_hash/keccakc512/opt64lcu24`<br>`crypto_hash/keccakc512/opt64lcu6`<br>`crypto_hash/keccakc512/opt64u6`<br>`crypto_hash/keccakc512/compact`<br>`crypto_hash/keccakc512/compact8`<br>`crypto_hash/keccakc512/gil/singlefile`<br>`crypto_hash/keccakc512/gil/singlefile_unrolled`<br>`crypto_hash/keccakc512/inplace`<br>`crypto_hash/keccakc512/inplace32bi`<br>`crypto_hash/keccakc512/simple`<br>`crypto_hash/keccakc512/simple32bi`<br>`crypto_hash/keccakc512/sphlib`<br>`crypto_hash/keccakc512/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `keccakc768` | `crypto_hash/keccakc768/opt32bi-rvku2`<br>`crypto_hash/keccakc768/opt32bi-s2lcu4`<br>`crypto_hash/keccakc768/opt32biT-s2lcu4`<br>`crypto_hash/keccakc768/opt64lcu24`<br>`crypto_hash/keccakc768/opt64lcu6`<br>`crypto_hash/keccakc768/opt64u6`<br>`crypto_hash/keccakc768/compact`<br>`crypto_hash/keccakc768/compact8`<br>`crypto_hash/keccakc768/inplace`<br>`crypto_hash/keccakc768/inplace32bi`<br>`crypto_hash/keccakc768/simple`<br>`crypto_hash/keccakc768/simple32bi` |
| `crypto_hash` | Hashing (fixed-length output) | `lane256` | `crypto_hash/lane256/c` |
| `crypto_hash` | Hashing (fixed-length output) | `lane512` | `crypto_hash/lane512/c` |
| `crypto_hash` | Hashing (fixed-length output) | `luffa256` | `crypto_hash/luffa256/opt32`<br>`crypto_hash/luffa256/sphlib`<br>`crypto_hash/luffa256/thomaz/basic` |
| `crypto_hash` | Hashing (fixed-length output) | `luffa384` | `crypto_hash/luffa384/opt32` |
| `crypto_hash` | Hashing (fixed-length output) | `luffa512` | `crypto_hash/luffa512/opt32`<br>`crypto_hash/luffa512/sphlib` |
| `crypto_hash` | Hashing (fixed-length output) | `md2` | `crypto_hash/md2/openssl` |
| `crypto_hash` | Hashing (fixed-length output) | `md4` | `crypto_hash/md4/openssl` |
| `crypto_hash` | Hashing (fixed-length output) | `nasha256` | `crypto_hash/nasha256/opt`<br>`crypto_hash/nasha256/opt_v4` |
| `crypto_hash` | Hashing (fixed-length output) | `nasha512` | `crypto_hash/nasha512/opt`<br>`crypto_hash/nasha512/opt_v4` |
| `crypto_hash` | Hashing (fixed-length output) | `ripemd160` | `crypto_hash/ripemd160/openssl` |
| `crypto_hash` | Hashing (fixed-length output) | `round3jh256` | `crypto_hash/round3jh256/simple`<br>`crypto_hash/round3jh256/sphlib`<br>`crypto_hash/round3jh256/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `round3jh512` | `crypto_hash/round3jh512/simple`<br>`crypto_hash/round3jh512/sphlib`<br>`crypto_hash/round3jh512/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `sarmal256` | `crypto_hash/sarmal256/opt64` |
| `crypto_hash` | Hashing (fixed-length output) | `sarmal512` | `crypto_hash/sarmal512/opt64` |
| `crypto_hash` | Hashing (fixed-length output) | `sha1` | `crypto_hash/sha1/openssl` |
| `crypto_hash` | Hashing (fixed-length output) | `sha224` | `crypto_hash/sha224/openssl` |
| `crypto_hash` | Hashing (fixed-length output) | `sha3224` | `crypto_hash/sha3224/oncore32bits`<br>`crypto_hash/sha3224/oncore64bits`<br>`crypto_hash/sha3224/openssl`<br>`crypto_hash/sha3224/usekcp` |
| `crypto_hash` | Hashing (fixed-length output) | `sha3256` | `crypto_hash/sha3256/compact`<br>`crypto_hash/sha3256/oncore32bits`<br>`crypto_hash/sha3256/oncore64bits`<br>`crypto_hash/sha3256/openssl`<br>`crypto_hash/sha3256/usekcp` |
| `crypto_hash` | Hashing (fixed-length output) | `sha3384` | `crypto_hash/sha3384/oncore32bits`<br>`crypto_hash/sha3384/oncore64bits`<br>`crypto_hash/sha3384/openssl`<br>`crypto_hash/sha3384/usekcp` |
| `crypto_hash` | Hashing (fixed-length output) | `sha3512` | `crypto_hash/sha3512/oncore32bits`<br>`crypto_hash/sha3512/oncore64bits`<br>`crypto_hash/sha3512/openssl`<br>`crypto_hash/sha3512/usekcp` |
| `crypto_hash` | Hashing (fixed-length output) | `sha384` | `crypto_hash/sha384/openssl` |
| `crypto_hash` | Hashing (fixed-length output) | `shabal256` | `crypto_hash/shabal256/sphlib` |
| `crypto_hash` | Hashing (fixed-length output) | `shake128` | `crypto_hash/shake128/cryptopp`<br>`crypto_hash/shake128/oncore32bits`<br>`crypto_hash/shake128/oncore64bits`<br>`crypto_hash/shake128/openssl`<br>`crypto_hash/shake128/usekcp`<br>`crypto_hash/shake128/usexof` |
| `crypto_hash` | Hashing (fixed-length output) | `shake256` | `crypto_hash/shake256/cryptopp`<br>`crypto_hash/shake256/gil/singlefile`<br>`crypto_hash/shake256/gil/singlefile_unrolled`<br>`crypto_hash/shake256/oncore32bits`<br>`crypto_hash/shake256/oncore64bits`<br>`crypto_hash/shake256/openssl`<br>`crypto_hash/shake256/usekcp`<br>`crypto_hash/shake256/usexof` |
| `crypto_hash` | Hashing (fixed-length output) | `shavite3256` | `crypto_hash/shavite3256/8-bit`<br>`crypto_hash/shavite3256/low-mem`<br>`crypto_hash/shavite3256/lower-mem`<br>`crypto_hash/shavite3256/new-aes-round`<br>`crypto_hash/shavite3256/no-salt`<br>`crypto_hash/shavite3256/sphlib`<br>`crypto_hash/shavite3256/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `shavite3512` | `crypto_hash/shavite3512/8-bit`<br>`crypto_hash/shavite3512/IntelL1Cache`<br>`crypto_hash/shavite3512/different-order`<br>`crypto_hash/shavite3512/low-mem`<br>`crypto_hash/shavite3512/lower-mem`<br>`crypto_hash/shavite3512/new-aes-round`<br>`crypto_hash/shavite3512/no-salt`<br>`crypto_hash/shavite3512/sphlib`<br>`crypto_hash/shavite3512/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `skein10241024` | `crypto_hash/skein10241024/opt` |
| `crypto_hash` | Hashing (fixed-length output) | `skein256256` | `crypto_hash/skein256256/opt` |
| `crypto_hash` | Hashing (fixed-length output) | `skein512256` | `crypto_hash/skein512256/opt`<br>`crypto_hash/skein512256/little`<br>`crypto_hash/skein512256/simple`<br>`crypto_hash/skein512256/sphlib`<br>`crypto_hash/skein512256/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `skein512512` | `crypto_hash/skein512512/opt`<br>`crypto_hash/skein512512/little`<br>`crypto_hash/skein512512/simple`<br>`crypto_hash/skein512512/sphlib`<br>`crypto_hash/skein512512/sphlib-small` |
| `crypto_hash` | Hashing (fixed-length output) | `tiger` | `crypto_hash/tiger/cryptopp` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `bikel1` | `crypto_kem/bikel1/portable` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `bikel3` | `crypto_kem/bikel3/portable` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `frodokem1344aes` | `crypto_kem/frodokem1344aes/optimized`<br>`crypto_kem/frodokem1344aes/x64` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `frodokem1344shake` | `crypto_kem/frodokem1344shake/optimized`<br>`crypto_kem/frodokem1344shake/x64` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `frodokem640` | `crypto_kem/frodokem640/reference`<br>`crypto_kem/frodokem640/optimized` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `frodokem640aes` | `crypto_kem/frodokem640aes/optimized`<br>`crypto_kem/frodokem640aes/x64` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `frodokem640shake` | `crypto_kem/frodokem640shake/optimized`<br>`crypto_kem/frodokem640shake/x64` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `frodokem976` | `crypto_kem/frodokem976/reference`<br>`crypto_kem/frodokem976/optimized` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `frodokem976aes` | `crypto_kem/frodokem976aes/optimized`<br>`crypto_kem/frodokem976aes/x64` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `frodokem976shake` | `crypto_kem/frodokem976shake/optimized`<br>`crypto_kem/frodokem976shake/x64` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem1264` | `crypto_kem/ledakem1264/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem12sl` | `crypto_kem/ledakem12sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem1364` | `crypto_kem/ledakem1364/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem13sl` | `crypto_kem/ledakem13sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem1464` | `crypto_kem/ledakem1464/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem14sl` | `crypto_kem/ledakem14sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem3264` | `crypto_kem/ledakem3264/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem32sl` | `crypto_kem/ledakem32sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem3364` | `crypto_kem/ledakem3364/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem33sl` | `crypto_kem/ledakem33sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem3464` | `crypto_kem/ledakem3464/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem34sl` | `crypto_kem/ledakem34sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem5264` | `crypto_kem/ledakem5264/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem52sl` | `crypto_kem/ledakem52sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem5364` | `crypto_kem/ledakem5364/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem53sl` | `crypto_kem/ledakem53sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem5464` | `crypto_kem/ledakem5464/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakem54sl` | `crypto_kem/ledakem54sl/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa12` | `crypto_kem/ledakemcpa12/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa13` | `crypto_kem/ledakemcpa13/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa14` | `crypto_kem/ledakemcpa14/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa32` | `crypto_kem/ledakemcpa32/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa33` | `crypto_kem/ledakemcpa33/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa34` | `crypto_kem/ledakemcpa34/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa52` | `crypto_kem/ledakemcpa52/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa53` | `crypto_kem/ledakemcpa53/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `ledakemcpa54` | `crypto_kem/ledakemcpa54/portableopt` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `rsa2048` | `crypto_kem/rsa2048/gmp`<br>`crypto_kem/rsa2048/gmpxx`<br>`crypto_kem/rsa2048/ntl` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `threebears1248r2ccax` | `crypto_kem/threebears1248r2ccax/opt`<br>`crypto_kem/threebears1248r2ccax/vec` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `threebears1248r2cpax` | `crypto_kem/threebears1248r2cpax/opt`<br>`crypto_kem/threebears1248r2cpax/vec` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `threebears624r2ccax` | `crypto_kem/threebears624r2ccax/opt`<br>`crypto_kem/threebears624r2ccax/vec` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `threebears624r2cpax` | `crypto_kem/threebears624r2cpax/opt`<br>`crypto_kem/threebears624r2cpax/vec` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `threebears936r2ccax` | `crypto_kem/threebears936r2ccax/opt`<br>`crypto_kem/threebears936r2ccax/vec` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `threebears936r2cpax` | `crypto_kem/threebears936r2cpax/opt`<br>`crypto_kem/threebears936r2cpax/vec` |
| `crypto_scalarmult` | Scalar multiplication (e.g. ECDH) | `kummer` | `crypto_scalarmult/kummer/ref5`<br>`crypto_scalarmult/kummer/ref5u` |
| `crypto_scalarmult` | Scalar multiplication (e.g. ECDH) | `nistp256` | `crypto_scalarmult/nistp256/mj32`<br>`crypto_scalarmult/nistp256/s2n`<br>`crypto_scalarmult/nistp256/s2n-alt` |
| `crypto_sign` | Public-key digital signatures | `donald1024` | `crypto_sign/donald1024/openssl`<br>`crypto_sign/donald1024/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `donald2048` | `crypto_sign/donald2048/cryptopp`<br>`crypto_sign/donald2048/openssl`<br>`crypto_sign/donald2048/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `donald512` | `crypto_sign/donald512/openssl`<br>`crypto_sign/donald512/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldb163` | `crypto_sign/ecdonaldb163/openssl`<br>`crypto_sign/ecdonaldb163/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldb233` | `crypto_sign/ecdonaldb233/openssl`<br>`crypto_sign/ecdonaldb233/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldb283` | `crypto_sign/ecdonaldb283/openssl`<br>`crypto_sign/ecdonaldb283/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldb409` | `crypto_sign/ecdonaldb409/openssl`<br>`crypto_sign/ecdonaldb409/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldb571` | `crypto_sign/ecdonaldb571/openssl`<br>`crypto_sign/ecdonaldb571/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldk163` | `crypto_sign/ecdonaldk163/openssl`<br>`crypto_sign/ecdonaldk163/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldk233` | `crypto_sign/ecdonaldk233/openssl`<br>`crypto_sign/ecdonaldk233/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldk283` | `crypto_sign/ecdonaldk283/openssl`<br>`crypto_sign/ecdonaldk283/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldk409` | `crypto_sign/ecdonaldk409/openssl`<br>`crypto_sign/ecdonaldk409/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldk571` | `crypto_sign/ecdonaldk571/openssl`<br>`crypto_sign/ecdonaldk571/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldp160` | `crypto_sign/ecdonaldp160/openssl`<br>`crypto_sign/ecdonaldp160/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldp192` | `crypto_sign/ecdonaldp192/openssl`<br>`crypto_sign/ecdonaldp192/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldp224` | `crypto_sign/ecdonaldp224/openssl`<br>`crypto_sign/ecdonaldp224/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldp256` | `crypto_sign/ecdonaldp256/openssl`<br>`crypto_sign/ecdonaldp256/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldp384` | `crypto_sign/ecdonaldp384/openssl`<br>`crypto_sign/ecdonaldp384/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ecdonaldp521` | `crypto_sign/ecdonaldp521/openssl`<br>`crypto_sign/ecdonaldp521/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ed448goldilocks` | `crypto_sign/ed448goldilocks/32`<br>`crypto_sign/ed448goldilocks/64` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf16fastr3` | `crypto_sign/mqom2cat1gf16fastr3/ref_default`<br>`crypto_sign/mqom2cat1gf16fastr3/ref_memopt`<br>`crypto_sign/mqom2cat1gf16fastr3/plain32_default`<br>`crypto_sign/mqom2cat1gf16fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf16fastr5` | `crypto_sign/mqom2cat1gf16fastr5/ref_default`<br>`crypto_sign/mqom2cat1gf16fastr5/ref_memopt`<br>`crypto_sign/mqom2cat1gf16fastr5/plain32_default`<br>`crypto_sign/mqom2cat1gf16fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf16shortr3` | `crypto_sign/mqom2cat1gf16shortr3/ref_default`<br>`crypto_sign/mqom2cat1gf16shortr3/ref_memopt`<br>`crypto_sign/mqom2cat1gf16shortr3/plain32_default`<br>`crypto_sign/mqom2cat1gf16shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf16shortr5` | `crypto_sign/mqom2cat1gf16shortr5/ref_default`<br>`crypto_sign/mqom2cat1gf16shortr5/ref_memopt`<br>`crypto_sign/mqom2cat1gf16shortr5/plain32_default`<br>`crypto_sign/mqom2cat1gf16shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf256fastr3` | `crypto_sign/mqom2cat1gf256fastr3/ref_default`<br>`crypto_sign/mqom2cat1gf256fastr3/ref_memopt`<br>`crypto_sign/mqom2cat1gf256fastr3/plain32_default`<br>`crypto_sign/mqom2cat1gf256fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf256fastr5` | `crypto_sign/mqom2cat1gf256fastr5/ref_default`<br>`crypto_sign/mqom2cat1gf256fastr5/ref_memopt`<br>`crypto_sign/mqom2cat1gf256fastr5/plain32_default`<br>`crypto_sign/mqom2cat1gf256fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf256shortr3` | `crypto_sign/mqom2cat1gf256shortr3/ref_default`<br>`crypto_sign/mqom2cat1gf256shortr3/ref_memopt`<br>`crypto_sign/mqom2cat1gf256shortr3/plain32_default`<br>`crypto_sign/mqom2cat1gf256shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf256shortr5` | `crypto_sign/mqom2cat1gf256shortr5/ref_default`<br>`crypto_sign/mqom2cat1gf256shortr5/ref_memopt`<br>`crypto_sign/mqom2cat1gf256shortr5/plain32_default`<br>`crypto_sign/mqom2cat1gf256shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf2fastr3` | `crypto_sign/mqom2cat1gf2fastr3/ref_default`<br>`crypto_sign/mqom2cat1gf2fastr3/ref_memopt`<br>`crypto_sign/mqom2cat1gf2fastr3/plain32_default`<br>`crypto_sign/mqom2cat1gf2fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf2fastr5` | `crypto_sign/mqom2cat1gf2fastr5/ref_default`<br>`crypto_sign/mqom2cat1gf2fastr5/ref_memopt`<br>`crypto_sign/mqom2cat1gf2fastr5/plain32_default`<br>`crypto_sign/mqom2cat1gf2fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf2shortr3` | `crypto_sign/mqom2cat1gf2shortr3/ref_default`<br>`crypto_sign/mqom2cat1gf2shortr3/ref_memopt`<br>`crypto_sign/mqom2cat1gf2shortr3/plain32_default`<br>`crypto_sign/mqom2cat1gf2shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat1gf2shortr5` | `crypto_sign/mqom2cat1gf2shortr5/ref_default`<br>`crypto_sign/mqom2cat1gf2shortr5/ref_memopt`<br>`crypto_sign/mqom2cat1gf2shortr5/plain32_default`<br>`crypto_sign/mqom2cat1gf2shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf16fastr3` | `crypto_sign/mqom2cat3gf16fastr3/ref_default`<br>`crypto_sign/mqom2cat3gf16fastr3/ref_memopt`<br>`crypto_sign/mqom2cat3gf16fastr3/plain32_default`<br>`crypto_sign/mqom2cat3gf16fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf16fastr5` | `crypto_sign/mqom2cat3gf16fastr5/ref_default`<br>`crypto_sign/mqom2cat3gf16fastr5/ref_memopt`<br>`crypto_sign/mqom2cat3gf16fastr5/plain32_default`<br>`crypto_sign/mqom2cat3gf16fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf16shortr3` | `crypto_sign/mqom2cat3gf16shortr3/ref_default`<br>`crypto_sign/mqom2cat3gf16shortr3/ref_memopt`<br>`crypto_sign/mqom2cat3gf16shortr3/plain32_default`<br>`crypto_sign/mqom2cat3gf16shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf16shortr5` | `crypto_sign/mqom2cat3gf16shortr5/ref_default`<br>`crypto_sign/mqom2cat3gf16shortr5/ref_memopt`<br>`crypto_sign/mqom2cat3gf16shortr5/plain32_default`<br>`crypto_sign/mqom2cat3gf16shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf256fastr3` | `crypto_sign/mqom2cat3gf256fastr3/ref_default`<br>`crypto_sign/mqom2cat3gf256fastr3/ref_memopt`<br>`crypto_sign/mqom2cat3gf256fastr3/plain32_default`<br>`crypto_sign/mqom2cat3gf256fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf256fastr5` | `crypto_sign/mqom2cat3gf256fastr5/ref_default`<br>`crypto_sign/mqom2cat3gf256fastr5/ref_memopt`<br>`crypto_sign/mqom2cat3gf256fastr5/plain32_default`<br>`crypto_sign/mqom2cat3gf256fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf256shortr3` | `crypto_sign/mqom2cat3gf256shortr3/ref_default`<br>`crypto_sign/mqom2cat3gf256shortr3/ref_memopt`<br>`crypto_sign/mqom2cat3gf256shortr3/plain32_default`<br>`crypto_sign/mqom2cat3gf256shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf256shortr5` | `crypto_sign/mqom2cat3gf256shortr5/ref_default`<br>`crypto_sign/mqom2cat3gf256shortr5/ref_memopt`<br>`crypto_sign/mqom2cat3gf256shortr5/plain32_default`<br>`crypto_sign/mqom2cat3gf256shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf2fastr3` | `crypto_sign/mqom2cat3gf2fastr3/ref_default`<br>`crypto_sign/mqom2cat3gf2fastr3/ref_memopt`<br>`crypto_sign/mqom2cat3gf2fastr3/plain32_default`<br>`crypto_sign/mqom2cat3gf2fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf2fastr5` | `crypto_sign/mqom2cat3gf2fastr5/ref_default`<br>`crypto_sign/mqom2cat3gf2fastr5/ref_memopt`<br>`crypto_sign/mqom2cat3gf2fastr5/plain32_default`<br>`crypto_sign/mqom2cat3gf2fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf2shortr3` | `crypto_sign/mqom2cat3gf2shortr3/ref_default`<br>`crypto_sign/mqom2cat3gf2shortr3/ref_memopt`<br>`crypto_sign/mqom2cat3gf2shortr3/plain32_default`<br>`crypto_sign/mqom2cat3gf2shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat3gf2shortr5` | `crypto_sign/mqom2cat3gf2shortr5/ref_default`<br>`crypto_sign/mqom2cat3gf2shortr5/ref_memopt`<br>`crypto_sign/mqom2cat3gf2shortr5/plain32_default`<br>`crypto_sign/mqom2cat3gf2shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf16fastr3` | `crypto_sign/mqom2cat5gf16fastr3/ref_default`<br>`crypto_sign/mqom2cat5gf16fastr3/ref_memopt`<br>`crypto_sign/mqom2cat5gf16fastr3/plain32_default`<br>`crypto_sign/mqom2cat5gf16fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf16fastr5` | `crypto_sign/mqom2cat5gf16fastr5/ref_default`<br>`crypto_sign/mqom2cat5gf16fastr5/ref_memopt`<br>`crypto_sign/mqom2cat5gf16fastr5/plain32_default`<br>`crypto_sign/mqom2cat5gf16fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf16shortr3` | `crypto_sign/mqom2cat5gf16shortr3/ref_default`<br>`crypto_sign/mqom2cat5gf16shortr3/ref_memopt`<br>`crypto_sign/mqom2cat5gf16shortr3/plain32_default`<br>`crypto_sign/mqom2cat5gf16shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf16shortr5` | `crypto_sign/mqom2cat5gf16shortr5/ref_default`<br>`crypto_sign/mqom2cat5gf16shortr5/ref_memopt`<br>`crypto_sign/mqom2cat5gf16shortr5/plain32_default`<br>`crypto_sign/mqom2cat5gf16shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf256fastr3` | `crypto_sign/mqom2cat5gf256fastr3/ref_default`<br>`crypto_sign/mqom2cat5gf256fastr3/ref_memopt`<br>`crypto_sign/mqom2cat5gf256fastr3/plain32_default`<br>`crypto_sign/mqom2cat5gf256fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf256fastr5` | `crypto_sign/mqom2cat5gf256fastr5/ref_default`<br>`crypto_sign/mqom2cat5gf256fastr5/ref_memopt`<br>`crypto_sign/mqom2cat5gf256fastr5/plain32_default`<br>`crypto_sign/mqom2cat5gf256fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf256shortr3` | `crypto_sign/mqom2cat5gf256shortr3/ref_default`<br>`crypto_sign/mqom2cat5gf256shortr3/ref_memopt`<br>`crypto_sign/mqom2cat5gf256shortr3/plain32_default`<br>`crypto_sign/mqom2cat5gf256shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf256shortr5` | `crypto_sign/mqom2cat5gf256shortr5/ref_default`<br>`crypto_sign/mqom2cat5gf256shortr5/ref_memopt`<br>`crypto_sign/mqom2cat5gf256shortr5/plain32_default`<br>`crypto_sign/mqom2cat5gf256shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf2fastr3` | `crypto_sign/mqom2cat5gf2fastr3/ref_default`<br>`crypto_sign/mqom2cat5gf2fastr3/ref_memopt`<br>`crypto_sign/mqom2cat5gf2fastr3/plain32_default`<br>`crypto_sign/mqom2cat5gf2fastr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf2fastr5` | `crypto_sign/mqom2cat5gf2fastr5/ref_default`<br>`crypto_sign/mqom2cat5gf2fastr5/ref_memopt`<br>`crypto_sign/mqom2cat5gf2fastr5/plain32_default`<br>`crypto_sign/mqom2cat5gf2fastr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf2shortr3` | `crypto_sign/mqom2cat5gf2shortr3/ref_default`<br>`crypto_sign/mqom2cat5gf2shortr3/ref_memopt`<br>`crypto_sign/mqom2cat5gf2shortr3/plain32_default`<br>`crypto_sign/mqom2cat5gf2shortr3/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `mqom2cat5gf2shortr5` | `crypto_sign/mqom2cat5gf2shortr5/ref_default`<br>`crypto_sign/mqom2cat5gf2shortr5/ref_memopt`<br>`crypto_sign/mqom2cat5gf2shortr5/plain32_default`<br>`crypto_sign/mqom2cat5gf2shortr5/plain32_memopt` |
| `crypto_sign` | Public-key digital signatures | `pass769` | `crypto_sign/pass769/ref-karatsuba` |
| `crypto_sign` | Public-key digital signatures | `pass863` | `crypto_sign/pass863/ref-karatsuba` |
| `crypto_sign` | Public-key digital signatures | `ronald1024` | `crypto_sign/ronald1024/openssl`<br>`crypto_sign/ronald1024/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ronald1536` | `crypto_sign/ronald1536/openssl`<br>`crypto_sign/ronald1536/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ronald2048` | `crypto_sign/ronald2048/openssl`<br>`crypto_sign/ronald2048/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ronald3072` | `crypto_sign/ronald3072/openssl`<br>`crypto_sign/ronald3072/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ronald4096` | `crypto_sign/ronald4096/openssl`<br>`crypto_sign/ronald4096/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ronald512` | `crypto_sign/ronald512/openssl`<br>`crypto_sign/ronald512/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `ronald768` | `crypto_sign/ronald768/openssl`<br>`crypto_sign/ronald768/opensslnew` |
| `crypto_sign` | Public-key digital signatures | `rwb0fuz1024` | `crypto_sign/rwb0fuz1024/gmp` |
| `crypto_sort` | Constant-time sorting | `int16` | `crypto_sort/int16/portable4`<br>`crypto_sort/int16/stdsort` |
| `crypto_sort` | Constant-time sorting | `int32` | `crypto_sort/int32/portable3`<br>`crypto_sort/int32/portable4`<br>`crypto_sort/int32/portable5`<br>`crypto_sort/int32/compact`<br>`crypto_sort/int32/radix256ml`<br>`crypto_sort/int32/radix256sml`<br>`crypto_sort/int32/stdsort` |
| `crypto_sort` | Constant-time sorting | `int64` | `crypto_sort/int64/portable4`<br>`crypto_sort/int64/stdsort` |
| `crypto_sort` | Constant-time sorting | `uint32` | `crypto_sort/uint32/compact`<br>`crypto_sort/uint32/stdsort`<br>`crypto_sort/uint32/useint32` |
| `crypto_sort` | Constant-time sorting | `uint64` | `crypto_sort/uint64/stdsort`<br>`crypto_sort/uint64/useint64` |
| `crypto_stream` | Stream cipher | `aes128ctr` | `crypto_stream/aes128ctr/cryptopp`<br>`crypto_stream/aes128ctr/openssl` |
| `crypto_stream` | Stream cipher | `aes128estream` | `crypto_stream/aes128estream/e/bernstein/big-1`<br>`crypto_stream/aes128estream/e/bernstein/little-1`<br>`crypto_stream/aes128estream/e/bernstein/little-2`<br>`crypto_stream/aes128estream/e/bernstein/little-3`<br>`crypto_stream/aes128estream/e/bernstein/little-4`<br>`crypto_stream/aes128estream/e/gladman`<br>`crypto_stream/aes128estream/e/hongjun/v0`<br>`crypto_stream/aes128estream/e/hongjun/v1` |
| `crypto_stream` | Stream cipher | `aes192ctr` | `crypto_stream/aes192ctr/cryptopp`<br>`crypto_stream/aes192ctr/openssl` |
| `crypto_stream` | Stream cipher | `aes256ctr` | `crypto_stream/aes256ctr/cryptopp`<br>`crypto_stream/aes256ctr/openssl` |
| `crypto_stream` | Stream cipher | `aes256estream` | `crypto_stream/aes256estream/e/gladman`<br>`crypto_stream/aes256estream/e/hongjun/v0`<br>`crypto_stream/aes256estream/e/hongjun/v1` |
| `crypto_stream` | Stream cipher | `cryptmtv3` | `crypto_stream/cryptmtv3/e/v3` |
| `crypto_stream` | Stream cipher | `dragon` | `crypto_stream/dragon/e/submissions/dragon` |
| `crypto_stream` | Stream cipher | `hc128` | `crypto_stream/hc128/e/hc-128/200606`<br>`crypto_stream/hc128/e/hc-128/200701a`<br>`crypto_stream/hc128/e/hc-128/200701b` |
| `crypto_stream` | Stream cipher | `hc256` | `crypto_stream/hc256/e/hc-256/200511`<br>`crypto_stream/hc256/e/hc-256/200701` |
| `crypto_stream` | Stream cipher | `nlsv2` | `crypto_stream/nlsv2/e/v2/sync/1`<br>`crypto_stream/nlsv2/e/v2/sync/2` |
| `crypto_stream` | Stream cipher | `panama` | `crypto_stream/panama/cryptopp` |
| `crypto_stream` | Stream cipher | `snow20` | `crypto_stream/snow20/e/benchmarks/snow-2.0` |
| `crypto_stream` | Stream cipher | `sosemanuk` | `crypto_stream/sosemanuk/cryptopp`<br>`crypto_stream/sosemanuk/e/submissions/sosemanuk` |
| `crypto_stream` | Stream cipher | `tpy` | `crypto_stream/tpy/e/tpy` |
| `crypto_stream` | Stream cipher | `tpy6` | `crypto_stream/tpy6/e/tpy6` |
| `crypto_stream` | Stream cipher | `tpypy` | `crypto_stream/tpypy/e/tpypy` |
| `crypto_stream` | Stream cipher | `trivium` | `crypto_stream/trivium/e/submissions/trivium` |
| `crypto_xof` | Extendable-output function (XOF) | `shake128` | `crypto_xof/shake128/openssl`<br>`crypto_xof/shake128/tweet`<br>`crypto_xof/shake128/unrollround`<br>`crypto_xof/shake128/usekcp` |
| `crypto_xof` | Extendable-output function (XOF) | `shake256` | `crypto_xof/shake256/openssl`<br>`crypto_xof/shake256/tweet`<br>`crypto_xof/shake256/unrollround`<br>`crypto_xof/shake256/usekcp` |

## 2. Portable 구현 없음 — ISA 전용 구현만 존재 — 64개

순수 C default 구현이 없고 아키텍처 특화 구현만 있는 경우.

| Category | crypto_xxxx 의미 | Algorithm | 존재하는 ISA 전용 구현 경로 |
|---|---|---|---|
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `ecfp256e` | `crypto_dh/ecfp256e/v01/var`<br>`crypto_dh/ecfp256e/v01/w8s1`<br>`crypto_dh/ecfp256e/v01/w8s2`<br>`crypto_dh/ecfp256e/v01/w8s4`<br>`crypto_dh/ecfp256e/v01/w8s8` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `ecfp256h` | `crypto_dh/ecfp256h/v01/var`<br>`crypto_dh/ecfp256h/v01/w8s1`<br>`crypto_dh/ecfp256h/v01/w8s2`<br>`crypto_dh/ecfp256h/v01/w8s4`<br>`crypto_dh/ecfp256h/v01/w8s8` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `ecfp256i` | `crypto_dh/ecfp256i/v01/var`<br>`crypto_dh/ecfp256i/v01/w8s1`<br>`crypto_dh/ecfp256i/v01/w8s2`<br>`crypto_dh/ecfp256i/v01/w8s4`<br>`crypto_dh/ecfp256i/v01/w8s8` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `ecfp256q` | `crypto_dh/ecfp256q/v01/var`<br>`crypto_dh/ecfp256q/v01/w8s1`<br>`crypto_dh/ecfp256q/v01/w8s2`<br>`crypto_dh/ecfp256q/v01/w8s4`<br>`crypto_dh/ecfp256q/v01/w8s8` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `ecfp256s` | `crypto_dh/ecfp256s/v01/var`<br>`crypto_dh/ecfp256s/v01/w8s1`<br>`crypto_dh/ecfp256s/v01/w8s2`<br>`crypto_dh/ecfp256s/v01/w8s4`<br>`crypto_dh/ecfp256s/v01/w8s8` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `gls1271` | `crypto_dh/gls1271/ref4` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `hecfp127i` | `crypto_dh/hecfp127i/v02/var`<br>`crypto_dh/hecfp127i/v02/w8s01`<br>`crypto_dh/hecfp127i/v02/w8s02`<br>`crypto_dh/hecfp127i/v02/w8s04`<br>`crypto_dh/hecfp127i/v02/w8s08`<br>`crypto_dh/hecfp127i/v02/w8s16`<br>`crypto_dh/hecfp127i/v02/w8s32` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `hecfp128bk` | `crypto_dh/hecfp128bk/v02/varglv4`<br>`crypto_dh/hecfp128bk/v02/w8s01glv4`<br>`crypto_dh/hecfp128bk/v02/w8s02glv4`<br>`crypto_dh/hecfp128bk/v02/w8s04glv4`<br>`crypto_dh/hecfp128bk/v02/w8s08glv4`<br>`crypto_dh/hecfp128bk/v02/w8s16glv4`<br>`crypto_dh/hecfp128bk/v02/w8s32glv4` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `hecfp128fkt` | `crypto_dh/hecfp128fkt/v02/varglv4`<br>`crypto_dh/hecfp128fkt/v02/w8s01glv4`<br>`crypto_dh/hecfp128fkt/v02/w8s02glv4`<br>`crypto_dh/hecfp128fkt/v02/w8s04glv4`<br>`crypto_dh/hecfp128fkt/v02/w8s08glv4`<br>`crypto_dh/hecfp128fkt/v02/w8s16glv4`<br>`crypto_dh/hecfp128fkt/v02/w8s32glv4` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `hecfp128i` | `crypto_dh/hecfp128i/v02/var`<br>`crypto_dh/hecfp128i/v02/w8s01`<br>`crypto_dh/hecfp128i/v02/w8s02`<br>`crypto_dh/hecfp128i/v02/w8s04`<br>`crypto_dh/hecfp128i/v02/w8s08`<br>`crypto_dh/hecfp128i/v02/w8s16`<br>`crypto_dh/hecfp128i/v02/w8s32` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `hecfp61e2bk` | `crypto_dh/hecfp61e2bk/v01/varglv8`<br>`crypto_dh/hecfp61e2bk/v01/w8s01glv8`<br>`crypto_dh/hecfp61e2bk/v01/w8s02glv8`<br>`crypto_dh/hecfp61e2bk/v01/w8s04glv8`<br>`crypto_dh/hecfp61e2bk/v01/w8s08glv8`<br>`crypto_dh/hecfp61e2bk/v01/w8s16glv8`<br>`crypto_dh/hecfp61e2bk/v01/w8s32glv8` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `hecfp61e2i` | `crypto_dh/hecfp61e2i/v01/var`<br>`crypto_dh/hecfp61e2i/v01/w8s01`<br>`crypto_dh/hecfp61e2i/v01/w8s02`<br>`crypto_dh/hecfp61e2i/v01/w8s04`<br>`crypto_dh/hecfp61e2i/v01/w8s08`<br>`crypto_dh/hecfp61e2i/v01/w8s16`<br>`crypto_dh/hecfp61e2i/v01/w8s32` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `hecfp64e2bk` | `crypto_dh/hecfp64e2bk/v01/varglv8`<br>`crypto_dh/hecfp64e2bk/v01/w8s01glv8`<br>`crypto_dh/hecfp64e2bk/v01/w8s02glv8`<br>`crypto_dh/hecfp64e2bk/v01/w8s04glv8`<br>`crypto_dh/hecfp64e2bk/v01/w8s08glv8`<br>`crypto_dh/hecfp64e2bk/v01/w8s16glv8`<br>`crypto_dh/hecfp64e2bk/v01/w8s32glv8` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `hecfp64e2i` | `crypto_dh/hecfp64e2i/v01/var`<br>`crypto_dh/hecfp64e2i/v01/w8s01`<br>`crypto_dh/hecfp64e2i/v01/w8s02`<br>`crypto_dh/hecfp64e2i/v01/w8s04`<br>`crypto_dh/hecfp64e2i/v01/w8s08`<br>`crypto_dh/hecfp64e2i/v01/w8s16`<br>`crypto_dh/hecfp64e2i/v01/w8s32` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `jacfp127i` | `crypto_dh/jacfp127i/v01/var`<br>`crypto_dh/jacfp127i/v01/w4s01`<br>`crypto_dh/jacfp127i/v01/w4s02`<br>`crypto_dh/jacfp127i/v01/w4s04`<br>`crypto_dh/jacfp127i/v01/w4s08`<br>`crypto_dh/jacfp127i/v01/w4s16`<br>`crypto_dh/jacfp127i/v01/w4s32`<br>`crypto_dh/jacfp127i/v01/w8s01`<br>`crypto_dh/jacfp127i/v01/w8s02`<br>`crypto_dh/jacfp127i/v01/w8s04`<br>`crypto_dh/jacfp127i/v01/w8s08`<br>`crypto_dh/jacfp127i/v01/w8s16`<br>`crypto_dh/jacfp127i/v01/w8s32` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `jacfp128bk` | `crypto_dh/jacfp128bk/v01/varglv4`<br>`crypto_dh/jacfp128bk/v01/w4s01glv4`<br>`crypto_dh/jacfp128bk/v01/w4s02glv4`<br>`crypto_dh/jacfp128bk/v01/w4s04glv4`<br>`crypto_dh/jacfp128bk/v01/w4s08glv4`<br>`crypto_dh/jacfp128bk/v01/w4s16glv4`<br>`crypto_dh/jacfp128bk/v01/w4s32glv4`<br>`crypto_dh/jacfp128bk/v01/w8s01glv4`<br>`crypto_dh/jacfp128bk/v01/w8s02glv4`<br>`crypto_dh/jacfp128bk/v01/w8s04glv4`<br>`crypto_dh/jacfp128bk/v01/w8s08glv4`<br>`crypto_dh/jacfp128bk/v01/w8s16glv4`<br>`crypto_dh/jacfp128bk/v01/w8s32glv4` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `kumfp127g` | `crypto_dh/kumfp127g/v02/var` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `kumfp128g` | `crypto_dh/kumfp128g/v02/var` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `kumfp61e2g` | `crypto_dh/kumfp61e2g/v01/var` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `kumfp64e2g` | `crypto_dh/kumfp64e2g/v01/var` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `kumjacfp127g` | `crypto_dh/kumjacfp127g/v01/var`<br>`crypto_dh/kumjacfp127g/v01/w4s01`<br>`crypto_dh/kumjacfp127g/v01/w4s02`<br>`crypto_dh/kumjacfp127g/v01/w4s04`<br>`crypto_dh/kumjacfp127g/v01/w4s08`<br>`crypto_dh/kumjacfp127g/v01/w4s16`<br>`crypto_dh/kumjacfp127g/v01/w4s32`<br>`crypto_dh/kumjacfp127g/v01/w8s01`<br>`crypto_dh/kumjacfp127g/v01/w8s02`<br>`crypto_dh/kumjacfp127g/v01/w8s04`<br>`crypto_dh/kumjacfp127g/v01/w8s08`<br>`crypto_dh/kumjacfp127g/v01/w8s16`<br>`crypto_dh/kumjacfp127g/v01/w8s32` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `prjfp127i` | `crypto_dh/prjfp127i/v01/var`<br>`crypto_dh/prjfp127i/v01/w4s01`<br>`crypto_dh/prjfp127i/v01/w4s02`<br>`crypto_dh/prjfp127i/v01/w4s04`<br>`crypto_dh/prjfp127i/v01/w4s08`<br>`crypto_dh/prjfp127i/v01/w4s16`<br>`crypto_dh/prjfp127i/v01/w4s32`<br>`crypto_dh/prjfp127i/v01/w8s01`<br>`crypto_dh/prjfp127i/v01/w8s02`<br>`crypto_dh/prjfp127i/v01/w8s04`<br>`crypto_dh/prjfp127i/v01/w8s08`<br>`crypto_dh/prjfp127i/v01/w8s16`<br>`crypto_dh/prjfp127i/v01/w8s32` |
| `crypto_dh` | Public-key Diffie-Hellman key exchange | `prjfp128bk` | `crypto_dh/prjfp128bk/v01/varglv4`<br>`crypto_dh/prjfp128bk/v01/w4s01glv4`<br>`crypto_dh/prjfp128bk/v01/w4s02glv4`<br>`crypto_dh/prjfp128bk/v01/w4s04glv4`<br>`crypto_dh/prjfp128bk/v01/w4s08glv4`<br>`crypto_dh/prjfp128bk/v01/w4s16glv4`<br>`crypto_dh/prjfp128bk/v01/w4s32glv4`<br>`crypto_dh/prjfp128bk/v01/w8s01glv4`<br>`crypto_dh/prjfp128bk/v01/w8s02glv4`<br>`crypto_dh/prjfp128bk/v01/w8s04glv4`<br>`crypto_dh/prjfp128bk/v01/w8s08glv4`<br>`crypto_dh/prjfp128bk/v01/w8s16glv4`<br>`crypto_dh/prjfp128bk/v01/w8s32glv4` |
| `crypto_hash` | Hashing (fixed-length output) | `bblake512` | `crypto_hash/bblake512/xop` |
| `crypto_hash` | Hashing (fixed-length output) | `cheetah256` | `crypto_hash/cheetah256/asm`<br>`crypto_hash/cheetah256/asm64` |
| `crypto_hash` | Hashing (fixed-length output) | `cheetah512` | `crypto_hash/cheetah512/asm`<br>`crypto_hash/cheetah512/asm32`<br>`crypto_hash/cheetah512/asm64` |
| `crypto_hash` | Hashing (fixed-length output) | `fugue384` | `crypto_hash/fugue384/ccalik/aesni`<br>`crypto_hash/fugue384/ccalik/vperm` |
| `crypto_hash` | Hashing (fixed-length output) | `keccakc256treed2` | `crypto_hash/keccakc256treed2/sseu24`<br>`crypto_hash/keccakc256treed2/sseu4`<br>`crypto_hash/keccakc256treed2/xopu24` |
| `crypto_hash` | Hashing (fixed-length output) | `keccakc512treed2` | `crypto_hash/keccakc512treed2/sseu24`<br>`crypto_hash/keccakc512treed2/sseu4`<br>`crypto_hash/keccakc512treed2/xopu24` |
| `crypto_hash` | Hashing (fixed-length output) | `lux256` | `crypto_hash/lux256/asm` |
| `crypto_hash` | Hashing (fixed-length output) | `lux512` | `crypto_hash/lux512/asm` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqc128` | `crypto_kem/hqc128/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqc128round4` | `crypto_kem/hqc128round4/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqc192` | `crypto_kem/hqc192/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqc192round4` | `crypto_kem/hqc192round4/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqc256` | `crypto_kem/hqc256/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqc256round4` | `crypto_kem/hqc256round4/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqcrmrs128` | `crypto_kem/hqcrmrs128/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqcrmrs192` | `crypto_kem/hqcrmrs192/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `hqcrmrs256` | `crypto_kem/hqcrmrs256/avx` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `nhcompact1024cca` | `crypto_kem/nhcompact1024cca/avx2` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `nhcompact512cca` | `crypto_kem/nhcompact512cca/avx2` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `nhcompact768cca` | `crypto_kem/nhcompact768cca/avx2` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `saberx4` | `crypto_kem/saberx4/avx2` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `sikep434comp` | `crypto_kem/sikep434comp/amd64`<br>`crypto_kem/sikep434comp/amd64asm`<br>`crypto_kem/sikep434comp/arm`<br>`crypto_kem/sikep434comp/arm64`<br>`crypto_kem/sikep434comp/arm64asm`<br>`crypto_kem/sikep434comp/mulx`<br>`crypto_kem/sikep434comp/mulxadx`<br>`crypto_kem/sikep434comp/x86` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `sikep503comp` | `crypto_kem/sikep503comp/amd64`<br>`crypto_kem/sikep503comp/amd64asm`<br>`crypto_kem/sikep503comp/arm`<br>`crypto_kem/sikep503comp/arm64`<br>`crypto_kem/sikep503comp/arm64asm`<br>`crypto_kem/sikep503comp/mulx`<br>`crypto_kem/sikep503comp/mulxadx`<br>`crypto_kem/sikep503comp/x86` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `sikep610comp` | `crypto_kem/sikep610comp/amd64`<br>`crypto_kem/sikep610comp/amd64asm`<br>`crypto_kem/sikep610comp/arm`<br>`crypto_kem/sikep610comp/arm64`<br>`crypto_kem/sikep610comp/arm64asm`<br>`crypto_kem/sikep610comp/mulx`<br>`crypto_kem/sikep610comp/mulxadx`<br>`crypto_kem/sikep610comp/x86` |
| `crypto_kem` | Key encapsulation mechanism (KEM) | `sikep751comp` | `crypto_kem/sikep751comp/amd64`<br>`crypto_kem/sikep751comp/amd64asm`<br>`crypto_kem/sikep751comp/arm`<br>`crypto_kem/sikep751comp/arm64`<br>`crypto_kem/sikep751comp/arm64asm`<br>`crypto_kem/sikep751comp/mulx`<br>`crypto_kem/sikep751comp/mulxadx`<br>`crypto_kem/sikep751comp/x86` |
| `crypto_sign` | Public-key digital signatures | `lattisigns512` | `crypto_sign/lattisigns512/avx` |
| `crypto_sign` | Public-key digital signatures | `luov8117404pc` | `crypto_sign/luov8117404pc/avx2` |
| `crypto_sign` | Public-key digital signatures | `luov863256pc` | `crypto_sign/luov863256pc/avx2` |
| `crypto_sign` | Public-key digital signatures | `luov890351pc` | `crypto_sign/luov890351pc/avx2` |
| `crypto_sign` | Public-key digital signatures | `mqqsig160` | `crypto_sign/mqqsig160/sse` |
| `crypto_stream` | Stream cipher | `rijn256ctr` | `crypto_stream/rijn256ctr/gil` |
| `crypto_stream` | Stream cipher | `simon128128ctr` | `crypto_stream/simon128128ctr/avx2`<br>`crypto_stream/simon128128ctr/neon`<br>`crypto_stream/simon128128ctr/sse4` |
| `crypto_stream` | Stream cipher | `simon128192ctr` | `crypto_stream/simon128192ctr/avx2`<br>`crypto_stream/simon128192ctr/neon`<br>`crypto_stream/simon128192ctr/sse4` |
| `crypto_stream` | Stream cipher | `simon128256ctr` | `crypto_stream/simon128256ctr/avx2`<br>`crypto_stream/simon128256ctr/neon`<br>`crypto_stream/simon128256ctr/sse4` |
| `crypto_stream` | Stream cipher | `simon64128ctr` | `crypto_stream/simon64128ctr/avx2`<br>`crypto_stream/simon64128ctr/neon`<br>`crypto_stream/simon64128ctr/sse4` |
| `crypto_stream` | Stream cipher | `simon6496ctr` | `crypto_stream/simon6496ctr/avx2`<br>`crypto_stream/simon6496ctr/neon`<br>`crypto_stream/simon6496ctr/sse4` |
| `crypto_stream` | Stream cipher | `speck128128ctr` | `crypto_stream/speck128128ctr/avx2`<br>`crypto_stream/speck128128ctr/avx512`<br>`crypto_stream/speck128128ctr/neon`<br>`crypto_stream/speck128128ctr/sse4` |
| `crypto_stream` | Stream cipher | `speck128192ctr` | `crypto_stream/speck128192ctr/avx2`<br>`crypto_stream/speck128192ctr/avx512`<br>`crypto_stream/speck128192ctr/neon`<br>`crypto_stream/speck128192ctr/sse4` |
| `crypto_stream` | Stream cipher | `speck128256ctr` | `crypto_stream/speck128256ctr/avx2`<br>`crypto_stream/speck128256ctr/avx512`<br>`crypto_stream/speck128256ctr/neon`<br>`crypto_stream/speck128256ctr/sse4` |
| `crypto_stream` | Stream cipher | `speck64128ctr` | `crypto_stream/speck64128ctr/avx2`<br>`crypto_stream/speck64128ctr/avx512`<br>`crypto_stream/speck64128ctr/neon`<br>`crypto_stream/speck64128ctr/sse4` |
| `crypto_stream` | Stream cipher | `speck6496ctr` | `crypto_stream/speck6496ctr/avx2`<br>`crypto_stream/speck6496ctr/avx512`<br>`crypto_stream/speck6496ctr/neon`<br>`crypto_stream/speck6496ctr/sse4` |
