# Reconstruction round KINF-COPY-1 — type covariance of native inversion suffices for DIM-1's selector: PREREGISTRATION (draft for owner review)

**Status: research draft, not a control plane.** Written by the research thread `research/equivalence` (node E8) and
held on that branch under `research/equivalence/preregistration-drafts/` for owner review. No round is opened, no pull
request exists, nothing under `verification/` is written, no `D` is designated and no `F` exists. If the owner opens
the round, this text moves to the record directory below on a pull request from the designated `D`; every measurement
marked *(at L)* is re-taken at `D`; `controls.py` is generated; the predicted execution tree is built and dispatched;
and this file may change before `F` (`G9`). Measurements were taken at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`.

```v3-round
round KINF-COPY-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-kinf-copy-1-type-covariance/
record AM verification/receipts/KINF-COPY-1.json
execution A verification/lean-mathlib/OIBridge/CopyCovariance.lean
execution A verification/lean/kinf_copy1_probe.py
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
execution M .github/workflows/verify.yml
```

The record directory would hold this preregistration, `controls.py` and the result note. **No manuscript, no built
artifact, `verification/ROADMAP.md`, no landed kernel module and no other round's record change under any outcome.**

## The objects

- **`D`** — to be designated by the owner. Drafting measurements: L. **`F`**, **`E`**, **`Λ`**, **`Q`** as §A.39.

## What the round is

K∞-Copy (ROADMAP :1027–1030) is copy naturality: DIM-1's `NativeGate` (CompositeDimension.lean:218) reads one NOT `N`
in both relations, so identical copies' NOTs agree. The two-NOT J/K maps at `d = 5, 7` (NB-1, thread-B records) meet
every two-copy relation with mismatched NOTs. The ROADMAP records an untested candidate weakening (:1027–1030): the
conjugacy class of native inversion is fixed by system type. The round asks three questions, each read by its own rule:

- **Q-RED (kernel).** With two-NOT data `NativeGate2 Ω z NC NT G` (DIM-1's clauses with `NC` on the control side and
  `NT` on the target), does a target-side conjugation by a linear body automorphism fixing the corner axis give two-NOT
  data with the target NOT conjugated; and, when `NT` is the conjugate of `NC` by such an automorphism (*type
  covariance*), is the conjugated gate a one-NOT native gate, so that DIM-1's selector gives `d = 1 ∨ d = 3` (and
  `d = 3` with `2 ≤ d`), also for a conjugator reversing the corner axis?
- **Q-POS (kernel, positive control).** Is there two-NOT data at `d = 3` with `NT ≠ nflip` (the swapped gate)?
- **Q-EXACT (exact layer).** Do the exact instances behave as the theorems state, and do the known two-NOT countermodels
  (J/K maps at `d = 5, 7`) violate type covariance?

## The kernel declarations the round would add (frozen surface, module `OIBridge/CopyCovariance.lean`)

Import `OIBridge.DenseOrbit` (as the built split module; it reaches `K2Guard`); namespace `OIBridge.CopyCovariance`. The statement surface is §B–§D of the design
module `EqvSeams` and the three declarations of `EqvSeamsControl` as built in design run 38083519826 (both copied
byte-identically in `research/equivalence/lean/`), moved into one module with no statement changed:

- §B token-action calculus at every dimension (helpers): `homMap_comp'`, `homMap_id'`, `actT_comp'`, `actT_id'`,
  `actT_congr`, `lin_apply_eq_sum'`, `lin_lin_comm'`, `actC_actT_comm'`, and the definition `actTEq g h hgh hhg :
  W d ≃ₗ[ℝ] W d` (the target action of a linear automorphism).
- §C the maximal cone under a body-preserving map of one copy: `sum_mul_ehom`, `affine_linear_apply`,
  `sum_homMap_mul_ehom`, `prodEffVal_actT`, `isEffectOn_comp`, and
  `actT_mem_maxCone (hg : ∀ x ∈ Ω, g x ∈ Ω) (hω : ω ∈ maxCone Ω) : actT g ω ∈ maxCone Ω`.
- §D the structure `NativeGate2 Ω z NC NT G` (fields `frame`, `posFwd`, `posInv`, `relT : ∀ ω, actT NT (G (actT NT ω))
  = G ω`, `relC : ∀ ω, actC NC (G (actC NC ω)) = actT NT (G ω)`); `nativeGate2_of_nativeGate`,
  `nativeGate_of_nativeGate2`, `map_corner_of_fix`, `conjGate_apply`, `conjGate_symm_apply`, and the five headline
  theorems, quoted from the built module:

```lean
theorem nativeGate2_conj (hG : NativeGate2 Ω z NC NT G) {g h : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}
    (hgh : ∀ x, g (h x) = x) (hhg : ∀ x, h (g x) = x)
    (hgΩ : ∀ x ∈ Ω, g x ∈ Ω) (hhΩ : ∀ x ∈ Ω, h x ∈ Ω) (hgz : g z = z) :
    NativeGate2 Ω z NC (h ∘ₗ NT ∘ₗ g) (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh)
