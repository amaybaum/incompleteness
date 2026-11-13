# G3 unit 1 (r1): the emergent energy origin and the covariant gravitational source

**Scope.** Paper-only audit under Issue #873. The planning record is c.6859060590 (`amaybaum`,
2026-11-13T16:40:09Z). The unit authorization is c.6859687612 (`amaybaum`, 2026-11-13T17:07:37Z),
item 1: "Authorize, start now (Recommended)", paper-only. This record proves no theorem in Lean, runs no
computation and changes no manuscript. It adopts no premise.

**Source snapshot.** `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` (2026-11-13). Every
`file:line` below refers to that commit.

**Support labels.** [K] marks a kernel-checked declaration on `main`, whose statement was read here and
not rebuilt. [A] marks exact algebra done by hand here. [P] marks a paper derivation, in the corpus or
here. [L, recalled] marks literature recalled from memory and not re-read for this unit; no verdict
rests on it. "Conjecture" marks an unsupported proposal. **Conditional** means the claim holds only under
the named hypotheses.

**Convention.** The countermodel uses signature (−,+,+,+), units c = 1, and G_μν + Λ g_μν = 8πG T_μν. In
this signature a uniform vacuum energy density ρ has stress tensor −ρ g_μν. The corpus states no
signature, and nothing below depends on the choice beyond the sign of ρ.

***

## 0. Verdict

**Counterexample, scoped as follows.**

OI's existing results do not imply that a uniform additive shift Ω ↦ Ω + C·1 of the emergent
Hamiltonian leaves the covariant gravitational source unchanged. Those results are:

- the substratum, the partition and the reduced transition law;
- the fixed-basis representation and the action-scale calibration;
- every further datum the corpus derives from the emergent generator: channels and circuit data, Gibbs,
  KMS and passive states, the operational transition identification, and counting passivity.

Two covariant, conserved completions (§3) share all of these data at a reference representative. They
differ only in how the source responds to the shift [A, within the admissibility class of §2].

Offset decoupling follows only conditionally, on an added assumption that OI does not supply. Three
such assumptions are:

- the geometry-first source (posited at GR:340 and GR:352);
- a shift-equivariant trace sector of the G3 equation (§5, route R2);
- a principle that fixes the origin.

Under the geometry-first source the question moves rather than closes. The classical energy origin
then carries it. The corpus fixes that origin by convention (GR:58) and takes the value of the
classical vacuum energy as an input (GR:334, GR:356).

This record makes no claim about the magnitude of Λ.

***

## 1. Inventory

### 1.1 Kernel-checked declarations on `main` [K]

Lean tree: `verification/lean-mathlib/OIBridge/`, every module below imported by `OIBridge.lean`
(imports at :86, :93, :95, :96, :97 and :284). Each statement was read; none was rebuilt.

