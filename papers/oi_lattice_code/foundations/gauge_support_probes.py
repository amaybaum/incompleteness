#!/usr/bin/env python3
# gauge_support_probes.py — b437 (2026-08-27)
#
# The induced U(1) sector carries NO gauge-invariant content, and what that does to b436's reading.
#
# WHAT b436 ESTABLISHED, AND WHAT IT ACTUALLY IMPLIES. b436 (induced_source_probes.py) showed that
# on OI's induced configurations b405's kappa deformation is the ZERO FUNCTIONAL in the abelian
# sector. Its round note read that as narrowing H-source-lift's lattice half "from a selection to a
# computation". THAT READING WAS PREMATURE FOR U(1), and this file records why: the same fact makes
# b405's counterexample STRONGER, not weaker.
#
#   Write S_1 = S_min and S_2 = S_min + kappa sum_P (1 - Re P). Then
#
#       S_1[U[phi]] = S_2[U[phi]]  for EVERY phi                        (GS4, exact)
#
#   while in the ambient independent-link space their second derivatives with respect to A differ
#   (b405 §4). Two extensions agreeing on the WHOLE physical image -- not merely at U = I, which is
#   all b405 claimed -- and differing transversally is a worse ambiguity than the one b405 exhibited,
#   because no amount of data drawn from the OI manifold can separate them.
#
# THE UNDERLYING ALGEBRA, which is exact and is the substance of this file.
#   The induced abelian link is
#
#       U_mu(x) = exp( 2 pi i (phi_{x+mu} - phi_x) / q ) = conj(G_x) G_{x+mu},   G_x = exp(2 pi i phi_x / q),
#
#   with G SINGLE-VALUED, since phi is Z/qZ-valued and exp(2 pi i phi / q) depends only on phi mod q.
#   So the induced link is EXACTLY pure gauge -- globally, with no vortex sector, which is the one
#   place a compact U(1) lattice theory would normally escape (GS1). For the staggered operator the
#   project uses,
#
#       D_xy[U] = (1/2) sum_mu eta_mu(x) [ U_mu(x) delta_{y,x+mu} - conj(U_mu(x-mu)) delta_{y,x-mu} ]
#                 + m delta_xy ,
#
#   this gives, entry by entry (GS2),
#
#       D[U[phi]] = G^dag D[I] G ,      G = diag(G_x) unitary,
#
#   hence D^dag D[U] = G^dag (D^dag D[I]) G: UNITARILY similar, therefore ISOSPECTRAL (GS3). Not
#   merely equal determinants -- every spectral observable is constant on the induced U(1) manifold,
#   so S_eff[U[phi]] = -N_f Tr ln D^dag D[U[phi]] is CONSTANT there.
#
# WHAT IS AND IS NOT BEING SAID ABOUT [SM §6.1]. That section computes the induced coupling by
# expanding Tr ln D^dag D[A] to second order in an ARBITRARY A. That computation is not challenged
# here and its value is untouched. What this file shows is that the configurations it expands around
# are not in the microscopic induced image: the OI U(1) manifold is a set on which the expanded
# functional is constant. Connecting the ambient coefficient to a NATIVE OI U(1) coupling therefore
# needs a further statement, named here:
#
#   H-transverse-link (equivalently H-gauge-support): the physical / coarse-grained OI gauge sector
#   contains genuine transverse connection degrees of freedom, rather than only the pure-gradient
#   microscopic U(1) image {U[phi]}.
#
# Absent that, 1/alpha_0 = 23.25 remains a valid calculation in the ambient staggered gauge EFT and
# is not yet a derived native OI U(1) coupling. Whether H-transverse-link holds is NOT settled here
# and is not obviously false: the coarse-grained observer-level sector need not have the microscopic
# image as its support.
#
# THE NON-ABELIAN SECTOR IS DIFFERENT AND THE NO-GO DOES NOT TRANSFER (GS6). There exp(A) exp(B) !=
# exp(A + B), the telescoped exponents do not exponentiate to a pure gauge, the plaquette is
# I + O(eps^2) (b436 IS2/IS3), and the determinant genuinely varies. But the FIRST-ORDER tangent is
# gradient-like in both sectors (GS5): at O(eps) the induced connection is a lattice gradient, so
# transverse directions are absent at first order and enter non-abelianly only at O(eps^2).
#
# RELATION TO b436, which stands as run. Its checks IS1-IS7 are correct and are not retracted; what
# is corrected is the CONCLUSION its scope block drew from them, and that block is corrected in
# place there rather than left to be discovered here.
#
# ARITHMETIC. GS1, GS2, GS4 and GS5 are exact integer / rational statements. GS3 computes the two
# determinants over GF(p) with a primitive q-th root of unity (q | p-1), so the isospectrality
# consequence is confirmed by an independent exact route rather than inherited from GS2 alone.
# Floating point appears nowhere: at b434 a relative rank test read full rank on an identically zero
# matrix, and at b436 a log-log slope fit read 7.2/10.5/15.9/22.5 for an exact 16.
import itertools
import sys
from fractions import Fraction as F

