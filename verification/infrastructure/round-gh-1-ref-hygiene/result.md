# Repository hygiene round GH-1 — HALTED at the closing checkpoint: RESULT

**Halted at the closing checkpoint: `GH1-6` is `SCOPE-EXCEEDED`, and no `E` was certified.** The
frozen predicate requires `dev` at its `D` tip at `E`. `dev` was at its `D` tip through stage 2;
afterwards the repository owner merged `main` at `B` into `dev` (pull request #723), so at the
candidate `E` the predicate was false. `GH-1` itself never wrote `dev`. `GH1-0` to `GH1-5` reached
their passing outcomes.

**Nothing of the round's execution landed except this record.** `main` carries the round's control
plane (the preregistration, blob `b41439ce33eb92766087c4977a8c2efa52666850`) and this note. The
`§A.38` text, `tools/ephemeral_ref_lint.py`, `tools/ephemeral_ref_baseline.json`, the
`ephemeral-refs` gate step and the `verification/README.md` correction were executed and measured
at the candidate `E`, and none of them is on `main`. The retirement of the ten stale remote heads
is a change to the remote, not to the tree, and stands. The facts below are recorded as measured.

Executed from the certified merge of this round's control plane and from nothing else. The
execution's first act verified this round's preregistration blob at that base.

- **`B` (mandated execution base)** — `2c6a4373e7a6b5c6faa0b3981f0a8813bc5a5701`, first parent
  `D` = `8f60d841034370b9daa78ac347465281ca1bee76`; push run 35872041341, all five jobs green,
  the control-plane base check in mode `B` over 26 rows and 8 frozen blobs with no failure
- **Freeze blob at `B`** — `b41439ce33eb92766087c4977a8c2efa52666850` at
  `verification/infrastructure/round-gh-1-ref-hygiene/preregistration.md`, verified before any
  edit
- **Shape** — non-sealing, `E` → `L`, no `P`. No manifest record, prospective declaration,
  manifest-baseline change or guard clause; no round certificate and no attestation (readings `R1`
  and `R2`)
- **Status** — HALTED at the closing checkpoint, at the first stop outcome, `GH1-6`
  `SCOPE-EXCEEDED`; no `E` certified

| target | outcome | predicted |
|---|---|---|
| `GH1-0` | `BASE-HOLDS` | `BASE-HOLDS`, strong |
| `GH1-1` | `HISTORY-INDEPENDENT` | `HISTORY-INDEPENDENT`, strong |
| `GH1-2` | `REFS-RETIRED` | `REFS-RETIRED`, strong, conditional on the owner's deletion |
| `GH1-3` | `FORWARD-RULE-INSTALLED` | `FORWARD-RULE-INSTALLED`, strong |
| `GH1-4` | `HISTORY-UNTOUCHED` | `HISTORY-UNTOUCHED`, strong |
| `GH1-5` | `STATUS-ACCURATE`, no correction from the ref retirement and exactly one, reading `R1`'s | the same, moderate |
| `GH1-6` | `SCOPE-EXCEEDED` — stop | `SCOPED`, strong |

***

## `GH1-0` — the base: BASE-HOLDS

The execution branch was created at `B` exactly. The preregistration at `B` has the frozen blob.
The control-plane self-test and lint self-test pass, and `--mode B` at `B` passes 26 rows and 8
frozen blobs with no failure. Each row's command was also run directly: the `D` rows 11 of 11 at
`D`, the `D->B` rows 5 of 5, the `B` rows 10 of 10.

***

## `GH1-1` — the main-only replay at `B`: HISTORY-INDEPENDENT

A repository built from a bundle of `main` alone at `B`: HEAD `B`, 2712 commits (equal to `main`
in the full checkout), not shallow, no alternates, refs only `main` and its remote-tracking ref.
The nine side-only tips and all thirty side-only commits are absent; the one contained tip is
present. The object `_SI3_ATTEMPT1` names is absent: `git cat-file -e` and
`git merge-base --is-ancestor` both exit 128. In it, at `B`:

| check | result |
|---|---|
| guard `verification/lean/edge_rigidity_probe.py` | `ALL CHECKS PASS`, 105 PASS, 0 FAIL, verdict map identical to `D`'s; `R7-SI3` PASS, its 28 locating controls holding, `P12 attempt 1 unreachable` true on an absent object |
| `tools/certificate_verifier.py --self-test`, `--mode authoritative` | OK; 89 vectors executed, 0 mismatches, exact |
| control-plane self-test, lint self-test, `--mode B --ref HEAD` | pass; 26 rows, no failure |
| Lean kernel check, the six core files | pass (toolchain `v4.33.0`) |
| numerical probes (44 files) and foundations probes (12 files) | all pass |
| `tools/release_gate.py` | PASS, 19 of 19; `lean-axioms` 4187 named results, no `sorry` |

**Mathlib provisioning (`H3`).** The third-party packages were supplied at the pinned revisions.
The `lake-manifest.json` Lake generated in the main-only tree is byte-identical to the full
checkout's: nine packages, each with the same revision, URL, type and input revision. `OIBridge`
was built fresh from the main-only tree, 181 build outputs for the 181 modules tracked at `B`,
none shared with the full checkout's build.

**The first release-gate invocation produced no verdict.** Its `lean-axioms` step's first Lake
call generated the manifest, which runs Mathlib's post-update cache download; the execution
environment's network policy blocks the cache host, and the call was stopped by the gate's timeout
before any repository check ran. The authoritative measurement is the fresh `OIBridge` build from
the main-only tree followed by a complete release-gate run, the 19 of 19 PASS above.

***

## `GH1-2` — the stale refs: REFS-RETIRED

Immediately before any deletion `F1`'s procedure was re-run against the remote: step 3 held for
every tip, and it yielded ten lines whose digest equals `F1`'s. Those lines were the deletion list;
it was held as execution-time scratch and never entered the repository. The executing session's
deletion push was refused (HTTP 403), as the preregistration records, and the owner deleted
exactly the listed heads.

After the deletion the remote carries two heads, `main` and `dev`, each at its pre-deletion tip,
and the procedure yields no line. A fresh default clone of the remote: HEAD `B`, not shallow, no
alternates, 2712 commits reachable from all of its refs, equal to `main`. The nine side-only tips,
all thirty side-only commits and the object `_SI3_ATTEMPT1` names are absent from it. In it, at
`B`:

| check | result |
|---|---|
| guard | `ALL CHECKS PASS`, 105 PASS, 0 FAIL, verdict map identical to `D`'s; `R7-SI3` 28 of 28 locating controls holding |
| verifier `--self-test`, `--mode authoritative` | OK; 89 vectors, 0 mismatches, exact |
| control-plane self-test, lint self-test, `--mode B --ref HEAD` | pass; 26 rows, no failure |
| `tools/release_gate.py` | PASS, 19 of 19; `lean-axioms` 4187 named results, no `sorry` |

Provisioning was as in `GH1-1`: the generated manifest byte-identical to the full checkout's, and
`OIBridge` built fresh from the clone, 181 build outputs, none shared. The first Lake call again
entered the blocked cache download and was stopped before any repository check ran; it produced no
verdict. The authoritative measurement is the fresh build followed by the complete release-gate run
above.

***

## `GH1-3` — the forward rule: FORWARD-RULE-INSTALLED

Measured on the stage-3 commit and at the candidate `E`. None of these objects landed.

- **`AGENTS.md`** gained `§A.38`, appended after the last line of `§A.37` with one separating blank
  line. The section is byte-equal to the frozen text, and the file at `B` is an unchanged prefix of
  the file at the candidate `E`.
- **`tools/ephemeral_ref_lint.py`**, standard library only, implements the frozen specification.
  Its pattern is byte-equal to the frozen pattern.
- **`tools/ephemeral_ref_baseline.json`** was emitted by `--emit-baseline` from the tree at `B`:
  29 entries over 17 paths, counts summing to 29, each of multiplicity one, 12 distinct names, all
  under `verification/` — `F4` exactly. It carries the frozen pattern and no branch name. The
  emission from the full checkout at `B` and from the fresh clone at `B` are byte-identical.
- **`tools/release_gate.py`** gained the frozen step `ephemeral-refs` immediately after
  `control-plane-lint`, with a three-line comment, and no other change.

The baseline is read as a mapping from `(path, line_sha256)` keys to counts. A file that lists one
key twice is not a well-formed mapping and is refused as malformed before any comparison. The
verdict is the frozen one, applied to a well-formed baseline: FAIL iff some key's current count
exceeds its baseline count, or the baseline's pattern differs from the tool's.

`--self-test` passed all eleven frozen cases, `(a)` to `(k)`. It could fail: with the pattern's
lookbehind removed, case `(i)` failed; with counts not summed over identical lines, case `(c)`
failed. The tree check passed over 906 tracked text files: 29 grandfathered occurrences, none new,
none retired. The self-test assembled its fixture names at run time, so the lint's own source, the
baseline, `§A.38` and the gate comment carried no match (`H5`). The release gate passed 20 of 20
with the new step; the guard stayed at 105 PASS, 0 FAIL with `D`'s verdict map; the verifier was
authoritative OK.

***

## `GH1-5` — the status sweep: STATUS-ACCURATE

After the deletion the five surfaces `F5` names were re-read: `README.md`,
`verification/README.md`, `verification/ROADMAP.md`, `AGENTS.md` and
`verification/lean-manuscript-census.json`. None carries a present-tense statement that a
temporary branch exists, is preserved or must be consulted, or any retired tip or side-only commit
by SHA. The passages that mention an earlier execution attempt are past-tense records that name no
branch, and they remain true. The ref retirement required no correction.

Reading `R1` required one, made at stage 4 and not landed. In `verification/README.md`'s `CV-1`
paragraph the text from "A landed round is now also **data**:" through "one record per round that
has topology:" was replaced by the frozen sentence scoping the certificates and attestations to the
`CV-1` migration snapshot, reflowed to the paragraph's width. Whitespace-normalized, the paragraph
equalled the paragraph at `B` under exactly that substitution. It was the only one of the file's
125 paragraphs that differed, and neither "one certificate per round" nor "one record per round
that has topology" remained in the file. The guard, the verifier and the release gate were green on
the commit carrying it. On `main` the paragraph is the paragraph at `B`.

***

## `GH1-4` — historical artifacts: HISTORY-UNTOUCHED

`git diff --name-status B E`, evaluated at the candidate `E`, the commit that first carried this
note:

| status | path |
|---|---|
| `M` | `AGENTS.md` |
| `A` | `tools/ephemeral_ref_baseline.json` |
| `A` | `tools/ephemeral_ref_lint.py` |
| `M` | `tools/release_gate.py` |
| `M` | `verification/README.md` |
| `A` | `verification/infrastructure/round-gh-1-ref-hygiene/result.md` |

Nothing is deleted. The modified files are the two the mutation budget names and the one `GH1-5`
correction; the added files are the three the budget names. Each of `F4`'s seventeen files has its
`B` blob at the candidate `E`.

***

## `GH1-6` — scope: SCOPE-EXCEEDED

The frozen passing outcome is a predicate on the repository at `E`, and one of its conjuncts is
`dev` at its `D` tip. That conjunct was false at the candidate `E`.

- **`dev` through stage 2.** At `D` `dev` was at `42a9e6eb006e29957389661a44feafe050f3811f`, a
  commit contained in `main`. It was at that tip immediately before and immediately after the
  stage-2 deletion.
- **`dev` at the closing checkpoint.** The repository owner merged `main` at `B` into `dev` through
  pull request #723, after stage 2. The new tip's parents are the old `dev` tip and `B`; the tip
  itself is not on `main`.
- **`GH-1` and `dev`.** The execution never wrote `dev`: it pushed nothing before the closing
  checkpoint, and the deletion list excluded `dev` by construction.

The other conjuncts held at the candidate `E`. Nothing under the guard,
`tools/certificate_verifier.py`, `.github/workflows/`, `verification/seals/` or
`verification/certificates/` (certificates, attestations, the conformance corpus and the live
policy) had changed, nor anything under `verification/programmes/`, `verification/audits/`, any
other round's directory, `papers/`, `book/` or the Lean trees. No round certificate, attestation or
guard clause of this round existed.

At the candidate `E` the guard was at `ALL CHECKS PASS`, 105 PASS and 0 FAIL, with `D`'s verdict
map. The verifier was authoritative OK. The lint self-test and the tree check passed with no new
occurrence, and the release gate passed 20 of 20. None of this changes the outcome: the frozen
predicate was false, the round halts at this stop outcome, and the candidate `E` is not `E`.

***

## Chronology

The execution's commits after `B` are four, each a single-parent child of its predecessor, the
first a child of `B`: the stage-3 commit, the stage-4 commit, the commit that first carried this
note and was the candidate `E`, and the commit carrying this halt record. The branch absorbed no
later `main`; there was no merge, rebase, amend or force-push, and nothing was pushed before the
closing checkpoint. `GH-1` carries no mechanical chronology control of its own (reading `R2`);
this record and exact-head review stand in its place.

None of those four commits is on `main`. This record reaches `main` by a single commit from `B`
that adds this file and changes nothing else.
