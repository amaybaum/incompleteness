ACCEPT WITH CHANGES

# Independent review of LEDGER-r6 and RESPONSE-LC-1

This review is read-only, paper-only and non-author. It covers `diff LEDGER-r5.md LEDGER-r6.md`
and `RESPONSE-LC-1.md`, checked at `main` (`dfeec843`).

Fifteen owner and Issue comments were read through the API:
- #914 comments 6880010243 and 6879158095;
- the thirteen per-Issue comments listed by the coordinator.

The bodies of #1234 and #1063 were also read. No file was edited, no computation was run and
nothing was posted.

## 1. LC-1: the three T-6 rows

**B-STR-5** (the hierarchy) is correct. Each of its quotations matches its source line:

| r6 quotes | Source |
|---|---|
| "canonical for the framework", "where each technical result lives" | Structure:102 |
| "The hierarchy nests: Level A ⊃ Level B ⊃ Level C ⊃ Level D" | Structure:144 |
| "Apart from the G3–G4 relation … not established" | Structure:158 |

PE is right for a classification scheme whose nesting holds by definition.

**C-STR-7** (the placements) is correct.
- §2.3–§2.5 (Structure:162–198) and §12.4 (:892–954) are covered.
- "Forced uniquely in OI, conditionally on H-link and H-cust" is quoted from :168.
- The :179 against :191–192 contradiction stays a manuscript-correction candidate (F-17). §F's
  F-17 row now cross-references C-STR-7 and keeps the MC cell.

**C-STR-8** (the Born test) is correct and carries its T flag. The quotations match their sources:

| r6 quotes | Source |
|---|---|
| "Born rule … Confirmed at 10⁻³–10⁻⁴" | Structure:900 |
| "A Born rule test at 10⁻⁵ precision confirms Level 1" | Structure:950 |
| "trivially 'predicted'", "Not falsifiable within the framework" | Structure:177 |
| "do not distinguish OI from alternative frameworks" | Structure:906 |

The T flag is defined in the vocabulary. The class wording is tightened in N1 below.

**Two observations recorded for LC-2.** Both are correct at source:
- Structure:198 places the empirical content at "Level D × Level G3".
- The A/4 entries appear at :903–904 and at :926.

N2 adds two more.

## 2. LC-7: the D8 mirror cells

**Met.** FULL:2894 is byte-identical to `book/ch10-chemistry.md`:86, and FULL:2896 to :88 (checked
with `cmp`). D8 in §11 and its §F.1 cell now cite both.

## 3. §H, the Issue homes

**Checked against the owner record.** Each §H.1–§H.3 row matches #914 comment 6880010243 ("I adopt
these, with Option A and r4's specific homes") and the per-Issue record it cites:

| Rows | Record |
|---|---|
| MC-1 to MC-5 | #1028 comment 6880012900; the units and authorizations are verbatim in substance |
| F-32, and F-3's Higgs clauses at Substratum:152 and :201 | #1058 comment 6880013690 |
| D7 | #1190 comment 6880014644 |
| D5 and F-7 | #1142 comment 6880015405 |
| S-1, S-2, M-33 and U-10 | #1238 comment 6880016318 |
| F-17 (:179), G-30 and T-4 | #1244 comment 6880017798 |
| D2 | #1029 comment 6880018502 |
| F-10 | #1015 comment 6880019139 |
| RO-1, S-J, S-A and EXACT | #1169 comment 6880022363 |
| J-1, J-2, and the scope quotation | #1234 comment 6880023408 |
| RO-3, and the scope quotation | #1055 comment 6880024537 |
| M9 | #1245 comment 6880025217 |
| U-2 | #1062 comment 6880025953 |

Each authorization quote is accurate.

**The LC-8 claim is correct.** `QUEUE-PROPOSAL-r4.md`:184 and :599 define LC-8 as recording homes
for J-1, J-2 and M1–M9, and propose homes only for J-1, J-2, M1 and M9. All four are recorded:
- J-1 and J-2 at #1234;
- M1 at #914, O-IF-SELECT;
- M9 at #1245.

