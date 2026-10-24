# Node 8 amendments

Amendments to the frozen preregistration (`PREREG.md`, sha256
`ca5f976071f3dc257c0e4abefff9b782c9eca0db9c06ddffea8df69f486bf9dd`, committed at `382fc9e4`). `PREREG.md` is not
edited. PREREG §19 requires amendments under `amendments/` with time and reason, before the computation they touch.
Each entry gives its date, its source, its reason, and the state of knowledge when it was written. No entry changes a
decision clause in a candidate's favour.

**State of knowledge when A-1 and A-2 were written (2026-10-21, 03:55 UTC).** No probe of step 2 had been run. The
quote check (I-12) had been run: 84/84 fragments pass at the drafting commit `a501b418`; at `382fc9e4` the fragment
`mc-node7/NODE.md:82` ("provisional on K-10 at n = 4") no longer matches, node 7's record having moved after K-10's
CI confirmation (§0). No operational state space, access class, pure set or purification clause had been computed for
any class. The expected shapes recorded in PREREG §0 and §6.10 were known; nothing else.

***

**A-1. Owner's interpretation rule for every purification verdict (owner, 2026-10-21; relayed by the coordinator).**
Written before any verdict line of step 1 was generated.

Owner's text, verbatim: "Interpretation rule (owner). A successful purification witness demonstrates what the
specified realization permits, not that observational incompleteness universally produces purification. Equally,
failure to reconstruct exact quantum mechanics in these small realizations does not by itself disprove OI or its
finite-precision (A2) predictions. Operational access, finite-set purification and convex-closure purification are
reported separately, and finite-model success is never classified as an exact quantum reconstruction."

Enforcement in the step-1 probe (`probe/p8s1.py`):
- every generated purification line is produced by one function that takes the class name and the reading
  ("preparable set, budget m" / "across the declared theory" / "convex closure") as mandatory arguments and prefixes
  the line with them; no purification line is printed by any other code path (a static scan of the probe source
  checks that the only `print` of a line containing "Pur-E" or "Pur-U" is inside that function);
- the access class (I-58), the finite-set reading and the convex-closure reading (I-59) are printed as three separate
  blocks per class;
- the generated text is scoped to "the class <name> under reading <r>"; a scan of every generated verdict line
  rejects the words "OI", "observational incompleteness", "in general", "universally", "quantum mechanics",
  "quantum reconstruction" and "QM" in a purification line (check `A1-SCOPE`), so no line says or implies that OI in
  general produces or fails purification, and no finite-model result is classified as an exact quantum
  reconstruction (I-59's unit test, KM-34).

**A-2. Confirmatory review of the frozen bytes (`scratchpad/mc8/review/REVIEW-confirm-frozen.md`, relayed by the
coordinator, 2026-10-21).** Written before the affected mutants ran and before any verdict line printed.

Defects, each fixing a mutant definition (PREREG §14):
- **D1, KM-31 (PREREG l. 1119).** Under the timing convention (§6.10) one waiting step already reads x₁ = h in
  K-SWAP, so a one-step-only computation still reports full access. The mutant's case is replaced by: "the access
  class computed from zero-step protocols only (readout of x₀)"; I-58 must catch it (K-SWAP's class must print full
  hidden access).
- **D2, KM-32 (l. 1120–1121).** On ℛ₁'s grid the preparable-weight rule also gives only δ₀, δ₁ as pure, so the
  mutant's output may equal the correct output. The fixture is replaced by one where the two rules provably differ:
  state set {δ₀, δ₁, (1/3, 2/3)} with mixing weights {0, ½, 1}; the correct (preparable-weight) rule gives three pure
  states, real convex combination gives two. I-54's check runs on this fixture.
- **D3, KM-33 (l. 1122–1123).** diag(1/3, 2/3) has rational entries and passes the field check; it is caught by
  I-57's closure enumeration (H ω H† is not an instance state). The closure enumeration is named as the catching
  check. (Not run in step 1: the QM instance belongs to the controls of step 3.)

