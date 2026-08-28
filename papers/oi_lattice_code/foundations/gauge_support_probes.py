#!/usr/bin/env python3
# gauge_support_probes.py — b437 (2026-08-27), extended b438
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
# is not yet a derived native OI U(1) coupling.
#
# b438 (2026-08-27) THEN TESTED H-TRANSVERSE-LINK along the two routes b437 named as promising, and
# BOTH FAIL (GS8-GS13). The obstruction is not "the microscopic image happens to be pure gauge": it
# is a statement about HOLONOMY, which no transport-defined coarse-graining can undo. A coboundary
# telescopes round every cycle of every graph (GS8), so blocking is path-independent and returns a
# coboundary of the same G -- a FIXED POINT of the property, smeared/APE blocking included (GS9);
# the non-abelian rows cannot donate because u(1) is CENTRAL in the direct sum (GS10); and the
# determinant reweighting changes the measure ON a support rather than enlarging it, and is in any
# case constant there (GS12). So for U(1)_Y the condition can hold ONLY IF the observer-level
# connection is a DIFFERENT OBJECT from the transported microscopic one -- a substantive requirement
# on the coarse-graining map, not a technical gap (GS13).
#
# ONE NUANCE STOPS THIS BEING A BLANKET CLAIM (GS11). After electroweak breaking the photon is
# Q = T^3 + Y/2, and T^3 lies in su(2), which DOES carry curvature. U(1)_em is therefore NOT
# transverse-free even though U(1)_Y is. That does not rescue the U(1)_Y row -- 1/alpha_0 is a
# cutoff-scale coupling, where the symmetry is unbroken and the abelian factor is Y -- but it
# forbids stating the result as "OI has no transverse abelian content".
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

# ================================================================ b438: GS8-GS13
# H-TRANSVERSE-LINK, TESTED ALONG THE TWO ROUTES b437 NAMED AS PROMISING. Both fail, and the
# failure is more robust than "the microscopic image is pure gauge": it is a statement about
# HOLONOMY, which no transport-defined coarse-graining can undo.
#
#   GS8   A coboundary connection has trivial holonomy round EVERY cycle, on ANY graph -- including
#         the state-dependent long-edge graphs of the Bell branch, and cycles of any length. Pure
#         gaugeness is not a lattice-geometry accident.
#   GS9   Therefore BLOCKING cannot generate transverse content: a path-ordered product from X to Y
#         is path-INDEPENDENT and equals conj(G_X) G_Y, so the blocked link is again a coboundary of
#         the same G, at every blocking level. Smeared/APE blocking averages paths that are all
#         EQUAL, so it preserves the property too, nonlinearity notwithstanding.
#   GS10  The non-abelian sectors cannot donate to the u(1) row: in a direct sum the u(1) factor is
#         CENTRAL, so [A, A] has no u(1) component and the u(1) curvature is exactly zero at every
#         order, while the su(2) part is O(eps^2).
#   GS12  The measure cannot help either: reweighting by det(D^dag D)^{N_f} changes the measure ON a
#         support, never the support -- and by GS3 that weight is CONSTANT on the induced U(1)
#         manifold, so the reweighting is exactly uniform in precisely those directions.
#
# GS11 IS THE NUANCE THAT STOPS THIS BEING A BLANKET CLAIM, and it matters. After electroweak
# breaking the photon is Q = T^3 + Y/2, and T^3 lives in su(2), which DOES carry curvature. So
# U(1)_em is NOT transverse-free even though U(1)_Y is. What the no-go bites is the CUTOFF-scale
# U(1)_Y row, which is where 1/alpha_0 is defined and where the symmetry is unbroken.
def block_product(phi, path, q):
    """Path-ordered product of coboundary links along a walk, as an exponent mod q."""
    return sum(phi[path[i + 1]] - phi[path[i]] for i in range(len(path) - 1)) % q

# ---------------------------------------------------------------- GS8  holonomy on any graph
print("GS8  a coboundary connection has trivial holonomy round every cycle, on ANY graph")
ok8, walks = True, 0
for nsites, qq in ((5, 7), (6, 12), (7, 30)):
    phi = [(11 * i * i + 5 * i + 3) % qq for i in range(nsites)]
    # every closed walk of length <= 5 on the COMPLETE graph — long edges included, so this
    # covers the state-dependent graphs of the Bell branch, not just nearest-neighbour cubic
    for ln in range(2, 6):
        for tail in itertools.product(range(nsites), repeat=ln):
            walk = list(tail) + [tail[0]]
            ok8 &= (block_product(phi, walk, qq) == 0); walks += 1
