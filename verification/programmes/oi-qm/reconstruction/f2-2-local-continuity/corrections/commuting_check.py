#!/usr/bin/env python3
"""F2-2 correction 1: commuting gates with noncommuting logarithms, decided exactly.

Run:  python3 -I commuting_check.py > commuting-check-output.txt
Imports the frozen F2-1 arithmetic (../../f2-1-e1-consistency/e1_exact.py) by path and changes
nothing in it. Exact over Q(zeta_3); [W] marks a written argument.

T_loc flows a layer by the sum of its gates' generators. The exponential of that sum is the product
of the gates when the generators commute; two gates sharing a site can commute while two of their
generators do not, and then the layer neither implements the gates nor respects the one-edge cone.
"""
import hashlib
import importlib.util
import itertools
import os
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
E1_PATH = os.path.join(HERE, "..", "..", "f2-1-e1-consistency", "e1_exact.py")
_spec = importlib.util.spec_from_file_location("e1_exact", E1_PATH)
e1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(e1)
out = e1.out

q = 3
F = e1.field(q)
h = pow(2, -1, q)


def sym_rep(e):
    e %= q
    return e if 2 * e <= q else e - q


def diag(vals):
    d = len(vals)
    D = e1.zeros(F, d)
    for i, v in enumerate(vals):
        D[i][i] = v
    return D


def kron(*ms):
    A = ms[0]
    for B in ms[1:]:
        A = e1.kron(F, A, B)
    return A


def comm(A, B):
    return e1.mat_sub(F, e1.mat_mul(F, A, B), e1.mat_mul(F, B, A))


def nnz(A):
    return sum(1 for r in A for x in r if not F.is_zero(x))


def projector(vec, norm):
    """|v><v| / norm for a rational vector v."""
    d = len(vec)
    return [[F.frac(Fraction(vec[i] * vec[j], norm)) for j in range(d)] for i in range(d)]


I3 = e1.eye(F, 3)
pair_pts = list(itertools.product(range(q), repeat=2))
# the pair gate delta(1): |x,y> -> w^{-xy}|x,y>, and its principal generator (theta in (-1/2, 1/2])
delta = diag([F.zeta((-x * y) % q) for x, y in pair_pts])
G0 = diag([F.frac(Fraction(sym_rep(-x * y), q)) for x, y in pair_pts])
v = [1 if (x, y) in ((0, 0), (0, 1), (1, 0)) else 0 for x, y in pair_pts]
P = projector(v, 3)
G = e1.mat_add(F, G0, P)

C3 = e1.Carrier(q, 3, F)
X1, Z1, X3, Z3 = C3.X(0), C3.Z(0), C3.X(2), C3.Z(2)


def chain_quantities(Gp, label):
    K = e1.mat_add(F, kron(Gp, I3), kron(I3, Gp))
    D = e1.mat_mul(F, kron(delta, I3), kron(I3, delta))
    KD = comm(K, D)
    c1 = comm(K, X1)
    first_ok = e1.is_zero_mat(F, comm(c1, X3)) and e1.is_zero_mat(F, comm(c1, Z3))
    c2 = comm(K, c1)
    second = (not e1.is_zero_mat(F, comm(c2, X3))) or (not e1.is_zero_mat(F, comm(c2, Z3)))
    out("%-28s [K, D] nonzero entries: %d; first-order term [K, X_1] commutes with X_3, Z_3: %s; "
        "second-order term [K, [K, X_1]] fails to commute with X_3 or Z_3: %s"
        % (label, nnz(KD), first_ok, second))
    return K, D, KD, second


