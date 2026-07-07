# **AEZ v5: Authenticated Encryption by Enciphering** 

#### **Phillip Rogaway** 

**Viet Tung Hoang Ted Krovetz Phillip Rogaway** Florida State University Sacramento State UC Davis tvhoang@cs.fsu.edu ted@krovetz.net rogaway@cs.ucdavis.edu 

## March 21, 2017 

The named authors are both designers and submitters. 

#### **Abstract** 

AEZ encrypts by appending to the plaintext a fixed authentication block and then enciphering the resulting string with an arbitrary-input-length blockcipher, this tweaked by the nonce and AD. The approach results in strong security and usability properties, including nonce-reuse misuse resistance, automatic exploitation of decryption-verified redundancy, and arbitrary, userselectable ciphertext expansion. AEZ is parallelizable and its computational cost is close to that of AES-CTR. Our C implementation achieves peak speeds of 0.65 cpb on an Intel Skylake processor and 1.3 cpb on Apple’s A7 ARM processor. 

**The latest version of this document, and all related materials, can always be found on the AEZ homepage:** http://www.cs.ucdavis.edu/∼rogaway/aez 

# **Contents** 

|**0**|**Introduction**|**1**|
|---|---|---|
|**1**|**Specifcation**|**3**|
||1.1<br>Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>3|
||1.2<br>Arguments and Parameters . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
||1.3<br>Targeted use cases . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
||1.4<br>AEZ Extensions<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>4|
||1.5<br>Pseudocode . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>5|
||1.6<br>Usage cap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>10|
|**2**|**Security Goals**|**10**|
|**3**|**Security Analysis**|**14**|
|**4**|**Features**|**16**|
|**5**|**Design Rationale**|**19**|
|**6**|**Intellectual Property**|**20**|
|**7**|**Consent**|**20**|
|**8**|**Changes**|**20**|
|**Re**|**ferences**|**22**|
|**A **|**Specifcation of BLAKE2b**|**25**|
|**B **|**Specifcation of AEZ deciphering algorithms**|**26**|

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

# **1 Specification** 

## **1.1 Notation** 

**Numbers and strings.** A _number_ means a nonnegative integer, N = {0 _,_ 1 _,_ 2 _,..._ }. A bit is 0 or 1 and a string is a finite sequence of bits. The length of a string _X_ is written ∣ _X_ ∣. The empty string _ε_ is the string of length zero. Concatenation of strings _A_ and _B_ is written _AB_ or _A_ ∥ _B_ . When _X_ is a string or a bit, _X_<sup>_n_</sup> means _X_ repeated _n_ times; for example 0<sup>3</sup> = 000 and (01)<sup>2</sup> = 0101. By X<sup>∗</sup> we denote the set of all strings over the alphabet X , including _ε_ . By (X<sup>∗</sup> )<sup>∗</sup> we denote the set of all vectors over X<sup>∗</sup> , including the empty vector. The bitwise-and, bitwise-or, and bitwise-xor of strings _A_ and _B_ are denoted _A_ ∧ _B_ , _A_ ∨ _B_ , and _A_ ⊕ _B_ respectively. For operations on unequal-length strings, first drop the necessary number of rightmost bits from the longer (10 ⊕ 0100 = 11). For _X_ a string, let _X_ 0<sup>∗</sup> = _X_ 0<sup>_p_</sup> with _p_ the smallest number such that 128 divides ∣ _X_ ∣+ _p_ . If ∣ _X_ ∣= _n_ and 1 ≤ _i_ ≤ _j_ ≤ _n_ then _X_ [ _i_ ] is the _i_ th bit of _X_ (indexing from the left starting at 1), msb( _X_ ) = _X_ [1], and _X_ [ _i..j_ ] = _X_ [ _i_ ]⋯ _X_ [ _j_ ]. Let [ _n_ ] _t_ be the _t_ -bit string representing _n_ mod 2<sup>_t_</sup> and let [ _n_ ] be shorthand for [ _n_ ] 8; for example [0]<sup>16</sup> = ([0] 8)<sup>16</sup> = 0<sup>128</sup> and [1]<sup>16</sup> = (00000001)<sup>16</sup> . A byte is a string of eight bits. The set of all bytes is denoted Byte. A byte string is an element of Byte<sup>∗</sup> . 

A block is 128 bits. Let **0** = 0<sup>128</sup> . If _X_ = _a_ 1 ⋯ _a_ 128 is a block ( _ai_ ∈{0 _,_ 1}) then we define _X_ ≪ 1 = _a_ 2 ⋯ _a_ 128 0. For _n_ ∈ N and _X_ ∈{0 _,_ 1}<sup>128</sup> define _n_ ⋅ _X_ by asserting that 0 ⋅ _X_ = **0** and 1 ⋅ _X_ = _X_ and 2 ⋅ _X_ = ( _X_ ≪1) ⊕[135 ⋅ msb( _X_ )] 128 and 2 _n_ ⋅ _X_ = 2 ⋅( _n_ ⋅ _X_ ) and (2 _n_ + 1) ⋅ _X_ = (2 _n_ ⋅ _X_ ) ⊕ _X_ . 

**AES4 and AES10.** We assume familiarity with AES. For _K,X_ ∈{0 _,_ 1}<sup>128</sup> we write aesenc( _X,K_ ) for a single round of AES: permute _X_ by performing SubBytes then ShiftRows then MixColumns, then do an AddRoundKey with _K_ . For **_K_** = ( _K_ 0 _,K_ 1 _,K_ 2 _,K_ 3 _,K_ 4) a list of five blocks let AES4 **_K_** ( _X_ ) = AES4( **_K_** _,X_ ) be 

### aesenc(aesenc(aesenc(aesenc( _X_ ⊕ _K_ 0 _,K_ 1) _,K_ 2) _,K_ 3) _,K_ 4) _._ 

For **_K_** = ( _K_ 0 _,K_ 1 _,...,K_ 10) a list of 11 blocks define AES10 **_K_** ( _X_ ) = AES10( **_K_** _,X_ ) like we defined AES4 but composed of ten rounds of aesenc. Note that we do _not_ omit the final-round MixColumns, as does AES itself, for either AES4 or AES10. 

**BLAKE2b.** AEZ requires a 48 byte key. If the user provides such a key, it is used directly, otherwise the provided key is transformed into 48 bytes using the cryptographic hash function 

3 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

BLAKE2b [3]. All references to BLAKE2b in this document are to the unkeyed hash function in RFC 7693 [43] identified as id-blake2b384, which produces a 48-byte digest. For the sake of completeness, the BLAKE2b function is given in Appendix A. 

## **1.2 Arguments and Parameters** 

By _parameter_ we mean “a value on which AEZ encryption depends that, independent of any particular API, would usually to be held constant throughout some long-lived context.” Under this interpretation of the word, AEZ has five arguments and one parameter. See Figure 2. In particular, we do not regard keybytes = ∣ _K_ ∣/8 as a parameter (we permit keys of any length), nor npubbytes = ∣ _N_ ∣/8 (we permit nonces to have varying lengths, even within a session). While these two values are omitted from the CAESAR-specified API, they could be specified in a different API. 

The _authenticator length_ , abytes, determines how much longer a ciphertext is than its plaintext. Arbitrary values are allowed, but values exceeding 16 are not expected to provide additional security. We do not insist that abytes be held constant throughout a session; a user is free to change it with each encryption. Still, we expect most applications to fix abytes, and choose to regard it as a parameter. We will use _τ_ = 8 ⋅ abytes if we want to measure ciphertext expansion in bits. An unusual aspect of AEZ encryption is that it permits vector-valued AD: **_A_** ∈(Byte<sup>∗</sup> )<sup>∗</sup> . To recover the usual setting (a string-valued AD) the user selects an AD **_A_** with a single component. We provide a default value for the abytes parameter: abytes = 16. The only named parameter set, denoted aez, uses this value. A conforming AEZ implementation is free to select a different default. In any context where the key length or nonce length are _required_ to be fixed, we select byte lengths for these of keybytes = 48 and npubbytes = 12. Note that a default key length of 48-bytes does not mean that the designers are targeting 384-bits of security. We are not. 