Notes, same source:
- §16's non-gem rule for the full-access classes (l. 452–454; l. 1192 names ℛ₁ᵃ, ℛ₂ᵃ, K-SWAP and CL-C4) applies only
  if I-58 prints full access for that class; full access is never asserted before I-58 measures it. The probe prints
  the access class before any Lemma A instance is reported.
- I-50 (l. 1279) covers the ℛ₁, ℛ₂, K-SWAP and CL-C4 outputs; l. 1059's "QM must satisfy all" is narrowed to the QM
  row as scoped in §6.5.
- **CL-C4's inputs (l. 610–611), fixed explicitly.** Initial x: x₀ ∈ {0, 1}, each a visible point mass fixed by the
  protocol (node 6's P1 varies x₀ across histories; K-SWAP has x₀ = 0 only). Prior: the realization-datum prior on h
  with denominator ≤ 8, with the preparation bijections of the hidden cells, as K-SWAP. Composites: as ℛ₁ (two copies,
  one shared hidden counting-measure ancilla, local accessible class).
- **Shared ancilla, reading fixed.** Each copy's local preparation bijection may be *controlled by* the shared hidden
  ancilla s (it reads s) but acts on the copy's own hidden cells (h and its own hidden ancillas) only; no local
  preparation writes s. This is the reading consistent with "the joint accessible class is the local permutations and
  local coupling steps of each copy only" and with the ancilla's declared role, mixing (§2.2): s selects which local
  preparation each copy performs, so correlated composite states exist as 1/2-mixtures of two product preparations.
  The alternative reading, in which a copy's preparation may also write s (so that one copy's prior reaches the other
  through s), yields a different preparable set; the probe exhibits one exact element of the difference as a
  sensitivity row (`SHARED-ALT`), which decides nothing.
- KM-36's catching check is the mechanical 60/30/1 (and 6/1) count, and I-3 cites KM-36. (Step 3.)
- K-IF on SPK-conv: print the extreme points and the closure's description, not a size. (Step 3.)

Also fixed here, because the frozen text leaves them to the executor and they are needed before §6.10 runs:
- **I-55, the equivalence domain.** §13.1 names two options and Q-FIN (step 3) has not run, so the domain declared
  before §6.10 is the first option: a fixed finite carrier and finite horizon, the carriers being exactly the Ω of the
  §6.10 classes and the horizon the protocol depth the probe prints. It is printed with digest before §6.10.
