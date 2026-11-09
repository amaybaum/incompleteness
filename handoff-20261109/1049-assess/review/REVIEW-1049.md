# REVIEW-1049 — independent review of ASSESS-1049 (linear vs affine microscopic dynamics)

**WIP / UNVERIFIED. Model-written (Claude Code reviewer subagent, 2026-11-09).** Independent
review, not a human review. It adopts nothing, promotes nothing and authorizes nothing. No git or
GitHub write and no manuscript edit was made.

- **Under review.** `ASSESS-1049.md`, sha256
  `9e60b0ae881bd6e1dd1bd307fb0baaecccba5b3ef5207f61178960f34ab0e040` (re-hashed at review time),
  with `probes/p1–p3` (hashes as stated in its §8; all six re-hashed and matching).
- **Source snapshot.** `origin/main` = `fd539e150759a6ea51ab279aeeac80fc06050ade` (fetched
  2026-11-09; unchanged during the review). All corpus reads by `git show fd539e15:<path>`.
- **Authorization checked.** #1049 c.6740117832 (amaybaum, 2026-11-09T12:31:15Z) quotes the #1169
  option text verbatim: "One paper-only unit each, re-assessing its open question against today's
  #1210/#1211 findings … each with a fresh review. Exact generic checks only." The owner's Q1/Q2
  decisions quoted by the writer match #1049 c.6624263637 (2026-11-04T06:28:45Z) verbatim.
- **Reviewer probes** (`review/`; exact integer arithmetic; import nothing from `probes/`):
  - `rv_p1.py` sha256 `2d2753f5359a7f70fe91ad5e5c0d5a4b0723e189baf2a9db9a0927e4067b551a`;
    output `rv_p1.out` `907627f253e29e4923d1a3fe60a849955b861dbf54425a7bba804e011a95c98f`; ALL PASS.
  - `rv_p2.py` sha256 `a72f1c8787550c846d748199fcce4aa814b6550e0246e7e548933969c3a53034`;
    output `rv_p2.out` `9d3b65ef592c722f88554098991d4ff30b803919e73d8e1c096c5b67b13181a5`; ALL PASS.
  - One expectation in `rv_p1.py` was revised after its first run, and the revision is recorded
    in the code: I had predicted that composite odd q admits non-linear d = 1 solutions *with*
    reflection. It does not (see C2 below). The failing first-run line was my prediction, not a
    property of the writer's claim, and no other check changed.

## Verdict: REVISE

The central mathematical finding (claim 1) is correct, and P1 tests a faithful reading of the
corpus's principle. The d = 1, quarter-phase and b ≠ 0 extensions are correct as scoped, apart
from small wording points. Three blockers remain. Each is textual and can be fixed without new
computation:

- **B1.** The §A.19 / §A.25 search is incomplete. Two overstating sites are missed, and a corpus
  argument for excluding non-affine rules is left without a disposition.
- **B2.** Q-NEXT's "Equivalently" holds in one direction only (§A.34). The "P1 already reduces it
  to one function class" smallness argument rests on that converse.
- **B3.** "b = 0 does work only at four sites" is a universal negative stated over an inventory
  that omits A5 rows D7, D12, D13 and D15.

***

## 1. Claim 1 — affinity is not derived from the gauge principle

### 1.1 Independent verification of P1's functions (`rv_p1.py`, parts A–C)

I re-coded each function with my own conventions:
- a different neighbour-slot order;
- the point groups built by closure from generators: O_h from two 90° rotations and the
  inversion (48 elements), D4 from a 90° rotation and a reflection (8);
- the modular inverse in place of P^{q−2};
- an affinity test by first differences along each coordinate, which differs from P1's
  basis-decomposition test.

Results, all exhaustive over (ℤ/q)^{2d}:

| Function | Covariance f(λv + c) = λf(v) + 2c, all units λ, all c | Point-group invariant | Affine |
|---|---|---|---|
| d=3, q=5: (1/3)Σ + C·P⁻¹ | yes | O_h yes | **no** |
| d=3, q=7: same | yes | yes | **no** |
| d=3, q=2: Σ + [six neighbours equal] | yes (λ = 1 only; 2c = 0) | yes | **no** |
| d=2, q=7: (1/2)Σ + y₃χ(y₁² − y₂²) | yes | D4 yes | **no** |
| control (1/3)Σ, q=5,7 | yes | yes | yes |
| countercontrol (1/3)Σ + 1 | **fails** | yes | yes |

