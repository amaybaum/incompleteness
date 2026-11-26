# OI-QM-APPROX-1, unit 2 (G3-D14): report, revision r3

Revision r3 of the writer's report. It applies the five findings of the focused delta review of r2 (PR #1584 comment 7185177023, verdict ACCEPT WITH NITS) under the owner decision at #1169 c.7186638587 (amaybaum, 2026-11-26T08:28:18Z, item 7). r2 (`REPORT-r2.md`, commit `f257597b`) applied the first independent review (PR #1584 comment 7184945033, verdict REVISE, minor) under the owner decision at #1169 c.7185038641 (amaybaum, decision time 2026-11-26T07:02:13Z, "Lane 3" and section 2). The decision of 2026-11-26T08:28:18Z confirms the values the earlier record lost: the bound 288ε for ε ≤ 1/64, which the bound here implies, and the negative cases m = 1 and K = 1, subject to verification of their proofs. The change map is `CHANGES-r3.md`.

The following are unchanged from `PLAN.md` (committed as `d2fd361e`) and are not restated: the preregistered questions, the setting, the metrics M_H and M_C, the horizon (exactly K), the δ-forms V_δ, L_δ, I_δ, U_δ, C_δ, the notation C_δ[M, Λ], the productivity test and the stopping rule.

Pinned source: `origin/main` = `b6c6b80bbd4a878452e54759cc85f16c9ffb72da`; "OB/" = `verification/lean-mathlib/OIBridge/`. Every result below is this unit's paper argument [A], unless another label is given; beyond the two reviews cited it is unreviewed. No computation was run. Nothing here is adopted, promoted or proposed for the manuscripts.

## 0. Results

| ID | Question | Metric | Status | Where |
| --- | --- | --- | --- | --- |
| Q0 | δ-forms without imported quantum structure | none | Passed, relative to the given kinematics. The δ-forms for every δ > 0 do not imply the exact conditions (§1.3). | §1 |
| Q1 | Direction 1: C_δ ⇒ closeness of laws | M_C, hence M_H | Proved at fixed (d, m, K), with an explicit ε(δ, d, m, K), for d = 2 and for general d. | §3 |
| Q2-H | Direction 2 | M_H | Disproved. Counterexample: M_H = 0 at every level and for every (m, K), while I_δ fails for every δ < 1/2. | §4.1 |
| Q2-C | Direction 2 | M_C | Proved for m ≥ 2, K ≥ 2 when the metric covers every level the δ-forms reference, with δ(ε) = 184(N_Λ+1)ε. Disproved for m = 1 (any K) and for K = 1 (any m). A metric that omits a level L ≥ 2 does not bound U_δ at L. | §4.2–§4.4 |
| Cor | Both directions | M_C | For m ≥ 2, K ≥ 2 and all levels, three statements are equivalent: C_δ[m] for every δ > 0; M_C = 0; each availability set (at most m outcomes) lies in the quantum instruments and has them as its closure. The restriction m, K ≥ 2 is necessary for (b) ⇒ (a). | §5 |

Productivity verdict: gem (§7). The verdict rests on Theorem 4 (M_C and M_H) and on Theorem 5 (M_H). Neither depends on Lemma 7.

***

## 1. Node Q0: δ-forms

### 1.1 Condition by condition

Each δ-form of `PLAN.md` §3 comes from the exact condition (Main:572; [K] definitions cited). It replaces an equality or a membership with a distance of at most δ in the trace-norm induced norm.

| Condition | Exact form [K] | Objects used by the δ-form | Refers to the quantum instrument set? |
| --- | --- | --- | --- |
| V_δ | `CompositeOperationalValidity` (OB/OperationalValidity.lean:88) | PSD cone, trace, trace norm | no |
| L_δ | `SystemToLevelOne` (OB/LevelOneSeam.lean:117) | transport along `levelOneIdx` | no |
| I_δ | `InertSpectatorCompositionality` (OB/SpectatorBridge.lean:223) | `withSpectator`, relabellings | no |
| U_δ | `HasCompositeUnitaryControl` (OB/OperationalAssembly.lean:665) | unitary group, conjugation | no |
| C_δ | `IteratedAncillaClosure` (OB/AncillaClosure.lean:247) | uniform attachment, partial trace, `shiftIdx` transport | no |

The exact condition itself uses every object in the third column. All of them belong to the complex matrix kinematics that the characterization takes as given (Main:572; `FiniteOperationalTheory`, OB/OperationalAssembly.lean:594). The only addition is a norm.

The trace norm is the base norm of the kinematic state cone, with the trace as its order unit. In finite dimension every other norm is equivalent to it, with dimension-dependent constants. Under another choice of norm the results below change only in their constants.

### 1.2 Finding

Q0 passes, relative to the given kinematics. No δ-form refers to the quantum instrument set (`IsFiniteEndomorphicKrausInstrument`, OB/KrausSoundness.lean:112), which is the conclusion of the exact theorem.

The quantum structure of this setting sits in the kinematics: complex matrices, the PSD cone, the trace rule for probabilities and the tensor structure of ancilla levels. That kinematics is taken as given, and the exact and approximate forms share it. Stability results in this setting therefore test the passage from the five conditions to quantum instruments inside that kinematics. They cannot test the kinematics itself, whose derivation Main:572 states as open.

### 1.3 The δ-forms for every δ > 0 do not imply the exact conditions

