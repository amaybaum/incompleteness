# W1-1: can existing physics supply W1 (the hidden-sector entropy-slope / thermal-matching condition)?

Unit W1-1, paper-only, authorized by the owner (amaybaum, 2026-11-12, #1245 c.6829744096). Base: `origin/main`
`fb733b4a58558ef64bd7c3585712c76e9f2dfb42`. Line numbers are at that commit unless marked `@1b27369` (the commit the
earlier #1244/#1245 records cite). Method: reading and hand derivations only. No computation on OI rules, no Lean,
no manuscript edit, no premise adopted, no claim promoted. This report has had **no independent review**. Reading L
stays the current manuscript reading and reading C stays the conditional alternative (#1245 c.6828106610). Nothing
here changes that.

## 1. Plain-language summary

1. W1 says that the whole hidden sector's entropy, as a function of energy, rises at the same rate as the horizon's boundary count. That rate sets the classical horizon temperature that the ħ calibration needs (GR:58, :74, :78–82).
2. None of the six families of existing physics tested here supplies W1. Each one either fixes the hidden sector's *state* (W1 is about its *count*), uses ħ (the calibration's output), or needs a premise that is W1 or H-inert in other words.
3. Under one standard assumption (the B/D split is additive) W1 has an exact equivalent, derived here: the shell slope equals the boundary slope at the **mean** boundary energy. Reading L then needs the deep sector to hold essentially no energy. Reading C needs the realized horizon to carry the typical (mean) share.
4. A deep sector with a large gap would make W1 hold. But the infrared slope the calibration uses needs very small classical energy steps, and translation invariance puts the same small steps in the deep sector. The quantum "freeze-out" that would make those steps harmless is blocked by GR's own no-go at GR:84.
5. New: the selected exact linear model (SM:296) conserves an energy valued in ℤ/p. That has no ordering, so the slope W1 refers to is not defined there. A real-valued energy on substratum configurations is a further premise.
6. New: tying the boundary count to the horizon area means either the partition moves with energy, which adds a volumetric deep-cell term about 10⁶⁰ times the boundary term per unit of deep-cell entropy, or W1′ becomes a material-temperature coincidence.
7. W1 has no independent test inside the calibration: any excess r is absorbed into σ → σ(1+r), and no quoted number moves (#1245 c.6818970549). No candidate gives a hard-to-vary independent prediction (§A.29).
8. Verdict: **W1 is an additional physical assumption, not a derived result.** Minimal form (§8): a real-valued conserved classical energy (W1-0), plus one scalar equality of slopes at the realized horizon (W1-min). H-count as written at GR:58 is strictly stronger than what ħ uses.

## 2. Pre-stated productivity test and method (§A.31)

Fixed before the walk. A node is a **gem** iff it yields a fact strictly stronger than restating "S1–S4 do not supply W1"
(already recorded, GR:58, #1245 c.6818970549), **and** it either constrains W1's possible sources or exposes a hidden
assumption. Otherwise it is recorded only. Nodes were walked depth-first, decisive branch first. Each favourable branch
(one that would establish W1) was pressure-tested before being accepted. Output classes: NEW / POSITIVE / ELABORATING /
CONFIRMING / BORDERLINE.

## 3. Definitions (from the sources)

- **β_E and the shell.** GR:58: "Restrict the finite total system to a conserved energy shell and let visible configuration *i* carry energy *e_i*. If the boundary interaction is negligible at the shell scale, uniform counting gives P(i)=Ω_H(E−e_i)/Σ_jΩ_H(E−e_j)", with s_H = ln Ω_H and β = s_H′(E). GR:70: microreversibility gives ln(P_ij/P_ji) = −β_E(e_j−e_i)+…, with β_E = s_H′(E). GR:74: "Only the infrared slope is load-bearing", and with β_E at its H-count value, E′(0)=τ_K/β_E = ħ. GR:78–82: a\* = τ_K/β_E.
- **W1** (assumption-watch marker; #1244 c.6817396025, #1245 c.6818970549). β_E, counted over the whole hidden sector H = B ∪ D on the total-energy shell (GR:58, :70), equals ∂(σA/ε²)/∂E along dE = c²κ dA/(8πG) (GR:98). Equivalently T_micro = T_cl, with k_BT_cl = c²ε²κ/(8πGσ) (GR:100). Write β_geo(κ) := 8πGσ/(c²κε²).
- **H-count** (the current manuscript name of the posited condition that carries W1; GR:58): "the energy-dependent entropy of the whole hidden sector at the shell scale is the boundary count, s_H=σA/ε² up to an energy-independent constant, the shell energy E being the energy of the horizon first law and the deep hidden sector contributing no energy-dependent multiplicity and, by the choice of energy zero, no energy; S1–S4 do not supply it". On exact de Sitter, E = c⁴R/G, s_H = 4πσG²E²/(c⁸ε²) and s_H″ = β/E (GR:58). H-count is cited as a condition of ħ and the 1/4 at GR:88, :617 (U1), :623 (b), :673 (Theorem) and :466 (§7.3).
- **Reading L** (#1245 c.6818970549; owner: current reading, c.6828106610). The shell energy is c⁴R/G, as GR:58 states it literally: the first-law energy is the whole hidden sector's energy.
- **Reading C** (same sources; conditional alternative). The first-law area tracks the boundary layer's energy E_B, and D shares energy on the shell.
- **H-inert** (proposed, not adopted; c.6818970549). The deep sector contributes an energy-independent factor to the shell count, with E_D = 0. Proposed sources: a gap ≫ k_BT_cl; an exactly decoupled factor (Main:60; Substratum Theorem 24(iii), Substratum:257); a constrained ensemble with E_D fixed.
- **H-eq** (proposed, not adopted). Reading C plus a horizon-dominated shell: local ρ < 1, global dominance, and smooth concave s_D.
- **W1′** (proposed, not adopted). The boundary's log-count, as a function of energy, is σA(E)/ε² with σ constant. Neither (U2) (GR:619) nor S3 (GR:665) supplies it.
- **Horizon dominance.** The shell count is dominated by the horizon-equilibrium macrostate. GR:58 presupposes it and GR:50 (C3) suggests it. S1 (GR:661), the de Sitter calibration (GR:56) and H-Hawking (GR:649) do not supply it (c.6818970549).
- **ρ** (re-derived here, §5 N2). With s_B as in GR:58, s_B′ = β and s_B″ = β/E_B, so C_B = −β²/s_B″ = −2s_B (a negative heat capacity). For the joint count s_B(E_B)+s_D(E−E_B), the interior stationary point is a local maximum iff C_D < 2s_B. Define ρ := C_D/(2s_B). Then dE_B/dE_H = 1/(1−ρ). This agrees with c.6818970549.
- **S1–S4**: GR:661–667. **Theorem**: GR:673 (part (b) conditions include H-count). Proof scope: GR:675.

## 4. Counterexamples

**Established (recorded on #1245 c.6818970549; internally reviewed, ACCEPT WITH CHANGES; not on `main`)**

- **CE-L (reading L, non-additive).** ln w_D(E) = r·σA(E)/ε² with r = O(1). D carries no energy, but its multiplicity depends on the shell energy. This is consistent with S1's "~10¹²²" and the named conditions, yet β_E = (1+r)·β_geo.
- **CE-X (extensive, thermally active deep sector).** O(1) heat capacity per ε³ cell. Re-checked here: C_D/2s_B = [(4π/3)R³/ε³]/[8πR²σ/ε²] = R/(6εσ) ≈ 7×10⁵⁹ per Hubble volume (R = c/H₀ ≈ 1.37×10²⁶ m, ε = 2l_p, σ = 1). So reading C has no locally stable, horizon-dominated maximum.

**Derived here (hand derivations, not reviewed)**

- **CE-0 (no ordered energy in the selected model).** SM:296 proves that the exact linear rule conserves E(u,v) = u·u+v·v−u·Av over ℤ/q, and that "E takes p values" at prime q = p. ℤ/p has no ordering compatible with addition, and the mod-p map does not conserve the integer lift. So ∂ln Ω/∂E, β_E and W1 are undefined for that conserved quantity. Recalled from memory and not load-bearing: by the standard Gauss-sum count for a quadratic form over a finite field, the level sets are equinumerous up to a relative error of order p^(−rank/2), which would make any "slope" zero.
- **CE-M (moving partition, volumetric deep term).** Take a fixed finite cell set and a horizon of radius R that tracks the shell energy through the first law. Let deep cells carry shell entropy s_cell each. Moving the horizon by dR changes N_B by 8πR dR/ε², N_V by 4πR² dR/ε³ and N_D by about −4πR² dR/ε³. So d ln Ω_H = σ·8πR dR/ε² − s_cell·4πR² dR/ε³. Relative to the boundary term this is r_M = −(s_cell/σ)·R/(2ε) ≈ −2×10⁶⁰·s_cell/σ. This is a physical instance of CE-L's non-additivity. It ignores the energy carried by transferred cells, so it is an order-of-magnitude statement.
- **CE-F (fixed partition with additive cells; the dS form fails, not the IR slope).** For N_B non-interacting cells, Cramér's theorem (standard) gives s_B(E) = N_B s\*(E/N_B) with s\* concave, so s_B″ ≤ 0 at leading order. GR:58's dS form needs s_H″ = +β/E = 2s_B/E², which is of the same order N/E². So a fixed boundary layer of local cells cannot realize W1′ in its de Sitter form along the family. Recalled from memory: the same concavity holds for short-range-interacting cells in the thermodynamic limit. Only the slope at one point (all that ħ uses, GR:74) survives.

## 5. Root nodes (framing results, derived here)

**N0. W1 presupposes a real-valued, conserved classical energy on hidden configurations. NEW.**
GR:58 counts substratum configurations on "a conserved energy shell". The energy it pairs with them is the first-law
energy of classical GR (GR:58, :98). Main:50 posits a classical H_tot = H_V+H_H+H_int on the idealized continuum Γ.
The selected discrete model supplies only the ℤ/p-valued invariant of SM:296 (CE-0). No construction on `main` maps
substratum configurations to a real energy identified with the horizon first-law energy. GR's stress-energy coupling is
G3, open (GR:12). β_E is defined only relative to such a map. **Assumption-watch W1-0:** a real-valued, conserved,
additive classical energy on substratum configurations, identified with the first-law energy. It is not stated among
the conditions at GR:88, :623 or :673.

**N1. Count, not state. ELABORATING.** By GR:58's definition, β_E depends only on the hidden configuration set, the
energy function and E. No condition on the hidden sector's *distribution* changes it. That covers thermalization, ETH,
(EM), typicality of the state, a KMS or Unruh state, and max-entropy selection of the state. A state-level mechanism can
enter only by changing *which* set is counted (§6 C1, C2). This rules out half the candidate list at the root.

**N2. Exact identity under additivity. NEW.**
Assume **H-add**: Ω_H(E) = Σ_x Ω_B(x) Ω_D(E−x), with x = E_B (B–D interaction negligible at the shell scale; this
parallels GR:58's V–H assumption). Let p(x) ∝ Ω_B(x)Ω_D(E−x) be the shell's split distribution. A finite difference δ
of the sum gives

- e^{δβ_E} = E_p[e^{δβ_B(x)}] + Ω_D(E+δ)Ω_B(0)/Ω_H(E), so to first order in δβ: **β_E = E_p[β_B(E_B)] + (weight of the no-horizon endpoint E_B ≈ 0).** Symmetrically, β_E = E_p[β_D(E_D)] + (weight of the all-in-B endpoint).
- With W1′ in GR:58's dS form on p's support, β_B(x) = k·x with k = 8πσG²/(c⁸ε²), which is linear. Hence, without any saddle approximation, **β_E = β_dS(⟨E_B⟩_shell)**.
- **Reading L** (geometric κ set by the total E): W1 ⇔ ⟨E_D⟩_shell = 0, with relative error exactly **r = −⟨E_D⟩/E**. This is H-inert's energy clause; D's energy-independent multiplicity follows from H-add.
- **Reading C** (κ set by the realized E_B): W1 ⇔ **E_B,realized = ⟨E_B⟩_shell**. The realized split must be the shell-typical split, which is dominance with concentration. A bimodal p (endpoint maxima, as in CE-X) gives a mean that matches no realized state.
- Checks: for small D in canonical equilibrium at β, ⟨E_D⟩ ≈ U_D(T_cl). The excess r ≈ −U_D/E ≈ −ρ·O(1) agrees with dE_B/dE_H = 1/(1−ρ) (§3). CE-L violates H-add.

**N3. What W1′ means depends on how the partition responds to E. NEW.** Main's partition Γ_V×Γ_H is fixed (Main:50).
GR's horizon is state-dependent (GR:40, :56).
- (G) Moving partition: σ is constant per cell and cells are added geometrically. W1′ then holds by construction, but cells transfer between D, B and V. CE-M gives a volumetric deep term unless s_cell ≲ 10⁻⁶⁰σ.
- (F) Fixed partition: W1′ is the claim that the boundary layer's *material* microcanonical temperature equals c²ε²κ/(8πGσk_B), for every de Sitter κ (GR:56 claims independence of which H calibrates). This is a classical "T ∝ κ" law. It is a state/material coincidence, and CE-F excludes its dS form for local cells.
- The corpus already uses a moving partition in the BH case (GR:605, a shrinking n_B(t)). Neither reading derives W1′.

## 6. Candidate mechanisms, depth-first

Each node gives: what the candidate would establish; its assumptions and whether they are already in OI; its result
against the counterexamples; whether it gives an independent prediction (§A.29); and a verdict.

**C1. Thermalization, ergodicity, ETH, (EM).**
- *Would establish:* a common temperature for B and D (zeroth law). That is the stationarity condition of reading C's saddle.
- *Assumptions:* ETH/(EM) are named in OI as motivation and conditional premises (Main:500, :744; ledger (v), Main:724). Shell ergodicity of the joint B∪D system is not in OI.
- *Against the counterexamples:* by N1, a state condition does not change the count. Equal temperature is necessary for an interior saddle but does not give dominance. Under CE-X the count is dominated by the no-horizon endpoint whatever the state. Ergodicity *worsens* reading L: an active D that shares energy gives r = −⟨E_D⟩/E ≠ 0 (N2).
- *Selected model:* SM:296 shows the exact linear rule's shells split into exponentially many cycles, so ergodic shell counting fails there. Mixing for the rounded rule is open (Main:724(v)).
- *Independent prediction:* none.
- *Verdict:* **does not establish W1**; it supplies only the equal-temperature half of H-eq. CONFIRMING.

**C2. Typicality and maximal-entropy principles.**
- *Would establish:* canonical typicality ([31] at Main:744) gives the Gibbs form *given* the count. That is GR:58's own step, and it is neutral on the value of β. Posit (iv) (Main:724) selects the uniform measure, which is the count itself; it adds nothing to dominance.
- *Assumption, new:* a max-entropy selection of the *macrostate* (the B/D split). That is new beyond (iv). It yields the saddle (H-eq) iff ρ < 1 and global dominance hold.
- *Against the counterexamples:* under CE-X it selects the no-horizon endpoint. With the observed horizon, it would imply only C_D(T_cl) < 2s_B ~ 10¹²². That bound concerns an unobservable sector, so it is not testable.
- *Pressure-test:* the actual hidden contents beyond the cosmological horizon (CMB at 2.7 K) are about 10³⁰ times hotter than T_GH ≈ 2.7×10⁻³⁰ K (computed with the calibrated ħ for orientation only). If D includes them, the realized state is far from the max-entropy split. That bears on reading C's "realized = typical" (N2), not on the count.
- *Verdict:* **does not establish W1.** CONFIRMING.

**C3. Holographic and horizon entropy bounds** (Bekenstein, 't Hooft–Susskind, Bousso's covariant bound, the de Sitter N-bound and finite dimensionality; all recalled from memory).
- *Tangency lemma (derived here).* If s_H(E) ≤ f(E) := σA(E)/ε² on a neighbourhood of E\*, with equality at E\* and both functions differentiable, then s_H′(E\*) = f′(E\*). That is W1.
- *Pressure-test:*
  - (a) The physics form S ≤ A/4l_p² contains ħ. Using it to fix the 1/4 that OI derives is circular.
  - (b) An OI-native bound *with* an additive constant is W1 plus a second-order condition: it adds no content.
  - (c) An *absolute* OI-native bound needs s_D(E\*) ≈ 0. That is H-inert's entropy clause restated, and a new premise. The corpus's own use of holographic bounds is scoped to C_V×C_B "for a finite deep sector of any size" (GR:585; Substratum Corollary (i), Substratum:268). Extending it to D is new (H-holo).
  - (d) As recalled from memory, standard physics keeps the outside matter's entropy separate, S_gen = A/4 + S_out. Covariant-bound inequalities bound changes of S_out by area changes, which would bound |r| at O(1), not force r = 0. No verdict rests on this.
- *Against the counterexamples:* the bound excludes CE-L and CE-X only by fiat: they are exactly violations of it.
- *Independent prediction:* none, since the hidden sector is inaccessible.
- *Verdict:* **does not establish W1** without a saturation premise equivalent to H-inert. ELABORATING.

**C4. Equivalence principle, locality, and Jacobson's local-Rindler argument** (literature recalled from memory).
- *What the literature assumes:* Jacobson (1995) takes δS = ηδA for the heat flux across every local horizon as an input. That is area-entropy completeness, i.e. W1-like, assumed rather than derived (agrees with c.6818970549).
- *What it shows instead:* in QFT, the first law of entanglement with Bisognano–Wichmann modular flow makes the outside (deep) sector's entropy slope equal to the KMS β *automatically*, at first order around the vacuum. Existing physics therefore realizes the analogue of W1 the reading-C way (equal slopes), not by inertness.
- *Pressure-test:* this lives on the τ_K side. It is a statement about the emergent quantum state, it uses ħ, and it is H-spectrum's territory (GR:60, :144). Carrying it into the classical count needs configuration energies to be emergent eigenvalues, the naive H-energy that GR:84 proves is a no-go. Classically, Gibbs/KMS states exist for every β, and T_Unruh → 0 as ħ → 0. No classical mechanism fixes β geometrically, which is why T_cl must come from counting.
- *Verdict:* **does not establish W1.** BORDERLINE as structural support for keeping reading C as the alternative; it is not evidence for OI.

**C5. Unruh/Hawking universality** (temperature universality, dispersive robustness; GR:649 cites Schützhold–Unruh).
- *Would establish:* the KMS period τ_K under H-Hawking. That is the emergent side, and it uses ħ.
- *Against the definition:* by N1 it is silent on the count.
- *Verdict:* **does not establish W1.** CONFIRMING.

**C6. Decoupling of deep sectors.** Three sub-branches; (a) was decisive and was walked first.

- **(a) Gap / EFT decoupling (H-inert via gap).**
  - *Would establish (derived here):* by N2, with dilute deep excitations of granularity Δ on N_eff sites, r = −N_eff(βΔ)e^{−βΔ}/(2s_B). So W1 holds iff βΔ ≳ ln(N_eff/2s_B). For per-cell excitations in a Hubble volume (N_eff ≈ 3×10¹⁸², 2s_B ~ 10¹²²) that is βΔ ≳ 1.4×10². In calibrated units, for orientation only, Δ ≳ 5×10⁻⁵¹ J.
  - *Pressure-test (decisive):* H-slope is defined by the IR expansion in ΔE about 0 (GR:74), with probe gaps at τ_Kω ~ O(1) (GR:66). So the classical visible sector must carry configuration-energy differences at or below k_BT_cl. Translation invariance (A4; ledger (xi), Main:724) puts the same granularity in D. Whether D's low-energy configurations are extensive (per cell, as in CE-X) or collective (about one per Hubble volume, harmless) is fixed nowhere in the corpus. The quantum freeze-out that would give "collective", with radiation at T_GH carrying O(10⁻²) entropy per Hubble volume, needs the naive H-energy map, which GR:84 refutes.
  - *Against the counterexamples:* CE-L survives (it violates H-add, not the gap). CE-X is excluded only by hypothesis.
  - *Verdict:* **conditional sufficient route, not derived.** The decisive unknown is the classical low-energy configuration density of the deep sector. NEW (it identifies that unknown, and the GR:84 block on the freeze-out route).
- **(b) Causal one-way decoupling at the event horizon.**
  - *Would establish:* with D→B influence zero (L = 0), V×B is autonomous; the operational, sector-wise slope is s_B′, so W1 would reduce to W1′.
  - *Pressure-test:*
    - It uses *emergent* GR causal structure to constrain a *substratum* count: a Step-5 level mismatch.
    - The selected linear update has L ≠ 0 at every site-local cut with a deep neighbour (GR:128; #1245 c.6818702013).
    - GR:46 asserts bidirectional coupling at the horizon.
    - Even if granted, it leaves W1′ (N3) undischarged.
  - *Verdict:* **does not establish W1**; refuted in the selected model at site-local cuts. CONFIRMING.
- **(c) Exact decoupling** (Main:60; Substratum Theorem 24(iii)).
  - *Result:* an adjoined factor with product dynamics conserves its own energy. Sector-wise counting drops it, so ħ is unchanged. POSITIVE: enlargement is a gauge direction of ħ *for that class*.
  - *Gem:* a factor placed on the *joint* shell is not a product preparation (GR:86 makes the same distinction). Under reading L it shifts β_E by r = −⟨E_D⟩/E (N2), and is then visible in rate ratios. "Deep-sector enlargement is gauge for ħ" therefore holds exactly for energy-decoupled factors only.
  - *Verdict:* **does not cover the coupled D of GR §3.2's chain V↔B↔D.**

**C7 (side node). The identity of the first-law energy. BORDERLINE.** Derived here: with Friedmann H² = 8πGρ/3 and
R = c/H, the Misner–Sharp energy *inside* the Hubble sphere is E_MS = c⁴R/(2G). GR:58's E = c⁴R/G is therefore twice
an interior (visible-side) quantity. Recalled from memory: cosmological apparent-horizon thermodynamics (Cai–Kim;
Hayward) pairs horizon entropy with interior Misner–Sharp energy and a work term. Assigning c⁴R/G to the hidden sector
(reading L) is an identification worth review. ħ is unaffected, because only the differential pairing dE_H = energy
received by H enters (GR:70, :74). Assumption-watch marker only.

## 7. Hard-to-vary assessment (§A.29)

- No candidate gives an independent prediction or postdiction beyond W1. The structural reason is recorded in c.6818970549 and re-checked here: if W1 fails by r, then ħ = c³ε²/(4Gσ_eff), ε = 2√σ_eff·l_p and A/4l_p² are all unchanged with σ_eff = σ(1+r). Only σ's reading as entropy per boundary mode, and the boundary-count reading of the 1/4, move.
- So W1 is empirically inert inside the calibration. A hard-to-vary mechanism would need *independent* fixes of σ and ε (GR:98 and :102 fix neither), which none supplies.
- Tunability: the H-eq route carries a free ρ ∈ [0,1) that moves GR:58's literal form and §7.3's boundary share (c.6818970549). H-inert fixes ρ = 0 and has no free parameter, but it predicts nothing beyond the results it was built to preserve.

## 8. Conclusion

No tested mechanism from existing physics establishes H-inert, horizon dominance, or another sufficient condition for
W1 from OI's existing premises without adding a premise that is W1, or H-inert, restated. The mechanisms that fix a
*state* cannot fix a *count* (N1). The holographic bound gives W1 only when saturated, which is H-inert's entropy clause
(C3). The equal-temperature physics of QFT lives on the ħ side (C4–C5). Deep-sector decoupling works for
energy-decoupled factors only, and for gapped deep sectors only conditionally (C6). **W1 is an additional physical
assumption, not a derived result.**

**Minimal form.** Only the infrared slope at the realized shell is load-bearing for ħ and the 1/4 (GR:74, :82).
- **W1-0 (prerequisite).** A real-valued classical energy, conserved by φ and additive across V/H at the shell scale, is defined on hidden configurations and identified with the energy the hidden sector receives in the horizon first law (N0).
- **W1-min.** At the realized horizon (surface gravity κ\*), the log-derivative of the number of hidden configurations on the realized, dynamically connected energy sector, with respect to the energy received from V, equals 8πGσ/(c²κ\*ε²).
- H-count as written at GR:58 is **strictly stronger** than W1-0 + W1-min. It adds the global law s_H = σA/ε², E = c⁴R/G, s_H″ = β/E, and E_D = 0. Those extras are consumed by GR:58's de Sitter statements and the δ_bath estimate, and by §7.3's boundary share (c.6818970549). They are not consumed by ħ or the 1/4.
- Under H-add, W1-min becomes ⟨E_D⟩ ≈ 0 in reading L, or "realized = shell-typical split" in reading C (N2). Readings L and C keep their recorded standing.

## 9. Status table

| Item | Status | Support |
|---|---|---|
| H-count is not supplied by S1–S4 | Stated in the manuscript | GR:58, :88 |
| Only the IR slope β_E is load-bearing for ħ | Manuscript derivation | GR:74, :78–82 |
| Selected linear rule conserves a ℤ/p-valued E | Proved (SM) | SM:296 |
| Naive H-energy (configuration energies = eigenvalues) is a no-go | Manuscript proof | GR:84 |
| Exactly decoupled finite deep factor: T_ij unchanged | Proved | Substratum Thm 24(iii) (:257); Main:60 |
| CE-L, CE-X; reading-C stability C_D < 2s_B; σ → σ(1+r) absorption | Recorded, internally reviewed, off `main` | #1245 c.6818970549 (CE-X ratio and ρ re-derived here) |
| N0 / CE-0: β_E undefined for SM:296's invariant | Derived here | §4, §5 |
| N2: β_E = E_p[β_B] (+ endpoint); dS linearity ⇒ β_E = β_dS(⟨E_B⟩); reading L ⇔ ⟨E_D⟩=0, r = −⟨E_D⟩/E; reading C ⇔ realized = typical split | Derived here (under H-add) | §5 |
| CE-M: moving-partition term r_M ≈ −2×10⁶⁰ s_cell/σ | Derived here (order of magnitude) | §4 |
| CE-F: additive fixed boundary layer has concave s_B | Derived here (Cramér, independent cells) | §4 |
| Tangency lemma (saturated bound ⇒ equal slopes) | Derived here | §6 C3 |
| Gap route: W1 iff βΔ ≳ ln(N_eff/2s_B) | Derived here (dilute limit) | §6 C6(a) |
| W1 under H-add ∧ W1′ ∧ ⟨E_D⟩≈0 (L), or ∧ concentration at the realized split (C) | Conditional | §5 N2 |
| Ergodic B∪D shell counting in the selected model | Fails (cycle splitting) | SM:296 |
| Classical low-energy configuration density of D | Open (decisive) | §6 C6(a) |
| W1′; global dominance; the substratum → real-energy map (W1-0) | Open | §5 N0, N3; GR:12 (G3) |
| W1 itself | Additional physical assumption (not derived) | §8 |

## 10. Assumption-watch markers (cross-propagation)

- **W1-0** (real conserved energy on configurations). This also bears on GR §A (Theorems A.8–A.9 "energy shell", GR:797, :829), on SM:1227(ii) ("uniform measure on a T-invariant energy shell"), and on any use of "energy shell" for the exact linear rule.
- **Count vs state** (N1). Any future claim that a thermalization or KMS property fixes β_E should be checked against it.
- **Moving partition** (N3, CE-M). This bears on every use of σA(E)/ε² as a function of energy, including §7.3's Clausius step (GR:468).
- **Enlargement gauge for ħ only for energy-decoupled factors** (C6(c)). This bears on GR:132–138 and Structure:205/:305 if they are read as covering ħ.
- **First-law energy identity** (C7, BORDERLINE).

## 11. Reading inventory

- `AGENTS.md` (in full, as loaded).
- Issue #1245: the body and all 5 comments (c.6818702013, c.6818793241, c.6818970549, c.6828106610, c.6829744096).
- Issue #1244: the body and all 19 comments, including item 1–3 audits, the H-BD posit record, and the A/4-condition decisions (c.6824042569, c.6826832441, c.6829741165).
- `papers/GR.md` @fb733b4: :1–160 in full (§1, §2.1–2.3, §3.1–3.2 including H-BD and the corollary), :330–340, :460–480, :575–590, :599, :605–679 (§8.5 in full: U1–U3, (b), S1–S4, Theorem, proof scope). It was also grepped for deep-sector, equilibrium and H-count sites.
- `papers/Main.md` @fb733b4: :42–60 (Definition, Lemmas 1–3, measure Remark, the status Remark including the deep-factor statement), :74 ((C2)), :84, :443–451 and :498–502 (ETH and the mixing hypothesis), :724–736 (posit ledger items (i)–(xii) and the status ledger), :742–758 (§4.6, (EM)).
- `papers/Substratum.md` @fb733b4: :135, :181–191 (including Lemma 23.0), :251–268 (Theorem 24, the effective-finiteness corollary).
- `papers/SM.md` @fb733b4: :296 (cycle structure, the conserved E).
- `verification/` @fb733b4, grepped for `W1`, `H-inert`, `H-eq`, `W1′`/`W1'`, `horizon dominance`, `H-count`, `deep sector`, entropy-slope terms. No record on `main` concerns this W1: every `W1` hit is an unrelated label (pseudoentropy literature item, probe IDs, round CV-2). There are no `H-inert`, `H-eq`, `W1′` or `horizon dominance` hits. The deep-sector hits read (bh-consistency FINDINGS:94/164, observer-relative-finiteness DEPENDENCY-AUDIT:126/338, LEDGER.json:59/2326/2473, lemma-24-1 result:197–276) concern T_ij-level decoupling, not the entropy slope. **The established W1 counterexamples exist only in #1245 c.6818970549 (off `main`).**

## 12. Limits

- Hand derivations, not machine-checked, and no independent review yet. The unit requires an independent review and an owner checkpoint before any use.
- All literature (Jacobson 1995/2016, Bisognano–Wichmann, first law of entanglement, Bousso, the N-bound, Hawking 1976 box stability, Thirring and Lynden-Bell on negative heat capacity, Cai–Kim, Gauss-sum counts) is recalled from memory. No verdict rests on it; each verdict rests on corpus lines or on the derivations above.
- N2 assumes H-add and, for the linear form, W1′'s dS form on the whole support of p. CE-M ignores the energy carried by transferred cells. The numerical orientation values use the calibrated ħ and illustrate scale only.
- The candidate list is the one requested plus C7. It is not proven exhaustive. The last three passes (C5, C6(b), the §7 re-check) gave no NEW item.
- Provenance note: before creating this directory I wrote `origin/main` copies of `papers/GR.md` and `papers/Main.md` to `GR.md` and `Main.md` at the working root. Same-named files already existed there, of unknown origin, and were overwritten. Their earlier content is not recoverable from this session. The working copies for this unit are in `w1-1/src/`.
