## **Supersingular Isogeny Key Encapsulation** 

## `https://sike.org/` 

## **September 15, 2022** 

#### **Postal address:** 

Department of Combinatorics & Optimization University of Waterloo 200 University Ave. W Waterloo, Ontario N2L 3G1 Canada 

# **Contents** 

|**0**<br>**For**|**eword and postscript**|**1**|
|---|---|---|
|**1**<br>**The**|**SIKE protocol specifcation**|**2**|
|1.1|Mathematical Foundations . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>2|
|1.2|Data types and conversions . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>8|
|1.3|Detailed protocol specifcation . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>12|
|1.4|Symmetric primitives . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>20|
|1.5|Public key compression . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>20|
|1.6|Parameter sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>21|
|**2**<br>**Det**|**ailed performance analysis**|**34**|
|2.1|Reference implementation<br>. . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>35|
|2.2|Optimized and x64 assembly implementations . . . . . . . . . . . .|. . . . . . . . . . . .<br>36|
|2.3|Compressed SIKE implementation . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>39|
|2.4|64-bit ARM assembly implementation . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>40|
|2.5|ARM Cortex-M4 assembly implementation . . . . . . . . . . . . .|. . . . . . . . . . . .<br>41|
|2.6|VHDL hardware implementation . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>43|
|**3**<br>**Kno**|**wn Answer Test values**|**45**|
|**4**<br>**Exp**|**ected security strength**|**46**|
|4.1|Security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>46|
|4.2|Other attacks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>47|
|4.3|Security proofs<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . . . . . . . . . . .<br>48|

|**5**|**Analysis with respect to known attacks**|**50**|
|---|---|---|
||5.1<br>Classical security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>50|
||5.2<br>Quantum security . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>51|
||5.3<br>Side-channel attacks<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>52|
|**6**|**Advantages and Limitations**|**55**|
|**A **|**Explicit algorithms for**`isogen`ℓ**and**`isoex`ℓ**: Optimized implementation**|**62**|
|**B**|**Explicit algorithms for**`isogen`ℓ**and**`isoex`ℓ**: Reference implementation**|**73**|
|**C **|**Explicit algorithms for compressed SIKE: Optimized implementation**|**84**|
|**D **|**Computing optimized strategies for fast isogeny and discrete logarithm computations**|**95**|
||D.1<br>Strategies for`SIKEp434`<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>96|
||D.2<br>Strategies for`SIKEp503`<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>97|
||D.3<br>Strategies for`SIKEp610`<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. .<br>98|
||D.4<br>Strategies for`SIKEp751`<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .|. . 100|
|**E**|**Changes made in the 2nd round**|**102**|
|**F**|**Changes made in the 3rd round**|**103**|
|**G **|**Notation**|**104**|

# **Chapter 0** 

# **Chapter 1** 

# **The SIKE protocol specification** 

This document presents a detailed description of the Supersingular Isogeny Key Encapsulation (SIKE) protocol. This protocol is based on a key-exchange construction, commonly referred to as Supersingular Isogeny Diffie-Hellman (SIDH), which was introduced by Jao and De Feo in 2011 [26], and subsequently improved in various ways by numerous authors [9, 10, 13, 34]. This specification gives an overview of the mathematical foundations necessary for SIKE, as well as a complete description of all the algorithms and data type conversions used in implementing SIKE, and a brief discussion of the security of the protocol. 

For a summary of the notation used in this document, see Appendix G. 

## **1.1 Mathematical Foundations** 

Use of the supersingular isogeny key encapsulation (SIKE) protocol described in this document involves arithmetic operations of elliptic curves over finite fields. This section provides the mathematical concepts and data type conversions used in the description of the SIKE protocol. 

### **1.1.1 Finite Fields** 

A finite field consists of a finite set of elements closed under the operations of addition and multiplication defined over the set. There is an additive identity element (0) and a multiplicative identity element (1). Every element has a unique additive inverse, and every non-zero element has a unique multiplicative inverse. 

For a positive integer _q_ , there exists a finite field of _q_ elements if and only if _q_ is a power of a prime _p_ . Further, there is a unique representative, up to isomorphism, of every finite field of _q_ elements. We denote the finite field of _q_ elements by F _q_ . If F _q_ is a finite field with _q_ = _p_<sup>_t_</sup> for prime _p_ , we define the characteristic char(F _q_ ) of F _q_ to be _p_ . 

The finite fields used in supersingular isogeny cryptography are quadratic extension fields of a prime field F _p_ , with _p_ = 2<sup>_e_2</sup> 3<sup>_e_3</sup> − 1, where _e_ 2 and _e_ 3 are fixed public parameters, and where the extension field is formed as F _p_ 2 = F _p_ ( _i_ ) with _i_<sup>2</sup> + 1 = 0. 

When abstraction is useful we will refer to ℓ, _m_ ∈{2, 3}, such that ℓ � _m_ . 

2 

### **1.1.2 The Finite Field** F _p_ 

The elements of F _p_ are represented by the integers: 

with the field operations defined as follows: 

- Addition: If _a_ , _b_ ∈ F _p_ , then _a_ + _b_ = _r_ in F _p_ , where _r_ ∈ [0, _p_ − 1] is the remainder of _a_ + _b_ divided by _p_ , also known as addition modulo _p_ . 

- Multiplication: If _a_ , _b_ ∈ F _p_ , then _ab_ = _s_ in F _p_ , where _s_ ∈ [0, _p_ − 1] is the remainder of _ab_ divided by _p_ , also known as multiplication modulo _p_ . 

- Additive Inverse: If _a_ ∈ F _p_ , the unique solution in [0, _p_ − 1] to the equation _a_ + _x_ ≡ 0 (mod _p_ ) is the additive inverse (− _a_ ). 

- Multiplicative Inversion: If _a_ ∈ F _p_ , _a_ � 0, the unique solution in [0, _p_ − 1] to the equation _ax_ ≡ 1 (mod _p_ ) is the multiplicative inverse _a_<sup>−1</sup> . 

We make the convention that _a_ − _b_ = _a_ + (− _b_ ), and _a_ / _b_ = _a_ · _b_<sup>−1</sup> in the field F _p_ . 

### **1.1.3 The Finite Field** F 2 _p_ 

The elements of F _p_ 2 are represented by _s_ = _s_ 0 + _s_ 1 · _i_ , where _s_ 0, _s_ 1 ∈ F _p_ , with the field operations defined as follows: 

- Addition: If _a_ , _b_ ∈ F _p_ 2, then ( _a_ 0 + _a_ 1 · _i_ ) + ( _b_ 0 + _b_ 1 · _i_ ) = ( _a_ 0 + _b_ 0) + ( _a_ 1 + _b_ 1) · _i_ in F _p_ 2, where the additions ( _ai_ + _bi_ ) take place in F _p_ . 

- Multiplication: If _a_ , _b_ ∈ F _p_ 2, then ( _a_ 0 + _a_ 1 · _i_ )( _b_ 0 + _b_ 1 · _i_ ) = ( _a_ 0 _b_ 0 − _a_ 1 _b_ 1) + ( _a_ 0 _b_ 1 + _a_ 1 _b_ 0) · _i_ in F _p_ 2, where the addition, additive inverse and multiplication operations take place in F _p_ . 

- Additive Inverse: If _a_ ∈ F _p_ 2, then (− _a_ 0) + (− _a_ 1) · _i_ ∈ F _p_ 2 is the additive inverse (− _a_ ), where the values (− _ai_ ) are computed in the field F _p_ . 

- Multiplicative Inversion: If _a_ ∈ F _p_ , _a_ � 0, then ( _a_ 0( _a_<sup>2</sup> 0<sup>+</sup><sup>_a_2</sup> 1<sup>)−1 + ((−</sup><sup>_a_1)(</sup><sup>_a_2</sup> 0<sup>+</sup><sup>_a_2</sup> 1<sup>)−1) ·</sup><sup>_i_)∈F</sup><sup>_p_2is the</sup> multiplicative inverse _a_<sup>−1</sup> , where the operations take place in F _p_ . 

- Square root: If there exists an _r_ = α + β · _i_ ∈ F _p_ 2 with α, β ∈ F _p_ such that _r_<sup>2</sup> = _s_ , then we define √ _<u>s</u>_ = _r_ if either α � 0 is an even integer or α = 0 and β is an even integer, otherwise<sup>~~√~~</sup> _<u>s</u>_ = − _r_ . 

3 

### **1.1.4 Montgomery curves** 

A Montgomery curve is a special form of an elliptic curve. Let _A_ , _B_ ∈ F _q_ be field elements satisfying _B_ ( _A_<sup>2</sup> − 4) � 0 in F _q_ (where char(F _q_ ) � 2). A Montgomery curve _EA_ , _B_ defined over F _q_ , denoted _EA_ , _B_ /F _q_ , is defined to be the set of points _P_ = ( _x_ , _y_ ) of solutions in F _q_ to the equation 

_By_<sup>2</sup> = _x_<sup>3</sup> + _Ax_<sup>2</sup> + _x_ , 

together with an extra point O, called the point at infinity. For convenience, we may refer to the curve as: 

- _EA_ , _B_ when the underlying field F _q_ is either fixed by context, or unspecified, 

- _E_ (F _q_ ) when the curve parameters are either fixed by context, or unspecified, 

- _E_ when both the field and the curve parameters _A_ , _B_ are either fixed by context, or unspecified. 

- _EA_ when the underlying field F _q_ is fixed by context, or unspecified, and when _B_ (which specifies the quadratic twist) is presumed to either be _B_ = 1 or irrelevant. 

At times it will be convenient to refer to the _x_ -coordinate of a point _P_ . We will use the notation _xP_ to refer to the _x_ -coordinate of _P_ , and analogously _yP_ to refer to the _y_ -coordinate. 

The set of points of _E_ together with the point at infinity form a finite abelian group under a point addition rule. The order of an elliptic curve _E_ over a finite field F _q_ , denoted # _E_ (F _q_ ), is the number of points in _E_ including O. 

Oftentimes, Montgomery curves are indicated by _MA_ , _B_ , but we will use the notation _EA_ , _B_ instead. 

### **1.1.5 Point addition** 

Given two points _P_ = ( _xP_ , _yP_ ) and _Q_ = ( _xQ_ , _yQ_ ) such that _P_ � ± _Q_ on a Montgomery curve _EA_ , _B_ over a finite field F _q_ , we can compute _R_ = _P_ + _Q_ as 

and 

where _R_ = ( _xR_ , _yR_ ) and λ = ( _yP_ − _yQ_ )/( _xP_ − _xQ_ ). 

We can add a point to itself multiple times, say _k_ times, as follows: _P_ + _P_ + . . . + _P_ = [ _k_ ] _P_ . 

The order ord( _P_ ) of a point _P_ is the smallest positive integer _n_ such that [ _n_ ] _P_ = O (the point at infinity). 

### **1.1.6 Point doubling** 

Let _P_ = ( _xP_ , _yP_ ) ∈ _EA_ , _B_ be a point whose order does not divide 2. Then [2] _P_ = ( _x_ [2] _P_ , _y_ [2] _P_ ) ∈ _EA_ , _B_ can be computed as 

Observe that _x_ [2] _P_ only depends on _xP_ and _A_ . The optimized, inversion-free algorithm that takes advantage of this is given in Algorithm 3 of Appendix A. 

4 

### **1.1.7 Point tripling** 

Let _P_ = ( _xP_ , _yP_ ) ∈ _EA_ , _B_ be a point whose order does not divide 3. Then [3] _P_ = ( _x_ [3] _P_ , _y_ [3] _P_ ) ∈ _EA_ , _B_ can be computed as 

and 

Again we see that _x_ [3] _P_ only depends on _xP_ and _A_ . The algorithm that takes advantage of this is given in Algorithm 6 of Appendix A. 

### **1.1.8 Additional properties of elliptic curves** 

For any group _G_ , and a set of elements { _P_ 1, _P_ 2, . . . , _Pt_ } ⊆ _G_ we can define the subgroup ⟨ _P_ 1, _P_ 2, . . . _Pt_ ⟩ generated by this set to be the smallest subgroup of _G_ containing the elements _P_ 1, _P_ 2, . . . , _Pt_ . For an abelian group _G_ , we say a set of elements { _P_ 1, _P_ 2, . . . _Pt_ } ⊆ _G_ form a basis of _G_ if every element _P_ of _G_ admits a unique expression of the form 

where 0 ≤ _ki_ < ord( _Pi_ ) for all _i_ . Analogously, we say a set { _P_ 1, _P_ 2, . . . , _Pt_ } ⊆ _H_ forms a basis of a subgroup _H_ ⊆ _G_ when all elements of the subgroup _H_ admit a unique expression as above. The Weil pairing [39] can assist in determining whether or not a set forms a basis, since for _n_ = ord( _P_ ) = ord( _Q_ ), the order- _n_ Weil pairing _en_ has the property that ord( _en_ ( _P_ , _Q_ )) = _n_ if and only if ⟨ _P_ ⟩∩⟨ _Q_ ⟩ = {O}. 

For a positive integer _m_ , we define the set _E_ [ _m_ ] of _m_ -torsion elements of an elliptic curve _E_ (F _q_ ) to be the set of points in _E_ (F<sup>¯</sup> _q_ ) such that [ _m_ ] _P_ = O. 

An elliptic curve _E_ (F _q_ ) over a field of characteristic _p_ is called supersingular if _p_ | ( _q_ + 1 − # _E_ (F _q_ )), and ordinary otherwise. 

The _j_ -invariant of the elliptic curve _EA_ , _B_ is computed as 

The _j_ -invariant of an elliptic curve over a field F _q_ is unique up to isomorphism of the elliptic curve. The SIKE protocol defines a shared secret as a _j_ -invariant of an elliptic curve. 

5 

### **1.1.9 Isogenies** 

Let _E_ 1 and _E_ 2 be elliptic curves over a finite field F _q_ . An isogeny ϕ : _E_ 1 → _E_ 2 is a non-constant rational map defined over F _q_ which is also a group homomorphism from _E_ 1(F _q_ ) to _E_ 2(F _q_ ). If such a map exists we say _E_ 1 is isogenous to _E_ 2, and two curves _E_ 1 and _E_ 2 over F _q_ are isogenous if and only if # _E_ 1(F _q_ ) = # _E_ 2(F _q_ ). 

An isogeny ϕ can be expressed in terms of two rational maps _f_ and _g_ over F _q_ such that ϕ(( _x_ , _y_ )) = ( _f_ ( _x_ ), _y_ · _g_ ( _x_ )). We can write _f_ ( _x_ ) = _p_ ( _x_ )/ _q_ ( _x_ ) with polynomials _p_ ( _x_ ) and _q_ ( _x_ ) over F _q_ that do not have a common factor, and similarly for _g_ ( _x_ ). We define the degree deg(ϕ) of the isogeny to be max{deg( _p_ ( _x_ )), deg( _q_ ( _x_ ))}, where _p_ ( _x_ ) and _q_ ( _x_ ) are as above. It is often convenient to do isogeny calculations using only the _f_ ( _x_ ) component of the isogeny. 

Given an isogeny ϕ : _E_ 1 → _E_ 2 we define the kernel of ϕ as follows: 

For any finite subgroup _H_ of _E_ (F _q_ ), there is a unique isogeny (up to isomorphism) ϕ : _E_ → _E_<sup>′</sup> such that ker(ϕ) = _H_ and deg(ϕ) = | _H_ |, where | _H_ | denotes the cardinality of _H_ . In this case, we denote by _E_ / _H_ the curve _E_<sup>′</sup> . Given a subgroup _H_ ⊆ _E_ (F _q_ ), Vélu’s formula [58] can be used to find the isogeny ϕ and isogenous curve _E_ / _H_ . Vélu’s formula is computationally impractical for arbitrary subgroups. SIKE uses isogenies over subgroups that are powers of 2, 3 and 4. 

**2-isogenies** Let ( _x_ 2, _y_ 2) ∈ _EA_ , _B_ be a point of order 2 with _x_ 2 � ±0 and let ϕ2 : _EA_ , _B_ → _EA_ ′, _B_ ′ be the unique (up to isomorphism) 2-isogeny with kernel ⟨( _x_ 2, _y_ 2)⟩. Then _EA_ ′, _B_ ′ can be computed as 

Observe that _A_<sup>′</sup> only depends on _x_ 2. The inversion-free algorithm that takes advantage of this is given in Algorithm 11 of Appendix A . 

If _P_ = ( _xP_ , _yP_ ) is any point on _EA_ , _B_ that is not in ker(ϕ2), then ϕ2 : ( _xP_ , _yP_ ) �→ ( _x_ ϕ2( _P_ ), _y_ ϕ2( _P_ )), and this can be computed as 

and 

Observe that _x_ ϕ2( _P_ ) only depends on _xP_ and _x_ 2. The inversion-free algorithm that takes advantage of this is given in Algorithm 12 of Appendix A. 

6 

**4-isogenies** Let ( _x_ 4, _y_ 4) ∈ _EA_ , _B_ be a point of order 4 with _x_ 4 � ±1 and let ϕ4 : _EA_ , _B_ → _EA_ ′, _B_ ′ be the unique (up to isomorphism) 4-isogeny with kernel ⟨( _x_ 4, _y_ 4)⟩. Then _EA_ ′, _B_ ′ can be computed as 

Observe that _A_<sup>′</sup> only depends on _x_ 4. The inversion-free algorithm that takes advantage of this is given in Algorithm 13 of Appendix A . 

If _P_ = ( _xP_ , _yP_ ) is any point on _EA_ , _B_ that is not in ker(ϕ4), then ϕ4 : ( _xP_ , _yP_ ) �→ ( _x_ ϕ4( _P_ ), _y_ ϕ4( _P_ )), and this can be computed as 

and 

Observe that _x_ ϕ4( _P_ ) only depends on _xP_ and _x_ 4. The inversion-free algorithm that takes advantage of this is given in Algorithm 14 of Appendix A. 

**3-isogenies** Let ( _x_ 3, _y_ 3) ∈ _EA_ , _B_ be a point of order 3 and let ϕ3 : _EA_ , _B_ → _EA_ ′, _B_ ′ be the unique (up to isomorphism) 3-isogeny with kernel ⟨( _x_ 3, _y_ 3)⟩. Then _EA_ ′, _B_ ′ can be computed as 

The new coefficient _A_<sup>′</sup> only depends on _A_ and _x_ 3. The inversion-free algorithm that takes advantage of this is given in Algorithm 15 of Appendix A. 

If _P_ = ( _xP_ , _yP_ ) is any point on _EA_ , _B_ that is not in ker(ϕ3), then ϕ3 : ( _xP_ , _yP_ ) �→ ( _x_ ϕ3( _P_ ), _y_ ϕ3( _P_ )), and this can be computed as 

Observe that _x_ ϕ3( _P_ ) only depends on _xP_ and _x_ 3. The inversion-free algorithm that takes advantage of this is given in Algorithm 16 of Appendix A. 

The SIKE protocol defines secret keys from two separate key spaces, K2 and K3 (cf. §1.3.9). A secret key sk defines a subgroup _H_ of _E_ (F _q_ ), which in turn defines an isogeny ϕsk : _E_ → _E_ / _H_ . The public key is determined by the isogeny ϕsk and points _P_ , _Q_ ∈ _E_ (F _q_ ) (which are fixed globally as public parameters and do not depend on sk). More specifically, the public key corresponding to sk is determined by { _E_ / _H_ , ϕsk( _P_ ), ϕsk( _Q_ )}. The points _P_ and _Q_ are chosen so that { _P_ , _Q_ } forms a basis for _E_ [ℓ<sup>_e_ℓ</sup> ] . In our implementations, for efficiency reasons we represent a public key as a triplet of field elements, namely the three _x_ -coordinates { _x_ ϕsk( _P_ ), _x_ ϕsk( _Q_ ), _x_ ϕsk( _P_ − _Q_ )} of three points under the isogeny. It is possible to convert between representations using the methods given in [10]. For example, the Montgomery curve coefficient 

7 

_A_ of _E_ / _H_ can be recovered by the three _x_ -coordinates of a public key { _x_ ϕsk( _P_ ), _x_ ϕsk( _Q_ ), _x_ ϕsk( _P_ − _Q_ )} using the equation 

Similarly, the points ϕsk( _P_ ) and ϕsk( _Q_ ) can be recovered (up to simultaneous sign) from _x_ ϕsk( _P_ ) and _x_ ϕsk( _Q_ ) using the formula 

and 

and if 

then set _y_ ϕsk( _Q_ ) = − _y_ ϕsk( _Q_ ). 

## **1.2 Data types and conversions** 

The SIKE protocol specified in this document involves operations using several data types. This section lists the different data types and describes how to convert one data type to another. 

### **1.2.1 Curve-from-public-key computation -** `cfpk` 

An elliptic curve from a public key should be computed as described in this section. Informally, three field elements are interpreted as _x_ -coordinates to three points _P_ , _Q_ , and _P_ − _Q_ , from which a curve _E_<sup>′</sup> is computed and returned. 

**Input:** Three field elements ( _xP_ , _xQ_ , _xR_ ) of F _p_ 2. 

**Output:** A elliptic curve _E_<sup>′</sup> over F _p_ 2 or FAIL. 

**Action:** Convert ( _xP_ , _xQ_ , _xR_ ) to an elliptic curve as follows: 

1. For _i_ ∈ [ _P_ , _Q_ , _R_ ] verify _xi_ � 0 or return FAIL. 

2. Compute _A_ =<sup><u>(1−</u></sup><sup>_xPxQ_</sup> 4<sup>−</sup> _xP_<sup>_x_</sup> _x_<sup>_P_</sup> _Q_<sup>_xR_</sup> _xR_<sup>−</sup><sup>_xQxR_</sup><sup><u>)2</u></sup> − _xP_ − _xQ_ − _xR_ in F _p_ 2 . 

3. Set _E_<sup>′</sup> = _EA_ . 

4. Output _E_<sup>′</sup> . 

8 

### **1.2.2 Octet-string-to-integer conversion -** `ostoi` 

Octet strings should be converted to integers as described in this section. This routine takes as input an octet string _M_ of length mlen and interprets the octet string in base 2<sup>8</sup> of an integer. 

**Input:** An octet string _M_ of length mlen. 

**Output:** An integer _a_ . 

**Action:** Convert _M_ to an integer _a_ as follows: 

1. Parse _M_ = _M_ 0 _M_ 1 . . . _M_ mlen −1 into mlen-many octets. 

2. Interpret each octet _Mi_ as an integer in [0, 255]. 

3. Compute _a_ =<sup>�mlen</sup> _i_ =0<sup>−1</sup> _Mi_ 2<sup>8</sup><sup>_i_</sup> . 

4. Output _a_ . 

### **1.2.3 Octet-string-to-field-** _p_ **-element conversion -** `ostofp` 

Octet strings should be converted to elements of F _p_ as described in this section. This routine takes as input an octet string _M_ of length _Np_ = ⌈(log2 _p_ )/8⌉ and converts it to an integer, verifying that the integer is in the range [0, _p_ − 1]. 

**Input:** An octet string _M_ of length _Np_ . 

**Output:** A field element _a_ ∈ F _p_ or FAIL. 

**Action:** Convert the octet string _M_ to field element as follows: 

1. Convert _M_ to an integer _a_ (cf. §1.2.2) using _M_ and _Np_ as inputs. 

2. If _a_ � [0, _p_ − 1] output FAIL, otherwise output _a_ . 

### **1.2.4 Octet-string-to-field-** _p_<sup>2</sup> **-element conversion -** `ostofp2` 

Octet strings should be converted to elements of F _p_ 2 as described in this section. This routine takes as input an octet string _M_ of length 2 _Np_ , where _Np_ = ⌈(log2 _p_ )/8⌉ and converts it to two integers, verifying each is in the range [0, _p_ − 1], and interprets the results as an element of F _p_ 2. 

**Input:** An octet string _M_ of length 2 _Np_ . 

**Output:** A field element _a_ ∈ F _p_ 2 or FAIL. 

**Action:** Convert the octet string _M_ to field element as follows: 

1. Parse _M_ = _M_ 0 _M_ 1 where each _Mi_ is of length _Np_ . 

2. For _i_ ∈ [0, 1] convert _Mi_ to a field element _ai_ (cf. §1.2.3) or output FAIL. 

3. Form _a_ = _a_ 0 + _a_ 1 · _i_ , and return _a_ . 

9 

### **1.2.5 Octet-string-to-public-key conversion -** `ostopk` 

Octet strings should be converted to public keys as described in this section. This routine takes as input and octet string _M_ of length 6 _Np_ , where _Np_ = ⌈(log2 _p_ )/8⌉ and converts it to three field elements of F _p_ 2, interpreted as _x_ -coordinates of three points _P_ , _Q_ , and _R_ . 

**Input:** An octet string _M_ of length 6 _Np_ . 

**Output:** A public key ( _xP_ , _xQ_ , _xR_ ) or FAIL. 

**Action:** Convert the octet string _M_ to a public key as follows: 

1. Parse _M_ = _M_ 1 _M_ 2 _M_ 3, where each _Mi_ is an octet string of length 2 _Np_ . 

2. For _i_ ∈ [1, 2, 3] convert _Mi_ to a field element _xi_ (cf. §1.2.4) or return FAIL. 

3. Output pkℓ = ( _x_ 1, _x_ 2, _x_ 3). 

### **1.2.6 Integer-to-octet-string conversion -** `itoos` 

Integers should be converted to octet strings as described in this section. This routine takes as input an integer _a_ and an octet length mlen is provided as input. The routine will represent _a_ in base 2<sup>8</sup> and convert that to an octet string. A restriction is that 2<sup>8·mlen</sup> > _a_ . 

- **Input:** A non-negative integer _a_ together with a desired length mlen of the octet string, such that 2<sup>8·mlen</sup> > _a_ . 

**Output:** An octet string _M_ of length mlen octets. 

**Actions:** Convert _a_ into an mlen-length octet string as follows: 

1. Convert _a_ = _a_ mlen −12<sup>8(mlen −1)</sup> + _a_ mlen −22<sup>8(mlen −2)</sup> + · · · + _a_ 12<sup>8</sup> + _a_ 0 represented in base 2<sup>8</sup> . 

2. For 0 ≤ _i_ < mlen, set _Mi_ = _ai_ . 

3. Form _M_ = _M_ 0 _M_ 1 . . . _M_ mlen −1. 

4. Output _M_ . 

### **1.2.7 Field-** _p_ **-to-octet-string conversion -** `fptoos` 

Field elements of F _p_ should be converted to octet strings as described in this section. Informally the idea is that an element of F _p_ is an integer in [0, _p_ − 1] and is converted to a fixed length octet string. 

**Input:** An element _a_ ∈ F _p_ . 

**Output:** An octet string _M_ of length _Np_ = ⌈(log2 _p_ )/8⌉. 

**Actions:** Compute the octet string as follows: 

1. Since _a_ is an integer in the interval [0, _p_ − 1], convert _a_ to an octet string _M_ (cf. §1.2.6), with inputs _a_ and _Np_ . 

2. Output _M_ . 

10 

### **1.2.8 Field-** _p_<sup>2</sup> **-to-octet-string conversion -** `fp2toos` 

Field elements F _p_ 2 should be converted to octet strings as described in this section. Informally the idea is that the elements of F _p_ 2 consists of two field elements of F _p_ , each of these are converted to an octet string and the result is concatenated. 

**Input:** An element _a_ ∈ F _p_ 2. 

**Output:** An octet string _M_ of length 2 · _Np_ where _Np_ = ⌈(log2 _p_ )/8⌉. 

**Actions:** Compute the octet string as follows: 

1. Since _a_ ∈ F _p_ 2, we can represent it as _a_ = _a_ 0 + _a_ 1 · _i_ where _ai_ ∈ F _p_ . 

2. Convert _ai_ into an octet string _Mi_ of the length _Np_ (cf. §1.2.7). 

3. Form _M_ = _M_ 0 _M_ 1. 

4. Output _M_ . 

### **1.2.9 Public-key-to-octet-string conversion -** `pktoos` 

Public keys ( _xP_ , _xQ_ , _xR_ ) should be converted to octet strings as described in this section. This routine converts each _x_ -coordinate as an octet string encoding of a field elements and concatenates them to form the output octet string. 

In portions of the spec we will refer to a public key pk in octet string format without explicitly referencing the public-key-to-octet-string conversion. 

**Input:** A public key ( _xP_ , _xQ_ , _xR_ ) over a finite field F _p_ 2 

**Output:** An octet string _M_ of length 6 · _Np_ where _Np_ = ⌈(log2 _p_ )/8⌉ 

**Actions:** Compute the octet string as follows: 

1. Convert _xP_ , _xQ_ , _xR_ into the octet strings _M_ 1, _M_ 2, _M_ 3 respectively, each of length 2 _Np_ (cf. §1.2.6). 

2. Form _M_ = _M_ 1 _M_ 2 _M_ 3. 

3. Output _M_ . 

### **1.2.10 Compressed-public-key-to-octet-string conversion -** `cpktoos` 

Compressed public keys ( _bit_ , _bitEll_ 1, _bitEll_ 2, _t_ 1, _t_ 2, _t_ 3, _A_ , _s_ , _r_ ) ∈ Z<sup>3</sup> 2<sup>×(Zℓ</sup><sup>_e_)3×F</sup><sup>_p_2 ×Z2</sup> 2<sup>8 should be converted to</sup> octet strings as described in this section. This routine converts each component as an octet string encoding and concatenates them to form the output octet string. 

In portions of the spec we will refer to a public key pk_comp in octet string format without explicitly referencing the compressed-public-key-to-octet-string conversion. 

11 

- **Input:** A compressed public key ( _bit_ , _bitEll_ 1, _bitEll_ 2, _t_ 1, _t_ 2, _t_ 3, _A_ , _r_ , _s_ ) consisting of 3 bits, 3 elements in Zℓ _e_ , one element of the finite field and 2 bytes. 

- **Output:** An octet string _M_ of length 3 · _Nz_ + 2 · _Np_ + 3 where _Nz_ = ⌈(⌈log2 ℓ<sup>_e_</sup> ⌉)/8)⌉ and _Np_ = ⌈(log2 _p_ )/8⌉. 

