# Literature verification: reconstructions, complete positivity, controllability

Date: 2026-09-30. Read-only literature check.

## Method and verification levels (read first)

The egress proxy blocked every primary host, so WebFetch failed on all of them: arxiv.org,
iopscience, APS, Springer, Wikipedia, ADS, Semantic Scholar API, OSTI, PubMed, quantum-journal.org,
inspirehep and university pages. Everything below comes from WebSearch result indexes, meaning
search-engine titles and snippets drawn from arXiv, APS, IOP, Springer, Cambridge and similar
pages. No full text was read.

Tags:
- **[V]**: bibliographic data or content confirmed by search results that cite the primary page
  (arXiv abstract page, publisher page, or an equivalent).
- **[V-2]**: the content claim is confirmed only through a secondary source in the search
  results, such as a later paper, a review or a summary. Treat this as good but not primary.
- **[K]**: taken from prior knowledge and not confirmed in this session. **UNVERIFIED.** Check it
  against the full text before citing it.

Roles columns: (a) selects ℂ over ℝ/ℍ/Jordan/GPT; (b) complete positivity / purification /
dilation; (c) continuity or transitivity of reversible dynamics; (d) composition / tensor product.

***

## 1. Hardy (2001)

- **Bib [V]:** L. Hardy, "Quantum Theory From Five Reasonable Axioms", arXiv:quant-ph/0101012
  (v4, 25 Sep 2001). It is an arXiv preprint only; the absence of a journal version is [K]. A
  companion paper is L. Hardy, "Why quantum theory?", in *Non-locality and Modality* (Springer,
  NATO Sci. Ser., 2002), DOI 10.1007/978-94-010-0385-8_4 [V].
- **Definitions [V]:** K is the number of real parameters, or probability measurements, needed to
  determine the state. N is the maximum number of states that can be reliably distinguished in a
  single shot.
- **Axioms [V]:**
  1. **Probabilities**: relative frequencies converge.
  2. **Simplicity**: K = K(N), and for each N, K takes the minimum value consistent with the
     axioms.
  3. **Subspaces**: a system restricted to an M-dimensional subspace behaves like a system of
     dimension M.
  4. **Composite systems**: N_AB = N_A N_B and K_AB = K_A K_B.
  5. **Continuity**: there exists a continuous reversible transformation between any two pure
     states.
- **Derived [V]:** K = N^r with r a positive integer. r = 1 gives classical theory and r = 2 gives
  complex QM. Axioms 1–4 are satisfied by classical probability theory. Axiom 5 excludes the
  classical case, and dropping only the word "continuous" returns classical theory [V].
- **Roles:**
  - (a) The Composite axiom (K_AB = K_A K_B) forces K = N^r. That excludes real QM, where
    K = N(N+1)/2 and K_AB > K_A K_B, and quaternionic QM, where K = N(2N−1) and
    K_AB < K_A K_B. The quaternionic exclusion is stated in the search snippet [V-2]. Continuity
    excludes r = 1, and Simplicity then selects r = 2 as the least remaining value [V for r = 1/2;
    the "Simplicity picks the least r" mechanism is V-2].
    - The "local tomography" reading of K_AB = K_A K_B is standard [V-2].
  - (b) No axiom. That Hardy derives transformations to be completely positive by letting them act
    on part of a composite is [K] UNVERIFIED.
  - (c) The Continuity axiom (transitivity of continuous reversible dynamics on pure states) [V].
  - (d) The Composite-systems axiom, as a counting rule and not an explicit tensor-product
    postulate [V].

## 2. Chiribella, D'Ariano, Perinotti

- **Bib [V]:**
  - G. Chiribella, G. M. D'Ariano, P. Perinotti, "Probabilistic theories with purification",
    *Phys. Rev. A* **81**, 062348 (2010), arXiv:0908.1583.
  - Same authors, "Informational derivation of quantum theory", *Phys. Rev. A* **84**, 012311
    (2011), DOI 10.1103/PhysRevA.84.012311, arXiv:1011.6451.
