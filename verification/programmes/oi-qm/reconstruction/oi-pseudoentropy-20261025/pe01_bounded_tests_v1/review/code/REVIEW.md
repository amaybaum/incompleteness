# Independent code review of PE-01 (OI-PE-1): dispatch readiness

- **Head reviewed:** `0f1391cd470ec5c8513de05ced1bad3c61050c08` on `research/oi-pseudoentropy-20261025` (draft PR #923).
  The six code commits `0c91d5c8..0f1391cd` descend linearly from the frozen preregistration `85096e3f`. They add only
  the package code and `.github/workflows/pe01-bounded-tests.yml`, and `PLAN.md` and A1 are untouched. PIN's ancestry
  facts hold: `af38dc2d` and `1e025b67` are ancestors of `0c91d5c8`.
- **Read in full:** `PLAN.md`, `amendments/A1-owner-decisions.md`, `review/plan/README.md` (the plan-review records were
  skimmed for context only), `pe01/*.py`, `run.py`, `verdict.py` and the workflow. AGENTS.md is read as on `origin/main`,
  including §A.44.
- **Nothing was modified, committed, pushed, dispatched or posted.** All work ran in a fresh scratch clone.

## Verdict: BLOCK (narrowly), for dispatch readiness, even assuming the amendments for the open items are made

The verdict-bearing arithmetic is correct. My independent re-implementations agree exactly with the code (below), every
mutant aimed at an existing checkpoint was caught on its own condition, and the smoke reproduces green. The block is for
three reasons:

- **Controls that cannot fail.**
  - Nothing checks the window detection that decides condition (d) (R1).
  - Nothing checks K_cx where it matters (R3).
- **Checkpoints below the plan's stated scope.**
  - MO is not run on the m = 3 sweep (R4).
  - IM3 is not run on linear filters (R5).
- **Defects that cannot be fixed after the run.**
  - The verdict text prints undetermined horizons as values (R2).
  - The output format breaks GitHub's file-size limit (R6). RP compares bytes, and committed outputs must be the
    produced bytes, so the format must be fixed before dispatch.
  - Provenance is incomplete (R7).
  - An incomplete run is mislabelled VOID (R8).
  - Amendments are not tied to TH (R9).
  - The workflow may not be dispatchable from the branch (R10).

Each required fix is small and local.

## What I verified independently

- **Exactness control on adv^pred (§A.21).** `mine/brute.py` is written from the plan's definitions and shares no PE-01
  code. It brute-forces Pr[χ(v_K) = x_K] for every observer (ρ₀, ρ₁, a) and every χ, active observers included. It agrees
  exactly with `embedded.Sweep`'s K1 prediction curves, both all and passive, and with its window counts at every K, on:
  - G_clk n = 3, m = 1, K ≤ 14;
  - G_filt n = 4, m = 1, K ≤ 20;
  - G_clk n = 4, m = 1, K ≤ 20;
  - G_lin n = 3, m = 1, K ≤ 12;
  - G_clk n = 3, m = 2 (all 9216 observers), K ≤ 10.
- **K0 deterministic, worst and average, m = 1.** `mine/brute_k0.py` brute-forces every (ρ, a, F) with its own Q
  recursion. It agrees exactly with `Sweep.k0w` and `Sweep.k0a` on 𝔉_clk(3), 𝔉_filt(4) and 𝔉_lin(4) for K ≤ 9.
- **The m = 3 canonical forms.** `mine/m3check.py` finds 306 432 forms, all distinct. Each one is a fixed point of an
  independently coded BFS canonicalization, so every form is reachable and canonical. The forms with k ≤ 4 equal the 88
  classes obtained by canonicalizing all of Sym(4)². Together with the per-k Hall counts the code already checks, this
  proves the enumeration complete.
- **The linear-filter reduction, per observer.**
  - The argument holds. Since v₀ = 0, v_K = Σ_t x_t A^{K−1−t} b lies in the cyclic subspace W = span{Aⁱb}. The map
    ψ: Aⁱb ↦ eᵢ is a linear isomorphism W → F₂ʳ that conjugates A|_W to the companion matrix of g, the minimal
    polynomial of b, and sends b to e₀.
  - g(0) = 1 because A is invertible, and every such g of degree ≤ m is realized. That gives the 2^m classes.
  - Arbitrary functions of v restricted to W correspond to arbitrary functions on F₂ʳ. Linear functionals restrict
    surjectively onto W*.
  - The reduction is therefore exact for K1 with the optimal F, K1 prediction, the linear-prediction K0 and the window
    condition. It holds for passive observers only (a ≡ 0, item LF-A).
  - `mine/lincheck.py` checks every (A, b) at m ≤ 3 against its class representative on G_clk(3) and G_filt(4), K ≤ 14.
    It compares the multiset of (C₀, C₁, Q) cells and the set of linear-χ hit counts: 0 mismatches out of 1344 + 24 + 2
    observers per generator.
- **Smoke.** The 11 smoke shards ran in parallel on 4 cores, about 130 s wall, with controls green; collect and verdict
  printed SMOKE. I also ran the result-mode family shard n3-clk directly, which smoke never exercises: m = 2 active,
  linear filters m ≤ 4, the LP and IM3 on active observers. All its controls were green, in 163 s.
- **The dual LP.** The derivation is correct. For each sign pattern s, max_w min_φ s_φ(wΔ)_φ = min_π max_D Σ_φ π_φ s_φ Δ_φ(D),
  and the maximum over F is the sum of positive parts.
  - max_s min_φ s_φ y_φ = min_φ |y_φ|, so maximizing over the patterns gives the randomized worst case.
  - Taking s modulo a global flip is valid because the test class is closed under complement.
  - `solve_game` asserts exact primal = dual certificates, which is a real check.

## Mutants

Built by `mine/mutants.py` in scratch copies of the package. `BASE-*` runs of each harness on the unmodified copy are
all green.

| Mutant | Target | Outcome |
|---|---|---|
| (f) loosened to `footprint <= θ+1` | CX | caught: self-test fails on "footprint θ+1" (refused on: none) |
| (d) checks only the last K′ | CX | caught: self-test fails on "window value 1/8 − 2^(−K−2)" |
| (c) loosened to `K <= K_cx + 1` | CX | caught: self-test fails on "K = K_cx + 1" |
| clock register one bit short | FP | caught: FP fails, and IM3 (readout consistency) fails, at K = 1, 3, 4 … |
| output register width 0 | FP | crash (IndexError): a failure, but not a clean refusal |
| window floor `K >= Z+W` | AR | caught: region tables differ, θ = n rows 5–8 |
| Z over the autonomous control sequence only | AR | caught: "Z(G_clk) differs from the plan" |
| **K_cx = ⌈l_med/2⌉ instead of ⌊l_med/2⌋** | **AR** | **survives: AR passes, and so does every other check (R3)** |
| code θ(n) = n | TH | caught: "code theta(n) differs from the block" |
| code m = 3 cap at n = 8 set to 63 | TH | caught: "code m=3 cap at n=8 differs" |
| A1 block edited (θ at n = 8 → 10) | TH | caught: formula disagreement |
| a applied before ρ in the aggregated simulation | IM3 | caught: FullState mismatch and brute-force extraction mismatch |
| Q pushforward wrong (ρ₀⁻¹ used twice) | IM6, NC | caught: tape P_p ≠ Q_p at m = 1, 2 |
| **window test `>=` → `>`** | **(d)** | **survives: all windows vanish and every control stays green (R1)** |

## Findings

### Required

- **R1. Condition (d) is computed with no control that can fail.**
  - **Where.** The window detection is `pe01/embedded.py:300-338`: `ok = 4*|2S−M| >= M`, the run counters, and the `first`
    and `first_family` bookkeeping.
  - **The gap.** `embedded_bruteforce` (`pe01/shard.py:235-292`) checks K1 and the deterministic K0 only. Nothing compares
    the window set with an independent computation.
  - **Consequence.** The `>` mutant deletes every window, a favorable-direction defect, with all controls green. The
    current code is correct (my brute force agrees), so this is a missing checkpoint, not a bug.
  - **Fix.**
    - Extend `embedded_bruteforce` to compare, at every K, the count of (o, χ) with |adv| ≥ 1/8 at all of K−3..K against
      the Fraction tables: n = 3, 4 for m = 1 (all observers) and m = 2 (sample).
    - Cover the `"pred"` path as well (linear filters at n = 3, and an m = 3 sample). Add `_k0_pred`'s worst and average
      maxima, which today have no brute-force check either.
- **R2. `verdict.py` ignores the exactness flags and prints undetermined horizons as values.**
  - **Where.** `verdict.py:62-80` recomputes K_zero and K_δ from `values` alone. They are used at `:133-134`, `:145-153`
    and `:156`. The shard records the correct fields (`K_zero_determined`, `K_delta_determined`; `pe01/shard.py:52-64`),
    and the verdict never reads them.
  - **Examples from the smoke.**
    - `[n5-lin] B4d3 K1 on G_lin: … K_1/4=None (scope K <= 63)`. The true value is ≥ 1/2 from K = 6, since the degree-1
      annihilator belongs to the degree-≤3 class. The shard marks this K_δ undetermined.
    - `[n5-clk] B1 K0 worst: … K_1/4=119`. K_δ is undetermined here, and 119 is only an upper bound on it.
  - Each such line also sits under the section header "PROVED (exhaustive finite)". These are favorable readings
    presented as measurements (§6 item 5).
  - **Fix.**
    - Print from the record's determined flags. For example "K_1/4 undetermined (no certified value ≥ 1/4 in 24..63)",
      or "K_1/4 ≤ 119"; never `None` where undetermined.
    - Label bound and interval lines as bounds, not PROVED.
  - **Recommended, not required.**
    - Report the B4 lower bound at degree d as max(2^−d, the exact values at degree < d). The class is monotone in d.
    - Add MO: B4 at d ≤ B4 at d+1.
- **R3. K_cx has no control that can fail where it is used.**
  - **Why AR cannot see it.** K_cx enters AR only through the §7 tables (`pe01/ar.py:45-51`, `:58-60`). At θ = n+1 the
    clock bound 2^{n−m} − 1 ≤ K_cx in every cell (from the measured values: K_cx = 2^{n−1} − 1 for G_lin and G_filt,
    and 5, 9, 20, 42, 84, 168 for G_clk). The tables therefore never depend on K_cx, and the ceil/floor mutant survives.
  - **Why it matters.** K_cx decides the attribution rule: whether a fails-(f)-only witness is "attributed to resources"
    or is recurrence-scale. Note that the same fact means (f) implies (c) for every admissible cell, so (c) never binds a
    COUNTEREXAMPLE at θ = n+1. The verdict could state this as a structural fact.
  - **Fix.** Add an independent K_cx check.
    - For G_lin and G_filt, the closed form K_cx = 2^{n−1} − 1. The states (x, 0) are two fixed points; every other state
      lies on a cycle of length 2^n − 1, because a balanced output sums to 2^{n−1} ≡ 0 over a period.
    - For G_clk, orbit lengths from a separately coded cycle walk.
    - Record l_med in the AR record.
- **R4. MO is missing for the m = 3 sweep, and K0 ≤ K1 is not checked pointwise.**
  - **Where.** `shard_m3` (`pe01/shard.py:1005-1051`) never calls `shard_curve_controls`, and collect has no cross-shard
    MO.
  - **Unchecked §5 inclusions.**
    - 𝒫ᵉᵐᵇ(2, passive) ≤ 𝒫ᵉᵐᵇ(3, passive), both distinguishing and prediction.
    - 𝒫ᵉᵐᵇ(3, passive) ≤ U.
    - Linear filters with m = 3 ≤ 𝒫ᵉᵐᵇ(3, passive), since they are passive m = 3 observers.
    - The m = 3 K0 records pass no K0 check (`per_phi` against the value).
  - These are cheap, independent controls on the canonical-form sweep.
  - **K0 ≤ min_φ K1 and K0 ≤ E_ν K1.** `pe01/shard.py:954-986` checks each K0 value against its own test's `per_phi`,
    plus the U interval ordering and deterministic ≤ randomized. It never compares K0 with K1.
  - **Fix.**
    - Add the cross-shard comparisons in `collect.py`, pointwise over the common K range.
    - Run the K0 `per_phi` check in `shard_m3`.
    - Check `per_phi[φ] ≤ K1(φ)` and K0 worst ≤ min over named φ of K1. Otherwise, narrow MO's wording by amendment.
- **R5. IM3 (the full-state path) is not run for linear-filter observers at n ≤ 4.**
  - **Where.** The linear `Sweep` at `pe01/shard.py:676-678` has no `im3=`.
  - `linear_reduction_check` (`:860-869`) compares only the class maxima of K1. Its docstring claims a per-(A, b)
    comparison and the linear-prediction values.
  - **Fix.**
    - Pass `im3=Cm.FullState if n <= 4 else None`.
    - Make the reduction check per observer: compare the cell multiset with the representative's, as `mine/lincheck.py`
      does, and include the K0 linear-prediction values.
- **R6. Output size and form (open item 8).**
  - **The problem.**
    - `measurements.json` embeds every shard's full measurements (`pe01/collect.py:133`), duplicating the shard files that
      §8 also commits.
    - The smoke at n ≤ 5 already reaches 1.24 MB, without active observers, linear filters, the LP or m = 3. The largest
      parts are the K0 `per_phi` lists, per-K `argmax`/`tests` lists and the curve value lists.
    - The projected 80–100 MB is at or over GitHub's 100 MiB per-file hard limit (warning at 50 MiB). It is far from
      §A.42 item 1's "small structured file" and §A.28.
    - RP replays bytes, so the format is fixed at dispatch.
  - **Fix, before dispatch.**
    - `measurements.json` carries only the verdict inputs (controls, witnesses, horizons, AR, windows, shard statuses) and
      each shard file's sha256.
    - Shard curves are encoded losslessly and compactly: run-length encoding of repeated exact values, and `per_phi` and
      `argmax` stored only where they change, after the in-shard check has used them.
    - Collect fails if any file exceeds a stated budget, for example 20 MB.
  - Keep §2's "full exact curve" and the count multisets lossless.
- **R7. The committed structured outputs lack the run id (§8; §A.42 item 1; §A.44).**
  - Shard JSON deliberately omits it, which is right for replay. `<sid>.provenance.json` has it, but
    `measurements.json` and `verdict.json` do not (`pe01/collect.py:115-136`, `verdict.py:264`).
  - **Fix.**
    - Collect reads each `<sid>.provenance.json` and the replay records, and writes run id, attempt, job and shard sha256
      per shard.
    - `verdict.json` records the sha256 of `measurements.json`.
- **R8. "Not evaluated" is reported as VOID.**
  - **Where.** A primary shard that is incomplete or not run gets failures recorded for PC, NC, SY, MO, K0 and EX1
    (`pe01/collect.py:70-73`). A replay job that timed out records RP as failed (`:95-97`). In both cases `verdict.py`
    prints "VOID: failed checkpoint(s): …".
  - **Why it matters.** That states a failed checkpoint where none failed. VOID is defined in §6 item 1 as a failed
    checkpoint.
  - **Fix.** A separate class, `INCOMPLETE (no verdict)`, naming the unevaluated checkpoints and shards. VOID keeps
    precedence whenever an evaluated checkpoint failed.
  - **Recommended.** The incomplete record always writes `completed_cells: []` and drops the shard's controls (workflow
    lines 100-111 and 140-151). A control failure inside an m = 3 shard that later times out is therefore lost, contrary
    to A1. Write `<sid>.partial.json` after each class block, carrying the controls so far and the completed cells, and
    have collect ingest it.
  - The risk is low: the largest shards are about 1 h against a 330-min step timeout (Cost).
