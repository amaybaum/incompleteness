# Reconstruction round PT-STAGE-1 — the protocol tower: finite OI protocols as directed stages with SC∞ and finite rank: PREREGISTRATION (draft for owner review)

**Status: candidate control plane, native V3 draft for owner review. Not an F candidate.** Drafted on a pull request
from `D`. It is built from `research/archive/{oistage,rank}/RESULT.md` and `research/archive/sa/SA-LEDGER.md` on
`origin/research/archive`, and from `research/equivalence/NOTES-E2.md`, `NOTES-E7.md` (§1, row Kinf-Stage) and
`research/archive/eq/{A,E}/RESULT.md` on `origin/research/equivalence` (`424aa33b`). No design module, probe or
`controls.py` exists for it yet (no `.lean` file at `D` or on any `origin/*` branch mentions `protocolTower`); the
statement surface below is proposed and is fixed only by design runs before `F`. Nothing is executed. Only the owner
designates `F` under AGENTS §A.39; an instruction to proceed is not a designation.

```v3-round
round PT-STAGE-1
kind non-sealing
record-directory verification/programmes/oi-qm/reconstruction/round-pt-stage-1-protocol-tower/
```

```v3-governed-paths
record AM verification/programmes/oi-qm/reconstruction/round-pt-stage-1-protocol-tower/
record AM verification/receipts/PT-STAGE-1.json
execution A verification/lean-mathlib/OIBridge/ProtocolTower.lean
execution M verification/lean-mathlib/OIBridge.lean
execution M verification/lean-manuscript-census.json
```

D: dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4. Delta(D, F) is this preregistration and any amendments in the round's
`amendments/` directory; **no manuscript, built artifact, `verification/ROADMAP.md`, landed kernel module or other
round's record changes under any outcome.**

## What the round is

At `D`, K∞-Stage (ROADMAP.md:1022–1025) is "stage consistency, the elementary scope and finite rank: `SCInf`,
`BinaryVisible` and `FiniteRank`. … A predicate for the full elementary-visible scope is not yet formalized." These are
CMP-1's hypotheses (StageCompletion.lean: `SCInf` :78, `BinaryVisible` :244, `FiniteRank` :299), "proved for no OI
construction"; the `DirectedStages` values at `D` are `badD` (:342), `bitTower` (:393) and `midD`
(CompletionAction.lean:404). **Findings** (none kernel at `D`):
- **PT** (oistage §1.1, §2; written, exact T0–T5 on Ω = Z₄ × Z₂): finite Ω, `φ : Equiv.Perm Ω`, readout `π : Ω → V`,
  a probability weight μ (canonical `unif`, CanonicalMeasure.lean:106), a menu of permutations; stage n: protocols of
  length ≤ n over {obs, idle} ∪ A, records of positive weight, effects (protocol, record set), conditional counting.
  Forward maps are label inclusions, so the laws and SC∞ hold by `rfl`. No trace or ℂ enters (classical protocols).
- **Not in this round.** CT (§1.2), the lattice form: SC∞ by `card_fibre` (RegionTower.lean:398) and the cone
  `iterate_dependsOnlyOn_ball` (:283), with the action-interleaved cone lemma and `extPerm` transitivity missing. OPACT
  data (§5, F-S1; exact A1–A5): prefix-closed effects make `AffineRespect` (CompletionAction.lean:58) free, by label
  maps, and bijective actions give inverse data; without prefix closure it fails (A3).
- **NG1** (oistage §6; written, exact P1): for finite Ω every posterior is (μ∘σ⁻¹)·1_C normalized, so finitely many
  preparation vectors: the completed body is a polytope with finite automorphism group, and no drive exists. **NG2**
  (§7; written, re-read in SA §3; exact L1–L2): passive reads, `FiniteRank` and a time step with an inverse datum on the
  body leave a point or no d+2 extreme points in general position, excluding strictly convex bodies of dimension ≥ 2.
- **FiniteRank, open in general.** R0 (rank §1; written, exact on six instances): under SC∞, dim aff{prepVec x} =
  rank[p(e | x)] − 1, both infinite together. Finite Ω: rank ≤ |Ω| (written, SA §2.3); SA P3 (exact): an infinite
  carrier with SC∞, `BinaryVisible`, no `FiniteRank`. Leap rule on ℤ, readout v₀, uniform measure (rank §0, §4): passive
  nonlinear 1, 4, 6, 11, 21, 50, 89, 154 (n ≤ 8; ℚ to n = 4, two-prime F_p lower bounds beyond: affine dimension ≥ 153,
  unboundedness not proved); majority 1, 4, 8, 16, 32, 64, 120 (n ≤ 7, same fields); linear 1 at every horizon (written;
  exact to n = 8); with flip and swap, ranks 1, 3, 3 (linear), 1, 4, 7 (nonlinear) at L = 1, 2, 3 (F_p lower bounds).

