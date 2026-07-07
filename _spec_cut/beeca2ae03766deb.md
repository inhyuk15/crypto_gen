# **Shabal, a Submission to NIST’s Cryptographic Hash Algorithm Competition** 

## Initiated by the Saphir project 

```
http://www.shabal.com
```

#### <u>Editors:</u> 

Anne Canteaut, Benoˆıt Chevallier-Mames, Aline Gouget, Pascal Paillier, Thomas Pornin 

#### <u>Contributors:</u> 

Emmanuel Bresson, Christophe Clavier, Thomas Fuhr, Thomas Icart, JeanFran¸cois Misarsky, Mar´ıa Naya-Plasencia, Jean-Ren´e Reinhard, C´eline Thuillet, Marion Videau 

October 28, 2008 

#### **Shabal** 

Shabal is a cryptographic hash function submitted by the France funded research project Saphir to NIST’s international competition on hash functions. More specifically, the research partners of Saphir (with the notable exception of LIENS) initiated the conception of Shabal and were later joined by partners of the soon-to-be research projectSaphir2 who actively contributed to the final design of Shabal. Saphir2 is a 4-year research project funded by the French research agency (ANR) and will continue the works and achievements of the Saphir project starting from 2009. Partners of Saphir2 come from both industry and academia; in addition to partners of Saphir, 4 new partners (EADS SN, INRIA, Sagem S´ecurit´e and UVSQ) are about to join and contribute. 

Saphir (Security and Analysis of Hash Primitives<sup>1</sup> ) is an ANR<sup>2</sup> funded project on hash functions. Saphir has started on March 2006 for a duration of three years and brings five partners together: Cryptolog International, DCSSI, France Telecom (leader), Gemalto and LIENS. The goal of Saphir is to develop a better understanding of recent attacks on hash functions and their potential impact; to extend their scope; to reconsider the design of secure hash functions. The project also aims at proactively anticipating new research directions in the area of hash functions, and at making subsequent results available to the largest audience. 

# **Contents** 

|**Cover page**|**1**|
|---|---|
|**Table of contents**|**9**|
|**List of Figures**|**11**|
|**List of Tables**|**12**|
|**2.B.1 A Complete Written Specifcation of the Algorithm**|**13**|
|**1**<br>**A Short Introduction to Hash Functions**|**14**|
|1.1<br>Modes for Iterative Hash Functions . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>14|
|1.2<br>A General Description of a Sequential Iterative Hash Function<br>. . . . . . . .|. . .<br>15|
|1.3<br>Some Existing Iterative Modes<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>16|
|1.3.1<br>Plain Merkle-Damg˚ard . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>16|
|1.3.2<br>MD With Special Message Formatting . . . . . . . . . . . . . . . . . .|. . .<br>16|
|Strengthened MD. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>16|
|Prefx-Free MD.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|MD with a Counter. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|1.3.3<br>MD with Larger Internal State . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|Chop-MD.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|1.3.4<br>MD with Discontinuity<br>. . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|NMAC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>17|
|HMAC. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>18|
|Wide Pipe Hash. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>18|
|EMD. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>18|
|1.3.5<br>Sponge Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . .<br>18|
|The “Concatenate-Permute-Truncate” Design.<br>. . . . . . . . . . . . .|. . .<br>19|
|Belt-and-Mill Hash Functions.<br>. . . . . . . . . . . . . . . . . . . . . .|. . .<br>19|

4 

|**2**<br>**Co**<br>|**mplete **<br>|**Description of Shabal**<br>**20**<br><br>|
|---|---|---|
|2.1|Conve|ntions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>20|
||2.1.1|Endianess . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>20|
||2.1.2|Notation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>21|
|2.2|Descri|ption of the Mode of Operation<br>. . . . . . . . . . . . . . . . . . . . . . . . .<br>22|
||2.2.1|Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>22<br>|
||2.2.2|A High-Level View . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
||2.2.3|Security Results<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
|2.3|Specif|ying the Hash Function Shabal . . . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
||2.3.1|Overview<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>25|
||2.3.2|The Keyed Permutation . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>27|
|2.4|Tunab|le Security Parameters<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>28|
|2.5|Param|eter Choices in Shabal<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>29|
|**3**<br>**Som**|**e Tes**|**t Patterns**<br>**30**|
|3.1|The D|iferent Initialization Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.1|Initialization Vector for Shabal-192 . . . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.2|Initialization Vector for Shabal-224 . . . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.3|Initialization Vector for Shabal-256 . . . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.4|Initialization Vector for Shabal-384 . . . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.5|Initialization Vector for Shabal-512 . . . . . . . . . . . . . . . . . . . . . . .<br>31|
|3.2|Final|States and Outputs when Hashing Message A<br>. . . . . . . . . . . . . . . . .<br>32|
||3.2.1|Final State and Output for Shabal-192 . . . . . . . . . . . . . . . . . . . . .<br>32|
||3.2.2|Final State and Output for Shabal-224 . . . . . . . . . . . . . . . . . . . . .<br>32|
||3.2.3|Final State and Output for Shabal-256 . . . . . . . . . . . . . . . . . . . . .<br>32|
||3.2.4|Final State and Output for Shabal-384 . . . . . . . . . . . . . . . . . . . . .<br>33|
||3.2.5|Final State and Output for Shabal-512 . . . . . . . . . . . . . . . . . . . . .<br>33|
|3.3|Final|States and Outputs when Hashing Message B. . . . . . . . . . . . . . . . . .<br>33|
||3.3.1|Final State and Output for Shabal-192 . . . . . . . . . . . . . . . . . . . . .<br>33|
||3.3.2|Final State and Output for Shabal-224 . . . . . . . . . . . . . . . . . . . . .<br>34|
||3.3.3|Final State and Output for Shabal-256 . . . . . . . . . . . . . . . . . . . . .<br>34|
||3.3.4|Final State and Output for Shabal-384 . . . . . . . . . . . . . . . . . . . . .<br>34|
||3.3.5|Final State and Output for Shabal-512 . . . . . . . . . . . . . . . . . . . . .<br>35|
|3.4|Interm|ediate States for Messages A and B . . . . . . . . . . . . . . . . . . . . . . .<br>35|
|**4**<br>**Des**|**ign Ra**|**tionale**<br>**36**|
|4.1|AQu|stforProvablySecureEfciency.........................<br>37|
||<br>4.1.1|<br><br>A Short Story about the Mode of Operation of Shabal . . . . . . . . . . . .<br>37|
||4.1.2|Security Proofs: An Intuition as to Why Shabal is Secure . . . . . . . . . .<br>38|
|4.2|Desig|ning the Keyed Permutation _P_<br>. . . . . . . . . . . . . . . . . . . . . . . . . .<br>38|
||4.2.1|An NLFSR-based Structure . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>39|
||4.2.2|A Permutation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>39|
||4.2.3|Register _A_. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>39|
|||Introducing _A_.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>40|
|||Introducing _C_. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>40|
|||Introducing _M_. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>40|
|||Using _U_ and _V_ as S-Boxes.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .<br>40|
||4.2.4|Register _B_<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>40|
|||Introducing _A_.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>41|
|||Introducing _B_. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>41<br>|
|||The Addition of Constant `0xFFFFFFFF`.<br>. . . . . . . . . . . . . . . . . . . .<br>41|
||4.2.5<br>|Function _G_<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>41<br><br>|
||4.2.6|The Final Transformation . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>42|
|4.3|How|We Chose (_o_1_, o_2_, o_3) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .<br>42|

5 

||4.3.1<br>|The Basic Idea . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>|. .<br>42<br><br>|
|---|---|---|---|
||4.3.2|Linearization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>43|
||4.3.3|Search Methods. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>44|
||4.3.4|Results on the Linearized Function . . . . . . . . . . . . . . . . . . . . .|. .<br>44|
||4.3.5<br>|Final Results on the Real Function for _p_= 1 and _r_ = 12 . . . . . . . . . <br>|. .<br>44<br><br>|
|4.4|Shaba|l and Degree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>45|
||4.4.1|Degree of Weakinson-1bit . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>45|
||4.4.2|Degree of Weakinson-_⊕_-LinearUV-NoFinalUpdateA<br>. . . . . . . . . . .|. .<br>46|
|4.5<br>|Initial <br>|Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>|. .<br>46<br><br>|
|4.6|The E|fect of Counter _w_ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>47|
|4.7|Outpu|t of the Hash Function . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>47|
|4.8|Nonlin|earity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>47|
|**5**<br>**Sec**|**urity P**|**roofs for the Shabal Construction**|**48**|
|5.1|Introd|uction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>48|
||5.1.1|Provable Security for Hash Constructions . . . . . . . . . . . . . . . . .|. .<br>48|
|||Indiferentiability.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>48|
|||Security notions in idealized models. . . . . . . . . . . . . . . . . . . . .|. .<br>49|
||5.1.2|Summary of Our Security Results<br>. . . . . . . . . . . . . . . . . . . . .|. .<br>49|
||5.1.3|Roadmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>50|
|5.2|Refor|mulating the Mode of Operation of Shabal. . . . . . . . . . . . . . . . . .|. .<br>50|
|5.3|Shaba|l is Indiferentiable from a Random Oracle<br>. . . . . . . . . . . . . . . . .|. .<br>51|
||5.3.1|Preliminaries to the Proofs<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>52|
|||Our game-based proof technique. . . . . . . . . . . . . . . . . . . . . . .|. .<br>52|
|||Preliminary defnitions.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>52|
|||Hash graphs and graph-based simulators.<br>. . . . . . . . . . . . . . . . .|. .<br>53|
|||Detecting inconsistencies. . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>54|
||5.3.2|Proofs of Theorems 1 and 2 . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>54|
|||Proof of Theorem 1. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>54|
|||Proof of Theorem 2. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>63|
|5.4|Shaba|l is Collision Resistant in the Ideal Cipher Model. . . . . . . . . . . . . .|. .<br>65|
||5.4.1|A Security Model for Collision Resistance in the ICM<br>. . . . . . . . . .|. .<br>65|
||5.4.2|Proving Collision Resistance for Shabal’s Mode of Operation<br>. . . . . .|. .<br>66|
||5.4.3|Proof of Theorem 3<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>66|
|5.5|Shaba|l is Preimage Resistant in the Ideal Cipher Model . . . . . . . . . . . . .|. .<br>74|
||5.5.1|A Security Model for Preimage Resistance in the ICM . . . . . . . . . .|. .<br>74|
||5.5.2|Proving Preimage Resistance for Shabal’s Mode of Operation . . . . . .|. .<br>74|
||5.5.3|Proof of Theorem 4<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>75|
|||Preliminary defnitions.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>75|
|||Intuition of the proof. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>75|
|||The sequence of games.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>75|
|5.6|Shaba|l is Second Preimage Resistant in the Ideal Cipher Model . . . . . . . . .|. .<br>85|
||5.6.1|Capturing Second Preimage Resistance in the ICM . . . . . . . . . . . .|. .<br>85|
||5.6.2|Proving Second Preimage Resistance for Shabal’s Mode of Operation . .|. .<br>85|
||5.6.3|Proof of Theorem 5<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>86|
|||Intuition of the proof. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>86|
|||The sequence of games.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>86|
|**6**<br>**We**|**akened**|**Versions of Shabal**|**97**|
|6.1|With|Smaller Words . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>97|
|6.2|With|Linear Message Introduction . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>98|
|6.3<br>|With <br>|_U_(_x_) =_x_ and _V_(_x_) =_x_ . . . . . . . . . . . . . . . . . . . . . . . . . . . . <br>|. .<br>99<br>|
|6.4|With|_U_(_x_) = (_x ≪_1)_⊕x_ and _V_(_x_) = (_x ≪_2)_⊕x_<br>. . . . . . . . . . . . . . . .|. .<br>99|
|6.5|Witho|<br>ut the Last Update Loop on _A_ . . . . . . . . . . . . . . . . . . . . . . . .|. . 100|

6 

|6.6|Other|Non-described Variants . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 100|
|---|---|---|---|
|**7**<br>**Im**|**plemen**|**tation Tricks: How to Speed Up Codes on Your Platform**|**101**|
|7.1|Deskt|op and Server Systems . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 101|
||7.1.1|Cache Issues<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 101|
||7.1.2|Precomputations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 102|
||7.1.3|Machine Code Generation . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 102|
||7.1.4|Parallelism<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 103|
|7.2|Embe|dded and Small Systems . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 104|
|7.3|ASIC|and FPGA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . 104|

|**2.B.2**|**A Statement of the Algorithm’s Estimated Computational **|**Ef-**|
|---|---|---|
|**cienc**|**y and Memory Requirements in Hardware and Software**|**106**|
|**8**<br>**Com**|**putational Efciency And Memory Requirements In Hardware and Sof**|**t-**|
|**war**|**e**|**107**|
|8.1|High-End Software Platforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|107|
|8.2|Low-End Software Platforms<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|108|
|8.3|Smartcard Platforms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|109|
|8.4|Dedicated Hardware . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|109|
|**2.B.3 **|**A Series of Known Answer Tests and Monte Carlo Tests**|**111**|
|**9**<br>**Kno**|**wn Answer Tests and Monte Carlo Tests**|**112**|
|**2.B.4 **|**A Statement of the Expected Strength**|**113**|
|**10 Stat**|**ement of the Expected Strength**|**114**|
|10.1|Collision Resistance<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|114|
|10.2|Preimage Resistance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|115|
|10.3|Second-preimage Resistance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|115|
|10.4|Resistance to Length-extension Attacks<br>. . . . . . . . . . . . . . . . . . . . . . . .|115|
|10.5 <br>|Strength of a Subset of the Output Bits . . . . . . . . . . . . . . . . . . . . . . . .<br><br>|116<br>|
|10.6|PRF HMAC-Shabal<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|116|

7 

#### **2.B.5 An Analysis of the Algorithm with Respect to Known Attacks 117** 

|**11 Shabal: Resistance against Known Attacks**<br>**118**|
|---|
|11.1 Known Attacks Identifed by the Security Proofs . . . . . . . . . . . . . . . . . . . 119|
|11.1.1 Collision Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119|
|11.1.2 Second-preimage Attacks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . 119|
|11.1.3 Preimage Attacks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 120|
|11.2 Internal Collisions<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121|
|11.2.1 Generic Internal Collision Attack . . . . . . . . . . . . . . . . . . . . . . . . 121|
|11.2.2 One-block Internal Collisions . . . . . . . . . . . . . . . . . . . . . . . . . . 122|
|11.3 Diferential Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123|
|11.3.1 Truncated Diferential . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123|
|11.3.2 Diferential Trails without any Input Diference for _U_ and _V_ . . . . . . . . . 123|
|11.3.3 Diferential Trails without any Diference in _A_<br>. . . . . . . . . . . . . . . . 124|
|11.3.4 Symmetric Diferential Trails . . . . . . . . . . . . . . . . . . . . . . . . . . 125|
|11.4 Fixed Points<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126|
|11.5 Generic Attacks against Weakinson-1bit . . . . . . . . . . . . . . . . . . . . . . . . 126|
|11.6 (Second)-preimage Attack against Weakinson-NoFinalUpdateA . . . . . . . . . . . 127|
|11.6.1 Attack against Weakinson-NoFinalUpdateA with _p_= 1<br>. . . . . . . . . . . 127|
|11.6.2 Attack against Weakinson-NoFinalUpdateA with _p_= 2<br>. . . . . . . . . . . 128|
|11.7 Generic Attacks Against Merkle-Damg˚ard-Based Hash Functions . . . . . . . . . . 129|
|11.7.1 Length-extension Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129|
|11.7.2 Multi-Collisions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 129|
|11.8 Slide Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130|
|11.9 Algebraic Distinguishers and Cube Attacks<br>. . . . . . . . . . . . . . . . . . . . . . 130|
|11.10Attacks Taking Advantage of The Chosen Constants . . . . . . . . . . . . . . . . . 130|
|11.11Diferential Attack on HMAC-Shabal . . . . . . . . . . . . . . . . . . . . . . . . . . 130|
|Pseudo-Random Function. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 131|

|**2.B.6**<br>**tatio**|**A Statement that Lists and Describes the Advantages and Limi-**<br>**ns of the Algorithm**<br>**132**|
|---|---|
|**12 Adv**|**antages and Disadvantages of Shabal**<br>**133**|
|12.1|Simplicity of Design<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133|
|12.2|Provable Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133|
|12.3|Software Implementation Considerations . . . . . . . . . . . . . . . . . . . . . . . . 134|
||12.3.1 Word Size . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134|
||12.3.2 Very Few Requested Instructions to Code Shabal . . . . . . . . . . . . . . . 134|
||12.3.3 No S-Box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134|
||12.3.4 Speed Measures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135|
||12.3.5 Code Size . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136|

8 

**Acknowledgments 138** 

**Bibliography 140 Appendixes 144 A Basic Implementations 145** 

A.1 A Basic Implementation in C . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145 

A.1.1 shabal.h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 145 A.1.2 shabal.c . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 147 **B Detailed Test Patterns 154** B.1 Intermediate States for Shabal-192 (Message A) . . . . . . . . . . . . . . . . . . . . 154 B.2 Intermediate States for Shabal-192 (Message B) . . . . . . . . . . . . . . . . . . . . 169 B.3 Intermediate States for Shabal-224 (Message A) . . . . . . . . . . . . . . . . . . . . 183 B.4 Intermediate States for Shabal-224 (Message B) . . . . . . . . . . . . . . . . . . . . 198 B.5 Intermediate States for Shabal-256 (Message A) . . . . . . . . . . . . . . . . . . . . 212 B.6 Intermediate States for Shabal-256 (Message B) . . . . . . . . . . . . . . . . . . . . 227 B.7 Intermediate States for Shabal-384 (Message A) . . . . . . . . . . . . . . . . . . . . 242 B.8 Intermediate States for Shabal-384 (Message B) . . . . . . . . . . . . . . . . . . . . 256 B.9 Intermediate States for Shabal-512 (Message A) . . . . . . . . . . . . . . . . . . . . 271 

B.10 Intermediate States for Shabal-512 (Message B) . . . . . . . . . . . . . . . . . . . . 285 

9 

# **List of Figures** 

|1.1|Indiferentiability setup. The internal function _R_ is considered perfect. The mode||
|---|---|---|
||_C_<sup>_R_ </sup>has access to _R_. The simulator _S_<sup>_RO_ </sup>has oracle access to the random oracle||
||_RO_. The distinguisher interacts either with (_C_<sup>_R_</sup>_, R_) or (_RO, S_<sup>_RO_</sup>) and has to tell||
||them apart. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|15|
|1.2|A general iterative hash function construction.<br>. . . . . . . . . . . . . . . . . . . .|16|
|1.3|Plain Merkle-Damg˚ard construction. . . . . . . . . . . . . . . . . . . . . . . . . . .|16|
|1.4|Merkle-Damg˚ard construction with MD-strengthening. . . . . . . . . . . . . . . . .|17|
|1.5|Chop Merkle-Damg˚ard construction. . . . . . . . . . . . . . . . . . . . . . . . . . .|18|
|1.6|The sponge construction.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|19|
|2.1|The mode of operation: Message rounds . . . . . . . . . . . . . . . . . . . . . . . .|22|
|2.2|Final rounds: View 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|22|
|2.3|Final rounds: View 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|23|
|2.4|Main structure of the keyed permutation used in Shabal. . . . . . . . . . . . . . . .|29|
|4.1|Mode of Operation Old Mode 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|37|
|4.2|Mode of Operation Old Mode 2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|38|
|5.1|The inner primitive _P_ is assumed ideal. The cryptographic construction _C_<sup>_P_ </sup>has<br>oracle access to _P_. The simulator _S_<sup>_H_ </sup>has oracle access to the random oracle _H_.||
||The distinguisher interacts either with _Q_ = (_C_<sup>_P_</sup>_, P_) or _Q_<sup>_′_ </sup>= (_H, S_<sup>_H_</sup>) and has to||
||tell them apart. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|49|
|5.2|A reformulation of the mode of operation of Shabalwith a focus on the fnal rounds.<br>Note that the counter _w_ is omitted on this picture. . . . . . . . . . . . . . . . . . .|51|
|5.3|Our game-based construction of simulator _S_.<br>. . . . . . . . . . . . . . . . . . . . .|53|
|5.4|Indiferentiability: Simulator _S_ for _P_ in Game 1. . . . . . . . . . . . . . . . . . . .|55|
|5.5|Indiferentiability: Simulator _S_ for _P_ in Game 2. . . . . . . . . . . . . . . . . . . .|55|
|5.6|Indiferentiability: Simulator _S_ for _P_ in Game 3. . . . . . . . . . . . . . . . . . . .|57|
|5.7|Indiferentiability: Simulator _S_ for _P_ in Game 4. . . . . . . . . . . . . . . . . . . .|59|
|5.8|Indiferentiability: Simulator _S_ for _P_ in Game 5. . . . . . . . . . . . . . . . . . . .|61|
|5.9|Indiferentiability: Simulator _S_ for _P_ in Game 7. . . . . . . . . . . . . . . . . . . .|62|
|5.10|Indiferentiability: Simulator _S_ for _P_ in Game 8 (and fnal simulator). . . . . . . .|64|
|5.11|Indiferentiability: Simulation of _P_<sup>_−_1 </sup>in Game 2. . . . . . . . . . . . . . . . . . . .|64|
|5.12|Indiferentiability: Simulation of _P_<sup>_−_1 </sup>in Games 3–9. . . . . . . . . . . . . . . . . .|66|
|5.13|Collision resistance: simulator _S_ in Game 1. . . . . . . . . . . . . . . . . . . . . . .|67|
|5.14|Collision resistance: simulator _S_ in Game 2. . . . . . . . . . . . . . . . . . . . . . .|68|
|5.15|Collision resistance: simulator _S_ in Game 3. . . . . . . . . . . . . . . . . . . . . . .|69|
|5.16|Collision resistance: simulator _S_ in Game 4. . . . . . . . . . . . . . . . . . . . . . .|71|
|5.17|Collision resistance: simulator _S_ in Game 5. . . . . . . . . . . . . . . . . . . . . . .|72|
|5.18|Collision resistance: simulator _S_ in Game 6 (and fnal simulator). . . . . . . . . . .|73|
|5.19|Preimage resistance: simulator _S_ in Game 1.<br>. . . . . . . . . . . . . . . . . . . . .|76|
|5.20|Preimage resistance: simulator _S_ in Game 2.<br>. . . . . . . . . . . . . . . . . . . . .|77|

10 

|5.21 Preimage resistance: simulator _S_ in Game 3.<br>. . . . . . . . . . . . . . . . .|. . . .<br>78|
|---|---|
|5.22 Preimage resistance: simulator _S_ in Game 3.<br>. . . . . . . . . . . . . . . . .|. . . .<br>80|
|5.23 Preimage resistance: simulator _S_ in Game 5.<br>. . . . . . . . . . . . . . . . .|. . . .<br>82|
|5.24 Preimage resistance: simulator _S_ of Game 6 (and fnal simulator).<br>. . . . .|. . . .<br>83|
|5.25 Second preimage resistance: simulator _S_ in Game 1. . . . . . . . . . . . . .|. . . .<br>87|
|5.26 Second preimage resistance: simulator _S_ in Game 2. . . . . . . . . . . . . .|. . . .<br>88|
|5.27 Second preimage resistance: simulator _S_ in Game 3. . . . . . . . . . . . . .|. . . .<br>89|
|5.28 Second preimage resistance: simulator _S_ in Game 4. . . . . . . . . . . . . .|. . . .<br>91|
|5.29 Second preimage resistance: simulator _S_ in Game 5. . . . . . . . . . . . . .|. . . .<br>93|
|5.30 Second preimage resistance: simulator _S_ in Game 6. . . . . . . . . . . . . .|. . . .<br>94|
|5.31 Second preimage resistance: fnal simulator _S_. . . . . . . . . . . . . . . . . .|. . . .<br>95|

11 

# **List of Tables** 

|4.1|Degrees of the outputs of the message round function in Weakinson-1bit . . . . . .|45|
|---|---|---|
|4.2|Degrees of the outputs of the message round function in Weakinson-_⊕_-LinearUV-<br>NoFinalUpdateA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|46|
|8.1|Shabal performance on high-end software platforms . . . . . . . . . . . . . . . . . .|108|
|8.2|Shabal performance on low-end software platforms . . . . . . . . . . . . . . . . . .|109|
|11.1|Conditions derived from (11.4) for symmetric diferential trails<br>. . . . . . . . . . .|126|
|12.1|Shabal performance compared with other hash functions (1) . . . . . . . . . . . . .|135|
|12.2|Shabal performance compared with other hash functions (2) . . . . . . . . . . . . .|135|
|12.3|Code and data cache consumption of various hash functions, on x86 64-bit archi-<br>tecture.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|136|
|12.4|Code and data cache consumption of various hash functions, on x86 32-bit archi-<br>tecture.<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|137|
|12.5|Code and data cache consumption of various hash functions, on MiPS architecture.|137|

12 

**Part 2.B.1** 

**A Complete Written Specification of the Algorithm** 

13 

## **Chapter 1** 

# **Complete Description of Shabal** 

#### **Contents** 

|**2.1**|**Con**|**ventions . . . . . . . . . . . . . . . . . . . . . . . . . **|**. . . . . . . . .**<br>**20**|
|---|---|---|---|
||2.1.1|Endianess . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>20|
||2.1.2|Notation. . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>21|
|**2.2**|**Des**|**cription of the Mode of Operation . . . . . . . . . **|**. . . . . . . . .**<br>**22**|
||2.2.1|Description . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>22|
||2.2.2|A High-Level View . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>25|
||2.2.3|Security Results<br>. . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>25|
|**2.3**|**Spe**|**cifying the Hash Function Shabal**<br>**. . . . . . . . . **|**. . . . . . . . .**<br>**25**|
||2.3.1|Overview<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>25|
||2.3.2|The Keyed Permutation . . . . . . . . . . . . . . . . .|. . . . . . . . . .<br>27|
|**2.4**|**Tun**|**able Security Parameters**<br>**. . . . . . . . . . . . . . **|**. . . . . . . . .**<br>**28**|
|**2.5**|**Par**|**ameter Choices in Shabal**<br>**. . . . . . . . . . . . . . **|**. . . . . . . . .**<br>**29**|

In this section, we describe our candidate function to the NIST competition, which we facetiously baptized Shabal. The name of our algorithm was chosen as a tribute to S´ebastien Chabal, a French rugby player known for his aggressive playing as well as for his beard and long hair which got him the nickname of “Caveman”. 

This section contains the description of our algorithm. We also explain intuitions behind the reasons that made us shape Shabal the way it; the alternative possibilities and precise explanations for our design choices are dedicated to Chapter 4. Moreover, the description of Shabal may be easier to understand using the patterns given in Chapter 3 (one can also take a look at the detailed execution trace given in Appendix B). Implementation tricks aiming at simplifying or accelerating your Shabal implementation are discussed in Chapter 7. Finally, basic implementation is provided in Appendix A. 

### **2.1 Conventions** 

#### **2.1.1 Endianess** 

The input of Shabal is an ordered sequence of bits of arbitrary length. An empty sequence is allowed; Shabal accommodates to bitstreams of any length — however we evaluated its security only for inputs of length smaller than 2<sup>73</sup> bits. The input length can be any integer value and is not restricted to multiples of 8. Given a sequence of bits, bits are numbered by their index, the first bit having index 0. We use the terms _left_ and _right_ to describe an ordered sequence of bits: the first bit in the sequence is called the _leftmost_ bit, the last bit is the _rightmost_ bit. 

20 

The input sequence is first _padded_ : extra bits are added in a way which implies (among other properties) that the length of the padded sequence is not equal to 0 and is a multiple of 32. The padded sequence is then split into groups of eight bits. We will make use of the term _byte_ to denote such groups of bits<sup>1</sup> : the first byte consists of the eight first (leftmost) bits in the padded sequence; the next eight bits are grouped into the second byte, and so on. Since the length of the padded sequence is a multiple of 32, this process yields an integral number of bytes and that number is itself a multiple of 4. Each byte has a _value_ which is an integer between 0 and 255 (inclusive). The byte value is derived from the sequence of eight bits by using representation in base 2, the leftmost bit being most significant: if the eight bits of an octet, from left to right, are denoted _b_ 0, _b_ 1,... _b_ 7 then the value of this byte is equal to<sup>�7</sup> _i_ =0<sup>27</sup><sup>_−ibi_.</sup> 

As an illustration, the padding procedure begins by appending a bit set to 1. Thus, when the input sequence has a length which is a multiple of 8 ( _i.e.,_ the unpadded/raw input sequence is an integral number of bytes), then this additional bit becomes the addition of a new byte which has its upper (leftmost) bit set to 1: the new byte has value 128. 

Many protocols and software platforms define data as streams of bytes and not individual bits. On such architectures, the process of grouping bits together into bytes is assumed to have already taken place using the conventions discussed above. These conventions directly comply with NIST’s API for reference implementations within the Sha-3 competition; they are also compliant with widespread conventions such as the BER encoding of structures expressed in ASN.1 notation which are ubiquitous to many standards related to X.509. 

When the padded sequence has been converted into a sequence of bytes, these bytes are assembled into groups of four consecutive values: the first (leftmost) four bytes become the first group, the next four bytes become the second group, and so forth. Each group is hereafter called a _32-bit word_ or more simply a _word_ . Since the length of the padded input is a multiple of 32, this process yields an integral number of words. Each word has a _value_ which is derived from the four bytes with the so-called _little-endian_ convention: the first (leftmost) byte is least significant. Thus if the four bytes taken from left to right have values _c_ 0, _c_ 1, _c_ 2 and _c_ 3 — all lying in the range [0 _,_ 255]) then the value of the word is _c_ 0 + 2<sup>8</sup> _c_ 1 + 2<sup>16</sup> _c_ 2 + 2<sup>24</sup> _c_ 3. 

The operations of Shabal are expressed in terms of words. The output of Shabal is a sequence of words which is transformed into bits using the same conventions in reverse order: words become bytes with the little-endian convention and each byte represents a sequence of eight bits, the most significant one being the leftmost bit. Note that the final output bit sequence is truncated to a configurable output length<sup>2</sup> . 

It shall be noted that these conventions for the order of bits within a byte and bytes within a word are identical to those used by the well-known hash function MD5. They are sometimes referred to as _mixed-endian_ : big-endian at the bit level, and little-endian at the byte level. 

#### **2.1.2 Notation** 

In this section, we introduce notation that are extensively used in the remainder of this document. Let _x, y_ be _n_ -bit words ( _n_ = 32 for non-weakened versions of Shabal). We denote by _x ⊕ y_ the bitwise _exclusive or_ (or XOR) of _x_ and _y_ . By _x ∧ y_ we denote the bitwise logical _and_ of _x_ and _y_ . We will also denote by _<u>x</u>_ the complement of _x i.e., x ⊕_ **1** — the notation **1** (bold ’one’) stands for `0xFFFFFFFF` for a 32-bit word. Finally _x_ ≪ _j_ denotes the rotation of _x_ by _j_ bits to the left and _x ≪ j_ denotes the shift of _x_ by _j_ bits to the left. Rotation differs from shift in that bits disappearing on the left side come back on the right side in the former while they are simply erased in the latter (so _x ≪ j_ means that _j_ zero-bits enter from the right). It is expected that _j_ be lower than the bitsize of a word ( _i.e.,_ 32 for non-weakened version of Shabal). If this is not the case, _j_ is reduced modulo the word bitsize before the rotation is carried out. 

All logical operations used in this document are bitwise _i.e.,_ are applied separately on each and every bit in words. We will also use _wordwise_ operations _i.e.,_ operations on words such as addition 

> 1The equivalent term _octet_ is also often encountered in technical documents. 

> 2The intended output length also modifies internal processing. 

21 

and subtraction modulo 2<sup>32</sup> . We will denote additions modulo 2<sup>32</sup> by ⊞ or +, whose meaning will be clear from the context. In other words, if _X_ and _Y_ are arrays of 32-bit words, _X_ + _Y_ means that the result is an array of words containing words of _X_ and _Y_ added together with no carry propagating from one word to the next. The same convention applies for subtraction. 

### **2.2 Description of the Mode of Operation** 

The construction on which Shabal is based makes use of a keyed permutation _P_ and is proven to be indifferentiable from a random oracle. Shabal is entirely defined by this generic construction together with some particular specification of _P_ which we define in Section 2.3. 

Let _ℓh_ be the output length of Shabal. For notational simplicity, we will assume that only multiples of 32 are allowed (and most noticeably 192, 224, 256, 384 and 512). Throughout the rest of this document, Shabal with a message digest of _ℓh_ bits is referred to as Shabal- _ℓh_ as long as _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}_ .<sup>3</sup> 

#### **2.2.1 Description** 

<!-- Start of picture text -->
++ ++ ++ ++<br>W W W W<br>M 1 M 2 M 3 M 4<br>A<br>P P P P<br>B<br>C<br><!-- End of picture text -->

Figure 2.1: The mode of operation: Message rounds 

<!-- Start of picture text -->
++<br>W W W W W H =  H ( M )<br>Mk− 1 Mk Mk Mk Mk<br>A<br>P P P P P<br>B<br>C<br>��� Message rounds ��� ��� Final rounds ���<br><!-- End of picture text -->

Figure 2.2: Final rounds: View 1 

Our hash construction uses an internal buffer divided into three different parts ( _A, B, C_ ) _∈ {_ 0 _,_ 1 _}_<sup>_ℓa_</sup> _× {_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _× {_ 0 _,_ 1 _}_<sup>_ℓm_</sup> which at initialization are set to initial values ( _A_ 0 _, B_ 0 _, C_ 0). An auxiliary buffer _W ∈{_ 0 _,_ 1 _}_<sup>64</sup> is used as a counter to number message blocks. Due to its particular role, _W_ is not considered as a part of the internal buffer. Shabal hashes _ℓm_ -bit message blocks iteratively. The construction uses a keyed permutation _P_ where _P_ : _{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _×{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> _×{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _×_ 

> 3We explicitly consider the output size of 192 bits – which is not a request from NIST – since one may find it to be of particular interest for ECDSA-192. 

22 

<!-- Start of picture text -->
++<br>W W W W W H =  H ( M )<br>Mk− 1 Mk Mk Mk Mk<br>A<br>P P P P P<br>B<br>C<br>��� Message rounds ��� ��� Final rounds ���<br><!-- End of picture text -->

Figure 2.3: Final rounds: View 2 

_{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _→{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> _×{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> . By definition, for any key ( _M, C_ ) _∈{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _×{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> , the function _PM,C_ : ( _A, B_ ) _→PM,C_ ( _A, B_ ) = _P_ ( _M, A, B, C_ ) is a permutation. 

23 

<!-- Start of picture text -->
Description of the Mode of Operation<br>Initialization: ( A, B, C, W )  ← ( A 0 , B 0 , C 0 ,  1) .<br>Padding: Post-pad the message with a bit set to 1 followed by as many 0 bits as required<br>to yield a padded message with an exact number of ℓm -bit blocks.<br>Message rounds: For  w ranging from 1 to  k ( w being equal to  w = 2 32 · W [1]+ W [0]),<br>do:<br>• add: the message is introduced.<br>B ← B  +  Mw,<br>where B ← B  +  Mw means that B and Mw are added wordwise (again, there<br>is no carry from one word to the next).<br>• counter: XOR the counter in A [0] and A [1].<br>A [0]  ← A [0]  ⊕ W [0] , A [1]  ← A [1]  ⊕ W [1] .<br>• permute: apply the keyed permutation.<br>( A, B )  ←PMw,C ( A, B ) .<br>• sub: the message is subtracted.<br>C ← C − Mw,<br>where C ← C − Mw means that C and M are subtracted wordwise.<br>• swap: B and C are exchanged.<br>( B, C )  ← ( C, B ) .<br>Final rounds: At the end of message rounds, perform a series of final rounds: the<br>message round is applied 3 times with the lastly inserted message block Mk , the<br>counter w being left unchanged and fixed to k .<br><!-- End of picture text -->

**Output:** Output words _C_ [16 _− ℓh/_ 32] to _C_ [15]. The contents of _A_ and _B_ are ignored. 

A graphical view of the hash construction is displayed on Figure 2.1. At this stage, note that simple optimizations are possible in the final rounds (see the differences between Figures 2.2 and 2.3): in particular, the last _sub_ operation is removed, the last _swap_ , and the _sub_ and _add_ between applications of _P_ in final rounds. The first picture provides a view on atomic rounds made of sequences of _add, counter, permute, sub, exchange_ operations while the second picture shows a more efficient but somewhat more code-consuming presentation on the final rounds of Shabal. 

The effect of a message round on the internal state is denoted ( _A, B, C, w_ +1) = _R_ ( _Mw, A, B, C, w_ ) or ( _S, w_ + 1) = _R_ ( _Mw, S, w_ ) for short. The effect of final rounds is referred to as _F_ (with the notation ( _S, w_ ) = _F_ ( _Mk, S, w_ )); we remind that the only difference between _R_ and _F_ is that the counter is not incremented in _F_ as opposed to _R_ . 

24 

#### **2.2.2 A High-Level View** 

We give below a more synthetic view of Shabal. 

**Initialization:** ( _A, B, C_ ) _←_ ( _A_ 0 _, B_ 0 _, C_ 0) **Message Rounds:** _M_ = _M_ 1 _, . . . , Mk_ **For** _w_ from 1 to _k_ **do** 1. _B ← B_ + _Mw_ 2. _A ← A ⊕ w_ 3. ( _A, B_ ) _←PMw,C_ ( _A, B_ ) 4. _C ← C − Mw_ 5. ( _B, C_ ) _←_ ( _C, B_ ) **End do Final rounds: For** _i_ from 0 to 2 **do** 1. _B ← B_ + _Mk_ 2. _A ← A ⊕ k_ 3. ( _A, B_ ) _←PMk,C_ ( _A, B_ ) 4. _C ← C − Mk_ 5. ( _B, C_ ) _←_ ( _C, B_ ) **End do Output:** _H_ = msb _ℓh_ ( _C_ ) 

#### **2.2.3 Security Results** 

Chapter 5 focuses on security properties of the mode of operation and provides proofs that Shabal is _(a)_ indifferentiable from a random oracle, _(b)_ collision resistant, _(c)_ preimage resistant and _(d)_ second preimage resistant, assuming that the inner keyed permutation _P_ behaves as a random keyed permutation. All bounds are shown to be optimal in Chapter 11 where we exhibit generic attacks that meet these security bounds. We refer the reader to these sections for more details. 

### **2.3 Specifying the Hash Function Shabal** 

In Section 2.2, we have described the mode of operation on which our proposition Shabal is based. In this section, we describe a number of implementation details which characterize Shabal. Although other implementation choices of the mode could be defined as well to yield other hash functions, we stress that the design choices we make in what follows are integral parts of Shabal and that any other setting cannot be considered as being Shabal. 

#### **2.3.1 Overview** 

Shabal only defines message blocks of _ℓm_ = 512 bits. For two tunable security parameters _p ≥_ 2 and _r ≥_ 2, we define the internal state buffer as a ( _A, B, C_ ) which is a (1024 + 32 _r_ )-bit buffer viewed as arrays of 32-bit words. More precisely, _B_ and _C_ are 16-word arrays while _A_ is an _r_ -word 

25 

buffer. We thus have _ℓa_ = 32 _r_ . The counter _W_ , which is not considered as a part of the internal buffer, is viewed as a 2-word buffer. Shabal is then defined as follows. 

#### Description of Shabal (prefix approach) 

**Initialization:** ( _A, B, C_ ) _←_ 0, _w ←−_ 1. 

**Prefixing:** The message is prefixed with 32 words set to fixed values ranging from _ℓh_ (written as a 32-bit word) to _ℓh_ + 31 where _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}_ is the output length. 

<!-- Start of picture text -->
Padding: Post-pad the input message with a bit set to 1 followed by as many 0 bits as<br>required so that the padded message can be split into 512-bit blocks.<br>Message rounds: For  w  ranging from  − 1 to  k  ( w  being equal to  w = 2 32 ·W [1]+ W [0]),<br>do:<br>• add: the current message block is inserted.<br>B ← B  +  Mw.<br>• counter: XOR the counter in A [0] and A [1].<br>A [0]  ← A [0]  ⊕ W [0] , A [1]  ← A [1]  ⊕ W [1] .<br>• permute: apply the keyed permutation described in Section 2.3.2.<br>( A, B )  ←PMw,C ( A, B ) .<br>• sub: the message block is subtracted.<br>C ← C − Mw.<br>• swap: B and C are swapped.<br>( B, C )  ← ( C, B ) .<br><!-- End of picture text -->

**Final rounds:** When all message blocks are treated, perform 3 final rounds. A final round performs a message round with the last message block _Mk_ , the counter _w_ being fixed to the total number _k_ of message blocks inserted in the message insertion phase. 

**Output:** Finally output the words _C_ [16 _− ℓh/_ 32] to _C_ [15] in that order. The contents of _A_ and _B_ are ignored. 

The initialization value of _w_ is chosen to be _−_ 1 so that once the 2-block prefix message is treated, the index of the first input message block is _w_ = 1. Throughout the document, the prefix is denoted by ( _M−_ 1 _, M_ 0). In particular, it holds that _M−_ 1[0] = _ℓh_ , _M−_ 1[15] = _ℓh_ + 15, _M_ 0[0] = _ℓh_ + 16 and _M_ 0[15] = _ℓh_ + 31. 

It is worth noticing that, as an alternative to the above, one may ignore the prefixing of the message and precompute the contents ( _A, B, C_ ) = IV _ℓh_ of the internal state resulting from hashing the two blocks ( _M−_ 1 _, M_ 0). The simplified algorithm is described below. 

26 

Description of Shabal (IV approach) 

**Initialization:** ( _A, B, C_ ) _←_ IV _ℓh_ , _w ←_ 1. 

**Padding:** Post-pad the input message with a bit set to 1 followed by as many 0 bits as required so that the padded message can be split into 512-bit blocks. 

**Message rounds:** For _w_ ranging from 1 to _k_ ( _w_ being equal to _w_ = 2<sup>32</sup> _· W_ [1]+ _W_ [0]), do: 

_•_ **add:** the current message block is inserted. 

_B ← B_ + _Mw._ 

_A_ [0] _← A_ [0] _⊕ W_ [0] _, A_ [1] _← A_ [1] _⊕ W_ [1] _._ 

_•_ **permute:** apply the keyed permutation described in Section 2.3.2. ( _A, B_ ) _←PMw,C_ ( _A, B_ ) _._ 

_•_ **sub:** the message is subtracted. 

_C ← C − Mw. •_ **swap:** _B_ and _C_ are swapped. ( _B, C_ ) _←_ ( _C, B_ ) _._ 

**Final rounds:** When all message blocks are treated, perform 3 final rounds. A final round performs a message round with the last message block _Mk_ , the counter _w_ being fixed to the total number _k_ of message blocks inserted in the message insertion phase. 

**Output:** Finally output the words _C_ [16 _− ℓh/_ 32] to _C_ [15] in that order. The contents of _A_ and _B_ are ignored. 

In Section 3.1, the initialization vectors IV _ℓh_ are provided for all supported values of _ℓh_ . Let 

us stress once again that these two ways of defining Shabal are strictly equivalent. Depending on several parameters (see Section 4.5) among which performance tradeoffs, it is left as an implementation choice to follow one or the other approach. 

#### **2.3.2 The Keyed Permutation** 

We now move on to the description of the inner keyed permutation of Shabal. We make use of an NLFSR-based construction (see also Figure 2.4), whose design rationale are provided in Section 4.2.1. 

27 

<mark>Keyed Permutation</mark> _<mark>P</mark>_ <mark>used in Shabal</mark> **Input:** _M, A, B, C_ **Output:** _A, B_ For _i_ from 0 to 15, do: _• B_ [ _i_ ] _← B_ [ _i_ ] ≪ 17 Next _i_ For _j_ from 0 to _p −_ 1, do: _•_ For _i_ from 0 to 15, do: **–** Compute _A_ [ _i_ + 16 _j_ mod _r_ ] _← U_ � _A_ [ _i_ + 16 _j_ mod _r_ ] _⊕V_ ( _A_ [ _i −_ 1 + 16 _j_ mod _r_ ] ≪ 15) _⊕ C_ [8 _− i_ mod 16]� _⊕ B_ [ _i_ + _o_ 1 mod 16] _⊕_ ( _B_ [ _i_ + _o_ 2 mod 16] _∧ B_ [ _i_ + _o_ 3 mod 16]) _⊕ M_ [ _i_ ] where ( _o_ 1 _, o_ 2 _, o_ 3) = (13 _,_ 9 _,_ 6) are offset values discussed later in Section 4.3. **–** _B_ [ _i_ ] _←_ ( _B_ [ _i_ ] ≪ 1) _⊕ A_ [ _i_ + 16 _j_ mod _r_ ] _•_ Next _i_ Next _j_ For _j_ from 0 to 35, do: _• A_ [ _j_ mod _r_ ] _← A_ [ _j_ mod _r_ ] + _C_ [ _j_ + 3 mod 16] Next _j_ 

In the above description, _U_ : _x �→_ 3 _× x_ mod 2<sup>32</sup> and _V_ : _x �→_ 5 _× x_ mod 2<sup>32</sup> are used as nonlinear functions (see Section 4.2.3). Offset values ( _o_ 1 _, o_ 2 _, o_ 3) = (13 _,_ 9 _,_ 6) are carefully chosen as explained in Section 4.3. Parameters ( _p, r_ ) may have several acceptable values _p ≥_ 2 and _r ≥_ 2; however Shabal defines specific values for ( _p, r_ ) as discussed in Section 2.5. 

The final loop of _P_ ( _i.e.,_ where _A_ [ _j_ mod _r_ ] _← A_ [ _j_ mod _r_ ]+ _C_ [3+ _j_ mod 16]) is not fully generic towards the parameter _r_ as explained in Section 4.2.6. Changing a value for _r_ that differs from the one given in Section 2.5 implies applying modifications to this last loop. 

### **2.4 Tunable Security Parameters** 

Shabal features two security parameters: 

- **Parameter** _p_ **:** the number of loops performed within one application of the keyed permutation; larger values of _p_ provide better security guarantees. 

- **Parameter** _r_ **:** the remanence of _A_ . The minimal value for _r_ is 2 due to the insertion of the 64-bit counter _W_ in _A_ [0] and _A_ [1]. _r_ corresponds to a security margin as extensively discussed in Chapter 5. 

28 

<!-- Start of picture text -->
V ≪ 15<br>A<br>+ 0 11<br>+<br>C<br>0 8 15<br>U<br>M<br>+ 0 15<br>+<br>+ 0xFF...F +<br>x<br>y<br>B<br>0 6 9 13 15 +<br>≪ 1<br><!-- End of picture text -->

Figure 2.4: Main structure of the keyed permutation used in Shabal. 

In our security analysis, we only consider the case where 

since otherwise certain words of _A_ are more intensively used than others. 

We note however that parameters _p_ and _r_ have a different impact on the security of the hash function. Parameter _r increases_ the _capacity_ (in the sense of [7]) of the mode of operation of Shabal detailed in Section 2.2. Increasing _r_ is therefore a direct way to add a (provable security minded) security margin. However, we also note that too large a value for _r_ is not compatible with a correct level of diffusion and real-world security (furthermore, _r_ is structurally upper-bounded by 16 _p_ ). On the contrary, parameter _p_ does not increase the size of the internal state but has the effect to _strengthen_ the keyed permutation. Larger enough values of _p_ make the permutation behave in a less controllable way. In a sense, increasing _p_ makes the permutation closer to an idealized permutation. This is true up to a certain threshold above which taking larger values for _p_ will not increase security anymore. 

### **2.5 Parameter Choices in Shabal** 

The submitted algorithm Shabal strictly uses ( _p, r_ ) = (3 _,_ 12). Other choices of parameters must _not_ be considered as Shabal, even though their study may reveal interesting from a research perspective. In Shabal, it always holds that 16 _p_ = 0 mod _r_ so that all the words of _A_ are used equally often. 

29 

## **Chapter 3** 

# **Some Test Patterns** 

#### **Contents** 

|**3.1**|**The **|**Diferent Initialization Vectors**<br>**. . . . . . . . . . . . . . . . . . .**<br>**31**|
|---|---|---|
||3.1.1|Initialization Vector for Shabal-192 . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.2|Initialization Vector for Shabal-224 . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.3|Initialization Vector for Shabal-256 . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.4|Initialization Vector for Shabal-384 . . . . . . . . . . . . . . . . . . . . .<br>31|
||3.1.5|Initialization Vector for Shabal-512 . . . . . . . . . . . . . . . . . . . . .<br>31|
|**3.2**|**Final**|**States and Outputs when Hashing Message A**<br>**. . . . . . . . .**<br>**32**|
||3.2.1|Final State and Output for Shabal-192 . . . . . . . . . . . . . . . . . . .<br>32|
||3.2.2|Final State and Output for Shabal-224 . . . . . . . . . . . . . . . . . . .<br>32|
||3.2.3|Final State and Output for Shabal-256 . . . . . . . . . . . . . . . . . . .<br>32|
||3.2.4|Final State and Output for Shabal-384 . . . . . . . . . . . . . . . . . . .<br>33|
||3.2.5|Final State and Output for Shabal-512 . . . . . . . . . . . . . . . . . . .<br>33|
|**3.3**|**Final**|**States and Outputs when Hashing Message B**<br>**. . . . . . . . .**<br>**33**|
||3.3.1|Final State and Output for Shabal-192 . . . . . . . . . . . . . . . . . . .<br>33|
||3.3.2|Final State and Output for Shabal-224 . . . . . . . . . . . . . . . . . . .<br>34|
||3.3.3|Final State and Output for Shabal-256 . . . . . . . . . . . . . . . . . . .<br>34|
||3.3.4|Final State and Output for Shabal-384 . . . . . . . . . . . . . . . . . . .<br>34|
||3.3.5|Final State and Output for Shabal-512 . . . . . . . . . . . . . . . . . . .<br>35|
|**3.4**|**Inter**|**mediate States for Messages A and B . . . . . . . . . . . . . . .**<br>**35**|

We give in this chapter, for all output bitsizes _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}_ , different test patterns which everyone’s implementation must comply with. These data include the initialization vector IV _ℓh_ to use when writing Shabal in the IV manner, as well as the final content of the state and the hash result when hashing two example messages. The first example message (message A) is an all-zero full block, which may equivalently be denoted as 01<sup>512</sup> (bit list), 08<sup>64</sup> (byte list) or 032<sup>16</sup> (word list). The second example message (message B) is a 102-byte string defined as: 

##### “ `abcdefghijklmnopqrstuvwxyz-0123456789-ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-abcdefghijklmnopqrstuvwxyz` ” 

Note that message B is longer than one block but does not exactly fit on two blocks. 

With the aim to facilitate the writing and debugging of Shabal, we also provide the complete lists of all successive intermediate states when hashing message A and message B with all five functions Shabal- _ℓh_ (see in Appendix B). 

30 

### **3.1 The Initialization Vectors** 

#### **3.1.1 Initialization Vector for Shabal-192** 

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

#### **3.1.2 Initialization Vector for Shabal-224** 

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

#### **3.1.3 Initialization Vector for Shabal-256** 

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

#### **3.1.4 Initialization Vector for Shabal-384** 

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

#### **3.1.5 Initialization Vector for Shabal-512** 

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

31 

### **3.2 Final States and Outputs when Hashing Message A** 

The value of message A, expressed as a list of bytes, is the following: 

- `M1 : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00` 

Note that for each output length the hash value of message A is given twice: first as a word list directly extracted from the end of the state buffer C, then as a byte list expressed in accordance with its _little-endian_ representation. 

#### **3.2.1 Final State and Output for Shabal-192** 

- `A : A38C0C63 17C2CAE8 3248572C 1C89CAD5 176ED597 B242B8AD 73298C22 7ADF1817 00D909DA 61AD8518 90266914 9DC1F617` 

- `B : 260A3D42 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `C : F91EEE5E 99DCC78C 82F72599 8CACD775 09544255 ED275CF3 0166F95E 2C375AFA 49AAFBE0 4D9C01C6 CB6E700F CE4DCF97 D2BBBF00 0C5364FB B40C8732 0D733948` 

- `H : CB6E700F CE4DCF97 D2BBBF00 0C5364FB B40C8732 0D733948` 

- `H : 0F 70 6E CB 97 CF 4D CE 00 BF BB D2 FB 64 53 0C 32 87 0C B4 48 39 73 0D` 

#### **3.2.2 Final State and Output for Shabal-224** 

- `A : 08FC66FC CE392D14 42C29F35 5649D86A DCD65214 9A423F72 99D2F688 5073E130 1E1F9B61 A28A416E 9C9572AB C3A9B2BC` 

- `B : 33D58779 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `C : BE6AC9DC 86AFB8BB 300C6C1B 237F0C8C 6DEF5EEF 599CA070 540040F7 EEA985E4 4A5B8375 14A6DD99 E8D207F9 F7187681 326F6930 8BCAAE00 25F4855F 3120BA43` 

- `H : 14A6DD99 E8D207F9 F7187681 326F6930 8BCAAE00 25F4855F 3120BA43` 

- `H : 99 DD A6 14 F9 07 D2 E8 81 76 18 F7 30 69 6F 32 00 AE CA 8B 5F 85 F4 25 43 BA 20 31` 

#### **3.2.3 Final State and Output for Shabal-256** 

- `A : 3DBA182A D0D6787E DAD8F4C9 CC065328 A36A08C7 902C794E 43E5A220 E2F378F1 1E35B4C3 EF6B834E 8E442A11 6922E895` 

- `B : 66DF96F1 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `C : 57E837B3 3B2C6ACA E0358DC2 2BD758E9 30F7A2ED DF3516C7 253CB0E0 1A1A98FC C0088FDA 9ABA672A 79D0BD56 07AE488E 095E2114 06855B3B 1877A349 A2543F99` 

- `H : C0088FDA 9ABA672A 79D0BD56 07AE488E 095E2114 06855B3B 1877A349 A2543F99` 

- `H : DA 8F 08 C0 2A 67 BA 9A 56 BD D0 79 8E 48 AE 07 14 21 5E 09 3B 5B 85 06 49 A3 77 18 99 3F 54 A2` 

32 

#### **3.2.4 Final State and Output for Shabal-384** 

- `A : 37661E10 1BEDBBD5 B022D077 CB1781BD 23DCFA84 AF4946EC 9C681ADD 8C48B88C 6BC4D0CB 1F4A95CD 0F2C5CD4 D1BC38C6` 

- `B : CA3AFDBC 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `C : D4163C6A 49313E63 0D1ACCBE 7AD73B3E 3312DE9D DA850D91 03785C3A C611B112 5D1BCAFC 033755D2 3B8EE05E 15251E4E 636A724F F0A8E584 4AABEAAF 122FC0C4` 

- `H : 3312DE9D DA850D91 03785C3A C611B112 5D1BCAFC 033755D2 3B8EE05E 15251E4E 636A724F F0A8E584 4AABEAAF 122FC0C4` 

- `H : 9D DE 12 33 91 0D 85 DA 3A 5C 78 03 12 B1 11 C6 FC CA 1B 5D D2 55 37 03 5E E0 8E 3B 4E 1E 25 15 4F 72 6A 63 84 E5 A8 F0 AF EA AB 4A C4 C0 2F 12` 

#### **3.2.5 Final State and Output for Shabal-512** 

- `A : 1FD517B4 18EE0662 002DA3F7 3C864C42 00BDBC17 D3A91349 84B98D58 DB0A255C EA84933C 78858700 4E1BD28E 22E17C53` 

- `B : D90A51B3 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `C : C6168015 0A3F1FC8 688DD952 8E9E2FED 23EF9578 BCE2A7CB A5D80961 E6C9E632 9701A5A6 F037B89F 20C6C44E DC7931E7 2BB5AB82 B3ADCD32 9CE25056 22305E98` 

- `H : C6168015 0A3F1FC8 688DD952 8E9E2FED 23EF9578 BCE2A7CB A5D80961 E6C9E632 9701A5A6 F037B89F 20C6C44E DC7931E7 2BB5AB82 B3ADCD32 9CE25056 22305E98` 

- `H : 15 80 16 C6 C8 1F 3F 0A 52 D9 8D 68 ED 2F 9E 8E 78 95 EF 23 CB A7 E2 BC 61 09 D8 A5 32 E6 C9 E6 A6 A5 01 97 9F B8 37 F0 4E C4 C6 20 E7 31 79 DC 82 AB B5 2B 32 CD AD B3 56 50 E2 9C 98 5E 30 22` 

### **3.3 Final States and Outputs when Hashing Message B** 

The value of message B, expressed as a list of bytes, is the following: 

- `M1 : 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 78 79 7A 2D 30 31 32 33 34 35 36 37 38 39 2D 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50 51 52 53 54 55 56 57 58 59 5A` 

- `M2 : 2D 30 31 32 33 34 35 36 37 38 39 2D 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 78 79 7A` 

Note that for each output length the hash value of message B is given twice: first as a word list directly extracted from the end of the state buffer C, then as a byte list expressed in accordance with its _little-endian_ representation. 

#### **3.3.1 Final State and Output for Shabal-192** 

- `A : F9D98DBE 30B70551 86CB5CAF BDB2F590 AF169E21 BD8AF9BE 9EEA9756 F7D08C3A C51970D2 26C8004C 5BFD5D4B 24891C29` 

- `B : 34E18578 04C53BCB FC371288 11A6D737 61190916 E719D732 66662512 9D6323C1 0E02D0B3 F982ED56 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

33 

- `C : 593CCDF8 F2E993B0 DD79ADFB A855551E 2B63F3B6 24A62526 E88CEC5E 6FD09762 D678E2F8 2953038A 79AE0F69 76956D22 B4FDE80A 37058CF5 55561711 157B307D` 

- `H : 79AE0F69 76956D22 B4FDE80A 37058CF5 55561711 157B307D` 

- `H : 69 0F AE 79 22 6D 95 76 0A E8 FD B4 F5 8C 05 37 11 17 56 55 7D 30 7B 15` 

#### **3.3.2 Final State and Output for Shabal-224** 

- `A : 894924F9 B9663D4A 3211E95C E3077A9D 12706153 2CE27DCF CE8EC0DB 90F7B2A7 0AEA318D D66C462E 90837F7A 506E9AC9` 

- `B : 9E9BFB65 66B89207 696D88EA 677D16EF 5A9BE34F D3618C82 FBCC3A81 AA0538CC A574BC1A 1593FD54 A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `C : E3BD6C0F E3B4A56E E9349EB2 29739374 5522513E B4754483 8D7C035E 9236E8EE 3A11ED4E 8D2DD6C7 B474342A 1AD1A9F4 433DDB52 CF58F15B 565D4C45 F525711D` 

- `H : 8D2DD6C7 B474342A 1AD1A9F4 433DDB52 CF58F15B 565D4C45 F525711D` 

- `H : C7 D6 2D 8D 2A 34 74 B4 F4 A9 D1 1A 52 DB 3D 43 5B F1 58 CF 45 4C 5D 56 1D 71 25 F5` 

#### **3.3.3 Final State and Output for Shabal-256** 

- `A : 08ABA604 9C4035C7 8B73310B B3795EF0 E6B83DEB 7A57B2AB 31D05460 23D8D113 7630AEDA DCE8C11C A7146FD5 F5A59553` 

- `B : DA91E764 394C58F5 B1A9C163 7CADCDD5 25514A39 B6E44767 F91D226C 29C46011 6B9D04BB CA590BB3 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `C : C539CC9B CA52634F 214754DE 19A73AD2 AAF2D843 91D84323 7C4EFAFB 54D18CAB BF349FB4 304C8651 6CC43C53 DE2B54C2 D06FF9C2 9A535C6F 58AD6EFF 7A32F783` 

- `H : BF349FB4 304C8651 6CC43C53 DE2B54C2 D06FF9C2 9A535C6F 58AD6EFF 7A32F783` 

- `H : B4 9F 34 BF 51 86 4C 30 53 3C C4 6C C2 54 2B DE C2 F9 6F D0 6F 5C 53 9A FF 6E AD 58 83 F7 32 7A` 

#### **3.3.4 Final State and Output for Shabal-384** 

- `A : E0042A7C 232B50B8 3DD8F7C8 6CEA315D E27E7E4E E86814E8 F6FDAC30 6CC5A5C3 396FDAA7 70EB195E E7B2616E BE5A25FA` 

- `B : D2EA74CA 12F9F6AD 75E6BE06 A16ABFF6 060268AB F16FA81F 83DA0DA6 D37D8E46 BC83E112 3414D903 AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `C : 6D085ED6 71C06B61 6D009973 9317C3EB 0E2C0130 0B46DC3E C22786D7 D24409C3 9A6689A1 977A2DFA 772FEF13 A474444C CECBF13A 24B4FAC5 F073088C A0EBFB38` 

- `H : 0E2C0130 0B46DC3E C22786D7 D24409C3 9A6689A1 977A2DFA 772FEF13 A474444C CECBF13A 24B4FAC5 F073088C A0EBFB38` 

- `H : 30 01 2C 0E 3E DC 46 0B D7 86 27 C2 C3 09 44 D2 A1 89 66 9A FA 2D 7A 97 13 EF 2F 77 4C 44 74 A4 3A F1 CB CE C5 FA B4 24 8C 08 73 F0 38 FB EB A0` 

34 

#### **3.3.5 Final State and Output for Shabal-512** 

- `A : 706F3E32 22946DE1 15E78C72 2CE64CAC 5E568D8A 9C96B1AC 8F9951F0 B0FAA007 E3443293 15CCF7A7 0D0736D8 4930715B` 

- `B : 27D27CC5 240FAAD1 6AE08A5D DD1A5439 BE5864F8 F0671108 F8881886 85D62586 9E795F12 E6068F6B 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `C : 7F6F7E67 F00AD712 2F6635B3 5168B559 663E65F3 86337D64 4301DADF A5C84C25 94213EDB 716F8C06 607B7D59 B4224D98 D9601F7A CBDFA81C B9655D17 CFCE5973` 

- `H : 7F6F7E67 F00AD712 2F6635B3 5168B559 663E65F3 86337D64 4301DADF A5C84C25 94213EDB 716F8C06 607B7D59 B4224D98 D9601F7A CBDFA81C B9655D17 CFCE5973` 

- `H : 67 7E 6F 7F 12 D7 0A F0 B3 35 66 2F 59 B5 68 51 F3 65 3E 66 64 7D 33 86 DF DA 01 43 25 4C C8 A5 DB 3E 21 94 06 8C 6F 71 59 7D 7B 60 98 4D 22 B4 7A 1F 60 D9 1C A8 DF CB 17 5D 65 B9 73 59 CE CF` 

### **3.4 Intermediate States for Messages A and B** 

A complete follow-up of the execution of each Shabal- _ℓh_ on both messages A and B is given in Appendix B. 

35 

## **Chapter 4** 

#### **4.1.1 A Short Story about the Mode of Operation of Shabal** 

It may not be obvious at first sight to understand the design rationale behind the operating mode of Section 2.2; this mode of operation is the result of a long series of works which we sum up in this section. 

Before opting for the final mode previously described, we were planning to rely on the mode of operation shown on Figure 4.1 which we retrospectively call Old Mode 1. Old Mode 1 features a double message insertion, and a large keyed permutation. The idea of relying on multiple message insertion is not new (it exists for example in RadioGat´un): a direct effect of double insertion is to increase the diffusion of input differences<sup>1</sup> , which hardens the search for differential paths. Old Mode 1 also exploits the idea of an _accumulator_ ( _X_ on Figure 4.1) which collects input bits from all message blocks and prevents internal collisions from happening after one round of message insertion. 

Interestingly, this mode turned out to be indifferentiable from a random oracle, a must-have property. Also, provable resistance to collision, preimage and second preimage attacks can be shown in the ideal cipher model. Besides, the core object of Old Mode 1, a keyed permutation, is more efficiently instantiated than any unkeyed permutation defined on the same input domain since the field holding the parameter (key) does not require to be written and given as output. One may thus expect to realize better throughputs than with a basic sponge construction such as [7]. On the other hand, the domain of the keyed permutation still has to be very large to meet satisfactory security bounds and therefore Old Mode 1 leaves the impression that there is room for more advanced improvements. 

<!-- Start of picture text -->
M 1 M 2 Mk H<br>X<br>Y<br>P P P P<br>Z<br><!-- End of picture text -->

Figure 4.1: Mode of Operation Old Mode 1 

We later found how to refine Old Mode 1 into a more efficient mode of operation Old Mode 2 depicted on Figure 4.2. Old Mode 2 makes use of a smaller permutation than Old Mode 1 since a fraction of the input space has been converted into a part of the key space, with now 2 parameters instead of just one. Relying on a keyed permutation with optimally small input space is clearly beneficial to both security and performance, since it is much easier to construct efficient keyed permutations on smaller domains. Like Old Mode 1, Old Mode 2 turned out to be indifferentiable. But in addition to that, interestingly, this mode happens to support provable collision, preimage and second preimage resistance, although the simulators are much more intricate to conceive than in the case of Old Mode 1. 

> 1with double insertion, message modifications that one makes to correct differences in one round are also to be corrected in next round and so on. 

37 

<!-- Start of picture text -->
M 1 M 2 Mk− 1 Mk H<br>X<br>Y P P P P P<br>Z<br><!-- End of picture text -->

Figure 4.2: Mode of Operation Old Mode 2 

It finally became clear to us that the variable _X_ played no significant role in the security of Old Mode 2. Said differently, we found that Old Mode 2 could be reformulated to yield an equivalent mode which does not require to store and update _X_ . At any point in time indeed, an attacker is always able to set _X_ to a prescribed value _m_ by inserting _M_ = _m − X_ . Old Mode 2 then replaces variable _Y_ with _Y − X_ + _m_ . As a consequence, the mode of operation behaves exactly as if variables ( _X, Y_ ) were replaced with a single variable _Y − X_ . However, if one wants to continue the sequence of atomic blocks _i.e.,_ in order to construct the final value for _Y − X_ , it is requested to subtract the value _X_ (which is _m_ ) from the value of _Y_ (which is equal to the value of _Z_ before variables are swapped). We then studied the mode described in Section 2.2 as an evolution of Old Mode 2, where _Y − X_ was renamed _B_ , _m_ was renamed _M_ and _Z_ was renamed _C_ ; _A_ corresponds to a buffer that does not appear on the figures describing Old Mode 1 and 2. 

Further options such as the inclusion of a 64-bit counter _W_ or of a series of final rounds emerged later with the search for lightweight tricks that would strengthened security: the presence of a counter improves resistance against all forms of attacks as shown in Section 5.6; the implementation of final rounds arose from various discussions on the expected and actual degree (in the sense of Boolean functions) of the output bits, see Section 4.4. 

### **4.2 Designing the Keyed Permutation** _P_ 

In this section, we explain how the keyed permutation _P_ was designed. Let us start by saying that many approaches would be equally sound to instantiate _P_ . In this respect, we clearly made very specific choices and several features could possibly have led to other interesting constructions without necessarily decreasing security. Each time we had to make a choice between several 

38 

equivalent approaches, we let our decision be dictated by our quest for simplicity and performance. 

#### **4.2.1 An NLFSR-based Structure** 

The keyed permutation ( _A, B_ ) _�→PM,C_ ( _A, B_ ) is basically made upon a nonlinear feedback shift register (NLFSR). Both variables _A_ and _B_ are actually updated as 16-word NLFSRs whose nonlinear feedback functions depend on parameters _M_ and _C_ . However, the specificity of our design resides in that these NLFSRs are not independent from each other (we refer the reader to Figure 2.4 for a view on the two NLFSRs). The two feedback functions interact with one another: _B_ influences the feedback of register _A_ and conversely. 

#### **4.2.2 A Permutation** 

In order to guarantee that message rounds do not cause the internal state to lose entropy, we wanted _P_ to be a permutation for any fixed choice of parameters _M_ and _C_ . This property is ensured by the NLFSR-based structure used for both registers _A_ and _B_ . Function _P_ can actually be decomposed into an initial ≪ 17 rotation applied to input _B_ : 

and 16 _p_ steps of 

for the following elementary step function _π_ : 

where (remind that ( _o_ 1 _, o_ 2 _, o_ 3) stands for a fixed tuple of offsets) 

_Ar_ = _U_ ( _A_ 0 _⊕V_ ( _Ar−_ 1 ≪ 15) _⊕ C_ 8) _⊕ Bo_ 1 _⊕_ ( _Bo_ 2 _∧ Bo_ 3) _⊕ M_ 0 _B_ 16 = ( _B_ 0 ≪ 1) _⊕ Ar._ 

_P_ ends with a final transformation of the internal state 

( _A, B, C_ ) _�→_ ( _A_ + _σ_ ( _C_ ) _, B, C_ ) 

where _σ_ ( _C_ ) is an _r_ -word vector derived from the 16 words of _C_ . 

Thus, _P_ is a permutation if and only if the elementary step function _π_ is a permutation. From the previous description, it appears that, for given values of _M_ and _C_ , _πM,C_ can be inverted by using: 

_B_ 0 = ( _B_ 16 _⊕ Ar_ ) ≫ 1 _A_ 0 = _V_ ( _Ar−_ 1 ≪ 15) _⊕ C_ 8 _⊕U_<sup>_−_1</sup> ( _Ar ⊕ Bo_ 1 _⊕_ ( _Bo_ 2 _∧ Bo_ 3) _⊕ M_ 0) _._ 

Since any step of _P_ can be inverted by the previous formula, _P_ is a permutation. 

#### **4.2.3 Register** _A_ 

The role of register _A_ is to improve the effect of diffusion: if a difference occurs in one word of _A_ , it has to be corrected in the following words (which requires to include a difference in the corresponding message word), otherwise the difference will spread on and lead to an avalanche 

The feedback function in register _A_ is defined by: 

_At_ + _r_ = _U_ ( _At ⊕V_ ( _At_ + _r−_ 1 ≪ 15) _⊕ C_ 8 _−t_ ) _⊕G_ ( _Bo_ 1+ _t, Bo_ 2+ _t, Bo_ 3+ _t_ ) _⊕ Mt, ∀t ≥_ 0 

for some function _G_ whose characteristics are discussed in Section 4.2.5. We first provide more detail on the choices of all elementary operations performed while computing the feedback word. 

39 

##### **Introducing** _A_ **.** 

For performance reasons, only two taps of register _A_ are involved in the feedback function: the use of _At_ is required to ensure that _P_ is a permutation; _At_ + _r−_ 1 has been chosen for the second involved word in order to make that any difference introduced in _A_ by the feedback function immediately impacts the next step. These two words must affect the feedback in a nonlinear manner. Thus, some nonlinear functions, _U_ and _V_ , are used, whose choice is detailed below. Finally, the feedback function involves a rotated version of _At_ + _r−_ 1. This rotation aims at moving the least-significant bits of the words of _A_ to another position since the least-significant coordinate functions of _U_ and _V_ are both linear. 

##### **Introducing** _C_ **.** 

The words of _C_ are introduced by a XOR, as normally there is no real control over _C_ . But, the words of _C_ are not introduced in the same order as the words of _A_ . The reason is that, at Round _t_ , register _C_ corresponds to the _B_ output of the previous round. Then, at the beginning of Round _t_ , register _A_ has a linear dependency with the last _r_ words of _C_ . Most notably, if an attacker succeeds in finding a differential trail such that the last _r_ words of _C_ and the corresponding words of _A_ have the same differences at the end of Round ( _t −_ 1), these differences might cancel at Round _t_ if the words of _A_ and _C_ are taken in the same order. That is why, at each round, _C_ 8 _−i_ mod 16 is introduced at Step _i_ instead of _Ci_ mod 16. 

##### **Introducing** _M_ **.** 

_M_ is introduced directly by a XOR, so that any difference in _M_ will affect _A_ . The initial ≪ 17 rotation applied to _B_ before the first step guarantees that similar difference patterns in _B_ and _M_ do not cancel (this might be possible without the rotation by choosing appropriate linear approximations of _G_ ). 

##### **Using** _U_ **and** _V_ **as S-Boxes.** 

The feedback function of register _A_ uses two simple functions _U_ ( _x_ ) = 3 _× x_ mod 2<sup>32</sup> and _V_ ( _x_ ) = 5 _× x_ mod 2<sup>32</sup> whose goal is to increase both the degree and the nonlinearity. Their presence hardens the search for simple and high-probability differentials of the type “modify-then-correct”. 

Using two nonlinear functions instead of just one allows to guarantee that inserting two different message blocks will cause at least one difference between the inputs of one of the executions of _U_ or _V_ after two rounds. This property is proved in Section 11.3.2 (see Theorem 7) and cannot be derived when a single function, _e.g., U_ , is used. 

_U_ and _V_ have been chosen to be as simple as possible: they can easily be hard-coded under the form of a bit shift followed by addition, or equivalently as two additions for _U_ and three additions for _V_ if the multiplication by a small constant is not available on the hardware platform. The choice of nonlinear functions which can be implemented in software with simple CPU operations avoids the use of look-up tables which would have increased the code size, see Section 12.3.3. 

Moreover, the absolute constants 3 and 5 used in both multiplications are invertible modulo 2<sup>32</sup> , implying that _U_ and _V_ are permutations, and so no entropy on _x_ is lost. Another advantage of these two functions is that they cannot transform a symmetric difference, _i.e.,_ the all-0 or the all-1 word, into a symmetric difference as proven in Proposition 1 of Section 11.3.2. 

#### **4.2.4 Register** _B_ 

The nonlinear feedback function in register _B_ is defined by: 

_Bt_ +16 = ( _Bt_ ≪ 1) _⊕ At_ + _r, ∀t ≥_ 0 _._ 

40 

**Introducing** _A_ **.** 

Register _A_ impacts the feedback of register _B_ by the XOR with _At_ + _r_ . There is no need to use a more complicated operation since _At_ + _r_ is a nonlinear function of _A_ and _B_ . The use of the lastly computed word of _A_ for influencing _B_ is very natural since it corresponds to the word in _A_ which has the highest polynomial degree in the message bits. 

**Introducing** _B_ **.** 

The insertion of _Bt_ with the help of a XOR is required to ensure that _P_ is a permutation. The rotation _Bt_ ≪ 1 aims at avoiding that the differences appearing in _B_ after one loop of _P_ , _i.e.,_ 

after 16 elementary steps, correspond to the initial differences for differential trails which do not generate any difference in _A_ . Otherwise, the number of conditions required for having a collision on register _A_ after all of the three loops of _P_ would decrease (a detailed analysis on this is provided in Section 11.3.3). 

**The Addition of Constant** `0xFFFFFFFF` **.** 

Adding the constant `0xFFFFFFFF` is intended to avoid that the all-zero internal state is a trivial fixed point. See also Section 4.6. 

**4.2.5 Function** _G_ 

For implementation reasons, we wished _G_ to use a small number of taps of register _B_ . Three is actually the lowest number of taps as shown below. The offsets ( _o_ 1 _, o_ 2 _, o_ 3) were chosen by an empirical search over all possible triplets, with the goal to maximize resistance against certain differential paths of small Hamming weight. See Section 4.3. 

One of the main conditions in the choice of _G_ is that it must involve simple operations available on a 32-bit processor. For this reason, we chose a bitwise function _G_ , _i.e.,_ a function such that the _i_ -th output bit depends on the _i_ -th input bits only, and such that all 32 coordinate functions correspond to the same Boolean function _g_ . 

Then, this 3-variable Boolean must satisfy the following conditions: 

_• g_ must be balanced, otherwise _Bt_ and _Bt_ +16 are correlated; 

_• g_ must be nonlinear; 

These conditions imply that _g_ has degree 2 since the degree of an _n_ -variable balanced function is at most ( _n −_ 1). It is worth noticing that 3 is the lowest number of variables we could choose for satisfying the previous conditions. 

All such functions _g_ are equivalent, up to an affine permutation of the input and up to the addition of an affine function. For all of them, there exist exactly 4 biased approximation by a 

function of degree 1 and each of them holds with probability 3 _/_ 4. Here are some examples. _• g_ ( _x_ 1 _, x_ 2 _, x_ 3) = _x_ 1 + _x_ 2 _x_ 3. The biased affine approximations of _g_ are _x_ 1, _x_ 1 + _x_ 2, _x_ 1 + _x_ 3 and _x_ 1 + _x_ 2 + _x_ 3 + 1. _• g_ ( _x_ 1 _, x_ 2 _, x_ 3) = _x_ 1 + _x_ 2 + _x_ 2 _x_ 3. The biased affine approximations of _g_ are _x_ 1, _x_ 1 + _x_ 2, _x_ 1 + _x_ 3 + 1 and _x_ 1 + _x_ 2 + _x_ 3. _• g_ ( _x_ 1 _, x_ 2 _, x_ 3) = _x_ 1 _x_ 2 + _x_ 1 _x_ 3 + _x_ 2. The biased affine approximations of _g_ are _x_ 2, _x_ 1 + _x_ 2, _x_ 3 and _x_ 1 + _x_ 3 + 1. 

_• g_ ( _x_ 1 _, x_ 2 _, x_ 3) = _x_ 1 + _x_ 3 + _x_ 1 _x_ 2 + _x_ 1 _x_ 3 + _x_ 2 _x_ 3, _i.e.,_ The biased affine approximations of _g_ are _x_ 1, _x_ 2 + 1, _x_ 3 and _x_ 1 + _x_ 2 + _x_ 3. 

41 

It appears that the fact that a given input variable, _e.g., x_ 1, is involved in all approximations of degree 1 makes the search for differential trails much harder. An unsuitable value of _Bt_ has to be handled by the attacker, since she cannot use an approximation of _G_ which does not involve _x_ 1. Any balanced 3-variable Boolean function whose all biased affine approximations involve _x_ 1 is linear in _x_ 1: 

_g_ ( _x_ 1 _, x_ 2 _, x_ 3) = _x_ 1 + _q_ ( _x_ 2 _, x_ 3) _._ 

We have chosen for the quadratic function _q_ a function which is not symmetric, since it seems unsuitable than, when _o_ 2 _> o_ 3, _Bt_ + _o_ 2 = 0 implies that _q_ ( _Bt_ + _o_ 2 _, Bt_ + _o_ 3) = 0 and _q_ ( _Bt_ +2 _o_ 2 _−o_ 3 _, Bt_ + _o_ 2) = 0. 

#### **4.2.6 The Final Transformation** 

The transformation 

( _A, B, C_ ) _�→_ ( _A_ + _σ_ ( _C_ ) _, B, C_ ) 

applied to the internal state after the 16 _p_ steps of _π_ aims at strengthening the inverse permutation _P_<sup>_−_1</sup> . Otherwise, _P_<sup>_−_1</sup> would consist of 16 _p_ steps of _πM,C_<sup>_−_1,butpart</sup><sup>_B_oftheoutputof</sup><sup>_π_</sup> _M,C_<sup>_−_1is</sup> independent from both parameters _M_ and _C_ . Most notably, it follows that, for an _r_ -step _P_ , part _B_ of the input of _P_ is completely determined by the knowledge of outputs _A_ and _B_ . This unsuitable property may be exploited in a (second)-preimage attack for _p_ = 1 and _p_ = 2, see Section 11.6 for details. 

In order to eliminate this weakness, the final transformation makes part _A_ of the output dependent on _C_ . When computing backwards in a (second)-preimage attack, the _C_ -input of _P_<sup>_−_1</sup> at Round _i_ actually depends on _Mi_ since the message block has been subtracted before applying _P_<sup>_−_1</sup> . Then, the final transformation makes the _A_ input of the first _r_ elementary step functions _πM_<sup>_−_1</sup> _i,C_<sup>dependonboth</sup><sup>_Mi_and</sup><sup>_C_.</sup> 

To find the vector _σ_ ( _C_ ) involved in this transformation we have searched for those which lead to the highest dependence between the words of the _B_ -part of the output of _P_<sup>_−_1</sup> and the words of _M_ for _p_ = 1, _p_ = 2 and _p_ = 3. We have restricted our search to the _σ_ ( _C_ ) which can be computed by a simple loop of the form: for _i_ from 0 to _s −_ 1, 

We have then performed an exhaustive search for the size of the loop _s_ , the direction _e_ and the offset for the recommended choice of _r_ , _i.e., r_ = 12. Another condition was that each word of _A_ in the output of _P_ must depend on a different set of the words of _C_ . The vector _σ_ ( _C_ ) that we have chosen can be computed by a loop of size 36, with _e_ = 0 and offset = 3, _i.e.,_ for _i_ from 0 to 11, 

_σ_ ( _C_ )[ _i_ ] = _C_ [ _i_ + 3] + _C_ [ _i_ + 3 + _r_ ] + _C_ [ _i_ + 3 + 2 _r_ ] _._ 

It is worth noticing that each _A_ [ _i_ ] then depends on three words of _C_ that are all different for the different _i_ . If a different value for _r_ is to be used, _s, e_ and the offset must be recomputed. 

### **4.3 How We Chose** ( _o_ 1 _, o_ 2 _, o_ 3) 

#### **4.3.1 The Basic Idea** 

As explained in the previous section, the update of register _A_ in permutation _P_ involves some words of _B_ selected by an offset triplet ( _o_ 1 _, o_ 2 _, o_ 3). We now provide details on the method we used to elect such a triplet of offsets. 

To determine the best offset triplet ( _o_ 1 _, o_ 2 _, o_ 3), we have looked for triplets which ensure the best diffusion of differences inside the internal state of Shabal. To this purpose, we define a specific criterion. For the sake of readability, we consider in this section the function _R_ described in Section 2.2 but without specifying the counter _w_ . More precisely, _R_ is the message round function which takes as input the (32 + _r_ )-word internal state and the current message block and outputs 

42 

the internal state after the first round is completed (hence we have _R_ ( _M, Sold_ ) = _Snew_ , where _S_ is the internal state). 

Our main criterion was the following: given a vector _δ_ with small weight, the minimum of the weight of 

over all the possible values of _M_ should be maximal. Indeed, the idea behind this criterion is that we want to maximize the number of differences caused by a few input differences (in one round), in order to obtain as fast as possible an uncontrollably large set of differences. 

We have scalable security parameters, namely _r_ and _p_ . To study the diffusion of the round function, we need to specify these parameters. Since one of our goals is to design the function which ensures the best diffusion, we are thus searching for the triplets ( _o_ 1 _, o_ 2 _, o_ 3) which ensure the best diffusion even if _p_ and _r_ are the worst parameters for the diffusion. Proceeding this way, the chosen offsets should be a good choice whatever the choice of parameters. 

It is clear that _p_ = 1 is a bad choice for diffusion and even for security. The role of _r_ in the function is quite different: the bigger _r_ , the larger the capacity and the worst the diffusion. We thus decided to choose _r_ = 16 to proceed to the search. 

In a phase of analysis, to satisfy this criterion, we have first linearized the _R_ function. _R_ thus becomes an function: we have 

where _ψ_ is a linear function and _α_ a constant vector. Thus, we want to maximize the weight of 

This analysis gives arguments on the choice of the triplets for the linearized _R_ function but not for the real function. This first phase enables us to determine a family of good choices of triplets. Once this set is defined, we analyze these triplets over the real round function. 

#### **4.3.2 Linearization** 

There exist different nonlinear computations inside the round function. Firstly, the message insertion is made thanks to an integer addition. In the linearized form, this operation is switched into a bitwise XOR. Secondly, the functions _U_ and _V_ which are used to compute _A_ are also nonlinear. We have _U_ : _x �→_ 3 _× x_ mod 2<sup>32</sup> and _V_ : _x �→_ 5 _× x_ mod 2<sup>32</sup> ; we linearized them by replacing 3 _× x_ with _x ⊕_ ( _x ≪_ 1) and 5 _× x_ with _x ⊕_ ( _x ≪_ 2) (see also Section 6.4). These are clearly the best linear approximations of _U_ and _V_ . Finally, we need to linearize the computation of _B_ [ _i_ + _o_ 1 mod 16] _⊕ B_ [ _i_ + _o_ 2 mod 16] _∧ B_ [ _i_ + _o_ 3 mod 16]. As explained in Section 4.2.5, this computation can be linearized in four different ways (in the following, we denote by _R_ 1, _R_ 2 _R_ 3 and _R_ 4 the linearized round functions associated respectively to the first, the second, the third and the fourth linearized computations): 

1. _B_ [ _i_ + _o_ 1 mod 16] 

2. _B_ [ _i_ + _o_ 1 mod 16] _⊕ B_ [ _i_ + _o_ 2 mod 16] 

3. _B_ [ _i_ + _o_ 1 mod 16] _⊕ B_ [ _i_ + _o_ 3 mod 16] 

4. _B_ [ _i_ + _o_ 1 mod 16] _⊕ B_ [ _i_ + _o_ 2 mod 16] _⊕ B_ [ _i_ + _o_ 3 mod 16] 

These four different choices for the linearized round function enable us to determine conditions over the possible triplets. The first one gives arguments for the choices of _o_ 1, and respectively the second one for _o_ 2 and the third one for _o_ 3. The second and the third linearized round functions are exactly the same and the best _o_ 2 is thus the best _o_ 3 as well. This is logical since _B_ [ _i_ + _o_ 2 mod 16] and _B_ [ _i_ + _o_ 3 mod 16] play symmetric roles. We thus use the second and the fourth linearized round functions to choose _o_ 2 and _o_ 3. 

43 

#### **4.3.3 Search Methods** 

We have studied the Hamming weight of the output of _ψi_ ( _δ_ ) = _Ri_ ( _M ⊕δ, S_ ) _⊕Ri_ ( _M, S_ ) _,_ 1 _≤ i ≤_ 4 for _δ_ of low Hamming weight, using two methods. Using brute force search, it is possible to compute _ψi_ ( _δ_ ) for all _δ_ of weight three. It is possible to go a bit further using some algorithm dedicated to the search for low-weight vectors in a code, as we explain hereafter. It is worth noticing that the main classical algorithms for finding low Hamming weight words in a linear code are dedicated to binary codes while this is not the case here. Then, we used the following techniques: the values of _ψi_ ( _δ_ ) for all _δ_ of weight _w_ are computed and stored in a list. This list can then be sorted following a lexicographic order. Thanks to this sort, two consecutive elements in the list, namely _ψi_ ( _δ_ 1) and _ψi_ ( _δ_ 2) are close to each other for the Hamming distance with a higher probability than two random elements in the list. As _ψi_ is a linear function, we have 

Thus we have tested this way the weights of _ψi_ for _some_ elements of weight 2 _w_ . Hence this algorithm is probabilistic. To improve the quality of the result, it is possible to sort the list again using a different lexicographic order and to compute the XOR of consecutive elements lying in the resulting list again. With the recommended settings of Shabal, this algorithm can test many vectors of weight 4. 

#### **4.3.4 Results on the Linearized Function** 

Using the two search methods, we have first studied the function _R_ 1. We found that this function has a minimal output weight of 16 for _o_ 1 = 12 _,_ 13. The values 9 _,_ 10 and 14 give a weight bigger than 13. Other choices of _o_ 1 leads to a minimum weight less than 10. 

We have also studied the functions _R_ 2, _R_ 3 and _R_ 4 to determine a good family of offsets. In fact the study of _R_ 2 and _R_ 3 leads to the same results as mentioned above. We decided to study triplets of offsets such that the minimum weight obtained with _R_ 2 was bigger than 50 given _o_ 1 amongst 9 _,_ 10 _,_ 12 _,_ 13 _,_ 14. This value ensures that it remains sufficiently many offsets to test. As a result, we have pairs of offsets which could play the role of ( _o_ 1 _, o_ 2) or ( _o_ 1 _, o_ 3). The results lead to (12 _,_ 2), (12 _,_ 5), (12 _,_ 7), (12 _,_ 9), (13 _,_ 3), (13 _,_ 6), (13 _,_ 7), (14 _,_ 4), (14 _,_ 9). Amongst these pairs, we look at the ones that give the best results for _R_ 3. We select those with a final weight higher than 100. This leads to the triplets: (14 _,_ 9 _,_ 3), (14 _,_ 11 _,_ 4), (13 _,_ 8 _,_ 6), (13 _,_ 9 _,_ 6), (13 _,_ 12 _,_ 6),(13 _,_ 8 _,_ 7), (14 _,_ 9 _,_ 8). 

We remove on purpose the triplet (13 _,_ 12 _,_ 6) because two consecutive offsets always lead to a bad result with _R_ 2 and the triplets (14 _,_ 9 _,_ 8), (13 _,_ 8 _,_ 7), (13 _,_ 8 _,_ 6) because 8 is the worst possible offset for _R_ 1. Furthermore, 8 is special since it is the half of the number of words in the state _B_ . 

The remaining possible triplets are thus (14 _,_ 9 _,_ 3), (14 _,_ 11 _,_ 4) and (13 _,_ 9 _,_ 6). 

#### **4.3.5 Final Results on the Real Function for** _p_ = 1 **and** _r_ = 12 

After this analysis, we have studied these chosen triplets on the real ( _i.e.,_ non-linearized) function. Given a low-weight difference between two messages, the two associated internal states after one round should have a difference with a sufficiently high weight to ensure a good difference diffusion in the internal state. To check whether this property is true for a given triplet, we have computed the minimal weight of _R_ ( _M_ ) _⊕R_ ( _M ⊕ δ_ ) for all _δ_ of weight at most three. As this computation is not possible for every message _M_ , we computed the minimum weight over the _δ_ for different random messages. To accelerate the computation, instead of choosing random messages of random length, we chose random messages of constant length of 16 words and we randomly chose the IV of the internal state. This random choice of IV simulates the insertion of a random prefix message before the insertion of differences. We have made this analysis for _r_ = 12, which is the recommended _r_ . Nevertheless, we study the round function with _p_ sets to 1 and 2. With _p_ = 3, the output of the permutation seems to be random and whatever the small input difference is, the difference of the outputs looks like a random string. This property does not help to fix the best triplet of offsets. 

44 

We have repeated these computations about 2<sup>45</sup> times on all the selected triplets. We have finally chosen the triplet (13 _,_ 9 _,_ 6) which is from our computations the best one. 

### **4.4 Shabal and Degree** 

_P_ is a keyed permutation which takes as input an internal state _S_ = ( _A, B, C_ ) and a message block _M_ and which outputs _A_<sup>_′_</sup> and _B_<sup>_′_</sup> . Each bit of the output can be expressed as a Boolean function of the bits of the inputs. Nevertheless, it is impossible to write formally these functions since the number of input bits equals 1920. 

It has been shown that some properties of the algebraic normal form (ANF) of a Boolean function can be exploited to distinguish it from a random Boolean function (see Section 11.9 for instance). These attacks mainly rely on two properties: 

- the sparsity of the ANF of the Boolean function; 

- the degree of the Boolean function. 

It can be easily seen that the ANF of any output of _P_ has no reason to be sparse, because of the use of _U, V_ , of the different rotations and of the function _φ_ : ( _x, y_ ) _�→_ _<u>x ∧</u> y_ . The second criterion needs to be further investigated. Indeed, _U_ and _V_ have special algebraic expressions since they coincide many times with their linear approximations. Furthermore, the choice for function _φ_ of a bitwise operation may not ensure the growth of the degrees of the Boolean functions. 

However, estimating the degree requires to simplify some operations. We have thus investigated the degrees of the message round functions of two different weakened versions of Shabal: 

1. the weakened 1-bit version, named Weakinson-1bit (see Section 6.1), 

2. the weakened 32-bit version where _U_ and _V_ are linear functions, where all additions and subtractions are replaced by XORs and where the final update loop on _A_ is removed. This variant corresponds to Weakinson- _⊕_ -LinearUV-NoFinalUpdateA (see Section 6.3). 

Moreover, for both variants, we do not take into account the design of Shabal, in the sense that _B_ is assumed to be independent from _M_ (while _M_ is added to _B_ in the construction). 

The degrees of the outputs of the round function in both variants are obviously lower than the degrees obtained for the full Shabal, in particular because in both weakened versions, _U_ , _V_ and all additions are linear, implying that the only source of nonlinearity is the quadratic function _φ_ : ( _x, y_ ) _�→ x ∧_ _<u>y</u>_ <u>.</u> 

#### **4.4.1 Degree of Weakinson-1bit** 

The weakened version of Shabal with 1-bit words is of great interest since the Boolean function output by _P_ can be formally expressed with computer algebra software such as PARI/GP (see `http://pari.math.u-bordeaux.fr/` ). 

We have decided to study the degrees of the Boolean functions in the different parameters independently from each other. This leads to Table 4.1 which gives the degrees in the different input variables of the outputs of _P_ , for different values of parameter _p_ . Since the output degrees in _A_ , _C_ and _M_ are the same, they are all given in the same row in Table 4.1. 

|**Inputs**|_p_ = 1**,** deg(_A_<sup>_~~′~~_</sup>)|_p_ = 1**,** deg(_B_<sup>_~~′~~_</sup>)|_p_ = 2**,** deg(_A_<sup>_~~′~~_</sup>)|_p_ = 2**,** deg(_B_<sup>_~~′~~_</sup>)|_p_ = 3**,** deg(_A_<sup>_~~′~~_</sup>)|_p_ = 3**,** deg(_B_<sup>_~~′~~_</sup>)|
|---|---|---|---|---|---|---|
|_M, A, C_|From 1 to 2|From 1 to 2|From 4 to 8|From 2 to 8|From 8 to 14|From 10 to 14|
|_B_|From 2 to 5|From 2 to 5|From 7 to 12|From 5 to 12|From 14 to 16|From 12 to 16|

Table 4.1: Degrees of the outputs of the message round function in Weakinson-1bit 

45 

#### **4.4.2 Degree of Weakinson-** _⊕_ **-LinearUV-NoFinalUpdateA** 

For this weakened variant, we compute the degree by modeling the actions of all the different operations on the degree. For instance, to compute the degree of the Boolean function which takes _M_ as input and outputs _PM,_ 0(0 _,_ 0) = ( _A_<sup>_′_</sup> _, B_<sup>_′_</sup> ), we replace _M_ by the 512-bit all-1 vector and _A_ , _B_ and _C_ by the all-0 vector. This models the fact that each bit of _M_ has a degree equal to 1 while each bit of _A_ , _B_ and _C_ has a degree equal to 0. 

In our model, each operation which appears in the computation of _P_ updates the vector ( _A, B_ ). The model firstly assumes that deg( _φ_ ( _B_ [ _i_ ] _, B_ [ _j_ ])) = deg( _B_ [ _i_ ])+deg( _B_ [ _j_ ]). Secondly, it is assumed that deg( _A_ [ _i_ ] _⊕ A_ [ _j_ ]) = max( _A_ [ _i_ ] _, A_ [ _j_ ]). These are optimistic assumptions on the degree, since we do not take into account the reduction by the polynomials _x_<sup>2</sup> _i_<sup>+</sup><sup>_xi_whichare0over</sup><sup>**F**2forany</sup> input variable _xi_ . The assumption that _φ_ ensures the growth of the degree is strongly related to the fact that we use word rotations. Since _φ_ is a bitwise operation, if no rotation is used, the Boolean function would only depend on the input bits at the same position in the word, leading to a very weak function. With these rotations, the two polynomials corresponding to the inputs of _φ_ should have different monomials. For this reason, it seems realistic to assume that _φ_ ensures the growth of the degree. 

These different hypotheses lead to Table 4.2. It can be seen that, even for _p_ = 3, the obtained degree is not maximal ( _i.e.,_ less than 512). But, the actions of _U_ , _V_ and of the different additions modulo 2<sup>32</sup> are expected to ensure a much higher degree. Moreover, it has been chosen for the final rounds to use 3 consecutive iterations of permutation _P_ . We thus think that the resulting transformation is sufficient to resist all attacks that attempt to distinguish _P_ from a random keyed permutation. 

|**Inputs**|_p_ = 1**,** deg(_A_<sup>_~~′~~_</sup>)|_p_ = 1**,** deg(_B_<sup>_~~′~~_</sup>)|_p_ = 2**,** deg(_A_<sup>_~~′~~_</sup>)|_p_ = 2**,** deg(_B_<sup>_~~′~~_</sup>)|_p_ = 3**,** deg(_A_<sup>_~~′~~_</sup>)|_p_ = 3**,** deg(_B_<sup>_~~′~~_</sup>)|
|---|---|---|---|---|---|---|
|_M, A, C_|From 1 to 2|From 1 to 2|From 4 to 9|From 2 to 9|From 12 to 32|From 9 to 32|
|_B_|From 2 to 5|From 2 to 5|From 8 to 21|From 5 to 21|From 28 to 70|From 21 to 70|

Table 4.2: Degrees of the outputs of the message round function in Weakinson- _⊕_ -LinearUVNoFinalUpdateA 

It is worth noticing that both previous approaches aim at giving arguments on the choice of parameter _p_ and of the number of final rounds. Actually, computing the degrees of the underlying Boolean functions in Shabal is not feasible. 

### **4.5 Initial Values** 

For some initial values before the first message introduction, the scheme may be weaker than for some random-looking initial value. Indeed, some components of _A_ update, _e.g., B_ [ _i_ + _o_ 2 + mod32] _∧ B_ [ _i_ + _o_ 3 mod 32], preserve symmetry (in the sense that they transform the all-0 and the all-1 words into all-0 or all-1 words); furthermore, _U_ and _V_ functions have 0 as a fixed point. Therefore, we have tried to start the message rounds with an almost random initial state, called IV _ℓh_ . 

To set this IV _ℓh_ , we may have stated that one would choose some “natural” values, such as the expression of _π_ in hexadecimal. However, while this kind of setting is widely accepted to be trapdoor-free, it imposes to store in implementations the full values of IV _ℓh_ , which for our Shabal implementation is (1024+32 _r_ )-bit long per IV (that is ( _A, B, C_ )). Constrained environments such as low-cost smart cards, RFID or hardware would clearly suffer from this choice. 

Instead, we have decided to exhibit some IV _ℓh_ that come naturally from our definition of Shabal. More precisely, we have decided that the IV _ℓh_ would be obtained after performing some preliminary steps, with initial full-0 state value and message blocks ( _M−_ 1 _, M_ 0) = _{ℓh, ℓh_ +1 _, ..., ℓh_ +31 _}_ , where _ℓh_ is the wanted output length and where the prefix is composed of 32 words of 32 bits. The length of the prefix (that is 32 words) has been chosen so that it is sufficient to make the buffers almost random-looking. Thanks to this prefix, the state is set to a non-pathological value. As one can 

46 

see, there are as many IV _ℓh_ as the number of possible output lengths, in order to let (if possible) the hash values and security of the different-length Shabal independent. 

This kind of IV setting has two principal advantages. First, one may reasonably argue that this is trapdoor-free. Indeed, the IV _ℓh_ choice can be verified easily to be honestly generated. Second, this setting is very efficient regarding implementation: on low-power devices, one can simply prefix the message with ( _M−_ 1 _, M_ 0) and start Shabal with all-0 internal state; on the contrary, on nonrestricted machines or for faster implementations, one should tabulate the value IV _ℓh_ and directly start with message blocks. 

Clearly, if the number of IV _ℓh_ is too large in practice (even if reconstructible, certain implementations will prefer to tabulate the values), we may consider to limit them to fewer values. 

### **4.6 The of Counter** _w_ 

We have proposed to use a simple counter _w_ in our generic construction and in Shabal. In fact, the counter is not critical for the indifferentiability proof of Section 5.3. However, _w_ provides a simple way to avoid _fixed points_ (see also the addition of the all-one constant when updating _A_ [ _i_ + 16 _j_ mod _r_ ] in Section 4.2.4 and Section 11.4). 

Furthermore, counter _w_ makes second preimage attacks harder as shown in the proof of Theorem 5. This is due to the fact that an attacker which attempts to connect somewhere on the challenge path also has to collide on the counter. We refer the reader to Chapter 5 for more details. 

### **4.7 Output of the Hash Function** 

The output of the Shabal hash function is directly given by the construction depicted in Section 2.2, which is proven to be indifferentiable from a random oracle in Section 5.3. We have chosen to output the _ℓh/_ 32 last words of _B_ directly after the last keyed permutation is carried out, which are the words with highest degree. 

### **4.8 Nonlinearity** 

Let us summarize the sources of nonlinearity within Shabal: 

( _i_ ) the effect of carries due to the insertion of message blocks in both _B_ and C; 

( _ii_ ) functions _U_ ( _x_ ) = 3 _× x_ mod 2<sup>32</sup> and _V_ ( _x_ ) = 5 _× x_ mod 2<sup>32</sup> ; 

- ( _iii_ ) the quadratic function ( _x, y_ ) _�→ x ∧_ _<u>y</u>_ used when updating the words of of _A_ ; 

- ( _iv_ ) the final update loop on the buffer _A_ . 

These four ingredients excepted, Shabal is linear. As one can see in Chapter 6, we propose weakened versions of Shabal in order to simplify the cryptanalysis of the real function. In these simplified versions, nonlinear effects are typically eliminated to allow a simpler analysis: one at least among ( _i_ ) _,_ ( _ii_ ) _,_ ( _iii_ ) _,_ ( _iv_ ) is left nonlinear otherwise the cryptanalysis is trivial and uninteresting. 

47 

## **Chapter 5** 

# **Security Proofs for the Shabal Construction** 

#### **Contents** 

|**5.1**|**Intr**|**oduction**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .**|**48**|
|---|---|---|---|
||5.1.1|Provable Security for Hash Constructions . . . . . . . . . . . . . . . .|.<br>48|
||5.1.2|Summary of Our Security Results<br>. . . . . . . . . . . . . . . . . . . .|.<br>49|
||5.1.3|Roadmap . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>50|
|**5.2**|**Refo**|**rmulating the Mode of Operation of Shabal . . . . . . . . . . . .**|**50**|
|**5.3**|**Sha**|**bal is Indiferentiable from a Random Oracle**<br>**. . . . . . . . . . .**|**51**|
||5.3.1|Preliminaries to the Proofs<br>. . . . . . . . . . . . . . . . . . . . . . . .|.<br>52|
||5.3.2|Proofs of Theorems 1 and 2 . . . . . . . . . . . . . . . . . . . . . . . .|.<br>54|
|**5.4**|**Sha**|**bal is Collision Resistant in the Ideal Cipher Model . . . . . . .**|**65**|
||5.4.1|A Security Model for Collision Resistance in the ICM<br>. . . . . . . . .|.<br>65|
||5.4.2|Proving Collision Resistance for Shabal’s Mode of Operation<br>. . . . .|.<br>66|
||5.4.3|Proof of Theorem 3<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>66|
|**5.5**|**Sha**|**bal is Preimage Resistant in the Ideal Cipher Model . . . . . . .**|**74**|
||5.5.1|A Security Model for Preimage Resistance in the ICM . . . . . . . . .|.<br>74|
||5.5.2|Proving Preimage Resistance for Shabal’s Mode of Operation . . . . .|.<br>74|
||5.5.3|Proof of Theorem 4<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>75|
|**5.6**|**Sha**|**bal is Second Preimage Resistant in the Ideal Cipher Model . .**|**85**|
||5.6.1|Capturing Second Preimage Resistance in the ICM . . . . . . . . . . .|.<br>85|
||5.6.2|Proving Second Preimage Resistance for Shabal’s Mode of Operation .|.<br>85|
||5.6.3|Proof of Theorem 5<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|.<br>86|

##### and relies on a fixed-length primitive 

_P_ : _{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _× {_ 0 _,_ 1 _}_<sup>_ℓa_</sup> _× {_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _× {_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _→{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> _× {_ 0 _,_ 1 _}_<sup>_ℓm_</sup> 

which we consider to be either a compression function or a keyed permutation over _{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> _× {_ 0 _,_ 1 _}_<sup>_ℓm_</sup> with key space _{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _× {_ 0 _,_ 1 _}_<sup>_ℓm_</sup> . 

**Input message.** Let _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> be the input of _C_<sup>_P_</sup> . 

**Message padding.** _M_ is first padded with 1 _∥_ 0<sup>_ℓ_</sup> for smallest _ℓ ≥_ 0 such that _M ∥_ 1 _∥_ 0<sup>_ℓ_</sup> can be split into a list of _ℓm_ -bit input blocks 

**Initialization.** _C_<sup>_P_</sup> sets ( _m, a, b, c_ ) = (0 _, a_ 0 _, b_ 0 _, c_ 0). 

50 

**Message rounds.** For _i_ = 1 to _k_ , _C_<sup>_P_</sup> executes the two subroutines 

( _m, a, b, c_ ) = Insert[ _mi, i_ ]( _m, a, b, c_ ) _,_ ( _a, b_ ) = _P_ ( _m, a, b, c_ ) 

where for m _∈{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> and _w ∈{_ 0 _,_ 1 _}_<sup>64</sup> 

Insert[m _, w_ ]( _m, a, b, c_ ) = (m _, a ⊕_ ( _w_ ) _, c_ ⊟ _m_ ⊞ m _, b_ ) _,_ 

and ( _w_ ) stands for the 64-bit integer _w_ which most significant bits are completed with 0-bits to yield an _ℓa_ -bit integer. 

**Final rounds.** Given the current internal state ( _m, a, b, c_ ), _C_<sup>_P_</sup> now computes for _e_ = 1 to E: 

( _m, a, b, c_ ) = Insert[ _mk, k_ ]( _m, a, b, c_ ) _,_ ( _a, b_ ) = _P_ ( _m, a, b, c_ ) _._ 

**Output.** The output of _C_<sup>_P_</sup> ( _M_ ) is defined to be the string _b_ mod 2<sup>_ℓh_</sup> . 

The operating mode _C_ of Shabal is depicted on Fig. 5.2. 

<!-- Start of picture text -->
Mk− 1 Mk Mk Mk Mk<br>h<br>( m )<br>( a )<br>P P P P P<br>( b )<br>( c )<br>Final rounds →<br><!-- End of picture text -->

Figure 5.2: A reformulation of the mode of operation of Shabal with a focus on the final rounds. Note that the counter _w_ is omitted on this picture. 

### **5.3 Shabal is from a Random Oracle** 

For the sake of completeness, we consider the cases of _P_ being instantiated either as a random function or as a random keyed permutation. The first case allows us to introduce definitions and proof techniques. We then extend our results to the second case which directly relates to Shabal. 

**Theorem 1** (Random function) **.** _Assume P is a random function and let H be a random oracle. There exists a simulator S such that for any distinguisher D totalling at most N right calls,_ Adv( _D, C_ ) _≤ N_ (2 _N −_ 1) _·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup> _._ 

_S makes at most N calls to the random oracle H and runs in time at most O_ ( _N_<sup>2</sup> ) _._ 

**Theorem 2** (Random keyed permutation) **.** _Assume P is a random keyed permutation and let H be a random oracle. There exists a simulator S such that for any distinguisher D totalling at most N right calls,_ Adv( _D, C_ ) _≤ N_ (4 _N −_ 3) _·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup> _._ 

_S makes at most N calls to the random oracle H and runs in time at most O_ ( _N_<sup>2</sup> ) _._ 

This shows that _C_ has capacity ( _ℓa_ + _ℓm_ ) _/_ 2 in the sense of [7]. The remainder of this section is dedicated to a proof of Theorems 1 and 2. 

51 

### **5.4 Shabal is Collision Resistant in the Ideal Cipher Model** 

#### **5.4.1 A Security Model for Collision Resistance in the ICM** 

We model collision resistance of construction _C_<sup>_P_</sup> under the form of a security game played between a collision finder or adversary _A_ and a challenger _V_ . 

**Definition 7** (COLL Game) **.** _The game is described as follows:_ 

_1. A makes calls to the ideal cipher_ ( _P, P_<sup>_−_1</sup> ) 

_2. A outputs two messages M_ 1 _, M_ 2 _∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> 

_3. V computes C_<sup>_P_</sup> ( _M_ 1) _and C_<sup>_P_</sup> ( _M_ 2) _by calling P_ 

_4. V outputs_ 1 _if C_<sup>_P_</sup> ( _M_ 1) = _C_<sup>_P_</sup> ( _M_ 2) _or_ 0 _otherwise._ 

65 

`Simulation of` _P_<sup>_−_1</sup> `Input:` _x_ = ( _m, a, b, c_ ) _∈X_ `, origin` _O_ = `either` _C_ `or` _D_ `Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _x_ `to` _XO F_ `2. if there exists` _y → x ∈ ZC ∪ ZD F_ `(a) add` _y_ `to` _YO_ `and edge` _y → x_ `to` _ZO_ `(b) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `where` _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `3. randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `4. add node` _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _XO_ `and edge` _y → x_ `to` _ZO_ ˜ _F_ ˜ `5. if` _∃x ∈ XC ∪ XD_ `such that` _y → x ∈ ZC ∪ ZD_ `(event` Abort4 `) then abort 6. if` _∃x_ ˜ _∈ XC ∪ XD_ `such that` Dep(˜ _x, y_ ) `(event` Abort5 `) then abort 7. return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ 

Figure 5.12: Indifferentiability: Simulation of _P_<sup>_−_1</sup> in Games 3–9. 

We define the success probability Suc<sup>COLL</sup> ( _A, C_ ) of _A_ as the probability that _V_ outputs 1 when interacting with _A_ as per the COLL game. Suc<sup>COLL</sup> ( _A, C_ ) is a function of the total number _N_ of queries received by the ideal cipher ( _P, P_<sup>_−_1</sup> ) throughout the game. Note that _V_ itself has to make ( _k_ 1 + E) + ( _k_ 2 + E) calls to _P_ when verifying the response ( _M_ 1 _, M_ 2) of _A_ if hashing _M_ 1 and _M_ 2 leads to the insertion of respectively _k_ 1 and _k_ 2 message blocks. Thus overall _A_ makes _N −_ ( _k_ 1 + E) _−_ ( _k_ 2 + E) calls to ( _P, P_<sup>_−_1</sup> ). 

#### **5.4.2 Proving Collision Resistance for Shabal’s Mode of Operation** 

We conceive a simulator _S_ that simulates _V_ and ( _P, P_<sup>_−_1</sup> ) towards _A_ . An high-level view of _S_ is as follows. Simulator _S_ 

1. simulates the ideal cipher ( _P, P_<sup>_−_1</sup> ) and may abort while doing so 

2. receives _M_ 1 _, M_ 2 _∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> from _A_ 

3. runs its own simulation of _P_ to compute _C_<sup>_P_</sup> ( _M_ 1) and _C_<sup>_P_</sup> ( _M_ 2) 

4. outputs 0 

The underlying proof technique consists in making the simulation of _P_ abort when _C_<sup>_P_</sup> ( _M_ 1) = _C_<sup>_P_</sup> ( _M_ 2). Therefore either _S_ outputs 0 or the game aborts. Consequently 

Suc<sup>COLL</sup> ( _A, C_ ) _≤_ Pr [ _S_ aborts] _._ 

We state 

**Theorem 3** (Collision resistance) **.** _There exists a simulator S as above such that for any collision finder A playing as per the_ COLL _game limited to at most N calls to_ ( _P, P_<sup>_−_1</sup> ) _,_ Pr [ _S aborts_ ] _≤_ 3 _· N_ ( _N −_ 1) _·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup> + _N_ ( _N −_ 1) _·_ 2<sup>_−ℓh_</sup> _and S runs in time at most O_ ( _N_<sup>2</sup> ) _._ 

### **5.5 Shabal is Preimage Resistant in the Ideal Cipher Model** 

#### **5.5.1 A Security Model for Preimage Resistance in the ICM** 

We capture the preimage resistance of construction _C_<sup>_P_</sup> as a security game played between an adversary _A_ and a challenger _V_ . 

**Definition 9** (PRE Game) **.** _The game is described as follows:_ 

_1. V randomly selects h ←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _and sends h to A_ 

_2. A makes calls to the ideal cipher_ ( _P, P_<sup>_−_1</sup> ) 

_3. A outputs a message M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> 

_4. V computes C_<sup>_P_</sup> ( _M_ ) _by calling P_ 

_5. V outputs_ 1 _if C_<sup>_P_</sup> ( _M_ ) = _h or_ 0 _otherwise_ 

We define the success probability Suc<sup>PRE</sup> ( _A, C_ ) of _A_ as the probability that _V_ outputs 1 when interacting with _A_ as per the above game. Suc<sup>PRE</sup> ( _A, C_ ) is a function of the total number _N_ of queries received by the ideal cipher ( _P, P_<sup>_−_1</sup> ) throughout the game. Note that _V_ itself has to make _k_ + E calls to _P_ when verifying the response _M_ of _A_ if hashing _M_ leads to the insertion of _k_ message blocks. Thus _A_ makes _N −_ ( _k_ + E) calls to ( _P, P_<sup>_−_1</sup> ). 

#### **5.5.2 Proving Preimage Resistance for Shabal’s Mode of Operation** 

We conceive a simulator _S_ that simulates _V_ and ( _P, P_<sup>_−_1</sup> ) towards _A_ . An high-level view of _S_ is as follows. Simulator _S_ 

1. randomly selects _h ←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> 

2. sends _h_ to _A_ 

3. simulates the ideal cipher ( _P, P_<sup>_−_1</sup> ) and may abort while doing so 

4. receives _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> from _A_ 

5. runs its own simulation of _P_ to compute _C_<sup>_P_</sup> ( _M_ ) 

6. outputs 0 

Our proof technique is to make the simulation of _P_ abort upon detection of the event that _C_<sup>_P_</sup> ( _M_ ) = _h_ . Therefore either _S_ outputs 0 or the game aborts. Consequently 

Suc<sup>PRE</sup> ( _A, C_ ) _≤_ Pr [ _S_ aborts] _._ 

We state 

74 

**Theorem 4** (Preimage resistance) **.** _There exists a simulator S as above such that for any preimage finder A playing as per the_ PRE _game limited to at most N calls to_ ( _P, P_<sup>_−_1</sup> ) _,_ 

Pr [ _S aborts_ ] _≤ N ·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm−_log(</sup><sup>_ℓm_+1)</sup><sup>_−_2)</sup> 

_and S runs in time at most O_ ( _N_<sup>2</sup> ) _._ 

### **5.6 Shabal is Second Preimage Resistant in the Ideal Cipher Model** 

#### **5.6.1 Capturing Second Preimage Resistance in the ICM** 

Adapting the security model of previous sections, we now consider second preimage resistance in the same spirit. We define a security game played between an adversary _A_ and a challenger _V_ . The game is described as follows. 

**Definition 13** (SP Game) **.** _The security game takes as input a parameter κ ∈_ N _._ 

_1. V randomly selects a κ-bit message M_<sup>_∗_</sup> _←{_ 0 _,_ 1 _}_<sup>_κ_</sup> _and sends M_<sup>_∗_</sup> _to A_ 

_2. A makes a series of calls to the ideal cipher_ ( _P, P_<sup>_−_1</sup> ) 

_3. A outputs a message M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> 

_4. V computes C_<sup>_P_</sup> ( _M_ ) _by calling P_ 

_5. V outputs_ 1 _if C_<sup>_P_</sup> ( _M_ ) = _C_<sup>_P_</sup> ( _M_<sup>_∗_</sup> ) _or_ 0 _otherwise_ 

The success probability Suc<sup>SP</sup> ( _A, C_ ) of _A_ is the probability that _V_ outputs 1 when interacting with _A_ as per the SP game. In addition to Shabal’s parameters, Suc<sup>SP</sup> ( _A, C_ ) depends on the total number _N_ of queries received by the ideal cipher ( _P, P_<sup>_−_1</sup> ) throughout the game. Define _k_<sup>_∗_</sup> as the block length of _M_<sup>_∗_</sup> _i.e.,_ the number of _ℓm_ -bit blocks required to encode the padded input message (hence _k_<sup>_∗_</sup> = _⌈_ ( _κ_ + 1) _/ℓm⌉_ ). Assume that the block length of _M_ is _k_ ; then note that _V_ itself has to make _k_ + E calls to _P_ when verifying the response _M_ of _A_ . Thus in total _A_ makes _N −_ ( _k_ + E) calls to ( _P, P_<sup>_−_1</sup> ). 

#### **5.6.2 Proving Second Preimage Resistance for Shabal’s Mode of Operation** 

We build a simulator _S_ that simulates _V_ and ( _P, P_<sup>_−_1</sup> ) towards _A_ in the spirit of the previous section: our simulator _S_ 

1. randomly selects _M_<sup>_∗_</sup> _←{_ 0 _,_ 1 _}_<sup>_κ_</sup> 

85 

2. runs its own simulation of _P_ to compute _C_<sup>_P_</sup> ( _M_<sup>_∗_</sup> ) 

3. sends _M_<sup>_∗_</sup> to _A_ 

4. simulates the ideal cipher ( _P, P_<sup>_−_1</sup> ) towards _A_ ; the simulation may provoke the abortion of _S_ 

5. receives _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> from _A_ 

6. runs its own simulation of _P_ to compute _C_<sup>_P_</sup> ( _M_ ) 

7. outputs 0 

Our proof technique is to make the simulation of _P_ abort the game upon detection of the event that _C_<sup>_P_</sup> ( _M_ ) = _C_<sup>_P_</sup> ( _M_<sup>_∗_</sup> ). Consequently either _S_ outputs 0 or the game aborts and 

Suc<sup>SP</sup> ( _A, C_ ) _≤_ Pr [ _S_ aborts] _._ 

**Theorem 5** (Second preimage resistance) **.** _There exists a simulator S as above such that for any second preimage finder A playing as per the_ SP _game limited to at most N calls to_ ( _P, P_<sup>_−_1</sup> ) _,_ 

Pr [ _S aborts_ ] _≤_ 2 _· N ·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm−_log</sup><sup>_k∗_)</sup> _and S runs in time at most O_ ( _N_<sup>2</sup> ) _._ 

###### `Initialization of` _S_ 

`No input, no output 1. randomly select` _M_<sup>_∗_</sup> _←{_ 0 _,_ 1 _}_<sup>_κ_</sup> `2. set` _X_ = _Y_ = _Z_ = _∅_ `3. compute` _C_<sup>_P_</sup> ( _M_<sup>_∗_</sup> ) = _h_ `using the simulation of` _P_ `below` 

`Simulation of` _P_ 

`Input:` _y_ = ( _m, a, b, c_ ) _∈X_ `from` _O_ `(either` _A_ `or` _S_ `) Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _y_ `to` _Y F_ `2. if there exists` _y → x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) _∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _X_ `and edge` _y → x_ `to` _Z_ `(c) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ `Simulation of` _P_<sup>_−_1</sup> `Input:` _x_ = ( _m, a, b, c_ ) _∈X_ `from` _A_ `Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _x_ `to` _X F_ `2. if there exists` ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) = _y → x ∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _Y_ `and edge` _y → x_ `to` _Z_ `(c) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ 

`Completion of` _S_ `Input:` _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> `from` _A_ `1. compute` _C_<sup>_P_</sup> ( _M, ℓm_ ) `by calling` _P_ `accordingly 2. if` _C_<sup>_P_</sup> ( _M, ℓm_ ) = _h_ `then output` 1 `else output` 0 

Figure 5.26: Second preimage resistance: simulator _S_ in Game 2. 

88 

**Definition 14** (Predicate ConnectChallenge) **.** _Let G_ = ( _X, Y, Z_ ) _be the current graph and let x ∈ X. The Boolean predicate_ ConnectChallenge( _x_ ) _evaluates to True if and only if for some ℓ ∈_ [0 _, k_<sup>_∗_</sup> _−_ 2] _, x ∈ X_<sup>0</sup><sup>_,ℓ_</sup> _and x ⋆,ℓ_ ⇝+1 _yℓ_<sup>_∗_</sup> +1<sup>_._</sup> 

We modify _S_ to detect that ConnectChallenge( _x_ ) is realized for some response state _x_ output by the simulation of _P_ , in which case _S_ aborts. We refer to this abortion event as Abort1. _S_ is shown on Fig. 5.27. 

`Initialization of` _S_ `No input, no output 1. randomly select` _M_<sup>_∗_</sup> _←{_ 0 _,_ 1 _}_<sup>_κ_</sup> `2. set` _X_ = _Y_ = _Z_ = _∅_ `3. compute` _C_<sup>_P_</sup> ( _M_<sup>_∗_</sup> ) = _h_ `using the simulation of` _P_ `below Simulation of` _P_ `Input:` _y_ = ( _m, a, b, c_ ) _∈X_ `from` _O_ `(either` _A_ `or` _S_ `) Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _y_ `to` _Y F_ `2. if there exists` _y → x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) _∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _X_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _x_ ) `(event` Abort1 `) then abort (d) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ 

`Simulation of` _P_<sup>_−_1</sup> `Input:` _x_ = ( _a, b, c_ ) _∈X_ `from` _A_ `Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _x_ `to` _X F_ `2. if there exists` ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) = _y → x ∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _Y_ `and edge` _y → x_ `to` _Z_ `(c) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ `Completion of` _S_ `Input:` _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> `from` _A_ `1. compute` _C_<sup>_P_</sup> ( _M, ℓm_ ) `by calling` _P_ `accordingly 2. if` _C_<sup>_P_</sup> ( _M, ℓm_ ) = _h_ `then output` 1 `else output` 0 

Figure 5.27: Second preimage resistance: simulator _S_ in Game 3. 

We state: 

**Claim 15.** _One has |_ Pr [ _W_ 3] _−_ Pr [ _W_ 2] _| ≤_ Pr [Abort1] _≤ N ·_ ( _k_<sup>_∗_</sup> _−_ 1) _·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup> _._ 

_Proof._ Let _y_ = ( _m, a, b, c_ ) _∈ Y_ be a query to _P_ and suppose _y_ is the _q_ -th query to ( _P, P_<sup>_−_1</sup> ) for _q ∈_ [1 _, N_ ]. Considering the set _D_ ( _m, c_ ) of all possible response states _x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ), let us assume that _y ∈ Y_<sup>0</sup><sup>_,ℓ_</sup> for some _ℓ ∈_ [0 _, k_<sup>_∗_</sup> _−_ 2]. Noting _yℓ_<sup>_∗_</sup> +1<sup>=(</sup><sup>_m∗_</sup> _ℓ_ +1<sup>_, a_</sup> _ℓ_<sup>_∗_</sup> +1<sup>_, b_</sup> _ℓ_<sup>_∗_</sup> +1<sup>_, c_</sup> _ℓ_<sup>_∗_</sup> +1<sup>)andtaking</sup> 

89 

the probabilities over the random choice _x ← D_ ( _m, c_ ), we get that 

Hence 

Overall, 

which concludes the proof. 

**Game 4.** We now make _S_ abort when _A_ succeeds in connecting an antipath (with respect to _h_ ) to the challenge path _µ_<sup>_∗_</sup> . We define the predicate ConnectChallenge to nodes _y ∈ Y_ as follows. 

**Definition 15.** _Let G_ = ( _X, Y, Z_ ) _be the current graph and let y ∈ Y ._ ConnectChallenge( _y_ ) _evaluates to True if and only if for some ℓ ∈_ [1 _, k_<sup>_∗_</sup> _−_ 1] _, y ∈ Y_ 0 _,ℓ and x_<sup>_∗_</sup> _ℓ−_ 1 ⇝ _⋆,ℓ y._ 

We modify _S_ to detect that ConnectChallenge( _y_ ) is realized for some response state _y_ output by the simulation of _P_<sup>_−_1</sup> , in which case _S_ aborts. We refer to this abortion event as Abort2. The new simulator is depicted on Fig. 5.28. 

We state: 

**Claim 16.** _One has |_ Pr [ _W_ 4] _−_ Pr [ _W_ 3] _| ≤_ Pr [Abort2] _≤ N ·_ ( _k_<sup>_∗_</sup> _−_ 1) _·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup> _._ 

_Proof._ Let _x_ = ( _m, a, b, c_ ) _∈ Y_ be a query to _P_<sup>_−_1</sup> and suppose that _x_ is the _q_ -th query to ( _P, P_<sup>_−_1</sup> ) for _q ∈_ [1 _, N_ ]. Considering the set _D_ ( _m, c_ ) of all possible response states _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ), let us assume that _x ∈ X_ 0 _,ℓ_ for some _ℓ ∈_ [1 _, k_<sup>_∗_</sup> _−_ 1]. Noting _x_<sup>_∗_</sup> _ℓ−_ 1<sup>=(</sup><sup>_m∗_</sup> _ℓ−_ 1<sup>_, a∗_</sup> _ℓ−_ 1<sup>_, b∗_</sup> _ℓ−_ 1<sup>_, c∗_</sup> _ℓ−_ 1<sup>)andtaking</sup> the probabilities over the random choice _x ← D_ ( _m, c_ ), we get that 

Hence 

90 

`Initialization of` _S_ 

```
Noinput,nooutput
```

`1. randomly select` _M_<sup>_∗_</sup> _←{_ 0 _,_ 1 _}_<sup>_κ_</sup> `2. set` _X_ = _Y_ = _Z_ = _∅_ `3. compute` _C_<sup>_P_</sup> ( _M_<sup>_∗_</sup> ) = _h_ `using the simulation of` _P_ `below` 

`Simulation of` _P_ 

`Input:` _y_ = ( _m, a, b, c_ ) _∈X_ `from` _O_ `(either` _A_ `or` _S_ `) Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _y_ `to` _Y F_ `2. if there exists` _y → x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) _∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _X_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _x_ ) `(event` Abort1 `) then abort (d) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ `Simulation of` _P_<sup>_−_1</sup> `Input:` _x_ = ( _a, b, c_ ) _∈X_ `from` _A_ `Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _x_ `to` _X F_ `2. if there exists` ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) = _y → x ∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _Y_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _y_ ) `(event` Abort2 `) then abort (d) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ 

`Completion of` _S_ `Input:` _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> `from` _A_ `1. compute` _C_<sup>_P_</sup> ( _M, ℓm_ ) `by calling` _P_ `accordingly 2. if` _C_<sup>_P_</sup> ( _M, ℓm_ ) = _h_ `then output` 1 `else output` 0 

Figure 5.28: Second preimage resistance: simulator _S_ in Game 4. 

91 

Finally, 

as announced. 

**Game 5.** We now insert an early-abort condition as follows. _S_ creates two collections of sets _{Y_ [[ _β_ ]] _| β ∈{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _}_ and _{Y ⟨⟨γ⟩⟩| γ ∈{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _}_ where all sets are initially empty at the beginning of the game. Each time _A_ sends a query _x_ = ( _m, a, b, c_ ) to _P_<sup>_−_1</sup> , _S_ selects a response state _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) as in Game 2; however, _S_ now adds _y_ to sets _Y_ [[ _b_<sup>_′_</sup> ⊟ _m_ ]] and _Y ⟨⟨b_<sup>_′_</sup> _⟩⟩_ . This operation amounts to sort response states output by the simulation of _P_<sup>_−_1</sup> according to the two mappings ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) _�→ b_<sup>_′_</sup> ⊟ _m_ and ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) _�→ b_<sup>_′_</sup> . When adding _y_ to _Y_ [[ _b_<sup>_′_</sup> ⊟ _m_ ]] and _Y ⟨⟨b_<sup>_′_</sup> _⟩⟩_ , _S_ checks that these two sets have a limited number _B_ of elements and aborts if this is no longer the case. This is as depicted on Fig. 5.29. The bound _B_ is an optimization parameter which is later determined as in the proof of Theorem 4. 

We state: 

The proof is identical to the proof provided in the previous section. 

**Property 7.** _Unless S aborts,_ max _β |Y_ [[ _β_ ]]( _q_ ) _| ≤ B and_ max _γ |Y ⟨⟨γ⟩⟩_ ( _q_ ) _| ≤ B for any q ∈_ [1 _, N_ ] _._ 

**Game 6.** We now make sure that _A_ cannot create an E-path from _x_ 0 to some _x ∈X_ [ _h_ ] when sending a query to _P_ during the game. We reuse to the predicate Connect defined in Section 5.6. We modify simulator _S_ to detect a connection whenever a new output value _x ∈X_ is assigned to _P_ ( _y_ ) and abort when Connect( _x,_ ˜ _y_ ) is true for some preexisting _y_ ˜. We refer to this event as Abort4. The upgraded simulator is depicted on Fig. 5.30. 

**Claim 18.** _One has |_ Pr [ _W_ 6] _−_ Pr [ _W_ 5] _| ≤_ Pr [Abort4] _≤_ 2 _· N · B ·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup> _._ 

The proof is identical to the one provided in Section 5.5. 

**Property 8.** _Unless S aborts, the treatment of a request to P by S can by no means create a connection between a path and an antipath._ 

**Game 7.** We now ascertain that _A_ is unable to create an E-path from _x_ 0 to some _x ∈X_ [ _h_ ] by sending adaptively chosen queries to _P_<sup>_−_1</sup> during the game. We proceed in two steps and start by inserting a new abort condition. _S_ creates a collection of sets _{X_ [[ _λ_ ]] _| λ ∈{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _}_ where all sets are set to _∅_ at the beginning of the game. For each query _y_ = ( _m, a, b, c_ ) that _A_ sends to _P_ , _S_ assigns a response state _x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) as in Game 6; however, _S_ now adds _x_ to sets _X_ [[ _b_<sup>_′_</sup> ]]. When adding _x_ to _X_ [[ _b_<sup>_′_</sup> ]], _S_ checks that _|X_ [[ _b_<sup>_′_</sup> ]] _| ≤ B_ and aborts if this is not the case: this event is referred to as Abort5. 

The proof has already been given in Section 5.5. We claim the following property. 

**Property 9.** _Unless S aborts,_ max _λ |X_ [[ _λ_ ]]( _q_ ) _| ≤ B for any q ∈_ [1 _, N_ ] _._ 

**Game 8 (final game).** We modify simulator _S_ to detect a connection whenever a new output ˜ value _y ∈X_ is assigned to _P_<sup>_−_1</sup> ( _x_ ) and abort when Connect(˜ _x, y_ ) is true for some preexisting _x_ . We refer to this event as Abort6. The upgraded simulator is depicted on Fig. 5.31. 

**Claim 20.** _One has |_ Pr [ _W_ 8] _−_ Pr [ _W_ 7] _| ≤_ Pr [Abort6] _≤_ 2 _· N · B ·_ 2<sup>_−_(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup> _._ 

The proof is similar to the one of Section 5.5. We claim: 

**Property 10.** _Unless S aborts, requests to P_<sup>_−_1</sup> _treated by S can by no means create a connection between a path and an antipath._ 

92 

`Initialization of` _S_ `No input, no output 1. randomly select` _M_<sup>_∗_</sup> _←{_ 0 _,_ 1 _}_<sup>_κ_</sup> `2. set` _X_ = _Y_ = _Z_ = _∅_ `3. compute` _C_<sup>_P_</sup> ( _M_<sup>_∗_</sup> ) = _h_ `using the simulation of` _P_ `below Simulation of` _P_ `Input:` _y_ = ( _m, a, b, c_ ) _∈X_ `from` _O_ `(either` _A_ `or` _S_ `) Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _y_ `to` _Y F_ `2. if there exists` _y → x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) _∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _X_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _x_ ) `(event` Abort1 `) then abort (d) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ 

`Simulation of` _P_<sup>_−_1</sup> `Input:` _x_ = ( _a, b, c_ ) _∈X_ `from` _A_ `Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _x_ `to` _X F_ `2. if there exists` ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) = _y → x ∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _Y_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _y_ ) `(event` Abort2 `) then abort (d) add node` _y_ `to` _Y_ [[ _b_<sup>_′_</sup> ⊟ _m_ ]] `and` _Y ⟨⟨b_<sup>_′_</sup> _⟩⟩_ `(e) if` _|Y_ [[ _b_<sup>_′_</sup> ⊟ _m_ ]] _| > B_ `or` _|Y ⟨⟨b_<sup>_′_</sup> _⟩⟩| > B_ `(event` Abort3 `) then abort (f) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ 

`Completion of` _S_ `Input:` _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> `from` _A_ `1. compute` _C_<sup>_P_</sup> ( _M, ℓm_ ) `by calling` _P_ `accordingly 2. if` _C_<sup>_P_</sup> ( _M, ℓm_ ) = _h_ `then output` 1 `else output` 0 

Figure 5.29: Second preimage resistance: simulator _S_ in Game 5. 

93 

###### `Initialization of` _S_ 

```
Noinput,nooutput
```

`1. randomly select` _M_<sup>_∗_</sup> _←{_ 0 _,_ 1 _}_<sup>_κ_</sup> `2. set` _X_ = _Y_ = _Z_ = _∅_ `3. compute` _C_<sup>_P_</sup> ( _M_<sup>_∗_</sup> ) = _h_ `using the simulation of` _P_ `below` 

`Simulation of` _P_ 

`Input:` _y_ = ( _m, a, b, c_ ) _∈X_ `from` _O_ `(either` _A_ `or` _S_ `) Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _y_ `to` _Y F_ `2. if there exists` _y → x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) _∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _X_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _x_ ) `(event` Abort1 `) then abort (d) if` _∃y_ ˜ _∈ Y_ `such that` Connect( _x,_ ˜ _y_ ) `(event` Abort4 `) then abort (e) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ 

###### `Simulation of` _P_<sup>_−_1</sup> 

`Input:` _x_ = ( _m, a, b, c_ ) _∈X_ `from` _A_ `Output:` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `1. add node` _x_ `to` _X F_ `2. if there exists` ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) = _y → x ∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _Y_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _y_ ) `(event` Abort2 `) then abort (d) add node` _y_ `to` _Y_ [[ _b_<sup>_′_</sup> ⊟ _m_ ]] `and` _Y ⟨⟨b_<sup>_′_</sup> _⟩⟩_ `(e) if` _|Y_ [[ _b_<sup>_′_</sup> ⊟ _m_ ]] _| > B_ `or` _|Y ⟨⟨b_<sup>_′_</sup> _⟩⟩| > B_ `(event` Abort3 `) then abort (f) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ 

`Completion of` _S_ `Input:` _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> `from` _A_ 

`1. compute` _C_<sup>_P_</sup> ( _M, ℓm_ ) `by calling` _P_ `accordingly 2. if` _C_<sup>_P_</sup> ( _M, ℓm_ ) = _h_ `then output` 1 `else output` 0 

Figure 5.30: Second preimage resistance: simulator _S_ in Game 6. 

94 

`Initialization of` _S_ `No input, no output 1. randomly select` _M_<sup>_∗_</sup> _←{_ 0 _,_ 1 _}_<sup>_κ_</sup> `2. set` _X_ = _Y_ = _Z_ = _∅_ `3. compute` _C_<sup>_P_</sup> ( _M_ ) = _h_ `using the simulation of` _P_ `below Simulation of` _P_ `Input:` _y_ = ( _a, b, c_ ) _∈X_ `from` _O_ `(either` _A_ `or` _S_ `) Output:` _b_<sup>_′_</sup> `1. add node` _y_ `to` _Y F_ `2. if there exists` _y → x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) _∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _x_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _X_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _x_ ) `(event` Abort1 `) then abort (d) if` _∃y_ ˜ _∈ Y_ `such that` Connect( _x,_ ˜ _y_ ) `(event` Abort4 `) then abort (e) add node` _x_ `to` _X_ [[ _b_<sup>_′_</sup> ]] `(f) if` _|X_ [[ _b_<sup>_′_</sup> ]] _| > B_ `(event` Abort5 `) then abort (g) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _O_ 

`Simulation of` _P_<sup>_−_1</sup> `Input:` _x_ = ( _a, b, c_ ) _∈X_ `from` _A_ `Output:` _b_<sup>_′_</sup> `1. add node` _x_ `to` _X F_ `2. if there exists` ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) = _y → x ∈ Z_ `then return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ `3. else (a) randomly select` _a_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓa_</sup> `and` _b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_<sup>_ℓm_</sup> _F_ `(b) add node` _y_ = ( _m, a_<sup>_′_</sup> _, b_<sup>_′_</sup> _, c_ ) `to` _Y_ `and edge` _y → x_ `to` _Z_ `(c) if` ConnectChallenge( _y_ ) `(event` Abort2 `) then abort (d) add node` _y_ `to` _Y_ [[ _b_<sup>_′_</sup> ⊟ _m_ ]] `and` _Y ⟨⟨b_<sup>_′_</sup> _⟩⟩_ `(e) if` _|Y_ [[ _b_<sup>_′_</sup> ⊟ _m_ ]] _| > B_ `or` _|Y ⟨⟨b_<sup>_′_</sup> _⟩⟩| > B_ `(event` Abort3 `) then abort (f) if` _∃x_ ˜ _∈ X_ `such that` Connect(˜ _x, y_ ) `(event` Abort6 `) then abort (g) return` ( _a_<sup>_′_</sup> _, b_<sup>_′_</sup> ) `to` _A_ 

`Completion of` _S_ `Input:` _M ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> `from` _A_ `1. compute` _C_<sup>_P_</sup> ( _M, ℓm_ ) `by calling` _P_ `accordingly 2. output` 0 

Figure 5.31: Second preimage resistance: final simulator _S_ . 

95 

**Conclusion.** Summing up, we get the bound 

The first two terms are optimized as in Section 5.5. Noting that once optimized they remain smaller than 

we finally get the bound claimed in Theorem 5. 

96 

## **Chapter 6** 

# **Weakened Versions of Shabal** 

#### **Contents** 

|**6.1**|**With Smaller Words**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . .**<br>**97**|
|---|---|
|**6.2**|**With Linear Message Introduction . . . . . . . . . . . . . . . . . . . .**<br>**98**|
|**6.3**|**With** _U_(_x_) =_x_ **and** _V_(_x_) =_x_ **. . . . . . . . . . . . . . . . . . . . . . . . .**<br>**99**|
|**6.4**|**With** _U_(_x_) = (_x ≪_1)_⊕x_ **and** _V_(_x_) = (_x ≪_2)_⊕x_<br>**. . . . . . . . . . . . .**<br>**99**|
|**6.5**|**Without the Last Update Loop on** _A_**. . . . . . . . . . . . . . . . . . . 100**|
|**6.6**|**Other Non-described Variants . . . . . . . . . . . . . . . . . . . . . . . 100**|

In order to simplify the analysis of our hash function, we propose several weakened versions of Shabal, with names of the Weakinson-XXX form. The weaknesses that might be found on these variants may or may not teach us some things about the full hash function, depending on the techniques used in the attacks. Most of the variants we propose consist in removing the nonlinearity sources depicted in Section 4.8. 

Even if we have tried to simplify the cryptanalyst’s work, we may have not taken into account some simplifications that would be interesting to study. In case, we encourage the interested reader to consider other variants of Shabal, as far as they do follow the fundamental basis of its design. 

### **6.1 With Smaller Words** 

First proposed four variants simply consider that words are no more 32-bit words, but respectively 1-, 4-, 8- and 16-bit words. We therefore name these variants as Weakinson-1bit, Weakinson-4bit, Weakinson-8bit and Weakinson-16bit. Amongst these reduced versions, the 1-bit variant is much weaker, as many of the Shabal operations would be meaningless in this context ( _e.g.,_ the bit rotations, _U_ ( _x_ ) = 3 _× x_ mod 2<sup>32</sup> , _V_ ( _x_ ) = 5 _× x_ mod 2<sup>32</sup> , additions). 

Definitions of the variants Weakinson-1bit, Weakinson-4bit, Weakinson-8bit and Weakinson-16bit strictly follows the standard definition (see Section 2.3), except that operations that were modulo 2<sup>32</sup> are replaced by operations that are modulo 2<sup>1</sup> , 2<sup>4</sup> , 2<sup>8</sup> or 2<sup>16</sup> ( _x_ ≪ _y_ is replaced by _x_ ≪ ( _y_ mod (1 _,_ 4 _,_ 8 _,_ 16)) respectively). For the counter and the prefix blocks ( _M−_ 1 _, M_ 0), we simply consider them constructed on words of 1 (respectively 4,8,16) bits. Thus, for example, in Weakinson-1bit, the counter “loops” each 4 message blocks, while ( _M−_ 1 _, M_ 0) is made of alternating bits 0 and 1. 

The padding rule is unchanged but also applies on _small words_ . In the case of a message whose bitlength is a multiple of the block length (which is the case in the following examples) the padding thus consists of a full extra block. The first word of this block has value `0x0080` (resp. `0x80` , `0x8` , `1` ) for Weakinson-16bit (resp. Weakinson-8bit, Weakinson-4bit, Weakinson-1bit), and this first word is followed by 15 other words whose value is 0. 

Finally, to behave as a restriction of full Shabal over smaller words, the hash value corresponds to the last _ℓh/_ 32 words of the state buffer C. As a consequence, for all _small word_ variants 

97 

(Weakinson-1bit,. . . ,Weakinson-16bit), the exact output length is not equal to the expected one ( _e.g.,_ 64 bits instead of 256 for Weakinson-8bit). 

Pattern for Weakinson-1bit(01<sup>16</sup> ) is as follows, with _lh_ = 256: 

|`A : .......1 .......0 ...`|`....1 .......1 .......1 .......1 .......0 .......0`|
|---|---|
|`.......1 .......0 ...`|`....0 .......1`|
|`B : .......1 .......0 ...`|`....0 .......1 .......1 .......1 .......0 .......0`|
|`.......1 .......1 ...`|`....1 .......1 .......0 .......0 .......0 .......1`|
|`C : .......1 .......0 ...`|`....0 .......1 .......1 .......1 .......0 .......1`|
|`.......0 .......0 ...`|`....0 .......1 .......0 .......0 .......1 .......0`|
|`H : .......0 .......0 ...`|`....0 .......1 .......0 .......0 .......1 .......0`|

Pattern for Weakinson-4bit(04<sup>16</sup> ) is as follows, with _lh_ = 256: 

|`A : .......C .......E ...`|`....1 .......6 .......1 .......F .......5 .......5`|
|---|---|
|`.......8 .......E ...`|`....8 .......4`|
|`B : .......B .......E ...`|`....9 .......B .......4 .......8 .......D .......8`|
|`.......4 .......0 ...`|`....5 .......3 .......9 .......7 .......4 .......8`|
|`C : .......6 .......F ...`|`....4 .......F .......E .......5 .......C .......E`|
|`.......6 .......3 ...`|`....F .......F .......9 .......C .......0 .......D`|
|`H : .......6 .......3 ...`|`....F .......F .......9 .......C .......0 .......D`|

Pattern for Weakinson-8bit(08<sup>16</sup> ) is as follows, with _lh_ = 256: 

|`A : ......F1 ......EB ...`<br>`......D5 ......10 ...`|`...E1 ......3A ......C6 ......58 ......01 ......87`<br>`...8D ......52`|
|---|---|
|`B : ......DE ......54 ...`|`...51 ......7E ......FF ......95 ......2E ......56`|
|`......2E ......12 ...`|`...6E ......5E ......C5 ......59 ......25 ......26`|
|`C : ......C8 ......92 ...`|`...E2 ......5C ......99 ......ED ......A5 ......FF`|
|`......31 ......5D ...`|`...24 ......E0 ......DC ......3F ......69 ......D9`|
|`H : ......31 ......5D ...`|`...24 ......E0 ......DC ......3F ......69 ......D9`|

Pattern for Weakinson-16bit(016<sup>16</sup> ) is the following, with _lh_ = 256: 

|`A : ....076C ....40DC ..`|`..8788 ....AD4C ....F1EF ....69BF ....870A ....40ED`|
|---|---|
|`....3315 ....0EA5 ..`|`..7114 ....F084`|
|`B : ....A681 ....A393 ..`<br>`....C032 ....6A05 ..`|`..9AFA ....CACF ....29E5 ....94AF ....40F7 ....51F0`<br>`..598D ....60DF ....AC4C ....D942 ....432E ....39CC`|
|`C : ....87A9 ....30D0 ..`|`..AA7D ....18FC ....794D ....1071 ....2783 ....EA43`|
|`....8CCB ....BFFB ..`|`..55AF ....D177 ....1671 ....944F ....7EA4 ....0B5D`|
|`H : ....8CCB ....BFFB ..`|`..55AF ....D177 ....1671 ....944F ....7EA4 ....0B5D`|

### **6.3 With** _U_ ( _x_ ) = _x_ **and** _V_ ( _x_ ) = _x_ 

In order to simplify the update of the _A_ buffer, we propose a variant called Weakinson-SimpleUV, where the _U_ and _V_ functions are replaced by identity. We expect this variant to propose a simpler framework for cryptanalysis, without totally removing the _A_ memory effect. 

Pattern for Weakinson-SimpleUV(032<sup>16</sup> ) is as follows, with _lh_ = 256: 

- `A : 97B5AC21 07FABC4E 124079E3 5EE4374B 308FF84D 36F1F76B E256DF9C D5191AB2 37799815 A0244AB4 8091CABD E683AB20` 

- `B : 7B13E5F6 2BC07FC4 6D134194 BF615661 1AD65E53 CA80EC67 5EFD063E 8D3C4E19 F6A58A22 7E70FF7F 15F72B44 35198E6E 4F409255 4955C79C 8A5E526A D09F129E` 

- `C : E45B7968 415606C5 623DEAB2 CAA7C4C3 AD8156FC 312D55EE 463275AE D011A532 8051063F 47936F2C C5B7D1B0 AE9222A8 1224C272 3B6BB168 30A959E0 7CE5CCA4` 

- `H : 8051063F 47936F2C C5B7D1B0 AE9222A8 1224C272 3B6BB168 30A959E0 7CE5CCA4` 

### **6.4 With** _U_ ( _x_ ) = ( _x ≪_ 1) _⊕ x_ **and** _V_ ( _x_ ) = ( _x ≪_ 2) _⊕ x_ 

Another version that we propose is a variant called Weakinson-LinearUV, where the _U_ and _V_ functions are replaced by their linearized counterparts, that is _U_ ( _x_ ) = ( _x ≪_ 1) _⊕ x_ and _V_ ( _x_ ) = ( _x ≪_ 2) _⊕ x_ (remember for example that normally, _U_ is defined by _U_ ( _x_ ) = ( _x ≪_ 1) + _x_ mod 2<sup>32</sup> ). 

Pattern for Weakinson-LinearUV(032<sup>16</sup> ) is as follows, with _lh_ = 256: 

- `A : 7D2C8738 F05B4D6D 285269AD C84D795F 12B047FD 10E216D7 8841EBFA 36264ABE 4611AD57 7738084E F781D82E 8E6D4ECD` 

- `B : 536E59C1 D2A8024C E90C42A2 E94F7F95 CE7E2A0A BEFC757B F362487B 96524FFD D0C5C174 758695F7 E9DEA919 5161C9C1 260A0E37 3E2792B6 6B34F09A 4026F817` 

- `C : EB688602 0320F5D9 44CB8021 4AE599E9 76ABD9F6 13F6D196 DA89469C 1726D214 DD4E3CD9 FE604991 6B3143F8 A736F8E3 F5CBD4C9 ECC16C73 3E01E463 DE1C29BA` 

- `H : DD4E3CD9 FE604991 6B3143F8 A736F8E3 F5CBD4C9 ECC16C73 3E01E463 DE1C29BA` 

99 

### **6.5 Without the Last Update Loop on** _A_ 

One can also consider to remove the last loop on updating of _A_ in the permutation. More precisely, we would remove the 36 updates of form _A_ [ _j_ mod _r_ ] _← A_ [ _j_ mod _r_ ] + _C_ [ _j_ + 3 mod 16]. As shown in the analysis of Section 11.6, this results in a much weaker permutation. 

Pattern for Weakinson-NoFinalUpdateA(032<sup>16</sup> ) is as follows, with _lh_ = 256: 

- `A : E9C8136E 53AF87C2 2AC08B96 35924295 2C1E7E0A A08A0106 A1A16363 E70CC268 B6D84B88 2EA7E106 69890460 EBDB103E` 

- `B : 60C088C4 FD32344D 55F6AFC7 8159C310 0A838854 76385AFD 4AB18F25 51D586B2 C370B22D 75B471C2 5B8381FA 9D1C54E0 DAF7088D A1E92D63 7DF687DD FA7A8419` 

- `C : B2F4BD83 27099457 E2EEFE89 08154CEC 8CEDEA10 C8D599A5 320C880B AC21D064 EFCD7C6A 81F426FB 11576938 347955BF C45598B6 728E0694 D4D34ABD D9D1880E` 

- `H : EFCD7C6A 81F426FB 11576938 347955BF C45598B6 728E0694 D4D34ABD D9D1880E` 

### **6.6 Other Non-described Variants** 

In fact, the number of variants one may consider is almost infinite. The closer they are to the real Shabal, the more interesting the cryptanalysis is. Here, we enumerate some possible modifications, without explicitly giving some test patterns for them. 

One may notably: 

1. remove the counter _w_ ; 

2. reduce _r_ (which reduces the security margin of the construction); 

3. increase _r_ , whose effect remains unsure when it becomes large (as the diffusion is decreased); 

4. reduce _p_ (normally, the security is better if _p_ is larger, but for some differential attacks, increasing _p_ might be a way to decrease some probabilities, as it was the case with 82-round Sha, see [9]); we note that Weakinson-NoFinalUpdateA with _p_ = 1 and _p_ = 2 has been studied in Section 11.6. 

Changing the offsets or the rotate values is more tricky, and so is not considered as an educative variant. 

Of course, any non-trivial combination of the previously depicted variants is possible, and may be the subject of study by the community. Thus, the names of the variants follow our denomination strategy, with for example Weakinson- _⊕_ -16bit-SimpleUV. These combinations allow very weak versions of Shabal. Clearly, the goal is to attack variants that are as close as possible to full Shabal. 

100 

## **Chapter 7** 

# **Implementation Tricks: How to Speed Up Codes on Your Platform** 

#### **Contents** 

|**7.1**|**Des**|**ktop and Server Systems . . . . . . . . . . . . . . . . . . . . . . . . 101**|
|---|---|---|
||7.1.1|Cache Issues<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101|
||7.1.2|Precomputations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 102|
||7.1.3|Machine Code Generation . . . . . . . . . . . . . . . . . . . . . . . . . . 102|
||7.1.4|Parallelism<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103|
|**7.2**|**Emb**|**edded and Small Systems . . . . . . . . . . . . . . . . . . . . . . . 104**|
|**7.3**|**ASI**|**C and FPGA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 104**|

Shabal was meant to be efficient when implemented on common 32-bit and 64-bit general purpose hardware (without needlessly sacrificing performance on smaller systems or implementations with dedicated hardware). Nevertheless, efficient implementation on a given platform requires a proper mapping of the Shabal algorithm structure to the features of that platform. We here list some points which are worth taking into account when implementing Shabal. 

### **7.1 Desktop and Server Systems** 

Desktop and server systems are generic polyvalent computers, using one or a few central processors with a handful of 32-bit or 64-bit registers, and clocked at frequencies measured in gigahertz. That market is dominated by processors compatible with the so-called “x86” instruction set, initially created by Intel. The two now common variants for this instruction set consist of, respectively, about seven 32-bit user registers, or fifteen 64-bit registers. However, other architectures are still widely deployed as well, for instance SPARC and Power systems. 

#### **7.1.1 Cache Issues** 

On big systems, cache issues tend to dominate computation time, because the main memory is quite slower than the CPU. This is an increasing trend, since RAM speed benefits little from increased transistor density, contrary to CPU cores. 

Briefly stated, a hash function implementation provides maximum performance only when it fits within a fraction of the CPU level 1 caches. In a complete application, hashing is just a part of the overall data processing; thus, the hash function implementation shall use only a small part of the L1 caches, because other procedures down the data path use some cache as well, and are typically interleaved with the hash function implementation. Desktop and server processors 

101 

usually feature about 32 or 64 kilobytes of L1 cache for data, and about the same amount for code. 

Shabal implies a very low pressure on the data cache. The state of Shabal fits in less than 300 bytes. Elementary operations are word-based primitives implemented natively by most CPU; none of them is likely to benefit from table-based code. This economy of L1 cache is one of the strong points of Shabal, performance-wise. 

The code L1 cache, however, may become an issue if not taken into account during implementation. A common optimization technique is _loop unrolling_ : when a sequence of instructions is to be executed several times in a row, then it may be worthwhile to duplicate that sequence. Loop unrolling saves some or all of the cost of the loop management itself, at the expense of a greater L1 cache consumption. In Shabal, an obvious candidate for loop unrolling is the permutation, which repeats the same sequence _p_ times. When fully unrolled, this sequence fits in roughly 7 kilobytes of code with _p_ = 3 (this depends on the target architecture and the compiler). This should be small enough to fit in the L1 cache along with the rest of the application code which lies in the critical path. Conversely, unrolling two successive rounds of Shabal (which would transform the “swap” operation of _B_ and _C_ into a mere compilation-time data routing problem) appears not to be worthwhile, because it would double L1 cache consumption. 

Note that this effect of cache consumption is often overlooked in benchmarks, which run the measured function “alone”. 

#### **7.1.2 Precomputations** 

A number of computations do not depend on the actual data. For instance, in the permutation, the indices of the accessed state element are always the same. The value of _i_ +16 _j_ mod _r_ depends on _i_ and _j_ , but _not_ on the input data. This value may thus be computed in advance, at compilation time. Precomputing these indices is natural and immediate when loop unrolling is applied: by unrolling the loops on _i_ and _j_ , all indices become, at the syntax level, constant expressions which the compiler computes directly. 

Some programming language implementations may perform such unrolling automatically; however, this is an optimization feature which can rarely be finely tuned by the programmer. As we saw above, some loops are worth unrolling, but not all, and which unrolling level should be applied depends on the overall application structure and usage, of which the compiler knows little or none. Therefore, it is often necessary to apply unrolling “manually”, _i.e.,_ by duplicating the sequence by hand, directly in source code. Metalanguages ( _e.g.,_ the C preprocessor, when targeting the C programming language) can be used, to some extent, to perform this unrolling operation at compilation time. 

Another possible and quite different precomputation is related to the Shabal prefix. The input data is prefixed by 32 words (two full blocks), which value depend on the intended output length, but is independent of the message data. Instead of prefixing the input message, the Shabal implementation may directly initialize its internal state to the values it should contain _after_ processing the prefix blocks. Such a precomputed internal state uses about 176 bytes per intended output length. Depending on the implementation technique, these 176 bytes may be counted against the data or the code cache; either way, the cost is small, and substantially increases throughput when Shabal is primarily used on very small messages. 

#### **7.1.3 Machine Code Generation** 

The CPU executes _machine code_ . On desktop and server processors, programmers very rarely input machine code (or assembly, which is a direct translation of machine code). Optimization rules for laying out machine code instructions (in particular choosing in which CPU registers data should be stored) are complex, arcane, and more suited to automatic machine code generation. Indeed, modern CPU have been designed so that _compilers_ (in particular C compilers) may perform a good job at machine code generation. Using a programming language such as C also increases 

102 

portability, since optimization rules and actual instructions change between processor brands and generations. 

Optimization of a Shabal implementation is thus mostly a matter of giving the compiler as much information as possible on what operations shall occur. Precomputation of indices for state access is an important step in that process. When most loops are unrolled (namely, the _i_ and _j_ loops in the permutation, and the _i_ loop in the message input), then spatial layout of state elements becomes irrelevant: each of the state words ( _A_ , _B_ , _C_ and _W_ ) and of the current message block words ( _M_ ) are accessed independently, and which word is accessed is known at compile time. It turns out that it helps the compiler to explicitly state that fact, by first “copying” the full state to so many local variables with no “array” semantics. The machine code generation system knows how to optimize away unneeded copies (when the architecture supports machine opcodes with memory operands); and by making explicit copies to local variables, the programmer informs the compiler that the array semantics (ordered sequence of slots) need not be maintained. Furthermore, local variables which addresses are never taken are known never to be accessed through indirections, which again helps the compiler. 

The core permutation in Shabal uses three rotations of 32-bit words, by 1, 15 and 17 bits respectively. Some architectures feature explicit instructions for rotations ( _e.g.,_ the `rol` opcode on x86 processors); for other systems, logical shifts and Boolean combinations must be used. Regardless of the architecture features, usual programming language ( _e.g.,_ C) lack standard operators for expressing such a rotation. Some compilers provide ad hoc extensions. However, it turns out that most modern compilers recognize the “rotation construction” (two shifts and a Boolean bitwise or) and know how to use the specific rotation instructions of the processor, if available and worthwhile. 

The permutation includes multiplications by 3 and 5 (modulo 2<sup>32</sup> ). Multiplication by 3 can be implemented with two additions, or a logical shift and an addition. Multiplication by 5 is a matter of three additions, or one shift and one addition. On some platforms, multiplications by 3 or 5 can be performed with a single efficient opcode primarily designed for memory array access. Since the optimal representation of such a multiplication varies between architectures, it is recommended to express the operation as a raw multiplication, so that the compiler may choose the best code sequence for this operation. 

#### **7.1.4 Parallelism** 

Although Shabal is inherently a sequential algorithm, it has some limited support for local parallelism. Namely: 

- The decoding of a message block into 16 words may be performed in parallel, limited mostly by the input memory bus width and speed. 

- The addition (to _B_ ) and subtraction (from _C_ ) of message words can be performed in parallel. 

- The rotation by seventeen bits of all words of _B_ , at the beginning of the permutation, can be performed parallely. 

- The additions of words of _C_ to _A_ at the end of the permutation modify the various _A_ words independently from each other. 

- The swap of _B_ and _C_ is also a routing problem which can be performed in parallel. 

The easiest way to exploit this parallelism is to let the compiler perform its job. Loop unrolling and the use of local variables help the compiler detect which code chunks may be computed independently of each other, and thus be scheduled to operate simultaneously on distinct parts of the processor. 

Modern processors have special units meant for SIMD computations. An example is the SSE2 unit which is found on recent x86-compatible processors. Preliminary implementation experiments 

103 

have not shown those units to be worthwhile for Shabal implementation, mostly because transferring the data to and from the SIMD unit proved to be too expensive, with regards to the gains obtained by parallel execution. **7.2 Embedded and Small Systems** 

Recent embedded and small systems tend to align on the use of 32-bit processors, mostly MiPS and ARM cores. Even smart cards gradually abandon 8-bit and 16-bit cores. Shabal uses only 32-bit words and simple operations (bitwise Boolean operations, and additions modulo 2<sup>32</sup> ). Shabal does not use complex operations such as multiplications; modular multiplication is efficient on desktop and server systems, but many embedded systems lack efficient hardware support for multiplication (as was explained above, the multiplications by 3 and 5, which are part of the core permutation, are usually translated to additions or other simpler operations). 

The _w_ counter, stored in the _W_ buffer, is nominally defined as a 64-bit value; however, that counter is initialized at 0 and is incremented for each data block. Thus, the 32 higher bits of _W_ remain equal to zero as long as the total input data size is less than 2<sup>32</sup> 512-bit blocks, _i.e.,_ about 275 gigabytes<sup>1</sup> . This amount of data far exceeds what a typical embedded system may ever 

|process; this allows for a 32-bit only handling of _W_. Even if a full 64-bit _W_ must be maintained,|
|---|
|then it is easy to manually handle the carry: if the increment of the lower 32-bit of _W_ yields the<br>value 0, then a carry should be propagated to the higher bits. Note that besides being incremented|
|for each input block, the main use of _W_ is to be split into two 32-bit words, combined with two|
|state words at each round. Thus, even if the host platform supports 64-bit values natively, it may|
|be a good idea to keep _W_ as two separate 32-bit words.|
|If Shabal must be implemented on a very small, 8-bit or 16-bit CPU, then carry propagation|
|must be applied to all 32-bit additions. On such an architecture, 32-bit words are split into several<br>|
|chunks of length 8 or 16 bits; thus, a rotation by 16 bits, being a swap of the high and low halves,<br>|
|is a mere problem of data routing which can be solved with little to no runtime cost. Assuming<br>|
|the 16-bit rotation to be essentially free, we can see that all word rotations used in Shabal can|
|be simplifed to left or right rotations by 1 bit, which are often more efcient on small CPU than<br>generic _n_-bit shifts or rotations.|
|The initial state for Shabal is defned from the processing of the prefx, which depends only|
|on the intended output size. Performance-wise, this step is usually replaced by a precomputed|
|IV, which is the internal Shabal state _after_ processing of the prefx blocks. However, on platforms<br>where code space is a very scarce resource, that IV could be replaced by explicit processing of the|

prefix, which may use a few less code bytes, at the expense of some extra clock cycles for each hashed message. Another trade-off between code size and computing speed is the amount of loop unrolling which is applied when implementing the permutation. 

## **Part 2.B.2** 

**A Statement of the Algorithm’s Estimated Computational Efficiency and Memory Requirements in Hardware and Software** 

106 

## **Chapter 8** 

# **A Statement of the Expected Strength** 

113 

## **Chapter 10** 

# **Statement of the Expected Strength** 

#### **Contents** 

|**10.1 Collision Resistance . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 114**|
|---|
|**10.2 Preimage Resistance**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . . 115**|
|**10.3 Second-preimage Resistance . . . . . . . . . . . . . . . . . . . . . . . . 115**|
|**10.4 Resistance to Length-extension Attacks . . . . . . . . . . . . . . . . . 115**|
|**10.5 Strength of a Subset of the Output Bits . . . . . . . . . . . . . . . . . 116**|
|**10.6 PRF HMAC-Shabal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 116**|

In this chapter, we list our security claims, concerning collision resistance, one-wayness and second-preimage resistance of Shabal. In all following statements, the supported message length is supposed to be at most 2<sup>64</sup> blocks, _i.e.,_ 2<sup>73</sup> bits. Note that, as currently described, Shabal can accommodate longer messages (in fact, messages of arbitrary length), however we do not claim anything regarding the security for messages longer than this bound. 

### **10.1 Collision Resistance** 

In order to quantify the collision resistance of Shabal, we define a family of Shabal variants, in which the initial values of both the internal state and the counter can be arbitrarily fixed and are viewed as parameters. 

Let _M,_ ( _M_ 1 _, ..., Mk_ ) be a _k_ -uple of message blocks. We define Shabal<sup>_∗_</sup> ( _M, S_ 0 _, W_ 0) as the words _Ci_ for 16 _− ℓh/_ 32 _≤ i ≤_ 15 of state _Sk_ +3, which is defined by the following relations: 

Informally, Shabal<sup>_∗_</sup> ( _M, S, W_ ) is a version of Shabal( _M_ ) with the IV set to _S_ 0, and the initial value of the counter set to _W_ 0. The collision resistance of Shabal is defined as the resistance to the following type of adversaries: 

1. The challenger draws random message blocks _M−_ 1 _, M_ 0 and sends them to the adversary; 

2. The adversary outputs _M, M_<sup>_′_</sup> and wins the game if _M_<sup>_′_</sup> = _M_ and Shabal<sup>_∗_</sup> ( _M−_ 1 _||M_ 0 _||M,_ 0 _, −_ 1) = Shabal<sup>_∗_</sup> ( _M−_ 1 _||M_ 0 _||M_<sup>_′_</sup> _,_ 0 _, −_ 1). 

114 

As collisions exist for all hash functions, we randomize the security game by randomizing the prefix used for Shabal. 

The existence of deterministic adversaries that can output collisions for a given hash function with probability 1 can also be dealt with by taking account of _human ignorance_ [37]. We then define the notion of collision resistance of Shabal as its resistance to _known_ collision search algorithms, defined by their ability to output two distinct messages _M_ and _M_<sup>_′_</sup> such that _H_ ( _M_ ) = _H_ ( _M_<sup>_′_</sup> ). 

**Security Claim 1.** _For any ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}, finding a collision for Shabal of message digest ℓh bits requires at least_ 2<sup>_ℓh/_2</sup> _calls to the message round function._ 

### **10.2 Preimage Resistance** 

We define the preimage resistance of Shabal as its resistance to all known adversaries of the type described below. 

1. The challenger draws a random _H ∈{_ 0 _,_ 1 _}_<sup>_ℓh_</sup> and sends it to the adversary; 

2. The adversary outputs a message _M_ and wins the game if Shabal( _M_ ) = _H_ . 

We now claim the following security against preimage attacks. 

**Security Claim 2.** _For any ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}, any preimage attack against Shabal with ℓh-bit message digests requires at least_ 2<sup>_ℓh_</sup> _calls to the message round function._ 

### **10.3 Second-preimage Resistance** 

We define the notion of second-preimage resistance as the resistance to all known adversaries of the type described below, with a parameter _k_ . 

1. The challenger draws a random _M ∈{_ 0 _,_ 1 _}_<sup>2</sup><sup>_k_</sup> , and sends it to the adversary; 

2. The adversary outputs _M_<sup>_′_</sup> and wins the game if Shabal( _M_ ) = Shabal( _M_<sup>_′_</sup> ) and _M_<sup>_′_</sup> = _M_ . 

We now claim the following security against second-preimage attacks. 

**Security Claim 3.** _For any ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}, any second-preimage attack against Shabal-ℓh for messages shorter than_ 2<sup>_k_</sup> _bits requires at least_ 2<sup>_ℓh−k_</sup> _calls to the message round function._ 

### **10.4 Resistance to Length-extension Attacks** 

The well-known Merkle-Damg˚ard construction has an undesirable property called _length extension_ . It means that once an attacker has one collision, _i.e.,_ two messages _M_ 1 and _M_ 2 with _|M_ 1 _|_ = _|M_ 2 _|_ such that _H_ ( _M_ 1) = _H_ ( _M_ 2), then for any suffix _M_ it also holds that _H_ ( _M_ 1 _∥_ pad( _M_ 1) _∥M_ ) = _H_ ( _M_ 2 _∥_ pad( _M_ 2) _∥M_ ). 

The length-extension attack can be extended to a more general setting, in the following sense: given _H_ ( _M_ ), an attacker can compute _H_ ( _M ||_ pad( _M_ ) _||M_<sup>_′_</sup> ) for any _M_<sup>_′_</sup> , even if she does not know _M_ . 

The question then arises whether such an attack can be applied to Shabal. In other words, can an adversary generate a large number of distinct collisions, with the cost of only one collision search? We can consider the following security game: 

1. The challenger draws random message blocks _M−_ 1 _, M_ 0 and sends them to the adversary; 

115 

2. The adversary outputs _M, M_<sup>_′_</sup> and wins the game if Shabal<sup>_∗_</sup> ( _M−_ 1 _||M_ 0 _||M ||T,_ 0 _, −_ 1) = Shabal<sup>_∗_</sup> ( _M−_ 1 _||M_ 0 _||M_<sup>_′_</sup> _||T,_ 0 _, −_ 1) for all possible suffixes _T_ . 

The message extension attack can be applied to the Shabal hash function only if an internal collision occurs before the three final rounds. However, the complexity for finding an internal collision in Shabal- _ℓh_ (with _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}_ ) is expected to require at least 2<sup>512</sup><sup>_/_2</sup> calls to the message round function, as the cost of an internal collision is expected to be the same for the five output lengths. 

We then claim the following resistance to length-extension attacks. 

**Security Claim 4.** _For any ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}, any length-extension attack against Shabal-ℓh requires at least_ 2<sup>256</sup> _calls to the message round function._ 

### **10.5 Strength of a Subset of the Output Bits** 

This section claims the security of truncated versions of Shabal. The idea is not new and consists in building a variant of a hash function by simply truncating the output and keeping only the first bits output by the entire function. Here we go even further, by stating that we can not only _truncate_ the output but also extract _any substring_ of the output bitstring. Informally, our claim thus says that all bits resulting from a Shabal computation are equally strong. 

**Security Claim 5.** _For any ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _} and any ℓ ≤ ℓh, any ℓ-bit hash function specified by taking a fixed subset of the output bits of Shabal-ℓh meets the above requirements with ℓ replacing ℓh._ 

### **10.6 PRF HMAC-Shabal** 

In this section we suggest the use of Shabal in the HMAC construction and claim the following security bound about the security of HMAC-Shabalviewed as a PRF (Pseudo-Random Function) family. 

**Security Claim 6.** _For any ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}, any distinguishing attack against HMAC-Shabal-ℓh requires at least_ 2<sup>_ℓh/_2</sup> _calls to the message round function._ 

An argument for this claim is provided by the fact that distinguishing Shabal- _ℓh_ from a random function requires at least 2<sup>_ℓh/_2</sup> calls to the message round function. 

116 

## **Part 2.B.5** 

# **An Analysis of the Algorithm with Respect to Known Attacks** 

117 

## **Chapter 11** 

# **Shabal: Resistance against Known Attacks** 

#### **Contents** 

|**11.1 Known Attacks Identifed by the Security Proofs . . . . . . . . . . **|**. 119**|
|---|---|
|11.1.1 Collision Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. 119|
|11.1.2 Second-preimage Attacks<br>. . . . . . . . . . . . . . . . . . . . . . . . .|. 119|
|11.1.3 Preimage Attacks. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. 120|
|**11.2 Internal Collisions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **|**. 121**|
|11.2.1 Generic Internal Collision Attack . . . . . . . . . . . . . . . . . . . . .|. 121|
|11.2.2 One-block Internal Collisions . . . . . . . . . . . . . . . . . . . . . . .|. 122|
|**11.3 Diferential Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . **|**. 123**|
|11.3.1 Truncated Diferential . . . . . . . . . . . . . . . . . . . . . . . . . . .|. 123|
|11.3.2 Diferential Trails without any Input Diference for _U_ and _V_ . . . . . .|. 123|
|11.3.3 Diferential Trails without any Diference in _A_<br>. . . . . . . . . . . . .|. 124|
|11.3.4 Symmetric Diferential Trails . . . . . . . . . . . . . . . . . . . . . . .|. 125|
|**11.4 Fixed Points**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **|**. 126**|
|**11.5 Generic Attacks against Weakinson-1bit**<br>**. . . . . . . . . . . . . . . **|**. 126**|
|**11.6 (Second)-preimage Attack against Weakinson-NoFinalUpdateA**<br>**. **|**. 127**|
|11.6.1 Attack against Weakinson-NoFinalUpdateA with _p_= 1<br>. . . . . . . .|. 127|
|11.6.2 Attack against Weakinson-NoFinalUpdateA with _p_= 2<br>. . . . . . . .|. 128|
|**11.7 Generic Attacks Against Merkle-Damg˚ard-Based Hash Functions **|**. 129**|
|11.7.1 Length-extension Attacks . . . . . . . . . . . . . . . . . . . . . . . . .|. 129|
|11.7.2 Multi-Collisions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. 129|
|**11.8 Slide Attacks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . **|**. 130**|
|**11.9 Algebraic Distinguishers and Cube Attacks . . . . . . . . . . . . . . **|**. 130**|
|**11.10Attacks Taking Advantage of The Chosen Constants . . . . . . . . **|**. 130**|
|**11.11Diferential Attack on HMAC-Shabal**<br>**. . . . . . . . . . . . . . . . . **|**. 130**|

We study in this chapter the resistance of Shabal with respect to known attacks, especially to collision and (second)-preimage attacks. The structure of Shabal has some similarities with other _sponge-like_ hash functions that have been proposed in the literature such as Panama [17] and more recently RadioGat´un [5] or Grindahl [29]. The security analysis of Shabal with respect to known attacks stems from the security analysis made on _sponge-like_ hash functions. 

More precisely, Section 11.1 first presents the best collision attack, and (second)-preimage attacks, which originates from Shabal generic construction. These attacks have been exhibited by the security proofs given in Section 5. Generic attacks for internal collisions are also described in 

118 

Section 11.2. Section 11.3 then focuses on differential attacks and the search for some particular differential trails is investigated. Some attacks against weakened versions of Shabal are presented in Sections 11.5 and 11.6. Section 11.7 evaluates the applicability of length extension and multicollision attacks. In Section 11.8, we show that the slide attacks presented in [24] cannot be directly applied to Shabal. We finally explain in Section 11.10 the provenance of constants that are used in Shabal, as requested by NIST. In our analysis, we always consider that 16 _p ≡_ 0 mod _r_ . 

### **11.3 Attacks** 

Most of the collision attacks against hash functions that have been published for now consist in finding a set of message pairs that are to follow a differential trail ( _i.e.,_ a sequence of differences in internal states) that ends to a non-difference and next in estimating the probability of the trail. Thus, the first step in order to mount a differential attack against Shabal is to get a trail with non-zero probability. There is no systematic method to find a trail unless a simple backtracking process is used. Thus, the classical method consists in searching for some particular differential trails which can be handled more easily, such as truncated differential trails, symmetric differential trails or differential trails without any difference in register _A_ . 

#### **11.3.1 Truncated** 

At Asiacrypt 2007, Peyrin [35] found a collision attack against Grindahl using truncated differential trails. A truncated differential trail is a binary differential trail where each bit means that there is a difference or not in an input word. This approach has also been adopted by Bouillaguet and Fouque [11] for the analysis of a reduced version of RadioGat´un. It enabled the authors to discover differential trails with better properties than differential trails obtained through a backtracking algorithm given by the authors of RadioGat´un. 

Truncated differential trails for Shabal then correspond to differential trails for Weakinson-1bit, _i.e.,_ for the weakened version of Shabal with 1-bit words. The existence of such trails is discussed in Section 11.5. 

Truncated differential trails can be used for breaking Grindahl because Grindahl is a byteoriented hash function, using a simple message round function. However, it seems highly improbable that these differential trails can be exploited to derive differential trails on the complete version of Shabal since Shabal deals with 32-bit words, reducing the probability of a truncated difference cancelation. Indeed, most operations contributing to the security of _P_ in Shabal disappear when the word length is reduced to 1: rotations and the nonlinear functions _U_ and _V_ are replaced by the identity function in Weakinson-1bit. Thus, differential trails found on Weakinson-1bit do not take into account properties of these operations and it seems unlikely they could be adapted into a differential trail on Shabal. Therefore, Shabal should be immune against this kind of attacks. 

### **11.4 Fixed Points** 

In all previously considered differential attacks, internal collisions are obtained by considering pairs of messages with the same length. However, internal collisions may be searched for messages of different length. A strategy in such attacks consists in exploiting the existence of fixed points for the message round function. The use of a counter at each message round then avoids the existence of trivial fixed point for Shabal. 

### **11.5 Generic Attacks against Weakinson-1bit** 

When considering weakened versions of Shabal, generic attacks become practical. Thus it becomes possible to find collisions. Such collisions can then be used to derive differential trails. However, it seems highly unlikely that these differential trails can be exploited to derive differential trails on the complete version of Shabal, as explained in Section 11.3.1. In the case of Weakinson-1bit, it is possible to perform an exhaustive search over all possible one-block message differences. In 

126 

particular, we have found that a differential trail which does not cause any difference in register _A_ during the first loop can be found for roughly 56 % of the possible pairs ( _B, M_ ). 

### **11.6 (Second)-preimage Attack against Weakinson-NoFinalUpdateA** 

We now exhibit a preimage attack and a second-preimage attack against Weakinson-NoFinalUpdateA, _i.e.,_ the weakened variant of Shabal without the last update loop in _P_ . On this weakened variant, the attack is faster than the generic attack for _p_ = 1, and has the same complexity as the generic attack for _p_ = 2. The attack mainly relies on the following weakness of Weakinson-NoFinalUpdateA with _p_ = 1: given the outputs of _P_ , the attacker is able to choose a message block _M_ such that part _B_ of ( _PM,C_<sup>_−_1(</sup><sup>_A′, B′_)</sup><sup>_−M_)hasanyprescribedvalue.</sup> 

#### **11.6.1 Attack against Weakinson-NoFinalUpdateA with** _p_ = 1 

We first describe the second-preimage attack. Let _M_ be a _k_ -block message. As we have a counter, we search for another message _M_<sup>_′_</sup> of the same length as _M_ . We split _M_<sup>_′_</sup> into three parts: the first _k_ 1 blocks, 2 intermediate blocks and the last ( _k − k_ 1 _−_ 2) blocks. Let us now randomly choose _N_ 1 vectors ( _M_ 1 _, . . . , Mk_ 1) of _k_ 1 message blocks. We compute _N_ 1 internal states _Sk_ 1 obtained for each of these messages from the initial state. Similarly, we randomly choose _N_ 2 vectors ( _Mk_ 1+3 _, . . . , Mk_ ) of _k −k_ 1 _−_ 2 message blocks. From the final internal state obtained when _M_ is hashed, we compute backwards the internal states _Sk_ 1+2, before the insertion of _Mk_ 1+3 for these _N_ 2 messages. Now, we can use the 2 intermediate blocks _Mk_ 1+1 and _Mk_ 1+2 to find a collision of the 16 words on the _B_ -part of _Sk_ 1+1, which means that finding a collision on the rest of the internal state is enough to find a message which has the same hash value as _M_ . 

Let _β_ be a target value in _{_ 0 _,_ 1 _}_<sup>512</sup> for the _B_ -part of _Sk_ 1+1. For each of the _N_ 1 values of _Sk_ 1 = ( _Ak_ 1 _, Bk_ 1 _, Ck_ 1), we choose _Mk_ 1+1 = _Ck_ 1 _− β_ , implying that the _B_ -part of _Sk_ 1+1, which corresponds to _Ck_ 1 _− Mk_ 1+1, equals _β_ . 

The difference now with Shabal, is that we are able to go backwards. Let _A_ 0 _, . . . , A_ 11 and _B_ 0 _, . . . , B_ 15 be the values in registers _A_ and _B_ of _Sk_ 1+1, and let _A_ 16 _, . . . , A_ 27 and _B_ 16 _, . . . , B_ 31 be the values of _A_ and _B_ after applying _P_ . These outputs are known since they are included in the internal state _Sk_ 1+2. By definition, we have, for any 0 _≤ i ≤_ 15, 

This means that _Bi_ is entirely determined by _Sk_ 1+2, for _i_ from 4 to 15. We can then choose the words _Mk_ 1+2 _,i_ of index _i_ in the message block _Mk_ 1+2 for 4 _≤ i ≤_ 15 so that: 

For finding the values of _Mk_ 1+2 _,i_ , 0 _≤ i ≤_ 3, which lead to the expected values _βi_ , 0 _≤ i ≤_ 3, we now compute the values of _A_ 12, _A_ 13, _A_ 14 and _A_ 15 with the following equation for _i_ from 12 to 15: 

or equivalently, 

Computing _A_ 12 _, . . . , A_ 15 actually involves _A_ 24 _, . . . , A_ 27, some _Bi_ for _i ≥_ 18 and _C_ 9 _, . . . , C_ 12 which are known since they can be deduced from _Sk_ 1+2 and _Mk_ 1+2 _,_ 9 _, . . . , Mk_ 1+2 _,_ 12. Then, we can compute _B_ 0 _, . . . B_ 3 from (11.5), and we choose _Mk_ 1+2 _,_ 0 _, . . . , Mk_ 1+2 _,_ 3 such that 

127 

Finally we have found _N_ 1 prefixes _M_ 1 _, . . . , Mk_ 1 _, Mk_ 1+1 and _N_ 2 suffixes _Mk_ 1+2 _, Mk_ 1+3 _, . . . , Mk_ which lead to two sets of internal states _Sk_ 1+1 whose _B_ -parts are all equal to a given value _β_ . For _N_ 1 = _N_ 2 = 2<sup>32</sup><sup>_×_16+</sup> 2<sup>12</sup> = 2<sup>32</sup><sup>_×_14</sup> , we then find a collision between both sets of internal states. Therefore, a message _M_<sup>_′_</sup> with the same hash value as _M_ has been found within 2<sup>32</sup><sup>_×_14</sup> calls to the message round function, which is better than the generic second-preimage attack for a hash length _ℓh_ = 512. 

A preimage attack can be mounted by the same method. It consists in randomly choosing a final internal state whose part _C_ is (partially) determined by the targeted hash value. Then, the previously described attack enables to find a message which leads to this final internal state. 

#### **11.6.2 Attack against Weakinson-NoFinalUpdateA with** _p_ = 2 

For Weakinson-NoFinalUpdateA with _p_ = 2, the same method can be used. But, for _p_ = 2, we are able to fix only 12 words of the _B_ -part of _Sk_ 1+1. Actually, if we consider the backward computation from all _N_ 2 values for _Sk_ 1+2, the known variables corresponding to _Sk_ 1+2 are now _A_ 32 _, . . . , A_ 43 and _B_ 32 _, . . . , B_ 47. As in the previous case, all _Bi_ , for _i_ from 20 to 31, are completely determined by _Sk_ 1+2 and _Bi_ +16 using (11.5). This does not require any condition on _Mk_ 1+2. Now, we assign _Mk_ 1+2 _,_ 12, _Mk_ 1+2 _,_ 13, _Mk_ 1+2 _,_ 14 and _Mk_ 1+2 _,_ 15 to some fixed arbitrary values, _e.g.,_ 0. Then, we want that the input of the first elementary step of _P_ at round ( _k_ 1 + 2) satisfies 

Several intermediate values of _Ai_ , _Bi_ and _Mi_ can now be deduced by using the following relations: 

Actually, we have the following deduction sequence from the knowledge of _B_ 13 _, B_ 14 _, B_ 15: from (11.7) with 13 _≤ i ≤_ 15, we obtain _A_ 25 _, A_ 26 _, A_ 27. From (11.6) with 25 _≤ i ≤_ 27, we obtain _Mk_ 1+2 _,i_ for 9 _≤ i ≤_ 11. Thus, we obtain the prescribed values for words 9 to 11 of part _B_ of _Sk_ 1+1 if and only if 

Now, the values of _B_ 9 _, B_ 10 _, B_ 11 _, B_ 12 determine _A_ 21 _, A_ 22 _, A_ 23 _, A_ 24 by applying (11.7) with 9 _≤ i ≤_ 12. 

On the other hand, the knowledge of _Mk_ 1+2 _,i_ for 9 _≤ i ≤_ 15 leads to _A_ 28 _, A_ 29 _, A_ 30 _, A_ 31 by applying (11.6) with 28 _≤ i ≤_ 31. Then, _A_ 28 _, A_ 29 _, A_ 30 _, A_ 31 determine _B_ 16 _, B_ 17 _, B_ 18 _, B_ 19 by (11.7) with 16 _≤ i ≤_ 19. 

Now, _A_ 23 _, A_ 24 _, A_ 25 _, A_ 26 _, A_ 27 determine _A_ 12 _, A_ 13 _, A_ 14 _, A_ 15 by (11.6) with 12 _≤ i ≤_ 15, since _Bj_ for _j ≥_ 18 and _Mk_ 1+2 _,j_ for 9 _≤ j ≤_ 15 are known. ¿From _A_ 12 _, A_ 13 _, A_ 14 _, A_ 15 and _B_ 16 _, B_ 17 _, B_ 18 _, B_ 19, we obtain _B_ 0 _, B_ 1 _, B_ 2 _, B_ 3 by applying (11.7) with 0 _≤ i ≤_ 3. Therefore, for 

we obtain the prescribed values for the first 4 words of part _B_ of _Sk_ 1+1. 

Message blocks _Mk_ 1+2 _,i_ for 5 _≤ i ≤_ 8 can be deduced from (11.6) for 21 _≤ i ≤_ 24 since _A_ 21 _, A_ 22 _, A_ 23 _, A_ 24 and _Mk_ 1+2 _,_ 0 _, Mk_ 1+2 _,_ 1 _, Mk_ 1+2 _,_ 2 _, Mk_ 1+2 _,_ 3 are known. The knowledge of _A_ 27, _A_ 28, _Mk_ 1+2 _,_ 0 and _Mk_ 1+2 _,_ 8 determines _A_ 16 by applying (11.6) with _i_ = 16. From _A_ 16 and _B_ 20, we deduce _B_ 4 by (11.7) with _i_ = 4. We finally choose _Mk_ 1+2 _,_ 4 so that 

A message block _Mk_ 1+2 has then been found so that 12 words in part _B_ of _Sk_ 1+1 are equal to the corresponding words in _β_ ( _i.e.,_ all words except words 5 to 8). A (second)-preimage can 

128 

then be found as soon as a collision on the remaining 16 + 4 + _r_ words of the internal state can be found. This requires 2<sup>32</sup><sup>_×_16</sup> calls to the message round function, _i.e.,_ the same complexity as the generic second-preimage attack for a hash length _ℓh_ = 512. 

This attack does not apply to Shabal: the final transformation in _P_ , _i.e.,_ the last update loop, has been chosen in order to eliminate this weakness as explained in Section 4.2.6. 

### **11.7 Generic Attacks Against Merkle-Damg˚ard-Based Hash Functions** 

Most practical hash functions, such as SHA-1 or SHA-2, are iterated hash functions based on the well-known Merkle-Damg˚ard construction. Due to certain structural weaknesses of the MerkleDamg˚ard (MD) construction, MD-based hash functions are vulnerable to some generic attacks such as length-extension attacks [32] or multicollision attacks [25]. In this section, we investigate the applicability of these attacks on Shabal. 

#### **11.7.1 Length-extension Attacks** 

The well-known Merkle-Damg˚ard construction has an undesirable property called _length extension_ . It means that once an attacker has one collision, _i.e.,_ two distinct messages _M_ 1 and _M_ 2 with _|M_ 1 _|_ = _|M_ 2 _|_ = _kℓm_<sup>˙</sup> ( _k >_ 0) such that _H_ ( _M_ 1) = _H_ ( _M_ 2), then for any suffix _M_ it also holds that _H_ ( _M_ 1 _∥M_ ) = _H_ ( _M_ 2 _∥M_ ). 

The message extension attack can be applied to the Shabal hash function only if an internal collision occurs before the final rounds, or in the final rounds but before the second call to the message round function. In the latter case, the internal collision can be transformed into an internal collision before the final rounds by appending the same block message to the two messages leading to an internal collision. Thus, for simplicity reasons, we consider only the case where the internal collision occurs before the three final rounds. Once an adversary has found two distinct messages _M_ 1 and _M_ 2 such that _|M_ 1 _|_ = _|M_ 2 _|_ = _kℓm_<sup>˙</sup> ( _k >_ 0) and Shabal( _M_ 1) = Shabal( _M_ 2), it becomes possible to extend the collision. Indeed for every suffix _M_ , we then have Shabal( _M_ 1 _∥M_ ) = Shabal( _M_ 2 _∥M_ ). Note that it is necessary that _|M_ 1 _|_ = _|M_ 2 _|_ due to the use of a counter in Shabal. As explained in Section 11.2, the complexity for finding an internal collision in Shabal- _ℓh_ (with _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}_ ) is expected to require the order of 2<sup>(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup><sup>_/_2</sup> iterations of the message round function. Thus, the complexity of any length-extension attacks is expected to require at least 2<sup>256</sup> calls to the message round function, independently of _ℓh_ . For more details about recent investigations on these attacks, see [29]. 

#### **11.7.2 Multi-Collisions** 

The multi-collision attack [25] applies to iterative hash functions and exploits the fact that the complexity for finding 2<sup>_u_</sup> messages which have the same hash value corresponds to the complexity for finding _u_ internal collisions (from _u_ prescribed internal states). The 2<sup>_u_</sup> -collision attack against a hash function _H_ actually consists in finding _u_ pairs of messages ( _Mi, Mi_<sup>_′_), 1</sup><sup>_≤i ≤u_, of the same</sup> length _ki_ such that both inserting _Mi_ and inserting _Mi_<sup>_′_fromtheinternalstate</sup><sup>_Si−_1leadtothe</sup> same internal state _Si_ . From such pairs, 2<sup>_u_</sup> messages of length _k_ 1 + _. . ._ + _ku_ can be constructed by concatenating the previous _u_ messages and choosing either _Mi_ or _Mi_<sup>_′_foreach1</sup><sup>_≤i ≤u_.The</sup> complexity for finding a 2<sup>_u_</sup> -multicollision then corresponds to the complexity of finding _u_ internal collisions. 

As explained in Section 11.2, the complexity for finding an internal collision in Shabal- _ℓh_ (with _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}_ ) is expected to require the order of 2<sup>(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup><sup>_/_2</sup> calls to the message round function. Thus, in Shabal- _ℓh_ , _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}_ , the complexity for finding a 2<sup>_u_</sup> -multi-collision is expected to require at least _u ·_ 2<sup>(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup><sup>_/_2</sup> calls to the message round function. 

129 

### **11.8 Slide Attacks** 

Slide attacks apply on hash functions (see _e.g.,_ [24]) but there is no obvious way to transform them into practical attacks. In the hash function setting, a slide property would allow to detect a non-random behavior of the hash function. We have shown in Section 5 that the _P_ -based construction (see Section 2.2) is indifferentiable from a random oracle up to 2<sup>(</sup><sup>_ℓa_+</sup><sup>_ℓm_)</sup><sup>_/_2</sup> _>_ 2<sup>256</sup> calls to the message round function. Since Shabal is a particular instantiation of the _P_ -based construction, there is no slide property due to the operating mode of the hash function Shabal. Thus, there is no obvious slide attack against the Shabal hash function. 

### **11.9 Algebraic Distinguishers and Cube Attacks** 

Algebraic distinguishers consist in computing some coefficients of the algebraic normal form of a Boolean function, and in checking whether these binary coefficients are randomly distributed or not. They rely on the fact that the coefficient of a monomial of degree _d_ in the algebraic normal form corresponds to the sum modulo 2 of the values of the function when the input varies in a _d_ -dimensional linear space. Therefore, a distinguishing attack can be mounted if the attacker has access to such 2<sup>_d_</sup> evaluations of a Boolean function related to the considered primitive. This basic principle has been used for a long time for block ciphers in the so-called higher-order differential attacks. It has been introduced by Saarinen [39] for chosen-IV attacks against stream ciphers and been developed in [21]. Finally, Fischer, Khazaei and Meier [22] and Dinur and Shamir [20] have recently shown how such key-recovery attacks can be mounted based on the same technique. Moreover, [20] exhibits an algorithm for finding the monomials which must be considered in the attack, even if the algebraic normal form of the studied Boolean function is not known to the attacker. 

Such a distinguishing attack may apply in the context of hash functions. For _n_ -bit messages, each bit of the hash value can be seen as a Boolean function ( _m_ 1 _, . . . , mn_ ) _�→ h_ ( _m_ 1 _, . . . , mn_ ) in _n_ variables. It is clearly suitable that this function behaves like a random function. This means that, for any subset of the input bits, _I ∈{_ 1 _, . . . , n}_ , the superpoly of _I_ in _h_ behaves like a random polynomial, where the superpoly of of _I_ in _h_ corresponds to the ( _n −|I|_ )-variable function 

Thus, the fact that _h_ has a high degree and is not sparse is a priori sufficient to resist such attacks. The three final rounds in Shabal are expected to ensure that each coordinate of final internal state is a random-looking polynomial of the message bits (see Section 4.4 for some details on the degree). 

### **11.10 Attacks Taking Advantage of The Chosen Constants** 

To prevent the existence of possible “trapdoors”, the provenance of constants or tables used in Shabal have been justified. There is no table used in Shabal. The only constants specified in Shabal- _ℓh_ where _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 384 _,_ 512 _}_ , are the initial values IV _ℓh_ of the state ( _A, B, C_ ). Rationale of this choice is given in Section 4.5. 

### **11.11 Attack on HMAC-Shabal** 

At Crypto 2007, Fouque _et al._ [23] proposed a new attack to take into account differential collision paths in some hash functions such as MD4 and MD5 to recover some key bits of HMAC-MD4. The idea is to find differential collision paths that depend on bits of the IV. This kind of attack has been extended to MD4 at Eurocrypt 2008 by Wang _et al._ in [40]. These attacks use the fact that 

130 

differential paths with high probability exist and are easy to compute. This is the case for MD4 and the pseudo-collision on MD5 exhibited by den Boer and Bosselaers [19]. These attacks can be applied to HMAC-Shabal if it is possible to find such differential paths. Moreover, to recover the outer key of HMAC, such paths need to be constrained to use only one message block with constrained variation since the last call to the hash function has many zeroes. Finally, it is worth saying that distinguishing attacks are also possible using differential paths. But all these attacks rely on the fact that such differential paths can be easily found. 

##### **Pseudo-Random Function.** 

It is well-known that a good Pseudo-Random Function allows to construct a secure MAC algorithm. For instance, Bellare at Crypto 2006, in [2], proved that if the compression function of the underlying hash function behaves as a good PRF, and that a related PRF (by inverting the message and the key space) is secure under a specific related-key attack, then HMAC is a good MAC. Then, if the compression function of Shabal is a good PRF, then the HMAC-Shabal will be a good MAC. Finally, since no preservation property for PRF has been provided for the mode of operation of Shabal here, we cannot argue that Shabal( _k||M_ ) is a secure MAC if the compression function of Shabal is a PRF. 

131 

## **Part 2.B.6** 

**A Statement that Lists and Describes the Advantages and Limitations of the Algorithm** 

132 

## **Chapter 12** 

# **Advantages and Disadvantages of Shabal** 

#### **Contents** 

|**12.1 Simplicity of Design . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133**|
|---|
|**12.2 Provable Security**<br>**. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 133**|
|**12.3 Software Implementation Considerations . . . . . . . . . . . . . . . . 134**|
|12.3.1 Word Size . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134|
|12.3.2 Very Few Requested Instructions to Code Shabal . . . . . . . . . . . . . 134|
|12.3.3 No S-Box . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 134|
|12.3.4 Speed Measures. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 135|
|12.3.5 Code Size . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 136|

In this chapter, we try to present a first comparison of Shabal with other hash functions. Our comparison is made by exhibiting advantages and disadvantages of Shabal, as well as by gathering measures on some implementations of Shabal and other hash functions. 

### **12.1 Simplicity of Design** 

One aim of Shabal is to be secure while keeping a simple design. This simplifies both study and implementation. Each element of Shabal was carefully weighted with regards to security and implementation cost; whenever possible, we favored the simplest choice. 

The final result is that our function — or at least, our mode — is really simple to describe. The pictures of Figures 2.1, 2.2 and 2.3 give an overview of the design, and the only non-natural part of Shabal is certainly the permutation description which is described in Section 2.3.2 (see also Figure 2.4). The rest of the function is relatively easy to understand and to remember. 

#### **12.3.3 No S-Box** 

Shabal uses no S-Box. S-Boxes are a popular design element in cryptographic algorithms because they can be finely tuned to offer the optimal algebraic properties to defeat various types of attacks. However, S-Boxes are expensive to implement, not only in dedicated hardware, but also in software: S-Box access is a memory read by address, which exercises the caches and has a high latency, typically higher than numerical operations on modern processors. Moreover, small S-Boxes can only handle a few bits at a time, thus processing a full 32-bit word with S-Boxes will require several accesses; wider S-Boxes imply prohibitive costs in terms of code size. Besides, S-Box access works over the data cache in a typical CPU, and the data cache is a scarce resource (especially when we are processing huge amounts of data, which is why hash function performance matters in the first place). 

134 

In our design, the nonlinear functions _U_ and _V_ take the role of S-Boxes, albeit with weaker algebraic properties, but they are much less expensive to implement on most platforms. 

#### **12.3.4 Speed Measures** 

In this section, we give a comparison of Shabal with several other hash functions, on the architectures detailed in Chapter 8. This comparison is given in two tables, Table 12.1 and 12.2. In the tables, Shabal refers to implementations for all lengths _ℓh ∈{_ 192 _,_ 224 _,_ 256 _,_ 284 _,_ 512 _}_ , as the execution hardly depends on the output length. MD5 and Sha-1 times are just given for comparison, as these functions are known to be broken, respectively in practice and in theory. 

||**Ban**|**dwidth (M**|**B/s), for l**|**ong messa**|**ges**|
|---|---|---|---|---|---|
|**Platform**|Shabal|MD5|Sha-1|Sha-256|Sha-512|
|Xeon, 64-bit|194.52|412.98|318.62|143.55|191.06|
|Xeon, 32-bit|147.90|419.43|232.41|127.22|45.19|
|Athlon64, 64-bit|140.91|336.60|239.67|115.21|151.23|
|Athlon64, 32-bit|103.64|338.72|174.31|108.68|32.42|
|C7|67.79|139.09|63.61|29.18|11.53|
|Broadcom MiPS|6.24|10.20|6.15|2.90|1.50|

Table 12.1: Shabal performance compared with other hash functions (1) 

||**Ba**|**ndwidth (MB/s)**|**, for long messag**|**es**|
|---|---|---|---|---|
|**Platform**|Shabal|Whirlpool|RadioGat´un[32]|RadioGat´un[64]|
|Xeon, 64-bit|194.52|38.90|258.11|506.48|
|Xeon, 32-bit|147.90|26.42|181.99|55.92|
|Athlon64, 64-bit|140.91|21.79|225.58|443.69|
|Athlon64, 32-bit|103.64|15.68|143.55|126.03|
|C7|67.79|6.45|75.40|52.22|
|Broadcom MiPS|6.24|0.15|1.36|0.55|

Table 12.2: Shabal performance compared with other hash functions (2) 

The hash function implementations were extracted from the open-source `sphlib` library. Most notably, all these functions (including the Shabal optimized code) were implemented with the same optimization goals and efforts, with the same programming tools, by the same programmer. As such, relative performance of two functions on the same platform should be viewed as intrinsic to the functions themselves. Note that on the Broadcom MiPS platform, a specifically optimized Sha-256 implementation was used, with less loop unrolling; if the exact same C code was used on other platforms, the Sha-256 speed would drop to 1.76 MB/s. 

In the tables, one can see the effect of our choice of sticking to 32-bit words: the performance hit is minimal when switching from a 64-bit platform to a 32-bit platform (there is a performance hit because the 64-bit instruction set on x86 CPU offers more registers than the 32-bit instruction set). Conversely, functions which rely on 64-bit operations (Sha-512, Whirlpool and RadioGat´un[64]) greatly suffer from being run on a 32-bit only platform. 

Our goal was to be as efficient as possible on all types of platforms; this goal is mostly achieved. Indeed, we can compute the ratio of the fastest bandwidth divided by the slowest bandwidth on our set of platforms; this ratio may be viewed as a crude measure for the portability, performance-wise, of the design. We get the following figures: 

- on high-end platforms only (all the x86-compatible systems): 2.9 for Shabal, 4.9 for Sha256, 17.3 for Sha-512, 6.5 for Whirlpool, 3.4 for RadioGat´un[32] and 9.7 for RadioGat´un[64]; 

135 

- on all considered platforms (including the Broadcom): 31.2 for Shabal, 49.5 for Sha-256, 127 for Sha-512, 259 for Whirlpool, 190 for RadioGat´un[32] and 920 for RadioGat´un[64]. 

That Shabal exhibits the smallest ratios underlines our efforts for designs which are efficient on a wide range of systems. 

From these measures, comparing Shabal with the five non-broken hash functions, we see that Shabal is third on Xeon (64-bit), fourth on Athlon64, second on Xeon 32-bit and C7, and first on the Broadcom MiPS. In terms of performance portability, Shabal wins. We would like to underline that even if the security proof (see Chapter 5) influenced the design of Shabal, possibly at the expense of raw performance, the achieved bandwidth remains decent, and is actually quite good on some low-end platforms, such as the Broadcom MiPS, which are industrially significant (hash function performance matters much more on limited systems which perform network-based cryptography all day long than on high-end desktop systems where I/O bandwidth is more limited than computing power). 

#### **12.3.5 Code Size** 

Code size is a critical part of the performance of a hash function and it is rarely well measured by benchmarks. Benchmarks (such as the one we presented in the previous section) run the function “alone”, with the full processor caches at its disposal, which is not very representative of actual usage. Yet, on some platforms, the dramatic effect of code size can even be shown with a benchmark. In our previous example, we see that Whirlpool, RadioGat´un[32] and RadioGat´un[64] are much slower than expected on the Boradcom MiPS platform (when compared to, for instance, Sha-512). This is because their code size exceeds the limited L1 code cache on that architecture (8 kB), implying expensive cache misses for each message block. 

We measured the code size of the implementations of the functions on our three target architecture types. Tables 12.3, 12.4 and 12.5 list the code and data sizes. The “code” column measures the total code size for the complete implementation; the “update” column contains only those parts of the code which are on the execution path when hashing streamed data ( _i.e.,_ without initialization and finalization). The “state” is the size of the state structure which is maintained for a given hash computation; this is mutable data. The “data” column contains the size of the constant data tables which are accessed during main processing: these tables are not modified but they contribute to the data L1 cache pressure (among our test functions, only Whirlpool uses such tables; precomputed IV are not included since they are used only during initialization of the hash computation). 

|||**Code and d**|**ata size**||
|---|---|---|---|---|
|**Function**|code|update|state|data|
|MD5|2816|2128|88|-|
|Sha-1|5348|4592|92|-|
|Sha-256|10240|9728|104|-|
|Sha-512|1840|1696|200|-|
|Whirlpool|3840|3472|136|16464|
|RadioGat´un[32]|41072|18336|388|-|
|RadioGat´un[64]|41840|20368|776|-|
|Shabal|21456|7360|248|-|

Table 12.3: Code and data cache consumption of various hash functions, on x86 64-bit architecture. 

The internal mutable state size of Shabal is not very big for a function which offers a 512-bit output; it can still be a limitation on some constrained environments, especially smart cards, where RAM is a very scarce resource (contrary to ROM, which may be used for static tables but not for the function running state). Yet, on that specific subject, Shabal fares much better than RadioGat´un, and not much worse than Sha-512. 

136 

|||**Code and d**|**ata size**||
|---|---|---|---|---|
|**Function**|code|update|state|data|
|MD5|2400|2096|88|-|
|Sha-1|6960|6640|92|-|
|Sha-256|14352|13968|104|-|
|Sha-512|6000|5440|200|-|
|Whirlpool|7536|6928|136|16464|
|RadioGat´un[32]|49120|23088|388|-|
|RadioGat´un[64]|106944|54880|776|-|
|Shabal|24048|8080|248|-|

Table 12.4: Code and data cache consumption of various hash functions, on x86 32-bit architecture. 

|||**Code and d**|**ata size**||
|---|---|---|---|---|
|**Function**|code|update|state|data|
|MD5|4192|3616|88|-|
|Sha-1|8132|7500|92|-|
|Sha-256|8896|8232|104|-|
|Sha-512|7060|6268|200|-|
|Whirlpool|15004|14292|136|16464|
|RadioGat´un[32]|41476|21692|388|-|
|RadioGat´un[64]|109052|55004|776|-|
|Shabal|21036|7852|248|-|

Table 12.5: Code and data cache consumption of various hash functions, on MiPS architecture. 

137 

# **Appendixes** 

144 

## **Appendix A** 

# **Detailed Test Patterns** 

#### **Contents** 

|**B.1**|**Intermediate States for Shabal-192 **|**(Message A) . . . . . . . . . . . . 154**|
|---|---|---|
|**B.2**|**Intermediate States for Shabal-192 **|**(Message B) . . . . . . . . . . . . 169**|
|**B.3**|**Intermediate States for Shabal-224 **|**(Message A) . . . . . . . . . . . . 183**|
|**B.4**|**Intermediate States for Shabal-224 **|**(Message B) . . . . . . . . . . . . 198**|
|**B.5**|**Intermediate States for Shabal-256 **|**(Message A) . . . . . . . . . . . . 212**|
|**B.6**|**Intermediate States for Shabal-256 **|**(Message B) . . . . . . . . . . . . 227**|
|**B.7**|**Intermediate States for Shabal-384 **|**(Message A) . . . . . . . . . . . . 242**|
|**B.8**|**Intermediate States for Shabal-384 **|**(Message B) . . . . . . . . . . . . 256**|
|**B.9**|**Intermediate States for Shabal-512 **|**(Message A) . . . . . . . . . . . . 271**|
|**B.10 **|**Intermediate States for Shabal-512 **|**(Message B) . . . . . . . . . . . . 285**|

Please consider the environment before printing this chapter. 

### **B.1 Intermediate States for Shabal-192 (Message A)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
C:0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
```

```
W:FFFFFFFFFFFFFFFF
```

```
blocknumber=-1:messageblock
```

- `M : 000000C0 000000C1 000000C2 000000C3 000000C4 000000C5 000000C6 000000C7 000000C8 000000C9 000000CA 000000CB 000000CC 000000CD 000000CE 000000CF` 

```
blocknumber=-1:addMtoB
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

154 

- `B : 000000C0 000000C1 000000C2 000000C3 000000C4 000000C5 000000C6 000000C7 000000C8 000000C9 000000CA 000000CB 000000CC 000000CD 000000CE 000000CF` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

###### `block number = -1 : xor counter W into A` 

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 000000C0 000000C1 000000C2 000000C3 000000C4 000000C5 000000C6 000000C7 000000C8 000000C9 000000CA 000000CB 000000CC 000000CD 000000CE 000000CF` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 01800000 01820000 01840000 01860000 01880000 018A0000 018C0000 018E0000 01900000 01920000 01940000 01960000 01980000 019A0000 019C0000 019E0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=0)
```

- `A : F78A4200 10145AFD AE842D9A 7DA2B6D1 E125063B 87057989 D33D3495 15A94983 24F95064 DD75BF25 2CE50A5D 109E76BE` 

- `B : 028800C2 F8D8F4B6 29CC61C2 DCBC40CD 1DCAF9C4 7BEE8676 2FDACB6A E94AB67C D826AF9B 21AE40DA D032F5A2 EC4D8941 0B45BDFF ECDFA502 5243D265 8161492E` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : B11AE006 5117AAEA F864E13E 8395DEC5 7473DED3 F4F3C55C EE1065D0 0FBCE63D 5D489898 3D28BAC9 DF45C1AD C5245735` 

- `B : 6E986FA3 0EF5A5BE CF36EA1B A553B940 992294EF 350A49DA 7F0FA886 E84EC433 FEA840CE EDB4D4A1 A7FEF584 A4F133B9 9D075AD2 D2B370A6 B5683EE5 F2818B9F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

155 

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:subtractMfromC
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `C : FFFFFF40 FFFFFF3F FFFFFF3E FFFFFF3D FFFFFF3C FFFFFF3B FFFFFF3A FFFFFF39 FFFFFF38 FFFFFF37 FFFFFF36 FFFFFF35 FFFFFF34 FFFFFF33 FFFFFF32 FFFFFF31` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : FFFFFF40 FFFFFF3F FFFFFF3E FFFFFF3D FFFFFF3C FFFFFF3B FFFFFF3A FFFFFF39 FFFFFF38 FFFFFF37 FFFFFF36 FFFFFF35 FFFFFF34 FFFFFF33 FFFFFF32 FFFFFF31` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : FFFFFF40 FFFFFF3F FFFFFF3E FFFFFF3D FFFFFF3C FFFFFF3B FFFFFF3A FFFFFF39 FFFFFF38 FFFFFF37 FFFFFF36 FFFFFF35 FFFFFF34 FFFFFF33 FFFFFF32 FFFFFF31` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

156 

```
blocknumber=0:messageblock
```

- `M : 000000D0 000000D1 000000D2 000000D3 000000D4 000000D5 000000D6 000000D7 000000D8 000000D9 000000DA 000000DB 000000DC 000000DD 000000DE 000000DF` 

```
blocknumber=0:addMtoB
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:xorcounterWintoA
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-rotateB
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=0)
```

- `A : 40EDD726 1A8754BC 7AF69209 DD22532D 04BFEA68 4E68A17B 6E3AE516 89451CE8 237E61BE 50533EB1 77550A53 4EE347AA` 

- `B : 20C6148A C0A0482A 20FEE685 BD139D7F FB001597 B1D75E84 91851AE9 76FAE317 DCC19E41 AFECC14E 88EAF5AC B15CB855 BF5228D9 E538AB43 85496DF6 229DACD2` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : DCB0D1FF 9807FEF5 55FCAED1 DDFCB641 2546AE31 EFC27512 31D29DFA 9459E7A6 9E7C5606 FC6CB0E4 5699952C 8FDD2936` 

157 

- `B : 5EA811AF 428F0F99 F1F49AC3 7C94CC73 978382D6 603DF212 8A6C5F00 9DD710E7 9ACC1283 38218397 BBD6BA77 40BA3915 A41D007D DA4CDC6A C4BFB9E8 2E9D41FD` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

```
W:0000000000000000
```

```
blocknumber=0:permutation(j=2)
```

- `A : A26F4FDE 24426C48 949686DD 723E1870 D02F6DE4 7F2B95C6 80DE631A DADF6026 ABCC94F0 E7106561 2495F432 6F985A6C` 

- `B : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-addCtoA
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

158 

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=1:addMtoB
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:xorcounterWintoA
```

- `A : FD749ED5 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : FD749ED5 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 7588B179 411DD88F 67655DD2 9049BF97 90094F28 7B617ECB 8A04B53A 35EEB32F 4A9D8B9D 02A096D7 32122DCE 4632FAC6 E741260A C7A3E698 296995F2 C259FBAC` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=0)
```

- `A : 4938D355 5288CA69 C3588F79 A6C6D366 AE98E42B 3AC0111E FBC3BCCF 3E91F2FB 716B0E50 99F3F6A7 6EE059FF BB628852` 

- `B : F2A96EA1 F4E8814E 1608C053 0ECBF7E8 71758585 33FD1377 10352945 AAB36B5A` 

159 

   - `1BAFE695 634D24F6 F53BFD9C C8F88221 784560BF 2230F8A7 6E745B62 DD8ADBC0` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : 0C9CDDB2 AE1600E6 3EDE3006 940E8573 C3090C7B C3D810AC 12683C17 F034D340 D5985BF2 7954156D 527D532E 25F0ED34` 

- `B : B7270521 E3A38111 57CE7E2F 39B038AF C88CAF07 E151CC7C 8DE8FE5B 8F69C47E C43CEF67 9773B6F5 2B5634C0 FA007ECF CC7C32FA 78461E1D 317F752C B4DE9B3E` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : 89F5EF16 949BFB86 B4F5B8A9 13F6118A F9C835AD CBDD8F73 840DC321 3EFCE7E4 CC7B611A 06F8AF7A 67210CF8 E30A4E95` 

- `B : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : 7A9B88CD 8492257E 07217DFC 87235D0F FC88A7B1 BA130493 1A5AD340 68A1A357 A6339AA8 AFE28816 1FF513ED BD5E75DE` 

- `B : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : 7A9B88CD 8492257E 07217DFC 87235D0F FC88A7B1 BA130493 1A5AD340 68A1A357 A6339AA8 AFE28816 1FF513ED BD5E75DE` 

- `B : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : 7A9B88CD 8492257E 07217DFC 87235D0F FC88A7B1 BA130493 1A5AD340 68A1A357` 

160 

```
A6339AA8AFE288161FF513EDBD5E75DE
```

- `B : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : 7A9B88CD 8492257E 07217DFC 87235D0F FC88A7B1 BA130493 1A5AD340 68A1A357 A6339AA8 AFE28816 1FF513ED BD5E75DE` 

- `B : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 00000080 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : 7A9B88CD 8492257E 07217DFC 87235D0F FC88A7B1 BA130493 1A5AD340 68A1A357 A6339AA8 AFE28816 1FF513ED BD5E75DE` 

- `B : 615508F8 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:xorcounterWintoA
```

- `A : 7A9B88CF 8492257E 07217DFC 87235D0F FC88A7B1 BA130493 1A5AD340 68A1A357 A6339AA8 AFE28816 1FF513ED BD5E75DE` 

- `B : 615508F8 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : 7A9B88CF 8492257E 07217DFC 87235D0F FC88A7B1 BA130493 1A5AD340 68A1A357 A6339AA8 AFE28816 1FF513ED BD5E75DE` 

- `B : 11F0C2AA 56EB13DE 188D42CC 0AB6FDE7 6B18E52F EF26378C 8E46FF63 8C816CDF 6E383491 DA2FE12E D0141119 DBE748A9 D7E83812 449758EC F038A42A 4CD39ABA` 

161 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : C943C410 4B9134EF 31EFBB0F AC63BE5F 30AA2521 16A218E4 E80EABE4 0B834617 F5341AC3 D0B751D5 16B0FA0E 8F3DF915` 

- `B : BFCBED60 5599C245 5710D79A 04C5B506 19641080 37118802 0B7CAADC ED7E6057 D6BB8C1E 9B176C77 496727C2 C70C97B9 996C4BCA 3D407AC8 2E610CA5 CA3B74D4` 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=1)
```

- `A : 20491CA1 EB28B829 8E525199 B896DDA0 A7D79EBC 223E4E9D 210ADBB1 1C599CC5 682D693A 1F3CFE7A E90C388B D8C6DAA5` 

- `B : 820A468E 2D6D029B 82E25781 65698F76 A51AB7C5 8EE01181 000A92CC FDC5E5F5 72C1FB63 22F99F39 E363E1E2 C9700D2C 6AF0F6D6 A74144F2 82373D04 77D08A93` 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : 33E0DA7D EA775049 5B8219CC CEF0326D 0CE5C43A 9DF42A97 DC70AC5F A729892C 3A5C06D9 FE6F5621 51A2662D 00C48A61` 

- `B : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : A47D2606 E1449080 0C673FB4 9FE96A68 3B5890C7 7792845B 9E8F82EF AB60FD26 288A31D3 1F4DB4B4 1FBA8CD3 791EB4FF` 

- `B : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `C : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : A47D2606 E1449080 0C673FB4 9FE96A68 3B5890C7 7792845B 9E8F82EF AB60FD26 288A31D3 1F4DB4B4 1FBA8CD3 791EB4FF` 

162 

- `B : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `C : 643CF5C1 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : A47D2606 E1449080 0C673FB4 9FE96A68 3B5890C7 7792845B 9E8F82EF AB60FD26 288A31D3 1F4DB4B4 1FBA8CD3 791EB4FF` 

- `B : 643CF5C1 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `C : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

- `n0_final = 0 : add M to B` 

- `A : A47D2606 E1449080 0C673FB4 9FE96A68 3B5890C7 7792845B 9E8F82EF AB60FD26 288A31D3 1F4DB4B4 1FBA8CD3 791EB4FF` 

- `B : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `C : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

- `n0_final = 0 : xor counter W into A` 

- `A : A47D2604 E1449080 0C673FB4 9FE96A68 3B5890C7 7792845B 9E8F82EF AB60FD26 288A31D3 1F4DB4B4 1FBA8CD3 791EB4FF` 

- `B : 643CF641 FD921CA9 85FD62BB C64FDEEE E7134EE6 A9C79C80 50DBBBE1 F2DA6688 8E4E149D 1AC51D67 2D5E555E 3503E584 AB7CFB10 098B6CBF FA20195F 75488717` 

- `C : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : A47D2604 E1449080 0C673FB4 9FE96A68 3B5890C7 7792845B 9E8F82EF AB60FD26 288A31D3 1F4DB4B4 1FBA8CD3 791EB4FF` 

- `B : EC82C879 3953FB24 C5770BFA BDDD8C9F 9DCDCE26 3901538F 77C2A1B7 CD11E5B4 293B1C9C 3ACE358A AABC5ABC CB086A07 F62156F9 D97E1316 32BFF440 0E2EEA91` 

- `C : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

163 

- `A : 6F790FAB A4000660 457B3F54 96B16EA7 79837F24 938A78F3 D5933692 6CA2E17B 5E570DE2 8C5E25B4 E031024C 50192595` 

- `B : 9446B9F6 055D9F72 4B9918A7 BE11F2DC BDE71C96 1E772012 C5E98A03 097ED5ED F3DECB25 063DB15F 4AB648CA 39F60E65 7CC45DA7 E903DFB2 DFFB282B 7513447A` 

- `C : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : 1C290251 4185CEBF BE63FCF7 5123632C CE9E9872 8731B9CB 39B5BAD2 61418961 B1A3A821 F0B5BB96 2E98F6F6 21871755` 

- `B : CF4DBDA1 87AAA701 B9D331B5 7862DE48 35926EF3 33A4044D 5AB41D0E CC854370 046B6BE5 B20153FE D4F0929C DD308019 C8E9DCC3 AAC9F951 79BC157A 7498FE6A` 

- `C : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

- `A : F16BE812 B54B9216 05295BC3 55F0AA85 918A9119 3A83095E B944B03B A257427F C9469D61 5093FAE2 EFCB8BBF 94F698D6` 

- `B : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `C : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : 5402B016 26ABFA79 9BE7A217 6AF8A837 F46EF30C B23B2A3A 28E9C16E F273ECBB E5C70B26 FD9A2678 6F1F23C9 C8DBD0C1` 

- `B : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `C : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

```
n0_final=0:subtractMfromC
```

- `A : 5402B016 26ABFA79 9BE7A217 6AF8A837 F46EF30C B23B2A3A 28E9C16E F273ECBB E5C70B26 FD9A2678 6F1F23C9 C8DBD0C1` 

- `B : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `C : DAF40950 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `W : 00000002 00000000` 

164 

```
n0_final=0:swapBwithC
```

- `A : 5402B016 26ABFA79 9BE7A217 6AF8A837 F46EF30C B23B2A3A 28E9C16E F273ECBB E5C70B26 FD9A2678 6F1F23C9 C8DBD0C1` 

- `B : DAF40950 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `C : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

- `A : 5402B016 26ABFA79 9BE7A217 6AF8A837 F46EF30C B23B2A3A 28E9C16E F273ECBB E5C70B26 FD9A2678 6F1F23C9 C8DBD0C1` 

- `B : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `C : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `W : 00000002 00000000` 

- `n0_final = 1 : xor counter W into A` 

- `A : 5402B014 26ABFA79 9BE7A217 6AF8A837 F46EF30C B23B2A3A 28E9C16E F273ECBB E5C70B26 FD9A2678 6F1F23C9 C8DBD0C1` 

- `B : DAF409D0 3F639964 C66B562C 87C5FAC2 862A4A09 08488CB5 A468C3AB CA840679 1699CD03 27F8EB1A E5489065 CA366C8A 1042148A 4F12203B AA33E3DB 109A60B8` 

- `C : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

- `A : 5402B014 26ABFA79 9BE7A217 6AF8A837 F46EF30C B23B2A3A 28E9C16E F273ECBB E5C70B26 FD9A2678 6F1F23C9 C8DBD0C1` 

- `B : 13A1B5E8 32C87EC7 AC598CD6 F5850F8B 94130C54 196A1091 875748D1 0CF39508 9A062D33 D6344FF1 20CBCA91 D915946C 29142084 40769E24 C7B75467 C1702134` 

- `C : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : B2B7AC93 3280F0EF B7D1A386 134AD19A DFA84728 2E1F3273 F925D5FE 3BC0A039 09CA6539 80F200DF 72A143BF 9869ED12` 

- `B : F93A70E0 00D3F200 80E2EB89 F43A3B69 0871A07E E334ECAE 0874BBA2 DDD875D6 C239C0A1 D36560C3 CCC92962 D5BD3A34 1F601264 4D923358 C740F4B6 6E556C0C` 

- `C : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

165 

###### `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

- `A : 0E22DD0D 5A7ED8B2 555E9A44 68F49ABD 6F4B6A35 7BF14653 269337DB 6CB49E0E 18CB4BF6 A18475A2 6D809BBD 99766B2F` 

- `B : 8C380710 D2D21616 38F39361 5F2FBD22 F7D7F4F5 98125300 82961306 DD397F7D 75AEA3B1 034BE6CA 3333377E 3C71112B AE74B102 1F2ADF1C 57ED2149 4FE1B9E9` 

- `C : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 2)` 

- `A : B18E580E 6100E1AB B3089D3F 953C78F7 69DD127D 7E11BDC3 06E6CF36 CD828F57 03E5CBA8 A40C93A9 622FA53C 8FC52BE0` 

- `B : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `C : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - add C to A` 

- `A : AA38E80B A994046A C3229CBC 5AD13E73 ADC3B862 85DDBE95 BD7F2851 9F25611C AD5D9343 17CBF1F9 2CAA53C9 B22A93B1` 

- `B : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `C : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `W : 00000002 00000000` 

```
n0_final=1:subtractMfromC
```

- `A : AA38E80B A994046A C3229CBC 5AD13E73 ADC3B862 85DDBE95 BD7F2851 9F25611C AD5D9343 17CBF1F9 2CAA53C9 B22A93B1` 

- `B : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `C : 3B777D1B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `W : 00000002 00000000` 

- `n0_final = 1 : swap B with C` 

- `A : AA38E80B A994046A C3229CBC 5AD13E73 ADC3B862 85DDBE95 BD7F2851 9F25611C AD5D9343 17CBF1F9 2CAA53C9 B22A93B1` 

- `B : 3B777D1B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

166 

- `C : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : add M to B` 

- `A : AA38E80B A994046A C3229CBC 5AD13E73 ADC3B862 85DDBE95 BD7F2851 9F25611C AD5D9343 17CBF1F9 2CAA53C9 B22A93B1` 

- `B : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `C : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : xor counter W into A` 

- `A : AA38E809 A994046A C3229CBC 5AD13E73 ADC3B862 85DDBE95 BD7F2851 9F25611C AD5D9343 17CBF1F9 2CAA53C9 B22A93B1` 

- `B : 3B777D9B E71DA24C 9289C8A8 8EA8364D 65B0CA0B 2DFC6573 4FBE9E20 3305D39B 66A3B92C A17E515C EF5A6AFD E7C9BDB3 A76ADB19 FAFFF7BE E34C5EB4 82389BFD` 

- `C : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - rotate B` 

- `A : AA38E809 A994046A C3229CBC 5AD13E73 ADC3B862 85DDBE95 BD7F2851 9F25611C AD5D9343 17CBF1F9 2CAA53C9 B22A93B1` 

- `B : FB3676EE 4499CE3B 91512513 6C9B1D50 9416CB61 CAE65BF8 3C409F7D A736660B 7258CD47 A2B942FC D5FBDEB4 7B67CF93 B6334ED5 EF7DF5FF BD69C698 37FB0471` 

- `C : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 0)` 

- `A : EB3858E3 3571FF05 07F3E3A5 F01ACEC6 7C2B8559 782CE3DD 553117F5 DC8BA789 EC309F7C 79D58C9A 4E25C57F 79B079C2` 

- `B : 9725D95D 0BA369BF D9D4169F 615F3855 ABF9EC65 121FABD3 D24FD6F0 6D189461 F77EFA0D C358F69C 1A2D87E9 7080191B 78A13AB7 1475EB05 82DF916B 601339DB` 

- `C : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : 5C8DD649 1612AD22 789B27A7 2AB3CED6 46180EC5 FE6C7E91 A5AC461A 87B17270 CCE4F762 85DF8D82 3DC305DA F80F92C3` 

167 

- `B : D421E125 EB0EF9F6 B70F6574 FAFC24D3 64E8D056 5E1F25DB 66A357C4 DDC145FE 4D8FDDAD 6F5CBFE4 B33FD78A 344C031F 48A58454 29785764 5FEC9B32 B868FE39` 

- `C : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : 3F7A1D06 AEE6E8BA 33DFA929 684A2EF8 2D4ABF45 6CDA81F1 52EE20E5 592A3656 BC0F4857 A15C35CC F42A4EA9 825D3AC4` 

- `B : F91EEE5E 99DCC78C 82F72599 8CACD775 09544255 ED275CF3 0166F95E 2C375AFA 49AAFBE0 4D9C01C6 CB6E700F CE4DCF97 D2BBBF00 0C5364FB B40C8732 0D733948` 

- `C : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - add C to A` 

- `A : A38C0C63 17C2CAE8 3248572C 1C89CAD5 176ED597 B242B8AD 73298C22 7ADF1817 00D909DA 61AD8518 90266914 9DC1F617` 

- `B : F91EEE5E 99DCC78C 82F72599 8CACD775 09544255 ED275CF3 0166F95E 2C375AFA 49AAFBE0 4D9C01C6 CB6E700F CE4DCF97 D2BBBF00 0C5364FB B40C8732 0D733948` 

- `C : 260A3DC2 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : A38C0C63 17C2CAE8 3248572C 1C89CAD5 176ED597 B242B8AD 73298C22 7ADF1817 00D909DA 61AD8518 90266914 9DC1F617` 

- `B : F91EEE5E 99DCC78C 82F72599 8CACD775 09544255 ED275CF3 0166F95E 2C375AFA 49AAFBE0 4D9C01C6 CB6E700F CE4DCF97 D2BBBF00 0C5364FB B40C8732 0D733948` 

- `C : 260A3D42 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : A38C0C63 17C2CAE8 3248572C 1C89CAD5 176ED597 B242B8AD 73298C22 7ADF1817 00D909DA 61AD8518 90266914 9DC1F617` 

- `B : 260A3D42 E9E62340 385A3EBF 2978F492 A1DE4E1A AEDBB855 49DB44CD D0B179F3 7D7FAAE0 87798FA8 9F7F5E35 4A9F52FE A0F35652 65A6D26E 320A1851 EFF9A7CD` 

- `C : F91EEE5E 99DCC78C 82F72599 8CACD775 09544255 ED275CF3 0166F95E 2C375AFA 49AAFBE0 4D9C01C6 CB6E700F CE4DCF97 D2BBBF00 0C5364FB B40C8732 0D733948` 

- `W : 00000002 00000000` 

```
Hashvalue(wordarray):
```

168 

```
H:CB6E700FCE4DCF97D2BBBF000C5364FBB40C87320D733948
```

```
Hashvalue(bytearray):
```

- `H : 0F 70 6E CB 97 CF 4D CE 00 BF BB D2 FB 64 53 0C 32 87 0C B4 48 39 73 0D` 

### **B.2 Intermediate States for Shabal-192 (Message B)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:messageblock
```

- `M : 000000C0 000000C1 000000C2 000000C3 000000C4 000000C5 000000C6 000000C7 000000C8 000000C9 000000CA 000000CB 000000CC 000000CD 000000CE 000000CF` 

```
blocknumber=-1:addMtoB
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 000000C0 000000C1 000000C2 000000C3 000000C4 000000C5 000000C6 000000C7 000000C8 000000C9 000000CA 000000CB 000000CC 000000CD 000000CE 000000CF` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

   - `00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:xorcounterWintoA
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 000000C0 000000C1 000000C2 000000C3 000000C4 000000C5 000000C6 000000C7 000000C8 000000C9 000000CA 000000CB 000000CC 000000CD 000000CE 000000CF` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

169 

- `B : 01800000 01820000 01840000 01860000 01880000 018A0000 018C0000 018E0000 01900000 01920000 01940000 01960000 01980000 019A0000 019C0000 019E0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=0)
```

- `A : F78A4200 10145AFD AE842D9A 7DA2B6D1 E125063B 87057989 D33D3495 15A94983 24F95064 DD75BF25 2CE50A5D 109E76BE` 

- `B : 028800C2 F8D8F4B6 29CC61C2 DCBC40CD 1DCAF9C4 7BEE8676 2FDACB6A E94AB67C D826AF9B 21AE40DA D032F5A2 EC4D8941 0B45BDFF ECDFA502 5243D265 8161492E` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : B11AE006 5117AAEA F864E13E 8395DEC5 7473DED3 F4F3C55C EE1065D0 0FBCE63D 5D489898 3D28BAC9 DF45C1AD C5245735` 

- `B : 6E986FA3 0EF5A5BE CF36EA1B A553B940 992294EF 350A49DA 7F0FA886 E84EC433 FEA840CE EDB4D4A1 A7FEF584 A4F133B9 9D075AD2 D2B370A6 B5683EE5 F2818B9F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:subtractMfromC
```

170 

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `C : FFFFFF40 FFFFFF3F FFFFFF3E FFFFFF3D FFFFFF3C FFFFFF3B FFFFFF3A FFFFFF39 FFFFFF38 FFFFFF37 FFFFFF36 FFFFFF35 FFFFFF34 FFFFFF33 FFFFFF32 FFFFFF31` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : FFFFFF40 FFFFFF3F FFFFFF3E FFFFFF3D FFFFFF3C FFFFFF3B FFFFFF3A FFFFFF39 FFFFFF38 FFFFFF37 FFFFFF36 FFFFFF35 FFFFFF34 FFFFFF33 FFFFFF32 FFFFFF31` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : FFFFFF40 FFFFFF3F FFFFFF3E FFFFFF3D FFFFFF3C FFFFFF3B FFFFFF3A FFFFFF39 FFFFFF38 FFFFFF37 FFFFFF36 FFFFFF35 FFFFFF34 FFFFFF33 FFFFFF32 FFFFFF31` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

###### `W : 00000000 00000000` 

```
blocknumber=0:messageblock
```

- `M : 000000D0 000000D1 000000D2 000000D3 000000D4 000000D5 000000D6 000000D7 000000D8 000000D9 000000DA 000000DB 000000DC 000000DD 000000DE 000000DF` 

```
blocknumber=0:addMtoB
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:xorcounterWintoA
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

171 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

```
W:0000000000000000
```

```
blocknumber=0:permutation-rotateB
```

- `A : 6A2E9EF8 2A8ED2CE 5B7DEB2B 76F5EC56 C761D844 6FFDD495 A6E50D15 CB7EBB78 56F43E26 A9D57A1C 5FD697A6 E72A8ACB` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=0)
```

- `A : 40EDD726 1A8754BC 7AF69209 DD22532D 04BFEA68 4E68A17B 6E3AE516 89451CE8 237E61BE 50533EB1 77550A53 4EE347AA` 

- `B : 20C6148A C0A0482A 20FEE685 BD139D7F FB001597 B1D75E84 91851AE9 76FAE317 DCC19E41 AFECC14E 88EAF5AC B15CB855 BF5228D9 E538AB43 85496DF6 229DACD2` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : DCB0D1FF 9807FEF5 55FCAED1 DDFCB641 2546AE31 EFC27512 31D29DFA 9459E7A6 9E7C5606 FC6CB0E4 5699952C 8FDD2936` 

- `B : 5EA811AF 428F0F99 F1F49AC3 7C94CC73 978382D6 603DF212 8A6C5F00 9DD710E7 9ACC1283 38218397 BBD6BA77 40BA3915 A41D007D DA4CDC6A C4BFB9E8 2E9D41FD` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : A26F4FDE 24426C48 949686DD 723E1870 D02F6DE4 7F2B95C6 80DE631A DADF6026 ABCC94F0 E7106561 2495F432 6F985A6C` 

- `B : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-addCtoA
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

172 

- `B : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 58BCBB94 EC47A15F AEE93484 DFCBC8F7 A79448D8 BF65BE85 5A9D45D8 59979BCE C5CEA626 4B6B8229 16E719E3 7D6323F4 9305747C F34C64AE CAF91592 FDD6620B` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `C : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 58BCBAC4 EC47A08E AEE933B2 DFCBC824 A7944804 BF65BDB0 5A9D4502 59979AF7 C5CEA54E 4B6B8150 16E71909 7D632319 930573A0 F34C63D1 CAF914B4 FDD6612C` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 302D7A79 34333231 38373635 42412D39 46454443 4A494847 4E4D4C4B 5251504F 56555453 5A595857` 

```
blocknumber=1:addMtoB
```

- `A : FD749ED4 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : BD201D25 54AF06F3 1B549E1B 503B3691 1C07BA75 37DD3425 8ACABF7B 8DCACD28 FE05DB83 8DACAE89 5D2C5D4C C7AC6B60 E152BFEB 459DB420 214E6907 582FB983` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640` 

173 

```
1A48B71CF0976D17088CE80AA454EDF31C096BF4AC76224B5215781CCD5D2669
```

```
W:0000000100000000
```

```
blocknumber=1:xorcounterWintoA
```

- `A : FD749ED5 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : BD201D25 54AF06F3 1B549E1B 503B3691 1C07BA75 37DD3425 8ACABF7B 8DCACD28 FE05DB83 8DACAE89 5D2C5D4C C7AC6B60 E152BFEB 459DB420 214E6907 582FB983` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : FD749ED5 B798E530 33904B6F 46BDA85E 076934B4 454B4058 77F74527 FB4CF465 62931DA9 E778C8DB 22B3998E AC15CFB9` 

- `B : 3A4B7A40 0DE6A95E 3C3636A9 6D22A076 74EA380F 684A6FBA 7EF71595 9A511B95 B707FC0B 5D131B59 BA98BA58 D6C18F58 7FD7C2A5 68408B3B D20E429C 7306B05F` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=0)
```

- `A : AE92BFA7 A5A41F0D 97E9BFE0 D5D29125 D7E45AD4 AD76451A A07288D3 1CEAF9A7 EC0CCA2F 95DD5CBB 8F04308E 5CED88C8` 

- `B : A70EFF9C CF91415F 5F09EFC0 FEA428A2 C1CFD535 821D6591 A2635C06 D7B73173 7DFCCDC7 D00495F6 05CABBC0 0E916986 AEC2C512 8ADAF684 CC0AC526 CC200E64` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : 16432E52 F2DFD20D 94B0EB8C F25C60A2 5B7A200A C3588ED6 658076F8 583B6AD6 3613F4F2 B196A6CA F9AAD41D 5A9869F3` 

- `B : F908641C 7150CBBA 27B148F8 226E31BD 4A73A166 4A539216 429393EF 0A09F4EB 12454A23 AD29061F 60DA63F3 10814C51 F90055D0 29129C20 026A034A 3F8489E0` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : 9A1BAE76 63F344EA 3AB9815C FFF0A9EF 857327D2 CAE3E932 C69632F6 453E3FD7 EB8672D9 56EBC058 7203658F 89F9EF17` 

- `B : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6` 

174 

   - `5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : 8AC1482D 53E96EE2 8CE546AF 731DF574 883399D6 B9195E52 5CE34315 6EE2FB4A C53EAC67 FFD598F4 2AD76C84 644E1660` 

- `B : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `C : 61550878 89EF2B75 A1660C46 7EF3855B 7297B58C 1BC67793 7FB1C723 B66FC640 1A48B71C F0976D17 088CE80A A454EDF3 1C096BF4 AC76224B 5215781C CD5D2669` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : 8AC1482D 53E96EE2 8CE546AF 731DF574 883399D6 B9195E52 5CE34315 6EE2FB4A C53EAC67 FFD598F4 2AD76C84 644E1660` 

- `B : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `C : FCF1A617 2187C510 34FAA1DD 0E8416EE FE24431B A34F011E 4F844CAA 823C940F E21180E7 AE563FDE C247A3C7 5A0BA5AC CDBC1FA9 5A24D1FC FBC023C9 7303CE12` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : 8AC1482D 53E96EE2 8CE546AF 731DF574 883399D6 B9195E52 5CE34315 6EE2FB4A C53EAC67 FFD598F4 2AD76C84 644E1660` 

- `B : FCF1A617 2187C510 34FAA1DD 0E8416EE FE24431B A34F011E 4F844CAA 823C940F E21180E7 AE563FDE C247A3C7 5A0BA5AC CDBC1FA9 5A24D1FC FBC023C9 7303CE12` 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : 8AC1482D 53E96EE2 8CE546AF 731DF574 883399D6 B9195E52 5CE34315 6EE2FB4A C53EAC67 FFD598F4 2AD76C84 644E1660` 

- `B : FCF1A617 2187C510 34FAA1DD 0E8416EE FE24431B A34F011E 4F844CAA 823C940F E21180E7 AE563FDE C247A3C7 5A0BA5AC CDBC1FA9 5A24D1FC FBC023C9 7303CE12` 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 3231302D 36353433 2D393837 64636261 68676665 6C6B6A69 706F6E6D 74737271` 

175 

```
7877767500807A79000000000000000000000000000000000000000000000000
```

```
blocknumber=2:addMtoB
```

- `A : 8AC1482D 53E96EE2 8CE546AF 731DF574 883399D6 B9195E52 5CE34315 6EE2FB4A C53EAC67 FFD598F4 2AD76C84 644E1660` 

- `B : 2F22D644 57BCF943 6233DA14 72E7794F 668BA980 0FBA6B87 BFF3BB17 F6B00680 5A88F75C AED6BA57 C247A3C7 5A0BA5AC CDBC1FA9 5A24D1FC FBC023C9 7303CE12` 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:xorcounterWintoA
```

- `A : 8AC1482F 53E96EE2 8CE546AF 731DF574 883399D6 B9195E52 5CE34315 6EE2FB4A C53EAC67 FFD598F4 2AD76C84 644E1660` 

- `B : 2F22D644 57BCF943 6233DA14 72E7794F 668BA980 0FBA6B87 BFF3BB17 F6B00680 5A88F75C AED6BA57 C247A3C7 5A0BA5AC CDBC1FA9 5A24D1FC FBC023C9 7303CE12` 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : 8AC1482F 53E96EE2 8CE546AF 731DF574 883399D6 B9195E52 5CE34315 6EE2FB4A C53EAC67 FFD598F4 2AD76C84 644E1660` 

- `B : AC885E45 F286AF79 B428C467 F29EE5CE 5300CD17 D70E1F74 762F7FE7 0D01ED60 EEB8B511 74AF5DAD 478F848F 4B58B417 3F539B78 A3F8B449 4793F780 9C24E607` 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : 4CD8A476 C183CB00 EB15E699 0DA9B1DE A0EB57D0 D9904284 85488359 EC89FDEE 87262F39 56573E60 21B4EFC4 458269AA` 

- `B : 9E013C8D 418AFC55 5661DB7C 14EC44B4 F9153201 88738392 96E98368 0975D8D1 A5A8BAE5 40F67AC5 51541925 2CCCFE7B CD806D79 798D5C6C 9BCDF666 CA1F822E` 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=1)
```

- `A : CE92474C 4BEC74B0 28DB9B47 8DB33C30 0DC11FA4 5B09B805 738552C8 07D8C9EC 2DA81812 A9666E56 FD06BA39 000E0201` 

- `B : 8E853EFD 8409F2EE D62A2B37 85D0A413 207D83EE 467E968C 2F2A4317 ED1A4C5C 7A3CCD78 35FF7EC5 758C56F2 2BD53F39 693E3AA8 57ECFF22 BBE141FA 6C18324E` 

176 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : CB962C61 AAB5F2E1 BD48C6D2 7B006B1B BEC24D1C A7A67B33 B8CFC3C6 551FF849 32227BC2 388DD364 E2ABB1A3 8FEAD9F3` 

- `B : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : B135B153 9A854097 D06C7812 766B154C 1CBB394A 0F02EECD 40108811 C03F1085 22CFBD52 6E10599B 55D673B5 5251DB43` 

- `B : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `C : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : B135B153 9A854097 D06C7812 766B154C 1CBB394A 0F02EECD 40108811 C03F1085 22CFBD52 6E10599B 55D673B5 5251DB43` 

- `B : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `C : E621E3BD D911D5ED 04A77B99 DC69C6DF 889BACE0 9C4034D0 CFF1EB10 9FA94D55 E58ED5F6 6ECDA079 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : B135B153 9A854097 D06C7812 766B154C 1CBB394A 0F02EECD 40108811 C03F1085 22CFBD52 6E10599B 55D673B5 5251DB43` 

- `B : E621E3BD D911D5ED 04A77B99 DC69C6DF 889BACE0 9C4034D0 CFF1EB10 9FA94D55 E58ED5F6 6ECDA079 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `C : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `W : 00000002 00000000` 

- `n0_final = 0 : add M to B` 

- `A : B135B153 9A854097 D06C7812 766B154C 1CBB394A 0F02EECD 40108811 C03F1085 22CFBD52 6E10599B 55D673B5 5251DB43` 

177 

- `B : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `C : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `W : 00000002 00000000` 

- `n0_final = 0 : xor counter W into A` 

- `A : B135B151 9A854097 D06C7812 766B154C 1CBB394A 0F02EECD 40108811 C03F1085 22CFBD52 6E10599B 55D673B5 5251DB43` 

- `B : 185313EA 0F470A20 31E0B3D0 40CD2940 F1031345 08AB9F39 4061597D 141CBFC6 5E064C6B 6F4E1AF2 F8DD0AEF 9BC3588A E6792687 FB3107E7 89289CE4 090F0328` 

- `C : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : B135B151 9A854097 D06C7812 766B154C 1CBB394A 0F02EECD 40108811 C03F1085 22CFBD52 6E10599B 55D673B5 5251DB43` 

- `B : 27D430A6 14401E8E 67A063C1 5280819A 268BE206 3E721157 B2FA80C2 7F8C2839 98D6BC0C 35E4DE9C 15DFF1BA B1153786 4D0FCCF2 0FCFF662 39C91251 0650121E` 

- `C : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

- `A : BA7F4347 4863AD24 0217DF60 0D93104E 2415EBE3 3762C22A 0E26C6D8 45A1EC10 C78897F8 F58997A7 1C3FD0C5 06D77D1B` 

- `B : 69A07B7E A8B6F184 5EFF78F9 34F39108 96FDD010 B4791F7B 942C38A2 4546439D 09DA101E 61BFD560 C87FCC4E 9B02EDE9 DF9F255C A803BE1F 8E7A043D FECCCB8D` 

- `C : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : 9E3B324B 4BAF7BF8 8A1A81C7 10A836D8 3A6B0F26 2BED5D03 FFE01EEF F099D74B F33A942E DEA5482D C56A0714 6721E434` 

- `B : 7BA6E426 B2B967DB E0552F40 7A23F6F8 213ECBF0 49A88925 12CD89AE 12529CF1 7270ED88 772F2EC7 E51AE6A5 D95212F4 7AAABA60 8415DEC3 1CEBE96B F2FFBFAF` 

- `C : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

178 

- `A : D5362471 109DB504 9A4A190F 81D6045F 155D65AF B057CF0A F8488BD1 3F7BFE60 6F2DFF5B 00BE2E79 D45D77A9 6099636C` 

- `B : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `C : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : 15B08ECB DAB02117 B8D33009 70D24C6A B75862A2 100C71C3 E1CD4932 700A0A9F 664E3382 4A371C3B 4A67E3D4 943C81F5` 

- `B : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `C : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `W : 00000002 00000000` 

- `n0_final = 0 : subtract M from C` 

- `A : 15B08ECB DAB02117 B8D33009 70D24C6A B75862A2 100C71C3 E1CD4932 700A0A9F 664E3382 4A371C3B 4A67E3D4 943C81F5` 

- `B : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `C : 03AC7637 A5F0EFE2 3A488328 36A74BA5 0C2B6DDD 6D4BB59D AC745096 EA5799EC 3CCCB19E 3326FECD AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

###### `W : 00000002 00000000` 

- `n0_final = 0 : swap B with C` 

- `A : 15B08ECB DAB02117 B8D33009 70D24C6A B75862A2 100C71C3 E1CD4932 700A0A9F 664E3382 4A371C3B 4A67E3D4 943C81F5` 

- `B : 03AC7637 A5F0EFE2 3A488328 36A74BA5 0C2B6DDD 6D4BB59D AC745096 EA5799EC 3CCCB19E 3326FECD AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `C : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `W : 00000002 00000000` 

```
n0_final=1:addMtoB
```

- `A : 15B08ECB DAB02117 B8D33009 70D24C6A B75862A2 100C71C3 E1CD4932 700A0A9F 664E3382 4A371C3B 4A67E3D4 943C81F5` 

- `B : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `C : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `W : 00000002 00000000` 

179 

```
n0_final=1:xorcounterWintoA
```

- `A : 15B08EC9 DAB02117 B8D33009 70D24C6A B75862A2 100C71C3 E1CD4932 700A0A9F 664E3382 4A371C3B 4A67E3D4 943C81F5` 

- `B : 35DDA664 DC262415 6781BB5F 9B0AAE06 7492D442 D9B72006 1CE3BF03 5ECB0C5D B5442813 33A77946 AC2891DD FD4A79C4 1FA1F16D 68ABD2DF 6A96CDA9 A8254290` 

- `C : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

- `A : 15B08EC9 DAB02117 B8D33009 70D24C6A B75862A2 100C71C3 E1CD4932 700A0A9F 664E3382 4A371C3B 4A67E3D4 943C81F5` 

- `B : 4CC86BBB 482BB84C 76BECF03 5C0D3615 A884E925 400DB36E 7E0639C7 18BABD96 50276A88 F28C674E 23BB5851 F389FA94 E2DA3F43 A5BED157 9B52D52D 8521504A` 

- `C : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : E00AE65C 41E3AD21 962642C3 6DBBC826 7A0AE7C0 E561DCCB 104A79A2 F13D48ED BCD491BC 47007981 CA03134A DDCD05B0` 

- `B : 6C2A38A6 99125EC5 C7D291CC B2C855AA D4FCCA74 9A8545E8 13B9F5D3 3FB7CC3E E365BB53 5DE748E3 728A5C17 C5210F66 DA416724 F561F071 5F7C1767 9806974C` 

- `C : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

- `A : 87492C4D 9D4CAD67 A7274C1F 73A47CAB 52B9484B EEF47C12 785C3BCA 6286CE3D E02D1461 C6E1C1C8 C2823D6C C7EA98EB` 

- `B : ACC058BC 9EF93721 9EF03CA8 EDED87AC B62B7F77 0C14B5E6 1A0E2935 477AFF68 BE7DA515 D97DC35E BDCC0BCE 06199D99 19C479FD FBC8630E 395BEAFB AD741F5B` 

- `C : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 2)` 

- `A : 5A296E6B B453D5A8 1D363EEA 60DC971D 057EF2FC B7071E8D F33FE465 CA4C815C 1E2E0224 59253DB5 9C2E569B D43BEEA3` 

- `B : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `C : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

180 

###### `W : 00000002 00000000` 

```
n0_final=1:permutation-addCtoA
```

- `A : D826C264 D20E6759 AECD6DDA 8EF5DBD6 6BE8E4C1 7D7D7D1A 2F6314CF B37324FA 7C1E3493 35A43FC7 B1C288C8 F462F834` 

- `B : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `C : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : subtract M from C` 

- `A : D826C264 D20E6759 AECD6DDA 8EF5DBD6 6BE8E4C1 7D7D7D1A 2F6314CF B37324FA 7C1E3493 35A43FC7 B1C288C8 F462F834` 

- `B : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `C : 1D4DA0B2 E7C4360B AE3BBC56 2CDFE956 004CE609 0FC7EE48 CFBF873F E6194FD1 95CBCACB A175F302 CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : swap B with C` 

- `A : D826C264 D20E6759 AECD6DDA 8EF5DBD6 6BE8E4C1 7D7D7D1A 2F6314CF B37324FA 7C1E3493 35A43FC7 B1C288C8 F462F834` 

- `B : 1D4DA0B2 E7C4360B AE3BBC56 2CDFE956 004CE609 0FC7EE48 CFBF873F E6194FD1 95CBCACB A175F302 CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `C : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : add M to B` 

- `A : D826C264 D20E6759 AECD6DDA 8EF5DBD6 6BE8E4C1 7D7D7D1A 2F6314CF B37324FA 7C1E3493 35A43FC7 B1C288C8 F462F834` 

- `B : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

- `C : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : xor counter W into A` 

- `A : D826C266 D20E6759 AECD6DDA 8EF5DBD6 6BE8E4C1 7D7D7D1A 2F6314CF B37324FA 7C1E3493 35A43FC7 B1C288C8 F462F834` 

- `B : 4F7ED0DF 1DF96A3E DB74F48D 91434BB7 68B44C6E 7C3358B1 402EF5AC 5A8CC242 0E434140 A1F66D7B CD82B965 72202476 65877464 F76A6C01 12755A80 7A99E3CC` 

181 

- `C : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - rotate B` 

- `A : D826C266 D20E6759 AECD6DDA 8EF5DBD6 6BE8E4C1 7D7D7D1A 2F6314CF B37324FA 7C1E3493 35A43FC7 B1C288C8 F462F834` 

- `B : A1BE9EFD D47C3BF2 E91BB6E9 976F2286 98DCD168 B162F866 EB58805D 8484B519 82801C86 DAF743EC 72CB9B05 48ECE440 E8C8CB0E D803EED4 B50024EA C798F533` 

- `C : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 0)` 

- `A : E8944762 7BE8E366 597E5149 BE805B7B A478B79D D5559665 BD70C24D 5C30AF3E 7DB340CD AF64BBCF F4EF6D81 399AAEBF` 

- `B : DE9DE86C DBED9EA7 4D46E3AC 1FC6F977 6A3EEAB3 486F9957 943E3D09 AAC63AF2 874C863F E575C3E9 EE87A474 57BC99C0 C6FA2E80 3410C130 CC81E763 CE4E4EE3` 

- `C : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : 3EA1B235 DD7CC0AD 6AEBF1AA 542AD5EB 565684BF F19959DE 6D3D928A F45B85F1 AD5D43E8 94694935 8FBADF63 34677334` 

- `B : 71831A04 B792148C A202DCEC 48018DC3 86DF6971 FB498464 58395A8F 9E14F92E CFC741B5 E868B881 481B46BC 04AC1994 245D2641 66472441 0BC1A3B2 9738E7C9` 

- `C : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : D922DEAA 2DCAD210 A701A6BF AC069AC0 B6099E6C 067D8D76 16677DEE 8032A1F5 03B85B77 04743B88 BD2AAF8A C4F50011` 

- `B : 593CCDF8 F2E993B0 DD79ADFB A855551E 2B63F3B6 24A62526 E88CEC5E 6FD09762 D678E2F8 2953038A 79AE0F69 76956D22 B4FDE80A 37058CF5 55561711 157B307D` 

- `C : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - add C to A` 

- `A : F9D98DBE 30B70551 86CB5CAF BDB2F590 AF169E21 BD8AF9BE 9EEA9756 F7D08C3A C51970D2 26C8004C 5BFD5D4B 24891C29` 

182 

- `B : 593CCDF8 F2E993B0 DD79ADFB A855551E 2B63F3B6 24A62526 E88CEC5E 6FD09762 D678E2F8 2953038A 79AE0F69 76956D22 B4FDE80A 37058CF5 55561711 157B307D` 

- `C : 6712B5A5 3AFA6FFE 29704ABF 760A3998 C9806F7B 5385419B D6D5937F 11D69632 867A4728 FA0367CF 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : F9D98DBE 30B70551 86CB5CAF BDB2F590 AF169E21 BD8AF9BE 9EEA9756 F7D08C3A C51970D2 26C8004C 5BFD5D4B 24891C29` 

- `B : 593CCDF8 F2E993B0 DD79ADFB A855551E 2B63F3B6 24A62526 E88CEC5E 6FD09762 D678E2F8 2953038A 79AE0F69 76956D22 B4FDE80A 37058CF5 55561711 157B307D` 

- `C : 34E18578 04C53BCB FC371288 11A6D737 61190916 E719D732 66662512 9D6323C1 0E02D0B3 F982ED56 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : F9D98DBE 30B70551 86CB5CAF BDB2F590 AF169E21 BD8AF9BE 9EEA9756 F7D08C3A C51970D2 26C8004C 5BFD5D4B 24891C29` 

- `B : 34E18578 04C53BCB FC371288 11A6D737 61190916 E719D732 66662512 9D6323C1 0E02D0B3 F982ED56 77580C07 39804591 D2590E21 514A0457 11667C92 712C2FEB` 

- `C : 593CCDF8 F2E993B0 DD79ADFB A855551E 2B63F3B6 24A62526 E88CEC5E 6FD09762 D678E2F8 2953038A 79AE0F69 76956D22 B4FDE80A 37058CF5 55561711 157B307D` 

- `W : 00000002 00000000` 

```
Hashvalue:
```

```
H:79AE0F6976956D22B4FDE80A37058CF555561711157B307D
```

```
Hashvalue(bytearray):
```

- `H : 69 0F AE 79 22 6D 95 76 0A E8 FD B4 F5 8C 05 37 11 17 56 55 7D 30 7B 15` 

### **B.3 Intermediate States for Shabal-224 (Message A)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

183 

```
blocknumber=-1:messageblock
```

- `M : 000000E0 000000E1 000000E2 000000E3 000000E4 000000E5 000000E6 000000E7 000000E8 000000E9 000000EA 000000EB 000000EC 000000ED 000000EE 000000EF` 

```
blocknumber=-1:addMtoB
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 000000E0 000000E1 000000E2 000000E3 000000E4 000000E5 000000E6 000000E7 000000E8 000000E9 000000EA 000000EB 000000EC 000000ED 000000EE 000000EF` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:xorcounterWintoA
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 000000E0 000000E1 000000E2 000000E3 000000E4 000000E5 000000E6 000000E7 000000E8 000000E9 000000EA 000000EB 000000EC 000000ED 000000EE 000000EF` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 01C00000 01C20000 01C40000 01C60000 01C80000 01CA0000 01CC0000 01CE0000 01D00000 01D20000 01D40000 01D60000 01D80000 01DA0000 01DC0000 01DE0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=0)
```

- `A : E0F553CA 360FB9F0 13F563A2 1751BF18 97E7BD38 130C3A22 98E64161 83D3B87F F2FB6BE4 D594E9DE 8CA0C9A1 E61F0AC1` 

- `B : 024800E2 FB28F276 182C49FA 2B1FCF5D 6B8842C7 EF67C5DD 6481BE9E 7FB04780 0EA4941B 29CF1621 70F7365E 1A4CF53E 1CBAAC35 CA44460F EFB29C5D EB1240E7` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : 257C1CF3 FAC54BC3 B544997B B9426917 594FC7A1 D13345E4 17044F51 13DC1230 4D00378B E315C946 A6A4D823 AE0E1AAC` 

184 

- `B : 67772EA5 A9D983AA 1B7E3DF8 B711623E 65EF4DFA C225BD02 90585AE0 AE916A53 C7CACB3A 56A4987E AB550A38 72247C94 9FC56034 BA443604 379E8815 3A076C00` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:subtractMfromC
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `C : FFFFFF20 FFFFFF1F FFFFFF1E FFFFFF1D FFFFFF1C FFFFFF1B FFFFFF1A FFFFFF19 FFFFFF18 FFFFFF17 FFFFFF16 FFFFFF15 FFFFFF14 FFFFFF13 FFFFFF12 FFFFFF11` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : FFFFFF20 FFFFFF1F FFFFFF1E FFFFFF1D FFFFFF1C FFFFFF1B FFFFFF1A FFFFFF19 FFFFFF18 FFFFFF17 FFFFFF16 FFFFFF15 FFFFFF14 FFFFFF13 FFFFFF12 FFFFFF11` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

185 

```
A:01340BD473381D1DF97F750828F07BF48E842C24D8A8596FD2D4F99AD0763C3C
632406CB965BA4DD014EB6D93E7F3B64
```

```
B:FFFFFF20FFFFFF1FFFFFFF1EFFFFFF1DFFFFFF1CFFFFFF1BFFFFFF1AFFFFFF19
FFFFFF18FFFFFF17FFFFFF16FFFFFF15FFFFFF14FFFFFF13FFFFFF12FFFFFF11
C:EC9906C8F21851C0C0A747BA21DAD58B35156FDF088C98E726303F368A2D50AC
FEEE45AE8A1E966C7B811214CBC13AEBA351395D1D2C372B918C590CB58E1C9B
W:0000000000000000
blocknumber=0:messageblock
M:000000F0000000F1000000F2000000F3000000F4000000F5000000F6000000F7
000000F8000000F9000000FA000000FB000000FC000000FD000000FE000000FF
```

```
blocknumber=0:addMtoB
```

```
A:01340BD473381D1DF97F750828F07BF48E842C24D8A8596FD2D4F99AD0763C3C
632406CB965BA4DD014EB6D93E7F3B64
B:0000001000000010000000100000001000000010000000100000001000000010
0000001000000010000000100000001000000010000000100000001000000010
C:EC9906C8F21851C0C0A747BA21DAD58B35156FDF088C98E726303F368A2D50AC
FEEE45AE8A1E966C7B811214CBC13AEBA351395D1D2C372B918C590CB58E1C9B
W:0000000000000000
```

```
blocknumber=0:xorcounterWintoA
```

```
A:01340BD473381D1DF97F750828F07BF48E842C24D8A8596FD2D4F99AD0763C3C
632406CB965BA4DD014EB6D93E7F3B64
```

```
B:0000001000000010000000100000001000000010000000100000001000000010
0000001000000010000000100000001000000010000000100000001000000010
C:EC9906C8F21851C0C0A747BA21DAD58B35156FDF088C98E726303F368A2D50AC
FEEE45AE8A1E966C7B811214CBC13AEBA351395D1D2C372B918C590CB58E1C9B
W:0000000000000000
blocknumber=0:permutation-rotateB
A:01340BD473381D1DF97F750828F07BF48E842C24D8A8596FD2D4F99AD0763C3C
632406CB965BA4DD014EB6D93E7F3B64
B:0020000000200000002000000020000000200000002000000020000000200000
0020000000200000002000000020000000200000002000000020000000200000
C:EC9906C8F21851C0C0A747BA21DAD58B35156FDF088C98E726303F368A2D50AC
FEEE45AE8A1E966C7B811214CBC13AEBA351395D1D2C372B918C590CB58E1C9B
W:0000000000000000
```

```
blocknumber=0:permutation(j=0)
```

```
A:4389B9547C2E65DF7AC0A60E4D3E56717E2ECC0C301134952288EF2ADA590830
F8F8D0FD866100F7129EA35AB74146B4
B:3D7D89CC64237EF2265812A5119D3DC4819133F3CFAECB6ADD3710D525E6F7CF
07472F0279DEFF08ED215CA548FEB94BBC3646AB83919A20857F59F1B281A98E
```

186 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

```
W:0000000000000000
```

```
blocknumber=0:permutation(j=1)
```

- `A : E11D69E6 69E4164B 0FC5373C 7E495272 A8B9B043 8CDC5330 90551180 5E5046D9 9EB4F2BE E6580BF7 E5386C60 AD2654AD` 

- `B : 2CCEC394 1350B7FB 8F6F4688 88CED426 62696AA6 86FA62DD A0A9B234 191444CC 106CC81D 65A617A4 2A787188 104BDF1B 2F2AC2EB 7400988E 65545D9C C4ACEA3B` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : 01F5E756 E4B92946 BCFDB7C5 EFD3BD7F 466630E8 D1059816 DBA401AC 7E64640B B75BD62C 2F4525B5 AE5698A7 C7AF460B` 

- `B : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-addCtoA
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

187 

- `B : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=1:addMtoB
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:xorcounterWintoA
```

- `A : A5201466 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : A5201466 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : 0BB1D932 A19FE430 8D91814E A93043B5 DDD66A2A 2FE41119 7C804C60 9F6B145A 896DFDDC 2AE7143D 2234F702 73E19782 70C346A2 6C5C3A58 B01D2318 37396B1C` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18` 

188 

```
99405F2DE5B648A170AB1D43A10C25C216F1AC0538BBEB569B01DC60B1096D83
```

```
W:0000000100000000
```

```
blocknumber=1:permutation(j=0)
```

- `A : 1117E7A7 33F2EAC4 1C1B8823 477C7385 5A5AEA53 94ED38E9 CBE63E23 3AF61CE8 B964BBFA EA3AEAAE 41D58BD0 13DE80E2` 

- `B : AB194FD1 06D8D84E 2227FA94 9ECE08DF 1E09C1F9 34DAE524 CD19591C FBDFCBA2 5440BFBC 400B3D2B FA439A2B 0BE25019 0F6E951C 14B5618B 83DE31ED D6F15A42` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : DF76C800 CA73BBD4 CF3287F9 0E9B0C4F 045BF121 196B8245 19357752 9C1517BB 05DAAF5F C09AD7FF C350AF3F 79EDE108` 

- `B : 16FCB2AC DC80E49C 4A03A6CD DDEE277D C636D352 56D0E248 A69DE2F9 71AD89B2 88084887 B59A3E7D C44A4C51 E6A05382 E57924E6 CFFEBEAC E176EB76 CE085CC1` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : 0E6F0B4C 6559A807 5DF26C97 A40E5863 8B485A08 2337EE51 C933CD67 1FCBF8D8 60869449 025AA346 F0381F84 180502C2` 

- `B : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : 65051D8E 9BD99592 F97A736F 5FF1DD67 62D711A0 DC068F04 11B6318A B158BEBF 28180420 ED657C5D 255C667D 260328B8` 

- `B : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : 65051D8E 9BD99592 F97A736F 5FF1DD67 62D711A0 DC068F04 11B6318A B158BEBF 28180420 ED657C5D 255C667D 260328B8` 

- `B : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8` 

189 

```
64A734F8B7FC6D55BE58AA3B2D74A022558B227B625821E0CD2A36967BEA44BE
```

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : 65051D8E 9BD99592 F97A736F 5FF1DD67 62D711A0 DC068F04 11B6318A B158BEBF 28180420 ED657C5D 255C667D 260328B8` 

- `B : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : 65051D8E 9BD99592 F97A736F 5FF1DD67 62D711A0 DC068F04 11B6318A B158BEBF 28180420 ED657C5D 255C667D 260328B8` 

- `B : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 00000080 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : 65051D8E 9BD99592 F97A736F 5FF1DD67 62D711A0 DC068F04 11B6318A B158BEBF 28180420 ED657C5D 255C667D 260328B8` 

- `B : E4B57421 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000002 00000000` 

```
blocknumber=2:xorcounterWintoA
```

- `A : 65051D8C 9BD99592 F97A736F 5FF1DD67 62D711A0 DC068F04 11B6318A B158BEBF 28180420 ED657C5D 255C667D 260328B8` 

- `B : E4B57421 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

190 

###### `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : 65051D8C 9BD99592 F97A736F 5FF1DD67 62D711A0 DC068F04 11B6318A B158BEBF 28180420 ED657C5D 255C667D 260328B8` 

- `B : E843C96A 11009834 F8A23D20 FDFA0900 9BCA75B1 26042D64 58A604A2 96304409 BE5B3280 9143CB6C 3A86E156 4B854218 580A2DE3 D6AC7177 B8C13603 DB076212` 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : 4391A10E 3AE3E7C0 75D88812 B1835B7A 56932F34 B98C9226 7432E079 23E6A3AF 2C75A3FD 909E90CD 773EF253 7BC6C86A` 

- `B : D5DEB4C2 46A6A31D DF7B434C 5526BAF2 9EF83BA8 0A7B3711 3A8116C2 F079D443 AF3C3903 4DE6F9EB FDCCCF00 1333B3A5 0C7A0537 6844FAD0 FBA51BEA F87260A0` 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=1)
```

- `A : ECC02E5D 5CD02843 23E21DC1 58EFEA08 76644896 4A4B0D3E DDB4188B 843C5EAC 1DC12C83 938542E7 4E0625FA 29F64BBB` 

- `B : 7AF36518 276A5E1D 20B1BA18 DA49A6B6 DFCEA42D 788CD33A C4FBF781 36FA1CC3 4D47A3A5 38E2246A 27847C3F 817772BD 916FBD07 653D0761 D501D0A1 8B276012` 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : 2822A50E 3FC020F8 775F71F0 FD8CE38C A40D9ABE 9B7E1E3A 5E22CF13 0A410C42 219BFCC7 3AD12AC0 57D3B6A3 3E2D0EA5` 

- `B : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : 88652A38 8EDE7058 79D8D027 5654149A 8F8634BE F9B88017 B64078BF 5436B0F5 BE9EF22B 7300D449 A92FD940 B8E64611` 

- `B : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

191 

- `C : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : 88652A38 8EDE7058 79D8D027 5654149A 8F8634BE F9B88017 B64078BF 5436B0F5 BE9EF22B 7300D449 A92FD940 B8E64611` 

- `B : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `C : 7B95DA4F 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : 88652A38 8EDE7058 79D8D027 5654149A 8F8634BE F9B88017 B64078BF 5436B0F5 BE9EF22B 7300D449 A92FD940 B8E64611` 

- `B : 7B95DA4F 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `C : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : add M to B` 

- `A : 88652A38 8EDE7058 79D8D027 5654149A 8F8634BE F9B88017 B64078BF 5436B0F5 BE9EF22B 7300D449 A92FD940 B8E64611` 

- `B : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `C : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : xor counter W into A` 

- `A : 88652A3A 8EDE7058 79D8D027 5654149A 8F8634BE F9B88017 B64078BF 5436B0F5 BE9EF22B 7300D449 A92FD940 B8E64611` 

- `B : 7B95DACF 6919A8EF 9C66A3DD B6E3A04A 7DFD5216 37079368 EF36569B B8AAB4F8 64A734F8 B7FC6D55 BE58AA3B 2D74A022 558B227B 625821E0 CD2A3696 7BEA44BE` 

- `C : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : 88652A3A 8EDE7058 79D8D027 5654149A 8F8634BE F9B88017 B64078BF 5436B0F5 BE9EF22B 7300D449 A92FD940 B8E64611` 

192 

- `B : B59EF72B 51DED233 47BB38CD 40956DC7 A42CFBFA 26D06E0F AD37DE6C 69F17155 69F0C94E DAAB6FF8 54777CB1 40445AE9 44F6AB16 43C0C4B0 6D2D9A54 897CF7D4` 

- `C : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

- `A : 31D8859A 81BBD69A D832456B 27B965C0 47A2C6A8 82833477 0E8FC174 CCB34CEA 081D6329 C770D623 556C9A3E 167C914E` 

- `B : 37162622 67E2A9D0 965887A1 B0CD04F6 F004CEA2 30DC1796 AB1F8252 E0AE51BF 24030E4A 8DD9F62D 027D9CA3 690BDB63 47CA2C49 F9C5A005 FD968E3C CABF7596` 

- `C : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : 7BE20C18 AA2C47CF 982D6AA9 6AE528AE 647C8975 4D24674D 9D7FC322 D6A97646 56D7EB06 47E799F5 EABC486C E353B646` 

- `B : 86E8F0DE 9F97ACDA FB3A9209 7B7A7CBD 492189BC D9A04926 437CB336 DDF0EAC6 CC1BEF73 4E60546B 6329AC10 470D6197 14172E18 4150D8B9 99AD20A4 BC286294` 

- `C : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

- `A : 29FA00C0 8D7A0BC5 115E952C E6562CB0 3CAB8D45 5AB7CC65 178DD218 E5232A74 DADB9113 6BE977D8 3B017BC6 3045CAF4` 

- `B : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `C : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : ADCD9E99 88F56229 EBF98C94 F24FDBC7 38B63A4D 1AF4CB9D F8199694 DDC2B9FE F69A2362 926225C4 90C27A47 22A2DCB1` 

- `B : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `C : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : subtract M from C` 

193 

- `A : ADCD9E99 88F56229 EBF98C94 F24FDBC7 38B63A4D 1AF4CB9D F8199694 DDC2B9FE F69A2362 926225C4 90C27A47 22A2DCB1` 

- `B : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `C : 967FCA03 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : swap B with C` 

- `A : ADCD9E99 88F56229 EBF98C94 F24FDBC7 38B63A4D 1AF4CB9D F8199694 DDC2B9FE F69A2362 926225C4 90C27A47 22A2DCB1` 

- `B : 967FCA03 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `C : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

- `A : ADCD9E99 88F56229 EBF98C94 F24FDBC7 38B63A4D 1AF4CB9D F8199694 DDC2B9FE F69A2362 926225C4 90C27A47 22A2DCB1` 

- `B : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `C : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

###### `W : 00000002 00000000` 

- `n0_final = 1 : xor counter W into A` 

- `A : ADCD9E9B 88F56229 EBF98C94 F24FDBC7 38B63A4D 1AF4CB9D F8199694 DDC2B9FE F69A2362 926225C4 90C27A47 22A2DCB1` 

- `B : 967FCA83 9A1FA1F8 087265EC B4E75594 684012AA 31267973 0157610C 6F8725F5 C17D220B 1545A911 EED5C892 F75016C6 FCBB7937 0F54DBFD 022FE81F D79C317F` 

- `C : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

- `A : ADCD9E9B 88F56229 EBF98C94 F24FDBC7 38B63A4D 1AF4CB9D F8199694 DDC2B9FE F69A2362 926225C4 90C27A47 22A2DCB1` 

- `B : 95072CFF 43F1343F CBD810E4 AB2969CE 2554D080 F2E6624C C21802AE 4BEADF0E 441782FA 52222A8B 9125DDAB 2D8DEEA0 F26FF976 B7FA1EA9 D03E045F 62FFAF38` 

- `C : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `W : 00000002 00000000` 

194 

```
n0_final=1:permutation(j=0)
```

- `A : 9CAD29B1 A89358CB 9B5770C1 29C8BAF4 0B1899FD AE1ACC26 011F4255 70CB6B9E 4F1BD2B6 EB3D9804 20497238 FE4AB14D` 

- `B : 01173CD1 C5334103 F08E1786 EBEC8137 BE4EC702 B429F740 7AD0B8F7 18E12A7D 38CB28BD B08632ED FDFD3690 5AAE93F2 878D24A3 38989A67 C4D48781 13C81B7B` 

- `C : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

- `A : D550385F 9E18D944 38F76D2C 151A2FAC E7849148 A3F4532D 415AE1A2 A879EC8E E9B6AD1C B170E5DC C6B74FB6 BF92259F` 

- `B : CC0307CE BB664DC2 FA73BA78 D2D35DDF 6AD4DCE6 26DCF4A2 CCE9C1A7 71AF8E9A 5B3996DA 00EB4360 3CF2FFF2 5FB8F7B7 176127F0 2D3A981C 370C115E 70162587` 

- `C : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 2)` 

- `A : 5FFD77F6 7748D8F6 D1EEB1E2 2725E20E B541DD5C 09C7ADB7 798A6EF6 9B1BC0D0 47610F1B 156A99CE 8AC10645 9BE82916` 

- `B : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `C : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - add C to A` 

- `A : CB9C9831 F7C7EEE2 672F111F CF7B1858 2E62EDB4 D8A03D24 319C302A 79EDA771 9D5D45F6 C21F654E 9CC6415D 2A06710C` 

- `B : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `C : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `W : 00000002 00000000` 

- `n0_final = 1 : subtract M from C` 

- `A : CB9C9831 F7C7EEE2 672F111F CF7B1858 2E62EDB4 D8A03D24 319C302A 79EDA771 9D5D45F6 C21F654E 9CC6415D 2A06710C` 

- `B : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `C : 2F2DF649 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

195 

###### `W : 00000002 00000000` 

```
n0_final=1:swapBwithC
```

- `A : CB9C9831 F7C7EEE2 672F111F CF7B1858 2E62EDB4 D8A03D24 319C302A 79EDA771 9D5D45F6 C21F654E 9CC6415D 2A06710C` 

- `B : 2F2DF649 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `C : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : add M to B` 

- `A : CB9C9831 F7C7EEE2 672F111F CF7B1858 2E62EDB4 D8A03D24 319C302A 79EDA771 9D5D45F6 C21F654E 9CC6415D 2A06710C` 

- `B : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `C : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : xor counter W into A` 

- `A : CB9C9833 F7C7EEE2 672F111F CF7B1858 2E62EDB4 D8A03D24 319C302A 79EDA771 9D5D45F6 C21F654E 9CC6415D 2A06710C` 

- `B : 2F2DF6C9 BCC3BF71 4858641B 1EEE1974 4446EC47 C1C56677 68580CBF A24806C2 5B63AC5D 39889B4C 2E2175C7 94C616A5 0D0A32DC 16B73955 F7A4C570 B7EAF022` 

- `C : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - rotate B` 

- `A : CB9C9833 F7C7EEE2 672F111F CF7B1858 2E62EDB4 D8A03D24 319C302A 79EDA771 9D5D45F6 C21F654E 9CC6415D 2A06710C` 

- `B : ED925E5B 7EE37987 C83690B0 32E83DDC D88E888D CCEF838A 197ED0B0 0D854490 58BAB6C7 36987311 EB8E5C42 2D4B298C 65B81A14 72AA2D6E 8AE1EF49 E0456FD5` 

- `C : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 0)` 

- `A : 8DFF438F E6CFE964 AC30082E D3C8B038 4C6300DE 0D9DB8BC 78FC2DFD BEF23703 7AAD9D34 42832D7D 3F2A7DDE D6CE7FA3` 

- `B : F99EB726 E4D5AEDD 7A4E6F4A 0626997C 0281EE3A 6BBD4056 B5FE7362 5A0741DC 34270F45 D04C34A0 17C93AA4 73A7D344 B9708858 FC644C47 460C2942 ECBD906C` 

196 

- `C : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : C2D0320E D3313CC3 3B05577B FD933B4A EF7DDC9E F1F76F48 89B9ACCD B97CB043 E64AFCF7 BC990ABD 1901F3DB 952A2D59` 

- `B : A8C685C2 7A93D67F ED5EFCC7 07229415 1CB6DF7C 941C75EE 8D02EAE1 DEDB511E 5561D37B 8C56AA7D EB68DDCC E523623D 626333D0 F6C00838 FA5E01B6 9FF86F65` 

- `C : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : AB7D1FE8 8E5BB452 B1FA6ACB ACE0D826 1F67DA7C F3F4769D C1FC439F C2A14D05 0956F16F 99B5418E 2EB779CD F12F9B77` 

- `B : BE6AC9DC 86AFB8BB 300C6C1B 237F0C8C 6DEF5EEF 599CA070 540040F7 EEA985E4 4A5B8375 14A6DD99 E8D207F9 F7187681 326F6930 8BCAAE00 25F4855F 3120BA43` 

- `C : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - add C to A` 

- `A : 08FC66FC CE392D14 42C29F35 5649D86A DCD65214 9A423F72 99D2F688 5073E130 1E1F9B61 A28A416E 9C9572AB C3A9B2BC` 

- `B : BE6AC9DC 86AFB8BB 300C6C1B 237F0C8C 6DEF5EEF 599CA070 540040F7 EEA985E4 4A5B8375 14A6DD99 E8D207F9 F7187681 326F6930 8BCAAE00 25F4855F 3120BA43` 

- `C : 33D587F9 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : 08FC66FC CE392D14 42C29F35 5649D86A DCD65214 9A423F72 99D2F688 5073E130 1E1F9B61 A28A416E 9C9572AB C3A9B2BC` 

- `B : BE6AC9DC 86AFB8BB 300C6C1B 237F0C8C 6DEF5EEF 599CA070 540040F7 EEA985E4 4A5B8375 14A6DD99 E8D207F9 F7187681 326F6930 8BCAAE00 25F4855F 3120BA43` 

- `C : 33D58779 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5 FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : 08FC66FC CE392D14 42C29F35 5649D86A DCD65214 9A423F72 99D2F688 5073E130 1E1F9B61 A28A416E 9C9572AB C3A9B2BC` 

197 

- `B : 33D58779 1AD91014 D67F57EC FDADD8EC 75AB31C5 C50ECE4D B7C2CD52 3B8500C5` 

   - `FCCD0F17 F7EED488 FF906EED DB95D041 965CBF04 B0E05609 1B26DB06 843B9DE7` 

- `C : BE6AC9DC 86AFB8BB 300C6C1B 237F0C8C 6DEF5EEF 599CA070 540040F7 EEA985E4 4A5B8375 14A6DD99 E8D207F9 F7187681 326F6930 8BCAAE00 25F4855F 3120BA43` 

- `W : 00000002 00000000` 

- `Hash value (word array):` 

- `H : 14A6DD99 E8D207F9 F7187681 326F6930 8BCAAE00 25F4855F 3120BA43` 

- `Hash value (byte array):` 

- `H : 99 DD A6 14 F9 07 D2 E8 81 76 18 F7 30 69 6F 32 00 AE CA 8B 5F 85 F4 25 43 BA 20 31` 

- **B.4 Intermediate States for Shabal-224 (Message B)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

   - `00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

- `block number = -1 : message block` 

- `M : 000000E0 000000E1 000000E2 000000E3 000000E4 000000E5 000000E6 000000E7 000000E8 000000E9 000000EA 000000EB 000000EC 000000ED 000000EE 000000EF` 

- `block number = -1 : add M to B` 

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 000000E0 000000E1 000000E2 000000E3 000000E4 000000E5 000000E6 000000E7 000000E8 000000E9 000000EA 000000EB 000000EC 000000ED 000000EE 000000EF` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

- `block number = -1 : xor counter W into A` 

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000` 

   - `00000000 00000000 00000000 00000000` 

- `B : 000000E0 000000E1 000000E2 000000E3 000000E4 000000E5 000000E6 000000E7 000000E8 000000E9 000000EA 000000EB 000000EC 000000ED 000000EE 000000EF` 

198 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 01C00000 01C20000 01C40000 01C60000 01C80000 01CA0000 01CC0000 01CE0000 01D00000 01D20000 01D40000 01D60000 01D80000 01DA0000 01DC0000 01DE0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=0)
```

- `A : E0F553CA 360FB9F0 13F563A2 1751BF18 97E7BD38 130C3A22 98E64161 83D3B87F F2FB6BE4 D594E9DE 8CA0C9A1 E61F0AC1` 

- `B : 024800E2 FB28F276 182C49FA 2B1FCF5D 6B8842C7 EF67C5DD 6481BE9E 7FB04780 0EA4941B 29CF1621 70F7365E 1A4CF53E 1CBAAC35 CA44460F EFB29C5D EB1240E7` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : 257C1CF3 FAC54BC3 B544997B B9426917 594FC7A1 D13345E4 17044F51 13DC1230 4D00378B E315C946 A6A4D823 AE0E1AAC` 

- `B : 67772EA5 A9D983AA 1B7E3DF8 B711623E 65EF4DFA C225BD02 90585AE0 AE916A53 C7CACB3A 56A4987E AB550A38 72247C94 9FC56034 BA443604 379E8815 3A076C00` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

199 

- `B : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

###### `block number = -1 : subtract M from C` 

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `C : FFFFFF20 FFFFFF1F FFFFFF1E FFFFFF1D FFFFFF1C FFFFFF1B FFFFFF1A FFFFFF19 FFFFFF18 FFFFFF17 FFFFFF16 FFFFFF15 FFFFFF14 FFFFFF13 FFFFFF12 FFFFFF11` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : FFFFFF20 FFFFFF1F FFFFFF1E FFFFFF1D FFFFFF1C FFFFFF1B FFFFFF1A FFFFFF19 FFFFFF18 FFFFFF17 FFFFFF16 FFFFFF15 FFFFFF14 FFFFFF13 FFFFFF12 FFFFFF11` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : FFFFFF20 FFFFFF1F FFFFFF1E FFFFFF1D FFFFFF1C FFFFFF1B FFFFFF1A FFFFFF19 FFFFFF18 FFFFFF17 FFFFFF16 FFFFFF15 FFFFFF14 FFFFFF13 FFFFFF12 FFFFFF11` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:messageblock
```

- `M : 000000F0 000000F1 000000F2 000000F3 000000F4 000000F5 000000F6 000000F7 000000F8 000000F9 000000FA 000000FB 000000FC 000000FD 000000FE 000000FF` 

```
blocknumber=0:addMtoB
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

200 

###### `W : 00000000 00000000` 

```
blocknumber=0:xorcounterWintoA
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-rotateB
```

- `A : 01340BD4 73381D1D F97F7508 28F07BF4 8E842C24 D8A8596F D2D4F99A D0763C3C 632406CB 965BA4DD 014EB6D9 3E7F3B64` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=0)
```

- `A : 4389B954 7C2E65DF 7AC0A60E 4D3E5671 7E2ECC0C 30113495 2288EF2A DA590830 F8F8D0FD 866100F7 129EA35A B74146B4` 

- `B : 3D7D89CC 64237EF2 265812A5 119D3DC4 819133F3 CFAECB6A DD3710D5 25E6F7CF 07472F02 79DEFF08 ED215CA5 48FEB94B BC3646AB 83919A20 857F59F1 B281A98E` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : E11D69E6 69E4164B 0FC5373C 7E495272 A8B9B043 8CDC5330 90551180 5E5046D9 9EB4F2BE E6580BF7 E5386C60 AD2654AD` 

- `B : 2CCEC394 1350B7FB 8F6F4688 88CED426 62696AA6 86FA62DD A0A9B234 191444CC 106CC81D 65A617A4 2A787188 104BDF1B 2F2AC2EB 7400988E 65545D9C C4ACEA3B` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : 01F5E756 E4B92946 BCFDB7C5 EFD3BD7F 466630E8 D1059816 DBA401AC 7E64640B B75BD62C 2F4525B5 AE5698A7 C7AF460B` 

- `B : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

201 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

```
W:0000000000000000
```

```
blocknumber=0:permutation-addCtoA
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : EC9906C8 F21851C0 C0A747BA 21DAD58B 35156FDF 088C98E7 26303F36 8A2D50AC FEEE45AE 8A1E966C 7B811214 CBC13AEB A351395D 1D2C372B 918C590C B58E1C9B` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `C : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : EC9905D8 F21850CF C0A746C8 21DAD498 35156EEB 088C97F2 26303E40 8A2D4FB5 FEEE44B6 8A1E9573 7B81111A CBC139F0 A3513861 1D2C362E 918C580E B58E1B9C` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 302D7A79 34333231 38373635 42412D39 46454443 4A494847 4E4D4C4B 5251504F 56555453 5A595857` 

202 

```
blocknumber=1:addMtoB
```

- `A : A5201467 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : 50FC6839 5A7FB734 2D12B131 924A4305 A988E15C 81040E67 565DB8B9 BE6081E6 37257AEB CC5FC2AC C1C6555D 160A8237 F19E84AC 6F7D867D E7E1AC61 0FE773F3` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:xorcounterWintoA
```

- `A : A5201466 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : 50FC6839 5A7FB734 2D12B131 924A4305 A988E15C 81040E67 565DB8B9 BE6081E6 37257AEB CC5FC2AC C1C6555D 160A8237 F19E84AC 6F7D867D E7E1AC61 0FE773F3` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : A5201466 A9B8D94A D4CED997 68379D7B A7FC73BA F1A2546B 606782BF E0BCFD0F 2F25374E 069A149F 5E2DFF25 FAECF061` 

- `B : D072A1F8 6E68B4FF 62625A25 860B2494 C2B95311 1CCF0208 7172ACBB 03CD7CC1 F5D66E4A 855998BF AABB838C 046E2C15 0959E33D 0CFADEFB 58C3CFC3 E7E61FCE` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=0)
```

- `A : 8C6560B6 46C63757 88C69A25 846FFE84 1D1CEFD6 5FBEA9B1 F659B29C 772D12C6 30C10360 06A31BE8 EB368AA8 A21F7FDF` 

- `B : 9E34389F F9C9ED48 97683AF6 A4B76138 6791B60A 99DF525E EB431415 8F4814BB 2492200A F3EFD568 41BE724E 553CD80A 61295933 A0CC755E C6BEFA5C B45C3EE6` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : 23BBE3D7 CE453E25 7DE78C6F B5F31A7C A0A64F86 D1CB5DB0 2B5C3669 CEC91EF6 714AD2A9 81CCD639 04DD0E5F C30C0B39` 

- `B : 7FD3AB2F 8844471A 5EB7789C 06DFC577 41964142 4D8D8D7B 2DA4D98B 2263DDB1 95605C3C D6656B0B 0164970C E0755597 9D0B021F 6FAC48F2 59DE3D2F 598E9CC4` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18` 

203 

```
99405F2DE5B648A170AB1D43A10C25C216F1AC0538BBEB569B01DC60B1096D83
```

```
W:0000000100000000
```

```
blocknumber=1:permutation(j=2)
```

- `A : 75457F4C CFC19617 D104D673 18ACCC64 0588C3A0 0AD46F0E 002D5D7B 45ACAD09 33CE4C17 D042FCFB A1390D75 FDA502E4` 

- `B : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : CBDB918E 064183A2 6C8CDD4B D4905168 DD177B38 C3A30FC1 48AFC19E D73972F0 FB5FBBEE BB4DD612 D65D546E 0BA328DA` 

- `B : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `C : E4B573A1 4C1A0880 1E907C51 04807EFD 3AD8CDE5 16B21302 02512C53 2204CB18 99405F2D E5B648A1 70AB1D43 A10C25C2 16F1AC05 38BBEB56 9B01DC60 B1096D83` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : CBDB918E 064183A2 6C8CDD4B D4905168 DD177B38 C3A30FC1 48AFC19E D73972F0 FB5FBBEE BB4DD612 D65D546E 0BA328DA` 

- `B : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `C : 80521140 E3B2A21B B22511E8 94111090 C6655B74 9E3A9C8D D223B1DA EDD198E7 610928F8 A3751B68 2A65D900 56C2DD7B C8A45FBA E66A9B07 44AC880D 56B0152C` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : CBDB918E 064183A2 6C8CDD4B D4905168 DD177B38 C3A30FC1 48AFC19E D73972F0 FB5FBBEE BB4DD612 D65D546E 0BA328DA` 

- `B : 80521140 E3B2A21B B22511E8 94111090 C6655B74 9E3A9C8D D223B1DA EDD198E7 610928F8 A3751B68 2A65D900 56C2DD7B C8A45FBA E66A9B07 44AC880D 56B0152C` 

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : CBDB918E 064183A2 6C8CDD4B D4905168 DD177B38 C3A30FC1 48AFC19E D73972F0 FB5FBBEE BB4DD612 D65D546E 0BA328DA` 

- `B : 80521140 E3B2A21B B22511E8 94111090 C6655B74 9E3A9C8D D223B1DA EDD198E7` 

204 

```
610928F8A3751B682A65D90056C2DD7BC8A45FBAE66A9B0744AC880D56B0152C
```

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 3231302D 36353433 2D393837 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 00807A79 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : CBDB918E 064183A2 6C8CDD4B D4905168 DD177B38 C3A30FC1 48AFC19E D73972F0 FB5FBBEE BB4DD612 D65D546E 0BA328DA` 

- `B : B283416D 19E7D64E DF5E4A1F F87472F1 2ECCC1D9 0AA606F6 42932047 62450B58 D9809F6D A3F595E1 2A65D900 56C2DD7B C8A45FBA E66A9B07 44AC880D 56B0152C` 

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000002 00000000` 

```
blocknumber=2:xorcounterWintoA
```

- `A : CBDB918C 064183A2 6C8CDD4B D4905168 DD177B38 C3A30FC1 48AFC19E D73972F0 FB5FBBEE BB4DD612 D65D546E 0BA328DA` 

- `B : B283416D 19E7D64E DF5E4A1F F87472F1 2ECCC1D9 0AA606F6 42932047 62450B58 D9809F6D A3F595E1 2A65D900 56C2DD7B C8A45FBA E66A9B07 44AC880D 56B0152C` 

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : CBDB918C 064183A2 6C8CDD4B D4905168 DD177B38 C3A30FC1 48AFC19E D73972F0 FB5FBBEE BB4DD612 D65D546E 0BA328DA` 

- `B : 82DB6506 AC9C33CF 943FBEBC E5E3F0E8 83B25D99 0DEC154C 408E8526 16B0C48A 3EDBB301 2BC347EB B20054CB BAF6AD85 BF759148 360FCCD5 101A8959 2A58AD60` 

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : DF1A97E9 D6B1A782 D96A6348 DA9DAC23 5E46C0AF 6CB06C45 1A6C68C6 AA007071 9CFAB7D5 B45EA5D2 C44B5068 28B35FE0` 

- `B : 22D191FE 9F37773E BEC49E4E 4E7E0DA5 A6DD8463 8897B922 648E9D75 789E069A 1EB22E28 1C27D5FB 5FB40600 A2A1FB14 5E0E4A87 4551C1D7 06A08E05 71D3091C` 

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

205 

```
W:0000000200000000
```

```
blocknumber=2:permutation(j=1)
```

- `A : 3B44212B 38BAA6B1 DDAE09FA FA7EAC58 7DC6ACAB B9D314C2 E29E3349 BF392F25 2684E514 E7DD225E 9F9F888E 276E49D7` 

- `B : 34E7DF5E 23C3AAF3 4F5BF5EE 6A40590D 94C0122C 090DAFE4 A97D4D9B 29ADBB1C F9DF8284 FF0AF2B8 9D39FA05 40C2A58E 3E25C65A CC8F6893 1020D0BC A360C2E2` 

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : 77A014BC EEA36A0D 3771AF76 CEBD1EF8 72060B53 F42159D8 2669B358 F1D02FEC 912B7E1F F21D9DC4 1E589CD0 1B1EF3E6` 

- `B : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : C0EA29F8 985D617D 83266CB1 22BE3C02 E42AAFAF 786B1D97 DB1A2499 557250BE CCC257C1 C292DBF8 1444E9B4 7B67A3F0` 

- `B : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `C : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : C0EA29F8 985D617D 83266CB1 22BE3C02 E42AAFAF 786B1D97 DB1A2499 557250BE CCC257C1 C292DBF8 1444E9B4 7B67A3F0` 

- `B : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `C : 77CB0D35 7974830A C39AC165 B8E4F46F A12E9BD2 3EBA08B5 05432C2D 2F211688 58400DB1 5960CC6D FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : C0EA29F8 985D617D 83266CB1 22BE3C02 E42AAFAF 786B1D97 DB1A2499 557250BE CCC257C1 C292DBF8 1444E9B4 7B67A3F0` 

- `B : 77CB0D35 7974830A C39AC165 B8E4F46F A12E9BD2 3EBA08B5 05432C2D 2F211688 58400DB1 5960CC6D FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

206 

- `C : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

```
W:0000000200000000
```

- `n0_final = 0 : add M to B` 

- `A : C0EA29F8 985D617D 83266CB1 22BE3C02 E42AAFAF 786B1D97 DB1A2499 557250BE CCC257C1 C292DBF8 1444E9B4 7B67A3F0` 

- `B : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `C : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `W : 00000002 00000000` 

```
n0_final=0:xorcounterWintoA
```

- `A : C0EA29FA 985D617D 83266CB1 22BE3C02 E42AAFAF 786B1D97 DB1A2499 557250BE CCC257C1 C292DBF8 1444E9B4 7B67A3F0` 

- `B : A9FC3D62 AFA9B73D F0D3F99C 1D4856D0 09960237 AB25731E 75B29A9A A39488F9 D0B78426 59E146E6 FD1B8C9C 7AB9F9D9 F627B7D7 F0E592E0 ED7A88D4 B147C493` 

- `C : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : C0EA29FA 985D617D 83266CB1 22BE3C02 E42AAFAF 786B1D97 DB1A2499 557250BE CCC257C1 C292DBF8 1444E9B4 7B67A3F0` 

- `B : 7AC553F8 6E7B5F53 F339E1A7 ADA03A90 046E132C E63D564A 3534EB65 11F34729 084DA16F 8DCCB3C2 1939FA37 F3B2F573 6FAFEC4F 25C1E1CB 11A9DAF5 8927628F` 

- `C : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

- `A : B06DABA1 C2FAAF6C D26BD04A C346339C 401C0339 4E95BA16 FF3D20E2 01CC9798 E76A4A83 C859C1C9 D418DB48 FC04E5DE` 

- `B : 632C5D0B 68F2C4D3 338162E2 1F4E24CB B73FDA9E 7D10E97C 6AAB09D7 DDD5E635 080EF7A2 2C3F59B3 1994D0D9 E49EF0C6 90CD8CC0 76869305 0EC79A5F 2EF7097C` 

- `C : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : 90072ACB 3ECE3BEB D37570FA D6B90896 3A5BD5E8 AD157A12 62B0A0BE 533EBFC2 740AC54E 5933F890 9A93B77C 3D826737` 

207 

- `B : 4713E6F8 279E7D3C 14037EF6 79738F3B E58A8F8C 5CEDD597 B03A5B2D 79D654A3 7FE53A70 994F7772 1FA32EB7 E07B16E4 E43F3396 BFE7A3E7 80C06BFF F12F52C5` 

- `C : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

- `A : 08247C8E 390FEFE8 11B58153 9D1A521A 4DA938A6 85400B12 BF219BD8 3A0F40D3 680284AD 94558929 1B7BE1CC 9F38E8DE` 

- `B : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `C : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : 653350DB 22D9E2BD FCC5977E CA0FA236 7D270923 DAB1E238 0B00423D 89038744 850A665D C71B573C A98BA278 DF7A2F9F` 

- `B : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `C : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `W : 00000002 00000000` 

- `n0_final = 0 : subtract M from C` 

- `A : 653350DB 22D9E2BD FCC5977E CA0FA236 7D270923 DAB1E238 0B00423D 89038744 850A665D C71B573C A98BA278 DF7A2F9F` 

- `B : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `C : 0319E63A 1C9664A2 A36089D0 C6E04D01 397868B5 96DC5FD1 2A055D51 EDA624CE 05CF7B30 F54AC8DD E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `W : 00000002 00000000` 

```
n0_final=0:swapBwithC
```

- `A : 653350DB 22D9E2BD FCC5977E CA0FA236 7D270923 DAB1E238 0B00423D 89038744 850A665D C71B573C A98BA278 DF7A2F9F` 

- `B : 0319E63A 1C9664A2 A36089D0 C6E04D01 397868B5 96DC5FD1 2A055D51 EDA624CE 05CF7B30 F54AC8DD E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `C : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

208 

- `A : 653350DB 22D9E2BD FCC5977E CA0FA236 7D270923 DAB1E238 0B00423D 89038744 850A665D C71B573C A98BA278 DF7A2F9F` 

- `B : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `C : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

- `n0_final = 1 : xor counter W into A` 

- `A : 653350D9 22D9E2BD FCC5977E CA0FA236 7D270923 DAB1E238 0B00423D 89038744 850A665D C71B573C A98BA278 DF7A2F9F` 

- `B : 354B1667 52CB98D5 D099C207 2B43AF62 A1DFCF1A 0347CA3A 9A74CBBE 6219973F 7E46F1A5 F5CB4356 E3E5B8AC 8FAA9B0F 129F0D54 94FCB31C C1E6C257 A22089DC` 

- `C : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

- `A : 653350D9 22D9E2BD FCC5977E CA0FA236 7D270923 DAB1E238 0B00423D 89038744 850A665D C71B573C A98BA278 DF7A2F9F` 

- `B : 2CCE6A96 31AAA597 840FA133 5EC45687 9E3543BF 9474068F 977D34E9 2E7EC433 E34AFC8D 86ADEB96 7159C7CB 361F1F55 1AA8253E 663929F9 84AF83CD 13B94441` 

- `C : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : 60E8E576 316FE540 8A0B25AB 162A5B42 E6D7E5C1 6359F3DE 1F4EC558 E1651DB6 9749184B 8137C54B 27C916A6 D0E26E39` 

- `B : EC0B1162 0B3294A9 B6F7B2E1 E8BE96F2 25429D41 B44E013E CE4B5374 42676A2F AE231EAF 7393ED99 3A8566CF 4323AF6C AA4750F5 02E2494D 7CABDDCF CEA72C3F` 

- `C : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

- `A : 86790693 8A20F14E 300DC8BB 62D4566C A37F1C26 180D8571 D72EB4D2 9E6B3933 96B721ED BE48220A A21A0633 E6DF78B8` 

- `B : C8E12BE0 4A1ED32A E5676F5B 7920AF87 23CDE490 292BDF88 C1735F25 9DEE5319 25C0C433 92F8D583 BAF8FADA 1B6CF74B 080E4232 E236E814 D186F0B3 FCDA9EB3` 

- `C : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

209 

```
n0_final=1:permutation(j=2)
```

- `A : 7B677F6B 9264B604 1122E95A DA5BF2F1 A9924516 CC1A2335 2BDCF160 2A950BAF 4B8F21E4 F6726F41 A14A2B78 0C3AABCB` 

- `B : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `C : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - add C to A` 

- `A : 0FA9DF5F B8EC9A32 B0F714D7 8ACEF497 CA1716C8 E0BB9E9D FF6D05CC 759B7CD2 EE80D3D1 E060DBE1 7CFC31D2 FF1677D7` 

- `B : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `C : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

- `n0_final = 1 : subtract M from C` 

- `A : 0FA9DF5F B8EC9A32 B0F714D7 8ACEF497 CA1716C8 E0BB9E9D FF6D05CC 759B7CD2 EE80D3D1 E060DBE1 7CFC31D2 FF1677D7` 

- `B : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `C : 5804FB1A D60E0AF8 0FF636AC A83EB804 D4673603 12C050D0 1DCF5A8A 1CD59232 D5253D44 47A09F8F 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `W : 00000002 00000000` 

- `n0_final = 1 : swap B with C` 

- `A : 0FA9DF5F B8EC9A32 B0F714D7 8ACEF497 CA1716C8 E0BB9E9D FF6D05CC 759B7CD2 EE80D3D1 E060DBE1 7CFC31D2 FF1677D7` 

- `B : 5804FB1A D60E0AF8 0FF636AC A83EB804 D4673603 12C050D0 1DCF5A8A 1CD59232 D5253D44 47A09F8F 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `C : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `W : 00000002 00000000` 

```
n0_final=2:addMtoB
```

- `A : 0FA9DF5F B8EC9A32 B0F714D7 8ACEF497 CA1716C8 E0BB9E9D FF6D05CC 759B7CD2 EE80D3D1 E060DBE1 7CFC31D2 FF1677D7` 

- `B : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `C : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

210 

###### `W : 00000002 00000000` 

```
n0_final=2:xorcounterWintoA
```

- `A : 0FA9DF5D B8EC9A32 B0F714D7 8ACEF497 CA1716C8 E0BB9E9D FF6D05CC 759B7CD2 EE80D3D1 E060DBE1 7CFC31D2 FF1677D7` 

- `B : 8A362B47 0C433F2B 3D2F6EE3 0CA21A65 3CCE9C68 7F2BBB39 8E3EC8F7 914904A3 4D9CB3B9 48211A08 7F983949 050692E5 5F831C7F 14653119 E504C9CC 8299B2AA` 

- `C : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - rotate B` 

- `A : 0FA9DF5D B8EC9A32 B0F714D7 8ACEF497 CA1716C8 E0BB9E9D FF6D05CC 759B7CD2 EE80D3D1 E060DBE1 7CFC31D2 FF1677D7` 

- `B : 568F146C 7E561886 DDC67A5E 34CA1944 38D0799D 7672FE57 91EF1C7D 09472292 67729B39 34109042 7292FF30 25CA0A0D 38FEBF06 623228CA 9399CA09 65550533` 

- `C : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 0)` 

- `A : 10DC5597 4EB0AB2A E9391D54 5A2C8304 10B0B326 F153EAD7 01430C09 05F436D0 D7CD5D60 C56766D0 BC7937FC CB9FAB2A` 

- `B : 8B687EED 78A26178 B2A72BE1 DC5D3CB5 9EEFBFE3 E249E986 DD62CB0D E8858C0B E6D794ED 52B9B9AB A6A33663 7FF440CF 9EDED464 752B0541 31F576B8 6F79769D` 

- `C : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : 5E74B6C5 5E7772C8 FAA3B326 84A173D3 024DBC7D 25724599 7EA4A347 8633B5DC 70ECC490 DE3DC78E BFC0E264 E9260137` 

- `B : 4C2F25BF ABD255DA 039D8ABD A63E3971 B2CC44A8 E551EB7C FAFA8B80 C7D2E6DF 6C2460E1 04FBFE61 481A201E 84B60DB2 C00FEB4B 30DBB0E4 E2B1B1C8 A73EA719` 

- `C : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : CF452790 81296D85 8776EBA0 E26CDAAE 1DA6D373 7B25D5FA DBBF8BE9 EC424D6E 3CDDF23A 51106F6C 6CC1D02B 44A7C0D1` 

- `B : E3BD6C0F E3B4A56E E9349EB2 29739374 5522513E B4754483 8D7C035E 9236E8EE 3A11ED4E 8D2DD6C7 B474342A 1AD1A9F4 433DDB52 CF58F15B 565D4C45 F525711D` 

211 

- `C : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

```
W:0000000200000000
```

- `n0_final = 2 : permutation - add C to A` 

- `A : 894924F9 B9663D4A 3211E95C E3077A9D 12706153 2CE27DCF CE8EC0DB 90F7B2A7 0AEA318D D66C462E 90837F7A 506E9AC9` 

- `B : E3BD6C0F E3B4A56E E9349EB2 29739374 5522513E B4754483 8D7C035E 9236E8EE 3A11ED4E 8D2DD6C7 B474342A 1AD1A9F4 433DDB52 CF58F15B 565D4C45 F525711D` 

- `C : D0CD2B92 9CEDC63A 96A6C121 CBE07950 C30349B4 3FCCF6EB 6C3BA8EE 1E78AB3D 1DEC328F 161477CD A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : 894924F9 B9663D4A 3211E95C E3077A9D 12706153 2CE27DCF CE8EC0DB 90F7B2A7 0AEA318D D66C462E 90837F7A 506E9AC9` 

- `B : E3BD6C0F E3B4A56E E9349EB2 29739374 5522513E B4754483 8D7C035E 9236E8EE 3A11ED4E 8D2DD6C7 B474342A 1AD1A9F4 433DDB52 CF58F15B 565D4C45 F525711D` 

- `C : 9E9BFB65 66B89207 696D88EA 677D16EF 5A9BE34F D3618C82 FBCC3A81 AA0538CC A574BC1A 1593FD54 A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : 894924F9 B9663D4A 3211E95C E3077A9D 12706153 2CE27DCF CE8EC0DB 90F7B2A7 0AEA318D D66C462E 90837F7A 506E9AC9` 

- `B : 9E9BFB65 66B89207 696D88EA 677D16EF 5A9BE34F D3618C82 FBCC3A81 AA0538CC A574BC1A 1593FD54 A1D2FB2A E3B31AC6 A46C5A7F CDE04097 FDB835E0 0A706953` 

- `C : E3BD6C0F E3B4A56E E9349EB2 29739374 5522513E B4754483 8D7C035E 9236E8EE 3A11ED4E 8D2DD6C7 B474342A 1AD1A9F4 433DDB52 CF58F15B 565D4C45 F525711D` 

- `W : 00000002 00000000` 

```
Hashvalue:
```

- `H : 8D2DD6C7 B474342A 1AD1A9F4 433DDB52 CF58F15B 565D4C45 F525711D` 

```
Hashvalue(bytearray):
```

- `H : C7 D6 2D 8D 2A 34 74 B4 F4 A9 D1 1A 52 DB 3D 43 5B F1 58 CF 45 4C 5D 56 1D 71 25 F5` 

### **B.5 Intermediate States for Shabal-256 (Message A)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

212 

```
00000000000000000000000000000000
```

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:messageblock
```

- `M : 00000100 00000101 00000102 00000103 00000104 00000105 00000106 00000107 00000108 00000109 0000010A 0000010B 0000010C 0000010D 0000010E 0000010F` 

```
blocknumber=-1:addMtoB
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000100 00000101 00000102 00000103 00000104 00000105 00000106 00000107 00000108 00000109 0000010A 0000010B 0000010C 0000010D 0000010E 0000010F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:xorcounterWintoA
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000100 00000101 00000102 00000103 00000104 00000105 00000106 00000107 00000108 00000109 0000010A 0000010B 0000010C 0000010D 0000010E 0000010F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 02000000 02020000 02040000 02060000 02080000 020A0000 020C0000 020E0000 02100000 02120000 02140000 02160000 02180000 021A0000 021C0000 021E0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=0)
```

- `A : AE3F47E2 C68A60D9 C63E700C 04FB82A0 8088FEAE 64D8954B CC08DF9F F2497B68 7EC08316 F007C07B BBB8A77D 6C368247` 

- `B : 06080102 FE78F1B6 12CC57B2 93BBAACD 7B670151 9F336AB4 37EF2060 09AA8497 851F7CE9 0BDC3F84 406F5882 97E57DB8 55F0B81D 3D419F26 3DF98FF3 FF387D5F` 

213 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : FF750C93 E5788A46 9BBD7565 CC341456 AD7FFC12 CE83FA1C 6511FD37 E0E9DCD1 A72272C9 B2929B0B 78EE6F01 C3B82A6F` 

- `B : 14F4A4C4 CDE737FE 5675BD47 7A96E075 AE138F94 730BB19D E8CFD03E 2F12DCBE 0AB40ABF 0D3F0AB1 E49C3B9E 1C0110D8 F96173D7 4BFF3BAF E11D1D2E E166D991` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:subtractMfromC
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `C : FFFFFF00 FFFFFEFF FFFFFEFE FFFFFEFD FFFFFEFC FFFFFEFB FFFFFEFA FFFFFEF9 FFFFFEF8 FFFFFEF7 FFFFFEF6 FFFFFEF5 FFFFFEF4 FFFFFEF3 FFFFFEF2 FFFFFEF1` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

214 

- `B : FFFFFF00 FFFFFEFF FFFFFEFE FFFFFEFD FFFFFEFC FFFFFEFB FFFFFEFA FFFFFEF9 FFFFFEF8 FFFFFEF7 FFFFFEF6 FFFFFEF5 FFFFFEF4 FFFFFEF3 FFFFFEF2 FFFFFEF1` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : FFFFFF00 FFFFFEFF FFFFFEFE FFFFFEFD FFFFFEFC FFFFFEFB FFFFFEFA FFFFFEF9 FFFFFEF8 FFFFFEF7 FFFFFEF6 FFFFFEF5 FFFFFEF4 FFFFFEF3 FFFFFEF2 FFFFFEF1` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:messageblock
```

- `M : 00000110 00000111 00000112 00000113 00000114 00000115 00000116 00000117 00000118 00000119 0000011A 0000011B 0000011C 0000011D 0000011E 0000011F` 

```
blocknumber=0:addMtoB
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:xorcounterWintoA
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-rotateB
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

215 

###### `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=0)
```

- `A : 7F0490C3 946910EC 827CA63E 409A1072 2B03CF2C FED97162 7F90F2B4 4069B7E1 CCB74C96 09778D59 6B24AB90 80A11478` 

- `B : AA98C924 A5880F94 19DB44E2 61A3149F D4BC30D3 01668E9D 802F0D4B BFD6481E 3308B369 F6C872A6 949B546F 7F1EEB87 80BB6F3C 6BD6EF13 7DC359C1 BF25EF8D` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : D455C979 9F6F4358 7F3D0246 E8A1F260 BE9C04EA 15A315D0 279AC5A8 1C34F0F3 10A66C48 D8CCDB49 02B680C7 AB645FCF` 

- `B : 5923FD91 9DEBD978 66452E00 8510F1DD 4621F210 25FE398C FD1765AF 2B37300D 4DBB5054 8D0059EA A9F45566 E963DA91 4015256C 3DF13409 23E389D5 9D80D017` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : B6A03371 17243406 531455C7 44F0DBD6 EC3CC237 851D8290 D99C1EB9 AED060A3 C3433D0F 62FD9C1A 02BB7200 5FB743B0` 

- `B : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-addCtoA
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

216 

- `C : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

```
W:0000000000000000
```

```
blocknumber=0:swapBwithC
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=1:addMtoB
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:xorcounterWintoA
```

- `A : 52F84553 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

217 

```
blocknumber=1:permutation-rotateB
```

- `A : 52F84553 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : 8DDD6AAB 0B2C7CE2 CA5F4E54 A2BF2602 83F5B451 B0D0D2DF 7EE5396D 800415FC 6C2B4DC0 83A8A271 C60D7C42 11216717 72D67D51 59C86533 9BA86124 694AAB96` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=0)
```

- `A : 6C7E9B27 87B2F2E5 31E5DEFF 6942E14C BEB25D8B 33D83C6D 90F3CDCD 21D06696 2FE614D9 3D0961C9 CD249DAA 9B2F0544` 

- `B : 8DE67622 7A56AE20 0E25B32E 7D7CA4C6 46A6CAD7 AD86662D 92C640E8 DE27B290 084F70A6 C5A7DAD5 BEC19AD0 46923495 762D9E7A CBDDC77C F94AE349 4428499F` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : D154BCD2 8029A7A8 BD8F33D3 8C8CB879 0EDFB793 F99B963E 9CA7B797 384AA841 6E902BE0 DC3FF5DA 84C2EC43 0CEC8961` 

- `B : 656519B9 85CD79AD D4468C4E 4E1F2B1E 1C2241B1 78CCC67E 5EB1926D 4F5C13BF 3E35A261 F499EDFC 3FF3F98D FE572EAC 1D7B7498 91DFE738 91CD8EFB 4FE5C480` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : 6F764332 149C2AD3 D6586B4D 242A0474 491260B1 8EF3ADBF 5C1C3969 11CF9D58 4854D811 FAC675BA BA5C2B36 13DC2FD0` 

- `B : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : 4F852766 4A54CBDA 24836EDF E8E63DA9 929A5E99 90CB63FE 2449FFBE 919383C3 7A7BE418 052EC3F0 A546BEC8 9AB07B17` 

- `B : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433` 

218 

```
88B59D6060E2CEBA758B4B8B83E82A7FBC968828E6E00BF7BA839E559B491C60
```

```
W:0000000100000000
```

```
blocknumber=1:subtractMfromC
```

- `A : 4F852766 4A54CBDA 24836EDF E8E63DA9 929A5E99 90CB63FE 2449FFBE 919383C3 7A7BE418 052EC3F0 A546BEC8 9AB07B17` 

- `B : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : 4F852766 4A54CBDA 24836EDF E8E63DA9 929A5E99 90CB63FE 2449FFBE 919383C3 7A7BE418 052EC3F0 A546BEC8 9AB07B17` 

- `B : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : 4F852766 4A54CBDA 24836EDF E8E63DA9 929A5E99 90CB63FE 2449FFBE 919383C3 7A7BE418 052EC3F0 A546BEC8 9AB07B17` 

- `B : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 00000080 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : 4F852766 4A54CBDA 24836EDF E8E63DA9 929A5E99 90CB63FE 2449FFBE 919383C3 7A7BE418 052EC3F0 A546BEC8 9AB07B17` 

- `B : B405F0B1 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000002 00000000` 

219 

```
blocknumber=2:xorcounterWintoA
```

- `A : 4F852764 4A54CBDA 24836EDF E8E63DA9 929A5E99 90CB63FE 2449FFBE 919383C3 7A7BE418 052EC3F0 A546BEC8 9AB07B17` 

- `B : B405F0B1 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : 4F852764 4A54CBDA 24836EDF E8E63DA9 929A5E99 90CB63FE 2449FFBE 919383C3 7A7BE418 052EC3F0 A546BEC8 9AB07B17` 

- `B : E163680B 7D758846 72F366E6 3AAB81BB 515D8A38 71C3464F C2CEAD8A 8867DAC2 3AC1116B 9D74C1C5 9716EB16 54FF07D0 1051792D 17EFCDC0 3CAB7507 38C13692` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : 47280149 E0472C08 4C728C37 96F8D4EA 12DDB762 FCA64123 B97C739F 792DA29A 2E65DDAA D6DBED1F 4D3A2665 00F33A7D` 

- `B : 13CC581D C0361D87 AB8A9517 E2320200 4F995CED E0DF3242 C31ED775 961DE8E0 A4180083 13CD916B 9CE80FB7 56F2CA22 98750CEC 30674877 CADB99C6 18854631` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=1)
```

- `A : 774A249D EBA2B79B E65FFD6E DD6651EA 7CD9B57D 0F492665 368BCCC9 36F9F21E 9BABB0B8 69550AAF ED7CDA53 95787B45` 

- `B : 9CF247BE 3B5779CD 3F68E196 8B6F3469 FB66F69D 571491D5 94BE8B47 46BC557B C085DA65 33C66AB2 20701DFE 8F7C3A51 B3CC535B 90784974 5CC300BB F80C8183` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : 05F99A5A 361D65F4 FFFBD130 CD7FEDF4 232C8A7D 59E6C9C8 48671625 AC36413E 0DF498ED 2BD35EEB CF993C21 E244DA6C` 

- `B : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

220 

###### `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : 3187F450 2FBEDD0F 1889D7EF 68879728 818A816A 90B14D91 D2AE6269 BD0956C0 0B0876A9 2C854904 A95963DE B946899E` 

- `B : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `C : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : 3187F450 2FBEDD0F 1889D7EF 68879728 818A816A 90B14D91 D2AE6269 BD0956C0 0B0876A9 2C854904 A95963DE B946899E` 

- `B : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `C : C376680E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : 3187F450 2FBEDD0F 1889D7EF 68879728 818A816A 90B14D91 D2AE6269 BD0956C0 0B0876A9 2C854904 A95963DE B946899E` 

- `B : C376680E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `C : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

- `n0_final = 0 : add M to B` 

- `A : 3187F450 2FBEDD0F 1889D7EF 68879728 818A816A 90B14D91 D2AE6269 BD0956C0 0B0876A9 2C854904 A95963DE B946899E` 

- `B : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

- `C : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

- `n0_final = 0 : xor counter W into A` 

- `A : 3187F452 2FBEDD0F 1889D7EF 68879728 818A816A 90B14D91 D2AE6269 BD0956C0 0B0876A9 2C854904 A95963DE B946899E` 

- `B : C376688E D70D68BB A00A2F8E A507C0C9 A8CD3FAF 1AFA59D0 94C4B068 456DDCF5 CA86DB8C 983F89B9 DC04358C 129E3FFE 8D5DCEDE 26864434 6638C93E 73E8592F` 

221 

- `C : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : 3187F452 2FBEDD0F 1889D7EF 68879728 818A816A 90B14D91 D2AE6269 BD0956C0 0B0876A9 2C854904 A95963DE B946899E` 

- `B : D11D86EC D177AE1A 5F1D4014 81934A0F 7F5F519A B3A035F4 60D12989 B9EA8ADB B719950D 1373307F 6B19B808 7FFC253C 9DBD1ABB 88684D0C 927CCC71 B25EE7D0` 

- `C : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

- `A : 64D53798 30B6E019 E5F13356 422A0182 D89FD7C5 11EF0E93 B713DA4F 9D51A1BF 89102A8C CA86DD00 2C5A70C9 E59682E4` 

- `B : 5A754140 FDD13BE5 D3E842DA 6DE96B95 D9DE8B0E 89509A85 894E76A2 117B4BF7 18DCFF68 139F4201 0596FF26 E5913763 A050FD10 DF9985FF 3EF7544A D96831DC` 

- `C : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : 47DE9969 50A707E4 872B7E5F AE533A8E 84218E27 8A923B0E D74F3A07 F20E2576 09DB05EC 6D7E3C4B 78EF080E 0541AF6D` 

- `B : 1595E3AE 5778E6F4 7BD8C2EA B4E6B380 4599EC0E 8020F6BF 958C1AB4 D848C77C 89989846 88667C19 73F97FEC 9A8EABB6 3B7F8BF9 CA5ECF0E 555E6D6C BF21B930` 

- `C : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

- `A : 9136A866 BA3C98DF 001403F9 D30AC84B 2E00660D 5CC346E5 03D364DB 9390F4E8 3F31482A FD4A8250 B78A73F2 C4476199` 

- `B : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `C : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : E9E7EA9E 2CB3E1F0 7802992D 11B7CB97 F97896E0 977F8F9A 487BA965 3FD607B2 6A391CCB FD828DDC D5C844E3 6F1A2EA7` 

222 

- `B : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `C : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

- `n0_final = 0 : subtract M from C` 

- `A : E9E7EA9E 2CB3E1F0 7802992D 11B7CB97 F97896E0 977F8F9A 487BA965 3FD607B2 6A391CCB FD828DDC D5C844E3 6F1A2EA7` 

- `B : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `C : D017FE4E 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `W : 00000002 00000000` 

```
n0_final=0:swapBwithC
```

- `A : E9E7EA9E 2CB3E1F0 7802992D 11B7CB97 F97896E0 977F8F9A 487BA965 3FD607B2 6A391CCB FD828DDC D5C844E3 6F1A2EA7` 

- `B : D017FE4E 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `C : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

- `A : E9E7EA9E 2CB3E1F0 7802992D 11B7CB97 F97896E0 977F8F9A 487BA965 3FD607B2 6A391CCB FD828DDC D5C844E3 6F1A2EA7` 

- `B : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `C : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `W : 00000002 00000000` 

```
n0_final=1:xorcounterWintoA
```

- `A : E9E7EA9C 2CB3E1F0 7802992D 11B7CB97 F97896E0 977F8F9A 487BA965 3FD607B2 6A391CCB FD828DDC D5C844E3 6F1A2EA7` 

- `B : D017FECE 1B46A796 8B530864 1DDD5142 0CCB889E 67CBB9A1 29793840 BFF8B8FD 5DD8C149 C195E353 F778D226 4D31CA62 9593C1A5 F4DC33FD 89E0C2A8 EDA22694` 

- `C : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

223 

- `A : E9E7EA9C 2CB3E1F0 7802992D 11B7CB97 F97896E0 977F8F9A 487BA965 3FD607B2 6A391CCB FD828DDC D5C844E3 6F1A2EA7` 

- `B : FD9DA02F 4F2C368D 10C916A6 A2843BBA 113C1997 7342CF97 708052F2 71FB7FF1 8292BBB1 C6A7832B A44DEEF1 94C49A63 834B2B27 67FBE9B8 855113C1 4D29DB44` 

- `C : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : 90CAB5E7 8F875CB3 7A5A2121 F5BF07BB 45942608 DD5BB4F9 405C941D BBD9579C 7FDBF0BD F84551D3 D522845D 0EE87DA8` 

- `B : FBBB55F7 0BD7F336 8E2586BB D260690D 9813EAD9 C421D428 5EA3CE06 A7D05781 85017821 8AF5A87B 6246A641 D89EB690 69A31C57 BF8F703C 8F07F95D 90134ECC` 

- `C : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

- `A : D48B50A9 54EA4D22 29DBD192 1EEFCACC D3335894 F7A1F666 EEF7923E 89CDAB95 49461B6D 77D67895 B2A65404 8156AAFF` 

- `B : 0B7C3F51 4009CD8C 3F9857DE 1849F5B6 869E3121 006A2F3B F01E37F7 3109FA03 21765F15 BEFEE22A 12A962EF 502D5812 FF8A9FC5 7740E9E0 0F079F7A 5614C9F3` 

- `C : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

###### `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 2)` 

- `A : 0A2A24C8 F8586095 94E8187F 0096CBFB 89255366 02C67A5E 2CDBC68C 62CF0AE1 6C5402F0 3A43CB77 B61ED7D0 D30D9311` 

- `B : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `C : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `W : 00000002 00000000` 

```
n0_final=1:permutation-addCtoA
```

- `A : 7CA9B247 9E9BEFF7 4EE4A592 FE5650B3 3E973DB8 B5A71318 04BFB116 99A39DC0 353C5DB5 993EA4A2 459A870A A6A91851` 

- `B : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `C : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `W : 00000002 00000000` 

224 

```
n0_final=1:subtractMfromC
```

- `A : 7CA9B247 9E9BEFF7 4EE4A592 FE5650B3 3E973DB8 B5A71318 04BFB116 99A39DC0 353C5DB5 993EA4A2 459A870A A6A91851` 

- `B : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `C : 0A175F36 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `W : 00000002 00000000` 

```
n0_final=1:swapBwithC
```

- `A : 7CA9B247 9E9BEFF7 4EE4A592 FE5650B3 3E973DB8 B5A71318 04BFB116 99A39DC0 353C5DB5 993EA4A2 459A870A A6A91851` 

- `B : 0A175F36 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `C : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `W : 00000002 00000000` 

```
n0_final=2:addMtoB
```

- `A : 7CA9B247 9E9BEFF7 4EE4A592 FE5650B3 3E973DB8 B5A71318 04BFB116 99A39DC0 353C5DB5 993EA4A2 459A870A A6A91851` 

- `B : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `C : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `W : 00000002 00000000` 

- `n0_final = 2 : xor counter W into A` 

- `A : 7CA9B245 9E9BEFF7 4EE4A592 FE5650B3 3E973DB8 B5A71318 04BFB116 99A39DC0 353C5DB5 993EA4A2 459A870A A6A91851` 

- `B : 0A175FB6 DE711F02 46026474 D31144FE E5FA8F85 45828A5F D4F3C96F 9C64B94D C2CEA97F B3F04129 1BDE64FC 59725C7A B631A027 9608E3B2 E2C956D5 45FBEC07` 

- `C : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - rotate B` 

- `A : 7CA9B245 9E9BEFF7 4EE4A592 FE5650B3 3E973DB8 B5A71318 04BFB116 99A39DC0 353C5DB5 993EA4A2 459A870A A6A91851` 

- `B : BF6C142E 3E05BCE2 C8E88C04 89FDA622 1F0BCBF5 14BE8B05 92DFA9E7 729B38C9 52FF859D 825367E0 C9F837BC B8F4B2E4 404F6C63 C7652C11 ADABC592 D80E8BF7` 

- `C : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

225 

###### `W : 00000002 00000000` 

```
n0_final=2:permutation(j=0)
```

- `A : 2EB1121F 2F42E458 B41B281A 218E48E7 952E465D 23650000 751EC9DA DD262DAE C2774FC1 B28D8D45 5DB96F4E CFB0AEF3` 

- `B : 9AB83DC5 FA9D8467 DE58590A 5A46FFE4 54C62E48 F5E7E9F5 AF5E65EA C7EFA3C3 9877BB04 49D4BD7B 31B6FFC8 41A634C5 51D03526 5E774384 10B35CC0 6E6CA0F7` 

- `C : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

###### `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : 4EFB4B09 A0E2C3B8 B4E8EB92 7E77C334 DA205714 956A50C4 403A77F8 4A3A786D AAB74DE4 86726A02 2D88B2F1 C0686507` 

- `B : 9274CA46 D241ACA1 BC2E7F21 A4FEF233 FCC4EE8B 92424616 8CCB86DB B048DD7F 81EBC2FF CCB446B1 287AEBFD 02C45541 867FC2A7 D67B2833 9EA33187 691CC67C` 

- `C : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : 36818005 044E6515 C35442A8 8574DDFC 3C20F5DA FC2D15B6 D6DA9553 FDD91DF3 FA5E5BA4 558CF4A3 DACE3FB9 8F924C9E` 

- `B : 57E837B3 3B2C6ACA E0358DC2 2BD758E9 30F7A2ED DF3516C7 253CB0E0 1A1A98FC C0088FDA 9ABA672A 79D0BD56 07AE488E 095E2114 06855B3B 1877A349 A2543F99` 

- `C : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - add C to A` 

- `A : 3DBA182A D0D6787E DAD8F4C9 CC065328 A36A08C7 902C794E 43E5A220 E2F378F1 1E35B4C3 EF6B834E 8E442A11 6922E895` 

- `B : 57E837B3 3B2C6ACA E0358DC2 2BD758E9 30F7A2ED DF3516C7 253CB0E0 1A1A98FC C0088FDA 9ABA672A 79D0BD56 07AE488E 095E2114 06855B3B 1877A349 A2543F99` 

- `C : 66DF9771 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : 3DBA182A D0D6787E DAD8F4C9 CC065328 A36A08C7 902C794E 43E5A220 E2F378F1 1E35B4C3 EF6B834E 8E442A11 6922E895` 

- `B : 57E837B3 3B2C6ACA E0358DC2 2BD758E9 30F7A2ED DF3516C7 253CB0E0 1A1A98FC C0088FDA 9ABA672A 79D0BD56 07AE488E 095E2114 06855B3B 1877A349 A2543F99` 

226 

- `C : 66DF96F1 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

```
W:0000000200000000
```

- `n0_final = 2 : swap B with C (final state)` 

- `A : 3DBA182A D0D6787E DAD8F4C9 CC065328 A36A08C7 902C794E 43E5A220 E2F378F1 1E35B4C3 EF6B834E 8E442A11 6922E895` 

- `B : 66DF96F1 E4D309BD 6377D5E2 48F253E3 F8E9B974 0773C11C 8B2B886F 9D7AC002 343612B3 80C441F4 F676FCAD 3D6A453A 6CBEC284 2B3DE748 57EE16DB 80DBFF08` 

- `C : 57E837B3 3B2C6ACA E0358DC2 2BD758E9 30F7A2ED DF3516C7 253CB0E0 1A1A98FC C0088FDA 9ABA672A 79D0BD56 07AE488E 095E2114 06855B3B 1877A349 A2543F99` 

- `W : 00000002 00000000` 

```
Hashvalue(wordarray):
```

- `H : C0088FDA 9ABA672A 79D0BD56 07AE488E 095E2114 06855B3B 1877A349 A2543F99` 

```
Hashvalue(bytearray):
```

- `H : DA 8F 08 C0 2A 67 BA 9A 56 BD D0 79 8E 48 AE 07 14 21 5E 09 3B 5B 85 06 49 A3 77 18 99 3F 54 A2` 

### **B.6 Intermediate States for Shabal-256 (Message B)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:messageblock
```

- `M : 00000100 00000101 00000102 00000103 00000104 00000105 00000106 00000107 00000108 00000109 0000010A 0000010B 0000010C 0000010D 0000010E 0000010F` 

```
blocknumber=-1:addMtoB
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000100 00000101 00000102 00000103 00000104 00000105 00000106 00000107 00000108 00000109 0000010A 0000010B 0000010C 0000010D 0000010E 0000010F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

227 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:xorcounterWintoA
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000100 00000101 00000102 00000103 00000104 00000105 00000106 00000107 00000108 00000109 0000010A 0000010B 0000010C 0000010D 0000010E 0000010F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 02000000 02020000 02040000 02060000 02080000 020A0000 020C0000 020E0000 02100000 02120000 02140000 02160000 02180000 021A0000 021C0000 021E0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
W:FFFFFFFFFFFFFFFF
```

```
blocknumber=-1:permutation(j=0)
```

- `A : AE3F47E2 C68A60D9 C63E700C 04FB82A0 8088FEAE 64D8954B CC08DF9F F2497B68 7EC08316 F007C07B BBB8A77D 6C368247` 

- `B : 06080102 FE78F1B6 12CC57B2 93BBAACD 7B670151 9F336AB4 37EF2060 09AA8497 851F7CE9 0BDC3F84 406F5882 97E57DB8 55F0B81D 3D419F26 3DF98FF3 FF387D5F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : FF750C93 E5788A46 9BBD7565 CC341456 AD7FFC12 CE83FA1C 6511FD37 E0E9DCD1 A72272C9 B2929B0B 78EE6F01 C3B82A6F` 

- `B : 14F4A4C4 CDE737FE 5675BD47 7A96E075 AE138F94 730BB19D E8CFD03E 2F12DCBE 0AB40ABF 0D3F0AB1 E49C3B9E 1C0110D8 F96173D7 4BFF3BAF E11D1D2E E166D991` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

228 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:subtractMfromC
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `C : FFFFFF00 FFFFFEFF FFFFFEFE FFFFFEFD FFFFFEFC FFFFFEFB FFFFFEFA FFFFFEF9 FFFFFEF8 FFFFFEF7 FFFFFEF6 FFFFFEF5 FFFFFEF4 FFFFFEF3 FFFFFEF2 FFFFFEF1` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : FFFFFF00 FFFFFEFF FFFFFEFE FFFFFEFD FFFFFEFC FFFFFEFB FFFFFEFA FFFFFEF9 FFFFFEF8 FFFFFEF7 FFFFFEF6 FFFFFEF5 FFFFFEF4 FFFFFEF3 FFFFFEF2 FFFFFEF1` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : FFFFFF00 FFFFFEFF FFFFFEFE FFFFFEFD FFFFFEFC FFFFFEFB FFFFFEFA FFFFFEF9 FFFFFEF8 FFFFFEF7 FFFFFEF6 FFFFFEF5 FFFFFEF4 FFFFFEF3 FFFFFEF2 FFFFFEF1` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:messageblock
```

- `M : 00000110 00000111 00000112 00000113 00000114 00000115 00000116 00000117 00000118 00000119 0000011A 0000011B 0000011C 0000011D 0000011E 0000011F` 

229 

```
blocknumber=0:addMtoB
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:xorcounterWintoA
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-rotateB
```

- `A : 79F023D8 708745B8 B2D69F0A AB24079A 4C77DDAC B4B92870 88E6ECE2 747657E4 3395A2D7 5A9826A0 0D578B50 68F97918` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=0)
```

- `A : 7F0490C3 946910EC 827CA63E 409A1072 2B03CF2C FED97162 7F90F2B4 4069B7E1 CCB74C96 09778D59 6B24AB90 80A11478` 

- `B : AA98C924 A5880F94 19DB44E2 61A3149F D4BC30D3 01668E9D 802F0D4B BFD6481E 3308B369 F6C872A6 949B546F 7F1EEB87 80BB6F3C 6BD6EF13 7DC359C1 BF25EF8D` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : D455C979 9F6F4358 7F3D0246 E8A1F260 BE9C04EA 15A315D0 279AC5A8 1C34F0F3 10A66C48 D8CCDB49 02B680C7 AB645FCF` 

- `B : 5923FD91 9DEBD978 66452E00 8510F1DD 4621F210 25FE398C FD1765AF 2B37300D 4DBB5054 8D0059EA A9F45566 E963DA91 4015256C 3DF13409 23E389D5 9D80D017` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

230 

###### `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : B6A03371 17243406 531455C7 44F0DBD6 EC3CC237 851D8290 D99C1EB9 AED060A3 C3433D0F 62FD9C1A 02BB7200 5FB743B0` 

- `B : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-addCtoA
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : B555C7FE 3E7106A7 A72A6641 93015272 DA28C30E 696FD97D 9CB6C088 0AFE4119 A6E0372D 5138C2ED BE216420 B38B89AB 3EA8BA87 3299AE01 30924EF2 55CB35C4` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `C : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : B555C6EE 3E710596 A72A652F 9301515F DA28C1FA 696FD868 9CB6BF72 0AFE4002 A6E03615 5138C1D4 BE216306 B38B8890 3EA8B96B 3299ACE4 30924DD4 55CB34A5` 

231 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 302D7A79 34333231 38373635 42412D39 46454443 4A494847 4E4D4C4B 5251504F 56555453 5A595857` 

```
blocknumber=1:addMtoB
```

- `A : 52F84552 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : 19B9294F A6D86BFB 1395CF98 0370BFCC 4E9C346B E1E74EDD CCE439EB 3F317233 DF176C4A 9379EF0D 0466A749 FDD4D0D7 8CF605B6 84EAFD33 86E7A227 B0248CFC` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:xorcounterWintoA
```

- `A : 52F84553 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : 19B9294F A6D86BFB 1395CF98 0370BFCC 4E9C346B E1E74EDD CCE439EB 3F317233 DF176C4A 9379EF0D 0466A749 FDD4D0D7 8CF605B6 84EAFD33 86E7A227 B0248CFC` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : 52F84553 E54B7999 2D8EE3EC B9645191 E0078B86 BB7C44C9 D2B5C1CA B0D2EB8C 14CE5A45 22AF50DC EFFDBC6B EB21B74A` 

- `B : 529E3372 D7F74DB0 9F30272B 7F9806E1 68D69D38 9DBBC3CE 73D799C8 E4667E62 D895BE2E DE1B26F3 4E9208CD A1AFFBA9 0B6D19EC FA6709D5 444F0DCF 19F96049` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=0)
```

- `A : F6D73330 89E4C140 3E1E3376 8A749508 A272998B B4E5B3E3 4C0D8E29 7F5FC96D 76E421F9 550550FF 576B6AC2 E314C484` 

- `B : F9AC6F35 B8B2E012 85A4AF53 0DCFA1CA 8C205C04 706DCB81 545D4246 486CCA57 3830A25B 16CCE2E7 35B084A7 5FB4CC28 1FF2FF17 82D52D14 497FD717 4679AA65` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

232 

```
blocknumber=1:permutation(j=1)
```

- `A : C07120A5 04EE925E 300C7989 C5E1B76B 01DA3B70 7E8672A6 ACC3FAD9 B8572BD6 4814BD95 BCDD8C44 7871F536 AD059F2B` 

- `B : F266D21B B63BAB98 206805EE B84F2DF8 AFABFA63 A3F9E4B9 2F348E45 C223F47A 4FEF9BEC D688A86F A4928F38 8577D0C4 C1C03AA1 84D3D770 C1C3AB08 CB5B80E3` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : 8B5E482B EFEC43B6 A1FE969E 5C0B2ED9 A3A90B23 3C6E5B7C F85A8647 9B0EEF10 6AD2B985 A869C2D6 BF63A720 4D5430F0` 

- `B : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : 6B6D2C5F 25A4E4BD F0299A30 20C7680E ED31090B 3E4611BB C0884C9C 1AD2D57B 9CF9C58C B2D2110C AA4E3AB2 D4287C37` 

- `B : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `C : B405F031 C4233EBA B3733979 C0DD9D55 C51C28AE A327B8E1 56C56167 ED614433 88B59D60 60E2CEBA 758B4B8B 83E82A7F BC968828 E6E00BF7 BA839E55 9B491C60` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : 6B6D2C5F 25A4E4BD F0299A30 20C7680E ED31090B 3E4611BB C0884C9C 1AD2D57B 9CF9C58C B2D2110C AA4E3AB2 D4287C37` 

- `B : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `C : 4FA28DD0 5BBBD855 4707CF10 506E2EE8 50A8B63D 2AB0426C 2697E6EE B92E1202 507E672B 1EA1A181 2F460748 399EE238 6E493BDD 948EBBA8 642E4A02 40EFC409` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : 6B6D2C5F 25A4E4BD F0299A30 20C7680E ED31090B 3E4611BB C0884C9C 1AD2D57B 9CF9C58C B2D2110C AA4E3AB2 D4287C37` 

- `B : 4FA28DD0 5BBBD855 4707CF10 506E2EE8 50A8B63D 2AB0426C 2697E6EE B92E1202 507E672B 1EA1A181 2F460748 399EE238 6E493BDD 948EBBA8 642E4A02 40EFC409` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3` 

233 

```
C389C3046E80F45C4E8067C96E1EB16616AD33395E3193C8C31B0ECE241CCEC8
```

```
W:0000000100000000
```

```
blocknumber=2:incrementcounterW
```

- `A : 6B6D2C5F 25A4E4BD F0299A30 20C7680E ED31090B 3E4611BB C0884C9C 1AD2D57B 9CF9C58C B2D2110C AA4E3AB2 D4287C37` 

- `B : 4FA28DD0 5BBBD855 4707CF10 506E2EE8 50A8B63D 2AB0426C 2697E6EE B92E1202 507E672B 1EA1A181 2F460748 399EE238 6E493BDD 948EBBA8 642E4A02 40EFC409` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 3231302D 36353433 2D393837 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 00807A79 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : 6B6D2C5F 25A4E4BD F0299A30 20C7680E ED31090B 3E4611BB C0884C9C 1AD2D57B 9CF9C58C B2D2110C AA4E3AB2 D4287C37` 

- `B : 81D3BDFD 91F10C88 74410747 B4D19149 B9101CA2 971BACD5 9707555B 2DA18473 C8F5DDA0 1F221BFA 2F460748 399EE238 6E493BDD 948EBBA8 642E4A02 40EFC409` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `W : 00000002 00000000` 

```
blocknumber=2:xorcounterWintoA
```

- `A : 6B6D2C5D 25A4E4BD F0299A30 20C7680E ED31090B 3E4611BB C0884C9C 1AD2D57B 9CF9C58C B2D2110C AA4E3AB2 D4287C37` 

- `B : 81D3BDFD 91F10C88 74410747 B4D19149 B9101CA2 971BACD5 9707555B 2DA18473 C8F5DDA0 1F221BFA 2F460748 399EE238 6E493BDD 948EBBA8 642E4A02 40EFC409` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : 6B6D2C5D 25A4E4BD F0299A30 20C7680E ED31090B 3E4611BB C0884C9C 1AD2D57B 9CF9C58C B2D2110C AA4E3AB2 D4287C37` 

- `B : 7BFB03A7 191123E2 0E8EE882 229369A3 39457220 59AB2E37 AAB72E0E 08E65B43 BB4191EB 37F43E44 0E905E8C C470733D 77BADC92 7751291D 9404C85C 881281DF` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `W : 00000002 00000000` 

234 

```
blocknumber=2:permutation(j=0)
```

- `A : 27DDABAE 3485C441 EF71221A A12B9143 A9CF4744 5E5BDF73 9120D522 105DAB7D 7D653849 E57D34A3 EE830FDA 5D81CF9F` 

- `B : 83678676 D553452F 99228D2F D1CB70C0 24BA5CFB 12F27CE2 3BB176C0 FE6EE204 F419E461 756AB7D4 0C5C4D3D 2A9ED61B 3757ED75 25D86984 38874D5C 4EF16D03` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=1)
```

- `A : FDEC5D48 7F32E3BF 3312EE26 73F81D45 E771CB44 2A8DED27 D7AE1BDD A87D95D5 09F3FF4A CF3EAA2E 1B2F4B4C 4F8F64A2` 

- `B : 2EDDE854 6276F9BC 49DED920 6637625D BF78B943 1525AC15 93B25933 4CAD5F54 EA206A74 6A1873E8 D4558BA3 D93A4E8C 7621EE51 9EC2C1D0 595F7E9A CA60B02C` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : D22C0DEA A7764ACD C57D3D58 0AA68F74 A26B8BA2 47726CDB 66B4B2AC 505FB429 085C7159 85E454FC 0CD7F1DE 568BADDB` 

- `B : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : 49D1B737 96C0CBAE C9CF2F86 542E7918 D3A5BD5C E3997D87 7B56056E 254CF6C8 839885B1 8C118E4C 316AEF3C 688F9A5D` 

- `B : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `C : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : 49D1B737 96C0CBAE C9CF2F86 542E7918 D3A5BD5C E3997D87 7B56056E 254CF6C8 839885B1 8C118E4C 316AEF3C 688F9A5D` 

- `B : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `C : 7A75DA68 180AB4F9 58CB2CB4 8106C6BE C38EDCAE EB750AD1 8FF9077E B33FC762 4B124C8F 6E0079E3 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

235 

###### `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : 49D1B737 96C0CBAE C9CF2F86 542E7918 D3A5BD5C E3997D87 7B56056E 254CF6C8 839885B1 8C118E4C 316AEF3C 688F9A5D` 

- `B : 7A75DA68 180AB4F9 58CB2CB4 8106C6BE C38EDCAE EB750AD1 8FF9077E B33FC762 4B124C8F 6E0079E3 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `C : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : add M to B` 

- `A : 49D1B737 96C0CBAE C9CF2F86 542E7918 D3A5BD5C E3997D87 7B56056E 254CF6C8 839885B1 8C118E4C 316AEF3C 688F9A5D` 

- `B : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `C : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : xor counter W into A` 

- `A : 49D1B735 96C0CBAE C9CF2F86 542E7918 D3A5BD5C E3997D87 7B56056E 254CF6C8 839885B1 8C118E4C 316AEF3C 688F9A5D` 

- `B : ACA70A95 4E3FE92C 860464EB E56A291F 2BF64313 57E0753A 006875EB 27B339D3 C389C304 6E80F45C 4E8067C9 6E1EB166 16AD3339 5E3193C8 C31B0ECE 241CCEC8` 

- `C : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : 49D1B735 96C0CBAE C9CF2F86 542E7918 D3A5BD5C E3997D87 7B56056E 254CF6C8 839885B1 8C118E4C 316AEF3C 688F9A5D` 

- `B : 152B594E D2589C7F C9D70C08 523FCAD4 862657EC EA74AFC0 EBD600D0 73A64F66 86098713 E8B8DD01 CF929D00 62CCDC3D 66722D5A 2790BC63 1D9D8636 9D904839` 

- `C : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

- `A : 67D32091 5303AF58 5A861FAD 0C4A05CE 7A6147AA 345CEC5B 7C1199C6 7CECED68 826D1307 0C41559C 00B9D8B4 68FAEE46` 

- `B : 85E5A48A EAFA029C 12B066C0 100D7776 89D2178C 1F4A4C25 54426798 645F8C5B 7181E2DF 22CF1060 60631D4A 529CA9C3 54C885DA E3DD2861 9E42EC3E C8956A42` 

236 

- `C : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : F1D330FB 55A76650 3645D1D3 79E5AA6A A4480A6E C8A221B8 2D30A72C B7B74535 235DF568 17EB4789 BF57EC17 29851CE7` 

- `B : F0F15233 2E98CF7D 0BC24E4B 36898599 CF06258E D680203C E82CDCD8 1EC5FBAE ED2F0ABA EFC6B96F 097C14B8 23230613 F226FE25 F0E78E84 EE4A80AE D9626E4F` 

- `C : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

```
n0_final=0:permutation(j=2)
```

- `A : 553BD29F C35AB8A9 A7ECA963 47F2291E D1AF3761 7068CAA6 D7DFE602 2DC59B1A 22D5EA34 88C9C00A 2FF881C6 D21852D1` 

- `B : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `C : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : C8359612 02D93B49 D2D2ACDC 8A52D4CF 92D7F228 1DDB9BF6 27E535CD 606FADCA C41E494D 81A13354 57170C74 637610BA` 

- `B : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `C : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : subtract M from C` 

- `A : C8359612 02D93B49 D2D2ACDC 8A52D4CF 92D7F228 1DDB9BF6 27E535CD 606FADCA C41E494D 81A13354 57170C74 637610BA` 

- `B : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `C : 9E4A7FDD 3A4FB98C B5AA0FA5 B30C57C6 EABB1A2D 065782AF AD770253 F7905BB2 115D2A3F 6C3CFA7B 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : swap B with C` 

- `A : C8359612 02D93B49 D2D2ACDC 8A52D4CF 92D7F228 1DDB9BF6 27E535CD 606FADCA C41E494D 81A13354 57170C74 637610BA` 

237 

- `B : 9E4A7FDD 3A4FB98C B5AA0FA5 B30C57C6 EABB1A2D 065782AF AD770253 F7905BB2 115D2A3F 6C3CFA7B 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `C : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

- `A : C8359612 02D93B49 D2D2ACDC 8A52D4CF 92D7F228 1DDB9BF6 27E535CD 606FADCA C41E494D 81A13354 57170C74 637610BA` 

- `B : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `C : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `W : 00000002 00000000` 

- `n0_final = 1 : xor counter W into A` 

- `A : C8359610 02D93B49 D2D2ACDC 8A52D4CF 92D7F228 1DDB9BF6 27E535CD 606FADCA C41E494D 81A13354 57170C74 637610BA` 

- `B : D07BB00A 7084EDBF E2E347DC 176FBA27 53228092 72C2ED18 1DE670C0 6C03CE23 89D4A0B4 6CBD74F4 31E05A14 1DD4D6CF 1BE05204 479E28A2 4196F315 3DB5327D` 

- `C : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

- `A : C8359610 02D93B49 D2D2ACDC 8A52D4CF 92D7F228 1DDB9BF6 27E535CD 606FADCA C41E494D 81A13354 57170C74 637610BA` 

- `B : 6015A0F7 DB7EE109 8FB9C5C6 744E2EDF 0124A645 DA30E585 E1803BCC 9C46D807 416913A9 E9E8D97A B42863C0 AD9E3BA9 A40837C0 51448F3C E62A832D 64FA7B6A` 

- `C : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : BD28A5CF BA0BBFB0 00095A8C C1B09C32 D38E01FD F1CC7A37 CED0E9B6 7C714B13 C42B6040 A1C0E60C 5CD392A3 C0483484` 

- `B : 1509DB26 56317C44 79ED350B CB01B836 2E38B288 BA524EC3 F22F61D0 BB0304E3 B906B8ED 8DEEAB06 CB7CAADD 648BBC28 0AC735B1 E77D5E37 33A3A328 F7BB9519` 

- `C : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

238 

- `A : 71C9F985 C800394A 8FBD7622 AC657B69 2FB2355C D16C61B4 0D746211 A309E118 17C31A6B D8076499 B38EA0F6 9885FDE2` 

- `B : E89A0525 77CE7CF7 452129C5 54340C45 B44D8084 535C06E1 A82F9CA8 117C0BDA FC3B77A1 2C2290B8 E6BBDC66 9A8DFCC6 C5C3A1C1 E0692224 95CCDBBE B38134D4` 

- `C : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 2)` 

- `A : 1ADC4E68 7A0843ED C62C5677 43303AC9 E39D6B8C 6D6358A3 6A5C56A4 AC6F15A0 E3AF684E 1E4B0104 4DABDD43 BCD9E6D6` 

- `B : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `C : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - add C to A` 

- `A : E46B64EA 35DD33B1 3767DBDC DFB877B8 9E363B08 E3DF3CD2 94B90093 773D03B8 93A12EDC 808A2EEC C6644EF4 8C8F85F4` 

- `B : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `C : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

###### `W : 00000002 00000000` 

- `n0_final = 1 : subtract M from C` 

- `A : E46B64EA 35DD33B1 3767DBDC DFB877B8 9E363B08 E3DF3CD2 94B90093 773D03B8 93A12EDC 808A2EEC C6644EF4 8C8F85F4` 

- `B : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `C : 1B736F9A 12682707 DA719627 318BD9AD CC610018 25399CC6 17DB80C0 1112AF4C 7B976776 4F99CD0D 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `W : 00000002 00000000` 

```
n0_final=1:swapBwithC
```

- `A : E46B64EA 35DD33B1 3767DBDC DFB877B8 9E363B08 E3DF3CD2 94B90093 773D03B8 93A12EDC 808A2EEC C6644EF4 8C8F85F4` 

- `B : 1B736F9A 12682707 DA719627 318BD9AD CC610018 25399CC6 17DB80C0 1112AF4C 7B976776 4F99CD0D 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `C : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `W : 00000002 00000000` 

239 

```
n0_final=2:addMtoB
```

- `A : E46B64EA 35DD33B1 3767DBDC DFB877B8 9E363B08 E3DF3CD2 94B90093 773D03B8 93A12EDC 808A2EEC C6644EF4 8C8F85F4` 

- `B : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `C : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `W : 00000002 00000000` 

- `n0_final = 2 : xor counter W into A` 

- `A : E46B64E8 35DD33B1 3767DBDC DFB877B8 9E363B08 E3DF3CD2 94B90093 773D03B8 93A12EDC 808A2EEC C6644EF4 8C8F85F4` 

- `B : 4DA49FC7 489D5B3A 07AACE5E 95EF3C0E 34C8667D 91A5072F 884AEF2D 858621BD F40EDDEB 501A4786 3AD8308D 947C68C3 3967E980 96F922FC 0C927F64 9F2371B1` 

- `C : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - rotate B` 

- `A : E46B64E8 35DD33B1 3767DBDC DFB877B8 9E363B08 E3DF3CD2 94B90093 773D03B8 93A12EDC 808A2EEC C6644EF4 8C8F85F4` 

- `B : 3F8E9B49 B674913A 9CBC0F55 781D2BDE CCFA6990 0E5F234A DE5B1095 437B0B0C BBD7E81D 8F0CA034 611A75B0 D18728F8 D30072CF 45F92DF2 FEC81924 E3633E46` 

- `C : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 0)` 

- `A : A72DE636 5297305E F2707159 668235DB BD196957 5D16B98F 97EDABFF A8A4C5E3 93A64094 C93B80A3 493E6060 15BAF34E` 

- `B : 9DFAB6A3 C6D77880 8F8A3FEA 56D97CA8 DB124589 BE5700E4 D4A4752B D1AD2C04 1BF66F50 28DD3F35 74F574FF 494B5D40 FED2FC56 269A9445 F01FBCEF 5FBBB6A9` 

- `C : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : C9D3F423 B47F8AE4 359A3049 BCC98A64 DDBC4864 E9BD6633 87ABF033 CED5B802 2D289F8C 80B46CEB FCF20C9A 61AC8102` 

- `B : 66048AA2 6E002C53 A815E77E 1B0568F6 64F3EB60 03E592DD AA451932 3D0926F4 01C0D57C 1A3A0B71 238F2648 D1A0CF1B DFE64F36 5B77B146 986B7613 8E5D2AAF` 

- `C : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

240 

###### `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : 9CEAF17C 69EC9966 D73B3761 D13C3EBC 434ACAB3 FBC76F4C D4258F3C 8295350A 905C9850 D343C11C 97847D27 99775D23` 

- `B : C539CC9B CA52634F 214754DE 19A73AD2 AAF2D843 91D84323 7C4EFAFB 54D18CAB BF349FB4 304C8651 6CC43C53 DE2B54C2 D06FF9C2 9A535C6F 58AD6EFF 7A32F783` 

- `C : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - add C to A` 

- `A : 08ABA604 9C4035C7 8B73310B B3795EF0 E6B83DEB 7A57B2AB 31D05460 23D8D113 7630AEDA DCE8C11C A7146FD5 F5A59553` 

- `B : C539CC9B CA52634F 214754DE 19A73AD2 AAF2D843 91D84323 7C4EFAFB 54D18CAB BF349FB4 304C8651 6CC43C53 DE2B54C2 D06FF9C2 9A535C6F 58AD6EFF 7A32F783` 

- `C : 0CC31791 6F818D28 DEE2F99A E1113036 8DB8B09E 234FB1D0 698C90D9 9E37D282 E4147B30 CAD9862C 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : 08ABA604 9C4035C7 8B73310B B3795EF0 E6B83DEB 7A57B2AB 31D05460 23D8D113 7630AEDA DCE8C11C A7146FD5 F5A59553` 

- `B : C539CC9B CA52634F 214754DE 19A73AD2 AAF2D843 91D84323 7C4EFAFB 54D18CAB BF349FB4 304C8651 6CC43C53 DE2B54C2 D06FF9C2 9A535C6F 58AD6EFF 7A32F783` 

- `C : DA91E764 394C58F5 B1A9C163 7CADCDD5 25514A39 B6E44767 F91D226C 29C46011 6B9D04BB CA590BB3 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : 08ABA604 9C4035C7 8B73310B B3795EF0 E6B83DEB 7A57B2AB 31D05460 23D8D113 7630AEDA DCE8C11C A7146FD5 F5A59553` 

- `B : DA91E764 394C58F5 B1A9C163 7CADCDD5 25514A39 B6E44767 F91D226C 29C46011 6B9D04BB CA590BB3 58D41196 668B13D2 97D7D432 2166BAB2 99CD95C1 24247080` 

- `C : C539CC9B CA52634F 214754DE 19A73AD2 AAF2D843 91D84323 7C4EFAFB 54D18CAB BF349FB4 304C8651 6CC43C53 DE2B54C2 D06FF9C2 9A535C6F 58AD6EFF 7A32F783` 

- `W : 00000002 00000000` 

```
Hashvalue:
```

- `H : BF349FB4 304C8651 6CC43C53 DE2B54C2 D06FF9C2 9A535C6F 58AD6EFF 7A32F783` 

```
Hashvalue(bytearray):
```

241 

- `H : B4 9F 34 BF 51 86 4C 30 53 3C C4 6C C2 54 2B DE C2 F9 6F D0 6F 5C 53 9A FF 6E AD 58 83 F7 32 7A` 

### **B.7 Intermediate States for Shabal-384 (Message A)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:messageblock
```

- `M : 00000180 00000181 00000182 00000183 00000184 00000185 00000186 00000187 00000188 00000189 0000018A 0000018B 0000018C 0000018D 0000018E 0000018F` 

###### `block number = -1 : add M to B` 

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000180 00000181 00000182 00000183 00000184 00000185 00000186 00000187 00000188 00000189 0000018A 0000018B 0000018C 0000018D 0000018E 0000018F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:xorcounterWintoA
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000180 00000181 00000182 00000183 00000184 00000185 00000186 00000187 00000188 00000189 0000018A 0000018B 0000018C 0000018D 0000018E 0000018F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 03000000 03020000 03040000 03060000 03080000 030A0000 030C0000 030E0000 03100000 03120000 03140000 03160000 03180000 031A0000 031C0000 031E0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

242 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=0)
```

- `A : 73B2093A 2A799470 05BF52F2 607A3AE1 BDA5E845 9A4F4C59 45672DC2 977B1FC2 FD372A8B D7D97B33 8A5D1B6E 4D17CE45` 

- `B : 05080182 F1B8E8B6 D44C4392 F9C1290D 444A17BA 63A4B3A6 BC80D23D 6E98E03D 04E8D574 2E0284CC 738AE491 B4C431BA 8A7DF6C5 D3B26B8F FC78AD0D 99B9C51E` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : 34DCDD7F 3399F8DC A47ABF91 51043F32 FDF93568 64558055 3E48B569 0D011A26 DB56076A C383CE67 FA750B12 041BF733` 

- `B : AF9C5E68 55490C52 C44C5DCB C0EE508F AC3DD7E1 FB3556D4 7C8B5096 26D5C8B6 C2F28868 90630EBB BC90894C C773A3B8 16FD271C 3CCEA8B5 3946108D C18D6FE4` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:subtractMfromC
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

243 

- `C : FFFFFE80 FFFFFE7F FFFFFE7E FFFFFE7D FFFFFE7C FFFFFE7B FFFFFE7A FFFFFE79 FFFFFE78 FFFFFE77 FFFFFE76 FFFFFE75 FFFFFE74 FFFFFE73 FFFFFE72 FFFFFE71` 

```
W:FFFFFFFFFFFFFFFF
```

```
blocknumber=-1:swapBwithC
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : FFFFFE80 FFFFFE7F FFFFFE7E FFFFFE7D FFFFFE7C FFFFFE7B FFFFFE7A FFFFFE79 FFFFFE78 FFFFFE77 FFFFFE76 FFFFFE75 FFFFFE74 FFFFFE73 FFFFFE72 FFFFFE71` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : FFFFFE80 FFFFFE7F FFFFFE7E FFFFFE7D FFFFFE7C FFFFFE7B FFFFFE7A FFFFFE79 FFFFFE78 FFFFFE77 FFFFFE76 FFFFFE75 FFFFFE74 FFFFFE73 FFFFFE72 FFFFFE71` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:messageblock
```

- `M : 00000190 00000191 00000192 00000193 00000194 00000195 00000196 00000197 00000198 00000199 0000019A 0000019B 0000019C 0000019D 0000019E 0000019F` 

```
blocknumber=0:addMtoB
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:xorcounterWintoA
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

244 

```
blocknumber=0:permutation-rotateB
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=0)
```

- `A : CCCBA1B5 9E2FD849 89AD738F EA03554C 4C6371DE B511FBE1 C32FB2C4 E167BC5D A3B8F2F7 861F866F 0FA17732 5CBE8AEC` 

- `B : 86817371 DAB4EDE3 FC92F8B3 09D76240 B3DC8E21 4AAE041E 3C904D3B 1ED843A2 5C070D08 79A07990 F01E88CD A3017513 33745E4A 619027B6 76128C70 15BCAAB3` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : B98F348F 138FE48E 0084D32A B0E0FA9B 421966F9 31F37984 0D872018 F8EA2855 42A78E98 D97ED055 AC4EF3A7 14091C2E` 

- `B : A9DBD892 301E9E26 6FE8F3E6 D673177A DAE16D24 B3DD2796 2A91962E D6466495 FE7ED160 1F30E851 1F463D4E 091DEF43 DB0E2592 0D2CC917 1E5DC707 2C6C82CC` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : B4347AD7 C625A866 FA943F56 024604B5 6D6C6BE2 A28D22F0 68B51EB5 F354CB75 35D6B3E1 CD7F33BC 69707FFC 6C1B1417` 

- `B : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-addCtoA
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

245 

###### `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=1:addMtoB
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

```
W:0000000100000000
```

```
blocknumber=1:xorcounterWintoA
```

246 

- `A : C8FCA330 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : C8FCA330 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : 23F8A4E5 8ABE542C 4FCAF1CC 2D3F289E E02C394D D44B50A9 157D1B73 4C83E58C FB966022 86139EB8 344B26E2 E371F3EC 422D603A 9712667E A2CB650B 366D0D05` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=0)
```

- `A : 29DABD96 F74E1392 FCCD6D6D 6016B327 193F7D56 E1E754D0 C1A21C25 713AF436 82967D97 F48C9BBA A69674D7 3350318A` 

- `B : 6734CB7C DFF55475 5BD581F2 446284F9 2698F032 B68E0A7C 14A7D53C 17C2C0D1 8A45422D 07545934 31FFC6EC 0A4C29AC 527F821D 26952090 46A45885 F33356D2` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : EE45873E 91F25A63 FC45FB83 01A2AA3A CF67FE6E 033DA5F2 D00AF246 1D17F764 821A18CB C44843D5 800E8C1C 299E27BD` 

- `B : 4E4AF2A0 875E82F8 AE008BF2 64ED7F54 30D40750 56ABA8D3 56BED99B F9E459E0 0530FC9A 60A517F4 604589A4 EAC5069D 946705AB B1E81B2D A2BDBCB3 048EA53E` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : DBE86E2D 3B7FD0AC 33B7A95F F72D25D1 8E3BCD73 4EE405AF A5468DBC 7CFF44FA 029982C2 652E9095 527DEF92 42BF4BEA` 

- `B : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

247 

```
blocknumber=1:permutation-addCtoA
```

- `A : 8C89CA42 AD22E862 310841C6 C0A0B420 718171DD B2C04D06 DCD0D563 46056112 393222C8 4DDB2E0D 3CCA7460 E702E2C2` 

- `B : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : 8C89CA42 AD22E862 310841C6 C0A0B420 718171DD B2C04D06 DCD0D563 46056112 393222C8 4DDB2E0D 3CCA7460 E702E2C2` 

- `B : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : 8C89CA42 AD22E862 310841C6 C0A0B420 718171DD B2C04D06 DCD0D563 46056112 393222C8 4DDB2E0D 3CCA7460 E702E2C2` 

- `B : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : 8C89CA42 AD22E862 310841C6 C0A0B420 718171DD B2C04D06 DCD0D563 46056112 393222C8 4DDB2E0D 3CCA7460 E702E2C2` 

- `B : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 00000080 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : 8C89CA42 AD22E862 310841C6 C0A0B420 718171DD B2C04D06 DCD0D563 46056112` 

248 

```
393222C84DDB2E0D3CCA7460E702E2C2
```

- `B : F764B19A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

```
blocknumber=2:xorcounterWintoA
```

- `A : 8C89CA40 AD22E862 310841C6 C0A0B420 718171DD B2C04D06 DCD0D563 46056112 393222C8 4DDB2E0D 3CCA7460 E702E2C2` 

- `B : F764B19A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : 8C89CA40 AD22E862 310841C6 C0A0B420 718171DD B2C04D06 DCD0D563 46056112 393222C8 4DDB2E0D 3CCA7460 E702E2C2` 

- `B : 6335EEC9 428CEC2E 269B9DED 07338DA5 BEC3FC12 3168BCC0 D9EAA091 64C2A26A 6DB8DCDC 1B5AC626 37AD538D D4183D21 0E76F86A BCDA51B2 1C1B5468 DCE1967B` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : BCAC6965 BC456130 D2C53A25 9C87DCC6 E79EEF6B E013BF9B 8BB56810 BB0B3D73 1D08DDB3 BEA6B59C BFEFC1E6 0CAE3785` 

- `B : C23FF40E 30947FA2 5A92A998 0604026F 65E6E8B1 7D3D39E4 C79FD6CC 8D718658 39869BF4 77ECC62F 2F4A9903 5B61B239 5FBE664E 3A0E3DAA 150C6D0A DABB0FCE` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=1)
```

- `A : 5FC1D6C9 C32754E8 211541BE 13AADBA3 031836B2 2A4EA1D9 852D1D23 E29834B8 9109742B 28D6A906 216CD635 A27780E0` 

- `B : C28CC03F A83BBE0C 70DF0D50 6D1FECFA A53B5AB6 2D532531 51AC8453 476B73AE D3331EDE D3012749 807F8C47 5A96402E 439B05D1 A1AD2572 50CA38C8 A811D4DA` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

249 

```
blocknumber=2:permutation(j=2)
```

- `A : 4108B13A 325F6DBC 5DC0FA9B 75002C36 98BFAF7A AC636087 4BAF2F01 0FE87D16 A1201E01 6A947CD4 E4844B86 EEC546A5` 

- `B : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : 4E5861F5 2E6FB7AE B708BF8B B6DF970A 4A9F13E6 4E70FFC7 1C477078 0300DFEB F52C3A42 01A25E68 B7AEF964 D326F650` 

- `B : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `C : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : 4E5861F5 2E6FB7AE B708BF8B B6DF970A 4A9F13E6 4E70FFC7 1C477078 0300DFEB F52C3A42 01A25E68 B7AEF964 D326F650` 

- `B : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `C : E0A83396 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : 4E5861F5 2E6FB7AE B708BF8B B6DF970A 4A9F13E6 4E70FFC7 1C477078 0300DFEB F52C3A42 01A25E68 B7AEF964 D326F650` 

- `B : E0A83396 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `C : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `W : 00000002 00000000` 

- `n0_final = 0 : add M to B` 

- `A : 4E5861F5 2E6FB7AE B708BF8B B6DF970A 4A9F13E6 4E70FFC7 1C477078 0300DFEB F52C3A42 01A25E68 B7AEF964 D326F650` 

- `B : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `C : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

250 

###### `W : 00000002 00000000` 

- `n0_final = 0 : xor counter W into A` 

- `A : 4E5861F7 2E6FB7AE B708BF8B B6DF970A 4A9F13E6 4E70FFC7 1C477078 0300DFEB F52C3A42 01A25E68 B7AEF964 D326F650` 

- `B : E0A83416 F66EECCA F7B01C34 0266FC14 45BF9F72 69D77EF5 6135E596 FB1A69EF 7BA5CBB8 7051D5B8 9A32610B 568AB63E D5A8766A F9015931 E8F9690A B45DFE69` 

- `C : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : 4E5861F7 2E6FB7AE B708BF8B B6DF970A 4A9F13E6 4E70FFC7 1C477078 0300DFEB F52C3A42 01A25E68 B7AEF964 D326F650` 

- `B : 682DC150 D995ECDD 3869EF60 F82804CD 3EE48B7F FDEAD3AE CB2CC26B D3DFF634 9770F74B AB70E0A3 C2173464 6C7CAD15 ECD5AB50 B263F202 D215D1F2 FCD368BB` 

- `C : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

- `A : 5AC032DB 7835FAF9 9D3ACA4F 52A4439B 34003EF8 D9CBD4EF 371F3370 413D3009 E50777E8 9FC51900 5A4F213A 02096846` 

- `B : 078BA66D 03F2422E F3C52752 59FBBD14 B636D7F9 DDE18C4D 5EB94858 197D239F 34196680 36DB27B8 219EB60C 250FCD93 7C949B85 E30DE103 C6EE9655 54FD6D13` 

- `C : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : 0F05B0E0 32FAB2B8 97D516BC 4E391F09 FEBAEDD0 6C75B39A A57AD791 8CF52FFE E0AD084F F9602E76 D2232347 1194BE8F` 

- `B : 27C12D08 9DC6152C ABD39566 85C94B7F 733F5843 BD5CC912 90AE4C08 DC91064E 98C8821F A0B30237 2B17855B FBD97BD0 F86C2525 55918E62 D75804C5 DAF00A27` 

- `C : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

- `A : 75DB00C6 E780CF9A 4B5D5FFE E3C1540A 1700396D 5C013C57 97B4F350 36965EFD A5BC40C4 09DFFE2D 6B698281 F379046C` 

- `B : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

251 

- `C : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : 3748601C 1B5A9A55 B0AF1FEC FCFE71F9 975BCAA3 771789EE 1C73BB5B 49937F74 2A39C3C0 99725169 CE40F65B 647EA088` 

- `B : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `C : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `W : 00000002 00000000` 

```
n0_final=0:subtractMfromC
```

- `A : 3748601C 1B5A9A55 B0AF1FEC FCFE71F9 975BCAA3 771789EE 1C73BB5B 49937F74 2A39C3C0 99725169 CE40F65B 647EA088` 

- `B : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `C : 656DE437 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `W : 00000002 00000000` 

- `n0_final = 0 : swap B with C` 

- `A : 3748601C 1B5A9A55 B0AF1FEC FCFE71F9 975BCAA3 771789EE 1C73BB5B 49937F74 2A39C3C0 99725169 CE40F65B 647EA088` 

- `B : 656DE437 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `C : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

- `A : 3748601C 1B5A9A55 B0AF1FEC FCFE71F9 975BCAA3 771789EE 1C73BB5B 49937F74 2A39C3C0 99725169 CE40F65B 647EA088` 

- `B : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `C : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : xor counter W into A` 

- `A : 3748601E 1B5A9A55 B0AF1FEC FCFE71F9 975BCAA3 771789EE 1C73BB5B 49937F74 2A39C3C0 99725169 CE40F65B 647EA088` 

252 

- `B : 656DE4B7 F8191DFF 5CE74A44 3B194BB2 F481FBA8 9706D821 01660DC2 04293495 C1266D38 F59ED1EB B4AFC871 453B02B5 D9E9EA5C D631C9CE BAEFC5E9 411910EF` 

- `C : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

- `A : 3748601E 1B5A9A55 B0AF1FEC FCFE71F9 975BCAA3 771789EE 1C73BB5B 49937F74 2A39C3C0 99725169 CE40F65B 647EA088` 

- `B : C96ECADB 3BFFF032 9488B9CE 97647632 F751E903 B0432E0D 1B8402CC 692A0852 DA71824C A3D7EB3D 90E3695F 056A8A76 D4B9B3D3 939DAC63 8BD375DF 21DE8232` 

- `C : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : 1A4EA719 F0698671 F1A059F1 78AC9659 E7FC4989 09A85C59 C0005790 6AF3DAD6 FDD0BC75 A7610544 6EBB4706 5C84BC8F` 

- `B : 20BB2302 0F6DFD0A 4B8AE634 62053013 F6A06471 96D1FFBD 08F7ADF7 4758358D B6CC4713 1F312CC0 B0826A46 A9AE579C 4CC23F41 28AD2149 19F94DB1 C4EE6DC2` 

- `C : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

- `A : 817E579C E55778E3 48717CB5 A5F41442 11A17941 C8FDF843 AF1660C4 4A030F74 3F12381F 9E73AA5A A44E22BC 88044CB8` 

- `B : 5AC3EBAC 6C12C680 9D71E54C 92C5BCB1 2DAD0F03 4C2FAADE 4A5E86AD F94BD85D 13192644 24CADE9C D68A57C7 09574484 77DAF83C 6658452E 631B0459 3C202B0E` 

- `C : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 2)` 

- `A : C02FFE30 A65235AD A6DDBBDD F5741E0E 9D2636FC 65514408 C077EC60 8D365A4C 30F9C34D D85DAB73 65047BDA A3B324FF` 

- `B : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `C : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - add C to A` 

253 

- `A : E5D05403 03E0A0E1 1451872C 41541FB1 2907DD94 F1B27C79 B3816260 DD53ED13 424FD0AC C8C2B34F 076702F7 B23BD81D` 

- `B : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `C : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : subtract M from C` 

- `A : E5D05403 03E0A0E1 1451872C 41541FB1 2907DD94 F1B27C79 B3816260 DD53ED13 424FD0AC C8C2B34F 076702F7 B23BD81D` 

- `B : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `C : 46982585 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `W : 00000002 00000000` 

- `n0_final = 1 : swap B with C` 

- `A : E5D05403 03E0A0E1 1451872C 41541FB1 2907DD94 F1B27C79 B3816260 DD53ED13 424FD0AC C8C2B34F 076702F7 B23BD81D` 

- `B : 46982585 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `C : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

###### `W : 00000002 00000000` 

- `n0_final = 2 : add M to B` 

- `A : E5D05403 03E0A0E1 1451872C 41541FB1 2907DD94 F1B27C79 B3816260 DD53ED13 424FD0AC C8C2B34F 076702F7 B23BD81D` 

- `B : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `C : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `W : 00000002 00000000` 

```
n0_final=2:xorcounterWintoA
```

- `A : E5D05401 03E0A0E1 1451872C 41541FB1 2907DD94 F1B27C79 B3816260 DD53ED13 424FD0AC C8C2B34F 076702F7 B23BD81D` 

- `B : 46982605 ADAA0BF9 7BBB549E 2D5E0F54 6C5A4FBF 62C6A240 95FE3810 A51CA768 D96EC2AD E298C7C7 3E640619 3EDB56A3 AA9BF570 5D031D16 3A2674F5 B966EFDC` 

- `C : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `W : 00000002 00000000` 

254 

```
n0_final=2:permutation-rotateB
```

- `A : E5D05401 03E0A0E1 1451872C 41541FB1 2907DD94 F1B27C79 B3816260 DD53ED13 424FD0AC C8C2B34F 076702F7 B23BD81D` 

- `B : 4C0A8D30 17F35B54 A93CF776 1EA85ABC 9F7ED8B4 4480C58D 70212BFC 4ED14A39 855BB2DD 8F8FC531 0C327CC8 AD467DB6 EAE15537 3A2CBA06 E9EA744C DFB972CD` 

- `C : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 0)` 

- `A : 3476CE6E C2B87F0B 22FFE820 9EB55800 EE3D7C7F C4B99A54 901CB997 DEAF21BC A4D0E8EB 706AFF93 CCFCAC28 9858645E` 

- `B : 6A1D5F49 C312703F D8DB8B9A 4008EA63 2F3F32E9 B247EEB1 8FA11190 BCF24A31 519872AF 908A8A0F 2B67AA47 3D2B60CC 1E4B9BFE 491EF4F8 0ED4FF46 DE384264` 

- `C : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : 31F27E78 3D42EF58 A5D409BE 17C42E99 4F341777 40F90AE5 7F89E078 3F3E37F8 D619A8FA EFF73328 723396D0 3BA31091` 

- `B : 965760B8 4C90F859 66054B6C F530CAB5 779832D7 748711B4 928E4A0E BDB87B0D 6D3D64D9 E3A804B8 0CE4A2CF 926D10FE 8C5CDF74 2D3B1CEA 9DDFE10B 7CB14CCE` 

- `C : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : 23DD44CC CC74D106 D99B37D8 429EB8F6 789EFCB1 3B98A35C DDB85A3F CE00C04C 842C3359 552123AF 8EEBD747 14B2A6A7` 

- `B : D4163C6A 49313E63 0D1ACCBE 7AD73B3E 3312DE9D DA850D91 03785C3A C611B112 5D1BCAFC 033755D2 3B8EE05E 15251E4E 636A724F F0A8E584 4AABEAAF 122FC0C4` 

- `C : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - add C to A` 

- `A : 37661E10 1BEDBBD5 B022D077 CB1781BD 23DCFA84 AF4946EC 9C681ADD 8C48B88C 6BC4D0CB 1F4A95CD 0F2C5CD4 D1BC38C6` 

- `B : D4163C6A 49313E63 0D1ACCBE 7AD73B3E 3312DE9D DA850D91 03785C3A C611B112 5D1BCAFC 033755D2 3B8EE05E 15251E4E 636A724F F0A8E584 4AABEAAF 122FC0C4` 

- `C : CA3AFE3C 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

255 

```
W:0000000200000000
```

```
n0_final=2:subtractMfromC
```

- `A : 37661E10 1BEDBBD5 B022D077 CB1781BD 23DCFA84 AF4946EC 9C681ADD 8C48B88C 6BC4D0CB 1F4A95CD 0F2C5CD4 D1BC38C6` 

- `B : D4163C6A 49313E63 0D1ACCBE 7AD73B3E 3312DE9D DA850D91 03785C3A C611B112 5D1BCAFC 033755D2 3B8EE05E 15251E4E 636A724F F0A8E584 4AABEAAF 122FC0C4` 

- `C : CA3AFDBC 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : 37661E10 1BEDBBD5 B022D077 CB1781BD 23DCFA84 AF4946EC 9C681ADD 8C48B88C 6BC4D0CB 1F4A95CD 0F2C5CD4 D1BC38C6` 

- `B : CA3AFDBC 298219E1 5E0BF2B8 8F151F6D 648A1FC9 C1F29FEE CD9F4978 F81C514A 44EB858B D33B06CF 929CBC10 60672CBB 20B3CCCA EB12DED0 5CCD8C97 240C8D1C` 

- `C : D4163C6A 49313E63 0D1ACCBE 7AD73B3E 3312DE9D DA850D91 03785C3A C611B112 5D1BCAFC 033755D2 3B8EE05E 15251E4E 636A724F F0A8E584 4AABEAAF 122FC0C4` 

- `W : 00000002 00000000` 

```
Hashvalue(wordarray):
```

- `H : 3312DE9D DA850D91 03785C3A C611B112 5D1BCAFC 033755D2 3B8EE05E 15251E4E 636A724F F0A8E584 4AABEAAF 122FC0C4` 

```
Hashvalue(bytearray):
```

- `H : 9D DE 12 33 91 0D 85 DA 3A 5C 78 03 12 B1 11 C6 FC CA 1B 5D D2 55 37 03 5E E0 8E 3B 4E 1E 25 15 4F 72 6A 63 84 E5 A8 F0 AF EA AB 4A C4 C0 2F 12` 

### **B.8 Intermediate States for Shabal-384 (Message B)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:messageblock
```

- `M : 00000180 00000181 00000182 00000183 00000184 00000185 00000186 00000187 00000188 00000189 0000018A 0000018B 0000018C 0000018D 0000018E 0000018F` 

256 

```
blocknumber=-1:addMtoB
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000180 00000181 00000182 00000183 00000184 00000185 00000186 00000187 00000188 00000189 0000018A 0000018B 0000018C 0000018D 0000018E 0000018F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:xorcounterWintoA
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000180 00000181 00000182 00000183 00000184 00000185 00000186 00000187 00000188 00000189 0000018A 0000018B 0000018C 0000018D 0000018E 0000018F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 03000000 03020000 03040000 03060000 03080000 030A0000 030C0000 030E0000 03100000 03120000 03140000 03160000 03180000 031A0000 031C0000 031E0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=0)
```

- `A : 73B2093A 2A799470 05BF52F2 607A3AE1 BDA5E845 9A4F4C59 45672DC2 977B1FC2 FD372A8B D7D97B33 8A5D1B6E 4D17CE45` 

- `B : 05080182 F1B8E8B6 D44C4392 F9C1290D 444A17BA 63A4B3A6 BC80D23D 6E98E03D 04E8D574 2E0284CC 738AE491 B4C431BA 8A7DF6C5 D3B26B8F FC78AD0D 99B9C51E` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : 34DCDD7F 3399F8DC A47ABF91 51043F32 FDF93568 64558055 3E48B569 0D011A26 DB56076A C383CE67 FA750B12 041BF733` 

- `B : AF9C5E68 55490C52 C44C5DCB C0EE508F AC3DD7E1 FB3556D4 7C8B5096 26D5C8B6 C2F28868 90630EBB BC90894C C773A3B8 16FD271C 3CCEA8B5 3946108D C18D6FE4` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

257 

```
0000000000000000000000000000000000000000000000000000000000000000
```

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:subtractMfromC
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `C : FFFFFE80 FFFFFE7F FFFFFE7E FFFFFE7D FFFFFE7C FFFFFE7B FFFFFE7A FFFFFE79 FFFFFE78 FFFFFE77 FFFFFE76 FFFFFE75 FFFFFE74 FFFFFE73 FFFFFE72 FFFFFE71` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : FFFFFE80 FFFFFE7F FFFFFE7E FFFFFE7D FFFFFE7C FFFFFE7B FFFFFE7A FFFFFE79 FFFFFE78 FFFFFE77 FFFFFE76 FFFFFE75 FFFFFE74 FFFFFE73 FFFFFE72 FFFFFE71` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : FFFFFE80 FFFFFE7F FFFFFE7E FFFFFE7D FFFFFE7C FFFFFE7B FFFFFE7A FFFFFE79` 

258 

```
FFFFFE78FFFFFE77FFFFFE76FFFFFE75FFFFFE74FFFFFE73FFFFFE72FFFFFE71
```

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:messageblock
```

- `M : 00000190 00000191 00000192 00000193 00000194 00000195 00000196 00000197 00000198 00000199 0000019A 0000019B 0000019C 0000019D 0000019E 0000019F` 

```
blocknumber=0:addMtoB
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:xorcounterWintoA
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-rotateB
```

- `A : BB22A196 A1C1B9EC 8B50D287 4092494B 4A0B904D 1065A62A 15AFF6D9 88EECBDD 62189375 B55DE3B3 3FF60DE6 FA67BCE3` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=0)
```

- `A : CCCBA1B5 9E2FD849 89AD738F EA03554C 4C6371DE B511FBE1 C32FB2C4 E167BC5D A3B8F2F7 861F866F 0FA17732 5CBE8AEC` 

- `B : 86817371 DAB4EDE3 FC92F8B3 09D76240 B3DC8E21 4AAE041E 3C904D3B 1ED843A2 5C070D08 79A07990 F01E88CD A3017513 33745E4A 619027B6 76128C70 15BCAAB3` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

259 

###### `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : B98F348F 138FE48E 0084D32A B0E0FA9B 421966F9 31F37984 0D872018 F8EA2855 42A78E98 D97ED055 AC4EF3A7 14091C2E` 

- `B : A9DBD892 301E9E26 6FE8F3E6 D673177A DAE16D24 B3DD2796 2A91962E D6466495 FE7ED160 1F30E851 1F463D4E 091DEF43 DB0E2592 0D2CC917 1E5DC707 2C6C82CC` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : B4347AD7 C625A866 FA943F56 024604B5 6D6C6BE2 A28D22F0 68B51EB5 F354CB75 35D6B3E1 CD7F33BC 69707FFC 6C1B1417` 

- `B : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-addCtoA
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : 5272938C 2A1646F0 78E62977 944F1832 1CA6F1AA A854EBBA 8DB98C54 F2C627D8 30117F63 CF5C44A2 93711BBF F9F67353 B01D22B2 333F4D26 B285D303 86829CD5` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `C : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

260 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : 527291FC 2A16455F 78E627E5 944F169F 1CA6F016 A854EA25 8DB98ABE F2C62641 30117DCB CF5C4309 93711A25 F9F671B8 B01D2116 333F4B89 B285D165 86829B36` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 302D7A79 34333231 38373635 42412D39 46454443 4A494847 4E4D4C4B 5251504F 56555453 5A595857` 

```
blocknumber=1:addMtoB
```

- `A : C8FCA331 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : B6D5F45D 927DABC4 E551924E 04BE850C 911A6287 20CC609A BDE70537 26F95872 6848B400 119D7042 D9B65E68 443FB9FF FE6A6D61 85909BD8 08DB25B8 E0DBF38D` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

```
W:0000000100000000
```

```
blocknumber=1:xorcounterWintoA
```

- `A : C8FCA330 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : B6D5F45D 927DABC4 E551924E 04BE850C 911A6287 20CC609A BDE70537 26F95872 6848B400 119D7042 D9B65E68 443FB9FF FE6A6D61 85909BD8 08DB25B8 E0DBF38D` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : C8FCA330 E55C504E 003EBF26 BB6B8D83 7B0448C1 41B82789 0A7C9601 8D659CFF B6E2673E CA54C77B 1460FD7E 3FCB8F2D` 

- `B : E8BB6DAB 578924FB 249DCAA3 0A18097D C50F2234 C1344198 0A6F7BCE B0E44DF2 6800D091 E084233A BCD1B36C 73FE887F DAC3FCD4 37B10B21 4B7011B6 E71BC1B7` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

261 

```
blocknumber=1:permutation(j=0)
```

- `A : 7A6E1776 DDF02970 D65D1D53 BAE24561 94D00BB5 B33B9301 201C72B1 241B1BA9 DFFFF69C 3C1F4733 F8959DC0 E20B74B0` 

- `B : 57F1D267 E7A41B5F 0DC104BC B403D9FC E131B023 CEACEFCF CB3D7AD2 BA2C7FB3 F001A841 02E8FEB9 7EC904E6 FA099BB1 30161120 4D6DC0CD BF42C1C0 8B2A39F1` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : 62CDE717 7C878A2A F18DF07D D07D4C1E 62FC6E38 D68DA6EA D27ACA81 18B395DF D32F10CD 8C02A241 D174FEBD 52541198` 

- `B : 7E8D36A0 F8FF91B9 035A767F 8133DD8D EEB38F75 EEA48221 B8F1F4E7 D9F31100 7D31486B 86A988A7 F3E0064E DB918482 FD2FB387 B3A9D88F 5300B6FF F11819C3` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : 0D3444D1 A2C4A76B 6F438852 4C30C6D3 3D4487EC 40C7C67B D901E7E7 AD4F7F14 26F1A6B1 623E0EEF 76A36B21 FAD1A8BD` 

- `B : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : BDD5A0E6 1467BF21 6C9420B9 15A45522 208A2C56 A4A40DD2 108C2F8E 76559B2C 5D8A46B7 4AEAAC67 60EFEFEF 9F153F95` 

- `B : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `C : F764B11A 76172146 CEF6934D C6D28399 FE095F61 5E6018B4 5048ECF5 51353261 6E6E36DC 63130DAD A9C69BD6 1E90EA0C 7C35073B 28D95E6D AA340E0D CB3DEE70` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : BDD5A0E6 1467BF21 6C9420B9 15A45522 208A2C56 A4A40DD2 108C2F8E 76559B2C 5D8A46B7 4AEAAC67 60EFEFEF 9F153F95` 

- `B : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `C : 93014EB9 0DAFBAE1 628B28E4 5663152C 8995ECF0 E5E8A23F 201B727C 1D020030 363700A7 20D1E074 63815793 D447A1C5 2DE7BAF0 D6880E1E 53DEB9BA 70E49619` 

262 

###### `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : BDD5A0E6 1467BF21 6C9420B9 15A45522 208A2C56 A4A40DD2 108C2F8E 76559B2C 5D8A46B7 4AEAAC67 60EFEFEF 9F153F95` 

- `B : 93014EB9 0DAFBAE1 628B28E4 5663152C 8995ECF0 E5E8A23F 201B727C 1D020030 363700A7 20D1E074 63815793 D447A1C5 2DE7BAF0 D6880E1E 53DEB9BA 70E49619` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : BDD5A0E6 1467BF21 6C9420B9 15A45522 208A2C56 A4A40DD2 108C2F8E 76559B2C 5D8A46B7 4AEAAC67 60EFEFEF 9F153F95` 

- `B : 93014EB9 0DAFBAE1 628B28E4 5663152C 8995ECF0 E5E8A23F 201B727C 1D020030 363700A7 20D1E074 63815793 D447A1C5 2DE7BAF0 D6880E1E 53DEB9BA 70E49619` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 3231302D 36353433 2D393837 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 00807A79 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : BDD5A0E6 1467BF21 6C9420B9 15A45522 208A2C56 A4A40DD2 108C2F8E 76559B2C 5D8A46B7 4AEAAC67 60EFEFEF 9F153F95` 

- `B : C5327EE6 43E4EF14 8FC4611B BAC6778D F1FD5355 52540CA8 908AE0E9 917572A1 AEAE771C 21525AED 63815793 D447A1C5 2DE7BAF0 D6880E1E 53DEB9BA 70E49619` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

```
blocknumber=2:xorcounterWintoA
```

- `A : BDD5A0E4 1467BF21 6C9420B9 15A45522 208A2C56 A4A40DD2 108C2F8E 76559B2C 5D8A46B7 4AEAAC67 60EFEFEF 9F153F95` 

- `B : C5327EE6 43E4EF14 8FC4611B BAC6778D F1FD5355 52540CA8 908AE0E9 917572A1 AEAE771C 21525AED 63815793 D447A1C5 2DE7BAF0 D6880E1E 53DEB9BA 70E49619` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

263 

- `A : BDD5A0E4 1467BF21 6C9420B9 15A45522 208A2C56 A4A40DD2 108C2F8E 76559B2C 5D8A46B7 4AEAAC67 60EFEFEF 9F153F95` 

- `B : FDCD8A64 DE2887C9 C2371F88 EF1B758C A6ABE3FA 1950A4A8 C1D32115 E54322EA EE395D5C B5DA42A4 AF26C702 438BA88F 75E05BCF 1C3DAD10 7374A7BD 2C32E1C9` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : C1621A94 41DAD100 646F34DE 55E98D21 962B3AB6 B15F2393 B1EE66F1 49C50EB1 D1075BD1 C7DA6DCB 55B384F0 2B94E072` 

- `B : CD8EE412 980BB0AD 7F95EAD0 3CE38023 248302BC 7C01953C CDB7DB25 7CBCB49B F28A1E97 5391177D F401F50A 537C4E93 D55D52F5 865E74DF 7D79845B F273B14C` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=1)
```

- `A : 96BCB891 93A5C50B 1ECEEEDC 23677846 8295EE09 2DD7F4FD 9F40DA5D 12625134 74516C2E 41B17558 B8B8517C BE50CC99` 

- `B : 28E9F955 9B957C39 6C40E1CB D1333331 C2A896A9 464DA0DF DC2818C8 B8D65A50 8C577A41 CB78140E 0932FB36 7A601A9F D7D0B41D DE94E2BD 9A4C2D14 097ACC52` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : C98DF9C8 1B9A2E9B 3A634908 382A3427 E4878759 64B26D5A 5A8F2219 BBBAD729 E62E6EB4 846E49F4 A0F9A526 8ACE8904` 

- `B : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : 1CDD8460 9F7B05F6 A003B3C3 E294E519 526CA330 FE1BEF39 78087590 F805A380 5288AFB4 104616BF CE696AD7 5CCA350B` 

- `B : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `C : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

264 

```
blocknumber=2:subtractMfromC
```

- `A : 1CDD8460 9F7B05F6 A003B3C3 E294E519 526CA330 FE1BEF39 78087590 F805A380 5288AFB4 104616BF CE696AD7 5CCA350B` 

- `B : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `C : FEB1C328 B46699A2 6C73E139 223A3984 C7453F60 1406F26E 70F02FF5 8BB5A8BC C0627250 B1EAAE52 C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : 1CDD8460 9F7B05F6 A003B3C3 E294E519 526CA330 FE1BEF39 78087590 F805A380 5288AFB4 104616BF CE696AD7 5CCA350B` 

- `B : FEB1C328 B46699A2 6C73E139 223A3984 C7453F60 1406F26E 70F02FF5 8BB5A8BC C0627250 B1EAAE52 C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `C : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : add M to B` 

- `A : 1CDD8460 9F7B05F6 A003B3C3 E294E519 526CA330 FE1BEF39 78087590 F805A380 5288AFB4 104616BF CE696AD7 5CCA350B` 

- `B : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `C : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `W : 00000002 00000000` 

```
n0_final=0:xorcounterWintoA
```

- `A : 1CDD8462 9F7B05F6 A003B3C3 E294E519 526CA330 FE1BEF39 78087590 F805A380 5288AFB4 104616BF CE696AD7 5CCA350B` 

- `B : 30E2F355 EA9BCDD5 99AD1970 869D9BE5 2FACA5C5 80725CD7 E15F9E62 00291B2D 38D9E8C5 B26B28CB C13E1485 E59389EE 23513E41 FA92400F 2F5DF920 E71E64C5` 

- `C : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : 1CDD8462 9F7B05F6 A003B3C3 E294E519 526CA330 FE1BEF39 78087590 F805A380 5288AFB4 104616BF CE696AD7 5CCA350B` 

- `B : E6AA61C5 9BABD537 32E1335A 37CB0D3B 4B8A5F59 B9AF00E4 3CC5C2BF 365A0052 D18A71B3 519764D6 290B827C 13DDCB27 7C8246A2 801FF524 F2405EBB C98BCE3C` 

- `C : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79` 

265 

```
03D68C250DBDBAB8B7152B8AB0851DE8B670F970C6B873706B9E00F067C4EE5F
```

```
W:0000000200000000
```

- `n0_final = 0 : permutation (j = 0)` 

- `A : 37F8FEB6 65C6EBD9 91C48E11 EB2AD4AF 161441CB 9628F755 AF1E2252 E21B3462 F7D6F016 B6AC98CE 622A2142 DB40F538` 

- `B : 13519207 D285B64E 51F78425 80A08DE1 7EFF0086 1A890963 296A58D3 7150CB39 AB3DEC8E EA7DAE9D CFC2DA45 03049C89 31038C0D 9A06FE6F 8ABBCC99 87C2B729` 

- `C : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : 56A48A27 12C42D25 9731E707 3B293489 DD497502 163AACCF AC4E260B 1CA47C57 534979CA 434BA096 D56E0E11 17E5A4BE` 

- `B : A021A1AA DDE70D42 7A60B561 A2196A17 51488739 89A64DAF 78454048 0ABBCD33 FF20ACC5 39C08FE1 F74BAC73 C2DFF264 40B192E7 DDC8AFEF 46C640C7 ECDEEDFB` 

- `C : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

- `A : 405CB774 99277B8C 828C69C1 230CBE92 3EC5764E 1FE1F7BD 405620E2 AE36D90B 8E5DE0C1 026056E6 E11FD4A7 E3073C49` 

- `B : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `C : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : F22DBADB DA01C0F9 B07CE884 648CE14A F68ADB46 AE21CFDF B54BE6ED 3B2E265D 8EE37542 6FCB07DF 1E9493A9 8386F029` 

- `B : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `C : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : subtract M from C` 

- `A : F22DBADB DA01C0F9 B07CE884 648CE14A F68ADB46 AE21CFDF B54BE6ED 3B2E265D 8EE37542 6FCB07DF 1E9493A9 8386F029` 

- `B : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B` 

266 

   - `3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `C : A514F06C C8044646 2ADC622B 352394BF 4ABBC4FF FC932671 0D5D18F9 42060D08 8B5F15B0 0D3D403F B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : swap B with C` 

- `A : F22DBADB DA01C0F9 B07CE884 648CE14A F68ADB46 AE21CFDF B54BE6ED 3B2E265D 8EE37542 6FCB07DF 1E9493A9 8386F029` 

- `B : A514F06C C8044646 2ADC622B 352394BF 4ABBC4FF FC932671 0D5D18F9 42060D08 8B5F15B0 0D3D403F B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `C : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

- `A : F22DBADB DA01C0F9 B07CE884 648CE14A F68ADB46 AE21CFDF B54BE6ED 3B2E265D 8EE37542 6FCB07DF 1E9493A9 8386F029` 

- `B : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `C : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `W : 00000002 00000000` 

```
n0_final=1:xorcounterWintoA
```

- `A : F22DBAD9 DA01C0F9 B07CE884 648CE14A F68ADB46 AE21CFDF B54BE6ED 3B2E265D 8EE37542 6FCB07DF 1E9493A9 8386F029` 

- `B : D7462099 FE397A79 58159A62 9986F720 B3232B64 68FE90DA 7DCC8766 B6797F79 03D68C25 0DBDBAB8 B7152B8A B0851DE8 B670F970 C6B87370 6B9E00F0 67C4EE5F` 

- `C : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

- `A : F22DBAD9 DA01C0F9 B07CE884 648CE14A F68ADB46 AE21CFDF B54BE6ED 3B2E265D 8EE37542 6FCB07DF 1E9493A9 8386F029` 

- `B : 4133AE8C F4F3FC72 34C4B02B EE41330D 56C96646 21B4D1FD 0ECCFB99 FEF36CF2 184A07AD 75701B7B 57156E2A 3BD1610A F2E16CE1 E6E18D70 01E0D73C DCBECF89` 

- `C : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : 7A7FAB0C 81526FA0 B31A1667 0391CAE7 6D7CC15C 10709079 28FB14F2 F83DBBC2` 

267 

```
3925F48E1794C5FE5B3F955E5FF53CF5
```

```
B:67ECF95CC44D6B6D5C6B53FDED1273393F11F22FACE6CC7CCA9D1C3FFA249DD8
F64E042B028B0CF70AEAB6F5D7A8011E60428D30B36E8ABE4F2447E04513AA0B
```

```
C:63173B96B402591C34ED61CF2D5C619A1D3246F975941F2C8DF916AEC984DB0B
3F7BD03A939F1780513E87FAD476C23DF0C13AF0460EF6C6936CAAD6C5451841
```

```
W:0000000200000000
```

```
n0_final=1:permutation(j=1)
```

```
A:D377F9BD6DD422F4697DBDEF9D8B94C4FBD3908D3CDD3EAEFF47969E3EA721F7
C18EA1D50614C29B331C3A5B129C7788
```

```
B:CAA87BBEDF3053E16967B887DD9604D44052BA74A026A59D59D9FDDB192AB3C6
C0140E15973DC4E583572FFACD246906C4A97512A5FFD42C9EF0E6A14B7F8A1E
```

```
C:63173B96B402591C34ED61CF2D5C619A1D3246F975941F2C8DF916AEC984DB0B
3F7BD03A939F1780513E87FAD476C23DF0C13AF0460EF6C6936CAAD6C5451841
```

```
W:0000000200000000
```

- `n0_final = 1 : permutation (j = 2)` 

- `A : 11334407 E269A64C B805785A 8A5B98C4 4B2CB453 E5112548 54620017 7B0103DB 2C263CF3 90FEE027 D17F1169 11B5B480` 

- `B : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `C : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

```
W:0000000200000000
```

```
n0_final=1:permutation-addCtoA
```

```
A:D84B801F537463CB27AAE768E0AEBC1707530939A4D6781111978FDF8F260452
```

```
F77E3BD5DE6E324A20C13EDB8459FDFE
```

```
B:051BA4F7492F2AE0A31FF63D05CE22576E69CF105DDB1288F4497C1347F100B7
34FB57873495537CAD33A01D1EB62E295A8B292924FEB781136123D578B55F43
```

```
C:63173B96B402591C34ED61CF2D5C619A1D3246F975941F2C8DF916AEC984DB0B
3F7BD03A939F1780513E87FAD476C23DF0C13AF0460EF6C6936CAAD6C5451841
```

```
W:0000000200000000
```

```
n0_final=1:subtractMfromC
```

```
A:D84B801F537463CB27AAE768E0AEBC1707530939A4D6781111978FDF8F260452
```

```
F77E3BD5DE6E324A20C13EDB8459FDFE
```

```
B:051BA4F7492F2AE0A31FF63D05CE22576E69CF105DDB1288F4497C1347F100B7
34FB57873495537CAD33A01D1EB62E295A8B292924FEB781136123D578B55F43
```

```
C:30E60B697DCD24E907B42998C8F8FF39B4CAE0940928B4C31D89A8415511689A
C70459C5931E9D07513E87FAD476C23DF0C13AF0460EF6C6936CAAD6C5451841
```

```
W:0000000200000000
```

268 

```
n0_final=1:swapBwithC
```

- `A : D84B801F 537463CB 27AAE768 E0AEBC17 07530939 A4D67811 11978FDF 8F260452 F77E3BD5 DE6E324A 20C13EDB 8459FDFE` 

- `B : 30E60B69 7DCD24E9 07B42998 C8F8FF39 B4CAE094 0928B4C3 1D89A841 5511689A C70459C5 931E9D07 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `C : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `W : 00000002 00000000` 

```
n0_final=2:addMtoB
```

- `A : D84B801F 537463CB 27AAE768 E0AEBC17 07530939 A4D67811 11978FDF 8F260452 F77E3BD5 DE6E324A 20C13EDB 8459FDFE` 

- `B : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `C : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `W : 00000002 00000000` 

- `n0_final = 2 : xor counter W into A` 

- `A : D84B801D 537463CB 27AAE768 E0AEBC17 07530939 A4D67811 11978FDF 8F260452 F77E3BD5 DE6E324A 20C13EDB 8459FDFE` 

- `B : 63173B96 B402591C 34ED61CF 2D5C619A 1D3246F9 75941F2C 8DF916AE C984DB0B 3F7BD03A 939F1780 513E87FA D476C23D F0C13AF0 460EF6C6 936CAAD6 C5451841` 

- `C : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - rotate B` 

- `A : D84B801D 537463CB 27AAE768 E0AEBC17 07530939 A4D67811 11978FDF 8F260452 F77E3BD5 DE6E324A 20C13EDB 8459FDFE` 

- `B : 772CC62E B2396804 C39E69DA C3345AB8 8DF23A64 3E58EB28 2D5D1BF2 B6179309 A0747EF7 2F01273E 0FF4A27D 847BA8ED 75E1E182 ED8C8C1D 55AD26D9 30838A8A` 

- `C : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 0)` 

- `A : 96B22A2E 7E596DA0 39851350 5B993B8B D05FD685 6FD3086E 159504C0 ABFE4E42 89A3173F 2839BDE6 1271F888 EB2A3DA9` 

- `B : 8EFE3C4D 8800DA08 FE381C10 132D2BE8 34445DB3 EC9D21C1 B0D0CCDB 382E97AE 36B4152F 89C40C65 F267438D 1C22938D 828E16D5 5ABF8A64 6D20A11D C561D160` 

- `C : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

269 

###### `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : 2E5F9370 47C6AA9B 52F67D34 7E6B4C97 0404918E 1E580D65 3A596788 5E0BADA7 CEFB86A2 F6147458 385A5BB3 F870E621` 

- `B : 52E38CF3 E821067A 035EEE61 B645C86B 598CC23B D0D1C824 A6043DFB 77D23682 BCC846D1 ABB14DAF 49C705D0 B9D19472 FEE743DA 54D8E652 1FE7DA4D 2B37F099` 

- `C : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : 42CA7AB9 551AB388 71D002DF C21F9B38 1C09FBFD 3FE7495A 1B5E1B4C 28289356 CCFA8970 72FAC99E 304343E9 097BE5F5` 

- `B : 6D085ED6 71C06B61 6D009973 9317C3EB 0E2C0130 0B46DC3E C22786D7 D24409C3 9A6689A1 977A2DFA 772FEF13 A474444C CECBF13A 24B4FAC5 F073088C A0EBFB38` 

- `C : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - add C to A` 

- `A : E0042A7C 232B50B8 3DD8F7C8 6CEA315D E27E7E4E E86814E8 F6FDAC30 6CC5A5C3 396FDAA7 70EB195E E7B2616E BE5A25FA` 

- `B : 6D085ED6 71C06B61 6D009973 9317C3EB 0E2C0130 0B46DC3E C22786D7 D24409C3 9A6689A1 977A2DFA 772FEF13 A474444C CECBF13A 24B4FAC5 F073088C A0EBFB38` 

- `C : 051BA4F7 492F2AE0 A31FF63D 05CE2257 6E69CF10 5DDB1288 F4497C13 47F100B7 34FB5787 3495537C AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : E0042A7C 232B50B8 3DD8F7C8 6CEA315D E27E7E4E E86814E8 F6FDAC30 6CC5A5C3 396FDAA7 70EB195E E7B2616E BE5A25FA` 

- `B : 6D085ED6 71C06B61 6D009973 9317C3EB 0E2C0130 0B46DC3E C22786D7 D24409C3 9A6689A1 977A2DFA 772FEF13 A474444C CECBF13A 24B4FAC5 F073088C A0EBFB38` 

- `C : D2EA74CA 12F9F6AD 75E6BE06 A16ABFF6 060268AB F16FA81F 83DA0DA6 D37D8E46 BC83E112 3414D903 AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : E0042A7C 232B50B8 3DD8F7C8 6CEA315D E27E7E4E E86814E8 F6FDAC30 6CC5A5C3 396FDAA7 70EB195E E7B2616E BE5A25FA` 

- `B : D2EA74CA 12F9F6AD 75E6BE06 A16ABFF6 060268AB F16FA81F 83DA0DA6 D37D8E46 BC83E112 3414D903 AD33A01D 1EB62E29 5A8B2929 24FEB781 136123D5 78B55F43` 

270 

- `C : 6D085ED6 71C06B61 6D009973 9317C3EB 0E2C0130 0B46DC3E C22786D7 D24409C3 9A6689A1 977A2DFA 772FEF13 A474444C CECBF13A 24B4FAC5 F073088C A0EBFB38` 

- `W : 00000002 00000000` 

```
Hashvalue:
```

- `H : 0E2C0130 0B46DC3E C22786D7 D24409C3 9A6689A1 977A2DFA 772FEF13 A474444C CECBF13A 24B4FAC5 F073088C A0EBFB38` 

```
Hashvalue(bytearray):
```

- `H : 30 01 2C 0E 3E DC 46 0B D7 86 27 C2 C3 09 44 D2 A1 89 66 9A FA 2D 7A 97 13 EF 2F 77 4C 44 74 A4 3A F1 CB CE C5 FA B4 24 8C 08 73 F0 38 FB EB A0` 

### **B.9 Intermediate States for Shabal-512 (Message A)** 

```
init
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
W:FFFFFFFFFFFFFFFF
```

```
blocknumber=-1:messageblock
```

- `M : 00000200 00000201 00000202 00000203 00000204 00000205 00000206 00000207 00000208 00000209 0000020A 0000020B 0000020C 0000020D 0000020E 0000020F` 

```
blocknumber=-1:addMtoB
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000200 00000201 00000202 00000203 00000204 00000205 00000206 00000207 00000208 00000209 0000020A 0000020B 0000020C 0000020D 0000020E 0000020F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:xorcounterWintoA
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000200 00000201 00000202 00000203 00000204 00000205 00000206 00000207 00000208 00000209 0000020A 0000020B 0000020C 0000020D 0000020E 0000020F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

271 

```
W:FFFFFFFFFFFFFFFF
```

```
blocknumber=-1:permutation-rotateB
```

```
A:FFFFFFFFFFFFFFFF000000000000000000000000000000000000000000000000
00000000000000000000000000000000
```

```
B:0400000004020000040400000406000004080000040A0000040C0000040E0000
0410000004120000041400000416000004180000041A0000041C0000041E0000
C:0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
W:FFFFFFFFFFFFFFFF
blocknumber=-1:permutation(j=0)
```

<!-- Start of picture text -->
A : E2AA101E 3A5C2CEA E01C099D 8D1BE979 1C49D94D 7A06796B E9703766 7C25F07F<br>FEB14424 C24293CA BC669928 76D9392D<br>B : 0C080202 FCF8E3B6 A7CC2F72 67D0264D EBA626B2 8DED8694 1E97C899 8BC60F80<br>096EBBDB 35996C35 4BB166D7 810AC6D2 1565EFE1 CD97D315 17DBF662 7AD81686<br>C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000<br>00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000<br>W : FFFFFFFF FFFFFFFF<br>block number = -1 : permutation (j = 1)<br><!-- End of picture text -->

```
A:E524968F5F83748F98E7810D23285DCF2195FE4E7188ACDA7AF7FC8331F5BA1C
CC8D57434E46BE5DDAE5E19BBCEB09F1
```

```
B:98C2A26E203FE12991D449C486D27C0EE43EE5D9AA624C8B18358F565498E90F
08061EC6CB4E531AF07AB35CDEC22F95F4A1DE731558F50EAABFEFB83BBA68EF
C:0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
W:FFFFFFFFFFFFFFFF
blocknumber=-1:permutation(j=2)
A:DCED6C97B5937A56BC2D34794B2672FEA762CE01E0587D3EDAAA7818F9BF94BD
646EB744A0DA0A55C70BC02E292C7C6B
```

```
B:C1099EC707B38804E7442E38CC8AD853EB6F58DB1EA81CBE73B9D52A1DE85F1F
48910C72893B24F4C5A0E15EBBC4346972D2F45C75941FB66D8BE0A0A1A7524A
C:0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
```

```
W:FFFFFFFFFFFFFFFF
```

```
blocknumber=-1:permutation-addCtoA
```

```
A:DCED6C97B5937A56BC2D34794B2672FEA762CE01E0587D3EDAAA7818F9BF94BD
646EB744A0DA0A55C70BC02E292C7C6B
```

```
B:C1099EC707B38804E7442E38CC8AD853EB6F58DB1EA81CBE73B9D52A1DE85F1F
48910C72893B24F4C5A0E15EBBC4346972D2F45C75941FB66D8BE0A0A1A7524A
```

272 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
W:FFFFFFFFFFFFFFFF
```

```
blocknumber=-1:subtractMfromC
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `C : FFFFFE00 FFFFFDFF FFFFFDFE FFFFFDFD FFFFFDFC FFFFFDFB FFFFFDFA FFFFFDF9 FFFFFDF8 FFFFFDF7 FFFFFDF6 FFFFFDF5 FFFFFDF4 FFFFFDF3 FFFFFDF2 FFFFFDF1` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : FFFFFE00 FFFFFDFF FFFFFDFE FFFFFDFD FFFFFDFC FFFFFDFB FFFFFDFA FFFFFDF9 FFFFFDF8 FFFFFDF7 FFFFFDF6 FFFFFDF5 FFFFFDF4 FFFFFDF3 FFFFFDF2 FFFFFDF1` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : FFFFFE00 FFFFFDFF FFFFFDFE FFFFFDFD FFFFFDFC FFFFFDFB FFFFFDFA FFFFFDF9 FFFFFDF8 FFFFFDF7 FFFFFDF6 FFFFFDF5 FFFFFDF4 FFFFFDF3 FFFFFDF2 FFFFFDF1` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:messageblock
```

- `M : 00000210 00000211 00000212 00000213 00000214 00000215 00000216 00000217 00000218 00000219 0000021A 0000021B 0000021C 0000021D 0000021E 0000021F` 

```
blocknumber=0:addMtoB
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

273 

```
blocknumber=0:xorcounterWintoA
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-rotateB
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=0)
```

- `A : E3C2DE4A 15013A27 9779A969 2E533DBB F9542F32 1830E439 49354FD1 3FA73E25 62A98156 E3930697 3AEC9AE8 02836D8A` 

- `B : 15F96FCE BF883B5C 13B9B891 5F17F2CF 06EBD0CD E78F1BC6 B68AB02E C018C1DA 9D167EA9 1C2CF968 C5536517 FD3C9275 1C7D21B5 EABEC5D8 68C65696 D1ECC244` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : F762247A 9C5C1A1B 82879280 482A0C43 F996F842 F06FAEB4 6FBAE548 DD572216 AC03820D 16A91946 E8198C7A C460216D` 

- `B : 3453DF4C 85E7DAA3 A8D88D92 0E0FE970 5E2BDC68 2648D134 7AF313D8 BBAE5D27 32B126D6 5BFA1734 F7DEA750 4DACD757 3E9344D7 DAEDDAFA 41C9B79B 81715960` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : F67C2EF7 2774D155 4B92F221 8CA66230 E59A65D4 199FE418 2C22673B DA3186CB 17D54265 E4FDEA67 595B4C44 81C61457` 

- `B : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F` 

274 

```
48910C72893B24F4C5A0E15EBBC4346972D2F45C75941FB66D8BE0A0A1A7524A
```

```
W:0000000000000000
```

```
blocknumber=0:permutation-addCtoA
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

275 

```
blocknumber=1:addMtoB
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:xorcounterWintoA
```

- `A : 20728DFC 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : 20728DFC 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : 396F8213 0BE60F67 584DCE88 AC819915 AD8FD6DE 35523D50 A628E773 BA103BD0 14B49122 45B71276 BE898B41 649D7788 E480E5A5 3B32EB28 BD04DB17 A057434E` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=0)
```

- `A : E09EDBEE C276F931 B0D8D4CE C640E1B5 58895064 B8D5F730 14A7145B C93F3B68 74AFE6B9 57F8351D D7447331 BACD8A8A` 

- `B : 2CDF3F8A 2983105F 77E22D44 383740E2 FC690226 2D8E726F A7092543 42E0B336 A2393B02 2369EE0E 55A89A4D 8C089A65 D660EF5A 4BECD09E 352E9D1E 791198D7` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : B44A2D19 F0309531 7F1C7793 C8EE5AA1 58680662 EB3F6CD2 7CF1E331 DE187243 C37AE049 287F262C A892AFC2 AF71D3FE` 

- `B : D69722B0 F74395E3 AA072FE9 9BFA6F6F C4571BFB 8C9C3D0D 197F1ABA D54F4A6D 0FC7A4E3 491CB6D2 2BB2BCF6 2F009195 0B562728 83193211 E95326F2 D3C4BC12` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

276 

###### `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : 648A9B4A BC9B82CF BA639897 20F00F46 B9BC68E2 E22AA0F7 9693C179 6145A212 2530A066 B7509372 69C4375A D41A85F9` 

- `B : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : 2132BFA6 E13B89AC 56129D16 DDB5A2F3 BBD1DD24 F0C64B27 D4FD5B1A 35342F97 690292D9 81390905 FE4C9A18 773E6359` 

- `B : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : 2132BFA6 E13B89AC 56129D16 DDB5A2F3 BBD1DD24 F0C64B27 D4FD5B1A 35342F97 690292D9 81390905 FE4C9A18 773E6359` 

- `B : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : 2132BFA6 E13B89AC 56129D16 DDB5A2F3 BBD1DD24 F0C64B27 D4FD5B1A 35342F97 690292D9 81390905 FE4C9A18 773E6359` 

- `B : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : 2132BFA6 E13B89AC 56129D16 DDB5A2F3 BBD1DD24 F0C64B27 D4FD5B1A 35342F97 690292D9 81390905 FE4C9A18 773E6359` 

- `B : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

277 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 00000080 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : 2132BFA6 E13B89AC 56129D16 DDB5A2F3 BBD1DD24 F0C64B27 D4FD5B1A 35342F97 690292D9 81390905 FE4C9A18 773E6359` 

- `B : D9BF6951 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

```
blocknumber=2:xorcounterWintoA
```

- `A : 2132BFA4 E13B89AC 56129D16 DDB5A2F3 BBD1DD24 F0C64B27 D4FD5B1A 35342F97 690292D9 81390905 FE4C9A18 773E6359` 

- `B : D9BF6951 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : 2132BFA4 E13B89AC 56129D16 DDB5A2F3 BBD1DD24 F0C64B27 D4FD5B1A 35342F97 690292D9 81390905 FE4C9A18 773E6359` 

- `B : D2A3B37E AEA0B175 1964AC05 E6B30269 D3B16BA8 19852835 54DC8316 4F00080A AF0EFE0F 6B1EA328 ACCA78C1 AF357D2F 68692A18 40DB5DB3 B91A4A6F B2D2F9B6` 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : F7A45AB6 1B7B9FDD D4AE951B 98E4D1C7 4052E830 3D1FBFEB 49353DB2 A6F893F7 B07B4DEA F089D424 BDC0D6F0 7B2B5AC3` 

- `B : B0848635 348DCAB2 11277606 A3647ED9 18CFC09E F1EA107E 1F73C461 C7077C1C 11994E0A D94B6D8B 1BABD88C DABE5F63 D889F179 6532DB44 5965FE3B 02BEDD55` 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

278 

```
blocknumber=2:permutation(j=1)
```

- `A : 9E9110D9 C861EBC1 4A80AA8B B28E5A69 BE4F19B6 B920408A CBB77E5D A598F1B6 49D3DDF2 78B226D9 37DF0A9E 2393870E` 

- `B : 7A0A5BA9 131423DD 891CBBA5 4AE41FC3 87B3A331 6499F9DB F6C77DA3 526280C8 425C7332 8508CF29 8228E46C F80D1B51 F0A304BA 8CBA09FD 86837DD4 5F1AB4E3` 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : 80F57FDC 5D4889F6 E62F1768 641AF882 BDCDCA7F 9AE71255 CFF6CE83 5B672F19 B9351F52 535483EF 8C3EB8EC 56356B34` 

- `B : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : 6ECB062B B23CE91A 0441049B C38B431C 60793669 7D453E8B 2F57E5B4 B4433BDD 903007E0 8D5FC7D5 C523FB71 503E89FA` 

- `B : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `C : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : 6ECB062B B23CE91A 0441049B C38B431C 60793669 7D453E8B 2F57E5B4 B4433BDD 903007E0 8D5FC7D5 C523FB71 503E89FA` 

- `B : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `C : 74B5F999 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : 6ECB062B B23CE91A 0441049B C38B431C 60793669 7D453E8B 2F57E5B4 B4433BDD 903007E0 8D5FC7D5 C523FB71 503E89FA` 

- `B : 74B5F999 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `C : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

279 

###### `W : 00000002 00000000` 

```
n0_final=0:addMtoB
```

- `A : 6ECB062B B23CE91A 0441049B C38B431C 60793669 7D453E8B 2F57E5B4 B4433BDD 903007E0 8D5FC7D5 C523FB71 503E89FA` 

- `B : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `C : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : xor counter W into A` 

- `A : 6ECB0629 B23CE91A 0441049B C38B431C 60793669 7D453E8B 2F57E5B4 B4433BDD 903007E0 8D5FC7D5 C523FB71 503E89FA` 

- `B : 74B5FA19 7518DD5A A370733E A0AE0565 13DB5342 5A5C072B 7762521C 75916462 59CCDEDB 8FEC32AC 3E09476A C0BB7EC7 CC6311C9 4E9D08AE 449D8540 8C6C0223` 

- `C : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - rotate B` 

- `A : 6ECB0629 B23CE91A 0441049B C38B431C 60793669 7D453E8B 2F57E5B4 B4433BDD 903007E0 8D5FC7D5 C523FB71 503E89FA` 

- `B : F432E96B BAB4EA31 E67D46E0 0ACB415C A68427B6 0E56B4B8 A438EEC4 C8C4EB22 BDB6B399 65591FD8 8ED47C12 FD8F8176 239398C6 115C9D3A 0A80893B 044718D8` 

- `C : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

- `A : 149D7202 183AC7E6 54A20EE4 71EFEB74 4B531C29 5B5C9818 91630F92 66A9BA59 8530F23A E9D24A81 265E3865 1AF5CFAB` 

- `B : 9597F988 DDAFB60C 9AAC0D55 3EF4CF5C F9A4ACBB B80E0E97 26ED2DE4 08DF93E3 01A26AF6 DC9F8ACE C4093FBF 1E1532B9 AC45BC71 C57C026D BE5CE36D 869E253B` 

- `C : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : DC5BAB2B 8C22F3E3 E64FD398 3FCC92AC F04712D0 395B6353 2C7F8D1F A8E0C0F6 EDF6D320 81F104D5 221FCB0E A9A74700` 

- `B : 0DCEF553 028E5C2D 74EF49F5 47B48CD3 E14075A8 0E12E605 903A6F39 47E79F39 20E08138 CAE21981 91A25318 FC190821 573395CC 4C5C9877 AF39B43B 5A23757E` 

280 

- `C : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

- `A : CCE62684 2BDFF7E8 53FEF52D AEFA4E31 69AB67CB A5759544 2A7D89AD B8A165CD C145171C 18B81F66 A5213421 22837339` 

- `B : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `C : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : 33DB4080 A739C7A7 16DA62B5 001109DB BB3DA26F 3FCD4F0F A682FB43 BF495E62 4F5A3AF8 F73DA362 358E9DC4 CA023D68` 

- `B : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `C : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `W : 00000002 00000000` 

- `n0_final = 0 : subtract M from C` 

- `A : 33DB4080 A739C7A7 16DA62B5 001109DB BB3DA26F 3FCD4F0F A682FB43 BF495E62 4F5A3AF8 F73DA362 358E9DC4 CA023D68` 

- `B : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `C : 635F1F27 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `W : 00000002 00000000` 

```
n0_final=0:swapBwithC
```

- `A : 33DB4080 A739C7A7 16DA62B5 001109DB BB3DA26F 3FCD4F0F A682FB43 BF495E62 4F5A3AF8 F73DA362 358E9DC4 CA023D68` 

- `B : 635F1F27 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `C : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

- `A : 33DB4080 A739C7A7 16DA62B5 001109DB BB3DA26F 3FCD4F0F A682FB43 BF495E62 4F5A3AF8 F73DA362 358E9DC4 CA023D68` 

281 

- `B : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `C : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : xor counter W into A` 

- `A : 33DB4082 A739C7A7 16DA62B5 001109DB BB3DA26F 3FCD4F0F A682FB43 BF495E62 4F5A3AF8 F73DA362 358E9DC4 CA023D68` 

- `B : 635F1FA7 A17777DE DDF0EB20 FA7236AA 706DC640 6B8485BF F45E13D0 3F2006ED C68AD3E4 6F0973F9 3458F9A5 5482E645 A78CE9D8 B5DF6FEB 7EC7BCBA 17FFFD0D` 

- `C : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

- `A : 33DB4082 A739C7A7 16DA62B5 001109DB BB3DA26F 3FCD4F0F A682FB43 BF495E62 4F5A3AF8 F73DA362 358E9DC4 CA023D68` 

- `B : 3F4EC6BE EFBD42EE D641BBE1 6D55F4E4 8C80E0DB 0B7ED709 27A1E8BC 0DDA7E40 A7C98D15 E7F2DE12 F34A68B1 CC8AA905 D3B14F19 DFD76BBE 7974FD8F FA1A2FFF` 

- `C : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : 91502CEF FA5B99ED AE56D69D 589B022C 7BDA9079 AA8CBB35 2FA4D3A1 DACFCDAB 1B913AB3 3D90A836 F648A85B 09B6DD66` 

- `B : E78664F6 6E75DC7F EEB05E27 4F27B4E0 9D24AE31 438EEAD8 9F18FD26 3E84CED4 ABFDDF67 0D8AEBEC EF2386C7 6F5C7092 C9CD4D23 BA0AB16F A340D27C 5350A22C` 

- `C : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

- `A : F0F3C949 1A14D83E 7FABC2E3 DCE75A6F 67C8EA56 A9ABF3BE 4C8A9A07 51256499 A2AE3DDD FC862E24 F276FC93 D03C05B4` 

- `B : F11E0201 221265AB D5A7D1A1 2F5F3B13 67189E41 8464046B 33B8F921 52CA67E3 58F78879 FEFEF019 5E133093 FDA044B4 0BAD8FEE 22416E9E F5F4C101 087BDF3E` 

- `C : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 2)` 

282 

- `A : 0C9FC9C6 7AC06949 2349DF2D 1E4407AD E84F7CB7 7DC90184 235A999E B72D5614 7B08EA46 44C9F247 6D16C208 6A402409` 

- `B : D90A5233 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `C : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - add C to A` 

- `A : 5FD62497 B6FAC8E0 44F0FFA7 1A109387 5AE3DCD3 00BB37E4 94514359 A5130EA8 43CF6E99 9ED68230 8469B054 F22A6CB6` 

- `B : D90A5233 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `C : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : subtract M from C` 

- `A : 5FD62497 B6FAC8E0 44F0FFA7 1A109387 5AE3DCD3 00BB37E4 94514359 A5130EA8 43CF6E99 9ED68230 8469B054 F22A6CB6` 

- `B : D90A5233 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `C : B9C36972 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `W : 00000002 00000000` 

- `n0_final = 1 : swap B with C` 

- `A : 5FD62497 B6FAC8E0 44F0FFA7 1A109387 5AE3DCD3 00BB37E4 94514359 A5130EA8 43CF6E99 9ED68230 8469B054 F22A6CB6` 

- `B : B9C36972 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `C : D90A5233 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `W : 00000002 00000000` 

- `n0_final = 2 : add M to B` 

- `A : 5FD62497 B6FAC8E0 44F0FFA7 1A109387 5AE3DCD3 00BB37E4 94514359 A5130EA8 43CF6E99 9ED68230 8469B054 F22A6CB6` 

- `B : B9C369F2 D9A28BE6 6AA91390 2A8F6A26 F199322A C805C41D 8C75D4A1 DECA8FBC D7959A44 CF4E59B8 F6C6D063 BF6C8A71 90DDC37B 7FFED077 04ADA3A9 693A663A` 

- `C : D90A5233 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `W : 00000002 00000000` 

283 

```
n0_final=2:xorcounterWintoA
```

```
A:5FD62495B6FAC8E044F0FFA71A1093875AE3DCD300BB37E494514359A5130EA8
43CF6E999ED682308469B054F22A6CB6
```

```
B:B9C369F2D9A28BE66AA913902A8F6A26F199322AC805C41D8C75D4A1DECA8FBC
```

```
D7959A44CF4E59B8F6C6D063BF6C8A7190DDC37B7FFED07704ADA3A9693A663A
```

```
C:D90A5233625DBAFCA04AE0F115BBA5843D510ABB8DF79E61BBC7D290442F3794
A65F93BA7FCB1E4860830747B392208293AC0A65FFB4D0847900BFF48548658A
```

```
W:0000000200000000
```

```
n0_final=2:permutation-rotateB
```

```
A:5FD62495B6FAC8E044F0FFA71A1093875AE3DCD300BB37E494514359A5130EA8
43CF6E999ED682308469B054F22A6CB6
```

```
B:D3E5738617CDB3452720D552D44C551E6455E332883B900BA94318EB1F79BD95
3489AF2BB3719E9CA0C7ED8D14E37ED986F721BBA0EEFFFD4752095BCC74D274
C:D90A5233625DBAFCA04AE0F115BBA5843D510ABB8DF79E61BBC7D290442F3794
A65F93BA7FCB1E4860830747B392208293AC0A65FFB4D0847900BFF48548658A
W:0000000200000000
```

```
n0_final=2:permutation(j=0)
```

```
A:B50F955E14BC3748C5FA1146194908C57004768BD42009BE0549683186CDE330
8C38660A26BE88397BE289004FCA5136
B:0829DF493335F5B02F241782C99DAF9D47504F103BA8D656A830A61947C167E5
1AD4C7A3BFA24AFFC592ADE499F3537B471E29D6AA9E374CB4A1FC0F7E5F53D3
```

```
C:D90A5233625DBAFCA04AE0F115BBA5843D510ABB8DF79E61BBC7D290442F3794
A65F93BA7FCB1E4860830747B392208293AC0A65FFB4D0847900BFF48548658A
W:0000000200000000
n0_final=2:permutation(j=1)
```

```
A:EEEC612F0C2858E0110AB337D2E00B4EF5654CBC0C7EE7138760F284AB6C79AE
```

```
F7C8228E1E53B0CE8A9CF5884F5F50B5
```

```
B:999630480D50ADA10A73C89117DCC13D8697435196FDE39D250246443F226080
24BA11968C9332E065D017011EF9524684A6E0EFA6BD767511DCF564A82D21F7
C:D90A5233625DBAFCA04AE0F115BBA5843D510ABB8DF79E61BBC7D290442F3794
A65F93BA7FCB1E4860830747B392208293AC0A65FFB4D0847900BFF48548658A
```

```
W:0000000200000000
```

```
n0_final=2:permutation(j=2)
```

###### `A : D13EEC24 6EE69F0F 10237A16 6772D8CD 218A7975 16EE22A1 149915B3 1E746A94` 

```
DD0795A20128DE2640A445618D95E288
```

```
B:C61680150A3F1FC8688DD9528E9E2FED23EF9578BCE2A7CBA5D80961E6C9E632
9701A5A6F037B89F20C6C44EDC7931E72BB5AB82B3ADCD329CE2505622305E98
C:D90A5233625DBAFCA04AE0F115BBA5843D510ABB8DF79E61BBC7D290442F3794
```

284 

```
A65F93BA7FCB1E4860830747B392208293AC0A65FFB4D0847900BFF48548658A
```

```
W:0000000200000000
```

- `n0_final = 2 : permutation - add C to A` 

- `A : 1FD517B4 18EE0662 002DA3F7 3C864C42 00BDBC17 D3A91349 84B98D58 DB0A255C EA84933C 78858700 4E1BD28E 22E17C53` 

- `B : C6168015 0A3F1FC8 688DD952 8E9E2FED 23EF9578 BCE2A7CB A5D80961 E6C9E632 9701A5A6 F037B89F 20C6C44E DC7931E7 2BB5AB82 B3ADCD32 9CE25056 22305E98` 

- `C : D90A5233 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : 1FD517B4 18EE0662 002DA3F7 3C864C42 00BDBC17 D3A91349 84B98D58 DB0A255C EA84933C 78858700 4E1BD28E 22E17C53` 

- `B : C6168015 0A3F1FC8 688DD952 8E9E2FED 23EF9578 BCE2A7CB A5D80961 E6C9E632 9701A5A6 F037B89F 20C6C44E DC7931E7 2BB5AB82 B3ADCD32 9CE25056 22305E98` 

- `C : D90A51B3 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : 1FD517B4 18EE0662 002DA3F7 3C864C42 00BDBC17 D3A91349 84B98D58 DB0A255C EA84933C 78858700 4E1BD28E 22E17C53` 

- `B : D90A51B3 625DBAFC A04AE0F1 15BBA584 3D510ABB 8DF79E61 BBC7D290 442F3794 A65F93BA 7FCB1E48 60830747 B3922082 93AC0A65 FFB4D084 7900BFF4 8548658A` 

- `C : C6168015 0A3F1FC8 688DD952 8E9E2FED 23EF9578 BCE2A7CB A5D80961 E6C9E632 9701A5A6 F037B89F 20C6C44E DC7931E7 2BB5AB82 B3ADCD32 9CE25056 22305E98` 

- `W : 00000002 00000000` 

```
Hashvalue(wordarray):
```

- `H : C6168015 0A3F1FC8 688DD952 8E9E2FED 23EF9578 BCE2A7CB A5D80961 E6C9E632 9701A5A6 F037B89F 20C6C44E DC7931E7 2BB5AB82 B3ADCD32 9CE25056 22305E98` 

```
Hashvalue(bytearray):
```

- `H : 15 80 16 C6 C8 1F 3F 0A 52 D9 8D 68 ED 2F 9E 8E 78 95 EF 23 CB A7 E2 BC 61 09 D8 A5 32 E6 C9 E6 A6 A5 01 97 9F B8 37 F0 4E C4 C6 20 E7 31 79 DC 82 AB B5 2B 32 CD AD B3 56 50 E2 9C 98 5E 30 22` 

### **B.10 Intermediate States for Shabal-512 (Message B)** 

```
init
```

285 

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:messageblock
```

- `M : 00000200 00000201 00000202 00000203 00000204 00000205 00000206 00000207 00000208 00000209 0000020A 0000020B 0000020C 0000020D 0000020E 0000020F` 

```
blocknumber=-1:addMtoB
```

- `A : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000200 00000201 00000202 00000203 00000204 00000205 00000206 00000207 00000208 00000209 0000020A 0000020B 0000020C 0000020D 0000020E 0000020F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:xorcounterWintoA
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 00000200 00000201 00000202 00000203 00000204 00000205 00000206 00000207 00000208 00000209 0000020A 0000020B 0000020C 0000020D 0000020E 0000020F` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-rotateB
```

- `A : FFFFFFFF FFFFFFFF 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `B : 04000000 04020000 04040000 04060000 04080000 040A0000 040C0000 040E0000 04100000 04120000 04140000 04160000 04180000 041A0000 041C0000 041E0000` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=0)
```

- `A : E2AA101E 3A5C2CEA E01C099D 8D1BE979 1C49D94D 7A06796B E9703766 7C25F07F FEB14424 C24293CA BC669928 76D9392D` 

- `B : 0C080202 FCF8E3B6 A7CC2F72 67D0264D EBA626B2 8DED8694 1E97C899 8BC60F80 096EBBDB 35996C35 4BB166D7 810AC6D2 1565EFE1 CD97D315 17DBF662 7AD81686` 

286 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=1)
```

- `A : E524968F 5F83748F 98E7810D 23285DCF 2195FE4E 7188ACDA 7AF7FC83 31F5BA1C CC8D5743 4E46BE5D DAE5E19B BCEB09F1` 

- `B : 98C2A26E 203FE129 91D449C4 86D27C0E E43EE5D9 AA624C8B 18358F56 5498E90F 08061EC6 CB4E531A F07AB35C DEC22F95 F4A1DE73 1558F50E AABFEFB8 3BBA68EF` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation(j=2)
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:permutation-addCtoA
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `C : 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000 00000000` 

###### `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:subtractMfromC
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `C : FFFFFE00 FFFFFDFF FFFFFDFE FFFFFDFD FFFFFDFC FFFFFDFB FFFFFDFA FFFFFDF9 FFFFFDF8 FFFFFDF7 FFFFFDF6 FFFFFDF5 FFFFFDF4 FFFFFDF3 FFFFFDF2 FFFFFDF1` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=-1:swapBwithC
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

287 

- `B : FFFFFE00 FFFFFDFF FFFFFDFE FFFFFDFD FFFFFDFC FFFFFDFB FFFFFDFA FFFFFDF9 FFFFFDF8 FFFFFDF7 FFFFFDF6 FFFFFDF5 FFFFFDF4 FFFFFDF3 FFFFFDF2 FFFFFDF1` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : FFFFFFFF FFFFFFFF` 

```
blocknumber=0:incrementcounterW
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : FFFFFE00 FFFFFDFF FFFFFDFE FFFFFDFD FFFFFDFC FFFFFDFB FFFFFDFA FFFFFDF9 FFFFFDF8 FFFFFDF7 FFFFFDF6 FFFFFDF5 FFFFFDF4 FFFFFDF3 FFFFFDF2 FFFFFDF1` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:messageblock
```

- `M : 00000210 00000211 00000212 00000213 00000214 00000215 00000216 00000217 00000218 00000219 0000021A 0000021B 0000021C 0000021D 0000021E 0000021F` 

```
blocknumber=0:addMtoB
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:xorcounterWintoA
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010 00000010` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-rotateB
```

- `A : DCED6C97 B5937A56 BC2D3479 4B2672FE A762CE01 E0587D3E DAAA7818 F9BF94BD 646EB744 A0DA0A55 C70BC02E 292C7C6B` 

- `B : 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000 00200000` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F` 

288 

```
48910C72893B24F4C5A0E15EBBC4346972D2F45C75941FB66D8BE0A0A1A7524A
```

```
W:0000000000000000
```

```
blocknumber=0:permutation(j=0)
```

- `A : E3C2DE4A 15013A27 9779A969 2E533DBB F9542F32 1830E439 49354FD1 3FA73E25 62A98156 E3930697 3AEC9AE8 02836D8A` 

- `B : 15F96FCE BF883B5C 13B9B891 5F17F2CF 06EBD0CD E78F1BC6 B68AB02E C018C1DA 9D167EA9 1C2CF968 C5536517 FD3C9275 1C7D21B5 EABEC5D8 68C65696 D1ECC244` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=1)
```

- `A : F762247A 9C5C1A1B 82879280 482A0C43 F996F842 F06FAEB4 6FBAE548 DD572216 AC03820D 16A91946 E8198C7A C460216D` 

- `B : 3453DF4C 85E7DAA3 A8D88D92 0E0FE970 5E2BDC68 2648D134 7AF313D8 BBAE5D27 32B126D6 5BFA1734 F7DEA750 4DACD757 3E9344D7 DAEDDAFA 41C9B79B 81715960` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation(j=2)
```

- `A : F67C2EF7 2774D155 4B92F221 8CA66230 E59A65D4 199FE418 2C22673B DA3186CB 17D54265 E4FDEA67 595B4C44 81C61457` 

- `B : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:permutation-addCtoA
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : C1099EC7 07B38804 E7442E38 CC8AD853 EB6F58DB 1EA81CBE 73B9D52A 1DE85F1F 48910C72 893B24F4 C5A0E15E BBC43469 72D2F45C 75941FB6 6D8BE0A0 A1A7524A` 

- `W : 00000000 00000000` 

```
blocknumber=0:subtractMfromC
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780` 

289 

   - `7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `C : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `W : 00000000 00000000` 

```
blocknumber=0:swapBwithC
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000000 00000000` 

```
blocknumber=1:incrementcounterW
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : C1099CB7 07B385F3 E7442C26 CC8AD640 EB6F56C7 1EA81AA9 73B9D314 1DE85D08 48910A5A 893B22DB C5A0DF44 BBC4324E 72D2F240 75941D99 6D8BDE82 A1A7502B` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:messageblock
```

- `M : 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 302D7A79 34333231 38373635 42412D39 46454443 4A494847 4E4D4C4B 5251504F 56555453 5A595857` 

```
blocknumber=1:addMtoB
```

- `A : 20728DFD 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : 256CFF18 701AEC58 53AF968F 3CFA44AD 5FE2C938 971F911E A3E74D8D 521B8F39 80C8408F CB7C5014 0BE62387 060D7A95 C1203E8B C7E56DE8 C3E132D5 FC00A882` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:xorcounterWintoA
```

- `A : 20728DFC 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : 256CFF18 701AEC58 53AF968F 3CFA44AD 5FE2C938 971F911E A3E74D8D 521B8F39 80C8408F CB7C5014 0BE62387 060D7A95 C1203E8B C7E56DE8 C3E132D5 FC00A882` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

290 

###### `W : 00000001 00000000` 

```
blocknumber=1:permutation-rotateB
```

- `A : 20728DFC 46C0BD53 E782B699 55304632 71B4EF90 0EA9E82C DBB930F1 FAD06B8B BE0CAE40 8BD14410 76D2ADAC 28ACAB7F` 

- `B : FE304AD9 D8B0E035 2D1EA75F 895A79F4 9270BFC5 223D2E3F 9B1B47CE 1E72A437 811F0190 A02996F8 470E17CC F52A0C1A 7D178240 DBD18FCA 65AB87C2 5105F801` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=0)
```

- `A : 521A8160 F2C7A2D8 19943F75 98C8339B 765B34C2 4F6BDE89 F053F1FC E6C80AE5 2B7E001E 1CF7FF61 CBF8D1B7 0E09704D` 

- `B : 475728A8 B3A35E8E 92EC9E80 A5B803DA AD45B4B6 F4EE7D08 399A819E 25D2BD74 D6BFFCC0 A35B2D6F BA1B01D0 1BA29787 57CA7A1F BA9B42B2 2D3CCF0E C53C3C66` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=1)
```

- `A : 07350D5E 86098A1D D0B29046 34CE1DA3 37BD68F0 C7F82F4B A6EDC376 F2200D32 D0A7263D 5DF27B32 C4642766 D919D727` 

- `B : B4E0FE0E 4F042E9A C695D5BA 7E6A7EF7 75D3B0AF 4BD17EDC 48AEDBA5 6D435230 55B50B20 3F402F3D 5B7B6C18 FC74CD52 67D66331 4D3155D1 036BA295 87A78A00` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation(j=2)
```

- `A : ADA9B505 9CF7B61A 3ED16596 9B4A1C40 E9734A02 BC4E95ED EE66F036 DA2C1B9A 8352CCD2 E5870916 50B25176 1624D3E7` 

- `B : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:permutation-addCtoA
```

- `A : 6A51D961 C197BCF7 DA806A15 580FAFED EB88BE44 CAEA401D 2CD089D7 AE1AA91F C724BF45 AF6F7EA9 E53AB434 B948B147` 

- `B : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

291 

- `C : D9BF68D1 58BAD750 56028CB2 8134F359 B5D469D8 941A8CC2 418B2A6E 04052780 7F07D787 5194358F 3C60D665 BE97D79A 950C3434 AED9A06D 2537DC8D 7CDB5969` 

- `W : 00000001 00000000` 

```
blocknumber=1:subtractMfromC
```

- `A : 6A51D961 C197BCF7 DA806A15 580FAFED EB88BE44 CAEA401D 2CD089D7 AE1AA91F C724BF45 AF6F7EA9 E53AB434 B948B147` 

- `B : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `C : 755C0670 F05370EB E9972249 10C584EC 4160F767 1BA3164D 115DAFF5 CFD1F54F 46D0A152 0F530856 F61B9222 744E8F53 46BEE7E9 5C88501E CEE2883A 22820112` 

- `W : 00000001 00000000` 

```
blocknumber=1:swapBwithC
```

- `A : 6A51D961 C197BCF7 DA806A15 580FAFED EB88BE44 CAEA401D 2CD089D7 AE1AA91F C724BF45 AF6F7EA9 E53AB434 B948B147` 

- `B : 755C0670 F05370EB E9972249 10C584EC 4160F767 1BA3164D 115DAFF5 CFD1F54F 46D0A152 0F530856 F61B9222 744E8F53 46BEE7E9 5C88501E CEE2883A 22820112` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `W : 00000001 00000000` 

```
blocknumber=2:incrementcounterW
```

- `A : 6A51D961 C197BCF7 DA806A15 580FAFED EB88BE44 CAEA401D 2CD089D7 AE1AA91F C724BF45 AF6F7EA9 E53AB434 B948B147` 

- `B : 755C0670 F05370EB E9972249 10C584EC 4160F767 1BA3164D 115DAFF5 CFD1F54F 46D0A152 0F530856 F61B9222 744E8F53 46BEE7E9 5C88501E CEE2883A 22820112` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `W : 00000002 00000000` 

```
blocknumber=2:messageblock
```

- `M : 3231302D 36353433 2D393837 64636261 68676665 6C6B6A69 706F6E6D 74737271 78777675 00807A79 00000000 00000000 00000000 00000000 00000000 00000000` 

```
blocknumber=2:addMtoB
```

- `A : 6A51D961 C197BCF7 DA806A15 580FAFED EB88BE44 CAEA401D 2CD089D7 AE1AA91F C724BF45 AF6F7EA9 E53AB434 B948B147` 

- `B : A78D369D 2688A51E 16D05A80 7528E74D A9C85DCC 880E80B6 81CD1E62 444567C0 BF4817C7 0FD382CF F61B9222 744E8F53 46BEE7E9 5C88501E CEE2883A 22820112` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `W : 00000002 00000000` 

292 

```
blocknumber=2:xorcounterWintoA
```

- `A : 6A51D963 C197BCF7 DA806A15 580FAFED EB88BE44 CAEA401D 2CD089D7 AE1AA91F C724BF45 AF6F7EA9 E53AB434 B948B147` 

- `B : A78D369D 2688A51E 16D05A80 7528E74D A9C85DCC 880E80B6 81CD1E62 444567C0 BF4817C7 0FD382CF F61B9222 744E8F53 46BEE7E9 5C88501E CEE2883A 22820112` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

###### `W : 00000002 00000000` 

```
blocknumber=2:permutation-rotateB
```

- `A : 6A51D963 C197BCF7 DA806A15 580FAFED EB88BE44 CAEA401D 2CD089D7 AE1AA91F C724BF45 AF6F7EA9 E53AB434 B948B147` 

- `B : 6D3B4F1A 4A3C4D11 B5002DA0 CE9AEA51 BB995390 016D101D 3CC5039A CF80888A 2F8F7E90 059E1FA7 2445EC37 1EA6E89D CFD28D7D A03CB910 10759DC5 02244504` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=0)
```

- `A : 9C514AC4 3BADF179 BB75BFFD 5FB5FD4B E666B91F 318CA9B9 6D877BB1 05F34168 FAE6F46D 5BD6CB26 479B8912 F3D10A95` 

- `B : F312556D 199302E5 3039578C E5E90D95 6EABE1C1 CCA9767C EBF2837A 650DAF82 5A07F6B2 AF150B97 F0EFAE83 31632450 FC0BAFC0 842B7CA7 64617B88 A40288BC` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=1)
```

- `A : 854479F2 8F09B4AA CD8F4966 7337EA94 6ED28CCD F29CF0D4 82AFF90C 1F3B6E07 5740488B 4D92D5CC 7F5CEE46 3FA274C3` 

- `B : 43F1708B 7AF318A2 157BD5DD 77565888 75E874F6 2B3FC6CA 5746174C 0A46D438 CEB46B69 2EDC5C7A D3AFEB9E EE0E5DCB 693A2CB3 0535F664 B592F1E3 A8C18081` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `W : 00000002 00000000` 

```
blocknumber=2:permutation(j=2)
```

- `A : 4C5EE590 B0B92F77 4905E370 1B09A00A 61A1A07E 176DFB83 9BA40FFE 69DFDBD3 806B3232 D77D6038 0D08CEEC 290A0663` 

- `B : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

293 

###### `W : 00000002 00000000` 

```
blocknumber=2:permutation-addCtoA
```

- `A : DB37C6BF 43DF675E 9CF7D94F 41A9B99A D1734ACC B578E1D8 ACACDCFA 8E54E1B9 E6E32327 025724E8 BEFF14FC CA87F722` 

- `B : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `C : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `W : 00000002 00000000` 

```
blocknumber=2:subtractMfromC
```

- `A : DB37C6BF 43DF675E 9CF7D94F 41A9B99A D1734ACC B578E1D8 ACACDCFA 8E54E1B9 E6E32327 025724E8 BEFF14FC CA87F722` 

- `B : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `C : F401E6C7 A8F7B004 FF58C893 66A6C7F5 5189C53F 883F49F4 E003BEB6 49BFD56E 456F2D48 3CB0B9EF A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `W : 00000002 00000000` 

```
blocknumber=2:swapBwithC
```

- `A : DB37C6BF 43DF675E 9CF7D94F 41A9B99A D1734ACC B578E1D8 ACACDCFA 8E54E1B9 E6E32327 025724E8 BEFF14FC CA87F722` 

- `B : F401E6C7 A8F7B004 FF58C893 66A6C7F5 5189C53F 883F49F4 E003BEB6 49BFD56E 456F2D48 3CB0B9EF A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `C : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : add M to B` 

- `A : DB37C6BF 43DF675E 9CF7D94F 41A9B99A D1734ACC B578E1D8 ACACDCFA 8E54E1B9 E6E32327 025724E8 BEFF14FC CA87F722` 

- `B : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

- `C : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : xor counter W into A` 

- `A : DB37C6BD 43DF675E 9CF7D94F 41A9B99A D1734ACC B578E1D8 ACACDCFA 8E54E1B9 E6E32327 025724E8 BEFF14FC CA87F722` 

- `B : 263316F4 DF2CE437 2C9200CA CB0A2A56 B9F12BA4 F4AAB45D 50732D23 BE3347DF BDE6A3BD 3D313468 A76FD7F9 DD3A7EC0 B301F54F 801A5D4B A99AEBA3 E6943819` 

294 

- `C : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

```
W:0000000200000000
```

- `n0_final = 0 : permutation - rotate B` 

- `A : DB37C6BD 43DF675E 9CF7D94F 41A9B99A D1734ACC B578E1D8 ACACDCFA 8E54E1B9 E6E32327 025724E8 BEFF14FC CA87F722` 

- `B : 2DE84C66 C86FBE59 01945924 54AD9614 574973E2 68BBE955 5A46A0E6 8FBF7C66 477B7BCD 68D07A62 AFF34EDF FD81BA74 EA9F6603 BA970034 D7475335 7033CD28` 

- `C : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 0)` 

- `A : 007E853B BCF7132E 2EC6EDCC 6A95766A CCBF887C 97B7F87A 64D079C4 87051CBF 63B380CE FF88C2D0 01B3E368 6987989E` 

- `B : 999E2DCA 3470467A 25CF15A8 A7C8F6D3 9DD29047 B93FD52F 2FA2C7F7 67841B8D 12BA88AB D1D7C9EB A1AA8128 6D7B1388 2ABFB6C3 3626ECB8 7FB7B458 750D13C5` 

- `C : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 1)` 

- `A : 56AD8642 4F53444B 300FBED9 C2D9B8B8 17B6A359 BDFE6C80 C448E63E ABA7A6C3 6A8DE8A1 80AF4351 B1F5774E D8E1B1C7` 

- `B : 2E0852E3 F0095852 B3F9B371 08E8EEC7 AED737D1 0D2F16F1 114F075F E8167922 8C2768EB 13032863 8CA54377 E7D06057 BD363120 2E4C4A0F C4D87171 BE427EB6` 

- `C : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation (j = 2)` 

- `A : 463B12A4 9EEF72EE 84CA8F14 65710BEA B1AF37FE CC7E7CA8 ED166423 8B798937 7BA4A533 237B5AC1 724F6BEE D51A399B` 

- `B : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `C : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : permutation - add C to A` 

- `A : 1677073B AFE6FB03 5BF4E5AF B83D9650 282A845F 32CBF964 56820437 07776805 B4E598B0 2D046C41 639CF8A1 4A6765C2` 

295 

- `B : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `C : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : subtract M from C` 

- `A : 1677073B AFE6FB03 5BF4E5AF B83D9650 282A845F 32CBF964 56820437 07776805 B4E598B0 2D046C41 639CF8A1 4A6765C2` 

- `B : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `C : D873CFBA 64D2523D 734A4D44 9A24F9DC F00A8D1E ACCDF2B3 A806C3AA 7C088514 8ABF12DD B4AA420F C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `W : 00000002 00000000` 

- `n0_final = 0 : swap B with C` 

- `A : 1677073B AFE6FB03 5BF4E5AF B83D9650 282A845F 32CBF964 56820437 07776805 B4E598B0 2D046C41 639CF8A1 4A6765C2` 

- `B : D873CFBA 64D2523D 734A4D44 9A24F9DC F00A8D1E ACCDF2B3 A806C3AA 7C088514 8ABF12DD B4AA420F C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `C : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

- `n0_final = 1 : add M to B` 

- `A : 1677073B AFE6FB03 5BF4E5AF B83D9650 282A845F 32CBF964 56820437 07776805 B4E598B0 2D046C41 639CF8A1 4A6765C2` 

- `B : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `C : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

```
n0_final=1:xorcounterWintoA
```

- `A : 16770739 AFE6FB03 5BF4E5AF B83D9650 282A845F 32CBF964 56820437 07776805 B4E598B0 2D046C41 639CF8A1 4A6765C2` 

- `B : 0AA4FFE7 9B078670 A083857B FE885C3D 5871F383 19395D1C 18763217 F07BF785 03368952 B52ABC88 C304273C 4A3C9FBB ADE094AB 22E9730F 99D2D2D4 8776F89F` 

- `C : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - rotate B` 

296 

- `A : 16770739 AFE6FB03 5BF4E5AF B83D9650 282A845F 32CBF964 56820437 07776805 B4E598B0 2D046C41 639CF8A1 4A6765C2` 

- `B : FFCE1549 0CE1360F 0AF74107 B87BFD10 E706B0E3 BA383272 642E30EC EF0BE0F7 12A4066D 79116A55 4E798608 3F769479 29575BC1 E61E45D2 A5A933A5 F13F0EED` 

- `C : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 0)` 

- `A : 584547D8 E4ABC4A4 1B18E9F8 DBF7B600 C3F3A594 8810C99E 9D3395A0 1212F94B 489A7A9F 711209B5 447379E5 B27EE663` 

- `B : 77781FB2 AEEBEFC9 87F452FC 382285C6 F2013BAC 039F5284 AA900B87 33FAC75B 922D89BA 7CCF22E0 277F8A0A 336C316E F5140FA5 D768B0FE AFB5714C C6765424` 

- `C : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 1)` 

- `A : 8D8AFAD0 08370C73 EC83D0D7 A7D3D97D F752013A BA0F211B 940FB1EF D7DEDC36 9D82DEEF D0DD8110 DE2A4F3F F49CC319` 

- `B : D8D7ACC7 5B52C8E5 BF580A9D D0966821 867F5649 281CDBE7 74F5A7CF 6C96B250 562E165A 0E56B64C 5D833B3C 3EF4445E E285E18E EB21BF19 349AAC89 A4CD8B80` 

- `C : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation (j = 2)` 

- `A : D5BE9831 F3143340 7EE33692 DC9B0CA8 455306CC 05D59A83 4DED5952 2BE65A56 815F2F95 3DFF9C03 4F46B77F F84EB239` 

- `B : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `C : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

- `n0_final = 1 : permutation - add C to A` 

- `A : C0B614DD 3C1ADDC4 EB1A0C0F E9903001 BFC5D361 A6C32650 4F8FD140 407E23F0 60977788 76BF715E 60395D23 619DC4B3` 

- `B : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `C : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

297 

```
n0_final=1:subtractMfromC
```

- `A : C0B614DD 3C1ADDC4 EB1A0C0F E9903001 BFC5D361 A6C32650 4F8FD140 407E23F0 60977788 76BF715E 60395D23 619DC4B3` 

- `B : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `C : 3433BED2 3A96CF37 820FF5DB 750C28DB 7C031C93 0EE3368A E93C0FE8 D62E93DF DDA6A361 15075918 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `W : 00000002 00000000` 

- `n0_final = 1 : swap B with C` 

- `A : C0B614DD 3C1ADDC4 EB1A0C0F E9903001 BFC5D361 A6C32650 4F8FD140 407E23F0 60977788 76BF715E 60395D23 619DC4B3` 

- `B : 3433BED2 3A96CF37 820FF5DB 750C28DB 7C031C93 0EE3368A E93C0FE8 D62E93DF DDA6A361 15075918 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `C : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : add M to B` 

- `A : C0B614DD 3C1ADDC4 EB1A0C0F E9903001 BFC5D361 A6C32650 4F8FD140 407E23F0 60977788 76BF715E 60395D23 619DC4B3` 

- `B : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `C : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `W : 00000002 00000000` 

```
n0_final=2:xorcounterWintoA
```

- `A : C0B614DF 3C1ADDC4 EB1A0C0F E9903001 BFC5D361 A6C32650 4F8FD140 407E23F0 60977788 76BF715E 60395D23 619DC4B3` 

- `B : 6664EEFF 70CC036A AF492E12 D96F8B3C E46A82F8 7B4EA0F3 59AB7E55 4AA20650 561E19D6 1587D391 0BA31D33 BB26B667 FE37388D 801C3120 040076F2 56613B09` 

- `C : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - rotate B` 

- `A : C0B614DF 3C1ADDC4 EB1A0C0F E9903001 BFC5D361 A6C32650 4F8FD140 407E23F0 60977788 76BF715E 60395D23 619DC4B3` 

- `B : DDFECCC9 06D4E198 5C255E92 1679B2DF 05F1C8D5 41E6F69D FCAAB356 0CA09544 33ACAC3C A7222B0F 3A661746 6CCF764D 711BFC6E 62410038 EDE40800 7612ACC2` 

- `C : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7` 

298 

```
16F0D587E68709E40914D0D5A9F12D15BBAB137714431DCFD98C11924E2A5AC7
```

```
W:0000000200000000
```

- `n0_final = 2 : permutation (j = 0)` 

- `A : 25BB41ED 030944B0 7931C842 0EE6CB55 3C62EA04 E3473D7E EFF28F08 CEAD8919 33F792D7 6F755271 1F07D243 4A4C0B99` 

- `B : 2FE67E6A F508D465 02104DAA F31C6214 C87E8451 9F752FBB E958165A 28135C6E AB513550 DECEFB91 94340330 6C2D18FC 387346CE 3874BB3F 5D0627BC 1D3C6D2E` 

- `C : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 1)` 

- `A : F68087D5 875B00CB 60A8CE06 512155E1 E2935957 1B3E03D6 3C0BA829 2353F2E5 3888C584 8EE110C8 56764BCD 2BE6E607` 

- `B : 38A3B18C 1DFC4008 B8CF609C AFD76D35 578A32D8 4FF4B040 7B399887 843FA124 5FDD128B C5390817 B73F3798 76849BE6 6D8A2B34 94288A57 79F818AE E6D4D746` 

- `C : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation (j = 2)` 

- `A : 36D5FFBC E625E21B 4A8D142E 5248F193 D464E432 04E263D6 F1FAED97 A6D485AB FD8BB6ED 1C71434C B56A93B4 FD980801` 

- `B : 7F6F7E67 F00AD712 2F6635B3 5168B559 663E65F3 86337D64 4301DADF A5C84C25 94213EDB 716F8C06 607B7D59 B4224D98 D9601F7A CBDFA81C B9655D17 CFCE5973` 

- `C : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : permutation - add C to A` 

- `A : 706F3E32 22946DE1 15E78C72 2CE64CAC 5E568D8A 9C96B1AC 8F9951F0 B0FAA007 E3443293 15CCF7A7 0D0736D8 4930715B` 

- `B : 7F6F7E67 F00AD712 2F6635B3 5168B559 663E65F3 86337D64 4301DADF A5C84C25 94213EDB 716F8C06 607B7D59 B4224D98 D9601F7A CBDFA81C B9655D17 CFCE5973` 

- `C : 5A03ACF2 5A44DF04 9819C294 417DB69A 26BFCB5D 5CD27B71 68F786F3 FA4997F7 16F0D587 E68709E4 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : subtract M from C` 

- `A : 706F3E32 22946DE1 15E78C72 2CE64CAC 5E568D8A 9C96B1AC 8F9951F0 B0FAA007 E3443293 15CCF7A7 0D0736D8 4930715B` 

- `B : 7F6F7E67 F00AD712 2F6635B3 5168B559 663E65F3 86337D64 4301DADF A5C84C25` 

299 

```
94213EDB716F8C06607B7D59B4224D98D9601F7ACBDFA81CB9655D17CFCE5973
```

- `C : 27D27CC5 240FAAD1 6AE08A5D DD1A5439 BE5864F8 F0671108 F8881886 85D62586 9E795F12 E6068F6B 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `W : 00000002 00000000` 

- `n0_final = 2 : swap B with C (final state)` 

- `A : 706F3E32 22946DE1 15E78C72 2CE64CAC 5E568D8A 9C96B1AC 8F9951F0 B0FAA007 E3443293 15CCF7A7 0D0736D8 4930715B` 

- `B : 27D27CC5 240FAAD1 6AE08A5D DD1A5439 BE5864F8 F0671108 F8881886 85D62586 9E795F12 E6068F6B 0914D0D5 A9F12D15 BBAB1377 14431DCF D98C1192 4E2A5AC7` 

- `C : 7F6F7E67 F00AD712 2F6635B3 5168B559 663E65F3 86337D64 4301DADF A5C84C25 94213EDB 716F8C06 607B7D59 B4224D98 D9601F7A CBDFA81C B9655D17 CFCE5973` 

- `W : 00000002 00000000` 

```
Hashvalue:
```

- `H : 7F6F7E67 F00AD712 2F6635B3 5168B559 663E65F3 86337D64 4301DADF A5C84C25 94213EDB 716F8C06 607B7D59 B4224D98 D9601F7A CBDFA81C B9655D17 CFCE5973` 

```
Hashvalue(bytearray):
```

- `H : 67 7E 6F 7F 12 D7 0A F0 B3 35 66 2F 59 B5 68 51 F3 65 3E 66 64 7D 33 86 DF DA 01 43 25 4C C8 A5 DB 3E 21 94 06 8C 6F 71 59 7D 7B 60 98 4D 22 B4 7A 1F 60 D9 1C A8 DF CB 17 5D 65 B9 73 59 CE CF` 

300