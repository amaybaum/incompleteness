# Reconstruction round KTOKEN-MAXCONE-1 — the conditional pair-cone theorem for k tokens: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review; `F` is not designated.** It is drafted from `D`
and built from three sources:
- the landed OI-PAIR-MAXCONE-1 record (`round-oi-pair-maxcone-1/`, and `EqvK2MaxCone.lean` at `D`);
- the research design sources `FinitePauli.lean`, `FiniteReach.lean` and `FiniteReachTable.lean` of
  `research/finite-reconstruction-design-20261013` at `924dc918`. These are off main, cited as provenance only;
- the predicted execution tree built from them on the disposable branch `dev-equivalence/ktoken-maxcone`, and run at its
  exact head (*Design evidence* below).

That run is evidence for the proposed execution tree, not a `check-run` attestation of `F` or `E`. The five execution
files' blobs are frozen there. Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an instruction
to proceed is not a designation.

```v3-round
round KTOKEN-MAXCONE-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/
record AM verification/receipts/KTOKEN-MAXCONE-1.json
execution A verification/lean-mathlib/OIBridge/KTokenMaxCone.lean
execution A verification/lean/ktoken_maxcone1_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

D: b96662e6be4f537502c772db369ea32a35b213a8.
Delta(D, F) is this preregistration and any amendments in the round's `amendments/` directory. **No manuscript, built
artifact, `verification/ROADMAP.md`, landed kernel module or other round's record changes under any outcome.**

## What the round is

`pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153) gives `K = Q3` (EqvK2Schema.lean:239) for `K ⊆ W 3`. Its
hypotheses are:
- products (hH1);
- addition and nonnegative scaling (hadd, hsmul);
- `K ⊆ maxCone` (hmax);
- `cnot` invariance (hH2);
- target-token `actT (rotLin t)` and `actT cycEquiv` invariance (hA).

ROADMAP K2 (:1011–1019) lists composition beyond two tokens as open. At `D` every carrier is two-slot (`W d`,
`prodState`, `maxCone`, `actT`, `cnot`: CompositeDimension.lean:97, :161, :186, :198, :775; `dict`: EqvK2Schema.lean:78),
and no k-token type exists in the adopted library.

- **Q-INCL (kernel).** For every `k`:
  - does `K ⊆ maxConeK` with the invariance give `K ⊆ QK k`?
  - do products, cone closure and the invariance give `QK k ⊆ K`?
- **Q-EQ (kernel).** Is `K = QK k` under the six hypotheses? And, given hH1, hadd, hsmul and hmax, is it equivalent to
  the invariance, with one named kernel witness per direction (§A.34)?
- **Q-PAIR (kernel, with check A3).** At `k = 2`, through a carrier equivalence, does the k-token theorem yield the
  statement of EqvK2MaxCone.lean:153–160 with this independence?
  - without citing it, anything proved from it, or a sibling two-token theorem;
  - checked at the level of kernel terms.
- **Q-EXACT (exact layer).** At `k = 3`, do exact witnesses show:
  - each hypothesis load-bearing;
  - the CNOTs needed at every token;
  - two-token slice positivity insufficient?

## The statement surface (frozen; S1 compares the module with this block)

Module `OIBridge/KTokenMaxCone.lean`, namespace `OIBridge.KTokenMaxCone`, single import `OIBridge.EqvK2Generation`. The
block is the compiled form of the surface proposed at this round's first draft. It differs from that proposal only in
writing, not in meaning:
- adopted names are fully qualified;
- the effect family's type is written out;
- `cycEquiv` carries its coercion to a linear map;
- `k` and `K` are implicit binders.

