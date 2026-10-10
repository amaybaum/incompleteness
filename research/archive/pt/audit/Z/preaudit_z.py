#!/usr/bin/env python3
"""Coordinator's pre-audit facts for thread Z (stage 4, Q-EX: countermodels), fixed before reading Z's RESULT.
Exact arithmetic (sympy).  DECISION RULE (fixed before the first run): every line CONFIRMED or MISMATCH; the record
is PREAUDIT-Z-FIXED iff all lines CONFIRMED.  Nothing here uses Z's code or conclusions.

Run history.  Run 1 (kept as preaudit_z.run1.*): 3 of the first 5 lines CONFIRMED; P3a MISMATCH because my hand
formula for the torus pairing was wrong (the exact value is (1 + cos(theta + s1 s2 phi))/8, still >= 0, so the
conclusion stands and the formula is corrected here); P3c MISMATCH because the generic torus image of z_(1,1) IS
orthogonal to z_(-1,1) and z_(1,-1) for every angle (its pairing with the other defects is (1 - cos theta)/8 with
z_(-1,-1) and 0 with the other two) -- the correct non-orthogonality is between members of the orbit itself,
checked here; P4 crashed (sympy could not decide the sign of a trigonometric expression) -- run 2 uses rational
unitaries (3/5, 4/5).  P5c did not run in run 1; run 2 decides it by the lambda-interval method of indep_checkY R5.
P6 and P7 are added in run 2 before it ran (header fixed before run 2).  Run 2 (kept as preaudit_z.run2.*): 8/9,
P5c MISMATCH only because its asserted pairing value ipW(E0, SWAP E0) = 1 was a hand slip (exact value 2; the
lambda-interval [0, 2/3] is empty, as asserted); run 3 corrects the asserted value and nothing else.

Carrier and conventions as in the stage-3 audit: tables w in W 3 (4x4 real), pauliW(w) = sum w[m,n] s_m (x) s_n / 4,
ipW the entrywise inner product, Q3 = {w : pauliW(w) PSD}.  E0 = E00 + E13 - E22 (stage 3's single defect);
the Bell-type defects z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4, s in {+-1}^2 (the orbit Z_F); the surgery cone
K(Z) = (Q3 cap Z*) + cone Z for a finite, pairwise ipW-orthogonal set Z of tables outside Q3 permuted by the symmetry
group (stage 3's self-duality characterization, audited).  Symmetries as conjugations: SWAP (token exchange: table
transpose), actC Rz(theta) = Ad(e^{-i theta Z/2} (x) I), actT Rx(phi) = Ad(I (x) e^{-i phi X/2}).

Facts fixed.  P1: SWAP permutes Z_F (z_s -> z_{(-s1 s2, s2)}) and preserves Q3 (P4), so K(Z_F) is SWAP-invariant:
S1 is EXOTIC-X with the stage-3 cone (the protocol's expectation).  P2: ipW(E0, actC Rz(pi) E0) = -1, so no
self-dual cone invariant under the commuting torus contains E0: K(E0) cannot serve for S2.  P3: the torus pairings
of a Bell-type defect with its own images are (1 + cos(theta + s1 s2 phi))/8 >= 0 (no P2-type obstruction for Z_F);
actC Rz(pi) and actT Rx(pi) permute Z_F; a generic torus element moves z_s outside Z_F to a table not orthogonal to
z_s (the orbit is a 2-torus, not finite), so stage 3's finite-orthogonal surgery does not apply to S2 as it stands.
P4 (retention): Q3 is invariant under SWAP and the torus.  P5c (countercontrol): SWAP E0 is not in K(E0), so K(E0) is
not SWAP-invariant: S1 needs the Bell-type cone.  P6: the six local Paulis permute Z_F, so K(Z_F) is invariant under
the local-Pauli-and-transpose group LPT and under LPT + SWAP: those finite nodes are EXOTIC-X with the stage-3 cone.
P7: Ad(H (x) I) z_(1,1) is a Bell-type defect outside Z_F and outside K(Z_F) (pure-state witness P_{Psi+}), so the
stage-3 cone is not invariant under the control Clifford group: the node G16 + control Clifford needs a different
countermodel (Z's question).
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
E0 = E(0,0) + E(1,3) - E(2,2)
def zdef(s1, s2): return (E(0,0) + s1*E(1,3) + s2*E(2,2) - s1*s2*E(3,1))/4
ZF = {(s1,s2): zdef(s1,s2) for s1 in (1,-1) for s2 in (1,-1)}
def which(w):
    hits = [t for t in ZF if (w - ZF[t]).applyfunc(sp.simplify) == sp.zeros(4,4)]
    return hits[0] if hits else None
SWAPU = sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
th, ph = sp.symbols('theta phi', real=True)
def Rz(t): return sp.cos(t/2)*I2 - sp.I*sp.sin(t/2)*SZ
def Rx(t): return sp.cos(t/2)*I2 - sp.I*sp.sin(t/2)*SX
def actC(U, w): return Ad(kron(U, I2), w)
def actT(U, w): return Ad(kron(I2, U), w)
r35, r45 = sp.Rational(3,5), sp.Rational(4,5)
Rz_rat = r35*I2 - sp.I*r45*SZ; Rx_rat = r35*I2 - sp.I*r45*SX      # exact unitaries (3/5)^2 + (4/5)^2 = 1

print("== P  pre-audit facts for Z (fixed before reading Z)")
# P1: SWAP = table transpose; permutes Z_F
perm = {s: which(Ad(SWAPU, ZF[s])) for s in ZF}
perm_ok = all(perm[s] == (-s[0]*s[1], s[1]) for s in ZF)
tr_ok = all(Ad(SWAPU, ZF[s]) == ZF[s].T for s in ZF) and Ad(SWAPU, E0) == E0.T
rec("P1", "identity", perm_ok and tr_ok, "SWAP acts on tables as the transpose and permutes the Bell-type defects z_s -> z_(-s1 s2, s2): K(Z_F) is SWAP-invariant (S1 EXOTIC-X with the stage-3 cone, given SWAP preserves Q3: P4)", str(perm))
# P2: E0 and its torus images
pE0 = sp.simplify(ipW(E0, actC(Rz(th), E0)))
rec("P2", "identity", sp.simplify(pE0 - (1 + 2*sp.cos(th))) == 0 and ipW(E0, actC(Rz(sp.pi), E0)) == -1,
    "ipW(E0, actC Rz(theta) E0) = 1 + 2 cos theta, equal to -1 at theta = pi: no torus-invariant self-dual cone contains E0 (members of an invariant self-dual cone pair >= 0)", str(pE0))
# P3: Bell-type defects under the torus
pairs = {s: sp.simplify(ipW(ZF[s], actT(Rx(ph), actC(Rz(th), ZF[s])))) for s in ZF}
rec("P3a", "identity", all(sp.simplify(pairs[s] - (1 + sp.cos(th + s[0]*s[1]*ph))/8) == 0 for s in ZF),
    "ipW(z_s, torus(theta, phi) z_s) = (1 + cos(theta + s1 s2 phi))/8 >= 0 (run 1's hand formula was wrong; the sign conclusion stands): the P2 obstruction does not fire for the Bell-type defects", str(pairs[(1,1)]))
imgC = {s: which(actC(Rz(sp.pi), ZF[s])) for s in ZF}; imgT = {s: which(actT(Rx(sp.pi), ZF[s])) for s in ZF}
rec("P3b", "identity", all(v is not None for v in imgC.values()) and all(v is not None for v in imgT.values()),
    "the half-turns actC Rz(pi) = Ad(Z(x)I) and actT Rx(pi) = Ad(I(x)X) permute Z_F", f"Rz(pi): {imgC}; Rx(pi): {imgT}")
gen = actC(Rz_rat, ZF[(1,1)])                       # a rational-angle torus image (cos theta = 3/5... in Ad: cos = (9-16)/25 = -7/25)
others = {t: ipW(gen, ZF[t]) for t in ZF}
rec("P3c", "identity", which(gen) is None and others[(1,1)] == sp.Rational(1,8)*(1 + sp.Rational(-7,25)) and others[(1,1)] != 0 and others[(-1,1)] == 0 and others[(1,-1)] == 0,
    "a rational-angle torus image of z_(1,1) (cos theta = -7/25) lies outside Z_F and is not ipW-orthogonal to z_(1,1) itself (pairing (1 + cos theta)/8 = 9/100), while orthogonal to z_(-1,1), z_(1,-1): the orbit of a Bell-type defect is a 2-torus of mutually non-orthogonal tables, so stage 3's finite-orthogonal surgery does not apply to S2 directly", str(others))
# P4 retention: unitary conjugations preserve Q3 (exact PSD checks on a rank-4 sample and its images under rational unitaries)
rho = sp.Matrix([[2,1,0,sp.I],[1,2,1,0],[0,1,2,1],[-sp.I,0,1,3]])
w_rho = tab(rho)
ret = is_psd(pauliW(w_rho)) and is_psd(pauliW(Ad(SWAPU, w_rho))) and is_psd(pauliW(actC(Rz_rat, w_rho))) and is_psd(pauliW(actT(Rx_rat, w_rho))) and is_psd(pauliW(actT(Rx_rat, actC(Rz_rat, w_rho))))
rec("P4", "retention", ret, "Q3 is preserved by SWAP and by the torus (unitary conjugations; exact PSD checks on a rank-4 sample and its images under SWAP, actC Rz, actT Rx and their product, with rational unitaries)")
# P5c countercontrol: SWAP E0 in K(E0) = (Q3 cap E0*) + R+ E0 iff some lambda in [0, <SWAP E0, E0>/<E0,E0>] makes SWAP E0 - lambda E0 PSD
sE0 = Ad(SWAPU, E0); lam = sp.Symbol('lam', real=True)
M = pauliW(sE0) - lam*pauliW(E0); cs = charcoeffs(M)
conds = [sp.solve_univariate_inequality(sp.expand((-1)**k*cs[k]) >= 0, lam, relational=False) for k in range(len(cs))]
feas = sp.Interval(0, ipW(sE0, E0)/ipW(E0, E0))
for cset in conds: feas = feas.intersect(cset)
rec("P5c", "countercontrol", sE0 == E(0,0) + E(3,1) - E(2,2) and ipW(E0, sE0) == 2 and feas == sp.EmptySet,
    "countercontrol: SWAP E0 = E00 + E31 - E22 != E0 with ipW(E0, SWAP E0) = 2 >= 0 (no pairing obstruction; run 2's header value 1 was a hand slip, the E22 term contributes too), yet SWAP E0 - lambda E0 is PSD for no lambda in [0, 2/3] (exact root isolation on the characteristic coefficients): SWAP E0 is not in K(E0), so K(E0) is NOT SWAP-invariant (S1 needs the Bell-type cone, not K(E0))",
    f"feasible lambda: {feas}")
# P6: local Paulis permute Z_F
paulis = {f"{a}(x){b}": kron(SG[i], SG[j]) for i, a in enumerate("IXYZ") for j, b in enumerate("IXYZ") if (i == 0) != (j == 0)}
permP = {name: {s: which(Ad(U, ZF[s])) for s in ZF} for name, U in paulis.items()}
okP = all(v is not None for d in permP.values() for v in d.values())
rec("P6", "identity", okP, "all six local Paulis (X, Y, Z on either token) permute Z_F; with cnot, Ad(Z(x)I), Ad(I(x)Z), the transpose and SWAP (P1), K(Z_F) is invariant under LPT (64) and LPT + SWAP (192): those finite nodes are EXOTIC-X with the stage-3 cone",
    "; ".join(f"{k}: {v}" for k, v in permP.items()))
# P7: the control Hadamard carries z_(1,1) to a Bell-type defect outside Z_F and outside K(Z_F)
Hd = sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2)
h = actC(Hd, ZF[(1,1)])
psi_p = sp.Matrix([0,1,1,0])/sp.sqrt(2); Pp = tab(psi_p*psi_p.H)
spec = pauliW(h).eigenvals()
rec("P7", "witness", which(h) is None and spec == {sp.Rational(-1,8): 1, sp.Rational(1,8): 3} and is_psd(pauliW(Pp)) and all(ipW(Pp, ZF[s]) >= 0 for s in ZF) and ipW(Pp, h) == -sp.Rational(1,2),
    "Ad(H(x)I) z_(1,1) is a Bell-type defect (spectrum {-1/8, 1/8, 1/8, 1/8}) outside Z_F; the pure state P_{Psi+} is PSD and pairs >= 0 with every z_s (so it lies in K(Z_F) = K(Z_F)*) and pairs -1/2 with the image: K(Z_F) is not invariant under the control Hadamard, so the node G16 + control Clifford needs a countermodel other than the stage-3 cone",
    f"pairings with Z_F: {[ipW(Pp, ZF[s]) for s in ZF]}")
n_ = sum(R); print(f"checks: {len(R)}, confirmed: {n_}"); print("VERDICT", "PREAUDIT-Z-FIXED" if n_ == len(R) else "PREAUDIT-Z-MISMATCH"); sys.exit(0 if n_ == len(R) else 1)
