# F2-4 — control of E1-L across generator choices and sizes: rules fixed before the exact runs

Research design on a research branch. It is not a native round and not adopted, and it is not for
merge without separate review. This file is committed before any decisive computation of the round
is run.

Prior evidence, cited only as such:

- the F2-2 record `../f2-2-local-continuity/`: rules, result, and correction 1, which restricts
  E1-L to `Γ_comm`;
- the F2-3 record `../f2-3-commuting-family/`, whose open items this round takes up:
  - one-duration density over `Γ_diag` under both repertoires;
  - all-duration fullness under `R_cf` at `N ≥ 3`;
- the design evidence in `design/`, floating point and not a measurement.
  - `probe.py` builds `R_cf`'s integer-time orbits and the lines merged by the free half-layer
    alone, with a DFT standing in for `u`. Its findings:
    - one component at `(3,2)`, `(3,3)`, `(5,2)` and `(7,2)`, for every free pattern;
    - one orbit at `(3,3)`, `(5,3)`, `(3,4)` and `(7,3)`.
  - Exact timings: the one-site free half-layer's relation takes about 2 s at `q = 7` and about
    30 s at `q = 11`, per pattern.

## Framing (owner decision, 2026-10-15)

- **The question.**
  - Do F2-2's control results survive every admissible generator choice, in particular every
    diagonal logarithm choice?
  - Do they hold at every system size, not only at the computed ones?
- **Three kinds of statement, kept apart:**
  - universal robustness (every member of a stated family);
  - existence (some member);
  - generic behaviour (all members outside a stated exceptional set).
- **`R_cf` has priority.** `R_self` is reported separately as a positive control. Its results are
  not transferred to `R_cf`, and the reverse transfer is not made either.
- **Evidence levels.**
  - General claims over every odd prime `q` and every `N` need a written argument [W].
  - Computations are exact at the listed sizes only.
  - A modular rank is used only as a lower bound on a dimension, with its justification below.
- **Every result is conditional on E1-L.** That is R1–R4, `T_loc` and T1–T3, with F2-2's gates,
  repertoires, one generator per gate type, and correction 1's restriction to `Γ_comm`. Complex
  kinematics is inherited. Nothing here is physically sourced.

## Families

- **Coupling gates.** Every member of `Γ_comm`; at `N ≥ 3` this is `Γ_diag`, by F2-3 S4. One
  generator per gate type, as in F2-2.
- **Translations.** `Γ_all(X) = Γ_spec(X)`, since `X` has one-dimensional eigenspaces.
- **The free layer.**
  - `Γ_spec(u)`, the sign patterns of F2-2, for every one-duration statement.
  - `Γ_all(u)` only where a statement says so.

## The written statements [W] (proofs written in the result; each is checked exactly where listed)

- **AD (all-duration fullness).** Fix any odd prime `q`, any `N ≥ 1`, either repertoire, and every
  generator choice for which E1-L is defined. Then the all-duration algebra contains `su(q^N)`.
  The proof uses only:
  - (i) `u^{⊗N}` and every `X_k` are time-1 flows, so their adjoint actions preserve the algebra.
    So does conjugation by `Z_k ∝ u^{⊗N} X_k^{±1} (u^{⊗N})†`.
  - (ii) Every Weyl operator is therefore in the group. The complexified algebra is the span of
    the Weyl lines `W(v)` it contains, because distinct lines carry distinct characters of the
    Weyl group.
  - (iii) That set `S` of lines has three closure properties:
    - it is closed under `v ↦ −v`;
    - it is closed under the sitewise `J′`;
    - if `v, w ∈ S` and `⟨v,w⟩ ≢ 0`, then `v + w ∈ S`, because
      `[W(v), W(w)] = (τ^{⟨v,w⟩} − τ^{−⟨v,w⟩})W(v+w)`.
  - (iv) Each translation generator is a non-scalar function of `X_k`, so it puts some line
    `(a e_k, 0)` in `S`.
  - (v) A single-edge coupling is in both repertoires. Its pair generator is not a sum of one-site
    terms, since its exponential `δ_ij(m)` has operator-Schmidt rank `q`. So it puts in `S` a line
    supported on both sites.
  - (vi) A combinatorial lemma: from these seeds, the closure in (iii) is all of
    `𝔽_q^{2N} ∖ {0}`.
- **MONO (monotonicity).** Adding gates to a one-duration repertoire can only:
  - merge invariant blocks;
  - keep an element of infinite order.

  So if D1 and D2 hold for a sub-repertoire that contains no coupling half-layer, they hold for
  every choice of coupling generators.
- **PROD (D2 at every `N`).** If `hX` has infinite order modulo scalars on one site, then so does
  `h^{⊗N}X_1 = (hX) ⊗ h^{⊗(N−1)}` on `N` sites. This holds because `h` has finite order, being
  diagonalizable with root-of-unity eigenvalues.
