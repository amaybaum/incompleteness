#!/usr/bin/env python3
# condensate_space_probes.py — b86 (2026-08-13)
# The admissible condensate space for the dynamical-selection question:
# 16x16 matrices invariant under the JOINT cubic action (spin (x) taste),
# split by the involution M -> (1(x)xi5) M (1(x)xi5) into xi5-BLIND (+1) and
# xi5-FLIPPING (-1) sectors. Certifies the dimensions quoted in SM Theorem 9's
# Remark and locates M* = sum_j gamma_j (x) xi_j in the flipping sector.
# Deterministic; ranks read off an unambiguous singular-value gap (asserted).
import sys
import numpy as np

I2 = np.eye(2)
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]])
s3 = np.array([[1, 0], [0, -1]], complex)
def K(a, b): return np.kron(a, b)
g = [K(s1, I2), K(s2, s1), K(s2, s2), K(s2, s3)]
xi = [m.T for m in g]
xi5 = (g[0] @ g[1] @ g[2] @ g[3]).T
X5 = K(np.eye(4), xi5)

def Sig(k):
    i, j = [(2, 3), (3, 1), (1, 2)][k - 1]; return (1j / 2) * (g[i] @ g[j])
def tS(k):
    i, j = [(2, 3), (3, 1), (1, 2)][k - 1]; return (1j / 2) * (xi[i] @ xi[j])
def rot(S, th, dim=4): return np.cos(th / 2) * np.eye(dim) + 2j * np.sin(th / 2) * S
def joint(k, th): return K(rot(Sig(k), th), rot(tS(k), th))
GEN = [joint(3, np.pi / 2), joint(1, np.pi / 2) @ joint(3, np.pi / 2)]

def adjoint(U):
    A = np.zeros((256, 256), complex)
    for a in range(16):
        for b in range(16):
            E = np.zeros((16, 16), complex); E[a, b] = 1
            A[:, a * 16 + b] = (U @ E @ U.conj().T).reshape(-1)
    return A

fail = 0
M = np.vstack([adjoint(U) - np.eye(256) for U in GEN])
sv = np.linalg.svd(M, compute_uv=False)
rank = int(np.sum(sv > 1e-8))
gap_lo, gap_hi = sv[rank - 1], (sv[rank] if rank < len(sv) else 0.0)
print(f"invariant space: dim = {256 - rank}   (singular-value gap {gap_lo:.3e} -> {gap_hi:.3e})")
if not (gap_lo > 1e-6 and gap_hi < 1e-10): fail += 1; print("  FAIL: rank is not unambiguous")
null = np.linalg.svd(M)[2][rank:].conj().T
if null.shape[1] != 32: fail += 1; print(f"  FAIL: expected invariant dim 32, got {null.shape[1]}")

J = np.zeros((256, 256), complex)
for a in range(16):
    for b in range(16):
        E = np.zeros((16, 16), complex); E[a, b] = 1
        J[:, a * 16 + b] = (X5 @ E @ X5).reshape(-1)
w = np.linalg.eigvals(null.conj().T @ J @ null)
blind = int(np.sum(np.abs(w - 1) < 1e-6)); flip = int(np.sum(np.abs(w + 1) < 1e-6))
print(f"  xi5-BLIND (+1) = {blind}   xi5-FLIPPING (-1) = {flip}")
if (blind, flip) != (16, 16): fail += 1; print("  FAIL: expected a 16/16 split")

Ms = sum(K(g[j], xi[j]) for j in (1, 2, 3))
v = Ms.reshape(-1)
res = np.linalg.norm(v - null @ (null.conj().T @ v)) / np.linalg.norm(v)
herm = np.allclose(Ms, Ms.conj().T); flp = np.allclose(Ms @ X5 + X5 @ Ms, 0)
print(f"  M* invariant (residual {res:.2e}) | Hermitian {herm} | flipping {flp}")
if not (res < 1e-10 and herm and flp): fail += 1; print("  FAIL: M* does not sit in the flipping sector as claimed")
print("condensate_space_probes:", "ALL CHECKS PASS" if fail == 0 else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
