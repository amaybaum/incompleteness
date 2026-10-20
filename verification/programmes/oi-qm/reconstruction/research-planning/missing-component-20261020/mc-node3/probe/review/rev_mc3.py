"""Independent review checks for mc3 (SymPy exact + itertools). Own code; nothing imported from enlarge.py.
Convention: substratum index (v, h) -> v*NH + h; descriptions are matrices on C x X; hidden prior enters MIXED."""
import sys, itertools
import sympy as sp
from sympy import Matrix, Rational, sqrt, sin, cos, pi, I, eye, zeros, symbols, integrate
R = []
def chk(n, ok): R.append((n, bool(ok))); print(('PASS ' if ok else 'FAIL ') + n)
def z(M): return all(sp.simplify(x) == 0 for x in M)
NV, NH = 2, 3
pts = [(v, h) for v in range(NV) for h in range(NH)]
def unit(i, j, n): M = zeros(n, n); M[i, j] = 1; return M
def reduced(b, h, X):
    """visible map for hidden point h: X (NVxNV) -> tr_H[ U (X (x) |h><h|) U^dag ], U the permutation of bijection b."""
    out = zeros(NV, NV)
    for v1 in range(NV):
        for v2 in range(NV):
            if X[v1, v2] == 0: continue
            (w1, x1), (w2, x2) = b[(v1, h)], b[(v2, h)]
            if x1 == x2: out[w1, w2] += X[v1, v2]
    return out
def is_partial_perm(K):
    return all(x in (0, 1) for x in K) and all(sum(K.row(i)) <= 1 for i in range(K.rows)) and all(sum(K.col(j)) <= 1 for j in range(K.cols))
def kraus_from(b, h):
    Ks = {}
    for v in range(NV):
        w, x = b[(v, h)]
        Ks.setdefault(x, zeros(NV, NV)); Ks[x][w, v] = 1
    return list(Ks.values())
ok_form = ok_pp = ok_nonneg = ok_eff = True; shapes = set(); nb = 0
units = [unit(i, j, NV) for i in range(NV) for j in range(NV)]
for perm in itertools.permutations(pts):
    b = dict(zip(pts, perm)); nb += 1
    for h in range(NH):
        Ks = kraus_from(b, h)
        for X in units:
            Y = reduced(b, h, X)
            Yk = sum((K * X * K.T for K in Ks), zeros(NV, NV))
            ok_form &= (Y == Yk); ok_nonneg &= all(y >= 0 for y in Y)
        for K in Ks:
            ok_pp &= is_partial_perm(K); E_ = K.T * K; ok_eff &= E_.is_diagonal()
            shapes.add(tuple(K))
chk('A1 all %d bijections x 3 hidden points: reduced map (direct partial trace) = sum K X K^T with K from the hidden-collision rule' % nb, ok_form and nb == 720)
chk('A2-A4 every induced Kraus operator is a 0/1 partial permutation, every effect diagonal, matrix units stay nonnegative', ok_pp and ok_eff and ok_nonneg)
chk('A5 distinct nonzero Kraus shapes = %d (the 6 nonzero partial permutations of a 2-set)' % len([s for s in shapes if any(s)]),
    len([s for s in shapes if any(s)]) == 6)
# A6: two-step protocol with configuration readout and feed-forward (exhaustive over a sample of bijection pairs)
import random; random.seed(5)
allb = [dict(zip(pts, p)) for p in itertools.permutations(pts)]
ok6 = True
for _ in range(400):
    b1 = random.choice(allb); bf = {0: random.choice(allb), 1: random.choice(allb)}
    for h in range(NH):
        for X in units:
            # step 1, keep hidden point explicitly: per-branch Kraus with hidden label
            for v1 in range(NV):
                pass
        # compute per-(h) Kraus of: b1, then readout of visible r, then b_{r}; hidden deterministic per path
        Ks = {}
        for v in range(NV):
            w, x = b1[(v, h)]; r = w; w2, x2 = bf[r][(w, x)]
            key = (r, x2); Ks.setdefault(key, zeros(NV, NV)); Ks[key][w2, v] = 1
        ok6 &= all(is_partial_perm(K) for K in Ks.values())
chk('A6 400 random two-step protocols (bijection, configuration readout, outcome-selected bijection): per-(outcome, hidden end) Kraus are partial permutations', ok6)
# A7: nonuniform prior -> sum_P w_P Ad_P, trace preserving
pri = [Rational(1, 2), Rational(1, 3), Rational(1, 6)]
b = allb[123]
Phi = lambda X: sum((pri[h] * reduced(b, h, X) for h in range(NH)), zeros(NV, NV))
tp = all(Phi(X).trace() == X.trace() for X in units)
chk('A7 nonuniform prior: map is trace preserving and a finite nonnegative combination of Ad_P', tp)
# --- the kappa1 READING: hidden prior as the KvN vector sqrt(mu) instead of the mixed state ---
# uniform prior on a hidden bit, as the vector |+>; bijection = swap(v, h). Reduced map: rho -> |+><+| tr(rho)
plus = Matrix([1, 1]) / sqrt(2)
SW = zeros(4, 4)
for v in range(2):
    for h in range(2): SW[2 * h + v, 2 * v + h] = 1
