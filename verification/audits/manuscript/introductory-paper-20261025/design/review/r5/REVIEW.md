# Independent review: Introduction r5 design (OUTLINE/CLAIMS/CHANGES/DEPENDENCIES-r5 and the applications audit)

- **Object.** #918, branch `draft/oi-introductory-paper-20261025` at `d3cd119a`:
  `design/{OUTLINE,CLAIMS,CHANGES,DEPENDENCIES}-r5.md` and `design/applications-audit/{AUDIT.md,quarter.py,cc.py,lookelse.py}`.
  The committed AUDIT differs from `S/paper/apps/AUDIT.md` on line 5 only (the scratch prefix is elided). The three
  scripts are byte-identical to the scratch copies.
- **Baseline.** `draft/Introduction-r4.md`, sha256 `5f9fdcc5…68f6` (verified), with its re-checks.
- **Corpus.** `main` `687e885b` (`S/paper/mainwt`). History: `S/ppe/repo` (4,759 commits).
- **Other inputs.**
  - R11 `REVIEW.md` and `DIFF-REVIEW.md` (`S/paper/r11/`);
  - #936 at `4c0d705e` (`git diff 687e885b 4c0d705e`, `S/bhfix/wt`);
  - the arXiv abstracts in `S/paper/design-r5/dl/`.
- **Read-only.** No repository file was changed. My own checks are in `S/paper/design-r5-review/chk/`
  (`indep.py`, `lookelse2.py`, `shell.py`, `refs.py`), all run with `python3 -I`. Git was run with
  `-c gc.auto=0 -c maintenance.auto=false`.

## Verdict: ACCEPT WITH CHANGES

The design delivers the brief's three-question structure. Quantum emergence stays central (about 8.5 of the main-text
pages are Q1 plus §§6.1–6.3), and Theorems 1–4 are carried verbatim. The cosmological-constant subsection is
conditional throughout, and the 1/4 is correctly framed as consistency. The audit's key results reproduce
independently.

Required changes R1–R19 follow, all at wording or register level. None reopens the structure. The ones that matter
most:
1. **The black-hole subsection (R1–R5).**
   - It loses r4's full-product-shell qualifier in compression.
   - It still calls GR's Page curve "a conditional result", although DIFF-REVIEW settles, by exact algebra, that
     Thm A.8's value is wrong on a restricted shell. I re-derived this.
   - It states H-decouple more weakly than #936's corrected definition.
   - It omits GR's own condition that the Page curve, like the cosmological constant, is conditional on the covariant
     field equations (GR:12).
2. **"The one quantitative item with a stated test" is false as stated about the corpus (R10).** appendix-a:217
   lists four other pre-registered forward tests.
3. **Two hidden assumptions in §5.1:**
   - N-CC4's "no cancellation is required" (R6);
   - N-CC3's "same partition" (R7).
4. **The JUNO value's dependence on the Cabibbo identification is unstated (R11).**
5. **The page arithmetic undercounts the verbatim carry-overs by about 1 pp (R15, O1).**

## 1. Independent verification of the audit's key results

