# Premise audit of the Pauli-free four-copy theorem: dependency map (design)

**Status.** Design document on the disposable branch `claude/network-tool-access-8jtdhm`. It is not a governed record,
adopts no premise, and changes no manuscript and no ROADMAP row. The base for every statement about what the framework
supplies is certified `main` at `bcbc516f`. The audited theorem exists only at the design commit `ff9c3a35` on this
branch. The exact checks cited as `[X …]` are those of `verification/lean/kt4_prem1_probe.py`.

## 1. The audited statement

`OIBridge.FourCopy.kt4_forward_ie1` (`FourCopyHeadline.lean` at `ff9c3a35`) takes four pair cones `K_p ⊆ W 3`
(`p = 01, 23, 02, 13`), gates `N_p`, one-copy linear maps `A_p, B_p, A'_p, B'_p`, and five hypotheses:

| name | statement |
|---|---|
| `hcls` | `N_p = actC A_p ∘ actT B_p ∘ cnot ∘ actC A'_p ∘ actT B'_p`, the four maps orthogonal (N-CLASS) |
| `hadm` | `K_p` contains `prodState x y` for all `x, y ∈ eball 3`, lies in `maxCone (eball 3)`, and is a convex cone |
| `hcl` | `K_p` is closed |
| `hgate` | `N_p` maps `K_p` into `K_p` |
| `H` | a `KT4Core` structure on `(K_01, K_23, K_02, K_13)` over a real normed carrier `V` |

Its conclusion `C` is: every `K_p` is invariant under `actC R` and `actT R` for every rotation `R` (IE₁), and the
number of pairs with `det A_p · det B_p = −1` is even (`EvenCycle`).

The proof (`kt4_general_ie1`) uses `H` once, through Lemma B1 (`fourCopyCoherent_of_kt4Core`), to obtain the cone-level
interface FCC (`FourCopyCoherent`); B1 also reads the maxCone bound and the scaling clause of `hadm`. It derives the
inverse-gate clause from `hcls`, `hcl` and `hgate` (Lemma R, `inv_mem_of_orth`) and the bidual identity
`dualW (dualW K_p) = K_p` from `hadm` and `hcl` (`bidual_of_adm`).

Kernel status: in design run 37948419430 at `ff9c3a35`, `#print axioms kt4_forward_ie1` reports
`[propext, Classical.choice, Quot.sound]`. The run's release gate failed on modules off this theorem's dependency
closure (the unstarted Pauli stage and the unregistered census families), so the theorem is kernel-checked in a
design run and is not certified.

## 2. Verification layers

- **[K]** kernel-checked and certified on `main` at `bcbc516f` (declaration named).
- **[K-design]** kernel-checked in the design run at `ff9c3a35`; not certified.
- **[X]** an exact check of `kt4_prem1_probe.py` (check id): a symbolic identity, an exact witness, an exhaustive
  enumeration, a transcription check, a sample, or a countercontrol, as the probe labels it.
- **[W]** a written argument, given here or in the probe's `NOTE [written]` lines.
- **[L]** a standard published result, named where used.

The layers are not interchangeable: an [X] identity together with a [W] step is not a kernel proof.

## 3. The countermodels (Q1)

Every model uses `N_p = cnot` and identity locals unless the row says otherwise. "✓" means the hypothesis holds in the
model, "✗" that it fails.

| model | cones | `hcls` | `hadm` | `hcl` | `hgate` | `H` | IE₁ | `EvenCycle` |
|---|---|---|---|---|---|---|---|---|
| `M_Q` | uniform `Q3` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `M_cl` | uniform `int Q3 ∪ (SEP + cnot SEP)` | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| `M_max` | uniform `maxCone (eball 3)` | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| `M_D` | uniform `Q3`; `N_13 = actT reflY ∘ cnot`, `B_13 = reflY` | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ |
| `M_refl` | uniform `Q3`; `A_13 = reflY`, `N_13 = cnot` | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| `M_id` | uniform `Q3`; `N_p = id` | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `M_class` | the cone of the four products `prodState (s z3) (t z3)` | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ |
| `M_mix` | the ray of `E00` (the maximally mixed table) | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `M_int` | uniform `int maxCone ∪ Q3` | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ |
| `M_tok` | `(Q3, Q3, Q3, twin)`; `N_13 = cnotTw`, `B_13 = B'_13 = reflY`; anchor carrier | ✓ | ✓ | ✓ | ✓ | all fields but `tok` | ✓ | ✗ |
| `M_tokC` | uniform `Q3`; anchor carrier | ✓ | ✓ | ✓ | ✓ | all fields but `tok` | ✓ | ✓ |

