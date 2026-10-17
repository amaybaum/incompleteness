#!/usr/bin/env python3
"""Track C exact checks: the symmetric-cone screen and two relaxed-domain SP counterexamples.

Standard library only; arithmetic in Q(i) with fractions.Fraction.  Nothing is imported from
#820's or #832's checkers or from the kernel.  Run:  python3 -I symrigid_exact.py

Written theorem (report.md, C1): a closed convex cone C with SEP <= C <= maxCone on the two-qubit
carrier that is linearly isomorphic to the cone of a Euclidean Jordan algebra equals Q3 or
Gamma(Q3); every local CP map (every Phi_k) preserves both; CNOT preserves C iff C = Q3.
This script certifies the finite linear identities and witnesses that argument uses:
  R1  Gamma o Ad_(A(x)B) o Gamma = Ad_(A(x)conj B) on all 16 matrix units, A, B non-unitary.
  R2  Gamma_1 = (full transpose) o Gamma_2, and SWAP Gamma_2 SWAP = Gamma_1, on all 16 units.
  R3  the four computational product projectors form a frame of every domain cone.
  R4  X -> A X A^dag and X -> A X^T A^dag are Lorentz similarities of Herm(2) (polarized
      determinant identity on the Pauli basis); the transpose is improper (Pauli matrix
      diag(1,1,-1,1)).
  R5  CNOT maps the product state |+0><+0| out of Gamma(Q3) (Bell witness); Q3 is CNOT-invariant.
  R6  Gamma o Phi_1 o Gamma = (5/8) Ad_(I(x)conj D) + (3/8) id on all 16 units.
  R7  negative control for the pure-marginal lemma: a nonzero off-diagonal block with a zero
      |1><1| block gives a negative product expectation.
Relaxed-domain counterexamples (each keeps SP and drops exactly one domain clause):
  CX1 C_sigma  = {X : X + s Tr(X) sigma >= 0}: SP, closed convex, contains SEP (indeed Q3),
      not inside maxCone; Phi_1 sends a member outside.
  CX2 C'_sigma = {X : X - s' Tr(X) sigma >= 0}: SP, closed convex, inside Q3 <= maxCone,
      does not contain SEP; Phi_1 sends a member outside.
  Controls: with a rotation-invariant sigma neither witness fires; s = 0 (Q3) is preserved.
A mutation self-test runs first; the verdict prints only if every mutation is detected and
every unmutated check passes.
"""
from fractions import Fraction as Fr
import itertools
import sys

MUT = set()
RESULTS = []


def check(ok, cid, text):
    RESULTS.append((bool(ok), cid, text))


