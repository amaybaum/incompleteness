"""AC probe P3 -- record-writing operations versus reversibility on the observed body (Task 4).
Exact arithmetic (Fraction; sympy rationals for one symbolic identity).  The ball/rebit instrument
used in R1-R3 is an IMPORTED model (Lueders instrument of an unsharp sigma_z test, lambda = 3/5); it
is a control for the shape of the claim, not a source.

  R1  selective branch, normalised: x -> (4x, 4y, 3+5z)/(5+3z).  Maps the unit sphere onto the unit
      sphere (symbolic identity) and violates AffineRespect (witness: poles and centre)
  R2  non-selective (observe-and-forget): (x,y,z) -> (4x/5, 4y/5, z).  Informative (outcome law
      state-dependent) and NOT a body automorphism (inverse leaves the ball)
  R3  the unnormalised branches are linear and sum to R2's map (homogenised 4x4, exact)
  R4  eigenvector lemma behind NG2, generalised to any reversible non-selective instrument
      (written proof in the ledger): five rational unit vectors in general position, homogenised;
      the 4x4 matrices X having all five as eigenvectors are exactly the scalars (solution space of
      (X, lambda_1..5) has dimension 1)
  R5  countercontrol: four vertices of a tetrahedron (a simplex, d+1 points): the solution space has
      dimension 4 -- informative non-disturbing (classical) instruments exist
  R6  countercontrol: the square's four vertices ARE in general position in dimension 2: the
      solution space is the scalars (NG2's hypothesis is general position, not strict convexity)
  R7  independence of substratum and body reversibility, direction 2 (direction 1 is SA's P5(i)):
      Omega = {0,1}^2, f(v,h) = (1-v, 0) is NOT injective; with readout v and the uniform weight,
      every protocol preparation vector (protocols over {obs, idle} up to length 4, read on effects
      up to length 3) lies on the segment spanned by the two pure v-states, and the induced idle map
      is the swap of that segment: an involution, affine, reversible on the body
"""
from fractions import Fraction as Fr
from itertools import product
import sympy as sp

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name + (('  ' + detail) if detail else ''))


