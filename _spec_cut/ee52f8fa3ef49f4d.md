# The CiliPadi 

Family of Lightweight Authenticated Encryption 

Version 1.0 

Muhammad Reza Z’aba<sup>1</sup> , Norziana Jamil<sup>2</sup> , Mohd Saufy Rohmad<sup>3</sup> , Hazlin Abdul Rani<sup>4</sup> , and Solahuddin Shamsuddin<sup>4</sup> 

1 Faculty of Computer Science and Information Technology, University of Malaya `reza.zaba@um.edu.my` 

> 2College of Computing and Informatics, Universiti Tenaga Nasional `norziana@uniten.edu.my` 

> 3Faculty of Electrical Engineering, Universiti Teknologi MARA `saufy@uitm.edu.my` 

> 4CyberSecurity Malaysia `hazlin@cybersecurity.my solahuddin@cybersecurity.my` 

March 29, 2019 

#### **CyberSecurity Malaysia** 

Level 9 Tower 1 Menara Cyber Axis Jalan Impact 63000 Cyberjaya, Selangor Malaysia 

Tel: +603 8800 7999 Fax: +603 8008 7000 

E-mail: `cilipadi@cybersecurity.my` 

## **Contents** 

|**1**|**Intr**|**oduction**<br>**1**|
|---|---|---|
|**2**|**Pre**|**liminaries**<br>**1**|
||2.1|Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>1|
||2.2|Mode of Operation . . . . . . . . . . . . . . . . . . . . . . . . . .<br>1|
|**3**|**Spe**|**cifcation**<br>**2**|
||3.1|Parameters<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>2|
||3.2|Initialization Phase . . . . . . . . . . . . . . . . . . . . . . . . . .<br>4|
||3.3|Padding . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>4|
||3.4|Associated Data Authentication Phase . . . . . . . . . . . . . . .<br>4|
||3.5|Message Encryption Phase . . . . . . . . . . . . . . . . . . . . . .<br>5|
||3.6|Message Decryption Phase . . . . . . . . . . . . . . . . . . . . . .<br>5|
||3.7|Finalization Phase . . . . . . . . . . . . . . . . . . . . . . . . . .<br>5|
||3.8|The Permutation Function _P_<br>. . . . . . . . . . . . . . . . . . . .<br>5|
||3.9|The _F_ function . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>6|
|||3.9.1<br>`AddConstants` (`AC`) . . . . . . . . . . . . . . . . . . . . . .<br>7|
|||3.9.2<br>`SubCells` (`SC`)<br>. . . . . . . . . . . . . . . . . . . . . . . .<br>7|
|||3.9.3<br>`ShiftRows` (`SR`) . . . . . . . . . . . . . . . . . . . . . . . .<br>7|
|||3.9.4<br>`MixColumnsSerial` (`MCS`)<br>. . . . . . . . . . . . . . . . . .<br>8|
|**4**|**Des**|**ign Rationale**<br>**8**|
||4.1|Key Lengths<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>8|
||4.2|Sponge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>8|
||4.3|Permutation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>9|
|**5**|**Per**|**formance Analysis**<br>**9**|
||51|ImlementationResults<br>11|
||.|p <br>. . . . . . . . . . . . . . . . . . . . . . .<br>|
|**6**|**Sec**|**urity Analysis**<br>**12**|
||6.1|Diferential Cryptanalysis . . . . . . . . . . . . . . . . . . . . . .<br>12|
|||6.1.1<br>Preliminaries . . . . . . . . . . . . . . . . . . . . . . . . .<br>13|
|||6.1.2<br>_P_ as a Random Permutation<br>. . . . . . . . . . . . . . . .<br>14|
|||6.1.3<br>Collision-Producing Diferentials of CiliPadi . . . . . . . .<br>17|
|||6.1.4<br>Practical Security Bounds . . . . . . . . . . . . . . . . . .<br>18|
||6.2|Full Bit Difusion . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>19|
||6.3|Extension to Linear Cryptanalysis<br>. . . . . . . . . . . . . . . . .<br>19|
|**7**|**Stre**|**ngths and Weaknesses**<br>**19**|
||7.1|Strengths<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>20|
||7.2|Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>20|
|**A **|**Tes**|**t Vectors**<br>**23**|

ii 

## **2 Preliminaries** 

This section introduces the notation and other preliminaries as basis to understand subsequent sections. 

### **2.1 Notations** 

The notation used in this paper is given in Table 1. 

||Description|
|---|---|
|_K, N, T_<br>|The secret key, nonce, and tag, respectively<br>|
|_X∥Y_<br>|The concatenation of bit strings _X_ and _Y_<br>|
|_A_|The associated data where _A_=_A_1_∥. . . ∥As_<br>|
|_M_|The message where _M_ =_M_1_∥. . . ∥Mt_<br>|
|_C_|The ciphertext where _C_ =_C_1_∥. . . ∥Ct∥T_|
|_|X|_|The length of _X_ in bits|
|_S_|The internal state where _S_ = _Sr∥Sc_, _r_ = _|Sr|_ and<br>_c_=_|Sc|_<br>|
|_n_|The length of the internal state_S_, i.e._n_=_|S|_=_r_+_c_|
|`0`<sup>_x_</sup><br>2<sup>_,_</sup><sup>`1`</sup><sup>_x_</sup><br>2<br>|An all-zeros and all-ones binary string of _x_ bits, re-<br>spectively|
|_⌈X⌉_<sup>_i_</sup>|The frst _i_ bits (or leftmost bits) of _X_|
|(_X_1_∥. . . ∥Xx_)<br>_y←−X_|The parsing of the bit string _X_ into _x_ equally-sized<br>_y_-bit strings|

Table 1: Notation 

