# Introduction paper: design (outline and contribution statement)

**Status: design record, independently reviewed.** Owner-authorized design stage of the Introduction paper, which
replaces `papers/Explainer.md` as the primary short-form presentation (owner decision 2026-10-26; publication
structure Introduction → Main → Book). No paper text exists yet, and nothing here changes a manuscript. Every source
line is cited at `main` `687e885b`.

## Files

- `OUTLINE-r4.md`, `CONTRIBUTION-r4.md`, `SOURCES-r4.md`: the design in force. The outline maps each section onto the
  owner's six parts, cites each claim's source line, verification layer and originality class (from
  `../novelty-v5/AUDIT.md` r4), and budgets about 14.25 pages. `SOURCES-r4.md` carries the claim register, the
  untraced list, the risks and the owner decisions.
- Earlier revisions, each the object of the review named:
  - `OUTLINE.md`, `CONTRIBUTION.md`, `SOURCES.md` (r1): `review/REVIEW.md`, ACCEPT WITH CHANGES.
  - `*-r2.md`: `review/RECHECK-r2.md`, BLOCK (wording only).
  - `*-r3.md`: `review/RECHECK-r3.md`, BLOCK (wording only, one required change).
  - `*-r4.md`: `review/RECHECK-r4.md`, ACCEPT.
- `CHANGES-r2.md` … `CHANGES-r4.md`: the change notes, each mapping review items to edits.
- `probe/examples.py`: exact check of Main's §2.4 example and the XOR family (scratch probe; not cited by the paper).
- `probe/cards.py` and `review/r3/mycards.py`: the designer's and the reviewer's independent exact checks of the
  card-table game (book ch01 §1.11): one shuffle 1/2, two shuffles 1, chained 1/2; the "peek" gives 1/2 only when
  the burn card holding the record is overwritten, and 1 otherwise; under the permutation-unitary embedding the
  two-step channel is the identity.

## Not retained

- The CI log of the release gate at `687e885b` (run 40291389159, job 121467032075; sha256
  `e20abaee6061de73cd5a98749b0040abc999bff0acbf70db26f78b67d27a5251`), cited in the reviews as provenance for the
  axiom reports. A raw log is not committed as evidence (§A.42); the outline records that a retained expected result
  is required on `main` before the paper states the Lean check.
- Scratch locations the records cite as `S/…`: `S/paper/mainwt` is a checkout of `main` `687e885b`;
  `S/paper/design/` is this directory and `S/paper/review/` is `review/`; `S/paper/explainer/` is
  `../explainer-review/`; `S/pintro/repo/` is this repository at the PR head. The literature studies the novelty audit
  relies on and their reviews (`S/introaudit/lit-*`, `S/revlitcorr/`, `S/revlitbh/`) are not in the repository;
  whether to retain them is owner decision 3 in `SOURCES-r4.md`.
