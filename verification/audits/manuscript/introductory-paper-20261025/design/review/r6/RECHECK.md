# Re-check: Introduction design r6 (one idea, two consequences)

- **Object.** #918 at `f256c5f4` (`S/pintro/repo`): `design/{OUTLINE,CLAIMS,CHANGES,DEPENDENCIES}-r6.md`, plus the
  committed `review/r5/` and `applications-audit/CORRECTIONS.md`.
- **Byte checks.** The committed `review/r5/REVIEW.md` and `chk/*.py` are byte-identical to my originals.
  `SHA256SUMS` verifies clean.
- **Inputs.**
  - Baseline r4 (sha256 `5f9fdcc5…`);
  - `main` `687e885b`;
  - R11 `REVIEW.md`, `DIFF-REVIEW.md` and `DIFF-RECHECK.md`.
- **Read-only.** No repository file was changed. My budget estimate is `S/paper/design-r6-review/chk/budget.py`,
  run with `python3 -I`.

## Verdict: ACCEPT WITH CHANGES

The rescoping is faithfully executed:
- one thesis and two applications;
- every removed topic is gone from the text, with no residual dependence;
- both applications are explicitly not demonstrated resolutions (N-INT1, N-CC8, N-BH3, the abstract and the
  conclusion);
- Theorems 1–4 keep their statements, status words and witnesses.

Six required changes follow.
- **C1** corrects an overstatement that my own r5 R1 introduced and r6 copied verbatim: "only when" the shell is the
  full product space. DIFF-RECHECK N1 settles that the evidence supports "holds on the full product space, fails in
  general on a proper shell".
- **C2–C5** restore hypotheses lost in compression or in the results register:
  - C2: N-BH1 loses the bijectivity condition of the $P_{\rm succ}$ bound;
  - C3: N-DI1 promotes the fixed-basis statistics to "the quantum description";
  - C4: the process-dilation row omits "rational";
  - C5: the stochastic-inverse row omits "finite square".
- **C6** corrects the page arithmetic. The result, about 11.2 pp, is still inside 10–12.

## 1. r5-review items

| Item | r6 | Check |
|---|---|---|
| R1 | N-BH2, verbatim | Applied, but the text inherits my "only when" overstatement → **C1** |
| R2 (+ "in a pure joint state") | N-BH3 | Applied. The departure is correct: DIFF-RECHECK §2 confirms the pure-joint-state clause is A.8's own assumption. The "only for" clause → **C1** |
| R3 | §5 item 1 (r4:172 s1–3, s5; s4 to limitation 4) | Applied |
| R5 (minus the Page-time clause) | §6.2 item 4 | Applied. The drop is correct, since the content is removed. The shell clause → **C1** |
| R6, R7, R8, R9 | §4 N-CC4, N-CC3, N-CC1, N-CC0/N-CC6 | Applied verbatim (checked word for word) |
| R12 | §6.2 item 8 | Applied verbatim |
| R14 (folded) | N-BH3, N-CC2/N-CC8, N-DT1 | Applied in substance. N-BH3 carries the Page curve's dependence on the covariant field equations. CHANGES says it is also in N-DT1, but N-DT1's black-hole clause omits it (nit 3) |
| R16 | Abstract | Applied (sentence 5 with its status parenthesis; sentence 4 reduced) |
| R18 | N-BH1 sources; DEPENDENCIES §C, §R | Applied. One residual slip: DEPENDENCIES §R says "AUDIT cites both at SM:851". AUDIT §6.1 cites SM:849 for "hypothesis, not a derivation" (nit 6) |
| R19 | DEPENDENCIES §A, §R | Applied. ch19:38 is no longer used as an anchor |
| Nit 8 (Weinberg held) | — | Acceptable. N-CC0 then carries an uncited standard number, so make reading Weinberg a landing gate (O2) |
| **Moot: R4, R10, R11, R13, R17; nits 1, 5, 6** | — | **Truly moot.** No Page time, β, numerical agreement, JUNO, Cabibbo, arrow, PE-01 or horizon-entropy sentence survives in OUTLINE-r6. N-CC6 uses "the de Sitter entropy" only as a named standard quantity and makes no 1/4 claim. N-BH5's "QES agreement not established" is true without the Page-time qualifier (ch07:147) |