- **R9. Clearing an open item is a code edit, not an amendment.**
  - **Where.** `pe01/pending.py:502-514` is a code dict, and TH pins A1 only (`pe01/params.py:17-20`, `:211-226`).
  - **Fix.** The resolving amendment (A2) carries a machine-readable block that lists each resolved item id and its
    reading. TH pins A2's blob and ancestry exactly as it pins A1's, and records both blobs. `open_items()` returns the
    `PENDING` ids that A2's block does not resolve. Result mode refuses otherwise.
- **R10. Check that the workflow can be dispatched before asking for approval.**
  - `pe01-bounded-tests.yml` is not on `main`. GitHub's documentation states that `workflow_dispatch` requires the
    workflow file to exist on the default branch.
  - **Fix.** Land the workflow file on `main` through its own pull request, or confirm on the host that dispatch with
    `--ref research/oi-pseudoentropy-20261025` works. The run then uses the branch's copy at the run commit, which PIN
    pins.

### Nits

- **N1. FP is not independent of the clock-width formula.** Both sides use `composite.clock_bits` (`pe01/shard.py:390`,
  `:852`). FP therefore checks the layout arithmetic, not ⌈log₂(K+1)⌉. Undercharging is still caught, by IM3's readout
  check (mutant above). Compare instead with an independently written "least c with 2^c ≥ K+1".
