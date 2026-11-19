# REVIEW-U2A-r1: G3 unit 2(a) r1, GR:346 against self-consistent fixed points

**Verdict: REVISE.** One finding is blocking, seven are should-fix and three are nits.

What holds:

- The algebra is correct throughout: Lemma FP, both conventions, the negative-weight remark, the iteration slope, and the "same worlds" result on the de Sitter class.
- The explanation/determination split is a real and useful distinction.
- The refutation of N5 in the order of determination is sound.

What does not hold yet is the verdict (B). It is not established under the unit's own preregistered rule. The enumeration of readings omits the one the text most directly supports: priority of existence, or emergence. GR:346 says "the metric exists prior to the partition", and GR:342 says "Classical spacetime is logically prior to QM; QM is emergent". The record quotes only "presupposes" from GR:342.

On that reading, the "no entry point" step is the well-foundedness of the emergence relation. A mathematical fixed point does not refute it, and the implicit specification of §4.1 is an entry point for specification, not for emergence. Unless this reading is shown to collapse into E or S, the rule yields (C), or (A), not (B).

Separately, the record applies §8.3 in control C2(c) but not to the witness. The witness's R-dependence is exactly the configuration-differential part that AUDIT item 2.9 and GR:400 class as relative (U-2). U2A-F2 is narrower than stated, because GR:378(i) makes the corpus's own emergent vacuum energy depend on H (U-3).

**Target.** Branch `research/g3-offset-873-20261113` at `46a548fb19f3b5846ed62878c182c22e715d6735`, parent `e81e4fb2`. The commit adds only G3-UNIT2A-r1.md (613 lines) and NOTES-U2A-r1.md (116), in the unit-1 draft directory. "U2A:n" means a line of G3-UNIT2A-r1.md, "NU:n" a line of NOTES-U2A-r1.md, and "U1r5:n" a line of G3-UNIT1-r5.md. Corpus lines refer to `main` at `c3b5f37a`.

**Authority and context read:**

- #873 c.6863416405 (`amaybaum`, 2026-11-13T19:58:10Z): Q4, unit 2(a), paper-only, "must not assume the conclusion"; Q7, (ii-L) not adopted.
- PR #1275 review 5896999577 (posted by `amaybaum`, 2026-11-13T19:41:56Z, commit `e81e4fb2`): its "important limit" is that the exclusion of the convention-fixed coupling under (ii-L) "is not a demonstrated no-fixed-point theorem".

The unit stays inside the authorization: no premise is adopted, no manuscript is changed and no Lean is built.

**Checks at `46a548fb`.** All pass:

| Check | Result |
|---|---|
| `claims_check` | OK |
| `staleness_check` | OK, 13 matched |
| `voice_check` | OK |
| `artifact_placement_check` | OK |
| `legacy_records_check 46a548fb…` | 303 records intact |

None of them scans the drafts. I also scanned the two files by hand: no barred strings, no §A.32 or §A.33 phrases, and no capitals used for emphasis.

***

## Blocking

### U-1. The reading enumeration omits priority of existence, so (B) is not established by the rule

**Where.**

- §2.2 (U2A:160–182) and §2.4 (U2A:194–206);
- §4.4 (U2A:377–389), where the rule is applied;
- A1 (U2A:400–403);
- §0 (U2A:34–41);
- the dependent consequences 1, 5, 6 and 8 (U2A:464–508), U2A-F1, U2A-F4, QU2 and QU3.

**Evidence.**

- The text supports a third order. GR:346 s.4: "The circle breaks only if the metric *exists* prior to the partition." GR:342 opens with "**Ontological commitment.** Classical spacetime is logically prior to QM; QM is emergent". Only after that does it add the gloss "a claim about the direction of the derivation chain — that the trace-out producing QM presupposes the classical geometric structure". The record quotes "presupposes" (U2A:178–179) and does not quote "logically prior" or "QM is emergent". "Exists prior" and "emergent" are the vocabulary of ontological dependence, not of specification (⊳_E) or of value covariation (⊳_D).
- The reading the dichotomy omits is **Reading G**, emergence or grounding. Read N4 as "the realized metric is what it is partly in virtue of a property of the realized emergent description". Read N5 as the well-foundedness, or asymmetry, of "emerges from" / "is grounded in".
  - §2.2's refutation of N5-D does not touch N5-G. That refutation rests on the existence of solutions of joint equations, and a solution's existence says nothing about which relatum is grounded in which.
  - §4.1's acyclic specification graph is also not an entry point in the G sense. At S6 the realized radius R* is fixed by F(R*) = Λ_c, which reads ρ_Z(R*). That is a property of T(Π(g*)), the realized class. So the realized metric is partly what it is because a property of the realized emergent description is what it is, and that description emerges from the realized partition and metric (GR:342, GR:344). That is a cycle in G.
  - The map/value distinction of §4.1 and A7 answers ⊳_E. It does not answer G.
