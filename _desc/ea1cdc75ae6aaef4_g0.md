#### A: _x_ ⊞ _y_ Addition modulo word size: _x_ + _y_ mod 2<sup>32</sup> . R: _x ⊕ y_ Bitwise exclusive-or operation between _x_ 

Bitwise exclusive-or operation between _x_ and _y_ . 

X: _x_ ≪ _r_ Cyclic left rotation by _r_ bits in a 32-bit word. We also use Boolean operators _∧_ and _∨_ to denote bitwise “and” and “or” operations and double vertical _∥_ to denote concatenation of arrays and strings. Expression enclosed in single verticals _|v|_ refers to its size (length) in bits; we have _|t∥u|_ = _|t|_ + _|u|_ . A C-style notation is used for bit and byte arrays (unit size depends on context); vectors are zero-indexed with index in square brackets. We use ranges to indicate subarrays; _v_ [ _i · · · j_ ] refers to concatenation of all entries from _v_ [ _i_ ] to _v_ [ _j_ ], inclusive. All numerical values are stored and exchanged in little-endian fashion, with the least significant bit, byte, or vector array entry having index 0. Hexadecimal numbers (bytes or words) are prefixed with “0x”. Bit and byte arrays are read from left to right, with index starting with 0. The 32-bit integer 0x12345678 (decimal 305419896) is therefore stored and transmitted as four bytes 0x78 _∥_ 0x56 _∥_ 0x34 _∥_ 0x12. 

Any integer _n ∈_ (0 _,_ 2<sup>_m_</sup> ] has unique encoding as bit array B[ _m_ ] with _n_ =<sup>∑</sup><sup>_m_</sup> _i_<sup>_−_1</sup> 2<sup>_i_</sup> B[ _i_ ]. Therefore bit _i_ has numerical value 2<sup>_i_</sup> . The first bit (bit 0) of a byte is therefore 2<sup>0</sup> = 0x01 and the last bit (bit 7) is 2<sup>7</sup> = 0x80. One can always fetch bit _i_ from a byte array v[] in C with an expression such as (v[i >> 3] >> (i & 7)) & 1. 

Markku-Juhani O. Saarinen 

3 

~~<u><mark>�</mark></u>~~ <u>�</u> <mark>// cyclic rotate left for 32-bit words #define ROL32(x, y) (((x) << (y)) | ((x) >> (32 - (y)))) void sneik_f512( void *s, uint8_t dom , uint8_t rounds) { const uint8_t rc [16] = { // round constant table 0xEF , 0xE0 , 0xD9 , 0xD6 , 0xBA , 0xB5 , 0x8C , 0x83 , 0x10 , 0x1F , 0x26 , 0x29 , 0x45 , 0x4A , 0x73 , 0x7C // (only 8 used now) }; int i, j; // loop counters uint32_t t, *v = ( uint32_t *) s; // assume little endian! for (i = 0; i < rounds; i++) { // loop over rounds v[0] ^= ( uint32_t ) rc[i]; // xor round constant v[1] ^= ( uint32_t ) dom; // xor domain constant for (j = 0; j < 16; j++) { t = v[j]; // middle value t += v[(j - 1) & 0xF]; // feedback previous t = t ^ ROL32(t, 24) ^ ROL32(t, 25); // p(x) = x^25 + x^24 + x t ^= v[(j - 2) & 0xF]; // outer feedback t += v[(j + 2) & 0xF]; t = t ^ ROL32(t, 9) ^ ROL32(t, 17); // q(x) = x^17 + x^9 + x t ^= v[(j + 1) & 0xF]; // reverse feedback v[j] = t; // store the result } } }</mark> ~~� �~~ 

Listing 1: The SNEIK permutation f512<sup>_ρ_</sup> _δ_<sup>(S)inC.Wesetdom =</sup><sup>_δ_androunds =</sup><sup>_ρ_.</sup> 

## **2 The SNEIK** **_f_ 512 Permutation** 

