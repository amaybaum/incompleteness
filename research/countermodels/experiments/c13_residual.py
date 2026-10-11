# c13_residual.py -- research/countermodels node C13 (round 3): B3.C's residual region (C10.3) from the cone side.
# DECISION RULE (fixed before the first run, 2026-10-11T00:51:17Z by date -u; predictions in NOTES-C13 S0, 00:50:00Z):
#  Exact arithmetic only (int, Fraction, Gaussian rationals GQ); no float (guard EX). Omega(u, w) = (u0 w3 + u3 w0 - u1 w2 -
#  u2 w1)/2 (det Psi(v) = Omega(v, v)); |Om^|_{kl}^2 := |Omega(b_k, b_l)|^2/(|b_k|^2 |b_l|^2) (rational). On a circle
#  {sqrt(p) b3^ + sqrt(1-p) e^{it} b_j^} (b3 a product, so Omega(b3, b3) = 0) the minimum over t of |det Psi|^2 is
#  D_j = (1-p)(2 sqrt(p) A - sqrt(1-p) B)^2, A^2 = |Om^_3j|^2, B^2 = |Om^_jj|^2 ([W] in NOTES-C13); decided exactly:
#  D_j > 0 iff 4pA^2 != (1-p)B^2; D_j >= delta iff L = 4pA^2 + (1-p)B^2 - delta/(1-p) >= 0 and L^2 >= 16p(1-p)A^2B^2.
#  H1 for a defect I - cP_v with |det Psi(v)|^2 >= D (unit v): c lambda_max <= 1 iff 1 - 4D <= (2/c - 1)^2, i.e. D >= delta(c)
#  := (1 - (2/c - 1)^2)/4.
#  R0 basis: b1 = (2,3)(x)(2,-1+2i), b2 = CNOT b1, b3 = |0>(x)(1+2i, 2), b4 = (10, -5+10i, -6-12i, -6-12i): pairwise orthogonal;
#     det Psi(b1) = det Psi(b3) = 0 (products), det Psi(b2), det Psi(b4) != 0 (entangled); CNOT b3 = b3, CNOT b4 = b4;
#     <b1|CNOT|b1> = 0.
#  R1 minimal group G_min = closure<T^3 (diagonal unitaries in {b_k}), cnot>: dim ker(CNOT + I) = 1 (E- = C|1->), CNOT b1 = b2,
#     span(b3, b4) in E+; the product lines in span(b3, b4) are exactly L_A = b3 (in |0>(x)C^2) and L_B = (3,3,-2,-2) (in
#     C^2(x)|+>) (each intersection one-dimensional), and <L_A|L_B> != 0: no orthonormal product basis of span(b3, b4).
#     C10.2's cone for G_min: d4 = I - (32/25) P_{b4}: H1 (D = |det Psi(b4^)|^2 >= delta(32/25)); spectrum (-7/25, 1, 1, 1)
#     (X's single-defect condition lambda2 >= -lambda1); fixed by the torus (diagonal) and CNOT.
#  R2 case A: G_A = T^3 x| <cnot, g>, g the monomial transposition b1^ <-> b4^ (Pi = S3 on {1, 2, 4}; b3 fixed product; b2, b4
#     entangled, each G_A-equivalent to the product b1). h = (9+2i) b3 + b1: weight p on b3^ equals 85/98. For j in {1, 2, 4}:
#     D_j > 0 (the three orbit circles are product-free: h unreachable) and D_j >= delta(c), c = 251/250 (H1). s_min =
#     min(p^2, (2p-1)^2) = (36/49)^2 and c^2 s_min >= 4(c - 1) ((CC) for every pair of the orbit). The slice image
#     pi(d_h) = diag(1 - c(1-p), 1, 1 - cp, 1) in R^4_+. Spot checks at rational points w in {1, i, -1, -i, (3+4i)/5,
#     (5+12i)/13, (-7+24i)/25} of the circles j = 1, 2 (v = (9+2i) b3 + w b_j, same weights since |b1| = |b2|): det ratio >=
#     delta(c) and > 0; pairwise overlaps >= s_min.
#  R3 case B: G_B = T^3 x| <cnot, g'>, g' the transposition b3^ <-> b4^ (Pi = <(12), (34)>): residual (b2 ~ b1, b4 ~ b3).
#     h_B = 2 b1 + b2 (weights 4/5, 1/5), its orbit circles in span(b1, b2) (weights 4/5 and 1/5 on b1^) product-free (D > 0);
#     h' = b1 - 2 b2 = D CNOT h_B (D = diag(1, -1, 1, 1) in {b_k}) is orthogonal to h_B. For c in {101/100, 3/2}: y = P_hB + lam
#     d_h', lam = (c-1)/(4-2c): <y, d_hB> = 0, h'^dag y h' < 0, and at sample orbit points l (the two circles at the w above)
#     <y, d_l> - c(1 - s(h_B, h_l)) = lam c^2 s(h', h_l) >= 0 (the identity behind Lemma C13-O).
#  R4 torus node S2 (stage 4: actC Rz(t) o actT Rx(f)): at a rational point (half-angle cos/sin = 3/5, 4/5 and 5/13, 12/13)
#     U = Rz (x) Rx commutes with CNOT and is diagonal in (|0+>, |0->, |1+>, |1->) with four distinct eigenvalues; h = (3, 3, 1, -1)
#     (= 3|0+> + |1->, up to sqrt2); the circle v_w = (3, 3, w, -w): CNOT v_w = v_{-w}, U v_w is proportional to v_{w'} with
#     |w'| = 1; |det Psi(v_w)|^2/|v_w|^4 = 9/100 (lambda_max = 9/10) for every listed w; overlaps >= 16/25; c = 21/20: H1
#     (c 9/10 <= 1) and (CC) c^2 (16/25) >= 4(c - 1). With G16: (I(x)Z) maps |0+> -> |0->, |1-> -> |1+> (a double transposition)
#     and <v_w | (I(x)Z) v_w'> = 0 for all listed w, w' (orthogonal pairs in the G16-orbit).
#  CC1 the Bell circle of S2 (|0+> + w|1->, p = 1/2): v_1 and v_{-1} are orthogonal ((CC) fails; consistent with K_T, C7.6).
#  CC2 case A with h_B's support {b1, b2}: the G_A-orbit of h_B contains h' (orthogonal): dominance on the fixed b3 is needed.
#  CC3 case A at c = 101/100: the H1 decision fails on circle j = 2 (D_2 < delta(101/100)): the window is real.
#  VERDICT C13-RESIDUAL-EXACT iff every CHECK passes and every COUNTERCONTROL behaves as stated; else NO VERDICT.
from fractions import Fraction as Fr

