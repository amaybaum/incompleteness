"""Thread C side probe (exact): ideal branch for an atomic edge-face test of the hexagon.
Hexagon taken in a rational affine frame (affinely equivalent to the regular hexagon):
vertices (1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1). Reuses update_controls.branch_query."""
import sys, io, contextlib
from fractions import Fraction as Fr
import sympy as sp
with contextlib.redirect_stdout(io.StringIO()):
    import update_controls as uc
V = [(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
RAYS = [(1,a,b) for a,b in V]
# facet inequalities of the cone from consecutive vertex pairs (exact cross products)
CONE = []
for i in range(6):
    p, q = sp.Matrix(RAYS[i]), sp.Matrix(RAYS[(i+1)%6])
    n = p.cross(q)
    if all((n.T*sp.Matrix(r))[0] >= 0 for r in RAYS): CONE.append(tuple(n))
    else: CONE.append(tuple(-n))
assert all(all(sum(c[k]*r[k] for k in range(3)) >= 0 for c in CONE) for r in RAYS)
u = (1,0,0); e = (Fr(1,2), Fr(1,2), 0)
vals = [uc.val(e, r) for r in RAYS]
print("e on vertices:", vals)
F1 = [r for r in RAYS if uc.val(e, r) == 1]; F0 = [r for r in RAYS if uc.val(e, r) == 0]
print("F_e:", F1, " F_(u-e):", F0, " ranks:", sp.Matrix(F1).rank(), sp.Matrix(F0).rank())
span_int = sp.Matrix(F1).rank() + sp.Matrix(F0).rank() - sp.Matrix(F1+F0).rank()
print("dim(span F_e ∩ span F_(u-e)) =", span_int)
feas, b, _ = uc.branch_query(RAYS, CONE, u, e, [(v, v) for v in F1], "hex ideal")
print("ideal branch exists?", feas)
assert span_int == 1 and feas is False