With _πδ_<sup>_ρ_wedenoteafamilyofunkeyed</sup><sup>_ρ_-roundpermutationson</sup><sup>_b_-bitstateS,controlled</sup> by a domain identifier _δ_ : 

The security of _πδ_<sup>_ρ_shouldbeevaluatedinthecontextwhereitisused–wearenot</sup> claiming it to be a hermetic sponge resistant to all structural distinguishers [BDPA11]. 

The permutation is easily invertible but the inverse permutation is not required by any of the modes proposed in this document. 

**Parameters.** SNEIK is very flexible, but for the purposes of this specification we fix the state size to _b_ = 512 bits, which is organized as sixteen 32-bit words ( _n_ = 16). 

We note that the state required by any of the proposed AEAD and hashing modes is limited to essentially the 512-bit S – not much more than 64 bytes of RAM is required to perform any operation from start to finish. 

**Implementation strategies.** Listing 1 contains a compact C source code implementation of the SNEIK permutation instantiation _π_ = f512 (for _b_ = 512) as used in our SNEIKEN, SNEIKHA, and SNEIGEN proposals. This is not an optimized implementation but presented here as an additional reference. 

We note that the domain separator _δ_ or dom is an 8-bit integer, defined in the context of BLNK2 modes (See Table 2). Round constants are defined for up to 16 rounds, even though this version never uses more than 8. Our current round counts are quite optimistic, so we reserve the right to increase them if deemed necessary due to future cryptanalysis. 

There are two basic implementation methods, one organized as a non-linear feedback shift register (suitable for hardware) and a “register window” method suitable for lightweight software implementations. 

SNEIKEN and SNEIKHA 

4 

<!-- Start of picture text -->
s[ i ] s[ i − 1] s[ i − 2] · · · s[ i − 14] s[ i − 15] s[ i − 16]<br>⊕ d[ i ]<br>⊞<br>≪ 24 ≪ 25<br>⊕<br>⊕<br>⊞<br>≪ 9 ≪ 17<br>⊕<br>⊕<br><!-- End of picture text -->

**Figure 1:** The SNEIK permutation, viewed as a non-linear feedback shift register (NLFSR), Equation 2. This illustrates its structural similarity to some stream ciphers. In a simple _nr_ -cycle hardware implementation the sixteen registers are moved right for each clock, while a new value computed and loaded into the leftmost 32-bit register. 

**Non-linear feedback shift register.** Let _n ≥_ 5 be the size of the initial state s[0 _· · · n −_ 1] of 32-bit words (with the f512 instantiation we have _n_ = 16). Recurrence of Equation 2 defines a nonlinear feedback expander sequence s[ _i_ ] for any _i ≥ n_ . The seven arithmetic steps _tj_ are numbered just for referencing. Figure 1 illustrates the operation of the NLFSR. 

To compute _r_ rounds of the SNEIK permutation, we initialize the state s[0 _· · · n −_ 1] with input, run the expander sequence for _nr_ steps and return s[ _nr · · · n_ ( _r_ + 1) _−_ 1]. 

The domain separation constant d[ _i_ ] is nonzero only when _i_ mod _n ∈{_ 0 _,_ 1 _}_ . We interpret round constants to be just another kind of “domain separator”, separating rounds from each other. We set d[ _nj_ ] = rc[ _j_ ] from vector in Equation 3 and d[ _nj_ + 1] = _δ_ . 

The domain identifier value of _δ_ is set by higher level BLNK2 primitive (see Table 2 in Section 3). The first 16 round constants are: 

Markku-Juhani O. Saarinen 

5 

<!-- Start of picture text -->
s[0] s[1] s[2] s[3] s[4] s[5] s[6] s[7] s[8] s[9] s[10] s[11] s[12] s[13] s[14] s[15]<br>R0 R1 load save R2 R3<br>R0 R1 R2 load save R3<br>R0 R1 R2 R3 load save<br>save R1 R2 R3 R0 load<br>save R2 R3 R0 R1 load<br>save R3 R0 R1 R2 load<br>save R0 R1 R2 R3 load<br><!-- End of picture text -->