**Proposition 1.** *Let 𝔸 be the field of algebraic numbers. On a carrier with d ≥ 2, define T_alg as follows. A family is available at a level (or on the system) exactly when it has a Kraus representation with all Kraus matrix entries in 𝔸. Its available preparations are the uniform attachments of positive size followed by available single-outcome operations. Then T_alg is a `FiniteOperationalTheory`. It satisfies V, I, C and L exactly and U_δ for every δ > 0 at every level, and it fails `HasCompositeUnitaryControl`.*

*Proof.*
- 𝔸 is a field closed under complex conjugation and under square roots of positive elements.
- The six structure rules hold:
  - identity and Lüders readouts have entries 0 and 1;
  - coarse-graining takes unions of Kraus families;
  - feed-forward multiplies Kraus operators;
  - attaching I/r (r ≥ 1), running an available family and taking the partial trace gives Kraus operators (1/√r)(1 ⊗ ⟨i|)K(1 ⊗ |j⟩), whose entries lie in 𝔸.
- The same computations give exact closure, exact inert spectators (Kraus operators K ⊗ 1, reindexed) and exact trivial-ancilla consistency. Kraus families are completely positive and trace preserving, so validity holds.
- Unitaries with entries in 𝔸 are dense in each unitary group. To approximate a unitary, diagonalize it, approximate the eigenvector basis by an 𝔸-matrix and orthonormalize, and approximate each eigenvalue by a rational point of the unit circle. This gives U_δ for every δ > 0.
- The channel conj U with U = diag(1, e^{i}) on two basis states (identity elsewhere) is not available. Every Kraus representation of a unitary channel consists of multiples c_j U with Σ|c_j|² = 1. If c_j U had entries in 𝔸 for some c_j ≠ 0, then e^{i} would be algebraic, contrary to the Lindemann–Weierstrass theorem [L]. □

So the conjunction "C_δ for every δ > 0" is strictly weaker than the exact conditions. §5 identifies what it does characterize under M_C.

***

## 2. Norm lemmas

All norms are on complex matrices. For a family F = (F_a), ‖F‖ is the trace-norm induced norm of the map X ↦ ⊕_a F_a(X) (`PLAN.md` §3). ‖·‖_⋄ is the diamond norm.

- **N1 (Kraus-sum inequality) [L].** For matrices A_{ai}, B_{ai}: Σ_a ‖Σ_i A_{ai} X B_{ai}^†‖₁ ≤ ‖Σ_{ai} A_{ai}^†A_{ai}‖^{1/2} ‖Σ_{ai} B_{ai}^†B_{ai}‖^{1/2} ‖X‖₁.
  - *Proof.* For X = |u⟩⟨v|, ‖A|u⟩⟨v|B^†‖₁ = ‖Au‖‖Bv‖. Apply Cauchy–Schwarz over (a, i), then the singular value decomposition of X. □
  - Consequences: a quantum instrument has ‖F‖ = 1 on all complex matrices, and a completely positive family with Σ_a F_a^†(I) = M has ‖F‖ ≤ ‖M‖.
- **N2 (Choi bound) [L].** If J is the Choi matrix of Φ, then ‖Φ‖_⋄ ≤ ‖J‖₁.
  - *Proof.* A rank-one Choi matrix |u⟩⟨v| is that of X ↦ U X V^†, with ‖u‖ = ‖U‖_F and ‖v‖ = ‖V‖_F. Its diamond norm is at most ‖U‖_op‖V‖_op ≤ ‖u‖‖v‖. Sum over the singular value decomposition of J. □
- **N3 (diamond and induced norm) [L].** For input dimension N, ‖Φ‖_⋄ ≤ N‖Φ‖_{1→1}. For a family, apply this to the map into the direct sum. Hence ‖withSpectator_e(F)‖ ≤ N‖F‖.
- **N4 (hybrid bound for adaptive protocols).** Let two protocols of horizon K on the same level apply, at each node, families T and Q chosen by the same rule. Suppose ‖T − Q‖ ≤ e, ‖Q‖ ≤ 1 and ‖T‖ ≤ 1 + s at every node. Then for every input density ρ,
  TV(P^T(ρ), P^Q(ρ)) ≤ ½ Σ_{t=1}^{K} e(1+s)^{t−1} ≤ ½((1+max(e, s))^K − 1).
  - *Proof.* Treat the record as a block-diagonal classical register. A step acts blockwise, and its induced norm on block-diagonal inputs is the maximum over blocks. Let H_j use T at steps ≤ j and Q after. Then H_j − H_{j−1} is (Q-tail) ∘ (T_j − Q_j) ∘ (T-prefix), whose norm is at most e(1+s)^{j−1}. Sum over j and use |tr Y| ≤ ‖Y‖₁ for each history. □
  - N4 is an analogue of Main's adaptive telescoping Lemma (Main:604) [P], not a case of it. Main:604 compares quantum instruments on both sides through a maximum of diamond distances. N4 uses the family-sum induced trace norm and allows a non-quantum T, which is needed here.
- **N5 (effect operators and test families).**
  - For a family F at a level, Γ_{F,a} denotes the matrix with tr F_a(X) = tr(Γ_{F,a} X) for all X.
  - If |tr(Zσ)| ≤ η for every density σ, then ‖Z‖_op ≤ 2η, and ‖Z‖_op ≤ η when Z is Hermitian. (The operator norm is at most twice the numerical radius, and equals it for Hermitian Z.)
  - For every matrix Y, ‖Y‖₁ ≤ 4 max_E |tr(EY)| over projectors E, and ‖Y‖₁ ≤ 2 max_E |tr(EY)| for Hermitian Y. (Split Y into its Hermitian and anti-Hermitian parts; each has real trace against E.)
  - A general X is a combination of four positive matrices of total trace at most 2‖X‖₁.

