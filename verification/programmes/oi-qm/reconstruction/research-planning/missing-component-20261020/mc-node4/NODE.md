# Node 4: the coherent hidden prior as a candidate source at A1

Research only, consistency axis (§A.23). F2 stays A1 (exact finite operational QM on qubit-power registers). No
premise adopted, no status changed, nothing written to `main`.

**Base.** `main` = `809fa9d6`. `papers/` and `verification/lean-mathlib/` are identical between `df9e601e` and
`809fa9d6` (`git diff --quiet`), so paper lines (Main.md:n, Substratum.md:n, SM.md:n) and Lean lines hold at both.
Every [AT] name was confirmed by `git grep` of its declaration at `809fa9d6`; Lean paths are under
`verification/lean-mathlib/OIBridge/`. N1 = `../oa-node1/NODE.md`, MC1 = `../mc-node1/NODE.md` (with node 1b, §9),
MC2 = `../mc-node2/NODE.md`, MC3 = `../mc-node3/NODE.md`, PLAN = `../PLAN.md`, all with their review outcomes. LG =
`f2-ledger-20261020/LEDGER.md`.

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
- **κ2.** Processes are bimeasurable bijections of C × X, with any time index, real coupling or setting (MC3 §2). They
  act on vectors by their Koopman operators: permutation operators for countable X, composition operators on L².
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

**Continuum form [W].** A Koopman (weighted composition) operator maps |v⟩ ⊗ L²(X) into ⊕_{v′} |v′⟩ ⊗ L²(A_{v,v′}).
For fixed v′, the sets A_{v,v′} are pairwise disjoint over v, since they are images of disjoint sets under a bijection.
Products with visible configuration projectors keep this support separation. The visible map is then

  ρ ↦ Σ ρ_{v₁v₂} ⟨ψ_{v₂→v₂′}, ψ_{v₁→v₁′}⟩ |v₁′⟩⟨v₂′|,

and for fixed v′ the transported functions ψ_{v→v′} have disjoint supports. **Amplitudes are transported, never
added:** no configuration ever receives two amplitudes.

This is LG's monomial-branch lemma (LEDGER.md:116–123: "coherent preparations do not give coherent control") applied
to a hidden preparation that is never read. MC3's C1 row already identifies a non-distribution hidden state with a
coherent preparation. The lemma extends that identification to every hidden cardinality and to Koopman dynamics.

**Checks [EC].**
- E1: every bijection at |X| = 3 (720) and |X| = 4 (40 320) gives row-monomial Kraus operators with single-amplitude
  entries.
- E8: 12 221 two-step protocols with a visible readout and feed-forward, under the signed and Fourier priors, give the
  same.
- S1: the symbolic prior (h₀, h₁, h₂) over all 720 bijections at |X| = 3.

### 1.2 Corollaries

1. **Effects are diagonal [W; EC E2, S1b].** Row-monomiality makes K^H K diagonal, so no non-configuration test
   arises, sharp or unsharp.
2. **Native statistics are those of the mixed prior |h|² (statistical equivalence) [W; EC E3, E8, S1a].**
   - Take a protocol started in configuration states. Each branch amplitude is W|c⟩ ⊗ |h⟩ = Σ_x h_x W|c, x⟩, and the
     vectors W|c, x⟩ are distinct basis vectors or zero. Every outcome probability is therefore Σ_{x ∈ A} |h_x|² for
     a set A that the protocol fixes. In the continuum it is ∫_A |ψ|² dμ.
   - E3 checks this for all 40 320 bijections under six priors. S1a checks it symbolically: the probabilities are
     polynomials in h_x h̄_x alone, with no cross terms.
   - Visible states reached by earlier protocol steps are covered, since such steps are part of the protocol.
3. **One-outcome unitary channels are monomial [W; EC E4, E4r].**
   - conj(V) has a rank-one Choi matrix, so every Kraus operator is ∝ V. An invertible row-monomial matrix is
     monomial.
   - The entries of V, normalized, are ratios h_x/h_y of prior coordinates (E4r).
   - Non-unitary V with conj V available are ∝ a row-monomial K as well, which is what `hmem` of
     `countable_not_pairFlowSourced` (PairFlowEquivalence.lean:218) quantifies over.
