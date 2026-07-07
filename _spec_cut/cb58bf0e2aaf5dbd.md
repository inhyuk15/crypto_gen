# **HS1-SIV (v2)** 

Submitted and designed by **Ted Krovetz**<sup>1</sup> ted@krovetz.net July 27, 2015 

HS1-SIV uses a new PRF called HS1 to provide authenticated encryption via Rogaway and Shrimpton’s SIV mode [7]. HS1 (mnemonic for “Hash-Stream 1”) is designed for high software speed on systems with good 32-bit processing, including Intel SSE, ARM Neon, and 32-bit architectures without SIMD support. HS1 uses a universal hash function to consume arbitrary strings and a stream cipher to produce its output. 

This document defines HS1 and how to use it in an SIV construction. HS1 takes an arbitrary input string and IV and produces a pseudorandom string of any desired length. Each different (input, IV) pair supplied to HS1 yields an independent pseudorandom stream with high probability. SIV, as defined in [7], uses a block-cipher-based PRF to create a synthetic IV (an SIV) from given associated data and plaintext. The SIV is then used to encrypt the plaintext using a block-cipherbased encryption scheme. HS1-SIV instead uses HS1 to instantiate SIV mode. Ignoring many details for the moment, if A is the associated data, M is the plaintext, and N is HS1’s IV, then the SIV is defined as the first 16 bytes of HS1(A||M, N) and ciphertext C is defined as all but the first 16 bytes of HS1(SIV, N) xor’ed with M. The SIV and ciphertext are bundled together to create the final ciphertext. If (A, M, N) is repeated, then an observer knows this fact because the scheme is deterministic and the SIV will be identical, but no security degradation otherwise occurs. Supplying N as a nonce thus improves security by masking repeated encryptions. 

HS1 does its work by pairing an almost-universal hash function with a stream cipher. When given an (input, IV) pair, HS1 uses the hash function to hash the input, it then xor’s this hash result with the stream cipher’s key and uses the HS1 IV as the stream cipher’s IV. The stream cipher produces as many bytes as desired. As long as a (hash result, IV) pair is never repeated, and the stream cipher is secure against related-key attacks, the stream cipher will produce independent pseudorandom output streams. We introduce a new hash HS1-Hash which we use for the almostuniversal phase of HS1, and Bernstein’s Chacha is used as the stream cipher [1]. 

## **1 Specification** 

The figures in this document fully specify HS1-SIV with the exception of the Chacha stream cipher. We use the Chacha version specified in ChaCha20 and Poly1305 for IETF protocols [6], and attach it to make this document self-contained. The interface defined in that document has Chacha take four inputs: A 32-byte key, an initial counter value, a 12-byte IV, and a plaintext. The ciphertext produced is the same length as the plaintext and is pseudorandom. This document adopts that interface. Chacha[r](K, c, N, X) indicates the r-round Chacha encryption of X using key K, initial counter value c, and IV N. When we simply want an n-byte pseudorandom string, we let X be n zero bytes. 

> 1 Department of Computer Science, California State University, Sacramento CA 95819. This work supported by the generous support of NSF grants CNS-1314592 and CNS-0904380. 

HS1-SIV-Encrypt[b, t, r, ℓ](K, M, A, N) Inputs: K, a non-empty string of up to 32 bytes M, a string shorter than 2<sup>64</sup> bytes A, a string shorter than 2<sup>64</sup> bytes N, a 12-byte string Output: (T, C), strings of ℓ and |M| bytes, respectively Algorithm: 1. **k** = HS1-subkeygen[b, t, r, ℓ](K) 2. M<sup>′</sup> = pad(b, A) || pad(16, M) || toStr(8, |A|) || toStr(8, |M|) 3. T = HS1[b, t, r]( **k** , M<sup>′</sup> , N, ℓ) 4. C = M ⊕ HS1[b, t, r]( **k** , T, N, 64 + |M|)[64, |M|] 

Figure 1: Encryption. The ℓ-byte string T serves as authenticator for A and M, and serves as IV for the encryption of M. If N is a nonce, then repeat encryptions yield different T and C. Algorithm parameters b, t, r, and ℓ effect security and performance. 

### **1.1 Parameters** 

There are four parameters used throughout this specification, b, t, r, ℓ. Parameter b specifies the number of bytes used in part of the hashing algorithm (larger b tends to produce higher throughput on longer messages). Parameter t selects the collision level of the hashing algorithm (higher t produces higher security and lower throughput). Parameter r specifies the number of internal rounds used by the stream cipher (higher r produces higher security and lower throughput). Parameter ℓ specifies the byte-length of synthetic IV used (higher ℓ improves security and increases ciphertext lengths by ℓ bytes). The following table names parameter sets. 

|Name|b|t|r|ℓ|
|---|---|---|---|---|
|hs1-siv-lo|64|2|8|8|
|hs1-siv|64|4|12|16|
|hs1-siv-hi|64|6|20|32|

### **1.2 Notation** 

The algorithms in this document manipulate integers, vectors of integers, and strings of bytes. Vector and string indices begin with zero. If **v** is a vector, then **v** [a] is its a-th element and **v** [a, n] is the n-element subvector beginning at index a: ( **v** [a], **v** [a + 1], . . . , **v** [a + n − 1]). Similarly, if S is a string, then S[a, n] is the n-byte substring of S beginning at index a. The number of elements in **v** and bytes in S is indicated | **v** | and |S|. Concatenation is accomplished using “||” (eg, (1, 2, 3)||(4, 5) = (1, 2, 3, 4, 5) and 0xf0||0xa8 = 0xf0a8). The bitwise exclusive-or of same-length strings A and B is A ⊕ B. A string of k zero-bytes is represented 0<sup>k</sup> . pad(n, S) = S||0<sup>k</sup> where k is the smallest non-negative integer making the length of S||0<sup>k</sup> a non-negative multiple of n bytes. toStr(n, x) is the n-byte unsigned little-endian binary representation of integer x (eg, toStr(2, 3) = 0x0300). toInts(n, S) is the vector of integers obtained by breaking S into n-byte chunks and little-endian interpreting each chunk as an unsigned integer (eg, toInts(2, 0x05000600) = (5, 6)). 

2 

HS1[b, t, r]( **k** , M, N, y) Inputs: 

**k** , a vector (KS, **k** N, **k** P, **k** A), where KS, is a string of 32 bytes, **k** N, is a vector of b/4 + 4(t − 1) integers from **`Z`** 232, **k** P, is a vector of t integers from **`Z`** 260, and **k** A, is a vector of 3t integers from **`Z`** 264 M, a string of any length N, a 12-byte string y, an integer in **`Z`** 238 Output: 

Y, a string of y bytes Algorithm: 1. Ai = HS1-Hash[b, t]( **k** N[4i, b/4], **k** P[i], **k** A[3i, 3], M) for each 0 ≤ i < t 2. Y = Chacha[r](pad(32, A0 || A1 || . . . || At−1) ⊕ Ks), 0, N, 0<sup>y</sup> ) 

