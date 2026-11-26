# Records and rule files without review evidence (C-29 inventory, WIP / UNVERIFIED)

Status: working inventory for the independent review the owner authorized (amaybaum, 2026-11-26T07:05:39Z; #1169
comment 7185092393), quoted: "Authorize independent review of the A1 rule files and records that currently lack review
evidence ... Review the rule files and records on their actual merits. ... Do not create nominal review records merely
to make tests pass." It lists what the A1 controls read and what has no `oi-review-record/1` naming its blob. It is not
a review, creates no review record, and decides nothing.

Goal link (AGENTS.md sec. A.47): A1-EXIT (#1169); it serves the review that decides whether these records may be used
by any run under record lint (design r6 R6.REC.6, R6.REC.7; OBL-28 C-29).

Source of the dependencies: the local runs of the A1 runners after C-29 part 1 (tool commit 535273b6a, staged draft
configuration), reading the `record-invalid` items of every retained result; a row is listed when a run it rests on
reports the record `record-invalid`. A row listed here can fail for other reasons as well.

## Repository records read through the A1 configuration

Commit: every path below is on the tool branch `tools/a1-ledger-coverage-r6` at the commit that carries this file;
"main" gives its blob there (main 13f5c66a, checked against the remote with `git ls-remote` and a repository API
GET on 2026-11-26) where the path is on `main`.

| Path (tool audit directory) | Kind | sha256 | On main | A1 rows that rest on it |
|---|---|---|---|---|
| `rules/dr-deny-v1.json` | rule file (deny rules DR-1, DR-3, DR-4, DR-5) | daf3a8e231ace391f0037447d1266d1255df8dc015baaaa601fcc79b63cec6ae | yes, same blob | 93 rows: A1r-A11r, G1-G3, L1-L4, N-W, N3-config-route, RT-A, RT-C, RT-D, RT-D-gr58, RT-DR3W, RT-E, RT-H0, RT-L, RT-L2, RT-O9, RT-T0, RT-X, S11-1 to S11-14 (as run), S11-56, S2r, V1-V27-glossary, WB1-WB15, item11-T1p |
| `rules/resid-v1.json` | rule file (review pattern resid) | 7aa1412206f7bf5fec1d3573d76e1b91c0f6bc8f67704a1dcb75344d09aac221 | yes | the same 93 rows (every run that loads the configuration's rule files) |
| `rules/w1-w2-allow-v3.json` (supersedes v2; removes W1-a, for which no valid justification exists) | rule file (allow rules W1, W2) | 5485154a9c703192d4de65619ad5948d14fec7dbbffa2440b6482019efea15db | no | the same 93 rows; their allowances decide WB1-WB15, L1-L4, V7a-V7c, V25, S1r, S2r |
| `rules/w1-w2-allow-v2.json` (predecessor of v3) | rule file (allow rules W1, W2) | 306017d93211bded9cf63f964d60f17db543f02e11183fb82b05d6a76d2bb903 | no | the same rows, through the lineage lint of v3 |
| `rules/w1-w2-allow-v1.json` (predecessor of v2) | rule file (allow rules W1, W2) | 0cbb97c98725cba618598650b0cd9c687c97e280b3422c4ad6e62794a222b171 | yes | the same rows, through the lineage lint of v2 |
| `rules/register-infinity-params-v1.json` | params (per-edit parameters of items 5 and 6) | 05149ba694dd4017ad27dd60c02810403ec7351036776bea212768ba9ebc509f | yes | the same 93 rows; it sets op C's per-edit evaluation (S11-5, S11-6, S11-56) |
| `records/side-change-classes-v16.json` (the head of the class-record lineage v1-v16 at this commit; v16 pins this file's blob, so its own digest is not stated here; its predecessor v15 has sha256 b20e67c382c2f3d4849dbc1755d784f1e42e457546f6ad96a361c5034ba18268) | side-change class (tool-landing) | (see the path's blob) | no (v1 only, sha256 4b28d3d22452bca712ab7c082feee5af3cd1dc1d81260dae2d6b7808354687b8) | 19 rows: G1-G3, RT-C, RT-L, RT-L2, RT-O9, RT-X, S11-1, S11-3 to S11-6, S11-8 to S11-10, S11-12 to S11-14 |
| `records/gr58-hit-classification-v3.json` (supersedes v2; the ptr hit's reason says what ptr detects) | hit classification (`--classify`) | 0e2cd408c500313f3c214590f86d76eb33529875903682924f1f94a8340beb86 | no | RT-D-gr58, RT-D (through C-29 part 2: a `--classify` record is linted at its record commit) |
| `records/gr58-hit-classification-v2.json` (supersedes v1; names and reasons every profile hit on the line; predecessor of v3) | hit classification (`--classify`) | 28c5a5706605cabc5c7542ca3b9ad11f96151d3e8c829aa73b391420ecea54c1 | no | RT-D-gr58, RT-D (through C-29 part 2: a `--classify` record is linted at its record commit) |
| `records/gr58-hit-classification-v1.json` (predecessor of v2) | hit classification (`--classify`) | 8177b0923a7eddf09c473ce541e4c23de53067429a31d52260aa35f0bafa8410 | yes | the same rows, through the lineage lint of v2 |
| `records/repo-scope-v1.json` | scope record (`--scope`) | 32afecca8e371a1f51217a70058676144e874b24526ca0becddea04e2c12df42 | yes | item11-T1p, S11-11, RT-D (read through `--scope`; not chain-linted by op C at this commit) |
| `delegation-draft.json` | delegation contract (draft) | 015826146fd01b9f5ebc5ae8b1966f700e2f964b8989203d66b75e36e032f65c | yes | every op C run (RT-C, RT-X, RT-L, RT-L2, RT-O9, S11, G1-G3); read by its pin, not chain-linted |
| `controls.json` (keeps only `control_inputs`, `operations` and `direction`, R6.GATE.1) | controls file | fd6d16f84ad5d9ef70655461d46a62ec2af018b917841f475dea01bcc98bde72 | yes (older blob, sha256 96f3032097e817f33803d62e75b4055cb2f6111b29dc3a3ed58cb3e4115ce3d8) | every run (preflight controls of the configuration); read by its pin, not chain-linted |

Main's move from 83e08bd9 to 13f5c66a changes no digest above. It changes papers/SM.md (a ledgered path, so it
drifts further), papers/SM.tex and SM.pdf, and the Main, Substratum and FULL PDFs, which need the generated-artefacts
class; the B4 class records' pins at 13eeca70 predate these changes.

The A1 configuration itself (`retirement-config.json`, the staged draft at the plan directory's path) is admitted only
by the control harness; its review chain is outside C-29 and outside this inventory.

## Reconciliation and class records of B4 (branch `records/a1-b4-rebuild-20261126` at 13eeca70)

| Path (`verification/audits/foundations/a1exit-reconciliation-b4-20261126/records/`) | Kind | sha256 | A1 rows |
|---|---|---|---|
| `reconciliation-agents-md.json` | reconciliation (predecessor) | 331c06740385fc25bd131edb7c93496a240fe9844c9d8a085593a024497aefd9 | RT-L2, RT-O9-L2 (as predecessor of r2) |
| `reconciliation-agents-md-r2.json` | reconciliation | cf14d6a948d37927290b0fcd8c43ccc8c79e38bcc8af145f25d31f5e5c288bb1 | RT-L2, RT-O9-L2; its `M` and `X` are null, so it fails the binding of R6.RECON.2 (a) until a superseding record names them |
| `side-change-classes-m0.json` | side-change class (predecessor) | e422fc5c441f58fd536188fa8a9f7c3a58c8e5e7d9c94779df23dee96cdc4af2 | RT-L2, RT-O9 (as predecessor of r2) |
| `side-change-classes-r2.json` | side-change class (143 pins in eight classes) | fbc1ceddea1d5ef2811745bb39f8cdbfe7c30a2f41503927d019f56b96f45929 | RT-L2, RT-O9 |

## Not repository records

Control fixtures that a runner writes into in-memory commits (for example `records/n3-reconciliation.json`,
`records/n3-classes.json`, `rules/dup.json`, `records/control-recon.json`, `records/control-drift-classes.json`) are
not records of the repository and need no review; a row that fails because one is unreviewed is a runner question,
listed in the stage report.

## What a reviewer judges, per kind (design r6 sec. 6.3, 11; R6.REC.6, R6.REC.7)

- Every record: the schema and fields; the author; one verdict per item id, each on its merits; for a record that
  supersedes another, that the predecessor passes the lint itself and the lineage (`record_id`) is one chain.
- Deny rule file (`dr-deny-v1.json`): each rule's patterns against its positive and negative examples and its
  countercontrols, its scope, and whether it closes the retired forms it targets without matching legitimate text.
- Review pattern (`resid-v1.json`): each alternative against its examples; that it raises REVIEW only, as intended.
- Allow rule file (`w1-w2-allow-v2.json`, with its predecessor v1): each rule's literal, context and negative matchers, its fingerprints (the
  exact sentences at `recorded_at`), its scope and instance limit, and that its negative allowances admit no retired
  form; the widening review where a rule widens.
- Params (`register-infinity-params-v1.json`): the per-edit parameters against the plan checker the configuration
  pins (sentence splitter, profiles), and its examples.
- Side-change class record (tool lineage, B4 classes): that every pinned path is a side change the class correctly
  describes, with its exact blob; that no prefix classifies by itself; that the record pins the class records it
  supersedes; the reason of each class.
- Hit classification (`gr58-hit-classification-v2.json`, with its predecessor v1): the line's semantic classification
  against the text at the pinned segment, the profiles named, the reason given for each profile hit, and uniqueness of `file` and `line_sha256`.
- Scope record (`repo-scope-v1.json`): the scope's paths against the item 11 check it serves.
- Reconciliation record (B4): RC1 to RC13 re-derived from git objects for each path; that `M` and `X` name the run's
  commits (R6.RECON.21); the protected ranges and translation labels; `changes_decisions_on_X` empty; placement in a
  reconciliation directory.
- Delegation contract and controls file: read by pin and not chain-linted at this commit; listed so the reviewer can
  decide whether their review is needed for the A1 retirement.
