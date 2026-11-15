# Review of GAUGE-A1-TRACE r1 (independent, non-author)

**Status.** Paper-only review. No repository file was edited, committed or pushed; no GitHub record was written; no Lean build, simulation or computation was run. Lean source was read for statement types only. All `file:line` references are to `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. Abbreviations follow the trace (Sub, SM, Struct, ch02). No status change and no recovery credit is proposed here.

**Verdict: REVISE.** One blocking, five required and nine recommended findings.

The row classifications mostly survive a transitive read: 24 of 26 summary rows are confirmed as classified, and 2 are confirmed with a disagreement about their stated basis (table at the end). The headline is stronger than its support in three ways:

- (B1) it rests the gauge carrier's independence from A1 on a kernel theorem that does not show it, and it does not mention corpus text that says the opposite;
- (R1) it treats Theorem 1a and Lemma 1c as "not consumed", but they are the only written construction of the observer-level objects on which §4.4 to §4.9 are stated;
- (R2) its continuum-exclusion section reads A4 in the restated form it proposes, not as A4 stands.

None of these makes A1 a premise of a written step of Stage 2 (a)–(e). Once they are fixed, the favourable finding is narrower, but it stands.

***

## Findings

### B1 (blocking). The kernel does not show that the gauge derivation's carrier is outside A1, and the corpus contradicts the trace's placement of the gauge group

**Location.** §0 Finding (last two sentences); summary row "2(d) stabilizer … N (complex carrier, outside A1 by kernel)"; §1.3 (d) Theorem 5 bullet; §3 skeptical pass (2).

**Evidence.**

- `cx3b_complex_not_A1` (`A6Instantiation.lean:512`) proves `¬ (linkSubstratum (Fin d → ZMod L) (Fin 6 → ℂ) …).A1`. Its proof injects `ℂ` into the configuration space through constant families. It is a cardinality fact about the *packaged link-coupled substratum* with complex values. That substratum sits on a **finite** torus of sites (`Fin d → ZMod L`), so it is infinite only because of `ℂ`.
- The module header says in terms: "Nothing here touches the Standard-Model gauge-group derivation: Theorems 5 and 7 of `SM`, H-link, H-cust, the `(3,2,1)` decomposition, the condensate stabilizer … are neither consumed nor judged". The sentence that the complex carrier "is the object on which the derivation of `SM.md:114` and Theorem 5 is conducted" is a docstring, not a kernel statement. The audit row AM-11 itself records "[IR] whether the gauge-sector stages are carried on it is not traced".
- The corpus places the gauge group in two incompatible places:
  - SM:312, SM:340 and Sub:288 place it at observer level.
  - SM:428 places it at the substratum: "The SM gauge group … lives at the substratum: … the commutant (stabilizer) … of the $O$-equivariant condensate $\Sigma$ … a literal algebraic structure on the lattice, existing before any trace-out is performed".
  - SM:511 likewise says: "At the bijection level, $V_K = V_3 \oplus V_2 \oplus V_1$ is correct and the commutant $\mathrm{U}(3) \times \mathrm{U}(2) \times \mathrm{U}(1)$ acts block-diagonally on it."

  The trace cites only the observer-level side.
- The inference is invalid as an A1 argument in any case. A step carried out on an infinite carrier can still depend on A1 through the link between that carrier and `S`: a state or measure defining `Σ = ⟨φφ†⟩`, or the projection that defines the observer-level operator (R1). Finiteness of the carrier is not the relevant question.

**Exact fix.**

1. Rest the (N) classification of Theorem 5 on its proof content. The proof (SM:340–342) uses only Theorem 7, Schur's lemma, the unitary stabilizer of a block-diagonal Σ, and the hypotheses H-link (m = 1), H-cust, O-equivariance and genericity of Σ. None of these mentions `|S|`, a counting measure or recurrence.
2. Replace "The kernel proves that this carrier is outside A1" with: "`cx3b_complex_not_A1` proves only that the packaged link-coupled carrier with `ℂ^6` values, on a finite torus, does not satisfy the interface's finiteness predicate; its module states that it does not consume or judge SM Theorems 5 and 7."
3. Delete skeptical pass (2), or restate it as the R1 question.
4. Record the layer tension (SM:312/:340 and Sub:288 against SM:428 and :511) as a corpus finding outside the A1 question.
5. Add to Theorem 5's conditions that `Σ = ⟨φφ†⟩` presupposes a condensate state. Theorem 5 takes the state's O-equivariance as a hypothesis, so no measure is consumed in the proof, but none is supplied on an infinite carrier either.

### R1 (required). The observer-level objects of §4.4 to §4.9 are written only for finite `S`; "not consumed" understates this

**Location.** §0 Finding; summary row "2(b) … L/T labels in the supporting Theorem 1a and Lemma 1c … not consumed"; §1.3 (b) last two bullets; §3 skeptical pass (4); the quotation of SM:222.

**Evidence.**

- §4.4's matrix update and Theorem 5's "observer-level kinetic structure" are "stated on the observer-level branch of Corollary 1b" (SM:312).
- Corollary 1b's hypothesis concerns "the observer-level Markov part $T$" (SM:270), which is the `A = PUP` of Theorem 1a ("Let $S$ be finite", SM:242), with the canonical projection `P_μ` of Lemma 1c ("the counting measure of [Main] Lemma 3, or a stated structured prior", SM:252). Lemma 1c (ii) is a finite-dimensional determinant/Schur identity.
- SM's only written construction of the object on which (b)'s normalization α = 1/d and steps (d)–(e) are stated is therefore a finite-`S` projection. The bridge φ → L_obs is open (SM:232).
- The trace quotes SM:222 for "$\Lambda=\mathbb Z^d$" but omits the next sentence: "The finite bijection is fundamental; a real/complex wave operator is an observer-level lift". SM uses `Z^d` for the lift's Fourier analysis. It does not state that the substratum steps hold on `Z^d`.

**Exact fix.**

1. Narrow the headline to: "No written *proof* step of Stage 2 (a)–(e) consumes total finiteness of `S`. The observer-level objects on which (b)'s normalization and (d)–(e) are stated are constructed in SM only for finite `S`: Theorem 1a's hypothesis 'S finite', and Lemma 1c's counting measure or stated prior with its finite-dimensional Schur identity. Their relation to φ is the open bridge (SM:232). On an infinite carrier these objects need either a normalized measure or state to define `P_μ` and `Σ`, or must be carried as posited observer-level data."
2. Add this as skeptical pass (5): "Through the definition of the observer-level objects?" Answer: yes, in the sense just stated. It is not a use in a proof step.
3. Change "SM §4 already uses `Z^d`" to "SM §4 represents the observer-level lift on `Z^d` while stating that the finite bijection is fundamental (SM:222)".
4. Change the summary row for 2(b) from "not consumed by the form selection" to "not consumed by the form lemma; they define the observer-level branch on which α = 1/d and §4.4–§4.9 are stated".

### R2 (required). The continuum-exclusion section misreads A4 and cites, as A1-independent, a definition that entails A1; it also leaves open whether the finite alphabet is posited

**Location.** §2, the table and the paragraph after it ("What A1 adds beyond them is the exclusion of *infinitely many* sites"); §3 condition 2 ("A4: translations of a rank-`d` lattice").

**Evidence.**

- As written, A4 says "the coupling graph is a finite periodic lattice, the quotient of a rank-$d$ lattice by a finite-index sublattice" (Sub:98). Ledger item (xiii) says each site carries values "in a finite abelian group" (Main:728). Together with site factorization (viii), A4 and (xiii) as they stand already give a finite `S`. So retiring A1 alone does not admit `Z^d` with finite alphabets. That needs A4 restated (unit U-A4; changemap r2 OQ-6). The trace's table reads A4 as "translations form a rank-`d` lattice", which is the restated form, and does not say so.
- SM §2.4's definition, "$S = S_1 \times \dots \times S_N$ a product of finite sets" with vertices $\{1,\dots,N\}$, is a finite product of finite sets. It entails A1, so it cannot be cited as an exclusion that survives A1's retirement.
- Owner check item 3 asks whether the finite local alphabet is established or posited. Main:728 (xiii): "a posit of the selected lattice model, not derived and not an axiom of OI". The trace says only "properties of the selected lattice model".
- The gauge derivation itself works with continuous (`ℂ`-valued) observer-level fields (SM:312, Theorem 5's U(6)). "Continuous field values" are therefore excluded only at the substratum.

**Exact fix.**

1. Rewrite the paragraph after the table:

   > As A4 stands (finite periodic lattice) with (viii) and (xiii), `S` is finite, so A1 adds nothing to the lattice model. A1 adds a constraint only to objects without site factorization, such as Stage 1's dilation. Once A4 is restated for an infinite lattice (U-A4; changemap r2 OQ-6), what excludes intrinsically continuum theories is A4's lattice clause (a structural assumption) together with (viii) and (xiii) (posits of the selected lattice model, not derived; Main:728). This exclusion is posited, not established.

2. Drop SM §2.4 from the "finite local alphabets" row, or cite it with the note that it entails A1.
3. Add: "the exclusion of continuous field values applies at the substratum; the gauge steps use `ℂ`-valued observer-level fields."
4. In §3 condition 2, write "A4 (as written: a finite periodic lattice; restated under U-A4: a rank-`d` lattice)".

### R3 (required). The (T) list does not account for all entry points that its own source audit lists, and its counts are inconsistent

**Location.** §0 ("five places"); §1.5 ("Its A1 consumers are exactly the (T) rows above").

**Evidence.**

- AM-11 lists A2's justification (Sub:94; AM-3) among A1's entry points into Theorem 23. Sub:94 justifies A2 by "every map on a finite set restricting to a bijection on that image". That is a finiteness use in the justification of a Stage 1 input. The trace neither lists it nor says why it is excluded.
- AM-11 also lists the §3.2 forward dilation (Sub:110; AM-5). This is (V) on the constructed realization, but the trace should say so.
- Separately, the headline counts five (T) uses. The table has further (T) rows: Lemma 1c, Theorem 24 (i), Corollary (iii) and Proposition 9.5.

**Exact fix.**

1. Add a row: "A2's justification (Sub:94): T, in the justification of an input, not in a derivation step; Stage 2 does not need it because bijectivity of the second-order form is automatic (`a2_every_substratum`, `SubstratumInterfaceAudit.lean:106`, no finiteness)."
2. Add a row "§3.2 forward dilation (Sub:110): V".
3. Replace "exactly the (T) rows" with an explicit list, and state that the headline's five are the (T) uses in Theorem 23's chain. Lemma 1c, Theorem 24 (i), Corollary (iii) and Prop. 9.5 are (T) uses outside that chain.

### R4 (required). The `Z^d` claims are readings, but parts of the bottom line state them without the [IR] marker

**Location.** §0 ("Both steps run cleanly on `Z^d`"); §3 Answer ("depends on **neither** total finiteness **nor** the finite-lattice model class, in any written step").

**Evidence.**

- §1.3 (a) marks "Runs on `Z^d` … yes [IR]".
- No step of Stage 2 is written on `Z^d` for the substratum (R1).
- As A4 stands, the d = 3 selection is "within A4's assumed periodic-lattice class" (Sub:157).
- The continuum step that d = 3 is conditional on is formulated on finite graph families `G_N`, `N → ∞` (SM §3.1, the contamination diagnostic and the mesoscopic Ollivier construction).

**Exact fix.**

1. Mark both sentences [IR].
2. Restate the §3 Answer as: "No written proof step uses total finiteness. The finite-lattice model class enters through A4's wording, through SM §3.1's finite-graph-family continuum step, and through the finite-`S` construction of the observer-level objects (R1). Validity of (a)–(e) on `Z^d` is a reading [IR], to be written under U-A4."

### R5 (required). Owner question 4.2 (b): "No new probability premise would be added" needs a qualification

**Location.** §4.2 (b) and its recommendation.

**Evidence.** On `Z^d`, the following are not defined without a normalized measure or state on the infinite carrier, unless they are carried as posits:

- the observer-level Markov part of Corollary 1b, which needs `P_μ` (Lemma 1c);
- the "observer-level kinetic structure";
- the condensate `Σ = ⟨φφ†⟩` of Theorem 5.

Lemma 1c permits "a stated structured prior", and that is a Q6-type input. The option is coherent only if it says which of the two routes it takes.

**Exact fix.** Amend (b) to: "… with H-cust's kinetic clause, Corollary 1b's observer-level branch and the condensate state carried as premises on the rank-`d` lattice (so no measure is introduced); Theorem 1a, Lemma 1c and Proposition 4b are cited as finite-model results." Also cross-reference changemap r2 OQ-6, which asks the overlapping question about A4's finite lattice.

### r1 (recommended). The mirror finding is correct but incomplete

**Location.** §1.7.

**Evidence.**

- ch02:106 matches FULL:740 word for word, and FULL:1224 matches ch04-methodology.md:116 word for word. The chapter source of FULL:1224 (§A.14 pair) is therefore ch04-methodology.md:116, which the trace does not name.
- In SM, detailed balance is the θ = id case of Theorem 19's conclusion (SM:641), as the trace says.
- Sub:167 gives the direction correctly, but it states the reciprocity without Theorem 19's counting-prior hypothesis, and so do all three mirrors. That hypothesis is exactly the A1-relevant input.

**Exact fix.** Add ch04-methodology.md:116. Add: "Sub:167 and the three mirrors also omit the counting hidden prior, which is the hypothesis through which A1 enters (row 2(f) Theorem 19)."

### r2 (recommended). The even-side statement can be sharpened from the corpus

**Location.** §1.3 (e); §0 ("[IR]").

**Evidence.**

- A4's own illustration admits "a periodic cubic lattice of side at least $3$" (Sub:98), which includes odd sides.
- SM:292 records "for even $L$, staggered null modes", the one place where the parity of the side appears in this context.
- Theorem 12's remark asserts "the cubic lattice is bipartite" (SM:539) without that qualification.

**Exact fix.** Replace "The corpus does not state this" with: "The corpus states the even-side condition only for the staggered null modes (SM:292). Theorem 12 (SM:535–539) asserts bipartiteness without it, and A4's illustration admits odd sides (Sub:98)."

### r3 (recommended). The Stage 1 → Stage 2 interface statement is too absolute

**Location.** §1.2.

**Evidence.**

- Sub:145: "Identification of this local lattice output with the Bell-violating Stage-1 completion additionally assumes H-Bell."
- SM §2.3: the triple is specified "together with the stated local factorization and coupling data".

The corpus therefore treats the factorization as added data and assumes the Bell-inclusive identification under H-Bell. What is unwritten is the identification for the M1-T temporal sector.

**Exact fix.** Replace "No step identifies the Stage 1 dilation with the Stage 2 lattice model" with: "The Bell-inclusive identification is assumed under H-Bell (Sub:145) and SM §2.3 adds the factorization as data, but no step identifies the M1-T temporal dilation with the Stage 2 lattice model."

### r4 (recommended). An argument from silence

**Location.** §1.5 ("Sub:104 already says … A1 is not in that list").

**Evidence.** Sub:104 lists A3–A6 because they are the assumptions whose removal it discusses. That A1 is absent from the list is not evidence that A1 is dispensable.

**Exact fix.** Delete the sentence, or present it as context only.

### r5 (recommended). Lemma 1c's (T) applies to one option

**Location.** §1.3 (b).

**Evidence.** Lemma 1c reads "the counting measure of [Main] Lemma 3, *or a stated structured prior*" (SM:252). The finite-dimensional identity of (ii) is the finite-`S` use whichever option is taken.

**Exact fix.** Write "(T) through the counting-measure option and through (ii)'s finite-dimensional identity".

### r6 (recommended). Report the kernel hypotheses and carriers exactly

**Location.** §1.3 (d), local-promotion bullet.

**Evidence.** `cx3a_complex_axioms` gives A4Exact only under the translation-invariance hypothesis `hM` on the link coupling. The docstring requires it to be "reported with it every time". `cx3a` and `as1_complex` are stated on the finite torus `Fin d → ZMod L`. The claim that sites are arbitrary is correct for `a6cov_all` and `as1_leap_covariant`: `{ι V : Type} [DecidableEq ι] [AddCommGroup V]`, with no `Fintype`.

**Exact fix.** Add "(A4Exact under `hM`)" and "on a finite torus of sites".

### r7 (recommended). Record that E7's imports were traced

**Location.** §1.3 (a), "None of them uses `|S|`".

**Evidence.**

- SM:196 imports the coefficient from GR §5, which is conditional on H-slope and the detailed-balance rate ratio. That ratio rests on GR:70's finite counting.
- The ratio itself does not need it. GR §7.2 uses `T_cl` from GR §3.1, which rests on Lemma 1 only (GR:98), and `ε` and `σ` cancel.
- E7 is redundant for the selection (SM:200).

**Exact fix.** Add one sentence: "E7's ratio uses GR §3.1's `T_cl` (Lemma 1) and is independent of `ε` and `σ`; SM:196's import of the GR §5 coefficient is not needed for the ratio, and E7 is redundant for d = 3 (SM:200)."

### r8 (recommended). Changemap vintage

**Location.** §4.1, §4.2; the sources list.

**Evidence.** CHANGEMAP-A1C r2 postdates the trace. It extends U-21 to Sub:205, :207, :212, :223 and :233, and adds OQ-6 (whether A4's finite periodic lattice stays as a model condition), which overlaps 4.2.

**Exact fix.**

1. In 4.1, consider the whole of U-21. Option (b) rewrites a bullet under the lead "The structural assumptions A1–A6 exclude", and (xiii) is not among A1–A6, so (b) also needs Sub:205's lead restated.
2. In 4.2, cross-reference OQ-6.

### r9 (recommended). Route (β) is a narrower replacement for Theorem 19

**Location.** §1.3 (f) (β); §4.4.

**Evidence.**

- Theorem 19 holds for any partition-preserving, T-invariant bijection under the counting prior.
- Route (β) gives reciprocity only for the native nearest-neighbour linear rule, per horizon, under the uniform product prior. It rests on EF-1 r7 N1.8, an unreviewed draft. N1.8 itself states that the uniform product prior "is a premise of this comparison … not a derived property".
- The step-1 hypothesis checks out: with `𝒯(p,c) = (c,p)`, `𝒯φ𝒯 = φ⁻¹` for the second-order map.

**Exact fix.** Label (β) "a narrower replacement (native rule, per horizon)". In 4.4, state that preferring (b) is a sequencing choice and that P6, if proved, would restore the general statement.

A further minor point, folded in here rather than counted: Proposition 9.5 also consumes "the Main paper's trace-out construction" (Struct:646), whose hidden prior is a declared normalized prior (Main:58). "Consumed only through (i)'s finite `C_H`" should read "through (i)'s uniform prior on a finite `C_H` and the declared hidden prior of the trace-out construction". With P11, the finiteness could be dropped, but P11 is a candidate that needs a proof and should be marked so.

***

## Answers to the review checklist

1. **(N) and (L) rows, traced transitively.**
   - Kernel types: `theorem_7` acts on `Fin 3 × Bool`, the link set, not `S`. `theorem_8` acts on corner labels. `theorem_19` has `[Fintype H]` and does not assume `V` finite. `a6cov_all` and `as1_leap_covariant` are polymorphic in `ι`. `uniform_family_consistent` needs `Fintype Q` (a finite alphabet) and allows any site type.
   - Prose proofs: §4.7.1.2 (read here in full) and Theorem 13 use only representation theory, the bipartite grading and a momentum-space Schur complement. They contain no finiteness of `S`. Theorem 7b contains none either.
   - The exceptions are B1 (the stated basis for Theorem 5) and R1 (definitional dependence of the observer-level branch).
   - The `Z^d` validity is claimed [IR], not proved (R4).
2. **(T) uses.** The five are correct. Each was re-read at source, including GR:58 and :70, which the trace read only through AM-22. The list misses A2's justification (Sub:94), and the counts are inconsistent (R3).
3. **Continuum exclusion.** Inaccurate as A4 stands. The exclusion is posited, not established (R2).
4. **Conditions regardless of A1.** The list is substantially complete and correctly sourced, and no premise is presented as derived; the Bravais type and d = 3 are correctly called selections. Additions:
   - the condensate state behind `Σ` (B1);
   - Corollary 1b's observer-level branch as a premise (R1);
   - H-blind for observers that are not component-complete (SM:334); it is implicit in item 7's "otherwise a premise" and should be named.

   Item 2 should give A4's two readings (R2).
5. **Mirror finding.** Correct; incomplete (r1).
6. **Owner questions.** All four are genuine and their options are correct.
   - 4.1: the recommendation is sound but should consider the whole of U-21 (r8). Its rationale for (b) already holds as A4 stands (R2).
   - 4.2: (b) is sound once qualified (R5).
   - 4.3: sound. Opening an Issue is a planning act that needs the owner (§A.45).
   - 4.4: acceptable as sequencing (r9).
7. **Overstatement.**
   - Favourable direction: B1, R1 and R4.
   - Unfavourable direction: none found.
   - No recovery credit or status change is claimed. Candidates are marked as candidates, except "With P11 the finiteness could be dropped" (folded into r9).

***

## Row-by-row confirmation of the summary table

| # | Row | Trace | Review | Reason |
|---|---|---|---|---|
| 1 | Stage 1 constructed triple, C1, C3, C4 | V | agree | Main:60: the §3.4 equivalence uses only Lemma 1; the hidden space is constructed |
| 2 | Stage 1 recurrence sentence (Sub:137) | T | agree | "on a fixed finite representative … recurrence cycle" |
| 3 | Stage 1 C2 necessity forms | T | agree | stated for the uniform-prior bijection marginal (AM-21; Main:728 ledger row "reference prior π_H") |
| 4 | Stage 1 → 2 interface | not written | agree, refine | Sub:145 (H-Bell) and SM §2.3 address part of it (r3) |
| 5 | 2(a) dimension | L | agree | finite quotient only through A4's wording and SM:202; E7 checked (r7); the continuum step uses finite graph families; `Z^d` [IR] (R4) |
| 6 | 2(b) form lemma, α = 1/d | N; supporting T/L "not consumed" | agree (form lemma); disagree ("not consumed") | Theorem 1a and Lemma 1c define the observer-level branch that α = 1/d and §4.4 rest on (R1) |
| 7 | 2(c) K = 6 | N | agree | Theorem 6 is conditional on H-link only |
| 8 | 2(d) Theorem 7 | N | agree | `theorem_7` acts on `Fin 3 × Bool`, the link set, not `S` |
| 9 | 2(d) Theorem 5 stabilizer | N (complex carrier, outside A1 by kernel) | agree on N; disagree on basis | basis is the proof content; the kernel does not show it; corpus tension SM:428, :511; condensate state is a premise (B1) |
| 10 | H-cust kinetic via Prop. 4b | T | agree | "take the selected counting measure" (SM:334); product of finite counting measures |
| 11 | SU reduction, hypercharges | N | agree | SM:575–599 read; group algebra and anomaly conditions only |
| 12 | Local promotion, A6 | N | agree | polymorphic kernel statements; `cx3a` A4Exact is under `hM` (r6) |
| 13 | Theorem 7b | N; converse a paper argument | agree | no "Bravais" match in `OIBridge/` or `verification/lean/` confirmed; directions correctly separated (§A.34) |
| 14 | 2(e) tastes, chirality | L / N | agree | even-side point correct (r2); §4.7.1.2 and Theorem 13 contain no finiteness of `S` |
| 15 | 2(f) Theorems 17, 18, 20, 21 | N | agree | read at SM:623–655 |
| 16 | 2(f) Theorem 19 | T | agree | "Dividing by $\lvert\mathcal C_H\rvert$"; `[Fintype H]`, `V` not finite |
| 17 | Stage 3 | T | agree | GR:58 "Restrict the finite total system … uniform counting"; GR:70 counts `\lvert M_i\rvert`, read directly |
| 18 | Lemma 23.0 | N for Stage-2 invariants; T for ħ | agree | Sub:191 proof cites E4–E7, A3–A6 and the nearest-neighbour premise for Stage 2 |
| 19 | Theorem 23 | union of rows | agree, with R3 | add A2's justification (Sub:94) and the §3.2 dilation (V) |
| 20 | Theorem 24 (i) | T as stated | agree | `ω_H = 𝟙/\lvert C_H\rvert` (Sub:253) |
| 21 | Theorem 24 (ii) | N | agree | conditional on the alphabet-size hypothesis |
| 22 | Theorem 24 (iii) | N; the finite factor is the statement's scope | agree | proof uses `Tr σ_A = 1` (Sub:266) |
| 23 | Theorem 24 (iv) | V and N | agree | finite visible laws; local point group |
| 24 | Corollary (i), (ii) | V | agree | E3 bounds `C_V × C_B`; H-BD |
| 25 | Corollary (iii) | T for recurrence clause | agree | Sub:268 (iii) |
| 26 | Prop. 9.5 | T inherited | agree, refine | also the declared prior of Main's trace-out construction (r9, folded) |

***

## What this review could not check

- EF-1 r7 Lemma PM and N1.8 were read in N1.8's statement only. The composition in route (β) was checked only at its step-1 hypothesis.
- P6, P7, P11 and P13 were not checked.
- Changemap rows were checked for existence and wording at r1 and r2, not reviewed.
- Lean was not built; statement types were read.
- The proofs of Main §2.3 and §3.4 were not read.
- SM §3.1's continuum step was scanned, not audited.
- SM Theorems 8b to 11 were read in statement and proof outline only.
- DEPENDENCY-AUDIT.md was not read.
