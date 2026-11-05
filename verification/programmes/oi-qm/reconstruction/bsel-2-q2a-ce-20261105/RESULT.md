# BSEL-2 Q2A: verification of the candidate counterexample pair (result)

**Status: WIP / UNVERIFIED. Independent review pending; merge not authorized.** Paper-only. Writer: `writer-bsel2-ce`.
**Preregistration:** `PREREG.md` in this directory, frozen at commit `6fad52e1767c03a13e84c6c5ba8a4e119984bda4` and pushed
before any computation below. This file is added by the next commit and changes no other file. The pair, the controls
and the decision rule are applied as frozen; nothing was adjusted.
**Authorization:** owner ruling #1033 c.6662765230 (amaybaum, Claude Code session chat, 2026-11-05, shortly before
16:03Z), quoted verbatim in PREREG §0.
**Base:** `origin/main` `a8ab8dae3e9af7376c9233f4d474d7ccec1ecdb2`. Citations as in PREREG §1 (TSG, CLG, DC, CF, RC, B4,
SC).
**Method:** hand algebra in exact arithmetic. No script, CAS, numerical evaluation or search was used. Every value
below is written out.

**Notation.** Basis order `p₀ = (0,a₀)`, `p₁ = (0,a₁)`, `p₂ = (1,a₀)`, `p₃ = (1,a₁)`; vectors are written as coordinate
tuples in this order. `e₀ = e_{p₀}`, `e₁ = e_{p₂}` (PREREG §2). Columns of `H₄`: `h₀ = (1,1,1,1)`, `h₁ = (1,−1,1,−1)`,
`h₂ = (1,1,−1,−1)`, `h₃ = (1,−1,−1,1)`. `W = (h₀,h₁,h₂,h₃)/2` and `W′ = (h₀,h₂,h₁,h₃)/2` as columns at
`(p₀,p₁,p₂,p₃)`. The anchored columns are

- `We₀ = ½(1,1,1,1)`, `We₁ = We_{p₂} = ½(1,1,−1,−1)`;
- `W′e₀ = ½(1,1,1,1)`, `W′e₁ = W′e_{p₂} = ½(1,−1,1,−1)`.

***

## §1. K-a: unitarity

**Dot products of the columns of `H₄`** (all real):
- `h₀·h₀ = h₁·h₁ = h₂·h₂ = h₃·h₃ = 1+1+1+1 = 4`;
- `h₀·h₁ = 1−1+1−1 = 0`; `h₀·h₂ = 1+1−1−1 = 0`; `h₀·h₃ = 1−1−1+1 = 0`;
- `h₁·h₂ = (1)(1)+(−1)(1)+(1)(−1)+(−1)(−1) = 1−1−1+1 = 0`;
- `h₁·h₃ = (1)(1)+(−1)(−1)+(1)(−1)+(−1)(1) = 1+1−1−1 = 0`;
- `h₂·h₃ = (1)(1)+(1)(−1)+(−1)(−1)+(−1)(1) = 1−1+1−1 = 0`.

**`W`.** `W` is real, so `(WᴴW)(c,c′) = ¼ h_c·h_{c′}`. The ten entries with `c ≤ c′` are `¼·4 = 1` on the diagonal
and `¼·0 = 0` off it; the other six follow by symmetry of the real dot product. So `WᴴW = 1`.

**`W′`.** `(W′ᴴW′)(c,c′) = ¼ h_{σc}·h_{σc′}` with `σ = (0)(1 2)(3)`:
`(0,0) = ¼h₀·h₀ = 1`, `(0,1) = ¼h₀·h₂ = 0`, `(0,2) = ¼h₀·h₁ = 0`, `(0,3) = ¼h₀·h₃ = 0`, `(1,1) = ¼h₂·h₂ = 1`,
`(1,2) = ¼h₂·h₁ = 0`, `(1,3) = ¼h₂·h₃ = 0`, `(2,2) = ¼h₁·h₁ = 1`, `(2,3) = ¼h₁·h₃ = 0`, `(3,3) = ¼h₃·h₃ = 1`; the
rest by symmetry. So `W′ᴴW′ = 1`.

For square matrices `XᴴX = 1` gives `XXᴴ = 1`, so both are unitary.

**`L` and `K`.** `L = block-diag(H₂, H₂)` is real symmetric, so `LᴴL = L² = block-diag(H₂², H₂²)`, and
`H₂² = ½[[1+1, 1−1],[1−1, 1+1]] = 1`. `K = diag(1, −1, i, 1)` gives `KᴴK = diag(|1|², |−1|², |i|², |1|²) = 1`.

**K-a: pass.**

## §2. The data of the slices

**Readback `Γ`** (`Γ(w,v) = ‖P_w X e_v‖²`; fibre 0 is coordinates `p₀, p₁`, fibre 1 is `p₂, p₃`):

