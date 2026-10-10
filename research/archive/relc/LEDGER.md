# REL-C ledger — what survives when `GateRel` (relT ∧ relC) is replaced by `relC` alone

Read-only research thread. Base snapshot `L = e2426ba4109dcd719d518aefbd3c417b7c6fdc5b` (detached worktree `wt-L`,
read only). Nothing here is adopted, preregistered, frozen or governed; no git or GitHub state was changed.

Artifacts in this directory:
- `relc_probe.py`: exact computation (Fraction / sympy). Output is in `probe_output.txt`: 34 PASS, 0 FAIL.
- `dep_audit.py`: a syntactic call-graph audit of `CompositeDimension.lean` at `L`, with its own controls. Output is in
  `audit_output.txt`, and the controls PASS.
- `RelCDraft.lean`: an **UNBUILT** Lean design draft. It contains `sorry`s and has never been compiled.

Evidence levels used below: **kernel** (landed at `L`, read from source), **exact** (this thread's exact computation,
with controls), **written** (a proof written here and not kernel-checked), **open**.

## Productivity test

The test was applied as stated here. This ledger was written after the walk, so the test does not carry an
independent time-stamp.

> The thread produces a gem if and only if it yields a fact strictly stronger than "drop relT and re-read the landed
> proofs", **and** that fact either constrains something (a dimension, a NOT, the existence of a gate) or exposes a
> hidden assumption, such as a hypothesis that a landed proof reads but that is not load-bearing for its conclusion.
> Anything else counts as coherence relabeling and is recorded only.

## Setting (from `CompositeDimension.lean`, kernel)

- `toOp` identifies `W d` with `End(V)`, where `V = HVec d` and `n = d+1`.
- `toOp_actC`: `actC N` is left multiplication `L_H` by `H = homMap N`. It needs no hypotheses.
- `toOp_actT`: `actT N` is right multiplication `R_H`. This uses `IsNot` for self-adjointness.
- `E± = plusSpace / minusSpace`, with dimensions `P` and `Q`, and `P + Q = n` (`finrank_plus_add_finrank_minus`).
- `Q ≥ 1` (`one_le_finrank_minusSpace`).
- Using `actC_actC`, `relC` is equivalent to `G̃ ∘ L_H = (L_H ∘ R_H) ∘ G̃`, where `G̃ = opGate G`. So `G̃` conjugates `L_H`
  to `Θ := L_H R_H`, the map `F ↦ HFH`.
- `relT` is equivalent to `G̃ ∘ R_H = R_H ∘ G̃`.

## Node tree

### N1 — Q1: does relC alone balance the eigenspaces? (decisive branch)

**N1.1 Where the landed argument reads relT.**
- *Check:* reading the Lean source, cross-checked with `dep_audit.py`.
- *Verdict:* `finrank_plus_eq_finrank_minus_rel` reads relT in exactly one place. The `hplus` step of `Lop_eq_zero_rel`
  uses `opGate_comp_homMap_rel`, which is `hR.relT`. That step is the **injectivity** of `Lop`.
- `Lop_anti_rel` (the anticommutation `Lop ∘ Pop = −Pop ∘ Lop`) reads only `relC`.
- DIM-1's `finrank_plus_eq_finrank_minus` has the same structure: the audit lists `Lop_eq_zero` and `Lop_injective` as
  relT-tainted and `Lop_anti` as clean.

**N1.2 Does the landed route survive (is `Lop` injective under relC alone)?**
- *Check:* exact computation of the kernel dimension of `Lop`.
- *Verdict: NO.* `KG = K ∘ cnot` satisfies `IsNot`, frame and relC, fails relT, and has `dim ker Lop = 1`. Here `K`
  exchanges the matrix units `x⊗x` and `y⊗y` and commutes with `Θ`.
- Controls: `cnot` gives 0, which reproduces `Lop_injective_rel`. `G_R` (N4.4) also gives 0.
- So the landed *proof* needs relT. That does not settle whether the *conclusion* does.

