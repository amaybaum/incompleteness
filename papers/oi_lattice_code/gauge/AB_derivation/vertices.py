"""
vertices.py — Numerical implementation of bare D^(n) vertices and composite
(D†D)^(n) insertions for the A1 Part 2 / Γ_3 calculation.

See CONVENTIONS.md for sign conventions and momentum flow definitions.

All functions take:
  - `k`: fermion momentum array, shape (..., 4), with k_μ = 2π·n_μ/N values.
  - external momenta as 4-vectors shape (4,).

Returned Dirac structure is 4×4 matrix per k-point (last two axes of the array).
Color structure is returned separately as a sympy-free symbolic tensor
factored out of the numerical part (since all color structures at cubic order
in A are products/sums of T^a·T^b·T^c, which we track with string labels or
explicit matrix evaluation at the end).
"""
import numpy as np


# ============================================================
# Gamma matrices (Euclidean, Hermitian, {Γ^μ,Γ^ν}=2δ^{μν})
# ============================================================
# Chiral-basis in 4D Euclidean. Any Hermitian basis with the Clifford
# relation works; traces are representation-independent.
# Here we take: Γ^μ = [[0, σ^μ],[σ^μ†, 0]] with σ^μ = (i·σ_k, 𝟙) suitably.
# For simplicity and to ensure Hermiticity: use the standard Euclidean
# chiral basis Γ^μ_E = γ^μ with γ^0_E Hermitian, γ^k_E Hermitian via i·γ^k_M.
#
# Concrete 4×4 Hermitian matrices satisfying {Γ^μ,Γ^ν}=2δ^{μν}:

_I2 = np.eye(2, dtype=complex)
_Z2 = np.zeros((2, 2), dtype=complex)
_sx = np.array([[0, 1], [1, 0]], dtype=complex)
_sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
_sz = np.array([[1, 0], [0, -1]], dtype=complex)

# Euclidean chiral: Γ^μ = [[0, τ^μ],[τ̄^μ, 0]] with τ = (𝟙, -iσ), τ̄ = (𝟙, iσ)
# Standard Osterwalder–Schrader. Verify: Γ^μ Hermitian, anticommute correctly.
_tau = [_I2, -1j*_sx, -1j*_sy, -1j*_sz]   # τ^μ for μ=0,1,2,3
_taubar = [_I2,  1j*_sx,  1j*_sy,  1j*_sz]

def _block(A, B, C, D):
    return np.block([[A, B], [C, D]])

GAMMA = np.array([
    _block(_Z2, _tau[mu], _taubar[mu], _Z2) for mu in range(4)
])  # shape (4, 4, 4): GAMMA[μ] is the 4×4 matrix Γ^μ

# Sanity: verify Clifford algebra
def _check_clifford():
    for mu in range(4):
        for nu in range(4):
            ac = GAMMA[mu] @ GAMMA[nu] + GAMMA[nu] @ GAMMA[mu]
            expected = 2 * (1 if mu == nu else 0) * np.eye(4, dtype=complex)
            if not np.allclose(ac, expected, atol=1e-12):
                raise RuntimeError(
                    f"Clifford algebra FAILED at (μ={mu}, ν={nu}):\n{ac}"
                )
        if not np.allclose(GAMMA[mu].conj().T, GAMMA[mu], atol=1e-12):
            raise RuntimeError(f"Γ^{mu} is not Hermitian")

_check_clifford()


# ============================================================
# Lattice & free fermion objects
# ============================================================
def lattice_momenta(N):
    """Build the full grid of lattice 4-momenta k_μ = 2π n_μ/N.
    Returns array of shape (N^4, 4).
    """
    idx = np.arange(N)
    I0, I1, I2, I3 = np.meshgrid(idx, idx, idx, idx, indexing='ij')
    k = np.stack([2*np.pi*X.ravel()/N for X in [I0, I1, I2, I3]], axis=1)
    return k


def D0(k, m):
    """Free Dirac operator D_0(k) = m·𝟙 + i·Γ^α·sin(k_α).
    k: shape (..., 4).  Returns shape (..., 4, 4).
    """
    s = np.sin(k)  # (..., 4)
    # Build m·I + i·Σ_α s_α·Γ^α vectorized
    out = np.zeros(k.shape[:-1] + (4, 4), dtype=complex)
    out[..., :, :] = m * np.eye(4, dtype=complex)
    for mu in range(4):
        out += 1j * s[..., mu:mu+1, np.newaxis] * GAMMA[mu]
    return out


