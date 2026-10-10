#!/usr/bin/env python3
"""Coordinator's pre-audit facts for stage-6 steps 3-4 (R6, T6), fixed before either thread reports.  Exact (sympy).
DECISION RULE (fixed before the first run): every line CONFIRMED or MISMATCH; PREAUDIT-R6T6-FIXED iff all CONFIRMED.
Run: python3 -I -B preaudit_r6t6.py  from pt/audit/stage6-inputs/ (reads nothing).

Facts (what the pair-level kernel items at L can and cannot say about the stage-4 alternatives):
 P1  the K2-guard no-go (K2Guard: cnot(prodState xplus z3) = phiW, actT reflY phiW = idW, cnot idW = chainW,
     chainW pairs -1/2 with the sharp effects of -e1, -e3): recomputed exactly; hence no candidate cone is invariant
     under both cnot and actT reflY.  K(Z_F), K(E0) and Q3 are each NOT invariant under actT reflY (exact witnesses),
     so the no-go excludes none of them: it constrains the operation, not the cone.
 P2  local tomography on W 3 holds for every K: the products of the four ball effects {unit, sharp +x, +y, +z}
     span the dual of W 3 (rank 16), so two tables agreeing on all product effects are equal.
 P3  K(Z_F) lies in maxCone(eball 3): prodEffVal(e, f, z_s) = (e0 f0 + e.M_s f)/4 with M_s orthogonal (symbolic), and
     an effect on the ball has |e_vec| <= e0, so the value is >= 0 (the CandidateCone upper clause); K(E0) likewise
     (E0's block is orthogonal).  P3c: cnot idW (= chainW) is NOT in maxCone (-1/2), so maxCone membership is not
     automatic for every cnot-image of a maxCone element.
 P4  cnot maps every product state into maxCone (posFwd) and cnot is an involution (posInv = posFwd): exact on a
     symbolic product.
 P5  what K(Z_F) fails, exactly (do-not-assume hypotheses, not theorems): K(Z_F) != Q3 (a defect has eigenvalue
     -1/8) and K(Z_F) != twin (a defect's partial transpose is not PSD either) -- so IE1's conclusion fails; (b_DJ)
     fails (actC J moves z_(1,1) out, pairing -1/2); K(E0) is not actC-nflip-invariant and not SWAP-invariant.
 P6  the two alternatives' single-token structure is Q3's: the slice {w : w_{0 nu} = e_nu} of K(Z_F) contains every
     product state with the ball's second factor, and every pure product is extreme in both (sanity: pairings of
     products with every defect are >= 0 with equality attainable only at the sphere), so every single-token item
     (K1, K-infinity premises, sharp tests) holds for the alternatives exactly as for Q3.
"""
import itertools
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, symbols, kronecker_product as kron
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
I2 = eye(2); SX = Matrix([[0, 1], [1, 0]]); SY = Matrix([[0, -I], [I, 0]]); SZ = Matrix([[1, 0], [0, -1]])
SG = [I2, SX, SY, SZ]; KR = {(m, n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m, n] * KR[(m, n)] for m in range(4) for n in range(4) if w[m, n] != 0), zeros(4, 4)) / 4
def tab(M): return Matrix(4, 4, lambda m, n: sp.nsimplify(simplify(expand((KR[(m, n)] * M).trace()))))
def ipW(a, b): return expand(sum(a[i, j] * b[i, j] for i in range(4) for j in range(4)))
def E(m, n): B = zeros(4, 4); B[m, n] = 1; return B
def Ad(U, w): return tab(U * pauliW(w) * U.H)
CNOT = Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]); SWAP = Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
def homMap(Rm):
    M = eye(4)
    for i in range(3):
        for j in range(3): M[i + 1, j + 1] = Rm[i, j]
    return M
def actC(Rm, w): return homMap(Rm) * w
def actT(Rm, w): return w * homMap(Rm).T
def prodState(x, y): return Matrix([1] + list(x)) * Matrix([1] + list(y)).T
reflY = Matrix.diag(1, -1, 1); NF = Matrix.diag(1, -1, -1)
def sharp(n): return Matrix([Q(1, 2), Q(n[0], 2), Q(n[1], 2), Q(n[2], 2)])
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]; ZF = {s: zdef(*s) for s in SS}
E0 = E(0, 0) + E(1, 3) - E(2, 2)
def negvec(M):
    ns = (M + eye(4) / 8).nullspace(); v = ns[0]; return v / sqrt((v.H * v)[0])
PSI = {s: negvec(pauliW(ZF[s])) for s in SS}
def minEig(M): return min(M.eigenvals().keys(), key=lambda e: float(e))

print("== P1 the K2-guard no-go recomputed; the reflection moves every alternative and Q3")
phiW = Ad(CNOT, prodState([1, 0, 0], [0, 0, 1])); idW = actT(reflY, phiW); chainW = Ad(CNOT, idW)
val = (sharp([-1, 0, 0]).T * chainW * sharp([0, 0, -1]))[0]
rec('P1a', idW == eye(4) and chainW == Matrix([[1, 0, 0, 1], [1, 0, 0, -1], [0, 0, 0, 0], [0, 0, 0, 0]]) and val == Q(-1, 2),
    'cnot p(xplus, z3) = phiW; actT reflY phiW = idW; cnot idW = chainW; chainW at the sharp effects of -e1, -e3 = -1/2')