```lean
abbrev WK (k : ℕ) := (Fin k → Fin 4) → ℝ
def prodStateK {k : ℕ} (x : Fin k → Fin 3 → ℝ) : WK k := fun μ => ∏ i, hom (x i) (μ i)
def maxConeK {k : ℕ} (Ω : Set (Fin 3 → ℝ)) : Set (WK k) :=
  {ω | ∀ e : Fin k → (Fin 3 → ℝ) →ᵃ[ℝ] ℝ,
    (∀ i, OIBridge.KInfFoundations.IsEffectOn Ω (e i)) →
      0 ≤ ∑ μ, (∏ i, ehom (e i) (μ i)) * ω μ}
noncomputable def dictK {k : ℕ} (ω : WK k) : Matrix (Fin k → Fin 2) (Fin k → Fin 2) ℂ :=
  ∑ μ, ((ω μ : ℂ) / 2 ^ k) • Matrix.of fun a b => ∏ i, pauli (μ i) (a i) (b i)
def QK (k : ℕ) : Set (WK k) := {ω | (dictK ω).PosSemidef}
def cnotK {k : ℕ} (i j : Fin k) (ω : WK k) : WK k := fun μ =>
  sgn (μ i) (μ j) * ω (Function.update (Function.update μ i (pc (μ i) (μ j))) j (pt (μ i) (μ j)))
def actK {k : ℕ} (j : Fin k) (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (ω : WK k) : WK k :=
  fun μ => homMap N (fun ν => ω (Function.update μ j ν)) (μ j)
theorem subset_QK_of_maxCone_drive {k : ℕ} {K : Set (WK k)}
    (hmax : K ⊆ maxConeK (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K)
    (hA : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
      actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
        actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    K ⊆ QK k :=
theorem QK_subset_of_products_cone_drive {k : ℕ} {K : Set (WK k)}
    (hH1 : ∀ x : Fin k → Fin 3 → ℝ, (∀ i, x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodStateK x ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hH2 : ∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K)
    (hA : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
      actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
        actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    QK k ⊆ K :=
theorem kCone_eq_QK_of_drive_maxCone {k : ℕ} {K : Set (WK k)}
    (hH1 : ∀ x : Fin k → Fin 3 → ℝ, (∀ i, x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodStateK x ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxConeK (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K)
    (hA : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
      actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
        actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    K = QK k :=
theorem driveInvariantK_of_eq_QK {k : ℕ} {K : Set (WK k)} (h : K = QK k) :
    (∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K) ∧
      ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
        actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
          actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K :=
theorem kCone_eq_QK_iff_drive_maxCone {k : ℕ} {K : Set (WK k)}
    (hH1 : ∀ x : Fin k → Fin 3 → ℝ, (∀ i, x i ∈ OIBridge.TransitiveBody.eball 3) →
      prodStateK x ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxConeK (OIBridge.TransitiveBody.eball 3)) :
    K = QK k ↔ ((∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K) ∧
      ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K,
        actK j (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
          actK j (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :=
def pairCarrierEquiv : W 3 ≃ₗ[ℝ] WK 2 where
  toFun ω := fun μ => ω (μ 0) (μ 1)
  invFun η := fun a b => η ![a, b]
  map_add' _ _ := rfl
  map_smul' _ _ := rfl
  left_inv _ := rfl
  right_inv η := funext fun μ => congrArg η (funext fun i => by fin_cases i <;> rfl)
theorem pairCone_eq_Q3_of_kToken {K : Set (W 3)}
    (hH1 : ∀ x ∈ OIBridge.TransitiveBody.eball 3, ∀ y ∈ OIBridge.TransitiveBody.eball 3,
      prodState x y ∈ K)
    (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K)
    (hmax : K ⊆ maxCone (OIBridge.TransitiveBody.eball 3))
    (hH2 : ∀ ω ∈ K, cnot ω ∈ K)
    (hA : ∀ t : ℝ, ∀ ω ∈ K, actT (OIBridge.KInfFoundations.rotLin t) ω ∈ K ∧
      actT (OIBridge.KInfFoundations.cycEquiv : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) ω ∈ K) :
    K = Q3 :=
```

The hypotheses are written out in every statement:
- H1: products of `eball 3` states are in `K`;
- H2: `cnotK i j` for `i < j`;
- A: `actK j (rotLin t)` and `actK j cycEquiv` for `(j : ℕ) ≠ 0`.

At `k = 2`, CNOT into later tokens and actions off token 0 are exactly the landed hH2 and hA.

The landed objects S2 checks at `D` are:

