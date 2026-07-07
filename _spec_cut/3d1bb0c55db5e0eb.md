# **SFLASH, a fast asymmetric signature scheme for low-cost smartcards** 

# **Primitive specification and supporting documentation** 

Nicolas Courtois, Louis Goubin, Jacques Patarin 

CP8 Crypto Lab, SchlumbergerSema, 36-38 rue de la Princesse, BP 45, 78430 Louveciennes Cedex, France `courtois@minrank.org, LGoubin@slb.com, JPatarin@slb.com` 

**Note:** This document specifies the updated final version of the SFLASH signature scheme, slightly modified as allowed in the second stage of Nessie evaluation process, in order to improve the speed and the security. This is therefore the only official version of SFLASH. In some papers that refer to the old version, it is sometimes called SFLASH<sup>_v_1</sup> , and SFLASH<sup>_v_2</sup> is the new version. In the appendix of the present document we summarize all the changes in SFLASH, for readers and developers that are acquainted with the previous version. 

## **2 Notations** 

In all the present document, _||_ will denote the “concatenation” operation. More precisely, if _λ_ = ( _λ_ 0 _, . . . , λm_ ) and _µ_ = ( _µ_ 0 _, . . . , µn_ ) are two strings of elements (in a given field), then _λ||µ_ denotes the string of elements (in the given field) defined by: 

For a given string _λ_ = ( _λ_ 0 _, . . . , λm_ ) of bits and two integers _r_ , _s_ , such that 0 _≤ r ≤ s ≤ m_ , we denote by [ _λ_ ] _r→s_ the string of bits defined by: 

## **3 Parameters of the algorithm** 

The SFLASH algorithm uses three finite fields. 

- The first one, _K_ = **F** 128 is precisely defined as _K_ = **F** 2[ _X_ ] _/_ ( _X_<sup>7</sup> + _X_ + 1). We will denote by _π_ the bijection between _{_ 0 _,_ 1 _}_<sup>7</sup> and _K_ defined by: 

- _∀b_ = ( _b_ 0 _, . . . , b_ 6) _∈{_ 0 _,_ 1 _}_<sup>7</sup> _, π_ ( _b_ ) = _b_ 6 _X_<sup>6</sup> + _. . ._ + _b_ 1 _X_ + _b_ 0 (mod _X_<sup>7</sup> + _X_ + 1) _._ 

- The second one is _L_ = _K_ [ _X_ ] _/_ ( _X_<sup>37</sup> + _X_<sup>12</sup> + _X_<sup>10</sup> + _X_<sup>2</sup> + 1). We will denote by _ϕ_ the bijection between _K_<sup>37</sup> and _L_ defined by: 

- _∀ω_ = ( _ω_ 0 _, . . . , ω_ 36) _∈ K_<sup>37</sup> _, ϕ_ ( _ω_ ) = _ω_ 36 _X_<sup>36</sup> + _. . ._ + _ω_ 1 _X_ + _ω_ 0 ( mod _X_<sup>37</sup> + _X_<sup>12</sup> + _X_<sup>10</sup> + _X_<sup>2</sup> + 1) _._ 

### **3.1 Secret Parameters** 

1. An affine secret bijection _s_ from _K_<sup>37</sup> to _K_<sup>37</sup> . Equivalently, this parameter can be described by the 37 _×_ 37 square matrix and the 37 _×_ 1 column matrix over _K_ of the transformation _s_ with respect to the canonical basis of _K_<sup>37</sup> . We denote by _SL_ the square matrix (“ _L_ ” means “linear”) and _SC_ the column matrix (here “ _C_ ” means “constant”). 

2. An affine secret bijection _t_ from _K_<sup>37</sup> to _K_<sup>37</sup> . Equivalently, this parameter can be described by the 37 _×_ 37 square matrix and the 37 _×_ 1 column matrix over _K_ of the transformation _s_ with respect to the canonical basis of _K_<sup>37</sup> . We denote by _SL_ the square matrix (“ _L_ ” means “linear”) and _SC_ the column matrix (here “ _C_ ” means “constant”). 

3. A 80-bit secret string denoted by ∆. 

### **3.2 Public Parameters** 

The public key consists in the function _G_ from _K_<sup>37</sup> to _K_<sup>26</sup> defined by: 

Here _F_ is the function from _L_ to _L_ defined by: 

2 

By construction of the algorithm, _G_ is a quadratic transformation over _K_ , _i.e._ ( _Y_ 0 _, . . . , Y_ 25) = _G_ ( _X_ 0 _, . . . , X_ 36) can be written, equivalently: 

with each _Pi_ being a quadratic polynomial of the form 

all the elements _ζi,j,k_ , _νi,j_ and _ρi_ being in _K_ . 

## **4 Generation of the key** 

In the SFLASH scheme, the public is deduced from the secret key, as explained in section 3.2. We need only to describe how the secret key is generated. As described in section 3.1, the following secret elements have to be generated: 