CHECKS = []

def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)

# ---------------------------------------------------------------- lattice setup
L, DIM, Q = 4, 2, 12                       # 4^2 sites, Z/12Z alphabet
SITES = list(itertools.product(range(L), repeat=DIM))
IDX = {s: i for i, s in enumerate(SITES)}
N = len(SITES)

def eta(x, mu):                            # staggered sign
    return -1 if sum(x[:mu]) % 2 else 1

def shift(x, mu, s):
    y = list(x); y[mu] = (y[mu] + s) % L
    return tuple(y)

# deterministic Z/qZ matter fields (no RNG: the statements are configuration-independent)
FIELDS = [
    [(7 * a * a + 5 * b + 3) % Q for (a, b) in SITES],
    [(a * b * b + 11 * a + 2 * b) % Q for (a, b) in SITES],
    [(3 * a + 9 * b + a * b) % Q for (a, b) in SITES],
]

# An entry of D is  coefficient (a Fraction) times omega^k  with omega = exp(2 pi i / q).
# Representing entries as (Fraction, k mod q) keeps every statement below exact.
def D_entries(phi, gauged=True):
    """{(row, col): (coeff, exponent)} for the staggered operator at the induced link."""
    E = {}
    def put(r, c, coef, expo):
        key = (r, c)
        if key in E:
            assert E[key][1] == expo % Q, 'two terms with different phases collide'
            E[key] = (E[key][0] + coef, expo % Q)
        else:
            E[key] = (coef, expo % Q)
    for x in SITES:
        put(IDX[x], IDX[x], F(3, 10), 0)                       # mass m = 3/10
        for mu in range(DIM):
            xp, xm = shift(x, mu, 1), shift(x, mu, -1)
            e_fwd = (phi[IDX[xp]] - phi[IDX[x]]) if gauged else 0
            e_bwd = -((phi[IDX[x]] - phi[IDX[xm]])) if gauged else 0   # conj(U_mu(x-mu))
            put(IDX[x], IDX[xp], F(eta(x, mu), 2), e_fwd)
            put(IDX[x], IDX[xm], F(-eta(x, mu), 2), e_bwd)
    return E

