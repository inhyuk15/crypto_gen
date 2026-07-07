# HAETAE 

## **Algorithm Specifications and Supporting Documentation** 

Jung Hee Cheon, Hyeongmin Choe, Julien Devevey, Tim G¨uneysu, Dongyeon Hong, Markus Krausz, Georg Land, Junbum Shin, Damien Stehl´e, MinJune Yi. 

May 31, 2023. 

### **2 Preliminaries** 

#### **2.1 Notations** 

Matrices are denoted in bold font and upper case letters (e.g., **A** ), while vectors are denoted in bold font and lowercase letters (e.g., **y** or **z** 1). The _i_ -th component of a vector is denoted with subscript _i_ (e.g., _yi_ for the _i_ -th component of **y** ). 

Every vector is a column vector. We denote concatenation between vectors by putting the rows below as ( **u** _,_ **v** ) and the columns on the right as ( **u** _|_ **v** ). We naturally extend the latter notation to concatenations between matrices and vectors (e.g., ( **A** _|_ **b** ) or ( **A** _|_ **B** )). 

We let _R_ = Z[ _x_ ] _/_ ( _x_<sup>_n_</sup> + 1) be a polynomial ring where _n_ is a power of 2 integer and for any positive integer _q_ the quotient ring _Rq_ = Z[ _x_ ] _/_ ( _q, x_<sup>_n_</sup> + 1) = Z _q_ [ _x_ ] _/_ ( _x_<sup>_n_</sup> + 1). We abuse notations and identify _R_ 2 with the set of elements in _R_ with binary coefficients. We also let _R_ R = R[ _x_ ] _/_ ( _x_<sup>_n_</sup> + 1) be a polynomial ring over real numbers. For an integer _η_ , we let _Sη_ denote the set of polynomials of degree less than _n_ with coefficients in [ _−η, η_ ] _∩_ Z. Given **y** = (<sup>�</sup> 0 _≤i<n_<sup>_yixi, · · ·,_�</sup> 0 _≤i<n_<sup>_ynk−n_+</sup><sup>_ixi_)</sup><sup>_⊤∈Rk_(or</sup><sup>_Rk_</sup> R<sup>),wedefineits</sup><sup>_ℓ_2-normas</sup> the _ℓ_ 2-norm of the corresponding “flattened” vector _∥_ **y** _∥_ 2 = _∥_ ( _y_ 0 _, · · · , ynk−_ 1)<sup>_⊤_</sup> _∥_ 2. 

Let _BR,m_ ( _r,_ **c** ) = _{_ **x** _∈R_<sup>_m_</sup> R<sup>_|∥_</sup><sup>**x**</sup><sup>_−_</sup><sup>**c**</sup><sup>_∥_2</sup><sup>_≤r}_denotethecontinuoushyperballwithcenter</sup><sup>**c**</sup><sup>_∈Rm_and</sup> radius _r >_ 0 in dimension _m >_ 0. When **c** = **0** , we omit it. Let _B_ (1 _/N_ ) _R,m_ ( _r,_ **c** ) = (1 _/N_ ) _R_<sup>_m_</sup> _∩BR,m_ ( _r,_ **c** ) denote the discretized hyperball with radius _r >_ 0 and center **c** _∈R_<sup>_m_</sup> in dimension _m >_ 0 with respect to a positive integer _N_ . When **c** = **0** , we omit it. Given a measurable set _X ⊆R_<sup>_m_</sup> of finite volume, we let _U_ ( _X_ ) denote the continuous uniform distribution over _X_ . It admits **x** _�→ χX_ ( **x** ) _/_ Vol( _X_ ) as a probability density, where _χX_ is the indicator function of _X_ and Vol( _X_ ) is the volume of the set _X_ . For the normal distribution over R centered at _µ_ with standard deviation _σ_ , we use the notation _N_ ( _µ, σ_ ). 

For a positive integer _α_ , we define _r_ mod<sup>_±_</sup> _α_ as the unique integer _r_<sup>_′_</sup> in the range [ _−α/_ 2 _, α/_ 2) satisfying the relation _r_ = _r_<sup>_′_</sup> mod _α_ . We also define _r_ mod<sup>+</sup> _α_ as the unique integer _r_<sup>_′_</sup> in the range [0 _, α_ ) that satisfies _r_ = _r_<sup>_′_</sup> mod _α_ . We denote the least significant bit of an integer _r_ with LSB( _r_ ). We naturally extend this to integer polynomials and vectors of integer polynomials, by applying it component-wise. 

#### **2.2 Lattice assumptions** 

We first recall the well-known lattice assumptions MLWE and MSIS on algebraic lattices. 

**Definition 1 (Decision-** MLWE _n,q,k,ℓ,η_ **).** _For positive integers q, k, ℓ, η and the dimension n of R, we say that the advantage of an adversary A solving the decision-_ MLWE _n,q,k,ℓ,η problem is_ 

**Definition 2 (Search-** MSIS _n,q,k,ℓ,β_ **).** _For positive integers q, k, ℓ, a positive real number β and the dimension n of R, we say that the advantage of an adversary A solving the search-_ MSIS _n,q,k,ℓ,β problem is_ 

#### **2.3 Bimodal hyperball rejection sampling** 

Recently, Devevey et al. [DFPS22] conducted a study of rejection sampling in the context of lattice-based Fiat-Shamir with Aborts signatures. They observe that (continuous) uniform distributions over hyperballs can be used to obtain compact signatures, with a relatively simple rejection procedure. To make masking easier, HAETAE uses (discretized) uniform distributions over hyperballs, in the bimodal context. The proof of the following lemma is available in Appendix B. 

6 

**Lemma 1** **<u>(Bimodal</u> Hyperball Rejection Sampling).** _Let n be the degree of R, c >_ 1 _, r, t, m >_ 0 _, and r_<sup>_′_</sup> _≥ √r_<sup>2</sup> + _t_<sup>2</sup> _. Define M_ = 2( _r_<sup>_′_</sup> _/r_ )<sup>_mn_</sup> _and set_ 

_Let_ **v** _∈R_<sup>_m_</sup> _∩B_ (1 _/N_ ) _R,m_ ( _t_ ) _. Let p_ : R<sup>_m_</sup> _→{_ 0 _,_ 1 _/_ 2 _,_ 1 _} be defined as follows_ 

_Then there exists M_<sup>_′_</sup> _≤ cM such that the output distributions of the two algorithms from Figure 2 are identical._ 

<!-- Start of picture text -->
− v v<br><!-- End of picture text -->

Fig. 1: The HAETAE eyes 

Figure 1 illustrates (the continuous version) of the rejection sampling that we consider. The black circles have radii equal to _r_<sup>_′_</sup> and the pink circle has radius _r_ . We sample a vector **z** uniformly inside one of the black circles (with probability 1 _/_ 2 for each) and keep **z** with _p_ ( **z** ) = 1 _/_ 2 if **z** lies in the blue zone, with probability _p_ ( **z** ) = 1 if it lies inside the pink circle but not in the blue zone, and with probability _p_ ( **z** ) = 0 everywhere else. 

|_A_(**v**) :|_B_ :|
|---|---|
|1: **y** _←U_(_B_(1_/N_)_R,m_(_r_<sup>_′_</sup>))|1: **z**_←U_(_B_(1_/N_)_R,m_(_r_))|
|2: **b**_←U_(_{_0_,_1_}_)|2: return **z** with probability 1_/M _<sup>_′_</sup>|
|3: **z**_←_**y**+ (_−_1)<sup>_b_</sup>**v**|3: **else** return _⊥_|
|4: return **z** with probability _p_(**z**)||
|5: **else** return _⊥_||

Fig. 2: Bimodal hyperball rejection sampling 

#### **2.4 Sampling in a continuous hyperball-uniform** 

We explain how to sample from a uniform continuous hyperballl distribution. Multiple strategies exist, and the one we choose is such that a _k_ -dimensional module sample is obtained using only _kn_ +2 one-dimensional continuous Gaussian samples: 

7 

<!-- Start of picture text -->
y ← U ( BR,k ( r ′′ ))<br>1: yi ←N (0 ,  1) for i  = 0 , · · · , nk  + 1<br>2: L ←∥ ( y 0 , · · · , ynk +1) ⊤ ∥ 2<br>3: y ← r ′′ /L ·  ( � n i =0 − 1 yi xi, · · · ,  � n i =0 − 1 ynk−n + i xi ) ⊤ ∈Rk R<br>4: return y<br><!-- End of picture text -->

Fig. 3: Continuous hyperball uniform sampling 

**Lemma 2 ([VGS17]).** _The distribution of the output of the algorithm in Figure 3 is U_ ( _BR,k_ ( _r_<sup>_′′_</sup> )) _._ 

#### **2.5 Challenge sampling** 

The challenges we use are polynomials _c ∈R_ with binary coefficients and some of them are nonzero. The challenge space has size � _nτ_ � if exactly _τ_ coefficients are nonzero. To sample such challenges we rely on the (binary version of) SampleInBall algorithm from Dilithium, which we recall in Fig. 4. 

<!-- Start of picture text -->
SampleInBall( ρ, τ )<br>1: initialize  c  =  c 0 c 1  . . . c 255 = 00  . . .  0<br>2: For i  = 256  − τ to 255<br>3: j ←{ 0 , . . . , i}<br>4: ci =  cj<br>5: cj = 1<br>6: return c<br><!-- End of picture text -->

Fig. 4: Challenge sampling algorithm 

For the highest security, however, we require 255 bits of entropy for the challenge, which cannot be reached with �256 _τ_ �. To achieve it, we replace the challenge sampling for the parameter set with the following. Given a 256-bits hash _w_ 0 _. . . w_ 255 with Hamming weight _w_ , do the following. If _w <_ 128, return<sup>�255</sup> _i_ =0<sup>_wixi_.</sup> If _w_ = 128, return<sup>�255</sup> _i_ =0<sup>_wi ⊗w_0</sup><sup>_xi_.Otherwise,return�255</sup> _i_ =0<sup>_wi ⊗_1</sup><sup>_xi_.Exactlyhalfofallbinarypolynomials</sup> are reachable this way, which means that the challenge set has size 2<sup>255</sup> as desired. 

#### **2.6 High and low bits** 

In our scheme, the signature is comprised of a vector **z** , which we split in two, and a polynomial **c** . The upper part of **z** is split between its high and low bits, and the high bits are compressed. The lower part of **z** is not sent, and we instead send a so-called hint. Our technique may be reminiscent of the one from Dilithium [DKL<sup>+</sup> 18], which shares the high-level idea. We first recall the Euclidean division with a centered remainder. 

