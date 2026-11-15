# Queue proposal r3: manuscript corrections, ledger coverage and research obligations, grouped by Issue

**UNREVIEWED. Proposal for owner decision.** r3 revises `QUEUE-PROPOSAL-r2.md`, which is left unchanged.
It applies the owner's direction to group the changes by Issue; the disposition of each point is in
`RESPONSE-QUEUE-r2.md`. r2 applied the independent review `REVIEW-QUEUE-r1.md` (dispositions in
`RESPONSE-QUEUE-r1.md`). This document decides nothing. It changes no manuscript wording, tier,
readiness, authorization, Issue, label, Project card or queue. Every proposed change of planning
attribute, and every proposed assignment of an item to an Issue, is marked **(proposal)** and takes
effect only by a recorded owner decision (`AGENTS.md` §A.45 rule 3, line 1225 on `main`: "**A priority
is never authorization.**"). The work was read-only and paper-only: no computation on OI rules was run,
and nothing was committed, pushed or posted.

**The owner's direction for r3**, relayed by the coordinator and quoted verbatim (`amaybaum`,
2026-11-14, in the coordinating session): "Let's try to group the changes by Issue, no need to create a
separate Issue for each existing manuscript correction." No GitHub record of it was available when r3
was written.

**Inputs.**
- `LEDGER-r5.md`, reviewed by `REVIEW-r5.md` (verdict ACCEPT) and accepted by the owner on #914 in
  comment 6879158095 (`amaybaum`, 2026-11-14T14:50:47Z): "Yes, I accept ledger r5". The accepted text
  is r5 as preserved on draft PR #1292 at `de29ccd8`. The acceptance "covers the ledger as a record of
  evidentiary status" and does not "change any manuscript text, Issue priority, tier, readiness or
  authorization" (same comment). Row identifiers are those of r5, which changes no identifier of r4.
- `COVERAGE-AUDIT-r4.md`, accepted by `REVIEW-AUDIT-r4.md` (ACCEPT). "Audit F-n" is its §3.1, "§3.2"
  its single-source table, "K-n" its §8.
- Owner records, read through the GitHub API on 2026-11-14: #914 comments 6877871344 (ledger
  conditions), 6877908458 (QCD group), 6878200172 (scientific emphasis), 6878781541 (guidance on the
  audit and this proposal), 6879158095 (r5 accepted) and 6879221928 (guidance on the research
  ranking); #1169 comments 6877981234 and 6878199016 (S-J and EXACT).
- **The open Issues.** All 90 open Issues were listed through the API, and their titles and labels read.
  The planning-status blocks, and the comments cited, were read for these: #866, #868, #872, #873, #914,
  #944, #970, #996, #1007, #1008, #1015, #1028, #1029, #1049, #1055, #1058, #1060, #1062, #1063, #1074
  (closed), #1142, #1143, #1155, #1169, #1190, #1211, #1234, #1238, #1244, #1245 and #1255. Their bodies
  and comments were searched for the manuscript lines of every MC item and for the keywords "Koide",
  "Condition 2", "PMNS", "flavour", "observer-level map", "local-lift" and "random permutation".
- The frozen QB5(a) preregistration, `G3-QB5A-PREREG-r4.md` at `8dd0de90` on #1275, read through the
  GitHub API for its outcome classes only (RO-2).
- `AGENTS.md` at `main` `dfeec843`, §A.45 (lines 1209 onward), §A.25 (line 317 onward), §A.14
  (line 553).
- Manuscript lines were read at `main` `dfeec843`, the ledger's base (`LEDGER-r5.md` header,
  "Base"). Book-to-FULL mirror lines were located by exact line match against
  `book/The-Incompleteness-of-Observation-FULL.md`.

**The governing owner guidance, quoted.**
- #914 comment 6878781541 (`amaybaum`, 2026-11-14T14:26:48Z): "The subsequent queue proposal should
  distinguish manuscript corrections, missing ledger coverage, and scientific research
  obligations—they require different work and authorization." and "The audit does not yet justify
  promoting QCD or another downstream branch ahead of the shared foundational gaps."
- #914 comment 6878200172 (`amaybaum`, 2026-11-14T13:47:10Z): "Emphasis is not execution order.
  Prioritizing sector justification must not make it a new prerequisite for already authorized Bell,
  gravity or mechanism work." It "sets no execution order and changes no Issue's prerequisites,
  readiness or authorization", and queue changes "are then a separate decision".
- #914 comment 6879221928 (`amaybaum`, 2026-11-14T14:55:05Z), quoted verbatim:

  > The queue proposal's three-part structure is appropriate. For its research ranking, require each
  > proposed move to state:
  >
  > - which mandatory obligation it advances;
  > - its prerequisites, readiness and existing authorization;
  > - the concrete next unit and why it outranks alternatives.
  >
  > Sector justification, exactness and compatibility are the recommended emphasis—not a predetermined
  > ranking or new prerequisite for other work. Let the reviewed evidence justify the actual order.
  >
  > No manuscript wording, tier or queue change follows from preparing these drafts.

**How r3 is organized.**
- **Part A** groups every proposed change under the Issue it belongs to.
- **Parts 1–3** keep the detail of r2: the paired passages of each correction, the coverage gaps, and
  the research moves with their ranking. Each item's Issue is given in Part A.
- **Kinds of work.** The three kinds stay distinguishable in every Issue group, through a "Kind" column:
  - **MC**, a manuscript correction;
  - **LC**, missing ledger coverage;
  - **RO**, a research obligation;
  - **PC**, a planning change (a proposed change to a planning-status block, or the assignment of an
    item to an Issue).
- **Order.** The order of Issue groups in Part A is not a ranking. The only ranking is that of the
  research moves (Part 3), and it has no default order between RO-1 and RO-2.

***

## Part A. Changes grouped by Issue

### A.0 What an Issue assignment does and does not do

- **What it is.** An assignment names the accountable home of an item (§A.45 rule 6, line 1263). It is
  a planning act. It establishes nothing, authorizes nothing and changes no scientific status (§A.45
  rules 1–2).
- **What it needs.** Adding an item to an existing Issue widens that Issue's recorded scope. That needs
  an owner decision: the maintenance clause of §A.45 rule 3 allows entries to record "an existing owner
  decision or a sourced fact", and such updates "may not resolve an undecided question, widen an
  authorization or change scientific status". Every assignment below is therefore a **(proposal)**.
- **What each row gives.**
  - its kind;
  - its ledger row or finding;
  - what the item is;
  - the authorization it would need before work starts. Starting work needs, as recorded for that work,
    readiness, an owner authorization, a designated writer and no conflicting writer (§A.45 rule 3).
- **What each Issue's header gives.** The Issue's recorded tier, readiness and authorization, as read at
  source.

### A.1 Where the manuscript corrections go (proposal)

**Option A, proposed.** Each correction goes to a specific existing Issue where one already covers that
manuscript area:
- #1058 (Higgs);
- #1142 (GR §7.2 corollary and running vacuum);
- #1190 (Chapter 18);
- #1234 (linearity and the Bell branch);
- #1238 (claims scope and Main-independence);
- #1244 (A/4 and GR §8.5 conditions);
- #1029 (cross-references);
- #1015 (finiteness wording).

All the others become rows of one table in the planning block of **#1028**, "Correction planning:
scientific overclaims and status corrections (from the 2026-11-01 disposition)".

