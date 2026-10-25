ACCEPT WITH NITS — 1739f4e05e27f22911dee5e7a9f502089c9807e9 (PR #917, BH-02/BH-04 package `verification/programmes/black-hole-information/bh02_scramble_v1/`; published head 809fac52 + local candidates 6bf2d4b8, ff7b5c85, 836a661e, b25c30f9, 1739f4e0)

Reviewer: independent, read-only. The clone was not modified: `git status --porcelain --ignored` was empty before and after, and HEAD stayed at 1739f4e0. The one change to the clone was `git fetch origin main`, as instructed. Everything else was written only under `rev917b/` (pkg/ = exported files, empty/ = run directory, tools/ = reviewer scripts, mut/ = reviewer mutants, out/ = outputs). Rules applied: AGENTS.md as on `origin/main` (c91bf5dd).

The mathematics holds up. C1, C2, C4 and the greybody cancellation are correct and correctly scoped. The exact values are exact: I recomputed S_Page(4,4) by a different exact route and got the same rational. Replay is byte-identical under normal and -O runs. Every quote in the audit is verbatim. The findings worth fixing are in how the results are worded and classified, mainly in MANUSCRIPT-AUDIT.md and in two REPORT sentences, plus one missing control for C6(c). None of them changes a verdict.

## Evidence per check

### 1. Preregistration and amendments

- **Order is verifiable.** The chain is linear: 809fac52 → 6bf2d4b8 (PLAN.md only) → ff7b5c85 (+A1) → 836a661e (+A2) → b25c30f9 (code and results) → 1739f4e0 (audit).
  - The trees at ff7b5c85 and 836a661e contain no `checks.py`, `mutants.py` or `result.json`.
  - PLAN.md and both amendments are byte-unchanged after their own commits.
  - Commit times (08:23:41, 08:25:35, 08:27:28, then code at 09:20:09) are set by the author. They are consistent with the order, but they cannot prove "before any code ran". That claim rests on the author's word plus the tree contents.
- **A1 is justified, but it was informed by the outcome, and it decided the verdict.**
  - Its hand estimate is right. The concavity bound at (6,3,3) is 2.00698 and S_Page(8,8) is 1.58853 (I recomputed both).
  - So the preregistered half-filling cases could never certify. The three added cases were chosen after a calculation of the very quantity being certified. Under the rule "certify at least one case", A1 therefore fixed the C6(c) verdict.
  - This is disclosed exactly where it matters. The C6(c) verdict text says "all added by amendment A1; the preregistered half-filling cases are not certified by this bound", and REPORT finding 4 repeats it.
  - The substance does not depend on A1. My independent sector-formula values put the shell mean below S_Page in all six cases, and in (12,6,6) and (14,7,7) as well. Acceptable.
- **A2 is a real relaxation, but defensible.**
  - It drops "every other control passes" in favour of "the targeted control is among the failures, and every failure is listed".
  - The stated reason (shared components) is genuine, and the listing makes collateral failures visible. In the actual output, 11 of 15 mutants trip only their target.
  - M-bij trips K-classical and crashes C3; M-rank trips K-overlap and K-tight; M-page-formula trips CT1; M-unitary crashes C5. All are explicable.
  - One of A2's own examples does not occur: M-eig trips only K-eig. This is harmless.
  - Verdict: acceptable, because it is disclosed and the specificity can be checked from the printed lists.

### 2. Proofs

- **C1 is correct.** P_π maps |x⟩ to |π(x)⟩, and an aligned cut of a basis vector has an amplitude matrix with a single nonzero entry. It is scoped to configuration-aligned cuts in REPORT and in the PLAN's "Would not" section.
  - The exhaustive sweep is close to vacuous: it checks that a permutation maps basis vectors to basis vectors. REPORT says the universal claim rests on the proof, which is honest.
- **C2(i) is correct.** The amplitudes are relabelled, so the matrix has at most |supp| nonzero entries and its rank is at most |supp|.
- **C2(ii) is correct.** By Schur–Horn the diagonal is majorized by the spectrum. A marginal has at most the joint entropy, and p_t is a relabelling of p0.
- **C2(iii) is correct.** P_π fixes |+^n⟩, which is a product state. The maximum overlap with a product state is λ_max, so S_∞ ≤ −ln F and S_2 ≤ −2 ln λ_max ≤ −2 ln F.
  - The code checks the intermediate quantity ⟨+_R|ρ_R|+_R⟩ ≥ F exactly. That is a valid and slightly stronger check.
- **C2 tightness is correct.** Exact rank r together with exact purity 1/r forces a flat spectrum (equality case of Cauchy–Schwarz).
- **C4 is correct as stated in REPORT:** the curve ends at its maximum H(p0) and cannot turn over to zero.
  - The brief's paraphrase, "cannot turn down", is stronger than what was proved. The curve can dip in the middle, because p_t changes while R_t grows. Only the endpoint is controlled. Keep REPORT's wording.
- **Greybody cancellation is correct.** t_P/t_evap = 1 − (M_P/M0)³ does not depend on a constant a. It is checked exactly for four values of Γ and three values of M_P³.
  - The step model gives 1 − (16/175)√2 at a2/a1 = 4, μ = 3/4. I derived this by hand.
  - The power law gives 1 − 2^{−(3+p)/2}, which I also derived.
  - The O(μ³) correction claim is right: the fraction is (1 − √2/4)/(1 − μ³(1−ρ)).

### 3. Exactness

- **Exact claims are computed exactly.**
  - Ranks use Fraction Gaussian elimination.
  - Purities and F are exact rationals.
  - Page values are harmonic sums in Fraction.
  - 1 − √2/4 is an element of Q(√2), certified by 8(1−f)² = 1 exactly.
  - Logs use an atanh series with a correct remainder bound. `_down`/`_up` act on Fractions, so they are exact.
- **Numerical quantities are labelled NUMERICAL and controlled by K-eig:** 56405 diagonalizations, trace, purity and positivity all within 1e-12, and a complex-versus-real-embedding cross-check.
- **Independent recomputations** (`tools/indep.py`, my own code):
  - **Page values by a second exact route.** I used the Wishart one-point density (Laguerre polynomials) with the trace factorization E[T ln T] = mn ψ(mn+1). The γ terms cancel exactly.
    - Results: S(2,2) = 1/3, S(2,4) = 107/210, S(3,3) = 1669/2520, **S(4,4) = 664789/720720**, S(2,8), S(4,8).
    - All equal the harmonic formula exactly.
  - **The −1/2 limit.** S_Page(m,m) − ln m for m = 2…128 gives −0.3598, −0.4639, −0.4909, −0.4977, −0.4994, −0.49986, −0.49996.
    - Analytically, H_N = ln N + γ + 1/(2N) + O(N⁻²) gives H_{m²} − H_m − (m−1)/(2m) − ln m → −1/2.
  - **C1 sample.** 200 random permutation-orbit points at n = 4 across 4 cuts all have exact rank 1.
  - **C2 instance.** I used (1/3, 2/3, −2/3) on 3 configurations at n = 4, permuted.
    - Rank 2 ≤ supp 3. Exact purity 49/81.
    - λ_max = 0.7291 ≥ F = 1/144.
    - S_2 = 0.503 ≤ −2 ln F = 9.94.
    - S = 0.584 ≤ H(p_R) = 0.687 ≤ H(p0) = 0.965.
  - **C7 values.** 1 − 2^{−7/4} = 0.7026982. For β = 1.4847: S/S0 = 0.5975369, fraction lost 0.4024631, t_P/t_evap = 0.5381009. The step value is 0.8707005.
  - **Shell values.** The sector formula and the canonical bound match the package to 6 decimals in all six cases.

### 4. C6 (highest priority)

I read GR Appendix A in full (lines 717–869).

- **(a) is a fair reading of GR as written.**
  - The factorization is configuration-aligned. A.1 sets up configuration spaces, and A.2 builds U_φ on H_V⊗H_B⊗H_D by Stinespring from φ. Main §3.2 builds it the same way on configuration-indexed factors.
  - A.8 sets d_B = |C_B(t)| and d_R = |C_R(t)|. A.7 takes R ⊂ V as a set of coordinates.
  - "Definite initial state" (A.7) is a reading, but A.8 supports it. A.8 counts "initial conditions on Σ_E" by |Σ_E| and averages f(s) over s ∈ C_j, so its initial conditions are configurations.
  - GR names no factorization that is not aligned. So C6(a) applies to GR's own setting: H-scramble cannot hold for any φ, and A.8's conclusion fails for every initial configuration.
  - What remains conditional: the result does not cover an emergent factorization that GR does not specify, or a superposed initial state. Even for a superposition, C2 caps the entanglement at H(p0). H-scramble at the turnover would therefore need an initial state spread over at least about e^{S_Page} configurations, which is not a "definite" state.
  - Recommend citing A.8's counting over configurations as the textual anchor, in addition to the A.7 phrase.
- **(b) "imported, not derived" is supported.**
  - In A.8's proof, S_Page enters only through PSW/Haar concentration, and H-scramble is what carries the Haar fraction over to the orbit.
  - The cycle decomposition contributes exact time averages and the bound ln d_min.
- **(c) The shell point is right, and in fact stronger than stated, but its direction is not universal.**
  - A.8 states S_Page(d_B, d_R) with the full dimensions while concentrating on a shell subspace. PSW on a subspace concentrates around the shell's own typical value.
  - The three certified Hamming-weight cases are correct (rigorous intervals, recomputed).
  - The shell can also lie above S_Page. A diagonal shell span{|i⟩|i⟩} (energy = Hamming distance between b and r, at E = 0) gives a Haar mean of exactly H_m − 1. That exceeds S_Page(m,m) for m = 2, 3, 4, 8, 16 (0.5 > 1/3; 13/12 > 0.9224). Monte Carlo agrees: 0.49992 ± 0.0004 and 1.08298 ± 0.0004.
  - So what is shown is: the value depends on the shell, and with full dimensions it is wrong in general. "Below" holds only for the Hamming-weight cases tested.
- **(d) is a real gap.**
  - A.8 averages over a whole cycle (of order |Σ_E| steps) at a fixed bipartition and a fixed shell.
  - A.9 uses that result pointwise in t, with d_B(t) and d_R(t) moving on timescales far shorter than any cycle. A.9's proof is "direct substitution" and does not address this.
  - It is correctly recorded as an open obligation, with no computation claimed.

### 5. C3 and the safeguard

- The safeguard is respected. Every quantum input is labelled SUPPLIED. The C3 verdict states that it is "not a derivation of H-scramble" and gives the C2 cap and the C1 zero. CC4 shows that |+^n⟩ is never entangled.
- One over-reading in REPORT finding 2: "The capacity to scramble is a property of the supplied initial state, not of φ" (see F7).

### 6. C7 and the external Page 2013 control

- **Use of the abstract or database record.** Relying on these is acceptable here and is labelled in PROVENANCE.json and in REPORT's limitations.
  - I could not fetch the source myself: the proxy refused arxiv, inspire, crossref and semantic scholar.
  - The three quoted numbers are mutually consistent under the formula: 1/(1+β) = 0.40246, matching 40.25%, and 1 − (β/(1+β))^{3/2} = 0.53810.
- **What K-page2013 actually checks.** Page 2013 itself derives 0.5381 from this accounting. K-page2013 therefore confirms that the β formula is Page's accounting, transcribed correctly. It is not an independent physics test, and it resolves only to 4 decimal places: my mutant with exponent 1.5001 passes.
- **"Only exponents enter, no OI quantity" is essentially right.** σ, ħ and Γ cancel. Input (ii), the β = 1 turnover identification n_R = n_B(0) − n_B, is not an exponent, but REPORT lists it as an input.

### 7. MANUSCRIPT-AUDIT.md

- **Quotes and lines.**
  - All 19 items and the 7 propagation bullets were checked by script (`tools/quotes.py`) and by hand against 809fac52. Every quoted fragment appears verbatim on the cited lines.
  - Every `FULL:n` mirror line is byte-identical to its chapter line.
  - Two line nits:
    - Item 4's "the corrections are exponentially small" is at ch07:132 (FULL:2007), not 130–131.
    - Item 13's "where d_B = |C_B(t)|, …" is at GR:827, not 823.
- **Classifications.** Most are right. Exceptions are listed as F1–F4.
- **Omission.** The audit misses one restatement: ch07:114 (FULL:1989), "The Page time occurs at approximately half the black hole's entropy has been radiated". Under Page's own accounting the figure is 40.25% (C7(e)).

### 8. Controls and mutants

- **Author's battery.** I ran it once on the exported files from an empty directory (`out/mutants.txt`). It exited 0 with "ALL MUTANTS CAUGHT", and its output is **byte-identical to the committed `mutants-output.txt`** (cmp). Each control was seen to fail under its own mutant.
- **My mutants** (`tools/mymutants.py`):
  - R1: a leak on basis states in C1 (non-permutation). The C1 verdict flips to COUNTEREXAMPLE (4 states). This holds both with the single-nonzero shortcut and with rank alone.
  - R2: a rotation on top of the permutation in C2. 12 exact violations; the verdict is COUNTEREXAMPLE.
  - R3: a consistent error in the Page value that vanishes at m = 2. K-page-formula catches it. On its own the 4×4 Monte Carlo would have passed it (0.9241 ± 0.0018). R3b (+1e-6) is also caught.
  - R4: Q(√2) coefficient + 1e-9 is caught by K-ode. R4b (β exponent 1.505) is caught by K-page2013. R4c (1.5001) is not caught, which is expected at 4-decimal resolution.
  - R5: canonical bound × 0.9 in C6(c). **No control fails.** By arithmetic, a factor of 0.78 would falsely certify all six cases (see F3).
- **CC5 control.** CC5 is not a sharp countercontrol (see F4).

### 9. Replay and hygiene

- `sha256sum -c SHA256SUMS`: all 11 files OK.
- From an empty directory, `python3 -I -B checks.py` (twice) and `python3 -I -B -O checks.py` both reproduce result.json byte for byte, exit 0, in about 50 s.
- `report.py` reproduces REPORT.md byte for byte.
- There are no `assert` statements in checks.py, mutants.py or report.py.
- No absolute paths, e-mail addresses, tokens or secrets appear in the package.
- The diff 809fac52..1739f4e0 touches only the package directory.
- From the clone root: `tools/duplicate_check.py` OK; `tools/voice_check.py` OK (40 files); `tools/artifact_placement_check.py` OK (self-test passed).
- The worktree was clean before and after.

## Findings, ranked, with fixes

- **F1 (medium; audit over-reach, witness → universal).**
  - Item 13 says: "Haar on a proper shell gives a value strictly below S_Page(d_B, d_R) with these full dimensions". Item 4 has a similar "below".
  - As a universal statement this is false: the diagonal shell has Haar mean H_m − 1 > S_Page(m,m), exactly.
  - Fix: write "differs from (for the Hamming-weight shells tested, lies below; certified in three cases)". Keep the proposed GR text, which says "replaced by the Haar-on-shell mean".
  - Optionally, REPORT finding 4 and the C6(c) verdict could say the direction depends on the shell.
- **F2 (medium; unproved claim in proposed GR text).** Item 19's proposal adds "H-scramble is itself an equidistribution hypothesis, stronger than ergodicity". Nothing in the package shows that H-scramble implies single-cycle ergodicity: an orbit's weights on invariant cycle subspaces are conserved, so the two properties are not obviously ordered. Fix: "an equidistribution hypothesis on the orbit over pure states, which ergodicity over configurations does not supply (one long cycle satisfies the latter with S = 0)".
- **F3 (medium-low; a decisive verdict without a control).**
  - The C6(c) CONDITIONAL verdict rests on the canonical-entropy bound, and nothing checks that bound: the R5 mutant passes with zero failed controls.
  - The values are correct (I recomputed them independently), so the verdict stands.
  - Fix:
    - Add a control requiring the Monte Carlo mean to be at most the canonical upper bound in every case.
    - Recompute the canonical entropy by a second path, either by diagonalizing Tr_B Π_w/D numerically or by summing over explicit basis states.
- **F4 (low; CC5 design).**
  - H(p0) = 2.1988 lies inside the Page-like band [S_Page − 0.10, S_Page + 0.10] = [2.1749, 2.3749]. So C2 does not imply "0/40 Page-like". The control passed on outcome, not by construction.
  - Fix: use a state with H(p0) < S_Page(16,16) − 0.10. For example, (24/25|0⟩ + 7/25|1⟩)^7 ⊗ |0⟩ has H(p0) = 1.925.
- **F5 (low-medium; misattribution of published text).**
  - REPORT finding 1 says "The appendix's sentence that a bijection 'can' visit only product states understates this".
  - That sentence is book/ch07-gravity.md:126 (FULL:2001), not GR Appendix A. GR:837 already says "every visited state is a product state", for one long cycle.
  - MANUSCRIPT-AUDIT items 3 and 14 attribute both correctly. Fix the sentence in report.py and regenerate REPORT.md.
- **F6 (low; classification strength).**
  - **Items 1, 3 (first sentence) and 9** mark "derived from cycle typicality", "runs through the combinatorial structure" and "it can be combinatorial" as **contradicts**.
    - C3 shows that a permutation, which is combinatorial, does produce Page-like states from a superposition.
    - So the contradiction holds only for a definite initial configuration in the configuration factorization. In general the sentences are "conditions"/"not supported": they need a superposed initial state with H(p0) ≥ S_Page, which A.7's "definite initial state" excludes.
    - Fix: state that scope in each classification.
  - **Item 5** marks "fixed by … bijectivity and … boundary-mode counting" as contradicts.
    - The mode counting does supply S ∝ M² and the β = 1 identification. What fails is "bijectivity" (it does not enter the fraction) and "distinctive", because the same number appears in any model with these inputs.
    - Fix: narrow the classification accordingly.
- **F7 (low; C3 wording).**
  - REPORT finding 2: "The capacity to scramble is a property of the supplied initial state, not of φ".
  - H(p0) and F are upper bounds only. |+^n⟩ has the maximal H(p0) and is never entangled (CC4), and local permutations at depth 2 or less give S = 0.
  - Fix: "The entanglement any permutation can produce is bounded by properties of the supplied initial state (H(p0), F); reaching the bound also needs a permutation that mixes the state's phase pattern across the cut."
- **F8 (low; audit completeness and line nits).**
  - Add ch07:114 / FULL:1989 ("approximately half the black hole's entropy") under C7(e).
  - Correct item 4 to lines 130–132 (FULL:2005–2007) and item 13 to GR:827.
  - Item 14 proposes 0.922 while GR's displayed S_Page (A.8) is the large-dimension formula. Either change the display as well, or write "0.886 in the large-dimension form (exact Haar mean 0.922)".
- **F9 (nits).**
  - The −1/2 limit is shown only as a finite sequence. Add the one-line analytic limit (H_N asymptotics) to REPORT, so that no finite sequence stands in for a limit.
  - K-ode part (a) checks the difference quotient of a function defined to be linear, which is tautological. The Simpson integration is the real control. `rk4_page_time` is Simpson's rule, not RK4.
  - report.py hard-codes several numbers that it should read from result.json: 0.8862943611, 0.9223956598, "tending to −1/2", 0.5381, 40.25%, "all off half filling". They match result.json today.
  - C6(b)'s wording "imported … rather than produced by the substratum dynamics" would be clearer as "follows from the hypothesis H-scramble on the orbit, not from bijectivity or the cycle decomposition". A dynamics that satisfied H-scramble would produce the value.

## Additional observation (assumption-watch; outside this package's claims)

GR A.6(iii) takes ρ_B and ρ_D maximally mixed (the uniform Liouville prior, which makes the channel unital). A.6(i) and A.7 take the total state pure "from a definite initial state". Under the framework's own uniform-prior trace-out, the B∪R state is mixed. The relevant curve is then C4's classical one, which does not turn over. Recording this for BH-02 follow-up.

***

# Re-check of the fix commit

ACCEPT WITH NITS — 91e2230a745a5a944696308d5a5944f04581d765 (parent 1739f4e0)

The fix commit was exported to `pkg2/` and run from `empty2/`. I re-checked the diff 1739f4e0..91e2230a against each finding.

## Preregistration, replay and hygiene

- **Preregistration unchanged.** PLAN.md, A1 and A2 are byte-identical (cmp), and the diff does not touch them.
- **Integrity.** SHA256SUMS: 11/11 OK.
- **Replay.** `checks.py` under `-I -B` (twice) and under `-I -B -O` reproduces result.json byte for byte, exit 0. `report.py` reproduces REPORT.md. There are no asserts.
- **Scope of the diff.** It touches only the package directory.
- **Repository checks.** duplicate_check, voice_check and artifact_placement_check all pass. The worktree was clean before and after.
- **result.json changes.** A leaf diff (`tools/jdiff.py`) confirms PROVENANCE's claim. The only changed leaves are the CC5 fields and the C4, C6(a), C6(b) and C6(c) verdict strings. Everything else is an addition, and no previously reported number moved.

## Findings, one by one

- **F1 fixed.** The diagonal-shell result has been added.
  - Exact values: 1/2, 5/6, 13/12, 481/280 and 1715839/720720. Each equals H_m − 1; I checked against H_8 = 761/280 and H_16 = 2436559/720720.
  - Each is compared exactly with S_Page(m,m).
  - Monte Carlo at m = 2, 4, 8 is within 4 standard errors. This is control K-diag.
  - The words "strictly below" are gone from REPORT and the audit. Items 4 and 13 and the C6(c) verdict now say the direction depends on the shell.
- **F2 fixed.** "Stronger than ergodicity" is removed, and the text now says "no ordering … is claimed".
- **F3 fixed.** New control K-shell recomputes the canonical spectrum from explicit basis-state counts. That path is independent of the comb-based sector multiplicities: the spectrum is compared exactly, and the float entropy must fall inside the rigorous interval. Scaling the bound either up or down fails it. Remaining nit: the counts share D = comb(n,w) with the code they check. Adding Σcounts == D would cost nothing. (A wrong D would already trip K-eig through the Monte Carlo dimension.)
- **F4 fixed.** The CC5 state is now (24/25,7/25)^7 ⊗ |0⟩, with H(p0) = 1.923909, below the band edge of 2.1749. The implication "C2 rules out a Page-like state" is part of `cc5_ok`.
- **F5 fixed.** The "can" sentence is now attributed to ch07:126 (FULL:2001), and GR:837 is cited for the GR version.
- **F6 fixed.** Items 1, 3 and 9 say "contradicts (definite configuration, aligned split); otherwise conditions / not supported", and the setting is defined in the header. Item 5 is narrowed.
- **F7 fixed.** The capacity sentence is rewritten in terms of bounds and a mixing requirement.
- **F8 fixed.**
  - Item 20 (ch07:114 = FULL:1989) is added. Its quote is verbatim and the mirror line is identical.
  - Item 4 now cites lines 130–132 (FULL:2005–2007, mirror identical). Item 13 cites 823–827.
  - Item 14 now gives both 0.886 (the display at GR:829, which I confirmed is the large-dimension form) and 0.922.
- **F9 fixed.**
  - **Finite-size term.** I re-derived the analytic limit: H_N = ln N + γ + 1/(2N) − 1/(12N²) + O(N⁻⁴) gives −1/2 + 7/(12m²) + O(m⁻⁴). The m⁻⁴ coefficient is −1/12 − 1/120 = −11/120. That predicts (S − ln m + 1/2)·m² = 7/12 − 11/(120·1024) = 0.583244 at m = 32. The package reports 0.5832438188, which matches.
  - **K-ode** is now the Simpson integration plus the exact Q(√2) check. C7(a) and C7(c) are recorded as identities, and the verdict reads VOID if they fail.
  - The function is renamed to `simpson_page_time`.
  - **report.py** no longer hard-codes 0.886, 0.922 or 0.5381. The two remaining literals are β = 1.4847 and the limitations text.
  - The C6(b) wording and the C4 endpoint note are added.

## Mutants (§A.40: subset only, run once)

I ran `tools/subset_mutants.py`, which calls the package's own `run_one`, on four mutants:
- M-canonical and M-diag, which are new;
- M-cc5, whose target `low_entropy_state` changed;
- M-ode, whose K-ode composition and patched function name changed.

All four were caught with `run=clean`, and each line is byte-identical to the committed `mutants-output.txt`.

I did not re-run the other 13 locally, because their target code is unchanged. Two committed collateral changes are consistent with the new controls sharing code, but I did not re-run them:
- M-page-mc now also trips K-diag, which uses `haar_state`.
- M-ln now also trips K-shell, which uses `ln_interval`.

## Point 1: the Page 2013 values

- **Where they are labelled.** PROVENANCE says "abstract and database-record text … full text not accessed". The REPORT limitations say the values were "read from the abstract … full text … not consulted". The literature-control record now records that it checks only to 4 decimal places and that it "confirms the beta formula is Page's accounting, not an independent physics test".
- **No verdict depends on them as established.**
  - C7's COUNTEREXAMPLE to the unconditional reading follows from the computed β-sensitivity table (any β ≠ 1) and from the mass-dependent-coefficient models.
  - The quoted values only gate K-page2013, and that gate fails safe.
  - The phrase "reproducing the literature value" in the C7 verdict is the only place that leans on them.
- **Remaining nit.** MANUSCRIPT-AUDIT.md cites these figures at lines 32, 105, 162, 165 and 224, including in the item 20 proposal and in the proposals for items 5 and 17 for GR. None of these sites says the figures come from the abstract only or are pending verification.
- **Fix.** Add "(Page 2013 abstract/database record; full text not checked)" at those sites or in the audit header. Verify against the full text before any proposal that quotes 0.538 or 40% is adopted into the manuscripts. Also change "reproducing the literature value" to "reproducing the value quoted in the abstract".

***

# Re-check of the nit-fix commit

ACCEPT — 1f1aec6f4ffd3b41017f47a44535cf822ab2710e (parent 91e2230a)

Both nits from the previous re-check are fixed. One cosmetic issue in the new `--only` option is noted at the end; it does not affect the verdict.

1. **Scope of the change.** The diff 91e2230a..1f1aec6f touches only the package directory. PLAN.md, A1 and A2 are byte-identical to the versions in 6bf2d4b8, ff7b5c85 and 836a661e. SHA256SUMS checks 12 of 12 files OK, now including `mutants-targeted-output.txt`.
2. **Nit 1 (Page 2013 labels) is fixed.**
   - **Audit header.** It quotes β = 1.4847, 0.5381 and 40.25%, says the full text and Page 1976 have not been read, and says that conclusions resting on these values stay pending. It also bars adopting proposals 1, 5, 17 and 20 until the full text is checked.
   - **Every site in the audit carries the label "[Page 2013 abstract value; full text unverified]".** I grepped each use: lines 39, 112, 169, 172–173 and 231.
   - **REPORT.** The C7 verdict now reads "reproducing the value quoted in the abstract of Page 2013 (full text unverified)". The Page-time paragraph (lines 126–129) and the limitations (line 191) are labelled as well.
   - **One unlabelled line.** The computed sensitivity row at REPORT line 70 (β = 14847/10000) carries no label. It is an output computed at a stated β, so I accept it as is.
3. **Nit 2 (K-shell total) is fixed.** `canonical_by_enumeration` now also requires `sum(counts) == comb(n, w) == D`.
4. **The new `--only` selector.**
   - **Mutant definitions are unchanged.** The diff of mutants.py is confined to `main()`, and lines 1–165 are identical, including the MUTANTS list.
   - **A full run cannot skip anything.** Without the flag, the selection is all 17 mutants, and `mutants-output.txt` is unchanged.
   - **A targeted run always identifies itself.** It prints a "targeted run: …" line, so it can never cmp equal to the full output.
   - **I ran one targeted mutant,** `--only M-canonical`: it was caught cleanly, and its line is identical to `mutants-targeted-output.txt`.
   - **Cosmetic issue.** With `--only`, a name that is misspelled or unknown is silently dropped. A selection that ends up empty still prints "ALL MUTANTS CAUGHT". Suggested fix: exit 2 on an unknown name or an empty selection, and print "TARGETED: n/n caught".
5. **result.json and replay.**
   - The leaf diff against 91e2230a shows a single change, the text of /C7/verdict.
   - Replay is byte-identical under `-I -B` (run twice) and under `-I -B -O`, and `report.py` reproduces REPORT.md.
   - There are no asserts.
   - duplicate_check, voice_check and artifact_placement_check pass, and the worktree was clean before and after.

***

# Re-check of the full-text citation commit

ACCEPT — ce7937d22a284a528d12bd1d50b06dbea9845bfc (parent ee2d4e68)

1. **Scope.**
   - The diff ee2d4e68..ce7937d2 touches only files in the package: MANUSCRIPT-AUDIT, REPORT, report.py, PROVENANCE, result.json and SHA256SUMS. In checks.py it changes two string literals.
   - PLAN.md, A1 and A2 are byte-identical.
   - mutants.py and both mutant outputs are unchanged.
   - SHA256SUMS: 12/12 OK.
   - The parent ee2d4e68, which I had not seen before, makes `--only` exit 2 (VOID) on an unknown name or an empty selection. That resolves my earlier cosmetic note. The mutant definitions are untouched.
2. **Citations against LITERATURE-v2 and the PDFs.**
   - I compared each citation with LITERATURE-v2 §1, §2 and §6. I also checked each one against the PDF pages themselves, using the files under `revlitbh/dl`, whose sha256 matches PROVENANCE: Page 2013 43ba2ce2…, Page 2005 cc977f7f….
   - Page 2013:
     - β ≈ 1.48472 is Eq. (2), p.6.
     - t* ≈ 0.53810 t_decay is Eq. (8), p.11.
     - "about 40.25%" is on p.12.
     - τ₁₂ = (1−f)/(1+β) is Eq. (14), p.19.
   - Page 2005:
     - Eqs. (5)–(10) are on pp.10–11.
     - Eqs. (19)–(21) are on p.13.
   - PROVENANCE records that Page 1976 itself was not read.
   - No "unverified", "abstract value" or "pending" tag remains.
3. **The §6 fixes.**
   - **Item 1** is verbatim §6(b): "0.5381 at constant α with Page's photon-and-graviton β ≈ 1.4847 [Page 2013, Eqs. (2), (8)]".
   - **Item 5:** 0.538 is now attached only to the entropy-accounting clause, "at constant mass-loss coefficient". The mass-dependent clause stands alone ("would move it"). The β > 1 clause is limited to "emission into empty space" and cites Page 2005 Eqs. (5)–(10).
     - **Optional nit:** §6(b)'s wording was "for *semiclassical* emission into empty space". Page 2005's inequality also assumes semiclassical geometry and independent thermal modes, so restoring "semiclassical" would track the source exactly.
   - **The header** now reads "Proposals 1, 5, 17 and 20 may be adopted as far as these sources support them: … that species content, constant α and emission into empty space". That lifts them no further than LITERATURE-v2 §6 does.
   - **Items 17 and 20** keep their confirmed wording and gain citations. Item 17 already carries "for constant Γ".
4. **result.json and replay.**
   - The leaf diff against ee2d4e68 shows exactly two changes, both text: /C7/verdict and /C7/e_literature_control/source. K-page2013's logic and every number are unchanged.
   - Replay is byte-identical under `-I -B` (run twice) and under `-I -B -O`, and `report.py` reproduces REPORT.md.
   - duplicate_check, voice_check and artifact_placement_check all pass.
   - The worktree was clean before and after.
   - No absolute paths or e-mail addresses appear in the package.
