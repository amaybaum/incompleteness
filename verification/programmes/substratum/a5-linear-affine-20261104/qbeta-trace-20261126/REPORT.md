# Q-β b-consumption trace (#1049, lane 1) — REPORT

**Standing: WIP / UNVERIFIED. Paper-only research record.** Source reading and hand algebra only. No computation was run, no Lean was built, no manuscript or registry was edited, and no premise was adopted, weakened or dropped; A5 remains a posit. Conventions, decision rule, controls, productivity test and stopping rule are those of `PLAN.md` (committed first, `1fdd0907`). Every new step is labelled [A] (exact hand algebra here, unreviewed) or [W] (reasoning here, unreviewed). Other labels as in `PLAN.md` §3: [K], [P], [D] (A5-LA, Q4, Q3), [R] (POSIT-MIN, OA-1, H-D).

**Authorization.** Owner decision (amaybaum, 2026-11-26T06:25:53Z, #1169 comment 7184425769), lane 1, approved as written: "Determine which results genuinely depend on microscopic linearity and the zero-offset condition." Restrictions: paper-only, no computational experiments, no manuscript changes, no adoption of new premises, no automatic merges.

**Goal link (§A.47).** As in `PLAN.md`: #1049; decides the class of each A5 consumer and which branch of the decision rule obtains.

**Pin.** `main` = `b6c6b80bbd4a878452e54759cc85f16c9ffb72da`. `SM:n`, `Sub:n`, `Main:n`, `GR:n`, `Str:n` are lines of `papers/SM.md`, `papers/Substratum.md`, `papers/Main.md`, `papers/GR.md`, `papers/Structure.md` at the pin. The SM, Substratum and Main files are identical at the pin and at REPORT-r5's pin `e2e2a623`, and the A1-exit site map (pinned at `e837e3db`) has the same line numbering at these lines (every change between the two pins is an in-place line edit), so its line references apply at the pin.

**Notation.** As in `PLAN.md` §4 and A5-LA: Φ = τ_β ∘ L, β = (0, b𝟙), C the uniform two-slice subgroup, κ the coefficient sum, Δ = {(c𝟙, c𝟙)} the common uniform shifts, S_u = Σ_i u_i. On C, L acts as L_C(g_u, g_v) = (g_v, κg_v − g_u).

***

## 1. Countercontrol (required by `PLAN.md` §6)

S1 (SM:240 [P]; N = 4, q = 5, F_i(x) = x_{i−1} + x_{i+1} + 1, κ = 2). Sharp preparation at the zero two-slice configuration, absolute configuration readout at t = 1 (Main's absolute interface):
- linear part L: x_i(1) = 0 + 0 − 0 = 0, readout 0;
- S1: x_i(1) = 0 + 0 + 1 − 0 = 1, readout 𝟙 [A].

The labelled outcomes differ. The relational readout (configuration modulo a constant) gives the same class for both. **The countercontrol passes**, and the classification below is not vacuous: b = 0 has labelled content at Main's absolute interface (A5-LA Proposition 2.6(a) [D], recomputed here).

Preserved results A5-LA C1–C8: none is contradicted by any step below (checked per step; C2 and C3 are used as internal controls in §2.4).

***

## 2. New steps

### 2.1 The uniform-sector orbit at resonance [A]

For a translation-commuting second-order rule with uniform offset, β ∈ C and C is L-invariant, so the zero orbit p(t) = Φ^t(0) lies in C (A5-LA B0.1 [D], re-derived: Φ^t(z) = L^t z + p(t)). At κ ≡ 2, L_C = I + N_C with N_C(g_u, g_v) = (g_v − g_u, g_v − g_u) and N_C² = 0. Hence

  p(n) = Σ_{s<n} (I + sN_C)β = nβ + (n(n−1)/2) N_Cβ = ( b·n(n−1)/2 , b·n(n+1)/2 ).

Check: p(1) = (0, b); p(2) = Lβ + β = (b, 3b). On the real lift this is the secular term of A5-LA Proposition 2.5.

**Consequence (period).** Φ^n = id iff L^n = I and p(n) = 0. For prime q and b ≢ 0, p(n) = 0 iff n ≡ 0 (mod q) when q is odd, and iff n ≡ 0 (mod 4) when q = 2. At κ ≡ 2 the block N_C is nonzero, so q divides ord L_C and hence ord L. Therefore, for every resonant translation-commuting rule with uniform offset:
- q odd prime: ord Φ = ord L;
- q = 2: ord Φ = ord L if 4 ∣ ord L, and 2·ord L otherwise.

Off resonance at prime q a static uniform shift conjugates Φ to L (A5-LA R3 [D]), so ord Φ = ord L. In every case ord Φ divides 2·ord L, and ord Φ = ord L except at q = 2. (Without translation commutation, Φ^n(z) = z + p(n) with n = ord L gives Φ^{pn} = id in characteristic p, so ord Φ ∣ p·ord L.)

### 2.2 Theorem A.1 under a uniform offset [A]

Theorem A.1 (SM:1598–1602 [P]) is the ring wave map with λ_k = ζ^k + ζ^{−k}, so κ = 2 (resonant), and states ord F = qL for prime q with gcd(L, q) = 1, "q = 2 included". By §2.1:
- odd q: ord Φ = qL for every offset b;
- q = 2 (L odd, ord L = 2L, 4 ∤ 2L): ord Φ = 4L for b = 1.

**Controls [A].** L = 1, q = 2: L(u, v) = (v, u), order 2 = qL; Φ(u, v) = (v, u + 1), orbit (0,0) → (0,1) → (1,1) → (1,0) → (0,0), order 4. L = 1, q = 3: Φ(u, v) = (v, 2v − u + 1), orbit (0,0) → (0,1) → (1,0) → (0,0), order 3 = qL. L = 3, q = 2: on C the affine map is (g_u, g_v) ↦ (g_v, g_u + 1), p(6) = (1, 1) ≠ 0, p(12) = 0, ord Φ = 12 = 4L. The b = 0 limit reproduces qL in each case.

### 2.3 The shell-splitting negative transfers to affine rules [A]

For symmetric translation-invariant A (so 𝟙ᵀA = κ𝟙ᵀ) and uniform offset b,

  Q′(u, v) = E(u, v) − b(S_u + S_v),  E(u, v) = u·u + v·v − u·Av (SM:296),

is conserved by Φ. Derivation: with w = Av − u, E(v, w + b𝟙) = E(v, w) + 2bS_w + Nb² − bκS_v, and E(v, w) = E(u, v), S_w = κS_v − S_u; adding −b(S_v + S_w + bN) gives Q′(u, v). (This is A5-LA N4's Q′ [D], re-derived; a one-site check over 𝔽₃ is in §2.4.)

SM:296's argument [P] for the linear rule: cycle lengths divide e = p(p^{2m} − 1); E takes p values, so the largest E-shell has at least p^{2N−1} > e states and is not a single cycle. For the affine rule, §2.1 gives ord Φ = ord L at odd p, so the same bound holds verbatim with Q′ in place of E. At p = 2, ord Φ ∣ 2e, and p^{2N−1} > 2e holds when N ≥ m + 2, which holds for d ≥ 2 (N = L^d ≥ L + 1 ≥ m + 2); the number of cycles in that shell exceeds 2^{2N−2m−3}, exponential in N for d ≥ 2. So the negative of SM:296, SM:1416 and Main:736 (v) holds for every uniform offset at d ≥ 2 (and at d = 1 for odd p). A5-LA D6 had recorded "the shell-specific statement is not transferred"; it transfers.

### 2.4 At resonance an offset makes the quadratic-energy shell relationally uniform [A]

**Proposition (finite field).** Let q = p be an odd prime, κ ≡ 2 (mod p), A symmetric and translation-invariant, b ≢ 0 and p ∤ N. For every k ∈ 𝔽_p, the uniform law on the shell {Q′ = k}, pushed forward to G/Δ, is the uniform law on G/Δ. Hence every Δ-invariant observable (in particular every within-slice link difference x_{n+ê} − x_n, and the velocity v − u) has the same law on each Q′-shell as under the independent-uniform measure on G.

*Proof.* Under σ_c(u, v) = (u + c𝟙, v + c𝟙), E changes by c(2 − κ)(S_u + S_v) + Nc²(2 − κ) = 0 at κ ≡ 2, and S_u + S_v changes by 2Nc. So Q′(σ_c z) = Q′(z) − 2bNc. Since 2bN ≢ 0, c ↦ Q′(σ_c z) is a bijection of 𝔽_p: each Δ-orbit (p elements) meets each Q′-shell exactly once. ∎

**Controls [A].**
- b = 0: Q′ = E is Δ-invariant at κ ≡ 2, so E-shells are unions of Δ-orbits; E is non-constant on G/Δ, so some E-shell has a non-uniform law on G/Δ. The proposition is specific to b ≠ 0.
- p ∣ N: 2bN ≡ 0 and the proof fails, as it must, since then 𝟙 ∈ Im(A − 2I) and a fixed point exists (A5-LA B0.3(e) [D], C3); conversely for p ∤ N, 𝟙 ∉ Im(A − 2I) (A symmetric, 𝟙 ∈ Ker, 𝟙·𝟙 = N ≢ 0), so no fixed point exists (C2 for S1). The trivialization occurs exactly on the no-fixed-point branch.
- One site over 𝔽₃ (A = 2, b = 1): Q′ = (u − v)² − (u + v); on {Q′ = k}, u + v = w² − k for each w = u − v, one point per w, so w is uniform on every shell; Q′ is conserved (Q′(v, 2v − u + 1) − Q′(u, v) = 3v ≡ 0). For b = 0, E = w² and the shell E = 0 forces w = 0.
- S1 (p = 5, N = 4, b = 1): 2bN = 8 ≢ 0, so every Q′-shell of S1 is relationally uniform.

**Real lift [A]/[W].** At κ = 2 write E = E_⊥ + E_0, E_0 = N(g_u − g_v)², with E_⊥ the energy of the non-uniform modes. Under Φ the non-uniform modes obey the linear equation (A5-LA Proposition 2.5 [D]), so E_⊥ is conserved, and the uniform part of Q′ is Q′_0 = N w² − bN s (w = g_u − g_v, s = g_u + g_v), also conserved. For b = 0, E_0 ≥ 0 and the E-shell confines E_⊥ ≤ k. For b ≠ 0, Q′_0 is unbounded below, so the Q′-shell confines E_⊥ not at all: the microcanonical weight ∫ δ(E_⊥ + Nw² − bNs − k) dw ds = ∫ dw/(bN) does not depend on E_⊥, and after division by the divergent uniform-sector volume the marginal on the non-uniform modes is flat [W for the regularization]. **K-component form [W].** On the six-link carrier with H-b and μ_{A₁} = 1 the same computation runs along the uniform A₁ direction.

**Alternative energies [A].** E_⊥, and E_⊥ + f(Q′_0) for any f bounded below (for example f(x) = x², a quartic), are conserved and do confine E_⊥; over 𝔽_p, E_⊥ and E_⊥ + f(Q′_0) have non-uniform relational shells. The trivialization is specific to the total quadratic invariant.

### 2.5 The kernel's ensemble gap at one site [A]

`StochasticInterface.EnsembleDetermined φ` (:32 [K]) is uniqueness of the invariant probability; for a permutation of a finite set it holds iff φ is transitive. For a uniform offset with N ≥ 2, W ⊆ C, |C| = q² < q^{2N}, and W is Φ-invariant, so Φ is not transitive (A5-LA B3.1 [D], re-derived). At N = 1 the uniform sector is all of G:
- q odd, κ ≡ 2: by §2.1, ord Φ = q < q² = |G|, so Φ is not transitive; the gap holds;
- q = 2: take the wave substratum on a one-site torus (L = 1, any d, any α); F(c) = 2dα·c + b ≡ b, and Φ(p, c) = (c, p + 1) is a 4-cycle on the 4 configurations, so Φ is transitive and its ensemble is determined. The conclusion of `waveSubstratum_stochastic_interface_gap` (:191 [K]; its hypotheses `[NeZero L] [Fact (1 < q)]` admit L = 1, q = 2) fails for this affine rule.

### 2.6 The hydrodynamic gate for any offset [A]

In `HydroSourceAudit` (:137, :156, :170 [K]) the closure relation Φ_c(C x_t, C x_{t−1}) = C x_{t+1} with x_{t+1} = A x_t + b − x_{t−1} and additive C gives Φ_c(sum) = Φ_c(x) + Φ_c(y) − Φ_c(0, 0) on the range, with Φ_c(0, 0) = C(b). Hence Φ_c(n•u, n•v) = n•Φ_c(u, v) − (n − 1)•Φ_c(0, 0): degree at most one in n, for every offset b, uniform or not. No quadratic (advective) term arises. This is A5-LA B3.4 [D], re-derived without the uniformity assumption.

### 2.7 The readings stated on the Σ-route [P]/[W]

The manuscript states three readings of the group that Stage 2(d) computes:
- **(R-coup)** Sub:102 (A6 text): "The global commutant symmetry — the transformations constant across the lattice that leave the coupling itself unchanged … — is what the local gauge reading of [SM §3.1] proceeds from." The coupling contains no offset.
- **(R-kin)** Sub:163: "Under single-copy H-link and H-cust, the unitary stabilizer of the O-equivariant condensate with distinct block values is U(3)×U(2)×U(1) [SM Theorem 5]." SM:340: H-cust is "the observer-level kinetic structure is custodially scalar"; the proof reads "the pre-condensate observer-level kinetic term is invariant under the custodial unitary action". Sub:193 (Theorem 23): "the generic condensate stabilizer under H-cust". An offset is a source term, not a kinetic term, and Stab_{U(6)}(Σ) does not contain it.
- **(R-dyn)** SM:493: "The substratum dynamics is locally U(6) invariant …; they are removed spontaneously: the O-equivariant condensate Σ breaks U(6) → U(3)×U(2)×U(1) (Theorem 5, revised)". The ambient is the symmetry of the substratum dynamics, which an offset enters (Q4 S2–S3 [D]).

**A located variance, independent of A5 [W].** SM:130 states that at M = μI "the substratum dynamics, the threshold nonlinearity of the finite alphabet and the selected measure all commute with the signed permutations of the components", and "The custodial U(6) of the real lift (Theorem 5, §4.6) is broken by the threshold only down to this signed-permutation group, which suffices". So on SM's own account the substratum dynamics with its threshold is not U(6)-invariant, contrary to SM:493's sentence; and on the exact rule over ℤ/q no U(6) acts. SM:130 and SM:340 treat U(6) as a symmetry of the real lift's kinetic part with explicit breaking; SM:493 treats it as exact. A5-Q4-STAGE2D §2 cited SM:342 and SM:493 together for one route; they state different ambients.

**SM:130 and the offset [A].** Sign flips of a component commute with the component rule x ↦ Ax + b iff 2b = 0. A uniform A₁ offset (the same b on all six link components, H-b) leaves the permutations and breaks the sign flips for odd q; the six-dimensional permutation representation is reducible (trivial ⊕ standard), so SM:130's irreducibility route does not apply. The product route of Proposition 4b (SM:336 [P]: six identical, decoupled components) still applies, because the offset is the same in every component, and the connected response is offset-independent (Φ^t is a translate of L^t and the counting measure is translation-invariant). The conclusion (custodial scalarity at M = μI) holds; SM:130's sentence "commute with the signed permutations" uses 2b = 0. (The rounded rule's floor((Σ + 1)/3) is odd: floor((1 − S)/3) = −floor((S + 1)/3) for every integer S, checked on residues mod 3, so the rounded realization does satisfy the sign-flip clause.)

***

## 3. Classification table

Columns: consumer; source pin at `b6c6b80b`; class per locus (worst class in bold); linearity level needed (rule or lift); A1-exit ledger row (site-map entry at the line, or the row whose home covers the result); finite-q use; input labels. "Res." = resonant uniform sector (κ ≡ 2; with H-b, μ_{A₁} = 1).

| # | Consumer | Pin | Class | Level | Ledger row | Finite q | Inputs |
|---|---|---|---|---|---|---|---|
| D1 | Wave-form Lemma; Stage 2(b) | SM:224; Sub:159 | **(a)**: the proof's conclusion for affine f is α Σ x_j + b; downstream results read the linear part (α, nearest-neighbour symmetric form) | lift suffices for the form (SM:224 states the Lemma "at either the substratum-symbolic level or an observer-level linear lift"); Sub:159 states it mod q (rule level) | SM:222, :232 → X-41; Sub:159 no site entry, within X-45 (Theorem 23) | Sub:159 states the form mod q; the lift form uses none | [P], [D] A5-LA D1 |
| D2 | Dispersion and observer-level normalization | SM:226–232 | **(a)**: the symbol cos ω = αΣcos(k_j a) is that of L; the offset sources only the uniform mode, which no dispersion statement reads | lift (SM:232: α = 1/d belongs to L_obs) | SM:232 → X-41 | none for the lift; SM:232 notes 1/d ∈ ℤ/q needs 3 ∤ q | [P], [D] A5-LA D2, Prop. 2.5 |
| D3 | Stage 2(d), Σ-route | Sub:163; SM:340 (Theorem 5); SM:493; Sub:102 | **Q4b-dependent, node stopped.** R-coup and R-kin: **(a)**. R-dyn: (b) off Res. (static uniform shift to the fixed point, owner Q2); **(c)** on Res.: U(1)_S lost, 11 generators explicitly broken (Q4 N6a), while O1–O4 agree at group level and carrier agreement is conditional (Q4 outcome (iii)) | R-coup/R-kin: lift (kinetic term, coupling); R-dyn: rule (symmetry of the substratum dynamics) | Sub:163 no site entry; SM:334/:336 → X-10; Theorem 5 H-cust clause and Prop. 4b: X-17, X-18 | none | [P], [D] Q4 N0–N6 (H-b, lift, uniform offset), [W] §2.7 |
| D4 | §6 gauge map (link differences) | SM:811 | **(a)**: the map reads x_{n+ê} − x_n, invariant under uniform shifts; its uniqueness clause ("the additive structure the wave equation evolves") holds for affine rules, whose differences evolve by L | rule (linear part) | SM:811 → X-11 | yes: ℤ/q → U(1), 2π/q | [P], [D] A5-LA D4 |
| D5 | Energy-shell measure for the pushforward | SM:811 (with SM:290–296) | off Res.: (b) (Q′ = E(z − p) + const, shells are uniform translates; the link-difference law is equal); on Res.: **(c)** under the stated reading (quadratic total energy: "on-shell Gaussian", SM:296's E): each Q′-shell is relationally uniform (§2.4), the independent-uniform field SM:811 rejects. Alternative-energy branch (E_⊥, or E_⊥ + f(Q′_0)): (a) | rule (conserved energy of the rule or its real lift) | SM:811 → X-11 | exact form: odd prime p ∤ N; real-lift form: none | [P], [A] §2.4, [W] (regularization; K-component form) |
| D6 | Cycle splitting; Main posit (v) | Main:736 (v); Main:770; A5-LA B3.2 | **(a)** for d ≥ 2 (§2.3; B3.2 [D]) | rule | Main:736 (v) home of X-56; X-56 (SM §4.2) | yes: prime p ∤ L | [P], [A] §2.1, §2.3 |
| D7 | Theorem A.1 (period qL), cited at SM:92 | SM:1598–1602; SM:92 | odd q: (a) (ord Φ = qL, §2.2); q = 2: **(c)** (ord Φ = 4L ≠ 2L; at q = 2 every rule is resonant and no static uniform shift removes b) | rule | no site entry; SM:92 not in the site map | yes: prime q, gcd(L, q) = 1 | [P], [A] §2.1–2.2 |
| D8 | Continuous path | `SecondOrderDrive.driveQ_isContinuousPath` (:225) | **n/a**: holds for every `Rule` | neither | none | none | [K] |
| D9 | Representation and characterization | Main §3.4 | **n/a**: universal over finite visible laws; takes no A5 premise | neither | X-31, X-32 (their own A1 rows) | per those rows | [P], [R] H-D A5S-1b |
| D10 | GR §3–§6 | GR:673–679 | **n/a**: "A2-A5 … not for the universality-class-level claims"; GR:679's proof at derivation-sketch level | neither (as stated) | X-57, X-72 for GR's own A1 uses | per those rows | [P] |
| D11 | BFSS comparison | Str:300, :308 | **n/a**: BFSS is non-affine; outside Q-β | neither | none | none | [P] |
| D12 | Ensemble gap | `StochasticInterface` :89, :118, :182, :191 | N ≥ 2: (a) (§2.5; B3.1); N = 1, q odd: (a); N = 1, q = 2: **(c)** (§2.5: the affine one-site rule is transitive) | rule | no row (StochasticInterface not in the ledger's Lean list); A1 predicate rows X-81 | yes: `Fintype` configuration space | [K], [D] B3.1, [A] §2.5 |
| D13 | Advection gate | `HydroSourceAudit` :126, :137, :156, :170 | **(a)** for every offset, uniform or not (§2.6) | rule | none | none (general additive groups) | [K], [A] §2.6 |
| D14 | A6 carrier, `linkF : V →+ V` | `A6Instantiation` :147 (`linkSubstratum_A5`), :306, :484; `BackgroundIndependence` | **n/a**: A5 holds by the carrier's typing (A5 relocated; A5-LA N9, Q3 open); not a consumer of b | rule (typed additive links) | X-81 (A6Instantiation .A1 sites) | `CX3-a` holds at the complex carrier | [K], [D] Q3 |
| D15 | Shell-sampling site | SM:1416 (with SM:296) | the candidate-class label "use linear dynamics (A5)" is definitional (**n/a**); the stated negative ("does not satisfy linear dynamics and cycle ergodicity jointly") is **(a)** for d ≥ 2 (§2.3) | rule | no site entry at :1416; its cited remark is X-56 | yes: prime q not dividing L | [P], [A] §2.3 |
| D16 | Theorem 23 and Lemma 23.0 | Sub:193, Sub:189 | stated reading R-kin ("under H-cust"): **(a)**; under R-dyn: inherits D3 ((b) off Res., (c) on Res., O1–O4 at group level per Q4). **Q4b-dependent, node stopped** | R-kin: lift; R-dyn: rule. Stage 2(b) inherits D1 | Sub:189, :193, :195 → X-45 | Theorem 23 lists A1 among its hypotheses (X-45) | [P], [D] Q4 |
| Σ | Stage 2(d) on the Σ-route | as D3 | as D3 | as D3 | as D3 | as D3 | as D3 |
| T23 | Theorem 23 | as D16 | as D16 | as D16 | as D16 | as D16 | as D16 |
| 1416 | SM's shell-sampling site | as D15 | as D15 | as D15 | as D15 | as D15 | as D15 |
| K1 | `SubstratumInterfaceAudit` | `A5` :102; `waveSubstratum_A5` :211 | **n/a**: the predicate and a witness | — | X-81 (module's A1 sites) | witness on a finite torus | [K] |
| K2 | `HydroSourceAudit` | as D13; `map_zero_of_additive` :126 is the implication additivity ⇒ F 0 = 0 itself (n/a) | **(a)** | rule | none | none | [K], [A] |
| K3 | `StochasticInterface` | as D12; `phi_fixes_zero` :89 is the implication A5 ⇒ φ 0 = 0 itself (n/a) | **(c)** at N = 1, q = 2; (a) otherwise | rule | none | yes | [K], [A] |
| K4 | `HexLatticeGas` | `hexSubstratum_A5_witness` :641, `hexSubstratum_not_A5` :685 | **n/a**: a witness of non-additivity at nonzero arguments (non-affine), not a use of A5 | — | X-81 (`hexSubstratum_A1` :312) | finite | [K] |

**Further site met while tracing (outside the list).** SM:130 (custodial matching, signed permutations): conclusion (a) by the product route; the sentence uses 2b = 0 (§2.7). Ledger: no site entry at :130.

**Kernel re-enumeration at the pin [K, read].** Results taking A5 (or its unfolded form) as a hypothesis are still confined to `HydroSourceAudit` and `StochasticInterface`; `HexLatticeGas` carries its failure. Results whose statement carries `.A5` as a conclusion now also stand in `A6Instantiation` (`linkSubstratum_A5` :147, `pk3e_A5` :306, `cx3a_complex_axioms` :484) and `WaveSubstratumUnbounded` (`waveZ_A5` :58). Under H-D's criterion (i) ("statement carries `Substratum.A5`") the list therefore spans six modules at the pin, not four; no result takes any of the new entries as a hypothesis, and no OI → QM module appears.

***

## 4. Decision rule

Verbatim (`PLAN.md` §5): "If no consumer falls in class (c) under the reading the manuscript states, the outcome is 'unnecessary in sense (1) at stated scope' (criterion 2 of #1049). Otherwise #1049 reduces to Q4c, conditional on SM:232."

Consumers placed in (c) under a reading the manuscript states, from §3:
- D5, under the quadratic total-energy reading SM:811 states, on the resonant locus. SM:811's stated covariance ∝ □_lat^{-1} is the massless normalized operator, which is resonant by construction (Corollary 1b's constant-preserving kernel gives κ = 2). Conditions: for the real lift, that a substratum offset reaches the level at which the energy is taken (SM:232's unproved bridge), and H-b for the K-component form; for the exact form, κ ≡ 2 (mod p) on the substratum, odd p ∤ N.
- D7, at q = 2, unconditionally (Theorem A.1 states "q = 2 included").
- D12 / K3, at N = 1, q = 2 (the kernel statements admit the one-site torus).
- D3 and D16 under R-dyn (SM:493), conditional on μ_{A₁} = 1 (Q4c), H-b and SM:232.

**Outcome: the first branch does not obtain; the second branch obtains.** #1049 is not "unnecessary in sense (1) at stated scope". The second branch's wording ("reduces to Q4c, conditional on SM:232") describes the D3/D16 placement and, through SM:232, the real-lift form of D5. It does not describe D7 and D12/K3, whose placements are unconditional at q = 2 and do not involve Q4c, or the exact form of D5, which turns on substratum resonance κ ≡ 2 (mod p) rather than on the maintained lift branch. The rule is applied as written; the residual it leaves is stated in §7.

***

## 5. Productivity verdict (`PLAN.md` §7)

- Every listed consumer moves from REPORT-r5's "not traced" to a pinned class (§3).
- Consumers are placed in (c) under stated readings (D5, D7, D12/K3; D3/D16 on the R-dyn branch).
- Unrecorded uses of b = 0 are exposed: SM:811's energy-shell candidate at resonance (§2.4), Theorem A.1 at q = 2 (§2.2), the kernel ensemble gap at one site (§2.5), SM:130's sign-flip clause (§2.7).

**Verdict: gem.**

**§A.31 classification of findings.**
- NEW: §2.4 (at resonance an offset makes every quadratic-energy shell relationally uniform; D5 in (c)). A5-LA D5 recorded only that "the shell measures differ".
- NEW, minor: §2.1–2.2 (the period is offset-independent except at q = 2; Theorem A.1 changes at q = 2); §2.5 (the kernel gap's affine analogue fails on the one-site torus at q = 2).
- NEW, minor: the SM:130 / SM:340 versus SM:493 variance on whether U(6) is an exact symmetry of the substratum dynamics (§2.7), which bears on Q4b and is independent of A5.
- ELABORATING: §2.3 (the shell-splitting negative transfers; A5-LA D6 had not transferred it); §2.6 (the hydrodynamic gate for non-uniform offsets); SM:130's sign-flip use (recorded for Proposition 4b at Q4 N6(b)); the kernel re-enumeration (six statement-carrier modules).
- POSITIVE: D1, D2, D4, D6, D13, D15 use only the linear part.
- CONFIRMING: the countercontrol (A5-LA Proposition 2.6(a)).

**Assumption-watch marker AW-QB-1.** q = 2 is resonant for every rule, and there the uniform-sector sum n(n − 1)/2 does not vanish at n = q; any statement about periods, orbits or transitivity that includes q = 2 is checked separately for an offset.

**Passes.** Pass 1 (classification of the list) produced §2.1–2.3, §2.6 and the D3 branches. Pass 2 (scope boundaries of each classified statement: q = 2, N = 1, p ∣ N) produced §2.2's q = 2 case and §2.5. Pass 3 (sites cited by the consumers' proofs: SM:130, SM:290–296, SM:493, Corollary 1b) produced §2.4 and §2.7. Pass 4 (Main:364, Main:770, Str:300–308, GR:673–679, the A6Instantiation and WaveSubstratumUnbounded witnesses, and a re-check of D4 and D13 for non-uniform offsets) produced no NEW finding. Pass 5 (the K-component form of §2.4, the alternative-energy branch, the R-kin pressure test of §6) produced no NEW finding. The stopping rule is met.

***

## 6. Pressure tests (§A.31)

**Branches favourable to "A5 is unnecessary".**
- *R-kin and R-coup place D3 and D16 in (a).* The (a) class rests on Theorem 5 as a statement about Stab_{U(6)}(Σ) under a kinetic hypothesis. Its physical reading, "the unbroken subgroup of a state with condensate Σ is its unitary stabilizer" (SM:340 proof), presupposes that U(6) is a symmetry of the full pre-condensate dynamics, which is R-dyn. Under SM:130's own explicit-breaking account the threshold is a component-local, sign-symmetric breaking; a uniform A₁ offset is component-local but distinguishes A₁ from T₁ ⊕ E (it leaves S_6, not the signed permutations). So R-kin does not show that the offset is a harmless breaking of the same kind; it shows only that the offset does not enter the stabilizer as defined. Recorded as Q4b; the node stops.
- *D12 in (a) for N ≥ 2.* B3.1 needs a uniform offset (exact translation commutation). For non-uniform offsets under A4 "up to gauge" W can be larger; not examined.
- *D6 and D15 in (a).* The transfer uses ord Φ = ord L at odd p, which needs a translation-commuting rule with uniform offset; without translation commutation only ord Φ ∣ p·ord L holds, and the bound then needs N ≥ m + 2 at every p.

**Branches favourable to keeping A5.**
- *D5 in (c).* The placement depends on reading "a real-valued conserved energy" as the total quadratic invariant. E_⊥ (the non-uniform-mode energy) is conserved for affine rules and removes the effect; it is not stated in SM:811. Both branches are recorded (§3). The placement also needs the resonant locus at the level where the energy is taken.
- *D7 in (c).* Theorem A.1 is a theorem about the linear map and is correct as stated; the (c) placement concerns its use as a property of the substratum update at q = 2 (SM:92 lists it among the results that carry q). No other result found at the pin consumes the period at q = 2.
- *D12 / K3 in (c).* The failure is on the one-site torus only; for N ≥ 2 the gap holds for every uniform offset.

***

## 7. Open nodes

- **Q4b** (rule or coupling stabilizer; linear or affine elements). D3 and D16: (a) under R-coup and R-kin, (b)/(c) under R-dyn. Stopped per the stopping rule. The SM:130/SM:340 versus SM:493 variance (§2.7) is evidence for that decision, not a decision.
- **Q4c** (μ_{A₁} = 1 on the maintained branch), conditional on SM:232. SM:811's stated massless covariance and Corollary 1b's constant-preserving kernel place those sites on the resonant branch.
- **D5's energy reading**: total quadratic invariant (c) versus non-uniform-mode energy (a). Not stated in the manuscript.
- **Substratum resonance** κ ≡ 2 (mod q), that is α ≡ 1/d, for the exact form of D5; SM:232 places α = 1/d at observer level and Sub:169 leaves the substratum α undetermined.
- **Non-uniform offsets** (A4 "up to gauge"): D3, D5, D12 not examined.
- **O5** (A6 promotion; Q4 N7) and **Q3** (E1–E3) for D14: not examined here.
- **Composite q**: §2.1, §2.4 and §2.5 are stated for prime q.
- **Q-α** (whether the update is affine) and **Q-γ** (selection of b = 0): outside this lane.

***

## 8. Findings for routing (listed, not edited)

1. SM:493 "The substratum dynamics is locally U(6) invariant" against SM:130 (U(6) of the real lift, broken by the threshold to the signed permutations) and SM:340 (kinetic H-cust). Independent of A5; suggested route #1029; bears on Q4b (#1049).
2. SM:130 "commute with the signed permutations of the components": holds for linear and rounded rules, not for an affine component rule with 2b ≠ 0; the conclusion survives by Proposition 4b's product route. Relevant only if A5 is relaxed.
3. SM:92 / SM:1600 (Theorem A.1, q = 2 included): a property of the linear map; for an affine update at q = 2 the period is 4L. Relevant only if A5 is relaxed.
4. SM:811's "uniform measure on the energy shell of a real-valued conserved energy": for an affine update at resonance the total quadratic invariant gives the independent-uniform relational law. Relevant only if A5 is relaxed.
5. H-D `A5S-1b`'s closure "at four modules" is stale at the pin under its criterion (i) (six modules; §3). H-D is a frozen record; a mutable record citing it would carry the correction (§A.42 item 6).

***

## 9. Verification status and remediation (§A.46 items 4 and 8)

| Claim class | Where | Status | Missing verification | Accountable Issue | What would resolve it |
|---|---|---|---|---|---|
| New [A] steps §2.1–2.6 | §2 | partially verified: hand algebra, unreviewed | independent review; exhaustive finite checks on named cases (S1; the §2.2 and §2.4 controls; one-site q = 2) under a separate authorization | #1049 | a recorded independent review, or an authorized exact computation with green controls |
| [W] steps (§2.4 regularization and K-component form; §2.7 readings and variance; §6) | §2, §6 | exploratory | derivation at [A] or better; owner or referee reading for Q4b | #1049; #1029 for §8 item 1 | a written derivation; an owner decision on Q4b |
| Classification table | §3 | partially verified; rests on [D] inputs for D1, D2, D3, D16 | A5-LA and Q4 remediation (REPORT-r5 §7.6 V-1) | #1049 | as REPORT-r5 V-1 |
| Decision-rule outcome | §4 | follows from §3 | as §3 | #1049 | as §3 |

**Preservation rationale (proposal).** The record states, for each A5 consumer on `main`, its class and linearity level at a pin, and four uses of b = 0 not recorded elsewhere on `main`; it is the trace REPORT-r5 §7.6 V-2 names. Its landing needs an independent non-author review and a separate recorded owner decision (§A.46 item 8; §A.50 item 1).

**Off-`main` references (§A.42 item 8).**

| Reference | Where | Classification |
|---|---|---|
| #1169 comment 7184425769 (owner decision) | header | provenance: authority record, quoted with author and time; no result uses it |
| #1226 | `PLAN.md` §3 | provenance: named as not used |
| #1049, #1029, #1169 | §§4–9 | provenance: routing and accountability |
| commits `b6c6b80b`, `e2e2a623`, `e837e3db`, `1fdd0907` | header | on `main` (the first three) or on this record's branch (the plan commit, which lands with this record) |

Support off `main`: none.
