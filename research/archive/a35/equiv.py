"""Hadamard equivalence search: find row bijection s and column bijection r with all cross ratios
CR_H(i,k;j,l) = CR_K(s i, s k; r j, r l); backtracking with incremental checks. Exhaustive if it
returns None (up to the time limit)."""
import numpy as np, sys, time, itertools
sys.path.insert(0, '.')
from lib35 import *
def crtab(H):
    Hn = H / np.abs(H)
    # C[i,k,j,l] = H_ij H_kl conj(H_il H_kj), rounded to a small int code (fourth roots)
    C = np.einsum('ij,kl->ikjl', Hn, Hn) * np.conj(np.einsum('il,kj->ikjl', Hn, Hn))
    return np.round(np.angle(C) / (np.pi / 2)).astype(int) % 4
def equivalent(H, K, limit=120):
    CH, CK = crtab(H), crtab(K); n = H.shape[0]; t0 = time.time()
    s = [-1] * n; r = [-1] * n; used_s = set(); used_r = set()
    # assign rows and columns alternately: order: r0, s0, r1, s1, ...
    order = [('c', 0), ('r', 0)] + [x for j in range(1, n) for x in (('c', j), ('r', j))]
    def ok():
        rs = [i for i in range(n) if s[i] >= 0]; cs = [j for j in range(n) if r[j] >= 0]
        if len(rs) < 2 or len(cs) < 2: return True
        for i in rs:
            for k in rs:
                if i == k: continue
                for j in cs:
                    for l in cs:
                        if j == l: continue
                        if CH[i, k, j, l] != CK[s[i], s[k], r[j], r[l]]: return False
        return True
    def okpartial(kind, idx):
        rs = [i for i in range(n) if s[i] >= 0]; cs = [j for j in range(n) if r[j] >= 0]
        if kind == 'r':
            i = idx
            for k in rs:
                if k == i: continue
                for j in cs:
                    for l in cs:
                        if j != l and CH[i, k, j, l] != CK[s[i], s[k], r[j], r[l]]: return False
        else:
            j = idx
            for l in cs:
                if l == j: continue
                for i in rs:
                    for k in rs:
                        if i != k and CH[i, k, j, l] != CK[s[i], s[k], r[j], r[l]]: return False
        return True
    sol = [None]; nodes = [0]
    def bt(pos):
        if time.time() - t0 > limit: raise TimeoutError
        if pos == len(order): sol[0] = (s[:], r[:]); return True
        kind, idx = order[pos]; nodes[0] += 1
        for cand in range(n):
            if kind == 'r':
                if cand in used_s: continue
                s[idx] = cand; used_s.add(cand)
                if okpartial('r', idx) and bt(pos + 1): return True
                s[idx] = -1; used_s.discard(cand)
            else:
                if cand in used_r: continue
                r[idx] = cand; used_r.add(cand)
                if okpartial('c', idx) and bt(pos + 1): return True
                r[idx] = -1; used_r.discard(cand)
        return False
    try:
        found = bt(0)
    except TimeoutError:
        return 'timeout', nodes[0]
    return (sol[0] if found else None), nodes[0]
Fi = F4(1j); K = kron(Fi, Fi)
H34 = dita(Fi, [F4(1j if c % 2 == 0 else -1j) for c in range(4)], np.ones((4, 4)))
Dw = np.ones((4, 4), dtype=complex); Dw[1, :] = [1, 1j, 1, -1j]; Hw = dita(Fi, [Fi] * 4, Dw)
t = time.time(); print('K ~ K:', equivalent(K, K, 60)[0] is not None, '(%.1fs)' % (time.time() - t))
t = time.time(); res, nodes = equivalent(H34, K, 300); print('H34 ~ F4⊗F4:', res if res in (None, 'timeout') else 'YES', 'nodes', nodes, '(%.1fs)' % (time.time() - t))
if res not in (None, 'timeout'):
    s, r = res
    print('  row bijection', s); print('  col bijection', r)
    # verify: dephased H34[s^-1?] ... check by phases: H34[i,j] / K[s i, r j] should factor as p_i q_j
    Q = np.array([[H34[i, j] / K[s[i], r[j]] for j in range(16)] for i in range(16)])
    Q = Q / Q[:, :1]; Q = Q / Q[:1, :]
    print('  residual phase matrix constant after row/col dephasing:', np.allclose(Q, 1))
t = time.time(); res, nodes = equivalent(Hw, K, 300); print('Hw ~ F4⊗F4:', res if res in (None, 'timeout') else 'YES', 'nodes', nodes, '(%.1fs)' % (time.time() - t))