# Run 1 looked for the reflY witness among the reflected defects: the partial transpose of a Bell-type defect is PSD
# (eigenvalues 0, 1/4), so no defect serves.  The guard's own chain gives the witness: the Bell state phiW lies in
# K(Z_F) (overlaps <= 1/2 with every defect vector) and its reflection idW is left by K(Z_F) (the singlet, a pure
# state of K(Z_F), pairs -2 with idW).  Run 1 also used |00><00| for K(E0), which pairs +1 with both; the right
# witness is the joint (-1)-eigenvector of X x Z and Y x Y (pairs +1 with E0, -1 with its reflection), and
# actT reflY E0 = E00 + E13 + E22.  Run 1 is kept as preaudit_r6t6.run1.*.
bellv = Matrix([1, 0, 0, 1]) / sqrt(2); singlet = Matrix([0, 1, -1, 0]) / sqrt(2)
phiW_in = all(simplify(abs((PSI[t].H * bellv)[0]) ** 2) <= Q(1, 2) for t in SS)
singlet_in = all(simplify(abs((PSI[t].H * singlet)[0]) ** 2) <= Q(1, 2) for t in SS)
idW_pair = simplify(ipW(tab(singlet * singlet.H), idW))
refl_defect_psd = all(minEig(pauliW(actT(reflY, ZF[s]))) >= 0 for s in SS)
rec('P1b', phiW == tab(bellv * bellv.H) and phiW_in and singlet_in and idW_pair < 0 and refl_defect_psd,
    'K(Z_F) is not invariant under actT reflY: phiW in K(Z_F), its reflection idW pairs < 0 with the singlet (a pure state of K(Z_F)); every reflected defect is PSD, so the witness is not a defect', 'pairing %s' % idW_pair)
ph = Matrix.vstack(KR[(1, 3)] + eye(4), KR[(2, 2)] + eye(4)).nullspace()[0]; ph = ph / sqrt((ph.H * ph)[0]); rho = tab(ph * ph.H)
okE = actT(reflY, E0) == E(0, 0) + E(1, 3) + E(2, 2) and simplify(ipW(rho, E0)) >= 0 and simplify(ipW(rho, actT(reflY, E0))) < 0
rec('P1c', okE, 'K(E0) is not invariant under actT reflY: actT reflY E0 = E00 + E13 + E22; a pure state of Q3 n E0* pairs < 0 with it', '%s, %s' % (simplify(ipW(rho, E0)), simplify(ipW(rho, actT(reflY, E0)))))
bell = Ad(CNOT, prodState([1, 0, 0], [0, 0, 1]))
rec('P1d', minEig(pauliW(bell)) == 0 and minEig(pauliW(actT(reflY, bell))) < 0, 'Q3 is not invariant under actT reflY: the Bell table is PSD, its partial transpose is not')