- **N2. A tautological sub-check in IM2.** The "length-rule" check in `pe01/lc.py:229-232` recomputes `Ln`'s own formula
  and cannot fail. The real controls are the sibling-discrepancy check and the agreement of enumeration and DP. Remove
  it, or replace it with a check of the BM transition against brute-force LC.
- **N3. PC firing for 𝒫ᵉᵐᵇ(1) bypasses the sweep.** `pe01/shard.py:989-1000` uses a separate Sim/QChain path. Also assert
  that the sweep's emb_m1 curves on G_dec at K = 1 equal 1/2. That is exact, because the maximum is bounded by U = 1/2.
- **N4. The B1 K1 lower bound is not monotone beyond K = 23.** `pe01/bclasses.py:103-110` does not take a running
  maximum, although the class is monotone in K. Take max(curve[23], ·).
- **N5. The tag rules are partly unreachable or missing.** In `verdict.py:83-96`, the B4 COVERED-literature branch can
  never be reached, the BM (2·LC) and NC-1 closed forms are not implemented, and K0 lines get no tag (open item 4).
- **N6. K0 status is reported for the first witness only.** It covers only the first (o, χ) (`pe01/shard.py:793-794`,
  `:825-837`), and the verdict does not print `count_family`. Print it, and build a witness from `first_family` when
  `count_family` is nonzero.
- **N7. Malformed values crash instead of refusing.** `cx.conditions` raises on a malformed value (`pe01/cx.py:176`)
  instead of refusing on (d). Also cross-check the witness's `K_cx` field against AR's K_cx.
