# G3 unit 2(a) (r2): does GR:346's non-circularity argument exclude a self-consistent fixed point?

**Scope.** This is a paper-only test under Issue #873, continuing unit 1 (PR #1275).

- Authorization: #873 c.6863416405 (`amaybaum`, 2026-11-13T19:58:10Z), Q4: "G3 unit 2(a)", "a
  paper-only test of whether GR:346's non-circularity argument (ii-L) survives self-consistent fixed
  points. It must not assume the conclusion. The test adds no new premise, changes no manuscript and
  starts no Lean build." Q7: "(ii-L) is not adopted as a §A.29 premise for now."
- Unit 1: `G3-UNIT1-r5.md` on branch `research/g3-offset-873-20261113` at
  `e81e4fb23f4a5abda910cc69e9f79f93e6ae1523`, with `NOTES-r5.md`, `CONFIRM-r3.md` and `CONFIRM-r4.md`.
  "U1 §n" and "U1 B5" refer to that file.
- Review of unit 1: PR #1275 review 5896999577 (posted by `amaybaum`, 2026-11-13T19:41:56Z, at
  `e81e4fb2`). Its "important limit": the exclusion of K_cpl^conv under (ii-L) "rests on a reading of
  GR:346's *order-of-derivation argument*. It is not a demonstrated no-fixed-point theorem."
- This revision: r1 is `G3-UNIT2A-r1.md` at `46a548fb19f3b5846ed62878c182c22e715d6735`. Its independent
  review is `REVIEW-U2A-r1.md` (REVISE) at `a87c410d`. Dispositions are in `RESPONSE-U2A-r1.md`.

This record proves no theorem in Lean, runs no computation, changes no manuscript and adopts no premise.

**Source snapshot.** `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`. Every `file:line` refers to
that commit.

**Support labels**, as in unit 1: [K] kernel-checked declaration on `main` (read, not rebuilt); [A]
exact algebra or elementary logic, done by hand here; [P] a paper derivation or a reading of a paper
argument; [L, recalled] literature recalled from memory and not re-read, on which no verdict rests;
"Conjecture" an unsupported proposal. **Conditional** marks a claim that holds only under the
hypotheses it names.

**Convention.** As in unit 1: signature (−,+,+,+), c = 1, `G_μν + Λ g_μν = 8πG T_μν`; a uniform vacuum
energy density ρ has stress tensor `−ρ g_μν`. ħ is kept explicit.

***

## 0. Verdict

**Outcome (C), scoped.** GR:346's argument, written as a premise list without its conclusion, can be
read in three orders. On two of them it does not exclude the fixed point of §3. On the third it excludes
it given one bridge premise, which GR:346 does not state and which this record cannot settle on paper.

- **Order of explanation (Reading E).** The argument is valid, establishes (ii-W) and does not exclude
  the witness. Its step "no entry point" (N5) holds for specifications, and an implicitly specified
  fixed point has an entry point: the family of classical metrics and the maps defined on it [A, §4.1].
- **Order of determination (Reading D).** The argument excludes the witness only through N5-D, which is
  false as a general principle: joint equations with a solution realize a cycle of value dependence
  [A, §2.2].
- **Order of existence or emergence (Reading G).** The argument is valid. Its rule N5-G, that "emerges
  from" is well-founded, is not refuted by any equation model and is not equivalent to the exclusion
  being tested. It excludes the witness if and only if the witness instantiates N4-G. That holds exactly
  when a term of the boundary metric's law that is a function of the emergent class grounds the realized
  metric, rather than only co-constraining it. This is the bridge premise B_G (§2.4) [P].
- **The gap.** Whether a term in the boundary metric's law that is a function of the emergent class
  grounds the metric (excluded by N5-G) or only co-constrains it (admitted). §4.5 narrows it.
  - B_G fails, conditionally, if the boundary law is a coarse-grained consequence of the substratum
    dynamics in which the realized metric is grounded in `(S, φ)` directly.
  - Whether OI's boundary law has that status is G3, which is open (GR:12).
  - Even for a derived law, the corpus states no view on whether its terms ground its solutions.
- **Reading set.** r1 examined Readings E, D and S and a mixed reading, and omitted Reading G
  (REVIEW-U2A-r1, U-1). The decision rule of §1 is unchanged. It quantifies over every reading of the
  premise set, and with Reading G included it yields (C).
- **Witness.** A fixed-point model in the K_cpl^conv class on the de Sitter family (§3). It uses two
  conventions in unit 1's class, constructed rather than taken from the corpus: GR:362's mode sum with an
  added IR limit at the horizon scale (Z_I), and unit 1's normalization `ρ = ħe/v` (Z_II). Neither is the
  corpus's own convention. Under each, the loop
  partition → emergent class → convention-fixed `e_Z` → metric → partition
  closes with a nonzero response. It has exactly one fixed point for every completion constant in an
  open interval, and a calibrated constant reproduces any given de Sitter radius [A].
  - The witness satisfies (i), (iii), (Adm1)–(Adm3) on its solution set, and (ii) on Reading E [A], [P].
- **Controls.** C1–C4 (§1.4) are green on every reading (§4.3). C1′ (added at review; not part of the
  rule as first written) shows that on Reading E requirement (ii) adds nothing to (i) against the
  completions GR:350 contrasts. On Readings D, S and G, (ii) excludes them itself.

**Scope.** The model is restricted to exact de Sitter metrics and to assumption M1 (`n` and `ε`
independent of `R`). It does not show that K_cpl^conv is admissible outside de Sitter. It does not show
that OI's premises admit K_cpl^conv either: other posits exclude it (P11, GR:575, (ii-S)).

**Consequences** (§6), scoped to the de Sitter class and to M1.

1. On Readings E and D, GR:346 does not supply (ii-L). On those readings (ii-L) is an added premise
   [P]. On Reading G, GR:342's ontological commitment ("Classical spacetime is logically prior to QM; QM
   is emergent") gives, through its second clause and N5-G, a candidate independent motivation for an
   exclusion that is stronger than (ii-L). Whether that exclusion applies is the gap.
2. (ii-L), even as an added premise, is silent under GR:362's density estimate as written (Z_0). That
   density is constant on the de Sitter family, and the completion built on it has the field equations
   of K_dec with a shifted constant [A]. The corpus's emergent vacuum energy of GR:378(i), GR:388 and
   GR:400 does depend on `H` through the mode count. Its loop is the Reading 1 case. Reading G, which
   concerns grounding and not covariation, reaches Z_0 given B_G [P].
3. With the completion constant left free, the members of §3 realize the same de Sitter worlds as K_dec
   with Λ₀ left undetermined [A]. Whether the split of a constant between source and Λ carries a
   fine-tuning is unit 1's statement (U1 §3.1 (b)), and this record does not change it.
4. §8.3 is applied uniformly (§4.2).
   - With §8.3 in force, (ii-L) excludes neither part of K_cpl^conv. Reading G with B_G excludes the
     absolute part and admits the configuration-differential part. That is the position the corpus
     states (GR:358, GR:400, GR:575), conditional on §8.3 and on B_G.
   - Without §8.3, (ii-L) and Reading G with B_G also exclude GR:400 Reading 1.
5. Unit 1's AW-loop tension is absent on Reading E. On Readings D and G it stands, conditional on §8.3,
   as unit 1 records.

This record makes no claim about the magnitude of Λ.

***

## 1. Decision rule

This section fixes the rule and the controls. By the writer's account it was written before §2–§6 of
r1, after the sources had been read (NOTES-U2A-r1 §3). No separate commit pins it. §1.1–§1.5 are
unchanged from r1 except for the reason given for excluding GR:340 (§1.6). §1.6 lists what was added at
review.

### 1.1 The admissible premise set

"GR:346's argument, as stated" consists of:

- the four sentences of GR:346;
- the premises those sentences cite or presuppose: the definition of the partition by the causal
  horizon (GR:40, cited as §2.1 at GR:346), and the trace-out over a specific partition (GR:344, citing
  Main §1.4).

