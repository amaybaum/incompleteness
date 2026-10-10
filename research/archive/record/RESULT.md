# RECORD — record-writing observer interface (read-only, base 0f2687b7)

**Question.** Does letting observation write an external record and disturb the system remove the passive-readout
obstruction while leaving a fixed 4-dimensional system-effect space invariant under the non-selective dynamics?

**Status.** SEALED 2026-10-03. All four simulator-validation gates passed; no pending items. Read-only, off-repo;
no act, freeze or repository implication. Artifact hashes and this file's hash: SEAL.md.

## 0. Headline

> Level 1 is too weak to expose linear disturbance: under the linear rule every interface gives an i.i.d. fair
> record (written proof). Level 2 exposes it, and the linear orbit span remains at certified dimension 3
> through the tested horizon, while the nonlinear and majority orbit spans are certified to exceed 4. R4-global is excluded for
> nonlinear and majority at both levels (certified table ranks > 4). R4(r; G) is excluded for majority at both
> levels and for nonlinear at both levels; seven of the nonlinear Level-1 exclusions come from a post-freeze
> diagnostic. Linear is the only rule whose R4 status remains open, and all its evidence is UNDER-RANK: at Stage B
> (horizon 4) all 76 invasive linear interfaces keep certified table rank 3 and C dims [2, 3, 3, 3].

Preregistered terminal label (FREEZE, unchanged): **ALL FAIL** — no rule passes Q2 at either level.

## Provenance boundaries

1. **Frozen result** — FREEZE's Stage-A/Stage-B decision rule and the preregistered label; unchanged by anything
   below.
2. **Layered interpretation** — G / R4-global / R4(r; G) / Q reading of the same evidence (ADDENDUM-LAYERS.md,
   written before any Level-2 output existed).
3. **Post-freeze evidence** — the seven-interface depth-4 diagnostic and every guard-bypassed check, marked where
   used. It cannot change the frozen label; it may strengthen mathematical conclusions, which then rest on exact
   certified lower bounds, not on a frozen criterion.

Every conclusion below is tagged by evidence type: frozen verdict, exact lower-bound theorem, finite-horizon
observation, or post-freeze diagnostic.

## 1. What was frozen and run

- FREEZE.md (sha256 b66b1a69…) before any computation: interface class IC, search rule, criteria, stages, labels.
  ADDENDUM-LAYERS.md (662428cf…), the layered reading on owner direction, written while Level 2 was running and
  before any Level-2 output existed (Level-1 outcomes were already known); it changes no computation or criterion.
- **Interface class IC.** An observation O_κ, κ = (κ_0, κ_1): read b = v_0; append b to the external record;
  disturb (u_0, b) ↦ κ_b(u_0), with κ_b an injection of the two branch inputs into the four pair states; one leap.
  The joint system × record update is injective; the non-selective map is f_κ(ω) = κ_{v_0(ω)}(ω). |IC| = 144;
  the passive member is excluded: **143 interfaces**, each run for all three rules (linear, nonlinear, majority).
- **Letters.** o (selective observation), i (leap), m (non-selective observation); Level 2 adds f (flip v_0) and
  s (swap u_0, v_0). Preparations over {o, i} (L2 {o, i, f, s}); effects over {o, i, m} (L2 {o, i, m, f, s});
  generators G_1 = {i, m}, G_2 = {i, m, f, s}; seed r = (o, outcome 1).
- **Search.** Stage A: all 143 × 3 at L_p = L_e = 3. Stage B (L_p = L_e = 4): every pair with C_2 = C_1,
  dim ≤ 4, invariant. Level 2 ran because Level 1 ended ALL FAIL, for all rules alike. 429 Stage-A runs per level.
- **Exactness.** Exact window simulator (record_sim.py, e499a081…), validated V0 against QUOTIENT's simulator
  (34 protocols × 3 rules, 0 mismatches) and V1 against brute-force cone enumeration (114 pairs, 0 mismatches).
  Every table rank certified by the rank-basis method (full table, greedy columns, exact ℚ independence and
  spanning); WELLDEF checked on every generator.
