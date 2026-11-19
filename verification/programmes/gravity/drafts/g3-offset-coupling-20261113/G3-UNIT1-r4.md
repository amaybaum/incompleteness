# G3 unit 1 (r4): the emergent energy origin and the covariant gravitational source

**Scope.** This is a paper-only audit under Issue #873.

- Planning record: c.6859060590 (`amaybaum`, 2026-11-13T16:40:09Z).
- Unit authorization: c.6859687612 (`amaybaum`, 2026-11-13T17:07:37Z), item 1: "Authorize, start now
  (Recommended)", paper-only.
- Reviews on branch `research/g3-offset-873-20261113`:
  - `REVIEW-r1.md` (REVISE, of r1 at `e64b9a3c`), at `5fe230cd`;
  - `REVIEW-r2.md` (REVISE, of r2 at `1aaf87a2`), at `25257ae5`;
  - `CONFIRM-r3.md` (NOT CONFIRMED, delta check of r3 at `b207fbaa`), at `95681321`.
- Dispositions are in `RESPONSE-r1.md`, `RESPONSE-r2.md` and `RESPONSE-r3.md`.

This record does not prove a theorem in Lean, does not run a computation, does not change a
manuscript and does not adopt a premise.

**Source snapshot.** `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153` (2026-11-13). Every
`file:line` below refers to that commit.

**Support labels.** Every claim carries one of these labels.

- [K]: a kernel-checked declaration on `main`. Its statement was read here and was not rebuilt.
- [A]: exact algebra, done by hand here.
- [P]: a paper derivation, either in the corpus or here.
- [L, recalled]: literature recalled from memory and not re-read for this unit. No verdict rests on it.
- "Conjecture": an unsupported proposal.

A claim marked **conditional** holds only under the hypotheses it names.

**Convention.** Signature (−,+,+,+), units c = 1, and G_μν + Λ g_μν = 8πG T_μν. In this signature a
uniform vacuum energy density ρ has stress tensor −ρ g_μν. The corpus does not state a signature, and
nothing below depends on the choice except the sign of ρ.

***

## 0. Verdict

**Two-part verdict.** Both parts rest on node B5 (§3.4). They use two targets defined in §2: (SI),
invariance of the source when the representative's origin is relabelled, and (DZ), decoupling of a
convention-fixed zero-point offset.

1. **Counterexample, for source maps.** (SI) is not implied on the weak and loop readings of
   requirement (ii) ((ii-W), (ii-L)). Under the strong reading (ii-S), which corresponds for the source
   to GR:400 Reading 2, (SI) follows conditionally.
   - The witness is K_cpl^free (§3.1). It is world-equivalent to K_dec with Λ₀ left undetermined (the union over Λ₀), the corpus's standing for Λ (GR:162, GR:334, GR:356) [A].
   - This part carries no fine-tuning content.
2. **Conditional on (ii-L), for the coupling with physical content.** K_cpl^conv, the coupled
   completion with physical content, violates (DZ) [A].
   - It is excluded by (ii-S) and by GR:346 as argued (ii-L).
   - It is not admitted by the corpus's use. That use feeds back only a piece that GR:400 classes as
     relative in the sense of §8.3 (GR:573), conditional on that identification.
   - K_cpl^conv is compatible with OI's results only under (ii-W) applied to absolute emergent
     quantities, a reading no corpus text adopts.
   - (DZ) for the convention-fixed offset therefore follows conditional on GR:346's argument (ii-L)
     [P]. Whether that argument holds against self-consistent fixed points is not established: it is a
     requirement on the order of derivation, not a proof that no fixed point exists.

**OI's existing results** here are:

- the substratum, the partition and the reduced transition law;
- the fixed-basis representation and the action-scale calibration;
- the ordering requirements (i)–(iii), examined in B5;
- every datum the corpus derives from the operational content of the emergent generator: transition
  probabilities, channels, gaps, and the thermal, passivity and stationarity structures K10–K14.

At a reference representative, each coupled completion shares all of these data with K_dec and gives
the identical world ([A], within the admissibility class of §2). The exception is requirement (ii),
whose bearing on each completion B5 sets out.

**Assumption-watch AW-loop.** GR:346 and the wording "emergent vacuum energy" at GR:358, GR:374 and
GR:400 are in apparent tension. GR:400's qualifier reconciles them, conditional on §8.3's
identification (B5). The reconciliation is not stated at GR:346. This unit proposes no manuscript
change.

**At the level of solutions** (§2, SI′):

- In the divergence-free class with Λ a constant of the completion, K_cpl^free also violates (SI′).
- K_cpl^conv satisfies (SI) and (SI′) and violates (DZ) [A].
- In the trace-free class, which is the structure of the corpus's conditional Jacobson route
  (SM:160–162), any uniform term, `e_Z` included, drops out of the field equations [A]. (SI′) and (DZ)
  then reduce to one question: is the datum that selects the solution a function of the classical data
  alone?

**Other routes.** Decoupling follows from other added assumptions as well, and OI supplies none of
them:

- the geometry-first source (R1);
- an equivariant left-side and trace-sector pair (R2);
- a principle that fixes the origin (R3).

Under R1 the question moves to the classical energy origin. The corpus fixes that origin by
convention (GR:58) and takes the value of the classical vacuum energy as an input (GR:334, GR:356).

This record makes no claim about the magnitude of Λ.

***

## 1. Inventory

### 1.1 Kernel-checked declarations on `main` [K]

The Lean tree is `verification/lean-mathlib/OIBridge/`. Every module below is imported by
`OIBridge.lean`, at :86, :93, :95, :96, :97 and :284. Each statement was read, and none was rebuilt.

