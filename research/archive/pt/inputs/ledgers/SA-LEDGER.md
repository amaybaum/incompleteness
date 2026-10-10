# SA-LEDGER — thread SA: source K∞-Stage / K∞-Act

Status: COMPLETE (all sections filled). Read-only thread, base `8daf2bc0`.

## 0. Base and scope

- **Base.** `8daf2bc0ad9c4fe4e9ae422b3a9a010a80ab9e53` ("ROADMAP: K1 effect premise as K1-BRIDGE-1 landed it
  (#799)"), read in `scratchpad/wt-base`. Read-only. No file in the worktree was modified, and no git command
  that writes was run (only `rev-parse`, `log`, `merge-base --is-ancestor`, `diff --stat`). Paths below are
  relative to `verification/lean-mathlib/OIBridge/` unless they say otherwise.
- **Thread scope.** K∞-Stage (`SCInf`, `BinaryVisible`, `FiniteRank`, and the elementary-scope predicate that
  does not exist yet) and K∞-Act (`OpDatum`, `AffineRespect`, the inverse datum, `Undoes`). Nothing about K2,
  composites, K∞-Geom, K∞-Copy or Kₙ is decided here. Section 5 lists the interface questions handed on.
- **Evidence levels.** *kernel*: a landed identifier at the base, with file:line. *exact*: a script in
  `scratchpad/sa/`, run with exact rational arithmetic (Fraction/sympy; no float is used as evidence), with its
  command and output recorded. *written*: an argument given here and not kernel-checked. *prior*: an off-repo
  note, used only after the verification listed below. *citation*: literature.
- **Files read.** `AGENTS.md`; `verification/ROADMAP.md` row P1-K (line 68) and section "P1 — K" (lines
  972–1061); `verification/audits/foundations/kinf-seams-audit.md`;
  `verification/audits/foundations/kn-elementary-carrier-census.md`. Kernel modules read in full:
  `StageCompletion`, `CompletionAction`. Read in their relevant parts: `KInfFoundations` (§A, §B, §C, §E),
  `CompositionOrder` (§B–§D), `TransitiveBody` (§A, §D, §E, §F′), `OrbitGeneration` (definitions),
  `CompositeInterface`, `EffectSpace` and `K1Bridge` (headers), and the observer-architecture modules
  `PassiveQuotient`, `ObservabilityQuotient`, `ControlledQuotient`, `CanonicalMeasure`, `StochasticInterface`,
  `RegionTower`, `SecondOrderLayer`, `SubstratumInterface`, `PassiveObservation`, `InternalObserver`,
  `EmbeddedObservation` and `MicroscopicReversibility` (headers and the cited declarations).
- **Prior notes and how each was verified.**
  - Ancestry. Every base of the prior notes is an ancestor of `8daf2bc0`: `0f2687b7` (drive, oistage, rank,
    quotient), `254ad0a7` (opact) and `bd5de8f5` (seams audit). `git diff --stat <base> HEAD --
    verification/lean-mathlib/OIBridge/` shows **only added files** since those bases: `CompletionAction`
    (after opact only), `CompositeDimension`, `CompositeInterface`, `CompositionOrder`, `EffectSpace`,
    `K1Bridge` and `TransitiveBody`. No pre-existing module changed, so every file:line the notes cite in an
    older module is still valid. I re-grepped all of them at the base: RT:254/259/283/304/398, PQ:127/339/383/498/563,
    OQ:79/108/270, DG:149, CQ:56/133/185, CM:106/205/227, SI:118/182/191, PC4:582 and SOL:87/279/301 all match.
    `depth_two_circuit` is at `SecondOrderCircuit.lean:313`, not in `SecondOrderLayer` as the oistage note
    implies.
  - `opact/RESULT.md` and `DESIGN-CONSTRAINTS.md`. OPACT-1 has since landed (`CompletionAction`). The note's
    RESPECT premise **is** the landed `AffineRespect`, so it is a restatement and not a source. Its NATDUAL
    premise, a label-to-label table dual, is re-derived in §2 below (exact probe P4).
  - `drive/RESULT.md`. F-D3 (a stage-preserving datum has finite order) is **now a kernel theorem**:
    `CompositionOrder.finiteOrderOn_of_stagePreserving` (`CompositionOrder.lean:348`), with
    `not_stagePreserving_of_infiniteOrderOn` (:378). Γ0, compactness of `chartBody`, is now kernel too
    (`TransitiveBody.lean:109`, `:121`). F-D1, the matrix route forcing the Bloch ball, is accepted as *prior*.
    Its argument (an R_z(π/2)-invariant subspace that is also R_H-invariant is 0 or ℝ³) was re-read and is
    standard. It is not re-run, because nothing in §2 depends on it beyond "the ℂ route is circular".
  - `oistage/RESULT.md`, which carries the protocol tower PT, the lattice cone tower CT, F-S1, NG1 and NG2. PT's
    laws, F-S1 (prefix closure gives AffineRespect) and the Undoes claim were **re-derived independently**
    (exact probe P4, written §2). NG2's proof was re-read step by step (§3) and is sound as written. NG1 was
    re-checked on a new toy (P4: finite order, finitely many posteriors).
  - `rank/RESULT.md`. R0 (FiniteRank ⇔ finite rank of the protocol matrix, under SC∞) was re-derived as written
    and checked on new exact instances (P3). The nonlinear-rule ranks 1, 4, 6, 11, … are accepted as *prior*
    finite-horizon evidence. They are **not** a proof of infinite rank, and P3 supplies one on a different
    model.
  - `k-infinity/K-INF-DESIGN.md` §8–§11 (capacity two does not force strict convexity; Lemma D) and
    `threads/SUMMARY.md` were read. Lemma D is now kernel: `card_le_two_of_centrallySymmetric`
    (`KInfFoundations.lean:632`, `:648`).
  - `quotient/RESULT.md` and `wave2/` were skimmed for scope-predicate material. Nothing there bears on the
    Stage/Act fields beyond what is cited.

## 1. The landed observer architecture as it actually is

**1.1 Two disconnected halves.** The kernel at the base carries two observer architectures that share no
import:

| half | objects (file:line) | field | stage/table data | operation data |
|---|---|---|---|---|
| **field-neutral K∞ vocabulary** | `FiniteStage` (KInfFoundations:63); `StageMap`, `DirectedStages`, `SCInf`, `val`, `prepVec`, `body`, `coord`, `stageEffects`, `BinaryVisible`, `FiniteRank` (StageCompletion:53/63/78/98/135/141/157/176/244/299); `OpDatum`, `StateRespect`, `AffineRespect`, `CompletionChart`, `induced`, `after`, `Undoes`, `inducedEquiv` (CompletionAction:46/53/58/144/277/305/325/333); `StagePreserving`, `iterAfter` (CompositionOrder:234/242) | ℝ | arbitrary finite tables | arbitrary completion-valued data |
| **passive and controlled classical substratum** | `Equiv.Perm S` with `[Fintype S]`, `vis : S → I`; `itiRelK`, `BranchDomainK` (OQ:79/108); `itiSetoid`, `trajProb`, `hiddenExt` (PQ:127/339/498); `actWord`, `ctrlSetoid`, `ActionSeparating` (CQ:56/133/185); `unif`, `counting_invariant` (CM:106/205); the lattice `CouplingGraph`, `ball`, `iterate_dependsOnlyOn_ball`, `card_fibre` (RT:254/259/283/398); local gates `extPerm`, `gateEquiv` (SOL:87/279) | none (sets, permutations, counting) | trajectory probabilities, `trajProb` | permutations: the step φ and the action menu `acts : A → Equiv.Perm S` |
| **ℂ operational half** (for completeness) | `FiniteOperationalTheory` (OperationalAssembly), passive instruments (PassiveObservation), internal observer (InternalObserver), monomial interventions (SubstratumInterface), OI⁺ family (EmbeddedObservation, MicroscopicReversibility) | ℂ | trace rule | CP maps, conjugations |

- The **only `DirectedStages` instances** in the kernel are controls: `badD` (StageCompletion:342), `bitTower`
  (StageCompletion:393) and `midD` (CompletionAction:404). Checked by search at the base: `DirectedStages` and
  `FiniteStage` occur only in KInfFoundations, StageCompletion, CompletionAction, CompositionOrder,
  TransitiveBody and CompositeInterface (a comment only).
- The **only `OpDatum` instances** are `midOp` (CompletionAction:419, a control) and `idDatum`
  (CompositionOrder:228, the identity).
- **No module builds a `FiniteStage` from `trajProb`, `actWord` or any substratum object.** The
  field-neutral vocabulary is therefore *stated over* arbitrary tables. It is *supplied by* nothing.

**1.2 Consumers of the Stage/Act fields** (search at the base):
- `SCInf` → `val_eq_at` (SC:117), `val_same_stage` (SC:217), `sharpSeed_completion` (SC:224),
  `boundary_completion` (SC:232) and `perfectlyDistinguishable_visible` (SC:274). Nothing outside
  StageCompletion consumes it. OPACT-1, ORD-1 and TRB-1 do not use SC∞.
- `BinaryVisible` → `visible_test_completion` (SC:260) and `perfectlyDistinguishable_visible` (SC:274). No
  other module.
- `FiniteRank` → `exists_chart_of_finiteRank` (SC:304) and `exists_completionChart` (CA:154). Every downstream
  module (ORD-1, TRB-1) consumes the resulting `CompletionChart`, not `FiniteRank` itself.
- `OpDatum`, `AffineRespect` and `Undoes` → `existsUnique_induced` (CA:258), `induced_mem` (CA:300),
  `induced_after` (CA:319), `inducedEquiv` (CA:333), `preservesBody_inducedEquiv` (CA:352) and
  `isEffectOn_pullback` (CA:364); ORD-1's `finiteOrderOn_of_stagePreserving` (CO:348) and
  `exists_moved_of_infiniteOrderOn` (CO:295).

**1.3 What "operation" means in each half.**
- In the field-neutral half, an operation is a bare `OpDatum`: `τ : Prep D → CSpace D` with `mem_body`
  (CA:46). Nothing ties it to a table, an effect map or a protocol.
- In the classical half, an operation is a permutation of a finite carrier (`acts`, `actWord`, CQ:56). It acts
  on priors by pushforward, and its inverse is a power of itself (CQ header; finite order on a finite carrier).
- The only observation in the classical half is **passive**: it reads `vis` and does not disturb. That is the
  ℂ-free analogue of `passive_branch_scalar` (PassiveObservation:215). The only record-*writing* observer in the
  kernel, `recordInstr` (InternalObserver), is ℂ-typed.

## 2. Per-field ledger

### 2.0 Productivity test (fixed before the probes, §A.31)

A result counts as a gem only if both hold:
1. it says something strictly stronger than "field X is unsourced";
2. it either decides a field's outcome with a witness or countermodel, or exposes an assumption hidden in how
   the field is stated.

Below that bar a result is record-only.

### 2.1 The bridging construction every "A" below uses: the protocol tower PT (not landed)

The data are the landed classical data types:
- `Ω` with `φ : Equiv.Perm Ω`;
- `vis : Ω → I`;
- a probability weight `μ`;
- an action menu `acts : A → Equiv.Perm Ω` (CQ:56).

**Stage n.**
- Preparations: pairs `(σ, r)` with `σ` a word of length ≤ n over {observe, idle, actions} and `r` its record,
  with positive conditioning weight.
- Effects: pairs `(σ′, B)`, where `B` is a set of records.
- Table: `p((σ′,B),(σ,r)) = μ{ω : rec σ ω = r, rec σ′ (σ·ω) ∈ B} / μ{ω : rec σ ω = r}`.
- Forward maps: label inclusions.

`trajProb` (PQ:339) is the passive special case. The construction is the oistage note's PT, re-derived here.
It is **one definition, with no new premise**. It is not in the kernel. On an infinite carrier the lattice form
CT replaces `μ` by the uniform product measure on regions (RT:259 `ball`, RT:398 `card_fibre`).

### 2.2 Probes

Every probe is in `scratchpad/sa/` and was run as `python3 -I <script>`. Every output replays byte-identically.
Hashes are the first 16 hex digits of sha256.

| probe | script (sha256) | output (sha256) | result line |
|---|---|---|---|
| P1 lattice SC∞ | `p1_cone_scinf.py` (b1762b40f720eb27); argument `nonlinear`, then `linear` | `p1_out.txt` (efc2f0c0a5a7fb12) | per rule: uniform 25/25 equal; parity 25/25 (vacuous, see below); boundary-pinned 8/25; `OK` |
| P2 scope | `p2_scope.py` (ab0a6c33e4e5cda3) | `p2_out.txt` (ff212d26edafd2ed) | 9 PASS, `ALL-PASS` |
| P3 rank, infinite carrier | `p3_rank.py` (1c60ed4b3ff4a061) | `p3_out.txt` (88575ef727fe9add) | ranks `[1..12]`, Hilbert det closed form for N ≤ 8, `OK` |
| P4 collapse | `p4_collapse.py` (ad7840a70107581a) | `p4_out.txt` (d9f954e61ded4a43) | 13 PASS, 1 FAIL (C7, the countercontrol, was vacuous: see below), `SOME-FAIL` |
| P4b countercontrol | `p4b_countercontrol.py` (3321edf1315a7da6) | `p4b_out.txt` (98610a9571ea3ad9) | 4 PASS, `ALL-PASS`; witness relation `[1/5, -1/5, -1/5, 1/5]` |
| P5 inverse vs rank | `p5_inverse_vs_rank.py` (612074f213157b96) | `p5_out.txt` (89952f79e5347d27) | forced `S(A)` reads `-1/2` on `e_2`; ranks `[1..10]`; `OK` |
| replay of prior notes | `oistage/oistage_checks.py`, `opact/opact_checks.py` | `replay_oistage.txt`, `replay_opact.txt` | byte-identical to the notes' `out.txt` (`OK -- 20/20`, `OK -- 26 checks`). `leap_rank.py` imports a sibling module and does not run under `-I`, so it was not replayed. |

Two pre-stated countercontrols turned out vacuous. Both are recorded, not hidden.
- **P4 C7** was expected to fail and passed. Toy 1 is passively separating: the observation-only response rank
  is 8 = |Ω|. So every permutation respects affine relations whatever the effect language is. **Prefix
  closure is therefore sufficient for AffineRespect but not necessary.** The countercontrol needs a carrier
  whose hidden part is passively invisible; P4b supplies one.
- **P1 parity.** A parity constraint over the whole region leaves the marginal on the record's cone uniform
  whenever any bit outside the cone is free. The boundary-pinned family is the effective countercontrol.

### 2.3 The ledger

| field | kernel object (file:line) | consumers | outcome | derivation chain / premise / countermodel | witness, status |
|---|---|---|---|---|---|
| **SCInf** | `SCInf` SC:78 | `val_eq_at` SC:117, `val_same_stage` SC:217, `sharpSeed_completion` SC:224, `boundary_completion` SC:232, `perfectlyDistinguishable_visible` SC:274 | **A**, construction-level: no new premise, one unlanded definition | PT over the landed data. One global `p` and inclusion forward maps make `SCInf` hold by `rfl`. On a finite carrier the substratum ingredients are `trajProb` PQ:339 and `actWord` CQ:56. In the lattice form CT: `iterate_dependsOnlyOn_ball` RT:283 (cone) + `card_fibre` RT:398 (uniform fibres) + an action-interleaved cone lemma that is **not landed**. **Content (skeptical reading):** SC∞ is exactly projective consistency of the finite marginals of *one* global law. Any substratum with a global probability measure supplies it, and it carries no elementary or quantum content. | exact P1: uniform law at the exact cone radius equals the law at radius+1, 25/25 protocols for both rules, with local flip/swap actions interleaved. Countercontrol: the boundary-pinned (non-projective) family breaks it, only 8/25 equal. Kernel countercontrol `badD`/`not_scInf_bad` SC:342/350. Written: PT `rfl`. |
| **BinaryVisible** | `BinaryVisible` SC:244 | `visible_test_completion` SC:260, `perfectlyDistinguishable_visible` SC:274 | **A**, and **vacuous as stated** | PT with binary `vis`: `v0 i = (observe, {0})`, `v1 i = (observe, {1})`, carried by inclusion. **Hidden assumption exposed:** the structure requires only `p(v0)+p(v1)=1` and naturality. It is satisfied by the zero/unit pair on a one-point body, and by one constant-½ effect paired with itself. It enforces neither distinctness, sharpness nor a nontrivial body. All the scope content is in the *extra* hypotheses `h0`, `h1` of SC:274 (a sharp visible pair). In PT such a pair exists iff some protocol makes the next visible read certain both ways: yes on P4's toy, no on P3's tower. | exact P2 (a), (a2); P4 C3, C3b. |
| **FiniteRank** | `FiniteRank` SC:299 | `exists_chart_of_finiteRank` SC:304, `exists_completionChart` CA:154, then every `CompletionChart` consumer (CA, CO, TB) | **A on finite carriers, C on infinite carriers** | Finite Ω: `prepVec x = R(ν_x)` with `R` linear on ℝ^Ω, so the rank is at most the number of response classes, at most \|Ω\|. That is a written proof, and P4 C6 shows the rank stabilises at 8. But NG1 then makes the body a polytope (§3). Infinite Ω, **countermodel**: Ω = ℤ, φ(n) = n−1, `vis = [n=0]`, μ(n) = 1/((n+1)(n+2)). Then `val(e_m, x_k) = (k+1)/(k+m+1)`, i.e. diag × Hilbert, which is nonsingular for every N (Cauchy determinant, citation). So the preparation vectors are linearly independent for every N and `¬FiniteRank`. SC∞ and `BinaryVisible` hold on the same tower. **No non-disguised premise found.** Bounded stage rank, a finite fiducial effect set and finite predictive dimension are each FiniteRank restated (R0 below). Capacity two does not imply it: a centrally symmetric infinite-dimensional ball has capacity ≤ 2 by Lemma D (KF:632, any normed V). | exact P3 (ranks 1..12, Hilbert determinants N ≤ 8); P4 C6. R0 `FiniteRank ⇔ rank[val] < ∞` under SC∞ is prior (rank note §1), re-derived as written. The OI lattice evidence (nonlinear rule ≥ 154 at n = 8) is prior, finite-horizon, not a proof. |
| **elementary-scope predicate** | none (SC header lines 11–14: "the name ELEM is reserved") | the K∞-Geom branch (`relStrictConvex_of_supporting_singleton` KF:575), as its scope | **C for derivability; B with one premise** | **Not derivable.** The Z3-cycle protocol tower (binary `vis`) satisfies SC∞, `BinaryVisible` and FiniteRank (affine dimension 2), and has **three** preparations perfectly distinguished by three stage effects summing to the unit (capacity 3, a triangle). The sum is exactly one on every preparation,
 because every state yields one of the three itineraries, so it holds on the closed hull too (written). **No intrinsic construction found.** "The face generated by a perfectly distinguishable extreme pair" fails: in a triangular bipyramid the apexes N, S are extreme and perfectly distinguishable, their midpoint is interior, so the face is the whole body, and the equator triple is perfectly distinguishable (capacity 3). **Premise (ElemScope, §4 P-D):** `BinaryVisible` with a sharp pair, and no three states of `chartBody C` perfectly distinguishable by `fullEffects`. **Load-bearing:** the Z3 tower and the qutrit fail it, and the census's `diag(1,1,0)` counterexample lives on the qutrit. **Not the conclusion in disguise:** the square satisfies it (Lemma D, KF:648, central symmetry) and is not `RelStrictConvex` (KF:762). Within finite complex QM, capacity with all effects equals the Hilbert dimension (citation), so the predicate selects exactly the qubit. **Reading constraint:** "read on the visible factor alone" must mean records of visible outcomes after arbitrary operations, not passive reads. With passive-read tests, AffineRespect fails for hidden-coupling actions (P4b). | exact P2 (b), (b2), (c)–(c3), (d), (e); kernel Lemma D KF:632/648, `not_relStrictConvex_square` KF:762. |
| **OpDatum** | `OpDatum` CA:46 | every CA/CO theorem | **A, in two senses** | (i) **Trivially:** `idDatum` CO:228 is an `OpDatum` with `affineRespect_idDatum` CO:237, and `induced_idDatum` CO:250 makes it its own inverse. So the *existence* form of K∞-Act ("an OpDatum with AffineRespect and an inverse datum") is discharged by the identity. **Hidden assumption exposed:** the obligation has content only relative to the family of operations the downstream consumes. (ii) **For the observer's interventions:** `τ_a x := prepVec (x·a)` (append `a` ∈ menu ∪ {idle}), with `mem_body` from `prepVec_mem_body` SC:167. It is Prep-valued and stage-raising (n → n+1), so it is **not** `StagePreserving` (CO:234). | written; P4 (construction). |
| **AffineRespect** | `AffineRespect` CA:58 | `existsUnique_induced` CA:258 (and conversely `affineRespect_of_induced` CA:264) | **A** under a prefix-closed effect language, which PT has by definition; abstractly **B** with the premise `LabelDual` (§4 P-A) | **Label dual:** `p(e, x·a) = p(a·e, x)`, where `a·e` prefixes `a` to the test's protocol. Then `(τ_a x)(e) = val(a·e, x)`, and every finite affine relation among preparation vectors is killed coordinatewise (`lp.ext`). No SC∞ and no FiniteRank are used. **Load-bearing:** P4b, where with observation-only tests the controlled flip violates 20 of the 22 basis relations of D, witness `(δ00−δ01−δ10+δ11)/5`; kernel `midOp_not_affineRespect` CA:461. **Not necessary:** P4 C7. **Disguise check:** under a chart, AffineRespect ⇔ every pulled-back coordinate is a *finite real* affine combination of stage coordinates (§4 P-B), so a "finite dual" premise would be AffineRespect restated. The *label* dual is strictly stronger and non-disguised. It is countable, so it never yields a flow member (countable no-go, prior, re-read). | exact P4 C4 (3486 instances), C5 (76 relations, 0 violated, for idle and flip), P4b. |
| **inverse datum** | an `OpDatum S` with `AffineRespect S` (the `S` of `inducedEquiv` CA:333) | `comp_eq_id` CA:328, `inducedEquiv` CA:333, `preservesBody_inducedEquiv` CA:352, CO:348 | **A on finite carriers, C on infinite carriers** (B with the premise `InverseClosedMenu`, which the probe shows can cost FiniteRank) | Finite Ω: every menu permutation has finite order, so its inverse is a word in the menu (CQ header, §A). P4 C8b: ord(φ) = 8. Infinite Ω, **countermodel P5(i):** φ(n) = n−1 is a bijection of ℤ, μ geometric, menu {observe, idle}. FiniteRank holds: the body is the segment [A, D], rank 2. Yet W(A) = A/2 + D/2 and W(D) = D, so any S with `Undoes` has S(A) = 2A − D, which reads −1/2 on `e_2` and is not in the body. **Substratum reversibility (A2) does not give the inverse datum on the body.** P5(ii): adding the un-step φ⁻¹ to the menu restores it, but the matrix [min(1, 2^{j−m})] has full rank for every N (row differences are triangular with diagonal 1/2, written), so FiniteRank fails. | exact P5, P4 C8b. |
| **Undoes** | `Undoes` CA:325 | `comp_eq_id` CA:328, `inducedEquiv` CA:333 | **A** given label duals and a chart | For Prep-valued `S`, `T` with label duals `σ_S`, `σ_T`: `(after C S T).τ x (a) = val(σ_T (σ_S a), x)`. So `Undoes` ⇔ `σ_T ∘ σ_S` is the identity on label *values* (§4 P-C). In PT it is the identity of posteriors, `ν_{x·a·a⁻¹} = ν_x`. This needs a `CompletionChart`, i.e. FiniteRank, even to be stated. | exact P4 C8 (flip involution), C8b, P4b; written. |

## 3. Collapse analysis

### 3.1 The collapse exists

**One prefix-closed protocol tower over the landed classical data discharges all seven named fields together:**
`SCInf`, `BinaryVisible` (binary `vis`), `OpDatum`, `AffineRespect`, the inverse datum and `Undoes`, and also
`FiniteRank` when Ω is finite. The tower must have an inverse-closed menu, which is automatic on a finite
carrier.
- Witness: exact P4 (C1–C8b) together with the written proofs in §2.3.
- This confirms the oistage note's F-S1 and goes beyond it: a passively separating carrier (P4 C7) needs no
  prefix closure at all.

It answers the mission's question "does a single prefix-closed protocol tower with a reversible step datum give
SCInf, BinaryVisible and OpDatum+Undoes at once" with **yes, at construction level, with no new premise**.

### 3.2 The collapse is self-defeating downstream

Every body the collapse delivers falls into a regime where a landed or re-read no-go excludes the next seams.

| regime | what the collapse gives | what then fails | chain |
|---|---|---|---|
| finite Ω (the landed `[Fintype S]` architecture) | all seven fields | **K∞-Trans** for chart dimension ≥ 2; **K∞-Drive** for every dimension | **NG1** (prior; re-checked: P4 C9 finds 170 posteriors to horizon 6, every posterior is (μ∘σ⁻¹)·1_C normalised) makes the body a polytope. A polytope of dimension ≥ 2 has a non-extreme boundary state (an edge midpoint), so `not_boundaryTransitive_of_nonextreme_boundary` (TB:301) excludes every body-preserving family. Dimension 1 is a segment, and `not_drivable_Icc` (KF:529) applies up to affine equivalence. Every induced map has finite order: the finitely many posterior images span, as in the proof of CO:348 (written). A polytope has no continuous nontrivial automorphism flow, so `ElementaryDrivability` fails (written). |
| infinite Ω, FiniteRank holds, the step has an inverse datum | the seven fields, given an inverse-closed menu | **K∞-Trans** for chart dimension ≥ 2 | **NG2** (prior; proof re-read, every step checks): passive reads mean the branches τ_v are positive linear maps with Σ_v τ_v = W. W reversible gives M_v = W⁻¹τ_v positive with Σ M_v = I, so every extreme ray is an eigenvector of every M_v. If d+2 extreme points are in general position, M_v = λ_v I, every record law is state-independent, and the body is a point. Boundary transitivity forces every boundary state to be extreme (`extreme_of_isBoundaryState_of_transitive`, TB:290). In chart dimension ≥ 2 the boundary then supplies d+2 extreme points in general position (written), a contradiction with `chartBody_interior_nonempty` (TB:121). |
| infinite Ω, FiniteRank holds, the step has no inverse datum | SC∞, `BinaryVisible`, `OpDatum`, `AffineRespect` | the inverse datum for the step (P5(i)) | P5. NG2 is then silent: its hypothesis is invertibility of W on the body. |
| infinite Ω, FiniteRank fails | SC∞, `BinaryVisible`, `OpDatum`, `AffineRespect`, inverse | no chart, so `Undoes`, `inducedEquiv` and TRB-1 cannot even be stated | P3, P5(ii) |
| any Ω: the operations the tower itself supplies | a **countable** family (words over a countable menu) | **K∞-Trans** on `eball 3` | `not_boundaryTransitive_of_countable` (EffectSpace:858) is kernel. In any chart dimension ≥ 2 the boundary of a compact convex body with interior is uncountable, while one orbit of a countable family is countable (written). So a sourced transitive family must include **limits** of protocol operations, which are completion-valued and not Prep-valued. This agrees with the countable no-go (prior) and F-D3, now kernel CO:348/378. |

**Net.** In the landed passive architecture, K∞-Stage plus K∞-Act are cheap. The obstruction lies in the *source
regime* they force, not in any Stage/Act field. Two escapes stay open, and neither is landed in field-neutral form:
- **(E1) invasive, record-writing observation**, which drops NG2's passivity hypothesis. Its ℂ instance is
  `recordInstr_writes` / `recordInstr_not_passive` (InternalObserver:272/290).
- **(E2) a step that is irreversible on the body, with reversible interventions**, which drops NG2's
  W-invertibility. It is implicit in NG2's hypotheses, but the prior notes do not pursue it as an escape. It is
  unexplored here, and no model is offered. P5(i) shows that such steps occur on infinite carriers even when the
  substratum map is a bijection.

Either escape must also come with a **closure** of the countable operation family (Γ-type: the compact
`Aut(chartBody)`, Γ0 now kernel TB:109/121) before K∞-Trans can hold.

### 3.3 The specific collapse questions of the mission

- **Does FiniteRank follow from anything?** From landed structure, only from finiteness of the carrier, and
  that is exactly the regime NG1 closes. On infinite carriers nothing landed implies it (P3). Every stage-level
  equivalent found (R0's bounded protocol rank, a finite fiducial set) is a restatement. ElemScope (capacity
  two) does not imply it (§2.3).
- **Does AffineRespect follow from how operations act on stage frequencies?**
  - From the preparation side alone (Prep → Prep): **no**. Countermodels are `midOp` (kernel CA:461) and P4b.
  - From a label-level action on effects (the Heisenberg-side dual `e ↦ a·e`): **yes**, with no SC∞ and no
    FiniteRank (§4 P-A).
  - From a real-coefficient finite dual: yes, but that is AffineRespect restated (§4 P-B).
- **Do the prior no-gos decide any field as C?**
  - F-D1 (the ℂ route forces the Bloch ball) decides that supplying K∞-Act from the ℂ half is circular. It
    decides no field-neutral field.
  - F-D3 (CO:348), the countable no-go and EffectSpace:858 decide that **no** collapse via Prep-valued or
    label-dual data can carry K∞-Drive's flow or K∞-Trans. They decide no Stage/Act field, because K∞-Act does
    not ask for infinite order or transitivity.
  - EFFCLOSE versus drive bears on V4′, not on Stage/Act. ElemScope is stated on `fullEffects` of the chart
    body, not on `stageEffects`, so it does not inherit that conflict.
  - NG1 and NG2 decide no Stage/Act field. They decide that the collapse's bodies fail K∞-Trans (§3.2).
  - The leap ranks 1, 4, 6, … (≥ 154) are finite-horizon evidence and decide nothing. P3 is the decision for
    FiniteRank on infinite carriers.
  - The fields actually decided as C here are **FiniteRank** (infinite carriers, P3), the **inverse datum**
    (infinite carriers, P5) and **derivability of the elementary scope** (P2).
- **Can the elementary-scope predicate be stated so that these no-gos are avoided?** It can be stated so that it
  *triggers* none of them:
  - on the completed chart body, not on a finite stage (a finite stage exposes at most |P| points,
    `FiniteStage.exposed_le_card` KF:868);
  - with `fullEffects`, not `stageEffects`, which avoids the EFFCLOSE conflict;
  - with no flow or order clause, which avoids F-D3 and the countable no-go.

  **No scope predicate can avoid NG1 or NG2.** Those constrain the *source* (finite carrier; passive reads with
  a reversible step), and capacity-two polytopes exist (the segment; the square, P2(e) with Lemma D). The
  scope predicate and the source escape are separate obligations.

## 4. Proposed theorem statements (proposals, not proved)

These are **proposals only**: not kernel-checked, not frozen, and not to be cited as results. Names are
illustrative. Each carries its intended hypotheses and the countercontrol that must fail. "Proof idea" marks a
written sketch, not a proof.

**P-A. Label dual gives AffineRespect** (no SC∞, no FiniteRank).
```lean
def LabelDual {D : DirectedStages} (T : OpDatum D) (σ : Label D → Label D) : Prop :=
  ∀ a x, T.τ x a = val D (σ a) x
theorem affineRespect_of_labelDual {D : DirectedStages} {T : OpDatum D} {σ : Label D → Label D}
    (h : LabelDual T σ) : AffineRespect T
```
- Proof idea: evaluate `∑ c x • T.τ x` at `a` with `sum_smul_apply` (CA:423). It equals
  `(∑ c x • prepVec D x) (σ a) = 0`.
- Countercontrols that must fail `LabelDual` for every `σ`: `midOp` (CA:419; kernel `¬AffineRespect`), and the
  controlled flip with observation-only tests (P4b).
- Non-disguise: `LabelDual` ⇏ every AffineRespect datum. The irrational rotation of the ball tower is
  AffineRespect, and its pullbacks are stage effects for at most countably many angles (countable no-go).

**P-B. AffineRespect is exactly a finite real dual, under a chart** (records that a "finite dual" premise is a
restatement).
```lean
theorem affineRespect_iff_finiteDual {D : DirectedStages} (C : CompletionChart D) (T : OpDatum D) :
    AffineRespect T ↔ ∀ a : Label D, ∃ (s : Finset (Label D)) (l : Label D → ℝ) (m : ℝ),
      ∀ x, T.τ x a = m + ∑ b ∈ s, l b * val D b x
```
- The (←) direction needs no chart.
- The (→) direction uses `existsUnique_induced` (CA:258). The coordinate functionals separate points of the
  finite-dimensional direction, so d of them coordinatise the chart.
- Countercontrol for the (→) direction without a chart: none found. The statement is recorded with its
  hypotheses.

**P-C. Undoes from label duals.**
```lean
theorem undoes_of_labelDual {D : DirectedStages} (C : CompletionChart D) {S T : OpDatum D}
    (hS : AffineRespect S) {σS σT : Label D → Label D} (dS : LabelDual S σS) (dT : LabelDual T σT)
    (hinv : ∀ a x, val D (σT (σS a)) x = val D a x) : Undoes C S T hS
```
- Proof idea: `chart_coordsOf` (CA:175), `induced_gen` (CA:281), and `lp.ext` on the coordinates.
- Countercontrol: the reset datum, which is AffineRespect with no inverse (OPACT E7, prior), and the idle step
  of P5(i). For each, `hinv` fails for every candidate σS.

**P-D. The elementary scope, ElemScope** (a definition, the one field-neutral premise for the scope).
```lean
structure ElemScope (D : DirectedStages) (C : CompletionChart D) extends BinaryVisible D where
  sharp : ∃ (i : D.ι) (x0 x1 : (D.stage i).P),
    (D.stage i).p (v0 i) x0 = 1 ∧ (D.stage i).p (v1 i) x1 = 1
  cap2  : ∀ (x : Fin 3 → (Fin C.d → ℝ)) (e : Fin 3 → (Fin C.d → ℝ) →ᵃ[ℝ] ℝ),
    (∀ k, e k ∈ fullEffects (chartBody C)) → ¬ PerfectlyDistinguishable (chartBody C) x e
```
- Intended consequences:
  - with `SCInf`, a perfectly distinguishable visible pair, from SC:274 transported along `coordsOf`, so
    capacity exactly 2;
  - Lemma D gives `cap2` for every centrally symmetric chart body, the ball included.
- Countercontrols:
  - the Z3 protocol tower satisfies `SCInf`, `BinaryVisible`, `sharp` and FiniteRank, and **fails `cap2`**
    (P2(b));
  - the qutrit with every effect fails `cap2` (P2(d));
  - the bipyramid shows that `cap2` cannot be replaced by a capacity statement about the face generated by a
    sharp pair (P2(c)).
- Non-disguise: the square satisfies `cap2` (KF:648) and fails `RelStrictConvex` (KF:762), so
  `ElemScope ⇏ K∞-Geom`.
- Caveat for the governed round: KINF-1 halted over unit-effect handling. `PerfectlyDistinguishable`
  (KF:154) requires the effects to sum to one on Ω, and the unit may occur among the `e k`. If one `e k` is the
  unit, the other two vanish on Ω and cannot be certain on their own states. So the unit opens no loophole in
  `cap2`. This should still be re-checked when the definition is frozen.

**P-E. FiniteRank is bounded stage rank** (prior R0, re-derived; a restatement, recorded so it is not mistaken
for a source).
```lean
def StageRank (D : DirectedStages) (i : D.ι) : ℕ :=
  Module.finrank ℝ (Submodule.span ℝ (Set.range fun x : (D.stage i).P => (D.stage i).vec x))
theorem finiteRank_body_iff (hSC : SCInf D) :
    FiniteRank (body D) ↔ ∃ n, ∀ i, StageRank D i ≤ n
```
- Countercontrol: P3's tower has unbounded stage ranks and `¬FiniteRank`.
- Note: the (←) direction uses SC∞ to identify `val` with stage tables. Without it, `val` reads at the *chosen*
  upper stage. No countercontrol for dropping SC∞ was run, so the need for it is a statement of the proof route,
  not a tested claim.

**P-F. The protocol tower and its collapse package** (a construction; no premise beyond the data and, for
infinite Ω, an inverse-closed menu).
```lean
def protocolTower (Ω : Type) (φ : Equiv.Perm Ω) (vis : Ω → Bool) (μ : Ω →₀ ℝ) (A : Type) [Fintype A]
    (acts : A → Equiv.Perm Ω) : DirectedStages
theorem protocolTower_scInf : SCInf (protocolTower Ω φ vis μ A acts)          -- by rfl
def protocolTower_binaryVisible : BinaryVisible (protocolTower Ω φ vis μ A acts)
def appendOp (a : Option A) : OpDatum (protocolTower Ω φ vis μ A acts)
theorem appendOp_labelDual (a) : LabelDual (appendOp a) (prefixLabel a)
theorem undoes_appendOp_inv [Fintype Ω] (C) (a : A) : Undoes C (appendOp (inv a)) (appendOp a) _
theorem protocolTower_finiteRank [Fintype Ω] : FiniteRank (body (protocolTower Ω φ vis μ A acts))
```
- Countercontrols:
  - for `protocolTower_finiteRank` without `[Fintype Ω]`: P3;
  - for `undoes_appendOp_inv` without `[Fintype Ω]` and with the menu not inverse-closed: P5(i);
  - for SC∞ of the lattice form (CT) with a non-projective region family: P1's pinned boundary.
- Kernel cost: `μ` as a probability weight on an infinite Ω needs measure-level sums. A finite-Ω round is
  cheap. CT needs the action-interleaved cone lemma.

**P-G. The finite collapse excludes boundary transitivity** (records a downstream no-go that the collapse
triggers).
```lean
theorem not_boundaryTransitive_protocolTower [Fintype Ω] (C : CompletionChart (protocolTower …))
    (hd : 2 ≤ C.d) (G : Set ((Fin C.d → ℝ) ≃ᵃ[ℝ] (Fin C.d → ℝ))) (hG : PreservesBody (chartBody C) G) :
    ¬ BoundaryTransitive (chartBody C) G
```
- Proof idea: NG1 gives finitely many posteriors, so `chartBody C` is a polytope. A polytope in dimension ≥ 2
  has a non-extreme boundary state, and TB:301 finishes.
- Countercontrol showing `2 ≤ C.d` is load-bearing: the segment, with the swap. A two-class tower
  (`bitTower`-like) is boundary transitive under the reflection.

**P-H. NG2, field-neutral passive no-go** (prior statement; proof re-read; the hypotheses made explicit).
```lean
theorem ng2 (C : CompletionChart D) (V : Type) [Fintype V] (τ : V → OpDatum D)       -- branch data
    (hlin : ∀ v, AffineRespect (τ v)) (W S : OpDatum D) (hW …) (hSW : Undoes C S W _) (hWS : Undoes C W S _)
    (hsum : ∀ x, ∑ v, unnormalised (τ v) x = W.τ x)                                 -- observe-and-forget = W
    (hgen : effects are generated by records of τ)                                    -- PT/CT form
    (hgp : ∃ d+2 extreme points of chartBody C in general position) : C.d = 0
```
- Statement sketch only. The branch maps are unnormalised, so they live on the cone, not on the body. A
  faithful kernel form must use the cone over `chartBody`.
- Countercontrol: the prior note's invasive rebit (Q1–Q4, rank 3, infinite-order idle, observe-and-forget ≠ idle)
  violates `hsum` and has a non-polytope body.

## 5. What this thread does NOT decide; interface questions for K2

**Not decided here.**
- Whether any OI lattice rule with the uniform product measure has finite rank. The prior evidence is mixed:
  the linear rule has passive rank 1, and with flip and swap protocol rank 3 at L ≤ 3, with no bound proved; the
  nonlinear rule reaches ≥ 154 at n = 8. P3 is a countermodel on an infinite carrier with a non-uniform
  probability weight, not a lattice rule.
- Whether escape E1 (invasive, record-writing observation) or E2 (a step irreversible on the body) can be stated
  field-neutrally and yields a strictly convex finite-rank body. No model is offered for either.
- Whether ElemScope (P-D) is the right scope predicate for a successor foundations round. It is offered as the
  one premise that scopes K∞-Geom away from the census counterexample class without implying K∞-Geom. Choosing
  it is a governed-round decision.
- Anything about K∞-Drive, K∞-Trans, K∞-Seed, K∞-V4, K∞-Copy, K∞-Geom or Kₙ, beyond the downstream exclusions
  in §3.2, which are statements about the collapse's bodies only.
- Whether the action-interleaved cone lemma for CT holds in general. P1 checks instances with local actions at
  the visible site, at protocol length ≤ 3.
- Every negative result here is scoped to the construction actually tested: the passive protocol towers PT and
  CT over the landed classical data. None of them says that no observer-level extension can supply the seams.

**Interface handed to the K2 thread: what "reversible local action" K∞-Act would deliver.** If K∞-Act is
supplied by the collapse, a reversible operation on one elementary system is a datum with all of the following
properties:
1. **Typed.** It is an `OpDatum` that is Prep-valued and stage-raising: `τ_a x = prepVec (x·a)`.
2. **Effect side.** It carries a **label dual** `e ↦ a·e`: it maps stage effects to stage effects (P-A). Its
   induced map on the chart is `inducedEquiv` (CA:333), and it preserves the body (CA:352).
3. **Order and cardinality.** On a finite carrier it has finite order (NG1). The family it generates is
   countable in every case, so it is never a flow member (countable no-go) and never boundary transitive in
   dimension ≥ 2 (EffectSpace:858 for `eball 3`; written in general).
4. **Not completion-valued.** Members of a flow or of a transitive family must be limits of such data:
   completion-valued, with no label dual.

**Questions for K2, each decidable on its side.**
- **(K2-a)** Given two protocol towers with label-dual operations `a` and `b`, the product protocol tower carries
  `a ⊗ id` with label dual `(a·e) ⊗ f`. Does its induced map preserve COMP-1's composite body (`PreservesBody`
  of a `Composite`, CompositeInterface:243) for the minimal body, the maximal body, and the candidate d = 3 body?
  - Expectation, not checked: yes for the minimal and maximal bodies, since products of automorphisms preserve
    both.
  - The open part is the candidate body.
- **(K2-b)** A product of classical carriers with joint permutations yields simplex composites. DIM-1's
  `Entangling` therefore cannot come from the passive collapse on finite carriers. K2 should not assume that
  the local actions it composes come with an entangling joint action from the same source.
- **(K2-c)** K2's local actions must be compatible with **completion-valued** limits, not only with label-dual
  data. Is COMP-1's `jointReversible_words` (CompositeInterface:449) stable under pointwise limits of the factor
  actions on the chart? This is the place where K∞-Trans's closure requirement meets the composite.
- **(K2-d)** ElemScope is a capacity-two statement on one factor. K2 should check that the candidate composite
  of two capacity-two factors has capacity four. That is a consistency check of the scope predicate against
  local tomography, not a premise.

## 6. Verdict

**The architecture as landed can supply K∞-Stage and K∞-Act, but only together, and only in regimes that close
the route.** The kernel contains no `DirectedStages` or non-trivial `OpDatum` built from any OI object.

**What one construction supplies.** A single unlanded but premise-free construction over the landed classical
data, the prefix-closed protocol tower (§2.1), supplies `SCInf`, `BinaryVisible`, `OpDatum`, `AffineRespect`,
the inverse datum and `Undoes` at once (A, construction-level). It adds `FiniteRank` on finite carriers. Exact
P4/P4b and P1 witness this.

**Two of the fields are near-empty as stated.**
- `BinaryVisible` is satisfied by a zero/unit pair on a one-point body.
- The existence form of K∞-Act is discharged by the identity datum, `idDatum` CO:228.

The content of each lies in a hypothesis the seams audit does not name: a sharp visible pair, and the specific
operation family the downstream consumes.

**What is decided as C.**
- **FiniteRank** on infinite carriers (P3: Hilbert matrix, every N).
- The **inverse datum** on infinite carriers even with FiniteRank (P5(i)). Restoring it by an inverse-closed
  menu can destroy FiniteRank (P5(ii)).
- **Derivability of the elementary scope** (P2: the Z3 tower has capacity 3; the bipyramid defeats the
  face-of-a-sharp-pair construction).

**The scope needs one sharply named premise.** ElemScope (P-D) is capacity at most two on `fullEffects` of the
chart body, with a sharp visible pair. It is load-bearing (the Z3 tower and the qutrit fail it). It is not
K∞-Geom in disguise (the square satisfies it: kernel Lemma D plus `not_relStrictConvex_square`).

**AffineRespect has one non-disguised source.** It is the label-level (Heisenberg-side) dual (P-A). A real
finite dual is AffineRespect restated (P-B).

**The collapse is self-defeating downstream.**
- Finite carriers give polytopes (NG1), so K∞-Trans fails by the kernel's TB:301 and K∞-Drive fails.
- Infinite carriers with FiniteRank and a reversible step give bodies NG2 excludes from boundary transitivity
  (with TB:290).
- In every regime the supplied operations are countable, which EffectSpace:858 excludes from transitivity on
  `eball 3`.

So the live obligation upstream of the ball is not any Stage/Act field. It is the **source regime**: an
invasive (record-writing) observation, or a step irreversible on the body, together with a closure of the
countable operation family. Neither is landed in field-neutral form.

**Classification (§A.31).**
- **NEW:**
  - `BinaryVisible` is vacuous as stated, and the existence form of K∞-Act is discharged by `idDatum`. Both are
    hidden assumptions in the seams audit's formulation.
  - The P3 proof that the landed data types on an infinite carrier do not force FiniteRank.
  - P5: a bijective substratum step with no inverse datum on a finite-rank body, and the un-step's cost in
    FiniteRank.
  - The bipyramid separation for the face-of-a-sharp-pair scope.
  - The countable-family exclusion of K∞-Trans for every collapse-supplied family, a kernel link via
    EffectSpace:858.
  - Escape E2.
- **POSITIVE:**
  - ElemScope as a load-bearing, non-disguised scope predicate.
  - The label dual as the non-disguised source of AffineRespect.
- **CONFIRMING:**
  - oistage F-S1, NG1 and NG2; rank R0; drive F-D3, which ORD-1 has since landed at CO:348.
  - Prefix closure is sufficient but not necessary (P4 C7), which refines F-S1.

The fixed point (§A.31: 3–4 passes without NEW findings) was **not** reached in this thread. The NEW items above
came from the first passes, so further passes on E1, E2 and the CT cone lemma are where the next round of
gem-finding belongs.