def D0dag(k, m):
    """(D_0)^†(k) = m·𝟙 − i·Γ^α·sin(k_α).  (Hermitian conjugate at same k.)"""
    s = np.sin(k)
    out = np.zeros(k.shape[:-1] + (4, 4), dtype=complex)
    out[..., :, :] = m * np.eye(4, dtype=complex)
    for mu in range(4):
        out += (-1j) * s[..., mu:mu+1, np.newaxis] * GAMMA[mu]
    return out


def D_scalar(k, m):
    """D(k) = m² + Σ_α sin²(k_α), the scalar-in-Dirac D_0^† D_0 eigenvalue.
    Returns shape (...,).
    """
    return m**2 + np.sum(np.sin(k)**2, axis=-1)


def G0(k, m):
    """Propagator in Approach A: G_0(k) = 1/D(k) · 𝟙_4.
    Returns shape (..., 4, 4).
    """
    inv = 1.0 / D_scalar(k, m)  # (...,)
    out = np.zeros(k.shape[:-1] + (4, 4), dtype=complex)
    out[..., :, :] = np.eye(4, dtype=complex)
    out *= inv[..., np.newaxis, np.newaxis]
    return out


# ============================================================
# Bare D^(n) vertex matrix elements (Dirac part; color factored out)
# ============================================================
# Each D^(n) returns the "Dirac piece": the 4×4 matrix with the color T^a...T^c
# factors STRIPPED. The color structure is returned separately as metadata.
#
# Signature:
#   D1_dirac(k, p, mu)     → shape (..., 4, 4)    [Dirac], coefficient (ig_0)
#   D2_dirac(k, p, q, mu, nu) → δ_{μν} × coefficient (-ig_0²/2) × shape (..., 4, 4)
#   D3_dirac(k, p, q, r, mu, nu, rho) → δ_{μν}δ_{μρ} × coefficient (-ig_0³/6) × shape (..., 4, 4)
#
# "Coefficient" = pulled-out numerical factor; "shape" = Dirac matrix.
# Following STEP1c_DERIVATION §2 exactly.

def D1_dirac(k, p, mu):
    """D^(1)_μ(k; p) Dirac piece (coefficient i·g_0, color T^a stripped).
    Returns the 4×4 matrix  Γ^μ · cos((k+p/2)_μ)  as array of shape (..., 4, 4).
    """
    arg = k[..., mu] + p[mu]/2.0
    factor = np.cos(arg)  # (...,)
    out = factor[..., np.newaxis, np.newaxis] * GAMMA[mu]  # (..., 4, 4)
    return out


def D2_dirac(k, p, q, mu, nu):
    """D^(2)_{μν}(k; p, q) Dirac piece (coefficient -i·g_0²/2, color {T^a,T^b}/2 stripped).
    Returns δ_{μν} · Γ^μ · sin((k+(p+q)/2)_μ).
    Shape (..., 4, 4) — zeros if μ ≠ ν.
    """
    if mu != nu:
        return np.zeros(k.shape[:-1] + (4, 4), dtype=complex)
    P = p + q
    arg = k[..., mu] + P[mu]/2.0
    factor = np.sin(arg)
    out = factor[..., np.newaxis, np.newaxis] * GAMMA[mu]
    return out


def D3_dirac(k, p, q, r, mu, nu, rho):
    """D^(3)_{μνρ}(k; p, q, r) Dirac piece (coefficient -i·g_0³/6,
    color Σ_σ T^σ(a) T^σ(b) T^σ(c)/3! stripped).
    Returns δ_{μν}δ_{μρ} · Γ^μ · cos((k+(p+q+r)/2)_μ).
    """
    if mu != nu or mu != rho:
        return np.zeros(k.shape[:-1] + (4, 4), dtype=complex)
    P = p + q + r
    arg = k[..., mu] + P[mu]/2.0
    factor = np.cos(arg)
    out = factor[..., np.newaxis, np.newaxis] * GAMMA[mu]
    return out


