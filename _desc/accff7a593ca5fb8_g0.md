# **Specification** 

In this chapter, we present a full specification of our proposal `KIASU` . We first give the recommended parameter sets and then proceed with the description of the design. We explain the two authenticated encryption modes `KIASU` = and `KIASU` =, and then we describe `KIASU-BC` , a tweaked version of the `AES` block cipher. `KIASU-BC` is basically built by simply reusing the plain `AES` round function and by inserting a 64-bit tweak in each of the _r_ = 10 rounds. This can be seen as an extended version of the key schedule from the `AES` where the subkeys are XORed with the tweak value before each AddRoundKey operation. 

We first introduce some notations. We denote _EK_ ( _T, P_ ) the enciphering of the _n_ -bit plaintext _P_ with the tweakable block cipher `KIASU-BC` with _k_ -bit key _K_ and _t_ -bit tweak _T_ (similarly, _D_ represents the deciphering process). Note that we have _n_ = 128, _k_ = 128 and _t_ = 64 for `KIASU-BC` . The concatenation operation is represented by _||_ and _pad_ 10<sup>_∗_</sup> is the function that applies the 10* padding on _n_ bits, i.e. _pad_ 10<sup>_∗_</sup> ( _X_ ) = _X||_ 1 _||_ 0<sup>_n−|X|−_1</sup> when _|X| < n_ . In contrary, _unpad_ 10<sup>_∗_</sup> is the function that removes the 10* padding on _n_ bits, i.e. _unpad_ 10<sup>_∗_</sup> ( _X_ ) removes all the consecutive 0 bits in _X_ starting from the right (possibly none, possibly all). The truncation of the word _X_ to the first _i_ bits is given by _trunci_ ( _X_ ). Finally, _ϵ_ will represent the empty string. 

Our authenticated encryption scheme `KIASU` is composed of an encryption part and a verification/decryption part. The encryption part _E_ takes as input a variable-length plaintext _M_ (with _m_ = _|M |_ ), a variable-length associated data _A_ (with _a_ = _|A|_ ), a fixed-length public message number _N_ and a _k_ -bit key _K_ (we deliberately used the same letter _K_ to represent the key in the authenticated encryption scheme and the one in the tweakable block cipher, since they always refer to the same object). It outputs a _m_ -bit ciphertext _C_ and a _τ_ -bit tag `tag` (with _τ ∈_ [0 _, . . . , n_ ]), i.e. ( _C,_ `tag` ) = _EK_ ( _N, A, M_ ). The verification/decryption part _D_ takes as input a variable-length ciphertext _C_ (with _m_ = _|C|_ ), a _τ_ -bit tag `tag` (with _τ ∈_ [0 _, . . . , n_ ]), a variable-length associated data _A_ (with _a_ = _|A|_ ), a fixed-length public message number _N_ and a _k_ -bit key _K_ . It outputs either an error string _⊥_ to signify that the verification failed, or a _m_ -bit string _M_ = _DK_ ( _N, A, C,_ `tag` ) when the tag is valid. The maximum message length (in _n_ -bit blocks) is denoted _maxl_ and the maximum number of messages that can be handled with the same key is denoted _maxm_ . We have that _maxl_ = 2<sup>_⌈t/_2</sup><sup>_⌉−_3</sup> = 2<sup>29</sup> and _maxm_ = 2<sup>_⌊t/_2</sup><sup>_⌋_</sup> = 2<sup>32</sup> . This will ensure that as long as different fixed-length public message numbers (i.e. nonces) are used, the tweak inputs of all the tweakable block cipher calls are all unique. Note that there is a tradeoff possible here between _maxl_ and _maxm_ , as long as _maxl ·_ max _m_ = 2<sup>_t−_3</sup> . 

### **2.1 Parameters** 

The only parameter to the authenticated encryption `KIASU` is the choice between a nonce-respecting mode (denoted with a = sign) or a nonce-misuse resistant mode (denoted with a = sign). No parameter affects the internal tweakable block cipher `KIASU-BC` , which always uses a 128-bit key and a 64-bit tweak to select a permutation on 128 bits, mapping the plaintext space to the the ciphertext space. As we mention explicitly in the next chapter, selecting a different mode results in 

