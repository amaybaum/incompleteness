"""p6_r3rev_ghz_chsh -- independent r3 reviewer probe for QX-6 sec. 2 (no p1-p5 imports). Exact (sympy).
(1) GHZ-1: <XXX>, <XYY>, <YXY>, <YYX>; Mermin value 4; local max over 64 assignments.
(2) GHZ-1 X/Z content: every X/Z/I Pauli string with nonzero expectation, and the local assignment x=z=+1.
(3) GHZ-2: triangle graph state; <XZZ>,<ZXZ>,<ZZX>,<XXX>; value 4; local max over 64 assignments; realness.
(4) local-Clifford map (SH (x) SH (x) SHS)|GHZ> = e^{i pi/4}|triangle>, operators right to left; also the
    other readings of 'SH' to show the convention matters.
(5) CHSH: |Phi+> with A0=Z, A1=X, B=(Z+-X)/sqrt2 -> E=(-1)^{xy}/sqrt2, S=2sqrt2; the pi/3 comparator S=5/2
    and its TLM boundary status (exact); all 60 two-qubit stabilizer states with signed Pauli settings: max |S|.
"""
import itertools
import sympy as sp

I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2); S = sp.Matrix([[1, 0], [0, sp.I]])
P = {'I': I2, 'X': X, 'Y': Y, 'Z': Z}
def kron(*ms):
    out = ms[0]
    for m in ms[1:]: out = sp.Matrix(sp.kronecker_product(out, m))
    return out
def ket(bits):
    v = sp.zeros(2 ** len(bits), 1); v[int(bits, 2)] = 1; return v
def ev(psi, s):
    return sp.simplify((psi.H * kron(*[P[c] for c in s]) * psi)[0])

ghz = (ket('000') + ket('111')) / sp.sqrt(2)
vals = {s: ev(ghz, s) for s in ('XXX', 'XYY', 'YXY', 'YYX')}
M1 = vals['XXX'] - vals['XYY'] - vals['YXY'] - vals['YYX']
loc1 = max(x[0]*x[1]*x[2] - x[0]*y[1]*y[2] - y[0]*x[1]*y[2] - y[0]*y[1]*x[2]
           for x in itertools.product((1, -1), repeat=3) for y in itertools.product((1, -1), repeat=3))
print('(1) GHZ-1:', vals, 'value', M1, 'local max', loc1)
assert M1 == 4 and loc1 == 2

nz = {}
for s in itertools.product('IXZ', repeat=3):
    s = ''.join(s); e = ev(ghz, s)
    if e != 0 and s != 'III': nz[s] = e
sat = all(e == 1 for e in nz.values())   # assignment x_i = z_i = +1 gives product +1 for each string
print('(2) GHZ-1 X/Z strings with nonzero expectation:', nz, '; all +1 so x=z=+1 satisfies them:', sat)
assert set(nz) == {'XXX', 'ZZI', 'IZZ', 'ZIZ'} and sat

plus = (ket('0') + ket('1')) / sp.sqrt(2)
CZ = lambda i, j: sp.diag(*[(-1) ** (int(f'{k:03b}'[i]) * int(f'{k:03b}'[j])) for k in range(8)])
tri = CZ(0, 1) * CZ(0, 2) * CZ(1, 2) * kron(plus, plus, plus)
v2 = {s: ev(tri, s) for s in ('XZZ', 'ZXZ', 'ZZX', 'XXX')}
M2 = v2['XZZ'] + v2['ZXZ'] + v2['ZZX'] - v2['XXX']
loc2 = max(x[0]*z[1]*z[2] + z[0]*x[1]*z[2] + z[0]*z[1]*x[2] - x[0]*x[1]*x[2]
           for x in itertools.product((1, -1), repeat=3) for z in itertools.product((1, -1), repeat=3))
print('(3) GHZ-2 triangle:', v2, 'value', M2, 'local max', loc2, '; real amplitudes:', all(sp.im(a) == 0 for a in tri))
assert M2 == 4 and loc2 == 2

U = kron(S * H, S * H, S * H * S)
lhs = sp.simplify(U * ghz); rhs = sp.simplify(((1 + sp.I) / sp.sqrt(2)) * tri)   # e^{i pi/4}
diff = (lhs - rhs).applyfunc(lambda e: sp.simplify(sp.expand_complex(e)))
print('(4) (SH x SH x SHS)|GHZ> - e^{i pi/4}|tri> =', diff.T)
assert diff == sp.zeros(8, 1)
# other reading (left to right: H after S): HS x HS x SHS
U2 = kron(H * S, H * S, S * H * S); l2 = sp.simplify(U2 * ghz)
ph = [sp.simplify(sp.expand_complex(l2[k] / tri[k])) for k in range(8) if tri[k] != 0]
print('    with HS (S first) instead: proportional to |tri>?', len(set(ph)) == 1)

# (5) CHSH
phi = (ket('00') + ket('11')) / sp.sqrt(2)
A = [Z, X]; B = [(Z + X) / sp.sqrt(2), (Z - X) / sp.sqrt(2)]
E = {(x, y): sp.simplify((phi.H * kron(A[x], B[y]) * phi)[0]) for x in (0, 1) for y in (0, 1)}
Sv = sp.simplify(E[0, 0] + E[0, 1] + E[1, 0] - E[1, 1])
print('(5) |Phi+> correlators', E, 'S =', Sv)
Ec = {(0, 0): sp.Rational(1, 2), (0, 1): sp.Rational(1, 2), (1, 0): sp.Rational(1, 2), (1, 1): -1}
lhsT = abs(Ec[0, 0] * Ec[0, 1] - Ec[1, 0] * Ec[1, 1])
rhsT = sp.sqrt((1 - Ec[0, 0] ** 2) * (1 - Ec[0, 1] ** 2)) + sp.sqrt((1 - Ec[1, 0] ** 2) * (1 - Ec[1, 1] ** 2))
print('    pi/3 comparator: S =', Ec[0, 0] + Ec[0, 1] + Ec[1, 0] - Ec[1, 1], '; TLM lhs, rhs =', lhsT, rhsT)
# stabilizer states: orbit of |00> under 2-qubit Clifford generators (exact, up to global phase)
gens = [kron(H, I2), kron(I2, H), kron(S, I2), kron(I2, S),
        sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])]
def canon(v):
    v = sp.simplify(v)
    k = next(i for i in range(4) if v[i] != 0)
    return tuple(sp.nsimplify(sp.simplify(v[i] / v[k])) for i in range(4))
start = ket('00'); seen = {canon(start): start}; frontier = [start]
while frontier:
    nxt = []
    for v in frontier:
        for g in gens:
            w = sp.simplify(g * v); c = canon(w)
            if c not in seen: seen[c] = w; nxt.append(w)
    frontier = nxt
states = list(seen.values())
paul = []
for p in 'XYZ':
    for sgn in (1, -1): paul.append(sgn * P[p])
best = 0
for psi in states:
    T = [[sp.simplify((psi.H * kron(a, bb) * psi)[0]) for bb in paul] for a in paul]
    for a0, a1, b0, b1 in itertools.product(range(6), repeat=4):
        s_ = T[a0][b0] + T[a0][b1] + T[a1][b0] - T[a1][b1]
        best = max(best, abs(s_))
print('    two-qubit stabilizer states:', len(states), '; max |S| over signed Pauli settings:', best)
assert len(states) == 60 and best == 2
print('GHZ/CHSH PROBE DONE')
