# EQ2-B running notes — Theorem A′ (two-system classification, group form)

Design only. Base: certified main `bcbc516f`, read-only at `scratchpad/eq/base/` (integrity: `sha256sum -c
../base.manifest.sha256` exit 0, 1317 files, at the start of the thread). Writes only under `scratchpad/eq2/B/`.
No git write, no Lean, no CI, no agents. Lean text is UNBUILT. Exact arithmetic only for anything certified.

Mathlib reference: the pin is `rev = "v4.33.0"` in `verification/lean-mathlib/lakefile.toml` at the base (there is
no `lake-manifest.json` at the base: `git ls-tree bcbc516f verification/lean-mathlib/` lists only `OIBridge/`,
`OIBridge.lean`, `lakefile.toml`, `lean-toolchain`). A Mathlib source tree at exactly that tag exists read-only at
`scratchpad/ml-v433-src/m` (`git describe --tags` → `v4.33.0`, commit `db584cd6`, its `lean-toolchain`
`leanprover/lean4:v4.33.0`). Mathlib presence/absence claims below are greps of that tree, with the terms recorded.

## 0. Productivity test (fixed before any probe; AGENTS.md §A.31)

A finding is a **gem** iff BOTH:
1. it is strictly stronger than the restatements already in the inputs (read first):
   - EQ-C Theorem A and the v1 §5.1 steps a–g (written, exact ingredients);
   - INTEGRATION-DESIGN v2 §4 (Lemma COMPACT, Theorem A′ as "step e establishes more");
   - K2C U (cone uniqueness for `cnot` + exact SO(3)², Schmidt + spectral, no Lie theory);
   - k2d T6/T7 (finite native group interval; composition proposal);
2. AND it either
   - (i) decides one of the B-items by an exact countermodel or a theorem route whose computational ingredients
     are exact: B3(ii) (do all admissible entangling native gates at d = 3 reduce to `cnot`?), B4 (what Theorem A′
     needs in the countable regime), the route choice; or
   - (ii) exposes a hidden assumption of Theorem A′ / Lemma COMPACT / the formal route; or
   - (iii) removes a Lie-theoretic import from the formal route, replacing it by a kernel identifier at the base or
     by a Mathlib declaration verified present at the pin.

Below that bar: record-only (ELABORATING / CONFIRMING). Favourable branches get a countercontrol (§A.21, §A.31).

## 0.1 Decision rules (preregistered as rules, not expected numbers)

- **R1 (converse first).** A hypothesis is reported compatible with QM only if `Q3` with `cnot` and the local group
  satisfies it by an exact check or a cited standard fact. If `Q3` fails it, the verdict is INCOMPATIBLE.
- **R2 (foils).** Each hypothesis of Theorem A′ gets a foil that satisfies the other hypotheses and fails the
  conclusion (or makes the hypotheses inconsistent), exact where possible, written and labelled otherwise.
- **R3 (classification).** A solution-space dimension is reported only if an exact rational-rank upper bound equals an
  explicit lower bound verified symbolically for all parameters. Controls: `cnot` and its local equivalents lie in the
  family. Countercontrol: dropping one constraint family gives a strictly larger space with a member that violates
  positivity at an explicit exact point.
- **R4 (positivity).** Positivity is claimed only through exact values at explicit points (negative witnesses) or by
  inheritance from a landed positivity theorem through an exact identity. Random sampling certifies nothing.
- **R5 (Mathlib).** Present/absent only from greps of the pinned tree, terms recorded; otherwise "unverified".
- **R6 (kernel).** "Kernel-proved" only with a landed identifier, `file:line` at the base.
- **R7 (verdicts).** A script prints its VERDICT line only when every check passed (controls included); otherwise
  "VERDICT NOT RENDERED".

## 1. Node plan (depth-first; decisive branch first)

- **N1 (decisive for the route choice): B3(ii).** Classify the native, field-neutral class of `CtrlGate`s at d = 3
  (frame, two-sided positivity, `relC`, `IsNot`, normalization), and decide whether each reduces to `cnot` up to local
  maps and admissible symmetries. Then the cone-compatible subclass (orientation classes).