**Global level (part C).** On a periodic 4×4×4 lattice at q = 5, over 40 seeded random states,
the full phase-space map satisfies all four of the following exactly:
- the explicit inverse (u, v) = (F(v) − w, v);
- commutation with the three unit translations;
- the uniform symmetry Φ(λu + c, λv + c) = λΦ(u, v) + c;
- centre-freeness (changing x_i(t) leaves F_i unchanged).

The local exhaustive checks already imply these. Part C is a consistency check of the lattice
assembly.

**Paper check.**
- **Shift invariance.** a′, b′, c′ are shift-invariant, since 2·2c − 2c − 2c = 0.
- **Homogeneity.** C is cubic, and P⁻¹ (with 0 at P = 0) is homogeneous of degree −2 on units, so
  C·P⁻¹ is homogeneous of degree 1.
- **Isotropy.** The 48 elements permute (p_x, p_y, p_z), and C and P are symmetric.
- **d = 2.** The 90° rotation sends y₃ ↦ −y₃ and y₁² − y₂² ↦ −(y₁² − y₂²). χ(−1) = −1 because
  q ≡ 3 (mod 4).

All four points confirmed by hand.

**Strengthening the writer can adopt.** Non-affinity of the d = 3 family at *every* prime q ≥ 5,
not only at the checked q = 5 and 7, has a one-line proof. Let G = C·P⁻¹ on the plane
a′ + b′ + c′ = 0. Then:
- G(1, 1, −2) = −2/6 = −1/3;
- G(1, −1, 0) = 0, since C = 0;
- G(2, 0, −2) = 0, since C = 0.

So G is not additive, because −1/3 ≠ 0 when q ∤ 3. The map x ↦ (a′, b′, c′) is linear and onto
that plane (rank 2, with the diagonal as kernel), so f is not affine. The writer's "prime q ∤ 6"
statement thus has a complete paper proof, and P1 is a control on it.

### 1.2 Is "the uniform gauge principle" as the corpus states it what P1 tests? — Yes; not a blocker

**What the corpus says.**
- **SM:96.** The "transformations that preserve the emergent observables are the alphabet's
  additive-group automorphisms — rescalings x ↦ λx … and shifts x ↦ x + c"; "Operationally the
  absolute scale of the field value is unobservable".
- **Sub:163.** "a global rescaling of the field value φ".
- **Sub:270.** "the rescalings φ ↦ λφ … and shifts φ ↦ φ + c … leave every observable unchanged".
- **Sub:274.** "the more primitive … assumption 'the alphabet's additive automorphisms are gauge'
  yields an affine rule as a certified theorem".

**Readings of the principle.** It can be formalized in four ways. The writer covers the first
three; the fourth is the reviewer's addition.
- **(R-rel), relabelling.** This is the owner's Q2 reading. It constrains no rule.
- **(R-uni), uniform exact symmetry.** This is what P1 tests. "Global rescaling" and "the absolute
  scale" (SM:96, Sub:163) read most naturally this way.
- **(R-site), the base-point form.** This is the form SM:240 and Main:726 (vii) name. It is
  equivalent to affinity by the lemma.
- **Site-dependent automorphisms as exact symmetries.** The corpus's "site-wise relabellings"
  (Sub:270) could be read this way. The reading is untenable: it requires F_i(x + c e_k) = F_i(x)
  for k ≠ i, which excludes the linear wave rule itself. `rv_p1.py` part D confirms this. Read as
  relabellings, "site-wise" relabellings again constrain nothing. Sub:270's "site-wise" wording
  therefore does not supply (R-site).

**Conclusion.** The only reading that yields affinity is the one equivalent to it. P1 is a
counterexample to the reading the overstating sites need. It is not a counterexample to a
misread principle.

**κ ≡ 2 is not doing the work (part B).** As the writer formulates it, (R-uni) contains a
static shift symmetry, and that forces κ = 2dα ≡ 2. So (R-uni) is *not implied* by affinity:
affine rules with κ ≢ 2, such as α = 1 in d = 3, fail it. One might object that P1 refutes an
over-strong principle. Part B answers the objection: the α = 1 variant Σ + C·P⁻¹ satisfies the
κ-general covariance f(λv + c) = λf(v) + 6c, is O_h-invariant, and is non-affine. It also fails
the κ = 2 form, as it must. The counterexample therefore survives the weaker,
κ-independent uniform reading. *Nit N1:* state this in §2.1 so the reader does not take (R-uni)
for an over-strong reading.

