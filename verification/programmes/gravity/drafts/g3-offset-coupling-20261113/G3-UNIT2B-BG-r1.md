# G3 unit 2(b) (r1): the bridge premise B_G, grounding or co-constraint

**Scope.** This is a paper-only investigation under Issue #873, continuing units 1 and 2(a) (PR #1275).

- Authorization: #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU5: "a bounded, paper-only
  investigation of B_G: whether a term in the boundary-metric law that depends on the emergent class
  grounds the metric or only co-constrains it, including how far this reduces to the status of the
  boundary law under G3. It runs on #1275's branch, followed by an independent review and then the
  ChatGPT exact-head review. It adopts no premise, makes no manuscript change, involves no Lean build and
  makes no claim about Λ."
- Inputs, on branch `research/g3-offset-873-20261113`:
  - unit 2(a) r3, `G3-UNIT2A-r3.md` at `1ad01923efda24323217f3a5d9dd30a5c506fd3c` ("U2Ar3:n" is its
    line n), with its delta check `CONFIRM-U2A-r2.md` (CONFIRMED);
  - unit 1 r5, `G3-UNIT1-r5.md` ("U1r5:n"), unchanged since `e81e4fb2`;
  - the unit 1 forward correction `G3-UNIT1-CORR-r1.md` ("CORR") and its check `CONFIRM-CORR-r1.md`,
    which the branch head `3945940c` adds on top of `1ad01923`. Every other file cited here is
    identical at the two commits (NOTES-BG-r1 §1).
- Reviews on #1275: 5896999577 (unit 1 r5, at `e81e4fb2`) and 5898121925 (unit 2(a) r3, at `1ad01923`),
  both posted by `amaybaum`.

This record proves no theorem in Lean, runs no computation, changes no manuscript, adopts no premise and
makes no claim about the magnitude of Λ.

**Source snapshot.** `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`. Every `file:line` refers to
that commit.

**Support labels**, as in units 1 and 2(a): [K] kernel-checked declaration on `main`; [A] exact algebra or
elementary logic, done by hand here; [P] a paper derivation, or a reading of a paper statement;
[L, recalled] literature recalled from memory and not re-read, on which no verdict rests; "Conjecture" an
unsupported proposal. **Conditional** marks a claim that holds only under the hypotheses it names.

**Terms from unit 2(a).** ⊳_E (order of explanation, specification), ⊳_D (order of determination, value
dependence on a family) and ⊳_G (order of existence or emergence: `X ⊳_G Y` if `Y` is what it is partly in
virtue of `X`) are defined at U2Ar3:206–217. N1–N5 are the premises of GR:346 (U2Ar3:195–202), and N5-G is
the well-foundedness of ⊳_G (U2Ar3:226–231). Reading G is U2Ar3:277–287. The witness is the
K_cpl^conv fixed-point model on the de Sitter family under M1 (U2Ar3:291–419). **B_G** is: "a term of the
boundary metric's law that is a function of the emergent class grounds the realized metric, and does not
only co-constrain it" (U2Ar3:285–287).

***

## 0. Verdict

**Outcome (B), scoped to Reading G of GR:346 with N1–N3 read in ⊳_G (case β, §6 node B2).** Under every
formalization of B_G that the corpus's uses admit (§2), B_G either fails at every world the corpus admits
or contradicts a stated premise. Wherever a boundary law with a term that is a function of the emergent
class holds, that term co-constrains the realized metric and does not ground it.

- **The decisive step (Lemma U, §3.1) [A] given its premises.** A law term that is a function of the
  emergent class at the realized partition is grounded, through N1–N3-G, in the realized metric. By
  N5-G, nothing grounded in the metric grounds the metric. The same step classes the Einstein left side
  `G_μν[g]` as non-grounding, which unit 2(a)'s control C2(b) already requires (U2Ar3:485). Nothing in
  Reading G separates an emergent-class term from `G_μν[g]` in this respect.
- **What follows for B_G (§3.2–3.3).**
  - Read as a fact about a realized witness (F1), B_G is false at every world that satisfies Reading
    G's premises [A].
  - Read as "wherever the witness's law holds, its term grounds the metric" (F2), B_G is logically
    equivalent to the statement that no such world realizes the witness's law, which is the exclusion
    it was meant to supply [A]. In unit 2(a)'s rule this is clause (B)(b) (U2Ar3:138–141).
  - Read as a governing status for the boundary law (F3), B_G contradicts the corpus's stated
    commitments that `(S, φ)` is the fundamental object and its single bijection the only fundamental
    dynamics (P-F, P-D below) [P].