**Actions:** Compute the octet string as follows: 

1. Convert _t_ 1, _t_ 2, _t_ 3 into the octet strings _M_ 1, _M_ 2, _M_ 3 respectively, each of length _Nz_ (cf. §1.2.8). 

2. Convert _A_ into an octet string _M_ 4 of the length 2 · _Np_ (cf. §1.2.7). 

3. Let _M_ 5 = _r_ if _bit_ = 1 and _M_ 5 = _r_ ∨ 0 _x_ 80 if _bit_ = 0, i.e., info about _bit_ is encoded in the most significant bit of _r_ . 

4. Set _M_ 6 = _s_ , an octet. 

5. Set _M_ 7 = _bitEll_ 1 ∨ (2 · _bitEll_ 2), an octet. 

6. Form _M_ = _M_ 1 _M_ 2 _M_ 3 _M_ 4 _M_ 5 _M_ 6 _M_ 7. 

7. Output _M_ . 

## **1.3 Detailed protocol specification** 

This section specifies the supersingular isogeny key encapsulation (SIKE) protocol. Some options have been omitted from this specification for the purpose of simplicity. In particular, the full specification below does not employ point compression. Users seeking the compression of public keys described in [2, 9, 41, 42] should refer to the implementation provided at `https://github.com/Microsoft/ PQCrypto-SIDH` . 

The set of public parameters for SIKE is defined in §1.3.1. The two necessary isogeny computation algorithms are defined in §1.3.5. The IND-CPA PKE scheme is defined in §1.3.10. The subsequent INDCCA KEM is defined in §1.3.11. The security proofs of both the PKE and the KEM are in §4.3. 

### **1.3.1 Public parameters** 

The public parameters in SIKE are: 

- Two positive integers _e_ 2 and _e_ 3 that define a finite field F _p_ 2 where _p_ = 2<sup>_e_2</sup> 3<sup>_e_3</sup> − 1, 

- A starting supersingular elliptic curve _E_ 0/F _p_ 2, 

- A set of three _x_ -coordinates corresponding to points in _E_ 0[2<sup>_e_2</sup> ], and 

- A set of three _x_ -coordinates corresponding to points in _E_ 0[3<sup>_e_3</sup> ]. 

12 

### **1.3.2 Starting curve** 

The public starting curve is the supersingular elliptic curve 

with # _E_ 0(F _p_ 2) = (2<sup>_e_2</sup> 3<sup>_e_3</sup> )<sup>2</sup> and _j_ -invariant equal to _j_ ( _E_ 0) = 287496. This is the special instance of the Montgomery curve _By_<sup>2</sup> = _x_<sup>3</sup> + _Ax_<sup>2</sup> + _x_ , where _A_ = 6 and _B_ = 1. Note that this has been updated since the initial proposal, for reasons that are further explained in [11, §5]. The original curve had _j_ = 1728, for which _E_ 0 above is the only non-isomorphic 2-isogenous curve, meaning an attacker would have known for certain the first step taken away from this starting point in the 2-isogeny graph, regardless of the secret. There also exist only two (as opposed to four generally) isomorphism classes that are 3-isogenous to _j_ = 1728, so that distinct kernels can lead to isomorphic isogenies. Starting on _E_ 0 avoids both of these problems. Moreover, the combination of the basis points on _E_ 0 (defined in §1.3.3) and the computation of the secret kernel subgroups (defined in §1.3.6) ensures that the first 2-isogeny taken from _E_ 0 is not in the direction of the curve with _j_ = 1728, but rather to one of the two other 2-isogenous curves. 

### **1.3.3 Public generator points** 

The three _x_ -coordinates in the public parameters corresponding to points in _E_ 0[2<sup>_e_2</sup> ] are specified as follows. We first specify two points 

_P_ 2 ∈ _E_ 0(F _p_ 2) and _Q_ 2 ∈ _E_ 0(F _p_ 2) 

such that both points have exact order 2<sup>_e_2</sup> , and { _P_ 2, _Q_ 2} forms a basis for _E_ 0(F _p_ 2)[2<sup>_e_2</sup> ], i.e., the order-2<sup>_e_2</sup> Weil pairing _e_ 2<sup>_e_</sup> 2 ( _P_ 2, _Q_ 2) ∈ F<sup>×has full order, or equivalently,</sup><sup>_e_2([2</sup><sup>_e_2−1]</sup><sup>_P_2, [2</sup><sup>_e_2−1]</sup><sup>_Q_2) ∈F×is not equal to</sup> _p_<sup>2</sup> _p_<sup>2</sup> 1. Similarly, we specify two points 

such that both points have exact order 3<sup>_e_3</sup> , and { _P_ 3, _Q_ 3} forms a basis for _E_ 0(F _p_ 2)[3<sup>_e_3</sup> ]. 

Let _f_ := _x_<sup>3</sup> + 6 _x_<sup>2</sup> + _x_ and recall F _p_ 2 = F _p_ ( _i_ ) with _i_<sup>2</sup> + 1 = 0. The points _P_ 2, _Q_ 2, _P_ 3, _Q_ 3 are determined according to the following procedure: 

- _P_ 2 = [3<sup>_e_3</sup> ] � _i_ + _c_ , � _f_ ( _i_ + _c_ )�, where _c_ is the smallest nonnegative integer such that _P_ 2 ∈ _E_ 0(F _p_ 2) and [2<sup>_e_2−1</sup> ] _P_ 2 = (−3 ± 2 <u>√2, 0).</u> 

- • _Q_ 2 = [3<sup>_e_3</sup> ] � _i_ + _c_ , ~~�~~ _f_ ( _i_ + _c_ )�, where _c_ is the smallest nonnegative integer such that _Q_ 2 ∈ _E_ 0(F _p_ 2) and = 

- [2<sup>_e_2−1</sup> ] _Q_ 2 (0, 0). 

- _P_ 3 = [2<sup>_e_2−1</sup> ] � _c_ , ~~�~~ _f_ ( _c_ )�, where _c_ is the smallest nonnegative integer such that _f_ ( _c_ ) is square in F _p_ and _P_ 3 has order 3<sup>_e_3</sup> . 

- • _Q_ 3 = [2<sup>_e_2−1</sup> ] � _c_ , ~~�~~ _f_ ( _c_ )�, where _c_ is the smallest nonnegative integer such that _f_ ( _c_ ) is non-square in F _p_ and _Q_ 3 has order 3<sup>_e_3</sup> . 

The points _P_ 2, _Q_ 2, _P_ 3, _Q_ 3 could serve as public parameters for SIKE, but instead, for efficiency reasons (as described in [10]), we encode the points _P_ 2 and _Q_ 2 using the three _x_ -coordinates _xP_ 2, _xQ_ 2 and _xR_ 2, where _R_ 2 = _P_ 2 − _Q_ 2. Similarly, we encode _P_ 3, _Q_ 3 using the three _x_ -coordinates _xP_ 3, _xQ_ 3 and _xR_ 3, where _R_ 3 = _P_ 3 − _Q_ 3. 

13 

### **1.3.4 Public generator points (compressed SIKE)** 

The methodology for building generators for the compressed variant of SIKE is described below. It was introduced in [41] and is motived by key compression optimizations. Specify two points 

such that both points have exact order 3<sup>_e_3</sup> , and { _P_ 3, _Q_ 3} forms a basis for _E_ 0(F _p_ 2)[3<sup>_e_3</sup> ]. 

Let _f_ := _x_<sup>3</sup> + 6 _x_<sup>2</sup> + _x_ and recall F _p_ 2 = F _p_ ( _i_ ) with _i_<sup>2</sup> + 1 = 0. The points _P_ 2, _Q_ 2, _P_ 3, _Q_ 3 are determined according to the following procedure: 

- _P_ 2 = � <u>12</u> � _P_<sup>′</sup> 2 1 such that _P_ ′2<sup>=[3</sup><sup>_e_3]</sup> � _c_ , ~~�~~ _f_ ( _c_ )� is a point of order 2<sup>_e_2−1</sup> , where c is the smallest nonnegative integer such that _f_ ( _c_ ) is a non-square in F _p_ . 

- <u>1</u> 

- • _Q_ 2 = � 2 � _Q_<sup>′</sup> 2<sup>such that</sup><sup>_Q_′</sup> 2<sup>=[3</sup><sup>_e_3]</sup> � _c_ , ~~�~~ _f_ ( _c_ )� is a point of order 2<sup>_e_2−1</sup> and linearly independent with _P_<sup>′</sup> 2<sup>, where</sup><sup>_c_is the smallest nonnegative integer such that</sup><sup>_f_(</sup><sup>_c_) is a square in F</sup><sup>_p_.</sup> 

- _P_ 3 = [2<sup>_e_2</sup> ] � _c_ , ~~�~~ _f_ ( _c_ )�, where _c_ is the smallest nonnegative integer such that _f_ ( _c_ ) is square in F _p_ and _P_ 3 has order 3<sup>_e_3</sup> . 

- _Q_ 3 = (− _x_ ( _P_ 3), _i_ · _y_ ( _P_ 3)) is the distortion map of _P_ 3. 

The points _P_ 2, _Q_ 2, _P_ 3, _Q_ 3 could serve as public parameters for compressed SIKE, but instead, for efficiency reasons (as described in [10]), we encode the points _P_ 2 and _Q_ 2 using the three _x_ -coordinates _xP_ 2, _xQ_ 2 and _xR_ 2, where _R_ 2 = _P_ 2 − _Q_ 2. Similarly, we encode _P_ 3, _Q_ 3 using the three _x_ -coordinates _xP_ 3, _xQ_ 3 and _xR_ 3, where _R_ 3 = _P_ 3 − _Q_ 3. 

### **1.3.5 Isogeny computations** 

In this section we fix ℓ, _m_ ∈{2, 3} such that ℓ � _m_ . The two fundamental isogeny algorithms described are `isogen` ℓ and `isoex` ℓ. On input of the public parameters and a secret key, `isogen` ℓ outputs the public key corresponding to the input secret key. On input of a secret key and a public key, `isoex` ℓ outputs the corresponding shared key. These two algorithms will be used as building blocks for the PKE and KEM schemes defined in the subsequent sections. 

Both algorithms compute an ℓ<sup>_e_ℓ</sup> -degree isogeny via the composition of _e_ ℓ individual ℓ-degree isogenies; these ℓ-degree isogenies are evaluated on at least one point lying on the domain curve. Following [10, 13], rather than evaluating the image of an isogeny on a point _R_ = ( _xR_ , _yR_ ), it is more efficient to evaluate its image under the _x_ -only projection ( _xR_ , _yR_ ) �→ _xR_ . Since the coordinate maps for an isogeny ψ : _E_ → _E_<sup>′</sup> , _R_ �→ ψ( _R_ ) can always be written such that _x_ ψ( _R_ ) = _f_ ( _xR_ ) for some function _f_ [58], the `isogen` ℓ and `isoex` ℓ algorithms will assume the _i_ -th ℓ-degree isogeny ϕ _i_ adheres to this framework by writing ϕ _i_ : ( _x_ , — ) �→ ( _fi_ ( _x_ ), — ). 

> 1The notation <u>�</u> 21 <u>�</u> refers to the point halving map on Montgomery curves associated with some (arbitrary) square root convention. 

14 

Note that the definition of public parameters and public keys allows for the possibility of a generic implementation that reverts back to full isogeny computations which compute both the _x_ - and _y_ -coordinates of image points in either the Montgomery or short Weierstrass frameworks. In particular, the starting curve _E_ 0 defined in §1.3.2 is a special instance of a Montgomery curve and a short Weierstrass curve, and the public generator points in §1.3.3 uniquely define the _y_ -coordinates of _P_ 2, _Q_ 2, _P_ 3 and _Q_ 3. 

### **1.3.6 Computing public keys:** `isogen` ℓ 

A supersingular isogeny key pair consists of a secret key skℓ, which is an integer, and a set of three _x_ -coordinates pkℓ = ( _xP_ , _xQ_ , _xR_ ). 

**Public parameters.** A prime _p_ = 2<sup>_e_2</sup> 3<sup>_e_3</sup> −1, the starting curve _E_ 0/F _p_ 2, and public generators<sup>�</sup> _xP_ 2, _xQ_ 2, _xR_ 2� and<sup>�</sup> _xP_ 3, _xQ_ 3, _xR_ 3�. 

**Input.** A secret key skℓ. 

**Output.** A public key pkℓ. 

**Actions.** Compute a public key pkℓ, as follows: 

1. Set _xS_ ← _xP_ ℓ+[skℓ] _Q_ ℓ; 

2. Set ( _x_ 1, _x_ 2, _x_ 3) ←<sup>�</sup> _xPm_ , _xQm_ , _xRm_ �; 

3. For _i_ from 0 to _e_ ℓ − 1 do 

   - (a) Compute the _x_ portion for an ℓ-isogeny 

such that ker ϕ _i_ = ⟨[ℓ<sup>_e_ℓ−</sup><sup>_i_−1</sup> ] _S_ ⟩, where _S_ is a point on _Ei_ with _x_ -coordinate _xS_ ; 

   - (b) Set _Ei_ +1 ← _E_<sup>′</sup> ; 

   - (c) Set _xS_ ← _fi_ ( _xS_ ); 

   - (d) Set ( _x_ 1, _x_ 2, _x_ 3) ← ( _fi_ ( _x_ 1), _fi_ ( _x_ 2), _fi_ ( _x_ 3)); 

4. Output pkℓ = ( _x_ 1, _x_ 2, _x_ 3). 

### **1.3.7 Establishing shared keys:** `isoex` ℓ 

**Public parameters.** A prime _p_ = 2<sup>_e_2</sup> 3<sup>_e_3</sup> − 1. 

**Input.** A public key pk _m_ =<sup>�</sup> _xPm_ , _xQm_ , _xRm_ � and a secret key skℓ. 

**Output.** A shared secret _j_ , an octet string of length 2 _Np_ . 

**Actions.** Compute a shared secret _j_ , as follows: 

15 

1. Compute _E_ 0<sup>′from pk</sup> _m_<sup>using</sup><sup>`cfpk`(cf.§1.2.1);</sup> 

2. Set _xS_ ← _xPm_ +[skℓ] _Qm_ ; 

3. For _i_ from 0 to _e_ ℓ − 1 do 

   - (a) Compute the _x_ portion for an ℓ-isogeny 

such that ker ϕ _i_ = ⟨[ℓ<sup>_e_ℓ−</sup><sup>_i_−1</sup> ] _S_ ⟩, where _S_ is a point on _Ei_<sup>′with</sup><sup>_x_-coordinate</sup><sup>_xS_;</sup> 

   - (b) Set _Ei_<sup>′</sup> +1<sup>←</sup><sup>_E_′;</sup> 

   - (c) Set _xS_ ← _fi_ ( _xS_ ); 

4. Encode _j_ ( _Ee_<sup>′</sup> ℓ<sup>) into</sup><sup>_j_using</sup><sup>`fp2toos`(cf.§1.2.8).</sup> 

### **1.3.8 Optimized** `isogen` ℓ **and** `isoex` ℓ 

The algorithms `isogen` ℓ and `isoex` ℓ described above, though polynomial-time, are relatively inefficient in practice. In both cases, the most expensive part is the computation of the point [ℓ<sup>_e_ℓ−</sup><sup>_i_−1</sup> ] _S_ in step 3.a of each. Indeed, one such computation requires (at most) _e_ ℓ multiplications by the scalar ℓ, and is repeated _e_ ℓ times, for a total of _O_ ( _e_<sup>2</sup> ℓ<sup>)</sup><sup>_elementary operations_.</sup> 

In optimized implementations, following [13], it is recommended to replace the for loops by a recursive decomposition of the isogeny computation into _elementary operations_ , requiring only _O_ ( _e_ ℓ log _e_ ℓ) multiplications by the scalar ℓ, and a similar amount of evaluations of ℓ-isogenies. 

We call such a decomposition a _computational strategy_ , and we describe it by a full binary tree on _e_ ℓ − 1 nodes<sup>2</sup> . If we draw such trees so that all nodes lie within a triangular region of a hexagonal lattice, with all leaves on one border, then the path length of the tree is proportional to the computational effort required by the strategy. See Figure 1.1 for an example, and [13, §4] for a more formal definition. 

Figure 1.1: Three computational strategies of size _e_ ℓ − 1 = 6. The simple approach used in Sections 1.3.6 and 1.3.7 corresponds to the leftmost strategy. 

In practice, we represent any full binary tree on _e_ ℓ − 1 nodes in the following way: associate to any internal node the number of leaves to its right, then walk the tree in depth-first left-first order and output the labels as they are encountered. See Figure 1.2 for an example. 

Given any full binary tree represented this way, the computation in step 3 of `isogen` ℓ can be replaced by the following recursive procedure: 

> 2We recall that a _full_ binary tree on _n_ nodes is a binary tree with exactly _n_ nodes of degree 2 and _n_ + 1 nodes (leaves) of degree 0. 

16 

<!-- Start of picture text -->
3<br>Linearization: (3, 2, 1, 1, 2, 1)<br>2<br>2<br>1 1 1<br><!-- End of picture text -->

#### Figure 1.2: Linear representation of a strategy on 6 nodes. 

- **Input.** A starting curve _E_ , the _x_ -coordinate _xS_ of a point _S_ on _E_ , a list of _x_ -coordinates ( _x_ 1, _x_ 2, . . . ) on _E_ . A strategy ( _s_ 1, . . . , _st_ −1) of size _t_ − 1. 

**Output.** The image curve _E_<sup>′</sup> = _E_ /⟨ _S_ ⟩ of the isogeny ψ : _E_ → _E_ /⟨ _S_ ⟩ with kernel ⟨ _S_ ⟩, the list of image coordinates (ψ( _x_ 1), ψ( _x_ 2), . . . ) on _E_<sup>′</sup> . 

#### **Actions.** 

1. If _t_ = 1 (i.e., the strategy is empty) then 

- (a) Compute an ℓ-isogeny 

such that ker ϕ = ⟨ _S_ ⟩; 

(b) Return ( _E_<sup>′</sup> , _f_ ( _x_ 1), _f_ ( _x_ 2), . . . ); 

2. Let _n_ = _s_ 1 ; 

3. Let _L_ = ( _s_ 2, . . . , _st_ − _n_ ) and _R_ = ( _st_ − _n_ +1, . . . , _st_ −1); 

4. Set _xT_ ← _x_ [ℓ _n_ ] _S_ ; 

5. Set ( _E_ , ( _xU_ , _x_ 1, _x_ 2, . . . )) ← Recurse on ( _E_ , _xT_ , ( _xS_ , _x_ 1, _x_ 2, . . . )) with strategy _L_ ; 

6. Set ( _E_ , ( _x_ 1, _x_ 2, . . . )) ← Recurse on ( _E_ , _xU_ , ( _x_ 1, _x_ 2, . . . )) with strategy _R_ ; 

7. Return ( _E_ , ( _x_ 1, _x_ 2, . . . )). 

A similar algorithm, without the inputs ( _x_ 1, _x_ 2, . . . ), can be replaced inside `isoex` ℓ to obtain the same speedup. Remark that the simple algorithms of Sections 1.3.6 and 1.3.7 correspond to the strategy ( _e_ ℓ − 1, . . . , 2, 1). A _derecursivized_ version of this algorithm is given in Appendix A. 

We stress that the computational strategy is a public parameter independent of the (secret) input: it can be chosen once for all, and can possibly be hardcoded in the implementation. Changing it has no impact whatsoever on the security of the protocols (other than it affects the possible set of side-channel attacks). An implementer needs only be concerned with whether or not a given linear representation ( _s_ 1, . . . , _st_ −1) correctly defines a strategy, i.e. that it belongs to the language _S t_ defined by the following grammar: 

This can be readily verified with the following recursive procedure, that throws an error whenever a strategy is invalid, and terminates otherwise. 

17 

**Actions.** 

**Input.** A strategy ( _s_ 1, . . . , _st_ −1) of size _t_ − 1. 

1. If _t_ = 1 (i.e., the strategy is empty) return. 

2. Let _n_ ← _s_ 1 ; 

3. If _n_ < 1 or _n_ ≥ _t_ halt with error “Invalid strategy”; 

4. Let _L_ = ( _s_ 2, . . . , _st_ − _n_ ) and _R_ = ( _st_ − _n_ +1, . . . , _st_ −1); 

5. Recurse on _L_ ; 

6. Recurse on _R_ . 

These checks can easily be integrated into the isogeny computation algorithm. An analogous check is performed in the _derecursivized_ versions of Appendix A. 

### **1.3.9 Secret keys** 

The PKE and KEM schemes require two secret keys, sk2 and sk3, which are used to compute 2<sup>_e_2</sup> -isogenies and 3<sup>_e_3</sup> -isogenies, respectively (see §1.3.10 and §1.3.11). 

