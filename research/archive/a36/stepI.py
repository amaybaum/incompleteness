"""Step I (numerical, a discriminator only): does a second-order-extendable direction outside every hull integrate to a curve of
Hadamard matrices? Gauss-Newton on F(theta) = (H∘e^{iθ})(H∘e^{iθ})* − 16 I with θ = ε w + δ, δ ⟂ (gauge + w), for several ε.
Controls: a hull direction (must integrate), an obstructed direction (must fail)."""
import pickle, random, numpy as np
from lib36 import *
random.seed(363)
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
HR = []
for nm, vecs in hulls:
    cs = [coords_def(v) for v in vecs]; cs = [c for c in cs if any(x != 0 for x in c)]
    HR.append((nm,) + tuple(rref(cs, 49)))
def in_hull(x):
    for nm, Rh, ph in HR:
        v = [Fr(c) for c in x]
        for i, p_ in enumerate(ph):
            if v[p_] != 0:
                f = v[p_]; v = [a - f * b for a, b in zip(v, Rh[i])]
        if all(c == 0 for c in v): return nm
    return None
def extension(v):
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
            return [vt[i] + tr[i] for i in range(49)]
    return None
# numerical machinery
Hn = np.array([[complex(float(x.a), float(x.b)) for x in row] for row in SIG])
def Fnum(theta):
    Ht = Hn * np.exp(1j * theta.reshape(16, 16)); M = Ht @ Ht.conj().T - 16 * np.eye(16)
    iu = np.triu_indices(16, 1); return np.concatenate([M[iu].real, M[iu].imag])
def Jnum(theta, h=1e-7):
    f0 = Fnum(theta); J = np.zeros((240, 256))
    for m in range(256):
        t = theta.copy(); t[m] += h; J[:, m] = (Fnum(t) - f0) / h
    return J
Gn = np.array(GAUGE, float)
def integrate(w, eps_list, label):
    w = np.array(w, float); w /= np.linalg.norm(w)
    # constrain: δ orthogonal to gauge and to w (projector)
    Bm = np.vstack([Gn, w]); Qb, _ = np.linalg.qr(Bm.T); Pperp = np.eye(256) - Qb @ Qb.T
    res = []
    for eps in eps_list:
        theta = eps * w
        for it in range(40):
            f = Fnum(theta)
            if np.linalg.norm(f) < 1e-13: break
            J = Jnum(theta) @ Pperp
            step, *_ = np.linalg.lstsq(J, -f, rcond=None)
            theta = theta + Pperp @ step
        f = Fnum(theta); dev = theta - eps * w
        res.append((eps, np.linalg.norm(f), np.linalg.norm(dev)))
    print('  %-52s ' % label + ' | '.join('ε=%.2f: |F|=%.1e, |θ−εw|=%.1e' % r for r in res))
eps_list = [0.05, 0.1, 0.2, 0.4]
print('integration test (Gauss-Newton, |F| after convergence; a genuine curve gives |F| ~ 1e-14 with |θ−εw| = O(ε²)):')
# controls
hv = hulls[3][1]; hw = [sum(random.randint(-2, 2) * v[m] for v in hv) for m in range(256)]
integrate(hw, eps_list, 'control: a swapped-hull tangent direction')
integrate(to_vec([Fr(0)] * 26 + [Fr(random.randint(-2, 2)) for _ in range(23)]), eps_list, 'control: a generic residual direction (no correction)')
for si in (0, 1):
    V = spaces[si]; vs = [[Fr(0)] * 26 + [Fr(a) for a in row] for row in V]
    v = [sum(random.randint(-2, 2) * x[i] for x in vs) for i in range(49)]
    integrate(to_vec(v), eps_list, 'control: obstructed sector %d direction' % si)
for si in (2, 3, 4):
    V = spaces[si]; vs = [[Fr(0)] * 26 + [Fr(a) for a in row] for row in V]
    for trial in range(3):
        v = [sum(random.randint(-2, 2) * x[i] for x in vs) for i in range(49)]
        if all(c == 0 for c in v): continue
        w = extension(v)
        if w is None: print('  sector %d trial %d: no extension' % (si, trial)); continue
        h = in_hull(w)
        integrate(to_vec(w), eps_list, 'sector %d trial %d: w = v + t, %s' % (si, trial, ('in hull %s' % h[:14]) if h else 'outside every hull'))