| Objects | Location |
|---|---|
| `hom`, `homMap`, `ehom`, `sgn`, `pc`, `pt`, `W`, `prodState`, `maxCone`, `actT`, `cnot` | CompositeDimension.lean:100, :112, :167, :741, :744, :751, :97, :161, :186, :198, :775 |
| `IsEffectOn`, `rotLin`, `cycEquiv` | KInfFoundations.lean:116, :386, :416 |
| `eball` | TransitiveBody.lean:518 |
| `pauli`, `dict`, `Q3` | EqvK2Schema.lean:25, :78, :239 |
| `bloch` | EqvK2Block.lean:190 |
| `dict_cnot_block`, `exists_unit_sqrt`, `su_euler` | EqvK2Generation.lean:204, :280, :323 |
| `tokMat_rot`, `cycMat`, `tokMat_cyc` | EqvK2Converse.lean:87, :106, :133 |
| `pairCone_eq_Q3_of_drive_maxCone` | EqvK2MaxCone.lean:153 |

The module prints 68 axiom reports, in the order frozen in `controls.py` (`PRINTS`): the 14 surface declarations' proofs
and their supporting lemmas.

**Proof route (compiled).** The proof uses exact pure-state reachability on the recursive carrier `Carrier d n`
(`Fin 1` at 0, `Carrier d n × Fin d` at `n + 1`), reindexed to `Fin k → Fin 2` and `Fin k → Fin 4` by `carrierEquiv`:
- **Multiplexors.** `sign_induction` proves that every family of diagonal rotations on a target token, controlled by all
  earlier tokens, is a word in the named generators. Addition is block multiplication, a constant is the local flow,
  and multiplication by the sign of control bit `i` is conjugation by `cnotM (n+1) i n`. No Gray schedule is used.
- **SU(2) multiplexors.** Real rotation families are cyclic conjugates of diagonal ones, and `su_euler`
  (EqvK2Generation.lean:323) gives SU(2) multiplexors branchwise.
- **Reachability.** `reach_prod` writes every vector as a word applied to (first-token vector) ⊗ |0⟩ ⊗ … ⊗ |0⟩, and the
  first token is never driven.
- **The two inclusions.** The upper inclusion uses the dual of `K`, which holds the products and the invariance and
  hence every rank-one PSD table. The lower inclusion uses pure products and cone closure, with
  `psdFactorization_discharged`.
- **Transport.** The carrier transport is `dictionary_tabOf` and `mem_QK_iff`, and the coordinate formulas are
  `tabAct_cnotM`, `tabAct_localM`, `tabAct_rotK` and `tabAct_cycK`.

The pair theorem enters only as Q-PAIR's target statement. `FiniteWalsh.lean` and `FiniteCircuit.lean`, which hold the
Gray/Walsh normal form, are not ported: the cone theorems do not use them.

**The k = 2 independence (owner decision A3).**
- **Import and absence check.** The module imports `OIBridge.EqvK2Generation`, so `OIBridge.EqvK2MaxCone` is not in its
  environment. Its `#eval`, frozen in `controls.py` (`EVAL`), fails the build if the landed pair theorem is present, and
  otherwise logs that it is absent.
- **Check A3.** `checks/KTokenPairCheck.lean` imports both modules and checks two things over kernel terms:
  - STMT-IDENTITY: `pairCone_eq_Q3_of_kToken`'s statement is alpha-equivalent to `pairCone_eq_Q3_of_drive_maxCone`'s,
    with equal binder annotations and hypothesis names;
  - DEPCHECK: the recovery's transitive used-constants closure contains none of the pair theorem, a constant proved
    from it, a constant of the module `OIBridge.EqvK2MaxCone`, or the nine frozen sibling two-token theorems; and it
    does contain `kCone_eq_QK_of_drive_maxCone` and `su_euler`.
  - The sibling list is `blockInvariant_of_drive`, `pairCone_eq_Q3_of_drive_exact` and `pairCone_eq_Q3_iff_drive_exact`
    (EqvK2Generation); `pairCone_eq_Q3_of_block` and `pairCone_eq_Q3_iff_block` (EqvK2Block);
    `pairCone_eq_Q3_of_drive`, `subset_Q3_of_pure_dual` and `Q3_subset_of_pure` (EqvK2Schema); and
    `pairCone_eq_Q3_iff_drive` (EqvK2Converse).
- **The runner.** `checks/run_checks.py` generates twelve cases from that file and compiles all thirteen in the Mathlib
  bridge job (step W1). The runner and its cases are shown below.

  | Cases | Must |
  |---|---|
  | the positive file; `M_real`, the harness control | compile, with their markers |
  | `M_direct`, `M_iff`, `M_inline`, `M_deadref`, `M_sibling`, `M_required`, the three vacuity cases, the two statement cases | fail, each with its frozen codes |

