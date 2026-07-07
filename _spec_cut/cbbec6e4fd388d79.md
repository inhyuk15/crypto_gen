# **Elephant v1** 

## **2 Algorithmic Specification** 

The generic Elephant mode is presented in Section 2.2, and the three primitives used within the mode are presented in Sections 2.3-2.5. Before going to the mode, we briefly describe the notation used in 2.1. 

### **2.1 Notation** 

For _n ∈_ N, we let _{_ 0 _,_ 1 _}_<sup>_n_</sup> denote the set of _n_ -bit strings and _{_ 0 _,_ 1 _}_<sup>_∗_</sup> the set of arbitrarily length strings. For _X ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , we define 

to be the function that partitions _X_ into _ℓ_ = _⌈|X|/n⌉_ blocks of size _n_ bits, where the last block is appended with 0s. The expression “A ? B : C” equals B if A is true, and equals C if A is false. For _x ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> and _i ≤ n_ , we denote by _x ≪ i_ (resp., _x ≫ i_ ) a shift of _x_ to the left (resp., right) over _i_ positions. We likewise denote by _x_ ≪ _i_ (resp., _x_ ≫ _i_ ) a rotation of _x_ to the left (resp., right) over _i_ positions. We denote by _⌊x⌋i_ the _i_ left-most bits of _x_ . 

### **2.2 Elephant Authenticated Encryption Mode** 

Let _k, m, n, t ∈_ N with _k, m, t ≤ n_ . Let P : _{_ 0 _,_ 1 _}_<sup>_n_</sup> _→{_ 0 _,_ 1 _}_<sup>_n_</sup> be an _n_ -bit permutation, and _ϕ_ 1 : _{_ 0 _,_ 1 _}_<sup>_n_</sup> _→{_ 0 _,_ 1 _}_<sup>_n_</sup> be an LFSR. Define _ϕ_ 2 = _ϕ_ 1 _⊕_ id. Define the function mask : _{_ 0 _,_ 1 _}_<sup>_k_</sup> _×_ N<sup>2</sup> _→{_ 0 _,_ 1 _}_<sup>_n_</sup> as follows: 

We will describe the generic authenticated encryption mode of Elephant. It consists of two algorithms: encryption enc and decryption dec. 

3 

**Algorithm 1** Elephant encryption algorithm enc 

**Input:** ( _K, N, A, M_ ) _∈{_ 0 _,_ 1 _}_<sup>_k_</sup> _× {_ 0 _,_ 1 _}_<sup>_m_</sup> _× {_ 0 _,_ 1 _}_<sup>_∗_</sup> _× {_ 0 _,_ 1 _}_<sup>_∗_</sup> **Output:** ( _C, T_ ) _∈{_ 0 _,_ 1 _}_<sup>_|M|_</sup> _× {_ 0 _,_ 1 _}_<sup>_t_</sup> 1: _M_ 1 _. . . MℓM ←−n M_ 2: **for** _i_ = 1 _, . . . , ℓM_ **do** 3: _Ci ← Mi ⊕_ P( _N ∥_ 0<sup>_n−m_</sup> _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_0</sup> ) _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_0</sup> 4: _C ←⌊C_ 1 _. . . CℓM ⌋|M |_ 5: _T_ = 0 6: _A_ 1 _. . . AℓA ←−n N ∥A∥_ 1 7: _C_ 1 _. . . CℓC ←−n C∥_ 1 8: **for** _i_ = 1 _, . . . , ℓA_ **do** 9: _T ← T ⊕_ P( _Ai ⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_2</sup> ) _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_2</sup> 10: **for** _i_ = 1 _, . . . , ℓC_ **do** 11: _T ← T ⊕_ P( _Ci ⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_1</sup> ) _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_1</sup> 12: **return** ( _C, ⌊T ⌋t_ ) 

#### **2.2.1 Encryption** 

Encryption enc gets as input a key _K ∈{_ 0 _,_ 1 _}_<sup>_k_</sup> , a nonce _N ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> , associated data _A ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , and a message _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , and it outputs a ciphertext _C ∈ {_ 0 _,_ 1 _}_<sup>_|M|_</sup> and a tag _T ∈{_ 0 _,_ 1 _}_<sup>_t_</sup> . The description of enc is given in Algorithm 1, and it is depicted in Figure 1. 

#### **2.2.2 Decryption** 

Decryption dec gets as input a key _K ∈{_ 0 _,_ 1 _}_<sup>_k_</sup> , a nonce _N ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> , associated data _A ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , a ciphertext _C ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , and a tag _T ∈{_ 0 _,_ 1 _}_<sup>_t_</sup> , and it outputs a message _M ∈{_ 0 _,_ 1 _}_<sup>_|M|_</sup> if the tag is correct, or a dedicated _⊥_ -sign otherwise. The description of dec is given in Algorithm 2. 

### **2.3 160-Bit Permutation and LFSR** 

Section 2.3.1 defines the Spongent- _π_ [160] permutation. The 160-bit masking LFSR _ϕ_ 1 is defined in Section 2.3.2. These components are used in Dumbo. 

#### **2.3.1 Spongent Permutation** 

We denote by Spongent- _π_ [160]: _{_ 0 _,_ 1 _}_<sup>160</sup> _→{_ 0 _,_ 1 _}_<sup>160</sup> the 80-round Spongent permutation of Bogdanov et al. [21]. It operates on a 160-bit input _X_ as follows: **for** _i_ = 1 _, . . . ,_ 80 **do** _X ← X ⊕_ 0<sup>153</sup> _∥_ lCounter160( _i_ ) _⊕_ rev�0<sup>153</sup> _∥_ lCounter160( _i_ )� _X ←_ sBoxLayer160( _X_ ) _X ←_ pLayer160( _X_ ) 

4 

<!-- Start of picture text -->
N ∥ 0 n−m N ∥ 0 n−m<br>mask 0 K , 0 mask ℓ K M − 1 , 0<br>P P<br>M 1 MℓM<br>· · ·<br>C 1 CℓM<br>A 1 AℓA C 1 CℓC<br>mask K 0 , 2 mask ℓ K A− 1 , 2 mask 0 K , 1 mask ℓ K C − 1 , 1<br>P P P P<br>· · · · · · ⌊·⌋t T<br>Figure 1: Depiction of Elephant. For the encryption part (top): message is<br>n<br>padded as M 1  . . . MℓM ←− M , and ciphertext equals C = ⌊C 1  . . . CℓM ⌋|M | . For<br>the authentication part (bottom): nonce and associated data are padded as<br>A 1  . . . AℓA ←−n N ∥A∥ 1, and ciphertext is padded as C 1  . . . CℓC ←−n C∥ 1.<br><!-- End of picture text -->

where the function rev reverses the order of the bits of its input, and where the functions lCounter160, sBoxLayer160, and pLayer160 are defined as follows: 

- lCounter160: this function is a 7-bit LFSR defined by the primitive polynomial _p_ ( _x_ ) = _x_<sup>7</sup> + _x_<sup>6</sup> + 1 and initialized with “1000101”; 

- sBoxLayer160: this function consists of an S-box _S_ : _{_ 0 _,_ 1 _}_<sup>4</sup> _→{_ 0 _,_ 1 _}_<sup>4</sup> applied 40 times in parallel. In hexadecimal notation, this S-box is defined as 

|_X_|`0`|`1`|`2`|`3`|`4`|`5`|`6`|`7`|`8`|`9`|`A`|`B`|`C`|`D`|`E`|`F`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_S_(_X_)|`E`|`D`|`B`|`0`|`2`|`1`|`4`|`F`|`7`|`A`|`8`|`5`|`9`|`C`|`3`|`6`|