## **1.3 Targeted use cases** 

AEZ, for any choice of parameter values, primarily targets **use case 3: defense in depth.** This entails, for us: authenticity despite nonce misuse; limited privacy damage from nonce misuse; authenticity despite release of unverified plaintexts; limited privacy damage from release of unverified plaintexts. We do _not_ aim for robustness in the case that AEZ is used on huge amounts of data (more data than what the specification document permits). 

To a significant but lesser extent, AEZ also targets use case 2: high-performance applications. This entails, for us: high efficiency on machines with AES-NI capabilities; constant time execution when the message length is constant; messages sizes assumed to usually be fairly long. 

## **1.4 AEZ Extensions** 

Early versions of AEZ included a parameter extns, a string-valued _extensions directive_ . The intent was that this would, in the future, unlock capabilities traditionally seen as outside the scope of an encryption scheme’s functionality, including secret nonces (secret message numbers), plaintextlength obfuscation (via a specified padding regime), and encoding ciphertexts into a prescribed 

4 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

|**symbol**|**comments**|
|---|---|
|_M_|Plaintext. _M_ ∈Byte<sup>∗</sup>|
|_C_|Ciphertext. _C_ ∈Byte<sup>∗</sup>|
|_K_|Key. _K_ ∈Byte<sup>∗</sup>. Recommend ∣_K_∣≥128. Default is ∣_K_∣=384.|
|_N_|Nonce (aka: public sequence number). _N_ ∈Byte<sup>∗</sup>. ∣_N_∣≤128 recommended|
|**_A_**|Associated data. **_A_**∈(Byte<sup>∗</sup>)<sup>∗</sup>. String-valued AD is regarded as a one-element vector|
|abytes|Authenticator length. abytes∈N. Default is 16. abytes≤16 recommended.|

Figure 2: **Arguments and parameters to AEZ** . One might consider abytes an argument _or_ a parameter: its value is allowed to change during the uses of a key, but conventionally this would not be done. 

alphabet. These extensions are to be realized by a wrapper that keylessly transforms a plaintext, AEZ encrypts it, then keylessly transforms the result. We dropped the extns parameter when we made the AD vector-valued, as the same effect can now be achieved using that feature. A document defining AEZ extensions will be released later. 

## **1.5 Pseudocode** 

The definition of AEZ is provided in Figures 3 and 4. Let us explain some aspects of the pseudocode. 

**Encryption and decryption.** To encrypt a string _M_ we augment it with an _authenticator_ —a block of abytes zero bytes—and encipher the resulting string, tweaking this with a tweak formed from **_A_** , _N_ , and abytes. Next we encipher the augmented message. To decrypt a ciphertext _C_ we reverse the process, verifying the presence of the all-zero authenticator. 

**Enciphering.** Messages are enciphered by either of two methods. Strings of 1–31 bytes are enciphered using AEZ-tiny, while those of 32 bytes or more are enciphered using AEZ-core. 

Roughly following FFX [7, 16], AEZ-tiny uses a balanced Feistel network. The number of rounds depends on the length of the plaintext: as few as eight, or as many as 24. The round function is based on AES4. This is embodied in the pseudocode by the fact that our tweakable PRP decides to use AES4 or AES10 based on the first component of the tweak, employing the AES10 only for tweaks beginning with a −1. The Encipher-AEZ-tiny routine is illustrated at the bottom-right if Figure 5 for the setting where messages have 16 or more bytes. 

A novel feature of AEZ-tiny is the possible xoring of a bit into the ciphertext just before the algorithm’s conclusion. This is done to avoid simple random-permutation distinguishing attacks, for very short strings, based on the fact that Feistel networks only generate even permutations. A similar trick, conditionally swapping two fixed points, has been used before [37]. Our approach has the benefit that the natural implementation is constant-time. 

The heart of AEZ is AEZ-core. It melds EME [20, 21], OTR [30], and a variety of other ideas. Consider the case where we want to encipher a string _M_ = _M_ 1 _M_ 1<sup>′⋯</sup><sup>_MmM_</sup> _m_<sup>′</sup><sup>_M_x</sup><sup>_M_yhavinganeven</sup> number of blocks, all of them full. We call the first 2 _m_ blocks of _M_ the i-blocks. Refer to the top-left 

5 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

