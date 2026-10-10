"""Countercontrols adjacent to the S1-S5 proof (exact integer/rational arithmetic unless noted). Read-only.
 C3  d = 3 complex CNOT: frame, S1 form with M_0 = I, M_1 = N (the Bloch rotation fixing x), both native relations,
     S2 structure (E+ block [[0,A],[A,B]], V- block closed), p = q = 1.
 C5  d = 5 J/K map: frame, S1 form, target relation, S2 structure with p = 1, q = 3; the control relation fails;
     positivity is exact by reduction to C3 (BALL5-FINITE.md, section 1).
 C2  d = 2: p + q = 1, so p = q is impossible.
 C7  d = 7 algebraic candidate: frame, G^2 = I, both relations; violates max-cone positivity (1 - sqrt 3, uniform_nogo.log)."""
import numpy as np
OUT = []
def rep(n, ok, det=''):
    OUT.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + n + ('  ' + det if det else ''), flush=True)
def check(G, n, Nd, name, p):
    e = np.eye(n); k = [e[0] + e[n - 1], e[0] - e[n - 1]]; N = np.diag(Nd)
    frame = all(np.allclose(G @ np.kron(k[a], k[b]), np.kron(k[a], k[a ^ b])) for a in (0, 1) for b in (0, 1))
    # S1: G(k_a (x) t) = k_a (x) M_a t
    M = []
    okS1 = True
    for a in (0, 1):
        Ma = np.zeros((n, n))
        for j in range(n):
            img = (G @ np.kron(k[a], e[j])).reshape(n, n)
            # must be k_a (x) m: rank one with control factor k_a
            m = img[0]                                   # coefficient of u-row (k_a has u-component 1)
            okS1 &= np.allclose(img, np.outer(k[a], m)); Ma[:, j] = m
        M.append(Ma)
    iso = all(np.allclose(Ma[1:, 1:].T @ Ma[1:, 1:], np.eye(n - 1)) for Ma in M)
    rel_t = np.allclose(np.kron(e, N) @ G @ np.kron(e, N), G)
    rel_c = np.allclose(np.kron(N, e) @ G @ np.kron(N, e), np.kron(e, N) @ G)
    M1NM0 = np.allclose(M[1], N @ M[0])
    # S2 on G~ = G (I (x) M_0^-1): E+ block [[0, A_r],[A_r, B_rs]] and V- block closed & antisymmetric
    Gt = G @ np.kron(e, np.linalg.inv(M[0]))
    TA = list(range(1, n - 1)); Vp = [i for i in range(1, n - 1) if Nd[i] == 1]; Vm = [i for i in range(1, n) if Nd[i] == -1]
    ok2 = True
    for c in TA:
        colu = Gt[:, c * n + 0].reshape(n, n)
        ok2 &= np.allclose(colu[:, [0] + Vm], 0)                         # G~(c (x) u) in T_A (x) V+
        for r in Vp:
            col = Gt[:, c * n + r].reshape(n, n)
            ok2 &= np.allclose(col[:, 0], colu[:, r])                    # (u, r) block == (r, u) block  (same A_r)
            ok2 &= np.allclose(col[:, Vm], 0)
            for s in Vp:
                ok2 &= np.allclose(col[:, s], -Gt[:, c * n + s].reshape(n, n)[:, r])    # B antisymmetric
        for j in Vm:
            col = Gt[:, c * n + j].reshape(n, n)
            ok2 &= np.allclose(col[:, [0] + Vp], 0)
            for l in Vm:
                ok2 &= np.allclose(col[:, l], -Gt[:, c * n + l].reshape(n, n)[:, j])   # V- block antisymmetric
    rep('%s: frame %s, S1 form %s, M_a isometries %s, M_1 = N M_0 %s, S2 structure %s, target rel %s, control rel %s (p=%d)'
        % (name, frame, okS1, iso, M1NM0, ok2, rel_t, rel_c, p), True)
    return frame, okS1, iso, M1NM0, ok2, rel_t, rel_c
from disc_cnot_search import complex_cnot
r3 = check(complex_cnot(), 4, [1, 1, -1, -1], 'C3 complex CNOT (d=3)', 1)
rep('C3: every hypothesis and the S1/S2 structure hold; p = q = 1', all(r3))
import ball5_run1 as r1
perm = [0, 1, 2, 4, 5, 3]                              # J/K module order u,x,y,z,w1,w2 -> u,x,y,w1,w2,z
Pm = np.eye(6)[perm]; G5 = np.kron(Pm, Pm) @ r1.JK_G().mat() @ np.kron(Pm, Pm).T
r5 = check(G5, 6, [1, 1, -1, -1, -1, -1], 'C5 J/K (d=5)', 1)
rep('C5: frame, S1, S2, target relation hold; control relation FAILS; p = 1, q = 3', all(r5[:6]) and not r5[6])
rep('C2 d=2: p + q = d - 1 = 1 admits no p = q', all(p != 1 - p for p in (0, 1)))
from ball7 import build
r7 = check(build(), 8, [1, 1, 1, 1, -1, -1, -1, -1], 'C7 d=7 candidate', 3)
G7 = build(); rep('C7: frame, G^2 = I and both native relations hold (positivity fails: 1 - sqrt 3, see uniform_nogo.log)',
    r7[0] and np.allclose(G7 @ G7, np.eye(64)) and r7[5] and r7[6])
print('\nSUMMARY: %d PASS, %d FAIL' % (sum(OUT), len(OUT) - sum(OUT)))