A number written in typewriter font is always treated as a 4-bit hexadecimal value, i.e. `0` _,_ `1` _, . . ._ `f` . If the value is subscripted with ‘2’, as shown in Table 1 then it is treated as a 1-bit value, which applies only for `0` and `1` . 

### **2.2 Mode of Operation** 

The CiliPadi[ _n, r, a, b_ ] mode of operation is based on the MonkeyDuplex construction [3, 6] and depicted in Figure 1. It consists of four phases: initialization, associated data authentication, message encryption/decryption, and finalization. The state length is _n_ bits initialized with the value of the secret key _K_ and nonce _N_ . The bitrate is _r_ bits and the capacity is _c_ = _n − r_ bits. The permutation for the initialization and finalization phases has _a_ rounds while the 

> 1 _Cili padi_ is a Malay word for the bird’s eye chili. The name is chosen due to the Malay proverb, _kecil-kecil cili padi_ which means tiny but powerful. In our context, CiliPadi has a small footprint but secure for lightweight applications. 

1 

<!-- Start of picture text -->
A 1 As M 1 C 1 Mt Ct ⌈K⌉ r T<br>r r r r r<br>K∥N r Pn a Pn b Pn b Pn b Pn a<br>c c c c<br>0 c− 1 1<br>Initialization AD Authentication Message Encryption Finalization<br><!-- End of picture text -->

Figure 1: CiliPadi mode of operation 

permutation for the associated data and message encryption/decryption phases has _b_ rounds where _b > a_ . 

## **3 Specification** 

This section formally describes the specification of CiliPadi. 

### **3.1 Parameters** 

The CiliPadi[ _n, r, a, b_ ] family of authentiated encryption (AE) scheme consists of configurable parameters. For the purpose of evaluation, we propose four flavours of CiliPadi which is listed in Table 2 according to increasing level of security. They are CiliPadi-Mild, CiliPadi-Medium, CiliPadi-Hot and CiliPadi-ExtraHot. The lengths stated in the table are all in bits. 

|CiliPadi-|Algorithm||Leng|th of||No. o|f rounds|
|---|---|---|---|---|---|---|---|
||[_n, r, a, b_]|Key|Nonce|Tag|Block|_P _<sup>_a_</sup><br>_n_|_P _<sup>_b_</sup><br>_n_|
|Mild|[256_,_64_,_18_,_16]|128|128|64|64|18|16|
|Medium|[256_,_96_,_20_,_18]|128|128|96|96|20|18|
|Hot|[384_,_96_,_18_,_16]|256|128|96|96|18|16|
|ExtraHot|[384_,_128_,_20_,_18]|256|128|128|128|20|18|

Table 2: CiliPadi parameters where the primary member is CiliPadi-Mild 

Formally, the CiliPadi family of AE accepts a _k_ -bit secret key _K_ and a 128-bit nonce _N_ . These values become the initial value of the _n_ -bit internal state _S_ = _K∥N_ . The state is then updated by the permutation _Pn_<sup>_a_.If the</sup><sup>_sr_-bit associated</sup> data _A_ = _A_ 1 _∥ . . . ∥As_ is non-empty, it will be subsequently processed, along with the internal state, by the associated data authentication phase. Encryption takes the padded message _M_ = _M_ 1 _∥ . . . ∥Mt_ and outputs the ciphertext _C_ = _C_ 1 _∥ . . . ∥Ct_ and tag _T_ where _|Mi|_ = _|Ci|_ = _T_ = _r_ bits. Decryption takes the ciphertext _C_ and tag _T_ and outputs the original message _M_ if and only if _C_ is authentic, else it outputs _⊥_ . The components and high-level overview of CiliPadi are given in Figures 2 and 3, respectively. The descriptions are provided in the following sections. 

2 

