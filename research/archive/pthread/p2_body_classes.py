"""P2: the candidate premises on test bodies, exactly.

Per polytope body (all extreme points listed) and per eball d (finite subsets of the sphere, which
give NECESSARY conditions on every passive branch, hence sufficient for the scalar conclusion):

  SIMPLEX   conv(vertices) is a simplex (exhaustive barycentric search, plib.is_simplex_hull)
  EIG       linear maps M with every extreme ray hom(v) an eigenvector: solution-space dimension and
            the blocks (rays forced to share an eigenvalue).  Every branch of a passive readout
            (positive cone maps summing to the identity) lies in this space, because an extreme ray
            that is a sum of cone vectors is a sum of multiples of itself.
  NIWD      one block: every passive branch is a scalar on the span of the body (uninformative).
            (v1 of this probe used 'solution-space dimension 1', wrong for bodies that are not
            full-dimensional in their ambient coordinates; recorded in the ledger.)
  PI        passive incompleteness: some block holds >= 2 extreme rays, so no passive readout
            separates those two pure states.  If all blocks are singletons the body must be a
            simplex and the barycentric measure-and-prepare readout is passive and separating
            (constructed and checked).
  NRR       no reconstructing record: no readout (e_i) and preparations (y_i) with x = sum e_i(x) y_i.
            A reconstructing record is a passive separating readout, so PI => NRR; for simplices the
            barycentric record is constructed and checked.
  PBIN      no binary readout is injective on the pure states (an injective coordinate functional is
            searched on polytopes and normalised to a sharp seed)
  INCOMP    two binary readouts with no joint 4-outcome readout: for effects that are 0/1 on every
            vertex the joint element g11 is forced vertexwise; inconsistency = incompatibility.
            Simplices: the product joint readout is built for sample effects and checked.
  EXTDEC    some state has two different decompositions into pure states (affine dependence of
            vertices -> two decompositions, checked)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from itertools import product
from plib import affine_dim, is_simplex_hull, eig_blocks, hom, nullspace, barycentric, solve, fr, rank
from bodies import BODIES

checks = []


def chk(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


def affine_eval(coef, x):  # coef = (a, b1..bn): a + b.x
    return coef[0] + sum(c * xi for c, xi in zip(coef[1:], x))


def fit_affine(points, values):
    """Affine functional through the given (point, value) pairs, or None if inconsistent."""
    A = [[F(1)] + [fr(a) for a in p] for p in points]
    return solve(A, values)


def bary_record(verts):
    """Barycentric readout on a simplex: e_i = barycentric coordinate i (affine), y_i = vertex i."""
    k = len(verts)
    es = []
    for i in range(k):
        vals = [F(int(i == j)) for j in range(k)]
        es.append(fit_affine(verts, vals))
    return es


def check_reconstructs(verts, es, ys, test_points):
    for x in test_points:
        tot = [F(0)] * len(x)
        s = F(0)
        for e, y in zip(es, ys):
            w = affine_eval(e, x)
            if w < 0:
                return False
            s += w
            tot = [t + w * yy for t, yy in zip(tot, y)]
        if s != 1 or tuple(tot) != tuple(x):
            return False
    return True


def injective_functional(verts):
    n = len(verts[0])
    for base in range(2, 12):
        w = [F(base) ** i for i in range(n)]
        vals = [sum(a * b for a, b in zip(w, v)) for v in verts]
        if len(set(vals)) == len(vals):
            lo, hi = min(vals), max(vals)
            return w, [(x - lo) / (hi - lo) for x in vals]
    return None


def forced_joint(verts, ev, fv):
    """ev, fv: 0/1 values at vertices. g11 forced to min(e,f) = max(0, e+f-1) at each vertex.
    Returns the affine fit or None (inconsistent => no joint readout)."""
    g = [min(a, b) for a, b in zip(ev, fv)]
    return fit_affine(verts, g)


def ext_two_decomps(verts):
    """From an affine dependence sum c_i hom(v_i) = 0 build two different decompositions."""
    rows = [[hom(v)[r] for v in verts] for r in range(len(hom(verts[0])))]
    ns = nullspace(rows, len(verts))
    if not ns:
        return None
    c = ns[0]
    pos = [max(x, F(0)) for x in c]
    neg = [max(-x, F(0)) for x in c]
    sp = sum(pos)
    p1 = [w / sp for w in pos]
    p2 = [w / sp for w in neg]
    x1 = [sum(p1[i] * verts[i][j] for i in range(len(verts))) for j in range(len(verts[0]))]
    x2 = [sum(p2[i] * verts[i][j] for i in range(len(verts))) for j in range(len(verts[0]))]
    return p1, p2, x1, x2


table = {}
for name, (verts, desc) in BODIES.items():
    print(f"== {name}: {desc}")
    dim = affine_dim(verts)
    simp, _ = is_simplex_hull(verts)
    rays = [hom(v) for v in verts]
    soldim, blocks = eig_blocks(rays)
    niwd = (len(blocks) == 1)  # all extreme rays share one eigenvalue => M = lam*I on their span
    pi = any(len(b) >= 2 for b in blocks)
    print(f"   affine dim {dim}; simplex {simp}; eigen-solution dim {soldim}; blocks {blocks}")
    # consistency of PI with simplex (written theorem: PI <=> non-simplex)
    chk(f"{name}: PI (some block >= 2 rays) iff not simplex", pi == (not simp))
    if simp:
        es = bary_record(verts)
        cent = [sum(v[j] for v in verts) / len(verts) for j in range(len(verts[0]))]
        ok = check_reconstructs(verts, es, verts, verts + [tuple(cent)])
        chk(f"{name}: barycentric record reconstructs every state (passive, separating) => NOT NRR, NOT PI", ok)
        # complete readout context: deterministic and separating on the pure states
        det = all(affine_eval(e, v) in (0, 1) for e in es for v in verts)
        sep = len({tuple(affine_eval(e, v) for e in es) for v in verts}) == len(verts)
        chk(f"{name}: complete readout context exists (deterministic + separating on pure states)", det and sep)
        nrr = False
    else:
        nrr = True  # PI => NRR (a reconstructing record is a passive separating readout)
    # PBIN: an injective normalized binary readout on the vertices
    inj = injective_functional(verts)
    pbin = inj is None
    chk(f"{name}: a binary readout injective on pure states exists (PBIN fails on every polytope)", not pbin)
    # incompatibility
    if simp:
        # product joint readout for two sample (non-sharp) effects, values at vertices
        ev = [F(i + 1, len(verts) + 2) for i in range(len(verts))]
        fv = [F(len(verts) - i, len(verts) + 3) for i in range(len(verts))]
        ok = True
        g = {}
        for a, b in product((0, 1), repeat=2):
            vals = [(ev[i] if a else 1 - ev[i]) * (fv[i] if b else 1 - fv[i]) for i in range(len(verts))]
            g[(a, b)] = vals
            ok &= all(0 <= x <= 1 for x in vals)
        ok &= all(g[(1, 0)][i] + g[(1, 1)][i] == ev[i] and g[(0, 1)][i] + g[(1, 1)][i] == fv[i]
                  for i in range(len(verts)))
        chk(f"{name}: simplex => sample effects jointly readable (product joint readout)", ok)
        incomp = False
    else:
        found = None
        n = len(verts[0])
        cands = []
        for w in product([-2, -1, 0, 1, 2], repeat=n):
            for c in [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]:
                vals = [c + sum(F(wi) * xi for wi, xi in zip(w, v)) / 2 for v in verts]
                if all(x in (0, 1) for x in vals) and 0 in vals and 1 in vals:
                    cands.append(vals)
        for ev, fv in product(cands, cands):
            if forced_joint(verts, ev, fv) is None:
                found = (ev, fv)
                break
        incomp = found is not None
        chk(f"{name}: non-simplex => an incompatible pair of sharp binary readouts found", incomp)
        if found:
            print(f"   e@verts={[str(x) for x in found[0]]} f@verts={[str(x) for x in found[1]]}")
    dec = ext_two_decomps(verts)
    extdec = dec is not None and dec[0] != dec[1]
    if extdec:
        chk(f"{name}: two decompositions into pure states give the same state", dec[2] == dec[3])
    chk(f"{name}: EXTDEC iff not simplex", extdec == (not simp))
    table[name] = dict(dim=dim, simplex=simp, HTST=dim >= 2, NIWD=niwd, PI=pi, NRR=nrr, PBIN=pbin,
                       INCOMP=incomp, EXTDEC=extdec, blocks=blocks)

# eball d: finite sphere subsets (necessary conditions)
print("== eball d (finite subsets of the unit sphere; necessary conditions on passive branches)")
for d in (1, 2, 3):
    pts = []
    for i in range(d):
        for s in (1, -1):
            pts.append(tuple(F(s) if j == i else F(0) for j in range(d)))
    soldim, blocks = eig_blocks([hom(p) for p in pts])
    print(f"   eball {d}: rays +-e_i; eigen-solution dim {soldim}; blocks {blocks}")
    if d == 1:
        chk("eball 1: two singleton blocks (passive separating readout possible)", soldim == 2)
        # the measure-and-prepare readout along sharpEff z1: e(x) = 1/2 + x/2, y = (+1, -1)
        es = [(F(1, 2), F(1, 2)), (F(1, 2), F(-1, 2))]
        ok = check_reconstructs(pts, es, [(F(1),), (F(-1),)], [(F(1),), (F(-1),), (F(1, 3),), (F(0),)])
        chk("eball 1: record {sharpEff z1, sharpEff (-z1)} with re-preparation (+1,-1) reconstructs every state", ok)
    else:
        chk(f"eball {d}: only scalar maps keep +-e_i as eigenvectors => NIWD, PI, NRR on eball {d}", soldim == 1 and len(blocks) == 1)
# eball 0: unit readout reconstructs the single state
chk("eball 0: the unit readout with y = the point reconstructs (NRR and PI fail at d = 0)",
    check_reconstructs([()], [(F(1),)], [()], [()]))

# incompatibility on eball 2 (hence eball d >= 2 on the e1-e2 plane): forced g11 for sharpEff e1, sharpEff e2
pts2 = [(F(1), F(0)), (F(-1), F(0)), (F(0), F(1)), (F(0), F(-1))]
ev = [F(1), F(0), F(1, 2), F(1, 2)]
fv = [F(1, 2), F(1, 2), F(1), F(0)]
# forced values: at -e1, -e2: 0 (g11 <= e, f); at e1: f=1/2 forced both ways (g11 <= f, g11 >= e+f-1)
forced = [F(1, 2), F(0), F(1, 2), F(0)]
g = fit_affine(pts2, forced)
val = affine_eval(g, (F(-3, 5), F(-4, 5)))
print(f"   eball 2: forced g11 = {[str(x) for x in g]}; g11(-3/5,-4/5) = {val}")
chk("eball 2: forced joint element is negative at the sphere point (-3/5,-4/5) => incompatible", val == F(-1, 10))
chk("eball 2: (-3/5,-4/5) is on the unit sphere", F(9, 25) + F(16, 25) == 1)

print("== summary table (polytopes)")
cols = ["dim", "simplex", "HTST", "PI", "NRR", "NIWD", "PBIN", "INCOMP", "EXTDEC"]
print("   " + "body".ljust(14) + " ".join(c.ljust(7) for c in cols))
for name, row in table.items():
    print("   " + name.ljust(14) + " ".join(str(row[c]).ljust(7) for c in cols))

# strictness witnesses
chk("strictness: tri has HTST but not PI (HTST does not imply PI)", table["tri"]["HTST"] and not table["tri"]["PI"])
chk("strictness: pyramid has PI but not NIWD (PI does not imply NIWD)", table["pyramid"]["PI"] and not table["pyramid"]["NIWD"])
chk("strictness: square has PI but not PBIN (PI does not imply PBIN)", table["square"]["PI"] and not table["square"]["PBIN"])
chk("classical HV witness: Spekkens octahedron satisfies PI, NRR, NIWD and INCOMP",
    all(table["spekkens_oct"][c] for c in ("PI", "NRR", "NIWD", "INCOMP")))
chk("every simplex fails PI, NRR, NIWD, PBIN, INCOMP, EXTDEC",
    all(not table[b][c] for b in ("seg", "tri", "tet") for c in ("PI", "NRR", "NIWD", "PBIN", "INCOMP", "EXTDEC")))

# Spekkens: the incompatible pair is NOT a pair of classical response functions on the ontic simplex
oct_v = BODIES["spekkens_oct"][0]
ev = [F(int(0 in (i, j))) for i in range(4) for j in range(i + 1, 4)]   # "ontic state 0 in the pair"
fv = [F(int(1 in (i, j))) for i in range(4) for j in range(i + 1, 4)]   # "ontic state 1 in the pair"
chk("spekkens_oct: the pair (0 in pair, 1 in pair) has no joint readout on the body", forced_joint(oct_v, ev, fv) is None)
# affine extension (fit on the 4 points spanning the hull's affine span, check on all 6, eval at ontic vertices)
A = [[F(1)] + list(v) for v in oct_v]
ecoef = solve(A, ev)
ont = [tuple(F(int(k == m)) for m in range(4)) for k in range(4)]
ext_vals = [affine_eval(ecoef, o) for o in ont] if ecoef else None
print(f"   spekkens_oct: affine extension of e to ontic vertices = {[str(x) for x in ext_vals]}")
chk("spekkens_oct: that body effect exceeds 1 at an ontic vertex (not a classical response function)",
    ext_vals is not None and max(ext_vals) > 1)

npass = sum(1 for _, c in checks if c)
print(f"{'ALL-PASS' if npass == len(checks) else 'SOME-FAIL'} {npass}/{len(checks)}")
