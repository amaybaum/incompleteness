"""Step F4 (fast form of F2): hull membership in Def coordinates of (a) generic sector directions and (b) their second-order extensions w = v + t."""
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
T = TDITA; Tc = [T[0]] + T[1:5] + T[9:25]; Tr = [T[0]] + T[5:9] + T[25:41]
Cc = [coords_def(v) for v in Tc]; Cr = [coords_def(v) for v in Tr]
HR = []
for nm, vecs in hulls:
    cs = [coords_def(v) for v in vecs]; cs = [c for c in cs if any(x != 0 for x in c)]
    HR.append((nm,) + tuple(rref(cs, 49)))
print('hull tangents in Def coordinates: %d (dims %s) (%.0fs)' % (len(HR), sorted(set(len(h[1]) for h in HR)), time.time() - t0))
def in_hull(x):
    hits = []
    for nm, Rh, ph in HR:
        v = [Fr(c) for c in x]
        for i, p_ in enumerate(ph):
            if v[p_] != 0:
                f = v[p_]; v = [a - f * b for a, b in zip(v, Rh[i])]
        if all(c == 0 for c in v): hits.append(nm)
    return hits
zero = [Fr(0)] * 64
for si, V in enumerate(spaces):
    vs = [[Fr(0)] * 26 + [Fr(a) for a in row] for row in V]
    for trial in range(3):
        v = [sum(random.randint(-2, 2) * x[i] for x in vs) for i in range(49)]
        if all(c == 0 for c in v): continue
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
                for i_, p_ in enumerate(pv2): x[p_] = Rm[i_][len(Cr)]
                tr = [sum(x[k] * Cr[k][i] for k in range(len(Cr))) for i in range(49)]
                w = [vt[i] + tr[i] for i in range(49)]; assert Bvec(w, w) == zero
                # the full solution set in t_r: the null space of the linear map adds a family; test the particular w and a few members
                found = (w, x, pv2, Rm); break
        hv = in_hull(v)
        if found:
            w = found[0]; hw = in_hull(w)
            # also the freedom: null space directions of t_r -> B(vt, t_r): those keep B(w', w') = 0 only if B(n, n) = 0...; report the particular solution
            print('sector %d trial %d: v in hulls: %s | w = v + t (B(w,w)=0) in hulls: %s' % (si, trial, sorted(set(hv)) if hv else 'none', sorted(set(hw)) if hw else 'NONE — a second-order direction outside every hull'))
        else:
            print('sector %d trial %d: no Diţă correction found (obstructed by certificate in step G); v in hulls: %s' % (si, trial, sorted(set(hv)) if hv else 'none'))
print('done (%.0fs)' % (time.time() - t0))
