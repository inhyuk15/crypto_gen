# SCREAM Side-Channel Resistant Authenticated Encryption with Masking 

Vincent Grosso<sup>1</sup><sup>_∗_</sup> Ga¨etan Leurent<sup>2</sup> Fran¸cois-Xavier Standaert<sup>1</sup><sup>_†_</sup> Kerem Varici<sup>1</sup><sup>_‡_</sup> Anthony Journault<sup>1</sup><sup>_∗_</sup> Fran¸cois Durvaux<sup>1</sup><sup>_∗_</sup> Lubos Gaspar<sup>1</sup><sup>_‡_</sup> St´ephanie Kerckhof<sup>1</sup> 

- 1 ICTEAM/ELEN/Crypto Group, Universit´e catholique de Louvain, Belgium. 2 Inria, EPI Secret, Rocquencourt, France. 

Contact e-mail: `scream@uclouvain.be` 

Version 3 (Second Round Specifications), August 2015. 

##### **Abstract** 

This document defines the authenticated encryption (with associated data) algorithm SCREAM. It is based on Liskov et al.’s Tweakable Authenticated Encryption (TAE) mode with the new tweakable block cipher Scream. The main desirable features of SCREAM are: 

- A _simple_ and _regular_ design allowing excellent performances on a wide range of architectures, in particular if _masking_ is implemented _as a side-channel countermeasure_ ; 

- Inheriting from TAE, _security beyond the birthday bound_ , i.e. a 128-bit security guarantee with up to 2<sup>128</sup> bits of data processed with the same 128-bit key; 

- _Low overheads_ for the authentication mode (e.g. no extra cipher calls to generate masks); 

- _Fully parallelisable_ authenticated encryption with _minimal ciphertext length_ . 

#### **Updates from the first round candidate.** 

- Fixing mistakes in the authenticated encryption mode leading to simple forgeries (as pointed out by Wang Lei and Sim Siang Meng [18]). When no associated data is present, the mode is now identical to TAE as originally described by Liskov _et. al_ [19]. 

- Removal of the involutive family of authenticated encryption algorithm iSCREAM and its underlying block cipher iScream, which were not selected as second-round candidate. 

- Extension of the round constants from 8 to 16 bits (motivated by [14, 17]). 

- S-box with improved differential properties and algebraic degree (motivated by [4]). 

- ( _Editorial_ ) Clarification of the (primary, secondary, . . . ) recommended parameters. 

- ( _Editorial_ ) Removal of the performance evaluation (to be presented in a dedicated report). 

- ( _Editorial_ ) Description of the S-box and L-box properties, and rationale. 

> _∗_ PhD student funded by the ERC Project 280141 (acronym CRASH). 

> _†_ Associate researcher of the Belgian fund for scientific research (FNRS - F.R.S). 

> _‡_ Post-doctoral researcher funded by the ERC Project 280141 (acronym CRASH). 

1 

## **1 Design overview** 

The following cipher and encryption mode aim to allow implementations that are secure against _Side-Channel Attacks_ (SCAs) such as Differential Power Analysis (DPA) [16] and Electro-Magnetic Analysis (EMA) [9]. We believe they are important threats to the security of modern computing devices for an increasingly wide class of applications. In this context, numerous countermeasures have been introduced in the literature (a good survey can be found in [20]). Our designs will focus on SCA security based on masking (aka secret sharing) [5, 11] for three main reasons. First, it is a thoroughly investigated countermeasure with well established benefits (a security gain that can be exponential in the number of shares) and limitations (the requirement that the leakage of each share is sufficiently noisy and independent of the others) [7, 8, 28]. Second, it can take advantage of algorithms tailored for this purpose [10, 26]. Third, it can be implemented efficiently and securely both in software [29, 30] and hardware devices [22, 24]. As a result, and without neglecting the need to combine masking with other countermeasures to reach high physical security levels, we believe it is an important building block in the design of side-channel resistant implementations. 

Based on these premises, two important additional criteria are _implementation efficiency and design regularity/simplicity_ . The first one is motivated by the fact that more operations inevitably mean more leaking operations that may be exploited by a clever adversary (e.g. such as the analytical one in [33]). The second one derives from the observation that physically secure implementations are easier to obtain if computations are performed on well aligned data. For example, manipulating bits and bytes such as in the PRESENT block cipher [3] raises additional challenges for the developers (to guarantee that the bit manipulations do not leak more information than the byte ones). As a result, we also aim for implementation efficiency on various platforms, with performances close to the ones of the AES in an unprotected setting, and significantly improved when the masking countermeasure is activated. Concretely, this includes privileging highly parallel designs. 

As far as the block cipher used in our proposal is concerned, the LS-designs recently introduced at FSE 2014 appear as natural candidates to reach the previous goals [12] – we will take advantage of their general structure. As for the authenticated encryption mode, two main options are available. The first one is to directly exploit a block cipher based solution, for which the extra operations required for authentication are as linear (hence, easy to mask) as possible. Depending on the desired implementation and security properties (e.g. parallelism, need of decryption, misuse resistance), modes such as OCB [32], OTR [21], COPA [1] or COBRA [2] could be considered for this purpose. Yet, a drawback of such schemes is that they only guarantee birthday security. Alternatively, one can take advantage of the Tweakable Authenticated Encryption (TAE) proposed by Liskov et al. [19], which looses nothing in terms of its advantage of the underlying tweakable block cipher, hence can provide _beyond birthday security_ – we will opt for this second solution. 

Instantiating TAE requires a tweakable block cipher, which we achieve by extending the previously proposed block cipher Fantomas. Our main ingredient for this purpose is the addition of a lightweight tweak/key scheduling algorithm. In this respect, our choices were oriented by the conclusions in [15], where it was observed that allowing _round keys (and tweaks)_ to be _derived_ “ _on-the-fly_ ” both in encryption and decryption significantly improves hardware performances. 

Finally, since we care about physical security issues for which developers anyway have to pay attention to implementation aspects, we will not consider misuse resistance as a goal. For similar reasons, we will propose instances of our ciphers with and without security guarantees against related-key attacks – the later ones being the most relevant for our intended case studies. 

2 

In the following, we will denote our tweakable block cipher as Scream, and the TAE based on Scream as SCREAM. The designers have not hidden any weakness in any of these ciphers/modes. 

## **2 Security goals** 

Our security goals are summarized in Table 1. There is no secret message number. The public message number is a nonce. The cipher does not promise integrity or confidentiality if the legitimate key holder uses the same nonce to encrypt two different (plaintext,associated data) pairs under the same key. The numbers in the table correspond to key guesses to find the secret key for confidentiality, and to online forgery attempts for integrity. Any successful forgery or key recovery should be assumed to completely compromise confidentiality and integrity of all messages. 

Table 1: Summary of our security goals for SCREAM. 

||bits of security|
|---|---|
|Confdentiality of the plaintext|128|
|Integrity of the plaintext|128|
|Integrity of the associated data|128|
|Integrity of the public message number|128|
|Side-channel resistance|masking|
|Related-key security|optional|
|Misuse resistance|no|

The lower part of the table contains qualitative security statements. Side-channel resistant implementations are expected to be achieved with masking. Related-key security is optional and can be obtained with an increased number of rounds. Misuse resistance is not claimed. 

## **3 Specifications** 

### **3.1 Tweakable LS-designs** 

Scream is based on a variant of the LS-designs introduced in [12] that we will denote as Tweakable LS-designs (TLS-designs). They essentially update a _n_ -bit state _x_ by iterating _Ns_ steps, each of them made of _Nr_ rounds. The state is structured as a _l × s_ matrix, such that _x_ [ _i, ⋆_ ] represents a row and _x_ [ _⋆, j_ ] represents a column. The first row contains state bits 0 to _l −_ 1, the second row contains state bits _l_ to 2 _l −_ 1, . . . In the following, the number of rounds per step will be fixed to _Nr_ = 2. By contrast, the number of steps will vary and will serve as a parameter to adapt the security margins in Section 5. One significant advantage of TLS-designs is their simplicity: they can be described in a couple of lines, as illustrated in Algorithm 1. In this algorithm, _P_ denotes the plaintext, _TK_ a combination of the master key _K_ and tweak _T_ that we will call tweakey. Finally, S and L are the _s_ -bit S-box and _l_ -bit L-box that are used in our TLS-design. 

### **3.2 The tweakable block cipher Scream** 

Scream is an _n_ =128-bit cipher with _s_ =8-bit S-boxes and _l_ =16-bit L-boxes. Specifying this cipher requires to define these components, together with the round constants. The binary representation of the L-box and the bitslice representation of the S-box are given in Figure 1 and Algorithm 2. 

3 

**Algorithm 1** TLS-design with _l_ -bit L-box and _s_ -bit S-box <u>(</u> _n_ = _l · s_ <u>)</u> _x ← P ⊕ TK_ (0); _▷x is a l × s bits matrix_ **for** 0 _< σ ≤ Ns_ **do for** 0 _< ρ ≤ Nr_ **do** _r_ = 2 _·_ ( _σ −_ 1) + _ρ_ ; _▷ Round index_ **for** 0 _≤ j < l_ **do** _▷ S-box Layer x_ [ _⋆, j_ ] = S[ _x_ [ _⋆, j_ ]]; **end for** _x ← x ⊕ C_ ( _r_ ); _▷ Constant addition_ **for** 0 _≤ i < s_ **do** _▷ L-box Layer x_ [ _i, ⋆_ ] = L[ _x_ [ _i, ⋆_ ]]; **end for end for** _x ← x ⊕ TK_ ( _σ_ ); _▷ Tweakey addition_ **end for return** _x_ 