- **Axioms of the 2011 paper [V]:** five "standard" axioms plus one postulate.
  1. **Causality**: no signalling from the future. This means the probability of preparations is
     independent of the choice of later measurement, equivalently the deterministic effect is
     unique. The paraphrase is [K].
  2. **Perfect distinguishability**: every state that is not completely mixed is perfectly
     distinguishable from some other state [V].
  3. **Ideal compression**: every state admits an ideal compression scheme [V].
  4. **Local distinguishability**: two different bipartite states give different probabilities
     for some product experiment. This is equivalent to local tomography [V].
  5. **Pure conditioning**: for a pure bipartite state, each outcome of an atomic measurement on
     one side induces a pure state on the other [V].
  6. **Purification** (the postulate): every state has a purification, unique up to reversible
     channels on the purifying system [V].
- **2010 result [V]:** purification is equivalent to every physical process having a reversible
  realization, i.e. a reversible interaction with an environment that is then discarded. This is
  an operational Stinespring dilation. The paper also constructs a Choi–Jamiołkowski-type
  isomorphism.
- **Roles:**
  - (a) Local distinguishability (local tomography) selects ℂ. Real QM fails it and is otherwise
    regarded as satisfying the remaining principles, including purification [V-2]. The statement
    that real QM satisfies all five other principles is supported only by secondary sources:
    **UNVERIFIED against the paper text.**
    - Purification is what separates quantum from classical theory [V].
  - (b) Purification gives the dilation and Choi isomorphism [V]. CP itself is built into the OPT
    framework: tests are defined through their action on arbitrary extensions A⊗C, and the
    identity on the ancilla is always an admissible test [K]. For a textbook-level statement in
    the operational framework, see Chiribella, "Dilation of states and processes in
    operational-probabilistic theories", EPTCS **172** (QPL 2014), arXiv:1412.8539 [V]. It
    describes an operational GNS/Stinespring obtained from purification.
  - (c) No continuity axiom. Transitivity on pure states is derived from purification
    (uniqueness up to reversible maps) [K].
  - (d) Composition is framework-level in OPT: a symmetric monoidal structure in which
    parallel-composed systems are systems. Local distinguishability then fixes the linear-span
    tensor structure [K/V-2].

## 3. Masanes & Müller (2011)

- **Bib [V]:** Ll. Masanes, M. P. Müller, "A derivation of quantum theory from physical
  requirements", *New J. Phys.* **13**, 063001 (2011), arXiv:1004.1483.
- **Requirements [V]:**
  1. **Finiteness**: a capacity-2 system has a finite-dimensional state space.
  2. **Local tomography**: the state of AB is determined by the statistics of local measurements.
  3. **Equivalence of subsystems**: the states of a capacity-N system with E_N(ω) = 0 form a
     system equivalent to a capacity-(N−1) system.
  4. **Symmetry**: every pair of pure states is connected by a reversible transformation, and the
     reversible transformations form a continuous group. That the continuity sits inside this
     requirement is [K]; the search snippet gives only transitivity.
  5. **All measurements allowed**: every map from S_2 to [0,1] of the right type is an outcome
     probability.
  - The only theories satisfying all five are classical probability theory and finite-dimensional
    complex QM [V-2].
- **Roles:**
  - (a) Local tomography, together with continuous reversible interaction between two generalized
    bits, forces the Bloch-ball dimension d = 3. That is complex QM: rebits would be d = 2 and
    quaternionic bits d = 5 [V-2]. The full classification is in Ll. Masanes, M. P. Müller,
    D. Pérez-García, R. Augusiak, "Entanglement and the three-dimensionality of the Bloch ball",
    *J. Math. Phys.* **55**, 122203 (2014), arXiv:1111.4060 [V]. For d ≠ 3 the only consistent
    bipartite dynamics are trivial and there are no entangled states [V].
  - (b) Not an axiom; CP is derived [K].
  - (c) Symmetry (Requirement 4) [V, continuity K].
  - (d) Local tomography [V].