- pLayer160: this function moves the _j_ -th bit of its input to bit position _P_ 160( _j_ ), where 

#### **2.3.2 LFSR** 

For generating the masks of our scheme, we use the approach of Granger et al. [49]. We define _ϕ_ 1 as the following F2-linear map, where the _xi_ ’s correspond 

5 

**Algorithm 2** Elephant decryption algorithm dec 

**Input:** ( _K, N, A, C, T_ ) _∈{_ 0 _,_ 1 _}_<sup>_k_</sup> _× {_ 0 _,_ 1 _}_<sup>_m_</sup> _× {_ 0 _,_ 1 _}_<sup>_∗_</sup> _× {_ 0 _,_ 1 _}_<sup>_∗_</sup> _× {_ 0 _,_ 1 _}_<sup>_t_</sup> **Output:** _M ∈{_ 0 _,_ 1 _}_<sup>_|C|_</sup> or _⊥_ 1: _C_ 1 _. . . CℓM ←−n C_ 2: **for** _i_ = 1 _, . . . , ℓM_ **do** 3: _Mi ← Ci ⊕_ P( _N ∥_ 0<sup>_n−m_</sup> _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_0</sup> ) _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_0</sup> 4: _M ←⌊M_ 1 _. . . MℓM ⌋|C|_ 5: _T_<sup>¯</sup> = 0 6: _A_ 1 _. . . AℓA ←−n N ∥A∥_ 1 7: _C_ 1 _. . . CℓC ←−n C∥_ 1 9:8: **for** _T_ ¯ _i_ = 1 _← T, . . . , ℓ_ ¯ _⊕_ P( _AAi_ **do** _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_2</sup> ) _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_2</sup> 10: **for** ¯ _i_ = 1 _, . . . , ℓ_ ¯ _C_ **do** 11: _T ← T ⊕_ P( _Ci ⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_1</sup> ) _⊕_ mask<sup>_i_</sup> _K_<sup>_−_1</sup><sup>_,_1</sup> 12: **return** _⌊T_<sup>¯</sup> _⌋t_ = _T_ ? _M_ : _⊥_ 

to 8-bit words: 

### **2.4 176-Bit Permutation and LFSR** 

Section 2.4.1 defines the Spongent- _π_ [176] permutation. The 176-bit masking LFSR _ϕ_ 1 is defined in Section 2.4.2. These components are used in Jumbo. 

#### **2.4.1 Spongent Permutation** 

We denote by Spongent- _π_ [176]: _{_ 0 _,_ 1 _}_<sup>176</sup> _→{_ 0 _,_ 1 _}_<sup>176</sup> the 90-round Spongent permutation of Bogdanov et al. [21]. It operates on a 176-bit input _X_ as follows: 

where, as before, the function rev reverses the order of the bits of its input. The function lCounter176 is the same as lCounter160 of Section 2.3 but initialized with “1111010”, the function sBoxLayer176 consists of the function _S_ of Section 2.3 applied 44 times in parallel, and pLayer176 is now defined as the function that moves the _j_ -th bit of its input to bit position _P_ 176( _j_ ), where 

6 

#### **2.4.2 LFSR** 

For generating the masks of our scheme, we use the approach of Granger et al. [49]. The LFSR _ϕ_ 1 is defined as the following F2-linear map, where the _xi_ ’s correspond to 8-bit words: 

### **2.5 200-Bit Permutation and LFSR** 

Section 2.5.1 defines the Keccak- _f_ [200] permutation. The 200-bit masking LFSR _ϕ_ 1 is defined in Section 2.5.2. These components are used in Delirium. 

#### **2.5.1 Keccak Permutation** 

We denote by Keccak- _f_ [200]: _{_ 0 _,_ 1 _}_<sup>200</sup> _→{_ 0 _,_ 1 _}_<sup>200</sup> the 18-round Keccak permutation of Bertoni et al. [14, 47]. The state _X ∈{_ 0 _,_ 1 _}_<sup>200</sup> is represented as a 5-by-5-by-8 array _a ∈{_ 0 _,_ 1 _}_<sup>5</sup><sup>_×_5</sup><sup>_×_8</sup> , where for ( _x, y, z_ ) _∈_ Z5 _×_ Z5 _×_ Z8 the bit at position ( _x, y, z_ ) is set as 

Keccak- _f_ [200] operates on a 200-bit input _X_ as follows: 

**for** _i_ = 1 _, . . . ,_ 18 **do** 

where the functions _θ_ , _ρ_ , _π_ , _χ_ , and _ι_ are defined as follows: 

_ι_ : _a_ [ _x, y, z_ ] _← a_ [ _x, y, z_ ] _⊕ RC_ [ _i, x, y, z_ ] _._ 

For _ρ_ , the function _t_ [ _x, y_ ] is defined as 

|_t_|_x_= 3|_x_= 4|_x_= 0|_x_= 1|_x_= 2|
|---|---|---|---|---|---|
|_y_ = 2|153|231|3|10|171|
|_y_ = 1|55|276|36|300|6|
|_y_ = 0|28|91|0|1|190|
|_y_ = 4|120|78|210|66|253|
|_y_ = 3|21|136|105|45|15|

and for _ι_ , the round constants are given by 

7 

where _rc_ is computed from a binary LFSR defined by the primitive polynomial _p_ ( _x_ ) = _x_<sup>8</sup> + _x_<sup>6</sup> + _x_<sup>5</sup> + _x_<sup>4</sup> + 1. 

#### **2.5.2 LFSR** 

For generating the masks of our scheme, we use the approach of Granger et al. [49]. The LFSR _ϕ_ 1 is now defined as the following F2-linear map, where the _xi_ ’s correspond to 8-bit words: 

## **3 Parameterization of Elephant** 

Elephant consists of three instances, namely those built from instantiating the mode using the permutation and LFSR of Sections 2.3, 2.4, and 2.5, respectively. In more detail, we restrict our focus to _n ∈{_ 160 _,_ 176 _,_ 200 _}_ . We also set _m_ = 96, i.e. we restrict to nonces of size 96 bits. Parameters _k, t ∈_ N are still tunable. We propose the following three instances of Elephant (with Dumbo being the primary member): 

||||||||expected<br>security|limit on<br>online|
|---|---|---|---|---|---|---|---|---|
|instance|_k_|_m_|_n_|_t_|P|_ϕ_1|strength|complexity|
|Dumbo|128|96|160|64|Spongent-_π_[160]|(3)|2<sup>112</sup>|2<sup>50</sup>_/_(_n/_8)|
|Jumbo|128|96|176|64|Spongent-_π_[176]|(4)|2<sup>127</sup>|2<sup>50</sup>_/_(_n/_8)|
|Delirium|128|96|200|128|Keccak-_f_[200]|(5)|2<sup>127</sup>|2<sup>74</sup>_/_(_n/_8)|

Here, the online complexity is in terms of the number of _n_ -bit blocks (hence all instances support an online complexity of 2<sup>50</sup> bytes), and the strength is measured in the offline complexity, i.e., the number of primitive evaluations that the adversary can make. 

In Appendix B, we give a formal security analysis of the Elephant authenticated encryption mode in the ideal permutation model, and prove that the advantage of a nonce-based adversary in breaking security of either of the schemes is at most 

