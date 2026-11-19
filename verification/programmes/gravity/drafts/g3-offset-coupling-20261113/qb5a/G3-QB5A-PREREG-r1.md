# G3 QB5(a) (preregistration r1): the framework's own source terms against F4

**Scope.** This is the preregistration of a paper-only audit under Issue #873, continuing unit 2(b)
(PR #1275). It fixes the question, premises, inventory, classification scheme, decision rule, controls and
outcome classes before any source is read for the answer. It contains no analysis of an inventory
passage, renders no cell of the audit table and states no expected outcome.

- **Authorization.** #873 comment 6872004336 (`amaybaum`, 2026-11-14):
  - "QB5 | Authorize (a) — the F4-versus-F5 source audit, paper-only."
  - "QB6 | … Freeze and independently review the next unit's rule before analysis."
  - "The next investigation must test the framework's own gravitational source terms against F4, rather
    than selecting F4 merely because it excludes an unwanted coupling."
  - "The QB5(a) investigation may proceed once its decision rule passes independent preregistration
    review."
  - "QB7(a) | Do not adopt running-vacuum sourcing as a premise. QB7(b) | Leave the gravitating
    counterpart open for the QB5(a) investigation."
- **Owner guidance, 2026-11-14** (`amaybaum`, relayed by the coordinating session; see NOTES-QB5A-r1 §2
  for its record status): "The decision rule must apply equally to the corpus's own metric-dependent
  source terms and the disputed vacuum-offset coupling, without selecting F4 or F5 to obtain a preferred
  result." It is built in as invariant I-SYM (§1.3) and countercontrol RC-W (§10.4).
- **Inputs** on branch `research/g3-offset-873-20261113` at `8d661a649`, directory
  `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/`:
  - `G3-UNIT2B-BG-r5.md` ("r5:n"), with `CONFIRM-BG-r3.md` and `CONFIRM-BG-r4.md`;
  - `G3-UNIT2A-r3.md` ("U2Ar3:n") and `G3-UNIT1-r5.md` ("U1r5:n").

  These are reviewed research drafts on a branch, not established results on `main` (§A.46 item 7).
  Each is used below only for a definition or a stated, reviewed inference, and is cited where used.
- This preregistration runs no computation on OI rules, changes no manuscript, adopts no premise and
  makes no claim about Λ.

**Source snapshot.** `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`, the snapshot of units 1, 2(a)
and 2(b). Every corpus `file:line` refers to that commit. The executor records whether `main` has moved
at execution time (checkpoint X-2); a changed inventory passage is a deviation (§14.2), and the audit
still reads the pinned snapshot.

**Support labels**, as in r5: [K] kernel-checked declaration on `main`; [A] exact algebra or elementary
logic, by hand; [P] a paper derivation or a reading of a paper statement; [L, recalled] literature recalled
and not re-read, on which no verdict rests. **Conditional** marks a claim that holds only under the
hypotheses it names.

**Terms carried from r5 and unit 2(a).** ⊳_G (order of grounding), ⊳_D (order of determination), N1–N3
in ⊳_G, N3′, N5-G, Reading G, case β, the witness, B_G, F3, F4, F4-null, F4-c, F5, Lemma U, K1–K5, and
the content classes "grounding-content" and "CoC-content" relative to the witness's term (r5:36–48,
r5 §1–§3). The witness's term is written `ρ_Z` (U1r5:222–225; U2Ar3:315–342).

***

## 0. Summary

- **Question (§1).** Taken on the corpus's own sourcing commitments, is F4 consistent with the
  corpus, and in which scope? Is there a specified F4-c class? Is F5 consistent with it? The same
  classification and the same F4 and F5 tests are applied to every corpus source term and to the
  disputed vacuum-offset terms, the corpus's own offset (GR:352) and the witness's `ρ_Z`.
- **Stages.** Stage 2 renders a verdict for each formalization from the audit table. Stage 3 maps those
  verdicts to B_G's outcome (A), (B) or (C). Stage 2 is recorded in a commit before Stage 3 is written.
- **Stage-2 classes for F4 (§8.2).**
  - **R**: F4 rejected on the corpus's own commitments.
  - **Cc**: uniform F4 rejected, and an F4-c class specified that passes the grounding-relevance test
    and K1–K5.
  - **C**: F4 compatible with the corpus's commitments.
  - **U**: undetermined, with the deciding cell or control named.
- **Controls (§10).**
  - RC-P (positive): must return R.
  - RC-N (negative): must return C.
  - RC-X (countercontrol): opposite inputs must return different classes.
  - RC-W (witness-tuning countercontrol): must detect a rule that consults the witness.
  - RC-U (undetermined control): carried from r5 R-5.

  All five are defined on constructed examples.
- **Owner questions (§15).** Six, OQ-1 to OQ-6. OQ-1 to OQ-4 must be answered before freeze.

***

## 1. The question

### 1.1 Statement

Let F4 be r5's formalization (r5 §1.3, §3.4): the boundary law is not fundamental; the energy content of
every term of the realized equation other than the Einstein tensor grounds the realized metric. Let its
variants be those of §3.

**Q.** On Reading G, case β, conditional on N5-G, and on the premise base of §2:

- **Q1.** Does some term that the corpus holds as derived or required in a source role become
  unrealizable under F4, or under a given F4 variant, with no carve-out that has a difference relevant
  to grounding?
- **Q2.** Does the corpus commit, in grounding vocabulary, to some term grounding the metric, which F5
  or a co-constraint variant denies?
- **Q3.** Which scope of F4 do the corpus's sourcing statements fix, if any?
- **Q4.** Does the corpus fix the classical counterpart of an epoch-differential piece under §8.3, and
  what is GR:577's scope clause?
- **Q5.** Is the G3 target the corpus names (GR:12) a divergence-free sourcing law or a null-flux
  route?
- **Q6.** Where does GR:581's ground for non-sourcing fall against GR:384?

Q1 and Q2 decide the Stage-2 verdicts. Q3 to Q6 supply cells and candidate carves to Q1 and Q2 (§11).

### 1.2 What the question is not

The audit does not ask whether F4 excludes the witness. That was r5's result, conditional on F4 (r5 §3.4).
F4 is accepted or rejected here on the corpus's own sourcing commitments. That F4 excludes the witness,
or does not, is no reason for either verdict.

### 1.3 Blindness and symmetry

Two requirements, kept apart.

- **I-SYM (symmetry; owner guidance, 2026-11-14).**
  - Every row of the audit table receives the same attributes (§5) by the same operational tests. This
    includes the corpus's metric-dependent source terms, the corpus's vacuum-offset term (GR:352) and
    the witness rows W0-Z0, W0-ZI and W0-ZII (§4.4).
  - The derived cells (§6) are computed by the same predicates for every row.
  - Every clause of the decision rule (§8) and every carve (§7) is a predicate on attribute values. None
    names a row.
  - Consequence: two rows with identical attribute vectors receive identical derived cells and the
    same treatment in every verdict.
