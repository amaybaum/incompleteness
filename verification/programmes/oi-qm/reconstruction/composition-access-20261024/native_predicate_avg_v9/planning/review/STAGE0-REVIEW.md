# Review: NP-AVG-1 Stage 0 plan (`draft/STAGE0-PLAN.md`, `STAGE0-NOTES.md`)

**Reviewed objects.**
- `draft/STAGE0-PLAN.md` (475 lines) and `draft/STAGE0-NOTES.md` (122 lines).
- The design controls in `stage0-design/`, read in full: `sym_check`, `toy_closure`, `toy_block`
  and `toy_fartip`, scripts and outputs.

**Basis.** v8's rule, `native_predicate_v8/checks.py:191-204`: x_t = x_{t−2} ⊕ H(⊕_e x_{t−1}(·+e)),
where H is a permutation.

**Read-only.** Nothing was run on v8's class. The new reviewer toys are in `review/toy0/`. They
use the 1D analogue of v8's rule and the drafter's toy geometry:
- `l3prime_1d.py`: exact, exhaustive over 2^21 worlds;
- `parity_mutant.py`, `parity_mutant2.py`;
- `toy_rerun.py`.

## Verdict: ACCEPT WITH CHANGES

The configuration space, equivalences, propositions and decision rule are sound, and L3′ is
correct. The changes below fix three things:
- controls that cannot detect the error direction §A.31 cares about, which is over-elimination,
  favourable to collapse;
- one equivalent mutant;
- one source-dependent attribute that breaks the symmetry control.

## Findings

### 1. L3′ is sound for v8's rule (priority 1)

**The proof.** Take a quantity q at depth d ≥ 1 after the later slice L of the pair (E, L), and
its far-slice axis extreme u = c + (d−1)e on slice E. In the rule, x_E(u) is the t−2 term of
x_{L+1}(u) = x_E(u) ⊕ H(⊕ x_L(u±e′)), and of nothing else at slices L+1 and later.

Fix every pair variable except x_E(u). Then:
- slice L is fixed, and so is slice L+1 everywhere except at u;
- x_{L+1}(u) is a bijection of x_E(u);
- in the shifted pair (L, L+1), x_{L+1}(u) is q's near axis tip at distance d−1, so q is a
  bijection of it (the near-tip unique-path argument, PO2).

The composition is a bijection, and d = 1 (u = c) is included. The backward case is the mirror
image (x_{E−1}(u) = x_L(u) ⊕ H(⊕ x_E(u±e′))). The elimination step and its induction are the
same as for near tips, so the eliminated set is jointly independent of the retained set.

**Toy checks.**
- *Exact soundness* (`toy0/l3prime_1d.py`). The check uses the 1D analogue of the rule and an
  exhaustive 2^21-world window. Over 250 random subsets of a 16-quantity pool, with F and B types
  and depths 0–3, the eliminated set is *exactly* jointly uniform and independent of the retained
  set under L3 (0 violations) and under L3′ (0 violations).
- *Countercontrol.* A deliberately wrong far-tip rule (distance d, outside the cone) is caught in
  21 of 250 trials, so the test can fail.
- *Separation.* L3′ ⊆ L3 in all 250 trials. On {(1,3), (−1,1), (3,1)}, L3 keeps all three and L3′
  eliminates all three, and the exact law confirms that they are independent.

L3′ is therefore not a source of favourable bias. The genuine risks in that direction are in
implementation (findings 3–4).

### 2. Propositions, corollaries and the MISMATCH rule (priority 2)

**P_A and P_G are correct necessary conditions, as stated.**
- PO3 holds. An F near tip at reach r lies in a B cone only if the B reach is at least r+1, since
  B's slice-8 radius is d−1. The mirror case holds too, and a same-type cover forces equal reach
  and the same tip.
- PO5 holds. A non-fixed quantity's aligned near tip has norm |c|+d ≥ 1 on slice 8, so it is not
  V. On slice 7 it equals a Φ site only for Φ members or p.
- **PO7 is exactly right, which closes the gap I left open in RECHECK §1.3.** The even part of
  the frame is B8: the even port samples N[1], N[3] and N[5] have cones inside B8, and N[6] is
  odd. Tips in B8 imply |c|+t ≤ 8, so the whole cone lies in the frame.

**But P_A is weaker than the re-check's argument.** It constrains only the ρ-maximal element. The
re-check's form, "in every direction, the extremes of the dominant type are tied", gives more
power to C11. Optional change O-c.

**COLLAPSE_ALL's text inverts the evidence** (STAGE0-PLAN:247-253).
- Collapse is established by the *exact closure computation*, under its controls.
- C_A and C_G turn collapse into law failure, and they are proofs.
- P_A and P_G play no part in deriving COLLAPSE_ALL: they constrain survivors, and survivors are
  absent in that case.

Required: R7.

