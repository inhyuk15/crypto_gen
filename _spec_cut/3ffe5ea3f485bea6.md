# YAES v2<sup>1</sup> 

Designers: Antoon Bosselaers and Fre Vercauteren ESAT/COSIC, KU Leuven, Belgium 

Submitters: Antoon Bosselaers and Fre Vercauteren `frederik.vercauteren@esat.kuleuven.be` 

2014.05.14 

> 1 YAES is shorthand for Yet Another AES-based Authenticated Encryption Scheme 

1 

## **1 Specification** 

### **1.1 Parameters** 

YAES has three parameters: key length, nonce length and tag length. The key length will be equal to 16 bytes (128 bits), the nonce length can be between 1 and 16 bytes (but maximum of 127 bits set), and the tag length is between 8 and 16 bytes. 

### **1.2 Recommended parameter sets** 

Primary recommended parameter set `yaes128v2` : 16-byte (128 bit) key, 16-byte (127 bit, this is not a typo) nonce, 16-byte (128 bit) tag. 

### **1.3 Authenticated encryption** 

### **Notation and basic building blocks** 

- _{}_<sup>_∗_</sup> : set of finite length binary strings 

- 0<sup>_k_</sup> : a string of _k_ zero bits 

- 1<sup>_k_</sup> : a string of _k_ one bits 

- _⊕_ : bit-wise exclusive OR 

- _||_ : concatenation 

- **A** : associated data 

- **M** : plaintext 

- **K** : key 

- **N** : public message number 

- **C** : ciphertext 

- **T** : tag 

- _|X|_ : bit length of binary string _X ∈{}_<sup>_∗_</sup> where the length of the empty string is 0. 

- a binary string _a_ 0 _a_ 1 _a_ 2 _a_ 3 _a_ 4 _a_ 5 _· · ·_ is represented as a byte array _A_ with 

in particular _A_ [0] = `0x` _a_ 0 _a_ 1 _a_ 2 _a_ 3 _a_ 4 _a_ 5 _a_ 6 _a_ 7. 

- msb _b_ ( _X_ ): first _b_ bits of binary string _X ∈{}_<sup>_∗_</sup> where _b ≤|X|_ 

- _A_ 0<sup>_∗_</sup> : if _|A| <_ 128, _A ||_ 0<sup>128</sup><sup>_−|A|_</sup> else msb128( _A_ ) 

- _A_ 10<sup>_∗_</sup> : _A ||_ 10<sup>_∗_</sup> . Note that due to the 0<sup>_∗_</sup> operator, the result is always 128 bits. 

- _|X|b_ := _⌈|X|/b⌉_ : number of b-bit blocks in binary string _X ∈{}_<sup>_∗_</sup> 

- _b_ 

- **–** _X_ [0] _|| X_ [1] _|| · · · || X_ [ _x_ ] _← X_ with _x_ = _|X|b_ denotes _b_ -bit partitioning of _X_ (last block can be partial block) 

- F2128: the Galois field with 2<sup>128</sup> elements represented as F2128 _⟨θ⟩_ := F2[ _x_ ] _/f_ ( _x_ ) where _f_ ( _x_ ) = _x_<sup>128</sup> + _x_<sup>7</sup> + _x_<sup>2</sup> + _x_ +1. We note that _f_ ( _x_ ) is a primitive polynomial, i.e. the element _θ_ (or _x_ by abuse of notation) generates the full multiplicative group 

- a 128-bit string _a_ = _a_ 0 _· · · a_ 127 can be naturally interpreted as an element of F2128 as _a_ 0 + _a_ 1 _x_ + _· · ·_ + _a_ 127 _x_<sup>127</sup> 

2 

**–** _x · a_ (resp. _x_<sup>_i_</sup> _· a_ ) with _a ∈_ F2128: multiplication by _x_ (resp. _x_<sup>_i_</sup> ), note that this can be implemented by a right shift and an XOR (resp. repeated right shifts and XORs). In particular, given the bit string representation of _a_ = _a_ 0 _a_ 1 _· · · a_ 127, the bit string representation of _x · a_ is given by 

_x · a_ = _a_ 127( _a_ 0 _⊕ a_ 127)( _a_ 1 _⊕ a_ 127) _a_ 2 _a_ 3 _a_ 4 _a_ 5( _a_ 6 _⊕ a_ 127) _a_ 7 _· · · a_ 126 _._ 

- `AES128Round` ( _S, K_ ): one full AES-128 round with 16-byte state _S_ and 16-byte round key _K_ . This corresponds to the instruction ~~`m`~~ `128 aesenc` ~~`s`~~ `i128(S, K)` on processors that support AES-NI. 

