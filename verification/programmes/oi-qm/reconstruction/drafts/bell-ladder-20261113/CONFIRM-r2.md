# Focused confirmation: Bell ladder r2 (#868)

The reviewer is the author of REVIEW-r1. This confirmation is read-only and uses hand reasoning only.

**Object.** Branch `research/bell-ladder-868-20261113`, fetched by name, at head
`b8096c79fd166793700f60cca8c46c6b3c2af556`.
- The head is a single-parent child of main `c3b5f37a`.
- It adds 7 files under `verification/programmes/oi-qm/reconstruction/drafts/bell-ladder-20261113/` and nothing
  else.

## Verdict: ACCEPT WITH CHANGES (three small required changes, R1–R3; nonblocking nits N1–N4)

### (1) C1–C14 and the nonblocking items

All are applied as specified in `BELL-LADDER-r2.md`:

- C1: lines 233–237.
- C2: §0:73–74, :209–212 and :257.
- C3: (AL4) :197–200 and **Histories** :248–252.
- C4: :77–81 and :260–262.
- C5: :88–92 and stages 0–4.
- C6: :154–155.
- C7: :175.
- C8: :67–68.
- C9: :102.
- C10: :97 and :290.
- C11: :56.
- C12: :157–158.
- C13: :100, :103, :193–194, :259, :297–299.
- C14: :302.

Two nonblocking items are applied: `e_{x0} = f_{y0} = 0` (:219) and the composite converses (:96, :291). The
other two (the `Z_3` remark and the fixed point) are dispositioned in NOTES-r2.

`RESPONSE-r1.md` records each disposition and its check. Its hand checks agree with mine.

### (2) The witness finding

The witness is stated accurately in the ladder (scope bullet **Histories**, :248–252, tagged [A]). It is stated only
at its scope: inside (vii), with `μ_0`, the coset law and MI, and with no-signalling imposed on a setting-selected
read rather than on the complete fixed-region history.

- §4(iii) (:260–262) correctly calls this a weaker admissibility criterion, not an escape.
- Owner question Q4 is in NOTES-r2:97–98, and the assumption-watch marker is in NOTES-r2:54–56. Both are worded
  correctly.

### (3) The C5 relabel

It is consistent everywhere:

- The definition at :88–92 states "undetermined for OI's native rule unless stated".
- Stages 0–4 read "NOT FORCED (designed witness …)". Stage 7 reads UNDETERMINED; stages 5–6 read OBSTRUCTION.
- No "ESCAPE DEMONSTRATED" remains in r2. The remaining uses of "escape" are generic, and NOTES-r2:87–89 records the
  relabel.

### (4) Conditional heading

- The ledger heading is conditional (:77).
- Every class-(vii) conclusion in §0 and §4 carries its conditions: (vii), coset law, cell-valued settings,
  complete-history no-signalling over fixed regions, and every-run outputs.
- Nothing in BELL-LADDER-r2 is stated OI-wide.
- NOTES-r2 Q1 is the exception; see R2.

### (5) Byte identity and hashes

- `REVIEW-r1.md` @ `b8096c79` is byte-identical to my `REVIEW.md` (`cmp`).
- `BELL-LADDER-r1.md` and `NOTES-r1.md` are byte-identical to the reviewed working copies.
- All six sha256 values in `OBJECTS.md` match the committed blobs, with no substitutions:

| File | sha256 |
|---|---|
| `BELL-LADDER-r1.md` | `468905ed…` |
| `NOTES-r1.md` | `24a304a4…` |
| `REVIEW-r1.md` | `746171e9…` |
| `BELL-LADDER-r2.md` | `4b8e3a48…` |
| `NOTES-r2.md` | `dd8ee905…` |
| `RESPONSE-r1.md` | `496a2f7b…` |

- The rec-1 head `cd38655c` (NOTES-r2:15) is confirmed at the host ref.

### (6) New overclaims or inconsistencies (all in the committed NOTES-r2 or the §5 status table)

**R1 (NOTES-r2:59).** This line contradicts the new **Histories** finding, which shows that no-signalling on the
read part does not suffice.
- Old: "Requires complete-history NS only for the histories the outputs are read from; NS on a larger history
  implies it."
- New: "Requires NS on the complete fixed-region histories; NS on the part the outputs read does not suffice (the
  selected-read witness above). NS on a larger fixed history implies NS on a smaller fixed one."

**R2 (NOTES-r2:92–93, Q1).** "An escape needs a Layer-0 revision" is stronger than the ladder's own list (§0:80–81)
and than Q4.
- Old: "If yes, the ladder's answer for OI is the AL/Theorem-N′ obstruction and an escape needs a Layer-0 revision;"
- New: "If yes, the ladder's answer for OI is conditional: the AL obstruction (and Theorem N or N′ for
  graph-separated wings) holds for coset-uniform run laws, cell-valued settings and complete fixed-region
  histories, and an escape needs a Layer-0 revision or the failure of one of those conditions (§0; Q4);"

**R3 (BELL-LADDER-r2:272).** This status row is stale.
- Old: "| Proposition AL | [A], unreviewed | independent review of §4; extension to mixtures"
- New: "| Proposition AL | [A]; one independent non-author review (ACCEPT WITH CHANGES, applied in r2); ChatGPT
  review pending | ChatGPT review at the exact head; extension to mixtures"

Add a row after it:

> | Record convention for (AL4) | open | whether an embedded observer's complete history is the full fixed record
> region or may be a setting-selected read (NOTES Q4); AL's obstruction needs the former, and the selected-read
> witness of §4 gives PR for the latter |

### Nonblocking

- **N1, NOTES-r2:33.** "Same content" overstates the match: SB L4 is broader (any abelian groups, no finiteness).
  Main:362 covers the (vii) case.
- **N2, RESPONSE-r1.md:3.** It cites `REVIEW.md`; the file in the directory is `REVIEW-r1.md`. Its statement
  "nothing was committed, pushed or posted" (with NOTES-r2:10) describes writing time; the coordinator's commit
  `b8096c79` now holds the files.
- **N3, BELL-LADDER-r2:298.** The QH row's leading "support off `main`; no verdict here rests on it:" duplicates the
  per-use classifications that follow it. Drop the leading clause.
- **N4, stage 6 row (:102).** "given coset law and NS" could read "given coset law, cell-valued settings and
  complete fixed-region NS" to match (AL3)/(AL4).

No change to any verdict, classification or proof is needed. R1–R3 align the status surfaces with the r2 body.
