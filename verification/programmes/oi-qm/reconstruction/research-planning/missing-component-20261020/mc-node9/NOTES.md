# Node 9 draft: design questions for the owner, and literature status

These notes go with `PREREG.md` (DRAFT, NOT FROZEN). They are not part of the preregistration. Each open question must
be disposed of before the freeze.

## Closed by owner decision, 2026-10-21

**Q1. First model: closed.** Option A first; Option B next on the same engine and R-MENU; Option C as a side
calibration of PREREG §1.4.

- **Option A** (PREREG §4): pointer and record cells h ∈ ℤ₂^{2n}, φ = identity; reading ω(u, h) kicks h along u by a
  fresh bath bit; local Bell branch; first computation M0 (§4.1). On record [rec, review of 390e252f and owner check]:
  the seven-state single-toy-bit menu with the tested one-toy-bit partner admits purification; its convex closure,
  against the tested pure joint states, contains mixed states without purification. Neither is a prediction for
  Prep(𝓘) under §1.2.
- **Option B (aimed at M3).** MC6 P5 on ℤ₂² with the principle "each coupling step reads one record cell and refreshes
  the others it touches", meant to justify withholding Y; *w* is set by what the operations prepare from the counting
  measure. Risks: the gbit (if *w* = 1 is preparable, M5-L fails); a principle easy to vary on two cells; R-MENU (ii)
  failing by construction. Beyond-target prediction: POM value against preparation depth, versus (2+√2)/4.
- **Option C (aimed at M3 and M5).** A hidden direction λ from an *N*-point symmetric set on a circle; the readout along
  a writes sign(λ·a) and resamples λ on the half-circle about the outcome. The linear response 1 − θ/π bounds POM by
  3/4 in the continuum [W, unreviewed]. Beyond-target prediction: the linear law instead of Malus's cos², raw-direct and
  refuted by experiment [Q].

**Q2. Hidden-label control: closed.** K-HL0, K-HL1 and K-MENU, with K-HL1 running the premise check of PREREG §1.4.

**Q3. Fixed prior: closed.** Fixed within a realization, starting from the counting measure; every other preparation is
generated. A model choice, since Main.md:60 permits structured preparations (PREREG §0).

**Q4. Heralded conditioning: closed.** Generator (g6) with back-action; control K-HERALD.

## Closed in draft revisions 2 and 3, 2026-10-21

**QA. Option A's operation rule and clean-ancilla declaration: partially closed.** Two failure classifications are
defined (PREREG §2.2): an explicit violating preparation is M0 lost; a stated but unjustified operation restriction is
R-MENU unmet. The revision-1 rule ρ₀ is M0 lost by K-SYMP's witness [rec, owner check 2026-10-21]. The candidate Π_ω
(reversible record maps preserve the read/disturb pairing ω) is to be evaluated, not adopted; for it both
classifications are open. Main.md:290's update is symplectic, but that does not show that OI's available operations
enforce the rule (PREREG §4, claim table). Completed by QA′ in revision 3.

**QB. Beyond-target prediction: closed.** The sequential-readout repeatability postdiction of PREREG §4, derived from the
frozen read coupling; built into that coupling, so a match is at most CONFIRMING. |S| ≤ 2 in the local branch stays
prerecorded.

**QC. Restriction criterion: reopened and re-closed in revision 3.** The joint-pair form of revision 2 (support ≥ 2^*N*
over every canonical pair present) is violated by the declared coupling itself (W6, W1), and its exchange sentence is
false: Q is visible, so an exchange followed by a readout determines the pair (W3′) [rec, pre-freeze review of
6cf71e0e]. The corrected form (PREREG §4): the toy coordinates alone, every used pointer's P marginalized, support ≥
2^*n*, evaluated after each completed read-and-discard (or read-and-copy) and at every stopping time. Discarding at most
halves support, so it never creates a violation but can hide one; the joint support and the determined-functional
count are diagnostics. It remains an invariant to test, neither a general necessity nor a sufficient condition for
purification.

**QD. The POM–CHSH link: closed.** Written out as Lemma S [W] (PREREG §2.4): S_CHSH = 8*p* − 4, no-signalling from parity
equivalence, with the physical qualification that the common extension must exist in the model.

**QE. Node-8 reference version: closed.** K-N8 is pinned to MC8 `probe/p8s1.r2.run1.out` (sha256 `b5ce288c…bd951`) at
`78913467`, reviewed ACCEPT WITH NOTES; its 46 realization lines equal r1's [rec, coordinator check 2026-10-21]. MC8
A-5 corrects A-4's wording and changes no outcome.

**QA′. Π_ω and the resources of Option A: closed in revision 3, subject to the owner's confirmation at freeze.**
Decisions Q10–Q13 (owner, 2026-10-21) applied, with the pre-freeze review's B1–B6 (PREREG §4, §4.1):
- Π_ω is the normalizer of the read family {R_u} on the record carrier, computed by exhaustive backtracking; [W]
  identifies it with ASp(2*n*, 2), which excludes nothing at *n* = 1. Pointer-internal maps are not operations.
- The pointer policy is an independent postulate under R-MENU (v): PP-1 single use (default), PP-2 the back-acting
  copy (tested alternative), both with the independence clause and the unavailability of discarded pointers.
- Clean resources are declared with their counts. Two counts are separate postulates (PREREG §1.1, §4): the number of
  visible read-out sites and the number of clean coordinates, each stated with whether its conjugate is clean; coin
  cells take part in no coupling step (§1.2). Model A's own declaration is unchanged: *b_p* + *b_m* clean coordinates,
  none with a clean conjugate. Neither count bounds what is learnt by itself, since a second visible site with no clean
  coordinate can lift L1, and so can a second clean pair read through one site [rec, design/emb at `3f11c8f7` (tree
  `6afbdab5`), corrected; re-review ACCEPT WITH CORRECTIONS; N1–N7 applied in the commit that adds this line].
- C-i is a disclosed design input: design/c1 at `49033a3e` (reviewed) covers the whole record lifecycle; design/emb at
  `3f11c8f7` (tree `6afbdab5`; corrected; re-review ACCEPT WITH CORRECTIONS; N1–N7 applied in the commit that adds this
  line) decides nothing until a diff check confirms N1 as applied. M0 runs on the abstract pointer model, with AP-1 to AP-5 named as
  assumptions of this implementation; C1 delivers only u-reads within its search bounds.
- R-MENU is computed on the record carrier only; whether Π_ω, PP and the declaration are derivable from the substratum
  stays open (claim table, row 3).

## Open before freeze

**Q5. Sizes, depths, ancilla counts and the scope S (updated).** S = (*n*, *k*, *b_p*, *b_m*, *b_r*, *b_h*) and the
caps *s_max*, *d_max* are defined in PREREG §4.1; heralding counts separately from ordinary conditioning. Proposed
values, for the owner to fix:
- M2 at A = one and two systems, each with a same-type purifier (*n* ≤ 4 toy bits; 256 record configurations);
- M1's spectator-stability clause on ABS, with S one system of the smallest declared type, at M1's sizes plus that
  system;
- M3 decoders to depth D = 3, with stability checked at D = 4;
- equivalence and M0 at *k* ≤ 2 ancillas, halting if *k* = 1 and *k* = 2 differ (PREREG §1.3);
- M0 locally at *n* ≤ 2 with *b_p* ≤ 4, *b_m* ≤ 3 (PP-2), *b_r* = *b_p* + *b_m* + 2, *b_h* ≤ 2; *n* = 3 and larger
  budgets as a CI plan; *s_max* and *d_max* set from a dry count of the closure's state space, not from wall time.

**Remaining before freeze.**
1. Q5's values, *s_max* and *d_max* fixed by the owner.
2. The owner confirms PREREG §4's PP text, clean-resource declaration and Π_ω definition.
3. A diff check confirms the design/emb correction N1 as applied (the re-review of `a9af8ef0` returned ACCEPT WITH
   CORRECTIONS; N1–N7 applied in the commit that adds this line); until then its findings decide nothing.
4. Q6–Q9 disposed; node 8's `quotecheck.py` run with a node-9 fragment list (Q8).
5. An independent re-review of revision 3 against the pre-freeze checklist; then the frozen sha256 recorded.
6. Not blocking (I-17 prints "provisional"): the literature gates PC-POM, PC-SPK, PC-CDP, PC-S05, PC-BRS.
7. The owner confirms M1's spectator-stability clause (PREREG §3, reading (S) chosen over product preparability (P)),
   motivated by design/cards: Π_B, a classical simplicial theory without preparable product states, passes M1 as
   worded without it. Control K-CARD must FAIL M1 under the clause.

**Q6. Scope of M5.** M5-L and M5-A cover POM and CHSH only, linked by Lemma S (PREREG §2.4). Should further statistics
be added, such as the quantum set at NPA level 1, the chained Bell inequalities, or 3-bit POM? Is M5-A's A2 form wanted
as a live line, or PARKED from the start?

**Q7. M4 for Option A.** Option A is local-branch, so M4 can only FAIL there (K-BL makes a value above 2 void). A
branch-(a) composite with preparation-indexed edges is a different model, proposed as a later node with K-PR6 and M5-L as
its guards.

**Q8. Tag convention.** [Q] marks unread literature and [corpus] verbatim corpus quotes; [rec, owner …] is added for
owner-supplied checks and readings. The corpus quotes were checked at `eb19f063` (reachable from `main`;
`papers/Main.md` is byte-identical at `main` `af8c59d6`) by an ad hoc substring check at the cited lines; the Main.md:60
quotes were checked the same way at `d53febe7`, and the Main.md:290 and Main.md:320 quotes of revision 2 at `c81f2df4`.
At freeze, node 8's `quotecheck.py` should be run with a node-9 fragment list.

**Q9. Left out to keep the node short.** The CDP per-axiom audit (MC8 §6.3–§6.4); C5-IC; the interference diagnostic;
branch-(a) composites; robust (finite-precision) noncontextuality inequalities. The last matters: under ε-agreement PNC
is vacuous (MC6 `leak.py`), so M3 is an exact-equivalence test only.

## Option B handoff

What carries over from model A to Option B, unchanged unless an amendment says otherwise:
- the engine: equivalence by Lemma W, the closure search with its completeness certificate and deterministic caps,
  heralding with back-action, the exact ℚ(√2) and ℚ(i, √2) arithmetic, and the mechanical Ops(Π) computation;
- Lemma W, and Lemmas F, A, S and the composition lemma;
- the controls and mutants of PREREG §5 and §7, including K-PIND, K-REUSE and K-PEX and the independence clause they
  test;
- the biased-state control K-BIAS, (3/8, 3/8, 1/8, 1/8);
- model A's results as baseline for Option B's productivity test, beside the disclosed C-i and emb findings.

Option B needs its own Π, clean-resource declaration and record policy, each stated before computing.