| | `P₀Xe₀` | `P₁Xe₀` | `P₀Xe₁` | `P₁Xe₁` |
|---|---|---|---|---|
| `X = W` | `½(1,1,0,0)` | `½(0,0,1,1)` | `½(1,1,0,0)` | `½(0,0,−1,−1)` |
| `X = W′` | `½(1,1,0,0)` | `½(0,0,1,1)` | `½(1,−1,0,0)` | `½(0,0,1,−1)` |

Each vector has squared norm `¼ + ¼ = ½`. So `Γ(W) = Γ(W′) = [[½, ½],[½, ½]] = J/2`.

**Anchored moduli `α`** (`α(w,j) = |⟨e_w, Xe_j⟩|² = |X(p_{2w}, p_{2j})|²`): the four entries `X(p₀,p₀)`, `X(p₀,p₂)`,
`X(p₂,p₀)`, `X(p₂,p₂)` are `½, ½, ½, −½` for `W` and `½, ½, ½, ½` for `W′`. Every modulus squared is `¼`, so
`α(W) = α(W′) = J/4`.

**Fibre-Gram data** (`FG^{(i)}(j,k) = Σ_a conj(X((i,a),(j,a₀)))·X((i,a),(k,a₀))`, TSG:115–116), from the table above:
- `W`, fibre 0: `(0,0) = ¼+¼ = ½`; `(0,1) = (½)(½)+(½)(½) = ½`; `(1,0) = ½`; `(1,1) = ½`.
  `FG^{(0)}(W) = [[½, ½],[½, ½]]`.
- `W`, fibre 1: `(0,0) = ½`; `(0,1) = (½)(−½)+(½)(−½) = −½`; `(1,0) = −½`; `(1,1) = ½`.
  `FG^{(1)}(W) = [[½, −½],[−½, ½]]`.
- `W′`, fibre 0: `(0,0) = ½`; `(0,1) = (½)(½)+(½)(−½) = 0`; `(1,0) = 0`; `(1,1) = ½`. `FG^{(0)}(W′) = [[½, 0],[0, ½]]`.
- `W′`, fibre 1: `(0,0) = ½`; `(0,1) = (½)(½)+(½)(−½) = 0`; `(1,0) = 0`; `(1,1) = ½`. `FG^{(1)}(W′) = [[½, 0],[0, ½]]`.

Checks: each pair of fibres sums to `1` (`sum_fibreGram`, TSG:153), and each diagonal equals the corresponding
column of `Γ` (`fibreGram_diag`, TSG:127).

**Gram invariant.** `g(W) = FG^{(0)}(W)(0,1) = ½` and `g(W′) = FG^{(0)}(W′)(0,1) = 0`. So
**`|g(W)| = ½ ≠ 0 = |g(W′)|`.**

**Class.** `Γ_0 = Γ(W) = J/2 ≠ 1` for both constant lifts, so neither is in `PPer` (RC:32 requires `Γ 0 = 1`, which
does not depend on orientation). `J/2` is doubly stochastic and the lifts are constant, so `Γ_0 = 1` is the only `PPer`
clause that fails.

## §3. K-b: the complete-record laws

The masses are computed from the procedures (SC ll. 112–119; (r1), (r2)) for a general constant unitary lift
`U_t ≡ X`, and then evaluated for `X = W` and `X = W′`. Each step uses one fact: `T_{t,s} = XXᴴ = 1` (K-a). So between
reads the state does not change, and the times `t₁ < … < t_k` do not enter any mass.

### 3.1 C0
Root `|j,a₀⟩ = e_j`, one read at `t`. By (r1) the state is `Xe_j`; record `v` has mass `‖P_vXe_j‖² = Γ(X)(v,j)`. There
is no failure record. For both lifts every record `(t; j; v)` has mass `½` (§2 table), and the two masses of each root
sum to 1. **Equal.**

### 3.2 C2-ch (Rst-ch)
**Claim** (induction on `k`). For root `j` and read list `t₁ < … < t_k`, the record `(v₁,…,v_k)` has mass
`Γ(X)(v₁,j)·Π_{m=1}^{k−1} δ_{v_{m+1}v_m}`, and each branch of positive mass leaves the state `m·e_{v_k}e_{v_k}ᴴ`, where `m`
is its mass.
- **`k = 1`.** By H-comp the state at `t₁` is `x = Xe_j`. The Lüders read with record `v₁` leaves `P_{v₁}x xᴴP_{v₁}`,
  of trace `‖P_{v₁}x‖² = Γ(X)(v₁,j)`. Rst-ch replaces the ancilla by `|a₀⟩`. The state lies in fibre `v₁`, so this gives
  `Γ(X)(v₁,j)·|v₁,a₀⟩⟨v₁,a₀| = m₁e_{v₁}e_{v₁}ᴴ`.
