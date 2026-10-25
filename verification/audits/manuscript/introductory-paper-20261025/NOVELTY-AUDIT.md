> **Status: unreviewed audit record.** Its classifications, confidence levels
> and recommendations are provisional until an independent review compares the
> actual theorem statements and proofs; no verdict in it is an established
> result. References cited from memory are unverified. Apart from this block,
> the file is byte-identical to the auditor's report (sha256
> 9f8a0ef3ec7d1e62bf671dd38c82500ad5857ba375924a96fe35d531f51fcf3c). See
> `README.md`.

# Novelty and fidelity audit — introductory paper (PR #918)

Working title of the proposed paper: *Observational Incompleteness: From Deterministic Dynamics to
Quantum Observations*. This is audit 2 of `verification/audits/manuscript/introductory-paper-20261025/PLAN.md`
(branch `draft/oi-introductory-paper-20261025`, head `a02ef7f9`).

- **Sources read at** `main` `c91bf5dd84b6415e1c59820ae0333f3b062d10b6`: `AGENTS.md`; `papers/Main.md`
  (898 lines, read in full for §1–§3.4 and §4.4, skimmed for §3.3, §3.5 and §4.5–§4.6);
  `book/ch07-gravity.md` §7.6; `verification/lean-manuscript-census.json`; the Lean modules
  `OIBridge/{Equivalence,EquivalenceChain,HiddenMemory,C3Necessity,CausalReadback,RecurrenceHorizon,ReadbackRobustness}.lean`.
- **PR #917** was read at head `809fac52` (`verification/programmes/black-hole-information/PROGRAMME.md`)
  together with its single comment. #917 contains **no independently reviewed finding**, so under PLAN.md
  "Inputs and boundaries" every black-hole statement below is cited as **open**.
- **Literature access.** The proxy refused arxiv.org, ar5iv, export.arxiv.org and inspirehep.net (403 /
  DNS), so I could not open any full text. Each reference has a verification tag:
  - **[S]**: bibliographic data and abstract-level content confirmed through web-search result summaries.
    Full text was **not** read.
  - **[M]**: cited from memory and not verified in this session. It must be checked before it is cited
    in a paper.

  No source is presented here as read in full.
- **Writes.** This file is the only output. Reading #917's branch needed one `git fetch` of
  `research/oi-bh-information-audit` into the scratch clone. That added objects and a remote-tracking
  ref, and nothing else in the clone was modified.

Citations of the form `Main:NNN` are line numbers of `papers/Main.md` at `c91bf5dd`.

***

## 1. Claim map

The paper's central display is `S ⟺ D ⟺ Q_fb` (Main:18, Main:526–532). Per §A.34, each arrow is
listed below on its own line.

### 1.1 The three classes, as the kernel defines them (`OIBridge/Equivalence.lean`)

| Class | Kernel definition | Notes |
|---|---|---|
| **S** | `Stochastic P`: `P : (Fin (K+1) → V) → ℝ`, nonnegative, sums to 1 (l.147). | This is every probability law on the finite set `V^{K+1}`. |
| **D** | `RevRealizable P` (l.157–183): a finite `Hid`, a permutation `step` of `V × Hid`, and an **arbitrary initial law on `V × Hid`**. `P` is the pushforward of that law along the visible trajectory. | The docstring at l.150–156 says the initial law **need not factor** as visible prior × hidden prior. The stronger independent-prior form "is NOT what this theorem's class (D) asks for". |
| **Q_fb** | `QfbRealizable P` (l.190–217): a finite basis `Bas`, a unitary `U`, a **classical** initial law on `Bas`, and a read map `Bas → V`. The trajectory weight is `init(σ0)·∏|U_{σ_{k+1}σ_k}|²`, i.e. projective measurement in the **whole** fixed basis at every step, with collapse. | This class is exactly "functions (lumpings) of Markov chains whose transition matrix is unistochastic". No generator clause: the `U = e^{-iĤ}` remark of Main:532 is left unformalized (l.28–34). |

### 1.2 Components