- **N8. θ is hard-coded.** `verdict.py:22-23` and `:200` hard-code θ = n+1; derive it from `theta_by_n`. The
  `theta_fn` argument of `ar.ar_check` is unused (`pe01/ar.py:99`).
- **N9. Make the canonical-form check stronger.** Add distinctness and canonicity assertions to the Hall-count check
  (`pe01/shard.py:377-381`). With them the completeness argument is mechanical.
- **N10. The verdict's resource-model statement is generic.** §6 item 5 asks that an empty or narrower region cell
  turn "no admissible witness" into a resource-model fact. State whether the cell is empty per combination, not in one
  generic sentence.
- **N11. Small free checks and workflow hygiene.**
  - MO: randomized K0 ≤ average K0. This is a free check, since a pure test attains the average.
  - The workflow pins actions by tag, not SHA, and has no `concurrency:` group.
- **N12. Window values below K are read from the K-clocked composite.** `Witness.simulate` reads the values at K′ < K
  from that composite's registers, not from K′-clocked composites. This is equivalent, because the readout does not
  touch (v, x), but say so in the record.

## Open items

**(1) B3W-K0.**
- **Is the computation determined?** The plan is right that exact enumeration fails: 2^(2^w) tests at w ≥ 5.
- **Is the proposed bound pair correct?** Yes, provided both ends are maximized over windows and combined with the
  exact w ≤ 4 value.
  - Worst case: D_∪ restricted to a window gives 1 − |∪_W|·2^−w on every φ, and min_φ TV_W bounds every test from
    above.
  - Average case: the test 1[mixture > Q] attains TV(E_ν P^W, Q^W) ≤ E_ν |Δ_φ|, and E_ν TV_W bounds every test from
    above.
- **But an exact computation exists for the average case, so the interval should not replace it.**
  - (i) μ is φ-invariant, because φ is a bijection and μ uniform. The record is therefore stationary: every window of
    length w has the same marginal per φ, and only 16 window laws exist.
  - (ii) max_D E_ν adv_D = (1/|𝔉|) · max_s Σ_z (Σ_φ s_φ Δ_φ(z))₊, maximized over sign patterns s.
    - Only the union of supports needs enumeration; the off-support points contribute
      (2^w − |∪|) · 2^−w · (−Σ_φ s_φ)₊ in closed form.
    - A Gray-code walk over s costs about 2^{|𝔉|−1} · |∪| per window length: about 10^9–10^10 integer operations at
      n = 7, 8 and trivial at n ≤ 6.
  - (iii) The deterministic worst case is a genuine max–min integer program, so the interval is correct for it, and it
    is a lower-bound object under §2 anyway. A randomized worst case is available through the existing dual LP over
    window points at n ≤ 6.
- **Recommended wording.**
  - "B3 window K0: windows of equal length have equal marginals (μ is φ-invariant). This is verified exactly for every
    window used, and a failure is a checkpoint failure.
  - The average case is exact, by sign-pattern decomposition over the union of supports. The deterministic worst case is
    exact for w ≤ 4. For 5 ≤ w ≤ 16 it is the interval [max(exact_{w≤4}, max_w (1 − |∪_w| 2^−w)), max(exact_{w≤4},
    max_w min_φ TV_w)], exact only where the ends coincide, and bearing on no verdict otherwise.
  - The randomized worst case is exact by the dual LP at n ≤ 6."
- **Owner decision:** yes. It amends §3's word "exact".

**(2) LF-A.**
- **Is a ≡ 0 the evident intent?** Yes:
  - §3 defines the subclass by ρ alone, while active observers are claimed only for "all observers with m ≤ 2".
  - "Linear filter" (Key 1976, §9) denotes a passive linear functional of the stream.
  - K0 tests are functions of memory only.
  - T1 asks a passive linear-system question.
  - The class reduction is exact only for a ≡ 0.
- **Recommended wording.** "Linear-filter observers are passive (a ≡ 0). The subclass {ρ_x(v) = Av ⊕ xb: A ∈ GL(m,2),
  b ∈ F₂^m}, m ≤ 4, is enumerated exactly through the 2^m classes of the minimal polynomial of b under A. IM3 checks it
  per observer against the full set at n ≤ 4. Every result and every 'no witness' statement for it names the scope as
  passive linear filters."
- **Owner decision:** yes, since it fixes the enumerated scope. The stakes are bounded: m = 4 cells are admissible only
  at n = 8, θ = n+1, K ∈ [12,15] | [10,15] | [9,15].

**(3) Reading (a) as the fixed G_lin(p_n), G_filt(p_n), G_clk(p_n).**
- **Plan-faithful?** Yes. §1 fixes the polynomials, "p_n is primary", and names G_lin(p′) as a negative-control
  sibling. Families exist "for K0", and §6 item 4 uses 𝔉 only for the K0 status.
- **What the reading excludes.** A witness on another family member would also be a finite reversible realization, so
  this reading narrows the refutation. That narrowing is conservative toward the claim under audit, and the verdict
  should say so.
- **Recommended wording.** "In (a), G_lin, G_filt and G_clk denote G_lin(p_n), G_filt(p_n) and G_clk(p_n). Other
  members of 𝔉(n), the sibling included, enter through the K0 status only. Per-member window existence is reported as a
  measurement."
- **Owner decision:** yes, confirming the reading.

**(4) The COVERED-literature tag rule.**
- **Is the computation determined?** Partly. The four closed forms are "fixed now", but their mechanical form is not.
  - "B4 at or beyond its counting horizon" appears under COVERED-corpus and again as "the B4 counting bound" under
    COVERED-literature.
- **Plan-faithful reading:**
  - COVERED-corpus first.
  - Then COVERED-literature, by exact comparison with closed forms computed from formulas, not from measurements:
    - (L1) B1 K1 on G_lin(p_n) or G_lin(p′_n) has K_zero = n, firing at n+1 with value 1/2.
    - (L2) B2 on the same: the value at λ = n+1 equals 1 − Pr_Q[LC ≤ n+1], and K_δ equals the least K at which that
      closed form reaches δ (Massey: BM fixes the sequence from 2·LC ≤ 2(n+1) symbols; Gustavson–Rueppel count).
    - (L3) The B4 counting horizon. It is subsumed by COVERED-corpus, which takes precedence.
    - (L4) A B-class K1 curve equal pointwise to max(0, 1 − 2^{n−K}).
  - Otherwise untagged. candidate-NEW is never assigned by code. K0 lines get tags by the same rules.
