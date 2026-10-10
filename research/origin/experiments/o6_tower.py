"""o6_tower.py -- research/origin, round 2, node O6: the stage-crossing generator (HO-2c) against O3-T5's three
requirements (finite rank of an infinite-substratum completion; an infinite-order stage-crossing datum; invasive
repeatable observation).

QUESTION. What must a stage-crossing datum of a protocol tower do to the frame readout to generate a one-parameter
subgroup in the completion, and can the three requirements hold together with a repeatable readout, or are they
mutually exclusive on passive towers? The written theorem (NOTES-O6 T1, T2; design module OriginPassive, Sections C
and D) says: on a passive repeatable tower with finite rank every extreme point of the chart body is
outcome-deterministic, so there are at most 2^d of them and every reversible datum has finite order; an
infinite-order datum on a finite-rank body forces all but finitely many pure states to be outcome-random, hence
observation invasive there. This script builds the exact instances.

TOWERS (one substratum, the circle S^1 with its rotation-invariant measure; readout along a direction u: outcome +
iff cos(lambda - u) > 0, a half-circle):
  passive    the readout conditions the hidden angle (OI-STAGE's towers, A5);
  re-prepare the readout records the outcome and re-samples lambda from rho_{+-u}, a density supported in the
             outcome's half-circle (a KB-D-type law: read, then re-randomize the hidden variable within the cell);
             cosine law rho_u(lambda) = cos(lambda - u)/2 (the Kochen-Specker density on the circle) and, as a
             control, the uniform law rho_u = 1/pi on the half-circle.
  Datum g: rotation of the hidden angle by a, cos a = 3/5, sin a = 4/5; stage n = directions {k a : |k| <= n}.
CHECKS.
  P1  passive tower on the dyadic grid {j pi / 2^m}: every elementary arc is a reachable preparation (the
      intersection of two grid half-circles), and the table (elementary arcs x grid half-circles) has rank 2^m + 1,
      m = 1..6: the rank grows with the stage.
  K1  cosine law: P(+u | rho_psi) = (1 + cos(u - psi))/2 exactly (symbolic integrals on both halves of [0, 2 pi]);
      rho integrates to 1 and is nonnegative on its half-circle.
  K2  cosine law, stages n = 1..10 on Pythagorean directions: the table of single readouts and of two-step readouts
      (+u then +u') on the preparations rho_psi has rank 3 at every stage (finite rank, chart dimension 2: a disk).
  K3  the datum has infinite order: e^{ia} = (3 + 4i)/5 has minimal polynomial x^2 - (6/5) x + 1, not monic over Z,
      so it is not a root of unity; R(a)^k != 1 for k = 1..200 (exact).
  K4  the datum crosses stages: it maps stage n into stage n + 1 and the direction (n + 1) a is not in stage n
      (n = 1..20; all directions distinct).
  K5  the readout is repeatable (P(+u | rho_u) = 1) and invasive (observe-and-forget along u = 0 sends the Bloch
      vector of rho_a, (3/5, 4/5), to (3/5, 0)); the pure states rho_{ka}, k = 1..200, are outcome-random for the
      frame readout u = 0 (probability strictly between 0 and 1).
  K6  witness: with the closure member R(pi/2) (completion-valued) the owner's numbers are exact, (1, 1/2); with the
      stage data g^k, k = 1..200, the dephased probability is (1 + cos^2 ka)/2 > 1/2: the balanced mixer is not a
      stage operation.
  K7  the ball (sphere S^2, cosine law rho_psi(lambda) = (psi.lambda)^+ / pi): P(+u | rho_psi) = (1 + psi.u)/2 via the
      projection to the equatorial disk (symbolic: the area integral equals pi/2 + (pi/2) cos(beta)); the table on
      rational unit vectors has rank 4; OFF-Gamma': for g = R_z(a), J = R_x(pi/2), J g^m J^-1 and g^m do not commute,
      m = 1..60.
  K8  uniform re-preparation law on the dyadic grid: response 1 - |beta|/pi; the table rank grows with m (1..6).
  K9  responses f(beta) = c0 + c1 cos(beta) (minimal rank) with f(0) = 1 and f(beta) + f(beta + pi) = 1: the unique
      solution is c0 = c1 = 1/2; the degree-3 response 1/2 + (9/16) cos(beta) - (1/16) cos(3 beta) is repeatable, its
      re-preparation density -f'(t + pi/2) = (9/16) cos t + (3/16) cos 3t equals (3/4) cos^3 t (exact identity), so it
      is nonnegative on the half-circle, and its table on Pythagorean directions has rank 5.
DECISION RULE (fixed before the first run; the verdict line is generated from the measured booleans):
  PASSIVE_GROWS := P1.   INVASIVE_INSTANCE := K1 and K2 and K3 and K4 and K5 and K6.   BALL_OFF := K7.
  LAW_SELECTION := K8 and K9.
  VERDICT VOID if any countercontrol is True.
  VERDICT EXCLUSIVE-ON-PASSIVE-JOINT-ON-INVASIVE iff PASSIVE_GROWS and INVASIVE_INSTANCE and BALL_OFF and
    LAW_SELECTION; otherwise VERDICT MIXED with the failing items listed.
COUNTERCONTROLS (must be False):
  CC1 the passive dyadic table at m = 3 has rank 3;
  CC2 the rotation by pi/2 passes the infinite-order certificate;
  CC3 J' = R_z(pi/2) passes OFF-Gamma' at m = 1;
  CC4 the uniform-law table at m = 3 has rank 3;
  CC5 the re-preparing readout along u = 0 is passive at rho_a.

Run: python3 -I -B o6_tower.py > o6_tower.out 2> o6_tower.err; echo "exit $?" >> o6_tower.err
"""

