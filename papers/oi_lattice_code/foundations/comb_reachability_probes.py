#!/usr/bin/env python3
# b430/b431: which action-labelled combs a REVERSIBLE BOUNDED hidden sector can reach.
#
# b95 (repconsistency_probes.py) counts the comb family against a CP-instrument budget and finds
# generic combs unreachable at the passive dimension. b427 asked the complementary question --
# not "how big is the comb family" but "how much of it does OI's own construction reach" -- and
# measured the affine hull of the combs realizable by a bijective hidden sector of bounded size.
# That hull stops growing both with the horizon and with |C_H|, at a fixed fraction of the comb
# family's dimension. Two constraints explained part of it and a gap was left open.
#
# b430 closed the gap. The missing constraint is a SHIFT IDENTITY:
#
#     sum_{x_0} N(x_0, a_0 a_1..a_{K-1}, x_1 x_2..x_K) = sum_z N(x_1, a_1..a_{K-1} b, x_2..x_K z)
#
# for every a_0 and every b. Mechanism: psi_a is a bijection of S = C_V x C_H and the start
# measure is uniform on S, so the state at time 1 is AGAIN uniform on S. Averaging the K-step comb
# over the initial observation therefore reproduces the same comb one step shorter -- and that
# shorter comb is itself a marginal of the K-step comb, so the whole statement is a linear
# condition on the K-step comb alone. Forward causality says future actions cannot affect past
# outputs; this says the FIRST action and the FIRST observation cannot affect anything once
# averaged out, because reversibility makes the intermediate state uniform whatever happened first.
#
# b431 PROVES the dimension, and corrects it. Write Phi for "forget the first step" and M for the
# prefix marginal, "forget the last step" (by causality the last action drops with it). The shift
# identity says exactly Phi = M. Time reversal swaps the two, so C_K -- the space cut out by
# causality, normalization, unitality, reverse causality and the shift identity -- is reversal
# invariant, and the induction along M closes:
#
#   L1  M maps C_K INTO C_{K-1}. Causality, normalization and unitality are marginals of marginals.
#       Reverse causality is NOT routine, because reversal turns the last step into the FIRST; it
#       follows from R(M(v)) = Phi(R(v)) = M(R(v)), the middle step being the shift identity for
#       R(v), which lies in C_K by reversal invariance.
#   L2  M is ONTO C_{K-1}, by an explicit linear right inverse. For fixed (a_0 a_rest, x_1..x_{K-1})
#       the last step is a matrix A[x_0][x_K] whose ROW sums are fixed by M and whose COLUMN sums
#       are fixed by the shift identity. Their totals agree BECAUSE w satisfies the shift identity,
#       so the transportation problem is feasible, and A = r/nV + c/nV - T/nV^2 solves it linearly.
#   L3  ker(M|C_K) is exactly the ZERO-MARGIN space: those same matrices with zero row sums (from
#       M(v) = 0) and zero column sums (from the shift identity, whose right-hand side is M(v)).
#       Dimension (nV-1)^2 per block. It is closed under transpose, and reversal acts on it by
#       transposing, which is why reverse causality costs nothing there.
#
#   dim C_K = dim C_{K-1} + nV^{K-1} nA^K (nV-1)^2,  and summing gives  tot(K) (nV-1)/nV.
#
# So the "half" b427 and b430 saw is the nV = 2 case of dim(doubly stochastic)/dim(stochastic).
#
# SCOPE. What is characterized is the AFFINE HULL of the realizable set, not the realizable set
# itself, which is finite. The dimension of C_K is PROVED. That the realizable hull FILLS C_K
# rather than merely sitting inside it is reduced by the same induction to one claim -- the
# zero-margin space is spanned by differences of realizable combs -- which is verified at K <= 3
# and NOT proved in general. And this is the fixed-|C_H| sub-family: the framework's own
# construction grows C_H with the horizon and sits outside it, so none of these numbers bounds
# OI in general.
import itertools
import sys

import numpy as np

P = 1000003
nV = nA = 2                      # the case b427/b430 studied; BO5 sweeps others
CHECKS = []


