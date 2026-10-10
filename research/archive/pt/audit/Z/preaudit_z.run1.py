#!/usr/bin/env python3
"""Coordinator's pre-audit facts for thread Z (stage 4, Q-EX: countermodels), fixed before reading Z's RESULT.
Exact arithmetic (sympy).  DECISION RULE (fixed before the first run): every line CONFIRMED or MISMATCH; the record
is PREAUDIT-Z-FIXED iff all lines CONFIRMED.  Nothing here uses Z's code or conclusions.

Carrier and conventions as in the stage-3 audit: tables w in W 3 (4x4 real), pauliW(w) = sum w[m,n] s_m (x) s_n / 4,
ipW the entrywise inner product, Q3 = {w : pauliW(w) PSD}.  E0 = E00 + E13 - E22 (stage 3's single defect);
the Bell-type defects z_s = (E00 + s1 E13 + s2 E22 - s1 s2 E31)/4, s in {+-1}^2 (the orbit Z_F); the surgery cone
K(Z) = (Q3 cap Z*) + cone Z for a finite, pairwise ipW-orthogonal set Z of tables outside Q3 permuted by the symmetry
group (stage 3's self-duality characterization, audited: each defect has one negative eigenvalue -a and all others
>= a).  Symmetries as conjugations: SWAP (token exchange: table transpose), actC Rz(theta) = Ad(e^{-i theta Z/2} (x) I),
actT Rx(phi) = Ad(I (x) e^{-i phi X/2}).

Facts fixed.  P1: SWAP permutes Z_F (z_s -> z_{(-s1 s2, s2)}) and preserves Q3, so K(Z_F) is SWAP-invariant: S1 is
EXOTIC-X with the stage-3 cone (the protocol's expectation).  P2: ipW(E0, actC Rz(pi) E0) = -1, so no self-dual cone
invariant under the commuting torus contains E0 (an invariant self-dual cone pairs its members nonnegatively):
K(E0) cannot serve for S2.  P3: the torus pairings of a Bell-type defect with its own images are
(1 + cos theta)(1 + cos phi)/16 >= 0, so this obstruction does not fire for Z_F; actC Rz(pi) and actT Rx(pi) permute
Z_F; a generic torus element moves z_s to a table outside Z_F (the orbit is a 2-torus, not finite), so stage 3's
finite-orthogonal surgery does not apply to S2 as it stands.  P4 (retention): Q3 is invariant under SWAP and the
torus (unitary conjugations).  P5 (countercontrol): the SWAP image of E0 is E00 + E31 - E22 != E0 and is ipW-orthogonal
to... no: ipW(E0, SWAP E0) = 1 - (-1)(-1) ... computed exactly below; the point recorded is only that SWAP does NOT fix
E0, so K(E0)'s SWAP-invariance is not automatic and is decided exactly (it holds iff SWAP E0 in K(E0)).
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
def is_psd(M):
    x = sp.Symbol('x'); cs = sp.Poly(sp.expand((x*sp.eye(M.rows) - M).det()), x).all_coeffs()
    return all(sp.simplify((-1)**k * cs[k]) >= 0 for k in range(len(cs)))
def Ad(U, w): return tab(U*pauliW(w)*U.H)
E0 = E(0,0) + E(1,3) - E(2,2)
def zdef(s1, s2): return (E(0,0) + s1*E(1,3) + s2*E(2,2) - s1*s2*E(3,1))/4
ZF = {(s1,s2): zdef(s1,s2) for s1 in (1,-1) for s2 in (1,-1)}
SWAPU = sp.Matrix([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
th, ph = sp.symbols('theta phi', real=True)
def Rz(t): return sp.cos(t/2)*I2 - sp.I*sp.sin(t/2)*SZ
def Rx(t): return sp.cos(t/2)*I2 - sp.I*sp.sin(t/2)*SX
def actC(U, w): return Ad(kron(U, I2), w)
def actT(U, w): return Ad(kron(I2, U), w)

print("== P  pre-audit facts for Z (fixed before reading Z)")
# P1: SWAP = table transpose; permutes Z_F
sw = {s: Ad(SWAPU, ZF[s]) for s in ZF}
perm_ok = all(sw[s] == ZF[(-s[0]*s[1], s[1])] for s in ZF)
tr_ok = all(Ad(SWAPU, ZF[s]) == ZF[s].T for s in ZF) and Ad(SWAPU, E0) == E0.T
rec("P1", "identity", perm_ok and tr_ok, "SWAP acts on tables as the transpose and permutes the Bell-type defects z_s -> z_(-s1 s2, s2): K(Z_F) is SWAP-invariant (S1 EXOTIC-X with the stage-3 cone, given SWAP preserves Q3: P4)",
    str({s: (-s[0]*s[1], s[1]) for s in ZF}))
# P2: E0 and its half-turn image pair to -1
rec("P2", "identity", ipW(E0, actC(Rz(sp.pi), E0)) == -1 and ipW(E0, actC(Rz(th), E0)) == sp.expand(1 + 2*sp.cos(th)) or sp.simplify(ipW(E0, actC(Rz(th), E0)) - (1 + 2*sp.cos(th))) == 0,
    "ipW(E0, actC Rz(theta) E0) = 1 + 2 cos theta, equal to -1 at theta = pi: no torus-invariant self-dual cone contains E0 (members of an invariant self-dual cone pair >= 0)",
    str(sp.simplify(ipW(E0, actC(Rz(th), E0)))))
# P3: Bell-type defects under the torus
pair = sp.simplify(ipW(ZF[(1,1)], actT(Rx(ph), actC(Rz(th), ZF[(1,1)]))))
rec("P3a", "identity", sp.simplify(pair - (1 + sp.cos(th))*(1 + sp.cos(ph))/16) == 0,
    "ipW(z_s, torus(theta, phi) z_s) = (1 + cos theta)(1 + cos phi)/16 >= 0: the P2 obstruction does not fire for the Bell-type defects", str(pair))
permC = all(actC(Rz(sp.pi), ZF[s]) in ZF.values() for s in ZF); permT = all(actT(Rx(sp.pi), ZF[s]) in ZF.values() for s in ZF)
imgC = {s: [t for t in ZF if actC(Rz(sp.pi), ZF[s]) == ZF[t]][0] for s in ZF}; imgT = {s: [t for t in ZF if actT(Rx(sp.pi), ZF[s]) == ZF[t]][0] for s in ZF}
rec("P3b", "identity", permC and permT, "the half-turns actC Rz(pi) = Ad(Z(x)I) and actT Rx(pi) = Ad(I(x)X) permute Z_F", f"Rz(pi): {imgC}; Rx(pi): {imgT}")
gen = actC(Rz(sp.Rational(1,3)), ZF[(1,1)])   # a generic (irrational-angle) torus image, exact in cos/sin
rec("P3c", "identity", all(sp.simplify(gen - ZF[t]) != sp.zeros(4,4) for t in ZF) and sp.simplify(ipW(gen, ZF[(1,1)]) - (1 + sp.cos(sp.Rational(1,3)))/16) == 0 and sp.simplify(ipW(gen, ZF[(-1,1)])) != 0,
    "a generic torus image of z_(1,1) lies outside Z_F and is not ipW-orthogonal to the other defects: the torus orbit of a Bell-type defect is a 2-torus, so stage 3's finite-orthogonal surgery does not apply to S2 directly",
    str(sp.simplify(ipW(gen, ZF[(-1,1)]))))
# P4 retention: unitary conjugations preserve Q3 (checked on a PSD sample with the symbolic torus and SWAP)
rho = sp.Matrix([[2,1,0,sp.I],[1,2,1,0],[0,1,2,1],[-sp.I,0,1,3]])   # Hermitian; check PSD, then images PSD
w_rho = tab(rho)
ret = is_psd(pauliW(w_rho)) and is_psd(pauliW(Ad(SWAPU, w_rho))) and is_psd(sp.simplify(pauliW(actC(Rz(sp.Rational(2,7)), w_rho)))) and is_psd(sp.simplify(pauliW(actT(Rx(sp.Rational(3,5)), w_rho))))
rec("P4", "retention", ret, "Q3 is preserved by SWAP and by the torus (unitary conjugations; exact PSD checks on a rank-4 sample and its images)")
# P5 countercontrol: SWAP does not fix E0; ipW(E0, SWAP E0) computed; SWAP E0 in K(E0) iff (SWAP E0 - lambda E0) PSD for some lambda >= 0 -- decided exactly
sE0 = Ad(SWAPU, E0); lam = sp.Symbol('lambda', real=True)
x = sp.Symbol('x'); M = pauliW(sE0 - lam*E0); cs = sp.Poly(sp.expand((x*sp.eye(4) - M).det()), x).all_coeffs()
conds = [sp.expand((-1)**k * cs[k]) >= 0 for k in range(len(cs))]
feas = sp.solve_univariate_inequality(sp.And(*[c for c in conds if c is not sp.true]) if any(c is not sp.true for c in conds) else sp.true, lam, relational=False) if True else None
feas_nonneg = sp.Intersection(feas, sp.Interval(0, sp.oo)) if feas is not None else None
rec("P5c", "countercontrol", sE0 != E0 and ipW(E0, sE0) == 1 and feas_nonneg == sp.EmptySet,
    "countercontrol: SWAP E0 = E00 + E31 - E22 != E0 with ipW(E0, SWAP E0) = 1 >= 0 (no pairing obstruction), yet SWAP E0 - lambda E0 is PSD for no lambda >= 0: SWAP E0 is not in K(E0), so K(E0) is NOT SWAP-invariant (S1 needs the Bell-type cone, not K(E0))",
    f"feasible lambda: {feas_nonneg}")
n_ = sum(R); print(f"checks: {len(R)}, confirmed: {n_}"); print("VERDICT", "PREAUDIT-Z-FIXED" if n_ == len(R) else "PREAUDIT-Z-MISMATCH"); sys.exit(0 if n_ == len(R) else 1)
