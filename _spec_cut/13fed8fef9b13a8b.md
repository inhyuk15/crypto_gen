### **TinyJAMBU: A Family of Lightweight Authenticated Encryption Algorithms** 

Designers and Submitters: Hongjun Wu and Tao Huang 

Division of Mathematical Sciences Nanyang Technological University wuhongjun@gmail.com 

27 September 2019 

# **Contents** 

|**1**|**Intr**|**oduction**<br>**3**|
|---|---|---|
|**2**|**Tin**|**yJAMBU Authenticated Encryption Mode**<br>**4**|
|**3**|**Spe**|**cifcation**<br>**5**|
||3.1|Recommended parameter sets . . . . . . . . . . . . . . . . . . . .<br>5|
||3.2|Operations, Variables and Functions . . . . . . . . . . . . . . . .<br>5|
|||3.2.1<br>Operations<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>5|
|||3.2.2<br>Variables and Constants . . . . . . . . . . . . . . . . . . .<br>6|
|||3.2.3<br>The Keyed Permutation _Pn_ . . . . . . . . . . . . . . . . .<br>7|
||3.3|TinyJAMBU-128 . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>7|
|||3.3.1<br>The initialization . . . . . . . . . . . . . . . . . . . . . . .<br>7|
|||3.3.2<br>Processing the associated data<br>. . . . . . . . . . . . . . .<br>8|
|||3.3.3<br>The encryption . . . . . . . . . . . . . . . . . . . . . . . .<br>9|
|||3.3.4<br>The fnalization . . . . . . . . . . . . . . . . . . . . . . . .<br>9|
|||3.3.5<br>The decryption . . . . . . . . . . . . . . . . . . . . . . . .<br>10|
|||3.3.6<br>The verifcation . . . . . . . . . . . . . . . . . . . . . . . .<br>10|
||3.4|TinyJAMBU-192 . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>11|
||3.5|TinyJAMBU-256 . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>11|
|**4**|**Sec**|**urity Goals**<br>**12**|
||4.1|Security goals with unique nonce . . . . . . . . . . . . . . . . . .<br>12|
||4.2|Security goals with misused nonce<br>. . . . . . . . . . . . . . . . .<br>13|
|**5**|**Sec**|**urity of the TinyJAMBU Mode**<br>**14**|
||5.1|Security Model . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>14|
||5.2|Privacy<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>15|
||5.3|Authenticity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>16|
|**6**|**Sec**|**urity Analysis**<br>**20**|
||6.1|Properties of the TinyJAMBU Mode . . . . . . . . . . . . . . . .<br>20|
|||6.1.1<br>State collision for unique nonce . . . . . . . . . . . . . . .<br>20|
|||6.1.2<br>State collision for repeated nonce . . . . . . . . . . . . . .<br>20|
||6.2|Properties of the Keyed Permutation _Pn_ . . . . . . . . . . . . . .<br>21|

1 

|||6.2.1<br>Diferential properties of the keyed permutation _Pn_ . . . .<br>21|
|---|---|---|
|||6.2.2<br>Linear properties of the keyed permutation _Pn_<br>. . . . . .<br>23|
|||6.2.3<br>Algebraic properties of the keyed permutation _Pn_ . . . . .<br>23|
||6.3|Forgery Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>23|
|||6.3.1<br>Forgery attacks on nonce and associated data . . . . . . .<br>24|
|||6.3.2<br>Forgery attacks on plaintext/ciphertext<br>. . . . . . . . . .<br>24|
||6.4|Key Recovery Attacks . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
|||6.4.1<br>Diferential cryptanalysis<br>. . . . . . . . . . . . . . . . . .<br>25|
|||6.4.2<br>Linear cryptanalysis . . . . . . . . . . . . . . . . . . . . .<br>26|
|||6.4.3<br>Algebraic attacks . . . . . . . . . . . . . . . . . . . . . . .<br>26|
||6.5|Slide attack . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>26|
|**7**|**The **|**Performance of TinyJAMBU**<br>**27**|
||7.1|Hardware Performance . . . . . . . . . . . . . . . . . . . . . . . .<br>27|
||7.2|Software Performance<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>28|
|**8**|**Feat**|**ures**<br>**30**|
|**9**|**Des**|**ign Rationale**<br>**31**|
|**A **|**Ana**|**lysis of the Probability for Equation 5.2**<br>**36**|

2 