- **RED (`R_cf`, `N ≥ 3`).** Every nonzero `v ∈ 𝔽_q^{2N}` lies in the orbit of a one-site vector
  under the symplectic part of `R_cf`'s integer-time group. For `N ≥ 2` and `c ≠ 0`, the one-site
  vectors `(x e_i, 0)` and `(−c x e_j, 0)` lie in one orbit.
  - The proof uses `L_M: (x,z) ↦ (x, z − Mx)` for zero-diagonal symmetric `M`, its conjugate by
    `J`, and `J` itself. A third site is needed when `x` has support on exactly two sites.
- **CHAIN (one-duration density at every `N`, `R_cf`).** Fix `q` and a free pattern `f`. Suppose
  that at `N = 1`:
  - `R_cf`'s integer-time group with `f`'s free half-layer acts irreducibly on `sl(q)`;
  - `hX` has infinite order modulo scalars.

  Suppose further that, at `N = 2`, the integer-time group with the free half-layer acts
  irreducibly on `sl(q²)`. Then for every `N ≥ 1` and every coupling choice in `Γ_comm`, the
  one-duration repertoire is dense in `SU(q^N)` modulo phases. The argument:
  - at `N = 2`, from the `N = 2` hypothesis;
  - at `N ≥ 3`:
    - by RED, every line is joined to a one-site line;
    - by the `N = 1` hypothesis, all one-site lines at a site are joined;
    - by RED, the one-site lines `(x e_i, 0)` at different sites are joined;
    - PROD gives D2;
    - MONO removes every dependence on coupling generators.
- **SP (`R_self`).** The symplectic part of `R_self`'s integer-time group is `Sp(2N, q)`, which is
  generated by the unipotent subgroups with arbitrary symmetric off-diagonal blocks. This is a
  standard fact, cited in the result. Hence:
  - D1 holds from the integer-time group alone, at every `N`;
  - one-duration density follows for every coupling choice and every free pattern with an `N = 1`
    D2 certificate.

## Cells and decision rules (each verdict is generated from its measurements)

All exact computations use F2-1's field `ℚ(ζ_{8q})` and F2-2's gate objects, imported by path. The
single exception is the modular Lie dimension in AD-X.

- **AD-X, corroboration of AD at `(3,2)`, `(3,3)` and `(5,2)` under `R_cf`.**
  - Three members:
    - **`M0`:** the principal member.
    - **`M1`:** every pair generator replaced by the bilinear lift `−m·ŷᵢŷⱼ/q`, with
      `ŷ ∈ {0, …, q−1}`. This lift lies in `Γ_diag` and outside `Γ_spec`.
    - **`M2`:** the principal pair generator plus the integer lift
      `n(y) = ((3ŷᵢ + 5ŷⱼ + m) mod 3) − 1`. The free pattern is the last in F2-2's order, and the
      translation lifts are `θ_j + (j mod 2)`.
  - The generators are F2-2's: the free layer, every nonzero coupling of `R_cf`, and every
    translation.
  - The dimension modulo the identity of the generated algebra is computed modulo a prime
    `p ≡ 1 (mod 8q)`, `p < 2²⁵`, with `ζ_{8q}` mapped to a primitive root.
    - The rank of a set of reductions is at most the rank over `ℚ(ζ_{8q})`. Brackets commute with
      reduction. So the modular dimension is a lower bound [W].
  - Token `F24-AD-FULL` at a size iff the bound equals `q^{2N} − 1` for all three members.
  - `R_self`'s principal member at `(3,2)` is computed beside it as a positive control.
- **OD-1, one site, at `q ∈ {3, 5, 7, 11, 13}`.** For every free pattern `f ∈ Γ_spec(u)`:
  - **D1 (`R_cf`).**
    - The lines `𝔽_q² ∖ {0}` are grouped by the orbits of `R_cf`'s integer-time symplectic part.
    - They are then joined by F2-2's exact `adjoint_relation` of `f`'s free half-layer, with its
      adjoint.
    - D1 holds iff one component remains.
  - **D2.** F2-2's certificate `|tr g|² ∉ ℤ[ζ]` is applied to the words `h·X`, `h·Z` and `h·XZ`, in
    that order. The first certified word is printed.
  - **D1 (`R_self`).** It holds iff `R_self`'s orbits form one orbit.
  - The token `F24-OD1(q)` reports `ALL`, `SOME` or `NONE` over the patterns, separately for D1
    (`R_cf`) and for D2.
- **OD-2, two sites, `R_cf`, at `q ∈ {3, 5, 7, 11, 13}`, coupling-free.** For every free pattern:
  - The lines of `𝔽_q⁴ ∖ {0}` are grouped by `R_cf`'s integer-time orbits.
  - They are joined by links of the free half-layer `h ⊗ h`.
    - The link set is `{(v₁,v₂) ~ (w₁,w₂) : wᵢ ∈ R(vᵢ)}`. Here `R` is OD-1's exact one-site
      relation, extended by `R(0) = {0}`; this is exact, by the tensor-product structure of
      `Ad_{h⊗h}`.
    - It is applied through a sound subset: each line is joined to the links with
      `w₂ = min R(v₂)`, and to those with `w₁ = min R(v₁)`.
    - If the subset does not give one component, the full link set is used.
  - Token `F24-OD2(q)`: `ALL`, `SOME` or `NONE`, by whether one component remains.
