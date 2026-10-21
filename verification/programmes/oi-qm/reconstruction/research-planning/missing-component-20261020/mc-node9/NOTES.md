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
- Clean resources are declared with their counts. Two counts are separate postulates of model A's interface: the
  number of visible read-out sites and the number of clean pairs. Withholding a second clean pair is not enough, since a
  second visible site alone lifts L1 [rec, design/emb at blob `4e693fb7`, reviewed REVISE → corrected].
- C-i is a disclosed design input: design/c1 at `49033a3e` (reviewed) covers the whole record lifecycle; design/emb at
  blob `4e693fb7` (reviewed REVISE → corrected) decides nothing until a review accepts it. M0 runs on the abstract pointer model, with AP-1 to AP-5 named as
  assumptions of this implementation; C1 delivers only u-reads within its search bounds.
- R-MENU is computed on the record carrier only; whether Π_ω, PP and the declaration are derivable from the substratum
  stays open (claim table, row 3).

## Open before freeze

**Q5. Sizes, depths, ancilla counts and the scope S (updated).** S = (*n*, *k*, *b_p*, *b_m*, *b_r*, *b_h*) and the
caps *s_max*, *d_max* are defined in PREREG §4.1; heralding counts separately from ordinary conditioning. Proposed
values, for the owner to fix:
- M2 at A = one and two systems, each with a same-type purifier (*n* ≤ 4 toy bits; 256 record configurations);
- M3 decoders to depth D = 3, with stability checked at D = 4;
- equivalence and M0 at *k* ≤ 2 ancillas, halting if *k* = 1 and *k* = 2 differ (PREREG §1.3);
- M0 locally at *n* ≤ 2 with *b_p* ≤ 4, *b_m* ≤ 3 (PP-2), *b_r* = *b_p* + *b_m* + 2, *b_h* ≤ 2; *n* = 3 and larger
  budgets as a CI plan; *s_max* and *d_max* set from a dry count of the closure's state space, not from wall time.

**Remaining before freeze.**
1. Q5's values, *s_max* and *d_max* fixed by the owner.
2. The owner confirms PREREG §4's PP text, clean-resource declaration and Π_ω definition.
3. A review accepts the corrected design/emb report (the review of `b71199a8` returned REVISE; corrections applied);
   until then its findings stay [rec, reviewed REVISE → corrected].
4. Q6–Q9 disposed; node 8's `quotecheck.py` run with a node-9 fragment list (Q8).
5. An independent re-review of revision 3 against the pre-freeze checklist; then the frozen sha256 recorded.
6. Not blocking (I-17 prints "provisional"): the literature gates PC-POM, PC-SPK, PC-CDP, PC-S05, PC-BRS.

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
  constructions (M5-A's A2 form), with approximation error going to 0. That limit and its convergence notion are open
  design questions.
- *Literature named by the owner [Q, not read here; network-gated]:*
  - CDP 2011: purification implies no information without disturbance;
  - Chiribella, "Agents, subsystems, and the conservation of information";
  - the phase-group distinction between Spekkens' toy theory and qubit stabilizer QM;
  - Aaronson–Gottesman;
  - outcome-deterministic contextual models of stabilizer QM.