Let `N` sk2 = ⌈ _e_ 2/8⌉. Secret keys sk2 correspond to integers in the range {0, 1, . . . , 2<sup>_e_2</sup> − 1}, encoded as an octet string of length `N` sk2 using `itoos` (cf. §1.2.6). The corresponding keyspace is denoted K2. 

Let _s_ = ⌊log2 3<sup>_e_3</sup> ⌋ and `N` sk3 = ⌈ _s_ /8⌉. Secret keys sk3 correspond to integers in the range {0, 1, . . . , 2<sup>_s_</sup> − 1}, encoded as an octet string of length `N` sk3 using `itoos` (cf. §1.2.6). The corresponding keyspace is denoted K3. 

### **1.3.10 Public-key encryption** 

Algorithm 1 defines a public-key encryption scheme `PKE` = ( `Gen` , `Enc` , `Dec` ) [13, §3.3]. The two keyspaces K2 and K3 are defined in 1.3.9. The size of the message space M = {0, 1}<sup>_n_</sup> , as well as the function _F_ that maps the shared secret _j_ to bitstrings, are left unspecified; concrete choices corresponding to our implementations are specified in Section 1.4. Note that the function `Enc` generates randomness sk2. In the case of the key encapsulation mechanism we want to pass this randomness as input, in which case we write ( _c_ 0, _c_ 1) ← `Enc` (pk3, _m_ ; sk2) (see Line 7 of Algorithm 2). 

### **1.3.11 Key encapsulation mechanism** 

Algorithm 2 defines a key encapsulation mechanism `KEM` = ( `KeyGen` , `Encaps` , `Decaps` ), by applying a transformation of Hofheinz, Hövelmanns and Kiltz [23] to the PKE defined in §1.3.10. We slightly modify this transformation by including pk3 in the input to _G_ (as in [4]), and by simplifying “re-encryption” (see the proof of Theorem 1). Again, The two keyspaces K2 and K3 are defined in 1.3.9. The size of M = {0, 1}<sup>_n_</sup> as well as the functions _G_ and _H_ , are left unspecified; concrete choices corresponding to our implementations are specified in Section 1.4. 

18 

#### **Algorithm 1:** `PKE` = <u>(</u> `Gen` , `Enc` , `Dec` <u>)</u> 

|**function**`Gen`<br>**Input:** ()|**fu**|**nction**`Enc`<br>**Input:** pk3,_m_∈M,_r_ ∈K2|**fu**|**nction**`Dec`<br>**Input:** sk3, (_c_0,_c_1)|
|---|---|---|---|---|
|**Output:** (pk3,sk3)||**Output:** (_c_0,_c_1)||**Output:** _m_|
|**1**<br>sk3 ←_R_ K3|**4**|sk2 ←_r_|**10**|_j_←`isoex`3(_c_0,sk3)|
|**2**<br>pk3 ←`isogen`3(sk3)|**5**|_c_0 ←`isogen`2(sk2)|**11**|_h_←_F_(_j_)|
|**3**<br>**return** <sup>�</sup>pk3,sk3<br>�|**6**|_j_←`isoex`2(pk3,sk2)|**12**|_m_←_h_⊕_c_1|
||**7**<br>**8**|_h_←_F_(_j_)<br>_c_1 ←_h_⊕_m_|**13**|**return**_m_|
||**9**|**return**(_c_0,_c_1)|||

#### **Algorithm 2:** `KEM` = <u>(</u> `KeyGen` , `Encaps` , `Decaps` <u>)</u> 

|**function**`KeyGen`<br>**Input:** ()|**fu**|**nction**`Encaps`<br>**Input:** pk3|**fu**|**nction**`Decaps`<br>**Input:** (_s_,sk3,pk3), (_c_0,_c_1)|
|---|---|---|---|---|
|**Output:** (_s_,sk3,pk3)||**Output:** (_c_,_K_)||**Output:** _K_|
|**1**<br>sk3 ←_R_ K3|**5**|_m_←_R_ {0,1}<sup>_n_</sup>|**10**|_m_<sup>′ </sup>←`Dec`(sk3,(_c_0,_c_1))|
|**2**<br>pk3 ←`isogen`3(sk3)|**6**|_r_ ←_G_(_m_||pk3)|**11**|_r_<sup>′ </sup>←_G_(_m_<sup>′ </sup>||pk3)|
|**3**<br>_s_←_R_ {0,1}<sup>_n_</sup>|**7**|(_c_0,_c_1)←`Enc`(pk3,_m_;_r_)|**12**|_c_<sup>′</sup><br>0 <sup>←</sup><sup>`isogen`2(</sup><sup>_r_′)</sup>|
|**4**<br>**return** <sup>�</sup>_s_,sk3,pk3<br>�|**8**|_K_ ←_H_(_m_||(_c_0,_c_1))|**13**|**if** _c_<sup>′</sup><br>0 <sup>=</sup><sup>_c_0</sup><sup>**then**</sup>|
||**9**|**return**((_c_0,_c_1),_K_)|**14**|_K_ ←_H_(_m_<sup>′ </sup>||(_c_0,_c_1))|
||||**15**|**else**|
||||**16**|_K_ ←_H_(_s_||(_c_0,_c_1))|
||||**17**|**return**_K_|

#### **NIST’s API for the KEM** 

We now define how the inputs and outputs in Algorithm 2 match the API used in the implementations. NIST specifies the following API for the KEM: 

```
int crypto_kem_keypair(unsignedchar*pk,unsignedchar*sk);
int crypto_kem_enc(unsignedchar*ct,unsignedchar*ss,constunsignedchar*pk);
int crypto_kem_dec(unsignedchar*ss,constunsignedchar*ct,constunsignedchar*sk);
```

The public key `pk` is given by pk3. The secret key `sk` consists of the concatenation of _s_ , sk3 and pk3 3. The ciphertext `ct` consists of the concatenation of _c_ 0 and _c_ 1. Finally, the shared secret `ss` is given by _K_ . 

> 3Since NIST’s decapsulation API does not include an input for the public key, it needs to be included as part of the secret key. 

19 

## **1.4 Symmetric primitives** 

The three hash functions _F_ , _G_ and _H_ that are used in the key encapsulation mechanism `KEM` are all instantiated with the SHA-3 derived function `SHAKE256` as specified by NIST in [16]. 

Specifically, the function _G_ hashes the random bit string _m_ ∈M = {0, 1}<sup>_n_</sup> concatenated with the public key pk3. It is instantiated with `SHAKE256` , taking _m_ || pk3 as the input, requesting _e_ 2 output bits. In the notation of [16], this means _G_ ( _m_ || pk3) = `SHAKE256` ( _m_ || pk3, _e_ 2). The value _n_ corresponds to _n_ ∈{128, 192, 256}. 

The function _F_ is used as a key derivation function on the _j_ -invariant during public key encryption and is computed as _F_ ( _j_ ) = `SHAKE256` ( _j_ , _n_ ) using the notation of [16], where the requested output consists of _n_ bits. Again, the value _n_ corresponds to _n_ ∈{128, 192, 256}. 

The third function _H_ is used to derive the _k_ -bit shared key _K_ from the random bit string _m_ and the ciphertext _c_ produced by `Enc` . It is computed as `SHAKE256` ( _m_ || _c_ , _k_ ) with _m_ || _c_ as the input. The value _k_ corresponds to the number of bits of classical security, i.e., _k_ ∈{128, 192, 256}. 

## **1.5 Public key compression** 

Recall that uncompressed SIKE public keys are of the form ( _xP_ , _xQ_ , _xR_ ) ∈ (F _p_ 2)<sup>3</sup> , which correspond to three points _P_ , _Q_ , _R_ ∈ _EA_ (F _p_ 2) of exact order ℓ<sup>_e_</sup> , for ℓ ∈{2, 3}. Following [2] (and the further improvements described in [9, 59]), the idea of public key compression is to instead represent these points as elements of Zℓ _e_ × Zℓ _e_ with respect to a ℓ<sup>_e_</sup> -torsion basis that is determinstically chosen as a function of _EA_ . Encoding elements of Zℓ _e_ × Zℓ _e_ requires roughly half as many bits as encoding elements of F _p_ 2. In particular, the compressed keys require 3.5 log _p_ bits instead of the 6 log _p_ to represent the triple ( _xP_ , _xQ_ , _xR_ ). This translates to a ≈ 41% saving in key sizes. 

_Remark_ 1 _._ Note that ciphertext compression is also possible although compressed ciphertexts occupy about 4 log _p_ bits (≈ 33% savings) instead of the 3.5 log _p_ bits achieved in key compression due to a tradeoff introduced in [42] allowing for a much faster decapsulation. 

In Appendix C we describe the compression and decompression algorithms. Note that, since all of the operations in both algorithms are performed on public data, side-channel countermeasures (e.g., constanttime routines) are irrelevant except for the last step of the decompression algorithm in which we compute the last kernel generator using `Ladder3pt` (Algorithm 8). We point out that several alternatives for subroutines in both compression and decompression are possible. For example, compression requires the solutions of 2-dimensional discrete logarithm problems in _E_ (F _p_ 2)[ℓ<sup>_e_</sup> ], which can be solved directly in _E_ (F _p_ 2)[ℓ<sup>_e_</sup> ] (cf. [53]), but for improved performance our optimized implementation instead transports the problems to multiple 1-dimensional discrete logarithms in F<sup>×</sup> _p_<sup>2, by way of the Tate pairing [2, 9, 59].</sup> 

For more detailed information on the compression procedures followed in our implementation see [41] and [42]. 

_Remark_ 2 _._ It is worth mentioning that both SIKE public keys and ciphertexts are compressible. Due to the asymmetry in the original SIDH construction (binary and ternary torsions), compression techniques are faster in the binary torsion, and therefore torsions in Algorithms 2 are swapped for compression. 

20 

This implies that the most frequently used operation (Encapsulation) performs the fastest compression `compress` ℓ for ℓ = 3 which compressed points that are in the 2<sup>_e_2</sup> -torsion subgroup.<sup>4</sup> 

## **1.6 Parameter sets** 

This section presents four different parameter sets, the concrete security of which is discussed in Chapter 5. The underlying prime fields are of the form _p_ = 2<sup>_e_2</sup> 3<sup>_e_3</sup> − 1 where 2<sup>_e_2</sup> ≈ 3<sup>_e_3</sup> . 

The eight sets of parameters are `SIKEp434` , `SIKEp434_compressed` , `SIKEp503` , `SIKEp503_compressed SIKEp610` , `SIKEp610_compressed` , `SIKEp751` and `SIKEp751_compressed` , named so because of the bitlength of the prime field characteristic. In each case the parameters are, in order: the prime _p_ and the values _e_ 2 and _e_ 3; the values _xQ_ 2,0 and _xQ_ 2,1 such that _xQ_ 2 = _xQ_ 2,0 + _xQ_ 2,1 · _i_ ; the values _xP_ 2,0 and _xP_ 2,1 such that _xP_ 2 = _xP_ 2,0 + _xP_ 2,1 · _i_ ; the values _xR_ 2,0 and _xR_ 2,1 such that _xR_ 2 = _xR_ 2,0 + _xR_ 2,1 · _i_ ; the values _xQ_ 3,0 and _xQ_ 3,1 such that _xQ_ 3 = _xQ_ 3,0 + _xQ_ 3,1 · _i_ ; the values _xP_ 3,0 and _xP_ 3,1 such that _xP_ 3 = _xP_ 3,0 + _xP_ 3,1 · _i_ ; the values _xR_ 3,0 and _xR_ 3,1 such that _xR_ 3 = _xR_ 3,0 + _xR_ 3,1 · _i_ . 

### **1.6.1** `SIKEp434` 

   - `p` = `0002341F 27177344 6CFC5FD6 81C52056 7BC65C78 3158AEA3 FDC1767A E2FFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF` 

   - `e2` = `000000D8` 

   - `e3` = `00000089` 

- `xQ20` = `0000C746 1738340E FCF09CE3 88F666EB 38F7F3AF D42DC0B6 64D9F461 F31AA2ED C6B4AB71 BD42F4D7 C058E13F 64B237EF 7DDD2ABC 0DEB0C6C` 

- `xQ21` = `000025DE 37157F50 D75D320D D0682AB4 A67E4715 86FBC2D3 1AA32E69 57FA2B26 14C4CD40 A1E27283 EAAF4272 AE517847 197432E2 D61C85F5` 

- `yQ20` = `0001D407 B70B01E4 AEE172ED F491F4EF 32144F03 F5E054CE F9FDE5A3 5EFA3642 A1181790 5ED0D4F1 93F31124 264924A5 F64EFE14 B6EC97E5` 

- `yQ21` = `0000E7DE C8C32F50 A4E735A8 39DCDB89 FE0763A1 84C525F7 B7D0EBC0 E84E9D83 E9AC53A5 72A25D19 E1464B50 9D97272A E761657B 4765B3D6` 

- `xP20` = `00003CCF C5E1F050 030363E6 920A0F7A 4C6C71E6 3DE63A0E 6475AF62 1995705F 7C84500C B2BB61E9 50E19EAB 8661D25C 4A50ED27 9646CB48` 

- `xP21` = `0001AD1C 1CAE7840 EDDA6D8A 924520F6 0E573D3B 9DFAC6D1 89941CB2 2326D284 A8816CC4 249410FE 80D68047 D823C97D 705246F8 69E3EA50` 

- `yP20` = `0001AB06 6B849495 82E3F666 88452B92 55E72A01 7C45B148 D719D9A6 3CDB7BE6 F48C812E 33B68161 D5AB3A0A 36906F04 A6A6957E 6F4FB2E0` 

- `yP21` = `0000FD87 F67EA576 CE97FF65 BF9F4F76 88C4C752 DCE9F8BD 2B36AD66` 

> 4Note that the points pkℓ are in the complementary torsion other than ℓ. 

21 

   - `E04249AA F8337C01 E6E4E1A8 44267BA1 A1887B43 3729E1DD 90C7DD2F` 

- `xR20` = `0000F37A B34BA0CE AD94F43C DC50DE06 AD19C67C E4928346 E829CB92 580DA84D 7C36506A 2516696B BE3AEB52 3AD7172A 6D239513 C5FD2516` 

- `xR21` = `000196CA 2ED06A65 7E90A735 43F3902C 208F4108 95B49CF8 4CD89BE9 ED6E4EE7 E8DF90B0 5F3FDB8B DFE489D1 B3558E98 7013F980 6036C5AC` 

- `xQ30` = `00012E84 D7652558 E694BF84 C1FBDAAF 99B83B42 66C32EC6 5B10457B CAF94C63 EB063681 E8B1E739 8C0B241C 19B9665F DB9E1406 DA3D3846` 

- `xQ31` = `00000000` 

- `yQ30` = `00000000` 

- `yQ31` = `0000EBAA A6C73127 1673BEEC E467FD5E D9CC29AB 564BDED7 BDEAA86D D1E0FDDF 399EDCC9 B49C829E F53C7D7A 35C3A074 5D73C424 FB4A5FD2` 

- `xP30` = `00008664 865EA7D8 16F03B31 E223C26D 406A2C6C D0C3D667 466056AA E85895EC 37368BFC 009DFAFC B3D97E63 9F65E9E4 5F46573B 0637B7A9` 

- `xP31` = `00000000` 

- `yP30` = `00006AE5 15593E73 97609197 8DFBD70B DA0DD6BC AEEBFDD4 FB1E748D DD9ED3FD CF679726 C67A3B2C C12B3980 5B32B612 E058A428 0764443B` 

- `yP31` = `00000000` 

- `xR30` = `0001CD28 597256D4 FFE7E002 E8787075 2A8F8A64 A1CC78B5 A2122074 783F51B4 FDE90E89 C48ED91A 8F4A0CCB ACBFA7F5 1A89CE51 8A52B76C` 

- `xR31` = `00014707 3290D78D D0CC8420 B1188187 D1A49DBF A24F26AA D46B2D9B B547DBB6 F63A760E CB0C2B20 BE52FB77 BD2776C3 D14BCBC4 04736AE4` 

### **1.6.2** `SIKEp434_compressed` 

- `p` = `0002341F 27177344 6CFC5FD6 81C52056 7BC65C78 3158AEA3 FDC1767A E2FFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF` 

- `e2` 

- `e3` 

   - = `000000D8` 

   - = `00000089` 

- `xQ20` = `0001F23C F1B907ED EBDB6BC4 AB18C1E6 2CA20EA3 437D5D58 EC34981F 17D2CFAE C244241D 8494AF8A C8C1A359 A0BA4167 6F2E0B4D 0605C092` 

- `xQ21` = `00009866 7831535E 5E02562D B217BD86 F84B9830 AAD60641 454AE862 50218091 3E1798D6 13D59676 0AE93F0C 143FD643 8E99D2A5 01379355` 

- `xP20` = `00002F75 7834CA38 E9A149EE 9AA469F5 F7044F21 E0FFC221 2177C82D 7C3D4520 68F15591 30263CE3 3E3BED84 1E332D93 7FAB2BC0 89E57BDA` 

22 

- `xP21` = `0000123E E2393221 33D147DE EB520B4A 0AAC93CC D6E3505F 6B8B5E30 795A01C0 1EE1185C BF10F5A9 420E1AA3 EAF6013F F0232202 A614D2AE` 

- `xR20` = `000098A2 F720085C 56A0BEE7 3EC958DA 5EE05C6C 4E99E0C5 00C7C2ED FF10A433 56FF83F1 D082B5CF 6D37F0BF 78576711 78FA05E0 9636F391` 

- `xR21` = `0001E1E1 AD8568A6 9C98E305 6BCCF9D3 0B173824 682AF046 2E0DA766 6626E399 E428E873 7CBE44E6 A8C04533 2E6935C2 69B709F3 1DD34330` 

- `xQ30` = `0000F71F B8FC6F96 4822D12D 07448181 29564040 96D7A1B9 F6A36CD0 DAC0BA3A 0D05FEF8 DE7C9349 A293AA50 9F917803 B3312818 E432A58C` 

- `xQ31` = `000006C9 405C49DC ED859BBC 2A1EA424 00CF4E07 FE7AEAA8 1828E904 4AD1CD53 2441650F D103E1F1 81527785 73E647B6 E8F1EA18 55F28681` 

- `xP30` = `0000F71F B8FC6F96 4822D12D 07448181 29564040 96D7A1B9 F6A36CD0 DAC0BA3A 0D05FEF8 DE7C9349 A293AA50 9F917803 B3312818 E432A58C` 

- `xP31` = `00022D55 E6BB2967 7F76C41A 57A67C32 7AF70E70 32DDC3FB E5988D76 982E32AC DBBE9AF0 2EFC1E0E 7EAD887A 8C19B849 170E15E7 AA0D797E` 

- `xR30` = `0001606C 450113A8 35A7A52F 6A6A70C8 6D9225DD B1D8A858 748BF544 890B1610 299BFF5F 715D5643 8D0C69FA 211284A8 149C3EDF B42C18FD` 

- `xR31` = `00000000` 

### **1.6.3** `SIKEp503` 

- `p` = `004066F5 41811E1E 6045C6BD DA77A4D0 1B9BF6C8 7B7E7DAF 13085BDA 2211E7A0 ABFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF` 

- `e2` 

      - = `000000FA` 

   - `e3` = `0000009F` 

- `xQ20` = `00325CF6 A8E2C618 3A8B9932 198039A7 F965BA85 87B67925 D08D809D BF9A69DE 1B621F7F 134FA2DA B82FF5A2 615F92CC 71419FFF AAF86A29 0D604AB1 67616461` 

- `xQ21` = `003E7B04 94C8E60A 8B72308A E09ED348 45B34EA0 911E356B 77A11872 CF7FEEFF 745D98D0 624097BC 1AD7CD2A DF7FFC2C 1AA5BA3C 6684B964 FA555A07 15E57DB1` 

- `yQ20` = `003A3465 4000BD4C B2612017 BD5A1965 A9F89FE1 1C55D517 DF91B89B 94F4F9C5 8B9A9DD0 56915573 FEDC09CC D4997E82 378759E0 0A2DE225 CE04589D 201FD754` 

23 

- `yQ21` = `0019DEF0 E8930E51 23A22E34 6B1FFBD3 5EB01451 647D8708 A4835473 B2539BD2 6806ED10 5A29F2D3 F7EAA262 426A9653 38782C5D 20FBF478 E4D1C8DB FC5B8294` 

- `xP20` = `0002ED31 A03825FA 14BC1D92 C503C061 D843223E 611A92D7 C5FBEC0F 2C915EE7 EEE73374 DF6A1161 EA00CDCB 786155E2 1FD38220 C3772CE6 70BC6827 4B851678` 

- `xP21` = `001EE4E4 E9448FBB AB4B5BAE F280A99B 7BF86A1C E05D55BD 603C3BA9 D7C08FD8 DE7968B4 9A78851F FBC6D0A1 7CB2FA1B 57F3BABE F87720DD 9A489B55 81F915D2` 

- `yP20` = `00244D5F 814B6253 688138E3 17F24975 E596B09B B15C6418 E5295AAF 73BA7F96 EFED145D FAE1B21A 8B7B121F EFA1B6E8 B52F0047 8218589E 604B9735 9B8A6E0F` 

- `yP21` = `00181CCC 9F0CBE13 90CC1414 9E8DE88E E79992DA 32230DED B25F04FA DE07F242 A9057366 060CB599 27DB6DC8 B20E6B15 747156E3 C5300545 E9674487 AB393CA7` 

- `xR20` = `003D24CF 1F347F1D A54C1696 442E6AFC 192CEE5E 320905E0 EAB3C9D3 FB595CA2 6C154F39 427A0416 A9F36337 354CF1E6 E5AEDD73 DF80C710 026D4955 0AC8CE9F` 

- `xR21` = `0006869E A28E4CEE 05DCEE8B 08ACD597 75D03DAA 0DC8B094 C85156C2 12C23C72 CB2AB2D2 D90D4637 5AA6D66E 58E44F8F 219431D3 006FDED7 993F5164 9C029498` 

- `xQ30` = `0039014A 74763076 675D24CF 3FA28318 DAC75BCB 04E54ADD C6494693 F72EBB7D A7DC6A3B BCD188DA D5BECE9D 6BB4ABDD 05DB38C5 FBE52D98 5DCAF744 22C24D53` 

- `xQ31` = `00000000` 

- `yQ30` = `00000000` 

- `yQ31` = `00255120 12C90A68 69C4B29B 9A757A03 006BC7DF 0BF7A252 6A071393 9FA48018 AE3E249B D63699BE B3B8DEA2 15B7AE1B 5A30FE37 1B64C5F1 B0BF051A 11D68E04` 

- `xP30` = `0032D03F D1E99ED0 CB05C070 7AF74617 CBEA5AC6 B75905B4 B54B1B0C 2D736978 40155E7B 1005EFB0 2B5D0279 7A8B66A5 D258C76A 3C9EF745 CECE11E9 A178BADF` 

- `xP31` 

   - = `00000000` 

- `yP30` = `002D810F 828E3DC0 24D1BBBC 7D6FA6E3 02CC5D45 8571763B 7CCD0E4D BC9FA116 3F0C1F8F 4AE32A57 F89DF8D2 586D2A06 E9FA3044 2B94A725 266358C4 5236ADF3` 

- `yP31` = `00000000` 

24 

- `xR30` = `0000C146 5FD048FF B8BF2158 ED57F0CF FF0C4D5A 4397C754 2D722567 700FDBB8 B2825CAB 4B725764 F5F52829 4B7F95C1 7D560E25 660AD3D0 7AB011D9 5B2CB522` 

- `xR31` = `00288165 466888BE 1E78DB33 9034E2B8 C7BDF048 3BFA7AB9 43DFA05B 2D171231 7916690F 5E713740 E7C7D483 8296E673 57DC34E3 460A95C3 30D51697 21981758` 

### **1.6.4** `SIKEp503_compressed` 

   - `p` = `004066F5 41811E1E 6045C6BD DA77A4D0 1B9BF6C8 7B7E7DAF 13085BDA 2211E7A0 ABFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF` 

   - `e2` = `000000FA` 

   - `e3` = `0000009F` 

- `xQ20` = `00127E2A 93ACC146 DBAFF173 6C05A6AB C1D7A204 7ACAC67D 8376664F 752BF0C1 65BC8359 1A133452 94684CA7 905472FB 7B42CF74 279A103C 1160A907 9897F7FE` 

- `xQ21` = `0001D4E4 48A987A3 87135E53 AE756D50 BFE33804 1156E468 DF8496FA C2FEE315 9D54E45A 77375EE6 1CE7A424 DEDF5E8C D76BE308 1EA3A0F8 2ADF1DC7 A27FED74` 

- `xP20` = `001B3B05 B5B16AB7 51539381 BC40C380 BBCA4C51 F83BE1A1 33C120FF 512AF82F D1B48DC3 01A68CBF 26CB9CB9 16827692 2641449A 235EF7DE 9EBE4BF6 195AE5BC` 

- `xP21` = `0008EB09 019A3B1E 83624F58 A80A2F3B 0DCC51CC AD5E184B 9AE75909 CF081D49 05B1DA2C C0FCAA55 34E63CF4 376017F9 1B04770D B0747BDE 00D86781 2667C39D` 

- `xR20` = `001ED5A3 856AF031 A9F37C2B 74301AB4 8806000B 840B5ED2 CE216DDA 4BA4E182 FA9C323A 470100DE 379C0092 3A7A6773 F2CFDDE9 FB645FC3 989DBC05 3D8E2C7D` 