- The secret invertible 37 _×_ 37 matrix _SL_ , and the secret 37 _×_ 1 (column) matrix _SC_ , all the coefficients being in _K_ . 

- The secret invertible 37 _×_ 37 matrix _TL_ , and the secret 37 _×_ 1 (column) matrix _TC_ , all the coefficients being in _K_ . 

- The 80-bit secret string ∆. 

Note that, through the _π_ transformation, generating an element of _K_ is equivalent to generating a 7-bit string. In what follows, we call 

#### `next_7bit_random_string` 

the string of 7 bits obtained by calling 7 times the CSPRBG (we obtain first the first bit of the string, then the second bit, ..., until the seventh bit). To generate all these parameters, we apply the following method, which uses a cryptographically secure pseudorandom bit generator (CSPRBG). From a seed whose entropy is at least 80 bits, this CSPRBG is supposed to produce a new random bit each time it is asked to. 

1. To generate the invertible 37 _×_ 37 matrix _SL_ , two methods can be used: 

**First Method (“Trial and error”):** Generate the matrix _SL_ by repeating 

```
fori=0to36
forj=0to36
S_L[i,j]=pi(next_7bit_random_string)
```

until we obtain an invertible matrix. 

3 

**Second Method (with the LU decomposition):** Generate a lower triangular 37 _×_ 37 matrix _LS_ and an upper triangular 37 _×_ 37 matrix _US_ , all the coefficients being in _K_ , as follows: 

```
fori=0to36
forj=0to36
{
if(i<j)then{U_S[i,j]=pi(next_7bit_random_string);L_S[i,j]=0}
if(i>j)then{L_S[i,j]=pi(next_7bit_random_string);U_S[i,j]=0}
if(i=j)then{repeat(z=next_7bit_random_string)untilz!=(0,0,0,0,0,0,0)
U_S[i,j]=pi(z);L_S[i,j]=1}
```

```
}
```

Define then _SL_ = _LS × US_ . 

2. Generate _SC_ by using the CSPRBG to obtain 37 new random elements of _K_ (from the top to the bottom of the column matrix). Each of these elements of _K_ is obtained by 

```
pi(next_7bit_random_string)
```

3. To generate the invertible 37 _×_ 37 matrix _SL_ , two methods can be used: 

**First Method (“Trial and error”):** Generate the matrix _TL_ by repeating 

```
fori=0to36
forj=0to36
T_L[i,j]=pi(next_7bit_random_string)
```

until we obtain an invertible matrix. 

**Second Method (with the LU decomposition):** Generate a lower triangular 37 _×_ 37 matrix _LT_ and an upper triangular 37 _×_ 37 matrix _UT_ , all the coefficients being in _K_ , as follows: 

```
fori=0to36
forj=0to36
{
if(i<j)then{U_T[i,j]=pi(next_7bit_random_string);L_T[i,j]=0}
if(i>j)then{L_T[i,j]=pi(next_7bit_random_string);U_T[i,j]=0}
if(i=j)then{repeat(z=next_7bit_random_string)untilz!=(0,0,0,0,0,0,0)
U_T[i,j]=pi(z);L_T[i,j]=1}
```

```
}
```

Define then _TL_ = _LT × UT_ . 

4. Generate _TC_ by using the CSPRBG to obtain 37 new random random elements of _K_ (from the top to the bottom of the column matrix). Each of these elements of _K_ is obtained by 

```
pi(next_7bit_random_string)
```

5. Finally, generate ∆by using the CSPRBG to obtain 80 random bits. 

Note that the generation of a complete secret key thus requires 20282 bits from the CSPRBG (with the second method). 

4 

## **5 Signing a message** 

In the present section, we describe the signature of a message _M_ by the SFLASH algorithm. 

### **5.1 The signing algorithm** 

The message _M_ is given by a string of bits. Its signature _S_ is obtained by applying successively the following operations (see figure 1): 

1. Let _M_ 1 and _M_ 2 be the three 160-bit strings defined by: 

2. Let _V_ be the 182-bit string defined by: 

3. Let _W_ be the 77-bit string defined by: 

4. Let _Y_ be the string of 26 elements of _K_ defined by: 

5. Let _R_ be the string of 11 elements of _K_ defined by: 

6. Let _B_ be the element of _L_ defined by: 

7. Let _A_ be the element of _L_ defined by: 

8. Let _X_ = ( _X_ 0 _, . . . , X_ 36) be the string of 37 elements of _K_ defined by: 

9. The signature _S_ is the 259-bit string given by: 

5 

<!-- Start of picture text -->
Message M<br>SHA-1 SHA-1<br>? ?<br>160 bits 160 bits<br>- Y SHA-1( ·|| ∆)<br>?<br>160 bits<br>-<br>R<br>? ?<br>Y ||R<br>t − 1<br>?<br>B<br>F − 1<br>?<br>A<br>s − 1<br>?<br>Signature S<br><!-- End of picture text -->