***

## 3. Direction 1 (Q1): C_δ ⇒ closeness of laws under M_C and M_H

Fix a level n ≥ 1, with N = d·n. Let k = ⌈log₂(m N²)⌉ and Λ₁(n, m) = {n, N·n, 2, n·2^k}. When system-level histories are included, Λ₁(n, m) also contains the system and level 1.

### 3.1 Soundness: available families are near quantum instruments

**Theorem 2 (soundness).** *Assume V_δ and I_δ for families with at most m outcomes on the levels {n, N·n}, and η := δ(N(m+1) + 1) < 1. Then every available family F at level n with at most m outcomes has a quantum instrument F̃ with the same outcome set such that ‖F − F̃‖ ≤ ε_s := δ(4N(m+1) + 3).*

*Proof.*
1. Take the spectator R to be a copy of the level-n carrier, with the relabelling into level N·n, and let Ω = Σ_i |ii⟩. I_δ gives an available G at level N·n with Σ_a ‖G_a − F_a ⊗ id_R‖ ≤ δ. V_δ gives dist₁(G_a(|Ω⟩⟨Ω|/N), PSD) ≤ δ for each a.
2. Hence the Choi matrices J_a = (F_a ⊗ id)(|Ω⟩⟨Ω|) satisfy Σ_a dist₁(J_a/N, PSD) ≤ (m+1)δ. This step, from validity and inert spectators to positivity of the Choi matrix, is the approximate form of `cp_of_valid_inert` (OB/OperationalValidity.lean:105 [K]).
3. Write J_a = N P_a + N E_a with P_a ≥ 0 and Σ_a ‖E_a‖₁ ≤ (m+1)δ. Let F_a^+ be the completely positive map with Choi matrix N P_a. By N2, Σ_a ‖F_a − F_a^+‖_⋄ ≤ σ := N(m+1)δ.
4. For a density X, the trace clause of V_δ gives |Σ_a tr F_a^+(X) − 1| ≤ σ + δ. So M := Σ_a F_a^{+†}(I) satisfies ‖M − I‖ ≤ η < 1.
5. Let K_{ai} be Kraus operators of F^+ and Y = M^{−1/2}. Then F̃_a(X) := F_a^+(Y X Y) is a quantum instrument, since Σ_{ai} (K_{ai}Y)^†K_{ai}Y = I.
6. Write YXY − X = (Y−1)XY + X(Y−1) and apply N1, using |1 − √μ| ≤ |1 − μ| on the spectrum of M:
   ‖F̃ − F^+‖ ≤ ‖(Y−1)M(Y−1)‖^{1/2}‖YMY‖^{1/2} + ‖M‖^{1/2}‖(Y−1)M(Y−1)‖^{1/2} ≤ η + √(1+η) η.
7. Hence ‖F − F̃‖ ≤ σ + (1 + √2)η ≤ (2 + √2)σ + (1 + √2)δ ≤ ε_s. □

On the system, L_δ gives an available level-1 family within δ of transport(F). Theorem 2 at level 1 (N = d) and the isometry of transport then give ε_s^{sys} := δ + δ(4d(m+1) + 3).

### 3.2 Coverage: quantum instruments are near available families

**Theorem 3 (coverage).** *Assume U_δ at level L = n·2^k, I_δ for the two-outcome readout from level 2 into level L, and C_δ for families with at most m outcomes into level n. Then every quantum instrument J at level n with at most m outcomes has an available family G with the same outcome set such that ‖G − J‖ ≤ ε_c := (1+δ)^{3k+1} − 1 + δ ≤ (3k+2)δ e^{(3k+1)δ}.*

*Proof.* A minimal Kraus representation of J has r ≤ m N² operators. Pad it to 2^k with zero operators, and let out assign the outcomes. The Stinespring isometry V ψ = Σ_i K_iψ ⊗ |i⟩ extends to a unitary U on the carrier times a fresh register of k qubits, with U(ψ ⊗ |0⟩) = Vψ. Exactly,

J_a(X) = tr_fresh[Σ_{out(i)=a} P_i U Seed(X ⊗ I/2^k) U^† P_i],

where the P_i are the Lüders projectors of the fresh register and Seed resets each qubit (read it, flip it on outcome 1), so that Seed(X ⊗ I/2^k) = X ⊗ |0⟩⟨0|.

The pieces are supplied as follows, on the carrier (A × Fin n) × Fin 2^k transported to level L:
- The binary readout of qubit j. The native readout at level 2 is exactly Lüders (`readout_is_localLuders`, OB/OperationalAssembly.lean:658 [K]). I_δ, with the remaining register and Fin n as spectator, gives an available two-outcome family within δ of it. This is the approximate form of `availExt_relativeReadout` (OB/AncillaClosure.lean:231 [K]).
- The identity, the flips and U. U_δ gives single-outcome available maps within δ of each. The structure has no identity rule at ancilla levels.
- Feed-forward and coarse-graining are exact structure rules, so the composed family, with the outcome set of J, is available at level L.
- C_δ applied to that family gives an available G at level n within δ of its uniform-attach-and-discard.

The seed is the approximate form of `pureSeedPrep_available_of_swap` (OB/OperationalAssembly.lean:675 [K]). Error count:
- Along every branch the composite has depth 2k (seed) + 1 (U) + k (final readouts) = 3k + 1 layers. Each layer is within δ of an exact layer of norm 1 (N1). So the composed family is within (1+δ)^{3k+1} − 1 of the exact one.
- Uniform attachment of positive size followed by partial trace is completely positive and trace preserving, hence of norm 1 (N1).
- C_δ adds δ. □

