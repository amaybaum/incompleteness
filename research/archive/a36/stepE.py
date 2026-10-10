"""Step E: absorption per orientation; the second-order cone Q = {B(u,u)=0} against the union of the hull tangents:
tangent of Q at generic points of each hull (component test), the factor kernels, and the space of quadrics vanishing on all hulls."""
import pickle, time, random
from lib36 import *
import numpy as np
random.seed(36)
t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); K, LN = A['K'], A['LN']
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
D2 = pickle.load(open('stepD2.pkl', 'rb')); results = [r for r in D2['results'] if r[3]]
def Q(v, w):
    out = []
    for (i, j) in PAIRS:
        re = 0; im = 0; ci = i * N; cj = j * N
        for k, (a, b) in enumerate(C_SIG[(i, j)]):
            p = (v[ci + k] - v[cj + k]) * (w[ci + k] - w[cj + k])
            if p: re += a * p; im += b * p
        out.append(re); out.append(im)
    return out
def Bc(v, w):
    q = Q(v, w); return [dot(l, q) for l in LN]
Def = Tb + Rb                       # 49 representatives of Def = ker DF / gauge
T = Tb
names = ['%s %s' % (k, cp[:2]) for (k, cp, rows, ok, vecs) in results]
# absorption: dim (T + T_o)/T and the union's span
print('absorption by orientation (dim of (T + T_o)/T, with T the two fixed-pairing hulls):')
allT = []
for nm, (k, cp, rows, ok, vecs) in zip(names, results):
    d = rank(GAUGE + T + vecs) - rank(GAUGE + T)
    print('  %-40s dim T_o mod gauge %2d | adds %2d to T' % (nm, rank(GAUGE + vecs) - 31, d))
    allT.append(vecs)
# pairwise intersections of orientation tangents mod gauge
m = len(results)
print('pairwise dim(T_o ∩ T_o\') mod gauge:')
for i in range(m):
    row = []
    for j in range(m):
        di, dj = rank(GAUGE + allT[i]) - 31, rank(GAUGE + allT[j]) - 31
        row.append(di + dj - (rank(GAUGE + allT[i] + allT[j]) - 31))
    print('  ', row)
# component test: at a random rational point u of T_o, dim {v in Def : B(u, v) = 0}
print('second-order cone at generic points of each hull: rank of v -> B(u,v) on Def, and dim T_u Q = 49 - rank (T_o is a component iff dim T_u Q = dim T_o):')
for nm, vecs in zip(names, allT):
    dimo = rank(GAUGE + vecs) - 31
    for trial in range(2):
        u = [sum(random.randint(-3, 3) * v[mm] for v in vecs) for mm in range(256)]
        rows = [Bc(u, e) for e in Def]                      # 49 rows of 64
        rk = rank(rows, 64)
        print('  %-40s trial %d: rank %2d -> dim T_u Q = %2d (dim T_o = %2d) %s' % (nm, trial, rk, 49 - rk, dimo, 'COMPONENT' if 49 - rk == dimo else 'LARGER: %d extra' % (49 - rk - dimo)))
print('(%.0fs)' % (time.time() - t0))
# generic point of Def
u = [sum(random.randint(-3, 3) * v[mm] for v in Def) for mm in range(256)]
rk = rank([Bc(u, e) for e in Def], 64); print('generic u in Def: rank of B(u, .) = %d' % rk)
# full B on Sym^2(Def) in the Def basis, and the quadrics vanishing on every hull (modular rank for the count)
BB = {}
for i in range(49):
    for j in range(i, 49): BB[(i, j)] = Bc(Def[i], Def[j])
print('B on Sym^2(Def) computed (%.0fs)' % (time.time() - t0))
rows = [BB[(i, j)] for i in range(49) for j in range(i, 49)]
print('rank of B: Sym^2(Def) -> coker:', rank(rows, 64))
# coordinates of hull tangents in the Def basis (mod gauge): solve exactly using the adapted basis Gb+Tb+Rb
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
def coords_def(v):
    x = [sum(INV[j][i] * v[PIV[i]] for i in range(80)) for j in range(80)]
    return x[31:]                                          # Def coordinates (drop gauge)
P = 2**61 - 1; P2 = 2**31 - 1
def modrank(rows, p):
    M = [[x % p for x in r] for r in rows]; r = 0; n = len(M[0])
    for c in range(n):
        piv_ = next((i for i in range(r, len(M)) if M[i][c]), None)
        if piv_ is None: continue
        M[r], M[piv_] = M[piv_], M[r]; inv = pow(M[r][c], p - 2, p); M[r] = [x * inv % p for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]; M[i] = [(x - f * y) % p for x, y in zip(M[i], M[r])]
        r += 1
        if r == len(M): break
    return r
# constraint rows: for each hull, for basis t_a, t_b of T_o (coords c_a, c_b in Def): q(t_a,t_b) = sum_{i<=j} q_ij (c_a[i] c_b[j] + c_a[j] c_b[i]) / (1 + [i==j])
idx = {(i, j): n for n, (i, j) in enumerate((i, j) for i in range(49) for j in range(i, 49))}
cons = []
for nm, vecs in zip(names, allT):
    # independent representatives mod gauge
    Rr2, piv2 = rref([v[:] for v in vecs], 256)
    cs = [coords_def(v) for v in vecs]
    for a in range(len(cs)):
        for b in range(a, len(cs)):
            ca, cb = cs[a], cs[b]
            den = 1
            for x in ca + cb: den = den * x.denominator // gcd(den, x.denominator)
            ca = [int(x * den) for x in ca]; cb = [int(x * den) for x in cb]
            row = [0] * 1225
            for i in range(49):
                for j in range(i, 49):
                    row[idx[(i, j)]] = ca[i] * cb[j] + (ca[j] * cb[i] if i != j else 0)
            if any(row): cons.append(row)
print('constraint rows from all hulls:', len(cons), '(%.0fs)' % (time.time() - t0))
r1 = modrank(cons, P); r2 = modrank(cons, P2)
print('rank of the vanishing conditions mod two primes: %d, %d -> quadrics vanishing on every hull: %d (mod-p count)' % (r1, r2, 1225 - r1))
# do the B-components vanish on all hulls (they must), and do they span the space of vanishing quadrics?
Bq = []   # each coker coordinate l gives the quadric u -> l(B(u,u)) with coefficients BB[(i,j)][l] (times 2 for i<j)
for l in range(64):
    Bq.append([BB[(i, j)][l] * (2 if i != j else 1) for i in range(49) for j in range(i, 49)])
print('rank of the 64 B-quadrics mod p:', modrank(Bq, P), '| all B-quadrics satisfy the hull constraints:', all(sum(c * q for c, q in zip(row, bq)) == 0 for row in cons[:2000] for bq in Bq[:8]))
pickle.dump({'BB': BB, 'names': names, 'allT': allT}, open('stepE.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