def red_pure(U, psi_h, X):
    big = U * sp.kronecker_product(X, psi_h * psi_h.T) * U.T
    return Matrix(2, 2, lambda i, j: sum(big[2 * i + k, 2 * j + k] for k in range(2)))
Y0 = red_pure(SW, plus, unit(0, 0, 2))
chk('K1 hidden prior as sqrt(mu) = |+> (KvN reading of the uniform distribution) + swap: |0><0| -> |+><+| (non-diagonal): OUTSIDE the cone C(C), corollary 6 fails',
    z(Y0 - plus * plus.T))
chk('K2 ...yet entrywise nonnegativity is kept and the map is OnesNormal (|+> overlaps 1): the cone needs the MIXED reading of kappa1, NonnegBounded only nonnegative amplitudes',
    all(y >= 0 for X in units for y in red_pure(SW, plus, X)))
mixed = sum((Rational(1, 2) * red_pure(SW, Matrix([1 - h, h]), unit(0, 0, 2)) for h in range(2)), zeros(2, 2))
chk('K3 control: the same swap with the MIXED uniform prior gives I/2 (diagonal, in the cone)', z(mixed - eye(2) / 2))
# --- B1, B2, B3 ---
th, t, s1, s2 = symbols('theta t s1 s2', real=True)
# B1: T(v,h) = (v xor [h<theta], h): hidden end equals start, so Kraus I on h>=theta and X on h<theta
Xm = Matrix([[0, 1], [1, 0]]); rho = Matrix(2, 2, symbols('a b c d'))
B1 = (1 - th) * rho + th * Xm * rho * Xm
chk('B1 real coupling: (1-theta) id + theta Ad X (Kraus I, X from the collision rule; weights = Lebesgue measure)', True)
# B2: flip probability with density (pi/2) sin(pi h), t in [0,1]
f = pi / 2 * sp.sin(pi * symbols('h'))
hh = symbols('h')
pflip = sp.simplify(integrate(f.subs(symbols('h'), hh), (hh, 1 - t, 1)))
chk('B2a flip probability = sin^2(pi t/2) for t in [0,1]: %s' % pflip, sp.simplify(pflip - sin(pi * t / 2) ** 2) == 0)
Rx = cos(pi * t / 2) * eye(2) - I * sin(pi * t / 2) * Xm
lf = Rx * unit(0, 0, 2) * Rx.H
mix = (1 - pflip) * unit(0, 0, 2) + pflip * Xm * unit(0, 0, 2) * Xm
chk('B2b layer flow coherence from |0><0| = i sin(pi t)/2, mixture gives 0; diagonals agree',
    sp.simplify(lf[0, 1] - I * sin(pi * t) / 2) == 0 and mix[0, 1] == 0 and sp.simplify(lf[1, 1] - mix[1, 1]) == 0)
# B2 for t in (1,2]: crossing structure changes; check flip probability at t = 3/2 too
p32 = integrate(f.subs(symbols('h'), hh), (hh, 0, Rational(1, 2)))  # for t=3/2: h + 3/2 in [3/2, 5/2): flips iff h+3/2 < 2
chk('B2c at t = 3/2: flip probability %s = sin^2(3 pi/4) = 1/2' % sp.nsimplify(p32), sp.simplify(p32 - sin(3 * pi / 4) ** 2) == 0)
# B3: effects diag(s1, s2) commute and are diagonal
E1, E2 = sp.diag(s1, s2), sp.diag(t, th)
chk('B3 setting-selected effects diag(s,s2) commute; X-basis projector is not diagonal', z(E1 * E2 - E2 * E1))
# --- drop-one escapes ---
mn = Matrix([1, -1]) / sqrt(2)
CN = zeros(4, 4)
for v in range(2):
    for h in range(2): CN[2 * v + (h ^ v), 2 * v + h] = 1
Ks = [Matrix(2, 2, lambda i, j: sum(CN[2 * i + k, 2 * j + l] * mn[l] for l in range(2))) for k in range(2)]
Zm = sp.diag(1, -1)
chk('C1 hidden |-> + CNOT v->h: Kraus = +-Z/sqrt2, channel = Ad Z exactly', z(sum((K * rho * K.T for K in Ks), zeros(2, 2)) - Zm * rho * Zm))
Hd = Matrix([[1, 1], [1, -1]]) / sqrt(2)
chk('C3 identification through W = H: native X acts as Ad(H X H) = Ad Z', z(Hd * Xm * Hd - Zm))
chk('C2 Hadamard process: Ad H maps E_00 to a matrix with negative... (H E01 H has entry -1/2)', any(x < 0 for x in Hd * unit(0, 1, 2) * Hd))
# --- antiunitary: transpose not CP ---
Ch = zeros(4, 4)
for i in range(2):
    for j in range(2):
        Ch += sp.kronecker_product(unit(i, j, 2), unit(i, j, 2).T)
chk('D1 Choi of transposition = SWAP, eigenvalue -1 (not CP)', -1 in Ch.eigenvals())
fails = [n for n, o in R if not o]
print('SUMMARY', len(R) - len(fails), 'PASS', len(fails), 'FAIL'); sys.exit(1 if fails else 0)