RES = []
def rec(kind, cid, ok, text, detail=''):
    ok = bool(ok); RES.append(ok)
    print('%s %-4s %s %s%s' % (kind, cid, 'PASS' if ok else 'FAIL', text, (' -- ' + detail) if detail else ''))

class GQ:
    __slots__ = ('r', 'i')
    def __init__(self, r, i=0):
        self.r = r if isinstance(r, Fr) else Fr(r); self.i = i if isinstance(i, Fr) else Fr(i)
    def __add__(s, o): o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r + o.r, s.i + o.i)
    __radd__ = __add__
    def __sub__(s, o): o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r - o.r, s.i - o.i)
    def __rsub__(s, o): return GQ(o) - s
    def __neg__(s): return GQ(-s.r, -s.i)
    def __mul__(s, o):
        o = o if isinstance(o, GQ) else GQ(o); return GQ(s.r * o.r - s.i * o.i, s.r * o.i + s.i * o.r)
    __rmul__ = __mul__
    def conj(s): return GQ(s.r, -s.i)
    def n2(s): return s.r * s.r + s.i * s.i
    def __truediv__(s, o):
        if not isinstance(o, GQ): o = GQ(o)
        d = o.n2(); t = s * o.conj(); return GQ(t.r / d, t.i / d)
    def iszero(s): return s.r == 0 and s.i == 0
    def __eq__(s, o): o = o if isinstance(o, GQ) else GQ(o); return s.r == o.r and s.i == o.i
    def __hash__(s): return hash((s.r, s.i))
