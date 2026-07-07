## **NIST Special Publication 800-90A Revision 1** 

# **Recommendation for Random Number Generation Using Deterministic Random Bit Generators** 

Elaine Barker John Kelsey 

This publication is available free of charge from: http://dx.doi.org/10.6028/NIST.SP.800-90Ar1 

C O M P U T E R S E C U R I T Y 

## **NIST Special Publication 800-90A Revision 1** 

# **Recommendation for Random Number Generation Using Deterministic Random Bit Generators** 

Elaine Barker John Kelsey _Computer Security Division Information Technology Laboratory_ 

This publication is available free of charge from: http://dx.doi.org/10.6028/NIST.SP.800-90Ar1 

June 2015 

U.S. Department of Commerce _Penny Pritzker, Secretary_ 

National Institute of Standards and Technology _Willie May, Under Secretary of Commerce for Standards and Technology and Director_ 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

##### **Authority** 

This publication has been developed by NIST to further its statutory responsibilities under the Federal Information Security Modernization Act (FISMA) of 2014, 44 U.S.C. § 3541 _et seq._ , Public Law (P.L.) 113-283. NIST is responsible for developing information security standards and guidelines, including minimum requirements for Federal information systems, but such standards and guidelines shall not apply to national security systems without the express approval of appropriate Federal officials exercising policy authority over such systems. This guideline is consistent with the requirements of the Office of Management and Budget (OMB) Circular A-130, Section 8b(3), _Securing Agency Information Systems_ , as analyzed in Circular A-130, Appendix IV: _Analysis of Key Sections_ . Supplemental information is provided in Circular A-130, Appendix III, _Security of Federal Automated Information Resources_ . 

Nothing in this publication should be taken to contradict the standards and guidelines made mandatory and binding on Federal agencies by the Secretary of Commerce under statutory authority. Nor should these guidelines be interpreted as altering or superseding the existing authorities of the Secretary of Commerce, Director of the OMB, or any other Federal official. This publication may be used by nongovernmental organizations on a voluntary basis and is not subject to copyright in the United States. Attribution would, however, be appreciated by NIST. 

National Institute of Standards and Technology Special Publication 800-90A Revision 1 Natl. Inst. Stand. Technol. Spec. Publ. 800-90A Rev. 1, 109 pages (June 2015) CODEN: NSPUE2 

This publication is available free of charge from: http://dx.doi.org/10.6028/NIST.SP.800-90Ar1 

Certain commercial entities, equipment, or materials may be identified in this document in order to describe an experimental procedure or concept adequately. Such identification is not intended to imply recommendation or endorsement by NIST, nor is it intended to imply that the entities, materials, or equipment are necessarily the best available for the purpose. 

There may be references in this publication to other publications currently under development by NIST in accordance with its assigned statutory responsibilities. The information in this publication, including concepts and methodologies, may be used by Federal agencies even before the completion of such companion publications. Thus, until each publication is completed, current requirements, guidelines, and procedures, where they exist, remain operative. For planning and transition purposes, Federal agencies may wish to closely follow the development of these new publications by NIST. 

Organizations are encouraged to review all draft publications during public comment periods and provide feedback to NIST. All NIST Computer Security Division publications, other than the ones noted above, are available at <u>http://csrc.nist.gov/publications.</u> 

##### **Comments may be provided to:** 

National Institute of Standards and Technology Attn: Computer Security Division, Information Technology Laboratory 100 Bureau Drive (Mail Stop 8930) Gaithersburg, MD 20899-8930 Email: rbg_comments@nist.gov 

ii 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **Reports on Computer Systems Technology** 

The Information Technology Laboratory (ITL) at the National Institute of Standards and Technology (NIST) promotes the U.S. economy and public welfare by providing technical leadership for the Nation’s measurement and standards infrastructure. ITL develops tests, test methods, reference data, proof of concept implementations, and technical analyses to advance the development and productive use of information technology. ITL’s responsibilities include the development of management, administrative, technical, and physical standards and guidelines for the cost-effective security and privacy of other than national security-related information in Federal information systems. The Special Publication 800-series reports on ITL’s research, guidelines, and outreach efforts in information system security, and its collaborative activities with industry, government, and academic organizations. 

#### **Abstract** 

This Recommendation specifies mechanisms for the generation of random bits using deterministic methods. The methods provided are based on either hash functions or block cipher algorithms. 

#### **Keywords** 

Deterministic random bit generator (DRBG); entropy; hash function; random number generator. 

#### **Table of Contents** 

|**1**<br>**In**|**troduc**|**tion .................................................................................................... 1**|
|---|---|---|
|**2**<br>**C**|**onform**|**ance Testing .................................................................................... 1**|
|**3**<br>**S**|**cope ...**|**........................................................................................................... 1**|
|**4**<br>**T**|**erms a**|**nd Definitions ................................................................................... 3**|
|**5**<br>**S**|**ymbols**|**and Abbreviated Terms ................................................................. 9**|
|**6**<br>**D**|**ocume**|**nt Organization............................................................................... 10**|
|**7**<br>**F**|**unction**|**al Model of a DRBG....................................................................... 11**|
|**7.1**|**Entrop**|**y Input .................................................................................................................. 11**|
|**7.2**|**Other**|**Inputs .................................................................................................................... 12**|
|**7.3**|**The In**|**ternal State ........................................................................................................... 12**|
|**7.4**|**The D**|**RBG Mechanism Functions................................................................................. 12**|
|**8.**<br>**D**|**RBG M**|**echanism Concepts and General Requirements........................ 13**|
|**8.1**|**DRBG**|**Mechanism Functions ........................................................................................ 13**|
|**8.2**|**DRBG**|**Instantiations....................................................................................................... 13**|
|**8.3**|**Interna**|**l States................................................................................................................. 13**|
|**8.4**|**Securi**|**ty Strengths Supported by an Instantiation...................................................... 14**|
|**8.5**|**DRBG**|**Mechanism Boundaries...................................................................................... 15**|
|**8.6**|**Seeds**|**............................................................................................................................... 17**|
||**8.6.1**|**Seed Construction for Instantiation ................................................................ 18**|
||**8.6.2**|**Seed Construction for Reseeding ................................................................... 18**|
||**8.6.3**|**Entropy Requirements for the Entropy Input ................................................. 18**|
||**8.6.4**|**Seed Length....................................................................................................... 19**|
||**8.6.5**|**Randomness Source......................................................................................... 19**|
||**8.6.6**|**Entropy Input and Seed Privacy ...................................................................... 19**|
||**8.6.7**|**Nonce.................................................................................................................. 19**|
||**8.6.8**|**Reseeding .......................................................................................................... 20**|
||**8.6.9**|**Seed Use ............................................................................................................ 21**|
||**8.6.10**|**Entropy Input and Seed Separation ................................................................ 21**|
|**8.7**|**Other**|**Input to the DRBG Mechanism .......................................................................... 21**|
||**8.7.1**|**Personalization String....................................................................................... 21**|
||**8.7.2**|**Additional Input ................................................................................................. 22**|

iv 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

|**8.8**|**Predic**|**tion Resis**|**tance and Backtracking Resistance................................................. 23**|
|---|---|---|---|
|**9**<br>**DR**|**BG M**|**echanis**|**m Functions...................................................................... 25**|
|**9.1**|**Instant**|**iating a D**|**RBG...................................................................................................... 26**|
|**9.2**|**Resee**|**ding a DR**|**BG Instantiation .................................................................................. 29**|
|**9.3**|**Gener**|**ating Pse**|**udorandom Bits Using a DRBG.......................................................... 31**|
||**9.3.1**|**The Gen**|**erate Function ..................................................................................... 32**|
||**9.3.2**|**Reseedi**|**ng at the End of the Seedlife .............................................................. 35**|
||**9.3.3**|**Handling**|**Prediction Resistance Requests ..................................................... 35**|
|**9.4**|**Remov**|**ing a DR**|**BG Instantiation ................................................................................... 36**|
|**10**<br>**DR**|**BG Al**|**gorithm**|**Specifications ................................................................. 37**|
|**10.1 **|**DRBG**|**Mechanis**|**ms Based on Hash Functions ........................................................... 37**|
||**10.1.1**|**Hash_D**|**RBG ....................................................................................................... 38**|
|||**10.1.1.1**|**Hash_DRBG Internal State .............................................................. 39**|
|||**10.1.1.2**|**Instantiation of Hash_DRBG ............................................................ 39**|
|||**10.1.1.3**|**Reseeding a Hash_DRBG Instantiation ......................................... 40**|
|||**10.1.1.4**|**Generating Pseudorandom Bits Using Hash_DRBG .................... 41**|
||**10.1.2**|**HMAC_D**|**RBG ..................................................................................................... 43**<br>|
|||**10.1.2.1**|**HMAC_DRBG Internal State ............................................................ 43**|
|||**10.1.2.2**|**The HMAC_DRBG Update Function (Update)................................ 44**|
|||**10.1.2.3**|**Instantiation of HMAC_DRBG ......................................................... 45**|
|||**10.1.2.4**|**Reseeding an HMAC_DRBG Instantiation ..................................... 46**|
|||**10.1.2.5**|**Generating Pseudorandom Bits Using HMAC_DRBG .................. 46**|
|**10.2 **|**DRBG**|**Mechanis**|**m Based on Block Ciphers................................................................ 48**|
||**10.2.1**|**CTR_DR**|**BG......................................................................................................... 48**|
|||**10.2.1.1**|**CTR_DRBG Internal State................................................................ 50**|
|||**10.2.1.2**|**The Update Function (CTR_DRBG_Update) .................................. 51**|
|||**10.2.1.3**|**Instantiation of CTR_DRBG............................................................. 52**|
|||**10.2.1.4**|**Reseeding a CTR_DRBG Instantiation........................................... 54**|
|||**10.2.1.5**|**Generating Pseudorandom Bits Using CTR_DRBG ..................... 55**|
|**10.3**|**Auxili**|**ary Functi**|**ons ....................................................................................................... 58**|
||**10.3.1**|**Derivatio**|**n Function Using a Hash Function (Hash_df) ................................. 58**|
||**10.3.2**|**Derivatio**|**n Function Using a Block Cipher Algorithm (Block_Cipher_df).... 59**|

v 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

||**10.3.3**<br>**BCC and Block_Encrypt ................................................................................... 60**|
|---|---|
|**11**<br>**As**|**surance..................................................................................................... 62**|
|**11.1**|**Minimal Documentation Requirements....................................................................... 62**|
|**11.2**|**Implementation Validation Testing.............................................................................. 63**|
|**11.3 **|**Health Testing................................................................................................................. 63**|
||**11.3.1**<br>**Known Answer Testing..................................................................................... 64**|
||**11.3.2**<br>**Testing the Instantiate Function ...................................................................... 64**|
||**11.3.3**<br>**Testing the Generate Function ........................................................................ 64**|
||**11.3.4**<br>**Testing the Reseed Function ........................................................................... 65**|
||**11.3.5**<br>**Testing the Uninstantiate Function ................................................................. 65**|
|**11.4 **|**Error Handling................................................................................................................. 65**|
||**11.4.1**<br>**Errors Encountered During Normal Operation............................................... 65**|
||**11.4.2**<br>**Errors Encountered During Health Testing .................................................... 65**|
|**Appen**|<br>**dix A: (Normative) Conversion and Auxiliary Routines ....................... 67**|
|**A.1**|**Bitstring to an Integer .................................................................................................... 67**|
|**A.2**|**Integer to a Bitstring ...................................................................................................... 67**|
|**A.3**|**Integer to a Byte String.................................................................................................. 68**|
|**A.4**|**Byte String to an Integer................................................................................................ 68**|
|**A.5**|**Converting Random Bits into a Random Number....................................................... 68**|
||**A.5.1**<br>**The Simple Discard Method ............................................................................. 69**|
||**A.5.2**<br>**The Complex Discard Method.......................................................................... 69**|
||**A.5.3**<br>**The Simple Modular Method ............................................................................ 70**|
|**Appen**<br>**...**|<br>**dix B: (Informative) Example Pseudocode for Each DRBG Mechanism**<br>**.................................................................................................................... 71**|
|**B.1**|**Hash_DRBG Example .................................................................................................... 71**|
||**B.1.1**<br>**Instantiation of Hash_DRBG............................................................................. 72**|
||**B.1.2**<br>**Reseeding a Hash_DRBG Instantiation........................................................... 73**|
||**B.1.3**<br>**Generating Pseudorandom Bits Using Hash_DRBG ..................................... 74**|
|**B.2**|**HMAC_DRBG Example .................................................................................................. 76**|
||**B.2.1**<br>**Instantiation of HMAC_DRBG........................................................................... 77**|
||**B.2.2**<br>**Generating Pseudorandom Bits Using HMAC_DRBG ................................... 78**|
|**B.3**|**CTR_DRBG Example Using a Derivation Function ..................................................... 80**|
||**B.3.1**<br>**The CTR_DRBG_Update Function................................................................... 80**|

vi 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

||**B.3.2**<br>**Instantiation of CTR_DRBG Using a Derivation Function ............................. 81**<br>**B.3.3**<br>**Reseeding a CTR_DRBG Instantiation Using a Derivation Function ........... 82**|
|---|---|
||**B.3.4**<br>**Generating Pseudorandom Bits Using CTR_DRBG....................................... 84**|
|**B.4**|**CTR_DRBG Example Without a Derivation Function.................................................. 86**|
||**B.4.1**<br>**The CTR_DRBG_Update Function................................................................... 86**|
||**B.4.2**<br>**Instantiation of CTR_DRBG Without a Derivation Function.......................... 86**|
||**B.4.3**<br>**Reseeding a CTR_DRBG Instantiation Without a Derivation Function........ 86**|
||**B.4.4**<br>**Generating Pseudorandom Bits Using CTR_DRBG....................................... 87**|
|**Appen**|<br>**dix C: (Informative) DRBG Mechanism Selection................................. 88**|
|**C.1**|**Hash_DRBG .................................................................................................................... 88**|
|**C.2**|**HMAC_DRBG .................................................................................................................. 89**|
|**C.3**|**CTR_DRBG...................................................................................................................... 90**|
|**C.4**|**Summary for DRBG Selection....................................................................................... 92**|
|**Appen**|**dix D : (Informative) References.............................................................. 93**|
|**Appen**|**dix E : (Informative) Revisions ................................................................ 95**|

|**List of Figures**|
|---|
|**Figure 1: DRBG Functional Model............................................................................................................11**|
|**Figure 2: DRBG Instantiation....................................................................................................................13**|
|**Figure 3: DRBG Mechanism Functions within a Single Device.............................................................16**|
|**Figure 4: Distributed DRBG Mechanism Functions ...............................................................................17**|
|**Figure 5: Seed Construction for Instantiation.........................................................................................18**|
|**Figure 6: Seed Construction for Reseeding............................................................................................18**|
|**Figure 7: Sequence of DRBG States........................................................................................................23**|
|**Figure 8: Hash_DRBG ...............................................................................................................................39**|
|**Figure 9: HMAC_DRBG Generate Function.............................................................................................43**|
|**Figure 10: HMAC_DRBG_Update Function.............................................................................................44**|
|**Figure 11: CTR_DRBG Update Function .................................................................................................48**|
|**Figure 12: CTR-DRBG................................................................................................................................50**|
|**List of Tables**|
|**Table 1: Possible Instantiated Security Strengths .................................................................................14**|
|**Table 2: Definitions for Hash-Based DRBG Mechanisms......................................................................38**|
|**Table 3: Definitions for the CTR_DRBG...................................................................................................49**|

vii 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Table C-1: DRBG Mechanism Summary..................................................................................................92** 

viii 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **2 Conformance Testing** 

Conformance testing for implementations of this Recommendation will be conducted within the framework of the Cryptographic Module Validation Program (CMVP) and the Cryptographic Algorithm Validation Program (CAVP). The requirements of this Recommendation are indicated by the word “ **shall** .” Some of these requirements may be out-of-scope for CMVP or CAVP validation testing, and thus are the responsibility of entities using, implementing, installing or configuring applications that incorporate this Recommendation. 

### **3 Scope** 

This Recommendation includes: 

1. Requirements for the use of DRBG mechanisms, 

2. Specifications for DRBG mechanisms that use hash functions and block ciphers, 

3. Implementation issues, and 

4. Assurance considerations. 

> 1 NRBGs have also been called True Random Number (or Bit) Generators or Hardware Random Number Generators. 

- 2 DRBGS have also been called Pseudorandom Number (or Bit) Generators. 

1 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

This Recommendation specifies several DRBG mechanisms, all of which provided acceptable security when this Recommendation was published. However, in the event that new attacks are found on a particular class of DRBG mechanisms, a diversity of **approved** mechanisms will allow a timely transition to a different class of DRBG mechanism. 

Random number generation does not require interoperability between two entities, i.e., communicating entities may use different DRBG mechanisms without affecting their ability to communicate. Therefore, an entity may choose a single, appropriate DRBG mechanism for their consuming applications; see <u>Appendix C for a discussion of DRBG mechanism selection.</u> 

The precise structure, design and development of a random bit generator is outside the scope of this document. 

NIST Special Publication (SP) 800-90B [SP 800-90B] provides guidance on designing and validating entropy sources. SP 800-90C [SP 800-90C] provides guidance on the construction of an RBG from a randomness source and an **approved** DRBG mechanism from this document (i.e., SP 800-90A). 

2 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **4 Terms and Definitions** 

|Algorithm|A clearly specified mathematical process for computation; a<br>set of rules that, if followed, will give a prescribed result.|
|---|---|
|Approved|FIPS-approved, NIST-Recommended and/or validated by the<br>Cryptographic Algorithm Validation Program (CAVP).|
|Approved entropy source|An entropy source that has been validated as conforming to<br>[SP 800-90B].|
|Backtracking Resistance|<br> <br>An RBG provides_backtracking resistance_relative to time_T_if<br>it provides assurance that an adversary that has knowledge of<br>the state of the RBG at some time(s) subsequent to time_T_(but<br>incapable of performing work that matches the claimed<br>security strength of the RBG) would be unable to distinguish<br>between observations of_ideal random bitstrings _and<br>(previously unseen) bitstrings that are output by the RBG at or<br>prior to time_T_. In particular, an RBG whose design allows the<br>adversary to "backtrack" from the initially-compromised RBG<br>state(s) to obtain knowledge of prior RBG states and the<br>corresponding outputs (including the RBG state and output at<br>time_T_) wouldnotprovide backtracking resistance relative to<br>time_T_. (Contrast with _prediction resistance_.)|
|Biased|<br>A value that is chosen from a sample space is said to be biased<br>if one value is more likely to be chosen than another value.<br>Contrast with _unbiased_.|
|Bitstring|A bitstring is an ordered sequence of 0’s and 1’s.|
|Bitwise Exclusive-Or|An operation on two bitstrings of equal length that combines<br>corresponding bits of each bitstring using an exclusive-or<br>operation.|
|Block Cipher|A symmetric-key cryptographic algorithm that transforms one<br>block of information at a time using a cryptographic key. For<br>a block cipher algorithm, the length of the input block is the<br>same as the length of the output block.|
|Consuming Application|The application (including middleware) that uses random<br>numbers or bits obtained from an**approved**random bit<br>generator.|
|Cryptographic Key (Key)|A parameter that determines the operation of a cryptographic<br>function, such as:<br>1. The transformation from plaintext to ciphertext and<br>vice versa,|

3 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

||2. The generation of keying material, or<br>3. A digital signature computation or verification.|
|---|---|
|Deterministic Algorithm|An algorithm that, given the same inputs, always produces the<br>same outputs.|
|Deterministic Random<br>Bit Generator (DRBG)|An RBG that includes a DRBG mechanism and (at least<br>initially) has access to a randomness source. The DRBG<br>produces a sequence of bits from a secret initial value called a<br>seed_,_along with other possible inputs. A DRBG is often<br>called a Pseudorandom Number (or Bit) Generator. Contrast<br>with _NRBG_.|
|DRBG Mechanism|The portion of an RBG that includes the functions necessary<br>to instantiate and uninstantiate the RBG, generate<br>pseudorandom bits, (optionally) reseed the RBG and test the<br>health of the the DRBG mechanism.|
|DRBG Mechanism<br>Boundary|A conceptual boundary that is used to explain the operations<br>of a DRBG mechanism and its interaction with and relation to<br>other processes. (See_min-entropy_.)|
|Entropy|A measure of the disorder, randomness or variability in a<br>closed system. Min-entropy is the measure used in this<br>Recommendation.|
|Entropy Input|An input bitstring that provides an assessed minimum amount<br>of unpredictability for a DRBG mechanism. (See_min-_<br>_entropy_.)|
|Entropy Source|A combination of a noise source (e.g., thermal noise or hard<br>drive seek times), health tests, and an optional conditioning<br>component. The entropy source produces random bitstrings to<br>be used by an RBG.|
|Equivalent Process|Two processes are equivalent if, when the same values are<br>input to each process, the same output is produced.|
|Exclusive-or|<br> <br> <br>A mathematical operation; the symbol⊕, defined as:<br>0⊕ 0 = 0<br>1⊕ 0 = 1<br>0⊕ 1 = 1<br>1⊕ 1 = 0<br>Equivalent to binary addition without carry.|
|Fresh Entropy|A bitstring output from an entropy source, an NRBG or a<br>DRBG that has access to a Live Entropy Source that is being<br>used to provide prediction resistance.|
|Full Entropy|For the purposes of this Recommendation, a source of full-<br>entropy bitstrings serves as a practical approximation to a|

4 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

||source of ideal random bitstrings of the same length (see _ideal_<br>_random sequence_).|
|---|---|
|Hash Function|A (mathematical) function that maps values from a large<br>(possibly very large) domain into a smaller range. The<br>function satisfies the following properties:<br>1. (One-way) It is computationally infeasible to find any<br>input that maps to any pre-specified output;<br>2. (Collision free) It is computationally infeasible to find<br>any two distinct inputs that map to the same output.|
|Health Testing|Testing within an implementation immediately prior to or<br>during normal operation to determine that the implementation<br>continues to perform as implemented and as validated.|
|Ideal Random Bitstring|See_Ideal Random Sequence_.|
|Ideal Random Sequence|<br> <br>Each bit of an ideal random sequence is unpredictable and<br>unbiased, with a value that is independent of the values of the<br>other bits in the sequence. Prior to the observation of the<br>sequence, the value of each bit is equally likely to be 0 or 1,<br>and the probability that a particular bit will have a particular<br>value is unaffected by knowledge of the values of any or all of<br>the other bits. An ideal random sequence of _n_bits contains _n_<br>bits of entropy.|
|Implementation|An implementation of an RBG is a cryptographic device or<br>portion of a cryptographic device that is the physical<br>embodiment of the RBG design, for example, some code<br>running on a computing platform.|
|Implementation Testing<br>for Validation|Testing by an independent and accredited party to ensure that<br>an implementation of this Recommendation conforms to the<br>specifications of this Recommendation.|
|Instantiation of an RBG|An instantiation of an RBG is a specific, logically<br>independent, initialized RBG.  One instantiation is<br>distinguished from another by a “handle” (e.g., an identifying<br>number).|
|Internal State|The collection of stored information about a DRBG<br>instantiation. This can include both secret and non-secret<br>information. Compare to _working state_.|
|Key|See_Cryptographic Key_.|
|Live Entropy Source|An**approved**entropy source (see [SP 800-90B]) that can<br>providean RBG withbitshavingaspecifiedamountof|

5 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

||entropy immediately upon request or within an acceptable<br>amount of time, as determined by the user or application<br>relying upon that RBG.|
|---|---|
|Min-entropy|<br> <br> <br> <br>The_min-entropy_(in bits) of a random variable_X_is the largest<br>value_m_having the property that each observation of_X_<br>provides at least_m_bits of information (i.e., the min-entropy of<br>_X_is the greatest lower bound for the information content of<br>potential observations of_X_). The min-entropy of a random<br>variable is a lower bound on its entropy. The precise<br>formulation for min-entropy is−(log2max_pi_) for a discrete<br>distribution having_n_possible outputs with probabilities_p_1,…,<br>_pn_. Min-entropy is often used as a worst-case measure of the<br>unpredictability of a random variable. Also see[SP 800-90B].|
|Non-Deterministic<br>Random Bit Generator<br>(Non-deterministic RBG)<br>(NRBG)|An RBG that always has access to an _entropy source_and<br>(when working properly) produces output bitstrings that have<br>_full entropy_.Often called a True Random Number (or Bit)<br>Generator. (Contrast with a_deterministic random bit_<br>_generator_).|
|Nonce|A time-varying value that has at most a negligible chance of<br>repeating, e.g., a random value that is generated anew for each<br>use, a timestamp, a sequence number, or some combination of<br>these.|
|Personalization String|An optional string of bits that is combined with a secret<br>entropy input and (possibly) a nonce to produce a seed.|
|Prediction Resistance|<br>An RBG provides prediction resistance relative to time_T_if it<br>provides assurance that an adversary with knowledge of the<br>state of the RBG at some time(s) prior to_T_(but incapable of<br>performing work that matches the claimed_security strength_of<br>the RBG) would be unable to distinguish between<br>observations of ideal random bitstrings and (previously<br>unseen) bitstrings output by the RBG at or subsequent to time<br>_T_. In particular, an RBG whose design allows the adversary to<br>step forward from the initially compromised RBG state(s) to<br>obtain knowledge of subsequent RBG states and the<br>corresponding outputs (including the RBG state and output at<br>time_T_) wouldnotprovide prediction resistance relative to<br>time_T_. (Contrast with _backtracking resistance_.)|
|Pseudorandom|A process (or data produced by a process) is said to be<br>pseudorandom when the outcome is deterministic, yet also<br>effectively random, as long as the internal action of the<br>process is hidden from observation.  For cryptographic<br>purposes,“effectively”means“within the limits of the|

6 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

||<br>intended cryptographic strength.”|
|---|---|
|Pseudorandom Number<br>Generator|See_Deterministic Random Bit Generator_.|
|Random Number|For the purposes of this Recommendation, a value in a set that<br>has an equal probability of being selected from the total<br>population of possibilities and, hence, is unpredictable.  A<br>random number is an instance of an unbiased random variable,<br>that is, the output produced by a uniformly distributed random<br>process.|
|Random Bit Generator<br>(RBG)|A device or algorithm that outputs a sequence of binary bits<br>that appears to be statistically independent and unbiased. An<br>RBG is either a DRBG or an NRBG.|
|Randomness Source|A component of a DRBG (which consists of a DRBG<br>mechanism and a randomness source) that outputs bitstrings<br>that are used as entropy input by the DRBG mechanism. The<br>randomness source can be an entropy source or an RBG.|
|Reseed|To acquire additional bits that will affect the internal state of<br>the DRBG mechanism.|
|Secure Channel|A path for transferring data between two entities or<br>components that ensures confidentiality, integrity and replay<br>protection, as well as mutual authentication between the<br>entities or components. The secure channel may be provided<br>using**approved**cryptographic, physical or procedural<br>methods, or a combination thereof. Sometimes called a trusted<br>channel.|
|Security Strength|<br>A number associated with the amount of work (that is, the<br>number of operations of some sort) that is required to break a<br>cryptographic algorithm or system in some way. In this<br>Recommendation, the security strength is specified in bits and<br>is a specific value from the set {112, 128, 192, 256}. If the<br>security strength associated with an algorithm or system is_S_<br>bits, then it is expected that (roughly) 2<sup>_S_</sup>basic operations are<br>required to break it.|
|Seed|Noun : A string of bits that is used as input to a DRBG<br>mechanism. The seed will determine a portion of the internal<br>state of the DRBG, and its entropy must be sufficient to<br>support the security strength of the DRBG.<br>Verb : To acquire bits with sufficient entropy for the desired<br>security strength. These bits will be used as input to a DRBG<br>mechanism to determineaportionof theinitial internalstate.|

7 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