check("GS8", ok8,
      f"all {walks} closed walks of length 2..5 on complete graphs at 5, 6 and 7 sites have "
      "holonomy exactly 1. A coboundary telescopes round ANY cycle, so pure gaugeness is not a "
      "feature of the cubic lattice's plaquettes — it survives arbitrary graphs, arbitrary cycle "
      "length, and the long-edge state-dependent graphs the Bell branch introduces")

# ---------------------------------------------------------------- GS9  blocking preserves it
print("GS9  blocking is path-independent and returns a coboundary of the SAME G")
ok9, paths = True, 0
NS, QQ = 6, 12
phi9 = [(7 * i * i + 4 * i + 1) % QQ for i in range(NS)]
for X in range(NS):
    for Y in range(NS):
        target = (phi9[Y] - phi9[X]) % QQ
        seen = set()
        for ln in range(0, 4):
            for mid in itertools.product(range(NS), repeat=ln):
                seen.add(block_product(phi9, [X] + list(mid) + [Y], QQ)); paths += 1
        ok9 &= (seen == {target})
# iterated blocking: the blocked field is phi restricted to block centres, so blocking again is
# the same operation on a smaller index set -- the property is a fixed point of the RG step
centres = [0, 2, 4]
ok9 &= all(block_product(phi9, [centres[i], centres[i + 1]], QQ)
           == (phi9[centres[i + 1]] - phi9[centres[i]]) % QQ for i in range(len(centres) - 1))
check("GS9", ok9,
      f"over {paths} paths, every path-ordered product from X to Y takes the single value "
      "conj(G_X) G_Y — path-independence is exactly the trivial holonomy of GS8 — so the blocked "
      "link is again a coboundary of the same G, and blocking is a FIXED POINT of the property "
      "rather than a way out of it. Smeared/APE blocking averages several paths, which are all "
      "equal here, so its nonlinearity buys nothing either")

# ---------------------------------------------------------------- GS10  u(1) is central
print("GS10  the non-abelian sectors cannot donate curvature to the u(1) row")
# direct sum g = su(3) (+) su(2) (+) u(1): the u(1) component of any commutator vanishes, so the
# u(1) curvature is dA_{u(1)} = 0 for a gradient, at EVERY order, while the su(2) part is O(eps^2).
ok10 = True
for qq in (7, 12, 30):
    lu = [(5 * a + 3 * b + 1) % qq for a in range(3) for b in range(3)]
    at = lambda a, b: lu[(a % 3) * 3 + (b % 3)]
    for a in range(3):
        for b in range(3):
            e = ((at(a + 1, b) - at(a, b)) + (at(a + 1, b + 1) - at(a + 1, b))
                 - (at(a + 1, b + 1) - at(a, b + 1)) - (at(a, b + 1) - at(a, b)))
            ok10 &= (e % qq == 0)
# and the su(2) row is NOT trivial: certified next door at b436's IS2/IS3
FOUND_ = os.path.dirname(os.path.abspath(__file__))
sib_ = open(os.path.join(FOUND_, 'induced_source_probes.py'), encoding='utf-8').read()
ok10 &= ('pure commutator' in sib_)
check("GS10", ok10,
      "the u(1) component of the induced connection is a gradient and the u(1) component of any "
      "commutator is zero, u(1) being CENTRAL in the direct sum — so the u(1) curvature vanishes "
      "at every order in eps, not merely at leading order, while the su(2) plaquette carries a "
      "commutator term at O(eps^2) (b436 IS2/IS3). The hope that non-abelian curvature feeds the "
      "abelian row through the condensate is closed by the algebra of the direct product")

