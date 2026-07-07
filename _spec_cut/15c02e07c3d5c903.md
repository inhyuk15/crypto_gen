# **Saber: Module-LWR based key exchange, CPA-secure encryption and CCA-secure KEM** 

Jan-Pieter D’Anvers, Angshuman Karmakar Sujoy Sinha Roy, and Frederik Vercauteren 

imec-COSIC, KU Leuven 

Kasteelpark Arenberg 10, Bus 2452, B-3001 Leuven-Heverlee, Belgium `firstname.lastname@esat.kuleuven.be` 

**Abstract** In this paper, we introduce Saber, a package of cryptographic primitives whose security relies on the hardness of the Module Learning With Rounding problem (Mod-LWR). We first describe a secure DiffieHellman type key exchange protocol, which is then transformed into an IND-CPA encryption scheme and finally into an IND-CCA secure key encapsulation mechanism using a post-quantum version of the FujisakiOkamoto transform. The design goals of this package were simplicity, efficiency and flexibility resulting in the following choices: all integer moduli are powers of 2 avoiding modular reduction and rejection sampling entirely; the use of LWR halves the amount of randomness required compared to LWE-based schemes and reduces bandwidth; the module structure provides flexibility by reusing one core component for multiple security levels. A constant-time AVX2 optimized software implementation of the KEM with parameters providing more than 128 bits of post-quantum security, requires only 101K, 125K and 129K cycles for key generation, encapsulation and decapsulation respectively on a Dell laptop with an Intel i7-Haswell processor. 

## **2 Preliminaries** 

### **2.1 Notation** 

We denote with Z _q_ the ring of integers modulo an integer _q_ with representants in [0 _, q_ ) and for an integer _z_ , we denote _z_ mod _q_ the reduction of _z_ in [0 _, q_ ). _Rq_ is the quotient ring Z _q_ [ _X_ ] _/_ ( _X_<sup>_n_</sup> + 1) with _n_ a fixed power of 2 (we only need _n_ = 256). For any ring _R_ , _R_<sup>_l×k_</sup> denotes the ring of _l × k_ -matrices over _R_ . For _p | q_ , the mod _p_ operator is extended to (matrices over) _Rq_ by applying it coefficient-wise. Single polynomials are written without markup, vectors are bold lower case and matrices are denoted with bold upper case. _U_ denotes the uniform distribution and _βµ_ is a centered binomial distribution with parameter _µ_ and corresponding standard deviation _σ_ = � _µ/_ 2. If _χ_ is a probability distribution over a set _S_ , then _x ← χ_ denotes sampling _x ∈ S_ according to _χ_ . If _χ_ is defined on Z _q_ , **_X_** _← χ_ ( _Rq_<sup>_l×k_</sup> ) denotes sampling the matrix **_X_** _∈ Rq_<sup>_l×k_</sup> , where all coefficients of the entries in **_X_** are sampled from _χ_ . 

We use the part selection function `bits` ( _x, i, j_ ) with _j ≤ i_ to access _j_ consecutive bits of a positive integer _x ending_ at the _i_ -th index (assuming least significant bit in the 0-th index), producing an integer in Z2 _j_ ; i.e., written in standard C code the function returns ( _x ≫_ ( _i − j_ ))&(2<sup>_j_</sup> _−_ 1), where _≫_ is the right-shift operator. This is explained in Fig. 1.The part selection function is extended to polynomials and matrices by applying it coefficient-wise. Finally let _⌊⌉_ denote rounding to the nearest integer, which can be extended to polynomials and matrices 

Figure 1: The `bits` ( _x, i, j_ ) operator. 

### **2.2 Cryptographic definitions** 

Let KE be a Diffie-Hellman type key exchange protocol between two parties as illustrated in Protocol 1. KE is called (1 _− δ_ )-correct if after execution of the protocol _Pr_ [ _k_<sup>_′_</sup> = _k_ ] ⩾ 1 _− δ_ , where the probability is computed over the random coins used in Protocol 1. KE is called IND-RND secure if it is hard for an adversary to distinguish the real shared secret from random. More formally, we define the advantage of an adversary in distinguishing the key _k_ from a uniformly random key _k_<sup>ˆ</sup> _←U_ ( _K_ ) as follows: 

A public key encryption scheme consists of a triple of functions PKE = ( `KeyGen` _,_ `Enc` _,_ `Dec` ), where `KeyGen` returns a secret key _sk_ and a public key _pk_ ; 

3 

|**Public parameters**<br>**P**|
|---|
|Alice<br>Bob|
|Choose secret _a_|
|Compute **A** as function of **P** and _a_<br>**A**<br>- <sup>Choose secret</sup> <sup>_b_</sup>|
|Compute **B** as function of **P** and _b_<br><br>**B**<br>_k_ = Derive key from **P**_, a,_**B**<br>_k_<sup>_′_ </sup>= Derive key from **P**_, b,_**A**|

Protocol 1: Diffie-Hellman type key exchange protocol 

`Enc` takes a public key _pk_ and a message _m ∈M_ to produce a ciphertext _c ∈C_ , and `Dec` takes the secret key _sk_ together with ciphertext _c_ to output a message _m_<sup>_′_</sup> _∈M_ or the symbol _⊥_ to denote rejection. The PKE is said to be (1 _− δ_ )- correct if _Pr_ [ `Dec` ( _sk,_ `Enc` ( _pk, m_ )) = _m_ ] ⩾ 1 _− δ_ , where the probability is taken over ( _pk, sk_ ) _←_ `KeyGen` and the random coins of `Enc` . We use the notion of indistinguishability under chosen plaintext attacks (IND-CPA) and define the advantage of an adversary A by: 

The weaker notion of one-wayness under chosen plaintext attacks (OW-CPA) is as: 

A key-encapsulation mechanism KEM = ( `KeyGen` _,_ `Encaps` _,_ `Decaps` ) is a triple of probabilistic algorithms, where `KeyGen` returns a secret key _sk_ and a public key _pk_ , where `Encaps` takes a public key _pk_ and produces a ciphertext _c_ and a key _k ∈K_ , and where `Decaps` takes the secret key _sk_ , the public key _pk_ and ciphertext _c_ to return a key _k ∈K_ or the symbol _⊥_ to denote rejection. The KEM is said to be (1 _−δ_ )-correct if _Pr_ [ `Decaps` ( _sk, c_ ) = _k_ : ( _c, k_ ) _←_ `Encaps` ( _pk_ )] ⩾ 1 _−δ_ , where the probability is taken over ( _pk, sk_ ) _←_ `KeyGen` and the random coins of `Encaps` . We use the notion of indistinguishability under chosen ciphertext attacks (IND-CCA) to define the advantage of an adversary _A_ by: 

The advantage of an adversary A in distinguishing a pseudorandom generator `gen` () with seed _seed_ **_A_** _←U_ ( _{_ 0 _,_ 1 _}_<sup>256</sup> ) from a uniformly random distribution is 

4 

as follows: 

### **2.3 LWE, LWR and Mod-LWR problems** 

The learning with errors (LWE) problem was introduced by Regev [41] and its decisional version states that it is hard to distinguish uniform random samples ( **_a_** _, u_ ) _←U_ (Z<sup>_l_</sup> _q_<sup>_×_1</sup> _×_ Z _q_ ) from LWE-samples of the form 