# ------------------------------------------------------------------ layout, parameterized
def layout(K, nv=None, na=None):
    nv, na = nv or nV, na or nA
    trajs = list(itertools.product(range(nv), repeat=K))
    aseqs = list(itertools.product(range(na), repeat=K))
    tj = {t: i for i, t in enumerate(trajs)}
    aj = {a: i for i, a in enumerate(aseqs)}
    W = nv * len(aseqs) * len(trajs)
    def idx(x0, aseq, tr):
        return x0 * len(aseqs) * len(trajs) + aj[aseq] * len(trajs) + tj[tr]
    return trajs, aseqs, tj, aj, W, idx


def tot_dof(K, nv=None, na=None):
    """b95's count of the action-labelled comb family's free parameters."""
    nv, na = nv or nV, na or nA
    return sum(nv ** (k + 1) * na ** (k + 1) * (nv - 1) for k in range(K))


# ------------------------------------------------------------------ exact GF(p) linear algebra
def rref(M):
    M = np.asarray(M, dtype=np.int64).copy() % P
    if M.size == 0:
        return M, []
    rows, cols = M.shape
    piv, r = [], 0
    for c in range(cols):
        nz = np.nonzero(M[r:, c])[0]
        if nz.size == 0:
            continue
        k = r + int(nz[0])
        if k != r:
            M[[r, k]] = M[[k, r]]
        M[r] = (M[r] * pow(int(M[r, c]), P - 2, P)) % P
        col = M[:, c].copy()
        col[r] = 0
        hit = np.nonzero(col)[0]
        if hit.size:
            M[hit] = (M[hit] - np.outer(col[hit], M[r])) % P
        piv.append(c)
        r += 1
        if r == rows:
            break
    return M[:r], piv


def rank(M):
    M = np.asarray(M, dtype=np.int64)
    return 0 if M.size == 0 else rref(M)[0].shape[0]


def nullspace(M):
    M = np.asarray(M, dtype=np.int64)
    R, piv = rref(M)
    free = [c for c in range(M.shape[1]) if c not in piv]
    out = np.zeros((len(free), M.shape[1]), dtype=np.int64)
    for i, fc in enumerate(free):
        out[i, fc] = 1
        for r, c in enumerate(piv):
            out[i, c] = (-R[r, fc]) % P
    return out


def solution_dim(rows, W):
    return W - rank(rows)


def hull_dim(V):
    V = np.asarray(V, dtype=np.int64)
    return 0 if V.shape[0] < 2 else rank((V[1:] - V[0]) % P)


# ------------------------------------------------------------------ the constraint families
def causality_rows(K, nv=None, na=None):
    """For each j the j-step marginal may not depend on the actions from step j onward."""
    nv, na = nv or nV, na or nA
    trajs, aseqs, tj, aj, W, idx = layout(K, nv, na)
    rows = []
    for j in range(K):
        for x0 in range(nv):
            for head in itertools.product(range(na), repeat=j):
                for xs in itertools.product(range(nv), repeat=j):
                    base = None
                    for tail in itertools.product(range(na), repeat=K - j):
                        f = np.zeros(W, dtype=np.int64)
                        for rest in itertools.product(range(nv), repeat=K - j):
                            f[idx(x0, head + tail, xs + rest)] += 1
                        if base is None:
                            base = f
                        else:
                            rows.append((f - base) % P)
    return np.array(rows, dtype=np.int64) if rows else np.zeros((0, W), dtype=np.int64)


def normalization_rows(K, nv=None, na=None):
    """Every (x_0, action-sequence) block carries the same total mass."""
    nv, na = nv or nV, na or nA
    trajs, aseqs, tj, aj, W, idx = layout(K, nv, na)
    rows, base = [], None
    for x0 in range(nv):
        for aseq in aseqs:
            f = np.zeros(W, dtype=np.int64)
            for tr in trajs:
                f[idx(x0, aseq, tr)] = 1
            if base is None:
                base = f
            else:
                rows.append((f - base) % P)
    return np.array(rows, dtype=np.int64)


def comb_family_rows(K, nv=None, na=None):
    return np.vstack([causality_rows(K, nv, na), normalization_rows(K, nv, na)]) % P


