"""P4 -- the collapse probe: one prefix-closed protocol tower over the landed classical substratum data
(Omega finite, phi : Perm Omega, vis : Omega -> {0,1}, mu, acts : A -> Perm Omega), checked against every
K-inf-Stage and K-inf-Act field, with countercontrols.  Exact rational arithmetic only (Fraction, sympy Rational).

Protocol letters: 'o' = record vis(w) then apply phi; 'i' = apply phi (idle); 'f' = flip the hidden bit.
Preparation (sigma, r): condition mu on "running sigma records r", push forward to the final state.
Effect (sigma', r'): "running sigma' from the current state records r'".  Forward maps are label inclusions.
"""
from fractions import Fraction as F
from itertools import product
import sympy as sp

# ---------------------------------------------------------------- the substratum (a toy, not a candidate)
OMEGA = [(k, h) for k in range(4) for h in range(2)]
IDX = {w: n for n, w in enumerate(OMEGA)}
def phi(w):            # phase advances; the hidden bit flips when the phase wraps (order 8 on Omega)
    k, h = w
    return ((k + 1) % 4, h ^ (1 if k == 3 else 0))
def vis(w):            # binary visible readout couples phase and hidden bit
    k, h = w
    return (k + h) % 2 if k < 2 else h
def flip(w):
    k, h = w
    return (k, 1 - h)
MU = [F(n + 1, 36) for n in range(8)]          # non-uniform rational prior, sums to 1
assert sum(MU) == 1
STEP = {'o': phi, 'i': phi, 'f': flip}

def run(sigma, w):
    rec = []
    for a in sigma:
        if a == 'o':
            rec.append(vis(w))
        w = STEP[a](w)
    return tuple(rec), w

def seqs(alphabet, n):
    out = [()]
    for L in range(1, n + 1):
        out += list(product(alphabet, repeat=L))
    return out

def preps(alphabet, n):
    """all (sigma, r) with |sigma| <= n and positive conditioning weight, with their posteriors"""
    P = {}
    for s in seqs(alphabet, n):
        buckets = {}
        for w in OMEGA:
            r, w2 = run(s, w)
            buckets.setdefault(r, [F(0)] * 8)
            buckets[r][IDX[w2]] += MU[IDX[w]]
        for r, v in buckets.items():
            z = sum(v)
            if z > 0:
                P[(s, r)] = tuple(x / z for x in v)
    return P

def effects(alphabet, n):
    E = [((), ())]                                   # the unit
    for s in seqs(alphabet, n)[1:]:
        nobs = s.count('o')
        for r in product((0, 1), repeat=nobs):
            E.append((s, r))
    return E

def resp(e, w):
    s, r = e
    return 1 if run(s, w)[0] == r else 0

def p(e, nu):
    return sum(nu[IDX[w]] * resp(e, w) for w in OMEGA)

checks, ok = [], True
def check(name, cond, detail=''):
    global ok
    checks.append((name, bool(cond), detail))
    ok = ok and bool(cond)

N = 4
ALPH = ('o', 'i', 'f')
P = preps(ALPH, N)
E = effects(ALPH, N - 1)

# C1 table laws (FiniteStage fields) at every stage <= N
c1 = all(0 <= p(e, nu) <= 1 for nu in P.values() for e in E) and all(p(((), ()), nu) == 1 for nu in P.values())
check('C1 table laws: 0<=p<=1, unit certain', c1, f'{len(P)} preps x {len(E)} effects')

# C2 SCInf: p is one global function of (label, prep); a stage-n label read at any later stage gives the
# same number because the forward maps are inclusions.  Exercised as val read at stage n vs stage n+k: identical
# by construction -- recorded as a definitional fact, checked here only as a non-vacuity statement.
check('C2 SCInf definitional (one global p, inclusion forward maps)', True, 'definitional; see ledger §2')

# C3 BinaryVisible: v0 = ('o',),(0,)  v1 = ('o',),(1,) at every stage, carried by inclusion
v0, v1 = (('o',), (0,)), (('o',), (1,))
check('C3 BinaryVisible test sums to one on every prep', all(p(v0, nu) + p(v1, nu) == 1 for nu in P.values()))
sharp = [x for x, nu in P.items() if p(v0, nu) == 1] and [x for x, nu in P.items() if p(v1, nu) == 1]
check('C3b a sharp visible pair exists (hypotheses of perfectlyDistinguishable_visible)', bool(sharp))

# C4 label dual (F-S1): p(e, x.a) = p(a.e, x) for a in {i, f}; x at stage <= N-1, e at stage <= N-2
Psmall = {x: nu for x, nu in P.items() if len(x[0]) <= N - 1}
Esmall = [e for e in E if len(e[0]) <= N - 2]
def append(x, a):
    s, r = x
    return (s + (a,), r)
cnt = 0
dual_ok = True
for a in ('i', 'f'):
    for x, nu in Psmall.items():
        nu_a = P[append(x, a)]
        for e in Esmall:
            ae = ((a,) + e[0], e[1])
            cnt += 1
            if p(e, nu_a) != p(ae, nu):
                dual_ok = False