LC-8 is therefore closed only for those four, as r6 says. RO-7 is correctly listed as undecided.

### Should-fix S1. §H.4's "No home named" list is too wide, and contradicts r6's own pages.

r6 says D4, M2 to M8, and the RO parts of F-14, F-19 and U-3 have "no home named by these records".
That is true of the assignment record, which lists twelve homes and none of these. But several items
do have accountable Issues named in the ledger or in existing Issue bodies:

- **D4.** #1234's body, open item 2 ("Companions and book … The book has not been swept for this"),
  already tracks D4's content. `QUEUE-PROPOSAL-r4.md`:233 identifies D4 as "#1234 item 2".
- **M5.** r6's own §H.3 row for #1055 says the RO-3 inventory "bears on J-3, J-4 and M5".
- **M6 (G3).** The ledger names #873 as accountable for the G3 coupling step (§4.1, B-GR-6).
- **M2.** §2.4 names #1169 and #1236 as accountable for the operation that supplies condition (iv).
- **U-3.** B-QCD-6 and B-SM-GAUGE-5 link the mass gap and gauge dynamics to #1063, by #914 comment
  6877908458. `QUEUE-PROPOSAL-r4.md`:867 places U-3 (RO-10) under #1063's existing scope.

Replace §H.4's second bullet and its LC-8 sentence with:

"**Not assigned by the 2026-11-14 decision.** D4, M2 to M8, and the RO parts of F-14, F-19 and U-3
received no new assignment. Existing records already name:
- for D4, #1234 open item 2 (its body);
- for M2, #1169 and #1236 (§2.4);
- for M5, #1055 (RO-3, §H.3);
- for M6, #873 (§4.1);
- for U-3, #1063 (#914 comment 6877908458; B-QCD-6).

No home is recorded for M3, M4, M7 and M8, or for the RO parts of F-14 and F-19. LC-8 is closed for
J-1, J-2, M1 and M9; RO-7's home is undecided."

## 4. Nothing else changed

- **Scope of the diff.** The diff touches only:
  - the header and history;
  - the T definition and the "(r6)" provenance note;
  - the three new rows;
  - D8 in §11 and §F.1;
  - F-1, F-17, the Missing-coverage note and U-1;
  - the Q2 and Q5 pointers to §H, which RESPONSE-LC-1 discloses;
  - the new §H;
  - two §13 rows.
- **Identifiers.** A script comparison of r5 and r6 shows no identifier removed, and exactly
  B-STR-5, C-STR-7 and C-STR-8 added.
- **Unresolved findings.** There are still ten U rows. U-1 remains unresolved pending LC-2.

## Nits

- **N1. C-STR-8's class.** "DM for the Born form at the represented level" could be read as a
  derivation of the Born rule. Tighten it to "DM only as part of B-QM-1: Q_fb is defined with the
  Born dictionary (`papers/Main.md`:18, "does not select the quadratic exponent"); not a derivation
  of the Born rule; exponent UO (B-QM-11); T".
- **N2. Inputs for LC-2.** Two more observations for the Missing-coverage note:
  - Structure:168 and :178 repeat "Forced uniquely in OI". This is the wording F-17 cites at :703,
    while the cubic lattice is EF (B-SM-4).
  - Structure:913 lists "Three chiral generations | Confirmed" at Level 2, while chirality is open
    (B-SM-7) and generations are conditional on H-spin′.
- **N3. D2.** #1029 comment 6880018502 records Introduction:179 as also citing §3.2. D2 lists only
  :145; add :179.
- **N4. §H.3, #914 row for M1.** "As recorded in that row" has no referent. Write "assigned in #914
  comment 6880010243; no separate authorization recorded".
- **N5. §H.4, "Not decided".** The owner record also lists "any QB5(a) execution" and "any merge".
  Add both for completeness.
