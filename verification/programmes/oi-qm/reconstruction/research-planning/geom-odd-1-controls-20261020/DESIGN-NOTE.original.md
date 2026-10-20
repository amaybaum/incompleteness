# GEOM-ODD-1: the failed control searches, diagnosed, and a corrected control design

Design note for PR #830 (draft, not an F candidate), under the owner's instruction of 2026-10-20 (comment
6280945546): "Investigate failed control searches; design only." Nothing here is committed, pushed, dispatched or
adopted. The park rule of comment 6254707076 continues to hold. Every computation below was run locally in
`scratchpad/a830/` (shared 4-core host, load 9–10 during most runs); outputs are in `work/`, scripts in `scripts/`.

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
- **Reproduced:** yes. `e20_odd_bodies.run2.py` re-run in an isolated tree (`python -I -B`, 4 min 44 s) gives stdout
  byte-identical to the recorded `e20_odd_bodies.run2.out` (comment lines excluded): `work/e20-run2-replay.out`.
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
  `2.060·10⁻²` with 8867 cuts at round 26, the CI log's start-0 line (`0.020604…`, 8867 cuts, 26 rounds).
  The exact verifier self-test passes locally (55 s): `work/` and §2.1.
- **Root cause (construction): the alternating L1 coupling cannot converge to the control's gate.** Measured:
  1. The reference `R` (kernel `cnot`) lies in `F` with coordinates in `{−1, 0, 1}` (box 8), `R² = 1`, and is
     exactly `posFwd`/`posInv`-feasible on pool A (`work/a1.out`).
  2. `R` is a vertex of the generator's `posFwd` polytope `P_A`: its 200 tight pool-A quadruples have rank 48 = dim F,
     exact (Fraction rows, rank 48 modulo `2³¹ − 1` and modulo `10⁹ + 7`; `rank_p ≤ rank_ℚ`) (`work/a4-eball3.out`,
     `work/a8-eball3.out`).
  3. `R` is an isolated point of the generator's own coupled relaxation
     `K = {G ∈ F : G and G⁻¹ positive on pool A}`. With `H = R⁻¹`, every first-order direction `δ` must satisfy
     `⟨q, δ⟩ ≥ 0` on the 200 `G`-tight quadruples and `⟨q, −R⁻¹δR⁻¹⟩ ≥ 0` on the 200 `H`-tight ones. These 400 exact
     rows have rank 48, and an exact Stiemke certificate exists: a rational `y` with every `yᵢ > 0`
     (minimum `0.1774`) and `Σ yᵢ rowᵢ = 0`, checked in Fraction arithmetic (`work/a3-eball3-A-stiemke.out`). Hence no
     nonzero `δ` keeps all tight values nonnegative; because the `G`-side values are linear in `δ` and the `H`-side ones
     are linear up to `O(|δ|²)`, `R` is isolated in `K` (written argument; not a kernel proof).
  4. The alternation does not return to `R` even from nearby starts: with `G = R` and `H = R⁻¹ + ε ξ`,
     `ε ∈ {10⁻³, 3·10⁻², 0.3}`, 9 of 9 trials stall at residuals `5.1·10⁻⁴ … 1.8·10⁻²`, of the order of `ε`
     (`work/a2-basin.out`). Start 0's stalled point has `σ(G) ∈ [0.985, 1.006]`, `G` pool-feasible, and `G⁻¹` violating
     pool A by `−5.1·10⁻³`: a fixed point of block-coordinate descent on a nonsmooth coupled problem, not a gate.
  5. Random-objective vertices of the full `P_A` (box 8, the generator's seeds) are at distance 1.32–2.2 from `R`
     (0 of 20 equal `R`), matching comment 6255285218's scratch measurement (`work/a4-eball3.out`).

  So the control failed for a reason internal to the method: its target is an isolated point that the method cannot
  converge to. This says nothing about generator power on any search body, in either direction.

### F3. Preflight control `omegah` (run 39192591924)

- **Meant to establish:** the same, on E16b's Ω_h (`D = 7`, `dim F = 960`).
- **Returned:** 1 start, 0 rounds, residual `inf`, 13 500 cuts, `status: deadline`; `result-omegah.json` sha256
  `d19a54da…666e`.
- **Reproduced:** yes, the stall mechanism (bounded local replay, `scripts/a6_omegah_vertex.py`, 420 s budget):
  building the initial 3000 cut rows takes 74 s (`Problem.rows` loops over quadruples in Python); LP 0 takes 72 s
  on 4500 rows and leaves 43 305 of 147 456 pool quadruples violated; LP 1 takes 135 s on 6000 rows and leaves 16 770;
  LP 2 does not finish within the budget (`work/a6-omegah.out`). CI's 13 500 cuts are `3000 + 7 × 1500`: seven
  separation rounds, no pool-feasible vertex for `G`, so the coupling step never started.
- **Root cause (construction):** throughput. Separation adds at most 1500 rows a round against tens of thousands
  violated, each round costs one LP of 960 variables, and row construction is unvectorised. At the measured rates a
  single vertex needs at least about 29 rounds. This is a different failure from F2.
- **Structure of the Ω_h target, measured:** the 57 456 `G`-tight pool-A quadruples at `R` have rank 768 modulo
  `2³¹ − 1` (so rank over ℚ ≥ 768) and float rank 768; adding the `H`-side rows leaves the float rank at 768
  (`work/a8-omegah.out`, `work/a9-omegah.out`). With pools A ∪ B the float ranks are 776 (`G`) and 784 (`G + H`)
  (`work/a9-omegah-AB.out`). So, unlike `eball3`, Ω_h's gate lies on a face of the relaxation of dimension at most
  192 (exact bound from the modular rank; equality is a float measurement), of which about 176 dimensions survive a
  doubled pool. Whether those directions are genuine gate families or pool blindness is not determined here.

### A precision note on comment 6255285218

"`cnot` composed with a control-side Z-rotation passes every clause" holds for the rotation by π only: exact
verification on pools A ∪ B gives PASS for `R ∘ (Zπ ⊗ 1)` and `(Zπ ⊗ 1) ∘ R`, and `relC` fails for the rotation with
`cos = 3/5`, `sin = 4/5` (`work/a5.out`). This agrees with §F2 item 3: the gate is isolated, not on a continuous
family, in this relaxation.

## 2. Repairs, measured where cheap

### 2.1 The exact verifier

Unchanged. Its self-test passes on both bodies (`python3 -I -B controls_verify.py --self-test`: reference PASS,
identity fails the frame, `ref ∘ (1 ⊗ K₂)` fails `posFwd` only, `ref ∘ (1 ⊗ K_{1/2})` fails `posInv` only, invalid
effect fails VE, outside state fails VS, bad shape fails; `self-test: OK`).

### 2.2 Generator coupling: joint sequential linear programming (SLP)

Each step solves one LP in `(λ_G, λ_H)`: minimise `‖G_k H_k − 1 + ΔG H_k + G_k ΔH‖₁` subject to pool-A positivity of
both `G` and `H` (constraint generation) and a trust region, accepting a step only if `max|GH − 1|` decreases
(`scripts/a10_slp.py`). Float; any output goes to the exact verifier.

- Basin, both `G` and `H` perturbed (`ε ∈ {10⁻³, 3·10⁻², 0.3}`, 3 trials each): 9 of 9 return to `R`
  (residual ≤ `5.3·10⁻¹³`, `|G − R| ≤ 1.3·10⁻¹²`) in 2–4 steps, where the alternation stalls in 9 of 9
  (`work/a10-basin-both.out`). A first basin test that perturbed `H` alone was discarded: with `G = R` fixed it is
  solved trivially by one LP.
- Random starts (the generator's own vertex starts, seeds 1000–1004, 120 s each): start 3 reaches residual
  `1.3·10⁻¹²`; the other four stall at `0.88–1.0` with the trust radius collapsing (`work/a10-random.full`).
  Start 3's point, exactified by the frozen `exactify`, is a signed permutation `G = R ∘ diag(s)` with a
  non-product sign pattern, `G ≠ R`, `G ≠ R ∘ (Zπ ⊗ 1)`, `G² ≠ 1`; the frozen exact verifier prints **PASS** on pools
  A and B (`work/slp-verify-eball3-s3.json`, sha256 `80a367f8…ba1f`; candidate sha256 `5dc9fa9b…b393`;
  `work/a12.out`). A float diagnostic on 10⁶ random pure-state/pure-effect quadruples off the pools finds no value
  below `−10⁻⁹` for either `G` or `G⁻¹` (`work/a13-slp-s3.out`); that is not a certificate.

Reading: the SLP coupling converges to isolated gates from a neighbourhood and recovered an accepted `eball3` gate in
one of five random starts; it is still a local method and stalls from most starts. One hit in five starts is too small
a sample to set a cap.

### 2.3 Other repairs (described, not run)

Ranked by expected effect on the two failures.

1. **Vertex-step throughput (F3).** Vectorise row construction (the vectorised Gram over all 919 368 tight
   quadruples of pools A ∪ B completed within one bounded command, not separately timed, against 74 s for 3000 rows
   in the loop); add every violated
   row, or solve the full pool LP directly at `D = 3`; warm-start the dual simplex between rounds.
2. **SLP coupling (F2)**, §2.2, with a frozen multistart count and trust-region rule.
3. **Active-set exactification.** At an isolated gate there is no slack, so a rounded float point passes exact VP
   only if it is the vertex itself. Identify the near-tight rows, solve exactly (Fraction) on a full-rank subset, then
   verify; `limit_denominator` remains the fallback.
4. **Involutive ansatz `G² = 1`** as an optional restricted cell: `posInv` coincides with `posFwd`, both controls are
   involutive (exact). Its outcomes speak only of involutive gates; the SLP hit in §2.2 is not involutive, so this
   ansatz would have excluded it.
5. **Symmetry ansatz**, only with a frozen subgroup containing the controls' gates: the `eball3` reference commutes
   with `g ⊗ g` for `g = diag(1, −1, 1)`, with `Zπ ⊗ 1`, and with no other element of the sign stabiliser of
   `(z3, nflip)` acting on one factor or both (`work/a7.out`). An ansatz under the full stabiliser on both factors
   excludes `cnot`.

**Exact constructive recovery versus optimisation.** Exact recovery of the controls succeeds trivially and certifies
the verifier (the reference passes; so do `R ∘ (Zπ ⊗ 1)` and the SLP candidate). It does not calibrate the
generator: a linear objective built from `R`'s tight rows returns `R` to `10⁻¹³` (`work/a4-eball3.out`), which is the
vacuity hazard (the control would reproduce what it is meant to find). Optimisation from inputs that exclude the gate
is the only reading that tests the generator, and the two controls test it in opposite regimes: an isolated vertex
(`eball3`) and a face of dimension up to 192 (Ω_h).

## 3. Corrected control design (proposal)

### 3.1 What the preflight must show

(a) The exact verifier distinguishes gates from the kernel's linear-layer non-gates (unchanged self-test).
(b) The frozen generator, receiving `(z, N)` and the generation pool only, returns within the frozen cap a candidate
the verifier accepts on each control body, in each regime a search hit could occupy: isolated (`eball3`, preferably in
the family's own parametrisation `Ω_R(1, 1; 2)` with the family's pool rules, so the search code path is exercised)
and on a face (Ω_h).
(c) The acceptance is attributable to the repair: the frozen alternating generator (`e8ac54b5`) under the same cap
fails where the repaired one passes.
(d) Before any `D = 7` cell reads `HIT`, the same generator, pools and cap on `eball 7` with the family's pair
(`ne_seven_of_nativeGate`, CompositeDimension.lean:2741, kernel exclusion) return no accepted candidate. Scope: this
measures whether the pools let the generator manufacture a pool-relative "gate" where the kernel proves none; its
passing does not establish pool adequacy, since the generator is not exhaustive.

### 3.2 Decision rule (preregistered rule; no expected numbers)

| item | rule |
| --- | --- |
| P0 | `controls_verify.py --self-test` prints `self-test: OK` for both bodies; otherwise every preflight verdict is void |
| P1 | static independence check: the generator imports nothing from the verifier, reads no file but its pool, and contains no reference table; otherwise void |
| P2(c), c ∈ {`eball3`, `omegah`} | `PASS(c)` iff the verifier prints `PASS` on the generator's candidate within the cap; `FAIL(c)` otherwise (timeout, no candidate, exactification failure or verifier FAIL), with the reason recorded |
| P3 | the frozen alternating generator, same pools and cap, run on `eball3`: recorded as `XP1 fails as stated` or `XP1 does not fail`; it voids nothing, and if it does not fail, no reading credits the repair |
| park | as decided (6254707076): `FAIL` on either control parks the round |
| P4 (`D = 7` design, if written) | each `HIT-B` requires P2 PASS on both controls and the `eball 7` run of 3.1(d) with no accepted candidate at the same pool size and cap; an accepted `eball 7` candidate voids every `HIT` at that pool size |

### 3.3 Countercontrols

| credited element | countercontrol (the reading fails without it) |
| --- | --- |
| verifier `posInv` | `ref ∘ (1 ⊗ K_{1/2})` passes VL and `posFwd`, fails `posInv`; `gSq` on `eball 5` |
| verifier `posFwd` | `ref ∘ (1 ⊗ K₂)`; `gRev 3` |
| verifier frame | the identity |
| generator repair | XP1: the frozen alternation fails on `eball3` (F2 reproduced) |
| generator independence | XC-VAC: an objective built from `R`'s tight rows is excluded by P1; it is shown to return `R` (the hazard is real) |
| pool discrimination for `HIT` | 3.1(d) on `eball 7` |

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
| determinism | replay of one start: residual and cut count equal to the logged values (as done in §F2) |
| no search body runs before `F` | the dispatched matrix names control bodies only (`C0`) |

### 3.5 Resource estimate for `D = 7`

Measured: Ω_h (`dim F = 960`, 147 456 pool-A quadruples): 74 s for 3000 cut rows (loop), 72–135 s per LP at
4500–6000 rows, 43 305 → 16 770 violated rows over two rounds (local, loaded host); CI: seven separation rounds in about
945 s with no vertex. `eball3` (`dim F = 48`): alternation starts 11–65 s each in CI; SLP starts up to 120 s locally.
Derived: search bodies at `D = 7` with the frozen pair have the same `H` signature (four `+1`, four `−1`), so the same
free pattern of 1024 entries; Ω_h's measured frame rank 64 gives `dim F = 960`, and the frame rank of each search
body is to be measured, not assumed. Speculative: under the frozen cut loop one vertex costs over an hour; no estimate
for a repaired generator at `D = 7` is possible before repair 1 of §2.3 is timed on Ω_h.

### 3.6 Is the search target still meaningful?

`Q-BODY` remains meaningful as a search for exactly verified, pool-relative candidates for later kernel work, under
four conditions: green P0–P2 with a repaired generator; P4 at the same pool size; the cell restated as relative to its
`(z, N)` and pools; and the non-inference rule extended by §4 N4 (a gate that is irrational in `F`'s coordinates
cannot be returned as a `HIT`). `UNDECIDED-B` carries no information about `B`, as the draft states. No negative
result is stated for any body: every failure in §1 is a failure of a method on a control.

## 4. Gem-finding pass (§A.31)

Productivity test, fixed before the walk: a node is a gem if it yields a fact stronger than "the generator failed"
and either constrains the design or exposes an assumption the draft makes.

| node | assumption under test | check | verdict |
| --- | --- | --- | --- |
| N1 | recovering a known gate by local optimisation measures generator sensitivity | exact vertex rank, exact Stiemke certificate, basin runs (§F2) | NEW: the `eball3` gate is isolated in the generator's own relaxation; the alternation cannot converge to it from any tested start; F2 is the method's failure |
| N1.1 | favourable branch: the SLP repair works | `H`-only basin discarded as trivial; both-perturbed basin 9/9; random starts 1/5; exact verifier PASS on the hit; float off-pool diagnostic clean | POSITIVE, local: recovery is possible; robustness is not shown |
| N2 | the Ω_h failure is the same phenomenon | cut-loop replay; rank 768 (≤ 192-dimensional face) | NEW: different cause (throughput); target on a face of the relaxation, not isolated |
| N3 | a search-body `HIT` would sit in a regime the controls calibrate | N1 and N2 place the controls at opposite regimes; a strictly convex body's regime is unknown | ELABORATING: controls calibrate only the regimes they occupy; both are needed |
| N4 | gates are rational in `F`'s coordinates | controls have coordinates in `{−1, 0, 1}`; an isolated irrational gate has no slack, so no rounded point passes exact VP | NEW (assumption-watch): `HIT` is reachable only for gates rational in `F`; stated scope, not a finding about any body |
| N5 | a symmetry ansatz is neutral | equivariance of `R` under the sign stabiliser (§2.3 item 5) | CONFIRMING: the ansatz group must be frozen with the controls' gates in it |
| N6 | `UNDECIDED-B` over green controls is informative | the generator is local and non-exhaustive | CONFIRMING the draft's non-inference rule |
| N7 | "no generator candidate on `eball 7` passes VP" is a countercontrol | vacuous while the generator fails C-POS; non-exhaustive even when it passes | NEW (design): restated as 3.1(d) with explicit scope and gated on green controls |
| N8 | E20's control failure was a tolerance stall | reproduced run 2; LOG's correction | CONFIRMING LOG.md: iteration-capped cutting plane; `posFwd`-only target known not to exclude |

One pass was made over these nodes; the fixed-point condition (three to four passes without a NEW finding) is not
met, so the list is not claimed complete.

## 5. Open questions for the owner

1. Adopt joint SLP as the generator's coupling, with which multistart count, trust-region rule and cap; and whether
   repair 1 (vertex throughput) must be timed on Ω_h before any re-dispatch.
2. Run the `eball3` control in the family's parametrisation `Ω_R(1, 1; 2)` with the family's pool rules, alongside or
   instead of the Pythagorean pool.
3. Is P3 (the frozen alternation must fail) required, or recorded only.
4. Gate every `HIT` on P4 (`eball 7`, same pools and cap), voiding `HIT` tokens at a pool size where `eball 7` yields an
   accepted candidate.
5. Whether the involutive ansatz is a separate restricted cell, given that it excludes the non-involutive gate found
   in §2.2.
6. Carried over: how parking evidence reaches `main` (§A.42; comment 6255285218, item 2), and whether `Entangling`
   is read by `HIT`.
7. Whether Ω_h's residual face (about 176 dimensions at pools A ∪ B) should be resolved — genuine gate family or pool
   blindness — before Ω_h serves as a control; a denser pool rank sequence is the cheap check.

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
$S/venv/bin/python -I -B $S/scripts/a6_omegah_vertex.py $P $S/work 420              # F3 replay
$S/venv/bin/python -I -B $S/scripts/a8_modrank.py $P $S/work omegah
$S/venv/bin/python -I -B $S/scripts/a9_float_rank.py $P $S/work omegah AB
A10_BOTH=1 $S/venv/bin/python -I -B $S/scripts/a10_slp.py $P $S/work basin 0.3 3
A10_ONLY=3 $S/venv/bin/python -I -B $S/scripts/a10_slp.py $P $S/work random 1 120
python3 -I -B $P/controls_verify.py --verify eball3 $S/work/slp-candidate-eball3-s3.json $S/work/slp-verify-eball3-s3.json
(cd $S/e20/research/equivalence/experiments && $S/venv/bin/python -I -B e20_odd_bodies.run2.py)   # F1 replay
```
