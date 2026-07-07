# Ascon v1 

### **Submission to the CAESAR Competition** 

Christoph Dobraunig, Maria Eichlseder, Florian Mendel, Martin Schl¨affer 

**Institute for Applied Information Processing and Communications** Graz University of Technology Inffeldgasse 16a, A-8010 Graz, Austria 

Ascon `@iaik.tugraz.at` 

March 15, 2014 

## **Chapter 1** 

# **Specification** 

#### **1.1 Parameters** 

Ascon is a family of authenticated encryption designs Ascon _a,b_ -k. The family members are parametrized by the key length _k ≤_ 128 bits and internal round numbers _a, b_ . Each design specifies an authenticated encryption algorithm _Ea,b,k_ and a decryption algorithm _Da,b,k_ . 

The inputs for the authenticated encryption procedure _Ea,b,k_ are the plaintext _P_ , associated data _A_ , a secret key _K_ with _k_ bits and a public message number (nonce) _N_ with _k_ bits. No secret message number is used, i.e., its length is 0 bits. The output of the authenticated encryption procedure is an authenticated ciphertext _C_ of exactly the same length as the plaintext _P_ , and an authentication tag _T_ of size _k_ bits which authenticates both _A_ and _P_ : 

The decryption and verification procedure _Da,b,k_ takes as input the key _K_ , nonce _N_ , associated data _A_ , ciphertext _C_ and tag _T_ , and outputs the plaintext _P_ if the verification of the tag is correct or _⊥_ if the verification of the tag fails: 

#### **1.2 Recommended parameter sets** 

Tunable parameters include the key size _k_ , as well as the number of rounds _a_ for the initialization and finalization permutation _p_<sup>_a_</sup> , and the number of rounds _b_ for the intermediate permutation _p_<sup>_b_</sup> processing the associated data and plaintext. Table 1 contains our recommended parameter configurations. The list is sorted by priority, i.e., the primary recommendation is Ascon-128 and the secondary recommendation is Ascon-96. 

Table 1: Recommended parameter configurations for Ascon 

|name|algorithm||bit|size o|f|rou|nds|
|---|---|---|---|---|---|---|---|
|||key|nonce|tag|data block|_p_<sup>_a_</sup>|_p_<sup>_b_</sup>|
|Ascon-128|Ascon12_,_6-128|128|128|128|64|12|6|
|Ascon-96|Ascon12_,_8-96|96|96|96|128|12|8|

1 

#### **1.3 Notation** 

The following table specifies the notation and symbols used in this document. 

|_x ∈{_0_,_1_}_<sup>_k_</sup><br>|bitstring _x_ of length _k_ (variable if _k_ =_∗_)|
|---|---|
|0<sup>_k_</sup>_,_0<sup>_∗_</sup>|bitstring of _k_ bits or variable length, all 0|
|_|x|_|the length of the bitstring _x_ in bits|
|_⌊x⌋k_<br>|bitstring _x_ truncated to the frst (most signifcant) _k_ bits|
|_⌈x⌉_<sup>_k_</sup>|bitstring _x_ truncated to the last (least signifcant) _k_ bits|
|_x ⊕y_|xor of bitstrings _x_ and _y_|
|_x ∥y_|concatenation of bitstrings _x_ and _y_|
|_S_|the 320-bit state _S_ of the sponge construction|
|_Sr, Sc_|the _r_-bit rate and _c_-bit capacity part of the state _S_|
|_x_0_, . . . , x_4|the fve 64-bit words of the state _S_|
|_K, N, T_|secret key _K_, nonce _N_, tag _T_, all of _k ≤_128 bits|
|_P, C, A_<br>_⊥_<br>|plaintext _P_, ciphertext _C_, associated data _A_ (in blocks _Pi, Ci, Ai_)<br>error, verifcation of authenticated ciphertext failed<br>|
|_p, p_<sup>_a_</sup>_, p_<sup>_b_</sup>|permutations _p_<sup>_a_</sup>, _p_<sup>_b_ </sup>consisting of _a, b_ update rounds _p_, respectively|

#### **1.4 Mode of operation** 

The mode of operation of Ascon is based on duplex sponge modes like MonkeyDuplex [8], but uses a stronger keyed initialization and keyed finalization function. The core permutations _p_<sup>_a_</sup> and _p_<sup>_b_</sup> operate on a sponge state _S_ of size 320 bits, with a capacity of _c_ = 2 _k_ bits and a rate of _r_ = 320 _− c_ bits. For a more convenient notation, the rate and capacity parts of the state _S_ are denoted by _Sr_ and _Sc_ , respectively. The encryption and decryption operations are illustrated in Figure 1 and Figure 2 and specified in Algorithm 1. 

<!-- Start of picture text -->
A 1 As P 1 C 1 Pt Ct<br>k||a||b|| 0 ∗ r r r r r<br>p a p b p b p b p b p b p a<br>K||N c c c c c k T<br>0 ∗ ||K 0 ∗ || 1 K|| 0 ∗ K<br>Initialization Processing Processing Finalization<br>Associated Data Plaintext<br><!-- End of picture text -->

Figure 1: The encryption of Ascon. 