|**P**|**roc** Init(_K, N_)|**Proc** AD(_S, A_)|
|---|---|---|
|**1** <br>**2 **|_S ←K∥N_<br> **return** _S_|**1 for** _i_= 1_, . . . , s_ **do**<br>**2**<br>_S ←P _<sup>_b_</sup><br>_n_<sup>((</sup><sup>_Sr_</sup> <sup>_⊕Ai_)</sup><sup>_∥Sc_)</sup>|
|||**3 end**|
|**P**|**roc** Finalization(_S_)|**4** _S ←_(_Sr∥Sc ⊕_(`0`<sup>_c−_1</sup><br>2<br>_∥_`1`))|
|**1** <br>|_S ←P _<sup>_a_</sup><br>_n_<sup>(</sup><sup>_S_)</sup><br>|**5 return** _S_|
|**2**|_T ←⌈S⌉_<sup>_k _</sup>_⊕K_||
|**3 **|**return** _T_||
|**P**|**roc** MEnc(_S, M_)|**Proc** MDec(_S, C_)|
|**1 **|**for** _i_= 1_, . . . , t −_1 **do**|**1 for** _i_= 1_, . . . , t −_1 **do**|
|**2**|_Ci ←Sr ⊕Mi_|**2**<br>_Mi ←Sr ⊕Ci_|
|**3**|_S ←P _<sup>_b_</sup><br>_n_<sup>(</sup><sup>_Ci∥Sc_)</sup>|**3**<br>_S ←P _<sup>_b_</sup><br>_n_<sup>(</sup><sup>_Ci∥Sc_)</sup>|
|**4 **|**end**|**4 end**|
|**5**|_Ct ←Sr ⊕Mt_|**5** _Mt ←Sr ⊕Ct_|
|**6**|_S ←_(_Ct∥Sc_)|**6** _S ←_(_Ct∥Sc_)|
|**7 **|**return** _(S, C)_|**7 return** _(S, M)_|
|**P**|**roc** _P _<sup>_r_</sup><br>256<sup>(</sup><sup>_S_)</sup>|**Proc** _P _<sup>_r_</sup><br>384<sup>(</sup><sup>_S_)</sup>|
|**1**|(_X_1_∥. . . ∥X_4)<br>64<br>_←−S_|**1** (_X_1_∥. . . ∥X_6)<br>64<br>_←−S_|
|**2 **|**for** _i_= 1_, . . . , r_ **do**|**2 for** _i_= 1_, . . . , r_ **do**|
|**3**|_Y_1 _←F_1(_X_1)_⊕X_2|**3**<br>_Y_1 _←F_1(_X_1)_⊕X_2|
|**4**|_Y_2 _←X_3|**4**<br>_Y_2 _←X_3|
|**5**|_Y_3 _←F_2(_X_3)_⊕X_4|**5**<br>_Y_3 _←F_2(_X_5)_⊕X_6|
|**6**|_Y_4 _←X_1|**6**<br>_Y_4 _←X_1|
|**7**|_X ←Y_|**7**<br>_Y_5 _←F_3(_X_3)_⊕X_4|
|**8 **|**end**|**8**<br>_Y_6 _←X_5|
|**9**|_S ←X_|**9**<br>_X ←Y_|
|**10 **|**return** _S_|**10 end**|
|||**11** _S ←X_|
|**P**|**roc** _F _<sup>_i_</sup><br>_l_ <sup>(</sup><sup>_X_)</sup>|**12 return** _S_|
|**1** <br>|(_x_1_∥. . . ∥x_4)<br>16<br>_←−X_<br><br>2|**Proc** LED1r(_X, RC_)|
|**2**|(_w_1_∥w_2)<br>_←−l_|**1** _X ←_`AC`(_X RC_)|
|**3** <br>|(_z_1_∥z_2)<br>3_←−rc_[_i_]<br><br>|_,_<br>**2** _X ←_`SC`(_X_)|
|**4**|_x_1 _←_(`0`<sup>2</sup><br>2<sup>_∥w_1</sup><sup>_∥_</sup><sup>`0`2</sup><sup>_∥z_1</sup><sup>_∥_</sup><sup>`0`8</sup><br>2<sup>)</sup>|**3** _X ←_`SR`(_X_)|
|**5**|_x_2 _←_(`0`<sup>2</sup><br>2<sup>_∥w_2</sup><sup>_∥_</sup><sup>`0`2</sup><sup>_∥z_2</sup><sup>_∥_</sup><sup>`0`8</sup><br>2<sup>)</sup>|**4** _X ←_`MCS`(_X_)|
|**6**|_x_3 _←_(`2`_∥_`0`2_∥z_1_∥_`0`<sup>8</sup><br>2<sup>)</sup>|**5 return** _X_|
|**7**|<br><br> _x_4 _←_(`3`_∥_`0`2_∥z_2_∥_`0`<sup>8</sup><br>2<sup>)</sup>||
|**8**|_RC ←_(_x_1_∥x_2_∥x_3_∥x_4)||
|**9**|_X ←_LED1r(_X, RC_)||
|**10**|_X ←_LED1r(_X,_`0`<sup>64</sup><br>2 <sup>)</sup>||
|**11 **|<br> **return** _X_||

Figure 2: Components of CiliPadi 

3 

|**Proc** Encrypt(_K, N, A, M_)|**Proc** Decrypt(_K, N, A, C, T_)|
|---|---|
|**1** _S ←_Init(_K, N_)|**1** _S ←_Init(_K, N_)|
|**2** _S ←_AD(_S, A_)|**2** _S ←_AD(_S, A_)|
|**3** (_S, C_)_←_MEnc(_S, M_)|**3** (_S, M_)_←_MDec(_S, C_)|
|**4** _T ←_Finalization(_S_)|**4** _T _<sup>_′ _</sup>_←_Finalization(_S_)|
|**5 return** _(C, T)_|**5 if** _(T_ =_T _<sup>_′_</sup>_)_ **then**|
||**6**<br>**return** _M_<br>**7 else**|
||**8**<br>**return** _⊥_<br>**9 end**|

Figure 3: High-level overview of the encryption and decryption of CiliPadi 

### **3.2 Initialization Phase** 

The _n_ -bit state _S_ is initialized with the value of the _k_ -bit key followed by the 128-bit nonce _N_ . The internal state _S_ is initialized as 

Note that the nonce must never be repeated to encrypt different messages using the same secret key. The internal state can also be viewed as the concatenation of the _r_ -bit rate _Sr_ and _c_ -bit capacity _Sc_ parts, i.e. _S_ = _Sr∥Sc_ . The state is then processed by the _n_ -bit permutation _Pn_<sup>_a_,whichisdescribedlater.</sup> The output of this phase is fed to the associated data authentication phase, if the associated data is non-empty. 

### **3.3 Padding** 

Both the associated data and message blocks are individually padded only if its length is not a multiple of _r_ bits. Padding is performed by adding a bit `1` , and then as many zero bits as necessary until the padded data is in multiple of _r_ bits. If the length of the last block is _r −_ 1 bits, then only bit `1` is added. 

### **3.4 Associated Data Authentication Phase** 

If the associated data _A_ = _A_ 1 _∥ . . . ∥As_ is non-empty, then _A_ 1 is XORed with the inner state _Sr_ . The state _S_ is then updated by the permutation _Pn_<sup>_b_.This</sup> process is repeated for _Ai_ ( _i_ = 1 _, . . . , s_ ) until all associated data blocks are processed: 

After the last associated data is processed, the outer state _Sc_ is XORed with the binary string `0`<sup>_c_</sup> 2<sup>_−_1</sup> _∥_ `1` 2 to denote the completion of the associated data phase: 

The output of this phase is fed to either the message encryption or decryption phase, described next. 

4 

### **3.5 Message Encryption Phase** 

