# Audit: references on `main` that depend on content not retained on `main`

Status: read-only audit of `main` at `fc5abade2a8ca381caedaa93c0441570fc060319`, made on 2026-10-16. No record was changed by it.

## Method

The audit is `offmain_audit.py`, in this directory, run as `offmain_audit.py fc5abade…` from a clone with every remote branch fetched. Its complete output is `offmain_audit-output.txt`; every count below is a line of that output.

Unlike the archive's checker, the audit needs git history and the remote branches. The `exists` flags in class B and the branch groups in class C therefore describe the remote at the time of the run.

It scans every tracked text file on `main`, skipping `.pdf`, `.tex` (generated from `.md`) and binary files. It reports six classes:
- **P:** local or temporary paths: `/tmp/`, `scratchpad`, `/root/`, `/home/user`.
- **B:** names of branches other than `main`.
- **C:** hex tokens of 7–40 characters that resolve to a commit not reachable from `main`.
- **O:** blob or tree ids not reachable from `main`.
- **R:** CI run ids (11 digits) and job ids (12 digits) on lines that also say "run", "job" or "actions/".
- **D:** 64-hex digests cited under `verification/`, compared with the sha256 of every file tracked at `main`.

Each citing file is classed by what keeps it unchanged:
- **receipt:** `verification/receipts/*.json`, kept by the V3 verifier;
- **native-record:** under the record directory a receipt-holding round declares, kept by `G13`;
- **legacy-record:** listed in `legacy-records.json`, kept by the `legacy-records` step;
- **mutable:** anything else.

## Findings

| class | count | where |
| --- | --- | --- |
| C: commits not reachable from `main` | 107 distinct commits, cited as 134 distinct tokens at 237 file:line locations in 43 files | 236 locations in native-round records; 1 in a mutable file, `verification/lean/oi_channel1_check.py:2` |
| O: blobs and trees not reachable from `main` | 75 distinct objects (71 blobs, 4 trees), cited as 77 tokens at 77 locations | all in native-round records |
| B: other-branch names | 7 mentions of 6 names: `tmp/bg2-predicted-20261015`, `tmp/bg3-predicted-20261015`, `tmp/bg3-predicted-reduced-20261015`, `tmp/bg3-predicted-reduced2-20261016` (twice), `draft/bg-3-scope-transfer-20261015`, `research/round7-channel-audit` | all in native-round records: the BG-2, BG-3 and OI-CHANNEL-1 preregistrations |
| P: local or temporary paths | 14 lines in 3 files | 8 in `.github/workflows/bg2-orientation-design.yml` (the workflow's own temporary files); 1 in L3B's `logs/V12.log:2` (native record), naming a local checkpoint root; 5 in act-26's `result.md` (legacy record), of which line 931 rests an item on "an exact computation in the execution's scratchpad" and lines 287–326 narrate scratchpad runs |
| R: CI run and job ids | 842 citations at 686 locations in 199 files: 479 locations in native-round records, 107 in receipts, 98 in legacy records, 2 in mutable files | 438 distinct run ids and 173 distinct job ids; the lowest run id is 35317349625, at SI-2's `preregistration.md:12` |
| D: digests | 1168 distinct 64-hex digests cited under `verification/`; 65 equal a file tracked at `main` | — |

**Mutable CI references.** Both are on one line, `verification/programmes/oi-qm/reconstruction/bekir-golomb-orientation-design/README.md:71`, which cites run 38534906783 twice. That README is mutable: under §A.42 it is corrected in place once the run's evidence is retained.

**What D does not say.** A 64-hex token that equals no tracked file is not necessarily a missing file: receipts carry computed digests (`governed_paths_digest`, `execution_delta_digest`), and records cite digests of texts that were never files. The audit does not classify the 1103 digests that equal no tracked file. Four of them are BG-3's cited logs, which were identified by comparison with files held in the session that ran the rounds; they are retained in this archive's `bg3/`, where the checker verifies each digest from the tree.

**Clean.** The 46 files of the manuscripts (`papers/*.md`, `book/*.md`), `AGENTS.md`, `verification/ROADMAP.md`, the census registry and the coverage ledger contain no reference of classes P, B, C or O, and no GitHub tree or blob URL off `main`.

### What the commits are

The 107 commits, grouped by the remote branches that hold them:
- 62 on development branches only;
- 26 on predicted-tree branches only (`*-predicted*`, `tmp/*`);
- 6 on research branches only;
- 4 on both a development and a research branch;
- 9 on other branches.

Every one is held by at least one branch. None is yet unreachable, so deleting those branches would orphan them.

**Their role is mostly design evidence.** Typical citations are "design evidence: core `4d7d71d6`, run 38205087980" and a development-run table listing a commit, a run and an outcome.

- The rounds' validity does not depend on them: each `VERDICT HOLDS` is decided from the receipt commit on `main`.
- They do support recorded hazard measurements and design claims, which the rule requires to be retained.

### The mutable reference, and a stated policy that conflicts with the rule

- **The mutable reference.** `verification/lean/oi_channel1_check.py:2` says "Decision rule: PREREGISTRATION.md, commit 78aa5b25", which is the round-7 registration on `research/overview` and `research/round7-channel-audit`.
- **The conflicting policy.** OI-CHANNEL-1's landed preregistration states: "The historical research archives are cited, not imported into main". That was a deliberate decision, and the new rule reverses it.

### Time limits

- **CI logs.** GitHub Actions keeps logs for the repository's retention period: at most 90 days for a public repository, 90 days by default.
  - The oldest of the 96 runs retained here was created on 2026-09-22. The date of the lowest cited run id is not in the tree.
  - The repository's actual setting was not readable from the session that made this audit.
- **Disposable branches.** Deleting any of the branches above orphans the commits it holds.

## Remedies, as decided by the owner on 2026-10-16

- **R1, the evidence-retention archive:** approved for preparation as a draft, for review only. Tranche 1 is this directory: the four BG-3 logs and the decisive CI evidence of 96 runs. It does not resolve classes C, O, B or P, or the CI runs it does not retain.
- **R2, keeping the cited commit ids resolvable:** deferred. The evidence is archived first; which original object identities are indispensable is decided afterwards. Tags alone do not meet the main-only requirement.
- **R3, re-pointing `oi_channel1_check.py`'s docstring:** approved as a separate correction after R1 lands, once the archived rule is verified to match the rule the round used.
- **R4, self-contained rounds:** approved. A frozen control plane pins the hashes of its required inputs, and the landed package contains the evidence needed to verify its conclusions (AGENTS §A.42).