Figure 2: HS1 PRF. Hash M a total of t times with different keys and combine the result with the stream cipher’s key. 

Given vectors of integers **v** 1 and **v** 2, NH( **v** 1, **v** 2) = `∑` i<sup>n</sup> =<sup>/4</sup> 1<sup>((</sup><sup>**v**1[4i −3] +</sup><sup>**v**2[4i −3]) × (</sup><sup>**v**1[4i −1] +</sup> **v** 2[4i − 1]) + ( **v** 1[4i − 2] + **v** 2[4i − 2]) × ( **v** 1[4i] + **v** 2[4i])) where n = min(| **v** 1|, | **v** 2|) and is always a multiple of four. 

## **2 Security Goals** 

HS1-SIV provides confidentiality of plaintexts and integrity of ciphertexts, associated data and public message numbers. No private message numbers are employed by HS1-SIV. If we say an adversary can win an attack against HS1-SIV by (i) guessing the key in use or (ii) causing two different encryptions to use the same synthetic IV, then the following table summarizes an adversary’s probability of success over n encryptions, each of no more than 2<sup>32</sup> bytes, or n key guesses. 

|Name|KeySearch|SIV Collision|
|---|---|---|
|hs1-siv-lo|n/2<sup>256</sup>|n<sup>2</sup>/2<sup>56</sup> +n<sup>2</sup>/2<sup>64</sup>|
|hs1-siv|n/2<sup>256</sup>|n<sup>2</sup>/2<sup>112 </sup>+n<sup>2</sup>/2<sup>128</sup>|
|hs1-siv-hi|n/2<sup>256</sup>|n<sup>2</sup>/2<sup>168 </sup>+n<sup>2</sup>/2<sup>256</sup>|

SIV is designed to provide the maximum possible robustness against nonce reuse. HS1-SIV maintains full integrity and confidentiality, except for leaking collisions of (plaintext, associated data, public message number) via collisions of ciphertexts. If two different (plaintext, associated data, public message number) triples produce the same SIV, then forgeries become possible. 

3 

HS1-Hash[b, t]( **k** N, kP, **k** A, M) Inputs: **k** N, is a vector of b/4 integers from **`Z`** 232, kP, is an integer from **`Z`** 260 **k** A, is a vector of 3 integers from **`Z`** 264 (Not used when t ≤ 4) M, a string of any length Output: Y, an 8 byte (if t ≤ 4) or 4 byte (if t > 4) string Algorithm: 1. n = max(⌈|M|/b⌉, 1) 2. Let M1, M2, . . . , Mn be strings so that M1||M2|| · · · ||Mn = M and |Mi| = b for each 1 ≤ i < n. 3. **m** i = toInts(4, pad(16, Mi)) for each 1 ≤ i ≤ n 4. ai = (NH( **k** N, **m** i) + |Mi| **mod** 16) **mod** 2<sup>60</sup> for each 1 ≤ i ≤ n 5. h = k<sup>n</sup> P<sup>+ a1kn</sup> P<sup>−1</sup> + a2k<sup>n</sup> P<sup>−2</sup> + . . . + ank<sup>0</sup> P<sup>**mod**(261 −1)</sup> 6. **if** (t ≤ 4) Y = toStr(8, h) 7. **else** Y = toStr(4, ( **k** A[0] + **k** A[1] × (h **mod** 2<sup>32</sup> ) + **k** A[2] × (h **div** 2<sup>32</sup> )) **div** 2<sup>32</sup> ) 

Figure 3: The hash family HS1-Hash is (1/2<sup>28</sup> + ℓ/b2<sup>60</sup> )-AU for all M up to ℓ bytes, when **k** N and kP are chosen randomly and t ≤ 4. The hash family is (1/2<sup>28</sup> + 1/2<sup>32</sup> + ℓ/b2<sup>60</sup> )-SU when **k** A is also randomly chosen and t > 4 (the extra 1/2<sup>32</sup> coming from Line 7, a strongly universal hash developed by Lemire [5]). 

## **8 Changes** 

Version 1 mistakenly defined Prod and listed bitlengths in the Table of Section 1.1. Version 2 replaces Prod with NH, gives bytelengths in the table of Section 1.1, and increases the zeropadding on associated data from a multiple of 16 bytes to a multiple of b bytes to accommodate static AD and to simplify message/associated-data bundling. 

7 

#### `2.3.1.  The ChaCha20 Block Function in Pseudocode` 

```
   Note: This section and a few others contain pseudocode for the
   algorithm explained in a previous section.  Every effort was made for
   the pseudocode to accurately reflect the algorithm as described in
   the preceding section.  If a conflict is still present, the textual
   explanation and the test vectors are normative.
```

```
      inner_block (state):
         Qround(state, 0, 4, 8,12)
         Qround(state, 1, 5, 9,13)
         Qround(state, 2, 6,10,14)
         Qround(state, 3, 7,11,15)
         Qround(state, 0, 5,10,15)
         Qround(state, 1, 6,11,12)
         Qround(state, 2, 7, 8,13)
         Qround(state, 3, 4, 9,14)
         end
      chacha20_block(key, counter, nonce):
         state = constants | key | counter | nonce
         working_state = state
         for i=1 upto 10
            inner_block(working_state)
            end
         state += working_state
         return serialize(state)
         end
```

```
Nir & Langley                 Informational                     [Page 8]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

#### `2.6.  Generating the Poly1305 Key Using ChaCha20` 

```
   As said in Section 2.5, it is acceptable to generate the one-time
   Poly1305 pseudorandomly.  This section defines such a method.
```

```
   To generate such a key pair (r,s), we will use the ChaCha20 block
   function described in Section 2.3.  This assumes that we have a
   256-bit session key for the Message Authentication Code (MAC)
   function, such as SK_ai and SK_ar in Internet Key Exchange Protocol
   version 2 (IKEv2) ([RFC7296]), the integrity key in the Encapsulating
   Security Payload (ESP) and Authentication Header (AH), or the
   client_write_MAC_key and server_write_MAC_key in TLS.  Any document
   that specifies the use of Poly1305 as a MAC algorithm for some
   protocol must specify that 256 bits are allocated for the integrity
   key.  Note that in the AEAD construction defined in Section 2.8, the
   same key is used for encryption and key generation, so the use of
   SK_a* or *_write_MAC_key is only for stand-alone Poly1305.
```

```
   The method is to call the block function with the following
   parameters:
```

```
   o  The 256-bit session integrity key is used as the ChaCha20 key.
```

```
   o  The block counter is set to zero.
```

```
   o  The protocol will specify a 96-bit or 64-bit nonce.  This MUST be
      unique per invocation with the same key, so it MUST NOT be
      randomly generated.  A counter is a good way to implement this,
      but other methods, such as a Linear Feedback Shift Register (LFSR)
      are also acceptable.  ChaCha20 as specified here requires a 96-bit
      nonce.  So if the provided nonce is only 64-bit, then the first 32
      bits of the nonce will be set to a constant number.  This will
      usually be zero, but for protocols with multiple senders it may be
      different for each sender, but should be the same for all
      invocations of the function with the same key by a particular
      sender.