from fractions import Fraction as F
import sympy as sp

RES = {}
CC = {}


def rank(rows):
    M = [[F(x) for x in r] for r in rows]
    if not M:
        return 0
    rk = 0
    ncol = len(M[0])
    for col in range(ncol):
        piv = None
        for r in range(rk, len(M)):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col] / M[rk][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rk])]
        rk += 1
    return rk


print("== o6_tower ==")
print()
print("-- P1: passive tower on the dyadic grid")
p1_ranks = []
p1_reach = True
for m in range(1, 7):
    N2 = 2 ** (m + 1)          # number of grid points = number of elementary arcs
    half = 2 ** m              # a half-circle covers 2^m elementary arcs

    def H(i):
        # half-circle along u_i = i pi / 2^m: (u_i - pi/2, u_i + pi/2) = arcs i - 2^(m-1) .. i + 2^(m-1) - 1
        return {(i - half // 2 + t) % N2 for t in range(half)}
    for j in range(N2):
        # arc j = (g_j, g_{j+1}) = H(g_j + pi/2) cap H(g_{j+1} - pi/2)
        inter = H((j + half // 2) % N2) & H((j + 1 - half // 2) % N2)
        p1_reach = p1_reach and inter == {j}
    T = [[1 if j in H(i) else 0 for i in range(N2)] for j in range(N2)]
    p1_ranks.append(rank(T))
RES["P1"] = p1_reach and p1_ranks == [2 ** m + 1 for m in range(1, 7)]
CC["CC1"] = p1_ranks[2] == 3
print(f"P1  elementary arcs reachable as intersections of two grid half-circles: {p1_reach}; table ranks m = 1..6: "
      f"{p1_ranks} (2^m + 1: {[2 ** m + 1 for m in range(1, 7)]})  -> {RES['P1']}")

print()
print("-- K: the re-preparing (cosine-law) tower on the circle")
b, s, t = sp.symbols("beta s t", real=True)
# psi = 0: rho_0 supported on (-pi/2, pi/2), density cos(s)/2. Readout along u = beta.
# beta in [0, pi]: overlap (beta - pi/2, pi/2);  beta in [pi, 2 pi]: overlap (-pi/2, beta - 3 pi/2)
I1 = sp.simplify(sp.integrate(sp.cos(s) / 2, (s, b - sp.pi / 2, sp.pi / 2)) - (1 + sp.cos(b)) / 2)
I2 = sp.simplify(sp.integrate(sp.cos(s) / 2, (s, -sp.pi / 2, b - 3 * sp.pi / 2)) - (1 + sp.cos(b)) / 2)
norm = sp.integrate(sp.cos(s) / 2, (s, -sp.pi / 2, sp.pi / 2))
RES["K1"] = I1 == 0 and I2 == 0 and norm == 1
print(f"K1  P(+u | rho_psi) - (1 + cos beta)/2 on [0, pi]: {I1}; on [pi, 2 pi]: {I2}; normalization {norm}; density "
      f"cos(s)/2 >= 0 on (-pi/2, pi/2)  -> {RES['K1']}")

# Pythagorean directions: (cos ka, sin ka) exactly
CA, SA = F(3, 5), F(4, 5)


def cs(k):
    c, s_ = F(1), F(0)
    if k >= 0:
        for _ in range(k):
            c, s_ = c * CA - s_ * SA, s_ * CA + c * SA
    else:
        for _ in range(-k):
            c, s_ = c * CA + s_ * SA, s_ * CA - c * SA
    return c, s_


def resp_cos(u, psi):
    (cu, su), (cp, sp_) = u, psi
    return (1 + cu * cp + su * sp_) / 2


k2_ranks = []
for n in range(1, 11):
    dirs = [cs(k) for k in range(-n, n + 1)]
    rows = []
    for psi in dirs:
        row = [resp_cos(u, psi) for u in dirs]
        row += [resp_cos(u, psi) * resp_cos(u2, u) for u in dirs for u2 in dirs]
        rows.append(row)
    k2_ranks.append(rank(rows))
RES["K2"] = k2_ranks == [3] * 10
print(f"K2  table rank (single and two-step readouts) at stages n = 1..10: {k2_ranks}  -> {RES['K2']}")

x = sp.symbols("x")
lam = (sp.Rational(3) + 4 * sp.I) / 5
mp = sp.minimal_polynomial(lam, x)
mp_monic_int = all(c.is_integer for c in sp.Poly(mp, x).monic().all_coeffs())


def rot2(c, s_):
    return ((c, -s_), (s_, c))


def mul2(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


R = rot2(CA, SA)
P_ = R
k3_noid = True
for k in range(1, 201):
    if P_ == ((1, 0), (0, 1)):
        k3_noid = False
    P_ = mul2(P_, R)
mp_q = sp.minimal_polynomial(sp.I, x)
CC["CC2"] = not all(c.is_integer for c in sp.Poly(mp_q, x).monic().all_coeffs())
RES["K3"] = (not mp_monic_int) and k3_noid
print(f"K3  minimal polynomial of (3+4i)/5: {mp} (monic over Z: {mp_monic_int}); R(a)^k != 1 for k = 1..200: {k3_noid}"
      f"  -> {RES['K3']}")

k4 = True
for n in range(1, 21):
    stage = {cs(k) for k in range(-n, n + 1)}
    k4 = k4 and len(stage) == 2 * n + 1 and cs(n + 1) not in stage
RES["K4"] = k4
print(f"K4  stages n = 1..20: directions distinct, g(stage n) in stage n+1 and (n+1)a not in stage n: {k4}")

rep = all(resp_cos(cs(k), cs(k)) == 1 for k in range(-20, 21))
va = cs(1)
oaf = (va[0], F(0))          # observe-and-forget along e_0: v -> (v . e_0) e_0
invasive = oaf != va
random_frame = all(0 < resp_cos(cs(0), cs(k)) < 1 for k in range(1, 201))
CC["CC5"] = not invasive
RES["K5"] = rep and invasive and random_frame
print(f"K5  repeatable on stage directions: {rep}; observe-and-forget along u = 0 sends {va} to {oaf}: invasive "
      f"{invasive}; frame readout outcome-random on rho_(ka), k = 1..200: {random_frame}  -> {RES['K5']}")

# witness: Bloch vectors in the disk; mixers are rotations; frame dephasing v -> (v . e0) e0
def rotv(c, s_, v):
    return (c * v[0] - s_ * v[1], s_ * v[0] + c * v[1])


def pplus(v):
    return (1 + v[0]) / 2


e0 = (F(1), F(0))
coh = pplus(rotv(0, -1, rotv(0, 1, e0)))
mid = rotv(0, 1, e0)
deph = pplus(rotv(0, -1, (mid[0], F(0))))
k6_stage = True
for k in range(1, 201):
    c, s_ = cs(k)
    v = rotv(c, s_, e0)
    d = pplus(rotv(c, -s_, (v[0], F(0))))
    k6_stage = k6_stage and d == (1 + c * c) / 2 and d > F(1, 2)
RES["K6"] = coh == 1 and deph == F(1, 2) and k6_stage
print(f"K6  closure member R(pi/2): (P_coh, P_deph) = ({coh}, {deph}); stage data g^k, k = 1..200: P_deph = "
      f"(1 + cos^2 ka)/2 > 1/2 for all: {k6_stage}  -> {RES['K6']}")

print()
print("-- K7: the ball (sphere substratum, cosine law)")
c_ = sp.symbols("c", positive=True)
xx = sp.symbols("xx", real=True)
area = sp.pi / 2 + sp.integrate(2 * sp.sqrt(1 - xx ** 2 / c_ ** 2), (xx, -c_, 0))
k7_area = sp.simplify(area - (sp.pi / 2 + sp.pi * c_ / 2)) == 0
units = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1)), (F(3, 5), F(4, 5), F(0)),
         (F(0), F(3, 5), F(4, 5)), (F(2, 3), F(2, 3), F(1, 3)), (F(2, 7), F(3, 7), F(6, 7)),
         (F(1, 3), F(-2, 3), F(2, 3)), (F(-6, 7), F(2, 7), F(3, 7))]
units = units + [tuple(-a for a in v) for v in units]
tab = [[(1 + sum(p * q for p, q in zip(psi, u))) / 2 for u in units] for psi in units]
k7_rank = rank(tab)


def mul3(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)) for i in range(3))


