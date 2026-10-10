"""Step F2: are the second-order extendable residual directions (sectors 2,3,4 with their Diţă corrections) inside a known hull?
Also: each obstructed sector against the hull list."""
import pickle, time, random
from lib36 import *
random.seed(363); t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); LN = A['LN']
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
E = pickle.load(open('stepE.pkl', 'rb')); BB = E['BB']
C2 = pickle.load(open('stepC2.pkl', 'rb')); spaces = C2['spaces']
F = pickle.load(open('stepF.pkl', 'rb')); hulls = F['hulls']
Def = Tb + Rb
def Bidx(i, j): return list(BB[(min(i, j), max(i, j))])
def Bvec(x, y):
    out = [Fr(0)] * 64
    for i in range(49):
        if x[i] == 0: continue
        for j in range(49):
            if y[j] == 0: continue
            b = Bidx(i, j); c = x[i] * y[j]
            for l in range(64): out[l] += c * b[l]
    return out
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
def coords_def(v): return [sum(INV[j][i] * v[PIV[i]] for i in range(80)) for j in range(80)][31:]
def to_vec(x): return [sum(x[i] * Def[i][m] for i in range(49)) for m in range(256)]
T = TDITA; Tc = [T[0]] + T[1:5] + T[9:25]; Tr = [T[0]] + T[5:9] + T[25:41]
Cc = [coords_def(v) for v in Tc]; Cr = [coords_def(v) for v in Tr]
zero = [Fr(0)] * 64
hull_ranks = [rank(GAUGE + vecs) for _, vecs in hulls]
def in_hull(w):
    return [hi for hi, (nm, vecs) in enumerate(hulls) if rank(GAUGE + vecs + [w]) == hull_ranks[hi]]
for si, V in enumerate(spaces):
    vs = [[Fr(0)] * 26 + [Fr(a) for a in row] for row in V]
    for trial in range(2):
        v = [sum(random.randint(-2, 2) * x[i] for x in vs) for i in range(49)]
        if all(c == 0 for c in v): continue
        # the same extendability search as step G
        found = None
        for s_ in range(6):
            tc = [Fr(0)] * 49 if s_ == 0 else [sum(random.randint(-2, 2) * x[i] for x in Cc) for i in range(49)]
            vt = [v[i] + tc[i] for i in range(49)]
            rhs = Bvec(v, v); b2 = Bvec(v, tc); rhs = [rhs[l] + 2 * b2[l] for l in range(64)]
            cols = [Bvec(vt, y) for y in Cr]
            M = [[2 * cols[k][l] for k in range(len(Cr))] + [-rhs[l]] for l in range(64)]
            Rm, pv2 = rref(M, len(Cr) + 1)
            if len(Cr) not in pv2:
                x = [Fr(0)] * len(Cr)
                for i_, p in enumerate(pv2): x[p] = Rm[i_][len(Cr)]
                tr = [sum(x[k] * Cr[k][i] for k in range(len(Cr))) for i in range(49)]
                w = [vt[i] + tr[i] for i in range(49)]
                assert Bvec(w, w) == zero
                found = w; break
        vv = to_vec(v)
        hits_v = in_hull(vv)
        if found is not None:
            wv = to_vec(found); hits_w = in_hull(wv)
            # also: is w in the span T + T_h for some h (absorbed after correction)?
            print('sector %d trial %d: v itself in hulls %s | second-order-extended w = v + t in hulls %s' % (si, trial, hits_v[:6] if hits_v else 'none', [hulls[h][0] for h in hits_w][:6] if hits_w else 'NONE (a second-order direction outside every known hull)'))
        else:
            absorbed = [hi for hi, (nm, vecs) in enumerate(hulls) if rank(GAUGE + Tb + vecs + [vv]) == rank(GAUGE + Tb + vecs)]
            print('sector %d trial %d: obstructed; v in hulls %s | v in T + T_h for hulls %s' % (si, trial, hits_v[:6] if hits_v else 'none', [hulls[h][0] for h in absorbed][:6] if absorbed else 'none'))
print('done (%.0fs)' % (time.time() - t0))
