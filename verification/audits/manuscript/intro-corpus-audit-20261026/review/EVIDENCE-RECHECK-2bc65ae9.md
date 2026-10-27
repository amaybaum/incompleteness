*Recorded by the coordinator from the independent reviewer's report, verbatim. `S` in paths below is the session scratch directory, not retained.*

# Re-check 3: `git diff 8f6ea594 2bc65ae9` (commits 9226b6a5 and 2bc65ae9)

**Verdict: ACCEPT.** C1 is resolved, and the relabel of I-227 is justified. Both changes behave as intended. I-227 is
the only row whose evidence entry changes. All three `--check` modes pass, and my independent aggregation agrees on
all 409 rows. I found no new defects.

This was a read-only review of the diff only, in a fresh detached worktree at 2bc65ae9, which I removed at the end.

## 1. C1, the gap text for I-227 (commit 9226b6a5)

**Resolved.**

- **The fix.** E4:163-166 now chooses the reason by the clause that rejected the item. If the link names a research
  record or a probe file, the text is "listed items name other records or probes". Otherwise it is "listed items do not
  name this manuscript file".
- **Why the choice is exact.** `contradicted()` (E4:101-110) only ever rejects by one clause:
  - when the link names a record or probe, it rejects only on the record/probe comparison;
  - otherwise it rejects only under the manuscript clause;
  - a link that names neither gets no rejections, and no parenthetical is rendered.

  So the rendered reason always names the clause that fired.
- **Where the new text appears.** At 9226b6a5 it is rendered for exactly two links: I-227 link 0 and link 2. Both
  read "listed items do not name this manuscript file: E2-07, E3-18". That is correct, because E2-07 and E3-18 name
  neither GR.md nor book ch07.
- **Links with rejections but no gap.** I-193 link 1, I-045 and I-054 have rejected items, but they also have matched
  items, so no gap is rendered for them.
- **At 2bc65ae9.** The relabel makes I-227 links 0 and 2 paper-derivation, so the computation-gap text no longer
  applies anywhere. EVIDENCE.md contains no occurrence of "do not name this manuscript file".
- **Rule text.** The by-file note was added to the rule text in E4:22-23 and to the rendered rule in EVIDENCE.md.

## 2. The I-227 relabel (commit 2bc65ae9)

**Justified.**

- **The relabel.** `matrix/chain-relabels.json` changes I-227 link 0 (`papers/GR.md:833`) and link 2
  (`book/ch07-gravity.md:126`) from exact-algebra to paper-derivation.
- **The links' own text supports it.**
  - Link 0 quotes GR's argument: "The same holds for every bijection: acting on a definite configuration, φ visits
    only configurations … so S(ρ_R) = 0 along every such orbit". That is the written proof.
  - Link 2 is the book's restatement of it ("Book mirror: … visits only product states").
  - Neither link is a computation. The finite sweeps are link 1, the BHb record, which keeps exact-algebra and stays
    matched to E2-07 and E3-18.
- **I-225 is unaffected.** Its link 2 also cites GR.md:833, but it names the BHb record as well, so it still matches by
  record.
- **The effect on I-227 is as intended.**

| | Level | Artifact level | Basis |
|---|---|---|---|
| Before | traced-only | traced-only | — |
| After | traced-only | **reproduced** (support) | "weakest of all its links: traced-only (paper-derivation)" |

  I-227 is now listed under "Traced-only rows whose checked artifacts reach a higher level", whose count goes from 19
  to 20 reproduced. It is now treated the same way as I-216.
- **No other row changes.**
  - I compared `evidence.json` between 8f6ea594, 9226b6a5 and 2bc65ae9. In each step, only the entry for I-227
    differs.
  - I compared `matrix.json` row by row: only I-227 changes, and no top-level key changes.
  - `MATRIX.md` changes 7 lines. The two I-227 steps in the §5 dependency-block table change their layer, and that
    table is regrouped by layer, which renumbers its rows. With the row numbers ignored, the only difference is those
    two layer fields.

## 3. Checks

**`--check` modes.** At 2bc65ae9, `E4_aggregate.py --check`, `render_matrix.py --check` and `merge_matrix.py --check`
all pass.

**Full pipeline from scratch.** I deleted `evidence.json`, `EVIDENCE.md` and `MATRIX.md`, then ran merge, E4, merge
and render. `matrix.json`, `evidence.json`, `EVIDENCE.md` and `MATRIX.md` all came out byte-identical.

**Drift mutations** (`scripts/mutate3.sh`, output in `outputs/drift-mutations-3.txt`). The new case removes the
I-227 relabel and regenerates E4; E4 `--check` and `merge --check` both fail on it.

| Mutation | E4 `--check` | `render --check` | `merge --check` |
|---|---|---|---|
| Baseline | pass | pass | pass |
| Row level in `matrix.json` | fail | fail | fail |
| Row basis in `matrix.json` | fail | fail | fail |
| Chain edited in `matrix.json` | fail | pass | fail |
| Relabel edited | fail | pass | fail |
| Relabel edited, E4 regenerated | fail | pass | fail |
| Relabel removed, E4 regenerated | fail | pass | fail |
| Relabel added, E4 regenerated | fail | pass | fail |
| Part file chain only | pass | pass | fail |
| Part file chain, E4 regenerated | pass | pass | fail |
| `resolutions.json` edited | pass | pass | fail |
| Claim inventory edited | pass | fail | pass |
| I-227 relabel dropped, E4 regenerated (new) | fail | pass | fail |
| `not_covered` removed | fail | pass | pass |
| `evidence.json` row edited | fail | fail | fail |

The results match the 8f6ea594 run, and every mutation is caught by at least one check.

**Independent aggregation.** `scripts/reagg3.py` imports nothing from E4. It finds 0 differences from `evidence.json`
in 409 rows. The counts are 44 reproduced, 127 certificate-checked, 235 traced-only and 3 failed, unchanged, since
I-227 was traced-only before as well.

## 4. Anything else in the diff

Nothing else.

- **E4 code.** The only code change is the reason selection. The local name `why` in `grade_link` does not collide
  with the `why` in `aggregate()`, because they are in different functions.
- **The review file.** The added `review/EVIDENCE-RECHECK-8f6ea594.md` is my RECHECK2.md verbatim, apart from a
  coordinator header and the scratch path shortened to `S/rereview-e/`.
- **Manuscripts.** No file under `papers/` or `book/` is touched.