where the secret vector **_s_** _← βµ_ (Z<sup>_l_</sup> _q_<sup>_×_1</sup> ) is fixed for all samples, **_a_** _←U_ (Z<sup>_l_</sup> _q_<sup>_×_1</sup> ) and _e ← βµ_ (Z _q_ ) is a small error. A module version of LWE, called Mod-LWE, was analyzed by Langlois and Stehl´e [36] and essentially replaces the ring Z _q_ in the above samples by a quotient ring of the form _Rq_ with corresponding error distribution _βµ_ ( _Rq_<sup>_l×_1</sup> ). The rank of the module is _l_ and the dimension of the ring _Rq_ is _n_ . The case _l_ = 1 corresponds to the ring-LWE problem introduced in [37]. 

The LWR problem was introduced by Banerjee et al. [10] and is a derandomized version of the LWE problem. In contrast to the LWE problem, the “noise” in the LWR problem is generated deterministically by scaling and rounding coefficients modulo _q_ to modulo _p_ (with _p < q_ ). In detail, an LWR sample is given by 

for a fixed **_s_** _← βµ_ (Z<sup>_l_</sup> _q_<sup>_×_1</sup> ) and uniform random **_a_** _←U_ (Z<sup>_l_</sup> _q_<sup>_×_1</sup> ). The decisional LWR problem states that is it hard to distinguish samples from the LWR distribution from that of the uniform distribution. A reduction from the LWE problem to the LWR problem was given by Banerjee et al. [10], and further improved by Alwen et al. [6], Bogdanov et al. [15] and, Alperin-Sheriff and Daniel Apon [5]. 

The security of our protocol relies on the hardness of the module version of LWR (Mod-LWR), which is a straightforward generalization of Mod-LWE. A Mod-LWR sample is given by 

where the secret **_s_** _← βµ_ ( _Rq_<sup>_l×_1</sup> ) is fixed for all samples and **_a_** _←U_ ( _Rq_<sup>_l×_1</sup> ). The advantage of an adversary _A_ in distinguishing _m_ samples from a ModLWR distribution from that of a uniform distribution is defined as follows, where 

5 

_m_ , _k_ , _µ_ , _q_ and _p_ are positive integers with _q > p_ : 

## **3 Key Exchange** 

In Protocol 2 we describe a Diffie-Hellman type key exchange scheme Saber.KE based on the hardness of Mod-LWR problem. Unlike the Diffie-Hellman key exchange [23], in our scheme the two communicating parties sometimes fail to agree on the same key. As in previous works [24,40,12], we can make this failure probability negligibly small by sending some additional reconciliation data _c_ . 

||Alice|Bob|
|---|---|---|
|**1**|_seed_**_A_** _←U_(_{_0_,_1_}_<sup>256</sup>)||
|**2**|**_A_** _←_`gen`(seed**_A_**)_∈R_<sup>_l×l_</sup><br>_q_||
|**3**|**_s_** _←βµ_(_R_<sup>_l×_1</sup><br>_q_<br>)|**_s_**<sup>_′ _</sup>_←βµ_(_R_<sup>_l×_1</sup><br>_q_<br>)|
|**4**|**_b_** =`bits`(**_As_**+ **_h_**_, ϵq, ϵp_)_∈R_<sup>_l×_1</sup><br>_p_|**_b_**_,_seed**_A_**<br>- <sup>**_A_**</sup> <sup>_←_</sup><sup>`gen`(seed</sup><sup>**_A_**)</sup><sup>_∈Rl×l_</sup><br>_q_|
|**5**||**_b_**<sup>_′_ </sup>=`bits`(**_A_**<sup>_T_</sup>**_s_**<sup>_′_ </sup>+ **_h_**_, ϵq, ϵp_)_∈R_<sup>_l×_1</sup><br>_p_|
|**6**||_v_<sup>_′_ </sup>= **_b_**<sup>_T_</sup> `bits`(**_s_**<sup>_′_</sup>_, ϵp, ϵp_) +_h_1 _∈Rp_|
|**7**|_v_ = **_b_**<sup>_′T_</sup> `bits`(**_s_**_, ϵp, ϵp_) +_h_1 _∈Rp_|<br>**_b_**<sup>_′_</sup>_, c_<br>_c_=`bits`(_v_<sup>_′_</sup>_, ϵp −_1_, ϵt_)_∈Rt_|
|**8**|_k_ =`bits`(_v −_2<sup>_ϵp−ϵt−_1</sup>_c_+_h_2_, ϵp,_1)|_k_<sup>_′_ </sup>=`bits`(_v_<sup>_′_</sup>_, ϵp,_1)|
|**9**|_key_Alice =`kdf`(_k_)|_key_Bob =`kdf`(_k_<sup>_′_</sup>)|

Protocol 2: Saber.KE key exchange 

All moduli involved in the scheme are chosen to be powers of 2, in particular we choose _q_ = 2<sup>_ϵq_</sup> , _p_ = 2<sup>_ϵp_</sup> and _t_ = 2<sup>_ϵt_</sup> with _ϵq > ϵp >_ ( _ϵt_ +1), so we have 2 _t | p | q_ . In practice, our main parameter set will correspond to the case _ϵq_ = 13, _ϵp_ = 10 and _ϵt_ = 3. The secret vectors **_s_** and **_s_**<sup>_′_</sup> are sampled from _βµ_ ( _Rq_<sup>_l×_1</sup> ), with _µ < p_ , while the matrix **_A_** _∈ Rq_<sup>_l×l_</sup> is sampled using a pseudorandom generator `gen` () initialized with seed _A_ . The session key is obtained by feeding the common secret _k_ = _k_<sup>_′_</sup> _∈ R_ 2 into a key derivation function `kdf` (). The algorithm also uses three constants: a constant vector **_h_** _∈ Rq_<sup>_l×_1</sup> consisting of polynomials all coefficients of which are set to the constant 2<sup>_ϵq−ϵp−_1</sup> , a constant polynomial _h_ 1 _∈ Rq_ with all coefficients equal to 2<sup>_ϵq−ϵp−_1</sup> , and a constant polynomial _h_ 2 _∈ Rq_ with all coefficients set equal to (2<sup>_ϵp−_2</sup> _−_ 2<sup>_ϵp−ϵt−_2</sup> ). These constants are used to mimic rounding operations, which are necessary to reduce failure probability, while retaining the reduction to the underlying decisional Mod-LWR problem. 

6 

Note that the operations `bits` ( **_s_** _, ϵp, ϵp_ ) in line **6** and `bits` ( **_s_**<sup>_′_</sup> _, ϵp, ϵp_ ) in line **7** simply mean we are considering **_s_** mod _p_ and **_s_**<sup>**_′_**</sup> mod _p_ as elements in _Rp_ which is well defined since _p | q_ . 

