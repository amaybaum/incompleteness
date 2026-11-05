# OI-QM-SEL M-1: verification of the alternating-W candidate (result)

**Status: WIP / UNVERIFIED. Independent review pending; merge not authorized.** Paper-only. Writer: `writer-m1`.
**Preregistration:** `PREREG.md` in this directory, frozen at commit `7f3e8ffa99a3f841ca1e0c30691b236287c14a20`, pushed,
and the guiding draft pull request #1151 opened, before any computation below. This file is added by the next commit
and changes no other file. The pair, the controls and the decision rule are applied as frozen; nothing was adjusted, and
no other pair was examined.
**Authorization:** owner ruling #1031 c.6665461411 (pointer #1143 c.6665466217), quoted verbatim in PREREG §0.
**Base:** `origin/main` `f051916a113c9412b3efbb1ff813ec57c2ed265d`. Citations and abbreviations as in PREREG §1.
**Method:** hand algebra in exact arithmetic. No script, CAS, numerical evaluation, enumeration or search was used.
Every value below is written out.

**Notation.** Basis order `p₀ = (0,a₀)`, `p₁ = (0,a₁)`, `p₂ = (1,a₀)`, `p₃ = (1,a₁)`; vectors are coordinate tuples in
this order. `e₀ = e_{p₀}`, `e₁ = e_{p₂}`. Fibre 0 is the coordinates `p₀, p₁`; fibre 1 is `p₂, p₃`. Columns of `H₄`:
`h₀ = (1,1,1,1)`, `h₁ = (1,−1,1,−1)`, `h₂ = (1,1,−1,−1)`, `h₃ = (1,−1,−1,1)`. `W = (h₀,h₁,h₂,h₃)/2`,
`W′ = (h₀,h₂,h₁,h₃)/2` as columns at `(p₀,p₁,p₂,p₃)` (PREREG §2). `X` denotes either of `W`, `W′`.

***

## §1. K-a: unitarity

**Column dot products of `H₄`** (real): `h_c·h_c = 4` for each `c`; `h₀·h₁ = 1−1+1−1 = 0`; `h₀·h₂ = 1+1−1−1 = 0`;
`h₀·h₃ = 1−1−1+1 = 0`; `h₁·h₂ = 1−1−1+1 = 0`; `h₁·h₃ = 1+1−1−1 = 0`; `h₂·h₃ = 1−1+1−1 = 0`.

- **`W`.** Real, so `(WᴴW)(c,c′) = ¼ h_c·h_{c′}`: `1` on the diagonal and `0` off it, for all 16 entries (the six below
  the diagonal by symmetry of the real dot product).
- **`W′`.** `(W′ᴴW′)(c,c′) = ¼ h_{σc}·h_{σc′}`, `σ = (0)(1 2)(3)`: diagonal `¼·4 = 1`; off-diagonal entries are `¼` times
  a dot product of two distinct columns of `H₄`, hence `0`. So `W′ᴴW′ = 1`.
- For square matrices `XᴴX = 1` gives `XXᴴ = 1`.
- **`L`** `= block-diag(H₂, H₂)` is real symmetric; `H₂² = ½[[1+1, 1−1],[1−1, 1+1]] = 1`, so `LᴴL = 1`.
- **`K`** `= diag(1, −1, i, 1)`: `KᴴK = diag(1, 1, |i|², 1) = 1`. `LWK` is a product of unitaries.
- **`P`** `= swap(p₁, p₃)` and **`Z`** `= diag(1,1,−1,1)` are a permutation and a diagonal sign matrix; `H₂ ⊕ 1_C`
  (`H₂` on `p₀, p₂`, `1` on `p₁, p₃`) is block-diagonal with unitary blocks.
- **Extension.** `X ⊕ 1` is block-diagonal with unitary blocks.

**Symmetry (used in §4).** `W` is symmetric: its row `r` is `h_r/2` and its column `r` is `h_r/2`. `W′` is symmetric:
its rows are `(1,1,1,1)`, `(1,1,−1,−1)`, `(1,−1,1,−1)`, `(1,−1,−1,1)` (halved), which are its columns `h₀, h₂, h₁, h₃`
(halved) in the same order. So `Wᴴ = W` and `W′ᴴ = W′`.

**K-a: pass.**

## §2. Slice data

**Anchored columns.** `We₀ = ½(1,1,1,1)`, `We₁ = ½(1,1,−1,−1)`; `W′e₀ = ½(1,1,1,1)`, `W′e₁ = ½(1,−1,1,−1)`.

| | `P₀Xe₀` | `P₁Xe₀` | `P₀Xe₁` | `P₁Xe₁` |
|---|---|---|---|---|
| `X = W` | `½(1,1,0,0)` | `½(0,0,1,1)` | `½(1,1,0,0)` | `½(0,0,−1,−1)` |
| `X = W′` | `½(1,1,0,0)` | `½(0,0,1,1)` | `½(1,−1,0,0)` | `½(0,0,1,−1)` |

