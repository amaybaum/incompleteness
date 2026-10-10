"""Exploration only. (1) The isometry group of the union of the nine circles, counted as
(circle permutation sigma, per-circle maps z -> eps z or eps conj z) admitting an affine isometry,
i.e. preserving the Gram data of {c_r - c_0, a_r, b_r}.  (2) The family's image H on the union
(relabellings, conjugation, transpose) as a permutation group of a finite sample of classes.
(3) Whether the single-circle conjugation lies in H."""
import cmath
import itertools
import math
from circles import COORDS, R, circle_vectors, coord_data, dot

vecs = [circle_vectors(*r) for r in R]
cen = [c for (c, _, _) in vecs]
cosv = [[a + b for a, b in zip(A, B)] for (_, A, B) in vecs]
sinv = [[a - b for a, b in zip(A, B)] for (_, A, B) in vecs]
N = 9
D = [[a - b for a, b in zip(cen[k], cen[0])] for k in range(N)]
# Gram blocks
CC = [[dot(D[r], D[s]) for s in range(N)] for r in range(N)]
CA = [[dot(D[r], cosv[s]) for s in range(N)] for r in range(N)]
AA = [[dot(cosv[r], cosv[s]) for s in range(N)] for r in range(N)]
# centre differences relative to sigma(0): Gram of c_r - c_s is invariant: use full pairwise
CCfull = [[dot([a - b for a, b in zip(cen[r], cen[s])], [a - b for a, b in zip(cen[r], cen[s])]) for s in range(N)] for r in range(N)]
# inner products <c_r - c_t, a_s> for all r,t,s: store <c_r, a_s>
Ca = [[dot(cen[r], cosv[s]) for s in range(N)] for r in range(N)]


def count_iso():
    sols = []

    def ok_partial(sig, eps):
        k = len(sig)
        r = k - 1
        for s in range(k):
            if CCfull[r][s] != CCfull[sig[r]][sig[s]]:
                return False
            if eps[r] * eps[s] * AA[r][s] != AA[sig[r]][sig[s]]:
                return False
            # <c_r - c_s, a_t> for t in placed: must equal eps_t <c_sr - c_ss, a_st>
            for t in range(k):
                lhs = (Ca[r][t] - Ca[s][t]) * eps[t]
                rhs = Ca[sig[r]][sig[t]] - Ca[sig[s]][sig[t]]
                if lhs != rhs:
                    return False
                lhs = (Ca[t][r] - Ca[s][r]) * eps[r]
                rhs = Ca[sig[t]][sig[r]] - Ca[sig[s]][sig[r]]
                if lhs != rhs:
                    return False
        return True

    def rec(sig, eps):
        if len(sig) == N:
            sols.append((tuple(sig), tuple(eps)))
            return
        for t in range(N):
            if t in sig:
                continue
            for e in (1, -1):
                sig.append(t); eps.append(e)
                if ok_partial(sig, eps):
                    rec(sig, eps)
                sig.pop(); eps.pop()

    rec([], [])
    return sols


def feature(r, z):
    d = coord_data(*R[r])
    return tuple(S * z ** m / 64 for (S, m) in (d[p] for p in COORDS))


def key(v):
    return tuple((round(x.real, 9), round(x.imag, 9)) for x in v)


if __name__ == "__main__":
    sols = count_iso()
    print("(sigma, eps) pairs:", len(sols), " x 2^9 sine signs =", len(sols) * 2 ** 9)

    # sample of classes: each circle at +-e^{+-i t0}, plus +-1 (marked)
    t0 = 0.7
    params = [cmath.exp(1j * t0), -cmath.exp(1j * t0), cmath.exp(-1j * t0), -cmath.exp(-1j * t0), 1, -1]
    pts = []
    index = {}
    for r in range(N):
        for z in params:
            v = feature(r, z)
            k = key(v)
            if k not in index:
                index[k] = len(pts)
                pts.append(v)
    print("sample size", len(pts), "(expect 9*4 + 6 marked = 42)")
    rho = {p: ((p[1][1], p[1][2], p[1][0]), p[0]) for p in COORDS}
    cidx = {p: n for n, p in enumerate(COORDS)}

    def act_relabel(pi, tau):
        def f(v):
            return tuple(v[cidx[((pi[p[0][0]], pi[p[0][1]], pi[p[0][2]]), (tau[p[1][0]], tau[p[1][1]], tau[p[1][2]]))]] for p in COORDS)
        return f

    def act_conj(v):
        return tuple(x.conjugate() for x in v)

    def act_T(v):
        return tuple(v[cidx[rho[p]]].conjugate() for p in COORDS)

    def as_perm(f):
        out = []
        for v in pts:
            k = key(f(v))
            if k not in index:
                return None
            out.append(index[k])
        return tuple(out)

    perms = list(itertools.permutations(range(4)))
    gens = [as_perm(act_relabel(p, (0, 1, 2, 3))) for p in [(1, 0, 2, 3), (1, 2, 3, 0)]]
    gens += [as_perm(act_relabel((0, 1, 2, 3), p)) for p in [(1, 0, 2, 3), (1, 2, 3, 0)]]
    gens += [as_perm(act_conj), as_perm(act_T)]
    assert all(g is not None for g in gens), "family does not preserve the sample"
    ident = tuple(range(len(pts)))
    H = {ident}
    frontier = [ident]
    while frontier:
        nf = []
        for h in frontier:
            for g in gens:
                c = tuple(g[h[i]] for i in range(len(pts)))
                if c not in H:
                    H.add(c); nf.append(c)
        frontier = nf
    print("|H| on sample =", len(H))

    # single-circle conjugation of circle 0 (the Fourier circle)
    def phi(v):
        k = key(v)
        n = index[k]
        return v

    on0 = set(index[key(feature(0, z))] for z in params)
    phip = []
    for n, v in enumerate(pts):
        if n in on0:
            phip.append(index[key(act_conj(v))])
        else:
            phip.append(n)
    phip = tuple(phip)
    print("phi (conj on C0 only) in H:", phip in H)
    # isometry check numerically
    import random
    mx = 0
    def dist(u, v):
        return math.sqrt(sum(abs(a - b) ** 2 for a, b in zip(u, v)))
    for _ in range(200):
        r, s = random.randrange(N), random.randrange(N)
        z, w = cmath.exp(1j * random.uniform(0, 6.3)), cmath.exp(1j * random.uniform(0, 6.3))
        u, v = feature(r, z), feature(s, w)
        fu = feature(r, z.conjugate()) if r == 0 else u
        fv = feature(s, w.conjugate()) if s == 0 else v
        mx = max(mx, abs(dist(fu, fv) - dist(u, v)))
    print("phi distance defect (float):", mx)
    # countercontrol: quarter turn z -> i z on C0 only
    mx = 0
    for _ in range(200):
        r, s = 0, random.randrange(1, N)
        z, w = cmath.exp(1j * random.uniform(0, 6.3)), cmath.exp(1j * random.uniform(0, 6.3))
        u, v = feature(r, z), feature(s, w)
        fu = feature(r, 1j * z)
        mx = max(mx, abs(dist(fu, v) - dist(u, v)))
    print("countercontrol quarter-turn defect:", mx)
    # members of H fixing every sample point off C0 (excluding marked points of C0)
    fix_off = [h for h in H if all(h[n] == n for n in range(len(pts)) if n not in on0)]
    print("members of H fixing every sampled class off C0:", len(fix_off))