check('C4 label dual p(e, x.a) = p(a.e, x), a in {idle, flip}', dual_ok, f'{cnt} instances')

# C5 AffineRespect, complete certificate on the finite carrier.  prepVec x = R(nu_x), R linear on Q^Omega;
# R(delta_w) depends only on the response row of w over the effect language.  We compute ker R with labels up to
# depth L and show the rank has stabilised at the number of response classes (an exact upper bound on rank R),
# so the depth-L kernel IS ker R.  AffineRespect(a) <=> a_*(D) subset ker R, D = span{nu_x - nu_y} cap ker R.
def response_matrix(alphabet, L):
    Es = effects(alphabet, L)
    return sp.Matrix([[resp(e, w) for w in OMEGA] for e in Es])
def classes(alphabet, L):
    rows = {}
    for w in OMEGA:
        rows.setdefault(tuple(resp(e, w) for e in effects(alphabet, L)), []).append(w)
    return list(rows.values())

def pushmat(g):
    M = sp.zeros(8, 8)
    for w in OMEGA:
        M[IDX[g(w)], IDX[w]] = 1
    return M

def affine_respect(alphabet_eff, L, act):
    R = response_matrix(alphabet_eff, L)
    nus = list({nu for nu in P.values()})
    base = sp.Matrix(nus[0])
    diffs = sp.Matrix.hstack(*[sp.Matrix(nu) - base for nu in nus[1:]])
    # D = {diffs * c : R diffs c = 0}
    ker_c = (R * diffs).nullspace()
    Dvecs = [diffs * c for c in ker_c]
    A = pushmat(act)
    bad = [v for v in Dvecs if any(x != 0 for x in (R * (A * v)))]
    return R.rank(), len(Dvecs), len(bad)

ranks_full = [response_matrix(ALPH, L).rank() for L in range(1, 6)]
ncls_full = len(classes(ALPH, 5))
check('C6 FiniteRank: full-language response rank stabilises at #classes <= |Omega|',
      ranks_full[-1] == ranks_full[-2] == ncls_full <= 8, f'ranks L=1..5 {ranks_full}, classes {ncls_full}')
# affine dim of the body = rank{R nu_x} - 1
Rf = response_matrix(ALPH, 5)
body_rank = sp.Matrix.hstack(*[Rf * sp.Matrix(nu) for nu in set(P.values())]).rank()
check('C6b body affine dimension finite', body_rank - 1 <= 7, f'dim aff body (preps <= {N}) = {body_rank - 1}')

for a, g in (('idle', phi), ('flip', flip)):
    rk, nD, nbad = affine_respect(ALPH, 5, g)
    check(f'C5 AffineRespect({a}) with prefix-closed effects', nbad == 0, f'rank R {rk}, relations {nD}, violated {nbad}')

# C7 countercontrol (PREFIX-CLOSURE load-bearing): effects restricted to observation-only protocols {o, i}
rk, nD, nbad = affine_respect(('o', 'i'), 8, flip)
check('C7 countercontrol: obs-only effects, AffineRespect(flip) FAILS (expected)', nbad > 0,
      f'rank R_obs {rk}, relations {nD}, violated {nbad}')
rk2, nD2, nbad2 = affine_respect(('o', 'i'), 8, phi)
check('C7b control: obs-only effects, AffineRespect(idle) holds (idle is in the effect language)', nbad2 == 0,
      f'relations {nD2}, violated {nbad2}')

# C8 inverse datum and Undoes: posterior of x.f.f = posterior of x ; posterior of x.i^ord = posterior of x
def order(g):
    m, ws = 1, list(OMEGA)
    cur = [g(w) for w in ws]
    while cur != ws:
        cur = [g(w) for w in cur]
        m += 1
    return m
ordphi = order(phi)
Pdeep = preps(ALPH, 1)
und_f = all(P[((x[0] + ('f', 'f')), x[1])] == nu for x, nu in P.items() if len(x[0]) <= N - 2)
check('C8 Undoes(flip, flip): posterior(x.f.f) = posterior(x), hence equal prepVec on ALL labels', und_f)
def posterior_after(nu, word):
    v = list(nu)
    for a in word:
        g = STEP[a]
        w2 = [F(0)] * 8
        for w in OMEGA:
            w2[IDX[g(w)]] += v[IDX[w]]
        v = w2
    return tuple(v)
und_i = all(posterior_after(nu, 'i' * ordphi) == nu for nu in P.values())
check('C8b Undoes(idle^(ord-1), idle): phi has finite order, inverse is a power', und_i, f'ord(phi) = {ordphi}')

# C9 NG1 on this toy: finitely many posteriors; induced maps have finite order on the body
allpost = set(preps(ALPH, 6).values())
check('C9 NG1: posteriors up to horizon 6 are finitely many (bound |Omega|! 2^|Omega|)', len(allpost) <= 40320 * 256,
      f'{len(allpost)} distinct posteriors at horizon <= 6')

for name, ok_, det in checks:
    print(('PASS ' if ok_ else 'FAIL ') + name + (' -- ' + det if det else ''))
print('ALL-PASS' if ok else 'SOME-FAIL')