Further descriptions are given in Appendix A, and the round constants are in Appendix B. Following the conventions in [12], the S-box has algebraic degree 6 (vs. 5 for our first-round candidate), differential probability 2<sup>_−_5</sup> (vs. 2<sup>_−_4</sup> for our first-round candidate), and linear probability 2<sup>_−_2</sup> (as our first-round candidate). It can be implemented with only 39 gates, including 12 non-linear gates (vs. 36 and 11 for our first-round candidate). The (unchanged) L-box has branch number 8. 

|<br>0|0|1|1|1|0|1|0|0|0|0|1|1|1|0|0<br>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|<br><br>1|0|0|1|0|1|0|1|0|1|0|0|1|0|1|0<br><br><br>|
|<br><br><br>1|1|0|0|1|1|0|1|1|1|0|1|1|1|1|0<br><br><br>|
|<br><br><br>1|0|0|0|0|0|1|1|0|1|1|0|1|0|0|1<br><br><br>|
|<br><br><br>1|0|1|1|0|1|1|0|1|1|1|0|1|0|1|1<br><br><br>|
|<br><br><br>0|0|0|0|0|1|1|1|0|1|0|1|1|1|0|0<br><br><br>|
|<br><br><br>0|0|1|0|0|1|0|0|1|0|1|0|0|1|1|1<br><br><br>|
|<br><br>1|0|1|0|0|1|0|1|0|1|1|1|1|1|1|1<br><br><br>|
|<br><br>1|1|0|1|0|0|1|0|0|1|1|0|0|0|1|0<br><br><br>|
|<br><br>1|1|1|1|0|1|0|1|1|0|0|0|1|1|1|1<br><br><br>|
|<br><br>1|1|0|0|1|1|0|0|1|0|0|0|0|1|0|1<br><br><br>|
|<br><br>0|0|1|0|1|1|1|0|1|1|1|1|1|1|1|0<br><br><br>|
|<br><br><br>0|1|0|0|1|0|0|0|1|1|1|0|0|1|1|0<br><br><br><br>|
|<br><br><br>1|1|1|1|0|1|1|0|0|1|0|1|1|1|1|0<br><br><br><br>|
|<br><br>1|1|0|1|1|0|0|0|0|0|0|0|1|1|1|0<br><br>|
|<br>1|0|0|0|1|1|0|1|0|1|0|1|0|0|0|1<br>|

Figure 1: Scream L-box 

4 

**Algorithm 2** Scream S-box and inverse S-box, bitslice implementation. Input and output is in <u>(</u> _W_ 0 _, . . . , W_ 7) <u>(8</u> 16-bit words) 

**function** Sbox( _W_ 0 _, . . . , W_ 7) **function** InvSbox( _W_ 0 _, . . . , W_ 7) _▷ Feistel round 1 ▷ Feistel round 1 t_ 0 = ( _W_ 1 _∧ W_ 2) _⊕ W_ 0 _t_ 0 = _¬_ (( _W_ 1 _∧ W_ 2) _⊕ W_ 0) _t_ 1 = ( _W_ 1 _⊕ W_ 3) _t_ 1 = ( _W_ 1 _⊕ W_ 3) _t_ 2 = _W_ 2 _⊕ t_ 0 _t_ 2 = _W_ 2 _⊕ t_ 0 _W_ 4 = _W_ 4 _⊕_ (( _W_ 3 _⊕ t_ 2) _∧_ ( _W_ 2 _⊕ t_ 1)) _W_ 4 = _W_ 4 _⊕_ (( _W_ 3 _⊕ t_ 2) _∧_ ( _W_ 2 _⊕ t_ 1)) _W_ 5 = _W_ 5 _⊕ t_ 2 _W_ 5 = _W_ 5 _⊕ t_ 2 _W_ 6 = _W_ 6 _⊕_ ( _W_ 3 _∧ t_ 0) _W_ 6 = _W_ 6 _⊕_ ( _W_ 3 _∧ t_ 0) _W_ 7 = _W_ 7 _⊕_ ( _t_ 1 _∧ t_ 2) _W_ 7 = _W_ 7 _⊕_ ( _t_ 1 _∧ t_ 2) _▷ Feistel round 2 ▷ Feistel round 2 t_ 0 = ( _W_ 4 _∧ W_ 5) _⊕ W_ 6 _t_ 0 = ( _W_ 4 _∧ W_ 5) _⊕ W_ 6 _t_ 1 = ( _W_ 5 _∨ W_ 6) _⊕ W_ 7 _t_ 1 = ( _W_ 5 _∨ W_ 6) _⊕ W_ 7 _t_ 2 = ( _W_ 7 _∧ t_ 0) _⊕ W_ 4 _t_ 2 = ( _W_ 7 _∧ t_ 0) _⊕ W_ 4 _t_ 3 = ( _W_ 4 _∧ t_ 1) _⊕ W_ 5 _t_ 3 = ( _W_ 4 _∧ t_ 1) _⊕ W_ 5 _W_ 0 = _W_ 0 _⊕ t_ 0 _W_ 0 = _W_ 0 _⊕ t_ 0 _W_ 2 = _W_ 2 _⊕ t_ 1 _W_ 2 = _W_ 2 _⊕ t_ 1 _W_ 1 = _W_ 1 _⊕ t_ 2 _W_ 1 = _W_ 1 _⊕ t_ 2 _W_ 3 = _W_ 3 _⊕ t_ 3 _W_ 3 = _W_ 3 _⊕ t_ 3 _▷ Feistel round 3 ▷ Feistel round 3 t_ 0 = _¬_ (( _W_ 1 _∧ W_ 2) _⊕ W_ 0) _t_ 0 = ( _W_ 1 _∧ W_ 2) _⊕ W_ 0 _t_ 1 = ( _W_ 1 _⊕ W_ 3) _t_ 1 = ( _W_ 1 _⊕ W_ 3) _t_ 2 = _W_ 2 _⊕ t_ 0 _t_ 2 = _W_ 2 _⊕ t_ 0 _W_ 4 = _W_ 4 _⊕_ (( _W_ 3 _⊕ t_ 2) _∧_ ( _W_ 2 _⊕ t_ 1)) _W_ 4 = _W_ 4 _⊕_ (( _W_ 3 _⊕ t_ 2) _∧_ ( _W_ 2 _⊕ t_ 1)) _W_ 5 = _W_ 5 _⊕ t_ 2 _W_ 5 = _W_ 5 _⊕ t_ 2 _W_ 6 = _W_ 6 _⊕_ ( _W_ 3 _∧ t_ 0) _W_ 6 = _W_ 6 _⊕_ ( _W_ 3 _∧ t_ 0) _W_ 7 = _W_ 7 _⊕_ ( _t_ 1 _∧ t_ 2) _W_ 7 = _W_ 7 _⊕_ ( _t_ 1 _∧ t_ 2) **end function end function** 

5 

Finally, Scream has a light tweakey scheduling algorithm that we now detail. It takes the 128-bit key _K_ and the 128-bit tweak _T_ as input. The tweak is divided into 64-bit halves: _T_ = _t_ 0 _∥ t_ 1. Then, three different tweakeys are used every three steps as follows: 

The tweakeys can also be computed on-the-fly using a simple linear function _φ_ , corresponding to multiplication by a primitive element in _GF_ (4) (such that _φ_<sup>2</sup> ( _x_ ) = _φ_ ( _x_ ) _⊕ x_ , and _φ_<sup>3</sup> ( _x_ ) = _x_ ): 

### **3.3 The encryption mode SCREAM** 

We use the tweakable block cipher Scream in the TAE mode proposed in [19]. A plaintext ( _P_ 0 _, · · · , Pm−_ 1) is encrypted using a nonce (next denoted as _N_ ) – the algorithm produces a ciphertext ( _C_ 0 _, · · · , Cm−_ 1) and a tag _T_ . Blocks of associated data ( _A_ 0 _, · · · , Aq−_ 1) can optionally be authenticated with the message, without being encrypted. During the decryption process, the ciphertext values, tag and associated data are used to recover the plaintext. If the tag is incorrect, the algorithm returns a null output _⊥_ . The nonce is supplied by the user, and every message encrypted with a given key must use a different value for _N_ . The nonce bytesize _nb_ can be chosen by the user between 1 and 15 bytes (the recommended value is 11 bytes), and every message encrypted with a given key must use the same nonce size. The length of the associated data and the length of the message are limited to 2<sup>124</sup><sup>_−_8</sup><sup>_nb_</sup> bytes (which corresponds to 2<sup>120</sup><sup>_−_8</sup><sup>_nb_</sup> blocks). 

There are three main steps in the mode of operation. First, the associated data is processed by dividing it into 128-bit blocks. Each block is encrypted through the tweakable block cipher and the output values are XORed in order to get the main output of this step (denoted as auth.), as 

6 

illustrated in Figure 2. If the last block is incomplete, it is padded with a single `1` bit and the rest of the block is filled with zeroes (we denote this padding as ( `10`<sup>_∗_</sup> ) := ( `1000` _. . ._ `0` )). If the last block is a full block, it is not padded but the encryption uses a different tweak. 

<!-- Start of picture text -->
A 0 A 1 Aq− 1<br>˜ ˜ ˜<br>T 0 ′ EK T 1 ′ EK . . . T∗ ′ EK<br>� . . . � auth.<br><!-- End of picture text -->

Figure 2: TAE: associated data processing. 

Second, plaintext values are encrypted using the tweakable block cipher in order to produce the ciphertext values, as illustrated in Figure 3. If the last block is a partial block, its bitlength is encrypted to generate a mask, which it is then truncated to the partial block size and XORed with the partial plaintext block. Therefore, the ciphertext length is the same as the plaintext length. 

<!-- Start of picture text -->
Pm− 1<br>P 0 P 1 Pm− 2 length<br>˜ ˜ ˜ ˜<br>T 0 EK T 1 EK . . . Tm− 2 EK T ∗ EK<br>C 0 C 1 Cm− 2 �<br>Cm− 1<br><!-- End of picture text -->

Figure 3: TAE: encryption of the plaintext blocks. 