- **I-BLIND (no fitting to the witness).** The choice between F4 and F5, of an F4 scope, or of an F4-c
  class is not made by reading what it does to the witness. It is enforced in four ways.
  1. **Fixed candidate space.** The formalizations (§3) and candidate carves Δ1–Δ9 (§7.2) are fixed
     here, before any row is classified. A carve proposed during execution is a deviation (§14.2), and
     its justification may cite no attribute of a W0 row.
  2. **Reason-based carves.** A carve is admitted only through the grounding-relevance test (§7.1),
     which requires a stated reason tied to grounding and applied uniformly.
  3. **Inertness of constructed rows.** A row's stated status is read from the corpus. A constructed row
     has status Cx, and the rejecting predicates (§6.3) never fire on status Cx. The witness rows
     therefore cannot move a Stage-2 verdict. This is a consequence of I-SYM's uniform predicates, not a
     special case, and RC-W (§10.4) tests it.
  4. **Stage order.** The Stage-2 table and verdicts land in a commit before the W0 rows are classified
     and before any Stage-3 text exists (checkpoint X-7). Stage 3 is a mechanical mapping (§8.3) that
     cannot change a Stage-2 verdict.

***

## 2. Premise base and excluded list

### 2.1 Premise base (carried from r5 §1.1 and §3.1)

- **The corpus's stated premises:** the text at `c3b5f37a`, as cited, with its stated status.
- **Reading G's premises:**
  - N1–N2-G: GR:40; GR:346 s.1–s.2;
  - N3-G: GR:342's second clause "QM is emergent"; GR:344;
  - transitivity of ⊳_G;
  - N5-G, labelled as not stated in the corpus (U2Ar3:226–231).
- **N3′** (r5 §2.2): a quantity defined as a function of another is grounded in it [P; L, recalled].
  Covariation without definition is ⊳_D only (K5).
- **Lemma U, general form** (r5 §3.1) [A] given these premises: a law term grounded in the realized
  metric does not ground that metric. Only the general statement is used. Its application to the
  witness, and Corollary E (r5 §3.2), do not enter Stage 2.
- **The set-level reading** (r5 node F4-7; reviewed as sound in CONFIRM-BG-r3 §4) [P]: a count, total or
  density over a partition-selected set is grounded in the set's membership, and through N1–N2-G in the
  metric.
- **The diachronic reading** (r5 node F4-3) [P]: with a slice-local partition and diachronic relata, the
  cycle does not close.
- **P-D** (r5 §3.3): Main:44, Main:54, Structure.md:136. F3 is carried as rejected by (b2), and is not
  re-audited.

### 2.2 Excluded as premises

These are carried from r5 §1.1 and extended. Each may be quoted as vocabulary, but none is the premise of
a decisive step (K4).

- From r5:
  - B_G and its negation;
  - (ii-W), (ii-L), (ii-S) and (ii-G) as exclusions;
  - GR:342 "This ordering is forced …" and "not the reverse";
  - GR:346 s.4;
  - book/ch07-gravity.md:187;
  - GR:340 s.1's ordering clause;
  - GR:340 s.2 (P11);
  - GR:575's clause "What does not gravitate";
  - any form of the boundary law, its derivation, or its non-derivability (G3);
  - the separation clauses of Substratum.md:385–389, and GR:655's clause.
- **Added here.**
  - **Running-vacuum sourcing (QB7(a)).** The sourcing of the running-vacuum channel (GR:374–380;
    GR:400 Reading 1) is not adopted by owner decision and is not imported from the running-vacuum
    literature. Its corpus status is read from the text by the same test as every other row (§5.3),
    subject to OQ-1.
  - **F4, F5 and every variant** are assessed, never used as premises.
  - **Prior verdicts.**
    - r5's outcome (C) and its residual statement.
    - r5's "Reading [P]" column (r5 §2.4) and its node verdicts on the inventory's passages. The audit
      derives each cell from the text by the tests of §5–§6. r5's readings may be cited only after a cell
      is rendered, to record agreement or disagreement.
  - **The G3 route as a premise.** Q5 records what the corpus names as its target. No step takes a form
    of the boundary law as a premise. Where a W0 attribute depends on the route, Stage 3 is computed per
    route (§8.3).

***

## 3. Formalizations assessed

Each formalization is an F4 variant with a grounding domain `Dom(v)`, or a co-constraint formalization.
The variants are fixed here.

| ID | Statement | `Dom(v)` (the quantities whose energy content grounds the metric) |
|---|---|---|
| F4 | r5 §3.4, as stated | every quantity with role T or IC (§5.1), whatever its component |
| F4-law | F4 restricted to the law's input terms (QB5(a) "law terms"); ≡ F4[Δ3] | role T |
| F4-null | F4 restricted to the null-flux source (r5 F4-6); ≡ F4[Δ4] | role T or IC with a non-vanishing null–null component |
| F4[Δi] | F4 with the class of carve Δi not grounding (§7.2) | `Dom(F4)` minus `class(Δi)` |
| F5 | co-constraint, regularity view (r5 §1.3) | empty: no law term grounds the metric |
| F3 | fundamental governing law | carried, rejected by (b2) (r5 §3.3) |

- F4-c, in r5's sense, is any F4[Δi] that is admissible and whose class does not contain the witness's
  term. That sorting is done at Stage 3 (§8.3), never at Stage 2.
- An F4[Δi] whose class contains the witness's term is CoC-content with respect to it, as r5 R-6 classes
  F4-null. It is counted on that side at Stage 3 (OQ-3).

***

## 4. The inventory (closed)

### 4.1 Unit of classification

- A **row** is one inventory passage. A **quantity** is a gravitational term the passage names.
- When a passage names several quantities, each is classified separately (row IDs with a suffix, for
  example T-GR400·R1).
- Two rows concern the **same quantity** when they use the same symbol, or when one explicitly
  cross-references the other (a section reference or "the identity above"). The executor records the
  identification table before rendering any derived cell.
- Every row is classified by §5. A row that names no gravitational quantity receives role N, and its
  derived cells are "—".

### 4.2 Corpus rows (`c3b5f37a`)

**Group S: source-term passages, QB5(a)'s list.**