- **Step.** From `m·e_ve_vᴴ`, evolution by `T = 1` changes nothing. The read with record `w` leaves
  `m·P_we_ve_vᴴP_w = m·δ_{wv}e_ve_vᴴ`, of mass `m·δ_{wv}`. The reset leaves it unchanged, since `e_v` already carries `a₀`.

**Evaluation.** For both lifts `Γ = J/2`, so the record `(v₁,…,v_k)` from either root has mass `½` if
`v₁ = v₂ = … = v_k` and `0` otherwise. There is no failure record. The masses of each root and read list sum to
`½ + ½ = 1`.

Explicit first-read states, before the reset: from root `j = 1` with record `1`, `P₁We₁ = −½(e_{p₂}+e_{p₃})` and
`P₁W′e₁ = ½(e_{p₂}−e_{p₃})`. The states differ, but both have mass `½` and the reset sends both to `½·e₁e₁ᴴ`. The other
first-read states (table of §2) behave the same way. **Equal**, for every root, every read list and every record.

### 3.3 C2-sel (Rst-sel, reading (r2))
`Π := 1_V ⊗ |a₀⟩⟨a₀|`. After each read with record `v`, the test splits `P_vy` into `(v,ok)`, with state `ΠP_vy` and mass
`‖ΠP_vy‖² = |⟨e_v,y⟩|²`, and `(v,⊥)`, with state `(1−Π)P_vy` and mass `‖P_vy‖² − |⟨e_v,y⟩|²`. A `⊥` branch is not
continued.

**Claim** (induction on `k`). For root `j` and read list `t₁ < … < t_k`:
- (a) the all-ok record `((v₁,ok),…,(v_k,ok))` has mass `α(X)(v₁,j)·Π_{m<k} δ_{v_{m+1}v_m}`, and leaves the pure state
  `⟨e_{v₁},Xe_j⟩e_{v₁}` when all `v_m` are equal, and `0` otherwise;
- (b) the record `((v₁,⊥))` has mass `Γ(X)(v₁,j) − α(X)(v₁,j)`;
- (c) a record ending in `(v_m,⊥)` with `m ≥ 2` has mass `0`.

*Proof.* Step 1 from `x = Xe_j`: `ΠP_{v₁}x = ⟨e_{v₁},x⟩e_{v₁}`, of mass `α(X)(v₁,j)`, and `⊥` has mass
`Γ(X)(v₁,j) − α(X)(v₁,j)`. Step `m ≥ 2` from `y = ce_v`: `T = 1`, then `P_wy = δ_{wv}ce_v`. Since `e_v` lies in the range
of `Π`, the ok part is `δ_{wv}ce_v`, of mass `|c|²δ_{wv}`, and the `⊥` part is `(1−Π)δ_{wv}ce_v = 0`.

**Explicit step-1 states and masses.** These cover every root and record, for both lifts.

| root, record | `W`: ok state; mass | `W`: `⊥` state; mass | `W′`: ok state; mass | `W′`: `⊥` state; mass |
|---|---|---|---|---|
| `j=0`, `v=0` | `½e_{p₀}`; `¼` | `½e_{p₁}`; `¼` | `½e_{p₀}`; `¼` | `½e_{p₁}`; `¼` |
| `j=0`, `v=1` | `½e_{p₂}`; `¼` | `½e_{p₃}`; `¼` | `½e_{p₂}`; `¼` | `½e_{p₃}`; `¼` |
| `j=1`, `v=0` | `½e_{p₀}`; `¼` | `½e_{p₁}`; `¼` | `½e_{p₀}`; `¼` | `−½e_{p₁}`; `¼` |
| `j=1`, `v=1` | `−½e_{p₂}`; `¼` | `−½e_{p₃}`; `¼` | `½e_{p₂}`; `¼` | `−½e_{p₃}`; `¼` |

**Evaluation.** For both lifts, from either root and for any read list of length `k`:
- the all-ok record has mass `¼` if all `v_m` are equal, and `0` otherwise;
- `((v₁,⊥))` has mass `¼` for each `v₁`;
- every record ending in `⊥` at a later step has mass `0`.

The masses of each root and read list sum to `¼+¼` (all-ok) `+ ¼+¼` (`⊥` at step 1) `= 1`. For root `j = 1`, the
`(0,⊥)` and `(1,ok)` states differ in sign between the lifts. The masses are equal, `⊥` is not continued, and a
continued ok state enters later masses only through `|c|²`. **Equal**, for every
root, every read list and every record, the `⊥` records included.

### 3.4 Cross-check with W0 (B4 ll. 70–125)
- W0.1 gives `Γ_t(v,j)`, as in 3.1.
- W0.4 gives `Γ·Π𝒪₂`. Here `𝒪₂(t,s)(w,v) = ‖P_w·1·e_v‖² = δ_{wv}`, as in 3.2.
- W0.5 gives first-step factors `α` and `Γ − α`. The later factors are `β = |⟨e_w,e_v⟩|² = δ_{wv}` and
  `𝒪₂ − β = 0`, as in 3.3.

