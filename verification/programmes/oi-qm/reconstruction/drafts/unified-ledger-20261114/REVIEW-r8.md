ACCEPT

# Confirmation review of LEDGER-r8

This review is read-only, paper-only and non-author. It covers `diff LEDGER-r7.md LEDGER-r8.md`
and `RESPONSE-r7.md`, checked at `main` (`dfeec843`). No file was edited, nothing was run on OI
rules, and nothing was posted.

## S1: the reconciliation with T2

**Applied at source.** The §R.2 bullets now carry each point, and each was checked:

- **PR #1241.** It is on `main` as merge `1257617a9` and commit `e806e52cb`; both are ancestors of
  `dfeec843`. After it, Main:216, :340 and :352 cite "the horizon ratio of (C2)'s realization
  clause".
- **The Bell items.** They are #1234's item 3, Main:414 and :416, and they remain with #1234. Main:20
  is stated not to be among them.
- **Main:74.** It reads "Realization — τ_S/τ_B ~ 10⁻³² at the horizon", which is GR:48's ratio. It
  now has its own row in the §R.2 trace table, classified as an illustration, not a dependency. The
  row pairs it with GR:48 and GR:456 ("not derived from the substratum dynamics"), and marks it an
  MC-5 candidate.
- **D18.** In §11 and in the §F.1 row, D18 now cites Main:74 and GR:48, and U-10's outcome cell
  records the reconciliation.

## N1: superseded citations

**Applied in modified form, and the modification is correct.** My third item was wrong. My earlier
search matched `derivedOI_qm_iff_layerFlowExecutable` as a prefix of
`derivedOI_qm_iff_layerFlowExecutable_swap'`. A boundary-aware search finds the unprimed key cited
nowhere:
- `git grep -P "derivedOI_qm_iff_layerFlowExecutable(?![_'A-Za-z])"` over `papers/` and `book/` at
  `origin/main` returns no match;
- a token count finds GR citing only the primed identifier and the `_swap'` identifier, and Main
  only the primed one.

The corrected statement in r8 §R.5 is accurate. It names two superseded identifiers at three sites:
- `oiPlusPos_iff_qm` at GR:242;
- `carrier_general_oiPlusPos` at GR:242 and Main:588.

Each sits beside its successor.

## Nothing else changed

- **Scope of the diff.** Besides the two items, the diff touches only the header lines naming the
  revision.
- **Identifiers.** A script comparison of the identifiers of r7 and r8 shows no change.
- **Unresolved findings.** There are still ten U rows.
- **New errors.** None. The Main:74 row adds a candidate and states its scope as a mention, not a
  dependency.