- `xR21` = `000948FC DC0EFC46 B38B8F7E D2CB5680 AD864615 302C29D9 18E2EFD2 D317DB13 0AC1BADC ACC460E7 B9888640 B304FF9E 0D0FA616 BE343270 AF1D8BE1 829461EB` 

- `xQ30` = `003BAA0E 33084960 851B2BB6 8CF94538 C43CFA2B 2B296274 CD915284 4B843FCE F12839E7 E2AD41A9 0134A0DE C1D94B53 0FB5A80F DDAE6368` 

25 

```
C29E5CF8 43265AB3
```

- `xQ31` = `00167A0D 5F1DAC47 FAF2C217 2166CA3D 0DE573D2 C7ACB8E9 E9A0E5D1 1EB55A27 CCD7A8A8 34DA8A03 2D113D04 812366A8 7796C1DE 31FFA49D 17573D34 8A5C4FE0` 

- `xP30` = `003BAA0E 33084960 851B2BB6 8CF94538 C43CFA2B 2B296274 CD915284 4B843FCE F12839E7 E2AD41A9 0134A0DE C1D94B53 0FB5A80F DDAE6368 C29E5CF8 43265AB3` 

- `xP31` = `0029ECE7 E26371D6 655304A6 B910DA93 0DB682F5 B3D1C4C5 29677609 035C8D78 DF285757 CB2575FC D2EEC2FB 7EDC9957 88693E21 CE005B62 E8A8C2CB 75A3B01F` 

- `xR30` = `00264CBC 7895FF5B EED9E748 68E7C16A 90C73FFF 80F0E8A0 E806BC31 5C24BA51 AE9A3420 A8C0FF49 1C72EC37 911AD5D0 91DBB1FC 9FCF2360 AD730EDE D5B4F2E1` 

- `xR31` = `00000000` 

### **1.6.5** `SIKEp610` 

   - `p` = `00000002 7BF6A768 819010C2 51E7D88C B255B2FA 10C4252A 9AE7BF45 048FF9AB B1784DE8 AA5AB02E 6E01FFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF` 

   - `e2` = `00000131` 

   - `e3` = `000000C0` 

- `xQ20` = `25DA39EC 90CDFB9B C0F772CD A52CB8B5 A9F478D7 AF8DBBA0 AEB3E524 32822DD8 8C38F4E3 AEC0746E 56149F1F E89707C7 7F8BA413 45686297 24F4A8E3 4B06BFE5 C5E66E08 67EC38B2 83798B8A` 

- `xQ21` = `00000002 250E1959 256AE502 428338CB 47153995 51AEC78D 8935B2DC 73FCDCFB DB1A0118 A2D3EF03 489BA6F6 37B1C7FE E7E5F313 40A1A537 B76B5B73 6B4CDD28 4918918E 8C986FC0 2741FB8C 98F0A0ED` 

- `yQ20` = `A4FD5539 025C0611 E4B1CEC3 C36F0D75 90C035D3 A25AD930 22849CCE B3F67E4B 1DBE9884 04290DD8 B87B8D5E 69ED3B0C 5CDBCA24 8DC9D174 CF762012 CFE2D725 CFD92057 F2DBF8B0 4C7B12CC` 

- `yQ21` = `00000002 01C807BD 738624E2 2B87554A 2E053A46 A9573BA8 63D4A9D3 09533E30 B27BF7DD 8137F5CE 0F79C263 D9D05054 1D69817A 839085A7 6395F879 315F6999 E3441FC8 FB3936DE E1BEF5B4 E0E25096` 

26 

- `xP20` = `00000001 B368BC60 19B46CD8 02129209 B3E65B98 BC64A92B C4DB2F9F 3AC96B97 A1B9C124 DF549B52 8F18BEEC B1666D27 D4753043 5E842212 72F3A97F B80527D8 F8A359F8 F1598D36 5744CA30 70A5F26C` 

- `xP21` = `00000001 459685DC A7112D1F 6030DBC9 8F2C9CBB 41617B6A D913E652 3416CCBD 8ED9C784 1D97DF83 092B9B3F 2AF00D62 E08DAD8F A743CBCC CC1782BE 0186A343 2D3C97C3 7CA16873 BEDE01F0 637C1AA2` 

- `yP20` = `00000001 CD75CF51 2FFA9DF8 78EF4950 01A57ABC 07FC7CE9 BB488BB5 2DDCD727 2D8A4FD1 7DD258ED 3F844C86 2CF48803 B9AC2668 C7CB79C3 96128763 B578080C 30D14CA7 EB709F98 E3E682A3 91FB35A7` 

- `yP21` = `00000002 001062A6 289E4082 CED88402 9207A1AC DEC525D7 BC165A6C FF8BB469 A8588950 A416DBB9 24D2D673 E3D6C32D 232F6E6A DA62B376 08F652C0 B8628827 B304BF13 65D82113 46207B24 EFF09458` 

- `xR20` = `00000001 B36A006D 05F9E370 D5078CCA 54A16845 B2BFF737 C8653687 07C0DBBE 9F5A62A9 B9C79ADF 11932A9F A4806210 E25C92DB 019CC146 706DFBC7 FA2638EC C4343C1E 390426FA A7F2F07F DA163FB5` 

- `xR21` = `00000001 83C9ABF2 297CA696 99357F58 FED92553 436BBEBA 2C3600D8 9522E700 9D19EA5D 6C18CFF9 93AA3AA3 3923ED93 592B0637 ED0B33AD F12388AE 912BC4AE 4749E2DF 3C329299 4DCF3774 7518A992` 

- `xQ30` = `00000001 4E647CB1 9B7EAAAC 640A9C26 B9C26DB7 DEDA8FC9 399F4F8C E620D2B2 200480F4 338755AE 16D0E090 F15EA188 2166836A 478C6E16 1C938E4E B8C2DD77 9B45FFDD 17DCDF15 8AF48DE1 26B3A047` 

- `xQ31` = `00000000` 

- `yQ30` = `00000000` 

- `yQ31` = `E674067F 5EA6DE85 545C0A99 E9E71E64 FABFDC28 1D1E540F EDA47A56 ED3ADCDD E1841083 FABC7954 B467C71A C6349B04 974A7F9B 688C5F73 5632FEB3 94146B0A 08088006 9D8DA332 4EDF795B` 

- `xP30` = `00000001 587822E6 47707ED4 313D3BE6 A811A694 FB201561 111838A0 816BFB5D EC625D23 772DE48A 26D78C04 EEB26CA4 A571C67C E4DC4C62 0282876B 2F2FC263 3CA548C3 AB0C45CC 991417A5 6F7FEFEB` 

- `xP31` = `00000000` 

- `yP30` = `14F29511 4B69D476 9AC06DD0 7F051AD1 114BCB7F A6B6EDE1 9F840969 AFD56FD1 F728907D 3320A030 9462A944 4D24FE75 4666DB24 70080951 B31C2AC5 9704ABC7 670C3C3A 992C3C16 29791F30` 

- `yP31` = `00000000` 

- `xR30` = `00000001 DB73BC2D E666D24E 59AF5E23 B79251BA 0D189629 EF87E56C 38778A44 8FACE312 D08EDFB8 76C3FD45 ECF3746D 96E2CADB BA08B1A2 06C47DDD 93137059 E34C90E2 E42E10F3 0F6E5F52 DED74222` 

27 

- `xR31` = `00000001 B2C30180 DAF5D918 71555CE8 EFEC76A4 D521F877 B7543112 28C7180A 3E2318B4 E7A00341 FF99F34E 35BF7A10 53CA76FD 77C0AFAE 38E20918 62AB4F1D D4C8D9C8 3DE37ACB A6646EDB 4C238B48` 

### **1.6.6** `SIKEp610_compressed` 

- `p` = `00000002 7BF6A768 819010C2 51E7D88C B255B2FA 10C4252A 9AE7BF45 048FF9AB B1784DE8 AA5AB02E 6E01FFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF` 

- `e2` 

      - = `00000131` 

   - `e3` = `000000C0` 

- `xQ20` = `00000001 AAAF04FF FA0E920A 9D57B705 A019428F CDC7519A D382A3C2 452C47CB 0958477D DA6D112F 803F0B0F 93C1189A 79DC856F 653263E1 11A35C21 D5A9FF83 3915F8A6 AEABA65B 1D4949E2 C555B554` 

- `xQ21` = `32B70A9E C1ED3130 313FEB14 1828F365 9AF973AC 42AC8C4E FA89AC25 0A5C978C 29DA9D07 1606EAFE BFDBD97A 53548DF9 B5B860C2 AAEF8403 CF021DCE C87EE0C5 12F5D9AC BEECB66C 11E5AFE7` 

- `xP20` = `00000001 81858998 C9AA9597 F380DC28 ABF6173F 83F84A8F D45B0205 B42BCEFF EB609F11 B084205E C9F17599 B7215675 2BE0D893 1686BFB9 A6582EE8 D23460DE DF110BC4 E0E92734 CEC7D75E C902001D` 

- `xP21` = `1D339C0C E6B50439 45696090 3A352B20 7BDBF7ED 2188D1F2 42D8F96B E97DC4FD AB9FE77A 7CB98619 F53292B4 4EBE7E26 A0344E8E 3E184B43 578CE0DC A512D5D0 89EFE77D 25DCDF3B 81C74B30` 

- `xR20` = `00000001 3979F57A F9D5E767 65CD95CF 685BE36D 3F3EA6DB ADAAA9F1 6EE7CC74 1F593A2F BCD5D24B 09AECB20 256455E0 DA41CA94 2224B061 03AD1B10 267ABC59 0AB8D90E 8CDA3973 4AB33CFA BB3AC133` 

- `xR21` = `00000001 BB80FA13 4385E8FA 1ABB9587 609F59C2 BB895505 6BF18460 451D86CD EBF0B1AE 5199F138 493F5016 E5C22740 64045251 1A4E3A1F 3EDA6AA5 ED0D3AC3 7615E26A B80F6DF2 2B656DCB A22838C1` 

- `xQ30` = `56DAE1DE 4A196594 7D689C6D 0F08F041 34F8C8D1 1CD3F938 68E827DF 93C580BD F781ED32 A3892752 1B638CCC 4E946AEF B179EBB0 B0F185BD 80097AFE 4242C7BE B46AB1BA C8FB3AE9 11A231D2` 

- `xQ31` = `00000001 BA6391FD F6EE6623 55BE2450 7FFB171A 6FF4A5BF E00AE62E E208F738 41805CC8 E0F0C287 914E52FD 5684082C AEEC0DB6 909B1397` 

28 

```
EF04EEC9 06545386 898FD7F1 949493F0 8CF45895 79C09C95
```

- `xP30` = `56DAE1DE 4A196594 7D689C6D 0F08F041 34F8C8D1 1CD3F938 68E827DF 93C580BD F781ED32 A3892752 1B638CCC 4E946AEF B179EBB0 B0F185BD 80097AFE 4242C7BE B46AB1BA C8FB3AE9 11A231D2` 

- `xP31` = `C193156A 8AA1AA9E FC29B43C 325A9BDF A0CF7F6A BADCD916 22870273 6FF7F11F C969EDA6 DCB3AD02 A97BF7D3 5113F249 6F64EC68 10FB1136 F9ABAC79 7670280E 6B6B6C0F 730BA76A 863F636A` 

- `xR30` = `1797211F 860C7226 9AF31332 523E005D A5D6E2FA 48227319 BEEC8955 A8E3ECA2 3C590735 A275D333 351D1BD7 C41D5B2A 52AC5B75 84D9A17D 8E0AA956 E1C47B32 0EC98B94 6DCF3F89 9802B26A` 

- `xR31` = `00000000` 

### **1.6.7** `SIKEp751` 

   - `p` = `00006FE5 D541F71C 0E12909F 97BADC66 8562B504 5CB25748 084E9867 D6EBE876 DA959B1A 13F7CC76 E3EC9685 49F878A8 EEAFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF` 

   - `e2` = `00000174` 

   - `e3` = `000000EF` 

- `xQ20` = `00001723 D2BFA01A 78BF4E39 E3A333F8 A7E0B415 A17F208D 3419E759 1D59D8AB DB7EE6D2 B2DFCB21 AC29A40F 837983C0 F057FD04 1AD93237 704F1597 D87F074F 682961A3 8B5489D1 019924F8 A0EF5E4F 1B2E64A7 BA536E21 9F5090F7 6276290E` 

- `xQ21` = `00002569 D7EAFB6C 60B244EF 49E05B5E 23F73C4F 44169A7E 02405E90 CEB680CB 0756054A C0E3DCE9 5E295033 4262CC97 3235C2F8 7D89500B CD465B07 8BD0DEBD F322A2F8 6AEDFDCF EE65C093 77EFBA0C 5384DD83 7BEDB710 209FBC8D DB8C35C7` 

- `yQ20` = `000035B8 2D1BD2BA 608B4279 4C4820C5 6A3D8BBA D28380B8 D85A1910 E2609A61 F7BC0BCA 8ED8EF88 3E7E98C7 44A0AC85 D2893738 521B62EB 23D1983D 2EDCF2AB 437108DC 048AA853 FF9BC791 224B121E 8FDF1EA5 F617E6ED 5898663D DED49154` 

- `yQ21` = `00000F22 306A6963 907F16AA 38F89C67 2A4054DB 5FD1D265 98A3140E A204B100 94AE6409 3142AEB0 56942494 D216A74E D9F51FFC 9272D177` 

29 

```
21510133 34EC570B 532DB0C0 83CF3986 7F63D191 029033F9 42E977B8
5F69EC73 8B4C26D3 B72E2821
```

- `xP20` = `00004514 F8CC94B1 40F24874 F8B87281 FA6004CA 5B3637C6 8AC0C0BD B2983805 1F385FBB CC300BBB 24BFBBF6 710D7DC8 B29ACB81 E429BD1B D5629AD0 ECAD7C90 622F6BB8 01D0337E E6BC78A7 F12FDCB0 9DECFAE8 BFD643C8 9C3BAC1D 87F8B6FA` 

- `xP21` = `0000158A BF500B59 14B3A96C ED5FDB37 D6DD925F 2D6E4F7F EA3CC16E 10857540 77737EA6 F8CC7493 8D971DA2 89DCF243 5BCAC189 7D262769 3F9BB167 DC01BE34 AC494C60 B8A0F65A 28D7A31E A0D54640 653A8099 CE5A84E4 F0168D81 8AF02041` 

- `yP20` = `00000BF6 E4E7A28E 9A6EF66A 2F1614AE 2A2B5A58 3C9F2DC6 C83F84E2 D9E6577F 9E22B991 D58FB2F8 9666DC1D 40A2C0A3 AB876CF8 DA8878F1 2325BF8B 0CF92E45 AE006270 41C891BC 96FFBB87 4FC587E4 342F7809 8258DF2E 10A5708A 70A0D5A8` 

- `yP21` = `00001502 FB44178D 1DF80A53 858519CB CF233FE3 87905BC8 F9E41387 03C6DB7C 82302FBF B7E97153 F6001FE9 102D2597 AC2B300A 1C669D1A 2803F8D0 5BA3B1F2 ACBF27BC 1A127B4A 553916D6 2004FD21 633C5AEA AB748338 53B4C5C4 2EB71F7E` 

- `xR20` = `00006066 E07F3C0D 964E8BC9 63519FAC 8397DF47 7AEA9A06 7F3BE343 BC53C883 AF29CCF0 08E5A307 19A29357 A8C33EB3 600CD078 AF1C40ED 5792763A 4D213EBD E44CC623 195C387E 0201E723 1C529A15 AF5AB743 EE9E7C9C 37AF3051 167525BB` 

- `xR21` = `000050E3 0C2C0649 4249BC4A 144EB5F3 1212BD05 A2AF0CB3 064C322F C3604FC5 F5FE3A08 FB3A02B0 5A48557E 15C99225 4FFC8910 B72B8E13 28B4893C DCFBFC00 3878881C E390D909 E39F83C5 006E0AE9 79587775 443483D1 3C65B107 FADA5165` 

- `xQ30` = `00005BF9 54478180 3CBD7E0E A8B96D93 4C5CBCA9 70F9CC32 7A0A7E4D AD931EC2 9BAA8A85 4B8A9FDE 5409AF96 C5426FA3 75D99C68 E9AE7141 72D7F045 02D45307 FA4839F3 9A28338B BAFD54A4 61A53540 8367D513 2E6AA0D3 DA697336 0F8CD0F1` 

- `xQ31` = `00000000` 

- `yQ30` = `00000000` 

- `yQ31` = `00003351 F421FC15 8472AC2D D8B4DABB 5B599456 748A5BCC 4449398F 05ED1AD1 414B4EEB BB70FB91 383474B7 12EA4B5B F096092C DDD57C0A 090B0410 22064C3A 8DD3D890 E7B5AC34 A24CEF50 7955F027 CC4CECFD B67739CE 89F31FDC 5FE43243` 

- `xP30` = `0000605D 4697A245 C394B980 24A55547 46DC12FF 56D0C6F1 5D2F4812` 

30 

```
3B6D9C49 8EEE98E8 F7CD6E21 6E2F1FF7 CE0C969C CA29CAA2 FAA57174
EF985AC0 A5042600 18760E9F DF67467E 20C13982 FF5B49B8 BEAB05F6
023AF873 F827400E 453432FE
```

- `xP31` = `00000000` 

- `yP30` = `00005634 690BFC14 C45E2FAA 930D6258 9855E5BD D1435CFF BDF60962 8FD043B4 BF295BB3 5F7B6D37 836F2C59 A27BB61E D0FF57FF 8093FE6B 712133D2 6502F17C B0D46CDC 8CF9BA76 64EA2B6C 1672A8CA 2FF1CE31 3FEEEF41 99FC7F14 FE720617` 

- `yP31` = `00000000` 

- `xR30` = `000055E5 124A05D4 809585F6 7FE9EA1F 02A06CD4 11F38588 BB631BF7 89C3F98D 1C332584 3BB53D9B 011D8BD1 F682C0E4 D8A5E723 364364E4 0DAD1B7A 476716AC 7D1BA705 CCDD680B FD4FE473 9CC21A9A 59ED544B 82566BF6 33E89501 86A79FE3` 

- `xR31` = `00005AC5 7EAFD6CC 7569E8B5 3A148721 953262C5 B404C143 380ADCC1 84B6C21F 0CAFE095 B7E9C79C A88791F9 A72F1B2F 3121829B 2622515B 694A1687 5ED637F4 21B539E6 6F2FEF1C E8DCEFC8 AEA60805 5E9C4407 7266AB64 611BF851 BA06C821` 

### **1.6.8** `SIKEp751_compressed` 

- `p` = `00006FE5 D541F71C 0E12909F 97BADC66 8562B504 5CB25748 084E9867 D6EBE876 DA959B1A 13F7CC76 E3EC9685 49F878A8 EEAFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFF` 

- `e2` 

      - = `00000174` 

   - `e3` = `000000EF` 

- `xQ20` = `00002F42 9823758D A73CC081 3C8D2A15 5539422C C3626F96 0894A5F0 C80EB816 2757BB4F 9973B0AD 3BE80434 D2F2274B B2B67382 E963F75D 095A7F4B 2117D035 87A0253A BFECE7DA C3D05EF9 B771D1AE F9CA904C EDBFE5DD 06BDB972 1B084F9F` 

- `xQ21` = `000001EF 0F6ACD92 06BD5717 62E80C1C A9A70620 469CB867 4DC960DA A92B8DBF 4356747C 98CF6CF5 FC3868D6 6A81C877 0D1FF1E2 464E8D16 232E0F2A B97A4502 523E86E4 5695747D 7549DE8D CE950C87 1422F4AD 1C910B72 89D03AFD F60F82F6` 

31 

- `xP20` = `00002DAA 34E43B70 4940549A 6BD34F33 6869E9E3 9594567D C5D1D114 73A0905E F38A10FC 52BCCE8C 6626DB3A 14473A2D ABC9A0AE 65635619 590E3739 AEC25727 8D27A184 2DCF41DA AB8C9DC1 785E4B51 BDC11212 A65DAAF6 413E0B4B 01424D5D` 

- `xP21` = `000007C5 AD0C2460 8F54E811 A18B6C2C 38FB00A8 F10FBC51 AB3C3B01 6A98367C B1CE89FC 12583110 9517F405 517F588F FCB221D8 683750F2 D59C8D8A 4A35D14B A6B89451 5BD7E856 5CD5F779 FAFFB24C 27C9E87F FD650EF5 D6B1A59D 62367E02` 

- `xR20` = `00001F0C FC586169 3969F69E 0BB690DB 3F6F7028 CCB78EEE 62759E54 94CF24DD 007392D4 526946DB 5B856192 9B49996D D22B1AE8 D8D7F05F 9BEC60F6 750B56A0 77F5066E D3C9F67C 89DBE517 B99F7A17 5868AD6E 192470E6 18FBED50 F5EDDD87` 

- `xR21` = `000015FD 8097ACA6 9AB4F140 6445749E 9743F440 1A40E03B AD039AA3 E55803AC 88E8D7AE 9ACB6068 105AD134 E0327915 1A1BE245 82CEF065 03295CEB 3F278799 D02E3C8E E0EB62BE BFE133F8 E31F83C4 B4CD6093 7DD1D191 83A7AB9F 04FF9AF6` 

- `xQ30` = `000049E7 19883EE7 671DC6B2 E480C96C F1B38889 3E510957 A2BA76CB 65916AD7 6751440F E9A2ED54 2C82B09A 7E81BE06 97A1D7E9 D6EFEC66 19CAAC92 9BDE6EB6 3AF379DF 8F290BBD AE3E8ECE 23C125E9 BAB87AA5 F1248050 DA1AF4F4 0B74B755` 

- `xQ31` = `00003047 02CEB5C2 F0B4B99C CAD5DFB6 66DB825D 662A3A34 A40E79C6 9CEAB5FC 7374C1EF A6F1A465 F7C90CB2 45CD8A32 BC2B560F 1FE20740 7DD86656 7C6981A3 EE57971A FC29AABA C22EB799 F946B2E4 287C45C1 80DE6D62 FA4FF221 9900C63A` 

- `xP30` = `000049E7 19883EE7 671DC6B2 E480C96C F1B38889 3E510957 A2BA76CB 65916AD7 6751440F E9A2ED54 2C82B09A 7E81BE06 97A1D7E9 D6EFEC66 19CAAC92 9BDE6EB6 3AF379DF 8F290BBD AE3E8ECE 23C125E9 BAB87AA5 F1248050 DA1AF4F4 0B74B755` 

- `xP31` = `00003F9E D2734159 1D5DD702 CCE4FCB0 1E8732A6 F6881D13 64401EA1 3A01327A 6720D92A 6D062810 EC2389D3 042AEE76 3284A9F0 E01DF8BF 822799A9 83967E5C 11A868E5 03D65545 3DD14866 06B94D1B D783BA3E 7F21929D 05B00DDE 66FF39C5` 

- `xR30` = `0000193E 2242DBEF FD930260 70F635B4 73459058 55C22F21 2E26946E D8C84DFB 38C592AD C076400A 788DEE67 D6462706 64D4BFF7 78C48446 0250AE93 05D89BF3 832239B1 38D6D099 AD26B99C 5C83CE75 C20CDB7F 3FA01029 EDE53E4A B3B4DFD6` 

- `xR31` = `00000000` 

32 

33 

# **Chapter 2** 

# **Chapter 3** 

# **Chapter 4** 

# **Expected security strength** 

## **4.1 Security** 

The security of `SIKE` informally relies on the _(supersingular) isogeny walk problem_ : given two elliptic curves _E_ , _E_<sup>′</sup> in the same isogeny class, find a path made of isogenies of small degree between _E_ and _E_<sup>′</sup> . 

The isogeny walk problem has been considered in the literature even before the introduction of isogenybased cryptography. The best generic algorithm currently known is due to Galbraith [19]: it is a meetin-the-middle strategy that, on average, requires a number of elementary steps proportional to the square root of the size of the isogeny class of _E_ and _E_<sup>′</sup> . In the supersingular case, an improvement due to Delfs and Galbraith [15] has roughly the same computational complexity, but only uses a constant amount of memory. 

Over F _p_ 2, there is a unique isogeny class of supersingular elliptic curves (up to twist), and it has size roughly _p_ /12. Thus, the algorithm of Delfs and Galbraith would find an isogeny between the starting curve _E_ 0 and a public curve _E_<sup>′</sup> in _O_ (<sup>~~√~~</sup> _<u>p</u>_ ) time.<sup>1</sup> Nevertheless, these generic algorithms do not improve upon exhaustive search. Indeed, if _p_ = 2<sup>_e_2</sup> · 3<sup>_e_3</sup> − 1, the key spaces K2 and K3 have sizes roughly 2<sup>_e_2</sup> and 3<sup>_e_3</sup> ; thus, if these are chosen to balance out, then the size of the key spaces is roughly<sup>~~√~~</sup> _<u>p</u>_ . 

