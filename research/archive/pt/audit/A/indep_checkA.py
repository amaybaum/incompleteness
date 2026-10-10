"""Coordinator's independent check of thread A's numerical claims (audit; exact arithmetic).

Written from the landed definitions (verification/lean/kt4_prem1_probe.py conventions, re-typed here; no code
from pt/A/ is imported or copied). Decision rule, fixed before the first run: each claim below is CONFIRMED iff
its exact check holds; any failed check prints MISMATCH with the values. No timing in stdout.

Claims audited (thread A RESULT.md):
  C1  T_psi = actT RH phiW is a normalized rank-one PSD state (in Q3).
  C2  F = E00/2 - T_psi/4 satisfies ipW(F, T_psi) = -1/2.
  C3  F is nonnegative on every product state and on every cnot image of a product state over the closed
      unit ball (so F in dualW(K_gen)); proved here by an exact reduction: the pairing is
      1/2 - (1/4) * hom(x)^T B hom(y) with B computed exactly, and the bound hom(x)^T B hom(y) <= 2 is
      shown via the explicit decomposition of B (printed) and the Cauchy-Schwarz step stated in the output.
  C4  famI(phiW, phiW, T_psi/4, F) = -1/8 (phiW in K_gen; T_psi/4 in dualW(K_gen) since T_psi in Q3 = dualW(Q3)
      contains dualW... i.e. T_psi is nonnegative on K_gen because K_gen is inside Q3).
  C5  closing products under N = actT reflY o cnot reaches chainW, whose value at the sharp effects of
      -e1, -e3 is -1/2 (invalid table).
  C6  ipW(actT R0 F, cnot(prodState(-e2, e2))) = -2/5 and famI(F, phiW, cnot prodState(e2,-e3),
      cnot prodState(e2,e2)) = -1/2.
Countercontrols: C2' ipW(E00/2 + T_psi/4, T_psi) must be positive; C4' famI with E = phiW/4 (in Q3) in place of F
must be nonnegative.
"""
import sympy as sp
from itertools import product

Q = sp.Rational
R4 = range(4)
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
NEG = {(1, 3), (2, 2)}


def cnot(w):
    return sp.Matrix(4, 4, lambda m, n: (-1 if (m, n) in NEG else 1) * w[PC[m][n], PT[m][n]])


def hom(x):
    return sp.Matrix([1] + list(x))


def homMap(R):
    M = sp.zeros(4, 4)
    M[0, 0] = 1
    M[1:4, 1:4] = R
    return M


def actT(R, w):
    return w * homMap(R).T


def prodState(x, y):
    return hom(x) * hom(y).T


def ipW(E, X):
    return sp.expand(sum(E[m, n] * X[m, n] for m in R4 for n in R4))


def famI(X, Y, E, F):
    return sp.expand(sum(X[a, b] * Y[c, d] * E[a, c] * F[b, d] for a, b, c, d in product(R4, repeat=4)))


S = [sp.eye(2), sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]


def kron(A, B):
    return sp.kronecker_product(A, B)


def pauliW(w):  # landed dictionary: rho = (1/4) sum w_{mn} S_m (x) S_n
    return sum((w[m, n] * kron(S[m], S[n]) for m in R4 for n in R4), sp.zeros(4, 4)) / 4


ok_all = True


def report(cid, ok, detail):
    global ok_all
    ok_all = ok_all and ok
    print(f"{'CONFIRMED' if ok else 'MISMATCH '} {cid}: {detail}")


phiW = sp.diag(1, 1, -1, 1)
RH = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
reflY = sp.diag(1, -1, 1)
E00 = prodState([0, 0, 0], [0, 0, 0])
xplus, z3 = [1, 0, 0], [0, 0, 1]

# landed identity used throughout: phiW = cnot(prodState xplus z3)
report('C0', cnot(prodState(xplus, z3)) == phiW, 'phiW = cnot(prodState xplus z3) (phiW in cnot SEP, hence in K_gen)')

Tpsi = actT(RH, phiW)
rhoT = pauliW(Tpsi)
ev = rhoT.eigenvals()
report('C1', sp.simplify(rhoT.trace() - 1) == 0 and all(sp.re(k) >= 0 and sp.im(k) == 0 for k in ev) and rhoT.rank() == 1,
       f'T_psi = {list(Tpsi)}; rho trace 1, eigenvalues {ev}, rank {rhoT.rank()}')

