# G3 unit 2(b) (r5): the bridge premise B_G, grounding or co-constraint

**Scope.** This is a paper-only investigation under Issue #873, continuing units 1 and 2(a) (PR #1275).

- Authorization: #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU5: "a bounded, paper-only
  investigation of B_G: whether a term in the boundary-metric law that depends on the emergent class
  grounds the metric or only co-constrains it, including how far this reduces to the status of the
  boundary law under G3. … It adopts no premise, makes no manuscript change, involves no Lean build and
  makes no claim about Λ."
- **Revision history.**
  - r1 is `G3-UNIT2B-BG-r1.md` at `4acb3a49`, reviewed in `REVIEW-BG-r1.md` (REVISE) at `1970a36a`.
  - r2 is `G3-UNIT2B-BG-r2.md` at `8a3c43e19d3debd629f3e8506b96b00b47f4db6b`, checked in
    `CONFIRM-BG-r2.md` (REVISE) at `27c409a0`.
  - r3 is `G3-UNIT2B-BG-r3.md` at `7fd16a5d81f20d85b98544b8349f550c07b4c519`, checked in
    `CONFIRM-BG-r3.md` (ACCEPT WITH CHANGES) at `651849ab`.
  - r4 applies CONFIRM-BG-r3 CF-1 to CF-7. Dispositions are in `RESPONSE-BG-r3.md`.
  - r5 applies CONFIRM-BG-r4 (at `905b68cc`) DF-1 to DF-4 only. Dispositions are in `RESPONSE-BG-r4.md`.
    Earlier revisions are not edited.
- Inputs on branch `research/g3-offset-873-20261113`:
  - unit 2(a) r3, `G3-UNIT2A-r3.md` at `1ad01923` ("U2Ar3:n");
  - unit 1 r5, `G3-UNIT1-r5.md` ("U1r5:n");
  - the unit 1 forward corrections `G3-UNIT1-CORR-r1.md` and `G3-UNIT1-CORR-r2.md`;
  - reviews 5896999577 and 5898121925 on #1275.

This record proves no theorem in Lean, runs no computation, changes no manuscript, adopts no premise and
makes no claim about the magnitude of Λ.

**Source snapshot.** `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`. Every `file:line` refers to
that commit.

**Support labels**, as in units 1 and 2(a): [K] kernel-checked declaration on `main`; [A] exact algebra or
elementary logic, done by hand here; [P] a paper derivation, or a reading of a paper statement;
[L, recalled] literature recalled from memory and not re-read, on which no verdict rests; "Conjecture" an
unsupported proposal. **Conditional** marks a claim that holds only under the hypotheses it names.

**Terms from unit 2(a).**

- ⊳_E is the order of explanation (specification).
- ⊳_D is the order of determination (value dependence on a family).
- ⊳_G is the order of existence or emergence: `X ⊳_G Y` if `Y` is what it is partly in virtue of `X`.
  The three orders are defined at U2Ar3:206–217.
- N1–N5 are the premises of GR:346 (U2Ar3:195–202). N5-G is the well-foundedness of ⊳_G
  (U2Ar3:226–231).
- Reading G is U2Ar3:277–287.
- The witness is the K_cpl^conv fixed-point model on the de Sitter family under M1 (U2Ar3:291–419). Its
  partition is the static patch whose horizon is GR:40's event horizon (U2Ar3:303–304).
- **B_G** is: "a term of the boundary metric's law that is a function of the emergent class grounds the
  realized metric, and does not only co-constrain it" (U2Ar3:285–287).

***

## 0. Verdict

**Outcome (C). Scope: Reading G of GR:346 with N1–N3 read in ⊳_G (case β, §6 node B2), conditional on
N5-G.** The rule is r1's rule as repaired at review (§1.6). Under it, (C) is the outcome whenever the
premise base states no view on whether a derived law's source terms ground its solutions. Unit 2(a)
recorded that the corpus states none (U2Ar3:538), and the wider search here finds none (NOTES-BG-r3 §3).

- **Established.**
  - **Lemma U** (§3.1) [A], given its premises. A law term grounded in the realized metric cannot ground
    that metric. This is Reading G's reductio specialized to a law term.
  - **Corollary E** (§3.2) [A]. Read on the co-constraint view, B_G holds exactly when the witness's law
    is realized at no OI world.
  - **F3 is refuted** (§3.3) [P], by the single bijection: Main:44, Main:54, and A1–A6 at
    Structure.md:136.
- **The admissible formalizations (§3.4).**
  - **F5** (co-constraint, regularity view; CoC-content) is admissible.
  - **F4** (non-fundamental sourcing as grounding, stated on the energy content of every non-Einstein
    term of the realized equation; grounding-content) is admissible.
  - **F4-c** (F4 with a stated class of metric-defined terms not grounding; grounding-content) has K3
    undetermined, because the candidate classes examined fail and are not shown to be exhaustive.
  - No premise outside the excluded list selects between F4 and F5, so the outcome is (C).
- **What F4 gives [A] given F4.** With Lemma U, F4 excludes the witness's law on Reading G.
  - **Relata.** This holds for the witness as defined, whose partition uses GR:40's event horizon. It
    fails only for a variant whose partition is slice-local and whose grounding relata are diachronic
    (§6 node F4-3).
  - **Route.** On the corpus's conditional Jacobson route, the uniform term has zero null flux
    (U1r5:603–606, U1r5:671) [A]. The witness's dependence then sits in the datum that selects the
    integration constant (U1r5:596–600). F4 as stated still reaches it there, because the constant is a
    uniform term of the realized equation (SM:162). F4-null, an F4 restricted to the null-flux source,
    reaches the witness on neither route, since `g_μν k^μ k^ν = 0` algebraically (§6 node F4-6).
- **The cost of F4 on Reading G [P].**
  - With N3′ (or node B4), Lemma U's cycle does not depend on whether a term is emergent. Under F4,
    every source term defined as a function of the metric is unrealizable on Reading G.
  - **At stake in either §8.3 branch:**
    - GR:384's `ρ_s`, unless it is read as a consequence of the law (GR:426) rather than a term of it;
    - §7.3's `ρ_E` (GR:528–530);
    - GR:400 Reading 2's partition-geometry source, wherever it depends on `H`.
  - **Excluded with §8.3 not in force; undetermined with it:** GR:400 Reading 1 and the running
    channel's `H`-dependence (GR:374–380). Under §8.3 the outcome depends on what the classical
    counterpart is. For the running channel it leans to exclusion on the corpus's stated mechanism
    ("depending on the hidden sector's volume", GR:374; "via `A = 4πc²/H²`", GR:378(i)), by F4-7 (§6
    node F4-5).
  - The corpus requires "some state dependence on cosmological geometry" of the emergent vacuum energy
    (GR:374). That statement concerns dependence, not sourcing. Whether the running channel is a source
    is the coupling question GR:400 does not adjudicate, and its functional form is "not derived"
    (GR:633). The Type II channel is "a structural reading, not a derived law" (GR:354).
  - **Not at stake:** GR:695.
  - No carve-out has been stated that admits these and excludes the witness on a ground relevant to
    grounding. Partition-definedness does not supply one, because `ρ_Z` is partition-defined (§6 node
    F4-5).
  - The §8.3 branch rests on the geometry-first identification (U1r5:504–505).
- **How far the gap reduces to G3 (§4).**
  - The status sense of "derived" is fixed by P-D for any boundary law that holds.
  - "Directly" (U2Ar3:548–549) is B_G, which here is the question of F4 against F5.
  - G3's equation decides where the witness's dependence sits: in a source term, or in the selection of
    the integration constant. It therefore bears on which scope of F4 is natural. Reach is fixed by the
    scope, which the premise base does not fix: F4 as stated reaches the witness on both routes, and
    F4-null on neither [P].