Excluded from the premise set, because each is either a conclusion of (i)–(iii) or a separate posit:

- GR:342's "This ordering is forced …" and "not the reverse" (stated as the conclusion of (i)–(iii));
- book/ch07-gravity.md:187, "not a stipulation but a structural consequence" (the same conclusion);
- GR:340 s.1, "the metric evolves via Einstein's equations *before* the trace-out" (the ordering, which
  GR:342 states as the conclusion of (i)–(iii)), and GR:340 s.2, the geometry-first source (P11 of unit
  1, a posit: GR:352);
- GR:575, absolute emergent levels do not gravitate (the geometry-first proposal, GR:579).

Requirements (i) (GR:344) and (iii) (GR:348) are checked separately, as the brief requires.

### 1.2 Outcomes

- **(A) Excludes.** Some reading of the premise set (§1.1) yields a valid argument whose premises are
  neither refuted by an explicit model nor equivalent to the exclusion being tested, and that argument
  rules out every fixed point of the loop. The step that does so is named.
- **(B) Does not exclude.** Both of the following hold.
  - Every reading of the premise set either (a) fails to rule out the witness below, or (b) rules it out
    only through a premise that the witness refutes as a general principle, or that is equivalent to the
    exclusion being tested.
  - A witness is given: a fixed-point model inside the K_cpl^conv class, with existence (and uniqueness
    where claimed) shown by exact algebra, satisfying (i), (iii) and unit 1's admissibility conditions
    (Adm1)–(Adm3) on its solution set.
- **(C) Unresolved.** Neither (A) nor (B) is established. The precise gap is stated: a reading whose
  premise cannot be settled on paper, or a witness whose membership or existence cannot be shown.

### 1.3 What counts as a witness

- **Membership.** The field equation is `G[g] + Λ^Z g = 8πG(T^cl − ρ_Z g)` with `ρ_Z` a function of the
  emergent class `[r]` through a zero-point convention `Z` (U1 §2, §3.1).
- **Genuine loop.** `ρ_Z` varies with the metric through the partition: `dρ_Z/dR ≠ 0` on the family. A
  convention with constant `ρ_Z` is not a witness, because its loop is degenerate.
- **Not rigged.** Fixed points exist for an open set of completion constants, not only for one value.

### 1.4 Controls

- **C1 (positive control, the formalization is not vacuous).** Under the reading used for the verdict,
  the formalized argument must exclude the configuration GR:346 targets: a metric with no specification
  except as a function of the realized emergent description.
- **C2 (negative controls).** No reading used may exclude (a) K_dec; (b) the nonlinearity of the Einstein
  equation, in which the metric's value depends on itself; or (c) the corpus's own uses: GR:400
  Reading 1 (GR:388, "the self-consistent emergent-QFT calculation") under §8.3's identification, and
  the gap equation, which the corpus calls non-circular (GR:154; book/appendix-c-objections.md:259).
- **C3 (genuine loop).** §1.3.
- **C4 (not rigged).** §1.3.

A verdict is written only if C1–C4 are green. A failed control voids the verdict, and the outcome is
then (C) with the failed control named.

### 1.5 Productivity test (§A.31)

The unit is a gem if it yields a fact strictly stronger than the review's statement (that (ii-L) "is not
a demonstrated no-fixed-point theorem") and the fact either constrains a claim or exposes an assumption.
Otherwise it is recorded as a coherence check only.

### 1.6 Changes at review

- **Reading set.** §1.2 quantifies over every reading of the premise set. r1's enumeration (§2.4 of r1)
  omitted the order of existence or emergence (REVIEW-U2A-r1, U-1). r2 adds it as Reading G (§2.2,
  §2.4). The clauses of §1.2 are unchanged, and r2 applies them as they stand.
- **Control C1′, added at review (REVIEW-U2A-r1, U-5).** The formalization must account for GR:350's
  statement that (i)–(iii) fix the metric at the partition boundary and not laboratory fields. The
  result is reported for each reading (§4.3). C1′ bears on which reading GR:346 intends. The outcome
  rule of §1.2 does not depend on it, because §1.2 quantifies over every reading.
- **§1.1.** The excluded set is unchanged. Its GR:340 entry now separates s.1 (the ordering) from s.2
  (P11) (REVIEW-U2A-r1, U-9).

***

## 2. GR:346 as a premise list

### 2.1 The premises

| # | Premise | Source | Kind |
|---|---|---|---|
| N1 | The partition `Γ_V × Γ_H` is defined by the observer's causal structure: `Γ_H` is the set of degrees of freedom beyond causal reach. | GR:346 s.1; GR:40 | definition |
| N2 | Causal structure is determined by the null geodesics of the metric. | GR:346 s.2 | definition |
| N3 | The emergent quantum description is produced by the trace-out over a specific partition; QM is emergent. | GR:344; GR:342 ("QM is emergent"; "the trace-out producing QM") | definition |
| N4 | Hypothesis for reductio: the metric is derived from QM. | GR:346 s.3 | hypothesis |
| N5 | A chain of "derived from" links that returns to its start is "a circular dependency with no entry point" and yields no derivation. | GR:346 s.3 (implicit) | inference rule |
| C | "The circle breaks only if the metric exists prior to the partition." | GR:346 s.4 | conclusion: ¬N4 |

[P] for the transcription. Each entry is a quotation or a direct paraphrase of the cited line.

### 2.2 Three orders

- **Order of explanation (⊳_E).** `X ⊳_E Y` if the specification of `Y` takes `X` as an input. A
  specification is either explicit (`Y := f(X)`) or implicit (`Y :=` the unique element of a stated set
  that satisfies a stated condition). In the implicit case the inputs are the set, the condition and
  the maps the condition uses. The element that the condition selects is not an input.
- **Order of determination (⊳_D).** On a stated family of configurations, `X ⊳_D Y` if the value of `Y`
  is a non-constant function of the value of `X`, either through a map or through a joint equation.
- **Order of existence or emergence (⊳_G).** `X ⊳_G Y` if `Y` is what it is partly in virtue of `X`.
  The textual sources are GR:342 ("logically prior … QM is emergent") and GR:346 s.4 ("exists prior").
  ⊳_G concerns what grounds what. It is not a relation between values, and an equation model fixes
  values only.

**N5 under each order.**

- **N5-E [A].** A chain of explicit specifications that returns to its start specifies nothing. This is
  the well-foundedness of definitions, and it is true.
- **N5-D [A].** "A ⊳_D-cycle cannot be realized." This is false as a general principle. A pair of joint
  equations `x = f(y)`, `y = h(x)` with exactly one solution realizes a ⊳_D-cycle. Every nonlinear field
  equation realizes `g ⊳_D g`, including the Einstein equation.
- **N5-G [P].** ⊳_G is well-founded: nothing is grounded, even partly, in something that is grounded in
  it. This is a general asymmetry thesis. No equation model bears on it, since the existence of a
  solution says nothing about which relatum grounds which. It is the common position in the recalled
  literature on grounding, which also has dissenters (§8) [L, recalled]. It is not equivalent to the
  exclusion being tested: it constrains every cycle of emergence, including cycles that run through no
  dynamical law.

**The text [P].** GR:342 opens:

> "**Ontological commitment.** Classical spacetime is logically prior to QM; QM is emergent."

It then adds the gloss "It is a claim about the direction of the derivation chain — that the trace-out
producing QM presupposes the classical geometric structure, not the reverse". GR:346 uses "derived",
"derivation would require" and "entry point", and ends "exists prior".

- "Derivation", "entry point" and "presupposes" are terms of specification (⊳_E).
- "Logically prior", "QM is emergent" and "exists prior" are terms of ontological dependence (⊳_G).
- The first clause of GR:342 s.1, "Classical spacetime is logically prior to QM", is the ordering that
  GR:342 states (i)–(iii) force, so §1.1 excludes it as a premise. The second clause, "QM is emergent",
  is N3 in emergence form, and it is admissible.