- **Named premises.** N1–N3 as GR:346 and GR:342 state them (GR:40; GR:344; GR:346 s.1–s.2; GR:342 "QM is
  emergent"), read in ⊳_G; N3′, that a quantity defined as a function of the class is grounded in it
  (for the witness the horizon area suffices, §6 node B4); N5-G, which is Reading G's own principle and is not stated in the corpus; P-F,
  GR:342 ("the framework has no substance-level primitives … spacetime emerges from
  `[(S, φ)]/𝒢_sub`") and Substratum.md:385–389 ("two different substructures of the same total object
  `(S, φ)`"; "Both are derived rather than fundamental. The fundamental object is `(S, φ)`"); P-D, Main:44
  and Main:54 (one transition map, a bijection) and A1–A6 (Structure.md:136), which contain no
  gravitational law; P-S, SM:158 (the gravitational equations "are the equations of motion, not
  constraints on separate dynamics"), GR:352 ("a coupling theorem") and GR:655 ("the classical
  substratum's gravitational dynamics") [P].
- **Reduction to G3 (§4).** Unit 2(a) made B_G's failure conditional on the boundary law being "a
  coarse-grained consequence of `φ`", which it identified with G3 (U2Ar3:535–537, :548–552). Two senses
  of "derived" are distinct there.
  - The ontological status of a boundary law, that it holds, if it holds, in virtue of the substratum's
    realization, is fixed by P-F, P-D and P-S [P].
  - G3 concerns which law the substratum yields (GR:12, GR:162), and it is open.
  - B_G depends only on the first sense, so it does not reduce to G3. What remains open about the witness
    after B_G is G3's determination question: whether any substratum satisfying OI's premises has a
    boundary dynamics that obeys K_cpl^conv's equation rather than K_dec's [P].
- **The corpus on derived laws (§4.2).** Unit 2(a) recorded that "the corpus states no view" on whether a
  derived law's terms ground its solutions (U2Ar3:538, :550–551). The corpus does state the status of its
  own gravitational law, in terms that fix co-constraint on Reading G: SM:158, Substratum.md:387, GR:144,
  GR:581 and Main:686. None of them uses the word "ground". This is a reading [P], and a correction to
  the scope of unit 2(a)'s negative statement (§A.19).
- **Controls.** K1–K5 (§1.4) are green (§5).

**Scope.**

- The verdict concerns B_G and Reading G only.
- It does not show that K_cpl^conv is admissible in OI. That is G3's open question (§4.3), and other
  posits exclude K_cpl^conv: P11 (GR:340 s.2), GR:575 and (ii-S) (U2Ar3:76–78).
- It is conditional on N5-G, which the recalled literature contests (U2Ar3:806–810) [L, recalled].
- It is conditional on reading N1–N2 in ⊳_G (case β). In case α, where the realized partition is
  grounded in the observer's embedding and not in the metric (Main:26, Main:48), Reading G's reductio
  fails at N2-G, and Reading G excludes nothing. B_G is then idle (§6 node B2).
- The consequences for the witness keep unit 2(a)'s scope: the exact de Sitter class and assumption M1.
  Lemma U itself is not restricted to de Sitter.

**Consequences** (§8), each scoped.

1. On no reading of GR:346 examined in units 2(a) and 2(b) (E, D, mixed, S, G) does GR:346's argument
   exclude K_cpl^conv's field equation independently of G3 or of an added premise.
   - On Reading G, B_G supplies no exclusion of its own [A], [P].
   - Unit 2(a)'s candidate "independent motivation" for (ii-L) and (ii-G) through GR:342 read as N5-G
     (U2Ar3:82–85, :829–832) therefore supplies no exclusion of a field equation. Within Reading G, (ii-G)
     excludes only configurations whose metric is by its nature a quantity of the emergent description
     (C1-type).
2. (ii-L) remains what unit 2(a) found on Readings E and D: an added premise, silent under Z_0 and
   dependent on the §8.3 branch (U2Ar3:684–696). Holding it would require an independent motivation
   other than GR:346.
3. (DZ) for the convention-fixed offset rests on G3 (by determination), or on the posits P11, GR:575 or
   (ii-S), or on (ii-L) held as an added premise.
4. Unit 1 Part 2 (r5 and CORR X-1 to X-20), and unit 2(a)'s Reading G clause, would read accordingly if
   this verdict stands review (§8.4–8.5). No record is edited here.

***

## 1. Decision rule

**Provenance of the rule.** This section was written after the sources listed in NOTES-BG-r1 §2 had been
read and after an outline of the argument had been formed. Its clauses were not edited after §2–§8 were
written. The rule and the analysis land in one commit, and no commit pins the rule separately.

### 1.1 Premise base

- **The corpus's stated premises:** the text of `main` at `c3b5f37a`, as cited, with its stated status.
- **Reading G's own premises:** N1–N3 read in ⊳_G, and N5-G. B_G is the bridge premise of Reading G
  (U2Ar3:285–287) and has no role off it. N5-G is admitted as part of Reading G and is labelled as not
  stated in the corpus.
- **Excluded as premises** (each is a conclusion under test, or a posit whose use would decide the
  question):
  - B_G and its negation;
  - (ii-W), (ii-L), (ii-S) and (ii-G) as exclusions;
  - GR:342 "This ordering is forced …" and "not the reverse";
  - GR:346 s.4, "the metric exists prior to the partition" (C);
  - book/ch07-gravity.md:187;
  - GR:340 s.1's ordering clause, "the metric evolves via Einstein's equations *before* the trace-out";
  - GR:340 s.2, the geometry-first source (P11);
  - GR:575's clause "What does not gravitate";
  - any form of the boundary law, its derivation, or its non-derivability (G3).

### 1.2 Outcomes

An **OI world** is a realization `(S, φ, x₀)` that satisfies the premise base, with the partition realized
as GR:40 states, together with the completion under test.

- **(A) B_G supported.** There is a formalization of B_G that meets the corpus-use check of §2.4 under
  which the premise base (premises named) entails the following: at every OI world where a boundary law
  containing a term that is a function of the emergent class holds, that term grounds the realized
  metric. The entailment must not pass through the non-realizability of the law, since that is the
  exclusion B_G is meant to supply.
- **(B) B_G refuted / co-constraint.** For every such formalization, either
  - (b1) the premise base entails that at every OI world where such a law holds the term does not
    ground the realized metric, while the law relates items with a common ground (co-constraint); or
  - (b2) B_G contradicts a stated premise, which is named.
- **(C) Open.** Neither (A) nor (B). The precise residual is stated, for example a formalization on which
  the premise base decides nothing, or a reduction to G3's derivation status.

### 1.3 Formalizations quantified over

- **F1 (realized).** At an OI world `w` where the witness's law holds, its term grounds `g_w`.
- **F2 (law-level).** For every OI world where the witness's law holds, its term grounds the realized
  metric.
- **F3 (governing status).** The boundary law is a fundamental item, and the inputs of a fundamental law
  ground its outputs.
- Any further formalization found during the analysis is added to this list, and the clauses of §1.2
  apply to it unchanged.

### 1.4 Controls

- **K1 (positive, non-vacuity).** The formalization must class as grounding, and Reading G must exclude,
  a C1-type configuration (U2Ar3:483): a metric that is by its nature a quantity of the realized emergent
  description. The instance used must have the same realized value as the witness (`g_{R*}`), so that the
  verdict depends on the order of grounding and not on values.
- **K2 (negative).** The formalization must not exclude, or class as a ⊳_G-cycle:
  - (a) K_dec;
  - (b) the Einstein nonlinearity, where `G_μν[g]` depends on `g`;
  - (c) the gap equation, which the corpus calls non-circular (GR:154; book/appendix-c-objections.md:259).
- **K3 (uniformity with the corpus's uses).** The same criterion is applied to GR:340 (P11), GR:342,
  GR:346, Substratum.md:385–389, GR:162 (the Jacobson route), SM:160–162 and GR:400 Reading 1. A verdict
  that classes the witness's term differently from a corpus use, without a stated difference relevant to
  grounding, is void.
- **K4 (no import).** The premises of the decisive step are listed. None is in the excluded list of
  §1.1.
- **K5 (grounding is not determination).** The formalization must allow two configurations with the same
  ⊳_D graph to differ in ⊳_G. Otherwise "grounds" collapses into "determines", which unit 2(a) has
  already settled (U2Ar3:223–225).

A verdict is written only if K1–K5 are green. A failed control voids it, and the outcome is then (C) with
the failed control named.

### 1.5 Productivity test (§A.31)

The unit is a gem if it yields a fact strictly stronger than unit 2(a)'s statement (B_G "open … narrowed
to the status of the boundary law (G3) and to a view of laws the corpus does not state", U2Ar3:746), and
the fact either constrains a claim or exposes a hidden assumption. Otherwise it is recorded as a
coherence check.

***

## 2. Formalization

### 2.1 Objects

- At a world `w`: the realized metric `g`; the realized partition `Π = Π(g)` (GR:40); the realized
  emergent class `r = T(Π)`, the reduced description produced by the trace-out (GR:344; Main:686,
  Main:690); and the term `t = τ(r)`, for a map `τ`. For the witness, `τ = ρ_Z` (U2Ar3:315–328).
- **A law** is a relation `L(g, t, …) = 0` on a stated family of candidate configurations. For the witness
  it is `G[g] + Λ_c g = 8πG(T^cl − ρ_Z g)` (U2Ar3:342).

### 2.2 Three relations, kept apart

- **Specification (⊳_E).** `L` together with the family specifies `g*` implicitly as its solution. The
  inputs are the maps (`Π`, `T`, `τ`), not the realized values (U2Ar3:208–211, :425–441).
- **Determination (⊳_D).** On the family, `t` varies with `g` and `L` returns `g` from `t`. Cycles of
  ⊳_D are realized by every equation with a fixed point (U2Ar3:223–225) [A].
- **Grounding (⊳_G).** At the realized world, `Y` is partly what it is in virtue of `X`. ⊳_G is
  transitive, and under N5-G it is irreflexive and well-founded [P; L, recalled: Fine 2012].
  - It is a relation among realized items. Two configurations with the same values and the same ⊳_D
    graph can differ in ⊳_G (K5).
  - An item defined as a function of another is grounded in it: if `t := τ(r)`, then `r ⊳_G t`. This is
    definitional (essential) dependence, the standard case of partial grounding [P; L, recalled: Fine
    1994, Rosen 2010]. Call it N3′.

### 2.3 Two roles for a law term

Let `L` hold at `w`, with term `t`.

- **Grounds (Gr):** `t ⊳_G g`.
- **Co-constrains (CoC):** `t` does not ground `g` (`¬(t ⊳_G g)`), and `g` and `t` both have grounds in a
  common base `b`, so that `L` states a relation that holds between items grounded in `b`. In OI the
  candidate base is `b = (S, φ, x₀)` (P-F, Main:686).

Gr and CoC are exclusive. Neither is fixed by ⊳_E or ⊳_D: a term can be an input of the specification and
a value-determinant of `g` (U2Ar3:452–453) and still co-constrain [A].

### 2.4 The corpus's uses, read against §2.2–2.3 (K3)

| Corpus use | Text | Relation it states | Reading [P] |
|---|---|---|---|
| GR:340 s.2 (P11) | "The stress-energy sourcing gravity is the classical stress-energy of the total microstate" | "sourcing": a term of the law | `T^cl` is grounded in the microstate. Gr and CoC are both consistent with N5-G for the microstate part. The metric-dependent part of `T^cl`, such as `p g_μν`, is grounded in `g` and falls under Lemma U. The text fixes neither role. |
| GR:342 | "Classical spacetime is logically prior to QM; QM is emergent … no substance-level primitives … spacetime emerges from `[(S, φ)]/𝒢_sub` … the direction of the derivation chain … presupposes" | "emerges from" (⊳_G, the same reading unit 2(a) gives "QM is emergent"); "derivation chain", "presupposes" (⊳_E) | Spacetime is grounded in `(S, φ)` (P-F). The first clause is excluded as a premise (§1.1). |
| GR:346 | "Causal structure is determined by null geodesics … derived … no entry point … exists prior" | N1–N2 "determined", "defined" (⊳_D, and ⊳_G as definitional dependence); "derived", "entry point" (⊳_E) | Case β reads N1–N2 in ⊳_G, as Reading G does (U2Ar3:279–280). |
| Substratum.md:385 | "the metric is a property of the classical dynamics of the partition boundary … two different substructures of the same total object `(S, φ)`" | "property of"; co-projection | In ⊳_G, "property of the … partition boundary" together with N1–N2 gives a cycle that involves no law term (U2Ar3:617–620). Under N5-G it must be read as ⊳_D, or as grounded in the classical dynamics of the cells that the metric picks out as the boundary (§5, K2(a)). The co-projection clause supplies the common base. |
| Substratum.md:387–389 | the thermodynamic/statistical-mechanical analogy, "the relationship between them is one of projection … by averaging"; "Both are derived rather than fundamental. The fundamental object is `(S, φ)`" | projection; co-grounding in `(S, φ)` | CoC: thermodynamic relations hold between quantities grounded in the microstate [P; L, recalled: the standard reading of equations of state]. |
| Substratum.md:393 | "the metric, the surface gravity, the entropy, and the temperature determined by the partition geometry and the area-law theorem" | "determined" | ⊳_D. Read in ⊳_G it gives the cycle of the Substratum.md:385 row. |
| GR:162 | "uses the Einstein equations through Jacobson's relation (§3.1) and does not derive them" | status: used, not derived | The law is an input reached by a thermodynamic route, the "equation of state" route [L, recalled: Jacobson 1995]. No governing status is stated. |
| SM:158 | "Every orbit is self-consistent by construction: the state determines the graph, which determines the entropy and temperature, and the Clausius relation would constrain the graph's response … the Einstein equations are the equations of motion, not constraints on separate dynamics … a single bijection … The ontological object is still (S, F, V)." | "determines" (⊳_D); "constrain"; law = equation of motion of the single bijection | CoC, stated for the corpus's own lattice gravitational law: the law constrains, and adds no ontology beyond `(S, F, V)`. The loop state → graph → temperature → graph is called self-consistent. |
| SM:160–162 | Jacobson's inputs: (i) area law; (ii) the Unruh temperature of the Rindler observer's reduced state (SM:140); (iii) the null flux; (iv) Raychaudhuri | input (ii) is a property of a reduced description at a partition defined by the metric's null structure | Under Lemma U, input (ii) cannot ground the curvature it constrains. On Reading G the route is admissible only as CoC. GR:160 routes the temperature through the classical `T_cl` instead. |
| GR:144 | "they refer to the **same physical degrees of freedom**: the boundary modes `V × B`" | the matching of a classical and an emergent temperature | CoC: two descriptions of one set of substratum degrees of freedom, related by an equation. |
| GR:581 | "Relative energies within the emergent QFT … correspond to differences in the coupling structure of φ, which the Jacobson derivation reads as curvature" | "correspond to"; what curvature reads is φ's structure | CoC: the emergent relative energy co-describes the φ-structure that grounds the curvature. |
| GR:358 | "The emergent quantum description does feed back into gravitational dynamics through state-level quantities … the vacuum energy (volumetric, state-dependent, a property of `H_tot`) does [gravitate]" | "feed back" | Read in ⊳_G as Gr, a cycle by Lemma U. The paragraph assigns the gravitating vacuum energy to `H_tot`, which supports CoC. |
| GR:400 Reading 1 | "the emergent layer's curvature response … feeds back as a source" | "feeds back as a source" | As GR:358. Under §8.3 the piece is a classical microstate difference (GR:573), grounded in the substratum, and CoC applies. Without §8.3, Gr would be a cycle by Lemma U, and CoC applies. |
| Main:686, :690 | three descriptions "all derived from the same `φ` by the same trace-out procedure"; the joint matrix "exists and is unique given `φ`" | "derived from" | The emergent class is grounded in `(φ, Π, prior)`. The descriptions are "simultaneous rather than competing" (Main:692). |

**Result of the corpus-use check [P].** Every corpus use reads consistently with CoC for terms whose value
depends on the realized metric. No corpus use states Gr for such a term. The two phrasings that suggest
Gr, "feed back" at GR:358 and at GR:400 Reading 1, would close a ⊳_G-cycle if read as Gr (Lemma U). Each
paragraph also supplies a co-constraint reading.

***

## 3. The decisive step

### 3.1 Lemma U (uniformity)

**Premises.**

- N1–N2-G: `g ⊳_G Π`. The realized partition is partly what it is in virtue of the realized metric
  (GR:40; GR:346 s.1–s.2; U2Ar3:279–280) [P].
- N3-G: `Π ⊳_G r` (GR:342 "QM is emergent"; GR:344; U2Ar3:278–279) [P].
- N3′: `r ⊳_G t` for `t := τ(r)` (§2.2) [P].
- Transitivity of ⊳_G [P].
- N5-G: no `x` has `x ⊳_G x` [P; Reading G's premise, not stated in the corpus].

**Statement.** At any world satisfying these premises, `¬(t ⊳_G g)`. [A]

**Proof.** `g ⊳_G Π ⊳_G r ⊳_G t`, so `g ⊳_G t` by transitivity. If also `t ⊳_G g`, transitivity gives
`g ⊳_G g`, against N5-G. ∎

**Uniform instances [A].**

- `t = G_μν[g]`. A curvature of `g` is grounded in `g` (N3′ with `τ` the curvature map), so the Einstein
  left side does not ground `g`. Unit 2(a) classes the nonlinearity as admitted on Reading G (C2(b),
  U2Ar3:485). That classification presupposes CoC for `G_μν[g]`, and Lemma U is the same step applied to
  `ρ_Z`.
- `t = ρ_Z(r)`, the witness's term: CoC wherever the law holds.
- The ingredients of SM:160 input (ii) and the horizon entropy at a local horizon defined by `g`: CoC.
- What Lemma U uses is that `t` is grounded in `g`. The route through `Π` and the emergent class is one
  way of being grounded in `g`. "Emergent" adds nothing relevant to grounding beyond that. B_G's
  restriction to emergent-class terms (U2Ar3:612–615) therefore marks no difference for Reading G.

### 3.2 Corollary E (B_G at law level is the exclusion)

Define, for a completion `K` whose law has such a term:

- F1: at the OI world `w`, `t_w ⊳_G g_w`;
- F2(K): for every OI world `w` at which `K`'s law holds, `t_w ⊳_G g_w`.

Then [A]:

- F1 is false at every OI world (Lemma U).
- F2(K) holds if and only if no OI world realizes `K`'s law. *Proof.* If none does, F2(K) holds
  vacuously. If some `w` does, Lemma U gives `¬(t_w ⊳_G g_w)`, and F2(K) fails. ∎

So "Reading G excludes the witness if and only if B_G" (U2Ar3:504–507) reads, with B_G as F2, "Reading G
excludes the witness if and only if no OI world realizes the witness's law". In unit 2(a)'s rule, that is
a premise "equivalent to the exclusion being tested", clause (B)(b) (U2Ar3:138–141) [A].

### 3.3 Lemma F (when grounding is forced) and the governing reading

**What K1 separates [P].** Reading G excludes a configuration when its content, and not only its
equation, places the metric in a ⊳_G-cycle.

- **The C1-type configuration.** The metric is, by its nature, a quantity of the realized emergent
  description (for instance an expectation value fixed by `r`). So `r ⊳_G g` is part of what the
  configuration is. With N1–N3-G this is a cycle, and the configuration is realized at no OI world. This
  holds with the realized value equal to `g_{R*}`.
- **The witness.** Its metric is classical substratum data (U1r5:192; U2Ar3:296–297). Its content is a
  field equation and states no ⊳_G relation from `r` to `g`. A realization in which `g` is grounded in
  `(S, φ, x₀)` is therefore not excluded by Reading G. P-F (GR:342, Substratum.md:389) states that
  spacetime has such a ground.

**F3: governing status.** On F3 the witness's law is a fundamental item, and its input `ρ_Z` grounds the
realized metric.

- **(b2).** This contradicts stated premises [P]:
  - P-F, GR:342 ("the framework has no substance-level primitives") and Substratum.md:389 ("Both are
    derived rather than fundamental. The fundamental object is `(S, φ)`");
  - P-D, Main:44 (evolution is "iteration of a single transition map") and Main:54 (Lemma 3: `φ` is a
    bijection), with A1–A6 (Structure.md:136) listing no gravitational law;
  - P-S, SM:158 (the gravitational equations are "the equations of motion, not constraints on separate
    dynamics"; "The ontological object is still (S, F, V)"), GR:352 (decoupling is "a coupling theorem")
    and GR:655 ("the classical substratum's gravitational dynamics").
- **Independently,** in case β F3 also meets Lemma U: a governing law's input that is grounded in its
  output closes the same cycle [A].

### 3.4 Application

- **The witness.** At any OI world where its law holds, its term co-constrains the realized metric. The
  common base is `(S, φ, x₀)`: P-F for `g`, and Main:686 with N1–N3-G and N3′ for `ρ_Z`. Moreover
  `g ⊳_G ρ_Z`. In the order of grounding, the witness's law is a self-consistency condition that relates
  the metric to quantities grounded in it, which is the structure `G_μν[g]` already has [A] given Lemma U,
  [P] for the common base.
- **K_cpl^free** (CONFIRM-CORR-r1 K-3). Its term `e_free` is fixed on shell by the field equation, as a
  free coordinate on the σ-orbit (U1r5:352–355). Where it depends on `g` it falls under Lemma U, and
  where it does not it is not partition-defined. Reading G does not exclude K_cpl^free [P].

***

## 4. The reduction to G3

### 4.1 Two senses of "derived"

- **Status (ontological).** The law holds, if it holds, in virtue of the realization of `(S, φ, x₀)`.
  P-F, P-D and P-S fix this for any boundary law in OI:
  - no fundamental item other than `(S, φ)` is admitted (GR:342; Substratum.md:389);
  - the only fundamental dynamics is the bijection (Main:44, :54);
  - A1–A6 contain no gravitational law;
  - the corpus states its gravitational dynamics as the substratum's (GR:655) and its equations as
    equations of motion of the one bijection (SM:158). [P]
- **Derivation (epistemic).** A derivation on paper of which covariant equation the substratum yields,
  with conservation, Bianchi structure and the continuum limit. This is G3, open (GR:12; GR:162; GR:697
  (ii)).
- Unit 2(a)'s condition (a) (U2Ar3:535–537) needs only the first sense. Its words "That is G3, and G3 is
  open" use the second. B_G's failure does not wait on G3 [P].
- **The condition under which the status claim holds [P].** It presupposes that OI has a boundary metric
  at all, as a function of the substratum's realization. That presupposition is the stated commitment
  P-F, and its derivational support reaches only weak-field consistency (GR:691–697). If no metric
  emerges, there is no boundary law, and the question does not arise.

### 4.2 What the corpus says about derived laws

Unit 2(a) recorded that "the corpus states no view on this" (U2Ar3:538) after a search for grounding
vocabulary (NOTES-U2A-r3 §2). A search for the status of laws finds the following (NOTES-BG-r1 §3).

- SM:158: the gravitational law of the lattice model constrains the orbit of a single bijection, adds no
  ontology, and is "not constraints on separate dynamics". The loop through the temperature is stated to
  be "self-consistent by construction".
- Substratum.md:387: GR is the thermodynamic projection of `(S, φ)`, related to the statistical
  projection "by averaging".
- GR:144 and GR:581: equations between classical and emergent quantities hold because both refer to the
  same substratum degrees of freedom or φ-structure.
- Main:686–692: descriptions derived from one `φ` are "simultaneous rather than competing".

Reading [P]. These passages state, for the corpus's own derived relations, the co-constraint structure of
§2.3. None of them uses "ground", and none is a general philosophy of laws. They fix the stance for OI's
gravitational law and its classical–emergent matchings, which is what B_G needs. The disagreement
between the regularity and governing views of laws (U2Ar3:811–813) [L, recalled] is not needed: F3 is
excluded by the stated ontology, and F1 and F2 by Lemma U.

### 4.3 The residual, stated

After B_G the open question about the witness is one of determination.

- Does some substratum satisfying OI's premises have a boundary dynamics whose coarse-grained law,
  across configurations, is K_cpl^conv[Z] with a fixed completion constant, rather than K_dec, or
  neither?
- That is G3 together with 2(a)'s question QU5(b), whether OI fixes `Z` (U2Ar3:847–848). If such a law
  were derived, its `Z` would be a consequence of `φ` rather than a convention [P].
- On the de Sitter class with the constant left free, a single world does not separate the two:
  K_cpl^conv[Z_I] and K_cpl^conv[Z_II] realize the same de Sitter worlds as K_dec (U2Ar3:697–702) [A]. The
  difference between the laws lies in their counterfactual content, and outside the de Sitter class
  (U2Ar3:709–714).

This record makes no claim about the residual, and none about Λ.

***

## 5. Controls

| Control | Result | Status |
|---|---|---|
| K1 | A C1-type metric with realized value `g_{R*}` is grounded in `r` by its nature (§3.3). With N1–N3-G that is a ⊳_G-cycle, and Reading G excludes it. The witness, with the same value and the same ⊳_D graph, is not excluded. [A] given §3.3's premises, [P] for the classification | green |
| K2(a) | K_dec has no partition-defined term. Its metric-dependent stress-energy terms co-constrain (Lemma U). A precondition holds for K_dec and the witness alike: under N5-G, Substratum.md:385's "property of the classical dynamics of the partition boundary" must be read as ⊳_D, or as grounding in the classical dynamics of the cells the metric picks out, since read as grounding in the partition it makes OI's own metric cyclic (U2Ar3:617–620). The verdict does not use this precondition to separate completions. [P] | green |
| K2(b) | `G_μν[g]` co-constrains (Lemma U), as C2(b) of unit 2(a) requires. [A] | green |
| K2(c) | The gap equation matches the classical `T_cl` to the emergent `T_Q` and fixes ħ. The two "refer to the same physical degrees of freedom" (GR:144), and ħ grounds nothing upstream of the geometry (U2Ar3:246–248). CoC, no cycle; consistent with "non-circular" (GR:154). [P] | green |
| K3 | §2.4: every corpus use reads as CoC for terms grounded in the metric. GR:358 and GR:400 "feed back" would be cycles if read as Gr, and each paragraph supplies the CoC reading. No corpus use is classed differently from the witness's term. [P] | green |
| K4 | The decisive step (Lemma U, Corollary E) uses N1–N2-G, N3-G, N3′, transitivity, N5-G and the definition of the witness's term (U2Ar3:315–328). Lemma F and F3 use P-F, P-D and P-S. None is on the excluded list of §1.1. GR:340 s.1's first clause ("Spacetime geometry is part of the classical substratum") enters only through the witness's definition (U1r5:192; U2Ar3:296–297), as in both earlier units. [A] for the list | green |
| K5 | K1's pair has identical values and ⊳_D graphs and differs in ⊳_G. [A] | green |

K1–K5 are green, so the verdict is written.

***

## 6. Pressure tests (§A.31)

The tests run depth-first. Branch (A), the branch favourable to decoupling (B_G true gives (ii-G)'s
exclusion of K_cpl^conv), is tested first and with the most skepticism. Branch (B), the branch this record
adopts, is tested next.

### 6.1 Branch (A): can B_G be supported?

- **A1. "Feed back" (GR:358, GR:400 Reading 1) as grounding.** Read as Gr, each is a cycle by Lemma U.
  GR:358 assigns the gravitating vacuum energy to `H_tot`. Under §8.3, GR:400's piece is a classical
  microstate difference. Verdict: not support for (A); the two passages read as CoC. [P]
- **A2. GR:340 s.1, "evolves via Einstein's equations", as a governing law.** Its terms are classical
  (with P11), so it gives no emergent term a grounding role. The clause is also excluded as a premise
  (§1.1). Verdict: not support. [P]
- **A3. Strong emergence: a non-fundamental law whose macro terms ground micro or macro states
  ("downward").** This is F3's substance without fundamentality. It conflicts with Substratum.md:387–389
  (GR as projection "by averaging"; the fundamental object `(S, φ)`) and with GR:342 (no substance-level
  primitives). In case β it also meets Lemma U. Verdict: (b2). [P; L, recalled: the strong-emergence
  literature]
- **A4. Convention-dependence.** Claim: a φ-derived law cannot contain a convention-fixed term, so if
  K_cpl^conv holds it holds as a governing law, which forces B_G.
  - Once `Z` is fixed, `ρ_Z ∘ T ∘ Π` is a definite function on configurations. Whether the realized
    metrics satisfy the equation is a fact about `φ`'s realizations.
  - If a φ-derived law had this form, `Z` would be selected by `φ` and would not be a convention (§4.3).
  - Verdict: not support for (A). The question goes to QU5(b) of unit 2(a). [P]
- **A5. Diachronic grounding.** With grounding taken between time slices, a term at `s` could ground the
  metric at `s′ > s`. With a static-patch partition at each slice, the chain
  `g(s) ⊳_G Π(s) ⊳_G r(s) ⊳_G t(s) ⊳_G g(s′)` is acyclic, so N5-G does not forbid it.
  - Such a ground needs either F3 (governing status) or macro-to-micro grounding (A3). Both are (b2).
  - On P-D, `x(s′) = φ^{s′−s}(x(s))` is grounded in `x(s)` and `φ`, and not in a coarse-grained property
    of `x(s)` [P].
  - With GR:40's event-horizon partition, `Π(s)` depends on the future metric, and the chain closes again
    (AW-tel, U2Ar3:770–771).
  - Verdict: not support for (A). In this branch the refutation rests on P-F and P-D, not on N5-G. The
    witness is static, so the slice question does not change its classification. [P]
- **A6. The metric as itself emergent (GR:693, "the framework's own emergent-metric geometry").** If the
  definition of the metric passed through the emergent description (for instance through the light-cone
  speed of emergent excitations), OI's own metric would be C1-type. Reading G would then exclude OI's
  metric independently of any law term. This bears on Reading G's coherence with GR:693, not on B_G.
  Verdict: not support for (A); recorded as AW-metric (§9). [P]

**Branch (A) result.** No formalization yields (A). [A], [P]

### 6.2 Branch (B): is the refutation sound?

- **B1. N5-G is not a corpus premise.** B_G is defined only on Reading G, which includes N5-G. Without
  N5-G, Reading G's reductio is unavailable and B_G excludes nothing. The verdict is scoped to Reading G.
  Verdict: holds, scoped. [P]
- **B2. Is N1–N2-G (case β) forced?** The corpus gives the partition two grounds.
  - (β) GR:40 and GR:346: the partition is defined by the metric's causal structure.
  - (α) Main:48, Lemma 2: the partition is "the definition of embedded observation", `V ⊊ S`, with no
    metric. Main:26 speaks of "degrees of freedom beyond causal reach" without a metric. GR:40 says the
    horizon "implements" Lemma 2's partition.
  - In case α, `Π` is not grounded in `g`. Lemma U does not apply, and Reading G's reductio fails at
    N2-G, so Reading G excludes neither the witness nor C1 (K1 fails for Reading G in case α). B_G could
    then hold without a cycle on F3, which (b2) still excludes; on F1 and F2 it would be idle, since
    Reading G draws no exclusion from it.
  - Verdict: the outcome "Reading G does not exclude the witness's field equation" holds in both cases.
    The formal refutation of F1 and F2 is case β's. Recorded as AW-part (§9). [P]
- **B3. Overdetermination.** Could `t` be an additional partial ground of `g` beside `(S, φ, x₀)`? Lemma
  U excludes any edge `t ⊳_G g`, whatever other grounds `g` has. Verdict: holds. [A]
- **B4. Is N3′ (a function of `r` is grounded in `r`) too strong?** Lemma U needs only `g ⊳_G t`. The
  witness's `ρ_Z` reads `ε`, `N_modes = A/ε²` and `n` from the class (U2Ar3:306–313), and `A` is a
  property of the realized horizon, so `g ⊳_G A ⊳_G ρ_Z` holds through the horizon area alone, without
  N3′ [P]. Verdict: holds.
- **B5. Does the result make Reading G trivial?** No. On Reading G, (ii-G) excludes C1-type
  configurations. It does not exclude semiclassical boundary laws. That is Reading E's reach against the
  completions GR:350 contrasts (U2A-F7, U2Ar3:747), on Reading G as well. This weighs on which
  reading GR:342's "three independent requirements" intends. It does not bear on what follows from the
  premises. Verdict: holds; recorded as a finding (BG-F4). [P]
- **B6. Is co-constraint, as defined, the right negation?** Gr and CoC are exclusive (§2.3). An item
  with no ground at all is excluded for the metric by P-F. The third case, a term with no common base, is
  excluded for the witness by Main:686 and N1–N3-G. Verdict: holds. [P]

**Branch (B) result.** The refutation holds on Reading G in case β, conditional on N5-G. In case α B_G is
idle. F3 fails in both cases by (b2). [A], [P]

**§A.31 fixed point.** Not claimed. Passes and NEW findings: pass 1 (formalizations, §2–3), 1 NEW
(BG-F1); pass 2 (corpus uses, §2.4 and §4.2), 0 NEW (BG-F2 is ELABORATING); pass 3 (branch (A)), 0 NEW;
pass 4 (branch (B)), 1 NEW (AW-part). Two consecutive passes without a NEW finding is short of the 3–4
the fixed point requires.

***

## 7. Verdict from the rule

- **F1:** false at every OI world in case β (Lemma U). Clause (b1). [A]
- **F2:** equivalent to the non-realizability of the witness's law (Corollary E). Wherever the law is
  realized, the term co-constrains. Clause (b1). [A]
- **F3:** contradicts P-F, P-D and P-S. Clause (b2). [P]
- **No formalization meets (A)** (§6.1).
- **Controls:** K1–K5 green (§5).

**Outcome: (B).** B_G is refuted on Reading G in case β, conditional on N5-G, and wherever a boundary law
with an emergent-class term holds, the term co-constrains. In case α, B_G is idle (F1, F2) or excluded
(F3). The decisive step is Lemma U. Its consequence is that the "only if B_G" condition of Reading G's
exclusion is never met by a realization of the witness. What remains about the witness is G3's
determination question (§4.3), not B_G.

***

## 8. Consequences

All items adopt no premise and propose no manuscript change. Items that concern the witness keep unit
2(a)'s scope: exact de Sitter and M1.

### 8.1 Requirement (ii) and (ii-G)

- On Reading G, requirement (ii) excludes configurations whose metric is by its nature a quantity of the
  emergent description (C1-type). It excludes no field equation whose metric has a ground in
  `(S, φ, x₀)` [A], [P].
- This matches Reading E's reach (U2A-F7). On every reading examined, GR:346's argument excludes the
  quantum-first configuration and no semiclassical boundary law independently of G3 or of an added
  premise [P].

### 8.2 (ii-L)

- Unit 2(a)'s candidate independent motivation for (ii-L) and (ii-G), "GR:342's ontological commitment
  read as N5-G … conditional on B_G" (U2Ar3:82–85, :829–832), supplies no exclusion of a field equation.
  With B_G as F2, the condition is the exclusion itself (Corollary E) [A].
- (ii-L) stays what unit 2(a) found on Readings E and D: an added premise, silent under Z_0, which
  excludes a K_cpl^conv member only when `ρ_Z` varies through the partition and §8.3 is not in force
  (U2Ar3:684–696) [A], [P].
- Holding it under §A.29 would need an independent motivation other than GR:346 and GR:342 [P].

### 8.3 (DZ)

- (DZ) for the convention-fixed offset receives no support from GR:346's argument on any reading
  examined [P].
- Its remaining supports are:
  - G3, which by determination would decide which law holds;
  - the posits P11 (GR:340 s.2, GR:352), GR:575 and (ii-S) (GR:400 Reading 2), which the corpus does not
    adjudicate;
  - (ii-L) held as an added premise. [P]
- The world-level content of (DZ) on the de Sitter class is unchanged (U2Ar3:697–714).

### 8.4 Unit 1 Part 2 (r5 and its forward correction)

- U1r5:48–57 makes Part 2 "conditional on (ii-L)". CORR X-1 makes it "Conditional on Reading G of GR:346
  and the bridge premise B_G (open)", with B_G open at X-1 to X-20.
- If this verdict stands review, Part 2's exclusion of K_cpl^conv from GR:346 holds on no reading. Part 2
  would then be conditional on (ii-L) as an added premise, or on P11, GR:575 or (ii-S), and its open
  question would be G3's (§4.3) [P].
- CORR's clause "B_G … fails, conditionally, if the boundary law is a coarse-grained consequence of `φ`
  … The first condition is G3 (open); the corpus states no view on the second" (CORR X-1) would read as
  §4.1–4.2 state.
- Unit 1 Part 1 is unaffected. Reading G does not exclude K_cpl^free (§3.4) [P].
- This record edits neither r5 nor CORR.

### 8.5 Unit 2(a)

- Under unit 2(a)'s own rule, Reading G would meet clause (B)(b) in case β (Corollary E) and clause
  (B)(a) in case α (B2). Unit 2(a)'s outcome would then read (B) on the de Sitter class under M1, with
  the witness unchanged [A] for the classification, [P] for the readings.
- Unit 2(a)'s §8.3 table rows for "(ii-G) with B_G" (U2Ar3:469–470) state what follows given B_G. With
  B_G false at every realization, Reading G admits GR:400 Reading 1 in both §8.3 branches.
- AW-loop is then absent on Reading G, as on Reading E (U2Ar3:715–720), and stands only for Reading D
  (whose N5-D is false) and for (ii-L) held as an added premise [P].
- This record does not edit unit 2(a) r3.

### 8.6 What does not change

- The witness, its algebra and its scope (U2Ar3 §3).
- Unit 2(a)'s findings on Readings E, D and S.
- U2A-F2 (Z_0).
- The world-equivalence on the de Sitter class.
- GR:579's open question.
- G3's open status.
- No claim about Λ is made.

***

## 9. Findings

| ID | Finding | Class | Support |
|---|---|---|---|
| BG-F1 | On Reading G, with N1–N3 in ⊳_G, a law term grounded in the realized metric (as every emergent-class term at the metric's own partition is) cannot ground that metric (Lemma U). B_G as a property of a realized witness is false at every world satisfying Reading G's premises. As a law-level claim it is logically equivalent to the witness's non-realizability, so it supplies no exclusion of its own. The restriction to "emergent-class" terms marks no difference for grounding: the Einstein left side falls under the same lemma. | NEW (structural: the bridge premise had been treated as an open property of the completion; it is settled by Reading G's own reductio) | [A] §3.1–3.2 |
| BG-F2 | Unit 2(a)'s condition (a) on B_G conflates the ontological status of the boundary law (that it holds in virtue of `(S, φ)`, fixed by P-F, P-D and P-S) with its derivation (G3, open). Its condition (b), "the corpus states no view", is too broad: SM:158, Substratum.md:387, GR:144, GR:581 and Main:686–692 state co-constraint for the corpus's own derived relations. | ELABORATING (§A.19 correction of a negative claim; hidden assumption in "That is G3") | [P] §4.1–4.2 |
| BG-F3 | The governing reading of B_G (F3) contradicts the stated ontology: GR:342, Substratum.md:389, Main:44 and :54, A1–A6, SM:158, GR:352 and GR:655. | CONFIRMING (of unit 2(a)'s A8 skepticism, U2Ar3:599–601) | [P] §3.3 |
| BG-F4 | On Reading G, requirement (ii) excludes the C1-type configuration and no semiclassical boundary law, as on Reading E (U2A-F7). | ELABORATING (charity marker on GR:342's "three independent requirements") | [P] §6.2 B5, §8.1 |

**Productivity test (§1.5).** BG-F1 is strictly stronger than "B_G open, narrowed to G3 and an unstated
view of laws". It replaces an open bridge with a lemma and a corollary. It constrains a claim: unit 1
Part 2 and unit 2(a)'s Reading G clause (§8.4–8.5). BG-F2 exposes an assumption. The unit meets the test.

**Assumption-watch markers.**

- **AW-part (B2).** The corpus grounds the partition in two ways: in the observer's embedding, without a
  metric (Main:26, Main:48), and in the metric's causal structure (GR:40, GR:346). Reading G's reductio
  needs the second. Sites to check: GR:40 ("implements the causal partition of Lemma 2"), GR:346 s.1–s.2,
  and book/ch07-gravity.md:183. No change is proposed.
- **AW-metric (A6).** GR:693 calls the metric "the framework's own emergent-metric geometry" and encodes
  it through "the framework's own dispersion relation". If the metric's definition passes through the
  emergent description, Reading G's reductio applies to OI's own metric, C1-type, independently of any
  law term. Sites to check: GR:693, GR:340 s.1, GR:342. No change is proposed.
- **AW-ground (U2Ar3:760–766), updated.** Under N5-G, every corpus statement of the form "the metric is a
  property of / determined by the partition boundary" (Substratum.md:385, :393) is ⊳_D or CoC. Lemma U
  covers these as a family. No change is proposed.

***

## 10. Literature

All entries are recalled and were not re-read. No verdict rests on any of them.

- K. Fine, "Essence and modality", *Philosophical Perspectives* 8 (1994); K. Fine, "Guide to ground"
  (2012); G. Rosen, "Metaphysical dependence: grounding and reduction" (2010): transitivity and
  irreflexivity of strict partial ground, and definitional (essential) dependence as a case of ground.
  These are the premises used in §2.2 and Lemma U.
- E. Bliss (2014) and N. Thompson (2016): arguments that non-well-founded or symmetric grounding is
  coherent. This is the dissent from N5-G already recorded in unit 2(a); B1 scopes the verdict to it.
- T. Jacobson, "Thermodynamics of spacetime: the Einstein equation of state", *Phys. Rev. Lett.* 75,
  1260 (1995): the Einstein equation obtained as an equation of state from the Clausius relation at local
  Rindler horizons. This is the route GR:162 and SM:160 use, and its standard reading treats the field
  equation as a relation among thermodynamic quantities.
- D. Lewis on Humean supervenience; T. Maudlin, *The Metaphysics Within Physics* (2007); D. Armstrong,
  *What Is a Law of Nature?* (1983); and the debate on whether Humean laws can explain the facts they
  summarize (B. Loewer; M. Lange, in *Philosophical Studies*, around 2012–2013; details not verified).
  This is the regularity/governing disagreement. §4.2 does not need it, because F3 is excluded by the
  stated ontology.
- The strong-emergence and downward-causation literature (for example J. Wilson, *Metaphysical
  Emergence*, 2021): the position node A3 examines.

***

## 11. Owner questions

- **QB1. Review routing.** QU5 routes this unit to an independent review and then the ChatGPT exact-head
  review. Should the independent review also re-apply unit 2(a)'s rule to Reading G (§8.5), or is that
  left to a forward note after review?
- **QB2. Forward notes.** If the verdict stands review, should unit 2(a) r3 and CORR r1 receive forward
  notes (§8.4–8.5), as QU4 did for unit 1? The notes would state that Reading G's exclusion is never met
  by a realization, that Part 2 rests on (ii-L) as an added premise or on P11, GR:575 or (ii-S), and that
  the open question is G3's. No record would be edited.
- **QB3. QU2 follow-up.** With Reading G supplying no independent motivation, does (ii-L) stay a §A.29
  candidate, which would need a different motivation, or is it set aside?
- **QB4. QU3 follow-up.** For a future manuscript unit, BG-F4 and U2A-F7 give one scoping for GR:346,
  GR:342 ("forced") and book/ch07-gravity.md:183–187: requirement (ii) excludes a metric that is a
  quantity of the emergent description, and does not by itself exclude a semiclassical boundary law. No
  change is proposed here.
- **QB5. Next unit.** Candidates:
  - (a) AW-part: what grounds the cosmological partition (Main:48 against GR:40), on paper;
  - (b) AW-metric: whether GR:693's metric passes through the emergent description;
  - (c) unit 2(a)'s QU5(b): whether OI's premises fix `Z`;
  - (d) closing the G3 offset thread after review, with G3's determination question left open.

***

## 12. Limits

- The logic is by hand and is not machine-checked.
- Lemma U holds on Reading G in case β and is conditional on N5-G, which the corpus does not state and
  which the literature contests.
- The readings of corpus text (§2.4, §4.2) are [P].
- P-F is a stated commitment whose derivational support reaches weak-field consistency only
  (GR:691–697).
- The consequences for the witness keep unit 2(a)'s de Sitter and M1 scope.
- The rule and the analysis land in one commit. The rule was written after the sources were read and an
  outline formed (§1).
- The §A.31 fixed point is not reached.
- No claim is made about K_cpl^conv's admissibility under G3, or about Λ.
