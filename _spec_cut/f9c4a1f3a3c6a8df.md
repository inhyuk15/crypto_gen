# TRIAD v1 – A lightweight AEAD and hash function based on stream cipher Cover sheet 

Subhadeep Banik EPFL, Switzerland Takanori Isobe University of Hyogo, Japan Willi Meier FHNW, Switzerland Yosuke Todo NTT Secure Platform Laboratories, Japan Bin Zhang Chinese Academy of Science, China 

## **Contents** 

|**1**<br>**Intr**|**oduction**|**2**|
|---|---|---|
|1.1|NIST requirements . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>3|
|**2**<br>**Spe**|**cifcation**|**3**|
|2.1|Overview<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>3|
|2.2|Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>3|
|2.3|Update Function and Triad-P . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>4|
|2.4|Triad-AE<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>4|
|2.5|Triad-HASH<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>7|
|**3**<br>**Des**|**ign Rationale**|**8**|
|3.1|Perspective of Our Design . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>8|
|3.2|From Stream Cipher to AEAD<br>. . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>9|
|3.3|From Trivium to TRIAD<br>. . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>9|
|**4**<br>**Rep**|**ort of Cryptanalysis**|**11**|
|4.1|Time-Memory-Data Trade-of Attacks . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>11|
|4.2|Correlation Attack . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>12|
|4.3|Cube Attack<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>13|
|4.4|Guess-and-Determine Attack<br>. . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>14|
|4.5|Forgery Attack . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>14|
|4.6|Security of Hash Function . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>15|
|4.7|Fault Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>15|
|4.8|Security of Related-Key Attacks<br>. . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>15|
|4.9|Security under Unpreferable Use<br>. . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>15|
|**5**<br>**Perf**|**ormance**|**16**|
|5.1|Hardware Implementation . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>16|
||5.1.1<br>Triad-SC<br>. . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>17|
||5.1.2<br>Circuit Details<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>17|
||5.1.3<br>Timing<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>19|
||5.1.4<br>Performance<br>. . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>19|
|5.2|Software Implementation . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>20|
|**6**<br>**Ack**|**nowledgment**|**21**|
|**A Test**|**Vectors**|**24**|
|A.1|Triad-AE<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>24|
|A.2|Triad-HASH<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . . .<br>24|

1 

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

### **2.4 Triad-AE** 

Figure 2 summarizes the encryption of Triad-AE. 

4 

**Algorithm 2** Triad-P and Triad-P<sup>¯</sup> 

1: **procedure** `TriadP` ( **_a_** _,_ **_b_** _,_ **_c_** ) 2: **for** _i_ = 1 to 1024 **do** 3: ( **_a_** _,_ **_b_** _,_ **_c_** _, z_ ) _←_ `TriadUpd` ( **_a_** _,_ **_b_** _,_ **_c_** _,_ 0) 4: **end for** 5: **return** ( **_a_** _,_ **_b_** _,_ **_c_** ) 6: **end procedure** 

1: **procedure** `TriadPB` ( **_a_** _,_ **_b_** _,_ **_c_** ) 2: ( **_a_** _,_ **_b_** _,_ **_c_** _, z_ ) _←_ `TriadUpd` ( **_a_** _,_ **_b_** _,_ **_c_** _,_ 1) 3: **for** _i_ = 2 to 1024 **do** 4: ( **_a_** _,_ **_b_** _,_ **_c_** _, z_ ) _←_ `TriadUpd` ( **_a_** _,_ **_b_** _,_ **_c_** _,_ 0) 5: **end for** 6: **return** ( **_a_** _,_ **_b_** _,_ **_c_** ) 

7: **end procedure** 

Triad-AE provides authenticated encryption with associated data (AEAD) and accepts a 128bit key _K_ , 96-bit nonce _N_ , variable-length byte array for message _M_ , and variable-length byte array for associated data _A_ . The encryption of Triad-AE outputs a byte array for ciphertexts _C_ and its length is the same as that of message. Additionally, the encryption of Triad-AE outputs a 8-byte array for the tag _T_ . 

**Algorithm 3** Encryption and Decryption Algorithms of Triad-AE 

1: **procedure** `EncryptTriadAE` ( _K, N, M, A_ ) 2: _C ←_ `TriadSC` ( _K, N, M_ ) 3: _T ←_ `TriadMAC` ( _K, N, M, A_ ) 4: **return** ( _C, T_ ) 5: **end procedure** 1: **procedure** `DecryptTriadAE` ( _K, N, AD, C, T_ ) 2: _M ←_ `TriadSC` ( _K, N, C_ ) 3: _V ←_ `TriadMAC` ( _K, N, M, A_ ) 4: **if** _V_ = _T_ **then** 5: **return** _M_ 6: **else** 7: **return** _⊥_ 8: **end if** 9: **end procedure** 

Algorithm 3 shows the encryption and decryption algorithms of Triad-AE. Triad-AE consists of a stream cipher Triad-SC and message authentication code Triad-MAC. The encryption of Triad-AE first encrypt _M_ by using Triad-SC. Then, Triad-MAC generates a 64-bit tag _T_ independently of Triad-SC. The decryption of Triad-AE first decrypt _C_ by using Triad-SC. Then, a 64-bit tag is computed, and it verifies the delivered tag. Decrypted message is returned if the delivered tag is verified, but the message is not returned if it is not verified. 

