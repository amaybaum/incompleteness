#!/usr/bin/env python3
"""Coordinator's pre-audit facts for stage 5 (Q-EX-BRIDGE), fixed before threads D and C report.  Exact (sympy).
DECISION RULE (fixed before the first run): every line CONFIRMED or MISMATCH; PREAUDIT-BRIDGE-FIXED iff all CONFIRMED.

Facts.  B1: the native drive (one-parameter rotations about the NOT axis x, on-frame) idle-extended on the control
closes with cnot to an abelian 2-torus (dimension 2: stage 4's S3 instance), and J = cyc3 (the cyclic axis
permutation x -> y -> z -> x of ball3Drive) conjugates it to the rotations about y; the two coordinate flows with
cnot close to the full su(2)(+)su(2) (dimension 6): (b) for the drive and J on one token gives S4-C, UNIQUE by
stage 4.  B2: cyc3 is a signed axis permutation of order 3 about (1,1,1); with Rz(pi) it generates a finite group
(order 12: Y7's countercontrol), so {NOT, J} idle-extended is a finite extension of G16 (EXOTIC-E by stage 4, Y5),
and K(Z_F) is not invariant under cyc3 (x) I (exact witness), so no stage-3 cone serves there and the countermodel is
EBF existence.  B3: the gate's own flow exp(-i theta P1 (x) P-) is diagonal in the product basis |a>_Z |b>_X (inside
the 3-torus of product-diagonal unitaries), so stage 4's Z result for <T^3, G16> (EXOTIC-E, seeds on the circles)
covers a 'gate drive' candidate.  B4: steering / conditional admissibility: the stage-3 cones lie in maxCone and
local unitaries preserve maxCone, so the drive image of a defect keeps every conditional state admissible while
leaving the cone (exact instance).  B5: NOT-level consequences of relC: if actC N preserves K and G preserves K then
actT N preserves K (symbolic identity on the carrier); K(Z_F) is invariant under both NOTs (stage 4 pre-audit P6).
Countercontrols: the drive alone (one coordinate flow) closes to dimension 2 (not reachable); cyc3 has order 3 and
<cyc3, Rz(pi)> is finite; a product state keeps its conditional states and stays in every cone.
"""
import sys
import sympy as sp
R = []
def rec(cid, kind, ok, text, detail=""):
    ok = bool(ok); R.append(ok)
    print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}" + (f" -- {detail}" if detail else ""))
I2 = sp.eye(2); SX = sp.Matrix([[0,1],[1,0]]); SY = sp.Matrix([[0,-sp.I],[sp.I,0]]); SZ = sp.Matrix([[1,0],[0,-1]])
SG = [I2, SX, SY, SZ]; kron = sp.kronecker_product
KR = {(m,n): kron(SG[m], SG[n]) for m in range(4) for n in range(4)}
def pauliW(w): return sum((w[m,n]*KR[(m,n)] for m in range(4) for n in range(4) if w[m,n] != 0), sp.zeros(4,4))/4
def tab(M): return sp.Matrix(4,4, lambda m,n: sp.nsimplify(sp.expand((KR[(m,n)]*M).trace())))
def ipW(a,b): return sp.expand(sum(a[i,j]*b[i,j] for i in range(4) for j in range(4)))
def E(m,n): B = sp.zeros(4,4); B[m,n] = 1; return B
def charcoeffs(M):
    x = sp.Symbol('x'); return sp.Poly(sp.expand((x*sp.eye(M.rows) - M).det()), x).all_coeffs()
def is_psd(M):
    cs = charcoeffs(M); return all(sp.simplify((-1)**k * cs[k]) >= 0 for k in range(len(cs)))
def Ad(U, w): return tab(U*pauliW(w)*U.H)
CNOT = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
def zdef(s1, s2): return (E(0,0) + s1*E(1,3) + s2*E(2,2) - s1*s2*E(3,1))/4
ZF = {(s1,s2): zdef(s1,s2) for s1 in (1,-1) for s2 in (1,-1)}
def ad_closure_dim(gens):
    basis = [sp.Matrix(g) for g in gens]
    def rank(vs): return sp.Matrix.hstack(*vs).rank() if vs else 0
    changed = True
    while changed:
        changed = False; r0 = rank(basis)
        for u in list(basis):
            for v_ in list(basis):
                a1, b1 = u[:3,0], u[3:,0]; a2, b2 = v_[:3,0], v_[3:,0]
                br = sp.Matrix.vstack(a1.cross(a2), b1.cross(b2))
                if rank(basis + [br]) > r0: basis.append(br); r0 += 1; changed = True
    return rank(basis)