def unital_rows(K, nv=None, na=None):
    """A bijection started uniform on S keeps every intermediate state uniform, so the x_j
    marginal averaged over x_0 does not depend on the value."""
    nv, na = nv or nV, na or nA
    trajs, aseqs, tj, aj, W, idx = layout(K, nv, na)
    rows = []
    for aseq in aseqs:
        for j in range(K):
            base = None
            for y in range(nv):
                f = np.zeros(W, dtype=np.int64)
                for x0 in range(nv):
                    for tr in trajs:
                        if tr[j] == y:
                            f[idx(x0, aseq, tr)] += 1
                if base is None:
                    base = f
                else:
                    rows.append((f - base) % P)
    return np.array(rows, dtype=np.int64) if rows else np.zeros((0, W), dtype=np.int64)


def rev_perm(K, nv=None, na=None):
    """psi_a^{-1} with the actions reversed is again a realization."""
    nv, na = nv or nV, na or nA
    trajs, aseqs, tj, aj, W, idx = layout(K, nv, na)
    pm = np.zeros(W, dtype=np.int64)
    for x0 in range(nv):
        for aseq in aseqs:
            for tr in trajs:
                f2 = ((x0,) + tr)[::-1]
                pm[idx(x0, aseq, tr)] = idx(f2[0], aseq[::-1], f2[1:])
    return pm


def shift_rows(K, nv=None, na=None):
    """THE constraint: forget the first step = restart at time 1. See the header."""
    nv, na = nv or nV, na or nA
    trajs, aseqs, tj, aj, W, idx = layout(K, nv, na)
    if K < 2:
        return np.zeros((0, W), dtype=np.int64)
    rows = []
    for a0 in range(na):
        for a_rest in itertools.product(range(na), repeat=K - 1):
            for x1 in range(nv):
                for x_rest in itertools.product(range(nv), repeat=K - 1):
                    for b in range(na):
                        f = np.zeros(W, dtype=np.int64)
                        for x0 in range(nv):
                            f[idx(x0, (a0,) + a_rest, (x1,) + x_rest)] += 1
                        for z in range(nv):
                            f[idx(x1, a_rest + (b,), x_rest + (z,))] -= 1
                        rows.append(f % P)
    return np.array(rows, dtype=np.int64)


def proved_rows(K, nv=None, na=None):
    """Exactly what b427 established: causality + unitality, each also time-reversed."""
    base = np.vstack([comb_family_rows(K, nv, na), unital_rows(K, nv, na)]) % P
    return np.vstack([base, base[:, rev_perm(K, nv, na)]]) % P


def constrained_rows(K, nv=None, na=None):
    """Everything, including the shift identity: the space called C_K."""
    return np.vstack([proved_rows(K, nv, na), shift_rows(K, nv, na)]) % P


# ------------------------------------------------------------------ the induction along M
def prefix_marginal(K, b=0, nv=None, na=None):
    """M: sum out the last output. By causality the choice of last action b is immaterial."""
    nv, na = nv or nV, na or nA
    trajs, aseqs, tj, aj, W, idx = layout(K, nv, na)
    _, aseqs_p, tj_p, aj_p, Wp, idx_p = layout(K - 1, nv, na)
    M = np.zeros((Wp, W), dtype=np.int64)
    for x0 in range(nv):
        for ap in aseqs_p:
            for xp in tj_p:
                for z in range(nv):
                    M[idx_p(x0, ap, xp), idx(x0, ap + (b,), xp + (z,))] = 1
    return M


def append_map(K, nv=None, na=None):
    """L2's right inverse: A[x_0][x_K] = r/nV + c/nV - T/nV^2, with r the row sums M fixes and c
    the column sums the shift identity fixes."""
    nv, na = nv or nV, na or nA
    trajs, aseqs, tj, aj, W, idx = layout(K, nv, na)
    _, aseqs_p, tj_p, aj_p, Wp, idx_p = layout(K - 1, nv, na)
    iN, iN2 = pow(nv, P - 2, P), pow(nv * nv, P - 2, P)
    A = np.zeros((W, Wp), dtype=np.int64)
    for x0 in range(nv):
        for aseq in aseqs:
            for tr in trajs:
                x1, mid, xK = tr[0], tr[1:K - 1], tr[K - 1]
                a0, a_rest = aseq[0], aseq[1:]
                here = idx(x0, aseq, tr)
                A[here, idx_p(x0, (a0,) + a_rest[:K - 2], (x1,) + mid)] += iN
                A[here, idx_p(x1, a_rest, mid + (xK,))] += iN
                for z in range(nv):
                    A[here, idx_p(x1, a_rest, mid + (z,))] -= iN2
    return A % P


