"""Thread E -- independent exact replay of the K2 figures (read-only research; not a record).

Integer / Gaussian-integer / Fraction arithmetic only. No floating point, no randomness.
The 32 gates are taken from the K2 builder (copied, not edited); every other object
(Pauli algebra, CNOT transfer matrix, Wigner test, group closure, Lie spans, three-copy test)
is re-implemented here independently of the K2 scripts, as a cross-implementation control.

Sections
  A  the 32 gates: unital / trace-preserving, signed permutations, inverses, G^2 = I
  B  Wigner test by the Pauli algebra (automorphism / antiautomorphism of M_{2^n}),
     cross-checked against the K2 Choi-rank tags; countercontrols
  C  factorization: every admissible G = (D1 (x) D2) CNOT (D3 (x) D4), D_i local sign relabellings;
     countercontrol: non-admissible family members do not factor
  D  closure positivity, exact: integer group closure <G, N(x)I, I(x)N>, integer axis witnesses,
     and a Wigner certificate for every element of every surviving group
  E  Lie closure dimensions (own echelon over Q) and identification with the su(4) image
  F  three copies: pairwise branch rule, parity, and idle extension G (x) id_C
"""
import itertools, sys
from fractions import Fraction as Fr

FAIL = []
def check(name, cond):
    print(('PASS ' if cond else 'FAIL ') + name, flush=True)
    if not cond: FAIL.append(name)

# ---------------------------------------------------------------- Pauli algebra (Gaussian integers)
# single-qubit Paulis as 2x2 matrices over Z[i]; a Gaussian integer is a pair (re, im)
def gmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def gadd(a, b): return (a[0]+b[0], a[1]+b[1])
Z0, ONE, I_ = (0, 0), (1, 0), (0, 1)
NEG = lambda a: (-a[0], -a[1])
PM = [[[ONE, Z0], [Z0, ONE]], [[Z0, ONE], [ONE, Z0]], [[Z0, NEG(I_)], [I_, Z0]], [[ONE, Z0], [Z0, NEG(ONE)]]]
def mm(A, B):
    n = len(A); return [[(lambda s: s)(sum_g([gmul(A[i][k], B[k][j]) for k in range(n)])) for j in range(n)] for i in range(n)]
def sum_g(xs):
    s = Z0
    for x in xs: s = gadd(s, x)
    return s
# single-qubit product table: P_a P_b = ph[a][b] * P_{prod[a][b]}, ph a power of i (0..3)
pow_i = [ONE, I_, NEG(ONE), NEG(I_)]
prod1 = [[0]*4 for _ in range(4)]; ph1 = [[0]*4 for _ in range(4)]
for a in range(4):
    for b in range(4):
        M = mm(PM[a], PM[b])
        for c in range(4):
            for e in range(4):
                if all(M[i][j] == gmul(pow_i[e], PM[c][i][j]) for i in range(2) for j in range(2)):
                    prod1[a][b], ph1[a][b] = c, e
check('single-qubit Pauli table: XY = iZ, YX = -iZ', (prod1[1][2], ph1[1][2], prod1[2][1], ph1[2][1]) == (3, 1, 3, 3))
def digits(idx, n): return [(idx >> (2*(n-1-k))) & 3 for k in range(n)]
def undigits(ds):
    r = 0
    for d in ds: r = r*4 + d
    return r
def ptab(n):
    """n-qubit table: P_a P_b = i^{ph} P_c, index convention a = sum d_k 4^{n-1-k} (first factor most significant)"""
    D = 4**n; prod = [[0]*D for _ in range(D)]; ph = [[0]*D for _ in range(D)]
    for a in range(D):
        da = digits(a, n)
        for b in range(D):
            db = digits(b, n)
            prod[a][b] = undigits([prod1[x][y] for x, y in zip(da, db)])
            ph[a][b] = sum(ph1[x][y] for x, y in zip(da, db)) % 4
    return prod, ph
TAB = {1: ptab(1), 2: ptab(2), 3: ptab(3)}

def cols(G):
    """sparse columns of an integer matrix: col j -> list of (i, G[i][j])"""
    D = len(G); return [[(i, G[i][j]) for i in range(D) if G[i][j] != 0] for j in range(D)]