- Reading G passes the unit's controls:
  - **C1:** G excludes C1's configuration.
  - **C2(a):** K_dec has no emergent argument.
  - **C2(b):** the Einstein nonlinearity involves no emergent relatum, so it is not a grounding cycle.
  - **C2(c):** under §8.3, Reading 1's piece is a classical microstate difference (GR:573, GR:400), so it is not emergent in the G sense. The gap equation is also fine: ħ is determined by the geometry and does not ground the metric (GR:154, appendix-c:259).
- Reading G is neither refuted by the witness nor identical to (ii-L). It is a general asymmetry with its own motivation in GR:342. (ii-L) follows from it for this loop, but G has other content.
- Under §1.2 this is the (A) clause: "Some reading of the premise set yields a valid argument whose premises are neither refuted by an explicit model nor equivalent to the exclusion being tested". Alternatively it is (C): "a reading whose premise cannot be settled on paper". The open premise is whether a term of the metric's law that is a function of the emergent class grounds the metric, or only co-constrains it. In neither case is it (B).
- **The charity check points the same way.** On Reading E, requirement (ii) excludes only a metric explicitly defined as a function of its own realized description (C1). No completion in the corpus or in unit 1 has that form. Yet GR:342 presents (ii) as one of "three independent requirements" that force the ordering, and GR:350 contrasts the boundary metric, which (i)–(iii) "fix", with laboratory fields, which they do not. On Reading E that contrast rests on (i) alone. A formalization that makes (ii) idle against every completion its text is aimed at needs a stated reason for preferring it. Here the reading is selected on the basis of a partial quotation of GR:342.
- **Consequences that go too far.** "This unit found no independent motivation for (ii-L) in GR:346" (U2A:502–503) is premature, because Reading G is a candidate independent motivation, which is what Q7 asks about. Consequences 1, 5 and 8, U2A-F1 ("GR:346 … establishes (ii-W)") and U2A-F4 hold only on Reading E.

**Fix.**

1. In §2.2, add a third order:

   > "**Order of existence or emergence (⊳_G).** `X ⊳_G Y` if `Y` is what it is partly in virtue of `X` (GR:342: 'logically prior … QM is emergent'; GR:346 s.4: 'exists prior'). N5-G: ⊳_G is well-founded."

   Quote GR:342's first sentence in full where "presupposes" is quoted.
2. In §2.4, add Reading G, give its validity, and apply it to the witness. Do this in §4.1: at S6, R* is fixed through ρ_Z(R*), which is a property of the realized class.
3. Run C1–C4 on Reading G (§4.3).
4. Re-apply the rule (§4.4). The outcome is (B) only if Reading G is shown to collapse into Reading E or Reading S by an argument. For example, argue that a term in a law never grounds its solution, and reconcile that with GR:342's "QM is emergent". Otherwise the outcome is (C), with the gap named:

   > "whether a term in the boundary metric's law that is a function of the emergent class grounds the metric (excluded by N5-G) or only co-constrains it (admitted)"
5. Scope consequences 1, 5 and 8, U2A-F1 and U2A-F4 to Reading E, and replace U2A:502–503 with:

   > "GR:342's ontological commitment ('logically prior … QM is emergent') read as N5-G is a candidate independent motivation for (ii-L); whether it applies is the gap of §4.4"

   Carry this into QU2. In QU3, the proposal to scope GR:346 "to the order of explanation" should be offered only together with the alternative of scoping it to Reading G.

***

## Should-fix

### U-2. §8.3 is applied in control C2(c) but not to the witness

**Where.** C2(c) at U2A:371; §4.2 at U2A:359–362 ("The model therefore violates (ii-L) … by construction"); §1.1 at U2A:95 (GR:575 excluded); consequence 2 at U2A:473–478.

**Evidence.** C2(c) admits GR:400 Reading 1 under (ii-L) "only under that identification", meaning §8.3. The loop-carrying part of the witness, however, is ρ_Z(R) − ρ_Z(R₀). Under Z_I that is −β(R⁻⁴ − R₀⁻⁴), an H⁴ term that differs between configurations. The record's own consequence 4 says so (U2A:485–488). By the rule's wording, AUDIT item 2.9 (AUDIT.md:371–378) classes between-configuration differences as relative. GR:400 classes the epoch-differential curvature response as "relative … in the sense of §8.3". So if §8.3 is applied uniformly, the witness's loop runs through a classical microstate difference, and (ii-L) does not exclude it. "Violates (ii-L) by construction" holds only when §8.3 is not applied, and in that case (ii-L) also excludes Reading 1.

