# Tranche-2 inventory: final reconciliation

**Owner decision, 2026-10-17: INV-ACCEPTED-WITH-NOTES**, as the baseline for R2 planning and preservation priority. Accepted counts: 840 citations at 684 locations under the original rule; 437 rule-R run ids; 49 further direct runs (40 outside the rule, 9 range-cited); 1 job-only run; 487 runs in all; 99 covered by R1; 388 without an R1 entry. The 107 bundle heads are distinct from the 116 recoverable commits, which add the 9 range ancestors. The acceptance confirms the reconciliation for planning; it does not certify that raw logs are durably archived or that the bundles have passed an independent off-platform restoration.

Inventory: `tranche2-inventory-20261016.zip` (sha256 `9ed4140e01c5620d5e4071b6e4f5b523c6df716b2c76b9189723600330c07115`).
Independent validation: a second, separate validator (2026-10-17) found ACCEPT-WITH-NOTES, its notes applied here; before it, three rounds by the first validator, each recomputing everything from primary sources with the validator's own
scripts (not the builder's). Round 1: NOT VALIDATED (2 blockers). Round 2: NOT VALIDATED (2 blockers). Round 3:
**INVENTORY-VALIDATED**, no blockers. Host refs re-read at 21:04:42Z on 2026-10-16; all states recomputed from them.

## 1. Run ids the audit rule missed

The audit rule R (`offmain_audit.py`) counts an id only on a line containing `run`, `job` or `actions/`.

| Set | Count | How found | Validator |
| --- | --- | --- | --- |
| Rule-R runs | 437 | rule R at `fc5abade`, two hex-fragment matches of `38704428404` excluded | recount 840 citations / 684 locations / 437 runs / 173 jobs |
| Runs cited only on lines rule R skips | 40 | rule R's id shapes on lines failing its context test; ids inside a longer alphanumeric token or after a decimal point excluded | same 40 runs, cited 43 times at 41 locations (with the jobs' and further lines, 48 citations at 46 locations); no false positives; 141 excluded candidates are all hex fragments or decimal fractions |
| Further citing lines of rule-R runs | 21 lines | same scan | each row carries them; 4 runs move B → A |
| Jobs cited only on lines rule R skips | 4 | same scan; each confirmed with `get_workflow_job` | 109580668417, 112644271831, 112786500703, 112928987529 |
| Further citing line of a rule-R job | 1 | same scan | job 114538184326, `round-oi-channel-1-audit/preregistration.md:129` |
| Runs cited only as a range | 9 | `act-40 preregistration.md:744`, "36430858292 … 36450535104 — eleven design iterations"; inner runs = listed runs strictly between, on the endpoints' branch | the only range in the corpus (159 same-line id pairs examined); the 11 commits on the ancestry path match "eleven" |
| Any other form | 0 | substring search of every listed run id in all 1,371 files, PDFs' text included | 909 occurrences, all under rule R (840) or the extra scan (69) |

The audit's own figures stay as recorded (historical 842 / 438 / 173; corrected 840 / 684 / 437 / 173). The extra
runs and jobs are inventoried separately and labelled by how they were found (`cited_by`).

## 2. Source commits reachable from no ref on the host

| | Count |
| --- | --- |
| Heads of cited runs reachable from no branch, tag or pull head ref | **116** |
| — held as refs in the 84-commit bundle (`eee429d1…0ebd`) | 84 |
| — held as refs in the 23-commit supplement (`52e0a9f4…f0be`) | 23 |
| — held as ancestors, not refs (the act-40 range commits; inside both bundles: of 5eec100c in the supplement and of 7dacbc0f in the 84-commit bundle) | 9 |

Validator: both bundles match their manifests' size and sha256; their heads are disjoint and their union is the 107
bundle heads; all 116 commits are present after restoring both bundles into a scratch repository seeded only with
`main`; connectivity clean. The host served each of the 116 by sha on 2026-10-16 (fetched by sha, or confirmed with
`get_commit`, or an ancestor of such a commit); `fetch-by-sha.json` records which.

The off-main survey, covering every hex token on `main` (not only run heads), found 13 more commits and 6 blobs in
the same condition; they are in a third package (`cited-unreferenced-13c-6b-20261016.zip`,
`fdd69e0a0b753e85eca2f8d75736d9fb5a2960b5784308902f842d3fdd1f37a3`), restored and checked the same way.

## 3. The two job-only runs (tier J)

Round 1 found two runs reached only through a cited job, both with their logs not checked.

| Job | Run | Resolution | Final tier |
| --- | --- | --- | --- |
| 111566436954 | 37246891509 | logs checked: available; no direct citation of the run anywhere | **J** (job-only) |
| 114739543132 | 38227812539 | logs checked: available; the run is cited directly at `round-oi-finite-protocol-1/preregistration.md:204`, on a line rule R skips | **B** (outside-rule-R) |

## 4. Final figures

| | |
| --- | --- |
| Runs | 487 = 437 rule-R + 40 outside rule R + 9 range-only + 1 job-only |
| Jobs | 177 = 173 rule-R + 4 outside rule R; all map to a listed run with matching head_sha |
| Runs with an R1 entry | 99 (96 `ci-` entries + 3 BG-3-only); raw log bytes for 4 |
| Runs with no R1 entry | 388: tier A 200, tier B 187, tier J 1 |
| — of them cited directly | 387: tier A 200, tier B 187 (the 378 non-range: A 200, B 178; the 9 range runs: B); the inventory's `uncovered_cited_runs` |
| — reached only through a cited job | 1: run 37246891509 (tier J, branch-only, logs available) |
| Tier rule | the highest-ranking citing line decides; every known citing line counts (one run, 38534906783, differs from the older "cited only in" wording: B rather than C) |
| Logs | all 487 served on 2026-10-16; availability, not preservation |
| Directly cited runs with no R1 entry, by commit | on-main 169, host-unreferenced 116, branch-only 92, pull-ref-only 10; none tag-only (with the job-only run, branch-only 93) |
| All runs by commit | on-main 266, host-unreferenced 116, branch-only 95, pull-ref-only 10 |
| Retention | not readable; lower bound 52 days (the 2026-08-25 run's logs were served on 2026-10-16) |

## Notes carried from the validator (none blocking)

- Two host refs moved after `host-refs.txt` was read (the LOC-1 draft branch and `pull/853/head`, 273c1515 → fd5b3d4d); recomputed states are unchanged.
- The supplement bundle's own manifest lists its 23 heads; that it also holds the 9 range commits is recorded in `fetch-by-sha.json`.
- `cited_job_names` in the runs CSV is ordered differently from the JSON's `cited_jobs` in a few rows; same sets.