- **Readback.** Each vector has squared norm `¼+¼ = ½`, so `Γ(W) = Γ(W′) = [[½,½],[½,½]] = J/2`. For `I`,
  `P_wIe_v = δ_{wv}e_v`, so `Γ(I) = 1`.
- **Anchored moduli.** `α(X)(w,j) = |X(p_{2w}, p_{2j})|²`. Every entry of `W` and `W′` is `±½`, so `α(W) = α(W′) = J/4`.
  `α(I) = 1`.
- **Fibre-Gram data** (`FG^{(i)}(j,k) = ⟨P_iXe_j, P_iXe_k⟩`, TSG:115–116), from the table:
  - `W`: fibre 0 `(0,0) = ½`, `(0,1) = ¼+¼ = ½`, `(1,0) = ½`, `(1,1) = ½`; fibre 1 `(0,0) = ½`, `(0,1) = −¼−¼ = −½`,
    `(1,0) = −½`, `(1,1) = ½`.
  - `W′`: fibre 0 `(0,1) = ¼−¼ = 0`, `(1,0) = 0`, diagonal `½`; fibre 1 `(0,1) = ¼−¼ = 0`, `(1,0) = 0`, diagonal `½`.
  - Checks: the two fibres sum to `1` (`sum_fibreGram`, TSG:153); the diagonals are the columns of `Γ` (TSG:127).
- **Gram invariant.** `g(W) = ½`, `g(W′) = 0`. **`|g(W)| = ½ ≠ 0 = |g(W′)|`.**

## §3. K-b: `PPer` membership of the visible family

`AdmissibleDilationAt (Γ t) a₀ (U t)` (DC:134–136) fixes `Γ_t(i,j) = Σ_a |U_t((i,a),(j,a₀))|²`, so the visible family of
`U` is `Γ_t = Γ(I) = 1` at even `t` and `Γ_t = Γ(W) = J/2` at odd `t`; that of `U′` is the same, with `Γ(W′) = J/2`.
`Γ = (1, J/2, 1, J/2, …)` for both lifts.

- **`Γ 0 = 1`** (RC:33): `Γ_0 = Γ(I) = 1`.
- **`IsRowStochastic (Γ t)` for every `t`** (CR:48–49): `1` and `J/2` have entries in `{0, ½, 1}`, all nonnegative; each
  row of `1` is a unit vector and each row of `J/2` is `(½, ½)`, so every row sums to 1. Both matrices are symmetric, so
  `Γ_tᵀ = Γ_t` satisfies the same: the family is in `PPer` in either orientation (B4 l. 496, W9).
- **`PeriodicFamily Γ`** (RC:27–28) with `M = 2`: `t` and `t+2` have the same parity, so `Γ_{t+2} = Γ_t`.

Hence `PPer Γ` holds for the visible family of `U` and of `U′`, and `CoherentLift a₀ Γ U`, `CoherentLift a₀ Γ U′`
(CLG:124) hold.

**Control lifts.** `U^c` has odd slice `LWK` with `Γ(LWK) = J/2` (§5), so the same `Γ`. `U^M` has `Γ_t(U^M) = Γ_t(U)`:
`L` is block-diagonal across fibres, so `P_wLx = L_wP_wx` with `L_w` the unitary block of fibre `w`, and
`‖P_wLx‖ = ‖P_wx‖`. Both lie in `PPer` with the same `Γ`.

**K-b: pass.**

## §4. K-e: the complete-record laws

### 4.1 Relative objects

`T_{t,s} = U_tU_sᴴ` for `s < t`:
- `t, s` both even: `I·I = I`;
- both odd: `XXᴴ = I` (K-a);
- `t` odd, `s` even: `X·I = X`;
- `t` even, `s` odd: `I·Xᴴ = Xᴴ = X` (symmetry, §1).

So every relative object is `I` (same parity) or `X` (different parity), with `X = W` for `U` and `X = W′` for `U′`.
For a read time `t`, the root-to-read evolution is `U_t` = `I` (even) or `X` (odd).

### 4.2 C0

Root `e_j`, one read at `t`. By (r1) the state is `U_te_j`; record `v` has mass `‖P_vU_te_j‖² = Γ_t(v,j)`, with no
failure record.
- Even `t`: `δ_{vj}`, for both lifts.
- Odd `t`: `½` for every `(v, j)`, for both lifts (§2).

The masses of each root sum to 1. **C0: LAWS-EQUAL** for every root, time and record.

### 4.3 C2-ch (Rst-ch)

**Derivation from the procedures** (induction on the number of reads). Root `e_j`, read list `t₁ < … < t_k`.
- First read: the state is `x = U_{t₁}e_j`. Record `v₁` leaves `P_{v₁}xxᴴP_{v₁}`, of trace `Γ_{t₁}(v₁,j)`. It lies in
  fibre `v₁`. Rst-ch replaces the ancilla by `|a₀⟩`: it sends a state `σ` supported in fibre `v₁` to
  `tr(σ)·e_{v₁}e_{v₁}ᴴ`. The branch is `m₁e_{v₁}e_{v₁}ᴴ`, `m₁ = Γ_{t₁}(v₁,j)`.