There are two main inputs for this phase. The first comes from either the initialization (if the associated data is empty) or associated data authentication phase. The second input comes from the padded message _M_ = _M_ 1 _∥ . . . ∥Mt_ . The current inner state _Sr_ is first XORed with the first message block _M_ 1 to produce the ciphertext block _C_ 1. If there are more message block available, then this process is repeated until all message blocks are processed, except for the last block where the permutation _Pn_<sup>_b_isnotapplied:</sup> 

The _i_ -th ciphertext block is extracted from the current state prior to the execution of _Pn_<sup>_b_as</sup><sup>_Ci_=</sup><sup>_Sr⊕Mi_.Theoutputofthisphaseisfedintothefinalization</sup> phase. 

### **3.6 Message Decryption Phase** 

The decryption phase is almost identical to encryption. It receives two inputs. The first is the outcome of either the initialization or associated data authentication phase. The second input is the ciphertext _C_ = _C_ 1 _∥ . . . ∥Ct_ . The first ciphertext block assumes the value of _Sr_ and then the state _S_ is updated by _Pn_<sup>_b_.Thisprocessisrepeateduntilthesecondlastciphertextblock.Thelast</sup> ciphertext block is not processed by _Pn_<sup>_b_.</sup> 

The corresponding message block is only released when the tag is verified, i.e. only after succesful execution of the finalization phase. The _i_ -th message block is extracted from the current state prior to the execution of the permutation _Pn_<sup>_b_,i.e.</sup><sup>_Mi_=</sup><sup>_Sr⊕Ci_.</sup> 

### **3.7 Finalization Phase** 

This phase updates the internal state _S_ to output a single _r_ -bit tag. After the state has been processed by _Pn_<sup>_a_,</sup><sup>_Sr_isXORedwiththefirst</sup><sup>_r_bitsofthekey</sup><sup>_K_.</sup> The tag _T_ is the result of this XOR as follows. 

When decrypting ciphertext, the original message _M_ will only be released if the computed tag above matches the one supplied by the sending party. 

### **3.8 The Permutation Function** _P_ 

The permutation function _P_ makes use of an unkeyed 2-round<sup>2</sup> of the lightweight block cipher `LED` [19] as the round- and line- dependent _F_ -function in a Type-II 

> 2This refers to a full 2 rounds where no operation is omitted in the last (second) round. 

5 

<!-- Start of picture text -->
X 1 X 2 X 3 X 4<br>64 64 64 64<br>F 1 i F 2 i<br>d  = 4<br>X 1 X 2 X 3 X 4 X 5 X 6<br>64 64 64 64 64 64<br>F 1 i F 2 i F 3 i<br>d  = 6<br><!-- End of picture text -->

Figure 4: Type-II GFN employed in CiliPadi for _d_ = 4 and _d_ = 6 

generalized feistel network (GFN) [24]. We refer a Type-II GFN that accepts _d_ input sub-blocks as a _d_ -line Type-II GFN. For CiliPadi, _d_ is an even number and each line is of length _n/d_ bits. There are _d/_ 2 _F_ functions in each round that accepts input from odd-numbered lines. Let _X_ 1 _∥ . . . ∥Xd_ denote the input lines. They are updated by the _F_ -function in the _i_ -th round as follows. 

After the above transformations, the lines are shuffled by the permutation function _π_ before being used as input to the next round. For instance, the shuffle _π_ = _{_ 2 _,_ 3 _,_ 4 _,_ 1 _}_ means that the first input line is mapped to the second output line, the second input line to the third output line, and so forth. The same shuffle _π_ is used in both the message encryption and decryption phases. For CiliPadi, the shuffling<sup>3</sup> used are given in Table 3 and depicted in Figure 4 for _d_ = 4 and _d_ = 6. 

|Input length|Number of|Shufe|
|---|---|---|
|_n_ (in bits)|lines _d_|_π_|
|128|2|_{_2_,_1_}_|
|256|4|_{_4_,_1_,_2_,_3_}_|
|384|6|_{_4_,_1_,_2_,_5_,_6_,_3_}_|
|512|8|_{_4_,_1_,_2_,_5_,_8_,_3_,_6_,_7_}_|

Table 3: Shuffling used in the Type-II GFN 

### **3.9 The** _F_ **function** 

As mentioned earlier, the round- and line- dependent _F_ function is an unkeyed 2-round of the `LED` [19] block cipher where no operation is omitted in the last (i.e. 

> 3Note that in [23], the index starts with 0, ours start with 1. 

6 

<!-- Start of picture text -->
x 1 x 2 x 3 x 4 x 1 x 2 x 3 x 4 x 1 x 2 x 3 x 4 x 1 x 2 x 3 x 4<br>AC SC SR MCS<br>x 5 x 6 x 7 x 8 x 5 x 6 x 7 x 8 x 6 x 7 x 8 x 5 x 6 x 7 x 8 x 5<br>x 9 x 10 x 11 x 12 x 9 x 10 x 11 x 12 x 11 x 12 x 9 x 10 x 11 x 12 x 9 x 10<br>x 13 x 14 x 15 x 16 x 13 x 14 x 15 x 16 x 16 x 13 x 14 x 15 x 16 x 13 x 14 x 15<br><!-- End of picture text -->

Figure 5: A single round of `LED` 

second) `LED` round. A single `LED` round<sup>4</sup> consists of the following four operations, depicted in Figure 5, applied in sequence to the 64-bit input: `AddConstants` , `SubCells` , `ShiftRows` and `MixColumnsSerial` . The input to `LED` is 64 bits partitioned into 16 4-bit cells. Let _x_ = _x_ 1 _∥ . . . ∥x_ 16 denote this input which can be depicted as a 4 _×_ 4 matrix which is entered row-wise as follows. 

In AES, the input is entered column-wise. 

#### **3.9.1** `AddConstants` **(** `AC` **)** 

