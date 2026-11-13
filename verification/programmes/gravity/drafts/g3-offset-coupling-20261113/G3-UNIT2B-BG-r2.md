# G3 unit 2(b) (r2): the bridge premise B_G, grounding or co-constraint

**Scope.** This is a paper-only investigation under Issue #873, continuing units 1 and 2(a) (PR #1275).

- Authorization: #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU5: "a bounded, paper-only
  investigation of B_G: whether a term in the boundary-metric law that depends on the emergent class
  grounds the metric or only co-constrains it, including how far this reduces to the status of the
  boundary law under G3. … It adopts no premise, makes no manuscript change, involves no Lean build and
  makes no claim about Λ."
- **Revision history.**
  - r1 is `G3-UNIT2B-BG-r1.md` at `4acb3a49a73898d7ceb67c7f503d72c4597e34d6`.
  - Its independent review is `REVIEW-BG-r1.md` at `1970a36a`, verdict REVISE (one blocking finding,
    BG-1).
  - r2 answers it. Dispositions are in `RESPONSE-BG-r1.md`.
  - r1's outcome (B) is withdrawn. r2's outcome is (C) (§7).
- Inputs on branch `research/g3-offset-873-20261113`:
  - unit 2(a) r3, `G3-UNIT2A-r3.md` at `1ad01923` ("U2Ar3:n" is its line n);
  - unit 1 r5, `G3-UNIT1-r5.md` ("U1r5:n");
  - the unit 1 forward corrections `G3-UNIT1-CORR-r1.md` and `G3-UNIT1-CORR-r2.md` (the latter at
    `d4fe24be`);
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
- The witness is the K_cpl^conv fixed-point model on the de Sitter family under M1 (U2Ar3:291–419).
- **B_G** is: "a term of the boundary metric's law that is a function of the emergent class grounds the
  realized metric, and does not only co-constrain it" (U2Ar3:285–287).

***

## 0. Verdict

**Outcome (C), with the gap narrowed. Scope: Reading G of GR:346 with N1–N3 read in ⊳_G (case β, §6
node B2), conditional on N5-G.** The rule used is r1's rule as repaired at review (§1.6). r1's rule could
not return (A), and the repair is stated as a repair.

- **What is established.**
  - **Lemma U** (§3.1) [A], given its premises. A law term grounded in the realized metric cannot ground
    that metric. This is Reading G's own reductio, specialized to law terms.
  - **Corollary E** (§3.2) [A]. Read as a per-world claim, B_G holds exactly when the witness's law is
    realized at no OI world. Read that way, B_G adds nothing to the exclusion it was meant to supply.
  - **F3 is refuted** (§3.3) [P]. A fundamental governing gravitational law contradicts the single
    bijection (Main:44, Main:54; A1–A6 at Structure.md:136).
- **The gap (§3.4, §4).** Whether the boundary law's source term **grounds** the metric (F4,
  non-fundamental sourcing as grounding) or **co-constrains** it (CoC).
  - **Under F4**, Lemma U turns into an exclusion: no OI world realizes the witness's law, while P11's
    classical source is admitted [A] given F4. That holds only on three further conditions [P]:
    - the grounding relata are synchronic or whole-history, not slice-to-later-slice (§6 node F4-3);
    - the law is a divergence-free law in which the uniform term is a source (§6 node F4-6);
    - the corpus's partition-defined gravitational quantities are classed as non-source
      intermediaries (§6 node F4-5).
  - **Under CoC**, Reading G excludes no field equation whose metric has a ground in `(S, φ, x₀)`. What
    remains about the witness is then G3's determination question [A] given CoC, [P] for the residual.
  - **No premise outside the excluded list selects either.**
    - The corpus's sourcing vocabulary (GR:340, :352, :358, :581, :400) is consistent with F4, and it
      sits in the paragraphs of the geometry-first proposal.
    - The corpus's Jacobson route (GR:162, SM:160) reads the law as an equation of state, which
      supports CoC [L, recalled]. That route is "used … not derived" (GR:162).
- **How far the gap reduces to G3 (§4).**
  - The *status* sense of "derived" is fixed by P-D for any boundary law that holds: the law holds in
    virtue of `(S, φ)`'s realization [P].
  - P-D fixes the ultimate ground only. It does not settle whether the metric is grounded in `(S, φ)`
    "directly" (U2Ar3:548–549), and that is B_G.
  - The residual, F4 against CoC, depends partly on G3: which law, and by which route.
    - On a divergence-free sourcing law, F4 against CoC is live.
    - On the corpus's conditional Jacobson route, the uniform term has zero null flux (U1r5:671;
      U1r5:603–606) [A]. The witness's emergent dependence can then enter only through the datum that
      selects the integration constant, which is unit 1's R2a question (U1r5:589–606). F4, a claim about
      sources, does not reach it.
- **Controls.** K1–K5 are green for each formalization assessed, with K4 amended at review (§5).

**Scope.**

- The verdict concerns B_G and Reading G.
- It does not show that K_cpl^conv is admissible in OI. Other posits exclude it: P11, GR:575 and (ii-S)
  (U2Ar3:76–78).
- It is conditional on N5-G, which the recalled literature contests [L, recalled].
- It is conditional on case β. In case α (Main:26, Main:48), Reading G's reductio fails at N2-G, and B_G
  is idle (§6 node B2).
- The witness keeps unit 2(a)'s scope: exact de Sitter and assumption M1.

**Consequences** (§8). Each is conditional on the gap, and none edits a record.