On the system, the level-one family transports to an available system family exactly (`avail_of_availExt_one`, OB/LevelOneSeam.lean:107 [K]). So Theorem 3 at level 1 gives the same bound for system instruments. The δ-forms are applied only to families with at most max(m, 2) outcomes. The intermediate family with 2^k outcomes is formed by exact rules only.

### 3.3 History laws

**Theorem 4 (Direction 1, metrics M_C and M_H).** *At fixed (d, m, K) and level n, assume C_δ[max(m, 2), Λ₁(n, m)] with δ(N(m+1)+1) < 1, and let ε₁ = max(ε_s, ε_c). Then*
M_H(T, Q) ≤ M_C(T, Q) ≤ ε(δ, d, m, K) := ½((1+ε₁)^K − 1),
*which is at most K ε₁ when K ε₁ ≤ 1. The same holds for system-level histories with ε_s^{sys}.*

*Proof.*
- Soundness: take c(F) := F̃ from Theorem 2, and apply N4 with e = s = ε_s.
- Coverage: take c′(J) := G from Theorem 3, and apply N4 with T = c′(J), e = ε_c and s = ε_s. By Theorem 2 the norm of c′(J) is at most 1 + ε_s. □

### 3.4 Order of work: d = 2, then general d

- **d = 2, system-level histories, m = 2.**
  - Level 1 has N = 2, the copy level is 2, k = ⌈log₂ 8⌉ = 3 and L = 8.
  - η = 7δ and ε_s^{sys} = δ + 27δ = 28δ.
  - ε_c = (1+δ)^{10} − 1 + δ ≤ 11.5δ for δ ≤ 1/100.
  - Hence M_C ≤ ½((1+28δ)^K − 1) ≤ 28Kδ for 28Kδ ≤ 1, and the same bound holds for M_H.
  - Levels used: 1, 2, 8 and the system.
- **General d.** Theorem 4 holds as stated. ε_s grows linearly in N(m+1) = d n(m+1), ε_c grows as log₂(m d² n²) δ, and ε is linear in K for small δ. The proof uses no property of d = 2.

### 3.5 Pressure test (favourable branch)

1. **Strength of the hypothesis.** C_δ is uniform over every available family at the listed levels and over the unitary continuum. It relaxes the exact conditions but is not a finitely testable property. Theorem 4 transfers precision; it does not supply it.
2. **Hidden exact inputs.** The six structure rules are exact. Theorem 3 uses the exact Lüders form of the native readout and exact feed-forward. With approximate readout or composition the bound acquires further terms; this is not analysed (O2).
3. **Dimension dependence.** The soundness constant N(m+1) comes from the Choi bound. The transpose mixture (1−λ)id + λθ, which is positive and trace preserving, gives a lower bound of order δ only, so the factor N may not be optimal (O1). The bound is correct as stated.
4. **Scope of the conclusion.** The statement holds inside the given kinematics and says nothing about whether an OI mechanism supplies C_δ. Direction 1 is a stability property of the characterization, not evidence for OI (§A.29).
5. **Level bookkeeping.** Only the finitely many levels in Λ₁(n, m) enter. This was checked against each use of I_δ, U_δ and C_δ.

***

## 4. Direction 2 (Q2): closeness of laws ⇒ δ-conditions

### 4.1 Metric M_H: disproved

**Theorem 5 (counterexample, M_H).** *On any carrier, define T_dec as follows. At every level and on the system, the available families are exactly those whose branches are decomposable maps Φ = Ψ₁ + θ∘Ψ₂ with Σ_a tr F_a(X) = tr X. Here Ψ₁ and Ψ₂ are completely positive and θ is the full transpose of that level's carrier. Its preparations are the uniform attachments of positive size followed by available single-outcome operations. Then:*
- *(i) T_dec is a `FiniteOperationalTheory` satisfying V, U, C and L exactly;*
- *(ii) M_H(T_dec, Q) = 0 at every level and on the system, for every m and K;*
- *(iii) at every level n with N = d·n ≥ 2, I_δ fails for every δ < 1/2.*

*Proof.*
- (i) Decomposable maps are closed under:
  - composition, since θΨθ is completely positive with conjugated Kraus operators;
  - sums;
  - transport along reindexings, since θ commutes with conjugation by real permutation matrices;
  - attach, run and discard: the partial trace of a full transpose is the transpose of the partial trace, so attaching I/r (r ≥ 1), running an available family and discarding gives a decomposable system family.

  Readouts, the identity and all unitary conjugations are completely positive. Decomposable maps are positive, which gives validity. Closure and trivial-ancilla consistency follow from the same computations.
- (iii) θ_n (single outcome) is available at level n. Take a two-dimensional spectator and a relabelling into level 2n. Under θ_n ⊗ id, a maximally entangled state on a two-dimensional subspace of the carrier and the spectator maps to an operator with eigenvalue −1/2. Every family available at level 2n is positive, so ‖G − θ_n ⊗ id‖ ≥ 1/2 for each such G.
- (ii) Quantum instruments are decomposable, so every quantum protocol is a T_dec protocol. Conversely, for a T_dec protocol let M_{o₁…o_t} = F^{1†}_{o₁} ∘ ⋯ ∘ F^{t†}_{o_t}(I) along each branch. Duals of positive maps are positive, and the trace condition gives Σ_{o_t} M_{o₁…o_t} = M_{o₁…o_{t−1}}. So the effects form a tree of positive operators with P^T(ρ)(o⃗) = tr(M_{o⃗} ρ). Lemma 6 realizes every such tree by a quantum protocol with the same outcome set at every node. So the two behaviour sets coincide. □

