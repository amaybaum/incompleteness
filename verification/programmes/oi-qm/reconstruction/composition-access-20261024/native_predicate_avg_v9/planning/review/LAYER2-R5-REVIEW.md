*Recorded by the coordinator from the independent reviewer's report, because the reviewer's tool refused report files.*

# NP-AVG-1 Stage 0 Layer 2 r5: independent review

**Reviewed object:** `6ceedd82`, on top of `bc042a61`, PR #935. The review was read-only. Nothing ran on v8's configuration class. My probes used analogue regions ball(1), (2), (3), (5) and (6), and the design profile `mid`, whose key (3, 6, (0, 0, −2)) is not v8's.

**Verdict: ACCEPT WITH CHANGES.** The review is incomplete only where §9 says so.

## 1. r4 items and replay
- **Frozen files and retained evidence.**
  - Since 4a4d8bc1, only `layer2/**`, README, SHA256SUMS and new `review/` files changed.
  - `review/LAYER2-R4-REVIEW.md` is byte-identical to my delivered text.
  - All of SHA256SUMS verifies.
  - The 356 files of the replay copy match the blobs of 6ceedd82.
- **Replay** of `l2run.py design` on that copy, verified:
  - self-test 40/40;
  - quick mutants 61/61;
  - the 58-count cross-check passes;
  - the E1-check replay is byte-identical;
  - `crosscheck`, `refusal_probe_v8` and `dryrun_v8_plan_no_closure` are byte-identical to the committed outputs;
  - `certificate_toy` exits 2, the expected failure because the scratch copy is not a git repository;
  - `subdivision_bounds` and `midsize_validation` exit 0.
  - **Not verified:**
    - `subdivision_bounds.out` differs from the committed copy. The likely cause is recalibrated timing, but I did not check it.
    - Whether the last steps (calibration repeats, overhead, survivor-cap measure and derive, CI local check) completed: the session ended before the log reached them.
- **K1 and L-b.** `launch_decision` compares every per-shard estimate, and M_launch_mean_shard is killed. Applied. One caveat: `per_shard_jobs` splits the shared terms by modelled closure weight. The mid validation shows real spread far above the model's (§3), so on a contiguous plan the per-job check stays model-optimistic.
- **K2, K3, B1–B4.** Applied. The affordable κ is stated separately and labelled "never a candidate"; the stale 1.18 is gone; the measured / modelled / judged labels are in place.
- **L-a.** The rounding case 1.21 → 1.3 is tested, and M_kappa_round_nearest is killed.
- **CI items:** see §7. **A1–A4:** applied as design text. A3 and A4 are measured on mid; A3 shows 0 disagreements on 1,940 records.

## 2. The owner's decisions
- **Ceiling and scope.** The ceiling is per campaign, over the six owner-named components, and every ledger entry counts whatever its status: failed, cancelled and timed-out jobs, and retries (attempt > 1). L2-LEDGER covers this and M_ledger_skip_failed is killed. The retry allowance is an `OWNER` placeholder, and while it is open, startup and the decision refuse. Faithful.
- **Changes needed:**
  - **(G-1) Define `compute_seconds`.** It should be the host-recorded job duration. If it is, the planned `execution_overhead` must be dropped for jobs already ledgered; otherwise their overhead is counted twice.
  - **(G-2) κ applied to measured time.** `campaign_decision` multiplies measured time by κ as well as planned time. That is stricter than the owner's wording. It is safe, but it is a reading, so the owner should confirm it.
  - **(G-3) The campaign's start point.** It is not stated. Do local design runs count, or does the campaign start with the first CI calibration? The owner should confirm.
  - **(G-4) Calibration launches.** The config says `launches: 1`, while the CI proposal proposes two.

## 3. Subdivision
- **Correctness and exact accounting: correct.**
  - Cuts fall at representative rank ⌊kR/S⌋, so the shards are contiguous and cover 0 to N exactly.
  - The plan's representative counts come from the site-pair counts.
  - `l2cert` item 7 refuses a plan of another kind or one with failed accounting.
  - `l2merge` refuses a shard whose canonical representative count differs from the plan's. That is a run-time check of the v8 count file on v8.
  - Any cut gives an exact cover, so the count file affects only balance, never correctness.
