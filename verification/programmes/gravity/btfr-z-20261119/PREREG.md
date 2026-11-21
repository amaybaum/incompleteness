# BTFR-z: preregistration of the high-redshift baryonic Tully–Fisher test of a₀(z) = cH(z)/6

**Unit:** BTFR-z (P3), #873. **Authorization:** owner decision `amaybaum`, 2026-11-19T22:21:00Z,
#1169 comment 7023834853, item 3 row "P3 BTFR-z (#873): Fix in advance the high-redshift test, the
observational selection, the uncertainties and the competing predictions (§A.24 raw versus inferred
data)". Investigation only: no manuscript edit, no premise adopted, no merge.

**Goal link (§A.47).** Serves the second half of the §A.29 target (how vacuum energy gravitates),
through the G3 item of #873. The test decides whether the redshift extension a₀(z) = cH(z)/6 of the
conditional radial law in `papers/GR.md` §7.3 survives the published z ≈ 0.9–2.3 baryonic
Tully–Fisher (BTFR) data at the stated precision. It does not decide G3, the z = 0 value of a₀, or
the radial law itself.

**Freeze.** This file, `scripts/oi_model.py` and `data/` are committed and pushed before any
statistic in §5 is computed from the data. The analysis script written afterwards implements this
file; where it and this file differ, this file governs and the difference is reported in
`RESULT.md`.

***

## 0. Disclosure of what was read before this freeze

To choose the data and the controls, the author read the published fit results of the sources used
here. In particular:

- Übler et al. (2017, ApJ 842, 121; arXiv:1703.04321) Table 2 and §4.2: fixed-slope (a = 3.75) BTFR
  zero-points b = 10.68 ± 0.04 (z ~ 0.9, 65 galaxies) and 10.85 ± 0.05 (z ~ 2.3, 46 galaxies) at
  v_ref = 242 km/s, offsets Δb = −0.44 and −0.27 dex from the Lelli et al. (2016a) accurate-distance
  relation, and −0.33 and −0.09 dex without the pressure-support correction (§5.4).
- Lelli et al. (2016a, ApJL 816, L14) fits: s = 3.71 ± 0.08, log A = 2.27 ± 0.18 (118 galaxies);
  s = 3.75 ± 0.11, log A = 2.18 ± 0.23 (58 accurate-distance galaxies).
- Lelli et al. (2019, MNRAS 484, 3267) Table 2: V_f: s = 3.85 ± 0.09, I = 1.99 ± 0.18;
  V_max: s = 3.52 ± 0.07, I = 2.59 ± 0.15; and log V_f = 0.95 log V_max + 0.08.

The published z ~ 0.9 and z ~ 2.3 zero-points imply a between-epoch difference of +0.17 dex. The
headline statistic T2 (§5) was chosen with that number known. Its justification is structural,
not result-driven: T2 is the only statistic in which the local-anchor systematics (velocity
definition, local Υ★ and distance scale, local gas definition) cancel. To keep the choice from
biasing the verdict against OI, (i) T1 against the local anchor is reported in full beside it,
(ii) OI's headline verdict is the *least* severe of its prediction variants (§7), and (iii) the
forward-modelled OI prediction for T2 (§2.2) was computed and is frozen below before T2 was
computed from the data.

***

## 1. The claim under test, its derivation and its status

`papers/GR.md` (last changed `b023b92d`, 2026-11-19), §7.3:

- Status (GR:510, quoted exactly): "**Epistemic status.** Steps 1–3 are Tier 2 and conditional: the
  displacement formula follows from the Clausius relation applied to the boundary reservoir (§3.2)
  and therefore inherits the conditions on $T_{\rm dS}$ together with the local assumption
  $Q = M_Bc^2$; the dimensional factor is imported (Step 2); given these, $a_0 = cH/6$ and
  $v^4 = GM_B \cdot cH/6$ contain no fitted parameter. The interpolation constraints (i)–(v) are
  Tier 2 on the same conditions; the transition steepness is Tier 3 (solution-specific)."
- Redshift extension (GR:512, opening, quoted exactly): "**Redshift evolution.** On extending the
  conditional radial law to the supplied flat cosmological background, $a_0(z) = cH(z)/6$ and
  $H(z) = H_0\sqrt{\Omega_m(1+z)^3 + \Omega_\Lambda}$, so the critical acceleration increases with
  redshift: $a_0(z=1) = 1.79\,a_0(0)$, $a_0(z=2) = 3.03\,a_0(0)$, $a_0(z=3) = 4.57\,a_0(0)$."
