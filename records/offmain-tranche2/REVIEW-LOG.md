# Off-main tranche 2: review log (2026-10-17)

Branch `local/h7-not-on-main` in the session worktree. The approved SHA `e01b3cc3879ab47731af25325c897fd51375f157`
was pushed to `wip/offmain-tranche1-20261017` and opened as draft PR #856 against main, for CI only. Base: main
`49ba3297`.

## Commits
| commit | content |
| --- | --- |
| `a3020cf0` | tranche 2: retained off-main objects, `check_objects.py`, gate wiring |
| `bb01edfe` | self-test memo (scan verdicts by content digest; base-history lookups); full failure lists identical across all 24 cases, self-test 276 s → 70 s (reviewer's sequential timing) |
| `6e02e46e` | H7: nothing retained, withheld or missing is reachable from the base |
| `8af1eb47` | withhold the three raw outputs under `1f19a347` |
| `eaa7f4c4` | archive-relative H4, H0 exit-code checks, cases for O3/H1/H2/H4 |
| `83fad8fa` | README, AGENTS §A.42 and release-gate description |
| `945a72a1` | inclusion-proof withheld lists, O9, six cases. **This checkpoint fails its own checker**: O9 rejects two withheld entries (`3a61f0ca`, `de2e4b29`) whose paths include an `a42-support` branch path |
| `0c12c520` | fixes that failure: withheld paths restricted to this archive's commits |
| `84e5b678` | file-type rule for withholding, exact withheld paths, O9 under inclusion paths only, H0 case, README on empty files |
| `e01b3cc3` | `APPROVED_WITHHELD` in the checker: the withheld set must equal the approved 28 entries (22 raw logs and .out output, 3 raw outputs, 3 build PDFs), each non-empty |

Intermediate commits are kept as they are. Acceptance is assessed at the final reviewed SHA only; an intermediate
commit is not claimed to pass.

## Reviews
| reviewed SHA | verdict | main findings |
| --- | --- | --- |
| `bb01edfe` | CHANGES-NEEDED | H4 depended on the clone's objects and failed with all host branches (CI's checkout); four rules without cases; unchecked git exits; README counts |
| `83fad8fa` | CHANGES-NEEDED | blobs withheld under inclusion paths unchecked; withheld metadata unchecked; descriptions and rule citation |
| `0c12c520` | CHANGES-NEEDED | README on committed empty `.err`/`.log` files; relabelling with the list edited to match |
| `e01b3cc3` | APPROVE | three stored blobs could be relabelled withheld at `84e5b678`, fixed here; nits: no self-test case for two O9 branches, the zero-size rule reads the unchecked recorded size |

Review files: session scratchpad `s1017/review-*/REVIEW.md`.

## Local evidence at `e01b3cc3` (main-only clone and a clone with all 151 host branches)
`check_objects.py` tree, `--reconstitute` and `--self-test` (43 cases) OK; `check_retention.py --gate` HOLDS;
legacy records 303 intact; 48 receipts hold. Lean and the full release gate run in CI (§A.40).