where _qe_ expresses an upper bound on the number of evaluations of the encryption function, _qd_ the number of decryption queries, _ℓ_ the maximum length of a single query in blocks, _σ_ the total online complexity in blocks, and _p_ the number of evaluations of the random primitive P. Note that the dominating term in the bound is 4 _σp/_ 2<sup>_n_</sup> . By capping _σ ≤_ 2<sup>_n−_114</sup> , this term is less than 1 as long as _p ≤_ 2<sup>112</sup> . Likewise, by capping _σ ≤_ 2<sup>_n−_130</sup> , this term is less than 1 as long as _p ≤_ 2<sup>128</sup> . However, one also needs to take the other terms of the bound 

8 

into account. Most of the terms are negligible compared to 4 _σp/_ 2<sup>_n_</sup> , and are covered by taking a slightly stricter condition on _σ_ (note that 2<sup>50</sup> _/_ ( _n/_ 8) _<_ 2<sup>46</sup> and 2<sup>74</sup> _/_ ( _n/_ 8) _≤_ 2<sup>70</sup> for each of the instances). There is one exception to these negligible terms, namely the factor _p/_ 2<sup>_k_</sup> for Jumbo and Delirium: it equals 1 for _p_ = 2<sup>128</sup> . This term thus accounts for a factor 2 loss in the security strength of Jumbo and Delirium, and we must restrict the offline complexity for these variants by a factor 2, as indicated in above table. 

We stress that these security claims only holds in the nonce-respecting setting: the adversary may not evaluate the encryption function twice under the same nonce (it may make decryption queries for a reused nonce, though). _If the nonce is reused for two different evaluations of_ enc _, security is void._ In particular, if the nonce uniqueness condition is released, trivial confidentiality and integrity attacks can be mounted. This is not considered to be a flaw in the scheme. We also do _not_ claim security in case unverified plaintext is released [5]; we note, however, that in practice decryption of the ciphertext _C_ into the message _M_ takes place _only after the tag (in turn, computed from the nonce, associated data, and ciphertext) has been verified._ Finally, security decreases in the multi-key or related-key setting. 

## **5 Summary of Known Cryptanalytic Attacks** 

After briefly reviewing security aspects of the generic Elephant mode in Section 5.1, we discuss the main cryptanalytic results on Spongent in Section 5.2, and on Keccak in Section 5.3. 

13 

### **5.1 Generic Mode** 

In Appendix B, we prove that the generic mode of Elephant, based on a tweakable block cipher, is secure. The security proof is standard, and it builds among others on ideas of Bellare and Namprempre [9] and Namprempre et al. [71] (for insights in the encrypt-then-MAC approach), and Bernstein [10] (for insights in the Wegman-Carter-Shoup MAC mode). The analysis of the underlying tweakable block cipher, in turn, builds on Granger et al. [49]. 

### **5.2 Spongent Permutation** 

We discuss the main known cryptanalytic results in detail, and refer to Appendix A.1 for a complete list. 

**Differential Cryptanalysis.** The following result of Bogdanov et al. [22] provides a lower bound on the number of active S-boxes in any differential characteristic of Spongent- _π_ [ _b_ ] with _b ≥_ 64. The result and its proof are similar to those for the block cipher PRESENT [23]. 

**Theorem 5.1** (Theorem 1 of Bogdanov et al. [22]) **.** _Any 5-round differential characteristic of_ Spongent _-π_ [ _b_ ] _with b ≥_ 64 _involves at least 10 differentially active S-boxes._ 

Theorem 5.1 implies that after _r_ rounds of Spongent- _π_ [ _b_ ] with _b ≥_ 64, at least 2 _r_ S-boxes are differentially active. Since the S-box is differentially 4-uniform, it follows that the probability of any _r_ -round characteristic is at most 2<sup>_−_4</sup><sup>_r_</sup> . 

Note that the number of rounds of Spongent- _π_ [ _b_ ] is determined such that at least _b_ S-boxes are differentially active [22]. Equivalently, Spongent- _π_ [ _b_ ] should have at least _b/_ 2 rounds. 

More rounds can be attacked by relying on truncated differentials. For example, for _b_ = 176, Zhang and Liu [94] presented a 46-round truncated differential with (marginally) significant probability. These properties are derived from multidimensional linear approximations, following Blondeau and Nyberg [20]. In the next section, linear approximations are discussed in more detail. 

In conclusion, (truncated) differential cryptanalysis does not threaten fullround Spongent- _π_ [ _b_ ], for neither _b_ = 160 nor _b_ = 176. In addition, one should keep in mind that many of the best reduced-round distinguishers require more data than is allowed to be processed by the Elephant mode (i.e., no more than 2<sup>47</sup> chosen plaintexts). 

**Linear Cryptanalysis.** In order to assess the security of the permutation Spongent- _π_ [ _b_ ] against linear cryptanalysis, we follow the approach used by Bogdanov et al. [22]: rather than computing only the correlation of individual trails, the correlation of linear approximations will be estimated. Previous work has shown that 1-bit (per round) trails are dominant in PRESENT-like designs [30, 61], meaning that one can estimate the correlation of all 1-bit linear approximations over _r_ rounds by computing the product of _r_ sparse matrices of 

14 

size _b×b_ . Table 1 shows the resulting estimates, where _cr_ denotes the maximum absolute correlation after _r_ rounds. 

Table 1: Estimated maximum correlation of linear approximations of Spongent- _π_ [ _b_ ] with _b ∈{_ 160 _,_ 176 _}_ . The total number of rounds is denoted by _R_ (that is, _R_ = 80 for _b_ = 160 and _R_ = 90 for _b_ = 176). 

||_b_= 160|_b_= 176|
|---|---|---|
|_c_40|2<sup>_−_80</sup>|2<sup>_−_80</sup>|
|_c_44|2<sup>_−_88</sup>|2<sup>_−_88</sup>|
|_cR_|2<sup>_−_160</sup>|2<sup>_−_180</sup>|

The estimates in Table 1 could be improved by taking into account additional trails. For example, Abdelraheem [1] gives improved estimates by taking into account all trails with at most four linearly active S-boxes per round. This yields slightly improved distinguishers in some cases, but still covering at most one or two additional rounds. 

The results above imply that full-round Spongent- _π_ [ _b_ ] is not threatened by linear attacks, statistical saturation attacks, or multidimensional linear attacks [30, 32]. As for differential cryptanalysis, it should be remarked that the security margin remains large, especially because even the reduced-round distinguishers typically require more data than the Elephant mode can securely process. 

**Integral Cryptanalysis.** Division properties of Spongent- _π_ [ _b_ ] have been analyzed to some extent, in particular for _b_ = 88 [46, 88, 89]. Eskandari et al. [46] built a SAT-solver based tool to find, or show the absence of, division properties. They use this tool to show that Spongent- _π_ [176] does not have a bit-based division property covering 12 rounds or more. It was verified that the same holds for Spongent- _π_ [160]. 

It is often possible to setup a distinguisher that covers more rounds, by starting from the middle of the permutation and extending the division property in the forward and backward direction. For example, Sun et al. [89] presented a zero-sum distinguisher for 21 rounds of Spongent- _π_ [160] requiring 2<sup>159</sup> data. Remark that even this reduced-round distinguisher far exceeds the data limits imposed for Elephant. 

We now discuss the ramifications of the above results in the context of impossible differentials and zero-correlation linear approximations, by relying on a result of Sun et al. [87]. Sun et al. demonstrated that a nontrivial zerocorrelation linear approximation of a permutation constructively implies the existence of an integral distinguisher. They furthermore demonstrated that, as Spongent- _π_ [ _b_ ] has a bitwise (hence self-dual) linear layer, one can conclude that for (round-reduced) Spongent- _π_ [ _b_ ], any nontrivial impossible differential that does not depend on the choice of the S-box constructively implies the existence of an integral distinguisher. 

