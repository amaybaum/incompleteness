# Node 4: the coherent hidden prior as a candidate source at A1

Research only, consistency axis (§A.23). F2 stays A1 (exact finite operational QM on qubit-power registers). No
premise adopted, no status changed, nothing written to `main`.

**Base.** `main` = `809fa9d6`. `papers/` and `verification/lean-mathlib/` are identical between `df9e601e` and
`809fa9d6` (`git diff --quiet`), so paper lines (Main.md:n, Substratum.md:n, SM.md:n) and Lean lines hold at both.
Every [AT] name was confirmed by `git grep` of its declaration at `809fa9d6`; Lean paths are under
`verification/lean-mathlib/OIBridge/`. N1 = `../oa-node1/NODE.md`, MC1 = `../mc-node1/NODE.md` (with node 1b, §9),
MC2 = `../mc-node2/NODE.md`, MC3 = `../mc-node3/NODE.md`, PLAN = `../PLAN.md`, all with their review outcomes. LG =
`f2-ledger-20261020/LEDGER.md` at `origin/ccr-9c2ecca4-vkb666` `3ecdefe9`.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (two runs,
byte-identical); [UP] unsourced premise; [L] literature; [rec] recorded in the cited record, not re-derived.

**Productivity test (fixed before the node).** Gem iff the node yields a fact strictly stronger than "a coherent prior
is a non-classical posit" and either constrains the form a source must take or exposes a hidden assumption.

***

## 0. The model

- **κ1c (coherent prior).** The hidden sector X carries a fixed unit vector h ∈ ℓ²(X), or ψ ∈ L²(X, μ) for a
  continuum, in place of the probability measure μ_H of Main.md:60. Three forms are examined:
  - **N**, real nonnegative amplitudes. This is the Koopman–von Neumann reading h = √μ (MC3 K1–K2).
  - **R**, real amplitudes of both signs.
  - **C**, complex amplitudes.
- **κ2.** Processes are nonsingular, bimeasurable bijections of C × X, with any time index, real coupling or setting
  (MC3 §2). They act on vectors by their Koopman operators: permutation operators for countable X, weighted composition
  operators on L² for a continuum.
- **κ3.** The G3 identification: a process acts on joint descriptions by Ad_U.
- **κ4.** Readouts are visible configuration readouts, with classical feed-forward, coarse-graining, attach of
  configuration or uniformly mixed visible ancillas, and discard. The hidden sector is never read.

The corpus takes the mixed reading throughout:
- Main.md:60 makes the prior a measure;
- the kernel attaches "a maximally mixed ancilla, never a pure one" (`uniformAttach` OperationalAssembly.lean:492);
- a pure attach is derived only for configuration seeds (`pureSeedPrep_available_of_swap` :675).

***

## 1. Node Q1: what each form supplies

### 1.1 The transport lemma [W; EC E1, E8, S1]

**Statement.** Under κ1c–κ4, let X be countable and take the hidden configuration basis. For every finite protocol,
every Kraus operator of every outcome has the form K = Σ_x h_x Q_x, with each Q_x a 0/1 partial permutation of C.
Each row of K has at most one nonzero entry, and that entry is a single amplitude h_x.

**Proof.**
1. Permutation operators and configuration projectors are 0/1 partial permutations of C × X. So is the attach of a
   configuration ancilla, and a uniform visible attach is a mixture of such attaches. Their products are again 0/1
   partial permutations, so the joint operator W of each outcome branch is one.
2. The Kraus operator is K_{x′} = (I ⊗ ⟨x′|) W (I ⊗ |h⟩) = Σ_x h_x ⟨x′|W|x⟩.
3. Row (v′, x′) of W has at most one nonzero entry over all columns (v, x). ∎

**Continuum form [W].** A Koopman (weighted composition) operator of a nonsingular bijection maps |v⟩ ⊗ L²(X) into
⊕_{v′} |v′⟩ ⊗ L²(A_{v,v′}). For fixed v′, the sets A_{v,v′} are pairwise disjoint over v, since they are images of
disjoint sets under a bijection. Products with visible configuration projectors keep this support separation. The
visible map is then

  ρ ↦ Σ ρ_{v₁v₂} ⟨ψ_{v₂→v₂′}, ψ_{v₁→v₁′}⟩ |v₁′⟩⟨v₂′|,

and for fixed v′ the transported functions ψ_{v→v′} have disjoint supports. **Amplitudes are transported, never
added:** no configuration ever receives two amplitudes.

This is LG's monomial-branch lemma (LEDGER.md:116–123: "coherent preparations do not give coherent control") applied
to a hidden preparation that is never read. MC3's C1 row already identifies a non-distribution hidden state with a
coherent preparation. The lemma extends that identification to every hidden cardinality and to Koopman dynamics.

