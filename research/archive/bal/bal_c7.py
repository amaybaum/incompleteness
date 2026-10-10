"""BAL, node B1: a balanced NOT at d = 7 carrying a gate with the frame, relT and two-sided positivity.

N7b = diag(1, 1, 1, -1, -1, -1, -1) on R^7, z = e_7: homogenized eigenspaces of dimension 4 and 4 (balanced).
Gate C7b = jk_gate_general(7, u = 1, J, K) with sigma = diag(1, -1, ..., -1) != N7b,
  J pairs (1,2),(3,4),(5,6) on the tangent indices,
  K pairs (2,3),(4,5),(6,7) on E-(sigma): it preserves V = {2,3} (N = +1) and F = {4,5,6,7} (N = -1).

Checks (exact): IsNot, balance, frame, relT for N7b, G^2 = I, relC fails (explicit entry), sigma != N7b,
the normal form (corner maps I and homMap sigma; tangent outputs in T; blocks in Lsig(sigma) and commuting with
homMap N7b; tangent block invertible), the six certificate identities, exact rational sampling (not a certificate).
Controls:
  P1  the builder reproduces the landed gC5 (RelcSelectC5.lean tables) exactly, and c5_sep's entries (1, -1);
  P2  the same builder at d = 3 with nflip gives a gate satisfying relC as well (the complex CNOT case);
  P3  d = 5 with (p, q) = (3, 1): the builder with K pairs (2,3),(4,5) satisfies relT for diag(1,1,1,-1,-1);
  C1  relT checker: C7b with K pairs (2,7),(3,4),(5,6) (the unbalanced family's K) fails relT for N7b;
  C2  positivity evaluator: J replaced by 2J keeps frame/relT but gives an exact negative value;
  C3  gJ5_value = -1/10 reproduced (PARITY-NOT-1);
  C4  balance checker: nC5 is unbalanced (2,4), n5 balanced (3,3).
"""
import sys, random
from sympy import Matrix, Rational as R, eye, zeros, diag
from relt_common import (hom, homMap, apply, prod, isNot, frame, relT, relC, eig_dims, pairVal, actT_mat,
                         actC_mat, sgate, sharpVec)
from relt_lsig import Lsig_exact
from bal_gates import (cstruct, signs_N, jk_gate_general, landed_gC5, landed_nC5, entW, certificate_identities)

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