## **Chapter 1** 

# **Chapter 2 TinyJAMBU Authenticated Encryption Mode** 

The TinyJAMBU mode is a small variant of the JAMBU mode which is a third-round candidate of the CAESAR competition. In the TinyJAMBU mode, a 128-bit keyed permutation is used, the state size is 128 its, and the message block size is 32 bits. When nonce is reused, the TinyJAMBU mode provides better authentication security than the JAMBU mode. 

When nonce is reused, the TinyJAMBU mode provides better authentication security than the Duplex mode (for the same permutation size and the same message block size). The reason is that the attacker can easily set part of the state to arbitrary value when nonce is reused in the Duplex mode, while it is difficult to do that in the TinyJAMBU mode. 

The TinyJAMBU mode is shown in Fig. 2.1. If the last block of the associated data (or plaintext) is not a full block , the length of the partial block (the number of bytes) is xored to the state. 

Figure 2.1: The TinyJAMBU mode for 128-bit state and keyed-permutations 

4 

## **Chapter 3** 

# **Specification** 

#### **3.1 Recommended parameter sets** 

TinyJAMBU supports three key sizes: 128 bits, 192 bits and 256 bits. 

- Primary member: TinyJAMBU-128 128-bit key, 96-bit nonce, 64-bit tag, 128-bit state 

- TinyJAMBU-192 

- 192-bit key, 96-bit nonce, 64-bit tag, 128-bit state 

- TinyJAMBU-256 

- 256-bit key, 96-bit nonce, 64-bit tag, 128-bit state 

#### **3.2 Operations, Variables and Functions** 

The operations, variables and functions used in TinyJAMBU are defined below. 

##### **3.2.1 Operations** 

The following operations are used in the description of TinyJAMBU: 

- _⊕_ : bit-wise exclusive OR & : bit-wise AND _∼_ : bit-wise NOT _∥_ : concatenation 

- _⌊a⌋_ : floor operator, gives the integer part of _a_ 

5 

##### **3.2.2 Variables and Constants** 

The following variables and constants are used in TinyJAMBU: 

|_a{i···j}_|:|the word consists of _ai||ai_+1_|| · · · ∥aj_, where _ai_ is the _i_th<br>bit of _a_.|
|---|---|---|
|_AD_|:|associated data, a sequence of bytes.|
|_adi_|:|one bit of associated data.|
|_adlen_|:|the length of associated data in bits.|
|_C_|:|ciphertext, a sequence of bytes|
|_ci_|:|the _i_th ciphertext bit.|
|_FrameBits_|:|Three-bit FrameBits.|
|||FrameBits = 1 for nonce|
|||FrameBits = 3 for associated data|
|||FrameBits = 5 for plaintext and ciphertext|
|||FrameBits = 7 for fnalization|
|_FrameBitsi_|:|The _i_th bit of FrameBits.|
|_K_|:|the key.|
|_ki_|:|the _i_th bit of _K_.|
|_klen_|:|the key length in bits.|
|_M_|:|the plaintext, a sequence of bytes|
|_mi_|:|the _i_th bit of the plaintext.|
|_mlen_|:|the length of the plaintext in bits.|
|NONCE|:|the 96-bit nonce.|
|nonce_i_|:|the _i_th bit of the 96-bit nonce.|
|_Pn_|:|the 128-bit permutation with _n_ rounds|
|_S_|:|the 128-bit state of the permutation.|
|_si_|:|the _i_th bit of the state of the permutation.|
|_T_|:|the 64-bit authentication tag.|
|_ti_|:|the _i_th bit of the authentication tag.|

6 

##### **3.2.3 The Keyed Permutation** _Pn_ 

In TinyJAMBU, a 128-bit keyed permutation is used. The permutation _Pn_ consists of _n_ rounds. In the _i_ th round of the permutation, a 128-bit nonlinear feedback shift register is used to update the state as follows (shown in Fig. 3.1): 

StateUpdate( _S, K, i_ ): 

feedback = _s_ 0 _⊕ s_ 47 _⊕_ ( _∼_ ( _s_ 70& _s_ 85)) _⊕ s_ 91 _⊕ ki_ mod _klen_ for _j_ from 0 to 126: _sj_ = _sj_ +1 _s_ 127 = feedback 

end 

For example, _P_ 384 means that the state of the permutation is updated using the function StateUpdate() for 384 times. 32 rounds of the permutation can be computed in parallel on 32-bit CPU. 

