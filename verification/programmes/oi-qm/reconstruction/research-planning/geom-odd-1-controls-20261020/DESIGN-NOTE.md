# GEOM-ODD-1: the failed control searches, diagnosed, and a corrected control design

Design note for PR #830 (draft, not an F candidate), under the owner's instruction of 2026-10-20 (comment
6280945546): "Investigate failed control searches; design only." Nothing here is committed, pushed, dispatched or
adopted. The park rule of comment 6254707076 continues to hold. Every computation below was run locally in
`scratchpad/a830/`; outputs are in `work/`, scripts in `scripts/`. The first pass ran on a shared 4-core host at load
9–10; timings from it are marked as contended, and the timings used for diagnosis were re-taken on a quiet host
(load 0.5 at start). This revision incorporates the independent review in `scratchpad/rev830/REVIEW.md`
(verdict: confirmed with corrections); the changes are listed in `CORRECTIONS.md`.

## 0. Objects

| object | id |
| --- | --- |
| PR head (`draft/geom-odd-1`), the original preregistration | `f8e7508671397f33797adc561e457d2cbf5f5671` |
| drafting snapshot `D` | `dee3b5ae6fd3fb20fa1bad3337963e5af947f3a4` |
| revised preregistration (`staging/geom-odd-830-20261018`) | `8a4587c96d9ce8547ebc34d05949a4aeb1e27164` |
| preflight code (`staging/geom-odd-830-controls-20261018`) | `e8ac54b598906960961264e5c2c7fe843904e20b` |
| dispatch wrapper (`tmp/geom-odd-830-dispatch-cf9ddc11`) | `cf9ddc117420126682a5dc48687343bc5aea4ffd` |
| preflight run | `39192591924` (jobs `117868433544` eball3, `117868433431` omegah, `117872644074` aggregate) |
| `controls_verify.py` / `controls_gen.py` / `run_control.py` sha256 | `e6f3fcbc…0763` / `df7e640c…b855` / `3faa0fdf…06b9` (match the pins in `8a4587c9`) |
| E20 harness (research/equivalence `424aa33b`), `e20_odd_bodies.run2.py` | sha256 `ec95a697…93c3`, blob `34485203` |
| `CompositeDimension.lean` | blob `377f0b25` at both `D` and `e8ac54b5` |