| Row | Passage | Content located (not evaluated) |
|---|---|---|
| T-GR374 | GR:374 | emergent vacuum energy "a state-level quantity depending on the hidden sector's volume"; the "requires some state dependence" sentence |
| T-GR376 | GR:376 | the display of `Λ_eff(H)` |
| T-GR378 | GR:378 | the three architectural commitments (i)–(iii); `A = 4πc²/H²` |
| T-GR380 | GR:380 | the Type II identification; running `G`; the Bianchi identity |
| T-GR384 | GR:384 | the `ρ_s(H) = ρ_crit(H)` bullet; "total gravitating boundary energy" |
| T-GR422 | GR:422 | Corollary step (i), the total effective density: definitions of `ρ_s` |
| T-GR424 | GR:424 | the display of `ρ_s` |
| T-GR426 | GR:426 | the identity as "a consequence of Jacobson's Clausius relation applied to the de Sitter horizon" |
| T-GR400 | GR:400 | the Remark: Reading 1 (·R1) and Reading 2 (·R2) |
| T-GR528 | GR:528 | the CMB paragraph: "non-oscillating gravitational source"; entropy displacement |
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

**Group V: the corpus's vacuum-offset coupling (owner guidance).**

| Row | Passage | Content located |
|---|---|---|
| T-GR352 | GR:352 | the two completions, `𝒢 = 8πG T^cl` and `𝒢 = 8πG(T^cl − ρ_C g)`; "a coupling theorem" |
| T-GR577 | GR:577 | the reconstruction-gauge form; "Whether the offset sources curvature is not settled"; the scope clause (also Q4) |

**Group Q: rows for Q3 to Q6.**

| Row | Passage | Serves |
|---|---|---|
| G-GR12 | GR:12 | Q5: "the decisive Level-G3 target … is a covariant equation"; the displayed target form |
| G-GR162 | GR:162 | Q5: "the covariant field equations remain the Level-G3 target"; Jacobson used, not derived |
| G-GR370 | GR:370 | Q5: "the covariant Level-G3 target, open" |
| G-GR691 | GR:691 | Q5: the derivations' use of Einstein dynamics through Jacobson's relation |
| G-GR697 | GR:697 | Q5: item (ii), "The full nonlinear `G_μν = 8πG T_μν` … not established" |
| E-GR569 | GR:569 | Q4: relative effects; the absolute zero-point sum |
| E-GR573 | GR:573 | Q4: "What gravitates"; the classical microstate difference |
| E-GR575 | GR:575 | Q4: vocabulary only (excluded as a premise, §2.2) |
| E-GR579 | GR:579 | Q4: "The principle is uniform …" |

**Group C: context rows (drafting additions, OQ-4).** These are read to fill attributes of the rows
above for the same quantities. They are classified like every row.

| Row | Passage | Reason for inclusion |
|---|---|---|
| C-GR354 | GR:354 | stated status of the Type II channel (r5 F4-8) |
| C-GR358 | GR:358 | "feed back … through state-level quantities" (r5 K3 list) |
| C-GR382 | GR:382, :385–386 | the companion bullets of GR:384 |
| C-GR388 | GR:388, :398 | magnitude: the emergent-QFT channel and the substratum mode count |
| C-GR428 | GR:428–434 | the Corollary's clarifications on `ρ_s` (classical; physical locus; equivalence) |
| C-GR444 | GR:444–452 | Corollary steps (ii-a), (ii-b) and (iii): `ρ_s` "gravitationally active (because …)" |
| C-GR474 | GR:474 | Step 2's conversion of the entropy gradient |
| T-GR482 | GR:482 | "The Jacobson mechanism converts the entropy gradient into curvature" (r5 K3; AW-entropic) |
| C-GR532 | GR:532 | "the Jacobson sourcing is spatially local" |
| C-GR633 | GR:633 | "The Type II running-vacuum functional form is not derived" |
| C-SM164 | SM:164 | the continuation of SM:162: the correction term |

### 4.3 K3 corpus uses (carried from r5 K3)

GR:340, GR:342, GR:346, Substratum.md:385–393, GR:162, SM:160–162, GR:374–380, GR:384, GR:400 Reading 1,
GR:482 and GR:528–530. These are the uses against which a carve's uniformity is checked (GRT-4, §7.1).
Those not already rows are read for K3 only.

### 4.4 Constructed rows (status Cx)

| Row | Definition source | Note |
|---|---|---|
| W0-Z0 | `ρ_0` (U2Ar3:322–323), in K_cpl^conv[Z_0] (U2Ar3:340–342) | GR:362's density as written |
| W0-ZI | `ρ_I` (U2Ar3:324–325) | constructed IR limit |
| W0-ZII | `ρ_II` (U2Ar3:326–330) | unit 1's literal form |

- The convention map `Z` is defined at U1r5:222–225.
- W0 rows are classified by the same tests (§5–§6), at the point fixed by §11 (node Q-8).
- Their role attribute is computed per route, 𝒞_div (U1r5:198–204) and the Jacobson route (U1r5:603–606),
  because the route is not a premise (§2.2).

### 4.5 Rule for passages found later

- A passage not listed in §4.2–§4.4 that is found during execution is recorded as a deviation row
  `X-n` (§14.2). It is classified by the same scheme.
- It does not enter the decisive table. The Stage-2 verdict is rendered on the frozen inventory.
- The record states whether the verdict would differ if the row were included (a sensitivity line).
- An X-row changes a verdict already rendered only through an amendment (§14.3), and the verdict as
  rendered stays reported beside the amended one.
- This holds whether the passage is found before or after rendering.

***

## 5. Per-row attributes

Each attribute has values, an operational test and an example from outside the inventory. Every cell
cites the line or lines it rests on. A cell that the tests cannot fix from the cited text is "Und".

### 5.1 A1, role in the law

- **Values.**
  - T: a term of a field equation, as a source.
  - IC: an integration constant, or the datum that selects one.
  - Dep: a dependence on geometry is stated, with no role in a field equation.
  - N: no gravitational quantity.
  - Und.
- **Sub-attribute A1q.** Is the quantity also stated as a consequence of a law or relation applied to a
  given solution? Yes or no.
- **Sub-attribute A1c, component.**
  - full (general symmetric tensor or energy density);
  - uniform (∝ `g_μν`);
  - null-flux (only `T_μν k^μ k^ν` enters);
  - unstated.
- **Test.**
  - T if a passage on the quantity places it on the source side of a displayed or verbally stated field
    equation, or says it "sources", "is a (gravitational) source" or "source term", "gravitates", "is
    gravitationally active", "feeds back as a source", or is converted "into curvature".
  - IC if it is called an integration constant or the datum that fixes one.
  - Dep if only a dependence ("depends on", "inherits an `H`-dependence") is stated.
  - Role is aggregated per quantity: T if any row on the quantity gives T; otherwise IC; otherwise Dep.
  - A1q records consequence statements separately. A consequence statement does not remove role T. Its
    bearing on grounding is tested as carve Δ2 (§7.2).
- **Examples, outside the inventory.**
  - In textbook GR, the perfect-fluid `T_μν` in `G_μν = 8πG T_μν` is T, full.
  - The Komar mass of a Schwarzschild solution, computed from the solution, has A1q = yes and no role T.
  - In unimodular gravity, Λ is IC.
  - "The black hole's entropy depends on its area" is Dep.