Initialize a 6-bit round constant _rc_ 1 _∥ . . . ∥rc_ 6 set to all zeros. In each round of the permutation, the constant is updated by shifting its value 1 bit to the left. The new value for _rc_ 6 is taken as _rc_ 1 _⊕ rc_ 2 _⊕_ `1` . We also add the _F_ -function number encoded as a 4-bit value _l_ = _l_ 1 _∥ . . . ∥l_ 4 as one of the parameters in the constant value. This is to ensure that every _F_ -function has different constant value. 

The above matrix is XORed to the current value of the state in the first round of `LED` in the _F_ -function. The constants for the second round of `LED` are set to all-zeros. The complete values of the round constants are given in Table 4. 

#### **3.9.2** `SubCells` **(** `SC` **)** 

This operation substitutes the current value of each 4-bit cell with another 4-bit value, using the s-box of Present [9] given in Table 5. 

#### **3.9.3** `ShiftRows` **(** `SR` **)** 

This operation rotates the second, third and fourth row of the state matrix by one, two and three cells to the left. 

> 4We are not referring to v2 of `LED` [20]. 

7 

|Rnd.|Value|Rnd.|Value|Rnd.|Value|Rnd.|Value|
|---|---|---|---|---|---|---|---|
|1|(`0`_,_`1`_,_`0`_,_`1`)|6|(`7`_,_`6`_,_`7`_,_`6`)|11|(`3`_,_`6`_,_`3`_,_`6`)|16|(`1`_,_`6`_,_`1`_,_`6`)|
|2|(`0`_,_`3`_,_`0`_,_`3`)|7|(`7`_,_`5`_,_`7`_,_`5`)|12|(`7`_,_`4`_,_`7`_,_`4`)|17|(`3`_,_`5`_,_`3`_,_`5`)|
|3|(`0`_,_`7`_,_`0`_,_`7`)|8|(`7`_,_`3`_,_`7`_,_`3`)|13|(`7`_,_`1`_,_`7`_,_`1`)|18|(`7`_,_`2`_,_`7`_,_`2`)|
|4|(`1`_,_`7`_,_`1`_,_`7`)|9|(`6`_,_`7`_,_`6`_,_`7`)|14|(`6`_,_`3`_,_`6`_,_`3`)|19|(`6`_,_`5`_,_`6`_,_`5`)|
|5|(`3`_,_`7`_,_`3`_,_`7`)|10|(`5`_,_`7`_,_`5`_,_`7`)|15|(`2`_,_`7`_,_`2`_,_`7`)|20|(`5`_,_`3`_,_`5`_,_`3`)|

Table 4: The values for the second column of the round constant state matrix used in the first `LED` -round of all _F_ -functions. The round constants for the second `LED` -round are set to all-zeros. The first column of the round constant matrix is ( `0` _,_ `1` _,_ `2` _,_ `3` ) for _F_ 1<sup>_i_,(</sup><sup>`0`</sup><sup>_,_</sup><sup>`2`</sup><sup>_,_</sup><sup>`2`</sup><sup>_,_</sup><sup>`3`)for</sup><sup>_F j_</sup> 2<sup>,and(</sup><sup>`0`</sup><sup>_,_</sup><sup>`3`</sup><sup>_,_</sup><sup>`2`</sup><sup>_,_</sup><sup>`3`)for</sup><sup>_F j_</sup> 3<sup>.</sup> 

|_x_|`0`|`1`|`2`|`3`|`4`|`5`|`6`|`7`|`8`|`9`|`a`|`b`|`c`|`d`|`e`|`f`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|_S_[_x_]|`c`|`5`|`6`|`b`|`9`|`0`|`a`|`d`|`3`|`e`|`f`|`8`|`4`|`7`|`1`|`2`|

Table 5: The s-box _S_ of Present used in `LED` 

#### **3.9.4** `MixColumnsSerial` **(** `MCS` **)** 

This operation multiplies the current value of the state with the following 4 _×_ 4 matrix. 

The result of the multiplication is the new value of the state. 

### **4.3 Permutation** 

The permutation function makes use of an unkeyed 2-round of the lightweight block cipher `LED` [19] as the _F_ -function in a Type-II generalized feistel network (GFN) [24]. This is similar to the Simpira v2 permutation framework introduced by Gueron and Mouha [17]. To maximize diffusion, Simpira v2 utilizes a shuffling introduced by Suzaki and Minematsu [23], instead of the traditional left or right rotation of the input sub-blocks. The optimized shuffling allows us to achieve faster full diffusion of the input sub-blocks compared to the conventional Type-II GFN. A full diffusion means that all output sub-blocks are affected by all input sub-blocks. 

Note that Simpira v2 was originally designed to utilize native AES instructions such as Intel’s AES-NI present in many modern processors. The aim is to achieve a high throughput implementation. As there is no hardware-specific instructions for `LED` , this is not our ultimate aim. We chose to follow Simpira v2 due to its flexibility in extending to larger input lengths and also because it is easy to analyze its security with respect to differential and linear cryptanalysis. 

By employing a Type-II GFN, it is trivial to extend the input lengths in multiple of 128 bits. The use of 2-round `LED` as the _F_ -function allows us to borrow the security analysis done on Simpira v2, which utililizes 2-round AES instead. 

The `LED` block cipher is chosen due to its lightweight construction and its similarity to the AES. In contrast to a 1-round `LED` that has a minimum of one active s-box, a 2-round `LED` has a minimum of 5 active s-boxes, which is identical to the AES [15]. This allows us to easily extend the results of Gueron and Mouha [17], whom originally use AES in the Simpira v2 framework, to CiliPadi. 

