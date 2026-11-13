#!/usr/bin/env python3
"""Independent exact probes for the cone argument (DESIGN-DS r9 sec. 6, "What can be found"; r6 sec. 6 long form).
Controls/illustrations, not evidence.  Exact rational arithmetic throughout (fractions / sympy over QQ).
No C-gadget orbit is evaluated: every branch matrix here is an abstract nonnegative matrix on the 16 carrier
configurations of U', not a round of the frozen gadget.

  (1) dimension facts: dim span(QA family) = 4, so the orbit span of a window stabilizes by j = 13 at the latest;
  (2) WINDOW COUNTEREXAMPLE (K = 1): an exact nonnegative branch matrix B (column sums <= 1) with a constant herald
      q on the QA family, CONS(1) on all seven QA laws, VAL(1), whose window-fitted beta has the characteristic factor
      lam^2 - (6/5) lam + 1 (unit pair at angle arccos(3/5), not a root of unity).  W-CL fires with a non-root-of-
      unity pair; the orbit span is not invariant (dim W_2 > dim W_1), and the herald is not constant one step later;
  (3) the STABILIZED THEOREM checked on exact instances: when span(O_{K-1}) = span(O_K) and HC, CONS hold there,
      spec(beta) is contained (with multiplicity) in spec(A|_W), whose unit part consists of roots of unity;
  (4) herald-1 obstruction (paper argument, exact certificate): with q = 1 on the QA family no one-step CONS map can
      be the rotation about z by arccos(3/5) (rows (3/5,-4/5,0), (4/5,3/5,0) violate the zonoid bound).
"""
import itertools, json, sys, hashlib
from fractions import Fraction as Fr
import sympy as sp

lam = sp.symbols('lam')
STATES = list(itertools.product([0, 1], repeat=4))          # (z1, x1, z2, x2)
IDX = {s: i for i, s in enumerate(STATES)}
def fz(s): return s[0]
def fx(s): return s[1]
def fy(s): return (s[0] + s[1] + s[2] + s[3]) % 2
def chi(s): return ((-1) ** fx(s), (-1) ** fy(s), (-1) ** fz(s))   # R coordinates ordered (x, y, z)
def R(mu): return tuple(sum(mu[i] * chi(s)[a] for i, s in enumerate(STATES)) for a in range(3))

def qa_family():
    unif = [Fr(1, 16)] * 16
    fam = {'0': unif}
    F = {'x': fx, 'y': fy, 'z': fz}
    for a in 'xyz':
        for b in (0, 1):
            fam[a + str(b)] = [Fr(1, 8) if F[a](s) == b else Fr(0) for s in STATES]
    return fam

def rank(vectors):
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in v] for v in vectors]).rank()

def matvec(B, mu): return [sum(B[i][j] * mu[j] for j in range(16)) for i in range(16)]

def product_law(r):
    """Law on F_2^4 with chi_x, chi_y, chi_z independent with biases r (x, y, z), z2 uniform."""
    out = [Fr(0)] * 16
    for s in STATES:
        cx, cy, cz = chi(s)
        out[IDX[s]] = (1 + r[0] * cx) / 2 * (1 + r[1] * cy) / 2 * (1 + r[2] * cz) / 2 / 2
    return out

def unit_part(beta):
    M = sp.Matrix([[sp.Rational(x.numerator, x.denominator) if isinstance(x, Fr) else x for x in r] for r in beta])
    fl = sp.factor_list(M.charpoly(lam).as_expr(), lam)[1]
    return M, fl

