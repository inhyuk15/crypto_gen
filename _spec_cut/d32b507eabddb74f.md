### AES-CMCC v1.1 

Designer: Jonathan Trostle Submitter: Jonathan Trostle jon49175@yahoo.com 

2014.03.01 

**Chapter 1** 

# **Specification** 

#### **1.1 Parameters** 

AES-CMCC v1 has the following parameters: 

1. Stateful or stateless 2. Key size: 128 bits, 192 bits, or 256 bits. 3. Authentication Tag Length: 0 bytes up to 16 bytes. 

###### 4. Secret Message Number (SMN) length (stateful only): 16 bytes 

5. Stateful scheme ciphertext expansion: 0-8 bytes 6. Public Message Number (PMN) length (stateless only: 0-16 bytes) 7. The MAC algorithm for computing _V_ (see Section 1.3) can be any MAC algorithm with the 

standard MAC security property (forgery under an adaptive chosen message attack), except that if it takes a nonce as one of its input parameters, the MAC algorithm must be misuse resistant when a nonce is reused.<sup>1</sup> Each parameter is an integer number of bytes. 

#### **1.2 Recommended Parameter Sets** 

All recommended parameter sets have 128 bit keys, and the MAC algorithm for computing _V_ is AES-CMAC.<sup>2</sup> All stateful versions have a 16 byte SMN. 

|(1) Stateless: Authentication tag length 8 bytes, PMN length 4 bytes.|
|---|
|(2) Stateless: Authentication tag length 4 bytes, PMN length 4 bytes.|
|(3) Stateless: Authentication tag length 4 bytes, PMN length 2 bytes.|

> 1This MAC algorithm is used as part of the encryption process and does not produce the authentication tag in the 3rd parameter above. The authentication tag is a string of zero bits. 

> 2NIST Special Publication 800-38B Recommendation for Block Cipher Modes of Operation: The CMAC Mode for Authentication 

1 

(4) Stateless: Authentication tag length 2 bytes, PMN length 4 bytes. (5) Stateless: Authentication tag length 2 bytes, PMN length 2 bytes. 

We have not recommended any stateful parameter sets since these would require a shared strategy for generating the private message numbers between the communication peers (e.g., increment by 1 starting at 0). The call for ciphers allows the caller to generate message numbers using any caller specific algorithm, so the caller algorithm may not be known to the communication peer. 

#### **1.3 Authenticated Encryption** 

##### **1.3.1 CMCC Stateless Scheme** 

###### **Notation** 

We use _|_ to denote concatenation of strings, and _⊕_ denotes bitwise xor. _b_<sup>_j_</sup> is the bit _b_ repeated _j_ times. The notation _R_ 128 = 0<sup>120</sup> 10000111 denotes the bit string with 120 zero bits, followed by the bits 1,0,0,0,0,1,1, and 1. _x << n_ denotes the left shift operator (filling vacated bits with zero bits), after shifting the string _x_ by _n_ bits to the left. _|S|_ denotes the length of the string _S. B_ denotes the block length of the underlying block cipher (AES for this specification). _Ek_ denotes encryption using the block cipher and input key _k._ 

_LSBj_ ( _x_ ) and _MSBj_ ( _x_ ) denote the _j_ least significant bytes and _j_ most significant bytes of byte string _x_ respectively. 

###### **Padding** 

We will apply the padding scheme from the AES-CMAC algorithm to our mode when CBC encryption is performed. One difference is that we will sometimes need to pad by a full block length ( _B/_ 8 bytes)<sup>3</sup> and we use the same padding scheme as when the padding is between 1 and _B/_ 8 _−_ 1 bytes. 

1. Given the CBC encryption key _K,_ and byte strings _S_ 1 and _S_ 2 _,_ where _|S_ 1 _| ≤|S_ 2 _|._ We define _pad_ ( _S_ 1) _S_ 2 as follows: 

2. _pad_ _~~l~~ ength_ is the number of bits (which is a multiple of 8) needed to bring _S_ 1 up to the length of _S_ 2 and then bring _S_ 1 up to a multiple of the block size. More formally, 

_pad_ _~~l~~ ength_ = _|S_ 2 _| −|S_ 1 _|_ + _B −_ ( _|S_ 2 _|_ mod _B_ ) 

where mod values are taken between 1 and _B._ 