| # | Declaration (file:line) | Statement | Hypotheses | Bearing on the origin |
|---|---|---|---|---|
| K1 | `BohrFrequency.shift_modsq` (BohrFrequency.lean:235) | For `V : n → Fin m → ℂ`, `E : Fin m → ℝ`, `E₀ t : ℝ`, `i j : n`: `Umat V (fun a => E a + E₀) t i j * star (Umat V (fun a => E a + E₀) t i j) = Umat V E t i j * star (Umat V E t i j)`, where `Umat V E t i j = Σ_a V i a · e^{−i E_a t} · conj(V j a)` (:201). | None: `V` need not be unitary, and the spectrum may be degenerate. | Every transition probability is invariant under a common shift. |
| K2 | `BohrFrequency.normSq_expansion` (:215) | `|U_ij(t)|² = Σ_{(a,b)} (V_ia V̄_ja V̄_ib V_jb) e^{i(E_b − E_a)t}`. | None. | `|U_ij|²` depends on `E` only through the gaps `E_b − E_a`. |
| K3 | `BohrFrequency.gaps_determined` (:146); wrapper `bohr_frequency_completeness` (:291) | If the return probabilities are equal at every `t`, then `gaps E = gaps E'`. | `∀ a, 0 < p a` and `∀ a, 0 < p' a`. | The gaps are determined. The origin is not. |
| K4 | `BohrFrequency.reflect_conj` (:265), `reflect_modsq` (:279) | `(V̄, −E)` conjugates `U(t)` entrywise, and preserves every `|U_ij|²`. | None. | Context only: this is the antiunitary branch, not the origin. |
| K5 | `AntiunitaryInvariance.phase_families_shift` (AntiunitaryInvariance.lean:244) | If `∀ t, ∃ c : ℂ, ∀ a, e^{−iE_a t} = c · e^{−iE'_a t}`, then `E a − E' a = E b − E' b` for all `a, b`. | None. | A common scalar factor forces a common shift. |
| K6 | `AntiunitaryInvariance.phase_families_shift'` (:285) | Under K5's hypothesis, `∃ E₀ : ℝ, ∀ a, E a = E' a + E₀`. | `0 < m`. | Converse direction: exact phase-family equality up to scalars leaves exactly one origin. |
| K7 | `AntiunitaryInvariance.ad_eq_scalar` (:201) | If `U X U† = W X W†` for every `X`, then `∃ c, c c̄ = 1 ∧ U = c • W`. | `Nonempty n`, `U U† = 1` and `W W† = 1`. | Exact channel equality leaves a unimodular scalar, hence by K6 an origin. Used in GR Corollary A.3 (GR:745). |
| K8 | `CongruentReconstruction.reconstruction_translation_of_moduli` (CongruentReconstruction.lean:251) | Aligned spectra `E'(τa) = E a + E₀` and equal coefficient lines give `W diag(E') W† = D V diag(E) V† D† + E₀·1`. | `0 < m`, `V V† = 1`, nonzero overlaps, equal moduli, coefficient-line equality. | Reconstruction carries `+E₀·1` as a free parameter. |
| K9 | `PairIdentification.twoBranch_of_triangleGeneric` (PairIdentification.lean:296); `twoBranch_of_BGSignedClassification` (:446) | Equal transition probabilities give `H' = D H D† + E₀` or `H' = −D H̄ D† + E₀`. | `3 ≤ m`, `V V† = 1`, nonzero overlaps, distinct gaps, and (G4) for `E'` (:296) or the premise `BGSignedClassification` (:446). | `E₀` is free in both branches. |
| K10 | `ThermalOrientation.gibbs` (ThermalOrientation.lean:66, def); `gibbs_reflection` (:76) | `gibbs β E a = e^{−βE_a}/Σ_c e^{−βE_c}`, and `gibbs (−β) (−E + E₀) = gibbs β E`. | None. | `E₀` cancels in the normalization. The pure-shift form `gibbs β (E + E₀) = gibbs β E` is not stated as a separate declaration; it follows by the same cancellation [A]. |
| K11 | `ThermalOrientation.Passive` (:195), `StrictlyPassive` (:192) (defs); `passivity_selector_nonuniform` (:239) | Passivity: `E a < E b → p b ≤ p a`. Under distinct energies, one passive non-uniform profile excludes `−E + E₀`. | `∀ a b, a ≠ b → E a ≠ E b`, `Passive E p` and `p a ≠ p b`. | Passivity depends only on the order of the energies, so `Passive (E + c) p ↔ Passive E p` [A]. It selects orientation, not origin. |
| K12 | `ThermalOrientation.OperationalTransitionIdentification` (:318, def: a named premise, never assumed); `energyOrder_transport` (:336); `reflection_excluded_of_transition_identification` (:356) | OTI: `∀ a b, exp(−β_E(ε_b − ε_a)) = exp(−τ_K(ω_b − ω_a))`. Under OTI, the classical order of the `ε` equals the order of the `ω`. | `0 < β_E`, `0 < τ_K` and OTI. | OTI involves only differences, so it is invariant under independent shifts `ε ↦ ε + c` and `ω ↦ ω + c'` [A]. The classical-to-spectral link fixes no origin. |
| K13 | `ThermalOrientation.counting_passive` (:256) | For monotone `Ω`, the profile `a ↦ Ω(E_tot − ε a)/Z` is passive for `ε`. | `Monotone Ω` and `0 < Z`. | The classical energies `ε : Fin m → ℝ` are a parameter, not derived. The shift `(ε, E_tot) ↦ (ε + c, E_tot + c)` leaves the profile unchanged [A]. |
| K14 | `ThermalOrientation.stationary_offdiag` (:403), `stationary_spectral_form` (:472) | A state stationary under `Umat V E t` at every `t`, with injective `E`, is diagonal in the energy eigenbasis. | `V V† = 1` and `Function.Injective E`. | The hypothesis depends on `E` only through the conjugation, which is invariant under the shift. |
| K15 | `ShellAssignment.shellWeight_invariant` (ShellAssignment.lean:69), `marginal_stationary` (:104) | The uniform weight on a `φ`-invariant `shell : Finset (V × H)` is `φ`-invariant, and so is its visible marginal. | `shell` is `φ`-invariant. | The shell is an invariant set with no energy function. The kernel carries no real energy. |

**Docstring mismatch (minor).** The header of `BohrFrequency.lean` at line 7 names "`shift_normSq`". The
declaration is `shift_modsq` (:235). No Lean change is authorized in this unit.

### 1.2 Paper statements, classified