### 3.1 The carrier for `H`

`H` is verified in every model through one explicit carrier, `V = ℝ^{17×17} × ℝ^{17×17}` (probe §S2):
`stA x y = (x̂ ŷᵀ, 0)`, `stB x y = (0, x̂ ŷᵀ)` with `x̂ = (1, x)`, and product effects that read the other grouping's
states through the four-copy contraction.

- The evaluation laws, bilinearity, and both token clauses, all 256 index quadruples each, are exact identities
  [X H1–H5].
- The cross values are the four-copy contractions of FCC [X H6–H9]. An effect on a pair body is its table on the
  normalized slice [X H10].
- Hence FCC, the maxCone bound and nonnegative scaling of the four cones give every field of `KT4Core` on this `V`
  [X + W, note H.W].

With Lemma B1 [K-design] this gives **`H ⟺ FCC` relative to `hadm`**, each direction by its own named argument.
The cone-level content of `H` is FCC.

### 3.2 `M_cl` (the closedness foil), hypothesis by hypothesis

| clause | status | evidence |
|---|---|---|
| `hcls` | holds | `actC I = actT I = id`, so `cnot` is its own N-CLASS form [X M_cl.1] |
| `hadm` | holds | products lie in `SEP`. `K_cl ⊆ Q3 ⊆ maxCone`: `pauliW (prodState x y) = ρ(x) ⊗ ρ(y)` [X D5], `cnot = Ad(CNOT)` [X D1], `pairVal a b w = tr((opV a ⊗ opV b) pauliW w)` with `opV a ⪰ 0 ⟺ a ∈ L` [X D4, D6]. Convex cone: positive definite plus positive semidefinite is positive definite [W M_cl.2] |
| `hgate` | holds | `cnot` is conjugation by a unitary, so it preserves `int Q3`, and it is an involution [X D1, D2; W M_cl.3]. The inverse gate also preserves `K_cl` |
| `H` | holds | `cl K_cl = Q3`, so `dualW K_cl = dualW Q3` [W M_cl.4]. FCC for uniform `Q3` [X F2, F3 + W/L F.Q3: the Kronecker product of positive semidefinite matrices is positive semidefinite, e.g. Mathlib `Matrix.PosSemidef.kronecker`]. Then the carrier of §3.1 applies |
| `hcl` | **fails** | `T_ψ = actT R_H phiW` is a normalized rank-one state [X M_cl.6, M_cl.7] in `cl int Q3` [X M_cl.8]. Its table rank and that of `cnot T_ψ` are both 4 [X M_cl.9], so by pure-state extremality `T_ψ ∉ SEP + cnot SEP` [W M_cl.9W]. Rank-test control [X M_cl.10] |
| IE₁ | **fails** | `phiW = cnot (prodState xplus z3) ∈ K_cl` [X M_cl.11], while its rotated image `T_ψ ∉ K_cl` |
| `EvenCycle` | holds | every orientation bit is false [X M_cl.12] |

**Implication established.** `M_cl` is a model of `hcls ∧ hadm ∧ hgate ∧ H ∧ ¬C`, so it refutes
`hcls ∧ hadm ∧ hgate ∧ H ⇒ C`: **`hcl` cannot be dropped** from the theorem. `M_cl` also satisfies the two-sided gate
clause, so the inverse-gate clause does not substitute for closedness.

### 3.3 `M_max` (uniform maxCone), hypothesis by hypothesis

