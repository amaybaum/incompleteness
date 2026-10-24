# Node 8 preregistration: independent pre-freeze review, version 5

- File reviewed: `mc8/PREREG.md`, 1284 lines, sha256
  `2ff8367fa16a231219d755477121393a66a757f012dc75bf0004524db2c28ea6` (re-verified). Line numbers refer to this file.
- Previous draft diffed: `.PREREG.rev4.md`, sha256 `e1c0994e…` (re-verified; 230 changed lines). Previous reviews:
  `review/REVIEW-prefreeze-v4.md` (7 items), `review/REVIEW-prefreeze.md` (19 items).
- Corpus: worktree `mc8w`, detached at `a501b418`, clean. `quotecheck.py mc8w a501b418` reproduced: 84 fragments,
  0 failing. Read at the base for this pass: mc-node6/NODE.md:209–214 (P1, the delay line), :226–228 (P5);
  mc-node3/NODE.md:66–73 (κ1–κ4).
- Nothing was computed under any candidate. Checked by hand: the Spekkens counts and the identification of the
  transformation group; the stabilizer instance's closure; Lemma A's proof; K-SWAP's visible sequence and C1–C4.

## Verdict: REVISE

The seven items of the previous review are fixed at the cited lines and every non-blocking note was taken (tables
below). The owner's four scope clauses are present concretely. The mathematics added since version 4 is correct
except in one place, and that place is a must-hold control: the stabilizer instance declared as the QM positive control
is **not closed** under its own two-qubit Clifford group, so as written the I-57 enumeration fails and, by the file's own
rule (l. 528: "A failure voids §6"), every §6 verdict is void. Three further changes are needed before the first
computation is "fully determined with no choice left to execution", and one set of stale mirrors contradicts the
corrected §6.2. None of the four items needs a computation; all are text fixes of a few lines each. After them the
draft is freeze-ready.

***

## Blocking changes

1. **The QM positive control is not closed as claimed (l. 528; also l. 1039, 1259).**
   - The declared two-qubit state set is "the 60 two-qubit stabilizer states, the products of a stabilizer state with
     I/2, and I/4", with the two-qubit Clifford group as unitaries and "Closure: the instance is closed under the Clifford
     unitaries, Pauli readouts with conditioning, and partial trace".
   - Counterexample, by hand: CNOT maps |+⟩⊗|0⟩ to |Φ⁺⟩ and |+⟩⊗|1⟩ to |Ψ⁺⟩, so CNOT (|+⟩⟨+| ⊗ I/2) CNOT† =
     (|Φ⁺⟩⟨Φ⁺| + |Ψ⁺⟩⟨Ψ⁺|)/2 = (I⊗I + X⊗X)/4, which is not a product of a stabilizer state with I/2 (its Pauli expansion
     has an X⊗X term and no single-qubit term). The same state is the post-measurement state of X⊗X with conditioning on
     ψ⊗I/2. So the declared set is closed under neither operation; I-57's enumeration fails; the must-hold control fails;
     §6 is void.
   - Fix: declare the composite state set as all two-qubit stabilizer states, mixed included: the 60 pure states
     (stabilizer groups of order 4), the 30 states (I ± P)/4 for the 15 non-identity two-qubit Paulis P (order 2), and
     I/4 (order 1); 91 in all, mirroring SPK's 60/30/1. This set is closed under the Clifford group (it permutes
     stabilizer groups), under Pauli readouts with conditioning (post-measurement stabilizer groups are stabilizer
     groups), and under partial trace ((I ± P)/4 traces to I/2 or to a single-qubit stabilizer state); the 12 products
     with I/2 are among the 30.
   - Scope of the purification test must be stated, since the closed set contains two-qubit mixed states with no
     purifier in the instance: Pur-E and Pur-U are tested for the system A = one qubit with purifying system B = one
     qubit, the two-qubit composite being the AB of that test; the two-qubit system's own mixed states are not
     purification targets within the instance (or add three- and four-qubit stabilizer composites). Without this
     clause "must satisfy Pur-E … on the instance" reads as including A = two qubits, which fails for lack of a B.
   - Checked for the intended test: I/2's purifications in the declared composite are the 24 entangled two-qubit
     stabilizer states (60 − 36 products), which are exactly (I ⊗ U)|Φ⁺⟩ for the 24 single-qubit Cliffords U modulo
     phase, so the local Clifford group acts transitively on them and Pur-U holds; a pure ψ's purifications are the six
     ψ⊗χ, permuted transitively by the local Clifford group. Pur-E and Pur-U hold on the corrected instance for A = one
     qubit, in ℚ(i, √2). Bell purifier of I/2: correct.

