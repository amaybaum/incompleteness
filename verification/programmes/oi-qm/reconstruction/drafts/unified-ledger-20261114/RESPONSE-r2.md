# Response to the review of LEDGER-r2 (REVIEW-r2, verdict ACCEPT WITH CHANGES)

This work is paper-only, under #914 comments 6877420015, 6877871344 and 6877908458. No repository
file was edited, no computation was run on OI rules and nothing was posted. Sources were read on
`main` at `dfeec843`, re-fetched when r3 was written. LEDGER-r2 and REVIEW-r2 are unchanged: their
SHA-256 digests begin `ecc51e74` and `339a6129` before and after this work. They are preserved on
draft PR #1292 at `7971631f`. `LEDGER-r3.md` carries the result and is marked UNREVIEWED.

## A. Findings of REVIEW-r2

Each finding was checked at its source before it was applied. "Rv2:n" is a line of `REVIEW-r2.md`.

**S1 (W1-1's C6(a) dropped). Applied.**
- **Source check.** `verification/programmes/physical-realization/w1-1-20261112/STATUS.md`:60–62
  states the finding: the gap route C6(a) is "open for the finite substratum", and in the real
  lift of the linear rule (|α| < 1/d) "it fails".
- **The review is right.** REVIEW-r1 named this route (its B3), and r2 omitted it without a
  disposition.
- **Changes in r3.** §4.3 adds the sentence the review proposed. M9 adds the clause the review
  proposed, citing :60–62. Registry entry B-GR-7 records the failure as NEG. The finding bears on
  Q2, which is about linearity.

**N1 (W1 labels in §4.3). Applied.**
`W1-1-REPORT-r4.md`:301–302 calls W1-0 the "prerequisite" and W1-min the condition "on GR:58's
counted set". §4.3 now reads "implies its prerequisite W1-0 and its counted-set form W1-min (reading
L)" and cites :301–302.

**N2 (where the Bell decision is recorded). Applied.**
#914 comment 6877803663 was read through the API. Its author is `amaybaum`, it was created at
2026-11-14T13:13:09Z, and it quotes "I approve, proceed as suggested". §3.4 now cites that comment
and #1060's body after the quotation (§A.42 item 7). §13 classifies the comment as provenance.

**N3 (carrier scope of the pair-flow endpoint). Applied.**
The "operational pair-flow equivalence" census note says "nothing generalized beyond Fin 2". The
second bullet of §2.4 now says "on the two-valued carrier".

**N4 (Q9). Applied.**
Q9 now leads with the open part: whether a forward SM trace that consumes E1 is recorded as an
intermediate result. The point that it does not discharge the obligation follows as settled
(#914 comment 6877420015).

**Points in REVIEW-r2 that need no change.**
- The review's correction of its own earlier B1 reading (Rv2:19–22) agrees with RESPONSE-r1.
- Its OA note that Theorem S needs no (CVX) (Rv2:39–40) confirms r2's text.

## B. The owner's expansion

**Sources read through the API.**
- #914 comment 6877871344 (`amaybaum`, 2026-11-14T13:19:06Z). It records the owner's confirmation,
  "Yes, this is my decision, proceed as planned", and the seven conditions.
- #914 comment 6877908458 (`amaybaum`, 2026-11-14T13:22:18Z). It records "Yes, I approve adding the
  QCD group to r3" and lists the eleven obligations.
- #1063: its body, which quotes the frozen roadmap. Those roadmap lines were confirmed on `main` at
  `verification/ROADMAP.md`:1525–1536.
- #1003: a closed pull request, cited as provenance only.

The r3 header quotes the decisions and the operative sentences of the conditions verbatim.

**How r3 implements each condition.**

1. **Timing.** r3 starts after REVIEW-r2, and r2 and its review are unchanged (digests above).
2. **Levels.**
   - **New section §L.** It is the registry. Level A (§L.A) has four obligation rows: A-QM, A-BELL,
     A-GR and A-REAL, all UO, each cross-referenced to its partial results. Level B (§L.B) lists
     derivation claims by branch. Level C (§L.C) lists predictions, phenomenology and scope limits.
   - **Identifiers.** Each entry has a stable ID (A-*, B-<branch>-n, C-*), which the coverage audit
     can cross-reference. IDs are not ordinals and are not reused.
   - **Branch detail.** The detail of r2 §0–§13 is kept and referenced from the registry.
3. **Evidence classes.** Every registry row carries one of five classes: DM, CD[hypotheses], EF, PE
   or UO. A separate NEG flag records negative results and explicit failures. Examples:
   - B-QM-4, B-QM-8 and B-QM-12;
   - B-BELL-4 and B-BELL-5;
   - B-GR-4 and B-GR-7;
   - B-SM-6, B-SM-7 and B-SM-CP-2;
   - B-SM-BARY-3 and B-SM-BARY-4 (the leptogenesis shortfall, and the retracted instanton mechanism);
   - B-SM-GAUGE-3 and B-SM-GAUGE-4 (Haar confinement, and the polar map giving a Haar pushforward);
   - B-SM-NP-2 (archived code not extant, and Z_S universality violated);
   - B-BH-2 and B-BH-3.

   The support layer (K, XA, EX, P, N, RR, BK) is kept separate from the class, so a kernel
   theorem under a posited input reads CD with support K.
4. **Common model.**
   - **DM.** The class is scoped to results that hold for every model of the bare finite class
     (`papers/Main.md`:42, :724 items (ii)–(iii)). Its use therefore does not depend on which common
     model is chosen.
   - **§1.** It is retitled "Inputs the corpus states for the observation triple". It now says that
     items (vii) and (ix)–(xiii), with the Stage-2 inputs, specify the lattice model the SM branch
     uses (`papers/SM.md`:60), and that r3 does not treat that model as the common model.
   - **Q13.** Added; it asks which model is the common model.
5. **Part 4 entries.**
   - **Named entries.** B-P4-AOT (arrow of time), B-P4-MEAS (measurement problem) and B-P4-QCB
     (quantum–classical boundary).
   - **SM subquestions.**
     - B-SM-CP: strong CP.
     - B-SM-HIER: the Higgs hierarchy.
     - B-SM-FLAV: flavour and masses.
     - B-SM-NU: neutrinos.
     - B-SM-BARY: baryogenesis.
     - B-SM-GAUGE: gauge dynamics and confinement.
     - B-SM-NP: nonperturbative effects.
   - **QCD group.** B-QCD-1 to B-QCD-11, in the order of #914 comment 6877908458, inside the SM
     branch. Existing entries are cross-referenced, not duplicated (B-QCD-9 and B-QCD-10, for
     example, point to the SM-CP and SM-NP groups).
   - **Yang–Mills and QCD kept apart.** Pure Yang–Mills (B-QCD-6, the mass gap) is distinct from
     full QCD (B-QCD-5 confinement, B-QCD-8 hadron spectrum).
   - **Accountable Issue.** Gauge dynamics, action selection and the mass gap link to #1063, and
     PR #1003 is provenance only (§L.B, §13).
   - **Cross-checks.** Reproductions of known calculations are marked XC: B-QCD-4 (SM running),
     B-QCD-7 (chiral symmetry breaking in standard-measure Monte Carlo) and B-SM-NP-1.
   - **No fifth part.** None is created. The new entries sit under Levels A–C of the existing
     four-part target.
6. **Level C items from the owner's list.** Each takes only the status its source supports:
   - C-QCDVAC: QCD vacuum energy and gravitational coupling (`papers/GR.md`:579, 581, under §6.2's
     geometry-first proposal and the open G3 step).
   - C-EARLY-1 to C-EARLY-5: early-universe physics.
   - C-OBS: observer selection (`papers/Main.md`:742–758).
   - C-HUBBLE: the Hubble tension (`book/ch19-open-problems.md`:168–172, "the effect is too
     small").
   - C-TOPO: cosmic topology (`book/ch18-beyond.md`:228–262).
   - C-CONJ-1 to C-CONJ-4: the explicitly conjectural applications.

   The earlier prediction and test entries (C-PRED-1 to C-PRED-9) and the precision-sector scope
   limit (C-ANOM) are added from r2 and their sources.

**Tracing.** Every status cell in §L cites the source line that states it. The negative entries
rest on recorded searches (§A.19):
- **B-QCD-8.** `papers/` was searched for "hadron", "pion" and "proton mass", which found only
  `papers/GR.md`:581.
- **D8.** `book/ch05-gauge-structure.md` §5.4 was read for a confinement statement and has none.

Every off-`main` reference is classified in §13 under §A.42 item 8. None supports a scientific
status: each is planning or owner provenance.

**Found while building the registry; recorded, not resolved.** The coverage audit is a separate
later task. These were found incidentally while the registry was built:
- **D7.** `book/ch18-beyond.md`:256 calls the local chirality "derived", while SM:543 and :1320 and
  ch19:328 give H-χ′ as open.
- **D8.** `book/ch10-chemistry.md`:86–88 calls confinement and nuclear binding "derived". It cites
  ch05 §5.4, which carries no confinement statement.
- **D9.** `book/ch19-open-problems.md`:88 states that cutoff sensitivity is eliminated, while SM:613
  and :1570 defer the derivation.
- **D10.** `book/ch10-chemistry.md`:78–80 calls the possibility of baryogenesis "a theorem" from
  ingredients that rest on H-spin′, H-χ′ and solution-specific CP phases.
- **Q14.** Added. It asks whether the mass gap, confinement and the hadron spectrum are Part 4
  obligations or recorded scope limits. The papers state that the mass-gap proof is "not required"
  (`papers/Substratum.md`:225; `papers/SM.md`:1448), while #914 comment 6877908458 lists them as
  coverage obligations.

**Limits.**
- **Level B is not exhaustive.** It holds the derivation claims this record found. Condition 6's
  audit of Main, Substratum, SM, GR and Structure, with ch18–19 as controls, is expected to add
  entries. Structure in particular was not swept.
- **Biological entries not classified.** Appendix-a entries B1–B14 and F1–F9 are named in §L.C but
  not classified, and are left to the audit.
- **Inclusion is not derivation.** No entry adopts a claim or a premise, and none changes a status,
  tier, readiness or authorization.

## Read for r3, beyond RESPONSE-r1

- **`papers/`.**
  - `papers/Main.md`:322, 680–692, 740–758.
  - `papers/Substratum.md`:56, 225, 399–415, 461–465.
  - `papers/SM.md`:34, 300–308, 489, 519–525, 601–613, 665–671, 789–843, 1114–1128, 1142–1152,
    1318–1322, 1448, 1450–1468, 1484–1490, 1538–1584. Also the section headings.
  - `papers/GR.md`:338–358, 569–581, 693, 739.
- **`book/`.**
  - `book/ch18-beyond.md`: §18.1, §18.3, §18.8 and §18.9, plus the conjecture and status lines.
  - `book/ch19-open-problems.md`: §19.2.5–§19.2.8, §19.3.1–§19.3.5 and §19.4.
  - `book/appendix-a-prediction-status.md`: the prediction tables.
  - `book/ch10-chemistry.md`:16, 78–88.
  - `book/ch05-gauge-structure.md`: the headings, and §5.4 for "confine".
- **Other records.**
  - `verification/ROADMAP.md`:1525–1536.
  - `W1-1-REPORT-r4.md`:298–303.
  - W1-1 `STATUS.md`:60–62.
- **Owner records and Issues, through the API.**
  - #914 comments 6877803663, 6877871344 and 6877908458.
  - #1063: its body and state.
  - #1003: its state.

Not done:
- no Lean build;
- no script run;
- no reading of PR #1292 beyond the commit the coordinator named;
- no coverage audit.
