# Re-review of `0be12721` (PR #885): corrections to `1907963e`

Read-only review: nothing was committed, pushed, commented or dispatched, and no checkout was changed. The tree was
extracted with `git archive` into `…/review-885-integration-2/tree`. Paths are relative to
`…/missing-component-20261020/`.

## Verdict: CHANGES NEEDED (one blocking finding)

## 1. B1: the "two-site" wording is gone, but the encoding is now attached to the wrong stage (BLOCKING)

- The words "two-site" are gone from INTEGRATION.md. The formula now given matches the source exactly: the combined
  overview START-HERE.md:84–86 and `workspace/oi_native_x_instrument_v1/REPORT.md` §4.
- **BLOCKING B1′.** Obligation 2 (INTEGRATION.md:69–71) now reads "…then a reset with the calibrated post-Y law
  (5:3:2), fresh conditional resources and the outgoing encoding E(x,y,r,z) = …". That makes E the encoding the
  **Y reset must output**. No source says this.
  - **What E is in the source.** The source calls E "the current outgoing X encoding". It is the native-X
    instrument's output, and therefore the *input* to the Y stage. The three reachable codes in the same obligation
    arise from E at the second outward step. The native-X REPORT §6 and §end say that reusing E as the input of
    another reset is the next task.
  - **What the sources require of the Y reset's output.** For a post-Y state, the composition report
    (`workspace/oi_parallel_20261024/composition/REPORT.md` §4) gives only a decoded target,
    (X,Y,R,Z) = (y⊕a, y, y⊕b, z), with the 5:3:2 plane law and fresh fair z. It gives no site layout. The overview
    (l.174) and the native-Y SYNTHESIS ("Next construction target") ask for checks on the "entire outgoing carrier".
    Neither fixes E as the output.
  - **Conflict with obligation 3.** As written, obligation 2 also cuts against obligation 3, which says a reusable
    outgoing encoding is still open.
  - **Suggested fix.** "…starting from the native-X carrier E(x,y,r,z) = ((x,1,y) at q_Y, (x,1,r) at q_R,
    (0,0,z) at q_Z), …then a reset with the calibrated post-Y law (5:3:2), fresh conditional resources and an
    outgoing carrier that decodes to (y⊕a, y, y⊕b, z)". The alternative is to name E only as the X carrier, as the
    first review suggested.

## 2. Non-blocking findings of INTEGRATION-REVIEW-1907963e

| Finding | Status | Check |
|---|---|---|
| NB-1 README precedence | Addressed | README now rests precedence on the `PREREG.sha256` timestamp (`2026-10-23T11:00:02Z`). PREREG, its digest and the checker were first committed together in `9283b435`. Nit: "the two" reads as PREREG.md + PREREG.sha256; REPORT says "with the code". |
| NB-2 REPORT exceptions | Addressed | The header admits values marked as from the review. TV ≈ 0.298, the degree-2 flag and the "odd part divisible by 5 / 25" statement now each cite `review/REVIEW.md`, matching REVIEW 5b/5c and Q6c. |
| NB-3 run_*.out | Addressed | Both files were added and are listed in `review/SHA256SUMS`. They are byte-identical to each other, to the reviewer's scratch originals, and to `instrument_checks.out` at `455eb092`, which is the commit REVIEW.md reviews. |
| Nit: re-preparation "there" | Addressed | "at the outgoing receivers at the same tick" is accurate. |
| NB-4 native X | Addressed | "candidate" restored. "pending a proof audit of the inherited transport theorem" matches the external review (2a51fe2a…, l.49). The optional finite-algebraic herald note was knowingly left. |
| NB-5 native selector | Mostly addressed | The one-time-pad sentence matches NATIVE-SELECTOR-REVIEW F1 and its l.213 suggested text. **Left:** "readout of a setting" was not changed to "of the selected sign for a setting". This is minor, but the cell still says a setting is read out. |
| NB-6 read-reset | Addressed, with a nit | 2/5 and 9/10 are now scoped to XOR masks, and SF2 is stated correctly ("binding only if … fair and independent", READ-RESET-REVIEW l.242–254). Nit: "reversible permutations reach 7/30" drops *input-independent* and "also with validity required" (E1–E3, SF1). Data-dependent reversible processing is exactly what the review says can do better. Suggest "input-independent random permutations (which include the XOR masks) reach 7/30, also with validity required". |
| NB-7 selector record | Addressed | The qubit and independent-apparatus premise (F1), "no native selector constructed", and the factorization as the review's recommendation (F2, l.108) all match SELECTOR-RECORD-REVIEW. The factorization stays in the row rather than moving to Acceptance; that is acceptable. |
| NB-8 combined handoff | Addressed | "concrete application audit and not compiler certification" matches START-HERE l.25 ("…not all-formula compiler certification"). It is classed "internal". |
| NB-9 legend | Addressed | *external* is now defined. |
| NB-10 obligation 1 / native Y | Partly | Obligation 1 now says "has internal proof audits", which is accurate. **Knowingly left:** the native-Y row still omits that the staged-disclosure contract is abstract (supplied recorder and reset). |
| NB-11 #910 | Partly | The label difference is now stated. **Left:** the index is still pinned at `1c8c9e5e`, behind #910's head. This is acceptable for a snapshot. |
| NB-12 evidence location | Addressed | The three review reports and this index's review are retained in `integration-reviews/`. Their sha256 values match the first review's table and the scratch originals. Residual: those reports cite reviewer code that is not retained (for example the read-reset `mine/`). This is acceptable for a draft index, but must be resolved under §A.42 before landing. |
| NB-13 identifier | Addressed | `455eb092e5bdc37d203945e6689cee5032268dbf` exists. |

No changed cell introduces a new overclaim, apart from B1′ and the 7/30 scope nit.

## 3. Added files and hygiene

- `sha256sum -c` passes for `integration-reviews/SHA256SUMS` (4 files), `NI/SHA256SUMS` (6, with the new README and
  REPORT digests) and `NI/review/SHA256SUMS` (14).
- `INTEGRATION-REVIEW-1907963e.md` is byte-identical to the first review's REVIEW.md.
- Added lines contain no absolute local paths, no credentials and no personal data. Scratchpad references appear only
  in elided form (`…/scratchpad/…`, `scratchpad/read-reset-review/`).

## 4. Scope of the diff

`git diff --name-status 1907963e 0be12721` lists exactly 12 files:

- INTEGRATION.md;
- 4 review reports and SHA256SUMS in `integration-reviews/`;
- NI README, REPORT and SHA256SUMS;
- `review/SHA256SUMS`, `run_O.out` and `run_normal.out`.

Nothing else changed: the checker and its output are untouched.
