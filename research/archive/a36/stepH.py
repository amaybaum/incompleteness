"""Step H: the induced representation on coker(DF) of the transpose-free part of the stabilizer (order 512: product relabellings
and conjugation), its character, isotypic dimensions, and the invariant subspace im B (rank 47) inside coker."""
import pickle, time
from lib36 import *
import numpy as np
t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); LN = A['LN']
E = pickle.load(open('stepE.pkl', 'rb')); BB = E['BB']
C = pickle.load(open('stepC.pkl', 'rb')); elems = C['elems']
# elements without transpose: the theta-action (perm, sign) came from (op, g1, g2); recover op via the pattern: transpose maps (i,j)->(j,i) blocks.
# We stored only (perm, sign); identify transpose-free elements as those mapping every row index set {i*16..i*16+15} to a row index set.
def is_row_preserving(e):
    p, s = e
    for i in range(16):
        rows = set(p[i * 16 + j] // 16 for j in range(16))
        if len(rows) != 1: return False
    return True
sub = [e for e in elems if is_row_preserving(e)]
print('transpose-free subgroup order:', len(sub))
# action on the constraint space R^240 (pairs (i,j), Re/Im): row perm sigma from the theta action, sign s (conjugation)
pair_index = {pr: n for n, pr in enumerate(PAIRS)}
def sigma_of(e):
    p, s = e
    sig = [p[i * 16] // 16 for i in range(16)]; tau = [p[j] % 16 for j in range(16)]
    return sig, tau, s
def phases_of(e):
    """g.SIG = D1 SIG D2 with unimodular diagonal D1, D2 (Gaussian rationals); returns d (row phases) after checking the identity"""
    sig, tau, s = sigma_of(e)
    M = [[None] * 16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            x = SIG[i][j]; M[sig[i]][tau[j]] = x.conj() if s == -1 else x
    e_ = [M[0][j] * SIG[0][j].conj() for j in range(16)]                 # column phases with d_0 = 1
    d = [M[i][0] * SIG[i][0].conj() * e_[0].conj() for i in range(16)]
    assert all(M[i][j] == d[i] * SIG[i][j] * e_[j] for i in range(16) for j in range(16)), 'not a stabilizer element up to phases'
    return d
PH = {}
def act_constraint(e, r):
    """F -> D1 P conj^s(F) P^T D1^*: entry (i,j) -> (sig i, sig j) with the phase d_{sig i} conj(d_{sig j}); r in R^240 -> R^240 (rational)"""
    sig, tau, s = sigma_of(e)
    if e not in PH: PH[e] = phases_of(e)
    d = PH[e]; out = [Fr(0)] * 240
    for n, (i, j) in enumerate(PAIRS):
        i2, j2 = sig[i], sig[j]
        re, im = Fr(r[2 * n]), Fr(r[2 * n + 1])
        if s == -1: im = -im
        ph = d[i2].conj() * d[j2]
        val = G(re, im) * ph
        if i2 < j2: m = pair_index[(i2, j2)]; out[2 * m] += val.a; out[2 * m + 1] += val.b
        else: m = pair_index[(j2, i2)]; out[2 * m] += val.a; out[2 * m + 1] -= val.b
    return out
# control: the action preserves im DF (DF(g theta) = g DF(theta) up to the sign convention) -- check on the DF rows' span
DFt = transpose(DF)      # 256 columns... im DF = span of columns of DF (as vectors in R^240) = span of DFt rows
rk = rank(DFt, 240)
RrD, pD = rref(DFt, 240); imDF = [r[:] for r in RrD]          # basis (rref) of im DF, 176 rows
def in_imDF(v):
    v = [Fr(x) for x in v]
    for i, p in enumerate(pD):
        if v[p] != 0:
            f = v[p]; v = [x - f * y for x, y in zip(v, imDF[i])]
    return all(x == 0 for x in v)
for e in sub[:3] + sub[len(sub)//2:len(sub)//2 + 2] + sub[-3:]:
    assert all(in_imDF(act_constraint(e, c)) for c in imDF), 'im DF not preserved'
print('control: im DF preserved by the transpose-free stabilizer (8 elements, full basis): yes')
# coker coordinates: x(r) = LN^T r; section through 64 unit vectors at columns where LN has full rank
LNm = [list(l) for l in LN]                       # 64 x 240
Rr, piv = rref(LNm, 240); cols = piv[:64]
Msub = [[Fr(LNm[l][c]) for c in cols] for l in range(64)]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(64)] for i in range(64)]
Ri, pv = rref(aug, 128); assert pv == list(range(64)); INV = [r[64:] for r in Ri]
def coker_coords(r):
    x = [dot(l, r) for l in LN]                    # LN^T r
    return x
def rep_coker(e):
    """matrix of e on coker in the LN^T coordinates: for each section vector r_c (unit at column c), x = LN^T (g r_c); the coordinates
    of r_c itself are the columns of Msub; so M_e = X_g Msub^{-1}."""
    cols_img = []
    for c in cols:
        r = [0] * 240; r[c] = 1
        cols_img.append(coker_coords(act_constraint(e, r)))
    Xg = [[Fr(cols_img[c][l]) for c in range(64)] for l in range(64)]          # 64 x 64, column c = coords of g r_c
    return [[sum(Xg[l][c] * INV[c][k] for c in range(64)) for k in range(64)] for l in range(64)]
# characters: conjugacy classes of the subgroup
def compose(e, f):
    p, s = e; q, t = f; return (tuple(p[q[m]] for m in range(256)), s * t)
inv = {}
for e in sub:
    p, s = e; q = [0] * 256
    for m in range(256): q[p[m]] = m
    inv[e] = (tuple(q), s)
classes = []; seen = set()
for e in sub:
    if e in seen: continue
    cl = set(compose(compose(g, e), inv[g]) for g in sub); seen |= cl; classes.append(sorted(cl))
print('subgroup conjugacy classes:', len(classes), '(%.0fs)' % (time.time() - t0))
chi = []
for cl in classes:
    M = rep_coker(cl[0]); chi.append(sum(M[i][i] for i in range(64)))
sizes = [len(c) for c in classes]; order = len(sub)
print('character of coker: trivial-isotypic dim', sum(s * x for s, x in zip(sizes, chi)) / order, '| commutant dim', sum(s * x * x for s, x in zip(sizes, chi)) / order)
# im B inside coker: the span of all BB values (in LN^T coordinates already)
imB = [list(v) for v in BB.values()]
print('rank of im B:', rank(imB, 64))
# invariance of im B under the subgroup (spot check) and its character
Rb_, pb = rref(imB, 64); imB_basis = [[x for x in r] for r in Rb_]
def in_span(v, basis_rref, piv_):
    v = [Fr(x) for x in v]
    for i, p in enumerate(piv_):
        if v[p] != 0:
            f = v[p]; v = [x - f * y for x, y in zip(v, basis_rref[i])]
    return all(x == 0 for x in v)
ok = True
for e in sub[:3] + sub[-3:]:
    M = rep_coker(e)
    for b in imB_basis:
        img = [sum(M[l][k] * b[k] for k in range(64)) for l in range(64)]
        if not in_span(img, Rb_, pb): ok = False
print('im B invariant under the subgroup (spot-check):', ok)
# character on im B: restrict via a complement-free trick: trace on im B = trace of M restricted; compute via basis coordinates
def restrict_trace(M):
    # coordinates of M b_i in the rref basis: solve using pivots
    tr = 0
    for i, b in enumerate(imB_basis):
        img = [sum(M[l][k] * b[k] for k in range(64)) for l in range(64)]
        # coefficient of b_i in img = img[pivot_i] (rref basis has unit pivots and zeros elsewhere in pivot columns)
        tr += img[pb[i]]
    return tr
chiB = [restrict_trace(rep_coker(cl[0])) for cl in classes]
print('character of im B: trivial-isotypic dim', sum(s * x for s, x in zip(sizes, chiB)) / order, '| commutant dim', sum(s * x * x for s, x in zip(sizes, chiB)) / order)
pickle.dump({'classes': classes, 'chi_coker': chi, 'chi_imB': chiB, 'sizes': sizes}, open('stepH.pkl', 'wb'))
print('done (%.0fs)' % (time.time() - t0))