Figure 3.1: The 128-bit Nonlinear Feedback Shift Register in TinyJAMBU 

#### **3.3 TinyJAMBU-128** 

TinyJAMBU-128 uses a 128-bit key and a 96-bit nonce. The associated data length and the plaintext length are less than 2<sup>50</sup> bytes. The authentication tag is 64-bit. The TinyJAMBU authenticated encryption mode is used in TinyJAMBU-128. 

##### **3.3.1 The initialization** 

In the keyed permutation of TinyJAMBU-128, the 128-bit key of TinyJAMBU128 is used, and the _klen_ is set to 128. 

The initialization of TinyJAMBU-128 consists of two stages: key setup and nonce setup. 

**Key Setup.** The key setup is to randomize the state using the keyed permutation _P_ 1024. 

1. Set the 128-bit state _S_ as 0. 

2. Update the state using _P_ 1024. 

7 

**Nonce Setup.** The nonce setup consists of three steps. In each step, the Framebits of nonce (the value is 1) are XORed with the state, then we update the state using the keyed permutation _P_ 384, then 32 bits of the nonce are XORed with the state. 

for _i_ from 0 to 2: 

_s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 384 _s{_ 96 _···_ 127 _}_ = _s{_ 96 _···_ 127 _} ⊕ nonce{_ 32 _i···_ 32 _i_ +31 _}_ end for 

##### **3.3.2 Processing the associated data** 

After the initialization, we process the associated data _AD_ . In each step, the Framebits of associated data (the value is 3) are XORed with the state, then we update the state using the keyed permutation _P_ 384, then 32 bits of the associated data are XORed with the state. 

**Processing the full blocks of associated data:** 

for _i_ from 0 to _⌊adlen/_ 32 _⌋_ : _s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 384 _s{_ 96 _···_ 127 _}_ = _s{_ 96 _···_ 127 _} ⊕ ad{_ 32 _i···_ 32 _i_ +31 _}_ end for 

**Processing the partial block of associated data.** If the last block is not a full block (it is called a partial block), the last block is XORed to the state, and the number of bytes of associated data in the partial block is XORed to the state. 

if ( _adlen_ mod 32) _>_ 0: _s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 384 _lenp_ = _adlen_ mod 32 /* number of bits in the partial block */ _startp_ = _adlen − lenp_ /* starting position of the partial block */ _s{_ 96 _···_ 96+ _lenp−_ 1 _}_ = _s{_ 96 _···_ 96+ _lenp−_ 1 _} ⊕ ad{startp···adlen−_ 1 _}_ /* the number of bytes in the partial block is XORed to the state*/ _s{_ 32 _···_ 33 _}_ = _s{_ 32 _···_ 33 _} ⊕_ ( _lenp/_ 8) end if 

8 

##### **3.3.3 The encryption** 

After processing the associated data, we encrypt the plaintext _M_ . In each step, the Framebits of plaintext (the value is 5) are XORed with the state, then we update the state using the keyed permutation _P_ 1024, then 32 bits of the plaintext are XORed with the state, and we obtain 32 bits of ciphertext by XORing the plaintext with another part of the state. 

**Processing the full blocks of plaintext:** 

for _i_ from 0 to _⌊mlen/_ 32 _⌋_ : _s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 1024 _s{_ 96 _···_ 127 _}_ = _s{_ 96 _···_ 127 _} ⊕ m{_ 32 _i···_ 32 _i_ +31 _} c{_ 32 _i···_ 32 _i_ +31 _}_ = _s{_ 64 _···_ 95 _} ⊕ m{_ 32 _i···_ 32 _i_ +31 _}_ end for 

**Processing the partial block of plaintext.** If the last block is not a full block (it is a partial block), the last block is XORed to the state, and the number of bytes in the partial block is XORed to the state. 

if ( _mlen_ mod 32) _>_ 0: _s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 1024 _lenp_ = _mlen_ mod 32 /* number of bits in partial block */ _startp_ = _mlen − lenp_ /* starting position of partial block */ _s{_ 96 _···_ 96+ _lenp−_ 1 _}_ = _s{_ 96 _···_ 96+ _lenp−_ 1 _} ⊕ m{startp···mlen−_ 1 _} c{startp···mlen−_ 1 _}_ = _s{_ 64 _···_ 64+ _lenp−_ 1 _} ⊕ m{startp···mlen−_ 1 _}_ /* the length (bytes) of the last partial block is XORed to the state*/ _s{_ 32 _···_ 33 _}_ = _s{_ 32 _···_ 33 _} ⊕_ ( _lenp/_ 8) end if 

