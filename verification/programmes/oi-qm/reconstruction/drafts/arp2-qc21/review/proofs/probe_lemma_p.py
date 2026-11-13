#!/usr/bin/env python3
"""Independent exact probes for Lemma P (DESIGN-DS r9 sec. 6).  Controls/illustrations, not evidence.

Lemma P: every affine self-map Phi(r) = alpha + beta r of O = {|r|_1 <= 1} in R^3 has unit-modulus spectrum
(of beta, algebraic multiplicity) contained in the spectrum of some 3x3 signed permutation matrix.

Everything is exact (fractions + sympy over QQ).  No C-gadget orbit is evaluated.
  (1) the spectra of the 48 signed permutations, and the list of unit multisets that are NOT sub-multisets;
  (2) exhaustive grid hunt: beta columns and alpha on the grid {k/4}, Phi(V0) subset O (V0 = 0, +-e_a);
  (3) random rational hunt with denominators up to 12;
  (4) adversarial families: rotation + projection onto the hexagon / square sections (tightness of the rank-2 case);
      O_h composed with contractions; R60 and S_3 themselves fail Phi(O) subset O;
  (5) the proof's objects on the hexagon example: fixed point, limit idempotent, vertex permutation of Psi(O);
  (6) the hypothesis link used by the design: on U' (F_2^4) the QA family has R-images V0, and
      Lambda_{a,1} = 2 Lambda_0 - Lambda_{a,0}; every affine symplectic bijection of F_2^4 (Sp(4,2) x translations,
      not the gadget) induces Phi with Phi(V0) in O and passes Lemma P's conclusion.
"""
import itertools, random, sys
from fractions import Fraction as Fr
import sympy as sp

lam = sp.symbols('lam')

# ---------- spectra ----------
def unit_multiset(M):
    """Exact multiset of unit-modulus eigenvalues of a rational 3x3 matrix, as sorted tuple of labels."""
    Ms = sp.Matrix(M)
    p = sp.Poly(Ms.charpoly(lam).as_expr(), lam, domain='QQ')
    out = []
    for fac, mult in sp.factor_list(p.as_expr(), lam)[1]:
        f = sp.Poly(fac, lam, domain='QQ')
        d = f.degree()
        c = [sp.Rational(x) for x in f.all_coeffs()]
        c = [x / c[0] for x in c]
        if d == 1:
            root = -c[1]
            if root == 1: out += ['1'] * mult
            elif root == -1: out += ['-1'] * mult
        elif d == 2:
            b, cc = c[1], c[2]
            if cc == 1 and abs(b) < 2:
                lab = {0: 'i', -1: 'e60', 1: 'w'}.get(b, 'irr(t=%s)' % (-b))  # lam^2 - t lam + 1
                # b = -t ; t = 2cos(theta): t=1 -> 60deg (e60), t=-1 -> 120deg (w), t=0 -> 90deg
                out += [lab, lab] * mult
        elif d == 3:
            # irreducible rational cubic: unit roots only if all are (cyclotomic of degree 3 does not exist);
            # a real root of modulus 1 is +-1 (rational, contradiction) ; complex pair on circle forces rational
            # real root = -c3 (product), contradiction with irreducibility.  So none.
            pass
    return tuple(sorted(out))

def signed_perms():
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = [[0] * 3 for _ in range(3)]
            for i, j in enumerate(perm):
                M[j][i] = signs[i]
            yield M

def full_spectrum_labels(M):
    Ms = sp.Matrix(M)
    lab = []
    for fac, mult in sp.factor_list(Ms.charpoly(lam).as_expr(), lam)[1]:
        f = sp.Poly(fac, lam, domain='QQ'); c = f.all_coeffs()
        if f.degree() == 1:
            lab += [{1: '1', -1: '-1'}[int(-c[1])]] * mult
        else:
            b = c[1]; lab += [{0: 'i', -1: 'e60', 1: 'w'}[int(b)]] * (2 * mult)
    return tuple(sorted(lab))

SP_SPECTRA = sorted(set(full_spectrum_labels(M) for M in signed_perms()))

def is_submultiset(a, b):
    from collections import Counter
    ca, cb = Counter(a), Counter(b)
    return all(cb[k] >= v for k, v in ca.items())