Finally, the tag is generated as represented in Figure 4. That is, the checksum (i.e. the XOR of all plaintext blocks) is first encrypted, and the output of this encryption is then XORed with the output of the associated data processing step (auth.) in order to get the tag. 

<!-- Start of picture text -->
checksum<br>T Σ E ˜ K<br>� auth.<br>tag<br><!-- End of picture text -->

Figure 4: TAE: tag generation. 

For the security of the TAE mode, all the calls to the tweakable block cipher must use distinct values of the tweak. In addition, we use some special values for domain separation and we define the tweaks depending on the context. In general, we use tweaks of the form ( _N ∥ c ∥_ control byte), where _N_ is the nonce and _c_ is a block counter. The control byte and counter are then specified as follows (with _m_ the number of message blocks, and _q_ the number of associated data blocks): 

7 

**Plaintext encryption.** _c_ is a 120 _−_ 8 _nb_ -bit block counter. 

with _|P |_ a 127 _−_ 8 _nb_ -bit integer. Alternatively, this tweak can be written with the block counter _c_ , and the seven low order bits of _|P |_ as control bits (i.e. _ℓ_ = _|P |_ mod 128): 

Our version of the TAE mode is specified in Algorithm 3. 

**Algorithm 3** Tweakable Authenticated Encryption with Associated Data 

**function** TAE( _N_ , _A_ , _P_ ) _▷ Initialisation auth. ←_ 0; _▷ TAE: Encryption C ←_ ∅; **for** 0 _≤ i < ⌊|P |/_ 128 _⌋_ **do** Σ _←_ 0; _C ← C ∥ E_<sup>˜</sup> ( _Ti, Pi_ ); _▷ TAE: associated data_ Σ _←_ Σ _⊕ Pi_ ; **if** _|A| >_ 0 **then end for for** 0 _≤ i < ⌊_ ( _|A| −_ 1) _/_ 128 _⌋_ **do if** _|P |_ ∤ 128 **then** _auth. ← auth. ⊕ E_<sup>˜</sup> ( _Ti_<sup>_′, Ai_);</sup> _C ← C ∥ Trunc_ ( _E_<sup>˜</sup> ( _T∗, |Pi_ +1 _|_ )) _⊕ Pi_ +1; **end for** Σ _←_ Σ _⊕_ ( _Pi_ +1 _∥_ `0`<sup>_∗_</sup> ); **if** _|A|_ ∤ 128 **then end if** _Ai_ +1 _← Ai_ +1 _∥_ 10<sup>_∗_</sup> ; _auth. ← auth. ⊕ E_<sup>˜</sup> ( _T∗_<sup>_′, Ai_+1);</sup> _▷ TAE: Tag generation_ **else** _tag ← E_<sup>˜</sup> ( _T_ Σ _,_ Σ) _⊕ auth._ ; _auth. ← auth. ⊕ E_<sup>˜</sup> ( _T∗_<sup>_′, Ai_+1);</sup> **return** _C, tag_ **end if end function end if** 

### **5.1 The tweakable block cipher Scream** 

Scream is a tweakable block cipher derived from the LS-cipher Fantomas. The security analysis in [12] shows that such a design has good properties and follows the wide-trail strategy, which allows deriving simple bounds on the probability of differential and linear trails. However, the security notion for a tweakable block cipher is much stronger than for a standard block cipher. Indeed, the family of keyed permutations indexed by the tweak must be secure against adversaries who can query every member of the family. In particular, she can perform a differential attack between two members of the family with a different tweak value. In the following we focus our attention on this scenario, and evaluate the best differential trails in this context. This analysis is mostly dependent on the tweakey scheduling algorithms used in Scream. In Fantomas, the lack of key scheduling combined with key additions every round allows simple related-key trails with a single active S-box per round. In Scream, we avoid this weakness by using a construction similar to the one of LED [13]: the tweakey is used every second round, and we argue that related-tweak trails over _σ_ steps must have at least _⌊σ/_ 2 _⌋_ active steps, where each active step has at least 8 active S- boxes. More precisely, the tweakey scheduling of Scream is designed to allow improved bounds in several scenarios, by mixing the bits corresponding to the same S-box. It allows to reuse some of the analysis for fixed tweak/key in a context with differences in the tweak/key. In particular, the L-box has been selected in order to avoid simple iterative trails with a low number of active S-boxes. Our results are listed in Table 2, and the detailed analysis is available in Appendix C. 

|Setting|Steps:|1<br>2|3|4|5|6|7|8|9|
|---|---|---|---|---|---|---|---|---|---|
|Single-key, fxed-tweak|Scream|8 20|30|40||||||
|Single-key, chosen-tweaks|Scream|0<br>8|14|20|28|35||||
|Related-keys, chosen-tweaks|Scream|0<br>0|8|14|14|22|28|28|36|

Table 2: Minimum number of active S-boxes for Scream. 

Since differential trails with 26 active S-boxes or more have a probability below 2<sup>_−_128</sup> , the maximum number of steps that can be reached with a related-tweak trail is 4 with a single key, and 6 with related keys. Linear trails can have up to 32 active S-boxes, but there is no simple way to leverage different tweaks for such trails, as done in a related-key differential attack. 

### **5.2 The encryption modes SCREAM** 

The TAE encryption mode provides a tight security reduction to the security of its underlying tweakable block ciphers that we assume to have 128-bit security (see [19] for the details). 

### **5.3 Suggested and recommended parameters** 

Based on our previous security analysis, we suggest the parameters listed below, corresponding to lightweight security, single-key security and related-key security. For each type of security, we provide two sets of (tight and safe) parameters. Some of these suggestions being redundant, this makes a total of four sets of parameters for SCREAM (with 6, 8, 10 and 12 steps). 

9 

- **Lightweight security.** 80-bit security, with a protocol avoiding related keys _Tight parameters_ : 6 steps, _Safe parameters_ : 8 steps. 

- **Single-key security.** 128-bit security, with a protocol avoiding related keys _Tight parameters_ : 8 steps, _Safe parameters_ : 10 steps. 

- **Related-key security.** 128-bit security, with possible related keys _Tight parameters_ : 10 steps, _Safe parameters_ : 12 steps. 

Our recommended parameters are the safe ones with single-key or related-key security. Lightweight parameters are given for possible comparisons with other schemes. Tight parameters define interesting targets for further cryptanalysis efforts and could lead to additional performance gains. 

More precisely, we order our recommended sets of parameters as follows: 

- First set of recommended parameters: SCREAM with 10 steps, single-key security. 

- Second set of recommended parameters: SCREAM with 12 steps, related-key security. 

## **A Scream components’ descriptions** 

### **A.1 Scream S-box** 

#### **A.1.1 Table representation** 

|`0`|`1`|`2`|`3`|`4`|`5`|`6`|`7`|`8`|`9`|`A`|`B`|`C`|`D`|`E`|`F`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|`00`<br>`20 `|`8D `|`B2 `|`DA `|`33 `|`35 `|`A6 `|`FF `|`7A `|`52 `|`6A `|`C6 `|`A4 `|`A8 `|`51 `|`23`|
|`10`<br>`A2 `|`96 `|`30 `|`AB `|`C8 `|`17 `|`14 `|`9E `|`E8 `|`F3 `|`F8 `|`DD `|`85 `|`E2 `|`4B `|`D8`|
|`20`<br>`6C `|`01 `|`0E `|`3D `|`B6 `|`39 `|`4A `|`83 `|`6F `|`AA `|`86 `|`6E `|`68 `|`40 `|`98 `|`5F`|
|`30`<br>`37 `|`13 `|`05 `|`87 `|`04 `|`82 `|`31 `|`89 `|`24 `|`38 `|`9D `|`54 `|`22 `|`7B `|`63 `|`BD`|
|`40`<br>`75 `|`2C `|`47 `|`E9 `|`C2 `|`60 `|`43 `|`AC `|`57 `|`A1 `|`1F `|`27 `|`E7 `|`AD `|`5C `|`D2`|
|`50`<br>`0F `|`77 `|`FD `|`08 `|`79 `|`3A `|`49 `|`5D `|`ED `|`90 `|`65 `|`7C `|`56 `|`4F `|`2E `|`69`|
|`60`<br>`CD `|`44 `|`3F `|`62 `|`5B `|`88 `|`6B `|`C4 `|`5E `|`2D `|`67 `|`0B `|`9F `|`21 `|`29 `|`2A`|
|`70`<br>`D6 `|`7E `|`74 `|`E0 `|`41 `|`73 `|`50 `|`76 `|`55 `|`97 `|`3C `|`09 `|`7D `|`5A `|`92 `|`70`|
|`80`<br>`84 `|`B9 `|`26 `|`34 `|`1D `|`81 `|`32 `|`2B `|`36 `|`64 `|`AE `|`C0 `|`00 `|`EE `|`8F `|`A7`|
|`90`<br>`BE `|`58 `|`DC `|`7F `|`EC `|`9B `|`78 `|`10 `|`CC `|`2F `|`94 `|`F1 `|`3B `|`9C `|`6D `|`16`|
|`A0`<br>`48 `|`B5 `|`CA `|`11 `|`FA `|`0D `|`8E `|`07 `|`B1 `|`0C `|`12 `|`28 `|`4C `|`46 `|`F4 `|`8B`|
|`B0`<br>`A9 `|`CF `|`BB `|`03 `|`A0 `|`FC `|`EF `|`25 `|`80 `|`F6 `|`B3 `|`BA `|`3E `|`F7 `|`D5 `|`91`|
|`C0`<br>`C3 `|`8A `|`C1 `|`45 `|`DE `|`66 `|`F5 `|`0A `|`C9 `|`15 `|`D9 `|`A3 `|`61 `|`99 `|`B0 `|`E4`|
|`D0`<br>`D1 `|`FB `|`D3 `|`4E `|`BF `|`D4 `|`D7 `|`71 `|`CB `|`1E `|`DB `|`02 `|`1A `|`93 `|`EA `|`C5`|
|`E0`<br>`EB `|`72 `|`F9 `|`1C `|`E5 `|`CE `|`4D `|`F2 `|`42 `|`19 `|`E1 `|`DF `|`59 `|`95 `|`B7 `|`8C`|
|`F0`<br>`9A `|`F0 `|`18 `|`E6 `|`C7 `|`AF `|`BC `|`B8 `|`E3 `|`1B `|`D0 `|`A5 `|`53 `|`B4 `|`06 `|`FE`|