## 2. Results register

Each statement was checked against Main or GR at `687e885b` and against r4.

**Exact, with status and witnesses correct:** T1 (Main:526, :99 witnesses), T2 (Main:582), C, CAP (Main:484, :492),
PIN (Main:166), T3, RB (Main:137, :139), CP (Main:326), HAD, BORN, T4, IND, REL, BR, FC and BELL.
- C keeps a source for each direction, as §A.34 requires: ⇒ T2(a) in each realization; ⇐ T2(a) with `S_imp_D`.
- Main:99 confirms that the conditional-mutual-information vanishing criterion "is not formalized", so S-4's "not
  machine-checked" is accurate.
- BR displays no equivalence and uses `rooted_eq_iff_slice_eq` forward only, which is correct.

Two rows omit a hypothesis of the cited theorem. Both are inherited from r4, but r6's register claims the exact
statement.

- **PD (C4).** Main:496, Theorem (finite-horizon process dilation): "with **rational** multi-time law on a finite
  accessible horizon K", with |C_V| ≥ 2.
  - The independent-prior realization needs rational probabilities: a finite uniform hidden prior can produce only
    rational laws.
  - The register row is also mislabelled "r4:66 s2". It is r4:66's fourth sentence.
- **SI (C5).** Main:133: "If a **finite square** stochastic matrix has a stochastic left or right inverse …". The Lean
  lemma is stated for `Matrix n n ℝ`.
  - "Square" is load-bearing: $A=(1\;0)$ and $B=(1\;1)^{\!\top}$ are stochastic with $AB=I_1$, and $A$ is not a
    permutation matrix.
  - The register's "(= Main:133)" is therefore not exact.

**Sketch removal.** No status distinction is lost:
- r4:92's two status sentences, r4:114's routed-versus-history-level sentence and the S-4 criteria are kept;
- the prior-independence status is kept ("proved on paper, with exact probes").

One antecedent dangles. With r4:112 s1–2 removed, "Doukas states *the same argument* concurrently" has no argument
in view (nit 2).

## 3. The applications

