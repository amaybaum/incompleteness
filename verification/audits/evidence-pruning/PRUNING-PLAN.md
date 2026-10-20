# Frozen evidence archive: pruning review (draft)

**Scope:** optional follow-on to merged #886; exploratory draft, **not** approval to merge or remove scientific evidence. Base `main` = `809fa9d6fc931d7a75027ad72d6d2d4b03b722a5`. The archive is frozen at tree `480065e1dd778ccc4f6277d2074f2d5f1e2f1011` by `tools/evidence_archive_check.py`. No archive data or checker is changed in this first commit.

## Why inspect it

The archive has 1,861 Git-tree entries and approximately 16.46 MB of blob contents (tree inventory at the base). Most of this is **data deliberately retained for restoration and reproduction**, not bloat. The experiment is to reduce needless *current-tree code and bookkeeping* without deleting evidence that a surviving claim or workflow needs.

Preliminary candidate ledger (blob sizes at the base; classification is **provisional**, not a removal verdict):

| Path under `verification/audits/evidence-retention/` | Bytes | Classification / blocker |
| --- | ---: | --- |
| `build_archive.py` | 28,897 | Review for removal; listed as `complete` in `manifest.json` and named in a re-extraction recipe |
| `build_priority_runs.py` | 18,722 | Review for removal; `complete` entry in manifest |
| `build_research_runs.py` | 14,649 | Review for removal; `complete` entry in manifest |
| `build_tranche3.py` | 32,767 | Review for removal; `complete` entry in manifest and referenced by another builder |
| `build_tranche4_objects.py` | 11,156 | Review for removal; `complete` entry in manifest |
| `check_retention.py` | 199,808 | **KEEP for now:** the dispatch-only reproduction workflow calls it, and #829's earlier frozen policy requires `--gate` |
| `check_objects.py` | 195,528 | **KEEP for now:** independently verifies/restores retained Git objects |
| `manifest.json` | 555,580 | **KEEP for now:** current checker/reproducer uses entry and provenance mappings |
| `README.md` | 56,463 | Review for a shorter live overview, but keep the anchored line 53 and its exact cited text until independent citation check |
| `objects/`, `bg3/`, `ci/`, `runs/` | retained data | **KEEP** all retained Git objects, four BG-3 raw logs and every structured expected result |

The five builders total **106,191 bytes** and about **1,574 source lines**. They are not imported or invoked by the current `reproduce evidence` workflow, but the manifest explicitly inventories them. **Deleting them alone is invalid**: first design a forward-only manifest/citation migration and independently verify it; simply removing files would break the old checker and its promised guarantees. Removing the larger checkers/manifest could save substantially more code but has stronger dependencies and requires a separate workflow decision.

## Default boundary: preserve reproduction

The initial option is to **keep** `.github/workflows/reproduce-evidence.yml`, `reproduce.py`, `compare_result.py`, `job_outputs.py`, `extract_result.py`, and their currently required manifest/checker dependencies. A more aggressive option retires the optional workflow and removes its checker/build code after a separately approved migration; this is **not** authorized by this draft. Data-only cleanup that makes the workflow silently unusable is not acceptable.

## Mandatory dependencies

1. **Act-37 discrepancy (met):** the frozen preregistration says 4,829 axiom reports for run 36373806246, whereas its structured expected result says 4,803. The finding lives outside the archive in `verification/audits/provenance-errata/ACT37-CI-COUNT.md`, landed by #887 (`55a0e80a`). Do not edit the frozen Act-37 directory.
2. **Legacy-frozen native rounds:** #829 still needs an E-evidence retention PR and the direct `check_retention.py --gate` checkpoint under its original §A.42. Do not remove that command or weaken the requirement without satisfying and independently verifying the checkpoint.
3. **Frozen evidence and immutable claims:** never rewrite a saved expected result, run identity, job record, BG-3 byte artifact, retained object, legacy/frozen round, receipt or scientific verdict. New bookkeeping must be forward-only and attributable.
4. **Archive fingerprint:** any authorized archive change must recompute the exact directory tree ID, update `tools/evidence_archive_check.py`'s pin and test its negative controls. The old tree remains recoverable from the base commit.

## Stage 2: removal ledger

`LEDGER.md` replaces the provisional table above with the per-file audit: four builders removable (77,294 bytes), `build_archive.py` and every other code or bookkeeping file required, none undetermined, and the manifest migration `manifest_migration.py` checks byte for byte.

## Acceptance tests before any destructive patch is proposed for merge

- A dependency/citation census covering each deletion: exact file, role, `manifest.json` entry, consumer, surviving claim and any pinned source digest.
- Positive regression: exact restoration of retained objects in an isolated repository; equality of retained output bytes, hashes and cited lines; `check_objects.py`, `check_retention.py --gate`, archive fingerprint, V3 receipts, legacy records, and full release gate still pass **where applicable**. If tools are retired, provide a reviewed equivalent of every remaining required check, or defer deletion until its obligations end.
- Negative controls: corrupt a retained object, BG-3 log, expected result, provenance mapping and pin; each must fail its intended surviving check. Ensure no existing workflow calls a removed tool. Run all expensive checks in CI, not a disk-constrained shared checkout.
- Independent exact-tree review and a subsequent exact-head CI run. Report before/after tracked files, lines and bytes and the lost/replaced operational capability.

## Status and authority

**WIP / UNREVIEWED:** the draft branch carries one proposed pruning patch: the four builders of `LEDGER.md` removed, the manifest migrated, two `README.md` lines corrected, and `tools/evidence_archive_check.py` re-pinned to tree `ca86cd659b811a01495c421d4354aa3fa0f6b576`. No retained data, checker or workflow is changed or retired, and nothing is merged. The pin change needs the owner's authorization (AGENTS §A.42 item 8); opening this PR does not grant its merge.
