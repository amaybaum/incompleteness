# Reconstruction round KT4-PREM-1 — premise audit of the Pauli-free four-copy theorem: countermodels hypothesis by hypothesis, the pair-level completion and action route, and the source map: RESULT

Run under `AGENTS.md` §A.39 as a native round, in one pull request, #<PR>.

- **`D`** — `bcbc516fe78eb7aa303a41e7bc9cc106dd63bd58`, the head of `main` after round RELC-SELECT-1 landed, certified
  by push run 37755552123.
- **`F`** — `<F>`, single parent `D`; `delta(D, F)` is the preregistration alone, blob `<PREREG_BLOB>`. Its exact-head
  `workflow_dispatch` run <F_RUN> is its `check-run` attestation; the owner designated `F` in comment <F_COMMENT>. That
  run attests the control plane only.
- **Shape** — non-sealing; stages C1 (`<C1>`, `controls.py` blob `<CONTROLS_BLOB>`), S1 (`<S1>`, the probe and the
  workflow edit) and this note (S2).

**Outcome:** `KT4-PREM-1-READ`

The audited theorem is `OIBridge.FourCopy.kt4_forward_ie1` of the design module `FourCopyHeadline` at
`ff9c3a358c57ce938978f15f2915d2145ae7b4a5`: for four pair cones `K_p ⊆ W 3` (`p = 01, 23, 02, 13`), the hypotheses
`hcls` (N-CLASS gates), `hadm` (each `K_p` contains the product states, lies in `maxCone (eball 3)` and is a convex
cone), `hcl` (each `K_p` is closed), `hgate` (each `N_p` maps `K_p` into itself) and `H` (a `KT4Core` structure) give
the conclusion `C`: IE1 at every pair and `EvenCycle` of the orientation bits. Every statement below about a model is a
statement about that hypothesis list and that conclusion. Check ids in brackets are those of
`verification/lean/kt4_prem1_probe.py`; a bracketed `W` marks a written step, printed by the probe as a
`NOTE [written]` line beside the checks it rests on.

## The cells

**Q1-CL: CLOSEDNESS-FOIL-VERIFIED.** The closedness foil `M_cl` takes at every pair the cone
`K_cl = int Q3 ∪ (SEP + cnot SEP)`, where `SEP` is the convex cone of the product states, with `N_p = cnot` and every
local the identity.

| clause | in `M_cl` | evidence |
|---|---|---|
| `hcls` | holds | `cnot` is its own N-CLASS form with identity locals [M_cl.1] |
| `hadm` | holds | the product states lie in `SEP`; `K_cl ⊆ Q3 ⊆ maxCone` through the dictionary [D1–D6]; a positive definite table plus a positive semidefinite one is positive definite, so `K_cl` is a convex cone [W M_cl.2] |
| `hgate` | holds | `cnot` is conjugation by a unitary [D1] and an involution [D2]; the inverse gate preserves `K_cl` as well [W M_cl.3] |
| `H` | holds | `cl K_cl = Q3`, so the dual cones agree [W M_cl.4]; FCC for uniform `Q3` [F0–F3, F2v, F2s with the Kronecker product of positive semidefinite matrices]; the explicit carrier [H1–H10] |
| `hcl` | fails | `T_ψ = actT R_H phiW` is a normalized rank-one state [M_cl.5–M_cl.7] in the closure of `int Q3` [M_cl.8]; it and `cnot T_ψ` have table rank 4 [M_cl.9], so `T_ψ ∉ SEP + cnot SEP` by extremality of pure states [W M_cl.9W]; rank-test control [M_cl.10] |
| IE1 | fails | `phiW ∈ K_cl` [M_cl.11] and its image `T_ψ` under `actT R_H` is not in `K_cl` [W M_cl.11W] |
| `EvenCycle` | holds | every orientation bit is false [M_cl.12] |

`M_cl` is a model of `hcls ∧ hadm ∧ hgate ∧ H ∧ ¬C`: it refutes `hcls ∧ hadm ∧ hgate ∧ H ⇒ C`, so `hcl` cannot be
dropped from the theorem. Since the inverse gate also preserves `K_cl`, a two-sided gate clause does not take the place
of closedness.