| # | Statement | Location | Class |
|---|---|---|---|
| P1 | Transition data invariant under `H ↦ H + E₀`; Hamiltonian fixed up to overall energy shift (phase-locking lemma) | Main:228, Main:242 (kernel citation `twoBranch_of_triangleGeneric`) | paper, kernel-backed (K9) |
| P2 | Energy origin a global phase; dimensional obstruction | GR:172, GR:292 | paper, kernel-backed (K1) |
| P3 | Cross-interval data fix relative gauge up to one global phase, `e^{iθ(t)}` in the continuum | GR:292 | paper |
| P4 | Exact unitary channel equality forces `Ĥ^dir = Ĥ^seq + E₀` (Corollary A.3) | GR:745–747 | paper, kernel-backed (K6, K7) |
| P5 | Classical microreversibility gives `E_n = ħω_n + E_0` on a connected accessible sector (under H-balance) | GR:70 | paper; `E_0` free |
| P6 | H-slope uses `ΔE = E(ω)`, `E(0) = 0`: slope only | GR:74 | paper |
| P7 | H-energy, modular form: static and dynamical generators agree "up to one universal action scale and an additive constant" | GR:86 | paper; additive constant free |
| P8 | Gap equation `ħ = τ_K/β_E`, κ cancels | GR:78; Corollary A.4 GR:751 | paper (not in Lean) |
| P9 | H-count: `s_H = σA/ε²` up to a constant; "the deep hidden sector contributing … by the choice of energy zero, no energy"; exact de Sitter `E = c⁴R/G` | GR:58 | assumption (named condition) plus convention |
| P10 | `ρ_s = E_s/V_H` with `E_s = S_dS k_B T_cl`, equal to `ρ_crit` | GR:422–426 | paper; absolute energy assignment (see §6 F5) |
| P11 | Geometry-first: "The stress-energy sourcing gravity is the classical stress-energy of the total microstate" | GR:340 | posit (called "the geometry-first proposal" at GR:352) |
| P12 | Ordering requirements (i)–(iii) fix the metric at the partition boundary; three completions remain for laboratory sources | GR:344–348, GR:350 | paper |
| P13 | Two completions `𝒢 = 8πG T^cl` and `𝒢 = 8πG(T^cl − ρ_C g)` share substratum, partition, reduced law, fixed-basis representation and calibration; decoupling is a coupling theorem, open at G3 | GR:352 | paper (asserted; checked in §3) |
| P14 | Zero-point sum not in `H_tot`; relative differences gravitate, absolute levels do not, on the geometry-first proposal and conditional on the coupling step | GR:358; GR:573–579 | conditional proposal |
| P15 | Closure theorem and Lovelock leave `G` and `Λ` undetermined; their hypotheses are not established | GR:162 | paper citing literature |
| P16 | G3 target `E_μν[g, OI] = 8πG(T_μν − ℱ[g,T] g_μν)`; ladder G1–G4; field equations, stress-energy coupling, Bianchi structure and continuum limit "the named G3 opens" | GR:12 | open target |
| P17 | Jacobson with lattice corrections gives `G_μν + Λ g_μν = (8πG/c⁴) T_μν [1 + O(ε²κ²/c⁴)]`, conditional on the source coupling of GR §6.2, open at G3 | SM:160–162 | conditional |
| P18 | Discrete Einstein target `κ_OR = α 𝒯_ij`, curvature step open | SM:144–148 | open target |
| P19 | Type II running vacuum: matter conserved, Bianchi carried by running `G`; functional form not derived | GR:374 | structural reading, not derived |
| P20 | `Q = M_B c²` delivered as boundary heat: "the same coupling map G3 names as open" | GR:466 | assumption |
| P21 | `ρ_QFT/ρ_classical ∼ S_dS`: a dimensional identity; the vacuum-energy value is an input | GR:362; GR:334, GR:356 | paper; no Λ derivation |
| P22 | The descriptive distinction is established; dissolution is conditional; related approaches are trace-free equations [EvEMU11], sequestering [KP14] and Volovik | Introduction:159–161 | paper |
| P23 | No real positive-definite conserved energy in the exact or rounded finite rule; real lift has one for `|α| < 1/d` | SM:292; candidate SM:811 | paper |
| P24 | W1-0: real-valued energy, conserved by φ, additive across V/H at the shell scale, identified with the first-law energy; "an additional physical assumption, not a derived result" (for W1) | verification/programmes/physical-realization/w1-1-20261112/W1-1-REPORT-r4.md:140, :297–301, :346–351 | assumption (accepted record; STATUS.md in the same directory) |
| P25 | G3 map OPEN; emergent rest energy and heat must reach the boundary covariantly | verification/ROADMAP.md:85, :1194–1198 (frozen record; the Issue cites L75 and L1184–L1190 at `9613b21c`) | open |
| P26 | Geometry-first: three laboratory completions; required output is a selecting derivation or a proof that the premises do not select (H-GRAV) | verification/ROADMAP.md:1214–1219 | open |

### 1.3 Absent from the Lean trees (searched)