2. **§6.10's first computation still leaves four inputs to execution (l. 581–596, 522, 525, 1269–1270).**
   - (a) **Timing of φ.** For ℛ₂ (φ = swap h₁ ↔ h₂) and K-SWAP (φ = swap(x, h)) the access class depends on when φ acts
     relative to the observer's selected bijection and the coupling step within one time step, and on whether "waiting"
     is a step (the identity permutation is in the accessible set, so presumably yes). State the convention once: a
     time step is (selected visible permutation or declared coupling step) followed by φ, or φ first; readouts after
     the step. ℛ₁ (φ = identity) is unaffected; ℛ₂ and K-SWAP are not.
   - (b) **Composites.** ℛ₁'s "two copies, with shared hidden cells allowed and declared" declares nothing: say which
     hidden cells may be shared (a hidden counting-measure ancilla common to both copies, or the hidden bits themselves),
     what the joint prior set is (product of per-copy priors, or every joint prior with denominator ≤ 8 on the product
     hidden space), and whether the joint accessible class is the local permutations and local coupling steps only.
     ℛ₂ has no composites line at all, while I-52 requires composites printed per class and Pur-E needs a composite.
   - (c) **K-SWAP is not a §6.10 class but I-58 requires §6.10 to compute its access class.** §6.10 lists ℛ₁ and ℛ₂
     only; step 3 of §19 (l. 1269–1270) runs ℛ₁ᵃ, ℛ₁ᵇ, ℛ₂ᵃ, ℛ₂ᵇ and K-OPSTATE, not K-SWAP. Give K-SWAP its class entry
     under I-52 (Ω = {0,1}_x × {0,1}_h; φ = swap; no coupling step; ancilla conventions; the prior set, which the
     "operational state = hidden prior" check needs and the §6.5 row does not state; composites), and add it to the
     step-3 order. §16's non-gem clause (l. 1163–1164) should name it with ℛ₁ᵃ and ℛ₂ᵃ: its R1 line is a Lemma A corollary.
   - (d) **CL-C4 misdescribes node 6's P1 and states no φ.** mc-node6/NODE.md:211–212 defines P1 as the dynamics
     (x, h) ↦ (h, x) with visible history x₀, x₁, x₂, that is, φ = swap; C4 holds there because the swap is autonomous.
     l. 525 instead says "option-(B) access with the swap as the declared coupling step", which makes the swap
     observer-selected and leaves φ unstated; with φ = identity that realization has the same structure as K-OPSTATE,
     which l. 523 says fails C1, while l. 525 requires K-C1C4 to pass. Fix: CL-C4 is φ = swap with no coupling step, the
     prior a datum with denominator ≤ 8 (it then coincides with K-SWAP up to the prior set and initial x; say so, or
     merge the two rows and keep both roles).
   - Also at l. 587: "every hidden prior with denominator ≤ 8" should name its domain. §2.2 (l. 188–189) makes hidden
     ancillas counting-measure cells, so the prior is on h alone; then a preparation bijection of the four hidden bits
     composed with a prior p gives h-marginals p·k/8 + (1 − p)·k′/8, denominators up to 64. The preparable set is
     determined by the inputs, so this is not a choice, but the phrase should not suggest the preparable set is the
     denominator-≤ 8 grid; write "the realization-datum prior on h has denominator ≤ 8; the preparable set is whatever
     the declared ancillas and preparation bijections yield from it, printed (I-54)".