**Correctness:** Using Saber.KE two communicating parties agree on a common random key with overwhelming probability. A tight bound on the failure probability can be obtained using following observations from Bos et al. [17]: the reconciliation between two integer values _vi, vi_<sup>_′∈_Z</sup><sup>_p_iscorrectifthedistance</sup> between _vi_ and _vi_<sup>_′_issmallerthan</sup><sup>_p/_4(1</sup><sup>_−_1</sup><sup>_/t_),andfailsifthedistanceisbigger</sup> than _p/_ 4(1 + 1 _/t_ ). In between these values, the probability of success decreases linearly from 1 to 0. Consequently, a tight bound on the failure probability given the distribution of _∆vi_ = _vi_<sup>_′−vi_canbecalculatedbyaddingto</sup><sup>_∆vi_adiscrete</sup> uniformly distributed error _er ∈_ Z _p_ with range [ _−p/_ 4 _t, p/_ 4 _t_ ]. The success probability of the reconciliation between _vi_ and _vi_<sup>_′_thenequals</sup><sup>_Pr_[</sup><sup>_|∆vi_+</sup><sup>_er| < p/_4].</sup> Using the above observation we can estimate a bound on the error probability: 

**Theorem 1.** _Let_ **_A_** _be a matrix in Rq_<sup>_l×l_</sup> _and_ **_s_** _,_ **_s_**<sup>_′_</sup> _two vectors in Rq_<sup>_l×_1</sup> _sampled as in Protocol 2. Define_ **_e_** _and_ **_e_**<sup>_′_</sup> _as the rounding errors introduced by scaling and rounding_ **_As_** _and_ **_A_**<sup>_T_</sup> **_s_**<sup>_′_</sup> _, i.e._ `bits` ( **_As_** + **_h_** _, ϵq, ϵp_ ) =<sup>_<u>p</u>_</sup> _q_<sup>**_As_**+</sup><sup>**_e_**</sup><sup>_and_</sup><sup>`bits`(</sup><sup>**_A_**</sup><sup>_T_</sup><sup>**_s_**</sup><sup>_′_+</sup> **_h_** _, ϵq, ϵp_ ) =<sup>_<u>p</u>_</sup> _q_<sup>**_A_**</sup><sup>_T_</sup><sup>**_s_**</sup><sup>_′_+</sup><sup>**_e′_**</sup><sup>_.Leter∈Rqbeapolynomialwithuniformlydistributed_</sup> _coefficients with range_ [ _−p/_ 4 _t, p/_ 4 _t_ ] _. If we set_ 

_then after executing the Saber.KE protocol, both communicating parties agree on a n-bit key with probability_ 1 _− δ._ 

_Proof._ The polynomials _v_<sup>_′_</sup> and _v_ calculated by Bob and Alice respectively in Protocol 2 are given as: _v_<sup>_′_</sup> = (<sup>_<u>p</u>_</sup> _q_<sup>**_s_**</sup><sup>_′T_</sup><sup>**_As_**+</sup><sup>_h_1+</sup><sup>**_s_**</sup><sup>_′T_</sup><sup>**_e_**mod</sup><sup>_p_) and</sup><sup>_v_= (</sup><sup>_<u>p</u>_</sup> _q_<sup>**_s_**</sup><sup>_′T_</sup><sup>**_As_**+</sup><sup>_h_1+</sup> **_e_**<sup>_′T_</sup> **_s_** mod _p_ ). Here, the coefficients of **_e_** _,_ **_e_**<sup>_′_</sup> are the rounding errors and so are in ( _−_ 1 _/_ 2 _,_ 1 _/_ 2]. It can be easily seen that the values calculated by the communicating parties differ by _∆v_ = _||_ ( **_s_**<sup>_′T_</sup> **_e_** _−_ **_e_**<sup>_′T_</sup> **_s_** ) mod _p||_ . Therefore, Bob and Alice agree on the same secret if _||∆v_ + _er||∞ ≤_<sup>_<u>p</u>_</sup> 4<sup>.Hence,for</sup><sup>_δ_=</sup><sup>_Pr_[</sup><sup>_||_(</sup><sup>**_s_**</sup><sup>_′T_</sup><sup>**_e_**</sup><sup>_−_</sup><sup>**_e_**</sup><sup>_′T_</sup><sup>**_s_**+</sup><sup>_er_)</sup> mod _p||∞ > p/_ 4] the Saber.KE protocol is (1 _− δ_ ) correct. 

Similar to Bos et al. [16], a tight upper bound on the value of _δ_ is calculated using a Python script. To be able to practically compute the distribution of _∆v_ = _v_<sup>_′_</sup> _− v ∈ Rp_ , Bos et al. assume independence between the terms **_s_**<sup>_′T_</sup> **_e_** and **_e_**<sup>_′T_</sup> **_s_** , which is not necessarily the case. Analogous to Theorem 5.2 from Jin and Zhao [33], one could argue that they are independent if conditioned on **_s_**<sup>_′T_</sup> **_As_** _≡ a_ mod _q/p_ , where _a ∈ Rq/p_ . The recommended parameter set described in Section 6.2 yields _δ <_ 2<sup>_−_136</sup> . 

**Unbiased keys:** Since our moduli are powers of 2 and as such non-prime, there exists (negligibly small) exceptional sets for **_s_** and **_s_**<sup>**_′_**</sup> such that the common key is biased. The intuition is that if all coefficients of the polynomials in **_s_** or **_s_**<sup>**_′_**</sup> are divisible by a high power of 2, the same property will hold for **_As_** or **_A_**<sup>_T_</sup> **_s_**<sup>**_′_**</sup> , and their scaled versions. The following theorem however shows that outside these sets, uniformity is attained. 

7 

**Theorem 2.** _Let Sbad denote the set of elements in Rq_<sup>_l×_1</sup> _for which none of the coefficients w satisfies_ `gcd` ( _w, q_ ) _|_ ( _q/p_ ) _and let Sbad_<sup>_′denotethesetofelementsin_</sup> _Rq_<sup>_l×_1</sup> _for which none of the coefficients w satisfies_ `gcd` ( _w, p_ ) _|_ ( _p/_ 2) _. Let_ **_s_** _,_ **_s_**<sup>_′_</sup> _← βµ_ ( _Rq_<sup>_l×_1</sup> ) _and let_ **_A_** _←U_ ( _Rq_<sup>_l×l_</sup> ) _and determine k as follows:_ 

_1._ **_b_** = `bits` ( **_As_** + **_h_** _, ϵq, ϵp_ ) _2. k_ = `bits` ( **_b_**<sup>_T_</sup> ( **_s_**<sup>_′_</sup> mod _p_ ) + _h_ 1 _, ϵp,_ 1) 

_For_ **_s_** _∈/ Sbad and_ **_s_**<sup>_′_</sup> _∈/ Sbad_<sup>_′,kisdistributeduniformlyfor_</sup><sup>**_A_**</sup><sup>_←U_(</sup><sup>_R_</sup> _q_<sup>_l×l_</sup> ) _. This occurs with a probability Pr_ [ **_s_** _∈/ Sbad_ ] _Pr_ [ **_s_**<sup>_′_</sup> _∈/ Sbad_<sup>_′_]</sup><sup>_._</sup> 

_Proof._ Note that the multiplication of a uniformly distributed coefficient of **_A_** , by a coefficient _w_ of **_s_** , is uniformly distributed in its _ϵp_ most significant bits if `gcd` ( _w, q_ ) _|_ ( _q/p_ ), which is equivalent to stating that _⌊pw/q⌉_ is invertible in Z _p_ . 