- **Owner decision:** yes, but light. It is a reporting rule and bears on no verdict.

**(5) The implementation choices.**
- **Three candidates per combination: sound.**
  - (c) and (f) are both downward-closed in K; footprint is non-decreasing in K. (a) and (e) are global, and (b) is
    per witness: a failure there is itself a control failure and makes the stage VOID.
  - So the least window K decides COUNTEREXAMPLE, and the largest window K ≤ K_cx decides the attribution.
  - At θ = n+1, (f) implies (c) in every cell (R3).
- **The single B1 WHT: correct.** The Fourier coefficients of the [0, K] marginal are the K = 23 coefficients at
  T ⊆ [0, K], and IM4 confirms this. The B1 average K0 beyond K = 23 as a lower bound is correct, subject to R2.
- **EX8 over prediction F only at m = 4: acceptable.** The readout map's EX8 property does not depend on F, and every
  verdict-bearing witness is checked on its own composite.

**(6) K1 range to K_max.**
- **Plan-faithful?** Yes: §1 sets K ≤ K_max(n) except where §3 caps. The caps are m ≤ 2 K0 ≤ 255, the B-class limits
  and A1's m = 3 caps.
- **Owner decision:** no amendment is needed.

**(7) |adv| or a signed direction in condition (d).**
- **The literal text.** §2 defines adv^pred_D = |Pr_P[χ = X_K] − 1/2|, and (d) cites it. |adv| is the literal reading,
  and the code implements it faithfully.
- **The difference is material.**
  - My brute force on G_clk n = 4, m = 1 finds 4 |adv| windows at each of K = 11–14. Only 2 at K = 12 have one sign
    throughout.
  - G_clk n = 3, m = 2 has about 4–6 times as many |adv| windows as signed ones.
  - The first candidate witnesses in the smoke and in the result-mode n3-clk run alternate in sign. For example,
    n5-lin emb_m2_passive at K = 19 has Pr − 1/2 = (−9/64, 11/64, −5/32, 9/64).
- **What |adv| does to the window.** Once χ is held fixed across the window, |·| lets the effective predictor switch
  between χ and ¬χ from one K′ to the next. That is analyst choice of orientation per K′, which is what a fixed window
  exists to exclude.
- **Recommendation.**
  - Owner decision before dispatch, by amendment.
  - My recommendation is the signed reading for COUNTEREXAMPLE and attribution: the same χ attains
    Pr_P[χ = X_{K′}] − 1/2 ≥ 1/8 at every K′. It is conservative toward the claim under audit, as the plan already is
    for (f).
  - |adv|-only windows are reported as measurements, labelled sign-alternating.
  - Both counts are recorded.
  - The code change is one line in the window test, plus the run counter per χ. The monotonicity argument for the three
    candidates is unchanged.
  - If the owner keeps |adv|, the verdict must print the sign pattern (`pred_minus_half`) beside every COUNTEREXAMPLE.

**(8) Output size.** Required as R6. It is a technical fix, not an owner decision, provided the encoding stays lossless.

## Cost (§A.40)

My measurements on this 4-core host, one process each:

| Work | Measured | Extrapolated |
|---|---|---|
| n = 8 G_clk, m = 2 all, 2048 observers, deterministic K0 with 16 φ, K ≤ 16 | 24.1 s | ≈ 30 min per n = 8 family shard for 𝒫ᵉᵐᵇ(2) (K0 to 255, K1 to 1020) |
| m = 3 passive, n = 6 G_lin, K ≤ 30 | 357 s (full set) | ≈ 50 min at K ≤ 252 |
| m = 3 passive, n = 8 G_clk, K ≤ 31 | ≈ 32 min (full set) | — |
| dual LP, n = 6, m = 2, K = 31 | 0.3 s per sign pattern | ≈ 5 min for 32 patterns × 32 K |

- **Totals.** Compute comes to about 12–17 h, doubled by the replay jobs, about 25–35 runner-hours. The implementer's
  35 runner-hours is plausible. The wall-clock of 2–5 h is plausible too: 76 jobs, the longest shard-plus-replay chain
  about 2–3 h, against a 20-job concurrency limit.
- **Against §8.** This exceeds §8's sums, about 3–8 h without replay, by about 2× for compute. That is within §8's
  factor-3 tolerance, and RP accounts for the doubling.
- **Timeouts.** No shard is near the 330-min step timeout.

## Hygiene

- Neither the code nor the smoke outputs contain local paths, secrets or tokens. Recipes use `<dir>` placeholders;
  provenance records `local` off-CI.
- No `results/` directory or smoke output is committed at the head.
- The workflow is `workflow_dispatch`-only with `contents: read`.
  - The other push-triggered workflows on `main` do not run PE-01 code.
  - Shards write only to `out/` and artifacts.
  - The final marker reads `verdict.json`, which is structured data (§A.44).

## Scratch artefacts (not committed)

All under `<scratch>/revpe01code/`:

- `mine/brute.py`, `mine/brute_k0.py`, `mine/m3check.py`, `mine/lincheck.py`, `mine/mutants.py` (with the generated
  `mine/driver.py`), `mine/bench.py`, `mine/bench3.py`, `mine/benchlp.py`, `mine/resultpath.py`;
- `smoke.sh` and `smoke.log`, with the smoke outputs in `smoke_out/`.

***

# Addendum: re-review of head `df280443791abcdbe15c957cc843ae47379b7c09`

- **Scope.** The five commits on `0f1391cd`: `ba974de6` (R9), `069922fb` (R3, R6 and the B3W exact average), `38b136b8`
  (R1, R4, R5), `d4f4f100` (R2, R6–R8) and `df280443` (runner and workflow).
- **Method.** Every diff was read in full. Everything ran in my scratch clone, read-only, and nothing was dispatched or
  posted.

## Verdict: BLOCK (narrowly) on one new required item, R11

- R11 is a control that is vacuous where it matters, introduced with the B3W fix (below). I verified the computation
  itself independently, and it is correct.
