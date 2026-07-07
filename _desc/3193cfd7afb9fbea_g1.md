#### **1.1 Notations and Preliminaries** 

##### **1.1.1 Notations** 

Let _{_ 0 _,_ 1 _}_<sup>_∗_</sup> be the set of all finite bit strings, including the empty string _ε_ . For a bit string _X ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> , _|X|_ is its length in bits, and we have _|ε|_ = 0. For a bit string _X ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> and an integer _n ≥_ 1, we define a _n_ parsing operation. For _X_ = _ε_ , it is defined as ( _X_ [1] _, . . . , X_ [ _x_ ]) _← X_ , where _|X_ [ _i_ ] _|_ = _n_ for 1 _≤ i ≤ x −_ 1, 1 _≤|X_ [ _x_ ] _| ≤ n_ , and _X_ [1] _∥· · · ∥X_ [ _x_ ] = _X_ . Here _X∥Y_ is the concatenation of two bit strings _X_ and _Y_ . _n_ The number of blocks, _x_ , is the block length of _X_ . For _X_ = _ε_ , _X_ [1] _← X_ , where _X_ [1] = _ε_ . Note that _x_ = 1 and the block length of _X_ = _ε_ is 1. For a bit string _X ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> and two positive integers _n_ 1 _, n_ 2, we define a similar parsing operation. If _|X| > n_ 1, it is defined as ( _X_ [1] _, . . . , X_ [ _x_ ]) _←−−−n_ 1 _,n_ 2 _X_ , where _|X_ [1] _|_ = _n_ 1, _|X_ [2] _|_ = _· · ·_ = _|X_ [ _x −_ 1] _|_ = _n_ 2, 1 _≤|X_ [ _x_ ] _| ≤ n_ 2, and _X_ [1] _∥· · · ∥X_ [ _x_ ] = _X_ . If _|X| ≤ n_ 1, including _X_ = _ε_ , ( _X_ [1] _, . . . , X_ [ _x_ ]) _←−−−n_ 1 _,n_ 2 _X_ is equivalent to _X_ [1] _←− X_ and _x_ = 1. For a bit string _X ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> and an integer _ℓ ≤|X|_ , msb _ℓ_ ( _X_ ) denotes the first _ℓ_ bits of _X_ and lsb _ℓ_ ( _X_ ) denotes the last _ℓ_ bits of _X_ . 

For _X ∈{_ 0 _,_ 1 _}_<sup>_∗_</sup> with _|X| ≤ ℓ_ , we define a padding function as pad _ℓ_ ( _X_ ) = _X_ if _|X|_ = _ℓ_ , and pad _ℓ_ ( _X_ ) = _X∥_ 10<sup>_ℓ−_1</sup><sup>_−_(</sup><sup>_|X|_mod</sup><sup>_ℓ_)</sup> if 0 _≤|X| < ℓ_ . 

##### **1.1.3 Tweakable Even-Mansour (TEM)** 

The Even-Mansor construction is an easy way to construct a block cipher from a fixed open permutation [5]. The simplest construction is defined as _EK_ 1 _,K_ 2( _x_ ) = _K_ 2 _⊕P_ ( _x⊕K_ 1), given the open permutation _P_ , and keys _K_ 1 _, K_ 2. This is the case when there is only one iteration, and the security strength of the variant of _r_ iterations ( _Kr_ +1 _⊕ Pr_ ( _Kr−_ 1 _⊕ Pr−_ 1( _· · ·_ ( _P_ 1( _x ⊕ K_ 1)))) ) is proven to be _rn/_ ( _r_ + 1) bits [3]. The extension to tweakable block ciphers with 3 iterations and single-key _E_ ( _K, T, x_ ) = _K ⊕ T ⊕ P_ 3( _K ⊕ T ⊕ P_ 2( _K ⊕ T ⊕ P_ 1( _K ⊕ T ⊕ x_ ))) is proven to offer birthday security, i.e., _n/_ 2 bits, by Cogliati _et al._ [4]. In our design TEM-PHOTON, the needs are different: a TBC with block length 256 bits and key size 128 bits are needed, we extend the tweakable Even-Mansour construction to 4 iterations (to be conservative) with the key constructed by _K||K_ (the concatenation of the same 128-bit key twice) and the tweak by 0<sup>128</sup> _||T_ , as depicted in Fig. 1.5. We will show, by the security analysis, the probability of internal differentials (trying to exploit the fact the two halves of the key are the same) is too small to be utilized in any attack. 