1. On Reading G, GR:346 excludes K_cpl^conv's field equation if and only if F4 holds for the boundary
   law's source term (with the conditions above). Given CoC it excludes no field equation beyond G3's
   determination question [A] given each branch, [P] for the readings.
2. (ii-L) remains an added premise on Readings E and D, with unit 2(a)'s limits (U2Ar3:684–696). Unit
   2(a)'s candidate motivation through GR:342 read as N5-G is conditional on F4 rather than on an
   unspecified B_G.
3. Unit 2(a)'s outcome stays (C), with its gap narrowed from "B_G" to "F4 against CoC". Unit 1 Part 2
   (r5, CORR r1, CORR r2) keeps its conditional form. Forward notes are held until the gap is settled
   (QB2).

***

## 1. Decision rule

**Provenance of the rule.** §1.1–§1.5 are r1's rule, unchanged except where §1.6 states a repair.

- r1's rule was written after the sources had been read and an outline of r1's argument had formed
  (NOTES-BG-r1 §4).
- The repairs of §1.6 were written after REVIEW-BG-r1, which named the outcome it expected, (C). They
  are stated as repairs. The outcome that follows from them is reported whatever it is.
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
  - *added at review (§1.6, R-2):* the separation clauses of Substratum.md:385–389 (the metric and the
    wave function as properties of "different objects in the construction"; "Both are emergent …") and
    GR:655's clause "(a property of the classical substratum's gravitational dynamics)". These restate
    the geometry-first separation under test and are conclusion-adjacent.

### 1.2 Outcomes (as repaired, §1.6 R-1)

An **OI world** is a realization `(S, φ, x₀)` that satisfies the premise base, with the partition realized
as GR:40 states, together with the completion under test.

**Formalizations.** A formalization of B_G is classified by its **content**, meaning what the holding of
a boundary law consists in.

- **Grounding-content:** the law's holding includes the grounding of the realized metric by its source
  term.
- **CoC-content:** the law's holding is a relation among items with a common ground, and it includes no
  such grounding.
- **Admissible:** a formalization that passes K1–K5 and is not contradicted by a premise in the premise
  base.

**Outcomes.**

- **(A) B_G supported.** The premise base (premises named) leaves admissible at least one
  grounding-content formalization and no CoC-content formalization. On Reading G (N5-G, case β) the
  witness is then excluded by the content of its law.
- **(B) B_G refuted / co-constraint.** The premise base leaves admissible at least one CoC-content
  formalization and no grounding-content formalization. Each grounding-content formalization is
  rejected by (b2) a named stated premise it contradicts, or by a failed control.
- **(C) Open.** Both kinds remain admissible, or neither does. The residual is stated precisely.

**Non-vacuity, both ways.** No clause may be met by an entailment that holds only because the witness's
law is realized at no OI world. For grounding-content formalizations, non-realizability is a consequence
of their content together with Lemma U, not a premise. That is not vacuity.

### 1.3 Formalizations quantified over

- **F1 (realized, regularity view).** At an OI world `w` where the witness's law holds, its term grounds
  `g_w`. The law's holding is satisfaction of its equation, and grounding is a further fact of `w`.
  CoC-content.
- **F2 (law-level, regularity view).** For every OI world where the witness's law holds, its term grounds
  the realized metric. CoC-content in the same sense.
- **F3 (fundamental governing law).** The boundary law is a fundamental item, and its inputs ground its
  outputs. Grounding-content.
- **F4 (non-fundamental sourcing as grounding; added at review, R-3).** The boundary law is not
  fundamental. Its grounds trace mediately to `(S, φ)`. The energy content of its source term grounds the
  realized metric, and its geometric side does not. Grounding-content. §3.4 states F4 so that it is
  invariant under moving a uniform term across the equation.
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
  Substratum.md:385–393, GR:162, SM:160–162, GR:384, GR:482 and GR:400 Reading 1. A classification that
  differs from a corpus use without a stated difference relevant to grounding fails K3.
- **K4 (no import).** The premises of each decisive step are listed, and none is on the excluded list of
  §1.1.
- **K5 (grounding is not determination).** Configurations with the same ⊳_D graph must be able to differ
  in ⊳_G.

A verdict is written only if K1–K5 are green for the formalizations it rests on.

### 1.5 Productivity test (§A.31)

The unit is a gem if it yields a fact strictly stronger than unit 2(a)'s statement (B_G "open … narrowed
to the status of the boundary law (G3) and to a view of laws the corpus does not state", U2Ar3:746), and
the fact either constrains a claim or exposes a hidden assumption.

### 1.6 Repairs at review

- **R-1 (the rule was asymmetric; REVIEW-BG-r1 BG-1).**
  - r1's clause (A) required, for a formalization evaluated per world, that "at every OI world where
    [the] law holds, that term grounds the realized metric", and it barred an entailment through
    non-realizability. Its clause (b1) carried no matching bar.
  - The premise base contains N1–N3-G and N5-G, so Lemma U holds at every OI world. Clause (A) could
    therefore be met only vacuously, and that was barred, for every per-world formalization and before
    any analysis.
  - r1's rule could return (B) or (C) only. It was defective.
  - The repair (§1.2) classifies formalizations by content, applies a non-vacuity bar to both sides,
    and decides by which kinds of formalization remain admissible. Under the repaired rule, (A) is
    reachable: it obtains if CoC-content formalizations are refuted while a grounding-content one
    survives.
- **R-2 (conclusion-adjacent premises; BG-3).** The Substratum.md:385–389 separation clauses and GR:655's
  clause are added to the excluded list. r1 used them in P-F, in the A3 node and in the K3 table.