No disagreement.

### 3.5 Extension to `|A| = m ≥ 3`
For `X ⊕ 1` (PREREG §2), the anchored columns `Xe_j` have zero coordinates on the added vectors `(v,a)`,
`a ∉ {a₀,a₁}`. So:
- every `P_v`- and `Π`-projection above is unchanged;
- `T = (X⊕1)(X⊕1)ᴴ = 1`;
- every mass in 3.1–3.3 is unchanged;
- the added terms of every fibre-Gram sum are `conj(0)·0 = 0`, so `Γ`, `α` and `g` are unchanged;
- `X ⊕ 1` is unitary because it is block-diagonal with unitary blocks.

**K-b: pass.** `Λ_C0`, `Λ_C2-ch` and `Λ_C2-sel` agree entrywise for every root, read list and record, the `⊥` masses
included, at `|A| = 2` and at every `|A| ≥ 3`. `Γ` and `α` agree entrywise.

## §4. K-c: positive gauge control

- **`L ∈ 𝒢_L`** (TSG:78–79): unitary by §1. Its entries between different fibres, the rows `p₀,p₁` against the columns
  `p₂,p₃` and the reverse, are all 0.
- **`K` weak** (CLG:114–116): unitary by §1. Its column at `(0,a₀) = p₀` is `(1,0,0,0)` and its column at
  `(1,a₀) = p₂` is `(0,0,i,0)`. So `K p (j,a₀) = c_j·[p = (j,a₀)]` with `c = (c₀, c₁) = (1, i)`.
- **The control slice.** `WK` multiplies the columns of `W` by `(1, −1, i, 1)`:

  ```
  WK = ½ · [ 1  −1   i   1 ]
           [ 1   1   i  −1 ]
           [ 1  −1  −i  −1 ]
           [ 1   1  −i   1 ]
  ```

  `L` replaces rows `(r₀, r₁)` by `((r₀+r₁)/√2, (r₀−r₁)/√2)`, and likewise `(r₂, r₃)`. With
  `r₀+r₁ = (2,0,2i,0)`, `r₀−r₁ = (0,−2,0,2)`, `r₂+r₃ = (2,0,−2i,0)` and `r₂−r₃ = (0,−2,0,−2)`:

  ```
  LWK = (1/√2) · [ 1   0   i   0 ]
                 [ 0  −1   0   1 ]
                 [ 1   0  −i   0 ]
                 [ 0  −1   0  −1 ]
  ```

- **Related by construction.** The constant families `L_t ≡ L` and `K_t ≡ K` witness `TwoSidedRelated a₀ (W) (LWK)`
  (TSG:84–87).
- **Fibre-Gram data of `LWK`, computed from the matrix.** The anchored columns are `(LWK)e₀ = (1/√2)(1,0,1,0)` and
  `(LWK)e₁ = (1/√2)(i,0,−i,0)`.
  - Fibre 0: `(0,0) = ½`; `(0,1) = conj(1/√2)(i/√2) + 0 = i/2`; `(1,0) = −i/2`; `(1,1) = |i|²/2 = ½`.
  - Fibre 1: `(0,0) = ½`; `(0,1) = conj(1/√2)(−i/√2) + 0 = −i/2`; `(1,0) = i/2`; `(1,1) = ½`.
- **Predicted, `conj(c_j)·FG^{(i)}(W)(j,k)·c_k` with `c = (1, i)`.**
  - Fibre 0: `(0,0) = ½`; `(0,1) = 1·½·i = i/2`; `(1,0) = (−i)·½·1 = −i/2`; `(1,1) = (−i)·½·i = ½`.
  - Fibre 1: `(0,0) = ½`; `(0,1) = 1·(−½)·i = −i/2`; `(1,0) = (−i)·(−½)·1 = i/2`; `(1,1) = ½`.

  All eight entries agree with the computed ones.
- **Hence** `Γ(LWK) = J/2 = Γ(W)` and `|g(LWK)| = |i/2| = ½ = |g(W)|`.

**K-c: pass.** On a pair related by construction, the hand Gram computation reports the phase law of TSG:263 and no
difference in `(Γ, |g|)`.

## §5. K-d: ancilla countercontrol

- **(i)** `P₀W′e₀ = ½(1,1,0,0)` and `P₀W′e₁ = ½(1,−1,0,0)` are nonzero and orthogonal, so they are not collinear:
  `|g(W′)|² = 0 ≠ ¼ = Γ(0,0)Γ(0,1)`. `FG^{(0)}(W′) = ½·1` has rank 2, which exceeds the `|A| = 1` bound
  `rank ≤ |A|` (`fibreGram_rank_le`, TSG:146). The criterion is met by `W′`.

  Record of the other member: `P₀We₀ = P₀We₁ = ½(1,1,0,0)` are collinear, and `FG^{(0)}(W)`, `FG^{(1)}(W)` have rank 1.
  The criterion fixed in PREREG §3 is "at least one member", so this does not affect the outcome. It locates the
  separation: rank-1 Gram data (`W`, the same data as `H₂` at `|A| = 1`) against rank-2 Gram data (`W′`), which needs
  `|A| ≥ 2`.