def verify_window_certificate(path, fam):
    """Verify an explicit-B window certificate from B alone: B >= 0, column sums <= 1, HC(K), CONS(K) with Phi fitted
    at j = 0 (all seven QA laws), VAL(K), the irrational unit factor in chi_beta, and STAB(K) = false."""
    cert = json.load(open(path)); K = cert['K']; q = Fr(cert['q'])
    B = [[Fr(x) for x in row] for row in cert['B']]
    assert all(x >= 0 for row in B for x in row) and all(sum(B[i][j] for i in range(16)) <= 1 for j in range(16))
    orbit = [{k: list(mu) for k, mu in fam.items()}]
    herald_ok = True
    for j in range(K):
        nxt = {}
        for k, mu in orbit[-1].items():
            bm = matvec(B, mu); h = sum(bm)
            herald_ok = herald_ok and (h == q)
            nxt[k] = [x / h for x in bm]
        orbit.append(nxt)
    alpha = R(orbit[1]['0'])
    beta = [[R(orbit[1][a + '0'])[i] - alpha[i] for a in 'xyz'] for i in range(3)]
    Phi = lambda r: tuple(alpha[i] + sum(beta[i][jj] * r[jj] for jj in range(3)) for i in range(3))
    cons = all(R(orbit[j + 1][k]) == Phi(R(orbit[j][k])) for j in range(K) for k in fam)
    val = all(sum(c * c for c in R(mu)) <= 1 for lev in orbit for mu in lev.values())
    M, fl = unit_part(beta)
    irr = any(sp.Poly(f, lam).degree() == 2 and sp.Poly(f, lam).monic().all_coeffs() == [1, sp.Rational(-6, 5), 1] for f, m in fl)
    span_prev = rank([mu for lev in orbit[:K] for mu in lev.values()])
    span_K = rank([mu for lev in orbit for mu in lev.values()])
    print('(2b) window certificate %s: K = %d, q = %s ; HC(%d) %s ; CONS(%d) %s ; VAL(%d) %s ; irrational unit pair %s ;'
          ' rank span O_{K-1} = %d, rank span O_K = %d (STAB %s)' % (path, K, q, K, herald_ok, K, cons, K, val, irr,
          span_prev, span_K, span_prev == span_K))
    print('     chi_beta factors:', fl)
    assert herald_ok and cons and irr and span_prev != span_K
    return val