| clause | status | evidence |
|---|---|---|
| `hcls` | holds | as in `M_cl` |
| `hadm` | holds | `pairVal a b (prodState x y) = (a·x̂)(b·ŷ)` [X M_max.2; K `prodState_mem_maxCone`]. maxCone is a convex cone [W] |
| `hcl` | holds | it is an intersection of closed half-spaces [W] |
| `H` | holds | FCC for uniform maxCone: `fourVal X Y E F = ipW E (X F Yᵀ)` [X H8], `aᵀ(X F Yᵀ)b = ipW F ((Xᵀa)(Yᵀb)ᵀ)` [X F4], `pairVal a b (u vᵀ) = (a·u)(b·v)` [X F5], and self-duality of the Lorentz cone by Cauchy–Schwarz [X F6 + W F.max]. Then the carrier of §3.1 applies. Control: effects outside `dualW maxCone` give `−2` [X X6] |
| IE₁ | holds | `pairVal a b (actC R w) = pairVal (homMap Rᵀ a) b w`, and likewise for `actT` [X M_max.6]; `homMap Rᵀ` preserves `L` [W] |
| `EvenCycle` | holds | every orientation bit is false |
| `hgate` | **fails** | `idW ∈ maxCone` [X M_max.3 + F6]; `cnot idW = chainW` [K `cnot_idW`], which takes `−1/2` at the sharp effects of `−e₁, −e₃` [K `chain_value`; X M_max.4] |

**Implication established.** `M_max` is a model of `hcls ∧ hadm ∧ hcl ∧ H ∧ C ∧ ¬hgate`, so it refutes
`hcls ∧ hadm ∧ hcl ∧ H ∧ C ⇒ hgate`: **`hgate` is not necessary** relative to the other hypotheses and the conclusion.

It does **not** show that `hgate` can be removed from the theorem. `M_D` refutes `hcls ∧ hadm ∧ hcl ∧ H ⇒ C`.

### 3.4 The implications, one line each (P/A/C)

- `M_cl` refutes `hcls ∧ hadm ∧ hgate ∧ H ⇒ C`: `hcl` cannot be dropped.
- `M_D` refutes `hcls ∧ hadm ∧ hcl ∧ H ⇒ C`: `hgate` cannot be dropped [X M_D.1, M_D.2].
- `M_refl` refutes `hadm ∧ hcl ∧ hgate ∧ H ⇒ C`: `hcls` cannot be dropped [X M_refl.1].
- `M_class` refutes `hcls ∧ hcl ∧ hgate ∧ H ⇒ C`: `hadm` cannot be dropped; the failing clause is "every product lies
  in `K`" [X M_class.1–4].
- `M_tok` refutes `hcls ∧ hadm ∧ hcl ∧ hgate ∧ (H without tok) ⇒ C`: the token clauses cannot be dropped
  [X T1–T4, F10]. FCC fails for these cones (value `−1/8`), so by B1 no carrier carries `KT4Core` for them.
- `M_max` refutes `hcls ∧ hadm ∧ hcl ∧ H ∧ C ⇒ hgate`: `hgate` is not necessary.
- `M_id` refutes `hadm ∧ hcl ∧ hgate ∧ H ∧ C ⇒ hcls`: `hcls` is not necessary. No choice of orthogonal locals makes
  `id` N-CLASS [X M_id.1 + W].
- `M_mix` refutes `hcls ∧ hcl ∧ hgate ∧ H ∧ C ⇒ hadm`: `hadm` is not necessary [X M_mix.1].
- `M_tokC` refutes `hcls ∧ hadm ∧ hcl ∧ hgate ∧ (H without tok) ∧ C ⇒ tok`: the token clauses of the given data are not
  necessary [X T3].
- `M_int` refutes `hcls ∧ hadm ∧ H ∧ C ⇒ hcl` [X M_int.1, M_int.2]. Any proof that `hcl` is necessary must use `hgate`.
- **Written proof [W + L; finite steps X C1–C6]:** `hcls ∧ hadm ∧ hgate ∧ IE₁ ⇒ K_p ∈ {Q3, twin}`, hence `⇒ hcl`.
  So `hcl` is necessary relative to `hcls`, `hadm`, `hgate` and the conclusion (`H` is not used).
  - The literature input is one standard fact of Lie theory: the subgroup generated by one-parameter subgroups is the
    connected subgroup of the generated Lie algebra. That algebra is computed exactly to be `su(4)` [X C6].
  - The argument is not kernel-checked.
  - It identifies each pair cone relative to these hypotheses only.