||Also see_reseed_.|
|---|---|
|Seedlife|The length of the seed period.|
|Seed Period|The period of time between instantiating or reseeding a DRBG<br>with one seed and reseeding that DRBG with another seed.|
|Sequence|An ordered set of quantities.|
|Shall|Used to indicate a requirement of this Recommendation.<br>"**Shall**" may be coupled with "not" to become "**shall not**."|
|Should|Used to indicate a highly desirable feature for a DRBG<br>mechanism<br>that<br>is<br>not<br>necessarily required by this<br>Recommendation. "**Should**" may be coupled with "not" to<br>become "**should not**."|
|Source of Randomness|See_Randomness Source_.|
|String|See_Bitstring_.|
|Unbiased|A value that is chosen from a sample space is said to be<br>unbiased if all potential values have the same probability of<br>being chosen. Contrast with_biased_.|
|Uninstantiate|The termination of a DRBG instantiation.|
|Unpredictable|In the context of random bit generation, an output bit is<br>unpredictable if an adversary has only a negligible advantage<br>(that is, essentially not much better than chance) in predicting<br>it correctly.|
|Working State|A subset of the internal state that is used by a DRBG<br>mechanism to produce pseudorandom bits at a given point in<br>time. The working state (and thus, the internal state) is<br>updated to the next state prior to producing another string of<br>pseudorandom bits.|

8 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **5 Symbols and Abbreviated Terms** 

The following abbreviations are used in this Recommendation: 

|**Abbreviation**|**Meaning**|
|---|---|
|AES|<br>Advanced Encryption Standard,as specified in[FIPS 197].|
|DRBG|Deterministic Random Bit Generator.|
|FIPS|Federal Information ProcessingStandard.|
|HMAC|Keyed-Hash Message Authentication Code,as specified in[FIPS 198].|
|NIST|National Institute of Standards and Technology.|
|NRBG|Non-deterministic Random Bit Generator.|
|RBG|Random Bit Generator.|
|SP|NIST Special Publication.|
|TDEA|Triple Data Encryption Algorithm,as specified in[SP 800-67].|

The following symbols are used in this Recommendation: 

|**Symbol**|**Meaning**|
|---|---|
|+|Addition.|
|_X_⊕ _Y_|Bitwise exclusive-or (also bitwise addition modulo 2) of two bitstrings<br>_X_and_Y_of the same length.|
|_X || Y_|<br>Concatenation of two strings_X_and_Y_._X_and_Y_are either both bitstrings<br>or both byte strings.|
|⎡_x_⎤|The ceiling of_x_; the smallest integer ≥ _x_. For example,⎡5⎤ = 5, and<br>⎡5.3⎤ = 6.|
|**leftmost**(_V_,_a_)|<br>The leftmost_a_bits of_V_.|
|**len**(_a_)|The length in bits of string_a_.|
|**min**(_a_,_b_)|<br>The minimum of_a_and_b_.|
|<br>_x_**mod**_n_|The unique remainder_r_(where 0≤ _r_≤ _n_-1) when integer_x_is divided<br>by_n_. For example, 23 mod 7 = 2.|
|**rightmost**(_V_,_a_)|<br>The rightmost_a_bits of_V_.|
|**select**(_V_,_a_,_b_)|<br>A substring of string_V_consisting of bit_a_through bit_b_.|
||Used in a figure to illustrate a "switch" between input sources.|
|{_a_1, ..._a_i}|<br>The internal state of the DRBG at a point in time. The types and<br>number of the_ai _values depends on the specific DRBG mechanism.|

9 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

|**Symbol**|**Meaning**|
|---|---|
|0x_ab_|<br>Hexadecimal notation that is used to define a byte (i.e., eight bits) of<br>information, where_a_and_b_each specify four bits of  information and<br>have values from the range {0, 1, 2,…F}. For example, 0xc6 is used to<br>represent 11000110, where c is 1100, and 6 is 0110.|
|0<sup>_x_</sup>|<br>A string of_x_zero bits.|

### **6 Document Organization** 

This Recommendation is organized as follows: 

- ⎯ <u>Section 7 provides a functional model for a DRBG that uses a DRBG mechanism and</u> discusses the major components of the DRBG mechanism. 

- ⎯ <u>Section 8 provides concepts and general requirements for the implementation and use of a</u> DRBG mechanism. 

⎯ <u>Section 9 specifies the functions of a DRBG mechanism that were introduced in Section 8.</u> These functions use the DRBG algorithms specified in Section 10. 

- ⎯ <u>Section 10 specifies</u> **approved** DRBG algorithms. Algorithms have been specified that are based on the hash functions specified in [FIPS 180], and the block cipher algorithms specified in [FIPS 197] and [SP 800-67] (AES and TDEA, respectively). 

- ⎯ <u>Section 11 addresses assurance issues for DRBG mechanisms, including documentation</u> requirements, and implementation validation and health testing. 

This Recommendation also includes the following appendices: 

- ⎯ <u>Appendix A</u> provides conversion routines. 

- ⎯ <u>Appendix B provides example pseudocode for each DRBG mechanism. Examples of the</u> values computed for the DRBGs using each **approved** cryptographic algorithm and key size are available at http://csrc.nist.gov/groups/ST/toolkit/examples.html under the entries for SP 800-90A. 

- ⎯ <u>Appendix C provides a discussion on DRBG mechanism selection.</u> 

⎯ <u>Appendix D</u> provides references. 

- ⎯ <u>Appendix E provides a list of modifications to SP 800-90A since it was first published.</u> 

10 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **7 Functional Model of a DRBG** 

Figure 1 provides a functional model of a DRBG (i.e., one type of RBG). A DRBG **shall** implement an **approved** DRBG mechanism from SP 800-90A and at least one **approved** randomness source (see <u>Section 8.6.5), and may include additional optional sources, including</u> sources for nonces, personalization strings, and additional input. The components of this model are discussed in the following subsections. DRBG constructions are also discussed in [SP 800- <u>90C].</u> 

###### **Figure 1: DRBG Functional Model** 

#### **7.1 Entropy Input** 

Entropy input is provided to a DRBG mechanism for the seed (see Section 8.6) using a randomness source. The entropy input and the seed **shall** be kept secret. The secrecy of this information provides the basis for the security of the DRBG. At a minimum, the randomness source **shall** provide input that supports the security strength requested by the DRBG mechanism. Appropriate randomness sources are discussed in Section 8.6.5. 

Ideally, the entropy input would have full entropy; however, the DRBG mechanisms have been specified so that input with full entropy is not required. This is accommodated by allowing the length of the entropy input to be longer than the required entropy (expressed in bits), as long as the total entropy meets the requirements of the DRBG mechanism. The entropy input can be defined to be of variable length (within specified limits), as well as fixed length. In all cases, the DRBG mechanism expects that when entropy input is requested, the returned bitstring will contain at least the requested amount of entropy. Additional entropy beyond the amount requested is not required, but is desirable. 

11 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **7.2 Other Inputs** 

Other information may be obtained by a DRBG mechanism as input. This information may or may not be required to be kept secret by a consuming application; however, the security of the DRBG itself does not rely on the secrecy of this information. The information **should** be checked for validity when possible; for example, if time is used as an input, the format and reasonableness of the time could be checked. In most cases, a nonce is required during instantiation (see <u>Sections 8.6.1</u> and <u>8.6.7). When required, the nonce is combined with the entropy input to create the initial</u> DRBG seed. 

A personalization string **should** be used during DRBG instantiation; when used, the personalization string is combined with the entropy input bits and possibly a nonce to create the initial DRBG seed. The personalization string **should** be unique for all instantiations of the same DRBG mechanism type (e.g., all instantiations of **HMAC_DRBG** ). See <u>Section 8.7.1 for</u> additional discussion on personalization strings. 

Additional input may also be provided during reseeding and when pseudorandom bits are requested. See Section 8.7.2 for a discussion of this input. 

#### **7.3 The Internal State** 

The internal state is the memory of the DRBG and consists of all of the parameters, variables and other stored values that the DRBG mechanism uses or acts upon. The internal state contains both administrative data (e.g., the security strength) and data that is acted upon and/or modified during the generation of pseudorandom bits (i.e., the working state). 

#### **7.4 The DRBG Mechanism Functions** 

The DRBG mechanism functions handle the DRBG’s internal state. The DRBG mechanisms in this Recommendation have five separate functions: 

1. The instantiate function acquires entropy input and may combine it with a nonce and a personalization string to create a seed from which the initial internal state is created. 

2. The generate function generates pseudorandom bits upon request, using the current internal state and possibly additional input; a new internal state for the next request is also generated. 

3. The reseed function acquires new entropy input and combines it with the current internal state and any additional input that is provided to create a new seed and a new internal state. 

4. The uninstantiate function zeroizes (i.e., erases) the internal state. 

5. The health test function determines that the DRBG mechanism continues to function correctly. 

12 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **8. DRBG Mechanism Concepts and General Requirements** 

#### **8.1 DRBG Mechanism Functions** 

A DRBG mechanism requires instantiate, uninstantiate, generate, and health testing functions. A DRBG mechanism includes an optional reseed function. A DRBG **shall** be instantiated prior to the generation of output by the DRBG. These functions are specified in <u>Section 9.</u> 

#### **8.2 DRBG Instantiations** 

A DRBG may be used to obtain pseudorandom bits for different purposes (e.g., DSA private keys and AES keys) and may be separately instantiated for each purpose, thus effectively creating two DRBGs. 

A DRBG is instantiated using a seed and may be reseeded; when reseeded, the seed **shall** be different than the seed used for instantiation. Each seed defines a _seed period_ for the DRBG instantiation; an instantiation consists of one or more seed periods that begin when a new seed is acquired and end when the next seed is obtained or the DRBG is no longer used (see Figure 2). 

**Figure 2: DRBG Instantiation** 

#### **8.3 Internal States** 

During instantiation, an initial internal state is derived from the seed. The internal state for an instantiation includes: 

1. The working state: 

   - a. One or more values that are derived from the seed and become part of the internal state; these values **shall** remain secret, and 

   - b. A count of the number of requests produced since the instantiation was seeded or reseeded. 

2. Administrative information (e.g., security strength and prediction resistance flag). 

The internal state **shall** be protected at least as well as the intended use of the pseudorandom output bits requested by the consuming application. A DRBG mechanism implementation may be designed to handle multiple instantiations. Each DRBG instantiation **shall** have its own internal state. The internal state for one DRBG instantiation **shall not** be used as the internal state for a different instantiation. 

13 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **8.4 Security Strengths Supported by an Instantiation** 

The DRBG mechanisms specified in this Recommendation support four security strengths: 112, 128, 192 or 256 bits. The security strength for the instantiation is requested during DRBG instantiation, and the instantiate function obtains the appropriate amount of entropy for the requested security strength. Each DRBG mechanism has restrictions on the security strength it can support, based on its design (see <u>Section 10).</u> 

The actual security strength supported by a given instantiation depends on the DRBG implementation and on the amount of entropy provided to the instantiate function. Note that the security strength actually supported by a particular instantiation could be less than the maximum security strength possible for that DRBG implementation (see Table 1). For example, a DRBG that is designed to support a maximum security strength of 256 bits could, instead, be instantiated to support only a 128-bit security strength if the additional security provided by the 256-bit security strength is not required (e.g., by requesting only 128 bits of entropy during instantiation, rather than 256 bits of entropy). 

**Table 1: Possible Instantiated Security Strengths** 

|**Maximum Designed**<br>**Security Strength**|**112**|**128**|**192**|**256**|
|---|---|---|---|---|
|**Possible Instantiated**<br>**Security Strengths**|112|112, 128|112, 128, 192|112, 128, 192,<br>256|

Following instantiation, a request can be made to the generate function for pseudorandom bits (see <u>Section 9.3). The pseudorandom bits returned from a DRBG</u> **shall not** be used for any application that requires a higher security strength than the DRBG is instantiated to support. The security strength provided in these returned bits is the minimum of the security strength supported by the DRBG and the length of the bit string returned, i.e.: 

_Security_strength_of_output_ = **min** ( _output_length_ , _DRBG_security_strength_ ). 

A concatenation of bit strings resulting from multiple calls to a DRBG will not provide a security strength for the concatenated string that is greater than the instantiated security strength of the DRBG. For example, two 128-bit output strings requested from a DRBG that supports a128-bit security strength cannot be concatenated to form a 256-bit string with a security strength of 256 bits. A more complete discussion of this issue is provided in [SP 800-90C]. 

For each generate request, the security strength to be provided for the bits is requested. Any security strength can be requested during a call to the generate function, up to the security strength of the instantiation, e.g., an instantiation could be instantiated at the 128-bit security strength, but a request for pseudorandom bits could indicate that a lesser security strength is actually required for the bits to be generated. Assuming that the request is valid, the requested number of bits is returned. 

When an instantiation is used for multiple purposes, the minimum security strength requirement for each purpose must be considered. The DRBG needs to be instantiated for the highest security strength required. For example, if one purpose requires a security strength of 112 bits, and 

14 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

another purpose requires a security strength of 256 bits, then the DRBG needs to be instantiated to support the 256-bit security strength. 

#### **8.5 DRBG Mechanism Boundaries** 

As a convenience, this Recommendation uses the notion of a “DRBG mechanism boundary” to explain the operations of a DRBG mechanism and its interaction with and relation to other processes; a DRBG mechanism boundary contains all DRBG mechanism functions and internal states required for a DRBG. Data enters a DRBG mechanism boundary via the DRBG’s public interfaces, which are made available to consuming applications. 

**The DRBG mechanism boundary should not be confused with a cryptographic module boundary, as specified in [FIPS 140]; the relationship between a cryptographic module boundary and a DRBG boundary is mentioned below, but is more fully discussed in [SP** **<u>800-90C].</u>** 

Within a DRBG mechanism boundary, 

1. The DRBG internal state and the operation of the DRBG mechanism functions **shall** only be affected according to the DRBG mechanism specification. 

2. The DRBG internal state **shall** exist solely within the DRBG mechanism boundary. The internal state **shall not** be accessible by non-DRBG functions or other instantiations of that DRBG or other DRBGs. 

3. Information about secret parts of the DRBG internal state and intermediate values in computations involving these secret parts **shall not** affect any information that leaves the DRBG mechanism boundary, except as specified for the DRBG pseudorandom bit outputs. 

Each DRBG mechanism includes one or more cryptographic primitives (i.e., a hash function or block cipher algorithm). Other applications may use the same cryptographic primitive, but the DRBG’s internal state and the DRBG mechanism functions **shall not** be affected by these other applications. For example, a DRBG mechanism may use the same hash-function code as a digital-signature application. 

A DRBG mechanism’s functions may be contained within a single device, or may be distributed across multiple devices (see Figures 3 and 4). Figure 3 depicts a DRBG for which all functions are contained within the same device. As further discussed in [SP 800-90C], the DRBG mechanism boundary (in this case) is contained within a cryptographic module boundary. 

15 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Figure 3: DRBG Mechanism Functions within a Single Device** 

Figure 4 provides an example of DRBG mechanism functions that are distributed across multiple devices. In this case, each device has a DRBG mechanism sub-boundary that contains the DRBG mechanism functions implemented on that device, and the DRBG mechanism sub-boundary is contained within a cryptographic module boundary, as is further discussed in [SP 800-90C]. The boundary around the entire DRBG mechanism includes the aggregation of sub-boundaries providing the DRBG mechanism functionality. Each sub-boundary may be contained within a different cryptographic module boundary, or multiple sub-boundaries may be contained within the same cryptographic module boundary. 

The use of distributed DRBG-mechanism functions may be convenient for restricted environments (e.g., smart card applications) in which the primary use of the DRBG does not require repeated use of the instantiate or reseed functions. 

Each DRBG mechanism boundary or sub-boundary **shall** contain a health test function to test the “health” of other DRBG-mechanism functions within that boundary. In addition, a boundary or sub-boundary that contains an instantiate function **shall** contain an uninstantiate function in order to terminate an instantiation. 

16 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Figure 4: Distributed DRBG Mechanism Functions** 

When DRBG mechanism functions are distributed, a physically or cryptographically secure channel **shall** be used to protect the confidentiality and integrity of the internal state or parts of the internal state that are transferred between the distributed DRBG mechanism sub-boundaries. The security provided by the secure channel **shall** be consistent with the security required by the consuming application. See Section 4 for a more complete definition of a secure channel. 

For distributed DRBGs, each sub-boundary is the same as or is fully contained within a cryptographic module boundary. 

#### **8.6 Seeds** 

When a DRBG is used to generate pseudorandom bits, a seed **shall** be acquired prior to the generation of output bits by the DRBG. The seed is used to instantiate the DRBG and determine the initial internal state that is used when calling the DRBG to obtain the first output bits. 

Reseeding is a means of restoring the secrecy of the output of the DRBG if a seed or the internal state becomes known. Periodic reseeding is a good way of addressing the threat of either the DRBG seed, entropy input or working state being compromised over time. In some implementations (e.g., smartcards), an adequate reseeding process may not be possible. In these cases, the best policy might be to replace the DRBG, obtaining a new seed in the process (e.g., obtain a new smart card). 

The seed and its use by a DRBG mechanism **shall** be generated and handled as specified in the following subsections. 

17 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **8.6.1 Seed Construction for Instantiation** 

Figure 5 depicts the seed-construction process for instantiation. The seed material used to determine a seed for instantiation consists of entropy input from a randomness source, a nonce and an optional (but recommended) personalization string. Entropy input **shall** always be used in the construction of a seed; requirements for the entropy input are discussed in Section 8.6.3. Except for the case noted below, a nonce **shall** be used; requirements for the nonce are discussed in <u>Section 8.6.7. A</u> personalization string **should** also be used; requirements for the personalization string are discussed in <u>Section 8.7.1.</u> 

**Figure 5: Seed Construction for Instantiation** 

Depending on the DRBG mechanism and the randomness source, a derivation function may be required to derive a seed from the seed material. However, in certain circumstances, the **CTR_DRBG** mechanism based on block cipher algorithms (see <u>Section 10.2) may be</u> implemented without a derivation function. When implemented in this manner, a (separate) nonce (as shown in Figure 5) is not used. Note, however, that the personalization string could contain a nonce, if desired. 

#### **8.6.2 Seed Construction for Reseeding** 

Figure 6 depicts the seed construction process for reseeding an instantiation. The seed material for reseeding consists of a value that is carried in the internal state<sup>3</sup> , new entropy input and, optionally, additional input. The internal state value and the entropy input are required; requirements for the entropy input are 

discussed in Section 8.6.3. Requirements for the additional input are discussed in <u>Section 8.7.2. As in Section 8.6.1, a derivation function may be required for reseeding.</u> 

**Figure 6: Seed Construction for Reseeding** 

#### **8.6.3 Entropy Requirements for the Entropy Input** 

The entropy input **shall** have entropy that is equal to or greater than the security strength of the instantiation. Additional entropy may be provided in the nonce or the optional personalization string during instantiation, or in the additional input during reseeding and generation, but this is not required and does not increase the “official” security strength of the DRBG instantiation that is recorded in the internal state. The use of more entropy than the minimum value will offer a 

> 3 See each DRBG mechanism specification for the value that is used. 

18 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

security “cushion”. This may be useful if the assessment of the entropy provided in the entropy input is incorrect. Having more entropy than the assessed amount is acceptable; having less entropy than the assessed amount could be fatal to security. The presence of more entropy than is required, especially during the instantiation, will provide a higher level of assurance than the minimum required entropy. 

#### **8.6.4 Seed Length** 

The minimum length of the seed depends on the DRBG mechanism and the security strength required by the consuming application, but **shall** be at least the number of bits of entropy required. See the tables in <u>Section 10.</u> 

#### **8.6.5 Randomness Source** 

A DRBG mechanism requires an **approved** randomness source during instantiation and reseeding, including whenever prediction resistance is requested (see Section 8.8). This input is requested using the **Get_entropy_input** function introduced in Section 9 and is specified in more detail in [SP 800-90C]. 

An **approved** randomness source is an entropy source that conforms to [SP 800-90B], or an RBG that conforms to [SP 800-90C] − either a DRBG or an NRBG. 

#### **8.6.6 Entropy Input and Seed Privacy** 

The entropy input and the resulting seed **shall** be handled in a manner that is consistent with the security required for the data protected by the consuming application. For example, if the DRBG is used to generate keys, then the entropy inputs and seeds used to generate the keys **shall** (at a minimum) be protected at the same security strength as the keys. 

The security of the DRBG depends on the secrecy of the entropy input.  For this reason, the entropy input **shall** be treated as a critical security parameter (CSP) during cryptographic module validation. The entropy input for the DRBG function requiring the entropy input **shall** be obtained either from within the cryptographic module containing that function or from another cryptographic module and transported to the DRBG function's cryptographic module via a secure channel. 

#### **8.6.7 Nonce** 

A nonce may be required in the construction of a seed during instantiation in order to provide a security cushion to block certain attacks. The nonce **shall** be either: 

- a. A value with at least ( _security_strength_ /2) bits of entropy, or 

- b. A value that is expected to repeat no more often than a ( _security_strength_ /2)-bit random string would be expected to repeat. 

Each nonce **shall** be unique to the cryptographic module in which instantiation is performed, but need not be secret. When used, the nonce **shall** be considered to be a critical security parameter. 

A nonce may be composed of one (or more) of the following components (other components may also be appropriate): 

19 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

1. A random value that is generated anew for each nonce, using an **approved** random bit generator. 

2. A timestamp of sufficient resolution (detail) so that it is different each time it is used. 

3. A monotonically increasing sequence number, or 

4. A combination of a timestamp and a monotonically increasing sequence number, such that the sequence number is reset when and only when the timestamp changes. For example, a timestamp may show the date but not the time of day, so a sequence number is appended that will not repeat during a particular day. 

For case 1 above, the random value could be acquired from the same source and at the same time as the entropy input. In this case, the seed could be considered to be constructed from an “extra strong” entropy input and the optional personalization string, where the entropy for the entropy input is equal to or greater than (3/2 _security_strength_ ) bits. 

For case 2 above, the timestamp must be trusted. A trusted timestamp is generated and signed by an entity that is trusted to provide accurate time information. 

The nonce provides greater assurance that the DRBG provides _security_strength_ bits of security to the consuming application. If a DRBG were instantiated many times without a nonce, a compromise could become more likely. In some consuming applications, a single DRBG compromise could reveal long-term secrets (e.g., a compromise of the DSA per-message secret could reveal the signing key). 

A nonce **shall** be generated within a cryptographic module boundary. This requirement does not preclude the generation of the nonce within a cryptographic module that is different from the cryptographic boundary containing the DRBG function with which the nonce is used (e.g., the cryptographic module boundary containing an instantiate function). However, in this scenario, there needs to be a secure channel to transport the nonce between the cryptographic-module boundaries. See the discussion of distributed DRBGs in Section 8.5 and distributed RBGs in [SP <u>800-90C].</u> 

#### **8.6.8 Reseeding** 

Generating too many outputs from a seed (and other input information) may provide sufficient information for successfully predicting future outputs (see Section 8.8). Periodic reseeding will reduce security risks, reducing the likelihood of a compromise of the data that is protected by cryptographic mechanisms that use the DRBG. 

Seeds have a finite seedlife (i.e., the number of outputs that are produced during a seed period); the maximum seedlife is dependent on the DRBG mechanism used. Implementations **shall** enforce the limits on seedlife specified for the DRBG mechanism used or more stringent limits selected by the implementer.  When a DRBG's maximum seedlife is reached, the DRBG **shall not** generate outputs until it has been reseeded. 

Reseeding is accomplished 1) by an explicit reseeding of the DRBG by the consuming application, 2) by the generate function when prediction resistance is requested (see <u>Section 8.8)</u> or 3) when the end of the seed life is determined during the generate function (see Section 9.3.1). 

The reseeding of the DRBG **shall** be performed in accordance with the specification for a given DRBG mechanism. The DRBG reseed specifications within this Recommendation are designed 

20 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

to produce a new seed that is determined by both the old seed and newly obtained entropy input that will support the desired security strength. 

An alternative to reseeding would be to create an entirely new instantiation. However, reseeding is preferred over creating a new instantiation. If a DRBG instantiation was initially seeded with sufficient entropy, and the randomness source subsequently fails without being detected, then a new instantiation using the same (failed) source would not have sufficient entropy to operate securely. However, if there is an undetected failure in the randomness source of an already properly seeded DRBG instantiation, the DRBG instantiation will still retain any previous entropy when the reseed operation fails to introduce new entropy. 

#### **8.6.9 Seed Use** 

The seed that is used to initialize one instantiation of a DRBG **shall not** be intentionally used to reseed the same instantiation or used as the seed for another DRBG instantiation. In addition, a DRBG instantiation **shall not** reseed itself. Note that a DRBG does not provide output until a seed is available, and the internal state has been initialized (see Section 10). 

#### **8.6.10 Entropy Input and Seed Separation** 

The seed used by a DRBG and the entropy input used to create that seed **shall not** intentionally be used for other purposes (e.g., domain parameter or prime number generation). 

#### **8.7 Other Input to the DRBG Mechanism** 

Other input may be provided during DRBG instantiation, generation and reseeding. This input may contain entropy, but this is not required. During instantiation, a personalization string may be provided and combined with entropy input and a nonce to derive a seed (see Section 8.6.1). When pseudorandom bits are requested and when reseeding is performed, additional input may be provided (see <u>Section 8.7.2).</u> 

Depending on the method for acquiring the input, the exact value of the input may or may not be known to the user or consuming application. For example, the input could be derived directly from values entered by the user or consuming application, or the input could be derived from information introduced by the user or consuming application (e.g., from timing statistics based on key strokes), or the input could be the output of another RBG. 

#### **8.7.1 Personalization String** 

A personalization string is an optional (but recommended) input to the instantiate function and is used to derive the seed (see <u>Section 8.6.1).  The personalization string may be obtained from</u> inside or outside a cryptographic module, and may be an empty string.  Note that a DRBG does not rely on a personalization string to provide entropy, even though entropy could be provided in the personalization string, and knowledge of the personalization string by an adversary does not degrade the security strength of a DRBG instantiation, as long as the entropy input is unknown. When used within a cryptographic module, a personalization string is not considered to be a critical security parameter. 

21 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

The personalization string may contain secret information, but **shall not** include secret information that requires protection at a higher security strength than the DRBG being instantiated will support.  For example, a personalization string to be used to instantiate a DRBG at 112 bits of security strength **shall not** include information requiring 128 bits of protection. A given implementation of a DRBG may support the use of a personalization string, but is not required to do so. 

The intent of a personalization string is to introduce additional input into the instantiation of a DRBG. This personalization string might contain values unknown to an attacker, or values that tend to differentiate this DRBG instantiation from all others. Ideally, a personalization string will be set to some bitstring that is as unique as possible. Good sources for the personalization string contents include: 

- Application identifiers, 

- Device serial numbers, 

- User identification, 

- Per-module or per-device values, 

- Timestamps, 

- Network addresses, 

- Special key values for this specific DRBG instantiation, 

- Protocol version identifiers, 

- Random numbers, 

- Nonces, and 

- Outputs from other approved or nonapproved random bit generators. 

#### **8.7.2 Additional Input** 

Additional input may optionally be provided to the reseed and generate functions during requests.  The additional input may be obtained from inside or outside a cryptographic module, and may include secret or public information. Note that a DRBG does not rely on additional input to provide entropy, even though entropy could be provided in the additional input, and knowledge of the additional input by an adversary does not degrade the security strength of a DRBG. However, if the additional input contains secret/private information (e.g., a social security number), that information **shall not** require protection at a higher security strength than the security strength supported by the DRBG. A given implementation of a DRBG may include the additional input, but is not required to do so.  When used within a cryptographic module, the additional input used in DRBG requests is not considered to be a critical security parameter unless any secret information included in the additional input qualifies as a critical security parameter. 

Additional input is optional for both the DRBG and the consuming application, and the ability to enter additional input may or may not be included in an implementation. The value of the additional input may be either secret or publicly known; its value is arbitrary, although its length may be restricted, depending on the implementation and the DRBG mechanism. The use of additional input may be a means of providing more entropy for the DRBG internal state that will increase assurance that the entropy requirements are met. If the additional input is kept secret and has sufficient entropy, the input can provide more assurance when recovering from the compromise of the entropy input, the seed or one or more DRBG internal states. 

