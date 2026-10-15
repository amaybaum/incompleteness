# F2-2 — local continuity for candidate E1: rules fixed before the exact runs

Research design on a research branch. It is not a native round and not adopted, and it is not for
merge without separate review. This file is committed before any computation of the round is run.

Prior design evidence, cited only as such:

- the F2-1 record `../f2-1-e1-consistency/`: rules, amendment 1, result, review, and correction 1;
- thread H, `../f2-research-threads/H-extension-candidates.md`.

None of these counts as a measurement of this round, except where a cell below states that it
inherits an F2-1 measurement unchanged and names it.

## Framing (owner decisions, 2026-10-14 and 2026-10-15)

- **Targets.** These are F2-1's.
  - Dense finite quantum mechanics in both directions, with the diamond-norm error measure
    including ancillas and sequential composition.
  - Exact availability is a separate, stronger target.
- **What this round investigates.** It is a locality and consistency investigation of continuity
  stated as a local rule.
  - F2-1's T took the principal logarithm of the whole-system image. That T couples sites the
    update leaves uncoupled (F2-1 finding 1). Correction 1 showed that the update does not
    determine its half-period gate.
  - This round requires uncoupled systems to evolve independently, U_AB(t) ∝ U_A(t) ⊗ U_B(t).
  - The principal logarithm is not compulsory. The choice of generator is a parameter of the
    physical law. Every result is stated for the family of generator choices on which it is
    established.
- **Generator type, fixed in advance: a time-dependent local evolution is permitted.** Each tick
  runs the update's coupling layer and then its free layer.
  - Within a layer the generator is time-independent: the sum of the generators of that layer's
    local gates.
  - A time-independent generator for the whole tick is not part of this candidate. Nothing is
    concluded about it.
- **Centre-free couplings are a separate restriction.** SM §3.1's update reads the neighbours of
  a site and not the site itself. Every control cell is run twice:
  - with every symmetric coupling, R_self (F2-1's repertoire, whose Clifford generation used
    self-couplings);
  - with zero-diagonal couplings only, R_cf.

  The two are reported separately and not merged.
- **Alphabet.** E1 is investigated at odd prime q as a conditional branch.
  - q = 7 is added at N = 1 to test whether the gate-level results depend on q.
  - The q = 2 control records a limitation of the candidate. It is not a statement that nature
    requires odd q.
  - No result is selected by choosing q, and SM §2.7's alphabet claim is not used in either
    direction.
- **Complex kinematics is inherited (R1).** Every result is conditional on R1.

## The candidate E1-L

- **R1–R4 are F2-1's**: registration, Weil images, symplectic meter, counting-measure prior.
- **Factorization of the update.** With h = 2⁻¹ mod q, the leap's canonical image factors as

  ρ(L_M) = U_free · D(M),  U_free = u^{⊗N},  D(M) = Π_i δ_i(M_ii) · Π_{i<j} δ_ij(M_ij),

  where:
  - u is the one-site canonical image of J′;
  - δ_i(m) = diag(ω^{−h m y_i²}) on site i;
  - δ_ij(m) = diag(ω^{−m y_i y_j}) on the pair {i, j}.

  The factors of D(M) commute, and each is supported on one site or one coupled pair.
- **T_loc, local continuity.** Each local gate g is realized by the flow e^{2πi s G_g}, where:
  - the gates g are u, δ_i(m), δ_ij(m) and the translations X_k;
  - G_g is a self-adjoint generator supported on g's sites, with e^{2πi G_g} ∝ g;
  - G_g depends only on the gate, so the same rule applies at every site and every pair.

  A tick runs the coupling layer by Σ G_δ and then the free layer by Σ_i G_u^{(i)}. Each layer
  completes its gate, so the tick ends at ρ(L_M) up to phase. Translations, the source terms,
  flow by G_X.
- **Control items, as in F2-1.**
  - T1: unitary evolution between updates.
  - T2: selectable couplings and selectable translations.
  - T3: selectable durations.
- **Generator families.**
  - Γ_all(g): every generator of g.
  - Γ_spec(g): the generators that are functions of g, G = Σ_λ θ_λ P_λ. Each θ_λ is a lift of λ's
    eigenphase/2π, and a common real shift is allowed. This family is infinite.
  - The principal member: θ_λ ∈ (−1/2, 1/2].
  - Under Γ_spec the half-layer gates e^{πi G} are the spectral square roots, one sign per
    eigenvalue. Over one-duration repertoires that family is finite and is scanned exhaustively.
- **Repertoires.** R_self (every symmetric coupling) and R_cf (every zero-diagonal symmetric
  coupling), each with the translations τ_1, …, τ_N, are tested in two forms:
  - **All-duration:** the layer flows and the translation flows for every real duration.
  - **One-duration:** the integer-time images, together with the half-layer gates e^{πi G_free}
    and e^{πi G_coup(M)} for every selectable M. Translations act at integer time only.