The distribution of the coefficients of **_b_** = `bits` ( **_As_** + **_h_** _, ϵq, ϵp_ ) is as follows: since convolution of any distribution with a uniform distribution in Z _p_ results again in a uniform distribution in Z _p_ , we need only one term of the summation step to be uniform in its _p_ most significant bits. Therefore, the coefficients of **_b_** will be uniformly distributed if **_s_** _∈/ S_ bad. 

Finally note that the distribution of _k_<sup>_′_</sup> = `bits` ( **_b_**<sup>_T_</sup> ( **_s_**<sup>_′_</sup> mod _p_ ) + _h_ 1 _, ϵp,_ 1) is uniform if **_b_** has a uniform distribution and if **_s_**<sup>_′_</sup> _∈/ s_<sup>_′_</sup> bad<sup>. As above, a multiplication</sup> of a uniformly distributed coefficient of **_b_** , with a coefficient _w_<sup>_′_</sup> of **_s_** is uniformly distributed in its most significant bit if `gcd` ( _w_<sup>_′_</sup> _, p_ ) _|_ ( _p/_ 2). Therefore, _k_ will be uniform if the coefficients of **_b_** are uniformly distributed and if **_s_**<sup>_′_</sup> _∈/ S_ bad<sup>_′_.The</sup> probability of a sampling **_s_** and **_s_**<sup>_′_</sup> so that _k_ has a uniform distribution is thus _Pr_ [ **_s_** _∈/ S_ bad] _Pr_ [ **_s_**<sup>_′_</sup> _∈/ S_ bad<sup>_′_].</sup> 

Since in our setting **_s_** _,_ **_s_**<sup>**_′_**</sup> are sampled from _βµ_ ( _Rq_ ), the coefficients are small and thus the only sampleable vector in _S_ bad and _S_ bad<sup>_′_istheallzerovector</sup> which occurs with probability 2<sup>_−_1436</sup> . In the rest of the paper, we assume that the secret vectors are not in the vector sets: **_s_** _∈/ S_ bad and **_s_**<sup>_′_</sup> _∈/ S_ bad<sup>_′_.</sup> 

**Security:** The security of Saber.KE can be reduced to the decisional ModLWR problem as shown by the following theorem. 

**Theorem 3.** _For any adversary A, there exist three adversaries B0, B1 and B2 such that Adv_<sup>_ind-rnd_</sup> _Saber.KE_<sup>(</sup><sup>_A_)⩽</sup><sup>_Advprg_</sup> `gen` ()<sup>(</sup><sup>_B_0) +</sup><sup>_Adv_</sup> _l,l,µ,q,p_<sup>_mod-lwr_(</sup><sup>_B_1) +</sup><sup>_Advmod-lwr_</sup> _l_ +1 _,l,µ,q,p_<sup>(</sup><sup>_B_2)</sup><sup>_,_</sup> _if q/p_ ⩽ _p/_ (2 _t_ ) _._ 

_Proof._ The IND-RND security of our key exchange can be expressed as the probability that an adversary A can distinguish between _k_ and a uniformly random key _k_<sup>ˆ</sup> _←U_ ( _K_ ), given the public information **_A_** , **_b_** , **_b_**<sup>_′_</sup> and _c_ . The proof proceeds by a sequence of games _Gi_ , where Adv _Gi_ ( _A_ ) = _|Pr_ [ _SA,i_ ] _−_ 1 _/_ 2 _|_ , in which _SA,i_ is the event that the adversary guesses correctly in game _Gi_ . The sequence of games is depicted in Figure 2. 

The first game _G_ 0 is the original game. In game _G_ 1, the public matrix is no longer generated using the pseudorandom generator `gen` (), but is sampled from a uniformly random distribution. An adversary that can distinguish these 

8 

<!-- Start of picture text -->
Game G 0: Game G 1: Game G 2:<br>1. seed A ←U ( { 0 ,  1 } 256 ) 1. 1.<br>2.3.4. Asb , = s ← ′ bits ← gen β ((seed η (R l q × A 1 )) 2. 3.4. Asb , = s ←U ′ bits ← ( β R( η l q × (R l ) l q × 1 ) 2.3. As ′ ←U← βη (R(R l q ×l q ×l ) 1 )<br>A · s + h , ϵq, ϵp ) A · s + h , ϵq, ϵp ) 4. b ←U (R l p × 1 )<br>5. b ′ = bits ( 5. b ′ = bits ( 5. b ′ = bits (<br>A T · s ′ + h , ϵq, ϵp ) A T · s ′ + h , ϵq, ϵp ) A T · s ′ + h , ϵq, ϵp )<br>6.7.8.9. v + ckk ˆ ′′ =  h←U ==1 bits b bits T (R · (2  bits v () v ′ , ϵ ′ , ϵp ( p s −, ′  1) , ϵ 1 p, ϵ, ϵt ) p ) 6.7.8.9. v + ckk ˆ ′′ =  h←U ==1 bits b bits T (R · (2  bits v () v ′ , ϵ ′ , ϵp ( p s −, ′  1) , ϵ 1 p, ϵ, ϵt ) p ) 6.7.8. v + ck ′′ =  h ==1 bits b bits T · (  bits v ( v ′ , ϵ ′ , ϵp ( p s −, ′  1) , ϵ 1 p, ϵ, ϵt ) p )<br>10. u ←U ( { 0 ,  1 } ) 10. u ←U ( { 0 ,  1 } ) 9. k ˆ ←U (R2)<br>11. if u = 0: 11. if u = 0: 10. u ←U ( { 0 ,  1 } )<br>return( A , b , b ′ , c, k ′ ) return( A , b , b ′ , c, k ′ ) 11. if u = 0:<br>12. else: 12. else: return( A , b , b ′ , c, k ′ )<br>return( A , b , b ′ , c, k ˆ ) return( A , b , b ′ , c, k ˆ ) 12. else:<br>return( A , b , b ′ , c, k ˆ )<br>Game G 3: Game G 4: Game G 5:<br>2. A ←U (R l q ×l ) 2. A ←U (R l q ×l )<br>3. s ′ ← βη (R l q × 1 ) 3. s ′ ← βη (R l q × 1 ) 2. A ←U (R l q ×l )<br>4. b ←U (R l p × 1 ) 4. b ←U (R l q × 1 ) 4. b ←U (R l q × 1 )<br>5. bA ′T = · bits s ′ +( h , ϵq, ϵp ) 5. bA ′T = · bits s ′ +( h , ϵq, ϵp ) 5. b ′ ←U (R l p × 1 )<br>6. v ′ = b T ·  bits ( s ′ , ϵp, ϵp ) 6. v ′ = bits ( 6. v ′ ←U (R l p × 1 )<br>7. 8. cvk + ′′ =  h, ϵ =1 p bitsbits − 1( , ( 2 vϵ ′ , ϵp −p,  1) ϵq − 1) 7.8. b cvk T′′ = , ϵ = · q bits s bits ′ − +1(  h, ϵ ( v 1 p, ϵ ′ , ϵ−qq, ϵ 1) ,  1) p ) 7.8. cvk ′′ = , ϵ = p bitsbits − 1( , ϵ ( vp ′ , ϵ−p 1) ,  1)<br>9. k ˆ ←U (R2) 9. k ˆ ←U (R2) 9. k ˆ ←U (R2)<br>10.11. u if ←Uu = 0:( { 0 ,  1 } ) 10.11. u if ←Uu = 0:( { 0 ,  1 } ) 10. u ←U ( { 0 ,  1 } )<br>12. return(else: A , b , b ′ , c, k ′ ) 12. return(else: A , b , b ′ , c, k ′ ) 11. return(if u = 0: A , b , b ′ , c, k ′ )<br>return( A , b , b ′ , c, k ˆ ) return( A , b , b ′ , c, k ˆ ) 12. else:<br>return( A , b , b ′ , c, k ˆ )<br><!-- End of picture text -->