**Fix.** State once whether §8.3 is in force for the whole test, and apply that choice to both C2(c) and the witness.

- With §8.3 in force, §4.2 becomes "violates (ii-L) only if the configuration-differential part of `ρ_Z` is not a classical microstate difference". Add that, under §8.3, (ii-L) excludes neither part of K_cpl^conv: the constant part has no loop (Z_0), and the differential part is relative.
- Without §8.3, C2(c) records that (ii-L) excludes Reading 1. That is a fact about (ii-L), not a failure of the verdict's reading.

Either way, consequence 2 should add that the R-dependence of the witness is the same kind of piece that Reading 1 feeds back.

### U-3. U2A-F2's scope, and its NEW class

**Where.** U2A-F2 at U2A:519; consequence 2 at U2A:473–478; §0 item 2 at U2A:62–65; B5 at U2A:443–446.

**Evidence.**

- GR:378(i) states: "the boundary entropy `S_dS = σA/ε²` depends on `H` via `A = 4πc²/H²`, so the emergent vacuum energy inherits an `H`-dependence". GR:374, GR:388 and GR:400 then evaluate that H-dependence. So the emergent vacuum energy the corpus actually uses does vary across the de Sitter family through the mode count, and the loop does close in the corpus's own construction, as Reading 1's piece.
- What is constant under M1 is GR:362's density estimate, which GR:362 calls "a dimensional identity". The record cites GR:378 only for the area formula (U2A:223).
- That a constant vacuum density is a shift of Λ, and closes no loop, is the standard point unit 1 records ([L, recalled: Weinberg 1989], U1 §7: "cannot be distinguished from a bare Λ"). Its use here is a correct scope correction to U1 B5's sentence "the loop closes through the gaps and the mode count". It is not a structural blind spot.

**Fix.** Restate U2A-F2 as:

> "Under Z_0, GR:362's density estimate as written, `ρ_Z` is constant on the de Sitter family under M1. The loop does not close, and (ii-L) is silent; K_cpl^conv[Z_0] has K_dec's field equations with a shifted constant. The emergent vacuum energy of GR:378(i), GR:388 and GR:400 does depend on `H` through the mode count. Its loop is the Reading 1 case (U-2)."

Reclassify it as **ELABORATING (scope correction to U1 B5)**, and apply the same narrowing to §0 item 2 and consequence 2 ("the corpus's own mode-sum density" → "GR:362's density estimate").

### U-4. Consequence 4's fine-tuning sentence contradicts unit 1 r5 without a new result

**Where.** U2A:492–494 ("A fine-tuning reading of the constant part (GR:352 (a)) needs a value for `Λ^Z` fixed independently of `ρ_Z`, and no OI premise supplies one"). Related: U2A:476–477 ("(DZ) distinguishes … only by how one constant is split").

**Evidence.**

- U1r5:357–359, the reviewed text, places the fine-tuning reading on K_cpl^conv because "`ρ_Z(r₀)` is fixed by the emergent class and not read back from the field equation".
- GR:352(a) states that treating the zero-point sum as a source produces "the 10^122 discrepancy requiring cancellation or fine-tuning".
- The new sentence makes fine-tuning depend on an independently fixed Λ^Z. That is a naturalness premise, not a consequence of Lemma FP or of the world-equivalence. World-equivalence, which is correct ([A], U2A:479–484), concerns sets of worlds. Fine-tuning concerns how a free constant is related to a large fixed term. One does not settle the other. A valence change needs a new result (§A.22).

**Fix.**

- Replace U2A:492–494 with:

  > "Whether the split of that constant carries a fine-tuning (GR:352 (a); U1 §3.1 (b)) is not settled by the world-equivalence above; this record does not change unit 1's statement."
- Change "only by how one constant is split" to "at the level of de Sitter worlds, only by how one constant is split; whether that split carries a fine-tuning is U1 §3.1 (b)".

### U-5. C1 is near-vacuous. Add a corpus-anchored positive control.

**Where.** C1 at U2A:124–126 and U2A:368.

**Evidence.** C1's configuration, a metric with no classical family, specified only through its own realized description, is not a completion anyone proposes. C1 therefore shows only that Reading E is not literally empty. The control that would test fidelity is a configuration the corpus says (i)–(iii) exclude: GR:350 says they "fix the metric at the partition boundary", in contrast to laboratory fields. GR:340 contrasts the geometry-first ordering with "the semiclassical equation `G_μν = 8πG⟨T̂_μν⟩`" as "an emergent approximation". On Reading E, a semiclassical boundary metric, being an implicit fixed point, is admitted by (ii). So (i)–(iii) distinguish the boundary from the laboratory only through (i).