4. **The ones identity [W; EC E5].** Σ_{x′} K_{x′}^H 1 = (Σ_x h̄_x)·1 for every bijection. For a whole protocol the
   same holds, because each column of the joint operator lies in exactly one branch [W]. A uniform visible discard
   needs the kernel's weight splitting (`instAvail_onesNormal` InstrumentRealization.lean:313).
   - If Σ_x h_x ≠ 0, 1 lies in the span of the K^H 1. The family is then `OnesNormal` after splitting (MC1 T2 [rec]),
     and every available unitary fixes the all-ones ray (`instAvail_unitary_fixes_ones` InstrumentRealization.lean:398;
     E4b on four priors).
   - **A ray-moving deterministic phase requires hidden amplitudes of zero uniform weight, Σ_x h_x = 0**, over the
     coordinates the protocol uses. The KvN vector √μ never has this property.

### 1.3 The three forms

| form | unitary channels (κ2–κ4) | invariants | (a) continuum of non-monomial operations | (b) deterministic phase | (c) toward O-B |
|---|---|---|---|---|---|
| N, √μ (KvN) | permutations only (E4, E6) | `OnesNormal`, `NonnegBounded` and reality kept (E6) | no | no | coherent nonnegative states are reachable (MC3 K1); effects diagonal |
| R, signed | signed permutations; Z when Σ h = 0 (E6.Z-signed); never S | reality kept; `NonnegBounded` broken (E6 witness); `OnesNormal` broken iff Σ h = 0 | no | yes, ±1 only. MC1 T4 shows that Z completes TU on registers [W, L] | no |
| C, complex | monomial with phases from ratios of prior coordinates; S from the Fourier vector of a 4-cycle (E6.S-complex); n-th roots of unity from n-cycles [W] | all three broken when Σ h = 0 | no | yes | no |

**Countable or uncountable.**
- A fixed prior on a countable X, with countably many bijections and contexts, gives entries from a countable ratio
  set. The rays are then countable, CR's P1–P3 hold (N1 §2.1), and `countable_not_pairFlowSourced` applies.
- Uncountability needs both of the following [W; EC S2]:
  - a continuum of controlled bijections, for instance real couplings or continuous time;
  - a common eigenfunction.
- The second condition comes from rank one. A controlled step b gives a unitary channel iff the transported functions
  are proportional, i.e. ψ∘b⁻¹ = λψ on the relevant support.
  - S2a: on the circle with Lebesgue measure, ψ = e^{2πikx} and the controlled rotation (v, x) ↦ (v, x + vt mod 1)
    give exactly Ad diag(1, e^{−2πikt}) for every real t. This is a continuum of exact deterministic phases.
  - S2b, countercontrol: the real prior √2 cos 2πx gives the coherence factor cos 2πt. The Choi rank is 2 at t = 1/8,
    and the channel is unitary only at t ∈ ½ℤ, where t = ½ gives Ad Z.
  - S2c: ψ = 1, the KvN uniform prior, gives the identity at every t.
  - A continuum of amplitude values without the eigen-relation therefore gives mixtures, not unitaries.
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

**The continuous-time instance (S3).** Take node 3's moving-boundary flow (MC3 B2) with the coherent prior
ψ = √f e^{iα}, α arbitrary.
- Every Kraus operator is a scalar function times I or X, and the hidden phase cancels pointwise: |ψ|² = f (S3a).
- The channel equals the mixed-prior channel. The flip probability is sin²(πT/2), the layer flow's (S3b).
- From |0⟩⟨0| the layer flow carries the coherence i sin(πT)/2, and the coherent-prior flow carries 0 (S3c, S3d).
- So a continuous-time bijective flow acting on a coherent hidden state reproduces the rooted law and still realizes
  the mixture.