Figure 2: Sequence of games that are used in the proof of Theorem 3 

two games, can also distinguish the matrix generated through the pseudorandom generator from a uniformly random matrix, and therefore _|Pr_ [ _SA,_ 0] _−Pr_ [ _SA,_ 1] _|_ ⩽ Adv<sup>prg</sup> `gen` ()<sup>(</sup><sup>_B_0).</sup> 

During the second game _G_ 2, the vector **_b_** is generated uniformly random, so that ( **_A_** _,_ **_b_** ) is a uniformly distributed sample, in contrast to the first game _G_ 1, where ( **_A_** _,_ **_b_** ) forms a Mod-LWR sample. An adversary that can distinguish between game _G_ 1 and _G_ 2 has also solved the decisional Mod-LWR problem on this sample, and therefore _|Pr_ [ _SA,_ 1] _− Pr_ [ _SA,_ 2] _|_ ⩽ Adv<sup>mod-lwr</sup> _l,l,µ,q,p_<sup>(</sup><sup>_B_1).</sup> 

In game _G_ 2, the number of bits dropped in the calculation of **_b_**<sup>_′_</sup> and _c_ is _ϵq − ϵp_ and _ϵp − ϵt −_ 1 respectively, which is reduced to _ϵq − ϵp_ in game _G_ 3. If we compare _G_ 3 to _G_ 2, since ( _ϵq − ϵp_ ) ⩽ ( _ϵp − ϵt −_ 1), the number of dropped bits is the same or less, and therefore the number of available bits to the adversary 

9 

**Algorithm 1:** `Saber` _._ `KeyGen` <u>()</u> 

**1** _seed_ **_A_** _←U_ ( _{_ 0 _,_ 1 _}_<sup>256</sup> ) **2** **_A_** _←_ `gen` (seed **_A_** ) _∈ Rq_<sup>_l×l_</sup> **3** **_s_** _← βµ_ ( _Rq_<sup>_l×_1</sup> ) **4** **_b_** = `bits` ( **_As_** + **_h_** _, ϵq, ϵp_ ) _∈ Rp_<sup>_l×_1</sup> **5 return** ( _pk_ := ( **_b_** _, seed_ **_A_** ) _, sk_ := **_s_** ) 

is at least the same. From this we conclude that _G_ 2 is at least as hard as _G_ 3: _∀A, ∃A_<sup>_′_</sup> : Adv _G_ 2( _A_ ) ⩽ Adv _G_ 3( _A_<sup>_′_</sup> ). 

Up to game _G_ 3, the coefficients of the inputs for the generation of **_b_**<sup>_′_</sup> and _c_ are in Z _q_ and Z _p_ respectively. This is evened up to coefficients in Z _q_ for all of the calculations in game _G_ 4. Using **_s_**<sup>_′_</sup> instead of `bits` ( **_s_**<sup>_′_</sup> _, ϵp, ϵp_ ) does not change the result of the multiplication because _µ < p_ . Since _p | q_ , generating **_b_** from _U_ (R<sup>_l_</sup> _q_<sup>_×_1</sup> ) instead of _U_ (R<sup>_l_</sup> _p_<sup>_×_1</sup> ) makes the advantage of the adversary in Game _G_ 4 at least as big as in game _G_ 3, as the adversary in Game _G_ 4 can easily calculate the same value for _c_ as in Game _G_ 3. Cutting off the last _ϵq − ϵp_ bits of _v_<sup>_′_</sup> does not change the game since they are not used in the rest of the protocol. Thus we can state: _∀A_<sup>_′_</sup> _, ∃A_<sup>_′′_</sup> : Adv _G_ 3( _A_<sup>_′_</sup> ) ⩽ Adv _G_ 4( _A_<sup>_′′_</sup> ). 

Analogous to game _G_ 2, **_b_**<sup>_′_</sup> and _c_ are replaced by a uniform random value in game _G_ 5, so that the Mod-LWR samples ( **_A_** _,_ **_b_**<sup>_′_</sup> ) and ( **_b_** _, v_<sup>_′_</sup> ), which share secret key **_s_**<sup>_′_</sup> , are replaced by uniformly random variables. Therefore, an adversary that can distinguish between these two games, can solve the corresponding Mod-LWR decisional problem and thus _|Pr_ [ _SA′′,_ 4] _− Pr_ [ _SA′′,_ 5] _|_ ⩽ Adv<sup>mod-lwr</sup> _l_ +1 _,l,µ,q,p_<sup>(</sup><sup>_B_2).</sup> In the resulting game _G_ 5, the keys are independent of the values **_b_** , **_b_**<sup>_′_</sup> and _v_<sup>_′_</sup> . Moreover, since _v_<sup>_′_</sup> is uniformly distributed in R<sup>_l_</sup> _p_<sup>_×_1</sup> , where _q_ is a power of two, and since _k_<sup>_′_</sup> is generated as the first bit of _v_<sup>_′_</sup> , _k_<sup>_′_</sup> is also uniformly distributed, and therefore _Pr_ [ _SA′′,_ 5] = 1 _/_ 2. Working backwards from the probability of success in game _G_ 5 to that in game _G_ 0, and using the fact that Adv _Gi_ ( _A_ ) = _|Pr_ [ _SA,i_ ] _−_ 1 _/_ 2 _|_ , gives the desired result. 

## **4 CPA secure encryption** 

The key exchange scheme of the previous section can be transformed into a CPA secure public-key encryption scheme Saber.PKE by using a similar transformation from Diffie-Hellman key exchange to ElGamal encryption, i.e. the messages sent by Alice now define her public key, and the encryption simply consists of an XOR with the common (pre)key. 

The message space is _M ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> and a message _m ∈M_ is represented as an element in _Rq_ with coefficients in _{_ 0 _,_ 1 _}_ . Algorithms 1 to 3 describe the public-key encryption scheme Saber.PKE=( `KeyGen,Enc,Dec` ), where the setup parameters are the same as in the key-exchange scheme described before. If the optional parameter _r_ is specified while calling Saber.ENC, it is used as a seed to generate the secret vector **_s_**<sup>_′_</sup> . 

10 

**Algorithm 2:** `Saber` _._ `Enc` <u>(</u> _pk_ = ( **_b_** _, seed_ **_A_** <u>)</u> _, m ∈M_ ; _r_ <u>)</u> 