<!-- Start of picture text -->
A 1 As P 1 C 1 Pt Ct<br>k||a||b|| 0 ∗ r r r r r<br>p a p b p b p b p b p b p a<br>K||N c c c c c k T<br>0 ∗ ||K 0 ∗ || 1 K|| 0 ∗ K<br>Initialization AssociatedProcessingData ProcessingCiphertext Finalization<br><!-- End of picture text -->

Figure 2: The decryption of Ascon. 

2 

Algorithm 1: Authenticated encryption and decryption procedures 

|Authenticated Encryption _Ea,b,k_(_K, N, A, P_)|Verifed Decryption _Da,b,k_(_K, N, A, C, T_)|
|---|---|
|**Input:** key _K ∈{_0_,_1_}_<sup>_k_</sup>, _k ≤_128,<br>nonce _N ∈{_0_,_1_}_<sup>_k_</sup>,<br>plaintext _P ∈{_0_,_1_}_<sup>_∗_</sup>,<br>associated data _A ∈{_0_,_1_}_<sup>_∗_</sup>|**Input:** key _K ∈{_0_,_1_}_<sup>_k_</sup>, _k ≤_128,<br>nonce _N ∈{_0_,_1_}_<sup>_k_</sup>,<br>ciphertext _C ∈{_0_,_1_}_<sup>_∗_</sup>,<br>associated data _A ∈{_0_,_1_}_<sup>_∗_</sup>,<br>|
|**Output:** ciphertext _C ∈{_0_,_1_}_<sup>_∗_</sup>,<br>tag _T ∈{_0_,_1_}_<sup>_k_</sup>|tag _T ∈{_0_,_1_}_<sup>_k_</sup><br>**Output:** plaintext _P ∈{_0_,_1_}_<sup>_∗_</sup>or _⊥_|
|**Initialization**|**Initialization**|
|_c ←_2_· k_|_c ←_2_· k_|
|_r ←_320_−c_|_r ←_320_−c_|
|_P_1_. . . Pt ←_pad_r_(_P_)||
|_ℓ_=_|P|_ mod _r_|_ℓ_=_|C|_ mod _r_|
|_A_1_. . . As ←_pad<sup>_∗_</sup><br>_r_<sup>(</sup><sup>_A_)</sup><br>|_A_1_. . . As ←_pad<sup>_∗_</sup><br>_r_<sup>(</sup><sup>_A_)</sup><br>|
|_S ←k ∥a ∥b ∥_0<sup>_r−_24</sup> _∥K ∥N_<br>|_S ←k ∥a ∥b ∥_0<sup>_r−_24</sup> _∥K ∥N_<br>|
|_S ←p_<sup>_a_</sup>(_S_)_⊕_(0<sup>_r_+</sup><sup>_k _</sup>_∥K_)|_S ←p_<sup>_a_</sup>(_S_)_⊕_(0<sup>_r_+</sup><sup>_k _</sup>_∥K_)|
|**Processing Associated Data**|**Processing Associated Data**|
|**for** _i_= 1_, . . . , s_ **do**<br>|**for** _i_= 1_, . . . , s_ **do**<br>|
|_S ←p_<sup>_b_</sup>((_Sr ⊕Ai_)_∥Sc_)<br>|_S ←p_<sup>_b_</sup>((_Sr ⊕Ai_)_∥Sc_)<br>|
|_S ←S ⊕_(0<sup>319</sup> _∥_1)|_S ←S ⊕_(0<sup>319</sup> _∥_1)|
|**Processing Plaintext**|**Processing Ciphertext**|
|**for** _i_= 1_, . . . , t −_1 **do**|**for** _i_= 1_, . . . , t −_1 **do**|
|_Sr ←Sr ⊕Pi_|_Pi ←Sr ⊕Ci_|
|_Ci ←Sr_<br>|_S ←Ci ∥Sc_<br>|
|_S ←p_<sup>_b_</sup>(_S_)|_S ←p_<sup>_b_</sup>(_S_)|
|_Sr ←Sr ⊕Pt_<br>|_Pt ←⌊Sr⌋ℓ⊕Ct_<br>|
|_Ct ←⌊Sr⌋ℓ_|_Sr ←Ct ∥_(_⌈Sr⌉_<sup>_r−ℓ_</sup>_⊕_(1_∥_0<sup>_r−_1</sup><sup>_−ℓ_</sup>))|
|**Finalization**<br>|**Finalization**|
|_S ←p_<sup>_a_</sup>(_S ⊕_(0<sup>_r _</sup>_∥K ∥_0<sup>_k_</sup>))<br>|_S ←p_<sup>_a_</sup>(_S ⊕_(0<sup>_r _</sup>_∥K ∥_0<sup>_k_</sup>))|
|_T ←⌈S⌉_<sup>_k _</sup>_⊕K_<br>|<br>_T _<sup>_∗_</sup>_←⌈S⌉_<sup>_k _</sup>_⊕K_|
|**return** _C_1_∥. . . ∥Ct, T_|**if** _T_ =_T _<sup>_∗_</sup>**return** _P_1_∥. . . ∥Pt_<br>**else return** _⊥_|

##### **1.4.1 Padding** 