This is the coherent analogue of MC3's cone lemma. Under κ1 mixed the maps lie in 𝒞(C). Under κ1c they leave 𝒞(C), but
their unitary channels stay in the monomial class.

### 2.2 The minimal coherent-prior model that realizes the operations of A1 [W; EC S2a, S4, S5, S6; L]

O-A is not reachable with κ4 kept, so the minimal model drops κ4 as little as possible. **Model M\*:**
- (i) a hidden circle mode with the coherent prior ψ = e^{2πikx}, k ≠ 0;
- (ii) controlled rotations (v_j, x) ↦ (v_j, x + v_j t), t real, one for each token j. These are κ2-admissible
  real-coupled bijections;
- (iii) Lüders tests in the X and Y bases only, the two-basis case of MC1's TU;
- (iv) the native class: permutations, CNOT, configuration readout, attach and discard.

**Steps.**
1. (i) and (ii) give R_z(θ) exactly and deterministically for every θ (S2a). The circle returns in a product state, so
   one mode serves every use (S6).
2. (iii) and (iv) give R_x(π/2) exactly and deterministically (S4: Y-test preparation of |+i⟩, CNOT, X-basis test, X
   on one outcome).
3. Then R_x(π/2) R_z(θ) R_x(−π/2) = R_y(−θ), the ZYZ products give SU(2), and H is reached exactly (S5).
4. With the native CNOT this gives every unitary on 2^k registers [L: Barenco et al. 1995], and A1 through
   `exactAll_iff_physical_general` (GeneralCarrier.lean:100), as in MC1 T4 [W].

So the A1 increment over A2, which MC2 §1.5 identifies as (a) together with (b), can be carried by a coherent
continuum prior. The non-classical content left on the test side is then two fixed bases, an A2-type resource (MC2
§1.3). The test-basis continuum of MC1 T1 is not needed.

**Maximum skepticism on this favourable branch.**
1. *Not standalone.* κ4 is still dropped. Without the added tests the coherent prior supplies no non-monomial operation
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
- With κ4 dropped to two fixed bases, a continuum coherent eigenfunction prior realizes all A1 operations [W]. It needs
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

**Would a derived purification supply one? [EC E7; W]**
- E7a: the canonical purification Σ_x √μ_x |x⟩|x⟩_R with an untouched purifier gives exactly the mixed-prior channel,
  for all 24 bijections. Coherence between X and R is invisible at the description level as well as statistically.
- E7b: with the purifier acted on, the amplitudes are nonnegative, so the joint prior is form N. Nonnegativity holds,
  and all 576 rank-one cases fix the all-ones ray.
- E7c: a sign on the purifier changes the channel for 20 736 of 40 320 bijections. CDP purifications are unique up to
  a reversible map on the purifier, and a phase map is not a bijection. In OI's bijective class the phases are
  therefore extra data that purification does not fix.
- So a purification lift, if derived, gives the mixed or the N-form channels. It does not give the zero-uniform-weight
  vectors or eigenfunction phases that (b) and §2.2 need.

**Circularity [W; L].**
- In §2.2 the phase family is the posited field's own relative phase, ψ(x + t)/ψ(x) = e^{2πikt}. Positing ψ is
  positing a phase reference.
  - This is the reference-frame resource reading [L: Bartlett, Rudolph and Spekkens, Rev. Mod. Phys. 79 (2007) 555;
    Kitaev, Mayers and Preskill, Phys. Rev. A 69 (2004) 052326].
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
| 6 | names the κ and the CR premises given up | κ1. M\* also gives up κ4 at two bases, P1 (a continuum hidden mode) and P2 (real settings) |
| 7 | must-fail: κ1c–κ4 yields no non-monomial unitary channel | holds (E4, E8). Countercontrols: a Hadamard step before the bijection makes the Kraus operators non-row-monomial (E9b); an X-basis test gives a non-diagonal effect (E9c); a Hadamard step followed by configuration readout, equivalently an X-basis test, makes the coherent prior statistically visible: P(1) = 1 against ½ (E9a) |

