# Reconstruction round KTOKEN-MAXCONE-1 — the conditional pair-cone theorem for k tokens: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`. It is built from the landed OI-PAIR-MAXCONE-1 record (`round-oi-pair-maxcone-1/` and `EqvK2MaxCone.lean` at
`D`) and the multi-index table carrier of `research/equivalence/NOTES-E5.md` §3 (branch `research/equivalence`, head
`424aa33b`). No design module, probe or `controls.py` exists for it yet; the statement surface below is proposed and is
fixed only by design runs before `F`. Nothing is executed. Only the owner designates `F` under AGENTS §A.39; an
instruction to proceed is not a designation.

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

D: dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4.
Delta(D, F) is this preregistration and any amendments in the round's `amendments/` directory. **No manuscript, built
artifact, `verification/ROADMAP.md`, landed kernel module or other round's record changes under any outcome.**

## What the round is

`pairCone_eq_Q3_of_drive_maxCone` (EqvK2MaxCone.lean:153) gives `K = Q3` (EqvK2Schema.lean:239) for `K ⊆ W 3` from
products (hH1), addition and nonnegative scaling (hadd, hsmul), `K ⊆ maxCone` (hmax), `cnot` invariance (hH2) and
target-token `actT (rotLin t)`, `actT cycEquiv` invariance (hA); ROADMAP K2 (:1010–1018) lists composition beyond two
tokens as open. At `D` every carrier is two-slot (`W d`, `prodState`, `maxCone`, `actT`, `cnot`:
CompositeDimension.lean:97, :161, :186, :198, :775; `dict`: EqvK2Schema.lean:78) and no k-token type exists. Elsewhere
only the unbuilt draft `research/archive/eq4/F/FourCopyIE1.lean:220` (`research/archive`, `4dc0321c`) has one, `W4`;
the built four-copy modules (`dev-equivalence/kt4-at-l`, `288f80ec`) assume none.
`research/equivalence/lean/EqvPowerCone.lean` is the self-duality of the single-token power cone of Ω⋆, with no k-token
content; it is not used.

- **Q-INCL (kernel).** For every `k`: does `K ⊆ maxConeK` with the invariance give `K ⊆ QK k`, and do products, cone
  closure and the invariance give `QK k ⊆ K`?
- **Q-EQ (kernel).** Is `K = QK k` under the six hypotheses, and, given hH1, hadd, hsmul, hmax, equivalent to the
  invariance, with one named kernel witness per direction (§A.34)?
- **Q-PAIR (kernel).** At `k = 2`, through a carrier equivalence, does the k-token theorem yield
  EqvK2MaxCone.lean:153–160 exactly, without citing it?
- **Q-EXACT (exact layer).** At `k = 3`, do exact witnesses show each hypothesis load-bearing, the CNOTs needed at every
  token, and two-token slice positivity insufficient?

## The proposed statement surface

Module `OIBridge/KTokenMaxCone.lean`, importing `OIBridge.EqvK2MaxCone`; `H1`, `H2`, `A` are written out in the module.