- N2: Lemma COMPACT with explicit hypotheses; its route through IIP-1; the normalization countermodels.
- N3: the general (non-`CtrlGate`) gate case and the continuous case: what Lie glue is really needed; whether a
  Mathlib-supported substitute exists.
- N4: IE₁ accounting — `driveWords3`, the countable regime, the finite-group regime.
- N5: the other hypotheses (convexity, upper bound, local premise, entangling clause), purification, self-duality.
- N6: converse and foils.
- N7: formalization strategy.

## 2. Node log

### N1 — B3(ii): the native class of control gates at d = 3 (`b1_native_class.py`)

**Run 1 (kept: `b1_native_class.run1.py/.out/.err`): 17/20, VERDICT NOT RENDERED.** Checks C.0–C.2 failed. Cause:
a harness error in the symbolic builder `sym_gate`, which added `fam(e_k)` (corner columns included) once per
parameter instead of `fam(e_k) − fam(0)`. The printed test values (`a*e0 + a2*e0 + … + e0`) showed the corner
columns counted five times. Fixed in one function (diff recorded by keeping the run-1 script; the reconstructed
run-1 script reproduces the run-1 output byte for byte). Nothing else changed; the decision rule is unchanged.

**Run 2: 20/20, VERDICT NATIVE-CLASS.**
- Reduction (written, from landed lemmas): corner slices `gate_corner_ctrl` (RSB:60), `gate_corner_neg_ctrl` (RSB:99);
  with `u∘G = u`, `M₀ = Mfwd z G = 1 ⊕ O` with `O ∈ O(3)`, `Oz = z` (first row of `M₀` is `e₀ᵀ` by normalization;
  `|Oy| ≤ 1` on the ball from posFwd at `hom z ⊗ hom y`, the same for `O⁻¹` from posInv via `lor_Minv_ctrl` RSB:87).
  Parity `finrank_plus_eq_finrank_minus_relC` (RelcSelectParity:329) makes `N` a π-rotation about `u₀ ⊥ z`; a
  rotation moves `(z, u₀)` to `(z3, e_x)`.
- Tangent block: relC (C1), corner orthogonality `gt_tangent_corners_ctrl` (RSB:129, C2) and the landed tightness
  `gt_sphere_ctrl` (RSB:162, C3) leave **exactly 4** parameters (exact rank, 18 rational targets) and the four
  directions satisfy C3 and its −z analogue C4 identically on the sphere. **C4 is redundant** given C1 (dimensions:
  C1+C2+C3 = 4, C1+C2 = 32, no relC = 8, no corner orthogonality = 8).
- Two-sided positivity: exact symbolic values `(e₀ + a e₁)(f₀ + f₁)`, `e₀ + a₂e₂`, `e₀ + b₂e₂`, `e₀ + b₁e₁` at four
  product points, and the inverse family `F(1/a, 1/a₂, −1/b₂, −1/b₁)`, force `a, a₂, b₁, b₂ ∈ {±1}`.
- Of the 16 sign patterns, the 8 with `a b₁ + a₂ b₂ = 0` are each `(actC D₁ actT D₂) cnot (actC D₃ actT D₄)` with
  diagonal sign matrices (exact identities); the other 8 fail posFwd with value −46/125 at `x = (3/5, 4/5, 0)`,
  `y = e_y` (exact).
- Consequence: **every `CtrlGate` at d = 3 with `u∘G = u` is `ℓ₁ ∘ cnot ∘ ℓ₂`, `ℓᵢ` local O(3)×O(3).** Entangling is
  automatic at d = 3 (E.1). Countercontrols: without the tightness rows the space is 32-dimensional and a fixed member
  violates posFwd (value −4/5); without relC it is 8-dimensional.
- Pressure test pending (next script): an independent gate from EQ-E's QM family through the classification, and
  the orientation classes against an invariant cone.

