"""probe6: (a) BFS closure of the A33 grid action (is it a group of order 36864?);
(b) Newton-projected realizable points near a generic Σ point from mixed row+column twist
directions, with the relabelling-invariant Diţă signature (4-subsets of columns on which the rows
fall into four proportionality classes of four) for H and H^T; signature 0 for both certifies the
point is in no Diţă hull and on no Kronecker locus for ANY pairing."""
import numpy as np, itertools, sys, time
sys.path.insert(0, '.')
from lib35 import *
src = open('probe3b.py').read()
exec(src[:src.index('gens = [a33_perm')])
t0 = time.time()
idn = tuple(range(6))
gens = [tuple(a33_perm(nu, (True,) * 9).array_form) for nu in autos] + [tuple(a33_perm(idn, tuple(r != j for r in range(9))).array_form) for j in range(9)]
def comp(p, q): return tuple(p[i] for i in q)   # apply q then p
start = tuple(range(len(grid)))
seen = {start}; frontier = [start]
while frontier:
    nxt = []
    for p in frontier:
        for g in gens:
            r = comp(g, p)
            if r not in seen: seen.add(r); nxt.append(r)
    frontier = nxt
print('(a) BFS closure of the 81 generators on the grid: %d elements (%.0fs)' % (len(seen), time.time() - t0))
allp = {tuple(a33_perm(nu, eps).array_form) for nu in autos for eps in itertools.product([True, False], repeat=9)}
print('(a) parametrized pairs: %d; all inside the BFS closure: %s; closure inside the pairs: %s' % (len(allp), allp <= seen, seen <= allp))

# (b)
src5 = open('probe5.py').read()
exec(src5[src5.index('def phase_tangent'):src5.index('z, w = np.exp')])
rng = np.random.default_rng(357)
def dita_signature(H, tol=1e-7):
    n = H.shape[0]; Hn = H / np.abs(H); cnt = 0
    for S in itertools.combinations(range(n), 4):
        Rz = Hn[:, S]                      # 16 x 4
        Rz = Rz / Rz[:, :1]                # normalise first entry
        key = np.round(np.c_[Rz.real, Rz.imag], 5)
        classes = {}
        for i in range(n): classes.setdefault(key[i].tobytes(), []).append(i)
        if len(classes) == 4 and all(len(v) == 4 for v in classes.values()): cnt += 1
    return cnt
z, w = np.exp(1j * rng.uniform(0, 2 * np.pi, 2)); X, Y = U_circle(0, z), U_circle(0, w); H = kron(X, Y)
print('(b) signature of a Σ point: H %d, H^T %d; of a column-Diţă point: H %d, H^T %d; of the A34 witness: %d / %d' % (
    dita_signature(H), dita_signature(H.T),
    dita_signature(dita(X, [Y] * 4, np.exp(1j * rng.uniform(0, 6, (4, 4))))), dita_signature(dita(X, [Y] * 4, np.exp(1j * rng.uniform(0, 6, (4, 4)))).T),
    dita_signature(dita(F4(1j), [F4(1j)] * 4, np.array([[1, 1, 1, 1], [1, 1j, 1, -1j], [1, 1, 1, 1], [1, 1, 1, 1]]))), dita_signature(dita(F4(1j), [F4(1j)] * 4, np.array([[1, 1, 1, 1], [1, 1j, 1, -1j], [1, 1, 1, 1], [1, 1, 1, 1]])).T)))
found = []
for trial in range(12):
    Rm = np.zeros((16, 16))
    for _ in range(3):
        c, b = rng.integers(0, 4, 2); Rm[b::4, c * 4:(c + 1) * 4] += rng.normal()
        a, d = rng.integers(0, 4, 2); Rm[a * 4:(a + 1) * 4, d::4] += rng.normal()
    Rm /= np.linalg.norm(Rm)
    for eps in (0.6, 0.3):
        Phi, res = project(H, eps * Rm)
        if res < 1e-10:
            Hp = H * np.exp(1j * Phi)
            sig, sigT = dita_signature(Hp), dita_signature(Hp.T)
            d = defect_numeric(Hp)[0]
            found.append((eps, np.sqrt(max(dist2_U(Hp, H), 0)), sigma_residual(Hp), dita_col_residual(Hp), dita_row_residual(Hp), sig, sigT, d))
            print('    ε=%.1f converged: feature-dist %.3f  Σ-res %.3f  col-res %.3f  row-res %.3f  signature H %d H^T %d  defect %d' % found[-1])
            break
print('(b) converged points: %d; certified in no Diţă hull for any pairing (both signatures 0): %d' % (len(found), sum(1 for f in found if f[5] == 0 and f[6] == 0)))
print('(%.0fs)' % (time.time() - t0))
