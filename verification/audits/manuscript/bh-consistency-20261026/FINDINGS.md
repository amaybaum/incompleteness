# R11/R12: book and GR sites against the black-hole packages (read-only investigation)

Read at `main` `687e885b`. No repository file was changed. Written by the coordinator from the investigator's
report; the investigator's scratch tools are in `probe/` (`itemF_check.py`, `page_checks.py` and their `.out`
files) and the package replays in `replay-bh01/` and `replay-bh02/`.

## Checks run

- **BH-01 replay** (blobs at 687e885b): `result.json` reproduces byte for byte, and SHA256SUMS passes.
- **BH-02 replay:** `checks.py | cmp - result.json` gives identical output, and SHA256SUMS passes.
- **Item F recomputed independently** with exact rational intervals:
  - at 30 M☉, t_evap/τ_B^D ∈ [1.7853e57, 1.7856e65];
  - t_P/τ_B^D ≥ 1.154e57;
  - the crossover mass is in [1.059e10, 4.917e12] kg.
- **Page's exact mean entropy** (a Haar-random pure state): at m=n, S−ln m = −0.360, −0.464, −0.491, −0.498,
  −0.4994 for m = 2…32.
- **Page-time fraction with a mass-dependent coefficient:** for α∝M^{−p} it is 1−2^{−(3+p)/2}, giving 0.7027 at
  p=½.
- **Mirrors.** Every mirror quoted is byte-identical (full-line `grep -nxF`):

  | Book line | FULL line |
  |---|---|
  | ch07:110 | 1987 |
  | ch07:126 | 2003 |
  | ch07:159, :161 | 2036, 2038 |
  | ch18:130 | 4950 |
  | ch18:146 | 4966 |
  | ch18:148 | 4968 |
  | ch18:158 | 4978 |
  | ch19:334 | 5510 |

## Summary table

**Verdicts:** 9 SITE-ERROR (one of them conditions-level, R12), 1 CONSISTENT (ch18:130), 0 INTRO-ERROR,
0 UNDETERMINED among the listed sites. One related conflict without a marker is UNDETERMINED (§C.4).

| # | Site / FULL | Claim (status) | Support: what it proves, at which layer | Verdict |
|---|---|---|---|---|
| 1 | ch07:110 / 1987 | Resolves the paradox "because φ is bijective" | Main:66: bijectivity is a premise. BH-01 C1: written proof, sufficient only. BH-01 claim A: counterexamples, exhaustive finite. Anchors ch07:157 and ch19:72 separate conservation from recovery | SITE-ERROR |
| 2 | ch07:126 / 2003 | s1: the derivation is combinatorial. s2: PSW corrections vanish exponentially | GR A.8 (prose proof): value via H-scramble. BH-02 C6(b) (proof reading), C1 (proved plus exhaustive), C5 (exact). Own exact check | SITE-ERROR (s1, s2) |
| 3 | ch07:159–161 / 2036–2038 | Falsifier: a radiation deficit "that cannot be reproduced by the nested trace-out" | BH-01 claim A (exhaustive finite), claim E (proved identity). BH-01 audit L155 "unfalsifiable as stated", accepted by its recheck | SITE-ERROR |
| 4 | ch18:130 / 4950 | Preserves information, Page curve conditional; "framework-level interpretations" | Self-scoped; matches ch19:30 | CONSISTENT |
| 5 | ch18:146 / 4966 | Resolution from bijectivity; nested formalism "reproducing the Page curve" (unconditional) | GR A.1–A.4: consistency only (claim E). GR A.8–A.9: conditional on H-scramble | SITE-ERROR |
| 6 | ch18:158 / 4978 | Radiation preserves substratum information "through the nested partition" | Claims E and A; inconsistent with ch18:150 | SITE-ERROR |
| 7 | ch19:334 / 5510 | "Resolved (Page curve from typicality)" | GR A.8–A.9 conditional; ch19:72; appendix-a G11 class C | SITE-ERROR |
| 8 | GR:811 | τ_evap ≪ τ_B^D, so D is decoupled | Thm A.5 holds only for t ≪ τ_B^D (prose proof). BH-01 item F (exact intervals), confirmed by own recomputation. No other decoupling argument in the corpus | SITE-ERROR (false inequality) |
| 9 | GR:869 | A.8 "invokes only PSW … no ergodicity assumption" | GR:817 and :831–833 require H-scramble; BH-02 C1. ch07:147 already corrected | SITE-ERROR |
| 10 (R12) | ch18:148 / 4968 | "mass-independent fraction" | GR:849–863 and ch07:137 assume constant α. BH-02 C7 (exact algebra plus ODE control). Own check | SITE-ERROR (conditions level) |

