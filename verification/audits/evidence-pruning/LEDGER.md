# Evidence-retention archive: removal ledger

The dependency and citation audit of the code and bookkeeping files of `verification/audits/evidence-retention/`, and
the removal it supports. Line references are to `main` at `55a0e80abc4b96e7bf211566a036ad17ea64a69e`, where the archive
is tree `480065e1dd778ccc4f6277d2074f2d5f1e2f1011`. Retained evidence data (`objects/` other than its manifest, `bg3/`,
`ci/`, `runs/`) is outside the audit and unchanged.

## Method

For each file: its manifest entry, kind and citation count; every reference to its name in the tracked tree
(workflows, `tools/`, the release gate, AGENTS.md, receipts, legacy and native records, the manifest, the object
manifest and the archive's own files); every retained result that names it as extractor or reproduction tool; and the
records of #829 at `e12c1573` and `e35fe099`, #831 at `65b85147` and #824 at `72db07ca`.

A file is **removable** when no check, workflow, retained result, record or recorded citation depends on it, and its
removal needs no manifest edit that changes a citation, claim or retained-file mapping. It is **required** when a
dependent is named below. No file is classified as redundant, and none is undetermined.

## Classification (bytes at `55a0e80a`)

| File | Bytes | Class | Dependents (file:line at the base) |
| --- | ---: | --- | --- |
| `build_tranche3.py` | 32,767 | removable | `manifest.json:14568` (file record of `tranche3-record`, `complete`, 0 citations); `README.md:182` (description); `build_priority_runs.py:8,258` (itself removable). No retained result names it: the tranche-3 results name `job_outputs.py` as extractor and tool. |
| `build_priority_runs.py` | 18,722 | removable | `manifest.json:14908` (sole file of `priority-runs-record`, `complete`, 0 citations); `README.md:182`. R12's priority-run pins (`check_retention.py:638-660`, `PRIORITY_ALLOWLIST`) bind the run entry and `decisions/`, not this script. |
| `build_research_runs.py` | 14,649 | removable | `manifest.json:14680` (sole file of `research-runs-record`, `complete`, 0 citations); `check_retention.py:315` names the entry id only to exempt it from R13; the clause is inert without the entry. Research results name `extract_result.py`. |
| `build_tranche4_objects.py` | 11,156 | removable | `manifest.json:14696` (sole file of `tranche4-record`, `complete`, 0 citations). What it wrote is pinned independently: tranche 4's 66 ids in `check_objects.py` (`TRANCHE_MEMBERS`), the withheld approvals in `APPROVED_WITHHELD`, and the controls and approval it carried in `objects/manifest.json:22137,22147,22417`. #829 cites the objects, not the script. |
| `build_archive.py` | 28,897 | required | `objects/manifest.json:9295,18909`: archive-self citations of `build_archive.py:285,282`, which `check_objects.py` O7 reads; `bg3/results-116831668411.json:49`: this retained result's extractor is its `design_results` filter; `ci/36228429141/re-extraction-fdf3ec80cdaa.json:25-26`: its recipe; `manifest.json:12528`. |
| `check_retention.py` | 199,808 | required | AGENTS §A.42, closing paragraph: the direct `--gate` check for records frozen under the section's earlier form, which #829 names; `.github/workflows/reproduce-evidence.yml:139`; `check_retention.py:182` (`FIXED`). |
| `check_objects.py` | 195,528 | required | loaded by `check_retention.py:176-179` and run at `:1582`; the only verifier of `objects/`; `manifest.json:12570`. |
| `manifest.json` | 555,580 | required (edited) | read by `check_retention.py:206`, `reproduce.py:238,332`, `job_outputs.py:297,496`; lines 750 and 991 cited by `objects/manifest.json` (O7). |
| `README.md` | 56,463 | required (edited) | line 53 cited twice by `objects/manifest.json` (O7); `check_retention.py:182` (`FIXED`). |
| `reproduce.py` | 24,505 | required | `reproduce-evidence.yml:93`; the `reproduce.tool` of the tranche-1 results; `manifest.json:12546`. |
| `compare_result.py` | 18,297 | required | `reproduce-evidence.yml:97`; the recipe of every tranche-1 and BG-3 result; #829 `evidence/*.json` recipes at `e35fe099`. |
| `extract_result.py` | 33,671 | required | the extractor of 102 retained results; run by `check_retention.py:1595` and loaded by `job_outputs.py:120`; #829 evidence recipes. |
| `job_outputs.py` | 32,458 | required | `reproduce-evidence.yml:152,156`; the extractor and tool of the tranche-3 results; `check_retention.py:1612`. |
| `open-claims.json` | 12,840 | required | R16, `check_retention.py:759` (`OPEN_CLAIMS_PIN`). |
| `audit/offmain_audit-output.txt` | 64,993 | required | 24 citing locations in `objects/manifest.json` (O7). |
| `audit/audit.md` | 6,994 | required | `objects/manifest.json:10449` (O7, `audit.md:60`). |
| `audit/offmain_audit.py` | 9,827 | required | the recipe of `offmain_audit-output.txt` (`audit/audit.md:7`), a retained result O7 cites. |
| `decisions/pr862-comment-6270971164.json` | 4,258 | required | R12 decision pin, `check_retention.py:645,653`. |
| `decisions/pr862-comment-6272650041.json` | 2,700 | required | R12 decision pin, `check_retention.py:648,651`. |
| `objects/manifest.json` | 727,711 | required | pinned by size and sha256 at `manifest.json:12576-12577`; read by `check_objects.py`. |

| Class | Files | Bytes |
| --- | ---: | ---: |
| removable | 4 | 77,294 |
| required | 16 | 1,974,530 |
| undetermined | 0 | 0 |
| retained data, outside the audit | 1,322 | 14,406,073 |
| archive total | 1,342 | 16,457,897 |

## The removal

- The four removable files are deleted. They are at `55a0e80a` in `main`'s history.
- `manifest.json` (555,580 → 554,070 bytes, sha256 `c5180e20…46d8` → `979f04b3…60cd5`): the entries
  `research-runs-record`, `tranche4-record` and `priority-runs-record`, each listing only its builder, are removed;
  `build_tranche3.py` is removed from `tranche3-record`, which keeps `job_outputs.py`, and that entry's provenance
  source changes from "written for this archive: tranche 3's extractor, reproduction tool and comparator, and the
  script that cut the tranche" to "written for this archive: tranche 3's extractor, reproduction tool and
  comparator". Every touched entry is `complete` with no citations. The file keeps its serialization (indent 1,
  sorted keys, UTF-8, final newline), and no other byte changes.