| # | Declaration (file:line) | Statement | Hypotheses | Bearing on the origin |
|---|---|---|---|---|
| K1 | `BohrFrequency.shift_modsq` (BohrFrequency.lean:235) | For `V : n → Fin m → ℂ`, `E : Fin m → ℝ`, `E₀ t : ℝ`, `i j : n`: `Umat V (fun a => E a + E₀) t i j * star (Umat V (fun a => E a + E₀) t i j) = Umat V E t i j * star (Umat V E t i j)`, where `Umat V E t i j = Σ_a V i a · e^{−i E_a t} · conj(V j a)` (:201). | None; `V` need not be unitary. | Every transition probability is invariant under a common shift. |
| K2 | `BohrFrequency.normSq_expansion` (:215) | `|U_ij(t)|² = Σ_{(a,b)} (V_ia V̄_ja V̄_ib V_jb) e^{i(E_b − E_a)t}`. | None. | The probabilities depend only on the gaps `E_b − E_a`. |
| K3 | `BohrFrequency.gaps_determined` (:146); its wrapper `bohr_frequency_completeness` (:291) | Equal return probabilities at every `t` give `gaps E = gaps E'`. | `∀ a, 0 < p a` and `∀ a, 0 < p' a`. | The gaps are determined. The origin is not. |
| K4 | `BohrFrequency.reflect_conj` (:265), `reflect_modsq` (:279) | `(V̄, −E)` conjugates `U(t)` entrywise and preserves every `|U_ij|²`. | None. | Context only: the antiunitary branch. |
| K5 | `AntiunitaryInvariance.phase_families_shift` (AntiunitaryInvariance.lean:244) | If `∀ t, ∃ c : ℂ, ∀ a, e^{−iE_a t} = c · e^{−iE'_a t}`, then `E a − E' a = E b − E' b`. | None. | A common scalar factor forces a common shift. |
| K6 | `AntiunitaryInvariance.phase_families_shift'` (:285) | Under the hypothesis of K5, `∃ E₀ : ℝ, ∀ a, E a = E' a + E₀`. | `0 < m`. | Exactly one origin remains. |
| K7 | `AntiunitaryInvariance.ad_eq_scalar` (:201) | `(∀ X, U X U† = W X W†) → ∃ c, c c̄ = 1 ∧ U = c • W`. | `Nonempty n`, `U U† = 1`, `W W† = 1`. | Exact channel equality leaves a unimodular scalar. |
| K8 | `CongruentReconstruction.reconstruction_translation_of_moduli` (CongruentReconstruction.lean:251) | Aligned spectra `E'(τa) = E a + E₀` with equal coefficient lines give `W diag(E') W† = D V diag(E) V† D† + E₀·1`. | `0 < m`; `V V† = 1`; nonzero overlaps; equal moduli; equal coefficient lines. | `E₀` is free. |
| K9 | `PairIdentification.twoBranch_of_triangleGeneric` (PairIdentification.lean:296); `twoBranch_of_BGSignedClassification` (:446) | Equal transition probabilities give `H' = D H D† + E₀` or `H' = −D H̄ D† + E₀`. | `3 ≤ m`, `V V† = 1`, nonzero overlaps and distinct gaps for both. At :296, (G4) for `E'`. At :446, the premise `BGSignedClassification` and `W W† = 1`. | `E₀` is free in both branches. |
| K10 | `ThermalOrientation.gibbs` (ThermalOrientation.lean:66, def); `gibbs_reflection` (:76) | `gibbs β E a = e^{−βE_a}/Σ_c e^{−βE_c}`, and `gibbs (−β) (−E + E₀) = gibbs β E`. | None. | `E₀` cancels in the normalization. The pure-shift form `gibbs β (E + E₀) = gibbs β E` is not a separate declaration; the same cancellation gives it [A]. |
| K11 | `ThermalOrientation.Passive` (:195), `StrictlyPassive` (:192) (defs); `passivity_selector_nonuniform` (:239) | Passive: `E a < E b → p b ≤ p a`. One passive, non-uniform profile with distinct energies excludes `−E + E₀`. | `∀ a b, a ≠ b → E a ≠ E b`; `Passive E p`; `p a ≠ p b`. | `Passive (E + c) p ↔ Passive E p` [A]. The structure selects orientation, not origin. |
| K12 | `ThermalOrientation.OperationalTransitionIdentification` (:318, def; a named premise that is never assumed); `energyOrder_transport` (:336); `reflection_excluded_of_transition_identification` (:356) | OTI: `∀ a b, exp(−β_E(ε_b − ε_a)) = exp(−τ_K(ω_b − ω_a))`. Under OTI, the order of the `ε` is the order of the `ω`. | `0 < β_E`, `0 < τ_K`, and OTI. | OTI involves only differences, so it is invariant under independent shifts of `ε` and of `ω` [A]. |
| K13 | `ThermalOrientation.counting_passive` (:256) | For monotone `Ω`, the profile `a ↦ Ω(E_tot − ε a)/Z` is passive for `ε`. | `Monotone Ω`, `0 < Z`. | `ε` is a parameter. The shift `(ε, E_tot) ↦ (ε + c, E_tot + c)` leaves the profile unchanged [A]. |
| K14 | `ThermalOrientation.stationary_offdiag` (:403), `stationary_spectral_form` (:472) | A state that is stationary at every `t` and has injective `E` is diagonal in the energy eigenbasis. | `V V† = 1`, `Function.Injective E`. | The hypothesis uses `E` only through the conjugation. |
| K15 | `ShellAssignment.shellWeight_invariant` (ShellAssignment.lean:69), `marginal_stationary` (:104) | The uniform weight on a `φ`-invariant `shell : Finset (V × H)`, and its visible marginal, are `φ`-invariant. | `shell` is `φ`-invariant. | The shell carries no energy function. |

**Docstring mismatches (minor).** The header of `BohrFrequency.lean` names "`shift_normSq`" at line 8,
but the declaration is `shift_modsq` (:235). It names "`reflect_normSq`" at line 9, but the declaration
is `reflect_modsq` (:279). This unit authorizes no Lean change.

### 1.2 Paper statements, classified

| # | Statement | Location | Class |
|---|---|---|---|
| P1 | Transition data are invariant under `H ↦ H + E₀`; the Hamiltonian is fixed up to an overall energy shift. | Main:228, Main:242 | paper, backed by K9 |
| P2 | The energy origin is a global phase (the dimensional obstruction). | GR:172, GR:292 | paper, backed by K1 |
| P3 | Cross-interval data fix the relative gauge up to one global phase, which becomes `e^{iθ(t)}` in the continuum. | GR:292 | paper |
| P4 | Exact unitary channel equality forces `Ĥ^dir = Ĥ^seq + E₀` (Corollary A.3). | GR:745–747 | paper. Each step is [K] (K7, K5–K6); their composition is the prose step at GR:747 [P]. |
| P5 | `E_n = ħω_n + E_0` on a connected accessible sector, under H-balance. | GR:70 | paper; `E_0` is free |
| P6 | H-slope: `ΔE = E(ω)` with `E(0) = 0`; only the slope enters. | GR:74 | paper |
| P7 | H-energy, modular form: the two generators agree "up to one universal action scale and an additive constant". | GR:86 | paper; the additive constant is free |
| P8 | Gap equation `ħ = τ_K/β_E`; κ cancels. | GR:78; Corollary A.4 at GR:751 | paper; not in Lean |
| P9 | H-count: `s_H = σA/ε²` up to a constant. The shell energy `E` is "the energy of the horizon first law", and the deep hidden sector contributes, "by the choice of energy zero, no energy". Exact de Sitter gives `E = c⁴R/G`. | GR:58 | assumption (a named condition) together with a convention |
| P10 | `ρ_s = E_s/V_H`, with `E_s := S_dS k_B T_cl` ("the total thermal energy"), equals `ρ_crit`; this is attributed to "Jacobson's Clausius relation". | GR:422–426 | paper; see F5 |
| P11 | Geometry-first source: "The stress-energy sourcing gravity is the classical stress-energy of the total microstate". | GR:340 | a posit ("the geometry-first proposal", GR:352) |
| P12 | The ordering is "forced … through three independent requirements": (i) definiteness, (ii) non-circularity and (iii) uniqueness of ħ. In the book these are "not a stipulation but a structural consequence". | GR:342–348; book/ch07-gravity.md:183, :187 | paper argument, not kernel-checked; examined in B5 |
| P13 | Requirements (i)–(iii) fix the metric at the partition boundary. Three completions remain for laboratory sources. | GR:350 | paper |
| P14 | Two completions share the substratum, partition, reduced law, fixed-basis representation and calibration. Decoupling is a coupling theorem, open at G3. | GR:352 | paper; checked in §3 |
| P15 | "The emergent quantum description does feed back into gravitational dynamics through state-level quantities". The zero-point energy is "the ground-state eigenvalue of Ĥ_eff". | GR:358 | paper |
| P16 | Two readings of the emergent running. Reading 1: the emergent curvature response feeds back as a source, while "the substratum budget fixes the constant part". Reading 2 ("strict geometry-first"): "only partition geometry sources gravity". The corpus does not adjudicate between them. | GR:400 | paper |
| P17 | Relative differences gravitate and absolute levels do not, on the geometry-first proposal and conditional on the coupling step. How the electroweak and QCD transitions couple is not fixed by this rule. | GR:573–579 | conditional proposal |
| P18 | The closure theorem and Lovelock leave `G` and `Λ` undetermined; their hypotheses are not established. | GR:162 | paper citing literature |
| P19 | G3 target `E_μν[g, OI] = 8πG(T_μν − ℱ[g,T] g_μν)`, "under which the distinct-descriptions argument becomes a theorem of the dynamics". G3 covers field equations with conservation/Bianchi structure and the continuum limit. | GR:12 | open target; see AW-G12 |
| P20 | On the Jacobson route, input (iii) is the energy flux `δQ = ∫T_μν k^μ dΣ^ν`. The resulting equation `G_μν + Λ g_μν = (8πG/c⁴)T_μν[1 + O(ε²κ²/c⁴)]` is conditional on the source coupling of GR §6.2 and on further open inputs. | SM:160–162 | conditional |
| P21 | Discrete Einstein target `κ_OR = α 𝒯_ij`; the curvature step is open. | SM:144–148 | open target |
| P22 | Type II: matter is conserved and the Bianchi identity is carried by running `G`. The functional form is not derived. | GR:374 | structural reading |
| P23 | `Q = M_B c²` is delivered to the boundary: "the same coupling map G3 names as open". | GR:466 | assumption |
| P24 | `ρ_QFT/ρ_classical ∼ S_dS` is a dimensional identity, and the vacuum-energy value is an input. | GR:362; GR:334, GR:356 | paper; no Λ derivation |
| P25 | Absolute emergent quantities: `½ħω` per mode with a cutoff, and `ρ_QFT ∼ 10^{113}` J/m³. | GR:332, GR:336 | paper |
| P26 | No real positive-definite conserved energy exists in the exact or the rounded finite rule. | SM:292; the candidate is at SM:811 | paper |
| P27 | W1-0: a real-valued energy, conserved by φ, additive across V/H and identified with the first-law energy. W1 is "an additional physical assumption, not a derived result". | `verification/programmes/physical-realization/w1-1-20261112/W1-1-REPORT-r4.md`:140, :298, :301, :346–351 | assumption |
| P28 | The G3 map is open. | `verification/ROADMAP.md`:85, :1194–1198 | open |
| P29 | Laboratory superpositions (H-GRAV): three completions, with "a derivation that selects one … or a proof that the premises do not select" required. | `verification/ROADMAP.md`:1214–1219 | open |
| P30 | The relative/absolute rule "does not decide a transition between two configurations". | `verification/audits/manuscript/corpus-consistency-20261026/AUDIT.md`:55, :371–378 | audit record |

