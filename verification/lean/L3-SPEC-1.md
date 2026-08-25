# L3-SPEC-1 — statement specification: the SM structural-chain head + near-free items (b406; authored on gate-pass)

Same protocol as L2-SPEC: statements proposed-frozen for owner review; no `.lean` ahead of
the L1 gate; acceptance mirror `l3_chain_mirror_probe.py` (L3M1–L3M5, green). Target file on
gate-pass + sign-off: `OI_L3_Chain.lean` (Mathlib for matrices/Fintype; several items are
core-feasible).

## M1 — Theorem 1a (SM:238), two statements

**M1.1 (projected-evolution identity).** For square matrices over a commutative ring with
`P` idempotent, `Q = 1 − P`, `A = PUP, B = PUQ, C = QUP, D = QUQ`, and `xₜ₊₁ = U xₜ`:
`P xₜ₊₁ = A (P xₜ) + ∑_{s<t} B D^{t−1−s} C (P x_s) + B Dᵗ (Q x₀)` — by induction on the
iterated Q-equation, exactly the manuscript's displayed identity (mirror: exact through
t = 6 vs direct evolution).

**M1.2 (kernel equivariance).** If additionally `[U,R] = [P,R] = 0` then `[B Dᵐ C, R] = 0`
for every m. Necessity is witnessed: a non-equivariant `P` breaks it (mirror control).

## M2 — Theorem 2 (SM:282), the factorization with the convention pinned

**M2.1 (integer core).** On `(ZMod L)^d` sites with shifts `T_μ`, phases
`η_μ(x) = (−1)^{∑_{ν<μ} x_ν}`, and `2·D_st := ∑_μ η_μ (T_μ − T_μ⁻¹)`:
`(2 D_st)² = ∑_μ (T_μ − T_μ⁻¹)²` — an exact integer matrix identity (cross terms cancel by
η-anticommutation; mirror: int64-exact at d = 3, 4, L = 4).

**M2.2 (the manuscript form).** With `□_lat := −∑_μ (T_μ − T_μ⁻¹)²` (positive-Laplacian
convention): `D_st² = −¼ □_lat`. *Faithfulness note:* SM:282 states the identity without
displaying the □_lat sign convention; the spec pins it constructively — the identity is
exact in this convention, and only in it. Suggested future-version wording: display the
convention beside the theorem (register: minor, wording).

**M2.3 (chirality of the massless operator).** With `ε(x) = (−1)^{∑_μ x_μ}`:
`D_st ε + ε D_st = 0` exactly.

**M2.4 (Theorem-1 dispersion leg).** `cos ω = (1/d) ∑_j cos k_j` as an exact identity of
the plane-wave substitution on torus modes (the KG *limit* stays Tier 2; the exact
dispersion is Tier 1).

## M3 — Theorem 3 (SM:296), the equivalence at operator level

**M3.1.** For `D = D_st + m·ε + p₀·1` (the general center-carrying staggered operator):
`{D, ε} = 2m·1 + 2p₀·ε` exactly. Hence **center independence of D_st's diagonal
(m = p₀ = 0) ⟺ exact ε-chirality** — the manuscript's equivalence, with its two-line proof
sketch completed at operator level. *Scope, per the SM Remark:* the statement is about
`D_st`'s diagonal, NOT the second-order update's self-term `C = 2(1−d)` (which is the
Laplacian diagonal and mass-innocent); the Lean statement encodes this by construction.

**M3.2 (the squaring claim).** Given M2.3: `(D_st + m·ε)² = D_st² + m²·1` — the
manuscript's "squares to −¼(□ − 4m²)" in the pinned convention.

## G1 — GR:64, the finite detailed-balance lemma

**G1.1.** On a finite connected transition graph with rates satisfying
`W_{m→n}/W_{n→m} = e^{−τ(ω_n−ω_m)}` on every edge, the stationary distribution of the
master generator is `p ∝ e^{−τω}` (unique up to scale). **G1.2 (necessity).** On a
disconnected graph the stationary space is per-component Gibbs with independent constants —
witnessed non-global-Gibbs stationary state (mirror control). Connectedness is
load-bearing, exactly as the GR text says.

## S9 + C1a — near-free instances

**S9.1.** `k·(−2·zt·ω) + ω·(2·zs·k) = 2·ω·k·(zs − zt)` over any commutative ring —
`by ring`; the b401 quadratic boost-Ward residual (mirror: exact over ℚ).
**C1a.1.** `dim Sym²(ℝ³)^{B₃} = 1` with fixed vector δ — Corollary 1a's algebraic core as
a direct instance of L2's B1.0 machinery (mirror: 48-element generation, dim 1): quadratic
anisotropy is symmetry-forbidden, the manuscript's proof line kernel-checkable for free
once L2 lands.

## Faithfulness findings (this round)

(F1) M2's □_lat convention: pinned constructively; minor wording register item proposed.
(F2) M3's proof sketch: completed at operator level with no correction needed; the
Remark's C = 2(1−d) scope is encoded in the statement rather than left to prose.

## Review protocol

As L2-SPEC: owner sign-off (or line edits) freezes statements; `OI_L3_Chain.lean` is then
authored here with this mirror as acceptance instrument and the kernel run as gate.