- **§4.**
  - "Not a demonstrated resolution" is explicit: N-CC2, N-CC4 ("not computed"), N-CC8 ("reinterprets the problem and
    does not resolve it") and the limitation-7 item.
  - It depends on no removed topic.
  - No sentence reads as resolution.
- **§5.**
  - The distinction is explicit: "not established", "not resolved here", and limitation 4.
  - The H-decouple closure is respected. N-BH3's "closed system in a pure joint state, uncoupled from [D] and [V∖R],
    over whole cycles" is DIFF-REVIEW R1 as accepted.
  - Two defects:
    - **The A.8 scope is overstated as a necessity (C1).** DIFF-RECHECK §5 N1: the diagonal-shell counterexample
      and BH-02's certified Hamming cases show that the value *fails in general* on a proper shell. They do not
      show that it holds *only* on the full product space, because a special shell might coincide. My r5 R1/R2/R5
      text said "only when"/"only for"/"needs … a full-product energy shell", and r6 carries it at five sites. The
      PR's own README already uses the correct form ("holds on the full product space but not in general on a
      proper shell").
    - **N-BH1's compression drops a hypothesis (C2).** r4:181 reads "*Bijective dynamics* with complete endpoint
      access gives exact recovery, and with $\mathcal U$ inaccessible $P_{\rm succ}\ge1/|\mathcal U|$". It also
      notes that 32 non-injective maps violate the bound. BH-01 REPORT:17 likewise states it "with bijectivity".
      r6's one-sentence form states the bound with no bijectivity condition, so it reads as universal, which is
      false. It also drops the definition of "accessible advantage", and its retained "The endpoint guarantees
      above" refers to a guarantee that is no longer stated.
- **§6.1 N-DI1 overclaims by compression (C3).**
  - "The quantum description is the visible law of an embedded observer, and its features with no classical Markov
    analogue are memory carried in an inaccessible sector." Theorem 1 covers fixed-basis Born statistics only.
  - Coherent preparations and noncommuting interventions need conditions (i)–(v), which OI does not imply
    (`oi_alone_not_qm`).
  - Bell-violating correlations need ontic parameter dependence (H-Bell, open), not memory alone.
  - The sentence is conditional on the hypothesis, but even under the hypothesis the corpus supports only the
    fixed-basis statement.

## 4. Length

`chk/budget.py` builds each section from the r4 lines and the quoted new sentences the outline specifies. The
figures carry about ±5% from sentence splitting and math tokens.

| § | Outline | Estimate | Note |
|---|---|---|---|
| Abstract | 240 | ≈ 260 | five r4:12 sentences plus N-AB1/N-AB2 |
| §1 | 430 | ≈ 550 | r4:20–26 = 182; r4:30 less its last sentence; N-INT1; Contributions ≈ 150; r4:34 |
| §2 | 980 | ≈ 1,240 | r4 §2 plus §3.1 = 1,308 words; the sketches save **≈ 140 net**, not 275 (310 removed, 169 added in S-1 to S-5); N-LIT1 and the pointer add ≈ 65 |
| §3 | 900 | ≈ 870 | |
| §4 | 530 | ≈ 460 | |
| §5 | 520 | ≈ 480 | after C2 |
| §6 | 500 | ≈ 570 | |
| **Total** | **≈ 4,100 / 10.4 pp** | **≈ 4,430 / ≈ 11.2 pp** | at 395 words per page |
| Applications | 1,050 / 2.65 pp | ≈ 940 / ≈ 2.4 pp | |

- The window holds: about 11.2 pp is inside 10–12, and the applications are inside 2–3 pp.
- The slack to 12 pp is about 0.8 pp, not 1.6.
- Appendices A and B are outside the count, as the owner allows. Appendix B adds about 550 words.

## 5. Required changes (exact text)

**C1. A.8 scope: "holds on the full product space, fails in general on a proper shell".**
- OUTLINE §5 item 3 (N-BH2), replace sentence 2 with:
  > H-scramble posits equidistribution of the orbit on an energy shell. The mean entropy of that ensemble is Page's
  > average $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$ [Pag93] when the shell is the full product space;
  > on a smaller shell it differs in general, in a direction that depends on the shell [BHb, C6(c)].
- OUTLINE §5 item 4 (N-BH3), replace "Its stated value holds only for a full-product shell, and" with "Its stated
  value is established only for a full-product shell, and".
- OUTLINE §6.2 item 4, replace "needs H-scramble, the closure of the black hole and its radiation over whole cycles,
  and a full-product energy shell, and gives" with:
  > needs H-scramble and the closure of the black hole and its radiation, in a pure joint state, over whole cycles;
  > its stated value is established only for a full-product energy shell; and it gives
- CLAIMS N-BH2, replace "the ensemble mean equals S_Page only on the full product space" with:
  > the ensemble mean equals S_Page on the full product space and differs in general on a smaller shell (exact
  > counterexample: the diagonal shell, H_m − 1; certified Hamming-weight shells)
- CLAIMS N-BH3, replace "The value holds only on a full-product shell" with "The value is established only on a
  full-product shell". Add DIFF-RECHECK §5 N1 to its sources.
- DEPENDENCIES §C (Thm A.8 bullet), replace "holds only when the energy shell is the full product space" with "holds
  when the energy shell is the full product space and fails in general on a proper shell (DIFF-RECHECK N1)".

**C2. OUTLINE §5 item 2, the compressed r4:181 sentence.** Replace the quoted sentence and the bullet "'The endpoint
guarantees above are sufficient, not necessary' is kept" with:
> Of the 40,320 bijections of $\{0,1\}^3$, 1,376 give zero accessible advantage, the gain in success probability over
> a blind guess, for a binary message with one register unread after two emissions. For bijective dynamics, complete
> endpoint access gives exact recovery, and with the joint values $\mathcal U$ of the unread registers inaccessible,
> $P_{\rm succ}\ge1/|\mathcal U|$; these endpoint guarantees are sufficient, not necessary.

In CLAIMS N-BH1, read "the bound P_succ ≥ 1/|U| (for bijective dynamics)".

**C3. OUTLINE §6.1 (N-DI1).** Replace the quoted two sentences with:
> If the hypothesis holds, the fixed-basis statistics of quantum theory are the visible laws of an embedded observer,
> and their departures from Markov behaviour are memory carried in an inaccessible sector; whether the rest of
> operational quantum mechanics follows depends on completion conditions that OI does not imply (§3.2). Two
> long-standing problems would then change form: vacuum energy becomes a question about how two levels of
> description couple to geometry, and black-hole information separates into conservation and accessible recovery.

In CLAIMS N-DI1, replace "the quantum description is an embedded observer's visible law" with "the fixed-basis
statistics are an embedded observer's visible laws (Theorem 1); the operational extension is conditional on
(i)–(v)".

**C4. Process dilation (PD row and S-1).**
- Results register, row PD, Exact statement:
  > r4:66 s4: "A realization whose hidden prior is independent of x₀ exists", for a law with rational multi-time
  > probabilities on a finite horizon, |C_V| ≥ 2 (Main:496)
- OUTLINE §2, S-1, second sentence:
  > For a law with rational probabilities, a realization whose hidden prior is independent of $x_0$ also exists
  > [Main §3.4, Theorem (finite-horizon process dilation)]; it is proved on paper, with exact probes.

**C5. Stochastic-inverse lemma (SI row and r4:114 s1).**
- Results register, row SI, Exact statement:
  > "A finite square stochastic matrix with a stochastic one-sided inverse is a permutation matrix" (= Main:133)
- OUTLINE §2, "Sketches replaced by citations", row r4:114: r4:114 sentence 1 is kept with one change, "A stochastic
  matrix" → "A finite square stochastic matrix". Record this in CHANGES-r6 §4 as a hypothesis restored, not a
  sketch.

**C6. Page budget (OUTLINE "Page budget"; CHANGES-r6 §3 and §5).**
- Replace the word and page figures:
  - Abstract 260;
  - §1 550 (1.4 pp);
  - §2 1,240 (3.1 pp);
  - §3 870 (2.2 pp);
  - §4 460 (1.15 pp);
  - §5 480 (1.2 pp);
  - §6 570 (1.45 pp).
- Total ≈ 4,430 words, ≈ 11.2 pp; applications ≈ 940 words, ≈ 2.4 pp.
- In OUTLINE "Fit" and CHANGES-r6 §3: "save about 275 words, about 0.7 pp" → "save about 140 words net, about
  0.35 pp".
- Slack to 12 pp: about 0.8 pp.

## 6. Nits

1. **OUTLINE §2.** "r4:162's sentence (the instrument …)" → "r4:164's sentence". The decomposition is r4:164. The
   same applies in CHANGES-r6 §3 "Exception kept".
2. **r4:112, kept sentences.** "The rooted form is machine-checked, and Doukas states the same argument concurrently
   [Dou26, Prop. 1]" → "Theorem 3 is machine-checked in its rooted form, and Doukas states the same overlap-and-return
   argument concurrently [Dou26, Prop. 1]".
3. **N-DT1, black-hole clause.** "whether H-scramble and the closure condition hold, and the Page value on the
   relevant shell" → "whether H-scramble and the closure condition hold, the Page value on the relevant shell, and,
   in [GR]'s ladder, the covariant field equations". This makes CHANGES-r6's R14 claim true.
4. **Appendix B pointer.** "a minimal six-state model" → "a minimal model with six hidden states". It has
   2 × 6 = 12 configurations.
5. **Pre-scope provenance.** OUTLINE says `pre-scope/`, CHANGES `design-r6/pre-scope/`. State that it is
   `S/paper/design-r6/pre-scope/` (scratch), not in the repository.
6. **DEPENDENCIES §R.** "AUDIT cites both at SM:851" → "AUDIT cites 'emergent dressing pending' at SM:851; both
   phrases are at SM:849".
7. **§4 item 7 (N-LIT2).** Write out r5's exact N-LIT2 text in OUTLINE-r6 instead of "the same as pre-scope r6
   §5.1", so the outline is self-contained.
8. **PIN.** The bound is in bits (Main:166–170). Add "(in bits)" when the draft states it.

## 7. #937 sites (corpus-consistency review at `5221b53e`): r6 does not cite or lean on any of them

**Method.**
- I read each site at `687e885b`.
- I grepped OUTLINE-, CLAIMS- and DEPENDENCIES-r6 for each line reference.
- I mapped every section-level citation r6 makes onto line ranges: [GR §6.2] is GR:342–363, [GR §3.3] is GR:168–303,
  [GR §2.2] is GR:44–53, [Book §7.6] is the black-hole section, and there are GR App. A cites.

| Site | Topic | r6 |
|---|---|---|
| GR:583 ("gauge degree of freedom") | CC | Not cited. It appears only in §4's "Does not claim" ("that GR:583's gauge argument settles the coupling"). §8.3 is not cited. r6 uses GR:356's two completions in the weaker form (N-CC3) |
| ch19:38; preface:7; ch00:89; Explainer:22, :547 | CC, unconditional | Not cited. Already in DEPENDENCIES-r6 §A as "not usable" |
| ch07:207, ch07:258, ch09:90, GR:32, Substratum:324, SM:132, appendix-c:273 | CC, unconditional or "retrodicted" | Not cited or leaned on. r6 cites no Substratum, SM or appendix-c, and of ch07 only §7.6. GR:32 lies outside every GR section r6 cites. **Missing from DEPENDENCIES-r6 §A** (nit 9) |
| GR:567, GR:711 | QM-emergence scope | Not cited. Already in DEPENDENCIES-r6 §B. r6's text never says "equivalence of quantum mechanics", and §6.2 items 1–2 and C3 keep `oi_alone_not_qm` in view |
| GR:164, ch07:65 ("recovered as a prediction") | horizon entropy | Not leaned on. r6 keeps **no** horizon-entropy or consistency sentence; N-CC6 uses "the de Sitter entropy" only as a standard quantity in a dimensional identity. GR:164 is in §3.2, not the cited §3.3. **Missing from DEPENDENCIES-r6 §R** (nit 9) |

**Two notes.**
- **[GR §6.2], cited for N-CC1–N-CC3, contains two sites DEPENDENCIES §A already lists.** They are GR:356's last two
  sentences and GR:360's "eliminates". r6 states its own conditional sentences and does not quote them. No change is
  needed.
- **No #937 finding materially affects r6's text.** C1–C6 are unchanged by this input.

**Nit 9.** For completeness of the "must not lean on" register (§A.25):
- add ch07:207, ch07:258, ch09:90, GR:32, Substratum:324, SM:132 and appendix-c:273 to DEPENDENCIES-r6 §A;
- add GR:164 and ch07:65 to §R ("Handled only by PR #937");
- source: "#937 REVIEW.md at `5221b53e`".

## 8. Owner items

- **O1.** The DIFF-RECHECK N1 correction (C1) should also reach #936's README and CHANGE-NOTE, as that re-check
  says. My r5 REVIEW R1/R2/R5 text is superseded on this point by C1. The committed review is a frozen record and is
  left as is.
- **O2.** Make reading Weinberg 1989 a landing gate for N-CC0, which otherwise carries an uncited standard number.
  Padmanabhan stays first on the reading list for §4.
- **O3.** The carried items are unchanged: the "H-decouple" label once #936 lands; the A.8 remedy (r6 holds either
  way after C1); the §A.42 Lean retention; the R11 gates; and the 9 VERIFY markers.