- **OD-3, RED corroborated at `(3,3)`, `(5,3)`, `(7,3)` and `(3,4)`.**
  - Every orbit of `R_cf`'s integer-time symplectic part must contain a one-site vector, by exact
    integer orbit enumeration.
  - Token `F24-OD3` iff so at every size. The orbit counts are printed.
- **Conclusions, generated.**
  - **`F24-CF-DENSE-ALL-N(q)`** iff `F24-OD1(q)` is `ALL` for both D1 and D2, and `F24-OD2(q)` is
    `ALL`. By CHAIN it reads: under `R_cf`, the one-duration repertoire is dense at every `N`, for
    every coupling choice in `Γ_comm` and every free pattern in `Γ_spec(u)`.
  - **`F24-SELF-DENSE-ALL-N(q)`** iff `F24-OD1(q)` D2 is `ALL`, by SP and PROD. It is the same
    statement under `R_self`.
  - **`F24-AD-GENERAL`** is AD [W], printed with the AD-X corroboration beside it.
- **Classification.** Each conclusion is stated in the three kinds of the framing:
  - coupling generators: universal (MONO);
  - `Γ_spec(u)`: universal at the listed `q` if `ALL`;
  - `Γ_all(u) ∖ Γ_spec(u)`: not decided. F2-2 recorded two Clifford square roots of `u` at
    `q = 7`.

## Controls (a failed control voids every verdict)

- **K0.**
  - The sha256 of the imported F2-1 module is `e7d257bb09f5b75d4628cd0ebd85a0b189d377b3bdf91a48fd1196705a31e7a6`.
  - The sha256 of the imported F2-2 module is `246adb2bc6590a3d84234f6937409f2042bba796d646eae633f6383a62a90e57`.
  - F2-1's self-tests pass.
- **K-frozen.** The run reproduces F2-2's recorded values:
  - `R_cf`'s orbit sizes at `(3,2)`: 8, 8, 16 and 48;
  - the free-pattern counts: 4, 8 and 8 at `q = 3`, 5 and 7;
  - `X_1` as the first certified word for every pattern at `q = 3`, 5 and 7;
  - the `(3,2)` dimensions modulo the identity: 80 for the principal member, and 22 (`R_cf`) and
    40 (`R_self`) without translations. These are reproduced by the modular computation.
- **K-indep.**
  - (i) At `(3,2)`, for every free pattern, OD-2's link set equals F2-2's exact `adjoint_relation`
    of `h ⊗ h`, computed on the 9×9 matrix.
  - (ii) At `(3,2)`, the modular dimension equals F2-1's exact `lie_closure_dim` for `M1`, `M2` and
    the two mutations below.
  - (iii) At `(3,2)`, the sound subset of OD-2 is contained in the exact relation.
- **K-D1neg.**
  - With the free half-layer removed, OD-1 and OD-2 report one component per orbit. That is
    `(q² − 1)/4` at `N = 1` and the orbit count at `N = 2`, at every `q`.
  - With the free half-layer replaced by `u`, which is Clifford, the same counts are reported.
- **K-D2neg.** No certificate is issued on `X`, on `u` or on `u·X`.
- **K-AD-mut.** The bound falls below `q^{2N} − 1` at `(3,2)` and `(3,3)` in two mutations:
  - with the translations removed;
  - with every pair generator replaced by the local `Y ⊗ 1 + 1 ⊗ Y`, where `Y = diag(0, …, q−1)/q`.

  These show that hypotheses (iv) and (v) of AD do work.

## Invariants of the execution and where each is measured (§A.41)

| invariant | checkpoint |
| --- | --- |
| Rules fixed before any decisive computation | this file's commit precedes the script's; the result names both |
| F2-1 and F2-2 code unchanged | K0 hashes |
| Exact arithmetic, except the modular lower bound | K0 self-tests; K-indep (ii) ties the bound to an exact value |
| Conventions match F2-2's | K-frozen |
| Determinism | two runs, byte-identical output |
| Verdicts only over green controls | the verdict function prints `VERDICT VOID` if any control fails |

## Outcome classes

- **`F24-ROBUST-GENERAL`.** Both conclusions hold at every listed `q`, `F24-OD3` holds, and
  `F24-AD-FULL` holds at every AD-X size.
- **`F24-PARTIAL`.** Otherwise. The failing cells are listed with their members.

## Non-claims

- One-duration statements are not claimed for any `q` beyond those listed: CHAIN needs the `N = 1`
  and `N = 2` certificates at each `q`.
- Nothing is claimed about:
  - `Γ_all(u) ∖ Γ_spec(u)`;
  - time-independent generators for a whole tick;
  - orientations other than `i < j`.
- Density is not exactness. The one-duration sets are countable, and exact availability from all
  durations rests on Jurdjevic–Sussmann [L].
- Unitary control does not give preparations, measurements, state preservation, ancillas or
  composites. They are not inferred here, and the result states what they would require.
- No kernel proof. Nothing is physically sourced. Local continuity and `Γ_comm` remain added
  hypotheses.
