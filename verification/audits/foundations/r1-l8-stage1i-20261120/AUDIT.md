# R1-L8 Stage 1(i) — which horizon entropy supplies the normalization

**Status.** Writer's paper-only provenance audit, WIP / UNVERIFIED; revised after the independent
review of `e98cca04` (REVISE, minor; PR #1457, round 1), answered in §13. Classes, tests, decision rule and
controls were fixed in `PREREG.md` (commit `7dcd0799`, pushed before this file). Existing evidence
only: no law constructed, no hypothesis adopted or dropped, no manuscript, Lean or registry edit, no
conditional result promoted. A1 remains open and unadopted. Independent non-author review is
required before any use; the unit stops after that review.

**Authorization and goal link.** As in `PREREG.md`: owner `amaybaum`,
[#1169 comment 7041456852](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7041456852),
2026-11-20T14:01:28Z. Goal link (§A.47): decides whether a₀, Tully–Fisher and ρ_s are derived, or
depend on an imported normalization or on R1's selected law.

**Source pin.** `main` at `371acccc9f8531465afa7fcf4b5d1262235d26d1`; site notation as PREREG.
Algebra marked [W] re-reads displayed formulas exactly (K5); external literature is marked [LIT].

## 1. Verdict (generated from §3)

**Which entropy supplies the normalization.** In every traced result the normalization that survives
in the displayed value is the Clausius normalization of horizon thermodynamics (A2: the GR first law
dE = (c²κ/8πG)dA with the KMS temperature), or the identical Bekenstein–Hawking value inside an
imported derivation (A3), or no entropy normalization at all. The state count σA/ε² (A1) supplies
none: its normalization ε²/σ is solved for from measured ħ (GR:306–308), which makes it equal to the
A2 value by construction (GR:314–318, :158); in ρ_s and the concordance it cancels identically
(GR:428–430, :440); in a₀ and Tully–Fisher no site computes with it: the displayed value is the
imported factor times cH (GR:478–482), although GR:468–478 identify the displaced reservoir with the
boundary count (§2.4).

**Per-result classes under the corpus reading A\*** (full table §3):

| Result | Class under A\* | Normalization source surviving in the value | Law-dependent under A\* (Test K) | §A.23 axis |
|---|---|---|---|---|
| R1 a₀ = cH/6 | **X (i)** | Verlinde's factor (d−3)/((d−2)(d−1)), in whose derivation the area-entropy coefficient cancels; measured H | Displayed value: no, because it is imported. OI's own mechanism: not determined (U), since the factor is not derived in OI (§2.4) | consistency (retrodiction of an imported value) |
| R2 v⁴ = GM_B·cH/6, r_M | **X (i)**; deep-regime law conditional on the proposed displacement law | as R1 | as R1 | consistency; normalization comparison open (GR:547) |
| R2z a₀(z) = cH(z)/6 and its Tully–Fisher / r_M evolution | **X (i)**, with an extension that is OI-adopted, not derived (GR:56, :512) | as R1; the H(z) scaling is OI's extension beyond exact de Sitter | as R1 | **correctness** (OI-adopted, not derived (GR:56); not fitted; in tension, GR:514–516) |
| R3 ρ_s = ρ_crit | **X (a)** | none: σ, ε, the count and the law cancel; only the first-law prefactor, the area-law form and V_H remain | No | none (identity with a quantity computed from H) |
| R4 ρ_s/ρ_crit = 2/(d−1); d = 3 filter | **X (a)**; its use as a filter is conditional on the open source identification | none (as R3, with the d-dimensional first law, V = AR/d and Friedmann) | No | consistency at most, against the inferred Ω_total (§A.24) |
| R5 ħ = c³ε²/(4Gσ) | **X (m)**, Z; named conditions H-count, H-slope, H-frame, H-Hawking, local boost, symmetric rates | ε²/σ calibrated from measured ħ | Yes, in the unobserved ε²/σ (C1.b) | none (calibration) |
| R6 ε = 2√σ l_p; ε_lat = √(6σ) l_p | **X (m)** (K3), Z; ε_lat with H-link as a named condition | measured ħ | Yes (ε² = 4kσl_p²) | none |
| R7 the 1/4 | coefficient **X (a)**; the count's equality with it **X (m)**, Z (equivalent to the calibration) | A2 (Clausius at T_KMS) | Coefficient no; count's value yes (K4) | none (no direct test, GR:320) |
| R8 N_modes = S_dS/σ | **X (m)**; named conditions as R5 | measured ħ through ε | Yes | none |
| R9 dark-sector fraction 1 − Ω_B | **X (a, m)**; conditional on the open source identification | R3's identity and the supplied Ω_B | No | consistency (partly definitional, appA:110) |
| R10 §6.3 compression ratio ρ_QFT/ρ_cl ~ S_dS | **X (a)** (GR:364 calls it a dimensional identity); the ε_lat-cutoff variant X (m) | none / measured ħ | variant only | none |
| R11 GR App. A.6–A.7 | not a normalization consumer: the theorems are stated in mode numbers; S_BH = A/(4l_p²) is a label from R7 | — | — | none |

No traced result is class D. No displayed value is U under A\*: the corpus reading of each displayed
formula is determined (§2). The law dependence of OI's own entropy-displacement mechanism is U
(§2.4), so Stage 0's D1 is resolved for the displayed value only (§6).

**Dependence on R1's selected law (decision rule 2).** Under A\*, the values of a₀, the Tully–Fisher
normalization, ρ_s = ρ_crit and the concordance do **not** depend on the shell law: for ρ_s and the
concordance because the count's normalization cancels against its own Clausius temperature; for a₀
and Tully–Fisher because the value is imported whole (Xi), not as an OI result. GR:468–478 identify
the displaced reservoir with the boundary count; were OI to derive the factor with the count as the
volume-law entropy and Step 1's Clausius displacement, a₀ would be cH/(6k) (§2.4). No site computes
that combination, so the law dependence of OI's own mechanism is not determined. The results that do depend on the law are the
calibration outputs ħ's coefficient, ε, ε_lat, N_modes and the count's equality with A/(4l_p²)
(Stage 0 C1.a–c), none of which has an observational test. The law-independence of the four
owner-named results comes with the absence of OI-native normalization: each is an external input
(Xi) or an identity of external inputs (Xa).

**Internal consistency (decision rule 4).** The corpus is consistent in *values*: A1 (calibrated),
A2 and A3 coincide under H-count with the selected uniform shell law, and GR:356 states that "the
action-scale calibration and the entropy count are one normalization". It is not consistent in
*provenance*: fifteen findings (§4, F-1 to F-15) record sites that state a source or status for
these results stronger than, or different from, what the trace supports. The most material: the 1/6 is described as arising
"from the cubic-lattice geometry" (ch09:63) while GR:482 states it is "taken over from Verlinde's
analysis rather than rederived from the substratum"; spatial flatness is described as "structurally
explained rather than fine-tuned" (ch05:59–61), and ρ_s/ρ_crit ≈ 1 is treated as an inferred
observation (Sub:88), on the strength of an identity whose source identification GR:420 leaves open; the concordance's coefficient is said to inherit H-count "through ε = 2√σ l_P"
(SM:30), although ε cancels from it.

**Circularity (decision rule 5).** Two Test Z flags, both on the calibration and both wording
(§5): the 1/4 and ε = 2√σ l_p listed as "quantitative consequences specific to" the substratum
(GR:689) or as "substrate-computable" (ch09:258); and "ħ is derived, not free, conditional on the
calibration a_*=τ_K/β_E (§2.3; Step 4) and its named conditions" (GR:108) and "derives ħ from G and
ε" (GR:160), beside "one free geometric parameter (ε)" (GR:308). No traced result calibrates a
parameter from a measurement and then predicts that measurement. ρ_s = ρ_crit is the definition of
ρ_crit re-expressed (§2.3), so presenting it as an explanation of flatness (F-6) is the closest
case.

**Correctness vs consistency (§A.23).** This audit is consistency work and moves no correctness
band. Of the traced results only R2z (the redshift evolution a₀(z) = cH(z)/6, OI-adopted, not
derived (GR:56), and not in the imported source) is a correctness-axis confrontation; it is reported in tension
with three data sets (GR:514–516, :548–549). a₀ against g_† and the Tully–Fisher normalization are
consistency-axis comparisons of an imported formula with a value known before the import.

**Stage 0 consequences (recommendations only, §6).** C1.d is "not (c)" for its displayed value,
which is law-independent because it is imported; the law dependence of OI's own mechanism is not
determined. C1.e depends on the reading: under A1a, the pairing the displayed formula GR:426–428 uses
(confirmed in review), C1.e leaves (c) and Stage 0's N_c = 7, N_c′ = 14; under A1b, the GR:58/:336
reading that Stage 0's F5 used, C1.e stays (c). Stage 0's record is not edited here.

A1 remains open and unadopted. Nothing here authorizes a successor unit or a manuscript change.

## 2. Step trace

### 2.1 Where each constant enters (common to all results)

| Constant | Where it enters | Calibrated from measurement? |
|---|---|---|
| G | parameter of the classical Hamiltonian (GR:160); first-law prefactor c²κ/(8πG) (GR:98) | measured value used as an input, not fitted to a result |
| ħ | KMS temperature T_KMS = ħκ/(2πck_B) (GR:144); T_dS (GR:472) | measured; the gap equation solves for ε²/σ from it (GR:306–308) |
| ε²/σ | count density η = σ/ε² (GR:98); T_cl (GR:100) | yes: ε/√σ = 2l_p is the gap equation at measured ħ (GR:308, Sub:179, appB:169, gloss:73, appA:117) |
| σ | entropy per mode; assumed 1 for every quoted value (GR:102) | not fixed; cancels from the 1/4, ρ_s and the concordance |
| k_B | unit conversion between T and energy; S in nats | no |
| H | κ = cH; A = 4πc²/H²; V_H; a₀ | measured H₀ (67.4 or 73, GR:480–482) |
| Ω_B, Ω_m, Ω_Λ | dark-sector fraction (GR:454); H(z) (GR:512) | supplied from the reference cosmology |

### 2.2 R5–R8: the calibration (GR §§2.3, 3, 4, 5)

1. **Classical side, A1.** GR:98–100: "Jacobson [1] showed dE = T dS … The entropy density is
   η = σ/ε² … Thus dS = σ dA/ε². Equating: T_cl = c²ε²κ/(8πGk_Bσ)." This is the Clausius
   temperature of the count through the first law (**A1a**). GR:58 obtains the same quantity as the
   counting slope of the shell law under H-count (**A1b**): "k_BT_micro = (∂s_H/∂E)⁻¹ = … = k_BT_cl".
   The two coincide only under H-count (GR:336: "T_cl of §3.1 equals the hidden-sector energy-shell
   temperature under H-count").
2. **Matching.** GR:78–80, :144–150: β_Eħ = τ_K, i.e. T_cl = T_KMS, gives ħ = c³ε²/(4Gσ).
3. **Calibration.** GR:306–308: ε² = 4σl_p², "a self-consistency condition, not an independent
   determination … fixes only the ratio ε/√σ = 2l_p".
4. **The 1/4.** GR:316–318: σA/ε² = A/(4l_p²) "whatever σ"; the 1/4 is "fixed at 1/4 by the Hawking
   temperature and the first law (Hawking 1975)" and "the ratio 2π/8π"; GR:320: "the coefficient is
   equivalent to the Hawking-temperature normalization (T = ħκ/2πck_B plus the first law fixes
   it)". The corpus therefore identifies the coefficient with **A2** and transports it onto the
   count through step 3.

[W] Under the law-variation device (slope k·β_E): step 2 gives ħ = c³ε²/(4Gσk), step 3 gives
ε² = 4kσl_p², the count is A/(4k l_p²), T_cl (A1a) = k·T_KMS, the law's temperature (A1b) = T_KMS,
and the A2 entropy is A/(4l_p²) for every k. So the count equals the A2 value exactly when k = 1.

### 2.3 R3–R4: ρ_s and the concordance (GR §7.2; SM §3.2; Sub E7)

GR:426: "The horizon carries A/ε² = S_dS/σ modes, of total entropy S_dS = σA/ε² (§5). The classical
temperature is T_cl = c³ε²H/(8πGk_Bσ) (§3.1) … E_s = S_dS·k_BT_cl." The entropy is A1 and the
temperature is its own Clausius temperature: **A\* = A1a** (the displayed formula, not the shell
law's temperature).

[W] For any entropy S = ηA paired with its Clausius temperature through the first law,
k_BT = (c²κ/8πG)/η and k_B·S·T = c²κA/(8πG), independent of η. Hence:

| Reading | E_s | ρ_s/ρ_crit (d = 3) |
|---|---|---|
| A1a (displayed), any k | c²κA/(8πG) | 1 |
| A1b (count × law temperature), slope k | c²κA/(8πGk) | 1/k (Stage 0 F5) |
| A2 / A3 (S = c³A/(4Għ), T = T_dS) | c²κA/(8πG) | 1 |

With κ = cH and A = 4πc²/H², E_s = c⁵/(2GH) = c⁴R_H/(2G), R_H = c/H. ρ_s = ρ_crit is therefore the
statement 2G(E_s/c²)/c² = R_H, which is the flat Friedmann equation H² = 8πGρ/3 written for the
mass inside the Hubble radius [W]. Since ρ_crit and V_H are both computed from H, the equality is the
definition of ρ_crit re-expressed; it says nothing about spatial curvature unless the boundary
energy is identified with the gravitating density, which GR:420 and :444 leave open. Test N: the textbook A2 route gives the same value with no OI
quantity (control K1), so R3 is Xa. GR:430 and ch07:254 already state that "only Jacobson's dE …, an
area-law entropy, and the Friedmann volume enter"; appA:117 calls it "a normalization identity".

[W] General d (GR:440; SM:196), c = 1: k_B·S·T = HA/(8πG_d) for any Clausius-paired area entropy,
V_d = AR/d = A/(dH), so ρ_s = dH²/(8πG_d), against ρ_crit = d(d−1)H²/(16πG_d): ratio 2/(d−1). The
inputs that survive are the d-dimensional first-law prefactor (taken in the same form for every d,
GR:440), the ratio V/A = R/d and the d-dimensional Friedmann coefficient. No OI-specific quantity
survives (GR:440: the count is σA/ε^{d−1}; ε and σ cancel). The d = 3 selection is therefore a
property of these gravitational inputs, conditional on identifying the boundary thermal energy with
the gravitating density, which GR:420, :444 and SM:194 leave open. [LIT, not re-read: the
d-dimensional Misner–Sharp mass inside the apparent horizon of flat FLRW equals ρ_crit·V for every d,
so the ratio is that of the product TS to the Misner–Sharp energy.]

### 2.4 R1, R2, R2z: entropy displacement (GR §7.3)

1. **Step 1** (GR:472–476): ΔS = M_Bc²/(k_BT_dS) = 2πM_Bc²/(ħH), "the Clausius relation applied to
   the boundary reservoir": **A2**, at measured ħ. ch07:262 (FULL:2127) describes the same quantity
   as "the Bekenstein bound applied to a baryonic mass M_B in a de Sitter background" (A3-type
   provenance, same value).
2. **Step 2** (GR:478–482): a₀ = (d−3)/((d−2)(d−1))·cH = cH/6, "taken over from Verlinde's
   analysis rather than rederived from the substratum". ΔS of Step 1 does not appear in this formula
   or in Step 3 [W]; the value contains c, H and the imported factor only (Stage 0 F4 (1)). The prose
   around it nonetheless ties the mechanism to the boundary count: GR:468 ("The boundary-density
   normalization of §7.2 motivates a proposal for the structured component"), GR:470 (T_dS "requires
   H-count (the hidden sector's energy-dependent entropy is its boundary count)"), GR:472 ("Baryonic
   matter M_B is coupled to the boundary entropy through H_VB"), GR:478 ("The displaced entropy
   redistributes over the volume between the matter and the horizon").
3. **Step 3** (GR:486–488): g_total = √(g_B a₀) in the deep regime, v⁴ = GM_B·cH/6.
4. **Redshift** (GR:512): "On extending the conditional radial law to the supplied flat cosmological
   background, a₀(z) = cH(z)/6".

**The imported factor [LIT, re-read for this audit: arXiv:1611.02269v2, eqs. 1.2, 1.4–1.7,
2.12–2.15, 4.25–4.30].** Verlinde sets a₀ = cH₀ (eq. 1.2) and aM = (d−3)/((d−2)(d−1))·a₀
(eq. 1.7), which is GR's a₀. The volume-law entropy is normalized to the Bekenstein–Hawking entropy,
S_DE(r) = (r/L)·A(r)/(4Għ) (eqs. 2.12–2.15), and the displaced entropy is computed from the same
area entropy, S_M(L) = u(L)·d/dL[A(L)/(4Għ)] = −2πML/ħ (eq. 4.25): **A3** on both sides. In
eq. 1.5, (2π/(ħa₀))M_D² = (A(r)/(4Għ))·M_B/(d−1), the left side equals (8πGL/(4Għ))M_D² with
L = c²/a₀, so the coefficient 1/(4Għ), and ħ with it, cancels [W]. Verlinde's S_M(L) equals GR's
Step 1 ΔS (with L = c/H, both are 2πMc²/(ħH)) [W].

[W] Test K: rescaling the area-entropy coefficient by 1/k on both sides of eq. 1.5 (a count used for
both S_DE and S_M) leaves a₀ unchanged; rescaling S_DE only, with S_M kept at the A2 value of
Step 1 (a count for the volume law and Clausius at T_dS for the displacement), gives
g_D = √(g_B·aM/k), i.e. a₀ → cH/(6k). No site computes this combination; GR imports the value
whole (GR:482). But the reservoir whose entropy GR:472–478 displaces and redistributes is the
boundary entropy of §7.2, i.e. the count (GR:426), while Step 1's ΔS is the A2 value: the prose
describes the mixed reading. Under A\* the displayed value of a₀ is law-independent because it is
imported (Xi), not as an OI result. Whether OI's own mechanism gives cH/6 or cH/(6k) is not
determined on `main` (U), because the factor is not derived in OI.

Reviewer's ruling (round 1, PR #1457): with the same area entropy ηA normalizing both S_DE and S_M,
η and ħ cancel in Verlinde's eq. 1.5 (checked against the arXiv:1611.02269v2 TeX source); with
S_DE alone rescaled, a₀ = cH/(6k). Both statements hold, for different cases.

**Native content (Test N).** Verlinde's own derivation gives cH/6 and the deep-regime scaling with
no OI ingredient. R1–R2 are classed Xi only: no OI quantity survives, but the surviving input is
Verlinde's derivation (volume-law entropy, elastic response), not one of the textbook inputs PREREG
§4 lists for Xa. The OI-specific content is interpretive: the
identification of Verlinde's memory hypothesis with C2 (GR:484), the reservoir reading and the heat
input Q = M_Bc² (GR:470). None of these enters the value. The conditions GR:470 attaches to a₀
through T_dS (H-count, H-slope, H-frame, H-Hawking, local boost structure, symmetric rates) condition
the OI reading of the mechanism, not the number; T_dS at measured ħ needs no H-count (Stage 0 F4 (2)).

**R2z.** Verlinde states that he used the present-day H₀ and that "a0 should actually be defined in
terms of the dark energy density, or the value of the cosmological constant. This would imply that
a0 is indeed constant" (arXiv:1611.02269v2, §8.2). GR's a₀(z) = cH(z)/6 is therefore OI-adopted, not
derived, applied to a flat FLRW background outside the exact de Sitter scope on which GR states its
calibration (GR:56: the Kodama–Hayward temperature differs from ħH/(2πk_B) by about 22 % today, and
"extending the argument to a genuinely dynamical FLRW horizon … is not established here"). Class:
X (i) for the normalization at each z, conditional on that extension.

## 3. Classification table

Classes per PREREG §4 (U > X > C > D). "—" means the alternative is not a coherent reading of that
result's displayed formula. K = Test K (law-dependent?), N = Test N (OI-native quantity survives?),
Z = Test Z flag.

| Id | A1a (count, Clausius-paired) | A1b (count × law temperature) | A2 (Clausius at T_dS) | A3 (imported BH) | A\* (text) | Class under A\* | K / N / Z under A\* | Named conditions carried |
|---|---|---|---|---|---|---|---|---|
| R1 a₀ | cH/6 if the count is used on both sides of eq. 1.5; X (i) | cH/(6k) if the count is the volume-law entropy and Step 1's A2 value the displacement; X (i) | cH/6; X (i) | cH/6 (Verlinde as imported); X (i) | value: A3 inside the import; prose: the count as the displaced reservoir (GR:468–478), A2 for Step 1 | **X (i)** for the displayed value; OI's own mechanism U | value no (imported), mechanism undetermined / no / no | GR:470: T_dS conditions and Q = M_Bc² (not load-bearing for the value); C2 reading |
| R2 Tully–Fisher, r_M | as R1 | as R1 | as R1 | as R1 | as R1 | **X (i)**; mechanism U | as R1 | as R1; the proposed displacement law supplying g_total = √(g_B a₀) (GR:486) |
| R2z a₀(z) evolution | as R1 at each z | as R1 | as R1 | as R1 | as R1 plus H → H(z) | **X (i)**; the extension is OI-adopted, not derived | as R1 / no (H(z) is not an OI quantity; the extension is OI-adopted, not derived) / no | as R1; extension beyond exact de Sitter (GR:56, :512) |
| R3 ρ_s = ρ_crit | ρ_crit; X (a) | ρ_crit/k; X (a) | ρ_crit; X (a) | ρ_crit; X (a) | A1a (GR:426) | **X (a)** | no / no / no | first law; area-law form; source identification open (GR:420) |
| R4 2/(d−1), d = 3 filter | 2/(d−1); X (a) | 2/((d−1)k); X (a) | 2/(d−1); X (a) | 2/(d−1); X (a) | A1a (GR:440; SM:196 "normalized as in [GR §§5, 7.2]") | **X (a)**; filter use conditional | no / no / no | d-dimensional first-law form; source identification open (GR:444, SM:194); inferred Ω_total (Sub:88) |
| R5 ħ relation | c³ε²/(4Gσ); X (m) | c³ε²/(4Gσk); same | — (A2 takes ħ as input) | — | A1a = A1b under H-count (GR:78–80, :144) | **X (m)** | yes / yes / flagged (§5) | H-count, H-slope, H-frame, H-Hawking, local boost, symmetric rates (GR:88) |
| R6 ε, ε_lat | 2√σ l_p; X (m) | 2√(kσ) l_p; X (m) | — | — | calibration (GR:306) | **X (m)** (K3) | yes / yes / flagged (§5) | as R5; H-link single-link reading for ε_lat (GR:104) |
| R7 1/4 | count = A/(4l_p²) at k = 1 | count = A/(4k l_p²) | A/(4l_p²) for every k; X (a) | A/(4l_p²) as input; X (i) | A2 coefficient transported to the count (GR:318, :320) | coefficient **X (a)**; count's equality **X (m)**, **Z** | count yes, coefficient no / no / flagged | as R5 |
| R8 N_modes | A/(4σl_p²); X (m) | A/(4kσl_p²); X (m) | — | — | GR:316, :366 | **X (m)** | yes / yes / no | as R5 |
| R9 1 − Ω_B | via R3 | via R3 | via R3 | via R3 | GR:454 | **X (a, m)** | no / no / no | source identification and matter-like/vacuum-like split open (GR:452–456) |
| R10 compression ratio | dimensional identity; ε_lat variant X (m) | — | — | — | GR:364 | **X (a)** | variant only / no / no | coupling step G3 (GR:364) |
| R11 App. A.6–A.7 | labels only | — | — | — | GR:775, :789 | not a consumer | — | H-decouple etc., as GR states |

Every displayed value except R5–R8 is law-independent under A\* (R1–R2 because they are imported;
the law dependence of OI's own displacement mechanism is U). No row is D. Hypotheses such as H-count
and H-link are carried as named conditions; under PREREG §4's precedence they do not lower an X
class to C.

## 4. Consistency findings (decision rule 4)

Each finding names the site, the stronger or different statement, and the authoritative anchor.
Mirrors in `FULL.md` are listed with the chapter site. Severity is the writer's estimate for the
reviewer. All are recommendations for a separately authorized correction unit; nothing is edited.

| Id | Site(s) | Statement | Anchor and trace | Kind | Severity |
|---|---|---|---|---|---|
| F-1 | ch09:63; FULL:2478 | "the dimensional factor 1/6 arises from the cubic-lattice geometry combined with the d = 4 spacetime structure" | GR:482 "taken over from Verlinde's analysis rather than rederived from the substratum"; §2.4 | imported → substrate-derived | high |
| F-2 | appA:92 (row 23), :108 (G6); FULL:5539, :5555 | Layer "0/1" (substratum / substratum-level structural); row 23 omits "(factor imported)" | appA:48–50 layer definitions; GR:482 | imported → substrate-derived (layer); mirror inconsistency between rows 23 and G6 | medium |
| F-3 | ch03:118; FULL:979; Str:903 | a₀ = cH/6 listed among results "class-specific to OI's substratum representative" (ch03) and as a Level 3 prediction that "follow[s] from OI's algebra-channel pair" (Str:897, :903) | GR:482; Test N (§2.4): Verlinde's derivation gives the value with no OI ingredient | imported → native (related, weaker: Sub:375 "a MOND acceleration scale a₀ = cH/6 from entropy displacement" without the import; Sub:419 "specific GR-side prediction … which collectively distinguish the framework", import stated) | medium |
| F-4 | ch09:149; FULL:2564 | baryonic Tully–Fisher v⁴ = GM_B·cH/6 with empirical match "confirmed empirical relation" | GR:547 "normalization comparison open"; the form v⁴ ∝ M_B is the imported deep-MOND scaling | status stronger than anchor | medium |
| F-5 | ch09:258; FULL:2673 | "the 1/4 coefficient, the acceleration scale a₀ = cH/6 … constituting the substrate-computable record" | R7 (A2 coefficient, σ cancels), R1 (imported); GR:318, :482 | ambient / imported → substrate-computed | medium |
| F-6 | ch05:59, :61; FULL:1374, :1376; Sub:88; ch02:120; FULL:750 | flatness "Ω_total ≈ 1 — is, in the framework's gravitational sector … a structural feature rather than an initial condition"; d = 3 "the unique value at which the observed spatial flatness is structurally explained rather than fine-tuned" (ch05); E7: "The cosmological parameter inferred from observation … satisfies ρ_s/ρ_crit ≈ 1 (spatial flatness near critical density)" (Sub:88), which treats ρ_s as the observed total density; "spatial flatness" among the empirical inputs from which "the substratum is forced" (ch02:120), whose route into the reconstruction is E7 | GR:420 "Its use as a physical source is a separate question", GR:444; §2.3: ρ_s = ρ_crit is the definition of ρ_crit re-expressed (ρ_crit and V_H both from H) and says nothing about curvature unless the source identification is adopted; Ω_total is inferred (§A.24) | identity → explanation or observation; ambient → native | high |
| F-7 | SM:30 | concordance: "its coefficient inherits H-count and the horizon conditions of [GR §2, §8.5] through ε = 2√σ l_P" | GR:428–430, :440: ε and σ cancel; §2.3 | wrong provenance | medium |
| F-8 | SM:180, :200, :1424; Sub:157 | concordance as a "non-anthropic" filter that "independently excludes d ≥ 4"; "a consistency check that the framework passes exactly rather than by a numerical coincidence" | §2.3: the ratio and its d-dependence come from the first law, V/A and Friedmann; no OI quantity survives; the filter is conditional on the open source identification (GR:444) | ambient → native | high at SM:180 (it carries the answer to the anthropic objection); medium elsewhere |
| F-9 | SM:196 | ST/V "conditional on H-slope, the further conditions of [GR §8.5(b)] and the symmetric detailed-balance rates" | §2.3: S·T is independent of the calibration that these conditions support | over-conditioned; misattributes the normalization (conservative direction) | low |
| F-10 | GR:470, :510; ch07:260, :262; FULL:2125, :2127 | a₀ and Tully–Fisher "inherit" the conditions on T_dS through Step 1 | §2.4: Step 1's ΔS does not enter the displayed a₀ or v⁴; T_dS at measured ħ needs no H-count (Stage 0 F4 (2)). The same prose (GR:470–478) identifies the displaced reservoir with the count, which bears on OI's own mechanism (U), not on the displayed value | misattributes the normalization of the displayed value (conservative direction) | low |
| F-11 | ch07:262; FULL:2127 vs GR:472–476 | ΔS called "the Bekenstein bound applied to a baryonic mass" (book) vs "the Clausius relation" (paper) | same value (§2.4); different provenance (A3-type vs A2). Verlinde's eq. 4.28 calls the displaced entropy "up to a sign the familiar Bekenstein bound", a source for the book's wording | mirror provenance mismatch | low |
| F-12 | GR:689 | "the quantitative consequences specific to it (the fixed 1/4 coefficient and ε = 2√σ l_p …)" | GR:308 (ε is a calibration), GR:318–320 (1/4 = the Hawking-temperature normalization) | available → derived (see Z-1) | medium |
| F-13 | GR:108; GR:160; ch07:61, :65; FULL:1926, :1930 | "ħ is derived, not free, conditional on the calibration a_*=τ_K/β_E (§2.3; Step 4) and its named conditions" (GR:108); "derives ħ from G and ε" (GR:160); "the framework derives ħ downstream of this counting" | GR:308 "one free geometric parameter (ε) … not an independent determination"; Sub:179, appB:169, gloss:73 | value vs relation ambiguity (see Z-2) | low |
| F-14 | Str:904 | "Holographic A/4 at cosmological horizon" listed as a Level 3 OI-universality-class prediction, "Structural" | R7: the coefficient is the A2 value, reproduced by any Clausius-paired route (K1) | ambient → native | low |
| F-15 | appA:110 (G9); FULL:5557 | dark-sector budget ~95 % classed C (conditional structural) | GR:454, :545: "uses the supplied baryon fraction"; R9 is X (a, m) | class stronger than its inputs | low |

Sites that agree with the trace and were checked: GR:24–28, :88, :158, :308, :318–320, :356, :420,
:430, :444–446, :482, :510, :546–547, :551, :705; SM:166, :194; Sub:22, :179, :407, :507,
:529; Meth:507; appA:117; appB:169; appC:257; gloss:17, :73, :103; ch00:83; ch02:68, :112, :190;
ch04:44, :136; ch07:106, :254, :266–268, :298–299; ch09:48, :148; ch19:46, :116.

## 5. Circularity (Test Z)

| Id | Calibration | Equivalent statement | Presented as | Sites |
|---|---|---|---|---|
| Z-1 | ε²/σ solved from measured ħ (GR:306) | ε = 2√σ l_p (the calibration itself); σA/ε² = A/(4l_p²) (the calibration rewritten, GR:158: "consequences of it, not independent checks of it") | "quantitative consequences specific to" the substratum; "substrate-computable record" | GR:689; ch09:258 (FULL:2673); Str:904 (weaker) |
| Z-2 | as Z-1 | ħ = c³ε²/(4Gσ) with ε/√σ fixed by ħ | "ħ is derived, not free, conditional on the calibration a_*=τ_K/β_E (§2.3; Step 4) and its named conditions" (GR:108); "derives ħ from G and ε" (GR:160) | GR:108, GR:160 (against GR:308, Sub:179, which state the correct scope) |

Everywhere else the corpus calls these "consistency relations", which is the class the trace gives
(appA:117, Sub:529, ch04:44, ch07:106). ρ_s = ρ_crit is not calibrated, but it is the definition of
ρ_crit re-expressed (§2.3); F-6 presents it as explaining, or as observing, a flatness on which it
bears only through the open source identification.

## 6. Consequences for the Stage 0 record (recommendations only)

The Stage 0 record (`r1-l8-stage0-20261120/AUDIT.md`) is merged and is not edited.

- **D1 / C1.d.** Resolved for the displayed value only (§2.4): GR §7.3 uses A2 for its Step 1 and
  imports the value whole; the factor's own derivation uses A3 on both sides of eq. 1.5, where the
  coefficient cancels. The displayed a₀ is law-independent because it is imported, and C1.d is not
  (c) for that value; whether it is (a) or (b) under Stage 0 §5 turns on whether conditions GR
  attaches but that are not load-bearing for the value are counted. GR:468–478 identify the
  displaced reservoir with the boundary count, and the law dependence of OI's own mechanism is not
  determined, because the factor is not derived in OI.
- **F5 / C1.e.** F5's ρ_s = ρ_crit/k pairs the count with the shell law's temperature (A1b).
  GR:426–428 pairs the count with its own Clausius temperature T_cl = c³ε²H/(8πGk_Bσ) (A1a); under
  that pairing ρ_s = ρ_crit and the concordance 2/(d−1) for every k (§2.3). C1.e's (c) therefore rests
  on a reading the displayed formula does not use. The conclusion F5 drew for E7 (law dependence
  reaches the concordance check only) does not hold under A\*; its redundancy observation for the
  selection of d does.
- **Counts, by reading.** Under A1a (the displayed GR:426–428 pairing, confirmed by GR:426's §3.1
  citation, the formula's ε, σ form, GR:430 and ch07:254 / FULL:2119): N_c = 7, N_c′ = 14; C1.e
  → (a) on the review's reading, or (b) if its area-law premise is counted as a property; C1.d
  undetermined between (a) and (b) for its value; totals (a) 2–4, (b) 11–13, (c) 7, total 22. Under
  A1b (the GR:58 / :336 reading, which Stage 0's F5 used; F5 substituted the shell-law temperature for
  the displayed T_cl): C1.e stays (c), N_c = 8, N_c′ = 15, with C1.d as above. Any change is for the
  owner, by a record that cites this one.
- **F4.** Steps (1)–(2) confirmed. Step (3): the imported value uses A3 internally, where the
  coefficient cancels; GR §7.3's prose does identify the displaced reservoir with the count
  (GR:468–478), so step (3)'s concern applies to OI's own mechanism, which is undetermined, not to the
  displayed value.

## 7. Controls (PREREG §7)

| Id | Result | Verdict |
|---|---|---|
| K1 | Textbook route: S = c³A/(4Għ) from dS = dE/T_KMS with the first law; S·T_dS/V_H = ρ_crit and 2/(d−1) in d dimensions (§2.3). Test N: no OI quantity present, so **Xa**; Test K: no law; never D | Passed |
| K2 | κ_m = 3/2: exact count 6N₂(R²/ε_lat²) of links crossing a sphere centred on a site, = (3/2)A/ε_lat² + O(R/ε_lat) (GR:104). Native content (lattice), no measured or imported normalization, conditional on the single-link reading H-link, which SM Lemma 6a records as not a consequence of SM §4.4 (GR:104): **C** | Passed |
| K3 | ε = 2√σ l_p: solved from measured ħ (GR:306–308): **Xm**; Test Z flags GR:689 (Z-1) | Passed |
| K4 | The count after calibration under slope k: A/(4k l_p²) (§2.2): law-dependent | Passed |
| K5 | Every [W] step is exact algebra on displayed formulas (§§2.2–2.4); no numerical value is used as evidence of an identity. The numerical values quoted (GR:480–482) are the corpus's, not this audit's | Passed |

## 8. Coverage (PREREG §3 step 4)

Fixed-string hits, counted as matching lines in `papers/*.md` + `book/*.md` (of which in `FULL.md`):
`cH/6` 61 (23); `a_0` 285 (82); `Verlinde` 37 (12); `rho_s` 21 (6); `ρ_s` 1 (0);
`rho_{\text{crit}}` 21 (7); `2/(d-1)` 6 (1); `\frac{2}{d-1}` 2 (0); `concordance` 36 (10); `1/4` 128
(45); `A/(4` 32 (10); `4\sigma` 95 (36); `T_{\text{dS}}` 9 (3); `T_{\text{cl}}` 17 (6);
`\sigma A/\epsilon^2` 9 (1); `S_{\text{dS}}` 39 (14); `is derived, not free` 1 (0);
`value of $\hbar` 9 (4); `derive(s|d) $\hbar` (regex) 10 (4).

**Traced.** Every `cH/6`, `Verlinde`, `rho_s`, `rho_{\text{crit}}`, `2/(d-1)`, `\frac{2}{d-1}`,
`T_{\text{dS}}`, `T_{\text{cl}}`, `\sigma A/\epsilon^2` hit outside `FULL.md` was opened and assigned
to a result, a finding or the agreeing-site list of §4; the `concordance` hits in ch10 and ch11 use
the word in another sense. For `1/4`, `A/(4`, `S_{\text{dS}}`, `4\sigma`, the hits outside the
lattice-dispersion and SM matching contexts (SM:950, :1212, :1302, :1448; Sub:484; ch04:128) were
read at the hit line and assigned to R6–R8 or R10. `a_0` hits were read only where they co-occur
with MOND, `cH` or Verlinde. `FULL.md` was checked for the mirrors of every chapter finding (line
numbers in §4); it was not read independently.

**Not traced.** `.tex`/PDF mirrors; Lean modules (none states these normalizations); verification
records beyond S0, P7B and REMAINDER; GR §8.5's universality-class conditions beyond the lines
cited; the d-dimensional validity of the first-law prefactor GR:440 assumes; the internal
consistency of Verlinde's elastic-response argument (debated in the literature GR:484 cites). This
is not an exhaustive census.

## 9. §A.23 and §A.24 typing

| Result | Axis | Comparison typing (§A.24) |
|---|---|---|
| a₀ = cH/6 vs g_† = (1.20 ± 0.02 ± 0.24)×10⁻¹⁰ m/s² (GR:482) | consistency: the value is imported and the source presents it as reproducing Milgrom's scale (arXiv:1611.02269v2, after eq. 1.7) | radial-acceleration fit; depends on stellar mass-to-light (GR:482) |
| v⁴ = GM_B·cH/6 | consistency; normalization comparison open (GR:547) | raw/direct (velocities, baryonic masses) |
| a₀(z), BTFR and r_M evolution | **correctness**: extension OI-adopted, not derived (GR:56), not fitted; reported in tension (GR:514–516, :548–549) | raw/direct, with baryonic masses partly model-dependent (GR:516) |
| ρ_s = ρ_crit | none: identity with ρ_crit computed from H | — |
| 2/(d−1) | consistency at most, conditional on the source identification | inferred Ω_total ≈ 1 (Sub:88) |
| ħ, ε, 1/4, N_modes | none (calibration and consistency relations; no direct test of the 1/4, GR:320) | — |

Bands unchanged. This audit is a provenance trace; it adds no evidence for or against the framework's
match to nature.

## 10. Verification status and remediation (§A.46 item 4)

Evidence level: paper reading of the corpus at the pin, with [W] algebra (§§2.2–2.4) and one
re-read external source [LIT]. Review: independent non-author review of `e98cca04`, REVISE (minor), PR #1457 round 1, answered
in §13. Missing: a delta review of the revised head.
Accountable Issue: #1169 (authorization), with #1055 for Stage 0's record. Resolution: a review
recorded on the guiding PR. The findings F-1 to F-15 and Z-1, Z-2 are recommendations; any manuscript
correction is a separately authorized unit (§A.25, §A.27). The [W] readings of §2.3–§2.4 are not
results until reviewed and are used as premises only within this audit's own rows.

## 11. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7041456852 | Authorization, scope, goal link | Provenance; quoted in PREREG with author and time |
| #1169, #873, #1456, #1055 | Accountability; Stage 0 PR (merged) | Provenance |
| arXiv:1611.02269v2 | §2.4's reading of the imported factor | External literature [LIT], re-read; cited by GR:478 as [20] |
| Commit `7dcd0799` | Preregistration | On this branch; lands with this record |

## 12. What an independent reviewer must check

1. §2.3: that GR:426–428 pairs the count with its own Clausius temperature (A1a), not the shell
   law's (A1b); the product identity k_B·S·T = c²κA/(8πG) for any η; the d-dimensional ratio; and the
   restatement of ρ_s = ρ_crit as the flat Friedmann equation for the Hubble mass.
2. §2.4: that Step 1's ΔS does not enter a₀ or v⁴; the reading of Verlinde eqs. 1.2, 1.5, 1.7,
   2.12–2.15, 4.25 (A3 on both sides; cancellation of 1/(4Għ) in eq. 1.5); the mixed-reading value
   cH/(6k); that no corpus site computes the mixed combination while GR:468–478 identify the
   displaced reservoir with the count; and that OI's own mechanism is therefore U.
3. Test N for R3, R4 and R7's coefficient (Xa) and for R1–R2 (no OI quantity survives; Xi, since the
   surviving input is Verlinde's derivation).
4. The class precedence: in particular that R5–R8 are X (m) and R3–R4 X (a), not C.
5. Findings F-1, F-6, F-7 against their anchors, and that the agreeing-site list contains no
   overstatement.
6. §6: the C1.e conclusion under each reading (A1a: not (c); A1b: (c)) and the resulting Stage 0
   counts.
7. Controls K1–K5 and that no [W] step constructs a law, adds a premise or promotes a conditional
   result; that no manuscript, Lean or registry file is changed.

## 13. Answer to the independent review of `e98cca04` (round 1, REVISE minor)

PREREG is unchanged. Each item and where it is answered:

| Item | Change |
|---|---|
| B1 | "Does not enter" / "no site writes" replaced: no site computes the mixed combination, but GR:468–478 identify the displaced reservoir with the boundary count; a₀ is law-independent because it is imported (Xi), not as an OI result; OI's own mechanism is U; D1 resolved for the displayed value only. The reviewer's ruling (same entropy on both sides: η and ħ cancel; S_DE alone rescaled: cH/(6k)) is recorded in §2.4 (§1, §2.4, §3, §6) |
| B2 | R5, R8, ε_lat and R7's count equality are X (m) under PREREG §4's precedence, with Z where flagged; H-count, H-slope and H-link carried as named conditions (§1, §3) |
| B3 | Sub:88 moved from the agreeing list into F-6, with ch02:120 (FULL:750) (§4) |
| N4 | Stage 0 recount stated under both readings (§1, §6) |
| N5 | R1, R2 are X (i); Xa dropped with the reason (§2.4) |
| N6 | R2z: "OI-adopted, not derived (GR:56)" (§1, §2.4, §3) |
| N7 | GR:108 quoted in full; GR:160 cited against GR:308 (§1, F-13, Z-2) |
| N8 | F-8 at SM:180 raised to high |
| N9 | F-6 and §2.3: "the definition of ρ_crit re-expressed" |
| N10 | F-11 notes Verlinde eq. 4.28's wording; severity low |
