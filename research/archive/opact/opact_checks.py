#!/usr/bin/env python3
"""Exact checks for the OPACT investigation (read-only; models CMP-1's val/prepVec exactly).

CMP-1 definitions mirrored: Label = Σ i, E_i ; Prep = Σ i, P_i ;
val(a, x) = p_k(map_{a.1->k} a.2, map_{x.1->k} x.2) with k = ub(x.1, a.1) (a chain: k = max);
prepVec x = (val(a, x))_a.  All arithmetic is exact (fractions / sympy).
"""
from fractions import Fraction as Fr
from itertools import permutations, product
import sympy as sp

FAILS, N = [], [0]
def check(code, name, cond):
    N[0] += 1
    print(('  OK    ' if cond else '  FAIL  ') + code + ' ' + name)
    if not cond: FAILS.append(code)

class Tower:
    """A chain-indexed directed system 0 <= 1 <= ... with forward maps given per consecutive step."""
    def __init__(self, stages, stepE, stepP):
        self.S, self.stepE, self.stepP = stages, stepE, stepP   # stages[i] = (P list, E list, p(e,x))
    def mapE(self, i, k, e):
        for s in range(i, k): e = self.stepE[s](e)
        return e
    def mapP(self, i, k, x):
        for s in range(i, k): x = self.stepP[s](x)
        return x
    def labels(self): return [(i, e) for i, (P, E, p) in enumerate(self.S) for e in E]
    def preps(self):  return [(i, x) for i, (P, E, p) in enumerate(self.S) for x in P]
    def val(self, a, x):
        k = max(a[0], x[0]); P, E, p = self.S[k]
        return p(self.mapE(a[0], k, a[1]), self.mapP(x[0], k, x[1]))
    def prepVec(self, x): return tuple(self.val(a, x) for a in self.labels())
    def sc_inf(self):
        for i in range(len(self.S) - 1):
            P, E, p = self.S[i]; P2, E2, p2 = self.S[i + 1]
            for e in E:
                for x in P:
                    if p2(self.stepE[i](e), self.stepP[i](x)) != p(e, x): return False
        return True

print('E1  stage-natural table-dual pairs => completion duality, with SC∞ FAILING (classical Z3 model)')
# underlying classical model on Ω = {0,1,2}, operation π = cyclic shift
pi = lambda w: (w + 1) % 3
def push(vec):  # (π x)(ω) = x(π^{-1} ω)
    return tuple(vec[(w - 1) % 3] for w in range(3))
def pull(vec):  # (e∘π)(ω) = e(π ω)
    return tuple(vec[pi(w)] for w in range(3))
def orbit(v, f):
    out, cur = [], v
    for _ in range(3):
        if cur not in out: out.append(cur)
        cur = f(cur)
    return out
# stage i holds preparation vectors (π-closed) and effect labels (tag, base vector), scale s_i on non-unit effects
x0 = (Fr(1), Fr(0), Fr(0)); x1 = (Fr(1, 2), Fr(1, 3), Fr(1, 6)); x2 = (Fr(1, 5), Fr(2, 5), Fr(2, 5))
e0 = (Fr(1), Fr(1, 2), Fr(0)); e1 = (Fr(1, 3), Fr(0), Fr(1)); UNIT = ('u', (Fr(1),) * 3)
P0 = orbit(x0, push); P1 = P0 + orbit(x1, push); P2 = P1 + orbit(x2, push)
Eb0 = orbit(e0, pull); Eb1 = Eb0 + orbit(e1, pull)
E0 = [UNIT] + [('e', v) for v in Eb0]; E1 = [UNIT] + [('e', v) for v in Eb1]; E2 = E1
scale = [Fr(1), Fr(1, 2), Fr(1, 3)]       # cumulative scale at stage i on non-unit effects: breaks SC∞
def mkp(i):
    def p(e, x):
        tag, v = e
        s = Fr(1) if tag == 'u' else scale[i]
        return s * sum(v[w] * x[w] for w in range(3))
    return p
stages = [(P0, E0, mkp(0)), (P1, E1, mkp(1)), (P2, E2, mkp(2))]
T = Tower(stages, [lambda e: e, lambda e: e], [lambda x: x, lambda x: x])
Tp = lambda x: (x[0], push(x[1]))                                # T on Prep (stage-preserving)
Ts = lambda a: (a[0], a[1] if a[1][0] == 'u' else ('e', pull(a[1][1])))   # T* on Label
check('E1a', 'the tower is NOT SC∞ (scale 1, 1/2, 1/3 on carried effects)', not T.sc_inf())
check('E1b', 'stage duality p_i(e, T x) = p_i(T* e, x) at every stage',
      all(p(Ts((i, e))[1], x) == p(e, push(x)) for i, (P, E, p) in enumerate(stages) for e in E for x in P))