Table 3: Scream S-box, table representation. 

#### **A.1.2 Algebraic Normal Form** 

_y_ 0 = _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 + _x_ 0 _x_ 2 _x_ 3 + _x_ 1 _x_ 2 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 0 _x_ 2 _x_ 5 + _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 3 _x_ 5 + _x_ 1 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 + _x_ 0 _x_ 2 + _x_ 1 _x_ 2 + _x_ 0 _x_ 3 + _x_ 2 _x_ 3 + _x_ 0 _x_ 4 + _x_ 2 _x_ 4 + _x_ 2 _x_ 5 + _x_ 3 _x_ 5 + _x_ 4 _x_ 5 + _x_ 0 + _x_ 2 + _x_ 6 

_y_ 1 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 4 _x_ 5 + _x_ 0 _x_ 3 _x_ 4 _x_ 5 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 7 + _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 5 _x_ 7 + _x_ 0 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 0 _x_ 3 _x_ 5 _x_ 7 + _x_ 1 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 + _x_ 0 _x_ 2 _x_ 3 + _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 4 + _x_ 0 _x_ 3 _x_ 4 + _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 0 _x_ 1 _x_ 6 + _x_ 0 _x_ 3 _x_ 6 + _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 0 _x_ 2 _x_ 7 + _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 4 _x_ 7 + _x_ 2 _x_ 4 _x_ 7 + _x_ 2 _x_ 5 _x_ 7 + _x_ 3 _x_ 5 _x_ 7 + _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 2 + _x_ 1 _x_ 2 + _x_ 1 _x_ 3 + _x_ 2 _x_ 7 + _x_ 6 _x_ 7 + _x_ 1 + _x_ 2 + _x_ 3 + _x_ 4 

_y_ 2 = _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 + _x_ 0 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 6 + _x_ 0 _x_ 1 + _x_ 1 _x_ 2 + _x_ 0 _x_ 3 + _x_ 2 _x_ 3 + _x_ 0 _x_ 6 + _x_ 2 _x_ 6 + _x_ 5 _x_ 6 + _x_ 0 + _x_ 5 + _x_ 6 + _x_ 7 

_y_ 3 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 6 + _x_ 0 _x_ 1 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 + _x_ 0 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 4 + _x_ 1 _x_ 2 _x_ 4 + _x_ 0 _x_ 3 _x_ 4 + _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 0 _x_ 2 _x_ 5 + _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 3 _x_ 5 + _x_ 1 _x_ 3 _x_ 5 + _x_ 0 _x_ 3 _x_ 6 + _x_ 1 _x_ 3 _x_ 6 + _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 4 _x_ 6 + _x_ 2 _x_ 4 _x_ 6 + _x_ 2 _x_ 5 _x_ 6 + _x_ 3 _x_ 5 _x_ 6 + _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 0 _x_ 2 _x_ 7 + _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 1 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 + _x_ 2 _x_ 3 + _x_ 0 _x_ 4 + _x_ 2 _x_ 4 + _x_ 2 _x_ 5 + _x_ 3 _x_ 5 + _x_ 4 _x_ 5 + _x_ 3 _x_ 6 + _x_ 4 _x_ 6 + _x_ 2 _x_ 7 + _x_ 3 _x_ 7 + _x_ 4 _x_ 7 + _x_ 0 + _x_ 3 + _x_ 5 

_y_ 4 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 4 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 6 + _x_ 0 _x_ 1 _x_ 5 _x_ 6 + _x_ 0 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 4 _x_ 5 _x_ 6 + _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 3 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 4 _x_ 7 + _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 5 _x_ 7 + _x_ 1 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 4 _x_ 5 _x_ 7 + _x_ 3 _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 6 _x_ 7 + _x_ 1 _x_ 2 _x_ 6 _x_ 7 + 

14 

_x_ 0 _x_ 3 _x_ 6 _x_ 7 + _x_ 1 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 5 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 + _x_ 0 _x_ 1 _x_ 5 + _x_ 1 _x_ 2 _x_ 5 + _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 4 _x_ 5 + _x_ 1 _x_ 4 _x_ 5 + _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 6 + _x_ 0 _x_ 2 _x_ 6 + _x_ 1 _x_ 2 _x_ 6 + _x_ 1 _x_ 3 _x_ 6 + _x_ 0 _x_ 4 _x_ 6 + _x_ 2 _x_ 4 _x_ 6 + _x_ 3 _x_ 4 _x_ 6 + _x_ 0 _x_ 5 _x_ 6 + _x_ 1 _x_ 5 _x_ 6 + _x_ 4 _x_ 5 _x_ 6 + _x_ 1 _x_ 3 _x_ 7 + _x_ 2 _x_ 4 _x_ 7 + _x_ 3 _x_ 4 _x_ 7 + _x_ 1 _x_ 5 _x_ 7 + _x_ 3 _x_ 5 _x_ 7 + _x_ 4 _x_ 6 _x_ 7 + _x_ 5 _x_ 6 _x_ 7 + _x_ 0 _x_ 4 + _x_ 2 _x_ 4 + _x_ 3 _x_ 4 + _x_ 1 _x_ 5 + _x_ 3 _x_ 5 + _x_ 4 _x_ 5 + _x_ 0 _x_ 6 + _x_ 3 _x_ 6 + _x_ 4 _x_ 6 + _x_ 5 _x_ 6 + _x_ 0 _x_ 7 + _x_ 1 _x_ 7 + _x_ 4 _x_ 7 + _x_ 6 _x_ 7 + _x_ 1 + _x_ 2 + _x_ 3 + _x_ 6 

_y_ 5 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 3 _x_ 4 _x_ 5 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 6 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 6 + _x_ 0 _x_ 1 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 4 _x_ 7 + _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 4 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 4 + _x_ 0 _x_ 3 _x_ 4 + _x_ 0 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 6 + _x_ 1 _x_ 2 _x_ 6 + _x_ 0 _x_ 3 _x_ 6 + _x_ 1 _x_ 3 _x_ 6 + _x_ 0 _x_ 4 _x_ 6 + _x_ 2 _x_ 4 _x_ 6 + _x_ 1 _x_ 5 _x_ 6 + _x_ 2 _x_ 5 _x_ 6 + _x_ 3 _x_ 5 _x_ 6 + _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 1 _x_ 3 _x_ 7 + _x_ 2 _x_ 3 _x_ 7 + _x_ 2 _x_ 4 _x_ 7 + _x_ 2 _x_ 5 _x_ 7 + _x_ 2 _x_ 6 _x_ 7+ _x_ 0 _x_ 2+ _x_ 2 _x_ 4+ _x_ 1 _x_ 5+ _x_ 0 _x_ 6+ _x_ 1 _x_ 6+ _x_ 2 _x_ 6+ _x_ 3 _x_ 6+ _x_ 4 _x_ 6+ _x_ 5 _x_ 6+ _x_ 1 _x_ 7+ _x_ 3 _x_ 7+ _x_ 4 _x_ 7+ _x_ 0+ _x_ 7+1 

_y_ 6 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 2 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 3 _x_ 5 _x_ 6 + _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 4 _x_ 5 _x_ 6 + _x_ 1 _x_ 4 _x_ 5 _x_ 6 + _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 3 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 3 _x_ 4 _x_ 7 + _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 6 _x_ 7 + _x_ 0 _x_ 3 _x_ 6 _x_ 7 + _x_ 1 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 5 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 + _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 4 + _x_ 0 _x_ 2 _x_ 4 + _x_ 1 _x_ 2 _x_ 4 + _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 2 _x_ 5 + _x_ 0 _x_ 4 _x_ 5 + _x_ 1 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 6 + _x_ 1 _x_ 3 _x_ 6 + _x_ 2 _x_ 3 _x_ 6 + _x_ 1 _x_ 4 _x_ 6 + _x_ 3 _x_ 4 _x_ 6 + _x_ 2 _x_ 5 _x_ 6 + _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 4 _x_ 7 + _x_ 1 _x_ 4 _x_ 7 + _x_ 3 _x_ 4 _x_ 7 + _x_ 1 _x_ 5 _x_ 7 + _x_ 2 _x_ 5 _x_ 7 + _x_ 3 _x_ 6 _x_ 7 + _x_ 4 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 + _x_ 2 _x_ 3 + _x_ 2 _x_ 4 + _x_ 0 _x_ 5 + _x_ 1 _x_ 5 + _x_ 2 _x_ 5 + _x_ 3 _x_ 5 + _x_ 4 _x_ 5 + _x_ 0 _x_ 6 + _x_ 3 _x_ 6 + _x_ 4 _x_ 6 + _x_ 5 _x_ 6 + _x_ 3 _x_ 7 + _x_ 3 + _x_ 5 + _x_ 6 

