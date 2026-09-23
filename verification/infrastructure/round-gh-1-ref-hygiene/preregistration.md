# Repository hygiene round GH-1 — history independence, stale refs retired, forward rule installed: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. No lint,
baseline, gate step, `AGENTS.md` text, status correction or ref deletion exists at the time it is
written; each is an execution object and is created only after the certified merge of this file.

## The commit vocabulary this freeze uses, fixed first

- `D` — the drafting snapshot: `8f60d841034370b9daa78ac347465281ca1bee76`, the certified head of
  `main` after the `CV-2` halt record (push run 35852106002, all five jobs green). Every measurement
  in this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  SHA until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before
  the merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from `B`.
- `L` — the landing merge, first parent current green `main`, second parent exactly `E`.

## What `GH-1` is, and what it deliberately is not

`GH-1` is a non-sealing infrastructure round with three jobs:

1. **Show that the repository's required checks do not depend on side-branch history**: every
   required check passes in a repository that holds `main`'s complete history and no other ref
   or object, including the one guard check that names an unlanded commit.
2. **Retire the stale remote refs**: the ten remote branch heads, other than `main` and `dev`,
   present at `D`; they are deleted only after (1) holds, and the relevant clean-clone checks are
   repeated against the remote after deletion.
3. **Install the forward rule**: durable artifacts do not depend on temporary refs, stated in
   `AGENTS.md` and enforced for its textual half by a tree-local lint with a grandfather baseline.

### Boundaries, frozen

- **No historical rewrite.** No merged preregistration, amendment, result, closure, census, tag
  map, seal record, certificate or other historical artifact is edited because it contains an
  obsolete branch name or a statement that was true when it was made. Every occurrence present at
  `B` is grandfathered in place.
- **No durable inventory of ephemeral refs.** Neither this file, nor the result, nor the lint's
  baseline enumerates a temporary branch name or an unreachable attempt SHA. The concrete deletion
  list is an execution-time scratch inventory and never enters the repository. This file records
  counts and one digest of that inventory, which verifies it and does not enumerate it.
- **`dev` is out of scope.** It is not deleted, moved or otherwise touched.
- **The ten stale refs are in scope, and none is deleted before `GH1-1` holds.**

### What `GH-1` is not

`GH-1` carries none of the next verifier architecture (`V3`). The following are explicitly not
part of this round and nothing in it prepares, anticipates or constrains them: chronology anchors,
receipt or state-model design, governed-path-set digests, landing-delta semantics, and the
migration or retirement of `V1` or `V2`. `GH-1` adds no guard clause, changes no verifier text,
writes no seal record, prospective declaration or manifest-baseline change, and adds no conformance
vector. It does not re-open `CV-2`.

## Measurements at `D` that shape the round

### `F1` — the remote refs

At `D` the remote carries twelve branch heads: `main`, `dev`, and ten others. `dev` is contained in
`main`. Of the ten, one is fully contained in `main` and nine carry side-only commits: thirty
distinct commits in total not reachable from `main`. Exactly one of the ten carries the object
`_SI3_ATTEMPT1` names. No pull request is open. None of the ten tips is `D` or a descendant of
`D`.

**The inventory, FROZEN as a procedure.** The in-scope set and its digest are computed from the
remote alone, after `git fetch origin` has made every listed tip present locally:

1. Read `git ls-remote --heads origin`; each line is `<tip>` TAB `<ref>`.
2. Drop the lines whose `<ref>` is exactly `refs/heads/main` or `refs/heads/dev`.
3. For every remaining line, `git cat-file -e <tip>^{commit}` must succeed; if any fails, the
   outcome is `INVENTORY-DRIFT`.
4. Drop the lines whose `<tip>` is `D` or a descendant of `D` (`git merge-base --is-ancestor D
   <tip>` exits 0). This excludes this round's own branches, which descend from `D`.
5. Serialize each remaining line as the bytes `<ref>`, one space (0x20), `<tip>` as 40 lowercase
   hex digits, one line feed (0x0A); `<ref>` is the full ref name exactly as step 1 prints it.
   Sort the lines by byte order (`LC_ALL=C sort`) and concatenate them with nothing before, between
   or after.
6. The digest is the SHA-256 of those bytes, as 64 lowercase hex digits.

As one command, with `D` set to the drafting snapshot's SHA:

```
git ls-remote --heads origin | while read -r tip ref; do
  case "$ref" in refs/heads/main|refs/heads/dev) continue ;; esac
  git merge-base --is-ancestor "$D" "$tip" && continue
  printf '%s %s\n' "$ref" "$tip"
done | LC_ALL=C sort | sha256sum
```

Step 3 is checked separately, before the command runs. At `D` the procedure yields ten lines and
the digest `116b045af6066dc37edcfa3ae7d749eabd518241de98a15389491af4d7e375ec`, and re-reading the
remote when this file was committed yielded the same digest.

### `F2` — mechanical dependencies on objects outside `main`

Over the code and data files at `D` (extensions `.py`, `.json`, `.yml`, `.yaml`, `.sh`, `.toml`,
`.cfg`): 446 distinct full-length hex literals, of which 185 resolve to commits and exactly one
resolves to a commit outside `main`'s history — the value of `_SI3_ATTEMPT1` in
`verification/lean/edge_rigidity_probe.py`, read by one check, `P12 attempt 1 unreachable`, which
asks `git merge-base --is-ancestor` and passes when the object is absent or present and unreachable.
Of 1721 abbreviated literals of 12 to 39 hex digits, 25 resolve to commits and none lies outside
`main`. Temporary-branch tokens in code and data files: five, in two files, all string text — the
guard's checks of frozen sentences, and one note in `verification/lean-manuscript-census.json` —
and none resolved as a ref.

### `F3` — the main-only replay at `D`

A repository built from a bundle of `main` alone (`git bundle create <file> refs/heads/main`, then
`git clone <file>`): HEAD `D`, 2710 commits (equal to `main` in the full checkout), not shallow, no
alternates, refs only `main` and its remote-tracking ref; the nine side-only tips and the object
`_SI3_ATTEMPT1` names are absent, the two contained tips present. In it, at `D`:

| check | result |
|---|---|
| guard `verification/lean/edge_rigidity_probe.py` | `ALL CHECKS PASS`, 105 PASS, 0 FAIL; `R7-SI3` PASS with `P12 attempt 1 unreachable` true on an absent object |
| `tools/certificate_verifier.py --self-test`, `--mode authoritative` | OK; 89 vectors executed, 0 mismatches, exact |
| control-plane self-tests, lint self-test, `--mode B --ref HEAD` | pass |
| Lean kernel check, the six core files | pass (toolchain `v4.33.0`) |
| the workflow's numerical probes (44 files, the guard among them) and foundations probes (12 files) | all pass |
| `tools/release_gate.py` | PASS, 19 of 19 steps, `lean-axioms` over an `OIBridge` built in the main-only tree |

The Mathlib bridge's third-party packages were supplied from the pinned `lake-manifest.json`
revisions, identical in both checkouts; `OIBridge` itself was built from the main-only tree.

### `F4` — the tree-local token inventory

With the lint pattern frozen below, the tracked text files at `D` carry 29 temporary-branch tokens
in 17 files, 12 distinct, all under `verification/`: fifteen frozen round artifacts
(preregistrations, amendments, results and one closure), the guard (4) and the census registry (1).
The 29 occurrences fall on 29 distinct (path, line-hash) keys, each of multiplicity one. No tracked
file outside `verification/` carries one; `.gitignore`'s worktree entry does not match.

### `F5` — mutable status surfaces

`README.md`, `verification/README.md`, `verification/ROADMAP.md`, `AGENTS.md` and
`verification/lean-manuscript-census.json` carry no present-tense statement that a temporary
branch exists, is preserved, or must be consulted; the census note is a past-tense record of what
was not cited. Retiring the refs therefore makes no mutable status statement false.

### `F6` — the planned edits against the guard's live reads

A scratch commit on `D` carrying the round's planned edits — a stub lint and baseline under
`tools/`, the gate step, a new final section in `AGENTS.md`, and a result file in this round's
directory — leaves the guard at 105 PASS, 0 FAIL with a verdict map identical to `D`'s, and the
verifier authoritative OK. The same commit with a round certificate `verification/certificates/GH1.json`
added, whose base the verifier cannot derive, turns the verifier red
(`GH1:base:merge-disagreement`) and `R7-CV1` red through its bridge steps and `verifier-shadow-ok`;
`R7-CV1`'s census contracts do not change. Neither scratch commit exists outside the drafting
session.