- **What A3 is and is not.** A3 is a meta-level check over kernel-checked terms, not a kernel proof. If its templates do
  not elaborate, the round falls back to the absence check alone (A1), by amendment before `F`. It never falls back to
  importing `EqvK2MaxCone` (A2).

**Mathlib** (`lakefile.toml` pins `rev = "v4.33.0"`): the cone theorems use `Matrix.PosSemidef`,
`Matrix.posSemidef_submatrix_equiv`, `Finset.prod_univ_sum` and `Fin` tuple equivalences. There is no k-fold Kronecker
product and no gate-decomposition material.

**Census family** (appended after the BG-2 family, census:1485–1492 at `D`): "conditional k-token cone theorem:
products, cone closure, the k-fold maxCone bound and CNOT plus rotation/cyclic invariance give the PSD cone of the
k-fold Pauli dictionary (round KTOKEN-MAXCONE-1, reconstruction)". It is `kernel-only`, with `manuscript: []`, and its
note is frozen in `controls.py` (`FAMILY`).

**Import line**: `import OIBridge.KTokenMaxCone`, directly after `import OIBridge.TurnpikePremiseOrientation`
(OIBridge.lean:269 at `D`).

## The exact layer (frozen probe `verification/lean/ktoken_maxcone1_probe.py`)

The probe uses only the standard library and exact Q(i), and imports nothing from the kernel or from any landed checker.

Positive checks at `k = 3`:

| Code | What it checks |
|---|---|
| DICT3 | the dictionary inverts Pauli coordinates with factor 8; real coordinates; Pauli strings Hermitian, involutive, trace-orthogonal |
| PRODUCT3 | products are PSD of rank 1, 2, 4, 8 |
| REACH3 | the recursion rebuilds `x` and `x x†` from a first-token vector with `|0⟩ ⊗ |0⟩`, through SU(2) blocks of determinant 1, zero blocks included |
| DEMUX3 | the two-axis multiplexors equal the branchwise products |
| ADJOINT3 | the multiplexor circuits are unitary |
| QUANTUM3 | the PSD cone meets every hypothesis on exact samples (products, sums, scaling, product effects, every generator) |

Countercontrols. Each is an exact witness that the named hypothesis fails for a family meeting the others; the family
arguments are written below.
1. **ZERO3** (hH1): the zero cone.
   **SCALE3** (hsmul): `{ω ∈ QK 3 | ω 0 ≥ 1}`, which a product scaled by 1/2 leaves.
   **ADD3** (hadd): PSD of rank in {0, 1, 2, 4, 8}; ranks 2 + 1 give 3.
2. **SHIFT3** (hmax): `{ω | dictK ω + (Tr dictK ω / 6)·1 ⪰ 0}`. It is unitarily invariant and holds
   `1 − 2|000⟩⟨000|`, whose value on the product effect `|000⟩⟨000|` is −1.
   **SEP3** (hH2): the separable cone; `CNOT(0→1)|+00⟩` has a partial-transpose minor −1/4.
3. **ORBIT3** (hA): the conic hull of `π(ρ₀⊗ρ₁⊗ρ₂)π†`, for π in the CNOT group GL(3, F₂), which has 168 elements.
   Take `CNOT(1→2) CNOT(0→1) (a⊗b⊗c)` with `a, b, c = (3,4), (5,12), (1,2)`, apply `cycMat` on token 1 or 2, and no π
   pulls the result back to a product. Written: the rank-one elements of the hull are multiples of generators.
4. **CUT3** (connectivity): the 01|2 biseparable cone. `CNOT(1→2)` maps `Bell₀₁ ⊗ |0⟩` to GHZ, with token-2 minor −1/4.
5. **SLICE3** (route (c)): `W = 1 − (3/4)|G⟩⟨G|`, `G = |000⟩ + |111⟩`.
   - `⟨G|W|G⟩ = −1`;
   - the listed one-token contractions are PSD;
   - product values on the rational grid are ≥ 1/4;
   - `CNOT(0→2) CNOT(0→1) W` is −1/2 on `|+⟩⟨+| ⊗ |0⟩⟨0| ⊗ |0⟩⟨0|`.
   Written: `|a₀b₀c₀ + a₁b₁c₁| ≤ 1` for unit vectors.