### 5.2 A2, definiens (the N3′ test)

- **Values.**
  - M: defined as a function of the metric, directly or through a metric-defined item. Record the
    subtype:
    - M-geo: curvature, `H`, a horizon area or radius, a horizon temperature, a metric volume;
    - M-set: a count, total or density over a partition-selected set (F4-7);
    - M-em: an emergent computation from the class at the realized partition;
    - M-pure: a functional of the metric alone.
  - C: defined on the microstate of cells fixed independently of the metric.
  - X: a constant or convention with no metric input.
  - Und: no definition is stated in the inventory or the premise base.
- **Test.**
  - Write the defining expression as the corpus states it, with its citation.
  - The value is M if any argument is the metric or an item whose definition takes the metric, including
    the partition Π(g) of GR:40 in case β.
  - A value that covaries with `H`, with no definition through the metric, is not M (K5); record the
    covariation in A3v.
- **Sub-attribute A2t, cycle.**
  - closing: the dependence is on the same realized metric, or on a global structure such as an event
    horizon or a global Killing structure;
  - slice-local: defined from a slice's metric, with diachronic relata (F4-3);
  - Und.
- **Sub-attribute A2§, §8.3 counterpart.** It is filled only for quantities the corpus states as relative
  or epoch-differential (the words "relative", "difference", "epoch-differential" applied to the
  quantity). Values:
  - fixed-cell: a microstate difference on cells specified independently of the partition is named;
  - set-total: a total over the hidden sector or a partition-selected set is named;
  - emergent-as-defined: the emergent computation is named, with no relocation;
  - not fixed: no classical item is named for this quantity.
- **Examples, outside the inventory.**
  - The Hawking temperature `κ/2π` is M-geo.
  - The number of quanta inside a black-hole horizon is M-set.
  - The Ricci scalar term of `f(R)` gravity written as an effective stress tensor is M-pure.
  - The rest energy of an electron is C.
  - A fixed bare cosmological constant is X.
  - For A2§: "the electron/no-electron energy difference corresponds to a difference in the electron's
    own cells" is fixed-cell; "the difference in total radiation energy inside the Hubble volume" is
    set-total.

### 5.3 A3, stated status of the sourcing role

- **Values.**
  - D: derived, or D|cond, derived conditional on named conditions;
  - Rq: required;
  - Ps: posited, a proposal or a reading;
  - In: an input or imported;
  - ND: stated not derived;
  - Op: open, not settled, or not adjudicated;
  - Ns: none stated;
  - Conflict: rows on the same quantity give incompatible statuses;
  - Cx: a constructed row, not a corpus item.
- **Scope test (decisive).** A status word counts for A3 only if its grammatical scope includes the
  quantity's source role: its entering the field equation, gravitating, or being a source. A status word
  scoped to the quantity's value, functional form, dependence or magnitude is recorded in **A3v** (the
  status of value or form) and does not enter A3.
- **Word map.**
  - D: "derived", "follows from", "is a consequence of" a stated derivation, "theorem", "proved".
  - D|cond: D with "conditional on …" or a section status note naming conditions.
  - Rq: "requires", "is required", "must", "forces".
  - Ps: "proposal", "posit", "reading", "structural reading", "on the … proposal", "taken as".
  - In: "input", "imported".
  - ND: "not derived", "not presently derived".
  - Op: "open", "not settled", "does not adjudicate".
- **Inheritance.** If the passage carries no status word in scope, the status note of its enclosing
  subsection applies if that note's scope includes the source role. Cite it.
- **Aggregation.** If two rows on one quantity give statuses that differ in whether the source role is
  held (D or Rq against Ps, In, ND or Op), the value is Conflict, and the conflict is recorded as a
  finding.
- **Sub-attribute A3x.** Yes if the only stated ground for the row's status is a passage on the excluded
  list (§2.2).
- **Examples, outside the inventory.**
  - "Radiation pressure in the Friedmann equation is derived from the Stefan–Boltzmann law": D, scope
    includes the source role.
  - "We require that the inflaton's potential be flat": Rq, but scoped to the form (A3v), not to sourcing.
  - "Dark energy is modelled as a fluid with `w = −1`": Ps.
  - "The value of `G` is taken from experiment": In, scoped to the value (A3v).

### 5.4 A5g, grounding commitment

- **Values.**
  - Yes: the corpus states that the quantity grounds the metric or curvature;
  - Rev: it states that the metric grounds the quantity;
  - No;
  - Und.
- **Test.**
  - ⊳_G vocabulary must relate the quantity, or its energy, to the metric or curvature: "in virtue of",
    "grounds", "is what it is because of", "exists because of", "logically prior to".
  - Sourcing vocabulary ("sources", "gravitates", "feeds back", "converts into curvature") is not ⊳_G
    vocabulary (r5 §2.4).
  - Justificatory use, where a claim or identity is "grounded in" an argument, is not counted.
  - Und if ⊳_G vocabulary occurs but its relata are not both quantities.
  - The status of a Yes is read by §5.3 with "grounding" in place of "source role".
- **Examples, outside the inventory.**
  - "The field's energy is that in virtue of which spacetime curves": Yes.
  - "Matter tells spacetime how to curve": No (sourcing vocabulary).
  - "The theorem is grounded in Lemma 2": No (justificatory).

***

## 6. Derived cells and rejecting predicates

All derived cells are computed by the predicates below for every row. No predicate names a row.

### 6.1 Branches

The §8.3 relocation is a posit of the geometry-first proposal (U1r5:504–505), so every derived cell is
computed in two branches.

- **β0** (§8.3 not in force). The gravitating item's definiens is A2.
- **β1** (§8.3 in force).
  - For a quantity with A2§ filled, the definiens is A2§ mapped: fixed-cell → C; set-total → M;
    emergent-as-defined → M; not fixed → Und.
  - For any other quantity, A2 applies.

### 6.2 U[v, b]: unrealizable under variant v on Reading G

| Condition | U[v, b] |
|---|---|
| The quantity is in `Dom(v)`, its definiens in branch b is M, and A2t is closing | Y |
| The quantity is not in `Dom(v)`, or its definiens in branch b is C or X, or A2t is slice-local | N |
| Otherwise (membership in `Dom(v)`, the definiens or A2t is Und) | Und |

Y rests on Lemma U, general form, with N1–N3-G, N3′ (or the set-level reading) and N5-G [A] given those
premises.

### 6.3 Rejecting predicates

- **Rejecting for an F4 variant v (b2).** A row is rejecting for v in branch b iff:
  - A3 ∈ {D, D|cond, Rq};
  - A3x = no;
  - U[v, b] = Y.
- **Potentially rejecting for v.** A row is potentially rejecting iff it is not rejecting and either:
  - A3 ∈ {D, D|cond, Rq} and U[v, b] = Und; or
  - A3 = Conflict and U[v, b] ∈ {Y, Und}.
