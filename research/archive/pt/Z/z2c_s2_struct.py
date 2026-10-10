"""z2c_s2_struct.py -- thread Z, node S2 (the commuting torus with G16): structure, group, Bell-type seeds. EXACT.

Notation: computational basis |00>,|01>,|10>,|11> (first = control). Basis B = (|0+>, |1->, |0->, |1+>) (columns of W);
V1 = span(|0+>, |1->), V2 = span(|0->, |1+>). Circles C1(g) = (|0+> + e^{ig}|1->)/sqrt2, C2(g) = (|0-> + e^{ig}|1+>)/sqrt2.
Torus T2c = {Ad(Rz(th) (x) Rx(ph))}, Rz(th) = diag(e^{-i th/2}, e^{i th/2}), Rx(ph) = e^{-i ph/2} P+ + e^{i ph/2} P-.
G16 = <Ad(CNOT), Ad(Z(x)I), Ad(I(x)Z), T> (T = complex conjugation), as recorded and re-checked in z1.
DECISION RULE (fixed before the first run). Every line PASS/FAIL, exact sympy (symbols th, ph, g real).
  A1  W^* CNOT W = diag(1, -1, 1, 1) (the amendment's CNOT = I(x)P+ + Z(x)P-, a CZ in basis B); also
      CNOT = I(x)P+ + Z(x)P- as matrices.
  A2  W^* (Rz(th)(x)Rx(ph)) W = diag(e^{-i(th+ph)/2}, e^{i(th+ph)/2}, e^{-i(th-ph)/2}, e^{i(th-ph)/2}); it commutes
      with CNOT.
  A3  each of torus, CNOT, Z(x)I, I(x)Z, T maps C1 u C2 into C1 u C2 (symbolic g): image has zero weight off one V_k
      and equal weights 1/2 on its two poles; the torus acts transitively on each circle (relative phase th + ph on
      C1, th - ph on C2).
  A4  every C_k(g) and CNOT C_k(g) is maximally entangled: |det(coefficient matrix)|^2 = 1/4 (symbolic g).
  A5  the four psi_s of Z_F (z1) are C1(0), C1(pi), C2(0), C2(pi) up to phase (F = e_(1,1) at C1(0)).
  A6  Bell-type seed classification: in the product basis (|0+>, |0->, |1+>, |1->) with coefficients c00, c01, c10,
      c11, A = c00 c11, B = c01 c10: the torus fixes A and B; CNOT sends (A, B) to (-A, B); Z(x)I to (-A, -B);
      I(x)Z to (B, A); T to (conj A, conj B); and |A - B|^2 + |A + B|^2 = 2(|A|^2 + |B|^2) (identities, symbolic).
      With the AM-GM bounds |A| <= (|c00|^2+|c11|^2)/2, |B| <= (|c01|^2+|c10|^2)/2 [W], a maximally entangled psi
      has a maximally entangled orbit iff psi lies on C1 u C2.
  A7  group: the unitary part of G16 has 8 elements mod phase (closure of CNOT, Z(x)I, I(x)Z in basis B); exactly
      two of them lie in the torus (criterion: B-diagonal with d1 d2 = d3 d4): I and Z(x)I. So the identity
      component of S2 = <T2c, G16> is T2c (dim 2) and its component group G16/<Ad(Z(x)I)> has order 8.
  A8  the larger torus T3 = all B-diagonal unitaries contains CNOT (diag(1,-1,1,1)) and e^{i chi Z(x)X}
      (diag(e^{i chi}, e^{i chi}, e^{-i chi}, e^{-i chi})) and maps each circle onto itself (symbolic chi).
 Countercontrols (each must be REJECTED):
  CC1 the Bell state Phi+ = (|00> + |11>)/sqrt2 is maximally entangled but CNOT Phi+ = |+>|0> is a product
      (|det|^2 = 0), so the seed test rejects it.
  CC2 a local map outside the group, Ad(H(x)I), sends C1(0) off C1 u C2 (the circle-invariance test rejects it).
  CC3 CNOT is not in the torus (the A7 criterion rejects diag(1,-1,1,1): d1 d2 = -1 != d3 d4 = 1).
VERDICT 'VERDICT S2-STRUCT-EXACT' only if all checks PASS and all countercontrols are REJECTED; else
'VERDICT S2-STRUCT-FAILED'.
"""
import sympy as sp

I, sq2 = sp.I, sp.sqrt(2)
th, ph, g, chi = sp.symbols('theta phi gamma chi', real=True)
results = []


def check(name, ok, note=''):
    results.append((name, bool(ok)))
    print(f"{name:5s} {'PASS' if ok else 'FAIL'}  {note}")


def zero(M):
    return sp.simplify(sp.expand(M)) == sp.zeros(*M.shape)


def ket(*v):
    return sp.Matrix(v)