**C11 and MISMATCH genuinely check code against proof**, since the code does not encode P_A. But
they only examine *survivors*. Over-elimination produces fewer survivors and is invisible to every
MISMATCH bullet except C6's hand instances. MISMATCH is a guard against over-retention, not
against collapse bias. Making it the latter needs finding 3's controls.

### 3. Controls and mutants (priority 3)

**The planted off-axis set is not sufficient alone.** The drafter's observation stands:
- the mutant differs on 0 of 400 random toy sets;
- random sets almost never cover all six axis tips while leaving an off-axis cell free.

One planted A-geometry, F-type, depth-2 set catches *that* mutant. Over-elimination bugs confined
to one class (B type, G convention, a given depth, the far tips only) would pass. Required: R1, R2
and R3.

**C1 and C2 must exercise the production code.** C2 must test the production `tips()` output, and
C1 the production `in_cone()`, against the native evaluator. Testing a separately written
definition checks the lemma, not the code.

**C7's second closure must not share them.** It needs its own cone and tip code, written from the
plan's text; otherwise a definitional error is common-mode.

**C3 under G is vacuous unless its plants lie outside B8.** Inside B8 every tip is ineligible, so
everything is retained trivially.

**"Parity filter dropped" is an equivalent mutant on v8's contexts.**
- With the Φ analogue in the pool's parity class, as in v8 where all fixed quantities and records
  are even, dropping the cone parity test changes the closure in **0 of 400** sets (`parity_mutant2.py`,
  L = 2 and L = 4). This is PO1 ("parity automatic in the even class").
- No control can catch it, so the campaign cannot pass as written.
- Replace it with the E2 mutant (odd samples kept), which C0's context sizes catch.

**The design toys run with Φ in the wrong parity class.**
- `toy_closure.py` and `toy_fartip.py` use L = 3. Their Φ analogue (slices 2–3, |c| = 1 and 0) and
  p analogue are *odd*, while the pool is even. In those runs Φ never covers a pool tip, so "0
  self-supporting sets with Φ" was measured with Φ inert.
- That parity mismatch is also the only reason the parity mutant showed differences (33 of 400
  at L = 3).
- My re-run at L = 4, with Φ even (`toy_rerun.py`): still 0 self-supporting sets of size 1–3 under
  L3 and under L3′, in a 67-quantity pool.

So the toy conclusion holds, but the recorded design evidence must be re-run at the correct parity
(R4).

**The other controls can fail.** C0, C5, C6 (with the hand derivation before reading the computed
values: good), C9, C10, C12, C13 and C14, and the swapped-slices mutant, which C1 catches.

**C8 conflicts with G-linkage.** The sources (−7,0,±1) and (−8,0,0) are not C4v-invariant, so
"G-linked" (cones of S_G contain a source) can differ within an orbit. C8 would then VOID a correct
run, and S4's orbit representatives would mislabel G-linkage. Required: R5.

### 4. Survivor classification and degeneracies (priority 4)

**"Observer interface"** (STAGE0-PLAN:145-147) is close to vacuous as written. Under A every
non-fixed retained quantity is public by construction (record or port samples), and under G the
same holds. It does not express the owner's "distinguishability under the permitted observer
interface". A geometry-only version is needed (R6):
- **(a) Observer-equivalence classes.** Group records by the post-closure retained *public* set. Two
  records in one class are indistinguishable to the observer at the masking level. Count the
  classes overall and among survivors.
- **(b) Private dependence set.** For each survivor, list the Φ cells, separated into J cells
  (q8, q10) and others, and, under G, the source cells, inside the cones of its retained public
  part.
- **(c) A stated limit.** Linkage is *necessary, not sufficient*, for distinguishing carrier
  states. Distinguishability itself is a law question for Stage 1.

**No degeneracy is excluded.** E1–E3 are equivalences that are counted, and odd samples are inert
by L1. One gap remains, a label precondition: the decision labels assume the base context is
collapsed. If it is not, every record is a "linked survivor" and RESIDUE becomes trivial. By hand
it is collapsed:
- N[1] has the largest reach on a single site and goes first;
- N[3] follows;
- N[5]'s +z tip is q8, which Φ covers, but its other tips are free, so it goes too.

Make "base collapsed" a stated precondition, or define survivors relative to the base (R8).

### 5. Open items S1–S10 (priority 5)

**S6 needs owner approval and is not necessary.**
- PO8 has a three-case written proof (RECHECK §1.2), and the conclusion of C_A rests on it.
- S6 is a law computation, but on the 21-bit reference structure of Φ, not on any native record of
  the class. It is cheap: 22 subsets over 2^21 worlds.
- It is not needed for soundness. Its value is an independent mechanical check of the lemma that
  converts COLLAPSE_ALL into "Law_A fails".
- Recommendation: the owner approves it as a separately labelled proof-check. Failing that, PO8
  gets a named second reader.