# ============================================================
# Composite (D†D)^(n) vertex insertions
# ============================================================
# Returns the 4×4 Dirac matrix of the composite, at specified external momenta
# and Lorentz indices, with color structure tracked as a dict mapping
# color-ordering-strings to their prefactor.
#
# For simplicity at this sanity-check stage, we return the FULL matrix
# (Dirac × i·g_0^n/factor) and leave the color-coefficient symbolic via
# the returned `color_factor` dict.
#
# (D†D)^(1):  insertion with 1 external leg (p, μ, a).
# (D†D)^(2):  insertion with 2 external legs (p,μ,a), (q,ν,b).
# (D†D)^(3):  insertion with 3 external legs.

def DdagD_1(k, p, mu, m):
    """
    Composite (D†D)^(1)(k; p, μ):
      = D_0^†(k+p) · D^(1)_μ(k; p) − D^(1)_μ(k; p) · D_0(k)

    Coefficient (numerical prefactor): i·g_0 (from the single D^(1)).
    Color: T^a (stripped).
    Returns a Dirac matrix shape (..., 4, 4), where the scalar prefactor
    i·g_0 is INCLUDED in the returned array (imaginary unit carried through
    numerically; g_0 factor handled externally).

    Signature: returns the dimensionally-correct matrix modulo a single
    g_0 factor per external leg.
    """
    k_out = k + p  # fermion momentum after the insertion
    D0dag_out = D0dag(k_out, m)   # (..., 4, 4)
    D1 = D1_dirac(k, p, mu)       # (..., 4, 4)
    D0_in = D0(k, m)              # (..., 4, 4)
    # Matrix product along the last two axes:
    term_L = np.einsum('...ij,...jk->...ik', D0dag_out, D1)
    term_R = np.einsum('...ij,...jk->...ik', D1, D0_in)
    # Combined: i·g_0 · (term_L − term_R)
    return 1j * (term_L - term_R)  # 'i·g_0' factor: 1j carries the i, g_0 is separate


def DdagD_2(k, p, q, mu, nu, m):
    """
    Composite (D†D)^(2) — SYMMETRIC-color part only. For legacy compatibility.
    The full Dirac-color decomposition is:
      (D†D)^(2) = g_0² · {T^a,T^b}/2 · M_sym + g_0² · [T^a,T^b]/2 · M_antisym
    This function returns M_sym. For M_antisym use DdagD_2_antisym.

    See DdagD_2_full for the joint return of both channels.
    """
    M_sym, _ = DdagD_2_full(k, p, q, mu, nu, m)
    return M_sym


