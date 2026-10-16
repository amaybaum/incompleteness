# Audit: references on `main` that depend on content not retained on `main`

Status: read-only audit of `main` at `fc5abade2a8ca381caedaa93c0441570fc060319`, made on 2026-10-16. No record was changed by it.

## Method

The audit is `offmain_audit.py`, in this directory, run as `offmain_audit.py fc5abade…` from a clone with every remote branch fetched. Its output is `offmain_audit-output.txt`. Unlike the checker, it needs git history and the remote branches, so the `exists` flags in class B and the branch lists in class C describe the remote at the time of the run.

It scans every tracked text file on `main`, skipping `.pdf`, `.tex` (generated from `.md`) and binary files. It reports five classes:
- **P:** local or temporary paths: `/tmp/`, `scratchpad`, `/root/`, `/home/user`.
- **B:** names of branches other than `main`.
- **C:** every hex token of 7–40 characters that resolves to a commit not reachable from `main`.
- **O:** blob or tree ids not reachable from `main`.
- **D:** 64-hex digests cited under `verification/` that equal the sha256 of no file tracked at `main`. Paths are taken exactly as git lists them; an earlier, manual version of this check added a directory prefix twice and briefly reported four retained files as missing.

Each citing file was then classified:
- **native-round record:** under a receipt-holding round's record directory, kept by G13;
- **legacy record:** listed in `legacy-records.json`;
- **mutable:** anything else.

## Findings

| class | count | where | mutable? |
| --- | --- | --- | --- |
| C: commits not reachable from `main` | 134 distinct commits, 156 citing file-references | 155 in native-round records (preregistrations, result notes, `controls.py`); 1 in `verification/lean/oi_channel1_check.py` | 1 mutable |
| O: blobs and trees not reachable from `main` | 77 (73 blobs, 4 trees), 82 citing file-references | all in native-round records | none |
| B: other-branch names | 7 mentions: `tmp/bg2-predicted-20261015`, `tmp/bg3-predicted-20261015`, `tmp/bg3-predicted-reduced-20261015`, `tmp/bg3-predicted-reduced2-20261016` (twice), `draft/bg-3-scope-transfer-20261015`, `research/round7-channel-audit` | BG-2, BG-3 and OI-CHANNEL-1 preregistrations | none |
| P: temporary paths as evidence | 2 records | act-26 `result.md:931` rests an item on "an exact computation in the execution's scratchpad" (lines 287–326 narrate scratchpad runs); L3B `logs/V12.log:2` names a local checkpoint root `/root/.l3b_ckpt_v12` | none (legacy record; native-round record) |
| D: digests | 1168 distinct 64-hex digests cited under `verification/`, of which 65 equal a file tracked at `main` | most of the remainder are computed digests (receipt and governed-path digests); 4 named logs held only in a session scratchpad (below) | — |
| CI run references | 362 references in 181 files; about 477 distinct run or job ids | throughout the records; the oldest cited run is 35317349625, 2026-09-18 | — |

**Clean.** Manuscripts (`papers/*.md`, `book/*.md`), `AGENTS.md`, `verification/ROADMAP.md`, the coverage ledger and the census registry contain none of classes P, B, C or O, and no GitHub URL into a branch.

### What the commits are

Grouped by the branches that still hold them:

- 65 on development branches (`claude/*-dev`, `dev-equivalence/*`).
- 48 on predicted-tree branches (`claude/*-predicted`, `tmp/*`).
- 7 on research branches (`research/overview`, `research/round7-channel-audit`, `research/equivalence`, `research/conscious-observation-loop`).
- 4 on both a development and a research branch.
- 10 on other design or controls branches.

Every one is still held by at least one branch. None is yet unreachable, so deleting those branches would orphan them.

**Their role is mostly design evidence.** Typical citations are "design evidence: core `4d7d71d6`, run 38205087980" and a development-run table listing a commit, a run and an outcome.

- The rounds' validity does not depend on them: each `VERDICT HOLDS` is decided from the receipt commit on `main`.
- They do support recorded hazard measurements and design claims, which the rule requires to be retained.

### The one mutable reference, and a stated policy that conflicts with the rule

- **The mutable reference.** `verification/lean/oi_channel1_check.py:2` says "Decision rule: PREREGISTRATION.md, commit 78aa5b25", which is the round-7 registration on `research/overview` and `research/round7-channel-audit`.
- **The conflicting policy.** OI-CHANNEL-1's landed preregistration states: "The historical research archives are cited, not imported into main". That was a deliberate decision, and the new rule reverses it.

### Evidence that was held only in a session scratchpad

Nine cited digests match files in the scratchpad. Five of those files are also retained on `main`: the BG-2 design outputs `exact-output.json`, `independent-output.json` and `quoted-family-output.json`, and BG-3's frozen `edit-ledger.json`. A sixth match, `e3b0c442…`, is the digest of the empty file. **Four were held nowhere but the scratchpad. Tranche 1 retains them under `bg3/`:**

| file | sha256 | cited by |
| --- | --- | --- |
| BG-3 E bridge-log tail, job 116826161407, last 4999 lines | `84de2bc0…` | `verification/receipts/BG-3.json` (E's candidate entry) |
| BG-3 E design-run log, job 116831668411 | `bf1ab945…` | `verification/receipts/BG-3.json` |
| BG-3 corrected-design bridge-log tail, job 116805436638 | `9f1abf3c…` | BG-3 preregistration |
| BG-3 first-design bridge-log tail, job 116761232088 | `e77b0ded…` | BG-3 preregistration |

The full job logs these tails were cut from are still downloadable from GitHub until the retention limit.

### Time limits

- **CI logs.** GitHub Actions keeps logs for the repository's retention period: at most 90 days for a public repository, 90 days by default.
  - The oldest cited run's logs are still downloadable today. Under a 90-day limit they expire around 2026-12-17, and later runs expire in sequence.
  - The repository's actual setting was not readable from this session.
- **Disposable branches.** Deleting any of the branches above orphans the commits it holds.
- **Scratchpad.** It does not outlive the session.

## Remedies, as decided by the owner on 2026-10-16

- **R1, the evidence-retention archive:** approved for preparation as a draft, for review only. Tranche 1 is this directory: the four BG-3 logs and the decisive CI evidence of 96 runs. It does not resolve the remaining classes.
- **R2, keeping the cited commit ids resolvable:** deferred. The evidence is archived first; which original object identities are indispensable is decided afterwards. Tags alone do not meet the main-only requirement.
- **R3, re-pointing `oi_channel1_check.py`'s docstring:** approved as a separate correction after R1 lands, once the archived rule is verified to match the rule the round used.
- **R4, self-contained rounds:** approved. A frozen control plane pins the hashes of its required inputs, and the landed package contains the evidence needed to verify its conclusions (AGENTS §A.42).