**Checks [EC].** These are instances. Each follows from injectivity of the joint map, and none is independent
evidence of the lemma beyond its code path.
- E1: every bijection at |X| = 3 (720) and |X| = 4 (40 320) gives row-monomial Kraus operators with single-amplitude
  entries.
- E8: 12 221 two-step protocols with a visible readout and feed-forward, under the signed and Fourier priors, give the
  same.
- S1: the symbolic prior (h₀, h₁, h₂) over all 720 bijections at |X| = 3.
- The independent review computes the channel by a separate path, Ad_U followed by the partial trace with no Kraus
  operators, and agrees with the Kraus channel on all 720 bijections at |X| = 3 under a signed and a complex prior
  (review R1).

### 1.2 Corollaries

1. **Effects are diagonal [W; EC E2, S1b].** Row-monomiality makes K^H K diagonal, so no non-configuration test
   arises, sharp or unsharp.
2. **Native statistics are those of the mixed prior |h|² (statistical equivalence) [W; EC E3, E8, S1a; L].**
   - Take a protocol started in configuration states. Each branch amplitude is W|c⟩ ⊗ |h⟩ = Σ_x h_x W|c, x⟩, and the
     vectors W|c, x⟩ are distinct basis vectors or zero. Every outcome probability is therefore Σ_{x ∈ A} |h_x|² for
     a set A that the protocol fixes. In the continuum it is ∫_A |ψ|² dμ.
   - E3 checks this for all 40 320 bijections under six priors. S1a checks it symbolically: the probabilities are
     polynomials in h_x h̄_x alone, with no cross terms. The review extends it to 1 600 two-step protocols with a
     visible ancilla attached pure or uniformly mixed (review R4).
   - Visible states reached by earlier protocol steps are covered, since such steps are part of the protocol.
   - This is the immediate corollary of LEDGER.md:116–123. In coherence-theory terms it is the fact that permutations
     and configuration measurements commute with complete dephasing Δ, so configuration statistics depend on the input
     only through Δ(|h⟩⟨h|) = diag(|h|²). Dephasing-covariant operations are defined and studied in [L: Chitambar and
     Gour, "Critical examination of incoherent operations and a physically consistent resource theory of quantum
     coherence", Phys. Rev. Lett. 117, 030401 (2016); Chitambar and Gour, Phys. Rev. A 94, 052336 (2016); Marvian and
     Spekkens, "How to quantify coherence: distinguishing speakable and unspeakable notions", Phys. Rev. A 94, 052324
     (2016)]. Bibliographic data were confirmed; the full texts were not read.
3. **One-outcome unitary channels are monomial [W; EC E4, E4r].**
   - conj(V) has a rank-one Choi matrix, so every Kraus operator is ∝ V. An invertible row-monomial matrix is
     monomial.
   - The entries of V, normalized, are ratios h_x/h_y of prior coordinates (E4r). Unitarity forces all of them to be
     unimodular.
   - Non-unitary V with conj V available are ∝ a row-monomial K as well, which is what `hmem` of
     `countable_not_pairFlowSourced` (PairFlowEquivalence.lean:218) quantifies over.
4. **The ones identity, for h ∈ ℓ¹(X) (or ψ ∈ L¹, finite measure) [W; EC E5].**
   - Σ_{x′} K_{x′}^H 1 = (Σ_x h̄_x)·1 for every bijection.
   - For a whole protocol the same holds, because each column of the joint operator lies in exactly one branch [W]. A
     uniform visible discard needs the kernel's weight splitting (`instAvail_onesNormal` InstrumentRealization.lean:313).
   - If Σ_x h_x ≠ 0, 1 lies in the span of the K^H 1. The family is then `OnesNormal` after splitting (MC1 T2 [rec]),
     and every available unitary fixes the all-ones ray (`instAvail_unitary_fixes_ones` InstrumentRealization.lean:398;
     E4b on four priors). This direction is the one proved; the converse is not claimed.
5. **When a ray-moving deterministic phase is available [W; EC E4r, E6; review R2, R2b, C1].**
   - *Necessary:* Σ_x h_x = 0 (for h ∈ ℓ¹, by item 4). Also necessary (countable X): two coordinates of equal modulus
     and distinct phase. By item 3 a ray-moving monomial V has a normalized entry h_x/h_y that is unimodular and different from 1.
   - *Not sufficient:* Σ h = 0 alone does not give one. The priors (2, −1, −1), (3, −1, −2) and (3, −1, −1, −1) have
     Σ h = 0 and no unimodular ratio other than 1. Exhaustive single-step checks give only permutation channels, none
     ray-moving (review R2). The prior (3, −1+i, −2−i) has Σ h = 0 and gives none either (review C1).
   - *Sufficient:* an eigen-relation h∘σ⁻¹ = λh with λ ≠ 1 for some hidden bijection σ. The controlled step
     (v, x) ↦ (v, σ^v x) then gives Ad diag(1, λ) exactly, and the eigen-relation implies Σ h = 0 for h ∈ ℓ¹. Instances:
     (1, −1, 1, −1) under a 2-cycle (Z; E6.Z-signed, review R2b); the Fourier vector of a 4-cycle (S; E6.S-complex); the
     continuum eigenfunction of §1.3 (S2a).
   - A characterization that is both necessary and sufficient is not given.
   - The KvN vector √μ has Σ h > 0, so it never supplies one.

