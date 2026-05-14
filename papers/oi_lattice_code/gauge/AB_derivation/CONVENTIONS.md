# Γ_3 module — Conventions

Session: 2026-04-22 (continuation). Approach (A): G_0 = 1/D(k)·𝟙_4 propagator,
composite (D†D)^(n) vertex insertions, bare D^(n) rules from STEP1c_DERIVATION §2.

## Lattice

- 4-dim Euclidean hypercubic, periodic BC, N sites per direction.
- Momenta: k_μ = 2π·n_μ/N, n_μ ∈ {0, 1, ..., N-1}.
- Integration: (1/N^4)·Σ_k ≈ ∫ d^4k/(2π)^4 with dk = 2π/N per direction, so
  measure factor is dk4 = (2π/N)^4/(2π)^4 = 1/N^4 — a pure average over BZ sites.
- Convention matches step1c_crosscheck.py verbatim.

## Dirac

- 4×4 Hermitian Γ^μ with {Γ^μ, Γ^ν} = 2δ^{μν}·𝟙_4. Euclidean.
- Use a concrete representation (chiral/Dirac basis) for numerical evaluation;
  the representation doesn't matter for traces.

## Fermion bilinears (free)

- D_0(k)      = m·𝟙_4 + i·Γ^α·sin(k_α)
- D_0^†(k)    = m·𝟙_4 − i·Γ^α·sin(k_α)
- D_0^†·D_0   = (m² + Σ_α sin²(k_α))·𝟙_4 ≡ D(k)·𝟙_4
- G_0(k)      = 1/D(k) · 𝟙_4     (propagator in Approach A)

## Gauge / color

- U_μ(x) = exp(ig_0·A_μ(x+μ̂/2)), mid-link convention.
- A_μ = A_μ^a·T^a, Hermitian generators T^a, Tr[T^a T^b] = T(R)·δ^{ab}.
- All external A-legs carry INCOMING momentum convention:
    A^a_μ(p) is the amplitude for a gauge line of momentum p flowing INTO the vertex.
- Fermion loop: running momentum k. At a vertex absorbing incoming external
  momentum Δp, fermion goes k → k+Δp.

## Bare D^(n) vertices (momentum space)

All vertices have legs on a single lattice link (direction μ), enforced by
δ-functions on Lorentz indices. Fermion momentum `k` is the "pre-vertex"
momentum; external legs add in order; P = sum of all external incoming momenta.

- D^(1)_{μ,a}(k; p) = i·g_0 · Γ^μ · cos((k + p/2)_μ) · T^a

- D^(2)_{μν,ab}(k; p, q)
    = −(i·g_0²/2) · δ_{μν} · Γ^μ · sin((k + (p+q)/2)_μ) · {T^a, T^b}/2

- D^(3)_{μνρ,abc}(k; p, q, r)
    = −(i·g_0³/6) · δ_{μν}·δ_{μρ} · Γ^μ · cos((k + (p+q+r)/2)_μ)
      · (1/3!) · Σ_{σ∈S_3} T^{σ(a)} T^{σ(b)} T^{σ(c)}

Hermitian-conjugate rule (for symmetrized color): (D^(n))^† = −D^(n), for all n ≥ 1.

## Composite (D†D)^(n) insertions

These are the vertices we actually use (Approach A). They insert INTO the G_0
propagator chain. Arguments are external momenta carried into the composite.

(D†D)^(1)_{μ,a}(k ; p) = D_0^†(k+p) · D^(1)_{μ,a}(k; p) + (D^(1)_{μ,a})^†(k+p → k) · D_0(k)
  Using (D^(n))^† = −D^(n) pointwise:
  = D_0^†(k+p) · D^(1)_{μ,a}(k; p) − D^(1)_{μ,a}(k; p) · D_0(k)

For momentum-space evaluation, care with "at which momentum each D is evaluated":
- D^(1)_{μ,a}(k; p): fermion enters at k, exits at k+p. Vertex cos factor at (k+p/2).
- The left D_0^† is at outgoing momentum (k+p); the right D_0 is at incoming (k).

(D†D)^(2)_{μν,ab}(k; p, q)  [two external legs with momenta p, q on same link or two links]