Why #1028:
- **Its scope is this kind of work.** It "holds the scientific and status corrections" of a corpus
  audit (#1028 body).
- **Its working rules are the ones these corrections need** (#1028 body, "Working rules"):
  - "Minimum necessary change: each edit corrects one evidenced defect and its necessary consequences";
  - "Propagate corpus-wide (§A.25, §A.14) … rebuild the affected `.tex`/`.pdf` with `build.sh`";
  - "Correct in place (§A.27, §A.30)";
  - "Each edit is independently reviewed at its exact head before it lands".
- **Its authorization model matches.** Its block reads "not authorized (units authorized one by one are
  recorded on the Issue)", which is what each correction unit needs.
- **It already takes reassigned items by owner decision.** For example, #1028 comment 6658037322 records
  the reassignment of four items to it.
- **It already carries one candidate.** #1028 comment 6628572816 lists `book/ch19-open-problems.md`:20,
  the "Problems resolved" heading, among its cosmological-constant sites. That is D1.
- **No site conflict was found.** #1028 names the sites it edits alone ("Complexity:206, Substratum:56,
  Explainer:930 and Main:744"; "Main:720 belongs to #1015"). No MC item here touches them.

Its recorded planning (#1028 body): Tier "Supporting (provisional)"; Prerequisites "per item";
Readiness "ready"; Authorization "not authorized (units authorized one by one are recorded on the
Issue)".

**Caveat.** #1028's body ties it to "the 2026-11-01 disposition". Adding the ledger's corrections widens
that scope, which is an owner decision.

**Option B.** One new Issue, carrying the same correction units as rows of one table in its planning
block (§A.45 rule 4). It applies if the owner prefers #1028 to stay bound to its disposition. The
specific-home assignments would be the same under either option.

**Not proposed as homes, and why:**
- **#1255.** Its grouped drafts G-A to G-E cover its own thirteen findings (#1255 body).
- **#944.** It is a read-only audit whose "Corrections the audit identifies go to the owner as separate
  proposals" (#944 body).
- **#970.** It is a research backlog to be worked "after the source corrections are made accurate"
  (#970 body).

### A.2 Issues carrying research obligations and ledger coverage

**#914, "OI ↔ QM equivalence: proof gate (dependency index; carries #885)".**
- *Recorded planning.* Labels `tier: high`, `readiness: partly ready`.
- *Ledger authorization.* The ledger is "the bounded paper-only ledger under #914" (#914 comment
  6877420015, item 2), authorized for "reading, analysis, writing and independent review only"; r5 is
  accepted (#914 comment 6879158095).

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| LC-1 | LC | F-1, U-1 (T-6) | Rows for Structure's level hierarchy, placements and Born test | Owner decision whether a revision of the accepted r5 falls within the ledger authorization |
| LC-7 | LC | D8 | Correct D8's FULL mirror cell (:2894 and :2896) | As LC-1 |
| LC-2 | LC | U-1 | Focused re-audit of Structure coverage | Owner decision whether a second audit pass is covered |
| LC-3 | LC | U-10 | Main-independence trace of Main:20, :76, :660–674, :704. It reconciles with #1238's completed trace T2, which classified "37 items" of Main's downstream references, "6 are dependences" (#1238 comment 6800989329; "session files, not on `main`") | As LC-2 |
| LC-4 | LC | U-9 (K-9) | Search for the record of the R ≈ ε computation (ch19:244). Related: #1029 carries rotational-protection items X8 and X9 (#1029 comment 6590353594) | As LC-2 |
| LC-5 | LC | audit §10 | Reduced-depth reads (ch13 §13.6 first) | As LC-2 |
| LC-6 | LC | audit §10 | Read-only census lookup of the kernel identifiers | As LC-2 |
| LC-8 | LC | J-1, J-2; §10 M1–M9 | Record in the ledger the accountable Issues the owner assigns below | As LC-1 |
| RO-6 | RO | §10 M1; A-QM, A-GR, A-REAL | Observer-interface lift. **(proposal)** Track it under #914's O-IF-SELECT row. That row reads: Tier "High (provisional; existing O-PHASE tier)"; Readiness "blocked: no qualifying candidate in the bounded checked record …"; Authorization "paper-only bounded source assessment completed …; construction remains at selection gate" (#914 body) | No next unit; a qualifying candidate first |
| Q2, Q5, Q6, Q14 | owner questions | `LEDGER-r5.md` §12 | Q2 is also #1234 item 6. Q5 bears on #1055 and EXACT. Q6 decides D6 and D11. Q14 bears on #1063 | Owner answers |

**#1169, "OI-QM-EXT-1".**
- *Recorded planning.* Labels `tier: foundational`, `readiness: partly ready`.
- *S-J and EXACT* (#1169 comment 6878199016): Tier Foundational; Prerequisites and Readiness
  "undetermined pending owner decision"; Authorization "not authorized".

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-1 | RO | A-QM, A-BELL, A-REAL; Q7 | Paper-only specification of C: confinement (S-J) with closure within C (S-A) | Readiness, authorization and writer for S-J |
| PC-1 | PC | — | **(proposal)** A planning row for S-A (none was found in #1169 or #914) | Owner decision |
| PC-2 | PC | — | **(proposal)** S-J readiness → `ready`, for the RO-1 paper-only specification only | Owner decision |
| PC-3 | PC | J-3, J-4, M5 | **(proposal)** EXACT prerequisites → "the #1055 inventory (RO-3); owner answer to Q5" | Owner decision |

*Already authorized and not gated:* MECH-1 (#1169 body table).

**#873, "Mannheim gravity comparison and the OI G3 coupling gap".**
- *Recorded planning* (body, for the Issue as a whole): Tier "High (provisional)"; Readiness "ready";
  Authorization "not authorized".

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-2 | RO | B-CC-2; §9 QM–CC, GR–CC; M6; A-GR, A-REAL in part | Execute the frozen QB5(a) preregistration (F `8dd0de90`; "execution is not authorized", #873 comment 6875553420) | A recorded execution authorization on #873; a designated writer (none recorded for execution); a conflicting-writer check |

**#1055, "A1-NECESSITY: can OI's results that use total finiteness be recovered without the posit A1?"**
- *Recorded planning* (body): Tier "High"; Prerequisites "none recorded"; Readiness "ready";
  Authorization "not authorized".
- *Parent and owner direction.* Its parent is #914. The owner's direction there (#1055 comment
  6594944363): "Investigate eliminating A1 under the hard-to-vary procedure", with "The preserved results
  listed above … fixed in advance as controls".

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-3 | RO | J-3, J-4, M5, B-QM-8, B-QM-21, B-QM-28, B-BH-3, B-BH-4, C-PRED-8; A-QM, A-REAL | **(proposal)** The exactness inventory, carried here as #1055's next unit and linked to EXACT on #1169 | Owner authorization on #1055 and a designated writer; coordination with `writer-1007` (#1007) and #1015 |

**#1234, "Main/SM: linearity (vii) vs the … Bell branch — follow-ups from PR #1233", with #1049, "Linear vs
affine microscopic dynamics: what selects A5?".**
- *#1234's recorded planning* (body): Tier "Supporting (provisional)"; Readiness "blocked: owner
  questions"; Authorization "not authorized".
- *#1049's recorded planning* (body): Tier "Foundational"; Readiness "ready"; Authorization
  "paper-only (owner, chat 2026-11-04; #1049 c.6622105211)"; Designated writer "the coordinating
  session". Its r5 assessment was accepted at a bounded checkpoint, and "A5 is still a posit" (#1049
  comment 6768089770).

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-4 | RO | J-1, J-2; B-BELL-4, B-BELL-5; Q2; A-BELL, A-REAL | **(proposal)** Record J-1 and J-2 as #1234's open item 6 (its premise question (a)/(b)/(c), which is Q2). The research question of what selects A5 stays with #1049, which is already authorized | Owner answer to item 6. Then, for a controls list, authorization and a writer |
| D4 | MC | D4 | Carry the (vii) condition where the preparation-indexed route is stated in the book and the companions. This is #1234 item 2 ("The book has not been swept for this") | Owner decision on item 2; then a correction unit |

**#1211, "OI-SM-QM-BRIDGE".**
- *Recorded planning* (body): Tier "Foundational"; Readiness "ready"; Authorization "**unit 1 only**".

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-5 | RO | §9 QM–SM; Q9; A-REAL | Unit 2, not yet scoped | A scope, an owner authorization and a writer |

**#1245, "H-BD: origin and derivation of the deep-to-boundary influence bound".**
- *Recorded planning* (body block): Tier "High (provisional)"; Readiness "ready"; Authorization
  "paper-only".
- *Current status note.* The body's current note says: "No new investigation of the physical source of
  the entropy-slope equality is authorized yet."
- *W1 is already tracked here.* #1244's status note says "H-BD and the W1 thermodynamic-slope gap are
  tracked in #1245".

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-8 | RO | §10 M9; B-GR-7 | **(proposal)** Track M9, the energy shell and W1, here | A new owner authorization for a physical-source investigation |

**#1062, "OBS-EMERGE: a physical embedded observer from the native dynamics".**
- *Recorded planning* (body): Tier "High (provisional)"; Readiness "bare formation: ready; recording:
  blocked: O-REC"; Authorization "not authorized".

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-9 | RO | U-2 (F-2, C2–C4 clauses) | **(proposal)** Whether typical bijections admit a C1–C4 observer, recorded here as a genericity form of #1062's question ("Can OI's native rule produce a persistent embedded observer"). No Issue with exactly this scope was found | Owner decision; authorization and a writer |

**#1063, "LR-YM: gauge/QFT extension, Yang–Mills and the Barandes–Yang–Mills connection".**
- *Recorded planning* (body): Tier "Exploratory"; Readiness: the paper-only Yang–Mills source review is
  "ready", and integration is "blocked: #872"; Authorization "paper-only (PO-1102, workstream E …)".

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-10 | RO | U-3; B-QCD-5, B-QCD-6, B-QCD-8; Q14 | The nonperturbative phase and the coupling predictions; QCD obligations. No tier or readiness change is proposed | Under #1063's existing scope |

**New Issue, SM flavour derivation obligations (proposal).**

| ID | Kind | Ledger row / finding | Item | Authorization needed |
|---|---|---|---|---|
| RO-7 | RO | U-4 to U-8: B-SM-FLAV-3, B-SM-FLAV-6, B-SM-FLAV-9, B-SM-FLAV-10 | The 1/d amplitude, $b_{23} = 1$, the analytical K, and the $O(\lambda^3)$ route or exact diagonalization for Cond 2 | Owner decision to open it, then per-unit authorization |

Why a new Issue: no open Issue covers flavour derivations.
- **What the search found.** The keyword search found "Koide", "PMNS" and "Wolfenstein" only in
  correction contexts:
  - #1190: section pointers and wording;
  - #1255: JUNO corrections, group G-D;
  - #1028: the σ value of Wolfenstein A.
- **The alternative.** Rows in #970, whose purpose is to "Advance the scientific claims exposed as
  unproved, overbroad, conditional, or downgraded". Its sources are a different audit (#942), so this
  draft does not propose it.
- **Tier.** Whatever tier the owner sets, RO-7 stays below the shared gaps (#914 comment 6878781541).

### A.3 Issues carrying manuscript corrections

**#1028, scientific overclaims and status corrections (Option A).**
- *Recorded planning:* as quoted in A.1.
- **(proposal)** One table of the following rows, each a correction unit authorized one by one. Details
  of each item are in Part 1.

| Unit | Kind | Items (Part 1 IDs) | Authorization needed |
|---|---|---|---|
| MC-1 | MC | D8, F-31, F-33, D1 (already listed in #1028 comment 6628572816), F-34, F-36 | Per unit, on #1028 |
| MC-2 | MC | F-3 (chirality and generations; the Higgs clauses go to #1058), F-21, F-24, F-18, F-17 (:703 only; :179 goes to #1244), F-2 (coupling clause, with ch03:26 and FULL:891) | Per unit |
| MC-3 Substratum | MC | F-4, F-5, F-16, S-3, S-10, S-19 | Per unit |
| MC-3 GR | MC | F-11, F-12, F-13 (with ch19:46 and FULL:5193), F-15 | Per unit |
| MC-3 SM and appendix-a | MC | F-6, F-25, F-35, F-8, F-23, F-38, SM-36, the appendix-a F12 row | Per unit |
| MC-3 Structure | MC | F-19, F-20, T-9, T-12 | Per unit |
| MC-3 book | MC | D9, D10 | Per unit |
| MC-4 | MC | F-9, F-29 | Per unit |
| MC-5 | MC (contingent) | F-2 (C2–C4 clauses; waits for RO-9 on #1062); F-22 (waits for RO-10 on #1063); F-27, F-28, F-30 (each wait for a recovery note or RO-7); D6, D11 (wait for Q6 on #914) | After the item each waits for |

*Overlaps with #1190, to be settled by the owner before a unit touches the same line:*
- **F-35 and row 1 of appendix-a.** Row 1 (appendix-a:70) is also #1190's WP3-34/WP8-10, a different
  defect on the same row (#1190 body).
- **F-9 and SM:1118.** SM:1118 was reworded under #1190's WP3-33 (#1190 comment 6713826444). At
  `dfeec843` it reads "consistent with the extrapolated value at $0.6\sigma$". F-9's difference between
  three statements remains.
- **F-25 and SM:1279.** SM:1279 also appears in #1028's own "Decision 12 proposal (not applied)", on the
  σ value of Wolfenstein A (#1028 body).

**#1058, "HIGGS-INPUT: book states the composite Higgs doublet as derived …".**
- *Recorded planning* (body): Tier "Supporting (provisional)"; Readiness "ready"; Authorization "not
  authorized".

| ID | Kind | Item | Authorization needed |
|---|---|---|---|
| F-32 | MC | `book/ch19-open-problems.md`:196, "The framework derives exactly one scalar doublet" (FULL:5343) | **(proposal)** Add to #1058's site list. Its anchor is SM:468, the same as #1058's. Then a correction unit |
| F-3 (Higgs clauses) | MC | `papers/Substratum.md`:152 and :201, which return "one Higgs doublet" | As F-32 |

#1058's own rule applies: "Theorem recovery before concession … Record the search either way".

**#1142, "GR-C4-RELAX: GR §7.2 corollary 'under (C1)–(C4)' vs undischarged C4 at the horizon; running-vacuum
'relax' claim …".**
- *Recorded planning* (body): Readiness "independent review: `ready`. Any correction: `blocked:
  independent review`"; Authorization "`not authorized`".

| ID | Kind | Item | Authorization needed |
|---|---|---|---|
| D5 | MC | GR:418, the corollary "under Lemmas 1–3 and conditions (C1)–(C4)", whose proof also uses the geometry-first ordering, Jacobson's relation and H-count. It is the same corollary as #1142's item 1 | **(proposal)** Add to #1142's review; then a correction unit |
| F-7 | MC | GR:410, Σm_ν called an "OI prediction" and coupled to the running vacuum. It sits next to #1142's item 2 (the running-vacuum "relax" claim near GR:414) | As D5 |

**#1190, "SHOULD-FIX-RT: Chapter 18 corrections and parked release-3.2 owner questions".**
- *Recorded planning* (body): Tier "supporting (provisional)"; coordination owner Codex, for "Minimum
  Chapter 18 wording corrections". No authorization covers a new item.

| ID | Kind | Item | Authorization needed |
|---|---|---|---|
| D7 | MC | `book/ch18-beyond.md`:256, chirality "derived from the staggered trace-out" (FULL:5062) | **(proposal)** Add to #1190's Chapter 18 scope; then a correction unit |

**#1238, "CLAIMS-SCOPE-1: narrow the 'QM is / is derived from embedded observation' wording to the
proved scope".**
- *Recorded planning* (body): Tier "Supporting (provisional)"; Readiness "ready".
- *What it authorized.* Its authorization covered a listed set of edits, since merged as #1239 and
  #1241 (#1238 comments 6800989329 and 6804055462). The remaining sites "need an owner decision" (#1238
  comment 6804055462).

| ID | Kind | Item | Authorization needed |
|---|---|---|---|
| S-1, S-2, S-17 | MC | `papers/Substratum.md`:389 ("Both are derived rather than fundamental"), :421, :459 | **(proposal)** Add to #1238's remaining sites; then owner authorization |
| K-5 | MC | `book/ch19-open-problems.md`:356, "The framework derives the fundamental laws" (FULL:5503) | As S-1 |
| M-33 / U-10 | MC (contingent) | Main:704 and the other U-10 passages. They wait for LC-3 (on #914), which reconciles with #1238's trace T2 | After LC-3 |

**#1244, "Audit: three candidate proof/scope gaps in GR §3.2, GR §8.5 and Main §1.4".**
- *Recorded planning* (body table): Supporting (provisional), ready and not authorized for its items.
- *Authorized work on these lines.* It holds the authorized paper-only Structure:179 correction draft:
  "Structure:179: draft fix", with "No merge is authorized without approval" (#1244 comment 6828105179).
- *An authorized sweep.* It also holds an authorized sweep of older A/4 sites. In that sweep, "no
  conditions are added to unconditional mode-count or geometry statements" (#1244 comment 6824919310).

| ID | Kind | Item | Authorization needed |
|---|---|---|---|
| F-17 (:179) | MC | Structure:179 against :191–192, a level-placement contradiction. The authorized :179 draft addresses a different defect on the same line (A/4 as distinguishing OI) | **(proposal)** Owner decision whether the :179 draft also takes this defect, or a separate unit follows it |
| G-2 | MC | GR:12, "the counting $S = \sigma A/\epsilon^2$ itself unconditional", against GR:40 (the partition presupposes GR causal structure) | **(proposal)** Add to the sweep's dependency classification. This bears directly on the owner's rule for "unconditional mode-count" statements, so it is an owner question (below) |
| G-30 | MC | GR:615, "(a) *Unconditional.*", in GR §8.5, the section of #1244's item 1 | **(proposal)** Add to item 1; then a correction unit |
| T-4 | MC | Structure:453, an A/4 bound on "any horizon entropy … under the conditions of the horizon calibration" | **(proposal)** Add to the A/4 sweep |

**#1029, "Correction planning: cross-references, labels, ledger/census and evidence records".**
- *Recorded planning* (body): Tier "Supporting (provisional)"; Readiness "ready"; Authorization "not
  authorized (units authorized one by one are recorded on the Issue)".

| ID | Kind | Item | Authorization needed |
|---|---|---|---|
| D2 | MC | The H-Bell section citation: Main:20, SM:14, :60 cite §3.3; Introduction:145 and :179 cite §3.2. #1029 comment 6581824083 already flags stale H-Bell pointers (Explainer:58, :709; Substratum:467) for "a separate approved referencing unit" | **(proposal)** Add to that referencing unit |

**#1015, "SUBSTATE-1: minimal manuscript scope and finite-S dependency audit".**
- *Recorded planning* (body): Tier "Supporting (provisional)"; Readiness "ready"; Authorization
  "paper-only (PO-1102, workstream F)".
- *Its scope.* "Finiteness wording is tracked separately in #1015" (#1238 comment 6804055462).

| ID | Kind | Item | Authorization needed |
|---|---|---|---|
| F-10 (optional) | MC | GR:90, "Lemma 1 is a consequence of partition geometry", looser than GR:585 | **(proposal)** Note as an optional site; a correction unit only if the owner wants one |

### A.4 New Issues proposed

Only the SM-flavour Issue (A.2), and the MC Issue only under Option B (A.1). The candidates the
coordinator named were checked:
- J-1 and J-2 fit #1234;
- M1 fits #914's O-IF-SELECT row;
- M9 fits #1245;
- U-2 fits #1062 most closely;
- S-A fits #1169.

***

## Part 1. Manuscript corrections (MC)

### 1.0 What any MC unit needs

Each item's accountable Issue is given in Part A §A.3.

No MC item below is authorized. Each would need, separately:
1. a recorded owner authorization for that correction unit (§A.45 rule 3; §A.43);
2. an accountable Issue (§A.45 rule 6, line 1263: "A pull request is never an accountable home"). The
   ledger asks the owner whether any should be scheduled (`LEDGER-r5.md` §12, Q11). **(proposal)** No
   Issue per correction: Part A §A.3 assigns each item to a specific existing Issue where one covers it,
   and the rest to #1028 (Option A) or to one new Issue (Option B);
3. a manuscript PR limited to the minimum necessary change (`AGENTS.md`:317–330);
4. §A.25 propagation: a corpus-wide grep for the phrase and its paraphrases, every chapter edit
   mirrored into FULL and the reverse (§A.14), and regeneration of the affected `.tex`/`.pdf` with
   `sh ./build.sh` (papers: `papers/<NAME>.tex`, `.pdf`; book:
   `book/The-Incompleteness-of-Observation-FULL.tex`, `.pdf`, all present on `main`);
5. for paper edits, the §A.32/§A.33 added-lines battery;
6. independent review, and a separate owner decision to integrate (§A.45 rule 7, line 1278).

This proposal drafts no manuscript text. "Minimal correction" below names the defect the correction
would remove, not its wording.

**Mirrors.** "Mirrors" lists the mirrors the ledger or audit recorded and those this pass located by
exact line match. A §A.25 grep at correction time may find more. Where a phrase grep of
`papers/*.md` and `book/*.md` found hits whose context was not read, they are listed as "to check".

**Recovery before concession.** Where the finding is unresolved (U-n), the Code Review Rules require a
documented, proportionate recovery attempt before a substantive narrowing of an unrefuted
mathematical claim "solely because its proof is missing" (`AGENTS.md`, Code Review Rules,
"Theorem recovery before concession"). Those items are placed in MC-5 for that reason.

### 1.1 MC-1. Book passages that contradict a paper anchor already in the corpus

Direct contradictions in the book whose authoritative anchor (§A.25 step 2) is already a careful paper
statement. No new science is needed.

| ID | Passage A (book) | Passage B (anchor) | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| D7 | `book/ch18-beyond.md`:256: "$\mathrm{SU}(2)$ as chiral and $\mathrm{SU}(3)$ as vector-like, derived from the staggered trace-out" | `papers/SM.md`:543: "Theorem 13 (Chirality — conditional identification; minimal embedding certified vector-like; H-χ' sharpened, open)"; `book/ch19-open-problems.md`:328: "Open — named hypothesis H-χ'" | DC (`LEDGER-r5.md` §F.1) | Remove "derived"; state chirality at its source status (conditional, H-χ′ open) | FULL:5062; FULL `.tex`/`.pdf`; grep ch05 (the sentence cites "Chapter 5") |
| D8 | `book/ch10-chemistry.md`:86: "SU(3) color confinement (Chapter 5 §5.4) produces bound hadrons"; :88: "The mechanism is derived from the gauge structure of SU(3)" | `papers/SM.md`:801: whether the induced theory "is in the deconfined phase required for the perturbative matching to be valid", the Haar-measure theory confining (:801–811); `book/ch05-gauge-structure.md` §5.4 (from :81) carries no confinement statement (ledger §11 D8) | DC | Remove the derivation claim and the citation to a section that does not carry it; state confinement as open for the framework's measure | FULL:2894 and FULL:2896 (the ledger lists only :2894; :88 mirrors at :2896, located by this pass) |
| F-31 (K-1) | `book/ch19-open-problems.md`:106: "anomaly cancellation forces exactly three candidate matter sectors" | `papers/SM.md`:458: "anomaly cancellation fixes charges given the sector pattern; the selection of the observed family pattern … is not supplied by either" | DC (audit F-31) | Restate at SM's scope | FULL:5253 |
| F-32 (K-2) | ch19:196: "The framework derives exactly one scalar doublet" | `papers/SM.md`:468: "This theorem does **not** derive the existence of a Higgs doublet" | DC (audit F-32) | Remove the derivation claim | FULL:5343 |
| F-33 (K-4) | ch19:118: "The framework derives the total budget" | ch19:116: "the total fraction is partly definitional, equal to $1-\Omega_B$ by construction"; `papers/GR.md`:541: "partly definitional" | DC within the chapter (audit F-33) | Align :118 with :116 | FULL:5265 (and :5263 for :116) |
| D1 | ch19:20, the §19.2 heading "Problems resolved" | ch19:72: "the paradox is not resolved"; ch19:80: "Not resolved." | DC within the chapter (ledger §F.1) | Bring the heading into line with its entries | FULL:5167 |
| F-34 | `book/appendix-a-prediction-status.md`:145–158: eleven biology rows (B1, B2, B6–B14) labelled S; :28 defines S as "no fitted input and no open link specific to the entry" | `book/ch16-medicine.md`:6 and `book/ch17-bioinformatics.md`:6: "**Status — conjectural extension.** … offered as a *conjecture*, not an established result" | DC (audit F-34) | Relabel the eleven rows to the chapters' conjectural status; B3 unchecked (audit §10) | FULL:5669–5682; to check: `papers/Medicine.md`, `papers/Bioinformatics.md` (companion papers present on `main`; not read) |
| F-36 | appendix-a:131: "Normal mass ordering \| structural … \| C" | appendix-a:135: "the ordering a heuristic consequence of taste-breaking rather than a theorem"; `papers/SM.md`:1460 | DC between label and note (audit F-36) | Relabel N5 to its note's status | FULL:5655, :5659 |

### 1.2 MC-2. Paper passages that contradict an anchor in the corpus

| ID | Passage A | Passage B | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| F-3 | `papers/Substratum.md`:165: "Partition-spinor identification (Theorem 12) and trace-out (Theorem 13) give chirality."; also :151–152, :169, :173, :201, :203 | `papers/SM.md`:543 (Theorem 13 conditional; H-χ′ open); :468 (Higgs doublet not derived); :448 ("free-kernel identification refuted; H-spin' open"); Substratum:161, :193, :199 carry the conditions | DC on chirality; DA on generations and the Higgs (audit F-3) | Carry Theorem 23's own conditions (:193) into the Stage 2 text and the :201, :203 remarks | Substratum `.tex`/`.pdf`; grep `book/ch02-substratum.md` and FULL for the Stage 2 restatement |
| F-21 | `papers/SM.md`:567: "the 'wrong-chirality' doublers … become, in OI, the physical generations (Theorem 9)" | `papers/SM.md`:448: Theorem 9, "free-kernel identification refuted; H-spin' open" | DC (audit F-21) | State the generation identification as conditional on H-spin′ | SM `.tex`/`.pdf`; grep book ch05 |
| F-24 | `papers/SM.md`:863: "the GST relation [21] follows as a corollary" | `papers/SM.md`:887: "The GST relation [21] is an external empirical relation … inherits GST's empirical status" | DC within one section (audit F-24) | Make :863 agree with :887 (scope: :863 gives a scaling argument, audit F-24) | SM `.tex`/`.pdf` |
| F-18 | `papers/Structure.md`:417: "the emergent QFT's parameters are derived from the cubic-lattice structure rather than being moduli to be selected" | `papers/SM.md`:1396 (couplings at $M_Z$ "set by the threshold $\delta_0$ and the resummation parameters $A, B$, matched"); :1440 (Layer 3 mass scales, CP) | DC (audit F-18) | Restrict "derived" to the structural content SM derives | Structure `.tex`/`.pdf` |
| F-17 | `papers/Structure.md`:179: dark-sector phenomenology at Level G3 × D; :703: "OI's substratum produces $SU(3) \times SU(2) \times U(1)$ uniquely" | Structure:191 ("*[SM]:* Level D × Levels G1–G2"), :192 ("*[GR]:* Level D × Levels G1–G2"); `papers/SM.md`:14, :1424 (lattice selected by the observed group) | DC within Structure (:179 against :191–192); DA (:703) (audit F-17) | Reconcile the placements; carry H-link, H-cust and the selection at :703 | Structure `.tex`/`.pdf`; interacts with LC-1 (T-6) |
| F-2 (coupling clause only) | `papers/Structure.md`:733: "random permutations on finite sets typically lack the coupled-dynamics … features required for C1–C4" | `papers/Main.md`:147–151: "the fraction of bijections failing C1 at the $T$-level decays exponentially in the hidden-sector capacity $n_H$" (exact counting over all bijections for a fixed product partition, audit F-2) | DC for the coupling clause; the C2–C4 clauses unresolved (U-2) | Remove the coupling clause; leave the C2–C4 clauses to MC-5 (the corpus proves neither direction, audit F-2) | `book/ch03-structural-realism.md`:26 and FULL:891 (audit K-11); Structure `.tex`/`.pdf` |

### 1.3 MC-3. Differences in assumptions or scope, and single-source overstatements, with a settled anchor

Each item has a settled anchor and needs no new result.

**Substratum** (`papers/Substratum.md`; artifacts `Substratum.tex`/`.pdf`):

| ID | Passage A | Passage B / support | Class | Minimal correction |
|---|---|---|---|---|
| F-4 | :199: "no fitted parameters, no model-building choices, no landscape of alternatives at the level of the gauge sector" | `papers/SM.md`:1424: Theorem 7b selects the lattice "*because* $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ is observed" | DS (audit F-4) | State that the lattice input is selected by the structure counted as evidence |
| F-5 | :525: "**1 is structural with no open link of its own** (B-S), **2 are conditional structural** (B-C) …" | `papers/SM.md`:1269–1316: 2 S and 5 C among 22 | DS with unexplained residue (audit F-5) | State the mapping between the two counts |
| F-16 | :231–233: "a bidirectional correspondence for the **local reconstructed residue**", displayed with ⟷ | Theorem 23 (:193) witnesses data → class only; no witness for class → data (audit F-16; §A.34) | SO of directionality | Display the proved direction only (§A.34) |
| S-1 | :389: "Both are derived rather than fundamental" | `papers/GR.md`:162 (Einstein equations imported); Substratum:423 (conditional on G3) | SO (audit §3.2) | Carry the G3 condition |
| S-2 | :421: "does establish … derived from the same object by the same procedure under the same conditions" | ledger §9 GR–SM undetermined; Q4 | SO | Narrow to what is established |
| S-3 | :46: "The dark sector is the gravitational effect of the unreadable storage" | `papers/GR.md`:452, :540 (conditional, partly definitional) | SO | Carry the conditions |
| S-10 | :239: weak ER=EPR "as a structural consequence of the framework's holographic architecture" | `papers/Structure.md`:463 (OI "does not naturally produce full AdS/CFT-style correspondence") | SO | State it as proposed (ledger C-ERP, PE) |
| S-17 | :459: "generates every concept in fundamental physics" | G3 open | SO | Narrow |
| S-19 | :475–479: Class A "structural theorems" | generations on H-spin′; gauge reading on H-link, H-cust | SO | Carry the named hypotheses |

To check for mirrors: `book/ch02-substratum.md`:198 and FULL:832 contain "derived rather than
fundamental" (phrase grep; context not read).

**GR** (`papers/GR.md`; artifacts `GR.tex`/`.pdf`):

| ID | Passage A | Passage B / support | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| F-7 | :410: "all three results match the OI predictions of normal ordering with $\Sigma m_\nu$ near the oscillation minimum"; "both follow from the same lattice structure" | `papers/SM.md`:1464 (genericity heuristic, :1456); :1460 ("generically"); appendix-a:87, :130 (L, "oscillation inputs") | DA; SO in the coupling sentence (audit F-7) | State the neutrino items as heuristics; remove the unsupported coupling to the running vacuum | — |
| F-11 | :48: "$\tau_B \gtrsim 1/H$ … **Satisfied.**" | :456: "which is not derived from the substratum dynamics" | DS (audit F-11) | Align :48 with :456 | — |
| F-12 | :536: "no predictions are fit to the quantities they predict" | :539–545: "factor imported", "partly definitional", two "in tension" | DS (audit F-12) | Carry the table's own qualifications into the preamble | — |
| F-13 (K-3) | :454: "no particle dark matter exists"; `book/ch19-open-problems.md`:46: "Dark matter is not a particle" | GR:458: "a consistency check for the total dark sector budget, not a derivation of its internal structure"; GR:530: "$\rho_E \approx \Omega_{\text{CDM}}\,\rho_{\text{crit}}$ — an input" | DS (audit F-13) | Narrow to the corollary's scope | FULL:5193; to check: `book/ch00-introduction.md`:83 / FULL:310 and `book/ch09-universality.md`:254 / FULL:2721 (phrase grep "no particle dark matter"; context not read) |
| F-15 (K-10) | :530(iii): "adiabatic initial conditions set by inflation" | `book/ch19-open-problems.md`:194: "**Framework status.** Not addressed." | DA (audit F-15) | State inflationary initial conditions as an input at :530 | ch19:194 / FULL:5341 is the other passage, not changed |
| D5 | :418: "*Under Lemmas 1–3 and conditions (C1)–(C4)*" | proof uses the geometry-first ordering (:448–450), Jacobson's Clausius relation (:426), $T_{cl}$ resting on H-count (:422, :58); abstract places it at G4, conditional on G3 (:12) | DA (ledger §11 D5) | List the premises the proof uses | — |
| G-2 | :12: "the counting $S = \sigma A/\epsilon^2$ itself unconditional" | :40 (the partition presupposes GR causal structure) | SO (audit §3.2) | Carry the condition | — |
| G-30 | :615: "(a) *Unconditional.*" | (U1) uses Jacobson and H-count; S1 presupposes a horizon (audit §3.2); ledger B-GR-10, CD[S1–S4] | SO | Carry S1–S4 | — |
| F-10 (optional) | :90: "Lemma 1 is a consequence of partition geometry" | :585: "(independent in Part I; consequence of geometry in Part II)" | no conflict (withdrawn); optional (audit F-10) | Optional only | — |

**SM** (`papers/SM.md`; artifacts `SM.tex`/`.pdf`; appendix-a and FULL where noted):

| ID | Passage A | Passage B / support | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| F-6 | :1293 (composite Higgs row, **S**); appendix-a:91 (row 22, S) | :1116 ("The Higgs is the $A_1$ taste — a composite scalar"); :468; appendix-a:28 (S definition) | DA (audit F-6) | Relabel to carry the composite-hosting link | appendix-a:91 / FULL:5615 |
| F-25 | :871: "$A = \sin\theta$"; :1279 class **S** | :881: the identification "is a leading-order statement whose correction is the same open object as the Condition-2 ratio" | DA (audit F-25) | Carry the open identification link in the class | appendix-a row 6 (audit §5) and its FULL line, to check |
| F-35 | appendix-a:70: "S \| 0" | `papers/SM.md`:793: "conditional on single-copy H-link, Theorem 6" | DA (audit F-35) | Relabel row 1 | FULL:5594 |
| F-8 | :1353: "The same construction forces the following"; :1360: "with no free parameter to adjust" | :1290–1291 and footnote ᶠ (L, "given Condition 2"); :1048 ($b_{23} = 1$ a choice) | DA (audit F-8) | Carry Cond 2 and $b_{23} = 1$ | — |
| F-23 | :14: "contain no parameters fit to the predicted quantities"; :847; :14 and :1588: "six fermion masses from a single empirical input"; :989 | :971 ($Q_{\text{down}}$ "as a phenomenological input"); :887 (GST empirical); :1215 (K = 1/2 by "empirical fitting"); table E, R, P rows | SO within SM (audit F-23) | List the further empirical inputs | — |
| F-38 | :1110: "the substrate-level mechanism … is realized in the bijection"; :1100; :1092 | :1108 (mechanisms examined excluded; Cond 2 "a stated condition"); :1349 (values known beforehand) | SO (audit F-38) | Remove the match-to-mechanism inference | — |
| SM-36 | :1339: "strong evidence for the underlying $C_2/d$ identity" | one row "via Cond 2"; :1349 (retrodictions) | SO (audit §3.2) | Narrow | — |
| F-12 row (appendix-a) | appendix-a:190, F12 listed under forward predictions | the same row: "*retrodiction, not a forward bet*"; "does not discriminate" | placement (audit §5) | Move or relabel the row | FULL:5714 |

**Structure** (`papers/Structure.md`; artifacts `Structure.tex`/`.pdf`):

| ID | Passage A | Passage B / support | Class | Minimal correction |
|---|---|---|---|---|
| F-19 | :403: "OI's [SM §8.4] predicts Majorana neutrinos"; :1317: "so $0\nu\beta\beta$ should be observed" | `papers/SM.md`:1452: "On the branch where the singlet taste hosts the Higgs (Theorem 11, taken as input) and no gauge-singlet fermion" | DA (audit F-19) | Carry the branch condition |
| F-20 | :13: "The substratum-level equivalence reading does not hold."; :369 | :351: "in their standard formulation"; :242: "The provisional conclusion is (c)" | DS (audit F-20) | Carry the standard-formulation scope |
| T-4 | :453: "any horizon entropy in OI's framework is bounded by $A/4$ under the conditions of the horizon calibration" | calibration equality only; GSL open (`papers/GR.md`:781) | SO (audit §3.2) | Narrow to the calibration's conditions |
| T-9 | :813: the pair "captures … gauge couplings at $M_Z$, Yukawa structure producing CKM/PMNS" | `papers/SM.md`:1396, :1440 (fitted thresholds; solution-specific Yukawas) | SO | Narrow |
| T-12 | :970: "moderately favors the no-GUT universality class" | `papers/SM.md`:841 (not unique to OI) | SO | Narrow |

**Book, further** (book chapters; FULL mirrors):

| ID | Passage A | Passage B / support | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| D9 | `book/ch19-open-problems.md`:88: the lattice "eliminates the divergence and with it the cutoff sensitivity of $m_H$" (ledger §11 D9) | `papers/SM.md`:1570: "*structurally identified* … the theorem-level derivation is deferred"; :613 ("derivation deferred there") | DS (ledger §F.1) | State the protection as identified, its derivation deferred | FULL:5235 |
| D10 | `book/ch10-chemistry.md`:80: "the necessary ingredients are derived"; "the *possibility* of baryogenesis as a theorem" | `papers/SM.md`:1320 (three physical generations conditional on H-spin′; H-χ′ open); `papers/Substratum.md`:415 and ch19:184 (CP phases solution-specific inputs); `papers/SM.md`:1486–1490 (baryon number conserved at the substratum), :1496–1506 (violation emergent) | DA (ledger §F.1) | Carry the conditions; remove "theorem" | FULL:2886–2888 |
| K-5 | ch19:356: "The framework derives the fundamental laws" | `papers/GR.md`:162 (Einstein equations imported); `papers/SM.md`:14, :1428 ("compression") | SO (audit §8) | Narrow | FULL:5503 |

**Citations and conditions across papers.**

| ID | Passage A | Passage B | Class | Minimal correction | Mirrors |
|---|---|---|---|---|---|
| D2 | `papers/Main.md`:20, `papers/SM.md`:14, :60 cite [Substratum §3.3] for H-Bell; `papers/Introduction.md`:145 and :179 cite [Substratum §3.2] | definition at `papers/Substratum.md`:131–133 (§3.2); Stage-2 use at :171 (§3.3) (ledger §11 D2) | citation | One consistent citation to the definition | Main, SM, Introduction `.tex`/`.pdf` |
| D4 | the book chapters carrying the preparation-indexed Bell route; `papers/Substratum.md`:131–133, :193 | `papers/Main.md`:362, :414 and `papers/SM.md`:104: a coupling graph that varies between state classes needs an update outside (vii)/A5 (ledger §11 D4) | DA | Carry the (vii) condition where the route is stated. The book sites are not located in the ledger ("the book chapters carrying the preparation-indexed route") and must be located first; the wording depends on Q2 (linearity) if A5 is restricted | to be located |

### 1.4 MC-4. Manuscript-revision differences

| ID | Passages | Class | Minimal correction | Mirrors |
|---|---|---|---|---|
| F-9 | `papers/SM.md`:1118 ($m_H \approx 129$–$132$ GeV, "4–7 GeV below", "consistent … within the current $m_t$ uncertainty"); :1126 ("128–132 GeV … to ∼2–3σ (reduced to ≲1σ for the CMS $m_t$)"); :1294 ("$m_t$-consistent") | MR (audit F-9) | One comparison, stated once | SM `.tex`/`.pdf`; appendix-a row 22 if its comparison text differs (to check) |
| F-29 | `papers/SM.md`:981 ("0.474 ± 0.056. Match: 0.05σ"); :1289 ("0.465 ± 0.024 \| 0.27σ"); :1335 ("0.474"); appendix-a:86 ("Within 1σ") | MR (audit F-29) | One data value and comparison | appendix-a:86 / FULL:5610 |

### 1.5 MC-5. Contingent candidates: each waits for an LC trace, an RO outcome, a recovery note or an owner question

| ID | Passage A | Passage B | Class | What it waits for | Mirrors |
|---|---|---|---|---|---|
| F-2 (C2–C4 clauses), U-2 | `papers/Structure.md`:733 (persistence, capacity and readback clauses) | `papers/Main.md`:147–151 (C1 genericity only) | unresolved: "The corpus proves neither that typical bijections fail C2–C4 nor that they satisfy them" (`LEDGER-r5.md` §U, U-2) | recovery note (Code Review Rules) or RO-9 below | ch03:26, FULL:891 |
| F-22, U-3 | `papers/SM.md`:1448: "it does not affect any prediction of the OI framework"; `papers/Substratum.md`:225 | `papers/SM.md`:801: the deconfined phase "required for the perturbative matching to be valid"; :803–811 | DS; whether the nonperturbative phase affects the coupling predictions is open (U-3) | scope narrowing is possible for the structural results; the coupling question waits for RO-10 | SM, Substratum `.tex`/`.pdf` |
| F-27, U-5 | `papers/SM.md`:1036 ($\sin^2\theta_{13}$ coefficient used to determine $A_1$) | :1034 (path sum resting on the open $1/d$ normalization, :944) | DA; which route is load-bearing for "independent of Condition 2" (:1026) is not stated | recovery note, or a statement of the load-bearing route | — |
| F-28, U-6 | `papers/SM.md`:1048: "The natural-normalization choice $b_{23} = 1$"; :1056 | SM footnote ᶠ; appendix-a:96 name only Condition 2 | DA; normalization not derived | listing the choice among the open links needs no new result; a derivation is RO | appendix-a:96 / FULL:5620 |
| F-30, U-7 | `papers/SM.md`:1152: "The matching scale is derived"; :1172 ("a representation-theoretic structural identity") | :1160, :1196, :1215 ("empirical fitting on a moderately-restricted set"), :1219 | DS; analytical K open | recovery note on K | — |
| M-33 / U-10 | `papers/Main.md`:704: "quantitative predictions"; with :76, :20, :660–674 | not yet fixed: the paired passage "is to be fixed by the trace" (`LEDGER-r5.md` §U, U-10) | MC or LC, depending on the trace | LC-3 below (the Main-independence trace) | Main `.tex`/`.pdf` |
| D6 | `book/ch19-open-problems.md`:178: no obligation to derive η_B | Part 4 (#914 comment 6877420015) requires accounting for "other claimed downstream consequences" | scope; planning record against manuscript | owner question Q6 (`LEDGER-r5.md` §12) | FULL:5325 |
| D11 | `papers/SM.md`:1526: the full quantitative prediction "is open work" | `book/ch19-open-problems.md`:184–188: CP phases "solution-specific inputs"; no longer "an unmet derivation obligation" | DA | Q6: which statement is the anchor is undecided (ledger §F.1, MC column "SM:1526 or ch19:184–188") | FULL lines for ch19:184–188, to locate |

### 1.6 Proposed order (proposal)

1. **MC-1** (book direct contradictions). The paper anchors already state the careful form, so each
   correction is narrow and needs no new science. D7, D8 and F-32 assert as derived what SM states is
   not derived (SM:543, :801, :468). The lessons register records that the book has both lagged and
   led the papers (`AGENTS.md`, lessons register, first item).
2. **MC-2** (paper direct contradictions). Same reasoning. F-2's book mirror (ch03:26, FULL:891) moves
   with Structure in this unit, not in MC-1, so that the mirror follows its anchor.
3. **MC-3**, one unit per paper (Substratum, GR, SM, Structure), then the book and citation items. The
   per-paper grouping keeps each PR's propagation to one paper's mirrors and artifacts.
4. **MC-4** (revision differences), which needs only the current values chosen.
5. **MC-5**, each only after the item it waits for.

MC-1 and MC-2 touch disjoint files apart from FULL, so the order between them is a preference, not a
dependency. Nothing in Part 1 depends on Part 3 except MC-5.

**Authorization Part 1 needs.** For each unit: an owner decision assigning it to its Issue (Part A
§A.3), an owner authorization of the correction unit recorded on that Issue, and later a separate
integration decision (§1.0). None exists now for these defects. The one authorized draft on a line
listed here, #1244's Structure:179 draft, addresses a different defect (Part A §A.3).

The order above holds within whichever Issue carries the units. Assigning units to several Issues does
not reorder them.

***

## Part 2. Missing ledger coverage (LC)

Ledger work only: reading, classifying and writing rows, then independent review. No manuscript
change and no research.

| ID | Gap | Source of the gap | Proposed closure |
|---|---|---|---|
| LC-1 | **T-6**: Structure's level hierarchy and placements, and its Born test (`papers/Structure.md`:98–198, 892–954) has no row | `LEDGER-r5.md` §F, "Missing coverage still outstanding"; audit §4.5 T-6 (U, O, T) | Add rows: the hierarchy as a classification scheme (class per source); the placements, cross-referenced to F-17 (the :179 against :191–192 contradiction stays an MC); the Born test with its T flag (audit §4.5 notes "the Born form is in the definition of Q_fb (Main:14)") |
| LC-2 | **U-1**: whether Structure coverage is complete | §U, U-1: "Whether coverage is complete is for a re-audit" | After LC-1, a focused re-audit of Structure only, against T-1 to T-17 |
| LC-3 | **U-10**: Main's independence (Main:76, :20, :660–674, :704) | §U, U-10; audit observation after §4.5 | A read-only trace under the Code Review Rules' Main-independence rule: for each passage, illustration, stated input or dependency; fix the paired companion passage. Its outcome decides whether U-10 is MC (MC-5) or LC |
| LC-4 | **U-9 / K-9**: the "direct computation … R ≈ ε" (`book/ch19-open-problems.md`:244; FULL:5391) has no record cited | §U, U-9; audit §8 K-9 | A read-only search of `verification/` and `papers/` for the computation's record. Found: cite it at its stated scope. Not found: record the absence; the computation itself is RO-10's group |
| LC-5 | Material read at reduced depth: book ch13–17 derivations behind C-BIO (B1–B14, F1–F12); ch13 §13.6 (B3's S label unchecked); SM:960–966; Main §3.4 and GR §3.3 proof bodies; Structure §13.1.1.1 and §14.7–§14.9 | audit §1 ("Every count below is therefore a lower bound") and §10 | One bounded pass per area, ordered by substantive physical content: ch13 §13.6 first (it decides F-34's B3 row), then the reduced-depth proof bodies |
| LC-6 | Kernel identifiers not checked against `verification/lean-manuscript-census.json`, including the directional witnesses of the equivalence displays (audit F-16) and the question at G-9 | audit §10, "Kernel and census" | A read-only census lookup; no Lean build |
| LC-7 | Mirror lists in the ledger are incomplete: D8's FULL mirror is :2894 and :2896 (ch10:88 mirrors at :2896, found by exact line match) | this pass, §1.1 | Correct the D8 mirror cell in the next ledger revision |
| LC-8 | J-1/J-2 (§F.5) name an owner question (Q2) but no accountable Issue; M1–M9 (§10) name none | `LEDGER-r5.md` §F.5, §10 | Record in the ledger the Issues the owner assigns: **(proposal)** #1234 for J-1 and J-2, #914 (O-IF-SELECT) for M1 and #1245 for M9 (Part A §A.2) |

**Proposed order (proposal).** LC-1 and LC-7 (a ledger revision after the accepted r5), then LC-2,
LC-3, LC-4 and LC-6 (each read-only and independent of the others), then LC-5. LC-8 follows the owner's
naming of accountable Issues.

**Authorization Part 2 needs.** The ledger expansion and coverage audit are authorized under #914
comment 6877871344, condition 7 ("This approval authorizes the proposed ledger expansion and coverage
audit after the r2 review"), and #914 comment 6877420015, item 2 ("reading, analysis, writing and
independent review only"). The owner's acceptance of r5 (#914 comment 6879158095) authorizes nothing
further. Whether a revision of the accepted r5 (LC-1, LC-7), a second audit pass (LC-2), the
Main-independence trace (LC-3) and the further reads (LC-4 to LC-6) fall within the existing
authorizations is not stated in any of these records: **owner question**.

***

## Part 3. Research obligations (RO)

### 3.0 The mandatory obligations, and what is already running

**Mandatory obligations** are the Level A rows of `LEDGER-r5.md` §L.A, each UO:
- **A-QM**: inclusion QM ⊆ OI + E on one common realization, and the sector equivalence for a
  physically justified C;
- **A-BELL**: BELL-QSET, H-Bell and Tsirelson selection;
- **A-GR**: GR ⊆ OI on the same substratum and observer;
- **A-REAL**: one common physical realization satisfying the necessary premises jointly (Part 4 and
  joint satisfiability; §9, §10).

Their sources: #914 comments 6875046763, 6875548603 and 6877420015; #1169 comment 6876591512.

**Already authorized work, not ranked here and not gated by this proposal.** The emphasis "must not
make it a new prerequisite for already authorized Bell, gravity or mechanism work" (#914 comment
6878200172), and is not a "new prerequisite for other work" (#914 comment 6879221928). These continue
under their own records:
- **Mechanism.** MECH-1 (#1169 body table): "ready for authorized paper source selection; a
  qualifying physical lead remains the gate for candidate derivation"; owner scope #1169 comment
  6714000230 and writer activation 6714078965. It advances A-QM and A-BELL through M2 and M3
  (`LEDGER-r5.md` §10).
- **Bell.** #868 comment 6874036684: "Next step, authorized as paper-only": a full independent review
  of BS r2, and drafting the `SB-L3.md` extract with its reviews. It advances A-BELL.
- **Gravity.** #873 / #1275: G3 units 1, 2(a) and B_G are completed paper-only units (#873 comments
  6863416405, 6865179466, 6872004336). The QB5(a) preregistration is frozen at `8dd0de90`, and its
  execution is not authorized (#873 comments 6872998421 and 6875553420; RO-2 below).
- **Selection.** #1143: SEL-ACCESS-1 focused confirmation (#1143 body) and the Codex target-neutral
  discriminator (#1143 comment 6863602000).
- **Linearity.** #1049: Readiness "ready"; Authorization "paper-only"; Designated writer "the
  coordinating session" (#1049 body). Its r5 assessment is accepted at a bounded checkpoint (#1049
  comment 6768089770).
- **Carrier.** #1007 LA-GAP: "ready (owner activation …)", paper-only, writer `writer-1007`; "its
  remaining checks … are computations, which c.6642603567 does not authorize" (#1007 body).
- **QCD / Yang–Mills.** #1063: "the paper-only Yang–Mills source review: ready", PO-1102 workstream E
  (#1063 body). It stays at its recorded tier (below).

### 3.1 What each move states, and the evidence used to order them

Each move's accountable Issue is given in Part A §A.2 and repeated at the move.

**Required of each move (owner).** Per #914 comment 6879221928, each move below states: the mandatory
obligation it advances, with its `LEDGER-r5.md` rows; its prerequisites, readiness and existing
authorization as recorded on GitHub; and the concrete next unit and why it outranks the alternatives.
The emphasis of #914 comment 6878200172 (sector justification and confinement to C; exactness with
its carrier foundations; Bell as a separate track; early compatibility of the GR coupling; shared
missing steps and conflicting premises) is "the recommended emphasis—not a predetermined ranking"
(#914 comment 6879221928).

**The drafter's own comparison criteria.** To say why one move outranks another, this draft compares
three things: (i) how many Level A rows a move advances; (ii) what its outcome can and cannot show;
(iii) what it still needs before it can start under §A.45 rule 3 (readiness, a recorded owner
authorization, a designated writer, no conflicting writer). **These criteria and their use are the
drafter's own.** They come from the coordinator's task brief for r1, not from an owner record, and no
owner record gives them an order. The draft does not use them to impose an order the evidence does not
support.

| Move | Advances (Level A; ledger rows) | What its outcome can show | Still needed under §A.45 rule 3 |
|---|---|---|---|
| RO-1 S-J with S-A (#1169) | A-QM, A-BELL, A-REAL (3) | A specification of C; not itself a test | readiness (undetermined), authorization (none), writer (none); S-A has no planning row |
| RO-2 QB5(a) execution (#873) | A-GR, A-REAL, in part (2): B-CC-2; §9 QM–CC, GR–CC; M6 | A rule-determined verdict (A), (B) or (C) on the corpus's own sourcing commitments; (C) is the residual class | execution authorization (none), writer (none recorded for execution), conflicting-writer check |
| RO-3 EXACT carrier inventory (#1055, linked to #1169) | A-QM, A-REAL (2): J-3, J-4, M5, B-QM-8 | Whether J-3 and J-4 bind on an admitted carrier | #1055 is "ready"; authorization (none), writer (none); Q5 or #1055's owner direction for the carrier |
| RO-4 Linearity (J-1, J-2) (#1234, with #1049) | A-BELL, A-REAL (2): B-BELL-4, B-BELL-5, SM §3.1 | A list of preserved controls, after Q2 | #1234 "blocked: owner questions" (item 6 is Q2); then authorization and writer |
| RO-5 unit 2 (#1211) | A-REAL (1): §9 QM–SM; Q9 | A bounded trace | a scope; authorization (unit 1 only); writer |
| RO-6 M1 interface lift (#914, O-IF-SELECT; proposal) | A-QM, A-GR, A-REAL (3); blocks five branches (§10 M1) | Nothing yet: no candidate exists to test | a qualifying candidate |
| RO-7 to RO-10 downstream | one branch each | various | below |

**What the evidence shows.** No move in this table is both ready and authorized with a designated
writer. RO-1 has the widest reach among moves for which a next unit can be specified. RO-2 is the most
fully specified move: its question, inventory, decision rule and controls are frozen and independently
reviewed. What it still lacks is execution authorization and a designated writer. Its verdict, however,
may be the residual class (C), as the two earlier G3 units' outcomes were. **The evidence therefore
gives no order between RO-1 and RO-2.** They trade reach against specification, and the choice between
them is the owner's. They need different writers and address different questions, so authorizing one
does not block the other. Below them, the evidence supports the order RO-3, RO-4, RO-5, RO-6, for the
reasons given at each move. RO-3 now sits at a ready Issue (#1055), as RO-2 does (#873). It ranks below
RO-2 because its scope is not frozen, and below RO-1 on reach.

### 3.2 Proposed moves (proposal)

**RO-1 and RO-2 (owner's choice; no default order).**

**RO-1. Sector condition C: confinement (S-J) with closure within C (S-A). Paper-only specification.**
- *Obligations advanced.* A-QM (the sector equivalence "for a physically justified C"), A-BELL
  (BELL-QSET is stated "for the physically justified OI sector C", #1060 body, question 3), A-REAL.
  Ledger: §L.A A-QM, A-BELL; §12 Q7 (is H-Bell the route to C's recorded exclusion?).
- *Recorded planning.* S-J (#1169 comment 6878199016): Tier Foundational; Prerequisites, Readiness
  "undetermined pending owner decision"; Authorization "not authorized"; status source "open; no
  result on `main` establishes it". S-A: no planning row was found in #1169's body or its 229
  comments, or in #914's body or comments. It is named as an obligation in #1169 comment 6877981234
  ("Kept separate from S-A, closure within C") and in #914 comment 6878200172. #1169's labels:
  `tier: foundational`, `readiness: partly ready`.
- *Concrete next unit.* A paper-only specification: state C as a condition on the underlying model
  with its consequences for experiment families (#1169 comment 6876591512, answer 1); list each
  candidate physical ground for confinement to C, with its source on `main`, whether it is a premise,
  derived or newly proposed, and its §A.29 controls. It carries #1060's constraint that C "may not be
  chosen by testing whether the resulting correlations match quantum predictions" (#1060 body).
- *Why it outranks RO-3 to RO-6.* It advances three Level A rows, against two for RO-3 and RO-4 and one
  for RO-5, and, unlike RO-6, a next unit for it can be specified. The sector directions (#914 comment
  6875548603) and BELL-QSET (#1060 body) are stated relative to C. The owner records S-J and EXACT as
  determining "whether the central physical explanation succeeds" (#1169 comment 6878199016).
- *What it does not do.* RO-1 adds no prerequisite to #1060, #868 or #1143, or to any other
  authorized unit (#914 comments 6878200172 and 6879221928). That BELL-QSET is stated relative to C is
  a fact about its formulation; it does not make RO-1 a precondition for Bell work.
- *Needed before it can start.* Owner decisions on S-J's prerequisites, readiness and authorization; a
  planning row for S-A (§A.45 rule 6); a designated writer; and a check that no active item with a
  different writer writes the same question (§A.45 rule 3). The Codex discriminator on #1143 (comment
  6863602000: "the smallest target-neutral restriction … that excludes the explicit reversible
  PR/supraquantum countercontrol") overlaps this question.
- **(proposal)** S-J readiness → `ready` for this paper-only unit only; S-A receives a planning row
  under #1169.

**RO-2. G3 offset coupling: execute the frozen QB5(a) preregistration.**
- *Obligations advanced.* A-GR and A-REAL, in part. Ledger: B-CC-2 (CD[G3, open]); §9 QM–CC
  ("undetermined") and GR–CC; §10 M6. It does not decide the covariant field equation (B-GR-6, UO) and
  does not discharge A-GR.
- *Recorded planning.*
  - #873 body block, for the Issue as a whole: Tier "High (provisional)"; Prerequisites "none
    recorded"; Readiness "ready"; Authorization "not authorized". This readiness is the Issue's; no
    row records the readiness of QB5(a) execution.
  - QB5(a) was authorized as a paper-only source audit that "may proceed once its decision rule passes
    independent preregistration review" (#873 comment 6872004336).
  - The final check returned "ACCEPT FOR FREEZE" at `8dd0de90`, with "All controls are green" (#873
    comment 6872959810).
  - F was designated: "I designate 8dd0de90 as F; execution needs separate authorization" (#873
    comment 6872998421), which adds: "Execution is not authorized. No inventory row is classified and
    no source analysis starts until a separate owner authorization is recorded here."
  - The latest record, #873 comment 6875553420 (2026-11-14T09:57:14Z): "the QB5(a) preregistration
    stays frozen at `8dd0de90`, and its execution is not authorized". #873 has 12 comments; none
    authorizes execution.
  - **No designated writer is recorded for execution.** The only writer designation on #873 is for
    unit 1 (#873 comment 6859687612: "Claude is the writer").
- *What its outcomes can and cannot show.* The rule is a frozen, independently reviewed decision rule
  with green controls, whose verdict is one of (A), (B) or (C), with (C) the residual class
  (`G3-QB5A-PREREG-r4.md` §8.3 at `8dd0de90`).
  - **(A)** At least one formalization that counts the witness's vacuum-offset term as grounding the
    metric is Admissible, and no formalization that treats it only as a co-constraint survives.
  - **(B)** The reverse: a co-constraint formalization is Admissible, and no grounding formalization
    survives.
  - **(C)** "otherwise. The residual is stated: both kinds remain, neither does, or an undetermined item
    decides" (§8.3 item 3). An undetermined item that changes the result also yields (C) (§8.3 item 4),
    and a grid whose cells disagree yields (C) (§8.4). The two earlier G3 units each returned (C) (#873
    comments 6865179466 and 6872004336).
  - **What no outcome shows.**
    - Every verdict is conditional on Reading G, case β and N5-G (§1.1).
    - Universal-negative conclusions are relative to the frozen inventory and carve list (#873 comment
      6872827835, OQ-2).
    - The audit reads the corpus's own sourcing commitments. A conclusion resting on an unqualified
      assertion "is not independent physical verification of the assertion" (same comment, OQ-7).
    - "Physical source remains NOT PASSED; G3 remains (C)" (#873 comment 6872277416).
    - No outcome derives the covariant field equation or adopts a premise. Under §A.23 any outcome is a
      consistency result.
    - The preregistration's own productivity test counts a completed table that restates the baseline
      as a coherence check, not a gem (§12).
- *Why it ranks with RO-1 and above RO-3 to RO-6.* It is the only move whose question, inventory, rule
  and controls are already frozen and reviewed. Its start needs no new scope, only an authorization
  and a writer. It ranks with RO-1, not above it: it advances less, and its likeliest-looking outcome
  class on the record so far is the residual (C).
- *Needed before it can start.* A recorded owner execution authorization on #873; a designated writer;
  and a check that no other active writer works on the same branch or question (§A.45 rule 3). The
  preregistration also requires the executor to record whether `main` has moved from its source
  snapshot `c3b5f37a` (its "Source snapshot", checkpoint X-2).

**RO-3. Exactness (EXACT): which results depend on one fixed finite total carrier.**
- *Obligations advanced.* A-QM (exact inclusion), A-REAL. Ledger: J-3 ("known not to, on one fixed
  finite carrier, under the factorization interface of `papers/Main.md`:558 (unboundedness
  imported)"), J-4 ("undetermined on a completion"), §10 M5, B-QM-8, and Q5.
- *Accountable Issues.* **(proposal)** The inventory is carried as #1055's next unit, linked to EXACT on
  #1169 (Part A §A.2).
- *Recorded planning.* #1055 body: Tier "High"; Prerequisites "none recorded"; Readiness "ready";
  Authorization "not authorized"; its owner direction fixes preserved results "in advance as controls"
  (#1055 comment 6594944363). EXACT (#1169 comment 6878199016): Tier Foundational; Prerequisites,
  Readiness "undetermined pending owner decision"; Authorization "not authorized". Related: #1007, Tier
  Foundational, LA-GAP ready and paper-only, other SUBSTATE-1 work "undetermined pending owner
  decision (Q-D …)"; #872, "High (provisional)", "blocked: finite reconstruction", "not authorized";
  "#872's narrower scope does not cover all of exactness" (#1169 comment 6877981234).
- *Concrete next unit.* A paper-only inventory: every ledger result that uses one fixed finite total
  carrier (A1 recurrence and C-PRED-8; B-QM-8; B-QM-21; B-QM-28; B-BH-3, B-BH-4 and A.8's cycle
  averages; P-indivisibility at `papers/GR.md`:585), with what is known of each on an admitted
  carrier. A recorded countercontrol already exists: on a countable carrier, recurrence of every state
  does not give a common visible return time (#872 comment 6526240419, research-only, not on `main`).
- *Why it outranks RO-4 to RO-6.* It advances two Level A rows, as RO-4 does, but its first step needs
  one owner answer (Q5), where RO-4 needs an owner answer and an accountable Issue. It decides whether
  two of the four recorded joint-satisfiability conflicts (J-3, J-4) bind the target, or only one fixed
  finite carrier.
- *Needed before it can start.* An owner authorization on #1055 and a designated writer; Q5 (which
  carrier is admitted), or a scope that tabulates per candidate carrier, as #1055's owner direction
  already names one candidate weaker premise (#1055 body); coordination with `writer-1007` (#1007),
  #1015 and #872.
- **(proposal)** EXACT prerequisites → "the #1055 inventory (RO-3); owner answer to Q5".

**RO-4. Linearity: global A5 against the preparation-indexed Bell route and SM §3.1 (J-1, J-2).**
- *Obligations advanced.* A-BELL, A-REAL. Ledger: J-1, J-2 (§F.5); B-BELL-4, B-BELL-5; §9 Bell–SM;
  Q2.
- *Accountable Issues.* **(proposal)** #1234, as its open item 6, with the research question of what
  selects A5 staying on #1049 (Part A §A.2). The ledger names no Issue (`LEDGER-r5.md` §F.5 gives only
  "Q2").
- *Recorded planning.* #1234 body: Tier "Supporting (provisional)"; Readiness "blocked: owner
  questions"; Authorization "not authorized". Its item 6 is the premise question: "(a) the Bell branch
  is kept and (vii) is scoped …; (b) the long-edge route is restated or withdrawn …; (c) the manuscript
  stays as #1233 leaves it, with the incompatibility stated". #1049 body: Readiness "ready";
  Authorization "paper-only"; designated writer recorded. #1060 (H-Bell): Tier High; Prerequisites
  O-K2; "blocked: O-K2"; "not authorized".
- *Concrete next unit.* After Q2 is answered: a paper-only list of the A5-dependent results to serve as
  preserved controls under §A.29 (Q2 names the wave equation, Stage 2(b), harmonic boundary modes and
  "the eight located uses in round H-D").
- *Why it outranks RO-5 and RO-6.* Two Level A rows against one for RO-5; and unlike RO-6, a unit can
  be specified once Q2 is answered. It ranks below RO-3 because its first step is an owner answer, and
  #1234 is recorded as blocked on it.
- *Needed before it can start.* The owner's answer to #1234 item 6 (Q2); then readiness, authorization
  and a writer for the controls list. #1049's authorized work is not gated by it.

**RO-5. Cross-branch QM–SM trace: #1211 unit 2.**
- *Obligations advanced.* A-REAL (§9 QM–SM, "undetermined"); Q9.
- *Recorded planning.* #1211 body: Tier Foundational; Readiness "ready"; Authorization "**unit 1
  only**". Unit 1 accepted at r5, "ACCEPT WITH NITS"; "The ACCEPT authorizes nothing further" (#1211
  comment 6742071797).
- *Concrete next unit.* Not scoped on GitHub. Its finding FI-1 ("nothing on `main` supplies a
  non-monomial admissible operator on the configuration carrier", same comment) is M2, which MECH-1
  already addresses.
- *Why it outranks RO-6.* A next unit can be scoped, and #1211's readiness is recorded as "ready". It
  ranks below RO-1 to RO-4 because it advances one Level A row, and its next question overlaps
  authorized mechanism work.
- *Needed before it can start.* A scope, an owner authorization and a designated writer.

**RO-6. Observer-interface lift (M1).**
- *Obligations advanced.* A-QM, A-GR, A-REAL; §10 M1 blocks QM, SM, GR, cosmology and CC, more branches
  than any other mechanism.
- *Accountable Issue.* **(proposal)** #914, under its O-IF-SELECT row (Part A §A.2). The ledger names
  none (§10).
- *Recorded planning.* #914 O-IF-SELECT, Tier "High (provisional; existing O-PHASE tier)"; Readiness "blocked: no qualifying
  candidate in the bounded checked record; source assessment/review and negative deliverable
  complete"; Authorization "paper-only bounded source assessment completed …; construction remains at
  selection gate" (#914 body).
- *Concrete next unit.* None can be specified: there is no candidate to test.
- *Why it ranks last of RO-1 to RO-6.* Its reach is the largest, but no next unit exists.

**RO-7 to RO-10. Downstream and branch-local obligations: kept below the shared gaps.** "The audit does
not yet justify promoting QCD or another downstream branch ahead of the shared foundational gaps"
(#914 comment 6878781541). No tier or readiness change is proposed for any of them.
- **RO-7, SM flavour** (U-4 to U-8): the $1/d$ amplitude (B-SM-FLAV-9), the $b_{23} = 1$
  normalization (B-SM-FLAV-6), the analytical K (B-SM-FLAV-3), and the $O(\lambda^3)$ route or exact
  diagonalization for Cond 2 (B-SM-FLAV-10). **(proposal)** A new Issue (Part A §A.2): no open Issue
  covers flavour derivations.
- **RO-8, energy shell and W1** (§10 M9; B-GR-7): blocks GR, cosmology, CC and BH. **(proposal)**
  Tracked on #1245, which already tracks "the W1 thermodynamic-slope gap" (#1244 status note); its body
  records: "No new investigation of the physical source of the entropy-slope equality is authorized
  yet."
- **RO-9, observer genericity** (U-2): whether C2 and C4 fail for typical bijections. **(proposal)**
  Recorded on #1062 (OBS-EMERGE), the closest existing scope.
- **RO-10, QCD and nonperturbative questions** (U-3; B-QCD-5, B-QCD-6, B-QCD-8; K-9 / U-9): #1063, Tier
  "Exploratory"; the paper-only Yang–Mills source review is ready under PO-1102 workstream E;
  integration is "blocked: #872" (#1063 body). Q14 (`LEDGER-r5.md` §12) asks whether the mass gap,
  confinement and the hadron spectrum are Part 4 obligations or recorded scope limits. The record
  search for K-9 is LC-4, on #914.

### 3.3 Proposed planning changes, all marked (proposal)

None takes effect without a recorded owner decision.
Each is listed under its Issue in Part A.
1. #1169: S-J readiness → `ready` for the RO-1 paper-only specification only (PC-2); a planning row
   for S-A (PC-1); EXACT prerequisites → "the #1055 inventory (RO-3); owner answer to Q5" (PC-3).
2. #1055: the exactness inventory as its next unit (RO-3).
3. #1234: J-1 and J-2 recorded as its item 6 (RO-4). #914: M1 under O-IF-SELECT (RO-6). #1245: M9
   (RO-8). #1062: U-2 (RO-9).
4. One new Issue for SM flavour derivations (RO-7).
5. The MC assignments of Part A §A.3, with #1028 as the home of the remaining units (Option A), or one
   new Issue (Option B).

No tier change is proposed. No change is proposed for #1063 or any other downstream item, or for
RO-2's planning attributes: its execution needs the owner's separate, explicit authorization and a
designated writer, and readiness is not authorization (§A.45 rule 3).

**Authorization Part 3 needs.** Each new move (RO-1, RO-3, RO-4, RO-5) needs readiness, a recorded
owner authorization, a designated writer and no conflicting writer (§A.45 rule 3). RO-2 needs a
recorded execution authorization, a designated writer and the same conflicting-writer check. Any new
premise, mechanism or selection principle is judged under §A.29 (§A.45 rule 5). Integration and
publication are each separate decisions (§A.45 rule 7).

***


## Owner questions this proposal raises

Grouped by the Issue each concerns.

**The manuscript corrections.**
1. **Option A or B (Part A §A.1).** Under Option A, the remaining correction units become rows of
   #1028's planning block, which widens #1028 beyond "the 2026-11-01 disposition". Under Option B, one
   new Issue takes them instead.
2. **The specific homes (Part A §A.3).** Whether to assign:
   - F-32 and F-3's Higgs clauses to #1058;
   - D5 and F-7 to #1142;
   - D7 to #1190;
   - S-1, S-2, S-17 and K-5 to #1238;
   - F-17 (:179), G-2, G-30 and T-4 to #1244;
   - D2 to #1029;
   - F-10 to #1015.

   Each assignment widens that Issue's recorded scope.
3. **#1244: Structure:179.** Should the authorized Structure:179 draft also take F-17's level-placement
   defect at the same line, or should a separate unit follow it?
4. **#1244: GR:12.** G-2 records that the "unconditional" horizon count rests on a partition that
   presupposes GR causal structure (GR:40). #1244's sweep rule says "no conditions are added to
   unconditional mode-count or geometry statements". Is the count at GR:12 to be classified as
   unconditional under that rule, or is G-2's dependency to be carried?
5. **Overlaps with #1190.** F-35 shares appendix-a row 1 with #1190 WP3-34/WP8-10, and F-9's site
   SM:1118 was reworded under #1190 WP3-33. Which Issue owns each of these lines?
6. **Order and authorization.** Which correction units, if any, to authorize, and in what order (§1.6).

**#914 (ledger coverage and its owner questions).**

7. **The ledger authorization.** Do LC-1 and LC-7 (a revision of the accepted r5), and LC-2 to LC-6,
   fall within the existing ledger authorization (#914 comments 6877871344 and 6877420015)?
8. **The ledger's own questions.** Q5 (carrier) and Q6 (Part 4 scope; decides D6 and D11).
9. **M1.** Whether to track M1 under O-IF-SELECT (RO-6).

**#1169 and #873 (the first research moves).**

10. **RO-1 and RO-2.** Which to authorize, if either: the reach of RO-1 or the specification of RO-2
    (§3.1). There is no default order.
11. **S-J and S-A.** The S-J readiness and the S-A planning row (PC-1, PC-2).
12. **#873's stale pointer.** #873 comment 6600178826 says that #873's planning attributes "are kept
    in #1074". #1074 was closed on 2026-11-03T16:49:08Z, state reason `completed`, after that comment.
    The #873 body block is therefore the live record. The only open point is whether to note the stale
    pointer, which §A.45 rule 3's maintenance clause allows for a sourced fact.
13. **MECH-1's writer (#1169).** The body row names "Claude Code sole writer", while the body's
    coordination note says "Claude is paused as a writer" and the 2026-11-08 Claude assignment "is
    superseded for **new work only**". This proposal does not resolve it.

**#1055, #1234, #1245, #1062 and the new SM-flavour Issue.**

14. **#1055.** Whether it carries the exactness inventory (RO-3), linked to EXACT (PC-3).
15. **#1234 item 6, which is Q2.** Its answer gates RO-4. #1049's authorized work is not gated by it.
16. **#1245 and #1062.** Whether to record M9 on #1245 and U-2 on #1062.
17. **SM flavour.** Whether to open the SM-flavour Issue (RO-7), or to use #970 rows instead.

## Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #914 comments 6875046763, 6875548603, 6877420015, 6877871344, 6877908458, 6878200172, 6878781541, 6879158095, 6879221928; #1169 comments 6876591512, 6877981234, 6878199016 | The obligations, acceptance and guidance the proposal is organized by | Provenance: owner records quoted for scope; no scientific claim rests on them |
| The owner's grouping direction, relayed by the coordinator (no GitHub record seen) | The organization of Part A | Provenance only |
| Planning blocks and comments of #866, #868, #872, #873, #914, #944, #970, #1007, #1015, #1028, #1029, #1049, #1055, #1058, #1060, #1062, #1063, #1074, #1142, #1143, #1169, #1190, #1211, #1234, #1238, #1244, #1245, #1255 | Recorded tier, readiness, authorization and scope in Part A and Part 3 | Provenance: planning records (§A.45 rule 1) |
| #872 comment 6526240419 | The countable-carrier countercontrol named in RO-3 | Provenance only: a research-only paper result not on `main`; cited as motivation, not as support |
| #1238 comment 6800989329 (trace T2, "session files, not on `main`") | LC-3 | Provenance: LC-3 reconciles with it; no claim here rests on its content |
| `G3-QB5A-PREREG-r4.md` at `8dd0de90` on #1275 | RO-2's description of the outcome classes and their conditions | Provenance: a frozen planning record not on `main`, read for what its rule can return; no scientific claim here rests on it |
| `LEDGER-r5.md` (owner-accepted at `de29ccd8`), `REVIEW-r5.md`, `COVERAGE-AUDIT-r4.md`, `REVIEW-AUDIT-r4.md`, `QUEUE-PROPOSAL-r1.md`, `QUEUE-PROPOSAL-r2.md`, `REVIEW-QUEUE-r1.md` (drafts, not on `main`) | The findings and rows the proposal lists, and the reviews it applies | Provenance: every manuscript passage quoted here is cited by its line on `main` at `dfeec843` |

Every manuscript passage cited in this proposal is a line of a file on `main` at `dfeec843`.