- **Once R11 lands, the verdict is ACCEPT WITH NITS for dispatch**, conditional on:
  - **A2.** The amendment carrying the `pe01-resolutions` block, plus the one-line code commit that pins its commit in
    `params.A2_COMMIT`. R11's fix can ride in that same commit.
  - **R10.** Confirm on the host that `workflow_dispatch` works from the research branch, or land the workflow file on
    `main` first.

## What I re-ran (all bounded, local)

- **Smoke at the new head.** Green: 11 shards in parallel, about 130 s wall; collect reports `status green`, and the
  verdict prints SMOKE.
  - The smoke `measurements.json` is 153 KB; the largest shard file is 161 KB (n5-clk), against 1.24 MB at `0f1391cd`.
- **My own mutant harness**, `mine/mutants2.py`, rebuilt from my original. It writes copies to `mut2r/` and uses its own
  driver, `mine/driver2.py`.
  - The driver was updated only for the new API: the `(reading, subclass, generator)` window keys, `ar_check(plan)`, the
    selftest output shape, and FP against `clock_bits_independent`.
  - All seven BASE runs are green.
- **An independent B3W brute force**, `mine/b3wcheck.py`.
- **The signed-window semantics** against my original brute force.
- **A forced-incomplete test-mode shard:**
  - test-mode n3-clk, killed after 40 s, with the implementer's A2 stub;
  - then `run.py incomplete`, `collect` and `verdict.py`.
- **Result-mode refusal.** A result-mode shard refuses: "open plan items without an amendment: B3W-K0, D-SIGN, LF-A,
  TAG-L, WIT-A".

## Mutants (re-run from my own harness)

All 14 of my original mutants are caught, each on its own condition. The two that survived before are now caught:

- **AR-Kcx-upper-median:** "K_cx(G_lin, n=3) = 4 disagrees with the independent value 3".
- **WIN-strict:** IM3 window mismatches in `embedded_bruteforce`, n = 4, G_clk, m = 1, K = 11–14, and in
  `pred_bruteforce` (passive linear filters, m = 3).

FP-out-register-dropped is also a clean refusal now (FP, EX1 and IM3 fail; no crash).

**The two retargeted patch strings in the implementer's `mut2/mutants.py` keep their meaning:**
- **CX-d-last-only:** `for a in vals)` → `for a in vals[-1:])` inside `_all_ge`. This again checks only the last K′, now
  under both readings. It is caught on "window value …" and "malformed value" under both readings, and on
  "sign-alternating window [signed]".
- **WIN-strict:** `("abs", 4 * np.abs(d2) >= M)` → `>`. This is the same strictness change on the abs reading. The
  implementer's extra mutant, WIN-strict-signed, is the analogue on the signed reading.

**New mutants I added:**

| Mutant | Outcome |
|---|---|
| WIN-strict-signed | caught by IM3 (signed window counts) |
| SIGN-as-abs (signed test replaced by `4*abs(d2) >= M`) | caught: signed counts 0 vs 4, and 26 vs 94 |
| **B3W-gray-flip** (`y += s[j]*D[j]` instead of `2*s[j]*D[j]`) | **survives** (R11) |
| **B3W-outside-dropped** (off-support term removed) | **survives** (R11) |

## Status of R1–R10

- **R1, fixed.**
  - `embedded_bruteforce` now compares both readings' window counts, primary and family-wide, with a scalar brute force
    that shares no code with the sweep: n = 3, 4 at m = 1, and an m = 2 sample.
  - `pred_bruteforce` covers the pred path: passive linear filters at m = 3 and m = 2, and an m = 3 sample, including
    the K0-pred maxima.
- **R2, fixed.**
  - Horizons come from the shards' determined flags.
  - The smoke now prints `[n5-clk] B1 K0-worst … K_1/4 <= 119`, under 1b "Bounds and intervals (not PROVED)".
  - B4d3 on G_lin at n = 5 now reads K_1/4 = 6. That value is correctly determined: a certified lower bound ≥ δ at
    K = 6, with exact values below δ before it.
  - The B4 bound at degree d now takes the exact values at lower degrees, and MO checks B4 at d−1 ≤ B4 at d.
  - Interval lines print K ranges.
- **R3, fixed.** `kcx_independent` uses a scalar orbit walk, plus the closed form 2^{n−1}−1 for G_lin and G_filt.
  l_med is recorded, and the verdict states that (f) implies (c) at θ = n+1.
- **R4, fixed.**
  - `k0_vs_k1` runs pointwise, both `per_phi` against K1 and worst against K1, over the named φ, skipping K1 points that
    are not exact.
  - The K0 record checks run in `shard_m3`.
  - m = 3 ≤ U is checked in-shard, and passive m = 2 ≤ passive m = 3 and `plin_m3` ≤ passive m = 3 across shards in
    collect.
  - Also added: worst ≤ average, and deterministic ≤ randomized ≤ average.
- **R5, fixed.** The linear sweep carries `im3=FullState` at n ≤ 4, and the reduction check is now per observer: the
  sorted (C₀, C₁, Q) cells and the sorted linear-prediction hit counts against the class representative, for every (A, b).
- **R6, fixed.** RLE is lossless. `measurements.json` carries verdict inputs plus each shard's sha256 and byte count,
  and collect refuses any file over 20 MiB. The 1–3 MB projection for n = 8 is consistent with 161 KB at n = 5.
- **R7, fixed.** Collect writes run id, attempt and job per shard (from provenance) and the run id of the collect step.
  `verdict.json` records the measurements sha256 and the run.
- **R8, fixed, with one edge case (nit N13).**
  - Checkpoint status is failed → VOID, unevaluated → INCOMPLETE (no verdict), otherwise green. A failed checkpoint
    takes precedence.
  - A primary shard that is not complete, or a replay record that is missing, makes the stage INCOMPLETE.
  - `<sid>.partial.json` is written after every block. My killed test-mode n3-clk produced an `incomplete.json` keeping
    seven completed cells and the EX1, EX2, EX7, EX8, FP, IM3, K0 and MO controls. Collect ingests those controls, so a
    failure inside an incomplete shard voids the stage.
  - The workflow marker fails on both VOID and INCOMPLETE.
  - **This matches A1.** A not-run or incomplete m = 3 shard leaves its cells "not run" or "incomplete", is not a verdict,
    and does not by itself make the stage incomplete. A checkpoint failure inside it is VOID. Its partial output is
    committed, since the incomplete file is retained and hashed.
