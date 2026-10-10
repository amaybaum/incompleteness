"""Thread P (wave 2) -- exact checks for the V4' licence analysis.

Exact arithmetic only (sympy Rational / exact symbolic). Run with PYTHONDONTWRITEBYTECODE=1.
Conventions follow OIBridge at L = f7f5c3b0:
  ballEffect b (v) = 1/2 + (b . v)/2                 (KInfFoundations.lean:1026)
  rot3 t = rotation about axis 2 (z)                  (KInfFoundations.lean:351, 411)
  cyc3 v = (v2, v0, v1), cyc3.symm v = (v1, v2, v0)   (KInfFoundations.lean:416-432)
  seedTransport e g = e o g^{-1}                      (OrbitGeneration.lean:49)
An affine functional on R^3 is stored as (c, a) meaning v |-> c + a . v.
Precomposition with a linear map M: (c, a) o M = (c, M^T a).
"""
import itertools
import sympy as sp
from sympy import Rational as Q, Matrix, sqrt, symbols, simplify, eye

checks = []


def check(name, cond):
    ok = bool(cond)
    checks.append((name, ok))
    print(("PASS " if ok else "FAIL ") + name)


def be(b):
    """ballEffect b as (c, a)."""
    return (Q(1, 2), Matrix([Q(1, 2) * x for x in b]))


def ev(e, v):
    c, a = e
    return sp.nsimplify(c + (a.T * Matrix(v))[0]) if False else sp.simplify(c + (a.T * Matrix(v))[0])


def pre(e, M):
    """e o M for a linear M (as a matrix acting on column vectors)."""
    c, a = e
    return (c, sp.simplify(M.T * a))


def eq(e, f):
    return sp.simplify(e[0] - f[0]) == 0 and all(sp.simplify(x) == 0 for x in (e[1] - f[1]))


def rotz(c, s):
    return Matrix([[c, -s, 0], [s, c, 0], [0, 0, 1]])


CYC = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])      # cyc3: (x,y,z) -> (z,x,y)
CYCinv = CYC.T
e0, e1, e2 = [1, 0, 0], [0, 1, 0], [0, 0, 1]
r = be(e2)                                           # the seed (1 + z)/2

# ---------------------------------------------------------------- E1 cyc3 facts
print("== E1: the drive generator J = cyc3")
check("E1.1 cyc3 * cyc3^T = I (orthogonal, J^{-1} = J^T)", CYC * CYC.T == eye(3))
check("E1.2 cyc3^3 = I (finite order: J^{-1} = J^2)", CYC ** 3 == eye(3))
check("E1.3 cyc3 matches cyc3_apply: cyc3 (a,b,c) = (c,a,b)",
      CYC * Matrix([1, 2, 3]) == Matrix([3, 1, 2]))
check("E1.4 r o J^{-1} = ballEffect e0", eq(pre(r, CYCinv), be(e0)))
check("E1.5 r o J^{-2} = ballEffect e1", eq(pre(pre(r, CYCinv), CYCinv), be(e1)))
check("E1.6 r o J o J = r o J^{-1} (SEQ with J alone reaches J^{-1}, given J^3 = 1)",
      eq(pre(pre(r, CYC), CYC), pre(r, CYCinv)))
c_, s_ = symbols("c s", real=True)
R = rotz(c_, s_)
# generic rotation about z (c^2 + s^2 = 1): fixes the z-pole effects
fz = pre(r, R.T)
check("E1.7 r o rot3(t)^{-1} = r for every t (symbolic c, s)", eq(fz, r))
check("E1.8 ballEffect(-e2) o rot3(t)^{-1} = ballEffect(-e2)", eq(pre(be([0, 0, -1]), R.T), be([0, 0, -1])))

# ---------------------------------------------------------------- E2 CM1
print("== E2: CM1 -- drive words available as transformations, SEQ fails, V4' fails")
avail0 = [be(e2), be([0, 0, -1])]
# P1 for r on ball3: r(e2) = 1, r(-e2) = 0 ; effect on ball since |z| <= 1 (written)
check("E2.1 SharpSeed values: r(e2) = 1, r(-e2) = 0", ev(r, e2) == 1 and ev(r, [0, 0, -1]) == 0)
check("E2.2 avail0 is a perfectly distinguishing pair: sum = unit (symbolic)",
      sp.simplify(avail0[0][0] + avail0[1][0] - 1) == 0 and avail0[0][1] + avail0[1][1] == Matrix([0, 0, 0]))
tgt = pre(r, CYCinv)  # seedTransport r cyc3, cyc3 in driveWords3
check("E2.3 seedTransport r cyc3 = ballEffect e0 takes value 1 at e0 (a boundary state)", ev(tgt, e0) == 1)
check("E2.4 every member of avail0 takes value 1/2 at e0, so seedTransport r cyc3 not in avail0",
      all(ev(e, e0) == Q(1, 2) for e in avail0))