### 1.3 The three forms

The invariant conditions below are [W] from the swap of two hidden coordinates into the visible bit, which turns
|0⟩⟨0| into an operator with off-diagonal entry h_x h̄_y.

| form | unitary channels (κ2–κ4) | invariants | (a) continuum of non-monomial operations | (b) deterministic phase | (c) toward O-B |
|---|---|---|---|---|---|
| N, √μ (KvN) | permutations only (E4, E6) | `OnesNormal`, `NonnegBounded` and reality kept (E6) | no | no | coherent nonnegative states are reachable (MC3 K1); effects diagonal |
| R, signed | signed permutations at most. Z needs two coordinates of equal modulus and opposite sign, and an eigen-relation suffices (§1.2 item 5); S never (E6.Z-signed) | reality kept; `NonnegBounded` broken whenever coordinates of both signs are present (E6 witness); `OnesNormal` kept when Σ h ≠ 0 | no | ±1 phases only, and only under the conditions of §1.2 item 5. MC1 T4 shows that Z completes TU on registers [W, L] | no |
| C, complex | monomial, with unimodular ratios of prior coordinates as phases; S from the Fourier vector of a 4-cycle (E6.S-complex); n-th roots of unity from eigenvectors of n-cycles [W] | reality broken iff some h_x h̄_y is non-real, independently of Σ h (review C1b, C2: (1, i, 1) has Σ h ≠ 0 and breaks it); `OnesNormal` kept when Σ h ≠ 0 | no | yes, under the conditions of §1.2 item 5 | no |

**Countable or uncountable.**
- A fixed prior on a countable X, with countably many bijections and contexts, gives normalized entries from a
  countable ratio set, so the available level-one conjugations lie in countably many rays.
  - For finite X this is CR (N1 §2.1).
  - For countably infinite X, CR's P1 (finite configuration spaces, oa-node1:55) fails. The conclusion then goes
    through MC3 §2 corollary 3: `countable_not_pairFlowSourced` with a countable D.
- For single controlled steps of diagonal type, (v, x) ↦ (v, b^v x), uncountability needs both of the following [W; EC
  S2]:
  - a continuum of controlled bijections, for instance real couplings or continuous time;
  - a common eigenfunction.
- The second condition comes from rank one. Such a step gives a unitary channel iff the transported functions are
  proportional, i.e. ψ∘b⁻¹ = λψ.
  - S2a: on the circle with Lebesgue measure, ψ = e^{2πikx} and the controlled rotation (v, x) ↦ (v, x + vt mod 1)
    give exactly Ad diag(1, e^{−2πikt}) for every real t. This is a continuum of exact deterministic phases.
  - S2b, countercontrol: the real prior √2 cos 2πx gives the coherence factor cos 2πt. The Choi rank is 2 at t = 1/8,
    and the channel is unitary only at t ∈ ½ℤ, where t = ½ gives Ad Z.
  - S2c: ψ = 1, the KvN uniform prior, gives the identity at every t.
  - Within this class, a continuum of amplitude values without the eigen-relation gives mixtures, not unitaries.
- This uncountable family is a family of monomial unitaries. It lies outside CR and inside the monomial class, whose
  generated theory is not QM (`substratum_residual` StructuralClosure.lean:383, with `substratumClass` =
  `IsMonomial` :180, complex phases included).

***

## 2. Node Q2: the decisive check

### 2.1 No-go with κ2–κ4 kept [W; EC E4, E8, S2, S3]

**Statement.** Under κ1c–κ4, at any hidden cardinality, with any time model, coupling, setting or coherent prior, every
available one-outcome unitary channel on the visible token is conjugation by a monomial matrix.
- So no non-monomial unitary is available, not even one, and O-A (a) fails.
- It fails by monomiality, not by countability: at level one the mixing images `mixImage 1 θ`, θ ∈ (0, π/2), are not
  monomial.
- The question's conjecture holds in exact form. Coherence enters only through the overlaps ⟨ψ_{v₂→v₂′}, ψ_{v₁→v₁′}⟩,
  and support separation forces every rank-one overlap structure onto a monomial V.