F = E00 / 2 - Tpsi / 4
v = ipW(F, Tpsi)
report('C2', v == Q(-1, 2), f'ipW(F, T_psi) = {v}')
vcc = ipW(E00 / 2 + Tpsi / 4, Tpsi)
report("C2'", vcc > 0, f'countercontrol ipW(E00/2 + T_psi/4, T_psi) = {vcc} (> 0)')

# C3: pairing of F with products and cnot-images of products.
xs = sp.symbols('x1:4', real=True)
ys = sp.symbols('y1:4', real=True)
P = prodState(xs, ys)
for name, state in [('product', P), ('cnot image', cnot(P))]:
    val = ipW(F, state)
    # val = 1/2 - (1/4) * hom(x)^T B hom(y); recover B exactly from the bilinear form in (hom x, hom y)
    hx, hy = hom(xs), hom(ys)
    form = sp.expand(-4 * (val - Q(1, 2)))  # = hom(x)^T B hom(y)
    Bm = sp.zeros(4, 4)
    for m in R4:
        for n in R4:
            term = form
            term = sp.diff(term, xs[m - 1]) if m else term.subs({x: 0 for x in xs})
            term = sp.diff(term, ys[n - 1]) if n else term.subs({y: 0 for y in ys})
            Bm[m, n] = sp.expand(term).subs({x: 0 for x in xs}).subs({y: 0 for y in ys})
    recon = sp.expand((hx.T * Bm * hy)[0, 0] - form)
    b00 = Bm[0, 0]
    bxy = Bm[1:4, 1:4]
    brow = Bm[0, 1:4]
    bcol = Bm[1:4, 0]
    # bound: hom(x)^T B hom(y) = b00 + brow.y + x.bcol + x^T bxy y <= b00 + |brow| + |bcol| + ||bxy||_op on the ball
    # we print the blocks; for the cases here bxy is a signed permutation (operator norm 1) and the linear parts vanish
    sv = sorted(set(sp.Abs(s) for s in (bxy.T * bxy).eigenvals()))
    lin0 = (brow == sp.zeros(1, 3)) and (bcol == sp.zeros(3, 1))
    bound = b00 + (sp.sqrt(max(sv)) if sv else 0) if lin0 else None
    ok = recon == 0 and lin0 and bound is not None and bound <= 2
    report('C3', ok, f'{name}: F-pairing = 1/2 - (1/4)(b00 + x^T M y), b00 = {b00}, linear parts zero = {lin0}, '
                     f'M^T M eigenvalues {sv} so |x^T M y| <= {sp.sqrt(max(sv)) if sv else 0} on the unit ball; '
                     f'max <= {bound} <= 2, hence pairing >= 0 (Cauchy-Schwarz)')

E4 = Tpsi / 4
vI = famI(phiW, phiW, E4, F)
report('C4', vI == Q(-1, 8), f'famI(phiW, phiW, T_psi/4, F) = {vI}')
vIc = famI(phiW, phiW, E4, phiW / 4)
report("C4'", vIc >= 0, f'countercontrol famI(phiW, phiW, T_psi/4, phiW/4) = {vIc} (>= 0)')

N = lambda w: actT(reflY, cnot(w))
w1 = N(prodState(xplus, z3))
w2 = N(w1)
chainW = sp.Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]])
sharp = lambda u: sp.Matrix([Q(1, 2)] + [-Q(1, 2) * c for c in u])  # effect vector of the sharp test toward u
negx = sharp([1, 0, 0])
negz = sharp([0, 0, 1])
vch = (negx.T * w2 * negz)[0, 0]
report('C5', w1 == sp.eye(4) and w2 == chainW and vch == Q(-1, 2),
       f'N(prod xplus z3) = idW: {w1 == sp.eye(4)}; N^2 = chainW: {w2 == chainW}; value at sharp(-e1),sharp(-e3) = {vch}')

R0 = sp.Matrix([[Q(3, 5), Q(-4, 5), 0], [Q(4, 5), Q(3, 5), 0], [0, 0, 1]])
e2, e3 = [0, 1, 0], [0, 0, 1]
m2 = [0, -1, 0]
m3 = [0, 0, -1]
v6a = ipW(actT(R0, F), cnot(prodState(m2, e2)))
v6b = famI(F, phiW, cnot(prodState(e2, m3)), cnot(prodState(e2, e2)))
report('C6', v6a == Q(-2, 5) and v6b == Q(-1, 2), f'ipW(actT R0 F, cnot prod(-e2,e2)) = {v6a}; famI(F, phiW, cnot prod(e2,-e3), cnot prod(e2,e2)) = {v6b}')

print('AUDIT-A', 'ALL CONFIRMED' if ok_all else 'MISMATCH FOUND')