100 **algorithm** Encrypt( _K,N,_ **_A_** _,τ,M_ ) // AEZ authenticated encryption 101 _X_ ← _M_ ∥ 0<sup>_τ_</sup> ; ( _A_ 1 _,...,Aa_ ) ← **_A_** 102 **_T_** ←([ _τ_ ] 128 _,N,A_ 1 _,...,Aa_ ) 103 **if** _M_ = _ε_ **then return** AEZ-prf( _K,_ **_T_** _,τ_ ) 104 **return** Encipher( _K,_ **_T_** _,X_ ) 110 **algorithm** Decrypt( _K,N,_ **_A_** _,τ,C_ ) // AEZ authenticated decryption 111 ( _A_ 1 _,...,Aa_ ) ← **_A_** ; **_T_** ←([ _τ_ ] 128 _,N,A_ 1 _,...,Aa_ ) 112 **if** ∣ _C_ ∣< _τ_ **then return** � 113 **if** ∣ _C_ ∣= _τ_ **then if** _C_ = AEZ-prf( _K,_ **_T_** _,τ_ ) **then return** _ε_ **else return** � **fi fi** 114 _X_ ← Decipher( _K,_ **_T_** _,C_ ) 115 _M_ ∥ _Z_ ← _X_ where ∣ _Z_ ∣= _τ_ 116 **if** <u>(</u> _Z_ = 0<sup>_τ_</sup> <u>)</u> **then return** _M_ **else return** � 200 **algorithm** Encipher( _K,_ **_T_** _,X_ ) // AEZ enciphering 201 **if** ∣ _X_ ∣< 256 **then return** Encipher-AEZ-tiny( _K,_ **_T_** _,X_ ) 202 **if** ∣ _X_ ∣≥ 256 **then return** Encipher-AEZ-core( _K,_ **_T_** _,X_ ) 210 **algorithm** Encipher-AEZ-tiny( _K,_ **_T_** _,M_ ) // AEZ-tiny enciphering 211 _μ_ ←∣ _M_ ∣; _n_ ← _μ_ /2; Δ ← AEZ-hash( _K,_ **_T_** ) 212 **if** _μ_ = 8 **then** _k_ ← 24 **else if** _μ_ = 16 **then** _k_ ← 16 **else if** _μ_ < 128 **then** _k_ ← 10 **else** _k_ ← 8 **fi** 213 _L_ ← _M_ [1 _.. n_ ]; _R_ ← _M_ [ _n_ + 1 _.. μ_ ]; **if** _μ_ ≥ 128 **then** _i_ ← 6 **else** _i_ ← 7 **fi** 214 **for** _j_ ← 0 **to** _k_ − 1 **do** _R_<sup>′</sup> ← _L_ ⊕((E<sup>0</sup> _K_<sup>_,i_(Δ⊕</sup><sup>_R_10∗⊕[</sup><sup>_j_]128))[1</sup><sup>_.. n_]);</sup><sup>_L_←</sup><sup>_R_;</sup><sup>_R_←</sup><sup>_R_′</sup><sup>**od**</sup> 215 _C_ ← _R_ ∥ _L_ ; **if** _μ_ < 128 **then** _C_ ← _C_ ⊕(E<sup>0</sup> _K_<sup>_,_3(Δ⊕(</sup><sup>_C_0∗∨10∗)) ∧10∗)</sup><sup>**fi**</sup> 216 **return** _C_ 220 **algorithm** Encipher-AEZ-core( _K,_ **_T_** _,M_ ) // AEZ-core enciphering 221 Δ ← AEZ-hash( _K,_ **_T_** ) 222 _M_ 1 _M_ 1<sup>′⋯</sup><sup>_MmM_′</sup> _m_<sup>_M_uv</sup><sup>_M_x</sup><sup>_M_y←</sup><sup>_M_where∣</sup><sup>_M_1∣= ⋯= ∣</sup><sup>_M_′</sup> _m_<sup>∣= ∣</sup><sup>_M_x∣= ∣</sup><sup>_M_y∣= 128and∣</sup><sup>_M_uv∣< 256</sup> 223 _d_ ←∣ _M_ uv∣; **if** _d_ ≤ 127 **then** _M_ u ← _M_ uv; _M_ v ← _ε_ **else** _M_ u ← _M_ uv[1 _.._ 128]; _M_ v ← _M_ uv[129 _.._ ∣ _M_ uv∣] **fi** 224 **for** _i_ ← 1 **to** _m_ **do** _Wi_ ← _Mi_ ⊕ E<sup>1</sup> _K_<sup>_,i_(</sup><sup>_M_′</sup> _i_<sup>);</sup><sup>_Xi_←</sup><sup>_M_′</sup> _i_<sup>⊕E0</sup> _K_<sup>_,_0(</sup><sup>_Wi_)</sup><sup>**od**</sup> 225 **if** _d_ = 0 **then** _X_ ← _X_ 1 ⊕⋯⊕ _Xm_ ⊕ **0 else if** _d_ ≤ 127 **then** _X_ ← _X_ 1 ⊕⋯⊕ _Xm_ ⊕ E<sup>0</sup> _K_<sup>_,_4(</sup><sup>_M_u10∗)</sup> 226 **else** _X_ ← _X_ 1 ⊕⋯⊕ _Xm_ ⊕ E<sup>0</sup> _K_<sup>_,_4(</sup><sup>_M_u) ⊕E0</sup> _K_<sup>_,_5(</sup><sup>_M_v10∗)</sup><sup>**fi**</sup> 227 _S_ x ← _M_ x ⊕ Δ ⊕ _X_ ⊕ E<sup>0</sup> _K_<sup>_,_1(</sup><sup>_M_y);</sup><sup>_S_y ←</sup><sup>_M_y ⊕E−</sup> _K_<sup>1</sup><sup>_,_1</sup> ( _S_ x); _S_ ← _S_ x ⊕ _S_ y 228 **for** _i_ ←1 **to** _m_ **do** _S_<sup>′</sup> ←E<sup>2</sup> _K_<sup>_,i_(</sup><sup>_S_);</sup><sup>_Yi_←</sup><sup>_Wi_⊕</sup><sup>_S_′;</sup><sup>_Zi_←</sup><sup>_Xi_⊕</sup><sup>_S_′;</sup><sup>_C_</sup> _i_<sup>′←</sup><sup>_Yi_⊕E0</sup> _K_<sup>_,_0(</sup><sup>_Zi_);</sup><sup>_Ci_←</sup><sup>_Zi_⊕E1</sup> _K_<sup>_,i_(</sup><sup>_C_</sup> _i_<sup>′)</sup><sup>**od**</sup> 229 **if** _d_ = 0 **then** _C_ u ← _C_ v ← _ε_ ; _Y_ ← _Y_ 1 ⊕⋯⊕ _Ym_ ⊕ **0** 230 **else if** _d_ ≤ 127 **then** _C_ u ← _M_ u ⊕ E<sup>−</sup> _K_<sup>1</sup><sup>_,_4</sup> ( _S_ ); _C_ v ← _ε_ ; _Y_ ← _Y_ 1 ⊕⋯⊕ _Ym_ ⊕ E<sup>0</sup> _K_<sup>_,_4(</sup><sup>_C_u10∗)</sup> 231 **else** _C_ u ← _M_ u ⊕ E<sup>−</sup> _K_<sup>1</sup><sup>_,_4</sup> ( _S_ ); _C_ v ← _M_ v ⊕ E<sup>−</sup> _K_<sup>1</sup><sup>_,_5</sup> ( _S_ ); _Y_ ← _Y_ 1 ⊕⋯⊕ _Ym_ ⊕ E<sup>0</sup> _K_<sup>_,_4(</sup><sup>_C_u) ⊕E0</sup> _K_<sup>_,_5(</sup><sup>_C_v10∗)</sup><sup>**fi**</sup> 232 _C_ y ← _S_ x ⊕ E<sup>−</sup> _K_<sup>1</sup><sup>_,_2</sup> ( _S_ y); _C_ x ← _S_ y ⊕ Δ ⊕ _Y_ ⊕ E<sup>0</sup> _K_<sup>_,_2(</sup><sup>_C_y)</sup> 233 **return** _C_ 1 _C_ 1<sup>′⋯</sup><sup>_CmC_</sup> _m_<sup>′</sup><sup>_C_u</sup><sup>_C_v</sup><sup>_C_x</sup><sup>_C_y</sup> 

Figure 3: **AEZ authenticated-encryption: main routines.** The tweakable blockcipher E, the hash AEZ-hash, and the PRF AEZ-prf are all defined in Figure 4. Requested ciphertext expansion is _τ_ = 8⋅abytes bits. Algorithm Decipher( _K,_ **_T_** _,C_ ), not shown, returns the unique _M_ such that Encipher( _K,_ **_T_** _,M_ ) = _C_ . See the accompanying text for how this is computed. 

6 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

300 **algorithm** AEZ-hash( _K,_ **_T_** ) // AXU hash. _T_ is a vector of strings 301 ( _T_ 1 _,...,Tt_ ) ← **_T_** 302 **for** _i_ ← 1 **to** _t_ **do** 303 _ℓ_ ← max(1 _,_ ⌈∣ _Ti_ ∣/128⌉); _j_ ← _i_ + 2; _Z_ 1⋯ _Zℓ_ ← _Ti_ where ∣ _Z_ 1∣= ⋯= ∣ _Zℓ_ −1∣= 128 304 **if** ∣ _Zℓ_ ∣= 128 **then** Δ _i_ ← E<sup>_j,_</sup> _K_<sup>1(</sup><sup>_Z_1) ⊕⋯⊕E</sup><sup>_j,ℓ_</sup> _K_<sup>(</sup><sup>_Zℓ_)</sup><sup>**fi**</sup> 305 **if** ∣ _Zℓ_ ∣< 128 **then** Δ _i_ ← E<sup>_j,_</sup> _K_<sup>1(</sup><sup>_Z_1) ⊕⋯⊕E</sup><sup>_j,ℓ_</sup> _K_<sup>−1</sup> ( _Zℓ_ −1) ⊕ E<sup>_j,_</sup> _K_<sup>0(</sup><sup>_Zℓ_10∗)</sup><sup>**fi**</sup> 306 **return** Δ1 ⊕⋯⊕ Δ _t_ ⊕ **0** 310 **algorithm** AEZ-prf( _K,_ **_T_** _,τ_ ) // PRF used when _M_ = _ε_ 311 Δ ← AEZ-hash( _K,_ **_T_** ) 312 **return** (E<sup>−</sup> _K_<sup>1</sup><sup>_,_3</sup> (Δ) ∥ E<sup>−</sup> _K_<sup>1</sup><sup>_,_3</sup> (Δ⊕[1] 128) ∥ E<sup>−</sup> _K_<sup>1</sup><sup>_,_3</sup> (Δ⊕[2] 128) ∥⋯)[1 _..τ_ ] 400 **algorithm** E<sup>_j, i_</sup> _K_<sup>(</sup><sup>_X_)</sup> // Scaled-down TBC 401 _I_ ∥ _J_ ∥ _L_ ← Extract( _K_ ) where ∣ _I_ ∣= ∣ _J_ ∣= ∣ _L_ ∣= 128 402 **_K_** ←( **0** _,I,J,L,I,J,L,I,J,L,I_ ); **_k_** ←( **0** _, J, I, L,_ **0** ) 403 **if** _j_ = −1 **then** Δ ← _i_ ⋅ _L_ ; **return** AES10 **_K_** ( _X_ ⊕ Δ) **fi** 404 Δ ← _j_ ⋅ _J_ ⊕ 2<sup>⌈</sup><sup>_i_/8⌉</sup> ⋅ _I_ ⊕( _i_ mod 8) ⋅ _L_ 405 **return** AES4 **_k_** ( _X_ ⊕ Δ) 410 **algorithm** Extract( _K_ ) // Map key to subkeys 411 **if** ∣ _K_ ∣= 384 **then return** _K_ 412 **else return** BLAKE2b( _K_ ) 