**Lemma 3.** _Let a ≥_ 0 _and b >_ 0 _. It holds that_ 

_and this writing as a_ = _bq_ + _r with r ∈_ [ _−b/_ 2 _, b/_ 2) _is unique._ 

We define our base decomposition function. 

8 

**Definition 3 (High and low bits).** _Let r ∈_ Z _and α be a power of two. Successively define r_ 1 = _⌊_ ( _r_ + _α/_ 2) _/α⌋ and r_ 0 = _r_ mod<sup>_±_</sup> _α. Finally, define the tuple:_ 

We extend these definitions to vectors by applying them component-wise. We state that this decomposition lets us recover the original element and bound the components of the decomposition. 

**Lemma 4.** _Let α be a power of two. Let q >_ 2 _be a prime with α|_ 2( _q −_ 1) _and r ∈_ Z _. Then it holds that_ 

**Proof** _._ By Lemma 3, there exists a unique representation 

By identifying HighBits( _r, α_ ) and LowBits( _r, α_ ) in the above equation, we obtain the first result. Next, by definition of mod<sup>_±_</sup> , we have that _r_<sup>_′_</sup> _∈_ [ _−α/_ 2 _, α/_ 2). 

For the second range, since _r �→⌊_ ( _r_ + _α/_ 2) _/α⌋_ is a non-decreasing function, it is sufficient to show that _⌊_ (2 _q −_ 1+ _α/_ 2) _/α⌋≤⌊_ (2 _q −_ 1) _/α⌋_ . By assumption on _q_ , we have (2 _q −_ 1+ _α/_ 2) _≤⌊_ (2 _q −_ 1) _/α⌋α_ + _α −_ 1. Dividing by _α_ and taking the floor yields the result. 

We define HighBits<sup>_z_1</sup> ( _r_ ) = HighBits( _r,_ 256) and LowBits<sup>_z_1</sup> ( _r_ ) = LowBits( _r,_ 256). 

**High and low bits for hint** In order to produce the hint that we send instead of the lower part of **z** , we could use the previous bit decomposition. However, as noted in [DKL<sup>+</sup> 18, Appendix B] in a preliminary version, a slight modification allows to further reduce the entropy of the hint. 

The idea is to pack the high bits in the range [0 _,_ 2( _q −_ 1) _/α_ h). This is possible if we use the range [ _−α_ h _/_ 2 _−_ 2 _,_ 0) to represent the integers that are close to 2 _q −_ 1. 

**Definition 4 (High and low bits for hint).** _Let r ∈_ Z _. Let q be a prime and α_ h _|_ 2( _q −_ 1) _be a power of two. Let m_ = 2( _q −_ 1) _/α_ h _and_ 

_If r_ 1 = _m, let_ ( _r_ 0<sup>_′, r_</sup> 1<sup>_′_) = (</sup><sup>_r_0</sup><sup>_−_2</sup><sup>_,_0)</sup><sup>_._</sup> _Else,_ ( _r_ 0<sup>_′, r_</sup> 1<sup>_′_) = (</sup><sup>_r_0</sup><sup>_, r_1)</sup><sup>_.Wedefine:_</sup> 

As before, we extend these definitions to vectors by applying them component-wise. We state that this decomposition lets us recover the original element and bound the decomposition components. 

**Lemma 5.** _Let r ∈_ Z _. Let q be a prime, α_ h _|_ 2( _q −_ 1) _be a power of two and define m_ = 2( _q −_ 1) _/α_ h _. It holds that_ 

9 

**Proof** _._ Let _r ∈_ [0 _,_ 2 _q −_ 1]. Let _r_ 0, _r_ 1, _r_ 0<sup>_′_,and</sup><sup>_r_</sup> 1<sup>_′_definedasinDefinition4.If</sup><sup>_r_</sup> 0<sup>_′_=</sup><sup>_r_0and</sup><sup>_r_</sup> 1<sup>_′_=</sup><sup>_r_1,the</sup> equality _r_ 0<sup>_′_+</sup><sup>_r_</sup> 1<sup>_′· α_h=</sup><sup>_r_0+</sup><sup>_r_1</sup><sup>_· α_hmod 2</sup><sup>_q_holdsvacuously.</sup> If not, then _r_ 0<sup>_′_=</sup><sup>_r_0</sup><sup>_−_2and</sup><sup>_r_</sup> 1<sup>_′_=</sup><sup>_r_1</sup><sup>_−_2(</sup><sup>_q −_1)</sup><sup>_/α_hand</sup><sup>_r_</sup> 0<sup>_′_+</sup><sup>_r_</sup> 1<sup>_′α_h=</sup><sup>_r_0+</sup><sup>_r_1</sup><sup>_α_h</sup><sup>_−_2</sup><sup>_q_.ByLemma4,weget</sup> the first equality. 

The second property stems from the second property in Lemma 4. The modifications to _r_ 0 make _r_ 0<sup>_′_lie</sup> in the range [ _−α_ h _/_ 2 _−_ 2 _, α_ h _/_ 2). 

The last property stems from the third property in Lemma 4 and the fact that if _r_ 1 = _m_ , then we have _r_ 1<sup>_′_= 0.</sup> 

_⊓⊔_ 

10 

### **3 Specification** 

#### **3.1 Key generation** 

When using bimodal rejection sampling, the verification step relies on a key pair ( **A** _,_ **s** ) _∈R_<sup>_k_</sup> _p_<sup>_×_(</sup><sup>_k_+</sup><sup>_ℓ_)</sup> _× R_<sup>_k_</sup> _p_<sup>+</sup><sup>_ℓ_</sup> such that **As** = _−_ **As** mod _p_ . To generate such a pair, following [DDLL13], we choose _p_ = 2 _q_ and aim at **As** = _q_ **j** mod 2 _q_ for **j** = (1 _,_ 0 _, . . . ,_ 0)<sup>_⊤_</sup> . 

**Key generation and encoding** To build a key pair ( **A** _,_ **s** ) satisfying the above, we start by generating an MLWE sample **b** _−_ **a** = **A** 0 **s** 0 + **e** 0 mod _q_ , where **A** 0 _← U_ ( _R_<sup>_k_</sup> _q_<sup>_×_(</sup><sup>_ℓ−_1)</sup> ), **a** _← U_ ( _R_<sup>_k_</sup> _q_<sup>) and (</sup><sup>**s**0</sup><sup>_,_</sup><sup>**e**0)</sup><sup>_←U_(</sup><sup>_S_</sup> _η_<sup>_ℓ−_1</sup> _×Sη_<sup>_k_).</sup> For any **b** = **b** 1 + **b** 0, we define **A** = (2( **a** _−_ **b** 1) + _q_ **j** _|_ 2 **A** 0 _|_ 2 **I** _k_ ) as well as **s** = (1 _|_ **s** 0 _|_ ( **e** 0 _−_ **b** 0)). One sees that **As** = _q_ **j** mod 2 _q_ . In practice, the verification key is then comprised of **b** 1 and the seed that allows generating **A** 0 and **a** . The secret key is the seed used to generate **s** and ( **A** 0 _,_ **a** ). 

It remains to choose the decomposition of **b** , that we see as an _nk_ -dimensional vector with coordinates in [0 _, q −_ 1]. We choose **b** 0 with coordinates in _{−_ 1 _,_ 0 _,_ 1 _}_ such that if a coordinate of **b** is odd, then it is rounded to the nearest multiple of 4. We can then write **b** = **b** 0 +2 **b** 1, where **b** 1 is encoded using _⌈_ log2( _q_ ) _−_ 1 _⌉_ bits per coordinate. This is computed coordinate-wise with **b** 0 = ( _−_ 1)<sup>_⌊_</sup><sup>**b**</sup><sup>_/_2</sup><sup>_⌋_mod2</sup> **b** mod 2, i.e. one less bit than **b** . In all of the following, we let (LowBits<sup>vk</sup> ( **b** ) _,_ HighBits<sup>vk</sup> ( **b** )) denote ( **b** 0 _,_ **b** 1). When **b** is uniform, we notice that the coordinates of **b** 0 roughly follow a (centered) binomial law with parameters (2 _,_ 1 _/_ 2), which experimentally leads to smaller choices for _β_ , which we discuss and introduce now. 

**Rejection sampling on the key** A critical step of our scheme is bounding _∥_ **s** _c∥_ 2, where **s** is generated as before and _c ∈R_ is a polynomial with coefficients in _{_ 0 _,_ 1 _}_ and has less than or equal to _τ_ nonzero coefficients. The lower this bound is, the smaller the signature is, which in turn leads to harder forging. In the key generation algorithm, we apply the following rejection condition for some heuristic value _β_ : 

where _m_ = _⌊n/τ ⌋_ and _r_ = _n_ mod _τ_ . We argue that the left hand side is a bound on<sup>_<u>n</u>_</sup> _τ_<sup>_· ∥_</sup><sup>**s**</sup><sup>_c∥_</sup> 2<sup>2andthatthis</sup> condition leads to asserting _∥_ **s** _c∥_ 2 _≤ β_ . 

**Lemma 6.** _For any c ∈{_ 0 _,_ 1 _}_<sup>_n_</sup> _with hamming weight τ and a secret_ **s** _∈ Sη_<sup>_k_+</sup><sup>_ℓ_</sup> _, n∥c_ **s** _∥_ 2<sup>2</sup><sup>_isboundedby_</sup> 

_where m_ = _⌊n/τ ⌋ and r_ = _n_ mod _τ ._ 

**Proof** _._ We first rewrite _∥_ **s** _c∥_<sup>2</sup> as: 

where **s** ( _ωj_ ) = ( **s** 1( _ωj_ ), _· · ·_ , **s** _k_ + _ℓ_ ( _ωj_ )), and _ωj_ ’s are the primitive 2 _n_ -th roots of unity. Let _m_ = _⌊n/τ ⌋_ and _r_ = _n_ mod _τ_ . Since<sup>�</sup><sup>_n_</sup> _j_ =1<sup>_|c_(</sup><sup>_ωj_)</sup><sup>_|_2=</sup><sup>_nτ_and</sup> 

we can bound<sup>�</sup><sup>_n_</sup> _j_ =1<sup>_|c_(</sup><sup>_ωj_)</sup><sup>_|_2</sup><sup>_·∥_</sup><sup>**s**(</sup><sup>_ωj_)</sup><sup>_∥_</sup> 2<sup>2by rearrangement: let</sup><sup>_m_=</sup><sup>_⌊n/τ⌋_be the maximum number of</sup><sup>_|c_(</sup><sup>_ωj_)</sup><sup>_|_2’s</sup> that can be _τ_<sup>2</sup> . By sorting _∥_ **s** ( _ωj_ ) _∥_ 2 in a decreasing order, 