Ascon has a message block size of _r_ bits. The padding process appends a single 1 and the smallest number of 0s to the plaintext _P_ such that the length of the padded plaintext is a multiple of _r_ bits. The resulting padded plaintext is split into _t_ blocks of _r_ bits: _P_ 1 _∥...∥Pt_ . The same padding process is applied to split the associated data _A_ into _s_ blocks of _r_ bits: _A_ 1 _∥...∥As_ , except if the length of the associated data _A_ is zero. In this case, no padding is applied and no associated data is processed: 

##### **1.4.2 Initialization** 

The 320-bit initial value ( _IV_ ) of Ascon is formed by the secret key _K_ and nonce _N_ (both _k_ bits), as well as the key size _k_ , the initialization and finalization round number _a_ , and the intermediate round number _b_ , each written as an 8-bit integer: 

3 

In the initialization, _a_ rounds of the round transformation _p_ are applied to the initial value, followed by an xor of the secret key _K_ : 

##### **1.4.3 Processing Associated Data** 

Each (padded) associated data block _Ai_ with _i_ = 1 _, . . . , s_ is processed as follows. The block _Ai_ is xored to the first _r_ bits _Sr_ of the internal state _S_ . Then, the whole state _S_ is transformed by the permutation _p_<sup>_b_</sup> using _b_ rounds: 

After the last associated data block has been processed (also if _A_ = ∅), a single-bit domain separation constant is xored to the internal state _S_ : 

##### **1.4.4 Processing Plaintext/Ciphertext** 

**Encryption.** In each iteration, one (padded) plaintext block _Pi_ with _i_ = 1 _, ..., t_ is xored to the first _r_ bits _Sr_ of the internal state _S_ , followed by the extraction of one ciphertext block _Ci_ . For each block except the last one, the whole internal state _S_ is transformed by the permutation _p_<sup>_b_</sup> using _b_ rounds: 

The last ciphertext block is truncated to the unpadded length of the last plaintext blockfragment, _ℓ_ = _|P |_ mod _r_ : 

Thus, the length of the last ciphertext block _Ct_ is between 0 and _r −_ 1 bits, and the total length of the ciphertext _C_ is exactly the same as for the original plaintext _P_ . 

**Decryption.** In each iteration except the last one, the plaintext block _Pi_ is computed by xoring the ciphertext block _Ci_ with the first _r_ bits _Sr_ of the internal state. Then, the first _r_ bits of the internal state, _Sr_ , are replaced by _Ci_ . Finally, for each ciphertext block except the last one, the internal state is transformed by _b_ rounds of the core permutation _p_<sup>_b_</sup> : 

For the last, truncated ciphertext block with 0 _≤ ℓ< r_ bits, the procedure differs slightly: 

The plaintext is returned only if the tag _T_ has been successfully verified in the finalization. 

4 

##### **1.4.5 Finalization** 

In the finalization, the secret key _K_ is xored to the internal state and the state is transformed by the permutation _p_<sup>_a_</sup> using _a_ rounds. The tag _T_ consists of the last _k_ bits of the state xored with the key _K_ : 

The encryption algorithm returns the tag _T_ together with the ciphertext _C_ 1 _, . . . , Ct_ . The decryption algorithm returns the ciphertext _P_ 1 _, . . . , Pt_ only if the calculated tag value matches the received tag value. 

#### **1.5 The Permutations** 

The main components of Ascon are two 320-bit permutations _p_<sup>_a_</sup> (used in the initialization and finalization) and _p_<sup>_b_</sup> (used during data processing). The permutations iteratively apply an SPN-based round transformation _p_ that in turn consists of three subtransformations _pC, pS_ and _pL_ : 

_p_<sup>_a_</sup> and _p_<sup>_b_</sup> differ only in the number of rounds. The number of rounds _a_ for initialization and finalization, and the number of rounds _b_ for intermediate rounds are tunable security parameters. 

For the description and application of the round transformations, the 320-bit state _S_ is split into five 64-bit registers words _xi_ , 

as illustrated in Figure 3. 

<!-- Start of picture text -->
x 0<br>x 1<br>x 2<br>x 3<br>x 4<br><!-- End of picture text -->

Figure 3: The register word representation of the 320-bit state _S_ . 

##### **1.5.1 Addition of Constants** 

Each round _p_ starts with the constant-addition operation _pC_ which adds a round constant _cr_ to the register word _x_ 2 of the state _S_ : 

The round constant is different for each round; the values for the first round constants as required for the recommended number of rounds are given in Table 2. 

5 

Table 2: The round constants used in each round of _p_<sup>_a_</sup> and _p_<sup>_b_</sup> . 

round constant round constant 0 `0x000000000000000000f0` 6 `0x00000000000000000096` 1 `0x000000000000000000e1` 7 `0x00000000000000000087` 2 `0x000000000000000000d2` 8 `0x00000000000000000078` 3 `0x000000000000000000c3` 9 `0x00000000000000000069` 4 `0x000000000000000000b4` 10 `0x0000000000000000005a` 5 `0x000000000000000000a5` 11 `0x0000000000000000004b` _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 4 

Figure 4: The constants are added to word _x_ 2 of the state. 