**N1.3 Alternative route: similarity of `L_H` and `Θ`.**
- *Written proof.* By relC, `G̃` restricts to a linear isomorphism from `ker(L_H − 1)` onto `ker(Θ − 1)`, with
  `G̃⁻¹` mapping back because `G̃⁻¹Θ = L_H G̃⁻¹`.
  - `ker(L_H − 1)` is the set of `F` with values in `E₊`. Its dimension is `n·P`.
  - `ker(Θ − 1)` is the set of `F` commuting with `H`, which is `End(E₊) × End(E₋)`. Its dimension is `P² + Q²`.
  - So `nP = P² + Q²`. With `n = P + Q` this gives `Q(P − Q) = 0`, and since `Q ≥ 1`, **`P = Q`**.
  - Equivalent trace form: `tr L_H = n(P−Q)` and `tr Θ = (P−Q)²`, and these must be equal.
  - What the proof reads: `IsNot` only through "`N` is an involution, `Nz = −z`, `z ≠ 0`". It does not read the ball,
    the frame or positivity.
- *Exact check C1.1.* For every d ≤ 5 and every diagonal NOT type (`P = 1..d`), the code measures (by rank) the
  `+1`-eigendimensions of `L_H` and `Θ`, and their traces. They agree **iff `P = Q`** (table in `probe_output.txt`).
- *Exact check C1.2.* For d ≤ 3, the linear system `G·L_H = Θ·G` is solved exactly.
  - The solution-space dimensions match the predicted values (8, 39, 42, 112, 128, 144).
  - A random solution reaches the maximal-rank bound `Σ_λ min(mult)`.
  - An invertible solution exists exactly when `P = Q`.
- *Positive controls.* The landed `cnot` (d=3), `gJ5` (d=5) and `cnot1` (d=1) satisfy relC (C1.0).
- *Countercontrols.*
  - X1.3a: `id` satisfies relT for the unbalanced NOT `diag(1,−1)` at d=2, so relT alone does not balance.
  - X1.3b/c: `swapgate` at d=2 exchanges the entries `(0,2)` and `(2,2)`. It satisfies **frame + relT + invertibility**
    and fails relC.
- *Skeptic pass.* This branch is favorable: it makes the hypothesis weaker.
  - The algebra uses only `toOp_actC`, `toOp_actT` and `actC_actC`, all landed.
  - The dimension count is checked against measured ranks, not only against the formula.
  - The countercontrols show the computation separates relC from relT.
- *Verdict:* **relC alone gives balance and odd d.** This is **NEW**. Evidence: written proof, plus exact computation
  for diagonal NOTs with d ≤ 5. Non-diagonal NOTs are orthogonally conjugate to diagonal ones and are covered only by
  the written proof.

### N2 — Q2: an even-dimensional countermodel?

- *Verdict: none exists.* This follows from N1.3: no even `d` admits `IsNot (eball d) z N` together with an invertible
  `G` satisfying relC, with or without frame or positivity.
- The strongest even-d object found drops relC instead: `swapgate` at d=2 has frame + relT + invertibility. It fails
  relC (exact) and fails forward positivity at the exact rational witness:
  - control input `x = (1,0)`, target input `y = (0,1)`;
  - effects `a = hom(−4/5, −3/5)` and `b = hom(0,1)`;
  - `pairVal = −6/5`.
- Whether some even-d gate satisfies frame + relT + P± (dropping relC) was **not examined** beyond this one gate.
- Classification: **ELABORATING** (the branch is closed by N1).

### N3 — Q3: d = 3 under relC alone

- *Written.* The following landed proofs consume only the balance `finrank_plus_minus_three`: `tangentPlus_three`,
  `piRotation_three`, `det_three`, `not_gateRel_refl3` and `not_gateRel_negId3`. Replacing the balance by N1.3 gives:
  - with relC alone, both eigenspaces of `H` have dimension 2;
  - `N` is a π-rotation about a unit axis, with `det N = 1`;
  - **`refl3` and `−id` admit no invertible G with relC**, with or without the frame.