The candidate fails controls 2 and 5. It does not survive as a complete component. As the (b) component, or as the
A1 increment in M\*, it passes 1, 3, 4 and 7, and fails 5.

***

## 5. G6: independent prediction

- **Under κ2–κ4: none is possible from native protocols.** By §1.2 item 2 the coherent prior is statistically
  equivalent to the mixed prior |h|² on every native protocol. A deviation can appear only in a protocol with a
  non-native test or process (E9a).
- **M\*:** with the added tests its visible statistics are exactly those of QM. It predicts nothing beyond QM, and
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
| HA-K1 | the mixed reading of κ1 carries empirical content | Main.md:60; MC3 §2 ("the mixed reading of κ1 is load-bearing") | **exposed**: under κ2–κ4 it carries none. Native statistics fix \|h\|² only (§1.2 item 2). The mixed reading is load-bearing for description-level availability (the cone 𝒞(C), the phase channels) and for nothing a native test sees. The data determine Main.md:60's μ_H, and leave any phase field of a coherent h with \|h\|² = μ_H unconstrained |
| HA-K2 | a coherent prior brings interference into the visible sector | question framing | **exposed**: amplitudes are transported, never added (§1.1). Interference needs κ2 or κ4 dropped (E9a) |
| HA-K3 | uncountability needs a continuum of hidden amplitudes | question framing | **scoped**: one eigenfunction with a continuum of controlled bijections suffices (S2a). A continuum of amplitude values without the eigen-relation gives no unitary (S2b) |
| HA-K4 | the purification lift could make a coherent prior derivable | Main.md:600–602 | **refuted** for the canonical purification (E7a, E7b). The purifier phase is free data (E7c) |
| HA-K5 | the classical-enlargement escape is empty (MC3 §7) | MC3 HA-E1 | **scoped** to κ1 mixed, as MC3 K1 and C1 already indicate. Under κ1c, enlargement to a continuum gives an uncountable family of exact phases (S2a), all monomial |
| HA-K6 | A1 availability tracks what native tests can see | `ExactAllFiniteEndomorphicQuantumOps` | BORDERLINE (definitional). Under κ1c–κ4, Ad Z is available as a one-outcome family, yet no native test distinguishes it from the identity, because effects are diagonal and Z commutes with them |

Assumption-watch markers:
- **AW-MC4-1.** Dropping κ1 alone (a coherent prior with κ2–κ4) reaches only monomial unitary channels and diagonal
  effects, at every hidden cardinality and time model. A coherent-prior source for (a) must also drop κ2 or κ4.
- **AW-MC4-2.** On native protocols a coherent prior h and the mixed prior |h|² give identical laws. A claim that a
  coherent prior has observable content must name the non-native test at which it differs.
- **AW-MC4-3.** A continuum of exact deterministic phases from a coherent prior needs a continuum hidden mode coupled
  coherently at leading order. E3 as read in Substratum.md:92 bars that in the boundary layer.
- **AW-MC4-4.** A deterministic ray-moving phase from a coherent prior needs hidden amplitudes of zero uniform weight.
  Purifications of the mixed prior with nonnegative amplitudes never supply them.

***

## 7. The form of the missing component, as refined

The first clause of PLAN's form statement gains a scope sentence. Neither added condition is claimed sufficient
(§A.34):

> - κ1 dropped alone (a coherent hidden prior with κ2–κ4) yields only monomial unitary channels and diagonal effects,
>   and no native statistic beyond the mixed prior |h|². For (a) a coherent prior has to be paired with κ2 or κ4
>   dropped. A coherent prior of zero uniform weight supplies (b) deterministically. A coherent eigenfunction on a
>   continuum hidden mode, under real-coupled controlled flows, supplies a continuum of exact phases; with two fixed
>   non-configuration test bases it carries both A1 increments [W]. It needs a continuum in the coherently coupled
>   sector, which E3 as read in Substratum.md:92 bars, and a posited phase field (G2) (missing-component node `mc-node4`).

***

## 8. Not verified