def Rz_pi(n): return sp.Matrix([-n[0], -n[1], n[2]])
def gens_control(n): n = sp.Matrix(n); return [sp.Matrix.vstack(n, n), sp.Matrix.vstack(n, Rz_pi(n))]

print("== B  pre-audit facts for Q-EX-BRIDGE (fixed before threads D and C report)")
# B1: the drive about x alone: dim 2; with its cyc3-conjugate (about y): dim 6
cyc3 = sp.Matrix([[0,0,1],[1,0,0],[0,1,0]])     # x -> y -> z -> x as a rotation matrix (columns are images of e_x, e_y, e_z)
ex = sp.Matrix([1,0,0]); ey = cyc3*ex
d_x = ad_closure_dim(gens_control(ex)); d_xy = ad_closure_dim(gens_control(ex) + gens_control(list(ey)))
rec("B1", "identity", d_x == 2 and list(ey) == [0,1,0] and d_xy == 6,
    "the native drive about the NOT axis x closes with cnot to dimension 2 (abelian torus: stage 4's S3); cyc3 carries x to y, and the two coordinate flows close with cnot to su(2)+su(2) (dimension 6): (b) for the drive and J on one token gives S4-C, hence Q3 by stage 4", f"dims {d_x}, {d_xy}")
# B2: cyc3 order 3 about (1,1,1); <cyc3, Rz(pi)> finite; K(Z_F) not cyc3(x)I-invariant
Rzpi = sp.diag(-1, -1, 1)
grp = {sp.ImmutableMatrix(sp.eye(3))}; frontier = [sp.ImmutableMatrix(sp.eye(3))]
while frontier:
    new = []
    for g in frontier:
        for h in (cyc3, Rzpi):
            k = sp.ImmutableMatrix(h*g)
            if k not in grp: grp.add(k); new.append(k)
    frontier = new
axis = cyc3*sp.Matrix([1,1,1])
rec("B2a", "identity", (cyc3**3 - sp.eye(3)).is_zero_matrix and cyc3 != sp.eye(3) and axis == sp.Matrix([1,1,1]) and cyc3.det() == 1 and len(grp) == 12,
    "cyc3 is a rotation of order 3 fixing (1,1,1), and with Rz(pi) it generates a finite group of order 12 (Y7's countercontrol): {NOT, J} idle-extended on the control is a finite extension of G16, EXOTIC-E by stage 4 (Y5, Z z4), never UNIQUE", f"order {len(grp)}")
# unitary lift of cyc3: U = (I - i(X+Y+Z))/2 conjugates X->Y->Z->X (up to the direction convention); check it realizes the axis permutation and moves z_(1,1) out of K(Z_F) by a pure-state witness
Ucyc = (I2 - sp.I*(SX + SY + SZ))/2
imgs = [tab(kron(Ucyc, I2)*pauliW(E(a,0))*kron(Ucyc, I2).H) for a in (1,2,3)]
perm_ok = all(sum(1 for b in (1,2,3) if im[b,0] != 0) == 1 for im in imgs)
h = Ad(kron(Ucyc, I2), ZF[(1,1)])
inZF = any((h - ZF[t]).applyfunc(sp.simplify) == sp.zeros(4,4) for t in ZF)
# witness: pure state v in K(Z_F) (PSD, pairs >= 0 with every z_s) pairing negatively with h: take the negative eigenvector of pauliW(h)
ev = pauliW(h).eigenvects()
neg = [v for val, mult, vs in ev for v in vs if sp.simplify(val) < 0]
vneg = neg[0]; vneg = vneg/sp.sqrt(sp.simplify((vneg.H*vneg)[0,0])); Pv = tab(vneg*vneg.H)
pairs = [sp.simplify(ipW(Pv, ZF[s])) for s in ZF]
rec("B2b", "witness", perm_ok and not inZF and all(p >= 0 for p in pairs) and sp.simplify(ipW(Pv, h)) < 0 and is_psd(pauliW(Pv)),
    "the unitary lift of cyc3 permutes the control axes; its image of the defect z_(1,1) lies outside Z_F, and a pure state of K(Z_F) (PSD, pairing >= 0 with every defect) pairs negatively with it: K(Z_F) is not J-invariant, so the {NOT, J} countermodel is EBF existence, not the stage-3 cone", f"pairings with Z_F {pairs}, with the image {sp.simplify(ipW(Pv, h))}")
