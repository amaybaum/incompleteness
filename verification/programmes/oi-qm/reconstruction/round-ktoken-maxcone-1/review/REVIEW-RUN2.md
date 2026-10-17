# KTOKEN-MAXCONE-1 (#829): run 2 for owner review

Prepared 2026-10-17, local only. Nothing has been pushed or dispatched, and PR #829's branch has not been touched.

**Run 2 is ready to dispatch:** local branch `dev-equivalence/ktoken-maxcone-r2`, commit
**`1a3439c9eb84e000730618cdb3194ad8d26975c9`** (tree `1b96d583`), one commit on top of run 1's `1ab0fd9d`.

Pushing that branch keeps the commit id. Dispatching `verify.yml` on it gives the run-2 head SHA above.

Files in this folder:
- `controls.py`: a copy of the committed file;
- `preregistration.md`: the full revised draft;
- `preregistration.diff`: the diff against the PR's file at `625f853f`;
- `controls-selftest.txt`, `sim-check.txt`, `sim-verdict.txt`, `gate.txt`: local results;
- `tree/`: the worktree.

## (a) What changed after run 1, and why

Run 1 was dispatch run 39043849411 on `1ab0fd9d`. The host shows conclusion success, 38 of 38 jobs green, the
Mathlib bridge's Build, Release gate and A3 steps green with `A3-CHECK-NONVACUOUS: 13 cases as expected`, and the probe
shard printing `VERDICT KTOKEN-K3-EXACT`.
- **Settled by run 1.** It settled what run 1 could settle: the port builds as an adopted module, the scoped instances
  work, the A3 meta check compiles and its mutation cases behave, and the probe replays in CI.
- **Nothing in the module, the probe or the A3 files changed.** Their blobs are run 1's, and the preregistration now
  freezes them.

Run 2 adds three things.
1. **`controls.py`**, the round's static controls, in the style of BG-2's latest native round: `--self-test`,
   `check E --freeze F`, and `verdict E --freeze F --axioms LOG`. Its expected values come from two sources:
   - **The preregistration:**
     - the statement surface and hypotheses H1/H2/A from the original draft;
     - the list of S1 mutations, the S4 phrases and the four decision cells.
   - **What run 1 compiled:**
     - the surface as compiled, which differs from the draft only in name qualification, the written-out effect type,
       the `cycEquiv` coercion and implicit binders;
     - the 68 prints in order;
     - the probe's N = 3196, measured locally and byte-identical across replays; run 1 showed its final lines;
     - the census family;
     - the exact workflow, import and census edits.

   None of these values was tuned to make a check pass. The live workflow, import and census edits were compared with
   `D`'s files by the splice functions: all three equal.
2. **One workflow line pair:** the shard now also runs `controls.py --self-test`, as every landed native round's shard
   does.
3. **The revised preregistration**, re-cut at `D` = `b96662e6`. Every edit listed in STATE §6 is applied:
   - `D`, the ROADMAP lines (:1011–1019 and :1011–1014) and the import position (after :269);
   - `import OIBridge.EqvK2Generation`;
   - the compiled proof route: `sign_induction` with CNOT conjugation, `su_euler` branchwise, no Gray schedule;
   - Q-PAIR, now resting on S1's textual identity plus check A3 (the W1 step) and the absence line in the build log;
   - S2 extended to the objects actually used; S3 extended to siblings and the `#eval`;
   - new controls W, I, J, C2, P, R and T;
   - §A.42 retention rows, with the two pins pending;
   - an invariant→checkpoint table with twelve rows (§A.41).

## (b) Each control or check, its expected result in run 2, and what a deviation means

| Job / step | Expected in run 2 | A deviation means |
|---|---|---|
| `kernel` | success | an environment fault; it says nothing about the round |
| `bridge` › Build | success; the KTokenMaxCone blob is identical to run 1's | Run 1 built the same blob, so a red here is an environment or cache fault. Re-check the exact-head log before reading anything into it |
| `bridge` › Release gate | `release gate: PASS`, all 22 steps, including `lean-axioms` and `evidence-retention` | Locally, 21 of 22 pass on `1a3439c9` (`lean-axioms` needs Lean). A new failure would come from the added `controls.py`/preregistration (e.g. a voice/claims tool reading the record directory). That is a control-plane defect to fix before `F` |
| `bridge` › A3 step | success, with `A3-CHECK-NONVACUOUS: 13 cases as expected` | Same blobs as run 1, so red = environment fault. Should A3 regress anyway, the fallback is A1, never A2 |
| `probes_ktokenmaxcone1` › probe `--self-test` | 14 PASS codes, `checks: 3196, failures: 0`, 5/5 rejected, `VERDICT KTOKEN-K3-EXACT` | same blob as run 1; red = platform fault |
| `probes_ktokenmaxcone1` › `controls.py --self-test` | `controls: OK (0 failure(s))`, 35 PASS lines. Locally identical (`controls-selftest.txt`) | **The one genuinely new measurement in run 2.** Red = a defect in `controls.py`, or a CI-checkout difference: it reads only round-owned files plus `EqvK2MaxCone.lean`. Fix before `F`. No proof is affected |
| other probe shards, A42 shards, aggregate | success | unrelated; the 15 A42 exclusion shards cost about 6 CPU-hours on dispatch |

### What CI does not run, and was exercised locally

`check` and `verdict` need `F` and `E`, so I ran them on a simulated local chain: `D` → `F'` (preregistration) →
`C1` (`controls.py`) → `S1` → `E'`, with a stub result note. The simulation was deleted afterwards.