**The continuous-time instance (S3) [EC].** Take node 3's moving-boundary flow (MC3 B2) with the coherent prior
ψ = √F e^{iα}, F a positive density and α = 5h² + 3h.
- The transported functions are built from the flow, and the Gram matrix is integrated from ψ directly. Every
  integrand pairs one source point with itself, so the hidden phase drops out, and the channel with this α equals the
  channel with α = 0 (S3a). A countercontrol pairing two distinct source points keeps the phase (S3e).
- With F = (π/2) sin πh, the flip probability is sin²(πT/2), the layer flow's (S3b).
- From |0⟩⟨0| the layer flow carries the coherence i sin(πT)/2, and the coherent-prior flow carries 0 (S3c).
- On |0⟩⟨1| the coherent-prior channel is the mixture of I and X, and differs from Ad R_x(π/2) (S3d).
- So a continuous-time bijective flow acting on a coherent hidden state reproduces the rooted law and still realizes
  the mixture.

This is the coherent analogue of MC3's cone lemma. Under κ1 mixed the maps lie in 𝒞(C). Under κ1c they leave 𝒞(C), but
their unitary channels stay in the monomial class.

### 2.2 A coherent-prior model that realizes the operations of A1 [W; EC S2a, S4, S5, S6; review O1–O3; L]

O-A is not reachable with κ4 kept, so the model drops κ4 at a single basis. **Model M\*:**
- (i) a hidden circle mode with the coherent prior ψ = e^{2πikx}, k ≠ 0;
- (ii) controlled rotations (v_j, x) ↦ (v_j, x + v_j t), t real, one for each token j. These are κ2-admissible
  real-coupled bijections;
- (iii) Lüders tests in the X basis only, the one-basis case of MC1's TU;
- (iv) the native class: permutations, CNOT, configuration readout, attach and discard.

**Steps.**
1. (i) and (ii) give R_z(θ) exactly and deterministically for every θ (S2a). The circle returns in a product state, so
   one mode serves every use (S6).
2. An X test on |0⟩, with Z = R_z(π) applied on outcome −, gives |+⟩ deterministically. R_z(π/2) then gives |+i⟩
   (review O1, O2).
3. With that ancilla, CNOT, an X-basis test and X on one outcome give R_x(π/2) exactly and deterministically (S4;
   review O3; the countercontrol O4 with the ancilla |+⟩ fails as it should).
4. Then R_x(π/2) R_z(θ) R_x(−π/2) = R_y(−θ) and H is reached exactly (S5). ZYZ products lie in SU(2), and every element
   of SU(2) is reached by the Euler-angle theorem [L].
5. With the native CNOT this gives every unitary on 2^k registers [L: Barenco et al. 1995], and A1 through
   `exactAll_iff_physical_general` (GeneralCarrier.lean:100), as in MC1 T4 [W].

So the A1 increment over A2, which MC2 §1.5 identifies as (a) together with (b), can be carried by a coherent
continuum prior. The non-classical content left on the test side is then one fixed basis. The test-basis continuum of
MC1 T1 is not needed. At the level of primitives this is the standard universality of {H, R_z(θ) for all θ} with CNOT.
MC2 shows A2 with three fixed bases; A2 with one or two bases is not shown.

**Literature for the mechanism [L].**
- Phase kickback from an eigenvector of a shift is standard. Its use as a phase reference is in Bartlett, Rudolph and
  Spekkens, Rev. Mod. Phys. 79, 555 (2007), and Kitaev, Mayers and Preskill, Phys. Rev. A 69, 052326 (2004).
- Reuse of a coherence reservoir is Åberg, "Catalytic coherence", Phys. Rev. Lett. 113, 150402 (2014). Its claim of
  undiminished reuse is disputed (Bedkihal, Vaccaro and Barnett, arXiv:1603.00003). In M\* the reference is an exact
  eigenfunction of each controlled step and returns in a product state (S6), which is the case where no degradation
  arises.
- Bibliographic data for Åberg were confirmed; the full text was not read.

**Maximum skepticism on this favourable branch.**
1. *Not standalone.* κ4 is still dropped. Without the added test the coherent prior supplies no non-monomial operation
   and no native statistic beyond |h|² (§1.2 items 2–3). It supplies the A1 increment only.
2. *Placement.* The circle is coupled coherently and at leading order to the visible token, so it belongs to the
   boundary layer.
   - Substratum.md:92 reads E3 as a Hilbert-space dimension cutoff on C_V × C_B, and admits an infinite sector only
     when it is decoupled, or coupled with slow dynamics at O(t/τ_B) [rec; MC3 N1].
   - A deep placement relayed through boundary bits makes the circle coupled at leading order, so it does not escape.
   - With a finite boundary layer, the coherent prior offers finitely many ratios h_x/h_y. The rays are countable, so
     by CR the result is not A1.
   - Under E3 as read, **M\* is excluded in OI's own terms.**