**Fix.** Add a control C1′:

> "the formalization must account for GR:350's statement that (i)–(iii) fix the boundary metric and not laboratory fields"

Report the result for each reading. If Reading E accounts for it only through (i), state that (ii) is idle on Reading E, and weigh this in the reading selection (U-1).

### U-6. "Preregistered" cannot be verified

**Where.** U2A:79 ("This section was written before §2–§6"); NU:55–57.

**Evidence.**

- The rule and the analysis land in one commit (`46a548fb`). No commit pins §1 alone.
- NU:55–57 says the rule "was not drafted blind to the likely direction". It also says the sources had been read first.

§A.29 asks that the decision rule be preregistered. The writer's account is credible, but the repository cannot show it.

**Fix.**

- Replace U2A:79 with:

  > "This section fixes the rule and the controls. By the writer's account it was written before §2–§6, after the sources were read (NOTES §3); no separate commit pins it."
- Keep the word "preregistered" only with that qualifier.

### U-7. §0 overstates where Z_I and Z_II come from, and omits M1 from the scope

**Where.** U2A:43–44 ("two zero-point conventions taken from the corpus's mode sum (GR:362, GR:332) and from unit 1's definition of `ρ_Z`"); the §0 scope at U2A:53–55.

**Evidence.**

- Z_I adds an IR limit at q/R (U2A:232, :242–243) that GR:362 does not contain. q is a free convention constant.
- Z_II takes its R³ growth from unit 1's fixed normalizing volume v (U2A:244–247, B5 at U2A:443–446).
- Both are legitimate members of unit 1's class, since any map Z from [r] qualifies (U1 §2). The witness is about the logical reach of GR:346, so a constructed convention is acceptable. The surrogate rule is met as long as the conventions are described as constructed.
- M1 (U2A:230–231) is stated in §3.1, B1 and §10, but it is missing from §0's scope.

**Fix.**

- At U2A:43–44, write: "two conventions in unit 1's class, constructed from GR:362's mode sum with an added IR limit at the horizon scale (Z_I) and from unit 1's normalization `ρ = ħe/v` (Z_II); neither is the corpus's own convention".
- Add "and assumption M1 (`n`, `ε` independent of `R`)" to the scope sentence at U2A:53.

### U-8. The consequences are stated more strongly than the record's own scope

**Where.** U2A-F1, class "answers O0's open item" (U2A:518); consequence 6 at U2A:500–501.

**Evidence.** After U-1 the answer holds for Reading E on the de Sitter class only.

**Fix.** Write "addresses O0's open item on Reading E and the de Sitter class (§4.4)".

***

## Nits

### U-9. A4 conflates GR:340's ordering sentence with P11

**Where.** §1.1 at U2A:94; A4 at U2A:410–412.

**Evidence.**

- GR:340 s.1, "the metric evolves via Einstein's equations *before* the trace-out", is the ordering, and GR:342 says (i)–(iii) force it.
- P11 is s.2, "The stress-energy sourcing gravity is the classical stress-energy …" (U1 P11).

Excluding s.1 as a conclusion is correct. Excluding it as P11 is not.

**Fix.**

- At U2A:94: "GR:340 s.1 (the ordering; the conclusion of (i)–(iii), GR:342) and s.2 (P11, a posit: GR:352)".
- In A4: "This is the ordering GR:342 states as the conclusion of (i)–(iii), so it cannot serve as a premise; P11 (s.2) is the source posit."

### U-10. NU:17 is inaccurate at the head

**Where.** NU:17 ("outside the repository. Nothing was committed, pushed or posted").

**Evidence.** Both files are committed at `46a548fb`, by the coordinator.

**Fix.** Write: "Written in the working area by the writer; committed to the branch at `46a548fb` by the coordinator."

### U-11. The literature "Bearing" sentence is a negative claim over recalled sources

**Where.** U2A:576–577 ("None of them reports an objection from circularity of the kind GR:346 raises").

**Fix.** Write: "As recalled, none of them …"

***

## Checked and correct

**Lemma FP (U2A:264–273) [A].** 3R⁻² is strictly decreasing and −8πGρ_Z is non-increasing, so F is strictly decreasing and continuous on the open interval I. Its image is (F_∞, F_0). (a), (b) and (c) follow, and (c) reproduces U1's Λ^Z_1.