- **Simulator-validation gates** (fast evaluator record_fast.py, c2c94a68…, int64 + prefix sharing, against the
  reference record_sim):
  1. *Protocol level:* 5046 evaluations byte-equal — the full Level-1 Stage-A protocol set (418) for 2 κ × 3 rules,
     and 282 random Level-2 protocols (length ≤ 7) for 3 κ × 3 rules; 0 mismatches (validate_fast.py).
  2. *Level 1, full artifact:* the whole Level-1 Stage A recomputed on the reference simulator; stageA_L1.json is
     byte-identical to fast_stageA_L1.json, sha256 36ff602ac11e19023bba3f95443af9f8d33370ceccf9e4291e8dae102bfceba5.
  3. *Level 2 Stage A, sampled:* nine distinct complete jobs reproduced field-by-field on the reference simulator,
     0 mismatches. Eight came from a result-dependent stratified sample selected from the Stage-A output by rank
     extremes and verdict classes (replay_L2_sample.py; the rule produced nine picks, one nonlinear κ meeting two
     criteria); a ninth distinct job was added afterward as the first unreplayed job in frozen Stage-A order, the
     rule fixed before that replay ran and blind to its outcome: linear ((0,1),(0,2)) (replay_L2_ninth.py). Not
     preregistered; not a full Level-2 replay.
  4. *Level 2 Stage B:* executed on the fast evaluator; one complete job, fixed before any Stage-B output existed
     (linear κ = ((0,1),(0,1)), L_p = L_e = 4, protocols up to length 8), reproduced field-by-field on the reference
     simulator: identical record (preps 755, effects 1555, rank 3, certified, WELLDEF, invasive, C dims [2, 3, 3, 3],
     FAIL(dimC = 3)), MATCH (replay_stageB_gate4.py, gate4.log).
  Level-1 conclusions rest on full-artifact reproduction; Level-2 Stage A on protocol-level validation plus a
  nine-job sample; Stage B on protocol-level validation plus one preregistered complete job covering its length-8
  regime.

## 2. Definitions used in the reading

- **C(r; G)** = span({1} ∪ {w(r) : w ∈ G*}); C_k(r; G) uses words of length ≤ k.
- **R4(r; G):** there is a 4-dimensional system-effect sector E with 1, r ∈ E and g(E) ⊆ E for every g ∈ G.
  ("R4-sector" below means R4(r; G) at the stated level.) It rests on the named premise R4-MEASURED-EFFECT: the
  effect the observer actually reads belongs to the elementary system's effect sector.
- **R4-global:** the whole system-effect space has rank exactly 4.
- **Obstruction classes.** OVER-RANK: certified lower bound > 4 (terminal). UNDER-RANK: certified finite-horizon
  dimension < 4 (non-terminal). AT-RANK: certified finite-horizon dimension = 4 (non-terminal without a
  stabilization/invariance proof). R4-CLOSED: an invariant 4-dimensional sector proved structurally.

**Lemma (finite orbit-span exclusion).** For any finite horizon k and finite preparation set X,
dim(C_k(r; G)|_X) ≤ dim C_k(r; G) ≤ dim C(r; G) ≤ dim E for every E as in R4(r; G). Hence an exact certificate
dim(C_k(r; G)|_X) > 4 excludes R4(r; G). *Proof.* Restriction to X cannot raise rank; C_k ⊆ C; each g acts on
true effects as an exact dual map, so 1, r ∈ E and g(E) ⊆ E for all g ∈ G give w(r) ∈ E for every word w,
hence C(r; G) ⊆ E. ∎ The exclusion is independent of the finite-horizon well-definedness guard; the guard is
needed only for positive representation/invariance claims. A guard failure can destroy a proposed pass; it
cannot rescue a candidate already proved OVER-RANK. The same argument with the full table bounds R4-global:
a certified table rank > 4 excludes it unconditionally.

**Monotonicities.** (i) Same G, nested X ⊆ X′: dim(C_k|_X) ≤ dim(C_k|_X′). (ii) Same G, k ≤ k′: C_k ⊆ C_k′.
Both strengthen a certificate for the same object; neither can lower it. (iii) G_1 ⊆ G_2, with o, i, m
executed by the same code with the same κ at both levels: C(r; G_1) ⊆ C(r; G_2) as functionals on one state
space, so OVER-RANK propagates from Level 1 to Level 2, never back. The levels' different preparation alphabets
affect only how strongly a table certifies rank, not this inclusion. Level 2 is a different object, not a deeper
horizon of Level 1.