```

```
   After running the block function, we have a 512-bit state.  We take
   the first 256 bits or the serialized state, and use those as the one-
   time Poly1305 key: the first 128 bits are clamped and form "r", while
   the next 128 bits become "s".  The other 256 bits are discarded.
```

```
Nir & Langley                 Informational                    [Page 17]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   Note that while many protocols have provisions for a nonce for
   encryption algorithms (often called Initialization Vectors, or IVs),
   they usually don’t have such a provision for the MAC function.  In
   that case, the per-invocation nonce will have to come from somewhere
   else, such as a message counter.
```

```
2.6.1.  Poly1305 Key Generation in Pseudocode
```

```
      poly1305_key_gen(key,nonce):
         counter = 0
         block = chacha20_block(key,counter,nonce)
         return block[0..31]
         end
```

```
2.6.2.  Poly1305 Key Generation Test Vector
   For this example, we’ll set:
```

```
  Key:
  000  80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f  ................
  016  90 91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e 9f  ................
   Nonce:
   000  00 00 00 00 00 01 02 03 04 05 06 07              ............
   The ChaCha state setup with key, nonce, and block counter zero:
         61707865  3320646e  79622d32  6b206574
         83828180  87868584  8b8a8988  8f8e8d8c
         93929190  97969594  9b9a9998  9f9e9d9c
         00000000  00000000  03020100  07060504
   The ChaCha state after 20 rounds:
         8ba0d58a  cc815f90  27405081  7194b24a
         37b633a8  a50dfde3  e2b8db08  46a6d1fd
         7da03782  9183a233  148ad271  b46773d1
         3cc1875a  8607def1  ca5c3086  7085eb87
```

```
  Output bytes:
  000  8a d5 a0 8b 90 5f 81 cc 81 50 40 27 4a b2 94 71  ....._...P@’J..q
  016  a8 33 b6 37 e3 fd 0d a5 08 db b8 e2 fd d1 a6 46  .3.7...........F
```

```
   And that output is also the 32-byte one-time key used for Poly1305.
```

```
2.7.  A Pseudorandom Function for Crypto Suites based on ChaCha/Poly1305
```

```
   Some protocols, such as IKEv2 ([RFC7296]), require a Pseudorandom
   Function (PRF), mostly for key derivation.  In the IKEv2 definition,
   a PRF is a function that accepts a variable-length key and a
```

```
Nir & Langley                 Informational                    [Page 18]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   variable-length input, and returns a fixed-length output.  Most
   commonly, Hashed MAC (HMAC) constructions are used for this purpose,
   and often the same function is used for both message authentication
   and PRF.
```

```
   Poly1305 is not a suitable choice for a PRF.  Poly1305 prohibits
   using the same key twice, whereas the PRF in IKEv2 is used multiple
   times with the same key.  Additionally, unlike HMAC, Poly1305 is
   biased, so using it for key derivation would reduce the security of
   the symmetric encryption.
```

```
   Chacha20 could be used as a key-derivation function, by generating an
   arbitrarily long keystream.  However, that is not what protocols such
   as IKEv2 require.
```

```
   For this reason, this document does not specify a PRF and recommends
   that crypto suites use some other PRF such as PRF_HMAC_SHA2_256 (see
   Section 2.1.2 of [RFC4868]).
```

#### `2.8.  AEAD Construction` 

```
   AEAD_CHACHA20_POLY1305 is an authenticated encryption with additional
   data algorithm.  The inputs to AEAD_CHACHA20_POLY1305 are:
```

```
   o  A 256-bit key
```

```
   o  A 96-bit nonce -- different for each invocation with the same key
```

```
   o  An arbitrary length plaintext
```

```
   o  Arbitrary length additional authenticated data (AAD)
```

```
   Some protocols may have unique per-invocation inputs that are not 96
   bits in length.  For example, IPsec may specify a 64-bit nonce.  In
   such a case, it is up to the protocol document to define how to
   transform the protocol nonce into a 96-bit nonce, for example, by
   concatenating a constant value.
```

```
   The ChaCha20 and Poly1305 primitives are combined into an AEAD that
   takes a 256-bit key and 96-bit nonce as follows:
```

```
   o  First, a Poly1305 one-time key is generated from the 256-bit key
      and nonce using the procedure described in Section 2.6.
```

```
   o  Next, the ChaCha20 encryption function is called to encrypt the
      plaintext, using the same key and nonce, and with the initial
      counter set to 1.
```

```
Nir & Langley                 Informational                    [Page 19]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

- `Finally, the Poly1305 function is called with the Poly1305 key calculated above, and a message constructed as a concatenation of the following:` 

```
      *  The AAD
```

- `padding1 -- the padding is up to 15 zero bytes, and it brings the total length so far to an integral multiple of 16.  If the length of the AAD was already an integral multiple of 16 bytes, this field is zero-length.` 

```
      *  The ciphertext
```

- `padding2 -- the padding is up to 15 zero bytes, and it brings the total length so far to an integral multiple of 16.  If the length of the ciphertext was already an integral multiple of 16 bytes, this field is zero-length.` 

- `The length of the additional data in octets (as a 64-bit little-endian integer).` 

- `The length of the ciphertext in octets (as a 64-bit littleendian integer).` 

```
   The output from the AEAD is twofold:
```

```
   o  A ciphertext of the same length as the plaintext.
```

- `A 128-bit tag, which is the output of the Poly1305 function.` 

```
   Decryption is similar with the following differences:
```

```
   o  The roles of ciphertext and plaintext are reversed, so the
      ChaCha20 encryption function is applied to the ciphertext,
      producing the plaintext.
```

- `The Poly1305 function is still run on the AAD and the ciphertext, not the plaintext.` 

- `The calculated tag is bitwise compared to the received tag.  The message is authenticated if and only if the tags match.` 

```
   A few notes about this design:
```

`1.  The amount of encrypted data possible in a single invocation is 2^32-1 blocks of 64 bytes each, because of the size of the block counter field in the ChaCha20 block function.  This gives a total of 247,877,906,880 bytes, or nearly 256 GB.  This should be` 

```
Nir & Langley                 Informational                    [Page 20]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
       enough for traffic protocols such as IPsec and TLS, but may be
       too small for file and/or disk encryption.  For such uses, we can
       return to the original design, reduce the nonce to 64 bits, and
       use the integer at position 13 as the top 32 bits of a 64-bit
       block counter, increasing the total message size to over a
       million petabytes (1,180,591,620,717,411,303,360 bytes to be
       exact).
```

```
   2.  Despite the previous item, the ciphertext length field in the
       construction of the buffer on which Poly1305 runs limits the
       ciphertext (and hence, the plaintext) size to 2^64 bytes, or
       sixteen thousand petabytes (18,446,744,073,709,551,616 bytes to
       be exact).
```

```
   The AEAD construction in this section is a novel composition of
   ChaCha20 and Poly1305.  A security analysis of this composition is
   given in [Procter].
```

```
   Here is a list of the parameters for this construction as defined in
   Section 4 of RFC 5116:
```

