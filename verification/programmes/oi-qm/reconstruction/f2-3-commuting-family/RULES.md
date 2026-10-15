# F2-3 — the commuting generator family of E1-L: rules fixed before the exact runs

Research design on a research branch. It is not a native round and not adopted, and it is not for
merge without separate review. This file is committed before any decisive computation of the round
is run.

Prior evidence, cited only as such:

- the F2-2 record `../f2-2-local-continuity/`: rules, result, and correction 1, which restricted
  E1-L to the family Γ_comm and left open "whether Γ_comm contains non-diagonal coupling generators
  at N ≥ 2, and the control content of any member of Γ_comm outside Γ_spec";
- the design evidence in `design/`, floating point and not a measurement:
  - `probe.py` and its output: at (q, N) = (3, 2) under R_self, two non-diagonal pair generators
    commute with every site generator, and both fail on a three-site chain;
  - `explore.py` and its output: 40 random-start searches for commuting pair generators on the
    q = 3 chain. Every converged minimum (loss ≲ 10⁻¹³) has off-diagonal part ≲ 5 × 10⁻⁸.

## Framing (owner approval, 2026-10-15)

- **The question.** Does consistent local evolution, E1-L restricted to Γ_comm, admit genuinely
  non-diagonal coupling generators? If so, what control do they supply, and do they supply any
  capability beyond the diagonal family?
- **Exact classifications of bounded families are kept apart from universal statements.**
  - The structural lemma and its corollaries below are written arguments [W], stated for every odd
    prime q and every N within E1-L's rule. They are not kernel-checked.
  - The computations are exact at the listed sizes only.
- **Every result is conditional on E1-L** (R1–R4, T_loc, T1–T3, complex kinematics inherited),
  with F2-2's conventions:
  - **one generator per gate type.** The same G(m) is used for δ_ij(m) on every pair and the same
    g(m) for δ_i(m) on every site;
  - **orientation.** A pair generator acts on {i, j}, i < j, with its first tensor factor at site i,
    as in `f2_2_exact.py`;
  - **absent couplings contribute no term.** M_ij = 0 or M_ii = 0 adds no generator to the layer.
- **Γ_comm(R, N).** The set of generator choices for which, for every coupling M of the repertoire
  R, the generators of the gates in M's coupling layer pairwise commute.
- **Γ_diag.** The choices whose site and pair generators are diagonal in the registration basis.
  Each diagonal entry is any lift of its eigenphase, independently per basis state, so
  Γ_spec ⊊ Γ_diag.
- **Repertoires.** These are F2-2's: R_self (every symmetric coupling) and R_cf (every zero-diagonal
  coupling). One mutation repertoire, R_star, is used as a control only (below).
- **Alphabet.** Odd prime q. No result is selected by choosing q.

## The structural statements [W] (proof written in the result; each is checked exactly where
listed)

- **S1, shared-site conservation.**
  - Let G be supported on a pair containing site j, and let G′ be supported on a different pair
    {j, k}, with e^{2πiG′} ∝ δ_jk(b), b ≠ 0.
  - If [G, G′] = 0, then G commutes with δ_jk(b). Hence G conserves the registration value y_j.
  - The proof uses functional calculus and the injectivity of y ↦ b·y·1 on 𝔽_q.
- **S2, diagonality.** Within E1-L's rule, suppose the repertoire has, for a value m, a coupling
  whose layer contains an edge with value m at which some shared site plays the first-factor role,
  and also one at which a shared site plays the second-factor role. Then G(m) conserves both of its
  indices, so G(m) is diagonal.
  - On a chain with the i < j orientation, the middle site plays both roles.
- **S3, site generators.** Under R_self, every site generator g(a), a ≠ 0, is diagonal at every
  N ≥ 2. A site gate and a pair gate share a site in the same layer.
- **S4, the classification.** Under R_cf and R_self at every N ≥ 3, the coupling part of Γ_comm is
  exactly Γ_diag's.
  - One inclusion is S2–S3.
  - The other holds because diagonal generators commute.
  - At N = 2: under R_cf there is no constraint. Under R_self, G(b) conserves y₁y₂ and every
    level set of the chosen diagonal site generators.

## Sizes

- **Exact classification cells (E1, E2):** (q, N) ∈ {(3, 3), (5, 3), (7, 3)}, each on the chain
  (couplings with M_13 = 0) and on the complete graph, under R_cf and R_self.
- **The N = 2 residual (E3):** (3, 2) and (5, 2) under R_self.
- **Capability cells (C1, C2):** (3, 2) under R_self, for the two named non-diagonal members and
  the diagonal principal member.

## Cells and decision rules (each verdict is generated from its measurements)

- **E1, the necessary commutant.**
  - For each size, graph and repertoire, compute exactly the linear space 𝒦(m) of operators X on
    the pair satisfying the conditions S1 imposes. These are:
    - X commutes with δ(m);
    - X conserves the shared-site value for every shared-site role that occurs in a layer
      together with an edge of value m;
    - under R_self, X commutes with δ_i(a) ⊗ 1 and 1 ⊗ δ_j(a) for every a.
  - The computation is combinatorial: a matrix unit |s⟩⟨t| is allowed iff the two basis states
    agree on every conserved quantity, decided by integer arithmetic modulo q.
  - Every Γ_comm member's G(m) lies in 𝒦(m), by S1 [W].
  - Token `F23-DIAG-FORCED` at a size iff dim 𝒦(m) = q² and 𝒦(m) is the diagonal algebra, for
    every m. `F23-NONDIAG-ALLOWED` otherwise, with the dimension printed.