**Figure 2:** The sliding window implementation technique. Since five consecutive words (with wrap-around) from the state are used to compute a new value for the “middle word” (Equation 4), we can organize the computation in a way that there is only a single load and save per step. A set of four registers can be used in a way that avoids shifting values from one register to another. We can therefore efficiently unroll by 4, 8, or 16 steps. 

**Sliding register window.** Since there are no references beyond s[ _i − n_ ] back in the sequence, the recurrence of Equation 2 may be implemented with a static _n_ -word table – as was done in Listing 1. We may use “mod _n_ ” addressing and write s[ _i − n ± j_ ] as s[ _i ± j_ ] while _i_ repeatedly scans the values _i_ = 0 _,_ 1 _, · · · , n −_ 1 for each round. 

We see that the operation uses a “window” of five inputs to evaluate each new value: 

Four 32-bit state words can be used to store the _f_ inputs as the window moves; the value s[ _i −_ 2] is used at step _t_ 4 before a replacement value s[ _i_ + 2] is loaded for step _t_ 5. This is illustrated in Figure 2. 

The standard implementation method is therefore to unroll computation of at least four iterations of Equation 2. Table 1 gives some implementation metrics for the permutation on popular microcontrollers using this method. These ARMv7-m and AVR implementations are available with the C reference code at https://github.com/pqshield/sneik. 

**Table 1:** SNEIK permutation performance on 32-bit ARM Cortex-M4 (NXP/Freescale MK20DX256 @ 24 MHz) and 8-bit AVR (Atmel ATMEGA2560 @ 16 MHz) architectures. The “RAM” size is the input/output state + stack usage while “ROM” indicates the required Flash memory. Cycles per round were measured with _ρ_ = 8. 

|**MCU**|**Unroll**|**Name**|**RAM**|**ROM**|**Cycles/Round**|
|---|---|---|---|---|---|
|AVR|16-step|“fast”|64 + 14|1974|1078.1|
|AVR|4-step|“small”|64 + 19|618|1126.0|
|Cortex M4|16-step|“fast”|64 + 16|560|188.0|
|Cortex M4|4-step|“small”|64 + 28|232|211.8|

SNEIKEN and SNEIKHA 

6 

## **3 BLNK2 Primitive Sponge Operations** 

Our proposals are built using “BLINKER-style” [Saa14a] primitives. This new version is called BLNK2 (version number is optional). In addition to authenticated encryption and hashing, these primitives can be used to build more complex yet lightweight protocols where two (or more) parties have synchronized, continuously authenticated states. 

For these modes a tuple (S _, i_ ) defines the entire state: S _∈{_ 0 _,_ 1 _}_<sup>_b_</sup> is the permutation input/output block and _i ∈_ [0 _, b_ ) is a “next bit”read/write index to it, pointing at bit S[ _i_ ]. 

As is usual in permutation-based cryptography, the block size _b_ = 512 is split into two halves, “rate” of _r_ bits and “capacity” of _c_ bits; _r_ + _c_ = _b_ . We have S = S _r ∥_ S _c_ where S _r ∈{_ 0 _,_ 1 _}_<sup>_r_</sup> and S _c ∈{_ 0 _,_ 1 _}_<sup>_c_</sup> . The security of the construction is largely determined by capacity while the rate is almost directly proportional to its processing speed. 

These primitives may set additional flags on domain parameter _δ_ before passing them to the cryptographic permutation _πδ_<sup>_ρ_.This8-bitdomainidentifierisconstructedfrom</sup> fields given in Table 2. The primitive operations are: 