- **Budgets.** "Up to three hidden ancilla bits" is read as the budgets m ∈ {0, 1, 2, 3}; the class's declared budget
  for the per-budget purity line is m = 3, and the mixing weights of budget m are {k/2^m : 0 < k < 2^m} (so m = 0
  admits no mixing operation and every preparable state of that budget is pure by the definition; this is printed as
  the definition's consequence, not as a finding). "Across the whole declared theory" is the union of the preparable
  sets of every class of the family at m = 3, with weights {k/8}. In a composite the shared ancilla adds the weight
  1/2, which {k/8} already contains.
- **Visible ancillas.** The probe checks statically that φ and every coupling step read and write only x (x₁, x₂) and
  hidden cells; the visible ancillas are then relabelings of a register the observer already knows, and the
  transformation list is enumerated over the permutations of the core visible cells with that certificate printed.

***

**A-3. Retrospective clarification made after the step-1 results of `390e252f` were seen (2026-10-21).** Recorded
under PREREG §19's discrepancy procedure ("a later discrepancy is recorded, not repaired"). Source: the independent
review of `390e252f` (findings F1–F13); the repair scope was approved by the owner on 2026-10-21 and relayed by the
coordinator. State of knowledge when A-3 was written: the complete step-1 output of `390e252f` (`probe/p8s1.run1.out`,
`probe/p8s1.run2.out`) and the review's measurements. A-3 is therefore not a preregistered choice. It changes no class,
rule, criterion or decision clause of the preregistration, and no Pur-E or Pur-U outcome of the original run.

*Preserved unchanged.* `PREREG.md` (sha256 `ca5f9760…bf9dd`); A-1 and A-2 above; `probe/p8s1.py`,
`probe/p8s1.run1.out` and `probe/p8s1.run2.out`. The first three lines of `probe/SHA256SUMS` are those of `390e252f`;
the lines for the r1 files are appended after them. The original run prints the digest of this file
(`6856df0d…5ebec` at `390e252f`), which this entry changes. A byte-identical replay of `p8s1.run1.out` is therefore
made from a checkout of `390e252f`: `python3 -I -B p8s1.py` from `probe/`.

Readings fixed by the code of `390e252f` and stated nowhere before the run:
- **Denominator ≤ 8 (PREREG l. 588–589).** For one hidden bit, the priors are the Farey set F₈, all fractions a/n with
  n ≤ 8 (23 priors). For (h₁, h₂), the priors are the joint priors with a common denominator n ≤ 8 (407 priors, 37 up
  to relabeling). Sensitivity, measured by the review with priors on the k/8 grid instead: the one-bit preparable set
  at m = 3 has 19 states instead of 63, the one-bit composites have 22719 states instead of 195769, and the R2 preparable
  set at m = 3 has 38749 states instead of 93585. The pure sets are unchanged under both conventions: point masses at
  m = 1, 2, 3, for the composites and for R2. Pur-U does not depend on the priors. Counts change, and no Pur-E or Pur-U
  verdict changes. A per-entry Farey reading for the two-bit priors was not tested.
- **C2.** PREREG §19's table gives C2 only as "memory persistence, Main.md:76", a physical-regime premise. The probe
  of `390e252f` declared C2 "by the structural reading: every step is a bijection" and measured nothing. That reading
  holds for every realization satisfying condition O, so the C2 part of the K-C1C4 control was vacuous. Bijectivity of
  a step is also not persistence of a hidden record: ℛ₁ᵇ's destructive read is a bijection on Ω × fresh and overwrites
  h. C2 is therefore recorded as **not checked**. The K-C1C4 printout states "C1, C3, C4 measured; C2 not checked". The
  R1 witness candidates are the classes that pass C1, C3 and C4 in the tested protocols. That list characterizes the
  tested realizations only and does not establish independence from all of C1–C4. An operational C2 check is to be
  preregistered before any step-3 R1 line uses the list.
- **CL-C4 at x₀ = 0 (F7).** A-2 fixes x₀ ∈ {0, 1}. Phase C of `390e252f` computed CL-C4's states, purifications and
  Pur-U at x₀ = 0 only, so the counts printed for CL-C4 are those of x₀ = 0. I-58 prints full access at both values.
  The review checked that at x₀ = 1 the collected reversible transformations act transitively on all four point masses
  (x, h), so Pur-U also holds on the declared set of initial values.
- **Pur-U on B alone (F8).** Pur-U is tested on B as a single system: a pair of purifications (a ⊗ δ_b, a ⊗ δ_b') is
  connected iff a collected reversible transformation of B sends δ_b to δ_b'. The global φ also acts on A while U_B
  runs. The witnesses found for K-SWAP and CL-C4 have two steps, so A undergoes φ² = id and is unaffected. The review's
  composite-level search with A idle confirms Pur-U for both. For ℛ₁ and ℛ₂ the failures are unconnected pairs on B
  alone.

Code repairs, in `probe/p8s1_r1.py`; `probe/p8s1.py` is kept as run. The computations are those of `p8s1.py`; the
changes concern how the verdict text is generated and gated:
- **F1, Pur-E counted.** The Pur-E count and the "fails for N states" count are taken from the purification table:
  a state passes iff at least one pure composite state has it as its A-marginal. They are no longer taken from the size
  of the single-system pure set. Two positive controls gate section 6.10, and if either fails no purification line is
  printed. K-PURPOS feeds K-SWAP's one-bit line generator the four point masses plus the correlated pure composite
  state ½(δ₀₀ + δ₁₁); the reported count must rise from 2 to 3 of 63 and must name the mixed state P(h = 1) = ½.
  K-PURPOS-SPK passes the Spekkens toy bit pair (SPK-orig, §6.5 reading; 60/30/1 states, 60 pure) through the same Pur-E
  generator; it must report 7 of 7 A-states, the mixed state included, with 24 purifications. For R2 the Pur-E lines
  are counted from the purification table of the composite pure set. That set, the 16 products of point masses, is
  established analytically by the composite lemma, and the line prints the argument. Under A-2's reading every
  composite state is ½(α₀ ⊗ β₀ + α₁ ⊗ β₁). With ½ among the weights it is mixed unless (α₀, β₀) = (α₁, β₁). A
  product α ⊗ β with α = wα′ + (1 − w)α″ is the same mixture of the products α′ ⊗ β and α″ ⊗ β, so it is mixed unless
  both factors are single-system pure. The single-system pure set is the point masses (I-54-R2), and products of point
  masses are extreme.
- **F2, Pur-U generated from the uniqueness checks.** Pur-U is tested only on states with two or more purifications.
  For each such state the probe prints "connected pairs c of t" and names every pair of its purifications that no
  collected reversible transformation of B connects. A state with exactly one purification is vacuous for Pur-U. A
  state without a purification is a Pur-E failure and is not counted toward Pur-U. The hard-coded explanation "the
  hidden cells are never written by any op or phi" is removed: φ = swap(h₁, h₂) and the destructive reads write hidden
  cells, and waiting connects δ(0,1) and δ(1,0) in every R2 class (2 of 12 ordered pairs).
- **F3.** The K-C1C4 block, the class lines and the R1-candidate list print "C2 not checked", as above.
- **F9.** K-CL and I-54-R2 gate the lines that depend on them. `pur_line` scans each line against A-1's word list before
  printing it and refuses a hit, which also fails A1-SCOPE. The final line states that HOLDS certifies the controls
  only.

The repaired run is `probe/p8s1.r1.run1.out` and `probe/p8s1.r1.run2.out`. `probe/CHANGES-r1.md` accounts for every
line in which the repaired output differs from `p8s1.run1.out`.

***

**A-4. Retrospective clarification made after the step-1 results of `390e252f` and `d924b5bb` were seen
(2026-10-21).** Recorded under PREREG §19's discrepancy procedure ("a later discrepancy is recorded, not repaired").
Source: the independent review of `d924b5bb` (notes N1–N9); the scope was approved by the owner on 2026-10-21 and
relayed by the coordinator. State of knowledge when A-4 was written: the complete step-1 outputs of `390e252f` and
`d924b5bb`, both reviews and their scratch measurements, and one trial run of `probe/p8s1_r2.py`. A-4 is therefore not
a preregistered choice. It changes no class, rule, criterion or decision clause of the preregistration, and no Pur-E or
Pur-U outcome of the earlier runs. `PREREG.md`, A-1, A-2 and A-3 above, `probe/p8s1.py`, `probe/p8s1_r1.py` and their
outputs are unchanged. The r1 output prints the digest of this file (`f0ab4db2…dcc04` at `d924b5bb`), which this entry
changes; a byte-identical replay of `p8s1.r1.run1.out` is made from a checkout of `d924b5bb`.

*1. Resource accounting across composition and discarding.*
- **The composite marginals are the next budget.** Under A-2's reading a one-bit composite state is
  ½(α₀ ⊗ β₀ + α₁ ⊗ β₁): a shared fair hidden bit s selects between two preparations of each copy, and on copy A both
  come from one prior p at budget m, α_s = (k_s p + (2^m − k_s)(1 − p))/2^m with k_s ∈ {0..2^m}. Discarding B leaves
  ½[(k₀p + (2^m − k₀)(1 − p)) + (k₁p + (2^m − k₁)(1 − p))]/2^m = (Kp + (2^{m+1} − K)(1 − p))/2^{m+1} with
  K = k₀ + k₁, and K takes every value in {0..2^{m+1}}. For each prior the A-marginals of the composites are therefore
  exactly that prior's budget-(m+1) grid, and over all priors they are the budget-(m+1) local set S_onebit(m+1) [W].
  This is §2.2(a)'s embedding rule ("a 1/8 event selected by an independent fair coin becomes a 1/16 event, and the
  randomizer costs resources") applied to the shared ancilla: s is one more hidden ancilla bit of A's preparation.
- **Measured at m = 3** (`p8s1_r2.py`, check A4-MARG). The A-marginals of the 195769 composite states are 117 states,
  equal as a set to S_onebit(4) (117), against 63 in S_onebit(3); S_onebit(3) is contained in them and 54 states are
  added. For example P(h = 1) = 1/16 is a marginal and is not in S_onebit(3). The per-prior identity is also checked on
  the grids at m = 0, 1, 2, 3 (23, 39, 63, 117 states).
- **`composite_onebit`.** Its per-prior grid is {(k p + (8 − k)(1 − p))/8 : k = 0..8}: 8 = 2³ is written into the
  function, and its arguments S_single and W are not read (check A4-GRID, an AST scan of the function body). The
  composite it returns is the budget-3 composite whatever set is passed. Every call in step 1 passes the budget-3 set
  and weights, so no printed result is affected; a call at another budget would silently return the budget-3
  composite. The function is not changed.
- **The accounting rule.** Composing at budget m and then discarding lands at budget m + 1. The step-1 local sets, as
  counted (one declared budget per class, and "across the declared theory" as the union at m = 3), are therefore not
  closed under discarding, which §2.2 lists among the allowed operations. Iterating the rule gives the union of the
  budget-m local sets over m [W].
- **Pur-E on the enlarged set is unchanged** (check A4-PURE-E). Against the pure composite states of the step-1
  composite set, which are the four point-mass products (K-CL), with A-marginals 0 and 1, Pur-E holds for 2 of the
  117 states and fails for 115; none of the 54 added states has a purification. The pure set of S_onebit(4), and the
  enlarged R2 sets, were not computed.
- **Closure, not completion.** Closure under the declared operations is the accounting rule above. It is distinct from
  the topological completion of a state set in the operational norm, which would add limit states that no finite
  budget prepares. That completion is not adopted. The convex-closure lines of step 1 remain the separate reading that
  I-59 requires, and A-4 does not change them.
- **Consequence.** The step-1 objects are the declared budget-3 sets and their composites; they cannot be read as a
  complete operational theory closed under its own operations. The eight Pur-E/Pur-U answers of §6.10 are statements
  about those declared sets and are unchanged.

*2. The composition lemma [W].* Hypotheses, for a pair of local state sets S_A, S_B with mixing weights W and an
allowed composite set S_AB:
- (H1) every allowed composite state is either a product α ⊗ β with α ∈ S_A and β ∈ S_B, or a mixture
  wπ + (1 − w)π′ with w ∈ W of two distinct allowed product states π, π′ (under A-2 every composite is
  ½(α₀ ⊗ β₀ + α₁ ⊗ β₁), with ½ ∈ W);
- (H2) every product α ⊗ β with α ∈ S_A and β ∈ S_B is an allowed composite state.

*Claim.* Every pure composite state is a product of pure local states, so its marginals are pure. Hence no mixed local
state has a purification.

*Proof.* Let ψ be pure. By (H1) it is a product or a nontrivial W-mixture of two distinct allowed states; the second is
excluded by purity (§2.2), so ψ = α ⊗ β. Suppose α is mixed: α = wα′ + (1 − w)α″ with w ∈ W and α′ ≠ α″ in S_A. By
(H2), α′ ⊗ β and α″ ⊗ β are allowed; they are distinct, since their A-marginals differ; and
ψ = w(α′ ⊗ β) + (1 − w)(α″ ⊗ β). Then ψ is not pure, a contradiction. The same argument applies to β. The A-marginal
of ψ is α, which is pure. A purification of ρ is a pure composite state with A-marginal ρ, so ρ is pure. ∎

- This is the finite-weight form of the standard fact that the extreme points of the minimal tensor product of two
  state spaces are the products of extreme points [L]. The citation was not retrieved (network-gated) and is
  unverified.
- Scope: this model family, the one- and two-hidden-bit classes of §6.10 under A-2's shared-ancilla reading, at any
  budget m, since composites keep A-2's form and products of allowed states stay allowed. It is not a statement about
  other OI constructions, other composite rules, or other realization classes. The R2 composite lemma printed by
  `p8s1_r1.py` is its instance with the R2 pure set measured by I-54-R2. K-CL checks one instance exhaustively, and
  K8-SENS checks the same instance with k/8 priors.

*3. Corrections to A-3's wording (review of `d924b5bb`, N3 and N4).* A-3 is not edited; these entries correct it.
- **N3.** A-3 says that if either positive control fails "no purification line is printed". What is suppressed is every
  realization purification line: those of the eight classes, of CL, and the summary lines. The K-PURPOS and
  K-PURPOS-SPK fixture lines are printed before their checks run and are labelled as fixtures. In `p8s1_r2.py` the
  same holds for the three added fixture lines.
- **N4.** A-3 says "PREREG §19's table gives C2 only as …". That row is PREREG l. 264, in §3 ("OI premises available to
  the derivations"), not in §19. A-3's quotation of §19 ("a later discrepancy is recorded, not repaired", l. 1310) is
  correct.

*Code repairs, in `probe/p8s1_r2.py`.* `probe/p8s1_r1.py` is kept as run. The classes, rules, criteria, computations
and §6.10 verdict logic are those of `p8s1_r1.py`, except the Pur-U status of N2.
- **N1.** K-PURPOS gains two Pur-U countercontrols on the production path (`onebit_grid_text`). With K-SWAP's
  reversible maps removed, Pur-U must report "fails" and name (δ₀⊗δ₀, δ₀⊗δ₁). With pure composite states {d00, d11},
  it must report "vacuous". In scratch copies, forcing the status to 'holds' fails K-PURPOS and voids §6.10. So do the
  r1 rule (undecided counted as failing) and a vacuous branch returning 'holds'.
- **N2.** A state with a purification that is not a product of point masses makes Pur-U 'undecided', not 'fails'. It
  is not counted as failing, and the summary prints the status word. The fixture {d00, ½(d00 + d01)} must report
  'undecided'. No production line reaches this branch.
- **N5.** The A-3 statements that rested on review scratch work are computed after phase C as check lines that gate
  nothing: K8-SENS (the k/8 prior sensitivity block: 63 → 19, 195769 → 22719 and 93585 → 38749 states; pure sets
  unchanged), A3-CLC4-X1 (CL-C4 at x₀ = 1) and A3-COMP-U (the composite-level search with A idle, for K-SWAP and
  CL-C4). A4-GRID, A4-MARG and A4-PURE-E compute item 1 above.
- **N9.** The amendments digest line names A-3 and A-4, and the unused `c2_report` is removed.
- N6, N7, N8 and the convex-closure text (F5 of the review of `390e252f`) are not addressed.

The repaired run is `probe/p8s1.r2.run1.out` and `probe/p8s1.r2.run2.out`. `probe/CHANGES-r2.md` accounts for every
line in which it differs from `p8s1.r1.run1.out`.

***

**A-5. Correction of A-4's wording, made after the review of `78913467` (2026-10-21).** Recorded under PREREG §19's
discrepancy procedure ("a later discrepancy is recorded, not repaired"). Source: the independent review of `78913467`
(disposition ACCEPT WITH NOTES; findings 1–6), relayed by the coordinator. State of knowledge when A-5 was written: the
complete step-1 outputs of `390e252f`, `d924b5bb` and `78913467`, the three reviews and their scratch measurements. A-5
is not a preregistered choice. It changes no class, rule, criterion or decision clause of the preregistration, no code,
and no Pur-E or Pur-U outcome of any run. `PREREG.md`, A-1 to A-4 above, `probe/p8s1_r2.py` and its outputs are
unchanged; A-4 is not edited, and these entries correct it. The r2 output prints the digest of this file
(`37aff9f1…78f70` at `78913467`), which this entry changes; a byte-identical replay of `p8s1.r2.run1.out` (sha256
`b5ce288c…bd951`) is made from a checkout of `78913467`.

- **Scope of the composition lemma (finding 1).** A-4 item 2 states the lemma "at any budget m". It holds for m ≥ 1
  only. At m = 0 the weight set is empty (`weights(0)`, p8s1_r2.py:409–410), so ½ ∉ W and (H1) fails: the A-2
  composite ½(δ₀⊗δ₀ + δ₁⊗δ₁), preparable from the grid {0, 1} of the prior p = 1, is not a W-mixture, hence pure, and
  it is not a product. The claim's first sentence is false at m = 0. Its conclusion, that no mixed local state has a
  purification, holds there only vacuously, because no local state is mixed at m = 0. The hypotheses also use one weight
  set W for the local purity test (α = wα′ + (1 − w)α″) and for the composite purity test (ψ a W-mixture); the proof
  relies on this, and it is part of the lemma's statement. At m ≥ 1, ½ ∈ weights(m) and the proof stands as written.
- **Closure claim (finding 2).** A-4's "Closure under the declared operations is the accounting rule above" is narrowed
  to: closure under composing and discarding is the accounting rule above. The other operations §2.2 admits (the
  class's transformations and coupling steps, adjoining an uncoupled ancilla, classical coarse-graining of outcomes,
  and sequential composition with feed-forward, PREREG l. 242–243) were not shown to add no states beyond the union of
  the budget-m local sets. Feed-forward on a readout of a class with full hidden access, such as K-SWAP, could select
  with non-dyadic weights; that was not computed. The completion distinction and A-4's *Consequence* bullet are
  unaffected.
- **Per-prior identity (finding 3) [rec, review of `78913467`].** A-4's "The per-prior identity is also checked on the
  grids at m = 0, 1, 2, 3" is corrected. Check A4-MARG compares the union over priors of the per-prior half-sums with
  S_onebit(m+1) (p8s1_r2.py:2105–2111); it does not compare prior by prior, and the mutant that drops k = 2^m passes it
  by the p ↔ 1 − p symmetry. The per-prior form, ½(grid_m(p) + grid_m(p)) = grid_{m+1}(p), was confirmed by the
  reviewer's independent exact script, which does not import the probe: it holds for every prior in F₈ at m = 0..3.
  It is also A-4's [W] argument (K = k₀ + k₁ takes every value in {0..2^{m+1}}). The identity depends on A-2's
  per-prior grouping, in which both halves of copy A come from one prior. With mixed-prior pairs the marginals have
  197, 197, 393 and 787 states at m = 0..3, each a strict superset of S_onebit(m+1); 1/14 is an example of an added
  state. A4-MARG uses the same grouping, so it confirms the identity under A-2's reading and does not test the reading.
- **The [L] citation (finding 4).** A-4's "the standard fact that the extreme points of the minimal tensor product of two
  state spaces are the products of extreme points [L]" names no specific work. It stays unverified. The proof of the
  lemma is self-contained and does not depend on it.
- **Known cosmetic defects of the r2 output text (findings 5 and 6).** The reading label of the A-4 accounting line,
  "enlarged local set S_onebit(4), weights k/8, sensitivity" (p8s1_r2.py:2127), calls a line a sensitivity row that is
  not one: K8-SENS is the sensitivity block, and "weights k/8" refers to the budget-3 composite pure set the line is
  tested against. The A4-MARG message (p8s1_r2.py:2116–2118) always ends "the identity holds on the per-prior grids at
  m = 0..3", including on a FAIL; the per-m `equal` flags printed above it carry the measured result. A-4 item 1 states
  both contents correctly. No code is changed.
