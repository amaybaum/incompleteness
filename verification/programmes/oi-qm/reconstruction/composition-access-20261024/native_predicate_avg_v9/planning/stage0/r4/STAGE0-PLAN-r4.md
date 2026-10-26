# NP-AVG-1 Stage 0: masking geometry of the passive-readout class (r4)

26 October 2026, draft r4. A preregistration for Issue #929. The owner approved a
Stage-0 plan on 2026-10-26. This revises `STAGE0-PLAN-r3.md` (SHA-256
`683acdf46c28af943799f6fa053c0952eb557f6b6b8babd3a775f89bb1cbe32c`) after its re-check
(`review/STAGE0-RECHECK-r3.md`, committed at `6f35cc59`; RC1–RC10 and nits N1–N9). Every
change from r3 is traced to an RC item or nit in `STAGE0-CHANGES-r4.md`. Earlier rounds:
r2 (`STAGE0-PLAN-r2.md`, SHA-256
`2aa1620675b98bd2492fdc9fe17e72405340bb7365dc650611c58ff4af81d38a`) and its re-check
(`STAGE0-RECHECK-r2.md`, SHA-256
`33c279ef1b2f7af9a61386e492516e94b044a4403cd0765ea36b7298acbd76e6`, re-check R1–R6).
Item names: "review R#" is the r1 review, "re-check R#" the r2 re-check, "RC#" the r3
re-check (N2). r1 is `STAGE0-PLAN.md` (SHA-256
`4720ac77ecaa40aa16012eb4949743ac87fbed2c7f2f16cab80f4a9255471429`); its review is
`STAGE0-REVIEW.md` (SHA-256
`3392ca6622adbbb65a742a70cb3feef506c4b132b7a1ca2487c43dcc89defc19`).

**What Stage 0 is.** A geometry-only investigation, not a prediction experiment.
It computes no probability law of a native record. The one law computation is
S6, an approved, labelled proof-check on the 21-bit reference structure of Φ. It
does two things:
- it states the collapse argument of `RECHECK-r2.md` (SHA-256
  `676ecc085d3c2f329df6a05426550f8d6a914092bc553d678f844066f935d7a7`, §1) as
  propositions with proof obligations;
- it computes, exactly and with integer arithmetic, the masking closure of
  every record of the class.

Stage 1, the law machinery of `PLAN-r2.md` (SHA-256
`c9d8dbf86ab4b9add0fa030a157aeaab67df9d728e8baa22b99bfd85a05842c2`), runs only
if the owner approves it, and then only on what Stage 0 leaves.

**Launch and freeze.** The enumeration is not authorized by this plan. Launching
it, adding its workflow and every dispatch need owner approval, and it runs in
CI (§A.40, §A.43). The plan is committed alone, on a base containing
`fc452ea825b986a3babab5d110626e0019c39847`. §12 records the owner's decisions
and the remaining open items, each at its proposed value.

**Owner decisions (2026-10-26), recorded as decided:**
- **S6** is approved. It runs as an additional, labelled proof-check beside the
  three-case proof of PO8. It is not a result.
- **S1a** (the global closure bound) is included now. **S1b and S1c** are
  deferred. The global bound decides whether a larger search is scientifically
  useful and computationally justified; the search is never expanded merely
  because resources exist.
- **S4** (orbit representatives) is approved, under the R5 symmetry control,
  with a check that the reduction preserves the relevant counts: orbit-weighted
  counts must equal full counts on every checked instance (C8).
- **S9.** Every work in §8 is checked first-hand before any novelty claim.
- **R1–R9:** proceed.

**Execution sequence (owner):**
1. Apply R1–R9 and regenerate the affected design evidence.
2. Run S6, the corrected mutants, the planted controls and the small exact
   reference checks. The production and reference code are exercised on toy,
   planted and small-window instances, and on S6's 21-bit carrier structure
   only, never on v8's configuration class.
3. Submit plan, code and evidence for independent review.
4. Freeze the accepted plan with exact code and configuration hashes.
5. Enumerating v8's configurations needs a separate authorization.

Steps 1 and 2 are done as design evidence; §9 records them.

**Owner decisions on O1 and S11 (2026-10-26).**
- **O1, two-layer freeze: approved.** In the owner's terms:
  - Layer 1 is the scientific specification. It freezes the masking law, the
    geometry, the equivalence rules, the search domain, the invariants and the
    acceptance criteria.
  - Layer 2 is the implementation. Only after Layer 1 passes independent review
    are the production enumerator, the controls, the configuration hashes and
    the execution certificate finalized and frozen.
  - "Complete enumeration code now: No; defer until the design layer is
    frozen."

  This plan is therefore the Layer-1 object (§5b). The existing code is design
  evidence. The actual v8 enumeration is not authorized.
- **S11, P_A-dir: adopted as a required control, not a diagnostic.** In the
  owner's words: "It must detect incorrect elimination in individual directions
  even when aggregate counts appear correct." C11 (§6) is now required; its
  failure gives VOID or MISMATCH. §9 records the non-vacuity demonstration.

**Owner decisions on the r3 re-check (2026-10-26).**
- **O-a, approved.** The r3→r4 diff, with its new tests and results, is
  independently reviewed. The freeze follows only a clean independent acceptance.
- **O-b, approved in principle.** "Define and preregister the S1b/S1c trigger
  before examining S1 results. The trigger must depend on objective outcomes, not
  whether the result is desirable." The trigger is §12's rule T.
- **O-c, approved.** RESIDUE_UNLINKED keeps its G clause, resting on PO6 as stated
  in full in §4 ("independent of G given the frame").
- **O-d, approved.** RC7's new planted families and mutants are run now, on toy
  and planted instances only (§9).

**What Stage 0 does not claim.** Survivor counts are counts of configurations.
They imply nothing about unpredictability, computational hardness or quantum
behaviour. Any such reading needs a separate argument and is out of scope.
Empty, small or unfavourable survivor sets are valid outcomes.

## 1. Configuration space (frozen)

The geometry is v8's: q9 at the origin, n = 6, the complete six-neighbour
two-slice rule x_t = x_{t−2} ⊕ H(⊕_e x_{t−1}(· + e)), and H a permutation of
the eight triples.

- **Region:** Reg = ball(4), the ℓ¹ ball of 129 sites.
- **Items:** (x, t) with x ∈ Reg and t ∈ {−1, …, 23}, read as whole triples at
  every slice −1..t. There are 3,225 items (`PLAN-r2.md` O2).
- **Records:** sets of at most k = 2 items at distinct sites (`PLAN-r2.md` O1): 3,225
  singles and C(129, 2) · 25² = 5,160,000 pairs. The empty record is the base
  context (§5, S10).
- **Fixed quantities** (never eliminated): Φ, which is the six neighbours of q9
  at slice 7 together with V = q9 at slice 8; and p = q9 at slice 6.
- **Port samples:** N[0..n], the whole triples at (0, 0, −3) at slices 0..6.
  They are public and eliminable under A. Under G they are in-frame.
- **Context Ctx(R):** the fixed quantities, the port samples and every sample of
  R's items.

**Equivalences** (frozen; each is counted, none excludes a record):
- **E1, identity merge.** A record sample at a Φ site-time, at p or at a port
  sample is that quantity ("Φ in clear", "p in clear", "port in clear").
- **E2, parity (L1).** Odd-class samples are dropped as inert.
  Masking-equivalent records, those with equal even-class contexts, are
  counted.