##### **1.1.4 PHOTON Permutation** 

The PHOTON permutation [7] is a family of fixed-key AES-like functions used in the PHOTON hash function. It has five instances denoted _Pt_ , with state sizes being _t_ = 100 _,_ 144 _,_ 196 _,_ 256 and 288 bits respectively. In SIV-TEM-PHOTON, _P_ 256 is used and will be referred to as the PHOTON permutation for simplicity in this document. 

2 

**Algorithm** _FK_ ( _N, A, M_ ) 

1. _S ←_ 0<sup>_n_</sup> 15. **if** _|M_ [ _m_ ] _|_ = _n_ **then** 2. ( _A_ [1] _, . . . , A_ [ _a_ ]) _n←_ + _t A_ 16. _S ← S ⊕ M_ [ _m_ ] 3. **if** _|A_ [ _a_ ] _| < n_ + _t_ **then** _d ←_ 1 **else** _d ←_ 2 17. _T ← EK_<sup>4</sup><sup>_,N_(</sup><sup>_S_)</sup> 4. _A_ [ _a_ ] _←_ pad _n_ + _t_ ( _A_ [ _a_ ]) 18. **if** _n < |M_ [ _m_ ] _| < n_ + _t_ **then** 5. **for** _i_ = 1 **to** _a_ **do** 19. _M_ [ _m_ ] _←_ pad _n_ + _t_ ( _M_ [ _m_ ]) 6. _S ← S ⊕_ msb _n_ ( _A_ [ _i_ ]) 20. _S ← S ⊕_ msb _n_ ( _M_ [ _m_ ]) 7. _S ← EK_<sup>0</sup><sup>_,_lsb</sup><sup>_t_(</sup><sup>_A_[</sup><sup>_i_])</sup> ( _S_ ) 21. _S ← EK_<sup>_d,_lsb</sup><sup>_t_(</sup><sup>_M_[</sup><sup>_m_])</sup> ( _S_ ) 8. ( _M_ [1] _, . . . , M_ [ _m_ ]) _n←_ + _t M_ 22. _T ← EK_<sup>5</sup><sup>_,N_(</sup><sup>_S_)</sup> 9. **for** _i_ = 1 **to** _m −_ 1 **do** 23. **if** _|M_ [ _m_ ] _|_ = _n_ + _t_ **then** 10. _S ← S ⊕_ msb _n_ ( _M_ [ _i_ ]) 24. _S ← S ⊕_ msb _n_ ( _M_ [ _m_ ]) 11. _S ← EK_<sup>_d,_lsb</sup><sup>_t_(</sup><sup>_M_[</sup><sup>_i_])</sup> ( _S_ ) 25. _S ← EK_<sup>_d,_lsb</sup><sup>_t_(</sup><sup>_M_[</sup><sup>_m_])</sup> ( _S_ ) 12. **if** _|M_ [ _m_ ] _| < n_ **then** 26. _T ← EK_<sup>6</sup><sup>_,N_(</sup><sup>_S_)</sup> 13. _S ← S ⊕_ pad _n_ ( _M_ [ _m_ ]) 27. **return** _T_ 14. _T ← EK_<sup>3</sup><sup>_,N_(</sup><sup>_S_)</sup> 

Figure 1.3: The definitions of _F_ . 

The internal state of _P_ 256 can be seen as an 8 _×_ 8 array of 4-bit cells, where the cell located at row _i_ and column _j_ is denoted _S_ [ _i, j_ ] with 0 _≤ i, j <_ 8. _P_ 256 iterates a round function _Nr_ times and _Nr_ is 12 in the original _P_ 256 while it is 20 in SIV-TEM-PHOTON. Each round function consists of four operations (see Fig. 1.6): AddConstant[r], SubCells, ShiftRows and MixColumnSerial. 