| Item | My method | Result |
|---|---|---|
| **1/4 is a calibration identity** | `chk/indep.py`. GR Step 4 exactly as written (GR:148): $k_BT_{\rm cl}=c^2\epsilon^2\kappa/(a G\sigma)$, $k_BT_Q=\hbar\kappa/(bc)$, with $a,b$ symbolic. I first checked that $T_{\rm cl}$ is $dE/dS_{\rm count}$, i.e. that the mode count is *inside* $T_{\rm cl}$. | The calibration fixes only $\epsilon^2/\sigma=aG\hbar/(bc^3)$. Then $S_{\rm count}/(A/l_p^2)=b/a$, free of σ, which is 1/4 at $a=8\pi$, $b=2\pi$. Hawking route with no count: also $b/a$. Countercontrol: without the calibration, $S/(A/l_p^2)=G\hbar\sigma/(c^3\epsilon^2)$, which is not fixed. **Confirmed.** Because the count enters $T_{\rm cl}$, $T_{\rm cl}=T_Q$ is Hawking's $dS=dE/T$ rewritten, so the 1/4 is put in, not output. This is a sharper statement than `quarter.py`'s. |
| **10¹²² = (8/3)·S_dS** | `chk/indep.py`, sympy exact | $(\rho_{\rm cut}/\rho_{\rm crit})/S_{\rm dS}=\tfrac83(l_p/l_{\rm cut})^4$, exact. **Confirmed.** But the factor depends on the convention. With the honest mode sum $\rho=\hbar c/(16\pi^2l^4)$ it is $1/(6\pi^2)\approx0.017$, not "order one". The ratio itself runs from $6.0\times10^{122}$ ($\hbar c/l_p^4$ against $\rho_{\rm crit}$) or $8.8\times10^{122}$ (against $\rho_\Lambda$) down to $5.6\times10^{120}$ (mode sum against $\rho_\Lambda$). EvEMU11's abstract itself says "60 to 120 orders". See R9. |
| **Cabibbo dating** | path-limited `git log --all -S` | The form $\lambda=1/(\pi\sqrt2)$ and the comparison "0.22500 ± 0.00067 … 0.04%" first appear together in `054eb99a` (2026-04-04, `Predictions.md`), labelled "fifteen quantitative predictions with zero free parameters". `c_\lambda` first appears in `70ffe82f` (2026-07-05) and "≈190σ" in `3124ef0a` (2026-07-06). **Confirmed.** N-EX2's wording ("measured before they were written") holds independently of repository dating, since λ has been measured since 1963. |
| **JUNO split** | `git show 054eb99a:Predictions.md`; `git log -S'(4/3)'` | The value $1/3-1/(4\pi^2)$ is written on 2026-04-04, after JUNO's first result (Nov 2025, Juno:73), and compared there with 0.307 ± 0.013 at 0.1σ. **The audit's "undetermined" can be settled:** the 4/3 ratio first appears in `77ac23ce` (2026-04-30), 26 days later. Juno:237 shows the ratio is *equivalent* to preserving the TBM sum rule $2\sin^2\theta_{12}+\sin^2\theta_{23}=7/6$ at O(λ²), which the 04-04 values already satisfy. So the ratio is an operator-level restatement of a value already compared with data, not an independent input. Postdiction for the central value: **confirmed.** Forward exposure for the ±0.0014 precision: **confirmed**, as a test of a postdicted value. It is not "IP-in-kind" (R11). |
| **Look-elsewhere** | `chk/lookelse2.py` (distinct values; local density; complexity ranking) | **The count is wrong.** `lookelse.py` stores (value, label) pairs, so $1/(\pi\sqrt2)=\sqrt2/(2\pi)$ is counted twice: **5** distinct values within 1σ, not 6. The expected count is 2.5 by global density and 2.8 by local density (±0.03). **The method is weak but not misleading:** a count of family members is not a trials-corrected significance. A sharper statement: of the **11** family values at most as complex as $1/(\pi\sqrt2)$ (a+b+\|k\|+r ≤ 5), the chance that one lands within 1σ of a random target in [0.1, 0.5] is **≈3.5%**. That is before the trials factor over the fifteen observables of `054eb99a` and the dispersion selection. The audit's reading ("notable for so simple a form, but not by itself strong evidence") stands. r5 quotes no look-elsewhere number, so this affects the register only (R17). |
| **A.8 shell error** (coordinator input) | `chk/shell.py`, exact | The Haar mean on the diagonal shell $\mathrm{span}\{\|i\rangle\|i\rangle\}$ is exactly $H_m-1$: 1/2, 5/6, 13/12, 481/280 at m = 2, 3, 4, 8. Page's $S(m,m)$ is 1/3, 0.662, 0.922, 1.589. **Confirmed:** A.8's $S_{\rm Page}(d_B,d_R)$ holds only on the full product space. BH-02 REPORT C6(c) on `main` already carries the diagonal-shell result, so r5 can cite [BHb, C6(c)] for it. |

## 2. Status sentences against their sources

`chk/refs.py` keyword-checked 103 line references from AUDIT and DEPENDENCIES at `687e885b`. Apart from the items
below, every one lands on its stated line.

### §5.1 Cosmological constant (leads)

- No sentence uses "dissolve", "resolve", "eliminate" or "expect".
- N-CC2, N-CC5, N-CC7 and N-CC8 are at or below GR:356 and GR:360, the maintained anchors. The design rightly leaves
  aside GR:356's last two sentences, GR:360's "eliminates" and GR:583.
- Four sentences need changes.
  - **N-CC4 (hidden assumption, R6).** "…the zero-point sum … is not a source *and no cancellation is required*."
    - The target form $E_{\mu\nu}=8\pi G(T_{\mu\nu}-\mathcal F[g,T]g_{\mu\nu})$ carries an uncomputed Λ-like term
      $\mathcal F$.
    - Nothing fixes the vacuum part of the substratum's own classical stress-energy at H²/G. GR:581 asserts it, and
      GR:360 concedes it is "set by initial conditions".
    - So "no cancellation is required" is stronger than the conditional supports. What follows is only that *the
      zero-point sum* needs no cancellation; the remaining vacuum term is uncomputed. This is the audit's own §1.3
      item 5 ("why is the integration constant small"), and the permitted sentence did not inherit it.
  - **N-CC3 (hidden assumption, R7).**
    - "Two completions … can share the same substratum, **partition**, visible law, … and action-scale calibration
      while differing in exactly that offset." For the same $T^{\rm cl}$ the two completions give different
      expansion rates, and so different cosmological horizons.
    - The partition in GR is the cosmological horizon (§2.1), and the calibration uses its κ. So "same partition and
      calibration" holds only if the partition is held fixed by fiat or the source compensates.
    - CLAIMS rates this "proved at prose level". It is an unverified prose observation. r5 needs only the weaker
      true statement, that quantum data do not decide between the completions.
  - **N-CC1 (R8).** "…assigns the zero-point offset no observable content" is too strong while the gravitational
    response is open, and it reads as resolution. Limit it to visible statistics.
  - **N-CC0/N-CC6 (R9).** "About 10¹²²" and "a factor of order one" depend on convention (§1).