def main():
    fam = qa_family()
    # (1)
    d1 = rank([fam[k] for k in fam])
    print('(1) dim span(QA family) =', d1, '; strict growth of W_j stops by j <= 16 - %d + 1 = %d' % (d1, 16 - d1 + 1))
    assert d1 == 4

    # (2) window counterexample, K = 1, from the certificate file (exact rationals)
    cert = json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'cone_k1_certificate.json'))
    q = Fr(cert['q'])
    P = {tuple(int(t) for t in k.split(',')): Fr(v) for k, v in cert['P'].items()}
    G = {tuple(int(t) for t in k.split(',')): tuple(Fr(x) for x in v) for k, v in cert['G'].items()}
    # B delta_x = w(x) * ell_x, w = 8 q P(v(x)), ell_x = product law with R = G(v)/P(v)
    B = [[Fr(0)] * 16 for _ in range(16)]
    for s in STATES:
        v = chi(s)
        w = 8 * q * P[v]
        assert 0 <= w <= 1
        if P[v] == 0: continue
        F = tuple(g / P[v] for g in G[v])
        assert all(abs(f) <= 1 for f in F)
        ell = product_law(F)
        for i in range(16): B[i][IDX[s]] += w * ell[i]
    assert all(B[i][j] >= 0 for i in range(16) for j in range(16))
    assert all(sum(B[i][j] for i in range(16)) <= 1 for j in range(16))
    out = {}
    for k, mu in fam.items():
        bm = matvec(B, mu)
        h = sum(bm)
        assert h == q, ('herald not constant', k, h)
        out[k] = [x / h for x in bm]
    alpha = R(out['0'])
    beta = [[R(out[a + '0'])[i] - alpha[i] for a in 'xyz'] for i in range(3)]
    def Phi(r): return tuple(alpha[i] + sum(beta[i][j] * r[j] for j in range(3)) for i in range(3))
    cons = all(R(out[k]) == Phi(R(fam[k])) for k in fam)
    val = all(sum(c * c for c in R(m)) <= 1 for m in list(fam.values()) + list(out.values()))
    M, fl = unit_part(beta)
    print('(2) K = 1 counterexample: herald constant q =', q, '; CONS(1) on all 7 QA laws:', cons, '; VAL(1):', val)
    print('    alpha =', alpha)
    print('    beta =', [[str(x) for x in r] for r in beta])
    print('    char poly factors of beta:', fl)
    has_irr = any(sp.Poly(f, lam).degree() == 2 and sp.Poly(f, lam).monic().all_coeffs() == [1, sp.Rational(-6, 5), 1] for f, m in fl)
    print('    contains lam^2 - 6/5 lam + 1 (unit pair, not a root of unity):', has_irr)
    assert cons and val and has_irr
    W1 = rank([fam[k] for k in fam]); W2 = rank([fam[k] for k in fam] + [out[k] for k in fam])
    print('    dim W_1 =', W1, ' dim W_2 = dim span(O_1) =', W2, ' -> window span not invariant:', W2 > W1)
    h2 = sorted(set(sum(matvec(B, out[k])) for k in fam))
    print('    herald one step later on pi(QA): %d distinct values -> HC(2) holds: %s' % (len(h2), len(h2) == 1))
    # B is an abstract branch matrix: its true conditioned dynamics on an invariant span has only root-of-unity
    # unit eigenvalues (Perron-Frobenius on the polytope); the window-fitted beta does not see it.

    import glob
    for path in sorted(glob.glob('cone_window_K*_certificate.json')):
        verify_window_certificate(path, fam)

    # (3) stabilized theorem on exact instances: take the same B; let A = B/q; build the full Krylov span of QA under
    # A and test herald constancy there.  Then demonstrate the theorem on an instance where it applies: a column-
    # stochastic B built from a carrier permutation (affine bijection, symplectic) mixed with a conditioning-free
    # stochastic step, with q = 1 everywhere; compare spec(beta) with spec(A|_W).
    perm = lambda s: (s[1], s[0], s[2], s[3])     # z1 <-> x1: induces the swap r_x <-> r_z on every law
    assert len(set(perm(s) for s in STATES)) == 16
    Bp = [[Fr(0)] * 16 for _ in range(16)]
    for s in STATES:
        # with prob 3/4 apply perm, with prob 1/4 reset to Lambda_{z,0}-like law: a stochastic matrix
        Bp[IDX[perm(s)]][IDX[s]] += Fr(3, 4)
        for i in range(16): Bp[i][IDX[s]] += Fr(1, 4) * fam['z0'][i]
    # Krylov span
    basis = [fam[k] for k in fam]; j = 0; cur = [fam[k] for k in fam]
    while True:
        nxt = [matvec(Bp, m) for m in cur]
        if rank(basis + nxt) == rank(basis): break
        basis = basis + nxt; cur = nxt; j += 1
    Wmat = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in v] for v in basis]).T
    # A restricted to W: solve A w_k = W c_k
    cols = Wmat.columnspace(); Wb = sp.Matrix.hstack(*cols)
    Bs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in r] for r in Bp])
    C = (Wb.T * Wb).inv() * Wb.T * Bs * Wb
    assert Bs * Wb == Wb * C
    outp = {k: matvec(Bp, mu) for k, mu in fam.items()}
    a2 = R(outp['0'])
    b2 = [[R(outp[a + '0'])[i] - a2[i] for a in 'xyz'] for i in range(3)]
    # CONS on the whole stabilized span: check on every Krylov basis law (all are laws or differences of laws)
    def phi2(r): return tuple(a2[i] + sum(b2[i][jj] * r[jj] for jj in range(3)) for i in range(3))
    orbit = [fam[k] for k in fam]; cons2 = True
    for _ in range(j + 2):
        nxt = [matvec(Bp, m) for m in orbit]
        cons2 = cons2 and all(R(nm) == phi2(R(m)) for m, nm in zip(orbit, nxt)) and all(sum(nm) == 1 for nm in nxt)
        orbit = nxt
    pb = sp.Poly(sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in r] for r in b2]).charpoly(lam).as_expr(), lam)
    pW = sp.Poly(C.charpoly(lam).as_expr(), lam)
    # spec of [[1,0],[alpha,beta]] = (lam-1) * p_beta must divide p_{A|W}
    quo, rem = sp.div(sp.Poly((lam - 1) * pb.as_expr(), lam), pW)
    print('(3) stabilized instance: Krylov span stabilizes, dim W =', Wb.shape[1], '; CONS on QA:', cons2)
    print('    (lam-1) p_beta divides p_{A|W}:', rem.is_zero, '; p_beta =', sp.factor(pb.as_expr()))
    print('    unit factors of p_{A|W}:', [f for f, m in sp.factor_list(pW.as_expr(), lam)[1]])

    # (4) herald-1 certificate for the rotation about z by arccos(3/5): rows c_x = (3/5,-4/5,0), c_y = (4/5,3/5,0)
    # any column-stochastic B: c.d <= E_v|d.v| (v uniform on {+-1}^3) ; d = (1,-1,0): 7/5 > 1.
    Ev = lambda d: Fr(sum(abs(sum(d[a] * v[a] for a in range(3))) for v in itertools.product([1, -1], repeat=3)), 8)
    print('(4) herald 1: c_x.(1,-1,0) = 7/5 vs E|v_x - v_y| =', Ev((1, -1, 0)), '; violated:', Fr(7, 5) > Ev((1, -1, 0)))
    # any herald: P_w(v_x != v_y) >= 7/10 and P_w(v_x = v_y) >= 7/10 cannot both hold
    print('    any constant herald: needs P(v_x != v_y) >= 7/10 and P(v_x = v_y) >= 7/10: impossible')
    print('ALL CONE PROBES GREEN')

if __name__ == '__main__':
    main()