- **Controls.** K1–K5 are green for F3, F4 and F5 (§5). For F4-c, K3 is undetermined. That does not
  decide the outcome while uniform F4 is admissible (§7).
- **If the running channel were held as a premise (QB7(a)).** Uniform F4 would be rejected by (b2)
  wherever it excludes the channel: without §8.3, and with §8.3 unless the answer to (b) is a fixed-cell
  quantity. F4-c, with K3 undetermined, would then decide the outcome, which by §1.4 is (C) with K3 named.
  It would be (B) only if no grounded carve-out exists (§6 node F4-8).

**Scope.**

- The verdict concerns B_G and Reading G.
- It does not show that K_cpl^conv is admissible in OI. P11, GR:575 and (ii-S) exclude it
  (U2Ar3:76–78).
- It is conditional on N5-G, which is contested [L, recalled], and on case β. In case α (Main:26,
  Main:48), Reading G's reductio fails at N2-G, and B_G is idle (§6 node B2).
- The witness keeps unit 2(a)'s scope: exact de Sitter and M1.

**Consequences** (§8). Each is conditional, and none edits a record.

1. On Reading G, among the formalizations examined (F1–F5), GR:346 excludes K_cpl^conv's field
   equation if F4 holds for the boundary law's source terms, within F4's scope (§6 nodes F4-3, F4-6).
   Given F5 it excludes no field equation beyond G3's determination question [A] given each
   formalization, [P] for the readings. The list of formalizations is not shown to be exhaustive.
2. (ii-L) remains an added premise on Readings E and D (U2Ar3:684–696). Its candidate motivation through
   Reading G is conditional on F4, together with F4's cost.
3. Unit 2(a)'s outcome stays (C), with its gap narrowed from B_G to F4 against F5. Unit 1 Part 2 keeps its
   conditional form. Forward notes are held (QB2).

***

## 1. Decision rule

**Provenance of the rule.**

- §1.1–§1.5 are r1's rule, with every later edit recorded in §1.6. R-1 to R-3 were made at r2; R-4 to
  R-6 at r3 (R-6 recorded at r4); R-7 at r4.
- r1's rule was written after the sources had been read and an outline formed (NOTES-BG-r1 §4).
- The r2 repairs were written after REVIEW-BG-r1, which named the outcome it expected, (C). The r3
  repairs were written after CONFIRM-BG-r2, which stated that (C) survives once they are applied. The r4
  edits were written after CONFIRM-BG-r3, which accepted (C) with changes.
- Under the repaired rule, (C) is the outcome whenever the premise base states no view on whether a
  derived law's source terms ground its solutions. Unit 2(a) recorded that it states none (U2Ar3:538).
  That (C) agrees with the reviews' expectation is not evidence either way.
- The rule and the analysis land in one commit.

### 1.1 Premise base

- **The corpus's stated premises:** the text of `main` at `c3b5f37a`, as cited, with its stated status.
- **Reading G's own premises:** N1–N3 read in ⊳_G, and N5-G. B_G is the bridge premise of Reading G
  (U2Ar3:285–287). N5-G is labelled as not stated in the corpus.
- **Excluded as premises:**
  - B_G and its negation;
  - (ii-W), (ii-L), (ii-S) and (ii-G) as exclusions;
  - GR:342 "This ordering is forced …" and "not the reverse";
  - GR:346 s.4;
  - book/ch07-gravity.md:187;
  - GR:340 s.1's ordering clause;
  - GR:340 s.2 (P11);
  - GR:575's clause "What does not gravitate";
  - any form of the boundary law, its derivation, or its non-derivability (G3);
  - the separation clauses of Substratum.md:385–389 and GR:655's clause "(a property of the classical
    substratum's gravitational dynamics)" (R-2).

### 1.2 Outcomes (repaired, R-1)

An **OI world** is a realization `(S, φ, x₀)` that satisfies the premise base, with the partition realized
as GR:40 states, together with the completion under test.

**Formalizations.** A formalization of B_G is classified by its **content** with respect to the
witness's term, meaning what the holding of a boundary law consists in.

- **Grounding-content:** the law's holding includes the grounding of the realized metric by that term.
- **CoC-content:** the law's holding is a relation among items with a common ground, and that term does
  not ground the metric.
- **Admissible:** a formalization that passes K1–K5 and is not contradicted by a premise in the premise
  base.

**Outcomes.**

- **(A) B_G supported.** The premise base (premises named) leaves admissible at least one
  grounding-content formalization and no CoC-content formalization.
- **(B) B_G refuted / co-constraint.** The premise base leaves admissible at least one CoC-content
  formalization and no grounding-content formalization. Each grounding-content formalization is
  rejected by (b2) a named stated premise it contradicts, or by a failed control.
- **(C) Open.** Both kinds remain admissible, or neither does. The residual is stated.

**Non-vacuity, both ways.** No clause may be met by an entailment that holds only because the witness's
law is realized at no OI world. For grounding-content formalizations, non-realizability is a consequence
of their content together with Lemma U, not a premise. That is not vacuity.

### 1.3 Formalizations quantified over

- **F1 (realized).** At an OI world `w` where the witness's law holds, its term grounds `g_w`. This is B_G
  read on F5's view. By Corollary E it is false at every OI world where the law holds. It is not itself a
  CoC-content formalization (R-4).
- **F2 (law-level).** For every OI world where the witness's law holds, its term grounds the realized
  metric. This is B_G read on F5's view, and it holds only if no OI world realizes the law (Corollary E).
  It is not itself a CoC-content formalization (R-4).
- **F3 (fundamental governing law).** The boundary law is a fundamental item, and its inputs ground its
  outputs. Grounding-content.
- **F4 (non-fundamental sourcing as grounding; R-3).** The boundary law is not fundamental, and its
  grounds trace mediately to `(S, φ)`. The energy content of every term of the realized equation other
  than the Einstein tensor grounds the realized metric, and the Einstein tensor does not. Grounding-content.
  - §3.4 states F4 invariantly.
  - Node F4-6 names a narrower scope, F4-null, in which only the null-flux source term grounds. With
    respect to the witness's term F4-null is CoC-content, because the null flux of `ρ g_μν` vanishes.
- **F4-c (carved sourcing as grounding; R-7).** As F4, except that a stated class of metric-defined terms
  is not grounding while the witness's term is. Grounding-content. F4-c is a schema: its class is not
  fixed by the corpus.
  - Each candidate class examined so far fails (§6 node F4-5). Partition-definedness covers `ρ_Z`, so it
    does not yield an F4-c; removing `ρ_Z` from it ad hoc fails K3. "Emergent against classical" fails K4, because it is GR:575's excluded clause. "A
    consequence of the law, not a term of it" (GR:426) covers `ρ_s` only.
  - The candidates are not shown to be exhaustive, so K3 for the schema is undetermined.
  - (B) through F4-c therefore requires showing that no class with a difference relevant to grounding
    exists.
- **F5 (co-constraint, regularity view; R-4).** The boundary law's holding is satisfaction of its
  equation. Its term and the realized metric have grounds in `(S, φ, x₀)`, and the term does not ground
  the metric. CoC-content.
- Any further formalization found during the analysis is added under the same clauses.

### 1.4 Controls

- **K1 (positive, non-vacuity).** The formalization must class as grounding, and Reading G must exclude,
  a C1-type configuration (U2Ar3:483): a metric that is by its nature a quantity of the realized emergent
  description, with realized value `g_{R*}`.
- **K2 (negative).** The formalization must not exclude, or class as a ⊳_G-cycle:
  - (a) K_dec;
  - (b) the Einstein nonlinearity;
  - (c) the gap equation (GR:154; book/appendix-c-objections.md:259).