3. We define _L_ = _EK_ (0<sup>_B_</sup> ) _._ If the most significant bit of _L_ is zero, then define _K_ 1 = _L <<_ 1 _,_ otherwise, we define _K_ 1 = ( _L <<_ 1) _⊕ R_ 128 _._ If the most significant bit of _K_ 1 is zero, then define _K_ 2 = _K_ 1 _<<_ 1 _._ Otherwise, we define _K_ 2 = ( _K_ 1 _<<_ 1) _⊕ R_ 128 _._ 

   - If _pad length_ = 0 _,_ then _|S_ 1 _|_ is a multiple of _B_ ; let _F_ be the last block of _S_ 1 _._ We define _pad_ ( _S_ 1) _S_ 2 to be _S_ 1 with its last block replaced with _F ⊕ K_ 1 _._ 

> 3If _S_ 1 is a multiple of _B_ and _S_ 2 is one byte longer, than we pad _S_ 1 with _B/_ 8 bytes. If both strings are the same length which is a multiple of _B_ then we do not add any padding bytes. 

2 

If 1 _≤ pad_ _~~l~~ ength ≤ B,_ then we append the following string to the last (possibly empty) block _F_ of _S_ 1 : 10<sup>_pad_</sup> _~~l~~ ength−_ 1 _. pad_ ( _S_ 1) _S_ 2 is _S_ 1 with the last block of _S_ 1 replaced with _F |_ 10<sup>_pad_</sup> _~~l~~ ength−_ 1 _⊕ K_ 2 _._ 

Figures 1.1 and 1.2 describe the stateless version of CMCC. 

3 

###### **CMCC Mode - Encryption** 

_CBC_ ( _IV, P, Key_ ) is CBC encryption with initialization vector _IV,_ plaintext _P,_ and key _Key. MAC_ ( _IV, P, Key_ ) is MAC algorithm with output string of length _l/_ 8 bits (one block) with initialization vector _IV,_ plaintext _P,_ and key _Key. pad_ () is the padding algorithm defined in Section 1.3.1. _E_ ¯ _K_<sup>istheblockcipherwithkey</sup><sup>_K._¯</sup> 

¯ **Encryption Inputs:** plaintext _P,_ key _K_ = _K, L_ 3 _, L_ 2 _,_ ¯ _L_ 2 _, L_ 1, public message number _N,_ and associated data _A._ 

Given constant 0 _xb_ 6 _. . ._ 0 _xb_ 6 _,_ (repeated 16 times), we take the 16 _−|N |_ most significant bytes and prepend them to _N_ to obtain _M,_ where _|N |_ denotes the length of _N_ in bytes. 

Let _Z_ be the bit string with _τ_ zero bits ( _τ_ is the number of authentication bits). 

Let _W_ = _E_ ¯ _K_<sup>(</sup><sup>_M_)</sup><sup>_._</sup> 

_Q_ = _P |Z._ 

Let _Q_ = _P_ 1 _|P_ 2 where _|P_ 1 _|_ = _|P_ 2 _|_ or _|P_ 1 _|_ = _|P_ 2 _| −_ 8 ( _P_ 1 may be one byte shorter than _P_ 2 _._ ) 

_X_ = _CBC_ ( _W, pad_ ( _P_ 1) _P_ 2 _, L_ 3) _⊕ P_ 2 _, X_ is truncated to the length of _P_ 2 _._ 

_Y_ = _X|A_ 

_V_ = _MAC_ ( _W, Y, L_ 2) _,_ 

_P_ 1 = _P_<sup>¯</sup> 1 _,_ 1 _| . . . |P_<sup>¯</sup> 1 _,i|P_<sup>¯</sup> 1 _,i_ +1 where _i ≥_ 0 _, P_<sup>¯</sup> 1 _,_ 1 _, . . . , P_<sup>¯</sup> 1 _,i_ are full blocks and _P_<sup>¯</sup> 1 _,i_ +1 is a partial (possibly empty) block, 

_X_ 2 = _V ⊕ P_<sup>¯</sup> 1 _,_ 1 _|EL_ ¯2( _V_ + 1) _⊕ P_<sup>¯</sup> 1 _,_ 2 _| . . . |EL_ ¯2( _V_ + _i_ ) _⊕ P_<sup>¯</sup> 1 _,i_ +1 _._ ¯ ( _EL_ 2( _V_ + _j_ ) is truncated to the length of _P_<sup>¯</sup> 1 _,j_ +1 for _j ≥_ 1 _,_ and bits 31,63 of V are zeroed for j=1.) 

_X_ 1 = _CBC_ ( _W, pad_ ( _X_ 2) _X , L_ 1) _⊕ X, X_ 1 is truncated to the length of _X._ 