```
   o  K_LEN (key length) is 32 octets.
```

```
   o  P_MAX (maximum size of the plaintext) is 247,877,906,880 bytes, or
      nearly 256 GB.
```

```
   o  A_MAX (maximum size of the associated data) is set to 2^64-1
      octets by the length field for associated data.
   o  N_MIN = N_MAX = 12 octets.
```

```
   o  C_MAX = P_MAX + tag length = 247,877,906,896 octets.
```

```
   Distinct AAD inputs (as described in Section 3.3 of RFC 5116) shall
   be concatenated into a single input to AEAD_CHACHA20_POLY1305.  It is
   up to the application to create a structure in the AAD input if it is
   needed.
```

```
2.8.1.  Pseudocode for the AEAD Construction
      pad16(x):
         if (len(x) % 16)==0
            then return NULL
            else return copies(0, 16-(len(x)%16))
         end
```

```
Nir & Langley                 Informational                    [Page 21]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
      chacha20_aead_encrypt(aad, key, iv, constant, plaintext):
         nonce = constant | iv
         otk = poly1305_key_gen(key, nonce)
         ciphertext = chacha20_encrypt(key, 1, nonce, plaintext)
         mac_data = aad | pad16(aad)
         mac_data |= ciphertext | pad16(ciphertext)
         mac_data |= num_to_4_le_bytes(aad.length)
         mac_data |= num_to_4_le_bytes(ciphertext.length)
         tag = poly1305_mac(mac_data, otk)
         return (ciphertext, tag)
```

```
2.8.2.  Example and Test Vector for AEAD_CHACHA20_POLY1305
```

```
   For a test vector, we will use the following inputs to the
   AEAD_CHACHA20_POLY1305 function:
```

```
  Plaintext:
```

```
  000  4c 61 64 69 65 73 20 61 6e 64 20 47 65 6e 74 6c  Ladies and Gentl
  016  65 6d 65 6e 20 6f 66 20 74 68 65 20 63 6c 61 73  emen of the clas
  032  73 20 6f 66 20 27 39 39 3a 20 49 66 20 49 20 63  s of ’99: If I c
  048  6f 75 6c 64 20 6f 66 66 65 72 20 79 6f 75 20 6f  ould offer you o
  064  6e 6c 79 20 6f 6e 65 20 74 69 70 20 66 6f 72 20  nly one tip for
  080  74 68 65 20 66 75 74 75 72 65 2c 20 73 75 6e 73  the future, suns
  096  63 72 65 65 6e 20 77 6f 75 6c 64 20 62 65 20 69  creen would be i
  112  74 2e                                            t.
   AAD:
   000  50 51 52 53 c0 c1 c2 c3 c4 c5 c6 c7              PQRS........
  Key:
  000  80 81 82 83 84 85 86 87 88 89 8a 8b 8c 8d 8e 8f  ................
  016  90 91 92 93 94 95 96 97 98 99 9a 9b 9c 9d 9e 9f  ................
   IV:
   000  40 41 42 43 44 45 46 47                          @ABCDEFG
   32-bit fixed-common part:
   000  07 00 00 00                                      ....
   Setup for generating Poly1305 one-time key (sender id=7):
       61707865  3320646e  79622d32  6b206574
       83828180  87868584  8b8a8988  8f8e8d8c
       93929190  97969594  9b9a9998  9f9e9d9c
       00000000  00000007  43424140  47464544
```

```
Nir & Langley                 Informational                    [Page 22]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   After generating Poly1305 one-time key:
       252bac7b  af47b42d  557ab609  8455e9a4
       73d6e10a  ebd97510  7875932a  ff53d53e
       decc7ea2  b44ddbad  e49c17d1  d8430bc9
       8c94b7bc  8b7d4b4b  3927f67d  1669a432
  Poly1305 Key:
  000  7b ac 2b 25 2d b4 47 af 09 b6 7a 55 a4 e9 55 84  {.+%-.G...zU..U.
  016  0a e1 d6 73 10 75 d9 eb 2a 93 75 78 3e d5 53 ff  ...s.u..*.ux>.S.
  Poly1305 r =  455e9a4057ab6080f47b42c052bac7b
  Poly1305 s = ff53d53e7875932aebd9751073d6e10a
```

```
   keystream bytes:
   9f:7b:e9:5d:01:fd:40:ba:15:e2:8f:fb:36:81:0a:ae:
   c1:c0:88:3f:09:01:6e:de:dd:8a:d0:87:55:82:03:a5:
   4e:9e:cb:38:ac:8e:5e:2b:b8:da:b2:0f:fa:db:52:e8:
   75:04:b2:6e:be:69:6d:4f:60:a4:85:cf:11:b8:1b:59:
   fc:b1:c4:5f:42:19:ee:ac:ec:6a:de:c3:4e:66:69:78:
   8e:db:41:c4:9c:a3:01:e1:27:e0:ac:ab:3b:44:b9:cf:
   5c:86:bb:95:e0:6b:0d:f2:90:1a:b6:45:e4:ab:e6:22:
   15:38
```

```
  Ciphertext:
  000  d3 1a 8d 34 64 8e 60 db 7b 86 af bc 53 ef 7e c2  ...4d.‘.{...S.˜.
  016  a4 ad ed 51 29 6e 08 fe a9 e2 b5 a7 36 ee 62 d6  ...Q)n......6.b.
  032  3d be a4 5e 8c a9 67 12 82 fa fb 69 da 92 72 8b  =..^..g....i..r.
  048  1a 71 de 0a 9e 06 0b 29 05 d6 a5 b6 7e cd 3b 36  .q.....)....˜.;6
  064  92 dd bd 7f 2d 77 8b 8c 98 03 ae e3 28 09 1b 58  ....-w......(..X
  080  fa b3 24 e4 fa d6 75 94 55 85 80 8b 48 31 d7 bc  ..$...u.U...H1..
  096  3f f4 de f0 8e 4b 7a 9d e5 76 d2 65 86 ce c6 4b  ?....Kz..v.e...K
  112  61 16                                            a.
  AEAD Construction for Poly1305:
  000  50 51 52 53 c0 c1 c2 c3 c4 c5 c6 c7 00 00 00 00  PQRS............
  016  d3 1a 8d 34 64 8e 60 db 7b 86 af bc 53 ef 7e c2  ...4d.‘.{...S.˜.
  032  a4 ad ed 51 29 6e 08 fe a9 e2 b5 a7 36 ee 62 d6  ...Q)n......6.b.
  048  3d be a4 5e 8c a9 67 12 82 fa fb 69 da 92 72 8b  =..^..g....i..r.
  064  1a 71 de 0a 9e 06 0b 29 05 d6 a5 b6 7e cd 3b 36  .q.....)....˜.;6
  080  92 dd bd 7f 2d 77 8b 8c 98 03 ae e3 28 09 1b 58  ....-w......(..X
  096  fa b3 24 e4 fa d6 75 94 55 85 80 8b 48 31 d7 bc  ..$...u.U...H1..
  112  3f f4 de f0 8e 4b 7a 9d e5 76 d2 65 86 ce c6 4b  ?....Kz..v.e...K
  128  61 16 00 00 00 00 00 00 00 00 00 00 00 00 00 00  a...............
  144  0c 00 00 00 00 00 00 00 72 00 00 00 00 00 00 00  ........r.......
   Note the four zero bytes in line 000 and the 14 zero bytes in line
   128
```