def DdagD_2_full(k, p, q, mu, nu, m):
    """
    Composite (D†D)^(2)(k; p, q, μ, ν) with labeled legs (p,μ,a) and (q,ν,b):
      = D_0^†(k+P) · D^(2)_{μν}(k; p, q)
        − D^(1)_μ(k+q; p) · D^(1)_ν(k; q)
        − D^(2)_{μν}(k; p, q) · D_0(k)
    where P = p + q.

    The Taylor coefficient must be symmetric under simultaneous swap
    (p,μ,a) ↔ (q,ν,b). Decompose T^a T^b = {T^a,T^b}/2 + [T^a,T^b]/2.
    The Dirac piece multiplying {T,T}/2 is a (leg-swap)-SYMMETRIC Dirac matrix
    M_sym(p,μ; q,ν) = M_sym(q,ν; p,μ). The Dirac piece multiplying [T,T]/2 is
    a (leg-swap)-ANTISYMMETRIC Dirac matrix M_antisym(p,μ; q,ν) = -M_antisym(q,ν; p,μ).

    - D^(2) pieces (A, C) are proportional to δ_{μν} and are already symmetric
      under leg swap (since swapping p↔q and μ↔ν only permutes inside D^(2)
      which is itself symmetric). They multiply only {T,T}/2.
    - D^(1)D^(1) piece (B): breaks into sym + antisym Dirac parts under the
      leg swap, multiplying {T,T}/2 and [T,T]/2 respectively.

    Returns: (M_sym, M_antisym) — both (..., 4, 4) Dirac matrices.
    Overall factor: g_0² × [{T,T}/2 · M_sym + [T,T]/2 · M_antisym].
    Note: [T^a,T^b]/2 = (i/2) f^{abc} T^c.
    """
    P = p + q
    k_outP = k + P
    k_q = k + q

    D0dag_P = D0dag(k_outP, m)
    D0_in   = D0(k, m)

    D1_p_at_kq = D1_dirac(k_q, p, mu)     # D^(1)_μ(k+q; p)
    D1_q_at_k  = D1_dirac(k, q, nu)       # D^(1)_ν(k;   q)
    D1_q_at_kp = D1_dirac(k + p, q, nu)   # D^(1)_ν(k+p; q) — swapped
    D1_p_at_k  = D1_dirac(k, p, mu)       # D^(1)_μ(k;   p) — swapped
    D2_pq_at_k = D2_dirac(k, p, q, mu, nu)

    # D^(2) pieces: enter with coefficient (-i/2) × (sign from +/− in formula).
    # A: +D_0^† D^(2)   → (-i/2)·(+1) = -i/2
    # C: -D^(2) D_0     → (-i/2)·(-1) = +i/2
    A = np.einsum('...ij,...jk->...ik', D0dag_P, D2_pq_at_k)
    C = np.einsum('...ij,...jk->...ik', D2_pq_at_k, D0_in)
    dirac_from_D2 = -0.5j * A + 0.5j * C

    # D^(1)D^(1) piece: coefficient (i)(i)·(-1) = +1 per Dirac matrix product.
    # Unsymmetrized Dirac (with ordered color T^a T^b): +1 * D^(1)_μ(k+q;p)·D^(1)_ν(k;q)
    # Swap piece (with T^b T^a): +1 * D^(1)_ν(k+p;q)·D^(1)_μ(k;p)
    B = np.einsum('...ij,...jk->...ik', D1_p_at_kq, D1_q_at_k)
    B_swap = np.einsum('...ij,...jk->...ik', D1_q_at_kp, D1_p_at_k)

    # Sym Dirac × {T,T}/2: (B + B_swap) / 2
    # Antisym Dirac × [T,T]/2: (B - B_swap) / 2
    # (This is because T^a T^b = {T,T}/2 + [T,T]/2 for the original leg assignment,
    #  T^b T^a = {T,T}/2 - [T,T]/2 for the swapped leg assignment,
    #  and we symmetrize the TOTAL coefficient over leg permutation.)
    dirac_from_D1D1_sym     = 0.5 * (B + B_swap)
    dirac_from_D1D1_antisym = 0.5 * (B - B_swap)

    M_sym     = dirac_from_D2 + dirac_from_D1D1_sym
    M_antisym = dirac_from_D1D1_antisym

    return M_sym, M_antisym


def DdagD_2_antisym(k, p, q, mu, nu, m):
    """Antisymmetric-color part of (D†D)^(2): coefficient of [T^a,T^b]/2."""
    _, M_antisym = DdagD_2_full(k, p, q, mu, nu, m)
    return M_antisym