**Lemma 6 (tree realization).** *Every tree of positive operators M_{o₁…o_t} with Σ_{o_t} M_{o₁…o_t} = M_{o₁…o_{t−1}} and Σ_{o₁} M_{o₁} = I, branching at most m at each node, is the history law of an adaptive quantum protocol of Lüders instruments with the same branching.*

*Proof.* Put A_{o₁} = M_{o₁}^{1/2}. Suppose A satisfies A^†A = M_{o₁…o_{t−1}}.
- Take a polar decomposition A = W|A| with W unitary, which is always possible for a square matrix. Let |A|^+ be the pseudo-inverse of |A| and Π its support projector.
- For a fixed outcome o*, set B_{o_t} = W(|A|^+ M_{o₁…o_t} |A|^+ + [o_t = o*](1 − Π))W^†.
- Then B_{o_t} ≥ 0, and Σ_{o_t} B_{o_t} = W(Π + 1 − Π)W^† = I, using the unitarity of W.
- With A′ = B_{o_t}^{1/2}A, A′^†A′ = |A|W^†B_{o_t}W|A| = Π M_{o₁…o_t} Π = M_{o₁…o_t}. The last equality holds because 0 ≤ M_{o₁…o_t} ≤ |A|² keeps its support inside Π.
- The step-t instrument X ↦ B^{1/2}XB^{1/2} is a Lüders instrument chosen by the earlier outcomes. □

**Status of Q2 under M_H: disproved.** The failure occurs at ε = 0, so it is a statement about the metric, not about approximation. Closeness of behaviour sets, even equality at every level, does not determine inert spectators. M_H is uniform in the input state, so the conclusion also holds under Main's fixed-initial-state finite-test topology (Main:610).

The mechanism is the separation of positivity from complete positivity. The corpus already records it for ancilla-state experiments: `ancTranspose_not_cp` (OB/PartialTranspose.lean:123 [K]), and that file's account of why experiments with ancilla-state inputs alone cannot detect it. The new element is the full theory: four conditions hold exactly, I_δ fails by at least 1/2, and the history laws are identical to those of finite QM at every level.

Hence, under M_H, accessible-history laws do not determine `ExactAllFiniteEndomorphicQuantumOps` (OB/LevelOneSeam.lean:186), which is a statement about which maps are available. Nor do they determine:
- C_δ, for any δ < 1/2;
- the weakening "every available family lies within δ of a quantum instrument", for δ below the positive distance of θ_n from the quantum instruments at level n, that is, for all sufficiently small δ.

### 4.2 Metric M_C, m ≥ 2 and K ≥ 2: proved, with explicit δ(ε)

Horizon exactly K is kept by padding.
- **T side.** The padding family D_T is the single-outcome coarse-graining of the native readout at the level (rules (e) and (b) of Main:572), or `avail_id` on the system. It is available and completely positive and trace preserving, so tr D_T(X) = tr X for every X. Its partner c(D_T) is a single-outcome quantum instrument, hence also trace preserving.
- **Quantum side.** The padding instrument P is the identity channel. Its coverage partner c′(P) is a single-outcome available family whose trace behaviour is not controlled. The argument below uses c′(P) only through soundness partners.

**Lemma 7 (lifting to maps, metric M_C).** *At a level n, let m ≥ 2, K ≥ 2 and M_C(T, Q) < ε ≤ 1/48. Then there are correspondences c, c′ whose soundness and coverage terms are at most ε. For any such c, c′:*
- *‖F − c(F)‖ ≤ 160ε for every available F with at most m outcomes;*
- *‖c′(J) − J‖ ≤ 184ε for every quantum instrument J with at most m outcomes.*

*Hence both bounds hold with κ := 184ε.*

*Proof.*

A. *Horizon-one soundness.* For an available F, the T-protocol (F, D_T, …, D_T) has law tr F_a(ρ), and its partner (c(F), c(D_T), …) has law tr c(F)_a(ρ). So Σ_a |tr F_a(ρ) − tr c(F)_a(ρ)| ≤ 2ε for every density ρ.

B. *Test families.*
- For a projector E, let M_E = {E, 1 − E} (Lüders), G_E := c′(M_E), Γ_E := Γ_{G_E,1} and Γ′_E := Γ_{c(G_E),1} (N5).
- The quantum protocol π_E = (M_E, P, …, P) has law (tr Eσ, tr(1−E)σ). Its coverage partner is the T-protocol π_T = (G_E, c′(P), …, c′(P)), within ε in TV.
- The soundness partner of π_T is (c(G_E), c(c′(P)), …). Its padding steps are trace-preserving quantum channels, so its law is (tr Γ′_E σ, tr(I − Γ′_E)σ), again within ε of the law of π_T.
- Both outer laws are normalized two-outcome probability vectors, so their TV distance is |tr((Γ′_E − E)σ)| ≤ 2ε. Since Γ′_E − E is Hermitian, ‖Γ′_E − E‖ ≤ 2ε (N5).
- By A applied to G_E, |tr((Γ_E − Γ′_E)σ)| ≤ 2ε for every density. So ‖Γ_E − Γ′_E‖ ≤ 4ε and ‖Γ_E − E‖ ≤ 6ε.