- **Rejecting for a co-constraint formalization w (F5, or an F4[Δ] for the rows in its class).** A row
  is rejecting for w iff:
  - A5g = Yes;
  - its grounding status ∈ {D, D|cond, Rq};
  - A3x = no;
  - w denies grounding to the quantity.
- **Potentially rejecting for w.** As above, with A5g = Und, or with the grounding status Conflict.
- **D|cond.** A rejection resting on a D|cond row is conditional on that row's named conditions. The
  conditions are carried into the verdict and into Stage 3.
- **Cx rows.** A row with A3 = Cx never satisfies a rejecting or potentially rejecting predicate.

***

## 7. Carves: the grounding-relevance test

### 7.1 The test (GRT)

A carve Δ, a predicate on attribute values that defines `class(Δ)`, passes GRT iff all five hold.

- **GRT-1 (stated reason).** One of:
  - an inventory passage or the premise base gives a reason why items of one kind source, ground or are
    grounded in the metric while items of the other kind do not; or
  - it is derivable [A]/[P] from the non-excluded premise base that the two kinds differ in their ⊳_G
    relation to the metric, or in whether they are terms of the realized equation.
- **GRT-2 (K4).** The reason's premises are not on the excluded list (§2.2).
- **GRT-3 (K5).** The reason is not a difference of value, covariation or determination alone.
- **GRT-4 (K3, uniformity).** Applied as a predicate to every row, and to the K3 uses of §4.3, the class
  agrees with each corpus use, unless a further difference passing GRT-1 to GRT-3 is stated for the
  disagreement.
- **GRT-5 (no ad hoc edits).** `class(Δ)` is exactly the class the stated reason induces. No item is
  removed from it or added to it without its own GRT-passing reason (CONFIRM-BG-r4 DF-4).

A carve that fails GRT is rejected as a formalization (failed control). A carve whose GRT is Und is
undetermined (§8.1).

### 7.2 Candidate carves (fixed)

| Δ | Difference | Source of the candidate |
|---|---|---|
| Δ1 | partition-defined against not | GR:581's stated ground (r5 F4-5) |
| Δ2 | also a consequence of the law (A1q = yes) against not | GR:426 (r5 F4-5) |
| Δ3 | integration-constant selection (IC) against input term (T); defines F4-law | r5 F4-6; QB5(a) scope item |
| Δ4 | uniform (∝ `g`) against non-vanishing null flux; defines F4-null | r5 F4-6 |
| Δ5 | metric-defined (M) against fixed-cell (C) | r5 F4-7; GR:573's fixed-geometry examples |
| Δ6 | relative (A2§ filled) against absolute | §8.3; GR:569–577 (r5 F4-5) |
| Δ7 | emergent against classical | GR:575 (excluded), GR:452; GRT-2 decides |
| Δ8 | M-pure against terms with a non-metric argument | F4's exemption of the Einstein tensor (r5 §1.3, F4-1) |
| Δ9 | any further reason-bearing difference stated in an inventory row | closed by the inventory |

- Every candidate is tested by GRT. Listing a candidate here does not state that it passes or fails.
- A carve found during execution that is none of Δ1–Δ9 is a deviation (§14.2), and I-BLIND item 1
  applies to it.
- **Closure, both ways.** The negatives "no carve passes GRT" (needed for R) and "no row is rejecting for
  every co-constraint formalization" (needed for (A)) are relative to the frozen inventory and the
  candidate list. That relativity is stated with every verdict that uses it (OQ-2).

***

## 8. Decision rule

### 8.1 Stage 2: per-formalization verdicts

For each formalization in §3 and each branch b:

- **Rejected:** at least one rejecting row (§6.3), or a failed control (K1–K5, or GRT for a carve).
- **Admissible:**
  - no rejecting and no potentially rejecting row;
  - K1–K5 green, and GRT passed for a carve.
- **Undetermined:**
  - otherwise: no rejecting row, but some potentially rejecting row, or an undetermined control;
  - the r5 R-5 clause applies: an undetermined formalization is neither admitted nor rejected.

K1–K5 are r5's (r5 §1.4), applied per formalization. K3 is read as "K3 fails a carve for which no
difference relevant to grounding is stated" (NOTES-BG-r5 §3), operationalized by GRT.

### 8.2 Stage 2: summary class for F4

The summary class is computed per branch from the verdicts of uniform F4 and of every carve variant
F4[Δi] (including F4-law and F4-null).

| Class | Condition |
|---|---|
| **R**: F4 rejected on the corpus's own commitments | F4 is Rejected; no carve variant is Admissible; no carve variant is Undetermined |
| **Cc**: F4-c class specified | F4 is Rejected, and at least one carve variant is Admissible |
| **C**: F4 compatible | F4 is Admissible |
| **U**: undetermined | F4 is Undetermined; or F4 is Rejected, no carve variant is Admissible, and at least one is Undetermined |

- The four conditions partition the cases: each Stage-2 table falls in exactly one class [A].
- The F5 verdict is reported beside the class: Admissible, Rejected or Undetermined.
- Every verdict states:
  - Reading G, case β, N5-G;
  - the branch;
  - the conditions of any D|cond row it rests on;
  - the relativity of §7.2's closure clause.

### 8.3 Stage 3: B_G's outcome

Stage 3 is written after the Stage-2 commit (X-7).

1. **Classify the W0 rows** by §5–§6, per route ρ ∈ {𝒞_div, Jacobson}.
2. **Sort.** Each Admissible or Undetermined formalization v is sorted by its content with respect to
   the witness's term:
   - grounding-content if the W0 row's quantity is in `Dom(v)`;
   - CoC-content if it is not;
   - Und if a W0 attribute that decides membership is Und.

   F5 is CoC-content.
3. **Apply r5's outcome rule** (r5 §1.2) per branch and route:
   - **(A)** at least one grounding-content formalization is Admissible, and no CoC-content
     formalization is Admissible or Undetermined;
   - **(B)** at least one CoC-content formalization is Admissible, and no grounding-content formalization
     is Admissible or Undetermined;
   - **(C)** otherwise. The residual is stated: both kinds remain, or neither does, or an undetermined
     item decides.
4. **Robustness.** If an Und cell or an Undetermined formalization affects the result, compute the outcome
   under each resolution. If all resolutions agree, that outcome holds. Otherwise the outcome is (C), with
   the cell or control named.
5. **Report W0's derived cells,** U[v, b] for each v, as for every row.

**Implications by Stage-2 class.** Each implication is conditional on Reading G, case β and N5-G, on the
branch and route, and on the conditions of §8.2.

