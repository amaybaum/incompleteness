# W1-1 (r4): can existing physics supply W1 (the hidden-sector entropy-slope / thermal-matching condition)?

This is unit W1-1, a paper-only investigation authorized by the owner (amaybaum, 2026-11-12, #1245 c.6829744096).

- **Base.** `origin/main` `fb733b4a58558ef64bd7c3585712c76e9f2dfb42`, read with `git show`. Line numbers are at that commit.
- **Method.** Reading and hand derivations only. There was no computation on OI rules and no Lean work. No manuscript was edited, no premise adopted and no claim promoted.
- **Revision.** r2 applied the required changes F1–F12 of the independent review (`w1-1/REVIEW-W1-1.md`, ACCEPT WITH CHANGES). The focused re-check of r2 (`w1-1/REVIEW-W1-1-r2.md`) returned ACCEPT WITH NITS. r3 applied its nits N1–N7. Under the owner's gate (2026-11-13) r3 was delta-reviewed (`w1-1/DELTA-REVIEW-W1-1-r3.md`, ACCEPT WITH CHANGES), and r4 applies its required edits E1–E10. No verdict label moved from r2.
- **Readings.** Reading L stays the current manuscript reading and reading C stays the conditional alternative (#1245 c.6828106610).

## 0. Changes from r1, and whether any verdict moved

- **F1.** N0 / W1-0 is reclassified from NEW to **ELABORATING**. SM:292, SM:811 and GR:695 already state the substance. The gap that remains is narrower: the ħ condition lists (GR:88, :623, :637, :673) and Main's ledger (Main:724) do not carry the assumed shell.
- **F2.** The N2 identity is now stated as a lattice forward-difference identity. Its first-order reading carries an endpoint term p(0)e^{δβ_D}/δ and a (δ/2)Var_p(β_B) correction, and every ⇔ carries its hypotheses in both directions.
- **F3.** The "mean boundary energy" form rests on two hypotheses (H-add and W1′ in de Sitter form). That pair is not jointly realizable by local cells under either partition reading.
- **F4.** The σ-absorption of a W1 excess is restricted to 1+r > 0.
  - r ≤ −1 removes the β_E > 0 premise under which GR:186/:210 call the classical layer settled.
  - r < −1 also violates the Monotone-Ω hypothesis of `counting_passive`.
  - CE-M falls in that regime for s_cell ≳ 5×10⁻⁶¹σ.
- **F5.** "H-count strictly stronger" is replaced by a one-way implication with a witness for the failed converse. Each part of the condition list is tied to its source, κ\* is fixed per reading, and the GR:86 versus GR:70/:74 additivity tension is recorded.
- **F6.** C3 now engages GR:50, GR:661 and Substratum:268(i). A capacity bound fixed at the realized area gives slope 0. A saturated absolute bound forces s_D ≈ 0.
- **F7.** "Fixed nowhere" is narrowed. The real lift of the linear rule (SM:292) is shown, by a hand derivation, to realize CE-X.
- **F8.** The gap route is listed as a distinct open sufficient premise.
- **F9.** The counterexamples are relabelled "Recorded".
- **F10.** Cross-propagation sites are added, and the C1 cycle-splitting line is scoped.
- **F11.** Provenance note added.
- **F12.** Minor fixes made.

**Verdicts.**
- *Headline: unchanged.* W1 is an additional physical assumption, not a derived result.
- *What moved:*
  - N0 is now ELABORATING.
  - N2 is a first-order, conditional result rather than an "exact" one.
  - The H-count comparison is narrowed to one direction.
  - The gap route is an open, distinct premise rather than a restatement of H-inert. Its natural real-energy realization fails (F7), which strengthens the negative conclusion.
  - The §A.29 inertness of W1 holds only for 1+r > 0.
  - C3 is stronger: the corpus's own capacity statements give slope 0.

**r3 nits (N1–N7 of `REVIEW-W1-1-r2.md`).** These are precision fixes only. No verdict moved.
- **N1.** F4 wording: r ≤ −1 *removes a premise* rather than contradicting a stated fact; r < −1 *violates* `counting_passive`'s hypothesis; and "uniform" becomes "uniform to first order".
- **N2.** The validity conditions of N2's first-order form are added. The ⇐ direction under reading L is exact on the lattice under an added endpoint condition.
- **N3.** The F5 witness violates H-count at second order (over shell-scale e_i, ~10⁻¹²³, the δ_bath order).
- **N4.** The gap route is narrowed to *collective* deep configurations, and the real-lift negative is marked as immediate.
- **N5.** C3(c) now says the bound "goes beyond" GR:585 rather than "conflicts with" it.
- **N6.** CE-RL's assumptions a = ε and K components per site are stated.
- **N7.** The status of `counting_passive` is relabelled.

## 1. Plain-language summary

1. W1 says the whole hidden sector's entropy rises with energy at the same rate as the horizon's boundary count. That rate sets the classical horizon temperature the ħ calibration needs (GR:58, :74, :78–82).
2. None of the existing physics tested here establishes W1. Each candidate either fixes the hidden sector's state (W1 is about its count), uses ħ, needs a premise that restates W1 or H-inert, or needs a distinct open premise: a deep sector whose low-energy configurations are collective. That open premise is undetermined for the finite substratum, and it fails in the corpus's one real-energy model.
3. Under B/D energy additivity, the hidden slope equals the shell average of the boundary slope, plus an endpoint term and a small correction, to first order in the energy step. The "slope at the mean boundary energy" form further needs W1′ in de Sitter form. Local cells cannot supply that together with additivity.
4. W1 presupposes a real-valued conserved energy. The corpus already says this is assumed (GR:695, SM:292). The ħ condition lists do not carry it.
5. In the real lift of the linear rule (SM:292, |α| < 1/d), the classical hidden count is extensive. W1 then fails by a factor of about 7×10⁵⁹ (derived here).
6. Tying the count to the horizon area forces either a moving partition, which adds a volumetric deep term of order 10⁶⁰·s_cell/σ (order of magnitude, if deep cells carry entropy s_cell), or a coincidence of material temperatures.
7. A W1 excess with 1+r > 0 is absorbed into σ, so W1 then has no test inside the calibration. With r ≤ −1 the β_E > 0 premise is lost, the premise under which GR:186/:210 call the classical layer settled. For r < −1 the classical temperature is negative. No candidate gives a hard-to-vary independent prediction (§A.29).
8. **Verdict: W1 is an additional physical assumption.** Its minimal form, with the comparison to H-count, is in §8.

## 2. Pre-stated productivity test (§A.31)

This test was fixed before the walk. A node is a **gem** iff it yields a fact strictly stronger than the restatement
"S1–S4 do not supply W1" (already recorded at GR:58 and #1245 c.6818970549), *and* it either constrains W1's
possible sources or exposes a hidden assumption.

Nodes were walked depth-first, decisive branch first. Branches favourable to W1 were pressure-tested first. Output
classes: NEW / POSITIVE / ELABORATING / CONFIRMING / BORDERLINE.

## 3. Definitions (from the sources)

**The shell and β_E**
- GR:58: "Restrict the finite total system to a conserved energy shell … If the boundary interaction is negligible at the shell scale, uniform counting gives P(i)=Ω_H(E−e_i)/Σ_jΩ_H(E−e_j)", with s_H = ln Ω_H.
- GR:70: N_i = |M_i| = Ω_H(E−e_i) and ln(P_ij/P_ji) = −β_E(e_j−e_i)+…, with β_E = s_H′(E).
- GR:74: "Only the infrared slope is load-bearing"; E′(0) = τ_K/β_E = ħ.

**W1** (#1244 c.6817396025; #1245 c.6818970549)
- β_E, counted over all of H = B ∪ D on the total-energy shell, equals ∂(σA/ε²)/∂E along dE = c²κ dA/(8πG) (GR:98).
- Equivalently, k_BT_micro = k_BT_cl = c²ε²κ/(8πGσ) (GR:100). Write β_geo(κ) := 8πGσ/(c²κε²).

**H-count** (GR:58, verbatim; the manuscript's posited carrier of W1)
- "the energy-dependent entropy of the whole hidden sector at the shell scale is the boundary count, s_H=σA/ε² up to an energy-independent constant, the shell energy E being the energy of the horizon first law and the deep hidden sector contributing no energy-dependent multiplicity and, by the choice of energy zero, no energy; S1–S4 do not supply it".
- On exact de Sitter: E = c⁴R/G, s_H = 4πσG²E²/(c⁸ε²), s_H″ = β/E.
- It is a condition of ħ and the 1/4 at GR:88, :617, :623, :673 and :466.

**Readings L and C** (#1245 c.6818970549; status from c.6828106610)
- **L (current):** the shell energy is c⁴R/G, i.e. the first-law energy is the whole hidden sector's energy.
- **C (alternative):** the first-law area tracks the boundary energy E_B, and D shares energy on the shell.

**Proposed hypotheses** (all unadopted; c.6818970549)
- **H-inert:** D contributes an energy-independent factor, with E_D = 0.
- **H-eq:** reading C, a horizon-dominated shell, local ρ < 1, global dominance, and a smooth concave s_D.
- **W1′:** the boundary log-count as a function of energy is σA(E)/ε² with σ constant. It is not supplied by (U2) at GR:619 or by S3 at GR:665.

**Horizon dominance.** The shell count is dominated by the horizon-equilibrium macrostate. GR:58 and GR:50 (C3)
presuppose it (c.6818970549). S1 (GR:661), the de Sitter calibration (GR:56) and H-Hawking (GR:649) do not supply it.

**ρ** (re-derived and confirmed by review)
- s_B′ = β and s_B″ = β/E_B, so C_B = −2s_B.
- The interior stationary point is a local maximum iff C_D < 2s_B.
- With ρ := C_D/(2s_B), dE_B/dE_H = 1/(1−ρ).

**Structural conditions.** S1–S4 are at GR:661–667, the Theorem at GR:673, and the proof scope at GR:675.

## 4. Counterexamples

**Recorded on #1245 c.6818970549** (internally reviewed, off `main`; not established in the §A.46 sense). This unit
re-verified both on paper, and the review re-confirmed CE-X's ratio.

- **CE-L (reading L, non-additive).** ln w_D(E) = r·σA(E)/ε² with r = O(1). D carries no energy, but its multiplicity depends on E. Then s_H = (1+r)σA/ε² + const, so β_E = (1+r)β_geo.
- **CE-X (extensive, thermally active deep sector), with S1's capacity read as boundary capacity.** O(1) heat capacity per ε³ cell. C_D/2s_B = R/(6εσ) ≈ 7.1×10⁵⁹ per Hubble volume (R ≈ 1.37×10²⁶ m, ε = 2l_p, σ = 1). In reading C there is then no locally stable maximum dominated by the horizon.

**Derived here** (hand derivations, reviewed once)

- **CE-0: no ordered energy in the selected model.** SM:296 and SM:292 show the exact linear rule conserves E only modulo q. For ℤ/p-valued E there is no ordering compatible with addition, so no derivative exists. Only a finite-difference analogue is available, and near-equinumerous level sets would make it ≈ 0, which is infinite temperature (the r = −1 boundary of F4). The level-set count is recalled from memory as the standard Gauss-sum count and is not load-bearing.
- **CE-M: moving partition** (order of magnitude, if deep cells carry shell entropy s_cell).
  - Setting: a fixed finite cell set, and a horizon R that tracks E through the first law.
  - Cell counts: dN_B = 8πR dR/ε² and dN_V ≈ −dN_D ≈ 4πR² dR/ε³.
  - Result: r_M = −(s_cell/σ)·R/(2ε) ≈ −2×10⁶⁰ s_cell/σ. This ignores the energy carried by transferred cells. It falls in the non-absorbable regime r < −1 for s_cell ≳ 5×10⁻⁶¹σ (F4).
- **CE-F: fixed partition with additive cells.**
  - For N_B independent cells, Cramér's theorem gives s_B = N_B s\*(E/N_B) with s\* concave, so s_B″ ~ −N/E².
  - The de Sitter form needs s_B″ = +2s_B/E², the same order with the opposite sign.
  - So the de Sitter form of W1′ is excluded at leading order. The IR slope at one point is not excluded.
  - The extension to short-range-interacting cells is recalled from memory.
- **CE-RL: the real lift realizes CE-X.** See §6 C6(a′), F7.

## 5. Root nodes

**N0. W1 presupposes a real-valued, conserved classical energy. ELABORATING (F1).**

What the corpus already states:
- GR:58 opens with "Restrict the finite total system to a conserved energy shell".
- GR:695: "The shell is assumed, as in §2.3; it is not a consequence of Lemma 3, which supplies determinism, injectivity and the selected measure but no conserved energy."
- SM:292: "The exact linear rule over ℤ/qℤ conserves E below only modulo q … The rounded rule has no nonconstant polynomial invariant of degree at most two in the computed instances. Neither fact supplies the required real positive-definite conserved energy."
- SM:811 sets out a real-valued conserved energy only as a candidate.
- The real lift does carry a real conserved E. It is positive definite for |α| < 1/d, positive semidefinite at α = 1/d with null modes, and indefinite at α = 1 for d ≥ 2. Its null and indefinite directions have noncompact shells (SM:292). The real lift is not the finite substratum.
- Main:50 states H_tot = H_V + H_H + H_int, and Main:52 says the product decomposition is idealized.
- The identification clause ("the shell energy E being the energy of the horizon first law") is already inside H-count's text (GR:58).

The narrower gap is that the ħ / 1/4 condition lists (GR:88, :623, :637, :673) do not carry the assumed shell, and
Main's posit ledger (Main:724) has no real-energy posit.

**Assumption-watch W1-0.** A real-valued energy, conserved by φ, additive across V/H at the shell scale, and identified
with the energy H receives in the first law.

**N1. Count, not state. ELABORATING.** β_E depends only on the configuration set, the energy function and E (GR:58).
No condition on the hidden sector's distribution changes it, and that covers thermalization, ETH, (EM), typicality,
KMS/Unruh states, and max-entropy selection of a state. A state-level mechanism can matter only through which set is
counted, or through whether one orbit realizes the shell rates (SM:292: single-cycle ergodicity is needed to identify
the empirical law of one occupied orbit with the uniform law on the whole shell).

**N2. Shell slope as an average of boundary slopes. NEW (F2, F3).**

*Assumptions.*
- **H-add:** Ω_H(E) = Σ_x Ω_B(x)Ω_D(E−x).
- B and D share a common energy lattice of step δ, with E_B, E_D ≥ 0.
- p(x) := Ω_B(x)Ω_D(E−x)/Ω_H(E).
- β_B and β_D are forward-difference slopes.

*Identity (exact as a lattice identity).*
- Ω_H(E+δ)/Ω_H(E) = Σ_x p(x)·Ω_B(x+δ)/Ω_B(x) + p(0)·e^{δβ_D(E)}.

*First-order reading.*
- **β_E ≈ E_p[β_B(E_B)] + (δ/2)·Var_p(β_B) + p(0)e^{δβ_D(E)}/δ.**
- Validity:
  - δβ_B ≪ 1 on the support of p, so that third and higher cumulants of δβ_B are negligible, and δβ_D(E) ≪ 1, so that e^{δβ_D(E)} ≈ 1;
  - p(0) ≪ 1, so that ln(1 + p(0)e^{δβ_D}/E_p[e^{δβ_B}]) ≈ p(0)e^{δβ_D}. Exactly, δβ_E = ln E_p[e^{δβ_B}] + ln(1 + p(0)e^{δβ_D(E)}/E_p[e^{δβ_B}]); when p(0) is not small the endpoint enters as ln(1 + p(0)e^{δβ_D(E)}/E_p[e^{δβ_B}])/δ.
- The endpoint term is negligible only if p(0) ≪ βδ. That is stronger than "small endpoint weight".
- The variance term vanishes only as δ → 0, a limit a discrete lattice does not have. It is negligible if δ·Var_p(β_B) ≪ β.

*With W1′ in de Sitter form on p's support* (s_B = (k/2)x², k = 8πσG²/(c⁸ε²)):
- β_B(x) = kx + kδ/2. Then E_p[β_B] = β_dS(⟨E_B⟩) up to the same kδ/2 offset that β_geo carries.
- Hence, to first order in δ and with the endpoint and variance terms negligible:
  - **Reading L** (κ set by the total E): **W1 ⇔ ⟨E_D⟩_shell = 0**, and r = −⟨E_D⟩/E plus the two correction terms.
  - **Reading C** (κ set by the realized E_B): **W1 ⇔ E_B,realized = ⟨E_B⟩_shell.**
  - Both directions of each ⇔ hold only under all of: H-add, W1′ in de Sitter form on the support of p, the common lattice, δβ_B, δβ_D ≪ 1 on the support of p, p(0) ≪ βδ (which implies p(0) ≪ 1), and δ·Var_p(β_B) ≪ β (§A.34).
  - Exception: in reading L, ⟨E_D⟩ = 0 forces E_B = E on the shell, so Var(E_B) = 0 and p(0) = 0 for E > 0. The endpoint term of the identity is Ω_B(0)Ω_D(E+δ)/Ω_H(E), which p(0) = 0 does not remove. If also Ω_B(0)Ω_D(E+δ) = 0 and W1′(dS) holds at E and E+δ, then β_E = β_B(E) exactly, and the ⇐ direction holds exactly on the lattice with β_geo read as the forward difference of σA(E)/ε² (otherwise up to the kδ/2 offset). Only ⇒ needs the smallness conditions.
  - The kδ/2 offset is a relative O(δ/E) correction, negligible on either reading.

*Limits of the mean-energy form (F3).*
- The mean-energy form needs H-add together with W1′ in de Sitter form on all of p's support.
- For local cells, CE-F excludes the de Sitter form on a fixed partition, and CE-M breaks H-add on a moving partition.
- So that pair is not realized by local cells under either partition reading.
- The robust result is the general average-plus-endpoint identity. When p is concentrated at E_B\*, β_E ≈ β_B(E_B\*) without linearity, and "mean versus realized" matters only for a broad p.

*Cross-check.* For a small canonical D, r ≈ −U_D/E ≈ −ρ·O(1), consistent with dE_B/dE_H = 1/(1−ρ). CE-L violates H-add.

**N3. The partition reading of W1′. NEW.** Main's partition is fixed (Main:50). The horizon is state-dependent (GR:40, :56).
- **(G) Moving partition.** W1′ holds by construction, but cells transfer between D, B and V. That gives CE-M.
- **(F) Fixed partition.** W1′ becomes a material-temperature coincidence, T_material(E_B) ∝ κ for every de Sitter κ, which is a classical "T ∝ κ" law. CE-F excludes its de Sitter form for local cells.

The corpus already uses a moving partition for black holes (GR:605, n_B(t)). Neither reading derives W1′.

## 6. Candidate mechanisms, depth-first

**C1. Thermalization, ergodicity, ETH, (EM).**
- *What it would supply:* a common B/D temperature, i.e. the saddle-stationarity condition of reading C.
- *Status in OI:* ETH and (EM) appear as motivation and as conditional premises (Main:500, :744; ledger item (v) at Main:724). Joint shell ergodicity of B ∪ D is not in OI.
- *Against W1 (by N1):* none of these changes the count. Under CE-X the count is dominated by the no-horizon endpoint whatever the state, and under reading L an active, energy-sharing D gives r ≠ 0.
- *Scope (F10).* The cycle splitting of the exact linear rule (SM:294, :296) does not change the shell count (SM:292). It bears only on whether one orbit realizes the shell rates.
- *Prediction:* none.
- **Verdict: does not establish W1.** CONFIRMING.

**C2. Typicality and maximal entropy.**
- *Typicality:* canonical typicality ([31], Main:750–758) gives the Gibbs form from a given count, so it is neutral on β. Posit (iv) (Main:724) selects the uniform count itself.
- *Max-entropy selection of the split:* this is new beyond posit (iv). It yields H-eq only if ρ < 1 and the global maximum is the horizon one.
- *Under CE-X:* it selects the no-horizon endpoint. Combined with the observed horizon it would give C_D(T_cl) < 2s_B, a bound on an unobservable quantity.
- *Pressure-test:* if D includes the actual beyond-horizon contents (CMB at 2.7 K against T_GH ≈ 2.7×10⁻³⁰ K, the latter computed with the calibrated ħ for orientation only), the realized state is far from the max-entropy split. That bears on reading C's "realized = typical" (N2), not on the count.
- **Verdict: does not establish W1.** CONFIRMING.

**C3. Holographic and entropy bounds (F6).**
- *Tangency lemma (derived; confirmed by review).* Suppose s_H(E) ≤ f(E) on a neighbourhood of an interior E\*, with equality at E\* and both differentiable. Then s_H′(E\*) = f′(E\*).
- *The corpus's own capacity statements* are GR:50 (C3: "Hidden sector has A/ε² modes"), S1 (GR:661: capacity S_dS) and Substratum:268(i) (|C_V×C_B| ≤ e^{S_∂}). At the realized A each of these is **constant in E**.
  - Saturated at E\*, such a constant bound gives s_H′(E\*) = 0, i.e. β_E = 0, not β_geo.
  - With β_E > 0 it can be saturated only at the edge of the allowed energy range.
  - A bound yields W1 only if it tracks A(E) through the first law, which is the moving partition of N3 and CE-M. This is the precise form of GR:58's "fixing no entropy–energy slope".
- *Other cases.*
  - (a) The physics form A/4l_p² contains ħ, so using it is circular for the 1/4.
  - (b) An OI-native bound with an additive constant reduces to W1 plus a second-order condition.
  - (c) An absolute saturated bound with s_B = σA/ε² forces s_D ≈ 0. That is a trivial D factor on the shell: a special case of H-inert and strictly stronger than it. It also goes beyond the corpus's scoping of holographic bounds to C_V×C_B "for a finite deep sector of any size" (GR:585), which allows a deep sector of any size and does not bound D's shell count.
  - (d) Standard generalized-entropy bookkeeping keeps S_out separate (recalled from memory, not load-bearing).
- *Against the counterexamples:* CE-L and CE-X are excluded only by fiat.
- *Prediction:* none.
- **Verdict: does not establish W1.** ELABORATING.

**C4. Equivalence principle, locality, and Jacobson's argument.**
- Jacobson (1995) takes δS = ηδA as an input (recalled from memory).
- In QFT, the first law of entanglement with Bisognano–Wichmann flow makes the deep sector's slope equal to the KMS β at first order around the vacuum. That is the pattern of reading C (recalled from memory).
- This lives on the ħ / τ_K side, which is H-spectrum's (GR:60, :144). Transferring it to the classical count needs the naive H-energy map, which is a no-go by GR:84. Classically, Gibbs states exist for every β and T_Unruh → 0.
- **Verdict: does not establish W1.** BORDERLINE as structural support for keeping reading C as the alternative; it is not evidence for OI.

**C5. Unruh/Hawking universality.**
- This is τ_K-side only, under H-Hawking (GR:649), and it uses ħ. By N1 it is silent on the count.
- **Verdict: does not establish W1.** CONFIRMING.

**C6. Decoupling of deep sectors.**

*(a) Gap: a distinct open sufficient premise (F8).*
- *Derived here.* With dilute deep excitations of granularity Δ on N_eff sites, r = −N_eff(βΔ)e^{−βΔ}/(2s_B). So W1 holds iff βΔ − ln βΔ ≳ ln(N_eff/2s_B).
- For N_eff ≈ 3.2×10¹⁸² and 2s_B ≈ 4.5×10¹²² the threshold is βΔ ≳ 1.4×10², i.e. Δ ≳ 5×10⁻⁵¹ J (calibrated, orientation only).
- This is a physically distinct sufficient condition. The deep sector's thermally accessible low-lying configurations must be *collective*: N_eff ≪ 2s_B ≈ 4.5×10¹²² (with no gap, r ~ −N_eff/(2s_B)), far fewer than one per cell; of order one per Hubble volume is an example. Per-cell gaps are excluded by translation invariance if the visible sector's classical energy steps reach k_BT_cl, which is this unit's inference (pressure-test below). It is not a restatement of H-inert.
- *Pressure-test.* H-slope uses the IR expansion in ΔE about 0 (GR:74). My inference is that accessible visible classical energy differences must reach k_BT_cl; GR:66's text states only a positive probe gap over a finite window. Translation invariance (A4; ledger item (xi)) gives D the same granularity.
- GR:84 refutes the *naive H-energy* route to quantum freeze-out. It does **not** refute a classical gap in the finite-alphabet configuration energies.
- *Status:* undetermined for the finite substratum (which lacks a real conserved energy, N0). Negative in the real lift, immediately so: the lift's energies are continuous, so there is no gap (see (a′)).
- *Against the counterexamples:* CE-L survives (it violates H-add). CE-X is excluded only by hypothesis.
- **Verdict:** a conditional sufficient route, open; it is not a derivation. NEW (identifies the decisive input).

*(a′) The real lift (F7; derived here; the review's derivation, checked by hand).*
- Take the real lift of the linear rule with |α| < 1/d, where E is positive definite (SM:292).
- For a positive-definite quadratic form in n = 2N real variables, vol{E ≤ x} ∝ x^N, so Ω(E) ∝ E^{N−1}.
- Hence β = (N−1)/E and C = N−1. That is classical equipartition, with k_B/2 per quadratic degree of freedom and no freeze-out.
- Under reading L, with all of H in this form and the lift's E identified with the first-law energy (W1-0), β_E ≈ N_H/E while β_geo = 2s_B/E = 2σN_B/E. So β_E/β_geo = N_H/(2σN_B).
- With D about one Hubble volume of ε³ cells, this ratio is (4π/3)R³ε⁻³/(8πσR²ε⁻²) = R/(6σε) ≈ 7×10⁵⁹, i.e. r ≈ +7×10⁵⁹. That is CE-X with positive sign: CE-RL.
- Assumptions, each of order one:
  - one lattice site per ε³ (lattice spacing a = ε);
  - one real (u, v) pair per site. With K real components per site (K = 6 under GR:104), N_H is multiplied by K.
  - With K components the ratio is K·R/(6σε), ≈ 4×10⁶⁰ at K = 6; r ≫ 1 is unchanged.
- The positive-definite form stays positive definite when restricted to H's coordinates, so counting H alone is legitimate. V/H additivity, part of W1-0, is assumed despite the u·Av cross terms of E(u,v) = u·u + v·v − u·Av (SM:296).
- At α = 1/d the shells are noncompact (SM:292), so β_E is undefined there.
- Consistency note: GR:695 already invokes the classical equipartition theorem for the harmonic emergent boundary modes.
- A positive r this large is absorbable only by giving up σ ≤ ln q as an entropy per mode (GR:98); see §7.
- **Verdict:** in the corpus's one real-energy model, the gap route fails.

*(b) Causal one-way decoupling.*
- It uses emergent causal structure to bound a substratum count, which is a Step-5 level mismatch.
- The selected update has L ≠ 0 at site-local cuts (GR:128; #1245 c.6818702013), and GR:46 asserts bidirectional coupling.
- Even granted, it leaves W1′ undischarged.
- **Verdict: does not establish W1.** CONFIRMING.

*(c) Exact decoupling (Main:60; Substratum Theorem 24(iii), :257).*
- An energy-decoupled product factor drops out of sector-wise counting, so ħ is unchanged for that class. POSITIVE.
- A factor placed on the joint shell is not a product preparation (GR:86). Under reading L it shifts β_E by −⟨E_D⟩/E (N2, with N2's hypotheses).
- It does not cover the coupled D of GR's chain V↔B↔D.

**C7. Identity of the first-law energy. BORDERLINE.**
- Derived here: E_MS(inside the Hubble sphere) = c⁴R/(2G) (confirmed by review). So GR:58's c⁴R/G is twice an interior quantity.
- Cosmological apparent-horizon thermodynamics pairs horizon entropy with the interior Misner–Sharp energy (recalled from memory).
- ħ is unaffected, because only the differential "energy received by H" enters (GR:70, :74). This is a watch marker only.

## 7. Hard-to-vary assessment (§A.29) (F4)

- **1+r > 0.** A W1 excess r is absorbed by σ_eff = σ(1+r): ħ, ε = 2√σ_eff·l_p and A/4l_p² are unchanged (c.6818970549, re-checked). Only σ's reading as entropy per mode and the boundary-count reading of the 1/4 move. So W1 has no test inside the calibration in this regime.
  - Reading L's r = −⟨E_D⟩/E lies in [−1, 0], so it is absorbable except at its endpoint.
  - A large positive r, as in CE-RL, is absorbable only by abandoning σ ≤ ln q as an entropy per mode (GR:98).
- **r ≤ −1.** GR:186 and :210 do not assert β_E > 0 as a fact. They call the classical layer "settled" *with* β_E > 0, a premise H-count supplies. For r ≤ −1 that premise is removed, and the classical orientation is no longer settled.
- **r = −1.** Here β_E = 0 at E\*, an infinite temperature. A zero slope at one point is compatible with `counting_passive`'s Monotone-Ω hypothesis (ThermalOrientation.lean:256) but does not establish it. The profile is uniform to first order in e_i; its passivity is decided at second order, and for s_H″(E\*) > 0 it is not passive for ε.
- **r < −1.** Here β_E < 0, so the bath count decreases near E\*. That violates `counting_passive`'s Monotone-Ω hypothesis, so the theorem does not apply. For shell-scale ε_a, where the count is decreasing, the same argument applied to the reflected count gives a profile passive for −ε (derived here; not a kernel statement). Such a failure would flip the classical thermodynamic orientation rather than be inert. CE-M lies in this regime for s_cell ≳ 5×10⁻⁶¹σ. c.6818970549's "`counting_passive` … is unaffected" carries the same unstated restriction to 1+r > 0.
- **Independent predictions.** No candidate gives an independent prediction. A hard-to-vary mechanism would need independent fixes of σ and ε (GR:98 and :102 fix neither).
- **Tunability.** H-eq carries a free ρ. H-inert has no free parameter and adds no prediction.

## 8. Conclusion and minimal form

Within OI's present premises, no tested mechanism establishes W1 or a sufficient condition for it. The tested
mechanisms are thermalization/ETH, typicality/max-entropy, holographic bounds, equivalence-principle/Jacobson,
Unruh/Hawking universality, and exact or causal decoupling. Each one either:
- fixes a state rather than the count;
- uses ħ;
- needs a premise that restates W1 or H-inert (or is stronger than it, C3(c)); or
- needs the distinct open sufficient premise of C6(a). That premise is undetermined for the finite substratum and fails in the real lift (C6(a′)).

**W1 is an additional physical assumption, not a derived result.**

**Minimal form (F5).**
- **W1-0** (prerequisite; N0). A real-valued energy, conserved by φ, additive across V/H at the shell scale, and identified with the energy H receives in the horizon first law.
- **W1-min** (on GR:58's counted set). At the shell energy E\*, β_E := ∂ ln Ω_H/∂E over the **whole** hidden shell (GR:58, :70: N_i = |M_i|) equals 8πGσ/(c²κ\*ε²).
  - Reading L: κ\* = κ(E\*), with E\* the total first-law energy.
  - Reading C: κ\* = κ(E_B,realized).
- **W1-min′** (a separate, different condition). The same equality for the realized, dynamically connected sector. It is what one orbit's empirical rate ratio measures. Slopes over the whole shell and over a sector are not ordered by implication. Identifying them is the stationary-law / single-cycle ergodicity hypothesis (SM:292).

**Comparison with H-count (reading L).**
- **⇒ holds.** GR:58's setting (conserved shell; boundary interaction negligible; real energy, which is assumed per GR:695) together with H-count implies W1-0 and W1-min(L). The setting supplies conservation and additivity. H-count supplies the first-law identification, and s_H = σA(E)/ε² + const gives β_E = β_geo(κ(E\*)).
- **⇐ fails.** Witness (derived here): a fixed boundary layer of N_B independent cells (CE-F) with D empty and the cell density of states chosen so that s_B′(E\*) = β_geo(κ(E\*)) at one energy. W1-0 and W1-min(L) hold. But s_H″ < 0, so s_H ≠ σA(E)/ε² + const as a function of E, and H-count's de Sitter form (s_H″ = +β/E) fails. The witness violates H-count **at second order** (s_H″), the order at which GR:58 derives s_H″ = β/E from H-count on the exact de Sitter calibration. Over shell-scale e_i ~ k_BT the mismatch is |s_H″ − k|·e_i²/2 ~ (βe_i)(e_i/E) ~ 1/(2s_H) ≈ 2×10⁻¹²³, the δ_bath order; for |E − E\*| ~ E\* the two entropy functions differ at O(s_H). So the witness separates W1-min from H-count's second-order content (the δ_bath and de Sitter statements), not from its slope content.
- The extra content of H-count (the global law, E = c⁴R/G, s_H″ = β/E, E_D = 0) is consumed by GR:58's de Sitter statements, the δ_bath estimate and §7.3's boundary share. It is not consumed by ħ or the 1/4 (GR:74, :82).
- Under reading C the analogue of H-count is H-eq with W1′, and W1-min(C) follows from it only under N2's hypotheses.

**Assumption-watch W1-add (F5).** GR:86 says H-shell "is therefore not load-bearing". GR:70/:74 still take the
rate-ratio slope from N_i = Ω_H(E−e_i), which uses H-shell's weak-coupling / energy-additivity part (GR:60). At minimum
that additivity clause is load-bearing via GR:70. This is recorded, not resolved.

## 9. Status table

| Item | Status | Support |
|---|---|---|
| The shell is assumed, not supplied by Lemma 3 | Stated in manuscript | GR:58, GR:695 |
| No real positive-definite conserved energy in the exact or rounded finite rule; the real lift has one for \|α\|<1/d | Stated in SM | SM:292, SM:811 |
| ħ condition lists and Main ledger omit the shell / real energy | Finding (ELABORATING) | GR:88, :623, :637, :673; Main:724 |
| H-count not supplied by S1–S4 | Stated in manuscript | GR:58, :88 |
| Only the IR slope is load-bearing for ħ | Manuscript derivation | GR:74, :78–82 |
| Naive H-energy is a no-go | Manuscript proof | GR:84 |
| Exactly decoupled finite deep factor: T_ij unchanged | Proved | Substratum Thm 24(iii) (:257); Main:60 |
| `counting_passive`: monotone Ω ⇒ passive profile | Kernel theorem on `main` (statement read; not rebuilt in this unit) | ThermalOrientation.lean:256 |
| CE-L, CE-X; C_D < 2s_B stability; σ-absorption | Recorded off `main`, internally reviewed; re-verified on paper here | #1245 c.6818970549 |
| N2 lattice identity | Derived here (exact as a lattice identity) | §5 |
| N2 first-order form; reading-L/C equivalences | Derived here; conditional on H-add, W1′(dS) on supp p, common lattice, δβ_B, δβ_D ≪ 1, p(0) ≪ βδ, δVar small (reading-L ⇐ exact under the endpoint condition of §5) | §5 |
| H-add ∧ W1′(dS) jointly realized by local cells | No (CE-F, CE-M) | §5 |
| CE-M r_M ≈ −2×10⁶⁰ s_cell/σ | Derived here (order of magnitude) | §4 |
| CE-F concavity for independent cells | Derived here (Cramér) | §4 |
| CE-RL: real lift gives r ≈ +7×10⁵⁹ (reading L, D ≈ one Hubble volume) | Derived here (review's derivation, hand-checked) | §6 C6(a′) |
| Tangency lemma; constant capacity bound ⇒ slope 0 | Derived here | §6 C3 |
| Gap route threshold βΔ ≳ ln(N_eff/2s_B) | Derived here (dilute limit) | §6 C6(a) |
| Gap route truth for the finite substratum | Open | §6 C6(a) |
| W1-0 ∧ W1-min(L) ⇐ GR:58 setting ∧ H-count; converse fails | Derived here (witness) | §8 |
| r ≤ −1 removes GR:186/:210's β_E > 0 premise; r < −1 violates `counting_passive`'s Monotone-Ω hypothesis | Derived here | §7 |
| W1′; global dominance; substratum → real energy map | Open | §5; GR:12 (G3) |
| W1 | Additional physical assumption (not derived) | §8 |

## 10. Assumption-watch markers and cross-propagation (F10)

- **W1-0** (real conserved energy). Its direct consumers:
  - GR:186, :202, :210 ("classical configuration energies", "derived classical energy ordering", β_E > 0);
  - the kernel theorem `counting_passive` (ThermalOrientation.lean:256: ε : Fin m → ℝ, a monotone Ω : ℝ → ℝ, the additive form Ω(E_tot − ε a));
  - GR:695 (the entropic-force shell);
  - GR §A, Theorems A.8–A.9 (GR:797, :829);
  - SM:1227(ii) and SM:811.
- **1+r > 0 restriction** (F4). This applies to GR:186/:210 and `counting_passive`'s use as "unaffected by W1".
- **W1-add** (GR:86 versus GR:70/:74). Applies wherever H-shell is called non-load-bearing.
- **Count vs state** (N1).
- **Moving partition** (N3, CE-M). Applies to every use of σA(E)/ε² as a function of E, including §7.3's Clausius step (GR:468).
- **Enlargement gauge for ħ only for energy-decoupled factors** (C6(c)). Applies to GR:132–138 and Structure:205/:305 (at `fb733b4a`; :206/:306 on `origin/main` `911a5cb6`) if they are read as covering ħ.
- **First-law energy identity** (C7, BORDERLINE).

## 11. Reading inventory

**Issues.** #1245: body and all 5 comments. #1244: body and all 19 comments.

**Papers** (all via `git show fb733b4a:` for r2–r4, the base named at :5; :356 also cites `origin/main` `911a5cb6`):
- `papers/GR.md`: :1–160, :186, :202, :210, :330–340, :460–480, :575–605, :605–679, :695.
- `papers/Main.md`: :42–64, :74, :84, :443–451, :498–502, :724–736, :742–758.
- `papers/Substratum.md`: :135, :181–191, :251–268.
- `papers/SM.md`: :292, :294, :296, :811.

**Kernel.** `verification/lean-mathlib/OIBridge/ThermalOrientation.lean`: lines 240–275.

**Verification records.** `verification/` was grepped for W1, H-inert, H-eq, W1′, horizon dominance, H-count, deep sector and entropy slope. No record on `main` concerns this W1. The recorded counterexamples exist only in #1245 c.6818970549.

**Reviews.** `w1-1/REVIEW-W1-1.md`, `w1-1/REVIEW-W1-1-r2.md`, `w1-1/DELTA-REVIEW-W1-1-r3.md`.

## 12. Limits and provenance

- These are hand derivations, not machine-checked. r1 was independently reviewed (ACCEPT WITH CHANGES), and r2 was re-checked (ACCEPT WITH NITS). r3 was delta-reviewed (ACCEPT WITH CHANGES) and r4 applies its required edits. An owner checkpoint is required before any use.
- All literature is recalled from memory. No verdict rests on it.
- N2's first-order form, CE-M and the gap estimate carry the hypotheses stated at each.
- The numerical orientation values use the calibrated ħ for scale only.
- The candidate list is not proven exhaustive.
- **Provenance (F11, for the owner checkpoint).**
  - During r1 this session overwrote two pre-existing files, `GR.md` and `Main.md`, in the **shared scratchpad root** (not in `w1-1/`) with `origin/main` copies of the papers. The files were of unknown origin, and their earlier content is unrecoverable.
  - The reviewer checked that both root files now equal `fb733b4a`. This unit's sources (`w1-1/src/`) are byte-identical to `fb733b4a`.
  - This is the situation §A.26 covers. OA-1 (#1169) runs in parallel, and the root holds files from many sessions. Any concurrent unit that relied on root-level `GR.md` or `Main.md` should re-source from `git show`.
  - Recommendation: each unit writes only inside its own subdirectory. r2 was written only inside `w1-1/`.

## 13. r4 change map (`w1-1/DELTA-REVIEW-W1-1-r3.md`, required edits)

Each edit is applied with the review's exact replacement text, including the diff check's D1–D2. Every r4 line number equals its r3 line number.

| Edit | r4 location |
|---|---|
| E1 | :163–164 (§5 N2, first-order validity conditions) |
| E2 | :174 (§5 N2, reading-L ⇐ exception); :40 (r3 nits, N2) |
| E3 | :283–284 (§7, r = −1 and r < −1) |
| E4 | :238 (§6 C6(a), collective deep sector) |
| E5 | :309 (§8, ⇐ witness); :41 (r3 nits, N3) |
| E6 | :254–255 (§6 C6(a′), K factor and E(u,v)) |
| E7 | :331 (§9, N2 first-order row) |
| E8 | :1 (title); :7 (revision line); :363 (inventory); :373 (reviews); :377 (limits) |
| E9 | :356 (§10, Structure citation), by annotation (the narrower of the review's two options); the base line :5 is unchanged |
| E10 | not in this file: `OBJECTS.md` rows are added by the coordinator |
| Diff check D1–D2 | :363 (inventory base); :255 (W1-0 parenthetical) |
