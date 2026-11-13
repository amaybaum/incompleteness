# Independent review of unit W1-1

Reviewer: independent agent, read-only and paper-only. Object: `w1-1/W1-1-REPORT.md` (226 lines; cited below as
`R:<line>`). Sources: `origin/main` `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`, read with `git show` into a fresh
directory (`w1-1-review/`). The author's `w1-1/src/` copies are byte-identical to `fb733b4a` for GR, Main, SM,
Substratum and Structure (checked with `cmp`), so line numbers agree. I also read #1245 (all 5 comments) and #1244
c.6817132584–c.6818164393 (read-only), and the Lean statement of `counting_passive`
(`verification/lean-mathlib/OIBridge/ThermalOrientation.lean:256`). I ran no computation beyond hand arithmetic.
Authorization: owner amaybaum, 2026-11-12, #1245 c.6829744096.

## Verdict: ACCEPT WITH CHANGES

The headline verdict stands: W1 is an additional physical assumption, not a derived result (R:19, R:171). No change
below reverses it, and one of them (F7) makes it stronger. The required changes fix one novelty overclaim made without
the §A.19 search (F1). They also qualify "exact" statements whose hypotheses are not all stated (F2, F3), correct a
§A.29 claim that fails for r ≤ −1 (F4), and repair the "strictly stronger" comparison in §8, whose two sides count
different sets (F5). The rest are scope, labelling, cross-propagation and provenance items.

## Checks against the brief