def rational_sphere_point(d, rng):
    t = [R(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(d - 1)]
    s2 = sum(v ** 2 for v in t)
    return Matrix([2 * v / (1 + s2) for v in t] + [(s2 - 1) / (1 + s2)])


def sampled_min(G, d, rng, trials):
    worst = None
    for _ in range(trials):
        x = rational_sphere_point(d, rng)
        y = rational_sphere_point(d, rng)
        e = hom(rational_sphere_point(d, rng))
        f = hom(rational_sphere_point(d, rng))
        v = pairVal(e, f, apply(G, prod(x, y)))
        worst = v if worst is None or v < worst else worst
    return worst


def normal_form(g, N):
    """corner maps, tangent closure, blocks in Lsig(sigma) commuting with homMap N, invertible tangent block"""
    G, z, d = g["G"], g["z"], g["d"]
    n = d + 1
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
                return dict(ok=False, why="corner slice not product")
            cols.append(v)
        Ms.append(Matrix.hstack(*cols))
    M0, M1 = Ms
    S = M1 * M0.inv()
    sigma = S[1:, 1:]
    orth = S[0, 0] == 1 and S[0, 1:].is_zero_matrix and S[1:, 0].is_zero_matrix and \
        (sigma.T * sigma - eye(d)).is_zero_matrix
    Nh = homMap(N)
    Tidx = list(range(1, d))
    blocks = {}
    inT = True
    M0i = M0.inv()
    for j in Tidx:
        for c in range(n):
            Y = zeros(n, 1)
            Y[c] = 1
            X = zeros(n, 1)
            X[j] = 1
            out = apply(G, X * (M0i * Y).T)
            if not (out[0, :].is_zero_matrix and out[d, :].is_zero_matrix):
                inT = False
            for k in Tidx:
                blocks.setdefault((k, j), zeros(n, n))
                blocks[(k, j)][:, c] = out[k, :].T

    def in_Lsig(L):
        a = L[1:, 0]
        A = L[1:, 1:]
        return (L[0, 0] == 0 and (L[0, 1:] - a.T).is_zero_matrix and (A + A.T).is_zero_matrix
                and (sigma * a - a).is_zero_matrix and (sigma.T * A - A * sigma).is_zero_matrix)
    allL = all(in_Lsig(L) for L in blocks.values())
    comm = all((L * Nh - Nh * L).is_zero_matrix for L in blocks.values())
    Kt = Matrix.vstack(*[Matrix.hstack(*[blocks[(k, j)] for j in Tidx]) for k in Tidx])
    inv = Kt.det() != 0
    return dict(ok=orth and inT and allL and comm and inv, M0=M0, M1=M1, sigma=sigma, orth=orth, inT=inT,
                allL=allL, comm=comm, inv=inv)


rng = random.Random(20261008)

# ------------------------------------------------------------------ P1: the builder reproduces the landed gC5
print("== P1 landed gC5 (RelcSelectC5.lean) reproduced by the builder")
J5 = cstruct(6, [(1, 2), (3, 4)])
K5 = cstruct(6, [(2, 5), (3, 4)])
g5 = jk_gate_general(5, 1, J5, K5)
GC5 = landed_gC5()
check("P1 builder(d=5, u=1, J=(1,2)(3,4), K=(2,5)(3,4)) == landed gC5 as 36x36 matrices", (g5["G"] - GC5).is_zero_matrix)
nC5 = landed_nC5()
z5 = Matrix([0, 0, 0, 0, 1])
lhs = apply(actC_mat(nC5) * GC5 * actC_mat(nC5), entW(6, 3, 3))[4, 4]
rhs = apply(actT_mat(nC5) * GC5, entW(6, 3, 3))[4, 4]
check(f"P1 c5_sep entries reproduced: lhs = {lhs} (kernel 1), rhs = {rhs} (kernel -1)", lhs == 1 and rhs == -1)
check("P1 gC5: frame, relT(nC5), G^2 = I, relC fails",
      frame(GC5, z5) and relT(GC5, nC5) and (GC5 * GC5 - eye(36)).is_zero_matrix and not relC(GC5, nC5))
check("P1 gC5 sigma == nC5 (the -z corner identity holds: M1 M0^-1 = homMap nC5)",
      (normal_form(g5, nC5)["sigma"] - nC5).is_zero_matrix)

# ------------------------------------------------------------------ B1: the balanced d = 7 gate
print("== B1 the balanced NOT N7b at d = 7 and the gate C7b")
d = 7
N7b = signs_N(7, [0, 1, 2])  # +1 on coordinates 0,1,2 (homogeneous 1,2,3), -1 on 3..6 (homogeneous 4..7, z = 7)
z7 = Matrix([0, 0, 0, 0, 0, 0, 1])
J7 = cstruct(8, [(1, 2), (3, 4), (5, 6)])
K7 = cstruct(8, [(2, 3), (4, 5), (6, 7)])
g7 = jk_gate_general(7, 1, J7, K7)
G7 = g7["G"]
check("B1 IsNot (eball 7) z7 N7b", all(isNot(z7, N7b).values()))
check(f"B1 homogenized eigenspaces of N7b: {eig_dims(N7b)} (balanced)", eig_dims(N7b) == (4, 4))
check("B1 frame", frame(G7, z7))
check("B1 relT for N7b", relT(G7, N7b))
check("B1 G^2 = I (so G is invertible and G^-1 = G)", (G7 * G7 - eye(64)).is_zero_matrix)
TC = actC_mat(N7b)
TT = actT_mat(N7b)
D = TC * G7 * TC - TT * G7
check("B1 relC for N7b FAILS", not D.is_zero_matrix)
# an explicit failing entry, on a matrix unit
found = None
for p in range(8):
    for q in range(8):
        E = entW(8, p, q)
        L1 = apply(TC * G7 * TC, E)
        L2 = apply(TT * G7, E)
        diff = L1 - L2
        if not diff.is_zero_matrix:
            for a in range(8):
                for b in range(8):
                    if diff[a, b] != 0:
                        found = (p, q, a, b, L1[a, b], L2[a, b])
                        break
                if found:
                    break
        if found:
            break
    if found:
        break
print("     relC witness: entW %d %d, entry (%d,%d): actC side %s, actT side %s" % found)
check("B1 relC witness entry found with distinct sides", found is not None and found[4] != found[5])
nf = normal_form(g7, N7b)
check("B1 normal form: M0 = I, M1 = homMap sigma, sigma orthogonal with sigma z = -z",
      (nf["M0"] - eye(8)).is_zero_matrix and (nf["M1"] - g7["S"]).is_zero_matrix and nf["orth"]
      and (nf["sigma"] * z7 + z7).is_zero_matrix)
check("B1 sigma != N7b: the -z corner identity G(hom(-z) (x) Y) = hom(-z) (x) homMap(N7b) M0 Y FAILS",
      not (nf["sigma"] - N7b).is_zero_matrix)
check("B1 tangent outputs in T, blocks in Lsig(sigma) and commuting with homMap N7b, tangent block invertible",
      nf["inT"] and nf["allL"] and nf["comm"] and nf["inv"])
ids = certificate_identities(g7)
for k, v in ids.items():
    check("B1 certificate " + k, v)
w = sampled_min(G7, 7, rng, 120)
check(f"B1 exact rational sampling (sanity, not a certificate): min value {w} >= 0", w >= 0)

# ------------------------------------------------------------------ P2: d = 3 with nflip (relC holds there)
print("== P2 d = 3, nflip: the builder gives a native gate")
nflip = diag(1, -1, -1)
z3 = Matrix([0, 0, 1])
g3 = jk_gate_general(3, 1, cstruct(4, [(1, 2)]), cstruct(4, [(2, 3)]))
check("P2 frame, relT(nflip), relC(nflip), G^2 = I", frame(g3["G"], z3) and relT(g3["G"], nflip)
      and relC(g3["G"], nflip) and (g3["G"] * g3["G"] - eye(16)).is_zero_matrix)
check("P2 certificate identities", all(certificate_identities(g3).values()))

# ------------------------------------------------------------------ P3: d = 5, (p, q) = (3, 1)
print("== P3 d = 5 with dim Fix N = 3")
N531 = signs_N(5, [0, 1, 2])
g531 = jk_gate_general(5, 1, cstruct(6, [(1, 2), (3, 4)]), cstruct(6, [(2, 3), (4, 5)]))
check(f"P3 IsNot, eigenspaces {eig_dims(N531)}", all(isNot(z5, N531).values()) and eig_dims(N531) == (4, 2))
check("P3 frame, relT, G^2 = I, relC fails", frame(g531["G"], z5) and relT(g531["G"], N531)
      and (g531["G"] * g531["G"] - eye(36)).is_zero_matrix and not relC(g531["G"], N531))
check("P3 certificate identities", all(certificate_identities(g531).values()))

# ------------------------------------------------------------------ countercontrols
print("== countercontrols")
gbad = jk_gate_general(7, 1, J7, cstruct(8, [(2, 7), (3, 4), (5, 6)]))
check("C1 relT checker: K not commuting with N7b -> relT(N7b) fails (and relT(sigma) holds)",
      not relT(gbad["G"], N7b) and relT(gbad["G"], gbad["sigma"]))
g2J = jk_gate_general(7, 1, 2 * J7, K7)
check("C2a 2J variant keeps frame and relT(N7b)", frame(g2J["G"], z7) and relT(g2J["G"], N7b))
# Random rational sampling is NOT discriminating here (recorded on the first run: 400 samples found no negative
# value for the 2J variant).  The adversarial witness of the written proof is used instead: control x = t = e_1
# (x_z = 0), control effect e = (1, -J t), target y = y- = e_2 (coordinate 1), target effect f = (1, K y-).
# Then A + B = (P + Q)/2 = 1 and C = -c * beta with beta = 1, where c is the scale of J.
xw = Matrix([1, 0, 0, 0, 0, 0, 0])
yw = Matrix([0, 1, 0, 0, 0, 0, 0])
ew = Matrix([1, 0, -1, 0, 0, 0, 0, 0])
fw = Matrix([1, 0, 0, 1, 0, 0, 0, 0])
from relt_common import lor
check("C2 witness effects lie in the cone (e, f null) and x, y are unit", lor(ew) and lor(fw)
      and (xw.T * xw)[0, 0] == 1 and (yw.T * yw)[0, 0] == 1)
v_c7 = pairVal(ew, fw, apply(G7, prod(xw, yw)))
v_2J = pairVal(ew, fw, apply(g2J["G"], prod(xw, yw)))
check(f"C2b C7b is tight at the witness (value {v_c7} == 0); the 2J variant is negative there (value {v_2J} == -1)",
      v_c7 == 0 and v_2J == -1)
cnt = 0
for trial in range(200):
    x = rational_sphere_point(7, rng)
    y = rational_sphere_point(7, rng)
    e = hom(rational_sphere_point(7, rng))
    f = hom(rational_sphere_point(7, rng))
    if pairVal(e, f, apply(g2J["G"], prod(x, y))) < 0:
        cnt += 1
print(f"     info: random rational sampling found {cnt}/200 negative values for the 2J variant "
      f"(sampling is a sanity check only, not a positivity test)")
odd5 = [False, False, False, True, True, True]
perm5 = [5, 3, 4, 1, 2, 0]
gJ5 = sgate(odd5, perm5, 6)
x5 = Matrix([1, 0, 0, 0, 0])
w5 = Matrix([0, 0, R(-3, 5), 0, R(-4, 5)])
check("C3 gJ5_value = -1/10 reproduced", pairVal(sharpVec(w5), sharpVec(z5), apply(gJ5, prod(x5, z5))) == R(-1, 10))
n5 = diag(1, 1, -1, -1, -1)
check(f"C4 eigenspaces: nC5 {eig_dims(nC5)} unbalanced, n5 {eig_dims(n5)} balanced",
      eig_dims(nC5) == (2, 4) and eig_dims(n5) == (3, 3))

npass = sum(1 for _, c in checks if c)
print(f"bal_c7: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