C. *Soundness lifting.*
- Fix a density ρ, an available F and, for each outcome a, a projector E_a.
- The T-protocol "F, then G_{E_a} after outcome a, then D_T for the remaining K − 2 steps" has law tr(Γ_{G_{E_a},b} F_a ρ). Its partner (c(F), c(G_{E_a}), c(D_T), …) has law tr(Γ_{c(G_{E_a}),b} c(F)_a ρ).
- The outcome-1 terms give Σ_a |tr(Γ_{E_a}F_aρ) − tr(Γ′_{E_a}c(F)_aρ)| ≤ 2ε.
- Let Y_a = F_aρ − c(F)_aρ and D = Σ_a ‖Y_a‖₁. Since Σ_a ‖c(F)_aρ‖₁ = 1 and Σ_a ‖F_aρ‖₁ ≤ 1 + D,
  Σ_a |tr(E_a Y_a)| ≤ 2ε + 6ε(1 + D) + 2ε = 10ε + 6εD.
- Choose each E_a to attain the maximum in N5. Y_a need not be Hermitian, so the factor is 4, which gives D ≤ 40ε + 24εD. Hence D ≤ 40ε/(1 − 24ε) ≤ 80ε for ε ≤ 1/48.
- Splitting a general X into four positive parts of total trace at most 2‖X‖₁ gives ‖F − c(F)‖ ≤ 160ε.

D. *Coverage lifting.*
- Let J be a quantum instrument and G := c′(J).
- The quantum protocol "J, then M_{E_a}, then P for K − 2 steps" has law tr(M_{E_a,b}J_aρ). Its coverage partner (G, G_{E_a}, c′(P), …) is a T-protocol. The soundness partner of that T-protocol is (c(G), c(G_{E_a}), c(c′(P)), …), with law tr(Γ_{c(G_{E_a}),b} c(G)_aρ).
- By the triangle inequality the first and last laws are within 2ε in TV. So Σ_a |tr(E_a J_aρ) − tr(Γ′_{E_a}c(G)_aρ)| ≤ 4ε, and
  Σ_a |tr(E_a(J_aρ − c(G)_aρ))| ≤ 4ε + 2ε Σ_a ‖c(G)_aρ‖₁ = 6ε.
- J_aρ − c(G)_aρ is Hermitian, so N5 with factor 2 gives Σ_a ‖J_aρ − c(G)_aρ‖₁ ≤ 12ε. The four-part split gives ‖J − c(G)‖ ≤ 24ε.
- By C applied to the available family G, ‖G − c(G)‖ ≤ 160ε. Hence ‖c′(J) − J‖ ≤ 184ε. □

The bound proposed in the first review, κ = 288ε for ε ≤ 1/64, follows from Lemma 7: 184ε ≤ 288ε, and ε ≤ 1/64 implies ε ≤ 1/48.

**Theorem 8 (Direction 2, metric M_C).** *Let m ≥ 2, K ≥ 2 and ε ≤ 1/48. Let M_C(T, Q) < ε at every level of a set Λ that contains each level the δ-forms below reference. Let κ = 184ε, and let N_Λ be the largest carrier dimension of a base level of I in Λ. Then, for families with at most m outcomes, T satisfies V_κ, U_κ, I_{(N_Λ+1)κ}, C_{2κ} and L_{2κ} on Λ. Hence C_{δ(ε)}[m, Λ] holds with δ(ε) = 184(N_Λ + 1)ε.*

*Proof.* Apply Lemma 7 at each level of Λ.
- V: F_a(X) lies within ‖(F_a − c(F)_a)X‖₁ ≤ κ of the positive matrix c(F)_a(X), and the trace defect is at most κ‖X‖₁.
- U: c′(conj U) is within κ of conj U.
- I: take F at level n and a relabelling into level m′. Then withSpectator_e(c(F)) is a quantum instrument at level m′, and G = c′ of it satisfies ‖G − withSpectator_e(F)‖ ≤ κ + N‖c(F) − F‖ ≤ (N+1)κ by N3.
- C: for F available at level n(r+1), the uniform-attach-and-discard of c(F) is a quantum instrument at level n. c′ of it is within κ, and discarding has norm 1, so the total is at most 2κ.
- L: the same argument, through transport to level 1. □

### 4.3 Metric M_C, m = 1 or K = 1: disproved

**Proposition 11 (M_C, m = 1 or K = 1).** *For T_dec of Theorem 5, M_C(T_dec, Q) = 0 at every level and on the system in two cases:*
- *(a) at horizon K = 1, for every m;*
- *(b) at outcome bound m = 1, for every K.*

*In both cases C_δ[m, Λ] fails for every δ < 1/2 whenever Λ contains a level n with d·n ≥ 2 and the level 2n.*

*Proof.*
- Coverage, in both cases: every quantum instrument is available in T_dec, so take c′ to be the identity.
- (a) Soundness at K = 1. For an available F, the effects Γ_{F,a} = F_a^†(I) are positive (duals of positive maps) and sum to I. Let c(F) be the measure-and-prepare instrument c(F)_a(X) = tr(Γ_{F,a}X)τ for a fixed density τ. It is a quantum instrument with the same outcome set, and its horizon-one law equals that of F for every input. So the soundness term is 0.
- (b) At m = 1 every available family is single-outcome and trace preserving. So every T-law and every quantum law is identically 1, and any c gives soundness term 0.
- The failure of I_δ is Theorem 5 (iii). θ_n is a single-outcome family, so it lies in C_δ[m, Λ] for every m ≥ 1. □

So Direction 2 under M_C is disproved at m = 1 and at K = 1. The restriction m ≥ 2, K ≥ 2 in Theorem 8 is therefore necessary, not only sufficient for the proof. O3 is closed. The route through feed-forward-composed families at K = 1 with m ≥ 4 also fails, since (a) holds for every m.