15 

It can be concluded that Spongent has a very large margin against integraltype distinguishers. The same applies to zero correlation linear approximations and impossible differentials (not relying on the S-box structure), due to their links with integral properties. 

### **5.3 Keccak Permutation** 

We discuss the main known cryptanalytic results in detail, and refer to Appendix A.2 for a complete list. 

**Differential Cryptanalysis.** The differential properties of the permutation Keccak- _f_ [200] have been extensively analyzed and no significant differential distinguishers are expected to exist [14, 35, 65]. Due to Keccak’s weak alignment [15], there are no known analytic upper bounds on the probability of differential characteristics. Instead, computer assistance is required to determine bounds. 

The analysis in the Keccak reference [14] leads to lower bounds on the weight of symmetric characteristics in Keccak- _f_ – remark that Keccak- _f_ [200] characteristics are symmetric by definition. The results are summarized in the first three rows of Table 2. Improved bounds are presented by Mella, Daemen, and Van Assche [65] based on a dedicated search algorithm. For the characteristics corresponding to the lower bounds in Table 2, the reader is referred to Table 3 of [65]. 

Table 2: Lower and upper bounds on the minimum weight of differential characteristics in Keccak- _f_ [200] [14, 65]. 

|Rounds|Lower|bound|Upper|bound|
|---|---|---|---|---|
|2||8||8|
|3||20||20|
|4||46||46|
|5||50||89|
|6||92||142|
|18||276||—–|

Of course, the lack of high probability differential characteristics need not imply that all differentials have low probability. Bertoni et al. [15] argue that clustering of 2-round characteristics is prevented by weak alignment. This means that the propagation of differentials does not respect cell-boundaries in Keccak. Weak alignment leads the authors of Keccak to believe that it is unlikely that truncated differentials can be successfully exploited [15]. 

**Linear Cryptanalysis.** The Keccak reference [14] provides lower bounds on the weight of linear trails, where the weight of a linear trail equals minus the logarithm of the square of its correlation. These bounds are listed in Table 3. 

16 

The lower bound for full-round Keccak- _f_ [200] is 204, corresponding to a correlation which is only slightly smaller than the variance of the correlation of linear approximations in a random permutation. It should be emphasized that 204 is a rather rough lower bound, and the true minimum weight is expected to be much larger. 

As in the case of differential cryptanalysis, Bertoni et al. [15] provide arguments against clustering of linear trails based on Keccak’s weak alignment. 

Table 3: Lower and upper bounds on the minimum weight of linear trails in Keccak- _f_ [200] [14]. 

|Rounds|Lower|bound|Upper|bound|
|---|---|---|---|---|
|2||8||8|
|3||20||20|
|4||46||46|
|18||204||—–|

**Attacks Exploiting Algebraic Degree.** For keyed instances that use variants of Keccak- _f_ , such as Ketje [18] and Keyak [17], the attacks covering the highest number of rounds typically exploit the algebraic degree, e.g., cube [41], cube-like [40], or conditional cube attacks [53]. In the case of Ketje Jr., that builds on a round-reduced version of Keccak- _f_ [200], those attacks can cover up to 6 rounds [83]. If we take a broader look at constructions that use bigger variants of Keccak- _f_ , and also allow the attacker more degrees of freedom in placing the cube variables, those attacks usually lie in the region of 8 rounds [19,40,43,53,85] considering a targeted security level of 128-bits. Since Keccak- _f_ [200] used in Delirium has 18 rounds, we have a huge security margin against this type of attacks. Acknowledgments. This work was supported in part by the Research Council KU Leuven: GOA TENSE (C16/15/058). Yu Long Chen is supported by a Ph.D. Fellowship from the Research Foundation - Flanders (FWO). Christoph Dobraunig is supported by the Austrian Science Fund (FWF): J 4277-N38. Bart Mennink is supported by a postdoctoral fellowship from the Netherlands Organisation for Scientific Research (NWO) under Veni grant 016.Veni.173.017. 

### **A.1 Spongent Permutation** 

- Eskandari, Z., Kidmose, A.B., K¨olbl, S., Tiessen, T.: Finding Integral Distinguishers with Ease. In: Cid, C., Jr., M.J.J. (eds.) Selected Areas in Cryptography - SAC 2018 - 25th International Conference, Calgary, AB, Canada, August 15-17, 2018, Revised Selected Papers. Lecture Notes in Computer Science, vol. 11349, pp. 115–138. Springer (2018), `https: //doi.org/10.1007/978-3-030-10970-7` ~~`6`~~ 

- Zhang, G., Liu, M.: A distinguisher on PRESENT-like permutations with application to SPONGENT. SCIENCE CHINA Information Sciences 60(7), 72101 (2017), `https://doi.org/10.1007/s11432-016-0165-6` 

- Sun, L., Wang, W., Wang, M.: MILP-Aided Bit-Based Division Property for Primitives with Non-Bit-Permutation Linear Layers. Cryptology ePrint Archive, Report 2016/811 (2016) 

- Sun, L., Wang, M.: Towards a Further Understanding of Bit-Based Division Property. Cryptology ePrint Archive, Report 2016/392 (withdrawn) (2016) 

- Bogdanov, A., Knezevic, M., Leander, G., Toz, D., Varici, K., Verbauwhede, I.: SPONGENT: The Design Space of Lightweight Cryptographic Hashing. IEEE Trans. Computers 62(10), 2041–2053 (2013), `https://doi.or g/10.1109/TC.2012.196` 

- Abdelraheem, M.A.: Estimating the Probabilities of Low-Weight Differential and Linear Approximations on PRESENT-Like Ciphers. In: Kwon, T., Lee, M., Kwon, D. (eds.) Information Security and Cryptology - ICISC 2012 - 15th International Conference, Seoul, Korea, November 28-30, 2012, Revised Selected Papers. LNCS, vol. 7839, pp. 368–382. Springer (2012), `https://doi.org/10.1007/978-3-642-37682-5` ~~`2`~~ `6` 

- Bogdanov, A., Knezevic, M., Leander, G., Toz, D., Varici, K., Verbauwhede, I.: Spongent: A Lightweight Hash Function. In: Preneel, B., Takagi, T. (eds.) Cryptographic Hardware and Embedded Systems - CHES 2011 - 13th International Workshop, Nara, Japan, September 28 - October 1, 2011. Proceedings. LNCS, vol. 6917, pp. 312–325. Springer (2011), `https://doi.org/10.1007/978-3-642-23951-9` ~~`2`~~ `1` 

### **A.2 Keccak** 

- Chaigneau, C., Fuhr, T., Gilbert, H., Guo, J., Jean, J., Reinhard, J., Song, L.: Key-Recovery Attacks on Full Kravatte. IACR Transactions on Symmetric Cryptology 2018(1), 5–28 (2018), `https://doi.org/10.13154/t osc.v2018.i1.5-28` 

29 

- Fuhr, T., Naya-Plasencia, M., Rotella, Y.: State-Recovery Attacks on Modified Ketje Jr. IACR Transactions on Symmetric Cryptology 2018(1), 29–56 (2018), `https://doi.org/10.13154/tosc.v2018.i1.29-56` 

- Bi, W., Dong, X., Li, Z., Zong, R., Wang, X.: MILP-aided Cube-attacklike Cryptanalysis on Keccak Keyed Modes. Cryptology ePrint Archive, Report 2018/075 (2018) 