_y_ 7 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 6 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 2 _x_ 4 _x_ 6 + _x_ 0 _x_ 1 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 4 _x_ 5 _x_ 6 + _x_ 1 _x_ 4 _x_ 5 _x_ 6 + _x_ 3 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 3 _x_ 4 _x_ 7 + _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 5 _x_ 7 + _x_ 0 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 4 _x_ 5 _x_ 7 + _x_ 2 _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 6 _x_ 7 + _x_ 0 _x_ 3 _x_ 6 _x_ 7 + _x_ 1 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 5 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 + _x_ 0 _x_ 2 _x_ 3 + _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 3 _x_ 4 + _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 4 _x_ 5 + _x_ 2 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 6 + _x_ 1 _x_ 3 _x_ 6 + _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 4 _x_ 6 + _x_ 1 _x_ 4 _x_ 6 + _x_ 2 _x_ 4 _x_ 6 + _x_ 3 _x_ 4 _x_ 6 + _x_ 2 _x_ 5 _x_ 6 + _x_ 3 _x_ 5 _x_ 6 + _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 1 _x_ 3 _x_ 7 + _x_ 1 _x_ 4 _x_ 7 + _x_ 2 _x_ 4 _x_ 7 + _x_ 3 _x_ 4 _x_ 7 + _x_ 1 _x_ 5 _x_ 7 + _x_ 2 _x_ 5 _x_ 7 + _x_ 0 _x_ 6 _x_ 7 + _x_ 3 _x_ 6 _x_ 7 + _x_ 4 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 + _x_ 0 _x_ 2 + _x_ 0 _x_ 3 + _x_ 1 _x_ 3 + _x_ 2 _x_ 3 + _x_ 0 _x_ 4 + _x_ 0 _x_ 5 + _x_ 1 _x_ 5 + _x_ 2 _x_ 5 + _x_ 4 _x_ 5 + _x_ 0 _x_ 6 + _x_ 1 _x_ 6 + _x_ 2 _x_ 6 + _x_ 4 _x_ 6 + _x_ 5 _x_ 6 + _x_ 0 _x_ 7 + _x_ 2 _x_ 7 + _x_ 3 _x_ 7 + _x_ 4 _x_ 7 + _x_ 5 _x_ 7 + _x_ 0 + _x_ 1 + _x_ 4 + _x_ 7 

15 

### **A.2 Inverse Scream S-box** 

#### **A.2.1 Table representation** 

|`0`|`1`|`2`|`3`|`4`|`5`|`6`|`7`|`8`|`9`|`A`|`B`|`C`|`D`|`E`|`F`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|`00`<br>`8C `|`21 `|`DB `|`B3 `|`34 `|`32 `|`FE `|`A7 `|`53 `|`7B `|`C7 `|`6B `|`A9 `|`A5 `|`22 `|`50`|
|`10`<br>`97 `|`A3 `|`AA `|`31 `|`16 `|`C9 `|`9F `|`15 `|`F2 `|`E9 `|`DC `|`F9 `|`E3 `|`84 `|`D9 `|`4A`|
|`20`<br>`00 `|`6D `|`3C `|`0F `|`38 `|`B7 `|`82 `|`4B `|`AB `|`6E `|`6F `|`87 `|`41 `|`69 `|`5E `|`99`|
|`30`<br>`12 `|`36 `|`86 `|`04 `|`83 `|`05 `|`88 `|`30 `|`39 `|`25 `|`55 `|`9C `|`7A `|`23 `|`BC `|`62`|
|`40`<br>`2D `|`74 `|`E8 `|`46 `|`61 `|`C3 `|`AD `|`42 `|`A0 `|`56 `|`26 `|`1E `|`AC `|`E6 `|`D3 `|`5D`|
|`50`<br>`76 `|`0E `|`09 `|`FC `|`3B `|`78 `|`5C `|`48 `|`91 `|`EC `|`7D `|`64 `|`4E `|`57 `|`68 `|`2F`|
|`60`<br>`45 `|`CC `|`63 `|`3E `|`89 `|`5A `|`C5 `|`6A `|`2C `|`5F `|`0A `|`66 `|`20 `|`9E `|`2B `|`28`|
|`70`<br>`7F `|`D7 `|`E1 `|`75 `|`72 `|`40 `|`77 `|`51 `|`96 `|`54 `|`08 `|`3D `|`5B `|`7C `|`71 `|`93`|
|`80`<br>`B8 `|`85 `|`35 `|`27 `|`80 `|`1C `|`2A `|`33 `|`65 `|`37 `|`C1 `|`AF `|`EF `|`01 `|`A6 `|`8E`|
|`90`<br>`59 `|`BF `|`7E `|`DD `|`9A `|`ED `|`11 `|`79 `|`2E `|`CD `|`F0 `|`95 `|`9D `|`3A `|`17 `|`6C`|
|`A0`<br>`B4 `|`49 `|`10 `|`CB `|`0C `|`FB `|`06 `|`8F `|`0D `|`B0 `|`29 `|`13 `|`47 `|`4D `|`8A `|`F5`|
|`B0`<br>`CE `|`A8 `|`02 `|`BA `|`FD `|`A1 `|`24 `|`EE `|`F7 `|`81 `|`BB `|`B2 `|`F6 `|`3F `|`90 `|`D4`|
|`C0`<br>`8B `|`C2 `|`44 `|`C0 `|`67 `|`DF `|`0B `|`F4 `|`14 `|`C8 `|`A2 `|`D8 `|`98 `|`60 `|`E5 `|`B1`|
|`D0`<br>`FA `|`D0 `|`4F `|`D2 `|`D5 `|`BE `|`70 `|`D6 `|`1F `|`CA `|`03 `|`DA `|`92 `|`1B `|`C4 `|`EB`|
|`E0`<br>`73 `|`EA `|`1D `|`F8 `|`CF `|`E4 `|`F3 `|`4C `|`18 `|`43 `|`DE `|`E0 `|`94 `|`58 `|`8D `|`B6`|
|`F0`<br>`F1 `|`9B `|`E7 `|`19 `|`AE `|`C6 `|`B9 `|`BD `|`1A `|`E2 `|`A4 `|`D1 `|`B5 `|`52 `|`FF `|`07`|

Table 4: Inverse Scream S-box, table representation. 

#### **A.2.2 Algebraic Normal Form** 

_y_ 0 = _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 + _x_ 0 _x_ 2 _x_ 3 + _x_ 1 _x_ 2 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 0 _x_ 2 _x_ 5 + _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 3 _x_ 5 + _x_ 1 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 + _x_ 0 _x_ 2 + _x_ 1 _x_ 2 + _x_ 0 _x_ 3 + _x_ 1 _x_ 3 + _x_ 0 _x_ 4 + _x_ 2 _x_ 4 + _x_ 1 _x_ 5 + _x_ 4 _x_ 5 + _x_ 0 + _x_ 1 + _x_ 3 + _x_ 4 + _x_ 6 _y_ 1 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 4 _x_ 5 + _x_ 0 _x_ 3 _x_ 4 _x_ 5 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 7 + _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 5 _x_ 7 + _x_ 0 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 0 _x_ 3 _x_ 5 _x_ 7 + _x_ 1 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 + _x_ 0 _x_ 2 _x_ 3 + _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 4 + _x_ 0 _x_ 3 _x_ 4 + _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 1 _x_ 2 _x_ 5 + _x_ 1 _x_ 3 _x_ 5 + _x_ 1 _x_ 4 _x_ 5 + _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 6 + _x_ 0 _x_ 3 _x_ 6 + _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 0 _x_ 2 _x_ 7 + _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 1 _x_ 3 _x_ 7 + _x_ 0 _x_ 4 _x_ 7 + _x_ 2 _x_ 4 _x_ 7 + _x_ 1 _x_ 5 _x_ 7 + _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 2 + _x_ 1 _x_ 3 + _x_ 2 _x_ 3 + _x_ 1 _x_ 4 + _x_ 3 _x_ 4 + _x_ 1 _x_ 5 + _x_ 1 _x_ 6 + _x_ 3 _x_ 6 + _x_ 1 _x_ 7 + _x_ 3 _x_ 7 + _x_ 4 _x_ 7 + _x_ 6 _x_ 7 + _x_ 1 + _x_ 3 + _x_ 4 _y_ 2 = _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 + _x_ 0 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 6 + _x_ 0 _x_ 1 + _x_ 1 _x_ 2 + _x_ 0 _x_ 3 + _x_ 3 _x_ 5 + _x_ 0 _x_ 6 + _x_ 2 _x_ 6 + _x_ 5 _x_ 6 + _x_ 0 + _x_ 1 + _x_ 3 + _x_ 5 + _x_ 7 + 1 

_y_ 3 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 6+ _x_ 1 _x_ 2 _x_ 4 _x_ 6+ _x_ 0 _x_ 1 _x_ 5 _x_ 6+ _x_ 0 _x_ 2 _x_ 5 _x_ 6+ _x_ 1 _x_ 2 _x_ 5 _x_ 6+ _x_ 0 _x_ 3 _x_ 5 _x_ 6+ _x_ 1 _x_ 3 _x_ 5 _x_ 6+ _x_ 1 _x_ 2 _x_ 3 _x_ 7+ _x_ 0 _x_ 1 _x_ 2+ _x_ 0 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 4 + _x_ 1 _x_ 2 _x_ 4 + _x_ 0 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 0 _x_ 2 _x_ 5 + _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 3 _x_ 5 + _x_ 1 _x_ 3 _x_ 5 + _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 3 _x_ 6 + _x_ 0 _x_ 4 _x_ 6 + _x_ 2 _x_ 4 _x_ 6 + _x_ 1 _x_ 5 _x_ 6 + _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 0 _x_ 2 _x_ 7 + _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 1 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 + _x_ 1 _x_ 2 + _x_ 0 _x_ 4 + _x_ 1 _x_ 4 + _x_ 2 _x_ 4 + _x_ 3 _x_ 4 + _x_ 1 _x_ 5 + _x_ 4 _x_ 5 + _x_ 1 _x_ 7 + _x_ 4 _x_ 7 + _x_ 0 + _x_ 2 + _x_ 3 + _x_ 4 + _x_ 5 + 1 