def morphism(G, n, anti):
    """Phi(P_j) = sum_i G[i][j] P_i, extended complex-linearly.  True iff Phi(P_a P_b) = Phi(P_a) Phi(P_b)
    (anti=False) or Phi(P_b) Phi(P_a) (anti=True) for all Pauli strings a, b.  Exact over Z[i]."""
    prod, ph = TAB[n]; D = 4**n; C = cols(G)
    if all(len(c) == 1 and c[0][1] in (1, -1) for c in C):       # signed permutation: fast exact path
        pi = [c[0][0] for c in C]; sg = [c[0][1] for c in C]
        for a in range(D):
            for b in range(D):
                ab = prod[a][b]
                x, y = (pi[b], pi[a]) if anti else (pi[a], pi[b])
                if prod[x][y] != pi[ab]: return False
                # i^{ph(a,b)} s_ab  ==  s_a s_b i^{ph(x,y)}
                if (ph[a][b] + (0 if sg[ab] == 1 else 2)) % 4 != (ph[x][y] + (0 if sg[a]*sg[b] == 1 else 2)) % 4:
                    return False
        return True
    for a in range(D):
        for b in range(D):
            lhs = {}
            e = ph[a][b]
            for (i, v) in C[prod[a][b]]:
                lhs[i] = gadd(lhs.get(i, Z0), gmul(pow_i[e], (v, 0)))
            rhs = {}
            x, y = (b, a) if anti else (a, b)
            for (c, vc) in C[x]:
                for (d, vd) in C[y]:
                    k = prod[c][d]
                    rhs[k] = gadd(rhs.get(k, Z0), gmul(pow_i[ph[c][d]], (vc*vd, 0)))
            keys = set(lhs) | set(rhs)
            if any(lhs.get(k, Z0) != rhs.get(k, Z0) for k in keys): return False
    return True
def unital(G): return all(G[i][0] == (1 if i == 0 else 0) for i in range(len(G)))
def wig(G, n):
    """'U' unitary symmetry of Q, 'A' antiunitary (T o U), None otherwise"""
    if not unital(G): return None
    if morphism(G, n, False): return 'U'
    if morphism(G, n, True): return 'A'
    return None

def imul(A, B):
    n = len(A); Bt = list(zip(*B))
    return [[sum(x*y for x, y in zip(A[i], Bt[j]) if x and y) for j in range(n)] for i in range(n)]