22 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **8.8 Prediction Resistance and Backtracking Resistance** 

Figure 7 depicts the sequence of DRBG internal states that result from a given seed. Some subset of bits from each internal state are used to generate pseudorandom bits upon request by a user. The following discussions will use the figure to explain backtracking and prediction resistance. 

Suppose that a compromise occurs at _Statex_ , where _Statex_ contains both secret and non-secret information. 

###### **Figure 7: Sequence of DRBG States** 

<u>Backtracking Resistance: Backtracking resistance is provided relative to time</u> _T_ if there is assurance that an adversary who has knowledge of the internal state of the DRBG at some time subsequent to time _T_ would be unable to distinguish between observations of ideal random bitstrings and (previously unseen) bitstrings that were output by the DRBG prior to time _T_ . This assumes that the adversary is incapable of performing the work required to negate the claimed security strength of the DRBG. Backtracking resistance means that a compromise of the DRBG internal state has no effect on the security of prior outputs. That is, an adversary who is given access to all of the prior output sequence cannot distinguish it from random output with less work than is associated with the security strength of the instantiation; if the adversary knows only part of the prior output, he cannot determine any bit of that prior output sequence that he has not already seen with better than a 50-50 chance. 

For example, suppose that an adversary knows _Statex_ . Backtracking resistance means that: 

- a. The output bits from _State_ 1 to _Statex_ -1 cannot be distinguished from random output, and 

- b. The prior internal state values themselves ( _State_ 1 to _Statex_ -1) cannot be recovered, given knowledge of the secret information in _Statex_ . 

Backtracking resistance can be provided by ensuring that the DRBG generation algorithm is a one-way function. All DRBG mechanisms in this Recommendation have been designed to provide backtracking resistance. 

<u>Prediction Resistance: Prediction resistance means that a compromise of the DRBG internal</u> state has no effect on the security of future DRBG outputs.  That is, an adversary who is given access to all of the output sequence after the compromise cannot distinguish it from random output with less work than is associated with the security strength of the instantiation; if the adversary knows only part of the future output sequence, he cannot predict any bit of that future output sequence that he does not already know (with better than a 50-50 chance). 

- For example, suppose that an adversary knows _Statex_ . Prediction resistance means that: 

   - a. The output bits from _Statex_ +1 and forward cannot be distinguished from an ideal random bitstring by the adversary, and 

23 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

- b. The future internal state values themselves ( _Statex+_ 1 and forward) cannot be predicted (with better than a 50-50 chance), given knowledge of _Statex_ . 

Prediction resistance is provided relative to time _T_ if there is assurance that an adversary with knowledge of the state of the RBG at some time(s) prior to _T_ (but incapable of performing work that matches the claimed _security strength_ of the RBG) would be unable to distinguish between observations of _ideal random bitstrings_ and (previously unseen) bitstrings output by the RBG at or subsequent to time _T_ . In particular, an RBG whose design allows the adversary to step forward from the initially compromised RBG state(s) to obtain knowledge of subsequent RBG states and the corresponding outputs (including the RBG state and output at time _T_ ) would not provide prediction resistance relative to time _T_ . 

Prediction resistance can be provided only by ensuring that a DRBG is effectively reseeded with fresh entropy between producing output for consecutive DRBG requests. That is, an amount of entropy that is sufficient to support the security strength of the DRBG being reseeded (i.e., an amount that is at least equal to the security strength) must be provided to the DRBG in a way that ensures that knowledge of the current DRBG internal state does not allow an adversary any useful knowledge about future DRBG internal states or outputs. Prediction resistance can be provided when the randomness source is or has direct or indirect access to an entropy source or an NRBG (see Section 8.6.5). 

For example, suppose that an adversary knows internal _Statex_ -2 (see Figure 7). If the adversary also knows the DRBG mechanism used, he then has enough information to compute _Statex_ -1 and _Statex_ . If prediction is then requested for the next bits that are to be output from the DRBG, new entropy bits will be inserted into the DRBG instantiation before _Statex_ +1 is produced that will create a separation between _Statex_ and _Statex_ +1, i.e., the adversary will not be able to compute _Statex_ +1, simply by knowing _Statex_ ; the work required will be greatly increased by the entropy inserted during the prediction request. 

The introduction of fresh entropy via reseeding will also make the DRBG less susceptible to cryptanalytic attack. **Whenever an entropy source is available, it is strongly recommended that DRBGs be requested to provide prediction resistance as often as is practical.** 

24 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **9 DRBG Mechanism Functions** 

All DRBG mechanisms and algorithms are described in this document in pseudocode, which is intended to explain functionality. The pseudocode is not intended to constrain real-world implementations. 

Except for the health test function, which is discussed in <u>Section 11.3, the functions of the</u> DRBG mechanisms in this Recommendation are specified as an algorithm and an “envelope” of pseudocode around that algorithm. The pseudocode in each envelope (provided in this section) checks the input parameters, obtains input not provided via the input parameters, accesses the appropriate DRBG algorithm and manages the internal state. A function need not be implemented using such envelopes, but the function **shall** have equivalent functionality. 

During instantiation and reseeding (see <u>Sections 9.1 and 9.2), entropy input and (usually) a</u> nonce are acquired for constructing a seed as discussed in <u>Sections 8.6.1 and 8.6.2. In the</u> specifications of this Recommendation, a **Get_entropy_input** function is used for this purpose. The entropy input and nonce **shall** be provided as discussed in <u>Sections 8.6.5 and 8.6.7</u> and in [SP 800-90C]. 

The **Get_entropy_input** function is specified in pseudocode in [SP 800-90C] for various RBG constructions; however, in general, the function has the following meaning: 

**Get_entropy_input** : A function that is used to obtain entropy input. The function call is: 

( _status_ , _entropy_input_ ) = **Get_entropy_input** ( _min_entropy_ , _min_ length_ , _max_ length_ , _prediction_resistance_request_ ), 

which requests a string of bits ( _entropy_input_ ) with at least _min_entropy_ bits of entropy. The length for the string **shall** be equal to or greater than _min_length_ bits, and less than or equal to _max_length_ bits. The _prediction_resistance_request_ parameter indicates whether or not prediction resistance is to be provided during the request (i.e., whether fresh entropy is required<sup>4</sup> ). A _status_ code is returned from the function. 

Note that an implementation may choose to define this functionality differently by omitting some of the parameters; for example, for many of the DRBG mechanisms, _min_length = min_entropy_ for the **Get_entropy_input** function, in which case, the second parameter could be omitted. 

In the pseudocode in this section, two classes of error codes are returned: ERROR_FLAG and **CATASTROPHIC_ERROR_FLAG** . The handling of these classes of error codes is discussed in Section 11.4. The error codes may, in fact, provide information about the reason for the error; for example, when ERROR_FLAG is returned because of an incorrect input parameter, the ERROR_FLAG may indicate the problem. 

Consuming applications **should** check the _status_ returned from DRBG functions to determine whether or not the request was successful or if remediary action is required. For example, when 

> 4 Entropy input may be obtained from an entropy source or an NRBG, both of which provide fresh entropy. Entropy input could also be obtained from a DRBG that has access to an entropy source or NRBG. 

> The request for prediction resistance rules out the use of a DRBG that does not have access to either an entropy source or NRBG. 

25 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

the instantiate function returns an error, an instantiation will not have been created, and an invalid _state_handle_ will be returned (see Section 9.1); however, the lack of a _state_handle_ will be detected in a subsequent reseed or generate request. When the reseed function returns an error (see <u>Section 9.2), the indicated instantiation will not have been reseeded (i.e., the internal state</u> will not have been injected with fresh entropy). When the generate function returns an error, a null string is returned as the output string (see Section 9.3.1) and **shall not** be used as pseudorandom output. 

Comments are often included in the pseudocode in this Recommendation. A comment placed on a line that includes pseudocode applies to that line; a comment placed on a line containing no pseudocode applies to one or more lines of pseudocode immediately below that comment. 

#### **9.1 Instantiating a DRBG** 

A DRBG **shall** be instantiated prior to the generation of pseudorandom bits. The instantiate function: 

1. Checks the validity of the input parameters, 

2. Determines the security strength for the DRBG instantiation, 

3. Obtains entropy input with entropy sufficient to support the security strength, 

4. Obtains the nonce (if required), 

5. Determines the initial internal state using the instantiate algorithm, and 

6. If an implementation supports multiple simultaneous instantiations of the same DRBG, a _state_handle_ for the internal state is returned to the consuming application (see below). 

Let _working_state_ be the working state for the particular DRBG mechanism (e.g., **HMAC_DRBG** ), and let _min_length_ , _max_ length_ , and _highest_supported_security_strength_ be defined for each DRBG mechanism (see <u>Section 10). Let</u> **Instantiate_algorithm** be a call to the appropriate instantiate algorithm for the DRBG mechanism (see Section 10). 

The following or an equivalent process **shall** be used to instantiate a DRBG. 

**Instantiate_function (** _requested_instantiation_security_strength, prediction_resistance_flag, personalization_string_ ): 

1. _requested_instantiation_security_strength_ : A requested security strength for the instantiation. Implementations that support only one security strength do not require this parameter; however, any consuming application using that implementation must be aware of the security strength that is supported. 

2. _prediction_resistance_flag_ : Indicates whether or not prediction resistance may be required by the consuming application during one or more requests for pseudorandom bits. Implementations that always provide or do not support prediction resistance may not need to support this parameter if the intent is implicitly known. However, the user of a consuming application must determine whether or not prediction resistance may be required by the consuming application before electing to use such an implementation. If the _prediction_resistance_flag_ is not needed (i.e., it is known that prediction resistance is always performed or is not supported), then the _prediction_resistance_flag_ input 

26 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

parameter and instantiate process step 2 are omitted, and the _prediction_resistance_flag_ is omitted from the internal state in step 11 of the instantiate process. In addition, step 6 can be modified to not perform a check for the _prediction_resistance_flag_ when the flag is not used in an implementation; in this case, the **Get_entropy_input** call need not include the _prediction_resistance_request_ parameter. 

3. _personalization_string_ : An optional input that provides personalization information (see <u>Sections 8.6.1</u> and <u>8.7.1). The maximum length of the personalization string</u> ( _max_personalization_string_length_ ) is implementation dependent, but **shall** be less than or equal to the maximum length specified for the given DRBG mechanism (see Section <u>10). If the input of a personalization string is not supported, then the</u> _personalization_string_ input parameter and step 3 of the instantiate process are omitted, and instantiate process step 9 is modified to omit the personalization string. 

#### **Required information not provided by the consuming application during instantiation** 

(This information **shall not** be provided by the consuming application as an input parameter during the instantiate request): 

1. _entropy_input_ : Input bits containing entropy. The maximum length of the _entropy_input_ is implementation dependent, but **shall** be less than or equal to the specified maximum length for the selected DRBG mechanism (see Section 10). 

2. _nonce_ : A nonce as specified in Section 8.6.7. Note that if a random value is used in the nonce, the _entropy_input_ and random portion of the _nonce_ could be acquired using a single **Get_entropy_input** call (see step 6 of the instantiate process); in this case, the first parameter of the **Get_entropy_input** call is adjusted to include the entropy for the _nonce_ (i.e., the _security_strength_ is increased by at least ½ _security_strength_ , and _minlength_ is increased to accommodate the length of the nonce), instantiate process step 8 is omitted, and the _nonce_ is omitted from the parameter list in instantiate process step 9. 

Note that in some cases, a nonce will not be used by a DRBG mechanism; in this case, step 8 is omitted, and the _nonce_ is omitted from the parameter list in instantiate process step 9. 

#### **Output to a consuming application after instantiation:** 

1. _status_ : The status returned from the instantiate function. If any status other than SUCCESS is returned, either no _state_handle_ or an invalid _state_handle_ **shall** be returned to the consuming application. A consuming application **should** check the _status_ to determine that the DRBG has been correctly instantiated. 

2. _state_handle_ : Used to identify the internal state for this instantiation in subsequent calls to the generate, reseed, uninstantiate and health test functions. 

If a state handle is not required for an implementation because the implementation does not support multiple simultaneous instantiations, a _state_handle_ need not be returned. In this case, instantiate process step 10 is omitted, process step 11 is revised to save the only internal state, and process step 12 is altered to omit the _state_handle_ . 

#### **Information retained within the DRBG mechanism boundary after instantiation** : 

27 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

The internal state for the DRBG, including the _working_state_ and administrative information (see <u>Sections 8.3 and 10</u> for definitions of the _working_state_ and administrative information). 

**Instantiate Process:** 

Comment: Check the validity of the input parameters. 

1. If _requested_instantiation_security_strength_ > _highest_supported_security_strength_ , then return (ERROR_FLAG **,** Invalid). 

2. If _prediction_resistance_flag_ is set, and prediction resistance is not supported, then return (ERROR_FLAG, Invalid **)** . 

3. If the length of the _personalization_string_ > _max_personalization_string_length_ , return (ERROR_FLAG, Invalid **)** . 

4. Set _security_strength_ to the lowest security strength greater than or equal to _requested_instantiation_security_strength_ from the set {112, 128, 192, 256}. 

5. Null step. Comment: This null step replaces a step from the original version of SP 800-90 without changing the step numbers. 

Comment: Obtain the entropy input. 

6. ( _status_ , _entropy_input_ ) = **Get_entropy_input** ( _security_strength_ , _min_length_ , _max_length_ , _prediction_resistance_request_ ). 

Comment: _status_ indications other than SUCCESS could be ERROR_FLAG or **CATASTROPHIC_ERROR_FLAG** , in which case, the status is returned to the consuming application to handle. The **Get_entropy_input** call could return a _status_ of ERROR_FLAG to indicate that entropy is currently unavailable, and could return **CATASTROPHIC_ERROR_FLAG** to indicate that an entropy source failed. 

7. If ( _status_ ≠ SUCCESS), return ( _status,_ Invalid). 

8. Obtain a _nonce._ Comment: This step **shall** include any appropriate checks on the acceptability of the _nonce_ . See <u>Section 8.6.7.</u> Comment: Call the appropriate instantiate algorithm in Section 10 to obtain values for the initial _working_state._ 

9. _initial_working_state_ = **Instantiate_algorithm** ( _entropy_input_ , _nonce_ , _personalization_string, security_strength_ ). 

10. Get a _state_handle_ for a currently empty internal state. If an empty internal state cannot be found, return (ERROR_FLAG, Invalid **)** . 

28 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

11. Set the internal state for the new instantiation (e.g., as indicated by _state_handle_ ) to the initial values for the internal state (i.e., set the _working_state_ to the values returned as _initial_working_state_ in step 9) and any other values required for the _working_state_ (see <u>Section 10), and set the administrative information to the appropriate values (e.g., the</u> values of _security_strength_ and the _prediction_resistance_flag_ ). 

12. Return (SUCCESS, _state_handle_ ). 

#### **9.2 Reseeding a DRBG Instantiation** 

The reseeding of an instantiation is not required, but is recommended whenever a consuming application and implementation are able to perform this process. Reseeding will insert additional entropy into the generation of pseudorandom bits. Reseeding may be: 

- Explicitly requested by a consuming application, 

- Performed when prediction resistance is requested by a consuming application, 

- Triggered by the generate function when a predetermined number of pseudorandom outputs have been produced or a predetermined number of generate requests have been made (i.e., at the end of the seedlife), or 

- Triggered by external events (e.g., whenever entropy is available). 

The reseed function: 

1. Checks the validity of the input parameters, 

2. Obtains entropy input from a randomness source that supports the security strength of the DRBG, and 

3. Using the reseed algorithm, combines the current working state with the new entropy input and any additional input to determine the new working state. 

Let _working_state_ be the working state for the particular DRBG instantiation (e.g., **HMAC_DRBG** ) , let _min_length_ and _max_ length_ be defined for each DRBG mechanism, and let **Reseed_algorithm** be a call to the appropriate reseed algorithm for the DRBG mechanism (see <u>Section 10).</u> 

The following or an equivalent process **shall** be used to reseed the DRBG instantiation. 

#### **Reseed_function (** _state_handle, prediction_resistance_request, additional_input_ ): 

- 1) _state_handle_ : A pointer or index that indicates the internal state to be reseeded. If a state handle is not used by an implementation because the implementation does not support multiple simultaneous instantiations, a _state_handle_ is not provided as input. Since there is only a single internal state in this case, reseed process step 1 obtains the contents of the internal state, and reseed process step 6 replaces the _working_state_ of this internal state. 

29 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

- 2) _prediction_resistance_request_ : Indicates whether or not prediction resistance is to be provided during the request (i.e., whether or not fresh entropy bits are required)<sup>5</sup> . Without the explicit prediction resistance request, the entropy input could be provided from either a DRBG with no access to an entropy source (i.e., fresh entropy would not be provided), or the entropy input could be provided by an entropy source or by an RBG with access to an entropy source (i.e., fresh entropy would be provided in these cases). 

DRBGs that are implemented to always support prediction resistance or to never support prediction resistance do not require this parameter. However, when prediction resistance is not supported, the user of a consuming application must determine whether or not prediction resistance may be required by the application before electing to use such a DRBG implementation. 

If prediction resistance is not supported, then the _prediction_resistance_request_ input parameter and step 2 of the reseed process is omitted, and reseed process step 4 is modified to omit the _prediction_resistance_request_ parameter _._ 

If prediction resistance is always performed, then the _prediction_resistance_request_ input parameter and reseed process step 2 may be omitted, and reseed process step 4 is replaced by: 

   - ( _status_ , _entropy_input_ ) = **Get_entropy_input** ( _security_strength_ , _min_length_ , _max_length_ ) 

- 3) _additional_input_ : An optional input. The maximum length of the _additional_input_ ( _max_additional_input_length_ ) is implementation dependent, but **shall** be less than or equal to the maximum value specified for the given DRBG mechanism (see Section 10). If the input by a consuming application of _additional_input_ is not supported, then the input parameter and step 2 of the reseed process are omitted, and step 5 of the reseed process is modified to remove the _additional_input_ from the parameter list. 

**Required information not provided by the consuming application during reseeding** (This information **shall not** be provided by the consuming application as an input parameter during the reseed request): 

1. _entropy_input_ : Input bits containing entropy. This input **shall not** be provided by the DRBG instantiation being reseeded. The maximum length of the _entropy_input_ is implementation dependent, but **shall** be less than or equal to the specified maximum length for the selected DRBG mechanism (see Section 10). 

2. Internal state values required by the DRBG for the _working_state_ and administrative information, as appropriate. 

#### **Output to a consuming application after reseeding:** 

1. _status_ : The status returned from the function. 

> 5 A DRBG may be reseeded by an entropy source or an NRBG, both of which provide fresh entropy. A DRBG could also be reseeded by a DRBG that has access to an entropy source or NRBG. The request for prediction resistance during reseeding rules out the use of a DRBG that does not have access to either an entropy source or NRBG. See [SP 800-90C] for further discussion. 

30 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **Information retained within the DRBG mechanism boundary after reseeding:** 

Replaced internal state values (i.e., the _working_state_ ) _._ 

**Reseed Process:** 

Comment: Get the current internal state and check the input parameters. 

1. Using _state_handle_ , obtain the current internal state. If _state_handle_ indicates an invalid or unused internal state, return (ERROR_FLAG **)** . 

2. If _prediction_resistance_request_ is set, and _prediction_resistance_flag_ is not set, then return (ERROR_FLAG **)** . 

3. If the length of the _additional_input_ > _max_additional_input_length_ , return (ERROR_FLAG **)** . 

Comment: Obtain the entropy input. 

4. ( _status_ , _entropy_input_ ) = **Get_entropy_input** ( _security_strength_ , _min_length_ , _max_length, prediction_resistance_request_ ). 

Comment: _status_ indications other than SUCCESS could be ERROR_FLAG or **CATASTROPHIC_ERROR_FLAG** , in which case, the status is returned to the consuming application to handle. The **Get_entropy_input** call could return a _status_ of  ERROR_FLAG to indicate that entropy is currently unavailable, and could return **CATASTROPHIC_ERROR_FLAG** to indicate that an entropy source failed. 

5. If ( _status_ ≠ SUCCESS), return ( _status_ ). 

   - Comment: Get the new _working_state_ using the appropriate reseed algorithm in Section 10. 

6. _new_working_state_ = **Reseed_algorithm** ( _working_state_ , _entropy_input_ , _additional_input_ ). 

- 7 Replace the _working_state_ in the internal state for the DRBG instantiation (e.g., as indicated by _state_handle_ ) with the values of _new_working_state_ obtained in step 6. 

8. Return (SUCCESS **)** . 

#### **9.3 Generating Pseudorandom Bits Using a DRBG** 

This function is used to generate pseudorandom bits after instantiation or reseeding. The generate function: 

1. Checks the validity of the input parameters. 

2. Calls the reseed function to obtain sufficient entropy if the instantiation needs additional entropy because the end of the seedlife has been reached or prediction resistance is 

31 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

required; see Sections 9.3.2 and <u>9.3.3 for more information on reseeding at the end of the</u> seedlife and on handling prediction resistance requests. 

3. Generates the requested pseudorandom bits using the generate algorithm. 

4. Updates the working state. 

5. Returns the requested pseudorandom bits to the consuming application. 

#### **9.3.1 The Generate Function** 

Let _outlen_ be the length of the output block of the cryptographic primitive (see <u>Section 10). Let</u> **Generate_algorithm** be a call to the appropriate generate algorithm for the DRBG mechanism (see <u>Section 10), and let</u> **Reseed_function** be a call to the reseed function in <u>Section 9.2.</u> 

The following or an equivalent process **shall** be used to generate pseudorandom bits. 

**Generate_function (** _state_handle, requested_number_of_bits, requested_security_strength_ **,** _prediction_resistance_request, additional_input_ ): 

1. _state_handle_ : A pointer or index that indicates the internal state to be used. If a state handle is not used by an implementation because the implementation does not support multiple simultaneous instantiations, a _state_handle_ is not provided as input. The _state_handle_ is then omitted from the input parameter list in process step 7.1, generate process steps 1 and 7.3 are used to obtain the contents of the internal state, and process step 10 replaces the _working_state_ of this internal state. 

2. _requested_number_of_bits_ : The number of pseudorandom bits to be returned from the generate function. The _max_number_of_bits_per_request_ is implementation dependent, but **shall** be less than or equal to the value provided in <u>Section 10 for a specific DRBG</u> mechanism. 

3. _requested_security_strength_ : The security strength to be associated with the requested pseudorandom bits. DRBG implementations that support only one security strength do not require this parameter; however, any consuming application using that DRBG implementation must be aware of the supported security strength. 

4. _prediction_resistance_request_ : Indicates whether or not prediction resistance is to be provided during the request. DRBGs that are implemented to always provide prediction resistance or that do not support prediction resistance do not require this parameter. However, when prediction resistance is not supported, the user of a consuming application must determine whether or not prediction resistance may be required by the application before electing to use such a DRBG implementation. 

If prediction resistance is not supported, then the _prediction_resistance_request_ input parameter and steps 5 and 9.2 of the generate process are omitted, and generate process steps 7 and 7.1 are modified to omit the check for the _prediction_resistance_request_ term. 

If prediction resistance is always performed, then the _prediction_resistance_request_ input parameter and generate process steps 5 and 9.2 may be omitted, and generate process steps 7 and 8 may be replaced by: 

_status_ = **Reseed_function** ( _state_handle_ , _additional_input_ ). 

32 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

Comment: _status_ indications other than SUCCESS could be ERROR_FLAG or **CATASTROPHIC_ERROR_FLAG** , in which case, the status is returned to the consuming application to handle. The **Get_entropy_input** call could return a _status_ of  ERROR_FLAG to indicate that entropy is currently unavailable, and could return **CATASTROPHIC_ERROR_FLAG** to indicate that an entropy source failed. 

If ( _status_ ≠ SUCCESS), return ( _status_ , _Null_ ). 

Using _state_handle_ , obtain the new internal state. 

( _status_ , _pseudorandom_bits, new_working_state_ ) = **Generate_algorithm** ( _working_state_ , _requested_number_of_bits_ ). 

Note that if the input of _additional_input_ is not supported, then the _additional_input_ parameter in the **Reseed_function** call above may be omitted. 

5. _additional_input_ : An optional input. The maximum length of the _additional_input_ ( _max_additional_input_length_ ) is implementation dependent, but **shall** be less than or equal to the specified maximum length for the selected DRBG mechanism (see Section <u>10). If the input of</u> _additional_input_ is not supported, then the input parameter, generate process steps 4 and 7.4, and the _additional_input_ input parameter in generate process steps 7.1 and 8 are omitted. 

#### **Required information not provided by the consuming application during generation:** 

1. Internal state values required for the _working_state_ and administrative information, as appropriate. 

#### **Output to a consuming application after generation:** 

1. _status_ : The status returned from the generate function. If any status other than SUCCESS is returned, a _Null_ string **shall** be returned as the pseudorandom bits. 

2. _pseudorandom_bits_ : The pseudorandom bits that were requested or a _Null_ string. 

#### **Information retained within the DRBG mechanism boundary after generation:** 

Replaced internal state values (i.e., the new _working_state_ ). 

#### **Generate Process:** 

Comment: Get the internal state and check the input parameters. 

1. Using _state_handle_ , obtain the current internal state for the instantiation. If _state_handle_ indicates an invalid or unused internal state, then return (ERROR_FLAG, _Null_ **)** . 

2. If _requested_number_of_bits_ > _max_number_of_bits_per_request_ , then return (ERROR_FLAG, _Null_ **)** . 

3. If _requested_security_strength_ > the _security_strength_ indicated in the internal state, then return (ERROR_FLAG, _Null_ **)** . 

33 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

4. If the length of the _additional_input_ > _max_additional_input_length_ , then return (ERROR_FLAG, _Null_ **)** . 

5. If _prediction_resistance_request_ is set, and _prediction_resistance_flag_ is not set, then return (ERROR_FLAG, _Null_ **)** . 

6. Clear the _reseed_required_flag._ Comment: See Section 9.3.2 for a discussion. 

Comment: Reseed if necessary (see Section 9.2). 

7. If _reseed_required_flag_ is set _,_ or if _prediction_resistance_request_ is set, then 

   - 7.1 _status_ = **Reseed_function** ( _state_handle_ , _prediction_resistance_request_ , _additional_input_ ). 

Comment: _status_ indications other than SUCCESS could be ERROR_FLAG or 

**CATASTROPHIC_ERROR_FLAG** , in which case, the status is returned to the consuming application to handle. The **Get_entropy_input** call could return a _status_ of ERROR_FLAG to indicate that entropy is currently unavailable, and could return **CATASTROPHIC_ERROR_FLAG** to indicate that an entropy source failed. 

- 7.2 If ( _status_ ≠ SUCCESS), then return ( _status, Null_ ). 

- 7.3 Using _state_handle_ , obtain the new internal state. 

- 7.4 _additional_input_ = the _Null_ string. 

- 7.5 Clear the _reseed_required_flag_ . 

Comment: Request the generation of _pseudorandom_bits_ using the appropriate generate algorithm in <u>Section 10.</u> 

8. ( _status_ , _pseudorandom_bits, new_working_state_ ) = **Generate_algorithm** ( _working_state_ , _requested_number_of_bits_ , _additional_input_ ). 

9. If _status_ indicates that a reseed is required before the requested bits can be generated, then 

   - 9.1 Set the _reseed_required_flag._ 

   - 9.2 If the _prediction_resistance_flag_ is set, then set the _prediction_resistance request_ indication. 

   - 9.3 Go to step 7. 

10. Replace the old _working_state_ in the internal state of the DRBG instantiation (e.g., as indicated by _state_handle_ ) with the values of _new_working_state_ . 

11. Return (SUCCESS, _pseudorandom_bits_ ). 

<u>Implementation notes:</u> 

34 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

If a reseed capability is not supported, or a reseed is not desired, then generate process steps 6 and 7 are removed; generate process step 9 is replaced by: 

