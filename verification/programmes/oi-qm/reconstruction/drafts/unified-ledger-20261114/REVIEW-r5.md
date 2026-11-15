ACCEPT

# Confirmation review of LEDGER-r5

This review is read-only, paper-only and non-author. It reviews `diff LEDGER-r4.md LEDGER-r5.md`
together with `RESPONSE-r4.md`. No file was edited, no computation was run and nothing was posted.

## Owner's four checks

**1. J-3 and J-4 have their conditions restored: MET.**
- J-3 now reads "known not to, on one fixed finite carrier, under the factorization interface of
  `papers/Main.md`:558 (unboundedness imported)".
- J-4 now reads "known not to, on one fixed finite S under that interface; undetermined on a
  completion".
- Both match §9 and Main:558. Main:558 proves the factorization half and imports the
  unboundedness.

**2. Q13 is aligned with the common-model (DM) definition: MET.**
- Q13 now ends "Whether each DM result holds in the answer depends on whether that model is a
  member of the bare finite class (§L evidence classes; Q5)". This agrees with the DM definition at
  r5:70–76.
- Its item list reads "(vii)–(xiii) and H-link", matching §1.

**3. The accepted audit r4 is cited: MET.**
The header, the §F preamble, U-1, U-10 and §13 cite `COVERAGE-AUDIT-r4.md` as accepted by
`REVIEW-AUDIT-r4.md`. `REVIEW-AUDIT-r4.md` opens "ACCEPT". The sections cited exist in audit r4:
- §3, "Findings register", at :160;
- §4.5, at :906;
- §8, "Book-control findings", at :1123.

COVERAGE-AUDIT-r1 to r3 and REVIEW-AUDIT-r1 to r3 appear only as history: in the header and in a
separate §13 row classed "Provenance only".

**4. All 10 unresolved findings remain explicit: MET.**
- §U has rows U-1 to U-10, and its count sentence reads "These ten findings".
- Only U-1 and U-10 changed. U-1 now cites audit r4. U-10's passage B now states that the audit
  names no companion passage, and that the paired passage is to be fixed by the trace.
- None is marked resolved.

## REVIEW-r4 findings

Each was checked at source and applied as proposed.

- **S1.** The Level A ranges were updated:
  - A-QM: B-QM-1 to B-QM-28, plus B-SUB-1 and B-SUB-2.
  - A-BELL: B-BELL-1 to B-BELL-9.
  - A-GR: B-GR-1 to B-GR-12.
  - A-REAL: B-SUB-1 and B-SUB-2.

  The new upper bounds are the highest identifiers in the registry.
- **S2 to S4.** As above.
- **N1.** B-QM-22 support is now K, naming the three kernel results Main:590 cites.
- **N2.** B-GR-12 is now CD[H-link; minimal-coupling factorization δ = 1], following GR:104.
- **N3.** B-QCD-9 and B-QCD-10 now read "class per the cross-referenced rows".
- **N4.** §5.1 points to the C-PRED-1 sub-rows and to F-6, F-25 and F-35.
- **N5.** C-EARLY-6 carries a group note, and its identifier is kept.
- **N6.** B-STR-2 carries "preliminary structural conclusions", quoted from Structure:1030.
- **N7.** U-10 is as described under check 4.

## Scope, identifiers and errors

- **Nothing else changed.** The diff touches only the items above and the revision-naming header
  lines.
- **Identifiers are stable.** The set of row identifiers is identical between r4 and r5, compared
  by script. There are ten U rows.
- **No new errors.** The changed cells add conditions or citations and remove none. None
  strengthens a status.

## Optional nit

Two sentences carried over from r4 still use "r4" to name the revision. At r5:98, "Rows added in
r4" is correct as history. At r5:1060, "The guidance r4 applies" would read better as "The guidance
the ledger applies". Neither is a status issue.