| Stage-2 class | F5 | B_G outcome |
|---|---|---|
| R | Admissible | (B): no grounding-content formalization survives, and F5 does |
| R | Rejected | (C): neither kind survives |
| Cc | Admissible | (C) if some admissible carve leaves the W0 quantity in its domain; (B) if every admissible carve's class contains it |
| Cc | Rejected | (A) if every admissible formalization is grounding-content; (B) if every one is CoC-content; otherwise (C) |
| C | Admissible | (C): uniform F4 and F5 both survive, unless the W0 quantity is outside `Dom(F4)` on that route |
| C | Rejected | (A) if no CoC-content variant is Admissible or Undetermined; otherwise (C) |
| U | any | (C), with the deciding item named, unless the robustness step returns one outcome |

The table is a reading aid. Items 1–5 govern. Where they disagree with the table, items 1–5 apply, and the
disagreement is recorded as a defect of this preregistration.

***

## 9. Hypothetical tables, one per class

These are constructed examples, not corpus readings. Each toy has its own toy premise base: Reading-G
analogues of N1–N3-G, N3′, transitivity and N5-G, and Lemma U, general form. K1–K5 are stipulated green
for every toy formalization unless stated otherwise. `w*` is a constructed toy row with status Cx.

Column key: Role (A1), Comp (A1c), Def (A2, A2t), St (A3), Gc (A5g), then U[F4], U[F4-law], U[F4-null]
(branch β0; the toys have no A2§).

### 9.1 Class R (toy TC-R)

| Row | Role | Comp | Def | St | Gc | U[F4] | U[law] | U[null] |
|---|---|---|---|---|---|---|---|---|
| p1: curvature-coupling term of a non-minimally coupled scalar, `ξ(G_μν φ² − ∇_μ∇_ν φ² + g_μν □φ²)`, on the source side | T | full | M-geo (closing), with matter argument φ | D | No | Y | Y | Y |
| p2: dust | T | full | C | D | No | N | N | N |
| w* | T | full | M (closing) | Cx | No | Y | Y | Y |

- **Toy carves.** None. The toy premise base states no reason-bearing difference.
- **Stage 2.** p1 is rejecting for F4, F4-law and F4-null, and no carve is admissible. Class **R**.
  F5 is Admissible.
- **Stage 3.** Every grounding-content variant is Rejected, and F5 is CoC. Outcome **(B)**.

### 9.2 Class C (toy TC-N)

| Row | Role | Comp | Def | St | Gc | U[F4] | U[law] | U[null] |
|---|---|---|---|---|---|---|---|---|
| n1: dust | T | full | C | D | No | N | N | N |
| n2: a horizon-defined energy density | T | full | M-geo (closing) | Ps | No | Y | Y | Y |
| n3: Komar mass | Dep, A1q = yes | — | M | Ns (A3v: D) | No | N | N | N |
| n4: bare Λ | IC | uniform | X | Ps | No | N | N | N |
| w* | T | uniform | M (closing) | Cx | No | Y | Y | N |

- **Toy carves.** None. Δ3 and Δ4 are tested by GRT like every carve; the toy states no reason for
  them, so F4-law and F4-null are Rejected by GRT-1. The same holds in every toy below unless a reason is
  stated.
- **Stage 2.** No row is rejecting or potentially rejecting for F4. Class **C**. F5 is Admissible.
- **Stage 3.** F4 is grounding-content (w* is in its domain), and F5 is CoC-content. Outcome **(C)**.

### 9.3 Class Cc (toy TC-C)

| Row | Role | Comp | Def | St | Gc | U[F4] |
|---|---|---|---|---|---|---|
| c1: the `R`-term of `f(R)` gravity written as an effective stress tensor | T | full | M-pure (closing) | D | No | Y |
| c2: a horizon-defined thermal density with a matter-count argument | T | full | M-geo (closing) | Ps | No | Y |

- **Toy carve.** The toy premise base contains axiom Ax-κ: "a functional of the metric alone belongs to
  the geometric side and is not a term of the source content". This states a reason in the sense of
  GRT-1, second clause. The carve Δκ = M-pure passes GRT, and `class(Δκ) = {c1}`.
- **Stage 2.** F4 is Rejected by c1. F4[Δκ] has no rejecting row (c2 is Ps) and is Admissible. Class
  **Cc**. F5 is Admissible.
- **Stage 3.**
  - If w* has a non-metric argument, it is outside `class(Δκ)`. F4[Δκ] is grounding-content, and with F5
    the outcome is **(C)**.
  - If w* is M-pure, it is inside `class(Δκ)`. F4[Δκ] is CoC-content, and no grounding-content
    formalization survives: **(B)**.

### 9.4 Class U (toy TC-U)

| Row | Role | Comp | Def | St | Gc | U[F4] |
|---|---|---|---|---|---|---|
| u1: a source term with no stated definition | T | full | Und | D | No | Und |

- **Stage 2.** u1 is potentially rejecting, and F4 is Undetermined. Class **U**, with u1's A2 named.
- **Stage 3.** Resolving u1 to M gives R, and so (B). Resolving it to C gives C, and so (C). The
  resolutions disagree, so the outcome is **(C)** with u1's A2 named.

### 9.5 The (A) route (toy TC-A)

| Row | Role | Comp | Def | St | Gc |
|---|---|---|---|---|---|
| a1: a fixed-cell vacuum energy, stated as "that in virtue of which the curvature is what it is" | T | uniform | C | D | Yes (D) |
| w* | T | uniform | M (closing) | Cx | No |

- **Stage 2.**
  - F4 has no rejecting row (a1 is C): class **C**.
  - F4-null denies a uniform term grounding, so a1 is rejecting for it: Rejected (it also fails GRT-1
    in this toy).
  - F5 is Rejected by a1.
- **Stage 3.** F4 is grounding-content with respect to w*. No CoC-content formalization is Admissible.
  Outcome **(A)**.

Each Stage-2 class is reached by at least one table, and each of (A), (B) and (C) is reached by at least
one table [A].

***

## 10. Controls

### 10.1 Rule-level controls

- The rule-level controls test the rule itself. Each has a required result.
- The reviewer runs them by hand at preregistration review. The executor re-runs them at node Q-0,
  before any inventory row is classified.
- A rule-level control that returns anything other than its required result, including Und, has
  failed.
- If any rule-level control fails, the rule is defective, execution halts, and only an amendment
  (§14.3) can resume it.
- A verdict printed over a failed or undetermined control is void.

### 10.2 RC-P (positive) and RC-N (negative)

- **RC-P.** TC-R (§9.1) must return class R for F4, F4-law and F4-null, with F5 Admissible.
- **RC-N.** TC-N (§9.2) must return class C, with F5 Admissible.

### 10.3 RC-X (countercontrol against fitting)

Each flip changes one input to its opposite. The class must change.

| Flip | From | To (required) |
|---|---|---|
| X1: TC-N, n2's status Ps → D | C | R (n2 rejecting; no toy carve) |
| X2: TC-R, p1's definiens M → C | R | C |
| X3: TC-A, a1's A5g Yes → No | F5 Rejected; (A) | F5 Admissible; (C) |
| X4: TC-C, remove Ax-κ | Cc | R |