**Ciphertext:** _X_ 1 _, X_ 2 

Figure 1.1: CMCC Mode Encryption - Stateless Version 

4 

**Decryption Inputs:** _X_ 1 _, X_ 2 _, M, A_ 

_W_ = _E_ ¯ _K_<sup>(</sup><sup>_M_)</sup><sup>_._</sup> 

_X_ = _CBC_ ( _W, pad_ ( _X_ 2) _X_ 1 _, L_ 1) _⊕ X_ 1 

_Y_ = _X|A._ 

_V_ = _MAC_ ( _W, Y, L_ 2) 

_X_ 2 = _X_<sup>¯</sup> 2 _,_ 1 _| . . . |X_<sup>¯</sup> 2 _,i|X_<sup>¯</sup> 2 _,i_ +1 where _i ≥_ 0 and _X_<sup>¯</sup> 2 _,_ 1 _, . . . , X_<sup>¯</sup> 2 _,i_ are full blocks and _X_<sup>¯</sup> 2 _,i_ +1 is a partial empty block, _P_ 1 = _V ⊕ X_<sup>¯</sup> 2 _,_ 1 _|EL_ ¯2( _V_ + 1) _⊕ X_<sup>¯</sup> 2 _,_ 2 _| . . . |EL_ ¯2( _V_ + _i_ ) _⊕ X_<sup>¯</sup> 2 _,i_ +1 

_P_ 2 = _CBC_ ( _W, pad_ ( _P_ 1) _X , L_ 3) _⊕ X_ 

_Q_ = _P_ 1 _|P_ 2 

_U_ = _LSBτ/_ 8( _Q_ ) 

- if ( _U_ ! = _Z_ ) _,_ return _⊥,_ otherwise _Q_ = _P_<sup>˜</sup> _|Z_ and return **Plaintext** _P, M_<sup>˜</sup> 

Figure 1.2: CMCC Mode Decryption - Stateless Version 

5 

## **Chapter 2** 

# **Security Goals** 

|goal|aes-cmcc v1,|aes-cmcc v1|aes-cmcc v1,|
|---|---|---|---|
||8 byte tag|4 byte tag|2 byte tag|
|confdentiality for plaintext|128|128|128|
|integrity for plaintext|64|32|16|
|integrity for Assoc. Data|64|32|16|
|integrity for PMN|64|32|16|

Table 2.1: Security goals: recommended parameters for stateless 

Table 2.1 gives the security strengths for the recommended parameters for the stateless case, but the integrity strengths do not include higher layer checks that act as authentication bits. These checks are protocol specific. The numbers in the table do not account for the case where the attacker is able to obtain messages encrypted under the key - see below for bounds for this latter case. 

The stateless case does not include a Secret Message Number (SMN). Although longer key lengths are possible (192 and 256 bits), the recommended key size for these parameter sets is 128 bits. 

#### **2.1 Additional Security Goals** 

In addition to authenticated encryption, CMCC has the following security goals: 

1. The cipher is designed to provide the maximum possible robustness against message-number reuse, i.e., that the cipher maintains full integrity and confidentiality, except for leaking collisions of (plaintext,associated data,secret message number,public message number) via collisions of ciphertexts. 

2. Ciphertext modification results in unpredictable changes to the plaintext; thus (a) modifications to a ciphertext will like cause a failure in higher level processing (resulting in session termination most likely) 

   - (b) data that is consumed immediately will be randomized and thus anomalous to the consuming agent, again causing alerts and/or session termination. 

6 

The implication of these properties is that, for many applications, the number of authentication bits that are part of the ciphertext can be reduced. The benefit is reduced network overhead. 

3. Stateful version: private message numbers will hide the number of messages previously sent. 

4. Stateful version: replay protection can be enforced by the receiver. 

##### **2.1.1 Resistance to Additional Specific Attacks** 

Here we discuss additional security features. 

1. Large number of legitimate messages encrypted, ciphertexts decrypted: Let _M_ be a bound on the maximum number of blocks in a query, _µ_ is the total number of blocks in the adversary queries, and _B_ is the cipher block length. CMCC encryption (stateless and stateful versions) is CCA2 MRAE secure for ( _ϵ, q_ ) with 

given that the adversary is restricted to _q_ queries, _α_ = 2<sup>_m_</sup> where _MinLen_ is the minimal bit length of the adversary queries and _m_ = _⌊MinLen/_ 2 _⌋, τ_ is the number of bits in the authentication tag, and _z ≤ q._ 