k0p, k1m = ket(1, 1, 0, 0) / sq2, ket(0, 0, 1, -1) / sq2
k0m, k1p = ket(1, -1, 0, 0) / sq2, ket(0, 0, 1, 1) / sq2
W = sp.Matrix.hstack(k0p, k1m, k0m, k1p)
s0, sx, sz = sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[1, 0], [0, -1]])
Pp, Pm = (s0 + sx) / 2, (s0 - sx) / 2
CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
ZI, IZ = sp.kronecker_product(sz, s0), sp.kronecker_product(s0, sz)
Rz = sp.diag(sp.exp(-I * th / 2), sp.exp(I * th / 2))
Rx = sp.exp(-I * ph / 2) * Pp + sp.exp(I * ph / 2) * Pm
TOR = sp.kronecker_product(Rz, Rx)

print('== A  basis B, CNOT, torus')
okA1 = zero(W.H * CN * W - sp.diag(1, -1, 1, 1)) and zero(CN - (sp.kronecker_product(s0, Pp) +
                                                                    sp.kronecker_product(sz, Pm)))
check('A1', okA1, 'W* CNOT W = diag(1,-1,1,1); CNOT = I(x)P+ + Z(x)P- (amendment)')
D = sp.diag(sp.exp(-I * (th + ph) / 2), sp.exp(I * (th + ph) / 2), sp.exp(-I * (th - ph) / 2),
            sp.exp(I * (th - ph) / 2))
check('A2', zero(W.H * TOR * W - D) and zero(TOR * CN - CN * TOR), 'torus diagonal in B; commutes with CNOT')


def C1(gg):
    return (k0p + sp.exp(I * gg) * k1m) / sq2


def C2(gg):
    return (k0m + sp.exp(I * gg) * k1p) / sq2


def on_circles(vec):
    b = sp.simplify(W.H * vec)
    w = [sp.simplify(sp.expand(b[i] * sp.conjugate(b[i]))) for i in range(4)]
    on1 = w[2] == 0 and w[3] == 0 and w[0] == sp.Rational(1, 2) and w[1] == sp.Rational(1, 2)
    on2 = w[0] == 0 and w[1] == 0 and w[2] == sp.Rational(1, 2) and w[3] == sp.Rational(1, 2)
    return on1 or on2, b


okA3 = True
for circ in (C1, C2):
    v = circ(g)
    for U in (TOR, CN, ZI, IZ):
        okA3 &= on_circles(U * v)[0]
    okA3 &= on_circles(v.conjugate())[0]
b1 = on_circles(TOR * C1(g))[1]
b2 = on_circles(TOR * C2(g))[1]
rel1 = sp.simplify(b1[1] / b1[0] * sp.exp(-I * g))
rel2 = sp.simplify(b2[3] / b2[2] * sp.exp(-I * g))
okA3 &= sp.simplify(rel1 - sp.exp(I * (th + ph))) == 0 and sp.simplify(rel2 - sp.exp(I * (th - ph))) == 0
check('A3', okA3, 'generators map C1 u C2 into itself; torus shifts gamma by th+ph on C1, th-ph on C2')


def det2(vec):
    return vec[0] * vec[3] - vec[1] * vec[2]


okA4 = True
for circ in (C1, C2):
    for vv in (circ(g), CN * circ(g)):
        d = det2(vv)
        okA4 &= sp.simplify(sp.expand(d * sp.conjugate(d))) == sp.Rational(1, 4)
check('A4', okA4, '|det|^2 = 1/4 for C_k(gamma) and CNOT C_k(gamma): maximally entangled')

okA5 = True
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
targets = {(1, 1): C1(0), (-1, -1): C1(sp.pi), (1, -1): C2(0), (-1, 1): C2(sp.pi)}
for s in SS:
    ps = ket(1, s[0] * s[1], s[0], -s[1]) / 2
    ov = (targets[s].H * ps)[0]
    okA5 &= sp.simplify(ov * sp.conjugate(ov)) == 1
check('A5', okA5, 'psi_(1,1) = C1(0), psi_(-1,-1) = C1(pi), psi_(1,-1) = C2(0), psi_(-1,1) = C2(pi) (rays)')

print('== A6  Bell-type seeds: orbit invariants in the product basis (|0+>, |0->, |1+>, |1->)')
c00, c01, c10, c11 = sp.symbols('c00 c01 c10 c11')
PB = sp.Matrix.hstack(k0p, k0m, k1p, k1m)       # product basis |a>_Z |b>_X, b = 0 <-> +
cvec = sp.Matrix([c00, c01, c10, c11])


def AB(U, anti=False):
    v = PB * cvec
    v = U * (v.conjugate() if anti else v)
    c = sp.expand(PB.H * v)
    return sp.expand(c[0] * c[3]), sp.expand(c[1] * c[2])