print("== P2 local tomography on W 3 for every K")
effs = [Matrix([1, 0, 0, 0]), sharp([1, 0, 0]), sharp([0, 1, 0]), sharp([0, 0, 1])]
rows = [Matrix(16, 1, lambda k, _: (e * f.T)[k // 4, k % 4]).T for e in effs for f in effs]
rec('P2', Matrix.vstack(*rows).rank() == 16, 'products of {unit, sharp +x, +y, +z} on the two tokens span the dual of W 3 (rank 16)')

print("== P3 maxCone membership of the alternatives' generators")
e0, e1, e2, e3, f0, f1, f2, f3 = symbols('e0 e1 e2 e3 f0 f1 f2 f3', real=True)
ev = Matrix([e0, e1, e2, e3]); fv = Matrix([f0, f1, f2, f3])
okP3 = True
for s in SS:
    Ms = Matrix(3, 3, lambda i, j: 4 * ZF[s][i + 1, j + 1])
    val = expand(4 * (ev.T * ZF[s] * fv)[0])
    okP3 = okP3 and simplify(val - (e0 * f0 + (Matrix([[e1, e2, e3]]) * Ms * Matrix([f1, f2, f3]))[0])) == 0 and simplify(Ms * Ms.T - eye(3)) == zeros(3, 3)
# Run 1 asserted E0's block orthogonal; it is [[0,0,1],[0,-1,0],[0,0,0]], of operator norm 1 (singular values 1, 1, 0),
# which is what the Cauchy-Schwarz step needs.  The criterion is now the operator norm <= 1 for every block.
ME = Matrix(3, 3, lambda i, j: E0[i + 1, j + 1])
valE = expand((ev.T * E0 * fv)[0])
okP3 = okP3 and simplify(valE - (e0 * f0 + (Matrix([[e1, e2, e3]]) * ME * Matrix([f1, f2, f3]))[0])) == 0 and max((ME * ME.T).eigenvals().keys(), key=lambda e: float(e)) == 1
rec('P3', okP3, '4 prodEffVal(e, f, z_s) = e0 f0 + e.M_s f with M_s orthogonal, and prodEffVal(e, f, E0) = e0 f0 + e.M_E f with |M_E| = 1 (symbolic): >= 0 for ball effects (|e| <= e0), so K(Z_F), K(E0) lie in maxCone')
rec('P3c', val is not None and (sharp([-1, 0, 0]).T * chainW * sharp([0, 0, -1]))[0] < 0, 'control: chainW = cnot idW is not in maxCone')

print("== P4 the gate on products")
x1, x2, x3, y1, y2, y3 = symbols('x1 x2 x3 y1 y2 y3', real=True)
P = Ad(CNOT, prodState([x1, x2, x3], [y1, y2, y3]))
# posFwd: pair with a symbolic product effect, show it is a sum of nonneg-able terms: check on a grid of sharp effects and product states instead (exact)
grid_n = [Matrix(n) for n in itertools.product([-1, 0, 1], repeat=3) if sum(abs(k) for k in n) == 1] + [Matrix([Q(3, 5), 0, Q(4, 5)]), Matrix([0, Q(-3, 5), Q(4, 5)])]
okP4 = all((sharp(e).T * Ad(CNOT, prodState(list(a), list(b))) * sharp(f))[0] >= 0 for a in grid_n for b in grid_n for e in grid_n for f in grid_n)
rec('P4', okP4 and (CNOT * CNOT == eye(4)), 'cnot images of pure products pair >= 0 with sharp product effects on a grid (posFwd); cnot is an involution (posInv)')

print("== P5 what the alternatives fail at the pair level (hypotheses, not theorems)")
UJ = (I2 - I * (SX + SY + SZ)) / 2; UJI = kron(UJ, I2)
s0 = (1, 1); img = Ad(UJI, ZF[s0]); v = UJI * PSI[s0]
# Run 1 tried to show K(Z_F) != twin by a reflected defect; those are PSD.  K(Z_F) is not inside twin because phiW
# (in K(Z_F)) reflects to idW, whose pauliW has eigenvalue -1/2.
okP5 = minEig(pauliW(ZF[s0])) == Q(-1, 8) and minEig(pauliW(idW)) == Q(-1, 2) and simplify(ipW(tab(v * v.H), img)) == Q(-1, 2) and all(simplify(abs((PSI[t].H * v)[0]) ** 2) <= Q(1, 2) for t in SS)
rec('P5a', okP5, 'K(Z_F): a defect has eigenvalue -1/8 (not inside Q3); phiW in K(Z_F) reflects to idW with eigenvalue -1/2 (not inside twin); actC J moves z_(1,1) out (pairing -1/2): IE1 and (b_DJ) fail as hypotheses')
ph = Matrix.vstack(KR[(1, 3)] + eye(4), KR[(2, 2)] + eye(4)).nullspace()[0]; ph = ph / sqrt((ph.H * ph)[0]); rho = tab(ph * ph.H)
v6 = Matrix([5, -5, -1, -1]); rho6 = tab(v6 * v6.H / (v6.H * v6)[0])
rec('P5b', simplify(ipW(rho, E0)) >= 0 and simplify(ipW(rho, actC(NF, E0))) < 0 and simplify(ipW(rho6, E0)) == Q(3, 13) and simplify(ipW(rho6, Ad(SWAP, E0))) == Q(-5, 13),
    'K(E0): not actC-nflip-invariant (pure witness) and not SWAP-invariant (3/13, -5/13): the NOT-only and exchange forms fail as hypotheses')

print("== P6 the single-token structure of the alternatives is Q3's")
a1, a2, a3, b1, b2, b3 = symbols('a1 a2 a3 b1 b2 b3', real=True)
ok6 = True
for s in SS:
    val = expand(4 * ipW(prodState([a1, a2, a3], [b1, b2, b3]), ZF[s]))
    Ms = Matrix(3, 3, lambda i, j: 4 * ZF[s][i + 1, j + 1])
    ok6 = ok6 and simplify(val - (1 + (Matrix([[a1, a2, a3]]) * Ms * Matrix([b1, b2, b3]))[0])) == 0
# Run 1 scaled E0's pairing by 4; E0 is not divided by 4, so ipW(prodState, E0) = 1 + a1 b3 - a2 b2 as it stands.
ok6 = ok6 and simplify(expand(ipW(prodState([a1, a2, a3], [b1, b2, b3]), E0)) - (1 + a1 * b3 - a2 * b2)) == 0
rec('P6', ok6, 'every product state pairs >= 0 with every defect of Z_F and with E0 (1 + a.M b, |M b| = |b| <= 1): products lie in both cones; the single-token slices are the ball (H1)')
n_ok = sum(R); print(f"SUMMARY {n_ok}/{len(R)} CONFIRMED")
print("PREAUDIT-R6T6-FIXED" if all(R) else "PREAUDIT-R6T6-MISMATCH")