ZERO, ONE, II = GQ(0), GQ(1), GQ(0, 1)
def V(*xs): return [x if isinstance(x, GQ) else GQ(x) for x in xs]
def kron2(a, b): return [a[0] * b[0], a[0] * b[1], a[1] * b[0], a[1] * b[1]]
def ipv(u, v): return sum((u[t].conj() * v[t] for t in range(len(u))), ZERO)
def n2v(v): return sum((x.n2() for x in v), Fr(0))
def ovl(u, v): return ipv(u, v).n2() / (n2v(u) * n2v(v))
def det(v): return v[0] * v[3] - v[1] * v[2]
def detr(v): return det(v).n2() / n2v(v) ** 2
def Om(u, w): return (u[0] * w[3] + u[3] * w[0] - u[1] * w[2] - u[2] * w[1]) / 2
def Om2(u, w): return Om(u, w).n2() / (n2v(u) * n2v(w))
def add(u, v): return [u[t] + v[t] for t in range(4)]
def sc(c, v): return [GQ(c) * x if not isinstance(c, GQ) else c * x for x in v]
def CNOTv(v): return [v[0], v[1], v[3], v[2]]
def canon(v):
    k = next(t for t in range(4) if not v[t].iszero()); a = v[k]; return tuple(x / a for x in v)
def proj(v):
    n = n2v(v); return [[v[i] * v[j].conj() / n for j in range(4)] for i in range(4)]
def eye4(): return [[ONE if i == j else ZERO for j in range(4)] for i in range(4)]
def dvec(v, c): P = proj(v); return [[(ONE if i == j else ZERO) - GQ(c) * P[i][j] for j in range(4)] for i in range(4)]
def mmul(A, B): return [[sum((A[i][t] * B[t][j] for t in range(4)), ZERO) for j in range(4)] for i in range(4)]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(4)] for i in range(4)]
def mscale(c, A): return [[GQ(c) * x for x in r] for r in A]
def tr(A): return sum((A[i][i] for i in range(4)), ZERO)
def hip(A, B): return tr(mmul(A, B))
def mv(A, v): return [sum((A[i][t] * v[t] for t in range(4)), ZERO) for i in range(4)]
def delta(c): return (1 - (2 / c - 1) ** 2) / 4
def D_pos(p, A2, B2): return 4 * p * A2 != (1 - p) * B2
def D_ge(p, A2, B2, dl):
    L = 4 * p * A2 + (1 - p) * B2 - dl / (1 - p)
    return L >= 0 and L * L >= 16 * p * (1 - p) * A2 * B2
W = [ONE, II, GQ(-1), GQ(0, -1), GQ(Fr(3, 5), Fr(4, 5)), GQ(Fr(5, 13), Fr(12, 13)), GQ(Fr(-7, 25), Fr(24, 25))]

# ---------- R0
b1 = kron2(V(2, 3), V(2, GQ(-1, 2)))
b2 = CNOTv(b1)
b3 = kron2(V(1, 0), V(GQ(1, 2), 2))
b4 = V(10, GQ(-5, 10), GQ(-6, -12), GQ(-6, -12))
B = [b1, b2, b3, b4]
orth = all(ipv(B[a], B[b]).iszero() for a in range(4) for b in range(4) if a != b)
prods = det(b1).iszero() and det(b3).iszero() and not det(b2).iszero() and not det(b4).iszero()
cfix = CNOTv(b3) == b3 and CNOTv(b4) == b4
swap0 = ipv(b1, CNOTv(b1)).iszero()
rec('CHECK', 'R0', orth and prods and cfix and swap0, 'eigenbasis: b1, b3 products, b2 = CNOT b1 and b4 entangled, CNOT fixes b3, b4, <b1|CNOT|b1> = 0',
    'norms^2 %s' % [n2v(b) for b in B])