Environment: Python 3.13.16 (CI used 3.11.17), numpy 2.4.6, scipy 1.17.1 (the preflight's pins).

## 1. The failed controls

Three control searches in the thread failed. None returned evidence about any body.

### F1. E20 positive control `eball 3` (runs 1 and 2, research branch; inherited by the draft)

- **Meant to establish:** that the `posFwd`-only cutting-plane LP reaches `FEASIBLE(pool)` on a body known to carry a
  gate (`cnot`), so that its verdicts on `eball 5` and Ω⋆⁵ are readable.
- **Returned:** `FAIL C4 -- eball 3: UNDECIDED(iterations) (18639 constraints)`; `VERDICT NOT RENDERED -- failing: ['C4']`.
- **Reproduced:** yes. `e20_odd_bodies.run2.py` re-run in an isolated tree (`python -I -B`, 4 min 44 s, contended host)
  gives stdout identical to the recorded `e20_odd_bodies.run2.out`: `work/e20-run2-replay.out`.
- **Root cause (construction):** an iteration cap on a slowly converging cutting plane (40 rounds, about 600 cuts a
  round, in a 48-dimensional `F`), as LOG.md (2026-10-11T10:39Z) records; S0-b's tolerance diagnosis was withdrawn
  there. Independently of the cap, the control could not have made E20's exclusion outcome meaningful: the relaxation
  imposes `posFwd` alone, and `gSq_sep` (RelcSelectSqueeze.lean:465) is an exact `eball 5` map meeting the frame, the
  relations and `posFwd`. This is already recorded in the draft (Consequence (2)).

### F2. Preflight control `eball3` (run 39192591924)

- **Meant to establish:** that the generator, told only `(z, N)` and pool A, returns within 1200 s a rational `G` that
  the exact verifier accepts (VS, VE, VL, VI, VP on pools A and B).
- **Returned:** 36 starts, best residual `max|GH − 1| = 0.006731`, `status: deadline`, no candidate;
  `result-eball3.json` sha256 `0dad77f6…9cca`. The verifier was never run on a candidate.
- **Reproduced:** yes. Start 0 replayed locally (`scripts/a2_alternation.py replay 0 40`) reaches residual
  `2.060·10⁻²` with 8867 cuts at round 26, the CI log's start-0 line (`0.020604…`, 8867 cuts, 26 rounds). The review
  ran the frozen `controls_gen.py` unmodified and matched starts 0–3 of the CI log exactly. The exact verifier
  self-test passes locally (55 s; §2.1).
- **What the target is.** Among the 4096 sign twists `R∘diag(s)` in `F` the verifier accepts exactly 32, one local-relabelling class; whether other points of `F` pass is not determined:
  1. The reference `R` (kernel `cnot`) lies in `F` with coordinates in `{−1, 0, 1}` (box 8), `R² = 1`, and is exactly
     `posFwd`/`posInv`-feasible on pool A (`work/a1.out`).
  2. Let `Γ = {diag(1, a, b, c) : a, b, c = ±1}` act on homogeneous coordinates of `eball 3`. Each element is an
     orthogonal automorphism of the ball, keeps the `z3` line and commutes with `nflip`. Exactly 32 distinct maps
     `(A ⊗ B) R (C ⊗ D)`, `A, B, C, D ∈ Γ`, lie in `F`; all 32 have the form `R ∘ diag(s)` with `s` a sign vector, and 8
     of them are involutions, `R` among them. Of the 4096 sign twists `R ∘ diag(s)` lying in `F`, exactly these 32 pass
     `posFwd` and `posInv` exactly on pools A ∪ B; the other 4064 fail (exact integer evaluation on positive
     rescalings, largest scaled entry 17) (`scripts/a14_orbit.py`, `work/a14-orbit.out`; the review's `x2_equiv.py`
     reports the same counts). Whole-body positivity of every member follows exactly from `R`'s (`nativeGate_cnot`,
     CompositeDimension.lean:1160), since `(e ⊗ f)((A ⊗ B) R (C ⊗ D)(x ⊗ y)) = (Aᵀe ⊗ Bᵀf)(R(Cx ⊗ Dy))` and the local
     factors map states to states and effects to effects; likewise for the inverse.
  3. `R` is a vertex of the generator's `posFwd` polytope `P_A`: its 200 tight pool-A quadruples have rank 48 = dim F,
     exact (Fraction rows, rank 48 modulo `2³¹ − 1` and modulo `10⁹ + 7`; `rank_p ≤ rank_ℚ`) (`work/a4-eball3.out`,
     `work/a8-eball3.out`).
  4. Each of the 32 members is an isolated point of the generator's own coupled relaxation
     `K_A = {G ∈ F : G and G⁻¹ positive on pool A}`. For a member `M` with `H = M⁻¹`, every first-order direction `δ`
     must satisfy `⟨q, δ⟩ ≥ 0` on the `G`-tight quadruples and `⟨q, −M⁻¹δM⁻¹⟩ ≥ 0` on the `H`-tight ones. For every
     member these exact rows have rank 48 modulo `2³¹ − 1`, and an exact Stiemke certificate exists: a rational `y`
     with every `yᵢ > 0` and `Σ yᵢ rowᵢ = 0`, checked in Fraction arithmetic. Tight counts range over 122–217 per side
     (`work/a15-orbit-isolation.out`, a filtered log: the `##`/`==` lines and the exact-tightness, rank, Stiemke and `LP status` lines of the run). For `R` (400 rows), under the normalisation `max yᵢ ≤ 1` of the LP that found
     it, `min yᵢ = 0.1774` (`work/a3-eball3-A-stiemke.out`); the review's certificate, normalised to `Σ yᵢ = 400`, has
     `min yᵢ = 0.4747`. Over the 32 members the minimum entry, normalised by `max yᵢ ≤ 1`, lies in 0.096–0.383.
     Because the `G`-side values are linear in `δ` and the `H`-side ones are linear up to `O(|δ|²)`, Stiemke with full
     rank gives some tight value at most `−κt + Ct² < 0` for small `t > 0`, so each member is isolated in `K_A`, and
     therefore in the A ∪ B version (written argument; not a kernel proof). The review's countercontrol: the `G`-side
     rows alone, or the `H`-side rows alone, admit no positive certificate, so isolation needs the coupling.
