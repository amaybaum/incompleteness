# c7_ebf_wall.py -- research/countermodels node C7 (round 2): the EBF wall over the Bell-diagonal slice.
# DECISION RULE (fixed before the first run, 2026-10-10T22:47Z by date -u; predictions in NOTES-C7 S0):
#  Exact arithmetic only (sympy Rational / exact radicals; no floats). Conventions of c2_structure.py and of the
#  coordinator's indep_checkC.py: tables 4x4, pauliW(w) = (1/4) sum w_mn sigma_m (x) sigma_n, ipW the entrywise sum,
#  z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4, psi_s the (-1/8)-eigenvector of pauliW(z_s), order
#  SS = [(1,1),(1,-1),(-1,1),(-1,-1)] (index 1..4). Fix = Hermitian matrices diagonal in {psi_s}; pi = diagonal part in
#  that basis (= the Haar average over T^3_F); diag_psi(d) = sum d_s psi_s psi_s^dag. Pairing tr(XY) on Herm(4).
#  Circ = {d : S := sum d >= 0, S^2/4 >= |d - (S/4) 1|^2};  R = {d : d_s <= S/2};  O = cone{e_s + e_t}.
#  Each line is CHECK <id> PASS/FAIL (a stated exact identity or inequality) or COUNTERCONTROL <id> (a case where the
#  construction must NOT apply). The script prints VERDICT C7-EBF-WALL-EXACT iff every CHECK and COUNTERCONTROL passes;
#  otherwise NO VERDICT. The verdict text is generated from the measured values, never pre-written.
#  W0  conventions: psi_s real orthonormal, maximally entangled (reduced state I/2); pauliW(z_s) = (I - 2P_s)/8;
#      diag_psi(1 - 2e_s) = 8 pauliW(z_s) (so the R-cone of Fix is cone pauliW(Z_F)).
#  C1  Circ facts: e_s + e_t on the boundary of Circ; |e_s + e_t - 1/2|^2 = 1 (the [W] step Circ in O*);
#      y_d = (-2,12,6,4)/5 and y_d' = (S/2)1 - y_d = (12,-2,4,6)/5 both on the boundary, <y_d, y_d'> = 0, u(y_d') = -u(y_d)
#      (the [W] extremality step), y_d has a negative entry.
#  D2  K^Circ = (Q3 n pi^-1(Circ)) + Circ is not self-dual: v = psi_2 + psi_3/2, p = pi(P_v) = (0,1,1/4,0),
#      c0 = y_d - p in Circ (strict), y = P_v + diag_psi(c0): pi(y) = y_d, <psi_2|y|psi_3> = 1/2 != 0, y not PSD.
#      [W] (NOTES-C7 W1) y in (K^Circ)* \ K^Circ.
#  CC-R countercontrol for the slice R (K^R = K(Z_F), self-dual): for every extreme ray 1 - 2e_s of R and every p >= 0,
#      (1 - 2e_s) - p in R forces p = 0 (symbolic: the three facet inequalities sum to -sum(p)/2 >= 0).
#  D4  the sandwich C0 = A + Circ <= K' <= C0* = (Q3 + R) n pi^-1(Circ) has a gap with an incompatible pair:
#      v = 5psi_1 + 3psi_2 + 3psi_3 + psi_4 (profile (25,9,9,1), in Circ, not in O), u = (psi_1 - psi_2 - psi_3 + psi_4)/2
#      (u perp v, profile 1/4 each, in O), w = P_u + (1/2) diag_psi(-1,1,1,1): pi(w) in Circ, tr(w P_v) = -3; the
#      Ghat-orbit pairing bounds of the two EBF seeds (NOTES-C7 W3): <P_u, g z> = 1/2 for every coordinate permutation,
#      <z, g z> in {0, 4}.
#  D5  the simplex fibre: u5 = 3psi_1 + psi_2 + psi_3 + psi_4, y5 = u5 u5^dag + 8 diag_psi(-1,1,1,1): pi(y5) = (1,9,9,9),
#      x^dag y5 x = -12 at x = 3psi_1 - psi_2 - psi_3 - psi_4 (not PSD), the orbit-pairing bounds of NOTES-C7 W4 (-6
#      and 10 for <u5 u5^dag, g z>), lower bound 160 for the coordinate-1-fixing elements, 20*8 = 160 for the others.
#  CC-Q countercontrol: the D5 seed with 8 replaced by 6 (= |u5|^2 (2p_1 - 1)) is PSD (rank-one condition met with
#      equality: det of the 2x2 compression is 0), so the construction needs lambda > 6.
import itertools
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, expand, conjugate, kronecker_product as kron

R_ = []
def rec(kind, cid, ok, text, detail=""):
    ok = bool(ok); R_.append(ok)
    print(f"{kind} {cid:<6} {'PASS' if ok else 'FAIL'} {text}" + (f" -- {detail}" if detail else ""))

