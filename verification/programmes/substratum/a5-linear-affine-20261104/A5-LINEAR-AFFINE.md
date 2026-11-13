# A5-LINEAR-AFFINE — linear vs affine microscopic dynamics (#1049)

**Status: WIP / UNVERIFIED. Paper-only.** Authorized by the owner on 2026-11-04, #1049
comment 6622105211. The authorization covers source reading, paper derivation, literature
examination, documented assumptions and independent review. It does not cover computation, Lean,
adopting a premise, promoting a claim, a merge or publication. No code, enumeration or Lean was
written or run. Every algebraic step below was done by hand.

**Revision.** Revised after independent reviews of `4e096997` (ACCEPT WITH CHANGES) and `fc5cf7e9` (ACCEPT WITH CHANGES; its one should-fix and three nits applied). The review texts are posted on #1083 comment 6718252075.

**Base.** `origin/main` at `1609dc440f5a12d05b750f6d894bb91d09a099a3`. Line numbers `File:N` refer to
`papers/File.md` at that commit.

**What this document is.** A scoped proposal with decision criteria (§1), a dependency inventory
(§2), and a depth-first paper investigation of #1049's question (§3), with results (§4), proposals
(§5), open items (§6) and a computation proposal for separate authorization (§7).

**What it is not.** It is not a verification record, not a native round, and not a manuscript
correction. It adopts no premise and changes no status. The [D] items are unreviewed.

**Support labels.**
- [K] Kernel-checked Lean on `main`, cited by module and declaration.
- [P] A reviewed paper or record result, cited by location.
- [D] A derivation in this document, unreviewed.
- [L] Literature from memory, not re-read.
- [O] An owner decision, cited.

**Notation.**
- The torus Λ has N sites, the alphabet is ℤ/q, and the per-site value is x_i. Where the
  K-component site variable matters (Stage 2(d), N9), the site alphabet is V_K = (ℤ/q)^K, or its
  lift.
- The two-slice configuration group is G = (ℤ/q)^Λ × (ℤ/q)^Λ ∋ z = (x(t−1), x(t)).
- A second-order rule is x(t+1) = F(x(t)) − x(t−1) (Main:726 item (xiii); kernel
  `SecondOrderLayer.Rule`, `SecondOrderDrive.ruleDynamics`).
- An **affine** rule has F(x) = Ax + b, with A additive and b ∈ (ℤ/q)^Λ. Its phase-space map is
  Φ = τ_β ∘ L, where L(u, v) = (v, Av − u), β = (0, b) and τ_β is translation by β. The map L is the
  **linear part**, and A5 is the case b = 0 (kernel `SubstratumInterfaceAudit.A5`).
- The **zero orbit** is p(t) := Φ^t(0).
- W := ℤ[L]β is the smallest L-invariant subgroup of G that contains β.
- C := {(a𝟙, c𝟙) : a, c ∈ ℤ/q} is the **uniform two-slice subgroup**, with |C| = q². It is
  L-invariant whenever A commutes with translations.
- When A commutes with translations, A𝟙 = κ𝟙, and κ is the coefficient sum. For the nearest-neighbour
  rule α Σ_{j∼i} x_j, κ = 2dα.