- **Root cause (construction): the alternating L1 coupling did not converge to any member of the class in any start
  tried.**
  1. CI: 36 starts, none below residual `6.7·10⁻³`.
  2. Local basin, `G = R` fixed and `H = R⁻¹ + ε ξ`, `ε ∈ {10⁻³, 3·10⁻², 0.3}`: 9 of 9 trials stall at residuals
     `5.1·10⁻⁴ … 1.8·10⁻²`, of the order of `ε` (`work/a2-basin.out`). Start 0's stalled point has
     `σ(G) ∈ [0.985, 1.006]`, `G` pool-feasible, and `G⁻¹` violating pool A by `−5.1·10⁻³`: a fixed point of the
     alternation that is not a gate.
  3. Random-objective vertices of the full `P_A` (box 8, the generator's seeds) are at distance 1.32–2.2 from `R`
     (0 of 20 equal `R`), matching comment 6255285218's scratch measurement (`work/a4-eball3.out`). Distance to the
     other 31 members was not measured.

  Isolation is a property of the target and the stall a property of the alternation; no causal link between them is
  shown, and the joint SLP of §2.2 converges to the same isolated points. The failure says nothing about generator
  power on any search body, in either direction.

### F3. Preflight control `omegah` (run 39192591924)

- **Meant to establish:** the same, on E16b's Ω_h (`D = 7`, `dim F = 960`).
- **Returned:** 1 start, 0 rounds, residual `inf`, 13 500 cuts, `status: deadline`; `result-omegah.json` sha256
  `d19a54da…666e`.
- **Reproduced:** the stall, by a bounded replay of the frozen generator's first vertex step
  (`scripts/a6_omegah_vertex.py`). `a6` prints each round's row count after that round's separation, so the LP of
  round `k` was solved on `3000 + 1500k` rows.

  | round | rows solved on | LP time, quiet host (`work/a6-omegah-quiet.out`) | LP time, review (`rev830/omegah/run.out`) | violated after |
  | --- | --- | --- | --- | --- |
  | 0 | 3000 | 44.0 s | 44.1 s | 43 305 |
  | 1 | 4500 | 69.2 s | 68.2 s | 16 770 |
  | 2 | 6000 | 122.6 s | 101.6 s | 16 472 |
  | 3 | 7500 | not finished within budget | not finished within budget | — |

  On the quiet host the initial 3000 rows took 0.5 s to build and each separation 0.2–8.2 s. The first pass's 74 s for
  3000 rows and 72 s / 135 s per LP were measured under contention and are not used. In CI, 13 500 cuts are
  `3000 + 7 × 1500`: at least seven separation calls (exactly seven if each added the full 1500), with `G` and `H`
  sharing one cut set, so the log does not say which vertex step was in progress at the deadline.
- **Root cause (construction): LP cost.** The LPs dominate and grow with the row count (44 → 69 → 102–123 s on a quiet
  host); violated rows fell from 43 305 to 16 770 after one round and then plateaued (16 472). No round-count bound
  follows from these numbers: one round of 1500 added rows removed 26 535 violations, and the next removed 298. This
  is a different failure from F2.
- **Structure of the Ω_h target, measured:** the 57 456 `G`-tight pool-A quadruples at `R` have rank 768 modulo
  `2³¹ − 1`, so rank over ℚ is at least 768 and the face of `P_A` containing `R` has dimension at most 192 (exact).
  The float rank is also 768, and adding the `H`-side rows leaves the float rank at 768 (`work/a8-omegah.out`,
  `work/a9-omegah.out`); with pools A ∪ B the float ranks are 776 (`G`) and 784 (`G + H`) (`work/a9-omegah-AB.out`).
  So, as a float measurement, `R` is first-order flat in about 176–192 directions of the coupled relaxation. That does
  not show `R` is non-isolated in `K_A`: second-order terms of `G⁻¹` can cut every such direction. Whether there is a
  curve of pool-relative gates through `R`, and whether any such curve consists of genuine gates or of pool-blind
  points, is not determined here.

### A precision note on comment 6255285218

"`cnot` composed with a control-side Z-rotation passes every clause" holds for the rotation by π only (and the
identity). Argument: `R ∘ (R_θ ⊗ 1)` meets `relT`, since `R_θ ⊗ 1` commutes with `T = 1 ⊗ H`; it meets `relC`,
`C G C = T G`, iff `C (R_θ ⊗ 1) C = R_θ ⊗ 1`, given `C R C = T R` and `R` invertible, that is iff `R_θ` commutes with
`H = 1 ⊕ nflip = diag(1, 1, −1, −1)`. `R_θ` rotates the plane of the second and third homogeneous coordinates, whose
`H`-eigenvalues are `+1` and `−1`, so this holds iff `sin θ = 0`. Exact witnesses agree: `R ∘ (Zπ ⊗ 1)` and
`(Zπ ⊗ 1) ∘ R` pass on pools A ∪ B, and `relC` fails at `cos θ = 3/5`, `sin θ = 4/5` (`work/a5.out`).

## 2. Repairs, measured where cheap

### 2.1 The exact verifier

Unchanged. Its self-test passes on both bodies (`python3 -I -B controls_verify.py --self-test`: reference PASS,
identity fails the frame, `ref ∘ (1 ⊗ K₂)` fails `posFwd` only, `ref ∘ (1 ⊗ K_{1/2})` fails `posInv` only, invalid
effect fails VE, outside state fails VS, bad shape fails; `self-test: OK`).

### 2.2 Generator coupling: joint sequential linear programming (SLP)

Each step solves one LP in `(λ_G, λ_H)`: minimise `‖G_k H_k − 1 + ΔG H_k + G_k ΔH‖₁` subject to pool-A positivity of
both `G` and `H` (constraint generation) and a trust region, accepting a step only if `max|GH − 1|` decreases
(`scripts/a10_slp.py`). Float; any output goes to the exact verifier. SLP was chosen after the `eball3` control had been
observed, so a later `eball3` PASS is not held-out evidence for it (§3.1(b)).

- Basin, both `G` and `H` perturbed (`ε ∈ {10⁻³, 3·10⁻², 0.3}`, 3 trials each): 9 of 9 return to `R`
  (residual ≤ `5.3·10⁻¹³`, `|G − R| ≤ 1.3·10⁻¹²`) in 2–4 steps (`work/a10-basin-both.out`). The alternation's basin
  runs (F2) perturbed `H` alone, so the two basin results are not like-for-like. A first SLP basin test that perturbed
  `H` alone was discarded: with `G = R` fixed it is solved by one LP.
- Random starts (the generator's own vertex starts, seeds 1000–1004, 120 s each): start 3 reaches residual
  `1.3·10⁻¹²`; the other four stall at `0.88–1.0` with the trust radius collapsing (`work/a10-random.full`). Start 3's
  point, exactified by the frozen `exactify`, is
  `G = (1 ⊗ diag(1, 1, −1)) · R · (Zπ ⊗ (−1₃))` exactly (`work/a14-orbit.out`; review `out/x2.out`): a member of
  `R`'s 32-point class, not an involution. The frozen exact verifier prints PASS on pools A and B
  (`work/slp-verify-eball3-s3.json`, sha256 `80a367f8…ba1f`; candidate sha256 `5dc9fa9b…b393`); the review reproduced
  both files byte for byte.

Reading: the SLP coupling recovered `cnot` up to a local relabelling in one of five random starts, and returns to `R`
from the perturbations tried. It is still a local method and stalls from most starts; one hit in five is too small a
sample to set a cap, and the hit rate is a rate against at least that 32-point class.

### 2.3 Other repairs (described, not run)

Ranked by expected effect on the two failures.

1. **LP cost at `D = 7` (F3).** Warm-start the LP between separation rounds (the frozen code rebuilds and re-solves
   from scratch each round), try the dual simplex or interior-point method of HiGHS with a time measurement on Ω_h on a
   quiet host, and test whether adding every violated row (or solving the full 147 456-row pool LP) costs less in total
   than incremental rounds. Row construction was 0.5 s for 3000 rows on a quiet host and is not a bottleneck at these
   sizes.
2. **SLP coupling (F2)**, §2.2, with a frozen multistart count and trust-region rule; the reference table read by
   `a10_slp.py` (`lam-eball3.json`, used for start points in basin mode and for printed distances) must not be read by
   a frozen generator (P1, §3.2).
3. **Active-set exactification.** At an isolated point of `K_A` there is no slack, so a rounded float point passes
   exact VP only if it is that point. Identify the near-tight rows, solve exactly (Fraction) on a full-rank subset, then
   verify; `limit_denominator` (bounds up to `2²⁰`) remains the fallback.
4. **Involutive ansatz `G² = 1`** as an optional restricted cell: `posInv` coincides with `posFwd`. Both references are
   involutive (exact), and `R`'s class contains 8 involutions, so on the `eball3` control the ansatz keeps the class
   while excluding 24 of its 32 representatives, among them the SLP hit. Its outcomes speak only of involutive gates.
5. **Symmetry ansatz**, only with a frozen subgroup containing the controls' gates: the `eball3` reference commutes
   with `g ⊗ g` for `g = diag(1, −1, 1)`, with `Zπ ⊗ 1`, and with no other element of the sign stabiliser of
   `(z3, nflip)` acting on one factor or both (`work/a7.out`); the review found the same commutation counts for all 32
   class members (`rev830/out/x4.out`). An ansatz under the full stabiliser on both factors excludes the whole class.

**Exact constructive recovery versus optimisation.** Exact recovery of the controls succeeds trivially and certifies
the verifier (the reference passes; so does every member of its class). It does not calibrate the generator: a linear
objective built from `R`'s tight rows returns `R` to `10⁻¹³` (`work/a4-eball3.out`), which is the vacuity hazard (the
control would reproduce what it is meant to find). Optimisation from inputs that exclude the gate is the only reading
that tests the generator. The two controls test it in different regimes: isolated points of `K_A` (`eball3`, exact)
and a point first-order flat in up to 192 directions (Ω_h; flatness a float measurement, non-isolation not shown).

## 3. Corrected control design (proposal)

### 3.1 What the preflight must show

(a) The exact verifier distinguishes gates from the kernel's linear-layer non-gates (unchanged self-test).
(b) The frozen generator, receiving `(z, N)` and the generation pool only, returns within the frozen cap a candidate
the verifier accepts on each control body. Since SLP was selected after observing `eball3`, a held-out control carries
the calibration credit: `eball3` in the family's own parametrisation `Ω_R(1, 1; 2)`, with the family's pool rules and
seeds not used in design, so the search code path is exercised. Ω_h covers the `D = 7` size; an Ω_h PASS may land on a
pool-blind point of its first-order-flat face, which bears on open question 7.
(c) The acceptance is attributable to the repair: the frozen alternating generator (`e8ac54b5`) under the same cap
fails where the repaired one passes. Run `39192591924` already is this run at cap 1200.
(d) Before any `D = 7` cell reads `HIT`, the same generator, pools and cap on `eball 7` with the family's pair
(`ne_seven_of_nativeGate`, CompositeDimension.lean:2741, kernel exclusion; frame consistent, `dim F = 960`,
`work/x3-rerun.out`) return no accepted candidate, and the run reaches the same stage as the Ω_h control
(pool-feasible vertices for `G` and `H` and a recorded residual trajectory). Scope: an accepted `eball 7` candidate is
decisive and voids `HIT`; no candidate does not establish pool adequacy, since the generator is not exhaustive.

### 3.2 Decision rule (preregistered rule; no expected numbers)

| item | rule |
| --- | --- |
| P0 | `controls_verify.py --self-test` prints `self-test: OK` for both bodies; otherwise every preflight verdict is void |
| P1 | static independence check: the generator imports nothing from the verifier, reads no file but its pool, and contains no reference table; otherwise void |
| P2(c), c ∈ {held-out `eball3` (`Ω_R(1, 1; 2)`), `omegah`} | `PASS(c)` iff the verifier prints `PASS` on the generator's candidate within the cap; `FAIL(c)` otherwise (timeout, no candidate, exactification failure or verifier FAIL), with the reason recorded |
| P3 | the frozen alternating generator, same pools and cap, run on the same control: recorded as `XP1 fails as stated` or `XP1 does not fail`; it voids nothing, and if it does not fail, no reading credits the repair |
| park | as decided (6254707076): `FAIL` on either control parks the round |
| P4 (`D = 7` design, if written) | each `HIT-B` requires P2 PASS on both controls and the `eball 7` run of 3.1(d), at the same pool size and cap, reaching the Ω_h control's stage with no accepted candidate; an accepted `eball 7` candidate voids every `HIT` at that pool size; an `eball 7` run that stalls before that stage leaves `HIT` unread |

### 3.3 Countercontrols

| credited element | countercontrol (the reading fails without it) |
| --- | --- |
| verifier `posInv` | `ref ∘ (1 ⊗ K_{1/2})` passes VL and `posFwd`, fails `posInv`; `gSq` on `eball 5` |
| verifier `posFwd` | `ref ∘ (1 ⊗ K₂)`; `gRev 3` |
| verifier frame | the identity |
| generator repair | XP1: the frozen alternation fails on the control (F2 reproduced) |
| generator independence | XC-VAC: an objective built from `R`'s tight rows is excluded by P1; it is shown to return `R` (the hazard is real) |
| pool discrimination for `HIT` | 3.1(d) on `eball 7` |
| novelty of any hit | the local-relabelling test of §4 N1.2 before a hit is read as distinct from a known gate |

### 3.4 Invariants and their checkpoints (§A.41)

| invariant | checkpoint |
| --- | --- |
| the verifier and generator run are the frozen blobs | sha256 of each file against its pin, at the dispatched commit |
| the verifier separates gates from linear-layer non-gates | P0 output lines |
| the generator never sees a gate | P1: import scan, file-access list, absence of the reference's table in the generator source and inputs |
| an accepted candidate is exactly verified, not floated | verifier report `verdict: PASS` with `VP.posFwd_negative = posInv_negative = 0`, pools A and B |
| the cap is honoured | `run_control.py` monotonic elapsed time `≤ cap` in the result; job `timeout-minutes` |
| the repair is what passed | P3 recorded at the same commit and cap |
| `HIT` is not a pool artifact detectable by the generator | P4's `eball 7` result at the same pool size |
| the `eball 7` run is comparable to the Ω_h control | P4 stage record: pool-feasible `G` and `H` vertices reached, residual trajectory logged, for both runs |
| a hit is not a relabelled known gate | the local-relabelling test (§4 N1.2) output recorded beside the hit |
| determinism | replay of one start: residual and cut count equal to the logged values (as done in §F2) |
| no search body runs before `F` | the dispatched matrix names control bodies only (`C0`) |

### 3.5 Resource estimate for `D = 7`

Measured (quiet host): Ω_h (`dim F = 960`, 147 456 pool-A quadruples): LP times 44.0, 69.2 and 122.6 s on 3000, 4500
and 6000 rows (review: 44.1, 68.2, 101.6 s); 43 305 → 16 770 → 16 472 violated rows; no pool-feasible vertex within
300 s. CI: at least seven separation rounds in about 945 s with no completed start. `eball3` (`dim F = 48`):
alternation starts 11–65 s each in CI; SLP starts up to 120 s locally (contended). Derived: search bodies at `D = 7`
with the frozen pair have the same `H` signature (four `+1`, four `−1`), so the same free pattern of 1024 entries;
`eball 7` with the family's pair has `dim F = 960` (`work/x3-rerun.out`), and the frame rank of each search body is to
be measured, not assumed. No estimate of the time to a pool-feasible vertex at `D = 7` is supported, under the frozen
cut loop or a repaired one, until repair 1 of §2.3 is timed on Ω_h.

### 3.6 Is the search target still meaningful?

`Q-BODY` remains meaningful as a search for exactly verified, pool-relative candidates for later kernel work, under
five conditions: green P0–P2 with a repaired generator and a held-out `eball3` control; P4 at the same pool size; the
local-relabelling test on any hit; the cell restated as relative to its `(z, N)` and pools; and the non-inference rule
extended by §4 N4 (an irrational gate isolated in `K_A` yields no `HIT` near it). `UNDECIDED-B` carries no information
about `B`, as the draft states. No negative result is stated for any body: every failure in §1 is a failure of a method
on a control.

## 4. Gem-finding pass (§A.31)

Productivity test, fixed before the walk: a node is a gem if it yields a fact stronger than "the generator failed"
and either constrains the design or exposes an assumption the draft makes.

| node | assumption under test | check | verdict |
| --- | --- | --- | --- |
| N1 | recovering a known gate by local optimisation measures generator sensitivity | exact vertex rank, exact Stiemke certificates for all 32 class members, basin runs (§F2) | NEW: the `eball3` target includes a set of 32 points (all the accepted sign twists) isolated in the generator's own relaxation, one local-relabelling class, other accepted points of `F` not excluded; the alternation did not converge to any of them in any start tried; F2 is the method's failure |
| N1.1 | favourable branch: the SLP repair works | `H`-only basin discarded as trivial; both-perturbed basin 9/9; random starts 1/5; exact verifier PASS on the hit | POSITIVE, local: recovery up to local relabelling is possible; robustness is not shown |
| N1.2 | favourable branch, missed in the first pass: the SLP hit is a gate distinct from `cnot` | exact decomposition `G = (1 ⊗ diag(1,1,−1)) R (Zπ ⊗ (−1₃))`; class of 32; no other sign twist passes | NEW (assumption-watch marker): before any control or search hit is read as new, test it for equivalence to a known gate under the body's local automorphisms; the first pass should have run this test on N1.1's branch, and did not |
| N2 | the Ω_h failure is the same phenomenon | quiet-host replay; rank ≥ 768 exact, 768 float | NEW: a different cause (LP cost); `R` first-order flat in up to 192 directions (float), non-isolation not shown |
| N3 | a search-body `HIT` would sit in a regime the controls calibrate | N1 and N2 place the controls in different regimes; a strictly convex body's regime is unknown | ELABORATING: controls calibrate only the regimes they occupy; both are needed |
| N4 | gates are rational in `F`'s coordinates | controls have coordinates in `{−1, 0, 1}`; at a gate isolated in `K_A` there is no slack, so no rounded point near an irrational one passes exact VP; `exactify` caps denominators at `2²⁰` | NEW (assumption-watch): a returned candidate is always rational, and an irrational gate isolated in `K_A` yields no `HIT` near it; on a positive-dimensional face rational gates may lie near an irrational one; stated scope, not a finding about any body |
| N5 | a symmetry ansatz is neutral | equivariance of the class under the sign stabiliser (§2.3 item 5) | CONFIRMING: the ansatz group must be frozen with the controls' gates in it |
| N6 | `UNDECIDED-B` over green controls is informative | the generator is local and non-exhaustive | CONFIRMING the draft's non-inference rule |
| N7 | "no generator candidate on `eball 7` passes VP" is a countercontrol | vacuous while the generator fails C-POS; non-exhaustive even when it passes | NEW (design): restated as 3.1(d) with explicit scope, a stage checkpoint, and gated on green controls |
| N8 | E20's control failure was a tolerance stall | reproduced run 2; LOG's correction | CONFIRMING LOG.md: iteration-capped cutting plane; `posFwd`-only target known not to exclude |

Two passes have now been made (the first pass and the review's), and the second produced a NEW finding (N1.2), so
the fixed-point condition (three to four passes without a NEW finding) is not met and the list is not claimed complete.

## 5. Open questions for the owner

1. Adopt joint SLP as the generator's coupling, with which multistart count, trust-region rule and cap; and whether
   repair 1 (LP cost at `D = 7`) must be timed on Ω_h on a quiet host before any re-dispatch.
2. Make the held-out `Ω_R(1, 1; 2)` control (family parametrisation, family pool rules, seeds unused in design) the
   `eball3` control of P2, given that SLP was selected after observing `eball3` with the Pythagorean pool.
3. Is P3 (the frozen alternation must fail) required, or recorded only.
4. Gate every `HIT` on P4 (`eball 7`, same pools and cap, same stage reached), voiding `HIT` tokens at a pool size where
   `eball 7` yields an accepted candidate.
5. Whether the involutive ansatz is a separate restricted cell; on the `eball3` control it keeps `R`'s class (8 of 32
   representatives are involutions), and what it would lose on a search body is unknown.
6. Carried over: how parking evidence reaches `main` (§A.42; comment 6255285218, item 2), and whether `Entangling`
   is read by `HIT`.
7. Whether Ω_h's first-order-flat directions (about 176 at pools A ∪ B, float) should be resolved before Ω_h serves as a
   control: exact nullspace (modular nullspace, rational reconstruction, integer check on all tight rows), then a curve
   in `K_A` or the statement "first-order flat"; and whether such a curve consists of genuine gates or pool-blind
   points. An Ω_h P2 PASS on such a point would calibrate the generator only relative to its pools.

## 6. Commands

```sh
S=<work-dir>
git -C <clone> archive e8ac54b5 verification/programmes/oi-qm/reconstruction/round-geom-odd-1 \
  verification/lean-mathlib/OIBridge/CompositeDimension.lean | tar -x -C $S/src
P=$S/src/verification/programmes/oi-qm/reconstruction/round-geom-odd-1/preflight
python3 -I -B $P/controls_verify.py --self-test
python3 -I -B $P/controls_verify.py --emit-pool eball3 $S/work/pool-eball3.json      # and omegah
$S/venv/bin/python -I -B $S/scripts/a1_structure.py $P $S/work
$S/venv/bin/python -I -B $S/scripts/a2_alternation.py $P $S/work eball3 replay 0 40   # F2 replay
$S/venv/bin/python -I -B $S/scripts/a2_alternation.py $P $S/work eball3 basin 0.001 3 # and 0.03, 0.3
A3_STIEMKE=1 $S/venv/bin/python -I -B $S/scripts/a3_rigidity.py $P $S/work eball3 A
$S/venv/bin/python -I -B $S/scripts/a4_vertex.py $P $S/work eball3 20
$S/venv/bin/python -I -B $S/scripts/a6_omegah_vertex.py $P $S/work 300              # F3 replay (quiet host)
$S/venv/bin/python -I -B $S/scripts/a8_modrank.py $P $S/work omegah
$S/venv/bin/python -I -B $S/scripts/a9_float_rank.py $P $S/work omegah AB
A10_BOTH=1 $S/venv/bin/python -I -B $S/scripts/a10_slp.py $P $S/work basin 0.3 3
A10_ONLY=3 $S/venv/bin/python -I -B $S/scripts/a10_slp.py $P $S/work random 1 120
python3 -I -B $P/controls_verify.py --verify eball3 $S/work/slp-candidate-eball3-s3.json $S/work/slp-verify-eball3-s3.json
$S/venv/bin/python -I -B $S/scripts/a14_orbit.py $P $S/work/slp-candidate-eball3-s3.json        # class, 4096 twists
python3 -I -B $S/scripts/a15_members.py $P $S/work/orbit
for f in $S/work/orbit/member-*.json; do A3_REF=$f A3_STIEMKE=1 $S/venv/bin/python -I -B $S/scripts/a3_rigidity.py $P $S/work eball3 A; done
$S/venv/bin/python -I -B $S/scripts/x3_eball7F.rev830-copy.py $P                    # eball 7 dim F
(cd $S/e20/research/equivalence/experiments && $S/venv/bin/python -I -B e20_odd_bodies.run2.py)   # F1 replay
```