## 4. The pair-level completion and action route (Q2)

**Question.** Does certified `main` imply closedness (`hcl`) or gate preservation (`hgate`) for composite systems?

**Answer: no, for either.**

- **Closedness is not implied.** The normalized slice of `K_cl` satisfies every field of COMP-1's `PreComposite` over
  the coordinate model.
  - The fields hold by [X I1] and [W I1W]. `lt` holds by the argument of the landed `minComposite` and
    `maxComposite`: `prodEff_eq_of_eff_eq` with `modelData_ext` [K].
  - So it is a `Composite`. Its body is not closed [X M_cl.7–M_cl.9], it is not invariant under local rotations, and
    `cnot` preserves it.
  - It is also a `CandidateCone` in the sense of K2-GUARD-1.
- **Gate preservation is not implied.** The landed instances `ball3MinComposite` and `ball3MaxComposite` [K] are
  composites whose bodies `cnot` does not preserve.
  - `cnot (prodState xplus z3) = phiW` [K `cnot_prodState_xplus_z3`] lies outside the minimal body: the functional
    `w₀₀ − w₁₁ + w₂₂ − w₃₃` is nonnegative on products and equals `−2` at `phiW` [X I2].
  - `idW` lies in the maximal body while `cnot idW` does not [X M_max.3, M_max.4; K `cnot_idW`, `chain_value`].
- **The completion layer is typed for one system.** On `main`:
  - a completed body is closed by definition [K `body_isClosed`];
  - an operation datum with an inverse datum induces a body-preserving affine equivalence of the chart
    [K `preservesBody_inducedEquiv`].
  - Both are stated for one `DirectedStages`. The landed directed systems are `badD` and `bitTower`
    (`StageCompletion`) and `midD` (`CompletionAction`), each a system of one copy's stages.
  - COMP-1's module header excludes the stage-level product of two `DirectedStages`.
  - No landed declaration builds a directed system for a pair, an operation datum for a pair gate, or a map from `W 3`
    to a completion chart.

**What the route would need.** These are additional assumptions, named so that neither silently contains `hgate` or
idle extension.

- **P-STAGE2.** The pair system is a directed system whose completion has a chart onto `W 3` with chart body the
  normalized slice of `K_p`.
  - It gives `hcl`: `body_isClosed` [K], and the chart body is the preimage of a closed set under a continuous chart
    [W].
  - It presupposes local tomography of the pair, which `W 3` encodes. Composite existence and local tomography are K2,
    which is OPEN.
- **P-ACT2.** The gate `N_p` is an operation datum on that system with an inverse datum, inducing `N_p` on the chart.
  - It gives `hgate` through `preservesBody_inducedEquiv` [K].
  - An operation datum carries each preparation into the completed body (`OpDatum.mem_body`). P-ACT2 therefore
    **states** gate preservation on preparations; it does not derive it.
- **Idle extension is not available as a source.**
  - Building the datum for `N_p = actC A ∘ actT B ∘ cnot ∘ actC A' ∘ actT B'` from one-copy data would need the local
    maps to extend idly to the pair.
  - For rotations, idle extension to the pair cone is IE₁ itself, the theorem's conclusion.
  - For `reflY`, idle extension is refuted on every `cnot`-invariant candidate cone [K `no_candidateCone_cnot_reflY`].

**Conclusion of Q2.** The certified framework implies neither `hcl` nor `hgate` for composite systems. The
completion and action route supplies `hcl` from a new premise (P-STAGE2). It supplies `hgate` only from P-ACT2, which
is gate preservation restated as reversible operation data.

## 5. Source map for `hcls`, `hadm` and the token clauses (Q3)