```lean
abbrev WK (k : ℕ) := (Fin k → Fin 4) → ℝ
def prodStateK (x : Fin k → Fin 3 → ℝ) : WK k := fun μ => ∏ i, hom (x i) (μ i)
def maxConeK (Ω : Set (Fin 3 → ℝ)) : Set (WK k) :=
  {ω | ∀ e, (∀ i, IsEffectOn Ω (e i)) → 0 ≤ ∑ μ, (∏ i, ehom (e i) (μ i)) * ω μ}
noncomputable def dictK (ω : WK k) : Matrix (Fin k → Fin 2) (Fin k → Fin 2) ℂ :=
  ∑ μ, ((ω μ : ℂ) / 2 ^ k) • Matrix.of fun a b => ∏ i, pauli (μ i) (a i) (b i)
def QK (k : ℕ) : Set (WK k) := {ω | (dictK ω).PosSemidef}
def cnotK (i j : Fin k) (ω : WK k) : WK k := fun μ =>
  sgn (μ i) (μ j) * ω (Function.update (Function.update μ i (pc (μ i) (μ j))) j (pt (μ i) (μ j)))
def actK (j : Fin k) (N : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ)) (ω : WK k) : WK k :=
  fun μ => homMap N (fun ν => ω (Function.update μ j ν)) (μ j)
-- H1 : ∀ x : Fin k → Fin 3 → ℝ, (∀ i, x i ∈ TransitiveBody.eball 3) → prodStateK x ∈ K
-- H2 : ∀ i j : Fin k, i < j → ∀ ω ∈ K, cnotK i j ω ∈ K
-- A  : ∀ j : Fin k, (j : ℕ) ≠ 0 → ∀ t : ℝ, ∀ ω ∈ K, actK j (rotLin t) ω ∈ K ∧ actK j cycEquiv ω ∈ K
theorem subset_QK_of_maxCone_drive (hmax : K ⊆ maxConeK (TransitiveBody.eball 3)) (hH2 : H2) (hA : A) : K ⊆ QK k
theorem QK_subset_of_products_cone_drive (hH1 : H1) (hadd : ∀ ω ∈ K, ∀ η ∈ K, ω + η ∈ K)
    (hsmul : ∀ c : ℝ, 0 ≤ c → ∀ ω ∈ K, c • ω ∈ K) (hH2 : H2) (hA : A) : QK k ⊆ K
theorem kCone_eq_QK_of_drive_maxCone (hH1) (hadd) (hsmul) (hmax) (hH2) (hA) : K = QK k
theorem driveInvariantK_of_eq_QK (h : K = QK k) : H2 ∧ A
theorem kCone_eq_QK_iff_drive_maxCone (hH1) (hadd) (hsmul) (hmax) : K = QK k ↔ H2 ∧ A
theorem pairCone_eq_Q3_of_kToken …  -- statement of EqvK2MaxCone.lean:153–160, proved from the k-token theorem
```

Supporting declarations (fixed in design, one print each): `dictKEquiv` onto `selfAdjoint`, Pauli-string algebra,
`dictK_cnotK`, `dictK_actK_rotLin`, `dictK_actK_cyc`, k-fold product positivity, `reachK`, `muxInvariant_of_drive`, the
dual transfer, `pairCarrierEquiv : W 3 ≃ₗ[ℝ] WK 2` with five transports. Landed objects: `hom`, `homMap`, `ehom`, `sgn`,
`pc`, `pt` (CompositeDimension.lean:100, :112, :167, :741, :744, :751), `IsEffectOn`, `rotLin`, `cycEquiv`
(KInfFoundations.lean:116, :386, :416), `eball` (TransitiveBody.lean:518), `pauli` (EqvK2Schema.lean:25). At `k = 2`,
CNOT into later tokens and rotations off token 0 are exactly the landed hH2, hA; the symmetric form is a corollary.

**Proof route (proposed: reachability).** (a) *Exact decomposition* (Barenco et al., Phys. Rev. A 52, 3457 (1995);
Nielsen–Chuang §4.5) gives invariance under every unitary but needs two-level decomposition, multi-controlled gates and
unitary square roots. (b) *Reachability*: `reach_block` (EqvK2Block.lean:300) is the `k = 2` case of the recursion of
Möttönen et al. (Quantum Inf. Comput. 5, 467 (2005)): every vector is a multiplexed SU(2) on the last token
(`Fin.snocEquiv`), controlled by the earlier ones, applied to (nonnegative (k−1)-token vector) ⊗ |0⟩, down to
`bloch α β ⊗ z3 ⊗ … ⊗ z3` (EqvK2Block.lean:190, :270); `su_euler` (EqvK2Generation.lean:323) splits it into `dUnit`,
`rotRe` multiplexors (:132, :218), each with n controls being two with n−1 and two CNOTs (Shende–Bullock–Markov, IEEE
Trans. CAD 25, 1000 (2006)), half angles by `exists_unit_sqrt` (:280), one control by `rtrick` (:360), `conjInv_ctrl`
(:411). The upper inclusion is `subset_Q3_of_maxCone_block`'s (EqvK2MaxCone.lean:116) argument: the dual of `K` holds
the products and the invariance, hence every rank-one PSD table. (c) *Induction on k*: the pair theorem gives one
control, not (b)'s k−1, and two-token slices do not bound the upper side (SLICE3). Proposed: (b); the pair theorem
enters as Q-PAIR only.