The number of rounds for _Pn_<sup>_b_,i.e.</sup><sup>_b_=16,isoneroundextrathanthe</sup> suggested number of rounds for Simpira v2 (i.e. 15) for _d_ = 4 and _d_ = 6. Furthermore, _Pn_<sup>_a_istworoundsmorethan</sup><sup>_P b_</sup> _n_<sup>,whichshouldprovideample</sup> protection against tag forgery in the finalization phase. 

#### **6.1.2** _P_ **as a Random Permutation** 

For _P_ to approximate a random permutation, the differential probability should be at most 2<sup>_−_256</sup> (2<sup>_−_384</sup> ) for _d_ = 4 ( _d_ = 6). As the differential probability of 

14 

|Round|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|
|AF|0|1|2|3|4|6|8|10|11|12|
|Round|11|12|13|14|15|16|17|18|19|20|
|AF|13|14|15|17|19|21|22|23|24|25|
|Round|21|22|23|24|25|26|27|28|29|30|
|AF|26|28|30|32|33|34|35|36|37|39|

Table 8: Active _F_ -function distribution for CiliPadi-Hot/ExtraHot ( _d_ = 6) 

the s-box is 2<sup>_−_2</sup> , this requires at least<sup><u>256</u></sup> 2<sup>= 128 (</sup><sup><u>384</u></sup> 2<sup>= 192) AS. A conservative</sup> approach is to assume each AF to contain only 5 AS as was the assumption made for a Type-II GFN that has 2 substitution layers interleaved with a single maximum distance separable (MDS)-based diffusion layer [10] (same as our 2- round `LED` with the exception that ours have an extra diffusion layer). Based on this approach, therefore, 2256 _×_ 5<sup>_≈_26(</sup> 2<sup><u>384</u></sup> _×_ 5<sup>_≈_39)AFisrequiredinorderfor</sup> _P_ to resist differential cryptanalysis. Indeed, 26 (39) AF gives 26 _×_ 5 = 130 (39 _×_ 5 = 195) AS. Based on this rough estimate, according to Table 7 (8), _P_ needs to have at least 27 (30) rounds for _d_ = 4 ( _d_ = 6) to avoid any biases from a random permutation. 

However, since _P_ makes use of `LED` , which inherits the wide trails strategy of the AES, we can improve the previous analysis. As illustrated in Figure 8 and proven by the designers of AES, any 4-round differential path provides a minimum of 25 active s-boxes. Suppose that a particular round in `LED` has one AF where the internal differential paths looks like the first 2 rounds of the 4-round path depicted in the figure. We can observe that `MCS` causes all 4-bit cells to have nonzero output difference. Then, these 16 nonzero differences become the input to the next subsequent _F_ -function which activate 16 AS in the first `LED` round and another 4 AS in the second `LED` round. It is therefore not possible for this second AF to have 5 AS as assumed before. Due to the wide trail strategy, this second AF is guaranteed to contain 20 AS. The AS pattern is 1 _→_ 4 _→_ 16 _→_ 4 _→_ 1. 

Table 9 expands the AF distribution given in Tables 7 and 8 by showing examples of truncated differential paths for _Pn_<sup>_a_forallflavoursofCiliPadi.As</sup> given earlier in this section, for _d_ = 4, 128 AS are required in order for _P_ to be resistant to differential cryptanalysis. For _d_ = 6, the number of AS is 192. Based on Table 9, the truncated differential path for _P_ 256<sup>18and</sup><sup>_P_20</sup> 256<sup>each contains</sup> a minimum of 180 and 185 AS, respectively. On the other hand, the path for _P_ 384<sup>18and</sup><sup>_P_20</sup> 384<sup>eachcomprises265and290AS,respectively.Thesenumbersfor</sup> CiliPadi are beyond the required number of AS. The upper bounds of the differential probability _p_ ˆ _u_ of _Pn_<sup>_a_for all variants ofCiliPadi are shown in Table 10.For</sup> each variant, we also provide the number of truncated paths that correspond to the number of AF. Note that a 6-round iterative truncated differential with 6 AF (0001 _→_ 0001), and a 16-round iterative truncated differential with 22 AF (000001 _→_ 000001) exists for _d_ = 4 and _d_ = 6 respectively. 

**Practical Confirmation:** We now experimentally confirm that our “active _F_ - function” estimation is a conservative lower bound, and that the actual number of AS per AF would be higher than 5 as the number of rounds increases. In 

15 

<!-- Start of picture text -->
1 AS<br>AC<br>SR MCS<br>Round SC<br>1<br>4 AS<br>AC<br>SR MCS<br>Round SC<br>2<br>16 AS<br>AC<br>SR MCS<br>Round SC<br>3<br>4 AS<br>AC<br>SR MCS<br>Round SC<br>4<br><!-- End of picture text -->

Figure 8: A 4-round differential path for `LED` that guarantees at least 25 active s-boxes (AS) 

other words, the number of AF provides us with an upper bound in terms of differential probability. To perform the differential search, we leverage upon the methodology described in [14]. Here, we focus on only the CiliPadi-Mild as a proof-of-concept and use the truncated differential path shown in Table 9 as a guide. We limit our input difference to have a hamming weight of 1 (only 1 bit out of any 64-bit word will be active at one time). Due to computational limitations, we bound the search based on each round of LED as: 

- **LED Round 1:** Based on the input difference, if the number of activated s-boxes is more than 8, we limit the number of branches to 2 for each s-box, whereby we select the two branches with the highest differential probability. Otherwise, we search all branches. 

- **LED Round 2:** Based on the input difference, if the number of activated s-boxes is more than 4, we limit the number of branches to 1 for each s- box, whereby we select the branch with the highest differential probability. Otherwise, we search all branches. 

Based on this methodology, we found a 4-round concrete path following the truncated differential path 0001 _→_ 0111 with a probability of 2<sup>_−_140</sup> : 