2 

quite different security notions. 

### **2.2 Recommended Parameter Sets** 

We propose two designs that have the same key, tag and public message number lengths, but differ in the security goals: 

- `KIASU` =: 128-bit key _K_ , 128-bit tag `tag` , 32-bit public message number _N_ . This design is made for nonce-respecting users (i.e. it is assumed that the public message number is always different for a same key). The encryption/authentication algorithm is denoted as _E_<sup>=</sup> , while the decryption/verification as _D_<sup>=</sup> . 

- `KIASU` =: 128-bit key _K_ , 128-bit tag `tag` , 32-bit public message number _N_ . This design is made for nonce-misuse users (i.e. it is preferable, but not required that the public message number is always different for a same key). The encryption/authentication algorithm is denoted as _E_<sup>=</sup> , while the decryption/verification as _D_<sup>=</sup> . 

The first parameter set is our preferred one, where the public message number _N_ is a nonce. 

### **2.3 Authenticated Encryption** 

In this section, we provide the high-level description of our proposal. `KIASU` uses a tweakable block cipher `KIASU-BC` as internal primitive (specified in Section 2.4), and we describe here the simple authenticated encryption modes built on top of it. `KIASU` has two main variants: 

- _E_<sup>=</sup> and _D_<sup>=</sup> (see Section 2.3.1): the first variant is for where adversaries are assumed to be nonce-respecting, meaning that the user must ensure that the value _N_ will never be used for encryption twice with the same key. This mode is largely inspired from Θ `CB3` [24], the tweakable block cipher generalization of `OCB3` . We will denote _E_<sup>=</sup> the encryption part of this first variant (and _D_<sup>=</sup> the verification/decryption part). 

- _E_<sup>=</sup> and _D_<sup>=</sup> (see Section 2.3.2): the second variant, quite close to the first one and inspired by `COPA` mode [2], relaxes this constraint and allows the user to reuse the same _N_ with the same key. We will denote _E_<sup>=</sup> the encryption part of this first variant (and _D_<sup>=</sup> the verification/decryption part). 

#### **2.3.1 Nonce-Respecting Mode:** _E_<sup>=</sup> **and** _D_<sup>=</sup> 

The encryption algorithm _E_<sup>=</sup> is depicted in Figures 2.1, 2.2 and 2.3, and an algorithmic description is given in Algorithm 1. The verification/decryption algorithmic description of _D_<sup>=</sup> is given in Algorithm 2. We note that our scheme follows the framework from Θ `CB3` [24] and therefore directly benefits from the security proof regarding authentication and privacy. 

<!-- Start of picture text -->
A 1 A 2 Ala A 1 A 2 Ala A∗ 10 ∗<br>EK 2 ,N, 1 EK 2 ,N, 2 . . . EK 2 ,N,la EK 2 ,N, 1 EK 2 ,N, 2 . . . EK 2 ,N,la EK 6 ,N,la<br>0 . . . Auth 0 . . . Auth<br>(a) Without padding. (b) With padding.<br><!-- End of picture text -->

**Figure 2.1:** Handling of the associated data for the nonce-respecting mode. 

3 

<!-- Start of picture text -->
M 1 M 2 Ml Σ<br>EK 0 ,N, 1 EK 0 ,N, 2 . . . . . . EK 0 ,N,l EK 1 ,N,l<br>final<br>Auth<br>C 1 C 2 Cl tag<br><!-- End of picture text -->

**Figure 2.2:** Message processing: in the case where the message-length is a multiple of the block size: no padding needed. 

**Algorithm 1:** The encryption algorithm _EK_<sup>=(</sup><sup>_N, A, M_).</sup> The value _N_ is encoded on log2( _maxm_ ) bits, while the integer values _i_ , _l_ and _la_ are encoded on log2( _maxl_ <u>)</u> bits. 