**The other items:**
- S1a: include it. Expect a large bound, because constraint blocks with their centres survive
  L3′.
- S1b and S1c: separate approval.
- S2: accept.
- S4: accept, subject to R5.
- S5: accept.
- S7: accept.
- S9: see finding 6.
- S10: accept, as R8's precondition.

### 6. Literature (priority 6; from memory, unverified)

Omissions worth checking before any novelty statement:
- **Moore (1962) and Myhill (1963), the Garden-of-Eden theorem; Maruoka and Kimura (1976).**
  Surjectivity and balance, and uniform-measure preservation, in *d* dimensions. This is the 3D
  context of L2; Hedlund and Coven–Paul are 1D.
- **Bipermutive cellular automata and the dual-unitary analogy.** Bertini, Kos and Prosen,
  *Phys. Rev. Lett.* 123, 210601 (2019), and the later classical and dual-unitary work. There,
  correlations survive only on light-cone edges. That is the known structure nearest to "survivors
  only in light-like axis-aligned ties", and the residue must be compared with it.
- **Wolfram (1986), "Cryptography with cellular automata".** Cellular-automaton dynamics as a
  masking or keystream source.
- **Kari (2005), "Theory of cellular automata: a survey".** Reversibility and surjectivity in
  higher dimensions.
- *Optional:* Brickell and Davenport (1991), on ideal secret sharing and matroids, for the
  "access structure" vocabulary of the residue.

### 7. The §A.41 table (priority 7)

Rows missing or mis-assigned:
- **"Elimination is exact (eliminated ⊥ retained)".** No computational checkpoint exists; C2 tests
  bijection only. Add R1's C15.
- **"Orbit representatives give per-record results".** True only for C4v-invariant attributes; the
  checkpoint is R5.
- **"The base context is collapsed".** Checked by C6 and S10, and a precondition of the labels (R8).
- **"The design-control evidence used the intended parity".** R4.
- **"The rule mutants are not equivalent".** R2.
- **"Distinguishability classification".** R6.
- **"Minimal witness" in MISMATCH.** Define the order (k, then context size, then canonical
  index), with a checkpoint.
- **§A.42 retention of the expected-result file and the reproduce recipe.** Name them in C13.

## Required changes before freeze

- **R1. Add C15, exact elimination soundness.** The production closure is dimension-parametric. On
  exhaustive 1D windows (about 2^21 worlds) and a small 2D window, the eliminated set must be
  exactly uniform and independent of the retained set, under L3 and under L3′. A wrong far-tip
  mutant, using distance d, must fail (it failed in 21 of 250 in `toy0/l3prime_1d.py`).
- **R2. Mutant list.**
  - Remove the equivalent parity-filter mutant, or replace it with "odd samples kept", which C0
    catches.
  - Add the wrong-far-tip mutant (C15) and a B-type-only off-axis mutant.
  - Run every rule mutant under A and under G.
- **R3. Make C3 and C4 a planted family.** For every convention, type and depth used, plant
  {q} ∪ all of q's near and far axis tips as depth-0 quantities.
  - The correct rule must retain the whole family, and the off-axis mutant must eliminate it.
  - Under G, plant outside B8.
  - C1 and C2 test the production `in_cone` and `tips`; C7 is written with its own cone and tip
    code.
- **R4. Re-run the design toys with Φ in the pool's parity class** (L even), record the corrected
  outputs and SHA-256 values in STAGE0-NOTES, and state the earlier parity mismatch.
- **R5. C8 checks C4v-invariant attributes only.** G-linkage, and any source-dependent attribute,
  is computed per record, never transferred from an orbit representative.
- **R6. Replace the "observer interface" bullet** with finding 4's (a)–(c).
- **R7. Reword COLLAPSE_ALL** (247-253): "by the exact closure computation (controls C0–C15 green)
  and the proved corollaries C_A and C_G". P_A and P_G stay as survivor checks (C11).
- **R8. Make "base context collapsed" a stated precondition of every label**, hand-derived in C6
  before the computed value is read. Otherwise label relative to the base.
- **R9. Complete the §A.41 table** per finding 7, including the definition of the minimal witness.

## Owner decisions

- **S6.** Not necessary. Recommend approving it as a labelled proof-check on the reference
  structure, with no native law computed. Otherwise PO8 gets a named second reader.
- **S1a.** Include. **S1b and S1c:** separate approvals, after S1a is seen.
- **S4.** Accept orbit representatives, with R5.
- **S9.** Add the finding-6 references to the list to check.
- **Optional, O-c.** Have C11 also check the per-direction form of P_A.
- **Launch.** The full enumeration stays unauthorized until a separate owner approval, as the plan
  states (STAGE0-PLAN:23, 420-422). With the changes above made, the plan is ready to be frozen and
  then launched.