def allowed(ms):
    return any(is_submultiset(ms, s) for s in SP_SPECTRA)

# ---------- geometry ----------
V0 = [(0, 0, 0)] + [tuple(s if i == a else 0 for i in range(3)) for a in range(3) for s in (1, -1)]
def l1(v): return sum(abs(x) for x in v)
def apply(alpha, beta, r): return tuple(alpha[i] + sum(beta[i][j] * r[j] for j in range(3)) for i in range(3))
def self_map(alpha, beta): return all(l1(apply(alpha, beta, v)) <= 1 for v in V0)

def main():
    report = {}
    # (1)
    print('signed-permutation spectra (%d distinct):' % len(SP_SPECTRA))
    for s in SP_SPECTRA: print('   ', s)
    cands = set()
    labs = ['1', '-1', 'i', 'w', 'e60']
    for n_real in range(4):
        for reals in itertools.combinations_with_replacement(['1', '-1'], n_real):
            for pair in [None, 'i', 'w', 'e60']:
                ms = list(reals) + ([pair, pair] if pair else [])
                if len(ms) <= 3: cands.add(tuple(sorted(ms)))
    forbidden = sorted(m for m in cands if not allowed(m))
    print('root-of-unity unit multisets (size<=3) NOT sub-multisets:', forbidden)
    assert forbidden == [('-1', 'w', 'w'), ('1', 'e60', 'e60')], forbidden

    # (2) exhaustive grid
    G = [Fr(k, 4) for k in range(-4, 5)]
    cols = [v for v in itertools.product(G, repeat=3)]
    count = 0; viol = 0; spectra_seen = {}; sample_count = {}
    alphas = [(Fr(0),) * 3, (Fr(1, 4), 0, 0), (Fr(1, 4), Fr(1, 4), 0), (Fr(1, 2), 0, 0), (Fr(1, 4), Fr(1, 4), Fr(1, 4))]
    for alpha in alphas:
        ok_cols = [v for v in cols if l1([alpha[i] + v[i] for i in range(3)]) <= 1 and l1([alpha[i] - v[i] for i in range(3)]) <= 1]
        for c0 in ok_cols:
            for c1 in ok_cols:
                for c2 in ok_cols:
                    beta = [[c0[i], c1[i], c2[i]] for i in range(3)]
                    count += 1
                    ms = unit_multiset_fast(beta)
                    spectra_seen[ms] = spectra_seen.get(ms, 0) + 1
                    if ms and (sample_count.get((ms, alpha), 0) < 25):
                        sample_count[(ms, alpha)] = sample_count.get((ms, alpha), 0) + 1
                        PROOF_SAMPLE.append((alpha, beta))
                    if not allowed(ms):
                        viol += 1
                        print('VIOLATION', alpha, beta, ms)
    print('grid {k/4}: %d affine self-maps of O checked over %d alphas, violations = %d' % (count, len(alphas), viol))
    print('   unit multisets seen:', sorted(spectra_seen.items(), key=lambda kv: -kv[1]))
    report['grid'] = (count, viol)

    # (3) random rational
    rnd = random.Random(20261109)
    nrand = 0; vr = 0
    while nrand < 20000:
        den = rnd.randint(1, 12)
        alpha = tuple(Fr(rnd.randint(-den, den), den * 3) for _ in range(3))
        if l1(alpha) > 1: continue
        beta_cols = []
        for a in range(3):
            for _ in range(200):
                v = tuple(Fr(rnd.randint(-den, den), den) for _ in range(3))
                if l1([alpha[i] + v[i] for i in range(3)]) <= 1 and l1([alpha[i] - v[i] for i in range(3)]) <= 1:
                    beta_cols.append(v); break
        if len(beta_cols) < 3: continue
        beta = [[beta_cols[j][i] for j in range(3)] for i in range(3)]
        assert self_map(alpha, beta)
        nrand += 1
        ms = unit_multiset_fast(beta)
        if not allowed(ms):
            vr += 1; print('RANDOM VIOLATION', alpha, beta, ms)
    print('random rational: %d self-maps, violations = %d' % (nrand, vr))
    report['random'] = (nrand, vr)
    # cross-check the fast exact routine against sympy factorization on a sample of the matrices seen
    keys = list(_cache.keys()); rnd.shuffle(keys); mism = 0
    for key in keys[:400]:
        if unit_multiset([[sp.Rational(x.numerator, x.denominator) for x in r] for r in key]) != _cache[key]: mism += 1
    print('fast-vs-sympy spectrum routine mismatches on 400 sampled matrices:', mism); assert mism == 0

    # (4) adversarial families
    def mm(A, B): return [[sum(Fr(A[i][k]) * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
    zero = (Fr(0),) * 3
    R60 = [[Fr(2, 3), Fr(-1, 3), Fr(2, 3)], [Fr(2, 3), Fr(2, 3), Fr(-1, 3)], [Fr(-1, 3), Fr(2, 3), Fr(2, 3)]]
    S3 = [[-x for x in row] for row in R60]
    for name, M in (('R60', R60), ('S_3 = -R60', S3)):
        ms = unit_multiset_fast(M)
        print('%s: self-map of O %s, unit spectrum %s, allowed %s' % (name, self_map(zero, M), ms, allowed(ms)))
        assert not self_map(zero, M) and not allowed(ms)
    # every scaling c*R60 that is a self-map has c <= 3/5 (column l1 = 5/3): no unit spectrum
    print('   max c in {k/60} with c*R60 a self-map:', max(Fr(k, 60) for k in range(61) if self_map(zero, [[Fr(k, 60) * x for x in r] for r in R60])))
    # rank-2 tightness: square section {z=0}, rotate by 90 deg: order-4 pair, allowed
    Psq = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]
    R90 = [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
    Phi_sq = mm(R90, Psq)
    ms = unit_multiset_fast(Phi_sq)
    print('Phi = R90 o proj_xy: self-map %s, unit spectrum %s, allowed %s' % (self_map(zero, Phi_sq), ms, allowed(ms)))
    assert self_map(zero, Phi_sq) and ms == ('i', 'i')
    # an affine example with fixed point p != 0 exercising the fixed-point step: Phi(r) = p + R90 Psq (r - p) shrunk
    # targeted rank-2 search: idempotent Psi(r) = a + Pi r, Pi = I - k phi^T (phi.k = 1), a in span(k);
    # count images Psi(O) inside O that are hexagons (all six Psi(+-e_a) vertices, pairwise non-parallel Pi e_a)
    grid = sorted(set(Fr(n, d) for d in (1, 2, 3, 4, 5, 6) for n in range(-2 * d, 2 * d + 1)))
    small = sorted(set(Fr(n, d) for d in (1, 2, 3) for n in range(-d, d + 1)))
    nidem = 0; nhex = 0; npar = 0
    ks = [k for k in itertools.product([Fr(0), Fr(1), Fr(-1), Fr(1, 2), Fr(2)], repeat=3) if any(k)]
    for k in ks:
        for phi in itertools.product(grid[::2], repeat=3):
            if sum(phi[i] * k[i] for i in range(3)) != 1: continue
            Pi = [[(1 if i == j else 0) - k[i] * phi[j] for j in range(3)] for i in range(3)]
            for s in small:
                av = tuple(s * k[i] for i in range(3))
                imgs = [apply(av, Pi, v) for v in V0[1:]]
                if not all(l1(v) <= 1 for v in imgs): continue
                nidem += 1
                cols = [tuple(Pi[i][a] for i in range(3)) for a in range(3)]
                def par(u, v): return all(u[i] * v[j] == u[j] * v[i] for i in range(3) for j in range(3))
                nonpar = all(not par(cols[x], cols[y]) for x, y in ((0, 1), (0, 2), (1, 2))) and all(any(c) for c in cols)
                # hexagon iff nonparallel and no column is in the closed parallelogram spanned by +-others
                if nonpar:
                    # in the plane, write each column in the basis of the other two: c_a = u c_b + v c_c ;
                    # c_a is a vertex of conv(+-c) iff |u| + |v| > 1
                    import sympy as _s
                    hexa = True
                    for a_, b_, c_ in ((0, 1, 2), (1, 0, 2), (2, 0, 1)):
                        M = _s.Matrix([[cols[b_][i], cols[c_][i]] for i in range(3)])
                        sol = M.solve_least_squares(_s.Matrix(cols[a_])) if False else None
                        A2 = _s.Matrix([[cols[b_][0], cols[c_][0]], [cols[b_][1], cols[c_][1]], [cols[b_][2], cols[c_][2]]])
                        uv = (A2.T * A2).inv() * A2.T * _s.Matrix(cols[a_])
                        if abs(uv[0]) + abs(uv[1]) <= 1: hexa = False
                    if hexa: nhex += 1
                    else: npar += 1
    print('rank-2 idempotents Psi with Psi(O) in O on the grid: %d ; hexagonal images: %d ; non-degenerate quadrilaterals: %d'
          % (nidem, nhex, npar))
    report['hex'] = nhex

    # (5) the proof's objects, exactly, on a sample of grid maps with non-empty unit spectrum (incl. alpha != 0):
    # fixed point p (Cesaro step; here solved exactly in O), spectral projection Pi = u(beta) p_<(beta) (Bezout),
    # Psi(r) = p + Pi (r - p): idempotent, commutes with Phi, Psi(O) in O, and Phi^m = id on Psi(O) (m = order).
    nchk = 0
    for (alpha, beta) in PROOF_SAMPLE:
        B = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in r] for r in beta])
        al = sp.Matrix([sp.Rational(x.numerator, x.denominator) for x in alpha])
        # fixed point in O: solve (I - B) p = al ; pick a solution in O by LP-free search over the solution set
        sol, params = (sp.eye(3) - B).gauss_jordan_solve(al)
        cand = None
        free = list(params)
        vals = [sp.Rational(n, 8) for n in range(-8, 9)]
        for combo in itertools.product(vals, repeat=len(free)):
            pp = sol.subs(dict(zip(free, combo)))
            if sum(abs(x) for x in pp) <= 1: cand = pp; break
        assert cand is not None, 'no fixed point found in O on the search grid'
        p = cand
        cp = sp.Poly(B.charpoly(lam).as_expr(), lam)
        per, rest = sp.Poly(1, lam), sp.Poly(1, lam)
        for fac, mult in sp.factor_list(cp.as_expr(), lam)[1]:
            f = sp.Poly(fac, lam)
            roots_unit = all(abs(complex(z)) > 1 - 1e-12 and abs(complex(z)) < 1 + 1e-12 for z in sp.Poly(f, lam).all_roots()) if f.degree() <= 2 else False
            if roots_unit: per = per * f**mult
            else: rest = rest * f**mult
        s_, t_, g = sp.gcdex(rest.as_expr(), per.as_expr(), lam)
        assert sp.simplify(g - 1) == 0
        def ev(poly_expr):
            P = sp.Poly(poly_expr, lam); M = sp.zeros(3)
            for k, c in enumerate(reversed(P.all_coeffs())): M += c * B**k
            return M
        Pi = ev(sp.expand(s_ * rest.as_expr()))
        assert Pi * Pi == Pi and Pi * B == B * Pi
        assert Pi.rank() == per.degree()
        m = 12   # every allowed root of unity here has order dividing 12
        Psi = lambda r: p + Pi * (r - p)
        Phi = lambda r: al + B * r
        for v in V0:
            r = sp.Matrix(v)
            q = Psi(r)
            assert sum(abs(x) for x in q) <= 1
            assert Psi(Psi(r)) == q and Phi(Psi(r)) == Psi(Phi(r))
            z = q
            for _ in range(m): z = Phi(z)
            assert z == q
        nchk += 1
    print('proof objects checked exactly on %d grid maps (fixed point, Bezout projection, Psi idempotent/commuting/'
          'inside O, Phi^12 = id on Psi(O))' % nchk)

    # (6) the hypothesis link on U'
    states = list(itertools.product([0, 1], repeat=4))   # (z1, x1, z2, x2)
    def fz(s): return s[0]
    def fx(s): return s[1]
    def fy(s): return (s[0] + s[1] + s[2] + s[3]) % 2
    F = {'x': fx, 'y': fy, 'z': fz}
    def R(mu): return tuple(sum(mu[s] * (1 - 2 * F[a](s)) for s in states) for a in 'xyz')
    unif = {s: Fr(1, 16) for s in states}
    QA = {'0': unif}
    for a in 'xyz':
        for b in (0, 1):
            QA[a + str(b)] = {s: (Fr(1, 8) if F[a](s) == b else Fr(0)) for s in states}
    for k, mu in QA.items(): print('   R(Lambda_%s) =' % k, R(mu))
    for a in 'xyz':
        assert all(QA[a + '1'][s] == 2 * unif[s] - QA[a + '0'][s] for s in states)
    # affine symplectic bijections of F_2^4: omega(f,g) = sum f_zi g_xi + f_xi g_zi ; act on configurations
    # enumerate GL(4,2) matrices preserving the symplectic form on configuration space (pairs (z1,x1),(z2,x2))
    Om = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
    def matmul2(A, B): return [[sum(A[i][k] * B[k][j] for k in range(4)) % 2 for j in range(4)] for i in range(4)]
    def T(A): return [list(r) for r in zip(*A)]
    sympl = []
    for bits in itertools.product([0, 1], repeat=16):
        A = [list(bits[4 * i:4 * i + 4]) for i in range(4)]
        if matmul2(matmul2(T(A), Om), A) == Om:
            sympl.append(A)
    print('   |Sp(4,2)| =', len(sympl))
    nmaps = 0; bad = 0; spectra = {}
    for A in sympl:
        for t in itertools.product([0, 1], repeat=4):
            def g(s): return tuple((sum(A[i][j] * s[j] for j in range(4)) + t[i]) % 2 for i in range(4))
            def push(mu):
                out = {s: Fr(0) for s in states}
                for s in states: out[g(s)] += mu[s]
                return out
            img = {k: R(push(mu)) for k, mu in QA.items()}
            alpha = img['0']
            beta = [[img[a + '0'][i] - alpha[i] for a in 'xyz'] for i in range(3)]
            consistent = all(img[k] == apply(alpha, beta, R(QA[k])) for k in QA)
            inO = all(l1(v) <= 1 for v in img.values())
            if not consistent: continue
            nmaps += 1
            ms = unit_multiset_fast(beta)
            spectra[ms] = spectra.get(ms, 0) + 1
            if not (inO and self_map(alpha, beta) and allowed(ms)): bad += 1
    print('   affine symplectic bijections inducing a QA-consistent Phi: %d ; Phi(V0) outside O or W-CL-type spectrum: %d' % (nmaps, bad))
    print('   their unit multisets:', spectra)
    assert viol == 0 and vr == 0 and bad == 0
    print('ALL LEMMA-P PROBES GREEN')