**Z_I [A].** The zero-point density between frequencies a and b is (b⁴ − a⁴)/(16π²).

- ω_IR = q(4π/(ε²N))^{1/2} = q/R, with N = 4πR²/ε².
- ρ_I = α − βR⁻⁴.
- F_0 = 3/(q²ε²), since β/(qε)⁴ = α.
- The quadratic bx² + 3x − L = 0 has positive root 2L/(3 + √(9+4bL)) exactly when L > 0.
- Existence holds if and only if −8πGα < Λ_c < 3/(q²ε²).

**Z_II [A].**

- ρ_II = (nħ/(12πv))(R³ε⁻⁴ − q⁴R⁻¹) and K = 2nGħ/(3v).
- F_0 = 3/(q²ε²), since the bracket vanishes at R = qε.
- The quintic Kε⁻⁴R⁵ + Λ_cR² − Kq⁴R − 3 has one sign change for every sign of Λ_c, so Descartes' rule gives exactly one positive root.

**Negative weight (U2A:304–308).** The equation |b|x² − 3x + L = 0 has two positive roots for 0 < L < 9/(4|b|), one for L ≤ 0, and none above 9/(4|b|).

**Iteration (U2A:310–313).** The slope is −2bx/3. With b = Gnħq⁴/(2π) and ε² = 4Gσħ, the condition x* < 3/(2b) is R*² > nq⁴ε²/(12πσ).

**C3 and C4.** dρ_I/dR = 4βR⁻⁵ > 0. dρ_II/dR > 0. The constants with a fixed point form an open interval or half-line.

**(i), (iii) and Adm1–Adm3 on the de Sitter family.**

- ρ_Z(R*) is constant on M, so the source is conserved.
- The null-flux term vanishes.
- ħ is independent of R: GR:42 "depends only on local geometric quantities … not … horizon area", and GR:78 "κ cancels".
- Naturality holds within de Sitter because the isometry group acts transitively. Outside de Sitter it is observer-dependent, which is AW-obs, correctly recorded.

**"Same worlds as K_dec" (consequence 3, U2A:479–484) [A].** Correct. F is a bijection from I onto (F_∞, F_0), and K_dec realizes g_R exactly when Λ₀ = 3R⁻². The union over constants agrees on R ∈ I. The limits are U-4's.

**The formalization N1–N5 and the E/D split.** These are faithful as far as they go. N1–N3 transcribe GR:40, GR:344 and GR:346. N5-E and N5-D are correctly stated. C2(b) correctly explains why (ii-L) needs its route qualifier. The gap equation is the corpus's own standard of non-circularity (GR:154: "The non-circularity is structural"; appendix-c:259). The defect is omission (U-1), not misstatement.

**The decision rule.** Excluding GR:342's "forced" and book/ch07-gravity.md:187 is legitimate: each states the conclusion of (i)–(iii), and using either as a premise would assume what is tested. It does not strip GR:346 of content. The content GR:346 loses on Reading E comes from the omission in U-1, not from these exclusions. C2 consists of real negative controls. C1 is weak (U-5).

**Pressure tests.**

- A1–A7 and B1–B7 are adequate apart from A1, which needs Reading G (U-1).
- B5 rightly flags that the loop's R-dependence is a convention artifact.
- A5 and A6 (observer-relativity, teleology) are good catches and correctly kept out of the verdict.
- The literature (§8) is marked recalled, and no verdict rests on it. The citations match the standard references, as far as I recall them.

**Citations checked on `main`.** All resolve to the stated content: GR:40, :42, :78, :154, :332, :340–352, :358, :362, :364 (N_modes = S_dS/σ), :374, :378, :388, :400, :569–581; appendix-c:259; AntiunitaryInvariance.lean:285.

**Register and labels.** Clean. [A] is used for algebra and logic, [P] for transcriptions and readings, and [L, recalled] for literature. The labels are correct, apart from §4.2's [A], which needs U-2's condition.

***

## Disposition

REVISE.

- **U-1 (blocking).** The outcome needs Reading G and a re-application of the preregistered rule. The likely result is (C), with the named gap, unless Reading G is argued to collapse into Reading E or Reading S.
- **U-2 to U-8 (should-fix).** U-2 makes the use of §8.3 consistent. U-3 narrows U2A-F2 and reclassifies it as ELABORATING. U-4 withdraws the unsupported fine-tuning sentence. U-5 adds C1′. U-6 qualifies "preregistered". U-7 fixes the description of the conventions and adds M1 to §0. U-8 scopes the consequences.
- **U-9 to U-11 (nits).**

No manuscript change is proposed.