## Sizes

- (q, N) ∈ {(3, 1), (5, 1), (7, 1), (3, 2)} for every cell.
- (3, 3) for the locality cells L1 and L3 only.

## Cells and decision rules (each verdict is generated from its measurements)

- **L0 factorization (exact).**
  - The identity above holds, and every image is unitary, for:
    - every symmetric coupling at the four control sizes;
    - every zero-diagonal coupling and every coupling used by L1 and L3 at (3, 3).
  - At (7, 1) the canonical images are first checked to be genuine: unitary, U W(z) U† = W(Lz),
    and U^{ord L} = I.
  - Token `E1L-FACTORIZED` iff all hold.
- **L1 uncoupled independence (exact).**
  - Block-diagonal couplings tested:
    - at (3, 2), every diagonal coupling;
    - at (3, 3), the zero coupling and every coupling [[M_A, 0], [0, m]] with M_A a zero-diagonal
      coupling of sites {1, 2} and m ∈ 𝔽_q.
  - The test: U_AB(t) ∝ U_A(t) ⊗ U_B(t) at t ∈ {1/6, 1/4, 1/2, 3/4, 1, 3/2}, computed by two code
    paths: the N-site construction, and the per-block constructions tensored.
  - It is run under the principal member and under one non-principal member of Γ_spec per gate
    (every θ_λ lifted by +1 except the smallest).
  - Token `E1L-INDEPENDENT` iff all hold. The [W] argument that it holds for every member of Γ_all
    is stated beside it.
- **L3 strict causal cone (exact, at (3, 3)).**
  - Chains tested: M = [[0, a, 0], [a, 0, b], [0, b, 0]] with a, b ∈ {1, 2}.
  - The test, at t ∈ {1/6, 1/4, 1/2, 3/4, 1} and under the same members as L1:
    - the Heisenberg images U(t)† X_1 U(t) and U(t)† Z_1 U(t) commute with X_3 and Z_3;
    - the images of X_3 and Z_3 commute with X_1 and Z_1.
  - Token `E1L-CAUSAL` iff all hold, with the [W] argument for Γ_all stated beside it. The
    composite principal-logarithm rule of F2-1 is evaluated on the same chains and reported as a
    comparison. It is not a control.
- **C-OI consistency.**
  - By L0, the integer-time images are F2-1's, so F2-1's C1 and C2 tokens at (3, 1), (3, 2) and
    (5, 1) apply unchanged. They are cited, not re-measured.
  - At (7, 1), F2-1's C1 battery and C2 checks are run through F2-1's own functions:
    - (i) the intertwiner dimension;
    - (ii) the A4 word check: every word of length ≤ 6 over {L_M, τ_1} for every coupling, from
      every registered start;
    - (iii) the two-time law with the symplectic meter;
    - normalization and back-action.
  - Token `E1L-CONSISTENT` iff L0 holds and (7, 1) passes.
- **C3(a) all durations.** The criterion, as in F2-1 A3, is that the generated algebra contains
  su(q^N): its dimension modulo the identity equals q^{2N} − 1.
  - **(a-self).** The exact dimension is computed for the principal member. Separately, the round
    checks the hypotheses of a [W] robustness argument over Γ_all:
    - (i) the integer-time group of R_self is the full Clifford group modulo phases (as F2-1 (c1);
      run at (7, 1));
    - (ii) Sp(2N, q) is transitive on the nonzero vectors of 𝔽_q^{2N}, so the Clifford adjoint
      action on sl(q^N) is irreducible;
    - (iii) the generator of a non-scalar gate is non-scalar.

    Token `E1L-SELF-FULL` with its scope.
  - **(a-cf).** The exact dimension is computed for the principal member. Then, over Γ_spec:
    - Take the orbits O of the symplectic part of R_cf's integer-time group on 𝔽_q^{2N} ∖ {0}.
      A precondition is that the group contains every Weyl operator modulo phases; it is checked.
    - Decide exactly, for each orbit and each generator type, whether that type has a nonzero
      component on some line W(z), z ∈ O, for every member of Γ_spec. This is integer
      feasibility of a rational linear system. Types whose gate has one-dimensional eigenspaces
      are decided over Γ_all.
    - If every orbit is touched by some type for every member, the algebra is full for every
      member [W: the algebra is invariant under the integer-time group's adjoint action, and an
      invariant subspace is a sum of orbit spans].
    - Otherwise the round lists up to 8 lattice points of the failing members, chosen
      deterministically, and computes their algebras exactly.

    Token `E1L-CF-FULL` or `E1L-CF-NOT-FULL`, each with its scope.