S _._ clr() Clear the state: S _←_ 0<sup>_b_</sup> , _i ←_ 0. S _._ fin( _δ_ ) Mark the end of given domain input (Algorithm 2). S _._ ratchet() Clear the “rate” part for forward security: S _←_ 0<sup>_r_</sup> _∥_ S _c_ , _i ←_ 0. S _._ put(D _, δ_ ) Absorb input data _D_ (Algorithm 3). D _←_ S _._ get( _n, δ_ ) Squeeze out _n_ bits into _D_ (Algorithm 4). C _←_ S _._ enc(P _, δ_ ) Encrypt plaintext P into ciphertext C (Algorithm 5). P _←_ S _._ dec(C _, δ,_ ) Decrypt ciphertext C into plaintext P (Algorithm 6). 

Additionally, we have a utility function S _._ inc( _δ_ ) (Algorithm 1) which updates the index _i_ by one and invokes the permutation _πδ_<sup>_ρ_ifitreachesthelimitsetbyrate</sup><sup>_r_orblock</sup><sup>_b_,</sup> depending on the full bit in the domain indicator _δ_ . 

**Algorithm 1** Increment index: S _._ inc( _δ_ <u>).</u> 

**Input:** Input state (S _, i_ ), domain _δ_ 

1: _i ← i_ + 1 _Increment index._ 2: **if** ( _δ ∧_ full = 0 and _i_ = _r_ ) or ( _δ ∧_ full = full and _i_ = _b_ ) **then** 3: S _← πδ_<sup>_ρ_(S)</sup> _Apply permutation if rate or block is full._ 4: _i ←_ 0 _Reset index._ 5: **end if** 

**Output:** Updated state (S _, i_ ). 

**Algorithm 2** End a data element <u>(padding):</u> S _._ fin( _δ_ <u>).</u> 

**Input:** Input state (S _, i_ ), domain _δ_ 1: S[ _i_ ] _←_ S[ _i_ ] _⊕_ 1 _Add padding bit, typically byte_ 0x01 _._ 2: **if** _δ ∧_ full = 0 **then** 3: S[ _r −_ 1] _←_ S[ _r −_ 1] _⊕_ 1 _Normal capacity; last rate byte gets_ 0x80 _._ 4: **end if** 5: S _← π_<sup>_ρ_</sup> _Permutation with domain end marker_ last _._ ( _δ ∨_ last)<sup>(S)</sup> 6: _i ←_ 0 _Reset index._ **Output:** Updated state (S _, i_ ). 

Markku-Juhani O. Saarinen 

7 

**Algorithm 3** Absorb data: S _._ put(D _, δ_ <u>).</u> 

**Input:** Input state (S _, i_ ), data D _∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , domain _δ_ . 

- 1: **for** _j_ = 0 _,_ 1 _, .., |_ D _| −_ 1 **do** 

#### 2: S[ _i_ ] _←_ S[ _i_ ] _⊕_ D[ _j_ ] 3: S _._ inc( _δ_ ) 4: **end for** 

_Add (xor) input data to the state. Increment index i._ 

**Output:** Updated state (S _, i_ ). 

#### **Algorithm 4** Squeeze data: D = S _._ get( _n, δ_ <u>).</u> 

**Input:** Input state (S _, i_ ), length of output _n_ , domain _δ_ . 

1: **for** _j_ = 0 _,_ 1 _, .., n −_ 1 **do** 

2: D[ _j_ ] _←_ S[ _i_ ] _Get a bit from the state._ 3: S _._ inc( _δ_ ) _Increment index i._ 4: **end for Output:** Output data D[0 _· · · n −_ 1], updated state (S _, i_ ). 

#### **Algorithm 5** Encrypt data: C = S _._ enc(P _, δ_ <u>).</u> 

**Input:** Input state (S _, i_ ), plaintext P, domain _δ_ . 