Measured at the frozen blob:
- 14 `PASS` lines;
- `checks: 3196, failures: 0` (N = 3196);
- final line `VERDICT KTOKEN-K3-EXACT`.

`--self-test` rejects five mutations, each with its code:

| Mutation | Code |
|---|---|
| trace factor 8 → 4 | DICT3 |
| conjugate omitted in the adjoint | ADJOINT3 |
| SHIFT3's sign | SHIFT3 |
| CNOT group below 168 | ORBIT3 |
| CUT3's CNOT reversed | CUT3 |

Shard `probes_ktokenmaxcone1`.

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Positive token | Rule |
|---|---|---|
| Q-INCL | `KTOKEN-MAXCONE-INCLUSIONS-PROVED` | S1 and S2 pass at `E`. In `E`'s exact-head bridge log, the reports of the two inclusions and of every supporting print lie within `[propext, Classical.choice, Quot.sound]`, and no `sorryAx` or `Lean.ofReduceBool` appears |
| Q-EQ | `KTOKEN-MAXCONE-EQ-PROVED` | Q-INCL's conditions, plus `kCone_eq_QK_of_drive_maxCone`, `driveInvariantK_of_eq_QK` and `kCone_eq_QK_iff_drive_maxCone`. S3: the iff's proof is exactly `⟨driveInvariantK_of_eq_QK, fun h => kCone_eq_QK_of_drive_maxCone …⟩`, one witness per direction, and the equality is the antisymmetry of the two inclusions |
| Q-PAIR | `KTOKEN-MAXCONE-PAIR-RECOVERED` | Q-INCL's conditions for the six transports and `pairCone_eq_Q3_of_kToken`. S1: its statement equals EqvK2MaxCone.lean:153–160 but for its name and the `OIBridge.` qualification. S3: its proof names `kCone_eq_QK_of_drive_maxCone` and neither `EqvK2MaxCone` nor a sibling. In the bridge log, the absence line and `A3-CHECK-NONVACUOUS: 13 cases as expected` |
| Q-EXACT | `KTOKEN-MAXCONE-K3-EXACT` | The probe blob at `E`, run by `controls.py` with `python3 -I -B --self-test`, prints the 14 codes, no `FAIL`, `checks: 3196, failures: 0`, the five rejections and `VERDICT KTOKEN-K3-EXACT`, with empty standard error |

Every positive token is gated on the static controls. If any of C1, C2, S1–S4, W, I, J, P, R, G or T fails at `E`,
or is not reported, `verdict` prints the failed controls, runs no probe and reads no axiom report. Every cell then
prints `KTOKEN-MAXCONE-<INCLUSIONS|EQ|PAIR|K3>-NOT-ESTABLISHED`, the round prints `KTOKEN-MAXCONE-1-NOT-READ`, and the
exit status is 1.

When every static control passes, each cell prints its positive token or `…-NOT-ESTABLISHED` by its rule above, and the
round prints `KTOKEN-MAXCONE-1-READ`. No rule reads another cell's outcome. The tokens are printed by
`controls.py verdict E --freeze F --axioms <E's bridge log>`.

`check` records each control's outcome only when that control runs. Its result maps exactly the controls that ran, and
a control that never recorded an outcome is absent and counts as failed.

`controls.py --self-test`, which the shard runs, drives `verdict` in two ways:
- **Through injected static results:** each required control failing alone, one control unreported, and the all-clean
  case.
- **End to end, through the real `check()`, on an in-memory fixture of `D`, `F` and `E`:**
  - with each control's record call removed from the source;
  - with a control's inputs absent (the workflow, `OIBridge.lean`, the result note, a pinned evidence file, the module
    header);
  - unmutated.

In every failing case `verdict` must return failure, name the control, print no positive token and never run the probe.

## The earned reading and the non-inference rule (frozen)

> Earned reading (only when all four cells are positive): for every k, a set of k-token tables containing the products
> of eball 3 states, closed under addition and nonnegative scaling, inside the k-fold maxCone, and invariant under CNOT
> into later tokens and the full rotation flow and cyclic map off the first token, is the cone of tables with positive
> semidefinite k-fold Pauli dictionary image; at k = 2 this yields the statement of the landed pair theorem without
> its use. Exact three-token witnesses with written family arguments show each hypothesis load-bearing, CNOTs needed
> at every token, slice positivity insufficient.

