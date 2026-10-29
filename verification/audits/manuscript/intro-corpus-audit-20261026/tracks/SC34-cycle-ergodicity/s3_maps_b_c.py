#!/usr/bin/env python3
"""Maps (b) and (c), exact small-size checks.

(b) rounded bijection, exactly as papers/main_repro/lyapunov_v3.py:
      nn(x) = sum over the 2d np.roll(+-1) neighbours (integer representatives in [0,q));
      new = ((nn(cur) + 1) // 3 - prv) % q ;  (prv, cur) -> (cur, new)
    and the 1D analog census of papers/main_repro/mixing_battery.py: f = (s+1)//2, L=5, q=4.
(c) SM 3.1 explicit state-dependent ring: R(i,x) = i+2 if x_{i+1} == 0 else i+1, Lft(i) = i-1;
      x_i(t+1) = (x_{Lft(i)}(t) + x_{R(i,x(t))}(t) - x_i(t-1)) mod q.

For each instance (exhaustive over all q^(2N) states, exact integers):
  K0 bijection
  K1 energy conservation, fraction of states at which one step changes
       E_q  = u.u + v.v - alpha u.A v  (mod q)   [alpha = 1/d mod q where invertible, else 1]
       E_R3 = 3*(u.u + v.v) - u.A v over Z on representatives in [0,q)  [(b) 3D: real alpha = 1/3, times 3]
       E_R2 = 2*(u.u + v.v) - u.A v over Z                                 [(b) 1D: real alpha = 1/2, times 2]
  K2 dimension of the space of degree<=2 polynomial invariants over F_p (p odd prime q), each basis
     element verified on all states; positive control: the same solver on map (a) of the same size
  K3 cycle census (pointer doubling, cross-checked by traversal when small); completeness
  K4 for a non-conserved energy: number of distinct E values visited by the largest cycle
"""
import itertools, math
import numpy as np

def adjacency(d, L):
    N = L**d; A = np.zeros((N, N), dtype=np.int64)
    coords = list(itertools.product(range(L), repeat=d)); index = {c: i for i, c in enumerate(coords)}
    for c in coords:
        for k in range(d):
            for s in (1, -1):
                c2 = list(c); c2[k] = (c2[k] + s) % L
                A[index[c], index[tuple(c2)]] += 1
    return A

def digits_of(idx, n, q):
    out = np.empty((n, idx.size), dtype=np.int64); t = idx.copy()
    for i in range(n): out[i] = t % q; t //= q
    return out

def index_of(dig, q):
    w = q ** np.arange(dig.shape[0], dtype=np.int64); return (dig * w[:, None]).sum(0)

def cycle_labels(P):
    lab = np.arange(P.size, dtype=P.dtype); Q = P.copy()
    for _ in range(int(math.ceil(math.log2(P.size))) + 1):
        lab = np.minimum(lab, lab[Q]); Q = Q[Q]
    return lab

def traversal_cycles(P):
    seen = np.zeros(P.size, bool); out = []; Pl = P.tolist()
    for s in range(P.size):
        if seen[s]: continue
        x = s; c = 0
        while not seen[x]: seen[x] = True; c += 1; x = Pl[x]
        out.append(c)
    return sorted(out)

def nullspace_mod_p(Mat, p):
    M = Mat.copy() % p; rows, cols = M.shape; piv = []; r = 0
    for c in range(cols):
        if r >= rows: break
        nz = np.nonzero(M[r:, c])[0]
        if nz.size == 0: continue
        k = r + nz[0]; M[[r, k]] = M[[k, r]]
        M[r] = (M[r] * pow(int(M[r, c]), p - 2, p)) % p
        for o in np.nonzero(M[:, c])[0]:
            if o != r: M[o] = (M[o] - M[o, c] * M[r]) % p
        piv.append(c); r += 1
    basis = []
    for f in [c for c in range(cols) if c not in piv]:
        vec = np.zeros(cols, dtype=np.int64); vec[f] = 1
        for i, pc in enumerate(piv): vec[pc] = (-M[i, f]) % p
        basis.append(vec)
    return np.array(basis, dtype=np.int64).reshape(len(basis), cols)