## Proposed wording for each SITE-ERROR

1. **ch07:110.** "resolves the paradox at the structural level … because φ is bijective" infers resolution from
   bijectivity. Bijectivity is a premise (Main:66) and gives only global conservation. BH-01 claim A shows it does
   not imply recovery from accessible records. The book's own ch07:157 and ch19:72 already separate the two.
   - **Replace with:** "The framework resolves the paradox at the level of information preservation: information is
     never lost from the substratum bijection φ because φ is bijective; how much of that information an observer can
     recover from the radiation is a separate question, which bijectivity alone does not settle and which the
     Page-curve derivation below addresses under its own conditions."
   - Keep sentence 3.
2. **ch07:126, two errors.**
   - **Sentence 1** attributes the derivation to the combinatorial structure. In GR Thm A.8 the cycles only supply
     time averages; the Page value enters through H-scramble (BH-02 C6(b)). On a definite configuration every
     bijection gives S=0 (BH-02 C1). **Replace with:** "The framework's derivation of the Page curve does not use the
     gravitational path integral: the cycle structure of the bijection φ supplies exact time averages, and the Page
     value enters through a typicality condition on the substratum orbit."
   - **Sentence 2** is false as written: the mean correction does not vanish exponentially in the dimension. It tends
     to ½ nat at equal dimensions and falls only polynomially otherwise. **Replace with:** "…for a bipartite quantum
     system in a Haar-random pure state, the marginal entropy of the smaller subsystem concentrates near Page's mean,
     about ln d_min − d_min/(2d_max), with deviations from it exponentially unlikely in the dimension."
   - No Introduction marker covers sentence 2.
3. **ch07:159–161.** The falsifier in 161 sentence 1 excludes nothing. Bijective dynamics reproduces radiation with
   no information (BH-01 claim A), and nested-trace consistency holds for every map (BH-01 claim E).
   - **159 sentence 1:** "The framework's resolution" → "The framework's account".
   - **161 sentences 1–2:** "Bijective dynamics is compatible with radiation that carries less information than the
     matter that formed it when the remainder is held in a sector the observer does not read, a remnant or the
     trans-cosmological region, and the nested trace-out is consistent for every dynamics; a measurement of the
     radiation alone therefore does not test the conservation claim, which rests on bijectivity as a premise. The
     QES + islands computations, which obtain a unitary Page curve…" The rest is unchanged.
   - No replacement falsifier is proposed.
4. **ch18:146.** It says "resolution" from bijectivity, and claims the nested formalism reproduces the Page curve
   unconditionally. **Replace with:** "Chapter 7 §7.6 developed the framework's account of the information paradox.
   Information is never lost from the substratum bijection φ because φ is bijective; whether the radiation carries it
   is a separate question, which bijectivity alone does not settle. [sentence 3 unchanged] The framework's
   nested-partition formalism (…) provides a self-consistent emergent quantum description that preserves unitarity at
   the substratum level; the Page curve at the emergent level follows under the scrambling condition H-scramble,
   which is not established (Chapter 7 §7.6)."
5. **ch18:158.** "(which it does, through the nested partition)" is refuted by BH-01 claims E and A, and is
   inconsistent with ch18:150. **Replace with:** "(the substratum preserves it, by bijectivity; whether the radiation
   carries it bijectivity alone does not settle)".
6. **ch19:334.** "Resolved (Page curve from typicality)" contradicts ch19:72, G11 in appendix A (class C,
   "Scrambling condition open") and ch09:127. **Replace with:** "Conditional (H-scramble)".