**Triad-SC.** Triad-SC encrypts message _M_ with mlen bytes and output ciphertext _C_ with mlen bytes. Algorithm 4 shows the algorithm of Triad-SC, where a constant is defined as 

5 

<!-- Start of picture text -->
AEAD Mode of Operations T [0]8 T [0]7 T [7]1<br>1bit<br>K<br>N P ¯ f f f f f f P ¯ f f f<br>con<br>1bit 1bit<br>¯ ¯ ¯<br>A [0]8 A [0]7 A [adlen + 6]1 M [0]8 M [0]7 M [mlen − 1]1<br>C [0]8 C [0]7 C [mlen − 1]1<br>1bit<br>K<br>N P f f f<br>con<br><!-- End of picture text -->

Figure 2: Encryption of Triad-AE 

#### **Algorithm 4** Triad-SC 

|1: **procedure** `TriadSC`(_K, N, M_)<br>|
|---|
|2:<br>(_a_1_∥· · · ∥a_80)_←_(_N_[0]_∥K_[4]_∥con_[3]_∥K_[3]_∥con_[2]_∥K_[2]_∥con_[1]_∥K_[1]_∥con_[0]_∥K_[0])|
|3:<br>(_b_1_∥· · · ∥b_88)_←_(_N_[11]_∥· · · ∥N_[1])<br>|
|4:<br>(_c_1_∥· · · ∥c_88)_←_(_K_[15]_∥· · · ∥K_[5])<br>|
|5:<br>(**_a_**_,_**_b_**_,_**_c_**)_←_`TriadP`(**_a_**_,_**_b_**_,_**_c_**)|
|6:<br>**for** _i_= 0 to mlen_−_1 **do**|
|7:<br>**for** _j_ = 8 to 1 **do**|
|8:<br>(**_a_**_,_**_b_**_,_**_c_**_, z_)_←_`TriadUpd`(**_a_**_,_**_b_**_,_**_c_**_,_0)<br>|
|9:<br>_C_[_i_]_j ←M_[_i_]_j ⊕z_<br>|
|10:<br>**end for**<br>|
|11:<br>**end for**|
|12:<br>**return** _C_|
|13: **end procedure**|

6 

Note that `TriadSC` can be used to decrypt the ciphertext. 

**Triad-MAC.** Triad-MAC generates a tag _T_ from _M_ with mlen bytes and _A_ with adlen bytes. First, we apply the byte-length padding to the associated data _A_ , and the padded associated data is denoted by _A_<sup>¯</sup> . Since we restrict the size of the associated data up to 2<sup>50</sup> _−_ 1 bytes, the byte size of _A_<sup>¯</sup> becomes adlen + 7. In detail, 

Algorithm 5 shows the algorithm of Triad-MAC, where a constant is defined as Eq. (1). 

**Algorithm 5** Triad-MAC 

1: **procedure** `TriadMAC` ( _K, N, M_ ) 2: ( _a_ 1 _∥· · · ∥a_ 80) _←_ ( _N_ [0] _∥K_ [4] _∥con_ [3] _∥K_ [3] _∥con_ [2] _∥K_ [2] _∥con_ [1] _∥K_ [1] _∥con_ [0] _∥K_ [0]) 3: ( _b_ 1 _∥· · · ∥b_ 88) _←_ ( _N_ [11] _∥· · · ∥N_ [1]) 4: ( _c_ 1 _∥· · · ∥c_ 88) _←_ ( _K_ [15] _∥· · · ∥K_ [5]) 5: ( **_a_** _,_ **_b_** _,_ **_c_** ) _←_ `TriadPB` ( **_a_** _,_ **_b_** _,_ **_c_** ) 6: **for** _i_ = 0 to adlen + 7 _−_ 1 **do** 7: **for** _j_ = 8 to 1 **do** 8: ( **_a_** _,_ **_b_** _,_ **_c_** _, z_ ) _←_ `TriadUpd` ( **_a_** _,_ **_b_** _,_ **_c_** _, A_<sup>¯</sup> [ _i_ ] _j_ ) 9: **end for** 10: **end for** 11: **for** _i_ = 0 to mlen _−_ 1 **do** 12: **for** _j_ = 8 to 1 **do** 13: ( **_a_** _,_ **_b_** _,_ **_c_** _, z_ ) _←_ `TriadUpd` ( **_a_** _,_ **_b_** _,_ **_c_** _, M_ [ _i_ ] _j_ ) 14: **end for** 15: **end for** 16: ( **_a_** _,_ **_b_** _,_ **_c_** ) _←_ `TriadPB` ( **_a_** _,_ **_b_** _,_ **_c_** ) 17: **for** _i_ = 0 to 7 **do** 18: **for** _j_ = 8 to 1 **do** 19: ( **_a_** _,_ **_b_** _,_ **_c_** _, T_ [ _i_ ] _j_ ) _←_ `TriadUpd` ( **_a_** _,_ **_b_** _,_ **_c_** _,_ 0) 20: **end for** 21: **end for** 22: **return** _T_ 23: **end procedure** 

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