_/* Associated data */ A_ 1 _|| . . . ||Ala||A∗ ← A_ where each _|Ai|_ = _n_ and _|A∗| < n_ Auth _←_ 0<sup>_n_</sup> **for** _i_ = 1 **to** _la_ **do** Auth _←_ Auth _⊕ EK_ (010 _||N ||i, Ai_ ) **end if** _A∗_ = _ϵ_ **then** Auth _←_ Auth _⊕ EK_ (110 _||N ||la, pad_ 10<sup>_∗_</sup> ( _A∗_ )) **end** _/* Message */ M_ 1 _|| . . . ||Ml||M∗ ← M_ where each _|Mi|_ = _n_ and _|M∗| < n_ Checksum _←_ 0<sup>_n_</sup> **for** _i_ = 1 **to** _l_ **do** Checksum _←_ Checksum _⊕ Mi Ci ← EK_ (000 _||N ||i, Mi_ ) **end if** _M∗_ = _ϵ_ **then** Final _← EK_ (001 _||N ||l,_ Checksum) _C∗ ← ϵ_ **else** Checksum _←_ Checksum _⊕ pad_ 10<sup>_∗_</sup> ( _M∗_ ) Pad _← EK_ (100 _||N ||l,_ 0<sup>_n_</sup> ) _C∗ ← M∗ ⊕ trunc|M∗|_ (Pad) Final _← EK_ (101 _||N ||l,_ Checksum) **end** _/* Tag generation */_ `tag` _← truncτ_ (Final _⊕_ Auth) **return** ( _C_ 1 _|| . . . ||Cl||C∗,_ `tag` ) 

4 

<!-- Start of picture text -->
M 1 M 2 Ml M∗ 10 ∗ Σ<br>0 n<br>EK 0 ,N, 1 EK 0 ,N, 2 . . . . . . EK 0 ,N,l EK 4 ,N,l EK 5 ,N,l<br>pad final<br>Auth<br>C 1 C 2 Cl C ∗ tag<br><!-- End of picture text -->

**Figure 2.3:** Message processing: in the case where the message-length is a not multiple of the block size. Note that the checksum Σ is computed with a 10<sup>_∗_</sup> padding for block _M_<sup>_∗_</sup> . 

**Algorithm 2:** The verification/decryption algorithm _DK_<sup>=(</sup><sup>_N, A, C,_</sup><sup>`tag`).</sup> The value _N_ is encoded on log2( _maxm_ ) bits, while the integer values _i_ , _l_ and _la_ are encoded on log2( _maxl_ <u>)</u> bits. 

_/* Associated data */ A_ 1 _|| . . . ||Ala||A∗ ← A_ where each _|Ai|_ = _n_ and _|A∗| < n_ Auth _←_ 0<sup>_n_</sup> **for** _i_ = 1 **to** _la_ **do** Auth _←_ Auth _⊕ EK_ (010 _||N ||i, Ai_ ) **end if** _A∗_ = _ϵ_ **then** Auth _←_ Auth _⊕ EK_ (110 _||N ||la, pad_ 10<sup>_∗_</sup> ( _A∗_ )) **end** _/* Ciphertext */ C_ 1 _|| . . . ||Cl||C∗ ← C_ where each _|Ci|_ = _n_ and _|C∗| < n_ Checksum _←_ 0<sup>_n_</sup> **for** _i_ = 1 **to** _l_ **do** _Mi ← DK_ (000 _||N ||i, Ci_ ) Checksum _←_ Checksum _⊕ Mi_ **end if** _C∗_ = _ϵ_ **then** Final _← EK_ (001 _||N ||l,_ Checksum) _M∗ ← ϵ_ **else** Pad _← EK_ (100 _||N ||l,_ 0<sup>_n_</sup> ) _M∗ ← C∗ ⊕ trunc|C∗|_ (Pad) Checksum _←_ Checksum _⊕ pad_ 10<sup>_∗_</sup> ( _M∗_ ) Final _← EK_ (101 _||N ||l,_ Checksum) **end** _/* Tag verification */_ `tag`<sup>_′_</sup> _← truncτ_ (Final _⊕_ Auth) **if** `tag`<sup>_′_</sup> = `tag` **then return** ( _M_ 1 _|| . . . ||Ml||M∗_ ) **else return** _⊥_ **end** 

