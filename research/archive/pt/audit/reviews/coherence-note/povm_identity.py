#!/usr/bin/env python3
"""Coordinator's exact check for the coherence-note review. Decision rule fixed before the first run: every line CONFIRMED else MISMATCH (exit 1)."""
import sys, sympy as sp
R=[]
def rec(cid,kind,ok,text,detail=""):
    ok=bool(ok); R.append(ok); print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} [{kind}] {text}"+(f" -- {detail}" if detail else ""))
rLL,rRR,mLL,mRR=sp.symbols('rho_LL rho_RR M_LL M_RR',real=True)
a,b,c,d=sp.symbols('a b c d',real=True)
rLR=a+sp.I*b; mRL=c+sp.I*d
rho=sp.Matrix([[rLL,rLR],[sp.conjugate(rLR),rRR]]); M=sp.Matrix([[mLL,sp.conjugate(mRL)],[mRL,mRR]])
p=sp.expand((rho*M).trace()); formula=sp.expand(rLL*mLL+rRR*mRR+2*sp.re(rLR*mRL))
rec("I1","identity", sp.simplify(p-formula)==0, "p(x) = tr(rho M(x)) = rho_LL M_LL + rho_RR M_RR + 2 Re(rho_LR M_RL) for Hermitian rho, M (symbolic)")
rec("I2","identity", sp.simplify(formula.subs({a:0,b:0})-(rLL*mLL+rRR*mRR))==0 and sp.simplify(formula.subs({c:0,d:0})-(rLL*mLL+rRR*mRR))==0, "the cross term vanishes if the path coherence rho_LR = 0 OR the effect's off-diagonal element M_RL = 0 (either suffices)")
# a fixed-basis (collapse) readout has diagonal effects in the record basis: M_RL = 0 identically, whatever rho is
rec("I3","identity", sp.simplify(formula.subs({c:0,d:0})-(rLL*mLL+rRR*mRR))==0, "an effect diagonal in the path basis (fixed-basis readout) gives the classical sum for EVERY coherence: coherence alone is not detectable without a basis-changing effect")
# record overlap: joint state sum_ij rho_ij |i><j| (x) |d_i><d_j| traced over the detector multiplies rho_LR by <d_R|d_L>
g1,g2=sp.symbols('g1 g2',real=True); gamma=g1+sp.I*g2  # <d_L|d_R>
rho_red=sp.Matrix([[rLL, rLR*sp.conjugate(gamma)],[sp.conjugate(rLR)*gamma, rRR]])
p2=sp.expand((rho_red*M).trace())
rec("I4","identity", sp.simplify(p2-(rLL*mLL+rRR*mRR+2*sp.re(rLR*sp.conjugate(gamma)*mRL)))==0, "with a path record (detector unread), the path's reduced coherence is rho_LR <d_R|d_L>, so the cross term is scaled by the record overlap; orthogonal records kill it")
n=sum(R); print(f"\nchecks: {len(R)}, confirmed: {n}"); print("VERDICT","COHERENCE-NOTE-IDENTITIES-CONFIRMED" if n==len(R) else "MISMATCH"); sys.exit(0 if n==len(R) else 1)