- **Related [V]:** Masanes, Müller, Augusiak, Pérez-García, "Existence of an information unit as a
  postulate of quantum theory", *PNAS* **110**, 16373 (2013), arXiv:1208.0493. It uses an
  information unit, continuity and reversibility of dynamics, and tomographic locality.

## 4. Dakić & Brukner

- **Bib [V]:**
  - B. Dakić, Č. Brukner, "Quantum Theory and Beyond: Is Entanglement Special?", arXiv:0911.0695
    (3 Nov 2009).
  - Published in H. Halvorson (ed.), *Deep Beauty: Understanding the Quantum World through
    Mathematical Innovation* (Cambridge Univ. Press, 2011), ch. 9, pp. 365–392.
- **Axioms [V-2]:**
  1. **Information capacity**: all systems with a capacity of one bit are equivalent.
  2. **Locality**: the state of a composite is determined by measurements on the subsystems, i.e.
     local tomography.
  3. **Reversibility**: a reversible transformation exists between any two pure states.
  - A fourth requirement, **Continuity** of those transformations, separates QM from classical
    theory.
  - Headline result: no theory other than QM exhibits entanglement consistently with the axioms.
- **Roles:**
  - (a) Locality (local tomography) plus continuity. The counting fixes the Bloch-ball dimension at
    3 [V-2].
  - (b) None.
  - (c) Reversibility plus Continuity [V-2].
  - (d) Locality [V-2].

## 5. Jordan-algebraic line; Koecher–Vinberg; BMU 2014; Müller–Ududec 2012

- **Koecher–Vinberg [V]:** finite-dimensional open, regular, homogeneous, self-dual cones
  correspond one-to-one with formally real (Euclidean) Jordan algebras. The cones are the
  symmetric cones.
  - Proved by M. Koecher (1957) and E. B. Vinberg (1960/61; sources differ on the date).
  - The exact journal lines were not verified. Koecher 1957, *Amer. J. Math.* **79**, 575
    ("Positivitätsbereiche im Rⁿ"), is [K]. Vinberg's paper and year are **UNVERIFIED**.
  - The classification of simple EJAs as real, complex or quaternionic Hermitian matrices, 3×3
    octonionic matrices, or spin factors is standard (Jordan–von Neumann–Wigner 1934) [K].
- **Barnum & Wilce [V]:** H. Barnum, A. Wilce, "Local tomography and the Jordan structure of
  quantum theory", *Found. Phys.* **44**, 192–212 (2014), arXiv:1202.4513.
  - Result [V]: using Hanche-Olsen, complex QM with superselection rules is the only non-signalling
    theory in which:
    - systems are EJAs (homogeneous self-dual cones);
    - composites are locally tomographic;
    - at least one system is a qubit.
  - **Role (a):** local tomography selects ℂ among EJAs [V].
- **Barnum, Graydon & Wilce [V]:** H. Barnum, M. A. Graydon, A. Wilce, "Composites and categories
  of Euclidean Jordan algebras", *Quantum* **4**, 359 (2020), arXiv:1606.09331.
  - Result [V]: no reasonable composite contains the exceptional algebra.
  - One dagger-compact category unifies real, complex and quaternionic QM, excluding the
    quaternionic bit.
  - **Role (d):** ℝ and ℍ can be composed if local tomography is dropped [V].
- **Barnum, Müller & Ududec [V]:** H. Barnum, M. P. Müller, C. Ududec, "Higher-order interference
  and single-system postulates characterizing quantum theory", *New J. Phys.* **16**, 123029
  (2014), DOI 10.1088/1367-2630/16/12/123029, arXiv:1403.4147.
  - **Postulates [V]:**
    1. no higher-order interference;
    2. classical decomposability of states;
    3. strong symmetry.
  - Solutions [V]: the non-classical solutions are real, complex and quaternionic QM, 3-level
    octonionic QM, and ball state spaces.
  - Adding a fourth postulate, **observability of energy**, leaves complex QM uniquely. This ties
    ℂ to the existence of Hamiltonian dynamics [V].
  - **Roles:**
    - (a) Observability of energy; no composition is assumed [V].
    - (c) Strong symmetry: reversible maps act transitively on tuples of perfectly
      distinguishable pure states. That definition is [K].
    - (d) None [V].