- AddConstant[r] consists in adding fixed values to the first column of the internal state. Concretely, _S_ [ _i,_ 0] _← S_ [ _i,_ 0] _⊕IC_ [ _i_ ] _⊕RC_ [ _r_ ] for all 0 _≤ i <_ 8, where the internal constant _IC_ = [0 _,_ 1 _,_ 3 _,_ 7 _,_ 15 _,_ 14 _,_ 12 _,_ 8] and _RC_ [ _r_ ] is a 4-bit round constant for round _r_ . While _RC_ [ _r_ ] in PHOTON is generated by a 4-bit linear feedback shift register, we use a 6-bit linear feedback shift register instead for the 20-round _P_ 256 and at each round we take the least significant 4 bits as _RC_ [ _r_ ]. The update function of the 6-bit linear feedback shift register is borrowed from LED [8] and defined as follows. Let ( _rc_ 5 _, rc_ 4 _, rc_ 3 _, rc_ 2 _, rc_ 1 _, rc_ 0) be the 6 bits which are initialized to zero. At each round _r_ , ( _rc_ 5 _, rc_ 4 _, rc_ 3 _, rc_ 2 _, rc_ 1 _, rc_ 0) are shifted one position to the left with _rc_ 0 being updated with _rc_ 5 _⊕ rc_ 4 _⊕_ 1. Then, the concatenation of _rc_ 3 _, rc_ 2 _, rc_ 1 and _rc_ 0 is used as _RC_ [ _r_ ]. Explicitly, _RC_ = [0 _x_ 1 _,_ 0 _x_ 3 _,_ 0 _x_ 7 _,_ 0 _xf,_ 0 _xf,_ 0 _xe,_ 0 _xd,_ 0 _xb,_ 0 _x_ 7 _,_ 0 _xf,_ 0 _xe,_ 0 _xc,_ 0 _x_ 9 _,_ 0 _x_ 3 _,_ 0 _x_ 7 _,_ 0 _xe,_ 0 _xd,_ 0 _xa,_ 0 _x_ 5 _,_ 0 _xb_ ]. 

- AddDomain[d]: as multiple of permutations are needed in the AEAD design, AddDomain[d] xors the domain separator _d_ to all cells of the second column at each round, as depicted in Fig. 1.6. 

- SubCells is a nonlinear substitution that applies the PRESENT S-box, as shown below, to each cell of the internal state. 

_S_ = [0 _xc,_ 0 _x_ 5 _,_ 0 _x_ 6 _,_ 0 _xb,_ 0 _x_ 9 _,_ 0 _x_ 0 _,_ 0 _xa,_ 0 _xd,_ 0 _x_ 3 _,_ 0 _xe,_ 0 _xf,_ 0 _x_ 8 _,_ 0 _x_ 4 _,_ 0 _x_ 7 _,_ 0 _x_ 1 _,_ 0 _x_ 2] 

- ShiftRows is a cyclic rotation of _i_ -th row by _i_ bytes to the left, for _i_ = 0 _, ...,_ 7. 

- MixColumnSerial is a multiplication of each column with a matrix _M_ over _GF_ (2<sup>4</sup> ) by 8 times, where _GF_ (2<sup>4</sup> ) is defined by the irreducible polynomial _x_<sup>4</sup> + _x_ + 1. The matrix _M_ can be implemented in an extremely compact way and _M_<sup>8</sup> results in an Maximum Distance Separable (MDS) matrix over _GF_ (2<sup>4</sup> ). 

3 

<!-- Start of picture text -->
A [1] A [2] pad n + t ( A [ a ])<br>� � � � � �� � � �� �<br>n t<br>0 n EK 0 EK 0 EK 0 S<br><!-- End of picture text -->

<!-- Start of picture text -->
case |M [ m ] | ≤ n<br>� M � � [1] � M � [ m ��  − 1]� pad n ( M [ m ]) N<br>n t<br>S EK 1 / 2 EK 1 / 2 EK 3 / 4 T<br>case n < |M [ m ] | ≤ n  +  t<br>M [1] M [ m − 1] pad n + t ( M [ m ])<br>� � � � � �� � � �� � 0 n N<br>n t<br>S EK 1 / 2 EK 1 / 2 EK 1 / 2 EK 5 / 6 T<br>0 t M [1] 0 t M [2] 0 t M [ m ]<br>t ≤ n<br>n<br>IV EK 7 EK 7 EK 7 msb<br>C [1] C [2] C [ m ]<br><!-- End of picture text -->