- **(ii) The `|A| = 1` statement, re-derived.** At `|A| = 1`, `P₀Xe_j = X((0,a₀),(j,a₀))·e₀`, so
  `g = conj(X_{00})X_{01}` and `|g|² = |X_{00}|²|X_{01}|² = Γ(0,0)Γ(0,1)`. Equal `Γ` therefore forces equal `|g|`, and
  Lemma R (b ⇒ a) (§6) relates the slices. This is B4 §3.1's argument (ll. 240–246). No pair with equal `Γ` and unequal
  `|g|` exists at `|A| = 1`, so the present pair contradicts nothing proved there.

**K-d: pass.**

## §6. K-e: the lemmas, re-derived from `main`

Only kernel lines on `main` and the definitions of PREREG §1 are used. `Q2A.md` (off `main`) is not used.

**Definitions re-read.**
- `TwoSidedRelated` (TSG:84–87), `LeftFibreGroup` (TSG:78–79), `WeakAnchorStabilizer` (CLG:114–116), `FibreGram`
  (TSG:95–97, with `fibreGram_apply` TSG:115–116), `GramPhaseEquiv` (TSG:102–103), `Γ` (B4 l. 39; DC:134–136) and `α`
  (B4 l. 43) read as in PREREG §1.
- The assessment's reading is the same. It uses `Γ = J/2`, `α ≡ ¼` and `g = ⟨P₀We₀, P₀We₁⟩`, which is
  `FibreGram a₀ W 0 0 1`, conjugate-linear in the first slot, as TSG:116 writes it. It derives non-relatedness from
  TSG:263 and TSG:839 (`mp`).
- No definition reads differently.

**Lemma R** (`|V| = 2`, any `|A|`; unitary slices `W, W′`). Each direction is proved separately.
- **(GPE ⇒ b).** Suppose `GramPhaseEquiv (FG(W)) (FG(W′))` with phases `c`, `|c_j| = 1` (TSG:102–103).
  - At `i, j = k`: `FG(W′)^{(i)}(j,j) = |c_j|²FG(W)^{(i)}(j,j)`. By `fibreGram_diag` (TSG:127) this says
    `Γ(W′)(i,j) = Γ(W)(i,j)`.
  - At `(i,j,k) = (0,0,1)`: `g(W′) = conj(c₀)g(W)c₁`, so `|g(W′)| = |g(W)|`.
- **(a ⇒ b).** If `W′ = LWK` with `L ∈ 𝒢_L` and `K` weak, `gramPhaseEquiv_of_twoSided` (TSG:263–265) gives GPE, and
  (GPE ⇒ b) applies.
  - Hand check of the same step: `fibreGram_left_mul` (TSG:207) removes `L`. `WKe_{(j,a₀)} = c_jWe_{(j,a₀)}` (CLG:116)
    gives `FG(WK)^{(i)}(j,k) = conj(c_j)FG(W)^{(i)}(j,k)c_k`. K-c confirms this law entrywise on one instance.
  - **This is the only direction the verdict uses.**
- **(b ⇒ a).** Suppose `Γ(W) = Γ(W′)` and `|g(W)| = |g(W′)|`.
  - Each `FG^{(i)}` is Hermitian, so `FG^{(0)}(1,0) = conj(g)`.
  - `sum_fibreGram` (TSG:153) gives `FG^{(1)} = 1 − FG^{(0)}`, so `FG^{(1)}(0,1) = −g` and `FG^{(1)}(1,0) = −conj(g)`.
    The diagonals are `Γ`.
  - Put `c₀ = 1`. Put `c₁ = g(W′)/g(W)` if `g(W) ≠ 0`, which is a phase by (b); otherwise `g(W′) = 0` and `c₁ = 1`.
  - The eight entries: the diagonals give `conj(c_j)Γc_j = Γ`. `(0,0,1)` gives `g·c₁ = g′`. `(0,1,0)` gives
    `conj(c₁)conj(g) = conj(g′)`. `(1,0,1)` gives `−g·c₁ = −g′`. `(1,1,0)` gives `−conj(g′)`.
  - So GPE holds, and `twoSided_slice_iff` (TSG:826–830, `mpr`), with both slices unitary, gives (a).
  - This direction is not used by the verdict. It shows that `(Γ, |g|)` is a complete invariant of the slice relation
    at `|V| = 2`, so `|g|` is the right invariant to test.

**Lemma C** (constant lifts `U_t ≡ X`, `U′_t ≡ X′`, both unitary).
- **(i) Relatedness.** `G(U,U′)` holds iff some `L ∈ 𝒢_L` and weak `K` give `X′ = LXK`.
  - (⇒): TSG:84 at `t = 0` gives `X′ = L₀XK₀`.
  - (⇐): take `L_t ≡ L` and `K_t ≡ K`.
  - Equivalently, by TSG:839 (`mp` and `mpr`), GPE holds at every `t`, and all slices are the same.