# ---------- R1 minimal group
# ker(CNOT + I): v with v0 = -v0, v1 = -v1, v3 = -v2  -> v0 = v1 = 0, v3 = -v2: one-dimensional, spanned by (0,0,1,-1)
# (CNOT + I) v = (2 v0, 2 v1, v2 + v3, v2 + v3): its rows (2,0,0,0), (0,2,0,0), (0,0,1,1) are independent and the fourth equals
# the third, so the rank is 3 and ker(CNOT + I) is one-dimensional, spanned by |1-> ~ (0,0,1,-1)
CPI = [[GQ(2) if i == j and i < 2 else ZERO for j in range(4)] for i in range(2)] + [V(0, 0, 1, 1), V(0, 0, 1, 1)]
m1 = V(0, 0, 1, -1)
kerdim1 = (CPI[2] == CPI[3] and CPI[0] == V(2, 0, 0, 0) and CPI[1] == V(0, 2, 0, 0) and CPI[2] == V(0, 0, 1, 1)
           and CNOTv(m1) == sc(-1, m1) and all(CNOTv(b) != sc(-1, b) for b in (b3, b4)))
LA = b3
LB = V(3, 3, -2, -2)
inspan = all(ipv(LB, b).iszero() for b in (b1, b2))
LBprod = det(LB).iszero() and LB[0] == LB[1] and LB[2] == LB[3]
# intersections are one-dimensional: (a, b, 0, 0) orthogonal to b1 forces b = -(conj(b1_0)/conj(b1_1)) a ... (b1, b2 share entries 0, 1)
oneA = not b1[1].iszero()      # the single condition conj(b1_0) a + conj(b1_1) b = 0 is non-degenerate in b
oneB = not ((b1[2] + b1[3]).iszero())   # (a, a, e, e): conj(b1_0+b1_1) a + conj(b1_2 + b1_3) e = 0 non-degenerate in e
nonorth = not ipv(LA, LB).iszero()
c4 = Fr(32, 25)
Db4 = detr(b4)
h1b4 = 1 - 4 * Db4 <= (2 / c4 - 1) ** 2
spec = (1 - c4) < 0 and 1 >= c4 - 1
rec('CHECK', 'R1', kerdim1 and inspan and LBprod and oneA and oneB and nonorth and h1b4 and spec,
    'minimal group: E- one-dimensional; the product lines of span(b3, b4) are L_A = b3 and L_B = (3,3,-2,-2), not orthogonal, so b4 is an entangled cnot-fixed eigenline; C10.2: K({I - (32/25)P_b4}) is explicit (H1, X\'s condition)',
    '<L_A|L_B> = %s; |det Psi(b4^)|^2 = %s; 1 - 4D = %s <= (2/c - 1)^2 = %s' % (ipv(LA, LB).r if ipv(LA, LB).i == 0 else (ipv(LA, LB).r, ipv(LA, LB).i), Db4, 1 - 4 * Db4, (2 / c4 - 1) ** 2))

# ---------- R2 case A
al = GQ(9, 2)
h = add(sc(al, b3), b1)
p = al.n2() * n2v(b3) / n2v(h)
cA = Fr(251, 250)
dA = delta(cA)
circ = {}
okA = p == Fr(85, 98)
for j, bj in ((1, b1), (2, b2), (4, b4)):
    A2 = Om2(b3, bj); B2 = Om2(bj, bj)
    pos = D_pos(p, A2, B2); ge = D_ge(p, A2, B2, dA)
    circ[j] = (A2, B2, pos, ge)
    okA &= pos and ge
smin = min(p * p, (2 * p - 1) ** 2)
ccA = cA * cA * smin >= 4 * (cA - 1)
slice_ok = all(x >= 0 for x in (1 - cA * (1 - p), 1 - cA * p))
spot_ok = True; pts = []
for j, bj in ((1, b1), (2, b2)):
    for w in W:
        v = add(sc(al, b3), sc(w, bj))
        dr = detr(v)
        spot_ok &= dr > 0 and dr >= dA
        pts.append(v)