def zero_margin_space(K, nv=None, na=None):
    """L3's kernel: zero row AND column sums per (action sequence, x_1..x_{K-1}) block."""
    nv, na = nv or nV, na or nA
    trajs, aseqs, tj, aj, W, idx = layout(K, nv, na)
    basis = []
    for aseq in aseqs:
        for mid in itertools.product(range(nv), repeat=K - 1):
            for u in range(nv - 1):
                for w in range(nv - 1):
                    f = np.zeros(W, dtype=np.int64)
                    for r, c, s in ((u, w, 1), (u, nv - 1, -1), (nv - 1, w, -1), (nv - 1, nv - 1, 1)):
                        f[idx(r, aseq, mid + (c,))] += s
                    basis.append(f % P)
    return np.array(basis, dtype=np.int64)


# ------------------------------------------------------------------ realizations
def comb_of(psis, K, nH, weights=None):
    trajs, aseqs, tj, aj, W, idx = layout(K)
    xof = [i // nH for i in range(nV * nH)]
    w = weights or [1] * nH
    v = [0] * W
    for x0 in range(nV):
        for aseq in aseqs:
            for h in range(nH):
                s = x0 * nH + h
                tr = []
                for a in aseq:
                    s = psis[a][s]
                    tr.append(xof[s])
                v[idx(x0, aseq, tuple(tr))] += w[h]
    return tuple(v)


def all_realizable(K, nH, bij=True):
    n = nV * nH
    maps = ([tuple(p) for p in itertools.permutations(range(n))] if bij
            else [tuple(t) for t in itertools.product(range(n), repeat=n)])
    return np.array(sorted({comb_of(ps, K, nH) for ps in itertools.product(maps, repeat=nA)}),
                    dtype=np.int64)


def sample_realizable(K, nH, N, seed=0xC0FFEE, weights=None):
    n = nV * nH
    s = seed
    def rp():
        nonlocal s
        p = list(range(n))
        for i in range(n - 1, 0, -1):
            s = (6364136223846793005 * s + 1442695040888963407) % (1 << 64)
            j = (s >> 33) % (i + 1)
            p[i], p[j] = p[j], p[i]
        return p
    return np.array(sorted({comb_of([rp() for _ in range(nA)], K, nH, weights)
                            for _ in range(N)}), dtype=np.int64)


def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)


# ------------------------------------------------------------------ BO1
print("BO1  the comb family, and the shift identity on realizations")
ok = True
for K in range(1, 6):
    ok &= (solution_dim(comb_family_rows(K), layout(K)[4]) - 1 == tot_dof(K))
check("BO1a", ok, "the causality and normalization conditions cut the comb family to exactly b95's "
      f"count {[tot_dof(K) for K in range(1, 6)]} at K=1..5 -- written down exactly, not sampled, "
      "so an under-determined hull cannot silently corrupt every number downstream")

viol = []
for K in (2, 3):
    S = shift_rows(K)
    for nH in (2, 3):
        V = all_realizable(K, nH)
        viol.append((K, nH, V.shape[0], int(np.count_nonzero((V @ S.T) % P))))
check("BO1b", all(v[3] == 0 for v in viol),
      "the shift identity holds on EVERY realizable comb enumerated -- "
      + ", ".join(f"K={k} |C_H|={h}: 0/{n}" for k, h, n, _ in viol))