## Owner inputs after revision 3 (2026-10-21), not yet applied to PREREG

**Compatible-records argument [rec, owner 2026-10-21; W, to be reviewed].**
- *Assumptions.* The whole apparatus (toy, pointers, bath, controller, memory) starts uniform subject to mutually
  compatible linear constraints, or as a mixture of such states. Its complete evolution is affine symplectic. Every
  retained record is physically present in it. The simultaneously accessible record coordinates are mutually compatible,
  i.e. their symplectic pairings vanish.
- *Claim.* Conditioning on the complete current record then leaves the remaining toy systems with support ≥ 2^*n*, for
  any finite apparatus and any time.
- *Proof.* With *K* the transported definite properties, *L* the readable record properties and *B* the remaining
  system, the definite properties of *B* are *K_B* = (*K* + *L*) ∩ *B*. This set is compatible because *K* and *L* are.
- *Scope.* It allows reused pointers and correlated apparatus coordinates. Fresh independent disturbances are one way to
  implement it, not a necessary assumption. Intermediate observations and feedback must be implemented inside the
  declared dynamics; a free external record breaks the premise.
- *Owner's exact check, two toy bits, one part read.* With one compatible linear readout, all 324 nonzero branches keep
  support 2. Reading both conjugate coordinates gives 96 point masses and 72 branches with support 2.
- *Consequence for this draft.* M0 "retained" under PP-1 or PP-2 is predicted by this argument wherever its assumptions
  hold. Before freeze, the productivity baseline (§6) must therefore include it, and gem (e) must be checked against it.
  That review is open.

**The biased-state obstruction, with weaker premises [rec, owner 2026-10-21; W, to be reviewed].**
- *Premises.* Every preparation of a fixed finite composite is a mixture of preparable uniform affine states. Ordinary
  randomization is allowed. At least one specified local binary linear measurement is accessible. Full tomography is not
  needed.
- *Argument.* That measurement gives probability 0, ½ or 1 on every uniform affine state. An operationally pure joint
  preparation must give the same operational state in every component, so it cannot give 3/4. The preparable
  (3/8, 3/8, 1/8, 1/8) gives 3/4, so within this family it has no purification for a purifier of any finite size; the
  gap is ≥ 1/4. This applies to the stated affine family only.
- *Target this sets for Option B.* Can a construction supply an operationally pure composite whose marginal gives
  the biased probability 3/4? A successful construction must leave the uniform-affine preparation structure somewhere,
  or change another explicit premise.

**Card-structure line (owner, 2026-10-21; book §1.11, `amaybaum/card-table` at `17115cc`).**
- *State definition.* In the two-card swap game, preparations with equal current visible distributions are separated
  perfectly by a later swap. So the current visible distribution is not the operational state, and such preparations must
  not be declared equivalent (§1).
- *Recording versus disturbance.* In the owner's controls, return certainty drops to ½ only when the hidden memory card
  the next swap would recover is replaced. Copying the visible card does not lower it. The game's burn rule couples the
  two by declaration. Replacement draws come from a depleted deck, so they are correlated, not independent.
- *Escape from the affine counting obstruction.* Uniform joint deals with unequal fibres give biased marginals. Example:
  {(0,0),(0,1),(0,2),(1,3)} gives P(A=0) = 3/4. A uniform deal is not automatically operationally pure: if its
  individual deals are preparable, it is an ordinary mixture.
- *Uniqueness control.* {(0,0),(0,1),(0,2),(1,0)} has the same A-marginal, but B predicts A with success 3/4 instead
  of 1. None of the 24 relabellings of B maps one deal to the other [rec, owner; coordinator check 2026-10-21, exact].
  A menu that admitted both as pure would fail Pur-U under local relabellings.
- *Question.* Can card-like preparation and intervention rules, motivated independently, make such a joint preparation
  operationally pure while remaining closed under the permitted protocols? Exploratory design work comes before any
  preregistration.

**Parked: a relativistic reading of access (owner, 2026-10-21, to return to).**
- Accessibility should be judged at an observation event: which records have physically arrived there.
- Finite propagation speed alone does not prohibit the hidden reset in the reflection counterexample.
- For a nonlocal branch, operational no-signalling constrains which hidden records may be read. Diagnostic: with
  a = λ, b = λ ⊕ xy, a local record r = λ lets Bob read x = b ⊕ r.
- Candidate requirement: every allowed local protocol, including ancillary measurements, retained records and selection
  flags, has accessible statistics independent of spacelike-separated choices. Conditioning on a distant outcome
  received later is not signalling.
- Popescu–Rohrlich correlations reach CHSH = 4 under no-signalling, so this does not select the quantum bound.

## Literature status

| source | read? | what was established |
|---|---|---|
| Spekkens et al., PRL 102, 010401 (2009), arXiv:0805.1463 | not by this session | The owner reports that Theorem 2 and its two-bit quantum example give 3/4 and (2+√2)/4 [rec, owner read 2026-10-21]. The task wording remains [Q]. Both values are also recomputed in house by K-PNC and K-QPOM |
| Spekkens, PRA 71, 052108 (2005), quant-ph/0406166 | no, [Q] | A search summary of the abstract: an operational notion of contextuality, and no-go theorems for preparations, transformations and unsharp measurements, with proofs in dimension 2 |
| Spekkens, PRA 75, 032110 (2007), quant-ph/0401052 | no, [Q] | Secondary summaries only: the knowledge-balance principle, no Bell violation or contextuality; PREREG §4 (ii)'s expected M3 FAIL of Option A rests on this |
| Bartlett, Rudolph, Spekkens, PRA 86, 012103 (2012), arXiv:1111.5057 | no, [Q] | A search summary: classical Liouville mechanics with a restriction on second moments plus maximum entropy gives Gaussian QM ("ERL") |
| Chiribella, D'Ariano, Perinotti, PRA 84, 012311 (2011), arXiv:1011.6451 | no, [Q] | A search summary lists the axioms: causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning, and purification |

Access: at drafting, WebFetch to arxiv.org, alphaxiv.org and web3.arxiv.org failed (ENOTFOUND), and curl through the
agent proxy got a 403 at CONNECT for arxiv.org, export.arxiv.org, journals.aps.org and semanticscholar.org. One WebFetch
to arxiv.org on 2026-10-21 failed again (ENOTFOUND). Nothing load-bearing rests on a [Q] source: the numbers that decide
M3 come from in-house controls; M2's wording is gated on PC-CDP; attributions are gated on PC-POM, PC-S05, PC-SPK and
PC-BRS.

## Owner investigation after the card exploration (2026-10-21), coordinator review

These results come from the owner's read-only session. The coordinator re-checked the computational claims in
`design/owner-checks/` (`fb.py` and `fb2.py`). The card-side and counting checks are exact. The quantum-side checks use
floating-point linear algebra and are a numerical cross-check of Clifford identities, not an exact certificate.

- *Menu closure first.* A restricted menu of uniform four-deal mixtures, 70 of them each extreme in the menu, becomes the
  full classical state space once a non-destructive read with heralding is allowed. Purity is judged on the closed menu
  only.
- *Uniqueness control.* There are 16 four-deal supports with a 3:1 marginal, in two classes under relabellings of B
  [exact].
- *Single-system card theory.* Operations are swap, and read-and-replace with a fresh fair card.
  - The space of outcome-probability functionals closes at dimension 3: normalization, E(−1)^v and E(−1)^h [exact].
  - ρ(a, b) = ½(I + aZ + bX) reproduces it. Swap ↔ H; read ↔ Z measurement with its update; swap–read–swap ↔ X
    measurement. Preparations form the diamond |a| + |b| ≤ 1. This is a restricted qubit theory [rec, owner].
  - Reusing one reservoir card across three reads with swaps between them determines the system in every branch. A
    fresh card at each read leaves support 2 [exact].
  - So the correspondence holds only with fresh, independent replacement resources, the same assumption as AP-1 in
    design/c1.
- *Two-system card coupling (q_B ^= q_A, p_A ^= p_B).*
  - 24 pure joint states are reachable, 8 of them with both marginals maximally mixed.
  - On the five-state finite menu, Pur-E and Pur-U pass. On the convex closure, Pur-E fails: P(q = 0) = 3/4 is preparable,
    but no pure joint state has that marginal [rec, owner].
  - Six-operation witness: (swap_A, couple)³, then read q_B. The cards give 0 with certainty; the qubit circuit
    (CNOT·(H ⊗ I))³ on |00⟩ gives 1 with certainty, with (U³)†Z_B U³ = −Z_A Z_B [card side exact; QM side numerical].
  - Adding one more swap_A returns the card distribution to its start, while QM still gives 1 [numerical].
  - Under the existing preparation and readout rules, the CNOT tests force all four output bits, so no 4-bit shuffle
    repairs the discrepancy [rec, owner; scoped to this representation].
- *Signed relations, i.e. the stabilizer formalism [rec, owner; Aaronson–Gottesman, Q].* Tracking signed joint relations
  reproduces the family's quantum transitions and measurement branches (owner: 192/192, 192/192, 160/160).
  - Dropping the sign update for swaps gives 16 failures; dropping it for the coupling gives 24.
  - The sign rules were taken from quantum theory, so this is reproduction or calibration, not reconstruction (§A.29).
  - Coordinator check: the reachable set under H_A, H_B, CNOT_AB, X_A, X_B and Z-measurement updates from |00⟩ has 24
    pure states, 8 of them maximally entangled [numerical].
- *The purification obstruction persists after the sign repair* [coordinator check, numerical]. Every single-qubit Bloch
  component of the 24 reachable states lies in {−1, 0, 1}, so local binary probabilities are 0, ½ or 1. This is the
  uniform-affine obstruction again: the biased state still has no purification in this family.
- *Two separate gaps, as the coordinator reads them.*
  - (G1) A composition law for joint records that supplies the sign/phase structure, the step from the toy theory to
    the stabilizer theory. It is needed for the six-operation witness.
  - (G2) Pure states outside the uniform-affine (stabilizer-type) class, the step from stabilizer to full QM. These are
    needed for C5-P on the convex closure.
  - C5-P bears directly on G2. G1 is a composite-statistics requirement in its own right.