- **E3, unordered pairs at distinct sites** (RC4). A same-site pair
  {(x, t1), (x, t2)} has the context of the single item (x, max(t1, t2)), which is
  enumerated; it is not a separate record.
- **E4, symmetry.** The group is C4v (order 8), the stabilizer in O_h of
  {Reg, q9, Φ's site set, port}.
  - It fixes q8 and q10 and permutes m with the other three neighbours.
  - The closure geometry is C4v-equivariant under A and under G. Under G, the
    frame's even part B8 is O_h-invariant, and the sources lie in the frame.
  - **Source-dependent attributes are not C4v-invariant**, because the
    sources (−7, 0, ±1) and (−8, 0, 0) are not. These are G-linkage, source
    cells, and the identities of the m and o cells. They are always computed
    per record (C8, S4).

## 2. Masking rules (frozen)

**Convention A (reference pair (7, 8)), under the fair prior.**
- **F type** (slice t ≥ 8, depth d = t − 8):
  - cone: slice 8 within d, and slice 7 within d − 1;
  - near tips: c ± d·e on slice 8 (c itself when d = 0);
  - far tips: c ± (d − 1)·e on slice 7, for d ≥ 1.
- **B type** (slice s ≤ 7, depth d = 7 − s): the mirror image, with slice 7
  near and slice 8 far.

**Convention G (initial pair (−1, 0)).** Every quantity is F type from slice 0,
with depth t:
- cone: slice 0 within t, and slice −1 within t − 1;
- near tips at distance t on slice 0; far tips at distance t − 1 on slice −1.

**Eligibility** (RC3). Under A, every tip is eligible. Under G, a tip is eligible
iff it is a seed, that is, outside the frame. The frame is the union of the
G-convention cones (slices −1 and 0) of Φ, V, p and the even port samples; its even
part is B8 (PO7).

**B8** (RC2) is V's cone in the pair (−1, 0): the even cells of slice 0 with
|c| ≤ 8 and of slice −1 with |c| ≤ 7.

**Parity.** Within the even class, cone membership has the correct parity
automatically (PO1). A consequence: on even-class contexts, a far-slice radius
of d and one of d − 1 select the same cells. The radius asymmetry therefore
acts through parity, and "symmetric radii" is not a distinguishable variant
(§6, mutant list).

**Rule L3′ (frozen, S2).** A non-fixed quantity q is eliminated if some
eligible tip u of q lies in the cone of no other currently retained quantity.
- The rule is iterated to its fixed point.
- ret(R) is the retained set.
- Elimination is monotone and does not depend on the order, and the eliminated
  set is jointly independent of the retained set (PO4, checked exactly by C15).
- Near-only L3 is reported beside L3′. The labels use L3′. L3 is L3′ with the far
  tips removed; cones are unchanged (RC3).

**Soundness of the far tips** (written proof in the report; the review's §1).
Fix every pair variable except x_E(u). Then x_{L+1}(u) = x_E(u) ⊕ H(…) is a
bijection of x_E(u). In the shifted pair (L, L+1), x_{L+1}(u) is q's near axis
tip at distance d − 1. The backward case is the mirror image.

Both rules are sufficient conditions only. "Retained" means "not eliminated by
the declared rule".

## 3. Survivors and their classification (frozen)

**Base precondition (review R8).** Every label of §5 presupposes that the base context
(the empty record) is collapsed under A and under G. The hand derivation below
is checked in C6, and is written into the report before the computed value is
read.
- **A:** N[1] (B type, depth 6) has the largest reach on the port's site. Its
  −z tip (0, 0, −9) on slice 7 lies in no other cone, so N[1] goes. N[3] goes
  next, by its tip (0, 0, −7). N[5]'s +z tip is q8, which Φ covers, but its −z
  tip (0, 0, −5) is free, so N[5] goes too. Only Φ and p remain.
- **G:** the port samples' cones lie inside B8 (PO7), so they have no seed tip,
  and nothing has a seed tip.

If the computed base is not collapsed, §5 uses the base-relative labels.

**Single item (q9, 9)** (RC8; C6's execution-time instance, written here before
any computed value). Its even samples are q9 at slices 0, 2, 4, 6 and 8. Slices 6
and 8 are p and V in clear (E1). Under A, (0, 0)₀, (0, 0)₂ and (0, 0)₄ are B type,
at depths 7, 5 and 3. Their +x near tips (7, 0, 0)₇, (5, 0, 0)₇ and (3, 0, 0)₇ lie
in no other cone once larger cones are gone. The port samples go as in the base.
So the record is collapsed under A, with p and V in clear. Under G, the three
samples have |c| + t ≤ 4: they are in-frame and retained, with no seed tip. So the
record is collapsed under G, with truncated record {q9@0, q9@2, q9@4}.

**Survivor definitions:**
- **A-survivor:** S_A(R) = ret_A(R) ∖ (Φ ∪ {p}) is nonempty.
- **G-survivor:** S_G(R), the retained quantities with at least one seed tip, is
  nonempty. The retained in-frame record samples are the truncated record.
- **Collapsed:** neither of the above holds.
- **Tie residue:** the set of all survivors.

**Linkage** (N1). Under A, J-linked ⊂ Φ-linked, and the three classes are:
- **J-linked:** the cones of S_A contain q8 or q10 at slice 7;
- **Φ-linked but not J-linked:** they contain a Φ cell (the six slice-7 cells or
  V's cell) but neither q8 nor q10;
- **unlinked:** they contain no Φ cell.
- **G-linked:** the cones of S_G contain a source cell at slice 0. This is
  computed per record.

**Distinguishability at the masking level (review R6),** replacing r1's "observer
interface":
- **(a) Observer-equivalence classes.** Records are grouped by their
  post-closure retained public set: p, V, any Φ in clear, retained record
  samples and retained port samples. Two records in one class are
  indistinguishable to the observer at the masking level. Classes are counted
  overall, among collapsed records and among survivors, under A and under G.
- **(b) Private dependence set** (RC5). Under A: the Φ cells (six slice-7 cells
  and V) in clear, together with the private Φ cells inside the cones of the
  retained non-fixed public quantities (record and port samples), split into J
  cells (q8, q10) and others. Under G: the source cells inside the cones of the
  retained non-fixed public quantities. Computed per record where
  source-dependent.
- **(c) Limit.** Linkage is necessary, not sufficient, for distinguishing
  carrier states. Distinguishability is a law question for Stage 1.

**Structure:**
- the cover graph and its components;
- the shared aligned tips: axis line, tip and reach;
- the residual support in bits, against S_max = 27;
- rule dependence (L3 only, L3′ only, or both).

**Degeneracies.** Each is counted and cross-tabulated with survivors; none is
excluded:
- items at q9, at a Φ site or at the port site, and items on the z-axis;
- pairs on a common axis line;
- records with a nontrivial stabilizer;
- items with t ≤ 0, and items with t = −1;
- masking-equivalent records (E2);
- records whose last sample is odd-class.

**Counterexamples reported:** records on which L3 and L3′ disagree; retained
self-supporting dynamical-constraint blocks; any survivor that contradicts
`RECHECK-r2.md` §1.

## 4. Propositions, corollaries and proof obligations

**Definitions** (RC2). For q = (c, t) of type T and depth d, and an axis direction
e, the *e-tip* of q is its near tip c + d e, and its *reach in e* is c·e + d. For
a set S, M_T(e) is the largest reach in e among the elements of S of type T (−∞ if
there is none). The *aligned directions* of q are the e = ±e_i with
c_i = ±‖c‖_∞ (all six when c = 0); ρ(q) = ‖c‖_∞ + d.

- **P_A** (rests on PO3, PO5). If S_A(R) is nonempty, every ρ-maximal element of
  S_A(R) shares each of its aligned near tips with another element of S_A(R) of
  the same type, at equal reach on the same axis line.
- **P_A-dir** (required, S11; rests on PO3, PO5). For every direction e, with
  S = S_A(R): if M_F(e) ≥ M_B(e), every F element of S at reach M_F(e) has its
  e-tip shared with another F element of S or located at a Φ site-time.
  Symmetrically for B type. When the two reaches are equal, both apply.
- **P_G** (rests on PO3, PO7). If S_G(R) is nonempty, every ρ-maximal element has
  |c| + t > 8, and shares each of its aligned near tips, a seed, with another
  element of S_G(R).
- **P_G-dir** (required, S11; rests on PO3, PO7). For every direction e, with
  S = S_G(R): if M_F(e) ≥ M_B(e), every F element of S at reach M_F(e) whose
  e-tip is eligible has its e-tip shared with another F element of S.
  Symmetrically for B type (slice −1, depth 0). When the reaches are equal, both
  apply.
- **C_A** (rests on PO8; for unlinked survivors also on PO6 (A)). A record
  collapsed under A fails Law_A. An unlinked S_A reduces to this case.
- **C_G** (rests on PO7, PO9; for G-unlinked survivors also on PO6 (G)). A record
  collapsed under G has Law_G = Law_P of its truncated record on each frame. That
  fails on all seventeen frames, by v8's per-family negative for every R and v8's
  zero-background diagnostic (`native_predicate_v8/REPORT.md:19-21, 37`).

**Proof obligations** (written in the report):

| item | statement |
| --- | --- |
| PO1 | Cone radii as stated in §2, forward and backward, under A and G. Within the even class every cone member has the parity of its radius automatically, so a far-slice radius of d and one of d − 1 select the same even cells |
| PO2 | L1 (parity decoupling) and L2 (uniform slice pairs under π), from `PLAN-r2.md`. For every fixed value of all other pair variables, a quantity's triple is a bijection of each of its near axis tips (distance d) and far axis tips (distance d − 1, d ≥ 1), by the unique straight path |
| PO3 | Covering inequalities. Let q have type T, depth d, and e-tip u at reach r = c·e + d. (a) If q′ has the opposite type and u lies in the cone of q′, then the reach of q′ in e is at least r + 1. (b) If q′ has type T and u lies in the cone of q′, then the reach of q′ in e is at least r, with equality only if u is also the e-tip of q′ (a shared tip). (c) Under A, u lies in the cone of a fixed quantity only if u is a Φ site-time (PO5) |
| PO4 | Iterated elimination is monotone (a larger context retains a superset) and order-independent (the result is the greatest self-supporting subset). The eliminated set is jointly uniform and independent of the retained set: under A, under π; under G, given the frame |
| PO5 | Φ-cover. Under A, the fixed quantities are Φ's seven cells, each of whose cone is itself, and p, whose cone is exactly the six slice-7 Φ cells and V's cell. So a tip lies in a fixed cone iff it is one of Φ's seven site-times: F near tips only at V's site-time, B near tips only at the six slice-7 Φ cells. The aligned near tip of a non-fixed quantity is never a Φ site-time: its norm is \|c\|₁ + d, which is 0 only for V itself and 1 only for a slice-7 Φ cell or p |
| PO6 | (A) Under π, if no cone of an element of S_A contains a Φ cell (the six slice-7 cells or V's cell), then S_A is jointly independent of Φ, and the record's law given (p, V, Φ in clear) is that of the collapsed record. (G) Given the frame, if no cone of an element of S_G contains a source cell of G at slice 0, then S_G is a function of the frame and the seeds only, hence independent of G given the frame, and Law_G of the record equals Law_P of its truncated record on that frame |
| PO7 | The even part of the frame equals B8 (slice 0: even, \|c\| ≤ 8; slice −1: odd, \|c\| ≤ 7). A quantity with \|c\| + t ≤ 8 has its whole cone inside the frame, and has no seed tip. A quantity has a seed tip iff \|c\| + t > 8 |
| PO8 | The Φ-in-clear lemma. Under A and π, Φ's seven triples are i.i.d. uniform and p = V ⊕ H(⊕ of the six slice-7 triples). Take any value of (p, V) with p.A = 0, and any set C of at most two of the six slice-7 Φ triples read in clear. (1) If q8 ∈ C, Y is fixed on every class, while t1(s) and t0(s) both give positive mass to both values of y, so no class is target-law. (2) If q10 ∈ C, R and Z are fixed on every class, and the same holds. (3) Otherwise C ⊆ {m, o1, o2, o3} with \|C\| ≤ 2. At least two of those four triples are unread and fresh, so (q8, q10) is uniform given the record, and J is uniform on every class. That is neither t1/20 (t1 has a zero entry) nor t0/44 (t0 is not uniform). Hence Law_A fails for every collapsed record. S6 checks all 22 subsets exactly |
| PO9 | C_G's reduction to v8: v8's negative holds for every R in C(4, 16), stream-closed or not, family by family and on the zero background (`native_predicate_v8/REPORT.md:19-21, 37`). A truncated record is a set of site-times of v8's domain, so it is covered |

**Proof versus computation.**
- **Proof:** PO1–PO9, P_A, P_G and the corollaries. C_G also inherits v8's
  computed negative.
- **Computation:** the closures, survivors, classifications and counts; the
  mechanical checks of P_A, P_G, P_A-dir and P_G-dir on every
  survivor; C15's exact soundness check of the elimination on small windows.
- **The asymmetry.** MISMATCH can detect over-retention: a survivor violating a
  proposition. It cannot detect over-elimination, since that only produces
  fewer survivors. Over-elimination, the error that favours collapse, is
  guarded by C2, C3, C6, C7 and C15, and by the mutant campaign.

## 5. Decision rule (preregistered)

Precedence, first match. Labels are generated from the measured values.

- **VOID** (RC1)**:** a required control fails, other than through one of the
  MISMATCH conditions below. These are C6's execution-time hand instances, C9,
  C10 (ii), C11 (ii) and C12. A run in which both a VOID control and a MISMATCH
  condition fail is VOID.
- **MISMATCH:** the computation contradicts a proof statement. That is, one of
  the following happens:
  - a survivor, or a planted retained set, violates P_A, P_G, P_A-dir or
    P_G-dir (C11 ii; PO3, PO5, PO7);
  - a fixed quantity is eliminated (PO5). C10 (i) is a code invariant that
    cannot fail by construction (§7), so it is not a control in VOID's list;
  - a port sample is not in-frame under G (C10 ii; PO7);
  - a retained in-frame cone leaves the frame (C12; PO7);
  - L3′ retains something L3 does not (C9; PO4);
  - a retained set lies outside the global closure bound (C9; PO4);
  - a hand derivation in C6 disagrees with the code (§3).

  The minimal witness is recorded (C16). Neither the proposition nor the counts
  is reported as established. Resolution needs a written amendment naming the
  error, and a full re-run of every control. Neither side is preferred
  silently.
- **INCOMPLETE:** a shard is missing, failed or non-deterministic, or the
  coverage check fails.
- **BASE_RESIDUE:** the base precondition (§3) fails.
  - The base retained set is reported.
  - A survivor is then a record whose retained set contains a quantity outside
    ret(∅).
  - The labels below are printed in base-relative form.
- **COLLAPSE_ALL:** every record is collapsed under A and under G. The text
  states that collapse is established by the exact closure computation, with
  every required control of §6 (C0–C3, C6–C18, the refusal check, the native
  self-test and S6) green (RC1), and is turned into law failure by the proved
  corollaries:
  - Law_A fails for every record of C_avg(4, 16, 2), by C_A;
  - Law_G fails on v8's seventeen frames, by C_G.

  P_A and P_G play no part in this label. Stage 1 is not needed for k ≤ 2.
  This is a consistency-axis result.
- **RESIDUE_UNLINKED:** survivors exist, and all are unlinked under A and
  G-unlinked under G. Law_A and Law_G fail for them, by PO6 (A) with C_A and PO6
  (G) with C_G (owner decision O-c). Stage 1 is not needed for k ≤ 2.
- **RESIDUE:** linked survivors exist. The classified residue is the output,
  and Stage 1, if approved, is restricted to it.

## 5a. Three independent safeguards (owner requirement)

Each safeguard uses reference calculations independent of the production
closure (`s0geom.py`) wherever practical:
- `s0native.py` is a separate native evaluator: scalar and bit-sliced, with no
  shared code.
- `s0ref.py` is a separate reference closure. It has its own context builder,
  cone and tip code written from this plan's text, and a different algorithm.

1. **Soundness.** Every elimination is justified by the frozen rule, and an
   incorrect elimination fails a control.
   - **C15:** exact uniformity and independence of the eliminated set, against
     brute-force marginals from `s0native` on exhaustive small windows.
   - **C18, elimination audit:** each logged elimination (q, u) is re-checked
     with `s0ref`'s cones and tips. The tip must be a valid tip of q, eligible,
     and uncovered by every quantity alive at that moment.
2. **Completeness.** Every eligible configuration is considered and every
   required elimination applied.
   - **C13:** a coverage manifest (exact index ranges, union equal to the domain,
     disjoint) and an independent recount by separate enumeration and formula. A
     skip-record mutant must fail it.
   - **C17, fixed-point verification:** using `s0ref`'s code, no retained
     quantity may have a free eligible tip.
   - **C7:** agreement with `s0ref`'s greatest self-supporting subset.
   - The un-applied-elimination mutant must fail C17 and C7.
3. **Non-vacuity.** Planted survivors (C3 families, the constraint block, and
   C11 (iii)'s families and Φ- and frame-adjacent families) must be retained.
   Planted non-survivors (each family minus one tip quantity, the block minus its
   centre, and C6's axis pair) must collapse. In-frame G plants are reported as
   the vacuity contrast. This distinguishes genuine collapse from accidental
   over-elimination.

## 5b. Two-layer freeze (owner decision O1, approved 2026-10-26)

**Layer 1: the scientific specification. This plan is the object to be frozen**
at owner step 4, after it passes independent review. It freezes:
- the masking law: L3′, with L3 reported beside it (§2);
- the geometry: the setup, the conventions, the pairs, the asymmetric cone radii
  and the frame (§1, §2);
- the equivalence rules: E1–E4 and the symmetry group (§1);
- the search domain: k ≤ 2 stream items, the S1a global bound, and S1b and S1c
  deferred (§1, §12);
- the invariants and propositions, with their proof obligations (§4, §7);
- the acceptance criteria: the survivor definitions and classification (§3);
  the decision rule and labels (§5); the safeguards (§5a); every control's
  definition and pass condition, including the required C11 (§6); and the
  coverage limits (§11).

**Design evidence, not frozen.** The code in `stage0/code-r4/` and the
evidence in `stage0/design-r4/` show that the specification can be
implemented and that its controls can fail. Layer 1 does not freeze them. The
code is: `s0geom`, `s0ref`, `s0native`, `s0controls`, `s0mutants`, `s0s6`,
`s0symcheck` (r1's `sym_check` folded in) and `s0run`. Its SHA-256 values are in
`RUN-MANIFEST.json`, as a record of what produced the evidence.

**Layer 2: the implementation.** It is a stated plan with its own later review.
It is finalized only after Layer 1 passes independent review: "Complete
enumeration code now: No; defer until the design layer is frozen". It is then
independently reviewed and hash-frozen before any launch authorization. Nothing
executes on v8's class without it. It covers:
- the production enumerator;
- the production control suite and mutant campaign, finalized from the design
  evidence against the frozen §6;
- the configuration hashes;
- the execution certificate.

It must contain:
1. **The record driver.** The index space through `record_at` (v8 parameters,
   authorization-bound), with orbit representatives (S4), the shard plan, and a
   mandatory dry run that prints the shard plan and context sizes without
   computing any closure.
2. **Per-record analysis** under A and G, with L3′ and L3, through `s0geom`'s
   frozen engine. This yields: survivors, the classification of §3,
   degeneracies, residual supports, and per-record G-linkage and source cells.
3. **C11, required.** It has three parts:
   - (i) the per-direction tip-status tables, compared with the reference, and
     the decision–table consistency (RC6);
   - (ii) P_A, P_G, P_A-dir and P_G-dir on every survivor and on the planted
     retained sets;
   - (iii) planted directional retention.

   It generates VOID (parts i and iii) or MISMATCH (part ii).
4. **Minimal-witness selection** (C16 order) on real records.
5. **The S1a driver:** the global closure bound on v8, under A and G, and per
   axis line.
6. **Shards and merge.** The shard schema and writer; the merge with exact
   coverage and disjointness; and the writers for `result.json` and
   `expected-controls.json`.
7. **The label generator** (§5): VOID, MISMATCH, INCOMPLETE, BASE_RESIDUE,
   COLLAPSE_ALL, RESIDUE_UNLINKED and RESIDUE. Labels are generated only by the
   merge, from structured files.
8. **The fail-closed certificate**, the re-check's items 1–8:
   1. **Frozen manifest.** The program verifies a manifest of the Layer-2 code
      SHA-256 values and the configuration constants (V8 setup,
      `Rule` fields, k, depth ranges, sampling rates, including C7's 1-in-1,000
      and C8's 1-in-100 (N6), S_max, budget, shard plan) at start-up. On any mismatch it prints VOID and exits 2 before computing
      anything.
   2. **Pre-flight controls** in the same job at the exact commit: C0–C3, C6,
      C10 (ii), C11 (planted sets and both direction mutants), C12–C18 (RC9 b),
      the refusal check, the native self-test and S6. Their structured
      results are read (§A.44); any failure is VOID, with no enumeration.
   3. **A passing mutant-campaign result** for the same code hashes, or the
      program refuses to run. Each mutant names its case and counts as killed
      only when that check fails cleanly on that case (§A.40). Mutants run only
      after the unmodified suite has passed. The campaign runs in CI (RC9 c).
   4. **In-run gates:**
      - C7 on its sample;
      - C8 equivariance and full count preservation on sampled and survivor
        orbits;
      - C9 against the computed v8 S1a bound;
      - C11 (i) on a deterministic sample of v8 records and on every survivor;
      - C11 (ii) on every survivor;
      - C17 and C18 on a deterministic sample of v8 records.

      A failure is VOID or MISMATCH under §5, never a label.
   5. **A merge that refuses** shards whose code or configuration digests differ
      from the manifest or from each other, or whose coverage is not exact
      (INCOMPLETE).
   6. **Authorization.** The v8 authorization is accepted only as an
      owner-designated input bound to the exact commit, and is echoed into
      `result.json`. `authorized_v8` is otherwise unreachable. The refusal is
      keyed on configuration content, not on an object flag. Any setup equal to
      v8's parameters is refused by every production, reference and native entry
      point. The refusal check includes a freshly constructed copy of v8's setup
      (RC9 a).
   7. **Determinism.** Normal and `-O` runs are identical per shard and merged.
      The dry run is mandatory before the real run.
   8. **Labels** come only from the merge's structured files, never from logs.

## 6. Required controls (each can fail)

**Configuration and code against the native rule**
- **C0, configuration space** (`s0symcheck.py` for v8's combinatorics;
  `s0controls.py` for the toy contexts). The following are checked:
  - the counts: 3,225 items and 5,160,000 pairs;
  - the orbit counts, 875 and 815,175, by direct canonicalization and by
    Burnside's lemma;
  - group orders 48 and 8;
  - ℓ¹-ball sizes equal the crystal-ball formula (A001845);
  - the context sizes per record, with production contexts equal to `s0ref`'s
    contexts. These catch the "odd samples kept" mutant.
- **C1, cones** (production `in_cone`), at the depths used and at both
  convention pairs:
  - A, pair (7, 8): F 0–15 and B 0–8;
  - G, pair (−1, 0): F 0–23, plus B depth 0.

  The method is lane-parallel native perturbation (`s0native.Lanes`) on generic
  random backgrounds; no v8 configuration is involved.
  - At depth ≤ 8, every cell within d + 2 on both slices is perturbed.
  - At depth > 8, every cell at distance d − 3 to d + 2 on both slices, of any
    parity, is perturbed, plus 1,000 deterministically sampled interior cells
    per depth, each on both slices: 2,000 interior perturbations per depth (N4).

  The measured dependence must lie inside the production cone, and each claimed
  radius must be attained. This also catches the swapped-slices mutant. The
  full run makes 301,640 perturbations. **Limit:** beyond depth 8, the cone's
  interior is sampled rather than perturbed exhaustively.
- **C2, tips** (production `tips`), at the same depths and pairs. Lane-parallel,
  eight lanes per tip, covering all eight values of each tip. Every near and far
  axis tip the production code emits must be a native bijection. Off-axis cells
  at the same distance must show non-bijective cases. The full run tests 541
  tips, with 39 non-bijective off-axis contrasts.

**Planted families and hand instances**
- **C3, planted families** (review R3). For every convention, type and depth used
  (A: F 1–15 and B 1–8; G: F 1–23), plant {q} together with every near and far
  axis tip of q as a depth-0 quantity, in the toy contexts.
  - Under G, the plant is centred outside the frame: at (6 + d, 0, 0) in the
    toy, at (9 + d, 0, 0) for v8's B8.
  - In-frame plants at depths 1–2 are the vacuity contrast, since inside the
    frame every tip is ineligible.
  - The production closure must retain each family in full.
  - The mutants that must eliminate them are listed under Mutants.
  - Also planted: the dynamical-constraint block (retained), and the block
    minus its centre (eliminated under L3′, retained under L3).
- **C6, hand-checked instances.**
  - Toy instances, worked in `STAGE0-NOTES-r2.md`: the axis pair collapses; the
    block and the block minus its centre behave as in C3.
  - At execution: the base context (the §3 derivation, under A and G) and the
    single item (q9, 9), derived by hand before their computed values are read.
    A disagreement is a MISMATCH.

**Independent implementation and symmetry**
- **C7, a second closure implementation.** A separately written algorithm
  computes the greatest self-supporting subset from an explicit cover graph. It
  has its own cone and tip code, written from this plan's text, and shares
  nothing with the production code. It must agree on every survivor, on every
  record containing a shared tip, and on a deterministic 1-in-1,000 sample of
  the rest. The sampling rule is a Layer-2 configuration constant under
  certificate item 1 (N6).
  - On v8 contexts (up to about 29 non-fixed quantities), `s0ref` runs in
    synchronous-deletion mode, so C7 compares two fixed-point algorithms there,
    not brute force. Brute force is used up to 8 non-fixed quantities, as on
    the toy class.
- **C8, symmetry** (review R5). The production retained set must be
  C4v-equivariant: ret(gR) = g·ret(R). This is checked in full on every
  survivor's orbit and on a deterministic 1-in-100 sample of orbits (a Layer-2
  configuration constant under certificate item 1; N6). Only C4v-invariant attributes are
  compared across an orbit: survivor status, sizes, Φ-linkage, J-linkage, and
  the counts of (b). G-linkage, source cells and the identities of m and o
  cells are computed per record. For survivor orbits, the closure of every
  record in the orbit is computed directly.
  - **Count preservation (S4, re-check R3, RC10):** every reported count,
    computed from orbit representatives, must equal the full computation on
    every checked instance. Representatives' retained, public and (b) sets are
    carried to each orbit member by the group action; source cells are
    recomputed per record. **The reported counts are exactly the following
    (52 on the toy class; on v8 the same list):**
    - per convention (A, G): survivors; L3/L3′ disagreements; observer classes
      overall, among survivors and among collapsed records;
    - under A: Φ-linked records; J-linked records; survivors J-linked,
      Φ-linked but not J-linked, and unlinked (N1); records whose (b) contains
      a J cell; records whose (b) contains a non-J Φ cell;
    - under G: records whose (b) contains a source cell (per record);
    - per convention, every degeneracy of §3 cross-tabulated with survivor
      status (8 degeneracies × 2);
    - masking-equivalent records; records with a nontrivial stabilizer.

    Count preservation covers every item of this list. G-linkage and source
    cells are computed per record and never orbit-reduced. The checked instances are
    the full toy class now (design evidence) and, in the Layer-2 v8 run, every record
    of a deterministic 1-in-100 sample of orbits and of every survivor orbit.

**Monotonicity, frame and propositions**
- **C9, monotonicity.**
  - For every record, ret_{L3′} ⊆ ret_{L3}.
  - Every record's retained set lies in the global closure bound (S1a).
- **C10.** It has two parts:
  - (i) a **code invariant**, not a control that can fail, since the closure
    iterates only non-fixed quantities: no fixed quantity appears in an
    elimination log;
  - (ii) under G, every port sample N[0..n] is in-frame, with no eligible tip and
    its whole cone inside the frame. This part can fail.

  E1 merges are counted.
- **C11, the per-direction control (required, owner decision S11).** "It must
  detect incorrect elimination in individual directions even when aggregate
  counts appear correct." It has three parts.
  - **(i) Per-direction tables and decisions.** At every elimination the closure
    records the status ('free', 'covered' or 'ineligible') it assigned to each
    labelled tip of the eliminated quantity: (e, near) and (e, far) for the six
    axis directions e. It records the same for every retained quantity at the
    fixed point. The independent reference (`s0ref.ref_direction_table`)
    computes the table from this plan's text at the same state. Every table must
    match. The state at an elimination is the initial context minus the
    quantities logged before it, in log order. The table must also agree with
    the decision: the logged tip's label has status 'free' in both the closure's
    and the reference's table; every retained quantity's fixed-point table has
    no 'free' entry. Either failure is **VOID** (RC6).
  - **(ii) Directional propositions.** P_A-dir (P_G-dir under G) and the
    aggregate P_A and P_G, exactly as stated in §4 (N8), are checked on every
    survivor and on the planted retained sets. These are C3's families for A F,
    A B and G F (G outside the frame), each family minus its near tip in each of
    the six directions, and a Φ-adjacent family for each type: a family whose
    near tip in one direction is a Φ site-time, so that a fixed quantity is that
    tip's only other cover. Under G the analogue is a frame-adjacent family,
    whose near tip in one direction is in the frame and so ineligible. A failure
    is **MISMATCH** (RC7).
  - **(iii) Planted directional retention.** The frozen rule must retain every
    such family and every Φ- or frame-adjacent family (fixed members excepted),
    and must eliminate every family minus one near tip. A failure is **VOID**.
    The design evidence plants depths 1–4 for each type. RC7 places the
    retention of the Φ-adjacent families in C3; r4 places it here, as C11
    (iii), so that the over-elimination demonstration below can leave every
    other control green. This departure is recorded in `STAGE0-CHANGES-r4.md`.

  **Non-vacuity** (RC7). It is shown by two mutants fixed before the run:
  - a single-direction over-retention mutant: −y tips are treated as covered
    ("blind −y");
  - a single-direction over-elimination mutant: −y tips ignore cover by fixed
    quantities.

  Each must fail C11 and leave every other control green. The demonstration also
  states the survivor counts of the class it runs on. Where these are zero, it
  does not claim that "aggregate counts appear correct" beyond those counts. On
  the toy class both survivor counts are zero, so the claim reaches no further
  than the counts that do not depend on survivors (§9). The two decision-level
  mutants are run as well:
  - the decision ignores free −y tips while the table is truthful;
  - the decision treats −y tips covered only by fixed quantities as free while
    the table is truthful.

  So are the B-only and G-only −y blind mutants. Every one is required to be
  caught by its named C11 case.

  In Layer 2, C11 (i) runs on a deterministic sample of v8 records and on every
  survivor; C11 (ii) on every survivor; C11 (iii) and the direction mutants in
  pre-flight.
- **C12, frame.** The frame's even part equals B8, and every retained in-frame
  cone lies in the frame.

**Evidence and exactness**
- **C13, evidence** (§A.42, §A.44).
  - **Design evidence (now).** `s0run.py` retains every step's stdout and stderr in
    `stage0/design-r4/runs/`, with `RUN-MANIFEST.json` and `RUN-MANIFEST.md`:
    the commands, exit codes, `-O` identity, output SHA-256 values and code
    SHA-256 values. Every retained output is deterministic.
  - **Layer 2 (implementation).** Each shard writes a structured `shard-<s>.json`, in a stated
    schema, with:
    the parameter digest, the covered index ranges, per-record codes, counts,
    witnesses and its own SHA-256.
  - The merge reads only those files and the exit status. It checks exact
    coverage and disjointness, and writes `result.json`.
  - The package retains three things: `result.json`, which is the expected
    result; `expected-controls.json`, the controls' expected values; and the
    reproduce recipe in `REPORT.md`, with the commit, the commands and the
    comparison.
  - Normal and `-O` runs are byte-identical, per shard and merged.
- **C14, static checks.** No floating point, no file read, the standard library
  only, no author engine.
- **C15, exact elimination soundness** (review R1). The production closure is
  dimension-parametric. It is run on exhaustive 1D windows (2^21 worlds) and on
  small 2D windows (2^18 worlds), under A geometry and under G geometry with a
  toy frame. **Coverage:** 1D reaches F depth ≤ 3 and B depth ≤ 2. 2D covers one
  depth-1 quantity with its window, in effect the constraint block. 3D
  soundness at v8's depths rests on the uniform-in-dimension proof, C2 (to
  depth 23) and C18. For random subsets of a planted and native-analogue pool, the
  eliminated set must be exactly uniform and independent of the retained set,
  under L3 and under L3′, by integer counting.
  - Every rule mutant is also run through C15.
  - The wrong-far-tip mutant must fail C15.
  - The off-axis mutants need depth ≥ 2 in two or more dimensions, which is
    beyond these windows, so they are caught by C3.
- **C17, fixed point** (completeness). Using `s0ref`'s cone and tip code, no
  retained quantity of any record has a free eligible tip.
- **C18, elimination audit** (soundness). Every logged elimination is
  re-checked with `s0ref`: the tip is valid and eligible, and uncovered by every
  quantity alive at that moment.
- **Refusal** (RC9 a). The refusal is keyed on configuration content. Any setup
  whose (dim, n, ρ, t_last, port, sources) equal v8's is refused by `Context`,
  `num_records`, `record_at` and `record_samples`. `s0ref.ref_context` refuses
  v8's (dim, n, port). The native evaluator takes no configuration, only
  windows of pair cells. The check makes 13 attempts, every one of which must be
  refused: the V8 object (5 entry points); a freshly constructed copy of v8's
  setup (5 entry points); the V8 object with its flag flipped; and
  `ref_context` with v8's parameters under A and under G.
- **C16, minimal witness.** Witnesses are ordered by:
  1. k;
  2. the number of even-class context quantities;
  3. the lexicographic order of the sorted item tuples (site, then t).

  A self-test injects several MISMATCH records and must report the minimal one.

**Mutants (review R2).** Each control above, broken in turn, must give VOID and name
its target. A mutant counts only when it fails on its named case. Every rule
mutant is run under A and under G.

The named case of each mutant is the one `s0mutants.CASES` defines, the single
source of this table (N9): a (control, predicate) pair fixed before the run. A
mutant counts as killed only when the suite exits 2 with parseable output, the
named control fails, and the predicate holds on that control's output. Mutants
run only after the frozen suite passes (RC9 c). The observed failures of the r4
quick run (§9) are in brackets.

| mutant | named case | [observed failures] |
| --- | --- | --- |
| near-only tips | C3: block minus centre retained | [C3, C11 i] |
| off-axis tips (all types) | C2: an emitted tip is not bijective | [C2, C3, C11 i–iii] |
| off-axis tips, B type only (does not apply to G, which has no B type at depth ≥ 1) | C2: an emitted B-type tip is not bijective | [C2, C3, C11 i, iii] |
| wrong far tip | C15: exactness violation | [C2, C3, C7, C11 i–iii, C15, C18] |
| far cone deleted | C1: dependence outside the cone | [C1, C3, C11 i–iii, C15, C18] |
| radius −2 | C1: dependence outside the cone | [C1, C3, C11 i–iii, C15, C18] |
| radius +2 | C1: claimed radius not attained | [C1, C3, C6, C7, C11 i–iii, C17] |
| swapped slices | C1: cone mismatch | [C1, C2, C6, C11 i, ii, C18] |
| odd samples kept (E2) | C0: context differs from the reference | [C0, C7, C11 i, C17, C18] |
| un-applied elimination | C17: retained quantity with a free tip | [C3, C6, C7, C11 i–iii, C17] |
| blind −y (over-retention; non-vacuity) | C11 (i): table mismatch | [C11 i–iii only] |
| −y tips ignore fixed covers (over-elimination; non-vacuity) | C11 (iii): Φ-adjacent family eliminated | [C11 i, iii only] |
| decision ignores free −y tips (table truthful) | C11 (i): decision inconsistent with table | [C11 i–iii] |
| decision treats fixed-only-covered −y tips as free (table truthful) | C11 (i): decision inconsistent with table | [C11 i, iii] |
| blind −y, B type only | C11 (ii): P_A-dir violation on a B planted set | [C11 i–iii] |
| blind −y, G only | C11 (ii): P_G-dir violation on a G planted set | [C11 i–iii] |
| skip record | C13: coverage and recount | [detected] |

Two mutants are removed as equivalent on even-class contexts, by PO1:
- **"parity filter dropped"** fails no control.
- **"symmetric (parity-blind) radii"** fails no closure-level control. C1's
  radius-attainment check detects it at the definition level only.

Both runs are retained as evidence of the equivalence.

## 7. Invariant → checkpoint

| invariant asserted | checkpoint |
| --- | --- |
| the configuration space and its counts are the frozen ones | C0 |
| the group is C4v, with correct orbit counts | C0 |
| orbit representatives preserve every reported count (the closed list of §6 C8: 52 counts on the toy class) and per-record results for C4v-invariant attributes | C8 (count preservation, equivariance; RC10) |
| source-dependent attributes are per record | C8 |
| production cones match the native rule, at A F 0–15, B 0–8 and G 0–23 at both pairs (interior sampled beyond depth 8) | C1 |
| production tips are bijective, near and far, at the same depths; off-axis cells are not | C2 |
| planted families survive at A F 1–15, B 1–8 and G F 1–23; planted non-survivors collapse | C3 |
| elimination is exact: the eliminated set is jointly uniform and independent of the retained set (independent native code) | C15 |
| every logged elimination is justified by the frozen rule (independent reference code) | C18 |
| every required elimination is applied (completeness) | C17, C7, the un-applied-elimination mutant |
| every eligible configuration is considered (completeness) | C13 manifest and recount, the skip-record mutant |
| planted survivors and planted non-survivors are separated (non-vacuity), including B-type, G and Φ-adjacent families | C3, C6, C11 (iii) |
| S6: PO8 holds on the 21-bit reference structure, with a positive and a negative control | `s0s6.py` |
| v8's class is not run without authorization, and the refusal is keyed on content (a fresh copy, a flipped flag and `ref_context` are refused) | the refusal check (13 attempts); Layer-2 certificate item 6 (RC9 a) |
| the frozen code and configuration are the ones run | Layer-2 certificate items 1–3 (§5b) |
| no over-elimination in any convention, type or depth | C3, C15, the mutant campaign |
| far tips are load-bearing beyond L3 | C3 (centre removed), the near-only mutant |
| the closure is computed correctly, by independent code | C6, C7 |
| the base context is collapsed (label precondition) | C6, S10, BASE_RESIDUE |
| monotonicity of rules and records | C9 |
| no fixed quantity is eliminated | code invariant (C10 i); cannot fail by construction |
| the port samples are in-frame under G | C10 (ii) |
| the closure's per-direction tables match the specification in every direction, and every decision agrees with its table, at every elimination and at the fixed point | C11 (i): required, VOID on failure (RC6) |
| retained sets satisfy P_A-dir and P_G-dir (and the aggregate P_A and P_G, as stated) | C11 (ii): required, MISMATCH on failure; on B-type, G and Φ-adjacent planted sets (RC7); design-evidence code now, Layer-2 code on v8 survivors |
| planted families, including Φ- and frame-adjacent ones, are retained, and families minus one near tip are eliminated | C11 (iii): required, VOID on failure |
| the per-direction control detects single-direction errors of both kinds | the over-retention (blind −y) and over-elimination (−y ignores fixed covers) mutants, each failing C11 only; and the decision-level, B-only and G-only mutants, each killed at its named C11 case (RC7) |
| every proof-dependent rule rests on a complete statement | §4: the PO table, and the PO references on P_A, P_A-dir, P_G, P_G-dir, C_A, C_G, the MISMATCH bullets and RESIDUE_UNLINKED (RC2, O-c) |
| the frame is B8, and in-frame cones stay inside it | C12 |
| the design evidence is retained and deterministic | C13 (design evidence): `runs/`, RUN-MANIFEST, `-O` identity |
| the Layer-2 evidence is structured, complete and retained | C13 (Layer 2), certificate items 5, 7 and 8 (§5b) |
| integer-only; no repository read | C14 |
| the minimal witness is well defined | C16 |
| the distinguishability classes (a)–(c) | §3 definitions, C8 (invariant parts), C7 (on survivors) |
| the design evidence used the intended parity | §9, rerun at L = 4 with Φ even |
| the rule mutants are not equivalent | the mutant table; the two equivalent mutants removed by PO1 |
| every control can fail | the mutant campaign |

## 8. Comparison with known results (before any novelty statement)

The report reads the following and states which parts of L2, L3′, P_A and P_G
are known. All are from memory and to be checked (S9):
- **One-time pad.** Shannon (1949).
- **Secret sharing and access structures.** Shamir (1979); Blakley (1979); Ito,
  Saito and Nishizeki (1987); and, optionally, Brickell and Davenport (1991) on
  ideal secret sharing and matroids.
- **Secret sharing with reversible memory cellular automata.** Martín del Rey,
  Pereira Mateus and Rodríguez Sánchez, *Appl. Math. Comput.* 170 (2005).
- **Permutive cellular automata.** Hedlund (1969); Shereshevsky; Boyle and Lind
  (1997).
- **Uniform-measure preservation.**
  - In one dimension: Hedlund (1969); Coven and Paul (1974).
  - In d dimensions: Moore (1962) and Myhill (1963), the Garden-of-Eden theorem,
    and Maruoka and Kimura (1976).
- **Higher-dimensional reversibility and surjectivity.** Kari (2005), "Theory of
  cellular automata: a survey".
- **Bipermutive cellular automata and dual-unitary circuits.** Bertini, Kos and
  Prosen, *Phys. Rev. Lett.* 123, 210601 (2019), and later classical and
  dual-unitary work. There correlations survive only on light-cone edges. It is
  the nearest known structure to "survivors only in light-like, axis-aligned
  ties", and the residue must be compared with it.
- **Cryptography with cellular automata.** Wolfram (1986).
- **Second-order reversible cellular automata.** Margolus (1984); Toffoli and
  Margolus (1987).
- **Light-cone counting.** OEIS A001845.

Coincident statements are cited, not claimed. The result specific to v8's
geometry is stated as a geometric fact on the consistency axis.

## 9. Design evidence (owner-approved; toys, planted sets and small windows only)

Nothing here ran on v8's configuration class. The r4 code is in `stage0/code-r4/`.
Its evidence is in `stage0/design-r4/`: every step's stdout and stderr in `runs/`,
and `RUN-MANIFEST.json` and `RUN-MANIFEST.md` with the commands, exit codes, `-O`
identity and SHA-256 values. Everything ran with `python3 -I -B` on Python 3.13.16.
The design evidence of r1–r3 is unchanged in its own directories and is summarized
in `STAGE0-PLAN-r3.md` §9; the four r2 toy scripts are re-run here. The toy setup is
3D, n = 2, region ball(1), last slice 6, port (0, 0, −2): 1,400 records in 488 C4v
orbits.

**r4 runs.**
- **Exits and determinism.** Every step exits 0. The control suite, S6, the
  sym-check and the four toy scripts are byte-identical under `-O`.
- **Not run locally.** The full mutant campaign is not run here; under §A.40 it
  runs in CI (RC9 d). The quick campaign took 845 s.
- **Cones and tips.**
  - C1: 301,640 perturbations, none outside the cone, every radius attained.
  - C2: 541 tips, all bijective; 39 off-axis contrasts.
- **Planted families.**
  - C3: every family retained at A F 1–15, B 1–8 and G F 1–23; every family minus
    its +x tip collapses.
  - Constraint block: 8 retained, and 0 once its centre is removed.
- **Reference agreement.** C7: 0 differences over 1,400 records × 2 conventions.
- **Symmetry.** C8: all 52 counts of the closed list compared, 0 mismatches,
  0 equivariance violations.
- **C10 (ii):** both toy port samples are in-frame.
- **C11.**
  - (i): 16,835 tables, 0 mismatches, 0 decision–table inconsistencies.
  - (iii): 96 planted sets, including 12 Φ- or frame-adjacent families, 0 failures.
  - (ii): 24 retained planted sets, 0 P_A-dir, P_G-dir, P_A or P_G violations.
- **Exactness and completeness.**
  - C15: 0 violations on 1D (2^21 worlds) and 2D (2^18).
  - C17 and C18: 0.
- **Refusal:** all 13 attempts refused.
- **S6:** "proof-check of PO8; not a result"; 0 target-law classes in all 22
  subsets; the positive and negative controls behave as stated.
- **Sym-check:** C0's v8 combinatorics, unchanged.
- **Mutant campaign (quick).**
  - The frozen suite is clean, and only then do mutants run.
  - All 16 mutants are killed at their named cases (the §6 table).
  - The equivalent mutants behave as stated: parity-dropped fails nothing;
    symmetric-blind fails only C1.
  - Non-vacuity: the over-retention mutant (blind −y) fails C11 (i)–(iii) and
    nothing else. The over-elimination mutant (−y tips ignore fixed covers) fails
    C11 (i) and (iii) and nothing else.
  - The two decision-level mutants (table truthful) are killed by C11 (i)'s
    decision–table check. The B-only and G-only blind mutants are killed by
    C11 (ii) on the B and G planted sets.

**Disclosure of the demonstrations' limits (RC7; owner requirement).**
- **The toy class has no survivors** under A or G. 30 of the 52 reported counts
  are identically zero on it:
  - every survivor-conditioned count;
  - the L3/L3′ disagreements;
  - the port-site degeneracy, because the toy region ball(1) does not contain the
    toy port site (0, 0, −2) (N7; not so on v8, where (0, 0, −3) ∈ ball(4));
  - G's source-cell count.

  The other 22 depend only on in-clear sets, truncated sets and record geometry,
  so no over-eliminating mutant can change them on this class.
- **"Reported counts identical to the frozen rule's"** is therefore weak
  evidence here. The demonstration rests on C11's own cases, not on the counts.
- **r3's demonstration was narrower than presented.**
  - It used one over-retention mutant (blind −y).
  - Its table check overrode exactly the field that C11 (i) compares.
  - Its proposition check depended on the planted "family minus −y tip".
  - It ran on a class with no survivors, where 24 of 44 counts were identically
    zero.
  - It tested neither over-elimination nor decision-level errors. The r3
    re-check's mutant `rv_decide_ignore_fixed_y` passed every r3 control.

  r4 adds the cases that catch these: decision–table consistency (C11 i), the
  Φ-adjacent families (C11 iii), and the B and G planted sets (C11 ii, iii).
- **These outcomes validate the machinery only.** They say nothing about v8's
  class.

## 10. Resources and launch

v8 contexts have at most 37 quantities. The prototype estimate is about 3.5 ms
per L3′ closure, which gives roughly 5–10 CPU-hours per (convention, rule)
pair over 5,163,225 records. Orbit representatives (S4) reduce this by about
6.3×. C7, C8, C15 and the mutants add a bounded fraction. The global closure
bound (S1a) is a handful of closures of about 1,600 quantities each.

The run is sharded in CI (S7). A dry run prints the shard plan without
computing any closure.

Launching the enumeration, adding the workflow and every dispatch need owner
approval (§A.43 item 4). The r3 design evidence was run locally as executor
evidence: controls about 2 minutes, the quick mutant campaign about 10, the full
about 33. Under §A.40, the Layer-2 mutant campaign and any repeated suite run in
CI (RC9 d). r4 ran locally only the cheap controls and the quick campaign. The Layer-2
enumeration runs in CI. Retention follows C13.

## 11. Coverage limits (stated in every output)

- k ≤ 2 stream items; v8's region and slices; the scaled control.
- One port; no later reads, unless S3 extends them.
- Conventions A and G, with the declared frame.
- L3′ and L3 only; survivors are not shown to be informative.
- No law computed, apart from the S6 proof-check on Φ's reference structure.
- Nothing at actual L; no A1/A2 statement; no claim about OI beyond the class.

## 12. Owner decisions and remaining open items

**Decided (2026-10-26):**
- **S1:** k ≤ 2.
  - **S1a,** the global closure bound, is included: the closures under A and G
    of the union of all items' samples, which is the C9 bound, and the closures of
    the items on every axis-parallel line meeting Reg (41 lines per axis, 123 in
    all). The per-line closures are reported only (N5).
  - **S1b and S1c** are deferred. Taking either up is decided by rule T below,
    fixed before any S1a result is read (owner decision O-b), and never merely
    on available resources.

**Rule T, the S1b/S1c trigger** (O-b, approved in principle; preregistered before
any S1 result). Its inputs are objective counts from S1a only:
- L_A, the number of non-fixed quantities in the global bound under A whose cone
  contains a Φ cell;
- L_G, the number of quantities in the global bound under G with a seed tip whose
  cone contains a source cell.

The rule is:
- **L_A = 0 and L_G = 0.** By PO4 (monotonicity) and PO6, no record of any size
  can have a linked survivor. S1b and S1c are not undertaken. The report states
  the k-independent consequence.
- **L_A > 0 or L_G > 0.** S1b (the minimal self-supporting record search, m ≤ 4,
  restricted to the global bound) is put to the owner as a new preregistration.
  S1c is taken up only if S1b's own preregistered rule calls for it.
- **In either case,** if the dry-run cost estimate exceeds S7's budget, the
  search is reported as not undertaken for cost.
- **Neutrality.** The rule fires on L_A and L_G only. It does not depend on the
  k ≤ 2 label (COLLAPSE_ALL, RESIDUE_UNLINKED, RESIDUE or BASE_RESIDUE), on
  whether any survivor appears, or on which direction any result points. In
  every case the outcome of the rule is reported.
- **S4:** orbit representatives, with R5 and the count-preservation check (C8).
- **S6:** approved as a labelled proof-check, and run (§9).
- **S9:** every work in §8 is checked first-hand before any novelty claim.
- **Review R1–R9, re-check R1–R6 and RC1–RC10:** applied (N2).
- **O-a to O-d (r3 re-check):** approved; see the header and rule T.

- **O1, approved:** the two-layer freeze (§5b). Layer 1 is the scientific
  specification. Layer 2 is the implementation, finalized and frozen only after
  Layer 1 passes independent review. "Complete enumeration code now: No; defer
  until the design layer is frozen."
- **S11, adopted:** P_A-dir is a required control, not a diagnostic. "It must
  detect incorrect elimination in individual directions even when aggregate
  counts appear correct." It is C11 (§6).
- **The v8 enumeration is not authorized.**

**Open, at their proposed values** (the re-check recommends accepting each):
- **S2.** L3′ for the labels, with L3 reported beside it.
- **S3.** Π_R contexts only. F2 contexts, and item (iii), only for survivors, if
  extended.
- **S5.** C7 sampling: 1 in 1,000, plus every survivor and every tie.
- **S7.** CI budget: 24 runner-hours over at most 32 shards, with a stop rule.
- **S8.** Location `native_predicate_avg_v9/stage0/`, under O6's base rule.
- **S10.** The base context is a precondition (R8), hand-derived in C6.

**Freeze (owner step 4, O1).** The Layer-1 freeze records this plan's SHA-256
as the scientific specification. The design-evidence code is not frozen.
Layer 2 is finalized after Layer 1's independent review, then reviewed itself,
and frozen with its code and configuration hashes and its execution
certificate before any launch authorization. That means the production
enumerator, the controls and the certificate (§5b). A change to any frozen item
is a new revision.

The decisions O3–O9 of `PLAN-r2.md` concern Stage 1 and are unchanged.