def Rz(c, s_):
    return ((c, -s_, F(0)), (s_, c, F(0)), (F(0), F(0), F(1)))


J = ((F(1), F(0), F(0)), (F(0), F(0), F(-1)), (F(0), F(1), F(0)))      # R_x(pi/2)
Jinv = ((F(1), F(0), F(0)), (F(0), F(0), F(1)), (F(0), F(-1), F(0)))
off = True
G = Rz(CA, SA)
Gm = G
for m in range(1, 61):
    A = mul3(mul3(J, Gm), Jinv)
    off = off and mul3(A, Gm) != mul3(Gm, A)
    Gm = mul3(Gm, G)
Jp = Rz(F(0), F(1))
Jpinv = Rz(F(0), F(-1))
A1 = mul3(mul3(Jp, G), Jpinv)
CC["CC3"] = mul3(A1, G) != mul3(G, A1)
RES["K7"] = k7_area and k7_rank == 4 and off
print(f"K7  projection area - (pi/2 + (pi/2) cos beta) == 0: {k7_area} (so P(+u|rho_psi) = (1 + psi.u)/2); table rank on "
      f"{len(units)} rational unit vectors: {k7_rank}; OFF-Gamma' for m = 1..60: {off}  -> {RES['K7']}")

print()
print("-- K8, K9: what finite rank asks of the re-preparation law")
k8_ranks = []
for m in range(1, 7):
    N2 = 2 ** (m + 1)
    def tri(d):
        d = d % N2
        d = min(d, N2 - d)
        return 1 - F(d, 2 ** m)
    k8_ranks.append(rank([[tri(i - j) for i in range(N2)] for j in range(N2)]))
