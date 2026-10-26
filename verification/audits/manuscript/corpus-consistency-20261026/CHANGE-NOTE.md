# Change note: corpus-consistency corrections (draft PR #937)

The edits are in the worktree `S/cc2/wt` (branch `fix/corpus-consistency-20261026`, head `5221b53e`, base main `687e885b`). They are uncommitted. They implement `verification/audits/manuscript/corpus-consistency-20261026/AUDIT.md` as corrected by `REVIEW.md`, within the owner's scope of 2026-10-26. Where REVIEW and AUDIT differ, REVIEW governs. Line numbers below are those at HEAD, and `[n]` gives the FULL.md mirror line.

## Changed files

- **Manuscript sources (25):**
  - papers: GR, SM, Substratum, Structure, Explainer, Methodology;
  - book: preface, ch00, ch02–ch09, ch17, ch18, ch19, glossary, appendix-a, appendix-c, bibliography, README;
  - `The-Incompleteness-of-Observation-FULL.md`.
- **Regenerated artifacts (14):** the `.tex` and `.pdf` of the six papers and of the book.

### Sparse checkout

The worktree's sparse checkout excluded every `.tex`/`.pdf`. I appended these 14 paths to the worktree-local `info/sparse-checkout` and ran `git sparse-checkout reapply`, so that the rebuilt artifacts can be committed. The original pattern file is saved at `S/cc2/edits/sparse-checkout.orig`. No other git state was touched, and no gc, prune or maintenance was run.

***

## 1. Final counts

### Koide under the Cabibbo standard

The rule applied is AGENTS' S definition ("chain walks end-to-end with all links Solid") together with appendix-a A.2. An entry whose chain has a link that the corpus itself states as open, argued or conditional in its leading-order value is C. The Cabibbo λ is C under this rule because of the emergent dressing (SM:849) and the dispersion chosen against data (SM:851).

| Entry | Corpus evidence | Result |
|---|---|---|
| Koide Q | SM:895: the amplitude A² = C₂ is "not yet derived from the dynamics — one-loop … A² ≈ 0.34, undershooting C₂ = 2 … an open computation". SM:849 calls Cabibbo's open link "complementary to (rather than the same footing as)" this one. | **C** |
| Koide θ₀ | SM:895: "the same footing as θ₀". SM:928: the magnitude normalization is "conditional only on the substrate criterion". SM:938: the residual is a possible loop-level cubic-breaking operator. | **C** |
| Wolfenstein A | **Bounded check only.** The leading-order value is the sine of a fixed lattice angle. No link in it is stated as open. SM:865 states that only the O(λ²) correction to the *measured* A is open ("the suppression is observed, not derived"). | **S** |
| λ(M_Pl) = 0 | **Bounded check only.** It rests on the composite Higgs (Theorem 11), and §7.4 states no open link. | **S** |

**Two possible open links in the remaining S entries (owner attention):**
- **Wolfenstein A:** the unprotected correction at SM:865.
- **λ(M_Pl) = 0:** the matching scale is 1/ε = M_Pl/(2√σ) with σ undetermined (GR:310, SM:1112). That scale is at M_Pl only for σ of order one.

If either is judged a leading-order open link, the SM S count falls to 1, or to 0 if both are. The coupling-sector entry 1/α₀ (appendix-a row 1, S) was not audited either.

### ⚠ The headline is two, not four

Applied consistently, the rule gives **2 unconditional parameter-free structural predictions** (Wolfenstein A and λ(M_Pl) = 0) and **5 conditional ones** (Cabibbo λ, |V_cb| = Aλ², sin²θ₁₃ = A⁴λ², Koide Q and Koide θ₀).

Every "seven parameter-free structural" site now reads "two unconditional and five conditional parameter-free structural".

### Recomputed tables

| Inventory | Before | After |
|---|---|---|
| SM §7.6 (22 observables) | 7 S + 6 L + 3 R + 2 E + 3 M + 1 P | **2 S + 5 C** + 6 L + 3 R + 2 E + 3 M + 1 P |
| SM:1300 structural-or-near-structural total | 7 + 6 = 13 | 2 S + 5 C + 6 L = 13 |
| appendix-a A.4.1 | 24 rows: 8 S + 3 C + 8 L + 1 M + 2 R + 2 E | **23 rows: 3 S + 7 C** + 8 L + 1 M + 2 R + 2 E (row 24, the Bekenstein–Hawking entropy, removed) |
| appendix-a A.4.2 (gravitational) | 13: 2 S + 9 C + 2 L | **10: 8 C + 2 L** (G4, G7 and G14 retired; IDs not reused, successors not renumbered, gaps not annotated) |
| appendix-a A.4.3 (neutrino) | 7: 2 S + 5 L | 7: **1 S + 1 C** + 5 L (N2 = sin²θ₁₃) |
| appendix-a A.4.4 (biology) | 12 S + 2 C | unchanged |
| appendix-a A.5 forward table | F1–F13 | F5 retired; F1–F4 and F6–F13 remain |
| ch06 §6.8 table (24 entries) | Class S 8, C 1 | Class S 3 (1/α₀, A, λ(M_Pl)), C 6 (A·B, λ, \|V_cb\|, Q, θ₀, sin²θ₁₃); Category A–E unchanged (evidence independence, not derivation class) |
| ch07 §7.10 table | 14 | **12** (S_BH and "CC dissolution (descriptive)" rows moved into a consistency-relations sentence); ch07:323 "fourteen" → "twelve" |
| ch04 Class B | 14: 4 B-S + 6 B-L + 2 B-M + 2 B-R | **13: 1 B-S + 2 B-C + 6 B-L + 2 B-M + 2 B-R** |
| GR:358, mutually independent consequences | 7 | **5** comparisons with data |
| GR §7.4 table | 10 rows | 8 rows (BH coefficient and CC rows moved into a consistency-relations sentence) |

**Notes on the table:**
- **ch04 Class B:**
  - B-C is a new sub-class, holding Cabibbo and Koide θ₀.
  - m_d/m_s moves from B-S to B-L. It was listed as B-S although SM classifies it L (via GST).
  - The 1/4 is now a consistency relation and is not counted.
- **GR:358:**
  - Item (1) is a normalization (2.6).
  - Items (2)–(3) are one consistency relation with no direct test (owner item 2).
  - The five are items (5), (6), (7), (9) and (11).

### Consistency relations: kept as stated results, outside the counts

