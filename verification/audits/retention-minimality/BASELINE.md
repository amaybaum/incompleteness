# Retrospective evidence-retention minimality audit (active, read-only)

Status: **WIP / UNVERIFIED necessity verdicts**. This is the first measured baseline of an active audit, not an archive change, a scientific claim, or a proposal to delete anything.

## Question and governing standard

Does each item retained by the evidence-retention archive have a surviving claim that needs **those bytes or that exact Git object**, or has the archive preserved a larger checkout/history closure than the claims actually require?

The governing rule is [AGENTS.md §A.42 item 8](../../../AGENTS.md): **necessity, not exposure**. Only an item shown to serve a surviving claim, and not shown redundant by regeneration and comparison, qualifies for new retention. Sections A.42(1–6) still require specific expected results, host-run attestation evidence, exact digest-pinned artifacts and owner designations. Item 8 governs newly retained content; it is not retroactive permission to remove previously archived material.

This audit separates two questions often conflated:
1. **Evidence necessity:** which original run outputs, identities, results and exact artifacts are essential to the particular claim at the recorded `file:line`?
2. **Reconstruction necessity:** which Git commit/tree/blob objects are essential to the *promised reproduction mode*, including exact historical checkout or full-tree restoration? A path subset is not equivalent to a full-tree checkout merely because the checker or Lean build passes.

All counts below are a reproducible **inventory**, not labels of required, redundant or optional.

## Pinned snapshot and measured census

- Repository base `D` (main, 2026-10-19): `6fe84106e842465f086c9bf301c82781421c0bfd`.
- Source object manifest: `verification/audits/evidence-retention/objects/manifest.json`, blob `2ee4fbb95118115b4fb874b3c59c65e1b155aec9`.
- Source evidence manifest: `verification/audits/evidence-retention/manifest.json`, blob `191d16654d8b98d33e0ffe57c2986677d76e0b11`.
- The archive itself is not modified by this audit. These are baseline counts at the named snapshot and are not intended as claims about future `main`.

| Tranche | Manifested contents | Stored material | Direct citations / pending / dependency-only |
| --- | --- | --- | --- |
| 1 | 96 `ci-*` expected-results entries; four byte-pinned BG-3 logs are separately represented | Structured run evidence and four exceptional raw artifacts | Run attestations and frozen digest/line citations; no per-file minimality verdict yet |
| 2 | 920 Git-object entries: 137 commits, 540 trees and 243 blobs | 892 files, 10,000,160 stored bytes; 28 blob entries withheld | 165 directly cited objects; 755 without direct citations, included as dependencies (727 stored, 28 withheld) |
| 3 | 22 `run-*` entries in the evidence manifest | 7 runs with only `run.json` + `jobs.json`; 15 also have `expected.json` | All 22 have mapped citations; whether *each field/file* is necessary remains untested |
| 4 | 66 Git-object entries | 64 files, 263,931 stored bytes; 2 withheld | 4 commits `awaiting_citation` and 62 dependent entries |
| 5 | 37 Git-object entries | 37 files, 261,310 stored bytes; none withheld | 3 commits `awaiting_citation` and 34 dependent entries |

Here, **directly cited** means an entry has nonempty `cited` in the manifest, **pending** means the commit has `awaiting_citation`, and **dependency-only** means neither. This is a manifest-accounting distinction: neither dependency-only nor pending is evidence of redundancy. The full-tree requirements in the current checker may legitimately require many objects with no direct citation. Conversely, a direct citation alone does not prove its full tree must be stored. The archive's membership/digest pins establish integrity, not a minimum-set theorem.

These counts can be re-derived at D without API calls:

```python
import json
from pathlib import Path

p = Path("verification/audits/evidence-retention")
objects = json.loads((p / "objects/manifest.json").read_text())["objects"]
for tranche in (2, 4, 5):
    rows = [x for x in objects if x["tranche"] == tranche]
    direct = sum(bool(x.get("cited")) for x in rows)
    pending = sum(bool(x.get("awaiting_citation")) for x in rows)
    print(tranche, len(rows), sum(bool(x.get("file")) for x in rows),
          sum(x["bytes"] for x in rows if x.get("file")),
          direct, pending, len(rows) - direct - pending)

entries = json.loads((p / "manifest.json").read_text())["entries"]
runs = [x for x in entries if x["id"].startswith("run-")]
print("ci", sum(x["id"].startswith("ci-") for x in entries),
      "runs", len(runs),
      "metadata-only", sum(
          not any(f["path"].endswith("/expected.json") for f in x["files"]) for x in runs))
```