- `README.md`: line 182 lists `job_outputs.py` alone; lines 333–334 state that a change to the frozen archive is an
  owner-authorized change of its pinned tree id. The line count is unchanged, and line 53, which the object manifest
  cites, is untouched.
- `tools/evidence_archive_check.py` pins the resulting tree.

`check_retention.py`, `check_objects.py`, `reproduce.py`, `compare_result.py`, `extract_result.py`, `job_outputs.py`
and `.github/workflows/reproduce-evidence.yml` are byte-identical.

## Before and after

| | Before | After |
| --- | ---: | ---: |
| archive files | 1,342 | 1,338 |
| archive bytes | 16,457,897 | 16,378,967 |
| manifest entries | 132 | 129 |
| archived files (`check_retention.py`) | 346 | 342 |
| citing locations / claims | 219 / 859 | 219 / 859 |
| claim statuses (differs / not retained / retained) | 1 / 80 / 778 | 1 / 80 / 778 |
| archive tree | `480065e1dd778ccc4f6277d2074f2d5f1e2f1011` | `c8b7e8861dfbb79af1a71c8cef8fcfaf0acea85e` |

## Checks on the resulting tree

Run at `7aa3c8bf7fb1f35e1d7e78115edaea4e65d7112d`, whose archive is tree `c8b7e8861dfbb79af1a71c8cef8fcfaf0acea85e`.
History modes ran in a full-history clone. Plain `check_retention.py` reads R9's scope from the tree, so its outcome
below is specific to that commit. On a commit whose tree carries a receipt that landed after the archive's base and that
the tranche neither covers nor names, such as `verification/receipts/KTOKEN-MAXCONE-1.json` from #829, that mode fails
R9; `check_retention.py --gate`, which reads R9's scope from history, is the check that applies there.

| Check | Outcome |
| --- | --- |
| `check_retention.py` | HOLDS: 0 failures, 84 gaps |
| `check_objects.py` | OK |
| `check_retention.py --gate` | HOLDS: history mode 0 failures; its self-test OK; `check_objects.py --reconstitute` OK (993 stored objects verified, 722 ids on `main`); `check_objects.py --self-test` OK (165 cases); job-output comparator OK; extractor self-test OK |
| `tools/evidence_archive_check.py`, `--self-test` | OK at `c8b7e8861dfb`; self-test OK |
| `tools/legacy_records_check.py <head>` | self-test OK; 303 records intact |
| `tools/artifact_placement_check.py` | OK |

Negative controls, each on the resulting tree and then restored:

| Change | Outcome |
| --- | --- |
| remove `build_archive.py` | R1 fails; O7 fails twice (`build_archive.py:282,285`) |
| remove `job_outputs.py` | R1 fails |
| remove `audit/offmain_audit-output.txt` | R1 fails; O7 fails 24 times |
| remove `open-claims.json` | R1 and R16 fail |
| remove `README.md` | O7 fails twice (`README.md:53`) |
| restore the `55a0e80a` manifest | R1 fails four times, once per removed builder |
| add `build_tranche3.py` back without a manifest record | R6 fails; `evidence_archive_check.py` fails |
