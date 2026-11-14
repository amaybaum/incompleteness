# G3 QB5(a) (preregistration r2): the framework's own source terms against F4

**Scope.** This is the preregistration of a paper-only audit under Issue #873, continuing unit 2(b)
(PR #1275). It fixes the question, premises, inventory, classification scheme, decision rule, controls and
outcome classes before any source is read for the answer. It contains no analysis of an inventory
passage, renders no cell of the audit table, and states no expected outcome.

- **Authorization.** #873 comment 6872004336 (`amaybaum`, 2026-11-14T04:53:01Z):
  - "QB5 | Authorize (a) — the F4-versus-F5 source audit, paper-only."
  - "QB6 | … Freeze and independently review the next unit's rule before analysis."
  - "The next investigation must test the framework's own gravitational source terms against F4, rather
    than selecting F4 merely because it excludes an unwanted coupling."
  - "The QB5(a) investigation may proceed once its decision rule passes independent preregistration
    review."
  - "QB7(a) | Do not adopt running-vacuum sourcing as a premise. QB7(b) | Leave the gravitating
    counterpart open for the QB5(a) investigation."
- **Owner guidance.** #873 comment 6872277416 (`amaybaum`, 2026-11-14T05:17:28Z):
  - "G3 QB5(a): The preregistration-first approach is essential."
  - "The decision rule must apply equally to the corpus's own metric-dependent source terms and the
    disputed vacuum-offset coupling, without selecting F4 or F5 to obtain a preferred result."

  It is built in as invariant I-SYM (§1.3), checkpoint X-5, and countercontrols RC-W and RC-T (§10.4,
  §10.7).
- **Revision history.**
  - r1 is `qb5a/G3-QB5A-PREREG-r1.md` at `2e18a2df`. Its independent review is
    `qb5a/REVIEW-QB5A-PREREG-r1.md` (REVISE) at `66015291`.
  - r2 applies QR-1 to QR-26. The dispositions are in `qb5a/RESPONSE-QB5A-r1.md`. r1 is not edited.
  - Owner answers to OQ-1 to OQ-5 and OQ-7 are pending. At each point of use, r2 carries the reviewer's
    recommended answer, marked "(pending owner decision OQ-n)". §15 gives the alternative text for each,
    so that an answer can be applied by a minimal amendment before freeze.
- **Inputs** on branch `research/g3-offset-873-20261113`, directory
  `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/`:
  - `G3-UNIT2B-BG-r5.md` ("r5:n"), with `CONFIRM-BG-r3.md` and `CONFIRM-BG-r4.md`;
  - `G3-UNIT2A-r3.md` ("U2Ar3:n") and `G3-UNIT1-r5.md` ("U1r5:n").

  These are reviewed research drafts on a branch, not established results on `main` (§A.46 item 7).
  They are used for definitions and stated, reviewed inferences only, and are cited where used.
- This preregistration runs no computation on OI rules, changes no manuscript, adopts no premise and
  makes no claim about Λ.

**Source snapshot.** `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`, the snapshot of units 1, 2(a)
and 2(b). Every corpus `file:line` refers to that commit. At execution the executor records whether `main`
has moved (X-2). A changed inventory passage is a deviation (§14.2), and the audit still reads the pinned
snapshot.

**Support labels** are as in r5: [K], [A], [P] and [L, recalled]. **Conditional** marks a claim that
holds only under the hypotheses it names.

**Terms carried from r5 and unit 2(a)** (r5:36–48; r5 §1–§3): ⊳_G, ⊳_D, N1–N3 in ⊳_G, N3′, N5-G,
Reading G, case β, the witness, B_G, F3, F4, F4-null, F4-c, F5, Lemma U, K1–K5, and the content classes
"grounding-content" and "CoC-content" relative to the witness's term. The witness's term is written
`ρ_Z` (U1r5:222–225; U2Ar3:315–342).

***

## 0. Summary

- **Question (§1).** On the corpus's own sourcing commitments, is F4 consistent with the corpus, and in
  which scope? Is an F4-c class specified? Is F5 consistent with the corpus? The same classification and
  the same F4 and F5 tests are applied to every corpus source term and to the disputed vacuum-offset
  terms, both the corpus's own offset (GR:352) and the witness's `ρ_Z`.
- **Stages.** Stage 2 gives verdicts on the formalizations from the audit table. Stage 3 maps them to
  B_G's outcome (A), (B) or (C). Stage 2 lands in a commit before Stage 3 is written. The headline rule of
  §8.4 combines the coordinates.
- **Stage-2 classes for F4 (§8.2).**
  - **R:** F4 rejected on the corpus's own commitments.
  - **Cc:** uniform F4 rejected, with an F4-c class specified that passes the grounding-relevance test
    and K1–K5.
  - **C:** F4 compatible.
  - **U:** undetermined, with the deciding cell or control named.
- **Controls (§10).**
  - RC-P (positive) and RC-N (negative).
  - RC-X (countercontrol, twelve flips).
  - RC-W, including W-e, the status-blindness of the predicates.
  - RC-U (undetermined).
  - RC-T, thirteen text controls that exercise the per-term tests.
  - X-18, a blind second reading of every attribute cell.

  All rule-level controls are on constructed or external examples.
- **Owner questions (§15).** OQ-1 to OQ-5 and OQ-7 are pending. OQ-6 is answered by #873 c.6872277416.

***

## 1. The question

### 1.1 Statement

Let F4 be r5's formalization (r5 §1.3, §3.4): the boundary law is not fundamental, and the energy content
of every term of the realized equation other than the Einstein tensor grounds the realized metric. Its
variants are those of §3.

**Q.** On Reading G, case β, conditional on N5-G, and on the premise base of §2:

- **Q1.** Does some term that the corpus holds as a commitment in a source role (§5.3) become
  unrealizable under F4, or under a given F4 variant, with no carve-out that has a difference relevant to
  grounding?
- **Q2.** Does the corpus commit, in grounding vocabulary, to some term grounding the metric, which F5 or
  a co-constraint variant denies?
- **Q3.** Which scope of F4 do the corpus's sourcing statements fix, if any?
- **Q4.** Does the corpus fix the classical counterpart of an epoch-differential piece under §8.3, and what
  is GR:577's scope clause?
- **Q5.** Is the G3 target the corpus names (GR:12) a divergence-free sourcing law or a null-flux route?
- **Q6.** Where does GR:581's ground for non-sourcing fall against GR:384?

Q1 and Q2 decide the Stage-2 verdicts. Q3–Q6 supply cells and candidate carves to them (§11).

### 1.2 What the question is not

The audit does not ask whether F4 excludes the witness. That was r5's result, conditional on F4 (r5 §3.4).
F4 is accepted or rejected here on the corpus's own sourcing commitments. That F4 excludes the witness, or
does not, is no reason for either verdict.

### 1.3 Blindness and symmetry

- **I-SYM (symmetry; owner guidance, #873 c.6872277416).**
  - Every row of the audit table receives the same attributes (§5) by the same operational tests. This
    covers the corpus's metric-dependent source terms, the corpus's vacuum-offset rows (GR:352, GR:577)
    and the witness rows W0-Z0, W0-ZI and W0-ZII (§4.4).
  - The derived cells (§6) are computed by the same predicates for every row.
  - Every carve (§7) and every decision clause (§8) is a predicate on attribute values. None names a
    row.
  - No carve predicate and no U cell reads A3 (stated status). Only the rejecting predicates of §6.3 read
    A3. W-e (§10.4) tests this.
- **I-BLIND (no fitting to the witness).** The choice between F4 and F5, of an F4 scope, or of an F4-c
  class is not made by reading what it does to the witness. It is enforced in six ways.
  1. **Fixed candidate space.** The formalizations (§3), the carve predicates Δ1–Δ8 (§7.2), and the
     enumeration procedure for Δ9.k (node Q-6a) are fixed here. The Δ9.k list lands in a commit before
     any GRT verdict (X-19). A carve found otherwise is a deviation (§14.2), and its justification cites
     no W0 attribute.
  2. **Reason-based carves.** A carve is admitted only through the grounding-relevance test (§7.1).
  3. **Inertness of constructed rows.** A3 is read from the corpus, so a constructed row has A3 = Cx. The
     rejecting predicates never fire on Cx, so W0 rows cannot move a Stage-2 verdict. This follows from
     the predicates. It is checked as a consistency property (§10.4), not counted as a countercontrol.
  4. **Stage order.** The Stage-2 table and verdicts land in a commit before the W0 rows are classified
     and before any Stage-3 text exists (X-7).
  5. **Text controls.** RC-T fixes the required values of the per-term tests on constructed sentences
     (§10.7). It is run by the executor and by the second reader.
  6. **Blind second reading.** A second reader, a different agent from the executor, classifies every
     attribute cell without having read r5's per-passage readings (X-18).
- **No coordinate selection.** No branch, route or witness convention is chosen to break a disagreement
  (§8.4).

***

## 2. Premise base and excluded list

### 2.1 Premise base (carried from r5 §1.1 and §3.1)

- **The corpus's stated premises:** the text at `c3b5f37a`, as cited, with its stated status.
- **Reading G's premises:**
  - N1–N2-G (GR:40; GR:346 s.1–s.2);
  - N3-G (GR:342's clause "QM is emergent"; GR:344);
  - transitivity of ⊳_G;
  - N5-G, labelled as not stated in the corpus (U2Ar3:226–231).
- **N3′** (r5 §2.2): a quantity defined as a function of another is grounded in it. Covariation without
  definition is ⊳_D only (K5).
- **Lemma U, general form only** (r5 §3.1) [A], given these premises: a law term grounded in the realized
  metric does not ground that metric. Its application to the witness, and Corollary E, do not enter
  Stage 2.
- **The set-level reading, general form only** (r5 node F4-7; reviewed as sound in CONFIRM-BG-r3 §4) [P]:
  a count, total or density over a partition-selected set is grounded in the set's membership, and through
  N1–N2-G in the metric.
- **The diachronic reading** (r5 node F4-3) [P]: with a slice-local partition and diachronic relata, the
  cycle does not close. Relata are a property of the formalization (§3).
- **P-D** (r5 §3.3): Main:44, Main:54, Structure.md:136. F3 is carried as rejected by (b2) and is not
  re-audited.

### 2.2 Excluded as premises

Items on this list may be quoted as vocabulary, but none is the premise of a decisive step (K4). A row
whose own passage is on this list has A3x = yes (§5.3).

- **From r5:**
  - B_G and its negation;
  - (ii-W), (ii-L), (ii-S) and (ii-G) as exclusions;
  - GR:342 "This ordering is forced …" and "not the reverse";
  - GR:346 s.4;
  - book/ch07-gravity.md:187;
  - GR:340 s.1's ordering clause and GR:340 s.2 (P11);
  - GR:575's clause "What does not gravitate";
  - any form of the boundary law, its derivation or its non-derivability (G3);
  - the separation clauses of Substratum.md:385–389, and GR:655's clause.
- **Added.**
  - **Running-vacuum sourcing (QB7(a)).** It is not adopted by owner decision and not imported from the
    running-vacuum literature. Its corpus status is read from the text by §5.3's test, as for every row
    (pending owner decision OQ-1). §8.2 carries the QB7(a) sensitivity line.
  - **F4, F5, F4-dia and every variant.** These are assessed, never used as premises.
  - **Prior verdicts.**
    - r5's outcome (C) and its residual.
    - r5's §2.4 "Reading [P]" column and its node verdicts on inventory passages. Cells are derived from
      the text by §5–§6. r5's readings are cited only after a cell is rendered, to record agreement or
      disagreement (X-13).
  - **The G3 route as a premise.** Q5 records what the corpus names as its target. No step takes a form of
    the boundary law as a premise. Roles are recorded per route where the passages state them (§5.1), and
    Stage 3 is computed per route.

***

## 3. Formalizations assessed

Every formalization in the main table is synchronic, as in r5 §3.4: energy content at a slice grounds the
realized metric at that slice.

| ID | Statement | `Dom(v)`: the quantities whose energy content grounds the metric |
|---|---|---|
| F4 | r5 §3.4, as stated | every quantity with role T or IC (§5.1), whatever its component |
| F4-law | F4 restricted to the law's input terms (QB5(a)'s "law terms"); ≡ F4[Δ3] | role T |
| F4-null | F4 restricted to the null-flux source (r5 F4-6); ≡ F4[Δ4] | role T or IC, with A1c ∈ {full-tensor, null-flux}. A1c = uniform is outside. A1c ∈ {density-only, unstated} gives Und |
| F4[Δ] | F4 with `class(Δ)` not grounding (§7.2), Δ ∈ {Δ1, …, Δ8, Δ9.k} | `Dom(F4)` minus `class(Δ)` |
| F5 | co-constraint, regularity view (r5 §1.3) | empty |
| F3 | fundamental governing law | carried, rejected by (b2) (r5 §3.3) |

**F4-dia** (r5 node F4-3) is F4 with diachronic relata: energy content at `s` grounds the metric at
`s′ > s`. Its domain is `Dom(F4)`. It is assessed by the same predicates, with its own U cells (§6.2). Its
verdict is reported beside F5's. It does not enter the Stage-2 summary class. It is sorted at Stage 3 like
any formalization.

**Sorting at Stage 3 (pending owner decision OQ-3).**

- F4-c, in r5's sense, is any admissible F4[Δ] whose class does not contain the witness's term.
- An admissible F4[Δ] whose class contains the witness's term is CoC-content with respect to it. This is
  r5 §1.2's content definition, relativized by R-6 and applied to every carve.
- The sorting is done at Stage 3 only.

***

## 4. The inventory (closed)

### 4.1 Unit of classification

- A **row** is one inventory passage. A **quantity** is a gravitational term the passage names. When a
  passage names several quantities, each is classified separately, under a suffixed row ID (for example
  T-GR400·R1).
- **Same quantity.** Two rows concern the same quantity when either:
  - they use the same symbol or name it by the same defined phrase; or
  - one explicitly cross-references the other (a section reference, or "the identity above").
- The executor records the same-quantity table at node Q-1. It lands in a commit before any derived cell
  (X-19).
- Every row is classified by §5. A row with no gravitational quantity has role N, and its derived cells
  are "—".

### 4.2 Corpus rows (`c3b5f37a`)

**Group S: source-term passages, QB5(a)'s list.**

| Row | Passage | Content located (not evaluated) |
|---|---|---|
| T-GR374 | GR:374 | the emergent vacuum energy, "a state-level quantity depending on the hidden sector's volume"; the sentence beginning "The defensible statement" |
| T-GR376 | GR:376 | the display of `Λ_eff(H)` |
| T-GR378 | GR:378 | the three architectural commitments (i)–(iii); `A = 4πc²/H²` |
| T-GR380 | GR:380 | the Type II identification; running `G`; the Bianchi identity |
| T-GR384 | GR:384 | the `ρ_s(H) = ρ_crit(H)` bullet; "total gravitating boundary energy" |
| T-GR422 | GR:422 | Corollary step (i), the total effective density: the definitions entering `ρ_s` |
| T-GR424 | GR:424 | the display of `ρ_s` |
| T-GR426 | GR:426 | the identity as "a consequence of Jacobson's Clausius relation applied to the de Sitter horizon" |
| T-GR400 | GR:400 | the Remark: Reading 1 (·R1) and Reading 2 (·R2) |
| T-GR528 | GR:528 | the CMB paragraph: "non-oscillating gravitational source"; the entropy displacement |
| T-GR530 | GR:530 | `ρ_E`, items (i)–(iv) |
| T-GR581 | GR:581 | QCD binding energy; the non-sourcing clause and its stated ground |
| T-SM144 | SM:144 | the discrete Einstein equation (target form) |
| T-SM146 | SM:146 | its display, `κ_OR = α 𝒯_ij` |
| T-SM148 | SM:148 | the definitions of `κ_OR`, `𝒯_ij` and `α` |
| T-SM150 | SM:150 | the proof, steps (i)–(iv) |
| T-SM152 | SM:152–156 | the sparse preparation-indexed edges diagnostic |
| T-SM158 | SM:158 | orbit self-consistency; "would constrain … were the curvature step (iv) supplied" |
| T-SM160 | SM:160 | Jacobson's four inputs, including (iii), the energy flux |
| T-SM162 | SM:162 | the displayed equation with `Λ g_μν` |
| T-GR695 | GR:695 | weak-field gravity at the fixed `G`: the Newtonian field and its source (QR-15) |

**Group V: the corpus's vacuum-offset coupling (owner guidance).**

| Row | Passage | Content located |
|---|---|---|
| T-GR352 | GR:352 | the two completions, `𝒢 = 8πG T^cl` and `𝒢 = 8πG(T^cl − ρ_C g)`; "a coupling theorem" |
| T-GR577 | GR:577 | the reconstruction-gauge form; "Whether the offset sources curvature is not settled"; the scope clause (also Q4) |

**Group Q: rows for Q3–Q6.**

| Row | Passage | Serves |
|---|---|---|
| G-GR12 | GR:12 | Q5: "the decisive Level-G3 target … is a covariant equation"; the displayed target form |
| G-GR162 | GR:162 | Q5: "the covariant field equations remain the Level-G3 target"; Jacobson used, not derived |
| G-GR370 | GR:370 | Q5: "the covariant Level-G3 target, open" |
| G-GR691 | GR:691 | Q5: the derivations' use of Einstein dynamics through Jacobson's relation |
| G-GR693 | GR:693 | Q5: the dimension and curvature tool (QR-15) |
| G-GR697 | GR:697 | Q5: item (ii), "The full nonlinear `G_μν = 8πG T_μν` … not established" |
| G-GR701 | GR:701 | Q5: "the covariant Level-G3 target equation (§7)" (QR-15) |
| G-SM120 | SM:120 | Q5: "Einstein's equations as self-consistency"; Jacobson's inputs on the graph (the inventory search, NOTES §5) |
| E-GR569 | GR:569 | Q4: relative effects; the absolute zero-point sum |
| E-GR571 | GR:571 | Q4: the Higgs potential paragraph (QR-15) |
| E-GR573 | GR:573 | Q4: "What gravitates"; the classical microstate difference |
| E-GR575 | GR:575 | Q4: vocabulary only (excluded as a premise; A3x = yes) |
| E-GR579 | GR:579 | Q4: "The principle is uniform …" |

**Group C: context rows** (classified like every row).

| Row | Passage | Reason for inclusion |
|---|---|---|
| C-GR354 | GR:354 | the stated status of the Type II channel |
| C-GR358 | GR:358 | "feed back … through state-level quantities" (r5's K3 list) |
| C-GR382 | GR:382, :385–386 | the companion bullets of GR:384 |
| C-GR388 | GR:388, :398 | magnitude: the emergent-QFT channel and the substratum mode count |
| C-GR418 | GR:418 | the statement of the Corollary whose proof is T-GR422 to T-GR426 (QR-15) |
| C-GR428 | GR:428–434 | the Corollary's clarifications on `ρ_s` |
| C-GR444 | GR:444–452 | Corollary steps (ii-a), (ii-b) and (iii) |
| C-GR458 | GR:458 | the uniform and structured components of the boundary entropy (inventory search) |
| C-GR468 | GR:468 | §7.3 Step 1, the entropy displacement (inventory search) |
| C-GR474 | GR:474 | §7.3 Step 2, the conversion of the entropy gradient |
| C-GR482 | GR:482 | "The Jacobson mechanism converts the entropy gradient into curvature" (r5 K3; AW-entropic) |
| C-GR532 | GR:532 | "the Jacobson sourcing is spatially local" |
| C-GR633 | GR:633 | "The Type II running-vacuum functional form is not derived" |
| C-SM164 | SM:164 | the continuation of SM:162: the correction term |

**Group K: the K3 uses of r5 that are not otherwise rows** (QR-8). These are split by sentence wherever
§2.2 excludes a sentence or clause.

| Row | Passage |
|---|---|
| K-GR340·s1, ·s2, ·s3, ·s4 | GR:340, sentences 1–4 (s1's ordering clause and s2 are excluded: A3x = yes) |
| K-GR342 | GR:342 (its excluded clauses: A3x = yes) |
| K-GR346 | GR:346 s.1–s.3 (s.4 is excluded) |
| K-Sub385, K-Sub387, K-Sub389, K-Sub391, K-Sub393 | Substratum.md:385, :387, :389, :391, :393 (the separation clauses of :385–389 have A3x = yes) |

GR:693 and GR:695 are added under QR-15. The search that closes the inventory, and each excluded hit with
its reason, are recorded in NOTES-QB5A-r2 §5.

### 4.3 K3 corpus uses

These are r5's K3 list: GR:340, GR:342, GR:346, Substratum.md:385–393, GR:162, SM:160–162, GR:374–380,
GR:384, GR:400 Reading 1, GR:482 and GR:528–530. Each is a row in §4.2 (Group K or another group), so
GRT-4 reads its attributes.

### 4.4 Constructed rows (A3 = Cx)

| Row | Definition source | Note |
|---|---|---|
| W0-Z0 | `ρ_0` (U2Ar3:322–323), in K_cpl^conv[Z_0] (U2Ar3:340–342) | GR:362's density as written |
| W0-ZI | `ρ_I` (U2Ar3:324–325) | constructed IR limit |
| W0-ZII | `ρ_II` (U2Ar3:326–330) | unit 1's literal form |

- The convention map `Z` is defined at U1r5:222–225.
- W0 rows are classified by §5–§6 at node Q-8, from these definition sources only.
- Their role is computed per route under §5.1's per-route clause, because the route is not a premise
  (§2.2). The routes are 𝒞_div (U1r5:198–204) and the Jacobson route (U1r5:603–606).

### 4.5 Rule for passages found later

- A passage not listed in §4.2–§4.4 that is found during execution is recorded as a deviation row `X-n`
  (§14.2), classified by the same scheme.
- It does not enter the decisive table. The verdict is rendered on the frozen inventory, and the record
  states whether it would differ with the row included.
- An X-row changes a rendered verdict only through an amendment (§14.3). The verdict as rendered stays
  beside the amended one.
- These rules apply before and after rendering alike.

***

## 5. Per-row attributes

Each attribute has values, an operational test and examples from outside the inventory. Every cell cites
its line or lines. A cell the tests cannot fix from the cited text is Und. A test that cannot be applied as
written gives Und (§14.2).

### 5.1 A1, role in the law

**Values.**

- T: a term of a field equation of the realized metric;
- IC: an integration constant, or the datum that selects one;
- NS: stated not to source;
- Dep: a dependence on geometry is stated, with no role in a field equation;
- N: no gravitational quantity;
- Conflict-R;
- Und.

**Sub-attributes.**

- **A1s, the side as presented:** left, right or verbal. It is recorded for information only and enters
  no predicate.
- **A1q:** yes if a passage states the quantity's value or identity as obtained by evaluating a law of the
  gravitational dynamics, as the passage identifies it, on a given solution. Otherwise no.
- **A1c, the component:**
  - full-tensor: a general symmetric tensor, or a stated density with a stated pressure other than
    `−ρ`;
  - density-only: an energy density with no stated pressure;
  - uniform: ∝ `g_μν`, or a density with pressure `−ρ`;
  - null-flux: only `T_μν k^μ k^ν` enters;
  - unstated.

**Test.**

- **T** if either:
  - the quantity is a term of a displayed or verbally stated field equation of the realized metric,
    other than the Einstein tensor, on either side as presented (r5 §3.4, node F4-1); or
  - a passage says it "sources", "is a (gravitational) source" or "source term", "gravitates", "is
    gravitationally active", "feeds back as a source", or is converted "into curvature".
- **IC** if it is called an integration constant, or the datum that fixes one. For a quantity and route
  on which both T and IC hold, the role is IC.
- **NS** if a passage states that the quantity does not source, gravitate or enter the field equation.
  Its status is read by §5.3, with "non-sourcing" in place of "source role".
- **Dep** if only a dependence is stated ("depends on", "inherits an `H`-dependence").
- **Per route.** Where the passages on a quantity state its role per route (a divergence-free sourcing
  law, or the Jacobson route), the role is recorded per route. This applies to every row, corpus or
  constructed.
- **Aggregation per quantity, and per route where recorded.**
  - T and NS on one quantity give Conflict-R. `Dom(v)` membership is then Und, unless the two are scoped
    to different branches (§6.1).
  - Otherwise: IC if any row gives IC; else T if any row gives T; else NS if any row gives NS; else Dep;
    else N.
  - A1q does not remove role T. Its bearing on grounding is the carve Δ2 (§7.2).

**Examples outside the inventory.**

- The perfect-fluid `T_μν` in `G_μν = 8πG T_μν` is T, full-tensor.
- A fixed `Λ g_μν` written beside the Einstein tensor is T, uniform, with A1s = left (TX-6).
- In unimodular gravity, Λ is IC (TX-7).
- The Komar mass of a Schwarzschild solution has A1q = yes and no role T (TX-13).
- A radiation density obtained from the Stefan–Boltzmann law has A1q = no.
- "The black hole's entropy depends on its area" is Dep.

### 5.2 A2, the definiens (the N3′ test)

**Values.**

- **M:** defined as a function of the metric, directly or through a metric-defined item. The subtype is
  recorded:
  - M-geo: curvature, `H`, a horizon area or radius, a horizon temperature, or the metric volume of a
    region selected by the metric;
  - M-set: a count, total or density over a set selected by the observer's causal partition (F4-7);
  - M-em: an emergent computation from the reduced description at the realized partition;
  - M-pure: a functional of the metric alone.
- **C:** defined on the microstate of cells fixed independently of the metric.
- **X:** a constant or convention with no metric input.
- **Und:** no definition is stated in the inventory or the premise base.

**Test.**

- Write the defining expression as the corpus states it, with its citation.
- The value is M if any argument is the metric or an item whose definition takes the metric. That
  includes the partition Π(g) of GR:40 in case β.
- **Measure clause.** The metric entering only as the measure or normalization that expresses a
  microstate-defined energy as a local density or tensor does not make the quantity M. This covers:
  - the proper volume element at a point;
  - the normalization of a 4-velocity;
  - raising and lowering indices.

  The following do make it M:
  - a metric volume of a region selected by the metric (a horizon volume, a Hubble volume);
  - curvature, `H`, or any derivative of the metric;
  - a horizon;
  - the partition.
- A value that covaries with `H` without a definition through the metric is not M (K5). The covariation is
  recorded in A3v.

**Sub-attributes.**

- **A2p, partition-definedness.**
  - Yes if an argument of the definiens is the observer's causal partition (in OI, Π(g) of GR:40), its
    boundary, or a set or count it selects.
  - No if the definiens is C or X, or if it is M with no such argument.
  - Und otherwise.
- **A2t, the cycle.**
  - closing: the dependence is on the same realized metric, or on a global structure such as an event
    horizon or a global Killing structure;
  - slice-local: defined from a slice's metric, with a slice-local partition;
  - Und.
- **A2§, the §8.3 counterpart.** It is filled only for quantities the corpus states as relative or
  epoch-differential, that is, where the words "relative", "difference" or "epoch-differential" are
  applied to the quantity.
  - fixed-cell: a microstate difference on cells specified independently of the partition is named;
  - set-total: a total over the hidden sector or over a partition-selected set is named;
  - emergent-as-defined: the emergent computation is named, with no relocation;
  - not fixed: no classical item is named for this quantity.

**Examples outside the inventory.**

- The Hawking temperature `κ/2π` is M-geo, with A2p = no.
- The average energy density inside a static star's photon sphere, total energy over that region's proper
  volume, is M-geo (TX-10).
- The number of quanta beyond a uniformly accelerated observer's Rindler horizon is M-set, with A2p = yes
  (TX-8).
- The `R`-term of `f(R)` gravity written as an effective stress tensor is M-pure.
- Dust with `ρ = n m c²` is C (TX-9). An electron's rest energy is C.
- A fixed bare cosmological constant is X.
- For A2§: "the electron/no-electron energy difference corresponds to a difference in the electron's own
  cells" is fixed-cell; "the difference in total radiation energy inside the Hubble volume" is set-total.

### 5.3 A3, the stated status of the source role

**Values.**

- D, D|cond and Rq: commitments with a status word;
- As: asserted in the corpus's own voice, with no status word in scope and no inherited status note whose
  scope includes the source role;
- Ps, In, ND and Op: hedges;
- Ns: the passage states nothing about the quantity's source role;
- Conflict;
- Cx: a constructed row, not a corpus item.

**Scope test.**

- A status word counts for A3 only if its grammatical scope includes the quantity's source role: its
  entering the field equation, gravitating, or being a source.
- A status word scoped to the quantity's value, functional form, dependence or magnitude is recorded in
  **A3v**, the status of value or form, and does not enter A3.
- A status word attaches to what it modifies. The examples below fix the test.

**Word map**, drawn from AGENTS.md's status vocabulary (§A.25, §A.33), not from inventory phrasing:

- **D:** "derived", "proved", "theorem", "lemma", "corollary", "established", "shown", "follows from", "is
  a consequence of" a stated derivation.
- **D|cond:** a D word with "conditional on …" or "under …" naming conditions, or an inherited status note
  naming conditions.
- **Rq:** "requires", "is required", "must", "forced", "forces", "necessary".
- **Ps:** "proposal", "posit", "posited", "hypothesis", "reading", "taken as", "take … to", "assumed", "on
  the … proposal".
- **In:** "input", "imported", "taken from experiment", "fitted", "retrodiction".
- **ND:** "not derived", "not presently derived", "not established".
- **Op:** "open", "not settled", "undecided", "not adjudicated", "does not adjudicate", "conjecture".

**Inheritance.**

- If a passage carries no status word in scope, the status note of its enclosing subsection applies if
  that note's scope includes the source role.
- Every line read through this clause is listed at Q-2, as a cited line rather than a row.

**Aggregation per quantity.** Commitment values are D, D|cond, Rq and As. Hedge values are Ps, In, ND and
Op.

- If any row gives a commitment value and any row gives a hedge value, the value is Conflict, and the
  conflict is recorded as a finding.
- Otherwise, if any row gives a commitment value, the value is:
  - D|cond if any row gives D|cond, with the union of the named conditions;
  - else D or Rq, if any row gives one;
  - else As.
- Otherwise, the value is the hedge value or values given, or Ns if every row gives Ns.

**A3x.**

- Yes if the row's own passage is on §2.2's excluded list.
- Yes if the only stated ground for the row's status is a passage on that list.
- No otherwise.

**Examples outside the inventory.**

- "That radiation enters the Friedmann equation as a source is derived from the Einstein equation with the
  perfect-fluid stress tensor": D, with scope including the source role (TX-1).
- "The radiation density is derived from the Stefan–Boltzmann law": D in A3v; A3 is Ns (TX-2).
- "The scalar's gradient energy gravitates": As (TX-3).
- "We take the dark fluid to gravitate, with `w = −1`": Ps (TX-4).
- "Whether the axion background sources curvature is not settled here": Op (TX-5).
- "We require that the inflaton's potential be flat": Rq in A3v (scoped to the form); A3 is Ns.

### 5.4 A5g, a grounding commitment

**Values.**

- Yes: the corpus states that the quantity grounds the metric or the curvature;
- Rev: it states that the metric grounds the quantity;
- No;
- Und.

**Test.**

- ⊳_G vocabulary must relate the quantity, or its energy, to the metric or the curvature: "in virtue of",
  "grounds", "is what it is because of", "exists because of", "logically prior to".
- Sourcing vocabulary ("sources", "gravitates", "feeds back", "converts into curvature") is not ⊳_G
  vocabulary.
- These phrases count as sourcing or justificatory vocabulary, and so as No, unless both relata are
  quantities and the phrase has one of the ⊳_G forms above: "because", "due to", "arises from", "emerges
  from", "results from", "determined by", "a property of".
- Justificatory use, where a claim or identity is "grounded in" an argument, is not counted.
- Und if ⊳_G vocabulary occurs but its relata are not both quantities.
- The status of a Yes is read by §5.3, with "grounding" in place of "source role". The same commitment and
  hedge sets apply, As included (pending owner decision OQ-7).

**Examples outside the inventory.**

- "The field's energy is that in virtue of which spacetime curves": Yes (TX-11).
- "Matter tells spacetime how to curve": No (TX-11).
- "The theorem is grounded in Lemma 2": No (justificatory).

***

## 6. Derived cells and rejecting predicates

All derived cells are computed by the predicates below for every row. No predicate names a row. No U cell
and no class predicate reads A3.

### 6.1 Branches and routes

- **β0, §8.3 not in force.** The gravitating item's definiens is A2.
- **β1, §8.3 in force.**
  - For a quantity with A2§ filled, the definiens is A2§ mapped: fixed-cell → C; set-total → M;
    emergent-as-defined → M; not fixed → Und.
  - Otherwise A2.
- **Geometry-first statements.** A statement explicitly conditional on the geometry-first proposal
  (U1r5:504–505) enters β1 only. In β0 it is recorded, and it gives no role and no status.
- **Routes.** Where any row's role is recorded per route, derived cells are computed per route, 𝒞_div and
  Jacobson. Otherwise one value serves both routes.

### 6.2 U[v, b]: unrealizable under variant v on Reading G

| Condition | U[v, b] |
|---|---|
| The quantity is in `Dom(v)`; its definiens in branch b is M; and either A2t is closing, or A2t is slice-local and v's relata are synchronic | Y |
| The quantity is not in `Dom(v)`; or its definiens in branch b is C or X; or A2t is slice-local and v's relata are diachronic (F4-dia) | N |
| Otherwise: membership in `Dom(v)`, the definiens or A2t is Und | Und |

Y rests on Lemma U, general form, with N1–N3-G, N3′ (or the set-level reading) and N5-G [A], given those
premises.

### 6.3 Rejecting predicates

Commitment set: `Com` = {D, D|cond, Rq, As} (pending owner decision OQ-7).

- **Rejecting for an F4 variant v (b2)**, in branch b (and route, where §6.1 applies), iff all of:
  - A3 ∈ `Com`;
  - A3x = no;
  - U[v, b] = Y.
- **Potentially rejecting for v** iff not rejecting, and either:
  - A3 ∈ `Com` and U[v, b] = Und; or
  - A3 = Conflict and U[v, b] ∈ {Y, Und}.
- **Rejecting for a co-constraint formalization w** (F5, or F4[Δ] for the quantities in `class(Δ)`) iff
  all of:
  - A5g = Yes;
  - its grounding status ∈ `Com`;
  - A3x = no;
  - w denies grounding to the quantity.
- **Potentially rejecting for w:** as above, with A5g = Und, or with the grounding status Conflict.
- **Labels.**
  - A verdict whose only rejecting rows have A3 = As, or a grounding status of As, is labelled "rests on
    unqualified assertion".
  - A rejection resting on a D|cond row is conditional on that row's named conditions. They are carried
    into the verdict and into Stage 3.
- **Cx.** A row with A3 = Cx satisfies no rejecting or potentially rejecting predicate.

***

## 7. Carves: the grounding-relevance test

### 7.1 The test (GRT)

A carve Δ, with `class(Δ)` a predicate on §5 attributes, passes GRT iff all five conditions hold.

- **GRT-1 (a stated reason).** Either:
  - an inventory passage or the premise base gives a reason why items of one kind source, ground or are
    grounded in the metric while items of the other kind do not; or
  - it is derivable [A]/[P] from the non-excluded premise base that the two kinds differ in their ⊳_G
    relation to the metric, or in whether they are terms of the realized equation.
- **GRT-2 (K4).** The reason's premises are not on the excluded list (§2.2).
- **GRT-3 (K5).** The reason is not a difference of value, covariation or determination alone.
- **GRT-4 (K3, uniformity).** State the carve's reason as a claim R_Δ about every item in `class(Δ)`.
  - GRT-4 fails if some corpus row x (§4.2, Group K included) that is not on the excluded list satisfies
    (a) or (b), and no further difference passing GRT-1 to GRT-3 is stated for x:
    - (a) x is in `class(Δ)`, and a passage on x states, in its own vocabulary, the negation of what R_Δ
      states of x;
    - (b) x is outside `class(Δ)`, and a passage on x states of x what R_Δ states of the class.
  - GRT-4 is Und if (a) or (b) turns on an Und attribute.
  - It is never applied to W0 rows.
- **GRT-5 (no ad hoc edits).** `class(Δ)` is exactly the class the stated reason induces. No item is
  removed from it or added to it without its own GRT-passing reason.

A carve that fails GRT is rejected as a formalization (a failed control). A carve whose GRT is Und is
Undetermined (§8.1).

### 7.2 Candidate carves (fixed)

| Δ | Difference | `class(Δ)` (a predicate on §5 attributes) | Source of the candidate |
|---|---|---|---|
| Δ1 | partition-defined against not | A2p = yes | GR:581's stated ground |
| Δ2 | also stated as a consequence of the gravitational law against not | A1q = yes | GR:426 |
| Δ3 | integration-constant selection against input term; defines F4-law | A1 = IC | QB5(a)'s scope item; r5 F4-6 |
| Δ4 | uniform against non-vanishing null flux; defines F4-null | A1c = uniform | r5 F4-6 |
| Δ5 | metric-defined against not | A2 ∈ {M-geo, M-set, M-em, M-pure} | N3′; r5 F4-7 |
| Δ6 | relative against absolute | A2§ filled | §8.3; GR:569–577 |
| Δ7 | emergent against classical | A2 = M-em | GR:575 (excluded); GRT-2 decides |
| Δ8 | a functional of the metric alone, against a term with a non-metric argument | A2 = M-pure | F4's own statement (below) |
| Δ9.k | each reason enumerated at node Q-6a | a Boolean combination of §5 attributes, as committed at Q-6a | the inventory, closed by Q-6a |

- Membership is Und where a predicate's attribute is Und.
- Listing a candidate does not state that it passes or fails.
- **Δ8's candidacy.** F4's statement exempts the Einstein tensor, a functional of the metric alone, from
  grounding (r5 §3.4). Δ8 asks whether that exemption extends to other functionals of the metric alone.
  Its candidacy rests on F4's statement alone, and GRT decides it.
- **Closure, both ways.** Two negatives are used: "no carve passes GRT" (for R) and "no co-constraint
  formalization survives" (for (A)). Both are relative to the frozen inventory and to Δ1–Δ8 with the
  committed Δ9.k (pending owner decision OQ-2). Every verdict that uses either negative states that
  relativity.

***

## 8. Decision rule

### 8.1 Stage 2: verdicts per formalization

For each formalization of §3, in each branch (and route, where §6.1 applies):

- **Rejected:** at least one rejecting row (§6.3), or a failed control (K1–K5, or GRT for a carve).
- **Admissible:**
  - no rejecting and no potentially rejecting row;
  - K1–K5 green, and GRT passed for a carve.
- **Undetermined:**
  - otherwise: no rejecting row, but a potentially rejecting row or an undetermined control;
  - r5 R-5's clause applies: an undetermined formalization is neither admitted nor rejected.

K1–K5 are r5's (r5 §1.4), applied per formalization. K3 for a carve is GRT-4.

### 8.2 Stage 2: the summary class for F4

The summary class is computed per coordinate, from uniform F4 and every carve variant F4[Δ] (F4-law and
F4-null included). F4-dia and F5 are reported beside it.

| Class | Condition |
|---|---|
| **R**: F4 rejected on the corpus's own commitments | F4 Rejected; no carve variant Admissible; no carve variant Undetermined |
| **Cc**: an F4-c class specified | F4 Rejected; at least one carve variant Admissible |
| **C**: F4 compatible | F4 Admissible |
| **U**: undetermined | F4 Undetermined; or F4 Rejected, no carve variant Admissible, and at least one Undetermined |

- The conditions partition the cases [A].
- Every verdict states:
  - Reading G, case β and N5-G;
  - the coordinate;
  - the conditions of any D|cond row it rests on;
  - the "rests on unqualified assertion" label, where it applies;
  - the relativity of §7.2's closure.
- **QB7(a) sensitivity line (pending owner decision OQ-1).** If a Stage-2 verdict would differ were the
  A3 cells of the rows that the same-quantity table identifies with GR:376's `Λ_eff(H)`, or with GR:400
  Reading 1's quantity, non-committal, the verdict is reported with that sensitivity line, labelled "rests
  on the corpus text's commitment to running-vacuum sourcing (QB7(a))".

### 8.3 Stage 3: B_G's outcome

Stage 3 is written after the Stage-2 commit (X-7). It is computed for each cell of the grid: branch
{β0, β1} × route {𝒞_div, Jacobson} × W0 row {Z0, ZI, ZII}.

1. **Classify the W0 rows** by §5–§6, per route.
2. **Sort.** Each Admissible or Undetermined formalization v, F4-dia included, is sorted by its content
   with respect to the W0 quantity:
   - grounding-content if the quantity is in `Dom(v)`;
   - CoC-content if it is not;
   - Und if a W0 attribute that decides membership is Und.

   F5 is CoC-content.
3. **Apply r5's outcome rule** (r5 §1.2):
   - **(A)** at least one grounding-content formalization is Admissible, and no CoC-content formalization
     is Admissible or Undetermined;
   - **(B)** at least one CoC-content formalization is Admissible, and no grounding-content formalization
     is Admissible or Undetermined;
   - **(C)** otherwise. The residual is stated: both kinds remain, neither does, or an undetermined item
     decides.
4. **Robustness.** If an Und cell or an Undetermined formalization affects the result, compute the
   outcome under each resolution. If all resolutions agree, that outcome holds. Otherwise the outcome is
   (C), with the item named.
5. **Report the W0 rows' derived cells,** U[v, b] for each v, as for every row.

**Implications by Stage-2 class.** These are a reading aid; items 1–5 govern. Each is conditional on
Reading G, case β, N5-G and the coordinate. "Surviving" means Admissible or Undetermined.

| Stage-2 class | F5 | W0 quantity in `Dom(F4)` | B_G outcome |
|---|---|---|---|
| R | Admissible | either | (B), unless F4-dia survives and is grounding-content, in which case (C) |
| R | Rejected | either | (C), unless only F4-dia survives: then (A) if it is grounding-content, (B) if it is CoC-content |
| Cc | Admissible | either | (C) if some admissible carve keeps the W0 quantity in its domain; (B) if every admissible carve's class contains it and no grounding-content formalization survives |
| Cc | Rejected | either | (A) if every surviving formalization is grounding-content; (B) if every one is CoC-content; otherwise (C) |
| C | Admissible | yes | (C) |
| C | Admissible | no | F4 is CoC-content: (B) if no grounding-content formalization survives; otherwise (C) |
| C | Rejected | yes | (A) if no CoC-content formalization survives; otherwise (C) |
| C | Rejected | no | F4 is CoC-content: (B) if no grounding-content formalization survives; otherwise (C) |
| U | any | any | (C), with the deciding item named, unless the robustness step returns one outcome |

Where the table and items 1–5 disagree, items 1–5 apply, and the disagreement is recorded as a defect of
this preregistration.

### 8.4 The headline

- **The Stage-2 class** is reported per coordinate (branch, and route where §6.1 applies). If all
  coordinates agree, that class is the headline class. Otherwise the headline states "coordinate-
  dependent", with every class shown.
- **The B_G outcome** is reported for every cell of the grid: branch × route × W0 row.
- **The headline outcome** is X if every cell returns X. Otherwise it is (C), with the grid shown and the
  deciding coordinates named.
- **No coordinate is selected to break a disagreement.** β1 rests on the geometry-first posit, the route is
  not a premise, and no convention is preferred.

### 8.5 Properties of the rule [A]

- **(i)** (A) requires F5 to be Rejected: by a row with A5g = Yes and a grounding status in `Com`, or by a
  failed F5 control.
- **(ii)** A scope or carve variant with no stated reason is Rejected by GRT-1. This applies to F4-law and
  F4-null alike, and changes r5's treatment of F4-null, whose controls r5 left unassessed (pending owner
  decision OQ-2).
- **(iii)** F4 is Admissible only if no committed row in its domain has an Und decisive cell. Otherwise
  the class is at best U.
- **(iv)** (C) is the outcome in each case so listed in §8.3's table, and wherever §8.4's grid disagrees.
- **(v)** Sorting carves by the W0 quantity's membership (§3; pending owner decision OQ-3) has two mirror
  consequences:
  - if a carve whose class contains every metric-defined quantity passes GRT and is Admissible, (A) is
    unreachable for a metric-defined W0 quantity;
  - if a carve whose class excludes a metric-defined W0 quantity passes GRT and is Admissible, it is
    grounding-content and blocks (B) in the same way.

***

## 9. Hypothetical tables, one per class

These are constructed examples, not corpus readings. Each toy has its own premise base: Reading-G
analogues of N1–N3-G, N3′, transitivity and N5-G, and Lemma U in general form.

- K1–K5 are stipulated green for every toy formalization unless stated otherwise.
- `w*` is a constructed toy row with A3 = Cx.
- The toys have no K3 uses, so GRT-4 is satisfied vacuously where a toy carve is stated.
- Δ3 and Δ4 are tested by GRT like every carve. Where a toy states no reason for them, F4-law and F4-null
  are Rejected by GRT-1.
- F4-dia's verdict equals F4's in every toy, because every toy row has A2t closing, apart from flip X6.

Column key: Role (A1), Comp (A1c), Def (A2, A2t), St (A3), Gc (A5g), then U[F4], U[F4-law] and U[F4-null]
in branch β0. The toys have no A2§.

### 9.1 Class R (toy TC-R)

| Row | Role | Comp | Def | St | Gc | U[F4] | U[law] | U[null] |
|---|---|---|---|---|---|---|---|---|
| p1: the curvature-coupling term of a non-minimally coupled scalar, `ξ(G_μν φ² − ∇_μ∇_ν φ² + g_μν □φ²)` | T | full-tensor | M-geo (closing), with matter argument φ | D | No | Y | Y | Y |
| p2: dust | T | full-tensor | C | D | No | N | N | N |
| w* | T | full-tensor | M (closing) | Cx | No | Y | Y | Y |

- **Toy carves.** None stated.
- **Stage 2.** p1 is rejecting for F4, F4-law and F4-null. No carve is admissible. Class **R**. F5 is
  Admissible. F4-dia is Rejected.
- **Stage 3.** No grounding-content formalization survives, and F5 is CoC-content. Outcome **(B)**.

### 9.2 Class C (toy TC-N)

| Row | Role | Comp | Def | St | Gc | U[F4] | U[law] | U[null] |
|---|---|---|---|---|---|---|---|---|
| n1: dust | T | full-tensor | C | D | No | N | N | N |
| n2: a horizon-defined energy density | T | full-tensor | M-geo (closing) | Ps | No | Y | Y | Y |
| n3: Komar mass | Dep, A1q = yes | — | M | Ns (A3v: D) | No | N | N | N |
| n4: bare Λ | IC | uniform | X | Ps | No | N | N | N |
| w* | T | uniform | M (closing) | Cx | No | Y | Y | N |

- **Stage 2.**
  - No row is rejecting or potentially rejecting for F4: class **C**.
  - F4-law and F4-null are Rejected by GRT-1.
  - F5 is Admissible, and F4-dia is Admissible.
- **Stage 3.** F4 and F4-dia are grounding-content (w* is in `Dom(F4)`), and F5 is CoC-content. Outcome
  **(C)**.

### 9.3 Class Cc (toy TC-C)

| Row | Role | Comp | Def | St | Gc | U[F4] |
|---|---|---|---|---|---|---|
| c1: the `R`-term of `f(R)` gravity written as an effective stress tensor | T | full-tensor | M-pure (closing) | D | No | Y |
| c2: a horizon-defined thermal density with a matter-count argument | T | full-tensor | M-geo (closing) | Ps | No | Y |

- **Toy carve.** The toy premise base contains axiom Ax-κ: "a functional of the metric alone belongs to
  the geometric side and is not a term of the source content". Δκ is the toy's instance of Δ8, with
  `class(Δκ)` = {A2 = M-pure} = {c1}. Δκ passes GRT: GRT-1 by its second clause; GRT-4 vacuously.
- **Stage 2.**
  - F4 is Rejected by c1.
  - F4[Δκ] has no rejecting row (c2 is Ps) and is Admissible: class **Cc**.
  - F5 is Admissible. F4-dia is Rejected by c1.
- **Stage 3.**
  - If w* has a non-metric argument, it is outside `class(Δκ)`, and F4[Δκ] is grounding-content. With F5
    surviving as CoC-content, the outcome is **(C)**.
  - If w* is M-pure, F4[Δκ] is CoC-content, and no grounding-content formalization survives. The outcome
    is **(B)**.

### 9.4 Class U (toy TC-U)

| Row | Role | Comp | Def | St | Gc | U[F4] |
|---|---|---|---|---|---|---|
| u1: a source term with no stated definition | T | full-tensor | Und | D | No | Und |
| w* | T | full-tensor | M (closing) | Cx | No | Y |

- **Stage 2.** u1 is potentially rejecting, so F4 is Undetermined. Class **U**, with u1's A2 named.
- **Stage 3.**
  - Resolving u1 to M gives R. F5 is Admissible, so the outcome is (B).
  - Resolving u1 to C gives C. F4 is then grounding-content (w* is in its domain), F5 is Admissible, and
    the outcome is (C).
  - The resolutions disagree, so the outcome is **(C)**, with u1's A2 named.

### 9.5 The (A) route (toy TC-A)

| Row | Role | Comp | Def | St | Gc |
|---|---|---|---|---|---|
| a1: a fixed-cell vacuum energy, stated as "that in virtue of which the curvature is what it is" | T | uniform | C | D | Yes (D) |
| w* | T | uniform | M (closing) | Cx | No |

- **Stage 2.**
  - F4 has no rejecting row: class **C**.
  - F4-null is Rejected, both by a1 (it denies a uniform term grounding) and by GRT-1.
  - F5 is Rejected by a1.
  - F4-dia is Admissible.
- **Stage 3.** F4 and F4-dia are grounding-content with respect to w*. No CoC-content formalization
  survives. Outcome **(A)**.

Every Stage-2 class, and each of (A), (B) and (C), is reached by at least one table [A].

***

## 10. Controls

### 10.1 Rule-level controls

- The rule-level controls test the rule itself. Each has a required result.
- The reviewer runs them by hand at preregistration review. The executor re-runs them at node Q-0, before
  any inventory row is classified. The second reader of X-18 runs RC-T before classifying.
- A rule-level control that returns anything other than its required result, including Und, has failed.
- If any rule-level control fails, the rule is defective and execution halts. Only an amendment (§14.3)
  can resume it.
- A verdict printed over a failed or undetermined control is void.

### 10.2 RC-P (positive) and RC-N (negative)

- **RC-P.** TC-R (§9.1) must return class R, with F4, F4-law and F4-null each Rejected, and F5
  Admissible.
- **RC-N.** TC-N (§9.2) must return class C, with F5 Admissible.

### 10.3 RC-X (countercontrol against fitting)

Each flip changes one input. The class must change as stated, or, where stated, stay unchanged.

| Flip | From | To (required) |
|---|---|---|
| X1: TC-N, n2's A3 Ps → D | C | R (n2 rejecting; no toy carve) |
| X2: TC-R, p1's A2 M → C | R | C |
| X3: TC-A, a1's A5g Yes → No | F5 Rejected; (A) | F5 Admissible; (C) |
| X4: TC-C, Ax-κ removed | Cc | R |
| X5: TC-R, p1's role T → Dep | R | C |
| X6: TC-R, p1's A2t closing → slice-local | R | R (every main-table variant is synchronic). F4-dia: Rejected → Admissible |
| X7: TC-R, p1's A3x no → yes | R | C |
| X8: TC-R, p1's A3 D → Conflict | R | U |
| X9: TC-C, Ax-κ replaced by a toy axiom on the toy's excluded list | Cc | R (GRT-2) |
| X10: TC-C, Ax-κ replaced by "c1's value covaries with the toy curvature" | Cc | R (GRT-3) |
| X11: TC-N, n2's A3 Ps → As | C | R (pending owner decision OQ-7; under the fallback, U) |
| X12: TC-C, a toy row c3 that Ax-κ's reason covers (M-pure, T, Ps) is placed outside `class(Δκ)` | Cc | R (GRT-5) |

A rule that returns the same class on both sides of a flip that requires a change is insensitive to the
input that decides it, and RC-X fails.

### 10.4 RC-W (witness-tuning countercontrol; owner guidance)

- **W-a (relabelling).**
  - Toy TC-W has rows k1 and k2 with identical attribute vectors: T, full-tensor, M (closing), D, Gc No.
    k2 is tagged "the witness".
  - Required: identical derived cells, and every Stage-2 verdict unchanged when the tag moves to k1.
- **W-c (decoy carve).**
  - Δ† is either "the offset term is exempt from grounding" (a row-identity predicate), or "defined
    through a zero-point convention", an attribute L that the toy premise base does not relate to ⊳_G or
    to membership among terms.
  - Required: Δ† fails GRT (GRT-1 for both forms; GRT-5 for the row-identity form), and F4[Δ†] is Rejected
    as a failed control.
- **W-e (status-blindness of the predicates).**
  - Toy TC-M has rows m1 and m2 with identical attribute vectors except A3: m1 is D and m2 is Cx.
  - Required:
    - for every carve predicate Δ1–Δ8, and each Δ9.k once enumerated, m1 ∈ `class(Δ)` if and only if
      m2 ∈ `class(Δ)`;
    - for every v, U[v](m1) = U[v](m2);
    - m1 is rejecting for v exactly when U[v](m2) = Y.
  - The control fails if any carve predicate or U cell reads A3, a row's identity or the witness tag. It
    is re-run at node Q-6c, after the Δ9.k list is committed.
- **Cx-clause consistency checks (not countercontrols).** These follow from §6.3's Cx clause and are kept
  as consistency checks only.
  - **W-b.** In TC-R and TC-N, w* is varied over Role ∈ {T, IC, Dep}, Comp ∈ {full-tensor, uniform}, Def ∈
    {M, C, X, Und} and Gc ∈ {Yes, No}. The Stage-2 classes stay R and C.
  - **W-d.** A decoy selector S†, "adopt F4 if U[F4](w*) = Y, else F5", changes output under W-b's
    variation. The frozen rule's output does not.

### 10.5 RC-U (undetermined control; carried from r5 R-5)

- TC-U (§9.4) must return class U, with u1's A2 named, and Stage 3 must return (C) with it named.
- **TC-K.** TC-R with one added toy carve Δk, drawn on a toy attribute that p1 has and w* lacks (a
  predicate on attributes, not on rows), with Δk's GRT-4 stipulated Und. It must return:
  - F4[Δk] Undetermined;
  - class U;
  - (C) with GRT-4 (K3) named.

  The reason: if Δk passed, F4[Δk] would be Admissible and grounding-content with respect to w*, giving
  (C). If it failed, the class would be R, giving (B). The resolutions disagree.

### 10.6 Formalization-level controls

K1–K5 (r5 §1.4) are assessed per formalization at node Q-7, under r5 R-5's clause: a failed control
rejects; an undetermined one leaves the formalization neither admitted nor rejected.

### 10.7 RC-T (text controls; constructed sentences outside the inventory)

The executor (at Q-0) and the second reader (X-18) must both return the required values. Any miss halts
the unit as a rule defect.

| ID | Sentence | Required |
|---|---|---|
| TX-1 | "That radiation enters the Friedmann equation as a source is derived from the Einstein equation with the perfect-fluid stress tensor." | A1 T; A3 D |
| TX-2 | "The radiation density is derived from the Stefan–Boltzmann law." | D in A3v only; A3 Ns |
| TX-3 | "The scalar's gradient energy gravitates." | A1 T; A3 As |
| TX-4 | "We take the dark fluid to gravitate, with `w = −1`." | A1 T; A3 Ps |
| TX-5 | "Whether the axion background sources curvature is not settled here." | A3 Op |
| TX-6 | "`G_μν + Λ g_μν = 8πG T_μν`, with Λ a fixed constant." | Λ: A1 T, A1c uniform, A2 X, A1s left |
| TX-7 | "In unimodular gravity Λ is an integration constant." | A1 IC |
| TX-8 | "The number of field quanta beyond a uniformly accelerated observer's Rindler horizon." | A2 M-set; A2p yes |
| TX-9 | "Dust with rest-energy density `ρ = n m c²`." | A2 C (measure clause) |
| TX-10 | "The average energy density inside a static star's photon sphere: the total energy within it divided by its proper volume." | A2 M-geo; A2p no |
| TX-11 | "The field's energy is that in virtue of which spacetime curves." / "Matter tells spacetime how to curve." | A5g Yes / No |
| TX-12 | "In this model the electromagnetic helicity density does not source curvature." | A1 NS |
| TX-13 | "The Komar mass of the solution." | A1q yes; no role T |

***

## 11. Execution order (§A.31, depth-first)

| Node | Content | Output |
|---|---|---|
| Q-0 | Re-run RC-P, RC-N, RC-X, RC-W, RC-U and RC-T | all green, or halt |
| Q-1 | The same-quantity table (§4.1); **commit** | the table (X-19) |
| Q-2 | Classify every corpus row of §4.2, Group K included (A1–A5g), in table order. List the lines read through §5.3's inheritance clause | the audit table, corpus rows |
| Q-2b | The blind second reading of X-18, run by a different agent; reconcile once, by citation | reconciled cells, with residual disagreements Und |
| Q-3 | Q5, the G3 target: rows G-GR12, G-GR162, G-GR370, G-GR691, G-GR693, G-GR697, G-GR701, G-SM120, T-SM160, T-SM162 | {divergence-free sourcing law; null-flux route; both named as alternatives; not fixed}, with citations |
| Q-4 | Q3, F4's scope: the A1c of rows with role T and A3 ∈ `Com`; any stated reason for a scope (an input to Q-6a) | {full; null-flux; law-input; not fixed} |
| Q-5 | Q4, §8.3: GR:577's scope clause; A2§ for every relative or epoch-differential quantity | the clause's scope; the counterpart per quantity |
| Q-6a | Enumerate Δ9.k (below); **commit** before any GRT verdict | the Δ9.k list (X-19) |
| Q-6b | Q6: Δ1's predicate applied to every row; where T-GR384's quantity falls | the induced class, and T-GR384's position |
| Q-6c | GRT for Δ1–Δ8 and every Δ9.k; re-run W-e | pass, fail or Und per carve, with reasons |
| Q-7 | Stage 2: §6, §8.1 and §8.2; K1–K5 per formalization; the skeptical nodes; the QB7(a) sensitivity line; **commit** | verdicts and summary class per coordinate |
| Q-8 | Classify W0-Z0, W0-ZI and W0-ZII by §5–§6, per route; the second reader classifies them independently (X-18) | W0 rows |
| Q-9 | Stage 3 (§8.3) and the headline (§8.4) | the B_G grid and the headline |
| Q-10 | Fixed-point passes | NEW count per pass |

**Q-6a (enumeration, committed before any GRT verdict).**

- List every sentence of a §4.2 row that contains a reason connective ("because", "since", "therefore",
  "hence", "so", "in virtue of", "as a consequence", "is a property of … and therefore"), and whose
  conclusion is that a quantity does or does not source, gravitate, ground or enter the field equation.
- For each sentence, write the predicate it induces as a Boolean combination of §5's attributes.
- A predicate equal to one of Δ1–Δ8 is merged with it.
- A reason that cannot be written on §5's attributes is a deviation (§14.2), with a sensitivity line.
- The list lands in a commit before Q-6c.

**Skeptical nodes (§A.31).** A cell is favourable to the framework in one of two directions:

- **coexistence:** it keeps a corpus source term realizable under F4 (role Dep or NS rather than T;
  definiens C or X; a status outside `Com`; a carve passing GRT);
- **decoupling:** it makes F4, or a variant that is grounding-content with respect to a W0 row,
  Admissible.

For every cell whose flip changes a Stage-2 verdict and whose value is favourable in either direction, a
node states the strongest textual reading on which the cell takes the other value, and the cited ground
for rejecting it. If no such ground exists, the cell is Und. The record lists every verdict-changing cell
(X-20).

**Fixed point.** Passes continue until three consecutive passes yield no NEW finding (§A.31). If that is
not reached, the record says so.

***

## 12. Productivity test (§A.31), fixed in advance

**Baseline.** r5's residual (r5 §7; BG-F5, BG-F6):

- F4 against F5, with F4's scope not fixed by the premise base;
- F4-c's K3 undetermined;
- under §8.3, F4's treatment of epoch-differential pieces undetermined;
- the corpus stating no view on whether source terms ground.

r5's determinate verdicts also belong to the baseline:

- uniform F4 admissible;
- F5 admissible;
- partition-definedness and emergent-against-classical failing as F4-c candidates;
- consequence-of-the-law covering `ρ_s` only.

An item counts under (a) below only if it is absent from this list, or differs from it.

**Gem.** The unit is a gem iff it yields a fact strictly stronger than the baseline AND either:

- **(a) constrains:** at least one of the following is determinate and not in the baseline, or differs
  from it:
  - a Stage-2 verdict on uniform F4 or a variant;
  - F4's scope (Q3);
  - a carve passing or failing GRT;
  - a counterpart fixed (Q4);
  - the G3 target (Q5); or
- **(b) exposes a hidden assumption:** an assumption-watch marker not among AW-part, AW-metric,
  AW-entropic and AW-ground (r5 §9).

**Coherence check.** A completed table whose verdicts and Q3–Q5 outputs restate the baseline or are
undetermined, with no new marker, is recorded as a coherence check. A class-U result is a gem only
through (b), or through a determinate Q3–Q5 output not in the baseline. Findings are classed NEW,
POSITIVE, ELABORATING, CONFIRMING or BORDERLINE.

***

## 13. Invariant → checkpoint table (§A.41)

| ID | Invariant asserted of the execution | Checkpoint that measures it |
|---|---|---|
| X-1 | No computation on OI rules; reading and hand logic only | NOTES lists every command run; the reviewer confirms only read-only git and grep commands |
| X-2 | The corpus is read at `c3b5f37a` | Every quotation is checked verbatim against `git show c3b5f37a:<path>` by the reviewer. NOTES records `main`'s head at execution and any inventory line that changed |
| X-3 | The rule is frozen before analysis | F contains this file and no execution file, and the first execution file appears in a descendant of F. Checked from the branch history |
| X-4 | The inventory is closed | The decisive table's row IDs equal §4.2 ∪ §4.4. Any other row is `X-n`, in the deviations table only. The reviewer compares the ID lists |
| X-5 | I-SYM | (i) Every row, including T-GR352, T-GR577, Group K and the W0 rows, has every §5 column filled with a citation or Und. (ii) The reviewer checks every pair of rows with identical attribute vectors for identical derived cells. (iii) A grep of the Stage-2 text for `W0`, `w*`, `ρ_Z`, `K_cpl` and "witness" finds nothing; corpus row IDs may appear |
| X-6 | I-BLIND: inertness and fixed candidates | (i) RC-W green at Q-0, and W-e green again at Q-6c. (ii) No Stage-2 verdict cites a W0 row. (iii) Every carve is one of Δ1–Δ8, or a Δ9.k as committed at Q-6a |
| X-7 | Stage 2 precedes Stage 3 | The Stage-2 table and verdicts land in a commit whose tree has no W0 classification and no Stage-3 text. Stage 3 lands in a descendant. Checked from the history |
| X-8 | Controls are green before any verdict | The Q-0 record precedes the table in the record and in the history |
| X-9 | No excluded premise in a decisive step (K4) | Each decisive step lists its premises; the reviewer checks each against §2.2 |
| X-10 | Running-vacuum sourcing is not adopted (QB7(a)) | The running-channel rows have A3 rendered from cited corpus text. No decisive step cites the running-vacuum literature or an owner adoption. The §8.2 sensitivity line is present wherever it applies |
| X-11 | Status scope (§5.3) | The reviewer checks every A3 cell that decides a verdict, whatever its value, and every D, D|cond, Rq and As cell |
| X-12 | Conditions are carried | Every verdict line names Reading G, case β, N5-G, the coordinate, its D|cond conditions, any As label and the closure relativity |
| X-13 | Prior readings are not anchors | No cell cites r5's §2.4 reading column or node verdicts as its ground. Agreement with r5 is recorded in a separate column after rendering |
| X-14 | Corpus-wide negative statements have a search (§A.19) | Any sentence "the corpus states no …" cites its search patterns and hits in NOTES. Hits outside the inventory become `X-n` rows |
| X-15 | This preregistration states no outcome | The reviewer confirms that §4–§12 render no cell of an inventory row and state no expected class |
| X-16 | No manuscript change; paper-only; no premise adopted | `git diff --stat` on `papers/` and `book/` is empty across the unit's commits, and every decisive step's premise list (X-9) contains only §2.1 items |
| X-17 | Barred strings are absent | A grep of the unit's files for the barred path strings returns nothing |
| X-18 | The attribute cells do not depend on the executor's prior readings | After Q-2 and before the Stage-2 commit, a second reader classifies every A1, A1c, A1q, A2, A2t, A2p, A2§, A3, A3x and A5g cell of every §4.2 row from the frozen tests and the cited corpus lines only. The second reader is a different agent from the executor. It has not read r5 §0, §2.4 or §6–§9, CONFIRM-BG-r2 to r4, NOTES-BG-r1 to r5, or the executor's table, and it classifies the text controls first. Disagreements are reconciled once, by citation, and a cell still in disagreement is Und. The second reading lands in the Stage-2 commit, and the reviewer checks it is complete. At Q-8 the second reader classifies the W0 rows independently, from §4.4's definition sources, under the same reconciliation rule |
| X-19 | Enumerations precede their uses | The same-quantity table (Q-1) lands before any derived cell, and the Δ9.k list (Q-6a) lands before any GRT verdict. Checked from the history |
| X-20 | Skeptical-node completeness | The record lists every cell whose flip changes a Stage-2 verdict and gives a node for each favourable one. The reviewer recomputes the list by flipping cells |
| X-21 | Stage 3 and the headline are mechanical | The reviewer recomputes Stage 3 and §8.4's headline from the Stage-2 commit and the W0 rows |
| X-22 | The text controls are green | RC-T is green at Q-0 for the executor, and before Q-2b for the second reader |

***

## 14. Freeze, deviations and amendments

### 14.1 Before freeze

- Revisions are numbered r2, r3, …. Each is accompanied by a response file that lists every change and its
  trigger. Each is independently reviewed (QB6), in a full round wherever the tests or the decision rule
  change.
- A reviewer may propose rule text but must not state an expected outcome for the inventory.
- An owner answer to a pending OQ is applied by the alternative text of §15. It is reviewed by a check of
  that edit alone, unless it changes text outside the marked points of use.
- **Freeze F (pending owner decision OQ-5).** The owner designates F on #873, after the reviewer's
  acceptance is recorded. F is the commit containing the accepted revision.
- No inventory row is classified before F.

### 14.2 Deviations after freeze

- A deviation is any departure from this preregistration during execution:
  - a passage outside the inventory (`X-n`, §4.5);
  - a carve reason not expressible on §5's attributes (Q-6a);
  - a test that cannot be applied as written;
  - a moved inventory passage on `main`.
- Each is recorded in a deviations table, with its discovery node and a sensitivity line.
- A test that cannot be applied as written gives Und for the cell. No substitute test enters the decisive
  table. A substitute may be shown in the sensitivity line.
- A deviation never changes a rendered verdict.

### 14.3 Amendments after freeze

- An amendment is a separate file (`G3-QB5A-AMEND-n.md`). It states:
  - the change and its reason;
  - whether it was written before or after any Stage-2 cell was rendered;
  - which rendered verdicts it would affect.
- Every amendment after F needs independent review before it takes effect. One written after any Stage-2
  cell has been rendered also needs a recorded owner decision.
- The verdict as originally rendered stays beside the amended one.
- This preregistration is not edited after F.

***

## 15. Owner questions

The reviewer's recommended answers are applied in the text, marked "(pending owner decision OQ-n)". Each
alternative below can be applied as a minimal edit before freeze.

- **OQ-1. QB7(a)'s scope.**
  - **Applied (recommended).**
    - "Adopt" is read as taking the running-vacuum sourcing on by decision or by import.
    - The running-channel rows are classified from the corpus text by §5.3's test, as every row is.
    - §8.2's QB7(a) sensitivity line shows whether a verdict reaches QB7(a)'s subject through the text.
  - **Alternative.**
    - In §2.2, replace the running-vacuum bullet with: "The rows that the same-quantity table identifies
      with GR:376's `Λ_eff(H)` or with GR:400 Reading 1's quantity are not rejecting for any F4 variant,
      whatever their A3."
    - Delete §8.2's sensitivity line.
    - Note that this is a row-identity exemption in the form W-c rejects, and it departs from I-SYM.
- **OQ-2. GRT, Δ1–Δ8 with Δ9.k, and the relativity of both negatives.**
  - **Applied (recommended).**
    - GRT-1 to GRT-5 and the candidate list are accepted.
    - Both negatives are relative to the frozen inventory and list.
    - A scope variant with no stated reason is Rejected (§8.5 (ii)), which treats F4-law and F4-null alike
      and differs from r5.
  - **Alternative.**
    - Replace §8.5 (ii) with: "F4-law and F4-null are assessed without GRT-1, as restatements of F4's
      scope, and are Rejected only by a rejecting row or by K1–K5."
    - In §3, mark their domains "not subject to GRT".
- **OQ-3. Counting carves that contain the witness's term.**
  - **Applied (recommended).** Such an admissible carve is CoC-content (§3). Both mirror consequences are
    stated (§8.5 (v)).
  - **Alternative.**
    - In §3, replace the sorting bullets with: "An admissible F4[Δ] whose class contains the witness's term
      is reported, and is not counted on either side at Stage 3."
    - In §8.5 (v), delete the first consequence.
- **OQ-4. The inventory.**
  - **Applied (recommended).** Groups S, V, Q, C and K, with QR-15's additions (C-GR418, E-GR571,
    G-GR701, G-GR693 and T-GR695), and the search recorded in NOTES-QB5A-r2 §5.
  - **Alternative.** Delete the rows the owner names. Each deletion is recorded as an exclusion, with its
    reason, in NOTES.
- **OQ-5. Freeze designation.**
  - **Applied (recommended).** The owner designates F on #873 after the reviewer's acceptance is recorded
    (§14.1).
  - **Alternative.** Replace §14.1's freeze bullet with: "F is the commit containing the accepted
    revision; the reviewer's recorded acceptance designates it."
- **OQ-6.** Answered by #873 c.6872277416 (`amaybaum`, 2026-11-14T05:17:28Z).
- **OQ-7. Does an unqualified assertion in the corpus's own voice count as a commitment?**
  - **Applied (recommended).** Yes, on both the sourcing side (F4) and the grounding side (F5). `Com`
    includes As (§6.3), and a verdict resting only on As rows is labelled.
  - **Alternative (fallback).** As makes a row potentially rejecting, never non-rejecting.
    - In §6.3, set `Com` = {D, D|cond, Rq}.
    - Add to both potentially rejecting predicates: "or A3 (respectively the grounding status) = As and
      U[v, b] ∈ {Y, Und} (respectively, the other conditions hold)".
    - In §10.3, X11 then requires C → U.

***

## 16. Limits

- The rule is preregistered. Its controls are hand-checked on constructed examples only.
- Every verdict is conditional on Reading G, case β and N5-G. In case α (r5 node B2), Lemma U does not
  apply and B_G is idle.
- The §8.3 branch rests on the geometry-first identification (U1r5:504–505).
- The negatives used by R and (A) are relative to the frozen inventory and the candidate list.
- (A) requires an explicit grounding commitment or a failed F5 control (§8.5 (i)).
- The witness keeps unit 2(a)'s scope: exact de Sitter and M1.
- No claim is made about K_cpl^conv's admissibility under G3, or about Λ.