I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
ZF = [zdef(*s) for s in SS]
def negvec(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]; return v / sqrt(expand((v.H * v)[0]))
PSI = [sp.simplify(negvec(z)) for z in ZF]
def P(v): return v * v.H
def tr(M): return expand(M.trace())
def ip(A, B): return expand((A * B).trace())
def dpsi(d): return sum((d[k] * P(PSI[k]) for k in range(4)), zeros(4, 4))
def pi_(X): return [expand((PSI[k].H * X * PSI[k])[0]) for k in range(4)]
def comb(c): return sum((c[k] * PSI[k] for k in range(4)), zeros(4, 1))
def Ssum(d): return sum(d)
def circ_margin(d):     # S^2/4 - |d - S/4 1|^2 ; d in Circ iff S >= 0 and margin >= 0
    S = Ssum(d); return expand(S ** 2 / 4 - sum((x - S / 4) ** 2 for x in d))
def in_circ(d, strict=False):
    S = Ssum(d); m = circ_margin(d)
    return (S > 0 and m > 0) if strict else (S >= 0 and m >= 0)
def in_R(d): S = Ssum(d); return all(x <= S / 2 for x in d)
def in_O(d): S = Ssum(d); return all(x >= 0 for x in d) and all(x <= S / 2 for x in d)
def red_A(g):
    rho = g * g.H; return Matrix(2, 2, lambda i, j: sum(rho[2 * i + k, 2 * j + k] for k in range(2)))