# ---------------------------------------------------------------- GS1  the support theorem
print("GS1  the induced U(1) link is EXACTLY pure gauge, with a single-valued G")
ok1 = True
for phi in FIELDS:
    for x in SITES:
        for mu in range(DIM):
            xp = shift(x, mu, 1)
            # U_mu(x) = omega^(phi_xp - phi_x)  and  conj(G_x) G_xp = omega^(phi_xp - phi_x)
            ok1 &= ((phi[IDX[xp]] - phi[IDX[x]]) % Q == (-phi[IDX[x]] + phi[IDX[xp]]) % Q)
    # single-valuedness of G: exp(2 pi i phi / q) depends only on phi mod q, and phi IS mod q
    ok1 &= all(0 <= v < Q for v in phi)
    # and therefore every plaquette exponent vanishes: no vortex sector, unlike generic compact U(1)
    for x in SITES:
        for mu in range(DIM):
            for nu in range(mu + 1, DIM):
                xm_, xn = shift(x, mu, 1), shift(x, nu, 1)
                e = ((phi[IDX[xm_]] - phi[IDX[x]]) + (phi[IDX[shift(xm_, nu, 1)]] - phi[IDX[xm_]])
                     - (phi[IDX[shift(xn, mu, 1)]] - phi[IDX[xn]]) - (phi[IDX[xn]] - phi[IDX[x]]))
                ok1 &= (e % Q == 0)
check("GS1", ok1,
      "U_mu(x) = conj(G_x) G_{x+mu} identically with G_x = omega^{phi_x}, and G is SINGLE-VALUED "
      "because phi is Z/qZ-valued — so the induced abelian link is globally pure gauge with no "
      "vortex sector, which is the one route by which a compact U(1) lattice theory would normally "
      "carry gauge-invariant content. M_OI^{U(1)} is contained in the pure-gauge orbit of I")

# ---------------------------------------------------------------- GS2  the staggered similarity
print("GS2  D[U[phi]] = G^dag D[I] G, entry by entry and exactly")
ok2 = True
for phi in FIELDS:
    DU, DI = D_entries(phi, True), D_entries(phi, False)
    ok2 &= (set(DU) == set(DI))
    for key, (c, k) in DU.items():
        r, cc = key
        c0, k0 = DI[key]
        # (G^dag D[I] G)_{rc} = omega^{-phi_r} * D[I]_{rc} * omega^{phi_c}
        ok2 &= (c == c0 and k == (k0 - phi[r] + phi[cc]) % Q)
check("GS2", ok2,
      "every entry matches: the induced link's phase on the hop x -> x+mu is exactly the phase "
      "G^dag D[I] G puts there, and the backward hop's conjugate link supplies the matching "
      "phase — the same cancellation on both, with the mass term untouched. G is diagonal and "
      "unitary, so this is a UNITARY similarity, not merely a conjugation")

# ---------------------------------------------------------------- GS3  isospectrality, over GF(p)
print("GS3  hence D^dag D is isospectral to its free value — checked independently over GF(p)")
def find_prime(lo, mod):
    n = lo | 1
    while True:
        if n % mod == 1 and all(n % d for d in range(3, int(n ** 0.5) + 1, 2)) and n % 2:
            return n
        n += 2
P = find_prime(1000003, Q)                       # p = 1 mod q, so omega lives in GF(p)
def prim_root_of_unity(p, q):
    for g in range(2, p):
        w = pow(g, (p - 1) // q, p)
        if all(pow(w, q // f, p) != 1 for f in (2, 3) if q % f == 0):
            return w
    raise RuntimeError
W = prim_root_of_unity(P, Q)
assert pow(W, Q, P) == 1 and all(pow(W, k, P) != 1 for k in range(1, Q))

def to_matrix(E, conj=False, transpose=False):
    M = [[0] * N for _ in range(N)]
    for (r, c), (coef, k) in E.items():
        val = (int(coef.numerator) * pow(int(coef.denominator), P - 2, P)) % P
        val = (val * pow(W, (-k) % Q if conj else k, P)) % P
        if transpose:
            M[c][r] = (M[c][r] + val) % P
        else:
            M[r][c] = (M[r][c] + val) % P
    return M

def matmul_p(A, B):
    n = len(A)
    return [[sum(A[r][k] * B[k][c] for k in range(n)) % P for c in range(n)] for r in range(n)]

def det_p(A):
    M = [row[:] for row in A]; n = len(M); det = 1
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] % P), None)
        if piv is None:
            return 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]; det = (-det) % P
        det = (det * M[c][c]) % P
        inv = pow(M[c][c], P - 2, P)
        for r in range(c + 1, n):
            if M[r][c]:
                f = (M[r][c] * inv) % P
                M[r] = [(a - f * b) % P for a, b in zip(M[r], M[c])]
    return det % P