##### **3.3.4 The** 

After encrypting the plaintext, we generate the 64-bit authentication tag _T_ as follows. The Framebits of finalization (the value is 7) are XORed with the state. 

_s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 1024 _t{_ 0 _···_ 31 _}_ = _s{_ 64 _···_ 95 _} s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 384 _t{_ 32 _···_ 63 _}_ = _s{_ 64 _···_ 95 _}_ 

9 

##### **3.3.5 The decryption** 

In a decryption process, the initialization and processing the associate data are the same as the encryption process. After processing the associated data, we decrypt the ciphertext _C_ . In each step, the Framebits of plaintext (the value is 5) are XORed with the state, then we update the state using the keyed permutation _P_ 1024. We obtain 32 bits of plaintext by XORing the ciphertext with 32 state bits _s{_ 64 _···_ 95 _}_ , then the plaintext is XORed with the state bits _s{_ 96 _···_ 127 _}_ . 

**Processing the full blocks of ciphertext:** 

for _i_ from 0 to _⌊mlen/_ 32 _⌋_ : _s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 1024 _m{_ 32 _i···_ 32 _i_ +31 _}_ = _s{_ 64 _···_ 95 _} ⊕ c{_ 32 _i···_ 32 _i_ +31 _} s{_ 96 _···_ 127 _}_ = _s{_ 96 _···_ 127 _} ⊕ m{_ 32 _i···_ 32 _i_ +31 _}_ end for 

**Processing the partial block of ciphertext.** If the last block is not a full block (it is a partial block), the number of bytes in the partial block is XORed to the state. 

if ( _mlen_ mod 32) _>_ 0: _s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 1024 _lenp_ = _mlen_ mod 32 /* number of bits in partial block */ _startp_ = _mlen − lenp_ /* starting position of partial block */ _m{startp···mlen−_ 1 _}_ = _s{_ 64 _···_ 64+ _lenp−_ 1 _} ⊕ c{startp···mlen−_ 1 _} s{_ 96 _···_ 96+ _lenp−_ 1 _}_ = _s{_ 96 _···_ 96+ _lenp−_ 1 _} ⊕ m{startp···mlen−_ 1 _}_ /* the length (bytes) of the last partial block is XORed to the state*/ _s{_ 32 _···_ 33 _}_ = _s{_ 32 _···_ 33 _} ⊕_ ( _lenp/_ 8) end if 

##### **3.3.6 The** 

After decrypting the plaintext, we generate a 64-bit authentication tag _T_<sup>_′_</sup> , then compare _T_<sup>_′_</sup> with the received tag _T_ . The Framebits of finalization are of value 7. 

_s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 1024 _t_<sup>_′_</sup> _{_ 0 _···_ 31 _}_<sup>=</sup><sup>_s{_64</sup><sup>_···_95</sup><sup>_}_</sup> _s{_ 36 _···_ 38 _}_ = _s{_ 36 _···_ 38 _} ⊕ FrameBits{_ 0 _···_ 2 _}_ Update the state using _P_ 384 _t_<sup>_′_</sup> _{_ 32 _···_ 63 _}_<sup>=</sup><sup>_s{_64</sup><sup>_···_95</sup><sup>_}_</sup> _T_<sup>_′_</sup> = _t_<sup>_′_</sup> _{_ 0 _···_ 63 _}_<sup>.Acceptthemessageif</sup><sup>_T ′_=</sup><sup>_T_;otherwise,reject.</sup> 

10 

#### **3.4 TinyJAMBU-192** 

TinyJAMBU-192 uses a 192-bit key and a 96-bit nonce. The associated data length and the plaintext length are less than 2<sup>50</sup> bytes. The authentication tag is 64-bit. 

The design of TinyJAMBU-192 is similar to that of TinyJAMBU-128. The differences between TinyJAMBU-192 and TinyJAMBU-128 are given below. 

**Keyed Permutation.** In the keyed permutation of TinyJAMBU-192, a 192-bit key is used, and the _klen_ is set to 192. 