## The round's shape, in `§A.37`'s terms

Non-sealing: `E` → `L`, no pin. `GH-1` writes no manifest record, no prospective declaration and
no baseline change, adds no guard clause, and writes no round certificate or attestation (reading
`R1`). Its chronology is the executor's check at `E` that every commit of `git rev-list E ^B`
descends from `B` and that the execution branch has absorbed no later `main`, recorded in the
result, followed by exact-head review; `GH-1` carries no mechanical chronology control of its own
(reading `R2`).

## The forward rule, FROZEN as text

At stage 3 `AGENTS.md` gains exactly the following section, appended after the last line of
`§A.37`, and nothing else in the file changes:

> ## §A.38 Durable artifacts do not depend on temporary refs
>
> Durable repository artifacts must not require preservation, existence, or reachability of
> temporary branches or unlanded Git objects. Failed attempts are recorded by their measured facts,
> not by a branch that must continue to exist.
>
> A temporary branch is any branch other than `main` and `dev`; an unlanded object is a commit not
> reachable from `main`. A durable artifact — a preregistration, amendment, result, closure,
> census, tag map, seal record, certificate, guard, verifier, workflow or registry — may state what
> an attempt measured: counts, verdicts, the blob identities of content that landed, and the
> outcome. It does not name the branch that carried the attempt as a place to look, does not pin an
> unlanded commit as evidence, and carries no check whose verdict changes when such a branch is
> deleted or such an object is garbage-collected. A concrete deletion list is execution-time
> scratch.
>
> Enforcement is tree-local. `tools/ephemeral_ref_lint.py` (release-gate step `ephemeral-refs`)
> reads the tracked files of the checked-out tree and never asks git whether a ref or object
> exists. It finds branch names under the agent prefixes `claude`, `codex`, `chatgpt`, `roadmap`,
> `copilot` and `dependabot`, bare or after `refs/heads/`, `refs/remotes/origin/` or `origin/`, and
> compares them with `tools/ephemeral_ref_baseline.json`, which grandfathers the occurrences present
> when this rule was adopted, keyed by path and the SHA-256 of the whole line, never by line
> number, and carrying no branch name. An occurrence beyond its key's grandfathered count fails; a
> grandfathered occurrence removed passes. An entry is never added to the baseline, and a
> grandfathered artifact is not rewritten to remove one. The lint detects temporary-branch names
> leaking into tracked content; it is not an inventory of the remote and establishes nothing about
> which branches exist or have been deleted. The rule's other half, unlanded objects,
> is not visible to a tree-local check; it is held by review, and was established for the tree at
> `GH-1`'s base by replaying every required check in a repository holding `main`'s history alone.
>
> Adopted in the hygiene round `GH-1`, which found twenty-nine temporary branch names in
> seventeen historical files and one guard check reading an unlanded commit, showed that check
> passing with the object absent, and retired ten stale remote branches.

## The lint, FROZEN as a specification

- **Files.** `tools/ephemeral_ref_lint.py`, standard library only; `tools/ephemeral_ref_baseline.json`.
- **Scan set.** Every path `git ls-files` lists at the repository root, read from the working
  tree; a file whose first 8000 bytes contain a NUL byte is binary and skipped; text is decoded as
  UTF-8 with replacement. No exclusions. Untracked files, including `.claude/worktrees/`, are not
  read.
- **Pattern.**

  ```
  (?<![\w./-])(?:(?:refs/heads|refs/remotes/origin|origin)/)?(claude|codex|chatgpt|roadmap|copilot|dependabot)/[A-Za-z0-9][A-Za-z0-9._/-]*
  ```

- **Key.** `(path, sha256(line))`, where `line` is the full line text without its terminating
  newline; the value is the number of matches on that line, summed over identical lines of the
  file.
- **Baseline.** JSON object `{"schema": "ephemeral-ref-baseline", "version": 1, "pattern": <the
  pattern above>, "entries": [{"path": ..., "line_sha256": ..., "count": n}, ...]}`, entries sorted
  by `(path, line_sha256)`. It is generated once, at stage 3, from the tree at `B` by the tool's
  `--emit-baseline` mode, and must equal `F4`: 29 entries, 17 paths, counts summing to 29.