- **(ii) Laws.** `Λ_C0` is the family `Γ(X)(·,j)`, the same for every `t`. `Λ_C2-ch` is the function of `Γ(X)` in §3.2.
  `Λ_C2-sel` is the function of `(Γ(X), α(X))` in §3.3.
  - Each determines its data: the single-read records give `Γ(X)(·,j)`, and under Rst-sel `(v,ok)` gives `α` and
    `(v,⊥)` gives `Γ − α`.
  - §3 derives these from the procedures for a general unitary `X`, so this is a derivation, not a citation.

**K-e: pass.**

## §7. Verdict, from the decision rule

PREREG §5: "**COUNTEREXAMPLE** iff K-a, K-b, K-c, K-d and K-e all pass and `|g(W)| ≠ |g(W′)|`."

| Condition | Result | Where |
|---|---|---|
| K-a unitarity | pass | §1 |
| K-b complete-record laws (C0, C2-ch, C2-sel; `⊥` included; `\|A\| ≥ 3` extension) | pass | §3 |
| K-c positive gauge control | pass | §4 |
| K-d ancilla countercontrol | pass | §5 |
| K-e re-derivation; definitions match | pass | §6 |
| `\|g(W)\| ≠ \|g(W′)\|` | `½ ≠ 0`: holds | §2 |

**Verdict: COUNTEREXAMPLE[C0, C2-ch, C2-sel; `|V| = 2`, `|A| ≥ 2`; constant lifts; equal complete-record laws (same
`Γ = J/2`, same `α = J/4`); all-unitary class; outside `PPer`].**

**The argument** (PREREG §4):
- K-b gives `O_C(U,U′)` for C ∈ {C0, C2-ch, C2-sel}.
- If `G(U,U′)` held, Lemma C (i) would give `W′ = LWK`, and Lemma R (a ⇒ b) would give `|g(W′)| = |g(W)|`. That
  contradicts `0 ≠ ½`, so `¬G(U,U′)`.
- Hence `Q[C]` (O⇒G) is false at `|V| = 2`, `|A| = 2`, and by §3.5 at every `|A| ≥ 2`, for each of the three
  candidates, over all unitary families.

## §8. Scoped conclusion

**Established here** (paper derivation in exact arithmetic; independent review pending):
- O⇒G fails for C0, C2-ch and C2-sel at `|V| = 2`, `|A| ≥ 2`, in the class of all unitary families (∀U).
- The witness is the constant pair `W = H₄/2` against `W′`, the same matrix with its columns at `(0,a₁)` and `(1,a₀)`
  exchanged.
- Read about OI lifts, this is CONDITIONAL[candidate tuple, ∀U, fixed `a₀`, (r1)], with (r2) for C2-sel (B4 ll.
  547–553).
- **Consequence for slice-wise readback.** At `|V| = 2`, `|A| ≥ 2`, two unitary slices with equal readback `Γ`, and
  equal `α`, need not be two-sided related. Equality of `Γ` slice by slice does not imply `G` there. This is the
  `|A| ≥ 2` counterpart of the `|A| = 1` equality `Fib = G` (B4 §3.1). It bears on F's undecided item l. 430, which the
  owner released for this verification. F itself is off `main` and is not edited.
- **Equivalence picture at `|V| = 2`, `|A| ≥ 2`, all-unitary class.**
  - **C0.** G⇒O holds, by kernel support on `main`.
    - `left_preserves_admissible` (TSG:217) and `weak_preserves_admissible` (CLG:273) make `L_tU_tK_t` an admissible
      dilation of the same `Γ_t` as `U_t`.
    - Lemma R (a ⇒ b) (§6) gives the same equality slice by slice.
    - `Λ_C0` is the family `Γ_t(·,j)` (§3.1, for any lift by (r1)), so it is unchanged.

    O⇒G fails (§7). So C0 is strictly coarser than `G`.
  - **C2-ch and C2-sel.** G⇒O fails. B4's witness WE (B4 ll. 323–341, [D] there and not reviewed on `main`) is
    re-derived here by hand, at `|V| = 2`, `|A| = 2`.
    - *The pair.* `U_0 = 1` and `U_t = P := swap((0,a₁),(1,a₁))` for `t ≥ 1`. The gauge element is `L_t ≡ L`, the
      §2 matrix of PREREG, which lies in `𝒢_L` (§4), with `K_t ≡ 1`. So `U` and `gU = (LU_t)` are `G`-related by
      construction (TSG:84).
    - *Rst-ch, root `j = 0`, reads `(0,1)`.*
      - For `U`: the read at 0 gives `0` with mass 1 and resets to `e_{p₀}`. Then `T_{1,0} = P` fixes `e_{p₀}`, so
        `p(0,0|0) = 1` and `p(0,1|0) = 0`.
      - For `gU`: `Le_{p₀} = (e_{p₀}+e_{p₁})/√2` lies in fibre 0, so the read gives `0` with mass 1 and resets to
        `e_{p₀}`. Then `T_{1,0}(gU) = LPLᴴ = LPL`. `L` gives `(e_{p₀}+e_{p₁})/√2`, `P` gives `(e_{p₀}+e_{p₃})/√2`,
        and `L` gives `½(e_{p₀}+e_{p₁}+e_{p₂}−e_{p₃})`.
      - So `p(0,0|0) = ¼+¼ = ½` and `p(0,1|0) = ½`.
      - The laws differ: `(1, 0)` against `(½, ½)`.
    - *Rst-sel, root `j = 0`, one read at 0.*
      - For `U`: `(0,ok)` has mass 1.
      - For `gU`: `(0,ok)` has mass `|⟨e_{p₀}, (e_{p₀}+e_{p₁})/√2⟩|² = ½`, and `(0,⊥)` has mass `½`.
    - With `⊕ 1` on further ancilla labels, `L` and `P` act as the identity there, so the same masses hold at
      `|A| ≥ 3`.

    O⇒G fails (§7). So C2-ch and C2-sel are incomparable with `G`, in the all-unitary class.