- `AES128RoundKey` ( _K, i_ ): returns the round key in the _i_ -th round of AES128, where by definition `AES128RoundKey` ( _K,_ 0) returns _K_ 

- `AES128` [ `r` ] `Rounds` ( _M, K, i_ ): _r_ full AES-128 rounds starting from the _i_ -th AES128 round with _M_ 16-byte message and _K_ the 16-byte AES key (the round keys are derived from _K_ using the standard AES-128 key schedule starting from the _i_ -th round). The pseudo-code of `AES128` [ `r` ] `Rounds` ( _M, K, i_ ) is given below. 

### **Algorithm** `AES128` [ `r` ] `Rounds` ( _M, K, i_ ) 

1. _S ← M_ 

   2. **for** _j_ = 0 **to** _r −_ 1 **do** 

   3. _Kj ←_ `AES128RoundKey` ( _K, i_ + _j_ ) 

   4. _S ←_ `AES128Round` ( _S, Kj_ ) 

   5. **return** _S_ 

- `AES128` ( _M, K_ ): standard full AES-128 with 16-byte message _M_ and 16-byte key _K_ 

The inputs to the authenticated encryption function `YAES128` ~~`E`~~ `NC` are a public message number **N** of maximum 127 bits, associated data **A** , a plaintext **M** , where the total combined length of **A** and **M** is maximum 2<sup>48</sup> bytes, a key **K** of 16 bytes and a tag length 64 _≤ τ ≤_ 128. The output is the ciphertext **C** of exactly the same bit length as **M** and a tag **T** of length _τ_ . The function uses two subroutines `AD128` and `EF128` for authenticating associated data and encrypting and authenticating the message respectively. 

The inputs to the authenticated decryption function `YAES128` ~~`D`~~ `EC` are a public message number **N** , associated data **A** , a ciphertext **C** , a key **K** and a tag **T** of length _τ_ . The output is the plaintext **M** or the error symbol _⊥_ when the input is deemed invalid. 

The full specification of the `YAES128` encryption/decryption functions are given on the next page. 

3 

**Algorithm** `YAES128` ~~`E`~~ `NC` ( **N** _,_ **A** _,_ **M** _,_ **K** _, τ_ ) 

1. **if** _|_ **A** _| >_ 0 **then** TA _←_ `AD128` ( **A** _,_ **K** ) 2. **else** TA = 0<sup>128</sup> 3. ( **C** _,_ TE) _←_ `EF128` ( **N** _,_ **M** _,_ **K** ) 4. **T** = TE _⊕_ TA 5. **return** ( **C** _,_ msb _τ_ ( **T** )) 

**Algorithm** `EF128` ( **N** _,_ **M** _,_ **K** ) 

128 1. _m ←|_ **M** _|_ 128; **M** [1] _|| · · · ||_ **M** [ _m_ ] _←_ **M** 2. _L ←_ `AES128` ( **N** 10<sup>_∗_</sup> _,_ **K** ) 3. _S ←_ 0<sup>128</sup> 4. **for** _i ←_ 1 **to** _m_ **do** 5. _V ←_ `AES128` [ `6` ] `Rounds` ( _L,_ **K** _,_ 1) 6. _V ← V ⊕_ **M** [ _i_ ]10<sup>_∗_</sup> 7. _S ← S ⊕_ `AES128` [ `4` ] `Rounds` ( _V,_ **K** _,_ 7) 8. **C** [ _i_ ] _←_ msb _|_ **M** [ _i_ ] _|_ ( _V ⊕ L_ ) 9. _L ← x · L_ 10. **if** _|_ **M** [ _m_ ] _|_ = 128 **then** _L ←_ ( _x_ + 1) _· L_ 11. **else** _L ←_ ( _x_<sup>2</sup> + 1) _· L_ 12. TE _←_ `AES128` ( _S ⊕ L,_ **K** ) 13. **return** ( **C** _,_ TE) 

**Algorithm** `YAES128` ~~`D`~~ `EC` ( **N** _,_ **A** _,_ **C** _,_ **K** _,_ **T** _, τ_ ) 

|1. **if** _|_**A**_| >_0 **then** TA_←_`AD128`(**A**_,_**K**)|
|---|
|2. **else** TA = 0<sup>128</sup>|
|3. (**M**_,_TE)_←_`DF128`(**N**_,_**C**_,_**K**)|
|4. **T**<sup>_′_ </sup>= TE_⊕_TA|
|5. **if** msb_τ_(**T**<sup>_′_</sup>) =**T then return M**|
|6. **else return** _⊥_|