However, the idea of Galbraith’s meet-in-the-middle approach can be easily adapted to attack SIKE in only _O_ (<sup>√4</sup> _<u>p</u>_ <u>) operations.</u> To find the secret isogeny of degree ℓ<sup>_e_ℓ</sup> between _E_ 0 and _E_<sup>′</sup> , an attacker builds a tree of all curves isogenous to _E_ 0 via isogenies of degree ℓ<sup>_e_ℓ/2</sup> , and a similar tree of all curves isogenous to _E_<sup>′</sup> of degree ℓ<sup>_e_ℓ/2</sup> . Since we suppose that an isogeny of degree ℓ<sup>_e_ℓ</sup> exists between _E_ 0 and _E_<sup>′</sup> , and since the length of this walk is much shorter than the size of the graph, with high probability the two trees will have exactly one curve _E_<sup>′′</sup> in common, so the secret isogeny will be recovered by composing the paths _E_ 0 → _E_<sup>′′</sup> and _E_<sup>′′</sup> → _E_<sup>′</sup> . This procedure only requires _O_ ( √ℓ<sup>_e_ℓ</sup> ) elementary steps, or _O_ (<sup>~~√~~4</sup> _<u>p</u>_ <u>), as announced.</u> 

Given two functions _f_ : _A_ → _C_ and _g_ : _B_ → _C_ with domain of equal size, finding a pair ( _a_ , _b_ ) such that _f_ ( _a_ ) = _g_ ( _b_ ) is known as the _claw problem_ in complexity theory. The claw problem can obviously be solved using _O_ (| _A_ | + | _B_ |) invocations of _f_ and _g_ on average, by building a hash table holding _f_ ( _a_ ) for any _a_ ∈ _A_ 

> 1The attentive reader will have noticed that knowing a generic path between _E_ 0 and _E_ ′ is not necessarily equivalent to knowing the secret path generated by `isogen` ℓ. However, a complete reduction of the security of SIKE to the isogeny walk problem is presented in [21]. 

46 

and looking for hits for _g_ ( _b_ ) where _b_ ∈ _B_ . However, one can do better with a quantum computer using Tani’s claw-finding algorithm [54], which only uses _O_ (<sup>~~√~~</sup> 3 | _A_ || _B_ |) invocations to quantum oracles for _f_ and _g_ . These complexities are optimal for a black-box claw attack [60]. For given supersingular curves _E_ , _E_<sup>′</sup> we could, for example, let _A_ resp. _B_ be the set of points of order exactly ℓ<sup>_e_ℓ/2</sup> on _E_ resp. _E_<sup>′</sup> , and _C_ the set of supersingular _j_ -invariants. The functions _f_ and _g_ compute ℓ<sup>_e_ℓ/2</sup> -isogenies which have kernels generated by their input points and return the _j_ -invariant of the final curve. Classically this is exactly the _O_ ( √ℓ<sup>_e_ℓ</sup> )<sup>~~√~~</sup> 3 attack described above, and applying Tani’s algorithm to `SIKE` gives an attack requiring _O_ ( ℓ<sup>_e_ℓ</sup> ) = _O_ (<sup>√6</sup> _<u>p</u>_ <u>)</u> invocations of a quantum isogeny computation oracle. 

While the generic algorithms described above (and their asymptotic complexities) were used for the security analysis in the initial `SIKE` proposal, a series of subsequent papers beginning with [1] have since argued that the parallel collision finding algorithm of van Oorschot and Wiener [57] is the best classical claw-finding attack on `SIKE` , and [27] even argues that the above query-optimal instantiation of Tani’s algorithm is outperformed by the classical van Oorschot and Wiener algorithm. We further discuss the concrete security of `SIKE` in Chapter 5. 

We stress that, while breaking `SIKE` keys can be reduced to claw finding, no reduction is known in the opposite direction, nor is it widely believed that such a reduction should exist. The security of `SIKE` is modeled after a much more specific problem named SIDH (see Problem 1). In particular the knowledge of the coordinates ( _x_ 1, _x_ 2, _x_ 3) output by `isogen` ℓ apparently gives more information than what is available in the claw problem. Nevertheless, to this day no attack seems to be able to exploit this auxiliary knowledge against `SIKE` . For this reason, we assume that the security of the claw problem and SIDH are equivalent, and analyze security accordingly. 

## **4.2 Other attacks** 

Other attacks applying to specific security models have appeared in the literature in recent years. 

Galbraith, Petit, Shani and Ti [21] exhibit a very efficient polynomial-time attack against SIDH with static keys. Their technique is readily adapted to a chosen ciphertext attack against the scheme `PKE` . However, their attack does not apply to `KEM` , as we will prove in the next section that the scheme is CCA secure. 

Many authors have considered the security of SIDH under various side-channel scenarios: 

- Galbraith, Petit, Shani and Ti [21] show how a secret _j_ -invariant can be recovered from some partial knowledge of it. 

- Ti [56] explains how a random perturbation to the inputs of `isogen` ℓ yields to a key recovery with very high probability in most protocols derived from SIDH. It is not clear, however, how the technique can be used against the public key format specified in 1.2.9. 

- Gélin and Wesolowski [22] present a loop-abort fault attack that potentially leads to an efficient key recovery against the “simple” version of `isogen` ℓ given in Algorithms 17 and 18. However their attack is efficiently countered by the additional checks in Algorithms 19 and 20. 

47 

A recent preprint by Petit [43] presents various polynomial-time attacks against generalizations of SIDH. None of the systems successfully attacked by Petit had previously appeared in the literature, and in particular the schemes presented in this document are not affected by the attack. It is not clear that Petit’s attacks could possibly be extended to break real uses of SIDH and derived schemes. The technique employed by Petit, however, sheds some light on the separation between the isogeny walk problem and the possibly (though not yet shown to be) easier SIDH problem. 

Even more recently, Petit and Lauter [44] showed that the isogeny walk problem used to construct the Charles-Goren-Lauter hash function [7] is equivalent to the problem of computing endomorphism rings of supersingular elliptic curves, which is possibly (but not yet shown to be) harder than the SIDH problem. However, it does not appear to be possible to extend the Charles-Goren-Lauter hash construction to yield key exchange. 

# **Chapter 5** 

# **Analysis with respect to known attacks** 

In choosing concrete parameter sizes, our goal is to ensure that the computational cost of breaking `SIKEpXXX` , where `XXX` ∈{434, 610, 751}, requires respective resources comparable to those required for key search on a _k_ -bit (ideal) block cipher B, where _k_ ∈{128, 192, 256}. In addition, our goal is to ensure that the computational cost of breaking `SIKEp503` requires resources comparable to those required for collision search on a 256-bit (ideal) hash function. 

We discuss the complexity of the best known classical attacks in §5.1 and the complexity of the best known quantum attacks in §5.2. Side-channel attacks are discussed in §5.3. 

## **5.1 Classical security** 

Following the submission of SIKE to the NIST call in November of 2017, a series of papers have emerged that have scrutinized the application of generic meet-in-the-middle attacks described in §4.1. The work of Adj, Cervantes-Vázquez, Chi-Domínguez, Menezes and Rodríguez-Henríquez [1] was the first paper to argue that the parallel collision-finding algorithm of van Oorschot and Wiener (vOW) [57] is actually the attack that should be used to evaluate the security of SIKE. The reason is that the _O_ ( _p_<sup>1/4</sup> ) memory that is required to mount the generic meet-in-the-middle attack — that which runs in _O_ ( _p_<sup>1/4</sup> ) time — is far beyond feasible for SIKE parameters in the ranges of interest. Since the best known generic attack against ideal block ciphers (e.g., AES) use only a moderate amount of memory, in deriving SIKE parameters for which the computational resources are comparable to AES instantiations, the most appropriate model is to fix an upper bound on the classical memory available, and to evaluate the runtime of the best known attacks subject to this limit. 

Under the assumption that the memory available permits the storage of 2<sup>80</sup> _units_ , Adj et al. [1] conclude that `SIKEp434` and `SIKEp610` meet the respective security requirements of NIST’s categories 2 and 4. A subsequent paper by Jaques and Schanck [27] — which is largely geared towards the analysis of quantum algorithms, but also considers vOW — further endorses the classical complexity claims of Adj et al with respect to these two curves and the NIST requirements they satisfy. And, in addition to a further endorsement of these two curves, a recent paper by Costello, Longa, Naehrig, Renes and Virdia [11] argues that `SIKEp751` , which was initially proposed to meet level 3, actually meets NIST’s category 5 requirements. 

50 

We refer to these three papers (and the original vOW paper) for the in-depth analyses, but we summarize their application to three SIKE parameterizations in Table 5.1, noting that they use slightly different memory assumptions and/or cost metrics in order to estimate the complexity of vOW against SIKE parameters. Adj et al. assume that the memory permits the storage of 2<sup>80</sup> units, and present their results in “total time”, where the unit of time is actually the time complexity of a degree ℓ<sup>_e_/2</sup> -isogeny; thus, although their _times_ fall slightly below NIST’s required _gate counts_ , the corresponding conversion to gate counts would see these parameters comfortably exceed NIST’s requirements. The classical analysis of Jaques and Schanck uses the PRAM model and estimates the number of classical gates under the assumption that the memory is 2<sup>96</sup> bits. Their model does incorporate the cost of the isogeny computations, but is still rather conservative. Finally, the vOW analysis of Costello et al. estimates the total number of x64 instructions required to mount the vOW attack, and argues that this is also a conservative lower bound on the true classical gate count. In particular, for the `SIKEp751` parameterization, they conclude that the true gate count corresponding to their estimated 2<sup>262</sup> x64 instructions would exceed NIST’s 2<sup>272</sup> gate count requirement. 

||Target<br>level|Classical gate<br>requirement|Clas<br>Total time|sical security estim<br>Gates|ates<br>x64 instructions|
|---|---|---|---|---|---|
|||[55]|[1]<br>memory 2<sup>80 </sup>units|[27, Fig. 4(d)]<br>memory 2<sup>96 </sup>bits|[11]<br>memory 2<sup>80 </sup>units|
|`SIKEp434`|1|143|128|142|143|
|`SIKEp503`|2|146|152|169<sup>∗</sup>|169<sup>∗</sup>|
|`SIKEp610`|3|207|189|209|210|
|`SIKEp751`|5|272|-|263<sup>∗</sup>|262|

Table 5.1: Classical security estimates of the three SIKE parameterizations according to Adj et al. [1], Jaques and Schanck [27], and Costello et al. [11]. Gate requirements and classical security estimates are all expressed as their base-2 logarithms. The values marked with (*) are not found in the actual papers. In the case of [11], we obtained the numbers for `SIKEp503` using their scripts, where (for the half-sized isogenies used in vOW) the optimal strategy for the 2-torsion resulted in 362 doublings and 189 4-isogenies, and the optimal strategy for the 3-torsion yielded 229 triplings and 275 3-isogenies. In the former scenario, a vOW isogeny required over 2<sup>22</sup> x64 instructions, and in the latter, over 2<sup>23</sup> x64 instructions. In the case of [27], the RAM operations for `SIKEp503` and `SIKEp751` were taken from the width-restricted table in §5.2. 

## **5.2 Quantum security** 

The initial `SIKE` proposal used the asymptotic complexity of Tani’s quantum claw-finding algorithm [54] together with crude lower bounds for the number of quantum gates used in an F _p_ -multiplication and the number of such multiplications in a typical isogeny computation to provide conservative resource estimates for the cost of quantum cryptanalysis of `SIKE` . The recent paper by Jaques and Schanck [27] conducts a much more detailed analysis of the best known quantum algorithms to solve the computational supersingular isogeny problem. Jaques and Schanck propose a model of quantum computation that allows 

51 

a direct comparison between quantum and classical algorithms. They treat qubit registers as memory peripherals for classical control processors, which run quantum circuits through RAM operations on qubit memory peripherals. This allows them to use the number of RAM operations as the algorithm’s cost function, derived either from the quantum gate count in a quantum circuit or the product of its depth and width. The crucial difference to previous cost estimates lies in considering the complexity of implementing and querying quantum memory. 

Jaques and Schanck consider both Tani’s algorithm as well as a direct application of Grover’s algorithm to the claw-finding problem, but also include the purely classical vOW algorithm. Their analysis provides various trade-offs between time, memory and RAM operations, which lead to the preference of different algorithm parameterizations depending on the given attack constraints. They conclude that in a scenario with limited memory, quantum algorithms promise to be more efficient, but that the classical vOW algorithm outperforms quantum algorithms for attackers with limited time. Therefore, in some scenarios, 

security against classical attacks is the limiting factor for selecting parameters. In particular, it is argued that the classical hardware required to run the query-optimal parameterization of Tani’s algorithm can be used to break `SIKE` faster by running the classical vOW algorithm on that same hardware. 

Figure 4 in [27] provides concrete cost estimates for solving the computational supersingular isogeny problem in different scenarios for the parameters `SIKEp434` and `SIKEp610` . The relevant constraint for matching the NIST security categories is imposing a depth restriction on quantum circuits between 2<sup>64</sup> and 2<sup>96</sup> (corresponding to the MAXDEPTH parameter in the NIST call for proposals [55]). Allowing depth 2<sup>96</sup> , Jaques and Schanck conclude that no known quantum algorithm can break `SIKE` in their model of computation with less than 2<sup>143</sup> classical gates and 2<sup>207</sup> classical gates for `SIKEp434` and `SIKEp610` , respectively. Therefore, these two parameter sets are suitable for NIST categories 1 and 3. Running the scripts accompanying [27] to produce the same tables for `SIKEp503` and `SIKEp751` suggest that no quantum algorithm can break those with less than 2<sup>146</sup> and 2<sup>272</sup> classical gates, respectively, which confirms that these parameter sets are suitable for NIST categories 2 and 5. 

Tables 5.2, 5.3, 5.4 and 5.5 were obtained with the methodology from [27], including all `SIKE` parameter sets<sup>1</sup> . They show the base-2 logarithm of the classical gate count costs (G) and the corresponding depth (D) and width (W) for a specific parameterisation of a given algorithm. The algorithms considered are a direct application of Grover search, Tani’s claw-finding algorithm and the classical van Oorschot-Wiener collision search algorithm (vOW). Table 5.2 shows results when the depth is restricted to either 2<sup>64</sup> or 2<sup>96</sup> . This corresponds to the NIST model for quantum computation. In this case, the classical vOW algorithm does not show the optimal gate count, but instead minimizes the memory (width) with the given depth restriction. Table 5.3 instead restricts the width of the algorithm to either 2<sup>64</sup> or 2<sup>96</sup> . Tables 5.4 and 5.5 show the gate cost optimal and the depth-width cost optimal settings. It should be noted that these 

parameterizations either violate a reasonable depth or width constraint. 

**5.3 Side-channel attacks** 

Side-channel analysis targets various physical phenomena that are emitted by a cryptographic implementation to reveal critical internal information of the device. Power consumption information, timing information, and electromagnetic radiation are all emitted externally as cryptographic computations are 

1Sam Jaques kindly produced these tables for us with the scripts used to generate the tables in [27]. 

52 

||`SI`|`KEp4`|`34`|`SI`|`KEp5`|`03`|`SI`|`KEp6`|`10`|`SI`|`KEp7`|`51`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Algorithm|_G_|_D_|_W_|_G_|_D_|_W_|_G_|_D_|_W_|_G_|_D_|_W_|
|Grover|190|64|127|226|64|162|280|64|216|352|64|288|
|Tani|175|63|126|210|64|161|264|64|216|336|63|288|
|vOW|145|64|91|162|63|109|189|63|136|225|63|173|
|Grover|158|96|63|194|96|98|248|96|152|320|96|224|
|Tani|143|95|62|178|96|97|232|96|152|304|95|224|
|vOW|155|95|70|173|95|88|200|95|115|236|96|151|

Table 5.2: Cost estimates for algorithms to solve the computational supersingular isogeny problem on `SIKE` parameter sets with depth constraints. The first three lines restrict to maximal depth close to 2<sup>64</sup> , the last three to 2<sup>96</sup> . 

||`SI`|`KEp43`|`4`|`SI`|`KEp50`|`3`|`SI`|`KEp61`|`0`|`SI`|`KEp75`|`1`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Algorithm|_G_|_D_|_W_|_G_|_D_|_W_|_G_|_D_|_W_|_G_|_D_|_W_|
|Grover|159|95|64|177|113|64|204|140|64|240|176|64|
|Tani|144|94|64|162|112|65|188|140|64|224|175|64|
|vOW|158|104|64|185|131|64|225|172|64|279|226|64|
|Grover|175|79|96|193|97|96|220|124|96|256|160|96|
|Tani|160|78|96|178|96|97|204|124|96|240|159|96|
|vOW|142|56|96|169|83|96|209|124|96|263|178|96|

Table 5.3: Cost estimates for algorithms to solve the computational supersingular isogeny problem on `SIKE` parameter sets with width constraints. The first three lines restrict to maximal width close to 2<sup>64</sup> , the last three to 2<sup>96</sup> . 

||`SI`|`KEp43`|`4`|`SI`|`KEp5`|`03`|`SI`|`KEp6`|`10`|`SI`|`KEp7`|`51`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Algorithm|_G_|_D_|_W_|_G_|_D_|_W_|_G_|_D_|_W_|_G_|_D_|_W_|
|Grover|132|122|10|150|140|10|177|167|10|213|202|11|
|Tani|124|114|25|142|132|25|169|159|25|205|194|27|
|vOW|132|14|128|150|15|145|177|14|173|213|16|208|

Table 5.4: Cost estimates for algorithms to solve the computational supersingular isogeny problem on `SIKE` parameter sets optimizing _G_ -cost. 

53 

||`SI`|`KEp43`|`4`|`SI`|`KEp50`|`3`|`SI`|`KEp6`|`10`|`S`|`IKEp7`|`51`|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Algorithm|_G_|_D_|_W_|_G_|_D_|_W_|_G_|_D_|_W_|_G_|_D_|_W_|
|Grover|132|122|10|150|140|10|177|167|10|213|202|11|
|Tani|131|122|10|149|139|10|177|166|10|213|202|11|
|VW|132|14|128|150|15|145|177|14|173|213|16|208|

Table 5.5: Cost estimates for algorithms to solve the computational supersingular isogeny problem on `SIKE` parameter sets optimizing _DW_ -cost. 

performed. Simple power analysis (SPA) analyzes a single power signature of a device, while differential power analysis (DPA) statistically analyzes many power runs of a device. Timing analysis targets timing information of various portions of the computation. Electromagnetic radiation can be seen as an extension of power analysis attacks by analyzing electromagnetic emissions instead of power. 

In general, isogeny-based cryptography comes down to two computations: generation of a secret kernel and computing a large-degree isogeny over that kernel. In schemes like SIKE, the secret kernel is found by computing a double-point multiplication over a torsion basis. Thus, there are 2 general approaches an attacker can exploit to attack the security of the cryptosystem via side-channel analysis: 

1. Reveal parts of the hidden kernel point, 

2. Reveal secret isogeny walks during the isogeny computation. 

Regarding the first approach, a double-point multiplication over a torsion basis is used to compute the hidden kernel. This computation shares many similarities with traditional elliptic curve cryptography. Accordingly, existing techniques for elliptic curve cryptography side-channel attacks can be applied to reveal information about this ladder and what kind of hidden kernel point was generated. Further, invalid parameters may be injected by providing an invalid torsion basis or invalid curve, thus limiting the possible number of valid kernel points of full isogeny order. 

For the second approach, the hidden kernel point is used to perform various walks of small degree on an isogeny graph. If an attacker can identify specific walks used during this computation, then the attacker has a subset of the isogeny computation between two distant isomorphism classes and the security of SIKE is weakened. As this part of the computation has no analogue in traditional ECC, this category of side-channels attacks is being actively investigated by the research community. 

In targeting these parts of the SIKE cryptosystem, an attacker no doubt has access to a wide range of power, timing, fault, and various other side-channels. Constant-time implementations using a constant set of operations has been shown to be a good countermeasure against SPA and timing attacks. Higher level differential power analysis attacks and fault injection attacks are much harder to defend against. Papers and publications describing side-channel attacks against SIKE and countermeasures include [22, 32, 33, 56]. We remark that most, if not all, post-quantum cryptosystems are vulnerable to side-channel attacks to some extent, and research in this area is extremely active. 

54 

# **Chapter 6** 

# **Appendix A** 

#### **Algorithm 3:** Coordinate doubling 

**function** `xDBL` **Input:** ( _XP_ : _ZP_ ) and ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24)</sup> **Output:** ( _X_ [2] _P_ : _Z_ [2] _P_ ) 

62 

#### **Algorithm 4:** Repeated coordinate doubling 

##### **function** `xDBLe` 

**Input:** ( _XP_ : _ZP_ ), ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24), and</sup><sup>_e_∈Z</sup> **Output:** ( _X_ [2<sup>_e_</sup> ] _P_ : _Z_ [2<sup>_e_</sup> ] _P_ ) 

```
//Alg.3
```

#### **Algorithm 5:** Combined coordinate doubling and differential addition 

##### **function** `xDBLADD` 

**Input:** ( _XP_ : _ZP_ ), ( _XQ_ : _ZQ_ ), ( _XQ_ − _P_ : _ZQ_ − _P_ ), and ( _a_<sup>+</sup> 24<sup>: 1) ∼(</sup><sup>_A_+ 2</sup><sup>_C_: 4</sup><sup>_C_)</sup> **Output:** ( _X_ [2] _P_ : _Z_ [2] _P_ ), ( _XP_ + _Q_ : _ZP_ + _Q_ ) 

**1** _t_ 0 ← _XP_ + _ZP_ **8** _t_ 1 ← _t_ 1 · _XP_ + _Q_ **15** _Z_ [2] _P_ ← _Z_ [2] _P_ · _t_ 2 **2** _t_ 1 ← _XP_ − _ZP_ **9** _t_ 2 ← _X_ [2] _P_ − _Z_ [2] _P_ **16** _ZP_ + _Q_ ← _ZP_<sup>2</sup> + _Q_ **3** _X_ [2] _P_ ← _t_ 0<sup>2</sup> **10** _X_ [2] _P_ ← _X_ [2] _P_ · _Z_ [2] _P_ **17** _XP_ + _Q_ ← _XP_<sup>2</sup> + _Q_ **4** _t_ 2 ← _XQ_ − _ZQ_ **11** _XP_ + _Q_ ← _a_<sup>+</sup> 24<sup>·</sup><sup>_t_2</sup> **18** _ZP_ + _Q_ ← _XQ_ − _P_ · _ZP_ + _Q_ **5** _XP_ + _Q_ ← _XQ_ + _ZQ_ **12** _ZP_ + _Q_ ← _t_ 0 − _t_ 1 **19** _XP_ + _Q_ ← _ZQ_ − _P_ · _XP_ + _Q_ **6** _t_ 0 ← _t_ 0 · _t_ 2 **13** _Z_ [2] _P_ ← _XP_ + _Q_ + _Z_ [2] _P_ **20 return** {( _X_ [2] _P_ : _Z_ [2] _P_ ), **7** _Z_ [2] _P_ ← _t_ 1<sup>2</sup> **14** _XP_ + _Q_ ← _t_ 0 + _t_ 1 ( _XP_ + _Q_ : _ZP_ + _Q_ )} 

#### **Algorithm 6:** Coordinate tripling 

##### **function** `xTPL` 

63 

#### **Algorithm 7:** Repeated coordinate tripling 

**function** `xTPLe` 

**Input:** ( _XP_ : _ZP_ ), ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>), and</sup><sup>_e_∈Z+</sup> **Output:** ( _X_ [3<sup>_e_</sup> ] _P_ : _Z_ [3<sup>_e_</sup> ] _P_ ) 

**1** ( _X_<sup>′</sup> : _Z_<sup>′</sup> ) ← ( _XP_ : _ZP_ ) 

**4 return** ( _X_<sup>′</sup> : _Z_<sup>′</sup> ) 

#### **Algorithm 8:** Three point ladder 

**function** `Ladder3pt` **Input:** _m_ = ( _m_ ℓ−1, . . . , _m_ 0)2 ∈ Z, ( _xP_ , _xQ_ , _xQ_ − _P_ ), and ( _A_ : 1) **Output:** ( _XP_ +[ _m_ ] _Q_ : _ZP_ +[ _m_ ] _Q_ ) **1**<sup>�</sup> ( _X_ 0 : _Z_ 0),),, ( _X_ 1 : _Z_ 1),),, ( _X_ 2 : _Z_ 2))<sup>�</sup> ←<sup>�</sup> ( _xQQ_ : 1),, ( _xPP_ : 1),, ( _xQQ_ − _P_ : 1)<sup>�</sup> **2** _a_<sup>+</sup> 24<sup>←(</sup><sup>_A_+ 2)/4</sup> **3 for** _i_ = 0 **to** ℓ − 1 **do 4 if** _mi_ = 1 **then 5** �( _X_ 0 : _Z_ 0), ( _X_ 1 : _Z_ 1)� ← `xDBLADD` �( _X_ 0 : _Z_ 0), ( _X_ 1 : _Z_ 1), ( _X_ 2 : _Z_ 2), ( _a_ +24<sup>: 1)�</sup> `// Alg. 5` **6 else 7** �( _X_ 0 : _Z_ 0), ( _X_ 2 : _Z_ 2)� ← `xDBLADD` �( _X_ 0 : _Z_ 0), ( _X_ 2 : _Z_ 2), ( _X_ 1 : _Z_ 1), ( _a_ +24<sup>: 1)�</sup> `// Alg. 5` 

**1**<sup>�</sup> ( _X_ 0 : _Z_ 0),),, ( _X_ 1 : _Z_ 1),),, ( _X_ 2 : _Z_ 2))<sup>�</sup> ←<sup>�</sup> ( _xQQ_ : 1),, ( _xPP_ : 1),, ( _xQQ_ − _P_ : 1)<sup>�</sup> 

