# REVIEW-1049-r3: independent review of ASSESS-1049 r3 (linear vs affine microscopic dynamics)

**WIP / UNVERIFIED. Model-written (Claude Code reviewer subagent, 2026-11-09). This is a fresh,
independent review, not a human review.** It adopts, promotes and authorizes nothing. I made no git
or GitHub write and no manuscript edit. I wrote only this file and `review/rv3_link_affinity.py` with
its `.out`. Re-runs of the earlier probes were hashed from stdout and not written to disk.

- **Under review.** `ASSESS-1049.md` r3, sha256
  `75d6af06fcac7750dcdd7677abf42fbbbeb50caa0acbb8db619e42fb39b82fa9`. I re-hashed it at the start and
  it matched. `DISPOSITIONS-r3.md` is `600d42e7…`. `r2/ASSESS-1049.md` (`1628cc78…a893`) and
  `review/REVIEW-1049-r2.md` (`22da4c92…cab3`) match the hashes the header and dispositions state.
- **Source snapshot.** Every corpus read used `git show fd539e15:<path>`, after `git fetch origin main`.
  During this review `origin/main` moved to `cac5d264` (#1212, "correct SM ring degree bounds"). That
  change touches only SM:112's degree-bound sentence. No clause cited or proposed for correction in
  ASSESS changed. The working tree is clean (`git status` is empty). The proposals exist only in the
  file.
- **Owner direction.** #1169 c.6740778880 (check the counterexamples against every stated gauge
  assumption before weakening) and #1169 c.6741291498 (a false Substratum sentence gets "a narrowly
  scoped correction, not merely a qualification").
- **Reviewer probe.** `review/rv3_link_affinity.py`, sha256
  `a260d6ddc8d19286df2dd532715e7eb4a7880500a8a2fe54678878118269536f`. Its output
  `rv3_link_affinity.out` is `49e4b993a4db9c1c8d926244deccb2cbe5371ba3e87280172a2b72fa8b654a28`. ALL PASS,
  exit 0, about 21 s, run with `python3 -I`.
  - It uses exact arithmetic over ℤ/q only: generic local functions, one-step identities, and linear
    systems mod q (rank over GF(p); Smith normal form for composite q).
  - It iterates no dynamics, computes no observable, and instantiates no OI mechanism.
  - It imports nothing from `probes/` or `review/`. The P1 constructions are re-coded with different
    slot orders: (+x, +y, +z, −x, −y, −z) for d = 3 and (E, N, W, S) for d = 2.

## Verdict: REVISE

The r2 findings are fixed (§1). The mathematics of the theorem recovery is correct, and I proved it
independently (§2.1). The corpus search holds: every written form of A6's interface is a link sum with
additive links, and no joint-insertion form exists (§2.2). The withdrawals at Sub:100, :104, :220,
ch02:84 = FULL:718 and Structure:259 are justified, on the ground the writer gives in §7 item 7: P1
is not a counterexample under any written reading of A6 (§2.3).

There are two blockers. Both are textual, and neither needs new computation.

- **R3-B1. The headline overstates what the recovery delivers under the written interface.**
  - §0 item 2, §2.1 *Consequence*, the §2.4 item 2 bold conclusion, the "Recovered" cells of the
    per-site table, O-A and F-9 attribute the recovery to "A6's written interface". They say the claim
    "is not an overstatement".
  - E3 gives the sites' route (gauge ⇒ base-point form ⇒ affine) only in GA7-α, the non-additive link
    sum. GA7-α is unstated.
  - Under the written interface, the record's own G1 shows two things. Gauge is idle. And the
    "precisely to the extent" and "exactly when" clauses hold in one direction only.
- **R3-B2. A false clause is missed in Sub:272's second sentence.** The clause is "The one route that
  would make the affine restriction *unconditional* — deriving the unobservability of absolute
  amplitude from the observer architecture itself". Under the uniform reading that §2.3.1 adopts, it
  is false for d = 2, 3, as F2 and F3 are. V1 leaves it standing, and V1's own new conclusion no longer
  connects to it. This is the R2-B2 failure in the passage the owner direction targets.

***

## 1. The r2 findings