**Conclusion of claim 1.** Confirmed for d ∈ {2, 3}.
- The overstatement finding against Sub:100, :104, :220, :272 and :274, ch02:84 and FULL:718 is
  correct. All seven were read at fd539e15.
- Main:726 (vii) and SM:240 do carry the base-point form. Main (vii) reads it as the *form in
  which* the gauge principle is taken, so the writer's "state the scope accurately" is fair.

### 1.3 Claim-scope points

- **Nit N2.** The summary, §7 F-1 and the brief say "d ≥ 2", but only d = 2 (q = 7) and d = 3
  (q = 2 and prime q ≥ 5) are exhibited. Say "d = 2, 3", or give a construction for d ≥ 4. The
  physically relevant d is 3, so nothing turns on this.
- **Nit N3.** "Under the owner's relabelling reading [O, Q2] the gauge constrains no rule"
  extends Q2. Q2 was decided for *amplitude shifts* in the b = 0 question. Label its application
  to rescalings and to the affine question as the writer's extension of [O], not as [O] itself.

## 2. The d = 1 claim — confirmed, with sharper scope

**Paper check.** With f = s + G(y):
- covariance gives G(λy) = λG(y) on units;
- at prime q this makes G linear, G(y) = gy;
- reflection makes G even, so G = 0.
The writer's proof is correct for odd prime q.

**Exact check (`rv_p1.py` part E).** Constraint propagation over all functions of the two
neighbour values gives:

| q | Without reflection | With reflection |
|---|---|---|
| 3, 5, 7 (prime) | exactly q solutions, all linear: (1−g)a + (1+g)b | unique solution, f = a + b |
| 9, 15 (composite odd) | 27 and 225 solutions, not all linear | unique solution, f = a + b |

**Consequences.**
- **(a) With reflection, the result holds at every odd q, not only prime q.** The unit λ = −1
  makes G odd, and reflection makes it even, so 2G = 0 and G = 0. The writer's intermediate step
  "G is linear" is false at composite q, but the conclusion still holds there. *Nit N4:* either
  scope the claim to odd q with this argument, or keep "odd prime" and note the step.
- **(b) Without reflection, (R-uni) plus centre-freeness forces linearity (b = 0) at odd prime q
  only.**
- **(c) The d = 1 result depends on there being exactly two read variables, so a single
  difference variable.** A centre read, or a range-2 read in d = 1, reopens non-affine solutions.
  *Nit N5:* the short forms "in d = 1 the principle forces linearity" (§0 / the brief, F-1) must
  carry centre-freeness, nearest-neighbour range and odd q. At q = 2, (R-uni) is vacuous in
  d = 1: for example the complement rule 1 + a + b and the constants are allowed. §2.1 has the
  hypotheses; the summaries drop them.

## 3. Quarter-phase claims, against QP DESIGN, PROOF-RECOVERY and MECH-2 at fd539e15

**Row 3a, G1 for non-affine rules.** Confirmed.
- QP states G1 for linear combinations (QP node 1), and its proof is an induction on the update.
  With "linear combination of type-τ variables" replaced by "function of type-τ variables", the
  same induction goes through for any centre-free rule that reads only opposite-colour sites. It
  uses neither additivity nor offsets.
- QP's own "Lemma G1 uses only the finite update" is about the level, not about linearity. The
  ELABORATING classification relative to QP is right.
- *Nit N6:* §3.2's "By P3 it fails only when a rule reads its own site or a same-colour site" is a
  universal statement. It follows from the [A] induction (contrapositive). P3 only exhibits the
  two countercontrols. Attribute it to [A].

**Row 3b, G2 for affine rules.** Confirmed.
- Step 3 of G2 (QP node 3) needs only that the two runs differ by a map linear in the state.
- With common offsets, Φ^t z − Φ^t z′ = L^t(z − z′) (B0.1; re-derived). G2's hypotheses already
  allow "supplied constant translations".
- *Nit N7:* "node 9 records that fixed offsets cancel" cites a different statement. Node 9 and
  PROOF-RECOVERY §5 say that the available t₋ₐ cancels a fixed coupling offset and recovers L, a
  separate-availability fact, not G2's run difference. Cite it as context only.
- *Nit N8:* "Not examined. Step 3 fails in general" asserts a failure without a witness. Write
  "step 3's identity is not available".