check('E1c', 'naturality: forward maps commute with T and T*',
      all(push(x) in stages[i + 1][0] for i in range(2) for x in stages[i][0]))
check('E1d', 'completion duality val(a, T x) = val(T* a, x) for every label and preparation',
      all(T.val(a, Tp(x)) == T.val(Ts(a), x) for a in T.labels() for x in T.preps()))
check('E1e', 'hence prepVec(T x) = prepVec(x) ∘ T* (the induced linear map acts on generators)',
      all(T.prepVec(Tp(x)) == tuple(T.prepVec(x)[T.labels().index(Ts(a))] for a in T.labels()) for x in T.preps()))

print('E2  RESPECT omitted: a preparation map with no affine extension and no dual')
st = (['x0', 'x1', 'xm'], ['u', 'e'],
      lambda e, x: Fr(1) if e == 'u' else {'x0': Fr(0), 'x1': Fr(1), 'xm': Fr(1, 2)}[x])
S2 = Tower([st], [], [])
pv = {x: S2.prepVec((0, x)) for x in st[0]}
mid = tuple((a + b) / 2 for a, b in zip(pv['x0'], pv['x1']))
check('E2a', 'affine relation prepVec xm = (prepVec x0 + prepVec x1)/2 holds', pv['xm'] == mid)
swap = {'x0': 'xm', 'xm': 'x0', 'x1': 'x1'}
img_mid = tuple((a + b) / 2 for a, b in zip(pv[swap['x0']], pv[swap['x1']]))
check('E2b', 'the swap x0<->xm breaks it: (T x0 + T x1)/2 = (1, 3/4) but T xm = (1, 0)',
      img_mid == (Fr(1), Fr(3, 4)) and pv[swap['xm']] == (Fr(1), Fr(0)))
s = {x: pv[x][1] for x in st[0]}; tgt = {x: pv[swap[x]][1] for x in st[0]}
# an affine dual would need tgt = α + β s on s ∈ {0, 1, 1/2}
al = tgt['x0']; be = tgt['x1'] - tgt['x0']
check('E2c', 'no affine functional of the state realizes x ↦ val(e, T x) (no dual effect)',
      al + be * s['xm'] != tgt['xm'])

print('E3  naturality omitted: stage-wise dual pairs that do not commute with the forward maps')
bit = (['f', 't'], ['u', 'v0', 'v1'],
       lambda e, x: Fr(1) if e == 'u' else Fr(1) if (e, x) in (('v0', 'f'), ('v1', 't')) else Fr(0))
B = Tower([bit, bit], [lambda e: e], [lambda x: x])
NOTp = {'f': 't', 't': 'f'}; NOTe = {'u': 'u', 'v0': 'v1', 'v1': 'v0'}
Tn = lambda x: x if x[0] == 0 else (1, NOTp[x[1]])           # T_0 = id, T_1 = NOT
Tns = lambda a: a if a[0] == 0 else (1, NOTe[a[1]])
check('E3a', 'the bit tower is SC∞', B.sc_inf())
check('E3b', 'each stage is table-dual on its own', all(
    bit[2](e, x if i == 0 else NOTp[x]) == bit[2](e if i == 0 else NOTe[e], x)
    for i in (0, 1) for e in bit[1] for x in bit[0]))
check('E3c', 'prepVec <0,f> = prepVec <1,f>: the same completed state', B.prepVec((0, 'f')) == B.prepVec((1, 'f')))
check('E3d', 'but their images differ: T is not well defined on the body',
      B.prepVec(Tn((0, 'f'))) != B.prepVec(Tn((1, 'f'))))
check('E3e', 'and completion duality fails for some label and preparation',
      any(B.val(a, Tn(x)) != B.val(Tns(a), x) for a in B.labels() for x in B.preps()))

print('E4  the dual on labels is not unique, the action on the body is')
Tg = lambda x: (x[0], NOTp[x[1]])
dualA = lambda a: (a[0], NOTe[a[1]])
dualB = lambda a: (0, NOTe[a[1]])                              # same rows, different labels (SC∞)
L = B.labels()
check('E4a', 'both label maps are duals: val(a, T x) = val(T*a, x)',
      all(B.val(a, Tg(x)) == B.val(dualA(a), x) == B.val(dualB(a), x) for a in L for x in B.preps()))