```
Nir & Langley                 Informational                    [Page 23]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   Tag:
```

```
   1a:e1:0b:59:4f:09:e2:6a:7e:90:2e:cb:d0:60:06:91
```

#### `3.  Implementation Advice` 

```
   Each block of ChaCha20 involves 16 move operations and one increment
   operation for loading the state, 80 each of XOR, addition and Roll
   operations for the rounds, 16 more add operations and 16 XOR
   operations for protecting the plaintext.  Section 2.3 describes the
   ChaCha block function as "adding the original input words".  This
   implies that before starting the rounds on the ChaCha state, we copy
   it aside, only to add it in later.  This is correct, but we can save
   a few operations if we instead copy the state and do the work on the
   copy.  This way, for the next block you don’t need to recreate the
   state, but only to increment the block counter.  This saves
   approximately 5.5% of the cycles.
```

```
   It is not recommended to use a generic big number library such as the
   one in OpenSSL for the arithmetic operations in Poly1305.  Such
   libraries use dynamic allocation to be able to handle an integer of
   any size, but that flexibility comes at the expense of performance as
   well as side-channel security.  More efficient implementations that
   run in constant time are available, one of them in D. J. Bernstein’s
   own library, NaCl ([NaCl]).  A constant-time but not optimal approach
   would be to naively implement the arithmetic operations for 288-bit
   integers, because even a naive implementation will not exceed 2^288
   in the multiplication of (acc+block) and r.  An efficient constant-
   time implementation can be found in the public domain library
   poly1305-donna ([Poly1305_Donna]).
```

#### `4.  Security Considerations` 

```
   The ChaCha20 cipher is designed to provide 256-bit security.
```

```
   The Poly1305 authenticator is designed to ensure that forged messages
   are rejected with a probability of 1-(n/(2^102)) for a 16n-byte
   message, even after sending 2^64 legitimate messages, so it is
   SUF-CMA (strong unforgeability against chosen-message attacks) in the
   terminology of [AE].
```

```
   Proving the security of either of these is beyond the scope of this
   document.  Such proofs are available in the referenced academic
   papers ([ChaCha], [Poly1305], [LatinDances], [LatinDances2], and
   [Zhenqing2012]).
```

```
   The most important security consideration in implementing this
   document is the uniqueness of the nonce used in ChaCha20.  Counters
   and LFSRs are both acceptable ways of generating unique nonces, as is
```

```
Nir & Langley                 Informational                    [Page 24]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   encrypting a counter using a 64-bit cipher such as DES.  Note that it
   is not acceptable to use a truncation of a counter encrypted with a
   128-bit or 256-bit cipher, because such a truncation may repeat after
   a short time.
```

```
   Consequences of repeating a nonce: If a nonce is repeated, then both
   the one-time Poly1305 key and the keystream are identical between the
   messages.  This reveals the XOR of the plaintexts, because the XOR of
   the plaintexts is equal to the XOR of the ciphertexts.
```

```
   The Poly1305 key MUST be unpredictable to an attacker.  Randomly
   generating the key would fulfill this requirement, except that
   Poly1305 is often used in communications protocols, so the receiver
   should know the key.  Pseudorandom number generation such as by
   encrypting a counter is acceptable.  Using ChaCha with a secret key
   and a nonce is also acceptable.
```

```
   The algorithms presented here were designed to be easy to implement
   in constant time to avoid side-channel vulnerabilities.  The
   operations used in ChaCha20 are all additions, XORs, and fixed
   rotations.  All of these can and should be implemented in constant
   time.  Access to offsets into the ChaCha state and the number of
   operations do not depend on any property of the key, eliminating the
   chance of information about the key leaking through the timing of
   cache misses.
```

```
   For Poly1305, the operations are addition, multiplication. and
   modulus, all on numbers with greater than 128 bits.  This can be done
   in constant time, but a naive implementation (such as using some
   generic big number library) will not be constant time.  For example,
   if the multiplication is performed as a separate operation from the
   modulus, the result will sometimes be under 2^256 and sometimes be
   above 2^256.  Implementers should be careful about timing side-
   channels for Poly1305 by using the appropriate implementation of
   these operations.
```

```
   Validating the authenticity of a message involves a bitwise
   comparison of the calculated tag with the received tag.  In most use
   cases, nonces and AAD contents are not "used up" until a valid
   message is received.  This allows an attacker to send multiple
   identical messages with different tags until one passes the tag
   comparison.  This is hard if the attacker has to try all 2^128
   possible tags one by one.  However, if the timing of the tag
   comparison operation reveals how long a prefix of the calculated and
   received tags is identical, the number of messages can be reduced
   significantly.  For this reason, with online protocols,
```

```
Nir & Langley                 Informational                    [Page 25]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   implementation MUST use a constant-time comparison function rather
   than relying on optimized but insecure library functions such as the
   C language’s memcmp().
```

#### `5.  IANA Considerations` 

```
   IANA has assigned an entry in the "Authenticated Encryption with
   Associated Data (AEAD) Parameters" registry with 29 as the Numeric
   ID, "AEAD_CHACHA20_POLY1305" as the name, and this document as
   reference.
```

#### `Tag:` 

```
  000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
```

```
Nir & Langley                 Informational                    [Page 35]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
  Test Vector #2:
  ==============
```

#### `One-time Poly1305 Key:` 

```
  000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  016  36 e5 f6 b5 c5 e0 60 70 f0 ef ca 96 22 7a 86 3e  6.....‘p...."z.>
```

```
  Text to MAC:
```