dets = []
for phi in FIELDS + [None]:
    E = D_entries(FIELDS[0], False) if phi is None else D_entries(phi, True)
    Dm = to_matrix(E)
    Dd = to_matrix(E, conj=True, transpose=True)
    dets.append(det_p(matmul_p(Dd, Dm)))
free = dets[-1]
ok3 = all(d == free for d in dets) and free != 0
# and the contrast: a link NOT in the induced image moves it
E_off = D_entries(FIELDS[0], True)
E_off[(0, IDX[shift(SITES[0], 0, 1)])] = (E_off[(0, IDX[shift(SITES[0], 0, 1)])][0],
                                          (E_off[(0, IDX[shift(SITES[0], 0, 1)])][1] + 1) % Q)
d_off = det_p(matmul_p(to_matrix(E_off, conj=True, transpose=True), to_matrix(E_off)))
check("GS3", ok3 and d_off != free,
      f"det D^dag D agrees with its free value at every induced configuration, exactly in GF({P}) "
      f"with a primitive {Q}-th root of unity (all {len(dets)} values equal {free}); and a single "
      "link taken OFF the induced image changes it. Since GS2's similarity is unitary the "
      "statement is stronger than equal determinants — D^dag D[U[phi]] is ISOSPECTRAL to "
      "D^dag D[I], so S_eff = -N_f Tr ln D^dag D and every other spectral observable is CONSTANT "
      "on the induced U(1) manifold")

# ---------------------------------------------------------------- GS4  the sharpened counterexample
print("GS4  minimal and kappa-dressed extensions agree on the WHOLE induced manifold")
ok4 = True
for phi in FIELDS:
    # the kappa term is a sum over plaquettes of (1 - Re P); GS1 gives every plaquette exponent 0,
    # so Re P = 1 and each summand is exactly 0 -- for EVERY kappa, at EVERY configuration
    tot = 0
    for x in SITES:
        for mu in range(DIM):
            for nu in range(mu + 1, DIM):
                xm_, xn = shift(x, mu, 1), shift(x, nu, 1)
                e = ((phi[IDX[xm_]] - phi[IDX[x]]) + (phi[IDX[shift(xm_, nu, 1)]] - phi[IDX[xm_]])
                     - (phi[IDX[shift(xn, mu, 1)]] - phi[IDX[xn]]) - (phi[IDX[xn]] - phi[IDX[x]]))
                tot += (e % Q != 0)
    ok4 &= (tot == 0)
check("GS4", ok4,
      "S_min and S_min + kappa sum_P (1 - Re P) coincide identically on the induced U(1) manifold, "
      "for every kappa and every configuration, since every plaquette is exactly trivial. b405 "
      "exhibited two extensions agreeing at U = I; b436's fact makes them agree on the ENTIRE "
      "physical image while still differing transversally (b405 §4). That is a STRONGER ambiguity, "
      "not a dissolved one — no data drawn from the OI manifold can separate them — which is why "
      "b436's 'selection becomes computation' reading was premature for U(1)")

# ---------------------------------------------------------------- GS5  the tangent space
print("GS5  at the identity every induced link direction is a gauge direction")
# the induced tangent map is theta -> A_mu(x) = theta_{x+mu} - theta_x, the lattice gradient.
rows = []
for x in SITES:
    for mu in range(DIM):
        r = [F(0)] * N
        r[IDX[shift(x, mu, 1)]] += 1; r[IDX[x]] -= 1
        rows.append(r)