9. If _status_ indicates that a reseed is required before the requested bits can be generated, then 

   - 9.1 _status_ = **Uninstantiate_function** ( _state_handle_ ). 

   - 9.2 Return an indication that the DRBG instantiation can no longer be used. 

#### **9.3.2 Reseeding at the End of the Seedlife** 

When pseudorandom bits are requested by a consuming application, the generate function checks whether or not a reseed is required by comparing the counter within the internal state (see <u>Section 8.3) against a predetermined reseed interval for the DRBG implementation. This is</u> specified in the generate process (see Section 9.3.1) as follows: 

- a. Step 6 clears the _reseed_required_flag_ . 

- b. Step 7 checks the value of the _reseed_required_flag_ . At this time, the _reseed_required_flag_ is clear, so step 7 is skipped unless prediction resistance was requested by the consuming application. For the purposes of this explanation, assume that prediction resistance was not requested. 

- c. Step 8 calls the **Generate_algorithm** , which checks whether a reseed is required. If it is required, an appropriate _status_ is returned. 

- d. Step 9 checks the _status_ returned by the **Generate_algorithm** . If the _status_ does not indicate that a reseed is required, the generate process continues with step 10. 

- e. However, if the status indicates that a reseed is required (see step 9), then the _reseed_required_flag_ is set, the _prediction_resistance_request_ indicator is set if the instantiation is capable of performing prediction resistance, and processing continues by going back to step 7. This is intended to obtain fresh entropy for reseeding at the end of the reseed interval whenever access to fresh entropy is available (see the concept of Live Entropy Sources in [SP 800-90C]). 

- f. The substeps in step 7 are executed. The reseed function is called; any _additional_input_ provided by the consuming application in the generate request is used during reseeding. The new values of the internal state are acquired, any _additional_input_ provided by the consuming application in the generate request is replaced by a _Null_ string, and the _reseed_required_flag_ is cleared. 

- g. The generate algorithm is called (again) in step 8, the check of the returned _status_ is made in step 9, and (presumably) step 10 is then executed. 

#### **9.3.3 Handling Prediction Resistance Requests** 

When pseudorandom bits are requested by a consuming application with prediction resistance, the generate function specified in <u>Section 9.3.1 checks that the instantiation allows prediction</u> resistance requests (see step 5 of the generate process); clears the _reseed_required_flag_ (even though the flag won’t be used in this case); executes the substeps of generate process step 7, resulting in a reseed, a new internal state for the instantiation, and setting the additional input to a 

35 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

_Null_ value; obtains pseudorandom bits (see generate process step 8); passes through generate process step 9, since another reseed will not be required; and continues with generate process step 10. 

#### **9.4 Removing a DRBG Instantiation** 

The internal state for an instantiation may need to be “released” by erasing (i.e., zeroizing) the contents of the internal state. The uninstantiate function: 

1. Checks the input parameter for validity, and 

2. Empties the internal state. 

The following or an equivalent process **shall** be used to remove (i.e., uninstantiate) a DRBG instantiation: 

#### **Uninstantiate_function (** _state_handle_ **):** 

1. _state_handle_ : A pointer or index that indicates the internal state to be “released”.  If a state handle is not used by an implementation because the implementation does not support multiple simultaneous instantiations, a _state_handle_ is not provided as input. In this case, uninstantiate process step 1 is omitted, and process step 2 erases the internal state. 

#### **Output to a consuming application after uninstantiation:** 

1. _status_ : The status returned from the function. 

#### **Information retained within the DRBG mechanism boundary after uninstantiation:** 

1. An empty internal state. 

#### **Uninstantiate Process:** 

1. If _state_handle_ indicates an invalid state, then return (ERROR_FLAG **)** . 

2. Erase the contents of the internal state indicated by _state_handle_ . 

3. Return (SUCCESS **)** . 

36 

NIST SP 800-90A Rev. 1 

HASH_DRBG Recommendation for Random Number 

Generation Using Deterministic RBGs 

**10 DRBG Algorithm Specifications** 

Several DRBG mechanisms are specified in this Recommendation. The selection of a DRBG 

mechanism depends on several factors, including the security strength to be supported and what 

cryptographic primitives are available. An analysis of the consuming application’s requirements for random numbers **should** be conducted in order to select an appropriate DRBG mechanism. Conversion specifications required for the DRBG mechanism implementations (e.g., between 

integers and bitstrings) are provided in Appendix A. Pseudocode examples for each DRBG 

mechanism are provided in <u>Appendix B. A detailed discussion on DRBG mechanism selection is</u> provided in Appendix C. 

Examples for determining correct implementation of each DRBG are available at 

<u>http://csrc.nist.gov/groups/ST/toolkit/examples.html.</u> 

**10.1 DRBG Mechanisms Based on Hash Functions** 

A DRBG mechanism may be based on a hash function that is one-way. The hash-based DRBG mechanisms specified in this Recommendation have been designed to use any **approved** hash function and may be used by consuming applications requiring various security strengths, providing that the appropriate hash function is used and sufficient entropy is obtained for the seed. 

The following are provided as DRBG mechanisms based on hash functions: 

1. The **Hash_DRBG** specified in Section 10.1.1. 

2. The **HMAC_DRBG** specified in Section 10.1.2. The maximum security strength that can be supported by each DRBG based on a hash function is the security strength of the hash function for pre-image resistance; these security strengths are provided in [SP 800-107]. [SP 800-57] identifies hash functions that can be used to support a 

required security strength. 

This Recommendation supports only four security strengths: 112, 128, 192, and 256 bits. Table 2 specifies the values that **shall** be used for the function envelopes<sup>6</sup> and DRBG algorithm for each **approved** hash function. 

6 Discussed in Section 9. 

37 

NIST SP 800-90A Rev. 1 

HASH_DRBG 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Table 2: Definitions for Hash-Based DRBG Mechanisms** 

||**SHA-1**|**SHA-224**<br>**and SHA-**<br>**512/224**|**SHA-256**<br>**and**<br>**SHA-**<br>**512/256**|**SHA-384**|**SHA-512**|
|---|---|---|---|---|---|
|**Supported security strengths**||S|ee[SP 800-5|7]||
|**_highest_supported_security_strength_**||S|ee[SP 800-5|7]||
|**Output Block Length(****_outlen_)**|160|224|256|384|512|
|**Required minimum entropy for**<br>**instantiate and reseed**||_s_|_ecurity_stren_|_gth_||
|**Minimum entropy input length**<br>**(****_min_length_)**||_s_|_ecurity_stren_|_gth_||
|**Maximum entropy input length**<br>**(****_max_ length_)**|||2<sup>35</sup>bits|||
|**Seed length (****_seedlen_) for**<br>**Hash_DRBG**|440|440|440|888|888|
|**Maximum personalization string**<br>**length**<br>**(****_max_personalization_string_length_)**|||2<sup>35</sup>bits|||
|**Maximum additional_input length**<br>**(****_max_additional_input_length_)**|||2<sup>35</sup>bits|||
|**_max_number_of_bits_per_request_**|||2<sup>19</sup>bits|||
|**Maximum number of requests**<br>**between reseeds(****_reseed_interval_)**|||2<sup>48</sup>|||

Note that since SHA-224 is based on SHA-256, there is no efficiency benefit when using SHA224, rather than SHA-256. Also note that since SHA-384, SHA-512/224 and SHA-512/256 are based on SHA-512, there is no efficiency benefit for using these three SHA mechanisms, rather than using SHA-512. However, efficiency is just one factor to consider when selecting the appropriate hash function to use as part of a DRBG mechanism. 

#### **10.1.1 Hash_DRBG** 

Figure 8 presents the normal operation of the **Hash_DRBG** generate algorithm **.** The **Hash_DRBG** requires the use of a hash function during the instantiate, reseed and generate functions; the same hash function **shall** be used throughout a **Hash_DRBG** instantiation. **Hash_DRBG** uses the derivation function specified in <u>Section 10.3.1 during instantiation and</u> reseeding.  The security strength of the hash function to be used **shall** meet or exceed the desired security strength required by the consuming application for DRBG output (see [SP 800-57]). 

38 

NIST SP 800-90A Rev. 1 HASH_DRBG 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **10.1.1.1 Hash_DRBG Internal State** 

The _internal_state_ for **Hash_DRBG** consists of: 

1. The _working_state_ : 

   - a. A value ( _V_ ) of _seedlen_ bits that is updated during each call to the DRBG. 

   - b. A constant ( _C_ ) of _seedlen_ bits that depends on the _seed_ . 

   - c. A counter ( _reseed_counter_ ) that indicates the number of requests for pseudorandom bits since new _entropy_input_ was obtained during instantiation or reseeding. 

2. Administrative information: 

   - a. The _security_strength_ of the DRBG instantiation. 

   - b. A _prediction_resistance_flag_ that indicates whether or not a prediction resistance capability is available for the DRBG instantiation. 

The values of _V_ and _C_ are the critical values of the internal state upon which the security of this DRBG mechanism depends (i.e., _V_ and _C_ are the “secret values” of the internal state). 

#### **10.1.1.2 Instantiation of Hash_DRBG** 

**Figure 8: Hash_DRBG** 

Notes for the instantiate function specified in <u>Section 9.1:</u> 

The instantiation of **Hash_DRBG** requires a call to the **Instantiate_function** specified in <u>Section 9.1. Process step 9 of that function calls the instantiate algorithm in this section.</u> 

The values of _highest_supported_security_strength_ and _min_length_ are provided in Table 2 of Section 10.1. The contents of the internal state are provided in Section 10.1.1.1. 

The instantiate algorithm: 

Let **Hash_df** be the hash derivation function specified in <u>Section 10.3.1 using the selected</u> hash function. The output block length ( _outlen_ ), seed length ( _seedlen_ ) and appropriate _security_strengths_ for the implemented hash function are provided in Table 2 of <u>Section 10.1.</u> 

39 

NIST SP 800-90A Rev. 1 

HASH_DRBG 

Recommendation for Random Number Generation Using Deterministic RBGs 

The following process or its equivalent **shall** be used as the instantiate algorithm for this DRBG mechanism (see step 9 of the instantiate process in Section 9.1). 

**Hash_DRBG_Instantiate_algorithm (** _entropy_input, nonce, personalization_string, security_strength_ **):** 

1. _entropy_input_ : The string of bits obtained from the randomness source. 

2. _nonce_ : A string of bits as specified in <u>Section 8.6.7.</u> 

3. _personalization_string_ : The personalization string received from the consuming application. Note that the length of the _personalization_string_ may be zero. 

4. _security_strength_ : The security strength for the instantiation. This parameter is optional for **Hash_DRBG** , since it is not used. 

#### **Output:** 

1. _initial_  working_state_ : The initial values for _V_ , _C_ , and _reseed_counter_ (see <u>Section 10.1.1.1).</u> 

#### **Hash_DRBG Instantiate Process:** 

1. _seed_material_ = _entropy_input_ || _nonce_ || _personalization_string_ . 

2. _seed_ = **Hash_df** ( _seed_material_ , _seedlen_ ). 

3. _V_ = _seed_ . 

4. _C_ = **Hash_df** ((0x00 || _V_ ), _seedlen_ ). Comment: Precede _V_ with a byte of zeros. 

5. _reseed_counter_ = 1. 

6. **Return** ( _V_ , _C_ , _reseed_counter_ ). 

#### **10.1.1.3 Reseeding a Hash_DRBG Instantiation** 

Notes for the reseed function specified in Section 9.2: 

The reseeding of a **Hash_DRBG** instantiation requires a call to the **Reseed_function** specified in <u>Section 9.2. Process step 6 of that function calls the reseed algorithm specified in</u> this section. The values for _min_length_ are provided in Table 2 of Section 10.1. 

The reseed algorithm: 

Let **Hash_df** be the hash derivation function specified in <u>Section 10.3.1 using the selected</u> hash function. The value for _seedlen_ is provided in Table 2 of <u>Section 10.1.</u> 

The following process or its equivalent **shall** be used as the reseed algorithm for this DRBG mechanism (see step 6 of the reseed process in Section 9.2): 

#### **Hash_DRBG_Reseed_algorithm (** _working_state, entropy_input, additional_input_ **):** 

1. _working_state_ : The current values for _V_ , _C_ , and _reseed_counter_ (see Section 10.1.1.1). 

2. _entropy_input_ : The string of bits obtained from the randomness source. 

40 

NIST SP 800-90A Rev. 1 

HASH_DRBG 

Recommendation for Random Number Generation Using Deterministic RBGs 

3. _additional_input_ : The additional input string received from the consuming application. Note that the length of the _additional_input_ string may be zero. 

#### **Output:** 

1. _new_working_state_ : The new values for _V_ , _C_ , and _reseed counter._ 

#### **Hash_DRBG Reseed Process:** 

1. _seed_material_ = 0x01 || _V_ || _entropy_input_ || _additional_input_ . 

2. _seed_ = **Hash_df** ( _seed_material_ , _seedlen_ ). 

3. _V_ = _seed_ . 

4. _C_ = **Hash_df** ((0x00 || _V_ ), _seedlen_ ) _._ Comment: Preceed with a byte of all zeros. 

5. _reseed_counter_ = 1. 

6. Return ( _V_ , _C_ , and _reseed_counter_ ). 

#### **10.1.1.4 Generating Pseudorandom Bits Using Hash_DRBG** 

Notes for the generate function specified in Section 9.3: 

The generation of pseudorandom bits using a **Hash_DRBG** instantiation requires a call to the generate function specified in <u>Section 9.3. Process step 8 of that function calls the generate</u> algorithm specified in this section. The values for _max_number_of_bits_per_request_ and _outlen_ are provided in Table 2 of <u>Section 10.1.</u> 

The generate algorithm: 

Let **Hash** be the selected hash function. The seed length ( _seedlen_ ) and the maximum interval between reseeding ( _reseed_interval_ ) are provided in Table 2 of Section 10.1. Note that for this DRBG mechanism, the reseed counter is used to update the value of _V_ , as well as to count the number of generation requests. 

The following process or its equivalent **shall** be used as the generate algorithm for this DRBG mechanism (see step 8 of the generate process in Section 9.3): 

**Hash_DRBG_Generate_algorithm (** _working_state, requested_number_of_bits, additional_input_ **):** 

1. _working_state_ : The current values for _V_ , _C_ , and _reseed_counter_ (see Section <u>10.1.1.1).</u> 

2. _requested_number_of_bits_ : The number of pseudorandom bits to be returned to the generate function. 

3. _additional_input_ : The additional input string received from the consuming application. Note that the length of the _additional_input_ string may be zero. 

#### **Output:** 

41 

NIST SP 800-90A Rev. 1 HASH_DRBG 

Recommendation for Random Number Generation Using Deterministic RBGs 

1. _status_ : The status returned from the function. The _status_ will indicate **SUCCESS,** or indicate that a reseed is required before the requested pseudorandom bits can be generated. 

2. _returned_bits_ : The pseudorandom bits to be returned to the generate function. 

3. _new_  working_state_ : The new values for _V_ , _C_ , and _reseed_counter._ 

#### **Hash_DRBG_Generate Process:** 

1. If _reseed_counter_ > _reseed_interval_ , then return an indication that a reseed is required. 

2. If ( _additional_input_ ≠ _Null_ ), then do 

   - 2.1 _w_ = **Hash** (0x02 || _V_ || _additional_input_ ). 

   - 2.2 _V_ = ( _V_ + _w_ ) mod 2<sup>_seedlen_</sup> _._ 

3. ( _returned_bits_ ) = **Hashgen** ( _requested_number_of_bits_ , _V_ ). 

4. _H_ = **Hash** (0x03 || _V_ ). 

5. _V_ = ( _V_ + _H_ + _C_ + _reseed_counter_ ) mod 2<sup>_seedlen_</sup> _._ 

6. _reseed_counter_ = _reseed_counter_ + 1. 

7. Return ( **SUCCESS** , _returned_bits_ , _V_ , _C_ , _reseed_counter_ ). 

**Hashgen (** _requested_number_of_bits_ , _V_ **)** : 

**Input:** 

1. _requested_no_of_bits_ : The number of bits to be returned. 

2. _V_ : The current value of _V_ . 

**Output:** 

1. _returned_bits_ : The generated bits to be returned to the generate function. 

**Hashgen Process:** 

2. _data_ = _V._ 

3. _W_ = the _Null_ string. 

4. For _i_ = 1 to _m_ 

   - 4.1 _w_ = **Hash** ( _data_ ). 

   - 4.2 _W_ = _W_ || _w._ 

   - 4.3 _data_ = ( _data_ + 1) mod 2<sup>_seedlen_</sup> . 

5. _returned_bits_ = **leftmost** ( _W_ , _requested_no_of_bits_ ) _._ 

6. Return ( _returned_bits_ ). 

42 

NIST SP 800-90A Rev. 1 

HMAC_DRBG Recommendation for Random Number Generation Using Deterministic RBGs 

#### **10.1.2 HMAC_DRBG** 

**HMAC_DRBG** uses multiple occurrences of an **approved** keyed hash function, which is based on an **approved** hash function. This DRBG mechanism uses the **HMAC_DRBG_Update** function specified in <u>Section 10.1.2.2 and the</u> **HMAC** function within the **HMAC_DRBG_Update** function as the derivation function during instantiation and reseeding. The same hash function **shall** be used throughout an **HMAC_DRBG** instantiation. The hash function used **shall** meet or exceed the security strength required by the consuming application for DRBG output (see [SP 800-57]). 

Figure 9 depicts the **HMAC_DRBG** in three stages. **HMAC_DRBG** is specified using an internal function ( **HMAC_DRBG_Update)** . This function is called during the **HMAC_DRBG** instantiate, generate and reseed algorithms to adjust the internal state when new entropy or additional input is provided, as well as to update the internal state after pseudorandom bits are generated. The operations in the top portion of the figure are only performed if the additional input is not null. Figure 10 depicts the **HMAC_DRBG_Update** function. 

#### **10.1.2.1 HMAC_DRBG Internal State** 

The internal state for **HMAC_DRBG** consists of: 

1. The _working_state_ : 

- a. The value _V_ of _outlen_ bits, which is updated each time another _outlen_ bits of output are produced (where _outlen_ is specified in Table 2 of Section <u>10.1).</u> 

- b. The _outlen-_ bit _Key_ , which is updated at least once each time that the DRBG mechanism 

generates pseudorandom bits. 

**Figure 9: HMAC_DRBG Generate Function** 

- c. A counter ( _reseed_counter_ ) that indicates the number of requests for pseudorandom bits since instantiation or reseeding. 

43 

NIST SP 800-90A Rev. 1 

HMAC_DRBG 

Recommendation for Random Number 

Generation Using Deterministic RBGs 

2. Administrative information: 

   - a. The _security_strength_ of the DRBG instantiation. 

   - b. A _prediction_resistance_flag_ that indicates whether or not a prediction resistance capability is required for the DRBG instantiation. 

The values of _V_ and _Key_ are the critical values of the internal state upon which the security of this DRBG mechanism depends (i.e., _V_ and _Key_ are the “secret values” of the internal state). 

#### **10.1.2.2 The HMAC_DRBG Update Function (Update)** 

The **HMAC_DRBG_Update** function updates the internal state of **HMAC_DRBG** using the _provided_data_ . Note that for this DRBG mechanism, the 

**HMAC_DRBG_Update** function also serves as a derivation function for the instantiate and reseed functions. 

**Figure 10: HMAC_DRBG_Update Function** 

Let **HMAC** be the keyed hash function specified in [FIPS 198] using the hash function selected for the DRBG mechanism from Table 2 in <u>Section 10.1.</u> 

The following or an equivalent process **shall** be used as the **HMAC_DRBG_Update** function. 

**HMAC_DRBG_Update (** _provided_data, K, V_ **):** 

1. _provided_data_ : The data to be used. 

2. _K_ : The current value of _Key_ . 

3. _V_ : The current value of _V_ . 

#### **Output:** 

1. _K_ : The new value for _Key_ . 

_2. V_ : The new value for _V_ . 

#### **HMAC_DRBG Update Process:** 

1. _K_ = **HMAC** ( _K_ , _V_ || 0x00 || _provided_data_ ). 

2. _V_ = **HMAC** ( _K_ , _V_ ). 

44 

NIST SP 800-90A Rev. 1 

HMAC_DRBG 

Recommendation for Random Number 

Generation Using Deterministic RBGs 

3. If ( _provided_data_ = _Null_ ), then return _K_ and _V_ . 

4. _K_ = **HMAC** ( _K_ , _V_ || 0x01 || _provided_data_ ). 

5. _V_ = **HMAC** ( _K_ , _V_ ). 

6. Return **(** _K_ , _V_ ). 

#### **10.1.2.3 Instantiation of HMAC_DRBG** 

Notes for the instantiate function specified in <u>Section 9.1:</u> 

The instantiation of **HMAC_DRBG** requires a call to the **Instantiate_function** specified in <u>Section 9.1. Process step 9 of that function calls the instantiate algorithm</u> specified in this section. The values of _highest_supported_security_strength_ and _min _length_ are provided in Table 2 of <u>Section 10.1. The contents of the internal state are</u> provided in Section 10.1.2.1. 

The instantiate algorithm: 

Let **HMAC_DRBG_Update** be the function specified in Section 10.1.2.2. The output block length ( _outlen_ ) is provided in Table 2 of Section 10.1. 

The following process or its equivalent **shall** be used as the instantiate algorithm for this DRBG mechanism (see step 9 of the instantiate process in <u>Section 9.1):</u> 

**HMAC_DRBG_Instantiate_algorithm (** _entropy_input, nonce,_ 

_personalization_string, security_strength_ **):** 

1. _entropy_input_ : The string of bits obtained from the randomness source. 

2. _nonce_ : A string of bits as specified in <u>Section 8.6.7.</u> 

3. _personalization_string_ : The personalization string received from the consuming application. Note that the length of the _personalization_string_ may be zero. 

4. _security_strength_ : The security strength for the instantiation. This parameter is optional for **HMAC_DRBG** , since it is not used. 

#### **Output:** 

1. _initial_  working_state_ : The initial values for _V_ , _Key_ and _reseed_counter_ (see <u>Section 10.1.2.1).</u> 

#### **HMAC_DRBG Instantiate Process:** 

1. _seed_material_ = _entropy_input_ || _nonce_ || _personalization_string_ . 

2. _Key_ = 0x00 00...00. Comment: _outlen_ bits. 

3. _V_ = 0x01 01...01. Comment: _outlen_ bits. 

Comment: Update _Key_ and _V_ . 

4. ( _Key_ , _V_ ) = **HMAC_DRBG_Update** ( _seed_material_ , _Key, V_ ). 

5. _reseed_counter_ = 1. 

6. Return ( _V_ , _Key_ . _reseed_counter_ ). 

45 

NIST SP 800-90A Rev. 1 

HMAC_DRBG Recommendation for Random Number Generation Using Deterministic RBGs 

#### **10.1.2.4 Reseeding an HMAC_DRBG Instantiation** 

Notes for the reseed function specified in <u>Section 9.2:</u> 

The reseeding of an **HMAC_DRBG** instantiation requires a call to the **Reseed_function** specified in Section 9.2. Process step 6 of that function calls the reseed algorithm specified in this section. The values for _min_length_ are provided in Table 2 of <u>Section 10.1.</u> 

The reseed algorithm: 

Let **HMAC_DRBG_Update** be the function specified in Section 10.1.2.2. The following process or its equivalent **shall** be used as the reseed algorithm for this DRBG mechanism (see step 6 of the reseed process in Section 9.2): 

#### **HMAC_DRBG_Reseed_algorithm (** _working_state, entropy_input, additional_input_ **):** 

1. _working_state_ : The current values for _V_ , _Key_ and _reseed_counter_ (see Section <u>10.1.2.1).</u> 

2. _entropy_input_ : The string of bits obtained from the randomness source. 

3. _additional_input_ : The additional input string received from the consuming application. Note that the length of the _additional_input_ string may be zero. 

#### **Output:** 

1. _new_working_state_ : The new values for _V_ , _Key_ and _reseed_counter._ 

#### **HMAC_DRBG Reseed Process:** 

1. _seed_material_ = _entropy_input_ || _additional_input_ . 

2. ( _Key_ , _V_ ) = **HMAC_DRBG_Update** ( _seed_material_ , _Key, V_ ). 

3. _reseed_counter_ = 1. 

4. **Return** ( _V_ , _Key_ , _reseed_counter_ ). 

#### **10.1.2.5 Generating Pseudorandom Bits Using HMAC_DRBG** 

Notes for the generate function specified in Section 9.3: 

The generation of pseudorandom bits using an **HMAC_DRBG** instantiation requires a call to the **Generate_function** specified in <u>Section 9.3. Process step 8 of that function</u> calls the generate algorithm specified in this section. The values for 

_max_number_of_bits_per_request_ and _outlen_ are provided in Table 2 of <u>Section 10.1.</u> 

The generate algorithm: 

Let **HMAC** be the keyed hash function specified in [FIPS 198] using the hash function selected for the DRBG mechanism. The value for _reseed_interval_ is defined in Table 2 of Section 10.1. 

The following process or its equivalent **shall** be used as the generate algorithm for this DRBG mechanism (see step 8 of the generate process in Section 9.3): 

46 

NIST SP 800-90A Rev. 1 

HMAC_DRBG 

Recommendation for Random Number 

Generation Using Deterministic RBGs 

**HMAC_DRBG_Generate_algorithm (** _working_state, requested_number_of_bits, additional_input_ **):** 

1. _working_state_ : The current values for _V_ , _Key_ and _reseed_counter_ (see Section <u>10.1.2.1).</u> 

2. _requested_number_of_bits_ : The number of pseudorandom bits to be returned to the generate function. 

3. _additional_input_ : The additional input string received from the consuming application. Note that the length of the _additional_input_ string may be zero. 

#### **Output:** 

1. _status_ : The status returned from the function. The _status_ will indicate **SUCCESS,** or indicate that a reseed is required before the requested pseudorandom bits can be generated. 

2. _returned_bits_ : The pseudorandom bits to be returned to the generate function. 

3. _new_  working_state_ : The new values for _V_ , _Key_ and _reseed_counter._ 

#### **HMAC_DRBG Generate Process:** 

1. If _reseed_counter_ > _reseed_interval_ , then return an indication that a reseed is required. 

2. If _additional_input_ ≠ _Null_ , then ( _Key_ , _V_ ) = **HMAC_DRBG_Update** ( _additional_input_ , _Key_ , _V_ ). 

3. _temp_ = _Null_ . 

4. While ( **len** ( _temp_ ) < _requested_number_of_bits_ ) do: 

   - 4.1 _V_ = **HMAC** ( _Key_ , _V_ ). 

   - 4.2 _temp_ = _temp_ || _V_ . 

5. _returned_bits_ = **leftmost** ( _temp_ , _requested_number_of_bits_ ). 

6. ( _Key_ , _V_ ) = **HMAC_DRBG_Update** ( _additional_input_ , _Key, V_ ). 

7. _reseed_counter_ = _reseed_counter_ + 1. 

8. Return ( **SUCCESS** , _returned_bits_ , _Key_ , _V_ , _reseed_counter_ ). 

47 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **10.2 DRBG Mechanism Based on Block Ciphers** 

A block cipher DRBG is based on a block cipher algorithm. The block cipher DRBG mechanism specified in this Recommendation has been designed to use any **approved** block cipher algorithm and may be used by consuming applications requiring various security strengths, providing that the appropriate block cipher algorithm and key length are used, and sufficient entropy is obtained for the seed. 

The maximum security strength that can be supported by the DRBG depends on the block cipher and key size used; the security strengths that can be supported by the block ciphers and key sizes are provided in [SP 800-57]. 

#### **10.2.1 CTR_DRBG** 

**CTR_DRBG** uses an **approved** block cipher algorithm in the counter mode as specified in [SP <u>800-38A], but allows the counter field to be a</u> subset of the input block, as specified in [SP 800- <u>38D]. Note that for TDEA, the input and output</u> block lengths are 64 bits, and for AES, the lengths are 128 bits. 

The same block cipher algorithm and key length **shall** be used for all block cipher operations of this DRBG. The block cipher algorithm and key length **shall** meet or exceed the security requirements of the consuming application. 