**Not established** (kept distinct, per the ruling):
- **`PPer`.** The witness has `Γ_0 = J/2 ≠ 1`. The `PPer` O⇒G cells at `|V| = 2`, `|A| ≥ 2` stay "not addressed".
- **Native OI-realizable lifts or restricted lift classes.** Nothing is said about them.
- **Physically sourced access.** P-conf, Acc₂, Rd, H-comp, Rst-ch and Rst-sel remain SOURCING-GAPs (B4 ll. 556–565).
- **Physical gauge or operational equivalence or inequivalence.** Not addressed.
- **A theorem promotion, a Lean statement or a manuscript claim.** None is made. A kernel formalization would need
  separate authorization, as `hadamard_slices_not_twoSided` had.

**Hidden-assumption watch (§A.31).**
- **The separation sits in the rank of the fibre-Gram data.** `W`'s data have rank 1 in each fibre, the data of `H₂`
  at `|A| = 1`. `W′`'s have rank 2, which only `|A| ≥ 2` allows. This matches TSG:105–107 ("the rank constraint is
  load-bearing") and the assessment's diagnosis.
  - CONFIRMING: the favourable reading at `|A| = 1` rests entirely on the rank-1 constraint.
- **Branch states differ while the laws agree.** The `⊥` and pre-reset states differ in sign or direction between the
  lifts (§3.2, §3.3), but Rst-ch's replacement channel and Rst-sel's non-continuation of `⊥` discard exactly that
  difference.
  - ELABORATING: a reset rule that continued `⊥` branches, or kept the ancilla, would be a different candidate. It is
    not one of the frozen candidates and is not tested.
- **∀U admits constant non-identity lifts.** Whether OI's lifts can be of this form is the restricted-class question
  (B4 W1). It is untouched.

## §9. Proposed change to the B4′ matrix (for owner approval; not applied)

The proposal is to split each of B4 rows 514, 519 and 521 by class. Proposed wording follows. Nothing in `B4PRIME.md`
is changed by this record.

| Model | `\|V\|` | `\|A\|` | Class | G⇒O | O⇒G | Support | Does NOT establish |
|---|---|---|---|---|---|---|---|
| C0 | 2 | ≥2 | all (witness outside `PPer`) | proved (TSG:217, CLG:273) | disproved: COUNTEREXAMPLE[C0, `\|V\|`=2, `\|A\|`≥2, no reset, same Γ, outside `PPer`] | G⇒O: TSG:217, CLG:273; O⇒G: the `W`/`W′` pair (this record) | the `PPer` cell; a native separation |
| C0 | 2 | ≥2 | `PPer` | proved (TSG:217, CLG:273) | not addressed | G⇒O: TSG:217, CLG:273 | either answer for O⇒G |
| C2-ch | 2 | ≥2 | all (O⇒G witness outside `PPer`) | disproved (WE) | disproved: COUNTEREXAMPLE[C2-ch, `\|V\|`=2, `\|A\|`≥2, Rst-ch, same Γ, outside `PPer`] | WE; the `W`/`W′` pair | the `PPer` O⇒G cell; a native separation |
| C2-ch | 2 | ≥2 | `PPer` | disproved (WE) | not addressed | WE | either answer for O⇒G |
| C2-sel | 2 | ≥2 | all (O⇒G witness outside `PPer`) | disproved (WE) | disproved: COUNTEREXAMPLE[C2-sel, `\|V\|`=2, `\|A\|`≥2, Rst-sel, same Γ and α, outside `PPer`] | WE; the `W`/`W′` pair | the `PPer` O⇒G cell; a native separation |
| C2-sel | 2 | ≥2 | `PPer` | disproved (WE) | not addressed | WE | either answer for O⇒G |