Two distinct sub-topologies at the composite level:
  (i)  Both legs on the SAME bare vertex (D^(2)):
         D_0^†(k+P) · D^(2)_{μν,ab}(k; p, q) − D^(2)_{μν,ab}(k; p, q) · D_0(k)
       (where P = p + q).
  (ii) One leg each on two bare D^(1)'s:
         − D^(1)_{μ,a}(k+q; p) · D^(1)_{ν,b}(k; q)
       (symmetrized over leg ordering: also +(p ↔ q, μ ↔ ν, a ↔ b) if both
        permutations aren't generated automatically by momentum labeling).

Per §4 of STEP1c_DERIVATION:
  (D†D)^(2) = D_0^† D^(2) − D^(1) D^(1) − D^(2) D_0

For distinct labeled external legs (p,μ,a) and (q,ν,b), this is:
  D_0^†(k+P)·D^(2)_{μν,ab}(k; p,q)  −  D^(1)_{μ,a}(k+q; p)·D^(1)_{ν,b}(k; q)  −  D^(2)_{μν,ab}(k; p,q)·D_0(k)

Note: D^(1) D^(1) already produces the correct leg labeling when we specify momentum flow;
the other ordering (q before p) would appear if we had a separate (D†D)^(2) contribution
from p↔q. But (D†D)^(2) is symmetric in its external legs by construction of the n=2
coefficient in the Taylor expansion, so there is only ONE (D†D)^(2)(p,q); the bare
pieces inside are what they are.

(D†D)^(3)_{μνρ,abc}(k; p, q, r) from §4:
  = D_0^†(k+P)·D^(3) − D^(1)·D^(2) − D^(2)·D^(1) − D^(3)·D_0
  (P = p+q+r)

For labeled external legs (p,μ,a), (q,ν,b), (r,ρ,c), the expansion sums over the
three ways to put one leg on D^(1) and two on D^(2) (and their D^(1)D^(2) vs D^(2)D^(1)
orderings, which are distinct because the intermediate D_0's involve different momenta).

## S_eff cubic-in-A: three topologies summed

From −N_f·Tr ln(1 + G_0·Δ) = −N_f·[Tr(G_0·Δ) − (1/2)Tr(G_0·Δ)^2 + (1/3)Tr(G_0·Δ)^3 − ...]:

At cubic order in A (picking cubic pieces of each term):

**T_tri  (triple-tadpole):**  −N_f · Tr[G_0 · (D†D)^(3)]
**T_dtad (double-tadpole):** +N_f · Tr[G_0 · (D†D)^(1) · G_0 · (D†D)^(2)]
**T_tri3 (triangle):**       −(N_f/3) · Tr[G_0 · (D†D)^(1) · G_0 · (D†D)^(1) · G_0 · (D†D)^(1)]

Sum over permutations of (p_i, μ_i, a_i) across labeled positions is built into each
term by summing over which external momentum(a) sit on which composite vertex:

- T_tri: (D†D)^(3) carries all 3 legs → no extra permutation sum.
- T_dtad: 3 choices for which leg is on (D†D)^(1); other 2 on (D†D)^(2) (whose color is
  already symmetrized).
- T_tri3: 2 inequivalent cyclic orderings (clockwise, counterclockwise) after fixing
  (D†D)^(1)'s at three vertex positions.

## Γ_3^{μνρ,abc}(p_1, p_2, p_3)

Defined via:
  S_eff[A] ⊃ (1/3!) ∫_{p_1+p_2+p_3=0} A^{a_1}_{μ_1}(p_1) A^{a_2}_{μ_2}(p_2) A^{a_3}_{μ_3}(p_3)
              × Γ_3^{μ_1μ_2μ_3, a_1a_2a_3}(p_1, p_2, p_3)

So Γ_3 is (3!) × (sum of topologies) with external momenta (p_1,p_2,p_3), fully
symmetrized over legs. Conversely: sum of topologies above = (1/3!) Γ_3 with the
leg-permutations already summed, so

  Γ_3(p_1, p_2, p_3) = 3! · [T_tri + T_dtad + T_tri3]_{cubic coeff, permutations included}

— but practically the 1/3! cancels the S_3 permutation sum, and I will just compute
Γ_3 directly as "the piece multiplying A·A·A in S_eff with the combinatoric factors
making Γ_3 Bose-symmetric by construction."

## Sanity-check targets (this session)

1. d^{abc} part of Γ_3 is nonzero; f^{abc} part vanishes (Furry).
2. Γ_3(p_1, p_2, p_3 = 0) has specific structure relating to ∂Π(p)/∂p.
3. Γ_3 is Bose-symmetric: invariant under simultaneous (p_i, μ_i, a_i) permutations.
4. Γ_3 → 0 as all p_i → 0 with smallness O(p^3).