CC["CC4"] = k8_ranks[2] == 3
RES["K8"] = all(k8_ranks[i] < k8_ranks[i + 1] for i in range(len(k8_ranks) - 1))
print(f"K8  uniform law (response 1 - |beta|/pi) on the dyadic grid, ranks m = 1..6: {k8_ranks}  -> {RES['K8']}")

c0, c1 = sp.symbols("c0 c1")
fb = c0 + c1 * sp.cos(b)
sol = sp.solve([fb.subs(b, 0) - 1, sp.expand_trig(fb + fb.subs(b, b + sp.pi) - 1).subs(b, sp.Rational(1, 3))],
               [c0, c1], dict=True)
born = sol == [{c0: sp.Rational(1, 2), c1: sp.Rational(1, 2)}]
f3 = sp.Rational(1, 2) + sp.Rational(9, 16) * sp.cos(b) - sp.Rational(1, 16) * sp.cos(3 * b)
f3_rep = sp.simplify(f3.subs(b, 0) - 1) == 0 and sp.simplify(f3 + f3.subs(b, b + sp.pi) - 1) == 0
dens = sp.Rational(9, 16) * sp.cos(t) + sp.Rational(3, 16) * sp.cos(3 * t)
dens_ok = sp.simplify(dens - (-sp.diff(f3, b).subs(b, t + sp.pi / 2))) == 0
grid_ok = sp.simplify(sp.expand_trig(dens) - sp.Rational(3, 4) * sp.cos(t) ** 3) == 0