- **Müller & Ududec [V]:** M. P. Müller, C. Ududec, "Structure of reversible computation
  determines the self-duality of quantum theory", *Phys. Rev. Lett.* **108**, 130401 (2012),
  arXiv:1110.3516.
  - Result [V]: bit symmetry, meaning every logical bit maps to every other by a reversible
    transformation, implies self-duality.
  - **Role:** this is (c) feeding into the self-duality half of Koecher–Vinberg. Homogeneity needs
    a separate argument [K].

## 6. Real and quaternionic QM: Wootters, Stueckelberg, Hardy–Wootters, Adler

- **Wootters [V]:** W. K. Wootters, "Local accessibility of quantum states", in W. H. Zurek (ed.),
  *Complexity, Entropy and the Physics of Information* (Addison-Wesley, 1990), pp. 39–46.
  - **Content [V-2]:** local accessibility. Measurements just sufficient for the subsystems are,
    performed jointly, just sufficient for the composite.
    - Real QM: K = N(N+1)/2, so K > K₁K₂ and local accessibility fails.
    - Quaternionic QM: K < K₁K₂.
    - Complex QM is the case with equality.
    - Wootters' conjectured form is g(N) = N^r − 1.
- **Hardy & Wootters [V]:** L. Hardy, W. K. Wootters, "Limited holism and real-vector-space quantum
  theory", *Found. Phys.* **42**, 454 (2012), arXiv:1005.4870.
  - Content [V-2]: real QM is not locally tomographic but is bilocally tomographic.
  - The volume/page is [K].
- **Stueckelberg [V]:** E. C. G. Stueckelberg, "Quantum theory in real Hilbert space", *Helv.
  Phys. Acta* **33**, 727–752 (1960). Follow-up: Stueckelberg & M. Guenin, *Helv. Phys. Acta*
  **34**, 621 (1961).
  - Content [V-2]: the complex structure is recovered from a real theory through an operator J
    commuting with all observables, i.e. a superselection-type rule.
  - Stueckelberg motivated J by the uncertainty relations [K].
- **Quaternionic composition [V-2]:** the ordinary tensor product fails because of
  noncommutativity. The naive product loses half the quaternionic action on each factor and cannot
  be iterated to three or more factors.
  - S. L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford Univ. Press, 1995)
    [V].
  - **Role (d):** composition is the known obstruction for ℍ.

## 7. Renou et al. (2021)

- **Bib [V]:** M.-O. Renou, D. Trillo, M. Weilenmann, T. P. Le, A. Tavakoli, N. Gisin, A. Acín,
  M. Navascués, "Quantum theory based on real numbers can be experimentally falsified", *Nature*
  **600**, 625–629 (2021), arXiv:2101.10873.
  - The full author list is [K]; the first three authors are [V].
- **Assumptions [V/V-2]:**
  - Standard QM postulates, with the Hilbert space taken over ℝ or ℂ.
  - **Composition by tensor product**: real QM keeps the Kronecker product.
  - **Independent sources are represented by product states** ρ_AB₁ ⊗ ρ_B₂C in a bilocal network
    (entanglement-swapping scenario; the witness is a CHSH-type quantity called CHSH₃).
  - Result: real QM cannot reproduce the complex prediction.
  - Real QM does reproduce all single-party and bipartite Bell correlations [V-2].
  - Experiments: PRL **128**, 040402 and 040403 (2022) [V].