**1** **_A_** _←_ `gen` (seed **_A_** ) _∈ Rq_<sup>_l×l_</sup> **2** **_s_**<sup>**_′_**</sup> _← βµ_ ( _Rq_<sup>_l×_1</sup> ) **3** **_b_**<sup>_′_</sup> = `bits` ( **_A_**<sup>_T_</sup> **_s_**<sup>_′_</sup> + **_h_** _, ϵq, ϵp_ ) _∈ Rp_<sup>_l×_1</sup> **4** _v_<sup>_′_</sup> = **_b_**<sup>_T_</sup> `bits` ( **_s_**<sup>_′_</sup> _, ϵp, ϵp_ ) + _h_ 1 _∈ Rp_ **5** _cm_ = `bits` ( _v_<sup>_′_</sup> + 2<sup>_ϵp−_1</sup> _m, ϵp, ϵt_ + 1) _∈ R_ 2 _t_ **6 return** _c_ := ( _cm,_ **_b_**<sup>**_′_**</sup> ) 

**Algorithm 3:** `Saber` _._ `Dec` <u>(</u> _sk_ = **_s_** _, cm,_ **_b_**<sup>**_′_**</sup> <u>)</u> 

**1** _v_ = **_b_**<sup>_′T_</sup> `bits` ( **_s_** _, ϵp, ϵp_ ) + _h_ 1 _∈ Rp_ **2** _m_<sup>_′_</sup> = `bits` ( _v −_ 2<sup>_ϵp−ϵt−_1</sup> _cm_ + _h_ 2 _, ϵp,_ 1) _∈ R_ 2 **3 return** _m_<sup>_′_</sup> 

**Security and Correctness:** It is easily seen that the security and correctness of the encryption scheme are equivalent to that of the key exchange introduced in Section 3. 

**Theorem 4.** _For any adversary A against Saber.PKE, there exists an adversary B against Saber.KE such that Adv_<sup>_ind-cpa_</sup> _Saber.PKE_<sup>(</sup><sup>_A_) =</sup><sup>_Adv_</sup> _Saber.KE_<sup>_ind-rnd_(</sup><sup>_B_)</sup><sup>_.Furthermore,_</sup> _Saber.PKE is_ (1 _− δ_ ) _correct if and only if Saber.KE is_ (1 _− δ_ ) _correct._ 

_Proof._ The proof proceeds by showing the equivalence between Saber.PKE and the combination of Saber.KE with a one time pad of the message _m_ with _k_ KE<sup>_′_.</sup> Note that the most significant bit of each coefficient of _v_<sup>_′_</sup> is equal to the corresponding (pre)key bits of _k_<sup>_′_</sup> in Saber.KE. Therefore, in line 5 of the Alg. 2, the addition is essentially a one time pad of the message bits _m_ with the coefficients of the (pre)key _k_<sup>_′_</sup> in the key exchange scheme (Protocol. 2). We can therefore conclude that the security of our encryption equals the security of our key exchange scheme for the same parameters. Similarly, it can be seen that Saber.PKE is correct if the keys _k_ and _k_<sup>_′_</sup> are equal. Hence, the correctness of the encryption scheme is equivalent to the correctness of the key exchange in Protocol. 2. 

## **5 CCA secure KEM** 

The CPA secure encryption scheme can be turned into a CCA secure KEM Saber.KEM=( `Encaps, Decaps` ) using an appropriate transformation. Recently, several post-quantum versions [30,46,42,32] of the Fujisaki-Okamoto transform with corresponding security reductions have been developed. At this point, the FO<sup>_⊥_</sup> transformation in [30] with post-quantum reduction from Jiang et al. [32] gives the tightest reduction for schemes with non-perfect correctness. However, other transformations could be used to turn Saber.PKE into a CCA secure KEM. 

11 

**Algorithm 4:** `Saber` _._ `Encaps` <u>(</u> _pk_ = ( **_b_** _, seed_ **_A_** <u>))</u> 

**1** _m ←U_ ( _{_ 0 _,_ 1 _}_<sup>256</sup> ) **2** ( _K, r_<sup>ˆ</sup> ) = _G_ ( _pk, m_ ) **3** _c_ = `Saber` _._ `Enc` ( _pk, m_ ; _r_ ) **4** _K_ = _H_ ( _K, c_<sup>ˆ</sup> ) **5 return** ( _c, K_ ) 

**Algorithm 5:** `Saber` _._ `Decaps` <u>(</u> _sk_ = ( **_s_** _, z_ <u>)</u> _, pk_ = ( **_b_** _, seed_ **_A_** <u>)</u> _, c_ <u>)</u> 

**1** _m_<sup>_′_</sup> = `Saber` _._ `Dec` ( **_s_** _, c_ ) **2** ( _K_<sup>ˆ</sup><sup>_′_</sup> _, r_<sup>_′_</sup> ) = _G_ ( _pk, m_<sup>_′_</sup> ) **3** _c_<sup>_′_</sup> = `Saber` _._ `Enc` ( _pk, m_<sup>_′_</sup> ; _r_<sup>_′_</sup> ) **4 if** _c_ = _c_<sup>_′_</sup> **then 5 return** _K_ = _H_ ( _K_<sup>ˆ</sup><sup>_′_</sup> _, c_ ) **6 else 7 return** _K_ = _H_ ( _z, c_ ) 

Saber.KEM is described in detail in Algorithm 4 and 5. The functions _G_ : _{_ 0 _,_ 1 _}_<sup>_∗_</sup> _→{_ 0 _,_ 1 _}_<sup>_l×n_</sup> and _H_ : _{_ 0 _,_ 1 _}_<sup>_∗_</sup> _→{_ 0 _,_ 1 _}_<sup>_n_</sup> are hash functions, _z_ is a secret random seed used to return a pseudorandom response when the re-encryption fails, and the `Saber` _._ `Enc` and `Saber` _._ `Dec` functions are from the CPA secure asymmetric encryption described in Section 4. 

**Correctness:** Following Hofheinz et al. [30], Saber.KEM is (1 _− δ_ ) correct if and only if Saber.PKE is (1 _− δ_ ) correct, and thus also if and only if Saber.KE is (1 _− δ_ ) correct. 

**Security:** By modeling the hash functions _G_ and _H_ as random oracles, a lower bound on the CCA security can be proven. We use the security bounds of Hofheinz et al. [30], which considers a KEM variant of the Fujisaki-Okamoto transform that can also handle a small failure probability _δ_ of the encryption scheme. This failure probability should be cryptographically negligibly small for the security to hold. Using Theorem 3.2 and Theorem 3.4 from [30], we get the following theorems for the security and correctness of our KEM in the random oracle model: 

**Theorem 5** (ROM, Hofheinz et al. [30]) **.** _For a IND-CCA adversary B, making at most qH and qG queries to respectively the random oracle G and H, and qD queries to the decryption oracle, there exists an IND-CPA adversary A such that:_ 

Jiang et al. [32] also provide a security reduction against a quantum adversary in the quantum random oracle model from IND-CCA security to OW-CPA security. IND-CPA with a sufficiently large message space implies OW-CPA [30,13]. Therefore, we can reduce the IND-CCA security of Saber.KEM to the IND.CPA security of the underlying public key encryption: 

12 

**Theorem 6** (QROM, Jiang et al. [32]) **.** _For any IND-CCA quantum adversary B, making at most qH and qG queries to respectively the random quantum oracle G and H, and qD many (classical) queries to the decryption oracle, there exists an adversary A such that:_ 