```
  000  41 6e 79 20 73 75 62 6d 69 73 73 69 6f 6e 20 74  Any submission t
  016  6f 20 74 68 65 20 49 45 54 46 20 69 6e 74 65 6e  o the IETF inten
  032  64 65 64 20 62 79 20 74 68 65 20 43 6f 6e 74 72  ded by the Contr
  048  69 62 75 74 6f 72 20 66 6f 72 20 70 75 62 6c 69  ibutor for publi
  064  63 61 74 69 6f 6e 20 61 73 20 61 6c 6c 20 6f 72  cation as all or
  080  20 70 61 72 74 20 6f 66 20 61 6e 20 49 45 54 46   part of an IETF
  096  20 49 6e 74 65 72 6e 65 74 2d 44 72 61 66 74 20   Internet-Draft
  112  6f 72 20 52 46 43 20 61 6e 64 20 61 6e 79 20 73  or RFC and any s
  128  74 61 74 65 6d 65 6e 74 20 6d 61 64 65 20 77 69  tatement made wi
  144  74 68 69 6e 20 74 68 65 20 63 6f 6e 74 65 78 74  thin the context
  160  20 6f 66 20 61 6e 20 49 45 54 46 20 61 63 74 69   of an IETF acti
  176  76 69 74 79 20 69 73 20 63 6f 6e 73 69 64 65 72  vity is consider
  192  65 64 20 61 6e 20 22 49 45 54 46 20 43 6f 6e 74  ed an "IETF Cont
  208  72 69 62 75 74 69 6f 6e 22 2e 20 53 75 63 68 20  ribution". Such
  224  73 74 61 74 65 6d 65 6e 74 73 20 69 6e 63 6c 75  statements inclu
  240  64 65 20 6f 72 61 6c 20 73 74 61 74 65 6d 65 6e  de oral statemen
  256  74 73 20 69 6e 20 49 45 54 46 20 73 65 73 73 69  ts in IETF sessi
  272  6f 6e 73 2c 20 61 73 20 77 65 6c 6c 20 61 73 20  ons, as well as
  288  77 72 69 74 74 65 6e 20 61 6e 64 20 65 6c 65 63  written and elec
  304  74 72 6f 6e 69 63 20 63 6f 6d 6d 75 6e 69 63 61  tronic communica
  320  74 69 6f 6e 73 20 6d 61 64 65 20 61 74 20 61 6e  tions made at an
  336  79 20 74 69 6d 65 20 6f 72 20 70 6c 61 63 65 2c  y time or place,
  352  20 77 68 69 63 68 20 61 72 65 20 61 64 64 72 65   which are addre
  368  73 73 65 64 20 74 6f                             ssed to
```

```
  Tag:
```

```
  000  36 e5 f6 b5 c5 e0 60 70 f0 ef ca 96 22 7a 86 3e  6.....‘p...."z.>
```

```
Nir & Langley                 Informational                    [Page 36]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
  Test Vector #3:
```

```
  ==============
```

#### `One-time Poly1305 Key:` 

```
  000  36 e5 f6 b5 c5 e0 60 70 f0 ef ca 96 22 7a 86 3e  6.....‘p...."z.>
  016  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
```

```
  Text to MAC:
```

```
  000  41 6e 79 20 73 75 62 6d 69 73 73 69 6f 6e 20 74  Any submission t
  016  6f 20 74 68 65 20 49 45 54 46 20 69 6e 74 65 6e  o the IETF inten
  032  64 65 64 20 62 79 20 74 68 65 20 43 6f 6e 74 72  ded by the Contr
  048  69 62 75 74 6f 72 20 66 6f 72 20 70 75 62 6c 69  ibutor for publi
  064  63 61 74 69 6f 6e 20 61 73 20 61 6c 6c 20 6f 72  cation as all or
  080  20 70 61 72 74 20 6f 66 20 61 6e 20 49 45 54 46   part of an IETF
  096  20 49 6e 74 65 72 6e 65 74 2d 44 72 61 66 74 20   Internet-Draft
  112  6f 72 20 52 46 43 20 61 6e 64 20 61 6e 79 20 73  or RFC and any s
  128  74 61 74 65 6d 65 6e 74 20 6d 61 64 65 20 77 69  tatement made wi
  144  74 68 69 6e 20 74 68 65 20 63 6f 6e 74 65 78 74  thin the context
  160  20 6f 66 20 61 6e 20 49 45 54 46 20 61 63 74 69   of an IETF acti
  176  76 69 74 79 20 69 73 20 63 6f 6e 73 69 64 65 72  vity is consider
  192  65 64 20 61 6e 20 22 49 45 54 46 20 43 6f 6e 74  ed an "IETF Cont
  208  72 69 62 75 74 69 6f 6e 22 2e 20 53 75 63 68 20  ribution". Such
  224  73 74 61 74 65 6d 65 6e 74 73 20 69 6e 63 6c 75  statements inclu
  240  64 65 20 6f 72 61 6c 20 73 74 61 74 65 6d 65 6e  de oral statemen
  256  74 73 20 69 6e 20 49 45 54 46 20 73 65 73 73 69  ts in IETF sessi
  272  6f 6e 73 2c 20 61 73 20 77 65 6c 6c 20 61 73 20  ons, as well as
  288  77 72 69 74 74 65 6e 20 61 6e 64 20 65 6c 65 63  written and elec
  304  74 72 6f 6e 69 63 20 63 6f 6d 6d 75 6e 69 63 61  tronic communica
  320  74 69 6f 6e 73 20 6d 61 64 65 20 61 74 20 61 6e  tions made at an
  336  79 20 74 69 6d 65 20 6f 72 20 70 6c 61 63 65 2c  y time or place,
  352  20 77 68 69 63 68 20 61 72 65 20 61 64 64 72 65   which are addre
  368  73 73 65 64 20 74 6f                             ssed to
```

```
  Tag:
  000  f3 47 7e 7c d9 54 17 af 89 a6 b8 79 4c 31 0c f0  .G˜|.T.....yL1..
```

```
Nir & Langley                 Informational                    [Page 37]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
  Test Vector #4:
  ==============
```

```
  One-time Poly1305 Key:
  000  1c 92 40 a5 eb 55 d3 8a f3 33 88 86 04 f6 b5 f0  ..@..U...3......
  016  47 39 17 c1 40 2b 80 09 9d ca 5c bc 20 70 75 c0  G9..@+....\. pu.
```

```
  Text to MAC:
```

```
  000  27 54 77 61 73 20 62 72 69 6c 6c 69 67 2c 20 61  ’Twas brillig, a
  016  6e 64 20 74 68 65 20 73 6c 69 74 68 79 20 74 6f  nd the slithy to
  032  76 65 73 0a 44 69 64 20 67 79 72 65 20 61 6e 64  ves.Did gyre and
  048  20 67 69 6d 62 6c 65 20 69 6e 20 74 68 65 20 77   gimble in the w
  064  61 62 65 3a 0a 41 6c 6c 20 6d 69 6d 73 79 20 77  abe:.All mimsy w
  080  65 72 65 20 74 68 65 20 62 6f 72 6f 67 6f 76 65  ere the borogove
  096  73 2c 0a 41 6e 64 20 74 68 65 20 6d 6f 6d 65 20  s,.And the mome
  112  72 61 74 68 73 20 6f 75 74 67 72 61 62 65 2e     raths outgrabe.
  Tag:
  000  45 41 66 9a 7e aa ee 61 e7 08 dc 7c bc c5 eb 62  EAf.˜..a...|...b
```

```
   Test Vector #5: If one uses 130-bit partial reduction, does the code
   handle the case where partially reduced final result is not fully
   reduced?
```

```
   R:
   02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   S:
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   data:
```

```
   FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
   tag:
   03 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

```
   Test Vector #6: What happens if addition of s overflows modulo 2^128?
```

```
   R:
   02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   S:
   FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
   data:
   02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   tag:
   03 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

```
Nir & Langley                 Informational                    [Page 38]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   Test Vector #7: What happens if data limb is all ones and there is
   carry from lower limb?
```

```
   R:
   01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   S:
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   data:
   FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
   F0 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
   11 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   tag:
   05 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

```
   Test Vector #8: What happens if final result from polynomial part is
   exactly 2^130-5?
