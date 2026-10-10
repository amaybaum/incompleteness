p = 'probe36_body.py'; t = open(p, encoding='utf-8').read()
a1 = 'zf = [Fr(0)] * 64\nfates = []'
print('anchor found:', t.count(a1))
start = t.index(a1)
end = t.index("print('  (%.0fs)' % (time.time() - t0))\n\nprint()")
new = '''zf = [Fr(0)] * 64
def certificate(v):
    """the obstruction certificate: B(v,v) outside the linear span of B(v,T) and B(T,T) in the cokernel, so no
    correction t in T makes B(v+t, v+t) vanish"""
    Bvv = Bvec(v, v); BvT = [Bvec(v, t) for t in Tco]
    span_rows = [list(r) for r in BvT] + [list(BTT[i][j]) for i in range(26) for j in range(i, 26)]
    return rank(span_rows + [list(Bvv)], 64) > rank(span_rows, 64)
def extension(v):
    """an explicit correction t in T_r with B(v+t, v+t) = 0, found by the linear solve 2B(v,t) = -B(v,v); None when the
    linear system is inconsistent"""
    Bvv = Bvec(v, v); cols = [Bvec(v, y) for y in Cr]
    M = [[2 * cols[k][l] for k in range(len(Cr))] + [-Bvv[l]] for l in range(64)]
    Rm, pv2 = rref(M, len(Cr) + 1)
    if len(Cr) in pv2: return None
    x = [Fr(0)] * len(Cr)
    for i_, p_ in enumerate(pv2): x[p_] = Rm[i_][len(Cr)]
    tr_ = [sum(x[k] * Cr[k][i] for k in range(len(Cr))) for i in range(49)]
    wv = [v[i] + tr_[i] for i in range(49)]
    return Bvec(wv, wv) == zf
random.seed(363)
fates = []; basis_fail = []
for si, V in enumerate(spaces):
    vs = [[Fr(0)] * 26 + [Fr(a) for a in row] for row in V]
    iso = all(Bvec(x, y) == zf for x in vs for y in vs)
    trials = []
    for tr in range(3):
        v = [Fr(0)] * 49
        while all(c == 0 for c in v):
            v = [sum(random.randint(-3, 3) * x[i] for x in vs) for i in range(49)]
        ob = certificate(v)
        trials.append((ob, None if ob else extension(v)))
    basis_fail.append(sum(1 for x in vs if not certificate(x)))
    fates.append((len(V), iso, trials))
check('sector fates (dim, isotropic, at three seeded pseudo-random directions each: (obstructed by certificate, extended by an explicit row-hull correction))', fates,
      [(8, False, [(True, None)] * 3), (8, False, [(True, None)] * 3), (4, True, [(False, True)] * 3), (2, True, [(False, True)] * 3), (1, True, [(False, True)] * 3)])
check('the certificate is direction-dependent: it fails at every structured basis vector of the two 8-dimensional sectors (of 8 each)', basis_fail[:2], [8, 8])
'''
t = t[:start] + new + t[end:]
t = t.replace('import numpy as np\nimport itertools\n', 'import numpy as np\nimport itertools\nimport random\n', 1)
open(p, 'w', encoding='utf-8').write(t)
print('patched')