**Q1-MAX: MAXCONE-MODEL-VERIFIED.** The maximal-cone model `M_max` takes `maxCone (eball 3)` at every pair, with
`N_p = cnot` and identity locals.

| clause | in `M_max` | evidence |
|---|---|---|
| `hcls` | holds | as in `M_cl` |
| `hadm` | holds | the product-state values factor [M_max.2; landed `prodState_mem_maxCone`]; the pairing is bilinear [W M_max.2W] |
| `hcl` | holds | an intersection of closed half-spaces [W M_max.2W] |
| `H` | holds | FCC for uniform `maxCone` [F4, F5, F6 and the self-duality of the Lorentz cone]; the explicit carrier [H1–H10]; control: an effect outside the product form of the dual gives `−2` [X6] |
| IE1 | holds | rotation covariance of the pairing [M_max.6; W M_max.6W] |
| `EvenCycle` | holds | every orientation bit is false |
| `hgate` | fails | `idW ∈ maxCone` [M_max.3, F6]; `cnot idW = chainW` takes `−1/2` at the sharp effects of `−e1, −e3` [M_max.4; landed `cnot_idW`, `chain_value`] |

`M_max` is a model of `hcls ∧ hadm ∧ hcl ∧ H ∧ C ∧ ¬hgate`: it refutes `hcls ∧ hadm ∧ hcl ∧ H ∧ C ⇒ hgate`, so `hgate`
is not necessary relative to the other hypotheses and the conclusion. It does not show that the theorem holds without
`hgate`: the model `M_D` of Q1-MAP refutes `hcls ∧ hadm ∧ hcl ∧ H ⇒ C`.

**Q1-MAP: COUNTERMODEL-MATRIX-VERIFIED.** Every model uses `N_p = cnot` and identity locals unless its row says
otherwise; ✓ marks a clause that holds, ✗ one that fails.

| model | cones and data | `hcls` | `hadm` | `hcl` | `hgate` | `H` | IE1 | `EvenCycle` | evidence |
|---|---|---|---|---|---|---|---|---|---|
| `M_Q` | uniform `Q3` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | [D1–D7, F0–F3, H1–H10] |
| `M_D` | uniform `Q3`; `N_13 = actT reflY ∘ cnot`, `B_13 = reflY` | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | [M_D.1, M_D.2] |
| `M_refl` | uniform `Q3`; `A_13 = reflY`, `N_13 = cnot` | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | [M_refl.1] |
| `M_id` | uniform `Q3`; `N_p = id` | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | [M_id.1; W M_id.1W] |
| `M_class` | the cone of the four products `prodState (s z3) (t z3)` | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | [M_class.1–M_class.4] |
| `M_mix` | the ray of `E00` | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | [M_mix.1] |
| `M_int` | uniform `int maxCone ∪ Q3` | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | [M_int.1, M_int.2] |
| `M_tok` | `(Q3, Q3, Q3, twin)`; `N_13 = actT reflY ∘ cnot ∘ actT reflY`, `B_13 = B'_13 = reflY`; anchor carrier | ✓ | ✓ | ✓ | ✓ | all fields but `tokA`, `tokB` | ✓ | ✗ | [T1–T4, F10, X5] |
| `M_tokC` | uniform `Q3`; anchor carrier | ✓ | ✓ | ✓ | ✓ | all fields but `tokA` | ✓ | ✓ | [T1–T3] |

The implications, one per model:

- `M_D` refutes `hcls ∧ hadm ∧ hcl ∧ H ⇒ C`: `hgate` cannot be dropped.
- `M_refl` refutes `hadm ∧ hcl ∧ hgate ∧ H ⇒ C`: `hcls` cannot be dropped.
- `M_class` refutes `hcls ∧ hcl ∧ hgate ∧ H ⇒ C`: `hadm` cannot be dropped; the clause that fails is that every product
  state lies in `K`.