where ∆ _Y_ is post-shuffle. The breakdown of the concrete differential path, the number of AS per round, and the comparison to our lower bound AS _l_ , is shown in Table 11. In the second round, there are 5 AF which leads to a probability 

16 

||Mild|(_P_ <sup>1</sup><br>2|<sup>8</sup><br>56<sup>)</sup>|Mediu|m (|_P_ <sup>20</sup><br>256<sup>)</sup>|Hot (|_P_ <sup>18</sup><br>384|<sup>)</sup>|ExtraHo|t (_P_|<sup>20</sup><br>384<sup>)</sup>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Rnd.|∆_X_|AF|AS|∆_X_|AF|AS|∆_X_|AF|AS|∆_X_|AF|AS|
|1|0001|0|0|0001|0|0|000001|0|0|000011|1|5|
|2|0010|1|5|0010|1|5|001000|1|5|000001|0|0|
|3|0110|1|20|0110|1|20|010010|1|20|001000|1|5|
|4|1110|2|10|1110|2|10|101001|2|10|010010|1|20|
|5|0111|1|20|0111|1|20|111110|3|60|101001|2|10|
|6|1100|1|5|1100|1|5|011111|2|10|111110|3|60|
|7|0001|0|0|0001|0|0|110001|1|20|011111|2|10|
|8|0010|1|5|0010|1|5|001100|1|5|110001|1|20|
|9|0110|1|20|0110|1|20|010000|0|0|001100|1|5|
|10|1110|2|10|1110|2|10|100000|1|5|010000|0|0|
|11|0111|1|20|0111|1|20|100100|1|20|100000|1|5|
|12|1100|1|5|1100|1|5|100110|2|10|100100|1|20|
|13|0001|0|0|0001|0|0|101111|3|60|100110|2|10|
|14|0010|1|5|0010|1|5|110111|2|10|101111|3|60|
|15|0110|1|20|0110|1|20|000111|1|20|110111|2|10|
|16|1110|2|10|1110|2|10|000011|1|5|000111|1|20|
|17|0111|1|20|0111|1|20|000001|0|0|000011|1|5|
|18|1100|1|5|1100|1|5|001000|1|5|000001|0|0|
|19||||0001|0|0||||001000|1|5|
|20||||0010|1|5||||010010|1|20|

Table 9: Numbers of AF and AS for truncated differential paths for _Pn_<sup>_a_</sup> 

_n_ 

|CiliPadi-|_n_|_a_|AF|AS|ˆ_pu_|Truncated Paths|
|---|---|---|---|---|---|---|
|Mild|256|18|18|180|2<sup>_−_360</sup>|122|
|Medium|256|20|19|185|2<sup>_−_370</sup>|10|
|Hot|384|18|23|265|2<sup>_−_530</sup>|144|
|ExtraHot|384|20|25|290|2<sup>_−_580</sup>|36|

Table 10: Differential probability upper bounds for _Pn_<sup>_a_</sup> 

of (2<sup>_−_2</sup> )<sup>5</sup> = 2<sup>_−_10</sup> , verifying the correctness of our implementation. However, although the third round has only 1 AF, the actual number of AS is 28 due to the strong diffusion capability of LED. It confirms our claim that the number of “active _F_ -functions” can be used as a conservative estimate of the security margin, and will lead to a conservative lower bound in terms of security margin (and equivalently, an upper-bound in terms of differential probability). 

#### **6.1.3 Collision-Producing Differentials of CiliPadi** 