11 

where _σ_ is a permutation for the indices, we have 

Then it reaches the maximum when the _m_ largest _∥_ **s** ( _ωj_ ) _∥_ 2<sup>2’saremultipliedwith</sup><sup>_τ_2’s,i.e.,</sup> 

#### **3.2 Discrete hyperball sampling** 

In orger to generate **y** from Figure 2 using the continuous hyperball uniform sampling from Figure 3, we apply a rounding-and-reject strategy which allows to generate rightly distributed samples. 

Fig. 5: Discrete hyperball uniform sampling 

**Lemma 7.** _Let n be the degree of R, M_ 0 _≥_ 1 _, r_<sup>_′_</sup> _, mi, N >_ 0 _. At each iteration, the algorithm from Figure 5 succeeds with probability ≥_ 1 _/M_ 0 _and the distribution of the output is U_ ( _B_ (1 _/N_ ) _R,m_ ( _r_<sup>_′_</sup> )) _if we set_ 

We note that with this rounding step, we do not need to handle the exact values of **y** , we just need enough precision to make sure the rounding is correct. The proof of this lemma can also be found in Appendix B. 

We now have all necessary ingredients in Figures 1, 2, 3, and 5 to make sure the resulting distribution of **z** is indeed uniform over the discretized hyperball. Thanks to Lemma 7 and Lemma 1, we already know the level of precision required for **y** to maintain the provable security of HAETAE. We analyze in Appendix C the required precision from a fix-point Gaussian sampler to obtain a **y** with such precision. 

#### **3.3 Signature encoding** 

To encode a signature, we will split some of its components into low and high bits. If we correctly choose the number of low bits, they will be distributed almost uniformly. The high bits on the other hand, will then follow a distribution with a very small variance and can be considerably compressed with a suitable encoding. While Huffman coding would be applied on each coordinate at a time, an arithmetic coding encodes the entire coordinates in a single number. In contrast to Huffman coding, arithmetic coding gets close to entropy also for alphabets, where the probabilities of the symbols are not powers of two. We recall a recent type 

12 

of entropy coding, named range Asymmetric Numeral systems (rANS) [Dud13], that encodes the state in a natural number and thus allows faster implementations. As a stream variant, rANS can be implemented with finite precision integer arithmetic by using renormalization. Furthermore, it is possible to avoid arithmetic operations altogether and realize high-speed implementations using lookup tables (tANS). 

**Definition 5 (Range Asymmetric Numeral System (rANS) Coding).** _Let n >_ 0 _and S ⊆_ [0 _,_ 2<sup>_n_</sup> _−_ 1] _. Let g_ : [0 _,_ 2<sup>_n_</sup> _−_ 1] _→_ Z _∩_ (0 _,_ 2<sup>_n_</sup> ] _such that_<sup>�</sup> _x∈S_<sup>_g_(</sup><sup>_x_)</sup><sup>_≤_2</sup><sup>_nandg_(</sup><sup>_x_) = 0</sup><sup>_forallx∈/S.Wedefinethefollowing:_</sup> 

- CDF : _S →_ Z _, defined as_ CDF( _s_ ) =<sup>�</sup><sup>_s_</sup> _y_<sup>_−_</sup> =0<sup>1</sup><sup>_g_(</sup><sup>_y_)</sup><sup>_._</sup> 

- symbol : Z _→ S, where_ symbol( _y_ ) _is defined as s ∈ S satisfying_ CDF( _s_ ) _≤ y <_ CDF( _s_ + 1) _._ 

- _C_ : Z _× S →_ Z _, defined as_ 

_Then, we define the rANS encoding/decoding for the set S and frequency g/_ 2<sup>_n_</sup> _as in Figure 6._ 

|Encode((_s_1_, · · · , sm_)_∈S_<sup>_m_</sup>)<br>Decode(_x ∈_Z)|
|---|
|1: _x_0 = 0<br>1: _y_0 =_x_|
|2: **for** _i_= 0_, · · · , m −_1 **do**<br>2: _i_= 0|
|3:<br>_xi_+1 =_C_(_xi, si_+1)<br>3: **while** _yi >_0 **do**<br>|
|4: Return _xm_<br>4:<br>_ti_+1 =symbol(_yi_ mod<sup>+ </sup>2<sup>_n_</sup>)<br>5:<br>_yi_+1 =_⌊yi/_2<sup>_n_</sup>_⌋·g_(_ti_+1)+(_yi_ mod<sup>+ </sup>2<sup>_n_</sup>)_−_CDF(_ti_+1)<br>6:<br>_i ←i_+ 1|
|7: _m_=_i −_1<br>8: return (_tm, · · · , t_1)_∈S_<sup>_m_</sup>|

Fig. 6: rANS encoding and decoding procedures 

**Lemma 8 (Adapted from [Dud13]).** _The rANS coding is correct, and the size of the rANS code is asymptotically equal to Shannon entropy of the symbols. That is, for any choice of_ **s** = ( _s_ 1 _, · · · , sm_ ) _∈ S_<sup>_m_</sup> _,_ Decode(Encode( **s** )) = **s** _. Moreover, for any positive x and any probability distribution p over S, it holds that_ 

_Finally, the cost of encoding the first symbol is ≤ n, i.e., for any x ∈ S, we have_ log( _C_ (0 _, s_ )) _≤ n._ 

We determine the frequency of the symbols experimentally, by executing the signature computation and collecting several million samples. Finally, we apply some rounding strategy in order to heuristically minimize the empirical entropy<sup>�</sup> _s∈S_<sup>_p_(</sup><sup>_s_) log(</sup><sup>_g_(</sup><sup>_s_)</sup><sup>_/_2</sup><sup>_n_).</sup> 

#### **3.4 Specification of** HAETAE 

Readers who are not familiar with the Fiat-Shamir with Aborts line of work may first check the uncompressed version of the scheme in Appendix A. We give the description of the signature scheme HAETAE in Figure 7 with the following building blocks: 

- Hash function _H_ gen for generating the seeds and hashing the messages, 

- Hash function _H_ for signing, returning _ρ_ , a seed for challenge sampling, 

- Extendable output function expandA for deriving **a** and **A** gen from seed **A** , 

13 

- Extendable output function expandS for deriving **s** gen and **e** gen from seedsk and countersk, 

- Extendable output function expandYbb for deriving **y** , _b_ and _b_<sup>_′_</sup> from seed _ybb_ and counter, 

The above building blocks can be implemented with symmetric primitives. Specifically, we use SHAKE256 for the hash functions and Extendable output functions, except for expandA. In all of the following sections, we let **j** = (1 _,_ 0 _, . . . ,_ 0) _∈R_<sup>_k_</sup> . The parameters _ρ_ 0 and _α_ h refer to the size of the seed and the compression factor, respectively. The parameter _β_ is the bound for _∥c_ **s** _∥_ , which will be checked by bounding 

by _nβ_<sup>2</sup> _/τ_ . The parameters _B_ , _B_<sup>_′_</sup> , and _B_<sup>_′′_</sup> refer to the radii of hyperballs. At Step 2 of the Sign algorithm, the variable _y_ 0 _∈R_ R refers to the first component of the vector **y** _∈R_<sup>_k_</sup> R<sup>+</sup><sup>_ℓ_</sup> . At Step 3 of the Sign algorithm, the vector **z** _∈R_<sup>_k_</sup> R<sup>+</sup><sup>_ℓ_</sup> is decomposed as **z** = ( **z** 1 _,_ **z** 2) with **z** 1 _∈R_<sup>_ℓ_</sup> R<sup>and</sup><sup>**z**2</sup><sup>_∈Rk_</sup> R<sup>. At Step 4 of the Verifyalgorithm,</sup> the variable _z_ ˜0 _∈R_ refers to the first component of the vector **z** ˜ _∈R_<sup>_k_+</sup><sup>_ℓ_</sup> . We assume that _q_ and _α_ h satisfy the assumptions from Lemma 5. 

Note that at Step 6 of the Verify algorithm, the division by 2 is well-defined as the operand is even. 

We also give a randomized signing of HAETAE in Figure 8. We observe that in the randomized version signing process, significant part of signing including the hyperball sampling algorithms for **y** can be performed “off-line”, i.e., before receiving a message _M_ to be signed. It holds for computations such as **w** = **A** _⌊_ **y** _⌉_ and HighBits<sup>h</sup> ( **w** ). In the “on-line” phase of signing, we can use **y** and the corresponging pre-computed components by choosing them randomly among the pre-sampled list. 

**Lemma 9.** _We borrow the notations from Figure 7. If we run_ Verify(vk _, M, σ_ ) _on the signature σ returned by_ Sign(sk _, M_ ) _for an arbitrary message M and an arbitrary key-pair_ (sk _,_ vk) _returned by_ KeyGen(1<sup>_λ_</sup> ) _, then the following relations hold:_ 

- _1)_ **w** 1 = HighBits<sup>h</sup> ( **w** ) _,_ 

- _2) w_<sup>_′_</sup> **j** = LSB( _⌊y_ 0 _⌉_ ) _·_ **j** = LSB( **w** ) = LSB( **w** _−_ 2 _⌊_ **z** 2 _⌉_ ) _._ 

_3)_ 2 _⌊_ **z** 2 _⌉−_ 2˜ **z** 2 = LowBits<sup>h</sup> ( **w** ) _−_ LSB( **w** ) _assuming it holds that B_<sup>_′_</sup> + _α_ h _/_ 4 + 1 _≤ B_<sup>_′′_</sup> _< q/_ 2 _,_ 

**Proof** _._ Let _m_ = 2( _q −_ 1) _/α_ h. Let us prove the first statement. By definition of **h** , it holds that **w** 1 = HighBits<sup>h</sup> ( **w** ) mod _m_ . However, the latter part of the equality already lies in [0 _, m −_ 1] by Lemma 5. The first part lies in the same range as we reduce mod<sup>+</sup> _m_ . Hence, the equality stands over Z too. 

We move on to the second statement. By considering only the first component of **z** = **y** + ( _−_ 1)<sup>_b_</sup> _c ·_ **s** , we obtain, modulo 2: 

This yields the result. Moreover, considering everywhere a 2 appears in the definition of **A** , we obtain that 

For the last statement, let us use the two preceding results. In particular, we note the identity 

We note that the last two elements have same parity, as the former one has the same parity as LowBits( **w** _, α_ h). By Lemma 5 their sum has infinite norm _≤ α_ h _/_ 2 + 2. Hence from its definition, it holds that 

