#!/usr/bin/env python3
"""Coordinator's pre-audit for T6 (stage 6, step 4), fixed before T6 reports: the exact one-token-map witnesses on
the explicit cones, recomputed with the coordinator's own table-level code (conventions of preaudit_r6t6.py; no
unitaries: rotations act on tables through homMap(R), which is orthogonal, so pairings are preserved).
Run: python3 -I -B preaudit_t6.py from pt/audit/stage6-inputs/T-audit/ (reads nothing).
DECISION RULE (fixed before the first run): per line CONFIRMED/MISMATCH; PREAUDIT-T6-FIXED iff all CONFIRMED.
 W0  the listed maps are exact rotations (R R^T = I, det 1), rational; R1 has order 3; R_n and Rx are quarter turns.
 W1  K(Z_F): actC/actT nflip and actC rot3(pi) permute the four defects (invariant), as do Ad(Z x I), Ad(I x Z)
     (phase flips) and SWAP.  Q3 control: every map preserves PSD on the Bell table and the defect images are not PSD.
 W2  K(Z_F): for g in {actC cyc3, actT cyc3, actC Rx(pi/2), actC R_n(pi/2)} the image of a defect leaves the cone
     with the exact witness pairing -1/2 (the image of the defect's own (-1/8)-eigenstate, which lies in K(Z_F)).
 W3  K(Z_F): actC R1 moves a defect out; a witness with pairing < 0 is found in the candidate set, and the best
     candidate value is printed (R6 / AUDIT-Y R7: -2383/5316 with their witnesses).
 W4  K(E0): for every listed map (actC/actT nflip, actC rot3(pi), actC/actT cyc3, actC Rx, actC R_n, actC R1) the
     image of E0 leaves K(E0): a pure state of Q3 n E0* pairs < 0 with it (value printed; R6: -1); SWAP: -5/13.
 W5  the weakest-form witness: K(Z_F) violates (b) for {flow about x, J = cyc3} on the control token (W2) and for
     {flow about x, phase flow about z} on the control token (W2 + W1: phases preserve it, the flow does not), so
     K(Z_F) is a candidate INDEPENDENCE countermodel for both weakest forms; and K(Z_F) is invariant under the
     NOT-only, phase-only and SWAP forms (W1), so it is not a countermodel for those (stage 5 forms).
"""
import itertools
import sympy as sp
from sympy import Matrix, Rational as Q, I, eye, zeros, sqrt, simplify, expand, kronecker_product as kron
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
def homMap(Rm):
    M = eye(4)
    for i in range(3):
        for j in range(3): M[i + 1, j + 1] = Rm[i, j]
    return M
def actC(Rm, w): return homMap(Rm) * w
def actT(Rm, w): return w * homMap(Rm).T
def swapW(w): return w.T
def minEig(M): return min(M.eigenvals().keys(), key=lambda e: float(e))
def isPSD(M): return minEig(M) >= 0
def zdef(s1, s2): return (E(0, 0) + s1 * E(1, 3) + s2 * E(2, 2) - s1 * s2 * E(3, 1)) / 4
SS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]; ZF = {s: zdef(*s) for s in SS}; ZL = [ZF[s] for s in SS]
E0 = E(0, 0) + E(1, 3) - E(2, 2)
def negstate(w):
    v = (pauliW(w) + eye(4) / 8).nullspace()[0]; v = v / sqrt((v.H * v)[0]); return tab(v * v.H)