> Non-inference rule: this round sources none of its hypotheses: not the products in K, the cone closure, the maxCone
> bound (product-test validity on an actual k-token cone), or the CNOT and rotation/cyclic invariance (the open
> compatibility premise A_miss with its gate part). The k-token carrier and Pauli dictionary are coordinate
> constructions carrying multi-token local tomography as a premise, not a field-neutral k-token dictionary from OI; the
> maxCone bound is not derived from IE₂, FCC or a composition principle. No Kn claim is made: state cones on qubit-power
> carriers say nothing about other sizes, the operational repertoire or drivability, and would combine with a descent
> from qubit-power carriers (KN-DESC-1, a draft) only through a map to operational carriers and a drivability source,
> neither supplied here. Invariance under every unitary is not shown. The probe is an exact computation and check A3 a
> meta-level check over kernel terms; neither is a Lean kernel proof, and finite witnesses are not universal statements.

**Premises this round does not source:**
- hH1, hadd, hsmul, hmax, hH2 and hA for any physical k-token cone;
- the k-token carrier (multi-token local tomography);
- the drive source, K∞-Trans and K∞-Geom;
- test validity. The sharp-test reduction `maxCone_bound_of_sharp_available` (EqvK2MaxCone.lean:194) is pair-level;
- IE₂ and FCC.

## The ROADMAP wording the round would license (row K2; not applied by the round)

The insertion point is after the K2 paragraph's first sentence (ROADMAP :1011–1014), under `KTOKEN-MAXCONE-1-READ` with
all four cells positive: "KTOKEN-MAXCONE-1 extends it to `k` tokens: a `k`-token set containing the products of
`eball 3`, closed under addition and nonnegative scaling, inside the `k`-fold `maxCone`, invariant under CNOT into later
tokens and the full rotation/cyclic actions off the first token, is the PSD cone of the `k`-fold Pauli dictionary
(`kCone_eq_QK_of_drive_maxCone`)."

"Composition beyond two tokens" may read "the sources of a `k`-token carrier and of these hypotheses". K2 and Kₙ remain
OPEN under every outcome.

## The controls (in `controls.py`)

- **S1 surface.**
  - Preamble: the single import, three `OIBridge.KTokenMaxCone` blocks, and the two scoped instances.
  - The fourteen frozen declarations, in order, equal to the block above. The 68 prints, in the frozen order.
  - No `sorry`, `admit`, `native_decide`, `axiom`, `implemented_by` or `extern`.
  - The recovery's statement equals EqvK2MaxCone.lean:153–160 up to name and qualification.
  - Mutations, each failing:
    - `hmax` dropped from the upper inclusion;
    - `hadd` dropped from the lower;
    - the guard `(j : ℕ) ≠ 0` removed;
    - `i < j` replaced by `i ≠ j`;
    - `K = QK k` weakened to `K ⊆ QK k`;
    - an extra print;
    - the classical instance made global;
    - a second import;
    - the recovery's conclusion changed.
- **S2 resolution.** The landed objects in the table above are at their lines and at `D`'s blobs at `E`.
- **S3 proof shape.**
  - The iff's two witnesses; the equality as antisymmetry.
  - The recovery's proof names the k-token theorem and neither `EqvK2MaxCone` nor a sibling.
  - The absence `#eval` is present verbatim, and `EqvK2MaxCone` appears nowhere else in the code.
  - Mutations: citing the pair theorem fails S3 alone; so do naming a sibling, an equivalence not built from its
    witnesses, and the module without the absence check.
- **S4 phrases.** The module header and, at `E`, the result note must be present, with none of: "OI supplies", "sources the k-token", "local tomography is derived",
  "is invariant under every unitary", "Kn is discharged", "Kn is closed", "K2 is closed", "OI implies QM", "kernel proof
  of" (for the probe).
- **W.** `verify.yml` at `E` is `D`'s with exactly six splices, each anchored once:
  - check A3's step after `Release gate` (`:149–150` at `D`), run with `if: ${{ !cancelled() }}`;
  - the shard after BG-2's last step (`:459–460`), running the probe's and `controls.py`'s self-tests;
  - the shard added to the aggregate's `needs`, env, echo and test lines (`:557`, `:577`, `:598`, `:618`).