### N1 continued — orientation classes and cone compatibility (`b2_orientation.py`)

**Run 1 (kept: `b2_orientation.run1.py/.out/.err`): 16/17, VERDICT NOT RENDERED.** Check B.5 used the effect vectors
of sharp(+e₁), sharp(+e₃) instead of K2Guard's sharp(−e₁) ⊗ sharp(−e₃) (`sharpVec ![-1,0,0] = ![1/2,-1/2,0,0]`),
giving +1/2. Harness error (B.4's own search had found the right effects, value −1/2). One line fixed.

**Run 2: 17/17, VERDICT ORIENTATION-CLASSES.**
- 16 representatives (8 patterns × `O ∈ {I, reflY}`; the rest of `O(2) ⊕ 1` differs by target z-rotations in L).
  Exactly 8 are `p ∘ c ∘ p′` with `p, p′` in the Pauli-sign subgroup of L and `c ∈ {cnot, T cnot}` (Q3, two each)
  or `{cnot′, T cnot′}` (R_B Q3, two each). The other 8 send `prodState xplus z3` outside maxCone under `G∘G`
  (value −1/2: the landed chain, for both one-copy reflections; `(R_A cnot)²` is new, `(R_B cnot)²` is K2Guard's).
- Hence in the cone setting: **`G ∈ L·{cnot, T∘cnot}·L` with `K = Q3`, or the `R_B`-conjugate with `K = R_B Q3`.**
  `T∘cnot` (antiunitary) is an admissible native gate preserving Q3, so the gate-level conclusion must include it and
  the group form must use `⟨L, GLG⁻¹⟩`, not `⟨L, G⟩`.
- Cross-check (pressure test of the favourable N1 verdict): EQ-E's quantum gate `CNOT·diag(1,1,u,ū)`, `u = (3+4i)/5`,
  with its own NOT `N_u`, after rotating `N_u`'s axis to `e_x`, lands on B1's pattern `(1,1,−1,1)` with `O = I`.
  One-directionality: `(S⊗I)·CNOT = actC(R_z(π/2))∘cnot` has the frame and fails relC for every horizontal
  π-rotation tried (so `ℓ₁∘cnot∘ℓ₂` is not automatically a control gate).
- KAK inputs exact: `cnot∘actC(R_x θ)∘cnot = Ad exp(−iθXX/2)`, YY and ZZ by local conjugation, XX/YY/ZZ commute.

### N2 — Lemma COMPACT (`b3_compact.py`, 9/9 on its first run)
- Edited before its first run: the marginal identity was first written with a spurious factor 2 (caught by reading,
  not by a run). After the first passing run a tautological sub-check of A.1 (`2**n == 2**n`) was replaced by an
  actual matrix-power computation; the output was byte-identical (`b3_compact.run1.*` kept).
- Countermodels: the owner's quadrant; **a local boost on Q3 itself** (`onC(B) = (1/3)Ad(diag(3,1)⊗I)`, exact) with
  `u(onC(B)ⁿ e00) = (3ⁿ+3⁻ⁿ)/2`; and the group form fails without normalization (`G (actC nflip) G⁻¹` moves `u`).
- IIP-1 route (landed `invariant_inner_product_span`, IIP:455): hspan (products span W 3, rank 16), bounded slice
  (exact identities `w_{μν} = Σ ab⟨e_a ⊗ e_b, w⟩`), block-scalar invariant forms from a finite subgroup (octahedral
  rotations; dimension 4), F-fixed vectors = span(e00). So Lemma COMPACT needs no Haar measure and no group closure.

### N3 — general gate and continuous case (`b4_lie_light.py`)
- **Run 1 (kept: `b4_lie_light.run1.*`): 8/9, VERDICT NOT RENDERED — a draft expectation refuted.** I expected
  `V1 ∩ so(Q) = l` (dim 6) for every non-Euclidean block scalar Q. Exact: dim 15 when exactly one of `b, b′` equals
  `c`. The extra 9 are the graph submodules `G∓ = {X ∓ φX}`, which connect only one marginal block to the
  correlations. **So the IIP-1 form alone does not exclude the graphs; EQ-C's bracket obstruction does.**
- Run 2 (A.1 restated as an identification + A.2 bracket test): 10/10. `V1 ∩ so(Q)` is exactly `l ⊕ M1 ⊕ M2` /
  `l ⊕ G−` / `l ⊕ G+` / `l`; neither `l ⊕ G±` is bracket-closed. Conjugated generators of `cnot` (`cnot′`, `T cnot`)
  span exactly `l ⊕ M1` (`l ⊕ M2`, `l ⊕ M1`) and contain a basis of it; the boost countermodel leaves V1.
- Design consequence (written): the general case needs no closed-subgroup theorem and no Yamabe if one uses
  (a) IIP-1, (b) the span `s` of tangent vectors of curves in Γ (a Lie algebra by differentiating `Ad_γ(t)`),
  (c) the exact V1/module/bracket certificates, (d) the normalizer lemma, and (e) generation by the inverse function
  theorem (Mathlib v4.33.0: `ContDiffAt.toOpenPartialHomeomorph`, InverseFunctionTheorem/ContDiff.lean:31) with a
  chart of the unitary group (`Unitary.openPartialHomeomorph`, CStarAlgebra/Unitary/Connected.lean) and
  `Unitary.mem_pathComponentOne_iff` (:336). Absent at the pin (grep): closed-subgroup theorem, Yamabe, Lie product
  formula, Lie correspondence, SVD.

### N4 — IE₁ accounting (`b5_ie1.py`, 9/9)
- **Correction to the brief: `driveWords3` is not countable.** It is `words(Set.range rot3 ∪ {cyc3})` with
  `rot3 : ℝ → …` (OrbitNormalization.lean:571, KInfFoundations.lean:449–450), and it equals SO(3): A.1 (cyc3
  conjugation gives the x-rotations, landed as `rotX`), A.2 (stabilizer of `e_z` in SO(3) is the z-rotations) and the
  landed `exists_word_pole` (ON:658). So IE₁ over `driveWords3` is exactly IE₁ over SO(3).
- Countable dense regime (e.g. rational-quaternion rotations, a countable group by exact multiplicativity): with K
  closed, IE₁ extends to SO(3) by continuity; without, `int Q3 ⊆ K ⊆ Q3` (Mathlib `Convex.interior_closure_eq_
  interior_of_nonempty_interior`, Convex/Topology.lean:268) and the boundary is unpinned (K_d; written with a
  Lindemann–Weierstrass or Baire step).
- Finite regime: local octahedral rotations + cnot generate the Clifford group (order 11520 exactly); the pure state
  `(1,1,1,2)/√7` has an entangled orbit (max marginal 45/49), so the closed cone `cone(Cliff·products)` is a
  countermodel. The native group H (order 8) likewise (k2d T6 re-derived; same 45/49).
- **Harness incident (determinism), recorded rather than hidden.** After a text-only edit (correcting two line
  references: `exists_word_pole` is ON:658 and `rotX` ON:581, not ON:654/ON:584), the third run of `b5_ie1.py`
  crashed inside `sympy.solve` (`NotImplementedError`; traceback kept as `b5_ie1.run3crash.*`). The two earlier runs
  had passed 9/9. Cause: `python3 -I` ignores `PYTHONHASHSEED`, so hash randomization is always on, and `solve`'s
  internal path depends on hash order. Fix: check A.2 now uses the exact sum-of-squares identity
  `(a−d)² + (b+c)² = (MᵀM−I)₀₀ + (MᵀM−I)₁₁ − 2(det M − 1)` (no solver). Three consecutive runs of the fixed script
  are byte-identical. Rule adopted for this thread: no `sympy.solve` in any probe; only expand/simplify-to-zero
  tests and exact rational linear algebra. Determinism of every probe is checked by `run_all.sh` (different hash
  seeds per run).

### N5–N6 — converse and foils (`b6_foils.py`, 8/8; two defects fixed before its first run)
- Before the first run: K.6 contained a vacuous self-comparison (replaced by the product-preservation checks for
  SWAP, R_B and a rational rotation), and the K_heis invariant compared `|det S|²` with `|c|²` instead of `|c|⁴`.
- Converse: products in Q3 (48 exact PSD instances + [L] Kronecker), Q3 ⊆ max (instances + [L]), cnot fixes u and is
  `Ad(CNOT)`; the twin inherits everything through R_B.
- One foil per hypothesis: K_nc (convexity), the ray ℝ≥0·e00 (products ⊆ K), B3 (K ⊆ max), K_F / C_H / K_heis
  (IE₁; K_heis exact: the orbit invariant `|det S| = |c|²` holds at an orbit point, 1/16 = 1/16 squared, and fails
  after `(I − iX) ⊗ I`, 5233/10000 vs 1/16), min / max (the gate).

### N7 inputs — module facts and certificate sizes (`b7_certificates.py`, 5/5)
- `dim Hom_l`: l→l 2; M1→M1, M2, N 1 each; M1→l 0; l→M1 0. **N is isomorphic to M1 and M2** (multiplicity 3 in V1's
  (3,3) part), so the invariant form must remove N before the submodule analysis (EQ-C's order was right; this makes
  it necessary). `Hom_l(M1, l) = 0` is now certified (it was asserted, not computed, in the v1 design's step e).
- Certificate sizes: V1's upper bound from **51 rational sphere pairs** (408 rows × 240, height 2645), rank 207;
  the native tangent block from the 96 relC/corner rows plus tightness rows at **8 rational targets**, rank 124.

### Replays of prior work (into `replay/`)
- EQ-C P1, P2, P3, P5, P7 and K2C P2, P4, P5: byte-identical to the recorded outputs.
- `eqreview/review_eqC_fast.py`: stdout identical except that the recorded file ends with an extra line `exit 0`
  (the recorder appended the exit status; not script output).

### Fixed point (§A.31)
Pass 1 (N1–N4): NEW — the native classification (every control gate at d = 3 is local∘cnot∘local; cone-compatible
ones are L{cnot, T cnot}L or the twin's); `driveWords3 = SO(3)`; Lemma COMPACT = IIP-1 on the slice; the graph
submodules survive the invariant form. Pass 2 (N5–N7, pressure tests): NEW-borderline — the Clifford-orbit
countermodel for finite IE₁ with a closed cone; `N ≅ M1` forcing the order of the steps; Entangling redundant at
d = 3. ELABORATING — the countable-regime sandwich; the Lie-light substitute for the Lie glue (written, inputs exact).
Fixed point NOT reached (two passes with NEW findings). Next pass: the Lean proof plan of K2C U's transitivity lemma
(Schmidt from the 2×2 spectral theorem), and whether the IFT generation step can be replaced by a finite KAK-type
word bound for a general admissible gate.

### Final integrity sweep
- Base: `sha256sum -c ../base.manifest.sha256` exit 0, 1317 files (unchanged from the start).
- `/home/user/incompleteness`: `git status --porcelain` empty; HEAD `bc3bf9bc…` (the same as at the start).
- Bytecode: no `__pycache__` newer than the protocol under `eq/C`, `k2c`, `eqreview`, `eq2` (`k2c/__pycache__` is from
  2026-10-06, untouched; every run used `-B`).
- Writes: all of mine are under `eq2/B/`. The harness keeps background-command logs in its own `tasks/` directory
  outside the scratchpad. Files newer than the protocol elsewhere in the scratchpad belong to other writers
  (`eqreview/HINF-REVIEW.md`, `eqreview/OPENAI-MATH-REVIEW.md`, `eqreview/replayC2/`, and thread A's directory).
- **Isolation note, recorded rather than hidden.** The sweep's `find` printed the *names* of files under `eq2/A/`. No
  file there was opened or read, and nothing in this thread depends on them. Future sweeps should exclude
  `eq2/A` and `eq2/C` from the `find`.