```

```
   R:
```

```
   01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   S:
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   data:
   FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
   FB FE FE FE FE FE FE FE FE FE FE FE FE FE FE FE
   01 01 01 01 01 01 01 01 01 01 01 01 01 01 01 01
   tag:
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

```
   Test Vector #9: What happens if final result from polynomial part is
   exactly 2^130-6?
```

```
   R:
   02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   S:
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   data:
   FD FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
   tag:
```

```
   FA FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
```

```
Nir & Langley                 Informational                    [Page 39]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   Test Vector #10: What happens if 5*H+L-type reduction produces
   131-bit intermediate result?
```

```
   R:
   01 00 00 00 00 00 00 00 04 00 00 00 00 00 00 00
   S:
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   data:
   E3 35 94 D7 50 5E 43 B9 00 00 00 00 00 00 00 00
   33 94 D7 50 5E 43 79 CD 01 00 00 00 00 00 00 00
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   01 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   tag:
   14 00 00 00 00 00 00 00 55 00 00 00 00 00 00 00
```

```
   Test Vector #11: What happens if 5*H+L-type reduction produces
   131-bit final result?
```

```
   R:
   01 00 00 00 00 00 00 00 04 00 00 00 00 00 00 00
   S:
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   data:
   E3 35 94 D7 50 5E 43 B9 00 00 00 00 00 00 00 00
   33 94 D7 50 5E 43 79 CD 01 00 00 00 00 00 00 00
   00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
   tag:
   13 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

```
A.4.  Poly1305 Key Generation Using ChaCha20
  Test Vector #1:
  ==============
```

```
  The key:
  000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  016  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
```

```
  The nonce:
  000  00 00 00 00 00 00 00 00 00 00 00 00              ............
