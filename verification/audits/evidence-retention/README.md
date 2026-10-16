# Evidence retention (AGENTS §A.42)

This archive retains, on `main`, evidence that records already frozen cite but that was held only off `main`: in a session scratchpad, in CI logs that expire, or in commits on branches other than `main`.

It is a governed audit record. It is not a research round and changes no historical result.

- **Frozen records stay unchanged.** No native-round record (G13), legacy record or receipt is edited. Instead, the manifest maps each citing `file:line` to its retained copy.
- **No claim is affected.** Nothing here strengthens a claim, repairs a check, or changes what any record says it measured.
- **Retention is not verification.** `tools/v3_verifier.py`'s verdicts are unchanged.

## Tranche 1 (this commit)

| directory | what | kind |
| --- | --- | --- |
| `bg3/` | BG-3's four cited job logs: the bridge-log tails of jobs 116826161407 (`E`), 116805436638 and 116761232088 (design trees), and the design-run log of job 116831668411 | `complete-as-cited`: byte-identical to the digest each citing record names |
| `ci/<run>/run.json` | for each of the 96 runs below, the run's identity and outcome (`id`, `head_sha`, `event`, `conclusion`, `created_at`, …) | `derived`: selected fields of a saved API listing page; `source_sha256` is that page |
| `ci/<run>/jobs.json` | every job of the run, with its name and conclusion | `derived`: selected fields of a saved API response; `source_sha256` is that response |
| `ci/<run>/bridge-excerpt.log` | from the Mathlib bridge job's log: the release-gate block, the build status line, any error or `sorry` marker, and the axiom reports of the round's own governed Lean modules | `excerpt`: exact lines of the served log; `line_ranges` are 1-based within it, and `served_sha256` is its digest |
| `audit/` | the off-`main` reference audit at `fc5abade`: script, output and report | audit record |

**The 96 runs** are of two kinds:
- every check run that a receipt under `verification/receipts/` records as `F`'s or `E`'s `check-run` attestation (93 runs);
- the three runs the V2 certificates under `verification/certificates/` cite.

They span 2026-09-21 to 2026-10-16. The oldest are the first to reach GitHub's log-retention limit.

**What "served" means.** The CI logs were read through GitHub's job-log API, which serves at most the last 5000 lines of a job log. Full log archives could not be downloaded from the session that built this tranche, because its network policy blocks the archive host. Each excerpt is therefore an excerpt of the served text, and the manifest records:
- the served text's line count;
- its digest;
- the original log length, where the API reported one.

Where a round's module was not rebuilt in a run, or its axiom reports fall outside the served lines, the manifest says so. Nothing is reconstructed in its place.

## Checking

From the repository root:

```
python3 -I verification/audits/evidence-retention/check_retention.py
python3 -I verification/audits/evidence-retention/check_retention.py --self-test
```

The checker uses the tree alone: no git history, network or third-party package. It verifies:
- every archived file's size and sha256;
- the digest match of each `complete-as-cited` file;
- that every citing file still has its recorded blob id, and the cited line still holds the cited token;
- every excerpt's line count against its ranges;
- the absence of secret patterns;
- that no unlisted file sits in the archive.

It lists every gap. The self-test mutates a copy and requires each rule to fire.

## Secrets and operational data

Every retained log and excerpt was scanned before commit for:
- token and key patterns;
- private-key headers;
- signed-URL parameters;
- IP addresses;
- e-mail addresses.

The only matches were GitHub's own masked lines (`Secret source: Actions`, `AUTHORIZATION: basic ***`) and the public Mathlib cache URL. Nothing was redacted.

## Not yet retained

Recorded here so the gap is visible, not resolved. Counts are from the audit at `fc5abade`:
- **Commits not reachable from `main`:** 134, cited from 155 places in native-round records and one mutable script.
- **Blobs and trees not reachable from `main`:** 77.
- **Other CI runs:** about 360 references in 181 files, minus the 96 runs above.
- **Act-26's scratchpad computation** (`result.md:931`), which was never saved in any form the audit found.

Each needs a documented resolution in a later tranche: retained content, an excerpt, or a recorded gap.