- *Exact certificates (C2.2, C2.3).*
  - `refl3`: `tr L_H = 8` and `tr Θ = 4`.
  - `negId3`: `tr L_H = −8` and `tr Θ = 4`.
  - Since the traces differ, the two maps are not similar, so no invertible G exists.
  - Control: `nflip` has `0 = 0` and `det 1` (C2.1).
- Classification: **ELABORATING**.

### N4 — Q4: higher odd d with relC + frame + positivity

**N4.1 Where DIM-1's selector reads relT (audit).**
- `dep_audit.py` finds only two direct consumers of `.relT`: `gate_actT` and `opGate_comp_homMap`. It finds no opaque
  destructuring of the hypothesis.
- In the block reduction, the only relT-tainted line is **L2668** of `blockData_of_orthonormal` (`hrow`, via
  `gate_actT` and `Minv_homMap`). That line shows `actT N ω = ω` for `ω = G(lift c ⊗ Minv(hom 0))`.
- Everything else is untainted: S1, S2, the block positivity, the `Phi_*` lemmas, `gt_center`, `not_entangling_one`
  and `dim_of_bounds`.
- Audit controls: it must flag the two known relT sites; it must not flag `Lop_anti` or `gt_center`; it must find the
  relC sites. PASS.
- The other relT use in the selector is parity, which is replaced by N1.3.

**N4.2 Replacement lemma (NEW).**
- *Statement.* With frame, posFwd, posInv and relC, for every `c ⊥ z` with `|c| ≤ 1`, every `a`, and every
  `u ∈ minusSpace N`: `Φ(a, c; u, hom 0) = 0`.
- *Proof A (eigen-sign plus mixed symmetry; written).*
  1. Split `c = c₊ + c₋` into its N-eigencomponents. Both are ⊥ z and have norm at most 1.
  2. By relC, `ω± = G(lift c± ⊗ Minv t)` satisfies `Hω±H = ±ω±` for every `t`.
  3. For `u ∈ E₋`, the map `a ↦ Φ(a; u, h0)` vanishes on `E_±`, and the map `a ↦ Φ(a; h0, u)` vanishes on `E_∓`.
  4. The landed `Phi_sphere.2` (positivity-derived and relT-free) equates the two maps. It extends from `Lor a` to all
     `a` by `linearMap_eq_zero_of_lor`. Hence both maps vanish.
- *Proof B (tangent curve; written).*
  1. `F(a) = pairVal(a, h0−u, G(hom c ⊗ Minv(h0−u)))` is ≥ 0 on `Lor`.
  2. On `Lor`, `F(a) = a₀ + a_z − 2Φ(a; u, h0)`. This uses `gt_corner`, `gt_corner_neg` (relC), `Phi_sphere` and
     `Phi_center`.
  3. `F` vanishes at `hom(−z)`, so the landed `tangent_vanish` gives `Φ(lift c'; u, h0) = 0` for every `c' ⊥ z`.
- *Consequence.* Every row of `ω` is orthogonal to `E₋`, hence fixed by `H` (`homMap_dot`). This is exactly what L2668
  needed. `blockData_of_orthonormal` and `dim_of_nativeGate` then go through verbatim.
- *Exact controls (section 4).*
  - The lemma's conclusion and the proof-A chain hold for `cnot` (GateRel) and for `G_R` (relC only, positive)
    (C4.5, C4.6, C4.8).
  - The proof-B slice formula holds on both (C4.11).
  - Step (i) holds at d=5 for the landed relC gate `gJ5` (C4.12).
  - Countercontrol `KG` (frame + relC, ¬relT): step (i) holds, mixed symmetry fails, and the conclusion fails (X4.7,
    X4.8). KG fails posFwd at an exact witness, value **−2/5** (X4.9). The same point gives 2/5 on `cnot` (C4.10).