3. **Stale mirrors of corrected content (l. 999, 1248, 1240, 235, 1033).**
   - l. 999, the scorecard's R1 cell for C5-P: "witness from §6.2 (CL, K-PR6, fiber freedom), exact". §6.2 now says CL
     fails C1 and is not a witness and `fiber_freedom` is not a witness (l. 469–470); I-56/KM-28 refuse exactly this
     cell. Write "witness from §6.2 (CL-C4, K-SWAP, K-PR6 or a §6.10 class, each with its K-C1C4 printout), exact".
   - l. 1248, I-48: "K-TRANS: on CL and on the qubit control … classical permutations on vertices; unitaries on the
     Bloch sphere instance" contradicts the K-TRANS row (l. 1037: CL-C4 and the stabilizer instance, hypothesis Pur-U
     checked first) and names an instance the file no longer uses. Align with l. 1037.
   - l. 1240, I-40: "9 product effects equal" should read "equal on the span of the 9 product Pauli operators" as l. 519
     and l. 1034 now do.
   - l. 235: "Under κ2 the inverse bijection is accessible (node 7's PC-4a [rec])" is false under option (B): the
     inverse of ℛ₁ᵇ's declared coupling step (h ^= r then x ^= h, with r consumed) is not a declared step. Since
     reversibility is measured, delete the clause or restrict it to the accessible visible permutations.
   - l. 1033, K-IF's class list omits CL-C4 and K-SWAP, both of which §6 uses as controls and I-38 says K-IF covers.

4. **New invariants without a mutant (l. 1254, 1255, 1258, 1259).** I-52, I-53, I-56 and I-58 carry KM-30, KM-27,
   KM-28 and KM-31. I-54 (mixture rule), I-55 (equivalence domain), I-57 (QM closure) and I-59 (two purification
   readings; a unit test only) have checkpoints but no mutant naming a failing case. Add, in §14's manner: KM-32 (I-54;
   case: the pure set of ℛ₁ computed with real convex combination so that only δ₀, δ₁ print pure while the preparable-set
   rule is in force); KM-33 (I-57; case: ω_{1/3} inserted into the one-qubit instance, caught by the field check);
   KM-34 (I-59; case: a grid Pur-E pass printing "purification holds" without the closure line); KM-35 (I-55; case: a
   D2 line scoped to Q_fb while the declared domain is a fixed carrier). Mutants on the Spekkens construction
   (a size-8 set that is not a coset admitted as a state) would also test I-3's transcription of l. 520.

***

## A. The seven items of REVIEW-prefreeze-v4, verified at the cited lines

| # | prior item | status | where |
|---|---|---|---|
| 1 | full κ2 access decides §6.10 at freeze | fixed: option (B) adopted and disclosed; Lemma A written with hypotheses and proof; φ stated per class (ℛ₁ identity, ℛ₂ swap); I-52 prints inputs with digest; ancilla conventions fixed (visible point mass at 0; hidden counting measure, number per class stated); consequences stated as expected shapes and non-gem; residual: item 2 above | l. 105–113, 174–189, 433–453, 581–596, 1163–1164, 1252 |
| 2 | pure / mixture / convexity ambiguous | fixed: mixture is the physical operation with preparable weights; state set finite and not convex-closed; pure relative to it; convex closure a separate object; I-54, I-59; Lemma K (i) and Q-PREP's reading stated | l. 202–230, 1254, 1258 |
| 3 | R1 witnesses: C1–C4 not required; fiber freedom; conclusion pre-stated | fixed: K-C1C4 required of witnesses; CL excluded; `fiber_freedom` excluded with the level argument; "not supplied by the corpus; whether C1–C4 imply it is R1"; I-56, KM-28; residual: scorecard l. 999 (item 3 above) | l. 460–472, 513–515, 1256, 1095 |
| 4 | SPK two-toy-bit set from memory | fixed: combinatorial rule written (cosets of W^⊥, W isotropic; affine symplectic maps; coset partitions), tagged as the node's reading, discrepancy via PC-SPK; counts verified below | l. 520 |
| 5 | QM instance unfixed | partly fixed: states, unitaries, composite, purifier and field named; closure claim false (item 1 above); K-TRANS now checks hypothesis and conclusion | l. 528, 1037 |
| 6 | PC-CDP contradiction; provisional row feeding Emergence | fixed: one rule (rows print provisional; a provisional row classifies Parked and yields no final supplied / Emergence / C6 label); I-53, KM-27; §13.1 Emergence names the gate; the C5-P class Parked while unmet | l. 561–567, 975–977, 1253, 1094 |
| 7 | §7.5 rows 4–5 name no class | fixed with the proposed wording | l. 704–705 |