**8 return** ( _X_ 1 : _Z_ 1) 

#### **Algorithm 9:** Montgomery _<u>j</u>_ -invariant computation 

64 

#### **Algorithm 10:** Recovering the Montgomery curve coefficient 

##### **function** `get_A` 

**Input:** _xP_ , _xQ_ and _xQ_ − _P_ corresponding to points on _EA_ : _y_<sup>2</sup> = _x_<sup>3</sup> + _Ax_<sup>2</sup> + _x_ 

**Output:** _A_ ∈ F _p_ 2 

**1** _t_ 1 ← _xP_ + _xQ_ **5** _t_ 0 ← _t_ 0 · _xQ_ − _P_ **9** _t_ 0 ← _t_ 0 + _t_ 0 **13** _A_ ← _A_ − _t_ 1 **2** _t_ 0 ← _xP_ · _xQ_ **6** _A_ ← _A_ − 1 **10** _A_ ← _A_<sup>2</sup> **14 return** _A_ **3** _A_ ← _xQ_ − _P_ · _t_ 1 **7** _t_ 0 ← _t_ 0 + _t_ 0 **11** _t_ 0 ← 1/ _t_ 0 **4** _A_ ← _A_ + _t_ 0 **8** _t_ 1 ← _t_ 1 + _xQ_ − _P_ **12** _A_ ← _A_ · _t_ 0 

#### **Algorithm 11:** Computing the 2-isogenous curve 

**function** `2_iso_curve` 

**Input:** ( _XP_ 2 : _ZP_ 2), where _P_ 2 has exact order 2 on _EA_ / _C_ 

**Output:** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24) ∼(</sup><sup>_A_′ + 2</sup><sup>_C_′: 4</sup><sup>_C_′) corresponding to</sup><sup>_EA_′/</sup><sup>_C_′=</sup><sup>_EA_/</sup><sup>_C_/⟨</sup><sup>_P_2⟩</sup> 

#### **Algorithm 12:** Evaluating a 2-isogeny at a point 

**function** `2_iso_eval` 

**Input:** ( _XP_ 2 : _ZP_ 2), where _P_ 2 has exact order 2 on _EA_ / _C_ , and ( _XQ_ : _ZQ_ ) where _Q_ ∈ _EA_ / _C_ 

**Output:** ( _XQ_<sup>′</sup> : _ZQ_<sup>′</sup> ) corresponding to _Q_<sup>′</sup> ∈ _EA_<sup>′</sup> / _C_<sup>′</sup> , where _EA_<sup>′</sup> / _C_<sup>′</sup> is the curve 2-isogenous to _EA_ / _C_ output from `2_iso_curve` 

#### **Algorithm 13:** Computing the 4-isogenous curve 

**function** `4_iso_curve` 

**Input:** ( _XP_ 4 : _ZP_ 4), where _P_ 4 has exact order 4 on _EA_ / _C_ 

- **Output:** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24) ∼(</sup><sup>_A_′ + 2</sup><sup>_C_′: 4</sup><sup>_C_′) corresponding to</sup><sup>_EA_′/</sup><sup>_C_′=</sup><sup>_EA_/</sup><sup>_C_/⟨</sup><sup>_P_4⟩, and constants</sup> ( _K_ 1, _K_ 2, _K_ 3) ∈ (F _p_ 2)<sup>3</sup> 

65 

#### **Algorithm 14:** Evaluating a 4-isogeny at a point 

##### **function** `4_iso_eval` 

**Input:** Constants ( _K_ 1, _K_ 2, _K_ 3) ∈ (F _p_ 2)<sup>3</sup> from `4_iso_curve` , and ( _XQ_ : _ZQ_ ) where _Q_ ∈ _EA_ / _C_ **Output:** ( _XQ_<sup>′</sup> : _ZQ_<sup>′</sup> ) corresponding to _Q_<sup>′</sup> ∈ _EA_<sup>′</sup> / _C_<sup>′</sup> , where _EA_<sup>′</sup> / _C_<sup>′</sup> is the curve 4-isogenous to _EA_ / _C_ output from `4_iso_curve` **1** _t_ 0 ← _XQ_ + _ZQ_ , **5** _t_ 0 ← _t_ 0 · _t_ 1 , **9** _t_ 1 ← _t_ 1<sup>2,</sup> **13** _XQ_<sup>′</sup> ← _XQ_ · _t_ 1 , **2** _t_ 1 ← _XQ_ − _ZQ_ , **6** _t_ 0 ← _t_ 0 · _K_ 1 , **10** _ZQ_ ← _ZQ_<sup>2,</sup> **14** _ZQ_<sup>′</sup> ← _ZQ_ · _t_ 0 , **3** _XQ_ ← _t_ 0 · _K_ 2 , **7** _t_ 1 ← _XQ_ + _ZQ_ , **11** _XQ_ ← _t_ 0 + _t_ 1 , **15 return** ( _XQ_<sup>′</sup> : _ZQ_<sup>′</sup> ) **4** _ZQ_ ← _t_ 1 · _K_ 3 , **8** _ZQ_ ← _XQ_ − _ZQ_ , **12** _t_ 0 ← _ZQ_ − _t_ 0 , 

#### **Algorithm 15:** Computing the 3-isogenous curve 

#### **Algorithm 16:** Evaluating a 3-isogeny at a point 

##### **function** `3_iso_eval` 

**Input:** Constants ( _K_ 1, _K_ 2) ∈ (F _p_ 2)<sup>3</sup> output from `3_iso_curve` together with ( _XQ_ : _ZQ_ ) corresponding to _Q_ ∈ _EA_ / _C_ 

**Output:** ( _XQ_<sup>′</sup> : _ZQ_<sup>′</sup> ) corresponding to _Q_<sup>′</sup> ∈ _EA_<sup>′</sup> / _C_<sup>′</sup> , where _EA_<sup>′</sup> / _C_<sup>′</sup> is 3-isogenous to _EA_ / _C_ 

66 

#### **Algorithm 17:** Computing and evaluating a 2<sup>_e_</sup> -isogeny, simple version 

**function** `2_e_iso` **Static parameters:** Integer `e2` from the public parameters **Input:** Constants ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24) corresponding to a curve</sup><sup>_EA_/</sup><sup>_C_, (</sup><sup>_XS_:</sup><sup>_ZS_) where</sup><sup>_S_has exact order</sup> 2<sup>`e2`</sup> on _EA_ / _C_ **Optional input:** ( _X_ 1 : _Z_ 1), ( _X_ 2 : _Z_ 2) and ( _X_ 3 : _Z_ 3) on _EA_ / _C_ **Output:** ( _A_<sup>+</sup> 24′ : _C_ 24′<sup>) corresponding to the curve</sup><sup>_EA_′/</sup><sup>_C_′=</sup><sup>_E_/⟨</sup><sup>_S_⟩</sup> **Optional output:** ( _X_ 1<sup>′:</sup><sup>_Z_</sup> 1<sup>′), (</sup><sup>_X_</sup> 2<sup>′:</sup><sup>_Z_</sup> 2<sup>′) and (</sup><sup>_X_</sup> 3<sup>′:</sup><sup>_Z_</sup> 3<sup>′) on</sup><sup>_EA_′/</sup><sup>_C_′</sup> 

**1 for** _e_ = `e2` − 2 **downto** 0 **by** −2 **do 2** ( _XT_ : _ZT_ ) ← `xDBLe` �( _XS_ : _ZS_ ), ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24),</sup><sup>_e_</sup> � `// Alg. 4` **3** �( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24), (</sup><sup>_K_1,</sup><sup>_K_2,</sup><sup>_K_3)</sup> � ← `4` _ `iso` _ `curve` (( _XT_ : _ZT_ )) `// Alg. 13` **4 if** _e_ � 0 **then 5** ( _XS_ : _ZS_ ) ← `4` _ `iso` _ `eval` (( _K_ 1, _K_ 2, _K_ 3), ( _XS_ : _ZS_ )) `// Alg. 14` **6 for** ( _X j_ : _Z j_ ) **in** _optional input_ **do 7** ( _X j_ : _Z j_ ) ← `4` _ `iso` _ `eval` �( _K_ 1, _K_ 2, _K_ 3), ( _X j_ : _Z j_ )� `// Alg. 14` **8 return** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24), �(</sup><sup>_X_1:</sup><sup>_Z_1), (</sup><sup>_X_2:</sup><sup>_Z_2), (</sup><sup>_X_3:</sup><sup>_Z_3)�</sup> 

67 

#### **Algorithm 18:** Computing and evaluating a 3<sup>_e_</sup> -isogeny, simple version 

**function** `3_e_iso` 

**Static parameters:** Integer `e3` from the public parameters **Input:** Constants ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>) corresponding to a curve</sup><sup>_EA_/</sup><sup>_C_, (</sup><sup>_XS_:</sup><sup>_ZS_) where</sup><sup>_S_has exact order</sup> 3<sup>`e3`</sup> on _EA_ / _C_ **Optional input:** ( _X_ 1 : _Z_ 1), ( _X_ 2 : _Z_ 2) and ( _X_ 3 : _Z_ 3) on _EA_ / _C_ ′ − ′ **Output:** ( _A_<sup>+</sup> 24 : _A_ 24 ) corresponding to the curve _EA_ ′/ _C_ ′ = _E_ /⟨ _S_ ⟩ **Optional output:** ( _X_ 1<sup>′:</sup><sup>_Z_</sup> 1<sup>′), (</sup><sup>_X_</sup> 2<sup>′:</sup><sup>_Z_</sup> 2<sup>′) and (</sup><sup>_X_</sup> 3<sup>′:</sup><sup>_Z_</sup> 3<sup>′) on</sup><sup>_EA_′/</sup><sup>_C_′</sup> **1 for** _e_ = `e3` − 1 **downto** 0 **by** −1 **do 2** ( _XT_ : _ZT_ ) ← `xTPLe` �( _XS_ : _ZS_ ), ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>),</sup><sup>_e_</sup> � `// Alg. 7` **3** �( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>), (</sup><sup>_K_1,</sup><sup>_K_2)</sup> � ← `3` _ `iso` _ `curve` (( _XT_ : _ZT_ )) `// Alg. 15` **4 if** _e_ � 0 **then 5** ( _XS_ : _ZS_ ) ← `3` _ `iso` _ `eval` (( _K_ 1, _K_ 2), ( _XS_ : _ZS_ )) `// Alg. 16` **6 for** ( _X j_ : _Z j_ ) **in** _optional input_ **do 7** ( _X j_ : _Z j_ ) ← `3` _ `iso` _ `eval` �( _K_ 1, _K_ 2), ( _X j_ : _Z j_ )� `// Alg. 16` **8 return** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>), �(</sup><sup>_X_1:</sup><sup>_Z_1), (</sup><sup>_X_2:</sup><sup>_Z_2), (</sup><sup>_X_3:</sup><sup>_Z_3)�</sup> 

68 

**Algorithm 19:** Computing and evaluating a 2<sup>_e_</sup> -isogeny, optimized version 

**function** `2_e_iso` 

**Static parameters:** Integer `e2` from the public parameters, a _strategy_ 

( _s_ 1, . . . , _s_ `e2` /2−1) ∈ (N<sup>+</sup> )<sup>`e2`/2−1</sup> 

**Input:** Constants ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24) corresponding to a curve</sup><sup>_EA_/</sup><sup>_C_, (</sup><sup>_XS_:</sup><sup>_ZS_) where</sup><sup>_S_has exact order</sup> 

2<sup>`e2`</sup> on _EA_ / _C_ 

**Optional input:** ( _X_ 1 : _Z_ 1), ( _X_ 2 : _Z_ 2) and ( _X_ 3 : _Z_ 3) on _EA_ / _C_ 

**Output:** ( _A_<sup>+</sup> 24′ : _C_ 24′<sup>) corresponding to the curve</sup><sup>_EA_′/</sup><sup>_C_′=</sup><sup>_E_/⟨</sup><sup>_S_⟩</sup> **Optional output:** ( _X_ 1<sup>′:</sup><sup>_Z_</sup> 1<sup>′), (</sup><sup>_X_</sup> 2<sup>′:</sup><sup>_Z_</sup> 2<sup>′) and (</sup><sup>_X_</sup> 3<sup>′:</sup><sup>_Z_</sup> 3<sup>′) on</sup><sup>_EA_′/</sup><sup>_C_′</sup> 

- **1** Initialize empty deque **S** 

- **2** `push`<sup>�</sup> **S** , ( `e2` /2, ( _XS_ : _ZS_ ))<sup>�</sup> 

- **3** _i_ ← 1 

- **4 while S** _not empty_ **do** 

- **5** ( _h_ , ( _X_ : _Z_ )) ← `pop` ( **S** ) **6 if** _h_ = 1 **then 7** �( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24), (</sup><sup>_K_1,</sup><sup>_K_2,</sup><sup>_K_3)</sup> � ← `4` _ `iso` _ `curve` (( _X_ : _Z_ )) `// Alg. 13` **8** Initialize empty deque **S**<sup>′</sup> **9 while S** _not empty_ **do** 

- **10** ( _h_ , ( _X_ : _Z_ )) ← `pull` ( **S** ) **11** ( _X_ : _Z_ ) ← `4` _ `iso` _ `eval` (( _K_ 1, _K_ 2, _K_ 3), ( _X_ : _Z_ )) `// Alg. 14` **12** `push`<sup>�</sup> **S**<sup>′</sup> , ( _h_ − 1, ( _X_ : _Z_ ))<sup>�</sup> **13 S** ← **S**<sup>′</sup> **14 for** ( _X j_ : _Z j_ ) **in** _optional input_ **do 15** ( _X j_ : _Z j_ ) ← `4` _ `iso` _ `eval` �( _K_ 1, _K_ 2, _K_ 3), ( _X j_ : _Z j_ )� `// Alg. 14` **16 else if** 0 < _si_ < _h_ **then 17** `push`<sup>�</sup> **S** , ( _h_ , ( _X_ : _Z_ ))<sup>�</sup> **18** ( _X_ : _Z_ ) ← `xDBLe` �( _X_ : _Z_ ), ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24), 2 ·</sup><sup>_si_</sup> � `// Alg. 4` **19** `push`<sup>�</sup> **S** , ( _h_ − _si_ , ( _X_ : _Z_ ))<sup>�</sup> **20** _i_ ← _i_ + 1 

- **21 else 22 Error:** Invalid strategy **23 return** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24), �(</sup><sup>_X_1:</sup><sup>_Z_1), (</sup><sup>_X_2:</sup><sup>_Z_2), (</sup><sup>_X_3:</sup><sup>_Z_3)�</sup> 

69 

**Algorithm 20:** Computing and evaluating a 3<sup>_e_</sup> -isogeny, optimized version 

**function** `3_e_iso` 

**Static parameters:** Integer `e3` from the public parameters, a _strategy_ ( _s_ 1, . . . , _s_ `e3` −1) ∈ (N<sup>+</sup> )<sup>`e3`−1</sup> **Input:** Constants ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>) corresponding to a curve</sup><sup>_EA_/</sup><sup>_C_, (</sup><sup>_XS_:</sup><sup>_ZS_) where</sup><sup>_S_has exact order</sup> 3<sup>`e3`</sup> on _EA_ / _C_ **Optional input:** ( _X_ 1 : _Z_ 1), ( _X_ 2 : _Z_ 2) and ( _X_ 3 : _Z_ 3) on _EA_ / _C_ 

′ − ′ **Output:** ( _A_<sup>+</sup> 24 : _A_ 24 ) corresponding to the curve _EA_ ′/ _C_ ′ = _E_ /⟨ _S_ ⟩ **Optional output:** ( _X_ 1<sup>′:</sup><sup>_Z_</sup> 1<sup>′), (</sup><sup>_X_</sup> 2<sup>′:</sup><sup>_Z_</sup> 2<sup>′) and (</sup><sup>_X_</sup> 3<sup>′:</sup><sup>_Z_</sup> 3<sup>′) on</sup><sup>_EA_′/</sup><sup>_C_′</sup> 

**1** Initialize empty deque **S** 

**2** `push`<sup>�</sup> **S** , ( `e3` , ( _XS_ : _ZS_ ))<sup>�</sup> 

**3** _i_ ← 1 

#### **4 while S** _not empty_ **do** 

- **5** ( _h_ , ( _X_ : _Z_ )) ← `pop` ( **S** ) **6 if** _h_ = 1 **then 7** �( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>), (</sup><sup>_K_1,</sup><sup>_K_2)</sup> � ← `3` _ `iso` _ `curve` (( _X_ : _Z_ )) `// Alg. 15` **8** Initialize empty deque **S**<sup>′</sup> **9 while S** _not empty_ **do** 

- **10** ( _h_ , ( _X_ : _Z_ )) ← `pull` ( **S** ) **11** ( _X_ : _Z_ ) ← `3` _ `iso` _ `eval` (( _K_ 1, _K_ 2), ( _X_ : _Z_ )) `// Alg. 16` **12** `push`<sup>�</sup> **S**<sup>′</sup> , ( _h_ − 1, ( _X_ : _Z_ ))<sup>�</sup> **13 S** ← **S**<sup>′</sup> **14 for** ( _X j_ : _Z j_ ) **in** _optional input_ **do 15** ( _X j_ : _Z j_ ) ← `3` _ `iso` _ `eval` �( _K_ 1, _K_ 2), ( _X j_ : _Z j_ )� `// Alg. 16` **16 else if** 0 < _si_ < _h_ **then 17** `push`<sup>�</sup> **S** , ( _h_ , ( _X_ : _Z_ ))<sup>�</sup> **18** ( _X_ : _Z_ ) ← `xTPLe` �( _X_ : _Z_ ), ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>),</sup><sup>_si_</sup> � `// Alg. 7` **19** `push`<sup>�</sup> **S** , ( _h_ − _si_ , ( _X_ : _Z_ ))<sup>�</sup> **20** _i_ ← _i_ + 1 

**21 else 22 Error:** invalid strategy 

**23 return** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>), �(</sup><sup>_X_1:</sup><sup>_Z_1), (</sup><sup>_X_2:</sup><sup>_Z_2), (</sup><sup>_X_3:</sup><sup>_Z_3)�</sup> 

70 

#### **Algorithm 21:** Computing <u>public keys in the 2-torsion</u> 

**function** `isogen` 2 

**Input:** Secret key sk2 ∈ Z (see §1.2.6) and public parameters 

{ `e2` , `e3` , `p` , `xP2` , `xQ2` , `xR2` , `xP3` , `xQ3` , `xR3` } (see §1.6) 

- **Output:** Public key _pk_ 2 = ( _x_ 1, _x_ 2, _x_ 3) equivalent to the output of Step 4 of `isogen` ℓ (see §1.3.6) 

- **1** �( _A_ : _C_ ), ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24)</sup> � ← ((6 : 1), (8 : 4)) 

**2** (( _X_ 1 : _Z_ 1), ( _X_ 2 : _Z_ 2), ( _X_ 3 : _Z_ 3)) ← (( `xP3` : `1` ), ( `xQ3` : `1` ), ( `xR3` : `1` )) 

#### **Algorithm 22:** Computing <u>public keys in the 3-torsion</u> 

#### **function** `isogen` 3 

71 

#### **Algorithm 23:** Establishing shared keys in the 2-torsion 

**function** `isoex` 2 

**Input:** Secret key sk2 ∈ Z (see §1.2.6), public key _pk_ 3 = ( _x_ 1, _x_ 2, _x_ 3) ∈ (F _p_ 2)<sup>3</sup> (see §1.2.9), and parameter `e2` (see §1.6) 

**Output:** A _j_ -invariant _j_ 2 equivalent to the output of Step 4 of `isogen` ℓ (see §1.3.7) 

**1** ( _A_ : _C_ ) ← ( `get` _ `A` ( _x_ 1, _x_ 2, _x_ 3) : 1) `// Alg. 10` **2** ( _XS_ : _ZS_ ) ← `Ladder3pt` (sk2, ( _x_ 1, _x_ 2, _x_ 3), ( _A_ : _C_ )) `// Alg. 8` **3** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24) ←(</sup><sup>_A_+ 2 : 4)</sup> **4** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24) ←</sup><sup>`2`_</sup><sup>`e`_</sup><sup>`iso`</sup> �( _A_<sup>+</sup> 24<sup>:</sup><sup>_C_24), (</sup><sup>_XS_:</sup><sup>_ZS_)</sup> � `// Alg. 17 or Alg. 19` **5** ( _A_ : _C_ ) ← (4 _A_<sup>+</sup> 24<sup>−2</sup><sup>_C_24:</sup><sup>_C_24)</sup> **6** _j_ = `j` _ `inv` (( _A_ : _C_ )) `// Alg. 9` **7 return** _j_ `// Encoded as in §1.2.8` 

#### **Algorithm 24:** Establishing shared keys in the 3-torsion 

#### **function** `isoex` 3 

**Input:** Secret key sk3 ∈ Z (see §1.2.6), public key _pk_ 2 = ( _x_ 1, _x_ 2, _x_ 3) ∈ (F _p_ 2)<sup>3</sup> (see §1.2.9), and parameter `e3` (see §1.6) **Output:** A _j_ -invariant _j_ 3 equivalent to the output of Step 4 of `isogen` ℓ (see §1.3.7) **1** ( _A_ : _C_ ) ← ( `get` _ `A` ( _x_ 1, _x_ 2, _x_ 3) : 1) `// Alg. 10` **2** ( _XS_ : _ZS_ ) ← `Ladder3pt` (sk3, ( _x_ 1, _x_ 2, _x_ 3), ( _A_ : _C_ )) `// Alg. 8` **3** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>) ←(</sup><sup>_A_+ 2 :</sup><sup>_A_−2)</sup> **4** ( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>) ←</sup><sup>`3`_</sup><sup>`e`_</sup><sup>`iso`</sup> �( _A_<sup>+</sup> 24<sup>:</sup><sup>_A_−</sup> 24<sup>), (</sup><sup>_XS_:</sup><sup>_ZS_)</sup> � `// Alg. 18 or Alg. 20` **5** ( _A_ : _C_ ) ← (2 · ( _A_<sup>−</sup> 24<sup>+</sup><sup>_A_+</sup> 24<sup>) :</sup><sup>_A_+</sup> 24<sup>−</sup><sup>_A_−</sup> 24<sup>)</sup> **6** _j_ = `j` _ `inv` (( _A_ : _C_ )) `// Alg. 9` **7 return** _j_ `// Encoded as in §1.2.8` 

72 

# **Appendix B** 

#### **Algorithm 26:** Repeated affine coordinate doubling 

##### **function** `xDBLe` 

**Input:** ( _xP_ , _yP_ ), ( _a_ , _b_ ), and _e_ ∈ Z 

**Output:** ( _x_ [2<sup>_e_</sup> ] _P_ , _y_ [2<sup>_e_</sup> ] _P_ ) 

**1** ( _x_<sup>′</sup> , _y_<sup>′</sup> ) ← ( _xP_ , _yP_ ) 

**2 for** _i_ = 1 **to** _e_ **do 3** ( _x_<sup>′</sup> , _y_<sup>′</sup> ) ← `xDBL` (( _x_<sup>′</sup> , _y_<sup>′</sup> ), ( _a_ , _b_ )) **4 return** ( _x_<sup>′</sup> , _y_<sup>′</sup> ) 

```
//Alg.25
```

#### **Algorithm 27:** Affine coordinate addition 

**function** `xADD` 

**Input:** _P_ = ( _xP_ , _yP_ ), _Q_ = ( _xQ_ , _yQ_ ), and ( _a_ , _b_ ) 

**Output:** ( _xP_ + _Q_ , _yP_ + _Q_ ) 

**1 if** _P_ = ∞ **then 5 if** _P_ = _Q_ **then 2 return** ( _xQ_ , _yQ_ ) **6 return** `xDBL` (( _xP_ , _yP_ ), ( _a_ , _b_ )) **3 if** _Q_ = ∞ **then 7 if** _P_ = − _Q_ **then 4 return** ( _xP_ , _yP_ ) **8 return** ∞ **9** _t_ 0 ← _yQ_ − _yP_ **14** _t_ 2 ← _xP_ + _xP_ **19** _t_ 0 ← _b_ · _t_ 0 **24** _t_ 1 ← _t_ 1 − _xP_ **10** _t_ 1 ← _xQ_ − _xP_ **15** _t_ 2 ← _t_ 2 + _xQ_ **20** _t_ 0 ← _t_ 0 + _yP_ **25** _x_ [ _P_ + _Q_ ] ← _t_ 1 − _xQ_ **11** _t_ 1 ← _t_ 1<sup>−1</sup> **16** _t_ 2 ← _t_ 2 + _a_ **21** _t_ 0 ← _t_ 2 − _t_ 0 **26** _y_ [ _P_ + _Q_ ] ← _t_ 0 **12** _t_ 0 ← _t_ 0 · _t_ 1 **17** _t_ 2 ← _t_ 2 · _t_ 0 **22** _t_ 1 ← _b_ · _t_ 1 **27 return** ( _xP_ + _Q_ , _yP_ + _Q_ ) **13** _t_ 1 ← _t_ 0<sup>2</sup> **18** _t_ 0 ← _t_ 0 · _t_ 1 **23** _t_ 1 ← _t_ 1 − _a_ 

#### **Algorithm 28:** Affine coordinate tripling 

##### **function** `xTPL` 