A rule that returns the same class on both sides of any flip is insensitive to the input that decides
it, and RC-X fails.

### 10.4 RC-W (witness-tuning countercontrol; owner guidance)

RC-W catches a rule tuned to the witness.

- **W-a (relabelling).**
  - Toy TC-W has rows k1 and k2 with identical attribute vectors: T, full, M (closing), D, Gc No. k2 is
    tagged "the witness".
  - Required: k1 and k2 receive identical derived cells, and moving the tag from k2 to k1 leaves every
    Stage-2 verdict unchanged.
- **W-b (inertness of constructed rows).**
  - In TC-R and TC-N, vary w* over every combination of Role ∈ {T, IC, Dep}, Comp ∈ {full, uniform},
    Def ∈ {M, C, X, Und} and Gc ∈ {Yes, No}, with its status Cx.
  - Required: the Stage-2 classes stay R and C respectively.
- **W-c (decoy carve).**
  - Δ† is either "the offset term is exempt from grounding" (a row-identity predicate), or "defined
    through a zero-point convention", an attribute L that the toy premise base does not relate to ⊳_G or
    to membership among terms.
  - Required: Δ† fails GRT (GRT-1 for both forms; GRT-5 for the row-identity form). F4[Δ†] is Rejected
    as a failed control.
- **W-d (decoy selector).**
  - Rule S† is "adopt F4 if U[F4](w*) = Y, else adopt F5".
  - Required: under W-b's variation, S†'s output changes and the frozen rule's output does not. This is
    the detection criterion: any rule whose Stage-2 output depends on a Cx row fails W-b.

### 10.5 RC-U (undetermined control; carried from r5 R-5)

- TC-U (§9.4) must return class U with u1's A2 named, and Stage 3 must return (C) with it named.
- A second toy, TC-K: TC-R with one added toy carve Δk, drawn on a toy attribute that p1 has and w*
  lacks (a predicate on attributes, not on rows), with Δk's K3 stipulated Und. It must return:
  - F4[Δk] Undetermined;
  - class U;
  - (C) with K3 named. If Δk passed, F4[Δk] would be Admissible and grounding-content with respect to
    w*, giving (C). If it failed, the class would be R, giving (B). The resolutions disagree.

### 10.6 Formalization-level controls

K1–K5 (r5 §1.4) are assessed per formalization at node Q-7, under r5 R-5's clause: a failed control
rejects the formalization; an undetermined one leaves it neither admitted nor rejected.

***

## 11. Execution order (§A.31, depth-first)

The nodes run in this order. Each closes with an explicit check and a recorded verdict.

| Node | Content | Output |
|---|---|---|
| Q-0 | Re-run RC-P, RC-N, RC-X, RC-W, RC-U | all green, or halt |
| Q-1 | Q5, the G3 target: rows G-GR12, G-GR162, G-GR370, G-GR691, G-GR697, T-SM160, T-SM162 | {divergence-free sourcing law; null-flux route; both named as alternatives; not fixed}, with citations |
| Q-2 | Q3, F4's scope: the A1c of the rows with role T and A3 ∈ {D, Rq}; any stated reason for a scope, fed to GRT for Δ3 and Δ4 | {full; null-flux; law-input; not fixed} |
| Q-3 | Q4, §8.3: GR:577's scope clause; A2§ for every relative or epoch-differential quantity | the clause's scope; the counterpart per quantity |
| Q-4 | Classify every corpus row of §4.2 (A1–A5g), in table order; the same-quantity table first | the audit table, corpus rows |
| Q-5 | Q6: Δ1 applied as a predicate to every row; where T-GR384's quantity falls | the induced class and T-GR384's position |
| Q-6 | GRT for Δ1–Δ9 | pass, fail or Und per carve, with reasons |
| Q-7 | Stage 2: §6, §8.1, §8.2; K1–K5 per formalization; the skeptical nodes (below); **commit** | the verdicts and the summary class per branch |
| Q-8 | Classify W0-Z0, W0-ZI and W0-ZII by §5–§6, per route | W0 rows |
| Q-9 | Stage 3: §8.3 | B_G outcome per branch and route |
| Q-10 | Fixed-point passes (below) | NEW count per pass |

**Skeptical nodes (§A.31).** A cell is favourable to the framework in one of two directions:

- **Coexistence:** it keeps a corpus source term realizable under F4. Examples: role Dep rather than T;
  definiens C or X; a status other than D or Rq; a carve passing GRT.
- **Decoupling:** it makes F4, or a variant that is grounding-content with respect to a W0 row,
  Admissible.

For each such cell that decides a Stage-2 verdict, a node states the strongest textual reading on which
the cell takes the other value, and the cited ground on which that reading is rejected. If no such ground
exists, the cell is Und. Both directions receive the same treatment.

**Fixed point.** Passes continue until three consecutive passes yield no NEW finding (§A.31). Where that
is not reached, the record says so.

***

## 12. Productivity test (§A.31), fixed in advance

- **Baseline.** r5's residual (r5 §7; BG-F5, BG-F6):
  - F4 against F5, with F4's scope not fixed by the premise base;
  - F4-c's K3 undetermined;
  - under §8.3, F4's treatment of epoch-differential pieces undetermined;
  - the corpus stating no view on whether source terms ground.
- **Gem.** The unit is a gem iff it yields a fact strictly stronger than the baseline AND either:
  - (a) **it constrains**: at least one of the following is determinate where the baseline has it open:
    - a Stage-2 verdict on uniform F4, or on some variant, from the corpus's own commitments;
    - F4's scope (Q3);
    - a carve passing or failing GRT;
    - a counterpart fixed (Q4);
    - the G3 target (Q5); or
  - (b) **it exposes a hidden assumption**: an assumption-watch marker not among AW-part, AW-metric,
    AW-entropic and AW-ground (r5 §9).
- **Coherence check.** A completed table whose Stage-2 verdicts and Q3–Q5 outputs are all undetermined
  or restate the baseline, with no new marker, is recorded as a coherence check.
- A class U result is a gem only through (b), or through a determinate Q3–Q5 output.
- Findings are classed NEW, POSITIVE, ELABORATING, CONFIRMING or BORDERLINE (§A.31).

***

## 13. Invariant → checkpoint table (§A.41)

