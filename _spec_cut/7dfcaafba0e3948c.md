### **ACORN: A Lightweight Authenticated Cipher (v2)** 

Designer and Submitter: Hongjun Wu 

Division of Mathematical Sciences Nanyang Technological University wuhongjun@gmail.com 

2015.08.29 

# **Contents** 

|**1**|**Spe**|**cifcation**<br>**2**|
|---|---|---|
||1.1|Recommended parameter sets . . . . . . . . . . . . . . . . . . . .<br>2|
||1.2|Operations, Variables and Functions . . . . . . . . . . . . . . . .<br>2|
|||1.2.1<br>Operations<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>2|
|||1.2.2<br>Variables and constants . . . . . . . . . . . . . . . . . . .<br>2|
|||1.2.3<br>Functions . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
||1.3|ACORN-128<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>3|
|||1.3.1<br>The state of ACORN-128 . . . . . . . . . . . . . . . . . .<br>3|
|||1.3.2<br>The functions of ACORN-128 . . . . . . . . . . . . . . . .<br>3|
|||1.3.3<br>The initialization of ACORN-128 . . . . . . . . . . . . . .<br>4|
|||1.3.4<br>Processing the associated data<br>. . . . . . . . . . . . . . .<br>5|
|||1.3.5<br>The encryption . . . . . . . . . . . . . . . . . . . . . . . .<br>5|
|||1.3.6<br>The fnalization . . . . . . . . . . . . . . . . . . . . . . . .<br>6|
|||1.3.7<br>The decryption and verifcation . . . . . . . . . . . . . . .<br>6|
|**2**|**Sec**|**urity Goals**<br>**7**|
|**3**|**Sec**|**urity Analysis**<br>**8**|
||3.1|The security of the initialization<br>. . . . . . . . . . . . . . . . . .<br>9|
||3.2|The security of the encryption process . . . . . . . . . . . . . . .<br>9|
||3.3|The security of message authentication . . . . . . . . . . . . . . .<br>9|
|**4**|**Fea**|**tures**<br>**11**|
|**5**|**The**|**Performance of ACORN**<br>**12**|
|**6**|**Des**|**ign Rationale**<br>**13**|
|**7**|**No **|**Hidden Weakness**<br>**15**|
|**8**|**Inte**|**llectual property**<br>**16**|
|**9**|**Con**|**sent**<br>**17**|
|**10 **|**Cha**|**nges**<br>**18**|

1 

## **Chapter 1** 

# **Specification** 

The specifications of ACORN-128 are given in this chapter. 

#### **1.1 Recommended parameter sets** 

- Primary Recommendation: ACORN-128 128-bit key, 128-bit nonce, 128-bit tag 

#### **1.2 Operations, Variables and Functions** 

The operations, variables and functions used in ACORN are defined below. 

##### **1.2.1 Operations** 

The following operations are used in ACORN: 

_⊕_ : bit-wise exclusive OR & : bit-wise AND _∼_ : bit-wise NOT _∥_ : concatenation _⌈x⌉_ : ceiling operation, _⌈x⌉_ is the smallest integer not less than _x_ 

##### **1.2.2 Variables and constants** 

The following variables and constants are used in ACORN: 

_AD_ : associated data (this data will not be encrypted or decrypted). _adi_ : one bit of associated data block. _adlen_ : bit length of the associated data with 0 _≤ adlen <_ 2<sup>64</sup> . _C_ : ciphertext. _ci_ : one ciphertext bit. 

2 

- _cai_ : a control bit at the _i_ th step. It is used to separate the processing of associated data, the processing of plaintext, and the generation of authentication tag. 

- _cbi_ : another control bit at the _i_ th step. It is used to allow a keystream bit to affect a feedback bit during initialization, processing of associated data, and the tag generation. 

- _IV_ 128 : 128-bit initialization vector of ACORN-128. _IV_ 128 _,i_ : the _i_ th bit of _IV_ 128. _K_ 128 : 128-bit key of ACORN-128. _K_ 128 _,i_ : the _i_ th bit of _K_ 128. _ksi_ : The keystream bit generated at the _i_ th step. _pclen_ : bit length of the plaintext/ciphertext with 0 _≤ pclen <_ 2<sup>64</sup> . _mi_ : one data bit. _P_ : plaintext. _pi_ : one plaintext bit. _Si_ : state at the beginning of the _i_ th step. _Si,j_ : _j_ th bit of state _Si ._ For ACORN-128, 0 _≤ j ≤_ 292. _T_ : authentication tag. _t_ : bit length of the authentication tag with 64 _≤ t ≤_ 128. 

##### **1.2.3 Functions** 

Two Boolean functions are used in ACORN: _maj_ and _ch_ . 

_maj_ ( _x, y, z_ ) = ( _x_ & _y_ ) _⊕_ ( _x_ & _z_ ) _⊕_ ( _y_ & _z_ ) ; _ch_ ( _x, y, z_ ) = ( _x_ & _y_ ) _⊕_ (( _∼ x_ )& _z_ ) ; 

#### **1.3 ACORN-128** 