Figure 1.4: The overall structure of SIV scheme. Top: Process of AD _A_ in _FK_ ( _N, A, M_ ). 2nd: Process of a plaintext _M_ in _FK_ ( _N, A, M_ ) for the case _|M_ [ _m_ ] _| ≤ n_ . 3rd: Process of _M_ in _FK_ ( _N, A, M_ ) for the case _n < |M_ [ _m_ ] _| ≤ n_ + _t_ . Bottom: _C_ = _EK_<sup>_IV_(</sup><sup>_M_).Notethat</sup><sup>_IV_=</sup><sup>_T_.</sup> 

The original _P_ 256 is defined to be the round function, 

RoundFunction[r] = MixColumnSerial _◦_ ShiftRows _◦_ SubCells _◦_ AddConstant[r] _,_ 

iterated for _r_ = 1 _, · · · ,_ 12. To incorporate the domain separator, we define _P_ 256[ _d_ ] with AddDomain[d] so the new round function becomes 

RoundFunction[r,d] = MixColumnSerial _◦_ ShiftRows _◦_ SubCells _◦_ AddDomain[d] _◦_ AddConstant[r] _._ 

4 

<!-- Start of picture text -->
K K K K K<br>n n n n n<br>∖ 2 ∖ 2 ∖ 2 ∖ 2 ∖ 2<br>⊕ ⊕ ⊕ ⊕ ⊕<br>Perm1 Perm2 Perm3 Perm4<br>⊕ ⊕ ⊕ ⊕ ⊕ ⊕ ⊕ ⊕ ⊕ ⊕<br>n n n n n n n n n n<br>∖ 2 ∖ 2 ∖ 2 ∖ 2 ∖ 2 ∖ 2 ∖ 2 ∖ 2 ∖ 2 ∖ 2<br>K T K T K T K T K T<br>Figure 1.5: Tweakable Even-Mansour construction<br>�✁✁✂✄☎✆✝✞☎✝✆ ✌✍☛✂ ✠✡✡✆ ✌✏☞✑✝✒✄✓✆ ✔☞✕✂✄✡✍✖☎✆✌ ✠✗ ☞✞✡<br>d ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎<br>d ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎<br>d ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎<br>✽ ✟✠✡✡✆ dd ✎✎ ✎✎ ✎✎ ✎✎ ✎✎ ✎✎ ✎✎ ✎✎<br>d ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎<br>d ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎<br>d ✎ ✎ ✎ ✎ ✎ ✎ ✎ ✎<br>✽ ✟✠✡✡✆ ✹ ☛☞✝✆<br>Figure 1.6: Round Function of P 256 [7], together adding of the domain separator d in the second column.<br>1.2 Specification of SIV-TEM-PHOTON Family<br>1.2.1 Specification of TEM-PHOTON<br>The 4 underlying permutations Perm Perm i  are defined as the RoundFunction[r,d] iterated for RoundFunction[r,d] iterated for iterated for  r = 5 i−− 4 ,  5 i−− 3 , · · · · · · ,  5 i<br>and i  = 1 ,  2 ,  3 ,  4, as depicted in Fig. 1.7. Here, |K|K||  =  |TT |  = 128 bits.<br>K K K K K<br>∖128 ∖128 ∖128 ∖128 ∖128<br>⊕ ⊕ ⊕ ⊕ ⊕<br>P 256 − P 256 − P 256 − P 256 −<br>5-round 5-round 5-round 5-round<br>round 1 ... 5 round 6 ... 10 round 11 ... 15 round 16 ... 20<br>⊕ ⊕ ⊕ ⊕ ⊕ ⊕ ⊕ ⊕ ⊕ ⊕<br>∖128 ∖128 ∖128 ∖128 ∖128 ∖128 ∖128 ∖128 ∖128 ∖128<br>K T K T K T K T K T<br><!-- End of picture text -->

The 4 underlying permutations Perm Perm _i_ are defined as the RoundFunction[r,d] iterated for RoundFunction[r,d] iterated for iterated for _r_ = 5 _i−−_ 4 _,_ 5 _i−−_ 3 _, · · · · · · ,_ 5 _i_ and _i_ = 1 _,_ 2 _,_ 3 _,_ 4, as depicted in Fig. 1.7. Here, _|K|K||_ = _|TT |_ = 128 bits. 