- `M_tok` refutes `hcls ∧ hadm ∧ hcl ∧ hgate ∧ (H without tokA, tokB) ⇒ C`: the token clauses cannot be dropped. FCC
  fails for these cones, at the value `−1/8` [F10], so by Lemma B1 no carrier carries `KT4Core` for them.
- `M_id` refutes `hadm ∧ hcl ∧ hgate ∧ H ∧ C ⇒ hcls`: `hcls` is not necessary.
- `M_mix` refutes `hcls ∧ hcl ∧ hgate ∧ H ∧ C ⇒ hadm`: `hadm` is not necessary; the cone `{0}` is a degenerate model
  of the same kind.
- `M_tokC` refutes `hcls ∧ hadm ∧ hcl ∧ hgate ∧ (H without tokA, tokB) ∧ C ⇒ tokA ∧ tokB` for the given carrier data:
  the token clauses of a given carrier are not necessary. Under `hadm`, whether some carrier carries `KT4Core` is FCC
  (below).
- `M_int` refutes `hcls ∧ hadm ∧ H ∧ C ⇒ hcl`: an argument that `hcl` is necessary has to use `hgate`.

**The carrier and `H ⟺ FCC`.** `H` is checked in the models through one explicit carrier, `V = ℝ^{17×17} × ℝ^{17×17}`
with `stA x y = (x̂ŷᵀ, 0)` and `stB x y = (0, x̂ŷᵀ)`, `x̂ = (1, x)`. Its evaluation laws, bilinearity and both token
clauses at all 256 index quadruples are exact identities [H1–H5]; its cross values are the four-copy contractions of
FCC [H6–H9]; an effect on a pair body is its table on the normalized slice [H10]. With the written step [W H.W], FCC,
the `maxCone` bound and nonnegative scaling give every field of `KT4Core` on `V`. With Lemma B1 of the design modules
(`fourCopyCoherent_of_kt4Core`, kernel-checked in the design run, not certified), this gives `H ⟺ FCC` relative to
`hadm`, each direction by its own argument. The countercontrol [X2] shows that a carrier reading the `02|13` state in
the `01|23` order fails `tokB`.

**Q1-NEC: CLASSIFICATION-STEPS-VERIFIED.** The written classification: `hcls ∧ hadm ∧ hgate ∧ IE1` give
`K_p ∈ {Q3, twin}` at every pair, hence `hcl`; `H` is not used. Its finite steps hold exactly:

- the full reflection `actC reflY ∘ actT reflY` commutes with `cnot` [C1];
- each of the sixteen reflection-pattern gates is a signed permutation of the sixteen entries, of finite order [C2];
- a mixed pattern sends `prodState xplus z3` to `idW` and `idW` to `chainW`, outside `maxCone` [C3, M_max.4], so no
  admissible cone is invariant under it;
- the full reflection acts on the Pauli side as the transpose, and `actT reflY` as the partial transpose, whose image of
  `Q3` is the twin [C4];
- `CNOT (I ⊗ Z) CNOT† = Z ⊗ Z` [C5];
- the real Lie algebra generated by `i σ_k ⊗ I`, `i I ⊗ σ_k` and `i Z ⊗ Z` has dimension 15 [C6].

The step from the generated Lie algebra to the generated group (the subgroup generated by one-parameter subgroups is
the connected Lie subgroup of the generated algebra) is a standard result of Lie theory and is not checked. The
argument [W C.W] makes `hcl` necessary relative to `hcls`, `hadm`, `hgate` and the conclusion; it is a written argument
and it is not kernel-checked. It identifies each pair cone relative to these hypotheses and no others.

**Q2: PAIR-ROUTE-GAP-VERIFIED.** `D` implies neither closedness nor gate preservation for a composite of two balls.

- The normalized slice of `K_cl` satisfies the four normalization values of COMP-1's coordinate model [I1; control X4];
  with `lt` by the argument of the landed `minComposite` and `maxComposite` (`prodEff_eq_of_eff_eq` with
  `modelData_ext`), it is a `Composite` whose body is not closed [M_cl.7–M_cl.9] and which `cnot` preserves [W I1W].