- The tension already noted (GR:516, quoted exactly): "**Tully-Fisher evolution.** McGaugh et al.
  (2024), analyzing Nestor Shachar et al. (2023) JWST kinematics, present the *baryonic*
  Tully-Fisher relation out to $z \sim 2.5$ and find no clear indication of evolution, noting
  unresolved differences between samples in the definition of baryonic mass and in the velocity
  measured. The baryonic relation is the direct test of $v_{\text{flat}}^4 = GM_B \cdot cH(z)/6$: at
  fixed $v_{\text{flat}}$ the law predicts a normalization shift
  $\Delta\log M_B = \log(H_0/H(z)) = -0.48$ dex at $z = 2$. The reported absence of evolution is
  therefore in tension with the law. The tension is not yet statistically quantified: that needs
  baryonic masses with reliable ALMA gas masses, and velocities measured as the law's
  $v_{\text{flat}}$."
- GR:522, test (ii), and the GR:547 table row ("normalization comparison open").

Derivation chain (GR §7.3 Steps 1–3): Clausius displacement ΔS = M_Bc²/(k_B T_dS) on the
conditional T_dS of §3.2 (H-count, H-slope, H-frame, H-Hawking, local boost structure, symmetric
detailed balance) and the local assumption Q = M_Bc²; the factor 1/6 imported from Verlinde (2016,
eq. 1.7); deep-MOND limit g = √(g_B a₀) ⇒ v⁴ = G M_B a₀. The redshift step replaces H₀ by H(z) of a
*supplied* flat background. Classification per the audit method: C (conditional structural) for
a₀ = cH₀/6; the redshift extension inherits every condition and adds the assumption that the
horizon relevant to a galaxy at redshift z is the instantaneous Hubble horizon c/H(z).

Book mirror: `book/ch07-gravity.md` carries the radial law, the r_M(z) shrinkage and its tension
(ch07:274, :280, :300) but not the BTFR normalization shift; `book/appendix-a-prediction-status.md`
G6 carries a₀ = cH/6 only. This unit edits none of them.

***

## 2. Predictions (fixed here)

### 2.1 H(z) model and the asymptotic OI prediction

H(z) = H₀ E(z), E(z) = √(Ω_m(1+z)³ + 1 − Ω_m), flat, radiation neglected. Primary parameters:
Planck 2018 VI (A&A 641, A6), TT,TE,EE+lowE+lensing: H₀ = 67.36 km s⁻¹ Mpc⁻¹, Ω_m = 0.3153.
Cosmology band: Ω_m ∈ {0.30, 0.33}. E(z) is independent of H₀. (C5 below checks GR's 1.79, 3.03,
4.57: the code gives 1.791, 3.033, 4.568.)

a₀ enters the BTFR through the deep-MOND limit v_flat⁴ = G M_b a₀(z), so at fixed v_flat

  **P_asym(z) = Δ log M_b = −log₁₀ E(z)**  (−0.227 at z = 0.9, −0.482 at z = 2, −0.540 at z = 2.3).

For a bin, P_asym is the mean over its galaxies of −log₁₀ E(z_i).

### 2.2 Forward-modelled OI prediction at the measured velocity