Figure 1.7: Specification of TEM-PHOTON 

##### **1.2.3 SIV-TEM-PHOTON-hash Hash Function** 

<!-- Start of picture text -->
M [1] M [2] M [3] M [4] T [1] T [2]<br>r 0 ∖ r 1 ∖ r 1 ∖ r 1 ∖ r 0 ∖ r 0 ∖<br>f [ d =0] f [ d =0] f [ d =0] f [ d =1 / 2] f [ d =0]<br>0 ∖ ∖ ∖ ∖ ∖<br>c 0 c 1 c 1 c 1 c 0<br>Absorbing Squeezing<br><!-- End of picture text -->

Figure 1.8: SIV-TEM-PHOTON-hash adopts Sponge-like construction, with initial absorbing bitrate _r_ 0, internal absorbing bitrate _r_ 1 and squeezing bitrate _r_ 0. 

**Algorithm** SpongeHash[ _<u>f</u>_<sup>[0</sup><sup>_/_1</sup><sup>_/_2]</sup> _<u>,</u>_ <u>pad</u> _<u>, r</u>_ 0 _<u>, r</u>_ 1 _<u>,</u>_ `ds` <u>](</u> _M_ <u>)</u> 

**Absorption Phase** : **Squeezing Phase** : 1. ( _M_ [1] _, . . . , M_ [ _m_ ]) _←−−−r_ 0 _,r_ 1 _M_ 13. _T_ = msb _r_ 0( _S_ ) 2. **if** _|M | ≤ r_ 0 **then** 14. **for** _i_ = 1 **to** _⌈_ `ds` _/r_ 0 _⌉−_ 1 3. _d ←_ ( _|M_ [ _m_ ] _|_ = _r_ 0)?1 : 2 15. _S ← f_<sup>[0]</sup> ( _S_ ) 4. _M_ [ _m_ ] _←_ pad _r_ 0( _M_ [ _m_ ]) 16. _T_ = _T ||_ msb _r_ 0( _S_ ) 5. **else** 17. **return** msb `ds` ( _T_ ) 6. _d ←_ ( _|M_ [ _m_ ] _|_ = _r_ 1)?1 : 2 7. _M_ [ _m_ ] _←_ pad _r_ 1( _M_ [ _m_ ]) 8. _S ←_ 0 9. **for** _i_ = 1 **to** _m −_ 1 10. _S ← S ⊕_ ( _M_ [ _i_ ] _||_ 0<sup>_|S|−|M_[</sup><sup>_i_]</sup><sup>_|_</sup> ) 11. _S_ = _f_<sup>[0]</sup> ( _S_ ) 12. _S ← f_<sup>[</sup><sup>_d_]</sup> <u>(</u> _S ⊕_ <u>(</u> _M_ <u>[</u> _m_ <u>]</u> _<u>||</u>_ 0<sup>_|S|−|M_[</sup><sup>_m_]</sup><sup>_|_</sup> <u>))</u> 

Figure 1.9: The definition of our modified Sponge construction. 

SIV-TEM-PHOTON-hash adopts the Sponge-like construction (as shown in Fig. 1.8 and 1.9). The difference with Sponge is that the initial absorbing rate and the squeezing rate are larger than the internal absorbing rate. Specifically, in SIV-TEM-PHOTON-hash, both of the initial absorbing bitrate and the squeezing bitrate are _r_ 0, whereas, the internal absorbing bitrate is _r_ 1 and output digest size is `ds` , _i.e.,_ 

The underlying permutation in SIV-TEM-PHOTON-hash is the TEM-PHOTON with both the master key _K_ and tweak _T_ set to the constant 0, and we keep the additional input _d_ , and denote the resulted permutation as _f_<sup>[</sup><sup>_d_]</sup> . _d_ = 0 is used for all other places, rather than the last call in the absorption phase. The padding rule follows the same as in the AEAD, i.e., when the last message is of full block (128 bits if _|M | ≤_ 128, 32 bits otherwise), no padding is necessary otherwise a bit string of 10<sup>_∗_</sup> is padded, and the corresponding _d_ is defined as 1 for full block, and 2 for non-full block. 

6