- *Corpus check (§A.19).* papers/Main.md:352 reads: "The purification, continuous-transitivity, and tomographic-locality
  axioms of the cited reconstructions are hypotheses of their continuum endpoint, which the classical-dimension
  obstruction places beyond any fixed finite carrier; they are not what the finite characterization uses." Testing C5-P
  as exact purification on one fixed finite carrier (nodes 8 and 9) therefore asks the finite stage for a property the
  corpus places in the completion. Lemma F already makes the quantum values unattainable for finite rational models. A
  test consistent with the corpus asks whether purification holds in the limit along a declared family of finite
  constructions (M5-A's A2 form). The limit and its convergence notion are specified in `design/limit/LIMIT-DESIGN.md`.
  Every pure stabilizer state gives a fixed local Pauli measurement only the probabilities 0, ½ or 1, so it misses the
  3/4 witness by at least 1/4 at every size [rec, owner 2026-10-21: stabilizer density-matrix expansion]. The bound is a
  property of affine operation rules, not of family size or of the finite stage: H on two qubits followed by one
  non-affine configuration exchange |110⟩ ↔ |111⟩ (a Toffoli, available in the sourced access) gives a pure three-qubit
  state with target marginal exactly diag(3/4, 1/4) [EC, `design/map/MAP.md`]. The biased witness therefore needs
  neither a limit nor a continuum; it needs one non-monomial gate (H), whose sourcing is the C5 discovery audit's test 8.
  A purifier of one system's size is not checked.
- *Literature named by the owner [Q, not read here; network-gated]:*
  - CDP 2011: purification implies no information without disturbance;
  - Chiribella, "Agents, subsystems, and the conservation of information";
  - the phase-group distinction between Spekkens' toy theory and qubit stabilizer QM;
  - Aaronson–Gottesman;
  - outcome-deterministic contextual models of stabilizer QM.

## Owner investigation summary after G1 (2026-10-21), coordinator review

These results come from the owner's read-only session and have not been independently reviewed as repository results.
The coordinator re-checked the exact items marked ✓ in `design/owner-checks/fb3.py`.

- **Card fragment.**
  - The outcome-probability space has dimension 3, and the state space is the diamond |x| + |z| ≤ 1.
  - Swap and read-with-reset reproduce a restricted qubit theory for the declared fragment.
  - Reservoir freshness is decisive in the three-read test.
  - The engine's double-slit tables encode chosen statistics; they are a reproduction, not a derivation.
- **Stabilizer calibration.**
  - The full two-qubit stabilizer operations reach 60 pure states, 24 of them maximally entangled.
  - This is calibration with supplied quantum algebra, and its classical simulability is established literature [Q].
- **Fixed gaps.**
  - Lemma G's 1/4 gap (see `design/limit/`).
  - **Diamond witness.** If conditional local states stay in the diamond, W = ⟨Z_A⟩ + ⟨X_A X_B⟩ ≤ 1. The state
    (15|00⟩ + 8|11⟩)/17 gives W = 401/289 ✓.
  - The best diamond-constrained approximation has total-variation error 28/289 [rec, owner].
  - Passing W is necessary for the target, not sufficient: a classical model with a less restricted menu reproduces
    those tables.
- **Limits must carry operations and composites.**
  - The rational rotation (1/289)[[161, −240], [240, 161]] has an irrational angle (cos θ = 161/289; Niven ✓). Under
    reversible closure, mixtures and limit closure it expands the diamond to the disk. This is conditional: the
    rotation is supplied, not native.
  - ρ± = (II ± YY)/4 agree on every product measurement built from I, X, Z. A declared interaction followed by local
    readout separates them, and the functional span grows from 9 to 10 [rec, owner]. This is the real-QT failure of
    local tomography [Q].
- **Local validity is not composite validity.**
  - (x, y, z) ↦ (z, y, x) preserves the Bloch ball but gives a negative probability on half of a Bell calibration.
  - (z, −y, x) is the Hadamard action.
  - All 24 orientation-preserving signed permutations pass and all 24 orientation-reversing ones fail [rec, owner].
- **The effect menu is substantive.**
  - On the diamond, a restricted effect family satisfies the tested "no simultaneous encoding" condition.
  - All affine-valid effects permit perfectly recovering one bit together with a 5/8 guess of a second [rec, owner].
  - "Every mathematically valid effect" is therefore an assumption.
- **The histories route (conditional; literature [Q]).**
  - A tensor-closed class of weakly positive systems is either strongly positive or real and nonnegative.
  - With a declared phase operation, recombination and marker readout, positivity gives |c_r|² ≤ a_r b_r and hence
    V² + D² ≤ 1.
  - It gives a Tsirelson bound under Bell-scenario assumptions.
- **Single-system history weights do not fix composition.** For D_t = [[½, it], [−it, ½]], every single-system weight is
  0, ½, ½ or 1, but the two-copy agree weight is ½ − 2t² ✓. It fails strong positivity at t = 1 and passes at t = 0,
  ¼ and ½, so a continuum of choices stays consistent.
- **Pairwise consistency does not license jointly retained records.**
  - At t = ½, every pair of three copies has agree weight 0.
  - Three actual bits satisfy 1[a=b] + 1[a=c] + 1[b=c] ≥ 1, so the pairwise distributions cannot describe three
    jointly retained bits.
  - The common refinement of the three partitions is not decoherent [rec, owner].
  - A history formalism therefore needs a physical rule for which partitions become records.
- **Classical countercontrol.** Hidden signs with means 2t and 2s give P(r_A ≠ r_B) = ½ − 2t_A s_B ✓. A bijective
  five-bit XOR pointer realizes it, so matching the two-system formula does not establish a history interpretation.
- **Owner's verdict.** No tested condition has earned the status of C5. Purification, information constraints,
  continuous reversible dynamics and history composition each leave named premises unresolved. CDP's other five axioms
  are not to be credited to C1–C4. Before the next construction, declare:
  1. one dynamics and resource model, including the apparatus, memory and preparations;
  2. one representation across all interventions;
  3. which records can coexist, including copying, reuse, heralding and later access;
  4. a compatible family and a convergence criterion, if the target is a completion;
  5. one independent consequence beyond the calibration targets.

  This is an open reconstruction problem with sharper controls. It does not rule out deterministic OI.

## Owner report 2, "Observer interfaces, coherent control and composite records" (2026-10-21), coordinator review

- *Source.* The owner's read-only session, as an HTML report pinned to `main` at `af8c59d6`. The report's own checker is
  committed in `design/owner-checks/report2/` together with its output.
- *Verification.*
  - The checker's sha256 `37dbc272…` and its output's sha256 `ae05d543…` match the report's stated hashes. Every
    internal assertion passes.
  - The coordinator independently recomputed the four-step witness from the report's definitions, without importing
    the checker (`coordinator_witness.py`). P(+++) = 1/4 for PZ and 3/16 for PX ✓.
- *Findings [rec, owner report 2].*
  - The four-label diamond calibration: R ↦ qubit conjugation (stipulated map); reset reads give span 1 → 3 → 3, while
    disturbance-free reads give 1 → 3 → 4; 8 of 24 hidden permutations preserve the quotient.
  - The product two-system quotient has exactly 128 = 8·8·2 automorphisms: local symmetries and exchange only.
  - The symplectic involution G : (a_A, b_A, a_B, b_B) ↦ (a_A, b_A ⊕ b_B, a_B ⊕ a_A, b_B), with reset reads and retained
    outcomes, gives the probability span 1 → 5 → 9 → 10 → 16. Every initial hidden distribution becomes statistically
    identifiable, and the product density-matrix quotient is not a sufficient state for this interface.
  - The witness word X_B, G, X_B, X_A gives the branch probabilities above, cross-checked by seed enumeration
    (16/64 vs 12/64).
  - Scope: one declared reduced-state model. It does not rule out deterministic OI.
  - Relation to G1: this is a trivial-extension (unsigned) lift of a symplectic gate. It is consistent with G1-REPORT,
    where the trivial extension reproduces the cards and not QM.
- *Corpus results the report names.* They are on `main` and already used in mc-node2 and mc-node5, but node 9's G1/G2
  framing does not yet connect to them:
  - the C5 discovery audit (`verification/audits/foundations/c5-discovery-audit.md`, verdict C, underdetermined), which
    frames the coherent resource as two separate obligations: O1, the relative-phase resource `PhasesAvailable`, and
    O2, the continuous coherent transition `LayerFlowExecutable`;
  - `sourcedOI_qm_iff_phaseFree`;
  - `fixedGateTheory_denseFiniteQM` and `fixedGateTheory_not_qm`;
  - `obsTheory_rule_independent`, whose observer theory is permTheory on the configuration space;
  - OPACT-1, COMP-1, and the conditional pair-cone theorem (KTOKEN-MAXCONE-1).
  
  Before G1/G2 work continues, map G1 (sign/phase composition) and G2 (pure states beyond stabilizer, continuous
  completion) onto O1/O2 and these results, so the thread reuses them rather than re-deriving them.
- *Manuscript bridge flagged by the report, not checked here.* papers/Main.md:702 asserts that every fundamental
  non-Markovian process "must therefore be classical-memory simulable in the operational sense of Bäcker, Beyer, and
  Strunz [28]". The report notes that BBS Definition 1 requires E₂(ρ) = Σᵢ Φᵢ(Mᵢ ρ Mᵢ†) with each Φᵢ CPTP, and that a
  classical hidden-variable simulation is not automatically a proof of that decomposition. Whether OI's
  fixed-basis/permutation representation meets the definition, in particular for coherent system inputs, is an open
  check on a manuscript claim. §A.25 applies if it changes.

## Owner report 3, "OI fixed-gate source investigation — independent handoff" (2026-10-21), coordinator review

- *Source.* The owner's read-only session, as an HTML report pinned to `main` at `af8c59d6`. The report's checker and
  its output are committed in `design/owner-checks/report3/`.
- *Verification.*
  - The checker's sha256 `d9697c3f…` and its output's sha256 `73c584d2…` match the report's stated hashes. A re-run
    replay-matches byte for byte, and every internal assertion passes.
  - `coordinator_spotcheck.py` recomputes, without importing the checker: P(0) = 9/25 after R and 49/625 after R²;
    337/625 for both R S R and the dephased R;R; and |x| + |z| = 31/25 for R|0⟩ ✓.
  - Control gap closed. The checker evaluates the CHSH closed form S = 2[cos 2kθ + sin² 2mθ · sin 2kθ] but never
    compares it with the state and observables. `coordinator_chsh_direct.py` builds CNOT·(R^m|0⟩ ⊗ |0⟩) and the
    report's four observables exactly. The formula equals A₀B₀ + A₀B₁ + A₁B₀ − A₁B₁ at all 169 pairs
    (m, k) ∈ [−6, 6]², including the reported (−6, −3) and (72, −47) ✓.
- *Findings [rec, owner report 3].*
  - Sufficient package. R = (1/5)[[3, −4], [4, 3]], S = diag(1, i) and CNOT, with quantum representation, zero
    ancillas, Z readout, feedback and discard, are dense in finite instruments. θ/π is irrational because
    2 cos θ = 6/5 is not an algebraic integer.
  - Exact bounded interpreter. A fixed online update on (D, k, j), where D is a Gaussian-integer branch matrix and j
    is one seed uniform on {0, …, 25^K − 1}, reproduces the full adaptive record law of every rational circuit with at
    most K uses of R. All 625 seeds were enumerated on eight protocols.
  - Seed-support lower bound. a_n ≡ 3 (mod 5) for (3 + 4i)^n = a_n + i b_n, so P(0 | Rⁿ) = a_n²/25ⁿ is in lowest
    terms. A uniform prior on M microstates needs 25ⁿ | M.
  - Growing family. J′ = 25J + d preserves the record of every protocol within the old budget, checked on 625 and
    15,625 refinements. This holds at the record level and is not a lattice embedding.
  - Fixed-carrier recurrence lemma. One fixed finite deterministic update per R use with a fixed readout makes every
    readout probability eventually periodic. cos²(nθ) is dense on every arithmetic progression, so the supremum error
    over all n is at least ½.
  - Obstructions. (i) The four-label diamond, with |x| + |z| ≤ 1, cannot hold R|0⟩. (ii) A basis permutation on
    diagonal system ⊗ diagonal ancilla is at trace distance ≥ 12/25 from R|0⟩, at every ancilla size.
  - Imports. Matrix encoding, tensor rule, gate matrices, Born weights and update rule are assumed. The model is not a
    C1–C4 witness and not Bell-local.
- *Coordinator assessment.*
  - Relation to the corpus: ELABORATING. Main.md's *finite operational realization and gluing* theorem (§3.4, at
    `papers/Main.md:544`) already has the same architecture: a digitized branch-matrix density register, K pre-loaded
    uniform seeds, one fixed injective step map per instrument, a predecessor stack, and gluing by restriction. The
    report's specialization adds three things:
    - exactness (G = 25, zero total-variation error, for the rational alphabet) in place of the ε-form;
    - compatibility between realizations at budgets K and K + 1, where the theorem's gluing is within one realization;
    - the 25ⁿ seed-support count.
  - The other two results are anticipated:
    - The recurrence lemma is a single-gate, repeated-use form of the remark at Main.md:542: no fixed finite carrier
      reproduces the exact continuum theory.
    - The basis-permutation obstruction is anticipated by Main.md §3.2 and by the kernel's configuration-level results
      (`permTheory_no_sign`, `instAvail_unitary_fixes_ones`, `coherentLiftClass_eq_substratumClass`).
  - Agreement with node 9's refocus: CONFIRMING. The report's next task is an OI realization with an encoding E fixed
    in advance and E(F_R(p)) = R E(p) R† on every admitted preparation, spectator composites included. This is the
    C5 audit's test 8 (sourcing one non-monomial gate), which the MAP identifies as the missing item. The report
    sources R where the MAP named H; both are non-monomial, and either one closes test 8's question for its alphabet.
  - Assumption-watch marker (BORDERLINE, conditional). The seed-support lemma couples the gate choice to the counting
    measure's support:
    - Exact reproduction of Rⁿ needs a uniform sector whose size is divisible by 25ⁿ.
    - H + Toffoli circuits have amplitudes (integer)/√2^h, so all their probabilities are dyadic
      (`coordinator_dyadic.py`, 2,000 random circuits, exact).
    - So if a realization's accessible sectors have power-of-two sizes, H + Toffoli is exactly reproducible and R is
      approximable only.
    - The corpus fixes no binary site alphabet (Main.md Lemma 3: counting measure on a finite S), so the marker is
      conditional on the realization.
    - Consequence for test 8: the target gate should be chosen together with the declared sector structure, not
      separately.
  - Pressure test of the favorable reading (§A.31). The construction shows that bounded record-level simulation does
    not need a fresh kick at each measurement. It does not show that an OI lattice supplies one:
    - The seed entropy, K log₂ 25 bits, scales with the R budget, and the recurrence lemma forbids a fixed carrier.
    - The resource moves from per-step kicks to a budget-sized initial seed.
    - This refines AP-1's scope for this interpreter only. It does not remove AP-1 from the card or lattice models.