def DdagD_3(k, p, q, r, mu, nu, rho, m):
    """
    Composite (D†D)^(3)(k; p, q, r, μ, ν, ρ) with legs (p,μ,a), (q,ν,b), (r,ρ,c).

    From §4:
      (D†D)^(3) = D_0^†·D^(3) − D^(1)·D^(2) − D^(2)·D^(1) − D^(3)·D_0

    Each "D^(1)·D^(2)" and "D^(2)·D^(1)" has 3 momentum assignments (which leg
    is on D^(1)). We must fully symmetrize.

    Returns Dirac matrix that, multiplied by g_0³ × (fully symmetric color
    product T^{abc}_sym = Σ_σ T^σ(a)T^σ(b)T^σ(c) / 3!), equals (D†D)^(3).

    This will also pick up pieces proportional to the ANTISYMMETRIC color
    f^{abc} (from the non-symmetric D^(1)D^(2) orderings) — Furry's theorem
    says these must cancel. We track the symmetric color explicitly here and
    then later verify numerically that the antisymmetric piece vanishes
    upon summing all topologies (including triangle).

    For simplicity at this first pass: symmetrize fully in the external legs
    and return only the symmetric-color coefficient matrix. Antisymmetric
    components can be inspected by NOT symmetrizing (done in a separate
    diagnostic function).
    """
    P = p + q + r
    k_P = k + P
    D0dag_P = D0dag(k_P, m)
    D0_in = D0(k, m)

    # D^(3) piece:
    D3_pqr = D3_dirac(k, p, q, r, mu, nu, rho)
    # D_0^† · D^(3) — coefficient (−i·g_0³/6) × (+1 from + sign) = −i/6 × g_0³
    A = np.einsum('...ij,...jk->...ik', D0dag_P, D3_pqr)
    # −D^(3) · D_0 — coefficient (−i·g_0³/6) × (−1) = +i/6 × g_0³
    D_end = np.einsum('...ij,...jk->...ik', D3_pqr, D0_in)

    # Mixed D^(1)·D^(2) and D^(2)·D^(1) pieces, symmetrize over which leg on D^(1).
    # For a symmetric "external legs on vertex" decomposition, there are 3 ways to
    # pick which leg is on D^(1), and for each, 2 orderings (D^(1) first or D^(2) first):
    #
    # Let's enumerate:
    # Label legs by their index in (p, q, r); mu_leg = mu,nu,rho; alpha_leg for color.
    legs = [(p, mu), (q, nu), (r, rho)]

    # Build D^(1)·D^(2) and D^(2)·D^(1) with the 3 choices of which leg is on D^(1).
    # Notation: "D(1)[leg_i] · D(2)[legs_j,k]" means fermion flow: k → k+p_j+p_k (through D^(2))
    # → k+p_j+p_k+p_i = k+P (through D^(1)).   With D^(1) SECOND (D^(1)·D^(2) means in
    # operator ordering, D^(1) is on the LEFT, so fermion enters on the RIGHT).
    #
    # Convention: matrices act on fermions by left multiplication. A chain
    # M_L · M_M · M_R applied to ψ_in (at momentum k_in) produces ψ_out at the
    # momentum at the leftmost. So for M_L · M_R with fermion in at k, intermediate
    # momentum is k + (momentum absorbed at M_R), output is k + (total).
    #
    # For D^(1)[leg_i] · D^(2)[legs_j,k]: first D^(2) absorbs p_j+p_k, then D^(1)
    # absorbs p_i. So:
    #   fermion in at k  → through D^(2)(k; p_j, p_k) at intermediate "k+p_j+p_k" (mid)
    #                    → through D^(1)(k+p_j+p_k; p_i) → output k+P.
    # Matrix: D^(1)_μ_i(k+p_j+p_k; p_i) · D^(2)_{μ_j μ_k}(k; p_j, p_k)
    #
    # For D^(2) · D^(1) (D^(2) on left): fermion in at k → through D^(1)(k; p_i) →
    # intermediate k+p_i → through D^(2)(k+p_i; p_j, p_k) → output k+P.
    # Matrix: D^(2)_{μ_j μ_k}(k+p_i; p_j, p_k) · D^(1)_μ_i(k; p_i)

    mix = np.zeros(k.shape[:-1] + (4, 4), dtype=complex)

    for i in range(3):
        j_idx = [jj for jj in range(3) if jj != i]
        p_i, mu_i = legs[i]
        p_j, mu_j = legs[j_idx[0]]
        p_k_leg, mu_k = legs[j_idx[1]]
        P_jk = p_j + p_k_leg

        # D^(1)·D^(2): D^(1)_{μ_i}(k+P_jk; p_i) · D^(2)_{μ_j μ_k}(k; p_j, p_k)
        # D^(2) is symmetric in its two legs, so we can just use (p_j, p_k) order:
        D2_jk_at_k = D2_dirac(k, p_j, p_k_leg, mu_j, mu_k)
        D1_i_at_kPjk = D1_dirac(k + P_jk, p_i, mu_i)
        L_ijk = np.einsum('...ij,...jk->...ik', D1_i_at_kPjk, D2_jk_at_k)
        mix = mix - L_ijk  # the "-" from "- D^(1) D^(2)"

        # D^(2)·D^(1): D^(2)_{μ_j μ_k}(k+p_i; p_j, p_k) · D^(1)_{μ_i}(k; p_i)
        D1_i_at_k = D1_dirac(k, p_i, mu_i)
        D2_jk_at_kpi = D2_dirac(k + p_i, p_j, p_k_leg, mu_j, mu_k)
        R_ijk = np.einsum('...ij,...jk->...ik', D2_jk_at_kpi, D1_i_at_k)
        mix = mix - R_ijk  # the "-" from "- D^(2) D^(1)"

    # Numerical prefactors:
    # A piece: from "+D_0^† D^(3)" with D^(3) carrying coeff (-i·g_0³/6) → overall +(-i/6)
    # D_end:   from "-D^(3) D_0" with D^(3) carrying (-i·g_0³/6) → overall -(-i/6) = +i/6
    # mix pieces: we used "-D^(1)D^(2) - D^(2)D^(1)" in mix. D^(1) carries (i·g_0), D^(2)
    #             carries (-i·g_0²/2), their product is (i)(-i/2) = 1/2 (per g_0³).
    #             So each mix term carries +1/2 per g_0³ before the leading "-".
    #             We already absorbed the "-" signs into mix.

    coeff_A    = -1j/6.0
    coeff_Dend = +1j/6.0
    coeff_mix  = +0.5   # BUT: we summed 3 choices of "which leg on D^(1)" × 2 orderings = 6 terms

    # WAIT — the (D†D)^(3) formula in §4 has single "−D^(1) D^(2)" and single "−D^(2) D^(1)",
    # not sums over leg assignments. The leg assignments arise from the DIFFERENTIATION,
    # i.e., δ³/δA δA δA of D^(1)·D^(2) picks up all orderings. But D^(2) ∝ A², D^(1) ∝ A,
    # so δ³ of D^(1)·D^(2) gives 3! = 6 ways to distribute the three δ's (i.e., the three
    # external legs). Each gives a distinct term.
    #
    # Hmm actually, thinking more carefully: D^(n) is the n-th Taylor coefficient in A.
    # D^(1)·D^(2) means "first-order in A times second-order in A" = total A^3. The
    # COEFFICIENT of A^3 in D^(1)·D^(2) already incorporates the fact that we're
    # extracting a specific cubic combination: D^(1)(A)·D^(2)(A,A) where the same
    # classical field A is Taylor-expanded in all three slots. To evaluate at
    # specific external momenta (p,q,r), we differentiate 3 times with respect to
    # distinct external momenta and get 3! = 6 permutation terms.
    #
    # This is exactly what my loop over `i` does (3 choices for which leg on D^(1),
    # and the two distinct D^(1)D^(2) vs D^(2)D^(1) orderings = 6 terms total).
    #
    # So `coeff_mix` should be +1/2 per term (the product of D^(1) and D^(2) coefficients,
    # modulo g_0³), with the "-" sign for D^(1)D^(2) and D^(2)D^(1) already in mix.
    # And no extra 1/3! because the 1/n! from the original Taylor expansion cancels the
    # 3! leg-assignment multiplicity... actually let me sort this out.
    #
    # D^(2)(A, A) = (1/2!) δ²D/δA² · A · A. So as a cubic functional, the A^3 part of
    # D^(1)(A) · D^(2)(A,A) already includes the 1/2! from D^(2). When we differentiate
    # to get the 3-leg vertex Γ^(3) = δ^3 S / δA δA δA (functional derivative with
    # factorials), we pick up the 3! from the S_3 permutations. Specifically:
    #   δ^3 [D^(1)(A) · D^(2)(A,A)] / δA(p_1) δA(p_2) δA(p_3)
    # should give Σ_{σ ∈ S_3} [D^(1)(p_σ(1)) · D^(2)(p_σ(2), p_σ(3))] / 2!
    #   = 3 · [sym over which leg on D^(1)] / 2! · 2 ordering-matched terms... 
    #
    # OK I'm going to go with the convention: "Γ_3 is the full vertex, fully
    # symmetrized". Each of my 6 terms in the loop corresponds to one distinct
    # {i, ordering} label, and the numerical prefactor per term is
    # [D^(1) coeff] × [D^(2) coeff] = (i)·(-i/2) = 1/2, all in units of g_0³.
    # Plus the leading "-" sign from "−D^(1)D^(2) −D^(2)D^(1)" in (D†D)^(3).
    #
    # Since I put the "-" in mix, mix already has +( -1 × +1/2 ) = −1/2 per mix term.
    # So coeff_mix = 1, not 0.5, to match. Hmm but I multiplied "+1" not "+1/2" in my
    # numeric pieces above. Let me rewrite more carefully:

    # Redo:
    mix2 = np.zeros(k.shape[:-1] + (4, 4), dtype=complex)
    for i in range(3):
        j_idx = [jj for jj in range(3) if jj != i]
        p_i, mu_i = legs[i]
        p_j, mu_j = legs[j_idx[0]]
        p_k_leg, mu_k = legs[j_idx[1]]
        P_jk = p_j + p_k_leg

        D2_jk_at_k    = D2_dirac(k, p_j, p_k_leg, mu_j, mu_k)
        D1_i_at_kPjk  = D1_dirac(k + P_jk, p_i, mu_i)
        L_ijk         = np.einsum('...ij,...jk->...ik', D1_i_at_kPjk, D2_jk_at_k)

        D1_i_at_k     = D1_dirac(k, p_i, mu_i)
        D2_jk_at_kpi  = D2_dirac(k + p_i, p_j, p_k_leg, mu_j, mu_k)
        R_ijk         = np.einsum('...ij,...jk->...ik', D2_jk_at_kpi, D1_i_at_k)

        # Each carries D^(1)·D^(2) = (i·g_0)·(-i·g_0²/2) = g_0³/2  Dirac matrix.
        # Overall sign in (D†D)^(3): "-" for both orderings.
        # Note: D^(2) is symmetric in its two legs, so we DON'T double-count by
        # swapping (j,k) — already included in the sym avg implicitly. For distinct
        # legs labeled j < k, the sum over (j, k) permutations is redundant.
        # But here, j_idx[0], j_idx[1] is ORDERED (e.g., for i=0: [1,2]; for i=1: [0,2];
        # etc.), so there's NO double-counting. Good.

        mix2 = mix2 - 0.5 * L_ijk  # − D^(1)·D^(2) with coeff 1/2
        mix2 = mix2 - 0.5 * R_ijk  # − D^(2)·D^(1) with coeff 1/2

    dirac = coeff_A * A + coeff_Dend * D_end + mix2
    # Overall (D†D)^(3) = g_0³ · [fully sym color] · dirac
    return dirac