The searches covered `verification/lean/` (6 files) and `verification/lean-mathlib/` (240 files). The
search patterns are listed in NOTES-r1.md §2. No declaration was found for any of the following:

- a metric, Einstein tensor, stress-energy tensor, Bianchi identity or cosmological constant;
- the horizon first law, the Clausius relation, Jacobson's argument, Unruh or KMS temperature, or an
  area law;
- a real conserved energy on the substratum;
- the gap equation `ħ = τ_K/β_E`.

The only appearance of `Λ` (`OI_Regulator_Symmetry.lean`) is the exterior power `Λ²ℝ⁴`. The classical
energies enter the kernel only as parameters (`ε` in K12 and K13). Classification: **missing**. On
paper the same items are assumptions or open targets (P9, P11, P16–P18, P24).

***

## 2. Target proposition

**Objects.**

- Fix `m ≥ 1`. An emergent representative is `r = (V, E, ρ)`. Here `V ∈ U(m)`, `E ∈ ℝ^m` is a spectrum
  in frequency units, and `ρ` is a density matrix on `ℂ^m`. Write `Ω_r = V diag(E) V†` and
  `U_r(t) = e^{−itΩ_r}`.
- The common shift is `σ_C(V, E, ρ) = (V, E + C·𝟙, ρ)` for `C ∈ ℝ`. Then `Ω_{σ_C r} = Ω_r + C·1`.
- Classical data `κ ∈ 𝒦` collect the substratum `(S, φ)`, the partition, the hidden prior and whatever
  classical energy–momentum assignment is supplied. Classical data are **held fixed** under `σ_C`.
- `Lor(M)` is the set of Lorentzian metrics on a 4-manifold `M`, and `Sym²(M)` the symmetric covariant
  2-tensor fields. The fixed calibration is `a_* = ħ` (GR:78).
- A **gravitational completion** is a pair `𝔊 = (𝒮, Λ)`, with source map `𝒮 : 𝒦 × R_m × Lor(M) → Sym²(M)`
  and field equation `G[g] + Λ g = 8πG 𝒮(κ, r, g)`.
- **Admissibility**, stated without reference to the offset, has three parts.
  - (Adm1) Naturality under diffeomorphisms of `M`.
  - (Adm2) Conservation: `∇^μ 𝒮_μν = 0` on solutions, as the contracted Bianchi identity requires.
  - (Adm3) Calibration: the source converts frequency to energy with `a_*`.

**The two statements to be separated.**

- **(TL) Transition-law invariance.** For every `C`, `|U_{σ_C r}(t)_{ij}|² = |U_r(t)_{ij}|²` and
  `Ad_{U_{σ_C r}(t)} = Ad_{U_r(t)}`.
  - The probability clause is K1 [K].
  - The channel clause holds because `U_{σ_C r}(t) = e^{−iCt}U_r(t)` and the scalar cancels in `Ad` [A].
  - Converse: K7 followed by K6 shows that exact channel equality leaves only such a shift [K].
- **(SI) Source invariance of a completion 𝔊.** For every `κ, r, g, C`,
  `𝒮(κ, σ_C r, g) = 𝒮(κ, r, g)`.

**Question.** Does (TL), together with (Adm1)–(Adm3), entail (SI) for every admissible completion?

(TL) holds unconditionally. So (SI) ⇒ (TL) holds trivially, and only the direction (TL) ⇒ (SI) has
content (§A.34).

**What is not done.** The representative `r` stays an argument of `𝒮`. Restricting the domain of `𝒮` to
`σ`-orbits, or to the operational data `Op(r) = (|U_r|², Ad_{U_r}, ρ)`, would make (SI) hold by
construction: it would state decoupling as a factorization. The proposition leaves that restriction
out and asks whether it follows.

**Lean-style sketch (not built).** Mathlib carries no Lorentzian Einstein tensor [L, recalled], so the
sketch abstracts spacetime and source.

```lean
-- sketch only; not compiled
structure Rep (m : ℕ) where
  V : Matrix (Fin m) (Fin m) ℂ
  unitary : V * Vᴴ = 1
  E : Fin m → ℝ
  ρ : Matrix (Fin m) (Fin m) ℂ
  trace_one : Matrix.trace ρ = 1

def Rep.shift (C : ℝ) (r : Rep m) : Rep m := { r with E := fun a => r.E a + C }

-- (TL), probability clause: this is BohrFrequency.shift_modsq (K1), with n := Fin m
example (r : Rep m) (C t : ℝ) (i j : Fin m) :
    BohrFrequency.Umat r.V (r.shift C).E t i j * star (BohrFrequency.Umat r.V (r.shift C).E t i j)
      = BohrFrequency.Umat r.V r.E t i j * star (BohrFrequency.Umat r.V r.E t i j) :=
  BohrFrequency.shift_modsq r.V r.E C t i j

-- abstract completions: K classical data, Geo metrics, Src symmetric 2-tensor fields
variable (K Geo Src : Type*) [AddCommGroup Src] [Module ℝ Src]

structure Completion (m : ℕ) where
  src : K → Rep m → Geo → Src
  Λ : ℝ

def SourceShiftInvariant (𝔊 : Completion K Geo Src m) : Prop :=
  ∀ κ r g C, 𝔊.src κ (r.shift C) g = 𝔊.src κ r g
```