**Algorithm** `DF128` ( **N** _,_ **C** _,_ **K** ) 

128 1. _c ←|_ **C** _|_ 128; **C** [1] _|| · · · ||_ **C** [ _c_ ] _←_ **C** 2. _L ←_ `AES128` ( **N** 10<sup>_∗_</sup> _,_ **K** ) 3. _S ←_ 0<sup>128</sup> 4. **for** _i ←_ 1 **to** _c_ **do** 5. _V ←_ `AES128` [ `6` ] `Rounds` ( _L,_ **K** _,_ 1) 6. **M** [ _i_ ] _←_ **C** [ _i_ ] _⊕_ msb _|C_ [ _i_ ] _|_ ( _V ⊕ L_ ) 7. _V ← V ⊕_ **M** [ _i_ ]10<sup>_∗_</sup> 8. _S ← S ⊕_ `AES128` [ `4` ] `Rounds` ( _V,_ **K** _,_ 7) 9. _L ← x · L_ 10. **if** _|_ **C** [ _c_ ] _|_ = 128 **then** _L ←_ ( _x_ + 1) _· L_ 11. **else** _L ←_ ( _x_<sup>2</sup> + 1) _· L_ 12. TE _←_ `AES128` ( _S ⊕ L,_ **K** ) 13. **return** ( **M** _,_ TE) 

**Algorithm** `AD128` ( **A** _,_ **K** ) 

128 1. _a ←|_ **A** _|_ 128; **A** [1] _|| · · · ||_ **A** [ _a_ ] _←_ **A** 2. _R ←_ `AES128` (0<sup>128</sup> _,_ **K** ) 3. _S ←_ 0<sup>128</sup> 4. **for** _i ←_ 1 **to** _a_ **do** 5. _V_ = **A** [ _i_ ]10<sup>_∗_</sup> _⊕ R_ 6. _S ← S ⊕_ `AES128` [ `4` ] `Rounds` ( _V,_ **K** _,_ 1) 7. _R ← x · R_ 8. **if** _|_ **A** [ _a_ ] _|_ = 128 **then** _R ←_ ( _x_ + 1) _· R_ 9. **else** _R ←_ ( _x_<sup>2</sup> + 1) _· R_ 10. _T ←_ `AES128` ( _S ⊕ R,_ **K** ) 11. **return** _T_ 

4 

<!-- Start of picture text -->
N10*  L  xL  x 2 L  x (m-1) L<br>AES128(K)  AES 6 (K,1)  AES 6 (K,1)  AES 6 (K,1)  ......  AES 6 (K,1)<br>M[1] M[2] M[3] M[m]<br>L<br>C[1] C[2] C[3] C[m]<br>AES 4 (K,7)  AES 4 (K,7)  AES 4 (K,7)  AES 4 (K,7)<br>......  S<br>R  xR  x 2 R  x (a-1) R  S<br>x m (x+1)L<br>A[1] A[2] A[3] A[a]10*      OR<br>0*  x m (x 2 +1)L<br>AES128(K)  AES 4 (K,1)  AES 4 (K,1)  AES 4 (K,1)  AES 4 (K,1)  AES128(K)<br>TE<br>x a (x+1)R  TA<br>R  ......         OR<br>x a (x 2 +1)R<br>T<br>AES128(K)<br>TA<br>2 Security goals<br><!-- End of picture text -->

We have the following security statements for a nonce respecting adversary and for the recommended parameters: 

- key recovery attack: security 128 bits 

- confidentiality of plaintext: security 64 bits 

- integrity of plaintext/associated data: security 55 bits 

The numbers given above mean the following: the advantage of the adversary for key recovery goes up as _k/_ 2<sup>128</sup> where _k_ is the number of key guesses. The advantage of the adversary for breaking the indistinguishability-from-random goes up as _q_<sup>2</sup> _/_ 2<sup>128</sup> where _q_ is roughly the total number of blocks that are submitted to encryption oracle. The advantage of the adversary of producing a valid forgery (i.e. ciphertext/tag pair that validates and was not generated by encryption oracle) goes up as _q_<sup>2</sup> _ϵ_ + _q_<sup>2</sup> _/_ 2<sup>128</sup> where _q_ is roughly the total number of blocks that are submitted to encryption oracle 

5 

and _ϵ_ is such the implicit hash function used is _ϵ_ -AXU (almost XOR universal). The lower number for the integrity of plaintext/associated data therefore thus comes from the fact that the best bound on 4-round AES is only _ϵ_ -AXU with _ϵ_ = 2<sup>_−_113</sup> .