_y_ 4 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 6 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 4 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 6 + _x_ 0 _x_ 1 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 4 _x_ 5 _x_ 6 + _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 3 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 4 _x_ 7 + _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 4 _x_ 5 _x_ 7 + _x_ 3 _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 6 _x_ 7 + _x_ 1 _x_ 2 _x_ 6 _x_ 7 + _x_ 0 _x_ 3 _x_ 6 _x_ 7 + _x_ 1 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 3 _x_ 6 _x_ 7 + 

16 

_x_ 2 _x_ 5 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 + _x_ 1 _x_ 3 _x_ 4 + _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 1 _x_ 2 _x_ 5 + _x_ 1 _x_ 3 _x_ 5 + _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 4 _x_ 5 + _x_ 2 _x_ 4 _x_ 5 + _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 6 + _x_ 0 _x_ 2 _x_ 6 + _x_ 1 _x_ 2 _x_ 6 + _x_ 0 _x_ 4 _x_ 6 + _x_ 1 _x_ 4 _x_ 6 + _x_ 2 _x_ 4 _x_ 6 + _x_ 3 _x_ 4 _x_ 6 + _x_ 0 _x_ 5 _x_ 6 + _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 7 + _x_ 2 _x_ 3 _x_ 7 + _x_ 3 _x_ 4 _x_ 7 + _x_ 3 _x_ 5 _x_ 7 + _x_ 4 _x_ 5 _x_ 7 + _x_ 1 _x_ 6 _x_ 7 + _x_ 3 _x_ 6 _x_ 7 + _x_ 4 _x_ 6 _x_ 7 + _x_ 5 _x_ 6 _x_ 7 + _x_ 1 _x_ 2 + _x_ 0 _x_ 4 + _x_ 2 _x_ 4 + _x_ 3 _x_ 4 + _x_ 3 _x_ 5 + _x_ 0 _x_ 6 + _x_ 1 _x_ 6 + _x_ 2 _x_ 6 + _x_ 3 _x_ 6 + _x_ 0 _x_ 7 + _x_ 1 _x_ 7 + _x_ 4 _x_ 7 + _x_ 6 _x_ 7 + _x_ 1 + _x_ 2 + _x_ 3 + _x_ 4 + _x_ 7 

_y_ 5 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 6 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 6 + _x_ 0 _x_ 1 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 2 _x_ 4 _x_ 7 + _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 2 _x_ 5 _x_ 7 + _x_ 2 _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 4 + _x_ 1 _x_ 2 _x_ 4 + _x_ 0 _x_ 3 _x_ 4 + _x_ 0 _x_ 3 _x_ 5 + _x_ 1 _x_ 3 _x_ 5 + _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 6 + _x_ 0 _x_ 3 _x_ 6 + _x_ 0 _x_ 4 _x_ 6 + _x_ 2 _x_ 4 _x_ 6 + _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 1 _x_ 3 _x_ 7 + _x_ 2 _x_ 3 _x_ 7+ _x_ 2 _x_ 6 _x_ 7+ _x_ 0 _x_ 2+ _x_ 1 _x_ 4+ _x_ 2 _x_ 4+ _x_ 3 _x_ 4+ _x_ 1 _x_ 5+ _x_ 3 _x_ 5+ _x_ 0 _x_ 6+ _x_ 2 _x_ 6+ _x_ 5 _x_ 6+ _x_ 4 _x_ 7+ _x_ 0+ _x_ 2+ _x_ 6+ _x_ 7 

_y_ 6 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 7+ _x_ 1 _x_ 2 _x_ 3 _x_ 5 _x_ 7+ _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 7+ _x_ 1 _x_ 2 _x_ 3 _x_ 6 _x_ 7+ _x_ 0 _x_ 1 _x_ 2 _x_ 3+ _x_ 0 _x_ 1 _x_ 2 _x_ 4+ _x_ 0 _x_ 1 _x_ 3 _x_ 4+ _x_ 1 _x_ 2 _x_ 3 _x_ 5+ _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 6 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 2 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 4 _x_ 5 _x_ 6 + _x_ 1 _x_ 4 _x_ 5 _x_ 6 + _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 3 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 2 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 6 _x_ 7 + _x_ 0 _x_ 3 _x_ 6 _x_ 7 + _x_ 1 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 5 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 + _x_ 0 _x_ 1 _x_ 4 + _x_ 0 _x_ 2 _x_ 4 + _x_ 1 _x_ 3 _x_ 4 + _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 2 _x_ 5 + _x_ 0 _x_ 4 _x_ 5 + _x_ 1 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 6 + _x_ 1 _x_ 4 _x_ 6 + _x_ 3 _x_ 4 _x_ 6 + _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 1 _x_ 3 _x_ 7 + _x_ 2 _x_ 3 _x_ 7 + _x_ 0 _x_ 4 _x_ 7 + _x_ 1 _x_ 4 _x_ 7 + _x_ 2 _x_ 4 _x_ 7 + _x_ 1 _x_ 5 _x_ 7 + _x_ 1 _x_ 6 _x_ 7 + _x_ 4 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 + _x_ 1 _x_ 3 + _x_ 2 _x_ 3 + _x_ 1 _x_ 4 + _x_ 0 _x_ 5 + _x_ 1 _x_ 5 + _x_ 3 _x_ 5 + _x_ 0 _x_ 6 + _x_ 2 _x_ 6 + _x_ 3 _x_ 6 + _x_ 4 _x_ 6 + _x_ 5 _x_ 6 + _x_ 1 _x_ 7 + _x_ 4 _x_ 7 + _x_ 1 + _x_ 3 

_y_ 7 = _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 1 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 _x_ 6 + _x_ 1 _x_ 2 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 2 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 2 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 5 + _x_ 1 _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 1 _x_ 4 _x_ 5 + _x_ 1 _x_ 3 _x_ 4 _x_ 5 + _x_ 2 _x_ 3 _x_ 4 _x_ 5 + _x_ 0 _x_ 2 _x_ 3 _x_ 6 + _x_ 0 _x_ 2 _x_ 4 _x_ 6 + _x_ 0 _x_ 1 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 5 _x_ 6 + _x_ 0 _x_ 4 _x_ 5 _x_ 6 + _x_ 1 _x_ 4 _x_ 5 _x_ 6 + _x_ 3 _x_ 4 _x_ 5 _x_ 6 + _x_ 0 _x_ 2 _x_ 3 _x_ 7 + _x_ 1 _x_ 2 _x_ 4 _x_ 7 + _x_ 0 _x_ 3 _x_ 4 _x_ 7 + _x_ 0 _x_ 1 _x_ 5 _x_ 7 + _x_ 0 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 2 _x_ 5 _x_ 7 + _x_ 1 _x_ 3 _x_ 5 _x_ 7 + _x_ 2 _x_ 3 _x_ 5 _x_ 7 + _x_ 0 _x_ 4 _x_ 5 _x_ 7 + _x_ 2 _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 1 _x_ 6 _x_ 7 + _x_ 0 _x_ 3 _x_ 6 _x_ 7 + _x_ 1 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 3 _x_ 6 _x_ 7 + _x_ 2 _x_ 5 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 _x_ 2 + _x_ 0 _x_ 2 _x_ 3 + _x_ 1 _x_ 2 _x_ 3 + _x_ 0 _x_ 3 _x_ 4 + _x_ 1 _x_ 3 _x_ 4 + _x_ 2 _x_ 3 _x_ 4 + _x_ 0 _x_ 1 _x_ 5 + _x_ 2 _x_ 3 _x_ 5 + _x_ 0 _x_ 4 _x_ 5 + _x_ 1 _x_ 4 _x_ 5 + _x_ 2 _x_ 4 _x_ 5 + _x_ 1 _x_ 2 _x_ 6 + _x_ 1 _x_ 3 _x_ 6 + _x_ 0 _x_ 4 _x_ 6 + _x_ 1 _x_ 4 _x_ 6 + _x_ 3 _x_ 4 _x_ 6 + _x_ 1 _x_ 5 _x_ 6 + _x_ 3 _x_ 5 _x_ 6 + _x_ 0 _x_ 1 _x_ 7 + _x_ 1 _x_ 2 _x_ 7 + _x_ 0 _x_ 3 _x_ 7 + _x_ 1 _x_ 3 _x_ 7 + _x_ 2 _x_ 3 _x_ 7 + _x_ 1 _x_ 4 _x_ 7 + _x_ 2 _x_ 4 _x_ 7 + _x_ 4 _x_ 5 _x_ 7 + _x_ 0 _x_ 6 _x_ 7 + _x_ 1 _x_ 6 _x_ 7 + _x_ 4 _x_ 6 _x_ 7 + _x_ 0 _x_ 1 + _x_ 0 _x_ 2 + _x_ 1 _x_ 2 + _x_ 0 _x_ 3 + _x_ 1 _x_ 3 + _x_ 0 _x_ 4 + _x_ 3 _x_ 4 + _x_ 0 _x_ 5 + _x_ 2 _x_ 5 + _x_ 0 _x_ 6 + _x_ 1 _x_ 6 + _x_ 2 _x_ 6 + _x_ 5 _x_ 6 + _x_ 0 _x_ 7 + _x_ 1 _x_ 7 + _x_ 2 _x_ 7 + _x_ 4 _x_ 7 + _x_ 5 _x_ 7 + _x_ 6 _x_ 7 + _x_ 0 + _x_ 2 + _x_ 3 + _x_ 5 + _x_ 6 +1 

17 

### **A.3 Scream L-box** 

#### **A.3.1** 8 **-bit table representation** 