### §5.2 Black holes

Measured against REVIEW.md, DIFF-REVIEW.md and #936 (`4c0d705e`):

- **N-BH2 loses an r4 qualification.** r4:190 reads "A dynamics satisfying H-scramble *with the full product space as
  its shell* would produce the Page value". r5's two-sentence condensation drops the italicized clause, so the
  sentence pair can be read as "H-scramble ⇒ Page value". After DIFF-REVIEW §6 this is exactly the scope defect in
  A.8 (R1).
- **N-BH3 says "The Page curve of [GR App. A] is a conditional result" (R2).**
  - Under its listed conditions (H-scramble, decoupling, time average) the stated value is still wrong on a
    restricted shell. Listing those conditions therefore asserts a sufficiency the evidence refutes
    (conditional → stronger).
  - Its decoupling clause ("stays decoupled … over the evaporation") is the drafted H-decouple that DIFF-REVIEW R1
    rejects as weaker than what A.8–A.9 use. A.8–A.9 need closure of B∪R, with no coupling to D *or to V∖R*, over
    whole cycles.
  - It omits GR:12's ladder: "G4, the cosmological implications (cosmological constant, dark sector, **Page curve**,
    …), conditional on G3".
- **The A.9 restatement.** r5 states the time-average scope itself and never cites A.9 as pointwise. This is
  consistent with #936. **Correct.**
- **§5.2 item 1 is inconsistent with CHANGES-r5 (R3).**
  - OUTLINE keeps r4:172 "minus its 'checked exhaustively' sentence".
  - CHANGES-r5 §2 keeps "first two sentences only", which would drop the toy-model sentence and "not a particular
    black hole" while claiming "toy-model scope" is kept.
- **N-BH4 (R4).** It drops "β exceeds 1 in the quasi-stationary semiclassical regime [Pag05]". CHANGES calls this
  information, but it is the qualification that stops 0.646 being read as the physical value.
- **N-BH1 sources.** It cites ch19:72 as "the scoped anchor" of the preservation-versus-recovery split. ch19:72 at
  `687e885b` states preservation only ("information is never lost") and nothing about recovery. The split's source is
  BH-01 claim A. This is a design-record citation only (R18).

### §5.3 Horizon thermodynamics

- N-HT1 and N-HT2 are at or below GR:148, :310 and :320, and they state the consistency framing the brief asks for.
- Nits:
  - "for every ε and σ" can be read as unconditional. Use GR:320's "whatever σ".
  - The cosmological-horizon temperature is Gibbons–Hawking 1977. [Haw75] covers the black-hole relation only.

### §5.4 and §5.5

- **N-PE1.** Gated correctly (§A.42). It is framed as validation.
- **N-MR1.** Below Main:632. Correct.
- **N-AR1 (R13).**
  - It drops two hypotheses of the cited theorem: bounded coupling-graph diameter (Main:730, Scope (i)) and the rate
    condition τ_mix ≪ τ_S (Main:740).
  - "Sufficiently fast-mixing" is Main:740's own phrase, written there in all capitals, but it hides the comparison.
  - It also cites only :730, while the observer-exclusion form is the :740 corollary.

### §6 and §7

- **§6.6 (N-GC1).** It is correct but incomplete without the Page curve's G3 dependence (R14).
- **§6.7 N-EX1.** Correct (Main:704).
- **N-EX2.** Correct (SM:849, appendix-a:217). Note that SM:849 itself also says "established at the structural
  level rather than merely hypothesized" (see §6).
- **N-EX3 (R11).** It omits the dependence on λ², and hence on the Cabibbo identification $c_\lambda=1$ (a commitment,
  SM:849).
- **§5.0, non-claim (9) and the CLAIMS summary (R10).** They call the JUNO test "the one quantitative item with a
  stated test ahead of full-precision data". appendix-a:217 lists "DESI Y5 (ν), the anisotropy amplitude, BTFR at
  z > 1, the A2 lattice thresholds, and JUNO design-lifetime precision" as pre-registered forward content. Scope the
  claim to this paper.

