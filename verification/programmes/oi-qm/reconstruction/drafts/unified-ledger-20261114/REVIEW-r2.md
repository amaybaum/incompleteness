ACCEPT WITH CHANGES

# Independent review of LEDGER-r2 and RESPONSE-r1

This review is read-only, paper-only and non-author. `main` is `dfeec843`, re-fetched by name for
this review. Sources were read at `c3b5f37a`; the only difference between the two commits is
`AGENTS.md`. No file was edited, no computation was run and nothing was posted. Levels A, B and C,
the QCD group, and the arrow-of-time and measurement entries belong to r3 (#914 comments
6877871344 and 6877908458). Their absence from r2 is not a finding.

## Dispositions in RESPONSE-r1

Every finding was applied. The places in r2 named for each finding exist and carry the change.

**Findings applied in modified form.**

- **B1 (black-hole scope).** The modification is sound. r2 scopes the failure correctly in §0,
  §8.1, §8.2, §8.3, §8.5 and §8.7. It cites C2 and C3 with BH-02's own labels (REPORT:3, 14–18)
  and lists the four routes that remain open (GR:815, 827, 829). One point in the response stands.
  My review called the r1 status phrase a widening, but r1 had paraphrased GR:805's "the theorem as
  stated has no instance". It only changed the subject from "the theorem" to "Page curve". The
  r1 Part 4 cell remained a widening.
- **B2 (extension E and condition C).** The modification is sound, and both corrections of my
  replacement text are right:
  - `whole-model-bridge.md`:13–16 says "on any one fixed finite-dimensional quantum carrier". My
    wording, "every fixed finite carrier", was looser than the source.
  - Access closure does appear beyond `EQUIVALENCE-OBLIGATIONS.md`:73. It is "remain open" at
    `branch_v10/REPORT.md`:84, and a hypothesis of the conditional theorem in
    `composition-access-20261024/REPORT.md`:3–5 and :34–39.
  - The "sector condition" hit at `representation-sector-audit.md`:23 is about superselection.
  - The quotations at `endpoints.md`:69 and `whole-model-bridge.md`:17–19 are exact.
  - The statement that no inventory was made is properly scoped.
- **B3 (OA-1, OA-2, OA-3 and W1-1).** The modification is sound on the two points the response
  raises:
  - OA-2's STATUS:34–36 labels its [W] and [RW] items "unreviewed hand derivations".
  - W1-1 STATUS:66–67 states one direction only: GR:58's setting with H-count implies W1-0 and
    W1-min(L), and the converse fails. My phrase "W1 … that H-count implies" overstated this.

  r2's OA citations match the sources (OA-1 STATUS:48–59, OA-2 :56–69, OA-3 :48–67). Theorem S
  uses Proposition B(i) and B(ii)(⇐) only (OA-3 r4:339–352), so it needs no (CVX). The
  contrapositive in §2.1 is valid and is labelled as inferred. One part of B3 was dropped with no
  disposition (S1 below).
- **B4 (exact inclusion against A1).** The modification is sound. QM–A1 is a conflict with a
  common-model input, not a pair of branches. r2 states it beneath §9 with both of its conditions:
  the factorization interface, and the unboundedness imported at Main:558. The QM–BH cell and M5
  agree with it.
- **S2 (GR–SM conflict).** The modification is sound. r2 records the conflict between SM §3.1 and
  global A5 inside the SM branch, beneath §9 (SM:104, 158; Main:362). It marks GR–SM undetermined.
  It also sends the ordering question (geometry-first against SM §3.1) to Q4, since no source states
  them inconsistent. §4.5, §5.5 and §6.5 agree with that.
- **S9 (SM steps).** The modification is sound. SM:232 lists what rests on L_obs: §4's dispersion
  results, the Lorentz-invariance argument and Theorem 6's mode count. It does not place the lift
  before H-link. r2 now lists the three steps without an order, and the §0 table, §5.2 and §5.4
  agree.
- **S10 (owner questions).** The modification is sound. My proposed Q9 asked about ordering, and
  #914 comment 6877420015 states that no ordering or readiness changes. The response is right to
  decline it. Q1, Q5 and Q7 match the owner records (6875046763, 6875548603, and #1169 comment
  6876591512, answers 3 and 4). Q12 is added.

**Findings applied as proposed.** S1, S3, S4, S5, S6, S7, S8 and N1–N10 were checked at their r2
locations. S5's addition of the "dense-instrument bridge" family is correct: the census note says
"nothing beyond Fin 2 at the endpoint", and that it is "still not exact quantum mechanics".

