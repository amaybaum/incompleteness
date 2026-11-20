# Bell-scope unit 1 r2: preservation note

This note covers the three files listed below and no other file. `../bell-ladder-20261113/OWNER-EXCEPTION.md`
records the owner exception under which they land, including the status note for findings 1–3 below. `BELL-SCOPE-UNIT1.md` and
`DISPOSITIONS-r2.md` are byte-identical copies from draft PR #1231 (branch
`research/bell-scope-868-20261111`, head `e1534b08fa3f361e05416b3cc0c1dcd2f3b23918`), at the paths
they have there. `REVIEW-BS-r2-NONAUTHOR.md` is a byte-identical copy of the non-author review of that
head from closed draft PR #1285 (branch `records/bell-landing-plan-868-20261114`, head
`a0fa2502d4b3fa525256399d8f297803684fd67e`, directory
`verification/programmes/oi-qm/reconstruction/bell-landing-20261114/`). They are preserved because
records on `main` use Theorem N and N′ as support (§A.42 items 2 and 8). Preservation establishes no
claim of the record (§A.46 item 1) and changes no scientific status.

Authority: owner decision of 2026-11-20 (`amaybaum`, #1169 comment 7030839727): "Narrow preservation
PR(s), not merges of the original drafts, for #1273, #1231 and #1232, plus #1274 where it is
needed." Accountable Issue: #868.

## Files

| File | Source | Blob | SHA-256 | Bytes |
| --- | --- | --- | --- | --- |
| `BELL-SCOPE-UNIT1.md` | #1231 @ `e1534b08` | `5814e479b16929fe8ab045a3f3b8fc4987704633` | `dd7115511e332b1cae20bdda7c3d94ec7f8af20bbd436750d7e6dfccbf078913` | 43178 |
| `DISPOSITIONS-r2.md` | #1231 @ `e1534b08` | `dd8cbc8c5c29ad28d175cbb67dcf23454fc3915a` | `d3a185181747877f2ef977c2be735b0e8b705164b4bfff7ec8635e4808e08d2f` | 5251 |
| `REVIEW-BS-r2-NONAUTHOR.md` | #1285 @ `a0fa2502` | `3ecccdd06c37106258781d73cc87750efa04ee88` | `cf6f3035e3f4754920ef84f4655f9935770d210430190415520948f1c123347a` | 28897 |

`git hash-object` on each file reproduces its blob. "BS:n" is line n of `BELL-SCOPE-UNIT1.md`.

## Citations on `main` that use the record

`selection-discriminator-20261113/support/synthesis/SYNTHESIS-r3.md`, line 731, cites "BS Theorem N/N′
(#1231 at `e1534b08`)" as support off `main` for MM-6 and for its §3 item 8 (the Bell stage-5
ceiling, through `drafts/bell-ladder-20261113/BELL-LADDER-r3.md`:102). Theorem N is BS:159–178 and
Theorem N′ is BS:185–196, in the file landed here; those uses are support on `main` at this path.
That record is not edited: `selection-discriminator-20261113/ARTIFACTS.sha256` and `RETENTION.json`
pin its bytes.

## Review and status

- ChatGPT review 5857227567 on #1231 (posted under `amaybaum`, 2026-11-11T10:22:16Z) at `7abf59d7`
  (r1): REVISE, five required fixes; `DISPOSITIONS-r2.md` records how r2 applies them. ChatGPT review
  5857981727 on #1231 (posted under `amaybaum`, 2026-11-11T11:24:59Z) at `e1534b08`: "ACCEPT for the
  corrected paper unit at its **restricted, conditional** scope; preserve OI-wide verdict
  **INDETERMINATE** and escape **NOT ESTABLISHED**."
- `REVIEW-BS-r2-NONAUTHOR.md`, a non-author review of `e1534b08`: ACCEPT WITH CHANGES. It re-derives
  Theorem N, Theorem N′, Lemma G (one direction), the §4.1 bound and §4.2–4.3 at their stated scope.
  Its findings 1–3 are corrections to statements outside that proved core, which this copy does not
  make: finding 1 (BS:49–54, :73–74, :246–253, :410, :453–456), that under ledger (vii) O1 is closed
  inside NBA's domain; finding 2 (BS:72–74), that a failure of NBA with complete-history
  no-signalling does not by itself give (B); finding 3 (BS:381–385), that the Level-A disjunction
  omits failures of (D), (F), (Gen), (Rec), measurement independence and every-run accounting. The
  review gives replacement text for each. The owner chose a superseding status note (#1169 comment
  7031779559); it is the section "Status note: BS findings 1–3" of `OWNER-EXCEPTION.md`.
- The copy of `REVIEW-BS-r2-NONAUTHOR.md` landed here is the one at #1285's head. It differs from the
  reviewer's first commit of the file (blob `2bd5af8bdf3227d22dad1c905a402a2cf16ee889`, at `d712097f`)
  at lines 262–263, by a rewording that its own lines 350–351 disclose, and in those two added lines.
- BS:3–5 and BS:471–472 describe r2 as awaiting re-review; review 5857981727 above is that re-review.
- All reviews are model reviews: evidence of review, not independent mathematical verification.
  The record is a paper-level research record and is not established (§A.46 items 1 and 7). Its
  verdicts are (C) indeterminate for OI itself, (A) an obstruction for the class 𝒞_sep only, and (B)
  not established.

## Not landed

`probes/generic_bell_checks.py` (blob `e47f3179`) and `probes/generic_bell_checks.out` (blob
`0798db76`) remain on #1231's branch. BS:439 classifies the probe as a gap if the record lands;
`REVIEW-BS-r2-NONAUTHOR.md` (Check 4) reads its [X] checks as provenance only while the ratification
of that run is open (#868 comment 6874036684, OQ-8). Theorem N and N′, which `main` uses, are paper
derivations; the one [X] tag inside Theorem N's proof (G1, BS:178) checks a fact the same review
finds immediate by hand (Check 1, step 4). By the owner exception (`OWNER-EXCEPTION.md`, E3) the probe is
provenance only, not independently reproduced support; landing it, and any replay of it, remain
open under OQ-8. The r1 text is on #1231's branch at `7abf59d7` and is provenance.
