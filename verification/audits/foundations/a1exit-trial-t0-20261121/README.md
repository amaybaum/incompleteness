# A1-EXIT trial T0: retained run evidence

This directory retains the evidence of the first verification run of the A1-EXIT trial commit `T0`. It carries
no manuscript claim. The trial and its expected outcome are preregistered in the retirement plan (#1477, §29
item 1, quoted below).

## Owner decisions

Both are #1169 comments posted under the owner's account (`amaybaum`) as the record of the owner's decision.

- **Dispatch authorization**, comment 7067861041, `amaybaum`, 2026-11-21T19:13:42Z:
  > Owner authorization recorded (2026-11-21): dispatch T0, once, with exactly these inputs:
  > - workflow `a1exit-trial-verify.yml`, ref `main`;
  > - `trial_sha` `5b6d48b58f45d3032bc33560aa5047c4b400f35a`;
  > - `plan_sha` `55544cc36dee5b7dd5b9079c0f03be24b74c137f`.
  >
  > The result is evaluated against #1477 §29, and the exact run evidence, `result.json` and the CI-built PDFs
  > are preserved. The expected `preserve` failure is acceptable only if it matches the eight-PDF comparison
  > findings the plan specifies. Any deviation is reported without reinterpretation.
- **T0 verdict**, comment 7068143470, `amaybaum`, 2026-11-21T19:36:22Z, the row of its decision table:
  > | T0 verdict | Accepted as matching #1477 §29 | Expected failure confirmed. §29 names eight affected PDFs, not eight finding lines, so nine findings across the eight PDFs are not a deviation. |

## Provenance

| Item | Value |
|---|---|
| Trial commit `T0` | `5b6d48b58f45d3032bc33560aa5047c4b400f35a` (branch `trial/a1exit-T0-55544cc3`) |
| Plan head `P*` | `55544cc36dee5b7dd5b9079c0f03be24b74c137f` (branch `research/a1exit-deletion-20261121`) |
| Workflow | `.github/workflows/a1exit-trial-verify.yml` at `main` `df6da1c6101e811acdc7952d5748aff57028e8ed`, `workflow_dispatch` |
| Run | 44939798305, attempt 1, job 136954278279 (`verify`), conclusion `failure` |
| Artifact | 14721572058, `a1exit-trial-verify-5b6d48b58f45d3032bc33560aa5047c4b400f35a`, 4468904 bytes |
| Artifact sha256 | `3627368ab0285f7f927f6279942aaa64e030b98f23c847289426af23565d524c`, equal to the digest the host reports for the artifact |
| Job log sha256 | `0edbbba710763899f0c3ffb27d31cf4d6813890add7fd726a3bbc54222d8ae27` |

Neither `T0` nor `P*` is reachable from `main`. Both commits are identified here by their full ids.

## Files

The files retained from the host are kept in the **complete** form: `artifact.zip`, `artifact/out/` and the
job log are byte-identical to what the host served, and nothing has been regenerated or redacted. The other
files are written for this record: `expected.json`, `check.py`, this README, and the Structure.md patch, which
is **derived** from git as its recipe states.

- `artifact.zip` is the artifact as downloaded. It holds `result.json`, the step logs and exit codes, the
  `preserve_check.py` reports, the toolchain record and the eight CI-built PDFs (`build/`).
- `artifact/out/` holds the artifact's `out/` members, extracted byte for byte so that they can be read in place.
  The PDFs stay inside `artifact.zip`; `check.py --extract DIR` writes them out.
- `job-136954278279.log` is the job log as the host served it. Its secrets are masked by the host (`***`).
  Before commit it was scanned for tokens, keys, signed URLs, IP addresses and e-mail addresses, with no hits.
- `expected.json` is the expected result. It records the commits, the run and artifact ids, the digest of
  every artifact member, the step outcomes, the nine preserve findings, the page counts and the verdict.
- `structure-md-main-to-T0.patch` is the change to `papers/Structure.md` from `main` (`df6da1c6`, blob
  `80b7d277`) to `T0` (blob `b82fc3be`), made by
  `git diff --binary --full-index df6da1c6 5b6d48b5 -- papers/Structure.md`. Applied to the `main` blob it
  rebuilds `T0`'s blob exactly. `expected.json` records its digest and both blob ids. It lets the Structure.pdf
  attribution below be checked from `main` alone, since `T0` is not on `main`.
- `check.py` checks the files above against `expected.json`. It reads the nine findings from
  `preserve_check.py`'s structured reports (`out/preserve_check-*.json`, schema `a1exit-checker-result-v1`) as
  well as from `result.json` and `preserve.log`. The `--commit`, `--verify-pins` and `--verify-ledger` reports
  must pass every check. In the tree report the only failing check must be the PDF comparison, and it must carry
  exactly the nine findings.

## Result against §29 item 1

The governing criteria are §29 item 1 of the plan's preregistration,
`verification/audits/foundations/a1exit-deletion-20261121/PREREG.md` at the plan head `55544cc3` (blob
`04f55e09560739fcd8eddd95f5b913da05a5c4ad`, line 5593). The plan is not on `main`. The item is retained here
verbatim, so the criteria the result is judged against are on `main`; this record does not change the plan.

