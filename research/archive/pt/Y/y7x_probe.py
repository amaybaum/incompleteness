# y7x_probe.py -- thread Y: [N, numerical] exploratory probe, guidance only. No verdict, no PASS/FAIL.
# Question (from y7 run 1): for R = rotation by 2pi/3 about (5,1,1) on the control, does R E0 leave K(E0), and does
# R z leave K(Z_F)? Membership tests used (written, RESULT Y7): R E0 in K(E0) iff <R E0, E0> >= 0 and
# max_{lam >= 0} min-eig(rho(R E0) - lam rho(E0)) >= 0; R z_s in K(Z_F) iff <R z_s, z_t> >= 0 for all t and
# max_{lam in R_+^4} min-eig(rho(R z_s) - sum lam_t rho(z_t)) >= 0. Grids are fixed; output rounded to 4 decimals.
# The probe also reports the largest violation of a pure state v in the cap of the image and outside the original
# cap(s), on a fixed deterministic family of v, to suggest an exact witness family.
import numpy as np

X = np.array([[0, 1], [1, 0]], dtype=complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1.0 + 0j, -1.0])
I2 = np.eye(2, dtype=complex)
S = [I2, X, Y, Z]
SS = [[np.kron(S[m], S[n]) for n in range(4)] for m in range(4)]
pW = lambda w: sum(w[m][n] * SS[m][n] for m in range(4) for n in range(4)) / 4
E0 = [[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0], [0, 0, 0, 0]]
ZF = [[[0.25, 0, 0, 0], [0, 0, 0, s1 / 4], [0, 0, s2 / 4, 0], [0, -s1 * s2 / 4, 0, 0]] for s1 in (1, -1) for s2 in (1, -1)]
U = (3 * I2 - 1j * (5 * X + Y + Z)) / 6
for p in (1, 2):
    G = np.kron(np.linalg.matrix_power(U, p), I2)
    A = G @ pW(E0) @ G.conj().T
    B = pW(E0)
    pair = 4 * np.trace(A @ B).real
    best = max(np.linalg.eigvalsh(A - lam * B).min() for lam in np.linspace(0, 4, 4001))
    print("[N] R^%d E0: <R E0, E0> = %.4f; max_lam min-eig(rho(R E0) - lam rho(E0)) = %.4f" % (p, pair, best))
    wA, VA = np.linalg.eigh(A)
    gA = VA[:, 0]
    worst = 0.0
    for k in (1, 2, 3):
        for s in np.linspace(-1.5, 1.5, 61):
            for ph in (1, 1j):
                v = gA + s * ph * VA[:, k]
                v = v / np.linalg.norm(v)
                a, b = (v.conj() @ A @ v).real, (v.conj() @ B @ v).real
                if a < 0 and b >= 0:
                    worst = min(worst, a)
    print("[N] R^%d E0: most negative <v|rho(R E0)|v> over the fixed family with <v|rho(E0)|v> >= 0: %.4f" % (p, worst))
    for i, z in enumerate(ZF):
        Az = G @ pW(z) @ G.conj().T
        pairs = [4 * np.trace(Az @ pW(t)).real for t in ZF]
        grid = np.linspace(0, 1, 11)
        bz = max(np.linalg.eigvalsh(Az - sum(l * pW(t) for l, t in zip(ls, ZF))).min()
                 for ls in np.array(np.meshgrid(grid, grid, grid, grid)).reshape(4, -1).T)
        print("[N] R^%d z_%d: min <R z, z_t> = %.4f; max over grid of min-eig(rho(R z) - sum lam rho(z_t)) = %.4f"
              % (p, i, min(pairs), bz))
print("[N] guidance only; no verdict.")