### 4.4 Metric M_C: a metric that omits a level

**Proposition 9 (M_C).** *For any level L ≥ 2, define T^{(L)} as follows. It is exact QM at every level other than L and on the system. At level L, the available families are exactly those whose Kraus operators all have the form 1_A ⊗ |j⟩⟨i| and are normalized (Σ K^†K = 1). Its level-L preparations are the uniform attachment of size L and its composites with available single-outcome maps. Then T^{(L)} is a `FiniteOperationalTheory`, M_C(T^{(L)}, Q) = 0 at every level except L, and U_δ fails at level L for every δ < 1.*

*Proof.*
- The normalized level-L families are closed under feed-forward and coarse-graining and contain the Lüders readout.
- Because of the normalization, attaching I/L, running such a family and discarding gives completely positive, trace-preserving system families, which are available in the exact-QM system.
- No structure rule links level L to another level except through the system.
- For X = ρ ⊗ |0⟩⟨1|, every available level-L map returns 0, because each Kraus operator 1 ⊗ |j⟩⟨i| gives ⟨i|0⟩⟨1|i⟩ = 0. But conj(1) returns X, with ‖X‖₁ = 1. □

This is narrower than a general failure of Direction 2 on fewer levels: a metric M_C that omits one level L ≥ 2 does not bound U_δ at that level. Theorem 8 is therefore stated for a level set containing every level the δ-forms reference.

### 4.5 Pressure test (favourable branch)

M_C builds in a family-by-family correspondence, and Theorem 8's force comes from it. Lemma 7 turns correspondence closeness of laws into closeness of maps. After that, the conditions follow by continuity, since exact QM satisfies them.

The content beyond that continuity:
- (a) Horizon two and two outcomes suffice for the lifting. Horizon exactly K is kept by trace-preserving padding on the T side and by soundness partners of the coverage partners.
- (b) Both thresholds are sharp in the sense of Proposition 11.
- (c) The level set must contain every referenced level (Proposition 9).

Under M_H the converse fails (Theorem 5). The constant N_Λ + 1 makes δ(ε) non-uniform in the level, so no level-uniform converse is obtained (O4).

***

## 5. Both directions under M_C

**Corollary 10 (metric M_C).** *Let m ≥ 2, K ≥ 2, and let Λ be all levels together with the system. The following are equivalent:*
- *(a) C_δ[m, Λ] holds for every δ > 0;*
- *(b) M_C(T, Q) = 0 at every level and on the system;*
- *(c) at every level and on the system, the set of available families with at most m outcomes is contained in the set of quantum instruments, and its closure equals that set (for each outcome set).*

*Proof.*
- (a) ⇒ (b): Theorem 4 at each level, letting δ → 0.
- (b) ⇒ (c): Lemma 7 with ε → 0. It places each available family at distance 0 from the closed set of quantum instruments (completely positive families with trace-preserving sum, at fixed outcome set and dimension), and each quantum instrument in the closure of the available set.
- (c) ⇒ (b): take c to be the identity for soundness and, for coverage, approximants within any η. N4 gives M_C ≤ ½((1+η)^K − 1).
- (b) ⇒ (a), instance by instance:
  - Fix δ > 0 and one instance of a δ-form. It references a finite set Λ_i of levels.
  - Let N_i be the largest base-level carrier dimension when the instance is one of I, and N_i = 1 when it is one of V, U, C or L, which have no base level of I.
  - M_C = 0 at the levels of Λ_i. So Theorem 8 on Λ_i, with ε ≤ min(1/48, δ/(184(N_i+1))), gives that instance at δ. For instances of V, U, C or L this reads ε ≤ min(1/48, δ/368).
  - Theorem 8 is not applied with Λ equal to all levels, where N_Λ is unbounded. □

**Outside m ≥ 2, K ≥ 2.** (a) ⇒ (b) still holds:
- At K = 1 with m ≥ 2, Theorem 4 applies.
- At m = 1, Theorem 4 does not apply, since it needs C_δ[2]. The direct argument is this. V_δ for every δ > 0 makes every single-outcome available family exactly trace preserving. So every m = 1 law is identically 1, both for T and for QM. Hence M_C = 0, with c arbitrary and c′ mapping every quantum instrument to D_T.

But at m = 1 or K = 1, (b) implies neither (a) nor (c). T_dec has M_C = 0 (Proposition 11), yet C_δ fails for δ < 1/2 and its available set is not contained in the quantum instruments.

The exact theorem identifies the available set with the quantum instruments (row D13). Under M_C with m, K ≥ 2, the stable content of the characterization is the identification of its closure. Proposition 1 shows that the two differ.

***

## 6. Inputs and labels

