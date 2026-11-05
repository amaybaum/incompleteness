# OI-QM-SEL M-2: separating power of C-pers on the M-1 instance (result)

**Status: WIP / UNVERIFIED. Independently model-reviewed: ACCEPT WITH CHANGES, no material findings (#1149
c.6668322323); fixes applied; delta check pending; merge not authorized.** Paper-only. Writer: `writer-m2`.
**Preregistration:** `PREREG.md` in this directory.
- Frozen at `Φ` = `be5e6311403db36b08cde2e4b0989eb8d57b5fab`, after the r3 delta review ACCEPT (PR #1149 c.6666080040).
- Instance bound by `B_I` = `7f9e6b6d00ff3be21ec9ed6b824ecde58f16f00f`, which changes §4 only.

This file is added by the commit after `B_I` and changes no other file. Definitions, controls and the decision rule are
applied as frozen. Nothing was adjusted, and no other pair was examined.

**Authorization.**
- #1031 c.6665461411 (M-2), quoted in PREREG §0.
- #1031 c.6666613671 (amaybaum, Claude Code session chat, 2026-11-05, before 19:00Z): "Once #1151 is safely landed,
  M-2 may proceed under its existing authorization". #1151 landed as the true merge `f810f5ee`.

**Base.**
- The branch integrated `origin/main` `6bf811ae0e97a53b770c53fafa601a3a023605a8` before `Φ`.
- PREREG's path:line citations are read at `f051916a113c9412b3efbb1ff813ec57c2ed265d`, as PREREG states.
- M-1's lines are read at `f810f5eea50807a375878d266192115a6b314ab0`.

**Method:** hand algebra in exact arithmetic. No script, CAS, numerical evaluation, enumeration or search. Every value
below is written out.

**Notation.**
- Basis order `p₀ = (0,a₀)`, `p₁ = (0,a₁)`, `p₂ = (1,a₀)`, `p₃ = (1,a₁)`; `e₀ = p₀`, `e₁ = p₂` (PREREG §4.1).
- Fibre 0 is `span{p₀,p₁}` and fibre 1 is `span{p₂,p₃}`; `P_v` projects onto fibre `v`.
- `X` denotes `W` (for `U`) or `W′` (for `U′`).

The columns, read from the matrices bound in PREREG §4.1:

| Column | `W` | `W′` |
|---|---|---|
| at `p₀` | `½(1,1,1,1)` | `½(1,1,1,1)` |
| at `p₁` | `½(1,−1,1,−1)` | `½(1,1,−1,−1)` |
| at `p₂` | `½(1,1,−1,−1)` | `½(1,−1,1,−1)` |
| at `p₃` | `½(1,−1,−1,1)` | `½(1,−1,−1,1)` |

`W` and `W′` are real and symmetric (each equals its transpose, entry by entry), so `Xᴴ = X`. Their unitarity is M-1's
K-a. It is used here only through `XXᴴ = 1`, which M-1 `RESULT.md` §1 establishes on `main`.

***

## §1. L-0: the C-pers law of the instance, from the procedures

**The procedure, written once and used for every lift in this record.**
1. **Root.** `e_j`.
2. **Evolve and read at `s`.** Compute the full vector `U_se_j ∈ ℂ^{V×A}`. The Lüders read `P_{v₁}` leaves the
   unnormalized vector `x := P_{v₁}U_se_j`, every ancilla component kept. No reset, test, dephasing or renormalization
   is applied.
3. **Evolve and read at `t`.** Apply the full matrix `T_{t,s} = U_tU_sᴴ` to `x`. The read `P_{v₂}` gives `P_{v₂}T_{t,s}x`.
4. **Mass.** `p(v₁,v₂ | j; s,t) = ‖P_{v₂}T_{t,s}x‖²`.

This is PREREG §3's mass. No failure record exists (PREREG (p4)).

**Relative objects.** `U_t = I` for even `t` and `X` for odd `t`. Hence `T_{t,s}` is:
- `I·I = I` when `s` and `t` are both even;
- `XXᴴ = I` when both are odd;
- `X·I = X` when `s` is even and `t` odd;
- `I·Xᴴ = X` when `s` is odd and `t` even.

So the four cases below, indexed by the parity of `s` and the parity of `t − s`, cover every `s < t` in `ℕ` (K-H).

**Case EE** (`s` even, `t − s` even): `U_s = I`, `T = I`. `x = P_{v₁}e_j = δ_{v₁j}e_j`, and `P_{v₂}x = δ_{v₂v₁}x`. Mass
`δ_{v₁j}δ_{v₂v₁}`, for both lifts.

**Case EO** (`s` even, `t − s` odd): `U_s = I`, `T = X`. `x = δ_{v₁j}e_j`, and the mass is
`δ_{v₁j}‖P_{v₂}Xe_j‖²`. From the column table:
- `Xe₀ = ½(1,1,1,1)` for both lifts;
- `We₁ = ½(1,1,−1,−1)` and `W′e₁ = ½(1,−1,1,−1)`.

Each fibre part has squared norm `¼ + ¼ = ½`. So the mass is `δ_{v₁j}·½`, for both lifts.

**Case OE** (`s` odd, `t − s` even): `U_s = X`, `T = I`. The mass is `‖P_{v₂}P_{v₁}Xe_j‖² = δ_{v₂v₁}‖P_{v₁}Xe_j‖²`, which
is `δ_{v₂v₁}·½` by the same fibre parts, for both lifts.

**Case OO** (`s` odd, `t − s` odd, so `t` even): `U_s = X`, `T = X`. The mass is `‖P_{v₂}XP_{v₁}Xe_j‖²`.

*Lift `U` (`X = W`).*
- Post-read vectors:
  - `P₀We₀ = ½(p₀+p₁)` and `P₁We₀ = ½(p₂+p₃)`;
  - `P₀We₁ = ½(p₀+p₁)` and `P₁We₁ = −½(p₂+p₃)`.
- `W(p₀+p₁) = ½(1,1,1,1) + ½(1,−1,1,−1) = (1,0,1,0) = p₀ + p₂`.
- `W(p₂+p₃) = ½(1,1,−1,−1) + ½(1,−1,−1,1) = (1,0,−1,0) = p₀ − p₂`.

| `j` | `v₁` | `x` | `Wx` | mass `v₂ = 0` | mass `v₂ = 1` |
|---|---|---|---|---|---|
| 0 | 0 | `½(p₀+p₁)` | `½(p₀+p₂)` | `¼` | `¼` |
| 0 | 1 | `½(p₂+p₃)` | `½(p₀−p₂)` | `¼` | `¼` |
| 1 | 0 | `½(p₀+p₁)` | `½(p₀+p₂)` | `¼` | `¼` |
| 1 | 1 | `−½(p₂+p₃)` | `−½(p₀−p₂)` | `¼` | `¼` |

*Lift `U′` (`X = W′`).*
- Post-read vectors:
  - `P₀W′e₀ = ½(p₀+p₁)` and `P₁W′e₀ = ½(p₂+p₃)`;
  - `P₀W′e₁ = ½(p₀−p₁)` and `P₁W′e₁ = ½(p₂−p₃)`.
- `W′(p₀+p₁) = ½(1,1,1,1) + ½(1,1,−1,−1) = (1,1,0,0) = p₀ + p₁`.
- `W′(p₂+p₃) = ½(1,−1,1,−1) + ½(1,−1,−1,1) = (1,−1,0,0) = p₀ − p₁`.
- `W′(p₀−p₁) = ½(1,1,1,1) − ½(1,1,−1,−1) = (0,0,1,1) = p₂ + p₃`.
- `W′(p₂−p₃) = ½(1,−1,1,−1) − ½(1,−1,−1,1) = (0,0,1,−1) = p₂ − p₃`.

| `j` | `v₁` | `x` | `W′x` | mass `v₂ = 0` | mass `v₂ = 1` |
|---|---|---|---|---|---|
| 0 | 0 | `½(p₀+p₁)` | `½(p₀+p₁)` | `½` | `0` |
| 0 | 1 | `½(p₂+p₃)` | `½(p₀−p₁)` | `½` | `0` |
| 1 | 0 | `½(p₀−p₁)` | `½(p₂+p₃)` | `0` | `½` |
| 1 | 1 | `½(p₂−p₃)` | `½(p₂−p₃)` | `0` | `½` |

So in case OO, `p_U = ¼` for every `(j, v₁, v₂)`, while `p_U′(v₁, v₂ | j) = ½·δ_{v₂j}`.

**Summary of `Λ_C-pers`** for the bound pair, every `s < t` in `ℕ`:

| parity of `s` | parity of `t − s` | `p_U(v₁,v₂ \| j)` | `p_U′(v₁,v₂ \| j)` |
|---|---|---|---|
| even | even | `δ_{v₁j}δ_{v₂v₁}` | `δ_{v₁j}δ_{v₂v₁}` |
| even | odd | `½·δ_{v₁j}` | `½·δ_{v₁j}` |
| odd | even | `½·δ_{v₂v₁}` | `½·δ_{v₂v₁}` |
| odd | odd | `¼` | `½·δ_{v₂j}` |

**Extension to `|A| = m ≥ 3`** (PREREG §4.1, the bound pair's extension). The slices are `I`, `X ⊕ 1`. The vectors
`e_j`, `x` and `Xx` above lie in `span{p₀,…,p₃}`, which `X ⊕ 1` maps as `X` does, and every `P_v` preserves that span.
So every mass above is unchanged at every `|A| ≥ 2`.

**L-0: pass.**

## §2. L-1 to L-3 and D-1, re-derived (K5)

- **L-1.** `{P_v}` are orthogonal projectors summing to `1`, and `T` is unitary. So
  `Σ_{v₁,v₂}‖P_{v₂}TP_{v₁}U_se_j‖² = Σ_{v₁}‖TP_{v₁}U_se_j‖² = Σ_{v₁}‖P_{v₁}U_se_j‖² = ‖U_se_j‖² = 1`.
  - On the instance, every row of the summary table sums to 1 over `(v₁, v₂)`:
    - EE: `1`;
    - EO: `½ + ½`;
    - OE: `½ + ½`;
    - OO: `4·¼` for `U`, and `½ + ½` for `U′`.
- **L-2.** `Σ_{v₂}‖P_{v₂}y‖² = ‖y‖²`, with `y = TP_{v₁}U_se_j` and `‖y‖ = ‖P_{v₁}U_se_j‖`. So the marginal over `v₂` is
  `Γ_s(v₁, j)`.
- **L-3.** At `|A| = 1`, `P_{v₁}U_se_j = U_s(v₁,j)e_{v₁}`. So
  `p = |U_s(v₁,j)|²·‖P_{v₂}Te_{v₁}‖² = Γ_s(v₁,j)·𝒪₂(t,s)(v₂,v₁) = r_U`.
- **D-1.** Under (t1) and (t2), the T-V procedure has:
  - root `ρ̃ = |j⟩⟨j| ⊗ |a₀⟩⟨a₀| = e_je_jᴴ`, evolved by `U_s`;
  - the Lüders instrument `ρ ↦ |v₁⟩⟨v₁|ρ|v₁⟩` on `V`, acting as `P_{v₁}·P_{v₁}` on `V × A`;
  - then evolution by `U_tU_sᴴ` and the Lüders instrument for `v₂`.

  Its branch has trace `‖P_{v₂}TP_{v₁}U_se_j‖²`, which is the C-pers mass. So `Λ_C-pers` is a subfamily of `Λ_T-V`,
  and `O_T-V ⇒ O_C-pers`.

**Pass.**

## §3. Controls

### K1 (positive gauge control)
- **General argument.** `U^M_t := LU_t` with constant `L = 1_V ⊗ H₂` is the case `L_t ≡ L` of K-B (i) below. So
  `Λ_C-pers(LU) = Λ_C-pers(U)` for every record.
- **Explicit check at a separating procedure** (case OO; `j = 0`, `(s,t) = (1,2)`, `(v₁,v₂) = (0,0)`).
  - `LWe₀ = L·½(1,1,1,1) = (1/√2)(1,0,1,0)`, so `x′ = P₀LWe₀ = p₀/√2`.
  - `T′_{2,1} = L·(LW)ᴴ = LWL`, using `Lᴴ = L` and `Wᴴ = W`.
  - `L(p₀/√2) = ½(p₀+p₁)`, then `W` gives `½(p₀+p₂)`, then `L` gives `½·(1/√2)(p₀+p₁+p₂+p₃)`.
  - Its fibre-0 part `(1/(2√2))(p₀+p₁)` has mass `2/8 = ¼`. This equals `p_U = ¼`.

**K1: pass.**

### K-B (invariance of the law)
- **(i) Time-dependent `L_t ∈ 𝒢_L`.**
  - `U′_t = L_tU_t` gives `T′ = L_tTL_sᴴ`, and `P_{v₂}T′P_{v₁}U′_se_j = P_{v₂}L_tTL_sᴴP_{v₁}L_sU_se_j`.
  - `L_s` is block-diagonal across fibres, so it commutes with `P_{v₁}`, and `L_sᴴP_{v₁}L_s = P_{v₁}`.
  - `P_{v₂}L_t = L_tP_{v₂}`, and `L_t` is unitary.
  - So the norm equals `‖P_{v₂}TP_{v₁}U_se_j‖`.
- **(ii) Constant weak `K`.**
  - `U′_t = U_tK` gives `T′ = U_tKKᴴU_sᴴ = T`.
  - `U′_se_j = c_jU_se_j`, with `|c_j| = 1` (CLG:146).
  - So every mass is unchanged.
- **No step uses an `a₀` reset frame.** The anchor enters only through the root `e_j`.

**K-B: pass.**

### K2 (`|A| = 1` countercontrol and reset-form cross-check)
- **(i)** L-3 holds (§2).
- **(ii)** The reset form `r = Γ_s(v₁,j)·𝒪₂(t,s)(v₂,v₁)` is evaluated on the instance from the slice data of §1:
  - `Γ_s = 1` for even `s` and `½` for odd `s`;
  - `𝒪₂ = δ` for `T = I`, and `‖P_{v₂}Xe_{v₁}‖² = ½` for `T = X`.

  It gives, for both lifts:
  - EE: `δ_{v₁j}δ_{v₂v₁}`;
  - EO: `δ_{v₁j}·½`;
  - OE: `½·δ_{v₂v₁}`;
  - OO: `½·½ = ¼`.

  These are, row by row, M-1's two-read C2-ch masses quoted in PREREG §4.1 (M-1 `RESULT.md` ll. 129–134).
  - Coverage: every record `(j; s,t; v₁,v₂)` over one period of the slices (period 2), hence every `s < t` (K-H).
  - No mismatch.

**K2: pass.**

### K3 (fixed-basis control)
L-2 holds. On the instance the marginals of the summary table over `v₂` are:
- for even `s`: `δ_{v₁j}`;
- for odd `s`: `½`, from `¼ + ¼` for `U` and from `½δ_{0j} + ½δ_{1j} = ½` for `U′`.

These equal M-1's C0 laws quoted in PREREG §4.1.

**K3: pass.**

### K5 (re-derivation)
- L-0 (§1), L-1 to L-3 and D-1 (§2), WD (K11) and the K-P values (K-P) are derived in this record.
- No B4 [D] or RES result is a premise.
- G-M1 (a)–(d) enter through G-M1 only (PREREG §4.1).

**K5: pass.**

### K7 (masses)
No normalization, conditioning or postselection is used. The `⊥` set is empty (PREREG (p4)). L-1 holds.

**K7: pass.**

### K9 (no imposed coherence)
- Roots are `e_j` only.
- No P-coh, `ρ₊` or phase is chosen apart from the lift.
- There is no reset.
- The ancilla components of `x` in §1 come from `U_s = X` alone.

**K9: pass.**

### K10 (adjustability)
Every reading is fixed: (p1)–(p4), (t1), (t2), (r1). Every read pair `s < t` is covered by the four parity cases. The
remaining freedom, `|A| = 2` or `|A| ≥ 3`, gives the same masses (§1, extension).

The outcome is the same for every admissible value. **K10: pass.**

### K11 (positive sensitivity, WD)
WD at the instance's `|A| = 2`:
- `H` acts as `H₂` on `span{p₀,p₂}` and as the identity on `p₁, p₃`.
- `U^D_t = I` for even `t` and `H` for odd `t`.
- `g` has `L ≡ 1`, `K_1 = Z` (with `Zp₂ = −p₂`, identity elsewhere) and `K_t = 1` otherwise. So `(gU^D)_1 = HZ` and
  `(gU^D)_t = U^D_t` otherwise.
- Procedure: root `j = 0`, reads `(1, 3)`.

Values:
- **`U^D`:** `x = P₀Hp₀ = P₀(p₀+p₂)/√2 = p₀/√2`. `T_{3,1} = HHᴴ = I`. So `p(0,0) = ½` and `p(0,1) = 0`.
- **`gU^D`:** `x = P₀HZp₀ = P₀Hp₀ = p₀/√2`. `T_{3,1} = H(HZ)ᴴ = HZH`.
  - On `span{p₀,p₂}`, `H₂ZH₂ = ½[[1,1],[1,−1]]·[[1,1],[−1,1]] = ½[[0,2],[2,0]] = [[0,1],[1,0]]`.
  - So `T(p₀/√2) = p₂/√2`, and `p(0,0) = 0`, `p(0,1) = ½`.

The laws differ: `(½, 0)` against `(0, ½)`. **K11: pass.**

### K-P (retention of ancilla coherence; PREREG §6.1)
The procedure of §1, unchanged, is applied to the K-P lifts, with root `j = 0` and reads `(0, 1)`. `L = 1_V ⊗ H₂`, and
`Q` exchanges `p₁` and `p₂`.

**`U^C`** (`U^C_0 = L`, `U^C_t = Q` for `t ≥ 1`).
- `x = P₀Lp₀ = P₀(p₀+p₁)/√2 = (p₀+p₁)/√2`. `T_{1,0} = QLᴴ = QL`.
- **C-pers mass:** `L(p₀+p₁)/√2 = ½[(p₀+p₁) + (p₀−p₁)] = p₀`, and `Qp₀ = p₀`. So **`p(0,0) = 1`**.
- **Reset form:** `Γ_0(0,0) = ‖P₀Lp₀‖² = 1`. `𝒪₂(1,0)(0,0) = ‖P₀QLp₀‖²`, with `QLp₀ = Q(p₀+p₁)/√2 = (p₀+p₂)/√2`, so it
  is `½`. Hence **`r(0,0) = ½`**.

**`U^P`** (`U^P_0 = L`, `U^P_t = QL` for `t ≥ 1`).
- `x = (p₀+p₁)/√2` as above. `T_{1,0} = QLLᴴ = Q`.
- **C-pers masses:** `Qx = (p₀+p₂)/√2`. So **`p(0,0) = ½`** and **`p(0,1) = ½`**.
- **Reset form:** `Γ_0(0,0) = 1`, and `𝒪₂(1,0)(0,0) = ‖P₀Qp₀‖² = ‖p₀‖² = 1`. Hence **`r(0,0) = 1`**.

All five values equal the frozen values (`U^C`: `p = 1`, `r = ½`; `U^P`: `p = ½, ½`, `r = 1`). They were obtained by the
same written procedure as the instance (§1). **K-P: pass.**

### K12 (device identity)
The two lifts are compared under the same roots, read pairs, projectors `P_v`, anchor `a₀` and decoder `(v₁, v₂)`.
Only `U ↦ U′` changes. **K12: pass.**

### K-D (same `Γ`)
`Γ = (1, J/2, 1, J/2, …)` for both lifts, from M-1 through G-M1 (PREREG §4.1; M-1 `RESULT.md` §3). It is also visible
in §1: the post-read vectors at odd `s` all have squared norm `½`. **K-D: pass.**

### K-H (ℕ coverage)
Both lifts have slices of period 2. The relative object depends only on the parities of `s` and `t`. The four parity
cases cover every `s < t` in `ℕ`, `s = 0` included. **K-H: pass.**

### K13 (joint-lift nativeness; conditional; reported)
- **Membership.** The visible family `Γ = (1, J/2, 1, J/2, …)` is in `PPer` in either orientation (G-M1 (d), M-1 K-b).
- **Joint process.** C-pers adds no preparation interaction, so the joint process is the lift itself.
- **Nativeness.** Reading "in `PPer`" as "native" is CONDITIONAL[F3's hypothesis; S-0]. S-0 (a defined `L_native` and a
  realization→lift correspondence) is not defined on `main`. So K13 is a necessary check only, and it is met.

**Control table.**

| Control | Result | Where |
|---|---|---|
| L-0 (law from procedures) | pass | §1 |
| L-1, L-2, L-3, D-1 | pass | §2 |
| K1 positive gauge control | pass | §3 K1 |
| K-B invariance | pass | §3 K-B |
| K2 (i) L-3; (ii) reset form = M-1's C2-ch masses, all records over one period | pass | §3 K2 |
| K3 marginals = M-1's C0 laws | pass | §3 K3 |
| K5 re-derivation | pass | §3 K5 |
| K7 masses | pass | §3 K7 |
| K9 no imposed coherence | pass | §3 K9 |
| K10 adjustability | pass | §3 K10 |
| K11 WD sensitivity | pass: `(½,0)` against `(0,½)` | §3 K11 |
| K-P coherence retention, exact values | pass: `U^C` `p = 1`, `r = ½`; `U^P` `p = ½, ½`, `r = 1` | §3 K-P |
| K12 device identity | pass | §3 K12 |
| K-D same `Γ` | pass | §3 K-D |
| K-H ℕ coverage | pass | §3 K-H |
| K13 (reported) | `PPer`, either orientation; nativeness CONDITIONAL[F3; S-0], necessary check only | §3 K13 |

## §4. Outcome, from the decision rule (PREREG §7.2)

Each outcome is checked in the frozen order, and the first that applies is the outcome:
1. **NOT-EVALUATED:** does not apply. G-M1 holds (PREREG §4.1).
2. **VOID:** does not apply.
   - Every listed control passes, and none is vacuous.
   - L-0 to L-3 are derived.
   - Every definition read matches its source line.
   - The bound instance is M-1's pair, verbatim.
3. **UNDECIDED:** does not apply. Equality and inequality are settled for every `s < t` by the parity cases, and no
   freedom changes the outcome (K10).
4. **SEPARATES:** applies. Case OO gives `p_U ≠ p_U′` for every `j` and every record.

**Separating record, written out.** Root `j = 0`, reads `(s, t) = (1, 2)`, record `(v₁, v₂) = (0, 0)`:
- `p_U = ‖P₀·½(p₀+p₂)‖² = ¼`;
- `p_U′ = ‖P₀·½(p₀+p₁)‖² = ½`.

**Every separating `(j; s, t)`, up to the period 2 of the slices.** These are exactly the procedures with `s` odd and
`t − s` odd (that is, `s` odd and `t` even), for both roots `j ∈ {0, 1}`.
- Every record of such a procedure separates: `¼` against `½` or `0`.
- No procedure with `s` even, or with `t − s` even, separates.
- The earliest separating read pair is `(1, 2)`.

**Verdict: SEPARATES[C-pers; M-1 instance `U = (I,W,I,W,…)`, `U′ = (I,W′,I,W′,…)`; `|V| = 2`, `|A| ≥ 2`; `PPer`].**

**K13 (reported with the outcome, PREREG §7.2):** the visible family `Γ = (1, J/2, 1, J/2, …)` is in `PPer` in either
orientation (G-M1 (d)). Reading this as nativeness is CONDITIONAL[F3's hypothesis; S-0]. S-0 is undefined on `main`,
so K13 is a necessary check only. It does not change the outcome.

## §5. Consequences (PREREG §7.3, applied as frozen)

- **Qualification.** C-pers meets SPEC §4.3's qualification clause on this instance: its separating power is
  established mathematically, through M-2. **This record does not adopt SPEC §4.3's selection.** As PREREG §7.3
  proposes, the selection is re-checked with H-comp counted, by owner decision, before any native freeze. #1143 is the
  accountable Issue.
- **Redo rule.** It is not triggered. M-1 reports that C2-ch and C2-sel do not separate the instance: "LAWS-EQUAL" for
  every root, read list and record (M-1 `RESULT.md` §4.3, §4.4; quoted in PREREG §4.1).
- **Persistence attribution**, per procedure `(j; s, t)`. For each separating procedure (`s` odd, `t` even, either `j`):
  - M-1's C2-ch law for the read list `(s, t)` from root `j` is `¼` for every record, for both lifts. It is equal.
  - M-1's C2-sel law for that read list is equal for both lifts (LAWS-EQUAL, every read list and record, `⊥`
    included).

  So no separating procedure of C-pers is separated by either reset class. Every C-pers separation on this instance is
  attributed to the persistent ancilla.

| `(j; s, t)` class | C-pers | C2-ch (M-1) | C2-sel (M-1) | Attributed to persistence |
|---|---|---|---|---|
| `s` odd, `t` even, `j = 0` | separates | equal | equal | yes |
| `s` odd, `t` even, `j = 1` | separates | equal | equal | yes |
| any other | equal | equal | equal | — |

- **Mechanism** (a reading of §1; ELABORATING). In case OO the second evolution acts on `x = P_{v₁}Xe_j`, which keeps the
  ancilla components and their relative sign.
  - `W′` maps each such `x` back into a single fibre, the fibre `j`.
  - `W` spreads each such `x` evenly over both fibres.
  - With the reset, `x` is replaced by `e_{v₁}`, and that difference does not enter (K2 (ii)).
  - **Dephasing control** (re-derived by hand). Dephasing the ancilla in the basis `{|a⟩}` after the first read
    replaces `x` by its two components `x_a = ⟨(v₁,a), x⟩·(v₁,a)`, `a ∈ {a₀, a₁}`, as a mixture. Every entry of `W` and
    `W′` is `±½`, so each component has amplitude `±½`. Then `Xx_a` has four entries of modulus `¼`, and its
    fibre-`v₂` part has mass `2·(1/16) = ⅛`. The case-OO mass is `⅛ + ⅛ = ¼` for every `(j, v₁, v₂)`, for both lifts.
    So under dephasing the lifts are not separated. The separation needs retained ancilla coherence, which is the
    mode K-P certifies on `U^C`.
  - This agrees with M-1's assumption-watch marker (M-1 `RESULT.md` ll. 383–387): phase information within a fibre is
    discarded by the resets, and survives without them.
- **Unchanged.** SPEC's present verdict, UNSOURCED, for every declared interface. This mathematical separation, with no
  sourced access, is a scoped gap.

## §6. Scope

**Established here** (paper derivation in exact arithmetic; independent review pending):
- On M-1's alternating-`W` pair, the C-pers complete-record laws differ, at `|V| = 2`, `|A| ≥ 2`, with the visible
  family in `PPer`.
- C-pers uses configuration-only preparation, two Lüders reads on `V`, a persistent ancilla, and no reset or imposed
  coherence.
- Since C-pers is a T-V procedure class (D-1), under (t1) and (t2) this is a T-V separation of the pair that needs no
  coherent preparation.
- Read about OI, it is CONDITIONAL[P-conf, Acc_pers, Rd, H-comp, Rst-none with `A` persisting, fixed `a₀`, (r1),
  (p1)–(p4), (t1), (t2)].
- K-P shows that the computation retains ancilla coherence on the K-P lift `U^C`, and populations on `U^P`.

**Not established.**
- Physical availability of C-pers.
  - H-comp is a SOURCING-GAP at #866 (B4 ll. 381–383 at `f051916a`).
  - Retention of `A` across the reads (S-8, O-RET) is a SOURCING-GAP at #1032.
  - P-conf, Rd and the record (S-1, S-2, S-4, S-5) are SOURCING-GAPs as listed in PREREG §8.
- Native OI realizability of the pair or of C-pers. `PPer` membership is not nativeness (K13), and S-0 is undefined.
- That native OI access distinguishes the pair. Any physical OI–QM difference or equivalence.
- Any statement about another pair, another read count or another class.
- The selection of SPEC §4.3. It waits for the owner re-check (§5).
- A theorem promotion, Lean statement or manuscript claim.
- That C-pers resolves `G`-classes. `Λ_C-pers` is invariant under time-dependent `L_t` and constant weak `K` (K-B), but
  not under time-dependent weak `K_t`, which `TwoSidedRelated` (TSG:84–87) allows. K11's WD is a `G`-related pair that
  C-pers separates. That the instance is not `G`-related rests on M-1 `RESULT.md` §9, not on this record.

## §7. Deviations from the frozen plan, and notes

- **None in definitions, controls or decision rule.** Everything was applied as frozen at `Φ`, with the instance bound
  at `B_I`.
- **Base integration.** Before `Φ` the branch merged `origin/main` at `6bf811ae`, by a true merge commit
  `84a012766059edce380d59fbc61d011e919fc7ef`, with no conflicts. That brought in M-1 and #1148.
  - #1148 edited the status lines of B4 and RES. Checked line by line between `f051916a` and this branch:
    - B4 ll. 3–4 and l. 604 at `f051916a` are rewritten;
    - ll. 5–603 move down by 5 on `main`;
    - ll. 605–608 move down by 6.
  - Every B4 line cited by PREREG or this record lies in ll. 5–603: ll. 33–34, 35, 40, 41–43, 58–60, 148–151, 229–230,
    309–315 and 381–383.
  - PREREG and this record cite B4, SC, RES and QP at `f051916a`, as PREREG's base line states. Those citations are
    unaffected.
- **Stale draft-time wording kept, by the freeze rule.** These words lie inside frozen sections, or in §12, which the
  freeze left unchanged:
  - the headings of PREREG §2 ("frozen at the freeze commit; draft now") and §7 ("fixed at the freeze; draft now");
  - PREREG §12 ("A delta review of r3 is required before the freeze").
  - Three passages that `B_I` supersedes:
    - PREREG l. 7, "The test instance is a placeholder (§4)";
    - the M-1 row of PREREG §10, "Not yet on `main`; PR #1151 is not merged … until then G-M1 fails";
    - PREREG H7, "M-1 is not landed, so G-M1 does not yet hold".

    Each described the state before `B_I`. §4.1 records that M-1 landed and that G-M1 holds.

  Changing them at `Φ`, or outside §4 at `B_I`, would have exceeded what those commits may change. They do not affect
  any definition or rule.
- **Not applied at `Φ`.** REV3's optional nits (#1149 c.6666080040) were not applied. Nit 2 (a K-P embedding clause for
  `|A| > 2`) is moot: the K-P lifts were evaluated at `|A| = 2`, their frozen dimension.
- **§9 row 1 checkpoint.** It requires a reviewer to read every commit between `Φ` and the `RESULT.md` commit
  `ee394ffc`, which is `B_I` only, and record that none states a C-pers law of the instance. The independent review
  records that it holds (#1149 c.6668322323).

## §8. Premise ledger (§A.42 item 8)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| M-1 record at `f810f5ee` (`PREREG.md` §2; `RESULT.md` §§3, 4.2–4.4, 8, 11) | The instance; G-M1 (a)–(d); K2 (ii), K3 and attribution inputs | Support on `main`. Independently reviewed (#1151 c.6665869201) and delta-checked (c.6665968807). Those reviews are recorded in comments, which are provenance |
| #1031 c.6665461411, c.6666613671 | Authorization | Provenance; owner designations quoted with author and time |
| SPEC (#1143 c.6665278924), via PREREG Appendix A | §5 consequences | As classified in PREREG §10: support off `main`, closed by verbatim quotation and by narrowing (selection not adopted) |
| PR #1149 reviews (c.6665799329, c.6665974132, c.6666080040) | PREREG's review history | Provenance |
| Kernel line CLG:146; B4/SC definitions | K-B (ii); definitions | Support on `main` (read at `f051916a`) |
| The commit order `Φ` (`be5e6311`) → `B_I` (`7f9e6b6d`) → the `RESULT.md` commit `ee394ffc`, on PR #1149's branch | The freeze-before-binding-before-evaluation invariant (PREREG §9 row 1) | **Support off `main` until landing.** The invariant uses the order and ancestry of these commits. The gap closes only if the branch lands by a true merge commit, with no squash and no rebase-merge, so that all three commits become reachable from `main` (§A.42 item 3), as M-1's record required (M-1 `RESULT.md` §15) |

**Checks run at this commit:** `tools/artifact_placement_check.py` and `tools/duplicate_check.py`.

## §9. Review and next steps

- Independent review (PREREG §7.1 step 6): ACCEPT WITH CHANGES, no material findings (#1149 c.6668322323); its fixes
  are applied, and a delta check is pending.
- Merge is not authorized.
- If merge is authorized, the pull request lands by a true merge commit, with no squash and no rebase, so that `Φ`,
  `B_I` and `ee394ffc` stay reachable from `main` (§A.42 item 3; §8).
- The selection under SPEC §4.3 is not made here. Its re-check, with H-comp counted, is proposed to the owner under
  #1143.
