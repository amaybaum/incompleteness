# Scratch (numerical guidance only, not evidence): tightness instances for C23's balanced route.
import numpy as np
def D(u, v): return np.diag([1, u*v, u, v]).astype(complex)
XB = np.array([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]], dtype=complex)
def proj(v): v = np.asarray(v, complex); return np.outer(v, v.conj())/np.vdot(v, v).real
def partner(h):
    h = np.asarray(h, complex)
    al = np.conj(h[2])*h[3]; be = np.conj(h[0])*h[1]
    us = [np.exp(1j*t) for t in (0.3, 1.1, 2.0, 2.9)]
    rows = []
    for u in us:
        den = np.conj(al) + u*np.conj(be)
        v = -(be + u*al)/den
        g = D(u, v) @ XB
        gh = g @ h
        assert abs(np.vdot(h, gh)) < 1e-9
        rows.append(gh)
    M = np.array(rows)
    r = np.linalg.matrix_rank(M, tol=1e-9)
    # k ⊥ h and ⊥ rows
    A = np.vstack([M.conj(), h.conj()[None, :]])
    _, s, vh = np.linalg.svd(A)
    null = vh[np.sum(s > 1e-9):]
    return r, null, us
def tight(h, k, c, which, eps_list, phis, rs):
    h = np.asarray(h, complex); k = np.asarray(k, complex)
    d = np.eye(4) - c*proj(h) - (2-c)*proj(k)
    nh, nk = np.linalg.norm(h), np.linalg.norm(k)
    best = None
    for eps in eps_list:
        U = D(np.exp(1j*eps), 1) if which == 1 else D(1, np.exp(1j*eps))
        dU = U @ d @ U.conj().T
        pair = np.trace(d @ dU).real
        for phi in phis:
            for r in rs:
                b = r*np.exp(1j*phi)*nh/nk
                u = h + b*k
                if (u.conj() @ d @ u).real >= 0: continue
                x = k - (np.vdot(u, k)/np.vdot(u, u))*u
                val = (x.conj() @ dU @ x).real/np.vdot(x, x).real
                if best is None or val < best[0]:
                    best = (val, eps, phi, r, pair, (x.conj() @ d @ x).real/np.vdot(x,x).real)
    return best
for name, h in [("ii", [2, 3j, 1, 6]), ("iii", [3, 1, 2j, 0]), ("iv", [3, 0, 2j, 1]), ("i", [6, 1j, 4, 3])]:
    r, null, us = partner(h)
    print(name, "rank", r, "null dim", null.shape[0])
    if null.shape[0] == 1:
        k = null[0].conj()  # rows of vh are conj? use solution of A x = 0: x = conj(vh row)
        A_ok = abs(np.vdot(np.asarray(h, complex), k))
        print("  |<h|k>|", A_ok)
        k = null[0].conj()
        hh = np.asarray(h, complex)
        print("  |<h|k>| (vh row)", abs(np.vdot(hh, k)), " k ~", np.round(k/k[np.argmax(abs(k))], 4))
        for c in (1.5, 1.01):
            for which in (1, 2):
                b = tight(h, k, c, which, [0.02, 0.05, 0.1, 0.2, -0.02, -0.05, -0.1, -0.2], np.linspace(0, 2*np.pi, 73), [0.9, 0.95, 0.98, 0.99, 0.995])
                print("   c", c, "H", which, "best", None if b is None else tuple(np.round(b, 6)))