The number of AF for a collision-producing truncated differential for CiliPadiMild and CiliPadi-ExtraHot can be identified by fixing both the input and output truncated differences to “1000” and “110000” respectively (i.e. 1000 _→_ 1000 and 110000 _→_ 110000 because _r_ is a multiple of 64. For ease of analysis, we use 1000 _→_ 1000 as the truncated differential for CiliPadi-Medium, by setting the remaining 96 _−_ 64 = 32 bits of the bitrate part to nonzero. For CiliPadi-Hot, 

17 

||Concrete Diferential||AS|AS_l_|
|---|---|---|---|---|
|`0`<sup>64</sup><br>2|`0`<sup>64</sup><br>2<br>`0`<sup>64</sup><br>2|(`0`<sup>28</sup><br>2 <sup>_∥_</sup><sup>`2`</sup><sup>_∥_</sup><sup>`0`32</sup><br>2 <sup>)</sup>|0|0|
|`0`<sup>64</sup><br>2|`0`<sup>64</sup><br>2<br>(`0`<sup>28</sup><br>2 <sup>_∥_</sup><sup>`2`</sup><sup>_∥_</sup><sup>`0`32</sup><br>2 <sup>)</sup>|`0`<sup>64</sup><br>2|5|5|
|`0`<sup>64</sup><br>2|(`0`<sup>28</sup><br>2 <sup>_∥_</sup><sup>`2`</sup><sup>_∥_</sup><sup>`0`32</sup><br>2 <sup>)</sup><br>`c25adcad9fdb44b1`|`0`<sup>64</sup><br>2|28|20|
|(`0`<sup>28</sup><br>2 <sup>_∥_</sup><sup>`2`</sup><sup>_∥_</sup><sup>`0`32</sup><br>2 <sup>)</sup>|<sup>`c25adcad9fdb44b1 7f46a6de679866ce`</sup>|`0`<sup>64</sup><br>2|36|10|
|`0`<sup>64</sup><br>2|`7f46a6de679866ce 8f01218a4117896f`|(`0`<sup>28</sup><br>2 <sup>_∥_</sup><sup>`2`</sup><sup>_∥_</sup><sup>`0`32</sup><br>2 <sup>)</sup>|-|-|

Table 11: Example of a concrete differential path for _P_ 256<sup>_a_</sup> 

we use 100000 _→_ 100000. We then employ the same searching algorithm to identify the truncated differential path with the lowest number of AF for _Pn_<sup>_b_.</sup> The results are summarized in Table 12 where _p_ ˆ _col_ denotes the probability of the collision-inducing path. The truncated paths corresponding to each of CiliPadi’s variants are as shown in Table 13. Note that a 6-round iterative truncated collision-producing differential exists for _d_ = 4, where 1000 _→_ 1000 with 6 AF. 

|CiliPadi-|_n_|_b_|AF|AS|ˆ_pcol_|
|---|---|---|---|---|---|
|Mild|256|16|18|180|2<sup>_−_360</sup>|
|Medium|256|18|18|180|2<sup>_−_360</sup>|
|Hot|384|16|22|260|2<sup>_−_520</sup>|
|ExtraHot|384|18|26|310|2<sup>_−_620</sup>|

Table 12: Collision-producing differential probability upper bounds for _Pn_<sup>_b_</sup> 

**Practical Confirmation:** We now experimentally confirm that the collision probabilities in Table 12 provides conservative lower bounds. Again, we target CiliPadi-Mild as a proof-of-concept and use the truncated differential path shown in Table 13 as a guide. Based on the same methodology described in Section 6.1.2, we found a 3-round concrete path following the truncated differential path with a probability of 2<sup>_−_140</sup> : 

where ∆ _Y_ is post-shuffle. The above differential path contains a total of 69 AS, which is significantly higher than the theoretical lower bound of 35 AS for a 3-round differential, as shown in Table 13. 

#### **6.1.4 Practical Security Bounds** 

In practice, the best cryptanalytic attack requires less computational complexity than an exhaustive search of the secret key. CiliPadi has key sizes of 128 and 256 bits, thus any statistical distinguisher for a successful attack must have a probability higher than 2<sup>_−_128</sup> and 2<sup>_−_256</sup> respectively. Based on Tables 10 and 12, the theoretical upper bounds of the differential probability indicate that all flavours of CiliPadi are highly resistant to differential cryptanalysis and collision attacks. In reality, the differential probabilities are much lower as depicted in 

18 

||Mild|(_P_ <sup>1</sup><br>2|<sup>6</sup><br>56<sup>)</sup>|Mediu|m (|_P_ <sup>18</sup><br>256<sup>)</sup>|Hot (|_P_ <sup>16</sup><br>384|<sup>)</sup>|ExtraHo|t (_P_|<sup>18</sup><br>384<sup>)</sup>|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Rnd.|∆_X_|AF|AS|∆_X_|AF|AS|∆_X_|AF|AS|∆_X_|AF|AS|
|1|1000|1|5|1000|1|5|100000|1|5|110000|1|5|
|2|1001|1|20|1001|1|20|100100|1|20|000100|0|0|
|3|1011|2|10|1011|1|10|100110|2|10|000010|1|5|
|4|1101|1|20|1101|2|20|101111|3|60|001001|1|20|
|5|0011|1|5|0011|1|5|110111|2|10|011010|2|10|
|6|0100|0|0|0100|0|0|000111|1|20|111011|3|60|
|7|1000|1|5|1000|1|5|000011|1|5|010111|1|5|
|8|1001|1|20|1001|1|5|000001|0|0|101011|3|60|
|9|1011|2|10|1011|2|10|001000|1|5|110111|2|10|
|10|1101|1|20|1101|2|5|010000|1|20|000111|1|20|
|11|1011|2|10|0011|1|5|100000|2|10|000011|1|5|
|12|1101|1|20|0100|0|0|100100|3|60|000001|0|0|
|13|1011|2|10|1000|1|5|100110|2|10|001000|1|5|
|14|1101|1|20|1001|1|20|101111|1|20|010010|1|20|
|15|0011|1|5|1011|2|10|110101|1|5|101001|2|10|
|16|0100|0|0|1101|2|20|001110|0|0|111110|3|45|
|17||||0011|1|5||||111101|2|10|
|18||||0100|0|0||||011100|1|20|

Table 13: Numbers of AF and AS for truncated collusion-producing differential paths for _Pn_<sup>_b_</sup> 

the practical confirmation experiments. Therefore, CiliPadi is expected to thwart any differential type attacks. 

### **6.2 Full Bit** 

With the availability of the full AF distribution, we can determine the minimum number of rounds for _P_ to achieve full bit diffusion. Here, the findings from Simpira v2 are directly applicable because the underlying round functions for both Simpira and CiliPadi have the same diffusion properties. For _d_ = 4, full bit diffusion is achieved after 4 _d −_ 6 = 16 _−_ 6 = 10 _F_ -functions [17]. Based on Table 7, 9 rounds of _P_ is sufficient for full bit diffusion. As for _d_ = 6, full bit diffusion is achieved after 5 rounds [23]. Thus, the current number of rounds of _P_ for all variants of CiliPadi are to achieve full bit 

## **7 Strengths and Weaknesses** 

The following list the expected strengths and weaknesses of CiliPadi. 

### **7.1 Strengths** 

CiliPadi has the following advantages: 

- It is trivial to expand the length of the permutation in multiple of 128 bits due to the use of a Type-II GFN. 

- The bitrate can be adjusted to allow different plaintext and tag lengths. 

- The design is based on the sponge construction, which have been extensively analyzed and employed in SHA-3 and one of the CAESAR portfolio Ascon. 

- Any AES-like block cipher or permutation can be adopted in the _F_ - function to replace the `LED` block cipher, if desired. 

### **7.2 Weaknesses** 

The known limitations of CiliPadi are: 

- The processing of the message and ciphertext blocks cannot be parallelized because due to the sequential processing of the input blocks. 

- The permutation can only be expanded in multiple of 128 bits. Extending with a smaller granularity, e.g. 32 bits, is not supported. This can be addressed by using a smaller block cipher as the _F_ -function such as KATAN and KTANTAN [11].