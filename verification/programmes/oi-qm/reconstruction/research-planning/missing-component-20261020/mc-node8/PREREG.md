# Node 8: do OI's premises constrain access across alternative interventions strongly enough to derive information causality or macroscopic locality? Preregistration

Research only, consistency axis (§A.23). No premise adopted, no status changed, nothing written to `main`. This file is
the node's preregistration. It is written, and its sha256 recorded, before any computation on a candidate. No
information quantity, visibility, distinguishability, CHSH value, macroscopic covariance, NPA membership or
derivation-step verdict has been computed under any candidate. The questions, candidates, derivation routes,
assumption ledgers, decision rules, controls and classification criteria are fixed here. The expected outcomes are not
(§A.29).

**Governing question (owner, 2026-10-21).** What restricts the response rules an embedded observer can encounter across
alternative interventions? Do OI's existing premises constrain access across alternative interventions strongly enough
to derive information causality (IC) or macroscopic locality (ML)? These are the node's approved questions
(`mc-node7` NODE.md §10, reviewed). The relation between path records and interference is a diagnostic of the same
problem: it shows where such a restriction would have to enter. If an added restriction is needed, the result is a
precise Conditional result that names a candidate missing physical principle. Either way the broader emergent-QM
hypothesis and the A2 programme stay open.

**Structure: one candidate addition and four questions, each with its own verdict.**
- **C5 (candidate), tested first** as the owner recommends: consistent information across interventions and
  composites (§5).
- **Q1.** What do C1–C4 constrain across interventions? Progress means a derived restriction on response rules, with
  its assumptions explicit (§6).
- **Q2.** Does that restriction explain complementarity? Progress means a physical link between path-record
  distinguishability and visibility, with achievable quantum boundary points (§7).
- **Q3.** Does it imply IC (3A) or ML (3B)? Each needs its own derivation from named OI premises. Finite memory may not
  stand in for either principle (§8).
- **Q4.** Does it constrain composites correctly? Quantum correlations stay achievable, post-quantum controls are
  excluded, and classical correlations are retained (§9).

**Working hypothesis, to be tested, not a result.** H-X: OI needs restrictions linking different interventions on the
same system, beyond constraints on individual recorded histories. The PR-box random-access code motivates it: Bob's
final record is small, and the excess concerns access across alternative questions, not how many bits are stored at
once (§4.2). C3's lower bound on capacity does not address that, and Shannon entropy applied to each actual record does
not by itself establish IC's cross-task inequality. Each question's verdict bears on H-X, and H-X's status is reported
from them (§15).

**Standing decisions (owner, 2026-10-21).**
- (a) Tsirelson's bound and (b) the full quantum correlation set are separate verdicts; (b-corr), the quantum
  correlator set alone, is a third line kept apart from (b) (§9). (b) is never claimed when only (a) is established.
- Every Emergence claim needs a derivation from OI premises, not an added rule. A result that needs a new axiom is
  Conditional on that named axiom (§13).