- **I.** `OIBridge.lean` at `E` is `D`'s with the one import line.
- **J.** The census at `E` is `D`'s with the one family.
- **C2.** The five frozen blobs (*Design evidence*).
- **P.** The retained evidence pinned below is present at `E` with its digests.
- **R.** The record directory holds exactly (the result note is required at `E`):
  - this file, `controls.py`, the two check files and the pinned evidence;
  - `evidence/f-run/` and `amendments/` if present;
  - the result note at `E`.
- **G.** `git diff --no-renames --name-status D E` lies inside the governed paths, and the legacy manifest is untouched.
- **T.** `delta(D, F)` is the control plane, and the execution is linear after `F`.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane; controls, module, probe and check files are the frozen ones | `C1`: this file's blob at `F`. `C2`: `git rev-parse <commit>:<path>` equal to the frozen blobs, for `controls.py` at stage 1 and all five files at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms; no `sorryAx` | `C3`: the dispatch run at exactly `E`, every job `success`; the 68 prints read by `verdict --axioms` |
| one witness per direction of the iff; the `k = 2` recovery uses the k-token theorem | `C5`: S1 and S3 in `controls.py check E --freeze F` |
| the `k = 2` recovery is independent of the pair theorem and its siblings, and its statement is the pair theorem's | `C3`: the bridge job's A3 step `success` with `A3-CHECK-NONVACUOUS: 13 cases as expected`, its eleven mutations failing in the same step; the absence line in the build log |
| the exact layer replays; its mutations are rejected | `C3`: shard `probes_ktokenmaxcone1` green; `verdict` re-runs the probe blob at `E` (N = 3196) |
| no positive token is printed while any required static control fails or never ran | `C3`: shard `probes_ktokenmaxcone1` running `controls.py --self-test`, whose `verdict` regression covers each of the 13 controls failing alone, one unreported, and the all-clean case, and whose end-to-end test runs the real `check()` with each control's record call removed and with each control's inputs absent |
| the classical carrier instance does not leak to importers | `C5`: S1 (the two scoped lines) |
| the module is registered; no manuscript or ROADMAP changes | `C4`: the release gate at `E` passing every step, `evidence-retention` included; `C5` (J, G) |
| the change stays inside the governed paths, with exactly the frozen workflow, import and census edits | `C6`: `git diff --no-renames --name-status D E`; `C5` (G, W, I, J) |
| the pre-`F` evidence the claims rest on is retained and unchanged (§A.42 item 2) | `C5` (P) at `E`, against the digests below; reviewers check that each pin resolves to retained content |
| `F`'s exact-head run is retained by the first execution commit (§A.42 item 2) | `C8`: `evidence/f-run/` present at stage 1, naming `F`'s run, job and digest; `C5` (R) |
| `E`'s exact-head run reaches `main` through its own evidence-retention pull request before reconciliation, and the receipt names each retained file's digest (§A.42 item 2) | `C8`: reviewer check of that pull request and of the receipt's candidate entry for `E`; `evidence-retention` at `Q` |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design evidence

**Run 1: the predicted tree less `controls.py` and the result note.**
- The tree was built on the disposable branch `dev-equivalence/ktoken-maxcone` from `D`, in two commits:
  - `fd6d4c66df5849bb7fccf8510444572396ba285e`: the module, probe, import line, family, the shard and its aggregate
    lines, and the A3 positive file;
  - `1ab0fd9dd2c6701197f2e0ab18401cafb76a090d`: A3's runner and its W1 step.
- The workflow was dispatched on exactly that head: run 39043849411, `head_sha` `1ab0fd9d…`, 38 jobs, every one
  `success`, the aggregate included.
- Mathlib bridge job 117428550018:
  - Build `success`;
  - Release gate step `success`;
  - A3 step `success`, with final line `A3-CHECK-NONVACUOUS: 13 cases as expected`.
- Probe job 117428550439: `mutations: 5 rejected, 0 accepted` and `VERDICT KTOKEN-K3-EXACT`.
- The axiom reports and the gate's per-step lines of this run are in its full log. They are recorded here only through
  the retained expected result below, and not otherwise.
- The run is evidence for the proposed execution tree. It does not stand in for `F`'s or `E`'s exact-head `check-run`
  attestation, nor for any check this file assigns to `F`, `E` or `Q`.

