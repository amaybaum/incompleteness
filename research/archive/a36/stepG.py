"""Step G: second-order census of R's stabilizer sectors with exact certificates:
obstruction certificate: B(v,v) not in span{B(v,T), B(T,T)}; extendability certificate: an explicit t in T with B(v+t, v+t) = 0."""
import pickle, time, random
from lib36 import *
random.seed(363); t0 = time.time()
A = pickle.load(open('stepA.pkl', 'rb')); LN = A['LN']
B = pickle.load(open('stepB.pkl', 'rb')); Gb, Tb, Rb = B['Gb'], B['Tb'], B['Rb']
E = pickle.load(open('stepE.pkl', 'rb')); BB = E['BB']
C2 = pickle.load(open('stepC2.pkl', 'rb')); spaces = C2['spaces']
Def = Tb + Rb
def Bidx(i, j): return list(BB[(min(i, j), max(i, j))])
def Bvec(x, y):
    """B of two vectors given by Def-coordinates x, y (lists of Fractions, length 49): bilinear expansion"""
    out = [Fr(0)] * 64
    for i in range(49):
        if x[i] == 0: continue
        for j in range(49):
            if y[j] == 0: continue
            b = Bidx(i, j); c = x[i] * y[j]
            for l in range(64): out[l] += c * b[l]
    return out
def coord_R(a):   # sector vector a (coeffs on Rb) -> Def coords
    return [Fr(0)] * 26 + [Fr(x) for x in a]
# T_c and T_r inside Def coordinates: recompute coordinates of TDITA vectors via the adapted basis
basis = Gb + Tb + Rb
Rr, piv = rref(basis, 256); PIV = piv[:80]
Msub = [[Fr(basis[j][p]) for j in range(80)] for p in PIV]
aug = [Msub[i] + [Fr(1) if k == i else Fr(0) for k in range(80)] for i in range(80)]
Ri, pv = rref(aug, 160); INV = [r[80:] for r in Ri]
def coords_def(v): return [sum(INV[j][i] * v[PIV[i]] for i in range(80)) for j in range(80)][31:]
T = TDITA; Tc = [T[0]] + T[1:5] + T[9:25]; Tr = [T[0]] + T[5:9] + T[25:41]
Cc = [coords_def(v) for v in Tc]; Cr = [coords_def(v) for v in Tr]
zero = [Fr(0)] * 64
print('control: B(T_c,T_c) = 0 and B(T_r,T_r) = 0 through the Def-coordinate expansion:', all(Bvec(x, y) == zero for x in Cc for y in Cc), all(Bvec(x, y) == zero for x in Cr for y in Cr))
Tcoords = [[Fr(1) if k == i else Fr(0) for k in range(49)] for i in range(26)]
BTT = [[Bvec(Tcoords[i], Tcoords[j]) for j in range(26)] for i in range(26)]
for si, V in enumerate(spaces):
    print('sector %d (dim %d):' % (si, len(V)))
    vs = [coord_R(a) for a in V]
    iso = all(Bvec(x, y) == zero for x in vs for y in vs)
    coupT = any(Bvec(x, t) != zero for x in vs for t in Tcoords)
    # generic element of the sector
    for trial in range(2):
        v = [sum(random.randint(-2, 2) * x[i] for x in vs) for i in range(49)]
        if all(c == 0 for c in v): continue
        Bvv = Bvec(v, v)
        BvT = [Bvec(v, t) for t in Tcoords]
        span_rows = [list(r) for r in BvT] + [list(BTT[i][j]) for i in range(26) for j in range(i, 26)]
        rk = rank(span_rows, 64); rk2 = rank(span_rows + [list(Bvv)], 64)
        obstructed_cert = rk2 > rk
        found = None
        if not obstructed_cert:
            # extendability: t = t_c + t_r; for sample t_c, solve linear in t_r: B(v,v) + 2B(v,t_c) + 2B(v+t_c, t_r) = 0
            for s in range(6):
                tc = [Fr(0)] * 49 if s == 0 else [sum(random.randint(-2, 2) * x[i] for x in Cc) for i in range(49)]
                vt = [v[i] + tc[i] for i in range(49)]
                rhs = Bvec(v, v); b2 = Bvec(v, tc)
                rhs = [rhs[l] + 2 * b2[l] for l in range(64)]
                cols = [Bvec(vt, y) for y in Cr]          # 14 columns of 64 (times 2)
                # solve sum_k x_k * 2*cols[k] = -rhs  exactly
                M = [[2 * cols[k][l] for k in range(len(Cr))] + [-rhs[l]] for l in range(64)]
                Rm, pv2 = rref(M, len(Cr) + 1)
                if len(Cr) not in pv2:
                    x = [Fr(0)] * len(Cr)
                    for i_, p in enumerate(pv2): x[p] = Rm[i_][len(Cr)]
                    tr = [sum(x[k] * Cr[k][i] for k in range(len(Cr))) for i in range(49)]
                    w = [vt[i] + tr[i] for i in range(49)]
                    assert Bvec(w, w) == zero
                    found = (s, x); break
        print('   trial %d: B(v,v)=0: %s | obstruction certificate (B(v,v) outside span{B(v,T),B(T,T)}): %s | extendable with an explicit Diţă correction: %s' % (trial, Bvv == zero, obstructed_cert, 'yes (t_c sample %d)' % found[0] if found else 'not found'))
    print('   sector isotropic for B (B(V,V)=0): %s | couples to T (B(V,T) != 0): %s' % (iso, coupT))
print('done (%.0fs)' % (time.time() - t0))
