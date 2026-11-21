# A1-EXIT trial T1: retained run evidence

This directory retains the evidence of the two verification runs of the A1-EXIT trial commit `T1`. It carries no
manuscript claim. The trial and its expected outcome are preregistered in the retirement plan (#1477, §28.1 item 5,
§29 item 2 and §30, quoted below). The T0 evidence it builds on is retained in `../a1exit-trial-t0-20261121/`.

## Status of this record: an owner exception to §A.42

`T0` and `T1` are not reachable from `main`, so this record names support that `main` does not hold. It lands under a
temporary exception the owner recorded at #1169 comment 7069511889 (`amaybaum`, 2026-11-21T21:29:35Z), limited to this
evidence-retention record. In the owner's words, the record must state:

> - T1 is a trial of proposed retirement content, not evidence that the retirement has occurred on `main`;
> - the off-`main` support is identified by exact, immutable commit hashes, with preserved artifacts and verification
>   procedures;
> - the support gap stays open until the retirement content has landed on `main` and been independently verified
>   there;
> - if the retirement is rejected or materially changed, the trial results are not to be presented as verification of
>   the final manuscript;
> - the exception waives no scientific, CI, regression or merge requirement.

Accordingly:
- **T1 is a trial.** Nothing in it has been applied to `main`; the A1 retirement is not authorized.
- **The support left open.** The claim this record leaves unsupported from `main` is that the trial commit `T1`, whose
  tree is named below, is the tree the two runs checked. The runs' own records (the artifact and the host's run, job and
  step conclusions) are retained here.