3. *Finiteness and recurrence.* M\* gives up total finiteness (Main.md:708 (ii)) and the finite order of φ (Main.md:139),
   and its real setting t is an uncountable context, so it gives up CR's P1 and P2.
4. *Sourcing.* The phase field is posited (§3).
5. *Exactness.* Each step is exact and finite. The A1 instrument assembly from exact unitaries is [W], as in MC1 T4
   and MC2 §2.4.

**Verdict on Q2.**
- With κ2–κ4 kept, a no-go: monomial unitaries only, at every cardinality.
- With κ4 dropped at one fixed basis, a continuum coherent eigenfunction prior realizes all A1 operations [W]. It needs
  a continuum in the coherently coupled sector, which E3 as read in Substratum.md:92 bars, and a posited phase field.

***

## 3. Node Q3: disguise (E0, G2) and the corpus texts

**Text checks (exact lines).**
- Main.md:60: "a realization … carries its own fixed hidden prior μ_H as part of the realization datum". It is a
  measure, and the swap example contrasts uniform with point-mass priors.
- Main.md:582 (unavoidable hidden predictive memory): "a bijection φ … with a hidden prior reproducing 𝒮". The
  posterior μ_p = P(H_t = · | …) is a probability law. The memory is classical (MC1 row 11 [rec]).
- Main.md:600 (canonical predictive quotient): the tail object's prior is "P itself at stage 0", and q_R "pushes the
  prior forward to P". It is a measure-level construction on classical hidden states.
- Main.md:602: it supplies "the substratum-level existence half". CDP uniqueness "is strictly stronger", and fiber
  freedom shows "completions here are not unique as wholes".
- SM.md:242 and Main.md:742 use the Koopman operator on real observables, never on a coherent state.

No corpus text derives or names a coherent hidden vector.

**Would a derived purification supply one? [EC E7; W]** The conclusion is scoped to purifications related by OI's
bijective purifier maps.
- E7a: the canonical purification Σ_x √μ_x |x⟩|x⟩_R with an untouched purifier gives exactly the mixed-prior channel,
  for all 24 bijections. Coherence between X and R is invisible at the description level as well as statistically.
- E7b: with the purifier acted on by bijections, the amplitudes are nonnegative, so the joint prior is form N.
  Nonnegativity holds, and all 576 rank-one cases fix the all-ones ray.
- E7c: a sign on the purifier changes the channel for 20 736 of 40 320 bijections. CDP purifications are unique up to
  a reversible map on the purifier, and a phase map is not a bijection. In OI's bijective class the phases are
  therefore extra data that purification does not fix.
- So a purification lift, if derived and related only by bijective purifier maps, gives the mixed or the N-form
  channels. It does not give the eigenfunction-type coordinates that (b) and §2.2 need (§1.2 item 5).

**Circularity [W; L].**
- In §2.2 the phase family is the posited field's own relative phase, ψ(x + t)/ψ(x) = e^{2πikt}. Positing ψ is
  positing a phase reference (§2.2, literature).
- No gate is posited, so E0's letter is kept. The posit carries the phase content verbatim, which fails G2.
- The choice of ψ (k, and the eigenfunction) is free, a G7 knob.
- By §1.2 item 2 no native protocol constrains the phase field at all.

**Verdict.** The coherent prior is a quantum resource state of the hidden sector, in disguise. No non-circular OI
reading is found.

***

## 4. Controls fixed in advance (§A.29), and their outcomes

Fixed before computing, for the candidate "κ1c with κ2–κ4", and for M\* where stated.