- *Recorded misprediction.* Before running, this thread predicted −6/5 for KG by applying mixed symmetry to KG. Mixed
  symmetry is a consequence of positivity and fails for KG, so the prediction was wrong. The exact value is −2/5.

**N4.3 Selector under relC.**
- *Written.* With `IsNot (eball d) z N`, frame, posFwd, posInv and relC (**no relT**), **`d ∈ {1, 3}`**. Adding
  `Entangling` gives **`d = 3`**, through `not_entangling_one`, which reads only the frame.
- The proof is DIM-1's: N1.3 supplies the balance, and N4.2 replaces L2668.
- So no odd `d ≥ 5` is admitted. In particular there is no d=5 gate with frame + relC + P±.
- *Skeptic pass.* This branch is favorable: it strengthens a landed selector. Checks done:
  - the mechanical audit;
  - two independent proofs of N4.2;
  - a positive relC-only control that is positive and not GateRel;
  - a non-vacuous countercontrol.
- *Residual risk.* The landed lemmas are stated over `NativeGate`, so restating them over a relT-free structure has not
  been kernel-checked. The audit is syntactic.
- Classification: **NEW**. Evidence: written proof, assembled from kernel lemmas whose relT-independence is audited.

**N4.4 relT is not implied (d = 3).**
- `G_R = cnot ∘ (I ⊗ homMap R)`, where `R` is the rotation about `z3` by `(3/5, 4/5)`, so `R` does not commute with
  `nflip`.
- *Exact* (C3.0–C3.5): frame holds, relC holds, **relT fails** (on 8 of the 16 matrix units), `G_R` is invertible with
  inverse `(I⊗Rᵀ)∘cnot`, and `G_R(x⊗y) = cnot(x⊗Ry)` symbolically.
- *Written*: positivity.
  - posFwd: from the landed `nativeGate_cnot.posFwd`, since `Ry ∈ eball 3`.
  - posInv: `pairVal a b ((I⊗M)ω) = pairVal a (Mᵀb) ω`, and `Mᵀ = homMap R` preserves `Lor`.
- So relT is a genuine extra constraint that is not load-bearing for the selector.
- `G_R` normalizes to `cnot`. Whether relC + frame + P± forces relT for the *normalized* gate `G∘(I⊗M₀⁻¹)` is
  **open** (not pursued).
- Classification: **NEW**.

### N5 — fixed-point passes

- Pass 1: the d=1 path, the ParityNot d=3 chain, and `OddChar`'s characterization. Corollary (written):
  `IsNot` + frame + relC exist **iff d is odd**. The forward direction is N1.3; the reverse is the landed `cnot1` and
  `gRev k`, which are GateRel and therefore relC.
- Pass 2: the posInv path (`gate_corner_symm`) does not need relC for `G.symm`. relC is not closed under inverse,
  although GateRel is.
- Neither pass produced a NEW finding. That is only 2 passes, not the 3–4 that §A.31 asks for.

## What survives under relC alone

| conclusion | GateRel (landed) | relC alone | relC + frame | relC + frame + P± |
|---|---|---|---|---|
| `dim E₊ = dim E₋` | kernel | **survives** (written; exact for diagonal NOTs, d≤5) | survives | survives |
| `d` odd | kernel | **survives** (written) | survives | survives |
| frame-compatible gates exist exactly at odd `d` | kernel (ODD-CHAR-1) | n/a | **survives** (written corollary) | — |
| d=3: `dim E± = 2`, `tangentPlus = 1`, π-rotation, `det N = 1` | kernel | **survives** (written; the landed proofs read only balance) | survives | survives |
| `refl3`, `−id` excluded at d=3 | kernel | **survives** (exact trace certificate + written) | survives | survives |
| landed injectivity of `Lop` | kernel | **fails** (KG, exact) | fails (KG has the frame) | open (G_R: injective) |
| `d ∈ {1,3}` | kernel (NativeGate) | no (gRev at every odd d) | no (gRev) | **survives** (written) |
| `d = 3` with Entangling | kernel | — | — | **survives** (written) |
| relT itself | — | not implied | not implied | **not implied** (G_R; exact algebra + written positivity) |
| relT for the normalized gate | — | — | — | **open** |

