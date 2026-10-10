"""Step F: the true Diţă hulls through the point. For each verified orientation, each factor's integrable directions:
a 4x4 Hadamard lies on the Fourier circles F4(a) relabelled (A33's nine circles); a generic factor on one, a real factor
(vertex) on three. A hull = orientation + one circle per factor; its tangent = xi (circle direction of X) + twists + eta_c (circle
directions of Y_c). Exact integrability control on every hull; spans; absorption of R's stabilizer sectors."""
import pickle, time, itertools
from lib36 import *
t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); LN = A['LN']
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
D2 = pickle.load(open('stepD2.pkl', 'rb')); results = [r for r in D2['results'] if r[3]]
C2 = pickle.load(open('stepC2.pkl', 'rb')); spaces = C2['spaces']
S4 = list(itertools.permutations(range(4)))
def deph(M):
    n = len(M); M = [[M[i][j] * M[i][0].conj() for j in range(n)] for i in range(n)]
    return [[M[i][j] * M[0][j].conj() for j in range(n)] for i in range(n)]
def key(M): return tuple(x.key() for r in M for x in r)
G4 = []   # 4x4 gauge: row and column phases
for i in range(4):
    v = [0] * 16
    for k in range(4): v[i * 4 + k] = 1
    G4.append(v)
for k in range(4):
    v = [0] * 16
    for i in range(4): v[i * 4 + k] = 1
    G4.append(v)
def reduce_mod_gauge(d):
    """canonical representative of a 4x4 direction modulo the gauge and sign: reduce against the gauge rref, normalise sign"""
    Rg, pg = rref(G4, 16)
    v = [Fr(x) for x in d]
    for i, p in enumerate(pg):
        if v[p] != 0:
            f = v[p]; v = [x - f * y for x, y in zip(v, Rg[i])]
    nz = next((x for x in v if x != 0), None)
    if nz is None: return None
    if nz < 0: v = [-x for x in v]
    return tuple(v)
def circle_directions(X):
    """the distinct integrable directions of X modulo gauge and sign: one per Fourier circle F4(a)[pi, tau] through X"""
    kX = key(deph(X)); dirs = {}
    cands = set()
    for i in range(4):
        for j in range(4):
            for i2 in range(4):
                for j2 in range(4):
                    cands.add((X[i][j] * X[i2][j2].conj()).key())
    for ak in cands:
        a = G(Fr(ak[0]), Fr(ak[1]))
        if a.norm2() != 1: continue
        Fa = F4(a)
        for pi in S4:
            for tau in S4:
                M = [[Fa[pi[i]][tau[j]] for j in range(4)] for i in range(4)]
                if key(deph(M)) == kX:
                    d = tuple(1 if (pi[i] % 2 == 1 and tau[j] % 2 == 1) else 0 for i in range(4) for j in range(4))
                    r = reduce_mod_gauge(d)
                    if r is not None and r not in dirs: dirs[r] = d
    return list(dirs.values())
def ker4_dim(M):
    rows = []
    for i in range(4):
        for j in range(i + 1, 4):
            re = [Fr(0)] * 16; im = [Fr(0)] * 16
            for k in range(4):
                c = M[i][k] * M[j][k].conj()
                re[i * 4 + k] -= c.b; re[j * 4 + k] += c.b; im[i * 4 + k] += c.a; im[j * 4 + k] -= c.a
            rows.append(intvec(re)); rows.append(intvec(im))
    return 16 - rank(rows, 16)
def factors(H, cp, rows):
    col = {(c, d): cp[c][d] for c in range(4) for d in range(4)}
    row = {(a, b): rows[b][a] for a in range(4) for b in range(4)}
    lam = {}; Y = []
    for c in range(4):
        Yc = []
        for b in range(4):
            i0 = row[(0, b)]; base = [H[i0][col[(c, d)]] for d in range(4)]; Yc.append(base)
            for a in range(4): lam[(a, b, c)] = H[row[(a, b)]][col[(c, 0)]] * base[0].conj()
        Y.append(Yc)
    X = [[lam[(a, 0, c)] for c in range(4)] for a in range(4)]
    return X, Y, row, col