| ID | Invariant asserted of the execution | Checkpoint that measures it |
|---|---|---|
| X-1 | No computation on OI rules; reading and hand logic only | NOTES lists every command run; the reviewer confirms that only read-only git and grep commands appear |
| X-2 | The corpus is read at `c3b5f37a` | Every quotation is checked verbatim against `git show c3b5f37a:<path>` by the reviewer; NOTES records `main`'s head at execution and any inventory line that changed |
| X-3 | The rule is frozen before analysis | The freeze commit F contains this file and no execution file. The first execution file appears in a descendant of F. Checked from the branch history |
| X-4 | The inventory is closed | The set of row IDs in the decisive table equals §4.2 ∪ §4.4. Any other row is marked `X-n` and appears only in the deviations table. The reviewer compares the ID lists |
| X-5 | I-SYM, uniform classification | (i) Every row, including T-GR352, T-GR577 and the W0 rows, has every column of §5 filled with a citation or Und. (ii) The reviewer checks every pair of rows with identical attribute vectors for identical derived cells. (iii) A grep of the record's rule-application text (§6–§8 analogues) for row IDs, `ρ_Z`, `K_cpl`, "witness" and `W0` finds hits only in the Stage-3 section and in table rows |
| X-6 | I-BLIND, inertness and fixed candidates | (i) RC-W green at Q-0. (ii) No Stage-2 verdict cites a W0 row. (iii) Every carve is one of Δ1–Δ9, or a deviation whose justification cites no W0 attribute |
| X-7 | Stage 2 precedes Stage 3 | The Stage-2 table and verdicts land in a commit whose tree contains no W0 classification and no Stage-3 text. Stage 3 lands in a descendant commit. Checked from the history |
| X-8 | Controls are green before any verdict | The Q-0 record precedes the table in the record and in the history. Any verdict is printed only beside a green Q-0 |
| X-9 | No excluded premise in a decisive step (K4) | Each decisive step lists its premises. The reviewer checks each against §2.2 |
| X-10 | Running-vacuum sourcing is not adopted (QB7(a)) | The rows on the running channel have A3 rendered from cited corpus text. No decisive step cites the running-vacuum literature or an owner adoption |
| X-11 | Status scope (§5.3) | Each A3 cell quotes its status word and names its grammatical object. The reviewer spot-checks all D and Rq cells and every cell that decides a verdict |
| X-12 | Conditions are carried | Every verdict line names Reading G, case β, N5-G, the branch, the route (Stage 3), its D|cond conditions and the closure relativity |
| X-13 | Prior readings are not anchors | No cell cites r5's §2.4 reading column or node verdicts as its ground. Agreement with r5 is recorded in a separate column after rendering |
| X-14 | Negative corpus-wide statements have a search (§A.19) | Any sentence of the form "the corpus states no …" cites the search patterns and hits in NOTES. Hits not in the inventory become `X-n` rows |
| X-15 | No outcome is stated in this preregistration | The reviewer confirms that §4–§12 render no cell of an inventory row and state no expected class |
| X-16 | No manuscript change; paper-only; no premise adopted | `git diff --stat` on `papers/` and `book/` is empty across the unit's commits |
| X-17 | Barred strings are absent | A grep of the unit's files for the barred path strings returns nothing |

***

## 14. Freeze, deviations and amendments

### 14.1 Before freeze

- Revisions of this preregistration are numbered r2, r3, …. Each is accompanied by a response file that
  lists every change and its trigger.
- Each revision is independently reviewed (QB6). A reviewer may propose rule text, but must not state an
  expected outcome for the inventory. A review that does so is recorded, and its proposals are adopted
  only if they can be justified without that expectation.
- **Freeze F.** F is the commit that contains the accepted revision, with the reviewer's acceptance
  recorded beside it. OQ-5 settles who designates it.
- No inventory row is classified before F.

### 14.2 Deviations after freeze

- A deviation is any departure from this preregistration during execution:
  - a passage outside the inventory (`X-n`, §4.5);
  - a carve outside Δ1–Δ9;
  - a test that cannot be applied as written;
  - a moved inventory passage on `main`.
- Each is recorded in a deviations table with its discovery node and a sensitivity line (the verdict with
  and without it).
- A deviation never changes a rendered verdict.

### 14.3 Amendments after freeze

- An amendment is a separate file (`G3-QB5A-AMEND-n.md`). It states:
  - the change;
  - its reason;
  - whether it was written before or after any Stage-2 cell was rendered;
  - which rendered verdicts it would affect.
- An amendment written after rendering needs independent review and a recorded owner decision before it
  takes effect.
- The verdict as originally rendered stays in the record beside the amended verdict.
- This preregistration is not edited after F.

***

## 15. Owner questions

OQ-1 to OQ-4 must be answered before F. OQ-5 and OQ-6 concern process.

- **OQ-1. QB7(a)'s scope.** QB7(a) says not to adopt running-vacuum sourcing as a premise. This
  preregistration reads that as: the channel's sourcing is not adopted by decision or imported, and its
  rows are classified by the same status test as every other row. If the corpus text itself held the
  sourcing as derived or required, the row would count as a commitment. The alternative reading bars
  those rows from rejecting F4 whatever the text says. That would depart from I-SYM. Which reading
  holds?
- **OQ-2. The grounding-relevance test and the candidate list.** Are GRT-1 to GRT-5 and Δ1–Δ9 accepted?
  Both universal negatives the rule uses ("no carve passes", for R; "no co-constraint formalization
  survives", for (A)) are relative to the frozen inventory and this list. Is that symmetric relativity
  accepted, in place of r5's open schema?
- **OQ-3. Counting carves that contain the witness's term.** §8.3 counts every admissible carve variant
  whose class contains the W0 quantity as CoC-content, extending r5 R-6 from F4-null to every carve.
  - This is required by I-SYM, since the carve is chosen without reference to the witness.
  - It has a consequence for the rule: if a carve whose class contains every metric-defined term passes
    GRT, then (A) is unreachable for a metric-defined W0 quantity.
  - This is a property of the rule, shown on the toys. It is not a reading of the corpus.

  Is this counting accepted?
- **OQ-4. Inventory additions beyond QB5(a)'s list.**
  - T-GR352 and T-GR577 (Group V) are added by the owner guidance.
  - Group Q's rows serve Q3 to Q6.
  - Group C's context rows are drafting additions (§4.2).

  Are these accepted as the frozen inventory?
- **OQ-5. Freeze designation.** This is a paper-only research unit, not a native V3 round. Is F
  designated by the owner on #873, or by the independent reviewer's acceptance?
- **OQ-6. Record of the guidance.** The 2026-11-14 owner guidance reached this draft through the
  coordinating session. Should it be recorded on #873, so that the record can quote it with author and
  time (§A.42 item 7)?

***

## 16. Limits

- The rule is preregistered. Its controls are hand-checked on constructed examples only.
- Every verdict is conditional on Reading G, case β and N5-G. In case α (r5 node B2), Lemma U does not
  apply and B_G is idle.
- The §8.3 branch rests on the geometry-first identification (U1r5:504–505).
- The negatives used by R and (A) are relative to the frozen inventory and candidate list.
- The witness keeps unit 2(a)'s scope: exact de Sitter and M1.
- No claim is made about K_cpl^conv's admissibility under G3, or about Λ.