**Figure 11: CTR_DRBG Update Function** 

**CTR_DRBG** is specified using an internal function ( **CTR_DRBG_Update** ). Figure 11 depicts the **CTR_DRBG_Update** function. This function is called by the instantiate, generate and reseed algorithms to adjust the internal state when new entropy or additional input is provided, as well as to update the internal state after pseudorandom bits are generated. Figure 12 depicts the **CTR_DRBG** in three stages. The operations in the top portion of the figure are only performed if the additional input is not null. 

Table 3 specifies the values that **shall** be used for the function envelopes and **CTR_DRBG** mechanism. 

48 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Table 3: Definitions for the CTR_DRBG** 

||**3 Key TDEA**<br>**AES-**<br>**128**<br>**AES-**<br>**192**|**AES-**<br>**256**|
|---|---|---|
|**Supported security strengths**|See[SP 800-57]||
|**_highest_supported_security_strength_**|See[SP 800-57]||
|**Input and output block length**<br>**(****_blocklen_)**|64<br>128<br>128|128|
|**Counter field length(****_ctr_len_)**|4 ≤ _ctr_len_≤ _blocklen_||
|**Key length(****_keylen_)**|168<br>128<br>192|256|
|**Required minimum entropy for**<br>**instantiate and reseed**|_security_strength_||
|**Seed length(****_seedlen = outlen + keylen_)**|232<br>256<br>320|384|
|**If a derivation function is used:**|||
|**Minimum entropy input length**<br>**(****_min_length_)**|_security_strength_||
|**Maximum entropy input length**<br>**(****_max_length_)**|2<sup>35</sup>bits||
|**Maximum personalization string**<br>**length**<br>**(****_max_personalization_string_length_)**|2<sup>35</sup>bits||
|**Maximum additional_input length**<br>**(****_max_additional_input_length_)**|2<sup>35</sup>bits||
|**If a derivation function is not used:**|||
|**Minimum entropy input length**<br>**(****_min_length_ =****_blocklen_+ ****_keylen_)**|_seedlen_||
|**Maximum entropy input length**<br>**(****_max_length_= ****_blocklen_+ ****_keylen_)**|_seedlen_||
|**Maximum personalization string**<br>**length**<br>**(****_max_personalization_string_length_)**|_seedlen_||
|**Maximum additional_input length**<br>**(****_max_additional_input_length_)**|_seedlen_||
|<br> <br> <br>**_max_number_of_bits_per_request_**<br>**(**for_B_=(2<sup>_ctr_len_</sup>- 4)× _blocklen_)|<br>**min**(_B_, 2<sup>13</sup>)<br>**min**(_B_, 2<sup>19</sup>)|<br>|
|**Maximum number of requests between**<br>**reseeds(****_reseed_interval_)**|2<sup>32</sup><br>2<sup>48</sup>||

Note that the claimed security strength for **CTR_DRBG** depends on limiting the total number of generate requests and the bits provided per generate request according to the table above. 

49 

Recommendation for Random Number 

NIST SP 800-90A Rev. 1 

Generation Using Deterministic RBGs 

Without these limits, it becomes possible, in principle, for an attacker to 

observe enough outputs from 

- **CTR_DRBG** to distinguish its outputs from ideal random bits. 

- The **CTR_ DRBG** may be implemented to use the block cipher derivation function specified in Section 

- <u>10.3.2</u> during instantiation and reseeding.  However, the DRBG mechanism is specified to allow an implementation tradeoff with respect to the use of this derivation function. The 

use of the derivation function is optional if either an **approved** RBG or 

- an entropy source provides full entropy output when entropy input is requested 

- by the DRBG mechanism. Otherwise, 

- the derivation function **shall** be used. 

- Table 3 provides the lengths required 

- for the _entropy_input_ , 

- _personalization_string_ and 

- _additional_input_ for each case. 

When using TDEA as the selected block cipher algorithm, the keys **shall** 

be handled as 64-bit blocks containing 

56 bits of key and 8 bits of parity as specified for the TDEA engine specified in [SP 800-67]. 

- **10.2.1.1 CTR_DRBG Internal State** 

- The internal state for the **CTR_DRBG** consists of: 

#### 1. The _working_state_ : 

- a. The value _V_ of _blocklen_ **Figure 12: CTR-DRBG** 

bits, which is updated each 

      - time another _blocklen_ bits of output are produced. 

   - b. The _keylen_ -bit _Key_ , which is updated whenever a predetermined number of output blocks are generated. 

   - c. A counter ( _reseed_counter_ ) that indicates the number of requests for pseudorandom bits since instantiation or reseeding. 

2. Administrative information: 

50 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

- a. The _security_strength_ of the DRBG instantiation. 

- b. A _prediction_resistance_flag_ that indicates whether or not a prediction resistance capability is required for the DRBG instantiation. 

The values of _V_ and _Key_ are the critical values of the internal state upon which the security of this DRBG mechanism depends (i.e., _V_ and _Key_ are the “secret values” of the internal state). 

#### **10.2.1.2 The Update Function (CTR_DRBG_Update)** 

The **CTR_DRBG_Update** function updates the internal state of the **CTR_DRBG** using the _provided_data_ . The values for _blocklen_ , _keylen_ and _seedlen_ are provided in Table 3 of <u>Section 10.2.1. The value of</u> _ctr_len_ is known by an implementation. The block cipher operation in step 2.2 of the **CTR_DRBG_UPDATE** process uses the selected block cipher algorithm. The specification of **Block_Encrypt** is discussed in <u>Section 10.3.3.</u> 

The following or an equivalent process **shall** be used as the **CTR_DRBG_Update** function. 

**CTR_DRBG_Update (** _provided_data, Key, V_ **):** 

1. _provided_data_ : The data to be used. This must be exactly _seedlen_ bits in length; this length is guaranteed by the construction of the _provided_data_ in the instantiate, reseed and generate functions. 

2. _Key_ : The current value of _Key_ . 

3. _V_ : The current value of _V_ . 

#### **Output:** 

1. _K_ : The new value for _Key_ . 

2. _V_ : The new value for _V_ . 

#### **CTR_DRBG_Update Process:** 

1. _temp = Null._ 

2. While ( **len** ( _temp_ ) < _seedlen_ ) do 

   - 2.1 If _ctr_len_ < _blocklen_ 

      - 2.1.1 _inc_ = ( **rightmost** ( _V_ , _ctr_len_ ) + 1) mod 2<sup>_ctr_len_</sup> . 

      - 2.1.2 _V =_ **leftmost** ( _V_ , _blocklen_ - _ctr_len_ ) _|| inc_ . 

Else _V = (V+1) mod 2_<sup>_blocklen_</sup> 

_._ 

   - 2.2 _output_block_ = **Block_Encrypt** ( _Key_ , _V_ ). 

   - 2.3 _temp_ = _temp_ || _output_block_ . 

3. _temp_ = **leftmost** ( _temp_ , _seedlen_ ). 

- 4 _temp_ = _temp_ ⊕ _provided_data_ . 

5. _Key_ **_=_ leftmost** ( _temp_ , _keylen_ ) _._ 

6. _V_ = **rightmost** ( _temp_ , _blocklen_ ) _._ 

51 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### 7. Return ( _Key_ , _V_ ). 

#### **10.2.1.3 Instantiation of CTR_DRBG** 

Notes for the instantiate function specified in <u>Section 9.1:</u> 

The instantiation of **CTR_DRBG** requires a call to the **Instantiate_function** specified in <u>Section 9.1. Process step 9 of that function calls the instantiate algorithm specified in this</u> 

section. The values of _highest_supported_security_strength_ and _min_length_ are provided in Table 3 of <u>Section 10.2.1. The contents of the internal state are provided in Section 10.2.1.1.</u> 

The instantiate algorithm: 

For this DRBG mechanism, there are two cases for processing. In each case, let **CTR_DRBG_Update** be the function specified in Section 10.2.1.2. The output block length ( _blocklen_ ), key length ( _keylen_ ), seed length ( _seedlen_ ) and _security_strengths_ for the block cipher algorithms are provided in Table 3 of <u>Section 10.2.1.</u> 

##### **10.2.1.3.1 Instantiation When a Derivation Function is Not Used** 

When instantiation is performed using this method, full-entropy input is required, and a nonce is not used. The following process or its equivalent **shall** be used as the instantiate algorithm for this DRBG mechanism: 

- **CTR_DRBG_Instantiate_algorithm (** _entropy_input, personalization_string, security_strength_ **):** 

   1. _entropy_input_ : The string of bits obtained from the randomness source. 

   2. _personalization_string_ : The personalization string received from the consuming application. Note that the length of the _personalization_string_ may be zero. 

   3. _security_strength_ : The security strength for the instantiation. This parameter is optional for **CTR_DRBG** . 

#### **Output:** 

1. _initial_  working_state_ : The initial values for _V_ , _Key_ , and _reseed_counter_ (see Section <u>10.2.1.1).</u> 

#### **CTR_DRBG Instantiate Process:** 

1. _temp_ = **len** ( _personalization_string_ ). 

Comment: Ensure that the length of the _personalization_string_ is exactly _seedlen_ bits. Note that in Section 9.1, processing step 3 obtained an _entropy_input_ of _seedlen_ bits using Table 3 to define the minimum and maximum lengths, which are both equal to _seedlen_ bits. 

2. If ( _temp_ < _seedlen_ ), then _personalization_string_ = _personalization_string_ || 0<sup>_seedlen -_</sup> _temp_ . 

3. _seed_material_ = _entropy_input_ ⊕ _personalization_string_ . 

52 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

4. _Key_ = 0<sup>_keylen_</sup> . Comment: _keylen_ bits of zeros. 

5. _V_ = 0<sup>_blocklen_</sup> . Comment: _blocklen_ bits of zeros. 

6. ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _seed_material_ , _Key_ , _V_ ). 

7. _reseed_counter_ = 1. 

8. Return ( _V_ , _Key_ , _reseed_counter_ ). 

##### **10.2.1.3.2 Instantiation When a Derivation Function is Used** 

When instantiation is performed using this method, the entropy input may or may not have full entropy; in either case, a nonce is required. 

Let **df** be the derivation function specified in <u>Section 10.3.2. When instantiation is performed</u> using this method, a nonce is required, whereas using the method in <u>Section 10.2.1.3.1 does not</u> require a nonce, since full entropy is provided when using that method. 

The following process or its equivalent **shall** be used as the instantiate algorithm for this DRBG mechanism: 

**CTR_DRBG_Instantiate_algorithm (** _entropy_input, nonce, personalization_string, security_strength_ **):** 

1. _entropy_input_ : The string of bits obtained from the randomness source. 

2. _nonce_ : A string of bits as specified in <u>Section 8.6.7.</u> 

3. _personalization_string_ : The personalization string received from the consuming application. Note that the length of the _personalization_string_ may be zero. 

4. _security_strength_ : The security strength for the instantiation. This parameter is optional for **CTR_DRBG** , since it is not used. 

#### **Output:** 

1. _initial_  working_state_ : The initial values for _V_ , _Key_ , and _reseed_counter_ (see Section <u>10.2.1.1).</u> 

#### **CTR_DRBG Instantiate Process:** 

1. _seed_material_ = _entropy_input_ || _nonce_ || _personalization_string_ . 

   - Comment: Ensure that the length of the _seed_material_ is exactly _seedlen_ bits. 

2. _seed_material_ = **df** ( _seed_material_ , _seedlen_ ). 

3. _Key_ = 0<sup>_keylen_</sup> . Comment: _keylen_ bits of zeros. 4. _V_ = 0<sup>_blocklen_</sup> . Comment: _blocklen_ bits of zeros. 

   - Comment: _blocklen_ bits of zeros. 

5. ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _seed_material_ , _Key_ , _V_ ). 

6. _reseed_counter_ = 1. 

7. Return ( _V_ , _Key_ , _reseed_counter_ ). 

53 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **10.2.1.4 Reseeding a CTR_DRBG Instantiation** 

Notes for the reseed function specified in <u>Section 9.2:</u> 

The reseeding of a **CTR_DRBG** instantiation requires a call to the **Reseed_function** specified in <u>Section 9.2. Process step 6 of that function calls the reseed algorithm specified in</u> this section. The values for _min _length_ are provided in Table 3 of <u>Section 10.2.1.</u> 

The reseed algorithm: 

For this DRBG mechanism, there are two cases for processing. In each case, let **CTR_DRBG_Update** be the function specified in Section 10.2.1.2. The seed length ( _seedlen_ ) is provided in Table 3 of Section 10.2.1. 

##### **10.2.1.4.1 Reseeding When a Derivation Function is Not Used** 

When reseeding is performed using this method, full-entropy input is required. 

The following process or its equivalent **shall** be used as the reseed algorithm for this DRBG mechanism (see step 6 of the reseed process in Section 9.2): 

#### **CTR_DRBG_Reseed_algorithm (** _working_state, entropy_input, additional_input_ **):** 

1. _working_state_ : The current values for _V_ , _Key_ and _reseed_counter_ (see Section <u>10.2.1.1).</u> 

2. _entropy_input_ : The string of bits obtained from the randomness source. 

3. _additional_input_ : The additional input string received from the consuming application. Note that the length of the _additional_input_ string may be zero. 

#### **Output:** 

1. _new_  working_state_ : The new values for _V_ , _Key_ , and _reseed_counter._ 

#### **CTR_DRBG Reseed Process:** 

1. _temp_ = **len** ( _additional_input_ ). 

Comment: Ensure that the length of the _additional_input_ is exactly _seedlen_ bits. The maximum length was checked in Section 9.2, processing step 2, using Table 3 to define the maximum length. 

2. If ( _temp_ < _seedlen_ ), then _additional_input_ = _additional_input_ || 0<sup>_seedlen - temp_</sup> . 

3. _seed_material_ = _entropy_input_ ⊕ _additional_input_ . 

4. ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _seed_material_ , _Key_ , _V_ ). 

5. _reseed_counter_ = 1. 

6. Return ( _V_ , _Key_ , _reseed_counter_ ). 

##### **10.2.1.4.2 Reseeding When a Derivation Function is Used** 

Let **df** be the derivation function specified in <u>Section 10.3.2.</u> 

54 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

The following process or its equivalent **shall** be used as the reseed algorithm for this DRBG mechanism (see reseed process step 6 of <u>Section 9.2):</u> 

**CTR_DRBG_Reseed_algorithm (** _working_state, entropy_input, additional_input_ **)** 

1. _working_state_ : The current values for _V_ , _Key_ and _reseed_counter_ (see Section <u>10.2.1.1).</u> 

2. _entropy_input_ : The string of bits obtained from the randomness source. 

3. _additional_input_ : The additional input string received from the consuming application. Note that the length of the _additional_input_ string may be zero. 

#### **Output:** 

1. _new_  working_state_ : The new values for _V_ , _Key_ , and _reseed_counter._ 

#### **CTR_DRBG Reseed Process:** 

1. _seed_material_ = _entropy_input_ || _additional_input_ . 

Comment: Ensure that the length of the _seed_material_ is exactly _seedlen_ bits. 

2. _seed_material_ = **df** ( _seed_material_ , _seedlen_ ). 

3. ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _seed_material_ , _Key_ , _V_ ). 

4. _reseed_counter_ = 1. 

5. Return ( _V_ , _Key_ , _reseed_counter_ ). 

#### **10.2.1.5 Generating Pseudorandom Bits Using CTR_DRBG** 

Notes for the generate function specified in Section 9.3: 

The generation of pseudorandom bits using a **CTR_DRBG** instantiation requires a call to the **Generate_function** specified in Section 9.3. Process step 8 of that function calls the generate algorithm specified in this section. The values for _max_number_of_bits_per_request_ and _max_additional_input_length_ , and _blocklen_ are provided in Table 3 of Section 10.2.1. If the derivation function is not used, then the maximum allowed length of _additional_input_ = _seedlen_ . 

For this DRBG mechanism, there are two cases for the processing. For each case, let **CTR_DRBG_Update** be the function specified in Section 10.2.1.2, and let **Block_Encrypt** be the function specified in Section 10.3.3. The seed length ( _seedlen_ ) and the value of _reseed_interval_ are provided in Table 3 of <u>Section 10.2.1. The value of</u> _ctr_len_ is known by an implementation. 

##### **10.2.1.5.1 Generating Pseudorandom Bits When a Derivation Function is Not Used** 

This method of generating bits is used when a derivation function is not used by an implementation. 

The following process or its equivalent **shall** be used as the generate algorithm for this DRBG mechanism (see step 8 of the generate process in <u>Section 9.3.3):</u> 

55 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**CTR_DRBG_Generate_algorithm (** _working_state, requested_number_of_bits, additional_input_ **):** 

1. _working_state_ : The current values for _V_ , _Key_ , and _reseed_counter_ (see <u>Section 10.2.1.1).</u> 

2. _requested_number_of_bits_ : The number of pseudorandom bits to be returned to the generate function. 

3. _additional_input_ : The additional input string received from the consuming application. Note that the length of the _additional_input_ string may be zero. 

#### **Output:** 

1. _status_ : The status returned from the function. The _status_ will indicate **SUCCESS,** or indicate that a reseed is required before the requested pseudorandom bits can be generated. 

2. _returned_bits_ : The pseudorandom bits returned to the generate function. 

3. _working_state_ : The new values for _V_ , _Key_ , and _reseed_counter._ 

#### **CTR_DRBG Generate Process:** 

1. If _reseed_counter_ > _reseed_interval_ , then return an indication that a reseed is required. 

2. If ( _additional_input_ ≠ _Null_ ), then 

Comment: Ensure that the length of the _additional_input_ is exactly _seedlen_ bits. The maximum length was checked in Section 9.3.3, processing step 4, using Table 3 to define the maximum length. If the length of the _additional input_ is _< seedlen_ , pad with zero bits. 

- 2.1 _temp_ = **len** ( _additional_input_ ). 

- 2.2 If ( _temp_ < _seedlen_ ), then _additional_input_ = _additional_input_ || 0<sup>_seedlen - temp_</sup> . 

- 2.3 ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _additional_input_ , _Key_ , _V_ ). 

Else _additional_input_ = 0<sup>_seedlen_</sup> . 

3. _temp_ = _Null_ . 

4. While ( **len** ( _temp_ ) < _requested_number_of_bits_ ) do: 

   - 4.1 If _ctr_len_ < _blocklen_ 

      - 4.1.1 _inc_ = ( **rightmost** ( _V_ , _ctr_len_ ) + 1) mod 2<sup>_ctr_len_</sup> . 

      - 4.1.2 _V =_ **leftmost** ( _V_ , _blocklen_ - _ctr_len_ ) _|| inc_ . 

Else _V = (V+1) mod 2_<sup>_blocklen_</sup> _._ 

56 

Recommendation for Random Number 

NIST SP 800-90A Rev. 1 

Generation Using Deterministic RBGs 

4.2 _output_block_ = **Block_Encrypt** ( _Key_ , V). 4.3 _temp_ = _temp_ || _output_block_ . 

5. _returned_bits_ = **leftmost** ( _temp_ , _requested_number_of_bits_ ). 

Comment: Update for backtracking resistance. 

7. _reseed_counter_ = _reseed_counter_ + 1. 

8. Return ( **SUCCESS** , _returned_bits_ , _Key_ , _V_ , _reseed_counter_ ). 

**10.2.1.5.2 Generating Pseudorandom Bits When a Derivation Function is Used** 

This method of generating bits is used when a derivation function is used by an implementation. 

Let **df** be the derivation function specified in <u>Section 10.3.2.</u> The following process or its equivalent **shall** be used as the generate algorithm for this DRBG mechanism (see step 8 of the generate process in <u>Section 9.3.3):</u> 

**CTR_DRBG_Generate_algorithm (** _working_state, requested_number_of_bits, additional_input_ **):** 

1. _working_state_ : The current values for _V_ , _Key_ , and _reseed_counter_ (see <u>Section</u> 

<u>10.2.1.1).</u> 2. _requested_number_of_bits_ : The number of pseudorandom bits to be returned to the generate function. 

3. _additional_input_ : The additional input string received from the consuming 

application. Note that the length of the _additional_input_ string may be zero. 

**Output:** 1. _status_ : The status returned from the function. The _status_ will indicate **SUCCESS,** or indicate that a reseed is required before the requested pseudorandom bits can be generated. 

2. _returned_bits_ : The pseudorandom bits returned to the generate function. 3. _working_state_ : The new values for _V_ , _Key_ , and _reseed_counter._ 

**CTR_DRBG Generate Process:** 

1. If _reseed_counter_ > _reseed_interval_ , then return an indication that a reseed is required. 

2. If ( _additional_input_ ≠ _Null_ ), then 2.1 _additional_input_ = **Block_Cipher_df** ( _additional_input_ , _seedlen_ ). 2.2 ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _additional_input_ , _Key_ , _V_ ). 

3. _temp_ = _Null_ . 

57 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

4. While ( **len** ( _temp_ ) < _requested_number_of_bits_ ) do: 

   - 4.1 If _ctr_len_ < _blocklen_ 

      - 4.1.1 _inc_ = ( **rightmost** ( _V_ , _ctr_len_ ) + 1) mod 2<sup>_ctr_len_</sup> . 

      - 4.1.2 _V =_ **leftmost** ( _V_ , _blocklen_ - _ctr_len_ ) _|| inc_ . 

Else 

      - 4.1.2 _V = (V+1) mod 2_<sup>_blocklen_</sup> 

         - _._ 

   - 4.2 _output_block_ = **Block_Encrypt** ( _Key_ , V). 

   - 4.3 _temp_ = _temp_ || _output_block_ . 

5. _returned_bits_ = **leftmost** ( _temp_ , _requested_number_of_bits_ ). 

Comment: Update for backtracking resistance. 

6. ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _additional_input_ , _Key_ , _V_ ). 

7. _reseed_counter_ = _reseed_counter_ + 1. 

8. Return ( **SUCCESS** , _returned_bits_ , _Key_ , _V_ , _reseed_counter_ ). 

#### **10.3 Auxiliary Functions** 

Derivation functions are internal functions that are used during DRBG instantiation and reseeding to either derive internal state values or to distribute entropy throughout a bitstring. Two methods are provided. One method is based on the use of hash functions (see <u>Section 10.3.1), and the other method is based on the use of block cipher algorithms (see Section 10.3.2). The block cipher derivation function specified in Section 10.3.2 uses a</u> **BCC** function and a **Block_Encrypt** call that are discussed in <u>Section 10.3.3.</u> 

The presence of these derivation functions in this Recommendation does not implicitly approve these functions for any other application. 

#### **10.3.1 Derivation Function Using a Hash Function (Hash_df)** 

This derivation function is used by the **Hash_DRBG** specified Section 10.1.1. The hash-based derivation function hashes an input string and returns the requested number of bits. Let **Hash** be the hash function used by the DRBG mechanism, and let _outlen_ be its output length. 

The following or an equivalent process **shall** be used to derive the requested number of bits: 

**Hash_df (** _input_string, no_of_bits_to_return_ **):** 

1. _input_string_ : The string to be hashed. 

2. _no_of_bits_to_return_ : The number of bits to be returned by **Hash_df.** The maximum length ( _max_number_of_bits_ ) is implementation dependent, but **shall** be less than or equal to (255 × _outlen_ ). _no_of_bits_to_return_ is represented as a 32-bit integer. 

#### **Output:** 

58 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

1. _status_ : The status returned from **Hash_df** . The status will indicate **SUCCESS** or **ERROR_FLAG** . 

2. _requested_bits_ : The result of performing the **Hash_df** . 

#### **Hash_df Process:** 

1. _temp_ = the Null string. 

3. _counter_ = 0x01. 

Comment: An 8-bit binary value representing the integer "1". 

4. For _i_ = 1 to _len_ do 

Comment : In step 4.1, _no_of_bits_to_return_ is used as a 32-bit string. 

   - 4.1 _temp_ = _temp_ || **Hash** ( _counter_ || _no_of_bits_to_return_ || _input_string_ ). 

   - 4.2 _counter_ = _counter_ + 1. 

5. _requested_bits_ = **leftmost** ( _temp_ , _no_of_bits_to_return_ ). 

6. Return ( **SUCCESS** , _requested_bits_ ). 

#### **10.3.2 Derivation Function Using a Block Cipher Algorithm (Block_Cipher_df)** 

This derivation function is used by the **CTR_DRBG** that is specified in <u>Section 10.2.</u> **BCC** and **Block_Encrypt** are discussed in Section 10.3.3. Let _outlen_ be its output block length, which is a multiple of eight bits for the **approved** block cipher algorithms, and let _keylen_ be the key length. 

The following or an equivalent process **shall** be used to derive the requested number of bits. 

#### **Block_Cipher_df (** _input_string, no_of_bits_to_return_ **):** 

1. _input_string_ : The string to be operated on. This string **shall** be a multiple of eight bits. 

2. _no_of_bits_to_return_ : The number of bits to be returned by **Block_Cipher_df** . The maximum length ( _max_number_of_bits_ ) is 512 bits for the currently **approved** block cipher algorithms. 

#### **Output:** 

1. _status_ : The status returned from **Block_Cipher_df** . The status will indicate **SUCCESS** or **ERROR_FLAG** . 

2. _requested_bits_ : The result of performing the **Block_Cipher_df** . 

#### **Block_Cipher_df Process:** 

1. If ( _number_of_bits_to_return_ > _max_number_of_bits_ ), then return an **ERROR_FLAG** and a Null string. 

59 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

2. _L_ = **len** ( _input_string_ )/8. Comment: _L_ is the bitstring representation of the integer resulting from **len** ( _input_string_ )/8. _L_ **shall** be represented as a 32-bit integer. 

3. _N_ = _number_of_bits_to_return_ /8. 

Comment: _N_ is the bitstring representation of the integer resulting from _number_of_bits_to_return_ /8. _N_ **shall** be represented as a 32-bit integer. 

Comment: Prepend the string length and the requested length of the output to the _input_string_ . 

4. _S_ = _L_ || _N_ || _input_string_ || 0x80. 

Comment: Pad _S_ with zeros, if necessary. 

5. While ( **len** ( _S_ ) mod _outlen_ ) ≠ 0, do _S_ = _S_ || 0x00. 

Comment: Compute the starting value. 

6. _temp_ = the _Null_ string. 

7. _i_ = 0. Comment: _i_ **shall** be represented as a 32-bit integer, i.e., **len** ( _i_ ) = 32. 

8. _K_ = **leftmost** (0x00010203...1D1E1F, _keylen_ ). 

9. While **len** ( _temp_ ) < _keylen_ + _outlen_ , do 9.1 _IV_ = _i_ || 0<sup>_outlen_-</sup><sup>**len**(</sup><sup>_i_)</sup> . Comment: The 32-bit integer representation of _i_ is padded with zeros to _outlen_ bits. 

   - 9.2 _temp_ = _temp_ || **BCC** ( _K_ , ( _IV_ || _S_ )). 

   - 9.3 _i_ = _i_ + 1. 

Comment: Compute the requested number of bits. 

10. _K_ = **leftmost** ( _temp_ , _keylen_ ). 

11. _X_ = **select** ( _temp_ , _keylen_ +1, _keylen_ + _outlen_ ). 

12. _temp_ = the _Null_ string. 

13. While **len** ( _temp_ ) < _number_of_bits_to_return_ , do 

   - 13.1 _X_ = **Block_Encrypt** ( _K_ , _X_ ). 

   - 13.2 _temp_ = _temp_ || _X_ . 

14. _requested_bits_ = **leftmost** ( _temp_ , _number_of_bits_to_return_ ). 

15. Return ( **SUCCESS** , _requested_bits_ ). 

#### **10.3.3 BCC and Block_Encrypt** 

**Block_Encrypt** is used for convenience in the specification of the **BCC** function. This function is not specifically defined in this Recommendation, but has the following meaning: 

60 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Block_Encrypt:** A basic encryption operation that uses the selected block cipher algorithm. The function call is: 

_output_block_ = **Block_Encrypt** ( _Key_ , _input_block_ ) 