(Adm1) and (Adm2) are not expressible at this abstraction. A concrete model would carry them as
hypotheses on a differential-geometric `Src`.

**Variant to keep distinct (offset provenance).** In (SI), `σ_C` relabels the representative at fixed
`κ`. A uniform offset can also be the visible image of a change in classical data. In Main's
frozen-bath setting (Main:340), the bath-averaged generator is
`Ĥ_eff = H_V + Tr_H[V_int(1⊗ρ_H)]`. Take `V_int ∋ 1_V ⊗ B`. Then a change `ρ_H → ρ'_H` shifts `Ĥ_eff`
by `tr(B(ρ'_H − ρ_H))·1_V`.

- The channel generator `−i[Ĥ_eff, ·]` does not see this shift [A].
- In the frozen-bath mixture over bath-conditioned unitaries `e^{−i(H_V + ⟨h|V_int|h⟩)t}`, the
  `h`-dependent scalar parts drop out of each term `U_h ρ U_h†`. The mixture does not see them either [A].

Both kinds of offset are invisible to (TL). A source of the geometry-first kind (P11) responds to the
second kind, because `H_tot` changes, and not to the first. (SI) is therefore stated at fixed `κ`.

***

## 3. Countermodel check (GR §6.2)

### 3.1 Construction

Take the following data:

- any `κ`, with a conserved classical stress tensor `T^cl` on `(M, g)`. The corpus supplies no map from
  `(S, φ)` to `T^cl` (P23, P24), so here it is external data, held fixed;
- a reference representative `r₀`;
- constants `G`, `ħ`, `Λ₀`, and a volume `v > 0` that normalizes the emergent offset to a density;
- `e(r) := tr(ρ Ω_r)` and `ρ(r) := ħ e(r)/v`.

Then `e(σ_C r) = e(r) + C · tr ρ = e(r) + C` [A].

The two completions:

- **K_dec:** `G[g] + Λ₀ g = 8πG T^cl`.
- **K_cpl:** `G[g] + Λ₁ g = 8πG (T^cl − ρ(r) g)`, with `Λ₁ := Λ₀ − 8πG ρ(r₀)`.

`Λ₁` is a constant of the completion. P15 records that covariance and the closure or Lovelock routes
leave the constant undetermined.

**Equality at `r₀` [A].** Rewrite K_cpl at `r₀` as
`G + Λ₀ g − 8πG ρ(r₀) g = 8πG T^cl − 8πG ρ(r₀) g`. This is K_dec. The two field equations are the same
equation for `g`, so with the same initial data they have the same solution.

**Admissibility [A].**

- Both completions are natural, because `g_μν` and the scalar `ρ(r)` are.
- Both are conserved when `∇^μ T^cl_μν = 0`, because `∇g = 0` and `ρ(r)` is constant on `M`.
- Both use `a_* = ħ`.

**Response to the shift [A].**

- Under `r₀ ↦ σ_C r₀`, K_dec does not change.
- K_cpl becomes `G + Λ₀ g = 8πG(T^cl − (ħC/v) g)`. Its effective cosmological term moves by
  `ΔΛ_eff = 8πG ħ C / v`.
- So K_dec satisfies (SI), and K_cpl violates it whenever `C ≠ 0`, `ħ/v ≠ 0` and `g ≠ 0`.

### 3.2 Data shared at `r₀`

| Datum | Shared? | Reason |
|---|---|---|
| Substratum `(S, φ)` | yes | Neither completion constrains `(S, φ)`, and no map from `(S, φ)` to a source is on `main` (P23, P24; GR:695 "The shell is assumed"). GR:340 counts the metric as substratum data, and the metric is the same. [P] |
| Partition | yes | The partition is fixed by the causal structure of `g` (GR:40, GR:346). Same `g` gives the same horizon, the same `A` and the same mode count `A/ε²`. [A] |
| Reduced transition law | yes | It depends on substratum, partition and prior. `σ_C r₀` gives the same law (K1). [K] |
| Fixed-basis representation | yes | `r₀` and `σ_C r₀` lie in one class (K6, K9). [K] |
| Action-scale calibration `ħ = τ_K/β_E` | yes | κ cancels (GR:78, GR:751). The first-law flux `δQ = ∫T_μν ξ^μ dΣ^ν` with null `k` sees no term `ρ g_μν k^μ k^ν = 0`, so both completions supply the same prefactor `dE = c²κ dA/(8πG)`. [A] plus [P] |
| Channels and circuit data | yes | The scalar cancels in `Ad` (§2, (TL)). [A] |
| Gibbs and KMS state, passivity, OTI, counting profile, stationarity | yes | These are invariant under the shift: K10 to K14. [A] and [K] |