- Ye, C., Tian, T.: New Insights into Divide-and-Conquer Attacks on the Round-Reduced Keccak-MAC. Cryptology ePrint Archive, Report 2018/059 (2018) 

- Song, L., Guo, J., Shi, D.: New MILP Modeling: Improved Conditional Cube Attacks to Keccak-based Constructions. Cryptology ePrint Archive, Report 2017/1030 (2017) 

- Li, Z., Bi, W., Dong, X., Wang, X.: Improved Conditional Cube Attacks on Keccak Keyed Modes with MILP Method. In: Takagi, T., Peyrin, T. (eds.) Advances in Cryptology - ASIACRYPT 2017 - 23rd International Conference on the Theory and Applications of Cryptology and Information Security, Hong Kong, China, December 3-7, 2017, Proceedings, Part I. LNCS, vol. 10624, pp. 99–127. Springer (2017), `https://doi.org/10.1 007/978-3-319-70694-8` ~~`4`~~ 

- Li, T., Sun, Y., Liao, M., Wang, D.: Preimage Attacks on the Roundreduced Keccak with Cross-linear Structures. IACR Transactions on Symmetric Cryptology 2017(4), 39–57 (2017), `https://doi.org/10.13154/t osc.v2017.i4.39-57` 

- Dong, X., Li, Z., Wang, X., Qin, L.: Cube-like Attack on Round-Reduced Initialization of Ketje Sr. IACR Transactions on Symmetric Cryptology 2017(1), 259–280 (2017), `https://doi.org/10.13154/tosc.v2017.i1.2 59-280` 

- Mella, S., Daemen, J., Van Assche, G.: New techniques for trail bounds and application to differential trails in Keccak. IACR Transactions on Symmetric Cryptology 2017(1), 329–357 (2017), `https://doi.org/10.1 3154/tosc.v2017.i1.329-357` 

- Li, M., Cheng, L.: Distinguishing Property for Full Round KECCAK-f Permutation. In: Barolli, L., Terzo, O. (eds.) Complex, Intelligent, and Software Intensive Systems - Proceedings of the 11th International Conference on Complex, Intelligent, and Software Intensive Systems (CISIS2017), Torino, Italy, July 10-12, 2017. Advances in Intelligent Systems and Computing, vol. 611, pp. 639–646. Springer (2017), `https://doi.org/10 .1007/978-3-319-61566-0` ~~`5`~~ `9` 

- Song, L., Liao, G., Guo, J.: Non-full Sbox Linearization: Applications to Collision Attacks on Round-Reduced Keccak. In: Katz, J., Shacham, H. 

30 

(eds.) Advances in Cryptology - CRYPTO 2017 - 37th Annual International Cryptology Conference, Santa Barbara, CA, USA, August 2024, 2017, Proceedings, Part II. LNCS, vol. 10402, pp. 428–451. Springer (2017), `https://doi.org/10.1007/978-3-319-63715-0 15` 

- Huang, S., Wang, X., Xu, G., Wang, M., Zhao, J.: Conditional Cube Attack on Reduced-Round Keccak Sponge Function. In: Coron, J., Nielsen, J.B. (eds.) Advances in Cryptology - EUROCRYPT 2017 - 36th Annual International Conference on the Theory and Applications of Cryptographic Techniques, Paris, France, April 30 - May 4, 2017, Proceedings, Part II. LNCS, vol. 10211, pp. 259–288 (2017), `https://doi.org/10.1007/9783-319-56614-6 9` 

- Qiao, K., Song, L., Liu, M., Guo, J.: New Collision Attacks on RoundReduced Keccak. In: Coron, J., Nielsen, J.B. (eds.) Advances in Cryptology - EUROCRYPT 2017 - 36th Annual International Conference on the Theory and Applications of Cryptographic Techniques, Paris, France, April 30 - May 4, 2017, Proceedings, Part III. LNCS, vol. 10212, pp. 216– 243 (2017), `https://doi.org/10.1007/978-3-319-56617-7 8` 

- Saha, D., Kuila, S., Chowdhury, D.R.: SymSum: Symmetric-Sum Distinguishers Against Round Reduced SHA3. IACR Transactions on Symmetric Cryptology 2017(1), 240–258 (2017), `https://doi.org/10.13154/tosc. v2017.i1.240-258` 

- Guo, J., Liu, M., Song, L.: Linear Structures: Applications to Cryptanalysis of Round-Reduced Keccak. In: Cheon, J.H., Takagi, T. (eds.) Advances in Cryptology - ASIACRYPT 2016 - 22nd International Conference on the Theory and Application of Cryptology and Information Security, Hanoi, Vietnam, December 4-8, 2016, Proceedings, Part I. LNCS, vol. 10031, pp. 249–274 (2016), `https://doi.org/10.1007/978-3-662-53887-6` ~~`9`~~ 

- Dinur, I., Morawiecki, P., Pieprzyk, J., Srebrny, M., Straus, M.: Cube Attacks and Cube-Attack-Like Cryptanalysis on the Round-Reduced Keccak Sponge Function. In: Oswald, E., Fischlin, M. (eds.) Advances in Cryptology - EUROCRYPT 2015 - 34th Annual International Conference on the Theory and Applications of Cryptographic Techniques, Sofia, Bulgaria, April 26-30, 2015, Proceedings, Part I. LNCS, vol. 9056, pp. 733–761. Springer (2015), `https://doi.org/10.1007/978-3-662-46800-5 28` 

- Jean, J., Nikolic, I.: Internal Differential Boomerangs: Practical Analysis of the Round-Reduced Keccak- f f Permutation. In: Leander, G. (ed.) Fast Software Encryption - 22nd International Workshop, FSE 2015, Istanbul, Turkey, March 8-11, 2015, Revised Selected Papers. LNCS, vol. 9054, pp. 537–556. Springer (2015), `https://doi.org/10.1007/978-3-662-4811 6-5` ~~`2`~~ `6` 

- Kuila, S., Saha, D., Pal, M., Chowdhury, D.R.: Practical Distinguishers against 6-Round Keccak-f Exploiting Self-Symmetry. In: Pointcheval, D., 

31 

Vergnaud, D. (eds.) Progress in Cryptology - AFRICACRYPT 2014 - 7th International Conference on Cryptology in Africa, Marrakesh, Morocco, May 28-30, 2014. Proceedings. LNCS, vol. 8469, pp. 88–108. Springer (2014), `https://doi.org/10.1007/978-3-319-06734-6 6` 

- Das, S., Meier, W.: Differential Biases in Reduced-Round Keccak. In: Pointcheval, D., Vergnaud, D. (eds.) Progress in Cryptology - AFRICACRYPT 2014 - 7th International Conference on Cryptology in Africa, Marrakesh, Morocco, May 28-30, 2014. Proceedings. LNCS, vol. 8469, pp. 69– 87. Springer (2014), `https://doi.org/10.1007/978-3-319-06734-6 5` 

- Dinur, I., Morawiecki, P., Pieprzyk, J., Srebrny, M., Straus, M.: Practical Complexity Cube Attacks on Round-Reduced Keccak Sponge Function. Cryptology ePrint Archive, Report 2014/259 (2014) 

- Morawiecki, P., Pieprzyk, J., Srebrny, M., Straus, M.: Preimage attacks on the round-reduced Keccak with the aid of differential cryptanalysis. Cryptology ePrint Archive, Report 2013/561 (2013) 