- **R-3 (missing formalization; BG-1).** F4 is added. r1's §1.3 clause "Any further formalization found
  during the analysis" already covered it. r1 did not consider it.

***

## 2. Formalization

### 2.1 Objects

- At a world `w`: the realized metric `g`; the realized partition `Π = Π(g)` (GR:40); the realized
  emergent class `r = T(Π)` (GR:344; Main:690); and the term `t = τ(r)`. For the witness, `τ = ρ_Z`
  (U2Ar3:315–328).
- **A law** is a relation `L(g, t, …) = 0` on a family of candidate configurations. For the witness it
  is `G[g] + Λ_c g = 8πG(T^cl − ρ_Z g)` (U2Ar3:342).

### 2.2 Three relations, kept apart

- **Specification (⊳_E)** and **determination (⊳_D)** are as in unit 2(a) (U2Ar3:208–213, :223–225).
- **Grounding (⊳_G)** is a relation at the realized world. It is transitive, and under N5-G it is
  irreflexive and well-founded [P; L, recalled: Fine 2012]. Configurations with the same values and the
  same ⊳_D graph can differ in ⊳_G (K5).
- **N3′.** A quantity defined as a function of another is grounded in it [P; L, recalled: Fine 1994,
  Rosen 2010]. For the witness, the horizon area alone gives `g ⊳_G ρ_Z`, without N3′ (§6 node B4).

### 2.3 Two roles for a law term

Let `L` hold at `w`, with term `t`.

- **Grounds (Gr):** `t ⊳_G g`.
- **Co-constrains (CoC):** `¬(t ⊳_G g)`, and `g` and `t` have grounds in a common base. In OI the
  candidate base is `(S, φ, x₀)`.

Neither role is fixed by ⊳_E or ⊳_D [A].

### 2.4 The corpus's uses (K3)

| Corpus use | Text | Relation stated | Reading [P] |
|---|---|---|---|
| GR:340 s.2 (P11; excluded as a premise) | "The stress-energy sourcing gravity is the classical stress-energy of the total microstate" | "sourcing" | Consistent with F4 and with CoC. The text fixes neither. |
| GR:342 | "no substance-level primitives … spacetime emerges from `[(S, φ)]/𝒢_sub`" | ultimate ground | Fixes `(S, φ)` as the ultimate ground. It permits mediate grounding among derived items, so F4 is not excluded. |
| GR:346 | N1–N2: "Causal structure is determined by null geodesics"; "derived", "entry point" | ⊳_D or ⊳_G; ⊳_E | Case β reads N1–N2 in ⊳_G (U2Ar3:279–280). |
| Substratum.md:385–389 (separation clauses excluded, R-2) | "the metric is a property of the classical dynamics of the partition boundary"; GR and QM as projections of `(S, φ)` | "property of"; projection | Not used in a decisive step. In ⊳_G, "property of the partition boundary" with N1–N2 is a cycle that involves no law term (U2Ar3:617–620). Under N5-G it must be read as ⊳_D, or as grounding in the classical dynamics of the cells that the metric picks out, for K_dec and the witness alike. |
| Substratum.md:393 | "the metric … determined by the partition geometry and the area-law theorem" | "determined" | ⊳_D. |
| GR:162 | "uses the Einstein equations through Jacobson's relation (§3.1) and does not derive them" | status: used, not derived | The route is the equation-of-state route, read as CoC [L, recalled: Jacobson 1995]. It is used, not derived. |
| SM:158 | the lattice construction: "the Clausius relation would constrain the graph's response … were the curvature step (iv) supplied"; "paralleling continuum GR where the Einstein equations are the equations of motion, not constraints on separate dynamics" | "constrain", hypothetical; the continuum parallel | Consistent with CoC for a hypothetical construction. The "equations of motion" clause is said of continuum GR as a parallel and supports P-D against F3. It says nothing on whether a source term grounds. |
| SM:160–162 | Jacobson's inputs: (i) area law, (ii) Unruh temperature of a reduced state, (iii) the energy flux `δQ = ∫T_μν k^μ dΣ^ν`, (iv) Raychaudhuri | input (iii) is the source; (i) and (ii) are thermodynamic intermediaries | Under F4, the source is input (iii). A uniform term has zero null flux (§6 node F4-6). Inputs (i) and (ii) are partition-defined: CoC under Lemma U, or non-source under F4. |
| GR:144 | "they refer to the same physical degrees of freedom: the boundary modes `V × B`" | matching | Consistent with CoC. Contains no source term. |
| GR:352 | "does not entail that it cannot source geometry … a coupling theorem" | "source" | Consistent with F4 and with CoC. "Coupling theorem" states derivation status (P-D). |
| GR:358 | "feed back into gravitational dynamics through state-level quantities … everything that contributes to `H_tot` gravitates" (in the geometry-first paragraph) | "feed back", "gravitates" | Consistent with F4 for classical energy content. Under F4, the emergent "feed back" needs a classical counterpart (§8.3). |
| GR:384; GR:422–426 | "The total gravitating boundary energy tracks the critical density at every `H` as an identity"; `ρ_s = E_s/V_H`, a horizon-defined energy | "gravitating", for a partition-defined energy | Grounded in `g` through the horizon. Under F4 it must be read as a geometric identity (it equals `ρ_crit = 3H²/(8πG)`), not as a source (§6 node F4-5). Under CoC it is an identity. |
| GR:482 | "The Jacobson mechanism converts the entropy gradient into curvature" (deep-MOND step) | "converts … into curvature", from a partition-defined quantity | Under F4, the boundary entropy gradient must be a non-source intermediary, or Reading G excludes the corpus's own §7.3 step (§6 node F4-5). Under CoC it is admitted. |
| GR:581 | "correspond to differences in the coupling structure of φ, which the Jacobson derivation reads as curvature"; "does not source curvature" | "reads as"; "source" | Mixed: CoC language for emergent relative energies, source language for the absolute baseline, on the geometry-first proposal. |
| GR:400 Reading 1 | "feeds back as a source" | "source" | Under §8.3 the piece is classical, and F4 and CoC both admit it. Without §8.3: F4 with Lemma U excludes it, and CoC admits it. |

