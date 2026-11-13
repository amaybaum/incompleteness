# Status note: OA-2, operations on emergent observer states richer than permutations

This note gives the current standing of `OA-2-REPORT-r4.md` in this directory. It does not change
that file or any other file here; r4 is the accepted text. The substitutions `OBJECTS.md` records are
separate from this note.

## Accepted record and reviews

- **Record.** `OA-2-REPORT-r4.md`, blob `8f8ddf73366deb1a2caa13d8c826744d1ba87607`, SHA-256
  `970935762ed94386726147f874b87fcab7666d392f117b0f00b2d3e0b90de0d3`, 1067 lines. The reviewed and
  accepted bytes, committed at `4b087b1ebab49992bc0c6b0b307581f42e41f9b1` (PR #1265), differ from
  these on lines 65 and 958 only; `OBJECTS.md`, section "Committed bytes differ from the reviewed working copies",
  gives their blob and SHA-256 and how to restore them. The checks stated below were made on the
  reviewed bytes. Source snapshots `main` at `fb733b4a`
  (r1), `ec257bee` (r2) and `615cc119` (r3, r4), each an ancestor of `main`. The record re-checks
  its Main:60 and Main:724 quotations at `911a5cb6`.
- **Review trail.** `OA-2-REPORT.md` (r1) to `OA-2-REPORT-r3.md` are the earlier revisions. They stay
  unchanged, apart from the substitutions `OBJECTS.md` records, which keep every line number,
  because the reviews and `OA-3-REPORT-*.md` cite their lines.
  - `REVIEW-OA-2.md`: r1, REVISE (F1–F9).
  - `REVIEW-OA-2-r2.md`: r2, ACCEPT WITH NITS (N1–N7).
  - `DELTA-REVIEW-OA-2-r3.md`: the r2 → r3 delta, ACCEPT WITH CHANGES (E1–E11); "Recheck of r4",
    ACCEPT WITH NITS (R1–R12); "Confirmation of r4", ACCEPT after one bookkeeping edit (C1).
  - `OBJECTS.md` ties each reviewed working copy to its committed blob. Its section
    "Committed bytes differ from the reviewed working copies" gives the reviewed and committed bytes of
    each file committed with a substitution.
- **The accepted blob and the confirmed text.** The confirmation names working-copy blob
  `655480e9` and requires C1, a 28-line block replacing r4:1040–1067.
  That working copy was not retained. In the committed r4, lines 1040–1067 equal the C1 block byte
  for byte. Lines 1–1034 equal the committed r3 with the E- and R-edits applied by the session's
  exact-substitution scripts, which the confirmation found to be the review's exact text. These
  checks were made by the package writer; they are not a review.
- **Nature of the reviews.** Separate read-only, paper-only AI-agent reviews; not human reviews,
  GitHub approvals or owner decisions. The record and its last review label every [W] and [RW] item
  an unreviewed hand derivation, none kernel-checked. The reviews record their own checks of named
  steps (for example `REVIEW-OA-2.md`'s verdict paragraph, and `DELTA-REVIEW-OA-2-r3.md` §2 on
  Proposition B(ii)). This note does not change those labels.
- **Authority.**
  - Unit: #1169 comment 6831588323 (`amaybaum`, 2026-11-12T17:55:41Z): "The owner answered
    "Authorize paper-only unit". The unit is OA-2: one bounded, paper-only investigation, ending in
    independent review."
  - Delta review: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z), item 1: "Run all
    three (Recommended)".
  - Acceptance record: #1169 comment 6842174066 (`amaybaum`, 2026-11-13T02:39:11Z): "OA-2: the delta
    review is complete, and r4 is accepted."

  Emphasis is removed from the quotations.

## What the record establishes

- **Paper-level research findings, not adopted.** They are hand derivations ([W], [RW]) on
  manuscript statements ([P]), Lean statements on `main` ([K]) and research records not
  independently established ([R]). The record changes no manuscript claim.
- **Laws over configurations (N0).** A bijection acts on them stochastically, and its reversible
  actions are permutations.
- **Theorem C.** At a fixed finite carrier, reversible trace-preserving emergent operations form a
  finite group, for every rule.
- **Designed control (N2.3).** A reversible classical computer `𝔊_K` shows an exact,
  preparation-contextual gbit at each bounded horizon, under C-PM′ and C-PM, with its uniform bath
  under μ-G (not established under μ-R or μ-O). At bounded horizons G0,
  G1 and G3 do not separate classical from quantum.
- **Theorem E(b), affine class.** Under (H1), H-AR (additive, cell-aligned observers), (H3) no
  supplied control, (H4) nested records, (SP) spanning and ledger item (xiv), the prepare–measure
  fragment is simplex-embeddable. Without (H4) or (SP) the affine class is narrowed, not closed.
- **Proposition B(ii) (⇒)** is proved under (CVX), closure of the available effects under mixing,
  with reviewer-supplied steps that the author did not re-derive. Without (CVX) the direction fails.
- **Class N, one cell, native `Z`/`X`.** Preparation- and measurement-noncontextual, with premises at
  `q = 2` only, on [R] premises and H-LIFT.