A0, B0 = sp.expand(c00 * c11), sp.expand(c01 * c10)
okA6 = True
At, Bt = AB(TOR)
okA6 &= sp.simplify(At - A0) == 0 and sp.simplify(Bt - B0) == 0
Ac, Bc = AB(CN)
okA6 &= sp.simplify(Ac + A0) == 0 and sp.simplify(Bc - B0) == 0
Az, Bz = AB(ZI)
okA6 &= sp.simplify(Az + A0) == 0 and sp.simplify(Bz + B0) == 0
Ai, Bi = AB(IZ)
okA6 &= sp.simplify(Ai - B0) == 0 and sp.simplify(Bi - A0) == 0
Aa, Ba = AB(sp.eye(4), anti=True)
okA6 &= sp.simplify(Aa - sp.conjugate(A0)) == 0 and sp.simplify(Ba - sp.conjugate(B0)) == 0
Asy, Bsy = sp.symbols('A B')
okA6 &= sp.expand((Asy - Bsy) * sp.conjugate(Asy - Bsy) + (Asy + Bsy) * sp.conjugate(Asy + Bsy)
                  - 2 * (Asy * sp.conjugate(Asy) + Bsy * sp.conjugate(Bsy))) == 0
detP = sp.expand(c00 * c11 - c01 * c10)
okA6 &= sp.expand(detP - (A0 - B0)) == 0
check('A6', okA6, 'torus fixes (A,B); CNOT (-A,B); ZI (-A,-B); IZ (B,A); T conj; parallelogram identity; '
      'det = A - B in the product basis')

print('== A7  the group S2 = <T2c, G16>: identity component and component group')


def mod_phase_key(U):
    Ub = sp.simplify(W.H * U * W)
    for e in Ub:
        if e != 0:
            return tuple(sp.nsimplify(sp.simplify(x / e)) for x in Ub)
    return None


units, frontier = {mod_phase_key(sp.eye(4)): sp.eye(4)}, [sp.eye(4)]
while frontier:
    nxt = []
    for U in frontier:
        for G in (CN, ZI, IZ):
            V = sp.simplify(G * U)
            k = mod_phase_key(V)
            if k not in units:
                units[k] = V
                nxt.append(V)
    frontier = nxt


def in_torus(U):
    Ub = sp.simplify(W.H * U * W)
    diag = all(Ub[i, j] == 0 for i in range(4) for j in range(4) if i != j)
    return diag and sp.simplify(Ub[0, 0] * Ub[1, 1] - Ub[2, 2] * Ub[3, 3]) == 0


inT = [k for k, U in units.items() if in_torus(U)]
okA7 = len(units) == 8 and len(inT) == 2 and in_torus(ZI) and in_torus(sp.eye(4)) and in_torus(TOR)
check('A7', okA7, f'unitary part of G16: {len(units)} elements mod phase; in the torus: {len(inT)} (I, Z(x)I); '
      'component group of S2 has order 16/2 = 8')

print('== A8  the larger torus T3 (all B-diagonal unitaries)')
ZX = sp.kronecker_product(sz, sx)
EZX = W * sp.diag(sp.exp(I * chi), sp.exp(I * chi), sp.exp(-I * chi), sp.exp(-I * chi)) * W.H
okA8 = zero(W.H * ZX * W - sp.diag(1, 1, -1, -1))
okA8 &= on_circles(EZX * C1(g))[0] and on_circles(EZX * C2(g))[0]
b = on_circles(EZX * C1(g))[1]
okA8 &= sp.simplify(b[1] / b[0] - sp.exp(I * g)) == 0
check('A8', okA8, 'Z(x)X = diag(1,1,-1,-1) in B; e^{i chi Z(x)X} fixes each circle pointwise (rays)')

print('== CC countercontrols (each must be REJECTED)')
phip = ket(1, 0, 0, 1) / sq2
d1, d2 = det2(phip), det2(CN * phip)
rej1 = bool(sp.simplify(d1 * sp.conjugate(d1)) == sp.Rational(1, 4) and sp.simplify(d2 * sp.conjugate(d2)) == 0)
print(f"CC1   {'REJECTED' if rej1 else 'NOT REJECTED'}  Phi+: |det|^2 = 1/4 but CNOT Phi+ has |det|^2 = 0")
HI = sp.kronecker_product(sp.Matrix([[1, 1], [1, -1]]) / sq2, s0)
rej2 = not on_circles(HI * C1(0))[0]
print(f"CC2   {'REJECTED' if rej2 else 'NOT REJECTED'}  Ad(H(x)I) C1(0) leaves C1 u C2")
rej3 = not in_torus(CN)
print(f"CC3   {'REJECTED' if rej3 else 'NOT REJECTED'}  CNOT not in the torus T2c (d1 d2 = -1, d3 d4 = 1)")

allok = all(ok for _, ok in results) and rej1 and rej2 and rej3
print(f"SUMMARY checks {sum(ok for _, ok in results)}/{len(results)} PASS; countercontrols rejected "
      f"{int(rej1) + int(rej2) + int(rej3)}/3")
print('VERDICT S2-STRUCT-EXACT' if allok else 'VERDICT S2-STRUCT-FAILED')