For TDEA, the basic encryption operation is called the forward cipher operation (see [SP <u>800-67]); for AES, the basic encryption operation is called the cipher operation (see [FIPS 197]). The basic encryption operation is equivalent to an encryption operation on a single</u> block of data using the ECB mode. 

For the **BCC** function, let _outlen_ be the length of the output block of the block cipher algorithm to be used. 

The following or an equivalent process **shall** be used to derive the requested number of bits. 

**BCC (** _Key, data_ **):** 

1. _Key_ : The key to be used for the block cipher operation. 

2. _data_ : The data to be operated upon. Note that the length of _data_ must be a multiple of _outlen_ . This is guaranteed by **Block_Cipher_df** process steps 4 and 8.1 in <u>Section 10.3.2.</u> 

#### **Output:** 

1. _output_block_ : The result to be returned from the **BCC** operation. 

#### **BCC Process:** 

1. _chaining_value_ = 0<sup>_outlen_</sup> . Comment: Set the first chaining value to _outlen_ zeros. 

2. _n_ = **len** ( _data_ )/ _outlen_ . 

3. Starting with the leftmost bits of data, split _data_ into _n_ blocks of _outlen_ bits each, forming _block_ 1 to _blockn_ . 

4. For _i_ = 1 to _n_ do 

   - 4.1 _input_block_ = _chaining_value_ ⊕ _blocki_ . 

   - 4.2 _chaining_value_ = **Block_Encrypt** ( _Key_ , _input_block_ ). 

5. _output_block_ = chaining_value. 

6. Return ( _output_block_ ). 

61 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **11 Assurance** 

A user of a DRBG employed for cryptographic purposes requires assurance that the generator actually produces (pseudo) random and unpredictable bits. The user needs assurance that the design of the generator, its implementation and its use to support cryptographic services are adequate to protect the user's information. In addition, the user requires assurance that the generator continues to operate correctly. 

The design of each DRBG mechanism in this Recommendation has received an evaluation of its security properties prior to its selection for inclusion in this Recommendation. 

An implementer selects a DRBG mechanism (e.g., **HMAC_DRBG** ), an appropriate cryptographic primitive (e.g., SHA-256 or SHA-512), the DRBG functions to be used (i.e., instantiate, generate and/or reseed), and will determine whether or not the DRBG will be distributed (see Section 8.5). Each choice of components effectively defines a different DRBG type. For example, an implementation of **HMAC_DRBG** using SHA-256 is considered to be a different DRBG than **HMAC_DRBG** using SHA-512. 

An implementation **shall** be validated for conformance to this Recommendation by a NVLAPaccredited laboratory (see <u>Section 11.2). Such validations provide a higher level of assurance</u> that the DRBG mechanism is correctly implemented. 

Health tests on the DRBG mechanism **shall** be implemented within a DRBG mechanism boundary or sub-boundary in order to determine that the process continues to operate as designed and implemented. See Section 11.3 for further information. 

A cryptographic module containing a DRBG mechanism **shall** be validated (see [FIPS 140]). The consuming application or cryptographic service that uses a DRBG mechanism **should** also be validated and periodically tested for continued correct operation. However, this level of testing is outside the scope of this Recommendation. 

Note that any entropy input used for testing (either for validation testing or health testing) may be publicly known. Therefore, entropy input used for testing **shall not** be used for normal operational use. 

#### **11.1 Minimal Documentation Requirements** 

A set of documentation **shall** be developed that will provide assurance to users and validators that the DRBG mechanisms in this Recommendation have been implemented properly. Much of this documentation could be placed in a user manual. This documentation **shall** consist of the following as a minimum: 

- Document the method for obtaining entropy input. 

- Document how the implementation has been designed to permit implementation validation and health testing. 

- Document the type of DRBG mechanism (e.g., **CTR_DRBG** ), and the cryptographic primitives used (e.g., AES-128 or SHA-256). 

- Document the security strengths supported by the implementation. 

62 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

- Document features supported by the implementation (e.g., prediction resistance, personalization string, additional input, etc.). 

- If DRBG mechanism functions are distributed, specify the mechanisms that are used to protect the confidentiality and integrity of the internal state or parts of the internal state that are transferred between the distributed DRBG mechanism sub-boundaries (i.e., provide documentation about the secure channel). 

- In the case of the **CTR_DRBG** , indicate whether a derivation function is provided. If a derivation function is not used, document that the implementation can only be used when full entropy input is available. 

- Document any support functions other than health testing. 

- If periodic testing is performed for the generate function, document the intervals and provide a justification for the selected intervals (see <u>Section 11.3.3).</u> 

- Document whether the DRBG functions can be tested on demand. 

- Document how the integrity of the health tests will be determined subsequent to implementation validation testing. 

#### **11.2 Implementation Validation Testing** 

A DRBG mechanism **shall** be tested for conformance to this Recommendation. A DRBG mechanism **shall** be designed to be tested to ensure that the product is correctly implemented. A testing interface **shall** be available for this purpose in order to allow the insertion of input and the extraction of output for testing. 

Implementations to be validated **shall** include the following: 

- The documentation specified in <u>Section 11.1.</u> 

- Any documentation or results required in derived test requirements. 

All DRBG functions included in an implementation **shall** be tested, including the health test functionality. The error handling of all implemented DRBG functions will be tested. See Section <u>11.4</u> for expected error handling behavior. 

Note that when the uninstantiate function is tested, testing **shall** demonstrate that the internal state has been zeroized. 

#### **11.3 Health Testing** 

A DRBG implementation **shall** perform self-tests to obtain assurance that the DRBG continues to operate as designed and implemented (health testing).  The testing function(s) within a DRBG mechanism boundary (or sub-boundary) **shall** test each DRBG mechanism function within that boundary (or sub-boundary), with the possible exception of the health test function itself. A DRBG implementation may optionally perform other self-tests for DRBG functionality in addition to the tests specified in this Recommendation. 

63 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

The testing of the error handling capability is not required during the conduct of health tests. However, errors encountered during health testing **shall** be handled as discussed in <u>Section 11.4.2.</u> 

All data output from the DRBG mechanism boundary (or sub-boundary) **shall** be inhibited while these tests are performed. The results from known-answer-tests (see <u>Section 11.3.1)</u> **shall not** be output as random bits during normal operation. 

#### **11.3.2 Testing the Instantiate Function** 

Known-answer tests on the instantiate function **shall** use a security strength that will be available during normal operations. If prediction resistance has been implemented, the 

_prediction_resistance_flag_ **shall** also be used. A representative fixed value and length of the _entropy_input_ , _nonce_ and _personalization_string_ (if supported) **shall** be used; the value of the _entropy_input_ used during testing **shall not** be intentionally reused during normal operations (either by the instantiate or the reseed functions). 

If the values used during the test produce the expected results, then the instantiate function may be used during normal operation. 

An implementation **should** provide a capability to test the instantiate function on demand. 

#### **11.3.3 Testing the Generate Function** 

During generate-function testing, a representative fixed value and length for the _requested_number_of_bits_ and _additional_input_ (if supported) **shall** be used. If prediction resistance is supported, then the use of the _prediction_resistance_request_ parameter **shall** be tested. 

If the values used during the test produce the expected results, then the generate function may be used during normal operation. 

Bits generated during health testing **shall not** be output as pseudorandom bits. 

An implementation **should** provide a capability to test the generate function on demand. 

64 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

In addition to testing the generate function before first use (see <u>Section 11.3.1), known-answer</u> tests **should** be performed at reasonable intervals, as defined by the implementer. 

#### **11.3.4 Testing the Reseed Function** 

Known-answer testing of the reseed function **shall** use the _security_strength_ in the internal state of the (testing) instantiation to be reseeded. A representative value of the _entropy_input_ and _additional_input_ (if supported) **shall** be used (see Sections 8.3 and 10). If prediction resistance for the reseed function is supported, then the use of the _prediction_resistance_request_ parameter **shall** be tested. 

If the values used during the test produce the expected results, then the reseed function may be used during normal operation. 

An implementation **should** provide a capability to test the reseed function on demand. 

#### **11.3.5 Testing the Uninstantiate Function** 

Testing of the uninstantiate function is not required during health testing. 

#### **11.4 Error Handling** 

The expected errors are indicated for each DRBG mechanism function (see Sections 9.1 through <u>9.4) and for the derivation functions in Section 10.3. The error handling routines</u> **should** indicate the type of error. 

#### **11.4.1 Errors Encountered During Normal Operation** 

Many errors that occur during normal operation may be caused by a consuming application’s improper DRBG request or possibly the current unavailability of entropy; these errors are indicated by “ERROR_FLAG **”** in the pseudocode. In these cases, the consuming application user is responsible for correcting the request within the limits of the user’s organizational security policy. For example, if a failure indicating an invalid requested security strength is returned, a security strength higher than the DRBG or the DRBG instantiation can support has been requested. The user may reduce the requested security strength if the organization’s security policy allows the information to be protected using a lower security strength, or the user **shall** use an appropriately instantiated DRBG. 

Catastrophic errors (i.e., errors indicated by the **CATASTROPHIC_ERROR_FLAG** in the pseudocode) detected during normal operation **shall** be treated in the same manner as an error detected during health testing (see Section 11.4.2). 

#### **11.4.2 Errors Encountered During Health Testing** 

Errors detected during health testing **shall** be perceived as catastrophic DRBG failures. 

When a DRBG fails a health test or a catastrophic error is detected during normal operation, the DRBG **shall** enter an error state and output an error indicator. The DRBG **shall not** perform any instantiate, generate or reseed operations while in the error state, and pseudorandom bits **shall not** be output when an error state exists. When in an error state, user intervention (e.g., power 

65 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

cycling of the DRBG) **shall** be required to exit the error state, and the DRBG **shall** be reinstantiated before the DRBG can be used to produce pseudorandom bits. Examples of such errors include: 

- A test deliberately inserts an error, and the error is not detected, or 

- A result is returned from the instantiate, reseed or generate function that was not expected. 

66 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **Appendix A: (Normative) Conversion and Auxiliary Routines** 

#### **A.1 Bitstring to an Integer** 

**Bitstring_to_integer (** _b_ 1 _, b_ 2 _,…, bn_ ): 

**Input:** 

1. _b_ 1 _, b_ 2 _,…, bn_ The bitstring to be converted. 

**Output:** 

1. _x_ The requested integer representation of the bitstring. 

**Process:** 

1. Let ( _b_ 1 _, b_ 2 _,…, bn_ ) be the bits of a bitstring from leftmost to rightmost (i.e., most significant to least significant). 

In this Recommendation, the binary length of an integer _x_ is defined as the smallest integer _n_ satisfying _x_ < 2<sup>_n_</sup> . 

#### **A.2 Integer to a Bitstring** 

**Integer_to_bitstring (** _x_ **):** 

**Input:** 

1. _x_ The non-negative integer to be converted. 

**Output:** 

1. _b_ 1, _b_ 2, ..., _bn_ The bitstring representation of the integer _x_ . 

**Process:** 

1. Let ( _b_ 1, _b_ 2, ..., _bn_ ) represent the bitstring, where _b_ 1 = 0 or 1, and _b_ 1 is the most significant bit, while _bn_ is the least significant bit. 

2. For any integer _n_ that satisfies _x_ < 2<sup>_n_</sup> , the bits _bi_ **shall** satisfy: 

3. Return ( _b_ 1, _b_ 2, ..., _bn_ ). 

In this Recommendation, the binary length of the integer _x_ is defined as the smallest integer _n_ that satisfies _x_ < 2<sup>_n_</sup> . 

67 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **A.3 Integer to a Byte String** 

**Integer_to_byte_string (** _x_ **):** 

#### **Input:** 

1. A non-negative integer _x_ , and the intended length _n_ of the byte string satisfying _2_<sup>_8n_</sup> _> x._ 

**Output:** 

1. A byte string _B_ of length _n_ bytes. 

**Process:** 

1. Let _B1, B2,…, Bn_ be the bytes of _B_ from leftmost to rightmost. 

2. The bytes of _B_ **shall** satisfy: 

3. Return ( _B_ ). 

#### **A.4 Byte String to an Integer** 

**Byte_string_to_integer (** _B_ **):** 

**Input:** 

1. A byte string _B_ of length _n_ bytes. 

#### **Output:** 

1. A non-negative integer _x._ 

#### **Process:** 

1. Let _B1, B2, …, Bn_ be the bytes of _B_ from leftmost to rightmost. 

2. _x_ is defined as follows: 

3. Return ( _x_ ). 

#### **A.5 Converting Random Bits into a Random Number** 

In some cryptographic applications, sequences of random numbers are required ( _a_ 0, _a_ 1, _a_ 2,…), where: 

- i) Each integer _ai_ satisfies 0 ≤ _ai_ ≤ _r_ -1, for some positive integer _r_ (the _range_ of the random numbers); 

68 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

- ii) The equation _ai_ = _s_ holds, with probability almost exactly 1/ _r_ , for any _i_ ≥ 0 and for any _s_ (0 ≤ _s_ ≤ _r_ -1); 

iii) Each value _ai_ is statistically independent of any set of values _aj_ ( _j_ ≠ _i_ ). 

Four techniques are specified for generating sequences of random numbers from sequences of random bits. 

If the range of the number required is _a_ ≤ _ai_ ≤ _b_ , rather than 0 ≤ _ai_ ≤ _r-_ 1, then a random number in the desired range can be obtained by computing _ai + a_ , where _ai_ is a random number in the range 0 ≤ _ai_ ≤ _b-a_ (that is, when _r = b-a_ +1) _._ 

#### **A.5.1 The Simple Discard Method** 

Let _m_ be the number of bits needed to represent the value ( _r_ –1).  The following method may be used to generate the random number _a_ : 

1. Use the random bit generator to generate a sequence of _m_ random bits, ( _b_ 0, _b_ 1, …, _bm_ -1). 

2. Let _c_ = ∑2<sup>_i_</sup> _bi_ . 

3. If _c_ < _r_ then put _a_ = _c_ , else discard _c_ and go to Step 1. 

This method produces a random number _a_ with no skew (no bias).  A possible disadvantage of this method, in general, is that the time needed to generate such a random _a_ is not a fixed length of time because of the conditional loop. 

The ratio _r_ /2<sup>_m_</sup> is a measure of the efficiency of the technique, and this ratio will always satisfy 0.5 < _r_ /2<sup>_m_</sup> ≤ 1. If _r_ /2<sup>_m_</sup> is close to 1, then the above method is simple and efficient.  However, if _r_ /2<sup>_m_</sup> is close to 0.5, then the simple discard method is less efficient, and the more complex method below is recommended. 

#### **A.5.2 The Complex Discard Method** 

Choose a small positive integer _t_ (the number of same-size random number outputs desired), and then let _m_ be the number of bits in ( _r_<sup>_t_</sup> –1).  This method may be used to generate a sequence of _t_ random numbers ( _a_ 0, _a_ 1, … , _at_ -1): 

1. Use the random bit generator to generate a sequence of _m_ random bits, ( _b_ 0, _b_ 1, …, _bm_ -1). 

3. If _c_ < _r_<sup>_t_</sup> , then 

let ( _a_ 0, _a_ 1, …, _at_ -1) be the unique sequence of values satisfying 0 ≤ _ai_ ≤ _r -_ 1 such that 

else discard _c_ and go to Step 1. 

69 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

This method produces random numbers ( _a_ 0, _a_ 1, … , _at_ -1) with no skew.  A possible disadvantage of this method, in general, is that the time needed to generate these numbers is not a fixed length of time because of the conditional loop.  The complex discard method may have better overall performance than the simple discard method if many random numbers are needed. 

The ratio _r_<sup>_t_</sup> /2<sup>_m_</sup> is a measure of the efficiency of the technique, and this ratio will always satisfy 0.5 < _r_<sup>_t_</sup> /2<sup>_m_</sup> ≤ 1. Hence, given _r_ , it is recommended to choose _t_ so that _t_ is the smallest value such that _r_<sup>_t_</sup> /2<sup>_m_</sup> is close to 1.  For example, if _r_ = 3, then choosing _t_ = 3 means that _m_ = 5 (as _r_<sup>_t_</sup> is 27) and _r_<sup>_t_</sup> / _m_ = 27/32 ≈ 0.84, and choosing _t_ = 5 means that _m_ = 8 (as _r_<sup>_t_</sup> is 243) and _r_<sup>_t_</sup> / _m_ = 243/256 ≈ 0.95. The complex discard method coincides with the simple discard method when _t =_ 1. 

#### **A.5.3 The Simple Modular Method** 

Let _m_ be the number of bits needed to represent the value ( _r_ –1), and let _s_ be a security parameter. The following method may be used to generate one random number _a_ : 

1. Use the random bit generator to generate a sequence of _m+s_ random bits, _(b0, b1, …, bm+s-_ 1<sup>_)_.</sup> 

3. Let _a=c_ mod _r_ . 

The simple modular method can be coded to take constant time.  This method produces a random value with a negligible skew, that is, the probability that _ai=w_ for any particular value of _w_ (0 ≤ _w_ ≤ _r-_ 1) is not exactly 1 _/r_ . However, for a large enough value of _s,_ the difference between the probability that _ai=w_ for any particular value of _w_ and 1 _/r_ is negligible.  The value of _s_ **shall** be greater than or equal to 64. 

70 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **Appendix B: (Informative) Example Pseudocode for Each DRBG Mechanism** 

The internal states in these examples are considered to be an array of states, identified by _state_handle_ . A particular state is addressed as _internal_state_ ( _state_handle_ ), where the value of _state_handle_ begins at 0 and ends at _n_ -1, and _n_ is the number of internal states provided by an implementation. A particular element in the internal state is addressed by _internal_state_ ( _state_handle_ ). _element_ . In an empty internal state, all bitstrings are set to _Null_ , and all integers are set to 0. 

For each example in this appendix, arbitrary values have been selected that are consistent with the allowed values for each DRBG mechanism, as specified in the appropriate table in <u>Section 10.</u> 

The pseudocode in this appendix does not include the necessary conversions (e.g., integer to bitstring) for an implementation. When conversions are required, they **shall** be accomplished as specified in <u>Appendix A.</u> 

The following routine is defined for these pseudocode examples: 

**Find_state_space** (): A function that finds an unused internal state. The function returns a _status_ (either “Success” or a message indicating that an unused internal state is not available) and, if _status_ = “Success”, a _state_handle_ that points to an available _internal_state_ in the array of internal states. If _status_ ≠ “Success”, an invalid _state_handle_ is returned. 

When the uninstantantiate function is invoked in the following examples, the function specified in <u>Section 9.4 is called.</u> 

#### **B.1 Hash_DRBG Example** 

This example of **Hash_DRBG** uses the SHA-1 hash function, and prediction resistance is supported. Both a personalization string and additional input are supported. A 32-bit incrementing counter is used as the nonce for instantiation ( _instantiation_nonce_ ); the nonce is initialized when the DRBG is instantiated (e.g., by a call to the clock or by setting it to a fixed value) and is incremented for each instantiation. 

A total of ten internal states are provided (i.e., ten instantiations may be handled simultaneously). 

For this implementation, the functions and algorithms are “inline”, i.e., the algorithms are not called as separate routines from the function envelopes. Also, the **Get_entropy_input** function uses only three input parameters, since the first two parameters (as specified in Section 9) have the same value. 

The internal state contains values for _V_ , _C_ , _reseed_counter_ , _security_strength_ and 

_prediction_resistance_flag_ , where _V_ and C are bitstrings, and _reseed_counter_ , _security_strength_ and the _prediction_resistance_flag_ are integers. A requested prediction resistance capability is indicated when _prediction_resistance_flag_ = 1. 

In accordance with Table 2 in <u>Section 10.1, the 112- and 128-bit security strengths may be</u> instantiated. Using SHA-1, the following definitions are applicable for the instantiate, generate and reseed functions and algorithms: 

71 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

1. _highest_supported_security_strength_ = 128. 

2. Output block length ( _outlen_ ) = 160 bits. 

3. Required minimum entropy for instantiation and reseed = _security_strength_ . 

4. Seed length ( _seedlen_ ) = 440 bits. 

5. Maximum number of bits per request ( _max_number_of_bits_per_request_ ) = 5000 bits. 

6. Reseed interval ( _reseed_interval_ ) = 100 000 requests. 

7. Maximum length of the personalization string ( _max_personalization_string_length_ ) = 512 bits. 

8. Maximum length of additional_input ( _max_additional_input_string_length_ ) = 512 bits. 

9. Maximum length of entropy input ( _max _length_ ) = 1000 bits. 

#### **B.1.1 Instantiation of Hash_DRBG** 

This implementation will return a text message and an invalid state handle (-1) when an error is encountered. Note that the value of _instantiation_nonce_ is an internal value that is always available to the instantiate function. 

Note that this implementation does not check the _prediction_resistance_flag_ , since the implementation has been designed to support prediction resistance. However, if a consuming application actually wants prediction resistance, the implementation expects that 

_prediction_resistance_flag_ = 1 during instantiation; this will be used in the generate function in <u>Appendix B.1.3.</u> 

#### **Hash_DRBG_Instantiate_function:** 

**Input:** integer ( _requested_  instantiation_  security_strength_ , _prediction_resistance_flag_ ), bitstring _personalization_string_ . 

**Output:** string _status_ , integer _state_handle_ . 

#### **Process:** 

Comment: Check the input parameters. 

1. If ( _requested_instantiation_security_strength_ > 128), then **Return** (“Invalid _requested_instantiation_security_strength_ ”, -1). 

2. If ( **len** ( _personalization_string_ ) > 512), then **Return** (“ _Personalization_string_ too long”, -1). 

Comment: Set the _security_strength_ to one of the valid security strengths. 

3. If ( _requested_instantiation_security_strength_ ≤ 112), then _security_strength_ = 112 Else _security_strength_ = 128. 

Comment: Get the _entropy_input_ . 

72 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

4. ( _status_ , _entropy_input_ ) = **Get_entropy_input** ( _security_strength_ , 1000, _prediction_resistance_request_ ). 

5. If ( _status_ ≠ “Success”), then **Return** ( _status_ , -1). 

Comment: Increment the nonce; actual coding must ensure that it wraps when the storage limit is reached. 

6. _instantiation_nonce_ = _instantiation_nonce_ + 1. 

Comment: The instantiate algorithm is provided in steps 7 to 11. 

7. _seed_material_ = _entropy_input_ || _instantiation_nonce_ || _personalization_string_ . 

8. _seed_ = **Hash_df** ( _seed_material_ , 440). Comment: **Hash_df** is defined in <u>Section 10.3.1.</u> 

9. _V_ = _seed_ . 

10. _C_ = **Hash_df** ((0x00 || _V_ ), 440). 

11. _reseed_counter_ = 1. 

Comment: Find an unused internal state. 

12. ( _status_ , _state_handle_ ) = **Find_state_space** ( ). 

13. If ( _status_ ≠ “Success”), then **Return** ( _status_ , -1). 

- 14 _._ Save the internal state. 

   - 14.1 _internal_state_ ( _state_handle_ ). _V_ = _V._ 

   - 14.2 _internal_state_ ( _state_handle_ ). _C_ = _C_ . 

   - 14.3 _internal_state_ ( _state_handle_ ). _reseed_counter_ = _reseed_counter_ . 

   - 14.4 _internal_state_ ( _state_handle_ ). _security_strength = security_strength._ 

   - 14.5 _internal_state_ ( _state_handle_ ). _prediction_resistance_flag = prediction_resistance_flag._ 

15. **Return** (“Success”, _state_handle_ ). 

#### **B.1.2 Reseeding a Hash_DRBG Instantiation** 

The implementation is designed to return a text message as the _status_ when an error is encountered. 

#### **Hash_DRBG_Reseed_function:** 

**Input:** integer ( _state_handle, prediction_resistance_request_ ), bitstring _additional_input_ . 

**Output:** string _status_ . 

**Process:** 

Comment: Check the validity of the _state_handle_ . 

73 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number 

Generation Using Deterministic RBGs 

1. If (( _state_handle_ < 0) or ( _state_handle_ > 9) or ( _internal_  state_ ( _state_handle_ ) = { _Null_ , 

_Null_ , 0, 0, 0})), then **Return** (“State not available for the _state_handle_ ”). 

Comment: Get the internal state values needed to determine the new internal state. 

2. Get the appropriate _internal_  state_ values. 

_V_ = _internal_state_ ( _state_handle_ ) _.V_ . 

_security_strength = internal_state_ ( _state_handle_ ) _.security_strength_ . 

Check the length of the _additional_input_ . 

3. If ( **len** ( _additional_input_ ) > 512), then **Return** (“ _additional_input_ too long”). 

Comment: Get the _entropy_input_ . 

4. ( _status, entropy_input_ ) = **Get_entropy_input** ( _security_strength,_ 1000, _prediction_resistance_request_ ). 

5. If ( _status_ ≠ “Success”), then **Return** ( _status_ ). 

Comment: The reseed algorithm is provided in steps 6 to 10. 

6. _seed_material_ = 0x01 || _V_ || _entropy_input_ || _additional_input_ . 

7. _seed_ = **Hash_df** ( _seed_material_ , 440). 

8. _V_ = _seed_ . 

9. _C_ = **Hash_df** ((0x00 || _V_ ), 440) _._ 

10. _reseed_counter_ = 1. 

Comment: Update the _working_state_ portion of the internal state. 

   11. Update the appropriate _state_ values. 

      - 11.1 _internal_state_ ( _state_handle_ ) _.V_ = _V_ . 

      - 11.2 _internal__ state ( _state_handle_ ) _.C_ = _C_ . 

      - 11.3 _internal_ state_ ( _state_handle_ ). _reseed_counter_ = _reseed_counter_ . 

   12. **Return** (“Success”). 

- **B.1.3 Generating Pseudorandom Bits Using Hash_DRBG** 

The implementation returns a _Null_ string as the pseudorandom bits if an error has been detected. 

Prediction resistance is requested when _prediction_resistance_request_ = 1. 

In this implementation, prediction resistance is requested by supplying 

_prediction_resistance_request_ = 1 when the **Hash_DRBG** function is invoked. 

**Hash_DRBG_Generate_function:** 

74 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

- **Input:** integer ( _state_handle_ , _requested_  no_of_bits_ , _requested_security_strength_ , _prediction_resistance_request_ ), bitstring _additional_input._ 

**Output:** string _status_ , bitstring _pseudorandom_bits_ . 

**Process:** 

Comment: Check the validity of the _state_handle_ . 

1. If (( _state_handle_ < 0) or ( _state_handle_ > 9) or ( _state_ ( _state_handle_ ) = { _Null_ , _Null_ , 0, 0, 0})), then **Return** (“State not available for the _state_handle_ ”, _Null_ ). 

2. Get the internal state values. 

   - 2.1 _V_ = _internal_state_ ( _state_handle_ ) _.V_ . 

   - 2.2 _C_ = _internal_state_ ( _state_handle_ ) _.C_ . 

   - 2.3 _reseed_counter_ = _internal_state_ ( _state_handle_ ) _.reseed_counter_ . 

   - 2.4 _security_strength_ = _internal_state_ ( _state_handle_ ) _.security_strength_ . 

   - 2.5 _prediction_resistance_flag = internal_state_ ( _state_handle_ ) _.prediction_resistance_flag_ . 

Comment: Check the validity of the other input parameters. 

3. If ( _requested_no_of_bits_ > 5000) then **Return** (“Too many bits requested”, _Null_ ). 

4. If ( _requested_security_strength_ > _security_strength_ ), then **Return** (“Invalid _requested_security_strength_ ”, _Null_ ). 

5. If ( **len** ( _additional_input_ ) > 512), then **Return** (“ _additional_input_ too long”, _Null_ ). 

6. If (( _reseed_counter_ > 100 000) or ( _prediction_resistance_request_ = 1)), then 6.1 _status_ = **Hash_DRBG_Reseed_ function** ( _state_handle, prediction_resistance_request, additional_input_ ). 

   - 6.2 If ( _status_ ≠ “Success”), then **Return** ( _status_ , _Null_ ). 

   - 6.3 Get the new internal state values that have changed. 

      - 7.3.1 _V_ = _internal_state_ ( _state_handle_ ) _.V_ . 

      - 7.3.2 _C_ = _internal_state_ ( _state_handle_ ) _.C_ . 

      - 7.3.3 _reseed_counter_ = _internal_state_ ( _state_handle_ ) _.reseed_counter_ . 

   - 6.4 _additional_input_ = _Null_ . 