2. Relationships among keys and related key attacks: There are no key relationships (the keys are independent) and related key attacks are not a threat. 

3. Software and Hardware Side Channels: Note that encryption and decryption are both performed using AES encryption (not decryption) and that padding is never checked (both encryptor and decryptor will pad but neither will verify any padding). So there is no padding oracle. The adversary cannot manipulate ciphertext to produce specific plaintext relations or patterns so the adversary cannot learn information about the plaintext or keys from integrity failures. 

Specific implementations may be vulnerable to side channels based on observable differences arising from distinct keys or plaintexts. Thus developers should consider methods for minimizing side channels in implementations. 

7 

## **Chapter 3** 

##### **3.1.2 (Misuse Resistant) CCA Encryption** 

Given the symmetric key encryption scheme _S_ = ( _Gen, Enc, Dec_ ) _._ We define the CCA2 encryption experiment _ExpCCA_ 2( _S, n, q, A_ ) here: 

1. The algorithm _Gen_ (1<sup>_n_</sup> ) is run and the key _K_ is generated. 

2. The adversary _A_ is given the input 1<sup>_n_</sup> and oracle access to _EncK_ () and _DecK_ () _._ 

8 

3. The adversary outputs a pair of messages _m_ 0 and _m_ 1 of the same length. 

4. A random bit _b ←{_ 0 _,_ 1 _}_ is selected. The ciphertext _c ← EncK_ ( _mb_ ) is computed and given to _A._ 

5. The adversary continues to have oracle access to _EncK_ () and _DecK_ () _._ However, the adversary is not allowed to query the decryption oracle with the ciphertext _c._ The adversary is limited to _q_ total queries (including the queries issued before the challenge ciphertext is generated). 

6. The adversary outputs a bit<sup>¯</sup> _b._ The output of the experiment is 1 if<sup>¯</sup> _b_ = _b_ and 0 otherwise. 

Inputs to _EncK_ () are of the form ( _P, M_ ) _,_ and inputs to _DecK_ () are of the form ( _C, M_ ) where _M_ is a message number, and the adversary may not reuse _M_ with the same key. If _DecK_ ( _C, M_ ) = _P,_ for adversary query ( _C, M_ ) _,_ then the adversary will not subsequently submit ( _P, M_ ) to _EncK_ () _._ 

The encryption scheme _S_ is defined to have CCA2 security for ( _ϵ, q_ ) if for all probabilistic polynomial time adversaries _A_ limited to _q_ queries, _Pr_ [ _ExpCCA_ 2( _S, n, q, A_ ) = 1] _≤_ 1 _/_ 2 + _ϵ._ We define _AdvS,n,q_<sup>_CCA_2(</sup><sup>_A_) = [</sup><sup>_Pr_[</sup><sup>_ExpCCA_2(</sup><sup>_S, n, q, A_) = 1]</sup><sup>_−_1</sup><sup>_/_2</sup><sup>_._</sup> 

We also define the CCA2 MRAE security experiment which is identical to the experiment above except the adversary may reuse the message number _M_ with the same key. However, no query can be submitted twice. In particular, _m_ 0 and _m_ 1 must be new queries. The encryption scheme _S_ is defined to have CCA2 MRAE security for ( _ϵ, q_ ) if for all probabilistic polynomial time adversaries _A_ limited to _q_ queries, _Pr_ [ _ExpCCA_ 2 _~~M~~ RAE_<sup>(</sup><sup>_S, n, q, A_)=1]</sup><sup>_≤_1</sup><sup>_/_2 +</sup><sup>_ϵ._Wedefine</sup> _AdvS,n,q_<sup>_CCA_2</sup> _~~M~~ RAE_ ( _A_ ) = [ _Pr_ [ _ExpCCA_ 2 _~~M~~ RAE_<sup>(</sup><sup>_S, n, q, A_) = 1]</sup><sup>_−_1</sup><sup>_/_2</sup><sup>_._</sup> 

##### **3.1.3 (Misuse Resistant) CPA Encryption** 

Given the CCA2 encryption experiment above, except we remove the decryption oracle from the experiment. We define the resulting experiment as the CPA encryption experiment, and if the adversary probability of success is bounded as above, we say that the encryption scheme is CPA secure for ( _ϵ, q_ ) _._ We have the analogous definitions for _AdvS,n,q_<sup>_CPA_(</sup><sup>_A_)and</sup><sup>_Adv_</sup> _S,n,q_<sup>_CPA_</sup> _MRAE_ ( _A_ ) _._ 

## **Chapter 4**