- **Verdict.** FAIL iff some current key's count exceeds its baseline count (a key absent from the
  baseline counts as zero), or the baseline's `pattern` differs from the tool's. Baseline keys whose
  current count is lower are reported as retired and pass. Output names the path and the line
  number of each new occurrence, never a token in the gate summary line.
- **Self-test.** `--self-test`, run by the gate step before the tree check, drives the real scan
  and comparison over a temporary git repository through: (a) an unchanged tree against its own
  baseline passes; (b) a new token in a new file fails; (c) a second identical grandfathered line
  in the same file fails; (d) a grandfathered line moved to another line number passes; (e) a
  grandfathered line removed passes and is reported retired; (f) a grandfathered line edited with
  its token kept fails; (g) a grandfathered line copied into another file fails; (h) the
  `refs/heads/` and `origin/` forms are detected; (i) a dotted path segment such as a hidden
  worktree directory is not; (j) an untracked file carrying a token is not read; (k) a baseline
  with a changed `pattern` fails.
- **Gate step.** `("ephemeral-refs", [sys.executable, "tools/ephemeral_ref_lint.py"])`, inserted
  immediately after `control-plane-lint` in `tools/release_gate.py` with a comment of at most four
  lines; no other change to that file.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `GH1-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` — stop before any execution object |