Finally, this holds over the integers as the right-hand side has infinite norm at most 2 _B_<sup>_′_</sup> + _α_ h _/_ 2 + 2 _< q_ . _⊓⊔_ **Theorem 1 (Completeness).** _Assume that B_<sup>_′′_</sup> = _B_<sup>_′_</sup> + � _n_ ( _k_ + _ℓ_ ) _/_ 2 + _√nk ·_ ( _α_ h _/_ 4 + 1) _< q/_ 2 _. Then the signature schemes of Figures 7 and 8 are complete, i.e., for every message M and every key-pair_ (sk _,_ vk) _returned by_ KeyGen(1<sup>_λ_</sup> ) _, we have_ Verify(vk _, M,_ Sign(sk _, M_ )) = 1 _._ 

14 

KeyGen(1<sup>_λ_</sup> <u>)</u> 1: seed _←{_ 0 _,_ 1 _}_<sup>_ρ_0</sup> 2: (seed **A** _,_ seedsk _, K_ ) = _H_ gen(seed) 3: ( **a** _|_ **A** gen) _∈R_<sup>_k_</sup> _q_<sup>_×ℓ_</sup> := expandA(seed **A** ) 4: countersk = 0 5: ( **s** gen _,_ **e** gen) := expandS(seedsk _,_ countersk) 6: **b** = **a** + **A** gen _·_ **s** gen + **e** gen mod _q_ // **b** _∈R_<sup>_k_</sup> _q_ 7: ( **b** 0 _,_ **b** 1) = (LowBits<sup>vk</sup> ( **b** ) _,_ HighBits<sup>vk</sup> ( **b** )) 8: **A** = (2( **a** _−_ **b** 1) + _q_ **j** _|_ 2 **A** gen _|_ 2 **Id** _k_ ) mod 2 _q_ // **A** _∈R_<sup>_k_</sup> 2 _q_<sup>_×_(</sup><sup>_k_+</sup><sup>_ℓ_)</sup> 9: **s** = (1 _,_ **s** gen _,_ **e** gen _−_ **b** 0) // **s** _∈ Sη_<sup>_k_+</sup><sup>_ℓ_</sup> 10: **if** _f_ ( **s** ) _> nβ_<sup>2</sup> _/τ_ then go to 5 11: return sk = ( **s** _, K_ ), vk = (seed **A** _,_ **b** 1) Sign(sk _<u>, M</u>_ <u>)</u> 1: _µ_ = _H_ gen(seed **A** _,_ **b** 1 _, M_ ) 2: seed _ybb_ = _H_ gen( _K, µ_ ) 3: counter = 0 4: ( **y** _, b, b_<sup>_′_</sup> ) := expandYbb(seed _ybb,_ counter) 5: **w** = **A** _⌊_ **y** _⌉_ 6: _ρ_ = _H_ (HighBits<sup>h</sup> ( **w** ) _,_ LSB( _⌊y_ 0 _⌉_ ) _, µ_ ) 7: _c_ = SampleInBall( _ρ, τ_ ) 8: **z** = ( **z** 1 _,_ **z** 2) = **y** + ( _−_ 1)<sup>_b_</sup> _c ·_ **s** 9: **h** = HighBits<sup>h</sup> ( **w** ) _−_ HighBits<sup>h</sup> ( **w** _−_ 2 _⌊_ **z** 2 _⌉_ ) mod<sup>+2(</sup><sup>_<u>q</u>_</sup> _α_<sup>_−_</sup> h<sup>1)</sup> 10: **if** _∥_ **z** _∥_ 2 _≥ B_<sup>_′_</sup> , then counter++ and go to 4 11: **else if** _∥_ 2 **z** _−_ **y** _∥_ 2 _< B_ **and** _b_<sup>_′_</sup> = 0, then counter++ and go to 4 12: **else** return _σ_ = (Encode(HighBits<sup>_z_1</sup> ( _⌊_ **z** 1 _⌉_ )) _,_ LowBits<sup>_z_1</sup> ( _⌊_ **z** 1 _⌉_ ) _,_ Encode( **h** ) _, c_ ) Verify(vk _<u>, M, σ</u>_ = ( _x,_ **v** _<u>, h, c</u>_ <u>))</u> 1: **z** ˜1 _←_ Decode( _x_ ) _· a_ + **v** and **h**<sup>˜</sup> = Decode( _h_ ) 2: ( **a** _|_ **A** gen) = expandA(seed **A** ) 3: **A** 1 = (2( **a** _−_ 2 **b** 1) + _q_ **j** _|_ 2 **A** gen) 4: **w** 1 = **h**<sup>˜</sup> + HighBits<sup>h</sup> ( **A** 1 **z** ˜1 _− qc_ **j** ) mod<sup>+2(</sup><sup>_<u>q</u>_</sup> _α_<sup>_−_</sup> h<sup>1)</sup> 5: _w_<sup>_′_</sup> = LSB(˜ _z_ 0 _− c_ ) 6: **z** ˜2 = [ **w** 1 _· α_ h + _w_<sup>_′_</sup> **j** _−_ ( **A** 1 **z** ˜1 _− qc_ **j** )] _/_ 2 mod<sup>_±_</sup> _q_ 7: **z** ˜ = (˜ **z** 1 _,_ ˜ **z** 2) 8: _µ_ ˜ = _H_ gen(seed **A** _,_ **b** 1 _, M_ ) 9: Return ( _c_ = SampleInBall( _H_ ( **w** 1 _, w_<sup>_′_</sup> _,_ ˜ _µ_ ) _, τ_ )) _∧_ ( _∥_ **z** ˜ _∥ < B_<sup>_′′_</sup> ) 

Fig. 7: Deterministic version of HAETAE 

**Proof** _._ We use the notations of the algorithms. We will focus on the deterministic version in Fig. 7, since Fig. 8 also has almost the same proof. The first and second equations from Lemma 9 state that _ρ_ = _ρ_ ˜ and thus _c_ = SampleInBall( _ρ, τ_ ). 

On the other hand, we use the last equation from the same lemma to bound the size of **z** ˜. We have: 

15 

Sign(sk _<u>, M</u>_ <u>)</u> // can be done off-line: using vk, make a list _L_ of ( **y** _,_ **w** _,_ **w** 1) 1: **y** _← U_ ( _B_ (1 _/N_ ) _R,_ ( _k_ + _ℓ_ )( _B_ )) 2: **w** = **A** _⌊_ **y** _⌉_ 3: **w** 1 = HighBits<sup>h</sup> ( **w** ) // can be done on-line: using sk, _M_ and pre-computed ( **y** _,_ **w** _,_ **w** 1) sampled // from _L_ 4: _µ_ = _H_ gen(seed **A** _,_ **b** 1 _, M_ ) 5: _b, b_<sup>_′_</sup> _←{_ 0 _,_ 1 _}_ 6: _c_ = SampleInBall( _H_ ( **w** 1 _,_ LSB( _⌊y_ 0 _⌉_ ) _, µ_ ) _, τ_ ) 7: **z** = ( **z** 1 _,_ **z** 2) = **y** + ( _−_ 1)<sup>_b_</sup> _c ·_ **s** 8: **h** = **w** 1 _−_ HighBits<sup>h</sup> ( **w** _−_ 2 _⌊_ **z** 2 _⌉_ ) mod<sup>+2(</sup><sup>_<u>q</u>_</sup> _α_<sup>_−_</sup> h<sup>1)</sup> 9: **if** _∥_ **z** _∥_ 2 _≥ B_<sup>_′_</sup> , then 10: go to 5 with resampled ( **y** _,_ **w** _,_ **w** 1) // resample ( **y** _,_ **w** _,_ **w** 1) _←L_ 11: **else if** ( _∥_ 2 **z** _−_ **y** _∥_ 2 _< B_ ) _∧_ ( _b_<sup>_′_</sup> = 0), then 12: go to 5 with resampled ( **y** _,_ **w** _,_ **w** 1) // resample ( **y** _,_ **w** _,_ **w** 1) _←L_ 13: **else** return _σ_ = (Encode(HighBits<sup>_z_1</sup> ( _⌊_ **z** 1 _⌉_ )) _,_ LowBits<sup>_z_1</sup> ( _⌊_ **z** 1 _⌉_ ) _,_ Encode( **h** ) _, c_ ) 

Fig. 8: Randomized signing of HAETAE. On/offline signing can accelerate the signing process. Note that the signing can also be accelerated even if **y** is sampled offline alone. 

#### **3.5 Parameter sets and signature sizes** 

We propose three different parameter sets with varying security levels, where we prioritize low signature and verification key sizes over faster execution time. The parameter choices are versatile, adaptable and allow size vs. speed trade-offs at consistent security levels. For example at cost of larger signatures, a smaller repetition rate _M_ is possible and thus a faster signing process. This versatility is a notable advantage over FALCON and MITAKA. 

Like in DILITHIUM, our modulus _q_ is constant over the parameter sets and allows an optimized NTT implementation shared for all sets. With only 16-bit in size, our modulus also allows storing coefficients memory-efficiently without compression. 

The rANS encoded values _h_ and high bits of **z** 1 lead to a varying signature size. In our current implementation we opted for a fixed signature size as reported in Table 3. We evaluated the distribution empirically and determined a threshold that requires a rejection in less than 0.1% of the cases. A field of two bytes indicates the length of the encoded values, the padding can be done with arbitrary data. 

A dynamic signature size would allow an individual implementation to reject and recompute signatures until a desired size threshold is reached and still be compatible with implementations without this rejection. Due to the small variance in the distribution of the signature size, however, this would result in a distinct performance overhead, if the threshold is more than a few bytes below to the average size. Figure 9 displays the signature size distribution of 1000 executions. 

In Table 3 we compare the signature and key sizes of HAETAE, DILITHIUM, and FALCON. The verification keys in HAETAE are 20% (HAETAE-260) to 25% (HAETAE-120 and HAETAE-180) smaller, than their counterparts in DILITHIUM. The advantage of the hyperball sampling manifests itself in the signature sizes, HAETAE has 30% to 40% smaller signatures than DILITHIUM. Less relevant are the secret key sizes, that are almost half the size in HAETAE compared to DILITHIUM. A direct comparison to FALCON for the same claimed security level is only possible for the highest parameter set, FALCON-1024 has a signature of less than half the size compared to HAETAE-260, and its verification key is about 14% smaller. 

16 