7. **GR:811.** "τ_evap ≪ τ_B^D" is false by at least 57 orders of magnitude at GR's own 30 M☉ example with
   τ_B^D ~ 1e17 s. It fails for every black hole above about 5×10¹² kg. No other argument for decoupling D exists in
   the corpus: Substratum covers only a deep sector that is coupled at no order. Thm A.7 is correct within its stated
   scope, t ≪ τ_B^D. **Replace with:** "Theorem A.5 freezes D only on timescales t ≪ τ_B^D, with
   τ_B^D ~ 1/H ~ 10¹⁷ s (§A.5), whereas τ_evap ≫ τ_B^D for every black hole heavier than about 5×10¹² kg
   (τ_evap/τ_B^D > 10⁵⁷ at 30 M☉). Theorem A.7 therefore holds on t ≪ τ_B^D; applying it out to the Page time and
   to τ_evap, as Theorems A.8–A.9 do, assumes in addition that D stays decoupled from B∪R over the evaporation, which
   timescale ordering does not supply."
8. **GR:869.** "invokes only Popescu-Short-Winter … no ergodicity assumption" contradicts Thm A.8's own H-scramble
   hypothesis (GR:817, :831–833). One long cycle is ergodic and has S=0 throughout (BH-02 C1). ch07:147 was already
   corrected in the same commit (6adfff0e), so the paper lags the book.
   - **Replace with:** "…through the cycle-typicality argument of Theorem A.8, which applies Popescu-Short-Winter [29]
     to the deterministic substratum dynamics on the energy shell under H-scramble, with no replica trick and no
     gravitational path integral; H-scramble is an equidistribution hypothesis on the orbit over pure states, which
     ergodicity over configurations does not supply."
   - The last sentence of GR:869 is conditional and is kept.
9. **R12, ch18:148.** "mass-independent fraction" drops the condition of a constant coefficient that ch07:137
   states. BH-02 C7: an M-dependent α moves the fraction. **Replace with:** "For a mass-independent emission
   coefficient (Chapter 7 §7.6), its Page time is a fixed fraction of the evaporation time set by …".

## A. Evidence by site

### A.1 ch07:110
- **Claim.** A conservation clause, plus the status word "resolves" applied to the paradox as ch07:112–114 defines
  it: the radiation carries no information, against unitarity.
- **Support.**
  - Main:66 makes bijectivity an imported premise and itself calls the black-hole case "a paradox to be resolved"
    under that premise.
  - BH-01 C1 is sufficiency under complete endpoint access.
  - BH-01 claim A shows that bijectivity does not imply recovery.
- **Introduction:** r2:180 and r2:183.
- **Pressure test.** Could "at the structural level" restrict the claim to conservation? No: the colon makes
  conservation the content of resolving *the paradox* of :112, and "structural level" is not a defined level in §7.6.
  ch19:72 shows the scoped form the book uses elsewhere.

### A.2 ch07:126
- **Sentence 1.** The A.8 proof uses the cycle decomposition only for exact averages, and the Page value enters
  through the Haar ensemble H-scramble posits. In A.8's own setting, bijections acting on configurations give S=0.
- **Sentence 2.** Page's mean is S(m,n) = Σ_{k=n+1}^{mn} 1/k − (m−1)/(2n). At m=n the deficit tends to ½. At fixed
  m it is about m/(2n): polynomial in the dimension. What is exponentially small is the deviation probability.
  Thm A.9 itself carries −½ at turnover.
- **Sentence 3** ("can … visit only product states") is understated, not overstated: every bijection does so.
- **Pressure test.** Could "runs through" merely describe the route? The contrast "rather than through the
  gravitational path integral" gives the combinatorial structure the value-supplying role, so that reading fails.
- **Introduction:** r2:189, :192, :194.