def monomials(n):
    return [(i,) for i in range(n)] + [(i, j) for i in range(n) for j in range(i, n)]

def eval_monos(dig, monos):
    out = np.empty((len(monos), dig.shape[1]), dtype=np.int64)
    for k, m in enumerate(monos):
        out[k] = dig[m[0]] if len(m) == 1 else dig[m[0]] * dig[m[1]]
    return out

# ---- step functions on digit arrays z = (u; v) = (x(t-1); x(t)), shape (2N, batch) ----
def step_a(z, N, q, A, alpha):
    u, v = z[:N], z[N:]
    return np.vstack([v, (alpha * (A @ v) - u) % q])

def step_b(z, N, q, A, div):
    u, v = z[:N], z[N:]
    return np.vstack([v, (((A @ v) + 1) // div - u) % q])      # A @ v = integer np.roll neighbour sum

def step_c(z, N, q, A_unused, unused):
    u, v = z[:N], z[N:]
    L = N; new = np.empty_like(v)
    for i in range(L):
        right = np.where(v[(i + 1) % L] == 0, v[(i + 2) % L], v[(i + 1) % L])
        new[i] = (v[(i - 1) % L] + right - u[i]) % q
    return np.vstack([v, new])

def build(step, N, q, A, par):
    n = 2 * N; S = q**n; P = np.empty(S, dtype=np.int32 if S < 2**31 else np.int64)
    ch = 1 << 20
    for s0 in range(0, S, ch):
        idx = np.arange(s0, min(S, s0 + ch), dtype=np.int64)
        P[s0:s0 + idx.size] = index_of(step(digits_of(idx, n, q), N, q, A, par), q)
    return P

def energies(N, q, A, alpha_mod):
    n = 2 * N; S = q**n; ch = 1 << 20
    Eq = np.empty(S, np.int64); E3 = np.empty(S, np.int64); E2 = np.empty(S, np.int64)
    for s0 in range(0, S, ch):
        idx = np.arange(s0, min(S, s0 + ch), dtype=np.int64); z = digits_of(idx, n, q)
        u, v = z[:N], z[N:]; uu = (u * u).sum(0) + (v * v).sum(0); uAv = (u * (A @ v)).sum(0)
        Eq[s0:s0 + idx.size] = (uu - alpha_mod * uAv) % q
        E3[s0:s0 + idx.size] = 3 * uu - uAv
        E2[s0:s0 + idx.size] = 2 * uu - uAv
    return Eq, E3, E2

def inv_dim(P, N, q, rng):
    n = 2 * N; S = q**n; monos = monomials(n)
    samp = rng.integers(0, S, 4 * len(monos) + 200)
    Mat = (eval_monos(digits_of(P[samp].astype(np.int64), n, q), monos)
           - eval_monos(digits_of(samp, n, q), monos)).T % q
    B = nullspace_mod_p(Mat, q)
    good = True; ch = 1 << 16
    for s0 in range(0, S, ch):
        idx = np.arange(s0, min(S, s0 + ch), dtype=np.int64)
        V1 = (B @ eval_monos(digits_of(idx, n, q), monos)) % q
        V2 = (B @ eval_monos(digits_of(P[s0:s0 + idx.size].astype(np.int64), n, q), monos)) % q
        good &= bool(np.all(V1 == V2))
    return B.shape[0], good

def census(P, label):
    lab = cycle_labels(P); cl = np.bincount(lab, minlength=P.size); reps = np.nonzero(cl)[0]
    lens = np.sort(cl[reps])[::-1]
    complete = int(cl.sum()) == P.size
    tv = (traversal_cycles(P) == sorted(lens.tolist())) if P.size <= 500000 else None
    fixed = int((P == np.arange(P.size)).sum())
    print(f"  [{label}] cycles {reps.size}; largest {lens[0]} = {100 * lens[0] / P.size:.2f}% of |S|; "
          f"top5 {lens[:5].tolist()}; fixed points {fixed}; complete {complete}; traversal-match {tv}")
    return lab, cl, lens, complete and (tv is not False)

def instance(kind, d, L, q, rng):
    N = L**d; n = 2 * N; S = q**n; A = adjacency(d, L)
    if kind == "b":
        div = 3 if d == 3 else 2
        step, par, desc = step_b, div, f"(b) rounded new=((nn+1)//{div} - prv) % q"
    elif kind == "c":
        step, par, desc = step_c, None, "(c) SM 3.1 explicit state-dependent ring"
    else:
        alpha = pow(d, -1, q) if math.gcd(d, q) == 1 else 1
        step, par, desc = step_a, alpha, f"(a) control, alpha={alpha}"
    print(f"\n=== {desc}: d={d} L={L} q={q} |S|={S}")
    P = build(step, N, q, A, par)
    ok = {"K0 bijection": bool(np.bincount(P, minlength=S).max() == 1)}
    alpha_mod = pow(d, -1, q) if math.gcd(d, q) == 1 else 1
    Eq, E3, E2 = energies(N, q, A, alpha_mod)
    for name, E in (("E_q (mod q, alpha=%d)" % alpha_mod, Eq), ("E_R3 = 3|u|^2+3|v|^2-u.Av (Z)", E3),
                    ("E_R2 = 2|u|^2+2|v|^2-u.Av (Z)", E2)):
        frac = float(np.mean(E[P] != E))
        print(f"  K1 {name}: changed by one step at {100 * frac:.2f}% of states")
    if q in (3, 5, 7) and S <= 5 * 10**7:
        dim, good = inv_dim(P, N, q, rng)
        print(f"  K2 degree<=2 polynomial invariants over F_{q}: dimension {dim} (all verified on every state: {good})")
        ok["K2 invariant basis verified"] = good
    lab, cl, lens, okc = census(P, kind)
    ok["K3 census complete and cross-checked"] = okc
    big = lab[np.argmax(cl)]
    on_big = lab == big
    print(f"  K4 largest cycle visits {np.unique(Eq[on_big]).size} distinct E_q values (of {q}) and "
          f"{np.unique(E3[on_big]).size} distinct E_R3 values")
    for k, v in ok.items(): print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    return all(ok.values())

if __name__ == "__main__":
    rng = np.random.default_rng(3)
    allok = True
    # K-1 fidelity control: step_b equals the literal repository step functions
    def lit_nn(x): return sum(np.roll(x, s, a) for a in range(3) for s in (1, -1))      # lyapunov_v3.py
    def lit_step(cur, prv, q): return (((lit_nn(cur) + 1) // 3) - prv) % q
    fid = True
    for Lt, qt in ((2, 3), (4, 1 << 16), (5, 7)):
        A = adjacency(3, Lt); N = Lt**3
        for _ in range(20):
            cur = rng.integers(0, qt, (Lt, Lt, Lt)); prv = rng.integers(0, qt, (Lt, Lt, Lt))
            z = np.concatenate([prv.ravel(), cur.ravel()])[:, None]
            out = step_b(z, N, qt, A, 3)
            fid &= np.array_equal(out[N:, 0], lit_step(cur, prv, qt).ravel()) and np.array_equal(out[:N, 0], cur.ravel())
    for _ in range(50):                                                                  # mixing_battery.py 1D
        qt, Lt = 4, 5; cur = rng.integers(0, qt, Lt); prv = rng.integers(0, qt, Lt)
        sres = np.roll(cur, 1) + np.roll(cur, -1); lit = ((sres + 1) // 2 - prv) % qt
        out = step_b(np.concatenate([prv, cur])[:, None], Lt, qt, adjacency(1, Lt), 2)
        fid &= np.array_equal(out[Lt:, 0], lit)
    print(f"K-1 step_b reproduces lyapunov_v3.step and mixing_battery 1D step exactly: {fid}")
    allok &= bool(fid)
    for kind, d, L, q in (("a", 1, 5, 3), ("b", 1, 5, 3), ("b", 1, 5, 4), ("b", 3, 2, 2), ("b", 3, 2, 3),
                          ("a", 1, 4, 3), ("c", 1, 4, 3), ("c", 1, 5, 3), ("c", 1, 4, 5), ("c", 1, 6, 3)):
        allok &= instance(kind, d, L, q, rng)
    print("\nALL CONTROLS GREEN" if allok else "\nSOME CONTROL FAILED")