| # | control | outcome |
|---|---|---|
| 1 | `permTheory_not_qm` (SubstratumInterfaceAudit.lean:716) and the monomial class (`substratum_residual`) stay non-QM | holds. With κ1c–κ4 every unitary channel is monomial, so H is unavailable and the theory is not QM. With the addition removed the theory is `permTheory` (`obsTheory_eq_permTheory` :774) |
| 2 | K_B, K(Z_F) and Γ(Q3) excluded by the candidate itself | **fails.** Under κ4 there are no non-configuration tests (§1.2 item 1), and the Σ3 exclusions need them (LG §4.5 item 2). M\* reaches full control, but O-B then reduces to X-4 and X-5 with G3, which are unsourced (MC2 §3) |
| 3 | rooted law (`finiteRootedRealizable_iff_pper` RootedClassificationAllTime.lean:192) and M1 on retained protocols | holds exactly. By §1.2 item 2 every native protocol's law under h equals its law under the mixed prior \|h\|², so the class of rooted laws is unchanged and retained protocols are unaffected. In M\* the controlled rotation is a κ2 process whose native statistics are those of the uniform prior (S8). The control holds because the coherence is idle on native protocols |
| 4 | `fixedGateTheory_not_qm` (DiscreteCompletion.lean:1948) survives | holds trivially: no completion rule is added |
| 5 | no E0 positing | holds in letter, since a state and not an operation is posited. **Fails in substance (G2):** the phase field carries the phase family (§3) |
| 6 | names the κ and the CR premises given up | κ1. M\* also gives up κ4 at one basis, P1 (a continuum hidden mode) and P2 (real settings) |
| 7 | must-fail: κ1c–κ4 yields no non-monomial unitary channel | holds (E4, E8). Countercontrols E9a–c: a Hadamard step before the bijection makes Kraus operators non-row-monomial (E9b); an X-basis test gives a non-diagonal effect (E9c); a Hadamard step followed by configuration readout, equivalently an X-basis test, makes the coherent prior statistically visible: P(1) = 1 against ½ (E9a). E9a–c run on separate code from E1–E3. The review's mutations R5a–c show that the checkers E1–E3 use (`row_monomial_tags`, the E3 comparison, `effect`) fail on bad inputs |

The candidate fails controls 2 and 5. It does not survive as a complete component. As the (b) component, or as the
A1 increment in M\*, it passes 1, 3, 4 and 7, and fails 5.

***

## 5. G6: independent prediction

- **Under κ2–κ4: none is possible from native protocols.** By §1.2 item 2 the coherent prior is statistically
  equivalent to the mixed prior |h|² on every native protocol. A deviation can appear only in a protocol with a
  non-native test or process (E9a).
- **M\*:** with the added test its visible statistics are exactly those of QM. It predicts nothing beyond QM, and
  nothing beyond OI's mixed-prior law on native protocols.
- **The E3-compliant finite version:**
  - its exact deterministic phases are confined to a finite set of ratios of boundary-layer amplitudes, and other
    phases are reached only approximately;
  - at finite experimental precision this is not testable;
  - the resolution scale is adjustable through the boundary dimension;
  - so it is a variant adjustable to fit any outcome, rejected under §A.29.
- **Decision rule: none found. G6 stays open.**

***

## 6. Hidden-assumption watch

| # | assumption | where | finding |
|---|---|---|---|
| HA-K1 | the mixed reading of κ1 is load-bearing | MC3 §2 ("the mixed reading of κ1 is load-bearing") | **scoped.** MC3's claim concerns availability (the cone 𝒞(C)), and it stands. The mixed reading carries no native statistical content: under κ2–κ4 native data depend on h only through \|h\|² (§1.2 item 2), the dephasing-covariance fact of [L]. Any phase field of a coherent h with \|h\|² = μ_H is unconstrained by native protocols |
| HA-K2 | a coherent prior brings interference into the visible sector | question framing | **exposed**: amplitudes are transported, never added (§1.1). Interference needs κ2 or κ4 dropped (E9a) |
| HA-K3 | uncountability needs a continuum of hidden amplitudes | question framing | **scoped**, for single controlled steps of diagonal type: one eigenfunction with a continuum of controlled bijections suffices (S2a). A continuum of amplitude values without the eigen-relation gives no unitary there (S2b) |
| HA-K4 | the purification lift could make a coherent prior derivable | Main.md:600–602 | **refuted** for the canonical purification and purifier maps that are bijections (E7a, E7b). The purifier phase is free data (E7c) |
| HA-K5 | the classical-enlargement escape is empty (MC3 §7) | MC3 HA-E1 | **scoped** to κ1 mixed, as MC3 K1 and C1 already indicate. Under κ1c, enlargement to a continuum gives an uncountable family of exact phases (S2a), all monomial |
| HA-K6 | A1 availability tracks what native tests can see | `ExactAllFiniteEndomorphicQuantumOps` | BORDERLINE (definitional). Under κ1c–κ4, Ad Z is available as a one-outcome family, yet no native test distinguishes it from the identity, because effects are diagonal and Z commutes with them |
| HA-K7 | zero uniform weight of the prior suffices for a deterministic phase | MC1 §4 2(ii) and MC3 C1 (the \|−⟩ instances) | **refuted**: necessary for h ∈ ℓ¹, not sufficient ((2, −1, −1), review R2). An eigen-relation under a hidden bijection suffices (§1.2 item 5) |

Assumption-watch markers:
- **AW-MC4-1.** Dropping κ1 alone (a coherent prior with κ2–κ4) reaches only monomial unitary channels and diagonal
  effects, at every hidden cardinality and time model. A coherent-prior source for (a) must also drop κ2 or κ4.
