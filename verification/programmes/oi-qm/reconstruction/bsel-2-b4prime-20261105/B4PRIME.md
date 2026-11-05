# BSEL-2 unit B4′: two-sided gauge relatedness against complete-record operational equivalence (paper record)

**Status: WIP / UNVERIFIED (complete draft, not reviewed).** Paper-only, written by the designated BSEL-2 writer
(#1033 c.6653013695).
**Scope:** `SCOPE.md` in this directory, a verbatim copy of the reviewed scope r3 (sha256 `df40103e…a3dd54cd`).
**Authorization:** owner approval to start, #1033 c.6653677971 (amaybaum, Claude Code session chat, 2026-11-05):
"Approved to start the independently reviewed paper-only unit. Proceed within its reviewed scope. No new scientific
computation or theorem promotion without separate authorization."
**Base:** `origin/main` `b606ee4116e97e39d90e65a4110dc70f78b7b99d`. The scope's drafting snapshot `D` is `4f016afd`. No
file under `verification/lean-mathlib/OIBridge/` changed between the two, and every [K] line cited here was re-read at
the base.
**Method:** reading and hand algebra only. No code, script, enumeration, symbolic or numerical computation, Lean build
or probe.

**Support labels.**
- [K]: kernel at the base (file:line under `verification/lean-mathlib/OIBridge/`).
- [F]: `BSEL2-B3-B5.md` at `88c175c3` (branch `research/bsel2-b3-b5-20261104`), cited by line, on F's own support.
  F is off `main`.
- [D]: derived in this record.
- Comments on #1033 are provenance only (owner ruling, c.6652903587). A cell that rests only on one is labelled
  UNRESOLVED (rests on c.<id>).

**Abbreviations.** TSG `TwoSidedGauge.lean`, CLG `CoherentLiftGauge.lean`, CF `CancellationFork.lean`, DC
`DilationChoice.lean`, RC `RootedClassification.lean`, CTI `CrossTimeInvariants.lean`. "B4N" is the B4′ note
c.6567713723, used as a cross-check only (scope §0, K-A).

***

## §0. Notation (scope §3, restated where used)

- **Carrier and gauge:**
  - The carrier is `V × A`, `|V| = n ≥ 2`, with fixed anchor `a₀`, `e_v := e_{(v,a₀)}`, `𝒜 := span{e_v}` and
    `C := 𝒜^⊥`. The fibre projector is `P_w := |w⟩⟨w| ⊗ 1_A`.
  - A lift is `U = (U_t)_{t∈ℕ}`, each `U_t` unitary on `ℂ^{V×A}`; ∀U ranges over all such families (scope §3).
  - `𝒢_L` = `LeftFibreGroup` [K TSG:78] and `𝒲` = `WeakAnchorStabilizer a₀` [K CLG:114]. A gauge element is
    `g = (L_t, K_t)` with `L_t ∈ 𝒢_L` and `K_t ∈ 𝒲`, acting by `gU := (L_tU_tK_t)`.
  - `G(U,U′)` is `TwoSidedRelated a₀ U U′` [K TSG:84].
- **Readbacks:**
  - Readback [K DC:86, DC:134]: `Γ_t(w,v) := Σ_a |U_t((w,a),(v,a₀))|² = ‖P_wU_te_v‖²`. It is column-stochastic
    [K `readback_isColStochastic` DC:93].
  - Relative object `T_{t,s} := U_tU_sᴴ`, with relative readback `𝒪₂(t,s)(w,v) = ‖P_wT_{t,s}e_v‖²`
    [K `RelativeCandidate`, `relativeCandidate_apply` CF:123, :128].
  - Anchored moduli: `α_t(w,j) := |⟨e_w,U_te_j⟩|²` and `β_{t,s}(w,v) := |⟨e_w,T_{t,s}e_v⟩|²`.
- **Two facts used throughout:**
  - **Fact W:** a weak `K` maps each anchored line to itself, `Ke_v = c_ve_v` with `|c_v| = 1`
    [K CLG:114, `weak_anchor_coeff_norm_one` CLG:146]. Being unitary, it therefore maps `C` onto `C`.
  - **Fact L:** `L ∈ 𝒢_L` is unitary and commutes with every `P_w`, so `‖P_wLx‖ = ‖P_wx‖` for all `x`.
- **𝒢 is a group (scope §3)** [D, with `weak_mul` K TSG:252]:
  - `𝒢_L` is closed under products and inverses: block-diagonal unitaries form a group.
  - Products of weak elements are weak (`weak_mul`).
  - If `K` is weak and unitary, then `Kᴴe_v = Kᴴ(c̄_v·c_ve_v) = c̄_vKᴴKe_v = c̄_ve_v`, so `Kᴴ` is weak.
  - Hence `G` is an equivalence relation, and `M_{t,s} := K_tK_sᴴ` is weak.
- **Candidates (scope §3):** C0 = (P-conf, Acc₁, Rd), C1 = (P-coh, Acc₁, Rd), C1′ = (P-conf, Acc₁, H-fac, all
  devices), and C2-x = (P-conf, Acc₂, Rd, H-comp, Rst-x). C2-auto is at `|A| = 1`; C2-ch and C2-sel are at `|A| ≥ 2`.

**Readings fixed here (stated before W0).**
- **(r1) Root-to-read evolution of the one-time candidates.** The state at a read at `t` is `U_t` applied to the root
  preparation. This is the coherent-lift convention [K `CoherentLift` CLG:124], and it is the root clause of H-comp for a
  single read.
- **(r2) The Rst-sel test follows every read, the last included.** This is the reading under which a single read
  carries an `(ok, ⊥)` record. The other reading omits the final test; its law is a coarse-graining of this one (the
  last read's ok and `⊥` masses summed). Every inequality reported below states which reads it uses.
- **(r3) "All devices" in H-fac (F ll. 62–65).** This means every finite internal space `H_d`, the one-dimensional one
  included; every unitary `G`; every unit `ψ`; and every partition into configuration-diagonal projectors.

## §1. W0: the complete-record laws `Λ_C`

Each law below is the family of unnormalized masses of every record, indexed by the candidate's procedures.

### W0.1 C0
- **Procedure:** root `j`, one read at `t`.
- **Branch masses:** by (r1) the state is `U_te_j`. Rd's record `v` has mass `‖P_vU_te_j‖² = Γ_t(v,j)`.
- **Bookkeeping:** there is no failure record. `Σ_v Γ_t(v,j) = ‖U_te_j‖² = 1` (K-G).
- **Result:** `Λ_C0(U) = (Γ_t(·,j))_{t,j}`. [D]

### W0.2 C1
- **Procedure:** root `ρ̃ = Σ_{jk} ρ_{jk} e_je_kᴴ` (that is, `ρ ⊗ |a₀⟩⟨a₀|`), for every density matrix `ρ` on `V`;
  one read at `t`.
- **Branch masses:** record `i` has mass
  `tr(P_iU_tρ̃U_tᴴ) = Σ_{jk} ρ_{jk}⟨P_iU_te_k, P_iU_te_j⟩ = Σ_{jk} ρ_{jk} FG^{(i)}_t(k,j) = tr(ρ·FG^{(i)}_t)`.
  - Here `FG^{(i)}_t := FibreGram a₀ U_t i`, with `FG^{(i)}(k,j) = ⟨P_iUe_k, P_iUe_j⟩` [K TSG:95, its docstring
    formula].
- **Bookkeeping:** there is no failure record. `Σ_i FG^{(i)}_t = 1` (the anchored columns are orthonormal), so the
  masses sum to `tr ρ = 1`.
- **Result:** `Λ_C1(U) = (tr(ρ·FG^{(i)}_t))_{ρ,t,i}`. [D]

### W0.3 C1′
- **Procedure:** root `j`, one read at `t` through a device `(H_d, G, ψ, {P_c})` as in (r3).
- **Branch masses:** with `X := G(1 ⊗ |ψ⟩)`, an isometry, and `A_c := XᴴP_cX`, cell `c` has mass
  `‖P_cG(U_te_j ⊗ ψ)‖² = ⟨U_te_j, A_c U_te_j⟩` (F ll. 62–65).
- **Bookkeeping:** there is no failure record. `Σ_c A_c = XᴴX = 1`.
- **Result:** `Λ_C1′(U) = (⟨U_te_j, A_cU_te_j⟩)_{j,t,device,c}`. [D]

### W0.4 C2-auto and C2-ch (factorized form)
- **Procedure:** root `j` and a read list `t₁ < … < t_k`, `k ≥ 1`.
- **Evolution (H-comp):** the state evolves by `U_{t₁}` from the root to `t₁`, and by `T_{t_{m+1},t_m}` between reads.
- **Unnormalized branch states, by induction on `m`:**
  - Before the first read the state is `U_{t₁}e_j`.
  - Rd with record `v₁` has mass `m₁ = Γ_{t₁}(v₁,j)`.
  - The post-read state lies in fibre `v₁`. Under Rst-auto (`|A| = 1`) it is already a multiple of `e_{v₁}`. Under
    Rst-ch the ancilla is replaced by `|a₀⟩`, which leaves the subnormalized state `m₁·e_{v₁}e_{v₁}ᴴ`.
  - In either case the state entering the next step is `m₁` times the pure state `e_{v₁}`; a phase does not enter any
    later norm.
  - Evolving by `T := T_{t₂,t₁}` and reading `v₂` multiplies the mass by `‖P_{v₂}Te_{v₁}‖² = 𝒪₂(t₂,t₁)(v₂,v₁)`, and
    leaves `m₁m₂·e_{v₂}` after the reset. Iterating gives the law below.
- **Result** [D]:

  `p(v₁,…,v_k | j) = Γ_{t₁}(v₁,j) · Π_{m=1}^{k−1} 𝒪₂(t_{m+1},t_m)(v_{m+1},v_m)`.

- **Bookkeeping:** there is no failure record. `Σ_w 𝒪₂(t,s)(w,v) = ‖T_{t,s}e_v‖² = 1`, so the masses sum to 1 for
  each `j` (K-G).

### W0.5 C2-sel (ok-chain and `⊥` form)
- **Procedure:** as W0.4. After each read the test `Π := 1_V ⊗ |a₀⟩⟨a₀|` is applied (r2).
- **One read and test:** let `x` be the unnormalized state before a read, and `v` the read's record. The test splits
  the branch in two:
  - `(v, ok)`, mass `‖ΠP_vx‖² = |⟨e_v,x⟩|²`, leaving `⟨e_v,x⟩e_v`;
  - `(v, ⊥)`, mass `‖P_vx‖² − |⟨e_v,x⟩|²`. This branch is not continued.
- **Result** [D]: a record is a sequence of `(v_m, ok)` that may end in one `(v_m, ⊥)`.
  - The step-1 factor is `α_{t₁}(v₁,j)` for ok, and `Γ_{t₁}(v₁,j) − α_{t₁}(v₁,j)` for `⊥`.
  - The step-`m` factor (`m ≥ 2`, from `e_{v_{m−1}}`) is `β(v_m,v_{m−1})` for ok, and
    `𝒪₂(v_m,v_{m−1}) − β(v_m,v_{m−1})` for `⊥`, both at `(t_m,t_{m−1})`.
  - The mass of a record is the product of its factors.
- **Bookkeeping:** the ok and `⊥` factors at each step sum over `v` to `Σ_vΓ = 1` or `Σ_v𝒪₂ = 1`, so the masses sum to
  1 for each `j` (K-G).

### W0.6 Cross-check against B4N (K-A)
- **Agreements:**
  - B4N D1 (C0) and D2 (C1) state the same laws.
  - B4N D4 states the factorization of W0.4, and for Rst-sel the ok-chain with `⊥` mass `‖(1 − |a₀⟩⟨a₀|)P_v·‖²`. That
    expression equals the step factor of W0.5.
  - B4N D2′ gives C1′'s law in the form `|⟨χ|φ⟩|²`. W0.3 gives the general effect form, of which that is the rank-one
    case (§2.3).
- **Result:** no disagreement, so no item halts.

## §2. E[C]: the exact operational quotients

`R_C` is the scope's frozen relation (scope §1). Each direction is decided on its own.

### 2.1 C0
- **E[C0]⊇ and E[C0]⊆:** both proved, at every `|V|`, `|A|`, over all unitary families [D].
- **Proof:** by W0.1, `Λ_C0(U)` is the family `Γ_t(·,j)` itself. So `O_C0 = R_C0`, which is slice-wise equality of
  `Γ` (F calls this `Fib`, l. 243).

### 2.2 C1
- **E[C1]⊇:** proved, every `|A|` [D]. Equal fibre-Gram data give equal masses `tr(ρ·FG^{(i)}_t)` (W0.2).
- **E[C1]⊆:** proved, every `|A|` [D].
  - Let `X := FG^{(i)}_t(U) − FG^{(i)}_t(U′)`. It is Hermitian (each Gram matrix is), and `tr(ρX) = 0` for every density
    matrix `ρ`.
  - With `ρ = |x⟩⟨x|` this gives `⟨x,Xx⟩ = 0` for every `x ∈ ℂ^V`. By complex polarization, `X = 0`.

### 2.3 C1′
- **E[C1′]⊇:** proved [D]. If `U′_te_j = c U_te_j` with `|c| = 1`, every mass `⟨U_te_j, A_cU_te_j⟩` (W0.3) is unchanged.
- **E[C1′]⊆:** proved [D].
  - Fix a unit vector `χ ∈ ℂ^{V×A}`. Take the device `H_d = ℂ`, `ψ = 1`, `G` any unitary with `Gχ = e_{(0,a₀)}`, and
    cells `{Q, 1 − Q}` with `Q = |(0,a₀)⟩⟨(0,a₀)|`. Both cells are configuration-diagonal, so the device is admitted
    by (r3).
  - Then `A_Q = Gᴴ Q G = |χ⟩⟨χ|`, so `Λ_C1′` contains `|⟨χ, U_te_j⟩|²` for every unit `χ`.
  - Write `x = U_te_j` and `y = U′_te_j`. Equal laws at `χ = x` give `|⟨x,y⟩| = 1`. Equality in Cauchy–Schwarz then gives
    `y ∈ U(1)·x`.

### 2.4 C2-auto (`|A| = 1`)
- **E[C2-auto]⊇:** proved [D], by the factorized law of W0.4.
- **E[C2-auto]⊆:** proved [D].
  - The single-read lists `(t)` give `Γ_t(·,j)` for every `j`.
  - The two-read lists `(s,t)` give `Γ_s(v,j)·𝒪₂(t,s)(w,v)`.
  - At `|A| = 1`, `Γ_s = |U_s|²` is doubly stochastic. So for each `v` some `j` has `Γ_s(v,j) > 0`, and dividing by it
    recovers `𝒪₂(t,s)(·,v)` for every `v` and every `s < t`.

### 2.5 C2-ch and C2-sel (`|A| ≥ 2`)
- **E[C2-ch]⊇ and E[C2-sel]⊇:** proved [D], by the formulas of W0.4 and W0.5. Every factor they use is a component of
  `R_C2-ch` or `R_C2-sel`.
- **E[C2-ch]⊆ and E[C2-sel]⊆:** disproved, **COUNTEREXAMPLE[C2-ch and C2-sel, `|V| = 2`, `|A| = 2`, equal `Γ`, witness
  outside `PPer`]** (witness WG) [D].
  - **Witness WG.** Write `a₁` for the second ancilla label, and let `S := swap((1,a₀),(0,a₁))` and
    `P := swap((0,a₁),(1,a₁))`. Set
    - `U_0 = U′_0 = S`;
    - `U_t = 1` and `U′_t = P` for `t ≥ 1`.

    All four maps are permutation matrices, hence unitary.
  - **Readbacks.**
    - `Se_0 = e_0` and `Se_1 = (0,a₁)`. Both lie in fibre 0, so `Γ_0 = [[1,1],[0,0]]` (rows `w`, columns `j`) for both
      lifts.
    - For `t ≥ 1`, `P` fixes `e_0` and `e_1`, so `Γ_t = 1` for both.
    - Relative objects: `T_{t,0} = U_tS`. For `1 ≤ s < t`, `T_{t,s} = 1` for `U` and `PP = 1` for `U′`.
    - Column `v = 0` of `𝒪₂(t,0)`: `U_tSe_0 = e_0` for both lifts, giving `(1,0)ᵀ` for both.
    - Column `v = 1`: `U_tSe_1 = (0,a₁)` for `U`, giving `(1,0)ᵀ`; and `P(0,a₁) = (1,a₁)` for `U′`, giving `(0,1)ᵀ`.
  - **`R_C2-ch` fails:** `𝒪₂(1,0)` differs in column 1.
  - **The laws are equal anyway.**
    - Column 1 of `𝒪₂(t,0)` enters a mass only after a read at `0` with record `1`, and that mass is
      `Γ_0(1,j) = 0` for every `j` in both lifts.
    - Every other factor in W0.4 agrees: `Γ_t` for every `t`; column 0 of `𝒪₂(t,0)`; and `𝒪₂(t,s) = 1` for
      `1 ≤ s < t`.
    - Under Rst-sel the extra factors also agree. `α_0(·,0) = (1,0)` and `α_0(·,1) = (0,0)` for both lifts;
      `α_t = 1` for `t ≥ 1`, since `P` fixes `e_0, e_1`; `β_{t,0}(·,0) = (1,0)` for both; column 1 of `β_{t,0}` is 0
      for both, since `(0,a₁)` and `(1,a₁)` have no anchored component; and `β_{t,s} = 1` for `1 ≤ s < t`.
    - The `⊥` masses are `Γ − α` and `𝒪₂ − β`. On the reachable branches they agree; for example root `j = 1` at
      `t = 0` gives `(0,⊥)` with mass 1 in both lifts.
  - **Masses (K-G):** each root's masses sum to 1, since `Σ_v Γ_0(v,j) = 1`.
  - **Class:** row 0 of `Γ_0` sums to 2, so `Γ_0` is not row-stochastic, and `Γ_0 ≠ 1`. The witness is outside
    `PPer` in either orientation (W9).
  - **Coverage (K-H):** both lifts are constant for `t ≥ 1`, and the argument covers every finite read list.
- **What this shows** [D]. Call `v` *reachable at `s`* when some record whose last read is at `s` with record `v`
  (under Rst-sel, `(v, ok)`) has positive mass, for some root `j` and some read list ending at `s`.
  - *Reachable columns are recovered.* If such a record has mass `m > 0`, appending a read at `t > s` to its read list
    gives masses `m·𝒪₂(t,s)(w,v)` under Rst-auto or Rst-ch, and `m·β_{t,s}(w,v)` and
    `m·(𝒪₂ − β)_{t,s}(w,v)` under Rst-sel. Dividing by `m` recovers column `v` (W0.4, W0.5).
  - *Unreachable columns never enter.* In W0.4 and W0.5, every factor in column `v` of the step `(s, t)` multiplies the
    mass of a record ending at `v` at `s`, or at `(v, ok)` under Rst-sel. If `v` is unreachable at `s`, every such
    product is 0, so column `v` enters no mass.
  - So the complete record determines `𝒪₂(t,s)(·,v)` exactly on the columns reachable at `s`. At `|A| = 1` every
    column is reachable (§2.4). At `|A| ≥ 2` a fibre can be unreachable (WG), and the frozen `R_C2` is then strictly
    finer than `O_C2`.
  - A reachability-restricted `R_C2` is a proposal only (scope §1, change 16), and is not pursued here.
  - The pair is `G`-related: at `t ≥ 1` both slices have fibre-Gram data `diag(1,0), diag(0,1)`, and `twoSidedRelated_iff`
    (mpr, TSG:839) applies with `c ≡ 1`. So WG bears on no owner-direction cell.
- **Equivalence:** `O_C = R_C` holds for C0, C1, C1′ and C2-auto, at the scopes stated. It fails for C2-ch and C2-sel.

## §3. The owner directions, per candidate (Cmp)

Throughout, **G⇒O** is `R[C]`: `∀U ∀g ∈ 𝒢, Λ_C(gU) = Λ_C(U)`. **O⇒G** is `Q[C]`: `O_C(U,U′) ⇒ G(U,U′)`. Each
G⇒O witness is a gauge image under one fixed procedure (K-I), so `Γ` is shared (K-D).

**Explicit witnesses.** All are checked by hand, in exact arithmetic.

- **H₂** `= (1/√2)[[1,1],[1,−1]]` acts on `span{e_0,e_1}` and as the identity elsewhere (on `C` and on further
  configurations). `Z := diag(1,−1)` on `e_0, e_1`, identity elsewhere; it is weak.
- **Alternating placement.** A matrix `M` is placed "alternating" when `U_t = 1` at even `t` and `U_t = M` at odd `t`.
  Then `Γ = (1, |M|², 1, |M|², …)`. For each `M` used here, `|M|²` is symmetric and doubly stochastic, so `Γ ∈ PPer` in
  either orientation: `Γ_0 = 1`, rows sum to 1, period 2 [K RC:32] (W9).
- **Provenance check.** The provenance note "`PPer` if placed at `t = 1` with `U₀ = 1`" (SCOPE §9) is false as
  stated. With `U_0 = 1` and `U_t = M` for every `t ≥ 1`, every candidate period `p ≥ 1` gives `Γ_p = |M|² ≠ 1 = Γ_0`,
  so `Γ` is not periodic. The alternating placement is used instead (K-E finding).

### 3.1 C0
- **G⇒O: proved★, every `|V|`, `|A|`, all unitary families.**
  - Support: F l. 178, `left_preserves_admissible` TSG:217 and `weak_preserves_admissible` CLG:273. Each slice
    `L_tU_tK_t` is an admissible dilation of the same `Γ_t`.
  - By W0.1 that is equality of `Λ_C0`.
- **O⇒G at `|V| = 2`, `|A| = 1`: proved★** (F ll. 254–261).
  - **K-A note.** The same argument is used in §3.5, where it settles a K-A item. It is therefore written out here.
  - At `|A| = 1`, `FG^{(i)}(j,k) = conj(U_{ij})U_{ik}`. Equal `Γ` fixes the diagonal moduli.
  - Column orthogonality gives `FG^{(1)}(0,1) = −FG^{(0)}(0,1)` for each unitary.
  - Equal moduli give `|FG′^{(0)}(0,1)| = |FG^{(0)}(0,1)|`. One phase `c̄_0c_1` therefore matches the `(0,1)` entry of
    both fibres (any phase does if it is 0), and the `(1,0)` entries are its conjugates. That is `GramPhaseEquiv`.
  - `twoSidedRelated_iff` (mpr, TSG:839) then gives `G`.
- **O⇒G at `|V| ≥ 3`, `|A| = 1`, all: disproved★.**
  - TG3 at `|V| = 4` [K TSG:907, :966].
  - The constant pair `F₃` against `F̄₃` at `|V| ≥ 3` (F ll. 244–249), re-derived under WA below.
  - Both have `Γ_0 ≠ 1`, so they lie outside `PPer`.
- **O⇒G at `|V| = 4`, `|A| = 1`, `PPer`: disproved★.**
  - The `Γ^alt` pair: alternating `H(1)` against alternating `H(i)` (F ll. 137–144, Q5a, Q5b).
  - Orientation re-checked here: `J/4` is symmetric and doubly stochastic.
- **O⇒G at `|V| = 3` and `|V| ≥ 5`, `|A| = 1`, `PPer`: disproved [D], witness WA.**
  - **Witness WA.** Alternating `F₃` against alternating `F̄₃`, with `F₃ = [ω^{jk}]/√3` and `ω = e^{2πi/3}`, and `⊕ 1` on
    further configurations at `|V| > 3` (scope §7).
  - **Equal `Γ`:** both lifts have `Γ = (1, J₃/3 ⊕ 1, 1, …)`.
  - **Non-relatedness.** The `∼_D` invariant of TSG:870 at `i₀ = 0`, `i₁ = 1`, `t = 1` is
    `FG^{(0)}(1,0)·FG^{(1)}(0,1) = conj(U_{01})U_{00}·conj(U_{10})U_{11}`.
    - For `F₃` this is `(1/3)(ω/3) = ω/9`; for `F̄₃` it is `ω̄/9`. These differ, since `ω ∉ ℝ`.
    - By `gramPhaseEquiv_cross_invariant` (TSG:870) and `gramPhaseEquiv_of_twoSided` (TSG:263, forward), the slices at
      `t = 1` are not two-sided related.
    - `TwoSidedRelated` requires every slice (TSG:84). So `¬G`.
  - **Scope-named alternative:** `Γ^alt ⊕ 1` also works at `|V| ≥ 5`. Its invariant `z/16` at `z = 1, i` is `1/16`
    against `i/16`.
- **O⇒G at `|V| ≥ 3`, `|A| ≥ 2`, all: disproved★** (F ll. 245–249: `F₃` on the anchored lines with `1` on `C`).
- **O⇒G at `|V| ≥ 3`, `|A| ≥ 2`, `PPer`: disproved [D], witness WA′.**
  - **Witness WA′.** `U_t = M_t ⊕ 1_C`, where `M_t` is WA's slice acting on `𝒜` in the basis `e_v`.
  - Since `U_te_j ∈ 𝒜`, only `a = a₀` contributes to the fibre-Gram data. So `FG^{(i)}(j,k) = conj(M_{ij})M_{ik}`, and
    the invariant is again `ω/9` against `ω̄/9`.
  - `gramPhaseEquiv_of_twoSided` holds for every `L ∈ 𝒢_L` at every `|A|`. So the larger left group does not relate
    the pair (W7).
- **O⇒G at `|V| = 2`, `|A| ≥ 2`: not addressed** (F §6 undecided, F l. 430; scope §8).

### 3.2 C1
- **G⇒O: disproved [D], every `|V| ≥ 2` and every `|A|`, witness WB, in `PPer`.**
  - **Witness WB.** `U` = alternating `H₂`; `g` has `L ≡ 1`, `K_t = Z` at odd `t` and `1` at even `t`.
  - Prepare `ρ = |+⟩⟨+|` with `|+⟩ = (e_0+e_1)/√2`, and read at `t = 1`.
    - For `U`: `H₂|+⟩ = e_0`, so the law is `(1, 0, …)`.
    - For `gU`: `H₂Z|+⟩ = H₂|−⟩ = e_1`, so the law is `(0, 1, …)`.
  - At `|A| ≥ 2` the states stay in `𝒜`, so the masses are the same.
  - **Comparison:** B4N's witness was `|V| = 4` with `H(1)`. A smaller witness suffices.
- **O⇒G: proved [D], every `|V|`, `|A|`, all unitary families.**
  - By §2.2, equal laws give equal `FG^{(i)}_t` for every `t`. That is `GramPhaseEquiv` with `c ≡ 1`, `‖1‖ = 1`.
  - `twoSidedRelated_iff` (mpr, TSG:839), with every slice unitary, then gives `G`.
- **Not equivalent:** C1 refines `G` strictly.

### 3.3 C1′
- **G⇒O: disproved [D], every `|V| ≥ 2` and every `|A|`, witness WC, in `PPer`.**
  - **Witness WC.** `U` = alternating `H₂`; `g` has `K ≡ 1`, `L_t = 1 − 2P_1` (`−1` on fibre 1) at odd `t` and `1`
    at even `t`. `L_t` is block-diagonal across fibres and unitary.
  - The device is §2.3's with `χ = (e_0+e_1)/√2` and `G = H₂` (so `Gχ = e_0`). Root `j = 0`, read at `t = 1`.
    - For `U`: `U_1e_0 = χ`, so cell `Q` has mass `|⟨χ,χ⟩|² = 1`.
    - For `gU`: `L_1U_1e_0 = (e_0−e_1)/√2`, so cell `Q` has mass 0.
- **O⇒G: proved [D], every `|V|`, `|A|`, all unitary families.**
  - By §2.3, `U′_te_j = c_j(t)U_te_j`. Put `K_t := U_tᴴU′_t`: it is unitary with `K_te_j = c_j(t)e_j`, so it is weak.
  - With `L_t = 1`, `U′_t = L_tU_tK_t`, which is `G` (TSG:84).
- **Not equivalent.**

### 3.4 C2-auto (`|A| = 1`)
- **G⇒O: disproved [D], every `|V| ≥ 2`, witness WD, in `PPer`.**
  - **Witness WD.** `U` = alternating `H₂` (`⊕ 1` beyond `|V| = 2`); `g` has `L ≡ 1`, `K_1 = Z` and `K_t = 1`
    otherwise.
  - Root `j = 0`, reads `(1,3)`.
    - For `U`: `T_{3,1} = H₂H₂ᴴ = 1`, so `p(0,0|0) = Γ_1(0,0)·1 = ½` and `p(0,1|0) = 0`.
    - For `gU`: `T = H₂K_3K_1ᴴH₂ᴴ = H₂ZH₂ = σ_x`, so `p(0,0|0) = 0` and `p(0,1|0) = ½`.
- **O⇒G at `|V| = 2`: proved [D from F].**
  - C2's single-read lists are C0's procedures (W0.1, W0.4), so `O_C2-auto ⊆ O_C0`.
  - `O_C0 ⊆ G` at `|V| = 2`, `|A| = 1` (§3.1, written out).
- **O⇒G at `|V| ≥ 3`: disproved [D], witness WA, in `PPer`; at `|V| = 4` also the `Γ^alt` pair.**
  - By E[C2-auto]⊇ it suffices that `R_C2-auto` agrees.
    - `Γ` agrees.
    - Same-parity `t, s`: `T = 1` or `M_tM_tᴴ = 1`.
    - Mixed parity: `|M|²` or `|Mᴴ|² = (|M|²)ᵀ`, which is `J₃/3 ⊕ 1` for `M = F₃` and for `M = F̄₃` alike
      (`J/4` for the `Γ^alt` pair).
  - The pair is not `G`-related (§3.1).
  - **K-A:** F Q5c's C2 cells (F ll. 366–376), which F derived through B4N D4, are re-derived here on W0.4. They agree.
- **Not equivalent at any `|V|`:**
  - At `|V| = 2`: `O_C2-auto ⊊ G`.
  - At `|V| ≥ 3`: incomparable.

### 3.5 C2-ch and C2-sel (`|A| ≥ 2`)
- **G⇒O: disproved [D], every `|V| ≥ 2`, witness WE, in `PPer`.**
  - **Witness WE.** `U_0 = 1` and `U_t = P = swap((0,a₁),(1,a₁))` for `t ≥ 1`; `g` has `L_t ≡ L := 1_V ⊗ H₂` on
    `{a₀,a₁}` (identity on any further labels) and `K ≡ 1`.
  - **Class:** `Γ ≡ 1` for both, since `P` fixes `e_0, e_1`. So `Γ ∈ PPer` with period 1, in either orientation.
  - **Rst-ch, root `j = 0`, reads `(0,1)`:**
    - Both lifts read `v₁ = 0` with mass 1: `Le_0 = ((0,a₀)+(0,a₁))/√2` lies in fibre 0.
    - For `U`: `T_{1,0}e_0 = Pe_0 = e_0`, so `p(0,0|0) = 1`.
    - For `gU`: `T = LPLᴴ`, with `Lᴴ = L` since `H₂` is real symmetric.
      - `Le_0 = ((0,a₀)+(0,a₁))/√2`.
      - `P` sends this to `((0,a₀)+(1,a₁))/√2`.
      - `L` sends that to `½[(0,a₀)+(0,a₁)+(1,a₀)−(1,a₁)]`.
      - So `p(0,0|0) = p(0,1|0) = ½`, with no `⊥` record.
  - **Rst-sel, root `j = 0`, single read at `0`:**
    - For `U`: `(0,ok) = 1`.
    - For `gU`: `(0,ok) = |⟨e_0,Le_0⟩|² = ½` and `(0,⊥) = ½`.
  - **Rst-sel, reads `(0,1)`, all-ok:**
    - For `U`: `((0,ok),(0,ok)) = 1`.
    - For `gU`: `((0,ok),(0,ok)) = ½·|½|² = ⅛` and `((0,ok),(1,ok)) = ⅛`.
    - So the difference is not confined to `⊥` masses.
  - Embedding with `⊕ 1` on further configurations covers `|V| > 2`.
- **O⇒G (Q2A) at `|V| ≥ 3`: disproved [D], witness WA′, in `PPer`.**
  - WA′'s lifts preserve `𝒜` at every `t`, and so does every relative object.
  - Hence, under Rst-ch, every post-read state is already on an anchored line. Under Rst-sel, `α_t = Γ_t` and
    `β = 𝒪₂`, so every `⊥` mass is 0 (W7).
  - `R_C2-ch` and `R_C2-sel` agree by the parity computation of §3.4, and E[C2-x]⊇ gives equal laws.
  - The pair is not `G`-related (§3.1, WA′).
- **O⇒G at `|V| = 2`: not addressed.**
  - **Conflict between scope sections.** Scope §9 preregistered this cell as "open (Q2A)". Scope §8 leaves F §6's
    undecided items untouched.
  - Any pair that disproved this cell would have equal `Γ` (W0) and would not be `G`-related. It would therefore decide
    F §6's undecided item "DC's strictness at `|V| = 2`, `|A| ≥ 2`" (F l. 430).
  - The stop resolves the conflict conservatively, in favour of §8. The cell stops at the scope boundary, not at a
    mathematical wall.
  - **Proof direction.** The two candidates differ.
    - **C2-ch.** A proof of `O_C2-ch ⊆ G` at `|V| = 2`, `|A| ≥ 2` would decide F l. 430's item, in the positive
      direction. Constant lifts are admitted under ∀U, and on them the C2-ch law is a function of `Γ` alone, so such
      a proof gives `Fib ⊆ G` slice by slice at that size. The C2-ch proof direction is therefore outside the scope
      boundary of §8.
    - **C2-sel.** The proof direction (`O_C2-sel ⊆ G` at `|V| = 2`, `|A| ≥ 2`) can be investigated without deciding
      F l. 430. No proof of it is established.
    - Whether to release the F l. 430 boundary is left to the owner.
- **Not equivalent at `|V| ≥ 3`.**

## §4. S1′: the subgroup C1′ respects
- **Result:** `𝒢_C1′ = {g : L_t ∈ U(1)·1 for every t; K_t ∈ 𝒲}`. Both inclusions proved [D], at every `|V| ≥ 2` and
  every `|A|`.
- **(⊇):** `L_tU_tK_te_j = λ_tc_j(t)U_te_j ∈ U(1)·U_te_j`. E[C1′]⊇ gives equal laws.
- **(⊆):** let `g ∈ 𝒢_C1′`.
  - E[C1′]⊆ gives `L_tU_tK_te_j ∈ U(1)·U_te_j` for every `U`, `t` and `j`. Since `K_te_j = c_je_j`, this says
    `L_tx ∈ U(1)·x` for every unit vector `x = U_te_j`, and as `U_t` ranges over all unitaries, every unit `x` occurs.
  - Then `e_p`, `e_q` and `(e_p+e_q)/√2` are eigenvectors of `L_t` for every pair `p, q`. That forces equal
    eigenvalues, so `L_t` is scalar.
- **Use in this record:** reported outside the owner-direction cells (scope §1). It is used by K-B.

## §5. Conditional block: composition physically sourced (Src′)

Everything in this section is **CONDITIONAL[H-comp, Acc₂, Rst-x, P-conf]**. It is stated relative to `𝒢_C2-x`, not
OI's gauge. Physical supply of H-comp, retention (Acc₂), any reset and P-conf is a **SOURCING-GAP** (#866, #1009,
#1023). No cell here fills a G⇒O or O⇒G cell.

### 5.1 `𝒢_C2-x`, re-derived
- **Result:** `𝒢_C2-x = {g : (i) K_tK_sᴴ ∈ U(1)·1 for every s, t; (ii) L_tᴴe_v ∈ U(1)·e_v for every t, v}`, for each
  `x`. Both inclusions are proved [D] at `|V| ≥ 2`. At `|A| = 1`, (ii) holds automatically, since `𝒢_L` is then the
  diagonal unitaries.
  - (i) is equivalent to `K_t = e^{iθ_t}K_0` for every `t`:
    - (⇐) `K_tK_sᴴ = e^{i(θ_t−θ_s)}K_0K_0ᴴ = e^{i(θ_t−θ_s)}1`.
    - (⇒) `K_tK_0ᴴ = λ_t1` gives `K_t = λ_tK_0`, and `|λ_t| = 1` because both sides are unitary.
  - The result agrees with B4N's `Sub[C2]` (K-A).
- **(⇐).** Write `M := K_tK_sᴴ = λ1`.
  - Then `T(gU) = λL_tT(U)L_sᴴ`, and by (ii) `T(gU)e_v = λφ_v L_tT(U)e_v`.
  - By Fact L, `𝒪₂` agrees. By (ii) and Fact W, `α` and `β` agree: `|⟨e_w, L_t y⟩| = |⟨L_tᴴe_w, y⟩| = |⟨e_w, y⟩|`.
    `Γ` agrees as in §3.1.
  - Every factor of W0.4 and W0.5 is therefore unchanged.
- **(⇒ ii), `|A| ≥ 2`.**
  - **Rst-sel.** Choose `U_s` with `U_se_j = y := L_sᴴe_v`. A single read at `s` gives `(v,ok)` with mass
    `|⟨L_sᴴe_v, U_se_j⟩|² = 1` for `gU`, and `|⟨e_v, y⟩|²` for `U`. Equality forces `y ∈ U(1)e_v`.
  - **Rst-ch.** Put `U_s = 1` and `U_t = XMᴴ`, with `X` unitary and the other times arbitrary. Take root `j = v`, which
    reads `v` at `s` with mass 1.
    - Then `𝒪₂(U)(t,s)(w,v) = ‖P_wXe_v‖²`, since `Mᴴe_v ∝ e_v` by Fact W.
    - And `𝒪₂(gU)(t,s)(w,v) = ‖P_wXy‖²`.
    - If `y ∉ U(1)e_v`, write `e_v = γy + δz` with `z ⊥ y` and `|γ| < 1`. Choose `X` with `Xy = e_w` and
      `Xz = e_{w′}`, `w ≠ w′`. The two masses are then 1 and `|γ|²`.
- **(⇒ i), given (ii).** Suppose `M = K_tK_sᴴ` is not scalar for some `s < t`.
  - *An eigenvector pair with one anchored member.* Since `M` is weak, `M = diag(μ_v) ⊕ M_C` on `𝒜 ⊕ C`.
    - If the `μ_v` are not all equal, take `x = e_j` and `y = e_k` with `μ_j ≠ μ_k`.
    - Otherwise all `μ_v = ν` and `M_C ≠ ν1`. This needs `C ≠ 0`, hence `|A| ≥ 2`. Take `y ∈ C` an eigenvector of
      `M_C` with eigenvalue `μ ≠ ν`, and `x = e_j` for any `j`.
  - *Eigenvalues.* Write `λ` and `μ` for the eigenvalues of `x` and `y`: `Mx = λx`, `My = μy`, `λ ≠ μ`.
  - *The lift.* Choose `F` unitary with `Fx = (e_0+e_1)/√2` and `Fy = (e_0−e_1)/√2`, and set `U_s = U_t = F`.
  - *Root and first read.* From the root `j` with `x = e_j`, the read at `s` gives record 0 with mass ½, and ok mass ½
    under Rst-sel, for both lifts (Fact L and (ii)). The post-read state is a multiple of `e_0`.
  - *Second read.* For `U`, `T = 1`, so the read at `t` gives record 1 with mass 0. For `gU`,
    `T(gU)e_0 = φL_tFMFᴴe_0 = φL_t((λ+μ)e_0 + (λ−μ)e_1)/2`, which puts mass `|λ−μ|²/4 > 0` on fibre 1.
  - *Conclusion.* The mass of the records `((0,·),(1,·))` is 0 for `U` and `½·|λ−μ|²/4` for `gU`, under every reset
    variant.

### 5.2 Own[C2-x]: does `O_C2-x ⇒ ∼_C2-x`?
**Own[C2-x] is disproved for every `x`, at every `|V| ≥ 2`, in `PPer`** [D]. Hence in no scope tested here is the
complete record of C2 a complete invariant of the gauge `𝒢_C2-x` that its laws respect.

- **`|V| = 2`, `|A| = 1` (C2-auto), witness WH.**
  - **The lifts.** Let `F′ := (1/√2)[[1,i],[i,1]]`, which is unitary. Set `U_t = 1`, `H₂`, `F′` for
    `t ≡ 0, 1, 2 (mod 3)`, and `U′_t := U_tK_t` with `K_t = Z` at `t ≡ 2` and `1` otherwise.
  - **Class:** `Γ = (1, J/2, J/2, …)` for both, with period 3, symmetric and doubly stochastic. So `Γ ∈ PPer`.
  - **Equal laws.** `M_{t,s} = Z` exactly when one of `t, s` is `≡ 2`. By E[C2-auto]⊇ it suffices to compare
    `|U_tZU_sᴴ|²` with `|U_tU_sᴴ|²` for the residue pairs `(r_s, r_t)`:
    - `(0,2)`: `|F′Z|² = |F′|²`, since a right diagonal phase leaves moduli unchanged.
    - `(2,0)`: `|ZF′ᴴ|² = |F′ᴴ|²`, since a left diagonal phase leaves moduli unchanged.
    - `(1,2)`: `F′H₂ = ½[[1+i, 1−i],[1+i, −1+i]]` and `F′ZH₂ = ½[[1−i, 1+i],[−1+i, 1+i]]`. Every entry of each has
      modulus² ½.
    - `(2,1)`: these are the conjugate transposes of the `(1,2)` matrices, so the moduli are again ½ throughout.
    - Every other residue pair has `M = 1`.
  - **Not `∼_C2-auto`.** Take any representation `U′_t = L_tU_tK′_t` with diagonal `L_t, K′_t`.
    - At `t = 1`: `H₂` has no zero entry, so `l_wk′_v = 1` for all `w, v`, forcing `K′_1 = λ̄1`.
    - At `t = 2`: `l_wk′_v f_{wv} = f_{wv}z_v`, with `F′` having no zero entry, which forces `K′_2 = μ̄Z`.
    - Then `K′_2K′_1ᴴ ∝ Z` is not scalar, so (i) fails for every representation.
  - The pair is `G`-related (by `g` itself, which lies outside `𝒢_C2-auto`).
- **`|V| = 2`, `|A| ≥ 2` (C2-ch, C2-sel), witness WI.**
  - **The lifts.** WH placed on `𝒜`, with `⊕ 1_C`. The laws are WH's: states stay in `𝒜`, and every `⊥` mass is 0.
  - **Not `∼_C2-x`.** Any `(L, K′) ∈ 𝒢_C2-x` has `L_t` diagonal on `𝒜` by (ii), and `K′_t` diagonal on `𝒜` by Fact W.
    Both preserve `𝒜`, as does `U_t`. Restricting to `𝒜` reproduces WH's forcing, so `K′_2K′_1ᴴ` is not scalar on `𝒜`.
- **`|V| ≥ 3`, every `|A|`.** WA and WA′ have equal laws and are not `G`-related. Since `𝒢_C2-x ⊆ 𝒢`, they are not
  `∼_C2-x`-related either.
- **What follows about `G` (Src′ (c)), relative to C2 only.**
  - `𝒢_C2-x ⊊ 𝒢`: WD and WE exhibit elements of `𝒢` that change C2's laws.
  - So time-dependent right freedom (`K_tK_sᴴ` not scalar), and at `|A| ≥ 2` left freedom off the anchored lines, are
    not symmetries of every C2 law.
  - The C2 classes are coarser than the `𝒢_C2-x` classes (5.2).
  - The C2 classes are incomparable with `G` at `|V| ≥ 3`, and inside `G` at `|V| = 2`, `|A| = 1`.
  - No interface-independent gauge classification follows.

## §6. Controls

| Control | Requirement | Result |
|---|---|---|
| K-A | Re-derived cells against B4N; a disagreement halts its item | W0 agrees with B4N D1, D2, D2′, D4. §3 agrees with B4N's `R`/`Q` cells at their witnesses' scopes, and §5.1 with B4N `Sub[C2]`. **One finding:** B4N §3(a) states, under its header scope "fixed anchor `a₀`, `\|V\| ≥ 2`", that C2 is comparable with `G` in neither direction. That claim is false at `\|V\| = 2`, `\|A\| = 1`, where `O_C2-auto ⊆ G` (§3.4). The item was halted and is settled by the hand check written in §3.1. B4N's `Q[C2]` cell is supported only at `\|V\| = 4`, by its witnesses (RHC6 images of TG3). |
| K-B | `R_C` invariant under `𝒢_C` | C0: `𝒢` (§3.1). C1′: §4 (⊇). C2-x: §5.1 (⇐). C1: checked on the subgroup `{L_t` free, `K_t ∈ U(1)·1}`, which multiplies `FG` by `\|κ\|² = 1`; `Sub[C1]` is not posed here: **pass** |
| K-C | Identity family against `H(1)` separated by every `R_C` (as frozen; `\|V\| = 4`, with `H(1)` on `𝒜` and `1` on `C` at `\|A\| ≥ 2`) | `Γ = 1` against `J/4`. This separates `R_C0`; `R_C1`, since `FG` has `Γ` on its diagonal; `R_C1′`, since `e_0` is not in `U(1)·H(1)e_0 = U(1)·½(1,1,1,1)`; and `R_C2`, which contains `R_C0`: **pass** |
| K-D | Same `Γ` for every pair offered about gauge freedom | WA, WA′, `Γ^alt`, WG, WH and WI have equal `Γ_t` for all `t`. Every G⇒O pair is a gauge image: **pass** |
| K-E | Explicit witness; class with orientation; frozen procedure, not X | Every witness is explicit. Classes and orientation are stated per witness. Every procedure is a P-conf or P-coh root with Rd reads, or an H-fac device read for C1′, one of the candidate's own; none uses global reversibility. Finding: the provenance placement "`U₀ = 1`, then constant" is not periodic (§3): **pass** |
| K-F | Directions separate; `twoSidedRelated_iff` direction named | §2 and §3 decide each direction on its own. TSG:839 `mpr` is used in §2.5, §3.1 and §3.2; non-relatedness uses TSG:263 (forward) with TSG:870. No uniqueness or extension result is used as a converse: **pass** |
| K-G | `⊥` kept unnormalized; masses sum to 1 per `j` | W0.4, W0.5, WE and WG checked; the conditioned all-ok statement in §3.5 is labelled: **pass** |
| K-H | ℕ coverage | WA, WA′ and WB–WD are period 2; WH and WI period 3; WE and WG constant from `t = 1`. Every equal-law claim is shown for every pair `s < t` and hence every finite read list: **pass** |
| K-I | Identical procedure | Every comparison changes only `U ↦ gU` or `U ↦ U′`. The two-time witnesses WD and WH use time-dependent `g`: **pass** |

All controls pass. One K-A item halted and was settled in the record.

## §7. Hidden-assumption watch (§A.31)

- **W1 (∀U):** every `Sub` result (§4, §5.1) uses ∀U to choose `U` after `g`, so none of them is a statement about
  OI-realizable lifts.
  - **NEW** [D]: WH shows that the law of one particular lift can be unchanged by some `g ∉ 𝒢_C2`. "Symmetry of all
    laws" and "relation between two given lifts" are different notions, and Own fails because of this difference.
- **W2:** ∀U is used as a quantifier over the lift space only. No step reads it as "sufficient reversible control",
  the condition bare OI does not supply (`main_result` (iii), GeneralCarrier:188).
- **W3 (reset frame):**
  - Condition (ii) of `𝒢_C2-x` at `|A| ≥ 2` comes from the `a₀` reset frame.
  - **NEW** [D]: E[C2]⊆ fails at `|A| ≥ 2` (WG). The relative readback `𝒪₂` determines the law, but the law
    determines `𝒪₂(t,s)` only on columns reachable at `s`. The `𝒪₂` carrier therefore overstates what the complete
    record of C2 fixes.
- **W4:** `a₀` is fixed throughout.
- **W5:** every law is per `j`, and no `prior` is used.
- **W6:** Own[C2-x] (§5.2) examines every representation of the relation explicitly, not one chosen by TSG:826 `mpr`.
- **W7:** the embeddings WA′ and WI were re-checked under the larger left group (TSG:263 at every `|A|`), with zero
  `⊥` mass.
- **W8 (Src′, the branch favourable to native gauge fixing):** under the conditional hypotheses, the fixing that
  H-comp supplies (`𝒢_C2 ⊊ 𝒢`) is real. But no subgroup of `𝒢` has C2's operational classes as its orbits.
  - *Argument.* Suppose a subgroup `H ⊆ 𝒢` has orbits equal to the `O_C2-x` classes. Then `Λ(hU) = Λ(U)` for every
    `h ∈ H` and every `U`, so `H ⊆ 𝒢_C2-x`, and every `H`-orbit lies inside a `∼_C2-x` class.
  - The pairs WH, WI, WA and WA′ are `O_C2-x`-related but not `∼_C2-x`-related (§5.2), so they lie in no common
    `H`-orbit. This contradicts the assumption.
- **W9 (orientation):** every `PPer` claim checks that `Γ` is doubly stochastic, so that either orientation holds.
  WG's `Γ_0` is neither row-stochastic nor `1`.
- **Productivity:** the two NEW items (W1, W3) are stronger than restating B4N or F, and each constrains a candidate
  or exposes an assumption. Both are recorded as assumption-watch markers.

## §8. Results (§9 of the scope, filled in)

Labels follow scope §5: proved, disproved, conditional, unresolved. ★ marks a cell F fixes on its own support. "Not
addressed" marks a cell stopped at the scope boundary (scope §8).

| Model | `\|V\|` | `\|A\|` | Class | G⇒O | O⇒G | Support | Does NOT establish |
|---|---|---|---|---|---|---|---|
| C0 | any | any | all | proved★ | (rows below) | F l. 178; TSG:217, CLG:273 | physical gauge equivalence; native access |
| C0 | 2 | 1 | all | proved★ | proved★ | F ll. 254–261, written out in §3.1 | the `\|A\| ≥ 2` case; physical equivalence |
| C0 | ≥3 | 1 | all (witness outside `PPer`) | proved★ | disproved★: COUNTEREXAMPLE[C0, `\|V\|`≥3, `\|A\|`=1, no reset, same Γ, outside `PPer`] | TG3 (TSG:907, :966); `F₃` (F ll. 244–249; WA) | a native separation |
| C0 | 4 | 1 | `PPer` | proved★ | disproved★: COUNTEREXAMPLE[C0, `\|V\|`=4, `\|A\|`=1, no reset, same Γ, `PPer`] | `Γ^alt` pair (F Q5a, Q5b) | a native separation |
| C0 | 3 | 1 | `PPer` | proved | disproved: COUNTEREXAMPLE[C0, `\|V\|`=3, `\|A\|`=1, no reset, same Γ, `PPer`] | WA [D] | a native separation |
| C0 | ≥5 | 1 | `PPer` | proved | disproved: COUNTEREXAMPLE[C0, `\|V\|`≥5, `\|A\|`=1, no reset, same Γ, `PPer`] | WA with `⊕ 1`; `Γ^alt ⊕ 1` [D] | a native separation |
| C0 | ≥3 | ≥2 | all (witness outside `PPer`) | proved★ | disproved★: COUNTEREXAMPLE[C0, `\|V\|`≥3, `\|A\|`≥2, no reset, same Γ, outside `PPer`] | F ll. 245–249 | a native separation |
| C0 | ≥3 | ≥2 | `PPer` | proved | disproved: COUNTEREXAMPLE[C0, `\|V\|`≥3, `\|A\|`≥2, no reset, same Γ, `PPer`] | WA′ [D] | a native separation |
| C0 | 2 | ≥2 | any | proved | not addressed | F l. 430 undecided; scope §8 | either answer for O⇒G |
| C1 | ≥2 | any | all; `PPer` | disproved: COUNTEREXAMPLE[C1, `\|V\|`≥2, `\|A\|` any, no reset, same Γ, `PPer`] | proved | WB; §2.2 with TSG:839 `mpr` [D] | that P-coh is available |
| C1′ | ≥2 | any | all; `PPer` | disproved: COUNTEREXAMPLE[C1′, `\|V\|`≥2, `\|A\|` any, no reset, same Γ, `PPer`] | proved | WC; §2.3, TSG:84 [D] | that any H-fac device is available |
| C2-auto | 2 | 1 | all; `PPer` | disproved: COUNTEREXAMPLE[C2-auto, `\|V\|`=2, `\|A\|`=1, Rst-auto, same Γ, `PPer`] | proved | WD; `O_C2 ⊆ O_C0` with F ll. 254–261 [D] | that H-comp or Acc₂ is physical |
| C2-auto | ≥3 | 1 | all; `PPer` | disproved: COUNTEREXAMPLE[C2-auto, `\|V\|`≥3, `\|A\|`=1, Rst-auto, same Γ, `PPer`] (WD `⊕ 1`) | disproved: COUNTEREXAMPLE[C2-auto, `\|V\|`≥3, `\|A\|`=1, Rst-auto, same Γ, `PPer`] (WA; `Γ^alt` pair at 4) | WD `⊕ 1`; WA [D] | a native separation |
| C2-ch | 2 | ≥2 | all; `PPer` | disproved: COUNTEREXAMPLE[C2-ch, `\|V\|`=2, `\|A\|`≥2, Rst-ch, same Γ, `PPer`] (WE) | not addressed (owner question, §3.5) | WE [D] | either answer for O⇒G |
| C2-ch | ≥3 | ≥2 | all; `PPer` | disproved: COUNTEREXAMPLE[C2-ch, `\|V\|`≥3, `\|A\|`≥2, Rst-ch, same Γ, `PPer`] (WE `⊕ 1`) | disproved: COUNTEREXAMPLE[C2-ch, `\|V\|`≥3, `\|A\|`≥2, Rst-ch, same Γ, `PPer`] (WA′) | WE `⊕ 1`; WA′ [D] | a native separation |
| C2-sel | 2 | ≥2 | all; `PPer` | disproved: COUNTEREXAMPLE[C2-sel, `\|V\|`=2, `\|A\|`≥2, Rst-sel, same Γ, `PPer`] (WE: root `(ok,⊥)` and all-ok) | not addressed (owner question, §3.5) | WE [D] | either answer for O⇒G |
| C2-sel | ≥3 | ≥2 | all; `PPer` | disproved: COUNTEREXAMPLE[C2-sel, `\|V\|`≥3, `\|A\|`≥2, Rst-sel, same Γ, `PPer`] (WE `⊕ 1`) | disproved: COUNTEREXAMPLE[C2-sel, `\|V\|`≥3, `\|A\|`≥2, Rst-sel, same Γ, `PPer`] (WA′) | WE `⊕ 1`; WA′ [D] | a native separation |

**Equivalence.** Both directions are proved at the same scope only for C0 at `|V| = 2`, `|A| = 1`: there, two-sided
gauge relatedness and complete-record operational equivalence are equivalent (★, on F's support). In every other
addressed cell the two notions differ, and the table records in which direction:
- C1 and C1′ refine `G` strictly: O⇒G holds and G⇒O fails.
- C0 coarsens `G` at `|V| ≥ 3`: G⇒O holds and O⇒G fails.
- C2 is incomparable with `G` at `|V| ≥ 3`, and strictly inside it at `|V| = 2`, `|A| = 1`.

**Further results, outside the owner-direction cells.**
- **E[C], the exact quotients** (§2):
  - `O_C = R_C` for C0, C1, C1′ and C2-auto (both inclusions proved).
  - For C2-ch and C2-sel, `R_C ⇒ O_C` is proved and `O_C ⇒ R_C` is disproved (WG).
- **S1′** (§4): `𝒢_C1′ = {L_t scalar, K_t weak}`.
- **Conditional block** (§5), each CONDITIONAL[H-comp, Acc₂, Rst-x, P-conf] and relative to `𝒢_C2-x`:
  - `𝒢_C2-x` = (i) ∧ (ii) (proved);
  - Own[C2-x] is disproved at every `|V| ≥ 2` in `PPer`;
  - physical supply is a SOURCING-GAP.

**Conditional readings (scope §4(ii)).** Each proved result above is a statement about the stated mathematical
objects. Read as a statement about OI lifts, it carries the conditions below. A disproved cell is a counterexample to
a universal statement about the same objects; read physically, it carries its row's tuple as well.

| Result | Reading |
|---|---|
| C0: G⇒O; O⇒G at `\|V\| = 2`, `\|A\| = 1`; E[C0]⊇, E[C0]⊆ | CONDITIONAL[C0 = (P-conf, Acc₁, Rd), ∀U, fixed `a₀`, (r1)] |
| C1: O⇒G; E[C1]⊇, E[C1]⊆ | CONDITIONAL[C1 = (P-coh, Acc₁, Rd), ∀U, fixed `a₀`, (r1)] |
| C1′: O⇒G; E[C1′]⊆; S1′ | CONDITIONAL[C1′ = (P-conf, Acc₁, H-fac with all devices), ∀U, fixed `a₀`, (r1), (r3) including `dim H_d = 1`] |
| C1′: E[C1′]⊇ | CONDITIONAL[C1′ = (P-conf, Acc₁, H-fac), ∀U, fixed `a₀`, (r1)]; it holds device by device |
| C2-auto: O⇒G at `\|V\| = 2`; E[C2-auto]⊇, E[C2-auto]⊆ | CONDITIONAL[C2-auto = (P-conf, Acc₂, Rd, H-comp, Rst-auto), ∀U, fixed `a₀`] |
| C2-ch: E[C2-ch]⊇ | CONDITIONAL[C2-ch = (P-conf, Acc₂, Rd, H-comp, Rst-ch), ∀U, fixed `a₀`] |
| C2-sel: E[C2-sel]⊇ | CONDITIONAL[C2-sel = (P-conf, Acc₂, Rd, H-comp, Rst-sel), ∀U, fixed `a₀`, (r2)] |
| §5: `𝒢_C2-x` = (i) ∧ (ii); Own[C2-x] disproved | CONDITIONAL[C2-x tuple, ∀U, fixed `a₀`, (r2) for x = sel], relative to `𝒢_C2-x` |

**SOURCING-GAP list, per candidate.** None of the following is physically supplied by anything in this record.
- **C0:** P-conf (`|j,a₀⟩` at the root, for each `j`); Acc₁; Rd.
- **C1:** P-coh (`ρ ⊗ |a₀⟩⟨a₀|` for every density matrix `ρ`); Acc₁; Rd.
- **C1′:** P-conf; Acc₁; H-fac with all devices (every `H_d`, unitary `G`, state `ψ` and configuration-diagonal cell
  partition).
- **C2-auto:** P-conf; Acc₂ (all records retained jointly); Rd; H-comp (root clause, and `U_tU_sᴴ` between reads);
  Rst-auto.
- **C2-ch:** as C2-auto, with Rst-ch (the ancilla-replacement channel) in place of Rst-auto.
- **C2-sel:** as C2-auto, with Rst-sel (the `|a₀⟩⟨a₀|` test, `⊥` retained) in place of Rst-auto.
- **Common to all:** which lift is OI's; the anchor `a₀`; which candidate, if any, is native.

## §9. Premise ledger (§A.42 item 8) and limits

**Premise ledger**
- **Support on `main`:** every [K] line cited, read at `b606ee41`.
- **Support off `main` (a gap until F lands):** F (`88c175c3`), used at:
  - ll. 62–67: the H-fac interface and NI, used for C1′;
  - l. 178: C0 G⇒O;
  - ll. 137–144 and 351–362: `Γ^alt`, Q5a, Q5b;
  - ll. 244–249: the `F₃` placement, re-derived here as WA and WA′;
  - ll. 254–261: `Fib = G` at `|V| = 2`, written out in §3.1;
  - l. 430: the undecided item.
- **F lines not used:** F's Lemma HS (l. 188) and the results that inherit it (Q1⇒, Q1c(⇒), DC's
  "R[C] ⇒ O_C ⊇ Fib") are not used. No class-F←c premise enters this record.
- **Provenance only:**
  - #1033 c.6567713723 and c.6567723333 (B4N and its review), used as cross-check (K-A);
  - c.6567694252 (the AR definition);
  - c.6652903587, c.6653013695, c.6653677971 and c.6652148478 (rulings, review and authorization);
  - #914 c.6563412926 and c.6558834119.
  - None supports a result.
- **Not used as support:** Main:646 and TSG:49–50 (context).

**Does NOT establish.**
- Any physical gauge equivalence or inequivalence.
- Any native observer or native access model.
- Which candidate, if any, OI physically supplies (SOURCING-GAP).
- Any statement about restricted classes of lifts or about OI-realizable lifts (W1).
- Any two-time H-fac device class.
- The cells marked not addressed.
- A global gauge classification.

Nothing here is promoted or propagated. Every [D] result is unreviewed.

**Proposals (not pursued; separate scope and authorization needed).**
- A reachability-restricted `R_C2` for `|A| ≥ 2` (§2.5).
- The `|V| = 2`, `|A| ≥ 2` cells (F l. 430).
