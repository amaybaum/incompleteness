"""EQ4-P exploration x1 -- FLOATING POINT, EXPLORATION ONLY.  NOT EVIDENCE.  Never cited as a certificate.

Question (lead-finding only): with the candidate hypothesis "K3 contains W3 = 1/2 - GHZ" (hence, by SLOCC invariance
and co-self-duality, every Ad(k) W3 as a state and every Ad(k) W3 as an effect, k = A (x) B (x) C), can any six-token
network constraint be violated?  Networks (each token shared by one state factor and one effect factor):
  theta : states x(0,1,2), y(3,4,5); effects: pair effects on (0,3), (1,4), (2,5)
  ring  : states x(P1,P2,R), y(Q,U1,U2); effects e(P1,P2,Q), f(R,U1,U2)
  K4    : states x(a,1,2), y(b,3,4), e'(a',b') [pair state]; effects e(a,b) [pair effect], x'(a',1,3), y'(b',2,4)
          (the pairing of a glued state with a glued effect on the quad (1,2,3,4); forced by the existence of K4 in
          the six-token family); also the split x'(a',1,4), y'(b',2,3).
Method: random starts + scipy BFGS on value / (product of Frobenius norms).  Output: minima found.  A negative minimum
is only a lead; it must be certified in exact arithmetic before anything is claimed.
"""
import sys

import numpy as np
from scipy.optimize import minimize

rng = np.random.default_rng(20261009)
G = np.zeros(8, dtype=complex)
G[0] = G[7] = 1 / np.sqrt(2)
W3 = 0.5 * np.eye(8) - np.outer(G, G.conj())


def gl2(p):
    return (p[0:4] + 1j * p[4:8]).reshape(2, 2)


def w3_orbit(p):
    k = np.kron(np.kron(gl2(p[0:8]), gl2(p[8:16])), gl2(p[16:24]))
    return k @ W3 @ k.conj().T


def psd4(p):
    M = (p[0:16] + 1j * p[16:32]).reshape(4, 4)
    return M @ M.conj().T


def t3(X):
    return X.reshape(2, 2, 2, 2, 2, 2)


def t2(X):
    return X.reshape(2, 2, 2, 2)


def theta(p):
    x, y = t3(w3_orbit(p[0:24])), t3(w3_orbit(p[24:48]))
    e0, e1, e2 = t2(psd4(p[48:80])), t2(psd4(p[80:112])), t2(psd4(p[112:144]))
    # token t has letters (i_t, j_t): effect E[i.., j..], state X[j.., i..]
    v = np.einsum("adAD,beBE,cfCF,ABCabc,DEFdef->", e0, e1, e2, x, y, optimize=True)
    n = np.prod([np.linalg.norm(m) for m in (x, y, e0, e1, e2)])
    return (v.real / n), v


def ring(p):
    x, y = t3(w3_orbit(p[0:24])), t3(w3_orbit(p[24:48]))
    e, f = t3(w3_orbit(p[48:72]).T), t3(w3_orbit(p[72:96]).T)
    # tokens P1,P2,Q,R,U1,U2 : letters (a,A),(b,B),(c,C),(d,D),(g,H),(h,K)  [i = lowercase, j = uppercase]
    v = np.einsum("abcABC,dghDHK,ABDabd,CHKcgh->", e, f, x, y, optimize=True)
    n = np.prod([np.linalg.norm(m) for m in (x, y, e, f)])
    return v.real / n, v


def k4(p, split=0):
    x, y = t3(w3_orbit(p[0:24])), t3(w3_orbit(p[24:48]))
    xp, yp = t3(w3_orbit(p[48:72]).T), t3(w3_orbit(p[72:96]).T)
    e, ep = t2(psd4(p[96:128])), t2(psd4(p[128:160]))
    # tokens a,b,a',b',1,2,3,4 : (i,j) letters a/A, b/B, c/C, d/D, e/E? (avoid clash) -> use p/P q/Q r/R s/S t/T u/U v/V w/W
    # a:(p,P) b:(q,Q) a':(r,R) b':(s,S) 1:(t,T) 2:(u,U) 3:(v,V) 4:(w,W)
    if split == 0:   # x'(a',1,3), y'(b',2,4)
        v = np.einsum("pqPQ,rtvRTV,suwSUW,PTUptu,QVWqvw,RSrs->", e, xp, yp, x, y, ep, optimize=True)
    else:            # x'(a',1,4), y'(b',2,3)
        v = np.einsum("pqPQ,rtwRTW,suvSUV,PTUptu,QVWqvw,RSrs->", e, xp, yp, x, y, ep, optimize=True)
    n = np.prod([np.linalg.norm(m) for m in (x, y, xp, yp, e, ep)])
    return v.real / n, v


def search(fun, dim, starts, label):
    best = np.inf
    for s in range(starts):
        p0 = rng.normal(size=dim)
        try:
            r = minimize(lambda p: fun(p)[0], p0, method="BFGS", options={"maxiter": 400, "gtol": 1e-10})
            val = r.fun
        except Exception:
            val = fun(p0)[0]
        best = min(best, val)
    print("%-10s starts=%d  min normalized value = %.6e" % (label, starts, best))
    sys.stdout.flush()
    return best


# control: the QM case (GHZ in place of W3) must give nonnegative minima; sanity of the contraction code
Wsave = W3.copy()
W3 = np.outer(G, G.conj())
search(theta, 144, 4, "ctrl-theta")
search(k4, 160, 4, "ctrl-K4")
W3 = Wsave
search(theta, 144, 12, "theta")
search(ring, 96, 12, "ring")
search(k4, 160, 12, "K4-split0")
search(lambda p: k4(p, 1), 160, 12, "K4-split1")