- The corpus calls the gap equation non-circular (GR:154; book/appendix-c-objections.md:259). There ħ is
  fixed by matching a geometric quantity to an emergent one, and ħ grounds nothing upstream of the
  geometry. That use is consistent with both ⊳_E and ⊳_G, so it does not discriminate between them.

The text therefore supports both Reading E and Reading G. r1's choice of Reading E rested on a partial
quotation of GR:342 (REVIEW-U2A-r1, U-1).

### 2.3 The readings of (ii) in these terms

| Reading | In terms of §2.2 |
|---|---|
| (ii-W) (U1 B5) | `C` under ⊳_E. The specification of the metric takes no input defined through the partition. The metric is a classical datum, definable before the partition. |
| (ii-L) (U1 B5) | No ⊳_D-cycle passes through an object defined through the partition. The qualifier "through post-partition data" is a property of the route of specification. Without it, (ii-L) would forbid the nonlinearity of the Einstein equation (C2(b)). |
| (ii-S) (U1 B5) | No object defined through the partition is an argument of the boundary metric's dynamical law, whatever its ⊳_D role. A ban on routes. |
| (ii-G) (this record) | `C` under ⊳_G. The realized boundary metric is not grounded, even partly, in a property of the realized emergent description. |

[P] for the mapping, which follows unit 1's definitions (U1 B5) for the first three rows.

### 2.4 Validity under each reading

- **Reading E** (N4 and N5 both in ⊳_E) [A]. Valid. N1–N3 give `metric ⊳_E causal structure ⊳_E partition
  ⊳_E QM`. N4 in ⊳_E closes a ⊳_E-cycle, and N5-E rejects it. The conclusion is (ii-W).
- **Reading D** (N4 and N5 both in ⊳_D) [A]. The inference is valid, but N5-D is false (§2.2). The
  argument is unsound, and it does not establish (ii-L).
- **Mixed reading** (N4 in ⊳_D, N5 in ⊳_E) [A]. The chain `QM ⊳_D metric ⊳_E … ⊳_E QM` is not a
  ⊳_E-cycle, so N5-E does not apply. The argument is invalid.
- **Reading S** (N4 read as "the metric's law has an argument defined through the partition") [A]. The
  step to "no entry point" requires that no specification of the realized metric exists. When the law's
  equation has a solution and a selection, an implicit specification exists (§4.1). The step then
  fails, and the exclusion holds only if the route ban is itself assumed. That ban is (ii-S), the
  exclusion being tested.