**1. Definitions.** These are faithful: W1 (#1244 c.6817396025; #1245 c.6818970549), H-count (R:33 matches GR:58 word
for word), readings L and C (#1245 c.6828106610), H-inert, H-eq, W1′ and ρ. I re-derived ρ (R:40):
C_B = −β²/s_B″ = −2s_B, the local maximum condition C_D < 2s_B, and dE_B/dE = s_D″/(s_B″+s_D″) = 1/(1−ρ). All are
correct. CE-L checks: s_H = (1+r)σA/ε² + const gives β_E = (1+r)β_geo. Three small departures from the sources:
- CE-X (R:48) omits c.6818970549's qualifier "with S1's capacity read as boundary capacity".
- R:39 weakens "presupposed by GR:58 and GR:50 (C3)" to "GR:50 suggests it".
- R:60 says Main:50 posits H_tot "on the idealized continuum Γ". Main:50–52 says the *product decomposition* is
  idealized and does not mention a continuum.

**2. Hand derivations.**
- **Tangency lemma (R:110): correct.** g = f − s_H ≥ 0 near E\* with g(E\*) = 0 has an interior minimum, so
  g′(E\*) = 0. It needs E\* interior and the bound to hold as a function of E (see F6).
- **N2 identity (R:77).** I re-derived it with forward differences on a common energy lattice of step δ, with
  E_B, E_D ≥ 0:

  Ω_H(E+δ)/Ω_H(E) = Σ_y p(y)·Ω_B(y+δ)/Ω_B(y) + Ω_B(0)Ω_D(E+δ)/Ω_H(E).

  This is exact. The first-order reading is not as stated (F2).
- **Linearity and sign (R:78–79): correct.** With s_B = (k/2)x² and k = 8πσG²/(c⁸ε²) (this matches GR:58:
  s_H′ = kE, s_H″ = k = β/E), β_B(x) = kx + kδ/2. So β_E ≈ k⟨E_B⟩ and β_E/β_geo = 1 − ⟨E_D⟩/E, giving
  r = −⟨E_D⟩/E with the convention β_E = (1+r)β_geo. The sign is right: the shell is hotter. The ensemble is the
  microcanonical split p(x) ∝ Ω_B(x)Ω_D(E−x) on the total-energy shell. The cross-check at R:81 switches to a
  canonical D. That is acceptable as an approximation: U_D ≈ C_D/β and 2s_B = βE give r ≈ −ρ.
- **Ratio ~7×10⁵⁹ (R:48): correct.** [(4π/3)R³/ε³]/[8πR²σ/ε²] = R/(6εσ). With R = 1.37×10²⁶ m and
  ε = 3.23×10⁻³⁵ m this is 7.1×10⁵⁹. It is per Hubble volume: D lies beyond the horizon, and its volume is not fixed
  anywhere. That framing is acceptable as orientation.
- **CE-M (R:53): correct to order of magnitude.** dN_B = 8πR dR/ε², the D→V transfer is 4πR²dR/ε³, and
  r_M = −(s_cell/σ)R/(2ε) ≈ −2.1×10⁶⁰ s_cell/σ. See F4 on its sign.
- **CE-F (R:54): correct at leading order.** For N independent cells s_B″ = s\*″/N ~ −N/E², while the dS form needs
  +2s_B/E², which has the same order and the opposite sign, so finite-N corrections cannot rescue it.
- **Gap route (R:134): correct, with one term dropped.** r = −N_eff(βΔ)e^{−βΔ}/(2s_B). The threshold is
  βΔ − ln βΔ ≳ ln(N_eff/2s_B). With N_eff ≈ 3.2×10¹⁸² and 2s_B ≈ 4.5×10¹²², βΔ ≳ 1.43×10², so the stated value holds.
  T_GH ≈ 2.7×10⁻³⁰ K and Δ ≳ 5×10⁻⁵¹ J both check.
- **C7 (R:152): correct.** E_MS = c⁴R/(2G).

**3. W1-0.** The reading of SM:296 is correct ("E takes p values"; F is linear mod p). But the corpus already states
the substance, and the report missed it (F1).

**4. §A.29 "no independent prediction".** Correct for 1+r > 0. It fails for 1+r ≤ 0 (F4).

**5. Minimal form.** The idea is sound: only the IR slope is used (GR:74, :82). But "H-count is strictly stronger than
W1-0 + W1-min" is not established as written (F5).

**6. Overreach.** Five places: summary item 2 and the conclusion on the gap route (F8); "exact" (F2); "Established"
counterexamples (F9); "NEW" for N0 (F1); "fixed nowhere in the corpus" (F7). Literature is consistently marked as
recalled and not load-bearing (R:223), and I found no verdict that rests on it.

## Findings and required changes

**F1 (required): N0/CE-0/W1-0 novelty claimed without the §A.19 search.** R:16 and R:58 label N0 "NEW" and assert
that no construction on `main` supplies a real energy. R:65 adds that W1-0 is unstated. R:217 shows SM was read only
at :296, and §11 shows no grep for "energy shell" or "conserved energy". The corpus already says the substance:
- SM:292: "The exact linear rule over ℤ/qℤ conserves E below only modulo q … The rounded rule has no nonconstant
  polynomial invariant of degree at most two … Neither fact supplies the required real positive-definite conserved
  energy." It also describes the real lift: positive definite for |α|<1/d, with null modes and noncompact shells at
  α = 1/d.
- SM:811 sets out a "real-valued conserved energy" only as a candidate.
- GR:695: "The shell is assumed, as in §2.3; it is not a consequence of Lemma 3, which supplies determinism,
  injectivity and the selected measure but no conserved energy."
- GR:58 opens with "Restrict the finite total system to a conserved energy shell".
- H-count's own text carries W1-0's identification clause ("the shell energy E being the energy of the horizon first
  law").
- Main:50 states H_tot, but the posit ledger (Main:724) does not list it.

*Required change:*
- Reclassify N0 as ELABORATING (cross-propagation).
- Cite SM:292, SM:811 and GR:695 as the existing statements.
- Restate the gap precisely: GR names the shell as an assumption (GR:58, :695), but the ħ condition lists (GR:88,
  :623, :637, :673) do not carry it, and Main's ledger (Main:724) has no real-energy posit. The identification clause
  is already inside H-count.
- Note that the real lift (SM:292, :294 "exact real linear map") does carry a real conserved energy. It is not the
  finite substratum, and its shells are noncompact on the normalized branch α = 1/d.
- Update R:16, R:58–65 and the R:189 status row.

**F2 (required): N2 is not "exact" as stated, and its endpoint term is mis-scaled.** R:14 and R:72 call it "exact";
R:78 says "without any saddle approximation"; R:79 says "relative error exactly r". The identity at R:77 is exact. The
step to first order is not:
- The endpoint term is p(0)·e^{δβ_D(E)}, so its contribution to β_E is about p(0)e^{δβ_D}/δ, not "the weight of the
  endpoint". The weight is dimensionless and β is an inverse energy. Neglecting it needs p(0) ≪ βδ, which is stronger
  than a small endpoint weight because βδ ≪ 1 in the IR regime.
- The averaging step leaves a cumulant correction (δ/2)·Var_p(β_B) = (δ/2)k²Var(E_B), which vanishes only as δ → 0.
  On a discrete energy lattice that limit is not available.

*Required change:*
- State the lattice and non-negativity assumptions.
- Write the endpoint term as p(0)e^{δβ_D(E)}/δ, with the condition p(0) ≪ βδ.
- State the O(δ·Var) correction.
- Replace "exact equivalent" (R:14), "Exact identity" (R:72) and "exactly r" (R:79) with "to first order in δ, under
  H-add and W1′(dS) on p's support, with the endpoint and variance terms negligible".
- The ⇔ statements at R:79–80 then carry those hypotheses in both directions (§A.34).

**F3 (required): N2's mean-energy corollary rests on a hypothesis pair that the report's own CE-F and CE-M obstruct.**
β_E = β_dS(⟨E_B⟩) needs H-add together with W1′ in dS form on the whole support of p. For local cells, CE-F (R:54)
excludes the dS form on a fixed partition. CE-M (R:53) breaks H-add on a moving partition, since cells transfer
between D, B and V. So the pair is not jointly realized by local cells under either partition. When p is concentrated,
β_E ≈ β_B(E_B\*) holds without linearity, and "mean versus realized" matters only for a broad p.

*Required change:* say this at N2 and in summary item 3. The general identity β_E = E_p[β_B] + endpoint (F2) is the
robust result. The "mean boundary energy" form is conditional on a hypothesis pair that is unrealized by local cells.

**F4 (required): §A.29 absorption σ → σ(1+r) holds only for 1+r > 0.** R:18 says "any excess r is absorbed", and R:160
says ħ, ε and A/4l_p² are unchanged with σ_eff = σ(1+r). That needs σ_eff > 0:
- At r = −1, β_E = 0 (infinite temperature).
- For r < −1, β_E < 0. The bath count then decreases, which contradicts `counting_passive`'s hypothesis
  (Ω : ℝ → ℝ Monotone, ThermalOrientation.lean:256) and the "β_E > 0" layer at GR:186 and GR:210.
- CE-M's r_M ≈ −2×10⁶⁰ s_cell/σ lies in that regime whenever s_cell ≳ 5×10⁻⁶¹σ. So such a failure would not be
  inert. It would flip the classical thermodynamic orientation.
- Reading L's r = −⟨E_D⟩/E lies in [−1, 0], so it is absorbable except at the endpoint r = −1.
- c.6818970549's "`counting_passive` … is unaffected" carries the same unstated restriction.
- A large positive r (see F7) is absorbable only by giving up σ ≤ ln q as an entropy per mode (GR:98). R:160 already
  says σ's reading moves, so this is consistent.

*Required change:*
- Restrict R:18, R:160–161 and the R:188 row to 1+r > 0.
- Add that r ≤ −1 contradicts the β_E > 0 input of GR:186 and `counting_passive`, and that CE-M at
  s_cell ≳ 10⁻⁶⁰σ is such a case.

**F5 (required): "H-count … strictly stronger than W1-0 + W1-min" (R:19, R:176) is not established as written.**
- W1-min (R:175) counts hidden configurations "on the realized, dynamically connected energy sector". GR:58 and GR:70
  count the whole shell: N_i = |M_i| over all shell microstates. SM:292 notes that the invariant shell ensemble exists
  without cycle ergodicity, and the report's own N1 (R:67) says dynamics does not change the count. Slopes over
  different sets are not ordered by implication, so H-count does not imply W1-min as defined.
- W1-0's conservation and V/H-additivity clauses are not part of H-count's text either. They come from GR:58's
  setting ("conserved energy shell"; "boundary interaction negligible").
- That additivity clause is the weak-coupling premise of H-shell (GR:60). GR:86 says H-shell "is therefore not
  load-bearing", but GR:70 and GR:74 take the rate-ratio slope from N_i = Ω_H(E−e_i), which uses it. The report
  should flag this tension in GR rather than list additivity as a missing condition without comment.
- W1-min's κ\* is ambiguous between readings: total E under L, E_B under C.

*Required change:*
- Define W1-min on GR:58's counted set (the whole shell), or justify the connected-sector variant as a separate,
  different condition.
- State the comparison as: GR:58's setting plus H-count implies W1-0 plus W1-min, and the converse fails. Give the
  converse a witness, for example a CE-F boundary layer tuned to the slope at one point.
- Record the GR:86 versus GR:70/:74 tension on additivity as an assumption-watch item.
- Fix κ\* per reading.

**F6 (required, minor): C3 does not engage the corpus's own capacity statements.** GR:50 (C3: "Hidden sector has
A/ε² modes"), S1 (GR:661: capacity S_dS) and Substratum:268(i) are the corpus's holographic-type statements about the
hidden sector. By the report's own tangency lemma, a capacity bound at the *realized* A is a constant in E. Saturated,
it gives s_H′(E\*) = 0, not β_geo. A bound gives W1 only if it tracks A(E) through the first law, which is the moving
partition of N3 and CE-M. This is the precise form of GR:58's "fixing no entropy–energy slope".

*Required change:* add this to C3. Also replace "That is H-inert's entropy clause restated" (R:114). An absolute
saturated bound with s_B = σA/ε² forces s_D ≈ 0, a trivial D factor, which is a special case of H-inert and strictly
stronger than it.

**F7 (required narrowing; content recommended): the "decisive unknown … fixed nowhere in the corpus" (R:135, R:137,
R:197) is too quick.** The one real-valued conserved energy the corpus supplies is the real lift of the linear rule
(SM:292), which is positive definite for |α| < 1/d. For a positive-definite quadratic form in 2N real variables,
Ω(E) ∝ E^{N−1}. So β = (N−1)/E and C = N−1. The classical deep sector is then extensive, which is CE-X itself, and the
classical count shows no freeze-out. Under reading L with the whole of H in this form, β_E/β_geo = N_H/(2σN_B). With
D ≈ one Hubble volume of ε³ cells, r ≈ R/(6σε) ≈ +7×10⁵⁹, the CE-X ratio again with positive sign. On the normalized
branch α = 1/d the shells are noncompact (SM:292), so β_E is undefined there. This is my hand derivation and is not
reviewed. It strengthens the report's negative conclusion.

*Required change:*
- Narrow R:135, R:137 and R:197 to: "not fixed for the finite substratum. In the real lift (SM:292, |α|<1/d) the
  classical count is extensive, which realizes CE-X. At α = 1/d it is undefined."
- Add the computation, labelled as a hand derivation.

**F8 (required): summary item 2 and §8 misdescribe the gap route.** R:13 says each family "needs a premise that is W1
or H-inert in other words". R:166–167 says no mechanism works "without adding a premise that is W1, or H-inert,
restated". C6(a) (R:133–137) is a distinct, physically meaningful sufficient condition: collective, gapped deep
low-energy configurations with βΔ ≳ ln(N_eff/2s_B). It is not a restatement of H-inert.

*Required change:* say that every candidate either restates W1 or H-inert or needs an open sufficient premise (the gap
route) whose truth is undetermined, and that is negative in the real lift (F7). Also qualify R:15 and R:135: GR:84
refutes the *naive H-energy* route to quantum freeze-out. It does not refute a classical gap in the finite-alphabet
configuration energies.

**F9 (required): "Established" counterexamples (R:45).** CE-L and CE-X are off `main` (#1245 c.6818970549). §A.46
items 1 and 7 bar calling them established or using them as unverified premises.

*Required change:*
- Rename the heading to "Recorded (#1245 c.6818970549; internally reviewed; off `main`)".
- State that this unit re-verified both: the CE-L slope and the CE-X ratio, the latter confirmed by this review.

**F10 (required): incomplete cross-propagation (§10).** The W1-0 marker omits its most direct consumers:
- GR:186, :202, :210, which use "classical configuration energies" and a "derived classical energy ordering";
- the kernel theorem `counting_passive` (ThermalOrientation.lean:256), whose hypotheses are real energies
  ε : Fin m → ℝ, a monotone Ω : ℝ → ℝ and the additive form Ω(E_tot − ε a);
- GR:695, the entropic-force shell.

The C1 line "ergodic shell counting fails there" (R:98, R:196) also needs scoping. Under the report's own N1, cycle
splitting does not change the count (SM:292). It bears only on whether one orbit realizes the shell rates.

*Required change:* add these sites to §10 and scope R:98 and R:196 accordingly.

**F11 (required, process; not a content blocker): provenance incident (R:226).** The author overwrote `GR.md` and
`Main.md` at the shared working root. The files were of unknown origin, and the earlier content is unrecoverable.
That is the case §A.26 covers (sweep, then quarantine, never delete). Both root files now equal `fb733b4a` (checked).
The unit's own sources are unaffected (`w1-1/src/` is byte-identical to `fb733b4a`). However, OA-1 (#1169) runs in
parallel, and the root holds files from many sessions.

*Required change:* report the incident to the owner in the checkpoint, so that any concurrent unit that relied on
root-level `GR.md` or `Main.md` re-sources from `git show`. Recommend writing only inside a unit's own subdirectory.

**F12 (minor citations).**
- Canonical typicality [31] is at Main:752 and :756, not Main:744.
- "τ_Kω ~ O(1)" (R:135) is the report's inference, not GR:66's text.
- The "Gauss-sum … would make any 'slope' zero" aside (R:52): on ℤ/p only a finite-difference analogue exists, and
  near-equinumerous level sets give it ≈ 0 (infinite temperature, the r = −1 boundary of F4). Say that, or drop the
  aside.
- The CE-M summary item (R:17) should keep "order of magnitude, if deep cells carry s_cell".

## What the unit establishes, and at what layer

At the layer of paper derivation (hand-checked, not machine-checked, independently reviewed here), the unit
establishes the following:
- Within OI's present premises, W1 is not supplied by thermalization or ETH, typicality or max-entropy, holographic
  bounds, equivalence-principle, Jacobson or Unruh/Hawking universality, or exact decoupling.
- State-level mechanisms cannot fix a shell count (N1).
- A saturated bound fixes the slope only if it tracks A(E) (tangency lemma, plus F6).
- Exact decoupling makes deep-sector enlargement a gauge direction of ħ only for independently prepared,
  energy-decoupled factors.
- Under B/D additivity, β_E is the shell average of the boundary slope plus an endpoint term (exact as a
  lattice-difference identity; first order as used).
- The gap route is a sufficient condition whose decisive input is undetermined for the finite substratum, and in the
  corpus's real lift it fails: that lift realizes CE-X (F7).
- Failure of W1 by 1+r > 0 is absorbed into σ, so W1 has no independent test within the calibration. Failure with
  r ≤ −1 is not absorbed and contradicts the β_E > 0 input.
- The precondition W1-0 (a real conserved energy identified with the first-law energy) is already named as assumed at
  GR:695 and SM:292, but is absent from the ħ condition lists.

W1 therefore stays an additional physical assumption, conditional and not derived. That is a consistency-axis result:
it moves no correctness band and promotes nothing (§A.23). Readings L and C keep the standing recorded in
c.6828106610. Nothing here is on `main` or established in the §A.46 sense, and the claim that H-count is strictly
stronger awaits F5.