- **K3 (uniformity with the corpus's uses).** The same criterion is applied to GR:340, GR:342, GR:346,
  Substratum.md:385–393, GR:162, SM:160–162, GR:374–380, GR:384, GR:400 Reading 1, GR:482 and
  GR:528–530. A classification that differs from a corpus use without a stated difference relevant to
  grounding fails K3.
- **K4 (no import).** The premises of each decisive step are listed, and none is on the excluded list of
  §1.1.
- **K5 (grounding is not determination).** Configurations with the same ⊳_D graph must be able to differ
  in ⊳_G.

A verdict is written only if K1–K5 are green for the formalizations it rests on. A formalization with a
failed control is rejected. One with an undetermined control is neither admitted nor rejected. If that
decides the outcome, the outcome is (C) with the control named (R-5).

### 1.5 Productivity test (§A.31)

The unit is a gem if it yields a fact strictly stronger than unit 2(a)'s statement (B_G "open … narrowed
to the status of the boundary law (G3) and to a view of laws the corpus does not state", U2Ar3:746), and
the fact either constrains a claim or exposes a hidden assumption. Otherwise it is recorded as a
coherence check.

### 1.6 Repairs at review

- **R-1 (r2; REVIEW-BG-r1 BG-1).** r1's clause (A) barred an entailment through non-realizability, and
  (b1) carried no matching bar. With Lemma U at every OI world, (A) was unreachable, so r1's rule was
  defective. The repair, §1.2:
  - formalizations are classified by content;
  - non-vacuity applies to both sides;
  - the outcome is decided by which kinds remain admissible.
- **R-2 (r2; BG-3).** The Substratum.md:385–389 separation clauses and GR:655's clause are added to the
  excluded list.
- **R-3 (r2; BG-1).** F4 is added.
- **R-4 (r3; CONFIRM-BG-r2 BC-1).** r2 labelled F1 and F2 "CoC-content" and called them admissible. By
  Corollary E, F1 is false wherever the law holds, and F2 holds only vacuously. Read literally, r2's
  rule had no admissible CoC-content formalization and returned (A), not the (C) r2 reported.
  - F5, the co-constraint view itself, is added.
  - F1 and F2 are restated as B_G read on F5's view.
  - With F5 admissible, the rule returns (C) (§7).
  - The (A) that r2 literally returned came from omitting the CoC formalization from the list. It was
    not a finding about the corpus.
- **R-5 (r3; BC-4).** These edits to §1.1–§1.5 were made at r2 and not recorded there.
  - **§1.1.** "and has no role off it" and the rationale clause of the excluded list were dropped. Reason:
    condensation. Neither changes the premise base.
  - **K1.** The phrase "so that the verdict depends on the order of grounding and not on values" was
    dropped. Its content is K5.
  - **K3.**
    - "(P11)" was dropped from the list, because P11 is excluded as a premise; its sentence is still
      read as vocabulary.
    - Substratum.md:385–389 became :385–393, to include :393.
    - GR:384 and GR:482 were added, as corpus uses that bear on F4.
    - The failure wording changed from "is void" to "fails K3", to fit the per-formalization structure
      of R-1.
  - **Closing line of §1.4.** It dropped "A failed control voids it, and the outcome is then (C) with the
    failed control named", and gained "for the formalizations it rests on". This left no clause for an
    undetermined control. r3 restores one above.
  - **§1.5.** It dropped "Otherwise it is recorded as a coherence check", restored above.
  - **K3 at r3.** GR:374–380 and GR:528–530 are added (CONFIRM-BG-r2 BC-3, BC-8).
- **R-6 (r3, recorded at r4; CONFIRM-BG-r3 CF-4).** These edits were made at r3 and not recorded there.
  - **§1.2.** The content classes are made relative to the witness's term. Grounding-content became "by
    that term", where r2 had "by its source term". CoC-content became "that term does not ground the
    metric", where r2 had "it includes no such grounding". This is substantive: it is what classes F4-null
    as CoC-content (§6 node F4-6).
  - **Clause (A).** It dropped its closing sentence, "On Reading G (N5-G, case β) the witness is then
    excluded by the content of its law", which restated Lemma U's consequence.
  - **Clause (C).** "The residual is stated precisely" became "The residual is stated".
  - **§1.3.** F4 is restated on the energy content of every non-Einstein term of the realized equation,
    where r2 had "the energy content of its source term" (CONFIRM-BG-r2 BC-2).
- **R-7 (r4; CONFIRM-BG-r3 CF-1).** F4-c is listed in §1.3. r3 counted it in §5 and §7 without listing it.

***

## 2. Formalization

### 2.1 Objects

- At a world `w`: the realized metric `g`; the realized partition `Π = Π(g)` (GR:40); the realized
  emergent class `r = T(Π)` (GR:344; Main:690); and the term `t = τ(r)`. For the witness, `τ = ρ_Z`
  (U2Ar3:315–328).
- **A law** is a relation `L(g, t, …) = 0` on a family of candidate configurations. For the witness it is
  `G[g] + Λ_c g = 8πG(T^cl − ρ_Z g)` (U2Ar3:342).

### 2.2 Three relations, kept apart

- **Specification (⊳_E)** and **determination (⊳_D)** are as in unit 2(a) (U2Ar3:208–213, :223–225).
- **Grounding (⊳_G)** is a relation at the realized world. It is transitive, and under N5-G it is
  irreflexive and well-founded [P; L, recalled: Fine 2012]. Configurations with the same values and the
  same ⊳_D graph can differ in ⊳_G (K5).
- **N3′.** A quantity defined as a function of another is grounded in it [P; L, recalled: Fine 1994,
  Rosen 2010]. For the witness, the horizon area alone gives `g ⊳_G ρ_Z` (§6 node B4). N3′ concerns how a
  quantity is defined. A quantity defined on the microstate, whose value covaries with the metric, is
  related to the metric by ⊳_D only (K5).

### 2.3 Two roles for a law term

Let `L` hold at `w`, with term `t`.

- **Grounds (Gr):** `t ⊳_G g`.
- **Co-constrains (CoC):** `¬(t ⊳_G g)`, and `g` and `t` have grounds in a common base. In OI the
  candidate base is `(S, φ, x₀)`.

Neither role is fixed by ⊳_E or ⊳_D [A].

### 2.4 The corpus's uses (K3)

| Corpus use | Text | Relation stated | Reading [P] |
|---|---|---|---|
| GR:340 s.2 (P11; excluded as a premise) | "The stress-energy sourcing gravity is the classical stress-energy of the total microstate" | "sourcing" | Consistent with F4 and with F5. Read as vocabulary only. |
| GR:342 | "no substance-level primitives … spacetime emerges from `[(S, φ)]/𝒢_sub`" | ultimate ground | Permits mediate grounding among derived items, so F4 is not excluded. |
| GR:346 | N1–N2: "Causal structure is determined by null geodesics"; "derived", "entry point" | ⊳_D or ⊳_G; ⊳_E | Case β reads N1–N2 in ⊳_G (U2Ar3:279–280). |
| Substratum.md:385–389 (separation clauses excluded, R-2) | "the metric is a property of the classical dynamics of the partition boundary" | "property of" | Not used in a decisive step. In ⊳_G with N1–N2 it is a cycle that involves no law term (U2Ar3:617–620). Under N5-G it must be read as ⊳_D, for K_dec and the witness alike. |
| Substratum.md:393 | "the metric … determined by the partition geometry and the area-law theorem" | "determined" | ⊳_D. |
| GR:162 | "uses the Einstein equations through Jacobson's relation (§3.1) and does not derive them" | status: used, not derived | The equation-of-state route, read as CoC [L, recalled: Jacobson 1995]. |
| SM:158 | the lattice construction: "the Clausius relation would constrain the graph's response … were the curvature step (iv) supplied"; "paralleling continuum GR where the Einstein equations are the equations of motion, not constraints on separate dynamics" | "constrain", hypothetical; the continuum parallel | Consistent with F5 for a hypothetical construction. The parallel supports P-D against F3. |
| SM:160–162 | Jacobson's inputs: (i) a proportional entropy law, (ii) the Unruh temperature, (iii) the energy flux `δQ = ∫T_μν k^μ dΣ^ν`, (iv) the Raychaudhuri equation; "(iii) is a definition and (iv) an identity" given the manifold; the displayed equation carries `Λ g_μν` | four inputs; the realized equation with a Λ term | A reading [P] of SM:160's list: input (iii) is the source, and inputs (i) and (ii) are thermodynamic intermediaries. SM:160 does not state that classification. A uniform term has zero null flux (§6 node F4-6). |
| GR:144 | "they refer to the same physical degrees of freedom: the boundary modes `V × B`" | matching | Consistent with F5. Contains no source term. |
| GR:352 | "does not entail that it cannot source geometry … a coupling theorem" | "source" | Consistent with F4 and with F5. |
| GR:358 | "feed back into gravitational dynamics through state-level quantities … everything that contributes to `H_tot` gravitates" | "feed back", "gravitates" | Consistent with F4 for classical energy content, and with F5. |
| GR:374–380 | "the emergent vacuum energy is a state-level quantity depending on the hidden sector's volume"; "boundary architecture requires some state dependence on cosmological geometry"; "the emergent vacuum energy inherits an `H`-dependence" through `A = 4πc²/H²`; `Λ_eff(H)`; Bianchi consistency through running `G` | a metric-dependent quantity in the field equations | GR:374 requires dependence, not sourcing. Under F4, its `H`-dependent part is unrealizable on Reading G without §8.3, and undetermined with §8.3, leaning to exclusion by F4-7 (§6 nodes F4-5, F4-8). Under F5 it is admitted. |
| GR:384; GR:422–426 | "The total gravitating boundary energy tracks the critical density at every `H` as an identity"; "a consequence of Jacobson's Clausius relation applied to the de Sitter horizon" | "gravitating", for a horizon-defined energy | Defined through `A` and `T_cl(H)`, so grounded in `g` (N3′). Under F4 it is unrealizable on Reading G if it is a term of the law. It is admitted if it is read as a consequence of the law (GR:426) rather than a term of it. Under F5 it is admitted. |
| GR:400 Reading 1 | "the emergent layer's curvature response … feeds back as a source"; "the substratum budget fixes the constant part" | "source" | Under F5, admitted. Under F4, excluded without §8.3 and undetermined with it (§6 node F4-5). |
| GR:400 Reading 2 | "only partition geometry sources gravity … `ν = ν_sub` alone" | "sources", for partition geometry | Under F4, a partition-geometry source that depends on `H` is grounded in `g` and unrealizable on Reading G. Under F5, admitted. |
| GR:482 | "The Jacobson mechanism converts the entropy gradient into curvature" | "converts … into curvature" | The entropy gradient is horizon-defined. It is admitted under F5. Under F4 it is admitted only if it is not a source term (see GR:528–530). |
| GR:528–530 | "requires a non-oscillating gravitational source … The entropy displacement satisfies this requirement"; "(i) its effective density is taken as `ρ_E ≈ Ω_CDM ρ_crit` … (ii) … a gravitational effect at the horizon, not a fluid component; (iii) it grows under its own gravity … (iv) … has the same source term as CDM" | source term | Under F4, `ρ_E` is a horizon-defined source and is unrealizable on Reading G. Under F5, admitted. |
| GR:532 | "the Jacobson sourcing is spatially local" | "sourcing" | Vocabulary consistent with both. |
| GR:581 | "correspond to differences in the coupling structure of φ, which the Jacobson derivation reads as curvature"; "a property of the partition geometry, not of the dynamics, and therefore, on the geometry-first proposal of §6.2 and conditional on its open coupling step, does not source curvature" | "reads as"; "source" | Mixed. The non-sourcing clause is stated on the geometry-first proposal. Its ground for non-sourcing is partition-definedness, which would also class `ρ_Z` as non-source (§6 node F4-5). |
| GR:695 | the Newtonian field from holographic equipartition, `a = GM/r²` | horizon quantities in the derivation and in `G` | Not at stake. The law's source is the mass. |

**Result [P].** The corpus's uses do not select between F4 and F5.

- The source vocabulary is consistent with F4.
- The matching relations and the route to Einstein's equations are consistent with F5.
- Uniform F4 classes the corpus's metric-dependent sources as sources, as its vocabulary does, so K3 is
  green. On Reading G, F4 then makes those sources unrealizable. That is F4's cost (§6 node F4-5).

***

## 3. The analysis

### 3.1 Lemma U

**Premises.**

- N1–N2-G: `g ⊳_G Π` (GR:40; GR:346 s.1–s.2) [P].
- N3-G: `Π ⊳_G r` (GR:342 "QM is emergent"; GR:344) [P].
- N3′: `r ⊳_G t`, or, for the witness, `g ⊳_G A ⊳_G ρ_Z` through the horizon area [P].
- Transitivity of ⊳_G [P].
- N5-G [P; Reading G's premise].

**Statement.** At any world satisfying these premises, `¬(t ⊳_G g)`. [A]

**Proof.** `g ⊳_G t` by transitivity. If `t ⊳_G g` as well, then `g ⊳_G g`, against N5-G. ∎

**Status.** Lemma U is the inference N1–N3 + N5 ⊢ ¬N4 that unit 2(a) states as Reading G (U2Ar3:277–284),
specialized to a law term. It shows that no world in which such a term grounds the metric is an OI world.
Whether the witness's law requires such a term depends on the formalization. On F5 the same step covers
`G_μν[g]`. Unit 2(a)'s C2(b) admits the nonlinearity because it "runs through … no emergent relatum"
(U2Ar3:485). That classification does not presuppose co-constraint.

### 3.2 Corollary E

- F1 is false at every OI world (Lemma U) [A].
- F2(K) holds if and only if no OI world realizes `K`'s law [A]. *Proof.* If none does, F2(K) holds
  vacuously. If some `w` does, Lemma U gives `¬(t_w ⊳_G g_w)`. ∎
- **Reading.** On F5's view, B_G read per world is exactly the witness's non-realizability. It supplies
  no exclusion of its own [A]. F1 and F2 are therefore not formalizations of co-constraint. They are B_G
  evaluated on it (R-4).

### 3.3 F3: a fundamental governing law

F3 contradicts P-D [P]:

- Main:44: evolution is "iteration of a single transition map";
- Main:54: Lemma 3, `φ` is a bijection;
- Structure.md:136: A1–A6 list no gravitational law.

This is (b2), and it uses no premise from the excluded list.

### 3.4 F4 and F5

**F4, stated invariantly.** The witness's equation can be written as
`G[g] + (Λ_c + 8πGρ_Z) g = 8πG T^cl`. A version of F4 keyed to "the right-hand side" would classify a
presentation, not a law [A]. F4 is therefore stated on **energy content**: every term of the realized
equation other than the Einstein tensor, taken as the scalar energy density and pressure it carries,
grounds the curvature.

- A constant Λ term, or `T^cl` with its energy content defined on the microstate (GR:340 s.2; W1-0, an
  assumption, U1r5:158), is grounded in nothing metric-dependent: no cycle.
- The witness's `ρ_Z` is defined from the class (U1r5:222–225), so it is grounded in `g` (N3′, B4): a
  cycle by Lemma U.
- This holds under Z_0 as well. There the value is constant, but the quantity is still defined from the
  class (N3′), consistent with U2Ar3:696.

**What F4 gives [A] given F4 and Lemma U's premises.** At an OI world the witness's law cannot hold. On
Reading G, GR:346 then excludes the witness.

**Is F4 admissible? [P]**

- **Controls.** K1–K5 are green (§5).
- **Premises cited against F4.**
  - P-D: not contradicted, since F4 is not fundamental.
  - GR:342: not contradicted, since mediate grounding is permitted.
  - SM:158 and GR:162: not contradicted, since one is hypothetical and the other is used, not derived.
- **Its cost on Reading G** is the unrealizability of the corpus's metric-dependent sources (§6 node
  F4-5).
  - The cost reaches the running-vacuum channel without §8.3. With §8.3 it is undetermined for that
    channel, leaning to exclusion (§6 node F4-5).
  - The corpus does not state the channel's sourcing as a premise. GR:374 requires "some state
    dependence on cosmological geometry", which concerns dependence, not sourcing. GR:400 does not
    adjudicate whether the running is a source. The functional form is "not derived" (GR:633). The Type
    II channel is "a structural reading, not a derived law" (GR:354) (§6 node F4-8).
  - The cost is therefore not a (b2) rejection on the present premise base.
- **Verdict.** F4 is admissible.

**F5.** F5 passes K1–K5 (§5), and no premise outside the excluded list contradicts it. At every OI world
where the witness's law holds, Lemma U entails F5's clause `¬(t ⊳_G g)`. F5's admissibility does not rest
on any world being unrealized. The common base is `(S, φ, x₀)`, by GR:342 for `g` and by Main:690 with
N1–N3-G for `ρ_Z`. F5 is admissible [P].

### 3.5 Application to K_cpl^free

Its term `e_free` is fixed on shell by the field equation as a free coordinate (U1r5:352–355), which unit
1 treats as a relabelling (U1r5:419–421). Under F5, Reading G does not exclude it. Under F4, whether
`e_free` is grounded in `g` is not examined (QB5(e)).

***

## 4. The reduction to G3

### 4.1 Status and derivation

- **Status [P].** By P-D, a boundary law that holds, holds in virtue of `(S, φ)`'s realization. This is
  fixed without G3.
- **Derivation.** Which covariant equation the substratum yields is G3 (GR:12; GR:162; GR:697 (ii)), and
  it is open.
- **Unit 2(a)'s condition.** It reads: "the boundary metric's law is a coarse-grained consequence of `φ`
  in which the realized metric is grounded in `(S, φ)` directly" (U2Ar3:548–549). Its "That is G3"
  (U2Ar3:535–536) runs the two senses together.
  - Status settles the ultimate ground.
  - It does not settle "directly", which excludes mediate grounding through the source term.
  - "Directly" is B_G, here F4 against F5 [P].

### 4.2 What the corpus says about derived laws

- **Passages consistent with co-constraint for the corpus's derived matching relations:** SM:158
  (hypothetical), Substratum.md:387, GR:144 and GR:581 ("reads as curvature").
- **Passages consistent with sourcing as grounding:** GR:340 s.2, GR:352, GR:358, GR:400, GR:528–530,
  GR:532 and GR:581 ("does not source curvature").
- Main:686–692 is an analogy about reduced quantum descriptions, not a statement about laws.
- A wider search (NOTES-BG-r3 §3) finds no passage that states whether a law's source terms ground its
  solutions. Unit 2(a)'s statement (U2Ar3:538) stands as worded [P].

### 4.3 How far the residual reduces to G3

- **Where the witness's dependence sits [P].**
  - On a divergence-free law in which the uniform term is a source (unit 1's class 𝒞_div,
    U1r5:198–204), the dependence sits in a source term.
  - On the corpus's conditional Jacobson route (SM:160–162), a uniform term contributes
    `ρ g_μν k^μ k^ν = 0` [A] (U1r5:603–605). The dependence can then enter only through the datum that
    selects the integration constant (U1r5:596–600).
  - Which form the G3 law takes is open.
- **F4's reach.** F4 as stated (§3.4) covers a uniform term of the realized equation, so it reaches a
  selection of `Λ_int` through `ρ_Z` on either route. Only F4-null (§6 node F4-6) leaves the witness
  unreached, and it does so on either route, because the null flux of `ρ g_μν` vanishes algebraically.
  The route bears on which scope is natural: on the Jacobson route the null flux is the source input,
  and on a divergence-free sourcing law the whole right side is the source. The premise base does not
  fix F4's scope [P].
- **The reading is not entailed by the route.** On the equation-of-state route the standard reading is
  co-constraint [L, recalled]. That is a reading, and the route is used, not derived (GR:162) [P].
- **The determination question remains on either reading.** Does some substratum satisfying OI's
  premises have a boundary law of K_cpl^conv form with a fixed constant (cf. U2Ar3:697–702,
  world-equivalence)? If such a law were derived, would its `Z` be a consequence of `φ` (unit 2(a)'s
  QU5(b), U2Ar3:847–848)?

***

## 5. Controls

| Control | F5 (CoC-content) | F3 | F4 (as stated) | Status |
|---|---|---|---|---|
| K1 | A C1-type metric (value `g_{R*}`) is grounded in `r` by its nature: cycle, excluded. The witness is not excluded. [A] | excluded | excluded | green |
| K2(a) K_dec | admitted [P] | not reached | energy content grounded in the microstate; admitted [P] | green |
| K2(b) nonlinearity | `G_μν[g]` not grounding (Lemma U) [A] | not reached | Einstein tensor not grounding, by F4's statement [P] | green |
| K2(c) gap equation | co-constraint (GR:144) [P] | not reached | no source term [P] | green |
| K3 | §2.4: every use is admitted [P] | — | §2.4: uniform F4 classes the corpus's metric-dependent sources (GR:374–380, GR:384 as a term, GR:400 Readings 1 and 2, GR:528–530) as sources, as the corpus's vocabulary does. Green for uniform F4. Their unrealizability on Reading G is a cost (F4-5). For F4-c, each candidate class examined fails K3 or K4 or does not cover the cases (§1.3, F4-5). The candidates are not shown to be exhaustive, so K3 for the schema is undetermined. [P] | green for F5, F3 and uniform F4; undetermined for F4-c |
| K4 | Lemma U and Corollary E use N1–N3-G, N3′, transitivity, N5-G and the witness's definition. None is excluded. [A] | Main:44, Main:54, Structure.md:136 only [A] | F4 is assessed, not used as a premise of any verdict. Its vocabulary sources include excluded paragraphs, which are cited as vocabulary. [P] | green |
| K5 | K1's pair has equal ⊳_D graphs and differs in ⊳_G. [A] | — | the same [A] | green |

The undetermined K3 for F4-c does not decide the outcome while uniform F4 is admissible. It would decide
it if uniform F4 were rejected (§6 node F4-8).

***

## 6. Pressure tests (§A.31)

The tests run depth-first. F4 is the branch favourable to decoupling, and it is tested first and with the
most skepticism. F5 follows, then the partition fork.

### 6.1 Branch F4

- **F4-1. Presentation.** A side-keyed F4 classifies presentations, not laws. The energy-content
  statement of §3.4 is invariant. Verdict: F4 survives only in the invariant form. [A]
- **F4-2. The corpus's own feedback.** GR:358's "feed back … through state-level quantities" and GR:400
  Reading 1 fall under F4-5. AW-loop stands under F4 as unit 2(a) recorded it for Reading G. [P]
- **F4-3. Relata.** If F4 is taken diachronically (energy content at `s` grounds curvature at `s′ > s`),
  the chain `g(s) ⊳_G Π(s) ⊳_G ρ_Z(s) ⊳_G g(s′)` is acyclic, and well-founded given a first slice, only if
  `Π(s)` is fixed by the metric on the slice. The witness's partition is the static patch bounded by
  GR:40's event horizon (U2Ar3:303–304). An event horizon depends on the future metric, and in exact de
  Sitter the static patch is fixed by the global Killing structure. With that partition the cycle
  returns. P-D does not exclude diachronic macro-to-macro grounding, which corrects r1's node A5.
  Verdict: diachronic relata remove the exclusion only for a variant with a slice-local partition. F4-3
  does not narrow the exclusion of the witness as defined. [P]
- **F4-4. Is F4 the conclusion in disguise?** F4 is a general claim about sources. It admits `T^cl` and
  constant terms, and it is not equivalent to (ii-G) or to the exclusion. Verdict: not an import. F4 is
  not entailed either. [P]
- **F4-5. The corpus's metric-dependent sources: F4's cost.**
  - With N3′, a term defined as a function of the metric is grounded in it, emergent or not. Under F4, a
    source term of that kind closes Lemma U's cycle. The witness's exclusion does not depend on how the
    corpus's sources are classified. Their classification decides what else F4 excludes.
  - **Cases.**
    - GR:374–380 (`Λ_eff(H)`; the emergent vacuum energy "depending on the hidden sector's volume",
      GR:374, with its `H`-dependence through `A = 4πc²/H²`, GR:378(i));
    - GR:400 Reading 1, and Reading 2's partition-geometry source where it depends on `H`;
    - GR:528–530 (`ρ_E`, with "the same source term as CDM"; but "(ii) … a gravitational effect at the
      horizon, not a fluid component");
    - GR:384's `ρ_s`, unless read as a consequence of the law (GR:426) rather than a term of it.
    - GR:695 is not a case: its law's source is the mass, and the horizon quantities enter its constants.
  - **§8.3 [P]: undetermined.**
    - **What §8.3 states.** For a relative difference, "there is a classical microstate difference
      corresponding to this energy difference … Relative differences appear in the classical
      stress-energy tensor and gravitate" (GR:573). Its examples are configuration differences at a fixed
      geometry ("An electron at rest vs. no electron"). GR:577 states the scope: mode structure producing
      relative differences "corresponds to classical microstate differences, is determined by the
      visible data, and gravitates".
    - **What F4 does under §8.3 depends on the counterpart.**

      | The gravitating item is … | Under F4 |
      |---|---|
      | a fixed-cell microstate quantity, as in GR:573's examples | admitted: N3′ does not apply, and covariation with `H` is ⊳_D (§2.2, K5) |
      | a total over the partition-selected hidden sector | excluded, by F4-7 |
      | the emergent computation as defined, with no relocation | excluded, by N3′ |

    - **The running channel.** The corpus describes its `H`-dependence as a hidden-sector quantity: "a
      state-level quantity depending on the hidden sector's volume" (GR:374; also GR:358), inherited
      through `A = 4πc²/H²` (GR:378(i)). On that stated mechanism the counterpart is a set-level total,
      and F4-7 excludes it. The status leans to exclusion.
    - **GR:400 Reading 1's curvature-response piece.** The corpus specifies no classical counterpart for
      it.
    - **Epoch-differential pieces generally.** The corpus fixes the counterpart for none of them. Their
      extension to §8.3 "rests on GR:400's statement and not on a derivation" (U1r5:506).
    - **Status.** Under §8.3, F4's treatment of Reading 1 and of the running channel is undetermined,
      and for the running channel it leans to exclusion.
    - **Scope of this branch.** It rests on the geometry-first identification (U1r5:504–505), whose
      clause GR:575 is excluded as a premise.
    - **The witness is excluded in either branch.** Its realized value `ρ_Z(R*)` is absolute
      (`R₀ = R*`, U2Ar3:469). §8.3's correspondence is stated for relative differences only, so with
      no relocation `ρ_Z` stays as defined from the class (U1r5:222–225), and N3′ applies.
  - **Carve-outs (the schema F4-c, §1.3).** A carve-out needs a difference relevant to grounding.
    - Partition-definedness covers `ρ_Z`, so it does not yield an F4-c; removing `ρ_Z` from it ad hoc
      fails K3. `ρ_Z` is partition-defined (B4), and GR:581 gives that ground,
      on the geometry-first proposal, for the absolute baseline not sourcing. A carve-out drawn there
      would put `ρ_Z` on the non-source side.
    - "Emergent against classical" fails K4, because it is GR:575's excluded clause.
    - "Relative against absolute" reduces to the §8.3 counterpart question above. A difference, as
      defined from metric-defined values, is itself grounded in `g` by N3′.
    - "A consequence of the law, not a term of it" (GR:426) is relevant to grounding for `ρ_s`. It does
      not apply to `ρ_E` (GR:530 (iv)) or to `Λ_eff(H)`.
    - For the running channel in particular: without §8.3, a carve-out that admits it and excludes the
      witness must separate two quantities of the same kind, emergent vacuum energies depending on `H`
      through the mode count (U2Ar3:690–691). With §8.3, K3 makes it admit the witness's R-dependence
      too, which unit 2(a) found to be 'the same kind of piece that Reading 1 feeds back'
      (U2Ar3:692–693). The witness is then excluded only through its absolute part (above), and the
      separation needed is the relative/absolute one, which reduces to the counterpart question.
  - **Verdict.** Uniform F4 is admissible.
    - On Reading G it makes the corpus's metric-dependent sources without a fixed-cell classical
      counterpart unrealizable, along with the witness. That is the tension the corpus carries between
      GR:581 and GR:384 and GR:528–530 (AW-entropic).
    - Whether a grounded carve-out exists is open. F4-c's K3 is undetermined. [P]
- **F4-6. Route and scope.** On the Jacobson route the source term is the null flux, and a uniform term
  has none (U1r5:603–605) [A]. The question then moves from a source term to the relation that selects
  the integration constant (U1r5:596–600).
  - F4 as stated covers the energy content of a uniform term of the realized equation, the Λ term of
    SM:162 included, so with Lemma U it excludes a selection through `ρ_Z`.
  - **F4-null,** an F4 restricted to the null-flux source term, does not reach the witness on either
    route. On a divergence-free sourcing law, too, the null flux of `ρ g_μν` vanishes, since
    `g_μν k^μ k^ν = 0` algebraically [A]. With respect to the witness's uniform term it is CoC-content.
  - Verdict: the route decides where the witness's dependence sits. It bears on which scope of F4 is
    natural: the null flux is the source input on the Jacobson route, and the whole right side is the
    source on a divergence-free sourcing law. Reach is fixed by the scope: F4 as stated reaches the
    witness on both routes, and F4-null on neither. The premise base fixes neither scope. [P]
- **F4-7. The label escape.** Could a partition-defined quantity be grounded in the substratum cells that
  the metric picks out, with the metric only selecting which cells count? Under N1–N2-G the partition's
  membership is partly grounded in `g`. A quantity of the picked-out set, such as a count, a total or a
  density over it, is grounded in the set, and so in `g`. Only the state of a fixed cell escapes.
  Verdict: no escape for set-level quantities such as `N_modes` or `ρ_s`. [P]
- **F4-8. Cost or (b2)?**
  - **The cost.** Under uniform F4 on Reading G, the running-vacuum channel's `H`-dependence
    (GR:374–380) and GR:400 Reading 1 are unrealizable without §8.3. With §8.3 they are undetermined,
    and the running channel leans to exclusion (F4-5). Reading 2's source is excluded wherever it depends
    on `H`.
  - **The status of the channel in the corpus.**
    - GR:374 requires "some state dependence on cosmological geometry" of the emergent vacuum energy.
      That concerns dependence, not sourcing.
    - Whether the running is a source is the question GR:400 states in two readings and does not
      adjudicate.
    - Its functional form is "not derived" (GR:633).
    - The Type II channel is "a structural reading, not a derived law" (GR:354).
  - **What follows if the channel's sourcing were held as a premise.**
    - Uniform F4 would be rejected by (b2), wherever its exclusion of the channel holds: without §8.3,
      and with §8.3 if the counterpart is a hidden-sector total.
    - F4-c, whose K3 is undetermined, would then decide the outcome, which by §1.4 is (C) with K3 named.
    - The outcome would be (B) only if no grounded carve-out exists, that is, only if F4-c fails K3 for
      every class.
  - **Verdict.** On the present premise base this is a cost, not a rejection. Whether the channel's
    sourcing is held as a premise is an owner question (QB7(a)). [P]

**Branch F4 result.** F4 is admissible.

- It excludes the witness on Reading G, for the witness as defined, within its scope (F4-6).
- Its cost is the unrealizability of the corpus's metric-dependent sources without a fixed-cell classical
  counterpart. That includes the running-vacuum channel without §8.3, and undetermined, leaning to
  exclusion, with §8.3.
- F4 is not entailed by the premise base. [P]

### 6.2 Branch F5

- **C-1. Is F5 the regularity view by assumption?** Yes. F5 states it (R-4), and it is admissible, not
  entailed. [P]
- **C-2. Does SM:158 or GR:162 entail F5?** SM:158 is hypothetical ("would … were"), and GR:162 states the
  route as used, not derived. Verdict: no. [P]
- **C-3. Does Substratum.md:385–389 entail F5?** Its separation clauses are excluded (R-2). Verdict: not
  used. [P]
- **C-4. Overdetermination.** Under F5, Lemma U excludes any edge `t ⊳_G g` whatever other grounds `g`
  has [A].

**Branch F5 result.** F5 is admissible and not entailed. [P]

### 6.3 Other nodes, re-evaluated

- **A2.** GR:340 s.1 is excluded as a premise. No bearing.
- **A3. Strong emergence.** Downward grounding of micro states contradicts P-D (`x(s′) = φ^{s′−s}(x(s))`)
  [P]. Macro-to-macro grounding is F4.
- **A4. Convention.** If a derived law had K_cpl^conv's form, would its `Z` be fixed by `φ`? That is
  unit 2(a)'s QU5(b).
- **A6.** AW-metric (§9).
- **B1.** N5-G: the verdict is scoped to Reading G.
- **B2. The partition's ground.**
  - (β) GR:40 and GR:346: the partition is defined by the metric's causal structure.
  - (α) Main:48, Lemma 2: "the definition of embedded observation", with no metric; Main:26 speaks of
    causal reach without a metric; GR:40 says the horizon "implements" it.
  - In case α Lemma U does not apply, and B_G is idle. AW-part.
- **B4. Lemma U without N3′.** `g ⊳_G A ⊳_G ρ_Z` through the horizon area (U2Ar3:306–313).

**§A.31 fixed point.** Not claimed. Passes from r3 on:

- pass 7 (r3: F4-5 reassessed with N3′; F4-7; F4-8) confirms 1 NEW, BG-F6, which CONFIRM-BG-r2 BC-3 first
  reported;
- pass 8 (r3: F4-3 and F4-6 re-run) yields 0 NEW;
- pass 9 (r4: the §8.3 counterpart cases; F4-c; F4-null's reach) yields 0 NEW.

Two consecutive passes without a NEW finding is short of the 3–4 the fixed point requires.

***

## 7. Verdict from the rule

- **Grounding-content formalizations.**
  - F3 is rejected by (b2), P-D (§3.3).
  - Uniform F4 is admissible (§3.4, §6.1).
  - F4-c has K3 undetermined (§1.3, §6 node F4-5). That does not decide the outcome while uniform F4
    is admissible.
- **CoC-content formalizations.** F5 is admissible (§3.4, §6.2). F1 and F2 are B_G on F5's view and fail
  by Corollary E.
  - F4-null is CoC-content with respect to the witness's term (R-6). Its controls are not assessed here;
    it does not decide the outcome while F5 is admissible, and it would have to be eliminated, with F5,
    for (A).
- **Controls.** Green for F3, F4 and F5 (§5).
- **Outcome: (C).** Both kinds remain admissible. Under the repaired rule this is the outcome whenever the
  premise base is silent on whether a derived law's source terms ground its solutions.
- **The residual.** F4 against F5.
  - Under F4, Reading G excludes the witness's law, for the witness as defined, unless the partition is
    slice-local and the relata diachronic (F4-3), and within F4's scope (F4-6). F4's cost is F4-5 and
    F4-8.
  - Under F5, Reading G excludes no field equation whose metric has a ground in `(S, φ, x₀)`, and what
    remains is G3's determination question.
  - The route decides whether the witness's dependence sits in a source term or in the selection of the
    integration constant. It bears on which scope of F4 is natural. Reach is fixed by the scope, which the
    premise base does not fix: F4 as stated reaches the witness on both routes, and F4-null on neither
    (§4.3).
  - If the running channel's sourcing were held as a premise (QB7(a)), uniform F4 would be rejected by
    (b2) wherever it excludes the channel: without §8.3, and with §8.3 unless the answer to (b) is a
    fixed-cell quantity. F4-c's undetermined K3 would then decide the outcome: (C) with K3 named. It would be (B) only if no
    grounded carve-out exists (§6 node F4-8).
- **Withdrawn.**
  - r1's outcome (B).
  - r1's claim that B_G "does not reduce to G3".
  - r2's statements that F4's exclusion is confined to a divergence-free sourcing law and needs
    synchronic relata.
  - r3's statements that §8.3 admits GR:400 Reading 1 and the running channel's `H`-dependence under
    F4, that holding the channel as a premise gives (B), and that F4-null reaches the witness on one
    route.

**Productivity (§1.5).** The result is strictly stronger than unit 2(a)'s gap.

- Corollary E shows that B_G read per world adds nothing to the exclusion.
- The gap moves to F4 against F5, with F4's scope and cost stated.
- Under F4, Reading G's exclusion is indifferent to emergence (BG-F6). That exposes an assumption and
  constrains how unit 2(a)'s and unit 1's gap is worded.
- The unit meets the test.

***

## 8. Consequences

All items are conditional on the gap of §7. None adopts a premise, proposes a manuscript change or edits
a record. The witness keeps the de Sitter and M1 scope.

### 8.1 Requirement (ii) and (ii-G)

- **Given F5:** on Reading G, requirement (ii) excludes C1-type configurations and no semiclassical
  boundary law, as on Reading E (U2A-F7) [P].
- **Given F4:** on Reading G it also excludes every source term defined as a function of the metric,
  emergent or classical. With §8.3 in force, a relative piece whose classical counterpart is a fixed-cell
  microstate quantity is admitted. The corpus fixes that counterpart for no epoch-differential piece
  (node F4-5) [P].

### 8.2 (ii-L)

- Unchanged from unit 2(a) on Readings E and D (U2Ar3:684–696).
- The candidate motivation through GR:342 read as N5-G (U2Ar3:82–85, :829–832) is conditional on F4. It
  carries F4's cost [P].

### 8.3 (DZ)

- (DZ) for the convention-fixed offset is supported by GR:346 on Reading G given F4, within F4's scope
  and at F4's cost.
- Otherwise it rests on:
  - G3, by determination;
  - the posits P11, GR:575 or (ii-S);
  - (ii-L) as an added premise. [P]

### 8.4 Unit 1 Part 2

- CORR r1 and r2 state Part 2 as conditional "on Reading G of GR:346 and the bridge premise B_G (open)".
- This record narrows B_G to F4 against F5 and does not settle it. Part 2's conditional form stands.
- CORR's clause on B_G's conditions would read with §4.1:
  - the status sense is fixed by P-D;
  - "directly" is F4 against F5;
  - G3's route bears on which scope of F4 is natural, and does not fix its reach;
  - the corpus states no view on whether source terms ground.
- Forward notes are held (QB2). Unit 1 Part 1 is unaffected under F5; K_cpl^free under F4 is not examined.

### 8.5 Unit 2(a)

- Under unit 2(a)'s rule, Reading G meets (B)(b) in case β given F5. Given F4 it meets (A) for the
  witness. While F4 against F5 is open it meets neither.
- Unit 2(a)'s outcome stays (C), with its gap narrowed to F4 against F5.
- Its §8.3 rows (U2Ar3:469–470) and AW-loop (U2Ar3:715–720) are unchanged until the gap closes [P].

### 8.6 What does not change

- The witness, its algebra and its scope.
- Unit 2(a)'s findings on Readings E, D and S.
- U2A-F2.
- The world-equivalence.
- GR:579's open question.
- G3's open status.
- No claim about Λ.

***

## 9. Findings

Identifiers are kept across revisions.

| ID | Finding | Class | Support |
|---|---|---|---|
| BG-F1 | Lemma U is Reading G's reductio specialized to a law term. Corollary E: on the co-constraint view, B_G read per world is exactly the non-realizability of the witness's law, and adds nothing to the exclusion. | ELABORATING | [A] §3.1–3.2 |
| BG-F2 | Unit 2(a)'s condition (a) ran together the status of a law (fixed by P-D) with its derivation (G3). The status sense does not settle "directly", which is B_G. The corpus contains passages consistent with co-constraint (SM:158, Substratum.md:387, GR:144, GR:581) and sourcing language consistent with grounding (GR:340, :352, :358, :400, :528–532, :581). It states no view on whether a law's source terms ground its solutions. | ELABORATING | [P] §4.1–4.2 |
| BG-F3 | The governing reading (F3) contradicts the single-bijection dynamics (Main:44, :54; Structure.md:136). | CONFIRMING | [P] §3.3 |
| BG-F4 | Given F5, on Reading G requirement (ii) excludes the C1-type configuration and no semiclassical boundary law (as U2A-F7). Given F4, it also excludes every source term defined as a function of the metric. | ELABORATING (conditional) | [P] §8.1 |
| BG-F5 | B_G narrows to F4 against F5. For the witness as defined (event-horizon partition), F4 excludes its law on Reading G. Diachronic relata escape only with a slice-local partition. G3's route decides whether the witness's dependence sits in a source term or in the selection of the integration constant. F4 as stated reaches both; F4-null reaches neither. The route bears on which scope is natural, and does not fix it. | ELABORATING | [A] null flux; [P] §4.3, §6.1 |
| BG-F6 | Under F4, Lemma U's cycle is indifferent to emergence: every source term defined as a function of the metric is unrealizable on Reading G. The corpus's own metric-dependent sources are at stake: GR:384 as a term, GR:400 Reading 2 where `H`-dependent, and GR:528–530, in either §8.3 branch; GR:400 Reading 1 and GR:374–380, excluded without §8.3 and undetermined with it (leaning to exclusion for GR:374–380, by F4-7). No carve-out relevant to grounding is stated, and partition-definedness fails because `ρ_Z` is partition-defined. | NEW (candidate; first reported in CONFIRM-BG-r2 BC-3; assumption-watch AW-entropic) | [P] §6.1 F4-5, F4-7, F4-8 |

**Assumption-watch markers.**

- **AW-part (B2).** The partition is grounded in the observer's embedding (Main:26, Main:48) or in the
  metric's causal structure (GR:40, GR:346). Reading G's reductio needs the second. Sites: GR:40,
  GR:346 s.1–s.2, book/ch07-gravity.md:183. No change is proposed.
- **AW-metric (A6).** GR:693 calls the metric "the framework's *own* emergent-metric geometry". If the
  metric's definition passes through the emergent description, Reading G's reductio applies to OI's own
  metric. Sites: GR:693, GR:340 s.1, GR:342. No change is proposed.
- **AW-entropic (BG-F6).** Wherever the corpus places a metric-defined quantity in the role of a source,
  a grounding reading of sources meets Lemma U on Reading G. Sites: GR:374–380, GR:384, GR:422–426,
  GR:482, GR:528–530 and GR:400; against them GR:581. No change is proposed.
- **AW-ground (U2Ar3:760–766).** Substratum.md:385 and :393 read as ⊳_D under N5-G.

***

## 10. Literature

All entries are recalled and were not re-read. No verdict rests on any of them.

- K. Fine, "Essence and modality" (1994); K. Fine, "Guide to ground" (2012); G. Rosen, "Metaphysical
  dependence: grounding and reduction" (2010).
- E. Bliss (2014) and N. Thompson (2016): dissent from well-founded grounding.
- T. Jacobson, "Thermodynamics of spacetime: the Einstein equation of state", *Phys. Rev. Lett.* 75,
  1260 (1995).
- D. Lewis on Humean supervenience; T. Maudlin, *The Metaphysics Within Physics* (2007); D. Armstrong,
  *What Is a Law of Nature?* (1983); and the Humean-explanation debate: the regularity and governing
  views that F5 and F3/F4 instantiate.
- The strong-emergence literature (node A3).

***

## 11. Owner questions

- **QB1. Unit 2(a)'s rule.** Re-applied, it leaves unit 2(a) at (C), with the gap narrowed to F4 against
  F5. Is a forward note on its gap wording wanted, or is this record enough?
- **QB2. Forward notes.** Should forward notes to unit 2(a) r3 and CORR r2 wait until F4 against F5 is
  settled, or should the narrowed wording of §8.4 be carried now?
- **QB3. QU2 follow-up.** The candidate motivation of (ii-L) and (ii-G) through Reading G is conditional
  on F4 and carries F4's cost. Does Q7 stay open on that basis?
- **QB4. QU3 follow-up.** Two scopings for GR:346, GR:342 ("forced") and book/ch07-gravity.md:183–187 are
  available to a future manuscript unit:
  - given F5, requirement (ii) excludes only metrics that are quantities of the emergent description;
  - given F4, it also excludes every source term defined as a function of the metric, including the
    corpus's §7.1–§7.3 constructions unless a grounded carve-out is found (§6 node F4-5).

  No change is proposed.
- **QB5. Next unit.** Candidates:
  - (a) F4 against F5: a paper-only audit of the source terms in GR:374–380, GR:384 and GR:422–426,
    GR:528–530, GR:400 and SM:144–162; of GR:581's ground against GR:384; of F4's scope (law terms, or the
    energy content of the realized equation, F4-6); of a specified class for F4-c (§1.3); of GR:577's
    scope clause and the classical counterpart of an epoch-differential piece under §8.3 (F4-5); and
    of whether the G3 target (GR:12) is a divergence-free sourcing law or a null-flux route;
  - (b) AW-part;
  - (c) AW-metric;
  - (d) unit 2(a)'s QU5(b);
  - (e) K_cpl^free under F4.
- **QB6. The rule.** This unit's decision rule was repaired at r2 and r3, after reviews that named the
  expected outcome, and its remaining edits were recorded at r4 (§1.6). Is the repaired rule accepted as
  the rule of record for this unit? Should the next unit's rule be fixed and reviewed before its
  analysis starts (§A.29)?
- **QB7. The F4 cost.** Two questions decide how F4-8 and F4-5 read:
  - (a) Is the sourcing of the running-vacuum channel (GR:374–380) to be held as a premise? The corpus
    requires its state dependence (GR:374) but leaves its sourcing unadjudicated (GR:400), with its form
    "not derived" (GR:633). If it is held, uniform F4 is rejected by (b2) wherever it excludes the
    channel: without §8.3, and with §8.3 unless the answer to (b) is a fixed-cell quantity. The outcome is
    then (C) with F4-c's K3 named. It would be (B) only if no grounded carve-out exists (§6 node F4-8).
  - (b) Under §8.3, is a relative epoch-differential piece's gravitating item a fixed-cell microstate
    quantity, a total over the hidden sector, or the emergent computation as defined? Under F4 the first
    is admitted, and the other two are excluded (§6 node F4-5).

***

## 12. Limits

- The logic is by hand.
- Lemma U holds on Reading G in case β, conditional on N5-G.
- F4 and F5 are readings [P]. Neither is entailed by the premise base.
- The rule was repaired at r2 and r3 after reviews that named the expected outcome, and its edits were
  recorded at r4 (§1.6).
- Under §8.3, F4's treatment of epoch-differential pieces is undetermined (QB7(b)).
- The rule and the analysis land in one commit.
- The §A.31 fixed point is not reached.
- No claim is made about K_cpl^conv's admissibility under G3, or about Λ.