Figure 4: **AEZ’s hash, PRF, TBC, key-derivation algorithms.** The last carries out key processing that an implementation would normally do at session-setup. Procedure Extract calls BLAKE2b, which returns a 48-byte digest. An alternative “scaled-up” algorithm, AEZ10, would redefine E by setting E<sup>_j,i_</sup> _K_<sup>(</sup><sup>_X_)=</sup> AES _K_ ( _X_ ⊕ _iI_ ⊕ _jJ_ ) where _I_ = AES _K_ ( **0** ) and _J_ = AES _K_ ( **1** ), now restricting keys to {0 _,_ 1}<sup>128</sup> . 

and top-right of Figure 5. Regard each rectangle with a pair of numbers as a TBC, the label being the tweak and the key _K_ left implicit. Each pair of i-blocks _MiMi_<sup>′issubjectedtoatwo-round</sup> Feistel network. This both begins the scrambling of _MiMi_<sup>′and yields a value</sup><sup>_X_=</sup><sup>_X_1 ⊕⋯⊕</sup><sup>_Xm_that</sup> is a computational almost-xor-universal hash of _M_ 1 _M_ 1<sup>′⋯</sup><sup>_MmM_</sup> _m_<sup>′.Thefinalpairofblocks</sup><sup>_M_x</sup><sup>_M_y</sup> are now processed, but where _X_ initially offsets one of them. This both begins the scrambling of _M_ x _M_ y and yields the value _S_ that is a computational almost-universal hash of all of _M_ . The TBC calls of the middle row of the i-blocks now inject an ( _i,S_ )-dependent value. Two more Feistel rounds to each i-block gives _C_ 1 _C_ 1<sup>′⋯</sup><sup>_CmC_</sup> _m_<sup>′.Tocompute</sup><sup>_C_x</sup><sup>_C_ywelikewiseemploytwomoreFeistel</sup> rounds, the _C_ x value offset by a value _Y_ = _Y_ 1 ⊕⋯⊕ _Ym_ analogous to _X_ . 

The top-middle panel shows how to deal with messages having an even number of blocks, the last of these a fragment. Now the message is partitioned into _M_ 1 _M_ 1<sup>′⋯</sup><sup>_MmM_</sup> _m_<sup>′</sup><sup>_M_u</sup><sup>_M_v</sup><sup>_M_x</sup><sup>_M_ywith all blocks</sup> full except _M_ v, which will have 1–15 bytes. The Figure 5 trapezoids used to process _M_ v denote 10<sup>∗</sup> padding (top and bottom) and truncation (middle). The value _X_ = _X_ 1 ⊕⋯⊕ _Xm_ ⊕ _X_ v ⊕ _X_ u now includes contributions from _X_ u and _X_ v, and similarly for _Y_ = _Y_ 1 ⊕⋯⊕ _Ym_ ⊕ _Y_ u ⊕ _Y_ v. 

Messages with an odd number of blocks are handled similarly, with the v-column omitted and the padding and truncation, if needed, moved to the u-column. We say “if needed” because no padding or truncation is used if the u block is full (ie, an odd number of blocks, all of them full). 

Let us call this construction just given AEZ-core[E]. It is the generalization of AEZ-core that employs an arbitrary tweakable blockcipher E. It should not be surprising that the construction is 

7 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

<!-- Start of picture text -->
M 1 M 1 ’ M m M m ’ M u M v M x M y<br>X<br>1, 1 1, m ∆ 0, 1<br>0, 0 0, 0 0, 4 Xu 0, 5 Xv<br>S X1 S Xm -1, 1<br>S S<br>2, 1 2, m -1, 4 -1, 5<br>... S<br>Y1 0, 0 Ym 0, 0 0, 4 Yu 0, 5 Yv -1, 2<br>1, 1 1, m 0, 2 ∆<br>Y<br>C1 C1’ Cm Cm’ Cu Cv Cx C y<br>L R<br>Z 1 Z ℓ-1 Z ℓ ∆ ⊕ 0<br>∆ ⊕ 1 0, 6<br>j, 1 j,  ℓ − 1 j,  ℓ 0, 6 ∆ ⊕ 2<br>... ∆i ∆ ⊕ 3 0, 6<br>0, 6<br>∆ ⊕ 4<br>∆ ⊕ 5 0, 6<br>0, 6<br>Z 1 Z ℓ-1 Z ℓ 10* ∆ ⊕ 6<br>∆ ⊕ 7 0, 6<br>j , 1 j,  ℓ − 1 j,  0 0, 6<br>... ∆i L * R *<br><!-- End of picture text -->

Figure 5: **Illustration of AEZ enciphering.** Rectangles with pairs of numbers are tweakable blockciphers, the pair being that tweak (the key, always _K_ , is not shown). **Top row:** enciphering a message _M_ of (32 or more bytes) with AEZ-core. The i-block (top left) is used for the bulk of the message, but the xy-block (top right) comprises the last 32 bytes, while the uv-block (top middle) comprises the prior 0–31 bytes. (The picture shows a uv-block of 17–31 bytes.) The string _X_ is computed via _X_ ← _X_ 1 ⊕⋯⊕ _Xm_ ⊕ _X_ u ⊕ _X_ v; if _X_ u or _X_ v is undefined then this term is omitted in computing _X_ . The string _Y_ is computed analogously. **Bottom left:** AEZ-hash computes Δ = ⊕ Δ _i_ from a vector-valued tweak encoding abytes, _N_ , and **_A_** . Its _i_ -th component _Z_ 1⋯ _Zℓ_ is hashed as shown, where _j_ = _i_ + 2 ≥ 3. **Bottom right:** AEZ-tiny, when operating on a string _M_ = _L_ ∥ _R_ of 16–31 bytes. More rounds are used if _M_ has 1–15 bytes. 

a strong-PRP under the assumption that the TBC used is secure as a tweakable-PRP. We prove this in the academic paper corresponding to this submission [22]. 

At this point we could instantiate E using a standard TBC based on AES: the XE method [28, 40] would do, yielding the scheme AEZ10 specified in the caption of Figure 4. We would then have a provably-secure enciphering scheme (for strings of 32 or more bytes) costing about five AES calls per pair of blocks, so 2.5 AES calls per block. The cost would be similar to EME [20, 21]: 0.5 more AES calls per block, but avoiding the repeated doubling and the use of AES-inverse. 

But suppose we shatter our abstraction boundary and look at all that is going on to encipher _M_ 