<!-- Start of picture text -->
1.5.2 Substitution Layer<br>In the substitution layer pS , 64 parallel applications of the 5-bit S-box S ( x ) defined in<br>Table 3 are performed on the 320-bit state. As illustrated in Figure 5, the S-box is applied<br>to each bit-slice of the five registers  x 0 , ..., x 4, where  x 0 acts as the MSB and  x 4 as the LSB<br>of the S-box.<br>x 0<br>x 1<br>x 2<br>x 3<br>x 4<br>Figure 5: The substitution layer of Ascon applies an 5-bit S-box S ( x ) to the state.<br>Table 3: The 5-bit S-box S ( x ) of Ascon.<br>x 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15<br>S ( x ) 4 11 31 20 26 21 9 2 27 5 8 18 29 3 6 28<br>x 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31<br>S ( x ) 30 19 7 14 0 13 17 24 16 12 1 25 22 10 15 23<br>The S-box will typically be implemented in its bitsliced form, with operations performed<br>on the entire 64-bit words. Figure 6 illustrates a bitsliced computation of the S-box values.<br><!-- End of picture text -->

6 

<!-- Start of picture text -->
x 0 x 1 x 2 x 3 x 4<br>x 0 x 1 x 2 x 3 x 4<br><!-- End of picture text -->

Figure 6: Bitsliced implementation of the 5-bit S-box _S_ ( _x_ ) 

This sequence of bitsliced instructions is well-suited for pipelining, as the following implementation with five temporary registers _t_ 0 _, . . . , t_ 4 shows: 

|`x0 `|`^= `|`x4;`|`x4 `|`^= `|`x3;`|`x2 `|`^= `|`x1;`|||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|`t0`|`= `|`x0;`|`t1`|`= `|`x1;`|`t2`|`= `|`x2;`|`t3`|`= `|`x3;`|`t4`|`= `|`x4;`|
|`t0 `|`=~ `|`t0;`|`t1 `|`=~ `|`t1;`|`t2 `|`=~ `|`t2;`|`t3 `|`=~ `|`t3;`|`t4 `|`=~ `|`t4;`|
|`t0 `|`&= `|`x1;`|`t1 `|`&= `|`x2;`|`t2 `|`&= `|`x3;`|`t3 `|`&= `|`x4;`|`t4 `|`&= `|`x0;`|
|`x0 `|`^= `|`t1;`|`x1 `|`^= `|`t2;`|`x2 `|`^= `|`t3;`|`x3 `|`^= `|`t4;`|`x4 `|`^= `|`t0;`|
|`x1 `|`^= `|`x0;`|`x0 `|`^= `|`x4;`|`x3 `|`^= `|`x2;`|`x2 `|`=~ `|`x2;`||||

Figure 7: Pipelinable instructions for the 5-bit S-box _S_ ( _x_ ) 

##### **1.5.3 Linear Diffusion Layer** 

The linear diffusion layer _pL_ of Ascon is used to provide diffusion within each of the five 64-bit register words _xi_ of the 320-bit state _S_ , as illustrated in Figure 8. We apply a linear function Σ0( _x_ 0) _, . . . ,_ Σ4( _x_ 4) to each word _xi_ separately, 

where the functions Σ _i_ are defined as follows: 

<!-- Start of picture text -->
x 0<br>x 1<br>x 2<br>x 3<br>x 4<br><!-- End of picture text -->

Figure 8: The linear diffusion layer of Ascon mixes bits within words using Σ _i_ ( _xi_ ). 

7 

**Chapter 2 Security Claims** Table 4: Security claims for recommended parameter configurations of Ascon. Security in bits Requirement Ascon-128 Ascon-96 

Confidentiality of plaintext 128 96 Integrity of plaintext 128 96 Integrity of associated data 128 96 Integrity of public message number 128 96 

There is no secret message number. The public message number is a nonce, i.e., the security claims are void if two plaintexts are encrypted under the same key and the same public message number. In particular, reusing the nonce for two messages allows to detect plaintexts with common prefixes and to deduce the xor difference of the first block pair 

that differs between the two messages. Except for the single-use requirement, there are no constraints on the choice of message numbers. The decryption algorithm may only release the decrypted plaintext after verification of the final tag. Similar to GCM, a system or protocol implementing the algorithm should monitor and, if necessary, limit the number of tag verification failures per key. After reaching this limit, the decryption algorithm rejects all tags. Such a limit is not required for the 

security claims above, but may be reasonable in practice. 

The number of processed plaintext and associated data blocks protected by the encryption algorithm is limited to 2<sup>64</sup> blocks per key. This requirement also imposes a message length limit of 2<sup>64</sup> blocks, which corresponds to 2<sup>72</sup> (Ascon-128) or 2<sup>80</sup> (Ascon-96) bytes (for plaintext and associated data). 

As for most encryption algorithms, the ciphertext length leaks the plaintext length since the two lengths are equal (excluding the tag length). If the plaintext length is confidential, users must compensate this by padding their plaintexts. 

We emphasize that we do not require ideal properties for the permutations _p_<sup>_a_</sup> _, p_<sup>_b_</sup> . Nonrandom properties of the permutations _p_<sup>_a_</sup> _, p_<sup>_b_</sup> are known and do not automatically afflict the claimed security properties of the entire encryption algorithm. 

8 

## **Chapter 3** 

# active rounds probability S-boxes 1 1 2<sup>_−_2</sup> 2 4 2<sup>_−_8</sup> 3 15 2<sup>_−_30</sup> 4 _∗_ 47 2<sup>_−_94</sup> Table 6: The best known differential trail for 4 rounds of _p_ (in truncated notation). truncated # active round differential S-boxes 0 `8000000000000000` 1 1 `8020400000000000` 3 2 `8120508c0a441020` 14 3 `b1567ccd18669181` 29 total 47 