The high-z velocities are peak circular velocities v_circ,max of an exponential-disk model, not
v_flat (Übler+2017 §2.3: high-z curves show no flat part). `scripts/oi_model.py` computes, for a
baryonic exponential disk of mass M and scale length R_d = R_e/1.678 under g = g_N ν(g_N/a₀), the
peak velocity within r ≤ 2.5 R_e (the typical extent of the data), and inverts it at
V_ref = 242 km/s. Variants: geometry {spherical enclosed mass (GR's convention), Freeman thin
disk} × ν {simple (GR §7.3 Step 4), RAR form 1/(1 − e^{−√y})} × H₀ {67.36, 73.0} × Ω_m {0.3153,
0.30, 0.33}. The central value is (spherical, simple, 67.36, 0.3153); the model band is half the
full range of the variants.

For T2 (z ~ 2.3 minus z ~ 0.9), with the published bin median sizes R_e = 4.8 kpc (z ~ 0.9) and
4.0 kpc (z ~ 2.3) (Übler+2017 Table 1) at nominal z = 0.9 and 2.3, the frozen output of
`python3 -I scripts/oi_model.py` is:

| Model | T2 prediction (dex) | model band |
|---|---|---|
| OI, asymptotic (P_asym) | −0.313 | ±0.003 (Ω_m) |
| OI, forward model (P_vmax) | −0.208 | ±0.011 |
| Constant-a₀ MOND, forward model | −0.058 | ±0.002 |
| Constant-a₀ MOND, asymptotic | 0 | — |

The −0.058 common to both forward models is the size difference between the bins. The analysis
re-evaluates these at the bins' median redshifts; the sizes stay as published.

### 2.3 Competing predictions

| Competitor | T1 (bin vs z = 0) | T2 (z ~ 2.3 − z ~ 0.9) | Scored? |
|---|---|---|---|
| MOND, constant a₀ | 0 (v_flat) | 0 (asym); −0.058 (forward model, §2.2) | yes |
| ΛCDM, analytic halo scaling (Mo, Mao & White 1998: M_h = V_h³/(10 G H(z)), fixed disk mass fraction m_d and V_c ∝ V_h) | −log₁₀ E(z) | −0.313 | yes; **identical in form to OI's P_asym**, so no outcome of this test separates the two |
| ΛCDM simulations / abundance matching | context only (below) | context only | no |

ΛCDM simulation predictions retrieved (none predicts the BTFR zero-point for v_circ,max of
massive star-forming disks at z ≈ 0.9–2.3 under this sample's selection, so none is scored; scoring
one would need a forward model of the simulation outputs that this unit does not have):

- EAGLE (Ferrero et al. 2017, arXiv:1607.03100, Table 2): stellar-mass TFR,
  M★ = M₀ ν^α exp(−ν^γ), ν = V_rot/50 km s⁻¹, V_rot = V_circ(r_h). Evaluated at V_rot = 242 km s⁻¹:
  log M★ = 10.885 (z = 0) and 10.620 (z = 1), a shift of −0.27 dex in *stellar* mass; the paper
  describes the evolution as weak and consistent with observations out to z = 1. No BTFR, no z > 1.
- SIMBA (Glowacki, Elson & Davé, arXiv:2011.08866): BTFR to z = 1; with the slope fixed to z = 0
  "the best-fit y-intercept slightly decreases with redshift for σ_DM and the spectral line width
  measures, while it increases in the case of V_flat" (their fixed-slope figure caption).
- Portinari & Sommer-Larsen (arXiv:astro-ph/0606531): "the stellar mass TF relation shows
  negligible evolution" between z = 0 and 1.

### 2.4 Retrodiction controls (not scored)

- **R1, free zero-point per bin.** Fits the data by construction; any rule rates it "consistent".
  Listed to show that fitted models earn nothing under the rule.
- **R2, Übler et al. (2017) toy model.** ΛCDM-motivated (MMW98 plus evolving f_gas, m_d, f_DM(R_e)),
  with f_DM(R_e, z) "tune[d] … to optimize the match between the toy model and the observed TFR
  evolution presented in this paper" (their §5). A retrodiction of these data; not scored.
- **R3, fitted exponent.** a₀ ∝ H(z)^p with p fitted from T2 (p̂ = −T2/log₁₀[E(z₂)/E(z₁)] in the
  asymptotic form). Descriptive only; p = 1 is OI and p = 0 constant-a₀ MOND. A fitted p is not a
  test of OI.

***

## 3. Data, selection and exclusions

| Role | Dataset | Source (fetched 2026-11-19) | Bytes kept |
|---|---|---|---|
| z ≈ 0 anchor (V_f) | Lelli, McGaugh & Schombert 2016a, ApJL 816, L14, data behind Fig. 2 (118 galaxies: log M_b, log V_f, errors, distance flag) | VizieR J/ApJ/816/L14/figure2 via `https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?-source=J/ApJ/816/L14/figure2&-out.max=unlimited&-out.all` | `data/lelli2016_btfr_fig2.tsv` |
| z ≈ 0 photometry, HI, geometry | SPARC (Lelli+2016b, AJ 152, 157) Table 1 | `https://astroweb.case.edu/SPARC/SPARC_Lelli2016c.mrt` | `data/SPARC_Lelli2016c.mrt` |
| z ≈ 0 rotation curves (V_max) | SPARC mass models | `https://astroweb.case.edu/SPARC/Rotmod_LTG.zip` | `data/Rotmod_LTG.zip` |
| High z | Übler et al. 2017, ApJ 842, 121, Table 3 (135 KMOS³D galaxies: z, log M★, log M_b, v_circ,max, σ₀) | VizieR J/ApJ/842/121/table3 (doi:10.26093/cds/vizier.18420121) via `https://vizier.cfa.harvard.edu/viz-bin/asu-tsv?-source=J/ApJ/842/121/table3&-out.max=unlimited&-out.all` | `data/ubler2017_table3.tsv` |

SHA-256 of the committed files:

| File | SHA-256 (file) | SHA-256 (lines not starting with `#`) |
|---|---|---|
| `Rotmod_LTG.zip` | `0a80cc90714828cc28b7dd57923576714d209f2490328c087c4a4ad607faf588` | — |
| `SPARC_Lelli2016c.mrt` | `5aa0501f6b0d881fa579030e315e7b5b6ef561a5bd3a07472f9929c7e5728243` | — |
| `lelli2016_btfr_fig2.tsv` | `d6f4e0f02be2f2ff2d0c157a4aa7542eb8d0afaf90c9522104310292b8093c1c` | `53685f8574c4afa154c6c1e7b8ac3ae722d3268734a67bada6b35d30a9e24a76` |
| `ubler2017_table3.tsv` | `551a1843395c21690adab64bd713121169b3ddb566cf3d259e08954daa7da2ae` | `91742f444278810e0fef788b1ce3512d193e35248452ad0e8184e205b1d0a5a7` |

Redaction (§A.42 item 4): each VizieR TSV, as served, carried two `#` header lines with the
service's contact e-mail address; they were removed. As served, the files hashed
`cf221153b9bb1a2f42f9912d68c78c01cd485c6181987019ae897a0ada2203f5` (Lelli) and
`8a2cf9b03ac0852ac5fcf3390cef1c3b3ef287c52aa5d438a2c0f7c6f0b40179` (Übler). VizieR headers carry the
request date, so a re-fetch matches the second column, not the first.

**Selection.**
- *Anchor, V_f:* the 58 accurate-distance galaxies of Lelli+2016a (distance flags 2 TRGB,
  3 Cepheid, 4 Ursa Major, 5 SN), the subsample Übler+2017 compared with; the 118-galaxy sample is
  used for control C1 only. Lelli's own cuts carry over: i ≥ 30°, flat outer rotation curve.
- *Anchor, V_max:* the same 58 galaxies; V_max = maximum of V_obs in the SPARC mass-model file;
  σ(V_max) = √(errV² + (V_max δi / tan i)²) with SPARC's i and δi; log M_b from the Lelli table.
- *High z:* all 135 galaxies of Übler Table 3 (their selection: modelled, peak velocity reached,
  v_rot,max/σ₀ > √4.4, no close neighbours). Bins by Hα band: z < 1.2 (YJ), 1.2 ≤ z < 1.9 (H),
  z ≥ 1.9 (K); the counts must be 65/24/46 (C2). The H bin (z ~ 1.5) is reported but not used in
  any verdict (the source paper does not fit it). No galaxy is removed.
- *Excluded before computation:* RC100 (Nestor Shachar+2023): its per-galaxy table is an image in
  the arXiv PDF and no machine-readable table was found; its baryonic masses are kinematic-fit
  parameters fitted to the same rotation curves (circular for a BTFR test); its velocities are at
  R_e. Genzel+2017/2020: no per-galaxy BTFR table retrieved; RC41 overlaps RC100. KROSS (Tiley+2019),
  ZFIRE (Alcorn+2017), Miller+2011: stellar masses only. McGaugh+2024: not retrieved. One high-z
  sample (KMOS³D, one instrument) is therefore the whole high-z evidence; this is a stated
  limitation of the result.

**§A.24 classification and comparison level.**

| Quantity | Class | Pipeline |
|---|---|---|
| Hα line-of-sight velocity and dispersion profiles (KMOS) | raw/direct | — |
| HI velocity fields, [3.6] flux, HI flux (SPARC) | raw/direct | — |
| v_circ,max (high z) | inferred | forward dynamical model: beam smearing, inclination from axis ratio with q₀ = 0.25, thick exponential disk, pressure-support term 2σ₀²(r/R_d) |
| V_f, V_max (z ≈ 0) | inferred, close to raw | inclination-corrected tilted-ring rotation curve |
| M★ (high z) | inferred | SED fit, BC03, Chabrier IMF, solar metallicity; D_L from an assumed flat ΛCDM (H₀ = 70, Ω_m = 0.3) |
| M_gas (high z) | inferred, not measured per galaxy | Tacconi+2017 depletion-time scaling relation in z, ΔMS, M★, R_e; molecular only |
| M_b (z ≈ 0) | inferred | 0.5 L[3.6] + 1.33 M_HI; molecular gas neglected |

No raw-level BTFR exists: every BTFR comparison here is between inferred masses at inferred
velocities. The comparison is therefore made at the level the sources publish (log M_b at fixed
velocity), with the inference chain carried as the systematic budget of §6, and every verdict is
conditional on that chain. In particular the high-z baryonic masses rest on a gas *scaling
relation*, not on per-galaxy gas measurements, and the high-z distance scale uses a ΛCDM
background (the same supplied background OI uses for H(z)).

***

## 4. Fitting

- Relation: log M_b = s log₁₀(v / 242 km s⁻¹) + b (v_ref = 242 km s⁻¹ as in Übler+2017).
- Anchor fits (free slope): generalized least squares with errors on both axes and vertical
  intrinsic scatter ζ, weights 1/(σ_y² + s²σ_x² + ζ²), ζ set so that χ²/(N − 2) = 1 (ζ = 0 if
  χ²/(N − 2) < 1 already); slope and intercept by iterated weighted least squares to convergence
  (|Δs| < 10⁻⁸). No outlier clipping.
- High-z fits (slope fixed to the anchor slope): b = Σw(y − s x)/Σw with the same weights,
  ζ set so that χ²/(N − 1) = 1.
- High-z per-galaxy errors: σ(log M★) = 0.15 dex and σ(log M_gas) = 0.20 dex (Übler §2.2),
  combined in linear mass with M_gas = M_b − M★; σ(v) = 20 km s⁻¹ (Übler §5.3.2 median).
- Statistical errors: bootstrap over galaxies, 2000 resamples, `numpy.random.default_rng(20261119)`.
- Deterministic: fixed seed, no timestamps in outputs; `results.json` is the structured output.

## 5. Statistics

- **T1(bin) = b_bin − b_anchor(242)**, the zero-point offset of a high-z bin from the z ≈ 0 anchor
  at fixed velocity, slope fixed to the anchor's. Central value with the V_f anchor (the law's
  velocity and the anchor Übler used); the V_max anchor enters through σ_vdef.