## Direction after the map (owner, 2026-10-21)

- *Decision.* On the coordinator's recommendation after `design/map/MAP.md` and owner report 3, the owner chose three
  things:
  - The H-LOC n = 3 run is deferred and not to be dispatched (`design/g1/G1-HYPOTHESIS.md`).
  - Node 9 works on sourcing a non-monomial gate: the C5 discovery audit's test 8.
  - The Lemma G framing is corrected in place, in this file, `design/limit/LIMIT-DESIGN.md` and PREREG §4: the 1/4 gap
    belongs to affine operation rules.
- *What test 8 already holds [corpus, `verification/audits/foundations/c5-discovery-audit.md`, T4–T6, and its
  polarization closure audit].*
  - The polarization candidate's map sends the shear layer to the quarter phase and the swap layer to the Hadamard
    matrix on the two-valued alphabet. The observer reads the position half of each site's (current, previous) pair,
    and the layers act by the Weil representation.
  - The resulting class is not configuration-level, so test 2 passes.
  - Its relabelling closure PolC has O1 at every level and no O2, since it is countable up to scalar. It satisfies the
    closure and is not QM.
  - Test 8 fails because the corpus does not supply the map. The discrete realization reads both slices of a visible
    site (Main.md:292, :316). The continuum statement at Main.md:216, which marginalizes the momenta, is an access
    statement of the right type, and it excludes the map (`design/test8/`, N4).
- *The refocused question.* Does any condition on observer access, of C1–C4's logical type and not mentioning the test
  vocabulary (audit test 7), force the polarization map? In report 3's form, the target is an encoding E, fixed before
  any experiment, that is not constant and reads the position half. E must intertwine both layers, E(τp) = S E(p) S†
  and E(σp) = H E(p) H, on every admitted preparation and with an untouched spectator. The swap half alone is a
  strictly weaker target (`design/test8/`, N3).
  - A positive answer is a candidate for test 8 only. O2 stays with the completion (Main.md:352).
  - H fits the dyadic marker of report 3's review. It is the swap's image on the two-valued alphabet; R is not. The
    quarter phase S is the shear's image only when the coupling has a centre term (`design/test8/`, N2).

## Owner report 4, "OI reversible implementation: independent handoff" (2026-10-21), coordinator review

- *Source.* The owner's read-only session, as an HTML report pinned to `main` at `af8c59d6`. The report's checker and
  its output are committed in `design/owner-checks/report4/`.
- *Verification.*
  - The checker's sha256 `d85da93c…` and its output's sha256 `9fa9dbf7…` match the report's stated hashes. A re-run
    replay-matches byte for byte. The compiled circuit is checked against a separately written arithmetic reference on
    all 5,632 admissible inputs.
  - `coordinator_report4_checks.py` recomputes the following without importing the checker:
    - the six-qubit preparation from a state vector: target (3, 4)/8, success 25/64; omitting the uncompute gives
      [[9, 9], [9, 10]] and 19/64 ✓;
    - the octahedron's closest point to R|0⟩ by a supporting-face argument: (21/25, 0, −4/25), squared trace distance
      9/1250 ✓. The checker only evaluates the distance to the stated point; the face argument shows it is the minimum;
    - the injection branches: Kraus 5√2·K = 5R and 5Rᵀ ✓;
    - the nonlinear leapfrog with swap and shear correction: Toffoli on all 64 inputs ✓;
    - the PR program's CHSH: 4 ✓.
- *Findings [rec, owner report 4].*
  - Reversible compilation. One real one-qubit experiment (H, Zᶻ, H, then readout and seed update) compiles to 1,095
    NOT/CNOT/Toffoli gates on 377 data bits, with clean uncomputation. An 11-bit clock makes it one autonomous
    bijection. The clock addresses distant wires, and no local controller is built.
  - PR countercontrol. The same compiler realizes a = r, b = r ⊕ xy in eight gates: uniform marginals, CHSH = 4,
    with global settings.
  - Stabilizer barrier. Under the canonical encoding, the affine update is Clifford. The stabilizer closure, with
    correlated retained baths, stays at trace distance ≥ 3/(25√2) from R|0⟩.
  - Magic-state route. H on three qubits plus Toffolis prepares (3|0⟩ + 4|1⟩)/5 heralded at 25/64. Injection gives
    R or R⁻¹ with probability ½ each, a symmetric random walk with infinite mean hitting time.
  - Nonlinear lattice primitive. A nonlinear coupling F gives the Toffoli from the leapfrog itself. Swap, shear
    correction, addressing and timing are added resources.
  - Encoding consistency. An H realized by card relabelling and a Toffoli taken from the canonical encoding are not
    one encoding: product card vertices give ⟨XZ⟩ + ⟨ZX⟩ ≤ 1, and the graph state gives 2.
- *Coordinator assessment.*
  - The PR countercontrol confirms existing corpus statements. Main.md:30 says every finite stochastic law has a
    finite reversible realization. GR.md:228 says every theory with full reversible control realizes the sealed core
    (`realizesSealedOICore_of_control`), so the OI clause does not select. The report also confirms that the
    sufficient conditional completion is GR §3.3's OI⁺ (GR.md:230–242, `carrier_general_oiPlus`). Neither is new.
  - The stabilizer barrier and the magic-state route agree with the corrected Lemma G framing. Affine rules stay
    Clifford/stabilizer, and H plus a non-affine Toffoli leaves the stabilizer class at a finite stage. The binary-seed
    preparation is an instance of report 3's dyadic marker: 9/25 arises from 64 binary seeds only conditionally,
    heralded at 25/64.
  - The nonlinear lattice primitive does not bear on availability: the kernel's sourced access already has the
    exchanges as interventions (`ExchangesAvailable`). It bears only on a native-dynamics account, and the Toffoli is
    monomial, so it does not touch test 8.
  - Two consequences for the test-8 design, both passed to the design pass in `design/test8/`:
    - (1) Common encoding. The polarization map must carry H (swap image), S (shear image) and the configuration
      relabellings in one encoding. The card-relabelling H shows that a gate realized in another encoding does not
      compose.
    - (2) Density of PolC. The polarization closure audit does not state whether PolC is dense in finite QM.
      `fixedGateTheory_denseFiniteQM` concerns `mixTheoryR` and is not a hypothesis schema PolC could meet. PolC lacks
      `FixedGateSourced` and `DenseUnitaryControl`, and its density is open (`design/test8/`, A2). Test 8 plus
      exclusion is not established as the whole finite-accuracy gap.
  - Exclusion is a separate obligation. A forced map that supplies QM's operations does not exclude the PR program.
    GR's OI⁺ handles exclusion through its operational-validity and composition conditions, which a test-8 candidate
    must also source.

## Test-8 design pass (`design/test8/`, 2026-10-21), coordinator review

- *Source.* A read-only design agent working in its own directory. `TEST8-DESIGN.md` is a draft and not frozen. Its two
  exact scripts verify against `SHA256SUMS`, and the coordinator's re-runs replay byte for byte. The pass was not
  independently reviewed. Classification: NEW.