### 1.3 Absent from the Lean trees (searched)

The search covered `verification/lean/` (6 files) and `verification/lean-mathlib/` (240 files). The
patterns are listed in NOTES-r2.md §2. No declaration was found for any of the following:

- a metric, the Einstein tensor, the stress-energy tensor, the Bianchi identity or a cosmological constant;
- the horizon first law, the Clausius relation, Jacobson's argument, the Unruh or KMS temperature, or an area law;
- a real conserved energy on the substratum;
- the gap equation `ħ = τ_K/β_E`.

The symbol `Λ` occurs in 22 Lean files, and no occurrence denotes a cosmological constant. It appears
as the exterior power `Λ²ℝ⁴` in `OI_Regulator_Symmetry.lean`, and elsewhere as the name of a region or
a matrix (for example `SecondOrderDrive.lean`:59 and :361, `MinimalRepertoire.lean`:21). Classical
energies enter the kernel only as parameters (`ε` in K12 and K13).

Classification: **missing**. On paper these items are assumptions or open targets (P9, P11, P19–P21,
P27).

***

## 2. Target proposition

**Objects.**

- **Representatives.** Fix `m ≥ 1`. A representative is `r = (V, E, ρ)`, where `V ∈ U(m)`, `E ∈ ℝ^m`
  (in frequency units) and `ρ` is a density matrix. Write `Ω_r = V diag(E) V†` and
  `U_r(t) = e^{−itΩ_r}`.
- **Shift.** `σ_C(V, E, ρ) = (V, E + C·𝟙, ρ)`, so that `Ω_{σ_C r} = Ω_r + C·1`.
- **Classical data.** `κ ∈ 𝒦` collects the substratum `(S, φ)`, the partition, the hidden prior and
  any supplied classical energy–momentum assignment. Per GR:340 the metric is substratum data.
  `κ⁻` denotes `κ` without the metric and without the partition, which the metric fixes (GR:346).
  Classical data are **held fixed** under `σ_C`.
- **Geometry.** `Lor(M)` is the set of Lorentzian metrics on a 4-manifold `M`, and `Sym²(M)` the set of
  symmetric 2-tensor fields. The calibration is `a_* = ħ` (GR:78).

**The completion class 𝒞_div.** A completion `𝔊 = (𝒮, Λ)` has a source map
`𝒮 : 𝒦 × R_m × Lor(M) → Sym²(M)` and the field equation `G[g] + Λ g = 8πG 𝒮(κ, r, g)`, whose left side
is divergence-free. Admissibility has three conditions:

- (Adm1) naturality under diffeomorphisms;
- (Adm2) `∇^μ 𝒮_μν = 0` on solutions;
- (Adm3) calibration through `a_*`.

**The class 𝒞_tf**, used in §5 only. Here the left side is trace-free, `R_μν − ¼R g_μν`, and the source
is the trace-free part of `𝒮` (see R2a). This class is distinct from 𝒞_div.

**The statements.**

- **(TL) Transition-law invariance.** For every `C`, `|U_{σ_C r}(t)_{ij}|² = |U_r(t)_{ij}|²` and
  `Ad_{U_{σ_C r}(t)} = Ad_{U_r(t)}`.
  - The probability clause is K1 [K].
  - The channel clause holds because `U_{σ_C r} = e^{−iCt}U_r` [A].
  - Converse: exact channel equality leaves only such a shift. This is [K] for each step (K7, K5–K6)
    and [P] for their composition (GR:747).
- **(SI) Source invariance of a completion.** For all `κ, r, g, C`: `𝒮(κ, σ_C r, g) = 𝒮(κ, r, g)`.
- **(SI′) Solution invariance of a completion.** For all `κ⁻, r, C`: `Sol(κ⁻, σ_C r) = Sol(κ⁻, r)`,
  where `Sol(κ⁻, r)` is the set of metrics that solve the completion's field equation for the data
  `(κ⁻, r)`. With the metric included in `κ`, (SI′) reads: `g_κ` solves for `r` if and only if it solves
  for `σ_C r`. When Λ is an integration constant, (SI′) and not (SI) is the meaningful form (§5, R2a).
- **Zero-point convention.** A map `Z` from the operational class `[r]` (gaps, mode count, cutoff) to a
  real origin `e_Z([r])`. GR:332 and GR:358 use one: the ground eigenvalue under `½ħω` per mode to the
  cutoff. (TL) does not supply `Z`, because K6 leaves the origin free. Any `Z` is therefore an added
  normalization ([K] for K6; [P] for the reading).
- **(DZ) Zero-point decoupling of a completion.** The source minus `T^cl` contains no dependence on
  `e_Z([r])`, with `T^cl` given by the classical assignment (P11, W1-0). (DZ) is a property of the
  source map, and it does not require `e_Z` to vary independently of `T^cl` in κ-space. A completion whose source reads the origin only
  through `e_Z([r])` satisfies (SI) trivially, because `σ_C` leaves `[r]` unchanged [A]. For such
  completions, (DZ) and not (SI) carries the content of the contrast at GR:352.

