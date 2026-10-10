"""BAL, node B3 pressure test: the derived necessary conditions must hold on every known valid gate.

For a gate G with frame + posFwd + posInv + relT(N), the written argument (LEDGER B3) derives, after normalization
Gt = G (I (x) M0^-1), with Fix sigma = span(u0):
  (a) every tangent block is L_{k,t} = [[0, alpha_{k,t} u0^T], [alpha_{k,t} u0, A_{k,t}]] with A_{k,t} u0 = 0;
  (b) alpha = (alpha_{k,t}) is orthogonal;
  (c) for each block B of u0-perp on which sigma = -I and which N preserves (B = V = Fix N - u0, or B = F = E-(N)),
      S_B = (alpha^T (x) I) K_B lies in so(T) (x) so(B), and so does S_B^{-1}.
This script extracts alpha and S_B from the actual gate matrices and checks (a)-(c) on:
  DIM-1's cnot (d = 3, nflip; transcribed in relt_common, NOT built by bal_gates), the landed gC5, the P3 gate
  (d = 5, dim Fix N = 3) and C7b (d = 7, balanced).  A violation on any of them would refute the derivation.
Countercontrol: the controlled-N gate (frame + relT, not positive) and gJ5 must fail (a)-(c) or the normal form.
"""
import sys
from sympy import Matrix, eye, zeros, diag
from relt_common import hom, homMap, apply, dim1_cnot, controlled_N_gate, sgate
from bal_gates import cstruct, signs_N, jk_gate_general, landed_gC5

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


def analyse(G, d, N):
    n = d + 1
    z = zeros(d, 1)
    z[d - 1] = 1
    hz, hm = hom(z), hom(-z)
    Ms = []
    for h in (hz, hm):
        cols = []
        for j in range(n):
            Y = zeros(n, 1)
            Y[j] = 1
            out = apply(G, h * Y.T)
            v = out[0, :].T
            if not (out - h * v.T).is_zero_matrix:
                return None
            cols.append(v)
        Ms.append(Matrix.hstack(*cols))
    M0, M1 = Ms
    if M0.det() == 0:
        return None
    S = M1 * M0.inv()
    sigma = S[1:, 1:]
    Tidx = list(range(1, d))
    M0i = M0.inv()
    blocks = {}
    for j in Tidx:
        for c in range(n):
            Y = zeros(n, 1)
            Y[c] = 1
            X = zeros(n, 1)
            X[j] = 1
            out = apply(G, X * (M0i * Y).T)
            if not (out[0, :].is_zero_matrix and out[d, :].is_zero_matrix):
                return None
            for k in Tidx:
                blocks.setdefault((k, j), zeros(n, n))
                blocks[(k, j)][:, c] = out[k, :].T
    fix = (sigma - eye(d)).nullspace()
    if len(fix) != 1:
        return dict(sigma=sigma, fix=len(fix))
    u0 = fix[0] / (fix[0].T * fix[0])[0, 0] ** 0  # keep exact; normalize below if a coordinate axis
    nz = [i for i in range(d) if u0[i] != 0]
    if len(nz) != 1:
        return dict(sigma=sigma, fix=1, nonaxis=True)
    ui = nz[0]
    u0 = zeros(d, 1)
    u0[ui] = 1
    m = d - 1
    alpha = zeros(m, m)
    shape_a = True
    for (k, t), L in blocks.items():
        a = L[1:, 0]
        A = L[1:, 1:]
        al = a[ui]
        rest = [a[i] for i in range(d) if i != ui]
        shape_a = shape_a and all(r == 0 for r in rest) and (L[0, 1:] - a.T).is_zero_matrix and \
            (A * u0).is_zero_matrix and L[0, 0] == 0
        alpha[Tidx.index(k), Tidx.index(t)] = al
    orth = (alpha.T * alpha - eye(m)).is_zero_matrix
    # the -1 blocks of sigma split by N: V = Fix N minus u0, F = E-(N)
    Ncoords = [N[i, i] for i in range(d)]
    assert N == diag(*Ncoords), "N must be diagonal here"
    assert all(sigma[i, j] == (1 if i == j == ui else (-1 if i == j else 0)) for i in range(d) for j in range(d)), \
        "sigma must be 2 u0 u0^T - I here"
    V = [i for i in range(d) if Ncoords[i] == 1 and i != ui]
    F = [i for i in range(d) if Ncoords[i] == -1]
    res = dict(shape_a=shape_a, orth=orth, blocks={})
    for name, B in (("V", V), ("F", F)):
        if not B:
            res["blocks"][name] = None
            continue
        b = len(B)
        # K_B on T (x) B: rows (k, i), cols (t, j), entry A_{k,t}[i, j]
        KB = zeros(m * b, m * b)
        for (k, t), L in blocks.items():
            A = L[1:, 1:]
            for ii, i in enumerate(B):
                for jj, j in enumerate(B):
                    KB[Tidx.index(k) * b + ii, Tidx.index(t) * b + jj] = A[i, j]
        SB = Matrix.vstack(*[Matrix.hstack(*[sum((alpha[kk, jx] * KB[kk * b:(kk + 1) * b, tx * b:(tx + 1) * b]
                                                  for kk in range(m)), zeros(b, b))
                                             for tx in range(m)]) for jx in range(m)])

        def in_soso(M):
            ok = True
            for jx in range(m):
                for tx in range(m):
                    blk = M[jx * b:(jx + 1) * b, tx * b:(tx + 1) * b]
                    tr = M[tx * b:(tx + 1) * b, jx * b:(jx + 1) * b]
                    ok = ok and (blk + blk.T).is_zero_matrix and (blk + tr).is_zero_matrix
            return ok
        inv = SB.det() != 0
        res["blocks"][name] = dict(dim=b, in_soso=in_soso(SB), invertible=inv,
                                   inv_in_soso=in_soso(SB.inv()) if inv else False)
    return res