- **Reading G** (N3, N4 and N5 in ⊳_G) [P].
  - N3-G: the realized emergent description emerges from the realized partition (GR:342, "QM is
    emergent"; GR:344).
  - N1–N2: the realized partition is fixed by the causal structure of the realized metric.
  - N4-G: the realized metric is grounded partly in the realized emergent description.
  - Together these give a ⊳_G-cycle, and N5-G rejects it. The conclusion is (ii-G).
  - The argument is valid. Its premises are not refuted by an equation model (§2.2), and N5-G is not
    the exclusion being tested.
  - Whether a given completion instantiates N4-G is a further question. For the witness, it is the
    **bridge premise B_G**: a term of the boundary metric's law that is a function of the emergent class
    grounds the realized metric, and does not only co-constrain it.

***

## 3. The fixed-point model

### 3.1 Objects

- **Family.** Classical data `κ_R`, `R ∈ I := (qε, ∞)`, with `q > 0` a convention constant, that differ
  only in the metric. `g_R` is de Sitter with radius `R` (Hubble rate `1/R`). Per GR:340 the metric is
  classical substratum data. `T^cl` has no non-uniform part. A uniform classical part, if one is
  present, is absorbed into the completion constant `Λ_c` below (conditional, as in U1 B2(c), on a
  covariant continuum limit in which a uniform classical energy has vacuum stress).
- **Constants.** `G`, `ħ`, `ε`, `σ`, with `ħ = ε²/(4Gσ)` (GR:78; GR:42). ħ does not depend on `R`:
  "κ cancels" (GR:78), and ħ "depends only on local geometric quantities — not on the observer's
  worldline or horizon area" (GR:42) [P].
- **Partition.** `Π(g_R)` is the static patch of a geodesic observer. Its horizon is the event horizon
  of GR:40, a sphere of area `A(R) = 4πR²` (GR:378 with c = 1) [A]. The de Sitter isometry group acts
  transitively on geodesic observers, so every geodesic observer's partition is congruent [A].
- **Emergent class.** `[r](R)` is the reduced description at `Π(g_R)`. The model reads three items from
  it:
  - the cutoff `ε`;
  - the horizon mode count `N_modes = A/ε²` (GR:364: `N_modes = S_dS/σ`, with `S_dS = σA/ε²`) [P];
  - the number `n > 0` of mode species, each carrying `½ħω` per mode (GR:332).
- **Model assumption M1.** `n` and `ε` do not depend on `R` on the family. This is an assumption of the
  model, not a corpus result.
- **IR scale read from the class.** `ω_IR([r]) := q (4π/(ε² N_modes))^{1/2}`, which equals `q/R` [A].

### 3.2 Three zero-point conventions

Each is a map from `[r]` to a real number, as unit 1's `Z` is (U1 §2). The mode sum per unit volume
between frequencies `a` and `b` is `(b⁴ − a⁴)/(16π²)`. This is GR:362's "mode sum `k⁴/(16π²)`" with a
lower limit added [A]. Z_I and Z_II are constructed conventions; the corpus states neither.

- **Z_0 (GR:362's density estimate as written: cut off at `1/ε`).**
  `ρ_0 := nħ/(16π²ε⁴) =: α`. Constant on the family under M1.
- **Z_I (density with an added IR limit).**
  `ρ_I([r]) := (nħ/(16π²))(ε⁻⁴ − ω_IR⁴)`, so `ρ_I(R) = α − β R⁻⁴`, with `β := nħq⁴/(16π²)`.
- **Z_II (unit 1's literal form `ρ_x = ħ e_x/v`, `v > 0` a fixed constant, U1 §3.1).** `e_II` is the
  total ground value over the visible volume `V := (4π/3)R³` (recoverable from `N_modes`):
  `e_II([r]) := V · (n/(16π²))(ε⁻⁴ − ω_IR⁴)`, so
  `ρ_II(R) = ħ e_II/v = (nħ/(12πv))(R³ε⁻⁴ − q⁴R⁻¹)`.

[A] for each formula, given the definitions. Membership in unit 1's class rests on `ε`, `N_modes` and `n`
being data of the emergent class [P].

**The corpus's emergent vacuum energy [P].** GR:378(i) states that "the boundary entropy
`S_dS = σA/ε²` depends on `H` via `A = 4πc²/H²`, so the emergent vacuum energy inherits an
`H`-dependence", and GR:374, GR:388 and GR:400 evaluate that dependence. The vacuum energy the corpus
uses therefore varies across the de Sitter family through the mode count. Its loop is the GR:400
Reading 1 case. What is constant under M1 is GR:362's density estimate, Z_0, which GR:362 calls "a
dimensional identity".

### 3.3 The loop and the fixed-point condition

The completion is K_cpl^conv[Z]: `G[g] + Λ^Z g = 8πG(T^cl − ρ_Z g)` (U1 §3.1, λ = 1). Set
`Λ_c := Λ^Z` plus any absorbed classical uniform part.

- On `g_R`, `G_μν[g_R] = −3R⁻² g_μν` [A]. With `T^cl` uniform-free, `g_R` solves the field equation if
  and only if `3R⁻² = Λ_c + 8πG ρ_Z(R)` [A].
- **The loop map.** Given `R`: partition `Π(g_R)` → class `[r](R)` → `ρ_Z(R)` → the de Sitter radius
  `L(R) := (3/(Λ_c + 8πGρ_Z(R)))^{1/2}` that the field equation returns, where the denominator is
  positive.
- **Fixed point.** `L(R) = R` if and only if `F(R) = Λ_c`, where `F(R) := 3R⁻² − 8πG ρ_Z(R)` [A].

**Lemma FP [A].** Let `ρ_Z : I → ℝ` be continuous and non-decreasing. Then `F` is continuous and
strictly decreasing on `I`, and `F(I) = (F_∞, F_0)`, where `F_∞ := lim_{R→∞} F(R)` and
`F_0 := lim_{R→qε⁺} F(R)`.

- (a) If `Λ_c ∈ (F_∞, F_0)`, the loop has exactly one fixed point in `I`. *Proof.* The intermediate value
  theorem gives one, and strict monotonicity excludes a second.
- (b) Conversely, if a fixed point `R* ∈ I` exists, then `Λ_c = F(R*) ∈ (F_∞, F_0)`, and `R*` is unique.
  *Proof.* `F(R*) = Λ_c` lies in the open image `F(I)`; uniqueness is as in (a).
- (c) **Calibration.** For any `R₀ ∈ I`, the choice `Λ_c := F(R₀)` makes `R₀` the unique fixed point.
  This is unit 1's `Λ^Z_1 = Λ₀ − 8πGρ_Z(r₀)` with `r₀ := [r](R₀)` and `Λ₀ = 3R₀⁻²`.

### 3.4 Instances

**Z_I [A].** `F(R) = 3R⁻² + 8πGβR⁻⁴ − 8πGα`, and `F′(R) = −6R⁻³ − 32πGβR⁻⁵ < 0`.

- `F_∞ = −8πGα`.
- `F_0 = 3/(q²ε²) + 8πGβ/(q⁴ε⁴) − 8πGα = 3/(q²ε²)`, because `8πGβ/(qε)⁴ = 8πGα`.
- **Existence and uniqueness:** exactly one fixed point if and only if `−8πGα < Λ_c < 3/(q²ε²)`.
- **Closed form.** With `x := R⁻²`, `b := 8πGβ` and `L := Λ_c + 8πGα`, the condition is
  `b x² + 3x − L = 0`. Its positive root is `x* = 2L/(3 + (9 + 4bL)^{1/2})`, which is positive if and
  only if `L > 0`.
- **The genuine-loop control.** `dρ_I/dR = 4βR⁻⁵ > 0`.
- **The calibrated constant.** For a fixed point at `R₀`, `Λ_c + 8πGα = 3R₀⁻² + 8πGβR₀⁻⁴`. This is an
  identity of the model. It states how close `Λ_c` must lie to `−8πGα` for a given `R₀`, and it makes
  no claim about any observed value.

**Z_II [A].** With `K := 2nGħ/(3v) > 0`, `F(R) = 3R⁻² − K(R³ε⁻⁴ − q⁴R⁻¹)`, and
`F′(R) = −6R⁻³ − K(3R²ε⁻⁴ + q⁴R⁻²) < 0`.

- `F_∞ = −∞`, and `F_0 = 3/(q²ε²) − K(q³ε⁻¹ − q³ε⁻¹) = 3/(q²ε²)`.
- **Existence and uniqueness:** exactly one fixed point if and only if `Λ_c < 3/(q²ε²)`.
- **Equivalent form:** `K ε⁻⁴ R⁵ + Λ_c R² − K q⁴ R − 3 = 0`. For every sign of `Λ_c` its coefficient signs
  change once, so by Descartes' rule it has exactly one root in `(0, ∞)`. That root lies in `I` exactly
  when `Λ_c < 3/(q²ε²)`, in agreement with Lemma FP.
- **The genuine-loop control.** `dρ_II/dR = (nħ/(12πv))(3R²ε⁻⁴ + q⁴R⁻²) > 0`.

**Z_0 [A].** `ρ_0 = α` is constant, `dρ_0/dR = 0`, and the loop is degenerate. The fixed point is
`R* = (3/(Λ_c + 8πGα))^{1/2}` whenever that lies in `I`, and the field equation is K_dec's with
`Λ₀ = Λ_c + 8πGα`. Z_0 fails C3 and is not a witness. It is used in §6.

**A negative mode weight.** If the species weight is negative, as for a fermion-type `−½ħω` per mode
[L, recalled], then `ρ_Z` is decreasing and Lemma FP does not apply. For Z_I with `b < 0` the condition
is `|b| x² − 3x + L = 0`. It has two positive roots when `0 < L < 9/(4|b|)` (a double root at equality),
one when `L ≤ 0`, and none when `L > 9/(4|b|)`, before the restriction to `x < (qε)⁻²` [A]. GR:332's
convention, `½ħω` per mode, has positive weight, so the witness uses `n > 0`.

**An operational entry point (Z_I) [A].** The iteration `x_{k+1} = (L − b x_k²)/3`, started from any
trial classical metric, has slope `−2b x*/3` at the fixed point. It converges locally if and only if
`x* < 3/(2b)`. With `ε² = 4Gσħ` this is `R*² > n q⁴ ε²/(12πσ)`. The verdict does not depend on this
remark. It shows that a trial classical metric serves as a computational entry point for large `R*`.
The entry point is one of specification and computation, not of grounding (§4.1).

### 3.5 The other requirements and admissibility

- **(i) Definiteness (GR:344).** At the fixed point the metric is a definite classical de Sitter metric,
  and the partition is the static patch at `R*`. Under Z_I and Z_II with `n > 0` the fixed point is
  unique, so no selection is needed. With a negative weight, each of several fixed points is a definite
  classical solution: the multiplicity is that of a classical solution set, selected by classical data,
  and not a superposition [P].
- **(iii) Uniqueness of ħ (GR:348).** ħ does not depend on `R` (GR:42, GR:78), so it depends on no
  state. The geometry is classical [P].
- **(Adm1)–(Adm3) (U1 §2).** On the de Sitter family `ρ_Z(R*)` is constant on `M`, so the source is
  conserved, as for unit 1's constant `ρ_x(r)` [A]. `ρ_Z` is computed from diffeomorphism-invariant
  class data, so the source is natural [P]. The calibration `a_* = ħ` is unchanged, because the
  null-flux term `ρ g_μν k^μ k^ν` vanishes (U1 §3.2) [A].
- **What is not claimed.** Beyond exact de Sitter, `ρ_Z` would vary in time. U1 B3 then requires energy
  exchange or a running `G`. The partition is observer-relative, and the event horizon is defined by the
  future (§5, nodes A5 and A6). The model makes no claim outside the de Sitter class.

***

## 4. The argument applied to the model

### 4.1 The specification graph of the model [A]

| Step | Object specified | Inputs |
|---|---|---|
| S0 | the constants and the family `{g_R : R ∈ I}` of classical metrics | none from any partition |
| S1 | the map `Π : g_R ↦` static-patch partition | S0 |
| S2 | the trace-out map `T :` partition `↦ [r]` | S1 and the substratum |
| S3 | the map `[r] ↦ ħ` (GR:78); constant in value | S1 |
| S4 | the convention map `Z : [r] ↦ ρ_Z` | S2, S3 |
| S5 | the condition `F(R) = Λ_c` on `I` | S0–S4, as maps |
| S6 | the realized metric `g* := g_{R*}`, `R*` the unique solution (Lemma FP) | S5 |
| S7 | the realized partition `Π(g*)` and the realized class `T(Π(g*))` | S6 |

**In ⊳_E.** The graph is acyclic. The realized metric (S6) is specified before the realized partition
(S7), and the family of metrics (S0) before any partition map. The model satisfies (ii-W). The
realized description `T(Π(g*))` enters only at S7. The input to S6 is the map `T`, defined on all
candidate partitions, and not the realized description. [A]

**In ⊳_G.** The question is different. At S6, `R*` is fixed by `F(R*) = Λ_c`, which reads `ρ_Z(R*)`, a
property of the realized class `T(Π(g*))`. That class emerges from the realized partition (N3-G), which
is fixed by the realized metric (N1–N2). If the law's term `ρ_Z` grounds the realized metric (B_G), the
metric is partly what it is in virtue of a property of a description that emerges from it, and the
witness instantiates a ⊳_G-cycle. If the term only co-constrains the metric, there is no such cycle.
The map/value distinction answers ⊳_E and does not answer ⊳_G. [P]

### 4.2 The order of determination, and §8.3

**Value dependence [A].** On the family `I`, `R ⊳_D ρ_Z`, because `dρ_Z/dR ≠ 0` for Z_I and Z_II. At
fixed `Λ_c`, `ρ_Z ⊳_D L`, because `L` is strictly monotone in `ρ_Z`. The loop is a ⊳_D-cycle.

**§8.3, applied uniformly.** §8.3's identification of relative emergent differences with classical
microstate differences is conditional (GR:573–579). The test is run in both branches, and the same
branch is applied to the witness and to control C2(c).

- Write `ρ_Z(R) = ρ_Z(R₀) + Δρ_Z(R)`. The constant part `ρ_Z(R₀)` is an absolute level assigned by the
  emergent description (GR:575). The part that carries the loop is `Δρ_Z`, under Z_I equal to
  `−β(R⁻⁴ − R₀⁻⁴)`, a difference between configurations. By the rule's wording AUDIT item 2.9
  (AUDIT.md:371–378) classes such differences as relative. GR:400 classes the epoch-differential
  curvature response as "relative … in the sense of §8.3" [A] for the split, [P] for the classing.

| | §8.3 in force | §8.3 not in force |
|---|---|---|
| (ii-L) on the witness | Not excluded. `Δρ_Z` is a classical microstate difference, so the loop runs through no post-partition datum, and `ρ_Z(R₀)` carries no loop. | Excluded: the loop runs through `Δρ_Z`, a post-partition datum. |
| (ii-L) on GR:400 Reading 1 | Admitted (C2(c)). | Excluded. |
| (ii-G) with B_G on the witness | Excluded through the absolute part `ρ_Z(R₀)`, which is emergent (GR:575). `Δρ_Z` is classical and admitted. | Excluded through both parts. |
| (ii-G) with B_G on GR:400 Reading 1 | Admitted: its piece is classical. | Excluded. |
| (ii-W) | Excludes neither, in either branch. | Excludes neither. |
| (ii-S) | Excludes the witness, in either branch. | Excludes the witness. |

[P] for the table, [A] for the loop structure it rests on.

So "the witness violates (ii-L)" holds only without §8.3, and in that branch (ii-L) also excludes
GR:400 Reading 1. This is a fact about (ii-L), not about the verdict's reading.

### 4.3 Controls

| Control | Result | Status |
|---|---|---|
| C1 | Take a metric with no classical family to range over: one specified only as a quantity of the realized emergent description at its own partition. No S0 exists. Reading E excludes it as a ⊳_E-cycle. Reading G excludes it as a ⊳_G-cycle, with no bridge premise needed, since the metric is by construction an emergent quantity. Readings D and S exclude it as well. If the metric is moreover in superposition, (i) excludes it too. [A], [P] | green |
| C2(a) | K_dec has no partition-defined or emergent argument in its law, and no reading excludes it. [A] | green |
| C2(b) | The Einstein nonlinearity `g ⊳_D g` runs through no partition-defined object and no emergent relatum, so Readings E, S and G do not exclude it. Reading D without the route qualifier would, which is why (ii-L) carries the qualifier (§2.3). [A], [P] | green |
| C2(c) | GR:400 Reading 1 under §8.3: Readings E and G admit it, and so does (ii-L) (§4.2). The gap equation (GR:154; book/appendix-c-objections.md:259) is an implicit determination in which ħ grounds nothing upstream of the geometry. Readings E and G class it as non-circular, as the corpus does. [P] | green |
| C3 | `dρ_I/dR > 0`, `dρ_II/dR > 0` (§3.4). Z_0 fails and is not used as a witness. [A] | green |
| C4 | Z_I: an open interval of `Λ_c`. Z_II: an open half-line. [A] | green |
| C1′ (added at review) | GR:350: (i)–(iii) "fix the metric at the partition boundary" and not laboratory fields. **Reading E:** (ii) excludes only C1's configuration, which no completion in the corpus or unit 1 has. A semiclassical boundary metric, an implicit fixed point, is admitted by (ii). The boundary/laboratory contrast then rests on (i) alone, and (ii) adds nothing to (i) against the completions GR:350 and GR:340 contrast. **Readings D, S, G:** (ii) itself excludes a boundary metric whose law feeds back the emergent description through the partition, while a laboratory field does not define the partition, so no cycle arises. [P] | reported per reading |

C1–C4 are green on every reading, so the verdict is written. C1′ is not a pass/fail control of §1.4. It
records that Reading E leaves requirement (ii) idle against every completion its text is aimed at,
which weighs against Reading E as the intended reading of GR:346 (charity).

### 4.4 Verdict from the rule

- **Reading E** is valid and does not rule out the witness: §4.1 exhibits the entry point. This is
  §1.2 (B)(a).
- **Reading D** rules out the witness only through N5-D, which §2.2 refutes as a general principle.
  This is (B)(b).
- **The mixed reading** is invalid. This is (B)(a).
- **Reading S** rules out the witness only by assuming (ii-S), the exclusion being tested. This is
  (B)(b).
- **Reading G** is valid. Its premises are neither refuted by the witness (§2.2) nor equivalent to the
  exclusion being tested. It rules out the witness if and only if B_G holds (§4.1). B_G is not stated in
  GR:346, and §4.5 finds that it cannot be settled on paper. So Reading G meets neither (B)(a) nor
  (B)(b), and (A) is not established.
- The witness of §3 meets §1.3, (i), (iii) and (Adm1)–(Adm3).

**Outcome: (C).** The gap is Reading G's bridge premise: whether a term in the boundary metric's law
that is a function of the emergent class grounds the metric (excluded by N5-G) or only co-constrains it
(admitted). The decisive step on Readings E and D is N5 ("no entry point"). It holds for specifications
and fails for determination. On Reading G, N5-G is not in question; the open step is whether the
witness instantiates N4-G. [A] for the logic and the model; [P] for the transcription of GR:346, the
reading of its vocabulary, and Reading G.

### 4.5 The gap, and two attempts to close it

**Attempt 1: Reading G collapses into Reading E (B_G false) [P, conditional].**

- In OI the classical metric is grounded in the substratum: "spacetime emerges from
  `[(S, φ)]/𝒢_sub`" (GR:342), and the metric is substratum data (GR:340). The emergent class is grounded
  in the substratum and the partition (N3-G).
- Suppose the boundary metric's law is a coarse-grained consequence of the substratum dynamics `φ`.
  Then the realized metric and `ρ_Z` are both grounded in `(S, φ)`, and the law states a regularity that
  relates them. The term `ρ_Z`, a functional of classical data through `Π` (AW-route), co-constrains the
  metric. B_G fails and Reading G excludes nothing that Reading E admits.
- **Corpus text on the same side.** Substratum.md:389 states that QM and GR are "Both … emergent. Both
  depend on the trace-out and the partition. … The fundamental object is `(S, φ)`". Substratum.md:385
  calls the metric "a property of the classical dynamics of the partition boundary" and both
  descriptions "two different substructures of the same total object `(S, φ)`". On that account the
  gravitational description and the emergent description are co-projections of `(S, φ)`, which is the
  premise of Attempt 1 (node A9) [P].
- **Why this does not settle the gap.**
  - (a) It is conditional on the boundary law being derived from `φ`. That is G3, and G3 is open
    (GR:12; U1 §4).
  - (b) It rests on a view of laws in which a derived law's terms do not ground its solutions. The
    corpus states no view on this [L, recalled: the regularity and governing views of laws, §8].
  - (c) If it succeeded it would make (ii) idle against every completion GR:350 contrasts (C1′). That
    weighs against it as a reading of GR:342's "three independent requirements".

**Attempt 2: Reading G collapses into Reading S [P].** With B_G, Reading G excludes the members of the
λ-families with a convention-fixed term, as (ii-S) does. Its bearing on K_cpl^free is not examined here.
Reading G is not the route ban, however. Its exclusion follows from N3-G, N5-G and B_G, each with its
own motivation. The ban is not assumed. The collapse into S fails as an argument, and Reading G's force
reduces to B_G.

**The gap, narrowed.** B_G fails, conditionally, if the boundary metric's law is a coarse-grained
consequence of `φ` in which the realized metric is grounded in `(S, φ)` directly, and if a derived law's
terms do not ground its solutions. Whether OI's boundary law has that status is G3 (open). The corpus
states no view on the second condition. B_G can hold only for a boundary law that is not derived in
that way, or on a governing view of derived laws.

***

## 5. Pressure tests (§A.31)

Three branches are tested depth-first:

- (A), the outcome favourable to decoupling, in its strongest form, which is Reading G with B_G;
- the collapse of Reading G, which would give (B);
- the witness itself.

### 5.1 Branch (A), strongest form

- **A1. Is "derived" in GR:346 a determination term?** No. The vocabulary of GR:346 ("derivation would
  require", "entry point") and GR:342's gloss ("presupposes") are terms of specification, and GR:342's
  "logically prior" and "QM is emergent" and GR:346's "exists prior" are terms of ontological
  dependence. Verdict: the text supports Readings E and G, not Reading D. [P]
- **A2. Do (i) and (ii) together exclude the fixed point?** (i) requires a definite partition. At a
  unique fixed point the partition is definite, and with several fixed points each is definite.
  Verdict: no exclusion by (i). [P]
- **A3. Does (iii) close a loop through ħ?** ħ is defined through the partition (GR:78), but its value
  does not depend on `R` (GR:42, GR:78). The loop through ħ is degenerate in ⊳_D, and ħ depends on no
  state. ħ grounds nothing upstream of the geometry, so it closes no ⊳_G-cycle. Verdict: no
  exclusion. [P]
- **A4. "The metric evolves via Einstein's equations before the trace-out" (GR:340 s.1).** This is the
  ordering that GR:342 states as the conclusion of (i)–(iii), so it cannot serve as a premise (§1.1).
  P11 (GR:340 s.2) is the source posit, which excludes K_cpl^conv as unit 1's route R1. Verdict: no
  exclusion by GR:346's premises. [P]
- **A5. Observer-relativity.** The partition is observer-relative (GR:42: "Different observers have
  different horizon areas"). A metric law that reads one observer's `e_Z` is consistent only where the
  relevant observers' partitions agree. On de Sitter they agree, because the isometry group acts
  transitively [A]. Outside de Sitter this may bind K_cpl^conv. It is not GR:346's argument. Verdict:
  no exclusion of the witness; recorded as AW-obs (§7).
- **A6. Teleology.** GR:40 defines the partition by the event horizon, which depends on the whole
  future. Outside de Sitter the K_cpl^conv law would be a condition on whole histories, not an initial
  value problem. In exact de Sitter the event horizon of a geodesic observer is the static-patch
  horizon at `R` [A]. Not GR:346's argument. Verdict: no exclusion of the witness; recorded as AW-tel.
- **A7. Is the map/value distinction of §4.1 empty?** In ⊳_E it is not: the map `T` is defined on
  candidate data `κ_R`, and unit 1 states the field equation as a condition on `κ` (U1 §2). In ⊳_G the
  distinction does not answer the question (§4.1). Verdict: it stands for Reading E and is idle for
  Reading G. [P]
- **A8. Reading G with B_G.** Taken together, N3-G, N5-G and B_G exclude the witness. Applied with
  §8.3, they also reproduce the corpus's stated position: the absolute part is excluded and the
  configuration-differential part admitted (§4.2). Skepticism toward this favourable reading:
  - B_G is not stated anywhere in the corpus; the search of NOTES-U2A-r2 §2 finds no statement on
    whether terms of the gravitational law ground the metric.
  - Inside OI, B_G sits uneasily with GR:342's "the framework has no substance-level primitives". The
    metric's ground is the substratum, and a law with an emergent term grounds the metric in that term
    only if the law is more than a regularity among items grounded in `(S, φ)` (Attempt 1).
  - On the de Sitter class, Reading G with B_G excludes a completion that realizes the same worlds as
    K_dec (§6 item 3). Its exclusion of the absolute part is a claim about grounding without a
    world-level signature on that class.

  Verdict: Reading G with B_G is coherent and matches the corpus's position, but it is not
  established. [P]
- **A9. Does the corpus's own gravitational law pass through the partition?** The corpus obtains the
  Einstein equations "through Jacobson's relation" (GR:162), from horizon thermodynamics at the
  partition (SM:160–162). Substratum.md:389 states that GR, like QM, depends "on the trace-out and the
  partition".
  - A grounding principle that counted every partition-dependent ingredient of the law as grounding the
    metric would put the corpus's own route in a ⊳_G-cycle. B_G as stated avoids this only because it is
    restricted to terms that are functions of the emergent class.
  - That restriction is therefore load-bearing for Reading G. Substratum.md:385–389, which treats both
    descriptions as projections of `(S, φ)`, supports co-constraint rather than grounding (Attempt 1).
  - Whether "the metric exists prior to the partition" (GR:346 s.4), read in ⊳_G, agrees with
    Substratum.md:389 depends on whether "GR" there means the gravitational description or the metric.
    Substratum.md:385 does not fix this. It is recorded under AW-ground and not adjudicated.

  Verdict: weighs against B_G and does not settle it. [P]

**Branch (A) result.** (A) is not established. Reading G yields it only with B_G, which is open.

### 5.2 Branch (B), via the collapse of Reading G

- **G1.** Attempt 1 (§4.5) yields (B) only conditional on G3 and on a view of laws the corpus does not
  state. Verdict: not established.
- **G2.** Attempt 2 (§4.5) fails as an argument.

**Branch result.** (B) is not established.

### 5.3 The witness

- **B1. Is the witness in the K_cpl^conv class?** Z_II is unit 1's literal form `ħ e_Z/v`. Z_I is a
  convention `Z` in unit 1's sense, since unit 1 allows any map from `[r]` to a real origin (U1 §2).
  Both are constructed (§3.2). Membership rests on `ε`, `N_modes` and `n` being class data, and on `ω_IR`
  being computed from `N_modes` [P], [A]. Verdict: holds, conditional on M1.
- **B2. Does the de Sitter restriction weaken the result?** GR:346 is stated for any metric. A step that
  excluded every fixed point would exclude this one. The scope statement of §0 records the restriction.
  Verdict: holds, scoped.
- **B3. Does a classical uniform energy (GR:334) change anything?** It enters `Λ_c`, and Lemma FP holds
  for every `Λ_c`. Verdict: holds.
- **B4. Does existence depend on a tuned constant?** No. Existence holds on an open set of constants
  (C4). Tuning concerns where in that set a given `R₀` falls (§3.4), which is a different question.
  Verdict: holds.
- **B5. Is the loop's R-dependence a convention artifact?** In part. Under Z_I it comes from the added IR
  limit `q`. Under Z_II it comes from unit 1's fixed normalizing volume `v`. Under Z_0, GR:362's density
  estimate, it is absent. The corpus's own emergent vacuum energy (GR:378(i)) does depend on `H`, but
  that is the Reading 1 case (§3.2). Under Z_0, (ii-L) has nothing to exclude. Reading G concerns
  grounding and not covariation, so it is not affected (§6 item 2). Verdict: holds; the finding is
  U2A-F2.
- **B6. Could OI fix the convention?** K6 (`AntiunitaryInvariance.phase_families_shift'`,
  AntiunitaryInvariance.lean:285) leaves the origin free [K]. Any `Z` is an added normalization (U1 §2)
  [P]. Verdict: no OI premise selects Z_0 over Z_I or Z_II.
- **B7. Is a non-solution metric an admissible input?** The `κ_R` with `R ≠ R*` are classical data that
  the field equation does not select. Stating a law as a condition on classical data quantifies over
  them (A7). Verdict: holds.

**Result.** The witness survives, within the de Sitter class and assumption M1.

**§A.31 fixed point.** Not claimed. r2 adds a reading raised at review (Reading G) and one further node
(A9), so the passes recorded here are not empty.

***

## 6. Consequences for (DZ) and for Part 2 of unit 1

All items are scoped to the de Sitter class of §3 and to assumption M1.

1. **The source of Part 2's condition.** Unit 1 states Part 2 as "(DZ) for the convention-fixed offset
   follows conditional on GR:346's argument (ii-L)", and labels (ii-L) "GR:346 as argued" (U1 §0, B5,
   R0, O0, F8).
   - **On Readings E and D**, GR:346's argument does not establish (ii-L) (§2.4). On those readings
     (ii-L) is an added premise [P], and (DZ) for the convention-fixed offset receives no support from
     GR:346.
   - **On Reading G**, GR:346 excludes the convention-fixed coupling given B_G (§4.4), whether or not
     §8.3 is in force (§4.2).
   - GR:342's ontological commitment read as N5-G is a candidate independent motivation for (ii-L), and
     for the stronger (ii-G). Whether it applies is the gap of §4.4.
   - The other corpus supports for (DZ) are (ii-S) (GR:400 Reading 2, for the source), P11 (R1) and
     GR:575 (§8.3). Each is a posit or a reading the corpus does not adjudicate (GR:352, GR:400) [P].
2. **The reach of (ii-L) as an added premise.**
   - (ii-L) excludes a K_cpl^conv member only if `ρ_Z` varies with the configuration through the
     partition, and §8.3 is not in force (§4.2) [A], [P].
   - Under Z_0, GR:362's density estimate as written, `ρ_Z` is constant on the family under M1. No
     ⊳_D-loop exists, and (ii-L) is silent. K_cpl^conv[Z_0] has the field equations of K_dec with
     `Λ₀ = Λ^Z + 8πGα` [A].
   - The corpus's own emergent vacuum energy (GR:378(i), GR:388, GR:400) depends on `H` through the mode
     count. Its loop is the Reading 1 case, and its configuration dependence is of the kind that §4.2
     classes as relative. The R-dependence of the witness is the same kind of piece that Reading 1
     feeds back.
   - U1 B5's statement that the loop "closes through the gaps and the mode count" holds for Z_I, Z_II and
     the vacuum energy of GR:378(i). It does not hold for Z_0.
   - Reading G with B_G reaches Z_0, because grounding does not require covariation [P].
3. **World content [A].** Take `n > 0` and Z_I or Z_II, with `Λ_c` left free. By Lemma FP, `F` is a
   bijection from `I` onto `(F_∞, F_0)`. K_cpl^conv realizes exactly one de Sitter world for each
   `Λ_c` in that interval. K_dec realizes `g_R` exactly when `Λ₀ = 3R⁻²`. The two therefore realize the
   same set of de Sitter worlds with `R ∈ I`, the union over their constants. This extends to K_cpl^conv,
   on the de Sitter class, unit 1's result for K_cpl^free: world-equivalence to K_dec with Λ₀ left
   undetermined, which is the corpus's standing for Λ (GR:162, GR:334, GR:356).
4. **Where the remaining content of (DZ) lies [P].**
   - Write `ρ_Z(R) = ρ_Z(R₀) + Δρ_Z(R)`. At the level of de Sitter worlds, the first term is absorbed into
     the free constant.
   - Whether that split carries a fine-tuning is unit 1's statement (GR:352 (a); U1 §3.1 (b)). The
     world-equivalence of item 3 does not settle it, and this record does not change unit 1's
     statement.
   - The second term, a difference between configurations, can separate K_cpl^conv from K_dec at the
     level of worlds only outside the de Sitter class.
   - Whether the configuration-differential part of an emergent absolute level gravitates is the
     question GR:579 leaves open ("How the energy released in the electroweak and QCD transitions couples
     to gravity is not fixed by the relative/absolute distinction"). AUDIT item 2.9 notes that such
     between-configuration differences are relative by the rule's wording (U1 P30, AW-loop caveat).
5. **AW-loop (U1 §6) [P].**
   - On Reading E, the feedback stated at GR:358 and GR:374, and the self-consistent calculation of
     GR:388 and GR:400 Reading 1, are consistent with GR:346 without §8.3.
   - On Readings D and G, the reconciliation is conditional on §8.3, as unit 1 records (§4.2).
   - AW-loop's conditionality therefore holds on Readings D and G. The gap of §4.4 decides between
     Readings E and G.
6. **O0 (U1 §5).** O0's open item asks "whether (ii-L) holds against self-consistent fixed points".
   - On Readings E and D, on the de Sitter class, the answer is that GR:346's argument does not exclude
     them (§4.4).
   - On Reading G it is open, with the gap B_G.
   - The owner question whether to hold (ii-L), or (ii-G), as a premise (Q7) is unchanged in kind.
7. **Part 1 of unit 1** is unaffected. K_cpl^free survives (ii-W) and (ii-L).
8. **GR:352.** GR:352 calls decoupling "a coupling theorem and … what G3 names as open".
   - On Readings E and D, GR:346 does not settle (DZ), which is consistent with GR:352.
   - On Reading G, GR:346 settles (DZ) for the convention-fixed offset given B_G.
   - The optional note proposed in CONFIRM-r4 D-2 ("GR:346 as argued, in the same section, would settle
     (DZ) conditionally") holds with (ii-L) added, or on Reading G given B_G.

No manuscript change is proposed. This record makes no claim about the magnitude of Λ.

***

## 7. Findings

| ID | Finding | Class | Support |
|---|---|---|---|
| U2A-F1 | On Readings E and D, on the de Sitter class, GR:346's argument does not exclude a fixed point of K_cpl^conv. On Reading E the argument is valid and establishes (ii-W). On Reading D its step "no entry point" (N5) fails. The witness satisfies (i), (iii), (Adm1)–(Adm3) and (ii-W), and for `n > 0` it is unique for every completion constant in an open interval. | ELABORATING (addresses O0's open item on Readings E and D and the de Sitter class, §4.4) | [A] §2.4, §3.3–3.4, §4.1; [P] §2.1–2.2 |
| U2A-F2 | Under Z_0, GR:362's density estimate as written, `ρ_Z` is constant on the de Sitter family under M1. The loop does not close, and (ii-L) is silent. K_cpl^conv[Z_0] has K_dec's field equations with a shifted constant. The emergent vacuum energy of GR:378(i), GR:388 and GR:400 does depend on `H` through the mode count, and its loop is the Reading 1 case (§4.2). | ELABORATING (scope correction to U1 B5) | [A] §3.2, §3.4; [P] §6 item 2 |
| U2A-F3 | On the de Sitter class, with the constant left free and `n > 0`, K_cpl^conv[Z_I] and K_cpl^conv[Z_II] realize the same de Sitter worlds as K_dec with Λ₀ undetermined. Beyond the split of a constant, (DZ)'s content lies in the configuration-differential part of `ρ_Z`, whose coupling is GR:579's open question. | ELABORATING | [A] §6 item 3; [P] §6 item 4 |
| U2A-F4 | On Reading E, GR:346 is consistent with GR:358, GR:374, GR:388 and GR:400 Reading 1 without §8.3. On Readings D and G, the reconciliation is conditional on §8.3. | ELABORATING (refines AW-loop) | [P] §6 item 5 |
| U2A-F5 | "Post-partition" is a property of a quantity's route of specification, not of its value: through `Π`, every such quantity is a functional of classical data. A ban on post-partition data that is not a ban on routes, (ii-S), must name the ⊳_D-cycles it forbids, and without the route qualifier it would forbid the Einstein nonlinearity. | ELABORATING (assumption-watch AW-route) | [A] §2.2–2.3, C2(b) |
| U2A-F6 | GR:346 also reads in the order of existence or emergence (Reading G; GR:342 "logically prior … QM is emergent", GR:346 "exists prior"). On that reading the argument is valid and excludes the convention-fixed coupling if and only if the bridge premise B_G holds. B_G is open, and it is narrowed to the status of the boundary law (G3) and to a view of laws the corpus does not state. With §8.3, Reading G with B_G reproduces the corpus's position: absolute part excluded, relative part admitted. | ELABORATING (from REVIEW-U2A-r1 U-1; gap of §4.4) | [P] §2.2, §2.4, §4.1, §4.5; [A] §4.2 split |
| U2A-F7 | On Reading E, requirement (ii) adds nothing to (i) against every completion GR:350 and GR:340 contrast (C1′). | ELABORATING (charity marker on GR:342's "three independent requirements") | [P] §4.3 |

**Productivity test (§1.5).** U2A-F1 and U2A-F6 together are strictly stronger than the review's
statement. They replace "not a demonstrated no-fixed-point theorem" with a premise-level diagnosis, an
explicit fixed point and a named, narrowed gap. U2A-F2 constrains a claim of unit 1. The unit meets the
test.

**Assumption-watch markers.**

- **AW-route (U2A-F5).** An inference of the form "X is a quantity of the emergent description, hence not
  a source" needs either a ban on routes or a grounding premise (B_G), not only the emergent provenance
  of X. Sites to check: GR:358 ("The zero-point sum does not contribute to `H_tot`"), GR:575, GR:581. No
  change is proposed.
- **AW-ground (U2A-F6).** Wherever the corpus argues from "QM is emergent" to a constraint on a
  gravitational law, the step needs a statement of whether the law's terms ground the metric. Sites to
  check: GR:342, GR:346, GR:358, and Substratum.md:385–389 (QM and GR "Both depend on the trace-out and
  the partition"; node A9). No change is proposed.
- **AW-obs (node A5).** A coupling through one observer's partition is consistent only where the
  relevant observers' partitions agree. This is a candidate constraint on K_cpl^conv outside maximal
  symmetry, independent of GR:346, and it is not tested here.
- **AW-tel (node A6).** With GR:40's event-horizon partition, a K_cpl^conv law outside de Sitter is a
  condition on whole histories. It is not tested here.

***

## 8. Literature

All entries are recalled, and none was re-read. No verdict rests on any of them. Each is listed for the
structure it shares with the loop.

- C. Møller (1962) and L. Rosenfeld, Nucl. Phys. 40, 353 (1963): the semiclassical equation
  `G_μν = 8πG⟨T_μν⟩`, with the state defined on the metric it sources. A loop of the form
  "metric → quantum state → source → metric", treated as a self-consistency condition. GR:340 itself
  calls this equation "an emergent approximation".
- A. A. Starobinsky, Phys. Lett. B 91, 99 (1980): a de Sitter solution sustained by its own trace-anomaly
  stress tensor, `⟨T_μν⟩ ∝ H⁴ g_μν`. A self-consistent de Sitter fixed point with an `H⁴` source, the
  structure of Z_I's IR term. The anomaly term enters with the sign that admits a solution at zero bare
  constant; Z_I's IR term with `n > 0` has the opposite sign.
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge, 1982): `⟨T_μν⟩` in de
  Sitter for conformal fields in the de Sitter-invariant state.
- J. Z. Simon, Phys. Rev. D 43, 3308 (1991); L. Parker and J. Z. Simon, Phys. Rev. D 47, 1339 (1993):
  reduction of order, which removes spurious solutions of the higher-derivative semiclassical equations.
  The known problems of such fixed points are spurious solutions and state ambiguity, not circularity.
- É. É. Flanagan and R. M. Wald, Phys. Rev. D 54, 6233 (1996): solutions of the semiclassical equation
  and reduction of order.
- A. G. Cohen, D. B. Kaplan and A. E. Nelson, Phys. Rev. Lett. 82, 4971 (1999): a vacuum energy bounded
  by the size of the region, an IR limit tied to the geometry.
- S. D. H. Hsu, Phys. Lett. B 594, 13 (2004), and M. Li, Phys. Lett. B 603, 1 (2004): holographic dark
  energy, a vacuum density fixed by a horizon scale that the resulting expansion fixes in turn. With the
  Hubble horizon the equation of state does not accelerate (Hsu); with the future event horizon it does,
  at the cost of a teleological definition (Li). This is the structure recorded as AW-tel.
- A. Gupta and N. Belnap, *The Revision Theory of Truth* (MIT Press, 1993): circular definitions treated
  as meaningful, through revision sequences and fixed points. This is the logical counterpart of
  N5-E against N5-D.
- The Hartree–Fock self-consistent field (textbook): orbitals specified implicitly as fixed points of the
  operator they define. An implicit specification with an entry point, the space of trial orbitals.
- On grounding: J. Schaffer, "On what grounds what" (2009); G. Rosen, "Metaphysical dependence: grounding
  and reduction" (2010); K. Fine, "Guide to ground" (2012). These treat grounding as asymmetric and
  well-founded, as N5-G does. Dissent: E. Bliss (2014) and N. Thompson (2016) argue that symmetric or
  circular grounding is coherent. The question N5-G answers is therefore contested, which is one reason
  §4.4 does not rest on it.
- On laws: D. Lewis's regularity view, in which laws summarize the distribution of particular facts and
  do not ground them, against governing views (D. Armstrong, 1983; T. Maudlin, 2007). This is the
  disagreement that §4.5 Attempt 1 condition (b) turns on.

Corpus, read first-hand: GR:388 calls the Reading 1 route "the self-consistent emergent-QFT calculation";
GR:154 and book/appendix-c-objections.md:259 call the gap equation non-circular. [P]

**Bearing.** The recalled treatments of semiclassical and horizon-cutoff vacuum energy handle loops of
GR:346's shape as fixed-point conditions. As recalled, none of them reports an objection from circularity
of the kind GR:346 raises in the order of determination. Whether such loops are excluded in the order of
grounding is not a question those treatments address. No verdict rests on this.

***

## 9. Owner questions

- **QU1. Review routing.** Should r2 go to a delta check against REVIEW-U2A-r1, then to an exact-head
  review, as unit 1 did?
- **QU2. Q7 follow-up.** On Readings E and D, GR:346 does not supply (ii-L), and (ii-L) would not reach
  Z_0. On Reading G, GR:342's ontological commitment read as N5-G is a candidate independent motivation
  for (ii-L) and for the stronger (ii-G), conditional on B_G. Does Q7 stay open, with that candidate
  tested as a §A.29 premise, or is (ii-L) set aside?
- **QU3. Q8 follow-up.** When a manuscript unit is authorized, two scopings of GR:346, GR:342 ("forced")
  and book/ch07-gravity.md:183–187 are available:
  - (a) the order of explanation, under which (ii) adds nothing to (i) against the completions GR:350
    contrasts, and there is no AW-loop tension;
  - (b) the order of existence, under which (ii) excludes the convention-fixed coupling given a stated
    grounding premise B_G, and the AW-loop reconciliation through §8.3 is needed.

  Which, if either, should such a unit adopt? No change is proposed here.
- **QU4. Unit 1 text.** Unit 1 r5 labels (ii-L) "GR:346 as argued" (§0, B5, R0, O0, F8, Q7). Should a
  unit-1 revision relabel (ii-L) as an added premise on Readings E and D, note Reading G, and scope B5's
  loop statement (U2A-F2)? Or does this record carry the correction forward?
- **QU5. Next unit.** Candidates:
  - (a) B_G: whether, in OI, a term of the boundary metric's law that is a function of the emergent class
    grounds the metric. This reduces in part to the status of the boundary law under G3;
  - (b) whether OI's premises fix the zero-point convention, or make `e_Z` configuration-dependent at
    all (Z_0 against Z_I and Z_II);
  - (c) GR:579's question for the configuration-differential part of `ρ_Z`;
  - (d) AW-obs as a constraint on K_cpl^conv outside maximal symmetry;
  - (e) O1, as restated in unit 1;
  - (f) closing G3's offset thread after review.

***

## 10. Limits

- The derivations are by hand and are not machine-checked.
- The model is the exact de Sitter class, under assumption M1. No claim is made outside it.
- The transcription of GR:346 into N1–N5, the classification of its vocabulary, and Reading G with B_G
  are [P].
- The literature, including the literature on grounding and on laws, is recalled. No verdict rests on it.
- The decision rule was written before the analysis by the writer's account only (§1). No commit pins it
  separately.
- The §A.31 fixed point is not reached.