|Security|120|180|260|
|---|---|---|---|
|_q_|64513|64513|64513|
|_M_|6.0|5.0|6.0|
|Key Rate|0.1|0.25|0.1|
|_β_|354.82|500.88|623.72|
|_B_|9388.97|17773.21|22343.66|
|_B_<sup>_′_</sup>|9382.26|17766.15|22334.95|
|_B_<sup>_′′_</sup>|12320.79|21365.10|24441.49|
|(_k, ℓ_)|(2,4)|(3,6)|(4,7)|
|_η_|1|1|1|
|_τ_|58|80|128|
|_α_h|512|512|256|
|_d_|1|1|0|
|Forgery||||
|BKZ block-size _b_|409 (333)|617 (512)|878 (735)|
|Classical hardness|119 (97)|180 (149)|256 (214)|
|Quantum hardness|105 (85)|158 (131)|225 (188)|
|Key-Recovery||||
|BKZ block-size _b_|428|810|988|
|Classical hardness|125|236|288|
|Quantum hardness|109|208|253|

Table 2: HAETAE parameters sets. Hardness is measured with the Core-SVP methodology. 

|**Scheme**<br>L|vl.<br>vk Si|gnature Sum Secret key|
|---|---|---|
|HAETAE-120|2<br>992|1,463 2,455<br>1,376|
|HAETAE-180|3 1,472|2,337 3,809<br>2,080|
|HAETAE-260|5 2,080|2,908 4,988<br>2,720|
|DILITHIUM-2|2 1,312|2,420 3,732<br>2,528|
|DILITHIUM-3|3 1,952|3,293 5,245<br>4,000|
|DILITHIUM-5|5 2,592|4,595 7,187<br>4,864|
|FALCON-512|1<br>897|666 1,563<br>1,281|
|FALCON-1024|5 1,792|1,280 3,072<br>2,305|

Table 3: NIST security level, signature and key sizes (bytes) of HAETAE, DILITHIUM, and FALCON. 

17 

- 0 _._ 15 0 _._ 1 

- 0 _._ 05 1 _,_ 450 1 _,_ 452 1 _,_ 454 1 _,_ 456 1 _,_ 458 1 _,_ 460 1 _,_ 462 1 _,_ 464 Signature size (bytes) 

1 _,_ 466 

- (a) HAETAE-120 

- 0 _._ 2 

- 0 _._ 15 0 _._ 1 

- 0 _._ 05 2 _,_ 328 2 _,_ 329 2 _,_ 330 2 _,_ 331 2 _,_ 332 2 _,_ 333 2 _,_ 334 2 _,_ 335 2 _,_ 336 2 _,_ 337 2 _,_ 338 2 _,_ 339 Signature size (bytes) 

2 _,_ 340 

- (b) HAETAE-180 

- 0 _._ 2 0 _._ 1 2 _,_ 899 2 _,_ 900 2 _,_ 901 2 _,_ 902 2 _,_ 903 2 _,_ 904 2 _,_ 905 2 _,_ 906 2 _,_ 907 2 _,_ 908 2 _,_ 909 Signature size (bytes) 

2 _,_ 910 

   - (c) HAETAE-260 

- Fig. 9: Signature size distribution over 1000 executions. 

18 

### **5 Security** 

_Unforgeability under Chosen Message Attacks_ (UF-CMA) is regarded as a standard security notion for digital signature schemes. The adversary is given the verification key and has access to a signing oracle to call on (adaptively) chosen messages. The adversary wins if it forges a valid signature of a new, non-queried message. _Strong Unforgeability under Chosen Message Attacks_ (SUF-CMA) is a slightly stronger security notion than UF-CMA: the adversary wins if it forges a valid signature-message pair that it did not already see. 

The concrete SUF-CMA security of HAETAE can be proven in the classical Random Oracle Model (ROM) under the standard MLWE and MSIS assumptions. However, since the proof is based on the forking lemma, the reduction is not tight, and it is not applicable in the Quantum Random Oracle Model (QROM) setting. First, using the zero-knowledge property of the underlying identification scheme, _Unforgeability under No Message Attacks_ (UF-NMA) reduces to (S)UF-CMA security, both in the ROM and the QROM. 

As pointed out in [DFPS23] and [BBD<sup>+</sup> 23], the security proofs in [AFLT16, KLS18] contain flaws. However, these works also introduce fixes. We therefore base our security proof on the fixed analyses of both [DFPS23] and [BBD<sup>+</sup> 23]. 

UF-NMA is directly related to a problem that can be viewed as a “convolution” of lattice and hash function problems. We call this problem BimodalSelfTargetMSIS. Similar to the SelfTargetMSIS described in [DKL<sup>+</sup> 18, KLS18], we can analyze the UF-CMA security based on the MLWE and BimodalSelfTargetMSIS assumptions. Note that in the ROM, MSIS reduces to BimodalSelfTargetMSIS, but the reduction is not tight and does not readily extend to quantum adversaries (it relies on the forking lemma). This said, this non-tightness and limitation to classical adversaries is not known to reflect any weakness. 

For setting parameters, we consider the hardness of MSIS and MLWE for relevant parameters. Intuitively, the MLWE assumption is used for security against key-recovery attacks, and the BimodalSelfTargetMSIS used for security against forgeries is identified to the MSIS assumption. 

#### **5.1 Security definition** 

We introduce the BimodalSelfTargetMSIS assumption and give a classical reduction from the standard MSIS assumption. BimodalSelfTargetMSIS is a variant of the SelfTargetMSIS assumption adapted to the bimodal setup. 

**Definition 6 (** BimodalSelfTargetMSIS _H,n,q,k,ℓ,β_ **).** _Suppose that H_ : _{_ 0 _,_ 1 _}_<sup>_∗_</sup> _× M →R_ 2 _is a cryptographic hash function. For positive integers q, k, ℓ, a positive real number β and the dimension n of R, we say that the advantage of an adversary A solving the search-_ BimodalSelfTargetMSIS _H,n,q,k,ℓ,β problem with respect to_ **j** _∈R_<sup>_k_</sup> 2<sup>_\ {_0</sup><sup>_}is_</sup> 

_In the ROM (resp. QROM), the adversary is given classical (resp. quantum) access to H._ 

**Theorem 2 (Classical Reduction from** MSIS **to** BimodalSelfTargetMSIS **).** _Assume that q is odd, H_ : _{_ 0 _,_ 1 _}_<sup>_∗_</sup> _× M →R_ 2 _is a cryptographic hash function modeled as a random oracle and that every polynomialtime classical algorithm has a negligible advantage against_ MSIS _n,q,k,ℓ,β. Then every polynomial-time classical algorithm has negligible advantage against_ BimodalSelfTargetMSIS _n,q,k,ℓ,β/_ 2 _._ 

**Proof** _(sketch)._ Consider a BimodalSelfTargetMSIS _n,q,k,ℓ,β/_ 2 classical algorithm _A_ that is polynomial-time and has classical access to _H_ . If _A_<sup>_|H_(</sup><sup>_·_)</sup><sup>_⟩_</sup> ( **A** ) makes _Q_ hash queries _H_ ( **w** _i, Mi_ ) for _i_ = 1 _, · · · , Q_ and outputs a solution ( **y** _, c, Mj_ ) for some _j ∈_ [ _Q_ ], then we can construct an adversary _A_<sup>_′_</sup> for MSIS _n,q,k,ℓ,β_ as follows. 

23 

The adversary _A_<sup>_′_</sup> can first rewind _A_ to the point at which the _i_ -th query was made and reprogram the hash as _H_ ( **w** _j, Mj_ ) = _c_<sup>_′_</sup> (= _c_ ). Then, with probability approximately 1 _/Q_ , algorithm _A_ will produce another solution ( **y**<sup>_′_</sup> _, c_<sup>_′_</sup> _, Mj_ ). We then have 

As _q_ is odd, we have **A** ( **y** _−_ **y**<sup>_′_</sup> ) = ( _c − c_<sup>_′_</sup> ) **j** mod 2. The fact that _c_<sup>_′_</sup> = _c_ implies that the latter is non-zero modulo 2, and hence so is **y** _−_ **y**<sup>_′_</sup> over the integers. As it also satisfies ( _−_ **b** _|_ **A** 0 _|_ **Id** _k_ ) _·_ ( **y** _−_ **y**<sup>_′_</sup> ) = 0 mod _q_ and _∥_ **y** _−_ **y**<sup>_′_</sup> _∥ < β_ , it provides a MSIS _n,q,k,ℓ,β_ solution for the matrix ( _−_ **b** _|_ **A** 0 _|_ **Id** _k_ ), where the submatrix ( _−_ **b** _|_ **A** 0) _∈R_<sup>_k_</sup> _q_<sup>_×ℓ_</sup> is uniform. _⊓⊔_ 

The above classical reduction from MSIS to BimodalSelfTargetMSIS is very similar to the reduction from MSIS to SelfTargetMSIS introduced in [DKL<sup>+</sup> 18] and is similarly non-tight. Moreover, since the reduction relies on the forking lemma; it cannot be directly extended to a quantum reduction in the QROM. 

**Security definitions.** We recall the definitions of the above security notions for digital signatures. 

**Definition 7 (Unforgeability under No Message Attacks (** UF **-** NMA **)).** _For a signature scheme S_ = (KeyGen _,_ Sign _,_ Verify) _, the advantage of a_ UF _-_ NMA _adversary A is defined as:_ 

**Definition 8 (Unforgeability under Chosen Message Attacks (** UF **-** CMA **)).** _Let S_ = (KeyGen _,_ Sign _,_ Verify) _be a signature scheme. A_ UF _-_ CMA _adversary A has access to the verification key and a signing oracle to make adaptive queries. Let the queried messages and the received signatures be_ ( _Mi, σi_ ) _for i_ = 1 _, · · · , Q. At the end of the experiment, it outputs a message-signature pair_ ( _M_<sup>_∗_</sup> _, σ_<sup>_∗_</sup> ) _. Then the advantage of A is defined as:_ 

**Definition 9 (Strong Unforgeability under Chosen Message Attacks (** SUF **-** CMA **)).** _Let S_ = (KeyGen _,_ Sign _,_ Verify) _be a signature scheme. An_ SUF _-_ CMA _adversary A has access to the verification key and a signing oracle to make adaptive queries. Let the queried messages and the received signatures be_ ( _Mi, σi_ ) _for i_ = 1 _, · · · , Q. At the end of the experiment, it outputs a message-signature pair_ ( _M_<sup>_∗_</sup> _, σ_<sup>_∗_</sup> ) _. Then the advantage of A is defined as:_ 

HAETAE achieves UF-CMA security in (Q)ROM, assuming MLWE and BimodalSelfTargetMSIS are hard. 

**Theorem 3 (** UF **-** CMA **Security of** HAETAE **in the QROM).** HAETAE _in Figure 7 is_ UF _-_ CMA _secure in the QROM._ 

