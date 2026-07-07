## **2 Specification** 

### **2.1 Overview** 

TRIAD is a family of lightweight symmetric-key schemes based on a stream cipher, and it consists of an authenticated encryption mode Triad-AE, and a hash function Triad-HASH. 

Triad-AE has an encrypt-and-mac construction, where a stream cipher Triad-SC is used for encryption and a message authentication code Triad-MAC is used for the mac. Both Triad-SC and Triad-MAC accept a 128-bit secret key and a 96-bit nonce, and Triad-MAC outputs a 64-bit tag. The same 128-bit secret key is loaded to both Triad-SC and Triad-MAC, but the claimed security level is up to 112 bits. 

Triad-HASH is based on the sponge construction with a 256-bit permutation Triad-P. The bit security level of the hash function based on the sponge construction depends on the birthday paradox for the bit length of the capacity. To achieve 112-bit security, the bit length of the rate part is 32 bits. 

### **2.2 Notation** 

TRIAD accepts a 128-bit key _K_ and a 96-bit nonce _N_ , and they are sometimes represented by using byte arrays as 

where _K_ [ _i_ ] and _N_ [ _i_ ] denote the _i_ th memory of _K_ and _N_ , respectively. 

Byte arrays _M_ for plaintext is also defined similarly, and _M_ [ _i_ ] denote the _i_ th memory of _M_ . Sometimes, the _j_ th bit of _M_ [ _i_ ] is written as _M_ [ _i_ ] _j_ , i.e., 

where _M_ [ _i_ ]1 is the msb of _M_ [ _i_ ]. We also use the same notation for the byte array for the associated data _A_ and ciphertext _C_ . We assume that the plaintext and associated data are byte string, and the size of bits is always multiple of 8. 

3 

```
TriadUpd
```

### **2.3 Update Function and Triad-P** 

<!-- Start of picture text -->
z<br>t<br>rt 1 68 73 74 79 80 pt<br>pt 1 64 65 66 85 87 88 qt<br>qt 1 68 77 84 85 87 88 rt<br>m<br>t<br><!-- End of picture text -->

Figure 1: TRIAD update function `TriadUpd` 

**Algorithm 1** TRIAD Update Function 1: **procedure** `TriadUpd` ( **_a_** _,_ **_b_** _,_ **_c_** _, msg_ ) 

2: _t_ 1 _← a_ 68 _⊕ a_ 80 _⊕ b_ 85 _· c_ 85 

- 3: _t_ 2 _← b_ 64 _⊕ b_ 88 

- 4: _t_ 3 _← c_ 68 _⊕ c_ 88 

- 5: _z ← t_ 1 _⊕ t_ 2 _⊕ t_ 3 

- 6: _t_ 1 _← t_ 1 _⊕ a_ 73 _· a_ 79 _⊕ b_ 66 _⊕ msg_ 

- 7: _t_ 2 _← t_ 2 _⊕ b_ 65 _· b_ 87 _⊕ c_ 84 _⊕ msg_ 

8: _t_ 3 _← t_ 3 _⊕ c_ 77 _· c_ 87 _⊕ a_ 74 _⊕ msg_ 9: ( _a_ 1 _, a_ 2 _, . . . , a_ 80) _←_ ( _t_ 3 _, a_ 1 _, . . . , a_ 79) 10: ( _b_ 1 _, b_ 2 _, . . . , b_ 88) _←_ ( _t_ 1 _, b_ 1 _, . . . , b_ 87) 11: ( _c_ 1 _, c_ 2 _, . . . , c_ 88) _←_ ( _t_ 2 _, c_ 1 _, . . . , c_ 87) 12: **return** ( **_a_** _,_ **_b_** _,_ **_c_** _, z_ ) 13: **end procedure** TRIAD contains a 256-bit internal state denoted by **_a_** = ( _a_ 1 _∥a_ 2 _∥ . . . ∥a_ 80), **_b_** = ( _b_ 1 _∥b_ 2 _∥ . . . ∥a_ 88), and **_c_** = ( _c_ 1 _∥c_ 2 _∥ . . . ∥c_ 88), and the internal state is updated by the TRIAD update function `TriadUpd` . The input of `TriadUpd` is 256-bit internal state ( **_a_** _,_ **_b_** _,_ **_c_** ) and 1-bit message _msg_ . `TriadUpd` outputs the updated internal state and 1-bit key stream _z_ . Figure 1 shows the update function, and Algorithm 1 shows the detailed algorithm. 

Triad-P and Triad-P<sup>¯</sup> are a cryptographic permutation based on `TriadUpd` . They repeats `TriadUpd` 1024 times, and Triad-P<sup>¯</sup> absorb “1” in the first round. Triad-P is used in Triad-SC and Triad-HASH, and Triad-P<sup>¯</sup> is used in Triad-MAC. 

### **2.5 Triad-HASH** 

Triad-HASH follows the extended sponge construction [BDPV08, GPP11] with a 256-bit permutation Triad-P with capacity _c_ = 224, input bitrate _r_ = 32, output bitrate _r_<sup>_′_</sup> = 128, digest size _n_ = 256, and internal state size _t_ = 256 as shown in Fig. 3 

The extended sponge construction consists of three phases. 

7 

<!-- Start of picture text -->
M’ 1 M’ 2 M’hlen z 1 z 2<br>r = 32<br>r’ =  128<br>P P P P<br>c =  224<br>c’ =  128<br>absorb squeeze<br><!-- End of picture text -->

Figure 3: Extended Sponge Construction 

**Initialization:** The message _IN_ with inlen bytes is padded by appending a single 1 bit followed by the minimal number of 0 bits to reach a length that is a multiple of 32, and formatted into _hlen_ 32-bit blocks _M_ 1<sup>_′, . . . , M_</sup> _hlen_<sup>_′_.Note that</sup><sup>_M ′_</sup> _i_ +1<sup>= (</sup><sup>_in_[4</sup><sup>_i_+ 3]</sup><sup>_∥in_[4</sup><sup>_i_+ 2]</sup><sup>_∥in_[4</sup><sup>_i_+ 1]</sup><sup>_∥in_[4</sup><sup>_i_]) for</sup> any 0 _≤ i < hlen −_ 1. The initial value of the internal state is given as 

and the remaining bits are initialized by zero. 

- **Absorbing:** the 32-bit input message blocks are XORed into the first 32 bits of the state, interleaved with applications of the permutation Triad-P. 

- **Squeezing:** 32-byte array _Z_ = ([31] _∥· · · ∥Z_ [1] _∥Z_ [0]) is returned as the hash value. Then, the first 128 bits of the state are returned as an output ( _Z_ [15] _∥· · · ∥Z_ [0]). With a single application of the permutation Triad-P, the first 128 bits of the updated states are returned as an output ( _Z_ [31] _∥· · · ∥Z_ [16]).