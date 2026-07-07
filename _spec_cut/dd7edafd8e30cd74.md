## Abstract

The CAESAR competition for standardization of schemes for authenticated encryption has received 49 entries. Constructions such as Keyak, ICEPOLE, Artemia, NORX and Ascon use DuplexWrap and JHAE modes. DuplexWrap is based on the sponge construction and JHAE is based on the JH hash function. Andreeva et al. have recently defined a generalized sponge like construction called Parazoa hash family and provided indifferentiability security bound for the same. They had shown that the sponge as well as the JH hash function are instances of the parazoa construction with suitable choices of parameters. In our work, we define *PPAE* as an Authenticated Encryption family based on Parazoa construction. The proposed AE mode supports feed-forward operation which is lacking in sponge based AE constructions. We also provide security analysis of the *PPAE* family.

Access provided by Daegu Gyeongbuk Institute of Science & Technology. Download conference paper PDF

### Similar content being viewed by others

## 2 Preliminaries

We discuss the notation used in this paper and give a formal introduction to Authenticated Encryption and its security notions.

### 2.1 Notations

Let \(\mathbb {Z}^{*}_{2}\) be set of bit strings of arbitrary length and \(\mathbb {Z}^{n}_{2}\) be set of *n*-bit strings, where \(n \in N\). Let \(p\Vert q\) denote the concatenation of bit strings \(p\,\text {and}\,q\). We use \(\lceil V\rceil ^{x}_{n}\) to denote \(``x''\) most significant bits of an *n*-bit string *V*, and \(\lfloor V\rfloor ^{y}_{n}\) to denote \(``y''\) least significant bits of the *n*-bit *V*. Further, *max*(*x*, *y*) outputs the bigger of the two values *x* and *y* and \(\perp \) is the invalid symbol.

