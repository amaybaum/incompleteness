#!/usr/bin/env python3
"""Map (a): the exact Z/q-linear rule x_i(t+1) = alpha * sum_{j~i} x_j(t) - x_i(t-1)  (mod q)
(SM 4.1 Lemma / Substratum step (b) / ch02 2.4: f = alpha(x_1+...+x_2d) mod q; SM :296 states alpha=1).

Exhaustive, exact-integer enumeration of the whole phase space (u,v) = (x(t-1), x(t)).
Energy (the corpus's harmonic leapfrog energy reduced mod q):
    E(u,v) = u.u + v.v - alpha * u.A v      (mod q),   A = nearest-neighbour adjacency (np.roll convention)
For each instance:
  C0  F is a bijection (image is a permutation)
  C1  E is conserved at every state (exact)
  C2  E identity control: E == |v-u|^2 + u.(2I - alpha A) v as integer polynomials (kinetic + potential of the
      lattice Laplacian when alpha = 1/d), checked over Z on random integer vectors (not mod q)
  C3  degree<=2 polynomial invariants over F_p (p odd prime): dimension of the space, every basis element
      verified on ALL states; E lies in the span
  C4  cycle census per E-shell; completeness: cycle sizes sum to shell size, shells sum to q^(2N);
      every cycle lies inside one shell
  C5  cross-check of the census against a plain visited-array traversal (small instances)
  C6  planted controls on the same index set: one-cycle-per-shell permutation -> census must give 1 per shell;
      random permutation with a planted cycle type -> census must return exactly that multiset
Verdict text is generated from the measurements; it prints only if every control is green.
"""
import sys, itertools, math
import numpy as np

def adjacency(d, L):
    N = L**d
    A = np.zeros((N, N), dtype=np.int64)
    coords = list(itertools.product(range(L), repeat=d))
    index = {c: i for i, c in enumerate(coords)}
    for c in coords:
        i = index[c]
        for k in range(d):
            for s in (1, -1):
                c2 = list(c); c2[k] = (c2[k] + s) % L
                A[i, index[tuple(c2)]] += 1          # L=2: +e and -e coincide -> weight 2, as np.roll sum
    return A

def digits_of(idx, n, q):
    out = np.empty((n, idx.size), dtype=np.int64)
    t = idx.copy()
    for i in range(n):
        out[i] = t % q; t //= q
    return out

def index_of(dig, q):
    n = dig.shape[0]
    w = q ** np.arange(n, dtype=np.int64)
    return (dig * w[:, None]).sum(axis=0)

def cycle_labels(P):
    """lab[x] = min index on the cycle of x (pointer doubling). Exact for a permutation."""
    n = P.size
    lab = np.arange(n, dtype=P.dtype); Q = P.copy()
    for _ in range(max(1, int(math.ceil(math.log2(n)))) + 1):
        lab = np.minimum(lab, lab[Q]); Q = Q[Q]
    return lab

def traversal_cycles(P):
    n = P.size; seen = np.zeros(n, bool); lengths = []
    Pl = P.tolist()
    for s in range(n):
        if seen[s]: continue
        x = s; c = 0
        while not seen[x]:
            seen[x] = True; c += 1; x = Pl[x]
        lengths.append(c)
    return sorted(lengths)

def solve_nullspace_mod_p(Mat, p):
    """Return basis (rows) of {c : Mat c = 0 mod p}."""
    M = Mat.copy() % p
    rows, cols = M.shape
    piv = []; r = 0
    for c in range(cols):
        if r >= rows: break
        nz = np.nonzero(M[r:, c])[0]
        if nz.size == 0: continue
        k = r + nz[0]
        M[[r, k]] = M[[k, r]]
        inv = pow(int(M[r, c]), p - 2, p)
        M[r] = (M[r] * inv) % p
        others = np.nonzero(M[:, c])[0]
        for o in others:
            if o != r:
                M[o] = (M[o] - M[o, c] * M[r]) % p
        piv.append(c); r += 1
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        vec = np.zeros(cols, dtype=np.int64); vec[f] = 1
        for i, pc in enumerate(piv):
            vec[pc] = (-M[i, f]) % p
        basis.append(vec)
    return np.array(basis, dtype=np.int64).reshape(len(basis), cols)

def monomials(n):
    lin = [(i,) for i in range(n)]
    quad = [(i, j) for i in range(n) for j in range(i, n)]
    return lin + quad