HT = [list(c) for c in zip(*SIG)]
hulls = []   # (name, vecs)
for (kind, cp, rws, ok, _) in results:
    H = SIG if kind == 'column' else HT
    X, Y, row, col = factors(H, cp, rws)
    dX = circle_directions(X); dY = [circle_directions(Yc) for Yc in Y]
    real = lambda M: all(x.b == 0 for r in M for x in r)
    print('%s %s: X real %s ker4 %d circles %d | Y_c real %s ker4 %s circles %s' % (kind, cp[:2], real(X), ker4_dim(X), len(dX), [real(Yc) for Yc in Y], [ker4_dim(Yc) for Yc in Y], [len(d) for d in dY]))
    assert all(len(d) >= 1 for d in dY) and len(dX) >= 1
    for choice in itertools.product(dX, *dY):
        xi = choice[0]; etas = choice[1:]
        vecs = []
        v = [0] * 256
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = xi[a * 4 + c]
        vecs.append(v)
        for c in range(4):
            v = [0] * 256
            for a in range(4):
                for b in range(4):
                    for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = etas[c][b * 4 + d]
            vecs.append(v)
        for c in range(4):
            for b in range(4):
                v = [0] * 256
                for a in range(4):
                    for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = 1
                vecs.append(v)
        if kind == 'row': vecs = [[v[(m % 16) * 16 + m // 16] for m in range(256)] for v in vecs]
        hulls.append(('%s %s' % (kind, cp[:2]), vecs))
print('hulls through the point:', len(hulls), '(%.0fs)' % (time.time() - t0))
def Q(v, w):
    out = []
    for (i, j) in PAIRS:
        re = 0; im = 0; ci = i * N; cj = j * N
        for k, (a, b) in enumerate(C_SIG[(i, j)]):
            p = (v[ci + k] - v[cj + k]) * (w[ci + k] - w[cj + k])
            if p: re += a * p; im += b * p
        out.append(re); out.append(im)
    return out
z240 = [0] * 240
bad = 0
for nm, vecs in hulls:
    if not all(dot(r, v) == 0 for r in DF for v in vecs): bad += 1; print('  NOT in ker DF:', nm)
    if not all(Q(u, v) == z240 for u in vecs for v in vecs): bad += 1; print('  NOT exactly integrable pairwise:', nm)
print('controls: every hull tangent in ker DF and D²F vanishing exactly on each hull: %s (%d failures) (%.0fs)' % ('yes' if bad == 0 else 'NO', bad, time.time() - t0))
dims = sorted(set(rank(GAUGE + v) - 31 for _, v in hulls)); print('hull tangent dims mod gauge:', dims)
allv = [v for _, vecs in hulls for v in vecs]
print('span of all hull tangents mod gauge:', rank(GAUGE + allv) - 31, 'of 49')
T = Tb
# absorption of R's stabilizer sectors: sector V (coords in Rb) is absorbed by hull h iff V ⊂ (T + T_h)/T
def sector_vecs(V): return [[sum(Fr(a[i]) * Rb[i][m] for i in range(23)) for m in range(256)] for a in V]
secs = [sector_vecs(V) for V in spaces]
print('sectors of R (dims):', [len(V) for V in spaces])
absorbed_any = []
for si, sv in enumerate(secs):
    base = rank(GAUGE + T)
    hits = []
    for hi, (nm, vecs) in enumerate(hulls):
        r_h = rank(GAUGE + T + vecs)
        r_hs = rank(GAUGE + T + vecs + sv)
        if r_hs == r_h: hits.append(hi)
    # partial absorption: dim of V ∩ (T+T_h)/T maximal over hulls
    best = 0
    for hi, (nm, vecs) in enumerate(hulls):
        d = rank(GAUGE + T + vecs) + len(sv) - rank(GAUGE + T + vecs + sv)   # dim of the sector's image inside (T+T_h)/T ... (sector maps injectively to R)
        best = max(best, d)
    print('  sector %d (dim %d): absorbed entirely by %d hulls %s; largest single-hull overlap %d' % (si, len(sv), len(hits), sorted(set(hulls[h][0] for h in hits))[:4], best))
pickle.dump({'hulls': hulls, 'secs': secs}, open('stepF.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