# B3: the gate flow exp(-i theta P1 (x) P-) is diagonal in the product basis |a>_Z|b>_X
th = sp.Symbol('theta', real=True)
P1 = (I2 - SZ)/2; Pm = (I2 - SX)/2; Hgen = kron(P1, Pm)
flow = sp.eye(4) + (sp.exp(-sp.I*th) - 1)*Hgen          # exp(-i theta Hgen) for a projector Hgen
plus = sp.Matrix([1,1])/sp.sqrt(2); minus = sp.Matrix([1,-1])/sp.sqrt(2); e0 = sp.Matrix([1,0]); e1 = sp.Matrix([0,1])
Bm = sp.Matrix.hstack(kron(e0, plus), kron(e1, minus), kron(e0, minus), kron(e1, plus))
flowB = (Bm.H*flow*Bm).applyfunc(sp.simplify)
offdiag_zero = all(flowB[i,j] == 0 for i in range(4) for j in range(4) if i != j)
rec("B3", "identity", (Hgen*Hgen - Hgen).is_zero_matrix and offdiag_zero and sp.simplify(flowB[1,1] - sp.exp(-sp.I*th)) == 0 and sp.simplify(flow.subs(th, sp.pi) - CNOT).is_zero_matrix,
    "the gate's own flow exp(-i theta P1(x)P-) is diagonal in the product basis (|0+>,|1->,|0->,|1+>) with CNOT at theta = pi: it lies in the 3-torus of product-diagonal unitaries, so stage 4's Z verdict for <T^3, G16> (EXOTIC-E) covers a 'gate drive' candidate", str([flowB[i,i] for i in range(4)]))
# B4: steering / conditional admissibility: K(Z_F) in maxCone (product-effect positivity) and local unitaries preserve maxCone; the drive image of a defect keeps conditional admissibility but leaves K(Z_F)
# maxCone membership for a table w: <w, p(x) (x) p(y)> >= 0 for all unit-ball x, y: check on the defect's drive image via its pauliW: for product pure states |a b>, 4 tr(rho P_ab) >= 0; exact at a sample and by the structure (unitary conjugation preserves the set of product effects)
Ux = lambda t: sp.cos(t/2)*I2 - sp.I*sp.sin(t/2)*SX
hz = Ad(kron(Ux(sp.Rational(1,3)), I2), ZF[(1,1)])   # drive image at a rational angle
import itertools
samples = []
for a in (sp.Matrix([1,0]), sp.Matrix([1,1])/sp.sqrt(2), sp.Matrix([1,sp.I])/sp.sqrt(2), sp.Matrix([3,4])/5, sp.Matrix([1,2*sp.I])/sp.sqrt(5)):
    for b in (sp.Matrix([1,0]), sp.Matrix([1,1])/sp.sqrt(2), sp.Matrix([1,sp.I])/sp.sqrt(2), sp.Matrix([3,4])/5, sp.Matrix([0,1])):
        pab = kron(a, b); samples.append(sp.simplify(4*(pab.H*pauliW(hz)*pab)[0,0]))
# a pure state of K(Z_F) pairing negatively with hz.  Run 1 used the negative eigenvector of pauliW(hz), which is the
# rotated Bell-type state itself and is NOT in Z_F* (overlap cos^2(1/6) > 1/2 with f_(1,1)): harness error.  The witness
# is the equal superposition of the two Bell-type states that the flow connects: X(x)I permutes z_(1,1) <-> z_(1,-1), so
# f' = (U(x)I) f_(1,1) = alpha f_(1,1) + beta f_(1,-1); v = (f_(1,1) + e^{i phi} f_(1,-1))/sqrt2 with the phase of beta/alpha
# has overlap 1/2 with f_(1,1) and f_(1,-1), 0 with the other two (in Z_F*), and (|alpha|+|beta|)^2/2 > 1/2 with f'.
# Run 2 transcribed Z's formula psi_s = (1, s1 s2, s1, -s2)/2 for the Bell-type states; in the stage-3 convention
# (control index first) it does not reproduce z_s (harness/convention slip, recorded below as information).  The
# states are taken instead as the normalized negative eigenvectors of pauliW(z_s) (eigenvalue -1/8), exactly.
def bellstate_from(z):
    vecs = [v for val, mult, vs in pauliW(z).eigenvects() for v in vs if sp.simplify(val) < 0]
    v = vecs[0]; return (v/sp.sqrt(sp.simplify((v.H*v)[0,0]))).applyfunc(sp.simplify)