def main():
    out("F2-2 correction 1 (2026-10-15): noncommuting generators of commuting gates. sha256 of the imported "
        "F2-1 module: %s" % hashlib.sha256(open(E1_PATH, "rb").read()).hexdigest())
    e1.header("The owner's witness: the pair gate delta(1) at q = 3")
    g0p = e1.mat_mul(F, G0, P)
    out("G0 diagonal, e^{2 pi i G0} = delta: %s" %
        all(F.root(q, (-x * y) % q) == F.zeta((-x * y) % q) for x, y in pair_pts))
    out("P = |psi><psi|, psi = (|00> + |01> + |10>)/sqrt3: P^2 = P %s; G0 P = 0 %s; P G0 = 0 %s"
        % (e1.mat_eq(e1.mat_mul(F, P, P), P), e1.is_zero_mat(F, g0p), e1.is_zero_mat(F, e1.mat_mul(F, P, G0))))
    out("[W] e^{2 pi i P} = 1 + (e^{2 pi i} - 1) P = 1 and G0 P = P G0 = 0, so e^{2 pi i (G0 + P)} = delta: "
        "G = G0 + P is a generator of delta supported on its pair, a member of Gamma_all outside Gamma_spec")
    out("P commutes with delta: %s; P commutes with delta (x) 1 on three sites and with 1 (x) delta: %s, %s"
        % (e1.is_zero_mat(F, comm(P, delta)),
           e1.is_zero_mat(F, comm(kron(P, I3), kron(delta, I3))),
           e1.is_zero_mat(F, comm(kron(P, I3), kron(I3, delta)))))

    e1.header("Three-site chain 1-2-3, both pairs coupled by delta(1): K = G_12 + G_23, D = delta_12 delta_23")
    K, D, KD, second = chain_quantities(G, "witness G = G0 + P:")
    row = C3.idx[(0, 1, 1)]
    col = C3.idx[(0, 0, 1)]
    target = F.mul(F.sub(F.one, F.zeta(2)), F.frac(Fraction(1, 3)))
    out("[K, D] at (|011>, |001>) = %s; equals (1 - w^2)/3: %s" % (F.show(KD[row][col]), KD[row][col] == target))
    out("[W] K commutes with e^{2 pi i K}; [K, D] != 0, so e^{2 pi i K} is not proportional to D: the coupling layer "
        "does not implement delta_12 delta_23 for this generator choice")
    out("[W] U(s)^+ X_1 U(s), U(s) = e^{2 pi i s K}, is analytic in s with s^2 coefficient proportional to "
        "[K, [K, X_1]]; that coefficient's commutator with X_3 or Z_3 is nonzero, so the strict one-edge cone fails "
        "for all small s != 0")
    witness_ok = (not e1.is_zero_mat(F, KD)) and KD[row][col] == target and second

    e1.header("Controls: diagonal generators")
    _, _, KD0, second0 = chain_quantities(G0, "principal G0:")
    E00 = diag([F.one if (x, y) == (0, 0) else F.zero for x, y in pair_pts])
    _, _, KDd, secondd = chain_quantities(e1.mat_add(F, G0, E00), "diagonal non-spectral G0+E00:")
    controls_ok = e1.is_zero_mat(F, KD0) and not second0 and e1.is_zero_mat(F, KDd) and not secondd

    e1.header("Two sites, R_self coupling [[1,1],[1,0]]: the site gate delta_1(1) and the pair gate delta_12(1)")
    site_exp = [(-h * y * y) % q for y in range(q)]
    dsite = diag([F.zeta(e) for e in site_exp])
    Gs0 = diag([F.frac(Fraction(sym_rep(e), q)) for e in site_exp])
    Ps = projector([0, 1, 1], 2)                     # inside the eigenspace {|1>, |2>} of delta_1(1)
    Gs = e1.mat_add(F, Gs0, Ps)
    out("site gate exponents %s; Ps = |+><+| inside the eigenspace span{|1>,|2>}: Ps^2 = Ps %s, [Gs0, Ps] = 0 %s, "
        "so e^{2 pi i (Gs0 + Ps)} = delta_1(1) [W]"
        % (site_exp, e1.mat_eq(e1.mat_mul(F, Ps, Ps), Ps), e1.is_zero_mat(F, comm(Gs0, Ps))))
    D2 = e1.mat_mul(F, kron(dsite, I3), delta)
    K2 = e1.mat_add(F, kron(Gs, I3), G0)
    K20 = e1.mat_add(F, kron(Gs0, I3), G0)
    nz2, nz20 = nnz(comm(K2, D2)), nnz(comm(K20, D2))
    out("non-spectral site generator: [K, D] nonzero entries %d; principal site generator: %d" % (nz2, nz20))
    site_ok = nz2 > 0 and nz20 == 0 and e1.is_zero_mat(F, comm(Gs0, Ps))

    e1.header("Summary")
    out("witness reproduced exactly (entry (1 - w^2)/3, second-order distant commutator): %s" % witness_ok)
    out("controls (principal and diagonal non-spectral generators commute with the layer): %s" % controls_ok)
    out("two-site overlap witness under R_self at (3,2): %s" % site_ok)
    out("RESULT %s" % ("PASS" if (witness_ok and controls_ok and site_ok) else "FAIL"))


if __name__ == "__main__":
    main()
