#!/usr/bin/env python3
"""Thread B exploration e1 [F] -- floating point, certifies nothing.

Question (DEPGRAPH 7.6, open): is some gate premise needed for IE1, or only for the parity?
Candidate foil: K01 = K23 = K_h := maxCone n {w : <h, w> >= 0}, K02 = K13 = maxCone, cnot gates, identity locals,
with h = diag(1, t, t, 0).  Written reduction (NOTES N-E1): FCC for this family holds iff h L h lies in SEP for every
L in maxCone; K_h is not IE1 when t > 1/2.  This script only samples L and tests SEP of h L h by PPT (two qubits).

Decision rule (exploration): report the minimum eigenvalue found over all samples of the partial transpose of
pauliW(h L h), for each t; a negative minimum below -1e-9 is reported as a float counterexample candidate.
Output is deterministic (fixed seed).  Nothing printed here is a certificate.
"""
import numpy as np

S = [np.eye(2, dtype=complex), np.array([[0, 1], [1, 0]], dtype=complex),
     np.array([[0, -1j], [1j, 0]], dtype=complex), np.array([[1, 0], [0, -1]], dtype=complex)]
SS = [[np.kron(S[m], S[n]) for n in range(4)] for m in range(4)]


def pauliW(w):
    out = np.zeros((4, 4), dtype=complex)
    for m in range(4):
        for n in range(4):
            out += w[m, n] * SS[m][n]
    return out / 4


def table_of(rho):
    return np.array([[np.real(np.trace(rho @ SS[m][n])) for n in range(4)] for m in range(4)])


def ptrans2(M):
    R = M.reshape(2, 2, 2, 2)
    return R.transpose(0, 3, 2, 1).reshape(4, 4)


def min_eig(M):
    return float(np.min(np.linalg.eigvalsh((M + M.conj().T) / 2)))


rng = np.random.default_rng(20261010)


def rand_pure():
    v = rng.normal(size=4) + 1j * rng.normal(size=4)
    v /= np.linalg.norm(v)
    return np.outer(v, v.conj())


def in_maxcone_float(w, n=400):
    # sample a, b on the boundary of the Lorentz cone
    worst = np.inf
    for _ in range(n):
        a = rng.normal(size=3); a /= np.linalg.norm(a)
        b = rng.normal(size=3); b /= np.linalg.norm(b)
        A = np.concatenate([[1.0], a]); B = np.concatenate([[1.0], b])
        worst = min(worst, A @ w @ B)
    return worst


DREF = np.diag([1.0, 1.0, -1.0, 1.0])
for t in (0.55, 0.6, 0.65, 0.70, 0.7071, 0.72, 0.75, 0.8):
    h = np.diag([1.0, t, t, 0.0])
    worst = np.inf
    worst_kind = None
    for k in range(4000):
        rho = rand_pure()
        L = table_of(rho)
        for kind, LL in (('Q3', L), ('twin', L @ DREF)):
            M = pauliW(h @ LL @ h)
            e = min(min_eig(M), min_eig(ptrans2(M)))
            if e < worst:
                worst, worst_kind = e, kind
    # rejection-sampled random tables in maxCone (float)
    for k in range(300):
        w = np.zeros((4, 4)); w[0, 0] = 1.0
        w[1:, 1:] = rng.uniform(-1, 1, size=(3, 3))
        w[0, 1:] = rng.uniform(-0.5, 0.5, size=3); w[1:, 0] = rng.uniform(-0.5, 0.5, size=3)
        if in_maxcone_float(w) < 0:
            continue
        M = pauliW(h @ w @ h)
        e = min(min_eig(M), min_eig(ptrans2(M)))
        if e < worst:
            worst, worst_kind = e, 'rand'
    print(f't={t:.4f}  min eigenvalue of pauliW(hLh) and its partial transpose over samples: {worst:+.6f} ({worst_kind})')

# IE1 failure of K_h (float illustration): w = Bell-diagonal (-1, 1, -1) in maxCone, <h,w> = 1 + t(-1+1) >= 0;
# swapping axes 2 and 3 on both tokens gives (-1, -1, 1) with <h,w'> = 1 - 2t < 0 for t > 1/2.
for t in (0.6,):
    h = np.diag([1.0, t, t, 0.0])
    w = np.diag([1.0, -1.0, 1.0, -1.0]); w2 = np.diag([1.0, -1.0, -1.0, 1.0])
    print(f't={t}: <h,w>={np.sum(h*w):+.3f} <h,w_rot>={np.sum(h*w2):+.3f}')