- `cnot` preserves neither landed instance: the functional `w00 − w11 + w22 − w33` is nonnegative on the products and
  `−2` at `phiW = cnot (prodState xplus z3)`, so `cnot` leaves the body of `ball3MinComposite` [I2]; `idW` lies in the
  body of `ball3MaxComposite` and `cnot idW` does not [M_max.3, M_max.4].
- The landed completion layer is typed for one directed system of stages: `StageCompletion.body` is the closed convex
  hull of the preparation vectors (`body_isClosed`), and an operation datum with an inverse datum induces a
  body-preserving equivalence of the chart (`preservesBody_inducedEquiv`). The only `DirectedStages` definitions at `D`
  are `badD`, `bitTower` and `midD`, each a system of one copy's stages, and COMP-1's module header places the
  stage-level product of two `DirectedStages` outside that module.

A pair-level route therefore needs two premises that `D` does not state:

- **P-STAGE2** — the pair system as a directed system whose completion has a chart onto `W 3` with chart body the
  normalized slice of `K_p`. It gives `hcl` through `body_isClosed`. It presupposes the pair's local tomography, which
  `W 3` encodes, and so the open composite obligation K2.
- **P-ACT2** — the gate `N_p` as an operation datum on that system with an inverse datum, inducing `N_p` on the chart.
  It gives `hgate` through `preservesBody_inducedEquiv`. An operation datum carries each preparation into the completed
  body (`OpDatum.mem_body`), so P-ACT2 states gate preservation on preparations; it does not derive it.

Idle extension does not supply P-ACT2's datum: for local rotations, idle extension of one-copy data to the pair cone is
IE1 itself, and for `reflY` it fails on every `cnot`-invariant candidate cone (`no_candidateCone_cnot_reflY`).

**Q3: SOURCE-MAP-CITATIONS-VERIFIED.** Every declaration of the frozen citation list resolves at `D` in its frozen file.

| hypothesis | what `D` supplies | what a route still needs | exact countermodels |
|---|---|---|---|
| `hcls` | `nativeGate_cnot`: `cnot` meets DIM-1's native-gate hypotheses at `d = 3`; `CtrlGate`, `dim_of_ctrlGate`, `three_of_ctrlGate`: the dimension selector without the target relation | a classification of control gates at `d = 3` as N-CLASS, which `D` does not contain; its inputs `IsNot`, `CtrlGate` and the entangling clause are open premises of ROADMAP row K1 | `M_refl` (cannot be dropped), `M_id` (not necessary) |
| `hadm` | `prodState_mem_maxCone`; COMP-1's `PreComposite`, `subset_maxBody`; K2-GUARD-1's `CandidateCone` | the pair system as a pre-composite in the coordinate model `W 3`, which presupposes the open composite obligation K2 | `M_class` (cannot be dropped), `M_mix` (not necessary) |
| token clauses, `H` | no statement with three or more tokens | under `hadm`, `H ⟺ FCC`: a composition principle for four copies that gives FCC | `M_tok` (cannot be dropped), `M_tokC` (not necessary for given data); FCC fails for `(Q3, Q3, Q3, twin)` [F10] |
| `hcl` | `body_isClosed`, for one system | P-STAGE2 | `M_cl` (cannot be dropped), `M_int` (necessity needs `hgate`) |
| `hgate` | `preservesBody_inducedEquiv`, for one system | P-ACT2, which restates gate preservation | `M_D` (cannot be dropped), `M_max` (not necessary) |

## The dependency map

**Proved consequences.**

- Kernel-checked in a design run, not certified: `kt4_forward_ie1`, `hcls ∧ hadm ∧ hcl ∧ hgate ∧ H ⇒ C`; Lemma B1,
  `H ∧ hadm ⇒ FCC`; Lemma R, `hcls ∧ hcl ∧ hgate ⇒` the inverse-gate clause; `hadm ∧ hcl ⇒` the bidual identity.