- **E2, sufficiency.** Every diagonal choice lies in Γ_comm. Checked exactly on two members at each
  size and graph:
  - the principal member;
  - a state-dependent lifted member, outside Γ_spec: θ + 1 on the states with y₁ = 1.
  - The test is that every layer's generators commute exactly (rational arithmetic).
  - Token `F23-DIAG-SUFFICES`.
- **E3, the N = 2 residual under R_self.**
  - The site generators' commutant is computed exactly. Token `F23-SITE-DIAG` iff it is diagonal.
  - The pair commutant dim 𝒦(m) is computed for two choices of site generator:
    - (i) principal, which is degenerate on y ↔ −y;
    - (ii) a lifted diagonal choice that separates y from −y.
  - Token `F23-N2-NONDIAG` under (i) iff dim 𝒦 > q², and `F23-N2-DIAG` under (ii) iff dim 𝒦 = q².
- **C1, the control algebra of the surviving members at (3, 2) under R_self.**
  - The members are principal site generators, with pair generators:
    - M_φ: G(b) = G₀(b) + |φ⟩⟨φ|, φ = (|11⟩ + |22⟩)/√2;
    - M_C: G(b) = G₀(b) + (1 − C⊗C)/2, C|y⟩ = |−y⟩.
  - The Lie algebra generated by the layer generators G_coup(M), M ∈ R_self, the free generator
    and the translation generators, over all durations. Its exact dimension modulo the identity is
    computed with F2-1's `lie_closure_dim`.
  - Token `F23-NONDIAG-FULL` iff it equals q^{2N} − 1 = 80 for both members. The diagonal principal
    member's dimension is computed alongside, as F2-2 measured it.
- **C2, capabilities beyond the diagonal family at (3, 2) under R_self.**
  - For each member, the half-layer gate h = e^{πiG_coup(M)} at M = [[0, 1], [1, 0]] and at
    M = [[1, 1], [1, 1]] is compared with the principal member's. The invariants compared:
    - (a) operator-Schmidt rank;
    - (b) whether h normalizes the Weyl group (Clifford);
    - (c) whether h|00⟩ has a negative Wigner value;
    - (d) whether h is diagonal.
  - The verdict rule:
    - `F23-NO-NEW-ALGEBRA` iff the C1 dimensions coincide with the diagonal member's. All-duration
      control then gains nothing.
    - `F23-GATE-DIFFERENCES` lists which invariants differ.
  - A difference in an invariant is reported as a difference of available gates at one duration,
    not as a capability claim beyond it.

## Controls (a failed control voids every verdict)

- **K0.** The sha256 of the imported F2-1 module must be
  `e7d257bb09f5b75d4628cd0ebd85a0b189d377b3bdf91a48fd1196705a31e7a6` and of the imported F2-2
  module `246adb2bc6590a3d84234f6937409f2042bba796d646eae633f6383a62a90e57`. F2-1's self-tests
  pass.
- **K-gen.** Every exhibited generator exponentiates to its gate exactly. For G = G₀ + K:
  - K is a Hermitian with integer spectrum (here a projector, K² = K);
  - K commutes with G₀;
  - K is supported inside one eigenspace class of the gate.

  Each is checked in rational arithmetic.
- **K-pos.** E2's diagonal members commute on every layer (exact zero commutators).
- **K-neg.** M_φ and M_C fail on the (3, 3) chain: some layer commutator is exactly nonzero. Their
  pair generators lie outside the chain's 𝒦(m).
- **K-mut.** R_star at (3, 3): the couplings with M_23 = 0, so site 1 is the first factor of both
  edges.
  - E1 must report dim 𝒦(m) > q².
  - The exhibited non-diagonal member G₀(m) + |0⟩⟨0| ⊗ |χ⟩⟨χ|, χ = (|1⟩ + |2⟩)/√2, must commute on
    every R_star layer and fail on the chain.
  - This shows that S2's hypothesis is needed, and that E1's test is not vacuous.
- **K-brute.** At (3, 3) on the chain under R_cf, 𝒦(m) is recomputed independently. The method is
  exact linear algebra: the nullspace of X ↦ [X ⊗ 1, 1 ⊗ δ₂₃(b)] together with X ↦ [X, δ(m)],
  with exact equality tests of roots of unity. Its dimension must equal E1's combinatorial count.
- **K-lie.** The dropped-translation mutation, as F2-2's K-Lie: C1's algebra without translations
  must fall below 80 for the principal member.

## Invariants of the execution and where each is measured (§A.41)

| invariant | checkpoint |
|---|---|
| Rules fixed before any decisive computation | this file's commit precedes the script's; the result names both commits |
| F2-1 and F2-2 code unchanged | K0 hashes |
| Exact arithmetic | every decisive line in integers, rationals or ℚ(ζ_n); K0 self-tests |
| Determinism | two runs, byte-identical output |
| Verdicts only over green controls | the verdict function prints `VERDICT VOID` if any control fails |

## Outcome classes

- **`F23-DIAGONAL-AT-N3`**: `F23-DIAG-FORCED` and `F23-DIAG-SUFFICES` at every N = 3 size, graph
  and repertoire. Consistent local evolution admits no non-diagonal coupling generator at those
  sizes, and S4 [W] states the same at every N ≥ 3.
- **`F23-NONDIAGONAL-AT-N3`**: some N = 3 cell reports `F23-NONDIAG-ALLOWED`. Its members are then
  listed and C1 is extended to them.
- The N = 2 and capability tokens are reported beside the class, not merged into it.

## Non-claims

- no kernel proof; S1–S4 are written arguments, exact only where computed;
- nothing about orientation conventions other than i < j, except that K-mut shows a single-role
  layer admits non-diagonal members;
- nothing about time-independent generators for a whole tick, about gate sets other than E1-L's,
  or about locality notions other than commuting layers;
- the round says nothing about whether nature realizes E1-L; local continuity remains an added
  hypothesis, not sourced.