Each is stated where its count used to be:
- **The Bekenstein–Hawking 1/4** (G4, A.4.1 row 24): the ratio 2π/8π that the calibration matches, conditional on H-slope, with no direct test.
- **The vacuum-energy level distinction / compression ratio** (G7): descriptive. ρ_QFT/ρ_crit ~ S_dS is a dimensional identity up to a factor between 1/(96π²) and 8/3.
- **The boundary-density normalization** ρ_s = ρ_crit (G14).

The statements sit in:
- appendix-a's new "Consistency relations" paragraph after A.4.2;
- a sentence after the GR §7.4 table;
- a sentence after the ch07 §7.10 table.

**⚠ Judgement call: G7.** REVIEW confirms the AUDIT classes for G7 ("descriptive relation"; its formula, the compression ratio, is "Consistency (dimensional identity)", items 2.7 and 2.10) and for G14 ("normalization identity"). I read both as consistency identities under the owner's item 2. If G7 is kept, the gravitational count is 11 (1 S + 8 C + 2 L).

G9 (partly definitional) is kept, because the dark budget is deferred.

***

## 2. Edits, site by site

### Horizon entropy and the 1/4 (AUDIT §1, REVIEW 1.x)

| Site | Original (short) | New (short) | Item |
|---|---|---|---|
| GR:12 | "obtains … including the 1/4 coefficient by direct boundary-mode counting" | "recovers …: with the calibration the count σA/ε² equals A/(4l_p²) for every ε, σ; the 1/4 the ratio 2π/8π of KMS period to first-law prefactor" | 1.1 |
| GR:162; ch07:63 [1940]; Explainer:477, :1043 | "predictive content … Any alternative ħ(ε) would fail at least one of these checks" | "enters three later results … The three relations share the calibration; they are consequences of it, not independent checks of it" | 1.4 (REVIEW: rewrite) |
| GR:164; ch07:65 [1942] | Gibbons–Hawking "recovered as a prediction, not used as an input" | "enters as the KMS temperature of Step 4; the calibration relates the ħ in it to ε and σ through ħ = c³ε²/(4Gσ)" | 1.5 (REVIEW wording) |
| GR:320 | "historically introduced as a proportionality constant — is here fixed" | "introduced by Bekenstein (1973) with a coefficient he could estimate only heuristically, and fixed at 1/4 by the Hawking temperature and the first law (Hawking 1975) — is here recovered" | 1.7 (REVIEW) |
| GR:322; ch07:104 [1981] | "a derived structural constant" | "the ratio of the two normalizations that the calibration matches, conditional on H-slope and the horizon and frame conditions" | 1.3 |
| GR:707 | "follows by direct mode counting … a structural constant rather than an empirical fit" | "is recovered: with the calibration the mode count equals A/(4l_p²) … not an empirical fit" | 1.1, 1.3 |
| GR §7.4 table | BH coefficient row "derived (2π/8π) … consistent" | row moved to a consistency-relations sentence | owner 2 |
| GR:358 (2)–(3), last sentence | "one algebraic fact"; quantum-first "treat ħ and the 1/4 factor as unexplained inputs" | "one consistency relation with no direct test … agrees with the Hawking-temperature normalization rather than testing it"; "treat ħ as an unexplained input" | owner 2, 1.2 |
| preface:7 [78] | "1/4 … becomes a derivation"; "(the derived 1/4 …)" | "recovered as a consistency relation of the horizon calibration (conditional on the conditions of Chapter 7)"; "(the 1/4 …)" | 1.2 (REVIEW wording) |
| ch00:21 [257] | "becomes a derivation rather than a postulate" | "recovered as a consistency relation between the classical and emergent horizon temperatures, conditional …; it has no direct test" | 1.2 (AUDIT wording) |
| ch00:81 [317] | "obtains the 1/4 from mode counting …; in the standard account the factor is a postulate" | "recovers the 1/4, which the standard account fixes from the Hawking temperature and the first law, as the ratio 2π/8π of its horizon calibration" | 1.2 (REVIEW wording) |
| ch00:89 [325] | "the Bekenstein-Hawking 1/4 factor as a derivation" | "… as a consistency relation under the horizon calibration" | 1.2, item 13 (1/4 clause) |
| ch02:112 [755]; ch02:192 [835] | "follows as a consequence of the same mode-counting analysis" / "follows from direct mode counting" | "the boundary-mode count reproduces …, the 1/4 being the ratio 2π/8π that the calibration matches" | 1.1 |
| ch03:42 [918] | 1/4 listed among Level-D predictions | "… the Bekenstein-Hawking 1/4 factor as a consistency relation" | owner 2 |
| ch03:118 [994] | "the Bekenstein-Hawking 1/4 factor from boundary mode counting" in the class-specific list | clause removed (GR:30 makes the 1/4 universality-class level, and it is a consistency relation) | 1.1 (addition) |
| ch04:44 [1163] | 1/4 as the C-class example | Cabibbo and Koide as the C examples; the 1/4 stated as a conditional consistency relation, not counted | owner 2 |
| ch04:134, :140 [1253, 1259] | BH coefficient "B-L"; "has no direct test" in the B count | removed from B-L; stated after the split as a consistency relation, not counted | owner 2 |
| ch06:14 [1538]; ch06:348 [1872] | 1/4 "Class B-L"; "from boundary-mode counting" | "a consistency relation, conditional on H-slope"; "as the ratio matched by the horizon calibration … (a consistency relation …)" | owner 2, 1.1 |
| ch07:90 [1967] | "historically unexplained constant … treat the 1/4 as either fitted …" | "Bekenstein (1973) … heuristically; Hawking (1975) fixed the 1/4 … The framework reproduces the same ratio from its horizon calibration" | 1.7 |
| ch07 table [2173, 2175] | S_BH row; CC-dissolution row | rows moved to a consistency-relations sentence after the table | owner 2 |
| ch09:8 [2488]; ch09:88 [2568]; ch09:333 [2813] | "conditional and has no direct test"; "follows"; "is derived but has no direct test" | "a consistency relation, conditional and without a direct test"; "is recovered"; "a consistency relation of the horizon calibration with no direct test" | 1.1, 1.3 |
| ch18:160 [4980] | the 1/4, ħ, RVM, MOND and echoes among "predictions … neither QM nor GR alone makes" | REVIEW's sentence: "conditional and consistency relations — … — rather than predictions independent of QM and GR; its forward exposure is listed in Appendix A.5" | 1.6 (REVIEW wording) |
| glossary:17 [6639] | "conventionally treated as a postulate … The framework *derives* …" | "follows from the Hawking temperature and the first law. In the framework it is the ratio 2π/8π fixed by the horizon calibration …" | 1.2 (AUDIT wording) |
| appendix-a:93 (row 24), :110 (G4), :99, :123, :217 [5646, 5663, 5652, 5676, 5770] | row 24 and G4; "(G4) is conditional"; "(entry 24 / G4)" | rows removed; the consistency-relations paragraph; ":217 … is a consistency relation … (A.4.2)" | owner 2, 1.8 |
| appendix-c:275 [6543] | "is derived but has no direct empirical test" | "is a consistency relation of the horizon calibration …" | 1.3 |
| Substratum:324 | "obtains … including the 1/4 coefficient by direct mode counting" | "recovers …, the mode count reproducing it once the calibration fixes ε/√σ = 2l_p and the 1/4 being the ratio 2π/8π …" | 1.1 |
| Structure:56, :142, :340, :450, :452 | 1/4 among the "22 SM predictions"; "derives the A/4"; "by mode counting" | 1/4 as a consistency relation; "recovers … the ratio of the KMS and first-law normalizations that the calibration matches" | 1.1, 3.6 |
| Explainer:521, :523, :697, :699 | "Bekenstein and Hawking introduced … in 1973"; "a mystery for 50 years"; "which the paper derives"; "treats … the 1/4 factor as unexplained inputs" | Bekenstein 1973 / Hawking 1975 history; "a consistency relation with Hawking's result rather than an independent test"; "recovers under its horizon calibration"; "treats ħ as an unexplained input" | 1.7, 1.2 |
| Methodology:21 | "derives the Bekenstein–Hawking entropy coefficient" | "recovers … as a consistency relation of its horizon calibration" | 1.1 (addition: missed site) |
| bibliography.md :118, :138 [6902, 6922] | — | Bekenstein (1973) and Hawking (1975) entries added (cited in ch07:90) | 1.7 |