## 3. Question 1 — existence (layer G)

**Structural G clauses** (selective branches; injective record writing; record never acted on; unit; forgetful
non-selective operation; consistent composition). G1 and the system/record split hold by construction. Exact
checks on the Stage-A tables (layers.py, 7bf0c3fa…):

| Level | Rule | G2 forgetful sum | G3 normalization | G3 trailing-idle consistency |
|---|---|---|---|---|
| 1 | linear | 143/143 | 143/143 | 143/143 |
| 1 | nonlinear | 143/143 | 143/143 | 143/143 |
| 1 | majority | 143/143 | 143/143 | 143/143 |
| 2 | linear | 143/143 | 143/143 | 143/143 |
| 2 | nonlinear | 143/143 | 143/143 | 143/143 |
| 2 | majority | 143/143 | 143/143 | 143/143 |

Level-1 run sha256 fcf1df29…; Level-2 run (layers_L2.log) writes a byte-identical artifact, sha256 fcf1df29…,
because the records carry only rule, κ and three booleans, all true at both levels — the file does not by itself
identify its level, and the Level-2 result is cited by its log.

Countercontrol (planned, fixed κ ((1,3),(0,2)), m implemented with the branch maps exchanged, so not the forgetful
sum): G2 fails for nonlinear and majority at both levels. For linear it passes at both levels and is vacuous there —
that κ, and its exchanged mutant, are operationally non-invasive for linear at Level 1 (every κ, §6) and at Level 2.

> **Post-run countercontrol census (complete, outcome-blind; does not alter the frozen criteria).** The same
> mutation over all 143 linear κ at Level 2 (cc_census_L2.py fd6ca73b, log 060a8638): G2 fails — the mutation is
> caught — on 71 / 143; on 68 of the 76 operationally invasive κ and 3 of the 67 non-invasive ones. On the other 8
> invasive κ the exchanged-branch m coincides with the forgetful sum on every tested effect (the mutation is
> operationally null there); on the other 64 non-invasive κ it is vacuous. Linear G2 at Level 2 is therefore
> discriminating: the 143/143 pass is not a consequence of the check being unable to see a non-forgetful m.

**G-invasiveness** (forgetting the outcome differs from idling on some effect), reported separately:
state-level f_κ ≠ id for all 143 κ by construction; operational:

| Level | linear | nonlinear | majority |
|---|---|---|---|
| 1 | 0 / 143 (proved, §6) | 143 / 143 | 143 / 143 |
| 2 | 76 / 143 | 128 + 15 (a) | 143 / 143 |

(a) Provenance split. **128 / 128** recorded directly by the frozen run. **15 / 15** (the κ that exit at the
well-definedness guard before the flag is set) established separately, from the same exact probability tables with
the guard bypassed for this check only (diag_welldef.py); the check compares table rows and does not use the guard.
The same 15 are also implied by Level 1: the frozen Level-1 run flagged every nonlinear κ invasive, its witness is a
preparation over {o, i} and an effect over {o, i, m} at horizon 3, and identical protocols with the same κ have
identical probabilities at Level 2. **Combined mathematical conclusion: 143 / 143 invasive.** The frozen control flow
itself emitted 128 flags.

Reading: the structural G clauses hold for all 429 runs at each level; G-invasiveness holds for nonlinear and majority at both levels
and for linear only from Level 2. The Level-1 interface is inadequate for the linear rule — it cannot expose
disturbance — rather than the linear rule failing G as a theory.

## 4. Question 2 — finite effect closure (R4)

### 4.1 Frozen Stage A tallies (preregistered criteria)

Level 1 (sha256 36ff602a…): linear NOT-INVASIVE 143 (rank 1); nonlinear FAIL (no stabilization) 143 —
dims [2,3,4] 7, [2,3,5] 24, [2,4,6] 8, [2,4,7] 12, [2,4,8] 92; majority FAIL (no stabilization) 143 —
[2,3,5] 1, [2,4,6] 2, [2,4,8] 140. Stage B Level 1: 0 advancing pairs.

