"""Exploration only. Symbolic separation of phi from each family member, shape by shape.
A test class is (circle r, generic unit z); its feature at coordinate p is the symbol (S, m)
(value S z^m / 64, injective in (S,m) for generic z).  Member feature maps, Lean shapes:
 shape1: x -> x o s(pi,tau);  shape2: conj(x o s);  shape3: conj(x o rho) o s;  shape4: x o rho o s
 (conj on symbols: m -> -m;  s(pi,tau) p = ((pi i1,pi i2,pi i3),(tau j1,tau j2,tau j3))).
phi: conj on circle 0, identity elsewhere.  Greedy cover of all 576 (pi,tau) per shape by
(test circle, coordinate) mismatches."""
import itertools
from circles import COORDS, R, coord_data
cidx = {p: n for n, p in enumerate(COORDS)}
data = [[coord_data(*r)[p] for p in COORDS] for r in R]
perms = list(itertools.permutations(range(4)))
def sidx(pi, tau):
    return [cidx[((pi[p[0][0]], pi[p[0][1]], pi[p[0][2]]), (tau[p[1][0]], tau[p[1][1]], tau[p[1][2]]))] for p in COORDS]
rho = [cidx[((p[1][1], p[1][2], p[1][0]), p[0])] for p in COORDS]
S_ALL = {(pi, tau): sidx(pi, tau) for pi in perms for tau in perms}
def cj(sym): return (sym[0], -sym[1])
def member_sym(shape, pt, r, n):
    s = S_ALL[pt]
    x = data[r]
    if shape == 1: return x[s[n]]
    if shape == 2: return cj(x[s[n]])
    if shape == 3: return cj(x[rho[s[n]]])
    if shape == 4: return x[rho[s[n]]]
def phi_sym(r, n):
    return cj(data[r][n]) if r == 0 else data[r][n]
for shape in (1, 2, 3, 4):
    # for each member, set of (r, n) mismatches
    miss = {}
    for pt in S_ALL:
        miss[pt] = set((r, n) for r in range(9) for n in range(4096) if member_sym(shape, pt, r, n) != phi_sym(r, n))
    assert all(miss.values()), "some member agrees with phi everywhere!"
    # greedy cover
    uncovered = set(S_ALL); chosen = []
    from collections import Counter
    while uncovered:
        cnt = Counter()
        for pt in uncovered:
            for key in miss[pt]:
                cnt[key] += 1
        best, c = cnt.most_common(1)[0]
        chosen.append((best, COORDS[best[1]], c))
        uncovered = {pt for pt in uncovered if best not in miss[pt]}
    circles_used = sorted(set(b[0][0] for b in chosen))
    print("shape", shape, ": greedy cover size", len(chosen), "test circles", circles_used)
    for b in chosen: print("    circle", b[0][0], R[b[0][0]], "coord", b[1], "covers", b[2])