**Question.** Does (TL), together with the admissibility conditions and the ordering requirements
(i)–(iii) (examined in B5), entail (SI), (SI′) or (DZ)? As for (SI) and (SI′), (DZ) ⇒ (TL) holds
trivially, and only the forward direction has content (§A.34).

- (SI) ⇒ (TL) and (SI′) ⇒ (TL) hold trivially, because (TL) holds unconditionally.
- Only (TL) ⇒ (SI) and (TL) ⇒ (SI′) have content (§A.34).

**What is not done.** `r` stays an argument of `𝒮`. Restricting `𝒮` to σ-orbits, or to the operational
data `Op(r)`, would give (SI) by construction, so the question would answer itself.

**Lean-style sketch (not built).** Mathlib carries no Lorentzian Einstein tensor [L, recalled], so the
sketch abstracts the geometry.

```lean
-- sketch only; not compiled
structure Rep (m : ℕ) where
  V : Matrix (Fin m) (Fin m) ℂ
  unitary : V * Vᴴ = 1
  E : Fin m → ℝ
  ρ : Matrix (Fin m) (Fin m) ℂ
  trace_one : Matrix.trace ρ = 1

def Rep.shift (C : ℝ) (r : Rep m) : Rep m := { r with E := fun a => r.E a + C }

-- (TL), probability clause: BohrFrequency.shift_modsq (K1), with n := Fin m
example (r : Rep m) (C t : ℝ) (i j : Fin m) :
    BohrFrequency.Umat r.V (r.shift C).E t i j * star (BohrFrequency.Umat r.V (r.shift C).E t i j)
      = BohrFrequency.Umat r.V r.E t i j * star (BohrFrequency.Umat r.V r.E t i j) :=
  BohrFrequency.shift_modsq r.V r.E C t i j

variable (K Geo Src : Type*) [AddCommGroup Src] [Module ℝ Src]

structure Completion (m : ℕ) where
  src : K → Rep m → Geo → Src
  Λ : ℝ
  solves : K → Rep m → Geo → Prop      -- the field equation, abstracted

def SourceShiftInvariant (𝔊 : Completion K Geo Src m) : Prop :=
  ∀ κ r g C, 𝔊.src κ (r.shift C) g = 𝔊.src κ r g

def SolutionShiftInvariant (𝔊 : Completion K Geo Src m) : Prop :=
  ∀ κ r g C, 𝔊.solves κ (r.shift C) g ↔ 𝔊.solves κ r g
```

**Offset provenance.** In (SI), `σ_C` relabels the representative while `κ` stays fixed. A uniform
offset can also be the visible image of a change in classical data. In Main's frozen-bath setting
(Main:340), `Ĥ_eff = H_V + Tr_H[V_int(1⊗ρ_H)]`. With `V_int ∋ 1_V ⊗ B`, a change `ρ_H → ρ'_H` shifts
`Ĥ_eff` by `tr(B(ρ'_H − ρ_H))·1_V`. Neither the channel generator nor the frozen-bath mixture of
bath-conditioned unitaries detects that shift [A]. A geometry-first source (P11) responds to it. This
mechanism elaborates GR:579 and AUDIT item 2.9 (P17, P30), which already record that changes of
absolute level caused by physical processes are not decided by the relative/absolute rule.

***

## 3. Countermodel check (GR §6.2)

### 3.1 Construction

**Data.**

- Any `κ`, with a conserved `T^cl`. A uniform part of `T^cl` is fixed only by the classical-origin
  convention of GR:58 (B2(c)) (conditional, as in B2(c), on a covariant continuum limit in which a
  uniform classical energy has vacuum stress). `T^cl` is otherwise held fixed.
- A reference representative `r₀` on the oriented branch.
- Constants `G`, `ħ`, `Λ₀` and `v > 0`.
- Two offset functionals:
  - `e_free(r) := min_a E_a`, the ground eigenvalue taken as a free coordinate on the σ-orbit;
  - `e_Z(r) := e_Z([r])` for a zero-point convention `Z` (§2).
- `ρ_x(r) := ħ e_x(r)/v` for `x ∈ {free, Z}`.

**Properties of the functionals [A].**

- `e_free(σ_C r) = e_free(r) + C`. `e_free` does not depend on the state `ρ`, the eigenframe `V` or the
  D-gauge. As a free coordinate on the σ-orbit it carries no dependence on the gaps.
- `e_Z(σ_C r) = e_Z(r)`, because `e_Z` depends only on the class. It depends on the gaps and the mode
  count.

**The λ-families.** For `x ∈ {free, Z}` and `λ ∈ ℝ`, set `𝒮^x_λ(κ, r, g) := T^cl − λ ρ_x(r) g` and
`Λ^x_λ := Λ₀ − 8πG λ ρ_x(r₀)`.

- **K_dec** is `λ = 0` (the same for both families): `G[g] + Λ₀ g = 8πG T^cl`.
- **K_cpl^free** is `x = free`, `λ = 1`: `G[g] + Λ^free_1 g = 8πG (T^cl − ρ_free(r) g)`.
- **K_cpl^conv** is `x = Z`, `λ = 1`: `G[g] + Λ^Z_1 g = 8πG (T^cl − ρ_Z(r) g)`.

`Λ^x_λ` is a constant of the completion. Covariance and the closure route leave it undetermined
(P18). "K_cpl" without a superscript means both.

**At `r₀` the field equations coincide [A].** For every `x` and `λ`, the equation at `r₀` reads
`G + Λ₀ g − 8πGλρ_x(r₀) g = 8πG T^cl − 8πGλρ_x(r₀) g`, which is K_dec. With the same initial data the
solution is the same.

**Admissibility [A].**

- Every member is natural, because `g` and the scalar `ρ_x(r)` are.
- Every member is conserved, because `∇g = 0` and `ρ_x(r)` is constant on `M`.
- Every member uses `a_*`.

**Response to the shift [A].**

- Under `r₀ ↦ σ_C r₀`, K_dec is unchanged.
- K_cpl^free becomes `G + Λ₀ g = 8πG(T^cl − (ħC/v) g)`, so `ΔΛ_eff = 8πGħC/v`. It therefore violates
  (SI) whenever `C ≠ 0`, `ħ/v ≠ 0` and `g ≠ 0`. It also violates (SI′), because the two equations have
  different de Sitter radii.
- K_cpl^conv is unchanged under `σ_C`, so it satisfies (SI) and (SI′). Its source minus `T^cl` is
  `−ρ_Z g`, which depends on `e_Z`. It therefore violates (DZ). K_dec, whose source minus `T^cl` is
  zero, satisfies it.

