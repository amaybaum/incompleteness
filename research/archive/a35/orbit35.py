"""Independent exact control of the stabilizers: orbit sizes of the dephased classes of F4⊗F4 and Hw under
G_ext by breadth-first search over generators, on exponent matrices mod 4 (pure numpy integer arithmetic).
|Stab| = |G_ext| / |orbit| with |G_ext| = 2654208."""
import numpy as np, sys, time, re
src = open('dita_defect_probe.py', encoding='utf-8').read()
head = src[:src.index("print('== 1.")]
sec1 = src[src.index("print('== 1."):src.index("print('== 2.")]
defs = '\n'.join(l for l in sec1.split('\n') if re.match(r'^[A-Za-z_][A-Za-z0-9_]* = ', l) and 'check(' not in l)
ns = {}; exec(head + '\n' + defs, ns)
ROOTS, F4F4, HW = ns['ROOTS'], ns['F4F4'], ns['HW']
def expo_matrix(H):
    return np.array([[ROOTS.index(x) for x in row] for row in H], dtype=np.int64)
def deph(E):
    E = E - E[:, :1]; E = E - E[:1, :]; return E % 4
def blockperm(p, q): return [4 * p[a] + q[b] for a in range(4) for b in range(4)]
ID = (0, 1, 2, 3); T = (1, 0, 2, 3); C = (1, 2, 3, 0)
ROWG = [blockperm(T, ID), blockperm(C, ID), blockperm(ID, T), blockperm(ID, C)]
SW = [4 * b + a for a in range(4) for b in range(4)]
def gens(E):
    out = []
    for g in ROWG: out.append(E[g, :]); out.append(E[:, g])
    out.append(E[np.ix_(SW, SW)]); out.append((-E) % 4); out.append(E.T.copy())
    return out
def orbit(E0):
    s0 = deph(E0); seen = {s0.tobytes(): s0}; frontier = [s0]
    while frontier:
        nxt = []
        for E in frontier:
            for F in gens(E):
                F = deph(F); k = F.tobytes()
                if k not in seen: seen[k] = F; nxt.append(F)
        frontier = nxt
    return len(seen)
t0 = time.time()
for nm, H in (('F4⊗F4', F4F4), ('Hw', HW)):
    n = orbit(expo_matrix(H)); print(nm, 'orbit', n, 'stabilizer', 2654208 / n, '(%.0fs)' % (time.time() - t0)); sys.stdout.flush()