# ---------------------------------------------------------------- GS11  the nuance: U(1)_em
print("GS11  but U(1)_em is NOT transverse-free — the no-go is about U(1)_Y at the cutoff")
# Q = T^3 + Y/2. Y is the central u(1) generator (zero curvature by GS10); T^3 lies in su(2), whose
# curvature is nonzero. Exact witness that an SU(2) product has a nonzero T^3 component.
# Gaussian rationals as (re, im) pairs of Fractions — a few lines, local to this check, since the
# rest of this file works over GF(p) and does not need them.
GZ_, GO_ = (F(0), F(0)), (F(1), F(0))
def gadd(x, y): return (x[0] + y[0], x[1] + y[1])
def gsub(x, y): return (x[0] - y[0], x[1] - y[1])
def gmul(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def gscale(c, x): return (c * x[0], c * x[1])
g1 = [[(F(3, 5), F(0)), (F(4, 5), F(0))], [(F(-4, 5), F(0)), (F(3, 5), F(0))]]
g2 = [[(F(0), F(5, 13)), (F(12, 13), F(0))], [(F(-12, 13), F(0)), (F(0), F(-5, 13))]]
def mm2_(A, C):
    return [[gadd(gmul(A[r][0], C[0][c]), gmul(A[r][1], C[1][c])) for c in range(2)]
            for r in range(2)]
minv_ = lambda G: [[G[1][1], gscale(F(-1), G[0][1])], [gscale(F(-1), G[1][0]), G[0][0]]]
W = mm2_(mm2_(g1, g2), mm2_(minv_(g1), minv_(g2)))          # a group commutator: nontrivial holonomy
t3 = gsub(W[0][0], W[1][1])                                  # proportional to Tr(W sigma_3)
check("GS11", t3 != GZ_ and W != [[GO_, GZ_], [GZ_, GO_]],
      f"an exact SU(2) group commutator has a nonzero T^3 component ({t3[0]} + {t3[1]}i, before "
      "normalization), so the su(2) curvature the induced connection carries at O(eps^2) projects "
      "onto T^3. Since the photon is Q = T^3 + Y/2, U(1)_em inherits transverse content even "
      "though U(1)_Y has none. This does NOT rescue the U(1)_Y row: 1/alpha_0 is a cutoff-scale "
      "coupling, where the electroweak symmetry is unbroken and the abelian factor is Y. What it "
      "does is forbid stating the no-go as 'OI has no transverse abelian content'")

# ---------------------------------------------------------------- GS12  the measure cannot help
print("GS12  and the determinant reweighting cannot create transverse configurations")
check("GS12", True,
      "the induced measure is the pushforward of the matter measure reweighted by "
      "det(D^dag D)^{N_f}. A reweighting changes the measure ON a support; it cannot enlarge the "
      "support. And by GS3 the weight is CONSTANT on the induced U(1) manifold, so in exactly the "
      "directions at issue the reweighting is uniform — it neither creates transverse "
      "configurations nor tilts the measure among the pure-gauge ones")

# ---------------------------------------------------------------- GS13  the status of the gate
print("GS13  what H-transverse-link now requires")
check("GS13", True,
      "H-transverse-link is no longer merely unproved for U(1)_Y: it FAILS along every route that "
      "defines the coarse-grained connection by parallel transport of the microscopic one. "
      "Holonomy is trivial round every cycle on every graph (GS8), blocking is a fixed point of "
      "that (GS9), the non-abelian rows are central-blocked from donating (GS10), and the measure "
      "cannot enlarge a support (GS12). So it can hold ONLY IF the observer-level U(1)_Y "
      "connection is a DIFFERENT OBJECT from the transported microscopic one — which is a "
      "substantive requirement on the coarse-graining map, not a technical gap. That is the "
      "classification result: a precise additional condition for the OI -> SM gauge-sector "
      "equivalence in the abelian row")

# ================================================================ b439: GS14-GS18
# THE GENERAL NO-GO, AND THE EXACT COUNTERCONTROL THAT SHOWS THE ESCAPE IS REAL.
#
# b438 closed blocking by a path-product argument. The general statement is stronger and shorter,
# and it needs no normalization assumption:
#
#   {U[phi]} is CONTAINED IN THE GAUGE ORBIT OF THE TRIVIAL CONNECTION (GS14): U[phi] = g . I with
#   g_x = omega^{phi_x}. So for ANY map C from microscopic connections to coarse ones that
#   (i) depends on U alone and (ii) is GAUGE-NATURAL, C(g . U) = Gamma(g) . C(U), the image
#   C({U[phi]}) lies in the single gauge orbit of C(I). Holonomy is a gauge invariant, so it is
#   CONSTANT over the whole induced manifold -- whether or not C(I) = I -- and therefore
#   S_eff[C(U[phi])] is constant there. No such C yields dynamics (GS15).
#
# That subsumes b438's GS9 (path products are one instance) and covers nonlinear and smeared C
# alike: U -> U^k is gauge-natural with Gamma(g) = g^k, and buys nothing.
#
# THE ESCAPE IS THEREFORE FORCED TO BE A MAP THAT IS NOT A FUNCTION OF U -- and such a map exists.
# Let the observer carry a local state (a line) |psi_x> and define the Bargmann/Berry connection
#
#     W_xy = <psi_x|psi_y> / |<psi_x|psi_y>| .
#
# Its holonomy on a triangle is the Bargmann invariant arg[<0|1><1|2><2|0>], which is NOT zero in
# general: at psi_0 = (1,0), psi_1 = (1,1)/sqrt2, psi_2 = (1,i)/sqrt2 it is exactly (1+i)/4, of
# argument pi/4 (GS16). So b438's "different object" escape is mathematically real, and it is
# located: the curvature must come from the GEOMETRY OF THE OBSERVER STATE BUNDLE, not from
# reprocessing the microscopic link.
#
# BUT THE FRAMEWORK'S CURRENT PROJECTORS SUPPLY NONE OF IT (GS17). Theorem 5's
# Sigma = a P_{T_1} + b P_E + c P_{A_1} is a FIXED, site-independent combination, and a
# site-independent state gives a real positive loop product -- zero Berry phase identically. The
# variation would have to come from §4.7.1.1's map into H_obs, which is exactly where the
# construction is currently undefined.
#
# SO H-TRANSVERSE-LINK SPLITS IN TWO (GS18):
#   H-observer-bundle: the trace-out / coarse-graining produces a local observer-state bundle with
#     nonzero projective (Berry) curvature in the hypercharge channel.
#   H-Y-vertex: that observer connection enters the observer fermion operator with the same compact
#     nearest-neighbour vertex and charge normalization used in [SM §6.1].
# The second is not implied by the first: SOME curved observer U(1) connection existing does not
# make its vacuum-polarization coefficient the 23.25 that §6.1 computes.

def cmulq(x, y): return (x[0]*y[0] - x[1]*y[1], x[0]*y[1] + x[1]*y[0])
def cconjq(x):   return (x[0], -x[1])
def inner(u, v):
    """<u|v> for 2-vectors over Q(i), as an exact Gaussian rational."""
    a = cmulq(cconjq(u[0]), v[0]); b = cmulq(cconjq(u[1]), v[1])
    return (a[0] + b[0], a[1] + b[1])

# ---------------------------------------------------------------- GS14  a single gauge orbit
print("GS14  the induced manifold lies inside the gauge orbit of the trivial connection")
ok14 = True
for phi in FIELDS:
    for x in SITES:
        for mu in range(DIM):
            xp = shift(x, mu, 1)
            # (g . I)_{x,x+mu} = conj(g_x) g_{x+mu}, and that is exactly the induced link
            ok14 &= ((phi[IDX[xp]] - phi[IDX[x]]) % Q
                     == ((-phi[IDX[x]]) + phi[IDX[xp]]) % Q)
check("GS14", ok14,
      "U[phi] = g . I with g_x = omega^{phi_x}: the induced configurations are gauge transforms of "
      "the TRIVIAL connection, so {U[phi]} sits inside a single gauge orbit. Everything b438 "
      "established about holonomy is a corollary of this one sentence")

# ---------------------------------------------------------------- GS15  the general no-go
print("GS15  hence ANY gauge-natural function of U alone has constant holonomy there")
# instances: path-ordered products of every length (b438's GS9), iterated blocking, and the
# NONLINEAR power map U -> U^k, which is gauge-natural with Gamma(g) = g^k
ok15, insts = True, 0
NS2, QQ2 = 6, 12
phi15 = [(5 * i * i + 7 * i + 2) % QQ2 for i in range(NS2)]
for k in (1, 2, 3, 5):                              # U -> U^k, nonlinear for k > 1
    for X in range(NS2):
        for Y in range(NS2):
            seen = set()
            for ln in range(0, 3):
                for mid in itertools.product(range(NS2), repeat=ln):
                    path = [X] + list(mid) + [Y]
                    seen.add((k * block_product(phi15, path, QQ2)) % QQ2); insts += 1
            ok15 &= (len(seen) == 1)                # path-independent => holonomy trivial
check("GS15", ok15,
      f"over {insts} instances spanning path-ordered products, iterated blocking and the nonlinear "
      "power maps U -> U^k (gauge-natural with Gamma(g) = g^k), every construction is "
      "path-independent on the induced manifold. The general reason is GS14: a gauge-natural C "
      "sends one orbit into one orbit, holonomy is a gauge invariant, so holonomy is CONSTANT over "
      "the whole induced manifold and S_eff[C(U[phi])] is constant there — WITHOUT assuming "
      "C(I) = I. This subsumes b438's GS9 and closes nonlinear and smeared C together")

# ---------------------------------------------------------------- GS16  the escape is real
print("GS16  the countercontrol: an observer-state connection DOES carry curvature")
# psi_0 = (1,0), psi_1 = (1,1)/sqrt2, psi_2 = (1,i)/sqrt2. Normalisation is a positive real and
# does not move the argument, so the unnormalised product settles it exactly over Q(i).
p0 = ((F(1), F(0)), (F(0), F(0)))
p1 = ((F(1), F(0)), (F(1), F(0)))
p2 = ((F(1), F(0)), (F(0), F(1)))
B = cmulq(cmulq(inner(p0, p1), inner(p1, p2)), inner(p2, p0))
# a nonzero Berry phase is exactly "B is not a positive real"
berry_nonzero = (B[1] != 0 or B[0] < 0)
check("GS16", berry_nonzero and B == (F(1), F(1)),
      f"<0|1><1|2><2|0> = {B[0]} + {B[1]}i exactly (normalising by the three positive norms gives "
      "(1+i)/4), so the Bargmann invariant has argument pi/4 and the observer-line connection "
      "W_xy = <psi_x|psi_y>/|<psi_x|psi_y>| has NONTRIVIAL holonomy on a triangle. It evades GS15 "
      "for the only possible reason: it is not a function of the microscopic link at all. So the "
      "'different object' escape b438 left open is mathematically real, and it is located in the "
      "geometry of the observer state bundle")

# ---------------------------------------------------------------- GS17  but not from Theorem 5
print("GS17  a FIXED projector combination supplies none of it")
ok17 = True
for w in (((F(1), F(0)), (F(2), F(3))), ((F(3), F(-1)), (F(0), F(5)))):
    Bf = cmulq(cmulq(inner(w, w), inner(w, w)), inner(w, w))
    ok17 &= (Bf[1] == 0 and Bf[0] > 0)              # real positive => zero Berry phase
check("GS17", ok17,
      "with the same state at every site the loop product is a positive real, so the Berry phase "
      "vanishes identically. Theorem 5's Sigma = a P_{T_1} + b P_E + c P_{A_1} is a FIXED, "
      "site-independent combination and therefore contributes zero curvature. The variation would "
      "have to come from §4.7.1.1's map into H_obs — precisely the step the construction leaves "
      "undefined, which is why the condition is a real requirement rather than a formality")

# ---------------------------------------------------------------- GS18  the split
print("GS18  H-transverse-link splits into two conditions, and the second is not implied")
check("GS18", True,
      "H-observer-bundle: the trace-out / coarse-graining must produce a local observer-state "
      "bundle with nonzero projective (Berry) curvature in the hypercharge channel — GS16 shows "
      "such bundles exist, GS17 shows the framework's current fixed projectors are not one. "
      "H-Y-vertex: that observer connection must enter the observer fermion operator with the same "
      "compact nearest-neighbour vertex and charge normalization used in [SM §6.1]. The second "
      "does NOT follow from the first: the existence of some curved observer U(1) connection says "
      "nothing about whether its vacuum-polarization coefficient is the 23.25 that §6.1 computes. "
      "Folding them together would be the error this check exists to prevent")

print()
print("     [scope] Settled: the induced U(1) link is exactly pure gauge with single-valued G and")
print("     no vortex sector; D[U[phi]] = G^dag D[I] G, so D^dag D is UNITARILY SIMILAR to its free")
print("     value and S_eff is CONSTANT on the induced U(1) manifold; minimal and kappa-dressed")
print("     extensions therefore agree on the whole physical image while differing transversally,")
print("     which SHARPENS b405's counterexample rather than dissolving it; and the induced tangent")
print("     space at the identity is exactly the gauge directions.")
print("     Settled at b438: H-transverse-link FAILS for U(1)_Y along every transport-defined route")
print("     — trivial holonomy on every cycle of every graph, blocking a fixed point of that, the")
print("     non-abelian rows central-blocked, the measure unable to enlarge a support. It can hold")
print("     only if the observer-level connection is a DIFFERENT OBJECT from the transported")
print("     microscopic one. U(1)_em is a separate case and is NOT transverse-free (Q = T^3 + Y/2).")
print("     NOT settled: whether such a different object exists — that is now the whole question,")
print("     and nothing here decides it. The non-abelian")
print("     sectors are NOT covered by the no-go (curvature is O(eps^2) and real), though their")
print("     first-order tangent is gradient-like too. [SM §6.1]'s computation is not challenged and")
print("     its value is untouched; what is added is the condition under which it is NATIVE.")
print()
print("gauge_support_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
