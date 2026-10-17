#!/usr/bin/env python3
"""Exact controls for the written theorem 'a polytope satisfies SP iff it is a simplex'.

SP (Barnum-Mueller-Ududec Postulate 1, as used in #820): every state is a convex combination of
perfectly distinguishable pure states, distinguishability by any affine effects 0 <= e <= 1 on
the body (the most generous effect set).  The theorem (report.md, C3) is a written argument;
these are exact planar instances.  Standard library only.  Run:  python3 -I polytope_sp_exact.py

  PS1  triangle: the three vertices form a frame (barycentric effects); SP holds.
  PS2  square: all six vertex pairs are perfectly distinguishable (exact interval LP), no three
       vertices form a frame, and p = (1/2, 1/5) lies on no vertex segment: SP fails.
  PS3  hexagon: no three vertices form a frame, and p = (1/3, 1/7) lies on no segment between
       a distinguishable pair: SP fails.
"""
from fractions import Fraction as Fr
import itertools
import sys

MUT = set()
RESULTS = []
INF = None


def check(ok, cid, text):
    RESULTS.append((bool(ok), cid, text))


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1]


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def distinguishable(v, w, V):
    """Is there an affine e with e(v)=1, e(w)=0 and 0 <= e <= 1 on V?  e = e0 + tau*e1."""
    d = sub(v, w)
    nn = dot(d, d)

    def e0(x):
        return Fr(dot(sub(x, w), d), nn)

    def e1(x):
        return cross(sub(w, v), sub(x, v))

    lo, hi = None, None
    for u in V:
        a, b = e0(u), e1(u)
        lower_bound = Fr(0)
        # lower_bound <= a + tau b <= 1
        if b == 0:
            if not (lower_bound <= a <= 1):
                return False
            continue
        t1, t2 = (lower_bound - a) / b, (1 - a) / b
        l, h = (t1, t2) if b > 0 else (t2, t1)
        lo = l if lo is None else max(lo, l)
        hi = h if hi is None else min(hi, h)
    return lo is None or hi is None or lo <= hi


def triple_frame(tri, V):
    """The unique affine e_i with e_i(v_j) = delta_ij; frame iff 0 <= e_i <= 1 on V for all i."""
    a, b, c = tri
    det = cross(sub(b, a), sub(c, a))
    if det == 0:
        return False

    def bary(x):
        l1 = Fr(cross(sub(x, a), sub(c, a)), cross(sub(b, a), sub(c, a)))
        l2 = Fr(cross(sub(b, a), sub(x, a)), cross(sub(b, a), sub(c, a)))
        return (1 - l1 - l2, l1, l2)

    return all(all(0 <= lam <= 1 for lam in bary(u)) for u in V)


def on_segment(p, v, w):
    return cross(sub(w, v), sub(p, v)) == 0 and 0 <= dot(sub(p, v), sub(w, v)) <= dot(sub(w, v), sub(w, v))


def in_triangle(p, tri):
    a, b, c = tri
    s = [cross(sub(b, a), sub(p, a)), cross(sub(c, b), sub(p, b)), cross(sub(a, c), sub(p, c))]
    return all(x >= 0 for x in s) or all(x <= 0 for x in s)


def covered(p, V):
    pairs = [(v, w) for v, w in itertools.combinations(V, 2) if distinguishable(v, w, V) and distinguishable(w, v, V)]
    frames3 = [t for t in itertools.combinations(V, 3) if triple_frame(t, V)]
    return (any(on_segment(p, v, w) for v, w in pairs) or any(in_triangle(p, t) for t in frames3)
            or p in V), pairs, frames3


def sec():
    tri = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(0), Fr(1))]
    if "triangle_to_square" in MUT:
        tri = tri + [(Fr(1), Fr(1))]
    ok = len(tri) == 3 and triple_frame(tuple(tri), tri)
    pts = [(Fr(1, 3), Fr(1, 3)), (Fr(1, 7), Fr(2, 5)), (Fr(1, 2), Fr(0))]
    ok &= all(covered(p, tri)[0] for p in pts)
    check(ok, "PS1", "triangle: its vertices form a frame (barycentric effects in [0,1]); sample points lie in the frame simplex (SP holds)")
    sq = [(Fr(0), Fr(0)), (Fr(1), Fr(0)), (Fr(1), Fr(1)), (Fr(0), Fr(1))]
    p = (Fr(1, 2), Fr(1, 2)) if "point_on_diagonal" in MUT else (Fr(1, 2), Fr(1, 5))
    cov, pairs, frames3 = covered(p, sq)
    ok = len(pairs) == 6 and len(frames3) == 0 and not cov
    check(ok, "PS2", f"square: {len(pairs)} of 6 vertex pairs distinguishable, {len(frames3)} three-vertex frames, p = (1/2,1/5) on no frame segment: SP fails")
    hx = [(Fr(2), Fr(0)), (Fr(1), Fr(2)), (Fr(-1), Fr(2)), (Fr(-2), Fr(0)), (Fr(-1), Fr(-2)), (Fr(1), Fr(-2))]
    p = (Fr(0), Fr(0)) if "hex_center" in MUT else (Fr(1, 3), Fr(1, 7))
    cov, pairs, frames3 = covered(p, hx)
    ok = len(frames3) == 0 and not cov
    check(ok, "PS3", f"hexagon: {len(pairs)} distinguishable vertex pairs, {len(frames3)} three-vertex frames, p = (1/3,1/7) on no frame segment: SP fails")


MUTATIONS = {"triangle_to_square": "PS1", "point_on_diagonal": "PS2", "hex_center": "PS3"}


def run():
    RESULTS.clear()
    sec()
    return list(RESULTS)


def main():
    selftest = []
    for mut, target in MUTATIONS.items():
        MUT.clear()
        MUT.add(mut)
        res = run()
        failed = sorted({cid for ok, cid, _ in res if not ok})
        selftest.append((mut, target, target in failed, failed))
    MUT.clear()
    res = run()
    for ok, cid, text in res:
        print(("PASS " if ok else "FAIL ") + cid + "  " + text)
    print()
    for mut, target, hit, failed in selftest:
        print(("MUTATION-REJECTED " if hit else "MUTATION-MISSED ") + f"{mut}: target {target}; failing {','.join(failed)}")
    n_fail = sum(1 for ok, _, _ in res if not ok)
    n_miss = sum(1 for _, _, hit, _ in selftest if not hit)
    print()
    print(f"checks: {len(res)}, failures: {n_fail}; mutations: {len(selftest)}, missed: {n_miss}")
    if n_fail == 0 and n_miss == 0:
        print("VERDICT POLYTOPE-SP-EXACT: PASS (planar exact instances of a written theorem)")
        return 0
    print("VERDICT POLYTOPE-SP-EXACT: NOT ESTABLISHED")
    return 1


if __name__ == "__main__":
    sys.exit(main())