PS = [negstate(z) for z in ZL]          # pure-state tables of the (-1/8)-eigenstates
# membership tests (self-duality of the explicit cones is the audited stage-3 result [A]; used only to certify
# NON-membership: y in K and <x, y> < 0 proves x not in K)
def pure_in_KZF(p): return all(simplify(ipW(p, t)) <= 2 for t in PS)         # overlap <= 1/2  <=>  ipW(p, P_t) <= 2
def pure_in_KE0(p): return simplify(ipW(p, E0)) >= 0
# rotations (rational)
cyc3 = Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])          # x->y->z->x
NF = Matrix.diag(1, -1, -1); ROT3PI = Matrix.diag(-1, -1, 1)
Rx90 = Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
def rodrigues(n, c, s):
    n = Matrix(n); K = Matrix([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return c * eye(3) + s * K + (1 - c) * n * n.T
Rn90 = rodrigues([Q(3, 5), 0, Q(4, 5)], 0, 1)
# R1: angle 2pi/3 about (5,1,1)/sqrt(27): sin * K(n/|n|) = (sqrt3/2)/sqrt27 * K(5,1,1) = K(5,1,1)/6; (1-cos) n n^T/27 = (3/2)/27 v v^T = v v^T/18
v511 = Matrix([5, 1, 1]); K511 = Matrix([[0, -1, 1], [1, 0, -5], [-1, 5, 0]])
R1 = Q(-1, 2) * eye(3) + K511 / 6 + v511 * v511.T / 18
print("== W0 the maps")
mats = {'nflip': NF, 'rot3pi': ROT3PI, 'cyc3': cyc3, 'Rx90': Rx90, 'Rn90': Rn90, 'R1': R1}
ok0 = all(simplify(M * M.T - eye(3)) == zeros(3, 3) and M.det() == 1 for M in mats.values()) and R1 ** 3 == eye(3) and R1 != eye(3) and Rx90 ** 4 == eye(3) and Rn90 ** 4 == eye(3) and Rn90 ** 2 != eye(3)
rec('W0', ok0, 'all listed maps are rational rotations; R1 has order 3; Rx(pi/2), R_n(pi/2) are quarter turns', 'R1 = %s' % R1.tolist())
print("== W1 K(Z_F) invariances")
def permutes_defects(f):
    imgs = [f(z) for z in ZL]; return all(any(img == z for z in ZL) for img in imgs) and len({tuple(img) for img in imgs}) == 4
inv_maps = {'actC nflip': lambda w: actC(NF, w), 'actT nflip': lambda w: actT(NF, w), 'actC rot3pi': lambda w: actC(ROT3PI, w),
            'Ad(Z x I)': lambda w: actC(Matrix.diag(-1, -1, 1), w), 'Ad(I x Z)': lambda w: actT(Matrix.diag(-1, -1, 1), w), 'SWAP': swapW}
inv = {k: permutes_defects(f) for k, f in inv_maps.items()}
bell = Ad = None
bellv = Matrix([1, 0, 0, 1]) / sqrt(2); BELL = tab(bellv * bellv.H)
q3ok = all(isPSD(pauliW(f(BELL))) for f in inv_maps.values()) and all(not isPSD(pauliW(f(ZL[0]))) for f in inv_maps.values())
rec('W1', all(inv.values()) and q3ok, 'K(Z_F): both NOTs, rot3(pi), the phase flips and SWAP permute the defects (invariant); Q3 control: PSD preserved, defect images not PSD', str(inv))
print("== W2 K(Z_F) leaves itself under the J/flow maps, witness -1/2")
w2 = {}
for name, f in {'actC cyc3': lambda w: actC(cyc3, w), 'actT cyc3': lambda w: actT(cyc3, w), 'actC Rx90': lambda w: actC(Rx90, w), 'actC Rn90': lambda w: actC(Rn90, w)}.items():
    best = None
    for s_i, z in enumerate(ZL):
        img = f(z); p = f(PS[s_i])       # the image of the defect's own negative eigenstate
        if pure_in_KZF(p):
            val = simplify(ipW(p, img)); best = val if best is None else min(best, val)
    w2[name] = best
rec('W2', all(v == Q(-1, 2) for v in w2.values()), 'K(Z_F): actC cyc3, actT cyc3, actC Rx(pi/2), actC R_n(pi/2) move a defect out; witness = image of its own eigenstate, pairing -1/2', str(w2))
print("== W3 K(Z_F) under R1: witness search")
cands = list(PS) + [BELL, tab(Matrix([0, 1, -1, 0]) * Matrix([0, 1, -1, 0]).T / 2), tab(Matrix([1, 0, 0, -1]) * Matrix([1, 0, 0, -1]).T / 2), tab(Matrix([0, 1, 1, 0]) * Matrix([0, 1, 1, 0]).T / 2)]
for g in [lambda w: actC(R1, w), lambda w: actC(R1 * R1, w), lambda w: actT(R1, w), lambda w: actC(cyc3, w), lambda w: actC(Rx90, w)]:
    cands += [g(p) for p in PS]
for a in itertools.product([-1, 0, 1], repeat=3):
    for b in itertools.product([-1, 0, 1], repeat=3):
        if sum(map(abs, a)) == 1 and sum(map(abs, b)) == 1:
            cands.append(Matrix([1] + list(a)) * Matrix([1] + list(b)).T)
cands = [c for c in cands if pure_in_KZF(c)]
best3 = None; which = None
for s_i, z in enumerate(ZL):
    img = actC(R1, z)
    for k, c in enumerate(cands):
        val = simplify(ipW(c, img))
        if best3 is None or val < best3: best3, which = val, (s_i, k)
    for t in ZL:                         # defects as witnesses (in K)
        val = simplify(ipW(t, img))
        if val < best3: best3, which = val, (s_i, 'defect')
rec('W3', best3 is not None and best3 < 0, 'K(Z_F): actC R1 moves a defect out of K(Z_F) (a witness in K pairs < 0 with the image)', 'best candidate value %s at %s (R6/AUDIT-Y R7 with their witnesses: -2383/5316); candidates %d' % (best3, which, len(cands)))
print("== W4 K(E0) leaves itself under every listed map")
mapsE = {'actC nflip': lambda w: actC(NF, w), 'actT nflip': lambda w: actT(NF, w), 'actC rot3pi': lambda w: actC(ROT3PI, w), 'actC cyc3': lambda w: actC(cyc3, w), 'actT cyc3': lambda w: actT(cyc3, w),
         'actC Rx90': lambda w: actC(Rx90, w), 'actC Rn90': lambda w: actC(Rn90, w), 'actC R1': lambda w: actC(R1, w), 'SWAP': swapW}
# pure states of Q3 n E0*: the joint (-1)-eigenvector of X x Z and Y x Y (pairs +1 with E0), basis products, Bell states, and their images
ph = Matrix.vstack(KR[(1, 3)] + eye(4), KR[(2, 2)] + eye(4)).nullspace()[0]; ph = ph / sqrt((ph.H * ph)[0]); RHO = tab(ph * ph.H)
v6 = Matrix([5, -5, -1, -1]); RHO6 = tab(v6 * v6.H / (v6.H * v6)[0])
candsE = [RHO, RHO6, BELL] + [c for c in cands]
for g in mapsE.values(): candsE += [g(RHO), g(RHO6)]
candsE = [c for c in candsE if pure_in_KE0(c)]
w4 = {}
for name, f in mapsE.items():
    img = f(E0); w4[name] = min(simplify(ipW(c, img)) for c in candsE)
rec('W4', all(v < 0 for v in w4.values()) and w4['SWAP'] == Q(-5, 13), 'K(E0): every listed one-token map and SWAP move E0 out (a pure state of Q3 n E0* pairs < 0 with the image); SWAP value -5/13', str(w4))
print("== W5 the weakest forms")
rec('W5', w2['actC Rx90'] == Q(-1, 2) and w2['actC cyc3'] == Q(-1, 2) and inv['Ad(Z x I)'] and inv['actC nflip'] and inv['SWAP'],
    'K(Z_F) violates (b) for {flow about x, J} and for {flow about x, phase flow about z} on the control token (the flow alone suffices), and satisfies the NOT-only, phase-only and SWAP forms')
print('SUMMARY %d/%d CONFIRMED' % (sum(R), len(R)))
print('PREAUDIT-T6-FIXED' if all(R) else 'PREAUDIT-T6-MISMATCH')