- The transport lemma is [W]. Its continuum form (support separation for weighted composition operators) and the ones
  identity for whole protocols are written, not formalized. The kernel has no coherent-prior or infinite-carrier
  object.
- The exhaustive checks cover |C| = 2 with |X| ≤ 4. Two-step protocols are a deterministic subsample (12 221
  protocols per prior), not exhaustive. Visible ancillas beyond the token are not exercised.
- The OnesNormal step "1 ∈ span{K^H 1} ⟹ `OnesNormal`" is taken from MC1 T2 and its review [rec].
- M\*'s register step rests on [L] Barenco et al. Its A1 conclusion is [W] through `exactAll_iff_physical_general`,
  as in MC1 T4. The instrument assembly from exact unitaries is not re-derived.
- The E3 placement argument (§2.2 item 2) relies on Substratum.md:92 as read in MC3 N1 [rec]. Whether a coherently
  coupled continuum could be relayed through a finite boundary at leading order without counting as boundary layer is
  [W].
- The reference-frame literature is cited, not re-derived.
- S2 uses SymPy integration on the circle for the stated ψ only. S3 uses one prior shape f and one phase α, with
  T symbolic.
- [rec] rows (MC1, MC2, MC3, LG) were taken as recorded.
- The first double run of `coherent_enum.py` failed E9b. Its countercontrol placed the Hadamard after the swap, where
  it acts on one column of each Kraus operator and leaves every row with a single entry, so the control was vacuous.
  The check now places the Hadamard before the bijection, where it mixes two input columns. Both final runs are
  byte-identical.

***

## 9. Files (`probe/`)

| file | role |
|---|---|
| `coherent_enum.py` | blocks E1–E9: exhaustive enumeration in exact Gaussian rationals, pure Python; Python 3.13.16, `-I -B` |
| `coherent_enum.run1.out`, `coherent_enum.run2.out` | 52 PASS, 0 FAIL; byte-identical |
| `coherent_exact.py` | blocks S1–S8: symbolic checks; SymPy 1.14.0, Python 3.13.16, `-I -B` |
| `coherent_exact.run1.out`, `coherent_exact.run2.out` | 14 PASS, 0 FAIL; byte-identical |
| `SHA256SUMS` | digests of the six files |

***

## 10. Productivity verdict

**Gem: yes, narrow.** Facts strictly stronger than "a coherent prior is a non-classical posit":
1. **Statistical equivalence.** Under κ2–κ4, every native protocol's law under a coherent prior h equals its law under
   the mixed prior |h|² [W; EC]. The mixed/coherent split of κ1 has no native statistical content. Any G6 for a
   coherent-prior candidate must live on non-native tests. This exposes HA-K1 and HA-K2 and constrains the form
   (AW-MC4-2).
2. **No-go.** With κ2–κ4 kept, a coherent prior of any form, at any cardinality and with any time model, gives only
   monomial unitary channels. It supplies (b), which needs zero uniform weight, and never (a). The uncountable phase
   family a continuum eigenfunction gives stays inside the monomial class.
3. **Relocation, with its price.** With κ4 dropped only to two fixed bases, a continuum coherent eigenfunction prior
   carries both A1 increments [W]. The continuum of MC1 T1 can sit in the prior instead of the test bases. That
   placement needs a continuum in the coherently coupled sector, which E3 as read bars, and a posited phase field that
   no native protocol constrains. This constrains the form (§7).
4. The canonical purification does not produce the needed coherent prior (E7). HA-K4 is refuted.

**Classification: NEW (narrow).**
- NEW: item 1, an immediate corollary of the row-monomial form that no record states; and item 3's relocation and
  placement cost.
- ELABORATING: item 2. It is LG's monomial-branch lemma (LEDGER.md:116–123) applied to an unread hidden preparation,
  with MC3's C1 identification, extended to any hidden cardinality and to Koopman dynamics.
- ELABORATING: item 4 and HA-K5.
- CONFIRMING: §3's text checks (MC2 §3, MC3 §6).
- G6: none found. A source for O-B is not supplied.