- K¨olbl, S., Mendel, F., Nad, T., Schl¨affer, M.: Differential Cryptanalysis of Keccak Variants. In: Stam, M. (ed.) Cryptography and Coding - 14th IMA International Conference, IMACC 2013, Oxford, UK, December 1719, 2013. Proceedings. LNCS, vol. 8308, pp. 141–157. Springer (2013), `https://doi.org/10.1007/978-3-642-45239-0` ~~`9`~~ 

- Dinur, I., Dunkelman, O., Shamir, A.: Collision Attacks on Up to 5 Rounds of SHA-3 Using Generalized Internal Differentials. In: Moriai, S. (ed.) Fast Software Encryption - 20th International Workshop, FSE 2013, Singapore, March 11-13, 2013. Revised Selected Papers. LNCS, vol. 8424, pp. 219– 240. Springer (2013), `https://doi.org/10.1007/978-3-662-43933-3` ~~`1`~~ `2` 

- Morawiecki, P., Pieprzyk, J., Srebrny, M.: Rotational Cryptanalysis of Round-Reduced Keccak. In: Moriai, S. (ed.) Fast Software Encryption - 20th International Workshop, FSE 2013, Singapore, March 11-13, 2013. Revised Selected Papers. LNCS, vol. 8424, pp. 241–262. Springer (2013), `https://doi.org/10.1007/978-3-662-43933-3` ~~`1`~~ `3` 

- Morawiecki, P., Srebrny, M.: A SAT-based preimage analysis of reduced Keccak hash functions. Inf. Process. Lett. 113(10-11), 392–397 (2013), `https://doi.org/10.1016/j.ipl.2013.03.004` 

- Dinur, I., Dunkelman, O., Shamir, A.: New Attacks on Keccak-224 and Keccak-256. In: Canteaut, A. (ed.) Fast Software Encryption - 19th International Workshop, FSE 2012, Washington, DC, USA, March 19-21, 2012. Revised Selected Papers. LNCS, vol. 7549, pp. 442–461. Springer (2012), `https://doi.org/10.1007/978-3-642-34047-5` ~~`2`~~ `5` 

32 

- Duc, A., Guo, J., Peyrin, T., Wei, L.: Unaligned Rebound Attack: Application to Keccak. In: Canteaut, A. (ed.) Fast Software Encryption - 19th International Workshop, FSE 2012, Washington, DC, USA, March 19-21, 2012. Revised Selected Papers. LNCS, vol. 7549, pp. 402–421. Springer (2012), `https://doi.org/10.1007/978-3-642-34047-5 23` 

- Daemen, J., Van Assche, G.: Differential Propagation Analysis of Keccak. In: Canteaut, A. (ed.) Fast Software Encryption - 19th International Workshop, FSE 2012, Washington, DC, USA, March 19-21, 2012. Revised Selected Papers. LNCS, vol. 7549, pp. 422–441. Springer (2012), `https://doi.org/10.1007/978-3-642-34047-5` ~~`2`~~ `4` 

- Naya-Plasencia, M., R¨ock, A., Meier, W.: Practical Analysis of ReducedRound Keccak. In: Bernstein, D.J., Chatterjee, S. (eds.) Progress in Cryptology - INDOCRYPT 2011 - 12th International Conference on Cryptology in India, Chennai, India, December 11-14, 2011. Proceedings. LNCS, vol. 7107, pp. 236–254. Springer (2011), `https://doi.org/10.1007/978-3642-25578-6` ~~`1`~~ `8` 

- Duan, M., Lai, X.: Improved zero-sum distinguisher for full round Keccak-f permutation. Cryptology ePrint Archive, Report 2011/023 (2011) 

- Boura, C., Canteaut, A., De Canni`ere, C.: Higher-Order Differential Properties of Keccak and _Luffa_ . In: Joux, A. (ed.) Fast Software Encryption - 18th International Workshop, FSE 2011, Lyngby, Denmark, February 1316, 2011, Revised Selected Papers. LNCS, vol. 6733, pp. 252–269. Springer (2011), `https://doi.org/10.1007/978-3-642-21702-9 15` 

- Bertoni, G., Daemen, J., Peeters, M., Van Assche, G.: The Keccak reference (January 2011) 

- Boura, C., Canteaut, A.: Zero-Sum Distinguishers for Iterated Permutations and Application to Keccak- _f_ and Hamsi-256. In: Biryukov, A., Gong, G., Stinson, D.R. (eds.) Selected Areas in Cryptography - 17th International Workshop, SAC 2010, Waterloo, Ontario, Canada, August 12-13, 2010, Revised Selected Papers. LNCS, vol. 6544, pp. 1–17. Springer (2010), `https://doi.org/10.1007/978-3-642-19574-7` ~~`1`~~ 

- Boura, C., Canteaut, A.: A zero-sum property for the KECCAK-f permutation with 18 rounds. In: IEEE International Symposium on Information Theory, ISIT 2010, June 13-18, 2010, Austin, Texas, USA, Proceedings. pp. 2488–2492. IEEE (2010), `https://doi.org/10.1109/ISIT.2010.55 13442` 

- Bernstein, D.J.: Second preimages for 6 (7? (8??)) rounds of Keccak? NIST hash forum: `http://cr.yp.to/hash/keccak-20101127.txt` (2009) 

- Lathrop, J.: Cube attacks on cryptographic hash functions. Thesis: `https: //scholarworks.rit.edu/theses/650/` (2009) 

33 

- Aumasson, J.P., Khovratovich, D.: Zero-sum distinguishers for reduced Keccak-f for the core functions of Luffa and Hamsi. Rump session of CHES: `https://131002.net/data/papers/AM09.pdf` (2009) 

- Aumasson, J.P., Khovratovich, D.: First Analysis of Keccak. NIST hash forum: `https://131002.net/data/papers/AK09.pdf` (2009) 

#### **B.1.1 Authenticated Encryption** 

An authenticated encryption scheme AE consists of two algorithms enc and dec. Encryption enc gets as input a key _K ∈{_ 0 _,_ 1 _}_<sup>_k_</sup> , a nonce _N ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> , associated data _A ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , and a message _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , and it outputs a ciphertext _C ∈{_ 0 _,_ 1 _}_<sup>_|M|_</sup> and a tag _T ∈{_ 0 _,_ 1 _}_<sup>_t_</sup> . Decryption dec gets as input a key _K ∈{_ 0 _,_ 1 _}_<sup>_k_</sup> , a nonce _N ∈{_ 0 _,_ 1 _}_<sup>_m_</sup> , associated data _A ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , a ciphertext _C ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , and a tag _T ∈{_ 0 _,_ 1 _}_<sup>_t_</sup> , and it outputs a message _M ∈{_ 0 _,_ 1 _}_<sup>_|C|_</sup> if the tag is correct, or a dedicated _⊥_ -sign otherwise. The two functions are required to satisfy 

In our work, the authenticated encryption scheme AE is based on an _n_ -bit permutation P, which is modeled as a random permutation: P _←−_ $ perm( _n_ ). The 

34 

security of AE against an adversary _A_ is defined as 

where the randomness of the oracles is taken over _K ←−{_ $ 0 _,_ 1 _}k_ , P _←−_ $ perm( _n_ ), and the function rand that for each input ( _N, A, M_ ) returns a random string of size _|M |_ + _t_ bits. The function _⊥_ returns the _⊥_ -sign for each query. 

We only consider _nonce-respecting_ adversaries: _A_ is not allowed to make two encryption queries for the same nonce. It is also not allowed to relay the output of the encryption oracle (enc _K_ in the real world and rand in the ideal world) to the decryption oracle (dec _K_ in the real world and _⊥_ in the ideal world). 

#### **B.1.2 Tweakable Block Ciphers** 