| r2 finding | Fixed? | Check |
|---|---|---|
| R2-B1 (one reading; Sub:270; F-8) | **yes** | §2.3.1 adopts reading (b) for both phrases. It is supported by Sub:270's attribution to "[SM §4.1]" (SM:240 is in §4.1; base-point form) and by Sub:274's statement of the lemma. Sub:270 has its own row. F-8 is restated as a failure of the inference. The r2 parenthetical is withdrawn. The precision point is N1 |
| R2-B2 (contradicted clauses left standing) | **yes for the four named passages** | Sub:272 first sentence: both clauses tabulated, and V1 deletes the comparative. Sub:274: F4 and F5, with V1 parts (i) and (ii). Sub:100 and ch02:84 = FULL:718: dispositioned in the per-site table, since the narrowings are withdrawn. **A further clause in Sub:272 is missed (R3-B2)** |
| R2-B3 (A6 reading-dependent; recovery; inventory; Q-NEXT) | **yes, with R3-B1** | GA7 is split six ways, and every site has an A6 column. §2.4 is the recovery note, with strongest results, verification, readings and gap. Inventory additions verified (§2.4 below). Q-NEXT leads with link-separability |
| N1 (F-7 prior record) | yes | §7 F-7 cites H-D D6, H-D-SR SR-1 and SR-3, and A5 C8 |
| N2 ("two further statements") | yes | Numbered list of five |
| N3 (Structure:301) | yes | "None: no overstatement"; O-F |
| N4 ("defined uniformly in q") | yes | §2.1 :255–259 and the GA8 row |
| N5 (clause-wise reading) | yes | Test text, Structure:219 row, §6 Q1(b) |
| N6 (`.tex` ranges) | yes for the listed sites | Verified at fd539e15: Substratum.tex :745–751, :783–784, :1407–1410, :1719–1720, :1729–1732, :1736–1739, :1768–1772, :1776–1778; FULL.tex :3312–3314. Residual ranges for sites r2 did not list: nit N8 |
| N7 (qualifier-only variant) | yes | Every correction has V1 (no new negative claim) and V2 (needs P1's proof on `main`) |
| N8 (inventory completeness) | yes | GA9; Theorem 24 (i), (iii), (iv); master principle; SM:585, :811; ch05:45 = FULL:1363, which I verified byte-identical. My own `git grep` for "amplitude-scale", "amplitude scale" and "global rescaling" over `papers/` and `book/` hits only sites the record lists, plus SM:1416, which states that the rounded realization "does not inherit … exact amplitude-scale invariance": no rule condition and no affine claim |

## 2. The theorem-recovery outcome

### 2.1 Independent proof: link sum plus uniform shift covariance forces affinity

**Paper proof.** Let F_i(x) = Σ_{j∈N(i)} m_ij(x_j) with arbitrary maps m_ij : A → A, where A is any
abelian group (A = ℤ/q, or (ℤ/q)^K). Suppose that for every c ∈ A the vector F(x + c𝟙) − F(x) is
independent of x.

1. Fix i and k ∈ N(i), with the sites in N(i) distinct (side ≥ 3, Sub:98). Fix all x_j for j ≠ k.
   The terms j ≠ k cancel, so D_k(x_k, c) := m_ik(x_k + c) − m_ik(x_k) is independent of x_k.
2. Put τ = m_ik − m_ik(0). Then τ(x + c) − τ(x) = τ(c) − τ(0) = τ(c), so τ is additive.
3. Hence m_ik = τ + m_ik(0) is affine, and F_i is affine.

For A = ℤ/q, an additive τ is x ↦ ax. This is E3, with no κ and λ = 1 only, at every d, every q and
any finite neighbourhood. Step 1 needs the neighbour slots to be independent variables. On a side-2
torus ±ê coincide, and their summed map is then affine, so the conclusion survives.

The converse is that every affine centre-free F_i = b + Σ a_j x_j is a link sum, with m_{i,1} =
a_1x + b and m_{i,j} = a_jx otherwise. So **among rules whose uniform-shift effect is state-independent,
link-separability ⟺ affinity.** That is gap G2, correctly stated.

**Exact generic check (rv3 V1–V4).** Condition (S) is *linear* in the unknown tables of the m_j. I
build the joint system from (S) for every x and c, with no slot-wise reduction. I then compare the
number of solutions with q^{2n}, the number of affine tuples, which all solve (S) (V1 generator check).

- **V1.** The counts are equal for:
  - n = 1 at q = 2–9 (composites by Smith normal form);
  - n = 2 at q = 2–9, 11 and 13;
  - n = 3 at q = 2–5;
  - n = 4 (the d = 2 neighbour count) at q = 2, 3, 5, 7 and 11;
  - n = 6 (d = 3) at q = 2, 3, 5 and 7. At q = 7 the system has 823 543 rows, and the solutions
    number 7^{12} = 13 841 287 201.
- **V3: separability is load-bearing.** General, non-separable 2-slot F with (S) has 81 solutions,
  against 27 affine, at q = 3, and 15 625 against 125 at q = 5.
- **V4: mutation control.** Keeping only the x = 0 rows gives 9 765 625 ≠ 625 at q = 5. The checker
  detects a vacuous system.
- **V2: internal index K = 2** (A = (ℤ/q)², maps A → A).
  - With shifts by every c ∈ A, the solutions are exactly the affine ones at q = 2 (n = 2, 3) and
    q = 3 (n = 2, 3).
  - With diagonal shifts c(1, 1) only, non-affine solutions exist at q = 3. The count is
    282 429 536 481 against 387 420 489 for n = 3.
  - At q = 2 diagonal shifts happen to suffice, because x₁x₂ is the only non-affine monomial. This is
    printed as a NOTE.
  - Scope consequence: nit N3.

**Verdict.** E3, its corollary (site-wise base-point form) and its converse are correct as stated
for K = 1.

### 2.2 Does every written form of A6's interface use the link sum?

I searched the whole corpus at fd539e15 (§A.19).
- **Places the link variable M(n, ê_j) occurs:** `papers/`, `book/`, `verification/` records, the Lean
  tree and `edge_rigidity_probe.py`.
- **Places an update is displayed:** SM:106, :112, :224–228, :312, :314, :627, :1602; Sub:98;
  ch05:30, :98; ch06:56.
- **The search terms:** "joint insertion", "non-additive link", "nonlinear link", "non-additive
  coupling", "nonlinear coupling", "link sum", "link-separab", "f(M".

What I found:
- **Kernel.** `BackgroundIndependence.linkF N M c i = ∑ j ∈ N i, M i j (c j)` with `M i j : V →+ V`.
  `A6Instantiation.linkRule` and `linkSubstratum` use the same typing at `Fin 6 → ZMod q` and
  `Fin 6 → ℂ`. `linkSubstratum_A5` proves F additive, "each `M i j` is additive and the neighbour
  sum is finite". `GradientLinkFlatness` and `LinkDecomposition` define no A6 interface.
- **Prose.**
  - SM:312 gives the general second-order linear update, C φ + Σ_j M^{(j)}[…] + D φ(t−1). SM:314 and
    ch05:98 give the isotropic matrix form.
  - SM:116, Sub:102 and ch02:86 = FULL:720 give the transformation law of the matrix link.
  - SM:118 says "The wave equation is carried to itself".
  - SM:523 says "The link is the carrier".
- **No joint-insertion form f(M_{i1}x_1, …) appears anywhere.** The one "nonlinear coupling" hit
  (`native-y-continuation…/PLAN.md:79`) is unrelated to A6. G_SM (SM:112) is the state-dependent graph,
  which Sub:102 separates from A6.

**Confirmed.** Every written form is a link sum, and every written link is additive or a matrix. One
precision point is nit N9: SM:312–314 are stated "on the observer-level branch … not the ℤ/qℤ
alphabet", so the substratum-level written instance is the kernel's `linkF`.

### 2.3 Are the withdrawals justified?

**Yes, on the ground of §7 item 7.** The owner's test narrows a site only where P1 satisfies every
assumption the site states.
- Sub:100, Sub:104, Sub:220 (Remark, Hypothesis dependencies, verified at Sub:214–221) and
  ch02:84 = FULL:718 (in the "six properties" list, ch02:74; A6 at ch02:86, byte-identical to
  FULL:720) all state A6.
- Under the only written interface, P1 lacks link-valued coupling data, which Sub:102 asserts ("the
  coupling is link-valued data on which the transformations act").
- Sub:220's "non-affine wave equations" also presuppose the link form.
- Structure:259 names A1–A6 in its paragraph. Its claim also cites Main (vii), which carries the
  base-point qualifier, so it is not an overstatement on either ground.
- Only GA7-β, which no source writes, would admit P1. That is correctly put to the owner (§6 Q2).

**But "withdrawn because P1 is excluded" is not "recovered".** That difference is R3-B1.

### 2.4 Remaining gaps G1 and G2

- **G1 is correct.** Typed additive, the interface makes F additive (`linkSubstratum_A5`), so the rule
  is linear by type and b = 0 is built in. The gauge principle is idle.
  - The tension with Sub:100 ("the further restriction to linear is imposed") and with Sub:102
    ("imposes no further condition on the rule") is real and well put.
  - So is the observation that "excluded precisely to the extent" (Sub:100; ch02:84 = FULL:718) and
    "exactly when … dropped" (Sub:220) then hold in one direction only.
  - One refinement (nit N4): even under GA7-α those clauses hold in both directions only for q ≥ 3. At
    q = 2 every map ℤ/2 → ℤ/2 is affine (rv3 V1, n = 1: 4 solutions = all maps), so every link sum is
    affine. Σ_j x_j² = Σ_j x_j there.
- **G2 is correct.** See the converse in §2.1. "Relocates the premise rather than deriving it, unless
  it has independent warrant" is the right reading under §A.29.

### R3-B1 (blocker): the recovery's basis is misattributed in the headline

The record makes two different claims, and in places it fuses them:

- **(i) Withdrawal.** P1 is not a counterexample at the A1–A6 sites under the written interface, so
  the P1-based narrowings are withdrawn. Shown.
- **(ii) Recovery of the sites' route.** "Amplitude-scale gauge restricts the update to an affine one
  via the linearity-equivalence lemma." E3 shows this only in GA7-α, with non-additive link maps,
  which the corpus does not state.
  - Under the written, additive interface, the conclusion holds by typing and gauge does no work
    (G1).
  - Under that interface, Sub:100's and ch02:84 = FULL:718's "excluded precisely (exactly) to the
    extent … assumed" and Sub:220's "exactly when … dropped" are false in one direction (G1's own
    finding).

Where the record fuses (i) and (ii):
- §0 item 2: "excluded by A6's written interface … and the claim is recovered: uniform gauge plus the
  link sum gives the base-point form". The link sum meant here is GA7-α.
- §2.1 *Consequence* (:266–268): "Among link-sum rules, the form in which the corpus writes A6's
  interface, uniform shift gauge does entail it". The corpus writes it with additive maps, and there
  E3 is not needed.
- §2.4 item 2, in bold: "recoverable and is not an overstatement". This contradicts G1 under the
  written interface.
- Per-site table: Sub:100 says "The claim is recovered (§2.4)", and Sub:104 says "Its route 'via the
  linearity-equivalence lemma' is the recovered one".
- O-A (:789–790): "the 'partly derived' claim is recovered under A6's written interface". Under that
  interface the "partly derived" attribution to gauge is exactly what G1 says is idle.
- F-9: "POSITIVE … under A6's written interface". E3 is positive under GA7-α. Under the written
  interface the relevant results are E2 and the kernel's typing.

§7 item 7 and G1 already say this correctly, so the headline contradicts the record's own body. That
is a claim/evidence-boundary defect (available or conditional → derived) in the outcome the owner
reads first.

**Fix.** At each site listed, separate (i) from (ii). Suggested wording for the §2.4 item 2 bold
sentence:

> "P1 is not a counterexample at Sub:100, :104, :220, ch02:84 = FULL:718 and Structure:259 under any
> written reading of A6, so r2's narrowings there are withdrawn. The sites' attribution of the affine
> part to amplitude-scale gauge 'via the linearity-equivalence lemma' holds in the non-additive
> link-sum class (GA7-α, not stated in the corpus). Under the interface as written, with additive
> links, the conclusion holds by typing, the gauge principle is idle, and the 'precisely to the
> extent' and 'exactly when' clauses hold in one direction only (G1). Which applies is §6 Q2."

Make the matching one-line changes at §0 item 2, :266–268, the per-site cells, O-A and F-9 ("POSITIVE
under GA7-α; under the written interface, E2").

## 3. Sub:270–274

### 3.1 The base-point reading at Sub:270

**It is correct.**
- Sub:270 attaches "amplitude-independent dispersion ⟺ affine dynamics" to "the linearity
  equivalence of [SM §4.1]".
- SM §4.1 begins at SM:220, and SM:240 states the lemma in base-point form.
- Sub:274 states it the same way.
- The "third, physical reading" split (§2.3.1) is right. Superposition about c fails exactly when a
  first difference depends on the base point, and the scale part is unit homogeneity. I checked P1's
  side of this exhaustively at d = 2, q = 7 (rv3 V5):
  - every single-slot response is invariant under uniform shifts;
  - the response depends on the background (witness at x = (0, 0, 0, 1));
  - f(λx + c𝟙) = λf(x) + 2c for all x, every unit λ and every c (also at d = 3, q = 5).

Sub:270 needs no correction under (b).

### 3.2 F-8: "the inference fails under either reading"

**Correct in substance. One precision point (N1).**
- Under (b) the parenthetical is true, the conclusion is false for d = 2, 3, and the inference is
  invalid. That is verified.
- Under (a) the parenthetical premise is false for P1. The inference from it would be valid, but the
  argument is unsound.
- The §2.3.1 truth-table row and F-8 say "fails" for both. Say "the argument fails under either
  reading: under (b) the inference is invalid, under (a) its premise is false."

### 3.3 The five false clauses F1–F5

| Clause | Review |
|---|---|
| F1 "strictly weaker than the output" | **False, correct.** It is false under (R-uni) at odd q: affine rules with b ≠ 0 fail λ = −1 (rv3 V6; r3 K3), and P1 satisfies (R-uni). Under (R-site) it is false by the lemma. Precision point (N2): "incomparable" holds at odd q. At q = 2 every isotropic centre-free affine rule a·Σ + b satisfies the κ = 2 uniform form (rv3 V6, exhaustive at d = 3). Every affine rule satisfies the κ-general form at q = 2, and P1's q = 2 construction satisfies it while not being affine. There the comparative is *true*, and only F2 fails. The manuscript clause is general in q, so it is false; F1's "the two are incomparable" should carry "at odd q" |
| F2 "a coherent object the principle *excludes*" | **False for P1's class under (R-uni) and (R-rel), correct.** The pair-is-false-under-every-reading table is right |
| F3 "so … presupposes an affine rule" | **False under (R-uni) (d = 2, 3) and (R-rel), correct** |
| F4 "the principled object that delivers the affine restriction" | **False for the uniform group, correct.** GA9's paper argument is correct: σ(w − y) + σ(y) = σ(w) + σ(0) with f onto gives τ additive. "Only the shifts enter that form" is correct |
| F5 "yields an affine rule as a certified theorem" | **False in the uniform reading, true as the lemma, correct** |
| **missed: F6** "The one route that would make the affine restriction *unconditional* — deriving the unobservability of absolute amplitude from the observer architecture itself" | **False under the reading §2.3.1 adopts (R3-B2)** |

### R3-B2 (blocker): the missed clause in Sub:272's second sentence

The clause says that deriving "absolute amplitude is unobservable" would make the affine restriction
unconditional. That requires unobservability ⇒ affinity.
- In the reading §2.3.1 states it uses ("the principle as Sub:270 and SM:96 state it, with uniform
  maps"), P1 refutes it for d = 2, 3, exactly as it refutes F2's "excludes" and F3's conclusion.
- It is true only in the (R-site) reading, where the principle is affinity restated, or in GA7-α,
  which Sub:272 does not state.
- After V1, the sentence would read: the route "that would make the affine restriction unconditional"
  is circular because unobservability "presupposes a rule for which [uniform maps] are exact
  symmetries".
  - The new conclusion no longer bears on the affine restriction.
  - The surviving clause asserts a false entailment in the same sentence.

This is the R2-B2 class of defect in the passage the owner direction (c.6741291498) targets.

**Fix.** Add F6, scoped like F1–F5, with a V1 and a V2. Two options for V1 are:
- **(α)** "The one route that would make the principle itself *unconditional* — …". This is the
  smallest change, and it is consistent with V1's new conclusion.
- **(β)** "The one route that would make the affine restriction *unconditional* — deriving the
  unobservability of absolute amplitude, in the base-point form, from the observer architecture
  itself — …". This is consistent with V1 of the first sentence, but it then needs the second
  sentence's conclusion to stay in base-point form.

Choose one, and say in §2.3.1 which reading each sentence of the corrected paragraph uses. V1 of the
first sentence uses the base-point form, and V1 of the second uses uniform symmetries. Mixing them is
not wrong, but the paragraph then has to say so.

### 3.4 V1 and V2; does V1 count as "a narrowly scoped correction, not merely a qualification"?

- **Sub:272, second sentence, V1: yes.** It replaces the false premise and the false conclusion. It
  does not append a caveat. Once F6 is fixed (R3-B2), it is a correction. One point (N5) concerns the
  record's claim that "the new premise restates 'not an exact symmetry', so the inference is valid".
  - That holds with "unobservable" read as dynamical indistinguishability.
  - Under the observer-resolution sense the sentence sets up ("what the embedded observer can
    resolve through the trace-out"), the inference also needs the open step "distinguished by the
    dynamics ⇒ resolvable", which the Status note flags.
  - Say so rather than calling the inference valid without qualification.
- **Sub:272, first sentence, V1: a correction in part.** Deleting the false comparative is a
  correction. The added qualifier makes "excludes" true only because, in base-point form, the
  principle *is* affinity (the record's own (R-site) point). The surviving opening, "Stated
  operationally it is *not* viciously circular", then rests on that reason. The base-point form is not
  the operational statement. The result is true but hollow. It should be raised with the owner in
  §6 Q1 (N6).
- **Sub:274 V1: borderline.** The qualifier sits inside the clause and changes its subject, so it is
  not assert-then-qualify (§A.30), and the record's argument for that is sound.
  - But it rescues "the group … delivers" by restricting the group to a form in which only its shifts
    act and which is equivalent to the conclusion.
  - The same paragraph's "more primitive and better-motivated assumption" and "relocates the
    irreducible assumption … to a more primitive and more defensible place" then attach to an
    assumption that, in the form now stated, is equivalent to affinity.
  - The owner asked for "not merely a qualification", and Q1(d) already raises the question.
  - I recommend that the record also offer a subject-changing V1′ (N6). One example: "The principled
    condition that delivers the affine restriction without overshooting is that a shift at one site
    changes the update by an amount independent of the state (the base-point form of the
    linearity-equivalence lemma); the **additive-automorphism** group $x \mapsto \lambda x + c$ is a
    proper subgroup of all permutations that preserves the alphabet's '+'". V1′ states what is true
    instead of narrowing what is false.
- **V2 everywhere.** These are correctly marked as adding a new negative claim whose proof is off
  `main` (§A.42 item 2; §A.46 item 1). That is consistent with r2 N7.
- **Register (§A.32–§A.33)** of all proposed paper text is neutral, with no history voice, no caps and
  no reader instruction.

### 3.5 Proposals only in the file

Confirmed. The working tree is clean, and the quoted source text matches fd539e15.

## 4. The writer's partial refusals

1. **No "link-sum form" wording proposed for paper prose: agreed.** Such wording would assert in the
   manuscript a premise the corpus does not state for non-additive maps (GA7-α). That is a new
   assumption under §A.29, outside this unit's authorization ("Not authorized: … new physical
   assumptions"). Putting it to the owner as §6 Q2 and O-G preserves the option r2 asked for without
   writing it into prose.
2. **"Distinguishes, in its evolution, states that differ only in absolute amplitude" in place of
   "makes the absolute amplitude dynamically observable": agreed as wording.** The two say the same
   dynamical thing, and the literal form avoids implying observer resolution. The cost is that the
   bridge to the paragraph's observer-resolution framing is now explicit and open. The record should
   say that, rather than call the inference valid (N5).

## 5. Full re-read, re-runs, scope

- **Re-runs.** All earlier scripts were re-run with `python3 -I` from `/tmp`, with stdout hashed: `p1`,
  `p2`, `p3`, `r2_gauge_inventory`, `r3_link_recovery`, `rv_p1`, `rv_p2` and `rv2_gauge_audit`. All
  exited 0, and all eight outputs match the stored `.out` hashes. All script hashes match §8.
  - `r3_link_recovery.py` imports only `itertools`.
  - Its K2 checks the joint condition on every tuple, so it is not circular. It does not separately
    check that every affine tuple is a solution, but the printed counts equal (q²)^slots.
- **Inventory spot-checks.**
  - GA1–GA9 sources verified verbatim at fd539e15: SM:94, :96, :240; Sub:98, :102, :163, :270–274;
    ch05:45; Structure:217, :219, :259, :301.
  - `A6Inv`, `A6Cov`, `A6Glob` and the "adopts no reading" text are verbatim from
    `BackgroundIndependence.lean`:1–135.
- **Downstream (§3), §2.2, O-B to O-F, Q-NEXT.** No change from r2 beyond the link-separability lead
  of Q-NEXT, which is correctly framed as warrant, not sufficiency.
- **Scope.** F-1 is scoped to d = 2, 3 and to non-link-sum, centre-free, nearest-neighbour rules. No
  universal negative is stated. [H] material is used as hypotheses only (§A.46 item 7).
- **Labels.** The labels are consistent. E3 is [A] plus [X]. The reading assessment is [P] with
  quotations.

## 6. Nits

- **N1.** F-8 and the §2.3.1 inference row should say: under (b) the inference is invalid; under (a)
  the premise is false, so the argument is unsound.
- **N2.** F1: "incomparable" at odd q. At q = 2, affinity implies the κ-general uniform form (and the
  κ = 2 form for isotropic rules), so there the comparative holds and only F2 fails (rv3 V6).
- **N3.** E3 and G4 scope: E3 is proved for K = 1. For the manuscripts' carrier (kernel
  `Fin 6 → ZMod q`) the same proof needs shifts by every c ∈ (ℤ/q)^K. Diagonal shifts do not suffice
  at q = 3 (rv3 V2). Add this to G4.
- **N4.** Sub:100 row and G1: "holds in both directions under GA7-α" needs q ≥ 3. At q = 2 every link
  sum is affine.
- **N5.** Sub:272 second-sentence V1: qualify "so the inference is valid". It is valid with
  "unobservable" read dynamically. The observer-resolution step is open (Status note).
- **N6.** Q1(d): raise the hollow-support point for Sub:272's opening ("not viciously circular") and
  for Sub:274's "more primitive and better-motivated" and "more primitive and more defensible place"
  under V1. Offer a subject-changing V1′ at Sub:274 (§3.4).
- **N7.** §2.4 Assessment: state why the vacuous-conditional reading of A6 ("if a rule has link data,
  it is covariant", which P1 would satisfy vacuously) is not available. Sub:102 asserts "the coupling
  *is* link-valued data".
- **N8.** `.tex` ranges for sites r2 did not list:
  - Sub:100's first clause, used by §2.4 item 4, starts at Substratum.tex:744;
  - Structure:219 is :980–982;
  - Structure:259 is :1144–1145;
  - Structure:301's claim is :1269–1271 (:1273 is the next sentence).
- **N9.** §2.4 item 2: SM:312–314 are stated on the observer-level branch, not the ℤ/q substratum. Cite
  the kernel's `linkF` and `linkSubstratum` at `Fin 6 → ZMod q` as the substratum-level written
  instance, and SM:116 and :312–314 as the prose form.

## 7. Summary

| ID | Kind | One line |
|---|---|---|
| R3-B1 | blocker | §0 item 2, §2.1 :266–268, §2.4 item 2 (bold), per-site "Recovered", O-A and F-9 attribute the recovery to A6's *written* interface and call the sites "not an overstatement". E3 delivers the sites' gauge route only under unstated GA7-α. Under the written interface gauge is idle and two clauses hold one way (G1). Separate withdrawal (shown) from recovery (conditional on GA7-α) |
| R3-B2 | blocker | Sub:272 second sentence: "The one route that would make the affine restriction *unconditional* — deriving the unobservability …" is false under the adopted uniform reading (d = 2, 3) and survives V1 disconnected from V1's new conclusion. Add F6 with V1 and V2 |
| N1 | nit | F-8 under (a): premise false (unsound), not an invalid inference |
| N2 | nit | F1 "incomparable" at odd q; at q = 2 the comparative holds |
| N3 | nit | E3 is K = 1; at K > 1 it needs shifts by every c ∈ V (diagonal fails at q = 3, rv3 V2) |
| N4 | nit | "Both directions under GA7-α" needs q ≥ 3 |
| N5 | nit | Sub:272 V1 "inference is valid" holds with dynamical "unobservable"; the observer-resolution step is open |
| N6 | nit | Q1(d): hollow support after V1 at Sub:272's opening and Sub:274's "more primitive"; offer a subject-changing V1′ |
| N7 | nit | Say why A6's vacuous-conditional reading is excluded (Sub:102 "the coupling *is* link-valued data") |
| N8 | nit | `.tex` ranges: Substratum.tex:744; Structure.tex:980–982, :1144–1145, :1269–1271 |
| N9 | nit | SM:312–314 are observer-level; cite the kernel `linkF` as the substratum-level instance |

**What re-review needs.** R3-B1 and R3-B2 applied, and a diff check of the changed passages. No new
computation is required: `rv3_link_affinity.py` covers N2–N4.