- **What closes it.** The gap closes when the retirement content lands on `main` and is independently verified there.
- **What a passing trial does not show.** That the planned retirement changes survive the prescribed checks does not
  establish that every scientific consequence of removing A1 is correct. The final scientific review covers that (#1477).

## Provenance

| Item | Value |
|---|---|
| Trial commit `T1` | `c06259692ddf12f7d3dffe170ec3118dc97682fc`, tree `5838b89d6a3dc792a47b9cdc59df7b3b3561d80b`, branch `trial/a1exit-T1-55544cc3` |
| Its single parent | `97070c986c28f7ff8a443cbda5890c1694dd76dd`, the ledger base |
| `T0` | `5b6d48b58f45d3032bc33560aa5047c4b400f35a` |
| Plan head `P*` | `55544cc36dee5b7dd5b9079c0f03be24b74c137f` (branch `research/a1exit-deletion-20261121`) |
| Dispatch 1 | `.github/workflows/a1exit-trial-verify.yml` on `main` `3a12f785278049c93a3bb50209582df4c492b0ad`, `trial_sha` = `T1`, `plan_sha` = `P*`; run 44951832698, attempt 1, conclusion `success` |
| Dispatch 1 artifact | 14726791183, `a1exit-trial-verify-c06259692ddf12f7d3dffe170ec3118dc97682fc`, 4472057 bytes, sha256 `96ef872b08f22bd5574ca34fdd717b33edec1a512068e920cd315d9503208f33`, equal to the host's digest |
| Dispatch 2 | `.github/workflows/verify.yml` on `trial/a1exit-T1-55544cc3` at `T1`; run 44953482787, attempt 1, conclusion `success` |

**How `T1` is built** (§28.1 item 5): `T0`'s tree with the eight PDFs of the ledgered sources replaced by the
CI-built PDFs of T0's verification run, and parent exactly `97070c98`. `git diff-tree T0 T1` lists exactly those eight
paths. Their sha256 digests are the `build/` member digests in `../a1exit-trial-t0-20261121/expected.json`, which
`check.py` compares. The PDFs were extracted with that directory's `check.py --extract`, which verifies before it
writes. The commit has fixed author and committer dates (2026-11-21T21:30:00Z, `Claude <noreply@anthropic.com>`), so
rebuilding it reproduces the id.

## Owner decisions

All are #1169 comments posted under the owner's account (`amaybaum`) as the record of the owner's decision.

- **Authorization of both dispatches and of this exception**, comment 7069511889, `amaybaum`, 2026-11-21T21:29:35Z:
  > | Dispatch 1: `a1exit-trial-verify.yml` | Authorized |
  > | Push `trial/a1exit-T1-55544cc3` | Authorized |
  > | Dispatch 2: `verify.yml` | Authorized |
  > | Evidence gap (§A.42) | Option (b): a temporary, explicitly documented exception |
  > | Actual A1 retirement | Not authorized |
  > | Merge of the evidence PR | Requires separate approval |
- **Dispatch 1 accepted**, comment 7069863094, `amaybaum`, 2026-11-21T21:59:38Z:
  > | T1 dispatch 1, run 44951832698 | Accepted as matching its expected outcome |

## The governing criteria

§28.1 item 5 of `verification/audits/foundations/a1exit-deletion-20261121/PREREG.md` at `P*` (blob
`04f55e09560739fcd8eddd95f5b913da05a5c4ad`, line 5504), on `T1`, verbatim:

>    - `T1`: a single-parent child of `97070c98` whose tree is `T0`'s with the eight PDFs replaced by that artifact's.
>      `a1exit-trial-verify.yml` and `verify.yml` are dispatched on `T1`; every step and job must pass.

The owner's authorization states the expectations: for dispatch 1, every required step passes, with zero
PDF-comparison findings, `guards --mutants` succeeding and `result.json` reporting `verdict: pass`; for dispatch 2,
every required CI job passes, including Lean/Mathlib and the release gate, with any skipped job reported and assessed
against the workflow's requirements.

## Results

**Dispatch 1** (run 44951832698):
- all 13 steps succeeded, the final gate included;
- `preserve_check.py`: pin findings 0, ledger validation findings 0 (371 splices, ledger sha256 `41ac4fd9…`), candidate
  findings 0, and `pdf compare against the CI build: 0 findings`;
- `guards_check.py --mutants`: 64 checks, all passing;
- every structured report (`out/*_check-*.json`) has `verdict: pass`, with no failing check;
- the rebuilt TeX equals the committed TeX, and the eight PDFs have the page counts in `result.json`;
- `result.json`: `verdict: pass`.

**Dispatch 2** (run 44953482787): all 41 jobs concluded `success`, including `Lean kernel check` and `Mathlib bridge`,
whose `Release gate` step succeeded. No job was skipped. One step was skipped, as designed: `Mathlib bridge` step
"KTRANS-SEP-2 marker complete reports with an axiom outside the three". Its condition
(`steps.ktrans_sep2_axioms.outputs.reports == 'complete-nonstandard'`, `verify.yml` at `T1`, line 211) holds only when
a report lies outside the three axioms; the preceding step, "KTRANS-SEP-2 axiom reports within the three axioms",
succeeded.

## Files

The files retained from the host are kept complete: `artifact.zip` and `artifact/out/` are byte-identical to what the
host served. The other files are written for this record.

- `artifact.zip`: dispatch 1's artifact as downloaded: `result.json`, the step logs and exit codes, the structured
  checker reports, the toolchain record and the eight CI-built PDFs (`build/`).
- `artifact/out/`: its `out/` members, extracted byte for byte; the PDFs stay inside the zip.
- `ci-record.json`: both runs' identity and their job and step conclusions, read from the host's API (§A.44). Raw logs
  are not retained; the host's logs for the two runs are their provenance.
- `expected.json`: the expected result.
- `check.py`: checks the files above against `expected.json`.

Before commit, the retained files were scanned for tokens, keys, signed URLs, IP addresses and e-mail addresses, with
no hits.

## Reproduction

From the repository root:

```sh
python3 -I -B verification/audits/foundations/a1exit-trial-t1-20261121/check.py              # integrity and outcomes; RESULT PASS
python3 -I -B verification/audits/foundations/a1exit-trial-t1-20261121/check.py --self-test  # 14 mutants, each required to report its target finding
python3 -I -B verification/audits/foundations/a1exit-trial-t1-20261121/check.py --github     # host artifact digest and both runs' job and step conclusions
```