def resp3(u, psi):
    (cu, su), (cp, sp_) = u, psi
    cb = cu * cp + su * sp_            # cos(u - psi)
    c3 = 4 * cb ** 3 - 3 * cb          # cos 3(u - psi)
    return F(1, 2) + F(9, 16) * cb - F(1, 16) * c3


dirs = [cs(k) for k in range(-8, 9)]
k9_rank = rank([[resp3(u, psi) for u in dirs] for psi in dirs])
RES["K9"] = born and f3_rep and dens_ok and grid_ok and k9_rank == 5
print(f"K9  degree-1 responses with f(0) = 1, f(beta) + f(beta + pi) = 1: {sol} (Born response forced: {born}); "
      f"degree-3 response repeatable: {f3_rep}, density = -f'(t + pi/2): {dens_ok}, density = (3/4) cos^3 t >= 0: "
      f"{grid_ok}, table rank on 17 Pythagorean directions: {k9_rank}  -> {RES['K9']}")

print()
print("-- countercontrols (must be False)")
for k in sorted(CC):
    print(f"{k}  {'CC-OK (False as required)' if not CC[k] else 'CC-FAIL (True)'}")
print()
for k in sorted(RES):
    print(f"  {k}: {RES[k]}")
PG = RES["P1"]
INV = all(RES[k] for k in ["K1", "K2", "K3", "K4", "K5", "K6"])
BALL = RES["K7"]
LAW = RES["K8"] and RES["K9"]
if any(CC.values()):
    print("VERDICT VOID: a countercontrol returned True.")
elif PG and INV and BALL and LAW:
    print("VERDICT EXCLUSIVE-ON-PASSIVE-JOINT-ON-INVASIVE: on the circle substratum the passive tower's rank grows with")
    print("  the stage (P1), as the theorem requires of any passive tower carrying an infinite-order datum; the")
    print("  re-preparing tower has rank 3 at every stage, an infinite-order stage-crossing datum, a repeatable and")
    print("  invasive readout and the exact witness in the closure (K1-K6); the ball version adds OFF (K7); finite rank")
    print("  constrains the re-preparation law (K8) and minimal rank forces the response (1 + cos beta)/2 (K9).")
else:
    bad = [k for k, v in [("PASSIVE_GROWS", PG), ("INVASIVE_INSTANCE", INV), ("BALL_OFF", BALL),
                          ("LAW_SELECTION", LAW)] if not v]
    print(f"VERDICT MIXED: failing items {bad}")