If the owner approves, the passages of B4 that state the `|V| = 2`, `|A| ≥ 2` O⇒G cells as not addressed for every
class would be corrected in place (§A.27) in a separately authorized change:
- §3.1 l. 273;
- §3.5 ll. 349–363;
- the Equivalence summary, ll. 524–529;
- §9's "Does NOT establish" and "Proposals", ll. 594 and 601;
- §9's premise ledger, l. 577 ("l. 430: the undecided item").

`SCOPE.md` l. 269 states the same cell as "not addressed". That file is a verbatim copy of the reviewed scope, so it is
not to be edited.

The matching #1033 planning entries would be updated with them. Whether `Q2A.md` on #1125 should carry a pointer is
the owner's decision; #1125 is not changed.

## §10. Premise ledger: §A.42 item 8 trace

Each reference to content not on `main` is classified by reading the claim it is attached to.

| Reference | Where cited | Claim it is attached to | Classification |
|---|---|---|---|
| #1033 c.6662765230 (owner ruling) | PREREG §0; this header | The authorization of the unit | Provenance. It is an owner designation quoted with author and time (§A.42 item 7). No mathematical claim uses it. |
| #1033 c.6662297536 (assessment) | PREREG §0, §1, §2; §6 | The origin of the candidate pair and its reading | Provenance. Priority for the pair is credited there. Every value it states is re-derived in §§1–6. |
| F, `BSEL2-B3-B5.md` at `88c175c3`, l. 430 | PREREG §0, §8; §8 | Naming of the released boundary; "bears on F l. 430" | Provenance. The conclusion is stated in this record's own terms (equal `Γ` does not imply `G`), with no use of F's content. |
| F ll. 254–261 (`\|A\| = 1` case) | PREREG §8 | K-d (ii) | Support on `main`. Re-derived in §5 (ii); also written out on `main` in B4 §3.1 ll. 240–246. |
| `Q2A.md` at `f3ef3d3d` (#1125 branch) | PREREG §3, §8; §6 | Lemmas R and C | Provenance. Both lemmas are re-derived from `main` in §6 (K-e). #1125 is not changed. |
| #1033 reviews of B4 (c.6654738032 and others) | not cited as support | — | Not used. B4 and SC supply definitions only (PREREG §1). |
| PREREG commit `6fad52e1` and this branch's commit order | header; PREREG §7 | The freeze-before-check invariant | **Support off `main` until landing.** (1) This invariant uses the order of the two commits. The gap closes only if the branch lands by a true merge commit. A squash merge or a rebase-merge would rewrite or orphan `6fad52e1` and `49021c8c`, so the cited ids would not be reachable from `main` (§A.42 item 3). (2) No GitHub record shows the push order. The pull request was opened after both commits existed, and commit dates are self-reported. (3) The frozen content that matters, the anchored columns `We_j` and `W′e_j`, was fixed in the host-timestamped assessment (#1033 c.6662297536, 15:43:36Z), before the ruling. (4) The other two columns cannot affect any tested quantity. P-conf roots are `e_j`, and on constant lifts `T = XXᴴ = 1`. So every mass of §3, and `Γ`, `α`, the fibre-Gram data and `g`, depend only on the anchored columns. The two columns only complete them to a unitary. The mathematical verdict depends only on `main` and the text of this record, and can be re-checked from the record alone. |
| B4 row 506 and WE (B4 ll. 323–341) | §8 "Equivalence picture" | C0 G⇒O; G⇒O fails for C2-ch and C2-sel | Support on `main`. C0 G⇒O rests on kernel lines TSG:217 and CLG:273, with Lemma R (a ⇒ b). WE's Rst-ch and Rst-sel masses are re-derived by hand in §8. Neither rests on B4's unreviewed [D] text or on F l. 178. |

**Definitions taken from B4 and SC** (both on `main`) are the frozen procedures, readings and tuples. No [D] result of
B4 is used as a premise (§A.46 item 7). The W0 formulas serve as a cross-check only (§3.4).

**Checks run at this commit:** `tools/artifact_placement_check.py` and `tools/duplicate_check.py`.

## §11. Review and next steps

- An independent mathematical review is required by the ruling and is pending. It should check:
  - the definitions;
  - the frozen pair against the assessment;
  - the hand algebra of §§1–5;
  - the decision-rule evaluation;
  - the scope statement and the §10 trace.
- Merge is not authorized. The proposed matrix change (§9) awaits the owner.
- The assessment's next open item, if the owner wishes to continue, is O⇒G for C0, C2-ch and C2-sel at `|V| = 2`,
  `|A| ≥ 2` in the `PPer` subclass. Constant lifts with `Γ ≠ 1` do not reach that subclass. It is not started here.