**What differs.** Only the response `∂Λ_eff/∂C`: zero for K_dec and `8πGħ/v` for K_cpl.

**What follows.** The countermodel exists. The transition-law results alone leave the offset coupling
undetermined. So do all the further data the corpus derives from the emergent generator. This is a
contrast with the antiunitary branch, which oriented thermal structure excludes (K11, K12). The
corresponding structures are shift-invariant, so they do not fix the origin.

### 3.3 Precision on GR:352 as written

GR:352 writes the pair as `𝒢 = 8πG T^cl` and `𝒢 = 8πG(T^cl − ρ_C g)`, with one `T^cl`. Read with the
same constant term in both, the two de Sitter solutions differ for `ρ_C ≠ 0`, since `H²` moves by
`8πGρ_C/3`. Then `A = 4πc²/H²`, the boundary mode count and the partition differ [A].

The pair therefore shares the partition only in one of three cases:

- `𝒢` includes a free constant, adjusted as in §3.1;
- `T^cl` is relabelled between the two completions (`T^cl_2 = T^cl_1 + ρ_C g`), which the corpus
  permits because it supplies no map from the substratum to `T^cl`;
- `ρ_C = 0`.

The substance of GR:352 stands. The statement needs that qualifier. See owner question Q1.

### 3.4 Pressure tests of the branches favourable to decoupling (§A.31)

**B1. "The origin is gauge, so a completion that reads it is unphysical; hence (SI)."**

- Check: the gauge status of the origin is established relative to the operational data: K1, K6 and
  K7, together with the shift-invariance of K10 to K14.
- It is not established relative to gravitational response. Declaring the origin gauge for all
  physics is (SI) restated.
- In standard physics the energy origin is unobservable without gravity and couples once gravity is
  included [L, recalled: Weinberg 1989, cited at Introduction:288].
- K_cpl is consistent once a representative is physically selected, by any structure outside the OI
  data listed.
- **Node verdict: rejected as a derivation.** The branch defines decoupling into the premise.

**B2. "Under the geometry-first source (P11), `r` is not an argument of `𝒮`, so (SI) holds."**

- Check: if `𝒮` depends on `(κ, g)` only, (SI) holds at fixed `κ` [A].
- Three limits apply.
  - (a) P11 is a posit. Its motivating requirements (i)–(iii) fix the metric at the partition boundary
    only. GR:350 admits three completions for laboratory sources, one of them semiclassical.
  - (b) P11 removes `r` from the domain. It entails (SI) as a premise; it does not derive it.
  - (c) The classical origin stays free. Classical evolution is blind to `H_tot ↦ H_tot + b`, since
    `{b, ρ} = 0` in Main:62 and φ conserves every function constant on its cycles (GR:84) [A].
    W1-0's additivity and conservation are preserved by per-subsystem constants, and by a per-cell
    constant `b`. A per-cell constant moves `T^cl` by `−(b/ε³) g`, which K_dec couples [A].
- **Node verdict: (SI) holds conditional on P11.** The origin question moves to the classical energy.
  The corpus fixes that origin by convention: "by the choice of energy zero" (GR:58), and "its value
  is an input" (GR:334, GR:356).

**B3. "Conservation and Bianchi exclude the coupled completion."**

- Check: for constant `C`, both completions are conserved (§3.1).
- For a time-dependent uniform shift `C(t)`, still invisible because `U ↦ e^{−i∫C}U`, K_cpl needs
  `∂_ν ρ = ∇^μ T^cl_μν` [A]. GR:292 records the continuum form `e^{iθ(t)}` of this gauge. That means
  either energy exchange with matter (Type I) or a running `G` (Type II, GR:374).
- **Node verdict: rejected for the constant case.** Conservation constrains only time-varying offsets.

**B4. "Covariance fixes the trace sector."**

- Check: GR:162 records that the closure theorem and Lovelock leave `G` and `Λ` undetermined
  [L, recalled: Lovelock 1971]. A second-order, metric-only, covariant, divergence-free geometric side
  admits `Λ g`.
- **Node verdict: rejected.**

Within this unit, B3 and B4 added no NEW item after B1 and B2. The §A.31 fixed point of three to four
empty passes is not claimed after one pass per branch.

***

## 4. Dependency trace