## 3. Classification

Numerical agreement is kept apart from prediction everywhere in the paper text. CLAIMS needs these corrections:

| ID | CLAIMS status | Correct status |
|---|---|---|
| N-CC3 | proved at prose level | prose observation, unverified ("same partition", §2); r5 uses the weaker form (R7) |
| N-CC4 | conditional | conditional, *and* the remaining vacuum term is uncomputed (R6) |
| N-BH2 | C6(c) conditional | C6(c): the diagonal shell is exact algebra ($H_m-1$); Hamming shells are certified by intervals. "Conditional" understates it |
| N-BH3 | conditional, and open | not established: needs H-scramble, B∪R closure over whole cycles, and a full-product shell; a time average only; G4 conditional on G3 |
| N-EX3 | NA + "IP-in-kind" | NA (postdiction) for the central value; **forward test of a postdicted value** for the precision. Drop "IP-in-kind", since N-INT3 defines IP as stated *before comparison*, and this value was compared first. Replace "undetermined" with the dating in §1 |
| N-EX2 | look-elsewhere "6 of 752" | 5 distinct values of 752; method caveat (R17) |
| N-AR1 | conditional on (EM) and the rate condition | the same, plus bounded-diameter partitions |

The rest are correct, including N-HT1 (identity, conditional), N-PE1 (validation) and N-MR1 (interpretation).

## 4. Literature

- **Abstract-level use is honest.** Each sentence is at the strength of the abstract I re-read:
  - [EvEMU11]: "resolves the discrepancy … does not … explain the observed value";
  - [KP14]: "renders all contributions from phase transitions automatically small";
  - [Vol06]: the many-body ground-state argument;
  - [tH14]: "classical at its core … reconciled with Bell's theorem";
  - [Jac95] and [CKN99] are correctly *not* used for the [mem] attributions.
- **Non-claim (10) itself makes a priority attribution (R12).** "A deterministic core analysed by quantum methods
  *is 't Hooft's*" assigns the viewpoint's origin to one book from its abstract, which itself says it is "an
  overview of older material". The viewpoint predates [tH14]. State non-novelty without assigning priority.
- **Major related works not cited (O4).**
  - *Vacuum energy versus Λ.*
    - Weinberg, *Rev. Mod. Phys.* 61, 1 (1989), the standard source for N-CC0's background number.
    - Padmanabhan's emergent-gravity papers, in which bulk vacuum energy does not gravitate and gravity is
      thermodynamic. This is the closest published analogue of §5.1 and §5.3 *together*, so it is the most likely
      referee question.
    - Unimodular gravity (Henneaux–Teitelboim 1989; Unruh 1989), adequately represented by [EvEMU11].
  - *Emergent QM from deterministic or classical dynamics.*
    - Adler, *Quantum Theory as an Emergent Phenomenon* (2004);
    - Wetterich, "quantum mechanics from classical statistics" (2010 onward);
    - Elze's cellular-automaton papers;
    - Spekkens's epistemic-restriction toy theory (2007), which is close to OI's "restricted access" framing.
  - *Embedded-observer limits.* Breuer (1995), Wolpert (2008). These are close to the paper's title concept.
  - All of these are [mem] here. Each needs at least an abstract read before citation.

## 5. Structure and budget

- **The brief is delivered.**
  - Q1 is §§1–4, Q2 is §5 (4.0 pp) and Q3 is §§6–7.
  - The section title is fixed.
  - The cosmological constant leads and is conditional.
  - Black holes are framed as preservation versus access, with "not resolved".
  - The 1/4 is consistency, and PE-01 is validation.
  - The Q3 list follows the brief's order.