- **AW-MC4-2.** On native protocols a coherent prior h and the mixed prior |h|² give identical laws. A claim that a
  coherent prior has observable content must name the non-native test at which it differs.
- **AW-MC4-3.** A continuum of exact deterministic phases from a coherent prior needs a continuum hidden mode coupled
  coherently at leading order. E3 as read in Substratum.md:92 bars that in the boundary layer.
- **AW-MC4-4.** For h ∈ ℓ¹, a deterministic ray-moving phase from a coherent prior needs Σ h = 0 and (countable X) two
  coordinates of equal modulus and distinct phase; an eigen-relation h∘σ⁻¹ = λh, λ ≠ 1, suffices. Purifications of the mixed prior
  with nonnegative amplitudes, related by bijective purifier maps, never supply one.

***

## 7. The form of the missing component, as refined

The first clause of PLAN's form statement gains a scope sentence. Neither added condition is claimed sufficient
(§A.34):

> - κ1 dropped alone (a coherent hidden prior with κ2–κ4) yields only monomial unitary channels and diagonal effects,
>   and no native statistic beyond the mixed prior |h|². For (a) a coherent prior has to be paired with κ2 or κ4
>   dropped. For (b), zero uniform weight of the prior is necessary (h ∈ ℓ¹) but not sufficient; an eigen-relation
>   h∘σ⁻¹ = λh with λ ≠ 1 under a hidden bijection σ suffices, by a single controlled step [W]. A coherent eigenfunction on a continuum hidden mode,
>   under real-coupled controlled flows, supplies a continuum of exact phases; with one fixed non-configuration test
>   basis it carries both A1 increments [W]. It needs a continuum in the coherently coupled sector, which E3 as read in
>   Substratum.md:92 bars, and a posited phase field (G2) (missing-component node `mc-node4`).

***

## 8. Not verified

- The transport lemma is [W]. Its continuum form (support separation for weighted composition operators) and the ones
  identity for whole protocols are written, not formalized. The kernel has no coherent-prior or infinite-carrier
  object.
- The exhaustive checks cover |C| = 2 with |X| ≤ 4. Two-step protocols are a deterministic subsample (12 221
  protocols per prior), not exhaustive. Visible ancillas are exercised only in the review's R4 (1 600 two-step
  protocols).
- The invariant conditions in the §1.3 table ("broken whenever", "iff some h_x h̄_y is non-real") are [W], with the
  exact instances cited there.
- The sufficient condition of §1.2 item 5 is proved by a single controlled step [W], with exact instances. No condition that is both necessary
  and sufficient is given.
- The OnesNormal step "1 ∈ span{K^H 1} ⟹ `OnesNormal`" is taken from MC1 T2 and its review [rec].
- M\*'s register step rests on [L] Barenco et al. and the Euler-angle theorem. Its A1 conclusion is [W] through
  `exactAll_iff_physical_general`, as in MC1 T4. The instrument assembly from exact unitaries is not re-derived.
- The E3 placement argument (§2.2 item 2) relies on Substratum.md:92 as read in MC3 N1 [rec]. Whether a coherently
  coupled continuum could be relayed through a finite boundary at leading order without counting as boundary layer is
  [W].
- The literature is cited, not re-derived. Bibliographic data were confirmed for every item cited in §1.2 item 2 and
  §2.2; the full texts were not read.
- S2 uses SymPy integration on the circle for the stated ψ only. S3 uses one density F, one phase α, and region
  boundaries read at T = 1/3, with T symbolic in the integrals.
- [rec] rows (MC1, MC2, MC3, LG) were taken as recorded.
- The first double run of `coherent_enum.py` failed E9b. Its countercontrol placed the Hadamard after the swap, where
  it acts on one column of each Kraus operator and leaves every row with a single entry, so the control was vacuous.
  The check places the Hadamard before the bijection, where it mixes two input columns. Both final runs are
  byte-identical.

***

## 9. Files (`probe/`)