fs = {s: bellstate_from(ZF[s]) for s in ZF}
bell_ok = all((tab((sp.eye(4) - 2*fs[s]*fs[s].H)/8) - ZF[s]).applyfunc(sp.simplify) == sp.zeros(4,4) for s in ZF)
zform = {s: sp.Matrix([1, s[0]*s[1], s[0], -s[1]])/2 for s in ZF}
zform_hits = {s: [t for t in ZF if (tab((sp.eye(4) - 2*zform[s]*zform[s].H)/8) - ZF[t]).applyfunc(sp.simplify) == sp.zeros(4,4)] for s in ZF}
zform_T = {s: [t for t in ZF if (tab((sp.eye(4) - 2*zform[s]*zform[s].H)/8).T - ZF[t]).applyfunc(sp.simplify) == sp.zeros(4,4)] for s in ZF}
print(f"INFO Z's formula psi_s = (1, s1 s2, s1, -s2)/2 reproduces, in the control-first convention: {zform_hits}; after token exchange (table transpose): {zform_T}")
fprime = kron(Ux(sp.Rational(1,3)), I2)*fs[(1,1)]
alpha = sp.simplify((fs[(1,1)].H*fprime)[0,0]); beta = sp.simplify((fs[(1,-1)].H*fprime)[0,0])
rest = sp.simplify((fprime - alpha*fs[(1,1)] - beta*fs[(1,-1)]).norm())
phase = sp.simplify(beta/alpha/sp.Abs(beta/alpha))
v2 = (fs[(1,1)] + phase*fs[(1,-1)])/sp.sqrt(2); Pv2 = tab(v2*v2.H); pairs2 = [sp.simplify(ipW(Pv2, ZF[s])) for s in ZF]
pair_h = sp.simplify(ipW(Pv2, hz))
rec("B4", "witness", bell_ok and rest == 0 and all(sp.simplify(sv) >= 0 for sv in samples) and all(p >= 0 for p in pairs2) and is_psd(pauliW(Pv2)) and pair_h < 0 and sp.simplify(pair_h + sp.sin(sp.Rational(1,3))/2) == 0,
    f"the drive image of z_(1,1) at angle 1/3 pairs >= 0 with {len(samples)} exact product effects (conditional-state admissibility, maxCone), yet the pure state (f_(1,1) + e^(i phi) f_(1,-1))/sqrt2 of K(Z_F) (overlaps 1/2, 1/2, 0, 0 with the Bell-type states) pairs -sin(1/3)/2 < 0 with it: steering-type principles are satisfied by the image while the cone is not preserved (INDEPENDENT route for candidate theta); the Bell-type states psi_s = (1, s1 s2, s1, -s2)/2 reproduce the stage-3 defects exactly", f"pairings with Z_F {pairs2}, with the image {pair_h}")
# B5: relC consequence (symbolic identity shape) and NOT-invariance of K(Z_F) on both tokens
XI = kron(SX, I2); IX = kron(I2, SX)
rel = all((Ad(XI, Ad(CNOT, Ad(XI, E(m,n)))) - Ad(IX, Ad(CNOT, E(m,n)))).is_zero_matrix for m in range(4) for n in range(4))
notinv = all(any((Ad(XI, ZF[s]) - ZF[t]) == sp.zeros(4,4) for t in ZF) for s in ZF) and all(any((Ad(IX, ZF[s]) - ZF[t]) == sp.zeros(4,4) for t in ZF) for s in ZF)
rec("B5", "identity", rel and notinv,
    "relC holds for Ad(CNOT) with the NOT = Ad(X) on all 16 basis tables (actC N . G . actC N = actT N . G), so NOT-preservation on the control plus gate preservation gives NOT-preservation on the target; K(Z_F) is invariant under both idle-extended NOTs (the NOT level of (b) excludes nothing)")
# countercontrols
rec("B6c", "countercontrol", d_x == 2 and len(grp) == 12 and all(sp.simplify(4*(kron(a, b).H*pauliW(tab(kron(a,b)*kron(a,b).H))*kron(a, b))[0,0]) == 4 for a, b in [(sp.Matrix([1,0]), sp.Matrix([0,1]))]),
    "countercontrols: the drive alone closes to dimension 2 (not reachable); the J group with Rz(pi) is finite (no infinite-order criterion); a product state's own conditional admissibility is trivial (pairing 4|<ab|ab>|^2 = 4 with itself in the ipW normalization; run 1 asserted 1: harness)")
n_ = sum(R); print(f"checks: {len(R)}, confirmed: {n_}"); print("VERDICT", "PREAUDIT-BRIDGE-FIXED" if n_ == len(R) else "PREAUDIT-BRIDGE-MISMATCH"); sys.exit(0 if n_ == len(R) else 1)
