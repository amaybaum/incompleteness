# BSEL-2 unit B4′: two-sided gauge relatedness against complete-record operational equivalence (paper record)

**Status: WIP / UNVERIFIED.** Paper-only, written by the designated BSEL-2 writer (#1033 c.6653013695). Not reviewed.
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