| Input | Label | Use |
| --- | --- | --- |
| `exactAll_iff_physical_general` (OB/GeneralCarrier.lean:100), `general_characterization` (:107) | [K] | Setting; the exact endpoint the δ-forms relax; row D13 |
| `FiniteOperationalTheory` (OB/OperationalAssembly.lean:594) and the five condition definitions (§1.1) | [K] definitions | δ-forms; structure rules kept exact; padding family D_T (rules (b), (e), `avail_id`) |
| `IsFiniteEndomorphicKrausInstrument` (OB/KrausSoundness.lean:112), `ExactAllFiniteEndomorphicQuantumOps` (OB/LevelOneSeam.lean:186) | [K] definitions | Target set; §4.1 conclusion |
| `readout_is_localLuders` (OB/OperationalAssembly.lean:658), `avail_of_availExt_one` (OB/LevelOneSeam.lean:107) | [K] | Exact steps used in Theorem 3 |
| `cp_of_valid_inert` (OB/OperationalValidity.lean:105), `availExt_relativeReadout` (OB/AncillaClosure.lean:231), `pureSeedPrep_available_of_swap` (OB/OperationalAssembly.lean:675) | [K] | Exact templates whose approximate forms Theorems 2–3 prove; not premises of the approximate statements |
| `ancTranspose_not_cp` and the account in OB/PartialTranspose.lean | [K] | Prior record of the positivity / complete-positivity separation (§4.1) |
| Main:572 (operational-extension boundary, six rules, five conditions, kinematics taken as given) | [P] | Setting; kinematics open |
| Main:604 (adaptive telescoping), :606, :610 | [P] | Comparison for N4; source of M_H |
| Main finite-b items (Main:574 clause (1), Rounding Lemma complex-entry constant) | [P], open | Not used |
| Unit 1 r4b, rows D13, D14 and the §7.1 coverage/soundness split | partially verified ([A]/[W]) | Labels and the motivation of M_C only |
| Independent review, PR #1584 comment 7184945033 (findings 1–8); focused delta review, PR #1584 comment 7185177023 (findings 1–5) | review records | Provenance for the r2 and r3 corrections. The padding route of Lemma 7 (trace-preserving padding on the T side; comparison of J with c(c′(J)) through soundness partners) and the construction of Proposition 11 (T_dec with the measure-and-prepare partner at K = 1, and trace preservation at m = 1) originate in the first review. The proofs written here and the constants 160ε and 184ε for ε ≤ 1/48 are this unit's own. |
| N1–N3, N5, Choi matrices, polar decomposition, decomposable maps, Lindemann–Weierstrass | [L] | Standard mathematics, recalled |
| #1222, #1227, #1229, the F945-R note | provenance only | No claim uses them |

No input is support off `main` (§A.42 item 8). The owner decisions cited in `PLAN.md` and in the header are provenance.

***

## 7. Productivity verdict and classification

**Gem**, under the test fixed in `PLAN.md` §6:
- Theorem 4 is an explicit ε(δ, d, m, K) bound (metrics M_C and M_H).
- Theorem 5 is a counterexample to stability in Direction 2 under M_H.
- Proposition 11 adds counterexamples under M_C at m = 1 and at K = 1.

Classification (§A.31):
- Theorem 4 (Direction 1, M_C and M_H): NEW for row D14, which had no statement. The mechanism (Choi projection, Stinespring with approximate pieces, telescoping) is standard.
- Theorem 5 (the M_H converse fails): NEW as a theory-level statement. Its mechanism is the known positivity / complete-positivity separation.
- Theorem 8 with Lemma 7 (the M_C converse for m, K ≥ 2) and Proposition 9 (a metric that omits a level): ELABORATING. The level-set requirement is the non-obvious part.
- Proposition 11 (the M_C converse fails at m = 1 and at K = 1): NEW. Its construction originates in the first review (§6).
- Proposition 1 and Corollary 10 (M_C): NEW. Under M_C the δ-relaxation characterizes the closure of the available sets, not the sets.

Assumption-watch markers:
- **W1 (metric).** Any claim that a theory is "approximately QM" must state whether closeness is of behaviour sets (M_H) or under a fixed family correspondence (M_C), and, for M_C, the outcome bound and the horizon.
  - M_H-closeness certifies no completion condition (Theorem 5).
  - M_C-closeness certifies none at m = 1 or K = 1 (Proposition 11).
  - This bears on #1216 Level B and on unit 1 §7.1, whose common recipe fixes a correspondence. A coverage or soundness bound stated as a behaviour-set supremum without a correspondence is an M_H statement.
- **W2 (exact structure rules).** The exact Lüders readout and exact feed-forward are inputs of Theorem 3 outside the five conditions. The exact trace preservation of the coarse-grained readout is an input of Lemma 7's padding.
- **W3 (kinematics).** All results hold inside the given complex matrix kinematics; none bears on its derivation.

## 8. Open nodes

| ID | Node | Status |
| --- | --- | --- |
| O1 | Optimal dimension dependence of the soundness constant (upper N(m+1)δ, lower of order δ) | open; not needed for any status above |
| O2 | Approximate structure rules (readout, feed-forward, preparations) | open |
| O3 | Direction 2 under M_C at K = 1 | closed, disproved (Proposition 11), for every m |
| O4 | A converse under M_C uniform in the level | open |
| O5 | Whether any OI-derived theory satisfies C_δ for small δ | outside this unit (#1169, #1211) |
| O6 | Derivation of the complex matrix kinematics (Main:572) | open; outside this unit |
| O7 | Histories with preparations other than the inputs | open |
| O8 | Main's finite-b items | #945; untouched |
| O9 | Optimal constant in Lemma 7 (184ε here) | open; not needed for any status above |

**Stopping rule.** Each direction reached a status at fixed (d, m, K), each with its metric:
- Q1: proved under M_C, hence under M_H.
- Q2 under M_H: disproved.
- Q2 under M_C: proved for m, K ≥ 2 with the level-set condition; disproved for m = 1 or K = 1.

The stop is by status.

## 9. Points for any further review

1. Corollary 10: the m = 1 argument for (a) ⇒ (b) outside m, K ≥ 2, and the choice N_i = 1 for instances of V, U, C and L.
2. Lemma 7 and Theorem 8: the hypothesis M_C(T, Q) < ε, under which correspondences with soundness and coverage terms at most ε exist.
3. §6: the attribution of the Lemma 7 padding route and of the Proposition 11 construction to the first review.