**Proof** _(sketch)._ The proof relies on the analysis of [DFPS23], which reduces UF-CMA security to UF-NMA security, where an adversary is not allowed to make signing queries. This analysis requires that the commitment min-entropy is high and the underlying _Σ_ -protocol is Honest-Verifier Zero-Knowledge (HVZK). The latter is proved by providing a simulator for non-aborting transcripts and proving that the distribution of _⌊_ **y** _⌉_ has sufficiently large min-entropy. 

24 

**Commitment min-entropy.** We first claim that the underlying _Σ_ -protocol has large commitment minentropy. The underlying identification protocol has _ε bits of min-entropy_ if 

for any (pk _,_ sk) _←_ KeyGen and **y** _← U_ ( _B_ (1 _/N_ ) _R,_ ( _k_ + _ℓ_ )( _B_ )). We note that LSB( _⌊y_ 0 _⌉_ ) is a binary vector of length _n_ and is statistically close to uniform. Thus, the inner probability is (very loosely) bounded by 2<sup>_−n_</sup> regardless of the choice of (pk _,_ sk). Hence we obtain at least 256 bits of min-entropy in all of our parameter sets. 

**HVZK.** Next, we show that the underlying _Σ_ -protocol satisfies the HVKZ property. To do so, we follow the strategy from [DFPS23, Section 4.2], which studies the simulation of non-aborting transcripts and switch to computational mode for aborting ones. We propose the following simulator in Figure 10. On input a challenge _c_ , it runs _A_ (0) as defined in Figure 2 (note that we are prevented from using _B_ as the exact rejection probability is unknown), and if it fails, it samples a uniform commitment and no answer. Here, _p_ ( **z** ) is 1 _/_ 2 if _∥_ **z** _∥≤ r_ and 0 everywhere else. 

##### Sim( **A** _, c_ ) : 

1: **y** _← U_ ( _B_ (1 _/N_ ) _R,m_ ( _r_<sup>_′_</sup> )) 

2: **w** _←_ (HighBits<sup>h</sup> ( **A** _⌊_ **y** _⌉_ ) _,_ LSB( _y_ 0)) 

3: **z** _←_ **y** 4: **u** _← U_ ( _R_<sup>_k_</sup> _q_<sup>)</sup> 

5: _u_ 0 _← U_ ( _R_ 2) 

6: **w** ˜ _←_ (HighBits<sup>h</sup> (2 **u** + _q_ **j** _u_ 0) _, u_ 0) 

7: **return** ( **w** _, c,_ **z** ) with probability _p_ ( **z** ), **else** ( ˜ **w** _, c, ⊥_ ) 

#### Fig. 10: HAETAE transcript simulator 

_(i) Simulating non-aborting transcripts._ When a sample is accepted, Lemma 1 states that the simulator follows exactly the same distribution as the real aglorithm. 

_(ii) Simulating aborting transcripts._ As argued in [DFPS23, Section 4.2], in this context, we can use a a computational notion of HVZK rather than the usual statistical definition. We introduce an LWE-like assumption which states that it is hard to distinguish **w** = **A** _⌊_ **y** _⌉_ mod _q_ from a uniform element mod _q_ . This LWE assumption is unusual only in its choice of distribution for the noise and the secret. 

These two properties allow us to apply [DFPS23, Theorem 4] to reduce the SUF-CMA security to UF-NMA security. 

If one wants to avoid this assumption, it is possible to use the reduction from [BBD<sup>+</sup> 23] by using _A_ (0) as a simulator. The non-aborting transcripts produced by this simulator have statistical distance 0 with real ones. 

**Proving** UF **-** NMA **security.** Finally, we note that the UF-NMA security game is exactly the problem defined in Definition 6, up to replacing the verification key by an uniform matrix (still in HNF form), which is done under the MLWE assumption. 

#### **5.2 Cost of known attacks** 

For the concrete security analysis, we list the best known lattice attacks and consider their costs for attacking HAETAE. 

All the best known attacks rely on the Block–Korkine–Zolotarev (BKZ) lattice reduction algorithm [SE94, CN11, HPS11]. The BKZ algorithm is a lattice basis reduction algorithm that repeatedly uses a Shortest Vector Problem (SVP) solver in small-dimensional projected sublattices. The dimension _b_ of these projected 

25 

sublattices is called the block-size. BKZ with block-size _b_ hence relies on an SVP solver in dimension _b_ . The block-size drives the cost of BKZ and determines the resulting basis’s quality. It provides a quality/time trade-off: If _b_ gets larger, better quality will be guaranteed, but the time complexity for the SVP solver will exponentially increase. The time complexity of the _b_ -BKZ algorithm is the same as the SVP solver for dimension _b_ , up to polynomial factors. Hence the time complexity differs depending on the SVP solver used. The most efficient SVP algorithm uses the sieving method proposed by Becker et al. [BDGL16] which takes time _≈_ 2<sup>0</sup><sup>_._292</sup><sup>_b_+</sup><sup>_o_(</sup><sup>_b_)</sup> . The fastest known quantum variant is proposed by Chailloux and Loyer in [CL21] and takes time _≈_ 2<sup>0</sup><sup>_._257</sup><sup>_b_+</sup><sup>_o_(</sup><sup>_b_)</sup> . 

Based on the BKZ algorithm, we will follow the _core-SVP_ methodology from [ADPS16] and as in the subsequent lattice-based schemes [ABB<sup>+</sup> 19, DKL<sup>+</sup> 18, FHK<sup>+</sup> 17, DKSRV18, BDK<sup>+</sup> 18]. It is regarded as a conservative way to set security parameters. We ignore the polynomial factors and the _o_ ( _b_ ) terms in the exponents of the run-time bounds above for the time complexity of the BKZ algorithm. 

We consider the _primal attack_ and the _dual attack_ for MLWE, and the plain BKZ attack for MSIS and BimodalSelfTargetMSIS problems. We remark that any MLWE _n,q,k,ℓ,η_ instance can be viewed as an LWE _q,nk,nℓ,η_ instance, and also any MSIS _n,q,k,ℓ,β_ can be viewed as an SIS _q,nk,nℓ,β_ instance. Even though the MLWE and MSIS problems have some extra algebraic structure compared to the LWE and SIS problems, we do not currently know how to exploit it to improve the best known attacks. For this reason, we estime the concrete hardness of the MLWE and MSIS problems over the structured lattices as the concrete hardness of the corresponding LWE and SIS problems over the unstructured lattices. 

We summarize the costs of the known attacks in Table 6. In the table, the required block-sizes for BKZ and the costs of the attacks in core-SVP hardness are given, estimated by the python script we submitted to the KpqC competition with this document. It is a modification of the security estimator of Dilithium [DS20]. The parameters for MLWE and MSIS problems are chosen based on Theorems 2 and 3. The numbers in parentheses are for the SUF-CMA security of randomized HAETAE (in the case of the deterministic signature, strong and weak unforgeability are the same). All costs are rounded downwards. 

|Parameter sets|HAETAE120|HAETAE180|HAETAE260|
|---|---|---|---|
|Target security|120|180|260|
|BKZ block-size _b_ to break SIS|409 (333)|617 (512)|878 (735)|
|Classical hardness|119 (97)|180 (149)|256 (214)|
|Quantum hardness|105 (85)|158 (131)|225 (188)|
|BKZ block-size _b_ for primal attack|431|820|1001|
|Classical hardness|126|239|292|
|Quantum hardness|110|210|257|
|BKZ block-size _b_ for dual attack|428|810|988|
|Classical hardness|125|236|288|
|Quantum hardness|109|208|253|

Table 6: Core-SVP hardness for the best known attacks 

**Primal attack.** Given an LWE instance ( **A** _,_ **b** ) _∈_ Z<sup>_k_</sup> _q_<sup>_×ℓ_</sup> _×_ Z<sup>_k_</sup> _q_<sup>,wefirstdefinethelattices</sup><sup>_Λm_=</sup><sup>_{_</sup><sup>**v**</sup><sup>_∈_</sup> Z<sup>_ℓ_+</sup><sup>_m_+1</sup> : **Bv** = **0** mod _q}_ for all _m ≤ k_ , where **B** = � **A** [ _m_ ] _|_ **Id** _m|_ **b** [ _m_ ]� _∈_ Z<sup>_m_</sup> _q_<sup>_×_(</sup><sup>_ℓ_+</sup><sup>_m_+1)</sup> , **A** [ _m_ ] is the uppermost _m × ℓ_ sub-matrix of **A** and **b** [ _m_ ] is the uppermost _m_ -dimensional sub-vector of **b** . As ( **A** _,_ **b** ) _∈_ Z<sup>_k_</sup> _q_<sup>_×ℓ_</sup> _×_ Z<sup>_k_</sup> _q_<sup>isanLWEinstance,thereexist</sup><sup>**s**and</sup><sup>**e**shortsuchthat</sup><sup>**b**=</sup><sup>**As**+</sup><sup>**e**.Thisimpliesthat(</sup><sup>**s**</sup><sup>_|_</sup><sup>**e**</sup><sup>_|−_1)</sup> is a short vector of _Λm_ . The primal attack consists in running BKZ on _Λm_ to find short vectors in _Λm_ . The variable _m_ is optimized to minimize the cost of the attack. 

26 

**Dual attack.** Given an LWE instance ( **A** _,_ **b** ) _∈_ Z _q_<sup>_k×ℓ_</sup> _×_ Z<sup>_k_</sup> _q_<sup>,wefirstdefinethelattices</sup><sup>_Λ′_</sup> _m_<sup>=</sup><sup>_{_(</sup><sup>**u**</sup><sup>_,_</sup><sup>**v**)</sup><sup>_∈_</sup> Z<sup>_m_</sup> _×_ Z<sup>_ℓ_</sup> : **A**<sup>_⊤_</sup> [ _m_ ]<sup>**u**+</sup><sup>**v**=</sup><sup>**0**mod</sup><sup>_q}_forall</sup><sup>_m≤k_,where</sup><sup>**A**[</sup><sup>_m_]istheuppermost</sup><sup>_m × ℓ_sub-matrixof</sup><sup>**A**.</sup> If ( **u** _,_ **v** ) is a short vector in _Λ_<sup>_′_</sup> _m_<sup>,then</sup><sup>**u**</sup><sup>_⊤_</sup><sup>**b**=</sup><sup>**v**</sup><sup>_⊤_</sup><sup>**s**+</sup><sup>**u**</sup><sup>_⊤_</sup><sup>**e**</sup> [ _m_ ]<sup>isshortif</sup><sup>**b**=</sup><sup>**As**+</sup><sup>**e**forshortvectors</sup><sup>**s**</sup> and **e** , and is uniformly distributed modulo _q_ if **b** is uniform and independent from **A** (here **e** [ _m_ ] refers to the uppermost _m_ -dimensional sub-vector of **e** ). This provides a distinguishing attack. The dual attack consists in finding a short non-zero vector in the lattice _Λ_<sup>_′_</sup> _m_<sup>usingBKZ.Thevariable</sup><sup>_m_isoptimizedtominimizethe</sup> cost of the attack. 