- **Reproducibility.** The plan is a pure function of region, slices, group and S, through the count file. Reproducible.
- **Canonical-image check: complete.** Group elements never change slices, so representative membership depends only on the order of t1 and t2. The slice pairs (0,0), (0,1), (1,0) and (2,1) cover t1 = t2, t1 < t2 and t1 > t2, so checking them on every site pair is complete.
  - My brute force, written independently and testing every slice pair, agrees with `l2sitepairs.count` pair by pair on ball(1), (2) and (3) at nt = 25, on ball(5) at nt = 4 (10 strict pairs) and on ball(6) at nt = 3 (20 strict pairs). Those radii bracket v8's ball(4) without touching it.
- **Drop and duplicate mutants.** They perturb `plan_from_cuts` and are killed by the accounting check at L2-SPLIT. L2-SPLIT's own once-per-record scan check would also catch a drop or duplicate at the scan level. Adequate.
- **Cost balance without v8 measurements: yes, by interleaving instead of weighting.** Assign the representative of rank q to shard q mod S. This needs no model; accounting stays exact by rank, and each shard verifies canon(r) = r for its ranks. My probe on mid (S = 128, normal mode, every gate at v8's rates, same machine):

  | plan | shard times |
  | --- | --- |
  | contiguous r5 subdivision | 8.5 s and 139.4 s |
  | interleaved | 52.2, 54.8, 53.4 and 50.7 s |

  - Interleaved, heaviest over mean is 1.04, and 0 of 1,301 ranks failed the canonical check.
  - Model-weighted cuts (r5's lever (i′)) cannot do this: the model ranked mid's shards wrongly.
  - **Recommend adopting interleaving.** It needs a merge check that the orbit sizes sum to N and every rank is covered, and the site-pair count, which `index_of_rank` uses on v8.

## 4. Survivor cap
- **The derivation is sound as mathematics.** P(some shard holds more than ⌊c/b⌋ of ⌈X/b⌉ uniform clusters) is exact, the partial cluster is treated conservatively, and my approximate check of X = 64, b = 8, c = 16 (≈ 0.05) matches the table's 0.048.
- **b is the weak point under contiguous shards.** A contiguous shard holds the pairs (i, j) of one or a few first sites. Survivors that share a site would land together, so the per-shard concentration could exceed any stated b.
- **Under interleaving, b ≈ 1 is credible.** Ranks scatter geometric clusters across shards.
- **Recommend c = 16 with interleaving.** P is about 3e-10 at X = 64, b = 1, and 3e-3 even at b = 4. An expected-cost comparison also favours 16 over 24 at plausible X: 24 costs 6,112 s more for a small drop in rerun risk.
- If contiguous shards are kept, use 24 (α = 1 %, X = 64, b = 8), or measure b on planted mid survivors.
- The scientific justification (exceeding the cap gives INCOMPLETE with the counts complete) is kept separate from these numbers. Good.

## 5. The count-only module (`l2sitepairs.py`): independent review against the owner's restrictions
- **Minimum metadata.** It uses dim, rho, tlast and port; n only for the v8 key. It forms no records, and its output depends only on the index-space geometry, not on the rule, n, sources, frame or any context. It therefore cannot carry outcome information. Holds.
- **No survivor evaluation, estimation or experimental computation.** Imports are restricted, and the audit hook refuses imports, opens other than the one output write, subprocesses, sockets, ctypes and file removal. Holds.
- **No persistence.** The output is validated to exactly the permitted keys and types, and exceptions report only their class name. Holds.
- **Algorithm and outputs published.** They are in the docstring and `SITE-PAIR-COUNT.md`. I verified the in-pair rule by hand and by brute force (§3). Holds.
- **Authorization.** It has its own scope, schema and designation line. It binds the commit, the module SHA-256, a clean Layer-2 tree and the host's owner check. It is disjoint from `l2auth`'s.
- **Guard gaps.** Besides fd 1, `sys.__stdout__`/`sys.__stderr__` and `_Sealed.real` also bypass the sealed streams. **The pinned-module basis is sufficient.** The designation names the module digest and the commit, which pins `l2config` too, so any edited module is refused. The runtime guard is defense in depth; state the extra bypasses in the gap note.
- **Changes before authorization:**
  - **(SP-1)** Add an in-module second count: explicit canonical images at the three order classes per site pair, with any disagreement VOID. Burnside's equality did not catch the drafter's own bug on ball(3), so the v8 output otherwise has no per-pair cross-check until the merge.
  - **(SP-2)** Make `validate` require each pair count ∈ {0, nt(nt−1)/2, nt(nt+1)/2, nt²}, each single ∈ {0, nt}, and N to equal its formula. This closes the integer channel.
  - **(SP-3)** Run it twice, with and without `-O`, and require byte-identical outputs. Record the commit with the output, and retain the file under §A.42 before use.
- **Resource limit to put to the owner:**
  - one process: `python3 -I -B code/l2sitepairs.py --profile v8 …`;
  - at the named commit and module SHA-256;
  - RLIMIT_CPU 60 s and RLIMIT_AS 1 GiB, set by the module;
  - a 5-minute job timeout if run in CI;
  - about 40 kB of output;
  - expected time under 1 s (measured ≤ 0.01 s on ball(3), 0.7 s for a full brute force on ball(6));
  - charged to the campaign ledger.

## 6. Feasibility
- **Under the model, the conclusion is arithmetically sound:** 31 % over at κ 1.3 before C7 sets 2–3, and the per-job limit fails at κ 1 with cap 16. But the model is not the reality.
- **My unbiased interleaved sample on mid measures the model's total error.**
  - The mean actual time is 52.8 s per shard (single copy), against the model's 108 s, so ρ ≈ 0.49.
  - C7 per-record work is 89 % of actual time (48.8 of 54.8 s in shard 37; 610 set-2 F_G records). That is about 0.080 s per F_G record per copy, against the model's 0.15.
- **v8 projection** (F_G ≈ 40 % of N, as on toy and mid): C7 set 2 is about 2.07 M × 0.080 × 2 ≈ 331,000 s, about 4× the ceiling at κ = 1. Without set 2, the corrected known terms (≈ 0.49 × 84 k ≈ 41 k) plus cap 16 fit at κ 1.3, and per-job fits under interleaving (≈ 1,800 s against 2,400 s).
- **So the binding term is C7 set 2 on F_G, and nothing else.** "Infeasible on two counts" overstates it: the per-job failure is an artifact of contiguous shards plus the model.
- **Redesigns that keep the κ rule and the Layer-1 criteria:**
  1. interleaved assignment (§3);
  2. Lemma G-D in C7's set-2 reference (lever iii; the owner approved it conditionally), with the E1 §9 cross-check — the only lever that addresses the binding term;
  3. D4(b), engineering the overhead.

  Excluded under these constraints: sampling `-O`, more shards (S7), D3 (it narrows the claim), lowering κ and raising timeouts.
- **Decisive next measurement (non-v8):** on mid, a preregistered sample of interleaved shards, or all 128 in CI, with per-term timers (closures, gates, C7 sets 1–4), run once with the full set-2 reference and once with a G-D-reduced prototype. That gives per-term ρ and the size of G-D's saving.
- **On v8,** the only remaining unknown is then |F_G|: the population-count amendment, which needs the owner's authorization.

## 7. CI calibration
- **Fixed:**
  - the self-pin is removed;
  - the three pins match the files;
  - all four action SHAs match their tags by `git ls-remote`;
  - 3.13.16 is in the versions manifest for 24.04 x64;
  - u_cal is preregistered: a one-sided 95 % bound, Wilson–Hilferty checked (χ²₀.₀₅,₁₉ ≈ 10.11), on the v8-weighted known terms;
  - CPU model and wall clock are recorded;
  - `aggregate` runs under `always()`.
- **Still blocking:**
  - **(CI-8) Second launch.** A second launch is a second push, so a new SHA, but `postrun.py` requires every launch's head_sha to equal one authorized SHA. CI-6's two-launch design would therefore come out VOID. Accept per-launch authorized SHAs with an identical tree, or choose one launch.
  - **(CI-9) Pin postrun.** `postrun.py` (sha256 `d0741b35…`) holds the preregistered statistic but is not pinned. The authorization must name its digest, and the digests of `l2plan` and `l2config`, which it calls.
- **Note:** live main (02e73e56) has a new workflow, `pe01-bounded-tests.yml`. It is dispatch-only and does not fire, but the proposal's list should be regenerated at launch.
- **After CI-8 and CI-9, it is ready for the owner's pre-dispatch review.**

## 8. Required changes
G-1 to G-4; interleaved assignment (or record why not); cap 16 conditional on interleaving, or 24 otherwise; SP-1 to SP-3; CI-8 and CI-9; restate the feasibility conclusion with the measured ρ and C7 share.

## 9. Not verified (session ended)
- The tail of the replay log (calibration repeats, overhead, survivor-cap measure and derive, CI local check).
- Why `subdivision_bounds.out` differs.
- Line-by-line review of the L2-LEDGER and L2-COUNTONLY test bodies, and of `refusal_probe`'s forged-file case.
- A full read of `LAYER2-PLAN.md` r5.
