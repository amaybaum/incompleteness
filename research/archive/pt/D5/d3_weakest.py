# d3_weakest.py -- thread D5, stage 5: the field-neutral counterpart of "substratum class + one drive".
# Run: python3 -I -B d3_weakest.py from pt/D5/.  Exact (integer/rational sympy matrices).  Reads (read-only)
# CompositeDimension.lean at L for cnot's sgn/pc/pt.
#
# Objects: on the 16-dim table space W 3 (row-major vec), the actC / actT generators of the rotation generators
# L_x (drive about the NOT axis x: nflip = R_x(pi)) and L_z (the substratum class's phase flow about the corner
# axis z, the monomial diag(1, e^{i phi})), and the cnot signed permutation C.  Lie closure = real span closed
# under commutators.
# DECISION RULES (fixed before the first run): PASS/FAIL per line; countercontrols (ids ending 'c') PASS when the
# closure is NOT of dimension 6.  VERDICT only if every line is PASS, else NO VERDICT.
#   W1   closure{actC L_x, actC L_z, C actC L_x C, C actC L_z C} has dimension 6 (= su(2)+su(2), the S4 algebra).
#   W1c  closure{actC L_z, C actC L_z C} (the phase flow alone on the control): dimension < 6.
#   W2c  closure{actC L_x, C actC L_x C} (the drive alone on the control): dimension < 6.
#   W3c  closure{actC L_z, actT L_z, C-conjugates} (phase flows of the substratum class on both tokens): < 6.
#   W4   closure{actT L_x, actT L_z, C-conjugates} (drive and phase on the target): dimension 6.
import re
from sympy import Matrix, zeros, eye, kronecker_product as kron
lines = []
def rep(ok, cid, msg=''):
    lines.append(('PASS' if ok else 'FAIL') + ' ' + cid + ((' ' + msg) if msg else ''))
    print(lines[-1])
cd = open('../base/verification/lean-mathlib/OIBridge/CompositeDimension.lean').read()
def parse_tab(name):
    m = re.search(r'def ' + name + r' : Fin 4 → Fin 4 → Fin 4\n(.*?)\n\n', cd, re.S)
    return {(int(a), int(b)): int(c) for a, b, c in re.findall(r'\| (\d), (\d) => (\d)', m.group(1))}
PC = parse_tab('pc'); PT = parse_tab('pt')
msg = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1', cd)
neg = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))}
C = zeros(16, 16)
for a in range(4):
    for b in range(4):
        C[4 * a + b, 4 * PC[(a, b)] + PT[(a, b)]] = -1 if (a, b) in neg else 1
def H0(L):
    M = zeros(4, 4)
    for i in range(3):
        for j in range(3):
            M[i + 1, j + 1] = L[i, j]
    return M
Lx = Matrix([[0, 0, 0], [0, 0, -1], [0, 1, 0]]); Lz = Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 0]])
def gC(L): return kron(H0(L), eye(4))
def gT(L): return kron(eye(4), H0(L))
def closure(gens):
    basis = []
    def add(M):
        if Matrix([list(B) for B in basis + [M]]).rank() > len(basis):
            basis.append(M); return True
        return False
    for g in gens: add(g)
    changed = True
    while changed:
        changed = False
        for A in list(basis):
            for B in list(basis):
                if add(A * B - B * A): changed = True
    return len(basis)
rep(C * C == eye(16), 'W0', 'cnot (parsed) is an involution on the table space')
d1 = closure([gC(Lx), gC(Lz), C * gC(Lx) * C, C * gC(Lz) * C])
rep(d1 == 6, 'W1', 'drive (about x) + substratum phase flow (about z), both on the control, with cnot: dim %d' % d1)
d2 = closure([gC(Lz), C * gC(Lz) * C])
rep(d2 < 6, 'W1c', 'phase flow alone on the control with cnot: dim %d' % d2)
d3 = closure([gC(Lx), C * gC(Lx) * C])
rep(d3 < 6, 'W2c', 'drive alone on the control with cnot: dim %d' % d3)
d4 = closure([gC(Lz), gT(Lz), C * gC(Lz) * C, C * gT(Lz) * C])
rep(d4 < 6, 'W3c', 'substratum phase flows on both tokens with cnot: dim %d' % d4)
d5 = closure([gT(Lx), gT(Lz), C * gT(Lx) * C, C * gT(Lz) * C])
rep(d5 == 6, 'W4', 'drive + phase flow on the target with cnot: dim %d' % d5)
nf = sum(1 for l in lines if l.startswith('FAIL'))
print('SUMMARY %d lines, %d FAIL' % (len(lines), nf))
print('VERDICT D3-WEAKEST-EXACT: (b) for the drive together with the substratum phase flow on one token generates '
      'su(2)+su(2) with cnot; each alone, and the phase flows on both tokens, do not' if nf == 0 else 'NO VERDICT')