ovmin = min(ovl(pts[a], pts[b]) for a in range(len(pts)) for b in range(a + 1, len(pts)) if canon(pts[a]) != canon(pts[b]))
spot_ok &= ovmin >= smin
rec('CHECK', 'R2', okA and ccA and slice_ok and spot_ok and smin == Fr(1296, 2401),
    'case A (Pi = S3): h = (9+2i) b3 + b1 (p = 85/98) is unreachable, H1 holds on its three orbit circles at c = 251/250, (CC) holds for every pair (s_min = (36/49)^2): K(G_A (I - cP_h)) is explicit given Theorem S\' (compact Z)',
    'circles (A^2, B^2): %s; smallest spot overlap %s; pi(d_h) = (%s, 1, %s, 1)' % ({j: (str(v[0]), str(v[1])) for j, v in circ.items()}, ovmin, 1 - cA * (1 - p), 1 - cA * p))

# ---------- R3 case B
hB = add(sc(2, b1), b2)
hp = add(b1, sc(-2, b2))
Dm = [ONE, GQ(-1), ONE, ONE]     # diag in {b_k}: acts on coefficients
# h' = D CNOT h_B: CNOT h_B = 2 b2 + b1; D multiplies the b2-coefficient by -1 -> b1 - 2 b2
via = add(b1, sc(-2, b2)) == hp and CNOTv(hB) == add(sc(2, b2), b1)
orthB = ipv(hB, hp).iszero()
qB = Fr(4, 5)
okB = orthB and via
for q in (qB, 1 - qB):
    okB &= D_pos(q, Om2(b1, b2), Om2(b2, b2))   # circle {sqrt(q) b1^ + sqrt(1-q) w b2^}: b1 product, Omega(b1,b1) = 0
witrec = []
samp = []
for w in W:
    samp.append(add(sc(2, b1), sc(w, b2))); samp.append(add(b1, sc(GQ(2) * w, b2)))
for c in (Fr(101, 100), Fr(3, 2)):
    lam = (c - 1) / (4 - 2 * c)
    y = madd(proj(hB), mscale(lam, dvec(hp, c)))
    p0 = hip(y, dvec(hB, c))
    q = ipv(hp, mv(y, hp))
    idok = True
    for l in samp:
        lhs = hip(y, dvec(l, c)).r - c * (1 - ovl(hB, l))
        rhs = lam * c * c * ovl(hp, l)
        idok &= lhs == rhs and lhs >= 0
    okB &= p0.iszero() and q.i == 0 and q.r < 0 and idok
    witrec.append('c=%s: <y,d_hB>=%s, h\'^dag y h\'/|h\'|^2=%s' % (c, p0.r, q.r / n2v(hp)))
rec('CHECK', 'R3', okB, 'case B (Pi = <(12),(34)>): h_B = 2b1 + b2 unreachable, h\' = D CNOT h_B orthogonal to it; exact witness y in K* \\ K for every c (Lemma C13-O identity at sample orbit points)', '; '.join(witrec))