5 

### **2.4** `KIASU-BC` **: a Tweakable Block Cipher** 

For encryption, the block cipher `KIASU-BC` denoted _E_ takes three inputs: a 64-bit tweak _T_ , a 128-bit key _K_ and a 128-bit plaintext _P_ . It outputs a 128-bit ciphertext _C_ = _EK_ ( _T, P_ ) as the encryption of _P_ under the key _K_ for the tweak value _T_ . Similarly, for decryption, the ciphertext _C_ is mapped back to the plaintext by _EK_<sup>_−_1(</sup><sup>_T, C_) =</sup><sup>_P_.</sup> 

In short, `KIASU-BC` is _exactly_ the `AES` cipher, but with a fixed 64-bit tweak value XORed to the internal state (on the two first rows) after each round key addition. There is no tweak schedule. Our cipher can actually be seen as one of the simplest instance of the more general `TWEAKEY` framework [21] (see Figure 2.7). As it is based on `AES` , the 128-bit internal state of `KIASU-BC` can be viewed as a 4 _×_ 4 matrix of bytes in the field noted K defined as _GF_ (256) by the irreducible polynomial _x_<sup>8</sup> + _x_<sup>4</sup> + _x_<sup>3</sup> + _x_ + 1. A note about 16 bytes to 4 _×_ 4 matrix conversation. To load the bytes to the state of the cipher, in accordance to the load/store instructions on the Intel processors, the bytes are loaded from the first column to the last, and from the top row to the bottom row. That is, the first byte is stored at position (1 _,_ 1) of the matrix, the second at (2 _,_ 1), the fifth at (1 _,_ 2), . . . , the last at (4 _,_ 4). Similarly are loaded the 8 bytes of the tweak but only at the two two rows, i.e. the first at (1 _,_ 1), then (2 _,_ 1) _,_ (1 _,_ 2) _,_ (2 _,_ 2) _, . . . ,_ (2 _,_ 4). 

TWEAKEY Schedule Algorithm ( _p_ = 2) 

<!-- Start of picture text -->
K AES KS AES KS . . .<br>T T T T<br>P =  s 0 f . . . f sr +1 =  C<br>s 1 sr<br><!-- End of picture text -->

**Figure 2.7:** Instantiation of the `TWEAKEY` framework for `KIASU-BC` . 

#### **2.4.1 Encryption** 

`KIASU-BC` reuses the entire `AES` round function _f_<sup>1</sup> . This round function is composed of four steps `SubBytes` , `ShiftRows` , `MixColumns` , and `AddRoundTweakey` in this order (slightly modifying the FIPS 197 terminology in [1]): 

- `SubBytes` : applies a Sbox _S_ on each of the 16 bytes of the internal state (see Appendix A.1). 

- `ShiftRows` : rotates bytes located in row _i_ by _i_ positions to the left in the state byte matrix 

- `MixColumns` : applies to each byte column a column-wise linear layer defined by the multiplication in K with the Maximum-Distance-Separable (MDS) matrix **M** : 

- `AddRoundTweakey` : XOR the 128-bit round key to the internal state and the 64-bit tweak _T_ to the two first rows (see Figure 2.8). 

The internal state is initialized to _P_ and `KIASU-BC` (as `AES` ) applies 10 such _f_ rounds in total, with in addition an `AddRoundTweakey` layer before the very first round. Moreover, as in `AES` the last 

> 1In terms of AES-NI instructions on the latest processors, we use `aesenc` and `aesenclast` as round functions (without any additional modifications!). 

9 

|_T_0|_T_2|_T_4|_T_6|
|---|---|---|---|
|_T_1<br>_T_=|_T_3|_T_5|_T_7|
|0<br>|0|0|0|
|0|0|0|0|

**Figure 2.8:** Tweak in `KIASU-BC` : the 64-bit values of the tweak _T_ = _T_ 0 _||T_ 1 _. . . ||T_ 7 are placed on the top two rows of the `AES` internal state. 

