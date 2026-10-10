#!/usr/bin/env python3
"""Coordinator's exact check of the owner's second stage-3 note (audit input; no thread code).
Decision rule fixed before the first run: every line CONFIRMED, else MISMATCH (exit 1)."""
import sys, sympy as sp
R=[]
def rec(cid,kind,ok,text,detail=""):
    ok=bool(ok); R.append(ok); print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}"+(f" -- {detail}" if detail else ""))
PC=[[0,0,3,3],[1,1,2,2],[2,2,1,1],[3,3,0,0]]; PT=[[0,1,2,3],[1,0,3,2],[1,0,3,2],[0,1,2,3]]
def cnot(w): return sp.Matrix(4,4, lambda m,n: (-1 if (m,n) in ((1,3),(2,2)) else 1)*w[PC[m][n],PT[m][n]])
S0=sp.eye(2); SX=sp.Matrix([[0,1],[1,0]]); SY=sp.Matrix([[0,-sp.I],[sp.I,0]]); SZ=sp.Matrix([[1,0],[0,-1]]); SG=[S0,SX,SY,SZ]
def pauliW(w): return sum((w[m,n]*sp.kronecker_product(SG[m],SG[n]) for m in range(4) for n in range(4)), sp.zeros(4,4))/4
def tab(rho): return sp.Matrix(4,4, lambda m,n: sp.nsimplify(sp.expand((sp.kronecker_product(SG[m],SG[n])*rho).trace())))
def ipW(a,b): return sp.expand(sum(a[i,j]*b[i,j] for i in range(4) for j in range(4)))
hom=lambda x: sp.Matrix([1,*x]); prod=lambda x,y: hom(x)*hom(y).T
# F = E00/2 - T_psi/4 with T_psi = actT R_H phiW (landed probe), in table form
phiW=sp.diag(1,1,-1,1); RH=sp.Matrix([[0,0,1],[0,-1,0],[1,0,0]]); H4=sp.eye(4); H4[1:,1:]=RH
Tpsi=phiW*H4.T; F=sp.zeros(4,4); F[0,0]=sp.Rational(1,2); F=F-Tpsi/4
rhoF=pauliW(F)
# a Gaussian-rational vector near the negative eigenvector, NOT an eigenvector
# rho(F) = I/8 - |psi><psi|/4 with psi = (1,1,1,-1)/2, so v^dagger rho(F) v < 0 iff |<psi|v>|^2 > |v|^2/2: take v near psi
v=sp.Matrix([1, 1+sp.I*sp.Rational(1,10), 1, -1+sp.Rational(1,7)])
q=sp.simplify((v.H*rhoF*v)[0,0]); nv=sp.simplify((v.H*v)[0,0])
Pv=(v*v.H)/nv; TPv=tab(Pv)
is_eig=(rhoF*v - (q/nv)*v).is_zero_matrix
rec("G1","witness", q<0 and not is_eig, "a Gaussian-rational v (not an eigenvector) with v^dagger rho(F) v < 0 exists; P_v = v v^dagger / v^dagger v has Gaussian-rational entries", f"v^dagger rho(F) v = {q}, eigenvector: {is_eig}")
val=ipW(F,TPv)
rec("G2","witness", all(e.is_rational for e in TPv) and val<0 and sp.simplify(val-4*(rhoF*Pv).trace())==0, "the Pauli table of P_v is rational and ipW(F, P_v) = 4 tr(rho(F) P_v) < 0 exactly: if F were in a self-dual K, P_v would not be", str(val))
# P_v is outside K_gen: pure, Schmidt rank 2 (not a product), and its cnot image is not a product either
C2=sp.Matrix([[v[0],v[1]],[v[2],v[3]]])
cv=sp.Matrix([v[0],v[1],v[3],v[2]])  # CNOT|v>
C2c=sp.Matrix([[cv[0],cv[1]],[cv[2],cv[3]]])
rec("G3","witness", sp.simplify(C2.det())!=0 and sp.simplify(C2c.det())!=0 and TPv.rank()==4 and cnot(TPv).rank()==4, "P_v is entangled (Schmidt rank 2) and so is CNOT P_v: the missed pure state is neither a product nor a CNOT image of one, as the corridor requires")
# the 36-point test is not a positivity test: a table passing all 36 axis-product checks and the cube bound, yet outside maxCone
c=sp.Rational(9,10); w=sp.zeros(4,4); w[0,0]=1; w[1,1]=c; w[1,2]=c; w[2,1]=c; w[2,2]=-c
AX=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
ok36=all(ipW(w,prod(a,b))>=0 for a in AX for b in AX)
cube=all(abs(w[i,j])<=1 for i in range(4) for j in range(4))
x=(1,0,0); y=(-1/sp.sqrt(2),-1/sp.sqrt(2),0)
val_cont=sp.simplify((hom(x).T*w*hom(y))[0,0])
rec("G4","countercontrol", ok36 and cube and val_cont<0, "a table passing all 36 axis-product checks and the cube bound can still lie outside maxCone: w = E00 + (9/10)(E11 + E12 + E21 - E22) has value 1 - (9/10) sqrt 2 < 0 at the unit vectors x = e1, y = -(e1 + e2)/sqrt 2 (the owner's point 1, instance)", f"continuous value {val_cont}")
n=sum(R); print(f"\nchecks: {len(R)}, confirmed: {n}"); print("VERDICT", "QSD-OWNER-NOTE2-CONFIRMED" if n==len(R) else "MISMATCH"); sys.exit(0 if n==len(R) else 1)