| `GH1-1` | `HISTORY-INDEPENDENT` — in a repository built from `B` with `main`'s complete history and no other ref: the nine side-only tips and the object `_SI3_ATTEMPT1` names absent (`git cat-file -e` fails for each); guard `ALL CHECKS PASS` with `D`'s 105 verdicts; verifier self-test and authoritative OK; control-plane self-tests, lint self-test and `--mode B`; release gate PASS; Lean kernel check; numerical and foundations probes; `R7-SI3` PASS with `P12 attempt 1 unreachable` true | `HISTORY-DEPENDENT` — any of these red; the dependency is recorded, no ref is deleted, the round stops |
| `GH1-2` | `REFS-RETIRED` — immediately before any deletion, `F1`'s inventory procedure is re-run against the remote and yields exactly `F1`'s digest, and the lines it yields are the deletion list; after the owner deletes exactly those heads, `git ls-remote --heads` shows none of them, `main` and `dev` at their pre-deletion tips; a fresh clone of the remote holds none of the nine side-only tips nor the object `_SI3_ATTEMPT1` names, and in it at `B` the guard, verifier authoritative, control-plane checks and release gate pass as in `GH1-1` | `INVENTORY-DRIFT` (step 3 fails or the recomputed digest differs: stop, report counts, delete nothing) or `REMOTE-DEPENDENT` (a post-deletion check red: stop and report) |
| `GH1-3` | `FORWARD-RULE-INSTALLED` — the `§A.38` text byte-equal to the frozen text; the lint and baseline as specified, the baseline equal to `F4`; lint self-test and tree check pass; the gate PASS with the new step; the guard's 105 verdicts unchanged; verifier authoritative OK | `RULE-BLOCKED` — any of these red; stop |
| `GH1-4` | `HISTORY-UNTOUCHED` — `git diff --name-status B E` deletes nothing, modifies only the files the mutation budget names, and adds only the three files it names; each of `F4`'s seventeen files has its `B` blob at `E` | `HISTORY-TOUCHED` — stop |
| `GH1-5` | `STATUS-ACCURATE` — after the deletion, every mutable, unpinned status surface is re-read and each present-tense statement made false is corrected in place, and only those; a frozen or pinned file is never edited | `STATUS-BLOCKED` — a false statement sits in a frozen or pinned file where it cannot be corrected: record it, do not edit, stop for the owner |
| `GH1-6` | `SCOPED` — at `E`: no guard, verifier, workflow, seal, certificate, attestation, conformance-vector or live-policy change; `dev` at its `D` tip; no object of reading `R1`'s declined options present | `SCOPE-EXCEEDED` — stop |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `GH1-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `GH1-1` | `HISTORY-INDEPENDENT` | strong | `F2`, `F3` |
| `GH1-2` | `REFS-RETIRED` | strong, conditional on the owner's deletion | `F1`; the one object outside `main` any check reads passes when absent (`F3`) |
| `GH1-3` | `FORWARD-RULE-INSTALLED` | strong | `F4`, `F6` |
| `GH1-4` | `HISTORY-UNTOUCHED` | strong | the budget writes none of `F4`'s files |
| `GH1-5` | `STATUS-ACCURATE` with no correction from the ref retirement and exactly one, reading `R1`'s | moderate | `F5`; the sweep covered five surfaces |
| `GH1-6` | `SCOPED` | strong | the shape declares none of those objects |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome; it is HALTED at
the first stop outcome, with the targets not reached recorded as such.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `GH1-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `GH1-1` | none | main-only replay at `B`; report to the owner with the scratch inventory, off-repository |
| 2 | `GH1-2` | none | the inventory re-run against the remote and its digest matched; the owner deletes exactly the listed heads; post-deletion checks against the remote |
| 3 | `GH1-3` | one: the lint, the baseline, the gate step and `§A.38` | lint self-test and tree check, gate, guard, verifier |
| 4 | `GH1-5` | one if any correction, else none | the status sweep after deletion |
| 5 | `GH1-4`, `GH1-6` | one: the result note; its commit is `E` | the closing checks at `E`, then the exact-head pull request |

No ref is deleted before stage 1's checkpoint is reported green. The session that executes the
round cannot delete remote refs (the attempt returns HTTP 403); the owner performs stage 2's
deletion.

## The mutation budget

- **Added:** `tools/ephemeral_ref_lint.py`, `tools/ephemeral_ref_baseline.json`,
  `verification/infrastructure/round-gh-1-ref-hygiene/result.md`.
- **Modified:** `AGENTS.md` (the `§A.38` section, appended); `tools/release_gate.py` (the one
  step and its comment); files that `GH1-5` corrects, each a mutable, unpinned status surface, each
  correction one sentence.
- **Deleted:** nothing.
- **Never written:** the guard, the verifier, `.github/workflows/verify.yml`, anything under
  `verification/seals/`, `verification/certificates/`, `verification/programmes/`,
  `verification/audits/`, any other round's directory, `papers/`, `book/`, the Lean trees, and each
  of `F4`'s seventeen files.

The result note records counts, outcomes and the SHAs of `B` and of landed commits only. It names
no temporary branch and no unlanded commit, and passes the lint it installs.

## What no outcome of this round licenses

1. Rewriting or annotating any historical artifact that names a temporary branch.
2. Treating the digest in `F1`, or any count, as a list of what was deleted.
3. A claim that the unlanded-object half of `§A.38` is mechanically enforced.
4. Any statement about `V3`, its chronology anchor, receipts, governed-path digests or landing
   deltas, or about the retirement of `V1` or `V2`.
5. Deleting `dev`, or any ref created after `D`, under this round.

## Hazards

- **`H1` — refs outside the default refspec.** The hosting service keeps its own pull-request refs,
  which a default clone does not fetch and this round cannot delete; objects they reach may remain
  retrievable. `GH1-1` measures independence without them, and `GH1-2` uses a default clone.
- **`H2` — inventory drift.** A stale head may move, vanish or be joined by another between `D`
  and execution. Any such change alters the recomputed digest and stops the round with nothing
  deleted. Heads whose tips descend from `D`, this round's own among them, are excluded by step 4,
  are out of scope, and are reported by count only.
- **`H3` — Mathlib provisioning.** A main-only clone has no Mathlib build. The replay supplies the
  third-party packages at the manifest's pinned revisions and builds `OIBridge` from the main-only
  tree; that `OIBridge` is not reused from the full checkout is part of the check.
- **`H4` — the baseline as an escape hatch.** A tree-local baseline can be regenerated to
  grandfather a new occurrence. `§A.38` forbids adding entries; review of any diff to the baseline
  is the defence.
- **`H5` — a lint that reads its own specification.** This file and the result contain the prefix
  list and the pattern; neither contains a match, which the lint's first run at stage 3 confirms.

## Files

### Files this round reads AND writes

`AGENTS.md`, `tools/release_gate.py`, and `GH1-5`'s corrections, if any.

### Files this round reads and MUST NOT write

The guard, `tools/certificate_verifier.py`, `.github/workflows/verify.yml`, `README.md`,
`verification/ROADMAP.md`, `verification/lean-manuscript-census.json`, and the fifteen other
files `F4` counts.

### Name freedom, at `D`

`round-gh-1`, `ref-hygiene`, `R7-GH1`, the word `GH1`, `gh1_`, `ephemeral_ref`, `ephemeral-ref`
and `§A.38` occur nowhere in the tree at `D`.

## Preconditions

```control-plane-preconditions
d: 8f60d841034370b9daa78ac347465281ca1bee76
merged: false
frozen-blob: verification/lean/edge_rigidity_probe.py 2eab600fb8cd078b3dd0f3867a6e7420cfc2b79f
frozen-blob: tools/certificate_verifier.py a475408874b850f34c31eca5e1cb4ab549601f38
frozen-blob: tools/release_gate.py ca851befa24028655ecbbee85e53482bc186eb82
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
frozen-blob: .github/workflows/verify.yml 3ed93ea20bb42f986850d008d5a5edc93a4b7e34
frozen-blob: verification/README.md b585d921eb85b84afb0148266848bc4f0df43270
frozen-blob: verification/ROADMAP.md f26f7c1c8d275539bccb21d6faa2e882abc6dcf8
frozen-blob: README.md e1aca1e9c916f23227e5f06dfff6a9c3adab18a8
# row 1: name freedom, drafting-time facts
{"id": "d1-dir-free", "scope": "D", "check": "git grep -l -- 'round-gh-1' $D", "expect": "empty"}
{"id": "d1-suffix-free", "scope": "D", "check": "git grep -l -- 'ref-hygiene' $D", "expect": "empty"}
{"id": "d1-tag-free", "scope": "D", "check": "git grep -l -- 'R7-GH1' $D", "expect": "empty"}
{"id": "d1-stem-free", "scope": "D", "check": "git grep -l -w -- 'GH1' $D", "expect": "empty"}
{"id": "d1-prefix-free", "scope": "D", "check": "git grep -l -- 'gh1_' $D", "expect": "empty"}
{"id": "d1-tool-free", "scope": "D", "check": "git grep -l -e 'ephemeral_ref' -e 'ephemeral-ref' $D", "expect": "empty"}
{"id": "d1-section-free", "scope": "D", "check": "git grep -l -F -- '§A.38' $D", "expect": "empty"}
# row 2: the trees at D
{"id": "d2-seals-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/seals)\" = ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125", "expect": "exit0"}
{"id": "d2-certificates-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/certificates)\" = 8aa1a8fac388b625653803f7dad7c2fdabb12cc4", "expect": "exit0"}
{"id": "d2-tools-tree", "scope": "D", "check": "test \"$(git rev-parse $D:tools)\" = 8dabe979dffeed607d886c98ca91485cb9a64c69", "expect": "exit0"}
{"id": "d2-infra-tree", "scope": "D", "check": "test \"$(git rev-parse $D:verification/infrastructure)\" = e3b4f2596af9fbd020b451e07643aca9d06b0c3a", "expect": "exit0"}
# row 3: provenance, D to B: D an ancestor, and nothing but this file between them
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -e 'verification/infrastructure/round-gh-1-ref-hygiene/preregistration.md'", "expect": "empty"}
{"id": "db3-seals-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/seals)\" = ea7b7161fa84d96d8bc5ae03b0c8aa58e1879125", "expect": "exit0"}
{"id": "db3-certificates-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:verification/certificates)\" = 8aa1a8fac388b625653803f7dad7c2fdabb12cc4", "expect": "exit0"}
{"id": "db3-tools-tree", "scope": "D->B", "check": "test \"$(git rev-parse $REF:tools)\" = 8dabe979dffeed607d886c98ca91485cb9a64c69", "expect": "exit0"}
# row 4: no execution object at B; the names occur in this file, so files are read directly and never through git grep
{"id": "b4-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-gh-1-ref-hygiene/ | grep -v -e '/preregistration.md$'", "expect": "empty"}
{"id": "b4-no-lint-files", "scope": "B", "check": "git ls-tree --name-only $REF tools/ | grep -e 'ephemeral'", "expect": "empty"}
{"id": "b4-gate-no-step", "scope": "B", "check": "git show $REF:tools/release_gate.py | grep -F -e 'ephemeral'", "expect": "empty"}
{"id": "b4-agents-no-section", "scope": "B", "check": "git show $REF:AGENTS.md | grep -F -e '§A.38'", "expect": "empty"}
{"id": "b4-guard-no-clause", "scope": "B", "check": "git show $REF:verification/lean/edge_rigidity_probe.py | grep -e 'R7-GH1' -e 'gh1_' -e 'GH1'", "expect": "empty"}
{"id": "b4-no-certificate", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/certificates/ | grep -e 'GH1\\.json$'", "expect": "empty"}
{"id": "b4-no-seal-record", "scope": "B", "check": "git ls-tree --name-only $REF verification/seals/ | grep -e 'GH1\\.json$'", "expect": "empty"}
# row 5: the SI-3 check GH1-1 exercises is present at B, once
{"id": "b5-attempt-constant-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c '^_SI3_ATTEMPT1 = ')\" = 1", "expect": "exit0"}
{"id": "b5-attempt-check-once", "scope": "B", "check": "test \"$(git show $REF:verification/lean/edge_rigidity_probe.py | grep -c -F \"out['P12 attempt 1 unreachable']\")\" = 1", "expect": "exit0"}
# row 6: this control plane at its path
{"id": "b6-self-present", "scope": "B", "check": "git ls-tree --name-only $REF verification/infrastructure/round-gh-1-ref-hygiene/preregistration.md", "expect": "nonempty"}
```

## The landing shape

Non-sealing, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is current green
`main`, its second parent exactly `E`; conflicts, if any, are resolved in `L` by merits. Full
continuous integration passes on `L` before it merges, and the push run on `main` is green before
any later round's landing is built. After the landing, the execution branch and this control
plane's branch are deleted in the ordinary way; neither is a temporary ref any artifact depends on.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; no rebase, amend or force-push. Each commit-bearing stage
commits before its checkpoint. A stop outcome halts the round; the halt is recorded in a result
note with the outcomes reached, and nothing else of the execution lands.

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — no round certificate.** `GH-1` writes no `V2` certificate. A certificate for a round
  landed after `CV-1` would be `native-v2`, the lifecycle `CV-2` was to install and whose delivery
  is now a migration requirement of the next architecture; `F6` shows the path has a live failure
  surface. The consequence is that the opening sentence of `verification/README.md`'s `CV-1`
  section — "`verification/certificates/` carries one certificate per round", and in the same
  sentence "under `attestations/`, one record per round that has topology" — becomes false at
  `GH-1`'s landing, since `GH-1` has topology and neither. `GH1-5` corrects that sentence in place
  so that it describes the frozen dataset: the text from "A landed round is now also **data**:"
  through "one record per round that has topology:", both located with whitespace normalized, is
  replaced, reflowed to the paragraph's width, by

  > `verification/certificates/` carries the `CV-1` migration snapshot: one certificate for each
  > round represented in that snapshot, fifty-one translated from the guard's blocks and the seal
  > manifest, plus `CV-1`'s own bootstrap certificate, issued by the `V1` guard that certifies the
  > round and never by the verifier it installs; and, under `attestations/`, one record for each
  > round in that snapshot that has topology:

  and nothing else in the paragraph changes; whitespace-normalized, the paragraph at `E` equals the
  paragraph at `B` with exactly that substitution. The corrected text is true of the snapshot
  permanently and makes no claim about rounds after it. The declined option is a `native-v2`
  certificate written during execution with an attestation appended after the landing, as `CV-1`
  did for its own.
- **`R2` — no mechanical chronology control.** `GH-1` adds no `V1` guard clause: `V1` is the
  representation the next architecture retires, and a clause added now is migration debt. The
  execution-time chronology is the executor's recorded check plus exact-head review. The declined
  option is an `R7-GH1` clause of the strengthened ancestry form.
- **`R3` — the inventory digest.** `F1` freezes the inventory as a procedure over the remote with
  a byte-exact serialization, and records its digest at `D`. Stage 2 re-runs the procedure against
  the remote immediately before any deletion; the deletion list is exactly the lines it yields,
  and only if their digest equals `F1`'s. Any mismatch is `INVENTORY-DRIFT` and deletes nothing.
  The digest names nothing and requires nothing to exist afterward. The declined option is a
  count-only identification, which cannot detect a head that moved.
- **`R4` — who counts as temporary.** `§A.38` defines a temporary branch as any branch other than
  `main` and `dev`, matching this round's scope; the lint's prefix list is narrower and names the
  agent prefixes the repository has used.
