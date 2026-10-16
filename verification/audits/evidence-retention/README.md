# Evidence retention (AGENTS §A.42)

This archive retains, on `main`, evidence that records already frozen cite but that was held only off `main`: in a session scratchpad, or in CI logs that expire.

It is a governed audit record. It is not a research round and changes no historical result.

- **Frozen records stay unchanged.** No native-round record (`G13`), legacy record or receipt is edited. The manifest maps each citing `file:line` to its retained copy, and states which of the claims made there the copy carries.
- **No claim is affected.** Nothing here strengthens a claim, repairs a check, or changes what any record says it measured.
- **Retention is not verification.** `tools/v3_verifier.py`'s verdicts are unchanged, and no retained file is a host attestation.

## Tranche 1 (this commit)

| path | what | kind |
| --- | --- | --- |
| `bg3/*.log` | BG-3's four cited job logs: the bridge-log tails of jobs 116826161407 (`E`), 116805436638 and 116761232088 (design trees), and the design-run log of job 116831668411 | `complete-as-cited`: byte-identical to the digest each citing record names |
| `bg3/run-*.json` | the run metadata of the two design-tree runs, 38848873989 and 38834744516 | `derived` |
| `ci/<run>/run.json` | for each of the 96 runs below, the run's identity and outcome (`id`, `head_sha`, `event`, `conclusion`, `run_attempt`, …) | `derived`: selected fields of a saved runs-API listing page; `source_sha256` is that page |
| `ci/<run>/jobs.json` | for 57 of the runs, every job, with its name, attempt and conclusion | `derived`: selected fields of a saved jobs-API response; `source_sha256` is that response |
| `ci/<run>/bridge-excerpt.log` | from the run's Mathlib bridge job log: the release-gate block, the build status line, cache lines, any error or `sorry` marker, and the build lines and axiom reports of the round's own governed Lean modules, each wrapped report with its continuation lines | `excerpt`: exact lines of the served log; `line_ranges` are 1-based within it, and `served_sha256` is its digest |
| `build_archive.py`, `audit/` | the script that cut this tranche, and the off-`main` reference audit at `fc5abade` it acts on | `complete` |

**The 96 runs** are of two kinds:
- every check run that a receipt under `verification/receipts/` records as `F`'s or `E`'s `check-run` attestation (93 runs);
- the three runs CV-1's certificate attestation cites.

They span 2026-09-22 to 2026-10-16. The oldest are the first to reach GitHub's log-retention limit.

## How the logs were read

The job logs were read through the session's GitHub job-log tool. It returns at most the last 5000 lines of a log, together with the log's full length. Complete log archives could not be downloaded from that session, because its network policy blocks GitHub's archive host. Each excerpt is therefore an excerpt of the served text, and the manifest records the served text's line count, its digest and the log's full length.

**Lines are counted by splitting on newline characters.** The served texts end without a newline, so a 5000-line tail has 4999 newline characters, and `wc -l` reports 4999. The citing records count that way: their "last 4999 lines" is this archive's 5000.

The four BG-3 logs were re-served on 2026-10-16, after their records were written. Each re-served text was byte-identical to the archived file. The manifest records this under each entry's `replay`; it is an observation of the host, not something the tree can show.

## What each entry states

**`retains`** is a mechanical summary of a CI entry's files: the run's metadata, job counts per attempt, the release-gate block's steps and verdict, cache lines, and a marker count. For each of the round's governed modules it gives the source lines of the `#print axioms` commands at the attested commit, and the lines whose reports are in the excerpt. A module's status is one of:
- `complete`: every report is in the served lines;
- `partial` or `none`: some or none are;
- `absent`: the module is not in the tree at the attested commit, so the run has nothing to report for it.

Of the 164 module records, 84 are complete, 5 partial, 31 none and 44 absent. Each partial and none record is listed as a gap.

The `#print axioms` lines come from each module's source at the attested commit. That source is on `main` but not in this archive, so the checker can check each status against the recorded lines, while the lines themselves can be checked only with git history.

**`claims`**: for every citing location, the claims that record makes about the cited run or log. Each claim is a verbatim fragment of the citing file, on a stated line, with one of three statuses:
- `retained`: the archived files it names carry the claim;
- `not retained`: no archived file carries it;
- `differs`: the archived files show something else.