def eval_monos(dig, monos):
    out = np.empty((len(monos), dig.shape[1]), dtype=np.int64)
    for k, m in enumerate(monos):
        out[k] = dig[m[0]] if len(m) == 1 else dig[m[0]] * dig[m[1]]
    return out

def run(d, L, q, alpha, quad_solver=True, traversal=True, seed=0):
    rng = np.random.default_rng(seed)
    N = L**d; n = 2 * N; S = q**n
    A = adjacency(d, L)
    M = np.zeros((n, n), dtype=np.int64)
    M[:N, N:] = np.eye(N, dtype=np.int64)
    M[N:, :N] = -np.eye(N, dtype=np.int64)
    M[N:, N:] = alpha * A
    print(f"\n=== map (a): d={d} L={L} N={N} q={q} alpha={alpha}  |S| = q^{n} = {S}")
    ok = {}
    # C2: energy identity over Z (not mod q)
    good = True
    for _ in range(200):
        u = rng.integers(-50, 50, N); v = rng.integers(-50, 50, N)
        E1 = u @ u + v @ v - alpha * (u @ (A @ v))
        E2 = (v - u) @ (v - u) + u @ ((2 * np.eye(N, dtype=np.int64) - alpha * A) @ v)
        # conservation over Z too (exact integer identity)
        u2, v2 = v, alpha * (A @ v) - u
        E3 = u2 @ u2 + v2 @ v2 - alpha * (u2 @ (A @ v2))
        good &= (E1 == E2) and (E1 == E3)
    ok['C2 energy identity/conservation over Z'] = bool(good)
    # build F and E on all states
    chunk = 1 << 21
    P = np.empty(S, dtype=np.int64 if S > 2**31 - 1 else np.int32)
    E = np.empty(S, dtype=np.int8)
    for s0 in range(0, S, chunk):
        idx = np.arange(s0, min(S, s0 + chunk), dtype=np.int64)
        z = digits_of(idx, n, q)
        z2 = (M @ z) % q
        P[s0:s0 + idx.size] = index_of(z2, q)
        u, v = z[:N], z[N:]
        E[s0:s0 + idx.size] = ((u * u).sum(0) + (v * v).sum(0) - alpha * (u * (A @ v)).sum(0)) % q
    ok['C0 bijection'] = bool(np.bincount(P, minlength=S).max() == 1)
    ok['C1 E conserved at every state'] = bool(np.all(E[P] == E))
    # C3: polynomial invariants of degree <= 2 over F_p
    inv_codes = None; dim_inv = None
    if quad_solver and q in (3, 5, 7, 11, 13):
        monos = monomials(n)
        samp = rng.integers(0, S, 4 * len(monos) + 200)
        z = digits_of(samp, n, q); z2 = digits_of(P[samp].astype(np.int64), n, q)
        Mat = (eval_monos(z2, monos) - eval_monos(z, monos)).T % q
        B = solve_nullspace_mod_p(Mat, q)
        dim_inv = B.shape[0]
        # verify every basis invariant on ALL states; build joint invariant code
        allgood = True
        codes = np.zeros(S, dtype=np.int64)
        base = 1
        chunk2 = 1 << 17
        for s0 in range(0, S, chunk2):
            idx = np.arange(s0, min(S, s0 + chunk2), dtype=np.int64)
            z = digits_of(idx, n, q); z2 = digits_of(P[s0:s0 + idx.size].astype(np.int64), n, q)
            V1 = (B @ eval_monos(z, monos)) % q
            V2 = (B @ eval_monos(z2, monos)) % q
            allgood &= bool(np.all(V1 == V2))
            w = np.array([q**k for k in range(dim_inv)], dtype=object) if dim_inv > 39 else q ** np.arange(dim_inv, dtype=np.int64)
            if dim_inv <= 39:
                codes[s0:s0 + idx.size] = (V1 * w[:, None]).sum(0)
            else:
                raise SystemExit("too many invariants for int64 code")
        ok['C3 every degree<=2 invariant basis element conserved on all states'] = allgood
        # E in span: coefficient vector of E
        ev = np.zeros(len(monos), dtype=np.int64); mi = {m: k for k, m in enumerate(monos)}
        for i in range(n): ev[mi[(i, i)]] += 1
        for i in range(N):
            for j in range(N):
                if A[i, j]:
                    a, b = i, N + j
                    ev[mi[(min(a, b), max(a, b))]] -= alpha * A[i, j]
        ev %= q
        rkB = np.linalg.matrix_rank  # not used over F_p; do exact check via elimination
        aug = solve_nullspace_mod_p(np.vstack([B, ev]).T % q, q)   # nontrivial relation with ev coeff !=0 ?
        inspan = any(r[-1] % q != 0 for r in aug)
        ok['C3b corpus energy E lies in the invariant span'] = bool(inspan)
        inv_codes = codes
    # C4: cycle census
    lab = cycle_labels(P)
    clen = np.bincount(lab, minlength=S)
    reps = np.nonzero(clen)[0]
    ok['C4a every cycle lies in one shell'] = bool(np.all(E[lab] == E))
    ok['C4b cycle sizes sum to |S|'] = int(clen.sum()) == S
    print(f"  cycles in whole space: {reps.size};  max cycle length {clen.max()};  distinct lengths {sorted(set(clen[reps].tolist()))}")
    shell_rows = []
    for e in range(q):
        mask_reps = reps[E[reps] == e]
        size_shell = int((E == e).sum())
        sum_cyc = int(clen[mask_reps].sum())
        ok[f'C4c shell E={e}: cycle sizes sum to shell size'] = (sum_cyc == size_shell)
        ninv = None
        if inv_codes is not None:
            ninv = int(np.unique(inv_codes[E == e]).size)
        lens = clen[mask_reps]
        shell_rows.append((e, size_shell, mask_reps.size, int(lens.max()), ninv,
                           dict(zip(*np.unique(lens, return_counts=True)))))
    for e, sz, nc, mx, ninv, hist in shell_rows:
        hs = ", ".join(f"{int(k)}x{int(v)}" for k, v in sorted(hist.items()))
        print(f"  shell E={e}: size {sz}, cycles {nc}, largest cycle {mx}"
              + (f", distinct joint-invariant values {ninv}" if ninv is not None else "")
              + f"\n      cycle-length histogram (length x count): {hs}")
    if dim_inv is not None:
        print(f"  degree<=2 polynomial invariants over F_{q} (no constant): dimension {dim_inv}")
    # C5: traversal cross-check
    if traversal and S <= 400000:
        ok['C5 census == plain traversal'] = traversal_cycles(P) == sorted(clen[reps].tolist())
    # C6 planted controls on the same index set
    Pl = np.empty_like(P)
    for e in range(q):
        mem = np.nonzero(E == e)[0]
        Pl[mem] = np.roll(mem, -1)
    labp = cycle_labels(Pl)
    ok['C6a planted one-cycle-per-shell detected as 1 cycle per shell'] = all(
        np.unique(labp[E == e]).size == 1 for e in range(q))
    perm = rng.permutation(S)
    planted = [1, 1, 2, 3, 5, 7]; rest = S - sum(planted)
    planted.append(rest)
    Pr = np.empty(S, dtype=P.dtype); pos = 0
    for c in planted:
        seg = perm[pos:pos + c]; Pr[seg] = np.roll(seg, -1); pos += c
    labr = cycle_labels(Pr); clr = np.bincount(labr, minlength=S)
    ok['C6b planted cycle type recovered exactly'] = sorted(clr[clr > 0].tolist()) == sorted(planted)
    allok = all(ok.values())
    for k, v in ok.items():
        print(f"  [{'PASS' if v else 'FAIL'}] {k}")
    if allok:
        split = [r for r in shell_rows if r[2] > 1]
        print(f"  VERDICT (controls green): {len(split)} of {q} energy shells split into more than one cycle; "
              f"no shell is a single cycle: {all(r[2] > 1 for r in shell_rows)}")
    else:
        print("  VERDICT VOID: a control failed")
    return allok, shell_rows

if __name__ == "__main__":
    allgreen = True
    cases = [(1, 5, 3, 1), (1, 4, 5, 1), (2, 3, 2, 1), (3, 2, 3, 1)]
    if len(sys.argv) > 1 and sys.argv[1] == "--small":
        cases = cases[:3]
    for d, L, q, a in cases:
        okc, _ = run(d, L, q, a, quad_solver=(q % 2 == 1), traversal=True)
        allgreen &= okc
    print("\nALL CONTROLS GREEN" if allgreen else "\nSOME CONTROL FAILED")