- *Findings.*
  - **N1.** The shear τ is an involution on configurations. Its position-fixing Weil images S and S† square to Z. So
    any E with E∘τ = Ad_S∘E commutes with Z; with swap covariance under H it also commutes with X. The site part is
    then I/2 for every spectator, and for every E, linear or not.
    - Coordinator check [arg]: the commutant of {Z, X} is the scalars. The argument uses only τ² = id, S² = Z, H Z H = X
      and closure of the preparation set under both layers.
  - **N2.** A diagonal lift of the shear (p, c) ↦ (p + Lc, c) has a phase ±i exactly when Σ_x L_xx a_x is odd. The
    corpus rule (Main.md:290) is centre-free (SM.md:224–236), so its images are real, CZ networks times Paulis. The
    audit's site quarter phase therefore rests on a self-coupled shear, which the displayed rule does not have.
  - **N3.** Swap covariance alone:
    - No affine-injective encoding exists, by a sign obstruction: a transposition cannot be intertwined with a
      unitary conjugation.
    - With U = H, solutions have rank at most 2. Their position readout is unsharp, with bias ≤ 1/√2 on p = c.
    - They read the previous value in the X basis.
    - The class they source is real and countable: no O1, no O2.
  - **N4.** Main.md:216 marginalizes the momenta. Formalized as E(p, c) = e(c), it forces E to be constant.
  - **N5.** C1–C4-type conditions leave the observer theory at `permTheory` (`permTheory_realizesSealedOICore`). A
    forcing condition must add a conjugate-basis readout, which is new structure (outcome C).
  - **A1.** PolC uses one carrier by stipulation. The shear gets the identity as a position relabelling and
    diag(1, ±i) as its Weil image. The Toffoli is not the image of a substratum relabelling: exactly 1,344 of the
    8! permutations of 8 positions are Clifford, the affine ones.
  - **A2.** Density of PolC is open (see the report 4 section).
- *Coordinator assessment.*
  - **N1's scope is narrower than "no access condition can force the map".** N1 rules out encodings of preparations on
    which the shear acts with order 2. A substratum whose state carries a ℤ/4 extension, for example a hidden phase
    register on which the shear acts with order 4, is outside it.
    - That escape changes the substratum. It is the central extension G1 studied (`design/g1/`, complex Pauli ℤ₄
      lift), now located precisely: the quarter phase needs the layer group itself to be extended.
    - Recorded as an assumption-watch marker on candidate 2: *the polarization map's shear image is a representation
      of the ℤ/4 lift, not of the layer group on configurations.*
  - **N4 rests on a reading.** Main.md:216 concerns §3.1's continuum phase-space flow. Identifying its momenta with
    the leapfrog's previous value is an interpretive step [arg]. The discrete realization at Main.md:292 and :316
    reads both slices. So N4 establishes that the one corpus access statement of the right type, *so read*, excludes
    the target. The difference between the two surfaces is recorded and not edited.
  - **N2 is the stronger marker.** It does not depend on any encoding. On the displayed centre-free rule, the Weil
    images are real, so the polarization route cannot reach O1 without a centre term the corpus excludes.
  - My framing in "Direction after the map" is corrected in place on the agent's points: NT and both layers in the
    target, the swap half strictly weaker, Main.md:216, and S needing a centre term.
- *Consequence for node 9.* On the corpus rule, test 8 through the polarization map cannot source O1. If test 8 is
  kept, the honest target is the swap half with NT, and a positive answer gives a real, countable class. A route to
  O1 needs one of three things: a centre term, a ℤ/4-extended substratum state, or a different sourcing map. Each is
  new structure and needs an owner decision. No probe is dispatched until a candidate access condition is written
  down; the decision rule in TEST8-DESIGN §4 is ready for one.

## Owner report 5, "Can interaction select the quantum state space?" (2026-10-22), coordinator review

- *Source.* The owner's read-only session, as an HTML report pinned to `main` at `af8c59d6`. The report's checker and
  its output are committed in `design/owner-checks/report5/`.
- *Verification.*
  - The checker's sha256 `be85b0c0…` and its output's sha256 `a6445f48…` match the report's stated hashes. A re-run
    replay-matches byte for byte.
  - `coordinator_report5_checks.py` recomputes the following with genuine complex Y, not the checker's real identity
    Y⊗Y = −J⊗J:
    - CNOT conjugates Y⊗Y to −X⊗Z;
    - after CNOT, ⟨XZ⟩ = −1 and +1 for ρ₊ and ρ₋;
    - P(+Z_B) = 49/50 and 1/50 under U = (3I + 4J⊗X)/5, with best common error 12/25;
    - W = SWAP/2 gives −1/2 after CNOT ✓.
  - It also writes ρ₊ = (II + YY)/4 and ρ₋ = (II − YY)/4 as coin mixtures of real Bell states, (ψ⁺ + φ⁻)/2 and
    (φ⁺ + ψ⁻)/2, prepared from |00⟩ by H, CNOT, X and Z.
  - The cited corpus results exist on `main`:
    - `round-oi-pair-maxcone-1/result.md`, the conditional pair-cone theorem over eball 3 and Q(i);
    - `round-comp-1-composite-interface/result.md`, which has local tomography as an explicit premise and a padding
      control showing its independence.
- *Findings [rec, owner report 5].*
  - **Sufficient package.** Local Bloch-ball geometry, locally tomographic composition, continuous reversible
    interaction and one compatible family give complex QM for finite collections of qubits, by two literature results
    [Q, not read here; network-gated]:
    - Krumm–Müller, Theorem 1: a genuine interaction selects d = 3;
    - de la Torre–Masanes–Short–Müller, Theorem 2: the quantum completion.
    These premises are adopted, not derived from C1–C4.
  - **Rebit witness.** ρ₊ and ρ₋ agree on the whole nine-dimensional product-effect span of real local tests. CNOT
    separates them perfectly, and the continuous real interaction exp(θJ⊗X) separates them with gap 24/25. A quotient
    that identifies them has a fixed error ≥ 12/25 on this experiment, so no limit along such a family repairs it.
  - **Joint state set.**
    - A set of product mixtures is too small for CNOT: XX + ZZ ≤ 1 on it, and = 2 on the gate's output.
    - The set of tables that are positive on all products is too large: W = SWAP/2 gives −1/2.
    - The −1/2 is rejected only for the standard gate lift; a consistent partial-transpose twist gives 0.
  - **Continuity.** A continuous path into a finite permutation group is constant. A stochastic interpolation is not
    reversible: (id + CNOT)/2 has rank 3.
- *Coordinator assessment.*
  - **Relation to the corpus: ELABORATING.**
    - The continuity point restates Main §3.2 and the kernel's `bijectionLevel_not_layerFlowExecutable`.
    - The tomography and cone controls illustrate COMP-1, where local tomography is an independent field, and the
      pair-cone theorem's conditional inclusions.
    - GR §3.3's OI⁺ works inside a fixed complex-matrix representation (GR.md:228–242). The report's package instead
      selects the complex representation, given local tomography and genuine interaction. That difference is worth
      keeping: OI⁺ presupposes what the package's ball-dimension step decides.
  - **Cross-link to test 8, N2 (CONFIRMING, [arg]).** On the corpus's centre-free rule, the polarization route's Weil
    images are real (H, CZ, Paulis). The report's rebit witness is realized inside that real class: ρ₊ and ρ₋ are coin
    mixtures of real Bell states prepared by H, CNOT, X and Z (coordinator check). So the class the corpus rule can
    source is not locally tomographic for real local tests. Its products miss the Y⊗Y coordinate, which only an
    interaction reveals.
    - The three routes to O1 that the test-8 review named all supply the complex structure that restores local
      tomography: a centre term, a ℤ/4-extended substratum state, or a different sourcing map.
    - Local tomography is the operational form of that choice. It is the premise COMP-1 shows independent, and the one
      the literature uses to exclude real QM.
    - This narrows node 9's open question to one fork, which the report states: keep the holistic coordinate (a real
      theory), or remove it by an independent locality-of-tests condition.
  - **Scope.**
    - The 12/25 bound holds for a quotient that retains these two preparations and this experiment. It is not a no-go
      for disc theories or for deterministic OI.
    - The literature results are [Q] until read; the network blocks arXiv.
    - Calling the package C5 would be a declared axiom package, as the report says, not a derived condition.

## Owner report 6, "A physical memory register under the native update" (2026-10-22), coordinator review

- *Source.* The owner's read-only session, as an HTML report pinned to `main` at `af8c59d6`. The report's checker and
  its output are committed in `design/owner-checks/report6/`.
- *Verification.*
  - The checker's sha256 `8ae711bf…` and its output's sha256 `36242146…` match the report's stated hashes. A re-run
    replay-matches byte for byte.
  - `coordinator_report6_checks.py` was written from Main.md:290's rule and the declared graph (0, 1), (1, 2), (0, 3),
    without the checker's hand-coded update. On all 256 states it confirms:
    - the six closed forms after three updates;
    - the hidden-pair identity (u₁, v₁) = (V₂ ⊕ p, U₀ ⊕ q);
    - the six-bit decoder;
    - exact period 10;
    - support 4, 4, 2, 1, 2, 4, 2, 1, 2, 4 over one period with known memory, and 4 at every time with the memory edge
      removed;
    - at t = 3, support 4 with unknown memory and 2 with known parity ✓.
- *Findings [rec, owner report 6].*
  - A visible memory site coupled to visible site 0 evolves under the same fixed rule. After three updates, one read
    of the visible cells recovers all six initial core bits and the current hidden pair.
  - The hidden pair's conditional law is the initial memory law, shifted and exchanged:
    P(hidden | record) = μ(q = h₂ ⊕ U₀, p = h₁ ⊕ V₂). So H(hidden | record) = H(memory), and the conditional support
    is 2^(2−r) for a uniform affine memory of relation rank r. That is d_posterior's rank formula on the full
    apparatus.
  - Back-action is measured against the same evolution with the memory edge removed: 32 and 48 of 64 core states
    differ at t = 2 and 3.
  - Perfect records exist only at t ≡ 3, 7 (mod 10). Retention needs further control.
  - Two extra record bits are necessary for a single-run reconstruction of an arbitrary six-bit core, and the
    construction attains that.