- **Critique [V]:** T. Hoffreumon, M. P. Woods, "Quantum theory based on real numbers cannot be
  experimentally falsified", arXiv:2603.19208 (Mar 2026).
  - They separate product-state independence from operational independence (no observable
    cross-source correlations).
  - They argue the Renou conclusion rests on the untestable product-state assumption.
  - A comment followed: arXiv:2604.07425.
  - Related work [V, content not checked]: arXiv:2604.19482 (real QM with a modified composition
    rule); "Partial independence suffices to rule out Real Quantum Theory experimentally",
    arXiv:2502.20102.
- **Roles:**
  - (a) and (d) coincide here. ℂ is selected only given the tensor-product composition of
    independent sources [V].

## 8. Selby, Scandolo & Coecke (2021)

- **Bib [V]:** J. H. Selby, C. M. Scandolo, B. Coecke, "Reconstructing quantum theory from
  diagrammatic postulates", *Quantum* **5**, 445 (2021), arXiv:1802.00367.
- **Content [V]:**
  - All postulates are stated diagrammatically, in process-theory / category terms.
  - The novel postulate is **symmetric purification**, which holds in both classical theory and QM.
  - Ordinary purification follows from symmetric purification plus purity of cups.
  - A **sharp dagger** is essential.
  - Causality is defined through discarding.
- **Full postulate list and the role of each: UNVERIFIED.** No full text was reachable.
  - Likely route [K]: the postulates lead to Jordan-algebraic / BMU-type single-system structure.
    Local tomography, or an equivalent composition postulate, then selects ℂ via Barnum–Wilce.
  - Do not cite which postulate selects ℂ without checking the paper.
- **Roles:**
  - (b) Symmetric purification [V].
  - (d) Composition is primitive, since the process theory is a symmetric monoidal category [V].

## 9. Solèr (1995)

- **Bib [V]:** M. P. Solèr, "Characterization of Hilbert spaces by orthomodular spaces", *Comm.
  Algebra* **23**(1), 219–243 (1995), DOI 10.1080/00927879508825218.
- **Content [V]:** an infinite-dimensional orthomodular space over an involutive division ring
  that contains an infinite orthonormal sequence is a Hilbert space over ℝ, ℂ or ℍ.
- **Role (a):** it narrows the field to three options but does not choose among ℝ, ℂ and ℍ. An
  extra input is needed, such as continuous symmetry (Wigner/Stone), composition, or
  observability of energy [K].
- Exposition: S. S. Holland, *Bull. AMS* **32**, 205 (1995) [K].

## 10. Complete positivity and initial correlations

- **Standard sources [V]:**
  - W. F. Stinespring, "Positive functions on C*-algebras", *Proc. AMS* **6**, 211–216 (1955).
  - M.-D. Choi, "Completely positive linear maps on complex matrices", *Linear Algebra Appl.*
    **10**, 285–290 (1975).
  - K. Kraus, *States, Effects, and Operations* (Springer LNP **190**, 1983).
  - The "trivial extension" argument: a map must remain positive when tensored with the identity
    on an untouched ancilla, which is CP. That this is the standard textbook motivation, as in
    Kraus and Nielsen–Chuang, is [K].
- **Critique [V]:** P. Pechukas, "Reduced dynamics need not be completely positive", *PRL* **73**,
  1060 (1994); R. Alicki, Comment, *PRL* **75**, 3020 (1995); Pechukas, Reply, *PRL* **75**, 3021
  (1995).
