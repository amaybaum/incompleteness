# NOTES-B8 — HO-4's composition-clause proposal tested against the realization theorem

Node B8 of `research/bridge` (round 2). Base L = `9f9f8257`. Evidence:
- [X] `experiments/b8_composition.py`: 4/4 PASS, VERDICT B8-EXACT. Run 1 is final; one pre-run edit is logged in
  the header; the replay is byte-identical.
- [K] at L: `finiteOI_not_implies_inert` (OIRealization.lean:360); `sameCore_both_sides` (OIRealization.lean:343);
  `InertSpectatorCompositionality` (SpectatorBridge.lean:223); `inertSpectator_iff_parallelReferenceExtension`
  (SpectatorBridge.lean:233); `HasParallelReferenceExtension` (ReferenceExtension.lean:447).
- [A] HO-4 v1 (received, `inbox/`): KZ6, KZ7 at their labels. The coordinator confirmed both independently. B8
  re-derives what it uses (X2, X3).
- The theorem text is Main.md:552–556 (the five clauses). It has no Lean declaration at L; the coverage ledger lists
  `opglue_probes.py` as its checker.

**Success criterion (set by the round-2 directive).** Two questions:
1. Does the clause that makes continuous local operations act on the pair appear among the realization theorem's
   clauses or their kernel counterparts?
2. Is it (b) under the disguise test?

## 0. Answer

1. **Clause (4) is a composition clause, and for a local rotation it is (b) for that rotation.** Main.md:552 reads:
   "the product construction implements the joint family by applying the local instruments' CP maps as
   `𝓘_a ⊗ 𝓘_b` on the joint branch register". For a unitary local instrument, through the dictionary, this is
   exactly `actC B(U)` (resp. `actT B(U)`) on the pair table (X1). So applied to a local rotation it is the composite
   action for that rotation, relative to the joint state space.
2. **No clause makes continuous, or any further, local operations act on the pair.** The theorem's input is a fixed
   quantum experiment: the joint Hilbert space and state, and a *finite* instrument family `𝓕`. So:
   - the joint state space is the PSD cone by hypothesis;
   - clause (4) acts on the members of `𝓕` and on nothing else.

   Which local operations are joint instruments is input, not a clause. The theorem's "range", the quantum
   experiments, excludes K(Z_F) by its hypothesis, not by clause (4). The same machinery with a non-quantum family
   realizes K(Z_F) exactly with clause (4) intact (B4): its local instruments are the NOTs and the local
   measure-and-prepare instruments, all compatible with K(Z_F).
3. **The excluding clause is the family-membership clause**: "an operation available to a token in isolation is an
   instrument of the joint family". At level H this is (A) / H-OI_g (B1.1, B5). Its matrix form at L is
   `InertSpectatorCompositionality` ⟺ `HasParallelReferenceExtension` (OI⁺-1). The kernel proves that bare finite
   OI does not imply it: the audited sealed C1–C4 core, with exact system QM and full composite unitary control, is
   realized in a theory without it (`finiteOI_not_implies_inert`). **Its absence from OI is CERTIFIED at the matrix
   level.**
4. **Disguise test.** Clause (4) together with membership of the flow is (b) for the flow, and the test **FAILS**: it
   restates I3.165's clause "local actions compatible with the composite cone" and OI⁺-1's spectator clause. Clause
   (4) alone, for a given family, is not (b) and excludes nothing (B4).
5. **Sharpening HO-4 (exact).** On K(Z_F), clause (4) admits exactly the single-token rotations
   `V4 = {I, R_x(π), R_y(π), R_z(π)}` on each token:
   - among the 24 Cliffords [X2];
   - over all of `SO(3)` [W §2], with KZ7 [A, re-derived for the two A_miss axes, X3].

   Extending one token's joint family by **one** rotation outside `V4` excludes K(Z_F), whether the rotation is
   discrete or continuous: `S`, `cyc3`, a π-rotation about a face diagonal, the drive step `R_z(θ)`. So
   "continuous" is not what excludes K(Z_F). It is what is needed to force `Q3`: the native discrete family, the
   Clifford group of order 11520, still leaves exotic cones [A, C5 census; B3-1], and every compact family with
   abelian identity component does too (B7-2).