**Input:** ( _xP_ , _yP_ ) and ( _a_ , _b_ ) **Output:** ( _x_ [3] _P_ , _y_ [3] _P_ ) **1** ( _x_ [2] _P_ , _y_ [2] _P_ ) ← `xDBL` (( _xP_ , _yP_ ), ( _a_ , _b_ )) `// Alg. 25` **2** ( _x_ [3] _P_ , _y_ [3] _P_ ) ← `xADD`<sup>�</sup> ( _xP_ , _yP_ ), ( _x_ [2] _P_ , _y_ [2] _P_ ), ( _a_ , _b_ )<sup>�</sup> `// Alg. 27` **3 return** ( _x_ [3] _P_ , _y_ [3] _P_ ) 

74 

#### **Algorithm 29:** Repeated affine coordinate tripling 

**function** `xTPLe` **Input:** ( _xP_ , _yP_ ), ( _a_ , _b_ ), and _e_ ∈ Z<sup>+</sup> **Output:** ( _x_ [3<sup>_e_</sup> ] _P_ , _y_ [3<sup>_e_</sup> ] _P_ ) **1** ( _x_<sup>′</sup> , _y_<sup>′</sup> ) ← ( _xP_ , _yP_ ) **2 for** _i_ = 1 **to** _e_ **do 3** ( _x_<sup>′</sup> , _y_<sup>′</sup> ) ← `xTPL` (( _x_<sup>′</sup> , _y_<sup>′</sup> ), ( _a_ , _b_ )) `// Alg. 28` **4 return** ( _x_<sup>′</sup> , _y_<sup>′</sup> ) 

#### **Algorithm 30:** Double-and-add scalar multiplication 

**function** `double_and_add` **Input:** _m_ = ( _m_ ℓ−1, . . . , _m_ 0)2 ∈ Z, _P_ = ( _x_ , _y_ ), and ( _a_ , _b_ ) **Output:** ( _x_ [ _m_ ] _P_ , _y_ [ _m_ ] _P_ ) **1** ( _x_ 0, _y_ 0) ← (0, 0) **2 for** _i_ = ℓ − 1 **to** 0 **by** −1 **do 3** ( _x_ 0, _y_ 0) ← `xDBL` (( _x_ 0, _y_ 0), ( _a_ , _b_ )) `// Alg. 25` **4 if** _mi_ = 1 **then 5** ( _x_ 0, _y_ 0) ← `xADD` (( _x_ 0, _y_ 0), ( _x_ , _y_ ), ( _a_ , _b_ )) `// Alg. 27` **6 return** ( _x_ 0, _y_ 0) 

#### **Algorithm 31:** Montgomery _<u>j</u>_ -invariant computation 

|**function**`j_inv`<br>**Input:** _a_<br>**Output:** _j_-invariant _j_(_Ea_,_b_)∈F_p_2|||
|---|---|---|
|**1** _t_0 ←_a_<sup>2</sup><br>**6** _j_←_j_+ _j_|**11** _j_←_j_+ _j_|**16** _t_0 ←_t_0<sup>−1</sup>|
|**2** _j_←3<br>**7** _j_←_j_+ _j_|**12** _j_←_j_+ _j_|**17** _j_←_j_·_t_0|
|**3** _j_←_t_0−_j_<br>**8** _j_←_j_+ _j_|**13** _j_←_j_+ _j_|**18 return** _j_|
|**4** _t_1 ←_j_<sup>2</sup><br>**9** _j_←_j_+ _j_|**14** _t_1 ←4||
|**5** _j_←_j_·_t_1<br>**10** _j_←_j_+ _j_|**15** _t_0 ←_t_0−_t_1||

75 

#### **Algorithm 32:** Computing the 2-isogenous curve 

**function** `curve_2_iso` **Input:** _xP_ 2 and _b_ , where _P_ 2 has exact order 2 on _Ea_ , _b_ **Output:** ( _a_<sup>′</sup> , _b_<sup>′</sup> ) corresponding to _Ea_<sup>′</sup> , _b_<sup>′</sup> = _Ea_ , _b_ /⟨ _P_ 2⟩ **1** _t_ 1 ← _xP_ 2 2 **3** _t_ 1 ← 1 − _t_ 1 **5** _b_<sup>′</sup> ← _xP_ 2 · _b_ **2** _t_ 1 ← _t_ 1 + _t_ 1 **4** _a_<sup>′</sup> ← _t_ 1 + _t_ 1 **6 return** ( _a_<sup>′</sup> , _b_<sup>′</sup> ) 

#### **Algorithm 33:** Evaluating a 2-isogeny at a point 

**function** `eval_2_iso` **Input:** ( _xQ_ , _yQ_ ) and _xP_ 2, where _P_ ∈ _Ea_ , _b_ , and _P_ 2 has exact order 2 on _Ea_ , _b_ **Output:** ( _xQ_<sup>′</sup> , _yQ_<sup>′</sup> ) corresponding to _Q_<sup>′</sup> ∈ _Ea_<sup>′</sup> , _b_<sup>′</sup> , where _Ea_<sup>′</sup> , _b_<sup>′</sup> is the curve 2-isogenous to _Ea_ , _b_ output from `curve_2_iso` **1** _t_ 1 ← _xQ_ · _xP_ 2 **5** _t_ 3 ← _t_ 2 − _t_ 3 **9** _t_ 1 ← _xQ_ − _xP_ 2 **13** _yQ_<sup>′</sup> ← _t_ 3 · _t_ 1 **2** _t_ 2 ← _xQ_ · _t_ 1 **6** _t_ 3 ← _t_ 3 + _xP_ 2 **10** _t_ 1 ← _t_ 1<sup>−1</sup> **14 return** ( _xQ_<sup>′</sup> , _yQ_<sup>′</sup> ) **3** _t_ 3 ← _t_ 1 · _xP_ 2 **7** _t_ 3 ← _yQ_ · _t_ 3 **11** _xQ_<sup>′</sup> ← _t_ 2 · _t_ 1 **4** _t_ 3 ← _t_ 3 + _t_ 3 **8** _t_ 2 ← _t_ 2 − _xQ_ **12** _t_ 1 ← _t_ 1<sup>2</sup> 

#### **Algorithm 34:** Computing the 4-isogenous curve 

**function** `curve_4_iso` **Input:** _xP_ 4 and _b_ , where _P_ 4 has exact order 4 on _Ea_ , _b_ **Output:** ( _a_<sup>′</sup> , _b_<sup>′</sup> ) corresponding to _Ea_<sup>′</sup> , _b_<sup>′</sup> = _Ea_ , _b_ /⟨ _P_ 4⟩ 2 **1** _t_ 1 ← _xP_ 4 **5** _t_ 2 ← 2 **9** _t_ 1 ← _t_ 1 · _b_ **13 return** ( _a_<sup>′</sup> , _b_<sup>′</sup> ) **2** _a_<sup>′</sup> ← _t_ 1<sup>2</sup> **6** _a_<sup>′</sup> ← _a_<sup>′</sup> − _t_ 2 **10** _t_ 2 ← _t_ 2<sup>−1</sup> **3** _a_<sup>′</sup> ← _a_<sup>′</sup> + _a_<sup>′</sup> **7** _t_ 1 ← _xP_ 4 · _t_ 1 **11** _t_ 2 ←− _t_ 2 **4** _a_<sup>′</sup> ← _a_<sup>′</sup> + _a_<sup>′</sup> **8** _t_ 1 ← _t_ 1 + _xP_ 4 **12** _b_<sup>′</sup> ← _t_ 2 · _t_ 1 

76 

#### **Algorithm 35:** Evaluating a 4-isogeny at a point 

|**function**`eval_4_iso`<br>**Input:** (_xQ_,_yQ_) and_xP_4, where_P_∈_Ea_,_b_, and <br>**Output:** (_xQ_<sup>′</sup>,_yQ_<sup>′</sup>) corresponding to_Q_<sup>′ </sup>∈_Ea_<sup>′</sup><br>from`curve_4_iso`|_P_4has exact order 4 on_Ea_,_b_<br>,_b_<sup>′</sup>, where_Ea_<sup>′</sup>,_b_<sup>′</sup> is the curve 4-isogenous to_Ea_,_b_output|
|---|---|
|**1** _t_1 ←_xQ_<sup>2</sup><br>**17** _t_4 ←_xP_4 ·_t_3|**33** _t_4 ←_t_2−1<br>**49** _yQ_<sup>′</sup> ←_yQ_<sup>′</sup> ·_t_5|
|**2** _t_2 ←_t_1<sup>2</sup><br>**18** _t_5 ←_t_1·_t_4|**34** _t_2 ←_t_2+_t_2<br>**50** _t_1 ←_t_1·_t_2|
|**3** _t_3 ←_xP_4<br>2<br>**19** _t_5 ←_t_5+_t_5|**35** _t_5 ←_t_2+_t_2<br>**51** _t_1 ←_t_1<sup>−1</sup>|
|**4** _t_4 ←_t_2·_t_3<br>**20** _t_5 ←_t_5+_t_5|**36** _t_1 ←_t_1−_t_5<br>**52** _t_4 ←_t_4<sup>2</sup>|
|**5** _t_2 ←_t_2+_t_4<br>**21** _t_2 ←_t_2−_t_5|**37** _t_1 ←_t_4·_t_1<br>**53** _t_1 ←_t_1·_t_4|
|**6** _t_4 ←_t_1·_t_3<br>**22** _t_1 ←_t_1·_xP_4|**38** _t_1 ←_t_3·_t_1<br>**54** _t_1 ←_xQ_·_t_1|
|**7** _t_4 ←_t_4+_t_4<br>**23** _t_1 ←_t_1+_t_1|**39** _t_1 ←_yQ_·_t_1<br>**55** _t_2 ←_xQ_·_t_3|
|**8** _t_5 ←_t_4+_t_4<br>**24** _t_1 ←_t_1+_t_1|**40** _t_1 ←_t_1+_t_1<br>**56** _t_2 ←_t_2+_xQ_|
|**9** _t_5 ←_t_5+_t_5<br>**25** _t_1 ←_t_2−_t_1|**41** _yQ_<sup>′</sup> ←−_t_1<br>**57** _t_3 ←_xP_4 +_xP_4|
|**10** _t_4 ←_t_4+_t_5<br>**26** _t_2 ←_xQ_·_t_4|**42** _t_2 ←_t_2−_t_3<br>**58** _t_2 ←_t_2−_t_3|
|**11** _t_2 ←_t_2+_t_4<br>**27** _t_2 ←_t_2+_t_2|**43** _t_1 ←_t_2−1<br>**59** _t_2 ←−_t_2|
|**12** _t_4 ←_t_3<sup>2</sup><br>**28** _t_2 ←_t_2+_t_2|**44** _t_2 ←_xQ_−_xP_4<br>**60** _xQ_<sup>′</sup> ←_t_1·_t_2|
|**13** _t_5 ←_t_1·_t_4<br>**29** _t_1 ←_t_1−_t_2|**45** _t_1 ←_t_2·_t_1<br>**61 return**(_xQ_<sup>′</sup>,_yQ_<sup>′</sup>)|
|**14** _t_5 ←_t_5+_t_5<br>**30** _t_1 ←_t_1+_t_3|**46** _t_5 ←_t_1<sup>2</sup>|
|**15** _t_2 ←_t_2+_t_5<br>**31** _t_1 ←_t_1+1|**47** _t_5 ←_t_5·_t_2|
|**16** _t_1 ←_t_1·_xQ_<br>**32** _t_2 ←_xQ_·_xP_4|**48** _t_5 ←_t_5<sup>−1</sup>|

**Algorithm 36:** Computing the 3-isogenous curve 

|**function**`curve_3_iso`<br>**Input:** _xP_3 and (_a_,_b_), where_P_3has exact order 3 on_Ea_,_b_||
|---|---|
|**Output:** Curve constant (_a_<sup>′</sup>,_b_<sup>′</sup>) corresponding to_Ea_<sup>′</sup>,_b_<sup>′</sup> = _Ea_,_b_/⟨_P_3⟩||
|**1** _t_1 ←_xP_3<br>2<br>**4** _t_2 ←_t_1+_t_1<br>**7** _t_1 ←_t_1−_t_2|**10** _a_<sup>′ </sup>←_t_1·_xP_3|
|**2** _b_<sup>′ </sup>←_b_·_t_1<br>**5** _t_1 ←_t_1+_t_2<br>**8** _t_2 ←_a_·_xP_3|**11 return**(_a_<sup>′</sup>,_b_<sup>′</sup>)|
|**3** _t_1 ←_t_1+_t_1<br>**6** _t_2 ←6<br>**9** _t_1 ←_t_2−_t_1||

77 

#### **Algorithm 37:** Evaluating a 3-isogeny at a point 

|**function**`eval_3_iso`<br>**Input:** (_xQ_,_yQ_) and_xP_3, where_P_∈_Ea_,_b_, and_P_3has exact order 3 on_Ea_,_b_|
|---|
|**Output:** (_xQ_<sup>′</sup>,_yQ_<sup>′</sup>) corresponding to_Q_<sup>′ </sup>∈_Ea_<sup>′</sup>,_b_<sup>′</sup>, where_Ea_<sup>′</sup>,_b_<sup>′</sup> is the curve 3-isogenous to_Ea_,_b_output<br>from`curve_3_iso`|
|**1** _t_1 ←_xQ_<sup>2</sup><br>**7** _t_1 ←_t_1−_t_2<br>**13** _t_2 ←_t_2·_t_3<br>**19** _t_2 ←_t_2·_t_3|
|**2** _t_1 ←_t_1·_xP_3<br>**8** _t_1 ←_t_1+_xQ_<br>**14** _t_4 ←_xQ_·_xP_3<br>**20** _xQ_<sup>′</sup> ←_xQ_·_t_2|
|**3** _t_2 ←_xP_3<br>2<br>**9** _t_1 ←_t_1+_xP_3<br>**15** _t_4 ←_t_4−1<br>**21** _yQ_<sup>′</sup> ←_yQ_·_t_1|
|**4** _t_2 ←_xQ_·_t_2<br>**10** _t_2 ←_xQ_−_xP_3<br>**16** _t_1 ←_t_4·_t_1<br>**22 return**(_xQ_<sup>′</sup>,_yQ_<sup>′</sup>)|
|**5** _t_3 ←_t_2+_t_2<br>**11** _t_2 ←_t_2<sup>−1</sup><br>**17** _t_1 ←_t_1·_t_2|
|**6** _t_2 ←_t_2+_t_3<br>**12** _t_3 ←_t_2<sup>2</sup><br>**18** _t_2 ←_t_4<sup>2</sup>|

78 

#### **Algorithm 38:** Computing and evaluating a 2<sup>_e_</sup> -isogeny, simple version 

**function** `iso_2_e` 

**Static parameters:** Integer `e2` from the public parameters 

**Input:** Constants ( _a_ , _b_ ) corresponding to a curve _Ea_ , _b_ , ( _xS_ , _yS_ ) where _S_ has exact order 2<sup>`e2`</sup> on 

_Ea_ , _b_ 

**Optional input:** {( _x_ 1, _y_ 1), ..., ( _xn_ , _yn_ )} on _Ea_ , _b_ **Output:** ( _a_<sup>′</sup> , _b_<sup>′</sup> ) corresponding to the curve _Ea_ ′, _b_ ′ = _E_ /⟨ _S_ ⟩ 

**Optional output:** {( _x_ 1<sup>′,</sup><sup>_y_′</sup> 1<sup>), ..., (</sup><sup>_x_</sup> _n_<sup>′,</sup><sup>_y_′</sup> _n_<sup>)} on</sup><sup>_Ea_′,</sup><sup>_b_′</sup> 

|**1** (_a_<sup>′</sup>,_b_<sup>′</sup>)←(_a_,_b_)||
|---|---|
|**2** _e_<sup>′</sup><br>2 <sup>←</sup><sup>`e2`</sup>||
|**3 if** _e_<sup>′</sup><br>2 <sup>_is odd_</sup><sup>**then**</sup>||
|**4**<br>(_xT_,_yT_)←`xDBLe`<br>�<br>(_xS_,_yS_),(_a_<sup>′</sup>,_b_<sup>′</sup>),_e_<sup>′</sup><br>2 <sup>−1</sup><br>�|`// Alg. 26`|
|**5**<br>(_a_<sup>′</sup>,_b_<sup>′</sup>)←`curve`_`2`_`iso`(_xT_,_b_<sup>′</sup>)|`// Alg. 32`|
|**6**<br>(_xS_,_yS_)←`eval`_`2`_`iso`((_xS_,_yS_),_xT_)|`// Alg. 33`|
|**7**<br>**for**(_x j_,_yj_)**in**_optional input_**do**||
|**8**<br>(_x_<sup>′</sup><br>_j_<sup>,</sup><sup>_y_′</sup><br>_j_<sup>) ←</sup><sup>`eval`_</sup><sup>`2`_</sup><sup>`iso`</sup><br>�<br>(_x j_,_y j_),_xT_<br>�|`// Alg. 33`|
|**9**<br>_e_<sup>′</sup><br>2 <sup>←</sup><sup>_e_′</sup><br>2 <sup>−1</sup>||
|**10 for**_e_=_e_<sup>′</sup><br>2 <sup>−2</sup><sup>**downto** 0</sup><sup>**by** −2</sup><sup>**do**</sup>||
|**11**<br>(_xT_,_yT_)←`xDBLe`((_xS_,_yS_),(_a_<sup>′</sup>,_b_<sup>′</sup>),_e_)|`// Alg. 26`|
|**12**<br>(_a_<sup>′</sup>,_b_<sup>′</sup>)←`curve`_`4`_`iso`(_xT_,_b_<sup>′</sup>)|`// Alg. 34`|
|**13**<br>**if** _e_�0**then**||
|**14**<br>(_xS_,_yS_)←`eval`_`4`_`iso`((_xS_,_yS_),_xT_)|`// Alg. 35`|
|**15**<br>**for**(_xj_,_yj_)**in**_optional input_**do**||
|**16**<br>(_x_<sup>′</sup><br>_j_<sup>,</sup><sup>_y_′</sup><br>_j_<sup>) ←</sup><sup>`eval`_</sup><sup>`4`_</sup><sup>`iso`</sup><br>�<br>(_x j_,_y j_),_xT_<br>�|`// Alg. 35`|
|**17 return**(_a_<sup>′</sup>,_b_<sup>′</sup>), <sup>�</sup>(_x_<sup>′</sup><br>1<sup>,</sup><sup>_y_′</sup><br>1<sup>), ..., (</sup><sup>_x_′</sup><br>_n_<sup>,</sup><sup>_y_′</sup><br>_n_<sup>)�</sup>||

79 

#### **Algorithm 39:** Computing and evaluating a 3<sup>_e_</sup> -isogeny, simple version 

**function** `iso_3_e` 

**Static parameters:** Integer `e3` from the public parameters 

**Input:** Constants ( _a_ , _b_ ) corresponding to a curve _Ea_ , _b_ , ( _xS_ , _yS_ ) where _S_ has exact order 3<sup>`e3`</sup> on 

_Ea_ , _b_ 

**Optional input:** {( _x_ 1, _y_ 1), ..., ( _xn_ , _yn_ )} on _Ea_ , _b_ 

**Output:** ( _a_<sup>′</sup> , _b_<sup>′</sup> ) corresponding to the curve _Ea_ ′, _b_ ′ = _E_ /⟨ _S_ ⟩ 

- **1** ( _a_<sup>′</sup> , _b_<sup>′</sup> ) ← ( _a_ , _b_ ) 

- **2 for** _e_ = _e_ 3 − 1 **downto** 0 **by** −1 **do** 

- **6** ( _xS_ , _yS_ ) ← `eval` _ `3` _ `iso` (( _xS_ , _yS_ ), _xT_ ) 

```
//Alg.37
```

#### **Algorithm 40:** Recovering the _x_ -coordinate of _R_ 

#### **function** `get_xR` 

**Input:** Parameters of _Ea_ , _b_ with generator points: ( _a_ , _b_ ), _P_ = ( _xP_ , _yP_ ), _Q_ = ( _xQ_ , _yQ_ ) **Output:** _xR_ , such that _R_ = _P_ − _Q_ 

**1** ( _xR_ , _yR_ ) ← `xADD`<sup>�</sup> ( _xP_ , _yP_ ), ( _xQ_ , − _yQ_ ), ( _a_ , _b_ )<sup>�</sup> `// Alg. 27` 

- **2 return** _xR_ 

80 

**Algorithm 41:** Recovering the _y_ -coordinates of _P_ and _Q_ , and the Montgomery curve coefficient 

_<u>a</u>_ 

**function** `get_yP_yQ_A_B` 

**Input:** _pk_ = ( _xP_ , _xQ_ , _xR_ ) **Output:** ( _yP_ , _yQ_ , _a_ , _b_ ) 

**1** _a_ ← `get` _ `A` ( _xP_ , _xQ_ , _xR_ ) **2** _b_ ← 1 

```
//Encodedasin§1.2.8
```

```
//Alg.10
```

```
//Alg.27
```

**16 if** _xT_ � _xR_ **then** 

**17** 

_yQ_ ←− _yQ_ 

**18 return** ( _yP_ , _yQ_ , _a_ , _b_ ) 

**Algorithm 42:** Computing <u>public keys in the 2-torsion</u> **function** `isogen` 2 **Input:** Secret key sk2 ∈ Z (see §1.2.6) and public parameters { _e_ 2, _e_ 3, _p_ , ( _xP_ 2, _yP_ 2), ( _xQ_ 2, _yQ_ 2), ( _xP_ 3, _yP_ 3), ( _xQ_ 3, _yQ_ 3)} (see §1.6) **Output:** Public key _pk_ 2 = ( _x_<sup>′</sup> _P_ 3<sup>,</sup><sup>_x_′</sup> _Q_ 3<sup>,</sup><sup>_x_</sup> _R_<sup>′</sup> 3<sup>) equivalent to the output of Step 4 of</sup><sup>`isogen`ℓ</sup> 

(see §1.3.6) **1** ( _a_ , _b_ ) ← (6, 1) **2** ( _xS_ , _yS_ ) ← `double` _ `and` _ `add`<sup>�</sup> sk2, ( _xQ_ 2, _yQ_ 2), ( _a_ , _b_ )<sup>�</sup> **3** ( _xS_ , _yS_ ) ← `xADD` (( _xP_ 2, _yP_ 2), ( _xS_ , _yS_ ), ( _a_ , _b_ )) **4** �( _a_<sup>′</sup> , _b_<sup>′</sup> ), ( _x_<sup>′</sup> _P_ 3<sup>,</sup><sup>_y_′</sup> _P_ 3<sup>), (</sup><sup>_x_′</sup> _Q_ 3<sup>,</sup><sup>_y_′</sup> _Q_ 3<sup>)</sup> � ← `iso` _ `2` _ `e`<sup>�</sup> ( _a_ , _b_ ), ( _xS_ , _yS_ ), ( _xP_ 3, _yP_ 3), ( _xQQ_ 3,, _yQQ_ 3))<sup>�</sup> **5** _xR_<sup>′</sup> 3<sup>←</sup><sup>`get`_</sup><sup>`xR`</sup> �( _a_<sup>′</sup> , _b_<sup>′</sup> ), ( _x_<sup>′</sup> _P_ 3<sup>,</sup><sup>_y_′</sup> _P_ 3<sup>), (</sup><sup>_x_′</sup> _Q_ 3<sup>,</sup><sup>_y_′</sup> _Q_ 3<sup>)</sup> � **6 return** _pk_ 2 = ( _x_<sup>′</sup> _P_ 3<sup>,</sup><sup>_x_′</sup> _Q_ 3<sup>,</sup><sup>_x_</sup> _R_<sup>′</sup> 3<sup>)</sup> `//` 

`// Alg. 30 // Alg. 27` _xQQ_ 3,, _yQQ_ 3))<sup>�</sup> `// Alg. 38 // Alg. 40 // Encoded as in §1.2.9` 

81 

#### **Algorithm 43:** Computing <u>public keys in the 3-torsion</u> 

- **function** `isogen` 3 **Input:** Secret key sk3 ∈ Z (see §1.2.6) and public parameters 

- { _e_ 2, _e_ 3, _p_ , ( _xP_ 2, _yP_ 2), ( _xQ_ 2, _yQ_ 2), ( _xP_ 3, _yP_ 3), ( _xQ_ 3, _yQ_ 3)} (see §1.6) 

- **Output:** Public key _pk_ 3 = ( _x_<sup>′</sup> _P_ 2<sup>,</sup><sup>_x_′</sup> _Q_ 2<sup>,</sup><sup>_x_</sup> _R_<sup>′</sup> 2<sup>) equivalent to the output of Step 4 of</sup><sup>`isogen`ℓ</sup> (see §1.3.6) 