- **Precise condition (Pechukas's theorem) [V-2]:**
  - Reduced dynamics is ρ_S ↦ Tr_E[U Φ(ρ_S) U†], where Φ is an assignment map ρ_S ↦ ρ_SE.
  - Suppose Φ is defined on **all** of S's state space and is **linear, consistent**
    (Tr_E Φ(ρ) = ρ) and **positive**. Then Φ(ρ) = ρ ⊗ ω_E with a **fixed** ω_E, i.e. a product
    initial state, and the reduced map is CP.
  - With initial correlations, one of three things must give:
    1. **positivity** of the map is lost on part of the state space;
    2. the domain is restricted (a "compatibility domain");
    3. linearity or consistency is abandoned.
  - Alicki's position [K]: keep the product assignment and treat correlated preparations as
    outside the dynamical-map description.
- **Jordan, Shaji & Sudarshan [V]:** "Dynamics of initially entangled open quantum systems", *PRA*
  **70**, 052110 (2004), arXiv:quant-ph/0407083.
  - With initial entanglement, the linear reduced map need not be CP and can map some positive
    matrices to non-positive ones unless the domain is restricted.
  - The maps look like operator-sum forms with some minus signs.
- **Discord line [V]:**
  - Rodríguez-Rosario, Modi, Kuah, Shaji, Sudarshan, *J. Phys. A* **41**, 205301 (2008): purely
    classical (zero-discord) correlations give CP reduced dynamics.
  - Shabani & Lidar, *PRL* **102**, 100402 (2009) claimed vanishing discord is necessary and
    sufficient.
  - The necessity part was refuted by Brodutch, Datta, Modi, Rivas, Rodríguez-Rosario, *PRA*
    **87**, 042301 (2013), arXiv:1212.4387, with an erratum in *PRL* **116**, 049901 (2016).
- **Modern resolution [V]:**
  - F. Buscemi, "Complete positivity, Markovianity, and the quantum data-processing inequality, in
    the presence of initial system-environment correlations", *PRL* **113**, 140502 (2014),
    arXiv:1307.0363.
  - CP is necessary and sufficient for the data-processing inequality. Reduced dynamics is CP, even
    with initial correlations, iff those correlations allow no anomalous backward flow of
    information from environment to system.
  - The setting is the "steering"/preparation picture, in which Buscemi's condition is stated for
    the correlated state and the class of local preparations [K].
- **General framework [V]:** J. M. Dominy, A. Shabani, D. A. Lidar, "A general framework for
  complete positivity", *Quantum Inf. Process.* **15**, 465–494 (2016), arXiv:1312.0908.
  - Three inequivalent notions of CP arise for correlated initial states.
  - Follow-up: Dominy & Lidar, "Beyond complete positivity", *QIP* **15**, 1349 (2016),
    arXiv:1503.05342. The volume/page is [K].
  - Assignment-map positivity implies CP (I. Sargolzahi, *QIP* **19**, 310 (2020),
    arXiv:1906.11502) [V-2].

## 11. Controllability (Lie-algebra rank condition)

- **Jurdjevic & Sussmann [V]:** V. Jurdjevic, H. J. Sussmann, "Control systems on Lie groups",
  *J. Diff. Eq.* **12**, 313–329 (1972).
  - Result [V-2]: on a **compact connected** Lie group G, the right-invariant system with drift
    is controllable iff the Lie algebra generated by the drift and the control fields is all of
    Lie(G). Transfer time is bounded.
- **Ramakrishna et al. [V]:** V. Ramakrishna, M. V. Salapaka, M. Dahleh, H. Rabitz, A. Peirce,
  "Controllability of molecular systems", *PRA* **51**, 960–966 (1995).
  - Result [V]: N-level systems are lifted to unitary propagators, and invariant-systems-on-Lie-groups
    results are applied.
- **Textbook [V]:** D. D'Alessandro, *Introduction to Quantum Control and Dynamics* (Chapman &
  Hall/CRC, 2007).
- **Also [V]:**
  - S. G. Schirmer, H. Fu, A. I. Solomon, "Complete controllability of quantum systems", *PRA*
    **63**, 063410 (2001), arXiv:quant-ph/0010031.
  - C. Altafini, *J. Math. Phys.* **43**, 2051 (2002), arXiv:quant-ph/0110147.
- **Statement [V-2/K]:**
  - Setup: i U̇ = (H₀ + Σ_k u_k(t) H_k) U with piecewise-constant unbounded controls.
  - If Lie{−iH₀, −iH₁, …} = su(N), or u(N), then because SU(N)/U(N) is compact and connected,
    every element of SU(N) is reachable in finite time. For u(N) the global phase is included.
  - Compactness is what makes the drift harmless: its flow is recurrent.

