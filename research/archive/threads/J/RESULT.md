# Thread J — P1: sharp-seed completion (read-only; certified main 6d0abf6b)

Line numbers are at `6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a`. KF = `KInfFoundations.lean`, RL = `RegionLimit.lean`,
RT = `RegionTower.lean`, PQ = `PassiveQuotient.lean`. Evidence levels are kept apart: **kernel** (a landed
identifier), **exact** (`j_controls.py` here, `OK -- 144 checks, 5 written notes`, replay identical, sha256
`a31d3f25…02e30eca`, output in `j_controls.out`), **written** (an argument stated here). Nothing here is a kernel
result unless it names a landed identifier. No dynamics, reversible map, drivability or transitivity is used anywhere.

## Outcome: CONDITIONAL — on one named completion theorem, stage consistency (SC∞). Not on finite predictive rank.

Given SC∞, the visible stage coordinate extends to the completion as a coordinate functional: affine, continuous,
an effect on Ω∞, with the 1/0 values on the distinguished pair kept exactly, and the pair perfectly distinguishable
(`PerfectlyDistinguishable`, KF:154, ι = Fin 2). The chain is written and short (§2). Without SC∞ the 1/0 values are
lost, and the countermodel has finite affine dimension (C1a). The countable-simplex completion has unbounded affine
dimension, and a fixed-stage seed survives there (C1b). So finite predictive rank (Main.md:352) is **neither
necessary nor sufficient** for the seed question. It is load-bearing for (SEC) and compactness (Thread F, B8 and
CM-INF), not here.

## 1. Sub-question (1): what the completion body is in the corpus — OPEN (missing definition)

- **Kernel.** `FiniteStage` (KF:63; `vec` KF:81, `states` KF:84) is the only body constructor. No other module
  uses it (grep). There are no stage maps, no directed system and no completion object in the field-neutral
  vocabulary. The KF header says the module "sources nothing".
- **No predictive-rank identifier** exists anywhere in `OIBridge`.
- **Manuscript.**
  - Main.md:352: "stagewise finiteness does not prove that this completion retains finite predictive rank".
  - Main.md:542: a reconstruction "must additionally show that its chosen completion retains finite predictive
    dimension".
  - Main.md:538 fixes one finite realization. Main.md:540 gives the SIC embedding, where the sharp effect extends to
    1/2 + √3/2 at an ontic vertex.
- **Region limit** (matrix regime, imported ℂ). The structure is a spatial tower, not a refinement:
  - `inclObs` (RL:102 and RT:123) is X ↦ X ⊗ 1, and `trace_inclObs_mul_restrict` (RT:190) is its duality with
    restriction;
  - `Consistent` (RT:319) and `consistent_mix` (RT:341) give the consistent families;
  - the RT header says: "no infinite-volume algebra … is constructed".
- **The only candidate definition is off-repo.** The scratchpad design note (`k-infinity/K-INF-DESIGN.md` §2,
  ungoverned) sets Ω∞ = cl conv{p(·|s)} ⊂ [0,1]^{E∞} in the product topology. It presupposes "maps carrying readbacks
  and preparations forward consistently" but never states that as a condition. That presupposition is the hidden
  premise this thread isolates.

## 2. The chain, given SC∞ (written; every step elementary)

**SC∞ (the named completion theorem).** There is a directed system of `FiniteStage`s with functorial forward maps
ι_{στ} on readbacks and preparations, such that

p_τ(ι e, ι s) = p_σ(e, s).

The body Ω∞ = cl conv{p(·|s)} sits in [0,1]^{E∞}, where E∞ = colim E_σ. In KF types it lives in V = ℓ^∞(E∞), which is
normed. ℝ^{E∞} is not normed when E∞ is infinite, and ℓ^∞ holds every cube point. The definition is free. What is
open is the consistency *theorem* for the stages OI actually supplies. Only the matrix analogue is kernel:
RT:152, RT:190, RT:233, RT:319.

| step | statement | uses |
| --- | --- | --- |
| J1 | p(·\|s) is a well-defined point of [0,1]^{E∞} for every stage preparation s | directedness, SC∞, functoriality |
| J2 | π := evaluation at ι e_v is linear on ℓ^∞(E∞), norm-continuous (norm 1) and product-continuous | definition |
| J3 | `IsEffectOn Ω∞ π`: π takes values in [0,1] on the whole cube, hence on Ω∞ | J2 |
| J4 | π(p(·\|x_v)) = p_σ(e_v, x_v) = 1 and π(p(·\|x_v′)) = 0 | SC∞ |
| J5 | `PerfectlyDistinguishable Ω∞ ![x_v, x_v′] ![π, 1 − π]` (the sum is 1 identically, and each effect is certain on its own state) | J3, J4 |
| J6 | π is proper and x_v is a boundary state of Ω∞ | J3, J4, kernel `isBoundaryState_of_certain_proper` KF:227 |

**Answers to the charter's sub-questions.**
- **(2)** π is affine and continuous through the limit. It is a coordinate, so continuity is automatic.
- **(3)** The 1/0 values survive. They are table entries carried by SC∞, and {π = 1} is closed.
- **(4)** The pair stays perfectly distinguishable.

**Second premise, only for the "available partner" reading.** Suppose the partner must be the other visible
*readback* e_{v′}, not the affine complement 1 − π. Then π + π_{e_{v′}} = π_unit on Ω∞ needs **TP**: forward maps
carry tests (outcome families summing to the unit) to tests. SC∞ on carried preparations does not constrain
preparations that first appear at later stages.