| Dependency | What it would supply | Supplied by OI? | Where stated | Bearing on the offset |
|---|---|---|---|---|
| G3: covariant field equations with conservation and Bianchi structure and the continuum limit | The equation and its source | No: open | GR:12, GR:352, GR:633, GR:655; ROADMAP.md:85 | Whether `𝒮` satisfies (SI) is a property of the G3 equation. The target form decides it only through `ℱ` (§5, R2). |
| Source choice (geometry-first, hidden-sector average, emergent near field) | Which tensor is `𝒮` | No: posited for the boundary metric, open for laboratory sources | GR:340, GR:350, GR:352; ROADMAP.md:1214–1219; Introduction:161 | Under P11, (SI) holds at fixed `κ` (B2). |
| W1-0: classical real energy and its identification with the first-law energy | `T^cl` from the substratum | No: assumption | W1-1-REPORT-r4.md:140, :301; GR:58, GR:695; SM:292 | Additivity and conservation leave per-cell constants free [A]. The identification with the differential first law fixes no constant. |
| Energy-origin conventions in the classical chain | Absolute classical energies | Conventions | GR:58 ("by the choice of energy zero"; `E = c⁴R/G`); GR:422–426 (`E_s = S_dS k_B T_cl`) | These carry the classical origin under P11 (§6, F5). |
| Emergent–classical intertwiner | Origin transport | Slope only | GR:70 (`E_n = ħω_n + E_0`), GR:74, GR:86 (additive constant) | `E_0` is free. Under `σ_C`, holding classical `E` fixed (`E_0 ↦ E_0 − ħC`) decouples. Holding `E_0` fixed couples. The corpus fixes neither. |
| Conservation and Bianchi | Constancy of the coupled offset | Identity of the geometric side; matter conservation posited (Type II) | GR:374; GR:12 | Constrains time-varying offsets only (B3). |
| Continuum limit and covariance | Lorentzian `(M, g)`, natural `𝒮` | No: open | GR:12; GR:697 item (ii); SM:144–148; SM:160–162 | The countermodel needs only a natural source and `g ≠ 0`. Any linear discrete source map with a metric-like invariant tensor admits the same λ-family [P]. |
| Matter–boundary energy transfer | `Q = M_B c²` to the boundary | No: assumption, "the same coupling map G3 names as open" | GR:466; ROADMAP.md:1194–1198 | `M_B c²` is a difference of energies, so it is invariant under `σ_C` [A]. The MOND chain does not consume the offset coupling. |
| State selection (H-state, H-balance, H-slope) | Thermal state, calibration | No: selection conditions | GR:62–66, GR:74, GR:88 | Shift-invariant (K10, K11) [A]. These conditions fix no origin. |
| Horizon-entropy and `10^122` relation | — | — | GR:362 (dimensional identity); GR:334, GR:356 (value an input) | No dependency. This record draws no Λ prediction from it. |
| C4 at the cosmological cut | Partition-level realization | No: not discharged | GR:52 | Independent of the offset. |

**Physical assumptions OI does not furnish.**

- the G3 equation;
- the source choice;
- W1-0;
- the classical energy origin;
- the transport of the origin `E_0`;
- the continuum limit and covariance;
- the matter–boundary map `Q = M_B c²`;
- the state-selection conditions.

None of them is derived on `main`.

***

## 5. Verdict, routes and next obligation

**Verdict: counterexample.** It is scoped to OI's existing results (§0, §3).

**Routes that would yield (SI).** Each is a proposed route, with its status. None is adopted.

- **R1. Geometry-first source (P11).** It yields (SI) at fixed `κ`. Status: posited (GR:340, GR:352).
  It moves the cosmological-constant freedom into the classical origin (B2).
- **R2. Shift-equivariant trace sector.** In the G3 target form `E_μν[g,OI] = 8πG(T_μν − ℱ[g,T] g_μν)`
  (GR:12), a uniform vacuum term `T ↦ T − ρ g` with constant `ρ` leaves the right side unchanged if and
  only if `ℱ[g, T − ρ g] = ℱ[g, T] − ρ` [A].
  - `ℱ = ¼ g^{μν}T_μν + const` satisfies this. This is the trace-free, or unimodular, sector, and it
    removes every uniform offset, emergent or classical. Λ returns as an integration constant
    through Bianchi and conservation [L, recalled: Ellis, van Elst, Murugan and Uzan 2011, cited at
    Introduction:244; unimodular gravity].
  - `ℱ = const` (Einstein with Λ) does not satisfy it.
  - Status: literature; not derived in OI. The target form as printed does not decide the question.
- **R3. Sequestering.** Global constraints cancel vacuum contributions in the field equations
  [L, recalled: Kaloper and Padilla 2014, cited at Introduction:258]. Status: literature; it requires
  global variables that OI does not supply.
