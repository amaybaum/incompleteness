# Changes from r1 to r2, with the source of each

## Sources

- Review r1 (sha256 `268d8f33…2eac`): blocking findings B1 and B2; non-blocking N2–N8 and Q4/Q7 notes.
- The coordinator's r2 instructions.
- The owner's decision of 2026-11-24 on item 7 and SM:1394 (**OWN-A**), which superseded the B1 instruction to keep
  item 7 open.

The r1 files (`PROPOSAL.md`, `CHANGE-INVENTORY.md`, `ITEM7-DOSSIER.md`, `diffs/`) are unchanged.

## Changes

| # | Change in r2 | Where | Source |
|---|---|---|---|
| 1 | r1's claims about item 7's failing lines are withdrawn. Only the measured counts are stated. | PROPOSAL-r2 §3.1; §32.9 | B1 |
| 2 | Item 7 is kept exactly as frozen. The restatement (design note 1), the narrower exception option and the reviewed false-positive exception are all withdrawn. O-1 is settled. | PROPOSAL-r2 §1, §3; §32.4 row 7; config `checks.item7` | OWN-A (supersedes B1's open-item handling) |
| 3 | New edit records D402–D409. The three book sentences and their FULL mirrors name the Chapter-5 properties. SM:1394 states its dependencies. Ledger: 407 splices, 409 records. | `diffs-r2/new-edit-records…`, `EDITS-P-to-r2.diff`, `LEDGER-new-splices…`; §32.9; §32.1; §32.10 pins | OWN-A |
| 4 | SM:1394 dependency trace, per prediction, with citations, evidence layers, the A1 determination and the open dependencies | PROPOSAL-r2 §3.3; §32.9 | OWN-A requirements 1–6 |
| 5 | Checks of the extended plan: build, static, simulate, pins, repo-scan, self-tests, verify-ledger and verify-pins, item 7 with negative controls, duplicate check, TeX rebuild | PROPOSAL-r2 §3.4; §32.9 results; `work-r2/*.out` | OWN-A |
| 6 | ESC-1 v2 carries W2-a and W2-b only. W1-a to W1-d are dropped, because no count line remains. | `diffs-r2/w1-w2-allow-v2.json.proposed`; §32.5 | OWN-A, ESC-1 |
| 7 | DR-1/3/4/5 and `resid` profiles, their rule files and reviews are removed from the configuration. O-10 is settled. | config; inventory C/D | OWN-A, N4 |
| 8 | The post-`F` side-change claim is corrected. O-9 is added, for a cycle-free plan-directory rule. A and C′ are both made conditional on O-9. B is invalid. | PROPOSAL-r2 §5; §32.7 | B2 |
| 9 | The §25.2 landing-diff reading for paths that `M` and `C` change identically; O-11 | §32.7; O-11 | N7 |
| 10 | Item 14's landing part goes through the tool, because `preserve_check --base main` is refused | §32.4 row 14; PROPOSAL-r2 §5 | review Q4 |
| 11 | The configuration `author` becomes a placeholder for the writer of this version | config; §32.2 | N5 |
| 12 | The T1′ trace is completed: `controls.json`'s `agents-md-at-T1p` and `a1_controls.py`'s real-tree controls are not acceptance inputs | §32.4, §32.5 | N6 |
| 13 | The foreseeable side-change and reconciliation records, frozen with `F`, are added to the configuration and the inventory | config `records`; inventory C | review Q7 |
| 14 | The V6 scan scope is corrected | PROPOSAL-r2 §2 | N3 |
| 15 | ESC-3 is reworded: "against blob sha256 `2856e58c…` … carried unchanged into `F`" | §32.5 | N8 |
| 16 | O-4 is reduced to N2: whether the predecessor v1's fingerprint lint is required. The W1-d part no longer arises. | PROPOSAL-r2 §4, O-4 | N2, OWN-A |
| 17 | Design citations are re-checked against v6.0e (sha256 `4024a31c…5205131`) and INVENTORY-v6.0e (`ce3abd51…20f0`). The P8 workflow wording follows v6.0e. | PROPOSAL-r2 §0; §32.2 | coordinator |
| 18 | New O-12: SM:1394's generation entry omits H-spin′. An optional edit D410 is proposed and not included. | PROPOSAL-r2 O-12 | finding of the OWN-A trace |