- *Coordinator assessment.*
  - **Relation to node 9: CONFIRMING K-SYMP2, ELABORATING.**
    - PREREG's K-SYMP2 is Main.md:290 on two sites, with a clean visible site and a hidden toy. It already prints M0
      "lost": hidden support 1 after two waiting steps.
    - This report is the same phenomenon with a separate memory site, and it adds three things:
      - full reconstruction of the initial core, which rules out the reading that the clean values merely overwrite
        the hidden site;
      - the exact prior identity;
      - a background-subtraction control for back-action.
    - It also agrees with the BBS-check counterexample (Main.md:60's swap with an initialized hidden slot) and with
      the emb finding that the lattice gives disturbance-free records.
  - **Resource accounting (POSITIVE, for this protocol).** In this protocol the information gained equals the known
    memory relations supplied. A uniform affine memory of rank r gives H(hidden | visible) ≥ 2 − r, and the protocol
    attains equality with native dynamics and no added operation. This agrees with PREREG §1.1's clean-resource rule,
    which counts clean coordinates and read-out sites as resources. It is information accounting for this protocol,
    not an irreversible expenditure: the evolution is periodic.
  - **Consequence for model A's M0 restriction (support ≥ 2ⁿ).**
    - The witness violates M0 whenever a known visible memory pair is admitted, so the native update cannot be the
      source of the restriction.
    - A restriction has to govern the operational package as a whole: which memory preparations are admitted,
      together with which records are jointly readable. Report 7 shows that a preparation restriction alone is
      insufficient.
    - Recommendation: when PREREG is next revised, add the four-site witness as a countercontrol beside K-SYMP2, with
      the edge-removed run as its paired positive control (M0 "retained"). Its value over K-SYMP2 is the
      reconstruction clause. Not applied yet, since it is a change to a draft preregistration.
  - **Scope.**
    - The memory preparation and the terminal read are assumed, not derived.
    - The two binary coordinates of a site are not shown to represent incompatible quantum observables, so learning
      both is not a violation of QM.
    - No post-measurement preparation is established.

## Owner report 7, "Two partial memories and the role of compatible records" (2026-10-22), coordinator review

- *Source.* The owner's read-only session, as an HTML report. The report's checker and its output are committed in
  `design/owner-checks/report7/`.
- *Verification.*
  - The checker's sha256 `c23b790c…` and its output's sha256 `06a2e3e7…` match the report's stated hashes. A re-run
    replay-matches byte for byte, in 7 CPU-seconds.
  - `coordinator_report7_checks.py` was built from Main.md:290's rule on the graph (0, 1), (1, 2), (0, 3), (1, 4),
    without the checker's code. It confirms:
    - whole-site hidden support at t = 3: 1 with both memory edges, 2 with either one alone, 4 with neither;
    - (u₁, v₁) = (V₀ ⊕ V₂, U₀) on all 256 admissible states;
    - support 2 when only the visible u coordinates are read, or only the visible v coordinates;
    - the number of Lagrangian subspaces of F₂⁸ from the formula Π(2ⁱ + 1) = 2,295, matching the report's
      enumeration;
    - by an independent rank method over all 2,295: 405 with support 2, 1,890 with support 4, none with 1 ✓.
- *Findings [rec, owner report 7].*
  - **Composed-memory countercontrol.** Two memories, each with one known coordinate (u₃ = u₄ = 0) and one fair
    conjugate. The known constraints are isotropic, and neither memory pair is fully known. With both couplings, the
    whole-site visible record determines the hidden pair and reconstructs every initially unknown bit.
  - **Conditional theorem.** Assume a uniform affine preparation with isotropic known constraints, linear symplectic
    evolution, and an isotropic jointly readable record space R on the visible sector. Then K = (A_t + R) ∩ H is
    isotropic, so n hidden pairs keep support ≥ 2ⁿ. The deciding pair V₀ ⊕ V₂ and U₀ has pairing 1, so the
    whole-site readout violates the record hypothesis. No maximal isotropic readout determines the hidden pair.
  - **Narrowing.** The report narrows my report 6 statement that only a preparation restriction can enforce M0; that
    statement is corrected in place above.
- *Coordinator assessment.*
  - **The theorem is the compatible-records argument already in this file**, from the owner on 2026-10-21 (section
    "Owner inputs after revision 3", still marked to be reviewed). Report 7 adds two things:
    - a written proof in the same three steps, which the coordinator checked: ⟨k, r′⟩ = 0 by sector,
      ⟨a, r′⟩ = 0 by R's isotropy, and ⟨k₁, k₂⟩ = 0 by A_t's isotropy;
    - a native exhaustive control.
    So it is CONFIRMING for that argument. It also discharges part of that section's open review: the proof holds as
    stated for the uniform affine class.
  - **My report 6 statement was wrong.** The compatible-records argument had already made record compatibility a
    hypothesis. Saying "only a preparation restriction can enforce M0" ignored it, and I should have caught that
    before writing it.
  - **Cross-link to the corpus surfaces (open, [arg]).** The isotropic condition rules out reading both coordinates
    of any one visible site, since ⟨u_x, v_x⟩ = 1. The corpus's discrete realization reads whole sites (Main.md:292,
    :316). Its continuum §3.1 marginalizes momenta (Main.md:216), and that matches the positions-only Lagrangian,
    which keeps support 2 here.
    - So the bound-preserving interface corresponds to the reading of Main.md:216, and whole-site access in §3.2
      defeats it.
    - Test-8 N4 found the same difference between the two passages. It is recorded and not edited.
    - The two findings point the same way: the §3.1 reading preserves the knowledge bound and excludes the
      polarization encoding, while the §3.2 reading supports neither.
  - **Recommendation.** At the next PREREG revision, add both native witnesses as M0 countercontrols beside K-SYMP2:
    - the four-site witness (fails preparation isotropy);
    - the five-site witness (isotropic preparation, fails record isotropy).
    Add the positions-only readout as the paired positive control, where M0 must print "retained". Not applied, since
    it is a change to a draft preregistration.
  - **Scope.** The theorem is conditional on the uniform affine linear class, and the isotropic interface is not shown
    to be OI's. The bound does not give amplitudes, contextuality, purification, the complex field or composition.
    Learning both coordinates of a site is not shown to contradict QM.

## Owner note on records across time (2026-10-22), coordinator check

- *Source.* A short owner note relayed in chat, with no checker attached. `design/owner-checks/report8/` holds the
  coordinator's check, built from Main.md:290's rule.
- *Claim and check.* In the five-site example, a single positions-only (visible u) read leaves hidden support 2, both
  at t = 3 and at t = 2. If the t = 2 positions are retained undisturbed and read together with those at t = 3, the
  support is 1. The reason is v_x(t) = u_x(t − 1): two consecutive position snapshots carry one whole-site snapshot.
  The coordinator check confirms all of this on 256 states:
  - u₁(3) = u₀(2) ⊕ u₂(2) and v₁(3) = u₀(3), so three bits suffice;
  - the five-site period is 16, and the positions-only terminal support never falls below 2 over it;
  - the four-site witness behaves the same way: support ≥ 2 over its period of 10 with a single terminal read, and 1
    with t = 2 and t = 3 retained. The owner did not state the last fact; the coordinator check adds it.
- *Assessment.*
  - **This refines the cross-link in report 7's review, and does not overturn the compatible-records argument.** That
    argument puts every retained record into R at the terminal cut. A t = 2 position record, transported to t = 3, is
    a momentum function, so R is not isotropic.
  - So "observers read positions only" is not a sufficient access condition. The condition has to say which position
    records can coexist across time, and what recording does to the subsequent evolution.
  - Identifying the lattice's u coordinates with physical positions is itself a modelling choice. Main.md:216
    projects onto configuration variables, and the discrete realization reads whole sites.
- *Three tests, as the owner frames them.*
  - (i) Single terminal positions-only read: a positive control.
  - (ii) Positions-only with free retention across times: a negative control.
  - (iii) Positions-only with embedded physical memory, covering acquisition, storage, subsequent interaction and final
    read in one protocol: the substantive construction question, open.
  - (i) and (ii) are added to PREREG §5 as K-POS and K-POS-RET, beside K-MEM4 (report 6) and K-MEM5 (report 7), and
    the four lines are added to M0's "required for retained" list. The owner recommended the controls; the draft is
    not frozen.

## Owner direction after the open-items brief (2026-10-22)

- *Recommended order.*
  1. Manuscript correction.
  2. An explicit conditional complex-QM benchmark.
  3. Review and extension of the six-site memory construction.
  4. A bounded model A calibration, if useful.
  5. H-LOC only once its evidential value and cost are justified.
- *Manuscript correction.* The owner read Bäcker–Beyer–Strunz. Their classical-memory condition is a quantum
  instrument followed by channels conditioned on its classical outcome. That matches the instrument-realizing reading
  of `design/bbs-check/`, so the swap counterexample no longer rests on a reconstruction.
  - Draft PR #893 (branch `ccr-5e87695b-wcffoc`, from `main` at `af8c59d6`) replaces the implication with the open
    bridge requirement at Main.md:702 and :704 and GR.md:601. It also corrects the dilation-sense Class C item at
    Substratum.md:476, ch04:144 and FULL:1261, and the ROADMAP row.
  - The rebuilt artifacts and local checks are listed on the PR.