A note says what the files show where it is not plain. Tranche 1 annotates 752 claims at 172 citing locations: 686 retained, 66 not retained, none differing. The claims not retained are:
- mostly job counts for runs whose job list was not retained;
- outputs of other jobs, such as probe, guard and shard results;
- statements a log tail cannot establish, such as what was not rebuilt, or what happened before the served lines;
- job identities that the log bytes do not state.

The annotations were made from the archived files alone. They are a reading of those files, which a reviewer can repeat from the tree.

**`missing`**: the evidence items found absent:
- 39 job lists, which were served inline and not saved;
- the axiom reports of 36 module records, the 31 none and 5 partial ones, with counts;
- the run metadata of the BG-3 design run 38857340321.

## Checking

From the repository root:

```
python3 -I verification/audits/evidence-retention/check_retention.py
python3 -I verification/audits/evidence-retention/check_retention.py --self-test
python3 -I verification/audits/evidence-retention/check_retention.py --later-provenance
python3 -I verification/audits/evidence-retention/check_retention.py --gate
```

The check uses the tree alone: no git history, network or third-party package. Its rules (R1–R9, listed in its docstring) verify:
- every archived file's size and sha256, and the digest match of each `complete-as-cited` file;
- that each citing file has its recorded blob id, the cited line still holds its tokens, and each claim's text stands verbatim where it says;
- every excerpt's ranges against its line count and the served text;
- the absence of secret patterns, IP addresses and e-mail addresses in every file here;
- that no unlisted file sits in the archive;
- the manifest's form;
- that each CI entry's summary is what its files say;
- coverage, recomputed from the tree: every receipt under `verification/receipts/`, and every certificate attestation that cites runs, is covered by this tranche or named in the manifest's `coverage.later`; each of their check-run attestations and cited runs has an entry that matches it.

At `fc5abade` every receipt is covered and `coverage.later` is empty. A receipt that lands after this tranche keeps its own evidence in its record directory (§A.42), and the checker reports it until `coverage.later` names it with that directory. A path named there may be neither covered nor cited by this tranche.

The tree cannot order commits, so whether a path named as later really landed after this tranche is checked against git history. `--later-provenance` (R10) checks that the tranche base is an ancestor of HEAD, and that no path named as later existed at the base.

`--gate` is the release gate's `evidence-retention` step. It runs the check in history mode, where R9's scope is read from git rather than from the tree: every receipt, and every certificate attestation citing runs, that existed at `fc5abade` must be covered, nothing else may be, and a receipt landed later needs no declaration. It then runs the self-test, whose R10 cases need that history and fail without it. The Mathlib bridge job, which runs the gate, checks out the full history.

It prints the gaps and every claim not retained. The self-test mutates a copy once for each of the checker's failure messages, and requires that message.

**`build_archive.py` documents how the tranche was cut.** It cannot be re-run from the tree, because its inputs (the saved API responses and served logs) are not retained; their digests are. The checker, not the build script, is the reproducible part.

## Secrets and operational data

Every file here was scanned before commit for:
- token and key patterns, and key-file headers;
- signed-URL parameters;
- IP addresses;
- e-mail addresses.

There were no matches. The design log shows GitHub's own masked values (`token: ***`, `AUTHORIZATION: basic ***`). It also shows runner metadata that GitHub publishes for public runs: worker id, region, and the repository's branch list. The only URLs are public ones, including the public Mathlib cache. Nothing was redacted.

## Not yet retained

These are recorded here so the gap is visible, not resolved. Counts are from `audit/offmain_audit-output.txt`:
- **Commits not reachable from `main`:** 107, cited at 236 locations in native-round records and one in a mutable script.
- **Blobs and trees not reachable from `main`:** 75.
- **Other CI evidence:** 842 citations of 438 run ids and 173 job ids. This tranche retains run metadata for 98 runs, job lists for 57, excerpts of 96 bridge-job logs and BG-3's four logs. No log longer than 5000 lines is retained complete.
- **Act-26's scratchpad computation** (`result.md:931`), which the audit found saved nowhere.

Each needs a documented resolution in a later tranche: retained content, an excerpt, or a recorded gap.