8 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

in AEZ10. Then the design starts to seem like major overkill: each block _Mi_ is subjected to 30 rounds of AES (ten shared with a neighboring block), plus additional AES rounds to produce the unpredictable, _M_ -dependent value _S_ that gets injected into the process while 20 rounds yet remain. 

In light of such overkill, AEZ-core selectively prunes some of the AES calls that AEZ10 would perform, using AES4 in their place. In particular, we prune invocations where we are trying to achieve computational xor-universal hashing. We leave enough AES rounds so that each block _Mi_ is effectively processed with 12 AES rounds, eight of these subsequent to injection of the highlyunpredictable _S_ and four of them shared with a neighboring block. The key steps in calculating _S_ are not pruned, nor the TBC used to mask u- and v-blocks. 

**Tweak processing.** So far we have not mentioned the processing of the tweak **_T_** built from _N_ and **_A_** . This is shown in the bottom-left of Figure 5. First we compute a hash AEZ-hash on **_T_** to create a value Δ; and then Δ is injected into AEZ-tiny and AEZ-core processing as shown. 

**Deciphering.** We define Decipher( _K,_ **_T_** _,Y_ ) as the unique _X_ such that Encipher( _K,_ **_T_** _,X_ ) = _Y_ . Logically, this is all we need say for the specification to be well-defined, so we omit writing out the implementing pseudocode in the body of this specification document. Still, we write it out in Appendix B, and explain here the needed changes in pseudocode. The reason the change is small is that enciphering and deciphering are highly symmetric for both AEZ-tiny and AEZ-core. 

AEZ-tiny deciphering is identical to AEZ-tiny enciphering except that we must count backwards instead of forwards, and we must do the only-even-cycles correction (line 215) at the beginning instead of the end. Specifically, a routine Decipher-AEZ-tiny( _K,_ **_T_** _,M_ ) (the _M_ now representing ciphertext) is identical to Encipher-AEZ-tiny( _K,_ **_T_** _,M_ ) except that line 214 is changed to count from _k_ − 1 down to 0, while for line 215 has each _C_ replaced by _M_ before moving the line up to just after line 212. 

AEZ-core deciphering is identical to AEZ-core enciphering except that we must take the xy-tweaks in reverse order. Specifically, a routine Decipher-AEZ-core( _K,_ **_T_** _,M_ ) (the _M_ now representing ciphertext) is identical to Encipher-AEZ-core( _K,_ **_T_** _,M_ ) except we swap tweaks (0 _,_ 1) and (0 _,_ 2), and we swap tweaks (−1 _,_ 1) and (−1 _,_ 2). These four tweaks appear at lines 227 and 232. 

**PRF.** Using the Carter-Wegman approach, we also build a PRF AEZ-prf: counter-mode is employed to extend the output length if abytes > 16. The PRF is only used for the special case of enciphering the empty message. This is done for efficiency reasons—to make AEZ-prf _K_ ( _X_ ) = Encrypt( _K,ε,X,τ,ε_ ) an attractive PRF. 

**Key processing.** For the users’ convenience, AEZ allows keys of any length. Using procedure Extract, the provided key is processed into 48 bytes, if it is not already of that length, using a cryptographic hash function. 

**Tweakable blockcipher.** The TBC E<sup>_j,i_</sup> _K_<sup>(</sup><sup>_X_)takesatweak(</sup><sup>_j,i_)with</sup><sup>_j_≥−1and</sup><sup>_i_≥0.The</sup> first component selects between AES10 (when _j_ = −1) and AES4 (when _j_ ≥ 0). Either way, the construction is based on XE [28, 40]. Earlier versions of E were more complex. The complexity aimed to improve speed and, later, to frustrate a birthday attack [19]. But the complexity improved speed only slightly, didn’t eliminate birthday attacks [12], and led to a bug in the v4 spec [10]. 

9 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

## **1.6 Usage cap** 

We impose a limit that AEZ be used for at most 2<sup>48</sup> bytes of data (about 280 TB); by that time, the user should rekey. For the purpose of this requirement, we say that, when encrypting ( _N,_ **_A_** _,M_ ) with a given key _K_ , AEZ is acting on ⌈∣ _N_ ∣/8⌉+⌈∣ **_A_** ∣/8⌉+⌈∣ _M_ ∣/8⌉ bytes. The above requirement stems from the existence of birthday attacks on AEZ, as well as the use of AES4 to create a universal hash function. 

# **2 Security Goals** 

**Nonce-reuse security.** AEZ achieves _nonce-reuse misuse-resistance_ (MRAE), as previously defined by Rogaway and Shrimpton [42]. In an MRAE scheme, repeating a nonce will violate privacy only insofar as repetitions of ( _N,_ **_A_** _,M_ ) triples will be identified as such. It will not compromise authenticity at all. SIV [42] is the best-known MRAE scheme. 

Some researchers call AE schemes nonce-reuse misuse-resistant more broadly, encompassing schemes that achieve much weaker notions, like those that leak the longest common block-aligned prefix (for some fixed and typically small blocksize). Such notions were invented to approximate best-possible security for online schemes, which they do rather inexactly. MRAE schemes can’t be online. 

**Exploitation of embedded novelty.** MRAE security implies automatic exploitation of randomness or sequence numbers present in messages: in any context where messages are known to be distinct (eg, a sequence number is embedded somewhere within) or are extremely unlikely to collide (eg, a freshly-generated session key is embedded somewhere within), use of a nonce unnecessary. In such settings, omission of a nonce does _not_ represent misuse; it is a sound way to encrypt. 

**Exploitation of domain-specific redundancy.** In many contexts, plaintexts have a certain expected structure. This might arise because the message was produced by or for a particular protocol. We intend that if the user checks for the anticipated structure and regards messages as inauthentic if they don’t comply, then this check augments authenticity and correspondingly lessens the need for the nominal redundancy that is inserted by AEZ before enciphering (that is, the extra abytes zero bytes). The concept of automatically exploiting redundancy present in plaintexts to achieve authenticity is well known in cryptographic folklore, where it has often been wrongly assumed, and demonstrably achieved for AE based on a strong-PRP [6]. 

**Releasing unverified plaintext.** When decrypting, an _unverified plaintext_ is a string that will be released if the ciphertext is deemed authentic, but is supposed to be quashed otherwise. While not definitionally mandated, AE schemes routinely compute such a thing. One form of encryptionscheme misuse is to release some or all of the unverified plaintext despite the ciphertext’s invalidity. This might happen because of an incremental decryption API or a more traditional side-channel. 

Contemporaneous work by Andreeva _et. al_ gives definitions to formalize an AE scheme’s security against release of unverified plaintexts [1]. Our own definitional approach is different; we formalize _robust_ AE, which incorporates the unverified-plaintext concern among its aspects. In claiming robust-AE security for AEZ the unverified plaintext is the value _X_ computed at line 114. Achieving robust AE implies that no harm would come of returning ( _X,_ �) instead of � at line 116. 

10 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

**Per-message nonce-length and parameter authentication.** No security problems result from employing nonces of varying lengths during a session, nor from changing the authenticator length abytes during a session. Of course accessing such capabilities would require an appropriate API. 

**Good security for low ciphertext expansion.** Traditionally, AE security definitions “give up” when the adversary forges. This means that, at least definitionally, it’s OK for a scheme to fail catastrophically when it first fails. A consequence is that authentication tags need to be so long that forgeries almost never occur. Yet there are applications where an occasional forgery is fine. For example, in some settings it ought to be fine to use a one-byte authenticator: while the adversary will have a 2<sup>−8</sup> chance of forging a given message, we could still expect that, say, a reasonable adversary won’t have much more than a 2<sup>−80</sup> chance to forge ten consecutive messages. 