#### **3.4 Impossible Differentials** 

In this section, we will discuss the application of impossible differential cryptanalysis to Ascon. Using an automated search tool, we were able to find impossible differentials for up to five rounds of the permutation and it is likely that impossible differentials for more rounds exist. However, we have not found any practical attack on Ascon using this property of the permutation. An impossible differential for 5 rounds of the permutation is given in Table 9. 

10 

Table 7: The best known collision-producing differential trail for intermediate rounds of Ascon-128 with 117 active S-boxes (in truncated notation). 

|round|truncated|# active|
|---|---|---|
||diferential|S-boxes|
|0|`8000000000000000`|1|
|1|`8100000001400004`|5|
|2|`9902a00003c64086`|17|
|3|`fcf7eee14feefdf7`|48|
|4|`dba6fe7b4fef8cef`|45|
|5|`0000400000000000`|1|
|total||117|

Table 8: The best known collision-producing differential trail for intermediate rounds of Ascon-96 with 192 active S-boxes (in truncated notation). 

|round|truncated|# active|
|---|---|---|
||diferential|S-boxes|
|0|`8000000000000000`|1|
|1|`c200000000000000`|3|
|2|`e238e10000000000`|11|
|3|`73b7fbf67f6f19f0`|44|
|4|`bb4ffe8fd5dddf7f`|48|
|5|`fffffdffffffffff`|63|
|6|`2d0486c240902436`|20|
|7|`2080000000000000`|2|
|total||192|

Table 9: The best known impossible differential, covering 5 rounds of _p_ 

||input diferential<br>output diferential|
|---|---|
||after 5 rounds|
|_x_0|`0000000000000000`<br>`0000000000100000`|
|_x_1|`0000000000000000`<br>`0000000000000000`|
|_x_2|`0000000000000000`<br>_→_<br>`0000000000000000`|
|_x_3|`0000000000000000`<br>`0000000000000000`|
|_x_4|`8000000000000000`<br>`0000000000000000`|

11 

## **Chapter 4** 

#### **5.1 Choice of the Mode** 

The design principles of Ascon follow the sponge construction [2], to be more precise, they are very similar to SpongeWrap [3] and MonkeyDuplex [8]. The sponge-based design has several advantages compared to other available construction methods like some block cipher- or hash function-based modes, and other dedicated designs: 

- The sponge construction is well-studied and has been analyzed and proven secure for different applications in a large amount of publications. Moreover, the sponge construction is used in the SHA-3 winner Keccak. 

- Flexible to adapt for other functionality (hash, MAC, cipher) or to designs that are nonce-reuse resistant and secure under release-unverified-plaintext. 

- Elegant and simple design, obvious state size, no key schedule. 

- Plaintext and ciphertext blocks can both be computed online, without waiting for the complete message or even the message length. 

- Little implementation overhead for decryption, which uses the same round permutation as encryption. 

- Weak round transformations can be used to process additional plaintext blocks, improving the performance for long messages. 

Compared to other sponge-based designs, Ascon uses a stronger keyed initialization and keyed finalization phase. The result is that even a complete state recovery is not sufficient to recover the secret key or to allow universal forgery. 

14 

The addition of 0<sup>319</sup> _∥_ 1 after the last processed associated data block and the first plaintext block acts as a domain separation to prevent attacks that change the role of plaintext and associated data blocks. If no associated data and only an incomplete plaintext block are present, there is no additional intermediate round transformation _p_<sup>_b_</sup> , only the initialization and finalization calls _p_<sup>_a_</sup> . To prevent that key additions between the two applications of _p_<sup>_a_</sup> cancel each other out, they are added to disjoint halves of the capacity part _Sc_ of the state. **5.2 Choice of the Round Constants** The round constants have been chosen large enough to avoid slide, rotational, self-similarity or other attacks. Their values were chosen in a simple, obvious way (increasing and decreasing counter for the two halves of the affected byte), which makes them easy to compute using a simple counter and inversion operation. In addition, their low entropy shows that the constants are not used to implement any backdoors. The pattern can also easily be extended for up to 16 rounds if a very high security margin is desired. Adding more than 16 rounds is not expected to further improve the security margin. The position for inserting the round constants (in word _x_ 2) was chosen so as to allow pipelining with the next or previous few operations (message injection in the first round or the following instructions of the bit-sliced S-box implementation). Similar to the round constants, the initialization vector is forced to be asymmetric in each word by including the parameters _k, a, b_ in fixed positions and fixed 0 bits in others. This inclusion of the parameters, in particular _k_ , also serves to distinguish the different members of the Ascon family. **5.3 Choice of the Substitution Layer** The substitution layer is the only non-linear part of the round transformation. It mixes 5 bits, each at the same bit position in one of the 5 state words. The S-box was designed according to the following criteria: 