PROOF_SAMPLE = []
_cache = {}
def charpoly_coeffs(b):
    T = b[0][0] + b[1][1] + b[2][2]
    S = (b[0][0]*b[1][1] - b[0][1]*b[1][0]) + (b[0][0]*b[2][2] - b[0][2]*b[2][0]) + (b[1][1]*b[2][2] - b[1][2]*b[2][1])
    D = (b[0][0]*(b[1][1]*b[2][2]-b[1][2]*b[2][1]) - b[0][1]*(b[1][0]*b[2][2]-b[1][2]*b[2][0])
         + b[0][2]*(b[1][0]*b[2][1]-b[1][1]*b[2][0]))
    return T, S, D   # p(l) = l^3 - T l^2 + S l - D

def unit_multiset_fast(beta):
    """Exact: unit-modulus eigenvalues of a rational 3x3 matrix.  A non-real unit pair of a real cubic has
    product 1, so p = (l^2 - t l + 1)(l - D); test that factorization, else count roots +-1 by division."""
    b = [[Fr(x) for x in r] for r in beta]
    key = tuple(tuple(r) for r in b)
    if key in _cache: return _cache[key]
    T, S, D = charpoly_coeffs(b)
    out = []
    t = T - D
    if S == 1 + t * D and abs(t) < 2:
        lab = {Fr(0): 'i', Fr(1): 'e60', Fr(-1): 'w'}.get(t, 'irr(t=%s)' % t)
        out += [lab, lab]
        if abs(D) == 1: out.append('1' if D == 1 else '-1')
    else:
        out2 = []
        for r, lab in ((Fr(1), '1'), (Fr(-1), '-1')):
            c = [Fr(1), -T, S, -D]
            while len(c) > 1:
                q = [c[0]]
                for a in c[1:]: q.append(a + q[-1] * r)
                if q[-1] != 0: break
                out2.append(lab); c = q[:-1]
        out = out2
    res = tuple(sorted(out))
    _cache[key] = res
    return res

if __name__ == '__main__':
    main()