delta = tuple(Fr(1) if b == (1, 'v1') else Fr(0) for b in L)   # a vector of CSpace off the body
phiA = tuple(delta[L.index(dualA(a))] for a in L); phiB = tuple(delta[L.index(dualB(a))] for a in L)
check('E4b', 'the two induced maps differ on the indicator vector of <1,v1> (off the body)', phiA != phiB)
check('E4c', 'and agree on every preparation vector', all(
    tuple(B.prepVec(x)[L.index(dualA(a))] for a in L) == tuple(B.prepVec(x)[L.index(dualB(a))] for a in L)
    for x in B.preps()))

print('E5  FiniteRank (or a continuity premise) omitted: RESPECT holds, no continuous extension')
Nmax = 40
def zstage(n):
    P = ['w'] + ['z%d' % j for j in range(1, n + 1)]; E = ['u'] + ['a%d' % k for k in range(1, n + 1)]
    def p(e, x):
        if e == 'u': return Fr(1)
        if x == 'w': return Fr(0)
        k, j = int(e[1:]), int(x[1:])
        return Fr(1, j) if k == j else Fr(0)
    return (P, E, p)
Z = Tower([zstage(n) for n in range(1, Nmax + 1)], [lambda e: e] * (Nmax - 1), [lambda x: x] * (Nmax - 1))
check('E5a', 'the tower is SC∞', Z.sc_inf())
pw = Z.prepVec((Nmax - 1, 'w'))
pz = {j: Z.prepVec((Nmax - 1, 'z%d' % j)) for j in range(1, Nmax + 1)}
norm = lambda u, v: max(abs(a - b) for a, b in zip(u, v))
check('E5b', '‖prepVec z_n − prepVec w‖ = 1/n for n ≤ 40', all(norm(pz[j], pw) == Fr(1, j) for j in pz))
Mx = sp.Matrix([[c - d for c, d in zip(pz[j], pw)] for j in range(1, Nmax + 1)])
check('E5c', 'the vectors prepVec z_n − prepVec w are linearly independent (rank 40): no affine relation',
      Mx.rank() == Nmax)
check('E5d', 'τ(w) = w, τ(z_n) = z_1 respects all relations, yet ‖τ z_n − τ w‖ = 1 for every n',
      all(norm(pz[1], pw) == 1 for _ in pz))

print('E6  a continuous flow moves a stage effect off any countable family (ball3, rot3)')
t = sp.symbols('t', real=True)
v = sp.Matrix([1, 0, 0]); Rm = sp.Matrix([[sp.cos(-t), -sp.sin(-t), 0], [sp.sin(-t), sp.cos(-t), 0], [0, 0, 1]])
r_tr = sp.simplify((1 + (Rm * v)[0]) / 2)            # seedTransport r (rot3 t) at (1,0,0), r = (1 + v0)/2
check('E6a', 'the transported seed at a fixed state is (1 + cos t)/2, non-constant in t',
      sp.simplify(r_tr - (1 + sp.cos(t)) / 2) == 0 and sp.diff(r_tr, t) != 0)

print('E7  reversibility omitted: a reset respects relations and is not an automorphism')
reset = lambda x: B.prepVec((0, 'f'))
check('E7a', 'the reset sends two distinct body points to one', B.prepVec((0, 'f')) != B.prepVec((0, 't'))
      and reset((0, 'f')) == reset((0, 't')))

print('E8  positive control: the natural dual NOT on the bit tower')
check('E8a', 'completion duality holds', all(B.val(a, Tg(x)) == B.val(dualA(a), x) for a in L for x in B.preps()))
check('E8b', 'the induced map swaps the two pure points and is an involution on the generators',
      B.prepVec(Tg((0, 'f'))) == B.prepVec((0, 't')) and B.prepVec(Tg(Tg((0, 'f')))) == B.prepVec((0, 'f')))

print('E9  divisibility: a one-parameter group acting by permutations of a finite set is trivial')
def sym(n):
    return [tuple(p) for p in permutations(range(n))]
def mul(p, q): return tuple(p[i] for i in q)
def power(p, m):
    r = tuple(range(len(p)))
    for _ in range(m): r = mul(p, r)
    return r
for n in (3, 4):
    G = sym(n); order = len(G); ident = tuple(range(n))
    check('E9.%d' % n, 'in Sym(%d) every |G|-th power is the identity' % n, all(power(g, order) == ident for g in G))

print()
print(('opact_checks: OK -- %d checks, 0 failed' % N[0]) if not FAILS else
      'opact_checks: FAILED %s of %d' % (' '.join(FAILS), N[0]))
