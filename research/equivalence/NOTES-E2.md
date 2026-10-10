# NOTES-E2 — the eight K∞ seams: which are discharged, by what, and what stays independent

Base L = `9f9f8257`. Evidence: [K] kernel at L; [D] design module `research/equivalence/lean/EqvSeams.lean` and
`EqvSeamsControl.lean`, byte-identical to the blobs at dev commit `f5367a7a` (branch `dev-equivalence/kinf-seams`),
built green in `workflow_dispatch` run **38083519826** (Mathlib bridge job 114305141530: `Build completed successfully
(3645 jobs)`, all fifteen `#print axioms` lines of the two modules `[propext, Classical.choice, Quot.sound]`; the gate's
`lean-axioms` step OK, 5875 named results, no sorry; the gate failed only at `lean-manuscript` — the two modules have no
registry family — and at `claims` and `duplicate`, which scan the branch's `research/` tree) — kernel-checked in a design
run, not certified; [X] exact probes under `experiments/`; [W] written here; [A] archive records.

**Productivity test (fixed before the probes, §A.31).** A seam result counts only if it is strictly stronger than "the
seam is unsourced" and either discharges the seam from others or a named weaker premise, or exhibits a countermodel to
such a discharge.

## Standing table

| seam | kernel object at L | E2 outcome | label | evidence |
| --- | --- | --- | --- | --- |
| K∞-Seed | `SharpSeed` OrbitGeneration.lean:65 | **discharged** from K∞-Stage (SC∞ and a completion chart), a *sharp stage test* (a stage effect with the value 1 at one stage preparation and 0 at another) and the chart body's identification with `eball` (K∞-Trans, or its dense form) | CONJECTURE [D] (proved in a design run; not certified) | `sharpSeed_eball_of_stage`, `exists_sharpSeed_eball_of_stage`, `exists_sharpSeed_eball_of_stage_dense` |
| K∞-Copy | one `N` in `NativeGate` CompositeDimension.lean:218 | **replaceable** by type covariance of native inversion: if the target copy's NOT is the conjugate of the control copy's NOT by a body automorphism fixing (or reversing) the corner axis, the two-NOT data reduce to a one-NOT native gate and DIM-1's selector applies; the two known two-NOT countermodels (J/K maps, d = 5, 7) violate the weaker premise | CONJECTURE [D] + [X] | `nativeGate2_conj`, `nativeGate_of_conj`, `dim_of_nativeGate2_conj`, `three_of_nativeGate2_conj_of_two_le`, `dim_of_nativeGate2_conj_neg`; `e2_copy_conj` 13/13 |
| K∞-Trans | `BoundaryTransitive` OrbitGeneration.lean:79 | **not discharged by the other single-system seams**: a body of chart dimension 4 carries ElementaryDrivability, a sharp seed, relative strict convexity (so singleton faces for every effect family) and capacity ≤ 2, and admits no body-preserving family that is boundary transitive or has a dense boundary orbit | CONJECTURE [W] + [X] (+ [K] contrapositive of TRB-1 and KTRANS-DENSE-1) | `e2_drive_trans` 10/10 |
| K∞-Drive | `ElementaryDrivability` KInfFoundations.lean:264 | no discharge; characterization OPS-Γ [A]; in chart dimension 3 a drive forces an ellipsoid (remark R3 below), in chart dimension 4 it does not (Ω₄) | CONJECTURE [W] + [L] (R3) | — |
| K∞-Act | `OpDatum`, `AffineRespect`, `Undoes` CompletionAction.lean:46/58/325 | no change: the existence form is discharged by the identity datum and the content is relative to the consumed family (SA §2.3 [A]); label duals source `AffineRespect` (SA P-A [A]) | OPEN | [A] |
| K∞-Stage | `SCInf` :78, `BinaryVisible` :244, `FiniteRank` :299 (StageCompletion) | no change: SC∞ by the protocol tower's `rfl` [A]; FiniteRank not forced on infinite carriers [A]; E2 adds that K∞-Seed is the stage-level sharp test plus this seam | OPEN | [A], [D] |
| K∞-V4 | `SeedOrbitAvailable` OrbitGeneration.lean:74 | no change; its `G` is K∞-Trans's `G` | OPEN | — |
| K∞-Geom | `SingletonFaces` :139, `RelStrictConvex` :144 (KInfFoundations) | no change as an obligation; E2 shows it does not supply transitivity even with drivability (Ω₄) | OPEN | [X] + [W] |

## 1. K∞-Seed is the stage-level sharp test (EqvSeams §A, [D])

`sharpSeed_completion` (StageCompletion.lean:224) gives `SharpSeed (body D) (coord D ⟨i, e⟩)` from `SCInf D` and
`(D.stage i).p e x1 = 1`, `(D.stage i).p e x0 = 0`. `sharpSeed_restrict` (OrbitNormalization.lean:427) reads it in the
chart (`chartBody C = bodyR C.L C.p0 (body D)`, CompletionAction.lean:166; `mem_range_of_mem_body`), and `sharpSeed_tr`
(OrbitNormalization.lean:242) carries it along any affine equivalence `A` with `A '' chartBody C = eball C.d`. The
design theorem, quoted:

```lean
theorem sharpSeed_eball_of_stage {D : DirectedStages} (C : CompletionChart D) (hSC : SCInf D)
    {i : D.ι} {e : (D.stage i).E} {x1 x0 : (D.stage i).P}
    (h1 : (D.stage i).p e x1 = 1) (h0 : (D.stage i).p e x0 = 0)
    (A : (Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ)) (hA : A '' chartBody C = eball C.d) :
    SharpSeed (eball C.d) (effTr A (effR C.L C.p0 (coord D ⟨i, e⟩)))
```

with the two existence forms through TRB-1's `chartBody_eq_eball` (TransitiveBody.lean:651) and KTRANS-DENSE-1's
`chartBody_eq_eball_of_dense` (DenseOrbit.lean:209). **Reading.** In K1's hypothesis list (`hP1 : SharpSeed (eball d)
r`, K1Bridge.lean:128) the seed is not an independent seam: it is supplied by K∞-Stage's SC∞ and chart, by the ball
identification K∞-Trans already supplies, and by one finite-stage fact — a stage test certain at one preparation and
impossible at another. That stage-level fact is exactly the "sharp visible pair" SA-LEDGER §2.3 found to carry all the
content of `BinaryVisible` [A]; it is a premise about a finite stage, checkable at a finite stage, and it is unsourced.
Classification: POSITIVE (a validated reduction; small).

## 2. K∞-Trans is independent of K∞-Drive, K∞-Seed, K∞-Geom and capacity two (`e2_drive_trans`, [X] + [W])

**The body.** Ω₄ = {(x, s) ∈ ℝ³ × ℝ : (x₀² + x₁² + x₂²)² + s⁴ ≤ 1}, the ℓ⁴-sum of the Euclidean 3-ball and the segment.

**What holds on Ω₄** (script checks D1–D8, with the written steps W1–W2 in its header):
- ElementaryDrivability (KInfFoundations.lean:264): flow `R_z(t) ⊕ 1`, NOT `= flow π`, `J = cyc3 ⊕ 1`; every field
  checked exactly (D1–D5), `J_off_axis` at `t = π/2` with the state `e₁`.
- a sharp seed `(1 + s)/2` (D6);
- relative strict convexity (W1: `F` is strictly convex along every nondegenerate segment), hence singleton faces for
  **every** effect family by `singletonFaces_of_relStrictConvex` (KInfFoundations.lean:590) [K]; exact midpoint instances
  (D8);
- central symmetry (D7), hence capacity ≤ 2 by Lemma D (`card_le_two_of_centrallySymmetric`, KInfFoundations.lean:632)
  [K] — so Ω₄ also meets the capacity clause of SA's proposed scope premise ElemScope [A].

**What fails.** The plane section `{x₁ = x₂ = 0}` is `{u⁴ + v⁴ ≤ 1}`, which is no ellipse (D9: the boundary points
`(1,0)`, `(0,1)`, `(t, ±t)` with `t⁴ = 1/2` force incompatible cross terms); an affine image of a ball centred at its
unique centre of symmetry has only ellipse sections through it (W3). By the contrapositives of
`exists_affine_image_eq_eball` (TransitiveBody.lean:602) and `exists_affine_image_eq_eball_of_dense` (DenseOrbit.lean:174)
[K], **no** set of affine automorphisms of Ω₄ is boundary transitive, and none has a dense boundary orbit (W4). Control
C1: on the Euclidean 4-ball the same drive checks pass and the section system is consistent (`B = 0`), so the
non-ellipse step is not vacuous.

**Reading.** The landed `not_boundaryTransitive_flow` (OrbitGeneration.lean:620) shows that one drive's flow is not
transitive on a body that *is* transitive under another family. Ω₄ is strictly stronger: on a general body the other
single-system seams together — drivability, a seed, the geometric seam in its strongest form, capacity two — admit no
transitive family at all, and no dense-orbit family either. So K∞-Trans (and KTRANS-DENSE-1's dense weakening) must be
supplied by its own source; it cannot be derived from those seams. The verdict is about the body Ω₄ only; it says
nothing about which bodies OI supplies, and nothing about chart dimension 3 (R3). Classification: **NEW** (for this
programme's chain: it upgrades the ROADMAP's "no theorem derives transitivity from ElementaryDrivability on a general
body" (:1021–1022) from an absence to a countermodel, under the geometric seam as well).

**Pressure test (§A.31, applied although the outcome is a separation).** (i) The non-ellipse certificate is a finite
exact system whose inconsistency is forced by rational arithmetic on `τ = t²` (`τ² = 1/2` against `τ = 1/2`), and its
control is consistent. (ii) The kernel theorems used in the contrapositive need compactness, convexity and interior
(W2), all elementary for Ω₄. (iii) The drive's fields are exactly the kernel structure's fields, `flow_add` in the
kernel's composition order. (iv) The strict-convexity proof is two lines of convexity (W1); its instances are exact.

**R3 — chart dimension 3 (remark, CONJECTURE [W] + [L]).** On a compact convex body with interior in ℝ³, the affine
automorphism group is compact and fixes the centroid; in an invariant inner product it lies in O(3). The closure of a
drive's flow is a nontrivial connected compact abelian subgroup of SO(3), hence a circle; `J_off_axis` makes `J` move that
circle, so the closed group they generate has identity component of dimension ≥ 2, hence SO(3) [L: the closed connected
subgroups of SO(3) are 1, SO(2), SO(3)]; an SO(3)-invariant body about its centre is a ball. So in chart dimension 3 a
drive alone forces the ellipsoid and transitivity, while Ω₄ shows this fails in chart dimension 4. The K route cannot use
this before DIM-1, whose selector is stated on `eball d` (circular); it is recorded as a structural fact about the seams.

## 3. K∞-Copy reduces to type covariance of native inversion (EqvSeams §B–§D, [D]; `e2_copy_conj`, [X])

**The two-NOT data.** `NativeGate2 Ω z NC NT G` is DIM-1's `NativeGate` with `relT` read with the target NOT `NT` and
`relC` with `NC` on the control side and `NT` on the result — the two-NOT reading of K2-LEDGER §6 [A], which records
(by a reading of the landed proof) that DIM-1's count consumes equal splits. **The reduction**, quoted:

```lean
theorem nativeGate2_conj (hG : NativeGate2 Ω z NC NT G) (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :
    NativeGate2 Ω z NC (h ∘ₗ NT ∘ₗ g) (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh)
theorem nativeGate_of_conj … (hcov : ∀ x, NT (g x) = g (NC x)) :
    NativeGate Ω z NC (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh)
theorem dim_of_nativeGate2_conj (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G) …
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3
```

(and `three_of_nativeGate2_conj_of_two_le` with `2 ≤ d`; `dim_of_nativeGate2_conj_neg` for a conjugator reversing the
corner axis, through `g ∘ NC`). The positivity transfer is `actT_mem_maxCone`: a target-side linear map carrying the
body into itself preserves `maxCone` (through `prodEffVal_actT`, the product effect with the target factor pulled back).
Only `IsNot` of the control NOT is used; the target NOT is constrained only through `hcov`.

**The probe** (`e2_copy_conj`, run 2: 13 checks, 0 failures, `VERDICT TYPE-COVARIANCE-CONSISTENT`, replay identical):
the kernel's `cnot` (parsed) is a one-NOT native gate (C1); conjugating its target copy by the exchange of the first two
axes gives two-NOT data with `NT = diag(−1, 1, −1) ≠ nflip`, same split (C2, C3); the reduction returns `cnot` exactly
(C5); the d = 5 and d = 7 J/K maps meet the relation clauses of the two-NOT reading (J1) with splits `(2,2) ≠ (1,3)`
and `(3,3) ≠ (1,5)`, so their NOTs are not even similar and no conjugator of any kind exists (J2), and neither has a
one-NOT reading with either NOT (J3); a shear fixing `z` breaks the positivity transfer (S1: value `−1/2`), so the
ball-preservation hypothesis of `actT_mem_maxCone` is load-bearing.

**Run 1 (kept: `e2_copy_conj.run1.*`)** did not render: two countercontrol expectations written before the run were
false. The swapped gate meets `relT(NT)` and `relC(NT, NT)` — it **is** a one-NOT native gate with the target NOT —
and the d = 7 J/K map meets `relT(NA)`. Both checks were over-specific forms of "no one-NOT reading"; they were
restated (C4, C6, J3) and no check of the reduction changed.

**Reading, with its scope.** (a) Type covariance suffices for the selector [D]. (b) For NOTs meeting `IsNot` (linear
involutions preserving the ball, hence orthogonal, with `N z = −z`), type covariance holds iff the two NOTs have equal
eigenspace dimensions [W: orthogonal involutions with `z` in their −1 space are conjugate by a `z`-fixing orthogonal map
iff their restrictions to `z^⊥` have equal ±1 multiplicities]; this is the equal-split condition K2-LEDGER §6 read off the
landed count [A]. (c) It is weaker than copy naturality as a premise on the copies' NOT assignments (the swapped data
have `NC ≠ NT`). (d) It is **not** shown to admit any gate that copy naturality excludes: the probe's own instance is a
one-NOT gate with the target NOT (C6). (e) The design module `EqvSeamsControl`'s header sentence "type covariance
therefore admits two-NOT data that the one-NOT hypothesis does not" is to be read in sense (c) only; the module was
built before run 1's finding and is kept byte-identical to the built blob. (f) Three-copy consistency of mismatched
splits (K-INF-DESIGN §17, probe 1b) was not run here. Classification: POSITIVE (confirms the ROADMAP's untested
candidate at :1027–1029, in the form "type covariance of native inversion, equivalently equal ±1 eigenspace dimensions",
with a kernel-checked design reduction and the countermodels' exclusion).

## 4. Cross-links the seams record

- **KTRANS-DENSE-1 against SA's countable-family exclusion.** SA-LEDGER §3.2 [A] closed every collapse regime partly
  because the operations a protocol tower supplies are countable and `not_boundaryTransitive_of_countable`
  (EffectSpace.lean:858) excludes countable families from boundary transitivity on `eball 3`. KTRANS-DENSE-1 [K] shows
  that the eleven pairing-table consumers need only a dense boundary orbit, which a countable family can have
  (`denseBoundaryOrbit_ratRefl`, `countable_seedOrbit_cone`, DenseOrbit.lean:403). So the countability obstruction no
  longer blocks the ball and the cone [K + W]. The NG1 regime still does: on a polytope of dimension ≥ 2 the orbit of a
  vertex under body automorphisms is a finite set of vertices, closed, and misses every non-vertex boundary state [W];
  the NG2 regime still does: a dense orbit gives the ball (`eq_qBall_of_dense`), whose boundary states are all extreme,
  and NG2's argument then collapses the body [A + W].
- **Ω₄ and the scope premise.** Ω₄ satisfies capacity ≤ 2 with a sharp pair, i.e. SA's ElemScope clauses [A], and
  relative strict convexity; neither scope nor geometry forces the ball without K∞-Trans.

## 5. Not decided here

Whether OI supplies a sharp stage test, a conjugator between copies' NOTs, a transitive or dense-orbit family, or any
seam; the three-copy consistency probe; any statement in chart dimension 3 at kernel level.