Expected census: `2 920 892 10000160 165 0 755`; `4 66 64 263931 0 4 62`; `5 37 37 261310 0 3 34`; `ci 96 runs 22 metadata-only 7`. This reproduces the manifest's accounting only; it does **not** run the independent restoration tests.

## First finding: risk of over-retention, not a proven removable object

Tranche 2 is the largest candidate: the majority of entries have no *direct* citation, and the archive's chosen `raw:connected` / `raw:tree` mechanisms restore broad historical trees. A lower-volume, claim-specific reconstruction might someday suffice for some cases, but that is a hypothesis. The audit must not recommend dropping a historical revision merely because a later revision looks similar: original identity, frozen digest, and the required mode of restoration may make it indispensable. In particular, `verification/lean-manuscript-census.json` and `verification/lean/edge_rigidity_probe.py` recur across archived trees and are useful **test candidates**, not declared duplicates.

Tranches 4 and 5 are small and attach to ongoing research/native rounds. Pending citation status means the claim has not yet landed on the baseline `main`; it is not by itself a reason to retain or remove, and F-to-receipt preservation obligations must be evaluated explicitly. Tranche 3 retains run/job metadata needed by many recorded push-run claims; only a claim-by-claim field-level audit could find excess. Tranche 1 contains expected results and the BG-3 digest/line-pinned exception, which §A.42 treats distinctly.

## Work method — depth-first, tranche 2 first

1. **Reconcile the inventory:** for each candidate identify its exact object id or file SHA, tranche, stored bytes, kind, `needed_by`, mapped surviving `file:line`, and whether the owner-approved policy requires exact historical bytes or a complete checkout. Distinguish a run's host identity from the possibility of regenerating scientific output.
2. **Classify against the actual guarantee:** `required`, `redundant`, `optional`, `undetermined`. A `required` or `redundant` row names the surviving claim and its proof. `optional` requires a demonstrated absence of any surviving claim requiring it. Missing source/original comparison evidence => `undetermined`, not `redundant`.
3. **Test a single tranche-2 pilot before broadening:** trace one cited historical commit's complete closure, examine whether each dependent object is on the selected reproduction path, and try a narrower counterfactual package **only in an isolated disposable copy**. Include a nontrivial negative control that rejects the omission of genuinely essential evidence. Do not use a later successful run as a substitute for a specific attested run.
4. **Prove any alleged redundancy:** regenerate the original from `main` or already retained content; compare byte-identically (or an expected result under `compare_result.py` where the policy permits), record exact commit, command, input and comparison. Prove offline restoration with no network, alternate object store or shared Git objects when full-tree restoration is part of the guarantee; run `fsck --full --strict`, the relevant archive checks and independent controls. Do not merely relax membership pins until a missing item ceases to be checked.
5. **Independently review the necessity ledger:** tally bytes and guarantees preserved, controls that would catch erroneous deletion, dependencies on ongoing F/E holds, and gaps/undetermined results. Then consider tranche 3 and later tranches. No broad inventory-based extraction or tranche expansion follows from an expiring log alone.

## Stop conditions and authority limits

- **Read-only audit. No deletions**, archive edits, record rewrites, ref deletion/movement, GC, prune, `main` merge, retention promotion, bulk extraction, workflow dispatch or special launch are authorized by this PR.
- Do not change `AGENTS.md`, `check_objects.py`, `check_retention.py`, `objects/manifest.json`, membership pins, receipts or scientific claims as part of this initial thread.
- A narrowed replacement archive, if eventually proposed, requires its **own** reviewed migration/compatibility proof and explicit owner authorization before any destructive step; pre-existing frozen records remain forward-only.
- Existing #862's 223-run extraction stays under its own approvals. This audit supplies necessity evidence before any further **new** bulk retention, not a retrospective claim that #862's full set should run.
- This initial commit publishes a verified snapshot and testable question. **Necessity classifications, a removable-object count, and any claimed space savings remain OPEN** until pilot regeneration, integrity controls, and independent review.

## Next active checkpoint

Publish a per-object, citation-aware pilot for tranche 2 that isolates one directly cited head, derives its reconstruction dependency closure, and reports both the full-tree and claim-minimal hypotheses with actual negative controls. Retain all originals unchanged. A separate reviewer should validate the pilot before generalizing it.