def nullity(M):
    M = [row[:] for row in M]
    rows, cols = len(M), len(M[0])
    r = 0
    for cc in range(cols):
        piv = next((i for i in range(r, rows) if M[i][cc] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][cc]
        M[r] = [x / pv for x in M[r]]
        for i in range(rows):
            if i != r and M[i][cc] != 0:
                f = M[i][cc]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return cols - r


# R1
x, y, z = sp.symbols('x y z', real=True)
sel = sp.Matrix([4 * x, 4 * y, 3 + 5 * z]) / (5 + 3 * z)
norm2 = sp.simplify((sel.dot(sel)).subs(x ** 2, 1 - y ** 2 - z ** 2))
check('R1 selective branch maps the unit sphere to the unit sphere (|x\'|^2 = 1 on x^2+y^2+z^2 = 1)',
      sp.simplify(norm2 - 1) == 0, f'|x\'|^2 on sphere = {norm2}')


def selF(p):
    X, Y, Z = p
    d = 5 + 3 * Z
    return (4 * X / d, 4 * Y / d, (3 + 5 * Z) / d)


N_, S_, O_ = (Fr(0), Fr(0), Fr(1)), (Fr(0), Fr(0), Fr(-1)), (Fr(0), Fr(0), Fr(0))
img_mid = selF(O_)
mid_img = tuple((a + b) / 2 for a, b in zip(selF(N_), selF(S_)))
check('R1 selective branch violates AffineRespect (centre = midpoint of poles)', img_mid != mid_img,
      f'image of centre {tuple(map(str, img_mid))} vs midpoint of images {tuple(map(str, mid_img))}')

# R2
lam = Fr(3, 5)
p_plus = lambda p: (1 + lam * p[2]) / 2  # noqa: E731
check('R2 non-selective map informative: P(+) differs on the poles', p_plus(N_) != p_plus(S_),
      f'P(+|N) = {p_plus(N_)}, P(+|S) = {p_plus(S_)}')
ns_inv = lambda p: (p[0] * Fr(5, 4), p[1] * Fr(5, 4), p[2])  # noqa: E731
q = ns_inv((Fr(1), Fr(0), Fr(0)))
check('R2 non-selective map is not a body automorphism: its inverse sends (1,0,0) outside the ball',
      sum(t * t for t in q) > 1, f'|M^-1 (1,0,0)|^2 = {sum(t * t for t in q)}')

# R3 unnormalised branches (homogenised (t, x, y, z), t = trace): Lueders with sqrt(E+-) = diag(2,1)/sqrt5, diag(1,2)/sqrt5
# branch +: t' = (t + lam z)/2 ; x' = (2/5) x ; y' = (2/5) y ; z' = (lam t + z)/2
Bp = [[Fr(1, 2), 0, 0, lam / 2], [0, Fr(2, 5), 0, 0], [0, 0, Fr(2, 5), 0], [lam / 2, 0, 0, Fr(1, 2)]]
Bm = [[Fr(1, 2), 0, 0, -lam / 2], [0, Fr(2, 5), 0, 0], [0, 0, Fr(2, 5), 0], [-lam / 2, 0, 0, Fr(1, 2)]]
S = [[Bp[i][j] + Bm[i][j] for j in range(4)] for i in range(4)]
target = [[1, 0, 0, 0], [0, Fr(4, 5), 0, 0], [0, 0, Fr(4, 5), 0], [0, 0, 0, 1]]
check('R3 unnormalised branches are linear and sum to the non-selective map', S == target)


def hv(p):
    return [Fr(1)] + list(p)


apply4 = lambda B, v: [sum(B[i][k] * v[k] for k in range(4)) for i in range(4)]  # noqa: E731
hn = apply4(Bp, hv((Fr(2, 7), Fr(3, 7), Fr(6, 7))))
sel_check = tuple(t / hn[0] for t in hn[1:]) == selF((Fr(2, 7), Fr(3, 7), Fr(6, 7)))
check('R3 normalising branch + reproduces R1\'s selective map (at (2,3,6)/7)', sel_check)


# R4 / R5 / R6 eigenvector lemma
def eig_system(vecs):
    n = len(vecs[0])
    k = len(vecs)
    # unknowns: X (n*n, row-major), then lambda_1..k ; equations: X v_j - lambda_j v_j = 0
    rows = []
    for j, v in enumerate(vecs):
        for i in range(n):
            row = [Fr(0)] * (n * n + k)
            for m in range(n):
                row[i * n + m] = v[m]
            row[n * n + j] = -v[i]
            rows.append(row)
    return rows


five = [hv(p) for p in [(Fr(0), Fr(0), Fr(1)), (Fr(1), Fr(0), Fr(0)), (Fr(0), Fr(1), Fr(0)),
                        (Fr(2, 7), Fr(3, 7), Fr(6, 7)), (Fr(-2, 3), Fr(-1, 3), Fr(-2, 3))]]
# general position check: every 4 of the 5 homogenised vectors are linearly independent


def det4(M):
    M = [row[:] for row in M]
    n = 4
    d = Fr(1)
    for cc in range(n):
        piv = next((i for i in range(cc, n) if M[i][cc] != 0), None)
        if piv is None:
            return Fr(0)
        if piv != cc:
            M[cc], M[piv] = M[piv], M[cc]
            d = -d
        d *= M[cc][cc]
        for i in range(cc + 1, n):
            f = M[i][cc] / M[cc][cc]
            M[i] = [a - f * b for a, b in zip(M[i], M[cc])]
    return d


gp = all(det4([five[i] for i in range(5) if i != skip]) != 0 for skip in range(5))
check('R4 the five homogenised sphere points are in general position (all 4-subsets independent)', gp)
nl = nullity(eig_system(five))
check('R4 matrices with five general-position eigenvectors: solution space dimension 1 (scalars only)', nl == 1,
      f'nullity = {nl}')
tet = [hv(p) for p in [(Fr(1), Fr(1), Fr(1)), (Fr(1), Fr(-1), Fr(-1)), (Fr(-1), Fr(1), Fr(-1)),
                       (Fr(-1), Fr(-1), Fr(1))]]
nl_t = nullity(eig_system(tet))
check('R5 countercontrol: tetrahedron (simplex) vertices: solution space dimension 4 (diagonal in vertex basis)',
      nl_t == 4, f'nullity = {nl_t}')
sq = [[Fr(1), Fr(a), Fr(b)] for a, b in [(1, 1), (1, -1), (-1, 1), (-1, -1)]]
nl_s = nullity(eig_system(sq))
check('R6 square vertices (general position in d = 2): solution space dimension 1', nl_s == 1, f'nullity = {nl_s}')

# R7 independence toy
Omega = [(v, h) for v in (0, 1) for h in (0, 1)]
f = {(v, h): (1 - v, 0) for (v, h) in Omega}
check('R7 f is not injective', len(set(f.values())) < len(Omega))
mu = {o: Fr(1, 4) for o in Omega}


def run(protocol, omega):
    rec = []
    o = omega
    for st in protocol:
        if st == 'obs':
            rec.append(o[0])
        o = f[o]
    return tuple(rec), o


def protocols(n):
    out = [()]
    for k in range(1, n + 1):
        out += list(product(('obs', 'idle'), repeat=k))
    return out


def posterior(prot, rec):
    w = {}
    for o in Omega:
        r, o2 = run(prot, o)
        if r == rec:
            w[o2] = w.get(o2, Fr(0)) + mu[o]
    tot = sum(w.values())
    return None if tot == 0 else {k: v / tot for k, v in w.items()}


def eff_value(nu, eprot, B):
    return sum(pw for o, pw in nu.items() if run(eprot, o)[0] in B)


effs = []
for ep in protocols(3):
    nobs = sum(1 for t in ep if t == 'obs')
    for r in product((0, 1), repeat=nobs):
        effs.append((ep, frozenset([r])))
preps = []
for pp in protocols(4):
    nobs = sum(1 for t in pp if t == 'obs')
    for r in product((0, 1), repeat=nobs):
        nu = posterior(pp, r)
        if nu is not None:
            preps.append((pp, r, nu))


def pvec(nu):
    return tuple(eff_value(nu, ep, B) for ep, B in effs)


pure0, pure1 = pvec({(0, 0): Fr(1)}), pvec({(1, 0): Fr(1)})
on_seg = True
for pp, r, nu in preps:
    q1 = sum(pw for o, pw in nu.items() if o[0] == 1)
    v = pvec(nu)
    on_seg &= all(v[k] == (1 - q1) * pure0[k] + q1 * pure1[k] for k in range(len(v)))
check('R7 every preparation vector lies on the segment [pure v=0, pure v=1]', on_seg, f'{len(preps)} preparations, {len(effs)} effects')


def idle_img(nu):
    w = {}
    for o, pw in nu.items():
        w[f[o]] = w.get(f[o], Fr(0)) + pw
    return w


swap_ok = all(pvec(idle_img(nu)) == tuple(pure0[k] + pure1[k] - pvec(nu)[k] for k in range(len(effs)))
              for _, _, nu in preps)
check('R7 induced idle map is the affine swap of the segment (x -> pure0 + pure1 - x)', swap_ok)
inv_ok = all(pvec(idle_img(idle_img(nu))) == pvec(nu) for _, _, nu in preps)
check('R7 induced idle map is an involution on the body (reversible) although f is not injective', inv_ok)

nfail = sum(1 for _, ok in results if not ok)
print(f'SUMMARY {len(results) - nfail}/{len(results)} PASS')
print('VERDICT ' + ('record-writing-constraints-hold' if nfail == 0 else 'NOT RENDERED'))