The round asks, for finite carriers only:
- **Q-TOWER (kernel).** Is `protocolTower` a `DirectedStages` with inclusion maps, `SCInf` by `rfl` (as `bitTower_scInf`
  StageCompletion.lean:401), a nonempty body, `BinaryVisible` for a Boolean readout, and a finite `Substratum`'s tower
  as an instance?
- **Q-RANK (kernel).** Has the body `FiniteRank` with direction of dimension ≤ `Fintype.card Ω`, hence a chart?
- **Q-SCOPE (kernel; the owner's choice below, or removed).** Is the chosen scope predicate defined, with its controls?

## The proposed statement surface

Module `OIBridge/ProtocolTower.lean`, importing `OIBridge.CompletionAction`, `OIBridge.CanonicalMeasure`,
`OIBridge.SubstratumInterfaceAudit`. Proposals, not built; `D⋯` abbreviates `protocolTower φ π acts μ hμ0 hμ1`:

```lean
inductive Step (A : Type) where | obs | idle | act (a : A)
variable {Ω V A : Type} [Fintype Ω] [DecidableEq Ω] [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]
  (φ : Equiv.Perm Ω) (π : Ω → V) (acts : A → Equiv.Perm Ω) (μ : Ω → ℝ) (hμ0 : ∀ ω, 0 ≤ μ ω) (hμ1 : ∑ ω, μ ω = 1)
def leaves : List (Step A) → Ω → Ω                                   -- the configuration a protocol leaves
def record : (w : List (Step A)) → Ω → (Fin (obsCount w) → V)        -- the readouts its obs steps write
noncomputable def table (e : Σ w, Finset (Fin (obsCount w) → V)) (x : Σ w, Fin (obsCount w) → V) : ℝ
  -- μ{ω : record x.1 ω = x.2 ∧ record e.1 (leaves x.1 ω) ∈ e.2} / weight x, weight x := μ{ω : record x.1 ω = x.2}
noncomputable def stage (n : ℕ) : FiniteStage   -- lengths ≤ n + 1, preparations of positive weight, p := table
noncomputable def protocolTower : DirectedStages                      -- ι := ℕ; maps: inclusions on values
theorem protocolTower_scInf : SCInf D⋯ := fun _ _ _ _ _ => rfl
noncomputable def protocolTower_binaryVisible (π : Ω → Bool) : BinaryVisible D⋯     -- V := Bool
theorem protocolTower_body_nonempty : (body D⋯).Nonempty
noncomputable def response : (Ω → ℝ) →ₗ[ℝ] CSpace D⋯                -- with `posterior : Prep D⋯ → Ω → ℝ`
theorem prepVec_eq_response (x : Prep D⋯) : prepVec D⋯ x = response … (posterior … x)
theorem protocolTower_finiteRank : FiniteRank (body D⋯)
theorem protocolTower_rank_le : Module.finrank ℝ (affineSpan ℝ (body D⋯)).direction ≤ Fintype.card Ω
theorem protocolTower_chart : Nonempty (CompletionChart D⋯)            -- by `exists_completionChart`
noncomputable def substratumTower (𝒮 : Substratum) [Fintype 𝒮.ι] [Fintype 𝒮.V] [DecidableEq 𝒮.V]
    (Vs : Finset 𝒮.ι) (acts : A → Equiv.Perm 𝒮.Conf) : DirectedStages   -- 𝒮.φ, restriction to Vs, unif
```

Landed objects at `D`: `FiniteStage` KInfFoundations.lean:63; StageCompletion.lean `StageMap` :53, `DirectedStages`
:63, `SCInf` :78, `val` :98, `prepVec` :135, `body` :141, `body_subset` :171, `BinaryVisible` :244, `FiniteRank` :299;
`CompletionChart` CompletionAction.lean:144, `exists_completionChart` :154; `unif` CanonicalMeasure.lean:106;
`Substratum` SubstratumInterfaceAudit.lean:60, `Conf` :78, `φ` :81. Rank proof route: `body_subset`, `response`.

**Q-SCOPE: the owner's choice before `F`.** At `D` the geometric branch of K∞ is elementary-scoped.
ROADMAP.md:1057–1063: "The geometric branch is scoped to an elementary system. … The successor foundations work must
formalize that scope, which requires a field-neutral predicate for an elementary system." ROADMAP.md:1077: "Because K∞'s
geometric branch is elementary-scoped, Kₙ is not a consequence of it." Row P1, ROADMAP.md:68: "K∞-Geom (the
elementary-scoped geometric input)". Candidates from the research record, not chosen here (**removal** of Q-SCOPE
leaves two cells):
- **(a) `ElemScope`** (SA §4 P-D): `BinaryVisible` with `sharp : ∃ i x0 x1, p (v0 i) x0 = 1 ∧ p (v1 i) x1 = 1` and
  `cap2`: no three states of `chartBody C` are `PerfectlyDistinguishable` (KInfFoundations.lean:154) by `fullEffects`
  (:149). Needs a chart. Excludes the Z3 tower and the qutrit (exact P2(b), P2(d)); the square meets `cap2`
  (`card_le_two_of_centrallySymmetric` :632, `card_le_two_of_centrallySymmetric_full` :648) and fails `RelStrictConvex`
  (`not_relStrictConvex_square` :762): no implication to K∞-Geom; refuted with available effects (eq/A C5);
  capacity-two polytopes keep the NG1 regime in scope (SA §3.3).
