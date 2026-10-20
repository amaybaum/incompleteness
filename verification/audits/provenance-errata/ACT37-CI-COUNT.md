# Act 37: forward note on the reported lean-axioms count

**Status:** provenance/count correction, not a new scientific verdict. This note is a mutable dependent of the frozen Act-37 record; the native record and receipt are not edited (AGENTS.md §A.39, G13).

## What differs

- At `verification/programmes/oi-qm/track-b/act-37-arc-exclusivity/preregistration.md:64`, the frozen description of the pre-Act-37 base `D = d014bafef404b991b4544e6d2041edcfab1ac765` says that its push run **36373806246** reported **4,829** named results from `lean-axioms`.
- The archived structured result at `verification/audits/evidence-retention/runs/36373806246/expected.json` records the same run, attempt 1, event `push` and head `d014bafe…`. Its `gate` output says `lean-axioms: PASS`, **4,803** named results, and reports no sorry. It also records 12 receipts and 303 legacy records.
- **Disposition: DIFFERS (4829 versus 4803).** This is a count/attribution discrepancy in the frozen prose, not evidence that the build failed, and not a change to Act 37's mathematical result. The frozen statement is retained verbatim as historical evidence. Do not silently replace either count or call this a reproduced check in this note.

## Evidence and reconstruction

The archived `expected.json` is the structured historical observation, not a raw log. Its `source` records the served log digest `bb153d18187f9c95b709c045b2051cc46d9da3e233d21a3a360d28e77f14047b`, along with a tail of 1,200 lines from a 12,683-line bridge log. Compare it with the frozen line and the run/job identities in `runs/36373806246/{run,jobs}.json`.

To re-check the build rather than merely read the archived observation, use a clean full-history checkout of `d014bafef404b991b4544e6d2041edcfab1ac765`, run that commit's Lean build and release gate, and compare the resulting gate output with the archived structured expectation according to its `reproduce.manual` recipe. An independent reviewer must check the commit, recipe and observed output before promoting any stronger conclusion.

## Scope and preservation

This note carries the 4829/4803 finding outside archive-manifest bookkeeping, so a future optional cleanup cannot erase its only current mention. The archive remains frozen pending separately authorized changes; nothing here authorizes pruning it. The Act-37 preregistration, result, frozen theorem statements, receipt and certified outcome `A37-EXCLUSIVITY-PROVED` are untouched. No new claim about a changed theorem count is made.