- **Open.** G3 for admissible non-affine rules; AW-OA2-1, -2 and -4.

**Claim supported by this record:** "For OI's gauge-derived affine rule class, under (H1),
additive cell-aligned observers, no supplied control, nested records, spanning and ledger item
(xiv), the prepare–measure fragment of the emergent operational theory is simplex-embeddable;
at any fixed finite carrier, reversible trace-preserving emergent operations form a finite group
for every rule; a designed reversible classical computer, with a uniform bath under the global
counting measure and the C-PM′/C-PM label conventions, shows an exact preparation-contextual gbit
at each bounded horizon, so the criteria G0, G1 and G3 do not separate classical from quantum
at bounded horizons; admissible non-affine rules remain open (paper-level research findings: hand derivations
that the record labels unreviewed, partly on research records not independently established,
not kernel-checked, with independent AI-agent reviews of the
report; not adopted; no manuscript claim affected)."

## Dependencies

| Reference | Classification |
| --- | --- |
| `papers/Main.md` and `verification/lean-mathlib/OIBridge/` lines at the snapshots | Support on `main`; see source drift. |
| Records under `reconstruction/` (MECH-1, MECH-2, apparatus-1, obsmu, mathcon1-polc, minacc-1, round-arp1-marc, operational-quotient v3) | Support on `main`, unchanged since `fb733b4a`. They are [R] records, so statements resting on them carry [R] (§A.46 item 7). |
| TUNE-1 `TUNE-1-STEP2-SESSION3.md` at `615cc119` (`T1/n`) | Support on `main`, as [R] prior art (Lemma A-T). |
| OA-1 r4 at `066be3b1` (`OA1r4:n`) | In this PR (`../oa-1-20261112/`), at the same blob. It lands with this record and is cited as research only (§A.46 item 7). OA-1's accepted text is r5. The r4 lines OA-2 cites are unchanged in r5, except §2A's N3 rows (r4:267–268), inside the range r4:236–270 that OA-2 cites (:98) only for the typing of the three measures. |
| #1169 comments 6831588323, 6841795465, 6842174066 | Governance provenance, quoted above. |
| #1237, #1255 | Provenance for the snapshot notes. |
| Commits `815d6a8e`, `5fec0966` and `4b087b1e` on this PR's branch, named in the reviews | Support on `main` once this PR lands by merge commit, which keeps them ancestors of `main`. |
| Working-copy blob ids in `DELTA-REVIEW-OA-2-r3.md` (:473, `1b282d9a`; :671, `655480e9`) | Named by their first 8 characters in the committed file, which closes the §A.42 item 3 gap by abbreviation: the abbreviated ids name session working copies that were not kept. Neither working copy was retained. The committed blob is tied to the confirmed text as stated above. |
| Other references inside the reviews (session paths, the reviewers' authorization statements, `origin/main` commits) | Provenance. Each verdict rests on the blobs `OBJECTS.md` records. |

## Source drift from `615cc119` to `main` (`62bdc2cf`)

- `verification/lean-mathlib/` and every cited record are unchanged. `main` changed no paper after
  `911a5cb6`.
- In `papers/Main.md`, :36, :60, :90, :151, :700 and :724 changed. The record re-checked its Main:60
  and Main:724 quotations at `911a5cb6`. Ledger items (iv), (vii), (xiii) and (xiv) are verbatim;
  item (ii) adds the source of the observer's finiteness ("from the finite-capacity clause of the
  Definition"), and its total-finiteness posit is unchanged.
- Main:90 now says that the visible law, which any emergent quantum description must reproduce,
  depends only on the partition, and does not by itself fix the quantum representation. The record
  cites Main:82–92 only for "does not fix cell alignment" (:192), which the change leaves as it was.

## Superseded lines in the accepted text

- Lines 3 and 8, "WIP / UNVERIFIED": these are the working labels of the draft. The record's
  standing is as stated in this note.
- Lines 18–19, "Nothing committed, pushed or posted" (Standing r2, retained): the record is
  committed and lands with this PR.
- Line 29, "`main` is now `615cc119…`", and line 36, "`origin/main` moved to `911a5cb6`": `main` at
  `62bdc2cf` has no further change to the cited sources.
- Lines 40–41, "OA-1: branch `research/oa1-w1-1-20261112` at `066be3b1…`": once this PR lands, that
  file is on `main` in `../oa-1-20261112/`.

## Landing

- **Together.** This record cites OA-1 r4, and OA-3 cites this record's r3 and r4. All four units
  land in one merge.
- **Mode.** Merge commit (neither squash nor rebase), so that `4b087b1e` and the other commits the
  reviews name remain ancestors of `main`. The branch commits carry "(WIP, not for merge)" in their
  messages; those were labels on the working checkpoints.
- **Basis.** §A.46 item 2: the record supports the claim above, at the strength stated. No record on
  `main` depends on it at `62bdc2cf`. The accountable Issue is #1169.
- **Owner record.** Landing package: #1265 comment 6846206075 (`amaybaum`, 2026-11-13T06:44:20Z):
  "Prepare after sequence (Recommended)"; the PR "then lands only after a separate owner merge
  decision, as a merge commit."