def ikron(A, B):
    m, n = len(A), len(B)
    return [[A[i//n][j//n]*B[i % n][j % n] for j in range(m*n)] for i in range(m*n)]
def idiag(v): return [[v[i] if i == j else 0 for j in range(len(v))] for i in range(len(v))]
def ident(n): return idiag([1]*n)
def key(A): return tuple(tuple(r) for r in A)
I4 = ident(4); I16 = ident(16)
R = idiag([1, 1, -1, 1])                      # y -> -y : transpose on one qubit, in Bloch coordinates
Nm = idiag([1, 1, -1, -1])                    # the NOT: conjugation by X
T2 = ikron(R, R); PB = ikron(I4, R); PA = ikron(R, I4)
NI = ikron(Nm, I4); IN = ikron(I4, Nm)

# ---------------------------------------------------------------- the CNOT transfer matrix, own code
CNm = [[ONE if (i, j) in [(0, 0), (1, 1), (2, 3), (3, 2)] else Z0 for j in range(4)] for i in range(4)]
def gkron(A, B):
    m, n = len(A), len(B)
    return [[gmul(A[i//n][j//n], B[i % n][j % n]) for j in range(m*n)] for i in range(m*n)]
P2 = [gkron(PM[a], PM[b]) for a in range(4) for b in range(4)]
def dag(A): return [[(A[j][i][0], -A[j][i][1]) for j in range(len(A))] for i in range(len(A))]
def gtr(A): return sum_g([A[i][i] for i in range(len(A))])
def transfer(U):
    D = len(U); out = [[0]*16 for _ in range(16)]
    for j in range(16):
        X = mm(mm(U, P2[j]), dag(U))
        for i in range(16):
            t = gtr(mm(P2[i], X)); assert t[1] == 0 and t[0] % 4 == 0
            out[i][j] = t[0] // 4
    return out
CN = transfer(CNm)
check('own CNOT transfer matrix is a unitary Wigner symmetry (U)', wig(CN, 2) == 'U')
check('countercontrol: T.CNOT is antiunitary (A), PT_B is neither', wig(imul(T2, CN), 2) == 'A' and wig(PB, 2) is None and wig(PA, 2) is None)
check('countercontrol: T (full transpose) is A, identity is U, N(x)I and I(x)N are U', wig(T2, 2) == 'A' and wig(I16, 2) == 'U' and wig(NI, 2) == 'U' and wig(IN, 2) == 'U')
# non-unital / non-Wigner countercontrol: depolarizing-like integer map (kills Bloch part)
dep = idiag([1] + [0]*15)
check('countercontrol: a non-invertible unital map is not Wigner', wig(dep, 2) is None)

# ---------------------------------------------------------------- A: the 32 gates (K2 builder, copied)
import sympy as sp
src = open('replay/k20_classify.py').read().split('# 1. the relations')[0]
_ns = {}
exec(src, _ns)                                 # defines build(M0d, A, K) in its own namespace
build = _ns['build']
sols = [(a1, a2, k1, k2) for a1, a2, k1, k2 in itertools.product((1, -1), repeat=4) if a1*k1 + a2*k2 == 0]
cands = [(m, w) for m in itertools.product((1, -1), repeat=2) for w in sols]
def toint(G): return [[int(G[i, j]) for j in range(16)] for i in range(16)]
Gs = {c: toint(build(c[0], sp.diag(c[1][0], c[1][1]), sp.Matrix([[0, c[1][2]], [c[1][3], 0]]))) for c in cands}
check('A: 32 candidate gates', len(Gs) == 32)
check('A: builder at (M0=I, A=I, K=J) equals the own CNOT transfer matrix',
      toint(build((1, 1), sp.eye(2), sp.Matrix([[0, -1], [1, 0]]))) == CN)
check('A: every gate unital (column u(x)u = e0) and trace-preserving (row u(x)u = e0)',
      all(unital(G) and G[0] == [1]+[0]*15 for G in Gs.values()))
check('A: every gate is a signed permutation matrix', all(imul(G, [list(r) for r in zip(*G)]) == I16 and all(sum(1 for x in r if x) == 1 for r in G) for G in Gs.values()))
gk = {key(G) for G in Gs.values()}
check('A: closed under inverse', all(key([list(r) for r in zip(*G)]) in gk for G in Gs.values()))
check('A: exactly 8 involutions', sum(1 for G in Gs.values() if imul(G, G) == I16) == 8)

# ---------------------------------------------------------------- SO-classes (same orbit routine semantics)
Ls = [idiag([1, x, y, 1]) for x in (1, -1) for y in (1, -1)]
def det_sign(L): return L[1][1]*L[2][2]*L[3][3]
def orbits(group):
    seen = {}; classes = []
    for c in cands:
        if c in seen: continue
        cl = []
        for LA, LB in group:
            L = ikron(LA, LB); H = imul(imul(L, Gs[c]), L)
            for c2 in cands:
                if c2 not in seen and Gs[c2] == H: seen[c2] = len(classes); cl.append(c2)
        classes.append(sorted(set(cl)))
    return classes
Ogrp = [(a, b) for a in Ls for b in Ls]
SOgrp = [(a, b) for a in Ls for b in Ls if det_sign(a) == 1 and det_sign(b) == 1]
co, cs = orbits(Ogrp), orbits(SOgrp)
check('A: 8 O-classes of size 4, 16 SO-classes of size 2', [len(c) for c in co] == [4]*8 and [len(c) for c in cs] == [2]*16)

# ---------------------------------------------------------------- B: Wigner tags, own test vs K2 tags
expected = {0: 'PTB.U.PTB', 1: 'U', 2: '-', 3: '-', 4: 'PTB after U', 5: 'U after PTB', 6: 'A', 7: 'PTB.A.PTB',
            8: 'PTB after U', 9: 'U after PTB', 10: 'A', 11: 'PTB.A.PTB', 12: 'PTB.U.PTB', 13: 'U', 14: '-', 15: '-'}
def tag(G):
    if wig(G, 2) == 'U': return 'U'
    if wig(G, 2) == 'A': return 'A'
    c = wig(imul(imul(PB, G), PB), 2)
    if c == 'U': return 'PTB.U.PTB'
    if c == 'A': return 'PTB.A.PTB'
    if wig(imul(PB, G), 2) == 'U': return 'PTB after U'
    if wig(imul(G, PB), 2) == 'U': return 'U after PTB'
    return '-'
tags = {i: tag(Gs[cs[i][0]]) for i in range(16)}
for i in range(16): print('   SO-class %2d rep %s : %s' % (i, cs[i][0], tags[i]))
check('B: own Pauli-algebra tags equal the K2 Choi-rank tags for all 16 SO-classes', tags == expected)
check('B: tags constant on each SO-class', all(tag(Gs[c]) == tags[i] for i in range(16) for c in cs[i]))
check('B: exactly 4 of 32 gates are unitary', sum(1 for G in Gs.values() if wig(G, 2) == 'U') == 4)

# ---------------------------------------------------------------- C: factorization through CNOT
D4 = [idiag([1, a, b, c]) for a, b, c in itertools.product((1, -1), repeat=3)]
def factorizations(G):
    out = []
    for L1, L2, L3, L4 in itertools.product(D4, repeat=4):
        l12 = [L1[i//4][i//4]*L2[i % 4][i % 4] for i in range(16)]
        l34 = [L3[j//4][j//4]*L4[j % 4][j % 4] for j in range(16)]
        if all(l12[i]*CN[i][j]*l34[j] == G[i][j] for i in range(16) for j in range(16)):
            out.append(tuple(det_sign(L) for L in (L1, L2, L3, L4)))
    return out
fac = {c: factorizations(Gs[c]) for c in cands}
check('C: every one of the 32 gates factors as (D1 (x) D2) CNOT (D3 (x) D4) with local sign relabellings',
      all(len(v) > 0 for v in fac.values()))
# the determinant pattern (det D1, det D2, det D3, det D4) is the invariant content; record the set per SO-class
for i in range(16):
    pats = sorted(set(p for c in cs[i] for p in fac[c]))
    print('   SO-class %2d (%s) determinant patterns (D1,D2,D3,D4): %s' % (i, tags[i], pats))
# countercontrols: family members outside the admissible set do not factor
bad = [(m, w) for m in itertools.product((1, -1), repeat=2) for w in itertools.product((1, -1), repeat=4)
       if w[0]*w[2] + w[1]*w[3] != 0]
nf = []
for m, w in bad:
    Gb = toint(build(m, sp.diag(w[0], w[1]), sp.Matrix([[0, w[2]], [w[3], 0]])))
    nf.append(len(factorizations(Gb)) == 0 and key(Gb) not in gk)
check('C countercontrol: none of the 32 unit-modulus sign members with a1 k1 + a2 k2 != 0 factors', len(bad) == 32 and all(nf))
# the reflection-parity rule: bits o = (det D1, det D2), i = (det D3, det D4) as 0/1
def bits(p): return tuple(int(x == -1) for x in p)
rule = True
for i in range(16):
    for p in set(q for c in cs[i] for q in fac[c]):
        oA, oB, iA, iB = bits(p)
        surv_pred = (oA ^ iA) == (oB ^ iB)
        rule &= surv_pred == (i in (0, 1, 6, 7, 10, 11, 12, 13))
        if surv_pred:
            kind = ('PTB.' if oA ^ oB else '') + ('A' if oA ^ iA else 'U') + ('.PTB' if oA ^ oB else '')
            rule &= kind == tags[i]
check('C: survivors <=> o_A^i_A = o_B^i_B (even reflection parity); type U/A = o_A^i_A; branch Q/PT_B(Q) = o_A^o_B', rule)
G2 = toint(build((1, 1), sp.diag(2, 1), sp.Matrix([[0, -1], [1, 0]])))
check('C countercontrol: a non-unit-modulus member (a1 = 2) admits no factorization', len(factorizations(G2)) == 0)

# ---------------------------------------------------------------- D: closure positivity, exact
def closure_group(G):
    gens = [G, NI, IN]; H = {key(I16): I16}; fr = [I16]
    while fr:
        new = []
        for h in fr:
            for g in gens:
                k = imul(g, h); kk = key(k)
                if kk not in H: H[kk] = k; new.append(k)
        fr = new
    return list(H.values())
axes = []
for i in (1, 2, 3):
    for sg in (1, -1):
        v = [1, 0, 0, 0]; v[i] = sg; axes.append(v)
def axis_min(h):
    best = None
    for s in axes:
        for t in axes:
            st = [s[i]*t[j] for i in range(4) for j in range(4)]
            out = [sum(h[r][c]*st[c] for c in range(16)) for r in range(16)]
            for f in axes:
                for g in axes:
                    v = sum(f[i]*g[j]*out[4*i+j] for i in range(4) for j in range(4))
                    if best is None or v < best[0]: best = (v, s, t, f, g)
    return best
surv, dead = [0, 1, 6, 7, 10, 11, 12, 13], [2, 3, 4, 5, 8, 9, 14, 15]
orders = {}
ok_surv, ok_dead = True, True
for i in range(16):
    H = closure_group(Gs[cs[i][0]]); orders[i] = len(H)
    w = min((axis_min(h) for h in H), key=lambda b: b[0])
    if i in surv:
        reflected = tags[i].startswith('PTB')
        cert = all((wig(imul(imul(PB, h), PB), 2) if reflected else wig(h, 2)) in ('U', 'A') for h in H)
        print('   SO-class %2d survives: |group| = %2d, exact axis minimum %d, every element a Wigner symmetry of %s: %s'
              % (i, len(H), w[0], 'PT_B(Q)' if reflected else 'Q', cert))
        ok_surv &= cert and w[0] == 0
    else:
        print('   SO-class %2d fails:    |group| = %2d, exact axis minimum %d at s,t,f,g = %s' % (i, len(H), w[0], w[1:]))
        ok_dead &= w[0] == -2
check('D: the 8 survivors: every group element is a Wigner symmetry of Q or of PT_B(Q) (exact certificate)', ok_surv)
check('D: the 8 failures: an exact integer witness at value -2 on pure axis states', ok_dead)
check('D: group orders are 8 or 16', set(orders.values()) <= {8, 16})
print('   group orders:', orders)

# ---------------------------------------------------------------- E: Lie closure (own echelon over Q)
class Span:
    def __init__(s): s.rows = {}
    def add(s, v):
        v = [Fr(x) for x in v]
        for p, r in s.rows.items():
            if v[p] != 0:
                f = v[p]; v = [a - f*b for a, b in zip(v, r)]
        p = next((i for i, x in enumerate(v) if x != 0), None)
        if p is None: return False
        pv = v[p]; v = [x/pv for x in v]
        for q in list(s.rows):
            r = s.rows[q]
            if r[p] != 0:
                f = r[p]; s.rows[q] = [a - f*b for a, b in zip(r, v)]
        s.rows[p] = v; return True
def flat(A): return [x for r in A for x in r]
def br(A, B): return [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(imul(A, B), imul(B, A))]
def lie(gens, cap=200):
    S = Span(); basis = []; queue = list(gens)
    while queue:
        g = queue.pop()
        if S.add(flat(g)):
            queue += [br(g, b) for b in basis]; basis.append(g)
            if len(basis) >= cap: break
    return basis, S
def span_dim(mats):
    S = Span(); return sum(1 for m in mats if S.add(flat(m)))
# su(4) image from the Pauli table: ad_{-iP_h}(P_d) = -i (i^{ph(h,d)} - i^{ph(d,h)}) P_{hd}
prod2, ph2 = TAB[2]
su4 = []
for h in range(1, 16):
    M = [[0]*16 for _ in range(16)]
    for d in range(16):
        c = gadd(gmul(NEG(I_), pow_i[ph2[h][d]]), gmul(I_, pow_i[ph2[d][h]]))
        assert c[1] == 0
        M[prod2[h][d]][d] = c[0]
    su4.append(M)
check('E: su(4) image has dimension 15 (own construction, all coefficients real)', span_dim(su4) == 15)
su4PT = [imul(imul(PB, x), PB) for x in su4]
check('E countercontrol: su(4) image and its PT_B conjugate are different 15-dim spans (union dim > 15)', span_dim(su4 + su4PT) > 15)
def lgen(k):
    m = [[0]*4 for _ in range(4)]; a, b = [(2, 3), (3, 1), (1, 2)][k]; m[a][b] = -1; m[b][a] = 1; return m
local = [ikron(lgen(k), I4) for k in range(3)] + [ikron(I4, lgen(k)) for k in range(3)]
check('E: local so(3)+so(3) lies in the su(4) image', span_dim(su4 + local) == 15)
def closure_alg(G):
    pows = [I16]; P = G
    while P != I16: pows.append(P); P = imul(P, G)
    gens = [imul(imul(Pw, x), [list(r) for r in zip(*Pw)]) for Pw in pows for x in local]
    B, _ = lie(gens); return B, len(pows)
ok = True
for i in surv:
    B, o = closure_alg(Gs[cs[i][0]])
    d = len(B); refl = tags[i].startswith('PTB')
    eq = span_dim(B) == 15 and span_dim(B + (su4PT if refl else su4)) == 15
    print('   SO-class %2d: order %d, Lie dim %d, equals %s: %s' % (i, o, d, 'PT_B su(4) PT_B' if refl else 'su(4) image', eq))
    ok &= d == 15 and eq
check('E: all 8 survivors generate exactly the 15-dim su(4) image (or its PT_B conjugate)', ok)
for name, G in [('identity', I16), ('N(x)N', ikron(Nm, Nm))]:
    B, _ = closure_alg(G); check('E negative control %s: Lie dim 6' % name, len(B) == 6)

# ---------------------------------------------------------------- F: three copies
def branch(LA, LB):
    q = wig(ikron(LA, LB), 2) in ('U', 'A'); pt = wig(imul(PB, ikron(LA, LB)), 2) in ('U', 'A')
    assert q != pt
    return 0 if q else 1
tab = {(i, j): branch(D4[i], D4[j]) for i in range(8) for j in range(8)}
check('F: pair branch = [det L_A != det L_B] on all 64 pairs (own Wigner test)',
      all(tab[i, j] == int(det_sign(D4[i]) != det_sign(D4[j])) for i in range(8) for j in range(8)))
seen = set((tab[i, j], tab[j, k], tab[k, i]) for i, j, k in itertools.product(range(8), repeat=3))
odd = [e for e in itertools.product((0, 1), repeat=3) if sum(e) % 2]
check('F: 512 triples: realised assignments are exactly the 4 even ones', sorted(seen) == sorted(e for e in itertools.product((0, 1), repeat=3) if sum(e) % 2 == 0))
check('F: no odd assignment realised', not (set(odd) & seen))
# idle extension: G acts on copies A, B; copy C idle.  Is (G (x) id_C) a symmetry of some relabelled
# tripartite quantum cone (L_A (x) L_B (x) L_C) Q_ABC, i.e. is L^-1 (G (x) I) L a Wigner symmetry of M_8?
I4m = I4
def idle_ok(G):
    GI = ikron(G, I4m); hits = []
    for a, b, c in itertools.product(range(8), repeat=3):
        L = ikron(ikron(D4[a], D4[b]), D4[c])
        w = wig(imul(imul(L, GI), L), 3)
        if w: hits.append((det_sign(D4[a]), det_sign(D4[b]), det_sign(D4[c]), w))
    return sorted(set(hits))
# controls first
check('F control: CNOT (x) id preserves Q_ABC (L = I)', wig(ikron(CN, I4), 3) == 'U')
check('F countercontrol: T_AB (x) id_C is not a Wigner symmetry of Q_ABC', wig(ikron(T2, I4), 3) is None)
check('F control: T_ABC is an antiunitary symmetry of Q_ABC', wig(ikron(T2, R), 3) == 'A')
idle = {}
for i in range(16):
    idle[i] = idle_ok(Gs[cs[i][0]])
    print('   SO-class %2d (%s): relabelled 3-copy cones invariant under G (x) id_C, by (det L_A, det L_B, det L_C, type): %s'
          % (i, tags[i], idle[i] if idle[i] else 'none'))
check('F: unitary and PT_B-conjugated unitary survivors (1, 13, 0, 12) have an invariant relabelled cone',
      all(idle[i] for i in (0, 1, 12, 13)))
check('F: antiunitary survivors (6, 10) and PT_B-conjugated antiunitary survivors (7, 11) have none',
      all(not idle[i] for i in (6, 7, 10, 11)))
check('F: no failing class has one', all(not idle[i] for i in dead))

print()
print('e_exact: %s -- %d failures' % ('OK' if not FAIL else 'FAILED', len(FAIL)))
for f in FAIL: print('  failed:', f)
sys.exit(1 if FAIL else 0)