```
0123456789ABCDEF
000038526A7B43291196AEC4FCEDD5BF87
10D7EF85BDAC94FEC64179132B3A026850
203A0268504179132BAC94FEC6D7EF85BD
30EDD5BF8796AEC4FC7B4329110038526A
40E5DDB78F9EA6CCF4734B211908305A62
50320A605849711B23A49CF6CEDFE78DB5
60DFE78DB5A49CF6CE49711B23320A6058
7008305A62734B21199EA6CCF4E5DDB78F
80FEC6AC9485BDD7EF68503A02132B4179
9029117B43526A0038BF87EDD5C4FC96AE
A0C4FC96AEBF87EDD5526A003829117B43
B0132B417968503A0285BDD7EFFEC6AC94
C01B2349716058320A8DB5DFE7F6CEA49C
D0CCF49EA6B78FE5DD5A6208302119734B
E02119734B5A620830B78FE5DDCCF49EA6
F0F6CEA49C8DB5DFE76058320A1B234971
```

`Table 5:` L1 _,_ 1 `.` 

```
0123456789ABCDEF
00005CA9F5B3EF1A46C19D6834722EDB87
106D31C498DE82772BACF005591F43B6EA
20E0BC4915530FFAA6217D88D492CE3B67
308DD124783E6297CB4C10E5B9FFA3560A
4024788DD197CB3E62E5B94C10560AFFA3
504915E0BCFAA6530F88D4217D3B6792CE
60C4986D31772BDE820559ACF0B6EA1F43
70A9F5005C1A46B3EF6834C19DDB87722E
80A5F90C50164ABFE36438CD91D78B7E22
90C894613D7B27D28E0955A0FCBAE6134F
A04519ECB0F6AA5F0384D82D71376B9EC2
B0287481DD9BC7326EE9B5401C5A06F3AF
C081DD2874326E9BC7401CE9B5F3AF5A06
D0ECB045195F03F6AA2D7184D89EC2376B
E0613DC894D28E7B27A0FC0955134FBAE6
F00C50A5F9BFE3164ACD9164387E22D78B
```

Table 6: L1 _,_ 2. 

18 

```
0123456789ABCDEF
```

```
000046F1B7A1E750167F398EC8DE982F69
10672196D0C6803771185EE9AFB9FF480E
207A3C8BCDDB9D2A6C0543F4B2A4E25513
301D5BECAABCFA4D0B622493D5C3853274
40703681C7D19720660F49FEB8AEE85F19
```

```
501751E6A0B6F04701682E99DFC98F387E
600A4CFBBDABED5A1C753384C2D4922563
706D2B9CDACC8A3D7B1254E3A5B3F54204
808ACC7B3D2B6DDA9CF5B304425412A5E3
90EDAB1C5A4C0ABDFB92D463253375C284
```

```
A0F0B601475117A0E68FC97E382E68DF99
B097D166203670C781E8AE195F490FB8FE
```

```
C0FABC0B4D5B1DAAEC85C374322462D593
D09DDB6C2A3C7ACD8BE2A413554305B2F4
E080C671372167D096FFB90E485E18AFE9
F0E7A116504600B7F198DE692F397FC88E
```

Table 7: L2 _,_ 1. 

```
0123456789ABCDEF
00004BAFE433789CD7743FDB90470CE8A3
101259BDF6216A8EC5662DC982551EFAB1
206F24C08B5C17F3B81B50B4FF286387CC
307D36D2994E05E1AA0942A6ED3A7195DE
401B50B4FF286387CC6F24C08B5C17F3B8
500942A6ED3A7195DE7D36D2994E05E1AA
60743FDB90470CE8A3004BAFE433789CD7
70662DC982551EFAB11259BDF6216A8EC5
80B1FA1E5582C92D66C58E6A21F6BD5912
90A3E80C4790DB3F74D79C7833E4AF4B00
A0DE95713AEDA64209AAE1054E99D2367D
B0CC876328FFB4501BB8F3175C8BC0246F
C0AAE1054E99D2367DDE95713AEDA64209
D0B8F3175C8BC0246FCC876328FFB4501B
E0C58E6A21F6BD5912B1FA1E5582C92D66
F0D79C7833E4AF4B00A3E80C4790DB3F74
```

Table 8: L2 _,_ 2. 

19 

### **A.4 Inverse Scream L-box** 

#### **A.4.1 Binary representation** 

|<br>0|1|1|1|1|0|0|1|1|1|1|0|0|1|1|1<br>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|<br><br>0|0|1|0|0|0|0|0|1|1|1|0|1|1|1|0<br><br><br>|
|<br><br><br>1|0|0|0|1|0|1|1|0|1|0|1|0|1|0|0<br><br><br>|
|<br><br><br>1|1|0|0|1|0|0|0|1|1|0|0|0|1|1|0<br><br><br>|
|<br><br><br>1|0|1|0|0|0|0|0|0|0|1|1|1|0|1|1<br><br><br>|
|<br><br><br>0|1|1|0|1|1|1|1|0|1|1|1|0|1|0|1<br><br><br>|
|<br><br><br>1|0|0|1|1|1|0|0|1|0|0|1|0|1|0|0<br><br><br>|
|<br><br><br>0|1|1|1|0|1|0|1|0|1|0|0|0|0|0|1<br><br><br>|
|<br><br>0|0|1|0|1|0|1|0|0|1|1|1|1|0|0|0<br><br><br>|
|<br><br>0|1|1|1|1|1|0|1|1|0|0|1|1|1|0|1<br><br><br>|
|<br><br>0|0|0|1|1|0|1|1|1|0|0|1|1|0|0|0<br><br><br>|
|<br><br>1|0|1|0|0|1|0|1|0|0|0|1|0|1|0|1<br><br><br>|
|<br><br>1|1|1|1|1|1|0|1|0|1|0|1|0|1|1|0<br><br><br>|
|<br><br><br>1|0|1|0|0|1|1|1|0|1|1|1|1|1|1|0<br><br><br><br>|
|<br><br>0|1|1|0|1|0|1|1|1|1|0|1|1|1|1|0<br><br><br>|
|<br>0|0|0|1|1|0|1|1|0|1|1|0|0|0|0|1<br>|

#### **A.4.2** 8 **-bit table representation** 

L( _b_ 0 _∥ b_ 1) = �L1 _,_ 1( _b_ 1) _⊕_ L2 _,_ 1( _b_ 0)� _∥_ �L1 _,_ 2( _b_ 1) _⊕_ L2 _,_ 2( _b_ 0)�. 

|`0`|`1`|`2`|`3`|`4`|`5`|`6`|`7`|`8`|`9`|`A`|`B`|`C`|`D`|`E`|`F`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|`00`<br>`00 `|`E7 `|`77 `|`90 `|`2A `|`CD `|`5D `|`BA `|`63 `|`84 `|`14 `|`F3 `|`49 `|`AE `|`3E `|`D9`|
|`10`<br>`DC `|`3B `|`AB `|`4C `|`F6 `|`11 `|`81 `|`66 `|`BF `|`58 `|`C8 `|`2F `|`95 `|`72 `|`E2 `|`05`|
|`20`<br>`AE `|`49 `|`D9 `|`3E `|`84 `|`63 `|`F3 `|`14 `|`CD `|`2A `|`BA `|`5D `|`E7 `|`00 `|`90 `|`77`|
|`30`<br>`72 `|`95 `|`05 `|`E2 `|`58 `|`BF `|`2F `|`C8 `|`11 `|`F6 `|`66 `|`81 `|`3B `|`DC `|`4C `|`AB`|
|`40`<br>`29 `|`CE `|`5E `|`B9 `|`03 `|`E4 `|`74 `|`93 `|`4A `|`AD `|`3D `|`DA `|`60 `|`87 `|`17 `|`F0`|
|`50`<br>`F5 `|`12 `|`82 `|`65 `|`DF `|`38 `|`A8 `|`4F `|`96 `|`71 `|`E1 `|`06 `|`BC `|`5B `|`CB `|`2C`|
|`60`<br>`87 `|`60 `|`F0 `|`17 `|`AD `|`4A `|`DA `|`3D `|`E4 `|`03 `|`93 `|`74 `|`CE `|`29 `|`B9 `|`5E`|
|`70`<br>`5B `|`BC `|`2C `|`CB `|`71 `|`96 `|`06 `|`E1 `|`38 `|`DF `|`4F `|`A8 `|`12 `|`F5 `|`65 `|`82`|
|`80`<br>`82 `|`65 `|`F5 `|`12 `|`A8 `|`4F `|`DF `|`38 `|`E1 `|`06 `|`96 `|`71 `|`CB `|`2C `|`BC `|`5B`|
|`90`<br>`5E `|`B9 `|`29 `|`CE `|`74 `|`93 `|`03 `|`E4 `|`3D `|`DA `|`4A `|`AD `|`17 `|`F0 `|`60 `|`87`|
|`A0`<br>`2C `|`CB `|`5B `|`BC `|`06 `|`E1 `|`71 `|`96 `|`4F `|`A8 `|`38 `|`DF `|`65 `|`82 `|`12 `|`F5`|
|`B0`<br>`F0 `|`17 `|`87 `|`60 `|`DA `|`3D `|`AD `|`4A `|`93 `|`74 `|`E4 `|`03 `|`B9 `|`5E `|`CE `|`29`|
|`C0`<br>`AB `|`4C `|`DC `|`3B `|`81 `|`66 `|`F6 `|`11 `|`C8 `|`2F `|`BF `|`58 `|`E2 `|`05 `|`95 `|`72`|
|`D0`<br>`77 `|`90 `|`00 `|`E7 `|`5D `|`BA `|`2A `|`CD `|`14 `|`F3 `|`63 `|`84 `|`3E `|`D9 `|`49 `|`AE`|
|`E0`<br>`05 `|`E2 `|`72 `|`95 `|`2F `|`C8 `|`58 `|`BF `|`66 `|`81 `|`11 `|`F6 `|`4C `|`AB `|`3B `|`DC`|
|`F0`<br>`D9 `|`3E `|`AE `|`49 `|`F3 `|`14 `|`84 `|`63 `|`BA `|`5D `|`CD `|`2A `|`90 `|`77 `|`E7 `|`00`|

Table 9: L1 _,_ 1. 

20 