## Classification summary

- **NEW** (N1.3): relT is not needed for balance or oddness. This answers what ODD-CHAR-1 left open ("does not show
  that … relT … is needed for oddness"). It also qualifies the PARITY-NOT-1 note: the note's sentence correctly
  describes the landed *argument*, but the conclusion does not need relT.
- **NEW** (N4.2–N4.3): relT is redundant for DIM-1's selector. In NB-1's consumption table, Rt is marked as used in
  S1, S4 and S5. This thread removes it at each step: S5 via N1.3, the S4 nonzero entry via N4.2, and in S1 Rt fed only
  `Minv_homMap`, which is used only at L2668. NB-1 lists countermodels for dropping Rc, the shared N, and positivity,
  and none for Rt. The finding is consistent with that gap.
- **NEW** (N4.4): relT is independent of the other four clauses.
- **ELABORATING**: N2, N3, the Lop-injectivity failure, and the d=2 frame+relT witness.
- **Assumption-watch markers.**
  - "A landed proof reads hypothesis X" is not the same as "X is load-bearing". A step-consumption table records use,
    not necessity, so each claim needs a drop-X countermodel or a drop-X proof.
  - relC is not closed under `G ↦ G⁻¹` (GateRel is). Arguments that switch to `G.symm` need to be checked for this.

## Open gaps

1. Nothing here is kernel-checked. Every "written" row needs a Lean proof (see below).
2. Whether relT holds for the normalized gate under relC + frame + P±.
3. Whether posFwd or posInv alone suffices (unchanged from ODD-CHAR-1). The N4 proof uses both: posInv enters through
   `lor_Minv` and `Mfwd_Minv`.
4. Even `d` with frame + relT + P± (dropping relC): only one gate was tested.
5. The exact computations cover diagonal NOTs only. General NOTs are covered by the written proof alone.

## What a later governed round could freeze (suggestion only)

- **Q-RELC-PAR.**
  - Statement: `finrank_plus_eq_finrank_minus_relC` and `not_even_of_relC`, from `IsNot (eball d) z N` and relC.
  - Kernel route: package `actC N` and `actT N` as linear maps; `G` restricts to an equivalence from
    `ker(actC − 1)` onto `ker(actC∘actT − 1)`; dimensions `n·P` (landed `finrank_ker_eq_of_pointwise`) and `P² + Q²`
    (restriction iso to `End(E₊) × End(E₋)`, using the same lemma twice).
  - Controls: `cnot`, `gJ5`, `cnot1` satisfy relC; countercontrol: d=2 `swapgate` (frame + relT, ¬relC).
- **Q-RELC-D3.** d=3 corollaries over relC, plus `¬relC` for `refl3` and `negId3`.
- **Q-RELC-SEL.**
  - Statement: `dim_of_ctrlGate` and `three_of_ctrlGate` over `CtrlGate` (frame, posFwd, posInv, relC).
  - Route: restate the untainted §Q lemmas over `CtrlGate` in a new module, which avoids editing DIM-1. Add
    `phi_minus_eq_zero` and `rows_mem_plus` in place of L2668.
  - Countercontrol: `KG` (frame + relC, with the exact posFwd witness −2/5).
- **Q-RELT-INDEP.** `CtrlGate (eball 3) z3 nflip cnotR ∧ ¬relT`.
- Any such round would also have to update the Lean–manuscript census registry for a strengthened selector (§A.35).
  Whether to do so is the owner's call; nothing here is adopted.