- **(b) `Elem2`, anchored as ElemVis** (eq/A §1; `research/archive/eq/A/ElementaryScope.candidate.lean` on
  `origin/research/equivalence`, unbuilt): two distinct extreme points with a non-boundary midpoint state, anchored on
  the certain states of a sharp `BinaryVisible` pair. Effect-free; holds for the qubit, fails at every complex level
  n ≥ 3 and the real qutrit (written, exact); no capacity bound alone (bipyramid). With GEOM2 (pair faces relatively
  strictly convex, true in complex QM at every level) it scopes only K∞-Geom's application, a framing change to
  ROADMAP.md:1057–1063 not applied here; it presupposes state completeness (eq/A C4); ELEM2 ∧ GEOM2 polytopes have
  dimension ≤ 1.
- **(c) The sharp visible pair alone**: (a)'s `sharp` clause, the hypotheses of `perfectlyDistinguishable_visible`
  (StageCompletion.lean:274). Stage-checkable, no chart; it does not delimit the scope: the Z3 tower meets it with
  capacity 3 (SA P2(b)), and the formalized K∞-Stage predicates hold on the qutrit (eq/E).

## The decision rules

| Cell | Token | Rule |
|---|---|---|
| Q-TOWER | `PT-STAGE-TOWER-PROVED` | the Q-TOWER declarations are exactly the frozen ones (S1) and resolve to the landed objects (S2); `protocolTower_scInf`'s proof is the frozen `rfl` term (S3); the exact-head run at `E` builds the module with every frozen `#print axioms` line within `[propext, Classical.choice, Quot.sound]` |
| Q-TOWER | `PT-STAGE-TOWER-NOT-ESTABLISHED` | otherwise |
| Q-RANK | `PT-STAGE-RANK-PROVED` | S1, S2, the build and the prints for the Q-RANK declarations; `protocolTower_finiteRank`'s proof names `prepVec_eq_response` and `body_subset` (S3) |
| Q-RANK | `PT-STAGE-RANK-NOT-ESTABLISHED` | otherwise |
| Q-SCOPE | `PT-STAGE-SCOPE-DEFINED` | S1, S2, the build and the prints for the chosen definition and its frozen controls (S3) |
| Q-SCOPE | `PT-STAGE-SCOPE-NOT-ESTABLISHED` | otherwise |

No rule reads another cell's outcome. `PT-STAGE-1-READ` when every retained cell is assigned; the tokens are printed by
`controls.py verdict E` from the measurements at `E`.

## The earned reading and the non-inference rule

> Earned reading (only when every retained cell is positive): for finite substratum protocol data the protocol tower is
> a field-neutral DirectedStages with inclusion maps, SC∞ by definitional equality, a nonempty body, BinaryVisible for a
> Boolean readout, and finite rank at most the number of configurations, hence a chart; a finite Substratum's tower is
> an instance. [Q-SCOPE: the chosen predicate is defined.]

> Non-inference rule: the tower gives stages and a chart, not a ball. On finite carriers the completed body is a
> polytope (NG1, written with exact instances, not a kernel theorem here), so in chart dimension ≥ 2 no body-preserving
> family is boundary transitive (`not_boundaryTransitive_of_nonextreme_boundary` TransitiveBody.lean:301 with NG1,
> written, SA §3.2) and no drive exists; NG2 (written) excludes strictly convex bodies of dimension ≥ 2 for passive
> towers with FiniteRank and a reversible step. A positive outcome sources neither K∞-Geom, K∞-Trans nor K∞-Drive and
> is evidence for none. SC∞ here is projective consistency of one global law, with no elementary or quantum content;
> BinaryVisible as stated holds on a one-point body (SA P2). Infinite-carrier finite rank (CT, R0, the leap ranks) is
> not addressed; no protocol tower is shown to meet a scope predicate. NG1 and NG2 concern passive classical towers;
> record-writing observation and a step irreversible on the body (SA §3.2) lie outside them and are not decided.

