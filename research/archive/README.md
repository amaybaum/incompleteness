# research/archive — the shared historical record of the OI research programme (read-only)

This directory preserves the off-repository working records of every research round and thread run against the
certified chain, from the V3 governance rounds through the PT programme's six stages (Q-EX-FULL). It is the
*archival* branch of the research tree: nothing here is modified after it lands; corrections and continuations go
to the thread branches (`research/bridge`, `research/countermodels`, `research/origin`, `research/equivalence`),
and the live overview lives on `research/overview`. The certified chain (`main`) is untouched by any of this.

Base of the records: the certified commit **L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`** (`main`, KT4-PREM-1
landed) for the PT stages 1–6; earlier records name their own base (`0f2687b7`, `bcbc516f`, …) in their notes.

## Provenance and integrity

- `MANIFEST.sha256` — sha256 of every file in this directory as copied (paths relative to `research/archive/`).
  Verify with `cd research/archive && sha256sum -c --quiet MANIFEST.sha256`.
- `EXCLUDED-LARGE.sha256` — files above the size limit (5 MiB text-like, 2 MiB binary), with size and sha256; they
  remain on the originating container and are recomputable from the scripts beside them.
- `EXCLUDED-SNAPSHOTS.txt` — directories that were copies of the repository tree (bases of read-only rounds); the
  records that used them cite the base commit, which is on `main`.
- `WORKTREES.md` — the 167 git worktrees that lived beside the records, with branch, HEAD, uncommitted-change count
  and whether the HEAD is reachable from an `origin` branch; `worktree-dirty-capture/` holds the uncommitted diffs
  and untracked files of the nine worktrees that had any.
- `pack_archive.py` — the packer that produced this directory (rules R1–R5 in its header).
- Every stage archive under `evidence/` carries its own manifest; every thread directory carries its own
  `RESULT.md` with the sha256 of every file it wrote, and every coordinator audit lists the hashes it verified.
  Replays recorded as "byte-identical" were produced with `python3 -I -B` on the originating container.

## Status vocabulary used throughout the records

[K] certified at L (Lean kernel, file:line) · [D] design module (not certified) · [W] written argument · [X] exact
computation (script + output + replay) · [A] audited stage record cited · [U] unsourced · [L] unverified literature.
Verdict labels: DERIVED / CONDITIONAL (on a named item at its status) / INDEPENDENT / UNRESOLVED; countermodel
labels UNIQUE / EXOTIC-X (explicit) / EXOTIC-E (existence) / EXCLUDES-KNOWN. Nothing in this archive changes a
certified status: consistency-axis work only (AGENTS.md §A.23).

## Index (top-level entries, in the order of the programme)

### The PT programme (stages 1–6, base L = 9f9f8257)

| entry | content |
|---|---|
| `pt/PROTOCOL*.md` + `.sha256` | the stage protocols and amendments (PROTOCOL, amendments 1–2; STAGE2, STAGE2-DS, STAGE3, STAGE4, STAGE5 + amendment 1, STAGE6 + amendments 1–2), each with its sidecar hash |
| `pt/A B C D` | stage 1 threads (premise audit; audited in `pt/INTEGRATION-REVIEW.md`) |
| `pt/S2 S3 DS` | stage 2 threads (pair system from data; composition consistency; double-slit review); `pt/INTEGRATION-ADDENDUM-STAGE2.md` |
| `pt/U X` + `pt/audit/X`, `pt/audit/reviews/NS` | stage 3 (Q-SD: exotic self-dual cones at levels (i)/(ii); the NS review); `pt/INTEGRATION-NOTE-STAGE3.md` |
| `pt/Y Z` + `pt/audit/Y`, `pt/audit/Z` | stage 4 (Q-EX: exclusion dichotomy, countermodels); `pt/INTEGRATION-NOTE-STAGE4.md` |
| `pt/D5 C5` + `pt/audit/D5`, `pt/audit/C5` | stage 5 (Q-EX-BRIDGE: no principle at L derives (b)); `pt/INTEGRATION-NOTE-STAGE5.md` |
| `pt/I1 I2 I3 I4 G6 R6 T6` + `pt/audit/stage6-inputs/{I,G,R,T}-audit` | stage 6 (Q-EX-FULL: 633-record inventory, NO-MEET graph, countermodel reassessment, test of (b): INDEPENDENCE); `pt/INTEGRATION-NOTE-STAGE6.md` |
| `pt/audit/stage*-inputs/OWNER-*` | the owner's notes that directed each stage (verbatim) |
| `pt/audit/STAGE3-RELAUNCH-LOG.md`, `pt/STAGE2-LAUNCH-LOG.md`, `pt/STAGE3-LAUNCH-LOG.md`, `pt/DS-LAUNCH-LOG.md` | launch and close logs with timestamps and hashes |
| `pt/inputs/`, `pt/*.manifest.sha256` | frozen inputs and their manifests |
| `evidence/` | the stage evidence archives `pt-stage{2..6}-evidence.tar.gz` with manifests, and the records snapshot taken at the stage-6 launch |
| `drafts/` | the coordinator's drafts, build scripts (`build_stage*_evidence.sh`), independent checks and this packer |

### The K programme and the governed rounds before PT (working records; the certified results are on `main` under `verification/`)

| entry | round / thread |
|---|---|
| `a30`–`a40`, `audit40`, `a41draft`, `a41exec`, `a42`, `a45`, `p2`, `p35`, `p4`, `d41` (snapshot, excluded) | A30–A45 (Diţă hull, torus locus, census, support minimality, bridge) working directories: pre-freeze measurements, discovery notes, probes, control planes |
| `v36`–`v39`, `v310`–`v314`, `ledger`, `record`, `rcpt`, `ci1`, `ciperf`, `ciperf2` | V3 governance rounds (V3-6 … V3-14), the receipts/CI infrastructure rounds (CI-1, CI-PERF-1, CI-RECEIPTS-1) and their local simulations |
| `round1`, `round2`, `round2cc`, `level3`, `level3b`, `frontier`, `select`, `kirc` | the premise ledger, Level 3A/3B, CC-1/CC-2, the K/I/R/C assumption audit, SELECT thread |
| `k-infinity`, `k-roadmap`, `k0`, `kinf1-freeze`, `kinf2`, `kinf2-freeze`, `nb1-freeze`, `og1`, `og1ctl.py`, `iip1`, `cmp1`, `opact`, `opact1`, `drive`, `oistage`, `rank`, `quotient` | K∞ rounds (KINF-1/2, NB-1, OG-1, IIP-1, CMP-1, OPACT-1) and the read-only investigations (OPACT, DRIVE, OI-STAGE, RANK, QUOTIENT) |
| `dim1_*.lean`, `kn`, `consc1`, `eff1r`, `k1b`, `k1c`, `k1st`, `k2`, `k2d`, `k2c`, `k2_replay_*.txt`, `sa`, `sa_replay_*.txt`, `ss`, `ac`, `pthread`, `kg`, `twole`, `pnot`, `odd`, `ktd`, `rcs`, `possep`, `relc`, `relt`, `bal`, `indep`, `threads`, `wave2`, `dthread`, `g3thread`, `g3replay` | DIM-1, Kₙ census, CONSC-1/2, EFF-1, K1-BRIDGE-1, KTRANS-DENSE-1, K1-SHARP-TESTS-1, K2-GUARD-1, K2 / SA / SS / K2C / AC / P threads, TWO-LE, PARITY-NOT-1, ODD-CHAR-1, RELC-SELECT-1, POS-SEP / REL-C / REL-T, Balanced-n5, wave-2 threads N/O/P/R, D and G3 threads |
| `eq`, `eq2`, `eq3`, `eq4`, `eq5`, `eqreview` | the EQ threads A–E, EQ2 A/B/C, EQ3-P (KT∞), EQ4-P/-F/-SIX/-SOURCE, EQ5-PREM, with the coordinator's audits and syntheses |
| `kt4prem` | KT4-PREM-1 (the four-token premise audit round; landed as L) — control plane, simulated chain, controls |
| `a41h.py`, `a42p.py`, `build_ledger41.py`, `overrides41.py`, `v314_*.py`, `extract_v314.py`, `proc_logs.py`, `sec7.py`, `explore.py`, `o.py`, `tools/summ.py`, `wait*.sh`, `*.log`, `*.txt`, `*.md` at the root | coordinator helper scripts, build/CI logs and notes of the rounds above (self-describing by name and header) |
| `mathlib-ref`, `mathlib433`, `ml-v433-src`, `ml4`, `pd` | vendored Mathlib references and a pandoc wheel — not copied (R3) |

Where a directory's purpose is not obvious from this table, its own `RESULT.md`, `NOTES.md`, `LEDGER.md` or
`README` states it; every thread record names the protocol it ran under and the commit it read.

## What this archive is not

It is not a certification record and contains no governed artifact: receipts, seals and manuscripts live on
`main` under their own gates. Nothing here was merged into the certified chain, and nothing here should be: a
result that is ready for a governed round is listed as such in `research/OVERVIEW.md` on `research/overview`, and
enters `main` only through the §A.39 lifecycle with separate authorization.