class G:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        o = g(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = g(o)
        return G(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return g(o) - self

    def __neg__(self):
        return G(-self.re, -self.im)

    def __mul__(self, o):
        o = g(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = g(o)
        d = o.re * o.re + o.im * o.im
        return self * G(o.re / d, -o.im / d)

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = g(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))


def g(x):
    return x if isinstance(x, G) else G(x, 0)


def zeros(n):
    return [[G() for _ in range(n)] for _ in range(n)]


def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = G(1)
    return M


def mm(A, B):
    return [[sum((A[i][l] * B[l][j] for l in range(len(B))), G()) for j in range(len(B[0]))]
            for i in range(len(A))]


def madd(*Ms):
    return [[sum((M[i][j] for M in Ms), G()) for j in range(len(Ms[0][0]))] for i in range(len(Ms[0]))]


def msc(c, M):
    return [[g(c) * x for x in r] for r in M]


def dag(M):
    return [[M[j][i].conj() for j in range(len(M))] for i in range(len(M[0]))]


def cj(M):
    return [[x.conj() for x in r] for r in M]


def transp(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def kronv(u, v):
    return [a * b for a in u for b in v]


def tr(M):
    return sum((M[i][i] for i in range(len(M))), G())


def quad(M, x):
    return sum((x[i].conj() * M[i][j] * x[j] for i in range(len(x)) for j in range(len(x))), G())


def outer(u, v=None):
    v = u if v is None else v
    return [[a * b.conj() for b in v] for a in u]


def is_psd(M):
    n = len(M)
    if not meq(M, dag(M)):
        return False
    A = [r[:] for r in M]
    for k in range(n):
        d = A[k][k]
        if d.im != 0 or d.re < 0:
            return False
        if d.re == 0:
            if any(not (A[i][k] == 0) for i in range(k + 1, n)):
                return False
            continue
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - A[i][k] * A[k][j] / d
    return True


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def gm(rows):
    return [[g(x) for x in r] for r in rows]


I2 = eye(2)
SX = gm([[0, 1], [1, 0]])
SY = [[G(), G(0, -1)], [G(0, 1), G()]]
SZ = gm([[1, 0], [0, -1]])
PAULI = [I2, SX, SY, SZ]
LAM = G(Fr(3, 5), Fr(4, 5))
D = [[G(1), G()], [G(), LAM]]
SWAP = zeros(4)
for _a, _b in itertools.product(range(2), repeat=2):
    SWAP[2 * _b + _a][2 * _a + _b] = G(1)
CNOT = madd(kron(gm([[1, 0], [0, 0]]), I2), kron(gm([[0, 0], [0, 1]]), SX))


def units4():
    for i, j in itertools.product(range(4), repeat=2):
        E = zeros(4)
        E[i][j] = G(1)
        yield E


def gamma2(M):
    """Partial transpose on the second token; index (a1, a2) -> 2 a1 + a2."""
    out = zeros(4)
    for a1, a2, b1, b2 in itertools.product(range(2), repeat=4):
        out[2 * a1 + a2][2 * b1 + b2] = M[2 * a1 + b2][2 * b1 + a2]
    return out


def gamma1(M):
    out = zeros(4)
    for a1, a2, b1, b2 in itertools.product(range(2), repeat=4):
        out[2 * a1 + a2][2 * b1 + b2] = M[2 * b1 + a2][2 * a1 + b2]
    return out


def ad(U, X):
    return mm(mm(U, X), dag(U))


def phi1(X):
    ID = kron(I2, D)
    w1, w2 = (Fr(1, 2), Fr(1, 2)) if "phi_weights" in MUT else (Fr(5, 8), Fr(3, 8))
    return madd(msc(w1, ad(ID, X)), msc(w2, X))


# ================================================================== R
def sec_r():
    A = [[G(1, 2), G(Fr(1, 3))], [G(0, -1), G(2, 1)]]
    B = [[G(Fr(3, 2)), G(1, -1)], [G(), G(0, Fr(1, 2))]]
    Bc = B if "missing_conj" in MUT else cj(B)
    ok = all(meq(gamma2(ad(kron(A, B), gamma2(E))), ad(kron(A, Bc), E)) for E in units4())
    check(ok, "R1", "Gamma2(Ad_(A(x)B)(Gamma2 Y)) = Ad_(A(x)conj B)(Y) on all 16 matrix units, A, B non-unitary: local congruences (hence local CP maps) preserve Gamma(Q3)")
    ok = all(meq(gamma1(E), transp(gamma2(E))) for E in units4())
    ok &= all(meq(ad(SWAP, gamma2(ad(SWAP, E))), gamma1(E)) for E in units4())
    check(ok, "R2", "Gamma1 = transpose o Gamma2 and SWAP Gamma2(SWAP Y SWAP) SWAP = Gamma1(Y) on all 16 units: Gamma1(Q3) = Gamma2(Q3)")
    prods = [kronv([G(int(a == 0)), G(int(a == 1))], [G(int(b == 0)), G(int(b == 1))]) for a in range(2) for b in range(2)]
    P = [outer(v) for v in prods]
    ok = meq(madd(*P), eye(4)) and all(tr(mm(P[i], P[j])) == (1 if i == j else 0) for i in range(4) for j in range(4))
    check(ok, "R3", "the four computational product projectors sum to I and pair as delta_ij: a 4-element frame in every cone with SEP <= C <= maxCone (they lie in C and in C* >= SEP)")
    # Lorentz similarities: polarized determinant identity on the Pauli basis
    A2 = [[G(2, 1), G(Fr(1, 2))], [G(0, 1), G(1, -3)]]
    c = det2(A2) * det2(A2).conj()

    def bil(X, Y):
        return (det2(madd(X, Y)) - det2(X) - det2(Y)) / 2

    ok = True
    for Xi, Xj in itertools.combinations_with_replacement(PAULI, 2):
        for L in (lambda X: ad(A2, X), lambda X: ad(A2, transp(X))):
            ok &= (bil(L(Xi), L(Xj)) == c * bil(Xi, Xj))
    coords = [[tr(mm(PAULI[mu], transp(PAULI[nu]))) / 2 for nu in range(4)] for mu in range(4)]
    ok &= all(coords[mu][nu] == ((1 if mu != 2 else -1) if mu == nu else 0) for mu in range(4) for nu in range(4))
    check(ok, "R4", "X -> A X A^dag and X -> A X^T A^dag scale the Minkowski form det by |det A|^2 (polarized identity on the Pauli basis); transpose is diag(1,1,-1,1) in Pauli coordinates (improper)")
    plus0 = kronv([G(1), G(1)], [G(1), G()])
    X = msc(Fr(1, 2), outer(plus0))
    CN = madd(kron(I2, gm([[1, 0], [0, 0]])), kron(SX, gm([[0, 0], [0, 1]]))) if "cnot_reversed" in MUT else CNOT
    Bell = ad(CN, X)
    s = [G(), G(1), G(-1), G()]
    v = quad(gamma2(Bell), s)
    ok = (v.re < 0 and v.im == 0) and is_psd(X) and is_psd(Bell)
    check(ok, "R5", f"CNOT|+0> = Bell; <s|Gamma2(Bell)|s> = {v.re} < 0 for s = |01>-|10>, so CNOT maps a product state out of Gamma(Q3); CNOT conjugation preserves Q3")
    ok = all(meq(gamma2(phi1(gamma2(E))), madd(msc(Fr(5, 8), ad(kron(I2, cj(D)), E)), msc(Fr(3, 8), E))) for E in units4())
    check(ok, "R6", "Gamma2 o Phi_1 o Gamma2 = (5/8) Ad_(I(x)conj D) + (3/8) id on all 16 units: Phi_1 preserves Gamma(Q3)")
    Xn = madd(kron(gm([[1, 0], [0, 0]]), msc(Fr(1, 2), I2)), msc(Fr(1, 4), madd(kron(gm([[0, 1], [0, 0]]), I2), kron(gm([[0, 0], [1, 0]]), I2))))
    cd = kronv([G(1), G(-2)], [G(1), G()])
    v = quad(Xn, cd)
    check(v.re < 0, "R7", f"pure-marginal lemma, negative control: zero |1><1| block with a nonzero off-diagonal block gives <cd|X|cd> = {v.re} < 0 at c = (1,-2), d = |0>")


# ================================================================== CX
def sigma(invariant=False):
    if invariant or "invariant_sigma" in MUT:
        return msc(Fr(1, 4), madd(eye(4), msc(Fr(1, 2), kron(I2, SZ))))
    return msc(Fr(1, 4), madd(eye(4), msc(Fr(1, 2), kron(I2, SX))))


def sec_cx():
    sg = sigma()
    s = Fr(1)
    t = s / (1 + s)
    ok = is_psd(sg) and tr(sg) == 1 and not meq(ad(kron(I2, D), sg), sg)
    check(ok, "CX0", "sigma = (I + (1/2) I(x)sigma_x)/4 is a full-rank density matrix and not invariant under Ad_(I(x)D) (unless the invariant-sigma control is selected)") if "invariant_sigma" not in MUT else check(is_psd(sg) and tr(sg) == 1, "CX0", "sigma (control: invariant)")

    def L(Y):                       # C_sigma = L(Q3), L(Y) = Y - t Tr(Y) sigma
        return madd(Y, msc(-t * tr(Y), sg))

    def Linv(X):
        return madd(X, msc(s * tr(X), sg))

    ok = all(meq(L(Linv(E)), E) and meq(Linv(L(E)), E) for E in units4())
    check(ok, "CX1a", "L and X -> X + s Tr(X) sigma are inverse on all 16 units: C_sigma = L(Q3) is a closed convex cone order-isomorphic to Q3")
    # explicit frame and effects for the computational basis (SP certificate for its frames)
    basis = [kronv([G(int(a == 0)), G(int(a == 1))], [G(int(b == 0)), G(int(b == 1))]) for a in range(2) for b in range(2)]
    P = [outer(v) for v in basis]
    Xs = [msc(G(1) / (1 - t), L(Pi)) for Pi in P]
    if "effect_unshifted" in MUT:
        Es = [msc(1, Pi) for Pi in P]
    else:
        Es = [madd(msc(1 - t, Pi), msc(t * tr(mm(Pi, sg)), eye(4))) for Pi in P]
    ok = meq(madd(*Es), eye(4)) and all(tr(mm(Es[j], Xs[i])) == (1 if i == j else 0) for i in range(4) for j in range(4))
    ok &= all(tr(Xi) == 1 for Xi in Xs)
    ok &= all(all(tr(mm(Ej, L(E))) == (1 - t) * tr(mm(Pj, E)) for E in units4()) for Ej, Pj in zip(Es, P))
    check(ok, "CX1b", "frame X_i = L(P_i)/(1-t), effects E_i = (1-t)P_i + t Tr(P_i sigma) I: sum E_i = I, Tr(E_j X_i) = delta, and Tr(E_j L(Y)) = (1-t)Tr(P_j Y) on all units (so E_j, I-E_j lie in C_sigma*)")
    # SEP <= C_sigma (written: p + s sigma >= 0); exact instances, and a member outside maxCone
    prods = [kronv([G(3), G(4)], [G(1), G(0, 1)]), kronv([G(1), G(-1)], [G(5), G(12)]), basis[0]]
    ok = all(is_psd(Linv(outer(v))) for v in prods)
    eps = Fr(1, 20)
    Xbad = madd(outer(basis[0]), msc(-eps, eye(4)))
    ok &= is_psd(Linv(Xbad)) and quad(Xbad, basis[3]).re < 0
    check(ok, "CX1c", "products lie in C_sigma (instances); X = |00><00| - I/20 lies in C_sigma but <11|X|11> = -1/20: C_sigma is not inside maxCone")
    # Phi_1 failure: X = |00><00| - t sigma (so Linv X = |00><00|)
    X = L(P[0])
    ok = is_psd(Linv(X))
    u = kronv([G(), G(1)], [G(1), G(0, 1)])
    val = quad(Linv(phi1(X)), u)
    ok &= (val.im == 0 and val.re < 0)
    check(ok, "CX1d", f"X = L(|00><00|) is in C_sigma, but <u| Linv(Phi_1 X) |u> = {val.re} < 0 for u = |1>(x)(1,i): Phi_1 does not preserve C_sigma")
    # controls: Q3 (s = 0) preserved on this X; invariant sigma gives no failure on this witness
    ok = is_psd(phi1(P[0]))
    sgi = sigma(invariant=True)
    Xi = madd(P[0], msc(-t, sgi))
    vali = quad(madd(phi1(Xi), msc(s * tr(phi1(Xi)), sgi)), u)
    ok &= vali.re >= 0
    check(ok, "CX1e", f"controls: Phi_1(|00><00|) is PSD (Q3, s = 0, preserved); with the invariant sigma' = (I + (1/2)I(x)sigma_z)/4 the same witness gives {vali.re} >= 0")
    # CX2: C'_sigma = {X : X - s2 Tr(X) sigma >= 0}, s2 = 1/2
    s2 = Fr(1, 2)

    def M2(X):
        return madd(X, msc(-s2 * tr(X), sg))

    ok = not is_psd(M2(P[0])) and quad(M2(P[0]), basis[3]).re < 0
    X2 = madd(P[0], msc(s2 / (1 - s2), sg))          # M2(X2) = |00><00| * Tr-scaling
    ok &= is_psd(M2(X2))
    u2 = kronv([G(), G(1)], [G(1), G(0, -1)])
    val2 = quad(M2(phi1(X2)), u2)
    ok &= (val2.im == 0 and val2.re < 0)
    t2 = s2 / (1 - s2)

    def L2(Y):                      # C'_sigma = L2(Q3), L2(Y) = Y + t2 Tr(Y) sigma
        return madd(Y, msc(t2 * tr(Y), sg))

    ok &= all(meq(M2(L2(E)), msc(1, E)) for E in units4())
    check(ok, "CX2", f"C'_sigma = L2(Q3) (inverse identity on all units) lies in Q3, excludes |00><00| (<11|.|11> < 0), contains X2 = |00><00| + sigma, and <u'| M2(Phi_1 X2) |u'> = {val2.re} < 0: Phi_1 does not preserve it")


# ================================================================== CW
def sec_cw():
    """The fidelity cut C_W = {X >= 0 : Tr(W X) >= 0}, W = I/2 - |Phi+><Phi+| (in the domain)."""
    phi = [G(1), G(), G(), G(1)]
    Pphi = msc(Fr(1, 2), outer(phi))
    W = madd(msc(Fr(1, 2), eye(4)), msc(-1, Pphi))
    # SEP <= C_W: product expectations of W equal 1/2 - |<ab|Phi+>|^2 >= 0 (written: max product fidelity 1/2)
    prods = [kronv([G(3), G(4)], [G(1), G(0, 1)]), kronv([G(1), G(1)], [G(1), G(1)]), kronv([G(1), G()], [G(1), G()]),
             kronv([G(1), G(0, 1)], [G(1), G(0, -1)])]
    ok = all(quad(W, v).re >= 0 for v in prods)
    ok &= any(quad(W, v).re == 0 for v in prods)
    check(ok, "CW1", "W = I/2 - Phi+ is nonnegative on sampled product vectors (zero at |+>|+> and |+i>|-i>): SEP <= C_W <= Q3 <= maxCone (written: product fidelity <= 1/2)")
    chi = [G(1), G(), G(), G(0, -1)]
    rho = msc(Fr(1, 2), outer(chi))
    mapped = rho if "phi_identity" in MUT else phi1(rho)
    v0, v1 = tr(mm(W, rho)), tr(mm(W, mapped))
    v2 = tr(mm(W, ad(kron(I2, D), rho)))
    ok = is_psd(rho) and v0 == 0 and v1 == Fr(-1, 4) and v2 == Fr(-2, 5)
    check(ok, "CW2", f"rho = |00 - i 11><00 - i 11|/2 has Tr(W rho) = {v0.re} (in C_W); Tr(W Phi_1 rho) = {v1.re}, Tr(W Ad_(I(x)D) rho) = {v2.re}: Phi_1 does not preserve C_W")
    # SP failure certificate (written argument in report C4): rho_bad = diag(2/5,3/10,1/5,1/10) in {Phi+,|01>,|10>,Phi-}
    phim = [G(1), G(), G(), G(-1)]
    e01 = [G(), G(1), G(), G()]
    e10 = [G(), G(), G(1), G()]
    rb = madd(msc(Fr(2, 5), Pphi), msc(Fr(3, 10), outer(e01)), msc(Fr(1, 5), outer(e10)), msc(Fr(1, 20), outer(phim)))
    ok = is_psd(rb) and tr(rb) == 1 and tr(mm(W, rb)).re >= 0 and quad(W, phi).re < 0
    # M_w = (1 - w/2) I + w Phi+ commutes with rb; eigenvalue lines a_i + b_i w of Y_w never meet on [0, 2)
    lines = [(Fr(2, 5), Fr(1, 5)), (Fr(3, 10), Fr(-3, 20)), (Fr(1, 5), Fr(-1, 10)), (Fr(1, 10), Fr(-1, 20))]
    if "degenerate_spectrum" in MUT:
        lines[1] = (Fr(2, 5), Fr(1, 5))
    for (a1, b1), (a2, b2) in itertools.combinations(lines, 2):
        if b1 == b2:
            ok &= (a1 != a2)
        else:
            w = (a2 - a1) / (b1 - b2)
            ok &= not (0 <= w < 2)
    Mw = lambda w: madd(msc(1 - w / 2, eye(4)), msc(w, Pphi))
    ok &= all(meq(mm(Mw(w), rb), mm(rb, Mw(w))) for w in (Fr(0), Fr(1, 3), Fr(3, 2)))
    check(ok, "CW3", "rho_bad = (2/5)Phi+ + (3/10)|01><01| + (1/5)|10><10| + (1/10)Phi- lies in C_W, commutes with every M_w, and Y_w has simple spectrum for all w in [0,2): its only M_w-orthogonal frame contains Phi+, which is outside C_W (SP fails; written C4)")


SECTIONS = [sec_r, sec_cx, sec_cw]
MUTATIONS = {
    "missing_conj": "R1",
    "phi_weights": "R6",
    "invariant_sigma": "CX1d",
    "effect_unshifted": "CX1b",
    "cnot_reversed": "R5",
    "phi_identity": "CW2",
    "degenerate_spectrum": "CW3",
}


def run():
    RESULTS.clear()
    for sct in SECTIONS:
        sct()
    return list(RESULTS)


def main():
    selftest = []
    for mut, target in MUTATIONS.items():
        MUT.clear()
        MUT.add(mut)
        res = run()
        failed = sorted({cid for ok, cid, _ in res if not ok})
        selftest.append((mut, target, target in failed, failed))
    MUT.clear()
    res = run()
    for ok, cid, text in res:
        print(("PASS " if ok else "FAIL ") + cid + "  " + text)
    print()
    for mut, target, hit, failed in selftest:
        print(("MUTATION-REJECTED " if hit else "MUTATION-MISSED ") + f"{mut}: target {target}; failing {','.join(failed)}")
    n_fail = sum(1 for ok, _, _ in res if not ok)
    n_miss = sum(1 for _, _, hit, _ in selftest if not hit)
    print()
    print(f"checks: {len(res)}, failures: {n_fail}; mutations: {len(selftest)}, missed: {n_miss}")
    if n_fail == 0 and n_miss == 0:
        print("VERDICT SYMRIGID-EXACT: PASS (exact certificates of finite identities and witnesses; the classification is a written argument)")
        return 0
    print("VERDICT SYMRIGID-EXACT: NOT ESTABLISHED (a control failed or a mutation was missed; no reading is drawn)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