The keyed permutation _P_ 1024 in TinyJAMBU-128 is replaced with _P_ 1152 in TinyJAMBU-256. _P_ 384 in TinyJAMBU-128 is still _P_ 384 in TinyJAMBU-192. 

#### **3.5 TinyJAMBU-256** 

TinyJAMBU-256 uses a 256-bit key and a 96-bit nonce. The associated data length and the plaintext length are less than 2<sup>50</sup> bytes. The authentication tag is 64-bit. 

The design of TinyJAMBU-256 is similar to that of TinyJAMBU-128. The differences between TinyJAMBU-256 and TinyJAMBU-128 are given below. 

**Keyed Permutation.** In the keyed permutation of TinyJAMBU-256, a 256-bit key is used, and the _klen_ is set to 256. 

The keyed permutation _P_ 1024 in TinyJAMBU-128 is replaced with _P_ 1280 in TinyJAMBU-256. _P_ 384 in TinyJAMBU-128 is still _P_ 384 in TinyJAMBU-256. 

11 

## **Chapter 4** 

# **Security Goals** 

In TinyJAMBU, each pair of key and nonce is used to protect only one message. If verification fails, the new tag and the decrypted plaintext should not be given as output. 

In TinyJAMBU, the associated data plays the same role as nonce. When the same nonce but different associated data are used for a key, it is equivalent to the use of unique nonce for the key. 

The nonce misuse happens when the same nonce and the same associated data are reused for a key. When nonce is misused, TinyJAMBU provides strong protection of the secret key, and provides strong authentication security, but provides weak protection of the plaintext. 

#### **4.1 Security goals with unique nonce** 

The security goals of TinyJAMBU for unique nonce are given in Table 4.1. We assume that each each key is used to process at most 2<sup>50</sup> byes of messages (associated data, plaintext/ciphertext), and each message is at least 8 bytes. Note that the authentication security in Table 4.1 includes the integrity security of plaintext, associated data and nonce. 

Table 4.1: Security Goals of TinyJAMBU with Unique Nonce 

||Encryption|Authentication|
|---|---|---|
|TinyJAMBU-128|112-bit|64-bit|
|TinyJAMBU-192|168-bit|64-bit|
|TinyJAMBU-256|224-bit|64-bit|

12 

#### **4.2 Security goals with misused nonce** 

When nonce is misused in TinyJAMBU (the same nonce and the same associated data are reused for a key), the secret key of TinyJAMBU remains strong, and the authentication of TinyJAMBU remains strong (suppose that a secret key is used to process at most 2<sup>50</sup> bytes of data, and each message consists of at least 8 bytes of data). 

When nonce is reused, an attacker is able to decrypt the ciphertext since the encryption of TinyJAMBU is somehow similar to the Cipher Feedback mode. The security goals of TinyJAMBU for reused nonce are given in Table 4.2. 

Table 4.2: Security Goals of TinyJAMBU with Repeated Nonce (an adversary has the maximum forgery advantage when a key was used to process adaptively chosen 2<sup>50</sup> bytes of data, and each message is at least 8 bytes) 

||Secret Key|Authentication|Max. Forgery Adv.|
|---|---|---|---|
|TinyJAMBU-128|112-bit|64-bit|2<sup>_−_15</sup>|
|TinyJAMBU-192|168-bit|64-bit|2<sup>_−_15</sup>|
|TinyJAMBU-256|224-bit|64-bit|2<sup>_−_15</sup>|

13 

#### **6.2 Properties of the Keyed Permutation** _Pn_ 

In the following, we will analyse the differential, linear and algebraic properties of the keyed permutation _Pn_ . 

##### **6.2.1 Differential properties of the keyed permutation** _Pn_ 

In this section, we analyse the differential properties [2, 4] of the TinyJAMBU permutation _Pn_ . The following three types of differences will be analysed. 

- Type 1. Input differences at _S_ 96 _···_ 127 

- Type 2. Arbitrary input differences, output differences at _S_ 96 _···_ 127 

- Type 3. Input differences at _S_ 96 _···_ 127 , output differences at _S_ 96 _···_ 127 

- Type 4. Arbitrary input differences, arbitrary output differences 

In the following, we will analyse the differential propagation using the Mixed Integer Linear Programming (MILP) [13]. We use the Gurobi optimizer [8] to find the bounds for the permutations. 

###### **Type 1 Differences** 