_•_ invertible and no fix-points _•_ efficient bit-sliced implementation with few, well pipelinable instructions _•_ each output bit depends on at least 4 input bits _•_ algebraic degree 2 to ease threshold implementations and masking _•_ maximum differential and linear probability 1/4 _•_ differential and linear branch number 3 _•_ avoid trivially iterable differential properties in the message injection positions The _χ_ mapping of Keccak fulfills several of the aforementioned properties and is already well analyzed. In addition, the _χ_ mapping is highly parallelizable and has a compact description with relatively few instructions. This makes _χ_ fast in both, software and hardware. The drawback of _χ_ are its differential and linear branch numbers (both 2), a fix-point at value zero and that each output bit only depends on 3 input bits, only two of them non-linearly. For a better interaction with the linear layer of Ascon and a better trade-off between performance and security, we require a branch number of 3. This and the other additional requirements can be achieved without destroying other properties by adding lightweight 15 

affine transformations to the input and output of _χ_ . The costs of these affine transformations are quickly amortized since a branch number of 3 (together with an according linear layer) essentially doubles the number of active S-boxes from round to round (in sparse trails). There are only a handful of options for a lightweight transformation (few xor operations) that achieve both required branch numbers. We experimentally selected the candidate that provided the best diffusion in combination with the selected linear layer. 

The bit-sliced design of the S-box has several benefits: it is highly efficient to implement parallel invocations on 64-bit processors (and other architectures), and no look-up tables are necessary. This effectively precludes typical cache-timing attacks for software implementations. 

The algebraic degree of 2 theoretically makes the S-box more prone to analysis with algebraic attacks; however, we did not find any practical attacks. We consider it more important to allow efficient implementation of side-channel countermeasures, such as threshold implementation [11] and masking, which is facilitated by the low degree. 

The differential and linear probabilities of the S-box are not ideal, but using one of the available 5-bit AB/APN functions like in Fides [5] was not an option due to their much more costly bit-sliced implementation. Considering the relatively lightweight linear layer, repeating more rounds of the cheaper, reasonably good S-box is more effective than fewer rounds of a perfect, but very expensive S-box. 

#### **5.4 Choice of the Linear Diffusion Layer** 

The linear diffusion layer mixes the bits within each 64-bit state word. For resistance against linear and differential cryptanalysis, we required a branch number of at least 3. Additionally, the interaction between the linear layers for separate words should provide very good diffusion, so different linear functions are necessary for the 5 different words. These requirements should be achieved at minimal cost. Although simple rotations are almost for free in hardware and relatively cheap in software, the slow diffusion requires a very large number of rounds. Moreover, the best performance can be achieved by balancing the costs of the substitution and linear layer. 

On the other hand, mixing layers as used in AES-based designs provide a high branch number, but are too expensive to provide an acceptable speed at a small size. The mixing layer of Keccak is best used with a large number of large words. Other possible candidates are the linear layers of Luffa [7], Hamsi [9], other SPN-based designs. However, these candidates were either too slow or provide a less optimal diffusion. 

The rotation values of the linear diffusion layer in Ascon are chosen similar to those of Σ in SHA-2 [10]. These functions offer a branch number of 4. Additionally, if we choose one rotation constant of each Σ function to be zero, the performance can be improved while the branch number stays the same. On the other hand, the cryptographic strength can be improved by using different rotation constants for each 64-bit word without sacrifice of performance. In this case, the branch number of the substitution and linear layer amplify each other which increases the minimum number of active S-boxes. 

#### **5.5 Statement** 

The designers have not hidden any weaknesses in this cipher. 

16 

## **Chapter 6** 

# **Tables** 

Table 10: The differential profile of the Ascon S-box. 