of the 10 rounds does not have the `MixColumns` layer and the output of this last round represents the ciphertext. 

As in `AES` , the first round key is set to _K_ and the next one _Ki_ +1 is generated with the following function from the previous one _Ki_ , 0 _≤ i_ . We denote _Ki_ [ _j_ ] the _j_ -th byte of the subkey _Ki_ , where the byte are numbered from left to right and up to bottom, and `RCON` the constants of the `AES` key schedule (see Appendix A.2 for the actual values). Graphically, this key derivation is also described on Figure 2.9. 

We emphasize that apart from the additional tweak XOR operations between each round, the `AES` encryption process stays exactly the same, including the key scheduling algorithm. In particular, when the tweak equals zero, we have that `KIASU-BC` _K_ (0 _, P_ ) = `AES` _K_ ( _P_ ) for any _K_ and _P_ . 

<!-- Start of picture text -->
S «<br><!-- End of picture text -->

**Figure 2.9:** The original `AES-128` key scheduling algorithm. One cell represents one byte, the `«` performs a rotation upwards by one cell of the whole 4-byte column, and _S_ is the `AES` non-linear S-Box. 

#### **2.4.2 Decryption** 

The decryption round function _f_<sup>_−_1</sup> is composed of four steps `InvAddRoundTweakey` , `InvMixColumns` , `InvShiftRows` , `InvSubBytes` in this order. We note that the same tweak value _T_ is used for both encryption and decryption. Since we are transforming back the ciphertext into the plaintext, the order of the operations described for the encryption side are performed in reverse order. Consequently, in the first round, the operation `InvMixColumns` is omitted. Note also that the subkeys are used in reverse order. 

10 

- `InvAddRoundTweakey` : XOR the 128-bit round key to the internal state and the 64-bit tweak _T_ to the two rows. 

- `InvMixColumns` : applies to each byte column a column-wise linear layer defined by the multiplication in K with the Maximum Distance Separable (MDS) matrix (which is the inverse of the `MixColumns` diffusion matrix): 

- `InvShiftRows` : rotates bytes located in row _i_ by _i_ positions to the right in the state byte matrix 

- `InvSubBytes` : applies the inverse Sbox _S_<sup>_−_1</sup> on each of the 16 bytes of the internal state (see Appendix A.1). 

11 

# `AES` **S-Box and constants** 

### **A.1** `AES` **S-Box and its inverse** 

We define here the `AES` S-Box _S_ and its inverse _S_<sup>_−_1</sup> , as an array where the value of _S_ ( _x_ ) can be found at the position _x_ in the array. 