A tweakable block cipher E<sup>�</sup> is a function that gets as input a key _K ∈{_ 0 _,_ 1 _}_<sup>_k_</sup> , tweak _T ∈T_ ,<sup>2</sup> and message _M ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> , and it outputs a ciphertext _C ∈ {_ 0 _,_ 1 _}_<sup>_n_</sup> . The tweakable block cipher is required to be bijective for any fixed ( _K, T_ ). 

In our application, we will not make use of the inverse E<sup>�</sup><sup>_−_1</sup> . More importantly, for our authenticated encryption scheme it suffices to use a tweakable block cipher that is secure against adversaries that only have access to E<sup>�</sup> , and not to E<sup>�</sup><sup>_−_1</sup> . The tweakable block cipher considered in this work is based on an _n_ -bit permutation P, which is modeled as a random permutation: P _←−_ $ perm( _n_ ). The security of E<sup>�</sup> against an adversary _A_ is defined as 

where the randomness of the oracles is taken over _K ←−{_ $ 0 _,_ 1 _}k_ , P _←−_ $ perm( _n_ ), and _π_ � _←−_ $ perm( _T , n_ ). 

### **B.2 Simplified Masked Even-Mansour** 

The Elephant authenticated encryption family uses its underlying permutation in a “Masked Even-Mansour” (MEM) construction [49]: the input to and output of the permutation P are masked using an LFSR evaluated on the secret key. However, the tweakable block cipher used in our proposal is simpler than the original construction in two ways: (i) the tweak only consists of the exponents of the LFSRs and not the nonce and (ii) in our application, the tweakable block cipher is only evaluated in the forward direction. The changes are not huge, but they do allow for a simpler description, security analysis, and bound. We will refer to this scheme as SiM (Simplified MEM). For generality, we will keep the formalization for an arbitrary amount of LFSRs, even though we will only use it for two LFSRs. 

> 2In our application, the tweak space is of a specific form and cannot be conveniently expressed as a set of binary strings. 

35 

#### **B.2.1 Specification** 

Let _k, n, z ∈_ N. Let P _∈_ perm( _n_ ) be an _n_ -bit permutation, and let _ϕ_ 1 _, . . . , ϕz_ : _{_ 0 _,_ 1 _}_<sup>_n_</sup> _→{_ 0 _,_ 1 _}_<sup>_n_</sup> be _z_ LFSRs. Let _T ⊆_ N<sup>_z_</sup> be a finite tweak space. Define the function mask : _{_ 0 _,_ 1 _}_<sup>_k_</sup> _× T →{_ 0 _,_ 1 _}_<sup>_n_</sup> as follows: 

We define the tweakable block cipher SiM : _{_ 0 _,_ 1 _}_<sup>_k_</sup> _× T × {_ 0 _,_ 1 _}_<sup>_n_</sup> _→{_ 0 _,_ 1 _}_<sup>_n_</sup> as 

### **B.4 Implication for Dumbo, Jumbo, and Delirium** 

#### **B.4.1 Dumbo: 160-Bit Elephant** 

We will prove that the 160-bit LFSR defined by (3) has maximal length, and that the tweak space used in Elephant with this LFSR is 2<sup>_−n_</sup> -proper with respect to ( _ϕ_ 1 _, ϕ_ 2). 

**Proposition B.4.** _Let n_ = 160 _. Let ϕ_ 1 : _{_ 0 _,_ 1 _}_<sup>160</sup> _�→{_ 0 _,_ 1 _}_<sup>160</sup> _be the LSFR given in (3), and ϕ_ 2 = _ϕ_ 1 _⊕_ id _. The tweak space T_ = _T_ 1 _×T_ 2 = _{_ 0 _,_ 1 _, . . . ,_ 2<sup>154</sup> _}× {_ 0 _,_ 1 _,_ 2 _} is_ 2<sup>_−n_</sup> _-proper with respect to_ ( _ϕ_ 1 _, ϕ_ 2) _._ 

_Proof._ The proof is almost identical to [49, Lemma 4], with the main difference that a different discrete logarithm must be computed. Let _V_ be the 160 _×_ 160 matrix over F2 that represents _ϕ_ 1 of (3). As shown in [49, Lemma 3], _ϕ_<sup>_i_</sup> 1<sup>(</sup><sup>_L_) =</sup> _V_<sup>_i_</sup> _· L_ is 2<sup>_−n_</sup> -proper for _i ∈{_ 0 _, . . ._ 2<sup>_n_</sup> _−_ 2 _}_ if the minimal polynomial of _V_ is primitive and of degree _n_ . A quick computation using Sage [90] shows that this polynomial 

is irreducible and primitive. 

Next, let _ℓ_ = log _x_ ( _x_ + 1) in the field F2[ _x_ ] _/p_ ( _x_ ). We have to show that _ϕ_<sup>_b_</sup> 2<sup>_◦ϕ_</sup> 1<sup>_a_(</sup><sup>_L_)=(</sup><sup>_V_+</sup><sup>_I_)</sup><sup>_b · Va · L_=</sup><sup>_Vℓ·b · Va · L_isuniqueforanydistinctsetof</sup> tweaks. A simple Sage computation gives the following values for _ℓ_ and 2 _ℓ_ : 

_ℓ_ = 742800116542094474882643562714650758474536684889 _≈_ 2<sup>159</sup><sup>_._02</sup> _,_ 

2 _ℓ_ = 24098595753286031561602292713018497293140826803 _≈_ 2<sup>154</sup><sup>_._08</sup> _._ 

37 

If we consider that _b ∈{_ 0 _,_ 1 _,_ 2 _}_ divides the tweak space into three sets, the smallest difference is between the set with _b_ = 0 and the set corresponding to _b_ = 2, which is bigger than 2<sup>154</sup> . Hence, by ensuring that 0 _≤ a ≤_ 2<sup>154</sup> , we have that for any two distinct ( _a, b_ ) _,_ ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) _∈{_ 0 _,_ 1 _, . . . ,_ 2<sup>154</sup> _} × {_ 0 _,_ 1 _,_ 2 _}_ , _ϕ_<sup>_b_</sup> 2<sup>_◦ϕa_</sup> 1<sup>=</sup><sup>_ϕ_</sup> 2<sup>_b′◦ϕ_</sup> 1<sup>_a′_.</sup> 

Finally, using both of the above observations, one can easily observe that _T_ is 2<sup>_−n_</sup> -proper in light of Definition B.1. 

We directly obtain that Dumbo is secure in the random permutation model. 

**Corollary B.5.** _Let_ ( _k, m, n, t_ ) = (128 _,_ 96 _,_ 160 _,_ 64) _. Let T_ = _{_ 0 _,_ 1 _, . . . ,_ 2<sup>154</sup> _} × {_ 0 _,_ 1 _,_ 2 _}. Consider_ Dumbo _:_ Elephant = (enc _,_ dec) _of Section 2 based on_ Spongent _- π_ [160] _, modeled as a random_ 160 _-bit permutation, and on ϕ_ 1 : _{_ 0 _,_ 1 _}_<sup>160</sup> _→ {_ 0 _,_ 1 _}_<sup>160</sup> _of (3). For any adversary A making at most qe construction encryption queries, qd construction decryption queries, each query at most ℓ padded nonce and associated data and message blocks, and in total at most σ ≤_ 2<sup>158</sup> _padded nonce and associated data and message blocks, and p primitive queries,_ 