Comment: Steps 7 to 15 provide the rest of the generate algorithm. Note that in this implementation, the **Hashgen** routine specified in <u>Section 10.1.1.4</u> is provided inline as steps 8 to 12. 

7. If ( _additional_input_ ≠ _Null_ ), then do 

   - 7.1 _w_ = **Hash** (0x02 || _V_ || _additional_input_ ). 

75 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

9. _data_ = _V._ 

10. _W_ = the _Null_ string. 

11. For _i_ = 1 to _m_ 

11.1 _w_ = **Hash** ( _data_ ). 

11.2 _W_ = _W_ || _w._ 

11.3 _data_ = ( _data_ + 1) mod 2<sup>440</sup> . 

12. _pseudorandom_bits_ = **leftmost** ( _W_ , _requested_no_of_bits_ ) _._ 

13. _H_ = **Hash** (0x03 || _V_ ). 

14. _V_ = ( _V_ + _H_ + _C_ + _reseed_counter_ ) mod 2<sup>440</sup> _._ 

15. _reseed_counter_ = _reseed_counter_ + 1. 

Comments: Update the _working_state_ . 

16. Update the changed values in the _state._ 

   - 16.1 _internal_state_ ( _state_handle_ ) _.V = V._ 

   - 16.2 _internal_state_ ( _state_handle_ ) _.reseed_counter = reseed_counter._ 

17. **Return** (“Success”, _pseudorandom_bits_ ). 

#### **B.2 HMAC_DRBG Example** 

This example of **HMAC_DRBG** uses the SHA-256 hash function. Reseeding and prediction resistance are not supported. The nonce for instantiation consists of a random value with _security_strength_ /2 bits of entropy; the nonce is obtained by increasing the call for entropy bits via the **Get_entropy_input** call by _security_strength_ /2 bits (i.e., by adding _security_strength_ /2 bits to the _security_strength_ value). The **HMAC_DRBG_Update** function is specified in Section <u>10.1.2.2.</u> 

A personalization string is supported, but additional input is not. A total of three internal states are provided. For this implementation, the functions and algorithms are written as separate routines. Also, the **Get_entropy_input** function uses only two input parameters, since the first two parameters (as specified in <u>Section 9) have the same value, and prediction resistance is not</u> available. 

The internal state contains the values for _V_ , _Key_ , _reseed_counter_ , and _security_strength_ , where _V_ and _C_ are bitstrings, and _reseed_counter_ and _security_strength_ are integers. 

In accordance with Table 2 in <u>Section 10.1, security strengths of 112, 128, 192 and 256 bits may</u> be instantiated. Using SHA-256, the following definitions are applicable for the instantiate and generate functions and algorithms: 

76 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

1. _highest_supported_security_strength_ = 256. 

2. Output block ( _outlen_ ) = 256 bits. 

3. Required minimum entropy for the entropy input at instantiation = (3/2) _security_strength_ (this includes the entropy required for the nonce). 

4. Seed length ( _seedlen_ ) = 440 bits. 

5. Maximum number of bits per request ( _max_number_of_bits_per_request_ ) = 7500 bits. 

6. Reseed_interval ( _reseed_ interval_ ) = 10 000 requests. 

7. Maximum length of the personalization string ( _max_personalization_string_length_ ) = 160 bits. 

8. Maximum length of the entropy input ( _max _length_ ) = 1000 bits. 

#### **B.2.1 Instantiation of HMAC_DRBG** 

− This implementation will return a text message and an invalid state handle ( 1) when an error is encountered. 

#### **HMAC_DRBG_Instantiate_function:** 

**Input:** integer ( _requested_instantiation_security_strength_ ), bitstring _personalization_string_ . **Output:** string _status,_ integer _state_handle_ . 

#### **Process:** 

Check the validity of the input parameters. 

1. If ( _requested_instantiation_security_strength_ > 256), then **Return** (“Invalid − 

_requested_instantiation_security_strength_ ”, 1). 

2. If ( **len** ( _personalization_string_ ) > 160), then **Return** (“ _Personalization_string_ too − 

long”, 1) 

Comment: Set the _security_strength_ to one of the valid security strengths. 

3. If ( _requested_security_strength_ ≤ 112), then _security_strength_ = 112 Else if ( _requested_ security_strength_ ≤ 128), then _security_strength_ = 128 Else if ( _requested_ security_strength_ ≤ 192), then _security_strength_ = 192 Else _security_strength_ = 256. 

Comment: Get the _entropy_input and the nonce_ . 

4. _min_entropy_ = 1.5 × _security_strength_ . 

5. ( _status_ , _entropy_input_ ) = **Get_entropy_input** ( _min_entropy_ , 1000). 

6. If ( _status_ ≠ “Success”), then **Return** ( _status_ , −1). 

77 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

Comment: Invoke the instantiate algorithm. Note that the _entropy_input_ contains the nonce. 

7. ( _V_ , _Key_ , _reseed_counter_ ) = **HMAC_DRBG_Instantiate_algorithm** ( _entropy_input_ , _personalization_string_ ). 

Comment: Find an unused internal state. 

8. ( _status_ , _state_handle_ ) = **Find_state_space** ( ). 

9. If ( _status_ ≠ “Success”), then **Return** ( _status_ , −1). 

10. Save the initial state. 

   - 10.1 _internal_state_ ( _state_handle_ ) _.V_ = _V._ 

   - 10.2 _internal_state_ ( _state_handle_ ) _. Key = Key._ 

   - 10.3 _internal_state_ ( _state_handle_ ) _. reseed_counter_ = _reseed_counter_ . 

   - 10.4 _internal_state_ ( _state_handle_ ) _.security_strength_ = _security_strength_ . 

11. Return (“Success” and _state_handle_ ). 

#### **HMAC_DRBG_Instantiate_algorithm** : 

**Input:** bitstring ( _entropy_input_ , _personalization_string_ ). 

**Output:** bitstring ( _V_ , _Key_ ), integer _reseed_counter_ . 

#### **Process:** 

1. _seed_material_ = _entropy_input_ || _personalization_string_ . 

2. Set _Key_ to _outlen_ bits of zeros. 

3. Set _V_ to _outlen_ /8 bytes of 0x01. 

4. ( _Key_ , _V_ ) = **HMAC_DRBG_Update** ( _seed_material_ , _Key_ , _V_ ). 

5. _reseed_counter_ = 1. 

6. **Return** ( _V_ , _Key_ , _reseed_counter_ ). 

#### **B.2.2 Generating Pseudorandom Bits Using HMAC_DRBG** 

The implementation returns a _Null_ string as the pseudorandom bits if an error has been detected. 

#### **HMAC_DRBG_Generate_function:** 

**Input:** integer ( _state_handle_ , _requested_no_of_bits_ , _requested_security_strength_ ). 

**Output:** string ( _status_ ), bitstring _pseudorandom_bits_ . 

#### **Process:** 

Comment: Check for a valid state handle. 

1. If (( _state_handle_ < 0) or ( _state_handle_ > 2) or ( _internal_state_ ( _state_handle_ ) = { _Null_ , _Null_ , 0, 0}), then **Return** (“State not available for the indicated _state_handle_ ”, _Null_ ). 

2. Get the internal state. 

78 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

- 2.1 _V_ = _internal_state_ ( _state_handle_ ). _V_ . 

- 2.2 _Key_ = _internal_state_ ( _state_handle_ ). _Key_ . 

- 2.3 _security_strength = internal_state_ ( _state_handle_ ) _.security_strength._ 

- 2 _._ 4 _reseed_counter = internal_state (state_handle).reseed_counter._ 

Comment: Check the validity of the rest of the input parameters. 

3. If ( _requested_no_of_bits_ > 7500), then **Return** (“Too many bits requested”, _Null_ ). 

4. If ( _requested_security_strength_ > _security_strength_ ), then **Return** (“Invalid _requested_security_strength_ ”, _Null_ ). 

Comment: Invoke the generate algorithm. 

5. ( _status_ , _pseudorandom_bits_ , _V_ , _Key_ , _reseed_counter_ ) = 

   - **HMAC_DRBG_Generate_algorithm** ( _V_ , _Key_ , _reseed_counter_ , _requested_number_of_bits_ ). 

6. If ( _status_ = “Reseed required”), then **Return** (“DRBG can no longer be used. A new instantiation is required”, _Null_ ). 

7. Update the changed state values. 

   - 7.1 _internal_state_ ( _state_handle_ ). _V_ = _V_ . 

   - 7.2 _internal_state_ ( _state_handle_ ). _Key = Key._ 

   - 7.3 _internal_state_ ( _state_handle_ ). _reseed_counter_ = _reseed_counter_ . 

8. **Return** (“Success”, _pseudorandom_bits_ ). 

#### **HMAC_DRBG_Generate_algorithm** : 

**Input** : bitstring ( _V, Key_ ), integer ( _reseed_counter_ , _requested_number_of_bits_ ). 

**Output** : string _status_ , bitstring ( _pseudorandom_bits_ , _V_ , _Key_ ), integer _reseed_counter_ . 

**Process** : 

- 1 If ( _reseed_counter_ ≥ 10 000), then **Return** (“Reseed required”, _Null, V, Key, reseed_counter_ ). 

2. _temp_ = _Null_ . 

- 3 While ( **len** ( _temp_ ) < _requested_no_of_bits_ ) do: 

   - 3.1 _V_ = **HMAC** ( _Key_ , _V_ ). 

   - 3.2 _temp_ = _temp_ || _V_ . 

4. _pseudorandom_bits_ = **leftmost** ( _temp_ , _requested_no_of_bits_ ). 

5. ( _Key_ , _V_ ) = **HMAC_DRBG_Update** ( _Null_ , _Key_ , _V_ ). 

6. _reseed_counter_ = _reseed_counter_ + 1. 

7. **Return** (“Success”, _pseudorandom_bits_ , _V_ , _Key_ , _reseed_counter_ ). 

79 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **B.3 CTR_DRBG Example Using a Derivation Function** 

This example of **CTR_DRBG** uses AES-128 and uses the entire input block as the counter field. The reseed and prediction resistance capabilities are supported, and prediction resistance is obtained during every **Get_entropy_input** call and reseed request. Although the _prediction_resistance_request_ parameter in the **Get_entropy_input** and reseed request could be omitted, in this case, they are shown in the pseudocode as a reminder that prediction_resistance will be performed. A block cipher derivation function using AES-128 is used, and a 

personalization string and additional input are supported. A total of five internal states are available. For this implementation, the functions and algorithms are written as separate routines. **AES_ECB_Encrypt** is the **Block_Encrypt** function (specified in Section 10.3.3) that uses AES128 in the ECB mode. 

The nonce for instantiation ( _instantiation_nonce_ ) consists of a 32-bit incrementing counter. The nonce is initialized when the DRBG is instantiated (e.g., by a call to the clock or by setting it to a fixed value) and is incremented for each instantiation. 

The internal state contains the values for _V_ , _Key_ , _reseed_counter_ , and _security_strength_ , where _V_ and _Key_ are bitstrings, and all other values are integers. Since prediction resistance is known to be supported, there is no need for _prediction_resistance_flag_ in the internal state. 

In accordance with Table 3 in <u>Section 10.2.1, security strengths of 112 and 128 bits may be</u> supported. Using AES-128, the following definitions are applicable for the instantiate, reseed and generate functions: 

1. _highest_supported_security_strength_ = 128. 

2. Input/output block length ( _blocklen_ ) = 128 bits. 

3. Key length ( _keylen_ ) = 128 bits. 

4. Required minimum entropy for the entropy input during instantiation and reseeding = _security_strength._ 

5. Minimum entropy input length ( _min _length_ ) = _security_strength_ bits. 

6. Maximum entropy input length ( _max _length_ ) = 1000 bits. 

7. Maximum personalization string input length ( _max_personalization_string_input_length_ ) = 800 bits. 

8. Maximum additional input length ( _max_additional_input_length_ ) = 800 bits. 

9. Seed length ( _seedlen_ ) = 256 bits. 

10. Maximum number of bits per request ( _max_number_of_bits_per_request_ ) = 4000 bits. 

11. Reseed interval ( _reseed_interval_ ) = 100 000 requests. 

#### **B.3.1 The CTR_DRBG_Update Function** 

#### **CTR_DRBG_Update:** 

**Input:** bitstring ( _provided_data_ , _Key_ , _V_ ). 

**Output:** bitstring ( _Key_ , _V_ ). 

80 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **Process:** 

1. _temp = Null._ 

2. While ( **len** ( _temp_ ) < 256) do 

   - 2.1 _V_ = ( _V_ + 1) mod 2<sup>128</sup> . 

   - 2.2 _output_block_ = **AES_ECB_Encrypt** ( _Key_ , _V_ ). 

   - 2.3 _temp_ = _temp_ || _output_block_ . 

3. _temp_ = **leftmost** ( _temp_ , 256). 

- 4 _temp_ = _temp_ ⊕ _provided_data_ . 

5. _Key =_ **leftmost** ( _temp_ , 128) _._ 

6. _V_ = **rightmost** ( _temp_ , 128) _._ 

7. **Return** ( _Key_ , _V_ ). 

#### **B.3.2 Instantiation of CTR_DRBG Using a Derivation Function** 

− This implementation will return a text message and an invalid state handle ( 1) when an error is encountered. **Block_Cipher_df** is the derivation function in <u>Section 10.3.2, and uses AES-128 in</u> the ECB mode as the **Block_Encrypt** function. 

Note that this implementation does not include the _prediction_resistance_flag_ in the input parameters, nor save it in the internal state, since prediction resistance is known to be supported. 

#### **CTR_DRBG_Instantiate_function** : 

**Input:** integer ( _requested_instantiation_security_strength_ ), bitstring _personalization_string_ . 

**Output:** string _status,_ integer _state_handle_ . 

#### **Process:** 

Comment: Check the validity of the input parameters. 

1. If ( _requested_instantiation_security_strength_ > 128) then **Return** (“Invalid − 

_requested_instantiation_security_strength_ ”, 1). 

2. If ( **len** ( _personalization_string_ ) > 800), then **Return** (“ _Personalization_string_ too − 

long”, 1). 

3. If ( _requested_instantiation_security_strength_ ≤ 112), then _security_strength_ = 112 Else _security_strength_ = 128. 

Comment: Get the entropy input. 

4. ( _status_ , _entropy_input_ ) = **Get_entropy_input** ( _security_strength_ , _security_strength_ , 1000, _prediction_resistance_request_ ). 

5. If ( _status_ ≠ “Success”), then **Return** ( _status_ , −1). 

81 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

Comment: Increment the nonce; actual coding must ensure that the nonce wraps when its storage limit is reached, and that the counter pertains to all instantiations, not just this one. 

6. _instantiation_nonce_ = _instantiation_nonce_ + 1. 

Comment: Invoke the instantiate algorithm. 

7. ( _V_ , _Key_ , _reseed_counter_ ) = **CTR_DRBG_Instantiate_algorithm** ( _entropy_input_ , _instantiation_nonce_ , _personalization_string_ ). 

Comment: Find an available internal state and save the initial values. 

8. ( _status_ , _state_handle_ ) = **Find_state_space** ( ). 

9. If ( _status_ ≠ “Success”), then **Return** ( _status_ , −1). 

10. Save the internal state. 

   - 10.1 _internal_state__ ( _state_handle_ ).V = _V_ . 

   - 10.2 _internal_state__ ( _state_handle_ ). _Key = Key._ 

   - 10.3 _internal_state__ ( _state_handle_ ). _reseed_counter_ = _reseed_counter_ . 

   - 10.4 _internal_state__ ( _state_handle_ ). _security_strength_ = _security_strength_ . 

11. **Return** (“Success”, _state_handle_ ). 

#### **CTR_DRBG_Instantiate_algorithm:** 

**Input** : bitstring ( _entropy_input_ , _nonce_ , _personalization_string_ ). 

**Output** : bitstring ( _V_ , _Key_ ), integer ( _reseed_counter_ ). 

#### **Process** : 

1. _seed_material_ = _entropy_input_ || _nonce_ || _personalization_string_ . 

2. _seed_material_ = **Block_Cipher_df** ( _seed_material_ , 256). 3. _Key_ = 0<sup>128</sup> . Comment: 128 bits. 4. _V_ = 0<sup>128</sup> . Comment: 128 bits. 

5. ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _seed_material_ , _Key_ , _V_ ). 

6. _reseed_counter_ = 1. 

7. **Return** ( _V_ , _Key_ , _reseed_counter_ ). 

#### **B.3.3 Reseeding a CTR_DRBG Instantiation Using a Derivation Function** 

The implementation is designed to return a text message as the _status_ when an error is encountered. 

#### **CTR_DRBG_Reseed_function:** 

82 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Input:** integer ( _state_handle_ ), integer _prediction_resistance_request_ , bitstring _additional_input_ . 

**Output:** string _status_ . 

**Process:** 

Comment: Check for the validity of _state_handle_ . 

1. If (( _state_handle_ < 0) or ( _state_handle_ > 4) or ( _internal_state_ ( _state_handle_ ) = { _Null_ , _Null_ , 0, 0}), then **Return** (“State not available for the indicated _state_handle_ ”). 

2. Get the internal state values. 

   - 2.1 _V_ = _internal_state_ ( _state_handle_ ). _V_ . 

   - 2.2 _Key_ = _internal_state_ ( _state_handle_ ). _Key._ 

   - 2 _._ 3 _security_strength = internal_state_ ( _state_handle_ ) _.security_strength._ 

3. If ( **len** ( _additional_input_ ) > 800), then **Return** (“ _additional_input_ too long”). 

4. ( _status_ , _entropy_input_ ) = **Get_entropy_input** ( _security_strength_ , _security_strength_ , 1000, _prediction_resistance_request_ ). 

6. If ( _status_ ≠ “Success”), then **Return** ( _status_ ). 

Comment: Invoke the reseed algorithm. 

7. ( _V_ , _Key_ , _reseed_counter_ ) = **CTR_DRBG_Reseed_algorithm** ( _V_ , _Key_ , _reseed_counter_ , _entropy_input_ , _additional_input_ ). 

8. Save the internal state. 

   - 8.1 _internal_state_ ( _state_handle_ ). _V_ = _V_ . 

   - 8.2 _internal_state_ ( _state_handle_ ). _Key = Key._ 

   - 8.3 _internal_state_ ( _state_handle_ ). _reseed_counter = reseed_counter._ 

   - 8.4 _internal_state_ ( _state_handle_ ). _security_strength_ = _security_strength_ . 

9. **Return** (“Success”). 

#### **CTR_DRBG_Reseed_algorithm:** 

- **Input** : bitstring ( _V_ , _Key_ ), integer ( _reseed_counter_ ), bitstring ( _entropy_input_ , _additional_input_ ) _._ 

**Output:** bitstring ( _V_ , _Key_ ), integer ( _reseed_counter_ ). 

#### **Process:** 

1. _seed_material_ = _entropy_input_ || _additional_input._ 

2. _seed_material_ = **Block_Cipher_df** ( _seed_material_ , 256). 

3. ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _seed_material_ , _Key_ , _V_ ). 

4. _reseed_counter_ = 1. 

5. **Return** ( _V_ , _Key_ , _reseed_counter_ ). 

83 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **B.3.4 Generating Pseudorandom Bits Using CTR_DRBG** 

The implementation returns a _Null_ string as the pseudorandom bits if an error has been detected. **CTR_DRBG_Generate_function:** 

- **Input:** integer ( _state_handle_ , _requested_no_of_bits_ , _requested_security_strength_ , _prediction_resistance_request_ ), bitstring _additional_input_ . 

**Output:** string _status_ , bitstring _pseudorandom_bits_ . 

**Process:** 

Comment: Check the validity of _state_handle_ . 

1. If (( _state_handle_ < 0) or ( _state_handle_ > 4) or ( _internal_state_ ( _state_handle_ ) = { _Null_ , _Null_ , 0, 0}), then **Return** (“State not available for the indicated _state_handle_ ”, _Null_ ). 

2. Get the internal state. 

   - 2.1 _V_ = _internal_state_ ( _state_handle_ ). _V_ . 

   - 2.2 _Key_ = _internal_state_ ( _state_handle_ ). _Key._ 

   - 2.3 _security_strength = internal_state_ ( _state_handle_ ) _.security_strength._ 

   - 2.4 _reseed_counter = internal_state (state_handle).reseed_counter_ . 

Comment: Check the rest of the input parameters. 

3. If ( _requested_no_of_bits_ > 4000), then **Return** (“Too many bits requested”, _Null_ ). 

4. If ( _requested_security_strength_ > _security_strength_ ), then **Return** (“Invalid _requested_security_strength_ ”, _Null_ ). 

5. If ( **len** ( _additional_input_ ) > 800), then **Return** (“ _additional_input_ too long”, _Null_ ). 

6. _reseed_required_flag_ = 0. 

7. If (( _reseed_required_flag_ = 1) OR ( _prediction_resistance_flag_ = 1)), then 

   - 7.1 _status_ = **CTR_DRBG_Reseed_function** ( _state_handle_ , _prediction_resistance_request_ , _additional_input_ ). 

   - 7.2 If ( _status_ ≠ “Success”), then **Return** ( _status_ , _Null_ ). 

   - 7.3 Get the new working state values; the administrative information was not affected. 

      - 7.3.1 _V_ = _internal_state_ ( _state_handle_ ). _V_ . 

      - 7.3.2 _Key_ = _internal_state_ ( _state_handle_ ). _Key._ 

      - 7 _._ 3.3 _reseed_counter = internal_state (state_handle).reseed_counter_ . 

   - 7.4 _additional_input_ = _Null_ . 

   - 7.5 _reseed_required_flag_ = 0. 

Comment: Generate bits using the generate algorithm. 

84 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

8. ( _status_ , _pseudorandom_bits, V, Key, reseed_counter_ ) = **CTR_DRBG_Generate_algorithm** ( _V_ , _Key_ , _reseed_counter_ , _requested_number_of_bits_ , _additional_input_ ). 

9. If ( _status_ = “Reseed required”), then 

   - 9.1 _reseed_required_flag_ = 1. 

   - 9.2 Go to step 7. 

10. Update the internal state. 

   - 10.1 _internal_state_ ( _state_handle_ ). _V_ = _V_ . 

   - 10.2 _internal_state_ ( _state_handle_ ). _Key = Key._ 

   - 10.3 _internal_state_ ( _state_handle_ ). _reseed_counter = reseed_counter._ 

   - 10.4 _internal_state_ ( _state_handle_ ). _security_strength_ = _security_strength_ . 

11. **Return** (“Success”, _pseudorandom_bits_ ). 

#### **CTR_DRBG_Generate_algorithm:** 

**Input:** bitstring ( _V_ , _Key_ ), integer ( _reseed_counter_ , _requested_number_of_bits_ ) bitstring _additional_input_ . 

**Output:** string _status_ , bitstring ( _returned_bits_ , _V_ , _Key_ ), integer _reseed_counter_ . 

**Process:** 

1. If ( _reseed_counter_ > 100 000), then **Return** (“Reseed required”, _Null_ , _V_ , _Key_ , _reseed_counter_ ). 

2. If ( _additional_input_ ≠ _Null_ ), then 

      - 2.1 _additional_input_ = **Block_Cipher_df** ( _additional_input_ , 256). 

   - 2.2 ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _additional_input_ , _Key_ , _V_ ). 

   - Else _additional_input_ = 0<sup>256</sup> . 

3. _temp_ = _Null_ . 

4. While ( **len** ( _temp_ ) < _requested_number_of_bits_ ) do: 

   - 4.1 _V_ = ( _V_ + 1) mod 2<sup>128</sup> . 

   - 4.2 _output_block_ = **AES_ECB_Encrypt** ( _Key_ , _V_ ). 

   - 4.3 _temp_ = _temp_ || _output_block_ . 

5. _returned_bits_ = **leftmost** ( _temp_ , _requested_number_of_bits_ ) 

6. ( _Key_ , _V_ ) = **CTR_DRBG_Update** ( _additional_input_ , _Key_ , _V_ ) 

7. _reseed_counter_ = _reseed_counter_ + 1. 

8. **Return** (“Success”, _returned_bits_ , _V_ , _Key_ , _reseed_counter_ ). 

85 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

#### **B.4 CTR_DRBG Example Without a Derivation Function** 

This example of **CTR_DRBG** is the same as the previous example except that a derivation function is not used (i.e., full entropy is always available). As in <u>Appendix B.3, the</u> **CTR_DRBG** uses AES-128. The reseed and prediction resistance capabilities are available. Both a personalization string and additional input are supported. A total of five internal states are available. For this implementation, the functions and algorithms are written as separate routines. **AES_ECB_Encrypt** is the **Block_Encrypt** function (specified in Section 10.3.3) that uses AES128 in the ECB mode. 

The internal state contains the values for _V_ , _Key_ , _reseed_counter_ , and _security_strength_ , where _V_ and _Key_ are strings, and all other values are integers. Since prediction resistance is known to be supported, there is no need for _prediction_resistance_flag_ in the internal state. 

In accordance with Table 3 in <u>Section 10.2.1, security strengths of 112 and 128 bits may be</u> supported. The definitions are the same as those provided in <u>Appendix B.3, except that to be</u> compliant with Table 3, the maximum size of the _personalization_string_ is 256 bits. In addition, the maximum size of any _additional_input_ is 256 bits (i.e., **len** ( _additional_input_ ≤ _seedlen_ )). 

#### **B.4.1 The CTR_DRBG_Update Function** 

The update function is the same as that provided in <u>Appendix B.3.1.</u> 

#### **B.4.2 Instantiation of CTR_DRBG Without a Derivation Function** 

The instantiate function ( **CTR_DRBG_Instantiate_function** ) is the same as that provided in Appendix B.3.2, except for the following: 

- Step 2 is replaced by: 

   - If ( **len** ( _personalization_string_ ) > 256), then **Return** (“ _Personalization_string_ too long”, − 1). 

- Step 6 is replaced by : 

_instantiation_nonce_ = _Null._ 

The instantiate algorithm ( **CTR_DRBG_Instantiate_algorithm** ) is the same as that provided in <u>Appendix B.3.2, except that steps 1 and 2 are replaced by:</u> 

_temp_ = **len** ( _personalization_strin_ g). 

If ( _temp_ < 256), then _personalization_strin_ g = _personalization_string_ || 0<sup>256-</sup><sup>_temp_</sup> . 

_seed_material_ = _entropy_input_ ⊕ _personalization_string_ . 

#### **B.4.3 Reseeding a CTR_DRBG Instantiation Without a Derivation Function** 

The reseed function ( **CTR_DRBG_Reseed_function** ) is the same as that provided in <u>Appendix B.3.3, except that step 3 is replaced by:</u> 

If ( **len** ( _additional_input_ ) > 256), then **Return** (“ _additional_input_ too long”). 

86 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

The reseed algorithm ( **CTR_DRBG_Reseed_algorithm** ) is the same as that provided in <u>Appendix B.3.3, except that steps 1 and 2 are replaced by:</u> 

_temp_ = **len** ( _additional_input_ ). 

If ( _temp_ < 256), then _additional_input_ = _additional_input_ || 0<sup>256-</sup><sup>_temp_</sup> . 

_seed_material_ = _entropy_input_ ⊕ _additional_input_ . 

#### **B.4.4 Generating Pseudorandom Bits Using CTR_DRBG** 

The generate function ( **CTR_DRBG_Generate_function** ) is the same as that provided in <u>Appendix B.3.4, except that step 5 is replaced by:</u> 

If ( **len** ( _additional_input_ ) > 256), then **Return** (“ _additional_input_ too long”, _Null_ ). 

The generate algorithm ( **CTR_DRBG_Generate_algorithm** ) is the same as that provided in <u>Appendix B.3.4, except that step 2.1 is replaced by:</u> 