SIS **attack.** To analyze the hardness of BimodalSelfTargetMSIS, we analyze the hardness of the corresponding MSIS. Intuitively, if we assume that _H_ is a cryptographic hash, then the input structure will not help find the preimage. So we can assume that _M_ is fixed. Then the problem turns into finding the preimage **x** of _c_ with respect to _H_ ( _·, M_ ) and then finding **y** satisfying **x** = **Ay** _− qc_ **j** mod 2 _q_ . Apart from the first step, if we have the preimage _c_ , then the second step will be turned into finding **y**<sup>_′_</sup> satisfying (2 **b** _|_ **A** 0 _|_ **Id** _k_ ) _·_ **y**<sup>_′_</sup> = **t** mod _q_ , for a known vector **t** over _Rq_ . Here, **y**<sup>_′_</sup> is defined as **y**<sup>_′_</sup> = (( _y_ 0 _− x_<sup>_′_</sup> 0<sup>)</sup><sup>_/_2</sup><sup>_, y_1</sup><sup>_, · · ·, yk_+</sup><sup>_ℓ−_1)</sup><sup>_⊤_and</sup><sup>**t**= 2</sup><sup>_−_1</sup><sup>_·_</sup><sup>**x**+</sup><sup>_x′_</sup> 0<sup>**b**</sup> mod _q_ , where _x_<sup>_′_</sup> 0<sup>=(</sup><sup>_x_0+</sup><sup>_c_mod2)whichactuallydecidestheLSBof</sup><sup>_y_0.Also,</sup><sup>_∥_</sup><sup>**y**</sup><sup>_′∥_2isboundedbythe</sup> same bound used for _∥_ **y** _∥_ 2. This implies that solving BimodalSelfTargetMSIS is at least as hard as solving MSIS with the same norm bound or finding the preimage of a hash as an attack perspective. However, for the hardness of BimodalSelfTargetMSIS problem, we will analyze it more conservatively, as the hardness of MSIS problem with a twice larger norm bound, taking into account the classical reduction from MSIS to BimodalSelfTargetMSIS in Theorem 2. We analyze the best known attacks for SIS problem, for both MSIS and BimodalSelfTargetMSIS problems that the unforgeability of our signature scheme relies on. 

Given an SIS instance **A** _∈_ Z<sup>_k_</sup> _q_<sup>_×ℓ_</sup> with a bound _β_ , we define the lattices _Λ_<sup>_′′_</sup> _m_<sup>=</sup><sup>_{_</sup><sup>**u**</sup><sup>_∈_Z</sup><sup>_m_:</sup><sup>**Bu**=</sup><sup>**0**mod</sup><sup>_q}_</sup> for all _m ≤ k_ + _ℓ_ , where **B** is the _k × m_ leftmost sub-matrix of ( **A** _|_ **Id** _k_ ). Then a short non-zero vector in the lattice _Λ_<sup>_′′_</sup> _m_<sup>isasolutiontotheSISproblem.Oncemore,weuseBKZandoptimizethechoiceof</sup><sup>_m_.</sup> 

Note that if _β > q_ , then there are some trivial non-zero solutions to SIS problem such as ( _q,_ 0 _, · · · ,_ 0) with _ℓ_ 2-norm _< β_ . Depending on the parameters, the security could be affected by some existing attacks [DKL<sup>+</sup> 18]. We choose the prime _q_ larger than the MSIS bound _β_ to avoid such weaknesses. 

27 

### **A Uncompressed** HAETAE 

In this appendix, we present HAETAE without its compression step. Readers who are not familiar with the Fiat-Shamir with Aborts line of work may find it easier to read this version first. It highlights the use of bimodal rejection sampling applied to the Fiat-Shamir with Aborts paradigm. 

The key generation algorithms ensures that **As** = _q_ **j** mod 2 _q_ , while also putting **A** in a “close to Hermite Normal Form”. Namely, instead of the right part of **A** being **Id** _k_ , it is 2 **Id** _k_ . This subtlety impacts the compression design, in the uncompressed version of HAETAE. 

The signature for a message _M_ consists of _c_ = _H_ ( **A** _⌊_ **y** _⌉_ mod 2 _q, M_ ) and **z** = _⌊_ **y** _⌉± c_ **s** . Sometimes, the vector **z** is rejected and the signing procedure is restarted. Note that **Az** = **A** _⌊_ **y** _⌉_ + _qc_ **j** mod 2 _q_ , independently of the sign that was chosen for _c_ **s** . The verification step then checks the consistency of the pair ( **z** _, c_ ) and the smallness of **z** . 

KeyGen(1<sup>_λ_</sup> <u>)</u> 

1: **A** gen _←R_<sup>_k_</sup> _q_<sup>_×_(</sup><sup>_ℓ−_1)</sup> and ( **s** gen _,_ **e** gen) _← Sη_<sup>_ℓ−_1</sup> _× Sη_<sup>_k_</sup> 2: **b** = **A** gen _·_ **s** gen + **e** gen _∈R_<sup>_k_</sup> _q_ 3: **A** = ( _−_ 2 **b** + _q_ **j** _|_ 2 **A** gen _|_ 2 **Id** _k_ ) 4: **s** = (1 _,_ **s**<sup>_⊤_</sup> gen<sup>_,_</sup><sup>**e**</sup><sup>_⊤_</sup> gen<sup>)</sup><sup>_⊤_</sup> 5: **if** _f_ ( **s** ) _> nβ_<sup>2</sup> _/τ_ then restart 6: return sk = ( **A** _,_ **s** ) and vk = **A** Sign(sk _<u>, M</u>_ <u>)</u> 

1: **y** _← U_ ( _B_ (1 _/N_ ) _R,_ ( _k_ + _ℓ_ )( _B_ )) 2: **w** _←_ **A** _⌊_ **y** _⌉_ 3: _c_ = _H_ ( **w** _, M_ ) _∈R_ 2 4: **z** = **y** + ( _−_ 1)<sup>_b_</sup> _c ·_ **s** for _b ← U_ ( _{_ 0 _,_ 1 _}_ ) 5: **if** _∥_ **z** _∥_ 2 _> B_<sup>_′_</sup> , then restart 6: **else if** _∥_ 2 **z** _−_ **y** _∥_ 2 _< B_ , then restart with probability 1 _/_ 2 7: return _σ_ = ( _⌊_ **z** _⌉, c_ ) Verify(vk _<u>, M, σ</u>_ = ( **z** ˜ _<u>, c</u>_ <u>))</u> 1: **w** ˜ = **Az** _− qc_ **j** mod 2 _q_ 2: return ( _c_ = _H_ ( ˜ **w** _, M_ ) ) _∧ ∥_ **z** ˜ _∥ < B_ + _~~<u>√</u>~~ n_ (2 _k_ + _ℓ_ ) <u>� �</u> 

Fig. 11: High-level description of uncompressed HAETAE 

### **B Discretizing Hyperballs** 

#### **B.1 Useful Lemma** 

We will rely on the following claim. 

**Lemma 10.** _Let n be the degree of R. Let m, N, r >_ 0 _and_ **v** _∈R_<sup>_m_</sup> _. Then the following statements hold:_ 

_1. |_ (1 _/N_ ) _R_<sup>_m_</sup> _∩BR,m_ ( _r_ ) _|_ = _|R_<sup>_m_</sup> _∩BR,m_ ( _Nr_ ) _|,_ 

_2. |R_<sup>_m_</sup> _∩BR,m_ ( _r,_ **v** <u>)</u> _<u>|</u>_ = _|R_<sup>_m_</sup> _∩BR,m_ ( _r_ ) _|,_ 

_3._ Vol( _BR,m_ ( _r −_<sup>_√_</sup> _<u>mn/</u>_ 2)) _≤|R_<sup>_m_</sup> _∩BR,m_ ( _r_ ) _| ≤_ Vol( _BR,m_ ( _r_ +<sup>_√_</sup> _<u>mn/</u>_ 2)) _._ 

**Proof** _._ For the first statement, note that we only scaled (1 _/N_ ) _R_<sup>_m_</sup> and _BR,m_ ( _r_ ) by a factor _N_ . For the second statement, note that the translation **x** _�→_ **x** _−_ **v** maps _R_<sup>_m_</sup> to _R_<sup>_m_</sup> . 

30 

We now prove the third statement. For _x ∈R_<sup>_m_</sup> , we define _T_ **x** as the hypercube of _R_<sup>_m_</sup> R<sup>centered in</sup><sup>**x**with</sup> side-length 1. Observe that the _T_ **x** ’s tile the whole space when **x** ranges over _R_<sup>_m_</sup> (the way bounderies are handled does not matter for the proof). Also, each of those tiles has volume 1. As any element in _T_ **x** is at Euclidean distance at most<sup>_√_</sup> _<u>mn/</u>_ 2 from **x** , the following inclusions hold: 

Taking the volumes gives the result. _⊓⊔_ 

### **C Fixed-Point Sampling** 

In this appendix, we explain how to sample from the discretized hyperball distribution using fixed-point arithmetic. 

We first describe the representation of numbers and operations. A fixed-point number in precision _p_ will consist in a _p_ -bit signed integer _k ∈_ Z _∩_ [ _−_ 2<sup>_p−_1</sup> _,_ 2<sup>_p−_1</sup> ) along with an implicit scaling exponent _e_ : the represented number is _x_ = _k ·_ 2<sup>_e−p_</sup> _∈_ [ _−_ 2<sup>_e−_1</sup> _,_ 2<sup>_e−_1</sup> ). The data can for example be stored in a _p_ -bit integer in two’s complement representation. The scaling exponent _e_ is not stored, it only exists on paper. For convenience, a precision _p_ fixed-point number _x_ with implicit exponent _e_ will be referred to as a ( _p, e_ )-number. 

When performing arithmetic operations on fixed-point numbers, particular care must be taken with overflows: in the analysis, we make sure that during the algorithm execution, any ( _p, e_ )-number _x_ will satisfy _|x| <_ 2<sup>_e−_1</sup> . The following assumes no overflow occurs. We can add, subtract and negate ( _p, e_ )- numbers exactly (note that we only consider the situation where the operands of those operations share the same exponent). We assume that we can multiply ( _p, e_ 0)-number _x_ 0 with a ( _p, e_ 1)-number _x_ 1 into a ( _p, e×_ )-number _x×_ as if the multiplication was exact and then rounded to a nearest representable number. Finally, we assume that we can compute an inverse square-root of a ( _p, e_ )-number _x_ into a ( _p, e_<sup>_′_</sup> )-number _y_ with possibly slightly more error than that. This is summarized as follows: 