**Changes the review did not request.**

- §2.4 uses "coverage and soundness directions". This matches #1169 comment 6876591512, answer 2.
- §5.6 says JUNO is a retrodiction now, with a forward test at design-lifetime precision. This
  matches appendix-a:98 and :211.
- (x) is scoped to the reference class, as Main:724 states.
- The new §13 traces the off-`main` references.

All four are correct.

## Bell planning records

These were checked against #1060's body, #1291 (closed as a duplicate; comment 6877802766), #914
comment 6877803663 and #868 comment 6877804030.

- §3.3 and §3.4 use BELL-QSET, which is #1060 question 3. They state its whole-interface scope and
  the requirement that C be justified without testing for quantum correlations.
- The coverage direction is assigned to #868, and the related selection problem to #1143.
- #1291 is cited only as the place the scope was first drafted. §13 classifies it as provenance
  only and #1060 as a planning record.
- §3.4 states that assigning an Issue discharges no obligation. This is correct.

## Should-fix

**S1. The W1-1 C6(a) finding was dropped without a disposition.**
Locations: §4.3 and M9 (§10).
Source: `verification/programmes/physical-realization/w1-1-20261112/STATUS.md`:60–62.

W1-1 finds one distinct sufficient route for W1, the gap route C6(a). That route is open for the
finite substratum and fails in the real lift of the linear rule. It is a finding about A5's rule
class, and Q2 (linearity) depends on such findings. r2 does not mention it.

Add to §4.3, after "…the converse fails by a witness (…:48–59, 66–67)": "The one distinct
sufficient route found, a deep sector whose thermally accessible configurations are collective
(C6(a)), is open for the finite substratum and fails in the real lift of the linear rule,
|α| < 1/d (W1-1 STATUS:60–62; paper-level)." In M9, after "Main's posit ledger", add "; the C6(a)
route fails in the real lift of the linear rule (STATUS:60–62)".

## Nits

- **N1 (§4.3).** "Implies its minimal form (W1-0 and W1-min, reading L)" uses a label the source
  does not use. W1-1 calls W1-0 a "prerequisite" and W1-min the condition "on GR:58's counted set"
  (W1-1-REPORT-r4:301–302). Replace the phrase with "implies its prerequisite W1-0 and its
  counted-set form W1-min (reading L)".
- **N2 (§3.4).** The owner quotation gives the author and date but not where the decision is
  recorded or when. Under §A.42 item 7, add "(#914 comment 6877803663, 2026-11-14T13:13:09Z; also
  #1060's body)".
- **N3 (§2.4, second bullet).** The real pair-flow endpoint does not state its carrier scope. The
  third bullet does. Add "on the two-valued carrier" after "exact finite operational QM", as the
  pair-flow equivalence family states ("nothing generalized beyond Fin 2").
- **N4 (Q9).** Part 4 already states that a conditional reconstruction "does not discharge" the
  obligation (#914 comment 6877420015). The open part of Q9 is narrower: whether an E1-consuming
  forward trace is recorded as an intermediate result. Consider leading with that.

## No new errors found in

- §0, §1 (including the A1–A6 kernel note, which matches the census at :470) and §2.1–§2.7.
- §3, §5.4–§5.7, §6.7, §7.6–§7.7 (matching appendix-a:109 and :111), §8, §9 and the entries
  beneath it, §10 to §13 and D1–D6.

Every new citation I sampled resolves to its stated content at `dfeec843`.

## Checked by the reviewer

- **Owner records and Issues, read through the API.**
  - #914 comments 6877803663, 6877871344 and 6877908458.
  - #1291 comment 6877802766, and #868 comment 6877804030.
  - The bodies and states of #1060, #1291 and #1143.
- **Ledger files.** LEDGER-r2 and RESPONSE-r1, read in full.
- **Planning and research records.**
  - `oi-qm-ext-1/endpoints.md`:51–69, and `whole-model-bridge.md`:11–30.
  - `branch_v10/REPORT.md`:84, `composition-access-20261024/REPORT.md`:1–8 and :34–39.
  - `representation-sector-audit.md`:23.
  - OA-2 STATUS:33–37 and :56–69; OA-3 STATUS:46–67.
  - OA-2 r4's (CVX) lines, and OA-3 r4's use of Proposition B.
  - W1-1 STATUS:42–73, and W1-1-REPORT-r4:298–311.
- **Census.** The notes of the five families cited in §2.4.
- **Book.** appendix-a:211.