1: **for** _j_ = 0 _,_ 1 _, .., |_ P _| −_ 1 **do** 2: C[ _j_ ] _←_ S[ _i_ ] _⊕_ P[ _j_ ] _Xor plaintext with the state._ 3: S[ _i_ ] _←_ C[ _j_ ] _Ciphertext goes into the state._ 4: S _._ inc( _δ_ ) _Increment index i._ 5: **end for** 

- **Output:** Ciphertext C[0 _· · · |_ P _| −_ 1], updated state (S _, i_ ). 

- **Algorithm 6** Decrypt data: P = S _._ dec(C _, δ_ <u>).</u> 

**Input:** Input state (S _, i_ ), ciphertext C, domain _δ_ . 

1: **for** _j_ = 0 _,_ 1 _, .., |_ P _| −_ 1 **do** 

2: P[ _j_ ] _←_ S[ _i_ ] _⊕_ C[ _j_ ] _Xor ciphertext with the state._ 3: S[ _i_ ] _←_ C[ _j_ ] _Ciphertext goes into the state._ 4: S _._ inc( _δ Increment index i._ 

- 4: S _._ inc( _δ_ ) 5: **end for** 

- **Output:** Plaintext P[0 _· · · |_ C _| −_ 1], updated state (S _, i_ ). 

**Table 2:** Domain indicator _δ_ bits and 

**Name Value Class Purpose** 

#### last 0x01 Flag 

Final (padded) block marker. 

full 0x02 Flag Full state indicator. 

ad 0x10 Input Authenticated Data / Hash input. adf 0x12 Input Full-state AAD (adf = ad _∨_ full). key 0x20 Input Secret key material. keyf 0x22 Input Initialization block (keyf = key _∨_ full). 

hash 0x40 Output Hash, MAC, or XOF. 

#### ptct 0x70 

In/out Plaintext/ciphertext duplex block. 

SNEIKEN and SNEIKHA 

8 

## **4 SNEIKEN: Authenticated Encryption** 

The SNEIKEN authenticated encryption with associated data (AEAD) algorithm is characterized by the following six variables: 

|**Var**|**Description**|**Length**|
|---|---|---|
|_K_|Secret key|Fixed _k_|
|_N_|Nonce or IV|Fixed _n_|
|_A_|Associated data|Any _a_|
|_P_|Plaintext|Any _p_|
|_T_|Authentication tag|Fixed _t_|
|_C_|Ciphertext|_p_+_t_|

The algorithm provides integrity and confidentiality protection for _P_ and _C_ but only integrity protection for _A_ . Capacity _c_ = _b − r_ is equivalent to the key size _k_ in encryption and decryption. Associated data is processed at with full-state rate ( _r_ = _b_ ). Generally speaking, the confidentiality is at _k_ -bit security level and integrity is at _t_ -bit level. SNEIKEN128 is the primary member of the family: 

|**Name**|**Rate**|**Rounds**|**Key**|**Nonce**|**Tag**|
|---|---|---|---|---|---|
|SNEIKEN128|_r_ = 384|_ρ_= 6|_k_ = 128|_n_= 128|_t_= 128|
|SNEIKEN192|_r_ = 320|_ρ_= 7|_k_ = 192|_n_= 128|_t_= 128|
|SNEIKEN256|_r_ = 256|_ρ_= 8|_k_ = 256|_n_= 128|_t_= 128|

**Encryption and decryption.** We define a 6-byte “variant identifier block” as follows: ID[0 _.._ 5] = 0x61 _,_ 0x65 _, r/_ 8 _, k/_ 8 _, n/_ 8 _, t/_ 8 (5) 

The first two bytes are ASCII ’a’ and ’e’, followed by byte lengths for rate, key, nonce, and tag. We denote the encryption process by _C ←_ SNEIKEN( _K, N, A, P_ ). Algorithm 7 contains the full procedure for SNEIKEN using the BLNK2 primitives from Section 3. 

**Algorithm 7** Authenticated encryption _C ←_ SNEIKEN( _K, N, A, P_ <u>).</u> 

**Input:** Secret key _K_ , (public) nonce _N_ , associated data _A_ , and plaintext _P_ . 

1: S _._ clr() _Initialize the state:_ S = 0<sup>_b_</sup> _, i_ = 0 2: S _._ put(ID _∥ K ∥ N,_ keyf) _Identifier, secret key, and nonce._ 3: S _._ fin(keyf) _Pad and permute the key block._ 4: S _._ put( _A,_ adf) _Associated authenticated data._ 5: S _._ fin(adf) _Pad and permute, even if a_ = 0 _._ 6: _C_<sup>_′_</sup> _←_ S _._ enc( _P,_ ptct) _Actual ciphertext._ 7: S _._ fin(ptct) _Pad and permute, even if p_ = 0 _._ 8: _T ←_ S _._ get( _t,_ hash) _Authentication tag, t bits._ 9: _C ← C_<sup>_′_</sup> _∥ T Authenticated ciphertext._ **Output:** Ciphertext _C_ . 

Algorithm 8 specifies the corresponding decryption and authentication function 

_{P,_ FAIL _} ←_ SNEIKEN<sup>_−_1</sup> ( _K, N, A, C_ ) _._ (6) 

Decryption must output **only** FAIL upon integrity check failure (no partial plaintext!) 

**Code Size.** Compiling size-optimized encrypt.c that implements the NIST AEAD API (for Encryption and Decryption) resulted in 1100 bytes of executable code and data on AVR and 626 bytes on Cortex-M4. This is the only component required for implementation in addition to the permutation (Table 1). Full assembler implementation or coimplementation with SNEIKHA may yield smaller code size. 

Markku-Juhani O. Saarinen 

9 

**Algorithm 8** Authenticated decryption _<u>{P,</u>_ FAIL _<u>} ←</u>_ SNEIKEN<sup>_−_1</sup> <u>(</u> _K, N, A, C_ <u>).</u> 

**Input:** Secret key _K_ , (public) nonce _N_ , associated data _A_ , and ciphertext _C_ ( _p_ + _t_ bits). 

1: S _._ clr() 

2: S _._ put(ID _∥ K ∥ N,_ keyf) 

3: S _._ fin(keyf) 

4: S _._ put( _A,_ adf) 

5: S _._ fin(adf) 

6: _P ←_ S _._ dec( _C_ [0 _· · · p −_ 1] _,_ ptct) 

7: S _._ fin(ptct) 

8: _T_ = S _._ get( _t,_ hash) 

9: **if** _T_ = _C_ [ _p · · · p_ + _t −_ 1] **then** 10: **return** _P_ 11: **else** 12: **return** FAIL 13: **end if** 

_Initialize the state:_ S = 0<sup>_b_</sup> _, i_ = 0 _Identifier, secret key, and nonce. Pad and permute the key block. Associated authenticated data. Pad and permute, even if a_ = 0 _. Decrypt plaintext from first p bits of C. Pad and permute, even if p_ = 0 _. Authentication tag, t bits._ 

_Last t bits of C matches with tag T . Authentication failure._ 

**Output:** Plaintext _P_ or FAIL. 

**MAC-and-continue.** Lightweight protocols can avoid per-message rekeying by padding the MAC with S _._ fin(hash), and then directly continuing to process the next message (from step 4 in Algorithm 7). The decryption side must of course mirror these operations to keep both parties synchronized. 

A protocol that uses SNEIKEN in a MAC-and-continue setting can incorporate a ratchet operation S _._ ratchet() that explicitly clears the “rate” portion and is therefore irreversible. This enforces forward security when used appropriately in relation to permutation calls. The “capacity” should contain enough secret entropy to maintain security. 

Therefore MAC-and-continue is not only a significant speedup but also saves memory and provides forward security. There is no longer any need to retain the original secret keying material after initialization, unless the protocol is of connectionless datagram type. All exchanged messages are “continuously authenticated” (across messages) which simplifies handshake protocol design as separate hashes are not required.