Recall that NIST’s call for lightweight authenticated encryption schemes [72] requested security up to an online complexity of around 2<sup>50</sup> bytes. By limiting the total online complexity _σ_ to 2<sup>50</sup> _/_ ( _n/_ 8) blocks, the bound of Corollary B.5 is at most 1 for _p ≤_ 2<sup>112</sup> . 

#### **B.4.2 Jumbo: 176-Bit Elephant** 

We will prove that the 176-bit LFSR defined by (4) has maximal length, and that the tweak space used in Elephant with this LFSR is 2<sup>_−n_</sup> -proper with respect to ( _ϕ_ 1 _, ϕ_ 2). 

**Proposition B.6.** _Let n_ = 176 _. Let ϕ_ 1 : _{_ 0 _,_ 1 _}_<sup>176</sup> _�→{_ 0 _,_ 1 _}_<sup>176</sup> _be the LSFR given in (4), and ϕ_ 2 = _ϕ_ 1 _⊕_ id _. The tweak space T_ = _T_ 1 _×T_ 2 = _{_ 0 _,_ 1 _, . . . ,_ 2<sup>173</sup> _}× {_ 0 _,_ 1 _,_ 2 _} is_ 2<sup>_−n_</sup> _-proper with respect to_ ( _ϕ_ 1 _, ϕ_ 2) _._ 

_Proof._ The proof is identical to that of Proposition B.4, with the difference that for the 176 _×_ 176 matrix _V_ that represents _ϕ_ 1 of (4), the corresponding polynomial 

is irreducible and primitive. The discrete logarithm _ℓ_ = log _x_ ( _x_ + 1) in the field F2[ _x_ ] _/p_ ( _x_ ) and its related 2 _ℓ_ are computed as 

_ℓ_ = 18881376151403786777481463432029450294100461562220699 _≈_ 2<sup>173</sup><sup>_._66</sup> _,_ 

- 2 _ℓ_ = 37762752302807573554962926864058900588200923124441398 _≈_ 2<sup>174</sup><sup>_._66</sup> _._ 

38 

Again, dividing the tweak space into 3 sets according to the value _b ∈{_ 0 _,_ 1 _,_ 2 _}_ , the smallest difference is between set _b_ = 0 and set _b_ = 1, or _b_ = 1 and _b_ = 2, which is bigger than 2<sup>173</sup> . Hence, by ensuring that 0 _≤ a ≤_ 2<sup>173</sup> , we have that for any two distinct ( _a, b_ ) _,_ ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) _∈{_ 0 _,_ 1 _, . . . ,_ 2<sup>173</sup> _}×{_ 0 _,_ 1 _,_ 2 _}_ , _ϕ_<sup>_b_</sup> 2<sup>_◦ϕa_</sup> 1<sup>=</sup><sup>_ϕ_</sup> 2<sup>_b′◦ϕ_</sup> 1<sup>_a′_.</sup> 

We directly obtain that Jumbo is secure in the random permutation model. 

**Corollary B.7.** _Let_ ( _k, m, n, t_ ) = (128 _,_ 96 _,_ 176 _,_ 64) _. Let T_ = _{_ 0 _,_ 1 _, . . . ,_ 2<sup>173</sup> _} × {_ 0 _,_ 1 _,_ 2 _}. Consider_ Jumbo _:_ Elephant = (enc _,_ dec) _of Section 2 based on_ Spongent _- π_ [176] _, modeled as a random_ 176 _-bit permutation, and on ϕ_ 1 : _{_ 0 _,_ 1 _}_<sup>176</sup> _→ {_ 0 _,_ 1 _}_<sup>176</sup> _of (4). For any adversary A making at most qe construction encryption queries, qd construction decryption queries, each query at most ℓ padded nonce and associated data and message blocks, and in total at most σ ≤_ 2<sup>174</sup> _padded nonce and associated data and message blocks, and p primitive queries,_ 

As before, limiting the total online complexity _σ_ to 2<sup>50</sup> _/_ ( _n/_ 8) blocks, the bound of Corollary B.7 is at most 1 for _p ≤_ 2<sup>127</sup> . 

#### **B.4.3 Delirium: 200-Bit Elephant** 

We will prove that the 200-bit LFSR defined by (5) has maximal length, and that the tweak space used in Elephant with this LFSR is 2<sup>_−n_</sup> -proper with respect to ( _ϕ_ 1 _, ϕ_ 2). 

**Proposition B.8.** _Let n_ = 200 _. Let ϕ_ 1 : _{_ 0 _,_ 1 _}_<sup>200</sup> _�→{_ 0 _,_ 1 _}_<sup>200</sup> _be the LSFR given in (5), and ϕ_ 2 = _ϕ_ 1 _⊕_ id _. The tweak space T_ = _T_ 1 _×T_ 2 = _{_ 0 _,_ 1 _, . . . ,_ 2<sup>197</sup> _}× {_ 0 _,_ 1 _,_ 2 _} is_ 2<sup>_−n_</sup> _-proper with respect to_ ( _ϕ_ 1 _, ϕ_ 2) _._ 

_Proof._ The proof is identical to that of Proposition B.4, with the difference that for the 200 _×_ 200 matrix _V_ that represents _ϕ_ 1 of (5), the corresponding polynomial 

is irreducible and primitive. The discrete log _ℓ_ = log _x_ ( _x_ + 1) in the field F2[ _x_ ] _/p_ ( _x_ ) and its related 2 _ℓ_ are computed as 

_ℓ_ = 692180606625676931900534627786122994390018641930530681719698 _≈_ 2<sup>198</sup><sup>_._78</sup> _,_ 

2 _ℓ_ = 1384361213251353863801069255572245988780037283861061363439396 _≈_ 2<sup>199</sup><sup>_._78</sup> _._ 

39 

Again, dividing the tweak space into 3 sets according to the value _b ∈{_ 0 _,_ 1 _,_ 2 _}_ , the smallest difference is between set _b_ = 2 and set _b_ = 0, which is bigger than 2<sup>197</sup> . Hence, by ensuring that 0 _≤ a ≤_ 2<sup>197</sup> , we have that for any two distinct ( _a, b_ ) _,_ ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) _∈{_ 0 _,_ 1 _, . . . ,_ 2<sup>197</sup> _} × {_ 0 _,_ 1 _,_ 2 _}_ , _ϕ_<sup>_b_</sup> 2<sup>_◦ϕa_</sup> 1<sup>=</sup><sup>_ϕ_</sup> 2<sup>_b′◦ϕ_</sup> 1<sup>_a′_.</sup> 

We directly obtain that Delirium is secure in the random permutation model. 

**Corollary B.9.** _Let_ ( _k, m, n, t_ ) = (128 _,_ 96 _,_ 200 _,_ 128) _. Let T_ = _{_ 0 _,_ 1 _, . . . ,_ 2<sup>197</sup> _}× {_ 0 _,_ 1 _,_ 2 _}. Consider_ Delirium _:_ Elephant = (enc _,_ dec) _of Section 2 based on_ Keccak _- f_ [200] _, modeled as a random_ 200 _-bit permutation, and on ϕ_ 1 : _{_ 0 _,_ 1 _}_<sup>200</sup> _→ {_ 0 _,_ 1 _}_<sup>200</sup> _of (5). For any adversary A making at most qe construction encryption queries, qd construction decryption queries, each query at most ℓ padded nonce and associated data and message blocks, and in total at most σ ≤_ 2<sup>198</sup> _padded nonce and associated data and message blocks, and p primitive queries,_ 

As before, limiting the total online complexity _σ_ to 2<sup>74</sup> _/_ ( _n/_ 8) blocks, the bound of Corollary B.9 is at most 1 for _p ≤_ 2<sup>127</sup> .