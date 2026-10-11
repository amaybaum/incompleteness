# HP-bridge-17 — the sufficient bridge in the owner's form: OpDrive(θ₀) and the J-datum, classification (C)

From `research/bridge`, node B20 (round 5). Proposed for the origin thread (O14), the equivalence thread (E19, E22) and
the countermodels thread (K(Z_F)). The coordinator routes, and applies the owner's classification with origin's O14.

## Statements and labels

1. **The data and their pair availability** (B20-1; availability). OpDrive(θ₀) := `TokenAvailAt 𝓘 arch zPh n` for
   every `n` (`zPh = diag(1, w)`, `w = 3/5 + 4i/5`, the operator of `R_z(θ₀)`); the J-datum := `TokenAvailAt 𝓘 arch uJ n`
   for every `n` (`uJ = (1 − i(X + Y + Z))/2`). OI (I4.29, I4.30, I4.32) + {OpDrive(θ₀), the J-datum} ⇒ `PairAvailAt` of
   both at every level; each datum is exactly that pair availability. Label: CONDITIONAL (on the two data, introduced,
   not OI premises) — [D] (run 38124442150, `lean/BridgeOpDrive.lean`, 21/21 standard).
2. **The derived half** (B20-2; availability in, invariance out). OI (I4.32, I4.134) + {OpDrive(θ₀), the J-datum} +
   (T)_𝓘 ⇒ (T) for `{R_z(θ₀), J}`: a pair cone `K ⊆ W 3` with the class's transfer clause is invariant under
   `actT R_z(θ₀)` and `actT J` (`bridge_derived_half`). (T)_𝓘 is introduced, not an OI premise; by `transferClause_iff`
   it is (b) as a schema over the class, and it cannot be dropped (the full class satisfies both data; K(Z_F) is moved by
   `actT R_z(θ₀)`). Kernel closure rules: spectator, transport, discard, ray, block; no bind step, no limiting step, no
   availability beyond the two data. Label: CONDITIONAL (on the two data and (T)_𝓘) — [D]; the separation [D] + [X] + [A].
3. **Exact availability, not density.** The chain needs the exact operators `zPh` and `uJ`. A dense subgroup would give
   membership of its own elements only; the passage to invariance under `actT R_z(θ₀)` would need a closed cone (H3,
   I3.149, introduced) and the continuity of `U ↦ coordOf (Ad(1 ⊗ U) (dict ω))` [W], and would yield invariance only.
   Neither built nor claimed.
4. **Sufficient, not necessary.** Alternative generating sets, each adding a datum to the stated access, are not
   excluded: a finite-order non-Clifford datum (origin's `rot(π/8)`, HO-27 item 4); the Hadamard and `π/8` phase [L];
   the exchange's layer flow at one non-Clifford time with the quarter phase. Their density at the level claimed is
   origin's (O14/O15).
5. **Exclusion, refutation, non-equivalence** (B20-3). The bridge's premises are jointly unsatisfiable at K(Z_F) (the
   exclusion lemma with certified pairings `−4/5`, `−1`); FM refutes both data; FM's `Q3` has both invariances with
   neither datum, so the bridge is not an equivalence.
6. **Disguise test and classification** (B20-4). OpDrive(θ₀) restates I2.33's phase intervention at `θ₀` in
   availability form and I3.169's operational reading at `θ₀`; it is not (b) in disguise; it is H-T's token clause at
   level M, whose (A) is I4.29 with I4.30. Owner's classification: B20 **(C)**, pending O14; B14-6 as amended **(D)** for
   the drive's availability. Scope: insufficiency for the complete stage-6 inventory is definitive within that scope and
   says nothing about every conceivable extension of OI.

## Evidence

| item | pointer |
|---|---|
| module | `lean/BridgeOpDrive.lean` (sha256 `5d41b3f3…`); imports `BridgeToken`, `BridgeConverge`, and the equivalence thread's `EqvK2Converse` (carried on the dev branch only); run 38124442150 |
| script | `experiments/b20_bridge.py` P1–P5 (run 2; run 1 kept), replay byte-identical |
| notes, results | `NOTES-B20.md`; `RESULTS.md` rows B20-1 … B20-4, V-5 |

## What the recipient may assume

Items 1–6 at their labels. For O14: a candidate principle that yields `TokenAvailAt zPh n` and `TokenAvailAt uJ n` at
every level, in a context-stable, label-invariant, unitary-ray-saturated architecture, feeds item 2 directly; one that
yields only a dense set needs item 3's premises and gives invariance only.

## What the recipient may not assume

- certification;
- (T) for `{R_z(θ₀), J}` from the data without (T)_𝓘;
- that OpDrive(θ₀) is necessary, or that any alternative generating set is dense at a level;
- that any inventory item at L implies either datum;
- an equivalence between the data and the invariances.