ACORN-128 uses a 128-bit key and a 128-bit initialization vector. The associated data length and the plaintext length are less than 2<sup>64</sup> bits. The authentication tag length is less than or equal to 128 bits. We strongly recommend the use of a 128-bit tag. 

##### **1.3.1 The state of ACORN-128** 

The state size of ACORN-128 is 293 bits. There are six LFSRs being concatenated in ACORN-128. The state is shown in Fig.1.1. 

##### **1.3.2 The functions of ACORN-128** 

There are three functions in ACORN-128: the function to generate keystream bit from the state, the function to compute the overall feedback bit, and the function to update the state. 

3 

Figure 1.1: The concatenation of 6 LFSRs in ACORN-128. _fi_ indicates the overall feedback bit for the _i_ th step; _mi_ indicates the message bit for the _i_ th step. 

**Generate the Keystream Bit.** At each step, the keystream bit is computed using the function _ksi_ = _KSG_ 128( _Si_ ) : 

**Compute the Feedback Bit.** At each step, the feedback bit is computed using the function _fi_ = _FBK_ 128( _Si, cai, cbi_ ) : 

_ksi_ = _KSG_ 128( _Si_ ) ; _fi_ = _Si,_ 0 _⊕_ ( _∼Si,_ 107) _⊕maj_ ( _Si,_ 244 _, Si,_ 23 _, Si,_ 160) _⊕ch_ ( _Si,_ 230 _, Si,_ 111 _, Si,_ 66) _⊕_ ( _cai_ & _Si,_ 196) _⊕_ ( _cbi_ & _ksi_ ) ; 

**The State Update Function.** At each step, the pseudo code for the state update function _Si_ +1 = StateUpdate128( _Si_ , _mi_ , _cai_ , _cbi_ ) is given as : 

_Si,_ 289 = _Si,_ 289 _⊕ Si,_ 235 _⊕ Si,_ 230; _Si,_ 230 = _Si,_ 230 _⊕ Si,_ 196 _⊕ Si,_ 193; _Si,_ 193 = _Si,_ 193 _⊕ Si,_ 160 _⊕ Si,_ 154; _Si,_ 154 = _Si,_ 154 _⊕ Si,_ 111 _⊕ Si,_ 107; _Si,_ 107 = _Si,_ 107 _⊕ Si,_ 66 _⊕ Si,_ 61; _Si,_ 61 = _Si,_ 61 _⊕ Si,_ 23 _⊕ Si,_ 0; _fi_ = _FBK_ 128( _Si, cai, cbi_ ) ; 

for _j_ := 0 to 291 do _Si_ +1 _,j_ = _Si,j_ +1 ; _Si_ +1 _,_ 292 = _fi ⊕ mi_ ; 

##### **1.3.3 The initialization of ACORN-128** 

The initialization of ACORN-128 consists of loading the key and _IV_ into the state, and running the cipher for 1792 steps. 

1. Initialize the state _S−_ 1792 to 0. 

2. Let _m−_ 1792+ _i_ = _K_ 128 _,i_ for _i_ = 0 to 127; Let _m−_ 1792+128+ _i_ = _IV_ 128 _,i_ for _i_ = 0 to 127; 

4 

Let _m−_ 1792+256 = _K_ 128 _,i_ mod 128 _⊕_ 1 for _i_ = 0; Let _m−_ 1792+256+ _i_ = _K_ 128 _,i_ mod 128 for _i_ = 1 to 1535; 

3. Let _ca−_ 1792+ _i_ = 1 for _i_ = 0 to 1791; Let _cb−_ 1792+ _i_ = 1 for _i_ = 0 to 1791; 

4. for _i_ = _−_ 1792 to _−_ 1, _Si_ +1 = StateUpdate128( _Si_ , _mi_ , _cai_ , _cbi_ ); 

Note that in the initialization, the keystream bit is used to update the state since _cbi_ = 1. 

##### **1.3.4 Processing the associated data** 

After the initialization, the associated data _AD_ is used to update the state. 

1. Let _mi_ = _adi_ for _i_ = 0 to _adlen −_ 1; Let _madlen_ = 1; Let _madlen_ + _i_ = 0 for _i_ = 1 to 255; 

2. Let _cai_ = 1 for _i_ = 0 to adlen+127; Let _cai_ = 0 for _i_ = adlen+128 to adlen+255; Let _cbi_ = 1 for _i_ = 0 to adlen+255; 

3. for _i_ = 0 to _adlen_ + 255, _Si_ +1 = StateUpdate128( _Si_ , _mi_ , _cai_ , _cbi_ ); 

Note that even when there is no associated data, we still need to run the cipher for 256 steps. When we process the associated data, the keystream bit is used to update the state since _cbi_ = 1. The cipher specification is changed for 128 steps (since the value of _cai_ is set to 0 for 128 steps) so as to separate the associate data from the plaintext/ciphertext. 

##### **1.3.5 The encryption** 

After processing the associated data, at each step of the encryption, one plaintext bit _pi_ is used to update the state, and _pi_ is encrypted to _ci_ . 