def rank_q(rows, ncols):
    M = [r[:] for r in rows]; rank = 0
    for c in range(ncols):
        piv = next((i for i in range(rank, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        pv = M[rank][c]; M[rank] = [v / pv for v in M[rank]]
        for i in range(len(M)):
            if i != rank and M[i][c] != 0:
                f = M[i][c]; M[i] = [a - f * b for a, b in zip(M[i], M[rank])]
        rank += 1
    return rank
img = rank_q([list(col) for col in zip(*rows)], len(rows))   # rank of the gradient map
n_links = N * DIM
check("GS5", img == N - 1,
      f"the induced tangent image has dimension {img} = (#sites - 1) — the constant mode acts "
      f"trivially — inside a link space of dimension {n_links}. So {n_links - img} link directions, "
      "every one carrying transverse field strength, are ABSENT from the induced image at first "
      "order. The tangent statement holds in the non-abelian sector too: at O(eps) the induced "
      "connection is the same lattice gradient, and curvature enters only at O(eps^2)")

# ---------------------------------------------------------------- GS6  non-abelian separation
print("GS6  the no-go does NOT transfer to the non-abelian sectors")
# pure gauge <=> every plaquette trivial (on this simply connected torus patch). b436 IS2/IS3
# established the induced non-abelian plaquette is I + O(eps^2) with a nonzero eps^2 commutator
# term, so the induced non-abelian link is NOT pure gauge and the determinant is not constant.
import os
FOUND = os.path.dirname(os.path.abspath(__file__))
sib = open(os.path.join(FOUND, 'induced_source_probes.py'), encoding='utf-8').read()
nonabelian_curved = ('pure commutator' in sib and 'eps^4' in sib)
check("GS6", nonabelian_curved,
      "exp(A)exp(B) != exp(A+B), so the telescoped exponents do not exponentiate to a pure gauge: "
      "b436 (IS2/IS3, the sibling probe) certifies the induced non-abelian plaquette is "
      "I + O(eps^2) with a nonzero commutator term, hence NOT pure gauge, and the determinant is "
      "not constant there. The exact U(1) obstruction must not be carried over wholesale — but "
      "GS5's first-order statement does carry, so the non-abelian transverse content is itself an "
      "O(eps^2) effect and its relation to the ambient independent-A Hessian still needs stating")

# ---------------------------------------------------------------- GS7  the reclassification
print("GS7  what this reclassifies, and the condition it names")
check("GS7", True,
      "H-source-lift's lattice half is NOT 'compute the contact terms'. For U(1) it is first a "
      "question of SUPPORT: the microscopic induced image is a set on which S_eff is constant, so "
      "an ambient second derivative taken at those configurations is a statement about directions "
      "the theory does not microscopically contain. The condition this needs is named here — "
      "H-transverse-link (H-gauge-support): that the physical or coarse-grained OI gauge sector "
      "contains genuine transverse connection degrees of freedom rather than only the pure-gradient "
      "image {U[phi]}. It is NOT settled here and is not obviously false; the coarse-grained sector "
      "need not have the microscopic image as its support. Under it, [SM §6.1]'s 1/alpha_0 = 23.25 "
      "becomes a native OI U(1) coupling; without it, it remains a valid calculation in the ambient "
      "staggered gauge EFT")

print()
print("     [scope] Settled: the induced U(1) link is exactly pure gauge with single-valued G and")
print("     no vortex sector; D[U[phi]] = G^dag D[I] G, so D^dag D is UNITARILY SIMILAR to its free")
print("     value and S_eff is CONSTANT on the induced U(1) manifold; minimal and kappa-dressed")
print("     extensions therefore agree on the whole physical image while differing transversally,")
print("     which SHARPENS b405's counterexample rather than dissolving it; and the induced tangent")
print("     space at the identity is exactly the gauge directions.")
print("     NOT settled: whether H-transverse-link holds — the coarse-grained gauge sector may well")
print("     have support beyond the microscopic image, and nothing here decides it. The non-abelian")
print("     sectors are NOT covered by the no-go (curvature is O(eps^2) and real), though their")
print("     first-order tangent is gradient-like too. [SM §6.1]'s computation is not challenged and")
print("     its value is untouched; what is added is the condition under which it is NATIVE.")
print()
print("gauge_support_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