AEZ permits short authentication tags, getting security as strong as possible given the selected authenticator length. This implies that we must use a new definition for AE, one that does _not_ give up when a forgery occurs. It is described next. 

**Robust AE.** Our new security definition for AE formalizes that one is doing _as good a job as possible for a given value τ of ciphertext expansion_ ( _τ_ = 8 ⋅ abytes). The statement is required to hold even in the face of decryption leaking some specified information. An academic paper corresponding to this submission [22] defines and investigates this notion of _robust AE_ (RAE). Here we sketch the idea. 

We restrict attention to AE schemes Π = (K _,_ E _,_ D) that operate on strings of any length and that are _τ_ - _expanding_ , ∣E _K_<sup>_N,_</sup><sup>**_A_**</sup> ( _M_ )∣= ∣ _M_ ∣+ _τ_ , for a user-selectable _τ_ ∈[0 _..τ_ max]. We first consider an adversary that has access to one of two pairs of oracles. In the _real_ setting the _encryption oracle_ encrypts according to E and the _decryption oracle_ decrypts according to D. In the _ideal_ setting the encryption oracle, asked ( _N,_ **_A_** _,τ,M_ ), returns _πN,_ **_A_** _,τ_ ( _M_ ) where, for each _N,_ **_A_** _,τ_ , the function _πN,_ **_A_** _,τ_ is a uniformly selected random injection from _μ_ -bit strings to ( _μ_ + _τ_ )-bit ones. All of these functions are chosen independently. The decryption oracle, given ( _N,_ **_A_** _,τ,C_ ), checks if there’s an _M_ such that _πN,_ **_A_** _,τ_ ( _M_ ) = _C_ . If so, it returns _M_ . Otherwise it returns the distinguished value �. 

The above notion coincides with that of a _pseudorandom injection_ (PRI) that has been updated to regard _τ_ as in input. To arrive at the more general notion of an RAE scheme, we modify how decryption works in the ideal setting. This is unchanged when ( _N,_ **_A_** _,τ,C_ ) is valid (that is, when there is an _M_ such that _πN,_ **_A_** _,τ_ ( _M_ ) = _C_ ), but when it’s not, a simulator _S_ gets to return what it wants. The return value may be based only on _N,_ **_A_** _,C,τ_ and any saved state of _S_ . The real decryption algorithm D can now be augmented to capture any desired leakage when the ciphertext is invalid: have algorithm D return what it wants, as long as it is recognizably invalid (eg, we can require that the length of the unverified plaintext not be ∣ _C_ ∣− _τ_ bits). The notion is stronger than before insofar as not only must the scheme approximate a PRI with respect to valid ciphertexts, but, when they’re invalid, the simulator must still be able to approximate that which D returns. 

While the simulator _S_ and invalid-message-returning D strengthen the RAE notion relative to the PRI notion, the key aspect, we think, is simply our insistence that encryption looks like a PRI even in the case that the ciphertext expansion is zero or small. In fact, when the ciphertext expansion is large, the PRI notion and the MRAE notion effectively coincide [42]. On the other hand, when ciphertext expansion is zero, the RAE (and PRI) notion coincides with that of a strong-PRP. RAE security can be thought of as a way to bridge strong-PRP security and MRAE security, coinciding 

11 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

|**Security goal**|**Query complexity**|**Time complexity**|**Approx formula**|
|---|---|---|---|
|Confdentiality of plaintext|55|128|_s_<sup>2</sup>/2<sup>110 </sup>+_t_/2<sup>128</sup>|
|Authenticity of plaintext|55|128|_s_<sup>2</sup>/2<sup>110 </sup>+_t_/2<sup>128</sup>|
|Authenticity of AD|55|128|_s_<sup>2</sup>/2<sup>110 </sup>+_t_/2<sup>128</sup>|
|Authenticity of the nonce|55|128|_s_<sup>2</sup>/2<sup>110 </sup>+_t_/2<sup>128</sup>|
|Robust AE|55|128|_s_<sup>2</sup>/2<sup>110 </sup>+_t_/2<sup>128</sup>|

Figure 6: **Security goals for AEZ with default parameters (** aez **).** Query complexity is log base-2 of blocks queried: one needs about 2<sup>55</sup> blocks before having a good chance to violate the goal. Time complexity is log base-2 of cycles: one needs about 2<sup>128</sup> time to break the goal if one has only small amount of plaintext/ciphertext. The formula bounds adversarial advantage as a function of queried blocks ( _s_ ) and time ( _t_ ) by a known, modest-size adversary. The final row, RAE security, not only implies the other rows but also nonce-reuse misuse-resistance: AEZ provides maximum-possible robustness against nonce reuse. 

### with the former when _τ_ is zero and the latter when _τ_ is large. 

**Provable security.** AEZ has been developed using the tools of provable security. The paradigm used is what we call _prove-then-prune_ . First, a scheme is designed and proven secure when its underlying cryptographic tool—a tweakable blockcipher (TBC), in the case of AEZ—meets some well-established security definition. At that point one could instantiate the primitive with a conventional tool—eg, using AES and the XE construction [28, 40], as we described for AEZ10. One would then have a scheme with a customary provable-security claim. Instead, to make our scheme faster, we choose to selectively instantiate _some_ of the TBC calls with a construction based on AES4, a four-round version of AES. Insofar as AES4 is _not_ secure as a PRP (and, additionally, our method of tweaking it is not always XE), this step is effectively heuristic. 

We call the instantiation of a scheme using a mixture of full and downgraded primitives the _scaleddown_ design. In contrast, using a conventional construction for the primitive would yield the usual, _scaled-up_ design. AEZ is a scaled-down realization of AEZ. It is a _thesis_ underlying our design methodology that the approach is useful both to discover good schemes and to have some measure of assurance for them. 

**Quantitative security statements.** For the scaled-up version of AEZ with default parameters, we expect that an adversary cannot be exhibited that violates RAE security with advantage exceeding 4 _s_<sup>2</sup> /2<sup>128</sup> + _t_ /2<sup>128</sup> where _s_ is the total number of 16-byte blocks of messages encrypted or authenticated (plus 3 blocks per message, by convention) and _t_ is the time (including the description size) in which the adversary runs. The second addend is a stand-in for an advantage term associated to breaking the PRP security for the underlying blockcipher. Constants 3 and 4 are the result of ongoing analysis. The number of encryption and decryption queries does not appear in the formula above because we have folded them into _s_ . 

For aez itself, the formula should be replaced by 4 _s_<sup>2</sup> /2<sup>113</sup> + _t_ /2<sup>128</sup> because of the higher maximal expected differential probability of AES4 [25] compared to an ideal hash or cipher. 

Many authors prefer to think of security in terms of number-of-bits. We would summarize the 4 _s_<sup>2</sup> /2<sup>113</sup> < _s_<sup>2</sup> /2<sup>110</sup> term of the last formula by saying that aez is expected to have 55 bits of 

12 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

security. We warn that when an author makes a claim like “GCM has 128 bits of security” the focus is _time_ complexity, imagining a fixed and small amount of ciphertext. When saying that we have at least 55 bits of security we are speaking exclusively of query complexity: that an adversary must gather roughly 2<sup>55</sup> blocks (2<sup>59</sup> bytes) worth of ciphertext before it has a good chance to break RAE security (assuming an explicitly given attack of reasonable description size and time complexity). Recall our usage cap, that AEZ should be used for at most 2<sup>48</sup> bytes. One might summarize targeted security goals for aez as shown in Figure 6. 