1. Let _madlen_ +256+ _i_ = _pi_ for _i_ = 0 to _pclen −_ 1; Let _madlen_ +256+ _pclen_ = 1; Let _madlen_ +256+ _pclen_ + _i_ = 0 for _i_ = 1 to 255; 

2. Let _cai_ = 1 for _i_ = _adlen_ + 256 to _adlen_ + _pclen_ + 383; Let _cai_ = 0 for _i_ = _adlen_ + _pclen_ + 384 to _adlen_ + _pclen_ + 511; Let _cbi_ = 0 for _i_ = _adlen_ + 256 to _adlen_ + _pclen_ + 511; 

3. for _i_ = _adlen_ + 256 to _adlen_ + _pclen_ + 511, 

   - _Si_ +1 = StateUpdate128( _Si_ , _mi_ , _cai_ , _cbi_ ); 

   - _ci_ = _pi ⊕ KSG_ 128( _Si_ ); 

end for; 

5 

Note that even when there is no plaintext, we still need to run the cipher for 256 steps. When we process the plaintext, the keystream bit is not used to update the state since _cbi_ = 0. The cipher specification is changed for 128 steps (since the value of _cai_ is set to 0 for 128 steps) so as to separate the processing of plaintext/ciphertext and the finalization. 

##### **1.3.6 The** 

After processing all the plaintext bits, we generate the authentication tag _T_ . 

1. Let _madlen_ + _pclen_ +512+ _i_ = 0 for _i_ = 0 to 767; 

2. Let _cai_ = 1 for _i_ = _adlen_ + _pclen_ + 512 to _adlen_ + _pclen_ + 1279; Let _cbi_ = 1 for _i_ = _adlen_ + _pclen_ + 512 to _adlen_ + _pclen_ + 1279; 

3. for _i_ = _adlen_ + _pclen_ + 512 to _adlen_ + _pclen_ + 1279, 

   - _Si_ +1 = StateUpdate128( _Si_ , _mi_ , _cai_ , _cbi_ ); 

   - _ksi_ = _KSG_ 128( _Si_ ); 

end for; 

The authentication tag _T_ is the last _t_ keystream bits, i.e., 

_T_ = _ksadlen_ + _pclen_ +1279 _−t_ +1 _∥ ksadlen_ + _pclen_ +1279 _−t_ +2 _∥· · · ∥ ksadlen_ + _pclen_ +1279. 

##### **1.3.7 The decryption and verification** 

The decryption and verification are very similar to the encryption and tag generation. The finalization in the decryption process is the same as that in the encryption process. We emphasize that if the verification fails, the ciphertext and the newly generated authentication tag should not be given as output; otherwise, the state of ACORN-128 is vulnerable to known-plaintext or chosenciphertext attacks (using a fixed _IV_ ). 

6 

## **Chapter 2** 

# **Security Goals** 

The security goals of ACORN are given in Table 2.1. In ACORN, each key, IV pair is used to protect only one message. If verification fails, the new tag and the decrypted ciphertext should not be given as output. 

Note that the authentication security in Table 2.1 includes the integrity security of plaintext, associated data and nonce. 

Table 2.1: Security Goals of ACORN-128 <u>(128-bit</u> tag) 

||Encryption|Authentication|
|---|---|---|
|ACORN-128|128-bit|128-bit|

7 

## **Chapter 3** 

#### **3.1 The security of the initialization** 

The initialization can be attacked by analyzing the relation between IV and keystream. In ACORN-128, the IV passes through at least 1792 steps before affecting ciphertext. This large number of steps in the initialization is to prevent various attacks against stream cipher initialization: the linear attack (such as the attack in [14]), differential attacks (such as the attacks in [16] and [15]) and cube attacks [7, 8]. 

#### **3.2 The security of the encryption process** 

We emphasize here that ACORN encryption is a stream cipher with a large state which is updated continuously. The attacks against a block cipher cannot be applied directly to ACORN. 

**Statistical Attacks.** If the _IV_ is used only once for each key, it is impossible to apply a differential attack to the encryption process. It is extremely difficult to apply a linear attack (or correlation attack) to recover the secret state since the state of ACORN is updated in a nonlinear way. In general, it would be difficult to apply any statistical attack to recover the secret state due to the nonlinear state update function (the statistical correlation between any two states vanishes quickly as the distance between them increases). 

## **Chapter 4** 

# **No Hidden Weakness** 

We state here that the designer/designers have not hidden any weaknesses in this cipher. 

15 

## **Chapter 8** 

# **Changes** 

We made the following tweaks in the second round submission: 

1. The number of steps in the initialization, padding of associated data, padding of plaintext, and finalization are changed from 1536, 512, 512, 512 to 1792, 256, 256, 768, respectively. The main reason from the change is to increase the steps in the initialization, so as to provide better protection of the secret key when nonce is reused. 

2. In the initialization stage, the key bits are now used as inputs in 1664 steps. (In version 1, the key bits are used only in 128 steps.) The reason for this tweak is to strengthen the cipher against the nonce reuse attack (in encryption/decryption) so that the secret key cannot be easily recovered in the nonce reuse attack. 

18