Level 2 (sha256 580d4721…): linear FAIL(dimC = 3, stabilized) 76, NOT-INVASIVE 67 (64 rank 1, 3 rank 3);
nonlinear FAIL (no stabilization) 128 — [2,4,6] 4, [2,4,7] 20, [2,5,8] 2, [2,5,9] 17, [2,5,10] 36,
[2,5,11] 49 — and INCONCLUSIVE(welldef) 15; majority FAIL (no stabilization) 143 — [2,4,8] 1, [2,5,8] 2,
[2,5,10] 12, [2,5,11] 4, [2,5,12] 24, [2,5,13] 60, [2,5,14] 40. Stage B Level 2 (sha256 339f68b5…): the 76 linear pairs, all
FAIL(dimC = 3): table rank 3, certified, WELLDEF holds, invasive, C dims [2, 3, 3, 3] (C_1 = C_2 = C_3; FREEZE:
"stabilized") for every one.

All tables certified; WELLDEF holds except the 15 Level-2 nonlinear interfaces (all with κ_b's image a fixed
v-row per branch), whose verdict does not depend on the guard (§4.3).

### 4.2 Certified ranks (R4-global)

| Level | Rule | Certified table rank over the 143 κ | R4-global |
|---|---|---|---|
| 1 | linear | 1 (all) | UNDER-RANK; rank 1 at every horizon (proved, §6) |
| 1 | nonlinear | 6–13 | OVER-RANK, excluded |
| 1 | majority | 8–14 | OVER-RANK, excluded |
| 2 | linear | 1–3 at horizon 3; 3 at horizon 4 for all 76 invasive κ | UNDER-RANK; unresolved globally |
| 2 | nonlinear | 7–15 | OVER-RANK, excluded |
| 2 | majority | 11–20 | OVER-RANK, excluded |

### 4.3 R4(r; G) by level

- **Majority:** OVER-RANK for every κ at both levels (certified dim C_2 ≥ 5).
- **Nonlinear, Level 2:** OVER-RANK for every κ: certified dim C_2 ≥ 5, including the 15 that fail the
  well-definedness guard (diag_welldef.py, guard skipped only for the dimension count: dims [2,4,5] ×7,
  [2,4,7] ×8).
- **Nonlinear, Level 1:** 136 κ OVER-RANK at Stage A. Seven κ had C_1 = 3 and certified dim C_2 = 4 (AT-RANK at
  Stage A); the frozen rule fails them for not stabilizing.

> **Post-freeze diagnostic (does not alter the preregistered Stage-A label or advance rule).** The seven run at
> the Stage-B horizon (L_p = L_e = 4; diag_nl7.py, diag_nl7b.py). The depth-4 guard fails for all seven, which
> does not affect dimension lower bounds. Certified dims: six κ [2, 3, 5, 9] (ranks 13–18), and
> ((1,0),(3,2)) [2, 3, 4, 6] (rank 17). Every one has certified dim C_3 ≥ 6: OVER-RANK, R4(r; G_1) excluded.
> For six of the seven, the richer preparation set lifts certified dim C_2 from 4 to 5 — a direct instance of
> monotonicity (i): AT-RANK at a shallow horizon was a restriction artifact.

- **Linear:** Level 1 {unit} only (UNDER-RANK, proved). Level 2: 76 κ with C remaining at certified dimension 3
  through the Stage-A horizon (C_1 = C_2; FREEZE: "stabilized") (UNDER-RANK, non-terminal). Stage B: all 76
  remain at certified dimension 3 through horizon 4 (C dims [2, 3, 3, 3], table rank 3, WELLDEF holds); still
  UNDER-RANK and non-terminal by the rule below.
  Reading rule for Stage B, fixed before its output: a linear κ that remains at certified dimension ≤ 3, or remains
  at 4 through the tested horizons, is finite-horizon evidence (UNDER-RANK / AT-RANK) until a structural upper bound
  or stabilization theorem exists; only such a theorem gives R4-CLOSED. A single certified value > 4 makes that κ
  OVER-RANK at once by the lemma.
  Terminology: FREEZE's "stabilized" (and its C4 verdict) is the finite criterion C_k = C_{k−1} at the largest k
  reached; it is reported under that name as the frozen verdict. In the layered reading, "stabilizes" is reserved
  for a structural result; repeated finite-horizon equality is written "remains at d through the tested horizons".

## 5. Question 3 — discrimination