| # | Statement (exact scope) | Where proved | Kernel / evidence | Directional status |
|---|---|---|---|---|
| **C1** S ⇒ D | Every finite-horizon law on finite `V` is the visible marginal of a permutation of `V × Hid` with some initial law on `V × Hid`. | Main:532 says this is "the response-table construction of §3.4". | `S_imp_D` (Equivalence.lean:419). The kernel construction is **not** the response table: its hidden state is a clock together with the **entire trajectory record** `τ`, the initial law is `P` pushed forward to `(τ0,(0,τ))`, and `exists_perm_extending` (l.60) pads the result to a permutation. | Own witness. |
| **C1′** S ⇒ D, independent-prior form | The same, with a hidden prior μ_H **independent of the visible initial state** (response table, ledger, clock), for rational laws (Main:496–500) or for arbitrary real laws (the response-table extension, Main:498). | Prose proof at Main:500; probes `process_dilation_probes.py`, `review4_probes.py`. | Main:500 and the census family note both cite `S_imp_D` as this theorem's kernel witness. `S_imp_D`'s own docstring says it does **not** prove this form. **Untraced to the kernel** (fidelity note F2). | Prose and probe only. |
| **C2** D ⇒ Q_fb | Take `U = permMatrix(step⁻¹)`. Its Born weights are indicators, so the full-basis measured chain is the deterministic orbit. | Main:532 | `D_imp_Qfb` (l.294), `permMatrix_mem_unitaryGroup` (EquivalenceChain.lean:178). | Own witness. |
| **C3** Q_fb ⇒ S | Born chain weights are nonnegative and sum to 1, because unitarity makes the columns unit vectors. | Main:532 | `Qfb_imp_S` (l.245), `sum_chain` (l.99). | Own witness. |
| **C4** The three ⟺ | `finite_horizon_equivalence` (l.459) assembles C1–C3 and takes none of them as a hypothesis. | Main:526–532 | Kernel (Mathlib). | Each direction has its own witness, so §A.34 is satisfied **for the class definitions above**. |
| **C5** One-step uniform-prior marginal | A uniform-prior bijection marginal is doubly stochastic. Conversely, each doubly stochastic matrix is such a marginal: exactly when its entries are rational, and approximately otherwise (Birkhoff–von Neumann). | Main:270–272 | Probes only. Not kernel-checked. | The forward direction is elementary. The converse rests on BvN. |
| **C6** One-step ancilla dilation | `W\|i⟩ = Σ_j √T_ij \|j⟩⊗\|i⟩` is an isometry with ancilla-marginal `T`, and it extends to a unitary. | Main:206–208 | `dilation_isometry`, `dilation_marginal`, `dilation_extends` (EquivalenceChain.lean:292–335). | Own witness. |
| **C7** Stochastic-inverse lemma | A finite stochastic matrix with a stochastic one-sided inverse is a permutation matrix. | Main:133–135 | `isPermMatrix_of_stochastic_inverse` (EquivalenceChain.lean:109). | — |
| **C8** Recurrence ⇒ P-indivisible | Let `φ` be a bijection on a finite `C_V × C_H` with uniform prior. If `T` is not a permutation, then the process is P-indivisible (Main:115–129). The C4 version (Main:137–139): C4 forces some rooted map Γ_k to be a non-permutation, and with `Γ_L = I` this gives indivisibility somewhere in the cycle. | Main:115–141 | `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon.lean:148) via `c4r_implies_pIndivisible` (CausalReadback.lean:134). The census marks this family **kernel-only** with `manuscript: []`, and Main does not cite it. The step "C4 ⇒ some Γ_k is a non-permutation" is prose. | One-way theorem. Main:121 correctly states that the TV-monotonicity converse is false. |
| **C9** Readback ⇒ CMI | A C4 gap of size δ on histories of probability ≥ p₀ gives `I(X_<k;X_{k+1}\|X_k) ≥ p₀δ²/ln2` (Pinsker). | Main:167–170 | Probes (`c4_backflow_probes.py`). Not kernel-checked (no Pinsker in OIBridge). | One-way. |
| **C10** Unavoidable hidden memory | In any faithful deterministic realization: (a) `P(X_{t+1}\|p,x) = (f_x)_#μ_p`; (b) TV(next laws) ≤ TV(posteriors); (c) `M_t ≤ I(X_<t;H_t\|X_t) ≤ log₂\|C_H\|`. | Main:582–590 | `unavoidable_hidden_predictive_memory` (HiddenMemory.lean:185). | (a)–(c) are kernel-checked. The "biconditional" `M_t>0 ⟺ readout-relevant hidden memory` (Main:592, Summary Main:580(2)) is prose. Neither of its directions has a separate kernel witness (F6). |
| **C11** C3 necessity | `I(X_<t;X_>t\|X_t) ≤ log₂ m` (data processing). | Main:484–492 | `c3_necessity`, `card_hidden_ge_two_pow_Istar` (C3Necessity.lean). | One-way. |
| **C12** Characterization (ii) ⟺ (iii) | Within the accessible window: non-Markovian ⟺ arises from a per-horizon bijection marginal with C1, C3, C4 and a fixed prior. | Main:516–522, proof Main:608 | (iii)⇒(ii): C9 (prose and probes). (ii)⇒(iii): C1′ (prose; the kernel pointer is the weaker C1). | Both directions have prose witnesses. Main:596 records that C4 coincides with (ii) in any faithful realization, which makes the equivalence close to definitional (F5). |
| **C13** Canonical predictive quotient | The future-tail object `T(P)` is terminal among faithful deterministic realizations: the unique morphism sends each state to its visible future, and fibres need not be unique. | Main:600 | Census names `fiber_freedom`. I did not audit this module. | — |
| **C14** No fixed finite carrier for qubit operational behaviour | Nonnegative factorization through N states gives the bound, together with the **imported** unboundedness of nonnegative rank [Heinosaari et al.]. | Main:538 | The factorization half is elementary. The unboundedness is external. | One-way (obstruction). |
| **C15** ε-gluing / uniform continuum realization | For fixed `d`, a finite instrument family or net, horizon `K` and ε, one finite reversible realization reproduces all adaptive protocols to TV ≤ ε. | Main:544–578 | Prose with explicit bounds; probes `opglue_probes.py`. I did not check the kernel coverage. | Two-sided ε-density for the constructed subclass (Main:578). |
| **C16** Black-hole Page curve, Page time 0.646 t_evap, generalized second law | book §7.6. | book/ch07-gravity.md:108–156 | Conditional on **H-scramble**, which ch07:126 calls "named, not established". #917 has no reviewed result. | **Open**. |

**Scope conditions common to C1–C4.**
- Finite visible alphabet and a finite horizon K.
- The hidden space grows with K.
- Readout is in one fixed basis, measured at every step.
- Only passive (non-intervened) laws are covered.

These are not part of C1–C4:
- interventions, which are C15 and the comb theorem (Main:460);
- coherent preparations and composites, which are open (Main:534);
- a single all-time realization, which is impossible by periodicity (Main:618).

***

## 2. Prior literature, component by component

Classification key:
- **(a)** a direct application of known results;
- **(b)** a known result restated in OI terms;
- **(c)** a new combination or packaging;
- **(d)** plausibly a new theorem.

### 2.1 S ⇒ D (C1, C1′)

**What is known.**
- **Pushing randomness into initial conditions.** Every finite-horizon law is a deterministic function of
  a random initial condition. This is the elementary "random mapping" or functional representation of a
  process: `X_{k+1} = f(X_{≤k}, U_{k+1})` with independent uniform `U`. It is standard in probability
  (e.g. Kallenberg, *Foundations of Modern Probability*, transfer / noise-outsourcing lemma [M]).
- **Stationary infinite-horizon analogue.** It is textbook ergodic theory. Every stationary process is the
  coordinate process of the two-sided shift, which is an invertible measure-preserving map on path space
  (Kolmogorov extension plus the shift [M]). The kernel's "clock together with the full trajectory record"
  carrier is the finite, cyclically closed truncation of this canonical construction.