- **Quantum emergence is central in the body.**
  - The abstract keeps only r4:12 s1–3 for Q1, which drops the memory and indivisibility sentence (Theorems 2–3).
    That is the discriminating content of the quantum-emergence part (R16).
  - The §6.1 heading "Full quantum equivalence" sits uneasily with DEPENDENCIES §C ("never 'equivalence of quantum
    mechanics'"). This is a nit.
- **Theorems 1–4** are carried verbatim, with their hypotheses, layers, references and witnesses (CHANGES §4 checked
  against r4:58–64, 86–94, 110–114, 214–220). Confirmed.
- **The page arithmetic is not plausible as tabled (R15).**
  - Measured on r4 with comments stripped: main narrative 4,739 words on 12 pp, about 395 words per page.
  - The verbatim carry-overs exceed their budget lines:

    | Section | Carried text | Words | Budget | Over by |
    |---|---|---|---|---|
    | §1 | r4:20–36 | ≈ 535 | 390 | ≈ 145 |
    | §2 | r4:40–100 plus N-LIT1 | ≈ 1,030 | 870 | ≈ 160 |
    | §3 | r4:102–124 | 556 | 480 | ≈ 75 |
    | §5.2 | after R1–R4 | ≈ 540 | 420 | ≈ 120 |
    | §7 | r4 §6.5 (212) + items 7–11 + conclusion | ≈ 450 | 340 | ≈ 110 |

  - Estimated r5 main text: ≈ 5,600 words, or **≈ 14.2 pp** (≈ 13.9 pp with §5.4 gated out). The stated fallback
    (cutting §5.5) recovers about 0.2 pp.
- **Lost in compression.**
  - The full-product-shell clause of r4:190 (R1).
  - The β > 1 clause of r4:195 (R4).
  - Potentially, r4:172's toy-model sentence (R3).
  - The §4 lead r4:128 ("Three examples … (§4.3)") must be rewritten for two examples (nit).
  - Nothing else that r4's reviews required is lost: the sci-N2 text, the §A.34 witnesses, the T1 wording, the
    ERRATUM-r4 decomposition (to Appendix B) and the R11/R12 markers are all kept.

## 6. New findings and the audit's line references

- **Main:726 ("replaces [the past hypothesis] … with a theorem"): CONFIRMED, and wider than reported.**
  - The theorem (Main:730–734) bounds τ_B by the local mixing time. Main:740 turns it into "a sufficiently
    fast-mixing equilibrium supports no (C2)/(C4) observer".
  - A selection rule of this kind says where observers can be. It does not say that the past had lower entropy.
    In a recurrent finite system, a non-equilibrium excursion that admits observers has entropy rising in both
    time directions from its minimum, which is the classic objection to selection-only accounts.
  - Main:740 itself concedes that (EM) at the required rate "is itself a physical hypothesis … the theorem … does not
    supply it".
  - The overclaim also sits at:
    - Main:740 (the corollary's title "past-hypothesis replacement" and its last sentence, "is replaced here by a
      structural selection rule"; the corollary also writes "SUFFICIENTLY FAST-MIXING" in capitals, against §A.33);
    - Substratum:56 ("replaces the low-entropy 'past hypothesis'");
    - Explainer:930 ("replaces the postulate with a derivation … No additional axiom required");
    - Complexity:204 ("dissolved … by a theorem").
  - Class NEW. It is an assumption-watch marker alongside AW-8. r5 is unaffected once R13 is applied.
- **Line-reference errors in the audit and DEPENDENCIES (R18).**
  - AUDIT §0 (Cabibbo row) and §9 cite **SM:851** for "established at the structural level … emergent dressing
    pending". Both phrases are at **SM:849**, the same paragraph as "This is a hypothesis, not a derivation". SM:849
    therefore asserts and then qualifies within itself, which belongs in DEPENDENCIES §F.
  - DEPENDENCIES §D: **ch19:72** does not carry the preservation-versus-recovery split.
  - AUDIT §9: the **preface:7** quotation is "becomes a derivation", not "derivation rather than a postulate", which
    is ch00:21's wording.
  - The rest check: ch09:108's site is right; "GR §3.1 (GR:96–104)" is a range beginning at the heading; SM:16 is a
    one-line offset within an abstract, which is harmless.
- **DEPENDENCIES §B misses CC sites, and one of its anchors is unsafe (R19).**
  - Missed sites:
    - preface:7 / FULL:78 ("The cosmological constant discrepancy of 10¹²² … becomes a calculable compression
      ratio");
    - ch00:89 / FULL:325 (the CC clause, listed only for a₀);
    - Explainer:22 and :547 ("not a discrepancy. It equals S_dS").
  - **ch19:38**, which DEPENDENCIES uses as the *conditional anchor*, states its condition and then asserts
    unconditionally: "The QFT zero-point energy … does not gravitate", "The 10¹²² discrepancy is the de Sitter
    entropy". It is the §A.30 pattern and cannot be the anchor. Use GR:356 up to "the dissolution is conditional".

## 7. Required changes (exact text)

**R1. OUTLINE §5.2 item 3 (N-BH2).** Replace the quoted two sentences with:
> In the framework's nested-partition construction the Page value enters only through the scrambling hypothesis
> H-scramble, which no bijection satisfies from a definite configuration with configuration-aligned cuts [BHb, C1,
> C6(a)–(b)]. H-scramble posits equidistribution of the orbit on an energy shell, and the mean entropy of that
> ensemble equals Page's average $S_{\rm Page}(d_B,d_R)$ for factor dimensions $d_B,d_R$ [Pag93] only when the shell
> is the full product space; on a smaller shell it differs, in a direction that depends on the shell [BHb, C6(c)].

- Sources: add BH-02 REPORT:20, which includes the diagonal shell, exact $H_m-1$; DIFF-REVIEW §6.
- Layer: P + E + A.

**R2. OUTLINE §5.2 item 4 (N-BH3).** Replace the quoted text with:
> The Page curve of [GR App. A] is not established. Its stated hypothesis H-scramble is open. It also requires that
> the black hole and its radiation evolve as a closed system, uncoupled from the sector beyond the cosmological
> horizon and from the rest of the visible sector, over whole cycles of the dynamics; timescale ordering does not
> supply this, since $t_{\rm evap}/\tau_B^D \ge 10^{57}$ at 30 solar masses over the assumed parameter intervals
> [BHa, item F]. Its stated value holds only for a full-product shell, and what the cycle-typicality argument
> supplies is a time average at a fixed bipartition, so the curve along one trajectory is open [BHb, C6(c)–(d)]. In
> the dependency ladder of [GR] the Page curve is also conditional on the covariant field equations. The black-hole
> information problem is not resolved here.

- Sources: add GR:12 ("G4 … Page curve … conditional on G3"), DIFF-REVIEW R1 (the H-decouple definition) and §6.
- Keep the owner default: use the label "H-decouple" only if it is adopted with DIFF-REVIEW R1's definition.
- In "Does not claim", replace "the pointwise Page curve" with "the Page curve, pointwise or as a cycle average on a
  restricted shell".

**R3. §5.2 item 1 and CHANGES-r5 §2, row "BH setting".**
- OUTLINE item 1, replace the line with: "r4:172 sentences 1–3 and 5, verbatim. Sentence 4 (the verification
  layers) is carried by §7.1 item 4."
- CHANGES row, column r5: "sentences 1–3 and 5; sentence 4 moves to §7.1 item 4".

**R4. OUTLINE §5.2 item 5 (N-BH4).** Replace "it is 0.646 at β = 1, β is not derived, and a mass-dependent
coefficient moves the fraction [BHb, C7]" with:
> it is 0.646 at β = 1; β is not derived and exceeds 1 in the quasi-stationary semiclassical regime [Pag05], and a
> mass-dependent coefficient moves the fraction [BHb, C7].

In CHANGES-r5 §2, row "Page time", remove "β > 1 in the quasi-stationary regime" from "Dropped".

**R5. OUTLINE §7.1, item 4.** Specify the exact text:
> 4. No resolution of the black-hole information problem: the Page curve of [GR App. A] needs H-scramble, the closure
> of the black hole and its radiation over whole cycles, and a full-product energy shell, and gives a cycle average
> rather than a curve along one trajectory; the Page-time fraction is conditional on its three inputs; the
> correspondence with islands is conjectural; the generalized second law is open; and the results of §5.2 concern
> finite toy models, each proved on paper or checked exhaustively at small size or by exact arithmetic. No claim is
> made that information reaches $D$, that [GR, Thm A.7] fails within its stated scope, or that no other decoupling
> argument exists.

**R6. OUTLINE §5.1 item 4, first bullet (N-CC4).** Replace with:
> If the covariant field equations take the form [GR] targets, $E_{\mu\nu}[g,\mathrm{OI}]=8\pi G\,(T_{\mu\nu}-\mathcal
> F[g,T]\,g_{\mu\nu})$, with the classical stress-energy of the substratum as source, the zero-point sum of the
> emergent description is not a source and needs no cancellation; the vacuum term that remains, from the
> substratum's classical energy density and from $\mathcal F$, is not computed.

In "Does not claim", add: "that the vacuum term of the target equation is small".

**R7. OUTLINE §5.1 item 3 (N-CC3).** Replace the sentence "Two gravitational completions … [GR §6.2]." with:
> The quantum description therefore does not decide between gravitational completions that differ by a term
> $\rho_C\,g_{\mu\nu}$, such as $\mathcal G_{\mu\nu}=8\pi G\,T^{\rm cl}_{\mu\nu}$ and $\mathcal G_{\mu\nu}=8\pi
> G\,(T^{\rm cl}_{\mu\nu}-\rho_C\,g_{\mu\nu})$ [GR §6.2].

In CLAIMS N-CC3, set status to "prose observation (GR:356); the 'same partition and calibration' clause is not
verified, because the cosmological horizon depends on the completion. r5 uses the weaker form".

**R8. OUTLINE §5.1 item 2 (N-CC1).** Replace "so the quantum description assigns the zero-point offset no observable
content [GR §6.2]" with:
> so the offset has no content in the visible statistics of the quantum description [GR §6.2].

**R9. OUTLINE §5.1 items 1 and 5.**
- N-CC0:
  > Summing zero-point energies of the quantum fields up to a Planck-scale cutoff gives a vacuum energy density some
  > 120 orders of magnitude above the observed one, the exact power depending on the cutoff convention; if that
  > density sources curvature, it must be cancelled to that accuracy.
- N-CC6:
  > With a Planck-scale cutoff the mismatch equals the de Sitter entropy up to a numerical factor fixed by the cutoff
  > convention; this is a dimensional identity, not an independent prediction.
- CLAIMS N-CC0/N-CC6, add: "Factor 8/3 for $\rho=\hbar c/l_p^4$ against $\rho_{\rm crit}$; $1/(6\pi^2)$ for the mode
  sum $\hbar c/(16\pi^2l^4)$. Ratio from $5.6\times10^{120}$ to $8.8\times10^{122}$ across conventions (review
  `chk/indep.py`)."

**R10. "The one quantitative item".**
- §5.0 (N-INT3), last sentence:
  > The applications in this section are conditional proposals, finite results, consistency relations and one
  > interpretation; none is an independent prediction. §6.7 discusses the one quantitative item within this paper's
  > scope that has a stated test ahead of full-precision data.
- §7.1 non-claim (9):
  > (9) No Standard-Model value is claimed as an independent prediction. The JUNO precision test of §6.7 is a forward
  > test of a value written after JUNO's first result.
- CLAIMS "Summary for the owner", second bullet:
  > Within r5's scope, the only item with a stated test ahead of data is the JUNO precision test (N-EX3), a test of a
  > postdicted value. The corpus records further pre-registered forward tests in the gravitational and dark sectors
  > (appendix-a:217), which r5 excludes.

**R11. OUTLINE §6.7 N-EX3.** Replace with:
> The value sin²θ₁₂ = 1/3 − 1/(4π²) = 0.30798 was written after JUNO's first result; JUNO's projected design-lifetime
> precision of ±0.0014 will test it. The value rests on the Cabibbo identification above and on a Wilson-coefficient
> ratio that is not derived [Juno].

In CLAIMS N-EX3, replace the "Agreement and dating" cell with:
> **NA** for the central value (0.07σ; a postdiction). For the precision, a **forward test of a postdicted value**,
> not an independent prediction. Dating: the value and its comparison (0.307 ± 0.013, 0.1σ) are in `054eb99a`
> (2026-04-04); the 4/3 ratio first appears in `77ac23ce` (2026-04-30), and Juno:237 shows it is equivalent to the
> sum rule $2\sin^2\theta_{12}+\sin^2\theta_{23}=7/6$ at O(λ²), which the 04-04 values already satisfy. The ratio was
> therefore introduced after the value had been compared with data.

Change OUTLINE's "Whether 4/3 was selected with the data in view is **undetermined**" to match. The JUNO projection
should be cited to the JUNO collaboration, VERIFY, not only to [Juno].

**R12. OUTLINE §7.1 non-claim (10).** Replace with:
> (10) No claim that the viewpoint is new: deterministic systems analysed with quantum methods have been studied
> before, for example in [tH14]. The paper's results are the theorems and their scopes.

**R13. OUTLINE §5.5 N-AR1.** Replace with:
> Under the effective-mixing hypothesis (EM), on partitions of bounded coupling-graph diameter, an equilibrium region
> whose local mixing time is much shorter than an observer's record-persistence time supports no observer with
> persistent, read-back records [Main §4.6]; the selection rule does not by itself supply a low-entropy past.

- Source: Main:730–734 and Main:740 (the rate condition).
- In "Does not claim", add: "that the past hypothesis is replaced (Main:726, :740)".

**R14. OUTLINE §6.6 N-GC1.** Replace sentence 2 with:
> The cosmological-constant proposal of §5.1 is conditional on them, as is, in the dependency ladder of [GR], the
> Page curve of §5.2; the horizon calibration of §5.3 uses Einstein's first law as an input.

**R15. OUTLINE "Page budget".**
- Replace the per-section word figures for §1, §2, §3, §5.2 and §7 with the sizes measured on r4 (§5 above): 535,
  1,030, 556, 540 and 450.
- Set the total to ≈ 5,600 words, ≈ 14.2 pp (≈ 13.9 pp without §5.4).
- Add the line:
  > Reaching 13 pp needs about 0.9 pp of trims that remove no qualification. Candidates are §6.2's second paragraph
  > (r4:226) to an appendix, and r4:66–68's construction details to an appendix next to Appendix A. This is an owner
  > decision.

**R16. OUTLINE Abstract, Q1.** Replace "r4:12, sentences 1–3" with "r4:12, sentences 1–3 and 5 (the memory and
indivisibility sentence), with sentence 4 reduced to 'and the Born exponent is not selected'". Raise the abstract
budget to 260 words.

**R17. CLAIMS N-EX2 and AUDIT §6.2, look-elsewhere.** Replace "6 of 752 simple forms within 1σ, about 2.5 expected"
with:
> 5 distinct values of 752 within 1σ, about 2.5 expected by density (`lookelse.py`'s 6 counts $1/(\pi\sqrt2)=\sqrt2/(2\pi)$
> twice). This is a density count, not a trials-corrected significance: of the 11 family values at most as complex as
> $1/(\pi\sqrt2)$, the chance that one lies within 1σ of a random target is about 3.5%, before the trials factor over
> the corpus's other observables and the dispersion selection.

The AUDIT is a WIP design record, so correct it in place.

**R18. Line references.**
- AUDIT §0 Cabibbo row and AUDIT §9 "Classification": "SM:851" → "SM:849".
- DEPENDENCIES §D "r5 cites instead": replace "ch19:72 (5248) for the preservation-versus-recovery split" with "BH-01
  REPORT:17, :36 (claim A) for the preservation-versus-recovery split; ch19:72 states preservation only".
- OUTLINE N-BH1 sources: drop "ch19:72 (the scoped anchor)".
- AUDIT §9: split the preface:7 quotation ("becomes a derivation") from ch00:21's.

**R19. DEPENDENCIES §B and §C.**
- §B: add rows for preface:7 (FULL:78), ch00:89 (CC clause), Explainer:22 and Explainer:547.
- §B: replace "ch19:38 (5214), conditional form" in the "r5 cites instead" column with "GR:356, up to 'the
  dissolution is conditional'".
- §B: add ch19:38 itself as a site: "states the condition, then asserts 'does not gravitate' and '10¹²² is the de
  Sitter entropy' unconditionally (§A.30)".
- §C, Main:726 row: extend the site list to Main:740 (title, last sentence and the capitals of §A.33),
  Substratum:56, Explainer:930 and Complexity:204, and mark it "confirmed by independent review".
- §F: add "SM:849 asserts 'established at the structural level' in the same paragraph as 'a hypothesis, not a
  derivation'".

## 8. Nits

1. **N-HT1.** "equals A/(4l_p²) for every ε and σ" → "equals A/(4l_p²) whatever the value of σ". Add [GH77]
   (Gibbons–Hawking 1977), VERIFY, for the cosmological-horizon temperature.
2. **§6.1 heading.** "Full quantum equivalence: operational completion" → "From the correspondence to operational
   quantum mechanics".
3. **§4 lead (r4:128).** Rewrite for two examples, with Appendix B for the card table.
4. **N-INT2.** Apply r4 sci re-check nit N-a: "unpublished repository research records [BHa; BHb], with written
   proofs and exact or exhaustive checks".
5. **N-EX2, optional.** Add "one of whose ingredients was chosen among candidate dispersions by comparison with the
   measured value [SM]" (SM:851, ≈190σ).
6. **N-PE1.** "attacks of this kind … are known" needs a citation once §5.4 is ungated. A bare "known" will draw a
   referee query.
7. **N-CC1 sentence 1.** "belong to different levels of description" → "are defined at different levels of
   description". The definitional reading is what GR:356 establishes.
8. **N-CC0.** Cite Weinberg 1989 (VERIFY) for the background number.
9. **OUTLINE "Sources".** Cite the in-repo `applications-audit/AUDIT.md`, not `S/paper/apps/AUDIT.md`.

## 9. Owner decisions

- **O1. Length.** At r5's verbatim carriage the main text is ≈ 14 pp. Accept that, or authorize the appendix moves
  in R15. No qualification needs to be cut either way.
- **O2. H-decouple.** Adopt the label once #936 lands with DIFF-REVIEW R1's definition: closure of B∪R, no coupling
  to D or V∖R, over whole cycles. R2's wording holds with or without the label.
- **O3. A.8 remedy (#936 follow-up).**
  - Option 1, restricting to Σ_E = H_B⊗H_R, makes the energy shell the whole product space. That means no energy
    constraint on B∪R, which is physically restrictive.
  - Option 2, the Haar-on-shell mean, moves the turnover and the Page-time identification.
  - R1 and R2 hold under either option.
- **O4. Literature.** Read at least the abstracts of Weinberg 1989, Padmanabhan, Adler 2004, Wetterich and Spekkens
  2007, and decide whether §2.2 and §5.1 cite them. Padmanabhan is the most likely referee comparison for §5.1 with
  §5.3.
- **O5. Corpus queue.** Main:726 family, R19 sites and ch19:38: route them to the separate manuscript-consistency
  change (§A.25, §A.30).
- **O6. AW-9.** The S/C/L/R/P/M/E scheme has no postdiction marker. The Cabibbo row (appendix-a:74, S) is the test
  case.