_K_ ˆ has **Multi** two **target** beneficial **protection:** effects: it makesAs described in [16], hashing the public key intosure that _K_ depends on the input of both parties, and it offers multi-target protection. In this scenario, the adversary uses Grover’s algorithm to precompute an _m_ that has a relatively high failure probability. Hashing _pk_ into _K_<sup>ˆ</sup> ensures that an attacker is not able to use precomputed ‘weak’ values of _m_ . 

## **6 Security analysis and parameter selection** 

### **6.2 Parameter selection** 

We use a python script to choose parameters _q_ , _p_ and _t_ for optimum usage of communication bandwidth, while achieving a quantum security level of 128 and failure probability 2<sup>_−_128</sup> . Additional parameter sets are generated as Light and Fire versions of the Saber.KEM, a light and paranoid version respectively. 

We would like to remark that choosing _p_ and _q_ as primes facilitates the use of NTT based polynomial multiplications [16,3]. However, rounding from _Rq_ to _Rp_ introduces significant bias as _p_ ∤ _q_ . Bogdanov et al. [15] proved the pseudorandomness of the LWR problem for moduli _p_ and _q_ for general lattices but left it as open problem for the ring version. However by choosing _p_ and _q_ 

14 

as a power-of-two, we can be assured of the pseudorandomness, which we also showed in Subsection. 3. 

|Sec Cat<br>fail prob|attack|Classical<br>Quantum<br>pk (B)|sk (B)|ciphertext (B)|
|---|---|---|---|---|
|LightSaber-KEM:|_k_ = 2,|_n_= 256, _q_ = 2<sup>13</sup>, _p_= 2<sup>10</sup>,|_t_= 2<sup>2</sup>,|_µ_= 10|
|1<br>2<sup>_−_120</sup>|primal<br>dual|126<br>115<br>672<br>126<br>115|1568|736|
|Saber-KEM: _k_ =|3, _n_=|256, _q_ = 2<sup>13</sup>, _p_= 2<sup>10</sup>, _t_= 2|<sup>3</sup>, _µ_=|8|
|3<br>2<sup>_−_136</sup>|primal<br>dual|199<br>181<br>992<br>198<br>180|2304|1088|
|FireSaber-KEM:|_k_ = 4,|_n_= 256, _q_ = 2<sup>13</sup>, _p_= 2<sup>10</sup>, _t_|= 2<sup>5</sup>,|_µ_= 6|
|5<br>2<sup>_−_165</sup>|primal<br>dual|270<br>246<br>1312<br>270<br>245|3040|1472|

Table 1: Security and correctness of Saber.KEM. 

## **8 Results** 

In Table 3, we compare our software implementation of Saber with software implementations of other lattice based post-quantum key exchange and encryption schemes. We compiled the Saber software using `gcc-7.1` with optimization flags `-O3` and measured computation time using a single core of a Intel(R) Core(TM) i7-6600U processor running at 2.60GHz with hyper-threading, Turbo-Boost, and 

18 

multi-core support disabled on a Dell Latitude E7470 laptop with Ubuntu 16 _._ 04 operating system. 

We remark that a totally fair comparison between the listed schemes and their software implementations is not possible since they are based on different hard problems, offer different levels of post-quantum security, implemented with different levels of optimizations and benchmarked on different platforms. Nevertheless, it is clear from the table that Saber is highly efficient both in terms of bandwidth and computation time. 

The implementations of Saber and Kyber use similar building blocks namely polynomial multiplication, generation of random matrix **_A_** , sampling of small secret (and error) polynomials and standard symmetric-key primitives for CCA transformations. In Table 2, we compare the performances of these building blocks excluding the symmetric-key primitives. Our Toom-Cook multiplication requires only 3,439 cycles. On the other hand, Kyber uses highly AVX-optimized NTT for polynomial multiplications. Furthermore, Kyber spends much less cycles in polynomial multiplications by generating the matrix _A_ in the NTT domain directly and by keeping the secret polynomials in the NTT domain. 

Saber does not require sampling of error polynomials, thus saving in computation time and entropy usage. As already described in Section 7 generating the random matrix _A_ is faster in Saber (when same pseudorandom number generator is used) since rejection sampling is not performed, resulting in optimal usage of random numbers. Though in this paper we consider only software implementation on high-end Intel processors, we would like to remark that random number generation is very expensive on resource-constrained platforms. When we compare the high-level _C_ implementations of Saber and Kyber, we see that Saber performs better than Kyber. 

Finally note that at the expense of either using larger public keys, or caching the decompressed matrix **_A_** , the implementation would run at least 25% faster. 

19 

Table 3: Performance and comparison of lattice-based KEMs and public-key encryption schemes. Cycles for key generation, encapsulation/encryption, and decapsulation/decryption are represented by **K** , **E** , and **D** respectively in the 5th column. Sizes of secret key ( _sk_ ), public key ( _pk_ ) and ciphertext ( _c_ ) are reported in the last column. Constant-time implementations are marked with ✓in the column **ct?** . Performances are measured on the platform specified in the beginning of this section if not indicated otherwise. 

|**Scheme**|**Problem**<br>**S**|**ecurit**|**y ct? Cy**|**cles**|**Bytes**|
|---|---|---|---|---|---|
||**Passivel**|**y secu**|**re KEM**<br>|**s**<br>||
|NewHope [4]<br>`AVX2 optimized`|Ring-LWE|255|✓<br>**K:** <br>**E:** <br>**D:**|88,920<sup>_†_</sup><br> 110,986<sup>_†_</sup><br> 19,422<sup>_†_</sup>|**sk:** 1,792<br>**pk:** 1,824<br>**c:** 2,048|
|Frodo [17]|LWE|130|✓<br>**K:** <br>**E:** <br>**D:**|2,938,000<sup>_⋆_</sup><br> 3,484,000<sup>_⋆_</sup><br> 338,000<sup>_⋆_</sup>|**sk:** 11,280<br>**pk:** 11,296<br>**c:** 11,288|
||**CCA-**|**secure**|**KEMs**|||
|NTRU Prime [11]|NTRU|129|✓<br>**K:** <br>**E:** <br>**D:**|6,115,384<sup>_⊗_</sup><br> 59,600<sup>_⊗_</sup><br> 97,452<sup>_⊗_</sup>|**sk:** 1,600<br>**pk:** 1,218<br>**c:** 1,047|
|NTRU KEM [31]<br>`AVX2 optimized`|NTRU|123|✓<br>**K:** <br>**E:** <br>**D:**|307,914<sup>_⊥_</sup><br> 48,646<sup>_⊥_</sup><br> 67,338<sup>_⊥_</sup>|**sk:** 1,422<br>**pk:** 1,140<br>**c:** 1,281|
|spLWE-KEM [21]|spLWE|128|?<br>**K:** <br>**E:** <br>**D:**|336,700<sup>_‡_</sup><br> 813,800<sup>_‡_</sup><br> 785,200<sup>_‡_</sup>|**sk:** ?<br>**pk:** ?<br>**c:** 804|
|Kyber [16]|Module-LWE|161|✓<br>**K:**|92,461|**sk:** 2400|
|`AVX2 + assembly`|||**E:**|120,280|**pk:** 1088|
|`optimized`|||**D:**|113,718|**c:** 1152|
|Kyber [16]|Module-LWE|161|✓<br>**K:**|251,856|**sk:** 2400|
|`C implementation`|||**E:** <br>**D:**|336,112<br> 435,836|**pk:** 1088<br>**c:** 1152|
|Saber|Module-LWR|180|✓<br>**K:**|101,138|**sk:** 2,304|
|`AVX2 optimized`|||**E:** <br>**D:**|125,392<br> 129,138|**pk:** 992<br>**c:** 1,088|
|Saber|Module-LWR|180|✓<br>**K:**|190,420|**sk:** 2,304|
|`C implementation`|||**E:** <br>|279,291<br>|**pk:** 992<br>|
||||**D:**|306,346|**c:** 1,088|
|**CC**|**A-secure publi**|**c-key **|**encrypti**|**on scheme**|**s**|
|NTRUEncrypt [28]|NTRU|159|_×_<br>**K:** <br>**E:** <br>**D:**|1,194,816<sup>_†_</sup><br> 57,440<sup>_†_</sup><br> 110,604<sup>_†_</sup>|**sk:** 1120<br>**pk:** 1,027<br>**c:** 980|
|Lizard [22]|LWE,LWR|128|_×_<br>**K:** <br>**E:** <br>**D:**|97,573,000<sup>_†_</sup> <br> 35,050<sup>_†_</sup><br> 80,840<sup>_†_</sup>|**sk:** 466,944<sup>_•_</sup><br>**pk:** 2,031,616<sup>_•_</sup><br>**c:** 1,072|

