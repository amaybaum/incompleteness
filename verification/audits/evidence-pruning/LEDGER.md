# Frozen evidence archive: removal ledger (stage 2, draft)

**Scope.** The per-file dependency and citation audit of the code and bookkeeping files of
`verification/audits/evidence-retention/`, the removal set it supports, and that set's manifest migration.
Base: `main` `55a0e80abc4b96e7bf211566a036ad17ea64a69e` (the archive is byte-identical to `809fa9d6`, tree
`480065e1dd778ccc4f6277d2074f2d5f1e2f1011`). Retained evidence data (`objects/` other than its manifest, `bg3/`,
`ci/`, `runs/`) is out of scope and unchanged. This ledger authorizes nothing: the archive is frozen (AGENTS §A.42
item 8) and any change to it is an owner-authorized change of `tools/evidence_archive_check.py`'s pin.

## Method

For each file: its manifest entry, kind and citation count; every reference to its name anywhere in the tracked tree
(`git grep` over workflows, `tools/`, the release gate, AGENTS.md, frozen records, receipts, legacy records, the
manifest, the object manifest and the archive's own files); every retained result naming it as extractor or
reproduction tool; and, for open rounds, the frozen records of #829 at `F` `e12c1573` and at its head `e35fe099`.

A file is **removable** only when no check, workflow, retained result, frozen record or recorded citation depends on
it, and its removal needs no manifest edit that changes what a citation or claim records. It is **required** when a
dependent is named below. No file is classified as redundant, and none is **undetermined**.

## Ledger (bytes at the base)

| File | Bytes | Class | Dependents (file:line at the base) |
| --- | ---: | --- | --- |
| `build_tranche3.py` | 32,767 | removable | `manifest.json:14568` (file record of `tranche3-record`, `complete`, 0 citations); `README.md:182` (description); `build_priority_runs.py:8,258` (itself removable). No retained result names it: the tranche-3 results name `job_outputs.py` as extractor and tool. |
| `build_priority_runs.py` | 18,722 | removable | `manifest.json:14908` (sole file of `priority-runs-record`, `complete`, 0 citations); `README.md:182`. R12's priority-run pins (`check_retention.py:638-660`, `PRIORITY_ALLOWLIST`) bind the run entry and `decisions/`, not this script. |
| `build_research_runs.py` | 14,649 | removable | `manifest.json:14680` (sole file of `research-runs-record`, `complete`, 0 citations); `check_retention.py:315` names the entry id only to exempt it from R13, so the clause becomes inert. Research results name `extract_result.py`. |
| `build_tranche4_objects.py` | 11,156 | removable | `manifest.json:14696` (sole file of `tranche4-record`, `complete`, 0 citations). What it wrote is pinned independently: tranche 4's 66 ids in `check_objects.py` (`TRANCHE_MEMBERS`), the withheld approvals in `APPROVED_WITHHELD`, and the controls and approval it carried in `objects/manifest.json:22137,22147,22417`. #829 cites the objects, not the script. |
| `build_archive.py` | 28,897 | required | `objects/manifest.json:9295,18909`: archive-self citations of `build_archive.py:285,282`, which `check_objects.py` O7 reads; `bg3/results-116831668411.json:49`: this retained result's extractor is its `design_results` filter; `ci/36228429141/re-extraction-fdf3ec80cdaa.json:25-26`: its recipe; `manifest.json:12528`. |
| `check_retention.py` | 199,808 | required | `AGENTS.md:924` and #829 (old §A.42: direct `--gate` checkpoint); `.github/workflows/reproduce-evidence.yml:139`; `check_retention.py:182` (`FIXED`). |
| `check_objects.py` | 195,528 | required | loaded by `check_retention.py:176-179` and run at `:1582`; the only verifier of `objects/`; `manifest.json:12570`. |
| `manifest.json` | 555,580 | required (migrated) | read by `check_retention.py:206`, `reproduce.py:238,332`, `job_outputs.py:297,496`; lines 750 and 991 cited by `objects/manifest.json` (O7). |
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
| retained data, out of scope | 1,322 | 14,406,073 |
| archive total | 1,342 | 16,457,897 |

## Manifest migration

`manifest_migration.py` computes the migrated manifest from the base blob and checks it byte for byte (`--check`):

- remove the entries `research-runs-record`, `tranche4-record` and `priority-runs-record`, each listing only its
  builder;
- remove `build_tranche3.py` from `tranche3-record`, keeping `job_outputs.py`, and set its provenance to
  "written for this archive: tranche 3's extractor, reproduction tool and comparator".

All four touched entries are `complete` with no citations, so every citing location, claim, status and retained-file
mapping is unchanged. The script refuses a base whose digest differs and a serialization that does not reproduce the
base manifest byte for byte before the edit. Base manifest sha256 `c5180e20…46d8`; migrated sha256
`979f04b3…60cd5` (555,580 → 554,070 bytes).

`README.md` changes on two lines, after the cited line 53 and without changing the line count: line 182's row drops
the two removed builders, and line 315 states where the four builders are kept (the base commit).

## Before / after

| | Before | After |
| --- | ---: | ---: |
| archive files | 1,342 | 1,338 |
| archive bytes | 16,457,897 | 16,379,386 |
| manifest entries | 132 | 129 |
| archived files (`check_retention.py`) | 346 | 342 |
| citing locations / claims | 219 / 859 | 219 / 859 |
| claim statuses (differs / not retained / retained) | 1 / 80 / 778 | 1 / 80 / 778 |
| archive tree | `480065e1dd778ccc4f6277d2074f2d5f1e2f1011` | `ca86cd659b811a01495c421d4354aa3fa0f6b576` |

**Capability lost:** the in-tree copies of four one-shot scripts that cannot cut new tranches (the archive is not
extended) and that no check or workflow runs. They stay at the base commit on `main`'s history.
**Capability kept unchanged:** `check_retention.py` (byte-identical, so #829's `--gate` checkpoint runs the same
code), `check_objects.py`, the `reproduce evidence` workflow and every tool it consumes.

## Checks

Run locally on the pruned tree, the history-mode checks in a full-history clone (the shared session clone is shallow,
where `--gate` and `--reconstitute` cannot decide H3). The exact commands and outcomes are in the removal commit's
message. Negative controls: removing a required file (`build_archive.py`, `job_outputs.py`,
`audit/offmain_audit-output.txt`, `open-claims.json`, `README.md`) fails `check_retention.py` (R1/R16) or
`check_objects.py` (O7); the unmigrated manifest over the pruned tree fails R1 four times and the migration
`--check`; a removed builder re-added without a record fails R6 and the archive pin.

Still owed before merge (PRUNING-PLAN.md): an independent exact-tree review, the full release gate and an exact-head
CI run, a `reproduce evidence` run if the owner wants the workflow exercised, and the owner's authorization of the pin.
