# RESPONSE to the focused confirmation of BELL-LADDER r2

The confirmation (`CONFIRM-r2.md`, on branch head `b8096c79`) returned ACCEPT WITH CHANGES, with required changes
R1–R3 and nonblocking items N1–N4.

Before writing r3, I checked that the committed `BELL-LADDER-r2.md`, `NOTES-r2.md` and `RESPONSE-r1.md` at
`b8096c79` (fetched by name) are byte-identical to the writer's working copies (`cmp`). `BELL-LADDER-r3.md` and
`NOTES-r3.md` are built from those committed files.

Each r3 file changes in two places only: its title or revision line, and the items below. No disagreement is
recorded. No verdict, classification or proof changes.

| Item | Disposition | Check |
|---|---|---|
| R1 (NOTES-r2:59) | Applied in NOTES-r3 as specified. | The **Histories** witness (BELL-LADDER §4 scope limits) is no-signalling on the read part `(y, λ_B[y])` and signals on the fixed region `(ρ, ρ ⊕ x)`. So NS on the read part does not suffice, and the r2 line contradicted it. NS on a larger fixed history implies NS on any fixed sub-history, as its marginal. |
| R2 (NOTES-r2:92–93, Q1) | Applied in NOTES-r3 as specified. | BELL-LADDER §0 lists four ways out: an update outside (vii), a non-coset law, settings that are not cell values, or postselection. Q4 adds the record convention. The r2 wording "an escape needs a Layer-0 revision" omitted all of these except the first. |
| R3 (BELL-LADDER-r2:272) | Applied. The AL status row now records one independent review and a pending ChatGPT review. A new row, "Record convention for (AL4)", is added after it. | The r2 row predated the review. The new row matches NOTES Q4 and the §4 **Histories** bullet. |
| N1 (NOTES-r2:33) | Applied. For (vii), L4's content is Main:362; L4 itself is broader. | SB:155: L4 holds for any abelian site groups and has no finiteness hypothesis. Main:362 states the linear-update case only. |
| N2 (RESPONSE-r1.md:3; NOTES-r2:10) | RESPONSE-r1 is left unchanged, because it is a committed record and is corrected forward here. Its "`REVIEW.md`, this directory" is the committed `REVIEW-r1.md`, and its "nothing was committed, pushed or posted" described the time of writing. The coordinator committed the r2 files on #1273 at `b8096c79`. NOTES-r3 now says that the writer made no commit and that the coordinator committed r2 at `b8096c79`. | The `b8096c79` tree holds `REVIEW-r1.md`; there is no `REVIEW.md`. |
| N3 (BELL-LADDER-r2:298) | Applied. The leading clause of the QH row is dropped, leaving its per-use classifications. | Both per-use cells already state the classification. |
| N4 (stage 6 row) | Applied. The cell now reads "given coset law, cell-valued settings and complete fixed-region NS". | This matches (AL3) and (AL4). |