_temp_ = **len** ( _additional_input_ ). 

If ( _temp_ < 256), then _additional_input_ = _additional_input_ || 0<sup>256-</sup><sup>_temp_</sup> . 

87 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **Appendix C: (Informative) DRBG Mechanism Selection** 

Almost no application or system designer starts with the primary purpose of generating good random bits. Instead, the designer typically starts with a goal that he wishes to accomplish, then decides on cryptographic mechanisms, such as digital signatures or block ciphers that can help him achieve that goal.  Typically, as the requirements of those cryptographic mechanisms are better understood, he learns that random bits will need to be generated, and that this must be done with great care so that the cryptographic mechanisms will not be weakened.  At this point, there are three things that may guide the designer's choice of a DRBG mechanism: 

- a. He may already have decided to include a set of cryptographic primitives as part of his implementation. By choosing a DRBG mechanism based on one of these primitives, he can minimize the cost of adding that DRBG mechanism.  In hardware, this translates to lower gate count, less power consumption, and less hardware that must be protected against probing and power analysis.  In software, this translates to fewer lines of code to write, test, and validate. 

For example, a module that generates RSA signatures has an available hash function, so a hash-based DRBG mechanism (e.g., **Hash_DRBG** or **HMAC_DRBG** ) is a natural choice. 

- b. He may already have decided to trust a block cipher, hash function, or keyed hash function to have certain properties.  By choosing a DRBG mechanism based on similar properties, he can minimize the number of algorithms he has to trust. 

For example, an AES-based DRBG mechanism (i.e., **CTR_DRBG** using AES) might be a good choice when a module also provides encryption with AES.  Since the security of the module is dependent on the strength of AES, the module's security is not made dependent on any additional cryptographic primitives or assumptions. 

- c. Multiple cryptographic primitives may be available within the system or consuming application, but there may be restrictions that need to be addressed (e.g., code size or performance requirements). 

For example, a module with support for both hash functions and block ciphers might use the **CTR_DRBG** if the ability to parallelize the generation of random bits is needed. 

The DRBG mechanisms specified in this Recommendation have different performance characteristics, implementation issues, and security assumptions. 

#### **C.1 Hash_DRBG** 

**Hash_DRBG** is based on the use of an **approved** hash function in a counter mode similar to the counter mode specified in [SP 800-38A].  For each generate request, the current value of _V_ (a secret value in the internal state) is used as the starting counter that is iteratively changed to generate each successive _outlen_ -bit block of requested output, where _outlen_ is the number of bits in the hash function output block. At the end of the generate request, and before the pseudorandom output is returned to the consuming application, the secret value _V_ is updated in order to prevent backtracking. 

88 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Performance.** The **Generate function** is parallelizable, since it uses the counter mode. Within a generate request, each _outlen_ -bit block of output requires one hash function computation and several addition operations; an additional hash function computation is required to provide the backtracking resistance. **Hash_DRBG** produces pseudorandom output bits in about half the time required by **HMAC_DRBG** . 

**Security. Hash_DRBG** ’s security depends on the underlying hash function’s behavior when processing a series of sequential input blocks.  If the hash function is replaced by a random oracle, **Hash_DRBG** is secure.  It is difficult to relate the properties of the hash function required by **Hash_DRBG** with common properties, such as collision resistance, pre-image resistance, or pseudorandomness.  There are known problems with **Hash_DRBG** when the DRBG is instantiated with insufficient entropy for the requested security strength, and then later provided with enough entropy to attain the amount of entropy required for the security strength, via the inclusion of additional input during a generate request. However, these problems do not affect the DRBG’s security when **Hash_DRBG** is instantiated with the amount of entropy specified in this Recommendation. 

**Constraints on Outputs.** As shown in Table 2 of <u>Section 10.1, for each hash function, up to 2</u><sup>48</sup> generate requests may be made, each of up to 2<sup>19</sup> bits. 

**Resources. Hash_DRBG** requires access to a hash function, and the ability to perform addition with _seedlen_ -bit integers. **Hash_DRBG** uses the hash-based derivation function **Hash_df** (specified in <u>Section 10.3.1) during instantiation and reseeding. Any implementation requires the</u> storage space required for the internal state (see Section 10.1.1.1). 

**Algorithm Choices.** The choice of hash functions that may be used by **Hash_DRBG** is discussed in Section 10.1. 

#### **C.2 HMAC_DRBG** 

**HMAC_DRBG** is built around the use of an **approved** hash function using the HMAC construction.  To generate pseudorandom bits from a secret key ( _Key_ ) and a starting value _V_ , the **HMAC_DRBG** computes 

_V_ = **HMAC** ( _Key_ , _V_ ). 

At the end of a generation request, the **HMAC_DRBG** generates a new _Key_ and _V_ , each requiring one HMAC computation. 

**Performance. HMAC_DRBG** produces pseudorandom outputs considerably more slowly than the underlying hash function processes inputs; for SHA-256, a long generate request produces output bits at about 1/4 of the rate that the hash function can process input bits.  Each generate request also involves additional overhead equivalent to processing 2048 extra bits with SHA256. Note, however, that hash functions are typically quite fast; few if any consuming applications are expected to need output bits faster than **HMAC_DRBG** can provide them. 

**Security.** The security of **HMAC_DRBG** is based on the assumption that an **approved** hash function used in the HMAC construction is a pseudorandom function family.  Informally, this means that when an attacker does not know the key used, HMAC outputs look random, even given knowledge and control over the inputs.  In general, even relatively weak hash functions seem to be quite strong when used in the HMAC construction.  On the other hand, there is not a 

89 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

reduction proof from the hash function’s collision resistance properties to the security of the DRBG; the security of **HMAC_DRBG** ultimately relies on the pseudorandomness properties of the underlying hash function. Note that the pseudorandomness of HMAC is a widely used assumption in designs, and the **HMAC_DRBG** requires far less demanding properties of the underlying hash function than **Hash_DRBG** . 

**Constraints on Outputs.** As shown in Table 2 of <u>Section 10.1, for each hash function, up to 2</u><sup>48</sup> generate requests may be made, each of up to 2<sup>19</sup> bits. 

**Resources.  HMAC_DRBG** requires access to a dedicated HMAC implementation for optimal performance. However, a general-purpose hash function implementation can always be used to implement HMAC. Any implementation requires the storage space required for the internal state (see <u>Section 10.1.2.1).</u> 

**Algorithm Choices.** The choice of hash functions that may be used by **HMAC_DRBG** is discussed in Section 10.1. 

#### **C.3 CTR_DRBG** 

**CTR_DRBG** is based on using an **approved** block cipher algorithm in counter mode (see [SP <u>800-38A]).  At the present time, only three-key TDEA and AES are</u> **approved** for use by the Federal government for use in this DRBG mechanism.  Pseudorandom outputs are generated by encrypting successive values of a counter; after a generate request, a new key and new starting counter value are generated. 

**Performance.** For large generate requests, **CTR_DRBG** produces outputs at the same speed as the underlying block cipher algorithm encrypts data.  Furthermore, **CTR_DRBG** is parallelizable.  At the end of each generate request, work equivalent to two, three or four encryptions is performed, depending on the choice of underlying block cipher algorithm, to generate new keys and counters for the next generate request. 

**Security.** The security of **CTR_DRBG** is directly based on the security of the underlying block cipher algorithm, in the sense that, as long as some limits on the total number of outputs are observed, any attack on **CTR_DRBG** represents an attack on the underlying block cipher algorithm. 

**Constraints on Outputs.** As shown in Table 3 of <u>Section 10.2.1, for each of the three AES key</u> sizes, up to 2<sup>48</sup> generate requests may be made, each of up to 2<sup>19</sup> bits, with a negligible chance of any weakness that does not represent a weakness in AES.  However, the smaller block size of TDEA imposes more constraints: each generate request is limited to 2<sup>13</sup> bits, and at most, 2<sup>32</sup> such requests may be made. 

The output constraints are necessary to avoid a distinguishing attack on the **CTR_DRBG** , described in [Campagna], in which the fact that a single generate call can never produce a duplicate block from the block cipher is used to build a distinguisher for the DRBG's outputs. These output constraints apply to the use of **CTR_DRBG** for any single purpose, regardless of how many times the DRBG is reseeded. However, the distinguishing attack is theoretical − it poses no practical threat to any real-world application of the DRBG. 

90 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

The distinguishing attack is conceptually quite simple. For concreteness, consider the case of TDEA **CTR_DRBG** . The DRBG generates a maximum of 128 64-bit blocks per generate request, thus providing 2<sup>13</sup> bits per request. An ideal random source would have a very small probability (about 2<sup>-51</sup> ) of producing a pair of identical 64-bit blocks within that generate request output; each generate request from the **CTR_DRBG** is generated by running the block cipher in counter mode, so there can never be a duplicate block produced within a generate request output. (The block cipher is rekeyed between generate requests, so duplicate blocks can appear in different generate request outputs.) TDEA **CTR_DRBG** permits the use of up to 2<sup>32</sup> generate requests. An ideal random source, providing 2<sup>32</sup> sequences of 128 64-bit blocks, would have a probability of about 2<sup>-19</sup> of having a duplicate block in one of those sequences of 128 64-bit blocks; the **CTR_DRBG** will never have such a duplicate block. This provides a distinguisher − an attacker, given a sequence of 2<sup>13</sup> 2<sup>32</sup> = 2<sup>45</sup> bits from an ideal random source, has about a 2<sup>-19</sup> probability of seeing an event happen that could never happen from TDEA **CTR_DRBG** . 

Consider some application in which a DRBG's outputs must not be distinguishable by an attacker, and assume that an attacker who sees 2<sup>64</sup> bits of output from the TDEA **CTR_DRBG** across at least one reseed, and wants to decide whether these bits came from the **CTR_DRBG** or from an ideal random source. The best case for the attacker is that each generate request used the maximum allowed value of 2<sup>13</sup> bits of output = 128 64-bit blocks of output. In this case, the TDEA **CTR_DRBG** received 2<sup>45</sup> generate requests. An ideal random sequence has a probability of about 2<sup>-6</sup> of having a duplicate block in one of the generate outputs; the **CTR_DRBG** outputs will never have one. An attacker looking at the sequence will not be able to determine that it came from the **CTR_DRBG** , though he would have a pretty large advantage in a distinguishing game. 

The case for AES **CTR_DRBG** is similar: each generate request may produce no more than 2<sup>19</sup> bits, which means 2<sup>12</sup> 128-bit blocks. In an ideal random sequence of 2<sup>12</sup> 128-bit blocks, the probability that any two blocks will be the same is approximately 2<sup>-105</sup> ; AES **CTR_DRBG** will never provide a generate output with duplicate blocks. AES **CTR_DRBG** permits up to 2<sup>48</sup> generate requests, so an attacker seeing the maximum length of output permitted (2<sup>67</sup> bits) from either an AES **CTR_DRBG** instance or an ideal random sequence will have a 2<sup>-57</sup> probability of being able to distinguish the two. 

**Resources.  CTR_DRBG** may be implemented with or without a derivation function. 

When a derivation function is used, **CTR_DRBG** can process the personalization string and any additional input in the same way as any other DRBG mechanism, but at a cost in performance because of the use of the derivation function (as opposed to not using the derivation function; see below). Such an implementation may be seeded by any **approved** randomness source that may or may not provide full entropy. 

When a derivation function is not used, **CTR_DRBG** is more efficient when the personalization string and any additional input are provided, but is less flexible because the lengths of the personalization string and additional input cannot exceed _seedlen_ bits. Such implementations must be seeded by a randomness source that provides full entropy (e.g., an **approved** entropy source that has full entropy output or an **approved** NRBG). 

**CTR_DRBG** requires access to a block cipher algorithm, including the ability to change keys, and the storage space required for the internal state (see <u>Section 10.2.1.1).</u> 

91 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

**Algorithm Choices.** The choice of block cipher algorithms and key sizes that may be used by **CTR_DRBG** is discussed in Section 10.2.1. 

#### **C.4 Summary for DRBG Selection** 

Table C-1 provides a summary of the costs and constraints of the DRBG mechanisms in this Recommendation. 

|**Table C-**|**1: DRBG Mechanism Sum**|**mary**|
|---|---|---|
||**Dominating**<br>**Cost/Block**|**Constraints**<br>**(max.)**|
|Hash_DRBG|2 hash function calls|2<sup>48</sup>calls of 2<sup>19</sup>bits|
|HMAC_DRBG|4 hash function calls|2<sup>48</sup>calls of 2<sup>19</sup>bits|
|CTR_DRBG (TDEA)|1 TDEA encrypt|2<sup>32</sup>calls of 2<sup>13</sup>bits|
|CTR_DRBG (AES)|1 AES encrypt|2<sup>48</sup>calls of 2<sup>19</sup>bits|

92 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

### **Appendix E : (Informative) Revisions** 

The original version of this Recommendation was completed in June, 2006. In **March 2007** , the following changes were made (note that the changes are indicated in italics): 

1. Section 8.3, item 1.a originally stated the following: 

“One or more values that are derived from the seed and become part of the internal state; these values must usually remain secret” 

The item now reads: 

“One or more values that are derived from the seed and become part of the internal state; these values **_should_** remain secret”. 

2. In Section 8.4, the third sentence originally stated: 

“Any security strength may be requested, but the DRBG will only be instantiated to one of the four security strengths above, depending on the DRBG implementation.” 

The sentence now reads: 

“Any security strength may be requested _(up to a maximum of 256 bits)_ , but the DRBG will only be instantiated to one of the four security strengths above, depending on the DRBG implementation.” 

3. In Section 8.7.1, the list of examples of information that could appear in a personalization string included private keys, PINs and passwords. These items were removed from the list, and seedfiles were added. 

4. In Section 10.3.1.4, a step was inserted that will provide backtracking resistance (step 14 of the pseudocode). The same change was made to the example in Appendix B.5.3 (step 19.1). In addition, the two occurrences of _block_counter_ (in input 1 and processing step 

   - 1) were corrected to be _reseed_counter_ . 

This Recommendation was developed in concert with American National Standard (ANS) X9.82, a multi-part standard on random number generation. Many of the DRBGs in this Recommendation and the requirements for using and validating them are also provided in ANS X9.82, Part 3. Other parts of that Standard discuss entropy sources and RBG construction. During the development of the latter two documents, the need for additional requirements and capabilities for DRBGs were identified. As a result, the following changes were made to this Recommendation in **August 2008** : 

1. Definitions have been added in Section 4 for the following: **approved** entropy source, DRBG mechanism, fresh entropy, ideal random bitstring, ideal random sequence and secure channel. The following definitions have been modified: backtracking resistance, deterministic random bit generator (DRBG), entropy, entropy input, entropy source, full entropy, min-entropy, prediction resistance, reseed, security strength, seed period and source of entropy input. 

2. In Section 6, a link was provided to examples for the DRBGs specified in this Recommendation. 

95 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

3. In Section 7.2, paragraph 3. 2<sup>nd</sup> sentence: The “ **should** ” has been changed to “ **shall** ”, so that the sentence now reads: 

The personalization string **shall** be unique for all instantiations of the same DRBG mechanism type (e.g., **HMAC_DRBG** ). 

4. In Section 8.2, paragraph 2, additional text was added to the first sentence, which now reads: 

A DRBG is instantiated using a seed and may be reseeded _; when reseeded, the seed_ **_shall_** _be different than the seed used for instantiation_ . 

5. In Section 8.5, Figure 4 has been updated, and the last paragraph has been revised to discuss the use of a secure channel. 

6. In Sections 8.6.5 and 8.6.9, statements were inserted that prohibit a DRBG instantiation from reseeding itself. 

7. References to “entropy input” have been removed from Section 8.6.9. 

8. Section 8.8: An example was added to further clarify the meaning of prediction resistance. 

9. In Section 9, a _prediction_resistance_request_ parameter has been added to the **Get_entropy_input** call, along with a description of its purpose to the text underneath the call. 

10. In Section 9, a footnote was inserted to explain why a _prediction_resistance_request_ parameter may be useful in the **Get_entropy_input** call. 

11. In Section 9.1, the following changes were made: 

   - The following sentence has been added to the description of the _prediction_resistance_flag_ : 

In addition, step 6 can be modified to not perform a check for the 

_prediction_resistance_flag_ when the flag is not used in an implementation ; in this case, the **Get_entropy_input** call need not include the _prediction_resistance_request_ parameter. 

- The following requirement has been added to the **Required information not provided by the consuming application during instantiation:** 

This input **shall not** be provided by the consuming application as an input parameter during the instantiate request. 

   - A _prediction_resistance_request_ parameter has been added to the **Get_entropy_input** call of step 6 of the **Instantiate Process** . 

   - Step 5 was originally intended for implementations of the **Dual_EC_DRBG** to select an appropriate curve. This function is now performed by the **Dual_EC_DRBG** ’s Instantiate_algorithm. Changes were made to provide the security strength to the Instantiate_algorithm. The Instantiate_algorithm for each DRBG was changed to allow the input of the security strength. 

12. In Section 9.2, the following changes have been made: 

96 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

   - A _prediction_resistance_request_ parameter has been added to the **Reseed_function** call. 

   - A description of the parameter has been added below the function call. 

   - A step was inserted that checked a request for prediction resistance (via the _prediction_resistance_request_ parameter) against the state of the _prediction_resistance_flag_ that may have been set during instantiation. 

   - A _prediction_resistance_request_ parameter has been added to the **Get_entropy_input** call of (newly numbered) step 4 of the **Reseed Process** . 

   - In the description of the _entropy_input_ parameter, a restriction was added that the _entropy_input_ is not to be provided by the instantiation being reseeded. 

   - A footnote was inserted to explain why the prediction_resistance_request parameter might be useful. 

13. In Section 9.3.1, the following changes were made: 

   - Text has been added to item 4 to refer to the **Reseed_function** . 

   - A _prediction_resistance_request_ parameter has been added to the **Get_entropy_input** call of step 7.1 of the **Generate Process** . 

   - A substep was inserted in step 9 of the **Generate Process** to check the _prediction_resistance request_ against the state of the _prediction_resistance_flag_ . 

14. In Section 9.3.2, step e, a phrase addressing the presence of the _prediction_resistance_request_ indicator was inserted. 

15. In Sections 10.1 and 10.3.1, the new hash functions approved in FIPS 180-4 have been added. 

16. In Sections 10.1.2 ( **HMAC_DRBG** ) and 10.2.1 ( **CTR_DRBG** ), the update functions have been renamed to reflect the DRBG with which they are associated (i.e., renamed to **HMAC_DRBG_Update** and **CTR_DRBG_Update** ). 

17. In Section 10.1.2.1, the last paragraph has been revised to indicate that only the Key is considered to be a critical value. 

18. In Sections 10.1.2.3, 10.2.1.3.1, 10.2.1.3.2 and 10.3.1.2, the description of the _personalization_string_ has been revised to indicate that the length the _personalization_string_ may be zero. 

19. In Section 10.2.1.5, the following statement has been added to the first paragraph: 

If the derivation function is not used, then the maximum allowed length of _additional_input_ = _seedlen_ . 

20. In Section 10.3.1.2, the specification was changed to select an elliptic curve and return the parameters of that curve to the **Instantiate_function** that called the routine. 

21. In the first paragraph of Appendix A.1, a statement has been added that if alternative points are desired, they **shall** be generated as specified in Appendix A.2. 

97 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

   22. The original Appendices C and D on entropy sources and RBG constructions, respectively, have been removed and the topics will be discussed in SP 800-90B and C 

   23. In Appendix C.2 (originally Appendix E.2), a paragraph has been inserted after the table of E values that discusses the analysis associated with the table values. 

   24. The additional uses of the _prediction_resistance_request_ parameter (as specified in Section 9) have been added to the following appendices: 

      - D.1.1, step 4; 

      - D.1.2, Input and step 4; 

      - D.1.3, step 7.1; 

      - D.3.2, step 4; 

      - D.3.3, Input and step 4; and 

      - D.3.4, step 7.1. 

   25. The name of the update call has been changed in the following appendices: 

      - D.2.1, step 4; 

      - D.2.2, step 5; 

      - D.3.1, title; and 

      - D.4.1, title. 

   26. In Appendix D.3 (originally Appendix F.3), the first paragraph, which  discusses the example, has been modified to discuss the _prediction_resistance_request_ parameter in the **Get_entropy_input** call. 

   27. In Appendix D.5 (originally Appendix F.5), the description of the example in paragraph 2 has been changed so that the example does not include prediction resistance, and the definition for the _reseed_interval_ has been removed from the list. The **Dual_EC_Instantiate_function** has been modified to reflect the changes made to the **Instantiate_function** and **Instantiate_algorithm** (see the last bullet of modification 8 above). In addition, the pseudocode for the **Reseed_function** has been removed, and steps in F.5.1 and F.5.2 that dealt with reseeding have been removed. 

- In **June 2015** , the following substantive changes were made in Revision 1 of [SP 800-90A]: 

   1. The following definitions were modified to be consistent with definitions in other parts of this Recommendation: backtracking resistance, entropy source, non-deterministic random bit generator, prediction resistance, and source of entropy input. The following definitions have been removed: public key and public-key pair. A definition for 

      - "randomness source" has been added, and the definition of "source of entropy input" has been removed. 

   2. The term "source of entropy input" has been replaced by "randomness source" to avoid confusion with the term "entropy source input," which is used in SP 800-90C to mean input from an entropy source. A "randomness source" (formerly "source of entropy input") could be an entropy source, an NRBG or a DRBG. 

98 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

3. Section 5: The ECDLP abbreviation and the floor and gcd symbols were removed. Definitions of the leftmost, rightmost, min and select functions have been added, and have been used  throughout the document. 

4. Section 6: The reference to number-theoretic problems was removed, as well as the old Appendix A that provided security considerations for DRBGs based on elliptic curves, and the old Appendix F that listed **shall** statements. 

5. Section 7: The first paragraph has been modified, and includes an additional **shall** statement. In Section 7.1, the first two sentences have been modified for clarity. In Section 7.2, the second paragraph and the first sentence of the third paragraph have been modified for clarity; the personalization string is now recommended, rather than required, to be unique. In Section 7.4, the second item has been modified for clarity, and the last paragraph has been removed, since it was not needed here. 

6. Section 8: In Section 8.1, the second sentence has been modified for clarity. In Section 8.2, additional text has been added to the last sentence for clarity. In Section 8.3, item 1b, the reference to _blocks_ was removed, since it pertained to the Dual_EC_DRBG. In Section 8.4, the third sentence is a general statement that replaces the last two sentences of that paragraph; the subject with more detail is now discussed below Table 1. In the paragraph under Figure 4, text has been inserted in the second sentence for clarity. The first sentence of the next paragraph has been modified for clarity, and an additional paragraph has been added to the section to mention the relationship between a DRBG sub-boundary and a cryptographic module boundary. 

7. Section 8.5: A reference to the cryptographic boundary for FIPS 140 has been inserted in **bold** to draw the reader’s attention to the fact that it is different than the DRBG’s boundaries. In the paragraph under item 3, an example has been provided for clarity. In the following two paragraphs, a reference to SP 800-90C has been inserted to direct the reader to that document for further discussion on cryptographic module boundaries. 

8. Section 8.6: In Section 8.6.2, a reference to fresh entropy has been inserted in the second sentence. In Section 8.6.3, text has been inserted at the end of the second sentence for clarity. In Section 8.6.4, a **shall** statement has been inserted at the end of the first sentence. Sections 8.6.5 and 8.6.7 were revised to clarify the source of the entropy input and nonce. In Section 8.6.6, text was inserted that states that entropy input is a critical security parameter for cryptographic module validation.   Section 8.6.7 was modified to provide more information about suitable nonces and to state that the uniqueness of the nonce is applicable to the cryptographic module in which it is used, and to indicate that the nonce is a critical security parameter. In Section 8.6.8, text was added about enforcing the seedlife. In Section 8.6.9, ‘DRBG’ was changed to ‘DRBG instantiation’ for clarity. 

9. Section 8.7: Sections 8.7.1 and 8.7.2 have been modified to clarify that the optional personalization string and additional input may be obtained from outside a cryptographic module, that the personalization string is not a critical security parameter, and that the additional input may be a critical security parameter if secret information is included. 

10. Section 8.8: The last sentence of the second paragraph under the list has ‘direct or indirect’ inserted for clarity. A paragraph has been added to the end of the section to recommend reseeding whenever possible. 

99 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

11. Section 9: A paragraph discussing the pseudocode used has been inserted at the beginning of the section, and modifications to the third and fourth paragraphs have been made for clarity; text has also been added to the next-to-last paragraph that discusses error codes more thoroughly. The last sentence in the third paragraph has been modified to only require that the entropy input and nonce be provided as discussed in Sections 8.6.5 and 8.6.7 and in SP 800-90C. A paragraph has been added to discuss checking the status code. In Section 9.2, clarifying information has been inserted about the _prediction_resistance_request_ parameter. In Sections 9.1, 9.2 and 9.3, returns to the consuming application have been modified for those cases where other than SUCCESS is appropriate as a status to be returned from the function (e.g., parameter errors, entropy unavailability or entropy source failure); this change was made to better accommodate the various **Get_entropy_input** constructions specified in SP 800-90C. In Section 9.1 and 9.3.1, the item in the list referring to elliptic-curve parameters was removed, and the discussion of the _status_ output has been modified for clarity. 

12. Section 10: Section 10 now includes a link to the DRBG test vectors on the NIST web site. 

Sections 10.1, 10.1.1 and 10.1.2 now include short discussions about selecting hash functions to support the DRBG's intended security strength. 

The **Dual_EC_DRBG** has been removed, and section numbers adjusted accordingly. In Section 10.2.1, a paragraph under Table 3 has been added for explanatory purposes. In Section 10.2.1.3.2, the first paragraph has been modified for clarity. Section 10.2 has been modified to allow the counter field to be a subset of the input block and to allow either derivation function specified in the document; this is indicated in step 2.1 of Section 10.2.1.2 and step 4.1 of Sections 10.2.1.5.1 and 10.2.1.5.2 (note that this change continues to allow the use of the entire input block as the counter field, as was specified in the previous versions of this document); Table 3 has been modified to include restrictions on the length of the counter field and to indicate the restrictions on the number of bits that can be requested during a single request as a function of the counterfield length and the previous restriction on the number of bits that could be requested. The first paragraphs of Sections 10.3 and 10.3.2 have been modified slightly for clarity. 

Step 11 in Section 10.3.2 has been respecified using the (new) select function. 

13. Section 11: The third paragraph has been added for clarity, and the last sentence of the next paragraph has been removed. In Section 11.1, the references to the **Dual_EC_DRBG** have been removed from the third and fifth bullet, and the wording of the next-to-last bullet has been modified to be conditional. In Section 11.2, additional text has been inserted to address validation testing. In Section 11.3, the health testing requirements have been modified. 

14. The previous Appendix A was removed; this appendix contained application-specific constants for the **Dual_EC_DRBG** . 

15. Appendix A now contains the conversion routines. Appendix A.5.4 (the old Appendix B.5.4), which contained the complex modular method for converting bits to numbers, has been removed because of an error in the specification. 

100 

NIST SP 800-90A Rev. 1 

Recommendation for Random Number Generation Using Deterministic RBGs 

16. Appendix B now contains the pseudocode examples previously provided in Appendix D, less examples for the **Dual_EC_DRBG** . In Appendix B.4, the discussion of the example has been changed slightly. 

17. The previous Appendix C was removed; this appendix contained security considerations relating to the **Dual_EC_DRBG** . 

18. The new Appendix C is the same as the previous Appendix E, minus the **Dual_EC_DRBG** discussion. 

Additional text has been inserted into the discussion of the **CTR_DRBG** in Appendix C.3 (the constraints subsection) that discusses the constraints provided in Table 3 of Section 10.2.1. 

19. The referenced documents now in Appendix D have been updated, and a reference to [Campagna] has been added. 

20. The previous Appendix F was removed; this appendix contained a list of **shall** statements that could not be validated by NIST’s validation program. 

101