```
0123456789ABCDEF
00009E049AD14FD54B138D1789C25CC658
10059B019FD44AD04E1688128CC759C35D
20F668F26C27B923BDE57BE17F34AA30AE
30F36DF76922BC26B8E07EE47A31AF35AB
4039A73DA3E876EC722AB42EB0FB65FF61
503CA238A6ED73E9772FB12BB5FE60FA64
60CF51CB551E801A84DC42D8460D930997
70CA54CE501B851F81D947DD4308960C92
80AE30AA347FE17BE5BD23B9276CF268F6
90AB35AF317AE47EE0B826BC2269F76DF3
A058C65CC289178D134BD54FD19A049E00
B05DC359C78C1288164ED04AD49F019B05
C09709930D46D842DC841A801E55CB51CF
D0920C960843DD47D9811F851B50CE54CA
E061FF65FBB02EB42A72EC76E8A33DA739
F064FA60FEB52BB12F77E973EDA638A23C
```

Table 10: L1 _,_ 2. 

```
0123456789ABCDEF
00001EB9A71907A0BEA8B6110FB1AF0816
106A74D3CD736DCAD4C2DC7B65DBC5627C
207E60C7D96779DEC0D6C86F71CFD17668
30140AADB30D13B4AABCA2051BA5BB1C02
407B65C2DC627CDBC5D3CD6A74CAD4736D
50110FA8B60816B1AFB9A7001EA0BE1907
60051BBCA21C02A5BBADB3140AB4AA0D13
706F71D6C87668CFD1C7D97E60DEC06779
8086983F219F8126382E30978937298E90
90ECF2554BF5EB4C52445AFDE35D43E4FA
A0F8E6415FE1FF5846504EE9F74957F0EE
B0928C2B358B95322C3A24839D233D9A84
C0FDE3445AE4FA5D43554BECF24C52F5EB
D097892E308E9037293F21869826389F81
E0839D3A249A84233D2B35928C322C8B95
F0E9F7504EF0EE4957415FF8E65846E1FF
```

Table 11: L2 _,_ 1. 

21 

```
0123456789ABCDEF
000054BEEAD88C6632A5F11B4F7D29C397
10BFEB01556733D98D1A4EA4F0C2967C28
20E5B15B0F3D6983D74014FEAA98CC2672
305A0EE4B082D63C68FFAB4115277399CD
40D682683C0E5AB0E47327CD99ABFF1541
50693DD783B1E50F5BCC9872261440AAFE
6033678DD9EBBF550196C2287C4E1AF0A4
708CD832665400EABE297D97C3F1A54F1B
80D88C66320054BEEA7D29C397A5F11B4F
906733D98DBFEB0155C2967C281A4EA4F0
A03D6983D7E5B15B0F98CC26724014FEAA
B082D63C685A0EE4B0277399CDFFAB4115
C00E5AB0E4D682683CABFF15417327CD99
D0B1E50F5B693DD7831440AAFECC987226
E0EBBF550133678DD94E1AF0A496C2287C
F05400EABE8CD83266F1A54F1B297D97C3
```

Table 12: L2 _,_ 2. 

## **B Round Constants** 

We use simple constants in order to limit their implementation cost, but expect them to avoid any kind of slide attack of self-similarity property. The round constants in Scream are defined as: _C_ ( _ρ_ ) = 2199 _· ρ_ mod 2<sup>16</sup> . We consider constants of the form _C_ ( _ρ_ ) = _C · ρ_ mod 2<sup>16</sup> because they can implemented by incrementing a counter by steps of _C_ . However, we would rather avoid the trivial choice _C_ = 1 because this implies simple linear relations between the constants, such as _C_ (2 _ρ_ + 1) = _C_ (2 _ρ_ ) _⊕_ 1. Concretely, we built 16 _×_ 16 matrices with the binary representation of _C_ (1), _C_ (2), . . . , _C_ (16), and computed the rank of these matrices. There are a few values that give a full rank matrix, and we decided to use the smallest value with this property: 2199. 

22 

### **C.1 Single key, fixed tweak** 

With a fixed tweak, Scream is a slightly modified version of Fantomas, with a different L-box. Therefore, we can compute bounds on its number of active S-boxes for differential and linear trails following [12]. 

### **C.2 Single key, chosen tweaks** 

The L-box of Scream has been chosen so that trails over one step (2 rounds) with the same input and output difference pattern have at least 14 active S-boxes. Due to the structure of the tweakey scheduling, a pair of tweaks with a truncated difference _δ_ gives tweakeys with the difference pattern _δ_ in every round. In particular a trail ‘ `-x-` ’ using a difference in the tweak leads to the same pattern of active S-boxes _δ_ at the beginning and at the end of the second round; this implies at least 14 active S-boxes. 

We also use bounds from single key trails in our analysis of related-key trails. For instance, a ‘ ’ trail `-xx-` gives truncated differences _δ_ ⇝ _a_ , _b_ ⇝ _δ_ assuming a difference _δ_ in the tweakeys, and the truncated difference _a_ must be transformed into _b_ after a tweakey addition with difference _δ_ . This can transformed into a single key trail over two steps: _b_ ⇝ _δ_ ⇝ _a_ , and we know that such a trail has at least 20 active S-boxes. Moreover, we can enumerate the trails with 20 active S-boxes, and we found than there is a single trail where the patterns _a_ , _b_ , and _δ_ are compatible: 

This leads to the following analysis of differential trails: 

**5-step trails.** We can list all the possible 5-step trails with 3 active steps or less (we use symmetries to consider only half of the patterns), and compute a lower bound on the corresponding number of active S-boxes: 

`-x-x-` **:** At least 28 active S-boxes. 

`-x-xx` **:** At least 30 active S-boxes (14 + 8 + 8). 

`-xx-x` **:** At least 28 active S-boxes (20 + 8). 

`-xxx-` **:** At least 28 active S-boxes (20 + 8; 20 for steps 1 and 3 combined). 

`x-x-x` **:** At least 30 active S-boxes (8 + 14 + 8). If there are 4 or more active steps, this implies at least 8 _×_ 4 = 32 active S-boxes. 

**6-step trails.** Similarly, we can list all the possible 6-step trails with 4 active steps or less: 

`-x-x-x` **:** At least 36 active S-boxes (14 + 14 + 8). 

`-x-xx-` **:** At least 34 active S-boxes (14 + 20). 

`-x-xxx` **:** At least 38 active S-boxes (14 + 8 + 8 + 8). 

`-xx-xx` **:** At least 36 active S-boxes (20 + 8 + 8). 

`-xxx-x` **:** At least 36 active S-boxes (20 + 8 + 8; 20 for steps 1 and 3 combined). 

`-xxxx-` **:** At least 36 active S-boxes (20 + 8 + 8; 20 for steps 1 and 4 combined). 

23 

`x-x-xx` **:** At least 38 active S-boxes (8 + 14 + 8 + 8). 

`x-xx-x` **:** At least 36 active S-boxes (8 + 20 + 8). 

If there are 5 or more active steps, this implies at least 8 _×_ 5 = 40 active S-boxes. 

In addition, we verified that there is no valid trail with only 34 active S-boxes following `-x-xx-` : the only trail with weight 20 for steps 3 and 4 gives a tweak difference _δ_ with no valid trails _δ_ ⇝ _δ_ for step 1. This proves that 6-step trails have at least 35 active S-boxes. 

### **C.3 Related keys, chosen tweaks** 

**All tweakeys active.** First, let us consider trails with a difference in all the tweakeys. Using a difference in the key and in the tweak, it could be possible to have tweakey differences with only 8 active S-boxes per step. However, such trails must still activate at least _⌊σ/_ 2 _⌋_ steps. Therefore, they have at least 8 _· ⌊σ/_ 2 _⌋_ active S-boxes. 

We can improve this bound using the property of the tweakey scheduling that the same tweakeys are used every three rounds. In particular, a trail ‘ `-x-x-` ’ would have tweakey differences _δ_ 0, _δ_ 1, _δ_ 2, _δ_ 0, _δ_ 1, _δ_ 2, and transitions _δ_ 1 ⇝ _δ_ 2 and _δ_ 0 ⇝ _δ_ 1. This can be turned into a 2-step single key trail _δ_ 0 ⇝ _δ_ 1 ⇝ _δ_ 2 that has at least 20 active S-boxes. This implies the following bounds: 

- The only 7-step trail with 3 active steps is ‘ `-x-x-x-` ’; it has at least 28 active S-boxes. Trails with 4 or more active steps have at least 32 active S-boxes. 

- The only 9-step trail with 4 active steps is ‘ `-x-x-x-x-` ’; it has at least 40 active S-boxes. Trails with 5 or more active steps have at least 40 active S-boxes. 

**Some tweakeys inactive.** The tweakey scheduling of Scream further allows to cancel some key and tweak differences. Let us now consider trails where some tweakeys are inactive. Without loss of generality, we assume that _δ_ [ _K_ ] = _δ_ [ _T_ ]. The tweakey differences for the following rounds will be: 

In particular, the truncated pattern _δ_ will be the same for all the active tweakeys, because _φ_ is computed on each state line independently. 

This leads to the following analysis of trails: 

   - **2-step trails.** They can have no active step if the second tweakey is inactive. 

- **3-step trails.** A 3-step trail with a single active step has at least 8 active S-boxes. This can 

- be reached by following ‘ `--x` ’. 

**4-step trails.** A 4-step trail with a single active step must follow ‘ `--x-` ’. The third step must have the same input and output pattern, therefore it has at least 14 active S-boxes. Trails with two or more active steps have at least 16 active S-boxes. 

More generally, a trail over _σ_ steps has at least: 

- 14 _· ⌊σ/_ 3 _⌋−_ 6 active S-boxes if _σ_ mod 3 = 0. 

- 14 _· ⌊σ/_ 3 _⌋_ active S-boxes otherwise. 

24