cases = [
    ("DIM-1 cnot, d = 3, nflip", dim1_cnot(), 3, diag(1, -1, -1)),
    ("landed gC5, d = 5, nC5", landed_gC5(), 5, diag(1, -1, -1, -1, -1)),
    ("P3, d = 5, dim Fix N = 3", jk_gate_general(5, 1, cstruct(6, [(1, 2), (3, 4)]), cstruct(6, [(2, 3), (4, 5)]))["G"],
     5, signs_N(5, [0, 1, 2])),
    ("C7b, d = 7, balanced N7b", jk_gate_general(7, 1, cstruct(8, [(1, 2), (3, 4), (5, 6)]),
                                                  cstruct(8, [(2, 3), (4, 5), (6, 7)]))["G"], 7, signs_N(7, [0, 1, 2])),
]
for label, G, d, N in cases:
    r = analyse(G, d, N)
    ok_nf = r is not None and "shape_a" in r
    check(f"{label}: normal form with p_sigma = 1 on a coordinate axis", ok_nf)
    if not ok_nf:
        continue
    check(f"{label}: (a) blocks [[0, alpha u0^T], [alpha u0, A]] with A u0 = 0", r["shape_a"])
    check(f"{label}: (b) alpha orthogonal", r["orth"])
    for nm, info in r["blocks"].items():
        if info is None:
            print(f"     {label}: block {nm} empty")
            continue
        check(f"{label}: (c) block {nm} (dim {info['dim']}): S_B in so(T)(x)so(B), invertible, S_B^-1 in so(T)(x)so(B)",
              info["in_soso"] and info["invertible"] and info["inv_in_soso"])

print("== countercontrols (not positive): must fail the normal form or (a)-(c)")
Gc, _, _ = controlled_N_gate(Matrix([0, 0, 0, 0, 1]), diag(1, 1, -1, -1, -1))
r = analyse(Gc, 5, diag(1, 1, -1, -1, -1))
check("CC controlled-n5 gate (frame + relT, not positive): fails", r is None or "shape_a" not in r or not (
    r["shape_a"] and r["orth"]))
gJ5 = sgate([False, False, False, True, True, True], [5, 3, 4, 1, 2, 0], 6)
r = analyse(gJ5, 5, diag(1, 1, -1, -1, -1))
check("CC gJ5 (frame + relT + relC with n5, not positive): fails", r is None or "shape_a" not in r or not (
    r["shape_a"] and r["orth"]))

npass = sum(1 for _, c in checks if c)
print(f"bal_scond: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