- Step: from `m·e_ve_vᴴ`, evolution by `T = T_{t_{l+1},t_l}` and read `w` give mass `m·‖P_wTe_v‖² = m·𝒪₂(w,v)`, and the
  reset leaves `m·𝒪₂(w,v)·e_we_wᴴ`.

So `p(v₁,…,v_k | j) = Γ_{t₁}(v₁,j) · Π_{l=1}^{k−1} 𝒪₂(t_{l+1},t_l)(v_{l+1},v_l)`, with no failure record. This agrees
with B4 W0.4 (ll. 95–112).

**Factors on this pair.**
- `Γ_{t₁}`: `1` or `J/2` (§4.2), equal for both lifts.
- `𝒪₂` for `T = I`: `‖P_we_v‖² = δ_{wv}`.
- `𝒪₂` for `T = X`: `‖P_wXe_v‖² = Γ(X)(w,v) = ½` for both lifts (§2).

**Closed form**, for both lifts: the mass is `Π` of one factor per read, where the first factor is `δ_{v₁j}` if `t₁` is
even and `½` if odd, and the factor of read `l+1` is `δ_{v_{l+1}v_l}` if `t_{l+1} − t_l` is even and `½` if odd.

**Explicit states.** Before the reset the branch states differ: from root `j = 1`, read at `t₁ = 1` with record `1`,
`P₁We₁ = ½(0,0,−1,−1)` against `P₁W′e₁ = ½(0,0,1,−1)`; from `e₁` across an odd step with record `0`,
`P₀We₁ = ½(1,1,0,0)` against `P₀W′e₁ = ½(1,−1,0,0)`. Each has mass `½`, and the reset sends both to `½·e_we_wᴴ`.

**Bookkeeping.** `Σ_vΓ_{t₁}(v,j) = 1` and `Σ_w𝒪₂(w,v) = 1` (`δ` or `½+½`), so the masses of each root and read list sum
to 1. **C2-ch: LAWS-EQUAL** for every root, read list and record.

### 4.4 C2-sel (Rst-sel, reading (r2))

**Derivation from the procedures.** `Π = 1_V ⊗ |a₀⟩⟨a₀|`, so `ΠP_v = e_ve_vᴴ`.
- A read with record `v` followed by the test splits an unnormalized pure state `y` into `(v,ok)`, state
  `ΠP_vy = ⟨e_v,y⟩e_v`, mass `|⟨e_v,y⟩|²`, and `(v,⊥)`, state `(1−Π)P_vy`, mass `‖P_vy‖² − |⟨e_v,y⟩|²` (`Π` and
  `1 − Π` are complementary orthogonal projectors). `⊥` is not continued.
- First read, `y = U_{t₁}e_j`: ok mass `α_{t₁}(v₁,j)`, `⊥` mass `Γ_{t₁}(v₁,j) − α_{t₁}(v₁,j)`.
- Later read, from the continued ok state `y = ce_v` (`|c|²` its mass), `T = T_{t_{l+1},t_l}`: ok mass
  `|c|²·|⟨e_w,Te_v⟩|² = |c|²β(w,v)` with state `c⟨e_w,Te_v⟩e_w`; `⊥` mass `|c|²(𝒪₂(w,v) − β(w,v))`.

So an all-ok record has mass `α_{t₁}(v₁,j)·Πβ(v_{l+1},v_l)`, and a record ending in `(v_m,⊥)` has the same product up
to read `m−1` times `(Γ − α)` (if `m = 1`) or `(𝒪₂ − β)` (if `m ≥ 2`) at read `m`. This agrees with B4 W0.5
(ll. 114–127).

**Factors on this pair.** Every entry of `W` and `W′` has modulus `½`.
- `t₁` even: `α = 1`, `Γ − α = 0`. `t₁` odd: `α(v₁,j) = |X(p_{2v₁},p_{2j})|² = ¼`, `Γ − α = ½ − ¼ = ¼`.
- `T = I`: `β = δ`, `𝒪₂ − β = 0`. `T = X`: `β(w,v) = |X(p_{2w},p_{2v})|² = ¼`, `𝒪₂ − β = ½ − ¼ = ¼`.

All factors are equal for the two lifts.

**Closed form**, for both lifts: an all-ok record has mass `Π` of one factor per read, `δ` for an even gap (or even
`t₁`, against `j`) and `¼` for an odd gap (or odd `t₁`); a record ending in `(v_m,⊥)` has the all-ok factors of reads
`1, …, m−1` times `0` (even gap at `m`, or even `t₁` if `m = 1`) or `¼` (odd).