**Row 3c, Q(i).** Confirmed.
- Q(u′, v′) = Σ k_ij u_i u_j − Q + b·u = Q + b·u (mod 2) by hand.
- `rv_p2.py` checks it exhaustively for every symmetric zero-diagonal K, every b and every state
  at n = 3 and 4 (4,096 and 262,144 cases).
- The countercontrols break conservation: a uniform b = 1, and a centre term at b = 0.

**Row 3d, Q(iii) for b ≠ 0.** Confirmed on paper.
- QP's proof of (iii) conditions each record branch to "a fixed sequence of symplectic
  center-free steps and constant translations", and "Translations change values, not which
  functionals are determined" (QP node 6). An affine native step is a translation composed with
  a symplectic linear step, so the proof applies verbatim.
- This row has no probe support, and needs none. The brief's "(P2)" for Q(iii) is inaccurate:
  ASSESS row 3d is labelled [P]; [A], and P2 does not test Q(iii).
- The "without affinity" cell cites M-INACC's G_σ, which reads i ± 2. Lemma Q holds for linear
  symmetric centre-free rules on *any* graph, so attributing G_σ's failure to non-affinity is
  consistent.

**MECH-2:532.** The text reads "That exclusion does not carry over to `G_SM`, whose nonlinearity
breaks the grading: P★'s record-1 branch … reaches a carrier law with `z + x` determined (support
`{01, 10}`)".
- G_SM's closed form, f_i = u_{i−1} ⊕ (u_{i+1} ∨ u_{i+2}) (MECH-2:40), reads the same-colour
  site i+2.
- P★'s prior is a product: independent uniform unknowns plus known constants (MECH-2 node 6). The
  writer's factorized-prior scope therefore covers P★.
- The product-support argument is correct. Under the functional split, the conditioned support
  is S_E × S_O. A mixed sum z + x that is constant on a product set forces z and x to be constant
  separately. So {01, 10} needs a sector-mixing slot.
- A linear rule with an i+2 read can also determine a mixed functional. Non-affinity is therefore
  neither necessary nor, in an NN centre-free read pattern, sufficient for this observation.
- The finding stands. *Nit N9:* "misattributes" is slightly strong, because in G_SM the
  non-affinity and the i+2 read are the same term (u_{i+1} ∨ u_{i+2}). Prefer "attributes to
  nonlinearity what, under product priors, requires the same-colour read".

**§3.2, correction to the BRIDGE premise.** BRIDGE §0 item 6 (draft, [H]) lists "linearity" among
the premises. That is literally true of QP's stated class N, which is linear. The writer's
refinement, that the obstruction uses the bipartite centre-free read pattern plus affinity (G2),
is correct. Calling it a "correction" is fair only as a correction of what is *used*.

## 4. Item 4 — scope of P2 and P3 (assessment for the owner; the owner decides)

**What they do.**
- They iterate the second-order form u′ = F(u) − v, v′ = u on cycle graphs C₄, C₅ and C₆. The
  coefficients are random symmetric per tick and per edge (P2), or random local tables per site
  and per tick (P3), at q ∈ {2, 3, 5}, for up to 5 ticks.
- They record coefficient vectors (P2) or functional support (P3).
- P2(B) is a one-step identity, checked exhaustively.

**What they do not do.**
- They compute no OI observable, encoded state, carrier law, CP map, prior, record statistic or
  readout.
- They instantiate no proposed mechanism. G_SM, G_σ, NNB and the AP1 apparatus are not run; P3's
  i+2 countercontrol borrows only G_SM's read *pattern*, with random tables.
- They adopt no premise.

**My assessment.**
- **Within "exact generic checks" in substance.** The objects are generic: arbitrary graphs,
  coefficients and functions. The statements checked are the writer's paper lemmas: the G1
  induction, the Q(i) identity and G2's step-3 linearity.
- **Caveat (i), proximity.** P2(A), P2(C) and P3 iterate the framework's own update form, which is
  the native step of Main:726 (xiii), over several ticks. That puts them nearer to "running the
  dynamics" than an identity check is. P2(B) and P1 are cleanly generic. P3 is the most
  mechanism-adjacent, because of its SM:112 read-pattern countercontrol.
- **Caveat (ii), sampling.** P2(A) uses 20 seeded random runs and P2(C) 50. These are exact in
  arithmetic but sampled. They are instances of universally quantified paper claims and support
  nothing beyond the [A] proofs.