**Mathlib** (`lakefile.toml` pins `rev = "v4.33.0"`, no `lake-manifest.json` at `D`; on-disk checkout of that tag,
`db584cd6`): `Matrix.PosSemidef.kronecker` (Analysis/Matrix/Order.lean:213), `Matrix.kronecker_mem_unitary`,
`Matrix.specialUnitaryGroup` (LinearAlgebra/UnitaryGroup.lean:91, :255), `Finset.prod_univ_sum`
(Algebra/BigOperators/Ring/Finset.lean:157), `Fin.snocEquiv` (Data/Fin/Tuple/Basic.lean:717), `finFunctionFinEquiv`
(Algebra/BigOperators/Fin.lean:580); no k-fold Kronecker product, no gate-decomposition material. **Census family:**
"conditional k-token cone theorem: products, cone closure, the k-fold maxCone bound and CNOT plus rotation/cyclic
invariance give the PSD cone of the k-fold Pauli dictionary (round KTOKEN-MAXCONE-1, reconstruction)", `kernel-only`,
`manuscript: []`. **Import line** after `import OIBridge.EqvK2MaxCone` (OIBridge.lean:268).

## The exact layer (frozen probe `verification/lean/ktoken_maxcone1_probe.py`)

Standard library, exact Q(i), nothing imported from the kernel or the landed checker. Positive checks at `k = 3`: DICT3,
PRODUCT3 (products PSD of rank 1, 2, 4, 8), REACH3 (the recursion rebuilds `x x†` from a scaled `bloch ⊗ z3 ⊗ z3`),
DEMUX3, ADJOINT3, QUANTUM3. Countercontrols, each meeting every hypothesis but the named one (written family arguments):

1. hH1: the zero cone (ZERO3). hsmul: `{ω ∈ QK 3 | ω 0 ≥ 1}`, left by a product scaled by 1/2 (SCALE3; the landed
   density-matrix control also fails addition). hadd: PSD of rank in {0, 1, 2, 4, 8}; ranks 2 + 1 give 3 (ADD3).
2. hmax: `{ω | dictK ω + (Tr dictK ω / 6)·1 ⪰ 0}`, unitarily invariant, holds `1 − 2|000⟩⟨000|`, of value −1 on the
   product effect `|000⟩⟨000|` (SHIFT3). hH2: the separable cone; `CNOT(0→1)|+00⟩` has a partial-transpose minor
   −1/4 (SEP3).
3. hA: the conic hull of `π(ρ₀⊗ρ₁⊗ρ₂)π†`, π in the CNOT group GL(3, F₂): for `CNOT(1→2) CNOT(0→1) (a⊗b⊗c)`, `a, b, c =
   (3,4), (5,12), (1,2)`, and `cycMat` (EqvK2Converse.lean:106) on any token, none of the 168 π pulls it back to a
   product (ORBIT3); written: rank-one elements of the hull are multiples of generators.
4. Connectivity: the 01|2 biseparable cone; `CNOT(1→2)` maps `Bell₀₁ ⊗ |0⟩` to GHZ, token-2 minor −1/4 (CUT3).
5. Route (c): `W = 1 − (3/4)|G⟩⟨G|`, `G = |000⟩ + |111⟩`: `⟨G|W|G⟩ = −1`; listed one-token contractions PSD; grid
   product-effect values ≥ 1/4; `CNOT(0→2) CNOT(0→1) W` is −1/2 on `|+⟩⟨+| ⊗ |0⟩⟨0| ⊗ |0⟩⟨0|` (SLICE3). Written:
   `|a₀b₀c₀ + a₁b₁c₁| ≤ 1` for unit vectors; `(Tr e)·1 − (3/4)eᵀ ⪰ 0` for PSD `e`.