- **1** ( _a_ , _b_ ) ← (6, 1) **2** ( _xS_ , _yS_ ) ← `double` _ `and` _ `add`<sup>�</sup> sk3, ( _xQ_ 3, _yQ_ 3), ( _a_ , _b_ )<sup>�</sup> `// Alg. 30` **3** ( _xS_ , _yS_ ) ← `xADD` (( _xP_ 3, _yP_ 3), ( _xS_ , _yS_ ), ( _a_ , _b_ )) `// Alg. 27` **4** �( _a_<sup>′</sup> , _b_<sup>′</sup> ), ( _x_<sup>′</sup> _P_ 2<sup>,</sup><sup>_y_′</sup> _P_ 2<sup>), (</sup><sup>_x_′</sup> _Q_ 2<sup>,</sup><sup>_y_′</sup> _Q_ 2<sup>)</sup> � ← `iso` _ `3` _ `e`<sup>�</sup> ( _a_ , _b_ ), ( _xS_ , _yS_ ), ( _xP_ 2, _yP_ 2), ( _xQ_ 2, _yQ_ 2)<sup>�</sup> `// Alg. 39` **5** _xR_<sup>′</sup> 2<sup>←</sup><sup>`get`_</sup><sup>`xR`</sup> �( _a_<sup>′</sup> , _b_<sup>′</sup> ), ( _x_<sup>′</sup> _P_ 2<sup>,</sup><sup>_y_′</sup> _P_ 2<sup>), (</sup><sup>_x_′</sup> _Q_ 2<sup>,</sup><sup>_y_′</sup> _Q_ 2<sup>)</sup> � `// Alg. 40` **6 return** _pk_ 3 = ( _x_<sup>′</sup> _P_ 2<sup>,</sup><sup>_x_′</sup> _Q_ 2<sup>,</sup><sup>_x_</sup> _R_<sup>′</sup> 2<sup>)</sup> `// Encoded as in §1.2.9` 

#### **Algorithm 44:** Establishing shared keys in the 2-torsion 

**function** `isoex` 2 

**Input:** Secret key sk2 ∈ Z (see §1.2.6), public key _pk_ 3 = ( _x_<sup>′</sup> _P_ 2<sup>,</sup><sup>_x_′</sup> _Q_ 2<sup>,</sup><sup>_x_</sup> _R_<sup>′</sup> 2<sup>) ∈(F</sup><sup>_p_2)3 (see §1.2.9),</sup> and parameter `e2` (see §1.6) **Output:** A _j_ -invariant _j_ 2 equivalent to the output of Step 4 of `isogen` ℓ (see §1.3.7) **1** ( _y_<sup>′</sup> _P_ 2<sup>,</sup><sup>_y_′</sup> _Q_ 2<sup>,</sup><sup>_a_,</sup><sup>_b_) ←</sup><sup>`get`_</sup><sup>`yP`_</sup><sup>`yQ`_</sup><sup>`A`_</sup><sup>`B`(</sup><sup>_x_′</sup> _P_ 2<sup>,</sup><sup>_x_′</sup> _Q_ 2<sup>,</sup><sup>_x_</sup> _R_<sup>′</sup> 2<sup>)</sup> `// Alg. 41` **2** ( _xS_ , _yS_ ) ← `mult` _ `double` _ `add` �sk2, ( _x_<sup>′</sup> _Q_ 2<sup>,</sup><sup>_y_′</sup> _Q_ 2<sup>), (</sup><sup>_a_,</sup><sup>_b_)</sup> � `// Alg. 30` **3** ( _xS_ , _yS_ ) ← `xADD` �( _x_<sup>′</sup> _P_ 2<sup>,</sup><sup>_y_′</sup> _P_ 2<sup>), (</sup><sup>_xS_,</sup><sup>_yS_), (</sup><sup>_a_,</sup><sup>_b_)</sup> � `// Alg. 27` **4** ( _a_ , _b_ ) ← `2` _ `e` _ `iso` (( _a_ , _b_ ), ( _xS_ , _yS_ )) `// Alg. 38` **5** _j_ 2 = `j` _ `inv` ( _a_ ) `// Alg. 31` **6 return** _j_ 2 `// Encoded as in §1.2.8` 

82 

#### **Algorithm 45:** Establishing shared keys in the 3-torsion 

|**function**`isoex`3|
|---|
|**Input:** Secret key sk3 ∈Z(see §1.2.6), public key _pk_2 =(_x_<sup>′</sup><br>_P_3<sup>,</sup><sup>_x_′</sup><br>_Q_3<sup>,</sup><sup>_x_′</sup><br>_R_3<sup>) ∈(F</sup><sup>_p_2)3 (see §1.2.9),</sup><br>and parameter`e3`(see §1.6)|
|**Output:** A _j_-invariant _j_3equivalent to the output of Step4of`isogen`ℓ(see §1.3.7)|
|**1** (_y_<sup>′</sup><br>_P_3<sup>,</sup><sup>_y_′</sup><br>_Q_3<sup>,</sup><sup>_a_,</sup><sup>_b_) ←</sup><sup>`get`_</sup><sup>`yP`_</sup><sup>`yQ`_</sup><sup>`A`_</sup><sup>`B`(</sup><sup>_x_′</sup><br>_P_3<sup>,</sup><sup>_x_′</sup><br>_Q_3<sup>,</sup><sup>_x_′</sup><br>_R_3<sup>)</sup><br>`// Alg. 41`|
|**2** (_xS_,_yS_)←`mult`_`double`_`add`<br>�<br>sk3,(_x_<sup>′</sup><br>_Q_3<sup>,</sup><sup>_y_′</sup><br>_Q_3<sup>), (</sup><sup>_a_,</sup><sup>_b_)</sup><br>�<br>`// Alg. 30`|
|**3** (_xS_,_yS_)←`xADD`<br>�<br>(_x_<sup>′</sup><br>_P_3<sup>,</sup><sup>_y_′</sup><br>_P_3<sup>), (</sup><sup>_xS_,</sup><sup>_yS_), (</sup><sup>_a_,</sup><sup>_b_)</sup><br>�<br>`// Alg. 27`|
|**4** (_a_,_b_)←`3`_`e`_`iso`((_a_,_b_),(_xS_,_yS_))<br>`// Alg. 39`|
|**5** _j_3 =`j`_`inv`(_a_))<br>`// Alg. 31`|
|**6 return** _j_3<br>`// Encoded as in §1.2.8`|

83 

# **Appendix C** 

#### **Algorithm 56:** Computing compressed public keys in the 3<sup>_e_3</sup> -torsion 

#### **function** `PublicKeyCompression_2` 

   - **Input:** Private key _sk_ 2 ∈ Z2<sup>_e_</sup> 2 and public key _pk_ 2 = ( _x_ 1, _x_ 2, _x_ 3) and Montgomery coefficient _A_ 

   - **Output:** Compressed public key _pk_  comp_ 2 = ( _bit_ , _b_ 1, _b_ 2, _t_ 1, _t_ 2, _t_ 3, _A_ , _r_ 1, _r_ 2) according to compressed encoding 

- **1** (( _xP_ , _xQ_ , _xR_ ) : _P_ , _Q_ , _R_ ∈ _EA_ ′=0) ← _IsogenyDual_ ( _sk_ 2, _A_ ) `// see [41] for dual iso. computation` 

- **2** _xU_ , _yU_ , _xV_ , _yV_ , _r_ 1, _r_ 2, _b_ 1, _b_ 2 ← _BuildOrdinaryE_ 3 _nBasis_ ( _A_ ) 

- **3** _xU_<sup>′,</sup><sup>_y_</sup> _U_<sup>′,</sup><sup>_x_</sup> _V_<sup>′,</sup><sup>_y_</sup> _V_<sup>′←</sup><sup>_MoveBasisToEA_′=0(</sup><sup>_sk_2,</sup><sup>_A_,</sup><sup>_xU_,</sup><sup>_yU_,</sup><sup>_xV_,</sup><sup>_yV_)</sup> `evaluation` 

- **4** _yP_ , _yQ_ , _A_<sup>′</sup> ← `get` _ `yP` _ `yQ` _ `A` _ `B` ( _xP_ , _xQ_ , _xR_ ) 

- **5** _c_ 0, _d_ 0, _c_ 1, _d_ 1 ← _ph_ ( _xP_ , _yP_ , _xQ_ , _yQ_ , _xU_<sup>′,</sup><sup>_y_′</sup> _U_<sup>,</sup><sup>_x_</sup> _V_<sup>′,</sup><sup>_y_′</sup> _V_<sup>,</sup><sup>_A_′, 3)</sup> 

      - `// Alg. 48` 

   - `// see [41] for dual iso.` 

      - `// Alg. 41 // Alg. 55` 

- **6 if** _d_ 1 (mod 3<sup>_e_3</sup> ) � 0 **then** 

- **7** _bit_ ← 0 

- **8** _t_ 1 ←− _d_ 0 · _d_ 1<sup>−1</sup> 

- **9** _t_ 2 ←− _c_ 1 · _d_ 1<sup>−1</sup> 

- **10** _t_ 3 ← _c_ 0 · _d_ 1<sup>−1</sup> 

#### **11 else** 

- **12** _bit_ ← 1 

- **13** _t_ 1 ←− _d_ 1 · _d_ 0<sup>−1</sup> 

- **14** _t_ 2 ← _c_ 1 · _d_ 0<sup>−1</sup> **15** _t_ 3 ←− _c_ 0 · _d_ 0<sup>−1</sup> 

**16 return** ( _bit_ , _b_ 1, _b_ 2, _t_ 1, _t_ 2, _t_ 3, _A_ , _r_ 1, _r_ 2) 

```
//Encodedasin§1.2.10
```

**Algorithm 57:** Computing compressed ciphertexts in the 2<sup>_e_2</sup> -torsion 

#### **function** `CiphertextCompression_3` 

**Input:** uncompressed points in ciphertext 

**Output:** compressed points for ciphertext 

```
//Seereference[42]fordetailsonciphertextcomputationandencoding
```

**1 return** _compressed points for ciphertext_ 

93 

**Algorithm 58:** Compute a kernel generator for the last 2<sup>_e_2</sup> -isogeny 

#### **function** `CiphertextDecompression_2` 

**Input:** Secret key sk2 ∈ Z2<sup>_e_</sup> 2 and compressed ciphertext 

**Output:** A kernel generator of the last 2<sup>_e_2</sup> -isogeny 

```
//See[42]formoredetailsinciphertextdecompressioncomputation
```

**1 return** _kernel generator of last_ 2<sup>_e_2</sup> _isogeny_ 

#### **Algorithm 59:** Compute a kernel generator for the last 3<sup>_e_3</sup> -isogeny 

#### **function** `PublicKeyDecompression_3` 

**Input:** Secret key _sk_ 3 ∈ Z3<sup>_e_</sup> 3 and compressed public key 

{ _bit_ , _b_ 1, _b_ 2, ( _t_ 1, _t_ 2, _t_ 3) ∈ (Z3<sup>_e_</sup> 3 )<sup>3</sup> , _A_ , _r_ 1, _r_ 2} **Output:** A kernel generator ( _x_<sup>′</sup> , _z_<sup>′</sup> ) ∈ _EA_ [3<sup>_e_3</sup> ] of the last 3<sup>_e_3</sup> -isogeny **1** ( _x_ 1, _y_ 1) _P_ 1, ( _x_ 2, _y_ 2) _P_ 2 ← _BuildOrdinaryE_ 3 _nBasis_  decompression_ ( _A_ , _bit_ , _b_ 1, _b_ 2, _r_ 1, _r_ 2) `// Alg. 49` **2 if** _bit_ = 0 **then 3** _scal_ ← ( _t_ 1 + _sk_ 3 · _t_ 3)(1 + _sk_ 3 · _t_ 2))<sup>−1</sup> **4** _x_ , _z_ ← `Ladder3pt` ( _scal_ , ( _x_ 1, _x_ 2, _x_ ( _P_ 1 − _P_ 2)), ( _A_ : 1))) `// Alg. 8` **5 else 6** _scal_ ← ( _t_ 1 + _sk_ 3 · _t_ 2)(1 + _sk_ 3 · _t_ 3))<sup>−1</sup> **7** _x_ , _z_ ← `Ladder3pt` ( _scal_ , ( _x_ 2, _x_ 1, _x_ ( _P_ 2 − _P_ 1)), ( _A_ : 1))) `// Alg. 8` **8** ( _x_<sup>′</sup> , _z_<sup>′</sup> ) ← _xTPLe_  fast_ ( _x_ , _z_ , _A_ /2, _e_ 3) `// Alg. 46` **9 return** ( _x_<sup>′</sup> , _z_<sup>′</sup> ) 

94 

# **Appendix D** 

# **Computing optimized strategies for fast isogeny and discrete logarithm computations** 

Algorithms 19 and 20 need to be parameterized by a computational strategy as described in Section 1.3.8. Any valid strategy, i.e. any sequence ( _s_ 1, . . . , _sn_ −1) corresponding to a full binary tree, can be used without affecting the security of the protocol. 

For the sake of efficiency, we recommend using the parameters specified in this section. They were generated by the algorithm below. The inputs to the algorithm are the strategy size _n_ , which is one less than the number of leaves in the tree, the cost for a scalar multiplication step _p_ and the cost for an isogeny computation and evaluation step _q_ . Specifically, we use _n_ 4, the size of the strategy for computations using the 2-torsion group, _p_ 4 the cost of two `xDBL` operations, _q_ 4 the cost of computation and evaluation of a 4-isogeny, i.e. of the functions `4_iso_curve` and `4_iso_eval` . Similarly, _n_ 3 is the size of the strategy for computations using the 3-torsion group, _p_ 3 the cost of a `xTPL` operation, and _q_ 3 the cost of computation and evaluation of a 3-isogeny, i.e. of the functions `3_iso_curve` and `3_iso_eval` . We denote the respective strategies by _S_ 4 and _S_ 3, respectively. 

#### **Algorithm 60:** Computing optimized strategy 

**function** `compute_strategy` **Input:** Strategy size _n_ , parameters _p_ , _q_ > 0 **Output:** Optimal strategy of size _n_ 

**1** _S_ ← [1 → ϵ] **2** _C_ ← [1 → 0] **3 for** _i_ = 2 **to** _n_ + 1 **do 4** Set _b_ ← argmin0< _b_ < _i_ ( _C_ [ _i_ − _b_ ] + _C_ [ _b_ ] + _bp_ + ( _i_ − _b_ ) _q_ ) **5** Set _S_ [ _i_ ] ← _b_ . _S_ [ _i_ − _b_ ] . _S_ [ _b_ ] **6** Set _C_ [ _i_ ] ← _C_ [ _i_ − _b_ ] + _C_ [ _b_ ] + _bp_ + ( _i_ − _b_ ) _q_ **7 return** _S_ [ _n_ + 1] 

95 

## **D.1 Strategies for** `SIKEp434` 

### **D.1.1 Isogeny in the** 2 **-torsion** 

- `n4` = `107` 

- `p4` = `5633` 

- `q4` = `5461` 

- `S4` = ( `48` , `28` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `13` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `5` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `2` , `1` , `1` , `1` , `21` , `12` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` ) 

### **D.1.2 Isogeny in the** 3 **-torsion** 

- `n3` = `136` 

- `p3` = `5322` 

- `q3` = `5282` 

- `S3` = ( `66` , `33` , `17` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `16` , `8` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `32` , `16` , `8` , `4` , `3` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` ) 

### **D.1.3 DLP in the subgroup of order** 2<sup>_e_2</sup> 

- `w2` = `4` 

`n2` = `53` 

`p` = `8 q` = `3 S2` = ( `19` , `13` , `8` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` ) 

96 

### **D.1.4 DLP in the subgroup of order** 3<sup>_e_3</sup> 

`w3` = `3` 

- `n3` = `45` 

`p` = `9` 

- `q` = `3` 

- `S3` = ( `18` , `9` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` ) 

## **D.2 Strategies for** `SIKEp503` 

### **D.2.1 Isogeny in the** 2 **-torsion** 

- `n4` = `124` 

- `p4` = `7490` 

- `q4` = `7278` 

- `S4` = ( `61` , `32` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `29` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `13` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `5` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `2` , `1` , `1` , `1` ) 

### **D.2.2 Isogeny in the** 3 **-torsion** 

- `n3` = `158` 

- `p3` = `7189` 

- `q3` = `7051` 

- `S3` = ( `71` , `38` , `21` , `13` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `5` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `2` , `1` , `1` , `1` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `17` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `33` , `17` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `16` , `8` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` ) 

97 

### **D.2.3 DLP in the subgroup of order** 2<sup>_e_2</sup> 

`w2` = `5` 

`n2` = `49` 

- `p` = `10` 

- `q` = `3` 

- `S2` = ( `15` , `10` , `7` , `5` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` ) 

### **D.2.4 DLP in the subgroup of order** 3<sup>_e_3</sup> 

- `w3` = `3` 

- `n3` = `52` 

- `p` = `9` 

- `q` = `3` 

- `S3` = ( `19` , `13` , `8` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` ) 

## **D.3 Strategies for** `SIKEp610` 

### **D.3.1 Isogeny in the** 2 **-torsion** 

- `n4` = `151` 

- `p4` = `10370` 

- `q4` = `10096` 

- `S4` = ( `67` , `37` , `21` , `12` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `16` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `33` , `16` , `8` , `5` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `16` , `8` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` ) 

98 

### **D.3.2 Isogeny in the** 3 **-torsion** 

- `n3` = `191` 

- `p3` = `10084` 

- `q3` = `9794` 

- `S3` = ( `86` , `48` , `27` , `15` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `12` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `21` , `12` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , 

   - `3` , `2` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , 

   - `1` , `38` , `21` , `12` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `17` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` ) 

### **D.3.3 DLP in the subgroup of order** 2<sup>_e_2</sup> 

- `e2` = `305` 

- `w2` = `5` 

- `n2` = `60` 

- `p` = `10` 

- `q` = `3` 

- `S2` = ( `19` , `13` , `9` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` ) 

### **D.3.4 DLP in the subgroup of order** 3<sup>_e_3</sup> 

`e3` = `192 w3` = `3 n3` = `63` 

- `p` = `9` 

`q` = `3` 

- `S3` = ( `23` , `13` , `9` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` ) 

99 

## **D.4 Strategies for** `SIKEp751` 

### **D.4.1 Isogeny in the** 2 **-torsion** 

- `n4` = `185` 

- `p4` = `14166` 

- `q4` = `13810` 

- `S4` = ( `80` , `48` , `27` , `15` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `12` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `21` , `12` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `33` , `20` , `12` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `8` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `16` , `8` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` ) 

### **D.4.2 Isogeny in the** 3 **-torsion** 

- `n3` = `238` 

- `p3` = `13898` 

- `q3` = `13409` 

- `S3` = ( `112` , `63` , `32` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `31` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `15` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `49` , `31` , `16` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `15` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `7` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `21` , `12` , `8` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `4` , `2` , `1` , `1` , `2` , `1` , `1` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `9` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `4` , `2` , `1` , `1` , `1` , `2` , `1` , `1` ) 

### **D.4.3 DLP in the subgroup of order** 2<sup>_e_2</sup> 

- `w2` = `4` 

`n2` = `92` 

`p` = `8` 

100 

- `q` = `3` 

- `S2` = ( `34` , `19` , `13` , `9` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` , `12` , `8` , `5` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` ) 

### **D.4.4 DLP in the subgroup of order** 3<sup>_e_3</sup> 

`e3` = `239` 

- `w3` = `3` 

- `n3` = `79` 

`p` = `9` 

`q` = `3` 

- `S3` = ( `28` , `19` , `13` , `7` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `3` , `1` , `1` , `1` , `1` , `1` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` , `9` , `6` , `4` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `1` , `2` , `1` , `1` , `1` , `1` , `3` , `2` , `1` , `1` , `1` , `1` , `1` , `1` ) 

101 

# **Appendix E** 

# **Changes made in the 2nd round** 

The main differences between the first round and second round SIKE submissions are as follows. 

- Two new parameter sets have been added: `SIKEp434` (§1.6.1) and `SIKEp610` (§1.6.5). 

- One parameter set ( `SIKEp964` ) has been removed. 

- Security categories for parameter sets have been adjusted upward. Chapter 5 presents the rationale for this change. 

- The starting curve has been changed from _A_ = 0 to _A_ = 6. §1.3.2 presents the rationale for this change. 

- An additional implementation including public key compression has been added (§1.5, §2.3). 

102 

# **Appendix F** 

# **Changes made in the 3rd round** 

The main differences between the second round and third round SIKE submissions are as follows. 

- Optimized ARMv8 implementations are now available for all parameter sets. 

- Optimized Cortex M4 and VHDL implementations are now available for all uncompressed parameter sets. 

- New (space and time) optimizations for compressed SIKE have been added; see Appendix C. 

- New pre-computation tables for discrete logarithms have been added, reducing static library sizes for compressed SIKE by 80-90%; see Appendix D. 

- Appendix C and Appendix D in the previous version have been swapped. 

103 

# **Appendix G** 

# **Notation** 

- ℓ, _m_ Integers ℓ, _m_ ∈{2, 3} such that ℓ � _m e_ ℓ The index of ℓ in the degree of the ℓ-power isogeny 

- skℓ The secret key corresponding to points in the ℓ<sup>_e_ℓ</sup> -torsion pkℓ The public key corresponding to points in the ℓ<sup>_e_ℓ</sup> -torsion ϕℓ The secret ℓ<sup>_e_ℓ</sup> -isogeny corresponding to skℓ _P_ ℓ A point of exact order ℓ<sup>_e_ℓ</sup> in _E_ 0(F _p_ 2) \ _E_ 0(F _p_ ), such that the order-ℓ<sup>_e_ℓ</sup> 

   - Weil pairing, _e_ ℓ<sup>_e_</sup> ℓ ( _P_ ℓ, _Q_ ℓ), has exact order ℓ<sup>_e_ℓ</sup> 

- _Q_ ℓ A point of exact order ℓ<sup>_e_ℓ</sup> in _E_ 0(F _p_ ) _R_ ℓ The point defined as _R_ ℓ = _Q_ ℓ − _P_ ℓ 

- `isogen` ℓ The algorithm that computes public keys — see §1.3.6 `isoex` ℓ The algorithm that establishes shared keys — see §1.3.7 _Ea_ The Montgomery curve defined by _Ea_ /F _p_ 2 : _y_<sup>2</sup> = _x_<sup>3</sup> + _ax_<sup>2</sup> + _x_ 

- _Ea_ The Montgomery curve defined by _Ea_ /F _p_ 2 : _y_<sup>2</sup> = _x_<sup>3</sup> + _ax_<sup>2</sup> + _x p_ The prime field characteristic defined as _p_ = 2<sup>_e_2</sup> 3<sup>_e_3</sup> − 1 

- _xP_ The _x_ -coordinate of the point _P yP_ The _y_ -coordinate of the point _P_ K2 The keyspace corresponding to points in the 2<sup>_e_2</sup> -torsion 

- K3 The keyspace corresponding to points in the 3<sup>_e_3</sup> -torsion 

- `N` _p_ The number of bytes used to represent elements in F _p_ 

- `N` sk The number of bytes used to represent secret keys 

- `N` _pk_ The number of bytes used to represent public keys Z The ring of integers F _q_ The finite field with _q_ elements 

- F¯ _q_ The algebraic closure of the finite field with _q_ elements 

- F _p_ The prime field with _p_ elements F _p_ 2 The quadratic extension field F _p_ 2, constructed over the prime field F _p_ as F _p_ 2 = F _p_ ( _i_ ) with _i_<sup>2</sup> + 1 = 0 

- P<sup>_n_</sup> ( _K_ ) The projective space of dimension _n_ over the field _K Q_ 2 A point of exact order 2<sup>_e_2</sup> in _E_ 0(F _p_ ) _P_ 2 A point of exact order 2<sup>_e_2</sup> in _E_ 0(F _p_ 2) \ _E_ 0(F _p_ ), such that the order-2<sup>_e_2</sup> Weil pairing, _e_ 2<sup>_e_</sup> 2 ( _P_ 2, _Q_ 2), has exact order 2<sup>_e_2</sup> 

104 

- _R_ 2 The point defined as _R_ 2 = _Q_ 2 − _P_ 2 _Q_ 3 A point of exact order 3<sup>_e_3</sup> in _E_ 0(F _p_ ) _P_ 3 A point of exact order 3<sup>_e_3</sup> in _E_ 0(F _p_ 2) \ _E_ 0(F _p_ ), such that the order-3<sup>_e_3</sup> Weil pairing, _e_ 3<sup>_e_</sup> 3 ( _P_ 3, _Q_ 3), has exact order 3<sup>_e_3</sup> 

- _R_ 3 The point defined as _R_ 3 = _Q_ 3 − _P_ 3 

- SIKE Supersingular isogeny key encapsulation SIDH Supersingular isogeny Diffie–Hellman PKE Public-key encryption KEM Key encapsulation mechanism 

- IND-CPA Indistinguishability under chosen plaintext attack IND-CCA Indistinguishability under chosen ciphertext attack RSA Rivest–Shamir–Adleman (cryptosystem) ECC Elliptic curve cryptography ⊕ The binary exclusive or (XOR) of equal-length bitstrings I An oracle computing isogenies of degree ℓ<sup>_e_ℓ/2</sup> B A block cipher 

- _G_<sup>_C_</sup> The number of gates of a classical circuit _G_<sup>_Q_</sup> The number of gates of a quantum circuit _D_<sup>_C_</sup> The depth of a classical circuit _D_<sup>_Q_</sup> The depth of a quantum circuit 

- `AES` Advanced Encryption Standard `PKE` An isogeny-based public-key encryption scheme `KEM` An isogeny-based key encapsulation mechanism `Gen` Key generation algorithm for `PKE Enc` Encryption algorithm for `PKE Dec` Decryption algorithm for `PKE` 

- `KeyGen` Key generation algorithm for `KEM Encaps` Encapsulation algorithm for `KEM Decaps` Decapsulation algorithm for `KEM` _F_ A random oracle _G_ A random oracle _H_ A random oracle 

- `SHAKE256` A customizable extendable-output function standardized by NIST _c_ 0 First part of an encapsulation of `KEM` _c_ 1 Second part of an encapsulation of `KEM` 

105