theorem nativeGate_of_conj (hG : NativeGate2 Ω z NC NT G) … (hgz : g z = z)
    (hcov : ∀ x, NT (g x) = g (NC x)) :
    NativeGate Ω z NC (actTEq g h hgh hhg ≪≫ₗ G ≪≫ₗ actTEq h g hhg hgh)
theorem dim_of_nativeGate2_conj (hN : IsNot (eball d) z NC) (hG : NativeGate2 (eball d) z NC NT G) …
    (hgz : g z = z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3
theorem three_of_nativeGate2_conj_of_two_le (hd : 2 ≤ d) … : d = 3
theorem dim_of_nativeGate2_conj_neg … (hgz : g z = -z) (hcov : ∀ x, NT (g x) = g (NC x)) : d = 1 ∨ d = 3
```

- §E (positive control at `d = 3`): `swap01` (the exchange of the first two axes), `swap01_swap01`, `swap01_mem`,
  `swap01_z3`, `swapped_nativeGate2 : NativeGate2 (eball 3) z3 nflip (swap01 ∘ₗ nflip ∘ₗ swap01) (…)`,
  `swapped_not_ne : swap01 ∘ₗ nflip ∘ₗ swap01 ≠ nflip`, and `swapped_nativeGate` (the same gate is a one-NOT native
  gate with the target NOT; see the hazard below).

`#print axioms` lines: the fifteen of run 38083519826 less §A's three (twelve), in the built order. **Census family:**
"type covariance of native inversion suffices for DIM-1's selector: two-NOT native-gate data whose target NOT is the
conjugate of the control NOT by a linear body automorphism fixing or reversing the corner axis reduce to a one-NOT native
gate (round KINF-COPY-1, reconstruction)", `modules: ["CopyCovariance"]`, `status: "kernel-only"`, `manuscript: []`.
**Import line** after `import OIBridge.RelcSelectC5`.

## The exact layer (frozen probe `verification/lean/kinf_copy1_probe.py`)

The probe is `research/equivalence/experiments/e2_copy_conj.py` run 2 (sha256 `c28e1b97…`), with its kernel path set
to `CompositeDimension.lean` beside it in the tree and nothing else changed: Python standard library only (`re`,
`sys`, `fractions`), exact rational arithmetic, one `PASS`/`FAIL` line per check, the verdict line last. Its checks:
C1 (kernel `cnot` parsed from CompositeDimension.lean meets the one-NOT relations), C2–C3 (the swapped gate: two-NOT
data, `NT = diag(−1, 1, −1) ≠ nflip`, equal splits), C4 (no one-NOT reading with the control NOT), C6 (a one-NOT reading
with the target NOT — a recorded fact), C5 (the reduction returns `cnot` exactly), J1–J3 at `d = 5` and `d = 7` (the J/K
maps meet the two-NOT clauses; their NOTs have unequal splits `(2,2)/(1,3)` and `(3,3)/(1,5)`, so no conjugator of any
kind exists; no one-NOT reading with either NOT), S1 (a shear fixing `z` breaks the positivity transfer: value `−1/2`).
The probe runs in a shard of its own, `probes_kinfcopy1`, with the aggregate `Numerical probes` job's four-place edit
(as KT4-PREM-1); `controls.py` checks the workflow at `E` is `D`'s with exactly that edit.

## The decision rules (frozen; implemented by `controls.py verdict`)

| Cell | Outcome | Rule |
|---|---|---|
| Q-RED | `KINF-COPY-REDUCTION-PROVED` | the module's §B–§D statements are exactly the frozen ones (S1), resolve to the landed objects (S2), and the exact-head run at `E` builds the module with every frozen `#print axioms` line within `[propext, Classical.choice, Quot.sound]` |
| Q-RED | `KINF-COPY-REDUCTION-NOT-ESTABLISHED` | otherwise |
| Q-POS | `KINF-COPY-SWAPPED-WITNESS` | `swapped_nativeGate2` and `swapped_not_ne` have their frozen statements and are built within the three axioms at `E` |
| Q-POS | `KINF-COPY-SWAPPED-NOT-ESTABLISHED` | otherwise |
| Q-EXACT | `KINF-COPY-INSTANCES-CONSISTENT` | the probe blob at `E`, run by `controls.py` with `python3 -I`, prints a `PASS` line for every one of C1–C6, J1 (both `d`), J2 (both `d`), J3 (both `d`), S1, no `FAIL` line, `checks: 13, failures: 0` and `VERDICT TYPE-COVARIANCE-CONSISTENT` |
| Q-EXACT | `KINF-COPY-INSTANCES-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. The round's outcome is `KINF-COPY-1-READ` when the three cells are assigned. The
tokens are printed by `controls.py verdict E` from the measurements at `E`.

## The earned reading and the non-inference rule (frozen)

> Earned reading (only when all three cells are positive): DIM-1's selector holds for two-NOT native-gate data whose
> target NOT is the conjugate of the control NOT by a linear body automorphism fixing or reversing the corner axis; the
> two known two-NOT countermodels at d = 5 and d = 7 violate that condition on their exact data.

> Non-inference rule: this round does not show that OI supplies a conjugator between the copies' NOTs, a NOT, a native
> gate or a ball; adopts no premise; and makes no manuscript claim. It does not show that type covariance admits any
> gate that copy naturality excludes: the positive control's gate is also a one-NOT native gate with the target NOT.
> The equivalence, for NOTs of the ball, between type covariance and equal ±1 eigenspace dimensions is a written argument
> and is not part of this round. Positivity of the J/K maps is not re-checked. The probe is an exact computation, not a
> Lean kernel proof.

**Premise this round does NOT source:** type covariance itself (`hcov` with `hgz`, `hgΩ`, `hhΩ`) — the existence of a
corner-fixing body automorphism carrying one copy's NOT to the other's — and every DIM-1 premise (`IsNot`,
`NativeGate2`'s frame and positivity clauses).

## The ROADMAP wording the round would license (HP-1, row K∞-Copy; not applied by the round)

At L, ROADMAP :1027–1030 reads: "**K∞-Copy** — identical-copy covariance, or copy naturality: identical copies' NOTs
agree. An untested candidate weakening is that the frame-preserving conjugacy class of the native inversion is
determined by system type rather than by token; if the planned exact probe confirms it, the obligation becomes type
covariance of native inversion." Under `KINF-COPY-1-READ` with all three cells positive, the last two sentences may be
replaced by: "Copy naturality may be weakened to type covariance of native inversion — the target copy's NOT is the
conjugate of the control copy's NOT by a body automorphism fixing or reversing the corner axis — under which DIM-1's
selector applies (`dim_of_nativeGate2_conj`); the two-NOT countermodels at d = 5 and d = 7 violate it." The phrase
"equivalently, for NOTs of the ball, equal ±1 eigenspace dimensions" of HP-1 is **not** licensed by this round (it rests
on a written argument). Caution carried with the wording: the weakening is not shown to admit any gate that copy
naturality excludes. K∞-Copy stays OPEN under every outcome.

## The controls (in `controls.py`)

- **S1 surface**: preamble, every declaration in order and by kind, every theorem's signature up to `:=`, every
  definition whole, the twelve `#print axioms` lines. Mutations, each failing with its code: `hgz` dropped from
  `nativeGate_of_conj`; `hcov` reversed (`NC (g x) = g (NT x)`); `hgΩ` dropped from `nativeGate2_conj`; `relC` of
  `NativeGate2` read with `NT` on the control side; the conclusion of `dim_of_nativeGate2_conj` weakened to `Odd d`;
  a thirteenth print.
- **S2 resolution**: `NativeGate`, `IsNot`, `actT`, `actC`, `maxCone`, `prodState`, `corner`, `W`, `eball`,
  `dim_of_nativeGate`, `three_of_nativeGate_of_two_le` resolve to the landed declarations (CompositeDimension,
  TransitiveBody, K2Guard at `D`). Mutation: a local `maxCone`.
- **S3 hypothesis load-bearing (exact layer, read through Q-EXACT)**: the ball preservation of the conjugator (S1 shear,
  value `−1/2`); the conjugacy hypothesis (J2: no conjugator exists for the J/K data). A kernel statement of the J/K
  two-NOT clauses is new work and is not part of this round.
- **S4 phrases** (module header, result note): "OI supplies", "derived from OI", "copy naturality is not needed",
  "K∞-Copy is discharged", "replaces copy naturality", "admits gates that copy naturality excludes", "kernel proof of"
  (for the probe), "design module", "not for merge".
- **P, W**: the probe at S1 and `E` is the frozen blob; the workflow is `D`'s with the frozen edit.
- **V**: each cell one token by its rule; the note contains exactly the three computed tokens; the earned reading
  exactly when all three are positive; the non-inference rule under every outcome. Self-test mutations: a broken
  signature fails only Q-RED; a broken control fails only Q-POS; a probe with one witness value changed fails only
  Q-EXACT.
- **I, C, R, G** as in KTRANS-DENSE-1 (one import line; one family; record directory exactly three files; `delta(D, E)`
  exactly the record paths and the five execution paths).

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls and the probe are the frozen ones | `C2`: blobs of `controls.py` and the probe at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms | `C3`: the dispatch run at exactly `E`, every job concluded `success`; the Mathlib bridge build and the twelve prints |
| the exact layer replays and renders | `C3`: shard `probes_kinfcopy1` green with `VERDICT TYPE-COVARIANCE-CONSISTENT`; the aggregate `Numerical probes` job green |
| the module is registered; no manuscript changes | `C4`: the release gate at `E` passing every step |
| the statements, the workflow edit and the note are the frozen ones | `C5`: `controls.py check E --freeze F` |
| the change stays inside the governed paths | `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design evidence and the predicted outputs

| run | commit | workflow run | measured |
|---|---|---|---|
| 1 | `0578b13d` (`dev-equivalence/kinf-seams`) | 38083220991 | build failed at `sum_mul_ehom` (§C) only |
| 2 | `f5367a7a` (proof repair of `sum_mul_ehom`) | 38083519826 | `Build completed successfully (3645 jobs)`; all fifteen prints of `EqvSeams` and `EqvSeamsControl` `[propext, Classical.choice, Quot.sound]`; `lean-axioms` OK (5875); gate red at `lean-manuscript` (no family), `claims`, `duplicate` (research archive on the branch) |
| 3 | `8c92343e` (`dev-equivalence/split-l3`, based on L; the predicted module `CopyCovariance` = §B–§D of `EqvSeams` and `EqvSeamsControl`, no statement changed, blob `fb9c73fe`) | 38091534622 | Mathlib bridge job 114328799399: `Build completed successfully (3646 jobs)`; all twelve `CopyCovariance` prints `[propext, Classical.choice, Quot.sound]`; linter warnings only (unused `first` alternatives inherited from `EqvSeams`); release gate every step PASS except `lean-manuscript` (the unregistered modules) |
| exact | `research/equivalence` | `e2_copy_conj` run 2 (local, replayed by the coordinator) | 13 checks, 0 failures, `VERDICT TYPE-COVARIANCE-CONSISTENT`; run 1 kept (two countercontrol expectations refuted, restated as C4/J3, C6 added) |

**Predicted outputs, generated from those measurements by the rules:** Q-RED `KINF-COPY-REDUCTION-PROVED` and Q-POS
`KINF-COPY-SWAPPED-WITNESS` (run 2's statements and prints, unchanged by the move into one module), Q-EXACT
`KINF-COPY-INSTANCES-CONSISTENT` (`checks: 13, failures: 0`). Run 3 built the moved module standalone over L with all
twelve prints standard, so the module split is measured. **Not yet measured:** the predicted execution tree at the
designated `D` with the family, the probe and its shard, to be built and dispatched before `F`. Pre-`F` hygiene (proofs
only): the unused `first` alternatives the linter reports may be removed.

**Hazard (frozen into S4 and the non-inference rule).** `e2_copy_conj` C6: the control's swapped gate also has a
one-NOT reading with the target NOT. No sentence of the result note may say that type covariance admits gates that copy
naturality excludes.

## Stages and outcomes

Stages as KT4-PREM-1 (C1 `controls.py`; S1 the module, probe, workflow edit, import line and family in one commit; proof
repairs only; S2 the result note = candidate `E`). **`KINF-COPY-1-READ`**: `controls.py check E --freeze F` OK, three
tokens printed, the exact-head run at `E` green on every job. **`KINF-COPY-1-HALTED`**: anything else (`S12`). No
outcome sources a conjugator or edits the ROADMAP or a manuscript; correctness bands unchanged (consistency axis).