- Exact identities with written steps: `FCC ∧ hadm ⇒ H` on the explicit carrier, so `H ⟺ FCC` relative to `hadm`.
- Written, with one standard input from Lie theory and exact finite steps: `hcls ∧ hadm ∧ hgate ∧ IE1 ⇒ K_p ∈ {Q3, twin}`,
  hence `hcl`.
- Certified on `D`: a completed body of one directed system is closed, and an operation datum with an inverse datum
  preserves it.

**Premises with an independent source on `D`.** None of the five hypotheses. Each has landed supporting facts, listed in
Q3's second column.

**Additional assumptions the theorem needs.** Each fails in a model of the pair-level interface at `D` (Q1, Q2):
`hcls` (N-CLASS gates); `hadm` (the pair system as a coordinate-model pre-composite); `hcl` (P-STAGE2 or another
closure principle); `hgate` (P-ACT2, gate preservation in any phrasing); `H`, equivalently FCC.

**Open questions.**

1. A weaker replacement for `hgate`. `hgate` is not necessary (`M_max`) and cannot be dropped (`M_D`). The proof uses
   it at product states (`bell_mem`, `link_mem`) and, through Lemma R, for the inverse gate (`bell_mem_dual`,
   `parity_witnesses`). Whether a clause stated at product states, with the Bell table in the dual of `K_p`, suffices
   is not tested here.
2. A source for FCC in a composition principle for four copies.
3. The stage-level product of two directed systems and its identification with `W 3`, which COMP-1 leaves open and K2
   requires.
4. Kernel verification of `M_cl`, `M_max` and the classification argument, which needs the four-copy vocabulary on
   `main`.

## The earned reading

> The hypothesis hcl cannot be dropped from the Pauli-free four-copy theorem: the closedness foil satisfies hcls, hadm,
> hgate and H and fails IE1. The hypothesis hgate is not necessary relative to hcls, hadm, hcl, H and the conclusion:
> the maximal-cone model satisfies all of them and fails hgate; this does not show that hgate can be removed, and the
> D-gate model refutes the implication without it. Each of hcls, hadm, hgate and the token clauses cannot be dropped,
> and each of hcls, hadm and the token clauses of the given data is not necessary, by the models of the matrix. Under
> hadm, H is equivalent to the cone-level interface FCC, one direction by Lemma B1 of the design modules and the other
> by an explicit carrier. Certified main supplies neither closedness nor gate preservation for a composite of two
> balls; a pair-level completion supplies closedness only from a new premise, and gate preservation only from a
> premise that states it on preparations.

## The non-inference rule

> This round adopts no premise, sources none of the five hypotheses, and makes no manuscript claim and no ROADMAP claim.
> Its countermodels are models of the hypothesis sets they are stated for and of nothing more; none is a physical
> theory. The necessity of hcl relative to hcls, hadm, hgate and the conclusion rests on a written argument with one
> standard input from Lie theory and is not kernel-checked; the probe checks its finite steps only. The audited
> theorem is kernel-checked in a design run and is not certified. Nothing here says that the observational axioms force
> quantum cones: the classification of a pair cone as Q3 or its twin holds relative to N-CLASS gates, admissible cones,
> gate preservation and IE1, none of which is sourced.

## Evidence

- The probe, blob `5609d96a9886d5d8548c0322e084849e700ba72b`, run by `controls.py` at this commit and in the
  KT4-PREM-1 shard of the exact-head run at this commit, prints 79 `PASS` lines and no `FAIL` line, and ends:

  ```
  kt4_prem1_probe: OK -- 79 checks
  ```

  Its checks by kind: 38 identities, 21 witnesses, 3 enumerations, 7 transcription checks against the landed tables,
  2 samples and 8 countercontrols.
- `controls.py check <E> --freeze <F>` prints `controls: OK -- <N> checks`; `controls.py verdict <E>` prints the six
  outcomes above.
- The exact-head run at this commit, run <E_RUN>, <E_RUN_RESULT>.

Correctness bands are unchanged: the round is consistency-axis work.