### A.3 ch07:159–161
- The named outcome is reproducible by bijective dynamics (claim A, and PROGRAMME:13's F(b,r)=(b,r)), and the nested
  trace-out holds for every map (claim E). The falsifier therefore excludes nothing.
- 161's last sentence ("sharp prediction once β is derived") is not contradicted.
- **Introduction:** the r2:182 marker; §6.5 item 4.

### A.4 ch18:130
The qualifying sentence was added 2026-10-16 in commit 8cada745. "Following from the same commitment to
geometry-first ordering" is interpretive and labelled as such in the same line.

### A.5 ch18:146
The line dates from 2026-05-14, before the §7.6 corrections. The Page curve is attributed unconditionally to the
nested formalism, which carries no recovery content.

### A.6 ch18:158
Both grammatical readings are unsupported. The line is also inconsistent with ch18:150, "inaccessible at the
emergent level".

### A.7 ch19:334
The parenthetical names the Page curve as the means of resolution, so the favourable reading ("Resolved" means
preservation, as at ch19:72) is excluded. "Conditional (H-scramble)" was accepted by BH-01's recheck as fitting the
table's register.

### A.8 GR:811
- GR:787 gives τ_B^D ~ 1e17 s. Saving GR:811 would need τ_B^D > 1e79 s at 30 M☉.
- A.5's correction, O(t/τ_B^D), is about 1e57 at t_evap.
- Substratum:256 and :280 cover only a deep sector coupled at no order, and they state that a slowly coupled sector
  is controlled only at O(t/τ_B).
- **Introduction:** r2:208 is at item F's strength. RECHECK R2-3 adds "that [GR, Thm A.7] fails within its stated
  scope t ≪ τ_B^D" to the non-claims.
- **Assumption watch:** A.7 states its error as O(τ_S/τ_B^D), while A.5(i) gives O(t/τ_B^D). Unresolved here.

### A.9 GR:869
A.8 requires H-scramble, an equidistribution hypothesis over pure states. A long cycle is ergodic on the
configuration shell and still has S=0. ch07:147, edited in the same commit 6adfff0e, already states H-scramble.
**Introduction:** r2:192.

### A.10 R12, ch18:148
The derivation assumes a constant α; ch07:137 states this explicitly. For α∝M^{−p}, the fraction is
1−2^{−(3+p)/2}. **Introduction:** r2:199–201.

## B. The Introduction

Its prose on these points is at the packages' strength; there is no INTRO-ERROR. Three OWNER markers need
adjusting:
- **r2:182:** drop "ch18:130 inherits ch07:110".
- **r2:182 and r2:191:** "contradicts" is too strong for ch07:110 and ch18:146 sentence 2; there the relation is
  that the text claims more than its support. It is exact for ch18:158, GR:811 and GR:869.
- **r2:191:** it names only ch07:126 sentence 1, but sentence 2 also needs correcting.

## C. Related findings without an R11 marker

1. **ch07:132 / FULL:2009** "the corrections are exponentially small", and **GR:611** "plus exponentially small
   corrections": both are false near turnover. This is the same family as A.2 sentence 2.
2. **ch18:150 / FULL:4970:** "inaccessible at the emergent level" is in tension with the Page-curve account (O-3).
3. **ch07:151 / FULL:2028 and GR:871:** "it can be combinatorial" paraphrases A.2 sentence 1 (O-2).
4. **GR:841–847 (Thm A.9), UNDETERMINED.** A.9 claims "direct substitution" from A.8, but A.8 is a time average at
   a fixed bipartition, while A.9 is a curve pointwise in t along one trajectory with a moving bipartition (BH-02
   C6(d), an open textual obligation). r2:205 correctly lists this step as open. It would be settled by a proof of
   typicality pointwise along trajectories, or by restating A.9 for time averages.
5. **GR A.6(iii) versus A.7:** maximally mixed hidden sectors in one, a pure total state in the other (BH-02
   assumption watch). Not assessed here.

## D. Propagation lists

After any edit, regenerate `papers/GR.tex`/`.pdf` and `book/The-Incompleteness-of-Observation-FULL.tex`/`.pdf`,
or flag them stale in the same commit.

**D.1 "Resolution" inferred from bijectivity.**
- **Primary:** ch07:110/1987, ch07:159/2036, ch07:161/2038, ch18:146/4966.
- **Paraphrases:**
  - ch07:12/1889: "Section 7.6 resolves the black hole information paradox: …" → "treats the black hole information
    paradox: …; the Page curve follows under H-scramble …".
  - ch09:108/2588: "(resolving the BH information paradox in Chapter 7 §7.6)" → "(the information-preservation half
    of Chapter 7 §7.6)".
  - ch07:118/1995, heading "The framework's resolution: nested trace-out." → "The observer's description: nested
    trace-out." (claim E applies).