Non-blocking notes of v4, all taken: RQ purification half in house (l. 519, 1034); SPK-conv decided by Lemma K with the
computation confirming the instance (l. 521); the trivial system defined (l. 190–191); Lemma K (i) cites F-2 (l. 410);
the equivalence domain tied to D2's scope and declared before step 3, I-55 (l. 969–971, 1255); K-OPSTATE fails C1,
stated at both sites (l. 523, 600); D2's G6 rule can only refute, the isomorphism construction establishes (l. 538–540);
expected shapes stated for §6.10, R1, D2 under option (B) (l. 105–108, 450–451, 542); K-PR6 "admits K-C's
realization: yes/no" with Q-FIN carrying a vacuous rejection (l. 328–329); MC7 NODE.md:42–43 (l. 95); "additional-
consequence requirement" reconciled with "postdiction requirement" (l. 957).

## B. The owner's four scope clauses

1. **K-SWAP** (l. 522; l. 182–187; I-58; KM-31). Construction as the owner stated: x visible initially 0, hidden h,
   φ = swap, no coupling beyond φ, readouts each step. Visible sequence checked: (0, h) → (h, 0) → (0, h) → …, so
   0, h, 0, h; at step 2 the visible value is 0 for both h and the two histories (0, 0) and (0, 1) predict different
   next values, which is C4 in Main.md:80's form; C1 (the transition at step 1 depends on h), C2 (h survives, carried
   in x and back), C3 (one bit for one bit) hold. Must-hold on the restricted interface: present ("the restricted
   interface must admit K-SWAP"). §6.10 prints each class's access class before any purification verdict: present
   (l. 184–186, I-58). "Restricted access is never asserted from the primitive list": present verbatim (l. 184).
   Residual: K-SWAP needs a §6.10 class entry (item 2c).
2. **Preparable-weight mixtures** (l. 202–223). Distinct from convex mixtures: yes. Embedding under added ancillas
   with 1/8 → 1/16: l. 211–213. Purity within a budget and across the theory: l. 213–215. Declared convex-closed
   completion with the operations extending to it, extension printed per class: l. 215–218. The "looks pure because
   decomposers are missing" hazard: l. 218–219. Finite-grid purification does not establish CDP purification or exact
   QM: l. 220–221. Lemma K not applied where its hypothesis fails: l. 221. Two printed verdict lines, Pur-E on the
   preparable set and on the convex closure: l. 221–223, I-59. Complete.
3. **Lemma A** (l. 433–453). Hypotheses (A1) full simplex or grid, (A2) the interface distinguishes distributions by a
   composed protocol, (A3) classical product composites: present and each "to be checked on a class before the lemma is
   applied". "Recovering a state by repeated experiments is tomography, which quantum states also allow": l. 447–448.
   Re-check where a preparation restriction remains: l. 448–449. Complete. Proof checked, see D.
4. **C1–C4 required of R1 witnesses only** (l. 513–515) with a role column on every control (l. 517–528: RQ,
   SPK-orig, SPK-conv, K-SWAP, K-OPSTATE, CL, CL-C4, BW, K-PR6, QM each carry witness / calibration). Complete.

## C. Is §6.10 fully determined?

Fixed: Ω per class; φ per class (ℛ₁ identity; ℛ₂ swap); accessible bijections (every permutation of the visible
configurations); coupling steps (clean and destructive forms, the destructive one with a fresh counting-measure bit per
use, after node 6's P5, which I read at mc-node6:226–228 and which matches); ancilla conventions (§2.2 and "up to two
visible, up to three hidden", budgets assessed per count); priors (denominator ≤ 8, domain to be named); the access-class
computation (I-58); the two purification readings (I-59); the I-52 digest. Not fixed: the φ timing convention, the
composites of both classes, K-SWAP's inputs, CL-C4's φ (item 2). The old unrestricted 𝒫(V) wording is gone: every
remaining "unrestricted" or "full access" (l. 106, 109, 181, 433, 438, 542, 1146) names Lemma A's hypothesis, the
drafting history, or Main.md:407's behaviour class.

## D. The fixed instances, checked by hand

- **Spekkens rule (l. 520).** ℤ₂^{2n} with the standard symplectic form; every subspace is isotropic in the sense
  ω(w, w) = 0 automatically in characteristic 2, and the file's condition (ω vanishes on W × W) is the right one.
  n = 1: isotropic W are {0} (one state of size 4, the mixed state) and the three lines (W^⊥ = W, two cosets each): 6
  pure states of size 2. Correct. Affine symplectic maps of ℤ₂²: Sp(2, 2) ≅ S₃ times 4 translations = 24 = S₄, all
  permutations of the four ontic states, as in Spekkens. n = 2: Lagrangian (dim-2 isotropic) subspaces of ℤ₂⁴ number
  (2 + 1)(2² + 1) = 15, each with 4 cosets: 60 pure states of size 4 (Spekkens' 36 product + 24 correlated = 60);
  dim-1 isotropic W: the 15 nonzero vectors, W^⊥ of dimension 3, 2 cosets each: 30 states of size 8; dim 0: one of
  size 16. 60/30/1 correct. "They permute the family": an affine symplectic map sends cosets of W^⊥ to cosets of
  (SW)^⊥ with SW isotropic, correct; conversely a permutation preserving the 30 hyperplanes preserves their pairwise
  intersections (the 2-flats), hence is affine over ℤ₂, and its linear part must preserve isotropy of planes, hence
  is symplectic, so the stated group is exactly the family's symmetry group, as Spekkens' "knowledge-balance-
  preserving permutations" (order 11520 for two toy bits) requires. Measurements as coset partitions: correct. The
  symplectic presentation is Spekkens' later (2016) form, not the 2007 paper's wording; the file tags it as the node's
  reading and routes discrepancies through PC-SPK, which is right. SPK-conv's extreme points are the 60 (the 30 and
  the 1 are averages of them), so Lemma K's hypotheses hold there as l. 521 says.
- **Stabilizer instance (l. 528).** One qubit: six stabilizer states and I/2 are closed under the 24 Cliffords and
  under Pauli readouts with conditioning; entries in ℚ(i, √2) (H carries 1/√2, S carries i). Composite: not closed as
  declared (item 1). Purification of I/2 within the declared composite: exists (the Bell states, and all 24 entangled
  stabilizer states), with Pur-U holding under the local Clifford group; stated in item 1.
- **Lemma A (l. 433–453).** The proof is correct under its hypotheses: (A2) gives a composed protocol that writes every
  hidden cell's value into readable cells, so the statistics of that protocol are the hidden distribution and two
  preparations with different distributions are inequivalent, while equal distributions give equal statistics for
  every protocol (the visible initial point mass is fixed by O3); (A1) fixes the state set; (A3) makes the composite's
  states joint distributions whose extreme points are point masses with point-mass marginals. The grid reading's
  "pure states are the extreme preparable priors" should be read with §2.2's definition (not a nontrivial
  preparable-weight mixture): on the k/8 grid with weight-1/2 mixing available, k/8 = ½((k−1)/8) + ½((k+1)/8) for
  0 < k < 8, so only δ₀, δ₁ are pure, agreeing with "extreme"; on a grid lacking weight 1/2 the two notions can differ.
  The file's instruction to re-check on the grid (l. 448–449) covers this; a note, not a blocker.
- **ℛ₁ᵃ meets (A2) in one step** (x ^= h is a declared coupling step), so its §6.10 line is Lemma A's instance, as
  l. 451–453 and l. 1163–1164 say. Under the timing convention of item 2(a), ℛ₂ᵃ with a one-bit observer and φ = swap
  also reads both hidden bits by composition (read, wait, read), so its access class is expected full as well; the
  file does not pre-state it, which is right.

## E. §A.41

Every invariant in §18 names a measuring checkpoint, I-52 to I-59 included; mutants are missing for I-54, I-55, I-57,
I-59 (item 4). The classifier cannot emit a final "supplied", Emergence or C6 label while PC-CDP is unmet: l. 563–565
(the rule), l. 975–977 (Emergence requires the gate met; provisional never yields Emergence), I-53 and KM-27; the
Conditional label needs its C6… named (l. 968), and l. 566–567 Parks the C5-P class while the gate is unmet, so no final
Conditional can print on a provisional C6 either. Consistent. Every PC gate prints "not run (precondition unmet)" and
reads only a digest-printed amendment (I-28). Table order: I-58, I-59 precede I-57 (cosmetic).

## F. Register

- All-caps tokens are identifiers only (PROG, CHSH, NODE, PREP, OPSTATE, SWAP, TRANS, PREREG, ERASE, PLAN, POVM, SUMS,
  REVIEW, IEEE, FULL, AMENDMENTS); "NOT" at l. 459 is inside a [Q] fragment of Main.md:600.
- Claims stronger than their evidence: l. 528's closure claim (item 1). Everything else labelled "expected shape",
  "must-hold" or "measured" is disclosed as such; Lemma A's and Lemma K's consequences are stated as pure mathematics on
  defined objects and re-checked per class.
- No verdict is pre-stated as a result; "under option (B) the expected shape is open" (l. 542) is right.
- No revision-history voice in claims. l. 109–113 and l. 90–92 narrate the drafting, which a preregistration's
  state-of-knowledge section may do; l. 957's "the owner's earlier text … names the same clause" is a cross-reference,
  fine here (it would not be in `papers/`).

***

## Notes (non-blocking)

1. "Provisional" is used in two senses: I-53's provisional audit row (PC-CDP unmet) and l. 992's "Emergence and
   Conditional print as provisional until the review is recorded". Name the second "pending review" to keep KM-27's
   case unambiguous.
2. K-SWAP and CL-C4 will both land in Lemma A's full-access case once the access computation reports what the owner
   expects; their R1 lines then establish R1 for C5-P by a corollary. §16 already makes a Lemma A corollary a non-gem;
   the R1 line itself still prints as decided, which is as the owner intends (a violating C1–C4 model is a positive
   finding). The live content of §6.10 under option (B) is ℛ₁ᵇ and ℛ₂ᵇ, where the fresh hidden bit per destructive
   read is what can prevent full access; say so in §6.10 so the computation's point is visible.
3. SPK-orig's Pur-E on the n = 1 system with a one-toy-bit purifier: the mixed state's purifications are the 24
   correlated states, which are the graphs of the 24 affine maps of ℤ₂², permuted transitively by the local affine
   symplectic group; the pure states' purifications are products. So on the built two-toy-bit space both Pur-E and
   Pur-U are expected to hold for A = one toy bit, as the literature the file gates says. Not to be written as a
   verdict; recorded so the measurement has a hand check to agree with.
4. l. 1163–1164's non-gem clause and l. 451's "Sub-class ℛ₁ᵃ is the intended instance": after item 2(c)–(d), list every
   full-access class there (ℛ₁ᵃ, ℛ₂ᵃ, K-SWAP, CL-C4) so that an R1 line from any of them is classified alike.
5. Bibliographic data unchanged from v4 and consistent with my knowledge; the [L-c] arXiv identifiers remain
   unverifiable here.