## 1. Clause (4) at the table level (X1)

For `U ∈ {P = diag(1, (3+4i)/5), S, H, V}`, checked on all 16 basis tables:
- `M(actC B(U) ω) = (U⊗I)M(ω)(U⊗I)*` and `M(actT B(U) ω) = (I⊗U)M(ω)(I⊗U)*`;
- `P` is the drive's rational step, with `B(P) = R_z(θ)`, `cos θ = 3/5`;
- `V` is the Clifford lift of `cyc3`; `B(V)` is the kernel's `cycEquiv` matrix.

So `𝓘_a ⊗ id` for a unitary local instrument is the kernel's composite action of its Bloch rotation.
`M` is used as a comparison tool only; it is never a premise.

## 2. The rotations clause (4) admits on K(Z_F) (X2, X3; [W] for `SO(3)`)

- **X2.** Among the 24 one-qubit Cliffords modulo phase, on token A and on token B, exactly the four Paulis permute
  the defect lines `ψ_s`, and so preserve K(Z_F). This holds because each is a unitary conjugation preserving `Q3`
  and `ipW`-orthogonal. Each of the other 20 per token (40 in all) is excluded by a certified witness:
  `y = φφ*` with `max_t |⟨ψ_t|φ⟩|² ≤ 1/2`, so `y ∈ PSD ∩ Z_F* ⊆ K(Z_F)`, and `tr(y·X) < 0` for the image `X` of a
  defect.
- **X3.** For the flows of A_miss, `R_z(t) = diag(1, c + is)` and `R_x(t) = H R_z(t) H`, on both tokens: the
  witnesses `(W^{±1}⊗I)ψ_s` are certified. Their pairings with the moved defects are `−s` and `+s` identically,
  under `c² + s² = 1`. So every `t` with `sin t ≠ 0` moves K(Z_F). This is KZ7 for the two axes that matter.
- **[W] All of `SO(3)`.** By KZ7 [A] (every axis), the single-token stabilizer contains only `I` and π-rotations.
  - Two π-rotations about axes at angle `α` compose to a rotation by `2α`. Closure therefore forces `α ∈ {0, π/2}`.
  - So the axes are mutually perpendicular, the stabilizer lies in a Klein four-group, and since it contains the
    coordinate `V4` it equals it.
- **X4, control.** Every witness pairs nonnegatively with the image of every Bell projector (an element of `Q3`)
  under the same local map. The exclusions are specific to K(Z_F), as in B4 R12.

## 3. Verdict

| item | status |
|---|---|
| clause (4) for a unitary local instrument = composite action on the table | [X] X1 (dictionary as comparison tool) |
| a clause of the realization theorem making continuous local operations joint instruments | **absent**: the family `𝓕` is input (Main.md:552) |
| its matrix form, inert-spectator compositionality, implied by the sealed C1–C4 core with exact system QM and full composite unitary control | **no**: CERTIFIED [K at L, OIRealization.lean:360] |
| the excluding clause (membership + clause (4)) passes the disguise test | **FAILS**: it is (b) / OI⁺-1's spectator clause |
| HO-4's proposal ("a realization theorem whose composition clause makes continuous local operations act on the pair cannot have K(Z_F) in its range; that clause is (b)") | **confirmed**, with the sharpening: one non-`V4` local rotation suffices to exclude K(Z_F); continuity is needed only to force `Q3` |

- **Gem classification.**
  - **ELABORATING**: HO-4's proposal is confirmed and located. The clause is family membership, not clause (4),
    and its matrix form is certified independent of OI.
  - **NEW, small**: the single-token stabilizer of K(Z_F) is exactly `V4`. This gives a discrete exclusion criterion.
- **Not claimed.**
  - Nothing about exotic cones other than K(Z_F).
  - The realization theorem itself is not a kernel declaration at L.