### Cosmological constant (AUDIT §2, REVIEW 2.x)

| Site | Original (short) | New (short) | Item |
|---|---|---|---|
| GR:24 | "is dissolved by …; … the dynamical form of the dissolution is conditional" | "is addressed by …; the descriptive distinction is established, and the dissolution is conditional on the G3 coupling theorem" | 2.3 |
| GR:32 | "§6 dissolves the CC problem" | "§6 gives the conditional dissolution of …" | REVIEW §9 (missed) |
| GR:338 | "ρ ~ H²/G … — precisely observed" | "the Friedmann scale at which any O(1) component of a flat universe sits; its value is an input (§6.2)" | 2.6 |
| GR:356 (last sentence) | "artifact … never enters the stress-energy tensor; no decoupling mechanism is needed" | "belongs to the emergent description; that it does not enter … is the geometry-first proposal …, and establishing it is the coupling step that G3 leaves open" | 2.2 |
| GR:358 (item 1) | "(1) the CC dissolution — sits at ρ ~ H²/G … without fine-tuning" | "(1) the vacuum-energy normalization — of the Friedmann scale …, value set by initial conditions …, absence of a 122-digit cancellation conditional on the coupling step" | 2.6 |
| GR:360; ch07:201 [2078] | "eliminates the 122-digit cancellation entirely" | "Conditional on the coupling step, the framework removes the need for the 122-digit cancellation" | 2.5 |
| GR:362 | "What the framework excludes is the zero-point sum as a gravitational source" | "What the geometry-first proposal excludes, conditional on the coupling step, is …" | 2.1 (addition: same inference in §6.2) |
| GR:366 | "= S_dS … now identified as …"; "the value the framework expects" | "~ S_dS — a dimensional identity …, up to a convention-dependent factor between 1/(96π²) and 8/3 …; on that reading, and conditional on the coupling step …"; "a normalization, not a prediction" | 2.6, 2.7 |
| GR:368; ch07:199 [2076] | "— a triangulation that strengthens the empirical case for both programs" | deleted | 2.8 |
| GR:583 | "it is a theorem of the reconstruction … attributes physical content to a gauge degree of freedom" | "…present in no visible transition statistics … The embedded observer's quantum data therefore contain no fact about the absolute zero-point offset. Whether the offset sources curvature is not settled by this invariance; it is the coupling question that §6.2 leaves open at Level G3." | 2.1 (AUDIT wording) |
| GR:585 | "The dissolution applies to each …" | "On the geometry-first proposal of §6.2, conditional on the open coupling step, …" + "How the energy released in the electroweak and QCD transitions couples to gravity is not fixed by the relative/absolute distinction and requires the same open coupling step." | 2.1, 2.9 |
| GR:587 | heading "Why QCD binding energy gravitates but the quantum vacuum does not"; "therefore does not source curvature" | heading "QCD binding energy and the quantum vacuum"; "therefore, on the geometry-first proposal …, conditional on its open coupling step, does not source curvature" | 2.1 |
| GR:707 | "dissolved at the descriptive-levels register … not a failure of cancellation" | "the descriptive distinction established and the dissolution conditional on the coupling step …: on that reading …" | 2.3 |
| GR §7.4 table | "Cosmological constant \| ρ ~ H²/G \| observed value \| no discrepancy" | moved to the consistency-relations sentence as a normalization whose value is an input | 2.6, owner 2 |
| preface:7 [78]; ch00:21 [257]; ch00:89 [325] | "becomes a calculable compression ratio"; "a calculable ratio rather than a fine-tuning failure"; "as an information compression ratio … all follow" | "read as the compression ratio …, conditional on an open coupling step"; "(conditional on an open coupling step)" | REVIEW §9 (missed) |
| ch02:192 [835]; ch02:228 [871] | "The cosmological constant problem dissolves:"; "the dissolution of the CC problem" | "receives a conditional treatment: …; the dissolution is conditional on the covariant coupling step (Chapter 7)"; "the conditional dissolution" | 2.3 |
| ch06:348 [1872] | "the dissolution … at the level of two incommensurable descriptive levels" | + "conditional on the covariant coupling step" | 2.3 |
| ch07:167 [2044] | "The framework dissolves the problem rather than solving it." | "proposes a dissolution rather than a solution … The descriptive distinction is established; that the zero-point sum does not source curvature is the covariant coupling step that [GR §6.2] leaves open, so the dissolution is conditional on it." | 2.4 (AUDIT wording) |
| ch07:171 [2048] | "what gravity couples to"; "— precisely what is observed" | "what on the proposal gravity couples to"; "the Friedmann scale …; its value is an input" | 2.4, 2.6 |
| ch07:175, :177 [2052, 2054] | "The classical substratum's vacuum energy is the gravitating object"; "The stress-energy that sources gravity is the classical …" | "On this proposal …"; "The proposal is that …; establishing it is the coupling step left open" | 2.4 |
| ch07:191, :193, :195 [2068, 2070, 2072] | "= S_dS"; "up to factors of order one"; "the framework's structural quantity …"; "independent reason to expect" | dimensional identity "up to a convention-dependent factor between 1/(96π²) and 8/3"; "on the framework's reading"; "the observed density … is an input" | 2.7, 2.6 |
| ch07:207, :258 [2084, 2135] | "Section 7.7 established that … does not gravitate"; "(does not gravitate)" | "proposed … — the descriptive distinction established, the gravitational decoupling conditional …"; "(on the proposal of Section 7.7, does not gravitate)" | REVIEW §9 (missed) |
| ch09:90 [2570] | "gravity couples to the classical substratum … that does not gravitate" | the coupling and non-gravitation made explicitly conditional on [GR §6.2] | REVIEW §9 (missed) |
| ch09:259 [2739] | "dissolves the commensurability …; … so nothing needs quenching because nothing physical was there" | "proposes to dissolve …, conditional on the coupling step …"; "invisible to every quantum statistic, and on the geometry-first proposal nothing needs quenching; whether the offset sources curvature is the coupling step that [GR §6.2] leaves open" | 2.1 (addition: the GR:583 inference in the book) |
| ch18:140, :142, :144 [4960, 4962, 4964] | "each dissolving when …"; "gravity couples to the classical substratum"; "a derivable quantity"; "no cancellation required" | "conditional on the covariant rung G3"; "on the geometry-first proposal …, a coupling step open at G3"; dimensional identity …; "not a fine-tuning failure"; "… if the coupling step holds" | 2.3, 2.7 |
| ch19:38 [5214] | "Dissolved at the descriptive level …; … artifact … and does not gravitate" | "Descriptive distinction established; the dissolution is conditional …"; "… up to a convention-dependent factor …"; REVIEW's sentence "that it does not gravitate is the coupling step that [GR §6.2] leaves open" | 2.3 (REVIEW) |
| ch19:330 [5506] | "Dissolved (10¹²² = S_dS)" | "Descriptive distinction established; gravitational form conditional (G3)" | 2.7 |
| glossary:51 [6673] | "The framework *dissolves* this problem" | "proposes to *dissolve* …; the descriptive distinction is established; the dissolution is conditional on the open coupling step" | 2.3 (addition) |
| appendix-c:273 [6541] | "cosmological constant magnitude" among the retrodicted | removed (with REVIEW's rewrite of the paragraph) | 3.6 INC clause |
| Substratum:324 | "dissolves the cosmological constant problem" | "addresses …, the descriptive distinction established and the dissolution conditional on the open coupling step" | REVIEW §9 (missed) |
| SM:132 | "that dissolves the cosmological-constant problem" | "that underlies the conditional treatment of the cosmological-constant problem ([GR §6.2])" | REVIEW §9 (missed) |
| SM:1534; Structure:975 | "is dissolved as …" / "dissolves the 10¹²² discrepancy ([GR §6])" | conditional on the coupling step that [GR §6.2] leaves open | 2.3 (addition) |
| Explainer:22, :533, :547, :549 | "strongest piece of existing evidence"; "dissolves"; "not a discrepancy. It equals S_dS"; "sits exactly at … the value the framework expects … nothing to cancel" | "On the framework's reading … a sign …; whether gravity ignores … is an open step"; "conditional treatment"; "Up to a convention-dependent factor it equals S_dS … as it does for any theory with a Planck cutoff …"; "a normalization, not a prediction … If the open coupling step holds …" | REVIEW §9, 2.3, 2.6, 2.7 |

### Counts, the SM classification and JUNO (AUDIT §3–§4, REVIEW 3.x, 4)

| Site | Original (short) | New (short) | Item |
|---|---|---|---|
| SM:841; ch06:118 [1642] | "Observed λ = 0.22500 ± 0.00067" | "+ (global fit with unitarity imposed)" | 4 (NQ, PDG source) |
| SM:849 | "established at the structural level rather than merely hypothesized" | "the unit prefactor is established …, the emergent dressing is open, and the prediction is conditional on it (class **C**, §7.6)" | 4 (AUDIT wording) |
| SM:895 | "… weaker than a full derivation and stronger than a fit." | + "; both Koide entries are accordingly conditional structural predictions (class **C**, §7.6)" | REVIEW §4 (Koide) |
| SM:1010, :1341; ch06:267 [1791]; ch08:138 [2341] | sin²θ₁₃ "Layer 1 unconditional structural" | "Layer 1 structural, independent of Cond 2, conditional only through λ" | 4 (inheritor) |
| SM:1255, :1262, :1265, :1267–1268, :1276 | legend S/L/…; λ, \|V_cb\|, Q, θ₀, sin²θ₁₃ marked **S** | legend adds **C**; the five rows marked **C** | 4, REVIEW §4 |
| SM:1296; appendix-a:139 [5692] | λ² scale "unconditional structural" / "holds unconditionally" | "the λ² scale conditional on the emergent dressing" | 4 (inheritor) |
| SM:1298, :1300 | "**7 are unconditional parameter-free structural**"; "The 22-observable table contains no C-class entries"; "7 structural + 6 layered = 13" | "**2 …** (A, λ(M_Pl)) and **5 are conditional structural predictions** (…)"; sentence removed; "2 structural + 5 conditional structural + 6 layered = 13" | owner 1 |
| SM:1310 | "the **S** set contains two … families" | "the **S** and **C** entries contain …; until that closure both are classified **C**" | owner 1 |
| SM:1426 | C-class absent; "the only candidate for C in v1.9.5" | **C** defined; version narration removed | owner 1, §A.33 |
| SM:1456 | "the twenty-two structural predictions of §7" | "the twenty-two classified observables of §7" | 3.6 |
| appendix-a:8, :28, :30, :74, :76, :79–80, :82, :95, :99, :132, :139, :231 [5561 …] | 13 gravitational; S examples λ, Q, sin²θ₁₃; row 5 "S … 0.04%"; rows 7, 10, 11, 13 S; "8 S + 3 C … Total: 24 … *seven*"; N2 S; "2 S + 5 L"; :231 counts | ten; S examples A, λ(M_Pl); C examples add Cabibbo and Koide; row 5 "C … 0.04% (global fit; retrodiction)"; rows 7, 10, 11, 13 C; "3 S + 7 C … Total: 23 … *two* unconditional and *five* conditional"; N2 C; "1 S + 1 C + 5 L"; :231 recounted | owner 1, owner 2, 3.1 |
| appendix-a:217, :231 [5770, 5784]; appendix-c:275 [6543] | "the anisotropy amplitude" / "the rotational-anisotropy amplitude" in the pre-registered set | removed | 3.4 |
| preface:7 [78]; appendix-c:275 [6543] | JUNO "from a prediction made before the measurement"; "a *pre-registered* prediction made before the JUNO measurement" | "by a parameter-free retrodiction — the derivation postdates the measurement — and JUNO's design-lifetime precision is a pre-registered forward test"; "a *parameter-free* retrodiction …" | 3.5 |
| appendix-c:279, :347 [6547, 6615] | "predictions that have been tested (and confirmed)" | "claims that have been compared with data …"; "retrodictions or consistencies with existing data" | 3.5 (OVR) |
| appendix-c:8, :273 [6276, 6541] | "seven parameter-free structural"; "Thirteen …"; "explained as *structural consequences* … not just fit to data" | counts recomputed; REVIEW's rewrite of :273 (couplings "among the fitted"; gauge group and generation count no longer listed among the 22; last sentence removed) | 3.6 (REVIEW) |
| ch00:77 [313] | "quantitative and parameter-free"; "Koide … exactly 2/9" (observed 0.666661); couplings "from one universal … coupling plus RG running"; "with no parameters fit to the retrodicted quantities" | "quantitative"; "exactly 2/3"; "+ a threshold fixed by one of the couplings and two threshold parameters matched to the other two"; classified 2 + 5 + remainder, "no parameters fit … in the structural and layered classes" | 3.6 (+ the numeric 2/9 error) |
| ch00:21, :89, :97 [257, 325, 333]; ch02:228; ch03:42; ch04:202; ch05:13, :196; ch07:8; ch08:272; ch09:8, :231, :325; ch17:234; ch19:362; Substratum:198, :228; Structure:197, :944; Explainer:679, :858, :862 | "seven parameter-free structural", "twenty-two parameter-free/zero-parameter", "thirteen gravitational", "each at ≲ 1σ", "twenty-two quantitative predictions …" | "two unconditional and five conditional parameter-free structural"; "twenty-two classified …"; "ten gravitational"; "the measured comparisons each at ≲ 1σ"; "the remainder layered, chained or fitted, the gauge couplings among the fitted" | owner 1, 3.6 |
| ch04:42, :130, :132, :134, :140 [1161 …] | Cabibbo and Koide "S-class" examples; B-S {λ, A, m_d/m_s, θ₀}; "four B-S … fourteen" | S examples A and λ(M_Pl); new B-C {λ, θ₀}; m_d/m_s B-L; "one B-S, two B-C … thirteen"; "+ three matched coupling parameters" | owner 1, 3.6 |
| ch06:14, :179, :297, :299, :302–303, :312, :332 [1538 …] | Cabibbo and Koide "Class B-S"; Koide "currently … B-S … former open question now settled"; table **S** ×5; "the derivational Class C of the A·B row" | "B-C" with the open link named; history voice removed; table **C** ×5; "the derivational Class C" | owner 1, §A.33 |
| ch09:73 [2553] | "0.04%–1.01σ across 22 predictions" | "for the measured comparisons (gauge couplings matched by construction)" | REVIEW 3.6 |
| ch18:349 [5169] | "Twenty-two parameter-free SM predictions match observation. Thirteen … Seven …"; echoes | REVIEW's restatement, recounted to 2 + 5 and ten entries; echoes removed | 3.1 (REVIEW) |
| ch19:28 [5204]; GR:358; Explainer:699 | "seven independent consistency checks and no fitted parameters"; "seven … mutually independent"; "ten consequences matching observation, seven …" | REVIEW's "consistency relations collected in [GR §6.2] — several conditional on G3, one … three matched parameters, one … imported factor"; "five … mutually independent comparisons with data" | 3.3 (REVIEW), 2.6 |
| ch19:362 [5538] | "record of resolved problems … preregistered structural predictions … is met across multiple sectors"; "seven neutrino-sector predictions" | "The record is retrodictive: … the pre-registered forward set (Appendix A.6) awaits its data"; "entries" | 3.2 |
| Structure:56 | "Cabibbo … at 0.05σ" | "0.12σ" (SM:841); λ and Koide "both conditional structural" | 3.6 |
| ch07:323 [2200] | "the fourteen entries in this chapter's table" | "the twelve entries" | owner 2 |

### Echoes (AUDIT §5, REVIEW §6)

| Site | Original (short) | New (short) | Item |
|---|---|---|---|
| GR:603 | "The framework therefore predicts … no OI-specific echo …" + "four-event … stack … −0.45, p = 0.66 … 5.9σ" | "On this argument no OI-specific echo, comb or wall-reflection feature is expected: … ringdown morphology, and no echo amplitude is derived." The unretained numerical clause is removed (owner 3, §A.42). | 5 |
| ch18 §18.6 :164–182 [4984–5002] | forward echo prediction, Δt formula, ε/r₊ amplitude, falsification clause | the published searches (citations kept) + REVIEW's core sentence + GR §8.4's partition argument + a short conceptual-content paragraph | 5 (REVIEW wording) |
| ch18:18 [4838] | "develops gravitational wave echoes as a forward prediction … most directly observable signature … accessible to current LIGO/Virgo/KAGRA" | "takes up gravitational wave echoes: [GR §8.4] argues …; no echo amplitude is derived" | REVIEW §6 (missed) |
| ch18:28, :160, :339, :349 [4848, 4980, 5159, 5169] | echoes listed as testable / a forward prediction | removed | 5 |
| appendix-a:183 (F5), :208 [5736, 5761] | F5 row; F5 falsification bullet | removed; ID F5 not reused, successors not renumbered, gap not annotated | 5 |
| ch00:101 [337]; book/README:90; appendix-c:277, :279, :303, :347 [6545 …] | "gravitational wave echoes at Δt = …" | "the absence of an OI-specific gravitational-wave echo for external observers" / removed from the forward lists | 5 |

### Outside the five: items affecting the Introduction (owner 5)

| Site | Original (short) | New (short) | Item |
|---|---|---|---|
| GR:567 | "the mixing hypothesis holds … which is (C4)'s realization — so the equivalence applies in our universe" | "the horizon complement is a generic chaotic hidden sector, so the mixing hypothesis behind (C2) is motivated there; (C4) is a named realization condition not discharged at the cosmological cut (§2.2), and the application of the equivalence to our universe is conditional on it" | 6 |
| GR:711 | "[Main] establishes the equivalence …"; "establishes that … three faces …, with QM emerging as the unique self-consistent description" | "establishes a finite-horizon correspondence between the recordable laws of an embedded observer and fixed-basis quantum laws"; "proposes that … descend from one finite deterministic construction, with the covariant field equations (G3) and the selection of full operational quantum mechanics open" | 7 |

***

## 3. Departures from REVIEW or AUDIT wording, with reasons

1. **appendix-a:74.** AUDIT reads "postdiction"; I wrote "retrodiction", the appendix's own vocabulary (R class, A.6).
2. **GR:320 and Explainer:521 cite in prose.**
   - They read "Bekenstein (1973)" and "(Hawking 1975)" without numbered references, because adding a numbered entry to GR's reference list would collide with #936, which appends one there.
   - The book gained bibliography entries for both.
   - **REVIEW 1.7's request stands: the owner should confirm the Bekenstein-1973 history first-hand.** I wrote it from memory: Bekenstein proposed ln2/8π heuristically; Hawking's "Particle creation by black holes" appeared in Commun. Math. Phys. 43, 199 (1975).
3. **ch18:349 and appendix-c:273.**
   - REVIEW's gravitational clause ("conditional relations, identities and estimates … thirteen") is adapted to the new inventory: "ten … conditional relations and estimates". The identities left the count under owner item 2.
   - REVIEW's placeholder "[corrected count]" is resolved as "two unconditional and five conditional".
4. **ch19:28.** REVIEW's replacement is used, keeping the quantum-sector clause "— the quantum representation under the translation hypothesis (T) ([Main §3.4]) —" attached to the quantum sector only. REVIEW's objection was to attributing the seven gravitational relations to (T) and to G1/G2.
5. **ch19:38.** REVIEW's sentence is used.
   - The lead "Dissolved at the descriptive level; the dynamical form is conditional …" also becomes "Descriptive distinction established; the dissolution is conditional …". Otherwise the cell would assert and then qualify, the defect 2.3 corrects at GR:24.
   - The 10¹²² = S_dS clause gains "up to a convention-dependent factor" (2.7).
6. **GR:603.** REVIEW's ch18 sentence is adapted to GR's own paragraph, which already contains the partition argument: "On this argument no OI-specific echo … is expected …; no echo amplitude is derived".
7. **ch00:89.**
   - The 1/4 and CC clauses are corrected.
   - "all follow from the single statement … and four conditions" becomes AUDIT item 13's "the four conditions on the partition, and the named hypotheses of each chapter". Without that, the sentence would assert unconditional consequence of the newly conditional clauses.
   - The a₀ "parameter-free prediction" clause is left (deferred, item 13).
8. **ch07:63, GR:162 and Explainer:477/:1043.** These use REVIEW 1.4's preferred rewrite, AUDIT's second option, rather than deletion. The bold heading "The predictive content of the gap equation" / "Predictive content" becomes "The consequences of the gap equation" / "What the gap equation fixes".
9. **Additions beyond the AUDIT and REVIEW site lists.** These apply the same verdicts at further sites found by re-grep:
   - GR:362, GR:587 (heading), SM:1534, Structure:975, glossary:51, ch09:259: CC conditionality. ch09:259 repeated GR:583's INCORRECT inference ("nothing physical was there").
   - Methodology:21: 1/4.
   - ch03:118: 1/4 removed from the class-specific list.
   - SM:1296, appendix-a:139, SM:1010/:1341, ch06:267, ch08:138: λ inheritance.
   - ch00:77: the Koide "exactly 2/9" against an observed 0.666661 is a numeric error; the value is Q = 2/3. The couplings' fitted thresholds are also named there.
   - ch04: m_d/m_s B-S → B-L, matching SM's L.
   - Removal of revision-history voice (§A.33) inside sentences I was rewriting anyway: ch06:179 "now complete / currently / former … now settled"; SM:1426 "v1.9.5".

***

## 4. Deferred (outside the five; owner 5)

**Named in the owner's deferral:**
- **Arrow of time** (AUDIT items 9 and 10):
  - Substratum:56, :350 (§A.33 history voice), :356 "No additional axiom is needed";
  - Main:726, Main:740 (the corollary title "past-hypothesis replacement" and the ALL-CAPS "SUFFICIENTLY FAST-MIXING");
  - Complexity:204; Explainer:930; ch02:196 [839].
- **Measurement "dissolves"** (item 8): ch19:333 [5509], ch19:64 [5240], Main:666.
- **Dark budget** (items 11 and 12):
  - ch19:339 [5515], ch19:116 [5292], :118 [5294]; GR:709 "explains ~95%";
  - G9 remains in the gravitational count;
  - the GR §7.4 "Dark sector fraction" row.
- **a₀** (item 13, non-1/4 clauses):
  - ch00:89 "parameter-free prediction";
  - also Explainer:671 and glossary:103 "with no fitted parameters" while the factor 1/6 is imported.
- **ch19:336** "Hierarchy problem | Dissolved (lattice is UV)".

**Noticed, not changed (outside scope, or not demonstrably within the five):**
- Medicine:554 "the same mechanism that dissolves the hierarchy and cosmological-constant naturalness problems".
- Koide numeric inconsistencies across the corpus:
  - Q quoted as 0.02% (ch00:77, appendix-a:79), against < 0.01% (SM table) and 0.001% (ch06 table);
  - "Koide relation 2/9" labels where the angle is meant (ch03:42, :118, ch05:196);
  - ch06:205 "Q = 2/3 from C₂(T₁)/d²".
- SM abstract (SM:14) "Wolfenstein A … to 0.23σ" against 0.8σ in the SM table.
- ch09:259 cites "Chapter 7 §7.6" for the vacuum-energy levels; the CC section is §7.7.
- Borderline "twenty-two quantitative predictions" phrasing that REVIEW marks not required: Substratum:38, :322 (lists the fitted couplings among "predictions follow"), :368, :404; ch02:218; ch03:10, :18, :122, :212, :240 (also lists the 1/4 among the "Level G3 × Level D predictions"); ch06:12; Structure:380; readers-guide:27.
- ch02:120 "The Bekenstein-Hawking 1/4 factor is not a postulate; …" was kept per AUDIT's keep list. Its "not a postulate" contrast is milder than ch00:81's, but the owner may want it aligned with 1.2.
- Structure:438 "already produces the A/4".
- GR §7.4 ħ row "structural" (ħ is a calibration, GR:310).
- ch19 "The earlier framing of this as …" (pre-existing history voice).
- The audit record's own hygiene items listed in REVIEW §5 (mirror.sh path, AUDIT.md:6/:9, digest, #936 head, "nothing … committed"). These are not manuscript edits and were not touched.

***

## 5. Lines owned by PR #936: exact follow-ups after the merge of main `17b830bc`

#936 landed as `17b830bc`. I recomputed its changed lines with `git diff -U0 687e885b 17b830bc`. That diff differs from the earlier `b61cbaa9`: it also changes ch07:147, GR:817, GR:825, GR:871 and others. **None of my edits touches a line #936 changed: overlap 0.**

To find follow-ups, I scanned every line #936 changed, as it reads at `17b830bc`, for the in-scope phrase families: dissolution, the 1/4 "derived", mode counting, echo, counts, retired IDs, "does not gravitate". The mode-count hits in the Page-curve passages are correct as written: ch07:147, :157, :161; ch19:72; GR:611, :805, :877. ch18:150 ("the shared structural feature with the cosmological constant dissolution") names the section and needs nothing. That leaves four sites.

Each "Current text" quote below is exact at `17b830bc` and unique in its file; it also occurs once in FULL.md. Line numbers are given at `17b830bc`, then after the merge with my edits; FULL shifts by +2 because of the new ch04 B-C paragraph. Apply each edit to the chapter and to FULL.md identically.

| # | Site at 17b830bc → after merge [FULL at 17b830bc → after merge] | Current text (exact) | Proposed text | Item |
|---|---|---|---|---|
| F1 | book/README.md:64 → 64 (not mirrored) | `the Bekenstein–Hawking entropy with the $1/4$ factor derived (GW250114 confirms the classical area theorem), dark-sector phenomenology including $a_0 = cH/6$, the dissolution of the $10^{122}$ cosmological constant discrepancy,` | `the Bekenstein–Hawking entropy with the $1/4$ factor recovered as a consistency relation of the horizon calibration (GW250114 confirms the classical area theorem), dark-sector phenomenology including $a_0 = cH/6$, the conditional dissolution of the $10^{122}$ cosmological constant discrepancy (descriptive distinction established, gravitational decoupling conditional on the open coupling step),` | 1.1/1.3, 2.3 |
| F2a | book/ch07-gravity.md:12 → 12 [1889 → 1891] | `Section 7.5 derives the Bekenstein-Hawking entropy $S = A/(4 l_p^2)$ by direct boundary-mode counting, with the $1/4$ coefficient emerging as the ratio of the Euclidean KMS period to the Jacobson prefactor under the same conditions;` | `Section 7.5 recovers the Bekenstein-Hawking entropy $S = A/(4 l_p^2)$: with the calibration the boundary-mode count reproduces it, the $1/4$ coefficient being the ratio of the Euclidean KMS period to the Jacobson prefactor that the calibration matches, under the same conditions;` | 1.1 |
| F2b | same line | `Section 7.7 dissolves the cosmological constant problem by identifying the emergent quantum vacuum energy and the effective cosmological constant as properties of logically distinct descriptions rather than commensurable quantities whose $10^{122}$ ratio requires cancellation.` | `Section 7.7 proposes a dissolution of the cosmological constant problem by identifying the emergent quantum vacuum energy and the effective cosmological constant as properties of logically distinct descriptions rather than commensurable quantities whose $10^{122}$ ratio requires cancellation; the descriptive distinction is established, and the dissolution is conditional on the covariant coupling step that [GR §6.2] leaves open.` | 2.3 (AUDIT §15) |
| F3 | book/ch07-gravity.md:110 → 110 [1987 → 1989] | `the same mechanism that produced the cosmological constant dissolution in §7.7 below` | `the same mechanism that underlies the conditional cosmological constant dissolution in §7.7 below` | 2.3 |
| F4 | book/ch18-beyond.md:146 → 146 [4966 → 4968] | `the same mechanism that produced the cosmological constant dissolution. The framework` | `the same mechanism that underlies the conditional cosmological constant dissolution. The framework` | 2.3 |
| F5′ | book/ch18-beyond.md:158 → 158 [4978 → 4980] | `The cosmological constant ratio is a substratum quantity (the de Sitter entropy) being misidentified as an emergent quantity (the vacuum energy).` | `On the framework's reading, conditional on the coupling step, the cosmological constant ratio is a substratum quantity (the de Sitter entropy, up to a convention-dependent factor) being misidentified as an emergent quantity (the vacuum energy).` | 2.3, 2.7 |

The labels F1–F5′ are local to this note; they are not appendix-a IDs.

**No change needed** at ch07:288 [2165 → 2167] ("…normalization identities and formulas awaiting tests") or appendix-a:103 [5656 → 5658] ("…separate from the descriptive vacuum-energy distinction and the classical boundary-density normalization"). The ħ calibration identity remains in the ch07 table, and the two relations now appear in A.4.2's consistency paragraph, so both texts stay accurate.

After applying F1–F5′, rebuild the book (`sh ./build.sh --book`). README is not built.

### Conflict check against #936 (`git diff 687e885b 17b830bc`)

I simulated the merge with `git merge-file -p ours base theirs` for every manuscript file both sides changed: book/README, FULL.md, appendix-a, bibliography, ch07, ch09, ch18, ch19, glossary, papers/GR. Ours is the worktree, base is `687e885b`, theirs is `17b830bc`. The outputs are written only to `S/cc2/edits/mergesim/`; no git object or ref was written.

- **Text sources: 0 conflicts in all 10 files.**
- **Mirror rule after the simulated merge:** every merged chapter line occurs in the merged FULL.md (0 misses).

My edits near #936 hunks merge cleanly but should be eyeballed:

| My edit | Nearby #936 change | Gap |
|---|---|---|
| GR:603 | GR:605 | 1 line |
| ch18:160 | ch18:158 | 1 line |
| ch19:330 | ch19:334 | — |
| appendix-a G4/G7/G14 deletions at :110/:113/:119 | :103 and :116 | — |
| bibliography Bekenstein (:118) and Hawking (:138) entries | #936's insertions after :152 and :162 | — |
| FULL.md | — | the same pairs |

**Binary and generated conflicts are certain:**
- `papers/GR.tex`/`.pdf` and `book/The-Incompleteness-of-Observation-FULL.tex`/`.pdf` are changed on both sides.
- **Resolve by regenerating**, not by picking a side: after the merge and F1–F5′, run `sh ./build.sh GR` and `sh ./build.sh --book`, then `tools/staleness_check.py`.
- SM, Substratum, Structure, Explainer and Methodology artifacts are changed only on my side.

`verification/coverage/LEDGER.json` is changed only by #936.
- My GR edits leave GR's line count unchanged at 1007 and touch no ledger-fingerprinted statement; the Appendix A theorems are untouched.
- coverage_check should therefore hold after the merge. Re-run it.

***

## 6. Build and check results

**Build:**
- `sh ./build.sh SM GR Substratum Structure Explainer Methodology`: OK.
- `sh ./build.sh --book`: OK.
- No dropped glyphs reported.

| Artifact | Pages before → after | Median chars/page before → after |
|---|---|---|
| SM | 145 → 146 | 3115 → 3137 |
| GR | 86 → 86 | 3182 → 3210 |
| Substratum | 52 → 52 | 3248 → 3243 |
| Structure | 98 → 98 | 2952 → 2970 |
| Explainer | 69 → 69 | 2882 → 2863 |
| Methodology | 54 → 54 | 3090 → 3090 |
| Book (FULL) | 553 → 553 | 3068 → 3059 |

**Checks** (from the worktree root, after the build):
- `tools/staleness_check.py`: OK. The 7 rebuilt artifacts are stamped to their sources; the other 6 papers are unstamped only because their artifacts are outside the sparse checkout.
- `tools/voice_check.py`: OK. `tools/claims_check.py`: OK. `tools/duplicate_check.py`: OK.
- `papers/oi_lattice_code/mirror_check.py`: 0 divergences. In addition, the FULL diff's added and removed lines equal, as multisets, the union of the chapter diffs (103 = 103).
- `citation_check.py`: 112 citations, 0 broken. `architecture_check.py`: 259 invariants, 0 violations.
- `tools/dependency_label_check.py --strict`: OK (self-test OK).
- `tools/coverage_check.py`: OK (128 statements). **No ledger fingerprint went stale, so no ledger entry was updated.**
- `tools/lean_manuscript_census.py`: OK. `tools/artifact_placement_check.py`: OK.
- Also run: `toolchain_check` OK; `voice_scope_test` OK; `baseline_label_check` OK; `citation_roles_check <HEAD>`: self-test OK, all hold.
- §A.32/§A.33 battery on the added lines in `papers/`: no new meta-commentary, reader-instruction, caps-emphasis or history-phrase hits. The only hits sit in unchanged text of edited paragraphs: "currently" at SM:849, SM:1456 and Explainer:679.

***

## 7. Re-grep (§A.25 step 6)

Counts are occurrences in `papers/*.md`, `book/*.md` (excluding FULL) and README.md, then in FULL.md. They are case-sensitive.

| Phrase | Sources (before → after) | FULL (before → after) |
|---|---|---|
| "seven parameter-free" | 14 → **0** | 11 → **0** |
| "twenty-two" | 42 → 43 | 30 → 31 |
| "Twenty-two" | 9 → 8 | 6 → 5 |
| "thirteen gravitational" | 9 → **0** | 9 → **0** |
| "Thirteen gravitational" | 2 → **0** | 2 → **0** |
| "parameter-free" | 86 → 91 | 67 → 70 |
| "prediction, not" | 9 → 7 | 6 → 5 |
| "recovered as a prediction" | 2 → **0** | 1 → **0** |
| "echo" | 42 → 17 | 37 → 13 |
| "F5" | 2 → **0** | 2 → **0** |
| "does not gravitate" | 6 → 6 | 4 → 4 |
| "no fitted parameters" | 10 → 9 | 7 → 6 |
| "preregistered" | 2 → 1 | 1 → 0 |

**Why each survivor is legitimate:**

- **"twenty-two" / "Twenty-two".** Every survivor is either:
  - qualified by the new classification ("classified …, two unconditional and five conditional …"); or
  - a neutral inventory reference (ch04:74 "some S-class, some C-class, some R-class", now true; ch06:12; readers-guide:27); or
  - a REVIEW-marked borderline site listed under §4.

  Other "seven" survivors name different sets: ch02:54 and Explainer:860 "seven structural inputs/predictions"; ch07:12 "seven structural results" (#936's line); ch09:158.
- **"parameter-free" (91):**
  - 28 are the new count wording;
  - 20 are the JUNO sin²θ₁₃₂ value ("parameter-free retrodiction", no fitted parameter; L through Cond 2);
  - 6 are definitional or negative ("strictly parameter-free", "not a parameter-free …");
  - 3 are the deferred a₀;
  - 19 are other legitimate uses: the S legend, "not a parameter-free first principle", ch09's comparisons with other programs, Complexity's chemistry chain, "parameter-free retrodictions" as Class B's name, ch06's "four Layer-1 relations are parameter-free" (true: no fitted input).
- **"prediction, not":** Explainer:769 ("a specific prediction, not a free parameter"), and the ch00:101 and ch15 "proposal-level prediction, not a test of the characterization theorems". All are correct.
- **"echo":**
  - GR:603 (×2) and ch18:18/:164/:166, now the GR §8.4 statement;
  - ch00:101 and README:90 ("absence of an OI-specific … echo");
  - bibliography titles (Tsang; Westerweck), which ch18 §18.6 still cites;
  - ch13 "photon echoes" and Explainer:741 "pre-echo" (other senses).
- **"does not gravitate":**
  - GR:362: ħ does not gravitate, a different claim;
  - ch07:207, ch07:258, ch09:90 and ch19:38, each now explicitly the conditional proposal.
- **"no fitted parameters":**
  - ch04:42: the S-class definition;
  - ch06:92 (1/α₀), ch06:110 (λ: still no fitted parameter, now C), ch06:165 (Koide);
  - Substratum:198: the gauge sector;
  - Explainer:880: the chemistry chain;
  - Explainer:671 and glossary:103: a₀, deferred item 13.
- **"preregistered":** Main:478 is a preregistered probe ensemble, correct as stated.
