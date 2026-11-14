# Response to the review of LEDGER-r1 (REVIEW-r1, verdict REVISE)

Paper-only, under the owner authorization on #914 (comment 6877420015). Each finding was checked
at its source on `main` (`dfeec843`; `papers/`, `book/` and `verification/` identical to
`c3b5f37a`) before it was applied. No file in the repository was edited, no computation was run,
nothing was posted. `LEDGER-r2.md` carries the result and is marked UNREVIEWED.

Dispositions: **applied**; **applied in modified form**, with the reason; **declined**, with the
reason. No finding is declined outright. Where the review is wrong in part, the lines are given.
"r1:n" is a line of `LEDGER-r1.md`; "Rv:n" a line of `REVIEW-r1.md`.

## Blocking

**B1 (black-hole "no instance"). Applied in modified form.**
Checked: `papers/GR.md`:805, 813, 815, 823–827, 829, 839; BH-02 `REPORT.md`:3, 14–16, 18–19;
`book/appendix-a-prediction-status.md`:102, 111.
- The review is right that the failure is scoped to definite initial configurations with an
  aligned bipartition, and that it comes from a bijection mapping configurations to
  configurations, not from finiteness (GR:813: "acting on a definite configuration, φ visits only
  configurations"; BH-02 C6(b): the cycle structure "contributes exact averaging bookkeeping").
  r1:294 ("conflicting with finite configuration orbits") misplaced the cause, and the Part 4 cell
  at r1:31, "Open (no instance)", dropped the scope.
- Partly wrong: the r1:31 status cell, "Page curve has no instance as stated", is GR:805's own
  phrase ("the theorem as stated has no instance (scope below)"), not a widening. The replacement
  is applied anyway because it carries the scope.
- r2: §0 BH row (status and Part 4 cells), §8.1 (bound S(ρ_R) ≤ H(p₀); C3 with its scope; BH-02
  standing and C1 coverage; the four routes left open), §8.2, §8.3, §8.5, §8.7. The C3 wording keeps
  BH-02's own labels: the superposition is supplied by the analyst, is not an OI mechanism, and C3
  "is not a derivation of H-scramble" (REPORT:16).

**B2 (negative claim about E and C). Applied in modified form.**
Checked: `oi-qm-ext-1/endpoints.md`:51–69; `oi-qm-ext-1/whole-model-bridge.md`:11–19, 21–30;
`oi-qm-ext-1/README.md`:24–43; `native-y-continuation-20261024/EQUIVALENCE-OBLIGATIONS.md`:73. I
also repeated the §A.19 search across `papers/`, `book/` and `verification/` for "sector condition",
"condition C", "extension E", "access closure" and "candidate extension".
- r1:58–60 was too wide; the review is right.
- Two corrections to the review's replacement (Rv:89–95):
  - "Its first state/readout bridge fails on every fixed finite carrier" is not the record's
    statement. The bridge fails because E-AR's preparations have no realization by density states
    and preparation-independent effects "on any one fixed finite-dimensional quantum carrier"
    (whole-model-bridge:13–16).
  - "'Composed observer-access closure' appears only as an obligation label" is too narrow. Access
    closure also appears as an open item in several native-y reports (e.g.
    `branch_v10/REPORT.md`:84) and as a hypothesis of a conditional composition theorem in a
    research draft (`composition-access-20261024/REPORT.md`:3–5, 34–39). The one corpus hit for
    "sector condition" (`verification/audits/manuscript/representation-sector-audit.md`:23)
    concerns superselection sectors. It is not a condition C.
- Other reconstruction records (e.g. `apparatus-1-20261107/`, `mechanism-1-20261107/`) assess
  further candidate mechanisms. r2 says that no full inventory was made, so it makes no claim that
  E-AR is the only candidate.
- r2: §1 closing paragraph; §2.3.
- NOTES: only the ledger and this response were written. NOTES-r1:72–73 is superseded by r2 §1,
  and the files read for r2 are listed below.

**B3 (missing OA-1, OA-2, OA-3, W1-1). Applied in modified form.**
Checked: OA-1 `STATUS.md`:43–77; OA-2 `STATUS.md`:33–37, 49–81; OA-3 `STATUS.md`:46–81; W1-1
`STATUS.md`:42–84; W1-1 `W1-1-REPORT-r4.md` §8 (the "Comparison with H-count").
- The records are on `main`, are relevant, and are missing from r1; the review is right.
- Modifications:
  - **Review status.** The review calls each record "agent-reviewed" (Rv:101, 130). OA-2's status
    note says the record and its last review "label every [W] and [RW] item an unreviewed hand
    derivation" (OA-2 STATUS:34–36). r2 says "independent AI-agent reviews of each report", notes
    OA-2's own labelling, and applies §A.46 items 1 and 7 (not established, not usable as an
    established premise).
  - **W1 and H-count, one direction at a time (§A.34).** The review writes "W1, the shell
    entropy–energy slope that H-count implies at GR:58" (Rv:115) and "W1, implied by H-count"
    (Rv:139–140). The source states one direction only. In reading L, GR:58's setting with H-count
    implies W1-0 and W1-min, and the converse fails by a witness (W1-1 STATUS:66–67; report §8,
    "⇒ holds" and "⇐ fails"). r2 §4.3 states exactly that.
  - **"A5 in tension with the QM branch"** (Rv:120). The records give obstructions inside the
    affine class under named observer hypotheses (H1, H-AR, H3, H4, SP, (xiv); for G_SM,
    Theorem S's conditions). The review's own S6 (Rv:257–258) says these are "not statements that
    a nonlinear update is needed". r2 states the results with their hypotheses, and gives the
    contrapositive reading as inferred (§2.1, last sub-bullet). It does not record a branch
    conflict.
- r2: §2.1 (new research-records bullet); §4.3; §9 QM–SM reason cell, taken nearly verbatim from
  Rv:124–129; M4; M9.
- The review links on PR #1173 and PR #1265 are classified in r2 §13 as provenance.

**B4 (exact inclusion against A1). Applied in modified form.**
Checked: `papers/Main.md`:356, 558, 560; `papers/Substratum.md`:92; `papers/GR.md`:585; #914 comment
6875046763 ("the target cannot assume one fixed finite total carrier").
- Correct: Main:558 proves the factorization half and imports the unboundedness from [55], with the
  conclusion "no fixed finite realization is exactly operationally equivalent to even a single
  qubit's full theory". r1's "undetermined" was wrong for one fixed finite S.
- Modification:
  - The QM–BH cell is changed as proposed.
  - QM–A1 is not a pair of branches, so it is placed as a stated conflict beneath the §9 table
    instead of as a table row.
  - M5 is rewritten to name the conflict and point to Q5.
- r2: §2.5; §9 QM–BH; the QM–A1 entry beneath §9; M5.

## Should-fix

**S1 (Bell–SM conditions). Applied.**
Checked: `papers/Main.md`:362, 412, 414; Main:724 item (x) ("on the reference vacuum/uniform state
class"); `papers/Substratum.md`:131, 171.
- Each condition in the review is at source, including:
  - the unstated (vii) status of the "equivalent nonlocal response map" (Main:412);
  - the exclusion of wings inside the graph cone (Main:414).
- r2: §3.1 (fifth bullet), §3.5, §9 Bell–SM.

**S2 (GR–SM conflict sits within SM). Applied in modified form.**
Checked: `papers/SM.md`:60, 104, 144, 158.
- Correct: the proved conflict is between SM §3.1's evolving graph and global A5. Both are SM
  premises, and GR's premises do not enter.
- Modification: rather than a §9 row named "SM §3.1–SM Stage 2(b)", which is not a pair of
  branches, the conflict goes in the "inside a branch" list beneath §9. That list now records it as
  "known not to" for global A5. The GR–SM row is marked undetermined, as the review proposes.
- r2 §4.5 is adjusted to match. Geometry-first ordering against SM §3.1 is left undetermined and
  sent to Q4, since no source states the two inconsistent.

**S3 (D4 omits Theorem 23). Applied.**
Checked: `papers/Substratum.md`:131–133, 193; `papers/Main.md`:414. A grep confirms the book
chapters carrying the preparation-indexed route (ch00, ch01, ch02, ch03, ch04, ch18, ch19) do not
carry the (vii) condition.
- r2: D4; §3.5.

**S4 (gauge-group classification). Applied.**
Checked: `papers/SM.md`:390 (Theorem 7b), 1424 (Tier 2, "the same fact stated in two directions").
- r2: §5.7 as proposed; §0 SM row (status and Part 4 cells); §5.1 (the two-directions quotation).

**S5 (QM scope and sourcing targets). Applied, with one addition.**
Checked:
- `papers/Main.md`:18, 80, 554, 588;
- `OIBridge/StructuralClosure.lean`:348–349, where `substratumGen_not_control` is stated at
  `Fin 2`;
- census families at `verification/lean-manuscript-census.json`:643, 661, 670, 679, 688.

The review's line 652 is the "state-mixing coupling construction" family, already cited in r1.
- **Addition.** The "dense-instrument bridge" family (:688) carries "discrete completion" from dense
  unitary control to dense finite QM, still not exact and nothing beyond `Fin 2` at the endpoint.
  It is listed, since leaving it out would understate the kernel-only state.
- **Scope.** The pair-flow equivalence family states "nothing generalized beyond Fin 2", and r2
  carries that.
- r2: §0 QM row; §2.1; §2.3 (Born exponent); §2.4; M2.

**S6 (unsourced "branches blocked"). Applied.**
Checked:
- `papers/GR.md`:815, 422–426, 466 (the cosmology chain uses horizon thermodynamics; GR's one use
  of graph curvature is the §8.7 consistency tool at :693, outside that chain);
- `papers/SM.md`:294;
- Main:724 (v).

Changes in r2 §10:
- **M2.** BH removed: its need is a preparation or a non-aligned partition (GR:815), which is M3,
  and M3's entry now says so.
- **M4.** QM and BH marked inferred.
- **M5.** GR marked inferred, with the reason (G3's continuum limit is a different completion).
- **M8.** Cosmology marked inferred.

A header line in §10 defines "inferred".

**S7 (Bell classification). Applied.**
Checked: `papers/Main.md`:360, 427; `papers/Substratum.md`:133, 193.
- With H-Bell's clause (i) being the required dependence itself, "CR" overstated what is
  reconstructed.
- r2: §0 Bell Part 4 cell; §3.7. §3.1 also records that the response-table construction realizes
  arbitrary finite stochastic laws (Main:360).

**S8 (A5 entry). Applied.**
Checked: `papers/Substratum.md`:100; Main:724 item (vii).
- r2: §1 A5 row as proposed.

**S9 (SM weakest link and first missing step). Applied in modified form.**
Checked: `papers/SM.md`:232.
- The table and §5.4 now agree, and §5.2's weakest link matches the table: H-χ′ (open), with H-link
  and H-cust conditional.
- Modification: the review asks for §5.4's wording, which said the observer-level lift comes
  "before" H-link and H-χ′. SM:232 lists what rests on the lift: §4's dispersion results, the
  Lorentz-invariance argument and Theorem 6's mode count. It does not place the lift before
  Theorem 7 or the carrier identification.
- r2 therefore lists the three steps and says that the sources state no order among them (§0 SM
  row; §5.4).

**S10 (owner questions partly answered). Applied, Q9 in modified form.**
Checked against the owner records:
- #914 comments 6875046763 (decision 3; "cannot assume one fixed finite total carrier"; "compatible
  model and operational interface"), 6875548603 (Bell exclusion "in the physical sector") and
  6877420015 (Part 4; "conditional reconstruction does not discharge");
- #1169 comment 6876591512 (answers 3 and 4).

Changes:
- **Q1, Q5, Q7.** As proposed. Q7 also names BELL-QSET under #1060 (below).
- **Q9 (modified).** The review proposes asking whether #1211 is "to be ordered before or after
  the QM sector work". That is a question about ordering and prerequisites. The ledger proposes
  none, and #914 comment 6877420015 states that no unit's prerequisites, ordering or readiness
  change. Q9 is kept as a scope question: does the forward SM trace count toward Part 4 only when
  the quantum description it consumes is derived in the same model?
- **Q12.** Added as the missing question.

## Nits

All checked at source.

| Nit | Disposition | Where in r2 |
|---|---|---|
| N1, the "fixes only ε/√σ" cite should be GR:306 and :547 | Applied | §4.1 |
| N2, SM:14 and SM:60 also cite [Substratum §3.3] | Applied | D2 |
| N3, D3 is not a disagreement (Substratum:373 cites both sources) | Applied | D3 reclassified "dual citation, consistent"; its identifier is kept; Q11 now lists D1, D2, D4 and D5 |
| N4, ch19:22 itself names an unresolved entry | Applied | D1 |
| N5, step (i)'s T_cl rests on H-count | Applied | D5, citing GR:422 and :58 |
| N6, A1 and A2 are also formalization gaps (census note at :470) | Applied | A note under the §1 table; the A6 row no longer carries the census remark |
| N7, the diff also rewords §A.46's opening paragraph and adoption line | Applied | r2 Base paragraph (confirmed by `git diff c3b5f37a dfeec843 -- AGENTS.md`) |
| N8, G8 is Layer 2(a) (appendix-a:109); GR:412 (iii) | Applied | §7.6, §7.7. §7.7 also gives a₀ (G6, Layer 0/1) and the budget (G9, Layer 1) their own table layers |
| N9, the factorization half is proved, the unboundedness imported; SIC exact over ℚ(√3) | Applied | §2.1 |
| N10, GR:352's selection condition | Applied | §6.7 |

## Planning facts reflected

Verified through the GitHub API:
- **#1060.** Body (question 3, BELL-QSET).
- **#1291.** Closed with `state_reason` "duplicate"; comment 6877802766.
- **#868.** Comment 6877804030.
- **#1143.** Title.

The owner decision is quoted verbatim, with its author and date: (`amaybaum`, 2026-11-14) "I approve,
proceed as suggested".

In r2:
- **§3.3.** The physical-sector exclusion is tied to BELL-QSET.
- **§3.4.** Gives the obligation's scope and the accountable Issues:
  - #1060, for H-Bell, Tsirelson selection and BELL-QSET;
  - #868, for the coverage direction;
  - #1143, for the related operational-selection problem;
  - #1291, as provenance only.

  It also states that assigning an Issue discharges no scientific obligation.
- **Q7.** Updated.
- **§13.** Classifies each reference.

## Changes not requested by the review

Each corrects a defect found while checking a finding.
- **§2.4, sector directions.** r1 asked for C "with both sector directions". #1169 comment
  6876591512, answer 2, requires coverage and soundness and makes necessity optional. r2 says
  "coverage and soundness directions".
- **§5.6, JUNO.** r1 called sin²θ₁₂ "a forward test". Appendix-a:98 and :211 class the current
  match as a retrodiction and name JUNO's design-lifetime precision as the pre-registered forward
  test. r2 states both.
- **§1 and §3.1, ledger item (x).** Item (x) is scoped to the reference state class, as Main:724
  states.
- **§13 (new).** The §A.42 item 8 tracing moves into the ledger, since r2 adds off-`main`
  references.

## Read for r2, beyond NOTES-r1

- **`papers/`.**
  - `papers/GR.md`:306, 352, 412, 422, 547, 585, 605, 805–839.
  - `papers/Main.md`:18, 80, 356, 360–362, 412–414, 427, 554, 558–560, 588; ledger items (v),
    (vii), (x) and (xiv) of :724.
  - `papers/SM.md`:14, 60, 104, 144, 158, 232, 294, 390, 1424.
  - `papers/Substratum.md`:92, 100, 131–133, 171, 193, 373.
- **`book/`.** `appendix-a-prediction-status.md`:98, 102–113, 123, 211; `ch19-open-problems.md`:20–22;
  and a search for "preparation-indexed" across the chapters.
- **`verification/programmes/oi-qm/reconstruction/`.**
  - `oi-qm-ext-1/README.md`:1–60, `endpoints.md`:1–80 and `whole-model-bridge.md`:1–30.
  - `native-y-continuation-20261024/EQUIVALENCE-OBLIGATIONS.md`:1–8, 68–76.
  - `composition-access-20261024/REPORT.md`:1–42.
  - The `STATUS.md` files of `oa-1-20261112/` (in full), `oa-2-20261112/` (in full) and
    `oa-3-20261112/`.
- **Other `verification/` records.**
  - `verification/programmes/physical-realization/w1-1-20261112/STATUS.md` and
    `W1-1-REPORT-r4.md`, §8 and the W1 and H-count definitions.
  - `verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md`:1–40.
  - `verification/audits/manuscript/representation-sector-audit.md`:1–30.
  - `verification/lean-manuscript-census.json`, the families at :470 and :636–690.
  - `OIBridge/StructuralClosure.lean`:348–354.
- **Owner records and Issues, through the API.**
  - #914 comments 6875046763, 6875548603 and 6877420015.
  - #1169 comment 6876591512.
  - #1060: the body and comments after 2026-11-13.
  - #1291: its state and comments.
  - #868: comments after 2026-11-13.
  - #1143: its title and state.

Not done: no Lean build, no script run, no reading of PR #1289 or other off-`main` drafts.