> _†_ Compiled using `gcc-4.9.2` and benchmarked on Intel Core i7-4770K (Haswell) computer 

> _⋆_ Benchmarked on a 2.6GHz Intel Xeon E5 (Sandy Bridge) with hyperthreading enabled. 

> _⊗_ Benchmarked on an Intel Haswell processor. 

> _‡_ Benchmarked on a Macbook Pro PC with 2.6GHz Intel Core i5. 

> _•_ Following the explanation provided in [16]. 

> _⊥_ Benchmarked on an Intel i7-Haswell, 3.5GHz processor. 

20 

## **A Toom-Cook-4 polynomial multiplication.** 

Here we describe the Toom-Cook polynomial multiplication used in our implementation. 

**Algorithm 6:** Toom-Cook Algorithm 

**Input:** Two polynomials _A_ ( _x_ ) and _B_ ( _x_ )of degree _n_ = 256 **Output:** _C_ ( _x_ ) = _A_ ( _x_ ) _∗ b_ ( _x_ ) `// Splitting` _A_ ( _x_ ) `into four polynomials of size` 64 **1** _A_ ( _y_ ) = _A_ 3 _· y_<sup>3</sup> + _A_ 2 _· y_<sup>2</sup> + _A_ 1 _· y_ + _A_ 0 where _y_ = _x_<sup>64</sup> `// Splitting` _B_ ( _x_ ) `into four polynomials of size` 64 **2** _B_ ( _y_ ) = _B_ 3 _· y_<sup>3</sup> + _B_ 2 _· y_<sup>2</sup> + _B_ 1 _· y_ + _B_ 0 `// Evaluation of the polynomials at` _y_ = _{_ 0 _, ±_ 1 _, ±_ 2<sup><u>1</u></sup><sup>_,_2</sup><sup>_, ∞}_</sup><sup>`.These`</sup> `multiplications are computed using Karatsuba` **3** _w_ 1 = _A_ ( _∞_ ) _∗ B_ ( _∞_ ) = _A_ 3 _∗ B_ 3 **4** _w_ 2 = _A_ (2) _∗ B_ (2) = ( _A_ 0 + 2 _· A_ 1 + 4 _· A_ 2 + 8 _· A_ 3) _∗_ ( _B_ 0 + 2 _· B_ 1 + 4 _· B_ 2 + 8 _· B_ 3) **5** _w_ 3 = _A_ (1) _∗ B_ (1) = ( _A_ 0 + _A_ 1 + _A_ 2 + _A_ 3) _∗_ ( _B_ 0 + _B_ 1 + _B_ 2 + _B_ 3) **6** _w_ 4 = _A_ ( _−_ 1) _∗ B_ ( _−_ 1) = ( _A_ 0 _− A_ 1 + _A_ 2 _− A_ 3) _∗_ ( _B_ 0 _− B_ 1 + _B_ 2 _− B_ 3) **7** _w_ 5 = _A_ ( 2<sup><u>1</u>)</sup><sup>_∗B_(</sup> 2<sup><u>1</u>) = (8</sup><sup>_· A_0 + 4</sup><sup>_· A_1 + 2</sup><sup>_· A_2 +</sup><sup>_A_3)</sup><sup>_∗_(8</sup><sup>_· B_0 + 4</sup><sup>_· B_1 + 2</sup><sup>_· B_2 +</sup><sup>_B_3)</sup> **8** _w_ 6 = _A_ (<sup>_−_</sup> 2<sup><u>1</u>)</sup><sup>_∗B_(</sup><sup>_−_</sup> 2<sup><u>1</u>) = (8</sup><sup>_·A_0</sup><sup>_−_4</sup><sup>_·A_1 +2</sup><sup>_·A_2</sup><sup>_−A_3)</sup><sup>_∗_(8</sup><sup>_·B_0</sup><sup>_−_4</sup><sup>_·B_1 +2</sup><sup>_·B_2</sup><sup>_−B_3)</sup> **9** _w_ 7 = _A_ (0) _∗ B_ (0) = _A_ 0 _∗ B_ 0 `// Interpolation` **10** _w_ 2 = _w_ 2 + _w_ 5 **11** _w_ 6 = _w_ 6 _− w_ 5 **12** _w_ 4 = ( _w_ 4 _− w_ 3) _/_ 2 **13** _w_ 5 = _w_ 5 _− w_ 1 _−_ 64 _· w_ 7 **14** _w_ 3 = _w_ 3 + _w_ 4 **15** _w_ 5 = 2 _· w_ 5 + _w_ 6 **16** _w_ 2 = _w_ 2 _−_ 65 _· w_ 3 **17** _w_ 3 = _w_ 3 _− w_ 7 _− w_ 1 **18** _w_ 2 = _w_ 2 + 45 _· w_ 3 **19** _w_ 5 = ( _w_ 5 _−_ 8 _· w_ 3) _/_ 24 **20** _w_ 6 = _w_ 6 + _w_ 2 **21** _w_ 2 = ( _w_ 2 + 16 _· w_ 4) _/_ 18 **22** _w_ 3 = _w_ 3 _− w_ 5 **23** _w_ 4 = _−_ ( _w_ 4 + _w_ 2) **24** _w_ 6 = (30 _· w_ 2 _− w_ 6) _/_ 60 **25** _w_ 2 = _w_ 2 _− w_ 6 **26 return** _w_ 1 _· y_<sup>6</sup> + _w_ 2 _· y_<sup>5</sup> + _w_ 3 _· y_<sup>4</sup> + _w_ 4 _· y_<sup>3</sup> + _w_ 5 _· y_<sup>2</sup> + _w_ 6 _· y_ + _w_ 7; 

24