- **T2 = b(z ~ 2.3) − b(z ~ 0.9)**, both bins fitted with the same fixed slope (the V_f anchor's).
  T2 uses one instrument, one pipeline and one mass recipe at both epochs, and is independent of the
  local anchor except through the slope. **T2 is the headline statistic.** Slope-4 values of T1 and
  T2 are reported as a sensitivity row.

## 6. Uncertainty budget (formulae fixed here; values computed)

σ_O is the quadrature sum of the rows that apply.

| Term | T1(bin) | T2 |
|---|---|---|
| stat | bootstrap σ(b_bin) ⊕ bootstrap σ(b_anchor at 242) | bootstrap σ(b_2.3) ⊕ σ(b_0.9) |
| σ_ps, pressure support | ½·\|T1(v_rot) − T1(v_circ)\|, v_rot² = v_circ² − 4.4σ₀² | ½·\|T2(v_rot) − T2(v_circ)\| |
| σ_vdef, v_circ,max vs V_f | ½·\|T1(V_max anchor) − T1(V_f anchor)\| | 0 (same definition at both epochs) |
| σ_IMF, M★ scale (SED-Chabrier vs Υ[3.6] = 0.5) | 0.10 × median(M★/M_b) of the bin | 0.10 × \|median f★(2.3) − median f★(0.9)\| ⊕ 0.05 × mean of the two median f★ (epoch-dependent SED systematics) |
| σ_gas, gas scaling relation | 0.15 × median(M_gas/M_b) of the bin ⊕ 0.05 (atomic gas / gas-definition mismatch) | 0.10 × median f_gas(2.3) ⊕ 0.02 (Übler's atomic corrections +0.04 vs +0.02) |
| σ_incl, coherent inclination (q₀ 0.20 vs 0.25) | 0.02 | 0 |
| σ_sel, sample selection | 0.06 | 0.06 (Übler: Δb_bTFR 0.17 fiducial, 0.20 parent sample, 0.28 first-order) |
| σ_dist, local distance scale | 0.04 | 0 |
| σ_H0, high-z D_L (H₀ = 70 assumed) | 0.03 | 0 |

The prediction band σ_P of each model is that of §2 (model variants and Ω_m).

## 7. Decision rule

For model m with prediction P_m ± σ_P and observation O ± σ_O:

  z_m = |O − P_m| / √(σ_O² + σ_P²);  **consistent** if z_m ≤ 2, **in tension** if 2 < z_m ≤ 3,
  **excluded** if z_m > 3.

- Applied identically to OI (P_asym and P_vmax), constant-a₀ MOND (asym and forward model) and the
  ΛCDM halo scaling, for T2 and for T1 at z ~ 0.9 and z ~ 2.3.
- **OI headline verdict** = the T2 verdict of the *less* severe of OI's two predictions (P_asym,
  P_vmax). OI is excluded on T2 only if both are excluded. T1 verdicts are reported beside it; if T1
  and T2 disagree, both are stated and no single verdict is drawn from T1.
- **Sensitivity.** If |P_OI − P_MOND| < 2 σ_O (for the matching prediction pair), a "consistent"
  verdict for either is reported as "consistent, non-discriminating". "In tension" and "excluded"
  stand regardless.
- **Favourable branch.** If OI is consistent and constant-a₀ MOND is excluded, the result is
  favourable to OI and to the ΛCDM halo scaling equally, and requires a skeptical pass (§A.31)
  before it is stated anywhere else.
- **Voiding.** A verdict prints only over green controls (§8). C1 and C2 failing voids T1; C2 or C3
  failing voids T2; C5 or C6 failing voids every OI verdict. Void verdicts are printed as "VOID" with
  the failed control named.
- Verdict text in `RESULT.md` is generated by the script from `results.json`.

## 8. Controls (pass criteria fixed here)

- **C1, z ≈ 0 zero-point (anchor reproduction).** Fitting the Lelli+2016a table with §4's method:
  slope within 1σ of the published value and log M_b at 242 km s⁻¹ within 0.05 dex of the published
  relation's, for both the 118-galaxy sample (s = 3.71 ± 0.08, log A = 2.27) and the 58-galaxy
  sample (s = 3.75 ± 0.11, log A = 2.18). C1b: log(0.5 L[3.6] + 1.33 M_HI) from the SPARC table
  matches the Lelli table's log M_b with median |difference| ≤ 0.02 dex. C1c (V_max anchor): the
  58-galaxy V_max fit gives log M_b at 242 km s⁻¹ within 0.10 dex of Lelli+2019's V_max relation and
  slope within 2σ of 3.52 ± 0.07.
- **C2, published high-z offset (Übler+2017).** Band counts 65/24/46; with s = 3.75 fixed:
  b = 10.68, 10.85 and 10.75 (all 135) within 0.03 dex; bootstrap σ within 0.02 of 0.04, 0.05, 0.03;
  Δb versus the published Lelli 58-galaxy relation = −0.44 and −0.27 within 0.03; without the
  pressure-support correction (v_rot) Δb = −0.33 and −0.09 within 0.04.
- **C3, injection–recovery.** 500 mock catalogues per injection, at the observed velocities and
  redshifts: log M_mock = b_anchor + s log(v/242) + δ + N(0, √(σ_y² + s²σ_x² + ζ_bin²)), with
  δ = 0 (constant a₀) and δ = P_asym(z_i) (OI). Pass: the mean recovered T1 (both bins) and T2 lie
  within 0.02 dex of the injected values, and the standard deviation of recovered T2 lies within a
  factor 1.5 of the data's bootstrap σ(T2). Reported, not pass/fail: the fraction of δ = 0 mocks in
  which the rule (stat-only σ) classifies OI-asym as excluded on T2 (the power of the test against OI).
- **C5, exactness.** E(1), E(2), E(3) reproduce GR's 1.79, 3.03, 4.57 to two decimals.
- **C6, forward-model limits.** Deep-MOND limit: forward shift equals −log₁₀ E(2) within 0.01 dex;
  Newtonian limit: forward shift within 0.01 dex of 0. Bessel approximations within 10⁻⁶ of
  reference values. (At freeze: −0.4815 vs −0.4818; −0.0045; 4 × 10⁻⁸.)

## 9. Recipe

```
python3 -I verification/programmes/gravity/btfr-z-20261119/scripts/btfr_z.py
```

writes `results.json` and `RESULT.md` beside this file and exits non-zero if a data hash does not
match §3. The expected output values are recorded in `RESULT.md` after the run.