||0|1|2|3|4|5|6|7|8|9|a|b|c|d|e|f|10|11|12<br>|13|1|4|15|16|17|18|19|1a|1|b|1c|1d|1e<br>1f|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|32|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>|0|0|0|0|0||0|0|0|0|0|0|0||0|0|0|0<br>0|
|1|0|0|0|0|0|0|0|0|0|4|0|4|0|4|0<br>|4|0|0|0|0||0|0|0|0|4|0|4||0|4|0|4<br>0|
|2|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>|0|0|4|0|4||0|4|0|4|0|4|0||4|0|4|0<br>4|
|3|0|4|0|0|0|4|0|0|0|4|0|0|0|4|0<br>|0|4|0|0|0||4|0|0|0|4|0|0||0|4|0|0<br>0|
|4|0|0|0|0|0|0|8|0|0|0|0|0|0|0|8<br>|0|0|0|0|0||0|0|8|0|0|0|0||0|0|0|8<br>0|
|5|0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>|0|0|4|0|4||4|0|4|0|4|0|4||0|0|4|0<br>4|
|6|0|2|0|2|0|2|0|2|0|2|0|2|0|2|0<br>|2|0|2|0|2||0|2|0|2|0|2|0||2|0|2|0<br>2|
|7|0|0|4|4|0|0|4|4|0|0|4|4|0|0|4<br>|4|0|0|0|0||0|0|0|0|0|0|0||0|0|0|0<br>0|
|8|0|0|0|0|0|0|4|4|0|0|0|0|0|0|4<br>|4|0|0|0|0||0|0|4|4|0|0|0||0|0|0|4<br>4|
|9|0|2|0|2|2|0|2|0|2|0|2|0|0|2|0<br>|2|2|0|2|0||0|2|0|2|0|2|0||2|2|0|2<br>0|
|a|0|2|2|0|2|0|0|2|0|2|2|0|2|0|0<br>|2|0|2|2|0||2|0|0|2|0|2|2||0|2|0|0<br>2|
|b|0|0|2|2|0|0|2|2|0|0|2|2|0|0|2<br>|2|0|0|2|2||0|0|2|2|0|0|2||2|0|0|2<br>2|
|c|0|8|0|0|0|0|0|0|8|0|0|0|0|0|0<br>|0|8|0|0|0||0|0|0|0|0|8|0||0|0|0|0<br>0|
|d|0|2|0|2|0|2|0|2|2|0|2|0|2|0|2<br>|0|2|0|2|0||2|0|2|0|0|2|0||2|0|2|0<br>2|
|e|0|4|4|0|4|0|0|4|0|0|0|0|0|0|0<br>|0|0|4|4|0||4|0|0|4|0|0|0||0|0|0|0<br>0|
|f|0|0|0|0|0|0|0|0|4|4|0|0|4|4|0<br>|0|0|0|0|0||0|0|0|0|4|4|0||0|4|4|0<br>0|
|1|0<br>0|0|0|0|0|0|0|0|0|8|0|8|0|0|0<br>|0|0|0|0|0||0|0|0|0|8|0|8||0|0|0|0<br>0|
|1|1<br>0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>|0|0|8|0|8||0|8|0|8|0|0|0||0|0|0|0<br>0|
|1|2<br>0|2|0|2|0|2|0|2|0|2|0|2|0|2|0<br>|2|2|0|2|0||2|0|2|0|2|0|2||0|2|0|2<br>0|
|1|3<br>0|0|8|0|8|0|0|0|0|0|8|0|8|0|0<br>|0|0|0|0|0||0|0|0|0|0|0|0||0|0|0|0<br>0|
|1|4<br>0|0|0|0|4|4|4|4|0|0|0|0|4|4|4<br>|4|0|0|0|0||0|0|0|0|0|0|0||0|0|0|0<br>0|
|1|5<br>0|0|0|0|0|4|0|4|0|4|0|4|0|0|0<br>|0|0|4|0|4||0|0|0|0|0|0|0||0|0|4|0<br>4|
|1|6<br>0|0|0|0|0|0|0|0|0|0|0|0|0|0|0<br>|0|2|2|2|2||2|2|2|2|2|2|2||2|2|2|2<br>2|
|1|7<br>0|0|4|0|4|0|0|0|0|0|4|0|4|0|0<br>|0|0|0|4|0||4|0|0|0|0|0|4||0|4|0|0<br>0|
|1|8<br>0|0|0|0|2|2|2|2|0|0|0|0|2|2|2<br>|2|0|0|0|0||2|2|2|2|0|0|0||0|2|2|2<br>2|
|1|9<br>0|0|0|4|0|0|4|0|4|0|0|0|0|4|0<br>|0|4|0|0|0||0|4|0|0|0|0|0||4|0|0|4<br>0|
|1|a<br>0|2|2|0|0|2|2|0|2|0|0|2|2|0|0<br>|2|0|2|2|0||0|2|2|0|2|0|0||2|2|0|0<br>2|
|1|b<br>0|0|2|2|2|2|0|0|0|0|2|2|2|2|0<br>|0|0|0|2|2||2|2|0|0|0|0|2||2|2|2|0<br>0|
|1|c<br>0|4|0|4|0|0|0|0|4|0|4|0|0|0|0<br>|0|4|0|4|0|||0|0|0|0|4|0||4|0|0|0<br>0|
|1|d<br>0|0|0|4|0|4|0|0|4|0|0|0|0|0|4<br>|0|4|0|0|0||0|0|4|0|0|0|0||4|0|4|0<br>0|
|1|e<br>0|0|0|0|0|0|0|0|2|2|2|2|2|2|2<br>|2|0|0|0|0||0|0|0|0|2|2|2||2|2|2|2<br>2|
|1|f<br>0|0|4|4|4|4|0|0|0|0|0|0|0|0|0<br>|0|0|0|4|4||4|4|0|0|0|0|0||0|0|0|0<br>0|

19 

Table 11: The linear profile of the Ascon S-box. 