||`y0`|`y1`|`y2`|`y3`|`y4`|`y5`|`y6`|`y7`|`y8`|`y9`|`yA`|`yB`|`yC`|`yD`|`yE`|`yF`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|`0x`|`63`|`7C`|`77`|`7B`|`F2`|`6B`|`6F`|`C5`|`30`|`01`|`67`|`2B`|`FE`|`D7`|`AB`|`76`|
|`1x`|`CA`|`82`|`C9`|`7D`|`FA`|`59`|`47`|`F0`|`AD`|`D4`|`A2`|`AF`|`9C`|`A4`|`72`|`C0`|
|`2x`|`B7`|`FD`|`93`|`26`|`36`|`3F`|`F7`|`CC`|`34`|`A5`|`E5`|`F1`|`71`|`D8`|`31`|`15`|
|`3x`|`04`|`C7`|`23`|`C3`|`18`|`96`|`05`|`9A`|`07`|`12`|`80`|`E2`|`EB`|`27`|`B2`|`75`|
|`4x`|`09`|`83`|`2C`|`1A`|`1B`|`6E`|`5A`|`A0`|`52`|`3B`|`D6`|`B3`|`29`|`E3`|`2F`|`84`|
|`5x`|`53`|`D1`|`00`|`ED`|`20`|`FC`|`B1`|`5B`|`6A`|`CB`|`BE`|`39`|`4A`|`4C`|`58`|`CF`|
|`6x`|`D0`|`EF`|`AA`|`FB`|`43`|`4D`|`33`|`85`|`45`|`F9`|`02`|`7F`|`50`|`3C`|`9F`|`A8`|
|`7x`|`51`|`A3`|`40`|`8F`|`92`|`9D`|`38`|`F5`|`BC`|`B6`|`DA`|`21`|`10`|`FF`|`F3`|`D2`|
|`8x`|`CD`|`0C`|`13`|`EC`|`5F`|`97`|`44`|`17`|`C4`|`A7`|`7E`|`3D`|`64`|`5D`|`19`|`73`|
|`9x`|`60`|`81`|`4F`|`DC`|`22`|`2A`|`90`|`88`|`46`|`EE`|`B8`|`14`|`DE`|`5E`|`0B`|`DB`|
|`Ax`|`E0`|`32`|`3A`|`0A`|`49`|`06`|`24`|`5C`|`C2`|`D3`|`AC`|`62`|`91`|`95`|`E4`|`79`|
|`Bx`|`E7`|`C8`|`37`|`6D`|`8D`|`D5`|`4E`|`A9`|`6C`|`56`|`F4`|`EA`|`65`|`7A`|`AE`|`08`|
|`Cx`|`BA`|`78`|`25`|`2E`|`1C`|`A6`|`B4`|`C6`|`E8`|`DD`|`74`|`1F`|`4B`|`BD`|`8B`|`8A`|
|`Dx`|`70`|`3E`|`B5`|`66`|`48`|`03`|`F6`|`0E`|`61`|`35`|`57`|`B9`|`86`|`C1`|`1D`|`9E`|
|`Ex`|`E1`|`F8`|`98`|`11`|`69`|`D9`|`8E`|`94`|`9B`|`1E`|`87`|`E9`|`CE`|`55`|`28`|`DF`|
|`Fx`|`8C`|`A1`|`89`|`0D`|`BF`|`E6`|`42`|`68`|`41`|`99`|`2D`|`0F`|`B0`|`54`|`BB`|`16`|

**Table A.1:** The `AES` S-Box _S_ . The retrieve the value of _S_ ( _x_ ), convert _x_ to its hexadecimal representation, and use its four leftmost bits `x` and four rightmost bits `y` as coordinates in the table. For example _S_ ( `0x25` ) = `0x3F` . 

25 

```
y0y1y2y3y4y5y6y7y8y9yAyByCyDyEyF
```

