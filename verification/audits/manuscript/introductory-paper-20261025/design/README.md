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

## Erratum

`ERRATUM-r4.md` corrects one clause in the r4 records (OUTLINE-r4 §5-h, SOURCES-r4 §5-h, CONTRIBUTION-r4 non-claim 13,
and the RC-A row of `review/RECHECK-r4.md`): "admits no classical-memory decomposition (Main:702)" holds for the swap
with an initialized hidden slot, not for the card game's uniform, independent burn card, whose two-step identity map
decomposes through classical memory. The r4 files are kept as reviewed; the erratum gives the corrected wording and the
exact check behind it (`../draft/review/scientific/probe/card_exact.py`).


## Revision 5: the applications scope (WIP, under review)

On 2026-10-26 the owner widened the paper's scope: "ambitious in its scientific implications but conservative in its
claims", organized around three questions (what OI is; what it might explain; what remains to be proved), with about
four pages of "Applications and Potential Resolutions". The cosmological constant leads, as a proposal conditional on
the open covariant field equations. Black-hole information is treated as preservation versus accessible recovery.
Horizon thermodynamics is presented as consistency, not prediction.

- `applications-audit/`: the read-only audit of each candidate application against the corpus at `687e885b`
  (`AUDIT.md`), with its symbolic and numerical checks:
  - `quarter.py`: the Bekenstein–Hawking 1/4 is fixed by the calibration of two normalizations, for every mode density;
  - `cc.py`: the 10¹²² ratio against the de Sitter entropy at a Planck cutoff;
  - `lookelse.py`: the look-elsewhere count for simple closed forms near the Cabibbo value.
- `OUTLINE-r5.md`, `CLAIMS-r5.md`, `CHANGES-r5.md`, `DEPENDENCIES-r5.md`: the r5 design. It has a section plan with page
  budgets, a register of every claim beyond r4 with its status and dating, a change map from r4, and the corpus
  overclaims r5 must not lean on (these go to separate manuscript-consistency changes). Independent outline review is
  in progress.

## Revision 6: one idea, two consequences

The independent review of the r5 design (`review/r5/REVIEW.md`, with its checks in `review/r5/chk/`) returned ACCEPT
WITH CHANGES: 19 required wording changes. The structure stood. It confirmed by its own code that the 1/4 is a
calibration identity and that Theorem A.8's Page value holds on the full product space but not in general on a proper
shell. `applications-audit/CORRECTIONS.md` records the four audit errors it found.

On 2026-10-26 the owner then narrowed the paper. Quantum emergence is the central thesis, with two applications: the
cosmological constant (leading) and black-hole information (preservation versus accessible recovery). Everything else
is removed: horizon entropy, Cabibbo, JUNO, the Page time, PE-01, the arrow of time and the measurement reading. The
target is 10–12 pages, with 2–3 for the applications. The paper states that neither application is a demonstrated
resolution, and it cites the technical papers for derivations instead of re-deriving them.

`OUTLINE-r6.md`, `CLAIMS-r6.md`, `CHANGES-r6.md` and `DEPENDENCIES-r6.md` are that design:
- about 10.4 main-text pages, with 2.65 for the two applications;
- a results register, one row per result, giving the exact statement, status and layer, the reference, and a witness
  for each direction of every equivalence;
- every r5-review change on retained content applied, and the rest recorded as moot.

Independent re-check is in progress.

## Revision 7

The independent re-check of r6 (`review/r6/RECHECK.md`, with its page-budget check in `review/r6/chk/`) returned
ACCEPT WITH CHANGES. The re-scoping is faithful, and both applications are stated as not demonstrated resolutions.
It confirmed that r6 neither cites nor leans on any of the corpus sites found incorrect in #937. Its six required
changes are applied in `OUTLINE-r7.md`, `CLAIMS-r7.md`, `CHANGES-r7.md` and `DEPENDENCIES-r7.md`:
- Theorem A.8's Page value holds on the full product space and fails in general on a proper shell;
- bijectivity is restored to the black-hole success bound;
- "the quantum description" is limited to the fixed-basis statistics;
- two theorem rows get back a dropped hypothesis each;
- the page budget is corrected to about 11.2 main-text pages, with about 2.4 for the applications.

Reading Weinberg 1989 first-hand is a landing gate. A confirmation re-check of the r6→r7 diff is in progress.