**Non-goals.** We have not tried to achieve security beyond the birthday bound; like traditional modes of operation based on a 128-bit blockcipher, there _are_ easy distinguishing and forging attacks by the time the adversary queries AEZ with about 2<sup>64</sup> blocks of message, AD, or nonce. There are even key-recovery birthday attacks, as already shown by Fuhr, Leurent, and Suder [19] and Chaigneau and Gilbert [12]. Similarly, we are not targeting time-complexity security in excess of what is inherent in employing a 128-bit key. (That said, we avoid the obvious 2<sup>128</sup> -time brute-force attack for keys in excess of 128 bits by processing arbitrary-length keys to 48-byte subkey material in our key extraction processing.) We did not target related-key-attack security, although our use of a cryptographic hash function for keys not of 48 bytes suggests that we will achieve that end for strings of all other lengths. 

**Warnings.** Robust AE should not be understood as blanket permission to omit a nonce or allocate too few bits for ciphertext expansion. Let us elaborate. 

In the context of AE, misuse resistance (MR) has, of late, been brandished far too liberally, with some authors going so far as to call their _online_ AE schemes _misuse resistant_ , or even _nonce free_ . We disapprove. Online AE schemes can never be misuse-resistant in the sense originally defined [42], and, what is worse, it is unclear that they imply _any_ useful guarantee when nonces repeat. The definitions here [18] are deceptive, sounding stronger than they are [23]. 

We worry that the expansion of the term “misuse resistance” to online schemes may wrongly signal that there are online AE schemes where nonces are effectively optional. We wish to emphasize that, even with RAE, nonces _still_ should not be construed as optional in the absence of supporting analysis. Specifically, a nonce must be used unless one has certitude that, even in the presence of the adversary, all encrypted ( **_A_** _i,Mi_ ) pairs will be distinct; or else one has some other domain-specific reason to believe that, for the given context, leaking plaintext-equality is not problematic. 

In a similar vein, AEZ allows little or no ciphertext expansion. But the adversary’s per-message forging probability increases with decreasing redundancy. Applications should not reduce abytes to zero or some other small value without ensuring that, combining the abytes zero bytes with any decryption-verified redundancy, there remain enough total bits _r_ of redundancy that forging each message with probability 2<sup>−</sup><sup>_r_</sup> is alright. 

The robust AE notion does not guarantee security against _arbitrary_ leakage. For AEZ, one can release the entire string _X_ ← Decipher( _K,_ **_T_** _,C_ ) at line 114, but we have not indicated that anything beyond that may be released. In particular, Barwell, Page, and Stam [4, Appendix E] point out that if one is following the early-abort strategy to reject invalid ciphertext then it is crucial that one not release the partially decrypted ciphertext: with early-abort processing, all that may be released is, as usual, the indication of invalidity. 

13 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

# **8 Changes** 

**AEZ v1** (2014.03.15): Initial definition. Submitted to the CAESAR competition. **AEZ v1.1** (2014.04.29): A minor revision to correct various v1 typos. 

**AEZ v2** (2014.08.17): A major revision. The enciphering algorithm MEM was replaced by EME4. While no problems were ever found with MEM, the move facilitates two major gains: (a) the cost is reduced from from 1.8 times that of AES to 1.0 times that of AES, while (b) all use of the AES-inverse operation is removed from AEZ. Also, EME4 is simpler, and the entire spec was correspondingly simplified. 

**AEZ v3** (2014.09.22): A modest revision. To simplify implementations the ( _M_ x _,M_ y) pair of blocks is now taken from the end of the string being enciphered/deciphered instead of the beginning. Round keys were simplified. To minimize latency and facilitate 

20 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

fast rejection of invalid ciphertexts, both _X_ and Δ are added to _M_ x. Support is added for vector valued-AD, which entailed enriching AEZ-hash and removing Format(), extns, and the upper limit on abytes. Functions (FF0, EME4, AHash, AMac) were renamed to (AEZ-tiny, AEZ-core, AEZ-hash, AEZ-prf). 

**AEZ v4** (2015.08.29): A minor revision. The Extract() procedure was rewritten to be conceptually simpler and ensure that knowledge of some subkeys ( _I_ , _J_ , or _L_ ) won’t imply knowledge of others. The default key length was changed to 48 bytes. The XEX construction, 

instead of XE, is now used in AEZ-hash, changing the definition of E. It was hoped that this would help frustrate a key-recovery birthday attack described by Fuhr, Leurent, and 

Suder [19], but it was later shown by Chaigneau and Gilbert that such birthday attacks remain [12]. Offset conventions in E were further modified for aesthetic reasons. **AEZ v4.1** (2015.10.14): Housecleaning: fixed two typos in the pseudocode (lines 403, 408) and some minor textual edits. Update of performance claims to reflect newer CPUs. **AEZ v4.2** Some notational tweaks in response to comments. 

**AEZ v5** (2017.03.20): Simplified the definition of the tweakable blockcipher E to correct a serious bug pointed out by Bonnetain, Derbez, Duval, Jean, Leurent, Minaud, and Suder [10]: 

an error in our v4 definition of offsets for E resulted in the same offset being used for two 

different tweaks, destroying security. We took this opportunity to more broadly simplify E. Its overly complex definition no longer seemed rational, as fresh timing studies revealed that our convoluted definition of E was only marginally faster than the most straightforward one, 

- while key-recovery birthday attacks had not been thwarted by prior changes to E. 

# **A Specification of BLAKE2b** 

For completeness, we give the full description of BLAKE2b, closely following the BLAKE2b documentation [3, 43]. For each byte string _X_ , let ∥ _X_ ∥ denote the byte length of _X_ . For each string _X_ with ∥ _X_ ∥≤ 128, let pad( _X_ ) denote the string _Y_ with ∥ _Y_ ∥= 128 obtained by appending zero or more 0-bits to _X_ . Let _X_ ⋙ _ℓ_ denote the right circular shift by _ℓ_ bits on the string _X_ . For any 64-bit strings _X_ and _Y_ , let _X_ + _Y_ denote the string obtained by regarding _X_ and _Y_ as integers, adding them modulo 2<sup>64</sup> , then regarding the resulting integers as a string. BLAKE2b uses little-endian convention in parsing between integers and strings. 

The specification of the BLAKE2b hash is given in Figure 9, where the compression function Compress is as follows. It takes as input a 64-byte string _h_ , a 128-byte message _M_ , and an integer 0 ≤ _t_ < 2<sup>128</sup> . Let _f_ 0 = 0<sup>64</sup> if _t_ is a multiple of 128, and let _f_ 0 = 1<sup>64</sup> otherwise. Let _f_ 1 = 0<sup>64</sup> . Parse _t_ as _t_ 0 _t_ 1, where ∣ _t_ 0∣= ∣ _t_ 1∣= 64. Recall that BLAKE2b uses little-endian convention, so _t_ 0 contains the least significant bits of _t_ . Parse _h_ as _h_ 0⋯ _h_ 7, and _M_ as _M_ 0⋯ _M_ 15, where ∣ _h_ 0∣= ⋯= ∣ _h_ 7∣= ∣ _M_ 0∣= ⋯= ∣ _M_ 15∣= 64. Initialize ( _v_ 0 _,...,v_ 15) ←( _h_ 0 _,...,h_ 7 _,_ IV0 _,_ IV1 _,_ IV2 _,_ IV3 _,t_ 0 ⊕ IV4 _,t_ 1 ⊕ IV5 _,f_ 0 ⊕ IV6 _,f_ 1 ⊕ IV7), where the constants IV0 _,...,_ IV7 are defined in Table 2. One then processes the state ( _v_ 0 _,...,v_ 15) in 12 

25 

_AEZ v5_ 

_Hoang, Krovetz, and Rogaway_ 