- **R4. Substratum phase (conjecture).** The permutation matrix `P_φ` is a definite unitary with
  determinant `sgn φ`. A choice of logarithm branch would fix a total-system frequency origin, up to
  `2π/Δt · ℤ` and the per-mode branch choices of GR:84.
  - Obstruction: the visible generator is reconstructed from phase-blind data (K7), so the
    total-system phase does not reach it. The branch choice is itself unselected (GR:84).
  - Status: conjecture.

**Smallest next proof obligation (O1).** Decide whether OI's premises force the trace sector of the G3
equation to be shift-equivariant: whether `ℱ[g, T − ρ g] = ℱ[g, T] − ρ` for constant `ρ`. Two outcomes
are possible.

- A proof from independently motivated premises yields (SI) for every uniform offset. Such premises
  could be a substratum-fixed spacetime volume element, which this record leaves open: GR:693 places
  the emergent metric in bond weights, not in cell counts.
- An admissible non-equivariant `ℱ` compatible with every OI premise is a G3-level countermodel.

Prerequisite: W1-0 must fix what `T` is. Until then O1 can be posed only in the form of the λ-family
of §3.

Each route keeps the Λ value an input. This record makes no claim about its magnitude.

***

## 6. Findings

| ID | Finding | Class | Support |
|---|---|---|---|
| F1 | GR:352's non-implication holds. An explicit, covariant and conserved pair shares all listed data and differs in the offset response. | POSITIVE | [A] §3.1–3.2 |
| F2 | GR:352's pair shares the partition only if `𝒢` carries a free constant, if `T^cl` is relabelled, or if `ρ_C = 0`. | ELABORATING | [A] §3.3 |
| F3 | The shared data extend beyond GR:352's list to every structure the corpus derives from the emergent generator. The origin, unlike the orientation, is not fixed by oriented thermal structure. | POSITIVE | [K] K10–K14, [A] |
| F4 | Offset provenance: a uniform shift at fixed classical data and a uniform shift induced by a classical (hidden) energy change are both invisible to (TL). The geometry-first source treats them differently. The absolute/relative rule of GR:573–577 is phrased in the emergent description and does not separate them. | NEW (candidate; for review) | [A] §2, from Main:340 |
| F5 | Under P11, the classical origin carries the question. GR:58 fixes it by choice (`E_D = 0`; `E = c⁴R/G`, the first law integrated with zero constant). GR:422–426 uses `E_s = S_dS k_B T_cl = c⁴R/(2G)`, while `∫_0^R T_cl dS = c⁴R/G = 2E_s` [A]. These are two absolute assignments to one horizon, and neither follows from the differential first law. | ELABORATING (assumption-watch AW-abs) | [A] |
| F6 | The G3 target form decides offset coupling only through the shift-equivariance of `ℱ`. | ELABORATING | [A] §5 R2 |
| F7 | The header of BohrFrequency.lean:7 names `shift_normSq`; the declaration is `shift_modsq` (:235). | minor | read |

**Algebra for F5.**

- `S_dS = σA/ε²`, with `A = 4πc²/H²` and `T_cl = c³ε²H/(8πG k_B σ)` (GR:422).
- `S_dS k_B T_cl = c⁵/(2GH) = c⁴R/(2G)`, with `R = c/H`.
- `k_B T_cl dS_dS = (c³ε²H/(8πGσ))(σ/ε²) 8πR dR = c⁴ dR/G`, so the integral from `R = 0` is `c⁴R/G`
  (GR:58).
- The factor 2 is the Euler relation `E ∂S/∂E = 2S` for `S ∝ E²`.

F5 records the assignments only. It makes no claim about which assignment, if either, is the
gravitating energy, and none about magnitude.

**Assumption-watch markers.**

- **AW-prov (F4).** Applies to every use of "invisible to transition data" as a criterion of
  gravitational inertness: GR:352, GR:577, Introduction:159.
- **AW-abs (F5).** Applies to GR:58's de Sitter statements, GR:422–426, and the §7.3 boundary share
  (GR:466 onward).

***

## 7. Literature

These inputs are recalled and were not re-read. No verdict rests on them.

- S. Weinberg, Rev. Mod. Phys. 61, 1 (1989): a vacuum energy enters as `−ρ g_μν` and cannot be
  distinguished from a bare Λ.
- D. Lovelock, J. Math. Phys. 12, 498 (1971), cited at GR:162: uniqueness of `a G_μν + b g_μν` in four
  dimensions.
- T. Jacobson, Phys. Rev. Lett. 75, 1260 (1995): the Clausius route gives the Einstein equations, with
  Λ as an undetermined constant.
- G. F. R. Ellis et al., Class. Quantum Grav. 28, 225007 (2011), cited at Introduction:244: trace-free
  equations.
- N. Kaloper and A. Padilla, Phys. Rev. Lett. 112, 091304 (2014), cited at Introduction:258:
  sequestering.
- R. M. Wald, axioms for the renormalized stress tensor: the residual ambiguity includes a term
  proportional to `g_μν`.