check("E2.5 hence SEQ fails on avail0 at (r, J^{-1}) and V4'(driveWords3, r, avail0) fails",
      not any(eq(tgt, e) for e in avail0))

# ---------------------------------------------------------------- E3 CM2
print("== E3: CM2 -- SEQ holds for trans = range rot3, J not an available transformation")
unit = (Q(1), Matrix([0, 0, 0]))
zero = (Q(0), Matrix([0, 0, 0]))
effs = avail0 + [unit, zero]
closed = all(any(eq(pre(e, R), f) for f in effs) for e in effs)
check("E3.1 {be e2, be(-e2), 1, 0} is closed under precomposition by every rot3 t (symbolic)", closed)
check("E3.2 cyc3 is not a rotation about z (cyc3 e2 = e1 != e2), so cyc3 notin range rot3",
      CYC * Matrix(e2) != Matrix(e2))
check("E3.3 V4'(driveWords3) still fails: seedTransport r cyc3 notin effs",
      not any(eq(tgt, e) for e in effs))

# ---------------------------------------------------------------- E4 CM3
print("== E4: CM3 -- V4' holds, generator closure of the whole family fails")
unsharp = (Q(3, 4), Matrix([0, 0, Q(1, 4)]))          # unsharpSeed, OrbitGeneration.lean:626
u_t = pre(unsharp, CYCinv)                            # 3/4 + v0/4
check("E4.1 unsharpSeed o J^{-1} = 3/4 + v0/4", eq(u_t, (Q(3, 4), Matrix([Q(1, 4), 0, 0]))))
# not directional: a directional effect has the constant 1/2 (OrbitGeneration ball3_sharp_eq: c = 1/2)
check("E4.2 3/4 + v0/4 has constant term 3/4 != 1/2, so it is not ballEffect b for any b", u_t[0] != Q(1, 2))
check("E4.3 3/4 + v0/4 != unsharpSeed (values at e0: 1 vs 3/4)",
      ev(u_t, e0) == 1 and ev(unsharp, e0) == Q(3, 4))
# V4' holds for avail = directionalFamily U {unsharpSeed} by seedOrbit_ball3Drive (kernel) -- recorded, not computed

# ---------------------------------------------------------------- E5 consistency of SEQ
print("== E5: SEQ needs transformations that map states to states")
D2 = 2 * eye(3)
bad = pre(r, D2)
check("E5.1 r o (2 id) takes 3/2 at e2: not an effect on ball3", ev(bad, e2) == Q(3, 2))

# ---------------------------------------------------------------- E6 finite instance of the closure theorem
print("== E6: closure induction, finite instance (S = {rot3(pi/2), cyc3}, forward precomposition only)")
RZ = rotz(0, 1)


def key(e):
    return (e[0], tuple(e[1]))


# forward closure of {r} under e -> e o s for s in S (no inverses supplied)
A = {key(r): r}
frontier = [r]
while frontier:
    nxt = []
    for e in frontier:
        for M in (RZ, CYC):
            f = pre(e, M)
            if key(f) not in A:
                A[key(f)] = f
                nxt.append(f)
    frontier = nxt
# the group generated by S: close {I} under left multiplication by S and S^{-1}
G = {tuple(eye(3)): eye(3)}
fr = [eye(3)]
while fr:
    nx = []
    for g in fr:
        for M in (RZ, RZ.T, CYC, CYC.T):
            h = M * g
            if tuple(h) not in G:
                G[tuple(h)] = h
                nx.append(h)
    fr = nx
orbit = {key(pre(r, g.T)): None for g in G.values()}
check("E6.1 |<S>| = 24 (rotation group of the cube)", len(G) == 24)
check("E6.2 forward SEQ-closure of {r} = seed orbit {r o g^{-1} : g in <S>} (6 effects be(+-e_i))",
      set(A.keys()) == set(orbit.keys()) and len(A) == 6)

# ---------------------------------------------------------------- E7 inverse of an infinite-order J
print("== E7: an infinite-order J whose inverse is reached through the flow")
Jx = Matrix([[1, 0, 0], [0, Q(3, 5), -Q(4, 5)], [0, Q(4, 5), Q(3, 5)]])  # rotation about x, cos = 3/5
check("E7.1 Jx orthogonal", Jx * Jx.T == eye(3))
P = Jx
fin = False
for n in range(1, 61):
    if P == eye(3):
        fin = True
        break
    P = P * Jx
check("E7.2 Jx^n != I for n = 1..60 (infinite order: cos = 3/5 is not a root-of-unity cosine; Niven, written)",
      not fin)