Given TP, the finite stage partition holds on all of Ω∞, because it is a closed linear condition on finitely many
coordinates. An *infinitely refined* visible partition does not survive (C1b).

**Proposed Lean (candidates; nothing frozen):**
- `FiniteStage.Hom` and `DirectedStages` (with SC∞ as a field);
- `completionBody : Set (lp (fun _ : E∞ => ℝ) ∞)`;
- `completionBody_convex`;
- `seedCoord_isEffectOn`;
- `seed_perfectlyDistinguishable_completion`.

All are cheap once the definitions exist. None needs `[FiniteDimensional ℝ V]` or compactness.

## 3. Controls (exact, `j_controls.py`)

| control | result | what it shows |
| --- | --- | --- |
| **T1** classical simplex tower Δ₁ ⊂ … ⊂ Δ₈ | SC holds at every step; the seed π₀ is 1/0 on (δ₀, δ₁) at every stage; the visible partition sums to the unit on every preparation | positive instance |
| **T2** consistent disk tower (rational unit vectors; a surrogate, not OI-sourced) | the seed (1 + x·r)/2 is 1/0 on ±x at every stage; tables in [0,1] | positive instance, non-classical shape |
| **C1a** two-stage tower violating SC: p_σ(e\|x) = 1, p_τ(ιe\|ιx) = 1/2 | both stages valid; SC fails at (e, x); the seed is no longer certain at x_v; affine dimension ≤ 1 | **SC∞ is load-bearing, and finite rank does not save the seed** |
| **C1b** countable-simplex completion in [0,1]^{E∞}, product topology | see the next three rows | — |
| — escape state | δ_n agrees with the escape state 0̸ (unit 1, every visible coordinate 0) on the first M coordinates for all n ≥ M (M ≤ 10), so δ_n → 0̸ ∈ Ω∞, and the partial visible sums at 0̸ are 0 while the unit is 1 | the infinite visible partition is not a test on Ω∞ |
| — limit of stage seeds | e_n = π_n is sharp on (δ_n, δ₀) at stage n; e_n → 0 on mixtures and on 0̸; lim e_n(δ_n) = 1 but (lim e_n)(lim δ_n) = 0 | **the constructed stage coordinate that loses sharpness in the limit** |
| — fixed-stage seed | π₀ keeps 1/0 on (δ₀, δ₁) and lies in [0,1] at 0̸; δ₀…δ_K are affinely independent for K ≤ 8 (dimension unbounded) | a fixed-stage seed survives with no finite rank |
| **C2** SIC Bloch ball, Q(√3) | see the next three rows | — |
| — C2(i) | the sharp operational coordinate (1+z)/2 has unique response vector c_i = 1/2 ± √3/2, and c_max − 1 > 0 (exact sign) | an effect on the body, not a response effect (Main.md:540): effecthood must be tested on Ω, never on a realization's ontic simplex |
| — C2(ii) | over all 16 visible cells T: max = \|T\|/4 + \|s_T\|/(4√3) and min = \|T\|/4 − \|s_T\|/(4√3); sharpness would need \|T\| = 2 and \|s_T\|² = 12, but every \|T\| = 2 cell has \|s_T\|² = 4; the size-3 cells are certain at −a_k with minimum 1/2 | no visible-partition readout of a fixed SIC realization supplies a sharp pair; the seed hypothesis is unsatisfiable there |
| — C2(iii) | p_i(−a_j) = 1/3 for i ≠ j, so no ball state has two zeros, and p_i = 1 needs a_i·r = 3 | conditioning on a visible cell leaves the ball image; closing under it gives Δ₃, and the ball geometry is lost |
| **C3** classical finite simplex Δ₃ | consistent; the seed is sharp; partition of unity holds | passes trivially |
| **M** region inclusion (matrix regime, imported ℂ; RL:116, RL:125) | (X⊗1)² = X⊗1; tr((X⊗1)ρ) = tr(X restrict ρ); the pair keeps 1/0 | the landed matrix analogue of SC∞ plus J4 |

## 4. Gem classification (§A.31): NEW

The hidden assumption is in the design-note completion. "Maps carrying readbacks and preparations forward
consistently" is stated as construction and never as a condition, and it is the only premise the sharp seed
needs. Finite predictive rank, the premise previously named for P1, is dissociated from the seed question in both
directions (C1a, C1b).

Cross-propagation, as assumption-watch markers:
- **(a)** P1 splits into two parts:
  - **P1-def**: the definition, with SC∞. This is all that the seed (Thread H's V3) needs.
  - **P1-rank**: finite predictive rank. This is needed only for compactness, (SEC) and the Lean `[FiniteDimensional]`
    typing of B8.
- **(b)** Whenever "the visible readout" is used as a sharp seed, the body must be closed under visible
  conditioning. On a fixed finite realization of the Bloch ball, that closure is the simplex (C2(iii)). So a sharp
  visible seed and a ball body cannot both come from one fixed realization. This is consistent with Thread G's C7a,
  which supports only the poles. The seed must enter at the level of the completion, not of a realization.
- **(c)** The product-topology completion admits escape states with no visible value (C1b). Any later use of an
  *infinite* visible partition (for example, in a region tower whose visible alphabet grows) as a test on Ω∞ needs a
  tightness or σ-additivity premise that the design note does not supply.

## 5. Scope and limits

- Every chain step is written, not kernel. "Proved" applies only to KF:227, the RT/RL identifiers and the KF
  definitions cited.
- The T2 tower is an illustrative surrogate. Whether the stages OI actually supplies satisfy SC∞ field-neutrally
  is the open content of the named theorem.
- Main.md and the ROADMAP were not edited. The worktree was removed at the end of the thread.