||0|1||2||3||4|5|6|7|8|9|a|b|c|d|e||f|10|11|12|13|1|4|1|5|1|6|17|18|19<br>|1a|1|b|1|c|1d|1e<br>1f|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0<br>1|6|0||0||0||0|0|0|0|0|0|0|0|0|0|0||0|0|0|0|0||0||0||0|0|0|0|0||0||0|0|0<br>0|
|1|0|0||0||0||0|0|8|0|0|4|4|0|0|-4|4||0|0|0|4|4||0||0||4|-4|4|0|-4||0|-|4|0|-4<br>0|
|2|0|0||0||0||0|0|-8|8|0|0|4|4|0|0|4||4|0|0|4|4||0||0|-|4|-4|0|0|0||0||0|0|0<br>0|
|3|0|8||0||0||0|0|0|0|0|4|0|4|0|4|0|-|4|-8|0|0|0||0||0||0|0|4|0|4||0||4|0|-4<br>0|
|4|0|0||0||4||0|-4|0|0|0|0|4|0|0|4|-4|-|4|0|0|4|0|-|4||0||0|0|0|-8|0|-|4|-|4|0|4<br>-4|
|5|0|0||0||4||0|4|0|0|0|-4|0|0|0|0|0|-|4|0|0|0|-4||4||0|-|4|-4|4|0|-4||4||0|-8|0<br>-4|
|6|0|0||0||4||0|-4|0|0|0|0|0|-4|0|4|0||0|0|0|0|-4|-|4||0|-|4|-4|0|8|0|-|4|-|4|0|-4<br>4|
|7|0|0||0|-|4||0|-4|0|0|0|4|4|4|0|0|-4||0|0|0|-4|0|-|4||0||0|0|-4|0|-4||4||0|-8|0<br>4|
|8|0|0||0||0||0|0|0|0|0|0|4|4|0|0|-4|-|4|0|0|0|0||0||0||0|0|0|8|-4||4||0|8|4<br>-4|
|9|0|0||0||0||0|0|0|-8|0|-4|0|4|0|4|0||4|0|0|4|4||0||0|-|4|4|4|0|0||4|-|4|0|0<br>4|
|a|0|0||0||0||0|0|0|0|0|0|0|0|0|0|0||0|0|0|4|4||0||0||4|4|0|8|4|-|4||0|-8|4<br>-4|
|b|0|8||0||0||0|0|0|0|0|-4|4|0|0|-4|-4||0|8|0|0|0||0||0||0|0|4|0|0|-|4||4|0|0<br>4|
|c|0|0|-|8||4|-|8|-4|0|0|0|0|0|4|0|-4|0||0|0|0|-4|0||4||0||0|0|0|0|4||0|-|4|0|0<br>0|
|d|0|0||0|-|4|-|8|4|0|0|0|4|-4|-4|0|0|-4||0|0|0|0|4|-|4||0|-|4|-4|4|0|0||0||0|0|4<br>0|
|e|0|0||0|-|4||8|-4|0|0|0|0|-4|0|0|-4|-4|-|4|0|0|0|4||4||0|-|4|-4|0|0|4||0|-|4|0|0<br>0|
|f|0|0||8|-|4|-|8|-4|0|0|0|-4|0|0|0|0|0|-|4|0|0|4|0||4||0||0|0|-4|0|0||0||0|0|-4<br>0|
|10|0|0||0||0||0|0|-8|0|0|4|0|-4|-4|0|-4||0|0|0|0|0||4|-|4||4|4|4|0|-4||0|-|4|0|-4<br>0|
|11|0|0||0||0||0|0|0|0<br>|-8|0|-4|4|-4|-4|0||0|0|8|4|-4|-|4|-|4||0|0|0|0|0||0||0|0|0<br>0|
|12|0|-8||0||0||0|0|0|0|0|-4|4|0|-4|0|0|-|4|0|0|-4|4|-|4|-|4||0|0|4|0|4||0||4|0|-4<br>0|
|13|0|0||0||0||0|0|-8|-8|0|0|0|0|4|-4|4|-|4|0|0|0|0|-|4||4||4|-4|0|0|0||0||0|0|0<br>0|
|14|0|0||0||4||0|4|0|0|0|4|4|-4|-4|-4|0|-|4|0|0|4|0||0||4|-|4|4|-4|0|4||4||0|0|0<br>4|
|15|0|0||0||4||0|-4|0|0|0|0|0|-4|4|0|-4||4|0|8|0|4||0||4||0|0|0|0|0||4||4|0|-4<br>-4|
|16|0|0||0|-|4||0|-4|0|0|0|4|0|0|-4|4|4||0|8|0|0|-4||0||4||0|0|4|0|4||4||0|0|0<br>-4|
|17|0|0||0||4||0|-4|0|0|8|0|-4|0|-4|0|0||0|0|0|4|0||0|-|4||4|-4|0|0|0||4||4|0|4<br>4|
|18|0|0||0||0||0|0|0|-8|0|4|4|0|-4|0|0||4|0|0|0|0||4|-|4|-|4|-4|-4|0|0|-|4||4|0|0<br>-4|
|19|0|0||0||0||0|0|0|0|0|0|0|0|4|-4|-4||4|0|-8|4|-4|-|4|-|4||0|0|0|0|4||4||0|0|-4<br>-4|
|1a|0|8||0||0||0|0|0|0|0|-4|0|-4|-4|0|4||0|0|0|-4|4|-|4|-|4||0|0|-4|0|0||4|-|4|0|0<br>-4|
|1b|0|0||0||0||0|0|0|0|8|0|-4|4|-4|-4|0||0|0|0|0|0|-|4||4|-|4|4|0|0|-4|-|4||0|0|-4<br>-4|
|1c|0|0||8||4||0|-4|0|0|0|4|0|0|4|-4|4||0|0|0|-4|0||0|-|4|-|4|4|4|0|0||0||0|0|4<br>0|
|1d|0|0||0|-|4||0|4|0|0|8|0|4|0|4|0|0||0|0|8|0|-4||0|-|4||0|0|0|0|4||0|-|4|0|0<br>0|
|1e|0|0||0||4||0|4|0|0|0|4|-4|4|4|4|0|-|4|8|0|0|4||0|-|4||0|0|-4|0|0||0||0|0|-4<br>0|
|1f|0|0||8||4||0|4|0|0|0|0|0|4|-4|0|-4||4|0|0|-4|0||0||4||4|-4|0|0|4||0|-|4|0|0<br>0|

20