print("== W0 conventions")
ok_on = all(expand((PSI[i].H * PSI[j])[0]) == (1 if i == j else 0) for i in range(4) for j in range(4))
ok_real = all(x.is_real for v in PSI for x in v)
ok_me = all(expand(red_A(v) - eye(2) / 2) == zeros(4 // 2, 4 // 2) for v in PSI)
ok_z = all(expand(pauliW(ZF[k]) - (eye(4) - 2 * P(PSI[k])) / 8) == zeros(4, 4) for k in range(4))
ok_R = all(expand(dpsi([1 - 2 * (j == k) for j in range(4)]) - 8 * pauliW(ZF[k])) == zeros(4, 4) for k in range(4))
rec("CHECK", "W0", ok_on and ok_real and ok_me and ok_z and ok_R,
    "psi_s real orthonormal maximally entangled; pauliW(z_s) = (I - 2P_s)/8; diag_psi(1 - 2e_s) = 8 pauliW(z_s)")

print("== C1 Circ facts")
okO = all(in_circ([1 if k in (s, t) else 0 for k in range(4)]) and circ_margin([1 if k in (s, t) else 0 for k in range(4)]) == 0
          and expand(sum(((1 if k in (s, t) else 0) - Q(1, 2)) ** 2 for k in range(4))) == 1
          for s, t in itertools.combinations(range(4), 2))
yd = [Q(-2, 5), Q(12, 5), Q(6, 5), Q(4, 5)]
Syd = Ssum(yd); ydp = [Syd / 2 - x for x in yd]
u_yd = [x - Syd / 4 for x in yd]; u_ydp = [x - Ssum(ydp) / 4 for x in ydp]
ok_c1 = (circ_margin(yd) == 0 and Syd > 0 and circ_margin(ydp) == 0 and Ssum(ydp) > 0
         and expand(sum(a * b for a, b in zip(yd, ydp))) == 0 and all(a == -b for a, b in zip(u_yd, u_ydp))
         and min(yd) < 0 and min(ydp) < 0)
rec("CHECK", "C1", okO and ok_c1,
    "e_s + e_t on the boundary of Circ (O in Circ), |e_s + e_t - 1/2|^2 = 1; y_d, y_d' boundary, orthogonal, u(y_d') = -u(y_d)",
    "y_d = %s, y_d' = %s" % (yd, ydp))

print("== D2 the diagonal surgery K^Circ is not self-dual")
v2 = comb([0, 1, Q(1, 2), 0]); Pv2 = P(v2); p2 = pi_(Pv2)
c0 = [a - b for a, b in zip(yd, p2)]
y2 = Pv2 + dpsi(c0)
off23 = expand((PSI[1].H * y2 * PSI[2])[0])
ok_d2 = (p2 == [0, 1, Q(1, 4), 0] and c0 == [Q(-2, 5), Q(7, 5), Q(19, 20), Q(4, 5)] and in_circ(c0, strict=True)
         and pi_(y2) == yd and off23 == Q(1, 2) and pi_(y2)[0] < 0 and not in_circ(p2))
rec("CHECK", "D2", ok_d2,
    "y = P_v + diag_psi(c0): pi(y) = y_d (extreme ray of Circ with a negative entry), c0 in int Circ, <psi_2|y|psi_3> = 1/2, p not in Circ",
    "c0 margin %s, p margin %s, y_11 = %s" % (circ_margin(c0), circ_margin(p2), pi_(y2)[0]))

print("== CC-R countercontrol: no such witness for the slice R")
ps = sp.symbols('p1:5', nonnegative=True)
cc_ok = True
for s in range(4):
    ydR = [1 - 2 * (k == s) for k in range(4)]
    diff = [ydR[k] - ps[k] for k in range(4)]
    S = Ssum(diff)
    facets = [expand(S / 2 - diff[k]) for k in range(4) if k != s]     # must all be >= 0 for diff in R
    cc_ok = cc_ok and expand(sum(facets) + Ssum(ps) / 2) == 0            # sum of the three facet slacks = -sum(p)/2
rec("COUNTERCONTROL", "CC-R", cc_ok,
    "for each extreme ray 1 - 2e_s of R: the facet slacks of (1 - 2e_s) - p at t != s sum to -sum(p)/2, so p >= 0 in R forces p = 0")

print("== D4 the sandwich C0 <= K' <= C0* and an incompatible pair in the gap")
v4 = comb([5, 3, 3, 1]); Pv4 = P(v4); p4 = pi_(Pv4)
u4 = comb([Q(1, 2), Q(-1, 2), Q(-1, 2), Q(1, 2)]); Pu4 = P(u4); pu4 = pi_(Pu4)
z1 = [-1, 1, 1, 1]
w4 = Pu4 + dpsi([Q(1, 2) * x for x in z1])
pw4 = pi_(w4)
ip_wv = ip(w4, Pv4)
perm_vals = sorted(set(expand(sum(pu4[k] * (1 - 2 * (k == a)) for k in range(4))) for a in range(4)))
zz_vals = sorted(set(sum((1 - 2 * (k == a)) * (1 - 2 * (k == 0)) for k in range(4)) for a in range(4)))
ok_d4 = (p4 == [25, 9, 9, 1] and in_circ(p4, strict=True) and not in_O(p4)
         and expand((u4.H * v4)[0]) == 0 and pu4 == [Q(1, 4)] * 4 and in_O(pu4)
         and pw4 == [Q(-1, 4), Q(3, 4), Q(3, 4), Q(3, 4)] and in_circ(pw4) and in_R([Q(1, 2) * x for x in z1])
         and ip_wv == -3 and perm_vals == [Q(1, 2)] and zz_vals == [0, 4])
rec("CHECK", "D4", ok_d4,
    "P_v (profile (25,9,9,1) in Circ \\ O) and w = P_u + (1/2)diag_psi(-1,1,1,1) (pi(w) in Circ, w in Q3 + R) lie in C0*, tr(w P_v) = -3",
    "pi(w) = %s, Circ margins %s / %s; <P_u, g z> = %s, <z, g z> in %s" % (pw4, circ_margin(p4), circ_margin(pw4), perm_vals, zz_vals))

print("== D5 the fibre over the simplex slice")
u5 = comb([3, 1, 1, 1]); Pu5 = P(u5)
y5 = Pu5 + dpsi([8 * x for x in z1])
x5 = comb([3, -1, -1, -1])
neg5 = expand((x5.H * y5 * x5)[0])
pu5 = pi_(Pu5)
a_fix = expand(sum(pu5[k] * z1[k] for k in range(4)))                    # <u u^dag, z>, g fixing coordinate 1
a_mov = sorted(set(expand(sum(pu5[k] * (1 - 2 * (k == a)) for k in range(4))) for a in range(1, 4)))
lb_fix = 2 * 8 * a_fix + 8 ** 2 * 4                                       # |<u,gu>|^2 >= 0 dropped
lb_mov = 8 * 2 * min(a_mov)                                               # <z, g z> = 0
ok_d5 = (pi_(y5) == [1, 9, 9, 9] and neg5 == -12 and a_fix == -6 and a_mov == [10] and lb_fix == 160 and lb_mov == 160
         and all(x >= 0 for x in pi_(y5)))
rec("CHECK", "D5", ok_d5,
    "y5 = u u^dag + 8 diag_psi(-1,1,1,1): pi(y5) = (1,9,9,9) >= 0, x^dag y5 x = -12 (not PSD); orbit pairings >= 160 > 0",
    "<uu^dag, z> = %s (coordinate fixed), %s (moved); lower bounds %s, %s" % (a_fix, a_mov, lb_fix, lb_mov))

print("== CC-Q countercontrol: lambda = |u|^2 (2 p_1 - 1) = 6 gives a PSD table")
y6 = Pu5 + dpsi([6 * x for x in z1])
ev6 = [sp.nsimplify(e) for e in (Matrix(4, 4, lambda i, j: expand((PSI[i].H * y6 * PSI[j])[0]))).eigenvals().keys()]
rec("COUNTERCONTROL", "CC-Q", all(e >= 0 for e in ev6) and 0 in ev6,
    "at lambda = 6 the table is PSD with a zero eigenvalue: the seed needs 6 < lambda <= 9", "eigenvalues %s" % ev6)

nfail = R_.count(False)
print("summary: %d checks, %d failed" % (len(R_), nfail))
if nfail == 0:
    print("VERDICT C7-EBF-WALL-EXACT: K^Circ is not self-dual (witness pi(y) = %s, off-diagonal entry %s); the sandwich gap "
          "carries the incompatible pair tr(w P_v) = %s; the simplex-slice seed is non-PSD (%s) with orbit pairings >= %s; "
          "no witness exists for the slice R" % (yd, off23, ip_wv, neg5, min(lb_fix, lb_mov)))
else:
    print("NO VERDICT")
