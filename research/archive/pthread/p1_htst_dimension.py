"""P1: HasTwoSharpTests on polytope bodies is the statement 'affine dimension >= 2'.

For each body: (i) if affine dim >= 2, build an explicit witness (two normalized coordinate
functionals, checked to be sharp seeds and separated as the kernel predicate requires, all on
vertices -- sufficient because the functionals are affine and the body is the vertex hull);
(ii) if affine dim = 1, enumerate the sharp seeds (an affine e on a segment [p, q] with values in
[0,1] attaining 0 and 1 is determined by (e(p), e(q)) in {(1,0),(0,1)}) and check every pair is equal
or complementary on the body.  Exact rationals only.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from itertools import product
from plib import affine_dim, fr
from bodies import BODIES

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def normalized(vertices, w):
    vals = [sum(fr(a) * b for a, b in zip(w, v)) for v in vertices]
    lo, hi = min(vals), max(vals)
    if lo == hi:
        return None
    return [(x - lo) / (hi - lo) for x in vals]  # values of the sharp seed at the vertices


def htst_witness(vertices):
    n = len(vertices[0])
    cands = []
    for w in product([-1, 0, 1, 2], repeat=n):
        e = normalized(vertices, w)
        if e is not None:
            cands.append((w, e))
    for (w1, e), (w2, f) in product(cands, cands):
        sep1 = any(fv != ev for fv, ev in zip(f, e))
        sep2 = any(fv != 1 - ev for fv, ev in zip(f, e))
        sharp = (1 in e and 0 in e and 1 in f and 0 in f)
        if sep1 and sep2 and sharp:
            return w1, w2, e, f
    return None


for name, (verts, desc) in BODIES.items():
    k = affine_dim(verts)
    print(f"-- {name}: {desc}; affine dim {k}")
    wit = htst_witness(verts)
    if k >= 2:
        chk(f"{name}: dim>=2 and an explicit HasTwoSharpTests witness exists", wit is not None)
        if wit:
            print(f"   witness functionals w1={wit[0]} w2={wit[1]}; e@verts={[str(x) for x in wit[2]]} "
                  f"f@verts={[str(x) for x in wit[3]]}")
    else:
        chk(f"{name}: dim<=1 and the witness search finds none", wit is None)

# exhaustive segment check: sharp seeds on [p,q] are t and 1-t
seg = BODIES["seg"][0]
seeds = [(F(1), F(0)), (F(0), F(1))]  # (e(p), e(q)); affine on a segment => determined by endpoints
pair_ok = all((a == b) or (a[0] == 1 - b[0] and a[1] == 1 - b[1]) for a in seeds for b in seeds)
chk("seg: every pair of sharp seeds equal or complementary (kernel eq_or_compl_one, d=1)", pair_ok)

# the trit is a classical simplex on which HasTwoSharpTests HOLDS
chk("tri (classical trit, a simplex) satisfies HasTwoSharpTests", htst_witness(BODIES["tri"][0]) is not None)
chk("tet (classical 4-simplex) satisfies HasTwoSharpTests", htst_witness(BODIES["tet"][0]) is not None)

npass = sum(1 for _, c in checks if c)
print(f"{'ALL-PASS' if npass == len(checks) else 'SOME-FAIL'} {npass}/{len(checks)}")