```

```
  Poly1305 one-time key:
  000  76 b8 e0 ad a0 f1 3d 90 40 5d 6a e5 53 86 bd 28  v.....=.@]j.S..(
  016  bd d2 19 b8 a0 8d ed 1a a8 36 ef cc 8b 77 0d c7  .........6...w..
```

```
Nir & Langley                 Informational                    [Page 40]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
  Test Vector #2:
  ==============
```

```
  The key:
  000  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  016  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01  ................
  The nonce:
  000  00 00 00 00 00 00 00 00 00 00 00 02              ............
```

```
  Poly1305 one-time key:
  000  ec fa 25 4f 84 5f 64 74 73 d3 cb 14 0d a9 e8 76  ..%O._dts......v
  016  06 cb 33 06 6c 44 7b 87 bc 26 66 dd e3 fb b7 39  ..3.lD{..&f....9
  Test Vector #3:
  ==============
```

```
  The key:
  000  1c 92 40 a5 eb 55 d3 8a f3 33 88 86 04 f6 b5 f0  ..@..U...3......
  016  47 39 17 c1 40 2b 80 09 9d ca 5c bc 20 70 75 c0  G9..@+....\. pu.
  The nonce:
  000  00 00 00 00 00 00 00 00 00 00 00 02              ............
```

```
  Poly1305 one-time key:
  000  96 5e 3b c6 f9 ec 7e d9 56 08 08 f4 d2 29 f9 4b  .^;...˜.V....).K
  016  13 7f f2 75 ca 9b 3f cb dd 59 de aa d2 33 10 ae  ...u..?..Y...3..
A.5.  ChaCha20-Poly1305 AEAD Decryption
```

```
   Below we see decrypting a message.  We receive a ciphertext, a nonce,
   and a tag.  We know the key.  We will check the tag and then
   (assuming that it validates) decrypt the ciphertext.  In this
   particular protocol, we’ll assume that there is no padding of the
   plaintext.
```

```
Nir & Langley                 Informational                    [Page 41]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
  The key:
```

```
  000  1c 92 40 a5 eb 55 d3 8a f3 33 88 86 04 f6 b5 f0  ..@..U...3......
  016  47 39 17 c1 40 2b 80 09 9d ca 5c bc 20 70 75 c0  G9..@+....\. pu.
```

#### `Ciphertext:` 

```
  000  64 a0 86 15 75 86 1a f4 60 f0 62 c7 9b e6 43 bd  d...u...‘.b...C.
  016  5e 80 5c fd 34 5c f3 89 f1 08 67 0a c7 6c 8c b2  ^.\.4\....g..l..
  032  4c 6c fc 18 75 5d 43 ee a0 9e e9 4e 38 2d 26 b0  Ll..u]C....N8-&.
  048  bd b7 b7 3c 32 1b 01 00 d4 f0 3b 7f 35 58 94 cf  ...<2.....;.5X..
  064  33 2f 83 0e 71 0b 97 ce 98 c8 a8 4a bd 0b 94 81  3/..q......J....
  080  14 ad 17 6e 00 8d 33 bd 60 f9 82 b1 ff 37 c8 55  ...n..3.‘....7.U
  096  97 97 a0 6e f4 f0 ef 61 c1 86 32 4e 2b 35 06 38  ...n...a..2N+5.8
  112  36 06 90 7b 6a 7c 02 b0 f9 f6 15 7b 53 c8 67 e4  6..{j|.....{S.g.
  128  b9 16 6c 76 7b 80 4d 46 a5 9b 52 16 cd e7 a4 e9  ..lv{.MF..R.....
  144  90 40 c5 a4 04 33 22 5e e2 82 a1 b0 a0 6c 52 3e  .@...3"^.....lR>
  160  af 45 34 d7 f8 3f a1 15 5b 00 47 71 8c bc 54 6a  .E4..?..[.Gq..Tj
  176  0d 07 2b 04 b3 56 4e ea 1b 42 22 73 f5 48 27 1a  ..+..VN..B"s.H’.
  192  0b b2 31 60 53 fa 76 99 19 55 eb d6 31 59 43 4e  ..1‘S.v..U..1YCN
  208  ce bb 4e 46 6d ae 5a 10 73 a6 72 76 27 09 7a 10  ..NFm.Z.s.rv’.z.
  224  49 e6 17 d9 1d 36 10 94 fa 68 f0 ff 77 98 71 30  I....6...h..w.q0
  240  30 5b ea ba 2e da 04 df 99 7b 71 4d 6c 6f 2c 29  0[.......{qMlo,)
  256  a6 ad 5c b4 02 2b 02 70 9b                       ..\..+.p.
```

```
  The nonce:
  000  00 00 00 00 01 02 03 04 05 06 07 08              ............
```

```
  The AAD:
```

```
  000  f3 33 88 86 00 00 00 00 00 00 4e 91              .3........N.
```

```
  Received Tag:
```

```
  000  ee ad 9d 67 89 0c bb 22 39 23 36 fe a1 85 1f 38  ...g..."9#6....8
```

```
Nir & Langley                 Informational                    [Page 42]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

|`First, we calc`|`ulate the one-time Poly1305 key`|
|---|---|
|`@@@  ChaCha sta`|`te with key setup`|
|`61707865`|`3320646e  79622d32  6b206574`|
|`a540921c`|`8ad355eb  868833f3  f0b5f604`|
|`c1173947`|`09802b40  bc5cca9d  c0757020`|
|`00000000`|`00000000  04030201  08070605`|
|`@@@  ChaCha sta`|`te after 20 rounds`|
|`a94af0bd`|`89dee45c  b64bb195  afec8fa1`|
|`508f4726`|`63f554c0  1ea2c0db  aa721526`|
|`11b1e514`|`a0bacc0f  828a6015  d7825481`|
|`e8a4a850`|`d9dcbbd6  4c2de33a  f8ccd912`|
|`@@@ out bytes:`||
|`bd:f0:4a:a9:5c:`|`e4:de:89:95:b1:4b:b6:a1:8f:ec:af:`|
|`26:47:8f:50:c0:`|`54:f5:63:db:c0:a2:1e:26:15:72:aa`|

```
  Poly1305 one-time key:
  000  bd f0 4a a9 5c e4 de 89 95 b1 4b b6 a1 8f ec af  ..J.\.....K.....
  016  26 47 8f 50 c0 54 f5 63 db c0 a2 1e 26 15 72 aa  &G.P.T.c....&.r.
   Next, we construct the AEAD buffer
```

```
  Poly1305 Input:
  000  f3 33 88 86 00 00 00 00 00 00 4e 91 00 00 00 00  .3........N.....
  016  64 a0 86 15 75 86 1a f4 60 f0 62 c7 9b e6 43 bd  d...u...‘.b...C.
  032  5e 80 5c fd 34 5c f3 89 f1 08 67 0a c7 6c 8c b2  ^.\.4\....g..l..
  048  4c 6c fc 18 75 5d 43 ee a0 9e e9 4e 38 2d 26 b0  Ll..u]C....N8-&.
  064  bd b7 b7 3c 32 1b 01 00 d4 f0 3b 7f 35 58 94 cf  ...<2.....;.5X..
  080  33 2f 83 0e 71 0b 97 ce 98 c8 a8 4a bd 0b 94 81  3/..q......J....
  096  14 ad 17 6e 00 8d 33 bd 60 f9 82 b1 ff 37 c8 55  ...n..3.‘....7.U
  112  97 97 a0 6e f4 f0 ef 61 c1 86 32 4e 2b 35 06 38  ...n...a..2N+5.8
  128  36 06 90 7b 6a 7c 02 b0 f9 f6 15 7b 53 c8 67 e4  6..{j|.....{S.g.
  144  b9 16 6c 76 7b 80 4d 46 a5 9b 52 16 cd e7 a4 e9  ..lv{.MF..R.....
  160  90 40 c5 a4 04 33 22 5e e2 82 a1 b0 a0 6c 52 3e  .@...3"^.....lR>
  176  af 45 34 d7 f8 3f a1 15 5b 00 47 71 8c bc 54 6a  .E4..?..[.Gq..Tj
  192  0d 07 2b 04 b3 56 4e ea 1b 42 22 73 f5 48 27 1a  ..+..VN..B"s.H’.
  208  0b b2 31 60 53 fa 76 99 19 55 eb d6 31 59 43 4e  ..1‘S.v..U..1YCN
  224  ce bb 4e 46 6d ae 5a 10 73 a6 72 76 27 09 7a 10  ..NFm.Z.s.rv’.z.
  240  49 e6 17 d9 1d 36 10 94 fa 68 f0 ff 77 98 71 30  I....6...h..w.q0
  256  30 5b ea ba 2e da 04 df 99 7b 71 4d 6c 6f 2c 29  0[.......{qMlo,)
  272  a6 ad 5c b4 02 2b 02 70 9b 00 00 00 00 00 00 00  ..\..+.p........
  288  0c 00 00 00 00 00 00 00 09 01 00 00 00 00 00 00  ................
```

```
Nir & Langley                 Informational                    [Page 43]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```

```
   We calculate the Poly1305 tag and find that it matches
```

```
  Calculated Tag:
```

```
  000  ee ad 9d 67 89 0c bb 22 39 23 36 fe a1 85 1f 38  ...g..."9#6....8
```

```
   Finally, we decrypt the ciphertext
```

#### `Plaintext::` 

```
  000  49 6e 74 65 72 6e 65 74 2d 44 72 61 66 74 73 20  Internet-Drafts
  016  61 72 65 20 64 72 61 66 74 20 64 6f 63 75 6d 65  are draft docume
  032  6e 74 73 20 76 61 6c 69 64 20 66 6f 72 20 61 20  nts valid for a
  048  6d 61 78 69 6d 75 6d 20 6f 66 20 73 69 78 20 6d  maximum of six m
  064  6f 6e 74 68 73 20 61 6e 64 20 6d 61 79 20 62 65  onths and may be
  080  20 75 70 64 61 74 65 64 2c 20 72 65 70 6c 61 63   updated, replac
  096  65 64 2c 20 6f 72 20 6f 62 73 6f 6c 65 74 65 64  ed, or obsoleted
  112  20 62 79 20 6f 74 68 65 72 20 64 6f 63 75 6d 65   by other docume
  128  6e 74 73 20 61 74 20 61 6e 79 20 74 69 6d 65 2e  nts at any time.
  144  20 49 74 20 69 73 20 69 6e 61 70 70 72 6f 70 72   It is inappropr
  160  69 61 74 65 20 74 6f 20 75 73 65 20 49 6e 74 65  iate to use Inte
  176  72 6e 65 74 2d 44 72 61 66 74 73 20 61 73 20 72  rnet-Drafts as r
  192  65 66 65 72 65 6e 63 65 20 6d 61 74 65 72 69 61  eference materia
  208  6c 20 6f 72 20 74 6f 20 63 69 74 65 20 74 68 65  l or to cite the
  224  6d 20 6f 74 68 65 72 20 74 68 61 6e 20 61 73 20  m other than as
  240  2f e2 80 9c 77 6f 72 6b 20 69 6e 20 70 72 6f 67  /...work in prog
  256  72 65 73 73 2e 2f e2 80 9d                       ress./...
```

```
Appendix B.  Performance Measurements of ChaCha20
```

```
   The following measurements were made by Adam Langley for a blog post
   published on February 27th, 2014.  The original blog post was
   available at the time of this writing at
```

```
   <https://www.imperialviolet.org/2014/02/27/tlssymmetriccrypto.html>.
```

|`+----------------------------+-------------+-------------------+`<br>|
|---|
|`| Chip                       | AES-128-GCM | ChaCha20-Poly1305 |`<br>`+----------------------------+-------------+-------------------+`|
|`| OMAP 4460                  |  24.1 MB/s  |     75.3 MB/s     |`<br>|
|`| Snapdragon S4 Pro          |  41.5 MB/s  |     130.9 MB/s    |`<br>|
|`| Sandy Bridge Xeon (AES-NI) |   900 MB/s  |      500 MB/s     |`<br>`+----------------------------+-------------+-------------------+`|

```
                         Table 1: Speed Comparison
```

```
Nir & Langley                 Informational                    [Page 44]
```

```
RFC 7539                   ChaCha20 & Poly1305                  May 2015
```