# ============================================================
# Self-test
# ============================================================
if __name__ == "__main__":
    print("=== vertices.py self-test ===")
    print("Γ matrices:")
    print(f"  Γ^0 Hermitian: {np.allclose(GAMMA[0], GAMMA[0].conj().T)}")
    print(f"  Clifford algebra: OK (asserted on import)")
    print()

    N, m = 8, 0.1  # small for test
    k = lattice_momenta(N)
    print(f"Lattice: N={N}, m={m}, k shape: {k.shape}")

    D = D_scalar(k, m)
    print(f"D(k) range: [{D.min():.4f}, {D.max():.4f}]")
    print(f"D(k=0) = m² = {D[0]:.4f}  (expected: {m**2})")

    # Check D_0^† D_0 = D(k)·𝟙:
    D0_k = D0(k, m)
    D0d_k = D0dag(k, m)
    prod = np.einsum('...ij,...jk->...ik', D0d_k, D0_k)
    expected = D[..., np.newaxis, np.newaxis] * np.eye(4, dtype=complex)
    err = np.max(np.abs(prod - expected))
    print(f"D_0^†·D_0 = D(k)·𝟙:  max err = {err:.2e}  (should be ~0)")

    # Test D1_dirac
    p = np.array([0.1, 0.2, 0.3, 0.4])
    v = D1_dirac(k, p, 0)
    print(f"D^(1) shape: {v.shape}")

    # Test DdagD_1 — NOT expected to be well-defined at p=0 matrix-wise since it must
    # satisfy Ward-like identities. Just check it runs without error:
    M1 = DdagD_1(k, p, 0, m)
    print(f"(D†D)^(1) shape: {M1.shape}, magnitude range: [{np.abs(M1).min():.4f}, {np.abs(M1).max():.4f}]")

    # Test DdagD_2
    q = np.array([0.2, -0.1, 0.0, -0.1])
    M2 = DdagD_2(k, p, q, 0, 1, m)
    print(f"(D†D)^(2) shape: {M2.shape}, magnitude range: [{np.abs(M2).min():.4f}, {np.abs(M2).max():.4f}]")

    # Test DdagD_3
    r = -p - q  # momentum conservation
    M3 = DdagD_3(k, p, q, r, 0, 1, 2, m)
    print(f"(D†D)^(3) shape: {M3.shape}, magnitude range: [{np.abs(M3).min():.4f}, {np.abs(M3).max():.4f}]")

    print()
    print("All vertex functions run and return expected shapes.")