> 1. **N1: the `T0` expectation.** In `a1exit-trial-verify.yml` the `guards` step has no `always()` condition, so after
>    `preserve` fails it is skipped, and the final gate fails. The preregistered expectation for `T0` is therefore:
>    `preserve` fails with only `--pdf-compare` findings for the eight PDFs; `guards` is skipped; `result.json` and the
>    PDF upload are written. `guards` is covered on `T1`, where every step must pass.

The run did all four. The other steps succeeded: `inputs` (the inputs are full commit ids and the run is its
first attempt), checkout, `head` (the checkout is exactly the trial commit, a single-parent child of the
ledger base, with `P` present), Python setup, toolchain, plan, and the build, whose TeX equals the committed TeX
(`tex_files_differing: []`). The final gate ("Every required step succeeded") failed, as §29 item 1 states it
must, and the job concluded `failure`. The `--commit` check reported:

- 0 pin findings;
- 0 ledger validation findings (371 splices, ledger sha256 `41ac4fd9…`);
- 0 candidate findings.

Every tree mutant was caught.

The nine `--pdf-compare` findings fall on eight PDFs:

1. `book/The-Incompleteness-of-Observation-FULL.pdf`: extracted text differs from the CI-built PDF
2. `papers/Computation.pdf`: extracted text differs from the CI-built PDF
3. `papers/GR.pdf`: extracted text differs from the CI-built PDF
4. `papers/Main.pdf`: extracted text differs from the CI-built PDF
5. `papers/Methodology.pdf`: extracted text differs from the CI-built PDF
6. `papers/SM.pdf`: extracted text differs from the CI-built PDF
7. `papers/Structure.pdf`: 94 pages committed, 95 built
8. `papers/Structure.pdf`: extracted text differs from the CI-built PDF
9. `papers/Substratum.pdf`: extracted text differs from the CI-built PDF

## Structure.pdf: the 95th page

The committed `papers/Structure.pdf` is the blob on `main` at `df6da1c6`. `T0` does not change any PDF, and the
PDF's last change is the same commit as the last change to `papers/Structure.md`. The comparison
(`check.py --structure`) finds the following:

- **Where the text first differs.** Page 4.
- **The 95th page.** It holds the end of the reference list: the last line of one entry, `[Weinberg1979]` and
  `[Reuter1998]`. `[Reuter1998]` ends page 94 of the committed PDF.
- **Where the word changes come from.** The net word changes between the two PDFs were compared with the
  net word changes of `papers/Structure.md` from `df6da1c6` to `T0`, as multisets:
  - Every net removal in the source is a net removal in the PDF.
  - Every net addition in the source is a net addition in the PDF, apart from four tokens:
    - two `S`, which typeset as `𝑆`;
    - `3.1`, which the comparison drops as a number;
    - one `OI`, which accounts for the repeated table heading "Emerges from OI?" in the committed PDF.
  - The remaining differences are layout:
    - hyphenation and page numbers falling at different line and page breaks (for example `nec-`/`essary`
      against `necessary`);
    - table headings that repeat where a table crosses a page break. The committed PDF repeats them for the
      table in §7.7.4 ("Emerges from OI?") and the §14.10 cross-program table. The CI-built PDF repeats them for
      the §14.5 table ("Transports?") and the §12.4 empirical-status tables.
- **Net change.** The source edits add a net 134 words (+209, −75). In normalized tokens the CI-built PDF has
  33942 against the committed PDF's 33818.
- **Resolution.** Tokens are compared lower-cased, with punctuation, symbols and hyphens removed, and tokens of
  one to three digits are dropped as page numbers. The comparison does not resolve differences in symbols,
  punctuation or short numbers.

Within this comparison, no word other than those of the ledgered edits differs. The layout changes support
the explanation that the reference list's last lines moved to a new page under the longer text. A toolchain
contribution to the final page break has not been conclusively excluded: no run built `main`'s
`papers/Structure.md` with the CI toolchain, and the committed PDF was built separately.

`--structure` rebuilds `T0`'s `papers/Structure.md` from the `main` blob and the retained patch, checks it
against `T0`'s blob id, and needs no `T0` objects. It is a pass/fail check of the retained evidence: it fails
unless the page counts, the first differing page, the full text of page 95, the token counts and the four
residual multisets above are reproduced exactly, as recorded in `expected.json` with pdftotext 24.02.0. It
does not establish why the page appeared.

## Reproduction

From the repository root:

```sh
python3 -I -B verification/audits/foundations/a1exit-trial-t0-20261121/check.py              # integrity; RESULT PASS
python3 -I -B verification/audits/foundations/a1exit-trial-t0-20261121/check.py --self-test  # 17 mutants, each required to report its target finding
python3 -I -B verification/audits/foundations/a1exit-trial-t0-20261121/check.py --github     # host digest, run event, workflow, head and job conclusion; while the artifact is retained (until 2027-02-19)
python3 -I -B verification/audits/foundations/a1exit-trial-t0-20261121/check.py --structure  # pass/fail; needs git and pdftotext
```

To compare against a fresh download from the host, while the artifact is retained, download it with
`gh api repos/amaybaum/incompleteness/actions/artifacts/14721572058/zip > a.zip` and check that its sha256
equals the recorded digest.