- **Caveat (iii), redundancy.** None of P2(A), P2(C) or P3 is needed. Each supported statement
  has a complete short [A] proof, which I re-did (§3 above). If the owner rules them outside the
  authorization, nothing in ASSESS changes status except the [X] tags on rows 3a, 3b and 3c.

**Recommendation.** P1 and P2(B) are clearly within the authorization; `rv_p1.py` and `rv_p2.py`
are of the same kind. Ruling P2(A), P2(C) and P3 out costs nothing scientifically, so the
conservative choice is to drop their [X] tags and keep the [A] proofs.

## 5. Citations, §A.19 search, negatives, register

**Citations checked at fd539e15, all as quoted.**
- SM:96, :112, :224, :226, :232, :240, :306, :539 and :569 (ΓAΓ = −A at :569).
- Main:726 (v), (vii) and (xiii).
- Sub:98, :100, :102, :104, :159, :163, :220, :270, :272 and :274.
- ch02:84 and FULL:718 (identical text).
- MECH-1:434 and MECH-2:42 ("A5 fails"), :532.
- M-INACC RESULT §0 (Q(iii) step (s1) fails for G_σ; Q conserved) and :371 (Q(i) fails for G_SM).
- QP nodes 1, 3, 6 and 9, and :836–848.
- PROOF-RECOVERY §§1, 5 and 6.
- H-D `round-h-d-a5-status-adjudication/result.md` U6, which quotes the lemma and the older
  "center-free branch reduces it to a linear one" wording without separating the two forms.
- A5 §1.2, §3.2 and §6, including the N8/N8′ and N10 statements the writer cites.
- The row 2 identity, that Γ carries (A, b𝟙) to (−A, bε), and B0.1 are re-derived.

**B1 (blocker) — §A.19 / §A.25 search incomplete.** `git grep` over `papers/*.md` at fd539e15
finds three Structure sites that ASSESS does not cite:
- **Structure:219.** "OI's claim that the affine part of A5 … is forced … conditionally: the
  forcing runs through amplitude-scale gauge … An affine rule is therefore forced *given* that
  operational principle". This is the same overstatement as Sub:100.
- **Structure:259.** "amplitude-scale gauge invariance yields the affine restriction, weaker than
  A5 ([Main §4.5], item (vii))". It cites Main (vii) but drops its base-point qualifier.
- **Structure:219 and :301.** Under the alphabet-size hypothesis, "Non-linear dynamics over ℤ/qℤ
  generically produce q-dependent observable physics … violating the gauge equivalence". This is
  a corpus argument *against non-affine rules* from a principle other than amplitude-scale gauge.

**Consequences.**
- Owner question 1's site list, which would go to #1029, omits Structure:219 and :259.
- §2.1's negative "No corpus source gives it an independent reason" must cite Structure:219/:301
  and dispose of it. A5 N10 treats the same hypothesis for b = 0 only, finds it "Undetermined",
  and finds that it overshoots at cycle-type level.
- The disposition is likely to be that the argument is "generically", heuristic and conditional
  on an unproved hypothesis whose cross-q correspondence is unconstructed (SM:94). It therefore
  does not establish the base-point form, and the conclusion survives.
- The alphabet-size hypothesis already sits in Q-NEXT's list, so the gap is in the record, not in
  the direction of the next question.
- Also run the propagation grep over the `.tex` derivatives, which mirror the same sites.

**B2 (blocker) — Q-NEXT's "Equivalently" (§A.34, directional).**
- "Does any independently justified OI principle imply the site-wise base-point form in d = 3?
  Equivalently: does any such principle exclude the P1 class …?" Only one direction holds.
- A principle implying the base-point form (⇔ affinity, by the lemma) excludes P1's non-affine
  class. A principle that excludes P1's class need not exclude other non-affine rules: P1's class
  is a set of witnesses, not the complement of the affine class.
- The "Why it is small" paragraph says "P1 already reduces it to one function class … checked by
  asking whether it constrains f beyond the uniform group". That paragraph rests on the false
  converse.
- **Fix.** State exclusion of the P1 class as a *necessary condition* (a cheap screen) for a
  positive answer. Keep the question as stated in its first sentence. Drop the "reduces it to one
  function class" claim, or state it as "a negative answer can be shown by P1-type witnesses".