- Mandatory countercontrols for every route: K-PR6 (node 6's A = λ, B = λ ⊕ ab and its random-access-code use) and, for
  Q2, K-PROG (§4.2, §4.3).
- A1 exact stays distinct from A2 (§1).
- Even a successful complementarity result does not complete the Bell step. Nonlocality connects to measurement
  uncertainty and to steering [L: Oppenheim and Wehner, Science 330, 1072 (2010)], and a visibility trade-off does not
  supply that composite structure, so Q2 → Q4 needs its own step (§9.4).

**Tags.** [AT] adopted kernel theorem, declaration confirmed by `git grep` at the base; [W] written argument (to be
reviewed); [EC] exact computation (step 2; none run here); [NUM] floating-point evidence, never in a verdict; [L]
literature, cited from memory unless stated, not read in full; [L-s] bibliographic data and abstract-level claim checked
through a web-search summary at drafting, the paper not read; [L-c] existence and claims reported by the coordinator
and the owner on 2026-10-21, not retrieved at drafting, the paper not read; [rec] recorded in the cited record, not
re-derived; [Q] corpus or thread text quoted verbatim.

***

## 0. Base and drafting state

- Thread: `research/missing-component-20261020` at `a501b4189d7f1ada923d76179fa6a38a1a83b408` (PLAN = `../PLAN.md`; MCk =
  `../mc-nodek/NODE.md`; MC7 also `../mc-node7/PREREG.md` and `../mc-node7/amendments/AMENDMENTS.md`). Node 7's frozen
  records are cited, not changed.
- `main` at drafting: `37e55457e74702356b37a5c134fa7d5510cb2119`. `papers/` and `book/` are identical between the thread
  head and `main`. `verification/lean-mathlib/` differs only by the added `OIBridge/KTokenMaxCone.lean` and its import
  line; the cited Lean files (`OIBridge/FiniteEntropy.lean`, `OIBridge/C3Necessity.lean`) are identical at both.
- Every [Q] fragment was checked at `a501b418` by the drafting script `quotecheck.py` (whitespace collapsed,
  case-sensitive, within the stated line range): 74 fragments, 0 failing. Step 2 repeats the check (I-12).
- Worktree for drafting: a detached checkout of `a501b418`. Nothing was run in it except `git`, text search and the
  quote check. `arxiv.org` was unreachable; no paper was read in full.

**State of knowledge at drafting, stated so that the freeze can be judged.**
- No computation of §5–§9 has been run. The file was restructured twice before freeze on the owner's direction of
  2026-10-21; no computation preceded any version.
- Recorded facts the routes are built around, none a result of this node:
  - the adopted Bell branch is ontic parameter dependence (Main.md:392, :82);
  - node 7 recorded that the PR box LE(1,1) is O-admissible and admitted by every reading of Lemma 3 it tested [rec];
  - S ⟺ D ⟺ Q_fb holds for every finite law (Main.md:20, :82);
  - one controlled dynamics with a read-only program register realizes every instrument family (Main.md:560).
- **Drafting reasoning C5-0, disclosed because it shapes §5.** By the cited theorem that C5's properties, with the
  operational and composition assumptions of the IC argument, imply IC [L: Barnum et al. 2010; Al-Safi and Short 2011],
  an OI-admissible PR-box model obstructs C5 only if that model also satisfies those operational and composition
  assumptions (D-1 to D-7 of §5.2). Whether K-PR6 does is not known and is checked on the model itself (§5.3). This is a
  reading of [L] plus a [rec] fact. It is entered as step C5-0 and checked in step 2 as a [W] with its own premises; it
  is not a verdict.
- **A distinction fixed in advance.** Initial measurement independence, P(λ | x, y) = P(λ), and later ontic parameter
  dependence, b = b(x, y, λ), are different properties, and both hold on the adopted branch (a) (Main.md:82). No step of
  this file treats branch (a) as a failure of initial independence of a shared resource. Where a hidden-state route can
  fail, the file names the two possible failure modes and the step at which each would show (§8.1, IC-D5).

### 0.1 Corpus claims in the owner's direction, verified under §A.19

| # | claim | corpus text [Q] | verdict |
|---|---|---|---|
| V-1 | the double-slit account is an interpretation within the finite-law representation, not a quantitative fringe law from C1–C4 | Main.md:666: "The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix, altering the distribution of detection events."; "A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms."; "The Born rule, often treated as an independent postulate, is here part of the exact fixed-basis representation dictionary". Main.md:664: "the operational theory's unique selection remaining open (§3.4)". No fringe or visibility law appears in the physics papers or the book | supported for Main. Explainer.md:566 says "The mystery dissolves not into another postulate but into a derivation: this is what marginal statistics look like when paths through the partition are indistinguishable." with no quantitative law; its "derivation" is stronger than Main's support. Recorded, not acted on |
| V-2 | classical hidden-memory systems produce nonadditive patterns | book/ch01-observation.md:280–282: "a player who prices hands divisibly loses money at a rate equal to the interference term"; "Interference is not a substance; it is the failure of divisibility". Main.md:20: the representation "is also universal, so representability alone does not distinguish the memory-bearing sector from an ordinary Markov process" | supported |
| V-3 | C3 is a minimum hidden capacity, not a maximum on accessible information | Main.md:78: "The hidden sector has enough distinguishable states to encode the observed conditional past–future information", with $\log_2 \|\mathcal{C}_H\| \geq I^*$; Main.md:486: "I(X_{<t} ; X_{>t} \mid X_t) \leq \log_2 m" | supported. That C3 therefore cannot stand in for IC is the owner's inference, consistent with the text, and tested at IC-D5 route σ-cap (§8.1) |
| V-4 | S ⟺ D ⟺ Q_fb holds for all finite laws; C4 identifies the history-dependent sector but does not select QM | Main.md:20; "The discriminating content is history readback." Main.md:82: "C4 is not needed for the existence of a quantum representation; it is what makes the OI sector nontrivial." Main.md:578: "the response-table construction realizes arbitrary finite stochastic behavior, quantum or not". appendix-c:228: "which an ordinary classical stochastic process also reprodu[ces]" | supported |
| V-5 | C4 is the independent structural condition; C1 and C3 follow; C2 supplies persistence | Main.md:604: "Of the three structural conditions, only (C4) is logically independent."; Main.md:72: "(C1) and (C3) follow from (C4) in any faithful realization, and (C2) is a physical-regime premise"; Main.md:76: "a hidden record of visible history, once written, persists to the readback that uses it" | supported |
| V-6 | C4 does not require a causal write-then-read cycle (Main §1.3) | Main.md:80: "The condition is operational; it does not by itself assert a causal write-then-read cycle — a pre-sampled hidden variable revealed by the history satisfies it (the response-table construction, §3.4)." Main §1.3 is Main.md:70–82 | supported. C4 gives claim (i) of §6.1, not (ii) or (iii) |
| V-7 | a definite substratum state does not establish a trajectory through one geometric slit; that identification belongs to the physical realization | Main.md:666: "In the double-slit experiment, the particle traverses a single slit in the deterministic substratum." No theorem in Main derives this identification | the corpus asserts the identification at Main.md:666 without derivation. The node does not use it: "path" is defined operationally, by blocking (§7.2) |
| V-8 | one fixed dynamics can read a setting register and run different response rules | Main.md:560: "The per-instrument family assembles into one map: on the enlarged hidden sector carrying a read-only program register — the protocol table — alongside the visible record, the seeds, and the branch register" | supported; this is K-PROG's basis (§4.3) |
| V-9 | earlier nodes flagged purification as an added premise needing a source | PLAN.md:121–122: "Purification with uniqueness would cover all three, but only as a posit."; mc-node3/NODE.md:232–233: "Purification is the closest to what OI states. None of the three is derivable under κ1–κ4."; mc-node5/NODE.md:263: "The purification uniqueness that would give O-B is not supplied (Main.md:602; MC2 §3)."; mc-node5/NODE.md:344–346: "Each posits continuous reversibility or purification with uniqueness." Main.md:602: "purification demands existence and essential uniqueness — up to reversible transformations of the purifying system — within the operational theory" | supported in nodes 2, 3 and 5 (and node 4's E7, mc-node4/NODE.md:263–272 [rec]). Nodes 6 and 7 do not address it |

***

## 1. A1 exact, and the role of ε

- **Exact boundary.** Outcome (a) requires that the supremum of S_max over the admitted boxes equals 2√2 exactly, that
  the Tsirelson box itself is admitted, and that every local box is admitted. Admitting 2√2 + δ for any δ > 0 fails
  (i). Q2's quantum boundary points are tested exactly (§7.4).
- **Real boxes.** Correlation classes are sets of no-signalling boxes with real entries. Every no-signalling box is
  realized by an O-admissible realization whose prior is a realization datum (Main.md:60 [Q]: "a realization in the
  sense of §3.4 carries its own fixed hidden prior $\mu_H$ as part of the realization datum"; Main.md:578). Irrational
  entries are handled exactly in ℚ(√2) or by exact algebraic certificates.
- **ε, a tolerance (not Lemma 1's discreteness scale), never relaxes a clause.** It enters only to make exact statements
  decidable:
  1. rigorous enclosures (python-flint `arb` or mpmath `iv`, version printed) for log, asin and irrational cosines,
     refined to width 2^−64 then 2^−256, with an undecided comparison reported "undetermined";
  2. exact algebra at boundary cases (2E² − 1 = 0; V² + D² = 1);
  3. finite [EC] instances of a universal clause, which never decide it: a universal clause needs a reviewed [W], and
     one exact counterexample decides a failure.
- **A2 rows.** Node 7's ε = 1/100 rule is rerun as separately printed sensitivity rows labelled "A2", excluded from the
  verdict path (I-19).

***

## 2. Condition O (inherited) and clarifications

Condition O of MC7 PREREG §1 is adopted unchanged: O1 one state space Ω = 𝒞_V × 𝒞_H; O2 one dynamics, a composition of
bijections of Ω; O3 one source of probability, with the visible initial configuration a point mass fixed by the protocol
and μ_H independent of the settings; O4 configuration readout. O does not exclude K-PROG (V-8), which is why §4.3 exists.
- **Copies.** An N-copy experiment is one realization on the product carrier with any shared cells. Independence of
  copies is an assumption typed per reading (A-3, B-4).
- **Communication protocols.** Inputs, box inputs and the message are visible cells; each input value runs as part of
  the visible point mass; μ_H does not depend on inputs (Main.md:82 [Q]: "the Bell-violating branch adopted in §3.3
  retains measurement independence and relinquishes ontic parameter independence while preserving operational
  no-signaling"); the message moves by a bijection.
- **Interferometers.** Source, phase setting, path openings (each path open or blocked, a visible setting), the marker
  coupling, the recombination and the detector ports are visible cells. The marker is a register in the same Ω, coupled
  by a bijection, with no quantum rule in the hidden sector. Path is defined operationally, by blocking (V-7).

Checkpoint I-2 measures O. A realization that violates O counts neither for nor against any candidate.

***

## 3. OI premises available to the derivations

A derivation step cites premises from this list only. Anything else enters an assumption ledger and is typed under §10.

| id | premise | corpus text [Q] | status |
|---|---|---|---|
| C1 | non-zero coupling | Main.md:74: "hidden degrees of freedom affect the visible evolution at some accessible step — the conditional law of some visible transition depends on the hidden state" | diagnostic |
| C2 | memory persistence | Main.md:76 (as V-5) | physical-regime premise |
| C3 | sufficient capacity | Main.md:78; Main.md:486–488: "Conditioning on $X_t$: $X_{<t} \to H_t \to X_{>t}$ is a Markov chain. By data processing:" | [AT] `c3_necessity` (C3Necessity.lean:80) |
| C4 | history readback | Main.md:80: "two visible histories with the same current state induce different next-step laws, mediated through the hidden state"; and V-6 | the independent condition |
| P1 | Lemma 1 | Main.md:48: "The observer has finitely many distinguishable internal states, so the visible configuration space $\mathcal{C}_V$ is finite, with a discreteness scale $\epsilon$ providing a finite minimal cell volume." Main.md:62: "Of the structure above, only finite visible resolution is a theorem (Lemma 1)." | theorem (the paper's) |
| P2 | Lemma 2 | Main.md:50: "The observer is a proper subsystem: $V \subsetneq S$. The complement $H = S \setminus V$ is the hidden sector." | definition |
| P3 | Lemma 3 | Main.md:56: "a bijection: distinct states have distinct successors and predecessors"; "globally, the counting measure is selected among invariant measures as the maximal-entropy one". Main.md:60: "the counting measure is the default, not a constraint on representations". Main.md:62: "injectivity is the requirement that the dynamics preserve the observer's records" | posits (iii), (iv) |
| P4 | trace-out | Main.md:115–117: "let $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ be a bijection", with "\pi_V(\varphi(x_i, h)) = x_j". Main.md:522: "arises from marginalizing a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$" | theorem |
| P5k | the kernel's Shannon layer | FiniteEntropy.lean:383–385, `cmi_le_of_deterministic`: "cmi w a b (fun s => g (b s, c s)) ≤ cmi w a b c"; FiniteEntropy.lean:457–459, `cmi_le_log_card`: "cmi w a b c ≤ Real.log (Fintype.card γ)" | [AT]; natural-log units |
| P7 | the coupling-graph cone | Main.md:358: "Thus a setting intervention supported in region $A$ cannot alter a readout in region $B$ before the corresponding causal cones meet." Relative to Main.md:708: "(viii) site factorization — the configuration space is identified with a product of local configuration spaces over a set of sites" | theorem relative to (viii) |
| P8 | Bell ceiling hypotheses | Main.md:361–365: "(i) the dynamics is deterministic; (ii) the setting operations are"; "(iv) the interventions act on one common"; "pre-setting ensemble, so $p(\Omega\mid a,b)=p(\Omega)$" | theorem |
| P9 | branch (a) | Main.md:392: "at the microstate level, one wing's response depends on the remote setting. This is not an operational signal"; "a Bell preparation supplies bounded-degree long edges or an equivalent nonlocal response map" | adopted branch |
| P10 | operational no-signalling | Main.md:407: "a later local setting cannot produce an operational signal at the remote wing"; "Dropping that spatial/intervention structure returns the unrestricted OI behavior class, including PR, which is the mandatory negative control." | required |
| P11 | response-completeness | Main.md:405: "If $\Lambda$ is coarser than the response-relevant microstate, $I(\Lambda;Z)$ alone does not control CHSH" | stated requirement |
| P12 | implementation-fixedness | Main.md:550: "Each labelled instrument is one fixed map, applied whenever chosen, in every context; context enters only through the state." | gluing-theorem clause |
| P13 | reference geometry | SM.md:156: "is a sufficient sparsity condition for *typical local neighborhoods* to retain the reference graph geometry."; "This is not a theorem that $\kappa_{OR}$ converges everywhere" | diagnostic |
| P14 | information conservation and access | Substratum.md:44: "φ is a bijection: *perfect memory* — information is never created or destroyed."; "The partition $V$ defines the observer's *access* — both read and write." | construction premise |
| P15 | condition O and κ1–κ4 | MC7 PREREG §1; `mc-node3` [rec] | thread conditions |
| P16 | scope limits | Main.md:630: "It does not alone establish statistical product structure after conditioning, local tomography, or one common tensor-product instrument category."; Main.md:534: "exact coherent/composite compatibility is the residual operational-lifting problem" | stated limits |
| P17 | observer covariance | Main.md:668: "each partition satisfying the characterization conditions produces its own C1–C4-quantum description of the remaining degrees of freedom"; Main.md:674: "exists and is unique given $\varphi$. Its marginals reproduce Wigner's $T_W$ and Friend's $T_F$ respectively." | stated property |
| P18 | permutation unitary | Main.md:716: "the realization's permutation unitary, $\hat{H} = i\log U$, exact at integer horizon times for uniform, slice, and weighted priors" | proved |
| P20 | single controlled dynamics | Main.md:560 (as V-8) | corollary |
| P21 | canonical predictive quotient | Main.md:600: "**Theorem (canonical predictive quotient — a purification ingredient, substratum form).**" | theorem (substratum form) |

**Barred inputs** (checked by §14): E1 and any posited Hilbert-space, operator-algebra, Born-rule, amplitude or
quantum-instrument structure (the Koopman space ℓ²(Ω) of P18 is admitted because it is built from the substratum); E3
in its Hilbert-space reading (Substratum.md:92 [Q]: "E3, with the holographic bound read as a Hilbert-space dimension
cutoff"); Computation.md:130 [Q] ("realizable correlations are those approximable by finite-dimensional strategies");
the quantum-shadow realizations of Main.md:576–578; and, as premises, the quantum set, Q1 or any NPA level, TLM, 2√2,
the Tsirelson box, Tsirelson's vector representation, Born weights, the bridge V ≤ F_R and V² + D² ≤ 1. Main.md:356 [Q]
("the same reversible response-table construction that realizes arbitrary finite stochastic laws also realizes PR-box
behavior"; "The selector in a Bell experiment is therefore causal locality, not representability.") is respected, not
strengthened.

**Search under §A.19.** No corpus text mentions ML or IC (`git grep -i -E "information causality|macroscopic locality|local orthogonality|Navascu|Wunderlich|Pawlowski|Pawłowski"`
over `papers/*.md` and `book/*.md`; as MC7 PREREG §3.6). No corpus text states a fringe or complementarity law (V-1).
No corpus text states an information measure for the operational theory beyond Shannon information of record and
hidden variables (C3, P5k). A reviewer may add premises before step 2 (§17).

***

## 4. Order of work, and the mandatory countercontrols

### 4.1 Depth-first order

C5 first, then Q1 → Q2 → Q3 (3A, then 3B) → Q4 (§A.12). Each section has its own decision rule, verdict line and stopping
rule. A Failure in one does not cancel the others; all are reported. No verdict propagates to another section except
through a named step with its own premises and check, and each section's classifier reads only its own ledgers (I-23).
Common stopping rule: a section stops when each verdict line is decided or Parked with the gap named, or when a required
check exceeds §A.40's local bounds (then reported incomplete, moved to CI only with owner approval).

### 4.2 K-PR6, every route

- **Construction (node 6's B2, node 7's LE(1,1) [rec]).** Visible settings a, b, pointers q, r, preparers p₁, p₂; hidden λ
  ∈ {0, 1}, counting measure. Steps, each a bijection of Ω: p₁ ^= λ; p₂ ^= λ; q ^= p₁; r ^= p₂; r ^= a·b. Records A = λ
  and B = λ ⊕ ab: uniform marginals, no operational signalling, CHSH = 4. One reversible global update implements it,
  and its last step reads both settings.
- **K-PR6-RAC.** With box inputs x₀ ⊕ x₁ (Alice) and y (Bob), the outputs satisfy a ⊕ b = (x₀ ⊕ x₁)y. Alice sends m = x₀ ⊕
  a, and Bob outputs m ⊕ b = x_y: Σ_y I(x_y; G | y) = 2 bits on 1 bit sent.
- **Rule.** Every route carries a K-PR6 line, measured and printed: "rejected by premise X at step s" (premise quoted at
  file:line, violation exhibited exactly); "rejected only by the added axiom A" (Conditional at best); "rejected only by
  a Q-typed premise" (Reproduction); or "not rejected". A route whose conclusion bears on correlations or information,
  with "not rejected", fails as an OI derivation. Hidden reality, limited individual records, reversible dynamics and no
  observable signalling are all present in K-PR6, so a route using only these cannot reject it.

### 4.3 K-PROG, every Q2 route

- **Construction.** A deterministic apparatus in one Ω with one dynamics (Main.md:560): the marker copies a perfectly
  readable path bit, while a separate hidden register, read together with the phase setting, drives a phase-dependent
  output with a fringe-shaped law. Variants read the path-blocking settings too, so that blocked-path runs also look
  right. The K = 4 instance has V = 1 and D = 1.
- **Rule.** Every Q2 route carries a K-PROG line, of the same four kinds as K-PR6's. A route that does not reject K-PROG
  (with all its variants) does not distinguish a genuine interferometer mechanism from an apparatus programmed to output
  a fringe-shaped distribution, and fails Q2. A C1–C4 model with sinusoidal statistics shows Reproduction only.

***

## 5. C5 (candidate): consistent information across interventions and composites

Labelled **H-C5** throughout so that it cannot be confused with the corpus's (C1)–(C4). It is a candidate added
condition, not an OI premise.

### 5.1 Statement

Motivation: an observer's alternative ways of interrogating a system admit one consistent accounting of information,
including when the system interacts with others. C1–C4 describe how hidden information persists and affects
observations; H-C5 restricts how that information becomes accessible through different experimental choices.

The operational theory that OI generates admits an information quantity 𝓘(A : B) with, over all allowed states,
interventions and composites:
- (C5a) classical agreement: on ordinary recorded variables 𝓘 equals Shannon mutual information;
- (C5b) data processing: no allowed local operation on B increases 𝓘(A : B);
- (C5c) consistent composition: the chain-rule identities frozen below, not the bare phrase "obeys a chain rule";
- (C5d) nonnegativity and symmetry. Nonnegativity, not strict positivity: independent systems must be able to carry zero
  information.

**The identities and inequalities the C5 ⇒ IC proof uses, each a separate checkpoint (I-29).** A, B, C range over the
systems and composites of the declared domain; M is a classical message.
- (I1) the conditional quantity, by definition: 𝓘(A : B | C) := 𝓘(A : BC) − 𝓘(A : C). This imposes nothing
  substantive.
- (I2) decomposition consistency: 𝓘(A : BC) − 𝓘(A : C) = 𝓘(AC : B) − 𝓘(C : B).
- (I3) symmetry: 𝓘(A : B) = 𝓘(B : A).
- (I4) nonnegativity: 𝓘(A : B) ≥ 0 and 𝓘(A : B | C) ≥ 0.
- (I5) data processing: 𝓘(A : T(B)) ≤ 𝓘(A : B) for every allowed local operation T on B, and the conditional form
  𝓘(A : T(B) | C) ≤ 𝓘(A : B | C) where the proof uses it.
- (I6) classical agreement: on classical variables 𝓘 equals Shannon mutual information, including 𝓘(M : M) = H(M).
- (I7) the classical-target bound: 𝓘(Y : M) ≤ H(M) for classical M and any system Y.
- (I8) independence gives zero: 𝓘(A : B) = 0 when A and B are independent (product) systems.
- (I9) the iterated chain rule: 𝓘(X : BM) = Σ_i 𝓘(X_i : BM | X_{<i}), from (I1) applied repeatedly.

A construction that meets (I1) only by definition and fails (I2) does not satisfy (C5c). Mutation control KM-18 checks
that the checker catches such a measure.

This is an existing information-theoretic route to IC [L: Barnum, Barrett, Clark, Leifer, Spekkens, Stepanik, Wilce and
Wilke, NJP 12, 033024 (2010); Al-Safi and Short, PRA 84, 042323 (2011)], not a new theorem.

### 5.2 IC from H-C5: the derivation to be checked

Setup: independent uniform input bits X = (X_1, …, X_N) for Alice; an initially independent shared resource with
Alice's part A and Bob's part B; operational no-signalling; an m-bit classical message M; Bob's guess G_i for index i.
Target: Σ_i I_Sh(X_i : G_i) ≤ 𝓘(X : BM) ≤ H(M) ≤ m.

| step | statement | H-C5 property and other inputs | type |
|---|---|---|---|
| C5-S1 | I_Sh(X_i : G_i) ≤ 𝓘(X_i : B_{t₁}M): G_i is produced from (B_{t₁}, M) by Bob's local operation for index i | (I6), (I5) | [W] |
| C5-S2 | Σ_i 𝓘(X_i : B_{t₁}M) ≤ 𝓘(X : B_{t₁}M): by (I9), then for each i, 𝓘(X_i : B_{t₁}M \| X_{<i}) ≥ 𝓘(X_i : B_{t₁}M), using (I2), (I8) for the independent X_{<i}, (I4) and (I5) | (I2), (I4), (I5), (I8), (I9); independent inputs (D-1) | [W] |
| C5-S3a | 𝓘(X : B_{t₀}) = 0 at the slice t₀ before any input acts: initial independence | (I8); initial measurement independence (D-2) | [W] |
| C5-S3b | 𝓘(X : B_{t₁}) = 𝓘(X : B_{t₀}): Alice's operationally local intervention acts on Bob's system B as a local channel that leaves it unchanged, and B acquires no information about X before the message | (I5) on B; locality of Alice's intervention on B (D-3) | [W] |
| C5-S3c | 𝓘(X : B_{t₁}M) = 𝓘(X : B_{t₁}) + 𝓘(X : M \| B_{t₁}) | (I1), (I2) | [W] |
| C5-S4 | 𝓘(X : M \| B_{t₁}) = 𝓘(XB_{t₁} : M) − 𝓘(B_{t₁} : M) ≤ 𝓘(XB_{t₁} : M) ≤ H(M) ≤ m | (I2), (I3), (I4), (I7), as in [L]; re-derived in step 2. Any further identity the re-derivation needs is added to the list as (I10) and given its own checkpoint | [W] with [L] |
| C5-S5 | with repeated resources and protocol closure (nested random-access codes), IC excludes every box with S_max > 2√2; the PR random-access code fails IC at N = 2, m = 1 | repeated independent resources (D-4); wirings (D-5); the twirl's shared randomness (D-6); n → ∞ (D-7) [L: Pawłowski et al. 2009] | [W] with [EC] instances |

**Bob's system and its slices, declared for every route.** B is the system the route's 𝓘 is evaluated on (for example,
Bob's box half as an operational system, or a named set of hidden cells). t₀ is after preparation and before any input
acts; t₁ is after Alice's operations and before the message arrives; t₂ is Bob's readout. Each route states its B and
checks C5-S3a, C5-S3b and C5-S3c separately.

**Typed assumptions of the chain.**
- D-1 independent inputs: M (the game's definition).
- D-2 initial measurement independence of the resource from the inputs: O through O3 and P8 (iv). This is
  P(λ | x, y) = P(λ). Ontic parameter dependence (P9) does not violate it.
- D-3 locality of Alice's intervention on B: Alice's operationally local intervention is a local channel on the declared
  B, and B acquires no remote-input information before the message. P10 gives operational no-signalling for records;
  whether it gives D-3 for the declared B is the step-2 check.
- D-4 independent repeated resources: O under P-ctr for the product prior, A under P-dat; non-interaction A unless
  derived.
- D-5 wirings: O through κ4 feed-forward (P15).
- D-6 shared randomness: O (P3).
- D-7 the limit n → ∞: M.

### 5.3 The decisive obligation: can 𝓘 be built from OI's observer interface and shown to have (C5a)–(C5d)?

"One underlying reality" and finite memory do not prove H-C5; neither is accepted as a step. Each route below is tested,
not assumed to fail.
- **C5-0 (§0).** An OI-admissible PR-box model obstructs C5 only if it also satisfies the operational and composition
  assumptions that C5 ⇒ IC needs (D-1 to D-7, with B and its slices declared). Step 2 checks those assumptions on K-PR6
  itself, as a [W] with [EC]. Only if they hold does K-PR6 count as a model admitting no C5 measure. If they fail on
  K-PR6, the step at which they fail is recorded, and K-PR6 is not an obstruction to C5.
- **Negative route N-ont: Shannon information about the entire hidden microstate.** 𝓘_ont(A : B) = I_Sh(A ; full
  microstate of B's declared cells). Pre-registered reason it may fail: it includes distinctions the observer cannot
  access. Exact countercontrols: (1) two O-admissible realizations with identical record laws on every accessible
  protocol but different 𝓘_ont, which would show 𝓘_ont is not a quantity of the operational theory; (2) K-PR6 with its
  slices declared, recording whether C5-S3b fails for 𝓘_ont and in which mode: (i) Alice's operationally local
  intervention is not a local channel on the declared hidden cells, or (ii) those cells acquire remote-input
  information before the message. C5-S3a is checked separately and is not expected to fail on that account (D-2).
- **Negative route N-acc: accessible information.** 𝓘_acc(A : B) = max over single admissible readouts R of B of
  I_Sh(A : R). Pre-registered reason it may fail: it need not satisfy the chain rule. Exact countercontrol: a triple in
  OI realizations (𝒟_LE, 𝒟_RT, §8.3) violating (C5c) for 𝓘_acc. In quantum theory accessible information is not
  additive [L: DiVincenzo, Horodecki, Leung, Smolin and Terhal, PRL 92, 067902 (2004), locking]; that theorem concerns
  quantum theory, not OI's interface, so without an exact OI countercontrol the route is Parked, not refuted.
- **Positive route P-pq: Shannon information of the predictive quotient.** 𝓘_pq(A : B) = I_Sh(A ; T_B), with T_B
  the canonical predictive quotient of B's region (P21): hidden data modulo distinctions that no accessible protocol on
  B reveals. Point at which it is judged: whether quotients of composites are compatible with quotients of their parts
  ((C5c)), and whether (C5b) holds when B is acted on. K-PR6 is its first test.
- **Positive route P-ms: measured information over admissible readouts.** 𝓘_ms built from the Shannon entropies of
  B's admissible readouts [L: Short and Wehner, NJP 12, 033023 (2010), measurement entropy]. Point at which it is judged:
  whether the chain rule holds; [L] reports it can fail in general theories.

### 5.4 Verdict line H-C5 and what it settles

- **H-C5 is an existence claim. Verdict table, fixed now.**

  | finding | verdict printed |
  |---|---|
  | N-ont fails a required identity, or fails C5-S3 on a model that meets the chain's assumptions | "the hidden-state Shannon construction fails" (that construction only) |
  | N-acc fails a required identity | "the accessible-information construction fails" (that construction only) |
  | no construction found that meets every requirement, and no obstruction shown | "Undetermined". This is not a Failure, and the class is Parked with the gap named |
  | an OI-admissible model is shown to admit no measure meeting (C5a)–(C5d) and (I1)–(I9), and that model is shown to meet D-1 to D-7 itself | "OI does not imply C5", with the model. Adopting H-C5 then excludes that model, and the correlation lines read "Conditional on H-C5" |
  | a construction meets every required property on a declared domain (its states, interventions and composites stated) | "C5 established on domain 𝔇", with 𝔇 stated. The correlation lines may then reach "IC derived on 𝔇", subject to the circularity review and the K-PR6 line |

- **Adoption criterion, separate from mathematical correctness (a verdict-generator clause).** A Conditional line that
  adopts H-C5, or any other added axiom, also needs an established further consequence. The consequence must be derived
  from the axiom with OI's premises, independently testable (by an exact check or a raw-direct statistic under §A.24),
  and must extend beyond the CHSH target used to motivate the axiom. It need not contradict QM. Candidate consequences
  are evaluated from the measured lines (for example (b3), (b4), (b5) or a Q2 statement), never asserted. If none is
  established, the line reads "Conditional; additional-consequence requirement unmet". Mutation control KM-19 checks
  that the generator cannot print a bare "Conditional" in that case.
- **What H-C5 settles, fixed now.**
  - Excluding PR boxes: yes (C5-S5 at N = 2).
  - The CHSH upper bound: yes, with protocol closure (D-4 to D-7).
  - Achievability of quantum boundary values in OI: not settled; it needs a construction (Q4's (ii-Q)).
  - The quantitative interference–path trade-off: not established by this argument (Q2).
  - Full operational QM: not established.
  - Classical theory satisfies H-C5 as well, so a bound alone cannot show that OI reaches the quantum boundary.
- **Recorded alternatives, not pursued as primary.**
  - Information–disturbance: it holds in broad operational theories, and fixes neither the amount nor the quadratic law
    [L].
  - Purification with essential uniqueness [L: Chiribella, D'Ariano and Perinotti, PRA 84, 012311 (2011)]: the
    reconstruction needs five further axioms, and an ordinary hidden-variable completion is not automatically a
    purification. Earlier nodes flagged it as an added premise needing a source (V-9: PLAN.md:121–122;
    mc-node3/NODE.md:232–233; mc-node5/NODE.md:263, :344–346; node 4's E7 [rec]).

***

## 6. Q1: what do C1–C4 constrain across interventions?

### 6.1 Three claims, kept distinct

- (i) hidden information predicts future observations;
- (ii) an intervention physically changes hidden records and their later influence;
- (iii) acquiring path information necessarily reduces interference by a particular amount.

C4 gives (i) (V-6). (ii) needs a physical mechanism; (iii) needs a quantitative restriction on that mechanism. Q1
records, for each premise, which of (i)–(iii) it supplies.

### 6.2 Candidate restrictions and their test

For each of C1, C2, C3, C4, P3 (bijectivity), P7, P10, P12, P14 and P20, Q1 states the strongest restriction on how the
response rule under one intervention relates to the response rule under another on the same system, as a [W] statement
with its assumptions explicit.
- **Progress criterion.** A restriction counts iff it excludes K-PR6 or K-PROG exactly (with every variant) while
  admitting the classical controls (K-C) and the quantum controls (K-Q, CC-q of §7.4).
- **Otherwise** the premise is recorded as giving "no cross-intervention restriction beyond R", with an exact
  countermodel that satisfies the premise and realizes K-PR6 or K-PROG. P20 (one dynamics with a program register) is
  the first such test.
- C1–C4 are checked in their exact corpus statements per realization (K-C1C4, I-25). If C4 cannot be engaged in a
  one-shot architecture without a temporal embedding the corpus does not specify, the item is Parked with that embedding
  named (as MC7 PREREG §3.6 records).

### 6.3 Q1 verdict line and stopping rule

One line per premise: (i)/(ii)/(iii) supplied or not; the restriction derived, or the countermodel; its K-PR6 and
K-PROG lines; the class under §13. The section stops when every premise's line is decided or Parked. If no premise
yields a restriction, Q1's result names the restriction that would be needed as a candidate missing physical
principle (H-C5 is one), and Q2–Q4 test it as Conditional.

***

## 7. Q2: does that restriction explain complementarity?

Interference is a diagnostic here, not a target. A cos-law test enters only as part of K-PROG discrimination (§7.4).

### 7.1 The mathematics fact (not evidence for OI)

For equiprobable paths and an actual marker readout R with conditional laws p₀, p₁ on its outcomes:
D_R = ½ Σ_r |p₀(r) − p₁(r)| and F_R = Σ_r √(p₀(r) p₁(r)).

**Lemma.** D_R² + F_R² ≤ 1.
*Proof* [W]. Write s_r = √p₀(r) and t_r = √p₁(r), so Σ s_r² = Σ t_r² = 1. Then |p₀ − p₁| = |s_r − t_r| (s_r + t_r).
By Cauchy–Schwarz, Σ_r |s_r − t_r|(s_r + t_r) ≤ (Σ_r (s_r − t_r)²)^{1/2} (Σ_r (s_r + t_r)²)^{1/2}. Expanding,
Σ (s_r − t_r)² = 2 − 2F_R and Σ (s_r + t_r)² = 2 + 2F_R. Hence 2D_R ≤ 2(1 − F_R²)^{1/2}, that is, D_R² + F_R² ≤ 1.
∎ This is the Fuchs–van de Graaf-type bound [L: Fuchs and van de Graaf, IEEE Trans. Inf. Theory 45, 1216 (1999)].
Step 2 re-checks the two expansions and the factorization symbolically as K-LEM. It is mathematics and carries no
evidence about OI.

### 7.2 Operational definitions, inside the substratum

- **Path, by blocking.** p_j^R is the law of marker readout R when only path j is open, with the same preparation and
  the same marker coupling (V-7). Paths are equiprobable.
- **V, from unconditional counts.** With both paths open, V = (P_max − P_min)/(P_max + P_min) over the phase settings
  θ ∈ Θ_K, K ∈ {4, 6, 8, 12}, of the detection frequency at port 0. V is computed from the record law, never set equal
  to an overlap or to F_R.
- **D, over every admissible readout.** D = max over admissible marker readouts R of D_R. Complementarity concerns path
  information potentially available in the physical marker, whether or not anyone reads it [L: Englert, PRL 77, 2154
  (1996)]. Concealing an existing record from the observer does not restore interference. So D is the distinguishability
  available in the marker under every readout the operational theory admits (configuration readouts after any
  accessible bijection on the marker and ancillas, κ4), not what the observer happens to read. Inaccessible ontic
  knowledge is not used.
- **Eraser fringes, separate.** Fringes conditioned on a marker readout outcome (quantum-eraser fringes) are computed
  separately, as control K-ERASE, and never enter V.

### 7.3 The missing physical statement, and Q2's target

- **Bridge B-VF, to be derived and never assumed.** V ≤ F_R for the apparatus concerned and every admissible marker
  readout R, that is, V ≤ inf_R F_R. With the lemma applied at the readout R* that maximizes D_R, D² = D_{R*}² ≤ 1 −
  F_{R*}² ≤ 1 − V², so V² + D² ≤ 1.
- **An upper bound, not a saturation claim.** In quantum theory, for the balanced unconditional two-path setup, V ≤
  F_q(ρ₀, ρ₁) = inf_R F_R, where F_q is the root fidelity of the conditional marker states and the infimum runs over
  marker measurements; the standard equality takes the infimum over all POVMs [L: Fuchs and van de Graaf 1999]. The
  optimal readout attains the fidelity bound. It does not make the visibility equal to it: further loss of coherence can
  give V < F_q, and equality needs a pure marker and no further decoherence. Node 8 asserts no equality V = F_R at any
  readout; control CC-dec (§7.4) guards against confusing the upper bound with an achievable visibility.
- **What does not count.** Defining V to equal the overlap, or inserting quantum amplitudes to obtain the link, assumes
  the bridge (Reproduction).
- **Q2's precise target.** Which property of the shared substratum forces distinguishable path records to limit the
  observable interference response? C1–C4 identify the memory-bearing setting but do not supply the relation (V-4, V-6).
  Q2 tests each restriction Q1 produced, and H-C5 if adopted, for whether it implies B-VF on its admitted class.

### 7.4 Q2 decision rule, controls, verdict line and stopping rule

A candidate restriction explains complementarity iff all of the following hold:
- it implies B-VF for every realization in its admitted interferometer class, by a reviewed [W] with [EC] instances
  (response-table, hidden-memory and reference-update subclasses; hidden carriers up to 2^12; marker registers up to 4
  bits);
- it rejects K-PROG with all variants (K-PROG line, §4.3). The discrimination fixed now: with one path blocked the
  detection law must not depend on θ; with three paths, Sorkin's I₃ = P₀₁₂ − P₀₁ − P₀₂ − P₁₂ + P₀ + P₁ + P₂ − P_∅ must
  vanish while I₂ ≠ 0 [L: Sorkin 1994; Sinha et al. 2010, cited at Structure.md:1312]; and the both-open law at θ ∈ Θ_K
  must be ½(1 + V cos(θ − θ₀)) with V and θ₀ fixed by the realization before the pattern is computed. A variant that
  meets all three by reading the setting registers is still K-PROG, and only a restriction on response rules across
  interventions rejects it;
- quantum boundary points are achievable in its admitted class: for c ∈ {0, 1/2, 1/√2, 1}, a realization with V = c and
  D = √(1 − c²) exactly, constructed, not assumed. These are the pure-marker, no-further-decoherence points; achieving
  them is a separate construction, and a derived B-VF alone does not supply it;
- the controls behave as stated:
  - CC-hm, a hidden-memory model with the path recorded in a marker and context-dependent dynamics giving V = 1 with D = 1.
    Its C1–C4 status is computed in the exact statements. If it satisfies C1–C4, C1–C4 do not exclude it;
  - CC-w, a classical wave with polarization marking, computed from Jones vectors. It satisfies V² + D² ≤ 1, with
    equality for full polarization [L: Eberly and coworkers, 2016–2017], which shows that the inequality alone is not
    QM-selective;
  - CC-q, the quantum path–marker model computed from density matrices. It gives equality at pure marker states [L:
    Greenberger and Yasin, Phys. Lett. A 128, 391 (1988); Englert 1996];
  - CC-dec, computed exactly from density matrices: path state |+⟩, marker state I/2, and a coupling that applies I to
    the marker on path 0 and Z on path 1. Both conditional marker states are I/2, so F_R = 1 for every readout and D = 0.
    The path coherence is multiplied by tr[(I/2)Z] = 0, so V = 0. B-VF holds with V strictly below inf_R F_R. The
    checker must report V = 0 and inf_R F_R = 1 here, and must not report the bound as attained;
  - K-ERASE, eraser fringes computed separately.

  The positive controls are computed from their own models, never from the formula.

Verdict line Q2: the class (§13) of each candidate restriction, with its K-PR6 and K-PROG lines. Q2 cannot by itself
reach any correlation verdict (§9.4). Stopping rule: every candidate's line decided or Parked.

***

## 8. Q3: does it imply IC (3A) or ML (3B)?

Each sub-question needs its own derivation from named OI premises, with the Q1 restriction or H-C5 entering as a named
premise or a named added axiom. Finite memory (C3, P1) may not stand in for either principle: a step that cites only
capacity to bound information across alternative interventions is rejected by the circularity review (§14 item 21).

### 8.1 3A: information causality

- **IC-Sh (decision statement).** Σ_{i=1}^{N} I(a_i; G | b = i) ≤ m, Shannon mutual information in bits, for N
  independent uniform bits, an m-bit message and shared resources. The measure is the corpus's own (C3, P5k), and is a
  reading choice fixed now. Rényi-2 and min-entropy rows are sensitivity rows; they decide nothing.
- **IC-G, distinct from IC-Sh, amendment-gated.** Gachechiladze and Miklin [L-c] derive the TLM boundary from a
  generalized IC with correlated inputs and full receiver transcripts; their exact-selection result concerns the
  two-setting binary correlator region, including the zero-marginal case. It is not a reconstruction of arbitrary
  quantum experiments, and it is not promoted to one here. IC-G's statement is to be fixed from the paper before
  execution (PC-GM, §9.3). The OI-to-IC derivation stays open whichever form is used.
- **IC on boxes.** A box is IC-excluded iff a protocol in 𝒫 (P-vD, N = 2, m = 1, the K-PR6-RAC protocol; P-RAC(n), 1 ≤ n ≤
  12, nested codes with 2^n − 1 boxes; each optionally preceded by the twirl, O-admissible by [W]) gives a certified
  excess. A box is IC-admitted iff it is local (classical IC [W]) or has an exhibited exact quantum realization (quantum
  IC [L], a control only). Every other box is IC-undetermined and counts for no clause.
- **Bob's system and slices.** t₀ is after preparation and before any input acts; t₁ is after Alice's operations and
  before the message arrives or Bob's input acts; t₂ is Bob's readout. The decision reading IC-ont takes B = B_{t₁}:
  every cell in the backward cone of Bob's guess pointer, at slice t₁, except M's cells and Bob's input (P7, P11). Each
  route states its B; IC-rec takes Bob's records R_B instead.
- **Derivation route.** Each step is checked separately, and the ledger records which step fails, if any.

| step | conclusion | premises | type |
|---|---|---|---|
| IC-D1 | H(M) ≤ m | P1, P15 (O4) | [W]; [AT] `cmi_le_log_card` |
| IC-D2 | every record variable and B_{t₁} is a function of the microstate; Shannon information is defined for all | P3, P4, P15 | [W] |
| IC-D3 | between t₁ and t₂, G is a function of (M, B_{t₁}, b) alone, so I(a_i; G \| b = i) ≤ I(a_i; M, B_{t₁} \| b = i) | P7, P11; data processing | [AT] `cmi_le_of_deterministic`, [W] for the functional dependence |
| IC-D4 | Σ_i I(a_i; M, B_{t₁} \| b = i) ≤ I(a⃗; M, B_{t₁}) | chain rule [W]; P8 (iv), O3 | [W] |
| IC-D5a | I(a⃗; B_{t₀}) = 0: initial measurement independence | O3, P8 (iv) | [W] |
| IC-D5b | I(a⃗; B_{t₁}) = 0: Alice's operationally local intervention acts as a local channel that leaves B unchanged, and B acquires no remote-input information before the message | routes σ-cone, σ-ons, σ-cap, σ-Q1, σ-C5 | to be decided: the record-limitation step, across alternative questions |
| IC-D5c | I(a⃗; M, B_{t₁}) = I(a⃗; B_{t₁}) + I(a⃗; M \| B_{t₁}) ≤ I(a⃗; B_{t₁}) + H(M) | Shannon identities and P5k | [AT] with [W] |
| IC-D6 | on i.i.d. copies with wirings, IC-Sh excludes S_max > 2√2 and admits TB | [L: Pawłowski et al. 2009] replayed: the twirl [W], P-RAC closed forms [W], the binary-entropy bound [L, mathematics], exact algebra at 2E² = 1 | [W] with [EC] |

- **Where a hidden-state route can fail, named in advance.** Ontic parameter dependence (P9) is not a failure of
  IC-D5a: P(λ | x, y) = P(λ) holds on branch (a) (Main.md:82). A hidden-state route can fail instead because (i) an
  operationally local intervention of Alice is not a local channel on the declared B, which shows at IC-D3 (G then
  depends on Alice's cells after t₁) or at IC-D5b; or (ii) B acquires remote-input information before the message,
  which shows at IC-D5b. The ledger records which step fails, in which mode, on which model, with B and the slices
  stated.
- **Routes at IC-D5b (and IC-D3).**
  - σ-cone: the cones do not meet before t₂ (P7, P8). Judged against P9: does any step between t₀ and t₂ read Alice's
    cells and write into B or into G's inputs? K-PR6-RAC is the first test.
  - σ-ons: operational no-signalling (P10) gives I(a⃗; R_B) = 0 for Bob's records. Judged on whether substituting R_B
    for B is valid at IC-D3 (P11).
  - σ-cap: a capacity bound (P1, C3, P5k) on the cells through which a⃗ reaches B or G. Judged on whether OI fixes
    that number; a free constant is Failure-as-stated. V-3 is tested here, not assumed.
  - σ-Q1: the restriction Q1 produced, if any.
  - σ-C5: H-C5 through C5-S3a to C5-S3c, as a named added axiom (Conditional) unless §5.3 establishes it.
- **Assumptions.** B-1 Shannon measure (reading choice); B-2 independent uniform inputs (M); B-3 m classical bits (O);
  B-4 independent copies (O under P-ctr, A under P-dat; non-interaction A unless derived); B-5 wirings (O, κ4); B-6
  twirl randomness (O, P3); B-7 n → ∞ (M); B-8 locality of Alice's intervention on the declared B, the conclusions of
  IC-D3 and IC-D5b (to be derived; otherwise A). If B-8 is adopted for a response-complete B with deterministic
  dynamics, the resulting admitted set may coincide with that of ontic parameter independence, which Main.md:361–365
  bounds by 2. Step 2 computes B-8's conditional admitted set rather than assuming either outcome. B-9
  response-completeness (O, P11).
- **Readings.** IC-ont (B = B_{t₁} as above; decision reading); IC-rec (B replaced by records, route σ-ons); P-ctr and
  P-dat for B-4.

### 8.2 3B: macroscopic locality

- **ML-NW (formalized on boxes, coded from the covariance).** Over N i.i.d. copies, the normalized count fluctuations
  F_{A,a}, F_{B,b} have Gaussian limits with Var F_{A,a} = P(0|a)(1 − P(0|a)) and Cov(F_{A,a}, F_{B,b}) = P(00|ab) −
  P(0|a)P(0|b). P satisfies ML-NW iff some same-wing covariances make the 4 × 4 matrix PSD. The NPA level-1 moment
  matrix is a second code path (K-ML); the Schur complement makes ML-NW ⇔ Q1 an in-house box-level statement [W].
- **ML-F2 (fixed-register reading of Lemma 1).** One record bit per wing per run, by thresholds on the normalized
  fluctuations, one per wing and setting, universally quantified. Step 2 records by [W] whether the intersection over
  all finite registers equals ML-NW.
- **Derivation route.**

| step | conclusion | premises | type |
|---|---|---|---|
| ML-D1 | each wing's N-copy record is a visible configuration of a finite register | P1, P2, P4, P15 | [W] |
| ML-D2 | the record is the count per port at resolution N^{1/2} | P1; A-1, A-2 | [W] given A-1, A-2 |
| ML-D3 | the copies are i.i.d. | P3, P12; A-3 | [W]; A-3 unless derived |
| ML-D4 | the limiting macroscopic records admit a Bell-local model. The record-limitation step, across alternative settings | routes ρ-cone, ρ-geom, ρ-read, ρ-Q1 | to be decided |
| ML-D5 | the limit is Gaussian with the covariance above, and ML-D4 ⇔ the PSD completion | CLT [L, mathematics]; joint models for Gaussian marginals [W]; Schur complement [W] | [W] |
| ML-D6 | PSD completion ⇒ S_max ≤ 2√2 | exact level-1 sum of squares [EC, rec in MC7] | [EC] |

- **Routes at ML-D4.** ρ-cone (P7, P8 applied to macroscopic records, judged against P9; K-PR6 with N copies first);
  ρ-geom (P13, judged on whether "typical local neighborhoods" concerns the copies the record sums over, each of which
  carries its own long edge); ρ-read (P15, O4: a joint distribution exists for each setting pair, judged on whether one
  follows across setting pairs); ρ-Q1 (the Q1 restriction, if any).
- **Assumptions.** A-1 count map (A unless derived); A-2 α = 1/2 (A; sensitivity rows at α ∈ {1/3, 2/3}; if its only
  justification is that it makes quantum correlations macroscopically local [L-s: Gallego–Dakić v1], the reading is
  Reproduction at best); A-3 i.i.d. (O under P-ctr for the product prior, A under P-dat; load-bearing for quantum
  admission, since quantum correlations violate ML without it [L-s: Gallego and Dakić, PRL 127, 120401 (2021)]); A-4
  the limit with observers growing with N (M, and O under L1-a); A-5 CLT (M); A-6 the locality claim (to be derived;
  otherwise A, and the reading is Conditional on ML).
- **Readings.** L1-a (per-observer finiteness, family form; ML-NW); L1-b (one fixed observer; ML-F2); P-ctr, P-dat;
  α ∈ {1/3, 1/2, 2/3}, only 1/2 decision-bearing.

### 8.3 Countermodel classes (Q1, Q3, C5)

𝒟_LE: LE(n, k) with N copies, n ≤ 12, N ≤ 6 exactly, with [W] for N → ∞. 𝒟_gate: node 7's long-edge gate class (256
Boolean F, control register n ≤ 12). 𝒟_RT: response-table realizations of 𝒜_CHSH(n), n ≤ 12, with branch-(a) long edges.
IC games embed N ∈ {2, 4}, m = 1. Every realization goes through the condition-O engine.

### 8.4 Q3 verdict lines and stopping rule

Per reading of 3A and of 3B, separately: the derivation verdict (§10), outcome (a) (§9), the (b) lines, the K-PR6 line,
and the class (§13). Neither sub-question's result is used in the other's derivation. Stopping rule: each stops when its
record-limitation step is decided or Parked for every route and its clauses are evaluated.

***

## 9. Q4: does it constrain composites correctly?

### 9.1 Outcome (a), Tsirelson's bound

Inherited in structure from MC7 PREREG §4, tightened to A1 (§1). It is evaluated on each line's admitted set as
formalized, whatever its derivation verdict.
- **Scenario.** Binary settings and outcomes; correlators E(a, b); S_max over the eight CHSH orientations. Named boxes:
  PR (K-PR6's box); TB, the Tsirelson box, P(x, y | a, b) = (1 + (−1)^{x⊕y⊕ab}/√2)/4 in ℚ(√2), realized by the
  maximally entangled two-qubit state with A₀ = Z, A₁ = X, B₀ = (Z + X)/√2, B₁ = (Z − X)/√2; T1 = LE(5, 2), correlators
  (1, 1, 1, 1/5), post-quantum [rec, K-7]; LE(√2 − 1), S_max = 2√2, post-quantum; the 16 local vertices; NS.
- **Family stage** over LE(n, k) (n ≤ 100), LE(w) for real w, and T1: (i) no admitted member has S_max > 2√2 (for IC,
  every such member certified IC-excluded); (ii-S) S_max = 2√2 attained exactly by an admitted member, or else by a box
  of NS; (iii) every classical record law admitted.
- **Follow-up on NS**, iff the family stage passes: (F1) sup S_max ≤ 2√2 over admitted boxes, by a reviewed [W] with
  [EC] instances (𝒜_CHSH(n), n ≤ 12; node 7's grid, n ≤ 100); (ii-Q) TB admitted exactly; (iii-𝒜) every local box
  admitted. For IC, admission means certified IC-admission, an IC-undetermined box with S_max > 2√2 makes (i) or (F1)
  incomplete, and an undetermined box counts for no admission clause.
- **(a) is established** iff (i), (ii-S), (iii), (F1), (ii-Q) and (iii-𝒜) all hold. Classes are never reduced after a
  result.

### 9.2 Composite routes, (b-corr) and (b)

- **Q4-VR.** A box is VR-admitted iff its correlator matrix has unit vectors u_x (x only), v_y (y only) in a real
  inner-product space with E_xy = ⟨u_x, v_y⟩. VR ⇒ S_max ≤ 2√2 by Cauchy–Schwarz [W]. VR is exactly the quantum
  correlator set for binary outcomes: quantum ⇒ VR in house [W]; VR ⇒ quantum [L: Tsirelson 1980, 1987]. Requiring a
  joint distribution of all records restores 2 [L: Fine 1982] (control K-LHV, must under-generate). Routes from OI: V-K
  (P18: vectors in ℓ²(Ω) built from √μ; judged on whether u_x can depend on x alone under P9; drafting observation: a
  permutation-conjugated diagonal operator stays diagonal); V-W (P17, P16: a common local operator representation is
  Q-typed unless derived); V-M (via 3B, with its own step V-M-1). Each route carries a K-PR6 line.
- **(b-corr).** The admitted correlator set equals the quantum correlator set, by a reviewed proof of both inclusions
  (§A.34), with its [L] dependence printed. ML and VR can at most reach (b-corr).
- **(b).** The admitted set of boxes, marginals included, equals Q, by a reviewed proof of both inclusions. Finite tests
  only refute it or record exclusions. (b-corr) is never reported as (b) (I-27). ML-NW = Q1 at the box level, and Q1 ⊋ Q
  with nonzero marginals [L: Navascués, Pironio, Acín 2008], so ML cannot establish (b). IC's admitted set is not known
  [L], so (b) for IC is reported only as exclusions.

### 9.3 Branch-4 tests, run on every line that established (a), and on K-P

- (b1) zero marginals, two settings: T1, the LE members with 0 < w ≤ √2 − 1, and the zero-marginal boxes of 𝒜_CHSH(n), n
  ≤ 12, with certified TLM violation [L: Tsirelson 1980; Landau 1988, for quantum ⇒ TLM].
- (b2) nonzero marginals: an exact point in Q1 outside Q (exact PSD moment matrix; exact rational NPA 1+AB dual), search
  over tilted CHSH I_β, β ∈ {1/2, 1} [L: Acín, Massar, Pironio 2012] and 𝒜_CHSH(n), n ≤ 12; if none is found, (b2) is
  incomplete.
- (b3) chained, three settings: I₃ ≤ 3√3 [L: Wehner 2006], attainment reported.
- (b4) the Q1 points that violate IC [L-s: Cavalcanti, Salles and Scarani, Nat. Commun. 1, 136 (2010)], if reproducible
  exactly.
- (b5) the three-setting counterexamples of Pompili and Weilenmann [L-c]: sets in the (3,3;2,2) scenario that satisfy IC
  at every database size and contain post-quantum points, and a family P_m for every m ≥ 3, reported with I = 1/m. The
  paper reportedly states that its proof does not need an entropy with all the properties the general-theory proof of IC
  uses [L-c]. So these sets obstruct IC from selecting QM, but they do not settle whether the models admit the full C5.
  Two lines, kept apart:
  - (b5-IC): each point tested against every IC-type input line (IC-Sh, and IC-G if PC-GM is met);
  - (b5-C5): the full H-C5 requirements ((C5a)–(C5d), (I1)–(I9), and D-1 to D-7 for the C5 ⇒ IC chain) checked on
    the model. A correlation table alone does not fix the transformations and composites C5 must hold on, so the test
    declares the completion it uses (state space, transformations, composites). If the paper fixes none, (b5-C5) is
    Parked, or gated by PC-PW until an amendment fixes one from the paper.

  The exact points and any completion are to be fixed from the paper before execution (PC-PW).
- (b6) POM: node 7's bound and quantum witness [rec]; "silent" for lines whose statement does not address POM.
- (b7) bipartite scope only [L: Gallego, Würflinger, Acín and Navascués 2011].
- **Amendment gates.** PC-PW: before (b5) runs, an amendment quotes the points, and any completion the paper fixes
  (state space, transformations, composites), from the paper with page and equation numbers. PC-GM: before IC-G runs, an amendment quotes the generalized IC statement and maps it onto §8.1's game. Until
  then each prints "not run (precondition unmet)". No number is entered from memory or from an abstract (I-28).

### 9.4 The step Q2 → Q4

A complementarity result does not supply composite structure. A line that uses a Q2 result toward Q4 must carry its own
step, with named premises, connecting the single-system restriction to the composite one (for example through
measurement uncertainty and steering [L: Oppenheim and Wehner 2010]), with its own K-PR6 line. Without that step, Q2
results are reported as "does not bear on correlation limits".

### 9.5 Q4 verdict lines and stopping rule

For each line (from H-C5, Q1, 3A, 3B, Q4-VR): (a), (b-corr), (b) and the branch-4 table, each as certified-admitted,
certified-excluded or undetermined per test point, and the class. Stopping rule: every line decided or Parked, gated tests
excepted.

***

## 10. Typing assumptions, and derivation verdicts (all sections)

- **M** mathematics applied to objects the premises fix ([L] allowed only here). **O** supplied by a step citing §3,
  closed by [AT] or reviewed [W]. **A** physical and not supplied: a named axiom, which makes the result Conditional.
  **Q** a barred input, which makes the result Reproduction.
- A parameter that OI does not fix and that this file does not fix in advance is Failure-as-stated. A parameter fixed in
  advance here (α = 1/2; the measure B-1; the phase alphabets K) is A-typed when OI does not supply it, and tuned (Q or
  Reproduction) when its only justification is the quantum target.
- A derivation verdict is one of: derived; conditional on named A-typed assumptions; refuted at step k (every route at k
  has an exact countermodel); Parked at step k. It is computed from the step ledger (I-14), which lists per step and
  route the premises cited, the type, the K-PR6 line (and K-PROG for Q2), and the argument or countermodel.
- Derived iff every step is closed by [AT] or reviewed [W] ([L] for mathematics only) for every O-admissible
  realization in scope satisfying the cited premises, every assumption is M or O, and the K-PR6 line names an O-typed
  premise.

***

## 11. Literature, with what is and is not known

- *Complementarity:* Greenberger and Yasin 1988 [L]; Englert 1996 [L] (path information available in the marker,
  whether or not read; equality for pure states); Jaeger, Shimony and Vaidman, PRA 51, 54 (1995) [L]; classical
  polarization optics satisfies the same relation [L: Eberly and coworkers 2016–2017]; Fuchs and van de Graaf 1999 [L].
- *Third-order interference:* Sorkin 1994 [L]; Sinha et al. 2010 [L], as cited at Structure.md:1312.
- *Nonlocality, uncertainty and steering:* Oppenheim and Wehner, Science 330, 1072 (2010) [L].
- *Information-theoretic route to IC:* Barnum et al. 2010 [L]; Al-Safi and Short 2011 [L]; Short and Wehner 2010 [L];
  Dahlsten, Lercher and Renner, NJP 14, 063024 (2012) [L-s]; locking of accessible information, DiVincenzo et al. 2004
  [L].
- *IC:* Pawłowski et al., Nature 461, 1101 (2009) [L]; Allcock, Brunner, Pawłowski and Scarani 2009 [L]; Cavalcanti,
  Salles and Scarani 2010 [L-s]; Navascués, Guryanova, Hoban and Acín 2015 [L] (whether the almost-quantum set satisfies
  IC is open).
- *Recent IC results [L-c]:* Gachechiladze and Miklin, arXiv:2609.10508 (2026): the TLM boundary from a generalized IC
  with correlated inputs and full receiver transcripts, an exact-selection result for the two-setting binary correlator
  region, including zero marginals. Related: arXiv:2606.02416; arXiv:2602.10206; Jain, Gachechiladze and Miklin, PRL
  (2024), arXiv:2308.02478. Pompili and Weilenmann, arXiv:2610.06604 (2026): IC-satisfying sets with post-quantum points
  in (3,3;2,2) and for all m ≥ 3; all known IC formulations fail to characterize the quantum set; the proof reportedly
  does not need an entropy with every property of the general-theory IC proof, so it does not settle full C5.
- *ML:* Navascués and Wunderlich, Proc. R. Soc. A 466, 881 (2010) [L-s]; Q1 ≠ Q [L: Navascués, Pironio, Acín 2008];
  Gallego and Dakić 2021 [L-s] (non-i.i.d. quantum correlations violate ML).
- *Tsirelson's theorem* [L: Tsirelson 1980, 1987]; *Fine's theorem* [L: Fine 1982]; *reconstructions* [L: Chiribella,
  D'Ariano and Perinotti 2011].
- *Mathematics used as [L]:* the multivariate CLT; joint models for Gaussian marginals; the CHSH sum of squares (exact
  in MC7 [rec]); 1 − h((1 + x)/2) ≥ x²/(2 ln 2).

***

## 12. Controls and mutation controls

Every control runs before any verdict of the section it serves; a verdict over a failed control is void; verdict text
is generated from measurements and ledgers.

| # | control | serves | type | expectation |
|---|---|---|---|---|
| K-PR6 | §4.2's construction through the condition-O engine; then each route's line | all | must-hold replay; line printed per route | replays |
| K-PR6-RAC | Σ_y I(x_y; G \| y) = 2 on m = 1, exactly | C5, Q1, Q3, Q4 | must-hold replay; must be rejected by every IC line, premise named | replays |
| K-PROG | §4.3's construction and variants, V = 1, D = 1 at K = 4 | Q1, Q2 | must-hold replay; line printed per Q2 route | replays |
| K-9 | condition O on every realization | all | must-hold | holds |
| K-C1C4 | C1–C4 checker: the coin–die example (book ch01 §1.5) satisfies C1 and C4; a Markov chain fails C4; a zero-coupling realization fails C1; the tape-and-ledger fair coin satisfies C1–C3 and fails C4 [rec] | Q1, Q2 | must-hold both ways | as stated |
| K-LEM | the lemma's factorization and the two expansions, symbolically; a random exact rational instance | Q2 | must-hold | holds |
| K-VD | V from counts and D_R, F_R from marker record laws, by two code paths, on a model with known laws | Q2 | must-hold | holds |
| CC-hm | §7.4's hidden-memory model; its C1–C4 status computed exactly | Q1, Q2 | countercontrol, outcome measured | reported |
| CC-w | classical polarization wave from Jones vectors | Q2 | must satisfy V² + D² ≤ 1, equality at full polarization | satisfies |
| CC-q | quantum path–marker model from density matrices, c ∈ {0, 1/2, 1/√2, 1} | Q2 | must give equality exactly | equality |
| K-ERASE | eraser fringes computed separately, never entering V | Q2 | must-hold | separate |
| K-ONT | two O-admissible realizations with identical accessible record laws, checked for whether 𝓘_ont differs | C5 | countercontrol for N-ont | reported |
| K-ACC | search for a chain-rule violation of 𝓘_acc in 𝒟_LE and 𝒟_RT | C5 | countercontrol for N-acc | reported |
| K-C5+ | Shannon information on a purely classical interface satisfies (C5a)–(C5d), (I1)–(I9) and IC | C5 | must-hold | holds |
| K-I2 | a synthetic measure, exhibited exactly in step 2 before any route, that satisfies (I1) by definition and violates (I2) | C5 | must be flagged as failing (C5c) | flagged |
| K-PR6-C5 | D-1 to D-7 checked on K-PR6 itself, with B and the slices declared (C5-0) | C5 | measured; K-PR6 counts as an obstruction only if all hold | reported |
| CC-dec | path \|+⟩, marker I/2, coupling I on path 0 and Z on path 1, exactly: F_R = 1 for every readout, D = 0, V = 0 | Q2 | must-hold; the bound is reported as not attained | V = 0, inf F_R = 1 |
| K-1, K-7 | node 7's families and its fact that LE is quantum only at w = 0 | Q3, Q4 | must-hold | hold |
| K-2, K-3 | PR (LE(1,1)) and LE(2,1) | Q3, Q4 | must-fail admission under ML-NW, ML-F2, IC and K-P | rejected |
| K-C | classical admission: local vertices, LE at w = 0, rational mixtures | Q3, Q4 | must-hold | admitted |
| K-Q | quantum admission: TB in ℚ(√2), node 7's v = 12/17 point | Q3, Q4 | must-hold under ML-NW, IC, VR | admitted |
| K-ML | ML-NW's two code paths agree (local vertices, PR, TB, T1, LE(n,k) n ≤ 12, isotropic v ∈ {j/24}, 𝒜_CHSH(n) n ≤ 6) | Q3 | must-hold; disagreement voids ML | agree |
| K-IC | P-vD on PR gives 2 > 1; no protocol exceeds m on local vertices; TB stays ≤ 1 for n ≤ 12; the twirl preserves S_max on 100 rational boxes | Q3 | must-hold | holds |
| K-SOS | exact level-1 sum of squares for CHSH | Q3, Q4 | must-hold | holds |
| K-D+ / K-D− | derivation checker: a valid data-processing step closes; "on branch (a), Bob's readout at fixed microstate does not depend on Alice's setting" is refuted in 𝒟_LE | all | must-hold / must-fail | as stated |
| K-VR± / K-LHV / K-Kq | TB's correlators have exact vectors, PR's do not; the joint-distribution principle under-generates; in-house quantum ⇒ VR | Q4 | as stated | as stated |
| K-10 | node 7's 𝒜_CHSH reduction: no clause decided through it | Q4 | reported | reported |
| K-P | the quantum set as a principle (node 7's PC-3b) | all classifiers | must pass (a), (b-corr), (b1); Reproduction | passes |
| K-N1 to K-N7 | synthetic principles: S_max ≤ 3 fails (i); S_max ≤ 2√2 + 1/100 fails (i) at A1 and passes the A2 rows; S_max ≤ 2 fails (ii-S); excluding LE at w = 0 fails (iii); admitting only S_max < 2√2 fails (ii-S) and (ii-Q); S_max ≤ 2√2 on every box fails (b1); Q1 membership coded from the moment matrix passes (a) and (b-corr) and fails (b2) when its witness exists | Q3, Q4 | checker controls | as stated |
| K-N8 | synthetic "fringe law by response table" | Q2 | must be classified Reproduction (retrodiction) | Reproduction |

**Mutation controls.** Each names its target and counts as caught only when that check fails cleanly, after all
unmodified checks pass.
- KM-1 breaking any control suppresses every verdict it serves; KM-2 a line whose own checks fail prints "void".
- KM-3 dropping the PSD constraint from ML-NW admits PR, and the label changes to over-generation.
- KM-4 replacing m = x₀ ⊕ a by m = x₀ removes PR's exclusion, and K-2 fails.
- KM-5 marking a refuted step "closed" changes the class; Emergence is returned only when the ledger, the K-PR6 line
  and the circularity verdict permit.
- KM-6 removing an A-type tag without a closing step is caught by I-18.
- KM-7 inserting a target ("S_max ≤ 2√2", VR, B-VF or V² + D² ≤ 1) as a premise is caught by the static premise check
  and the checklist.
- KM-8 a floating-point comparison on the verdict path is caught by I-4.
- KM-9 defining V := F_R (or V := the marker overlap) is caught by I-24.
- KM-10 deleting a route's K-PR6 or K-PROG line suppresses that route's verdict (I-26).
- KM-11 one section's classifier reading another's verdict is caught by I-23.
- KM-12 printing a (b-corr) result on the (b) line is caught by I-27.
- KM-13 skipping the C4 check on CC-hm prints "unchecked" and suppresses the Q2 verdict.
- KM-14 using 𝓘_acc as 𝓘 without checking (I1)–(I9) is caught by I-29.
- KM-15 computing D from the observer's actual readout instead of the maximum over admissible readouts is caught by
  I-30.
- KM-16 letting an eraser (postselected) visibility enter V is caught by I-31.
- KM-17 asserting V = F_R at the optimal readout (reporting the fidelity bound as attained) is caught on CC-dec by I-33.
- KM-18 a checker that tests (C5c) by (I1) alone accepts K-I2's measure; with (I2) checked, K-I2 is flagged. Caught by
  I-29.
- KM-19 a generator that prints a bare "Conditional" for an adopted axiom without an established further consequence
  is caught by I-34.
- KM-20 treating ontic parameter dependence as a failure of initial independence (failing IC-D5a or C5-S3a on account
  of P9) is caught by I-35.

***

## 13. The four outcomes, and Parked

Each verdict line gets exactly one class, computed from its clause outcomes, derivation verdict, assumption ledger and
K-PR6 (and K-PROG) lines. Correlation classes carry "(Bell)". (b-corr) and (b) are reported separately and never change
a class.
- **Emergence.** Derived (§10); every assumption M or O; K-PR6 (and, for Q2, K-PROG) rejected by an O-typed premise; no
  barred input; the circularity review passes; the preregistered formalization; and the line's target holds ((a) for
  correlation lines; B-VF with achievable boundary points for Q2; a restriction meeting §6.2's criterion for Q1).
- **Conditional on {named axioms}.** The derivation needs named A-typed assumptions (or a refuted step's conclusion
  adopted as an axiom); none Q-typed; K-PR6 rejected by an O-typed premise or a named axiom; the review passes; and the
  target holds on the conditional admitted set (boxes of O-admissible realizations satisfying the cited premises and the
  axioms, computed in step 2 when it differs from the principle's own set). The label names every axiom, for example
  "Conditional on H-C5" or "Conditional on ML (derivation refuted at ML-D4)", and names it as a candidate missing
  physical principle. A Parked derivation makes the class Parked, and the conditional row is then reported as a row.
  - *Adoption criterion (verdict-generator clause, §5.4).* Mathematical correctness of a Conditional line is separate
    from adoption. The generator prints "Conditional; additional-consequence requirement unmet" unless the line's
    ledger records an established further consequence of the axiom: derived with OI's premises, independently testable,
    and extending beyond the CHSH target that motivated the axiom. It need not contradict QM.
- **Reproduction.** No required clause fails, and a Q-typed input is used, or K-PR6 or K-PROG is rejected only by a
  Q-typed premise, or a parameter or fringe amplitude is fitted (sub-label "retrodiction"), or the formalization codes
  the target (the quantum set, Q1, VR, B-VF or the fringe law) as the principle.
- **Failure.** A required clause fails ((i), (ii-S), (iii), (F1), (ii-Q), (iii-𝒜); for Q1 and Q2, an exact countermodel
  inside the cited premises; for any correlation route, K-PR6 not rejected; for Q2, K-PROG not rejected; for H-C5's
  derivation line, "OI does not imply C5", decided only as §5.4's table states). Sub-labels: over-generation, under-generation, classical exclusion, countermodel,
  Failure-as-stated (parameter named). Scoped to the formalization and classes examined.
- **Parked.** A named formalization gap, an undecided route the class depends on, an unmet amendment gate, an
  unresolvable checklist item, or an incomplete required check (range stated). H-C5's "Undetermined" (no suitable
  construction found, no obstruction shown) is Parked, never Failure.
- **H-C5's own line** prints §5.4's verdict text ("construction fails" per route; "Undetermined"; "OI does not imply
  C5"; "C5 established on domain 𝔇") beside its class. "C5 established on 𝔇" makes the correlation lines eligible for
  Emergence on 𝔇 only, with 𝔇 printed.

**Precedence:** 1 Parked; 2 Failure (attach "quantum ingredient" and the derivation verdict where they apply); 3
Reproduction; 4 Conditional; 5 Emergence. For every Failure and Conditional the node states the step and premise
responsible and which response maps remain admitted. The classifier reads only measured clauses, ledgers, the
countercontrol lines and the recorded circularity verdict (reviewer named); no class is a literal; Emergence and
Conditional print as provisional until the review is recorded.

***

## 14. Circularity-review checklist (every candidate, every section)

The reviewer records pass, fail or not applicable per line, with the step. A fail on items 1–6, 16, 18, 21 or 22 makes the
line Reproduction unless the step is removed and the derivation still closes; a fail on any other item makes it Parked
until resolved.
1. No posited Hilbert-space or operator-algebra structure, Born rule, amplitudes, quantum instruments or quantum states.
2. None of the quantum set, Q1/NPA, TLM, 2√2, TB, VR, B-VF, V² + D² ≤ 1 or the fringe law is a premise.
3. E3 only as a classical count (Substratum.md:92).
4. Neither Computation.md:130 nor the shadow realizations of Main.md:576–578.
5. No parameter fixed by its effect on the result; A-2's justification recorded verbatim.
6. ML-NW coded from the covariance; quantum IC used only as an admission control.
7. Every premise is in §3, quoted at its file:line.
8. Every assumption in its ledger with its type, no type changed after a result.
9. Records are visible configurations under O; no box, amplitude or marker state treated as primitive.
10. Operational no-signalling not used where the ontic statement is needed (IC-D3, IC-D5, C5-S3, V-K).
11. The Lemma 1 reading stated wherever used.
12. Each favourable branch pressure-tested (§A.31), with the countermodel attempt recorded.
13. Each displayed equivalence has a witness per direction (§A.34): ML-NW ⇔ Q1; VR ⇔ the quantum correlator set; H-C5
    ⇒ IC (one direction only is claimed).
14. No class, protocol family, tolerance, reading or rule changed after a result (I-15).
15. [L] closes mathematics only.
16. Q2: V from counts, D over admissible readouts, path by blocking, eraser fringes separate, no quantum rule in the
    hidden sector; positive controls from their own models.
17. Q2: interferometer parameters fixed by the architecture before the pattern is computed.
18. 𝓘 for H-C5 is built from OI's observer interface; checking (C5a)–(C5d) does not assume IC or any bound it implies.
19. Every route's K-PR6 line (and K-PROG for Q2) is present, with the premise quoted and the violation exhibited.
20. No section's verdict used elsewhere except through a named step (§4.1, §9.4).
21. Finite memory (C3, P1) does not stand in for IC, ML, H-C5 or B-VF: no step bounds information across alternative
    interventions by capacity alone.
22. Initial measurement independence and ontic parameter dependence are kept apart: no route is rejected, and no step
    fails, on the ground that branch (a) breaks independence of the shared resource. Each hidden-state failure names B,
    its slice, the step and the mode ((i) not a local channel; (ii) remote-input information before the message).
23. H-C5's identities are checked as listed ((I1)–(I9)), (I2) independently of (I1); a PR-box model is counted as an
    obstruction only with D-1 to D-7 checked on it; a model taken from a correlation table declares its completion.
24. Q2 asserts no saturation of B-VF; V and the fidelity bound are reported separately.

The checklist is pinned by this file's digest; reviewer additions before step 2 go under `amendments/`.

***

## 15. Productivity test and G6

**Productivity test (fixed now).** The node is a gem iff one of the following holds, strictly stronger than V-1 to V-9,
node 7's AW-MC7-2 (the admitted gate sets the magnitude) and Methodology.md:393 (no-signalling does not select the
quantum set):
- **H-C5:** "C5 established on domain 𝔇", with 𝔇 stated and (C5a)–(C5d), (I1)–(I9) proved there; or "OI does not
  imply C5", with an OI-admissible model on which D-1 to D-7 are checked and no measure can exist, naming the OI
  premise responsible. A construction failing ("construction fails") or "Undetermined" is record-only unless it
  identifies which identity fails and why.
- **Q1:** a derived cross-intervention restriction meeting §6.2's criterion; or, for each premise, the exact
  countermodel together with a precise statement of the restriction that would be needed (a candidate missing physical
  principle).
- **Q2:** B-VF derived from a named restriction with K-PROG rejected; or a C1–C4 countermodel (CC-hm or K-PROG) together
  with the named premise Main.md:666's which-path statement would need.
- **Q3:** IC or ML derived (Emergence, or Conditional on axioms strictly weaker than the principle, shown by a reviewed
  [W]); or a failure at an identified step with an exact countermodel that names the OI premise responsible and what it
  implies for MC6's N1–N3.
- **K-PR6:** any route whose K-PR6 line names an O-typed premise is a gem by itself.
- **H-X:** a decision on the working hypothesis supported by the above.

A Failure that only restates AW-MC7-2, MC6 §12 or V-1 to V-9 is a non-gem (record-only).

**G6 (rule inherited from MC7 PREREG §7):** a finite-precision, raw-direct statistic (§A.24) on which the line's admitted
set differs from QM by more than the stated resolution, of a size fixed by OI quantities with no free parameter, with
both outcomes possible. Scenarios fixed now: V² + D² > 1 at a fixed size; nonzero I₃ at a fixed size (Structure.md:1312's
bounds); coarse-grained Bell tests on non-i.i.d. sources [L-s: Gallego–Dakić]; the Q1 points that violate IC [L-s]; the
three-setting points once PC-PW is met [L-c]; chained, I3322 [L: Collins–Gisin 2004; an exact separating value needed]
and NPA 1+AB; the temporal CHSH bound [L: Le et al. 2017].

***

## 16. Invariant→checkpoint table (§A.41)

| # | property the node will assert | checkpoint that measures it |
|---|---|---|
| I-1 | this preregistration preceded every computation and is unchanged | sha256 in NODE.md and the commit message; the step-2 commit carries it byte-identical; amendments under `amendments/` with time, reason and state of knowledge, each before the computation it touches; the probe's first line prints the digest |
| I-2 | condition O holds for every realization | realizations only as (Ω, bijections, readout projection, prior); exhaustive bijectivity check; a static test that law code reads nothing else; K-9 count printed |
| I-3 | each candidate computed by its preregistered formalization | a parameter table transcribed from §5–§9, compared by the reviewer; each admit-function cites its section |
| I-4 | every verdict comparison exact or rigorously enclosed | rational and ℚ(√2) arithmetic; enclosure widths printed; AST scan for float use on the verdict path |
| I-5 | determinism | two runs, byte-identical, `SHA256SUMS` |
| I-6 | no verdict over a failed control | per-section gating on the controls of §12 it serves; KM-1 |
| I-7 | the checker detects over- and under-generation, classical exclusion, approximate principles, post-quantum admission below 2√2 and fitted fringe laws | K-N1 to K-N8, K-P |
| I-8 | universal clauses beyond computed ranges | reviewed [W]; failures by one exact violator |
| I-9 | follow-ups triggered as fixed | probe log with independent certificates |
| I-10 | (b) apart from (a), never established without the two-inclusion proof | separate blocks; no (b) line derived from (a) |
| I-11 | classification follows §13 | classifier inputs printed beside each class |
| I-12 | quotes verbatim at `a501b418` | `quotecheck.py`, 74 fragments, rerun in step 2 |
| I-13 | independent review, including §14 | review section in NODE.md with checklist results per line |
| I-14 | every step closed or refuted as recorded | step ledgers with premises, type, countercontrol lines, argument or countermodel; KM-5 |
| I-15 | nothing changed after a result | rule parameters and class definitions printed with digest before each section |
| I-16 | productivity and G6 follow §15 | table of structural reasons with their steps and N1–N3 items |
| I-17 | the classifier maps inputs to classes as fixed | unit tests: K-P, K-N1 to K-N8, one synthetic vector per class per section, precedence on two-condition vectors |
| I-18 | assumption ledgers complete and typed before any computation | ledgers from §5.2, §8.1, §8.2 printed with digest; each O or M entry names its closed step; KM-6 |
| I-19 | A2 rows never decide an A1 clause | separate block; static check; K-N2 |
| I-20 | ML-NW's code paths agree | K-ML |
| I-21 | IC exclusions certified | protocol, value and m printed per exclusion |
| I-22 | literature dependence visible | each line lists its [L], [L-s] and [L-c] items; a physical [L] dependence blocks Emergence |
| I-23 | depth-first order, no propagation | probe log of section order and stopping triggers; static check that each classifier reads only its own ledgers (V-M-1 and §9.4 steps excepted); KM-11 |
| I-24 | V from counts; neither V nor D from the other; V not set to F_R or an overlap | static check of the Q2 path; K-VD; KM-9 |
| I-25 | C1–C4 checked in their exact statements | per-realization C1 witness, C3 bound, C4 gap and C2 persistence printed; K-C1C4; KM-13 |
| I-26 | every route has its K-PR6 line (and K-PROG for Q2) | ledger check; KM-10 |
| I-27 | (b-corr) never reported as (b) | separate lines; unit test; KM-12 |
| I-28 | literature test points enter only through amendments | (b5) and IC-G read only from an amendment file whose digest is printed; otherwise "not run (precondition unmet)" |
| I-29 | each H-C5 property and each identity the C5 ⇒ IC proof uses has its own checkpoint | (C5a)/(I6) on classical record pairs exactly; (C5b)/(I5) on every allowed local operation in the declared domain; (I1), (I2), (I9) on every triple in the domain, (I2) checked independently of (I1); (I3), (I4) and (I8) on every pair; (I7) for every classical message; each printed per route with the domain; K-I2; KM-14, KM-18 |
| I-30 | D is the maximum over admissible marker readouts | the readout set enumerated (configuration readouts after accessible bijections on marker and ancillas) and its size printed; KM-15 |
| I-31 | eraser fringes separate | K-ERASE; static check that V reads only unconditional counts; KM-16 |
| I-32 | B-VF is never assumed | static premise check: B-VF appears only as a conclusion or a test target; KM-7 |
| I-33 | no saturation of B-VF is asserted | the Q2 report prints V and inf_R F_R separately and never prints equality as a property; CC-dec; KM-17 |
| I-34 | the adoption criterion is applied | every Conditional line prints its further-consequence status from the ledger; a unit test with no consequence yields "Conditional; additional-consequence requirement unmet"; KM-19 |
| I-35 | initial independence and parameter dependence are kept apart | IC-D5a and C5-S3a evaluated from O3 and the prior alone; a static check that neither reads P9's long-edge steps; the ledger names the failing step and mode (i) or (ii) for every hidden-state route; KM-20 |
| I-36 | H-C5's verdict follows §5.4's table | unit tests: one synthetic finding per table row returns that row's text; "Undetermined" maps to Parked, never Failure |

***

## 17. Procedure and freeze

- Step 2 order:
  1. quote check, condition-O engine, C1–C4 checker, classifier unit tests;
  2. common controls (K-PR6, K-PR6-RAC, K-PROG), mutation controls;
  3. H-C5 (§5): C5-0 with D-1 to D-7 checked on K-PR6 (K-PR6-C5), K-I2, routes N-ont, N-acc, P-pq, P-ms with
     (I1)–(I9) checked per route, the chain C5-S1 to C5-S5, and the adoption criterion;
  4. Q1 (§6); 5. Q2 (§7); 6. Q3, 3A then 3B (§8), then V-M-1;
  7. Q4 (§9), with (b5) and IC-G only if PC-PW and PC-GM are met;
  8. classification, H-X, productivity, G6;
  9. the independent review including §14, after which provisional labels become final or change as §14 states.
- Additions before step 2 (a reviewer's premise, route, reading or checklist item, a corrected quote, a PC-PW or PC-GM
  amendment) go under `amendments/` with time and reason, and a new sha256 is recorded. After a section's first
  computation its formalizations, classes, rules and criteria are frozen; a later discrepancy is recorded, not repaired.
- Negative results are acceptable and scoped to the readings, routes and classes examined. They do not establish that
  observational incompleteness as such cannot explain quantum behaviour; the emergent-QM hypothesis and the A2 programme
  stay open.