- **Making the map a bijection.** Recording history so that a logically irreversible step becomes
  injective is Bennett's construction:
  - C. H. Bennett, "Logical reversibility of computation," *IBM J. Res. Dev.* **17**, 525–532 (1973)
    [S: abstract and three-stage construction confirmed;
    https://www.cs.princeton.edu/courses/archive/fall06/cos576/papers/bennett73.html].
  - The completion of a partial injection to a permutation (`exists_perm_extending`) is elementary
    combinatorics. Toffoli's embedding of irreversible maps in reversible ones is the same idea
    (T. Toffoli, "Reversible computing," ICALP 1980, LNCS 85 [M]).
- **Hidden Markov / realization theory.** Its hard questions concern a **fixed finite** state space,
  usually for **stationary, infinite-horizon** processes: when does a process admit a finite hidden-Markov
  realization, and what is the minimal dimension? Key sources:
  - A. Heller, "On stochastic processes derived from Markov chains," *Ann. Math. Stat.* **36**, 1286–1291
    (1965) [S: bibliographic data only; https://www.projecteuclid.org/euclid.aoms/1177698514].
  - S. W. Dharmadhikari, "Functions of finite Markov chains," *Ann. Math. Stat.* **34**, 1022–1032
    (1963) [M].
  - H. Ito, S.-I. Amari, K. Kobayashi, "Identifiability of hidden Markov information sources and their
    minimum degrees of freedom," *IEEE Trans. Inf. Theory* **38**(2), 324–333 (1992). Its subject is the
    deterministic state-output subclass of HMMs, which is precisely the structure of the kernel's `Q_fb`
    [S: citation and subject confirmed via secondary summaries].
  - B. D. O. Anderson, "The realization problem for hidden Markov models," *Math. Control Signals Systems*
    **12**, 80–120 (1999) [S: secondary].
  - M. Vidyasagar, "The complete realization problem for hidden Markov models: a survey and some new
    results," *Math. Control Signals Systems* **23**, 1–65 (2011) [S: the conference version, CDC 2005,
    and the book chapter are confirmed; the MCSS volume and pages are M].

**Closeness.** At finite horizon, with the hidden space allowed to grow with K, the realization question
is trivial: realization theory itself treats it as the unconstrained case. Main does not claim the hard
version. It records that the all-time form with one fixed finite carrier is false (Main:618) and that the
hidden space grows (Main:522).

**Verdict.**
- C1 is **(a)**, high confidence. It is elementary, and its kernel proof is a formalization, not new
  mathematics.
- C1′ is **(a)/(c)**, high confidence: response table + Bennett history ledger + padding.

### 2.2 D ⇒ Q_fb and Q_fb ⇒ S (C2, C3)

**What is known.**
- A bijection of a finite configuration set acts as a permutation unitary, and classical reversible
  dynamics is the special case of unitary dynamics whose matrix in the configuration basis is a
  permutation. This is the finite Koopman representation:
  - B. O. Koopman, "Hamiltonian systems and transformations in Hilbert space," *PNAS* **17**(5), 315–318
    (1931) [S; doi:10.1073/pnas.17.5.315].
- It is also the "ontological basis" of the cellular-automaton interpretation, in which the evolution
  operator permutes the ontological states:
  - G. 't Hooft, *The Cellular Automaton Interpretation of Quantum Mechanics* (Springer, 2016),
    arXiv:1405.1548 [S: abstract-level; the permutation-operator detail is M].
  - H.-T. Elze, "Action principle for cellular automata and the linearity of quantum mechanics," *Phys.
    Rev. A* **89**, 012111 (2014) [M].
- Classical reversible computation as a sub-case of quantum circuits (Toffoli gates) is textbook (Nielsen &
  Chuang §1.4 [M]).
- Q_fb ⇒ S is the Born rule's normalization. A system measured projectively in a fixed basis at every step
  is a classical Markov chain with unistochastic transition matrix `|U|²`. The literature on when
  sequentially measured quantum processes are classical (Kolmogorov-consistent) is directly adjacent:
  - S. Milz, D. Egloff, P. Taranto, T. Theurer, M. B. Plenio, A. Smirne, S. F. Huelga, "When is a
    non-Markovian quantum process classical?", *Phys. Rev. X* **10**, 041049 (2020), arXiv:1907.05807
    [S].
  - P. Strasberg, M. García Díaz, "Classical quantum stochastic processes," *Phys. Rev. A* **100**, 022120
    (2019), arXiv:1905.03018 [S].

**Verdict.**
- C2 is **(a)/(b)**, very high confidence: a Koopman / 't Hooft-ontological-basis restatement.
- C3 is **(a)**.
- The p-independence remark ("the recovered table is the same for |U|^p", Main:534) follows immediately
  from 0/1 entries.

### 2.3 The equivalence as a whole (C4)

**What is known.**
- Every class is the set of all probability laws on `V^{K+1}`, and each arrow is elementary. Main says so
  itself: the representation is "universal, so representability alone does not distinguish the
  memory-bearing sector" (Main:20, Main:534).
- The closest packaged prior statement is Barandes' stochastic–quantum correspondence. It maps
  generalized ("indivisible") stochastic processes into unitarily evolving systems on dilated spaces of
  dimension ≤ n³:
  - J. A. Barandes, "The Stochastic-Quantum Correspondence," *Philosophy of Physics* **3**(1):8 (2025),
    arXiv:2302.10778 [S].
  - J. A. Barandes, "The Stochastic-Quantum Theorem," arXiv:2309.03085 [M; cited in Main as ref. 11].
  - Companion: Barandes, "Quantum Systems as Indivisible Stochastic Processes," arXiv:2507.21192 [S].
- The Main corpus already relocates the representation's existence in-house and keeps the import only for
  the ≤ n³ compression (Main:350, Main:636).

**Verdict.** Packaged as "three descriptions of the same finite law class", C4 is **(c)**: a clean,
kernel-checked packaging of known facts. It is **not (d)**. Confidence: high.

A referee will recognize that C4 is equivalent to the folklore statement "finite stochastic processes are
deterministic reversible dynamics with unknown initial conditions, and reversible dynamics is permutation
unitary". The Lean formalization is a genuine contribution of a different kind: formal verification, not
new physics.

### 2.4 Dilations (C5, C6)

**What is known.**
- C6 is the Stinespring isometry of the classical channel `T`, the canonical isometric dilation:
  - W. F. Stinespring, *Proc. AMS* **6**, 211–216 (1955) [M; Main ref. 15].
- Relatives:
  - Naimark's dilation for POVMs [M].
  - Sz.-Nagy's unitary dilation of contractions (B. Sz.-Nagy, *Acta Sci. Math.* **15**, 87–92 (1953) [M]).
  - Kümmerer's Markov dilations of semigroups to automorphism groups (B. Kümmerer, "Markov dilations on
    W*-algebras," *J. Funct. Anal.* **63**, 139–177 (1985) [S: bibliographic]). This is the
    infinite-horizon, operator-algebraic analogue of "Markov dynamics = reduction of reversible dynamics".
- C5 combines G. Birkhoff (1946, *Univ. Nac. Tucumán Rev. Ser. A* **5**, 147–151 [M]) with the
  thermodynamic-resource fact that the classical "noisy operations" (permutations with a uniform ancilla,
  then marginalization) generate the doubly stochastic maps:
  - M. Horodecki, P. Horodecki, J. Oppenheim, *Phys. Rev. A* **67**, 062104 (2003), arXiv:quant-ph/0212019
    [S].
  - G. Gour, M. P. Müller, V. Narasimhachar, R. W. Spekkens, N. Yunger Halpern, *Phys. Rep.* **583**, 1–58
    (2015) [M].
- The non-unistochastic doubly stochastic witnesses (Main:204) are standard. The 3×3 matrix with a zero
  pattern fails unistochasticity (K. Życzkowski et al., "Random unistochastic matrices," *J. Phys. A*
  **36**, 3425 (2003) [M]).

**Verdict.** C5 and C6 are **(a)**, very high confidence.

### 2.5 Non-Markovianity and indivisibility (C7–C9)

**What is known.**
- C7, that a nonnegative matrix with nonnegative inverse is monomial, is classical nonnegative-matrix
  theory (e.g. Berman & Plemmons, *Nonnegative Matrices in the Mathematical Sciences*, SIAM 1994 [M]).
  **(a)**
- **Divisibility and information backflow** (Main:121): Breuer–Laine–Piilo, *PRL* **103**, 210401 (2009)
  [M]; Rivas–Huelga–Plenio [Main refs 4–5].
- **Non-Markov processes that look divisible.** Main:606 states the strict gap between Markovianity and
  P-divisibility (XOR family). Its classical counterpart, non-Markov processes whose propagators satisfy
  semigroup / Chapman–Kolmogorov-type relations, is old:
  - P. Hänggi, H. Thomas, "Time evolution, correlations and linear response of non-Markov processes,"
    *Z. Phys. B* **26**, 85–92 (1977) [S].
  - W. Feller, "Non-Markovian processes with the semigroup property," *Ann. Math. Stat.* **30**, 1252 (1959)
    [M].
- **Revivals.** Finite environments necessarily produce non-Markovian revivals via recurrence. This is
  qualitatively standard (Breuer & Petruccione, *Theory of Open Quantum Systems* [M]; finite-bath revival
  literature). I did not locate an exact prior statement of C8 in the form "finite reversible bijection +
  non-permutation one-step marginal ⇒ P-indivisible, via the stochastic-inverse lemma", nor of its C4
  version.
- C9 is Pinsker's inequality applied to the conditional-mutual-information mixture decomposition. **(a)**

**Verdict.** C8 is **(c)**, possibly **(d)** in its exact C4-rooted form, medium–low confidence that it is
new. It is an elementary argument of the kind a referee will call folklore ("finite systems recur;
recurrence returns distinguishability; return of distinguishability violates contractivity"). It is the
best candidate for a stated original lemma, but not for a headline novelty claim.

### 2.6 Hidden memory and canonical quotient (C10, C11, C13)

**What is known.**
- C10(c) and C11 are data-processing bounds. Computational mechanics carries the same content: any
  predictive presentation's state carries at least the predictive information, `C_μ ≥ E`, and the causal
  states are the minimal sufficient statistic of the past for the future:
  - J. P. Crutchfield, K. Young, "Inferring statistical complexity," *PRL* **63**, 105 (1989) [M].
  - C. R. Shalizi, J. P. Crutchfield, "Computational mechanics: Pattern and prediction, structure and
    simplicity," *J. Stat. Phys.* **104**, 817–879 (2001), arXiv:cond-mat/9907176 [S: abstract; the
    specific `C_μ ≥ E` statement is M].
  - The capacity form `m ≥ 2^{I}` is the standard memory lower bound for HMM presentations [M].
  - C10(a) and (b) are definitional and TV monotonicity.
- C13 is the final-coalgebra / minimal-realization construction. For deterministic systems with output,
  the unique morphism to the final coalgebra sends a state to its output stream (here, its visible future
  tail). See J. J. M. M. Rutten, "Universal coalgebra: a theory of systems," *Theor. Comput. Sci.* **249**,
  3–80 (2000) [S: abstract; the stream example is M]. The automata analogue is the Myhill–Nerode
  minimal-realization theorem [M].

**Verdict.**
- C10 and C11 are **(a)/(b)**, high confidence.
- C13 is **(b)**, high confidence that the terminal-object statement is known under another name. The
  intro paper should call it the final-coalgebra / minimal-realization construction, not a new theorem.

### 2.7 Operational boundary (C14, C15)

**What is known.**
- C14 is imported:
  - T. Heinosaari, O. Kerppo, L. Leppäjärvi, M. Plávala, *Phys. Rev. A* **109**, 032627 (2024) [Main ref.
    55].
- Older close results that the intro paper must cite:
  - L. Hardy, "Quantum ontological excess baggage," *Stud. Hist. Phil. Mod. Phys.* **35**, 267–276 (2004),
    arXiv:quant-ph/0206060. This is the theorem that any ontological model of even a qubit needs
    infinitely many ontic states [S: content confirmed via secondary sources; venue and arXiv number are
    M]. Main cites it nowhere.
  - E. F. Galvão, L. Hardy, "Substituting a qubit for an arbitrarily large number of classical bits," *PRL*
    **90**, 087902 (2003) [S].
  - A. Montina, "Exponential complexity and ontological theories of quantum mechanics," *PRA* **77**,
    022104 (2008) [M].
- C15: classical deterministic models of **finite** sets of quantum statistics are known to exist once
  invasiveness or contextuality is permitted:
  - Bell's and Kochen–Specker's qubit models [M].
  - The general ontological-models framework: N. Harrigan, R. W. Spekkens, *Found. Phys.* **40**, 125
    (2010) [M].
  - The "clumsiness loophole" for Leggett–Garg (Wilde & Mizel, *Found. Phys.* **42**, 256 (2012) [M]).

**Verdict.**
- C14 is **(a)**.
- C15 is **(c)**: the explicit resource accounting, the single controlled dynamics and the ε-net
  uniformity are a new packaging. I did not check the details or their kernel coverage. It is outside the
  intro paper's core.

### 2.8 Programmes the paper positions against

- **Barandes** (above): the closest. It is a correspondence, not a derivation. Its reception is mixed and
  it lies at the physics/philosophy boundary (Main:212(iv)).
- **'t Hooft** (above): the same permutation-unitary mathematics; it differs in interpretive claims.
  Main:688 contrasts them by "mechanism".
- **Spekkens toy theory**: R. W. Spekkens, *Phys. Rev. A* **75**, 032110 (2007), arXiv:quant-ph/0401052
  [S]. Also S. D. Bartlett, T. Rudolph, R. W. Spekkens, *PRA* **86**, 012103 (2012) [M].
  - What it establishes: an epistemic restriction on classical systems reproduces many quantum phenomena
    but not Bell or Kochen–Specker violation.
  - Why it matters here: it is the natural foil for "incompleteness of an embedded observer". In OI the
    restriction is structural (a hidden sector) rather than a knowledge-balance principle.
  - Main does not engage it; it must be in the related work.
- **Koopman–von Neumann, Nelson, Adler, Slagle–Preskill, QBism / relational QM, CLPW / observer
  algebras**: cited in Main §4.4. For the intro paper, only KvN, 't Hooft, Barandes, Spekkens and the
  hidden-variable / ontological-model literature bear directly on C1–C4.

***

## 3. Black-hole application

### 3.1 What is known

**(i) Preserved versus recoverable information under reversible dynamics.**
- **Classical.** Injectivity of the global map preserves information. Whether an observer with access to
  registers `R` can recover a message `b` is a separate question:
  - it is the injectivity / distinguishability of `b ↦ law(R)`;
  - it is quantified by guessing probability or mutual information;
  - it is bounded by data processing.
- **Threshold behaviour.** Classical threshold recovery is the secret-sharing phenomenon:
  - A. Shamir, "How to share a secret," *CACM* **22**, 612 (1979) [M];
  - G. R. Blakley, *AFIPS* 1979 [M].
- **Counterexample.** #917 BH-01's `F(b,r)=(b,r)` is the trivial instance of "reversible but not
  recoverable from `r`". This is standard.
- **Quantum.**
  - The no-hiding theorem: S. L. Braunstein, A. K. Pati, *PRL* **98**, 080502 (2007) [M; Main ref. 42].
  - D. N. Page, "Information in black hole radiation," *PRL* **71**, 3743 (1993), arXiv:hep-th/9306083
    [S].
  - P. Hayden, J. Preskill, "Black holes as mirrors: quantum information in random subsystems," *JHEP* 09
    (2007) 120, arXiv:0708.4025 [S]. Information thrown in after the half-way point returns quickly, under
    a random / fast-scrambling assumption.
  - Decoupling theorems: P. Hayden, M. Horodecki, A. Winter, J. Yard, *Open Syst. Inf. Dyn.* **15**, 7
    (2008) [M]; F. Dupuis, M. Berta, J. Wullschleger, R. Renner, "One-shot decoupling," *CMP* **328**, 251
    (2014) [M].
  - Recoverability in all of these depends on (a) which subsystem is accessed and (b) a typicality or
    scrambling hypothesis on the dynamics, not on unitarity alone.
- **Review.** D. Harlow, "Jerusalem lectures on black holes and quantum information," *Rev. Mod. Phys.*
  **88**, 015002 (2016) [M].

**(ii) Page curve: typicality versus scrambling versus gravity.**
- **Typicality.** Page's curve is an average over Haar-random pure states:
  - D. N. Page, "Average entropy of a subsystem," *PRL* **71**, 1291 (1993), arXiv:gr-qc/9305007 [S].
  - E. Lubkin, *J. Math. Phys.* **19**, 1028 (1978) [S: via a secondary comment, arXiv:1406.5776].
  - Canonical typicality / measure concentration: S. Popescu, A. J. Short, A. Winter, *Nature Phys.*
    **2**, 754–758 (2006), arXiv:quant-ph/0511225 [S].
  - Typicality with a center / constraints: E. Bianchi, P. Donà, *PRD* **100**, 105010 (2019),
    arXiv:1904.08370 [S].
- **What typicality gives.** It shows that *most* states have Page entanglement. It does not show that a
  *given* dynamics produces such states. That requires a scrambling or randomness hypothesis (Hayden–
  Preskill).
- **Gravity.** The island / QES calculations derive the turnover from the gravitational path integral, not
  from typicality:
  - G. Penington, *JHEP* 09 (2020) 002, arXiv:1905.08255 [M];
  - A. Almheiri, N. Engelhardt, D. Marolf, H. Maxfield, *JHEP* 12 (2019) 063, arXiv:1905.08762 [M];
  - Almheiri, Mahajan, Maldacena, Zhao, arXiv:1908.10996 [S];
  - replica wormholes, arXiv:1911.12333 [S];
  - review: Almheiri, Hartman, Maldacena, Shaghoulian, Tajdini, "The entropy of Hawking radiation,"
    arXiv:2006.06872 (*Rev. Mod. Phys.* **93**, 035002 (2021) [M]).
- **4D evaporating Schwarzschild.** Island results are mostly for eternal or two-dimensional / reduced
  models:
  - Hashimoto, Iizuka, Matsuo, "Islands in Schwarzschild black holes," *JHEP* 06 (2020) 085,
    arXiv:2004.05863, is **eternal** [S];
  - arXiv:2110.04233 (Aref'eva–Volovich) argues islands fail to bound the entropy for the evaporating
    case [S: summary only].
  - I found no 4D evaporating QES computation that gives a Page-time fraction to compare against.
    Statement C16's "quantitatively matches QES" is therefore unsupported as stated.
- **Page-time fraction.** D. N. Page, "Time dependence of Hawking radiation entropy," *JCAP* 09 (2013)
  028, arXiv:1301.4995 [S: abstract figures]. It assumes fast scrambling and photon + graviton emission
  from a large Schwarzschild hole, and gives:
  - the Page time is **0.5381 t_evap**;
  - at that time the hole has lost **40.25 %** of its initial Bekenstein–Hawking entropy.

### 3.2 Direct consequence for the OI black-hole claim (a fidelity item, not a stylistic one)

The book's `t_P = (1 − 2^{-3/2}) t_evap ≈ 0.646 t_evap` (ch07:137–139) sets the turnover at
**half the initial area entropy radiated**, i.e. it takes `S_rad = ΔS_BH`. The coarse-grained radiation
entropy exceeds the area loss by a factor β > 1:
- β ≈ 4/3 for blackbody emission into vacuum: W. H. Zurek, *PRL* **49**, 1683 (1982) [S: via secondary
  sources];
- β ≈ 1.48 for photons and gravitons (Page) [M].

With β, the Page condition `β(S₀ − S) = S` gives:
- `S/S₀ = β/(1+β)`;
- with β = 1.4847, `S/S₀ = 0.5975`, which reproduces Page's "40.25 % lost";
- `t/t_evap = 1 − (S/S₀)^{3/2} = 0.5381`, which reproduces Page's number. I checked this arithmetic
  numerically in this session.

So 0.646 is the β = 1 idealization. The claim "independent of … the species-dependent greybody factor"
(ch07:139) is false for the Page time as standardly defined, because β is species- and greybody-dependent.
#917 BH-04 already flags this conditionality. The introductory paper **must not** state 0.646 as a
prediction or as agreeing with QES.

### 3.3 What an OI paper could legitimately claim

- **Own, modest, defensible.** A clean finite statement separating three properties for an embedded
  observer with a fixed access class `𝒜` (which registers it can read, and when):
  1. **preserved**: `φ` is a bijection;
  2. **recoverable by 𝒜**: the map from messages to joint record laws on `𝒜` is injective, with a
     quantitative version via guessing probability or TV;
  3. **typical**: the Page-type entropy profile holds for an ensemble of dynamics.

  It should come with:
  - a positive model (a swap into the radiation register);
  - a reversible negative model (retained hidden register; BH-01);
  - the control that a non-scrambling product-basis permutation generates no entanglement and so yields
    no quantum Page curve (BH-02).

  This would be **(b)/(c)**: standard information theory, presented in OI's observer-access language. It is
  a pedagogical contribution and should be labelled that way.
- **Not claimable now.** All of the following are #917 BH-02–BH-06, open, unreviewed:
  - resolution of the information paradox;
  - a derivation of the Page curve from bijectivity alone (it needs H-scramble, an ensemble assumption);
  - the 0.646 Page time;
  - quantitative agreement with QES;
  - "microscopic realization of islands";
  - a proof of the generalized second law from SSA + CPTP monotonicity. #917 BH-03 gives a reset-channel
    counterexample to unconditional entropy non-decrease.

***

## 4. Fidelity notes: wording in Main stronger than its proofs

These are places the introductory paper must not inherit.

- **F1 — the Layer-1 display is false as written.**
  - Main:97–99 displays `finite-horizon non-Markovianity ⟺ ∃ finite reversible hidden-state realization`
    and calls it "the paper's core".
  - The ⇐ direction fails: Markov laws also have such realizations (C1). Main itself says, at Main:596–598,
    that this "bare form … is **false**".
  - This is an internal contradiction (§A.30, §A.34). The paper must state either the universal-
    representation form (C4) or the C4-qualified universal form (C10 with Main:610), never this display.
- **F2 — a kernel pointer names a weaker theorem.**
  - Main:500, the process-dilation theorem, has a hidden prior μ_H *independent of the visible initial
    state*. It cites `S_imp_D` as its kernel witness, and so does the census family note "equivalence
    chain and memory", which lists "the process dilation (S_imp_D)".
  - `S_imp_D`'s class `RevReal` allows an arbitrary joint initial law: the hidden record *is* the whole
    trajectory. Its docstring (Equivalence.lean:153–156) explicitly says the independent-prior form is not
    what it proves.
  - The independent-prior / response-table form is therefore prose plus probes only. Main:532 also
    describes S⇒D as "the response-table construction", while the kernel proves it with a different,
    weaker carrier.
  - This is a §A.35-type registry mismatch. The intro paper should define D as the kernel does, or say
    explicitly that the independent-prior form is proved in prose.
- **F3 — Q_fb is narrower than its name suggests.**
  - The kernel's Q_fb is full-basis projective measurement at every step, with collapse and a classical
    initial law. It is therefore a lumped unistochastic Markov chain. "Finite-dimensional unitary systems
    with Born-rule readout" (Main:16, Main:530) will be read by physicists as including coherent
    preparations and partial measurements.
  - Main:532's added "fixed autonomous generator `U_φ = e^{-iĤ}`" is not part of the class and is not
    formalized (Equivalence.lean:28–34). Ĥ = i log U is branch-dependent (Main:268).
  - The paper must define Q_fb operationally, at the kernel's scope.
- **F4 — the title and introduction overstate.**
  - "The Equivalence of Quantum Mechanics and Embedded Observation" (Main:2) and "quantum mechanics is
    identified as its form" (Main:28) go beyond a theorem whose third class is Q_fb and whose
    representation is universal (Main:534). Main itself places full operational QM outside the
    equivalence (Main:22, Main:542).
  - The intro paper's subtitle "From Deterministic Dynamics to Quantum Observations" is acceptable only if
    "quantum observations" means fixed-basis records.
- **F5 — the "necessary and sufficient conditions" claim.**
  - Main:690 says "what the present framework adds is an equivalence with necessary and sufficient
    conditions — (ii) ⟺ (iii)". By Main:596, C4 coincides with (ii) in every faithful realization, so
    (iii)⇒(ii) is immediate and (ii)⇒(iii) is S⇒D. The equivalence is close to definitional.
  - Main:608 also says "Both directions of the equivalence are theorems of this paper". Neither direction
    is kernel-checked: C9 lacks Pinsker in the kernel, and C1′ is F2.
  - Present C12 as a reformulation, not a characterization theorem.
- **F6 — a biconditional asserted as proved.**
  - Summary Main:580(2) reads "`M_t > 0 ⟺` unavoidable readout-relevant hidden predictive memory —
    proved". The kernel (HiddenMemory.lean:185) proves only clauses (a)–(c). The biconditional is a prose
    corollary of (a).
  - The right-hand side is defined as differing pushforwards, which by (a) *are* the differing
    conditionals, so the biconditional is near-definitional. Under §A.34 neither direction has a separate
    kernel witness.
- **F7 — "proved unconditionally".** Summary Main:580(4) says "proved unconditionally" for the ε-gluing.
  This audit did not trace that claim to the kernel; treat it as untraced.
- **F8 — novelty framing against prior work.**
  - Main:30 positions OI against QBism, relational QM and 't Hooft as "instead prov[ing] the finite
    observable-law correspondence directly".
  - Main cites none of: hidden-Markov realization theory, Koopman as the source of the permutation
    unitary, Bennett's history-tape reversibilization, the stationary-shift canonical realization,
    computational mechanics, final coalgebras, or Hardy's excess-baggage theorem.
  - A referee will supply these. The intro paper must cite them first.
- **F9 — black-hole wording** (book §7.6). "The framework resolves the paradox", "proves the generalized
  second law", "quantitatively matches the QES prediction", "microscopic realization of the
  entanglement-island construction", and the 0.646 Page time "independent of … greybody factor" are all
  stronger than the support. The support is conditional on H-scramble, the island correspondence is
  conjectural (ch07:145), and the Page time conflicts with Page 2013 (§3.2). The book chapter carries
  these, not Main.md; recorded here because the intro paper's application would otherwise draw on them.

Smaller items:
- Main:28 "incompleteness is derived as a structural property" is fine.
- Main:62's "only finite visible resolution is a theorem" is correctly scoped.
- The scope remarks Main:534, Main:542, Main:612 and Main:618 are accurate, and the intro paper should
  reuse them.

***

## 5. Recommendation

**Position the paper as a technical perspective / pedagogical review, not a research article.**

**Reasons.**
- Every arrow of `S ⟺ D ⟺ Q_fb` is an application or restatement of known results:
  - functional representation and Bennett reversibilization (S⇒D);
  - Koopman / 't Hooft permutation unitaries (D⇒Q_fb);
  - Born normalization (Q_fb⇒S).
- Each class equals "all probability laws on `V^{K+1}`" (§2.1–§2.3).
- The supporting lemmas are data processing, TV contraction, Pinsker, Birkhoff–von Neumann, Stinespring,
  monomial-inverse and final-coalgebra results (§2.4–§2.6).
- The black-hole application has no reviewed result (§3), and its headline number conflicts with the
  standard calculation (§3.2).
- A research-article framing would invite exactly the "folklore" verdict, and could not survive a referee
  who knows realization theory.

**A novelty statement that would survive scrutiny** (phrase it as contribution, not discovery):

> We give a self-contained, machine-checked (Lean 4/Mathlib) account of the elementary fact that, at any
> finite horizon, three descriptions of an embedded observer's records — finite stochastic laws, visible
> marginals of finite reversible dynamics, and fixed-basis Born records of finite unitary systems —
> define the same class of laws. We emphasize that this representability is universal, and therefore
> carries no discriminating physical content by itself. We isolate what does discriminate: (i) a
> universal lower bound on hidden predictive memory in every faithful deterministic completion, and
> (ii) for a fixed finite reversible representative, recurrence together with history readback forces
> stochastic indivisibility somewhere in the cycle. We then state precisely where this finite
> correspondence stops short of operational quantum theory.

Item (ii) (C8) is the only component I would offer as possibly original. It should appear as an
elementary proposition with a hedged priority statement ("we have not found it stated in this form"), not
as the paper's main theorem. The Lean formalization is a real, citable contribution of the
formal-verification type.

**The related-work paragraph the paper needs**:
- Realization theory of functions of Markov chains and hidden Markov models: Dharmadhikari 1963; Heller
  1965; Ito–Amari–Kobayashi 1992; Anderson 1999; Vidyasagar 2011. Explain that the finite-horizon,
  growing-hidden-space case is the unconstrained one, and the fixed-dimension stationary case is the hard
  one.
- The stationary-shift canonical realization and Kolmogorov extension.
- Bennett 1973 and Toffoli 1980 for reversible embeddings.
- Birkhoff–von Neumann and noisy operations (Horodecki–Horodecki–Oppenheim 2003; Gour et al. 2015).
- Stinespring, Naimark, Sz.-Nagy and Kümmerer for dilations.
- Koopman 1931 and 't Hooft 2016 for permutation unitaries.
- Barandes 2023 / 2025 for the stochastic–quantum correspondence and its ≤ n³ compression.
- Milz et al. 2020 and Strasberg–García Díaz 2019 on when measured quantum processes are classical.
- Non-Markovianity and divisibility: Breuer–Laine–Piilo 2009; Rivas–Huelga–Plenio 2010 / 2014; Pollock
  et al. 2018; Hänggi–Thomas 1977; Feller 1959.
- Computational mechanics (Crutchfield–Young 1989; Shalizi–Crutchfield 2001) for memory bounds.
- Rutten 2000 for the terminal / predictive quotient.
- Ontological models and their state-space cost: Harrigan–Spekkens 2010; Hardy 2004; Galvão–Hardy 2003;
  Montina 2008; Heinosaari et al. 2024.
- Spekkens 2007 as the epistemic-restriction foil.
- For the application: Page 1993 (both papers); Lubkin 1978; Popescu–Short–Winter 2006; Hayden–Preskill
  2007; the decoupling theorems; Page 2013; the island / QES papers and review; Braunstein–Pati 2007.

All [M] items must be verified before citation.

**Open risks.**
1. **Fidelity carry-over.** Copying Main's Layer-1 display (F1), the "necessary and sufficient
   conditions" framing (F5) or the title-level "equivalence of QM" (F4) would put a false or overstated
   claim in the intro paper. Draft from the kernel definitions in §1.1.
2. **Kernel / prose mismatch (F2).** Fix the citation or the scope before the intro paper cites
   `S_imp_D` for the response-table form. A §A.35 registry correction may be owed.
3. **Black-hole section.** It must be confined to the finite preserved / recoverable / typical
   separation with explicit controls, and must cite H-scramble as an assumption. Remove or correct the
   0.646 figure against Page 2013 (the β factor). Do not claim QES agreement, GSL or island realization
   until #917 produces reviewed results.
4. **Priority of C8.** It is plausibly folklore in the finite-environment revival literature. A
   literature search with full-text access, which was not available here, is needed before claiming it.
5. **Unverified references.** arXiv and INSPIRE were unreachable, so every [M] item and every page /
   volume detail must be checked with full-text access. This applies especially to the β ≈ 1.48 factor,
   Hardy 2004's venue, and Vidyasagar 2011's pagination.
6. **Components not audited here:** the relating-evolution non-uniqueness and fibre-Gram classification
   (Main:624), the separability threshold (Main:308), and the Bell bound `I_ont ≥ 0.0309` (Main:22, prior
   art Hall 2010–2011, Barrett–Gisin 2011 [M]). They are outside the proposed paper's core. If any of them
   is promoted into the paper as a novelty, it needs its own audit; the fibre-Gram classification is the
   likeliest candidate for genuine novelty in the corpus.

***

### Search-result links consulted (all [S]; full texts not read)

- Page 2013: https://www.arxiv.org/abs/1301.4995 · https://inspirehep.net/literature/1215583
- Hayden–Preskill 2007: https://arxiv.org/abs/0708.4025 · https://resolver.caltech.edu/CaltechAUTHORS:HAYjhep07
- Page 1993: https://arxiv.org/abs/hep-th/9306083 · https://www.doi.org/10.1103/PHYSREVLETT.71.1291
- Popescu–Short–Winter: https://arxiv.org/abs/quant-ph/0511225v2 · https://research-information.bris.ac.uk/en/publications/entanglement-and-the-foundations-of-statistical-mechanics/
- Bianchi–Donà: https://arxiv.org/pdf/1904.08370
- Lubkin (via Dyer comment): https://pdf.arxiv.org/pdf/1406.5776
- Hashimoto–Iizuka–Matsuo: https://link.springer.com/doi/10.1007/JHEP06(2020)085
- Aref'eva–Volovich note: https://arxiv.org/pdf/2110.04233
- Almheiri et al. review: https://arxiv.org/abs/2006.06872 ; AMMZ https://arxiv.org/pdf/1908.10996 ; replica wormholes https://arxiv.org/abs/1911.12333v2
- Zurek 1982 (secondary): https://arxiv.org/pdf/gr-qc/9812075 · https://arxiv.org/html/2407.08777v2
- Heller 1965: https://www.projecteuclid.org/euclid.aoms/1177698514
- Ito–Amari–Kobayashi (secondary): https://arxiv.org/pdf/2008.11487 · https://arxiv.org/pdf/2609.06735
- Vidyasagar CDC 2005: https://folk.ntnu.no/skoge/prost/proceedings/cdc-ecc05/pdffiles/papers/0862.pdf
- Milz et al. 2020: https://arxiv.org/pdf/1907.05807
- Strasberg–García Díaz 2019: https://arxiv.org/pdf/1905.03018
- Horodecki–Horodecki–Oppenheim 2003: https://arxiv.org/abs/quant-ph/0212019v2
- Hardy excess baggage (secondary): https://arxiv.org/pdf/1002.3139 · https://arxiv.org/pdf/1005.3625
- Galvão–Hardy 2003: https://arxiv.org/abs/quant-ph/0110166
- Barandes: https://arxiv.org/abs/2302.10778v3 · https://philsci-archive.pitt.edu/28060 · https://arxiv.org/html/2507.21192v1
- Spekkens 2007: https://arxiv.org/abs/quant-ph/0401052
- Kümmerer 1985 (secondary): https://arxiv.org/pdf/1804.00918
- Koopman 1931: https://en.wikipedia.org/wiki/Bernard_Koopman (record) ; doi:10.1073/pnas.17.5.315
- Bennett 1973: https://www.cs.princeton.edu/courses/archive/fall06/cos576/papers/bennett73.html
- Rutten 2000: https://ir.cwi.nl/pub/48/0048D.pdf
- Shalizi–Crutchfield 2001: https://arxiv.org/abs/cond-mat/9907176v2
- 't Hooft CAI: https://arxiv.org/abs/1405.1548
- Hänggi–Thomas 1977: https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/55778