Self-test mutations, each rejected with its code: trace factor 8 → 4, omitted adjoint, SHIFT3 sign, CNOT group below 168,
CUT3's CNOT reversed. Final line `VERDICT KTOKEN-K3-EXACT`; shard `probes_ktokenmaxcone1`, splices as OI-PAIR-MAXCONE-1.

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Positive token | Rule |
|---|---|---|
| Q-INCL | `KTOKEN-MAXCONE-INCLUSIONS-PROVED` | the statements are exactly the frozen ones (S1) and resolve to the landed objects (S2); the exact-head run at `E` builds the module, and the prints of `subset_QK_of_maxCone_drive`, `QK_subset_of_products_cone_drive` and every supporting declaration are within `[propext, Classical.choice, Quot.sound]` |
| Q-EQ | `KTOKEN-MAXCONE-EQ-PROVED` | Q-INCL's conditions for `kCone_eq_QK_of_drive_maxCone`, `driveInvariantK_of_eq_QK`, `kCone_eq_QK_iff_drive_maxCone`, whose proof names exactly those two witnesses, one per direction (S3) |
| Q-PAIR | `KTOKEN-MAXCONE-PAIR-RECOVERED` | Q-INCL's conditions for `pairCarrierEquiv`, its transports and `pairCone_eq_Q3_of_kToken`, whose statement equals EqvK2MaxCone.lean:153–160 but for its name (S1) and whose proof names `kCone_eq_QK_of_drive_maxCone` and no `EqvK2MaxCone` theorem (S3) |
| Q-EXACT | `KTOKEN-MAXCONE-K3-EXACT` | the probe blob at `E`, run by `controls.py` with `python3 -I -B`, prints `PASS` for every code above, no `FAIL`, `checks: N, failures: 0` (`N` frozen at `F`) and `VERDICT KTOKEN-K3-EXACT`; `--self-test` rejects the five mutations |

Otherwise each cell prints `KTOKEN-MAXCONE-<INCLUSIONS|EQ|PAIR|K3>-NOT-ESTABLISHED`. No rule reads another cell's
outcome. `KTOKEN-MAXCONE-1-READ` when the four cells are assigned; tokens printed by `controls.py verdict E` at `E`.

## The earned reading and the non-inference rule (frozen)

> Earned reading (only when all four cells are positive): for every k, a set of k-token tables containing the products
> of eball 3 states, closed under addition and nonnegative scaling, inside the k-fold maxCone, and invariant under CNOT
> into later tokens and the full rotation flow and cyclic map off the first token, is the cone of tables with positive
> semidefinite k-fold Pauli dictionary image; at k = 2 this is the landed pair theorem. Exact three-token witnesses with
> written family arguments show each hypothesis load-bearing, CNOTs needed at every token, slice positivity insufficient.

> Non-inference rule: this round sources none of its hypotheses: not the products in K, the cone closure, the maxCone
> bound (product-test validity on an actual k-token cone), or the CNOT and rotation/cyclic invariance (the open
> compatibility premise A_miss with its gate part). The k-token carrier and Pauli dictionary are coordinate
> constructions carrying multi-token local tomography as a premise, not a field-neutral k-token dictionary from OI; the
> maxCone bound is not derived from IE₂, FCC or a composition principle. No Kn claim is made: state cones on qubit-power
> carriers say nothing about other sizes, the operational repertoire or drivability, and would combine with a descent
> from qubit-power carriers (KN-DESC-1, a draft) only through a map to operational carriers and a drivability source,
> neither supplied here. Invariance under every unitary is not shown. The probe is an exact computation, not a Lean
> kernel proof; finite witnesses are not universal statements.

**Premises this round does not source:** hH1, hadd, hsmul, hmax, hH2, hA for any physical k-token cone; the k-token
carrier (multi-token local tomography); the drive source, K∞-Trans, K∞-Geom, test validity (the sharp-test reduction
`maxCone_bound_of_sharp_available`, EqvK2MaxCone.lean:194, is pair-level) and IE₂/FCC.

## The ROADMAP wording the round would license (row K2; not applied by the round)

After the K2 paragraph's first sentence (ROADMAP :1010–1013), under `KTOKEN-MAXCONE-1-READ` with all four cells
positive: "KTOKEN-MAXCONE-1 extends it to `k` tokens: a `k`-token set containing the products of `eball 3`, closed under
addition and nonnegative scaling, inside the `k`-fold `maxCone`, invariant under CNOT into later tokens and the full
rotation/cyclic actions off the first token, is the PSD cone of the `k`-fold Pauli dictionary
(`kCone_eq_QK_of_drive_maxCone`)."
"Composition beyond two tokens" may read "the sources of a `k`-token carrier and of these hypotheses". K2 and Kₙ remain
OPEN under every outcome.