### 2.2 Authenticated Encryption - *AE*
        

          *AE* is a symmetric key encryption scheme which provides privacy as well as authenticity for a message. An AE scheme \(\varPi \) is defined as \(\varPi \) = (\(\mathcal {K}, \mathcal {E}, \mathcal {D})\), where \(\mathcal {K}\) is a key generation algorithm which chooses a secret key *K* uniformly random from a finite set, and \(\mathcal {E}\) and \(\mathcal {D}\) are encryption and decryption functions respectively. *AE* can use a nonce *N*. AE can also support an optional Associate Data (*A*). The encryption algorithm takes nonce *N*, Associated Data *A*, message *M* as input and output ciphertext *C* and Tag *T*. The decryption algorithm outputs the message *M*, if the tag \(T^{'}\) produced from *N*, *A*, *C* matches the given tag *T*, else it returns \(\perp \) (INVALID) and discards the message.

## 3 Parazoa Family

Parazoa family of hash functions [2] is generalization of a Sponge based hash function. Parazoa uses *s*-bit IV and *s*-bit ideal permutation \(\pi \). The padded message *M* is divided into *k* blocks of *m*-bit each. The Parazoa comprise of two main functions: the compression function *f* and the extraction function *g*. The compression function uses an *s*-bit state and one block of the message to update the state. \(f: \mathbb {Z}^{s}_{2} \times \mathbb {Z}^{m}_{2} \rightarrow \mathbb {Z}^{s}_{2}\). The extraction function takes the previous state, processes it and outputs a *p*-bit *P* and the next state. \(g : \mathbb {Z}^{s}_{2} \rightarrow \mathbb {Z}^{s}_{2} \times \mathbb {Z}^{p}_{2}\). Once the input blocks are processed by the *f* function, the extraction function *g* is called *l* times to produce *n*-bit hash digest where \(lp \ge n\).

### 3.1 Compression Function *f*
        

Compression function *f* takes previous state and a message block \(M_i\) as input and processes it to produce a new state. It process in two steps. First, with the help of an injection function \(L_{in}: \mathbb {Z}^{s}_{2} \times \mathbb {Z}^{m}_{2} \rightarrow \mathbb {Z}^{s}_{2}\), the message *M* is injected into the state \(V_{i-1}\). This injected state is permuted using \(\pi \) to get an intermediate state *y*. This intermediate state is transformed and combined with previous state and \(M_i\) using \(L_{out}: \mathbb {Z}^{s}_{2} \times Z^{s}_{2} \times \mathbb {Z}^{m}_{2} \rightarrow \mathbb {Z}^{s}_{2}\). Therefore, the compression function is defined as \(f(V_{i-1},M_i) = V_i\).

Let *C*(*x*) be capacity set. Formally *C*(*x*) is defined as follows. For any \(x \in \mathbb {Z}^s_2\), \(C(x) = \{V \in \mathbb {Z}^s_2 \mid \exists M \in \mathbb {Z}^m_2 \text { s.t } L_{in}(V,M) = x \}\).

### 3.2 Extraction Function *g*
        

Extraction function *g* takes s-bit state as input and produces *p*-bit output \(P_i\) along with an updated state, \(L_{ex}: \mathbb {Z}^s_2 \leftarrow \mathbb {Z}^p_2\). The only requirement of *g*-function is to be balanced. That is each \(P \in \mathbb {Z}^p_2\) is equally likely to occur.

### 3.3 Finalization Function *fin*
        

The *fin* function combines *l* blocks of *p*-bits extracted from *g*-functions to produce an *n*-bit digest. In most of the cases, *l* blocks of *p*-bits are concatenated and then chopped to the required length of *n* bits. The *fin* function is required to be balanced. That is, each digest *n* is equally likely to occur from the given *pl* bits of string.

### 3.4 Padding Function *pad*
        

The *pad* function is an injective function which transforms arbitrary length message *M* into *m*-bit message blocks. The last block of the padded message, \(M_k\), must satisfy the following condition: For any \(x \in \mathbb {Z}^s_2 \text{ and } (V^{'},M^{'})\) \( \in \mathbb {Z}^s_2\times \mathbb {Z}^m_2\):

### 3.5 Indifferentiability of Parazoa Functions

The indifferentiablility of parazoa functions are proved based on the assumption that the underlying permutation \(\pi \) is ideal. We quote the relevant theorem from [2] for the secutity bound of Parazoa.

### 
                      **Theorem 1**
                    

                    
            **(Indifferentiability).** Let \(\pi \) be a random *s*-bit permutation, and let RO be a random oracle. Let *H* be a Parazoa function parameterized by *l*, *m*, *n*, *p*, *s*, *t*. Let *D* be the distinguisher that makes at most \(q_1\) left queries of maximal length \((U-1)m\) bits, \(q_2\) right queries and runs in time *t*, where \(U\ge 1\). Then:

where, simulator *S*, makes at most \(q_s \le q_2\) queries to *RO* and runs in the time \(O(q^2_2).\)
          

The advantage of any adversary say \(\mathcal {A}\), in differentiating a Parazoa function with a random oracle is \(O \left( \frac{((U+l)q_1 + q_2)^2}{2^{s- p-d}} \right) \) such that \(\mathcal {A}\) can make at most \(q_1\) queries to the hash function and \(q_2\) queries to the underlying primitive used in the hash function. Each \(q_1\) query can call the underlying primitive at most \(U+l\) times.

          **Intuition on Capacity Loss** *d***:** In [2], \(d \ge 0\) is the minimum value such that for any given *x* and fixed \(P\in \mathbb {Z}^p_2\), there are at most \(2^{d}\) couples (*V*, *x*) such that \(V \in L_{ex}^{-1}(P)\). Thus, \(|C(x)| \le 2^{p+d}\) for any *x*. This is due to the fact that there is only one *P* which satisfies \(L_{ex}(V)=P\) and the total number of *P* are \(2^p\).

In the indifferentiability proof, the simulator is required to choose *V* such that it doesn’t belong to the set *C*(*x*) to avoid collisions. Thus, the simulator can choose at most \((2^{s-p-d})\) values of *V*. Thus, \((s-p-d)\) bits of the state: *(a)* cannot be affected by the distinguisher by message injection, and *(b)* cannot be obtained by distinguisher through extraction. The parameter *d* can vary between 0 and \(s-p\). When \(d=0\), then \((s-p)\) bits cannot be controlled by the adversary. Similarly when \(d=s-p\), then the adversary has complete control over the state. In sponge construction \((s-p)\) is called the capacity *C*. If *d* increases, then \((S-p-d)\) decreases, thus it is termed the capacity loss.

## 4 Practical Parazoa Hash - *PPH*
      

For a secure AE scheme, the ciphertext should be influenced by message block. In order to ensure this with efficient implementation, we fix the \(L_{in}\) function as *XOR*. The addition modulo 2 function satisfies all the requirements for \(L_{in}\). Our choice of the function is motivated by the fact that most of the practical designs such as Sponge, JH, FWP, FP modes have XOR as their \(L_{in}\) function. We denote this specific type of Parazoa hash family, as “*Practical Parazoa Hash*” function, *PPH*. The PPH construction is shown in Fig. 1. We use PPH as underlying construction for our Authenticated Encryption PPAE.

### 4.1 Compression Function \(f_{p}\)

The compression function \(f_p\), is an instance of the Parazoa *f*-function. It satisfies all the requirement of \(L_{in}, L_{out}\) functions. Since XOR is used, for any given \(x\in \mathbb {Z}^{s}_2\) and *V*, there will be only one \(M \in \mathbb {Z}^{s}_2\), thus satisfying the requirement.

The \(L_{in}(.,.)\) of *f* function is defined as XOR of *m*-bit M with *m* Most Significant Bit (MSB) of \(V_{i-1}\) and concatenating the XORed value with the \(s-m\) least significant bits of \(V_{i-1}\). More formally,

### 4.2 Extraction Function \(g_p\)

Extraction function \(g_p\) is an instance of the *g* function of the Parazoa. The *p*-most significant bits of \(V_{i-1}\) are output as *P*. Thus \(L_{ex}\) function is defined as below:

### 4.3 Indifferentiability Bound of *PPH*
        

We define a lemma using the adversarial advantage as given in Theorem 1 with little modification to define the advantage of an adversary for the practical parazoa function.

### 
                      **Lemma 1**
                    

                    The indifferentiability of PPH hash function is derived from Theorem [1].

where, *m* is the size of the message block.

          \(\mathbf{Insight\, on\, 2}^{{\varvec{s-max(m,p)}}}{} \mathbf{:}\) Consider the set of all couples (*V*, *x*) such that \(L_{in}(V,M)=x\) for some *M*. As shown in Fig. 2, it is required to make sure that, there is no internal \(\pi \) query collisions, so that the output, *y*, is always random which in turns makes \(P_i\) random. If \(P_i\) is random, then the output of this hash function will be indifferentiable with random oracle. Therefore, the adversary has control over *(i)* Compression function through *m*-bit message \(M_i\), *(ii)* Extraction function through *p*-bit output \(P_i\).

For a fixed \(P \in \mathbb {Z}^{p}_2\), there can be only one \(\lceil V \rceil ^{p}_{m} \in \mathbb {Z}^{p}_2\). Similarly, the message \(M \in \mathbb {Z}^{m}_2\) can be controlled by the adversary. Therefore, for a given *x* and fixed *M* there is only one *V*. Therefore, out of the \(2^{s}\) possible values for *V*, only \((2^{s-max(m-p)})\) values cannot be controlled by the adversary through *M* and *P*.

## 5 Practical Parazoa Authenticated Encryption Family (PPAE)

We propose a nonce based Associated Data supported Authenticated Encryption mode based on Practical Parazoa Hash family functions as described in Sect. 4. We describe PPAE, especially the modified *f* function to support the ciphertext. PPAE is shown in the Fig. 3.

### 5.1 Description

PPAE is a nonce based authenticated encryption mode which supports associated data *A*. It uses ideal permutation \(\pi \) as the underlying primitive. The IV used in PPAE is \(0^s\) and the internal state is of size *s* bits. PPAE takes *m*-bit key *K*, *m*-bit Nonce *N*, Associated Data *A* and Message *M* of variable size.

First *K* is used to initialize the mode. *N* and *A* are concatenated and padded using *pad* function as defined in Sect. 3. For *K* and \(pad(N\Vert A)\), \(f_p\)-function is used for compression. For every message block \(M_i\), one block of ciphertext \(C_i\) is produced using \(f_a\)-function. Once all the message blocks are compressed, then \(g_p\)-function is used to produce the *n*-bit tag *T*. The PPAE construction is shown in Fig. 3.

          \({\varvec{{f}_{a}}}\)-**function:** PPAE uses \(f_a\)-function as a modified version of \(f_p\)-function such that it produces ciphertext \(C_i\) for every \(M_i\) block. In this function, \(``m''\) most significant bits of the previous state \(\lceil V_{i-1}\rceil ^m_s\) are XOR’ed with the *m*-bit message \(M_i\) to form *m*-bit ciphertext \(C_i\). The \(f_a\)-function is shown in Fig. 4.

## 6 PPAE Security

### 6.1 PPAE: Privacy

Privacy of *PPAE* is defined as the advantage of the nonce respecting adversary to distinguish ciphertext from random string. Game playing framework [5] is used to find the advantage of the adversary. We define 7 games where Game *G*0 is the *PPAE* construction and Game *G*7 is a random oracle. The probability of the adversary to distinguish between each consecutive games are computed and union bound is applied to get the advantage of the adversary in distinguishing between a ciphertext and a random string.

The Theorem 2 provides the advantage of the adversary. Here *AE* means *PPAE*.

### 
                      *Proof*
                    

                    Game playing framework [5] is used to identify the adversary advantage for privacy of *PPAE*. Here, the initial game *G*0 represents *PPAE* construction and *G*7 represents random oracle. These subsequent games from *G*0 is modified with *bad* events such that the adversary can distinguish the given two consecutive games. The advantage of distinguishing the two games is the probability of occurrence of these *bad* events. Thus summing all the probability of occurrence of *bad* events in all the consecutive games gives the advantage of the adversary in distinguishing *PPAE* from random oracle.

In all the games *K* is chosen randomly from \(\mathbb {Z}^{m}_2\) and \(IV={0}^s\) to initialize the games. Each query takes Nonce, Associated Data and Message as input and returns corresponding Ciphertext and Tag. The adversary is nonce respecting.

Adversary can query \(\pi , \pi ^{-1}, AE\), at most \(q_{\pi }, q_{\pi ^{-1}}, q_{ae}\) times. Each \(q_{ae}\) queries \(\pi \) at most \((a+k+l+1)\) times. Thus, \(q_{ae}\) is bounded by \(q_{\pi }\) such that \((a+k+l+1) q_{ae} \le q_{\pi }\). We also define \(\sigma = q_{ae} + q_{\pi } +q_{\pi ^{-1}}\), overall internal permutation queries.

We define the term *state transition* where the input state is permuted to get a new output state. (i.e.) The input *x* is permuted using \(\pi \) to get *y*.

            **Game G0:** G0 perfectly simulates *PPAE*. G0 takes (*N*, *A*, *M*) as input and simulates our construction and outputs ciphertext *C* and tag *T*. *PPAE* queries uses \(\pi \) for state transition. \(\pi \) and \(\pi ^{-1}\) outputs a random permutation that is for every new input, output is different and random.

            **Game G1:** The \(\pi \) and \(\pi ^{-1}\) queries simulates random function that is for every new input, output is random, need not be different. Thus, G1 and G0 are identical games until the outputs of \(\pi \) and \(\pi ^{-1}\) queries collides with any of its previous outputs. This collision is denoted as *bad* event.

Set \(I_{\pi }\) stores all the (*x*, *y*) pairs of \(\pi \) and \(\pi ^{-1}\) queries. Since \(\pi , \pi ^{-1}\) is queried at most \(\sigma \) times by *PPAE* as well as adversary, there should not be any collision within this \(\sigma \) pairs. The bad event occurs when any of the pairs collides.

            **Game G2:** In G2, *PPAE* simulates random function and updates the set \(I_{\pi }\). Since the set is synchronized, the adversary cannot distinguish between G1 and G2. Thus, G2 and G1 are identical from adversary point of view.

            **Game G3:** In this game we use PRP/PRF switching Lemma [5] to make sure that all the output of internal state are random. For any two distinct input string, random permutation always output distinct strings, whereas random function might output same string. Thus, the advantage of the adversary in distinguishing between random function and permutation is the probability of same string output for two different input strings.

For a secure Authenticated Encryption, the ciphertext must be random so that the adversary cannot distinguish with Random Oracle output. So, we must make sure that the output ciphertext in each internal state must be random.

Also, since the *m*-bit input message \(M_i\) is controlled by the adversary and the output, *p*-bit \(P_i\) is also known, our construction cannot rely on these bits for random string. The output string is from the output state bits of the internal state transition. To create a random output state bits, the input to the state transition must be different from all the previous inputs. Since *max*(*m*, *p*)-bit is controlled by the adversary, \(s-max(m,p)\) bits needs to be different to make sure that input to the state transition is different.

Sets \(I_{l}\) and \(I_{lp}\) are used to store \(s-m\) LSB of *x* and \(s-p\) LSB of \(V_{k+i}\) (output of \(L_{out}\)) respectively. When \(s-m\) LSB of input collides with \(I_{l}\), it means that those bits have been already queried during the state transition. Even though the complete *s*-bit state may not be in \(I_{\pi }\), but still we make sure that the input to state transition is different by choosing a random value from \(\mathbb {Z}^{s-m}_2\) excluding the set \(I_{l}\). Similarly \(I_{lp}\) is used in extraction phase of *PPAE*.

In function, \(V_{i-1} \leftarrow L_{out}(y_{i-1},V_{i-2},M_{i-1})\), if \(V_{i-2}, M_{i-1}\) is fixed and \(y_{i-1}\) is random, then \(V_{i-1}\) is random. Since \(V_{i-1} \oplus M_{i} = C_{i}\). Therefore, \(C_{i}\) is random.

Similarly, in extraction function which outputs *p*-bit \(P_i\), we must make sure that \(s-p\) bit is always different from the set \(I_{p}\). Thus, for the complete construction, combining both the part, we must make sure that \(s-max(m,p)\) bit is different which cannot be controlled by the adversary.

If the adversary guesses the key correctly, then with probability 1 it can differentiate between both the games. Since the key is random, the probability of guessing the *m*-bit key will also become *bad* event.

Games G2 and G3 are identical until there is collision in the \((s-m)\) LSB of \(x_i\) in the set \(I_{l}\). The collision is denoted as *bad* event. If collision doesn’t occur in \(x_i\), then it is guaranteed that \(\lceil V_{i-1} \rceil ^{m}\) is random and \(\lfloor V_{i-1} \rfloor ^{s-m}\) is different.

            *Bad* event occurs when the input *x* to \(\pi \), collides with the elements in the set \(I_{\pi }\). Let \(Pr[\text{ coll }=1]\) be the probability of collisions which leads to occurrence of *bad* event. *Bad* event can also occur when the adversary guesses the key correctly. Thus,

Let \(Pr[coll_i]\) means that there is no collision till \(i-1\) queries and collision occurs in the \(i^{th}\) query. Therefore, \(Pr[\text{ coll }=1]\) is given by:

Since key is chosen randomly from \(\mathbb {Z}^m_2\), the probability of guessing the key is given as below:

From Eqs. (5), (6) and (7) we can derive [3] as given below:

            **Game G4:** In this game, we assign the output of state transition such that there will be no collisions. While assigning the *y* value Fig. 3, it is made sure that \((s- max(m,p))\) MSB of \(V_{i}\) is random and remaining bits are different from the set \(I_{l}\) or \(I_{lp}\) as required. This makes ciphertext as well as all \(P_i\) random. Therefore, from adversary point of view, both the games are identical.

            **Game G5:** Till now, both *PPAE* and \(\pi , \pi ^{-1}\) queries are synchronized by using \(I_{\pi }\) queries. Where as, in G5, *PPAE* queries doesn’t depend on set \(I_{\pi }\) making *PPAE* independent of \(\pi , \pi ^{-1}\). In G5, all the internal state transition *x*, *y* pairs are stored in the set \(I_{ae}\), and similarly \(\pi , \pi ^{-1}\) queries are stored in the set \(I_{\pi }\). If any of the internal queries in *PPAE* is present in \(I_{\pi }\), then we denote it as *bad* event and vise versa. This makes *AE* and \(\pi , \pi ^{-1}\) independent of each other.

            **Game G6:** In G6, *k*-blocks of *m*-bit \(C_i\) and *l*-blocks of *p*-bit \(P_i\) is chosen randomly to create ciphertext *C* and tag *T* accordingly. In G5 also, \(C_i\) and \(P_i\) are random. Therefore, from adversarial point of view G5 and G6 are identical.

            **Game G7:** G7 perfectly simulates VIL Random Oracle. In G7, *km* bits of ciphertext as well as *n* bits of tag is chosen randomly. From adversary point of view both G7 and G6 are identical.

Combining the probability difference between subsequent games, we will get the advantage of the adversary in differentiating *PPAE* and Random Oracle.

Using the Eqs. (1), (2), (3), (8), (9), (10), (11) and (12), we give the advantage of adversary.

This completes the proof of Theorem 2.

### 6.2 PPAE: Authenticity

The authenticity of the *PPAE* scheme is defined in terms of the ability of an adversary who can forge a valid (*N*, *C*, *T*) pair. The encryption and decryption functions in PPAE take key *K* and compress it and then answer queries from the adversary. Let us call these functions as encryption \(\mathbf {E}^{\pi ,\pi ^{-1}}\) and decryption \(\mathbf {D}^{\pi ,\pi ^{-1}}\) oracles respectively. For every (*N*, *A*, *M*) query to \(\mathbf {E}^{\pi ,\pi ^{-1}}\), the output (*C*, *T*) is stored in a set \(I_{auth}\) along with the nonce *N*.

The adversary is given access to these oracles as well as to \({\pi } \text {~and~} {\pi ^{-1}}\). Adversary \(\mathcal {A}\) can query \(\mathbf {E}^{\pi ,\pi ^{-1}}\), \(\mathbf {D}^{\pi ,\pi ^{-1}}\), \(\pi \text {~and~}\pi ^{-1}\) oracles at most \(q_e,q_d,q_{\pi },q_{\pi ^{-1}}\) times, respectively. Each query \(q_e \text { and } q_d\) can query the permutations \(\pi \text { and } \pi ^{-1}\) at most \(a+k+l+1\) times, where *a*, *k*, *l* are defined in Sect. 6.1. Finally, \(\sigma _{a} = q_e + q_d + q_{\pi } + q_{\pi ^{-1}}\) is the maximum number of queries allowed to \(\mathcal {A}\).

The adversary \(\mathcal {A}\) must be nonce-respecting for encryption queries only. After interacting with different oracles, \(\mathcal {A}\) outputs (*N*, *C*, *T*). We say that \(\mathcal {A}\) forged *PPAE* scheme if the decryption oracle outputs *M* for the given \((N,C,T) \notin I_{auth}\). The experiment outputs 1 if the forgery was successful and 0 otherwise. Mathematically, we say that \(\mathcal {A}\) forges the scheme if \(Exp^{auth}_{\text {PPAE},\pi ,\pi ^{-1}}(\mathcal {A})=1\). The advantage of the Adversary \(\mathcal {A}\) in forging the scheme is denoted by:

### 
                      *Proof*
                    

                    
            *(Authenticity).* The proof of this theorem is not being provided here due to space restrictions. It will be provided in the extended version of this work.

## 7 Examples

In this section, Keyak is instantiated using *PPAE* and derive the security bounds. Due to space constraint, more details will be provided in the extended version of this work.

### 7.1 Keyak

Keyak v1 [7] is one of the submissions to the CAESAR competition and is designed by the Keccak team. Keyak is based on the Duplex construction called DuplexWrap. This is similar to SpongeWrap [6] authenticated encryption mode.

          **Privacy of DuplexWrap.** The privacy advantage of DuplexWrap is

According to DuplexWrap, the security parameter is capacity *c*, \(c = s-max(m,p)\). Here, \(q_{ae} \ge \sigma \). Therefore, the privacy advantage of DuplexWrap using *PPAE* is

Therefore, the privacy advantage of the adversary of DuplexWrap is within the *PPAE* advantage given in Theorem 2.

          **Authenticity of DuplexWrap.** The authenticity advantage of the adversary for DuplexWrap is shown in Eq. 16. Let the size of tag *T* be *n* bits and the number of invocations of random permutation including the decryption queries be \(\sigma _{a}\).

The authenticity advantage for DupplexWrap using PPAE is derived below.

The higher bound compared to actual advantage is the extra cost for the general proof. Thus, the advantage of DuplexWrap is in accordance with advantage of *PPAE*.

## 8 Conclusion

In this work, we proposed *PPAE*, a new nonce based Authenticated Encryption with Associated Data family based on a variant of Parazoa hash family *PPH*. *PPAE* supports feed-forward operations which was lacking in sponge based construction. We also provided its privacy and authenticity security based on the indifferentiability security bounds of Parazoa. We also showed that Keyak [7] belong to the *PPAE* family and claim that Ascon [9] and NORX [3] also belong to the *PPAE* family.

## Author information

### Authors and Affiliations

### Corresponding author

## Editor information

### Editors and Affiliations

## Rights and permissions

## Copyright information

© 2015 Springer International Publishing Switzerland

## About this paper

### Cite this paper

Chang, D., R., S.M., Sanadhya, S.K. (2015). PPAE: Practical Parazoa Authenticated Encryption Family. In: Au, MH., Miyaji, A. (eds) Provable Security. ProvSec 2015. Lecture Notes in Computer Science(), vol 9451. Springer, Cham. https://doi.org/10.1007/978-3-319-26059-4_11

### Download citation

- DOI: https://doi.org/10.1007/978-3-319-26059-4_11 
- Published: 
- Publisher Name: Springer, Cham 
- Print ISBN: 978-3-319-26058-7 
- Online ISBN: 978-3-319-26059-4 
- eBook Packages: Computer ScienceComputer Science (R0)Springer Nature Proceedings Computer Science