- **Shift convention.** A uniform relabelling means y = x + c𝟙, applied to both slices.
- **S1** is the witness of SM:240 (entered by H2, #1050): N = 4, q = 5, F_i(x) = x_{i−1} + x_{i+1} + 1,
  so κ = 2 and b = 𝟙. For S1, β = (0, 𝟙) and Lβ = (𝟙, 2𝟙) are independent, so W = C.

***

## §1 Scoped proposal and decision criteria

This section was written before §2–§4. The drafting session had already read the sources and done
the S1 arithmetic, so this is a scoping statement, not a §A.39 preregistration.

### 1.1 Order of pursuit

- **B0 — structure of the affine class.** This is groundwork that both outcomes need: when an affine
  rule can be carried to a linear one, and by which transformations.
- **B1 — criterion 1, physical selection.** Candidates are taken depth-first, each closed by an
  explicit paper check. The order is: the corpus's own principles first, then standard physical
  principles. A successful selector would make B2 unnecessary, so B1 runs first.
- **B2 — criterion 2, observable equivalence.** This runs whatever B1 finds.
- **B3 — criterion 3, scoped negative.** It is assembled from the failed B1 nodes and the limits of
  B2.

### 1.2 Results to be preserved, which serve as controls (§A.29)

A result of this document fails if it contradicts any of the following.

| # | Control | Support |
|---|---|---|
| C1 | Base-point-independent first differences imply an affine rule (the affine lemma). | [P] Substratum:274, SM:240 |
| C2 | S1 is reversible, commutes with translations, is center-free and affine, has no fixed point, and no time-independent relabelling makes it linear. | [P] SM:240. #1050's exact-head review (all 5^8 states) is provenance. |
| C3 | Positive control: for a uniform offset on a ring of N sites with A − 2I = Δ (κ = 2, as for S1), a fixed point exists for every odd prime q ∣ N. | [D] B0.3(e); an internal check, not an independent control |
| C4 | The finite-horizon quantum representation and the characterization theorem do not use A5. | [P] Main:728 status ledger; H-D `A5S-1b` (no OI→QM kernel module consumes A5) |
| C5 | `driveQ` is a continuous path of `*`-automorphisms for every `Rule`, with no additivity assumed. | [K] `OIBridge/SecondOrderDrive.lean`, `driveQ_isContinuousPath`, `driveQ_one_eq_heisQ`; `Rule` at `SecondOrderLayer.lean:198` |
| C6 | Additive rules fix 0 and leave their ensemble undetermined. Additive rules admit no advective closure on additive coarse variables. | [K] `StochasticInterface.phi_fixes_zero`, `stochastic_interface_gap`; `HydroSourceAudit.coarseCloses_nsmul` |
| C7 | A5 remains an explicit posit of the selected model, stronger than the affine restriction. | [P] Main:726 item (vii); Substratum:100, :104; #1043 |
| C8 | The q-size freedom does not entail amplitude-scale gauge. | [P] Substratum:274; H-D-SR `SR-3` (the corpus does not adjudicate between the forms) |

### 1.3 Decision rules (fixed before the derivations)

**Criterion 1 succeeds** only if a candidate principle P satisfies all of the following:
- (a) P is stated precisely.
- (b) P is justified without presupposing additivity, a distinguished zero, or the conclusion.
- (c) P together with named hypotheses implies b = 0, proved on paper.
- (d) P excludes S1.
- (e) P has at least one consequence beyond excluding S1, checkable against a result not used to
  build P.
- (f) P preserves C1–C8.
- (g) P has no adjustable variant that fits either outcome.

A candidate that fails (b), (c), (e) or (g) is recorded as a scoped failure, with the failing clause
named.

**Criterion 2 succeeds** only if a theorem states all of the following:
- the class of systems;
- the observer interface: the visible/hidden split, the preparations, the readouts and instruments,
  the admissible transformations and the time domain;
- the named observables that agree;
- a proof;
- a countercontrol: a readout outside the class that does distinguish, so the theorem is not
  vacuous.

An equivalence that needs a transformation whose physical admissibility the corpus does not
establish is recorded as **coordinate equivalence only**.

**Criterion 3** is always produced. Each negative is stated for the construction actually tested.
No finite case is generalized.

**Skepticism rule (§A.31).** Every branch favourable to the framework gets an explicit
pressure-test paragraph (§3.3.8, and the N6 and N9 nodes).

***

## §2 Where A5 enters — dependency inventory

The "Under affine dynamics" column assumes a **uniform offset**. That is what exact translation
commutation gives (Corollary B0.3(a)). A4 "up to gauge" (Main:726 (xi)) can allow non-uniform
offsets, which are flagged where they matter.

| # | Site | Use of linearity | Under affine dynamics | Support |
|---|---|---|---|---|
| D1 | SM:224 Lemma; Substratum:159 Stage 2(b) | the form α Σ_{j∼i} x_j | The same proof without the additivity step gives α Σ x_j + b. Form plus one constant. | [P] proof text; [D] |
| D2 | SM:230–232, dispersion and lift | the linear part only | The linear part is unchanged. The offset sources only the uniform sector C: on G/C both rules induce the same map. In the lift, or with gcd(N, q) = 1, this is the k = 0 mode (Proposition 2.5). | [D] |
| D3 | Substratum:163 Stage 2(d); SM:344, §4.6 | amplitude-scale gauge (common phase); the stabilizer is computed for the linear part | **Candidate hidden use of b = 0** (see the paragraph after this table). For a uniform, cubic-invariant b ≠ 0 on the lift, the stabilizer of the affine rule among constant linear unitaries (the (A-lin) reading of `A5-Q4-STAGE2D.md`) is U(3)×U(2), and the singlet U(1) is lost. Open (Q4). | [P] text; [D] reviewer finding, checked by reading |
| D4 | SM:811, §6 map | exponential of **link differences** φ(n+ê) − φ(n) | A uniform offset cancels from differences, so the map is offset-blind. | [P] text; [D] |
| D5 | SM:811, energy-shell measure; Main:726 (v) | quadratic invariant Q of the linear rule | Q is not conserved. Q′ = Q − b(S_t + S_{t−1}) is conserved, where S = Σ_i x_i (Proposition B3.3). The shell measures differ. | [D] |
| D6 | Main:726 (v), cycle splitting | linear rule | #cycles(Φ) ≥ #cycles(L)/\|W\| (Proposition B3.2). Exponential counts transfer. The shell-specific statement is not transferred. | [D] |
| D7 | SM:92, Theorem A.1 (period qL) | linear wave map | Not transferred, and not examined. | — |
| D8 | Main §3.2/§3.4 continuous path | none | Holds for every `Rule`. | [K] C5 |
| D9 | Main §3.4 representation and characterization | none | Holds, universal over finite visible laws. | [P] C4 |
| D10 | GR §3–§6 | none stated | "Not on … A2–A5" (GR:679). GR:679 also states that a formal proof "has not been written out", so this is support at the level of a derivation sketch. | [P] sketch |
| D11 | Structure §6.5, BFSS | BFSS is non-affine | Unaffected by the linear/affine distinction. | [P] Structure:307 |
| D12 | `StochasticInterface` gap | A5 as hypothesis | The kernel proof needs a fixed point. Its conclusion extends to uniform-offset affine rules by another route (Proposition B3.1). | [K] for A5; [D] extension |
| D13 | `HydroSourceAudit` advection gate | A5 as hypothesis | Extends: an affine closure is degree ≤ 1 in n (Proposition B3.4). | [K] for A5; [D] extension |
| D14 | `A6Instantiation`, `BackgroundIndependence` (`linkF`) | link couplings typed `V →+ V` | Additivity is built into the carrier's type. See node N9. | [K] definitions |
| D15 | SM:1416, Layer 2 candidate classes | "linear dynamics (A5)" | Conditional on A5 as stated. | [P] |
| D16 | Theorem 23 (Substratum §3.5) | through D1 and D3 | Inherits D1 (form plus a constant). Its gauge-group output inherits D3's candidate: if the stabilizer is taken of the affine rule, the singlet-block U(1) (which Substratum:163 identifies as hypercharge) is lost for b ≠ 0; whether another U(1) can serve is not examined. Open (Q4). | [P]; [D] |

**D3 in detail (candidate, not resolved) [D].** The argument has four steps.
- **(i) b lies in the A₁ block.** Exact translation commutation makes b uniform (B0.3(a)). Isotropy
  (E4) makes b a cubic-fixed vector of V_K. Under 6 = T₁ ⊕ E ⊕ A₁ (SM:374, Theorem 7; Substratum:163),
  the cubic-fixed vectors are the A₁ block. So b ∈ V_1.
- **(ii) A commuting unitary must fix b.** On the lift, take a unitary g acting identically at every
  site. It commutes with x ↦ Ax + b iff gA = Ag and gb = b.
- **(iii) The affine stabilizer loses the singlet U(1).** The stabilizer of the linear part is
  U(3)×U(2)×U(1) (Substratum:163). The singlet factor must fix b ≠ 0, so the stabilizer of the
  affine rule is U(3)×U(2).
- **(iv) The common-phase step has nothing to remove.** The step "amplitude-scale invariance
  removes only the common overall phase" then acts as a relabelling b ↦ e^{iθ}b, not as a symmetry
  of the affine rule.

Stage 2(d) computes the stabilizer of the linear part only. Whether that choice is itself a use of
A5, or is justified otherwise (for example, if the stabilizer is meant to be that of the coupling
operator, not the rule), is not settled here. The same candidate reaches SM:344 through D3.

H-D's U1–U8 (`round-h-d-a5-status-adjudication/result.md`, `A5S-2a`) are D1, D3, D4 and D16 above.
U8 (SM §6) is D4 and D5: H-D lists the map-uniqueness, and this inventory adds that the map reads
differences. The kernel consumer list is H-D's `A5S-1b`, closed at four modules [P].

***

## §3 Work, depth-first

### 3.0 S1 recomputed by hand

- S1 commutes with translations and has no self-term.
- A fixed point needs equal slices x with 2x_i − x_{i−1} − x_{i+1} = 1 at every site. Summing over
  the ring gives 0 ≡ 4 (mod 5), so there is no fixed point. This agrees with C2.
- Zero orbit: x(−1) = x(0) = 0 gives uniform values g(t)𝟙 with g = 0, 0, 1, 3, 1, 0, 0, 1, … The
  period is 5.

### 3.1 B0 — structure of the affine class

**Lemma B0.1 (orbit decomposition) [D].** For every affine bijection Φ = τ_β ∘ L of a finite abelian
group G, and every t ≥ 0,

  Φ^t(z) = L^t z + p(t),  p(t) = Φ^t(0) ∈ W.

*Proof.* Induction: Φ^{t+1}(z) = L(L^t z + p(t)) + β = L^{t+1} z + p(t+1). W contains β, is
L-invariant, and contains p(0) = 0. ∎

This is the finite-group form of "general solution = homogeneous solution + particular solution"
for inhomogeneous linear recurrences [L: Lidl–Niederreiter, *Finite Fields*, linear recurring
sequences]. The time-dependent translation z ↦ z − p(t) therefore carries every trajectory of Φ to a
trajectory of L, for every affine rule, always.

**Proposition B0.2 (time-independent linearization) [D].** For Φ = τ_β ∘ L, the following are
equivalent:
- (i) Φ is conjugate, by some bijection of G, to an additive automorphism;
- (ii) Φ has a fixed point;
- (iii) β ∈ Im(I − L);
- (iv) Φ = τ_c ∘ L ∘ τ_{−c} for some c ∈ G.

*Proof.*
- (i)⇒(ii): an additive map fixes 0, and conjugation carries fixed points to fixed points.
- (ii)⇒(iii): Lc + β = c gives β = (I − L)c.
- (iii)⇒(iv): τ_c L τ_{−c}(z) = Lz + (I − L)c.
- (iv)⇒(i): immediate. ∎

This extends C2's fixed-point argument from S1 to the whole affine class. It also shows that, on a
finite carrier, *no* time-independent bijection linearizes an affine rule without a fixed point,
whether site-dependent or nonlinear.

**Corollary B0.3 (second-order, translation-commuting rules) [D].**
- **(a) The offset is uniform.** If F = A + b commutes with every lattice translation T, then
  F(0) = T F(0), so b = b·𝟙 is uniform, and AT = TA.
- **(b) The cokernel.** (I − L)(u, v) = (u − v, u + v − Av). Solving (I − L)(u, v) = β = (0, b𝟙)
  forces u = v and (2I − A)v = b𝟙. So the obstruction lies in Coker(A − 2I). It is trivial whenever
  A − 2I is invertible, that is, whenever the linear rule has no nonzero static solution. Over a
  prime field it is nontrivial only at **zero modes** of A − 2I.
- **(c) Uniform shifts.** The uniform relabelling y = x + c𝟙 carries the offset b to
  b + (2 − κ)c. The offset is removable by a uniform time-independent shift iff b ∈ (κ − 2)·ℤ/q.
  The obstruction class is b mod gcd(κ − 2, q).
- **(d) S1.** κ = 2 and A − 2I is the ring Laplacian Δ. Over 𝔽₅ on four sites, Ker Δ is the
  constants and Im Δ = {Σ v_i = 0}, using the 4th root of unity 2 ∈ 𝔽₅: the symbol values are
  0, 3, 1, 3. Since Σ 𝟙 = 4 ≢ 0, β ∉ Im(I − L). This **reproduces C2**.
- **(e) Positive control.** For an odd prime q ∣ N, Ker Δ = span{𝟙, (i)_i}. Then 𝟙 ⊥ both, since
  N ≡ 0 and N(N−1)/2 ≡ 0, so 𝟙 ∈ Im Δ and a fixed point exists. This derivation **is the support
  for C3**. The fixed point has a non-uniform profile, and by (c) no uniform shift removes b ≠ 0 here (κ = 2).
- **(f) A gapped example, for a cheap check.** Take x_i(t+1) = 2(x_{i−1} + x_{i+1}) + 1 − x_i(t−1)
  over 𝔽₅, so κ = 4. The uniform state v = 2 on both slices is fixed:
  2·(2 + 2) + 1 − 2 = 7 ≡ 2. The rule is uniform-shift-conjugate to linear.

**Reading.** The S1 phenomenon is **resonant forcing of a zero mode**. A uniform source cannot be
absorbed into a static background when the mode it drives is static under the linear rule. In S1 that
mode is the gapless k = 0 mode, κ = 2. This is the lattice analogue of a tadpole term J φ, which a
field shift removes iff the mode is massive [L: standard QFT]. For odd q, κ ≡ 2 is exactly the
normalization α ≡ 1/d (κ = 2dα) that SM:230–232 places at observer level. At q = 2, κ = 2dα ≡ 0 ≡ 2
for every α.

**Proposition B0.4 (A5 under the declared shift gauge) [D].** SM:96 states that rescalings and shifts
x ↦ x + c "preserve the emergent observables". Substratum:270 states that they "leave every
observable unchanged". With the convention of B0.3(c), the uniform relabelling y = x + c𝟙 carries the
linear rule to y(t+1) = Ay(t) − y(t−1) + (2 − κ)c𝟙: in two-slice form, Lz + (I − L)(c𝟙, c𝟙) with
(I − L)(c𝟙, c𝟙) = (0, (2 − κ)c𝟙). Hence:
- If κ ≢ 2 (mod q), the corpus's declared gauge carries the linear rule to affine rules. Then
  "linear" (A5) is a gauge-fixing condition, not a gauge-invariant property of the rule.
- Rescalings x ↦ λx commute with L, and carry b to λb.
- A5 is invariant under the declared amplitude-scale group iff κ ≡ 2 (mod q).

This bears on how C7 is read. It does not contradict C7.

### 3.2 B1 — candidate selection principles (criterion 1)

Each node gives: the statement; the justification; the implication, under named hypotheses; the S1
check; the independent consequence; and the verdict.

**N1 — Superposition of states.** *Statement:* sums of trajectories are trajectories. *Implication:*
this is A5 restated. *Verdict:* fails (b) — it presupposes additivity and a distinguished zero. Under
B0.4 it is not shift-gauge-invariant when κ ≢ 2. **Fail (b), (e).**

**N2 — Superposition of perturbations (base-point independence).** *Implication:* affine, by C1.
*S1:* satisfies it, since the differences of trajectories satisfy L (B0.1). **Not a selector.** [P]

**N3 — Linearity of the emergent quantum theory.** The Koopman/permutation operator U_Φ is linear and
unitary for every bijection, and SM Theorem 1a is stated for the Koopman operator of an arbitrary
bijection (SM:242). *S1:* satisfies it. **Not a selector.** [D, immediate]

**N4 — A conserved quadratic energy (Main:726 (v); SM §4.2).** *Check [D]:* for symmetric,
translation-commuting A, the linear rule conserves
Q(t) = x_t·x_t − x_t·A x_{t−1} + x_{t−1}·x_{t−1}. For F = A + b𝟙 one finds
Q(t+1) = Q(t) + b(S_{t+1} − S_{t−1}). So Q′ = Q − b(S_t + S_{t−1}) is conserved, which is a
degree-≤2 invariant. Asking for a *homogeneous* quadratic invariant presupposes the origin. *S1:*
satisfies the gauge-covariant form. **Not a selector.**

**N5 — Time reversal.** Every second-order rule is time-reversal symmetric: y(t) := x(−t) satisfies
y(t+1) + y(t−1) = F(y(t)). *S1:* satisfies it. **Not a selector.** [D]

**N6 — Existence of a vacuum (stationary configuration).** *Statement:* Φ has a fixed point.
*Implication:* by B0.2 this is equivalent to Φ being translation-conjugate to L. It is not
equivalent to b = 0. *S1:* excluded. *Pressure test:*
- (1) It selects "linear up to a translation of G". That is "linear" only if site-dependent
  translations are gauge, which the corpus does not state; SM:96 names one uniform shift.
- (2) Justification: the substratum is a permutation, and no corpus principle requires a fixed
  point rather than a short cycle. S1 has a uniform period-5 orbit that would serve as a "vacuum
  cycle" equally well. The variant "has a period-k orbit" fits other outcomes, which fails (g).
- (3) Independent consequence: a fixed point implies an undetermined ensemble (C6). But S1's
  ensemble is also undetermined (B3.1), so this consequence does not discriminate.

**Fail (b), (c), (e), (g).**

**N7 — Field-reflection symmetry.** *Statement:* Φ commutes with an involution z ↦ 2c − z.
*Implication [D]:* this holds iff 2(β − (I − L)c) = 0. For odd q that is exactly "c is a fixed
point", so N7 ⇔ N6. For q = 2 the involution is the identity and N7 is vacuous. *S1:* excluded,
because 2β ≠ 0 and S1 has no fixed point. **Reduces to N6, and is vacuous at q = 2.**

**N8 — Rescaling as a dynamical symmetry ("strong" amplitude-scale reading).** *Statement:* Φ
commutes with x ↦ λx for every unit λ. *Implication [D]:* (1 − λ)β = 0 for all units. For odd q,
λ = −1 gives b = 0, so **this selects exact linearity among affine rules at odd q.** *S1:* excluded.
*Pressure test:*
- (1) It does not force b = 0 at any even q. The units are odd, so 1 − λ is even, and b = q/2
  satisfies (1 − λ)b = 0 for every unit. At q = 2 it is vacuous: the only unit is 1, and the
  complement rule (b = 1) is allowed. q = 2 is the instance displayed in Main §3.2 (Main:726 (xiii)).
- (2) Rescaling about 0 presupposes the origin. Its shift-covariant form, rescaling about c, gives
  (1 − λ)(Lc + β − c) = 0, which for odd q is N6.
- (3) The corpus reads rescaling as a redundancy of description (a relabelling, SM:96, Substratum:270),
  and relabelling carries b to λb rather than requiring b = λb. Adopting the symmetry reading is a new
  premise.
- (4) No consequence beyond b = 0 was found.

**Fail (b), (e). Fails to force b = 0 at every even q, and is vacuous at q = 2.**

**N8′ — Shift as a dynamical symmetry (by-product).** Φ commutes with uniform shifts iff κ ≡ 2,
independent of b [D]: L(c𝟙, c𝟙) = (c𝟙, (κ − 1)c𝟙). S1 satisfies it. **Not a selector.** It is
precisely the condition under which a uniform offset cannot be removed by a static shift. Recorded as
an elaboration:
- For odd q, a substratum shift symmetry would force κ ≡ 2, hence dα ≡ 1. That needs
  gcd(d, q) = 1, the arithmetic SM:92 records for α = 1/d.
- For even q > 2, the condition is κ ≡ 2 ⇔ dα ≡ 1 (mod q/2).
- At q = 2, κ ≡ 2 holds for every α and imposes nothing on α.

**N9 — Background independence (A6), as extended here to an offset.** *Statement:* covariance under
site-dependent g : Λ → AddAut(V), with the link coupling transported (Main:726 (xii); kernel
`BackgroundIndependence.A6Cov`). `A6Cov` (BackgroundIndependence.lean:131) is defined on `linkF`
alone, with link couplings typed `V →+ V`, and says nothing about offsets. So any verdict below is
about **an extension chosen here**, not about A6 as formalized. Three natural extensions were
examined:
- **(E1) Additive links, untransported offset.** For F = `linkF` + b with b not transported,
  covariance requires g_i b_i = b_i for all g:
  - **K ≥ 2, any q:** a transvection moves any b ≠ 0, so b = 0, including at q = 2.
  - **K = 1, odd q:** λ = −1 gives b = 0.
  - **K = 1, q even > 2:** b ∈ {0, q/2}.
  - **K = 1, q = 2:** AddAut(ℤ/2) is trivial, so b is unconstrained.
  - *S1* (K = 1, q = 5) is excluded.
- **(E2) Affine link maps.** If link couplings may be affine maps V → V, the offset moves into the
  links. S1 is F_i = (x_{i−1} + 3) + (x_{i+1} + 3) over ℤ/5. Transport g_i ∘ M ∘ g_j⁻¹ keeps them
  affine, and covariance holds identically, as `a6cov_all` (D3-a) does for additive links. This
  restricts nothing.
- **(E3) Transported site offset.** If b_i ↦ g_i b_i is transported with the configuration,
  covariance again holds identically. This restricts nothing.

*Pressure test.*
- Only E1 selects b = 0, and E1 does so only given additive link couplings. That is additivity
  relocated to the links, not derived.
- The local group in the kernel is AddAut(V), with no translations, while the amplitude gauge
  includes shifts (SM:96, Substratum:270). Whether the local group is linear or affine is the
  linear/affine question in another form.

**Fail (b): relocation, not derivation, scoped to extensions E1–E3.** This is recorded as an
assumption-watch marker (§6).

**N10 — Alphabet-size independence (Structure:219, :301; SM §2.7).** *Statement:* systems differing
only in q have the same emergent observables. *Check [D]:* by B0.3(c) the removability class
b mod gcd(κ − 2, q) is q-dependent when κ ≠ 2 as an integer, which suggests the hypothesis might
exclude some integer-coefficient affine families. *Pressure test:*
- The hypothesis is "not proved for every observable" and needs a cross-q correspondence that is
  "not constructed" (SM:94).
- At the one level checkable by hand, cycle type, it excludes the linear rule too, since the linear
  ring period is qL (Theorem A.1, SM:92).

**Undetermined. Its premise is open and its correspondence unconstructed. At cycle-type level it
overshoots.**

**N11 — Recurrence (Axiom 2), maximal-entropy measure (Main:726 (iv)), isotropy (E4).** Exact return
of every state is automatic for any bijection of a finite set; Axiom 2 asserts only that
differentiation recurs. The uniform measure on G is invariant under both Φ and L.
A uniform b𝟙 is cubic-invariant. **Not selectors.** [D, immediate]

**Criterion 1 is not reached.** No candidate meets (b), (c), (e) and (g) together. The two that
select b = 0 relocate the assumption:
- N8, at odd q only, relocates it to a distinguished origin;
- N9/E1 relocates it to additive link transports.

All the other candidates either admit S1 or reduce to N6.

### 3.3 B2 — observable equivalence (criterion 2)

**3.3.1 Interface.**
- **Carrier.** G = G_V × G_H, a site factorization (Main:726 (viii)), with two slices on each
  visible site. Hilbert space ℓ²(G) = ℓ²(G_V) ⊗ ℓ²(G_H). The unitary is U_Φ|z⟩ = |Φz⟩. T(w) is the
  translation unitary, with T(w) = T_V(w_V) ⊗ T_H(w_H).
- **Preparations.** Every density matrix ρ on ℓ²(G). This includes Main §1.4's fixed visible state
  with a uniform hidden prior, and Substratum §4's ρ_V ⊗ ω_H with ω_H arbitrary.
- **Readouts and instruments.** Instruments on V, possibly at several times, with outcome
  probabilities given by the usual sequential formula. Readout classes, for an L-invariant subgroup
  Y ⊆ G:
  - **𝒜_Y**, the commutant of {T_V(y_V) : y ∈ Y} in B(ℓ²(G_V)), called *relational*. Two cases
    matter:
    - **𝒜_W** (Y = W), the largest class for a given rule.
    - **𝒜_C** (Y = C), which does not depend on b. Every uniform-offset rule with linear part L has
      β ∈ C, so W ⊆ C and 𝒜_C ⊆ 𝒜_W.
  - **The diagonal (configuration) readouts in 𝒜_C** are the functions of
    (x_V(t−1) mod a constant, x_V(t) mod a constant), with **independent** constants on the two
    slices.
    - Readouts of the current slice x_V(t) modulo a constant are included.
    - The velocity x_V(t) − x_V(t−1) is not included: it is invariant under a common shift (c, c) but
      not under (c, 0). Differences of velocities between sites are included.
    - For S1, W = C, so 𝒜_W = 𝒜_C. Hence 𝒜_W is not "every function modulo a common constant"
      for S1.
  - **Non-diagonal elements.** As a commutant, 𝒜_Y also contains non-diagonal operators: the
    T_V(w) themselves and the Fourier (character) projectors of G_V.
  - **𝒜_abs**, all operators, including Main §1.4's absolute configuration readout.
- **Time domain.** All t ∈ ℕ. There is no horizon restriction.
- **Admissible transformations.** None in Theorem 2.1, which uses the identity identification of
  labels. Theorem 2.2 names the transformation it needs.

**Theorem 2.1 (relational readouts) [D].**
*Hypotheses:*
- Φ = τ_β ∘ L on G = G_V × G_H;
- Y is an L-invariant subgroup with β ∈ Y (for example Y = W; or Y = C for every uniform-offset
  rule with linear part L, whatever b is);
- ρ is any initial state;
- 𝓘_1, …, 𝓘_n are instruments on V whose Kraus operators lie in 𝒜_Y;
- the instruments act at times t_1 < … < t_n.

*Conclusion:* the joint outcome distribution under Φ equals that under L.

*Proof.*
1. By B0.1, U_Φ^t = T(p(t)) U_L^t with p(t) ∈ W ⊆ Y, and U_L T(w) = T(Lw) U_L.
2. Claim, by induction on j: the post-instrument state under Φ is Ad T(p(t_j)) of the state under L.
3. Step: evolving by Δ gives Ad(T(p(Δ)) U_L^Δ T(p(t_j))) = Ad T(p(Δ) + L^Δ p(t_j)) ∘ Ad U_L^Δ, and
   p(Δ) + L^Δ p(t_j) = p(t_j + Δ) ∈ Y. Instruments with Kraus operators in 𝒜_Y commute with
   Ad T_V(y_V), and act trivially on H.
4. The final trace is invariant under unitary conjugation. ∎

**Theorem 2.2 (absolute readouts) [D].** For arbitrary instruments, the joint distribution under Φ
with instruments 𝓘_j equals that under L with instruments Ad T_V(p_V(t_j))⁻¹ ∘ 𝓘_j ∘ Ad T_V(p_V(t_j)).
In particular:
- **Coherent channels.** Φ^Φ_t(ρ_V) = Ad T_V(p_V(t)) ∘ Φ^L_t(ρ_V) for ρ_V ⊗ ω_H, with ω_H arbitrary,
  because the partial trace over H removes T_H.
- **Rooted transition probabilities.** T^Φ_{ij}(t) = T^L_{i, j − p_V(t)}(t). The time-0 labels agree,
  since p(0) = 0.

**Corollary 2.3 [D].** Under 𝒜_abs, every functional of the multi-time configuration law that is
invariant under a bijection of the visible alphabet applied separately at each time agrees for Φ and
L. This covers:
- joint and conditional entropies;
- I(X_{<k}; X_{k+1} | X_k), which is the readback quantity of Main §2.3;
- the Markov property;
- P-divisibility, since Γ^Φ(t,s) = Π(t) Γ^L(t,s) Π(s)⁻¹ with Π permutation matrices;
- CP-divisibility of the channel family.

For the stochastic–quantum representation, Θ^Φ(t) = Π(t) Θ^L(t): the finite-horizon representations
differ by a time-dependent permutation unitary. C4 is preserved.

**Proposition 2.4 (spectrum) [D].**
- **On the relational algebra.** Functions on G invariant under W form a subspace invariant under
  both U_Φ and U_L, and on it U_Φ = U_L = U_{L̄}, because f(Lz + β) = f(Lz). The Koopman spectra
  coincide on the W-invariant observable algebra.
- **On the full algebra.** tr U_Φ = #Fix(Φ) = 0 for S1, while tr U_L ≥ 1. The full Koopman spectra
  (equivalently the cycle types) differ for S1.
- **Linear-part spectrum.** The dispersion symbol of L is untouched.

**Proposition 2.5 (effective wave equation) [D].**
- **Over ℤ/q, in general.** On G/C, both rules induce the same linear map L̄ (Proposition 2.4,
  with C in place of W).
- **Mode statement.** In the real or complex lift, or over ℤ/q with gcd(N, q) = 1 (where the
  uniform and sum-zero sectors are complementary), take a uniform offset. Then the non-uniform
  Fourier modes obey exactly the linear equation, and the uniform mode obeys
  g(t+1) = κg(t) − g(t−1) + b. S1 has gcd(4, 5) = 1.
- **On the gapless locus κ = 2:**
  - the real lift's uniform mode grows as bt²/2, a secular term with no ℤ/q analogue;
  - over ℤ/q the uniform mode is periodic, with period 5 for S1.

So the effective wave equation acquires a constant uniform source. It is invisible to 𝒜_C
(Theorem 2.1). Under 𝒜_abs it is a uniform drift, and on the gapless branch it cannot be removed by a
static uniform shift.

**Proposition 2.6 (countercontrols, sharpness) [D].**
- **(a) Absolute readout.** For S1 with V = Λ (H trivial), ρ = |0⟩⟨0| and an absolute readout at
  t = 1, L gives 0 and Φ gives g(1)𝟙 = 𝟙. Theorem 2.1's hypothesis on the readout class is not
  vacuous.
- **(b) Time-independent relabelling.** With V = Λ, no time-independent relabelling makes the 𝒜_abs
  statistics of S1 agree for all point preparations. A full-state observer can detect period-1
  states, which L has and Φ lacks (B0.2).
- **(c) Partial visibility.** For uniform-prior events of the form {π_V(L^t − I)z = m}, the solution
  set is empty or a coset of ker π_V(L^t − I). So the averaged return probability agrees iff
  p_V(t) ∈ Im π_V(L^t − I). Agreement is therefore possible but not guaranteed. Not settled by hand;
  see §7.

**3.3.7 Coordinate versus gauge equivalence.**

| Transformation | Mathematical status | Physical admissibility on the record |
|---|---|---|
| z ↦ z − p(t), time-dependent uniform translation | always a conjugacy of trajectories (B0.1) | Not established. Theorem 24's generators (Substratum:251–262) and the adjoined amplitude-scale group (Substratum:270–272) are time-independent. |
| uniform static shift | removes b iff b ∈ (κ − 2)ℤ/q (B0.3(c)) | Declared gauge (SM:96, Substratum:270). Never available for S1 (κ = 2). |
| site-dependent static translation | removes b iff β ∈ Im(I − L) (B0.2) | Not declared gauge. A site-dependent relational reading would trivialize all configuration readouts. Never available for S1. |
| identity, with 𝒜_C or 𝒜_W readouts | Theorem 2.1, no transformation needed | Depends on whether 𝒜_C is the observer's readout class, which is not established. Owner decision Q1 (§6): Main's absolute interface is "the formal baseline", and the shift-invariant interface "a legitimate conditional alternative". |

**3.3.8 Pressure test of the favourable reading.** Theorem 2.1 favours the framework: it would make
A5 observationally inert. It is tested here.
1. **The interface.** Main §1.4 indexes T_ij by absolute visible configurations, so only Theorem
   2.2 applies at Main's stated interface. 𝒜_C is a *reading* of Substratum:270 ("no access to the
   absolute scale of the substratum field value"), not a stated interface.
2. **The cost of 𝒜_C, for configuration readouts.** A single-site visible sector has no nontrivial
   *configuration* readout in 𝒜_C, because C acts transitively on one site's two-slice values. It
   still has non-diagonal readouts in the commutant: translation operators and Fourier projectors.
   The diagonal readable alphabet shrinks from q^{2|V|} to q^{2|V|}/|C_V| = q^{2|V|−2}, and in
   general to q^{2|V|}/|W_V| for 𝒜_W. The velocity is not readable (§3.3.1).
3. **Dynamics-dependent preparations.** Preparations uniform on an energy shell (SM:811) are not
   common to Φ and L, since the shells of Q and Q′ differ (N4). Theorem 2.1 assumes a common ρ.
4. **Scope of uniformity.** β ∈ C needs exact translation commutation. Under A4 "up to gauge", β
   can be non-uniform. Then the 𝒜_C form does not apply, and W can be larger.
5. **Exactness.** Every statement is exact algebra. No floating point is involved.
6. **Literal reading of Substratum:270.** Conjugating by a uniform shift gives
   Φ′ = Ad T_V ∘ Φ ∘ Ad T_V⁻¹ at the visible interface, with a uniform hidden prior. So the statement
   that shifts "leave every observable unchanged" (Substratum:270) holds at the labelled fixed
   interface of Substratum §4 only up to a visible relabelling, or for 𝒜_C readouts. SM:96 is
   phrased as "preserve the emergent observables", and already reads nonlinear relabellings as
   preserving transition probabilities "under relabelling", so it is closer to the
   up-to-relabelling form.

**Result: criterion 2 is reached for a specified class.**
- Class: affine bijections, with relational readouts 𝒜_W. For uniform offsets this includes the
  b-independent class 𝒜_C. The equivalence holds for every preparation and at all times
  (Theorem 2.1).
- At Main's absolute interface the equivalence is coordinate equivalence only: a time-dependent
  outcome relabelling, under which all per-time-relabelling-invariant statistics and the quantum
  representability agree (Theorem 2.2, Corollary 2.3).
- Its physical admissibility is not established.

### 3.4 B3 — kernel consumers under affine dynamics

**Proposition B3.1 (ensemble gap without a fixed point) [D].** W is Φ-invariant: Φ(w) = Lw + β ∈ W.
If W ≠ G, Φ is not transitive, so `EnsembleDetermined` fails, by the reasoning of
`not_ensembleDetermined_of_disjoint`. For a uniform offset with N ≥ 2, |W| ≤ q² < q^{2N}. So the
conclusion of `stochastic_interface_gap` holds for S1, even though its hypothesis (A5) fails.

**Proposition B3.2 (cycle count) [D].** π∘Φ = L̄∘π = π∘L on G/W.
- Every Φ-cycle lies over one L̄-cycle, and every L̄-cycle has a Φ-cycle over it.
- The preimage of an L̄-cycle of length ℓ has |W|ℓ elements. Every L-cycle in it has length a
  multiple of ℓ, so it contains at most |W| L-cycles.
- So #cycles(Φ) ≥ #cycles(L̄) ≥ #cycles(L)/|W|.

**Proposition B3.3 (quadratic invariant) [D].** Given in N4.

**Proposition B3.4 (advection gate) [D].** For additive coarse maps C, C∘Φ = C∘L + C(β) is affine.
A closing coarse rule f is then affine on the range, with f(nc) = n(f(c) − f(0)) + f(0), which is of
degree ≤ 1 in n. The quadratic advective scaling is still excluded, on the same coarse class as
`coarseCloses_nsmul`. (In this proposition only, C denotes a coarse map, not the subgroup C.)

***

## §4 Results

| # | Claim | Verdict | Hypotheses | Support | Does NOT establish |
|---|---|---|---|---|---|
| R1 | Φ^t = τ_{p(t)} L^t | holds | affine bijection, finite abelian G | [D] | that τ_{−p(t)} is gauge |
| R2 | Time-independent linearizability ⇔ fixed point ⇔ β ∈ Im(I − L) | holds; reproduces C2. C3 is its case B0.3(e); §7's finite check of R2 (not authorized) would check B0.3(e) and C3 independently | as R1 | [D] | anything for infinite lattices or non-affine rules |
| R3 | Obstruction = resonance with zero modes of A − 2I; uniform-shift class b mod gcd(κ − 2, q) | holds | second-order, translation-commuting | [D] | that S1-type rules are physical |
| R4 | A5 is invariant under the declared shift gauge iff κ ≡ 2 | holds | SM:96 shift gauge as conjugation | [D] | which reading of the gauge is correct |
| R5 | Selection principles N1–N11 | none selects b = 0 with an independent justification. N8 (odd q only) and N9/E1 relocate the assumption. | as stated per node; N9 scoped to extensions E1–E3 | [D] | that no principle exists. The search is finite. |
| R6 | Theorem 2.1, relational equivalence | holds, all times, every preparation | readouts in 𝒜_W; for uniform offsets also 𝒜_C, independent of b | [D] | that 𝒜_C or 𝒜_W is OI's interface |
| R7 | Theorem 2.2 and Corollary 2.3, absolute interface | equal up to a time-dependent outcome relabelling; relabelling-invariant statistics, divisibility and representability agree | any readouts | [D] | equality of labelled statistics; admissibility of P(t) |
| R8 | Spectrum | equal on the W-invariant algebra; differs on the full algebra for S1 | as R6 | [D] | anything about the observer-level L_obs bridge (SM:232) |
| R9 | Kernel-consumer conclusions extend | B3.1, B3.2 and B3.4 hold for uniform offsets | as stated | [D]; the cited kernel results [K] | any kernel statement for affine rules |
| R10 | Candidate hidden use of b = 0 at Stage 2(d): the singlet-block U(1) is lost for b ≠ 0; whether another U(1) can serve is not examined | candidate; open (Q4) | lift; uniform, cubic-invariant offset b ≠ 0 | [D] (review finding) | that Stage 2(d) is wrong, or that it uses A5 rather than another premise |

**Outcome reached.**
- **Criterion 2**, for a precisely specified class (R6, with R7 at Main's interface).
- **Criterion 3**, for the candidates of §3.2 (R5).
- **Criterion 1** is not reached.

***

## §5 Consequences — proposals only, none adopted

**#914 (OI↔QM equivalence).**
- (a) R7 suggests stating that the finite-horizon representation is insensitive to the affine
  offset only up to a time-dependent permutation unitary, not that it is identical.
- (b) Any equivalence statement made at a labelled interface should name whether its readouts are
  𝒜_C, 𝒜_W or 𝒜_abs.
- (c) A5 should not be listed among the premises of the representation. This is already the record
  (C4).

**#1029 (corrections).**
- **(a) Substratum:270.** It asserts that shifts "leave every observable unchanged". Per §3.3.8
  item 6 and R4, this holds up to a visible relabelling or for 𝒜_C readouts, and when κ ≢ 2 the
  same shifts carry the linear rule to affine rules.
  - SM:96 already says "preserve the emergent observables" and reads nonlinear relabellings
    "under relabelling", so the scoping is aimed at Substratum:270.
  - A minimal-change candidate is to scope that sentence to its interface. This is a proposal for
    owner review, not an edit.
  - The corpus also calls x ↦ λx + c "additive-group automorphisms", although shifts are not
    automorphisms. #1050 routed that terminology to a separate corpus-consistency unit, and it is
    left there.
- **(b) A gauge-invariant restatement of A5.** If the owner adopts one, its form depends on the
  gauge assumed:
  - **Under the declared uniform-shift gauge** (SM:96, Substratum:270), for translation-commuting
    rules: "some uniform shift makes the rule linear", i.e. b ∈ (κ − 2)ℤ/q (B0.3(c)). This matches
    the gauge table (§3.3.7) and N6(1).
  - **Only if site-dependent static translations were gauge**, which the corpus does not declare:
    "the update has a fixed point", equivalently it is translation-conjugate to an additive rule
    (R2).
  - **The two forms differ.** At κ ≡ 2 with an odd prime q ∣ N (B0.3(e)), a fixed point exists, but
    no uniform shift removes b ≠ 0.
  - Either restatement would be a status change (⚑) and needs its own review.
- **(c) Main:726 (vii).** No change is implied: "stronger than the affine restriction" stays true.
- **(d) Stage 2(d).** R10 is a candidate for owner and referee attention, not a correction.

***

## §6 Open items and owner questions

- **Q1 (decisive; decided by the owner).** Which readout class is OI's observer interface on the
  lattice substratum: 𝒜_abs (Main §1.4 as written) or a relational class such as 𝒜_C, as
  Substratum:270 suggests? Under 𝒜_C, A5 adds no observable content for uniform-offset rules (R6).
  Under 𝒜_abs it does, exactly on the resonant locus of R3.
  - *Owner decision [O]:* "Preserve Main's currently specified absolute interface as the formal
    baseline. The shift-invariant interface is a legitimate conditional alternative, not yet a
    derived description of all OI observers." Quoted from #1049 comment 6624263637, posted from the
    owner's account (amaybaum) on 2026-11-04T06:28:45Z, which records the owner's chat decisions of
    2026-11-04.
- **Q2 (decided by the owner).** Is the amplitude-scale gauge a relabelling (conjugation of the
  description) or a dynamical symmetry? The relabelling reading leaves b ≠ 0 rules admissible. The
  symmetry reading (N8) gives b = 0 for odd q, but not at any even q.
  - *Owner decision [O]:* "Treat amplitude shifts as mathematical relabellings unless their
    physical gauge status is justified." Same source as Q1.
- **Q3.** Is the local internal group of A6 AddAut(V) or the affine group, and is an offset
  untransported, carried in the links, or transported (E1–E3)? This is the N9 assumption-watch
  marker. It carries A5 in relocated form, and it should be recorded alongside D14 whenever A6 or
  `linkF` is cited.
- **Q4 (open).** At Stage 2(d) (Substratum:163; SM:344), is the stabilizer taken of the linear part
  or of the affine rule? For a uniform, cubic-invariant b ≠ 0 on the lift, the affine rule's
  stabilizer among constant linear unitaries ((A-lin) in `A5-Q4-STAGE2D.md`) is U(3)×U(2), and the
  singlet U(1) is lost (D3, R10). This needs a referee reading.
- **Q5.** Provenance: #1049 attributes the witness to S1 (#1043). The manuscript text with the
  inline witness entered SM:240 through H2 (#1050, merge `981a5460`). S1 set the A5-scope wording
  and cited the counterexample in its record. This matters only for citation.
- **Open.** Infinite lattices and open chains, where a site-dependent quadratic h_i = −b i²/2
  removes the offset; composite q; offsets under A4 "up to gauge"; non-affine rules (out of scope);
  D7 (period formula).

***

## §7 Proposed computation — for separate authorization only

**Purpose.** Exact controls for R2, R3, R6, R7 and Proposition 2.6(c). It would upgrade them from [D]
to exhaustive finite computation on named small cases. It would not establish universal claims.

**Cases.**
- N ∈ {3, 4, 5}, q ∈ {2, 3, 5}, α ∈ {1, 2}, b ∈ ℤ/q, on rings.
- One visible/hidden split with |V| = 2 sites, both slices.

**Decision rules (preregistered as rules, not numbers).**
- **R2:** fixed-point existence equals [β ∈ Im(I − L)] in every case. In addition, compute the
  cycle types of Φ and L from the permutations, and check that they are equal iff
  β ∈ Im(I − L). This tests (i)/(iv) of B0.2 against (iii), not only (ii)⇔(iii).
- **R3:** removability by a uniform shift equals [b ∈ (κ − 2)ℤ/q].
- **R6:** check exhaustively, over every point preparation and every diagonal readout in 𝒜_C, that
  the multi-time laws are equal elementwise up to horizon 2·ord(Φ). This covers the classical
  (point-preparation, configuration-readout) part of Theorem 2.1 only. Arbitrary ρ and non-diagonal
  Kraus operators in 𝒜_C remain paper-only.
- **R7:** the laws are equal after the relabelling x_V ↦ x_V + p_V(t).
- **2.6(c):** report the return probability averaged over the uniform prior for both rules, with no
  predicted value.

**Controls.**
- Positive: the q ∣ N cases have fixed points; b = 0 reproduces L.
- Countercontrol: absolute readouts differ for S1 at t = 1. The velocity readout also distinguishes
  (it lies outside 𝒜_C).

**Verdicts** are read from exit statuses and schema files (§A.44). The work would be CI-scale
(§A.40) and must not run without owner approval.