**Explicit step-1 states**, read at `t₁ = 1` (every root and record):

| root, record | `W`: ok; `⊥` | `W′`: ok; `⊥` | masses (both lifts) |
|---|---|---|---|
| `j=0`, `v=0` | `½e_{p₀}`; `½e_{p₁}` | `½e_{p₀}`; `½e_{p₁}` | `¼`; `¼` |
| `j=0`, `v=1` | `½e_{p₂}`; `½e_{p₃}` | `½e_{p₂}`; `½e_{p₃}` | `¼`; `¼` |
| `j=1`, `v=0` | `½e_{p₀}`; `½e_{p₁}` | `½e_{p₀}`; `−½e_{p₁}` | `¼`; `¼` |
| `j=1`, `v=1` | `−½e_{p₂}`; `−½e_{p₃}` | `½e_{p₂}`; `−½e_{p₃}` | `¼`; `¼` |

The same table, with `j` replaced by the incoming anchored label `v` and the factor `|c|²`, gives every odd-gap step,
since `Te_v = Xe_v` there. The states differ by signs; the continued ok state enters later masses only through `|c|²`,
and `⊥` is not continued.

**Bookkeeping.** At each read the ok and `⊥` masses over `v` sum to the incoming mass (`Σ_vΓ = 1` at the first read,
`Σ_w𝒪₂(w,v) = 1` later). Writing `S_m` for the total all-ok mass after `m` reads and `B_m` for the total `⊥` mass at read
`m`: `S_1 + B_1 = 1` and `S_{m+1} + B_{m+1} = S_m`, so `S_k + Σ_m B_m = 1`. **C2-sel: LAWS-EQUAL** for every root, read
list and record, `⊥` records included.

### 4.5 Coverage

Every read list `t₁ < … < t_k` (`k ≥ 1`, any times in `ℕ`, reads at `t = 0` included) is covered: the masses depend only
on the parity of `t₁` and of each gap, and every case is computed in 4.2–4.4.

**K-e: pass** (complete; bookkeeping sums to 1; W0 cross-check agrees).

## §5. K-c: positive gauge control

- **`L` left-fibre** (TSG:78–79): unitary (§1); its entries between rows `p₀,p₁` and columns `p₂,p₃`, and the reverse,
  are 0.
- **`K` weak** (CLG:114–116): unitary; its column at `p₀ = (0,a₀)` is `(1,0,0,0)` and at `p₂ = (1,a₀)` is `(0,0,i,0)`, so
  `c = (c₀,c₁) = (1, i)`.
- **`G(U,U^c)`** by the families `L_t = L`, `K_t = K` at odd `t` and `L_t = K_t = I` at even `t` (TSG:84–87; `I` is
  in both classes).
- **The slice.** `WK` multiplies the columns of `W` by `(1,−1,i,1)`: rows `½(1,−1,i,1)`, `½(1,1,i,−1)`, `½(1,−1,−i,−1)`,
  `½(1,1,−i,1)`. `L` replaces rows `(r₀,r₁)` by `((r₀+r₁)/√2, (r₀−r₁)/√2)` and likewise `(r₂,r₃)`:
  `r₀+r₁ = (1,0,i,0)`, `r₀−r₁ = (0,−1,0,1)`, `r₂+r₃ = (1,0,−i,0)`, `r₂−r₃ = (0,−1,0,−1)`, so

  ```
  LWK = (1/√2) · [ 1   0   i   0 ]
                 [ 0  −1   0   1 ]
                 [ 1   0  −i   0 ]
                 [ 0  −1   0  −1 ]
  ```

- **Fibre-Gram data from the matrix.** `(LWK)e₀ = (1/√2)(1,0,1,0)`, `(LWK)e₁ = (1/√2)(i,0,−i,0)`.
  - Fibre 0: `(0,0) = ½`; `(0,1) = (1/√2)(i/√2) = i/2`; `(1,0) = −i/2`; `(1,1) = ½`.
  - Fibre 1: `(0,0) = ½`; `(0,1) = (1/√2)(−i/√2) = −i/2`; `(1,0) = i/2`; `(1,1) = ½`.
- **Predicted** `conj(c_j)FG^{(i)}(W)(j,k)c_k`: fibre 0 `(0,1) = ½·i = i/2`, `(1,0) = (−i)·½ = −i/2`,
  `(1,1) = (−i)·½·i = ½`, `(0,0) = ½`; fibre 1 `(0,1) = (−½)·i = −i/2`, `(1,0) = (−i)(−½) = i/2`, diagonal `½`. All
  eight entries agree.