- **R9, fixed.** `pending.open_items()` is driven only by the `pe01-resolutions` block of A2, and a reading counts only
  if it is listed in `READINGS`. In result mode TH requires a pinned A2: `A2_COMMIT` set, blob unchanged, A2 an ancestor
  of the run commit, A1 an ancestor of A2. A2's blob and resolutions are recorded. Test mode accepts an unpinned stub,
  labels everything "TEST OUTPUT: NOT A RESULT", and collect refuses to mix modes.
- **R10, open.** It is operational, and remains a dispatch condition.

**The 12 nits are fixed:**
- N1: `clock_bits_independent`.
- N2: the tautological sub-check is removed.
- N3: the sweep's emb_m1 values on G_dec at K = 1 are asserted to be 1/2.
- N4: the B1 curve and K0 beyond K = 23 take running maxima.
- N5: tags L1–L4, COVERED-corpus first, K0 lines tagged.
- N6: a family-wide candidate, per-member window counts, and `count_family` printed.
- N7: a malformed value refuses on (d), and each witness's K_cx is checked against AR.
- N8: θ is derived from `theta_by_n`; the unused argument is removed.
- N9: distinctness and canonicity assertions.
- N10: the region-cell statement is per combination.
- N11: randomized ≤ average. The pinned action SHAs match their tags (`git ls-remote`: checkout v4.2.2, setup-python
  v5.6.0, upload-artifact v4.6.2, download-artifact v4.3.0). A concurrency group is added.
- N12: the window note.

## The new B3W exact average, verified independently

`mine/b3wcheck.py` brute-forces max over every test D of mean_φ |P_φ(D) − Q(D)| on a window: all 2^(2^w) tests for
w ≤ 4, and meet-in-the-middle over all 2^32 tests at w = 5 for |𝔉| = 2.

- **Synthetic families**, |𝔉| = 3–5, 4 or 8 seeds, so that supports are small and the off-support term and the
  multi-flip Gray walk are active: **160 of 160 equal** to `b3_window_k0`.
- **Real families: all equal.**
  - n = 3 G_clk, w = 1–5 (w = 5: 5/16).
  - n = 3 G_filt, w = 4.
  - n = 4 G_clk, w = 4 and 5 (w = 5: 3/16).
  - n = 4 G_filt, w = 4.
  - n = 5 G_filt, w = 3 and 4; n = 5 G_clk, w = 4; n = 6 G_clk, w = 4.
- **Stationarity is checked mechanically** and holds for every family tested.

The decomposition is right, and so are the Gray-code update (y += 2 s_j D_j with s₀ fixed to +1), the off-support
closed form (2^w − |∪|)·(−M Σ s)₊ and the use of s modulo a global flip.

- **The worst case.** It is exact for w ≤ 4 by enumeration, with a mechanical average-vs-all-tests check there. For
  w ≥ 5 it is the interval [max(exact_{w≤4}, 1 − |∪_w| 2^−w), max(exact_{w≤4}, min_φ TV_w)]. Both ends are valid bounds.
- **The `per_phi` of the D_∪ lower end** is [lo]·|𝔉|, correctly, since P_φ(∪) = 1 for every φ.

## D-SIGN, the signed reading

The signed reading computes "one sign across the whole window for the same χ", as asked.

- **The run counter.** It is `4·(2S − M) ≥ M` for each χ (Pr[χ = X_K′] − 1/2 ≥ 1/8), reset on failure, with
  ≥ 4 consecutive K′ required (`embedded.py`). χ ranges over all 2^V functions, so a window of constant negative
  orientation for χ is counted exactly once, as the positive window of ¬χ.
- **Against my brute force.** Signed counts are exactly half of my "constant sign, either orientation" counts:
  - G_clk n = 3, m = 2: 360, 312, 372, 336 and 306 at K = 6–10, against 720, 624, 744, 672 and 612;
  - G_clk n = 4, m = 1: 1 at K = 12, against 2.
  - The abs counts are unchanged.
- **Downstream.** CX (d) under `signed` reads `pred_minus_half`. The witness K0 status and the family windows use the
  same signed rule. The verdict uses only A2's selected reading for COUNTEREXAMPLE and attribution; before A2 it prints
  both.

## New findings

- **R11 (required). The B3W exact-average control is vacuous where it matters.**
  - **Where.** The only control is `avg == avg_brute` at w ≤ 4 on the real families (`pe01/shard.py`, B3 block;
    `pe01/bclasses.py` `b3_window_k0`).
  - **At n ≤ 4**, |𝔉| = 2. The Gray walk then makes a single flip, and Σs ≥ 0, so the off-support term is always 0.
  - **At n ≥ 5**, windows with w ≤ 4 are exactly uniform, every average is 0, and the check compares 0 with 0.
  - **The off-support term never appears at w ≤ 4 on real families**: at least 64 seeds always fill all 2^w ≤ 16
    patterns.
  - **Consequence.** B3W-gray-flip and B3W-outside-dropped survive with all controls green. The code is correct at this
    head (my 160 synthetic and 12 real comparisons above), but the dispatched run would not detect a regression.
  - **Fix.** In the controls shard, add a synthetic self-test: random families with |𝔉| = 3–6 and 4–8 seeds, w ≤ 4,
    comparing `b3_window_k0`'s average with an all-tests brute force. `mine/b3wcheck.py` part (1) is a template. Then
    confirm that both mutants are caught.

## Nits

- **N13. The R8 split has an edge case.**
  - If no shard completes, `th` is None, collect records the CX self-test as *failed*, and the status becomes VOID
    (`pe01/collect.py:112-114`). `verdict.py` then crashes in `vg_selftest` on `limitation(None)` (`verdict.py:41`,
    `:306`), so no `verdict.json` is written.
  - Reproduced with the killed test-mode shard.
  - **Fix.** With no θ, record CX as unevaluated, so the status is INCOMPLETE, and guard `limitation()`.