## 12. "Composites are systems" / ancilla-closure analogues

- **Hardy (2011) [V]:** L. Hardy, "Reformulating and reconstructing quantum theory",
  arXiv:1104.2066. Later version: "Reconstructing quantum theory", arXiv:1303.1538, in Chiribella &
  Spekkens (eds.), *Quantum Theory: Informational Foundations and Foils* (Springer, 2016), ch. 7.
  - **Postulates [V-2]:**
    1. **Sharpness**;
    2. **Information locality**: maximal measurements on the components give a maximal
       measurement on the composite;
    3. **Tomographic locality**;
    4. **Compound permutability**: a compound reversible transformation permutes any maximal set
       of distinguishable states;
    5. **Sturdiness**: filters are non-flattening.
  - The output is states as positive operators and transformations as CP trace-non-increasing
    maps [V-2].
  - **Roles:**
    - (a) Tomographic locality [V-2].
    - (d) Information locality plus tomographic locality [V-2].
    - (c) Compound permutability, which is discrete and not continuous [V-2].
- **CDP purification [V]:** every process is a reversible system–environment interaction
  followed by discarding the environment. Systems are closed under parallel composition in OPT.
  The environment is itself a system to which the same principle applies, so iteration is
  automatic; that remark is [K].
  - Iterated closure is made explicit in G. Chiribella, "Agents, subsystems, and the conservation
    of information", *Entropy* **20**(5), 358 (2018), arXiv:1804.01943 [V; article number K].
    Every agent defines a subsystem, and all subsystem states have canonical purifications within
    a closed global system.
  - S. Gogioso, "A Process-Theoretic Church of the Larger Hilbert Space", arXiv:1905.13117 [V]:
    local process theories are rebuilt from a global reversible theory via purification.
- **Closest formal analogue of attach-a-fresh-ancilla-and-discard as a closure operation [V]:**
  - M. Huot, S. Staton, "Universal properties in quantum theory", QPL 2018, EPTCS pp. 213–224,
    arXiv:1901.10117. CPTP maps form the universal monoidal category with terminal unit receiving
    a functor from isometries: the "affine reflection" of isometries. In other words, freely
    adding discarding to pure (isometric) quantum theory yields exactly the channels.
  - Huot & Staton, "Quantum channels as a categorical completion", LICS 2019, arXiv:1904.09600
    [V title].
  - B. Coecke, S. Perdrix, "Environment and classical channels in categorical quantum mechanics",
    *LMCS* **8**(4) (2012; CSL 2010), arXiv:1004.1598 [V]. This axiomatizes "environment"
    (discarding) structures.
  - O. Cunningham, C. Heunen, "Axiomatizing complete positivity", QPL 2015, EPTCS **195**,
    148–157, arXiv:1506.02931 [V].
- **Masanes–Müller "equivalence of subsystems" is not a composite-closure postulate.** It concerns
  subspaces, i.e. faces [V].
- **Carcassi, Maccone & Aidala [V]:** G. Carcassi, L. Maccone, C. A. Aidala, "Four postulates of
  quantum mechanics are three", *PRL* **126**, 110402 (2021), arXiv:2003.11007.
  - Result: the tensor-product rule is derived from the state and measurement postulates plus a
    definition of composite system.
  - Relevant to (d). See also arXiv:2411.15964, "The composition rule for quantum systems is not
    the only possible one" [V title].

***

## Items needing full-text check before citation

1. The Selby–Scandolo–Coecke postulate list and which postulate selects ℂ.
2. That CDP's real-QM counterexample satisfies all principles except local distinguishability
   (currently secondary only).
3. Whether Hardy 2001 derives CP from the composite axiom.
4. The continuity clause inside Masanes–Müller Requirement 4.
5. Vinberg's citation and year; Koecher's journal line.
6. The page and volume numbers marked [K] (Hardy–Wootters, Dominy–Lidar 2016, Chiribella Entropy
   article number).
7. The full Renou et al. author list.