- **Hence** `Γ(LWK) = J/2 = Γ(W)`, `|g(LWK)| = ½ = |g(W)|`; the even slices are both `I`. So `Γ_t` and `|g_t|` agree at
  every `t`, and `Λ_C0(U^c) = Λ_C0(U)` (§4.2's derivation applies to any lift: `Λ_C0` is the family `Γ_t(·,j)`).

**K-c: pass.**

## §6. K-d: `|A| = 1` countercontrol

- **(i)** `P₀W′e₀ = ½(1,1,0,0)` and `P₀W′e₁ = ½(1,−1,0,0)` are nonzero and orthogonal, so not collinear:
  `|g(W′)|² = 0 ≠ ¼ = Γ(0,0)Γ(0,1)`. `FG^{(0)}(W′) = ½·1` has rank 2 > 1. Met by `W′`. (`W`'s fibre-Gram data have rank 1.)
- **(ii)** At `|V| = 2`, `|A| = 1`, `P₀Xe_j = X((0,a₀),(j,a₀))·e₀`, so `g = conj(X₀₀)X₀₁` and
  `|g|² = |X₀₀|²|X₀₁|² = Γ(0,0)Γ(0,1)`. Equal `Γ` forces equal `|g|` there, so the pair contradicts nothing proved at
  `|A| = 1`.

**K-d: pass.**

## §7. K-f: sensitivity of the law computation

The per-step rules of §4.3 and §4.4 are applied to the WE pair `(U^E, L·U^E)`, `U^E_0 = I`, `U^E_t = P = swap(p₁,p₃)`
for `t ≥ 1`.
- **Rst-ch, root 0, reads `(0,1)`.**
  - `U^E`: read at 0 from `e_{p₀}` gives record 0 with mass 1; reset to `e_{p₀}`; `T_{1,0} = P`, `Pe_{p₀} = e_{p₀}`. Records
    `(0,0)`, `(0,1)`: masses `(1, 0)`.
  - `L·U^E`: `Le_{p₀} = (e_{p₀}+e_{p₁})/√2` lies in fibre 0: record 0, mass 1; reset to `e_{p₀}`. `T_{1,0} = LPLᴴ = LPL`:
    `Le_{p₀} = (e_{p₀}+e_{p₁})/√2`; `P` gives `(e_{p₀}+e_{p₃})/√2`; `L` gives `½(e_{p₀}+e_{p₁}+e_{p₂}−e_{p₃})`, since
    `Le_{p₃} = (e_{p₂}−e_{p₃})/√2`. Masses `(¼+¼, ¼+¼) = (½, ½)`.
- **Rst-sel, root 0, one read at 0.** `U^E`: `(0,ok) = |⟨e_{p₀},e_{p₀}⟩|² = 1`, `(0,⊥) = 0`. `L·U^E`:
  `(0,ok) = |⟨e_{p₀},(e_{p₀}+e_{p₁})/√2⟩|² = ½`, `(0,⊥) = ‖e_{p₁}/√2‖² = ½`.
- **C0.** `(U, I)` (the identity lift): `Γ_1 = J/2` against `1`, a difference at every root.

These reproduce the frozen expected values (B4 ll. 335–347). Both WE lifts have `Γ ≡ 1` (`P` and `L` keep `e_v` in fibre
`v`), so WE lies in `PPer` with period 1, and it is `G`-related by construction (`L_t ≡ L`, `K_t ≡ I`, TSG:84).

**K-f: pass.** The machinery that reports LAWS-EQUAL in §4 reports a difference where one exists.

## §8. K-g: target-QM procedures

### (g1) T-sep₁

Root `ρ₊ ⊗ |a₀⟩⟨a₀|`, `|+⟩ = (e_{p₀}+e_{p₂})/√2`; evolve by `U_1`; Lüders read `P_v` at `t = 1`.
- `U`: `W|+⟩ = (We₀ + We₁)/√2 = (1/√2)·½[(1,1,1,1)+(1,1,−1,−1)] = (1/√2)(1,1,0,0)`. Branch `v = 0`: `(1/√2)(1,1,0,0)`,
  mass `½+½ = 1`. Branch `v = 1`: `0`, mass `0`.
- `U′`: `W′|+⟩ = (1/√2)·½[(1,1,1,1)+(1,−1,1,−1)] = (1/√2)(1,0,1,0)`. Branch `v = 0`: `(1/√2)(1,0,0,0)`, mass `½`.
  Branch `v = 1`: `(1/√2)(0,0,1,0)`, mass `½`.
- Cross-check through the fibre-Gram data: mass `= tr(ρ₊FG^{(v)}) = ½Σ_{jk}FG^{(v)}(j,k)`; for `W`, `½(½+½+½+½) = 1` and
  `½(½−½−½+½) = 0`; for `W′`, `½(½+0+0+½) = ½` twice.

**T-sep₁ separates: `(1, 0)` against `(½, ½)`.** T-sep₂ and T-sep₃ are not triggered.

### (g2) T-V gauge negative control

- **T-sep₁ on `U^M`.** `U^M_1 = LW`: `LW|+⟩ = L(1/√2)(1,1,0,0) = (1,0,0,0)` (first row `(x₀+x₁)/√2 = 1`, second
  `(x₀−x₁)/√2 = 0`). Masses `(1, 0)`, equal to `U`'s.
- **Every T-V procedure.** Root `ρ̃ = ρ ⊗ |a₀⟩⟨a₀|`; reads at `t₁ < … < t_k` with Kraus operators `E_r ⊗ 1_A` (any
  instruments on `V`, chosen in advance or from earlier records). The unnormalized branch state of a record
  `(r₁,…,r_k)` is `BρB̃ᴴ` with `B = (E_{r_k}⊗1)T_{t_k,t_{k−1}}⋯(E_{r₁}⊗1)U_{t₁}` applied to `ρ̃`. For `U^M`,
  `U^M_{t₁} = LU_{t₁}` and `T^M_{t,s} = LU_tU_sᴴLᴴ = LT_{t,s}Lᴴ`. `L = 1_V ⊗ H₂` acts on `A` only and `E_r ⊗ 1_A` on `V`
  only, so they commute, and `LᴴL = 1` cancels between factors: `B^M = LB`. The branch state is `L(Bρ̃Bᴴ)Lᴴ`, of the
  same trace. So `U` and `U^M` have equal laws for every T-V procedure.

### (g3) T-V sensitivity

WB: `U^B_1 = H₂ ⊕ 1_C` (`H₂` on `e_{p₀}, e_{p₂}`); `H₂|+⟩ = ½[(e₀+e₁)+(e₀−e₁)] = e₀`: masses `(1,0)`. Gauge image
`U^B_1Z`: `Z|+⟩ = (e₀−e₁)/√2`, `H₂` of it is `e₁`: masses `(0,1)`. `Z` is weak with `c = (1,−1)`. This reproduces B4
ll. 286–288.

**K-g: pass.** **T-V: DISTINCT[T-sep₁: `(1,0)` against `(½,½)`].** Since every T-V procedure is a T-V+R procedure,
T-V+R also distinguishes the lifts.

## §9. K-h: re-derivation and definitions; gauge determination

**Definitions re-read** at `f051916a`: TSG:78–79, 84–87, 95–97, 102–103, 115–116, 127–128, 153–154; CLG:114–116, 124,
146; DC:86–87, 134–136; RC:27–28, 32–33; CR:48–49, 190–192; SC ll. 24–25, 112–124; B4 ll. 40–44, 57–62, 229–230. Each
reads as stated in PREREG §1. No definition reads differently.

**Lemma R (a ⇒ b)** (`|V| = 2`, unitary slices `X, X′`). Suppose `X′ = LXK` with `LeftFibreGroup L` and
`WeakAnchorStabilizer a₀ K` with coefficients `c`. `gramPhaseEquiv_of_twoSided` (TSG:263–265) gives
`GramPhaseEquiv (FG(X)) (FG(X′))`; by its definition (TSG:102–103) there are `c′` with `|c′_j| = 1` and
`FG(X′)^{(i)}(j,k) = conj(c′_j)FG(X)^{(i)}(j,k)c′_k`.
- At `(i,j,j)`: `FG(X′)^{(i)}(j,j) = |c′_j|²FG(X)^{(i)}(j,j)`, which by `fibreGram_diag` (TSG:127) is `Γ(X′) = Γ(X)`.
- At `(0,0,1)`: `g(X′) = conj(c′₀)g(X)c′₁`, so `|g(X′)| = |g(X)|`.

**Gauge determination (branch P2-neq).** `|g(W)| = ½ ≠ 0 = |g(W′)|` (§2). If `G(U,U′)` held, TSG:84–87 at `t = 1` would
give `W′ = L₁WK₁` with `L₁` left-fibre and `K₁` weak, and Lemma R (a ⇒ b) would give `|g(W′)| = |g(W)|`. Contradiction:
**¬G(U,U′)**. Lemma R (b ⇒ a) is not needed and is not written.

**Premises.** No content off `main` and no derived result of B4 or RES is a premise: the laws (§4), the slice data (§2),
the witnesses WE and WB (§§7–8) and Lemma R are derived here.

**K-h: pass.**

## §10. K-i: extension to `|A| = m ≥ 3`

Slices `I`, `X ⊕ 1`. The anchored columns of `X ⊕ 1` have zero coordinates on the added vectors `(v,a)`, `a ∉ {a₀,a₁}`,
and `X ⊕ 1` is symmetric. So: relative objects are `I` or `X ⊕ 1`; from `e_v`, `(X⊕1)e_v = Xe_v`; every `P_v`- and
`Π`-projection, hence every mass of §4, is unchanged; the added terms of every fibre-Gram sum are `0`, so `Γ`, `α`, `g`
and §3 are unchanged; `|+⟩ ∈ 𝒜`, so T-sep₁'s masses are unchanged; `X ⊕ 1` is unitary. **K-i: pass**; the scope is
`|A| ≥ 2`.

## §11. Verdict, from the decision rule

PREREG §6: "**COUNTEREXAMPLE** iff no VOID condition holds and (P1) and (P2) hold."

| Condition | Result | Where |
|---|---|---|
| K-a unitarity | pass | §1 |
| K-b `PPer`, both orientations | pass | §3 |
| K-c positive gauge control | pass | §5 |
| K-d `\|A\| = 1` countercontrol | pass | §6 |
| K-e complete-record laws (coverage, bookkeeping, W0 cross-check) | pass | §4 |
| K-f sensitivity (WE; C0) | pass | §7 |
| K-g T-V (g1)–(g3) | pass | §8 |
| K-h re-derivation; definitions match | pass | §9 |
| exact arithmetic | every entry an integer, a multiple of `½`, `¼` or `1/√2`, or a Gaussian rational | throughout |
| (P1) `Λ_C0(U) = Λ_C0(U′)` | holds | §4.2 |
| (P2) ¬G, branch P2-neq | holds, `½ ≠ 0` | §9 |
| K-i extension (scope) | pass: `\|A\| ≥ 2` | §10 |
| C2-ch | LAWS-EQUAL | §4.3 |
| C2-sel | LAWS-EQUAL | §4.4 |
| T-V | DISTINCT[T-sep₁] | §8 |

**Verdict: COUNTEREXAMPLE[C0, C2-ch, C2-sel; `PPer`; `|V| = 2`, `|A| ≥ 2`; alternating lifts `U = (I,W,I,W,…)`,
`U′ = (I,W′,I,W′,…)`; equal complete-record laws; not two-sided related; T-V: DISTINCT[T-sep₁: `(1,0)` against
`(½,½)`]].**

For each `C ∈ {C0, C2-ch, C2-sel}`, `Q[C]` (O⇒G) is false at `|V| = 2`, `|A| ≥ 2` in the class `PPer`.

## §12. Reports (PREREG §5) and scoped conclusion

**Reports.**
- **C0:** LAWS-EQUAL. **Gauge:** `|g(W)| = ½`, `|g(W′)| = 0`; ¬G. **T-V:** DISTINCT by T-sep₁; T-V+R inherits it.
- **What C2-ch and C2-sel observe.** On this pair, their laws are functions of `Γ_{t₁}`, `α_{t₁}` and, at each later
  read, `𝒪₂` and `β` of `T ∈ {I, X}`. Every one of these is a sum or a single value of the squared moduli of entries of
  `X` in an anchored column (`α`, `β`: the entry at an anchored row; `Γ`, `𝒪₂`: summed over a fibre). After each read,
  Rst-ch replaces the post-read state by `e_v`, and Rst-sel keeps only its `e_v` component and does not continue `⊥`. So
  no relative phase between the components of `Xe_j` within a fibre ever enters a mass, and neither do the off-diagonal
  fibre-Gram entries (`g`). Those are what distinguish the lifts (§2) and what T-sep₁ reads (§8 (g1) cross-check). All
  entries of `W` and `W′` have modulus `½`, so every observed datum coincides.
- **Visible family:** `Γ = (1, J/2, 1, J/2, …)`, in `PPer` in either orientation. **Scope:** `|A| ≥ 2`.

**Established here** (paper derivation in exact arithmetic; independent review pending):
- O⇒G fails for C0, C2-ch and C2-sel at `|V| = 2`, `|A| ≥ 2`, for lifts whose visible family lies in `PPer`, witnessed by
  the alternating pair above. The same pair is distinguished by a one-read T-V procedure with a coherent preparation.
- With G⇒O for C0 (kernel: `left_preserves_admissible` TSG:217, `weak_preserves_admissible` CLG:273, which make every
  `L_tU_tK_t` an admissible dilation of the same `Γ_t`; `Λ_C0` is the family `Γ_t(·,j)`), C0 is strictly coarser than
  `G` in `PPer` at `|V| = 2`, `|A| ≥ 2`.
- For C2-ch and C2-sel, G⇒O fails in `PPer` (WE, re-derived in §7), and O⇒G fails in `PPer` (this pair): they are
  incomparable with `G` in `PPer` at `|V| = 2`, `|A| ≥ 2`.
- Conditional reading for OI lifts: CONDITIONAL[the candidate tuple, ∀U, fixed `a₀`, (r1)], with (r2) for C2-sel
  (B4 ll. 548–559).

**Not established** (as the ruling states):
- **Physical availability.** P-conf, Acc₂, Rd, H-comp, Rst-ch, Rst-sel and the coherent preparation `ρ₊` of T-sep₁ remain
  SOURCING-GAPs (B4 ll. 562–572; #1143 spec §4.4 S-0–S-8). The T-V separation is a statement about mathematical
  procedures, not about procedures available to an OI observer.
- **Native OI realizability.** `PPer` membership of the visible family is not nativeness. No native class of BSEL-2
  dilation lifts and no realization→lift correspondence (spec S-0) is defined on `main`. `PPer` equals finite rooted
  realizability of the visible family (RCAT:192–194), which says nothing about which dilation lift a realization
  implements.
- Any physical OI–QM difference or equivalence; C-pers (M-2); T-full.
- A theorem promotion, Lean statement or manuscript claim.

**Hidden-assumption watch (§A.31).** The favourable branch (C2 laws also equal) was pressure-tested by K-f, which shows
the same per-step rules detect the WE difference, and by the explicit state tables, which show the branch states do
differ between the lifts.
- **ELABORATING:** the separation of C2's observed data from `G` here rests on two features: the resets project every
  continued branch back onto an anchored line, and every entry of `W`, `W′` has modulus `½`. Under the alternating
  placement, the formulas of §4.3–§4.4 with `T ∈ {I, X, Xᴴ}` show that any two unitaries whose
  anchored columns and anchored rows have equal entrywise moduli give equal C0, C2-ch and C2-sel laws. Recorded as an
  assumption-watch marker for M-2: a reset-free procedure (C-pers) is the natural place for phase information to survive.
- **CONFIRMING:** the separation again sits in the rank of the fibre-Gram data (`W` rank 1, `W′` rank 2, §6), as in RES.

## §13. Proposed changes (for owner approval; not applied)

**B4′ matrix** (`B4PRIME.md`; nothing there is changed by this record):

| Row | Proposed O⇒G cell | Proposed support |
|---|---|---|
| l. 517 (C0, `\|V\|` = 2, `\|A\|` ≥ 2, `PPer`) | disproved: COUNTEREXAMPLE[C0, `\|V\|`=2, `\|A\|`≥2, no reset, same Γ, `PPer`] | this record (alternating `W`/`W′`) |
| l. 523 (C2-ch, same scope, `PPer`) | disproved: COUNTEREXAMPLE[C2-ch, `\|V\|`=2, `\|A\|`≥2, Rst-ch, same Γ, `PPer`] | this record |
| l. 526 (C2-sel, same scope, `PPer`) | disproved: COUNTEREXAMPLE[C2-sel, `\|V\|`=2, `\|A\|`≥2, Rst-sel, same Γ and α, `PPer`] | this record |

Each row's "Does NOT establish" would read "a native separation; physical availability". If approved, the passages of B4
that state these cells as not addressed (l. 281, l. 364, the Equivalence summary, §9's "Does NOT establish" and
"Proposals") would be corrected in place in a separately authorized change. `SCOPE.md` is a frozen copy and is not to be
edited.

**#1143 planning record:** the spec's §3 rows "C0, `≥2`, `PPer`, O⇒G open" and "C2-ch, C2-sel, `≥2`, `PPer`, O⇒G open",
and F4's "C2 laws open", would be updated to cite this record once it is independently reviewed. For the spec's §4.3:
C0, C2-ch and C2-sel all fail to separate this instance, so no C2 class enters the "smallest test" comparison; the M-2
comparison (C-pers against `C*`) is unaffected.

## §14. Premise ledger: §A.42 item 8 trace

| Reference | Where cited | Claim it is attached to | Classification |
|---|---|---|---|
| #1031 c.6665461411; #1143 c.6665466217 | PREREG §0; header | Authorization | Provenance: owner designation quoted with author and time (§A.42 item 7). No mathematical claim uses it. |
| #1143 c.6665278924 (spec), c.6665288579 (review) | PREREG §1, §3, §4, §7, §9; §12, §13 | Origin of the candidate (F4) and of the T-V definition; control numbering | Provenance. T-V and T-V+R are restated in full in PREREG §1, and every claim uses the restated definition. Every value F4 anticipates is derived here. |
| PREREG commit `7f3e8ffa` and this branch's commit order | header; PREREG §8 | Freeze before check | Support off `main` until landing. The order is recorded by the host: pull request #1151 was opened with `7f3e8ffa` as its only commit, before this file existed. The cited ids stay reachable from `main` only if the branch lands by a true merge commit. The mathematical verdict depends only on `main` and the text of both files, and can be re-checked from them. |
| Reviews of B4 and RES (#1033, #1139 comments) | not cited as support | — | Not used. B4, SC, QP and RES supply definitions, notation and the frozen matrices only. |
| B4 W0 (ll. 71–127), WB (ll. 285–288), WE (ll. 332–347) | §§4, 7, 8 | Cross-check; expected control values | Support on `main` as definitions and expected values only; every value is re-derived here (§A.46 item 7). |

**Checks run at this commit:** `tools/artifact_placement_check.py` and `tools/duplicate_check.py`.

## §15. Review and next steps

- Independent mathematical review is required by the ruling and is pending. It should check the pair against PREREG §2
  and QP ll. 107–125, the hand algebra of §§1–10, the decision-rule evaluation (§11) and the scope (§12).
- Merge is not authorized. The proposed changes (§13) await the owner.
- Per the ruling, M-2's evaluation of C-pers on this instance may start only after this instance and outcome are
  independently checked.