| hypothesis | what `main` supplies [K] | route, and the principles it still needs | exact countermodels |
|---|---|---|---|
| `hcls` | `nativeGate_cnot`: `cnot` satisfies DIM-1's native-gate hypotheses at `d = 3`. `CtrlGate`, `dim_of_ctrlGate`, `three_of_ctrlGate`: the dimension selector without the target relation | a classification of `CtrlGate` gates at `d = 3` as N-CLASS (exact certificates plus a written reduction, not kernel-checked, not on `main`). Its inputs `IsNot`, `CtrlGate` and the entangling clause (or `2 ≤ d`) are unsourced (ROADMAP K1, CONDITIONAL) | `M_refl` (cannot be dropped), `M_id` (not necessary) |
| `hadm` | `prodState_mem_maxCone`. COMP-1: `PreComposite.prod_mem`, `subset_maxBody`. K2-GUARD-1: `CandidateCone` and its instances | if the pair system is a COMP-1 pre-composite in the coordinate model `W 3`, the cone over its body satisfies `hadm` [W]; that presupposes K2 (composite existence, local tomography), OPEN | `M_class` (cannot be dropped), `M_mix` (not necessary) |
| tokens / `H` | nothing with three or more tokens | under `hadm`, `H ⟺ FCC` (§3.1), so the source question is FCC: positivity of each grouping's product effects on the other grouping's product states. A four-copy composite with one body, or a composition principle for four copies, would have to supply it; neither is stated on `main` | `M_tok` (cannot be dropped), `M_tokC` (not necessary as data); FCC itself fails for `(Q3, Q3, Q3, twin)` [X F10] |
| `hcl` | `body_isClosed`, for one system | P-STAGE2 (§4) | `M_cl` (cannot be dropped), `M_int` (necessity needs `hgate`) |
| `hgate` | `preservesBody_inducedEquiv`, for one system | P-ACT2 (§4), a restatement | `M_D` (cannot be dropped), `M_max` (not necessary) |

## 6. The dependency map

**(A) Proved consequences.**
- [K-design] `kt4_forward_ie1`: `hcls ∧ hadm ∧ hcl ∧ hgate ∧ H ⇒ C`.
- [K-design] `H ∧ hadm ⇒ FCC` (Lemma B1).
- [K-design] `hcls ∧ hcl ∧ hgate ⇒` the inverse-gate clause (Lemma R).
- [K-design] `hadm ∧ hcl ⇒` the bidual identity.
- [X + W] `FCC ∧ hadm ⇒ H` on the explicit carrier, so `H ⟺ FCC` relative to `hadm`.
- [W + L; finite steps X] `hcls ∧ hadm ∧ hgate ∧ IE₁ ⇒ K_p ∈ {Q3, twin}`, hence `hcl`.
- [K] A completed body of one directed system is closed. An operation datum with an inverse datum preserves it.

**(B) Independently sourced premises.**
- None of the five hypotheses is supplied on `main`.
- Each hypothesis has supporting landed facts, listed in §5's middle column.

**(C) Additional assumptions** the theorem needs. None is derivable from `main`; each fails in a model of `main`'s
pair-level interface (§3, §4).
- `hcls`, N-CLASS gates.
- `hadm`, the pair system as a coordinate-model pre-composite.
- `hcl`, P-STAGE2 or another closure principle.
- `hgate`, P-ACT2: gate preservation, however phrased.
- `H`, equivalently FCC.

**(D) Open questions.**
1. **A weaker replacement for `hgate`.** `hgate` is not necessary (`M_max`) but cannot be dropped (`M_D`). The proof
   uses it:
   - at product states (`bell_mem`, `link_mem`);
   - through Lemma R, for the inverse gate (`bell_mem_dual`, `parity_witnesses`).

   Whether a clause stated at product states, together with the Bell table lying in `dualW K_p`, suffices is untested.
2. **A source for FCC** from a composition principle for four copies.
3. **The pair-level stage product** of two directed systems, and its identification with `W 3` (COMP-1 open; K2 open).
4. **Kernel verification** of `M_cl`, `M_max` and the classification argument. This needs the four-copy vocabulary on
   `main`.

## 7. What is not claimed

- No hypothesis is adopted. None is claimed sourced, and no route above is claimed to be a derivation.
- "Necessary" is used once, for `hcl`, relative to `hcls`, `hadm`, `hgate` and the conclusion. It rests on a written
  proof with one standard input from Lie theory, and it is not kernel-checked.
- Every countermodel is a model of the hypothesis set it is stated for, and of nothing more.
- Nothing here says that the observational axioms force quantum cones.
  - The classification in §3.4 holds relative to N-CLASS gates, admissible cones, gate preservation and IE₁.
  - None of these is sourced.