**Result [P].** The corpus's uses do not select between F4 and CoC. Its source vocabulary is consistent
with F4 and is concentrated in the geometry-first paragraphs. Its matching relations and its route to
Einstein's equations are consistent with CoC. Its own partition-defined "gravitating" quantities (GR:384,
GR:482) require that F4 class them as non-source.

***

## 3. The analysis

### 3.1 Lemma U

**Premises.**

- N1–N2-G: `g ⊳_G Π` (GR:40; GR:346 s.1–s.2) [P].
- N3-G: `Π ⊳_G r` (GR:342 "QM is emergent"; GR:344) [P].
- N3′: `r ⊳_G t` (§2.2), or, for the witness, `g ⊳_G A ⊳_G ρ_Z` through the horizon area [P].
- Transitivity of ⊳_G [P].
- N5-G [P; Reading G's premise].

**Statement.** At any world satisfying these premises, `¬(t ⊳_G g)`. [A]

**Proof.** `g ⊳_G t` by transitivity. If `t ⊳_G g` as well, then `g ⊳_G g`, against N5-G. ∎

**Status.** Lemma U is the inference N1–N3 + N5 ⊢ ¬N4 that unit 2(a) states as Reading G (U2Ar3:277–284),
specialized to a law term. It shows that no world in which such a term grounds the metric is an OI world.
It does not by itself decide whether the witness's law requires such a term. On CoC the same step covers
`G_μν[g]`. Unit 2(a)'s C2(b) admits the nonlinearity because it "runs through … no emergent relatum"
(U2Ar3:485). That classification does not presuppose CoC.

### 3.2 Corollary E

- F1 is false at every OI world (Lemma U) [A].
- F2(K) holds if and only if no OI world realizes `K`'s law [A]. *Proof.* If none does, F2(K) holds
  vacuously. If some `w` does, Lemma U gives `¬(t_w ⊳_G g_w)`. ∎
- **Reading.** On the regularity view, which F1 and F2 build in (§1.3), B_G read per world is exactly the
  witness's non-realizability. It supplies no exclusion of its own [A].

### 3.3 F3: a fundamental governing law

F3 contradicts P-D [P]:

- Main:44: evolution is "iteration of a single transition map";
- Main:54: Lemma 3, `φ` is a bijection;
- Structure.md:136: A1–A6 list finiteness, determinism (bijection), bounded coupling degree, center
  independence, linearity and background independence, and no gravitational law.

A fundamental boundary law beside `φ` would be a second fundamental dynamics. This is (b2). It uses no
premise from the excluded list. (In case β, Lemma U independently excludes a governing input grounded in
its output.)

### 3.4 F4: non-fundamental sourcing as grounding

**Statement made invariant.** The witness's equation can be written with the uniform term on either side:
`G[g] + (Λ_c + 8πGρ_Z) g = 8πG T^cl`. A version of F4 keyed to "the right-hand side" would therefore
classify a presentation, not a law [A]. F4 is stated on **energy content**: every term other than the
Einstein tensor, taken as the scalar energy density and pressure it carries, grounds the curvature. The
tensor structure, such as `p g_μν` or the normalization of `u^μ` by `g`, does not. Under this statement:

- a constant Λ term is energy content grounded in nothing metric-dependent: no cycle;
- `T^cl`'s energy content is grounded in the microstate (GR:340 s.2; W1-0, an assumption: U1r5:158):
  no cycle;
- the witness's `ρ_Z` is energy content grounded in `g` through the horizon (§2.2): a cycle by Lemma U.

**What F4 gives [A] given F4 and Lemma U's premises.** At an OI world, the witness's law cannot hold,
because its holding includes `ρ_Z ⊳_G g` and Lemma U forbids that. On Reading G, GR:346 then excludes the
witness, and P11's classical source passes.

**Is F4 admissible?**

- **Controls.** K1–K5 are green, conditional on the K3 classification of nodes F4-5 and F4-6 (§5).
- **Premises cited against F4.**
  - P-D: not contradicted, since F4 is not fundamental.
  - GR:342, no substance-level primitives: not contradicted, since mediate grounding is permitted.
  - SM:158: the lattice construction is hypothetical, and its continuum parallel concerns P-D. Not
    contradicted.
  - GR:162 and SM:160, the equation-of-state route: this supports CoC [L, recalled], but the route is
    used, not derived. Not contradicted.
- **Verdict.** F4 is admissible [P].

**Is CoC admissible?** F1 and F2, the regularity view, pass K1–K5 (§5), and no premise outside the
excluded list contradicts them. The sourcing vocabulary is consistent with CoC, since a source term in an
equation of state co-constrains [L, recalled]. CoC is admissible [P].

### 3.5 Application to K_cpl^free

Its term `e_free` is fixed on shell by the field equation as a free coordinate (U1r5:352–355). Under CoC,
Reading G does not exclude it. Under F4, `ρ_free = ħ e_free/v` is energy content.

- On shell its value is fixed through the field equation by `g`, which is ⊳_E and ⊳_D.
- Whether `e_free` is grounded in `g` depends on whether the free coordinate is a realized fact of
  `(S, φ, x₀)` or a relabelling. Unit 1 treats it as a relabelling (U1r5:419–421).
- Not examined further. Recorded under QB5.

***

## 4. The reduction to G3

### 4.1 Status and derivation

- **Status [P].** By P-D, a boundary law that holds, holds in virtue of `(S, φ)`'s realization, since
  there is no second fundamental dynamics. This is fixed without G3.
- **Derivation.** Which covariant equation the substratum yields is G3 (GR:12; GR:162; GR:697 (ii)), and
  it is open.
- **What unit 2(a)'s condition (a) needs.** It reads: "the boundary law is a coarse-grained consequence
  of the substratum dynamics in which the realized metric is grounded in `(S, φ)` directly"
  (U2Ar3:524–527, :548–549). Its "That is G3" (U2Ar3:535–536) runs the status sense together with the
  derivation sense. Status settles the ultimate ground. It does not settle "directly", which excludes
  mediate grounding through the source term. "Directly" is B_G, which here is the F4 against CoC
  question [P].

### 4.2 What the corpus says about derived laws

- **Passages consistent with CoC for the corpus's derived matching relations:**
  - SM:158, a hypothetical lattice construction in which the Clausius relation "would constrain" the
    graph's response;
  - Substratum.md:387, projection "by averaging";
  - GR:144, "same physical degrees of freedom";
  - GR:581, "reads as curvature".
- **Passages consistent with sourcing as grounding:** GR:340 s.2, GR:352, GR:358, GR:581 ("does not
  source curvature") and GR:400.
- Main:686–692 is an analogy about reduced quantum descriptions and not a statement about laws.
- No passage states whether a law's source terms ground its solutions. Unit 2(a)'s statement that "the
  corpus states no view on this" (U2Ar3:538) stands as worded [P].

### 4.3 How far the residual reduces to G3

- **The route decides whether F4 can reach the witness [P].**
  - On a divergence-free law in which the uniform term is a source (unit 1's class 𝒞_div, U1r5:198–204),
    F4 against CoC is live.
  - On the corpus's conditional Jacobson route (SM:160–162), the source is the null flux. A uniform
    term contributes `ρ g_μν k^μ k^ν = 0` [A] (U1r5:603–605). The uniform part of the final equation is
    then the integration constant. The witness's emergent dependence can enter only through the datum
    that selects that constant (U1r5:596–600, R2a), which F4, a claim about sources, does not cover.
  - Which route the G3 law takes is open.
- **Given the route, the reading is still not entailed [P].** On the equation-of-state route the
  standard reading is CoC [L, recalled]. That is a reading, not a theorem, and the corpus states the
  route as used, not derived (GR:162).
- **The determination question remains on either reading.** Does some substratum satisfying OI's
  premises have a boundary law of K_cpl^conv form with a fixed constant (U2Ar3:697–714)? If such a law
  were derived, its `Z` would be a consequence of `φ` (U2Ar3:847–848) [P].

***

## 5. Controls

| Control | F1/F2 (CoC-content) | F3 | F4 | Status |
|---|---|---|---|---|
| K1 | C1-type metric (value `g_{R*}`) grounded in `r` by its nature: cycle, excluded. The witness is not excluded. [A] | excluded (grounding by nature) | excluded | green |
| K2(a) K_dec | no partition-defined term; admitted [P] | not reached | energy content grounded in the microstate; admitted [P] | green |
| K2(b) nonlinearity | `G_μν[g]` CoC by Lemma U [A] | not reached | geometric side, not grounding by F4's statement [P] | green |
| K2(c) gap equation | CoC (GR:144) [P] | not reached | no source term [P] | green |
| K3 | §2.4: every use reads as CoC [P] | — | §2.4: GR:384 and GR:482 must be classed as non-source (a geometric identity; an intermediary), a distinction stated at SM:160 between input (iii) and inputs (i)–(ii) [P] | green; for F4, conditional on that classification |
| K4 | Lemma U and Corollary E use N1–N3-G, N3′, transitivity, N5-G and the witness's definition. None is on the excluded list, including R-2. [A] | F3 uses Main:44, Main:54 and Structure.md:136 only. [A] | F4 is a formalization assessed, not a premise of any verdict. Its textual consistency includes excluded paragraphs (P11, GR:575's context); they are cited as vocabulary, not as premises. [P] | green |
| K5 | K1's pair has equal values and ⊳_D graphs and differs in ⊳_G. [A] | — | the same pair differs under F4 [A] | green |

**Changes from r1.**

- K4 is re-run with R-2. r1's K4 listed P-F with Substratum.md:385–389 for the F3 and A3 steps, which
  BG-3 shows to be conclusion-adjacent. F3 now rests on P-D alone (§3.3), and A3 is re-evaluated in §6.
- K3 adds GR:384 and GR:482, which r1 did not examine.

***

## 6. Pressure tests (§A.31)

The tests run depth-first. F4 is the branch favourable to decoupling: with N5-G, it excludes K_cpl^conv.
It is tested first and with the most skepticism, followed by CoC and then the partition fork.

### 6.1 Branch F4 (favourable to decoupling)

- **F4-1. Presentation.** A side-keyed F4 classifies presentations, not laws. The energy-content
  statement of §3.4 is invariant. Verdict: F4 survives only in the invariant form. [A]
- **F4-2. The corpus's own feedback.** Under F4 without §8.3, GR:358's "feed back … through state-level
  quantities" and GR:400 Reading 1 are excluded on Reading G, as under (ii-L). AW-loop then stands under
  F4. Verdict: F4 is coherent, at that cost. [P]
- **F4-3. Relata.** If F4 is taken diachronically (energy content at `s` grounds curvature at `s′ > s`),
  then with a static-patch partition the chain `g(s) ⊳_G Π(s) ⊳_G ρ_Z(s) ⊳_G g(s′)` is acyclic.
  - Lemma U does not close, and Reading G excludes nothing.
  - With GR:40's event-horizon partition, `Π(s)` depends on the future metric, and the cycle returns
    (AW-tel, U2Ar3:770–771).
  - P-D does not exclude diachronic macro-to-macro grounding. r1's node A5 placed its refutation in P-D,
    which holds only for F3 and for macro-to-micro grounding.
  - Verdict: F4 excludes the witness only with synchronic or whole-history relata, or with the
    event-horizon partition. [P]
- **F4-4. Is F4 the conclusion in disguise?** F4 is a general claim about sources, and it admits P11's
  classical source and any source not grounded in `g`. It is not equivalent to (ii-G) or to the
  exclusion. Its textual support sits in the geometry-first paragraphs, which are excluded as premises
  and are cited only as vocabulary. Verdict: not an import. F4 is not entailed either. [P]
- **F4-5. The corpus's partition-defined "gravitating" quantities.**
  - GR:384 calls `ρ_s(H)`, a horizon-defined energy, "the total gravitating boundary energy".
  - GR:482 has "the Jacobson mechanism" convert a boundary entropy gradient "into curvature".
  - GR:695 obtains the Newtonian field from holographic equipartition with the horizon temperature.
  - Each quantity is grounded in `g` through the partition. Under F4 read as "whatever gravitates
    grounds curvature", Lemma U would exclude the corpus's own §7.2, §7.3 and §8.7 steps on Reading G.
  - F4 survives only by classing these as a geometric identity (`ρ_s = ρ_crit`, GR:384 "as an
    identity") or as thermodynamic intermediaries. That is the input (iii) against (i)–(ii) distinction
    of SM:160.
  - Verdict: F4 survives with that stated distinction. The corpus's "gravitating" vocabulary is not
    uniformly F4's, which weakens its support for F4. [P]
- **F4-6. Route.** On the Jacobson route the source is the null flux, and a uniform term has none
  (U1r5:603–605) [A]. F4 then does not reach the witness's uniform term, and the question moves to the
  selection of the integration constant (U1r5:596–600). Verdict: F4's exclusion of the witness is
  confined to a divergence-free sourcing law. [P]

**Branch F4 result.** F4 is admissible. Its exclusion of the witness on Reading G is conditional on
N5-G, case β, synchronic relata, a divergence-free sourcing law, and the classification of F4-5. F4 is
not entailed by the premise base. [P]

### 6.2 Branch CoC

- **C-1. Is CoC the regularity view by assumption?** Yes. F1 and F2 build it in (REVIEW-BG-r1 BG-1 item
  3). CoC is admissible, not entailed. Verdict: holds as admissible. [P]
- **C-2. Does SM:158 or GR:162 entail CoC?** SM:158 is a hypothetical construction ("would … were").
  GR:162 states the route as used, not derived. The equation-of-state reading is a reading
  [L, recalled]. Verdict: no entailment. [P]
- **C-3. Does Substratum.md:385–389 entail CoC?** Its separation clauses are excluded (R-2). Its
  co-projection clause restates the separation under test. Verdict: not used. [P]
- **C-4. Overdetermination.** Under CoC, Lemma U excludes any edge `t ⊳_G g` whatever other grounds `g`
  has [A].

**Branch CoC result.** CoC is admissible and not entailed. [P]

### 6.3 Other nodes from r1, re-evaluated

- **A1.** "Feed back" at GR:358 and GR:400: see F4-2.
- **A2.** GR:340 s.1 as a governing law: excluded as a premise, and its terms are classical. No bearing.
- **A3. Strong emergence.**
  - Downward grounding of micro states by macro terms contradicts P-D: `x(s′) = φ^{s′−s}(x(s))` is
    fixed by `x(s)` and `φ` [P].
  - Macro-to-macro grounding is F4 and is not excluded.
  - r1's appeal to Substratum.md:387–389 is withdrawn (R-2).
- **A4. Convention.** If a derived law had K_cpl^conv's form, its `Z` would be fixed by `φ`. Unchanged.
- **A6. AW-metric.** Unchanged (§9).
- **B1. N5-G.** The verdict is scoped to Reading G.
- **B2. The partition's ground.** The corpus gives the partition two grounds.
  - (β) GR:40, GR:346: the partition is defined by the metric's causal structure.
  - (α) Main:48, Lemma 2: "the definition of embedded observation", `V ⊊ S`, with no metric; Main:26
    speaks of "causal reach" without a metric; GR:40 says the horizon "implements" Lemma 2's partition.
  - In case α Lemma U does not apply, Reading G's reductio fails at N2-G, and neither the witness nor the
    C1-type configuration is excluded. B_G is idle. AW-part.
- **B4. Lemma U without N3′.** `g ⊳_G A ⊳_G ρ_Z` through the horizon area suffices (U2Ar3:306–313).
  Unchanged.

**§A.31 fixed point.** Not claimed. Passes in r2: pass 5 (F4 branch), 0 NEW (F4-3, F4-5 and F4-6 are
ELABORATING); pass 6 (CoC branch), 0 NEW. With r1's four passes, the last two passes yield no NEW
finding, which is short of the 3–4 the fixed point requires.

***

## 7. Verdict from the rule

- **Grounding-content formalizations.**
  - F3 is rejected by (b2), P-D (§3.3).
  - F4 is admissible (§3.4, §6.1).
- **CoC-content formalizations.** F1 and F2 are admissible (§3.4, §6.2).
- **Controls.** Green for each (§5). F4's K3 is conditional on F4-5's classification.
- **Outcome: (C).** Both kinds remain admissible.
- **The residual.** Whether the boundary law's source term grounds the metric (F4) or co-constrains it
  (CoC).
  - Under F4, with N5-G, case β, synchronic relata and a divergence-free sourcing law, Reading G
    excludes the witness's law.
  - Under CoC, Reading G excludes no field equation whose metric has a ground in `(S, φ, x₀)`, and what
    remains is G3's determination question.
  - The residual depends partly on G3, through the route: on the Jacobson route F4 does not reach the
    uniform term (§4.3).
- **Withdrawn.** r1's outcome (B) and r1's claim that B_G "does not reduce to G3".

**Productivity (§1.5).** The result is strictly stronger than unit 2(a)'s gap. Corollary E shows that
B_G read per world adds nothing to the exclusion. The gap moves from "B_G … and a view of laws the corpus
does not state" to F4 against CoC, with three conditions F4 needs and with a route on which F4 does not
apply. It exposes an assumption (§4.1, "directly"; F4-3, the relata), and it constrains how unit 2(a)'s
and unit 1's gap is worded (§8). The unit meets the test.

***

## 8. Consequences

All items are conditional on the gap of §7. None adopts a premise, proposes a manuscript change, or
edits a record. The witness keeps the de Sitter and M1 scope.

### 8.1 Requirement (ii) and (ii-G)

- **Given CoC:** on Reading G, requirement (ii) excludes C1-type configurations and no semiclassical
  boundary law, as on Reading E (U2A-F7) [P].
- **Given F4 (with its conditions):** on Reading G it also excludes emergent-class sources grounded in
  the metric. With §8.3 in force it admits the configuration-differential part (U2Ar3:469) [P].

### 8.2 (ii-L)

- Unchanged from unit 2(a) on Readings E and D: an added premise, silent under Z_0, dependent on the
  §8.3 branch (U2Ar3:684–696).
- The candidate independent motivation through GR:342 read as N5-G (U2Ar3:82–85, :829–832) is
  conditional on F4. Under CoC it supplies no exclusion of a field equation [P].

### 8.3 (DZ)

- (DZ) for the convention-fixed offset is supported by GR:346 on Reading G given F4 and its conditions
  (§7).
- Otherwise it rests on:
  - G3, by determination;
  - the posits P11, GR:575 or (ii-S);
  - (ii-L) as an added premise. [P]

### 8.4 Unit 1 Part 2

- CORR r1 and CORR r2 state Part 2 as conditional "on Reading G of GR:346 and the bridge premise B_G
  (open)" (CORR r2 row 2 and X-1).
- This record narrows B_G to F4 against CoC, and it does not settle it. Part 2's conditional form
  stands.
- CORR's clause "B_G … fails, conditionally, if the boundary law is a coarse-grained consequence of `φ` …
  The first condition is G3 (open); the corpus states no view on the second" would read with §4.1:
  - the status sense is fixed by P-D;
  - "directly" is the F4 against CoC question;
  - that question depends partly on G3's route;
  - the corpus states no view on whether source terms ground.
- Forward notes are held until the gap is settled (QB2). Unit 1 Part 1 is unaffected. K_cpl^free under F4
  is not examined (§3.5).

### 8.5 Unit 2(a)

- Under unit 2(a)'s rule, Reading G meets (B)(b) in case β only given CoC. Given F4 it meets (A) for the
  witness. While F4 against CoC is open it meets neither. In case α it meets (B)(a), but that is not the
  reading unit 2(a) formalized.
- Unit 2(a)'s outcome therefore stays (C), with its gap narrowed to F4 against CoC (§7).
- Its §8.3 rows (U2Ar3:469–470) and AW-loop (U2Ar3:715–720) are unchanged until the gap closes [P].
- This record does not edit unit 2(a) r3.

### 8.6 What does not change

- The witness, its algebra and its scope.
- Unit 2(a)'s findings on Readings E, D and S.
- U2A-F2.
- The world-equivalence on the de Sitter class.
- GR:579's open question.
- G3's open status.
- No claim about Λ.

***

## 9. Findings

Identifiers are kept from r1, and new findings take new identifiers.

| ID | Finding | Class | Support |
|---|---|---|---|
| BG-F1 | Lemma U is Reading G's reductio specialized to a law term. Corollary E: on the regularity view (F1, F2), B_G read per world is exactly the non-realizability of the witness's law, and adds nothing to the exclusion. | ELABORATING (Lemma U restates Reading G's reductio; Corollary E shows that B_G read per world adds nothing to the exclusion) | [A] §3.1–3.2 |
| BG-F2 | Unit 2(a)'s condition (a) ran together the status of a law (fixed by P-D for any law that holds) with its derivation (G3). The status sense does not settle "directly", which is B_G. The corpus contains passages consistent with co-constraint for its derived matching relations (SM:158, Substratum.md:387, GR:144, GR:581) and sourcing language consistent with grounding (GR:340, :352, :358, :581, :400). It states no view on whether a law's source terms ground its solutions, so unit 2(a)'s negative statement stands as worded. | ELABORATING (hidden assumption in "That is G3") | [P] §4.1–4.2 |
| BG-F3 | The governing reading (F3) contradicts the single-bijection dynamics: Main:44, :54, and A1–A6 at Structure.md:136. | CONFIRMING (of U2Ar3:599–601) | [P] §3.3 |
| BG-F4 | Given CoC, on Reading G requirement (ii) excludes the C1-type configuration and no semiclassical boundary law, as on Reading E (U2A-F7). Given F4 it also excludes emergent-class sources grounded in the metric. | ELABORATING (conditional; charity marker on GR:342's "three independent requirements") | [P] §8.1 |
| BG-F5 | B_G narrows to F4 against CoC. F4's exclusion of the witness needs synchronic or whole-history grounding relata (or GR:40's event-horizon partition) and a divergence-free sourcing law. On the corpus's conditional Jacobson route a uniform term has zero null flux, and the witness's dependence moves to the selection of the integration constant, which F4 does not cover. | ELABORATING (gap of §7; route dependence on G3) | [A] null flux; [P] §3.4, §4.3, §6.1 |
| BG-F6 | The corpus's own partition-defined "gravitating" quantities (GR:384 `ρ_s`, GR:482's entropy gradient, GR:695's horizon temperature) are admissible on Reading G, in case β, only as CoC or as non-source intermediaries. F4 must draw the line at SM:160's input (iii). | ELABORATING (assumption-watch AW-entropic) | [P] §6.1 F4-5 |

**Assumption-watch markers.**

- **AW-part (B2).** The partition is grounded either in the observer's embedding (Main:26, Main:48) or in
  the metric's causal structure (GR:40, GR:346). Reading G's reductio needs the second. Sites: GR:40,
  GR:346 s.1–s.2, book/ch07-gravity.md:183. No change is proposed.
- **AW-metric (A6).** GR:693 calls the metric "the framework's *own* emergent-metric geometry". If the
  metric's definition passes through the emergent description, Reading G's reductio applies to OI's own
  metric. Sites: GR:693, GR:340 s.1, GR:342. No change is proposed.
- **AW-entropic (BG-F6).** Wherever the corpus derives a gravitational effect from a horizon-defined
  quantity (GR:384, GR:422–426, GR:482, GR:695), a reading of that step as grounding meets Lemma U on
  Reading G. Sites as listed. No change is proposed.
- **AW-ground (U2Ar3:760–766), unchanged in substance.** Substratum.md:385 and :393 read as ⊳_D or as
  CoC under N5-G.

***

## 10. Literature

All entries are recalled and were not re-read. No verdict rests on any of them.

- K. Fine, "Essence and modality" (1994); K. Fine, "Guide to ground" (2012); G. Rosen, "Metaphysical
  dependence: grounding and reduction" (2010): transitivity and irreflexivity of strict partial ground;
  definitional dependence as ground.
- E. Bliss (2014) and N. Thompson (2016): dissent from well-founded grounding (B1).
- T. Jacobson, "Thermodynamics of spacetime: the Einstein equation of state", *Phys. Rev. Lett.* 75,
  1260 (1995): the equation-of-state route.
- D. Lewis on Humean supervenience; T. Maudlin, *The Metaphysics Within Physics* (2007); D. Armstrong,
  *What Is a Law of Nature?* (1983); and the Humean-explanation debate: the regularity and governing
  views that F1/F2 and F3/F4 instantiate.
- The strong-emergence literature: the position node A3 examines.

***

## 11. Owner questions

- **QB1. Unit 2(a)'s rule.** Re-applied to Reading G (§8.5), it leaves unit 2(a) at (C), with the gap
  narrowed to F4 against CoC. Is a forward note on unit 2(a)'s gap wording wanted, or is this record
  enough?
- **QB2. Forward notes.** Should forward notes to unit 2(a) r3 and CORR r2 be held until F4 against CoC
  is settled, or should the narrowed wording of §8.4 be carried now?
- **QB3. QU2 follow-up.** (ii-L)'s and (ii-G)'s candidate motivation through Reading G is conditional
  on F4. Does Q7 stay open on that basis?
- **QB4. QU3 follow-up.** Two scopings of GR:346, GR:342 ("forced") and book/ch07-gravity.md:183–187
  are available for a future manuscript unit: given CoC, (ii) excludes only metrics that are quantities
  of the emergent description; given F4, it also excludes emergent sources grounded in the metric. No
  change is proposed.
- **QB5. Next unit.** Candidates:
  - (a) F4 against CoC: a paper-only audit of the source term in the corpus's conditional routes
    (SM:144–162, GR §3.1, §7.3, §8.7), including AW-entropic, and of whether the G3 target
    (GR:12) is a divergence-free sourcing law or a null-flux route;
  - (b) AW-part;
  - (c) AW-metric;
  - (d) unit 2(a)'s QU5(b) (whether OI fixes `Z`);
  - (e) K_cpl^free under F4 (§3.5).

***

## 12. Limits

- The logic is by hand.
- Lemma U holds on Reading G in case β and is conditional on N5-G.
- F4 and CoC are both readings [P]. Neither is entailed by the premise base.
- The rule was repaired after review, which had named the expected outcome. The repair is stated in
  §1.6.
- The rule and the analysis land in one commit.
- The §A.31 fixed point is not reached.
- No claim is made about K_cpl^conv's admissibility under G3, or about Λ.