## The controls (in `controls.py`)

- **S1 surface**: preamble, frozen declarations in order, one print each. Mutations, each failing with its code: `hmax`
  dropped from the upper inclusion; `hadd` from the lower; the guard `(j : ℕ) ≠ 0` removed; `i < j` replaced by
  `i ≠ j`; `K = QK k` weakened to `K ⊆ QK k`; `pairCone_eq_Q3_of_kToken` off EqvK2MaxCone.lean:153–160; an extra print.
- **S2 resolution**: the landed objects named above, `dict`, `bloch`, `su_euler`, `exists_unit_sqrt` and
  `pairCone_eq_Q3_of_drive_maxCone` resolve at `D`. **S3**: the iff names `driveInvariantK_of_eq_QK` forward and
  `kCone_eq_QK_of_drive_maxCone` backward; the pair recovery names no `EqvK2MaxCone` theorem (mutation: citing it fails
  S3 alone); the probe output carries the eight countercontrol codes.
- **S4 phrases** (header, result note): "OI supplies", "sources the k-token", "local tomography is derived", "is
  invariant under every unitary", "Kn is discharged", "Kn is closed", "K2 is closed", "OI implies QM", "kernel proof
  of" (for the probe).
- **P, W, V, I, C, R, G** as OI-PAIR-MAXCONE-1 (probe, workflow frozen; four tokens; the earned reading exactly when all
  four are positive; one import line; one family; the governed paths).

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane; controls and probe are the frozen ones | `C1`: this file's blob at `F`; `C2`: blobs at stage 1 and at `E`, `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms; no `sorryAx` | `C3`: the dispatch run at exactly `E`, every job `success`; the Mathlib bridge build and its prints |
| one witness per direction of the iff; the `k = 2` recovery uses the k-token theorem | `C5`: S3 in `controls.py check E --freeze F` |
| the exact layer replays; its mutations are rejected | `C3`: shard `probes_ktokenmaxcone1` green with `VERDICT KTOKEN-K3-EXACT`; the aggregate job green |
| the module is registered; no manuscript changes | `C4`: the release gate at `E` passing every step |
| the change stays inside the governed paths | `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design work required before F

1. Owner: indices `Fin k → Fin 4`, `Fin k → Fin 2` (proposed) or `Fin (4^k)`, `Fin (2^k)` via `finFunctionFinEquiv`;
   `k = 0` in or out; hypotheses triangular (proposed), nearest-neighbour `i → i+1` (stronger; adds the network
   identity for `CNOT(i→j)`) or symmetric (corollary only).
2. Build the design module: k-generic Pauli algebra (the landed `fin_cases` proofs do not generalize), intertwinings
   reducing to `tokMat_rot`, `tokMat_cyc` (EqvK2Converse.lean:87, :133), `dict_cnot` (BridgeDictionary.lean:71), the
   k-fold `pairVal_nonneg_of_maxCone` (CompositeDimension.lean:993), `reachK`, `muxInvariant_of_drive`, the dual
   transfer, `pairCarrierEquiv`; fix S1 and the print list from a green run.
3. Write and measure the probe (`N`, eight countercontrols, five mutations) and `controls.py` with its self-test; build
   and dispatch the predicted execution tree from `D`; the owner sets the design-run budget.
4. Owner: a k-fold sharp-test variant (cf. EqvK2MaxCone.lean:204), kernel countermodels, OI-CHANNEL-1's κ family at
   `k = 3` (none proposed). Check the three references in design notes. Re-derive the import position at `D`; other
   drafts also insert after `EqvK2MaxCone`, resolved at reconciliation by merits.

## Stages and outcomes

Stages as OI-PAIR-MAXCONE-1 (C1 `controls.py`; S1 module, probe, workflow edit, import line, family; proof repairs only;
S2 the result note = candidate `E`). **`KTOKEN-MAXCONE-1-READ`**: `controls.py check E --freeze F` OK, four tokens
printed, the exact-head run at `E` green on every job. **`KTOKEN-MAXCONE-1-HALTED`**: anything else (`S12`). No outcome
sources a hypothesis, edits the ROADMAP or a manuscript, or changes K2 or Kₙ; correctness bands unchanged (consistency).