- **N14. Three m = 3 handling gaps.**
  - In result mode, a complete m = 3 shard whose replay record is missing makes the whole stage INCOMPLETE
    (`collect.py:124-128`). Per A1, that m = 3 shard's cells should go "incomplete" instead.
  - `shard_m3` never calls `progress()`, so an incomplete m = 3 shard keeps no controls (its n ≤ 4 exhaustive EX1/EX8).
    Add a `progress` call after the exhaustive maps.
  - A job that fails before the shard step starts, e.g. at `pip install`, is labelled "incomplete" rather than "not run".
- **N15. L2 compares the B2 K1 K_δ, a maximum over λ, with the closed form at λ = n+1.**
  - At n = 4 and 5 a smaller λ fires earlier (K1 K_1/8 = 6 vs 8, and 8 vs 10), so L2 tags only n = 3.
  - This is conservative: it never produces a false COVERED tag. Say so in A2's TAG-L wording, or also compare with the
    closed-form K1 maximum over λ.
- **N16. Cosmetic.** Under reading `abs`, witnesses picked under both readings are listed together, so the same K can
  appear up to three times, with different (O, χ). Consider labelling each line with `found_under`.

## Conditions for dispatch, restated

1. **R11 lands**, preferably in the same commit that sets `params.A2_COMMIT`.
2. **A2 lands** with a `pe01-resolutions` block resolving B3W-K0, LF-A, WIT-A, TAG-L and D-SIGN, with D-SIGN choosing
   `signed` or `abs` by owner decision.
   - Then the pin commit lands.
   - Then a fresh local smoke and a test-mode or result-mode preflight run at that head, confirming refusal is gone
     only for the resolved items.
3. **R10 is confirmed** on the host, and the owner approves the dispatch (§A.43 item 4).

***

# Addendum 2: confirmation at head `07f3c127f55c48e74c15d06a344a91894da4c41a`

The diff `df280443..07f3c127` (`63fd3a69` R11, `07f3c127` N13–N16) was read in full. Everything below ran read-only in
scratch.

## Final verdict: ACCEPT WITH NITS for dispatch, conditional on A2 and R10

- **A2.** The amendment with its `pe01-resolutions` block, D-SIGN chosen by the owner.
- **The A2 pin.** The pin commit setting `params.A2_COMMIT`, followed by a smoke and preflight at that head.
- **R10.** Dispatchability from the research branch, confirmed on the host.
- **Owner approval** of the dispatch (§A.43 item 4).

No required finding remains open.

## R11: `b3w_selftest` (`pe01/shard.py`, called from `shard_controls`)

- **Independent of the code it checks.**
  - The reference counts patterns directly from the synthetic records and enumerates every test A ⊆ {0,1}^w in pure
    Python, in the integer form |2^w Σ_{z∈A} c(z) − |A|·M|.
  - It shares nothing with `b3_window_k0`: no `window_marginals`, no sign patterns, no off-support closed form.
- **Non-vacuous.**
  - The families have 3–6 members, so the Gray walk makes 2–5 flip coordinates. With 4–8 seeds, supports are small, and
    the check requires at least one case with empty patterns (`active_out > 0`).
  - It is deterministically seeded and takes 5.1 s locally.
- **Mutants re-run from my own harness** (`mine/mutants2.py`, kind `b3wself`, which calls `S.b3w_selftest` on a mutated
  copy):

| Mutant | Outcome |
|---|---|
| BASE (unmodified copy) | green |
| B3W-gray-flip | caught: K0 fails, case 0 w = 2 gives 1/4 against 1/3, plus further cases |
| B3W-outside-dropped | caught: K0 fails, case 6 w = 3 gives 13/50 against 67/200 |
| AR-Kcx-upper-median | caught (AR) |
| WIN-strict | caught (IM3 windows) |
| SIGN-as-abs | caught (IM3 signed windows) |
| CX-d-last-only (retargeted string) | caught, on its own conditions under both readings |

- These match the implementer's reported values. Both former survivors are now killed cleanly, on the right
  checkpoint.

## N13–N16

- **N13: empty input gives INCOMPLETE, and `verdict.json` is written.** Run on an empty directory:
  - collect gives `status incomplete`, and the CX self-test is recorded as "not evaluated", not failed;
  - `verdict.py` writes `verdict.json` with class `INCOMPLETE`, exit 0;
  - `limitation()` is guarded.
- **N14 (a): an m = 3 shard missing its replay marks only its own cells.**
  - I relabelled the smoke shards as result mode, added replay records for all of them, and added a stand-in
    `n3-clk-m3` with none.
  - Collect sets that shard to `incomplete` ("no replay record") and adds no RP entry to `unevaluated`. It removes the
    shard from `horizons`, `windows`, `shard_info` and `witnesses`.
  - Its controls are still counted, so a failure there would still VOID the stage. This matches A1.
- **N14 (b): partial output for m = 3.** `shard_m3` now calls `progress()` after the exhaustive composites, after the
  sweep and witnesses, and at the end.
- **N14 (c): a job that fails before the shard step is "not run".**
  - The incomplete step runs only if `steps.shard.outcome` is neither `skipped` nor empty, so a failure at `pip install`
    leaves no file, and collect reports "not run".
  - The upload is now `if-no-files-found: warn`, so the empty artifact does not fail the job. Its replay job then fails
    on the missing artifact. That is harmless: the shard is not in the collected data, so no RP is required for it.
  - Checked by reading the workflow; no workflow was run.
- **N15.** The L2 limitation is stated in `pending.py`'s TAG-L text, which suits A2's wording.
- **N16.** The verdict now prints one line per K, with the readings each witness was found under. Every candidate at
  each K still enters the COUNTEREXAMPLE test and the attribution, so no counterexample can be hidden by deduplication.

## Remaining nits (none blocks dispatch)

- **N17. `verdict.py` maps any exception in `generate` to INCOMPLETE.** That includes a read-side EX3 float
  detection, which would more precisely be VOID (EX3).
  - It is unreachable in practice: collect writes `measurements.json` through `canonical()`, which refuses floats.
  - The marker fails on either class.
  - Consider letting `ValueError("EX3…")` produce `VOID: failed checkpoint(s): EX3`.
- **N18. `b3w_selftest` covers w ≤ 4 only.** It cannot do more, since the reference enumerates all tests. My offline
  meet-in-the-middle check at w = 5 (Addendum 1) covers the w ≥ 5 path for |𝔉| = 2. The sign-pattern code does not
  depend on w, so this is sufficient.