| Control | Result |
|---|---|
| C1, C2, S1–S4, W, I, J, G, T | PASS |
| **P** and **R** | **FAIL**: the two §A.42 evidence pins are pending and the files are absent. This is exactly the designed behaviour: `F` cannot be designated with a pending pin |

`verdict` on that chain with a **synthetic** axiom log (not a real run) printed all four positive tokens. That run was
made before a fix: `KTOKEN-MAXCONE-1-READ` is now printed only when every static control passes, as the preregistration
says. The fix was re-tested by `--self-test` but not by a re-run of the simulated `verdict`. The synthetic tokens
establish nothing about the theorem; they only exercise the code.

## (c) Acceptance criteria for run 2 (preregistered decision rule)

**PREDICTED-TREE-GREEN** requires all of the following on the dispatch at exactly `1a3439c9`:
1. every job concludes `success`, including the aggregate and all 15 A42 exclusion shards;
2. the bridge job's gate prints `release gate: PASS`;
3. the A3 step's final line is `A3-CHECK-NONVACUOUS: 13 cases as expected`;
4. the probe step prints `VERDICT KTOKEN-K3-EXACT` with `checks: 3196, failures: 0` and `mutations: 5 rejected, 0
   accepted`;
5. the `controls.py --self-test` step prints `controls: OK (0 failure(s))`.

Run 2 is **void** for the freeze if any of these happens:
- the run is not at exactly `1a3439c9`;
- any job is red, cancelled or skipped other than as designed;
- any of the five lines above is missing.

A red in an untouched shard voids the run as evidence, though not the design. With the two-run cap reached, a re-run
needs a new owner allowance.

Run 2 does **not** test:
- P and R, which need the retained evidence;
- S4 on a result note;
- `check`/`verdict` at the real `F`/`E`;
- `F`'s or `E`'s exact-head attestations.

Those stay with the round (preregistration, *Design evidence* and the invariants table).

## (d) Run 2's tree, exactly

`git diff --stat b96662e6 1a3439c9` touches 9 files, with 4664 insertions and 1 deletion. This is the predicted
execution tree less the result note **and less the §A.42 evidence files**, which cannot be produced before the logs are
retrieved. Nothing in it is disposable.

| Path | Note |
|---|---|
| `verification/lean-mathlib/OIBridge/KTokenMaxCone.lean` | blob `14bb9fc0`, frozen |
| `verification/lean/ktoken_maxcone1_probe.py` | blob `04580c51`, frozen |
| `round-ktoken-maxcone-1/checks/KTokenPairCheck.lean` | blob `354bd7ce`, frozen |
| `round-ktoken-maxcone-1/checks/run_checks.py` | blob `dc6c77d1`, frozen |
| `round-ktoken-maxcone-1/controls.py` | blob `ea052f2d`, frozen |
| `round-ktoken-maxcone-1/preregistration.md` | the `F` candidate's text, pins pending |
| `.github/workflows/verify.yml` | six splices, checked by W |
| `verification/lean-mathlib/OIBridge.lean` | +1 line |
| `verification/lean-manuscript-census.json` | +1 family |

**The W1 step stays.** It is part of the round's frozen control:
- the preregistration names it (Q-PAIR rule, invariants row 4);
- `controls.py` W requires it, exactly as spliced, at `E`;
- removing it at `E` would fail W.

The `if: ${{ !cancelled() }}` line is frozen with it. Dropping that line is an owner choice, and must be made **before**
run 2, because it changes `verify.yml`, the W splice and the `controls.py` blob.

**Predicted SHA.** It is `1a3439c9eb84e000730618cdb3194ad8d26975c9`, since the commit already exists locally and
pushing keeps it. The actual `E` will differ, because it is built as `F` → stage 1 → stage 2 → stage 3 with the
evidence files. C2 and W, I, J check that `E`'s content equals what run 2 exercises.

## (e) Owner decisions before F

1. **Approve the push of `dev-equivalence/ktoken-maxcone-r2` and the run-2 dispatch.** This is the second and last
   design run under the cap.
2. **Retained evidence (§A.42).** The run-1 log (jobs 117428550018 and 117428550439) and the run-2 log must be turned
   into the expected-result files `evidence/run1-39043849411.json` and `evidence/run2.json`, and pinned by sha256 in the
   preregistration before `F`.
   - The logs can be retrieved only through the browser or the evidence-retention archiver (`reproduce evidence`
     workflow). The built-in API client cannot fetch them, so someone with that access has to do this.
   - The pins are `pending` today, and `controls.py check` fails P/R until they are filled.
3. **Keep or drop `if: ${{ !cancelled() }}`** on the A3 step (before run 2; see (d)).
4. **The new drafting PR.** PR #829's branch is at `D = dee3b5ae`. Re-cutting at `b96662e6` needs a new drafting PR, or
   a reset of that branch: your action. The revised preregistration and its diff are here for that.
5. **Landing order against #821–#825** (STATE §4). They all splice after the same import, census tail and aggregate
   lines. Whichever lands first changes `D`'s anchors for the others; W/I/J are anchored on text, not line numbers, so
   they survive if the anchors stay unique.
6. **Port scope** (three modules; FiniteWalsh/FiniteCircuit left out) and **the scoped instance**: confirm, or say so
   before `F`.
7. **`F` designation:** after run 2 is green and the pins are filled, on the exact-head `check-run` of `F` (§A.39).
