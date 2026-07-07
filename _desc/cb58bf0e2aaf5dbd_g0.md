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