For the sake of simplicity, we fix the precision _p_ to 128 once and for all and never perform operations with numbers of different precisions. 

#### **C.1 Gaussian samples** 

Our hyperball-uniform sampler relies on an algorithm that samples from the continuous Gaussian distribution. In our fixed-point sampling, we will make do with fixed-point approximations to samples from the continuous Gaussian distribution. Instead of sampling from the continuous Gaussian distribution and rounding, we sample from the discrete Gaussian distribution. For the discrete Gaussian sampler, we can for example rely on [BBE<sup>+</sup> 19]. 

**Lemma 11.** _Let σ >_ 0 _. Let D_ Z _,σ (resp. Dσ) be the distribution D over_ Z _(resp._ R _) such that D_ ( _k_ ) _∼_ exp( _−k_<sup>2</sup> _/_ (2 _σ_<sup>2</sup> )) _for all k ∈_ Z _(resp. k ∈_ R _). Then we have:_ 

Note that the statement could be rephrased using the smooth R´enyi divergence introduced in [DFPS22]. 

**Proof** _._ Using the discrete Gaussian tail bound from [Lyu12, Lemma 4.4], the weight of _D_ Z _,σ_ out of the interval [ _−_ 14 _· σ,_ 14 _· σ_ ] is _≤_ 2<sup>_−_140</sup> . Using the Poisson Summation Formula, we have that: 

32 

Further, for _k ∈_ Z _∩_ [ _−_ 14 _· σ,_ 14 _· σ_ ], the following inequalities hold: 

This completes the proof. 

_⊓⊔_ 

We will take _σ_ = 2<sup>124</sup> and view the sample from _D_ Z _,σ_ as a (128 _,_ 6)-number obtained as the rounding of a perfect continuous Gaussian sample. Lemma 11 implies that a signature forger for the imperfect Gaussian sampler succeeds with essentially the same probability with the ideal Gaussian sampler. 

#### **C.2 From Gaussian samples to approximate hyperball-uniforms** 

In the following, we assume that we have access to arbitrarily many statistically independent ( _p, e_ )-numbers _<u>yi</u>_ that approximate (perfect) samples _yi_ from _D_ 1 = _N_ (0 _,_ 1). We first consider the algorithm of Figure 3 with radius 1. We apply it using such _yi_ ’s and fixed-point arithmetic, with appropriately chosen implicit exponents for each step. We show that the vector **<u>y</u>** output by the approximate algorithm is close to the vector **y** output by the exact algorithm. As **y** is uniformly distributed in a hyperball, the computed vector **<u>y</u>** is an approximation to such a sample. 

We first bound the quantities involved during the computations. These bounds are for the exact quantities. To avoid overflows, we actually need them for the corresponding computed quantities. We will see later that as the numerical errors are low, the bounds still essentially hold. The bounds are probabilistic, and hold with probability extremely close to 1. 

**Lemma 12.** _Let d_ min = 6 _·_ 256+2 _and d_ max = 11 _·_ 256+2 _. The following bounds hold for all d ∈_ [ _d_ min _, d_ max] _:_ 

**Proof** _._ The first probability is 1 _−_ erf(2<sup>4</sup> _/√_ 2). The two others can be bounded the Laurent-Massart bounds for the chi-squared distribution, i.e., for all _d, t_ : 

For the last bound, we use [DFPS22, Lemma A.13]. The probability is exactly _I_ 1 _−_ 1 _/η_ 2(( _d_ + 1) _/_ 2 _,_ 1 _/_ 2) where _I_ refers to the regularized incomplete Beta function and 1 _/η_ is probabilistic magnitude upper bound. The results follow from numerical computations. _⊓⊔_ 

33 

Throughout the execution of the approximate version of the algorithm of Figure 3, we fix the precision to _p ≥_ 64. The implicit exponents vary depending on the algorithm step: the _yi_ ’s are represented by ( _p,_ 5)-numbers, their squares by ( _p,_ 13)-numbers, the squared-norm _∥_ **y** _∥_<sup>2</sup> by a ( _p,_ 13)-number, the inversenorm 1 _/∥_ **y** _∥_ by a ( _p, −_ 3)-number and the output coordinates on ( _p, −_ 1)-numbers. Assume that we have _~~|~~_ _<u>yi</u> − yi| ≤ ϵ_ 0 for all _i_ , for some _ϵ_ 0 _≥_ 2<sup>_−p_+5</sup> _/_ 2 = 2<sup>_−p_+4</sup> . To avoid overflows of _<u>yi</u>_ <u>’s,</u> it suffices that _|yi| ≤_ 2<sup>4</sup> _−_ 2<sup>_−p_+5</sup> _− ϵ_ 0. The first bound from Lemma 12 still holds for any _ϵ_ 0 _≤_ 2<sup>_−_5</sup> . We now consider the computations of the approximations _yi_<sup>2’stothe</sup><sup>_y_</sup> _i_<sup>2’s.Wehave:</sup> 

As addition is exact, we obtain: 

To avoid overflow of _∥_ **y** _∥_<sup>2</sup> and hence of the _yi_<sup>2’s,itsufficesthat</sup><sup>_∥_</sup><sup>**y**</sup><sup>_∥_2</sup><sup>_≤_212</sup><sup>_−_2</sup><sup>_−p−_13</sup><sup>_−ϵ_1.Thesecondbound</sup> from Lemma 12 still holds for any _ϵ_ 0 _≤_ 2<sup>_−_5</sup> . 

We continue with the inverse square root computation. The following holds: 

where the last inequality holds for any _ϵ_ 0 _≤_ 2<sup>_−_15</sup> . To avoid overflow of 1 _/∥_ **y** _∥_ , it suffices that 1 _/∥_ **y** _∥≤_ 2<sup>_−_4</sup> _−_ 2<sup>_−p−_3</sup> _− ϵ_ 2. The third bound from Lemma 12 still holds for any _ϵ_ 0 _≤_ 2<sup>_−_15</sup> . 

We finally evaluate the accuracy of the output vector **<u>z</u>** with respect to **z** := ( _y_ 1 _, . . . , yd_ )<sup>_⊤_</sup> _/∥_ **y** _∥_<sup>2</sup> . We have, for all _i_ : 

To avoid overflow of _<u>zi</u>_ <u>,</u> it suffices that _|zi| ≤_ 2<sup>_−_2</sup> _−_ 2<sup>_−p−_3</sup> _− ϵ_ 3. The fourth bound from Lemma 12 still holds for any _ϵ_ 0 _≤_ 2<sup>_−_20</sup> . 

Note that _ϵ_ 3 is of the order of 2<sup>14</sup> 2<sup>_−p_</sup> . This is a crude upper bound, as it assumes that errors are always in the same direction. 

#### **C.3 Using Approximate Hyperball-Uniforms** 

We consider the algorithm from Figure 5. Step 2 is performed exactly. For Step 1, we use a sample **<u>z</u>** obtained as described in the previous subsection, and multiply it by a radius _r_<sup>_′′_</sup> that we assume to be given as a 64-bit fixed-point arithmetic number. Given **<u>z</u>** <u>, this induces a change of the implicit exponent, and an additional tiny</u> error term. As _<u>zi</u>_ belongs to ( _−_ 1 _/_ 4 _,_ 1 _/_ 4) and is within _ϵ_ 4 from its corresponding _zi_ , we can prove that _r_<sup>_′′_</sup> _· zi_ belongs to ( _−r/_ 4 _, r/_ 4) and is within _r_<sup>_′′_</sup> _·_ ( _ϵ_ 4 + 2<sup>_−_63</sup> ) from its corresponding _r_<sup>_′′_</sup> _· zi_ . 

34 

Let **t** denote the rounded vector at Step 2. When rounded as in Step 2, both _r_<sup>_′′_</sup> _· zi_ and _r_<sup>_′′_</sup> _· zi_ result in the same vector **t** when the distance from _r_<sup>_′′_</sup> _· zi_ to Z _· N_ is _< N/_ 2 _−_ ( _ϵ_ 4 +2<sup>_−_63</sup> ). Let _D_ contained<sup>idealbe the distribution</sup> over Z<sup>_mn_</sup> _∩B_ ( _r_<sup>_′_</sup> ) of the rounded vector **t** at Step 2, when the whole rounding hypercube is contained in the initial hyperball. Let _D_ contained<sup>realbetheanalogousdistributionfortheapproximateversionofthealgorithm.</sup> From the discussion above, we have, for all **t** _∈_ Z<sup>_mn_</sup> : 

Here we want to use [Pre17, Lemma 3]. We also need an upper bound counterpart to the above. For usability for up to 2<sup>67</sup> samples via R´enyi divergence arguments, it suffices that the relative error _δ_ satisfies _≈_ 2<sup>_−_37</sup> . In practice, we will be using _Nr_<sup>_′_</sup> _∈_ [2<sup>25</sup> _,_ 2<sup>28</sup> ) as the sampling radius: if the sample is larger than that, we will not keep it. 

#### **C.4 Rejection Sampling with Approximate Distribution** 

In this subsection, we discuss what happens when we replace the ideal distribution used as a source for the rejection sampling by the real distribution. 

**Lemma 13.** _Let_ **v** _a vector, M >_ 0 _and P_<sup>_i_</sup> _, Q_<sup>_i_</sup> _, Q_<sup>_r_</sup> _be three probability distributions such that:_ 

_Then if we use the bimodal rejection sampling strategy for Q_<sup>_i_</sup> _and P_<sup>_i_</sup> _with Q_<sup>_r_</sup> _as a source, the resulting final distribution P_<sup>_r_</sup> _is such that_ 

**Proof** _._ Let _p_<sup>_i_</sup> and _p_<sup>_r_</sup> denote the acceptance probability of a single step of rejection sampling in the ideal and real setup, respectively. As each is related to a single random variable following either _Q_<sup>_i_</sup> or _Q_<sup>_r_</sup> and then follows the same process, it holds that 

Moreover, note that _p_<sup>_i_</sup> = 1 _/M_ . Hence, we have 

The first fraction is the ratio of the probability of the event “Get a **y** such that **y** _±_ **v** = **x** ” in the real (numerator) and ideal (denominator) setup. Hence, this ratio is bounded from above by _R∞_ ( _Q_<sup>_r_</sup> _∥Q_<sup>_i_</sup> ). Plugging the uppder bound for each fraction yields the result. _⊓⊔_ 

35