For the Type 1 differences, the input differences are at _S_ 96 _···_ 127, and there is no restriction on the output differences. The largest differential probabilities of the Type 1 differences are summarized in Table 6.1. 

21 

Table 6.1: Type 1 Differential Properties of _Pn_ 

|Round|Probability|Method|
|---|---|---|
|256|2<sup>_−_22</sup>|MILP|
|320|2<sup>_−_33</sup>|MILP|
|384|2<sup>_−_45</sup>|MILP|
|448|2<sup>_−_55</sup>|MILP|
|512|2<sup>_−_68</sup>|MILP|

###### **Type 2 Differences** 

For the Type 2 differences, there is no restriction on the input differences, and output differences are at _S_ 96 _···_ 127. The largest differential probabilities of the Type 2 differences are summarized in Table 6.2. 

Table 6.2: Type 2 Differential Properties of _Pn_ 

|Round|Probability|Method|
|---|---|---|
|384|2<sup>_−_28</sup>|MILP|
|512|2<sup>_−_47</sup>|MILP|

###### **Type 3 Differences** 

For the Type 3 differences, the input differences are at _S_ 96 _···_ 127, and output differences are at _S_ 96 _···_ 127. The largest differential probabilities of the Type 3 differences are summarized in Table 6.3. 

Table 6.3: Type 3 Differential Properties of _Pn_ 

|Round|Probability|Method|
|---|---|---|
|384|2<sup>_−_80</sup>|MILP|

###### **Type 4 Differences** 

For the Type 4 differences, there is no constraint on the input differences and output differences. The largest differential probabilities of the Type 4 differences are summarized in Table 6.4. 

22 

Table 6.4: Type 4 Differential Properties of _Pn_ 

|Round|Probability|Method|
|---|---|---|
|192|2<sup>_−_4</sup>|MILP|
|320|2<sup>_−_13</sup>|MILP|

##### **6.2.2 Linear properties of the keyed permutation** _Pn_ 

In this section, we analyse the linear properties [11, 12] of the TinyJAMBU permutation _Pn_ . The linear bias being analsed is for arbitrary input bits and output bits at _S_ 64 _···_ 95. 

In the analysis, we use the Mixed Integer Linear Programming (MILP) [13]. We will use the Gurobi optimizer [8] to find the linear bias of the permutations. The results are summarized in Table 6.5. 

Table <u>6.5:</u> Linear bias of _Pn_ 

|Round|Bias|
|---|---|
|256|2<sup>_−_13</sup>|
|320|2<sup>_−_17</sup>|
|384|2<sup>_−_23</sup>|
|448|2<sup>_−_27</sup>|
|512|2<sup>_−_30</sup>|

##### **6.2.3 Algebraic properties of the keyed permutation** _Pn_ 

We consider the algebraic property for the input bits at _S_ 96 _···_ 127. Our experiment shows that after 598 rounds, every output bit at _S_ 64 _···_ 95 is affected by the 32-bit input cube tester [7] at _S_ 96 _···_ 127 . 

#### **6.5 Slide attack** 

The slide attack [3] is an effective tool to analyse the cipher with self-similarity round functions. Although TinyJAMBU permutation has the sliding property, the frame bits being added to the state will prevent the slide attack since the position of the frame bits is fixed. For example, for two related keys with slide property, the slide property between the two states gets eliminated with the introduction of Framebits of nonce. 

26 

# **Analysis of the Probability for Equation 5.2** 

Here we show how to derive the maximum probability for Equation 5.2 with minimum required message blocks. The equation is given below. 

First, we ignore the min function, so the right hand side becomes: 

Let _z_ =<sup>�</sup> _i_ = _j,_ 1 _≤i,j≤θ_<sup>_βiβj_,wehave</sup> 

Then, 

Add 2 _z_ to both size, we have 

36 

Therefore, 

_θ z ≤_<sup><u>(</u></sup><sup>_θ −_</sup> 2 _θ_<sup>1)</sup> (� _βi_ )<sup>2</sup> _._ (A.1) _i_ =1 

probability reduce even more. 

Therefore, the _βi_ = _βj ≥_ 2<sup>_v/_2</sup> will obtain the maximum value of probability with least number of message blocks<sup>�</sup><sup>_θ_</sup> _i_ =1<sup>_βi_.Anydecreaseinthechoiceof</sup> _θ_ � _i_ =1<sup>_βi_willdecreasetheprobabilityinasquaredmanner.</sup> 

37