**Run 2: the predicted tree less the result note.** This is run 1's tree with `controls.py`, a draft of this
preregistration and the shard's `controls.py --self-test` step added.
- The tree is on the disposable branch `dev-equivalence/ktoken-maxcone-r2` at
  `6959ced4c327ebb800cf6d463a049e4066e37288`.
- The workflow was dispatched on exactly that head: run 39056982958, `head_sha` `6959ced4…`, 38 jobs, every one
  `success`, the aggregate included.
- Mathlib bridge job 117466847042 and probe job 117466847062. Their expected result is pinned below.
- Like run 1, the run is evidence for the proposed execution tree, not a `check-run` attestation of `F` or `E`.

**Frozen execution blobs.** These are the blobs run 1 exercised, together with `controls.py`. Run 2 exercised
`controls.py` at `8c8eb522623ee4c5da1d4ab9e40e10c20fd0bf69`. The frozen blob below differs from it only in the
self-test's end-to-end fixture, a change made after run 2: the fixture uses synthetic evidence only, never a retained
file, and two added cases check that `P` rejects a pin left pending and a pin whose digest is not the file's. No
control, rule or token changed. `C2` checks them:

| path | blob |
| --- | --- |
| `verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/controls.py` | `78c8ba364104b6efc465a901f25cfc70ee6967d7` |
| `verification/lean-mathlib/OIBridge/KTokenMaxCone.lean` | `14bb9fc07bf65e59e3f412ac7270ffb734a30069` |
| `verification/lean/ktoken_maxcone1_probe.py` | `04580c5104eaa4cf7eaa5fc32614582442f538e1` |
| `verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/checks/KTokenPairCheck.lean` | `354bd7ce18119da451883ab5189010a5113ffa16` |
| `verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/checks/run_checks.py` | `dc6c77d1f4b8326fcea095103c5cb98295f4fad7` |

A different blob at stage 1 or at `E` is a deviation from the frozen design, not a proof repair: it is recorded in the
result note, and the round halts.

**Retained evidence (§A.42).** Each file is a structured expected result in the form of §A.42 item 1:
- build success;
- the release gate's steps and verdict;
- the KTokenMaxCone `#print axioms` reports;
- the A3 and absence lines;
- the probe's lines;
- the failure markers.

Each file names its commit, run, job and recipe, and the digest of the log it was read from. The files are committed to
the record directory by the first execution commit, outside `amendments/`, and pinned here before `F`. Both were
extracted in CI from the full job logs by run 39063510375 (job 117486234075), using the independently reviewed
extractor at `0d94937d4d8dbc6662b4464842bcdb1523ede18e` with main's `extract_result.py` blob `05c41bce`. Each digest
below was recomputed from the extracted block. `F` is not designated with a pending pin.

| path | sha256 |
| --- | --- |
| `evidence/run1-39043849411.json` | `4e6303690387740559e4e37ca35037722f22c45a0b3da311365be06ca3be9b5c` |
| `evidence/run2.json` | `bc896c46a7ea528cc9010ac124a3c12866ec4b32669ddbd73dea016f47cd2a53` |

## Owner decisions

- The k = 2 check is A3: the built form plus a CI check, with fallback to A1, never to A2. There is no import experiment.
- The drafting snapshot is re-cut at `D` = `b96662e6`, and two design runs are allowed.
- A3 is wired as one bridge-job step (W1).
- Three research modules are ported; FiniteWalsh and FiniteCircuit are not.
- The classical carrier instance is scoped.

## Stages and outcomes

**Stages.**
1. `controls.py` at its frozen blob, the pinned evidence and `evidence/f-run/`.
2. The module, probe and check files at their frozen blobs, the workflow edit, the import line and the family.
3. The result note, candidate `E`.

**Outcomes.**
- **`KTOKEN-MAXCONE-1-READ`**:
  - `controls.py check E --freeze F` OK;
  - four tokens printed by `verdict`;
  - the five frozen blobs at `E` (`C2`);
  - the exact-head run at `E` green on every job.
- **`KTOKEN-MAXCONE-1-HALTED`**: anything else (`S12`).

No outcome sources a hypothesis, edits the ROADMAP or a manuscript, or changes K2 or Kₙ. Correctness bands are unchanged
(consistency axis).