**Scope of "only".** At fixed `κ` the transition law is fixed, so the class `[r]` is fixed. Within
the class, the residual freedom of `r` is (under K9's hypotheses, §1.1) the shift, the D-gauge, the
eigenframe phases and the antiunitary branch. On the oriented branch, which a passive non-uniform state
selects (K11), only the shift moves `e_free`. So on that branch K_cpl^free and K_dec differ only in how
they respond to the shift.

No shift-equivariant functional is invariant under a reflection `E ↦ −E + c` with `c` independent of
`E` [A]. Under a reflection anchored to the spectrum (`E ↦ −E + 2·mean(E)`), the mean `tr Ω/m` is
invariant. Since K9 leaves `E₀` free in the reflected branch, how K_cpl responds to the branch is a
convention. "Differ only" is stated on the oriented branch, where the question does not arise.

**On shell, two cases [A].**

- **(a) K_cpl^free.** `e_free` is a free coordinate on the σ-orbit. With the metric in `κ`, the field
  equation fixes only `Λ^free_1 + 8πGρ_free(r)`. At a fixed `Λ^free_1`, K_cpl^free admits a metric for
  every value of `Λ_eff`. It is therefore world-equivalent to K_dec with Λ₀ left undetermined (the union over Λ₀), the corpus's standing for Λ (GR:162, GR:334, GR:356). It is not world-equivalent to K_dec at one fixed
  `Λ₀`. No fine-tuning reading applies.
- **(b) K_cpl^conv.** `e_Z` is the ground eigenvalue under the emergent normalization (`½ħω` per mode
  to the cutoff; GR:332, GR:358). It is a function of the reconstructed gaps and mode count, so
  `ρ_Z(r₀)` is fixed by the emergent class and not read back from the field equation. Whether the
  observed `Λ_eff` is `Λ^Z_1 + 8πGρ_Z(r₀)` is then the fine-tuning reading at GR:352.

### 3.2 Data shared at `r₀`

| Datum | Shared? | Reason |
|---|---|---|
| Substratum `(S, φ)` | yes | No map from `(S, φ)` to a source is on `main` (P26, P27; GR:695). The metric, which is substratum data under GR:340, is the same. [P] |
| Partition | yes | Fixed by the causal structure of `g` (GR:40, GR:346). The same `g` gives the same horizon, `A` and mode count. [A] |
| Reduced transition law | yes | It depends on the substratum, the partition and the prior. `σ_C r₀` gives the same law (K1). [K] |
| Fixed-basis representation | yes | `r₀` and `σ_C r₀` lie in one class (K6, K9). [K] |
| Action-scale calibration | yes | κ cancels (GR:78, GR:751). The null-flux term `ρ g_μν k^μ k^ν = 0` vanishes, so the first-law prefactor is the same. [A] plus [P] |
| Ordering requirements (i)–(iii) (GR:342–348) | yes at `r₀` | The completions have the same metric, and it is classical. K_cpl^free survives (ii-W) and (ii-L); it is excluded by (ii-S). Whether (ii) excludes K_cpl^conv's dependence on post-partition data is the verdict of B5. [P] |
| Channels and circuit data | yes | The scalar cancels in `Ad`. [A] |
| Gibbs/KMS, passivity, OTI, counting profile, stationarity | yes | Each is shift-invariant (K10–K14). [A] and [K] |

**What differs.**

- K_cpl^free against K_dec: only `∂Λ_eff/∂C` on the oriented branch, 0 against `8πGħ/v`.
- K_cpl^conv against K_dec: only the term `−ρ_Z g` in the source minus `T^cl`. At fixed `κ` nothing
  differs.
- Whether pairs `κ, κ′` with equal `T^cl` and different `e_Z` exist is not shown. By GR:573, relative
  differences appear in `T^cl`. Any statement about such pairs is conditional on their existence.

**Scope of the shared list.** The list covers the operational content of the emergent generator. The
corpus also states absolute emergent quantities that depend on the representative:

- `½ħω` per mode and `ρ_QFT` (GR:332, GR:336);
- "the ground-state eigenvalue of Ĥ_eff" (GR:358).

These are not shift-invariant. K_cpl^free couples to the ground eigenvalue as a free coordinate, and
K_cpl^conv couples to its convention-fixed value. Unlike the antiunitary
branch, which oriented thermal structure excludes (K11, K12), the origin is fixed by none of the
shift-invariant structures above.

### 3.3 Precision on GR:352 as written

GR:352 writes `𝒢 = 8πG T^cl` and `𝒢 = 8πG(T^cl − ρ_C g)` with one `T^cl`. Read with the same constant
term, the de Sitter solutions differ for `ρ_C ≠ 0`. Then `H²` moves by `8πGρ_C/3`, and `A = 4πc²/H²`,
the boundary mode count and the partition move with it [A].

The pair therefore shares the partition only in three cases:

1. `𝒢` includes a free constant, adjusted as in §3.1.
2. `T^cl` is relabelled, `T^cl_2 = T^cl_1 + ρ_C g`. The classical-origin freedom of B2(c) permits
   this: a uniform part of `T^cl` is fixed only by the convention of GR:58 (conditional, as in B2(c),
   on a covariant continuum limit in which a uniform classical energy has vacuum stress).
3. `ρ_C = 0`. The pair then coincides, and the claim is empty.

Only the first two readings keep the content of GR:352. On either of them the non-implication at
GR:352 holds. See owner question Q1.

### 3.4 Pressure tests (§A.31)

**B1. "The origin is gauge, so a completion that reads it is unphysical; hence (SI)."**

The origin is gauge relative to the operational data (K1, K5–K7, K10–K14). It is not gauge relative to
gravitational response. Declaring it gauge for all physics restates (SI). Outside gravity the energy
origin is unobservable, and gravity couples to it [L, recalled: Weinberg 1989, cited at
Introduction:157].

K_cpl^free needs no outside structure: on shell the metric fixes its free coordinate, which is a
relabelling (§3.1, case (a)). K_cpl^conv takes its origin from a convention `Z`, which (TL) does not
supply (§2).

Node verdict: **rejected as a derivation.**

**B2. "Under the geometry-first source (P11), `r` is not an argument of `𝒮`, so (SI) holds."**

If `𝒮` depends only on `(κ, g)`, then (SI) holds at fixed `κ` [A]. Three limits apply.

- (a) Requirements (i)–(iii) concern the metric at the partition boundary. For a uniform term, that
  boundary is the cosmological horizon itself, so the laboratory scope of GR:350 does not apply. See
  B5.
- (b) P11 is a posit (GR:352, "the geometry-first proposal"). It removes `r` from the domain of `𝒮`.
  It therefore entails (SI) as a premise; it does not derive it.
- (c) The classical origin stays free.
  - Classical evolution is blind to `H_tot ↦ H_tot + b`: `{b, ρ} = 0` (Main:62), and φ conserves every
    function that is constant on its cycles (GR:84) [A].
  - The additivity and conservation in W1-0 survive per-cell constants [A].
  - A uniform per-cell energy `b` moves `T^cl` by `−(b/ε³) g` [A]. This is **conditional** on a
    covariant continuum limit in which a uniform per-cell energy has vacuum stress. That limit is open
    (GR:12; GR:697(ii)).

Node verdict: (SI) is **conditional on P11**. The question moves to the classical origin, which the
corpus fixes by convention (GR:58) and whose value it takes as an input (GR:334, GR:356).

**B3. "Conservation and the Bianchi identity exclude K_cpl."**

For constant `C`, every λ-member is conserved. Take a time-dependent uniform shift `C(t)`, which is
still invisible (`U ↦ e^{−i∫C}U`; GR:292). It requires `∂_ν ρ = ∇^μ T^cl_μν` [A], hence either energy
exchange or a running `G` (GR:374).

Node verdict: **rejected for the constant case.**

**B4. "Covariance fixes the trace sector."**

Covariance, a second-order metric-only left side and a divergence-free left side together admit
`Λ g` (GR:162) [L, recalled: Lovelock 1971].

Node verdict: **rejected.**

**B5. "The ordering requirements (i)–(iii) exclude a boundary metric that depends on the emergent
offset."**

Support class: GR:342–348 is a paper argument [P]. It is not kernel-checked. The book calls the ordering
"not a stipulation but a structural consequence" (book/ch07-gravity.md:187).

- **(i) Definiteness (GR:344).** Satisfied. On shell, `ρ_x(r)` is a definite real number: fixed by
  the field equation for `x = free`, by the convention for `x = Z` (§3.1). The metric is classical and
  not in superposition. [P]
- **(iii) Uniqueness of ħ (GR:348).** Satisfied. `ħ = τ_K/β_E` does not depend on κ (GR:751). A Hubble
  rate that depends on `ρ_x(r)` therefore leaves ħ independent of the state. [A]
- **(ii) Non-circularity (GR:346).** The argument reads: "If the metric were derived from QM … QM →
  metric → causal structure → partition → QM … The circle breaks only if the metric exists prior to the
  partition." Three readings are distinguished.
  - **Strong reading (ii-S).** The boundary metric's dynamical law has no argument that is defined only
    after the partition. (ii-S) excludes K_cpl^free and K_cpl^conv, and every `λ ≠ 0` in either
    family [A]. Under (ii-S), (SI) holds at fixed `κ`, and (DZ) holds for the uniform term [A,
    conditional on (ii-S)].
  - **Loop reading (ii-L), GR:346 as argued.** No self-consistent loop runs through post-partition
    data. (ii-L) is weaker than (ii-S). It excludes K_cpl^conv and not K_cpl^free (below).
  - **Weak reading (ii-W).** The metric is a classical datum that is definable before the partition, so
    the chain of definitions has an entry point. Both coupled completions satisfy (ii-W). Their metric
    is the classical substratum metric (GR:340), and the emergent quantity enters only its dynamical
    law.
- **Where the loop closes [P].** For K_cpl^free the loop does not close: the metric fixes the origin's
  coordinate. For K_cpl^conv it closes through the gaps and the mode count: partition → transition
  data → `e_Z` → metric → partition. GR:346 as argued ("no entry point") therefore excludes K_cpl^conv.
- **Which reading the corpus uses [P].**
  - GR:358 admits feedback from the emergent description into gravitational dynamics "through
    state-level quantities", for the cosmological metric (the running vacuum). In the same paragraph it
    excludes "the zero-point sum".
  - GR:374 speaks of "the emergent vacuum energy" as a state-level quantity "depending on the hidden
    sector's volume".
  - GR:400 Reading 1 feeds back "the emergent layer's curvature response — the ∼m²H² piece that
    survives adiabatic renormalization precisely because it is an epoch-differential (relative) effect
    in the sense of §8.3".
  - §8.3 (GR:573) says that relative differences gravitate because "there is a classical microstate
    difference corresponding to this energy difference … Relative differences appear in the classical
    stress-energy tensor". GR:575 places absolute levels assigned by the emergent description on the
    other side.
  - On the corpus's own account, then, Reading 1 feeds back the emergent computation of a quantity
    that has a classical counterpart. That is a classical source evaluated through the emergent
    description, not a loop through post-partition data. On this account Reading 1 and GR:346 are
    reconciled.
  - This account is conditional on §8.3's identification of relative emergent effects with classical
    microstate differences, which is part of the geometry-first proposal (GR:573–579; P17).
  - A further caveat [P]: the piece Reading 1 feeds back is relative between epochs. GR:579 records
    that the relative/absolute rule does not fix how energy changes between epochs couple (the
    electroweak and QCD transitions; AUDIT.md:55, item 2.9). By analogy, classing an epoch-differential
    vacuum term as relative in §8.3's sense rests on GR:400's statement and not on a derivation.
  - K_cpl^conv's `e_Z` is the absolute ground eigenvalue (GR:332, GR:358), which GR:575 classes as
    having no classical counterpart. The corpus's use therefore does not admit K_cpl^conv. K_cpl^conv
    survives only under (ii-W) applied to absolute emergent quantities, and no corpus text adopts that
    reading.
  - GR:400 states a strict reading separately, as "Reading 2 (strict geometry-first)", and does not
    adjudicate between the two readings.
  - Reading 1 excludes the constant emergent part by stipulation: "the substratum budget fixes the
    constant part" (GR:400). That is consistent with GR:575, but it restates (DZ) for the constant part.
    It does not derive it.
- **Skepticism toward the readings that favour decoupling.**
  - (ii-S) would give (SI) directly. (ii-L) would give (DZ) directly.
  - Holding either as a premise would remove GR:400's Reading 1 and the feedback stated at GR:358 and
    GR:374 only if §8.3's identification fails. Otherwise both stand.
  - The force of (ii-L) against self-consistent fixed points is not established. GR:346 is a
    requirement on the order of derivation, not a proof that no fixed point exists. This is what keeps
    Part 2 of the verdict conditional rather than derived.
- **Node verdict.**
  - K_cpl^free survives (ii-W) and (ii-L), and it is excluded by (ii-S). It is world-equivalent to K_dec with Λ₀ left undetermined (the union over Λ₀), the corpus's standing for Λ (GR:162, GR:334, GR:356).
  - K_cpl^conv is excluded by (ii-S) and by (ii-L). It is not admitted by the corpus's use,
    conditional on the §8.3 identification. It survives only under (ii-W) applied to absolute emergent
    quantities.
  - **Assumption-watch AW-loop:** see §6.

B3, B4 and B5 add no NEW finding. B5 yields one ELABORATING finding (F8, AW-loop). The fixed point of
§A.31, three to four empty passes, is not claimed.

***

## 4. Dependency trace

| Dependency | Supplies | Supplied by OI? | Where stated | Bearing on the offset |
|---|---|---|---|---|
| G3: field equations, conservation/Bianchi, continuum | the equation and its source | no: open | GR:12, :352, :633, :655; ROADMAP.md:85 | (SI) and (SI′) are properties of the left-side and source pair (§5, R2). |
| Source choice | which tensor is `𝒮` | no: posited (boundary), open (laboratory) | GR:340, :350, :352; ROADMAP.md:1214–1219; Introduction:161 | Under P11, (SI) holds at fixed `κ` (B2). |
| Ordering requirement (ii) | exclusion of an emergent argument | paper argument | GR:342–348; book/ch07-gravity.md:183–187 | (ii-S) excludes both coupled completions. GR:346 as argued (ii-L) excludes K_cpl^conv. The corpus's use does not admit it, conditional on §8.3 (B5, AW-loop). |
| W1-0 | `T^cl` from the substratum | no: an assumption | W1-1-REPORT-r4.md:140, :301; GR:58, :695; SM:292 | Per-cell constants are free [A]. |
| Classical origin conventions | absolute classical energies | conventions and definitions | GR:58; GR:422–426 | They carry the origin under P11 (F5). |
| Emergent–classical intertwiner | origin transport | slope only | GR:70, :74, :86 | `E_0` is free. Holding the classical `E` fixed under `σ_C` decouples the offset. Holding `E_0` fixed couples it. The corpus fixes neither. |
| Conservation and Bianchi | constancy of a coupled offset | geometric identity; matter conservation posited | GR:374; GR:12 | Constrains only time-varying offsets (B3). Fixes the admissible `ℱ` (R2). |
| Continuum limit and covariance | `(M, g)`, natural `𝒮`, vacuum stress tensor | no: open | GR:12; GR:697(ii); SM:144–148, :160–162 | The countermodel needs a natural source. Per-cell vacuum stress is conditional (B2(c)). |
| Matter–boundary transfer | `Q = M_B c²` | no: an assumption | GR:466; ROADMAP.md:1194–1198 | A difference of energies, so invariant under `σ_C` [A]. |
| State selection | thermal state, calibration | no | GR:62–66, :74, :88 | Shift-invariant (K10, K11) [A]. |
| `10^122` relation | — | — | GR:362; GR:334, :356 | No dependency, and no Λ prediction drawn. |
| C4 at the cosmological cut | partition-level realization | no | GR:52 | Independent of the offset. |

None of these is derived on `main`: the G3 equation, the source choice, a reading of (ii),
W1-0, the classical origin, the transport of `E_0`, the continuum limit and covariance, `Q = M_B c²`,
and the state selection.

***

## 5. Verdict, routes and obligations

**Verdict.** Two parts (§0).

1. **Counterexample, for source maps.** (SI) is not implied on the weak and loop readings of
   requirement (ii) ((ii-W), (ii-L)) (K_cpl^free). Under the strong reading (ii-S), which corresponds
   for the source to GR:400 Reading 2, (SI) follows conditionally. K_cpl^free is world-equivalent to K_dec with Λ₀ left undetermined (the union over Λ₀), the corpus's standing for Λ (GR:162, GR:334, GR:356).
2. **Conditional on (ii-L), for the coupling with physical content.** (DZ) for the convention-fixed
   offset follows conditional on GR:346's argument (ii-L) [P]. The force of (ii-L) against
   self-consistent fixed points is not established. K_cpl^conv is compatible with OI's results only
   under (ii-W) applied to absolute emergent quantities, a reading no corpus text adopts.

**Routes to (SI), (SI′) or (DZ).** These are proposed routes, each given with its status. None is adopted.

- **R0. GR:346 as argued (ii-L): no self-consistent loop through post-partition data.**
  - It excludes K_cpl^conv, and (DZ) for the convention-fixed offset follows for the uniform term
    [A, conditional on (ii-L)].
  - It is weaker than (ii-S) and already suffices against K_cpl^conv. It does not exclude K_cpl^free,
    which is world-equivalent to K_dec with Λ₀ left undetermined (the union over Λ₀), the corpus's standing for Λ (GR:162, GR:334, GR:356).
  - The stronger (ii-S) corresponds, for the source, to GR:400's Reading 2.
  - Status: the text of GR:346 as argued. The corpus's use (GR:358, GR:374, GR:400 Reading 1) is
    consistent with it, conditional on §8.3's identification (AW-loop). Its force against
    self-consistent fixed points is not established.
  - Holding it as a premise is a decision under §A.29.
- **R1. Geometry-first source (P11).**
  - It yields (SI) at fixed `κ`.
  - Status: posited. It moves the question to the classical origin (B2).
- **R2. An equivariant left-side and trace-sector pair.** Take the target form
  `E_μν = 8πG(T − ℱ[g,T]g)` (GR:12). A uniform term `T ↦ T − ρg` with constant `ρ` leaves the right side
  unchanged if and only if `ℱ[g, T − ρg] = ℱ[g, T] − ρ` [A]. `ℱ = const` fails this condition [A].
  Admissibility depends on the left side. There are two realizations.
  - **R2a. Trace-free left side** (class 𝒞_tf).
    - The equation is `E_μν = R_μν − ¼R g_μν` with `ℱ = ¼ g^{μν}T_μν + c`. The trace of the equation
      forces `c = 0` [A].
    - The contracted Bianchi identity and `∇^μ T_μν = 0` give `∂_ν(R + 8πG T^μ_μ) = 0` [A]. Hence
      `R + 8πG T^μ_μ = 4Λ_int`, and `Λ_int` returns as an integration constant.
    - The left side is not divergence-free, and the source `T − ¼Tg` is not conserved. The class lies
      outside 𝒞_div.
    - The field equations do not contain `ρ` [A]. So (SI′) holds over the full solution set. At fixed
      data, (SI′) holds if and only if the datum that selects the solution is a function of `κ`
      alone, not of `r`.
      - Example: the metric as substratum data (GR:340). Then `g_κ` solves for every `r` [A].
      - (SI′) fails if the selecting datum is `Λ_int` defined from a trace that contains `ρ_x(r)` [A].
    - Whether unimodular gravity removes the vacuum-energy problem is debated on exactly this point
      [L, recalled].
    - The corpus's conditional Jacobson route has this structure. Its input (iii), the null flux
      `δQ = ∫T_μν k^μ dΣ^ν` (SM:160), constrains only null–null components. Those components do not see
      `−ρ g` because `g_μν k^μ k^ν = 0` [A]. The displayed Λ (SM:162) is then the integration constant
      [L, recalled: Jacobson 1995].
    - Status: literature [L, recalled: Ellis, van Elst, Murugan and Uzan 2011, listed at
      Introduction:244 and cited at :161]. On the Jacobson route it is conditional on SM:160's open
      inputs, which include the source coupling of GR §6.2. It is not derived in OI.
  - **R2b. Divergence-free left side** (class 𝒞_div).
    - (Adm2) requires `∂_ν ℱ = 0` on solutions [A]. So `ℱ = ¼T` violates conservation for any matter
      whose trace is not constant.
    - A shift-equivariant, conserved `ℱ` must be a spacetime constant. One example is a spacetime
      average `ℱ = ¼⟨g^{μν}T_μν⟩` (defined when the spacetime 4-volume is finite, or for a normalized
      average) [A]. This is the structure of sequestering [L, recalled: Kaloper and
      Padilla 2014, listed at Introduction:258 and cited at :161]. The sequestering route of r1 is
      therefore R2b, not a separate route.
    - A cycle average over OI's finite recurrence (GR:585) would be one candidate for a spacetime-global
      functional. That is a conjecture and is not examined here.
- **R3. Substratum phase (conjecture).**
  - `P_φ` is a definite unitary with determinant `sgn φ`. A choice of branch would fix a total-system
    frequency origin up to `2π/Δt · ℤ` and the per-mode branches (GR:84).
  - Obstruction: the visible generator is reconstructed from data that do not see a phase (K7). The
    branch choice is unselected.

**Obligations.**

- **O0 (proposed by review r1; adopted as the first obligation).** Settle what requirement (ii)
  (GR:346), on the GR:350 scope, implies for a boundary metric that depends on the emergent origin.
  - Status: addressed on paper in B5, pending review.
    - K_cpl^free survives (ii-W) and (ii-L), and (ii-S) excludes it. It is world-equivalent to K_dec
      with Λ₀ left undetermined.
    - (ii-S) and GR:346 as argued (ii-L) both exclude K_cpl^conv.
    - The corpus's use (GR:358, GR:374, GR:400 Reading 1) does not admit K_cpl^conv, conditional on
      §8.3's identification (GR:573).
  - Remaining:
    - Whether (ii-L) holds against self-consistent fixed points. This is a proof question, and it is
      open.
    - Whether to hold (ii-L) as a premise. That is an owner decision under §A.29 (Q7). It removes
      Reading 1 only if the §8.3 identification fails (Q8).
  - If (ii-L) is held, (DZ) for the convention-fixed offset follows conditionally, and O1 becomes
    secondary for that question.
- **O1.** Decide whether OI's premises force the G3 equation's dependence on `T`, including its
  Λ-sector, to be invariant under `T ↦ T − ρg` (constant `ρ`) on its solution set, with conservation
  carried.
  - Known admissible realizations are R2a, with `Λ_int` fixed by classical data, and R2b, with `ℱ` a
    spacetime-global functional.
  - A non-equivariant admissible completion compatible with every OI premise is a G3-level
    countermodel. The λ-families of §3.1 give one at the level of the source map.
    - For K_cpl^free it is compatible with every OI premise unless (ii-S) is held.
    - For a convention-fixed coupling (K_cpl^conv) it is compatible only under (ii-W) applied to
      absolute emergent quantities, a reading no corpus text adopts (B5).
  - Prerequisite: W1-0 fixes what `T` is.

Every route leaves the value of Λ an input. This record makes no claim about the magnitude of Λ.

***

## 6. Findings

| ID | Finding | Class | Support |
|---|---|---|---|
| F1 | The non-implication at GR:352 holds, in the two-part form of §0. The λ-families are natural and conserved and share every listed datum at `r₀` (B5: K_cpl^free on (ii-W) and (ii-L), excluded by (ii-S); K_cpl^conv only under (ii-W) applied to absolute emergent quantities). On the oriented branch, K_cpl^free differs only in how it responds to the shift. K_cpl^conv differs only by the term `−ρ_Z g` in the source minus `T^cl`. | POSITIVE | [A] §3.1–3.2, §3.4 |
| F2 | GR:352's pair shares the partition only with a free constant in `𝒢` or with a classical-origin relabelling of `T^cl` (the relabelling conditional, as in B2(c), on a covariant continuum limit in which a uniform classical energy has vacuum stress). Under `ρ_C = 0` the claim is empty. | ELABORATING | [A] §3.3 |
| F3 | The shared data extend beyond GR:352's list to the operational content of the emergent generator (K10–K14, channels). Oriented thermal structure fixes the orientation; it does not fix the origin. The corpus's absolute emergent quantities (GR:332–336, :358) depend on the representative. | POSITIVE | [K], [A] |
| F4 | Offset provenance. A shift at fixed classical data, and a shift induced by a change of hidden state (the frozen-bath mechanism of Main:340), are both invisible to (TL). P11 treats them differently. (SI) is therefore stated at fixed `κ`. Extends GR:579 and AUDIT item 2.9. | ELABORATING (mechanism and target form) | [A] §2 |
| F5 | GR:58's `E` is by definition the first-law energy. Its de Sitter value `c⁴R/G` is the first law integrated from `R = 0` with zero constant [A]. GR:422's `E_s := S_dS k_B T_cl = c⁴R/(2G)` is a different quantity by definition. The factor 2 is the Euler relation for `S ∝ E²`. Under P11 the origin of `E` is a convention (GR:58). `E_s` carries no energy-origin constant; it inherits the additive constant of `s_H` (GR:58), set to zero in `S_dS = σA/ε²` (GR:422). | ELABORATING (assumption-watch AW-abs) | [A] |
| F6 | The equivariance condition on `ℱ` decides offset invariance only together with the left side. With the divergence-free left side named at GR:12, `ℱ = ¼T` is inadmissible, and the equivariant admissible choices are spacetime-global (R2b). The trace-free realization (R2a) leaves the divergence-free class. | ELABORATING (assumption-watch AW-G12) | [A] §5 |
| F7 | The header of `BohrFrequency.lean` names `shift_normSq` (:8) and `reflect_normSq` (:9); the declarations are `shift_modsq` (:235) and `reflect_modsq` (:279). | minor | read |
| F8 | Requirement (ii). K_cpl^free survives (ii-W) and (ii-L), is excluded by (ii-S), and is world-equivalent to K_dec with Λ₀ left undetermined. (ii-S) and GR:346 as argued (ii-L) exclude K_cpl^conv. The corpus's use does not admit it, because GR:400 Reading 1 feeds back only a piece classed as relative in the sense of §8.3 (GR:573). That reconciliation of GR:346 with GR:358, GR:374 and GR:400 is conditional on §8.3 and is not stated. | ELABORATING (assumption-watch AW-loop: the GR:346 / GR:400 reconciliation is conditional on §8.3 and unstated) | [P] B5 |
| F9 | On the corpus's conditional Jacobson route (SM:160–162), the uniform offset drops out of the field equations through the null flux. The offset question becomes the question of which datum selects the integration constant. | ELABORATING | [A], [L, recalled] |

**Algebra for F5 [A].**

- `S_dS = σ·4πc²/(H²ε²)` and `T_cl = c³ε²H/(8πG k_B σ)` (GR:422). Hence
  `S_dS k_B T_cl = c⁵/(2GH) = c⁴R/(2G)`.
- `k_B T_cl dS_dS = c⁴ dR/G`. Integrated from `R = 0`, this gives `c⁴R/G`.
- `ρ_s = E_s/V_H = 3c²H²/(8πG)`. The integrated Clausius energy over `V_H` gives `2ρ_crit`.

**Assumption-watch markers.**

- **AW-prov (F4).** Invisibility to transition data used as a criterion of gravitational inertness:
  GR:352, GR:577, Introduction:159.
- **AW-abs (F5).** GR:426 attributes `ρ_s = ρ_crit` to "Jacobson's Clausius relation". The integrated
  Clausius energy gives `2ρ_crit`. The value `ρ_crit` follows from the product definition
  `E_s = S_dS k_B T_cl`: the Clausius relation supplies `T` and the area law supplies `S`. This record
  makes no magnitude claim.
- **AW-loop (F8).**
  - GR:346 and the wording "emergent vacuum energy" at GR:358, GR:374 and GR:400 are in apparent
    tension.
  - GR:400's own qualifier ("relative … in the sense of §8.3") reconciles them, conditional on §8.3's
    identification of relative emergent effects with classical microstate differences (GR:573). That
    identification is part of the geometry-first proposal.
  - The reconciliation is not stated at GR:346.
  - The epoch-differential character of the fed-back piece adds the caveat recorded at GR:579 and in
    AUDIT item 2.9.
  - This unit proposes no manuscript change.
- **AW-G12 (F6).** GR:12's clause "under which the distinct-descriptions argument becomes a theorem of
  the dynamics" holds only for an equivariant `(E, ℱ)` pair. The printed target form does not supply
  one, so the clause is conditional on it. This unit proposes no manuscript change.

***

## 7. Literature

All of these entries are recalled, and none was re-read. No verdict rests on any of them.

- S. Weinberg, Rev. Mod. Phys. 61, 1 (1989). Listed at Introduction:288 and cited at :157. A vacuum
  energy enters as `−ρ g_μν` and cannot be distinguished from a bare Λ.
- D. Lovelock, J. Math. Phys. 12, 498 (1971). Cited at GR:162.
- T. Jacobson, Phys. Rev. Lett. 75, 1260 (1995). The null-flux Clausius route gives the Einstein
  equations with Λ undetermined.
- G. F. R. Ellis, H. van Elst, J. Murugan and J.-P. Uzan, Class. Quantum Grav. 28, 225007 (2011).
  Listed at Introduction:244 and cited at :161. Trace-free equations.
- N. Kaloper and A. Padilla, Phys. Rev. Lett. 112, 091304 (2014). Listed at Introduction:258 and cited
  at :161. Sequestering, with Λ tied to a spacetime average of the trace.
- R. M. Wald, *Quantum Field Theory in Curved Spacetime and Black Hole Thermodynamics* (University of
  Chicago Press, 1994). The section number is recalled as §4.6 and was not verified. The stress-tensor
  axioms leave a residual ambiguity that includes a term proportional to `g_μν`.
- The debate on whether unimodular gravity solves the cosmological-constant problem, centred on how the
  integration constant is selected. No specific paper is cited.