# ------------------------------------------------------------------ BO2
print("BO2  upper bound meets lower bound, so both are exact")
rows = []
for K in (1, 2, 3, 4):
    upper = solution_dim(constrained_rows(K), layout(K)[4]) - 1
    lower = hull_dim(sample_realizable(K, min(K + 1, 4), 4000))
    rows.append((K, upper, lower, tot_dof(K) // 2))
check("BO2", all(u == l == h for _, u, l, h in rows),
      "constraints (upper) and a sample of realizations (lower) agree at K=1..4 -- "
      + ", ".join(f"K={k}: {u}" for k, u, _, _ in rows)
      + " -- and each equals tot(K)/2, so the hull dimension AND the completeness of the "
        "characterization are established together")

# ------------------------------------------------------------------ BO3
print("BO3  what the proved-only ceiling was, and b427's K=5 prediction")
ceil_only = [solution_dim(proved_rows(K), layout(K)[4]) - 1 for K in range(1, 6)]
with_shift = [solution_dim(constrained_rows(K), layout(K)[4]) - 1 for K in range(1, 6)]
cum = [sum(tot_dof(j) // 2 for j in range(1, K + 1)) for K in range(1, 6)]
check("BO3a", ceil_only == [2, 12, 54, 224, 906],
      f"b427's proved-only ceiling reproduced and extended: {ceil_only}")
check("BO3b", ceil_only == cum,
      f"it is the cumulative sum of the realizable dimensions, {cum} -- so b427's K=5 figure of "
      "906 is DERIVED by a recursion rather than extrapolated, and is CONFIRMED")
check("BO3c", with_shift == [tot_dof(K) // 2 for K in range(1, 6)],
      f"adding the shift identity gives exactly tot(K)/2 at every horizon: {with_shift}")

# ------------------------------------------------------------------ BO4
print("BO4  countercontrols -- the identity encodes reversibility and the uniform prior")
c = {}
for K in (2, 3):
    Vm = all_realizable(K, 2, bij=False)
    c[K] = (Vm.shape[0], int(np.count_nonzero(((Vm @ shift_rows(K).T) % P).any(axis=1))))
V = sample_realizable(2, 3, 3000, weights=[1, 2, 3])
nu = (V.shape[0], int(np.count_nonzero(((V @ shift_rows(2).T) % P).any(axis=1))))
gap = [ceil_only[K - 1] - tot_dof(K) // 2 for K in (2, 3, 4)]
check("BO4a", all(v > 0.9 * n for n, v in c.values()),
      "dropping bijectivity breaks it in bulk -- "
      + ", ".join(f"K={k}: {v} of {n} all-maps combs violate it" for k, (n, v) in c.items()))
check("BO4b", nu[1] > 0.8 * nu[0],
      f"a non-uniform hidden prior breaks it too: {nu[1]} of {nu[0]} bijective-but-non-uniform "
      "realizations violate it, so the uniform start is load-bearing and not decoration")
check("BO4c", gap == [2, 12, 54],
      f"and without the shift identity the gap re-opens, {gap} at K=2,3,4 -- the new constraint "
      "is what closes it, not a restatement of the old ones")

# ------------------------------------------------------------------ BO5  (b431)
print("BO5  the law is (nV-1)/nV, not one half")
gen = []
for NV, NA, KS in ((2, 2, (1, 2, 3)), (3, 2, (1, 2)), (2, 3, (1, 2))):
    for K in KS:
        W = layout(K, NV, NA)[4]
        d = solution_dim(constrained_rows(K, NV, NA), W) - 1
        gen.append((NV, NA, K, d, tot_dof(K, NV, NA) * (NV - 1) // NV))
check("BO5a", all(d == p for *_, d, p in gen),
      "dim C_K = tot(K)(nV-1)/nV at "
      + ", ".join(f"(nV={a},nA={b},K={c}):{d}" for a, b, c, d, _ in gen)
      + " -- so the halving b427 and b430 saw is the nV=2 case of dim(doubly stochastic)/"
        "dim(stochastic) = (nV-1)/nV, not a fact about two-outcome combs")
check("BO5b", any(a == 3 and c == 2 and d == 56 for a, b, c, d, _ in gen),
      "and nV=3, K=2 gives 56, which is the hull dimension b427 measured by direct enumeration at "
      "nV=3, |C_H|=2 -- two independent routes to the same number")

# ------------------------------------------------------------------ BO6
print("BO6  L1 and L2: M maps C_K into C_(K-1), and onto it")
l12 = []
for K in (2, 3, 4):
    B, Bp = nullspace(constrained_rows(K)), nullspace(constrained_rows(K - 1))
    Mk = prefix_marginal(K)
    img = (B @ Mk.T) % P
    inside = not np.count_nonzero((img @ constrained_rows(K - 1).T) % P)
    V = (Bp @ append_map(K).T) % P
    lands = not np.count_nonzero((V @ constrained_rows(K).T) % P)
    l12.append((K, inside, lands, np.array_equal((V @ Mk.T) % P, Bp % P),
                rank(img) == Bp.shape[0]))
check("BO6", all(i and l and r and s for _, i, l, r, s in l12),
      "at K=2,3,4 the prefix marginal lands inside C_(K-1) (L1 -- including reverse causality, "
      "which follows from the shift identity intertwining forget-first with forget-last), and the "
      "explicit linear right inverse A = r/nV + c/nV - T/nV^2 lands in C_K and inverts it (L2), "
      "so M is onto")

# ------------------------------------------------------------------ BO7
print("BO7  L3: the kernel is exactly the zero-margin matrices")
l3 = []
for K in (2, 3, 4):
    Z = zero_margin_space(K)
    dz = rank(Z)
    pred = nV ** (K - 1) * nA ** K * (nV - 1) ** 2
    inside = not np.count_nonzero((Z @ constrained_rows(K).T) % P)
    killed = not np.count_nonzero((Z @ prefix_marginal(K).T) % P)
    revinv = rank(np.vstack([Z, Z[:, rev_perm(K)]]) % P) == dz
    B = nullspace(constrained_rows(K))
    kdim = B.shape[0] - rank((B @ prefix_marginal(K).T) % P)
    l3.append((K, dz, pred, inside, killed, revinv, kdim))
check("BO7", all(d == p == k and i and s and r for _, d, p, i, s, r, k in l3),
      "at K=2,3,4 the zero-margin space sits in C_K, is killed by M, is closed under time reversal "
      "(reversal transposes it, which is why reverse causality costs nothing there), and its "
      f"dimension nV^(K-1) nA^K (nV-1)^2 = {[d for _, d, *_ in l3]} is exactly dim ker(M|C_K) -- "
      "so dim C_K = dim C_(K-1) + that, and summing gives tot(K)(nV-1)/nV")

# ------------------------------------------------------------------ BO8
print("BO8  what is proved, and what is still only measured")
fill = []
for K, nH, N in ((2, 2, None), (2, 3, None), (3, 2, None), (3, 3, 20000)):
    V = all_realizable(K, nH) if N is None else sample_realizable(K, nH, N)
    D = (V[1:] - V[0]) % P
    rD = rank(D)
    fill.append((K, nH, rD, rank(np.vstack([D, zero_margin_space(K)]) % P) == rD))
check("BO8", [(K, h, ok) for K, h, _, ok in fill] == [(2, 2, True), (2, 3, True),
                                                      (3, 2, False), (3, 3, True)],
      "the remaining step -- that the realizable hull FILLS C_K rather than merely sitting inside "
      "it -- reduces by the same induction to: the zero-margin space is spanned by differences of "
      "realizable combs. True once |C_H| is large enough for the hull to stabilize (K=2 at "
      f"|C_H|=2, K=3 at |C_H|=3) and FALSE at K=3, |C_H|=2 where the hull is only {fill[2][2]} of "
      "42 -- so the claim is sharp, and is about the stabilized hull. Verified at K<=3, NOT proved")

print()
print("     [scope] The affine HULL is characterized, not the realizable set, which is finite.")
print("     dim C_K = tot(K)(nV-1)/nV is PROVED (L1-L3 above). That the realizable hull fills C_K")
print("     is reduced to one claim, verified at K <= 3 and not proved. This is the fixed-|C_H|")
print("     sub-family -- the framework's own construction grows C_H with the horizon and sits")
print("     outside it, so no number here bounds OI in general.")
print()
print("comb_reachability_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