**B3 (blocker) — "b = 0 does work only at four sites" (§0 item 3, §3.1; the brief's "only four
places").** This is a negative over A5's dependency inventory, and the table omits these rows:
- **D7.** Theorem A.1 period qL (SM:92), "Not transferred, and not examined" in A5. Whether b = 0
  matters there is unknown.
- **D12 and D13.** The kernel results `StochasticInterface` gap and `HydroSourceAudit` advection
  gate are proved under A5. Their extensions to affine rules are [D] in A5, unreviewed, so b = 0
  is used by the kernel statements as they stand.
- **D15.** SM:1416, Layer-2 candidate classes "linear dynamics (A5)".

**Fix.** Add these rows and restate the count as "among the rows examined". Alternatively,
classify D7 as open and D12, D13 and D15 as b0-dependent pending [D] extensions. §0 item 4 ("the
b = 0 content sits on one sector") inherits the same scope.

**Negatives, other scope points.**
- F-1's NEW label is consistent with the search. A5 scoped non-affine rules out (A5 §6 "Open"), and
  no record separates the uniform form from the base-point form for non-affine rules.
- "R5 remains a finite search" and §7 item 5 ("No universal negative is stated") are well scoped.
- *Nit N10:* §3.3 "For odd q this is α ≡ 1/d" needs gcd(d, q) = 1. At d = 3, q = 3 the locus
  κ ≡ 2 is empty.
- *Nit N11, item 5 (SA-1(a) column (ii)).* Two problems with the proposed rewording "conditional
  on A4 and on the affine restriction (a posit); linearity beyond affine not used":
  - It presupposes F-1's acceptance and an owner decision in "(a posit)". Prefer "the affine
    restriction (whose derivation from amplitude-scale gauge needs the site-wise base-point
    form)".
  - It drops the symmetric-coefficient / form-lemma input that SHARED's column also relies on
    ("form, symmetry and symplecticity").
  The substance, that b = 0 is not used, is correct: AP1's backaction identity treats a known
  displacement as no disturbance.

**Register.** ASSESS is a verification note, not `papers/` prose, so §A.32/§A.33 do not bind it.
- It contains no manuscript edit, no self-narration in manuscript voice and no caps emphasis
  outside identifiers.
- Status labels are used consistently.
- The [P] labels on WIP / UNVERIFIED records (A5, Q4, QP, MECH-2, M-INACC) are explained in §1 as
  "record, not established". They are used as cited records, not as premises (§A.46 item 7
  respected).
- Draft inputs are labelled [H].

## 6. Summary of findings

| ID | Kind | One line |
|---|---|---|
| B1 | blocker | Structure:219 and :259 overstatements missed; Structure:219/:301 alphabet-size argument against non-affine rules not disposed (§A.19, §A.25) |
| B2 | blocker | Q-NEXT "Equivalently" is one-directional: excluding the P1 class is necessary, not sufficient, for the base-point form; the "one function class" smallness argument falls with it (§A.34) |
| B3 | blocker | "b = 0 only at four sites" omits A5 D7 (unexamined), D12/D13 (kernel under A5) and D15; restate as "among rows examined" |
| N1 | nit | Note that (R-uni) forces κ ≡ 2 and add the κ-general form (rv_p1 B) so the counterexample does not look like it rests on an over-strong reading |
| N2 | nit | "d ≥ 2" → "d = 2, 3" (only these are exhibited) |
| N3 | nit | Applying owner Q2 to rescalings and the affine question is the writer's extension, not [O] |
| N4 | nit | d = 1: with reflection the result holds at every odd q (λ = −1 plus evenness); "G is linear" fails at composite q |
| N5 | nit | Short forms of the d = 1 claim must carry centre-free, NN (two read variables) and odd q |
| N6 | nit | "fails only when …" follows from the [A] induction, not from P3 |
| N7 | nit | Node 9 / PR §5 is about separate availability, not G2's run difference |
| N8 | nit | "Step 3 fails in general" → "step 3's identity is not available" |
| N9 | nit | "misattributes" → the grading break under product priors needs the same-colour read; G_SM's non-affinity and i+2 read share one term |
| N10 | nit | α ≡ 1/d needs gcd(d, q) = 1 |
| N11 | nit | Proposed SA-1(a) wording presupposes "(a posit)" and drops the symmetric-coefficient input |
| S1 | strengthening | Non-affinity of the d = 3 family at every prime q ≥ 5 has a one-line paper proof (§1.1) |

**What re-review needs.** B1–B3 applied, and a diff check of the changed passages. No new
computation is required.