| file | role |
|---|---|
| `coherent_enum.py` | blocks E1–E9: exhaustive enumeration in exact Gaussian rationals, pure Python; Python 3.13.16, `-I -B` |
| `coherent_enum.run1.out`, `coherent_enum.run2.out` | 52 PASS, 0 FAIL; byte-identical |
| `coherent_exact.py` | blocks S1–S8: symbolic checks; SymPy 1.14.0, Python 3.13.16, `-I -B` |
| `coherent_exact.run1.out`, `coherent_exact.run2.out` | 15 PASS, 0 FAIL; byte-identical |
| `SHA256SUMS` | digests of the six files |
| `review/rev_mc4.py`, `review/rev_mc4.out` | independent review, copied unchanged: R1 (separate Ad_U-plus-partial-trace path), R2/R2b (zero uniform weight not sufficient; eigenvector control), R3, R4 (visible ancillas), R5a–c (mutations of the author's checkers); 11 PASS. Run as `python3 -I -B rev_mc4.py <probe dir>` |
| `review/rev_mc4_onebasis.py`, `review/rev_mc4_onebasis.out` | review: one X basis suffices for M\* (O1–O3), countercontrol O4; 4 PASS |
| `review/rev_mc4_rowC.py`, `review/rev_mc4_rowC.out` | review: row C conditions (C1, C1b, C2); 3 PASS. Run with the review directory as argument |
| `review/SHA256SUMS` | digests of the six review files |

***

## 10. Productivity verdict

**Gem: yes, narrow.** Facts strictly stronger than "a coherent prior is a non-classical posit":
1. **No-go.** With κ2–κ4 kept, a coherent prior of any form, at any cardinality and with any time model, gives only
   monomial unitary channels and diagonal effects. It never supplies (a). The uncountable phase family that a continuum
   eigenfunction gives stays inside the monomial class.
2. **Conditions for (b).** For h ∈ ℓ¹, a deterministic ray-moving phase needs Σ h = 0 and two coordinates of equal
   modulus and distinct phase. Zero uniform weight alone is not sufficient. An eigen-relation under a hidden bijection
   is sufficient. This constrains the form (§7, AW-MC4-4).
3. **Statistical equivalence.** Under κ2–κ4, every native protocol's law under a coherent prior h equals its law under
   the mixed prior |h|². Any G6 for a coherent-prior candidate must therefore live on non-native tests (AW-MC4-2).
4. **Relocation, with its price.** With κ4 dropped at one fixed basis, a continuum coherent eigenfunction prior carries
   both A1 increments [W]. That placement needs a continuum in the coherently coupled sector, which E3 as read bars, and
   a posited phase field that no native protocol constrains.
5. The canonical purification, with bijective purifier maps, does not produce the needed coherent prior (E7).

**Classification: ELABORATING overall, with a BORDERLINE item at most.**
- Item 1 is LG's monomial-branch lemma (LEDGER.md:116–123) applied to an unread hidden preparation, with MC3's C1
  identification, extended to any hidden cardinality and to Koopman dynamics: ELABORATING.
- Item 3 is the immediate corollary of LEDGER.md:116–123 and the dephasing-covariance fact of coherence theory [L]:
  ELABORATING. HA-K1 scopes MC3 rather than exposing a new assumption.
- Item 4 is the continuous generalization of MC3's C1, assembled as in MC1 T4. At the primitive level it is the
  standard universality of an uncountable monomial primitive with one fixed basis ({H, R_z(θ)} with CNOT) [L].
  BORDERLINE at most, for the refinement that places the A1 increment in the prior at the cost of E3.
- Items 2 and 5, and HA-K5 and HA-K7: ELABORATING.
- §3's text checks: CONFIRMING (MC2 §3, MC3 §6).
- G6: none found. A source for O-B is not supplied.

***

## Review outcome

Independent review: `probe/review/` (`rev_mc4.py`, 11 PASS; `rev_mc4_onebasis.py`, 4 PASS; `rev_mc4_rowC.py`, 3 PASS;
outputs and `SHA256SUMS` copied unchanged from the reviewer's working copy, each replayed byte-identical from
`probe/review/` against this probe). Verdict: accept with notes. The notes are
applied in place above.

| item | verdict | applied as |
|---|---|---|
| zero uniform weight as the criterion for (b) | CORRECTED | necessary only, for h ∈ ℓ¹; sufficient condition an eigen-relation; equal-modulus distinct-phase pair added as a necessary condition; §1.2 item 5, §1.3 rows R and C, §7, AW-MC4-4, HA-K7 |
| minimality of M\* | CORRECTED | one X basis suffices (review O1–O3); "A2-type" removed; A2 shown by MC2 with three bases only |
| classification | CORRECTED | ELABORATING overall, BORDERLINE at most for the relocation; dephasing-covariance and reference-frame literature added [L]; HA-K1 recast as a scoping of MC3 |
| S3 tag | CORRECTED | S3 computes the Gram matrix from ψ and the flow, with countercontrol S3e |
| CR scope for countably infinite X | CORRECTED | through MC3 §2 corollary 3 |
| ℓ¹ requirement; eigenfunction scope; nonsingular bijections; Euler step; E7 scope; LG ref | CORRECTED | as stated in §0, §1.2, §1.3, §2.2, §3 |
| E1, E3, E8, S1 as instances; E9 code path | CORRECTED | marked as instances, review R1 cited; E9 separate code noted, review R5a–c cited |
| transport lemma, no-go, statistical equivalence, controls | CONFIRMED | — |
