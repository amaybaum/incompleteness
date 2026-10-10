"""Exact check: the right-hand sides of the six homMap rotation lemmas and the three rotYpi
lemmas, computed from literal transcriptions of the Lean definitions
  rotFun t v = ![c*v0 - s*v1, s*v0 + c*v1, v2]
  cycEquiv v = ![v2, v0, v1],  cycEquiv.symm v = ![v1, v2, v0]
  (rotX t).linear v = cycEquiv (rotFun t (cycEquiv.symm v))
  homMap N v = vecCons (v 0) (N (vecTail v))
  rotYpi x i = ![-1, 1, -1] i * x i.
Decision rule (fixed before the first run): PASS iff every stated RHS equals the computed entry
symbolically AND the countercontrol (a deliberately wrong index convention: rotX taken as the
rotation of coordinates (0, 1)) differs on at least one stated entry."""
import sympy as sp
c, s = sp.symbols('c s')
v = sp.symbols('v0:4')
def rotFun(x): return [c*x[0] - s*x[1], s*x[0] + c*x[1], x[2]]
def cyc(x): return [x[2], x[0], x[1]]
def cycs(x): return [x[1], x[2], x[0]]
def rotX(x): return cyc(rotFun(cycs(x)))
def rotYpi(x): return [-1*x[0], 1*x[1], -1*x[2]]
def homMap(N, w): return [w[0]] + N(list(w[1:]))
checks = []
h3 = homMap(rotFun, v); hX = homMap(rotX, v); hY = homMap(rotYpi, v)
stated = [
  ("homMap_rot3_one", h3[1], c*v[1] - s*v[2]),
  ("homMap_rot3_two", h3[2], s*v[1] + c*v[2]),
  ("homMap_rot3_three", h3[3], v[3]),
  ("homMap_rotX_one", hX[1], v[1]),
  ("homMap_rotX_two", hX[2], c*v[2] - s*v[3]),
  ("homMap_rotX_three", hX[3], s*v[2] + c*v[3]),
  ("homMap_rotYpi_one", hY[1], -v[1]),
  ("homMap_rotYpi_two", hY[2], v[2]),
  ("homMap_rotYpi_three", hY[3], -v[3]),
]
ok = True
for name, got, want in stated:
    good = sp.simplify(got - want) == 0
    ok &= good
    print(f"{'PASS' if good else 'FAIL'}  {name}: computed {sp.expand(got)}  stated {want}")
# countercontrol: rotX misread as rotFun on coordinates (0,1)
hBad = homMap(rotFun, v)
cc = any(sp.simplify(hBad[i] - w) != 0 for i, w in [(1, v[1]), (2, c*v[2] - s*v[3]), (3, s*v[2] + c*v[3])])
print(f"{'PASS' if cc else 'FAIL'}  countercontrol: wrong axis convention differs from the stated rotX entries")
ok &= cc
print(f"{sum(1 for n,g,w in stated if sp.simplify(g-w)==0) + int(cc)}/{len(stated)+1}")
print("VERDICT", "PRECHECK-HOMMAP-PASS" if ok else "PRECHECK-HOMMAP-FAIL")
