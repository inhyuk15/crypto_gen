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