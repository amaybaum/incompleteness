# Status note: OA-3, gbit and dual-gbit shapes in `G_SM`, and Theorem E(b) without (H4)

This note gives the current standing of `OA-3-REPORT-r4.md` in this directory. It does not change
that file or any other file here; r4 is the accepted text.

## Accepted record and reviews

- **Record.** `OA-3-REPORT-r4.md`, blob `0a36fd05ba6931705ecdbb1de9962d58a307c1cb`, SHA-256
  `4b847d72bceae6e6eacdffae14e00d801d086826e04f176fde2d20ea26e5c973`, 841 lines. Committed at
  `2d064a71d9a637c8b1d7983f91cdff2a6357a87b` (PR #1265). Source snapshot `main` at
  `615cc1190ec1bda69093be1eac49c839744008a5`, an ancestor of `main`. The record checks its cited
  lines at `911a5cb6`.
- **Review trail.** `OA-3-REPORT.md` (r1) to `OA-3-REPORT-r3.md` are the earlier revisions. They stay
  unchanged, apart from the substitutions `OBJECTS.md` records, which keep every line number,
  because the reviews cite their lines.
  - `REVIEW-OA-3.md`: r1, ACCEPT WITH CHANGES (F1–F7).
  - `RECHECK-OA-3-r2.md`: r2, ACCEPT WITH CHANGES (E1, E2; m1–m3 optional).
  - `DELTA-REVIEW-OA-3-r3.md`: the r2 → r3 delta at `469ecee9`, ACCEPT WITH CHANGES (R1–R4); "Recheck
    of a55f0588", ACCEPT WITH CHANGES (D1); "Confirmation of b13cbe01", ACCEPT.
  - `DELTA-REVIEW-OA-3-r4.md`: the r3 → r4 delta, ACCEPT WITH CHANGES (R1–R4, O1); "Confirmation of
    r4", ACCEPT, with one replacement in the Standing block.
  - `OBJECTS.md` ties each reviewed working copy to its committed blob. Its section
    "Committed bytes differ from the reviewed working copies" gives the reviewed and committed bytes of
    each file committed with a substitution. r4 is committed with its reviewed bytes.
- **The accepted blob and the confirmed text.** The confirmation names working-copy blob `b65e6d9c`
  and specifies the Standing replacement. Undoing exactly that replacement in the committed r4
  reproduces blob `b65e6d9c` byte for byte. This check was made by
  the package writer; it is not a review.
- **Nature of the reviews.** Separate read-only, paper-only AI-agent reviews; not human reviews,
  GitHub approvals or owner decisions. The record's [W] items are hand derivations; its [RW] steps
  were re-derived by the OA-3 reviewer. Nothing is kernel-checked or computed. As the record states
  (:7–9, :16, :727), the edits a delta review supplied are that reviewer's own text, confirmed as
  applied verbatim and not reviewed independently.
- **Authority.**
  - Unit: #1169 comment 6833027576 (`amaybaum`, 2026-11-12T18:58:01Z): "One more paper-only unit is
    authorized, OA-3." The same comment says "The G_SM enumeration and the simplex-embedding
    computation are not authorized."
  - Delta reviews: #1169 comment 6841795465 (`amaybaum`, 2026-11-13T02:14:35Z), item 1: "OA-3 r3's
    two statements that rely on the OA-2 r3 proof (:357–361 and :748) follow the outcome of the OA-2
    review."
  - Acceptance record: #1169 comment 6842225937 (`amaybaum`, 2026-11-13T02:42:46Z): "Current
    accepted texts on #1265: OA-1 r5, OA-2 r4, OA-3 r4 and W1-1 r4."

  Emphasis is removed from the quotations.

## What the record supports, and at what strength

- **Verdict: OPEN, narrowed.** These are paper-level research findings, not adopted, and the record
  changes no manuscript claim. They are hand derivations ([W], with [RW] steps) on manuscript
  statements ([P]) and research records not independently established ([R]).
- **Lemma OBS** (NEW at corpus level; the standard permutive-CA argument). In SM's ring rule `G_SM`
  at any `q ≥ 2`, an additive observer holding three consecutive sites, with their `u`-history
  retained, determines the entire configuration of a finite ring of `L` sites within `2(L−3)`
  ticks, for every setting. The statement is measure-free.
- **Theorem S** (ELABORATING). Take such observers with MP-0b history or heralded composites
  (V-ii-H), heralds, a measurement stage of at least `2(L−2)` and condition (PT). Then `G_SM`'s
  prepare–measure fragment is a simplex: neither the gbit shape nor the dual shape occurs. It is
  not an impossibility result for `G_SM`.
- **Gate cancellation (N1).** It transfers to `G_SM` under P1, P2 and H-PREP. It refutes read
  restriction rather than sourcing it.
- **N4** (NEW, a hidden assumption in OA-2 r3's gap paragraph). For the affine class under (H1),
  H-AR, (H3), (xiv) and (SP), Theorem E(b) holds with (H4) replaced by the heralded-composite effect
  class (V-ii-H). Under the narrower class (V-ii-U), a 3-cell shift shows a gbit, a memory artefact
  of that convention that does not count.
- **Open.** Small observers (no three consecutive held sites), horizons below Theorem S's bounds,
  infinite windows, the (V-ii-U) record class, initial laws with short preparations outside (PT), and
  herald typing as an interface premise.
- **Proposals only.** The three `G_SM` design amendments of §4. Running anything needs owner
  authorization.

**Claim supported by this record:** "In `G_SM` on a finite ring of `L` sites, an additive observer
holding three consecutive sites with retained history determines the whole configuration within
`2(L−3)` ticks, whatever the settings (measure-free); with history or heralded composites,
heralds, a measurement stage of at least `2(L−2)` and condition (PT), its prepare–measure fragment
is therefore a simplex, so neither the gbit nor the dual-gbit shape occurs; for OI's affine class,
Theorem E(b) holds with nested records replaced by the heralded-composite effect class; `G_SM`
for small observers, short horizons, infinite windows, the single-tick-read record class and
initial laws outside (PT) remains open (paper-level research findings: hand derivations with
reviewer re-derived steps, partly on research records not independently established, not
kernel-checked or computed; not an impossibility result for
`G_SM`; not adopted; no manuscript claim affected)."

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #1169. The owner's ruling, #1169 comment 6865680499 (`amaybaum`,
2026-11-13T21:44:54Z), states that "Model acceptance is evidence of review, not independent
mathematical verification", and that "A remediation plan does not authorize new work. It may state
that the obligation remains open." This plan authorizes no work. Each gap below remains open until
the evidence or decision named for it is recorded on `main`.

Here "partially verified" means reviewed by at least one separate AI-agent reviewer, or resting in
part on kernel-checked statements, without independent mathematical verification of the result;
"exploratory" means a result not reviewed by anyone but its writer, or a proposal that
claims no result.

- **Independently verified:** none of the record's own results.
- **Known-invalid:** none stated.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| Lemma OBS | partially verified | Hand derivation [W] with independent AI-agent reviews; not kernel-checked or computed | Independent mathematical verification | An independent mathematical verification recorded on `main` (for example a kernel formalization or a human review) |
| Theorem S | partially verified; conditional on MP-0b history or (V-ii-H), heralds, a measurement stage of at least `2(L−2)` and (PT) | Hand derivation [W] with independent AI-agent reviews; not kernel-checked or computed; uses OA-2 Proposition B, [W]/[RW] | Independent mathematical verification, including the OA-2 Proposition B steps it uses | As for Lemma OBS |
| Gate cancellation (N1) | partially verified; conditional on P1, P2 and H-PREP | Hand derivation [W] with independent AI-agent reviews; not kernel-checked or computed | Independent mathematical verification | As for Lemma OBS |
| N4, Theorem E(b) with (V-ii-H) | partially verified; conditional on (H1), H-AR, (H3), (xiv) and (SP) | Hand derivation with [RW] steps re-derived by the OA-3 reviewer | Independent mathematical verification | As for Lemma OBS |
| Edits supplied by the delta reviews (R1–R4 of `DELTA-REVIEW-OA-3-r4.md`; R1–R4, O1–O3 and O5 of `DELTA-REVIEW-OA-3-r3.md`) | exploratory; the reviewer's own text, not reviewed independently (r4:7–9, :16, :726–727) | Applied verbatim, as the delta reviews confirm | An independent review of that text | An independent review recorded on `main` |
| Statements resting on [R] records (MECH-1, MECH-2, minacc-1, apparatus-1, obsmu, the L3b round, OA-1 r4, OA-2 r3 and r4) | partially verified | Research records not independently established | Independent validation of each [R] premise used (§A.46 item 7) | A recorded validation of that premise on `main`, or the statement narrowed to carry it as a named condition |
| The three `G_SM` design amendments of §4 | exploratory | Proposals | Not applicable; nothing is claimed | Running anything needs owner authorization |

Where a gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

The items listed as open are not results of the record; they remain under #1169.

## Dependencies

| Reference | Classification |
| --- | --- |
| `papers/SM.md` and `papers/Main.md` lines at `615cc119` | Support on `main`; see source drift. |
| Records under `reconstruction/` (MECH-1, MECH-2, minacc-1, apparatus-1, obsmu) and the L3b round under `interface/` | Support on `main`, unchanged since `615cc119`. They are [R] records, so statements resting on them carry [R] (§A.46 item 7). |
| OA-2 r3 at `815d6a8e` (`OA2:n`), its reviews (`Rv2`, `Rv2b`), OA-2 r4 at `4b087b1e` (`OA2r4:n`), OA-1 r4 at `815d6a8e` (`OA1:n`) | In this PR, at the same blobs apart from the substitutions `../oa-2-20261112/OBJECTS.md` records, which keep every line number and change no line OA-3 cites, and they land with this record. Theorem S uses OA-2 Proposition B, [W]/[RW]. OA-2 r4 changed some r3 lines OA-3 cites. `DELTA-REVIEW-OA-2-r3.md` §2.5 and §3.4 and `DELTA-REVIEW-OA-3-r4.md` cover the bearing of B(ii)(⇒) and of class N at `q = 2`; r4 carries (CVX) where (⇒) is used. The other changed lines it cites are r4's qualifiers at r3:150, :396, :401, :440, :785, :798 and :805; the package writer checked them against the citing sentences, outside any review. OA-1's r4 → r5 changes touch only r4:267–268 among the lines cited (inside :236–270, cited for the typing of measures). |
| #1169 comments 6833027576, 6841795465, 6842225937 | Governance provenance, quoted above. The record cites c.6833027576 "as relayed by the coordinator; not re-fetched" (:21–22); its text is as quoted above. |
| #1265 comment 6848447181 (merge record; quoted under Landing); #1169 comment 6865680499 (the ruling; quoted under Verification status and Landing) | Governance provenance. No scientific result uses either; the Basis line uses only the quoted words, which are on `main` in this note (§A.42 item 7). |
| Literature [L] (Hedlund 1969; Schmid et al. 2021) | Context only. The record states that no verdict rests on it. |
| Commits `469ecee9`, `a55f0588`, `b13cbe01`, `815d6a8e`, `4b087b1e` and `2d064a71` on this PR's branch, named in the reviews | Support on `main` once this PR lands by merge commit, which keeps them ancestors of `main`. |
| Abbreviated working-copy ids in `DELTA-REVIEW-OA-3-r4.md` (`b6164dd6`, `b65e6d9c`) | Not objects in the repository; `b65e6d9c` is reproduced as stated above. They are abbreviated, so §A.42 item 3, which covers full ids, does not apply. |
| Other references inside the reviews (session paths, the PR's REST state, `origin/main` commits) | Provenance. Each verdict rests on the blobs `OBJECTS.md` records. |

## Source drift from `615cc119` to `main` (`62bdc2cf`)

- Every record the report cites is unchanged, and `main` changed no paper after `911a5cb6`.
- The cited lines of `papers/Main.md` and `papers/SM.md` read as the record states (:31–37). Main:60
  adds the source of visible finiteness, and ledger item (xiv) is verbatim. SM changed at :196 and
  :605, outside §3.1 (SM:100–169).

## Superseded lines in the accepted text

- Lines 3 and 11, "WIP / UNVERIFIED": these are the working labels of the draft. The record's
  standing is as stated in this note.
- Line 20, "Recorded on the research branch of draft PR #1265 (not for merge); not landed on
  `main`": the landing puts the record on `main`.
- Lines 31–33, "`origin/main` is now `911a5cb6`. `git diff 615cc119 911a5cb6` touches, under
  `papers/` and `verification/programmes/oi-qm/`, only `papers/Main.md` … and `papers/SM.md`": that
  diff also changes other papers (`GR`, `Substratum`, `Structure`, `Complexity`, `Computation`,
  `Medicine`, `Methodology`), none of which the record cites. No paper changed from `911a5cb6` to `62bdc2cf`.

## Landing

- **Together.** This record cites OA-2 r3 and r4 and OA-1 r4, all in this PR. All four units land in
  one merge.
- **Mode.** Merge commit (neither squash nor rebase), so that `2d064a71` and the other commits the
  reviews name remain ancestors of `main`. The branch commits carry "(WIP, not for merge)" in their
  messages; those were labels on the working checkpoints.
- **Basis.** Landed by the owner's merge decision "Merge now (Recommended)", recorded in the merge
  record #1265 comment 6848447181 (`amaybaum`, 2026-11-13T08:54:09Z, edited 09:07:32Z), which states
  "What landed: OA-1 r5, OA-2 r4, OA-3 r4 and W1-1 r4, as research records on their stated scope. No
  claim is promoted." The landing meets none of §A.46 item 2's conditions: no established claim
  needs the record, it carries no computation, and no record on `main` depended on it at `62bdc2cf`.
  The merge record names no owner exception. Under the owner's ruling, #1169 comment 6865680499
  (`amaybaum`, 2026-11-13T21:44:54Z), until the §A.46 amendment it calls for is adopted, "a landing
  that meets none of the existing conditions needs an explicit, recorded owner exception". The
  record's landing basis is therefore open until that amendment is adopted or such an exception is
  recorded. The record is preserved on `main`, not established (§A.46 item 1). Its removal is not
  automatic and is governed by item 6. The accountable Issue is #1169.
- **Owner record.** Landing package: #1265 comment 6846206075 (`amaybaum`, 2026-11-13T06:44:20Z):
  "Prepare after sequence (Recommended)"; the PR "then lands only after a separate owner merge
  decision, as a merge commit."