- **C3(b) one duration.** Density in SU(q^N), up to phase, is decided by:
  - **(D1)** the generated group acts irreducibly on sl(q^N) by conjugation, exactly. The test
    takes the closure of the touching relation over the orbit decomposition of the integer-time
    group, with the half-layer gates and their inverses.
  - **(D2)** the generated group has an element of infinite order modulo scalars. It is certified
    exactly by |tr g|² ∉ ℤ[ζ_n], on the preregistered words g = h·w for each named half-layer gate
    h, with w ∈ {X_1, Z_1, X_1 Z_1} ∪ {the integer-time leap images}. The first certified word is
    printed.
  - **The inference [W].** D1 and D2 give closure ⊇ SU(q^N): the Lie algebra of the closure is
    adjoint-invariant and not central. The failure of D1 gives a proper closure.
  - **Members.** Every member of Γ_spec (finite: the sign patterns) is evaluated. A summary
    `ALL`, `SOME` (listing which) or `NONE` is given for each repertoire and size.
  - **(b-self)** additionally reports:
    - the [L] route, Campbell–Anwar–Browne Appendix D as read by the owner, from Clifford
      generation and a non-Clifford gate;
    - whether the free half-layer is non-Clifford for every member of Γ_all, from the count of
      S ∈ SL(2, q) with S² = J′, since the free half-layer is a tensor power of one-site square
      roots of u.
  - Tokens `E1L-SELF-DENSE` and `E1L-CF-DENSE`, or their negations, each with its member summary.
  - **Separated failures (as F2-1 A3).** When D1 fails for a member, the round reports for that
    member, as separate cells, the layer fractions 1/3 and 1/4 under the same rule.
- **C4 escape from the known obstructions.**
  - **(a)** u preserves no nonnegativity. This is inherited from F2-1 C4(a) at the three F2-1
    sizes and checked at (7, 1).
  - **(b)** The free half-layer applied to |0…0⟩ has a negative Wigner value. This is checked
    exactly for every member of Γ_spec. Over Γ_all it is decided by the stabilizer-reachability
    test of correction 1 at N = 1, with the product argument [W] for N = 2.
  - **(c)** One-duration generating sets are finite, so the groups they generate are countable.
    The all-duration repertoires are continua.

## Controls (a failed control voids every verdict)

- **K0.** F2-1's exactness self-tests. The sha256 of the imported F2-1 module is printed and must
  equal `e7d257bb09f5b75d4628cd0ebd85a0b189d377b3bdf91a48fd1196705a31e7a6`.
- **K1.** q = 2, F2-1's K1. It records a limitation only.
- **K-L1 countercontrol.** The L1 test applied to F2-1's composite principal-logarithm rule at
  (3, 2) with M = 0 must report a failure.
- **K-L3 mutation.** A δ_13(1) generator term on sites {1, 3} is added to the coupling layer of
  each (3, 3) chain. The L3 test must report a failure at t = 1/2.
- **K-D1.**
  - The irreducibility test reports irreducible for the full Clifford integer-time group (R_self).
  - It reports reducible for R_cf's integer-time group alone, whenever that group has more than
    one orbit.
- **K-D2.** No certificate is issued for any integer-time generator, or for the words with h
  replaced by an integer-time image.
- **K-Lie.** The dropped-generator mutation (F2-1 A4) removes every translation from both
  repertoires. The algebra must fall below q^{2N} − 1.
- **K-touch.** For the principal member, "every orbit touched" must agree with the exact algebra
  dimension: touched everywhere implies full.
- **K-mod p.** A reduction modulo a prime splitting ℚ(ζ_n) is used only one-sided. A full result
  modulo p certifies the exact result; a deficient one is recomputed exactly and printed as such.

## Invariants of the execution and where each is measured (§A.41)

| invariant | checkpoint |
|---|---|
| Rules fixed before any computation | this file's commit precedes the script's; the result names both commits |
| F2-1's code unchanged | K0 hash |
| Exact arithmetic | K0 self-tests; every decisive line exact or one-sided modulo p as in K-mod p |
| Determinism | two runs, byte-identical output |
| Verdicts only over green controls | the verdict function prints `VERDICT VOID` if any control fails |

## Outcome classes

- **`E1L-LOCAL-CONSISTENT`**: L0, L1, L3 and C-OI hold.
- **`E1L-LOCAL-AND-SELF-CONTROLLING`**: in addition, `E1L-SELF-FULL` and `E1L-SELF-DENSE` hold
  at every control size, each with its stated scope.
- **R_cf results** are reported beside the verdict, with their scopes, and are not merged into it.
- **`E1L-NONLOCAL`**: L1 or L3 fails. **`E1L-INCONSISTENT`**: L0 or C-OI fails.

## Non-claims

- no general-N theorem, no kernel proof, nothing OI-derived;
- complex kinematics inherited;
- local continuity is an added physical hypothesis with control content T1–T3, not sourced;
- nothing about time-independent generators for a whole tick;
- nothing about minimality, about dimensions other than q^N, or about which alphabet nature uses.
