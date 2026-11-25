# GAMMA-1 unit G3, r1; paper-only; literature; unreviewed

**What this note does.** It records, from first-hand reading, the performed experiments that bear on
G1's targets X-1 to X-3 and on the open PC-wave entries of X-4 and X-5 (GAMMA-G1 r4 §§5.4, 5.5, 7.2,
7.4 and §12, "For G3"). For each source it gives the citation checked against Crossref, what was
measured, the numbers with their stated errors, the conditioning, whether the data are public, the
§A.24 class of each datum, and the read status. It renders no verdict on D-1, on (γ), on any credit
set or on any separation; §6 lists what the data allow G5 to test. It runs no computation,
simulation, enumeration or Lean, adopts no premise, edits no manuscript and changes no Issue. The
few [A-inf, by hand] items are arithmetic on numbers printed in a source, offered for G5 to check.

**Authorization.** #1305 body, planning-status block: "`paper-only`. G1 in wave 1; G2 and G3 in wave 2
(owner, 2026-11-15, recorded on #1169). No computation, simulation, enumeration, new premise or merge."
The #1169 comment that carries the wave-2 record was not located in this unit; the Issue body is
quoted as the authorization source. **Writer:** Claude. **Review:** a separate non-author reviewer
(pending).

**Inputs, at exact objects.** Branch `research/ro1-sector-c-1169-20261114` (PR #1294) at
`6ab9515dec3d54ad90058bfec0d24c49c0e78d73`, directory
`verification/programmes/oi-qm/reconstruction/drafts/ro1-sector-c-20261114/`. **Off `main`.**
- `GAMMA-PLAN-r1.md`, blob `77f1fcd8d32403b26fb87c47cfd572bbf982febb` (PLAN-G);
- `GAMMA-G1-r4.md`, blob `91a5d656bed2b5ef5781106f1e22bfecbf35cd8b` (G1, by section);
- `LIT-ERASER-r3.md`, blob `2b414173ce862d570aabb56e86c6b76344da0194` (LIT, by item). The items LIT read
  (Kim 2000, Walborn 2002, Ma 2013, Schwindt 1999, Dürr 1998 and the rest) are not re-summarized; where
  G3 re-opened one of them, it was for a question LIT did not record, and the item says so.
- #1305 body, read through the GitHub REST API on 2026-11-15.

**Read date.** 2026-11-15.

**Method and labels.** As LIT. Full texts were read only from open copies: arXiv PDFs converted to
text, and, for one item with no text layer (the Grangier thesis), page images read visually.
Abstracts of paywalled items were read from the publisher's page or the Crossref record. Bibliographic
data were checked against the Crossref REST API, and open-access locations against the OpenAlex API.
Paywalled full texts were not retrieved. Status labels: **FULL** (whole text read, version stated);
**SECTIONS** (named pages or sections read, rest NOT READ); **ABSTRACT**; **SECONDARY**; **NOT READ**.
"Not reported" means not found in the version read. §A.24 classes, as G1 §5.5: **raw-direct** (counts,
coincidence counts, integration times, a feature of plotted raw counts stated by the source);
**derived** (computed from raw counts by a formula the source states); **inferred** (fitted,
background-subtracted, corrected, or obtained from a theory formula).

***

## 1. X-4 re-read: Schwindt, Kwiat & Englert 1999 (G1's open items)

| Field | Record |
|---|---|
| Citation (Crossref) | P. D. D. Schwindt, P. G. Kwiat, B.-G. Englert, "Quantitative wave-particle duality and nonerasing quantum erasure", *Phys. Rev. A* 60(6), 4285–4290 (1 Dec 1999), doi:10.1103/PhysRevA.60.4285 |
| Version read | arXiv quant-ph/9908072v1 (23 Aug 1999, "to appear in Physical Review A"), FULL. Published version NOT READ |
| Data public | No data file or table; values are plotted only (Figs. 2–4) |

**1.1 Raw maximum and minimum counts (G1 §7.1, NC-rep; G1 §5.4).** Not reported. The text gives the
procedure only: "For Visibility measurements the polarization analyzer was lowered out of the beam
path, and the maximum and minimum count rates on detector 1 were measured as the length of path 2 was
varied slightly (via a piezoelectric transducer). After subtracting out the separately-measured
detector background (i.e., the count rate when the input to the interferometer was blocked, typically
100–400s⁻¹), the visibility was calculated in the standard manner: V = (Max − Min)/(Max + Min)." No
value of Max or Min, no integration time and no signal rate per setting appears in the version read.
The only rate bound stated is "the maximum detection rates were always less than 50,000s⁻¹". Fig. 2
plots `V` and `K` against the internal half-wave-plate angle `θ_HWP` (0° to 45°); Fig. 3 plots mixed and
partially mixed inputs; Fig. 4 plots eraser visibility against analysis angle. No error bars on
individual `V` points are described in the text.

**1.2 T-block conditions (G1 §5.4, "T-block conditions").** Stated: "With the polarization analyzer
in place, and path 2 blocked, the counts on the two detectors were measured. Detector 1 (2) looked at
polarization λ (λ⊥), determined by the analysis settings. After subtracting the backgrounds measured
for each detector, the count rates from detector 1 were scaled by the relative efficiency of the two
detectors: η₂/η₁ = 1.11 ± 0.01." "Next, we measure the corresponding quantities for path 2: R2λ and
R2λ⊥." The likelihood is their Eq. (2):

    L = [max{R1λ, R2λ} + max{R1λ⊥, R2λ⊥}] / (R1λ + R2λ + R1λ⊥ + R2λ⊥),   K = 2L − 1.

- The marker is read with both outcomes at once (two detectors behind the analysis prism), in each of
  the two blocked runs.
- Equal incident flux and equal integration time between the path-2-blocked and path-1-blocked runs:
  **not stated**. The quantities are "count rates", so integration time cancels per rate; the source
  intensity being equal across the two runs is not stated.
- Basis: "Except where noted, our measurements were suitably optimized to maximize K"; the optimal
  axes for linear polarizations are "(φ₁ + φ₂)/2 ± 45°" (their note 16). Fig. 2 also shows a second
  `K` set "fixed in the horizontal-vertical basis".
- Predictability: beam-splitter reflectivities and transmittivities "in the range 0.49 to 0.51 for all
  polarizations"; "P ≈ 0 in our experiments".
- The form of Eq. (2) is G1 §2.4's `K_P` with priors from the detected rates of the two blocked runs
  [A-inf: same expression, `c_π(m)` read as `R_{πm}`].

**1.3 What G1 did not record and the source states.**
- Light sources: the pure-input data use a 670 nm source "greatly attenuated"; the mixed-input data use
  "photons from an attenuated quartz halogen lamp that was spectrally-filtered" and a "tunable"
  diode-laser scheme. No anticorrelation or photon-statistics measurement is reported for these
  sources. The single-photon regime is argued from attenuation ("fewer than 10⁻⁴ photons were in the
  interferometer at any time"), and the existence of photons is taken from elsewhere: "we accept the
  existence of photons as an established experimental fact [13]", with [13] = Clauser 1974 and
  Grangier–Roger–Aspect 1986.
- On classical fields, the source states: "the counting rates of single-photon interferometers, such
  as the one used in our experiment, are proportional to the intensities of the corresponding
  classical electromagnetic field. But there is no allowance for individual detector clicks in
  Maxwell's equations [14], nor for the quantum entanglement of photonic degrees of freedom that we
  exploit. And clearly, the trajectory of a light quantum through the interferometer is a concept alien
  to classical electrodynamics, as is the experimenter's knowledge K about this trajectory." And, on a
  Bell test between path and polarization of the same photon: "this violation of Bell's inequality
  implies nothing about the success or failure of local-hidden-variable theories". No Bell test is
  reported as performed.
- The sorting eraser of Fig. 4(b) ("a completely-mixed state, with θ_HWP = 45°") was taken with the
  mixed source, i.e. the filtered lamp or the diode-laser scheme; the text does not say which for
  Fig. 4(b).

**1.4 Classification.**

| Datum | Class |
|---|---|
| Max, Min count rates at detector 1 | raw-direct; **not reported** |
| Background 100–400 s⁻¹ | raw-direct (stated range) |
| `V` per setting (Fig. 2) | inferred (background subtracted) |
| `R1λ`, `R1λ⊥`, `R2λ`, `R2λ⊥` | raw-direct; not reported |
| `K` per setting | inferred (background subtracted, efficiency-scaled) |
| η₂/η₁ = 1.11 ± 0.01 | measured apparatus input (E) |
| Mean `V² + K²` = 0.976 ± 0.017; 0.998 at minimum visibility; mixed 0.003 ± 0.001 | inferred (from the two inferred quantities) |

## 2. X-2: single-quantum anticorrelation

### 2.1 Grangier, Roger & Aspect 1986 (named in PLAN-G §5.3 and G1 §7.4)

| Field | Record |
|---|---|
| Citation (Crossref) | P. Grangier, G. Roger, A. Aspect, "Experimental Evidence for a Photon Anticorrelation Effect on a Beam Splitter: A New Light on Single-Photon Interferences", *Europhys. Lett.* 1(4), 173–179 (15 Feb 1986), doi:10.1209/0295-5075/1/4/004 |
| URL read | https://iopscience.iop.org/article/10.1209/0295-5075/1/4/004 (abstract on the article page) |
| Read status | ABSTRACT. Full text NOT READ (the PDF link returned the article page, not the PDF) |
| Paper's own claim (abstract) | "We report on two experiments using an atomic cascade as a light source, and a triggered detection scheme for the second photon of the cascade. The first experiment shows a strong anticorrelation between the triggered detections on both sides of a beam splitter. This result is in contradiction with any classical wave model of light, but in agreement with a quantum description involving single-photon states. The same source and detection scheme were used in a second experiment, where we have observed interferences with a visibility over 98%." |
| Key numbers | NOT READ in the EPL text |

### 2.2 Grangier 1986, doctoral thesis (the same experiment, first author)

| Field | Record |
|---|---|
| Citation | P. Grangier, *Étude expérimentale de propriétés non-classiques de la lumière ; interférences à un seul photon*, Thèse d'État, Université Paris-Sud (Orsay), defended 15 Sept 1986; HAL tel-00009436 (no DOI). Cited by Ma–Kofler–Zeilinger 2016 (arXiv 1407.2930) as Grangier 1986 |
| URL read | https://pastel.hal.science/tel-00009436 (file `tel-00009436.pdf`, 287 pages, scanned, no text layer) |
| Read status | SECTIONS: English abstract (front matter); table of contents; thesis pp. 59–64 (§II-A, semi-classical inequalities); pp. 94–110 (§II-C end, §II-D, results, counter-experiment, discussion); pp. 139–150 (§III-C, interference results and the auxiliary anticorrelation control). Read as page images. Rest NOT READ |
| Relation to the EPL paper | p. 98: of two versions of the anticorrelation experiment, "la deuxième version de l'expérience a été réalisée conjointement avec l'expérience d'interférences ... et c'est cette deuxième version qui sera décrite en détail". Whether the EPL paper reports the same runs and numbers: NOT READ |
| Data public | Yes for the tabulated counts below (thesis, open archive). No machine-readable file |

**Set-up and conditioning (pp. 60–61, 95–100).** Calcium radiative cascade; a detection of the first
photon ν_A at PMA opens a gate of duration `w` (≈ 9 ns; fitted `w₁ = 8.7 ns`, `w₂ = 9.1 ns`, Eq. II-57)
during which detections at PMB1 and PMB2, on either side of a beam splitter, are counted. Measured:
the trigger rate `N_A`, the gated rates `N₁`, `N₂`, and the gated coincidence count `N_c T`. All
counts are **conditioned on the trigger** (herald) by construction. Each measurement sequence: 16
counting periods of 400 s (p. 99). The source intensity is servo-controlled (p. 98–99).

**The classical bound (pp. 61–62).** With detection probabilities linear in the integrated classical
intensity in each gate (Eq. II-2: `P₁ = S_T ∫₀^w I_B`, `P₂ = S_R ∫₀^w I_B`, `P_c = S_R S_T (∫₀^w I_B)²`, gate
averages) and `⟨Ω²⟩ ≥ ⟨Ω⟩²`: `P_c ≥ P₁P₂` (II-5a), `N_c ≥ N₁N₂/N_A` (II-5b). The anticorrelation
parameter is `α = N_c N_A / (N₁N₂)`, and every semi-classical model gives `α_Class ≥ 1` (pp. 102, 108,
Fig. II-18). A second derivation including the trigger as a three-time intensity correlation is given in
§II-A-3 (pp. 63–64, read to its Eq. II-12 and the start of the Schwarz argument).

**Raw results, Table II-3 (p. 103), "Résultats bruts".** `N_Class T = (N₁N₂/N_A)·T` is the minimal
number of coincidences for any semi-classical model; `N_c T` is observed.

| `N_A` (s⁻¹) | `N₁` (s⁻¹) | `N₂` (s⁻¹) | `T` (s) | `N_Class T` | `N_c T` | `(1 − α)/Δα` |
|---|---|---|---|---|---|---|
| 4 720 | 2.45 | 3.23 | 15 200 | 25.5 | 6 | 8 |
| 8 870 | 4.55 | 5.75 | 17 200 | 50.8 | 9 | 14 |
| 12 100 | 6.21 | 8.44 | 14 800 | 64.1 | 23 | 8.5 |
| 20 400 | 12.6 | 17.0 | 19 200 | 204 | 86 | 12.7 |
| 36 500 | 31.0 | 40.6 | 13 200 | 456 | 273 | 11 |
| 50 300 | 47.6 | 61.9 | 8 400 | 492 | 314 | 10 |
| 67 100 | 71.5 | 95.8 | 3 600 | 367 | 291 | 5 |

- Headline (Eq. II-54): "la violation maximale est obtenue pour N_A = 8870 s⁻¹, pour la valeur du
  paramètre d'anticorrélation: α_exp ≅ 0.18 ± 0.06", with `α_exp = N_c T / N_Class T` (II-53) and
  `Δα = α/√(N_c T)` (p. 102): a Poisson error on the coincidence count alone. [A-inf, by hand: 9/50.8 ≈
  0.177 and 0.177/3 ≈ 0.059, consistent with the printed value.]
- First version (overlap circuits, not described in detail): "α_exp = 0.35 ± 0.05" (II-55); the thesis
  says its interpretation needed corrective procedures and that it cites those results "que très
  partiellement" (p. 98).
- No subtraction of accidental coincidences from `N_c T` is stated for Table II-3; true and delayed
  coincidence rates were recorded separately on overlap circuits (pp. 96, 100).

**Quantum prediction for this source.** The reference curve is not `α = 0`. With `x` the mean number of
cascades emitted during a gate (`x = wN/ξ`; `x = 1.5 × 10⁻⁵ N_A`, Eq. II-58; collection efficiency
`κ_A = (0.515 ± 0.015) × 10⁻³`, II-56), the thesis plots the theoretical `α` against `x` and `N_A`
(Fig. II-18, "DOMAINE QUANTIQUE"); the formula as written for the interferometer outputs is
`α_M.Q = x(x + 2)/(x + 1)²` (III-18, p. 149). `α → 0` only as `x → 0`.

**Counter-experiment, classical source (p. 104, Table II-4).** A photodiode driven by 3–4 ns electrical
pulses, triggered at rate `N_A`, with `p₁ = N₁/N_A` and `p₂ = N₂/N_A` set near those of the cascade
runs ("un peu inférieures à 10⁻³"). The emitted pulse "est évidemment descriptible par une intensité
classique". Observed `N_c T` against `N_Class T`:

| `N_A` (s⁻¹) | `N₁` | `N₂` | `T` (s) | `N_Class T` | `N_c T` |
|---|---|---|---|---|---|
| 4 760 | 3.02 | 3.76 | 31 200 | 74.5 | 82 |
| 8 880 | 5.58 | 7.28 | 31 200 | 143 | 153 |
| 12 130 | 7.90 | 10.2 | 25 200 | 167 | 157 |
| 20 400 | 14.1 | 20.0 | 25 200 | 349 | 341 |
| 35 750 | 26.4 | 33.1 | 12 800 | 313 | 329 |
| 50 800 | 44.3 | 48.6 | 18 800 | 798 | 840 |
| 67 600 | 69.6 | 72.5 | 12 800 | 955 | 925 |

The thesis states these "sont parfaitement compatibles avec les prédictions semi-classiques".

**Interference with the same source (§III-C, pp. 139–150).** A Mach–Zehnder interferometer, gated by
the same trigger. Raw counts are plotted (Fig. III-13: an elementary scan of 1 s per point, about 20
counts at a fringe maximum; a compilation of 15 scans, about 200); "un contraste de 99 % correspond à
un coup au minimum pour 200 coups au maximum" (p. 144). Contrasts after dark-count correction (Tables
III-2, III-3) lie between 0.981 and 0.995 for `x` from 0.061 to 1.12, with `σ` from 0.002 to 0.006 on the
ratio of gated to ungated contrast; the dark-count corrections are stated as below 0.05 for the
ungated and 0.003 for the gated contrasts (p. 141). The English abstract: "we have observed a fringe
visibility of 98 %, in perfect agreement with quantum mechanical predictions."
- The coincidence rate between the two interferometer outputs was recorded in the same runs ("tous les
  taux de comptages correspondant à l'expérience d'anticorrélation ... étaient enregistrés pendant le
  fonctionnement de l'interféromètre", p. 147; "nous avons enregistré le taux de coïncidences Ñ_c
  entre les deux sorties de l'interféromètre, pendant les portes w", p. 149), with `α̃` defined from
  fringe-averaged rates (III-16). The measured `α̃` values (pp. 150 ff.) are NOT READ. p. 147 states that
  the point at `x = 0.06` "correspond à une valeur du paramètre d'anticorrélation α = 0.11"; whether that
  value is measured or the value of III-18 at that `x` is not stated in the pages read [A-inf, by hand:
  III-18 at `x = 0.06` gives 0.1236/1.1236 ≈ 0.110].
- p. 149: "L'effet d'anticorrélation entre les deux sorties de l'interféromètre ne donne bien entendu
  aucune information sur le trajet suivi dans l'interféromètre."

**Classification.**

| Datum | Class |
|---|---|
| `N_A`, `N₁`, `N₂`, `T`, `N_c T` (Tables II-3, II-4) | raw-direct; herald-conditioned (gated) |
| `N_Class T` | derived (stated formula II-52) |
| `α_exp` = 0.18 ± 0.06 | derived (II-53), error by stated Poisson model |
| `α_M.Q(x)` and `x` from `N_A` | inferred (theory formula with fitted `κ_A ξ`, `w`) |
| Interference raw counts (Fig. III-13) | raw-direct, plotted only |
| Contrasts in Tables III-2, III-3 | inferred (dark-count corrected) |

### 2.3 Jacques et al. 2005 (open X-2 and X-1 source, same group lineage; not named in PLAN-G)

| Field | Record |
|---|---|
| Citation (Crossref) | V. Jacques, E. Wu, T. Toury, F. Treussart, A. Aspect, P. Grangier, J.-F. Roch, "Single-photon wavefront-splitting interference", *Eur. Phys. J. D* 35, 561–565 (2005), doi:10.1140/epjd/e2005-00201-y |
| Version read | arXiv 2011.12664v1 (posted 25 Nov 2020), titled "Single photon wavefront-splitting interference: an illustration of the light quantum in action", FULL. Published version NOT READ |
| Data public | Table I in the paper; a supplementary build-up movie (NOT READ). No data file |

**X-2 part.** Source: a single N-V colour centre in a diamond nanocrystal, pulsed at 532 nm, clock
triggered. Paths: the two halves of a Fresnel biprism, each to an avalanche photodiode. With `N_T`
trigger pulses, `α = N_C N_T/(N₁N₂) ≥ 1` for "any semi-classical theory of light, in which light is
treated as a wave and photodetectors are quantized". Gate 100 ns; "about 90% of the detected photons
are considered". Table I, ten sets of 10⁵ detections (≈ 5 s each), at "an identical mean number of
detected photons per pulse, below 10⁻²":
- (a) faint laser pulses: `N_C` per set 269, 212, 211, 196, 223, 221, 232, 248, 248, 219; `α` per set
  1.180, 0.937, 0.934, 0.875, 0.981, 0.982, 1.021, 1.077, 1.090, 0.970;
- (b) single-photon pulses: `N_C` per set 28, 23, 23, 28, 29, 31, 30, 32, 26, 26; `α` per set 0.132,
  0.109, 0.109, 0.133, 0.137, 0.147, 0.142, 0.152, 0.124, 0.123.
- Summary: "α = 1.00 ± 0.06 for faint laser pulses and α = 0.13 ± 0.01 for single-photon pulses", "with
  a 95% confidence interval". `α ≠ 0` is attributed to "remaining background fluorescence of the sample
  and to the two-phonon Raman scattering line". `N_T` per set is not tabulated; it follows from the
  counting time and the repetition period, which is given as 444 ns (Fig. 3 caption) and 436 ns (text):
  an internal discrepancy of the version read.

**X-1 part (Fig. 4).** Intensified CCD in the overlap region, 1 s snapshots, "a mean number of eight
photons detected on the CCD array per snapshot"; images of 272, 2240 and 19773 photocounts at 20, 200
and 2000 s; "more than ≈ 88% of the bright pixels correspond to detections of single photons". "A
visibility of 94% can be associated to the central fringe" (from a fit). The fit uses "free space
propagation theory from classical optics", and the source states "the well-known result from Quantum
Optics that phenomena like interference, diffraction, propagation, can be computed with the classical
theory of light even in the single-photon regime". The anticorrelation and the fringes are taken in
**separate runs** ("When the CCD is removed, it is then possible to demonstrate the single photon
behaviour"). No one-path pattern is reported.

| Datum | Class |
|---|---|
| `N₁`, `N₂`, `N_C`, counting time (Table I) | raw-direct; clock-conditioned gates |
| `α` per set; 1.00 ± 0.06, 0.13 ± 0.01 (95 %) | derived (stated formula); error at 95 % |
| Photocount images | raw-direct, shown as images only |
| 94 % central-fringe visibility | inferred (fit) |

### 2.4 Thorn et al. 2004 (undergraduate anticorrelation experiment)

*Am. J. Phys.* 72(9), 1210–1219 (2004), doi:10.1119/1.1737397 (Crossref). NOT READ (closed; the
institutional repository copy returned HTTP 403).

## 3. X-1: single-particle fringe build-up

| Source | Citation (Crossref) | Read status | What is recorded |
|---|---|---|---|
| Tonomura et al. 1989 | A. Tonomura, J. Endo, T. Matsuda, T. Kawasaki, H. Ezawa, "Demonstration of single-electron buildup of an interference pattern", *Am. J. Phys.* 57(2), 117–120 (1989), doi:10.1119/1.16104 | ABSTRACT (Crossref JATS abstract). Full text NOT READ (closed) | Abstract: "a kind of two-slit interference experiment using an electron microscope equipped with an electron biprism and a position-sensitive electron-counting system"; it "recorded the actual buildup process of the interference pattern with a series of incoming single electrons in the form of a movie". Numbers NOT READ. The interferometer is a biprism, not two slits (also stated by Bach et al. below) |
| Arndt et al. 1999 | M. Arndt, O. Nairz, J. Vos-Andreae, C. Keller, G. van der Zouw, A. Zeilinger, "Wave–particle duality of C60 molecules", *Nature* 401(6754), 680–682 (1999), doi:10.1038/44348 | ABSTRACT (nature.com). Full text NOT READ (closed) | Abstract: "the observation of de Broglie wave interference of C60 molecules by diffraction at a material absorption grating". The abstract describes a grating, not two slits, and does not describe single-detection build-up; detection method and numbers NOT READ |
| Bach et al. 2013 (open; not named in PLAN-G) | R. Bach, D. Pope, S.-H. Liou, H. Batelaan, "Controlled double-slit electron diffraction", *New J. Phys.* 15, 033018 (2013), doi:10.1088/1367-2630/15/3/033018 | FULL (arXiv 1210.6243v1, 22 Oct 2012). Published version (open access) NOT READ | below |
| Jacques et al. 2005 | §2.3 | FULL (arXiv) | §2.3 |

**Bach et al. 2013.** 600 eV electrons; two 50 nm slits, 280 nm centre separation; a movable mask 230 µm
behind the double slit selects slit 1, slit 2 or both; detection by microchannel plate, phosphor screen
and CCD. For the one-slit and two-slit patterns, "the images were summed up by adding each frame's
intensity, then normalized": each pattern is **separately normalized**, so no per-incident-electron
comparison of `P₁`, `P₂`, `P₁₂` is reported. The single-slit patterns show residual double-slit
structure from partial mask transmission ("weak double-slit diffraction can be seen in the negative
first order", and in the positive first order for `P₂`). Build-up with both slits open only: detection
rate about 1 Hz; Fig. 3 shows 2, 7, 209, 1004 and 6235 electrons; final build-up about 2 hours.
Supplementary movies (NOT READ); no data file.

| Datum | Class |
|---|---|
| Detection positions (blobs) in Fig. 3 | raw-direct, shown as images only |
| `P₁`, `P₂`, `P₁₂` images | inferred for G1's purposes (separately normalized; OCP:26 excludes such comparison) |

## 4. X-3: third-order interference

### 4.1 Sorkin 1994

| Field | Record |
|---|---|
| Citation (Crossref) | R. D. Sorkin, "Quantum mechanics as quantum measure theory", *Mod. Phys. Lett. A* 9(33), 3119–3127 (1994), doi:10.1142/S021773239400294X |
| Version read | arXiv gr-qc/9401003v2 (14 May 1994), FULL |
| Content | Theory. Defines `I_n`; the lemma `I_{n+1}(A₀, A₁, …) = I_n(A₀ ∐ A₁, …) − I_n(A₀, …) − I_n(A₁, …)`, so the `n`-th sum rule entails the `(n+1)`-th. `I₂ = 0` is "the additivity of classical measure theory"; `I₃ = 0` "defines a generalization of measure theory ... This is the level of quantum measure theory"; from it the quadratic form `|X| = I(X, X)/2` follows with `I` bi-additive (Eqs. 2–5) |
| Scope conditions stated | The three-slit sets are taken disjoint, "ignoring the possibility that the electron's trajectory winds around in such a manner as to go through both slits" (footnote). Closing slits is described as repeating the experiment "with some of the slits blocked off" |
| Statement bearing on G4 | "Given the failure of the sum rule I(A, B) = 0, it is clear that quantum probabilities cannot be interpreted in the same manner that classical ones are wont to be interpreted, in terms of (actual or fictitious) ensemble frequencies." The measure is given a preclusion reading instead |
| Raw-direct observables | None (theory). The paper proposes the three-slit sum as a "null test" |

### 4.2 Sinha, Couteau, Jennewein, Laflamme & Weihs 2010

| Field | Record |
|---|---|
| Citation (Crossref) | U. Sinha, C. Couteau, T. Jennewein, R. Laflamme, G. Weihs, "Ruling Out Multi-Order Interference in Quantum Mechanics", *Science* 329(5990), 418–421 (23 Jul 2010), doi:10.1126/science.1190545. Crossref lists no update or erratum |
| Version read | arXiv 1007.4193v1 (23 Jul 2010), FULL. Published version and the online supporting material (Methods, Fig. S1) NOT READ |
| Data public | No data file in the version read; supporting material NOT READ |

**Measured.** All eight slit combinations, including `p₀` (all closed), at fixed detector positions
(a multimode fibre of 62.5 µm core, movable along the pattern, ~180 mm from the slits); slits 30 µm wide,
100 µm apart (per De Raedt et al., §4.3, and Sawant et al., Fig. 3 caption; the version read refers to
its Fig. 1 for the dimensions); a static slit mask and a moving blocking mask, "thus eliminating any
dependence on the slit properties". `ε = p_ABC − p_AB − p_AC − p_BC + p_A + p_B + p_C − p₀` (Eq. 4) and
`κ = ε/δ` (Eq. 5), with `δ = I_AB + I_BC + I_CA` (Eq. 6), described in the text as "the sum of the
absolute values of the double slit interference terms" (Eq. 6 as printed shows no absolute values).
"κ is independent of the total particle flux onto the slits as long as it is constant in time." The
order of the eight combinations "was chosen randomly"; "up to 100 runs were cycled"; with the heralded
source, "we measured at each slit combination until the trigger count reached 30 million".

**Sources and regimes.** (i) Laser at microwatts with a power meter; (ii) laser attenuated to ~200 fW
with an APD; (iii) heralded single photons from down-conversion (~40000 photons/s), detections
"conditioned on the detection of a trigger photon". APD count rates kept below 100,000/s because
dead-time saturation "does not follow the square law, but has a deviation potentially
indistinguishable from a violation of Born's rule".

**Numbers** (central maximum of the three-slit pattern):
- Fig. 3 caption: power meter `κ = 0.0073 ± 0.0018`; attenuated laser, APD `κ = 0.0034 ± 0.0038`; heralded
  single photons `κ = 0.0064 ± 0.0119`. The text gives the last as `0.0064 ± 0.0120`: an internal
  discrepancy of the version read. Error bars from the Allan variance.
- Systematic errors, stated separately: a blocking-mask fault shifted opening B by 8 µm in the BC
  combination; an FDTD estimate of ±3 % transmission change gives `|κ| = 0.01`; power-meter
  nonlinearity 0.5 % gives `|κ| = 0.003`. Conclusion: "our particular setup enables us to bound the
  measurements of κ to better than 0.01"; "less than 10⁻² of the regular expected second order
  interference, at several detector positions".
- Values of `p_A`, `p_AB`, `δ` and the patterns: not reported in the main text (Fig. S1 NOT READ).

**Statements on the reference and on classical waves.** "The non-zero interference term I_AB is
expected in all wave theories including quantum mechanics"; `I_ABC` "will be zero in all wave theories
with a square-law relation between the field energy (or probability density) and field amplitude,
which is the case in quantum mechanics with Born's rule." "If δ = 0, then ε = 0 trivially and one deals
with classical probabilities instead of quantum behaviour."

| Datum | Class |
|---|---|
| Counts or powers per combination, `p₀` | raw-direct; not reported in the main text |
| `κ` values with errors | derived (stated formula); random error only |
| `|κ| < 10⁻²` | inferred (bound including estimated systematics) |

### 4.3 What exact solutions give for `I₃` (theory; bears on the declared reference and on PC-wave)

| Source | Citation (Crossref) | Version read | Statement |
|---|---|---|---|
| De Raedt, Michielsen & Hess 2012 | "Analysis of multipath interference in three-slit experiments", *Phys. Rev. A* 85, 012101 (2012), doi:10.1103/PhysRevA.85.012101 | arXiv 1112.2665v1, SECTIONS (§§I–V read; remainder NOT READ) | FDTD solutions of Maxwell's equations: for slits λ wide and 3λ apart in a steel plate, `Σ(θ)` "takes values in the 0.5% range"; for an idealized two-dimensional version of Sinha's device, "κ(θ = 0) = 4 × 10⁻⁵ and κ(θ) < 7 × 10⁻⁵, a factor 100 smaller than the values measured in the experiment". In the scalar Fraunhofer regime `Δ(θ) = 0` exactly (Eq. 7). "There is no theorem in Maxwell's theory that relates the solutions for the case ε(r, OOO) to solutions for the cases ε(r, COO) ... ε(r, OCC)", and "this general argument applies to the Schrödinger equation as well". OpenAlex lists a second arXiv record, 1103.0121 ("Multi-order interference is generally nonzero"), carrying the same DOI; it was not read |
| Sawant, Samuel, Sinha, Sinha & Sinha 2014 | "Nonclassical Paths in Quantum Interference Experiments", *Phys. Rev. Lett.* 113, 120406 (2014), doi:10.1103/PhysRevLett.113.120406 | arXiv 1308.2022v2, SECTIONS (abstract, introduction, results, conclusion) | Path-integral estimate, thin-slit approximation: "the wave function at the screen with both slits open is not exactly equal to the sum of the wave functions with the slits individually open"; "The three scenarios represent three different boundary conditions"; for Sinha's parameters `κ` at the central maximum is "of the order of 10⁻⁶"; for a 4 cm microwave arrangement, `10⁻³`. Sinha 2010's set-up "was not sensitive to a theoretically expected non-zeroness in κ due to systematic errors" |

**Further X-3 experiments named in the sources read** (all NOT READ): Söllner et al., *Found. Phys.* 42,
742–751 (2012); Park, Moussa & Laflamme, *New J. Phys.* 14, 113025 (2012) (NMR).

## 5. PC-wave on X-4 and X-5: what the sources read state

G1 §7.2 records PC-wave as *unknown* on X-4 and X-5 (OCP:38). G3 looked for first-hand statements of a
classical-field law for the marker-based `K` (X-4) and for the sorted two-photon coincidences (X-5).

- **X-4.** No source read derives `K` (G1 §2.4's statistic) for a classical field with a marker. What was
  found:
  - Schwindt 1999 (§1.3): the count rates are "proportional to the intensities of the corresponding
    classical electromagnetic field"; the data were taken with attenuated laser, filtered lamp and
    diode-laser sources whose photon statistics are not measured in the paper; `K` and the trajectory
    are called concepts "alien to classical electrodynamics".
  - Eberly, Qian & Vamivakas 2017, "Polarization coherence theorem", *Optica* 4, 1113 (2017),
    doi:10.1364/OPTICA.4.001113 (Crossref), read FULL as arXiv 1712.10046v1: for classical fields
    `V_F² + D_F² ≤ 1` by the Schwarz inequality and `P_F² = V_F² + D_F²` (Eq. 10), with
    `D_F = |I_a − I_b|/(I_a + I_b)`, an intensity imbalance of the two slits (a predictability-type
    quantity), not a marker-based distinguishability. A reply, *Optica* 6, 831 (2019),
    doi:10.1364/OPTICA.6.000831, exists (Crossref); the comment it answers and the reply were NOT READ.
  - De Zela, *Phys. Rev. A* 89, 013845 (2014) (Crossref title "Relationship between the degree of
    polarization, indistinguishability, and entanglement"), cited by Eberly et al.: NOT READ (closed).
- **X-5.** No source read states a classical-field bound or a classical model for the sorted
  coincidence fringes of Kim 2000, Walborn 2002 or Ma 2013. Ma 2013 (re-opened for this question only,
  arXiv 1206.6578v2) states the bipartite inequality `I² + V² ≤ 1` (Eq. 3) "which is an extension of the
  single-particle complementarity inequality" and reports polarization-correlation visibilities of
  98.0 % (H/V) and 96.9 % (R/L) without background subtraction (LIT 1.8); it gives no separability or
  classical bound. Schwindt's single-photon sorting eraser (Fig. 4) was realized with the classical
  sources of §1.3, at single-detector level with the marker on the same photon.

So PC-wave's X-4 and X-5 entries remain open on the record read; §6 states what G5 can do with this.

## 6. The data side of the §7.2 separations: what G5 can test

For each member of `𝒦` and each listed observable, the table states which measured observable bears
on the separation, at what stated precision, and its read status. No entry says that a separation
holds.

| Member | Observable | Data read first-hand | Precision as stated | Gaps |
|---|---|---|---|---|
| C0 | additivity defect `Δ` per incident particle (G1 §7.1) | Sinha 2010 measured all one-, two- and three-slit combinations and `p₀` at fixed positions, randomized order, flux assumed constant, so `I_AB = p_AB − p_A − p_B + p₀` is formable in its data | `δ` not reported; `κ = ε/δ` is reported, so `δ ≠ 0` in the analysed data [A-inf] | per-combination counts in the supporting material, NOT READ; normalization per trigger count (heralded) or per integration time (laser), not per incident particle; Bach 2013's `P₁`, `P₂`, `P₁₂` are separately normalized, so `Δ` is not formable from it |
| C0 | X-1 build-up | Jacques 2005 (272 / 2240 / 19773 photocounts), Bach 2013 (2 / 7 / 209 / 1004 / 6235 electrons) | images only; Jacques's 94 % visibility is a fit | no one-path pattern at the same normalization in either; Tonomura and Arndt ABSTRACT only. Whether X-1 without one-path data separates C0 is G1 §7.4's open point and is not decided here |
| PC-wave | X-2, `α` against `α ≥ 1` | Grangier thesis Table II-3: `α_exp = 0.18 ± 0.06` at `N_A = 8870 s⁻¹` (`N_c T = 9`, `N_Class T = 50.8`, `T = 17 200 s`), with six further rows; Jacques Table I: `α = 0.13 ± 0.01` | GRA: 1σ, Poisson on `N_c T` only; Jacques: 95 % interval | EPL text NOT READ; both herald- or clock-conditioned; the quantum prediction for the GRA source is `α_M.Q(x)`, not 0 (§2.2) |
| PC-wave | X-2 positive control on the data side | Grangier thesis Table II-4 (pulsed photodiode, `N_c T ≈ N_Class T`); Jacques Table I(a) (faint laser, `α = 1.00 ± 0.06`) | as above | — |
| PC-wave | X-1, X-3 | Sinha: "zero in all wave theories with a square-law relation"; Jacques: interference "can be computed with the classical theory of light even in the single-photon regime"; Sinha's power-meter run is a classical-intensity measurement of `κ` | `κ` bounds as in §4.2 | the sources state the classical wave reproduces these; nothing read contradicts G1's "do not separate" |
| PC-wave | X-4 | Schwindt 1999 (§1.3) | — | no classical derivation of `K` read (§5) |
| PC-wave | X-5 | Kim, Walborn, Ma (LIT) | Ma: `I(i) = 0.955(7)`, `V(ii) = 0.951(18)` (LIT 1.8) | no classical bound stated in any source read (§5) |
| CC4, CC5 | marker-protocol observables within VER2's scopes | none added by G3 | — | G3 found no measured observable that the sources read present as excluding a classically correlated marker model |
| — (AW-hyb, G1 §7.2) | a joint observable: fringes and anticorrelation in the same runs | Grangier thesis §III-C: interference contrasts 0.981–0.995 and the coincidence rate between the two interferometer outputs recorded in the same gated runs | contrasts with `σ` 0.002–0.006 | measured `α̃` values NOT READ; Jacques takes the two in separate runs; GRA EPL abstract: "The same source and detection scheme" |

**X-3 against the declared reference.** Measured: `|κ| < 10⁻²` (Sinha). Reference in G1 §7.4: `I₃ = 0`.
Exact-solution estimates, both below the measured bound: `~10⁻⁶` (quantum path integral, Sawant) and
`~4 × 10⁻⁵` (classical Maxwell, De Raedt) for Sinha's geometry. At the stated precision X-3 does not
distinguish the idealized reference, these corrections, or the linear-regime PC-wave.

**X-4 raw level (NC-rep, G1 §7.1).** Not possible from the version read: Schwindt's Max and Min rates
and the signal rate are not reported (§1.1).

## 7. Findings and assumption-watch markers (§A.31)

**Productivity test, fixed before the walk:** an item is a gem if it is strictly stronger than the
obvious restatement and either constrains (γ)'s comparisons or exposes an assumption in G1's
definitions. Favourable readings were pressure-tested: G3-F3 (the X-2 reference) was checked against
the source's own error and prediction, and G3-F4 against both the quantum and the classical
exact-solution literature, so that neither side is credited from one source.

| # | Finding | Check | Class |
|---|---|---|---|
| G3-F1 | Schwindt 1999 (arXiv v1) reports no Max or Min count rates, no signal rate and no integration time; equal source intensity across its two blocked runs is not stated. G1's raw-level NC-rep comparison and its T-block equal-flux check cannot be made from the version read | §1.1, §1.2 | CONFIRMING (G1 §5.4, §7.1 anticipated the gap); published version NOT READ |
| G3-F2 | The only FULL-read X-4 datum (Schwindt) was taken with attenuated laser and filtered thermal sources whose photon statistics are not measured in the paper, and the paper states that its count rates are proportional to classical intensities | §1.3 | NEW: exposes the assumption that X-4 data are single-quantum data; bears on PC-wave's X-4 entry and on any (s1) separation G5 might seek there |
| G3-F3 | The X-2 quantum prediction for the GRA source is `α_M.Q = x(x + 2)/(x + 1)²` with `x` set by the trigger rate, not `α = 0`; Jacques attributes `α ≠ 0` to background. G1 §7.4's declared reference ("a single excitation ... α = 0") is the `x → 0` idealization | §2.2, §2.3 | NEW: a comparison of a reference or native law with these data needs the source-specific reference and conditioning (herald- or clock-gated) |
| G3-F4 | Both `I₃ = 0` statements in G1 §7.2 (reference and linear PC-wave) rest on identifying the closed-slit amplitudes as parts of the open-slit amplitude. Quantum (Sawant) and classical (De Raedt) exact-solution analyses treat each slit configuration as a different boundary-value problem and give nonzero `κ` (`~10⁻⁶`, `~4 × 10⁻⁵`), below the `10⁻²` data bound | §4.1–§4.3 | NEW as cross-propagation: the external literature on X-3 meets the same structure as H-3 and G1's O11 stop (closing a slit changes the problem, not a setting); assumption-watch marker AW-bc |
| G3-F5 | The sources state uncertainty in different forms: GRA Poisson on one count (1σ), Jacques 95 % intervals, Sinha random error (Allan variance) with systematics as a separate bound. G1 §5.7's "σ the source's stated standard uncertainty" does not say which to use when random and systematic parts are stated separately; with Sinha's random error alone the power-meter `κ = 0.0073 ± 0.0018` lies about 4σ from 0 [A-inf, by hand], within the stated systematic bound | §2.2, §2.3, §4.2 | NEW: a hidden choice inside `κ_cmp`; assumption-watch marker AW-σ, for G5 to settle before any X-3 comparison |
| G3-F6 | Among sources read, only Sinha 2010 has one-path and two-path data at the same settings, but its per-combination values are in supporting material not read; Bach 2013's patterns are separately normalized | §3, §4.2 | ELABORATING: C0's `Δ` remains without a read number |
| G3-F7 | The Grangier thesis records interference and the anticorrelation between the interferometer outputs in the same gated runs (values NOT READ) | §2.2 | BORDERLINE: a candidate joint observable for AW-hyb; its values are unread and the source states it carries no path information |
| G3-F8 | Data-side positive controls for PC-wave exist in the X-2 sources: a pulsed photodiode (GRA, Table II-4) and faint laser pulses (Jacques, `α = 1.00 ± 0.06`) | §2.2, §2.3 | POSITIVE: the classical control is measured in the same apparatus |
| G3-F9 | Sorkin 1994 states that a measure with `I₂ ≠ 0` cannot be read as ensemble frequencies, and offers a preclusion reading | §4.1 | BORDERLINE; pointer for G4 (κ-ens, H-ens), no reading adopted |

**Cross-propagation.** AW-bc applies wherever a sum rule compares slit configurations (C0's `Δ`, X-3,
Deletion control). AW-σ applies to every quantitative comparison under `κ_cmp`. G3-F2 applies to every
use of Schwindt's data (D-1, AC-1's coverage half, MR-1's T1).

## 8. Read-status summary

| Item | Status |
|---|---|
| Schwindt, Kwiat & Englert 1999 | FULL (arXiv v1); re-read for §1 |
| Grangier, Roger & Aspect 1986 (EPL) | ABSTRACT |
| Grangier 1986 thesis | SECTIONS (pp. 59–64, 94–110, 139–150, front matter) |
| Jacques et al. 2005 | FULL (arXiv 2020 posting) |
| Thorn et al. 2004 | NOT READ |
| Tonomura et al. 1989 | ABSTRACT |
| Arndt et al. 1999 | ABSTRACT |
| Bach et al. 2013 | FULL (arXiv v1) |
| Sorkin 1994 | FULL (arXiv v2) |
| Sinha et al. 2010 | FULL (arXiv v1); supporting material NOT READ |
| De Raedt, Michielsen & Hess 2012 | SECTIONS (arXiv 1112.2665v1, §§I–V) |
| Sawant et al. 2014 | SECTIONS (arXiv 1308.2022v2) |
| Eberly, Qian & Vamivakas 2017 | FULL (arXiv v1) |
| Ma et al. 2013 | FULL in LIT; re-opened for §5 only |
| De Zela 2014; Söllner 2012; Park 2012; Kwiat–Schwindt–Englert 1999 (AIP CP461) | NOT READ |

## 9. Off-`main` references traced (§A.42 item 8)

| Reference | Claim it is attached to here | Classification |
|---|---|---|
| G1 r4 at `6ab9515d` | the targets, typing, classes, ceiling, reference and the "For G3" list this note answers | support off `main` (gap); G1 r3 accepted, #1169 c.6892563291 |
| PLAN-G at `6ab9515d` | X-list and named sources | support off `main` (gap); plan not reviewed |
| LIT r3 at `6ab9515d` | items not re-read (Kim, Walborn, Ma numbers, Dürr) | support off `main` (gap); reviewed |
| #1305 body | authorization and unit scope | provenance and governance |
| External sources (§§1–5) | every quoted number | external literature at the stated read status |

This note is off `main` and unreviewed. Nothing here authorizes G4, G5, a calculation or any change of
Issue, plan or manuscript.