- *Corrections to the coordinator's open-items brief.*
  - **Local tomography alone does not select QM.**
    - Krumm–Müller also assume ball-shaped local state spaces, all local rotations, no-signalling, and a closed
      connected reversible group with a genuine interaction.
    - De la Torre et al. assume identical locally quantum (complex) units, local tomography, and continuous reversible
      interaction with consistent extension to further systems.
    - Adding local tomography to the existing real construction may make its assumptions incompatible rather than
      complex. Locally indistinguishable states cannot be identified while an interaction that later distinguishes
      them is retained (report 5's 12/25 bound).
  - **Real stabilizer gates are not full real QM.** The N2 class (H, CZ, Paulis) is real Clifford. Two milestones stay
    separate: supplying the quarter phase, and supplying operations beyond the Clifford/stabilizer sector. Reaching the
    first does not reach the second.
  - **A different sourcing map is additional mathematical structure, not automatically new physical dynamics.** A
    self-coupling term does change the stated update. Before the substratum is altered, the freedom in the operational
    map should be audited for consistency across preparations, interventions and composites.
- *Disposition of the fork.*
  - The real model is kept as a calibration, not an endpoint.
  - Local tomography is an explicit hypothesis of a conditional reconstruction benchmark.
  - Added phase structure is investigated through concrete implementations, with every added resource identified.
  - The reconstruction target stays complex QM.
- *Memory item: conditional construction found, closure unresolved.*
  - The owner reports a six-site construction: fixed native dynamics supply a physical record, and its recording
    back-action keeps the bound under the declared positions-only terminal readout. The correlated initial preparation
    is assumed.
  - The coordinator has not received this construction's report or checker, so it is unverified here.
  - Next questions:
    - whether declared resources can generate the correlated ready state;
    - whether the record can be preserved, transferred and reused;
    - whether heralding with actual back-action keeps the restriction;
    - whether all jointly retained records stay compatible.
- *Model A, decisions.*
  - The primary exhaustive scope is n ≤ 2. n = 3 is optional corroboration after a cost estimate, not an automatic CI
    requirement.
  - Fix the preparation resources and operation alphabet before choosing *s_max* and *d_max*. A cap reached without a
    completeness argument is PARKED or bounded evidence, never a general success or failure.
  - The pointer policy and Π_ω need executable definitions, with native operations kept distinct from added interface
    assumptions.
  - The spectator-stability clause (S) is retained, which confirms item 7 of "Remaining before freeze".
  - Q6: do not broaden M5 unless the extra statistics separate surviving candidates.
  - Q7: mark M4 inapplicable to Option A.
  - Q8/Q9: run the quote check and publish explicit exclusions.
  - Verify the emb correction N1 by diff, and include the compatible-records proof in the baseline.
  - Passing the four native controls (K-MEM4, K-MEM5, K-POS, K-POS-RET) validates the checker's sensitivity. It does
    not prove closure.
  - These decisions are applied to PREREG at its next revision, if model A is still to be executed.
- *H-LOC (deferred).*
  - A tie between genuinely inequivalent surviving classes refutes the unique-selection claim within the declared
    family. It refutes neither locality nor OI. Equivalent descriptions are quotiented before ties are counted.
  - A reduced test is independent evidence only if its target was not fixed by the results used to design it;
    otherwise it is a consistency check.
  - No 20–3,000 CPU-hour run without a pilot giving a credible cost estimate, and only if the result would change a
    research decision.
- *Reviews, by dependence.*
  - First: PR #893 and the six-site construction.
  - Then: model A's exact revised PREREG, if it is to be executed.
  - The corrected card report and the H-LOC draft are reviewed before renewed use.
  - Earlier report reviews get targeted checks of their consequential claims, not blanket replays.
  - Literature-dependent controls stay gated: a freeze may carry an unresolved gate, but never counts it as verified.
- *Parked.* Relativity stays parked. The book/card discrepancies are revisited when a current argument depends on
  them. The network block does not set research order.

## Conditional complex-QM benchmark: first deliverable (2026-10-22)

- *Owner instruction.* Keep both routes side by side, and draft the unfrozen design note now.
  `design/benchmark/BENCH-DESIGN.md` carries:
  - the premise ledger:
    - route K: GR §3.3's well-formedness K-W1/K-W2 plus K1–K3, with conclusion scope exact finite endomorphic
      operational QM, and the K2′ primitive-source certificate;
    - route L: L1–L6 as expanded by the owner, plus the coverage line L7;
  - the theorem-dependency map;
  - the proposed scoring rules;
  - control scores for both routes.
- *Owner corrections, applied.*
  - The routes have different jobs.
  - The baseline meaning of Native is frozen at `fc9018e8`, and later observer restrictions stay Added.
  - An evidence column separates proof, bounded computation and assumption.
  - The theorem verdict requires every hypothesis for the same candidate, interpretation and completion.
  - Added premises are not counted as a distance from a derivation.
  - The theorem and adoption verdicts are separate.
  - The controls are corrected and separated: the classical bit fails d ≥ 2; the 12/25 bound is scoped; the real
    Clifford class is distinguished from full real QM; stabilizer preparations and their closure are separated;
    Spekkens and boxworld have their own rows, with named failed premises.
  - The milestones are diagnostics D1–D5, not conclusions.
- *Exact check.* `bench_controls_span.py` computes the product-effect span for four controls: 16 of 16 for complex QM
  and the stabilizer theory, and 9 below the joint 10 for the rebit and the real Clifford class.
- *Every kernel identifier the note cites* was confirmed present under `verification/lean-mathlib/OIBridge/`. No build
  was run.
- *Open before freeze:*
  - the literature gate: quote the Krumm–Müller, de la Torre et al. and Gross et al. hypotheses;
  - the rows marked [arg] or [open];
  - the six-site construction's report and checker;
  - then score the candidates.

## Owner reports on native memory, 2026-10-22: product-ready memory, relay, two-record mask, heralding closure

- *Source.* Four HTML reports from the owner's read-only session. Their four checkers and outputs are committed in
  `design/owner-checks/report9/` with `SHA256SUMS`.
- *Verification.*
  - All eight sha256 values match the reports' stated hashes. All four checkers replay byte for byte, the longest in
    5 CPU-seconds.
  - `coordinator_report9_checks.py` was built from Main.md:290's rule on the declared graphs, without the reports'
    code. It confirms the following.
  - Product-ready six-site memory:
    - with v₃ = v₄ = u₅ = 0, the period is 18 and u₅(2) = u₁(2) = u₀(1) ⊕ u₂(1) on all 512 states;
    - the hidden support under visible-u reads is 4, 2, 2, 4, 4, 2, 2, 4, 4, 4, 2, 4, 4, 2, 4, 2, 4, 4 over the period,
      and 1 if v₅(2) is also read;
    - the historical parity is recoverable only at t = 1, 2, 11, 15.
  - Relay, k = 0–3 enumerated: u₅₊ᵣ(2 + r) = f for r ≤ k, the periods are 18, 24, 20 and 56, and the minimum hidden
    support over each period is 2.
  - Seven-site masked conjugate: m = u₀(2) ⊕ u₆(2) = v₁(2) ⊕ r, and r is fair on all 64 complete records. Also
    u₄(12) = u₆(0).
  - Four-site heralding:
    - success probability 5/8;
    - accepted output 2/5, 2/5, 1/10, 1/10;
    - free-history countercontrol at t = 6: 4/5 and 1/5;
    - all six two-point subsets of F₂² are affine lines, so the vertices of {p_x ≤ 1/2} are uniform line states.
  - Not independently rechecked: the 14-site two-record count (2²⁰ states) and the relay rows for k ≥ 4. Both rest on
    the replayed checkers.
- *Findings [rec, owner].*
  - **Acquisition.** A product preparation with one known coordinate per memory site acquires an earlier parity
    under fixed native dynamics. The correlated preparation is unnecessary: it is one native step from the product
    menu. Back-action keeps the hidden support at 2 or more. Cancelling the kick is not symplectic.
  - **Storage.** A relay chain of k added sites guarantees readability through t = k + 2. There is a written proof for
    every k, and exhaustive checks for small k. A finite closed reversible device cannot keep a record readable at all
    late times (finite recurrence).
  - **Two records.** Compatible records of two toys coexist, with joint hidden support 4. For a conjugate attempt on
    one toy, the second record carries an unknown mask.
  - **Support versus weights.** Biasing the mask bit to P(r = 0) = p keeps support 2 but makes the second coordinate
    predictable with probability max(p, 1 − p). The time-2 position statistics are the same for every p; u₄(12)
    reveals p.
  - **Heralding closure.** Let Kₙ be the convex hull of uniform distributions on affine sets with isotropic
    constraints (K₁ = {p_x ≤ 1/2}). Kₙ is closed under affine symplectic evolution, isotropic terminal reads,
    conditioning and coarse heralding. Native heralding produces a nonuniform state inside K₁. Retaining the herald
    as free external history and reusing the apparatus produces the excluded biased line state.
  - **Literature named by the owner** [Q, not read here; `link.springer.com` and `arxiv.org` are denied by the
    proxy]:
    - Fankhauser, Gonda and De les Coves, *Synthese* (2025): a Lagrangian accessible-variable subspace
      (Definition 2.5), ready-state measurements, and Theorem 3.1 (measurable variables ↔ vanishing Poisson
      brackets);
    - Spekkens, "Quasi-quantization", arXiv:1409.5041 (2014): binary versions are not stabilizer QM.
- *Coordinator assessment.*
  - **CONFIRMING** the compatible-records argument and its stated scope.
    - Every positive construction is an instance of it.
    - The free-herald countercontrol is the failure its scope note already names ("a free external record breaks the
      premise").
    - The temporal-retention countercontrol K-POS-RET is the same failure across time.
    - The finite recurrence lemma for storage restates report 3's fixed-carrier recurrence lemma for a historical
      bit.
  - **ELABORATING:** concrete native acquisition, relay and closure constructions, with resources stated.
  - **Prior art for the mechanism.** The Fankhauser–Gonda–De les Coves framework, as the owner summarizes it, has the
    same structure as the compatible-records argument: a Lagrangian accessible subspace, with measurability given by
    vanishing brackets. The thread claims no novelty for the mechanism. A comparison of their observer premises with
    OI's interface is the owner's proposed next step. It is gated here until the paper can be read.
  - **The support-versus-weights finding bears directly on the draft PREREG (POSITIVE, a hidden assumption).**
    - M0's restriction is support-based: "support ≥ 2ⁿ" (PREREG §4). The biased-mask family satisfies it while making
      a conjugate coordinate predictable with probability close to 1. So the support form gives no guessing-probability
      bound.
    - Kₙ membership is the distributional form that the heralding closure theorem preserves under the declared
      operations. It implies point probabilities ≤ 2⁻ⁿ but is strictly stronger than that bound.
    - Recommendation, an owner decision, not applied: if model A is to be executed, restate M0's restriction as Kₙ
      membership of the toy marginal on every accessible record. Keep the support line as a reported diagnostic, and
      add the biased-mask family as a countercontrol, where support-M0 should print "retained" and Kₙ-M0 "lost".
  - **All-future equivalence: CONFIRMING.** The u₄(12) read separates preparations that agree on every current read.
    PREREG's Lemma W equivalence is already taken at unbounded depth, so snapshot equivalence is not what it uses.
  - **Benchmark.** The memory constructions enter `design/benchmark/` as a positive calibration row. They are native
    evolution within a declared memory construction, with added preparation and readout premises, and bear only on
    the compatible-records interface candidate. They score nothing on L1–L6.

## Owner decision: the Kₙ form of M0, and checked literature (2026-10-22)

- *Decision (owner, PREREG Q14).* M0's restriction becomes Kₙ membership of P(h | r) for every nonzero-probability
  physically available record, and stays a calibration condition of model A.
  - It was adopted after the native-memory results were seen, and the draft says so.
  - Three qualifications are written into PREREG:
    - M0 tests the preparations actually generated, never "allowed because they pass Kₙ";
    - membership is kept separate from reachability;
    - the finite menu is kept separate from its convex completion.
  - Support size, maximum point probability, guessing probability and single-toy K₁ membership are reported as
    diagnostics.
  - Membership is decided by exact rational feasibility over the uniform isotropic affine states (7 at n = 1, 91 at
    n = 2), and each verdict carries a certificate: mixture weights or a separating functional.
- *New countercontrols, in PREREG §5 and `design/kn/kn_controls.py` [exact].*
  - **K-BIAS-MASK.** A line with weights p, 1 − p. Support is 2, yet it lies outside K₁ for p ≠ ½. The guessing
    probabilities are 3/4 and 99/100 for the two biased cases; p = ½ is the paired positive.
  - **K-COMP2**, owner's example. Uniform on q₁ = q₂, p₁ = 0:
    - support 4, maximum point probability ¼, and both marginals in K₁;
    - outside K₂: the two constraints have bracket 1, and none of the 91 isotropic uniform states has support inside
      the set.
    - It rejects any checker that tests only support, point probability or marginals.
- *Fankhauser–Gonda–De les Coves* [rec, owner-checked; not readable here].
  - They define the observer's accessible variables as a Lagrangian subspace, and prove that the measurable linear
    variables are exactly those with vanishing mutual brackets.
  - The access restriction is part of their observer definition; symplectic dynamics does not supply it.
  - Their exact-learning requirement holds for every observer-conjugate value. It gives no guessing bound for
    arbitrarily biased distributions, so the probabilistic preparation and closure premises (Kₙ, heralding closure)
    stay essential.
  - **The concrete bridge for OI:** why its physically accessible records, stored records included, have compatible
    structure. Whole-site access (Main.md:292, :316) does not supply it.
- *Benchmark literature, owner-checked.* `design/benchmark/BENCH-DESIGN.md` now records the checked scopes:
  - Krumm–Müller Theorem 1;
  - de la Torre et al. Theorem 2;
  - Gross et al. Theorem 1, which covers full boxworld only and is not a theorem about every theory containing a PR
    box; the paper discusses hybrid exceptions.

  Verbatim quotations with locations remain to be recorded.
- *Next (owner):* a focused revision and review of model A's Kₙ test, including both countercontrols. In parallel, the
  benchmark carries the checked hypotheses. The memory constructions stay evidence about physical records; they do
  not supply geometry or composition.

## Review of the Kₙ revision (`1dcbde1d`) and corrections applied

- *Review.* A read-only reviewer worked from independent enumeration, an exact simplex with certificates, and a
  separate certificate verifier: `design/kn/review/REVIEW-KN.md` and `kn_review_checks.py`/`.out`. The coordinator
  re-ran the checker: it replays byte for byte, both in the reviewer's directory and in place. Verdict: **REVISE**.
  - The mathematics holds: the definition, K₁, the counts 7/91/2,467, the completeness of the Farkas test, convexity,
    and closure under marginals onto whole pairs.
  - The controls and the certificate path did not hold.
- *Coordinator check of the decisive witnesses [arg].*
  - **K-CORR2 is outside K₂.** Its support is a single isotropic uniform state's support. Every isotropic state has
    support of at least 4, so that state is the only possible component, and the weights are not uniform.
  - **K-MIX2 is inside K₂** by definition.
  - **My `in_Kn_by_support` docstring was false.** Uniform on 3 points is in K₁. It is replaced by a one-directional
    test, which is valid for K-COMP2.
- *Applied to PREREG.*
  - B1: K-MIX2 (positive) and K-CORR2 (countercontrol).
  - B2: in I-19, a generator census against the counting formula (7, 91, 2,467, 150,451, or the Lagrangian cosets 6,
    60, 1,080, 36,720), re-verification of every certificate by separate code, a static check that no diagnostic enters
    a verdict, and mutants KM-38 to KM-41 (support form, vertex-only, support plus marginals, dropped generator).
  - B3: the script is corrected, and certificates are cited from the review checker.
  - N1–N8:
    - the stale support sentence is removed;
    - the K-CLN-A, K-POS and K-REUSE arm 2 verdicts are restated in K₁ terms, K-REUSE's weights to be checked at
      execution;
    - "lost" rows print a separating functional, with support as a diagnostic;
    - K-CLN and K-CLN0 are noted as not exercising the Kₙ test;
    - h is stated to be whole pairs;
    - "accessible record (§1.1)" is used;
    - the weights are named P(P | r);
    - the qualifications are cross-referenced to I-6 and I-20;
    - "arbitrarily close to 1 (99/100 tested)".
- *Still open.* No re-review of this correction yet. The draft is not frozen.

## Owner report, "Preparations, readouts and instruments" (2026-10-22), coordinator review

- *Source.* An HTML report from the owner's read-only session. Its checker and output are committed in
  `design/owner-checks/report10/`.
- *Verification.*
  - The checker's sha256 `760455f5…` and its output's sha256 `584d45f4…` match the report's stated values, and a
    re-run replays byte for byte.
  - `coordinator_report10_checks.py` is separate code. It builds the two-preparation first-read feasible set exactly,
    as a zonotope, and tests the targets against its edges. Results:
    - The correlated repair's target (17/20, 3/20) is infeasible. The maximum of P₊ − P₋/2 over the set is 3/4,
      against 31/40, and (5/6, 1/6) is feasible.
    - The independent product encoding is infeasible.
    - The triple-correlation control is feasible, with response (17/20, 3/20), E(x, y, z) = (±½, ±½, 0) and total
      variation 1.
    - ((X + Y)/2)² = I/2, so the quantum trace distance is 1/√2.
    - Three retained nondisturbing reads give gap 1757/2000, with square > ½.
  - The first version of my zonotope walk had a sign-order bug. The triple-correlation positive control caught it.
- *The three points the owner asked a reviewer to check [arg].* The coordinator checked these, not an independent
  reviewer:
  - **The supporting half-space certificate is correct.** max over e ∈ [0, 1]^Λ of yᵀDe = Σ_λ max(0, (Dᵀy)_λ). The image
    D[0, 1]^Λ is a compact convex zonotope, so these inequalities for all y are necessary and sufficient.
  - **The same-copy scope is correct.** The Helstrom bound limits any measurement sequence with feedback on one copy
    to the trace distance, here 1/√2. It does not limit three independently prepared copies, and the report makes no
    such comparison.
  - **The distinction between first-read responses and instruments is correct.** Feasibility of D e = p says nothing
    about post-measurement updates. Repeatability fails for the fixed noisy response, whose values on the carrier are
    only 3/20 and 17/20.
- *Coordinator assessment.*
  - **CONFIRMING.** The |E(A)| + |E(B)| ≤ 1 bound for Kₙ under incompatible parities is the diamond witness of
    reports 3 and 4, and the purification diagnostic restates Lemma G's family under the convex Kₙ. These are
    calibrations under a fixed mapping, as scoped.
  - **ELABORATING.** The new content is the exact first-read test with dual certificates, and the separation of three
    failure modes on one example: insufficient distinguishability, sufficient distinguishability that is still
    infeasible, and a feasible fit that exposes too much under extra or sequential reads. The mechanisms are standard
    (Helstrom; preparation dependence versus preparation contextuality, Spekkens 2005), and the report claims no
    novelty.
  - **Placement.** Recorded in the benchmark as diagnostic D6, the single-system instrument screen, with the three
    encodings as its controls. Not added to PREREG: model A's question is M0 closure, and D6 applies to candidates.
    The owner's handoff asks to record the bounds with their fixed-mapping scopes and to carry the correlated failure
    and the sequential control to the next design review; both are done here.
  - **Next (owner):** declare preparations, accessible readouts and post-measurement dynamics together, before larger
    lattice constructions.

## D6 instrument benchmark built (owner specification, 2026-10-22)

- *Owner input.* D6 was a complete first-read test plus specific countercontrols, not a test of measurement
  sequences. The owner specified the next step:
  - a finite menu: X, Y, Z and R;
  - the eigenstate preparations together with r±;
  - outcome and update rules declared together;
  - tests of repetition, switching, retained outcomes and feedback, with physical record locations;
  - tests of extra accessible reads;
  - a positive control for complete instruments that imports quantum rules and is not a candidate.
- *Built.* `design/instrument/INSTR-DESIGN.md` and `instr_bench.py`/`.out` (exact; replays byte for byte; 2 CPU-seconds).
  - **Tests.** T1 first read, T2 repetition, T3 all fixed sequences of length ≤ 3, which covers adaptive strategies,
    and T4 the optimal adaptive depth-3 discrimination against the quantum trace distance.
  - **Positive.** The quantum reference and a label + seed deterministic dilation both pass T1–T4.
  - **Countercontrols:**
    - no state update: P F F F;
    - a wrong update: P F F P;
    - an accessible label read: P P P F;
    - report 10's triple-correlation encoding: P F F F. Its sharp X, Y, Z reads already expose h = xyz, so r± are
      separated perfectly at depth 3.
- *Disclosure.* Two of my declared expectations were wrong, both underpredicting failures: no-collapse also fails T4,
  and triple-correlation also fails T2. The checker was correct on analysis, and the expectation table was corrected
  after the first run. A float leak in V₀ was fixed before recording.
- *Scope.* Depth 3, a single qubit, no composites. Passing is evidence at that depth only.
- *Next.* Candidates are to be specified in this kernel format, starting with an OI construction that declares
  preparations, accessible reads and updates from its own dynamics. The Kₙ re-review and the source comparisons run
  alongside and do not block it.

## Owner review of the D6 instrument benchmark (2026-10-22), corrections applied

- *Owner review.* The owner reproduced the published output and found two gaps. Neither changes the six
  classifications.
  - **(1) No validity gate.** A model with cancelling negative transition weights scored PPPP. Coordinator check: its
    statistics match the reference on all 840 sequence–preparation pairs, so only a gate can catch it.
  - **(2) No coverage gate.** A model declaring no preparations passed vacuously.
  - The mathematics was confirmed:
    - fixed sequences cover adaptive strategies, given kernels that depend only on the current state and the
      measurement;
    - T4's same-copy comparison is appropriate;
    - the triple-correlation failure needs no extra read;
    - the record tuple suffices for this abstract benchmark.
- *Applied in `design/instrument/`.*
  - **VALIDITY gate:** exact, nonnegative, normalized kernels on every reachable state; otherwise INVALID.
  - **COVERAGE gate:** all ten preparations and the full menu are mandatory, and partial rows state k/10 and their
    menu. Only a VALID 10/10 PPPP row on XYZR can accept a candidate.
  - **The owner's two mutations as controls:** the cancelling negative weights print INVALID, and the empty
    preparation list is refused under COVERAGE.
  - **The fresh-card instrument as a restricted positive control:** reading one card coordinate replaces the other
    with a fresh card value. On menu XY it is VALID 4/10, PPPP. This "fresh card" reading is the coordinator's
    construction of the owner's description.
  - **The triple-correlation row** now states 2/10.
- *Four-state rotated-read obstruction (owner, checked exactly).* With the card preparations X±, Y±:
  - TV(X+, Y−) = ½, while R needs the gap 9/10 − 1/5 = 7/10;
  - the minimum worst-case error is exactly 1/10, attained by the response (1, 3/5, 2/5, 0);
  - **Decision recorded:** no search for an R update while these preparations are kept.
  - It is the measurement-side form of the diamond obstruction; the card preparations are K₁ line states.
- *Owner's order for the first substantive candidate.* Change the preparation encoding and its physically accessible
  apparatus together. The extra preparation structure needs an independently specified source, not just another
  update formula. The candidate passes first-read feasibility before longer sequences are implemented.