Figure 1: Signature generation with SFLASH 

6 

### **5.2 Computing** _A_ = _F_<sup>_−_1</sup> ( _B_ ) 

The function _F_ , from _L_ to _L_ , is defined by: 

As a consequence, _A_ = _F_<sup>_−_1</sup> ( _B_ ) can be obtained by the following formula: 

the value of the exponent _h_ being the inverse of 128<sup>11</sup> + 1 modulo 128<sup>37</sup> _−_ 1. In fact, _h_ can be explicitly given by: 

Three methods can be used to compute _A_ = _B_<sup>_h_</sup> : 

1. Directly compute the exponentiation _B_<sup>_h_</sup> by using the “square-and-multiply” principle. 

2. Use the following algorithm: 

   - (a) Initialize _A_ to: 

Note that _B �→ B_<sup>12810</sup> is a linear transformation of _L_ if we consider _L_ as a vector space over _K_ and can thus be easily computed. 

- (b) Compute 

This value can be computed either by using the “square-and-multiply” principle or by noticing that we also have 

with _A �→ A_<sup>12811</sup> being a linear transformation of _L_ if we consider _L_ as a vector space over _K_ . We can thus easily find _A_ by solving a system of linear equations over _K_ . 

   - (c) Apply 18 times the following transformation: replace _A_ by _u · A_<sup>12822</sup> . This is also practical, since _A �→ A_<sup>12822</sup> is a linear transformation of _L_ (considered as a vector space over _K_ ). 

3. Finally, we can also use the fact that 

Since _B �→ B_<sup>12811</sup> and _A �→ A_<sup>12822</sup> are two linear transformations of _L_ (considered as a vector space over _K_ ), _A_ can be found by solving a system of linear equations over _K_ . 

7 

## **6 Verifying a signature** 

Given a message _M_ ( _i.e._ a string of bits) and a signature _S_ (a 259-bit string), the following algorithm is used to decide whether _S_ is a valid signature of _M_ or not: 

1. Let _M_ 1 and _M_ 2 be the three 160-bit strings defined by: 

2. Let _V_ be the 182-bit string defined by: 

3. Let _Y_ be the string of 26 elements of _K_ defined by: 

4. Let _Y_<sup>_′_</sup> be the string of 26 elements of _K_ defined by: 

5. _•_ If _Y_ equals _Y_<sup>_′_</sup> , accept the signature. 

   - Else reject the signature. 

<!-- Start of picture text -->
Message M Signature S<br>SHA-1 SHA-1 G<br>? ? ?<br>160 bits 160 bits Y ′<br>?<br>- Y - Y =  Y ′ : accepted<br>Y =  Y ′ : rejected<br><!-- End of picture text -->

Figure 2: Signature verification with SFLASH 

## **7 Security of the SFLASH algorithm** 

SFLASH is a _C_<sup>_∗−−_</sup> scheme with a special choice of the parameters. The security of such schemes has been studied in [2]. 

The security is not proven to be equivalent to a simple to describe and assumed difficult to solve problem. However, here are the present results on the two possible kinds of attacks : 

8 

- **7.1 Attacks that compute a valid signature from the public key as if it was a random set of quadratic equations (** _i.e._ **without using the fact that we have a** _C_<sup>_∗−−_</sup> **scheme)** 

These attacks have to solve a MQ problem (MQ: Multivariate Quadratic equations), and the general MQ problem is NP-Hard. Moreover, when the parameters are well chosen, the known algorithms for solving such an MQ problem (such as XL, FXL or some Gr¨obner base algorithms) are efficient. With our choice of parameters for SFLASH, they require more computations than the equivalent of 2<sup>80</sup> TDES operations. 

- **7.2 Attacks that use the fact that the public key comes from a** _C_<sup>_∗−−_</sup> **scheme (and is not a random set of quadratic equations)** 

All the known attacks on this family have a complexity in _O_ ( _qr_ ), where _r_ is the number of removed equations ( _r_ = 11 in the SFLASH algorithm), and where _q_ is the number of elements of the finite field _K_ used (so _q_ = 128 = 2<sup>7</sup> for the SFLASH algorithm). So these attacks will require more than the equivalent of 2<sup>80</sup> TDES operations for the SFLASH algorithm. 

## **8 Summary of the characteristics of SFLASH** 

- Length of the signature: 259 bits. 

- Length of the public key: 15.4 Kbytes. 

- Length of the secret key: the secret key (2.45 Kbytes) is generated from a small seed of at least 128 bits. 

- Time to sign a message<sup>1</sup> : less than 2.7 ms (maximum time). 

- Time to verify a signature<sup>2</sup> : less than 0.8 ms ( _i.e._ approximately 37 _×_ 37 _×_ 26 multiplications and additions in _K_ ). 

- Time to generate a pair of public key/secret key: less than 1 s. 

- Best known attack: more than 2<sup>80</sup> TDES computations.