|`0x`|`52`|`09`|`6A`|`D5`|`30`|`36`|`A5`|`38`|`BF`|`40`|`A3`|`9E`|`81`|`F3`|`D7`|`FB`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|`1x`|`7C`|`E3`|`39`|`82`|`9B`|`2F`|`FF`|`87`|`34`|`8E`|`43`|`44`|`C4`|`DE`|`E9`|`CB`|
|`2x`|`54`|`7B`|`94`|`32`|`A6`|`C2`|`23`|`3D`|`EE`|`4C`|`95`|`0B`|`42`|`FA`|`C3`|`4E`|
|`3x`|`08`|`2E`|`A1`|`66`|`28`|`D9`|`24`|`B2`|`76`|`5B`|`A2`|`49`|`6D`|`8B`|`D1`|`25`|
|`4x`|`72`|`F8`|`F6`|`64`|`86`|`68`|`98`|`16`|`D4`|`A4`|`5C`|`CC`|`5D`|`65`|`B6`|`92`|
|`5x`|`6C`|`70`|`48`|`50`|`FD`|`ED`|`B9`|`DA`|`5E`|`15`|`46`|`57`|`A7`|`8D`|`9D`|`84`|
|`6x`|`90`|`D8`|`AB`|`00`|`8C`|`BC`|`D3`|`0A`|`F7`|`E4`|`58`|`05`|`B8`|`B3`|`45`|`06`|
|`7x`|`D0`|`2C`|`1E`|`8F`|`CA`|`3F`|`0F`|`02`|`C1`|`AF`|`BD`|`03`|`01`|`13`|`8A`|`6B`|
|`8x`|`3A`|`91`|`11`|`41`|`4F`|`67`|`DC`|`EA`|`97`|`F2`|`CF`|`CE`|`F0`|`B4`|`E6`|`73`|
|`9x`|`96`|`AC`|`74`|`22`|`E7`|`AD`|`35`|`85`|`E2`|`F9`|`37`|`E8`|`1C`|`75`|`DF`|`6E`|
|`Ax`|`47`|`F1`|`1A`|`71`|`1D`|`29`|`C5`|`89`|`6F`|`B7`|`62`|`0E`|`AA`|`18`|`BE`|`1B`|
|`Bx`|`FC`|`56`|`3E`|`4B`|`C6`|`D2`|`79`|`20`|`9A`|`DB`|`C0`|`FE`|`78`|`CD`|`5A`|`F4`|
|`Cx`|`1F`|`DD`|`A8`|`33`|`88`|`07`|`C7`|`31`|`B1`|`12`|`10`|`59`|`27`|`80`|`EC`|`5F`|
|`Dx`|`60`|`51`|`7F`|`A9`|`19`|`B5`|`4A`|`0D`|`2D`|`E5`|`7A`|`9F`|`93`|`C9`|`9C`|`EF`|
|`Ex`|`A0`|`E0`|`3B`|`4D`|`AE`|`2A`|`F5`|`B0`|`C8`|`EB`|`BB`|`3C`|`83`|`53`|`99`|`61`|
|`Fx`|`17`|`2B`|`04`|`7E`|`BA`|`77`|`D6`|`26`|`E1`|`69`|`14`|`63`|`55`|`21`|`0C`|`7D`|
|**Table A.2:** T|he`A`|`ES`in|verse|S-B|ox_S_<sup>_−_</sup>|<sup>1</sup>. T|he r|etriev|e th|e valu|e of|_S_(_x_)|, con|vert|_x_to|its hexadecimal|
|representation<br>For example _S_|, and<br>(`0x3`|use <br>`F`) =|its fo<br>`0x2`|ur le<br>`5`.|ftmo|st bi|ts `x`|and|four|right|most|bits|`y` as|coor|dina|tes in the table.|

**A.2** `AES` **`RCON` constants** 

The Table A.3 below gives the values of constants `RCON` used in the key scheduling algorithm of the `AES` . 

8d 01 02 04 08 10 20 40 80 1b 36 6c d8 ab 4d 9a 2f 5e bc 63 c6 97 35 6a d4 b3 7d fa ef c5 91 39 72 e4 d3 bd 61 c2 9f 25 4a 94 33 66 cc 83 1d 3a 74 e8 cb 8d 01 02 04 08 10 20 40 80 1b 36 6c d8 ab 4d 9a 2f 5e bc 63 c6 97 35 6a d4 b3 7d fa ef c5 91 39 72 e4 d3 bd 61 c2 9f 25 4a 94 33 66 cc 83 1d 3a 74 e8 cb 8d 01 02 04 08 10 20 40 80 1b 36 6c d8 ab 4d 9a 2f 5e bc 63 c6 97 35 6a d4 b3 7d fa ef c5 91 39 72 e4 d3 bd 61 c2 9f 25 4a 94 33 66 cc 83 1d 3a 74 e8 cb 8d 01 02 04 08 10 20 40 80 1b 36 6c d8 ab 4d 9a 2f 5e bc 63 c6 97 35 6a d4 b3 7d fa ef c5 91 39 72 e4 d3 bd 61 c2 9f 25 4a 94 33 66 cc 83 1d 3a 74 e8 cb 8d 01 02 04 08 10 20 40 80 1b 36 6c d8 ab 4d 9a 2f 5e bc 63 c6 97 35 6a d4 b3 7d fa ef c5 91 39 72 e4 d3 bd 61 c2 9f 25 4a 94 33 66 cc 83 1d 3a 74 e8 cb 8d 

**Table A.3:** The `AES RCON` constants used in the key scheduling algorithm. The constants are written on lines from left to right, from top to bottom. For example, `RCON` [1] = 1, `RCON` (2) = 2 and `RCON` (9)=0x1b. 

26