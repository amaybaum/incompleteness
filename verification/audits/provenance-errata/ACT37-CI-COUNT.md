# Act 37: forward note on the reported lean-axioms count

**Status:** provenance record, not a new scientific verdict. This note is a mutable dependent of the frozen Act-37 record; the native record and receipt are not edited (AGENTS.md §A.39, G13).

## What differs

- At `verification/programmes/oi-qm/track-b/act-37-arc-exclusivity/preregistration.md:64`, the frozen description of the pre-Act-37 base `D = d014bafef404b991b4544e6d2041edcfab1ac765` says that its push run **36373806246** reported **4,829** named results from `lean-axioms`.
- The archived structured result at `verification/audits/evidence-retention/runs/36373806246/expected.json`, in main's
  history at `48b18ac5`, records the same run, attempt 1, event `push` and head `d014bafe…`. Its `gate` output says `lean-axioms: PASS`, **4,803** named results, and reports no sorry. It also records 12 receipts and 303 legacy records.
- **Disposition: DIFFERS (4829 versus 4803).** This is a count/attribution discrepancy in the frozen prose, not evidence that the build failed, and not a change to Act 37's mathematical result. The frozen statement is retained verbatim as historical evidence, and neither count is replaced.
- **Recorded explanation.** 4829 − 4803 = 26, the number of `#print axioms` lines in `verification/lean-mathlib/OIBridge/DitaArcExclusivity.lean`, the module Act 37 adds. Runs whose tree contains the complete 26-theorem module report 4829 (stage 1, run 36379680840 at `94c2405f`, held 24 of them and reported 4827, `result.md`:169): the design run 36378121576 at `d79ac73c` (`preregistration.md`:1339) and stages 2 and 3 (`result.md`:170–171). Runs without it report 4803: the base `D`'s run 36373806246 (above) and F's own run 36379070237 at `8104323` (`verification/audits/evidence-retention/ci/36379070237/results.json`:84). So line 64 credits `D`'s run with the count of a tree that includes the Act-37 module.
- Line 64's count is the only differing claim among the base-run figures at lines 62–66; the archive records the probe durations stated there as not retained, not as differing.

## Evidence and reconstruction

The archived `expected.json` is the structured historical observation, not a raw log. Its `source` records the served log digest `bb153d18187f9c95b709c045b2051cc46d9da3e233d21a3a360d28e77f14047b`, along with a tail of 1,200 lines from a 12,683-line bridge log. Compare it with the frozen line and the run/job identities in `runs/36373806246/{run,jobs}.json`.

To re-check the build rather than merely read the archived observation, use a clean full-history checkout of `d014bafef404b991b4544e6d2041edcfab1ac765`, run that commit's Lean build and release gate, and compare the resulting gate output with the archived structured expectation according to its `reproduce.manual` recipe. An independent reviewer must check the commit, recipe and observed output before promoting any stronger conclusion.

## Scope and preservation

This note carries the 4829/4803 finding outside archive-manifest bookkeeping, so the finding does not depend on that bookkeeping surviving a future optional cleanup. The archive remains frozen pending separately authorized changes; nothing here authorizes pruning it. The Act-37 preregistration, result, frozen theorem statements, receipt and certified outcome `A37-EXCLUSIVITY-PROVED` are untouched. No new claim about a changed theorem count is made.
