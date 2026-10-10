"""EQ4-SIX exploration y5 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Sector Xi: operators invariant under the token permutations S_3 and the zero-sum diagonal phases
(theta1 + theta2 + theta3 = 0): X = sum_w d_w Pi_w + c |000><111| + h.c. (Pi_w = projector on computational strings
of weight w).  Tw_Xi = S_3 twirl o torus twirl; K_Xi := K3 cap Xi = Tw_Xi(K3) for any admissible K3.  Pairing
tr(XY) = d0 d0' + 3 d1 d1' + 3 d2 d2' + d3 d3' + 2 Re(c conj c'); co-self-duality in modulus form uses
d.d' - 2 |c||c'|.  Twirled filters M_k = Tw_Xi o Ad(k) map Xi to Xi and must preserve K_Xi.
Written (NOTES N2.x): BS* cap Xi = {d >= 0, |c| <= u0 + u1}, Tw_Xi(BS) = {d >= 0, |c| <= min(u0, 3 u1)},
u0 = sqrt(d0 d3), u1 = sqrt(d1 d2); QM: |c| <= u0.  The geometric family
phi_a(d) = C_a u0^(1-a) (sqrt3 u1)^a,  C_a^2 = (1-a)^-(1-a) a^-a,
is self-dual in Xi and invariant under all diagonal filters (Maclaurin), GHZ-free for a > 0.
Question (lead only): is the cone {|c| <= phi_a(d)} invariant under every twirled filter M_k?  Method: boundary points
(random d > 0, |c| = phi_a(d), random phase), random complex k = A (x) B (x) C, report the largest ratio
|c'| / phi_a(d').  Also the same test for QM (a = 0), which must give ratio <= 1.  Also the containment of
Tw_Xi(BS) (min(u0, 3u1) <= phi_a) on a grid.
"""
import sys

import numpy as np

rng = np.random.default_rng(2026100905)
W = np.array([bin(a).count("1") for a in range(8)])


def xi_op(d, c):
    X = np.diag(d[W]).astype(complex)
    X[0, 7] = c
    X[7, 0] = np.conj(c)
    return X


def tw(X):
    d = np.array([np.real(np.mean([X[a, a] for a in range(8) if W[a] == w])) for w in range(4)])
    return d, X[0, 7]


def phi(d, a):
    if np.any(d < 0):
        return -np.inf
    u0 = np.sqrt(d[0] * d[3])
    u1 = np.sqrt(d[1] * d[2])
    if a == 0:
        return u0
    C = np.sqrt((1 - a) ** (-(1 - a)) * a ** (-a)) if a < 1 else 1.0
    return C * u0 ** (1 - a) * (np.sqrt(3) * u1) ** a


def rk():
    return np.kron(np.kron(*[rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)) for _ in range(2)]),
                   rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)))


for a in (0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6):
    # containment of Tw(BS)
    worst_bs = np.inf
    for _ in range(2000):
        d = np.exp(rng.normal(size=4) * 2)
        lo = min(np.sqrt(d[0] * d[3]), 3 * np.sqrt(d[1] * d[2]))
        worst_bs = min(worst_bs, phi(d, a) / lo)
    worst = 0.0
    for _ in range(4000):
        d = np.exp(rng.normal(size=4) * 1.5)
        c = phi(d, a) * np.exp(2j * np.pi * rng.random())
        k = rk()
        Y = k @ xi_op(d, c) @ k.conj().T
        d2, c2 = tw(Y)
        worst = max(worst, abs(c2) / phi(d2, a))
    print("a = %.1f: min phi_a / min(u0, 3u1) over 2000 random d = %.4f (>= 1 needed); max |c'|/phi_a(d') over 4000 "
          "random boundary points and filters = %.4f (<= 1 needed)" % (a, worst_bs, worst), flush=True)
print("done", file=sys.stderr)