HT = rotz(-1, 0)  # rot3(pi), the NOT of ball3Drive
check("E7.3 Jx^{-1} = rot3(pi) Jx rot3(pi) (inverse is a forward word through the flow's half-turn)",
      HT * Jx * HT == Jx.T)

# ---------------------------------------------------------------- E8 countable generators: no exact transitivity
print("== E8: fixed-angle generators S = {rot3(arccos 3/5), cyc3}: words are rational, orbit misses the sphere")
Rq = rotz(Q(3, 5), Q(4, 5))
check("E8.1 the generators and their inverses are rational matrices",
      all(x.is_Rational for M in (Rq, Rq.T, CYC, CYC.T) for x in M))
# closure argument (written): rational matrices are closed under products, so every word is rational,
# and g e2 is a rational vector. Exact sample: all words of length <= 6 in S u S^{-1}.
gens = [Rq, Rq.T, CYC, CYC.T]
pts = set()
cnt = 0
for L in range(0, 7):
    for w in itertools.product(range(4), repeat=L):
        M = eye(3)
        for i in w:
            M = M * gens[i]
        cnt += 1
        pts.add(tuple(M * Matrix(e2)))
check("E8.2 all %d words of length <= 6 send e2 to rational points" % cnt,
      all(all(sp.Rational(x) == x and x.is_Rational for x in p) for p in pts))
b_irr = Matrix([sqrt(2) / 2, sqrt(2) / 2, 0])
check("E8.3 b = (sqrt2/2, sqrt2/2, 0) is on the unit sphere and is not rational",
      sp.simplify((b_irr.T * b_irr)[0] - 1) == 0 and not b_irr[0].is_Rational)
check("E8.4 so ballEffect b notin seedOrbit(words S) r: be(b) has an irrational coefficient, every orbit member "
      "r o g^{-1} = be(g e2) has rational ones", not (be(list(b_irr))[1][0]).is_Rational)
# density of <S> in SO(3) is a written/citation-level fact (rot by arccos 3/5 has infinite order; E7.2 analogue)
P = Rq
fin = False
for n in range(1, 61):
    if P == eye(3):
        fin = True
        break
    P = P * Rq
check("E8.5 rot3(arccos 3/5)^n != I for n = 1..60", not fin)

# ---------------------------------------------------------------- E9 limit step (b): uniform bound
print("== E9: limit step -- |be(b)(v) - be(b')(v)| <= |b - b'|/2 on the ball (Cauchy-Schwarz), exact instance")
bq = Matrix([Q(119, 169), Q(120, 169), 0])  # rational point near (sqrt2/2, sqrt2/2, 0)
check("E9.1 (119/169, 120/169, 0) is on the unit sphere", (bq.T * bq)[0] == 1)
d2 = sp.simplify(((bq - b_irr).T * (bq - b_irr))[0])
check("E9.2 |b' - b|^2 = 2 - 239 sqrt2/169 < 1/1000 (exact comparison)", sp.simplify(d2 - (2 - 239 * sqrt(2) / 169)) == 0
      and (Q(1, 1000) - d2).is_positive)

# ---------------------------------------------------------------- E10 remaining hypothesis audits
print("== E10: SEED-AVAIL and TRANS(flow) audits")
consts = [unit, zero]
check("E10.1 {1, 0} is closed under precomposition by every linear map (SEQ holds for any trans)",
      all(eq(pre(e, M), e) for e in consts for M in (R, CYC, CYCinv)))
check("E10.2 r notin {1, 0}: V4' fails at g = 1 (SEED-AVAIL is load-bearing)",
      not any(eq(r, e) for e in consts))
effJ = [be(e0), be(e1), be(e2)]
check("E10.3 {be e0, be e1, be e2} is closed under precomposition by cyc3 and cyc3^{-1}",
      all(any(eq(pre(e, M), f) for f in effJ) for e in effJ for M in (CYC, CYCinv)))
gw = Rq * CYC                                       # a word of driveWords3 (rot3(arccos 3/5) * cyc3)
tw = pre(r, gw.T)                                   # seedTransport r gw = be(gw e2)
check("E10.4 seedTransport r (rot3(arccos 3/5) * cyc3) = be(3/5, 4/5, 0)  [cyc3 e2 = e0; run 1 expected be(-4/5,3/5,0), wrong]",
      eq(tw, be([Q(3, 5), Q(4, 5), 0])))
check("E10.5 be(3/5, 4/5, 0) notin {be e0, be e1, be e2}: without TRANS(flow), V4' fails",
      not any(eq(tw, f) for f in effJ))

print()
nf = sum(1 for _, ok in checks if not ok)
print("OK -- %d checks, %d failures" % (len(checks), nf) if nf == 0 else "FAILED -- %d of %d" % (nf, len(checks)))
