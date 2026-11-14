# Response to the focused review of S3-PLAN-r8

**UNREVIEWED.** These are the writer's dispositions of `REVIEW-S3-PLAN-r8.md` (ACCEPT WITH CHANGES at
`8cdbb929`). The changes are in `S3-PLAN-r9.md`, and nothing else changes. `S3-PLAN-r8.md` is left
unchanged (SHA-256 `8af6893a57199c94e6449b33abdd2acdd60785ddde41c637fd64293148038885`).

## R12

**Check at source.** MR★ §M.6, "Countercontrols", begins at `amendments/MR-star.md`:1018 on `main`. Its
instance table gives each of the following fully, with operations, reference behaviour and separating
test:
- **CC4**, "An epistemically restricted classical field (Spekkens-type toy bits; Catani et al. 2023)",
  at l. 1066;
- **CC5**, "A classical eraser", at l. 1067;
- **CC7**, "Classical dephasing with no record", at l. 1069.

MR★'s review record reports that "the countercontrol checks" were verified (`MR-star.md`:1297–1300).
That is the same relayed report as for S-L3 (`stage1-log.json`:773), so under §A.46 item 7 these are
named premises. The README's stage 2 is "controls-only": it runs them; it does not construct them.

The finding is confirmed. r8's "class level only" was wrong.

| Site in r8 | Disposition in r9 |
|---|---|
| §8.2, class-(iv) examples (r8 ll. 499–501) | Now "fully specified on `main` as named premises: … CC4 (M-1), … CC5 (M-2) and … CC7 (M-3), in MR★ §M.6 (`MR-star.md`:1066–1069)"; running them needs an MR-1 stage-2 authorization |
| §8.4, check 7 (r8 ll. 709–710) | U4 uses M-7, M-8 and M-1 to M-3 as named premises, and constructs, verifies and runs none of them |
| §8.5, heading paragraph (r8 l. 721) | Now "Fully specified in MR★ §M.6 on `main`, as paper instances; named premises; running them needs an MR-1 stage-2 authorization", with specification, status, the role of stage 2 and the verifier role |
| §8.5, rows M-1 to M-3 (r8 ll. 726–728) | Class "(iv), named premise", with the §M.6 line cited for each |
| §8.4, check 1, CC5 sentence (r8 ll. 667–669) | Labelled "a named premise, specified at `MR-star.md`:1067" |
| §8.6, (e′) (r8 l. 800) | Now pending *verification and running*, not specification. It counts only once the cited generalized-noncontextual model has been verified and run as a control |
| §8.6, gating sentence (downstream) | The (e′) item now reads "an MR-1 stage-2 authorization and independent verification of CC4 and CC5" |
| §9, general stop (r8 l. 865) | Restated: "running M-1 to M-3 (CC4, CC5, CC7) as controls, which is MR-1 stage 2, or verifying them". The moot "full specification" is removed |

## Optional item

**Applied.** The verifier of S-L3 and of CC4, CC5 and CC7 is named by role: "an independent reviewer
under a separately authorized unit". This is stated in D-1's S-L3 counting condition and in §8.5, with
"This plan authorizes nothing".