**Premises this round does not source:** finite rank of any infinite-carrier completion; the CT lemmas; K∞-Act
(prefix-closed effects, `AffineRespect`, `Undoes`, inverse data); a sharp stage test (NOTES-E2 §1); K∞-Drive, K∞-Trans,
K∞-V4, K∞-Copy, K∞-Geom; a protocol tower meeting a scope predicate; the choice of μ (`stochastic_interface_gap`
StochasticInterface.lean:182).

## The ROADMAP wording the round would license

Not applied by the round. With Q-TOWER and Q-RANK positive, K∞-Stage (ROADMAP.md:1022–1025) may gain: "On finite
carriers the protocol tower has `SCInf` by definitional equality and a completion of finite rank
(`protocolTower_scInf`, `protocolTower_finiteRank`); infinite-carrier finite rank is not supplied." With Q-SCOPE
positive: "The elementary scope is formalized as `<predicate>`; no OI construction is shown to satisfy it." The owner
scopes ROADMAP.md:1021 ("All are unsourced"). K∞ and K∞-Stage remain OPEN under every outcome.

## The controls

- **S1 surface**: preamble, frozen declarations and signatures in order, frozen prints. Mutations failing with their
  codes: positivity dropped; an `n`-dependent table; a non-inclusion map; the bound changed; an extra print.
- **S2 resolution**: every landed object above resolves to its declaration at `D`.
- **S3 load-bearing**: `protocolTower_scInf`'s proof is `fun _ _ _ _ _ => rfl` (a `simp` proof fails S3 alone);
  `protocolTower_finiteRank`'s proof names `prepVec_eq_response` and `body_subset`; the module text has no `ℂ`,
  `Complex`, `Matrix` or `trace`; `not_scInf_bad` (StageCompletion.lean:350) resolves unchanged; Q-SCOPE's controls.
- **S4 phrases** (header, result note): "K∞-Stage is discharged", "sources K∞-Geom", "sources K∞-Trans", "the
  completion is a ball", "OI supplies finite rank", "scope is sourced", "kernel proof of NG", "design module".
- **V, G**: one token per retained cell, the earned reading exactly when all are positive; `D..E` inside the governed
  paths, one import line after `import OIBridge.EqvK2MaxCone` (OIBridge.lean:268, the last import at `D`), one census
  family (§A.35) `modules: ["ProtocolTower"]`, `status: "kernel-only"`, `manuscript: []`.

## Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| execution begins from the frozen control plane | `C1`: this file's blob at `F` |
| the controls are the frozen ones | `C2`: `controls.py` blob at stage 1 and at `E`; `controls.py --self-test` OK at `E` |
| every frozen declaration elaborates within the three axioms | `C3`: the dispatch run at exactly `E`, every job `success`; the Mathlib bridge build and the frozen prints |
| SC∞ by `rfl`; the rank proof factors through `response`; field-neutral content | `C5`: S3 in `controls.py check E --freeze F` |
| the module is registered; no manuscript changes; the change stays in the governed paths | `C4`: the release gate at `E` passing every step; `C6`: `git diff --no-renames --name-status D E`; `C5` (G) |
| the native receipts hold; the legacy records are untouched | `C7`: `v3_verifier --verify-round Q`; `legacy_records_check.py` at every stage commit and at `Q` |

## Design work required before F

1. The owner's choice for Q-SCOPE: (a), (b), (c) or removal; kernel forms of (a)'s controls (Z3 tower, qutrit, square
   as a chart body) and of (b)'s (qubit, qutrit) are not built, and their cost is unmeasured.
2. Build and dispatch the design module from `D` (build green, prints within the three axioms, gate red only at
   `lean-manuscript`), then the predicted execution tree; `controls.py`, its self-test and the family text. None exists.
3. Encoding: lengths ≤ n + 1 at stage n (oistage starts at horizon 0, where no binary visible test exists); `Fintype`
   for bounded words and records; general μ or `unif`; `weight` via `trajProb` (PassiveQuotient.lean:339) or not.
4. Owner decisions outside the default surface: R0 in kernel form (one witness per direction, §A.34); label duals (a
   K∞-Act round); CT; an exact layer replaying SA P3 or oistage P1 (adding a probe and the workflow to the paths).

## Stages and outcomes

C1 adds `controls.py`; S1 the module, import line and census family; later commits repair proofs only; S2 the result
note, candidate `E`. **`PT-STAGE-1-READ`**: `controls.py check E --freeze F` OK, one token per retained cell, the
exact-head run at `E` green on every job. **`PT-STAGE-1-HALTED`**: anything else (`S12`). No outcome sources K∞-Geom,
K∞-Trans, K∞-Drive or finite rank beyond finite carriers, or edits the ROADMAP or a manuscript; correctness bands
unchanged (consistency axis).
