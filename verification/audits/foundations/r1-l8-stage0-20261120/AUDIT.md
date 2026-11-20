# R1-L8 Stage 0 — which observational conclusions need a selected probability law

**Status.** Writer's paper-only requirements audit, WIP / UNVERIFIED. Classes, schema, controls and
decision rule were fixed in `PREREG.md` (commit `e87910a3`, pushed before this file). Existing
evidence only: no new measure construction, no replacement law, no new physical assumption, no
manuscript, Lean or registry edit. Independent non-author review is required before any use. A1
(Main posit ledger item (ii)) remains open and unadopted; nothing here authorizes Stage 1.

**Authorization and goal link.** As in `PREREG.md`: owner `amaybaum`,
[#1169 comment 7039208422](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7039208422),
2026-11-20T12:11:13Z. Goal link (§A.47), from the authorization: decides how much of OI genuinely
needs a selected probability law and how much needs only a declared law with provable properties.

**Source pin.** `main` at `23a28dab9976e67482d45247bc2fdcce10e224a8`; `M:n`, `GR:n`, `SM:n`,
`Sub:n`, `Str:n`, `Comp:n`, `Meth:n` are lines of `papers/Main.md`, `GR.md`, `SM.md`,
`Substratum.md`, `Structure.md`, `Complexity.md`, `Methodology.md` at the pin. Reused records are
cited by the short names of PREREG §2 with their own line numbers.

**Framing (owner technical note).** Every finding below concerns whether the particular law a
conclusion needs is justified, or which properties of a declared law suffice. Infinite full-product
carriers admit normalized translation-invariant laws and entropy densities (R1-INF Lemmas 1–2); no
row turns on probability or maximal entropy being undefined. Where a row cites the absence of an
invariant probability, it is for a specific countable or coupled carrier on which that absence is
proved (R1-INF C1; P7B 6.3 (ii)).

## 1. Verdict (generated from the table in §2)

**Counts.** 21 conclusion rows. Class (a): 2 (M2.a, M3.e). Class (b): 12. Class (c): **N_c = 7**. Of the seven (c)
rows, 4 have a `RETRO` observational consequence (they reproduce known values: the horizon
temperature, the ħ calibration, the Bekenstein–Hawking 1/4, the observed non-equilibrium phase),
0 have an `ACC` consequence, and 3 have none (`NONE`/`REC`). Under the alternative reading R′ of
PREREG §5, **N_c′ = 13** (adds M2.d, M3.a, M3.b, M3.c, C4.a, C4.b, whose weakest sufficient
condition fixes one finite factor of the law to be uniform).

**Decision rule applied (PREREG §6, N_c > 0).** R1 remains open for the following rows, each of
which obtains its claimed result only with a particular law or a selection principle:

| Row | Selection premise | Unresolved obligation |
|---|---|---|
| M1.a | Lemma 3's canonical (counting / maximal-entropy) law fixes the emergent description from the partition alone | Physical selection of the canonical law; in infinite volume P-ED supplies it only through (G3)+(G4), which restate the uniform posit (R1-INF §7) |
| M2.b | μ-O: the uniform law on the finite orbit of the actual microstate, carrying the static budget log₂(\|S\|/ℓ) and the orbit capacity log₂ p | No infinite-volume form: under β_A μ-O coincides with μ-G for β_A-typical points and the budget is not supplied (R1-INF Prop. 7.1); lemma L2 cannot deliver the static budget |
| M2.c | μ-R / posit (iv): maximal entropy compatible with the observer's records, as the uniform law on a finite orbit union | Collapses to μ-G at orbit level in infinite volume (R1-INF Prop. 7.2); with a reference law it is conditioning, a preparation (R1-INF Prop. 7.3) |
| C1.a | Equal weighting of the boundary-shell configurations (H-count; P7B H4) sets the slope β_E | Physical selection of the shell law (P7B 6.4; GR:88); coupled case: existence of a normalized invariant shell law (P7B 6.3, open Q1) |
| C1.b | As C1.a, through a_* = τ_K/β_E | As C1.a |
| C1.c | As C1.a, through the calibrated ε²/σ | As C1.a |
| M19.a | The typicality measure of canonical typicality (normalized unitarily invariant measure on a finite-dimensional energy shell) fixes "every local subsystem is in local equilibrium" | Lemma L8 or scope narrowing to a supplied local equilibrium (LE); physical source of the equilibrium state (A1-05 P8-S) |

No `ACC`-type conclusion traced here requires a selected law. This does not mean any law it uses is
physically justified: every (b) row carries property premises ((IP), (NR), Θ-invariance, equal
root masses, H-blind, H-ν, H-BD with its fibrewise property, (D5)) for which the framework gives no
reason that nature realizes them (column "Physical justification"), and every (a) row still
presupposes that nature's law is invariant at all. A1 remains open and unadopted.

**Findings beyond the classification (each [W] or cited; for the reviewer).**

- **F1 (M3.d).** For the selected update on `ℤ^d` (q prime, α ≠ 0, lattice-convex windows) the
  recurrence-scale P-indivisibility conclusion of §2.3 differs between two laws that are both
  invariant under the update and under translations: under β_A, the law P-ED selects, the rooted
  family is P-divisible at every horizon (NR-1 Thm. 3.3); under the torus counting law μ_L on the
  periodic configurations (R1-INF Lemma 1 (a)) the update has finite order on the support, and
  RIGID's kernel theorem gives P-indivisibility within a finite horizon [W]. The premise (NR) of
  M:131 is therefore false under the one selected law available and true under laws that
  reintroduce total finiteness under another name (NR-1 open question 3).
- **F2 (C4).** The counting step of H-BD's proof (GR:126) uses a property the counting measure has
  for every injection: an injection does not increase the number of points mapped into a set. A
  measure-theoretic H-BD (L10) would need the corresponding fibrewise non-expansion of the deep law,
  not only its normalization [W]. GR:128's own example shows that visible data depend on the deep
  law when the deep sector couples [W].
- **F3 (M19).** The global-to-local step fails for a law of maximal centred entropy density: for the
  selected update in d ≥ 2, m_H is invariant with h̄(m_H) = log|A| and u(0) = 0 almost surely (R1-INF
  Prop. 9 (b)), so the one-site marginal at the origin is not the equilibrium one [W, classical
  substratum reading, not Main's quantum canonical typicality].
- **F4 (C1.d).** The value a₀ = cH/6 and its companions in GR §7.3 contain no quantity fixed by the
  counting law at measured ħ and H; the law enters only through ε²/σ, which a₀ does not contain [W].
  GR:470 lists H-count among the inherited conditions; the trace finds only the existence of a
  log-rate slope load-bearing for the value.

## 2. The table

Observational-consequence types and classes are as defined in PREREG §§4–5. Layers: K (kernel
declaration on `main`, not built here), P (paper proof on `main`), I (imported result), W (reading
in this audit).

| Id | Conclusion and site | Obs. | Measure assumptions used in the proof | Weakest sufficient condition on `main` (layer) | Math. sufficiency | Physical justification | Class | Predictions vary? | Outstanding sourcing obligation | Stage 1 rec. |
|---|---|---|---|---|---|---|---|---|---|---|
| M1.a | Under the canonical law the emergent description is fixed by the partition alone (book ch01:79–83; M:84 "canonical choice"; M:58 default) | NONE | Lemma 3's selected law: counting on a finite carrier, maximal Shannon entropy among invariant laws (M:54; CM `counting_maximal_entropy`:227) | Finite: CM (K). Infinite full product: P-ED under (G1)–(G4), unique β_A (R1-INF Prop. 3, P); without (G3) unique only in d = 1 (Prop. 9) | Sufficient for the selection role in entropy-density form | None on `main`: R1-INF §7 "restates the uniform posit"; POSIT-MIN (iv) NOT FORCED | (c) c1 | Yes: M:58 (priors), P6 example 1 (invariant laws give different T) | Physical selection of the canonical law (R1) | None |
| M1.b | Reciprocity of visible transitions T_ij = T_θj,θi; detailed balance for T-even cells (SM:641–643, Thm 19; consumed at GR:70, P7B 6.1, Sub Thm 23 Stage 2(f)) | ACC | Counting hidden prior on a finite carrier (SM:643) | Flux reciprocity: normalized law invariant under φ and Θ; unweighted equality: equal root masses (P6 §2–3, P; `MeasuredReciprocity.reciprocal_flux`:90, `transition_reciprocity_of_equal_roots`:128, K) | Sufficient | None on `main` (P6: "physical selection … open under Q6") | (b) | Yes: P6 examples 1–2 | Θ-invariance and equal root masses of the physical law | None |
| M1.c | Custodial scalarity at the symmetric point: one common cone for the massless T₁, E, A₁ blocks (SM:334–336, Prop. 4b) | ACC | Counting law invariant under signed permutations of the six components; product of identical factors | The proof's extension clause: law equivariant under signed permutations (H-blind) (SM:334, P) | Sufficient | None on `main`; H-blind is a named condition | (b) | Not determined on `main` | H-blind for the physical law | None |
| M1.d | Canonical projection P_μ and the resummed kernel; dispersion cos ω = Â(k)/2 (SM:252–256, Lemma 1c) | ACC | (i): S_*μ = μ for the relabelling S; (iii): block form of U on the companion realization | Clause (i) for any μ preserved by S (SM:254, P); relation of (iii)'s coordinate projection to P_μ for a general invariant μ not traced | (i) sufficient; (iii) partly traced | None on `main` | (b) | Not determined on `main` | — | None |
| M2.a | No native autonomous production of readiness or held predictability in a fixed block, in law (PREP 1.3–1.4; consumed by PREP §6, #866 contract) | ACC | Invariance only | Any T-invariant probability on a measurable carrier (PREP 1.1–1.3, P [W]) | Sufficient | Whether nature's law is invariant at all is open (PREP §6: boundary law NEQ-T alternative) | (a) | No: holds for every law in 𝒜(φ) | Source of any non-stationary supply (PREP §6) | None |
| M2.b | μ-O: unique invariant law on the actual orbit; static budget log₂(\|S\|/ℓ); orbit capacity log₂ p (M:60; OA-1 r5:101; PREP 1.5(b)) | REC | Finite orbit; uniform law on it | Finite orbit only. Infinite: for unit α and β_A-typical points μ-O = μ-G, budget not supplied (R1-INF Prop. 7.1, P); on X_fin no invariant probability (R1-INF C1) | Sufficient on finite representatives only | None on `main` (PREP 1.5(b): "not a physically sourced preparation") | (c) c1 | Yes: finite orbit (positive budget) vs β_A (none) (PREP 1.5(b); R1-INF Prop. 7.1) | Decide whether #866's contract needs μ-O; L2 cannot supply the budget | Owner decision on scope narrowing (finite-representative statement); no construction |
| M2.c | μ-R / posit (iv): maximal entropy compatible with records; budget log₂(\|S\|/\|U\|); "knowing native under μ-R" (M:732 (iv); OA-1 r5:106–108; PREP 1.5(b′)) | NONE | Uniform law on a finite union of record-compatible orbits | Finite only. Infinite: collapses to μ-G (R1-INF Prop. 7.2, P); with reference β_A it is conditioning, a preparation (Prop. 7.3, P) | Sufficient on finite representatives only | None on `main` (posit (iv), "not derived") | (c) c1 | Yes: finite orbit union vs β_A (records exclude nothing at orbit level) | As M2.b | As M2.b |
| M2.d | Budget D(p₀,B‖ν_B) ≥ (N+1)(1 − h₂(ε)) for N held ε-predictable records (PREP 2.5–2.6, §6) | ACC | Reference u (finite) or ν invariant with ν_A = u_H ⊗ ν_{A∖H} (H-ν) | PREP 2.6 under H-ν and a finite cone (P [W]) | Sufficient | None on `main` (PREP 2.6: "a hypothesis to check for each model") | (b) | Not for the bound; its use to exclude an inflow endpoint needs a reference fixed in advance (REMAINDER §5) | H-ν source; O-INFLOW (REMAINDER §5, #866) | None here |
| M3.a | Doubly stochastic one-step and rooted maps (M:276–280; M:528) | ACC | Uniform law on a finite product carrier | (IP): φ preserves ν⊗ρ with ν uniform (M:280, P); window readouts on a full product carrier under P-ED (R1-INF Lemma 8, P) | Sufficient | None on `main`; observed unistochastic statistics are doubly stochastic (M:60) and are consistent with (IP) without implying it | (b) | Yes: counting law on the eventual image E (M:60) gives a non-doubly-stochastic matrix; R1-INF §9 C (non-invariant control) | (IP) for the physical law; non-coordinate readouts (R1-INF Lemma 8 scope) | Optional: Lemma 8 for general coarse-grainings (a property, not a law) |
| M3.b | Injectivity prong 1: a visibly differing hidden merge breaks double stochasticity, so is excluded where observed statistics are doubly stochastic (M:60; M:732 (iii); Sub:94; Meth:146) | ACC | As M3.a | As M3.a | Sufficient for the prong as scoped | As M3.a | (b) | As M3.a | As M3.a | None |
| M3.c | Non-permutation witness: doubly stochastic T non-permutation ⇒ nondegenerate row ⇒ hidden influence (C1) (M:441–443) | ACC | Common uniform hidden prior on a finite carrier | (IP) for double stochasticity (M:280); the second sentence ("fails P-divisibility by the return") is M3.d | Sufficient | As M3.a | (b) | As M3.a | As M3.a | None |
| M3.d | §2.3: non-permutation Γ_s ⇒ rooted family P-indivisible at recurrence scale (M:113–131) | REC (ACC only via an observed C4r) | Uniform prior on finite C_H; exact return Γ_N = I | (NR) with any normalized root-shared prior, no invariance (M:131, P); invariant μ with compact indicator-orbit closure (`ObservableRigidity.exists_pIndivisibleWithin_of_nonPermutation`:358, K) | Sufficient | None on `main`; under β_A for the selected update (NR) fails (NR-1 Prop. 2.3) | (b) | Yes, F1: β_A P-divisible at every horizon (NR-1 Thm. 3.3) vs μ_L P-indivisible [W] | A return source for the physical law (REMAINDER R2) | None from R1 |
| M3.e | Born-form identity T_ij = Born probabilities of Φ (M:288) | NONE | ρ_H = I/m | Any diagonal hidden prior [W]; status ledger records the fixed-Ĥ form for uniform, slice and weighted priors (M:740) | Sufficient | Not needed (representation) | (a) | No [W] | — | None |
| C1.a | Classical horizon temperature as a counting derivative: P(i) ∝ Ω(E − e_i), β = s′(E), T_cl (GR:58; GR:336) | RETRO | Uniform counting on a finite conserved shell (A1) | Decoupled: H4 law #⊗ν on the shell, any normalized deep ν, H5 proved (P7B Thm., 6.2–6.3, P). Coupled: none; no normalized invariant shell law for some coupled bijections (P7B 6.3 (ii), P) | Decoupled: sufficient with H1–H9. Coupled: not established | None on `main` (P7B 6.4; GR:88 "selection of the physical slope remains an additional condition") | (c) c1 | Yes: every real slope occurs under normalized invariant laws without H4 (P7B node 5) | Shell-law selection; coupled-case existence (P7B open Q1) | Recommended: scope the coupled existence question for the selected update (P7B Q1), noting conserved densities enter as free parameters (R1-INF Prop. 6) |
| C1.b | ħ = c³ε²/(4Gσ), i.e. ε/√σ = 2l_p (GR:78–80, :88; GR:552; SM:1586; book appendix-b:169) | RETRO (ħ measured; ε, σ not) | As C1.a, through β_E | As C1.a, with H-slope, H-frame, H-Hawking (P7B Thm. item 4, P) | As C1.a | As C1.a | (c) c1 | Yes, through β_E: a_* = τ_K/β_E (GR:80) with node 5's slopes | As C1.a | As C1.a |
| C1.c | Bekenstein–Hawking 1/4: σA/ε² = A/(4l_p²) (GR:316–318) | RETRO | As C1.b | As C1.b | As C1.a | As C1.a | (c) c1 | Yes [W]: a law with slope k·β_E gives ε² = 4kσl_p² and σA/ε² = A/(4k l_p²) | As C1.a | None beyond C1.a |
| C1.d | Entropy-displacement chain: a₀ = cH/6, baryonic Tully–Fisher, crossover radius (GR:466–500; table GR:542–551) | ACC | Inherits "T_dS requires H-count" (GR:470) | A law under which the shell rates have a log-rate slope (positive paired flux, P7B H9; P6 reciprocity) plus the KMS side (H-spectrum) [W] | Sufficient for the value [W]; the factor 1/6 is imported (GR:478) | None on `main` | (b) | No for the value [W]: a₀ contains c, H and the imported factor only | Coupling-map and heat-input conditions of GR:470 (not measure items) | None |
| C4.a | Boundary-only lemma (b) and gauge corollary under H-BD: Σ_j\|T_ij − T^(B)_ij\| ≤ 2t/τ_BD; \|C_D\| invisible at leading order (GR:114–138; book appendix-b:177–194, ch07:46, ch18:170; Meth:353) | GAUGE | Uniform hidden prior on finite C_H; H-BD's "fraction of d ∈ C_D" is counting; injectivity used to bound counts (GR:126) | H-BD part: none (L10; A1-05 P8-S: the counting proof "cannot simply be applied to an arbitrary exterior law"). Exact part within the cone: (D5) u_{B_n} ⊗ any normalized ν, no invariance (GR App. B, P) | Exact part sufficient; H-BD part only on finite carriers | None on `main`: τ_BD not fixed (GR:130); for the selected linear update H-BD with τ_BD > 2Δt fails at every cut with L ≠ 0 under counting (GR:128) | (b) | Yes, F2: GR:128's example, u_{V×B} ⊗ δ_d invariant [W], gives T(2Δt) = identity or bit flip; the uniform law gives every entry ½ | L10 with its fibrewise property (F2) | Low priority: GR:130 states no §8.5(b) result uses Steps 2–3 |
| C4.b | Effective finiteness: E3 bounds the observationally relevant \|C_V × C_B\| ≤ e^{S∂} under H-BD; leading-order transfer across H-BD-coupled extensions (Sub:54, :92, :268 (i)–(ii)) | GAUGE | As C4.a | As C4.a | As C4.a | As C4.a; Sub:268 (i) calls the E3 reading "the interpretive premise of A1" | (b) | As C4.a | As C4.a | None |
| M19.a | Equilibrium macrostate of (S,φ) ⇒ every local subsystem in local equilibrium (canonical typicality), hence observers only in the non-equilibrium phase (M:764; consumed at Sub:56 arrow of time, Sub:401, Str:718, ch04:178) | RETRO (observed non-equilibrium phase) | Normalized unitarily invariant measure on the unit sphere of a finite-dimensional energy subspace [31]; "typical" quantifier; finite (S,φ) (M:766) | None for the inference (L8 open). Narrowed form: local equilibrium (LE) supplied as a state per region (A1-05 P8-S). R1-INF §6: under P-ED, typicality only at substratum level (SLLN, ergodic theorem) | Not established beyond finite representatives | None on `main` (A1-05 P8-S: SOURCE GAP at the equilibrium state) | (c) c2 | Yes, F3: m_H (R1-INF Prop. 9 (b)) [W] | L8 or scope narrowing to (LE); physical source of the equilibrium state | Recommended: scope narrowing (separately authorized) before L8; F3 shows a homogeneity premise would be load-bearing for L8 |
| M19.b | Theorem bound τ_B ≤ τ_mix + O(ε) and the anti-Boltzmann-brain corollary, with local equilibrium stipulated (M:754–762; Comp:212) | NONE | Finite S for the exact Koopman setup and O(ε); local equilibrium by definition, not via M19.a (REMAINDER M20) | (IL) normalized φ-invariant μ with (EM) on μ-centred observables for the decay estimate (M:766; A1-05 P8-M, P) | Sufficient for the forward decay step only; τ_B transfer is a source gap independent of A1 (REMAINDER M18) | None on `main` | (b) | Not determined on `main` | (IL), (EM), uniform erosion | None |

## 3. Per-row notes

**M1 (Lemma 3 selection).** The item itself is the selection clause (M:54), not a conclusion; its
rows are the conclusions that consume it. On a finite carrier the kernel proves invariance and
maximal entropy of counting (`CanonicalMeasure.counting_invariant`:205,
`counting_maximal_entropy`:227) and that invariance alone does not select
(`invariance_does_not_select`:242). In infinite volume R1-INF gives E and N for every injective CA
on a full product (Lemma 1) and U only under (G3)+(G4) (Prop. 3); for the selected update in d ≥ 2
U fails without (G3) (Prop. 9 (b)). Control K1: M:84 states the reduced law as T(φ, 𝒫, μ_H) for
any specified prior, a statement that holds for every μ_H; only its "canonical choice" clause, and
the book's "determined by the partition alone" (ch01:79), need the selection, hence M1.a is (c)
and has no observational consequence (φ is not known to the observer). M1.b–M1.d use properties
of the law, not its selection. For M1.d the trace stops at SM Lemma 1c (iii): whether the
coordinate-block form used for the dispersion coincides with P_μ for an invariant μ that correlates
current and retarded fields is not settled by the text, and the row is marked partly traced.

**M2 (μ-G, μ-O, μ-R, posit (iv)).** μ-G is M1's law; its consumers are the M1 and M3 rows. M2.a
uses invariance only (PREP 1.1–1.3), so it holds for every law in 𝒜(φ). M2.b and M2.c report
budgets whose values are computed from the orbit structure the selection fixes; R1-INF Prop. 7
shows that in infinite volume, for unit α under β_A, both collapse to μ-G and the budgets are not
supplied. "Typical" there is relative to β_A itself (R1-INF Prop. 7.1). OA-1 r5:101 types μ-O as
derived on a finite orbit; that typing does not survive on an infinite carrier with β_A, since the
actual orbit has measure zero. M2.d's bound holds for any reference with H-ν; REMAINDER §5 records
that excluding the incoming-stream endpoint by a budget needs a reference fixed in advance, which is
a selection, but that exclusion is not a claimed result (O-INFLOW is not investigated).

**M3 (doubly stochastic corner and the uniform-prior consumers).** Main already carries (IP) at
M:280 as a hypothesis, not adopted, and R1-INF Lemma 8 proves L3 under it; the column-sum identity
uses invariance and uniformity of ν only. The variation witness is on `main`: M:60's eventual-image
example is a bijection of E with the counting law on E, invariant, with visible masses 2/5 and 3/5,
and its one-step matrix ((1/2, 1/2), (1/3, 2/3)) is not doubly stochastic. M3.e: for any diagonal
prior ρ_H = diag(ρ_k), P(j|i) = Σ_k ρ_k Σ_l |⟨j,l|U|i,k⟩|² = Σ_k ρ_k δ_{j, π_V φ(x_i, h_k)} [W],
which is the rooted map of that prior. M3.d [W, F1]: μ_L is invariant under F and under
translations (R1-INF Lemma 1 (a)) and is supported on the finite set Per_L, on which F has a finite
order N; the indicator orbit is then periodic, so its closure is compact, root masses are positive
for L larger than the window (R1-INF Lemma 1 (b)), and Γ_1 is a non-permutation for L beyond the
light cone (NR-1 Prop. 4.1, Thm. 3.3); `ObservableRigidity.exists_pIndivisibleWithin_of_nonPermutation`
then gives P-indivisibility within a finite horizon. Under β_A the same window is P-divisible at
every horizon (NR-1 Thm. 3.3). Before wraparound the two laws give the same rooted maps (NR-1
Prop. 4.1), so the difference is recurrence-scale only.

**C1 (H-count; coupled case scoped).** P7B node 5 is the variation witness: with a finite boundary
count, an infinite zero-energy deep sector, reversible energy-conserving dynamics and normalized
invariant laws, every real slope occurs. The slope, and through it T_cl, a_* and ε²/σ, is computed
from the shell weights, so C1.a–C1.c are (c) by test c1. The decoupled case (P7B Theorem, H1–H14)
is the comparison: its H4 fixes the boundary-shell weights by equal counting and leaves the deep
law free; P7B 6.4 records that its selection "is a posit of the same kind" as A1's uniform law. In
the coupled case the obstruction is earlier: P7B 6.3 (ii) has an energy-conserving deep-coupled
bijection of a countable shell with a single ℤ-orbit, on which no normalized invariant shell law
exists, and the selected update on an infinite carrier is not settled (P7B open Q1). R1-INF records
that P-ED is the β = 0 law and supplies no shell (R1-INF §6 table). C1.c [W]: if the classical slope
is k·β_E, GR:80 gives ħ = c³ε²/(4Gσk), so the calibration sets ε² = 4kσl_p² and σA/ε² = A/(4k l_p²).
C1.d [W, F4]: GR:474–480 use T_dS = ħH/(2πk_B) with measured ħ and the imported factor
(d−3)/((d−2)(d−1)); any law with a log-rate slope is calibrated to the same T_dS by the matching
itself, so the value of a₀ does not depend on which such law; GR:470's inherited H-count is not
contradicted, only found stronger than the value needs. This is a reading to be checked by the
reviewer, not a result.

**C4 (H-BD), traced.** Consumers found: GR:116–118 (lemma (b)), GR:122 (H-BD), GR:130 (the
emergent generator, as far as the data fix it, depends only on the local update; "Steps 2 and 3
are consistency checks … and no result of §8.5(b) uses them"), GR:132–138 (gauge corollary, H-BD
part), Sub:54, Sub:92 (A1's E3 reading), Sub:268 (i)–(ii), Meth:353, and the book mirrors
appendix-b:177–194, ch07:46, ch18:170 and their `FULL.md` copies. None of them reaches an `ACC`
consequence; every one concerns the invisibility of the deep sector's cardinality. Measure use in
the proof (GR:126) [W, F2]: elements of S_s have distinct deep components at step s by injectivity,
and at most a fraction Δt/τ_BD of C_D is bad for the reference path, so at most that many leave;
the step uses |f⁻¹(B)| ≤ |B| for an injection f, which a normalized ν satisfies only under a
fibrewise non-expansion of the deep dynamics. GR:128's example φ(v, b, d) = (v ⊕ b, b ⊕ d, d):
for fixed d the map acts on (v, b) as a bijection, so u_{V×B} ⊗ δ_d is invariant [W]; GR:128 gives
T(2Δt) = identity (d = 0) or the bit flip (d = 1) under these laws and every entry ½ under the
uniform law. The class is (b): the error bound and the gauge statement are structural and would
need a stated deep-law property, not a selection.

**M19 (canonical typicality, R5/L8).** The imported theorem quantifies over the normalized
unitarily invariant measure on a finite-dimensional shell; "every local subsystem" holds for
typical states with respect to that measure (A1-05 P8-S row "Local equilibrium/typicality").
F3 [W]: m_H is invariant under the selected update, has full centred entropy density and
u(0) = 0 almost surely, so maximal entropy in the entropy-density sense does not give an
equilibrium one-site marginal at the origin without the homogeneity premise (G3). M19.b is kept as
a control: the theorem's bound and the anti-Boltzmann-brain corollary use local equilibrium as a
stipulated state (REMAINDER M20) and need (IL) and (EM), not the global-to-local inference, so the
(c) of M19.a does not propagate to them; the arrow-of-time reading at Sub:56 does consume M19.a.

## 4. Controls (PREREG §7)

| Id | Result |
|---|---|
| K1 | M:84's general form T(φ, 𝒫, μ_H) holds for every μ_H; only the canonical-choice clause is (c) (M1.a). Passed |
| K2 | P-ED is cited only as a selection (M1.a, M3.a, M19.a); no row is (a) on P-ED alone. Passed |
| K3 | No finding is worded as probability or maximal entropy being undefined; the two non-existence statements cited are for a countable carrier (R1-INF C1) and a coupled countable shell (P7B 6.3 (ii)). Passed |
| K4 | M3.d records (NR) with root-shared normalized priors and no invariance. Passed |
| K5 | C4 has a consumer trace (§3 C4) before its class. Passed |
| K6 | Every (c) row names a witness: M1.a (M:58; P6 ex. 1), M2.b–c (R1-INF Prop. 7), C1.a–c (P7B node 5), M19.a (F3). Passed |
| K7 | (a) rows: M2.a uses invariance only, so it holds for every law in 𝒜(φ); M3.e holds for every diagonal hidden prior [W]. Passed |
| K8 | [W] items: F1–F4, M3.e, C1.c; each reads an existing proof or checks an example already on `main`. Passed |

**Counts by row.** (a): M2.a, M3.e — 2 rows. (b): M1.b, M1.c, M1.d, M2.d, M3.a, M3.b, M3.c, M3.d, C1.d,
C4.a, C4.b, M19.b — 12 rows. (c): M1.a, M2.b, M2.c, C1.a, C1.b, C1.c, M19.a — 7 rows. Total 21.

## 5. Coverage (PREREG §3)

**Searches at the pin.** Fixed-string hits: lines in `papers/*.md` + `book/*.md` | files in
`verification/lean*/` | Markdown files in `verification/`.

| Pattern | papers+book | Lean | verification |
|---|---|---|---|
| `maximal-entropy` | 10 | 2 | 45 |
| `maximal entropy` | 8 | 0 | 29 |
| `counting measure` | 14 | 5 | 67 |
| `uniform prior` | 21 | 6 | 56 |
| `uniform hidden prior` | 31 | 3 | 37 |
| `doubly stochastic` | 22 | 4 | 44 |
| `μ-O` / `μ-G` / `μ-R` | 0 / 0 / 0 | 1 / 0 / 0 | 50 / 53 / 46 |
| `H-count` | 84 | 0 | 50 |
| `H-BD` | 45 | 0 | 34 |
| `canonical typicality` | 4 | 0 | 20 |
| `local equilibrium` | 3 | 0 | 20 |
| `(IP)` / `(NR)` / `(IL)` | 5 / 13 / 2 | 0 | 6 / 9 / 6 |

**Traced.** Every papers/book hit was opened and assigned to a row, merged as a mirror, or set aside
as outside the six items (the uniform-prior consumers of REMAINDER rows M4–M9, M16, M18 and C3 other
than those in M3.d and C4.a). Lean hits read: `CanonicalMeasure.lean` (:205, :227, :242),
`ObservableRigidity.lean` (:160, :275, :358, :388), `MeasuredReciprocity.lean` (:90, :128, :311),
`Reciprocity.lean` (:129). The Lean hits for `doubly stochastic` in `CoherentLift`,
`ContinuousExtension` and `DilationChoice`, and for `uniform prior` in `RootedRecurrenceBridge`,
`SemigroupTransfer`, `PhysicalC4Discharge` and `PhysicalC4StorageReadback`, were read at the hit
lines only: they state matrix or finite-carrier facts and do not select a law; they are not traced
further. Verification records were read where §2 cites them; the remaining record hits were not
opened.

**Not traced.** `.tex`/PDF mirrors; book chapters beyond the mirrors named; companion papers outside
the hit lines; the reconstruction records that cite μ-O beyond OA-1 and PREP; REMAINDER rows outside
the six items. No Lean build, no computation. This is not an exhaustive census.

**Reused-record status.** REMAINDER and R1-INF were merged after an independent review and a
re-review (commits `5be38128`, `ae72e9d4`; merges `2be3cfad`, `e9008409`); their status paragraphs
still ask for a delta review, which their commit history shows was done. This audit reports that
mismatch and does not edit either record. Every result reused here keeps the layer its record
states (paper unless a kernel declaration is named).

## 6. Verification status and remediation (§A.46 item 4)

Evidence level: paper reading of existing records and manuscripts, with the [W] readings listed in
K8. Missing: an independent non-author review of this record at its exact head. Accountable Issue:
#1055 (with #1169 for the authorization and #1334 for the census). Resolution: a review recorded on
the guiding PR. The [W] readings F1–F4 are not results until reviewed; none is used as a premise of
another row's class except where the row says so (M3.d uses F1 only for "Predictions vary?").

## 7. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #1169 comment 7039208422 | Authorization, scope, classes, decision rule | Provenance; quoted in PREREG with author and time |
| #1169 comment 7037422124 | Goal link's priority record | Provenance |
| #1169, #1334, #1055, #866 | Accountability; O-INFLOW's programme | Provenance |
| Commits `5be38128`, `ae72e9d4`, `2be3cfad`, `e9008409` | Reused-record status | Support on `main`: all reachable from `main` at the pin |

## 8. What an independent reviewer must check

1. The class tests of PREREG §5 against each row, in particular the boundary case: M3.a–c (b) and
   C1.a–c (c), and that the R′ count (13) is computed correctly.
2. M1.a: that the "canonical choice" and the book's "determined by the partition alone" are the
   only consumers needing the selection, and that M:84's general form is measure-relative.
3. M1.d: whether SM Lemma 1c (iii) uses a property of μ beyond (i); the row is marked partly traced.
4. F1 (M3.d): μ_L's invariance, the finite order of F on Per_L, positivity of root masses, the
   non-permutation Γ_1 before wraparound, and the applicability of
   `exists_pIndivisibleWithin_of_nonPermutation`.
5. F2 (C4): the reading of GR:126's counting step and the invariance of u_{V×B} ⊗ δ_d in GR:128's
   example.
6. F3 (M19.a): that m_H is a fair classical analogue for the global-to-local step, and that the
   row does not claim a statement about Main's quantum canonical typicality.
7. F4 (C1.d) and the C1.c computation: that the calibration absorbs the slope into ε²/σ, and that
   a₀ contains no law-dependent quantity at measured ħ and H.
8. C4's consumer list, and GR:130's statement that no §8.5(b) result uses Steps 2–3.
9. That no row is worded as probability or maximal entropy being undefined (K3), and that no row
   reports mathematical sufficiency as physical justification.
10. That no row constructs a new law or proposes a replacement, and that no manuscript, Lean or
    registry file is changed.