- **Keep:** ch19:72/5248, ch19:30, ch18:130, ch07:157/2034, ch09:127, Main:66.
- **Re-grep for:** "resol", "never lost", "because $\varphi$ is bijective".

**D.2 Page curve attributed to combinatorics or bijectivity, or stated unconditionally.**
- **Primary:** ch07:126 s1, ch18:146, ch19:334, GR:869.
- **Paraphrases:**
  - GR:611: "from bijectivity (cycle decomposition …) and Popescu-Short-Winter typicality" → "from
    Popescu-Short-Winter typicality [29] transferred to the orbit by H-scramble, which is not established there, the
    cycle decomposition supplying exact time averages".
  - glossary:113/6735: "derives the Page curve from cycle typicality" → "obtains the Page curve under H-scramble".
  - ch07:12/1889, as in D.1.
  - ch07:151/2028 and GR:871 (O-2).
- **Keep:** ch07:116, :143, :147, :149; ch19:72; ch09:127; appendix-a:103 and :116; GR:717, :817, :841.

**D.3 Size of the PSW correction.** ch07:126 s2, ch07:132/2009, GR:611. GR:843 (Thm A.9's −½ term) is the anchor.

**D.4 Falsifier.** Only ch07:161/2038. ch18:343 is consistent.

**D.5 Decoupling of D.**
- **Primary:** GR:811. It is the only place in the corpus that states "frozen on evaporation" or "τ_evap ≪".
- **If O-1 is adopted:** GR:841, GR:611, GR:869 (last sentence), ch07:116/:126/:143/:149, ch18:146, ch19:72 and
  :334, glossary:113, ch09:127, appendix-a:116 (G11), each with its FULL mirror.

**D.6 R12, mass-independence.**
- **Primary:** ch18:148/4968.
- **Paraphrases:**
  - ch07:12/1889, "with a mass-independent Page time": add "for a mass-independent emission coefficient".
  - ch19:72/5248, "independent of mass": the same condition.
  - glossary:113/6735, "a mass-independent fraction": the same condition.
  - GR:611, "independent of mass and of the emission coefficient": add "when that coefficient is mass-independent".
- **Keep:** ch07:137/2014, ch07:139, GR:849–857, GR:863.
- **Re-grep for:** "mass-independent", "independent of mass". At 687e885b there are 5 book sites and 5 in FULL, plus
  GR:611 and GR:857.

## E. Owner decisions

- **O-1.** After GR:811 is fixed, should "D decoupled over the evaporation" become a named condition of Thm A.9
  (GR:841), GR:611 and every Page-curve status surface in the book? A.8–A.9 already rely on it, so naming it adds no
  new physical assumption, but it changes conditional labels across the corpus. The only mandatory change is GR:811
  itself.
- **O-2.** Should the H-scramble statements record BH-02 C6(a)? It says that for a definite configuration with an
  aligned split, no bijection satisfies H-scramble; satisfying it needs a superposed initial state or a non-aligned
  factorization. This affects ch07:126 s3, :149, :151 and GR:833, :869, :871.
- **O-3.** Which account the book gives: information inaccessible at the emergent level (ch18:150), or recovered
  through a conditional Page curve (ch07 §7.6, ch18:146). The proposed wording keeps both, separated as conservation
  versus recovery.
- **O-4.** Whether to state any empirical falsifier for recoverability. BH-01 and its review declined to supply one.
- **O-5.** "Horizon-factorization hypotheses" (GR:869) appears nowhere else in the corpus and is undefined.
- **O-6.** The ch19:334 cell: the two-word form "Conditional (H-scramble)", or a longer form that includes
  preservation.

All corrections belong in one separate, reviewed manuscript-consistency change, under the AGENTS rules:
- §A.14 and §A.25: FULL mirrors and paraphrases;
- §A.27 and §A.30: correct in place, no self-narration;
- §A.25 step 5: regenerate or flag the `.tex`/`.pdf` files.
