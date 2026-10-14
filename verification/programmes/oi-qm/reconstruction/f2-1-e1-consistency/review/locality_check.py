# Independent numerical check [N] of thread J's locality finding: for q = 3, the principal
# logarithm of U(x)U, U the one-site Fourier-type Weil image, versus log U (x) 1 + 1 (x) log U.
import numpy as np, scipy.linalg as sl
q = 3
w = np.exp(2j*np.pi/q)
F = np.array([[w**(j*k) for k in range(q)] for j in range(q)])/np.sqrt(q)
for phase in [1.0, np.exp(1j*np.pi/4), np.exp(1j*np.pi/2), np.exp(-1j*np.pi/3)]:
    U = phase*F
    L1 = sl.logm(U)
    U2 = np.kron(U, U)
    L2 = sl.logm(U2)
    Lsum = np.kron(L1, np.eye(q)) + np.kron(np.eye(q), L1)
    # compare modulo a multiple of the identity (global phase is not physical)
    D = L2 - Lsum
    D0 = D - np.trace(D)/D.shape[0]*np.eye(D.shape[0])
    print(f"phase arg {np.angle(phase):+.3f}: eig args U = {np.round(np.sort(np.angle(np.linalg.eigvals(U))),3)}; "
          f"||log(UxU) - (logU x 1 + 1 x logU)|| mod identity = {np.linalg.norm(D0):.3e}")