Per rule, Q3 passes iff some admissible κ passes Q2. No κ passes Q2 for any rule at either level. Nonlinear and majority cannot pass at
either level (OVER-RANK everywhere); linear has no C4 pass (Level 1 {unit}; Level 2 dimension 3 at Stages A and B).
**Preregistered terminal label: ALL FAIL.** Per FREEZE this is evidence that IC is too weak for the target; the
layered reading below says in which direction for each rule. The label is a statement about the preregistered Q2 criterion, not a
claim that the three rules fail in the same mathematical way: nonlinear and majority fail by excess dimension
(OVER-RANK, terminal, exact lower bounds); linear fails by insufficient observed dimension under the finite
criterion (UNDER-RANK through horizon 4, non-terminal). FREEZE maps both to FAIL.

Scope of the controls: the nonlinear and majority leap rules violate the corpus posit (A5), linearity of the
substratum update (Substratum.md:100); the linear rule is the A5-type representative. Their OVER-RANK behaviour
establishes that these particular A5-violating dynamics, under these observer interfaces, do not yield R4(r; G)
compression; it does not establish that a nonlinear substrate cannot yield QM.

Layered reading: G — all three rules, with the Level-1 interface inadequate for linear; R4-global and R4(r; G) —
nonlinear and majority excluded with proof (too large, terminal), linear open (too small at every tested horizon,
non-terminal). The two obstructions are of different kinds and different evidential strength.

## 6. Written result: linear rule, Level 1

linear_L1_proof.md (c0e3cd12…). For every κ ∈ IC and every Level-1 protocol, the record bits are i.i.d. fair.
Each reading at time t is v^t_0 = v^0_t + v^0_{−t} + h_t(initial data within radius t − 1): the cone-edge
variables enter with coefficient 1 (permutive rule) and are independent of everything earlier readings and
disturbances depend on. Hence rank 1, C = {unit}, and m indistinguishable from i on every Level-1 effect, although
f_κ ≠ id. The swap of Level 2 breaks the premise (it exposes u_0, an older value), which is why Level 2 is the
first level at which the linear rule can show disturbance.

## 7. Descriptive observation (not adopted as interpretation)

At the Level-2 Stage-A horizon, for each of the 76 invasive linear κ, the exact normalized preparation columns in
the coordinates (unit, P(read v_0 = 0), P(swap then read = 0)) lie in the unit square with hull vertices among the
edge midpoints (0, ½), (1, ½), (½, 0), (½, 1): all four for 36 κ, three for 40 (hull_all.py). At every vertex one
pair bit is determined and the other is a fair coin. This is a finite-horizon description; the exact state/effect
geometry is not certified, and no interpretation is adopted.

## 8. Held

PROPOSAL-LEVEL3.md (13779777…) records a possible further reversible pair action, written before any
computation, and is held. It is to be reformulated in field-neutral operational terms (a controlled reversible
coupling/permutation) and designed from the premise ledger, not run under its current name.

## 9. Artifacts (scratchpad/record)

FREEZE.md b66b1a69 · ADDENDUM-LAYERS.md 662428cf · record_sim.py e499a081 · record_fast.py c2c94a68 ·
record_analysis.py a9ac39fc · record_analysis2.py 4c152b5d · layers.py 7bf0c3fa · validate.py 4560d299 ·
validate_brute.py e86c788e · validate_fast.py c76920c2 · diag_welldef.py fa1181fe · diag_nl7.py 3f90a6b7 ·
diag_nl7b.py 3199d05f · hull_linear.py 094d5233 · hull_all.py f851ffd2 · linear_L1_proof.md c0e3cd12 ·
PROPOSAL-LEVEL3.md 13779777 · fast_stageA_L1.json 36ff602a · fast_stageA_L2.json 580d4721 ·
fast_stageB_L1.json 4f53cda1 (empty) · fast_stageB_L2.json 339f68b5 · layers_L1.json fcf1df29 · stageA_L1.json 36ff602a (original-simulator replay, byte-identical) · layers_L2.json fcf1df29 (= layers_L1.json, see §3) · cc_census_L2.py fd6ca73b · cc_census_L2.log 060a8638 · replay_L2_sample.py · replay_L2_ninth.py · replay_stageB_gate4.py.