# ---------- R4 torus node S2
def Urz_rx(cz, sz, cx, sx):
    # Rz on control: diag(cz - i sz, cz + i sz); Rx on target: cx I - i sx X
    Rz = [[GQ(cz, -sz), ZERO], [ZERO, GQ(cz, sz)]]
    Rx = [[GQ(cx), GQ(0, -sx)], [GQ(0, -sx), GQ(cx)]]
    return [[Rz[i // 2][j // 2] * Rx[i % 2][j % 2] for j in range(4)] for i in range(4)]
U = Urz_rx(Fr(3, 5), Fr(4, 5), Fr(5, 13), Fr(12, 13))
CN = [[ONE if (i, j) in ((0, 0), (1, 1), (2, 3), (3, 2)) else ZERO for j in range(4)] for i in range(4)]
comm = mmul(U, CN) == mmul(CN, U)
E = {'0+': V(1, 1, 0, 0), '0-': V(1, -1, 0, 0), '1+': V(0, 0, 1, 1), '1-': V(0, 0, 1, -1)}
eig = {}
diag_ok = True
for k, e in E.items():
    Ue = mv(U, e); kk = next(t for t in range(4) if not e[t].iszero()); lamk = Ue[kk] / e[kk]
    diag_ok &= Ue == sc(lamk, e); eig[k] = lamk
distinct = len(set(eig.values())) == 4
okS2 = comm and diag_ok and distinct
cS = Fr(21, 20)
for w in W:
    v = V(3, 3, w, -w)
    okS2 &= detr(v) == Fr(9, 100) and canon(CNOTv(v)) == canon(V(3, 3, -w, w))
    Uv = mv(U, v)
    ratio = Uv[2] / Uv[0] * 3            # v_{w'} has third entry w' when the first entry is 3
    okS2 &= canon(Uv) == canon(V(3, 3, ratio, -ratio)) and ratio.n2() == 1
ptsS = [V(3, 3, w, -w) for w in W]
ovS = min(ovl(ptsS[a], ptsS[b]) for a in range(len(ptsS)) for b in range(a + 1, len(ptsS)))
okS2 &= ovS >= Fr(16, 25) and cS * Fr(9, 10) <= 1 and cS * cS * Fr(16, 25) >= 4 * (cS - 1)
IZ = lambda v: [v[0], -v[1], v[2], -v[3]]
dbl = canon(IZ(E['0+'])) == canon(E['0-']) and canon(IZ(E['1-'])) == canon(E['1+'])
orthG16 = all(ipv(V(3, 3, w, -w), IZ(V(3, 3, w2, -w2))).iszero() for w in W for w2 in W)
rec('CHECK', 'R4', okS2 and dbl and orthG16,
    'torus node S2 without G16: the circle {3|0+> + w|1->} is an orbit with lambda_max = 9/10, overlaps >= 16/25; at c = 21/20 H1 and (CC) hold: an explicit exotic cone given S\'; with G16 the double transposition (I(x)Z) gives orthogonal pairs',
    'distinct torus eigenvalues %s; smallest overlap on the sampled circle %s' % (distinct, ovS))

# ---------- countercontrols
cc1 = ipv(V(1, 1, 1, -1), V(1, 1, -1, 1)).iszero()
rec('COUNTERCONTROL', 'CC1', cc1, 'the Bell circle of S2 (p = 1/2): |0+> + |1-> and |0+> - |1-> are orthogonal ((CC) fails; K_T, C7.6)')
rec('COUNTERCONTROL', 'CC2', orthB and via, 'case A: the G_A-orbit of h_B (support {b1, b2}) contains the orthogonal h\' (cnot is in G_A): dominance on the fixed product b3 is needed')
cc3 = not D_ge(p, Om2(b3, b2), Om2(b2, b2), delta(Fr(101, 100)))
rec('COUNTERCONTROL', 'CC3', cc3, 'case A at c = 101/100: H1 fails on the circle through b2 (the window c <= ~1.005 is real)')

def nofloat(x):
    if isinstance(x, float): return False
    if isinstance(x, (list, tuple)): return all(nofloat(y) for y in x)
    return True
rec('CHECK', 'EX', nofloat([p, smin, ovmin, ovS, Db4]), 'no float in any recorded value')
nf = sum(1 for r in RES if not r)
print('summary: %d checks, %d failed' % (len(RES), nf))
if nf == 0:
    print('VERDICT C13-RESIDUAL-EXACT: in the minimal group the cnot swap forces an entangled cnot-fixed eigenline (C10.2 explicit); '
          'case A (Pi = S3, fixed product b3): h = (9+2i)b3 + b1 (p = %s) gives three product-free orbit circles with H1 at c = %s '
          'and (CC) (s_min = %s): an explicit cone with a continuum of non-PSD extreme rays given S\'; case B (Pi = <(12),(34)>): '
          'orthogonal pairs and exact witnesses; the S2 torus node without G16: the circle surgery at c = %s' % (p, cA, smin, cS))
else:
    print('NO VERDICT')