600 **algorithm** Decipher( _K,_ **_T_** _,C_ ) // AEZ deciphering 601 **if** ∣ _C_ ∣< 256 **then return** Decipher-AEZ-tiny( _K,_ **_T_** _,C_ ) 602 **if** ∣ _C_ ∣≥ 256 **then return** Decipher-AEZ-core( _K,_ **_T_** _,C_ ) 610 **algorithm** Decipher-AEZ-tiny( _K,_ **_T_** _,C_ ) // AEZ-tiny deciphering 611 _μ_ ←∣ _C_ ∣; _n_ ← _μ_ /2; Δ ← AEZ-hash( _K,_ **_T_** ) 612 **if** _μ_ < 128 **then** _C_ ← _C_ ⊕(E<sup>0</sup> _K_<sup>_,_3(Δ⊕(</sup><sup>_C_0∗∨10∗)) ∧10∗)</sup><sup>**fi**</sup> 613 **if** _μ_ = 8 **then** _k_ ← 24 **else if** _μ_ = 16 **then** _k_ ← 16 **else if** _μ_ < 128 **then** _k_ ← 10 **else** _k_ ← 8 **fi** 614 _L_ ← _C_ [1 _.. n_ ]; _R_ ← _C_ [ _n_ + 1 _.. μ_ ]; **if** _μ_ ≥ 128 **then** _i_ ← 6 **else** _i_ ← 7 **fi** 615 **for** _j_ ← _k_ − 1 **downto** 0 **do** _R_<sup>′</sup> ← _L_ ⊕((E<sup>0</sup> _K_<sup>_,i_(Δ⊕</sup><sup>_R_10∗⊕[</sup><sup>_j_]128))[1</sup><sup>_.. n_]);</sup><sup>_L_←</sup><sup>_R_;</sup><sup>_R_←</sup><sup>_R_′</sup><sup>**od**</sup> 616 _M_ ← _R_ ∥ _L_ ; **return** _M_ 620 **algorithm** Decipher-AEZ-core( _K,_ **_T_** _,C_ ) // AEZ-core deciphering 621 Δ ← AEZ-hash( _K,_ **_T_** ) 622 _C_ 1 _C_ 1<sup>′⋯</sup><sup>_CmC_</sup> _m_<sup>′</sup><sup>_C_uv</sup><sup>_C_x</sup><sup>_C_y←</sup><sup>_C_where∣</sup><sup>_C_1∣= ⋯= ∣</sup><sup>_C_</sup> _m_<sup>′∣= ∣</sup><sup>_C_x∣= ∣</sup><sup>_C_y∣= 128and∣</sup><sup>_C_uv∣< 256</sup> 623 _d_ ←∣ _C_ uv∣; **if** _d_ ≤ 127 **then** _C_ u ← _C_ uv; _C_ v ← _ε_ **else** _C_ u ← _C_ uv[1 _.._ 128]; _C_ v ← _C_ uv[129 _.._ ∣ _C_ uv∣] **fi** 624 **for** _i_ ← 1 **to** _m_ **do** _Wi_ ← _Ci_ ⊕ E<sup>1</sup> _K_<sup>_,i_(</sup><sup>_C_</sup> _i_<sup>′);</sup><sup>_Yi_←</sup><sup>_C_</sup> _i_<sup>′⊕E0</sup> _K_<sup>_,_0(</sup><sup>_Wi_)</sup><sup>**od**</sup> 625 **if** _d_ = 0 **then** _Y_ ← _Y_ 1 ⊕⋯⊕ _Ym_ ⊕ **0 else if** _d_ ≤ 127 **then** _Y_ ← _Y_ 1 ⊕⋯⊕ _Ym_ ⊕ E<sup>0</sup> _K_<sup>_,_4(</sup><sup>_C_u10∗)</sup> 626 **else** _Y_ ← _Y_ 1 ⊕⋯⊕ _Ym_ ⊕ E<sup>0</sup> _K_<sup>_,_4(</sup><sup>_C_u) ⊕E0</sup> _K_<sup>_,_5(</sup><sup>_C_v10∗)</sup><sup>**fi**</sup> 627 _S_ x ← _C_ x ⊕ Δ ⊕ _Y_ ⊕ E<sup>0</sup> _K_<sup>_,_2(</sup><sup>_C_y);</sup><sup>_S_y ←</sup><sup>_C_y ⊕E−</sup> _K_<sup>1</sup><sup>_,_2</sup> ( _S_ x); _S_ ← _S_ x ⊕ _S_ y 628 **for** _i_ ←1 **to** _m_ **do** _S_<sup>′</sup> ←E<sup>2</sup> _K_<sup>_,i_(</sup><sup>_S_);</sup><sup>_Xi_←</sup><sup>_Wi_⊕</sup><sup>_S_′;</sup><sup>_Zi_←</sup><sup>_Yi_⊕</sup><sup>_S_′;</sup><sup>_M_′</sup> _i_<sup>←</sup><sup>_Xi_⊕E0</sup> _K_<sup>_,_0(</sup><sup>_Zi_);</sup><sup>_Mi_←</sup><sup>_Zi_⊕E1</sup> _K_<sup>_,i_(</sup><sup>_M_′</sup> _i_<sup>)</sup><sup>**od**</sup> 629 **if** _d_ = 0 **then** _M_ u ← _M_ v ← _ε_ ; _X_ ← _X_ 1 ⊕⋯⊕ _Xm_ ⊕ **0** 630 **else if** _d_ ≤ 127 **then** _M_ u ← _C_ u ⊕ E<sup>−</sup> _K_<sup>1</sup><sup>_,_4</sup> ( _S_ ); _M_ v ← _ε_ ; _X_ ← _X_ 1 ⊕⋯⊕ _Xm_ ⊕ E<sup>0</sup> _K_<sup>_,_4(</sup><sup>_M_u10∗)</sup> 631 **else** _M_ u ← _C_ u ⊕ E<sup>−</sup> _K_<sup>1</sup><sup>_,_4</sup> ( _S_ ); _M_ v ← _C_ v ⊕ E<sup>−</sup> _K_<sup>1</sup><sup>_,_5</sup> ( _S_ ); _X_ ← _X_ 1 ⊕⋯⊕ _Xm_ ⊕ E<sup>0</sup> _K_<sup>_,_4(</sup><sup>_M_u) ⊕E0</sup> _K_<sup>_,_5(</sup><sup>_M_v10∗)</sup><sup>**fi**</sup> 632 _M_ y ← _S_ x ⊕ E<sup>−</sup> _K_<sup>1</sup><sup>_,_1</sup> ( _S_ y); _M_ x ← _S_ y ⊕ Δ ⊕ _X_ ⊕ E<sup>0</sup> _K_<sup>_,_1(</sup><sup>_M_y)</sup> 633 **return** _M_ 1 _M_ 1<sup>′⋯</sup><sup>_MmM_′</sup> _m_<sup>_M_u</sup><sup>_M_v</sup><sup>_M_x</sup><sup>_M_y</sup> 

Figure 10: **AEZ deciphering routines.** 

rounds. In each round, we run the following sequence of operations: 

In round _r_ , the operation _Gi_ ( _a,b,c,d_ ), with _i_ ∈{0 _,_ 1 _,...,_ 7}, modifies the 64-bit variables _a,b,c,d_ as follows: 

where the permutations _σ_ 0 _,...,σ_ 9 on {0 _,_ 1 _,...,_ 15} are specified in Table 1. At the end of the 12th round, output ( _h_ 0 ⊕ _v_ 0 ⊕ _v_ 8) ∥( _h_ 1 ⊕ _v_ 1 ⊕ _v_ 9) ∥⋯∥( _h_ 7 ⊕ _v_ 7 ⊕ _v_ 15). 

# **B Specification of AEZ deciphering algorithms** 

For completeness, in Figure 10 we give the code for the deciphering routines of AEZ. 

26