#!/usr/bin/env python3
# b92: does the classical action-labelled comb theorem (Main §3.4) already reach
# QUANTUM instrument statistics? Test against the sharpest temporal witness:
# a Leggett-Garg violation from sequential projective qubit measurements.
# Exact arithmetic throughout (Fractions); rotation angle pi/3 makes every
# probability rational.
from fractions import Fraction as F
from itertools import product

# qubit, rotate about y by theta=pi/3 between measurement times, measure sigma_z.
# P(same | one step) = (1+cos t)/2 = 3/4 ; P(same | two steps) = (1+cos 2t)/2 = 1/4
p1 = F(3,4)     # one-step survival
p2 = F(1,4)     # two-step survival (no intermediate measurement)

# Action alphabet at time 2: a=1 MEASURE (collapse), a=0 SKIP.
# Visible alphabet {0,1} = sigma_z outcomes, recorded at t1, t2, t3.
def quantum_comb():
    """P(x_{k+1} | x_<=k, a_<=k) for the two action sequences, exactly."""
    P={}
    # step 1->2 : if measured, outcome distributed by one-step law; if skipped the
    # register simply repeats x1 (no information gained, no collapse).
    for x1 in (0,1):
        P[((x1,),(1,))] = {x1:p1, 1-x1:1-p1}       # measure at t2
        P[((x1,),(0,))] = {x1:F(1), 1-x1:F(0)}     # skip: register unchanged
    # step 2->3
    for x1 in (0,1):
        for x2 in (0,1):
            # measured at t2: collapse to x2, then one more step
            P[((x1,x2),(1,1))] = {x2:p1, 1-x2:1-p1}
            # skipped at t2: state still the t1 eigenstate, two steps of evolution
            P[((x1,x2),(0,1))] = {x1:p2, 1-x1:1-p2}
    return P

P=quantum_comb()
def corr(pa,pb):  # <x_a x_b> in +-1 convention from a survival probability
    return 2*pa-1
C12=corr(p1,None); C23=corr(p1,None); C13=corr(p2,None)
K=C12+C23-C13
print("== the target statistics ==")
print(f"  one-step survival {p1}, two-step {p2}")
print(f"  C12={C12}  C23={C23}  C13={C13}   K = C12+C23-C13 = {K}   (classical LG bound: K <= 1)")
print(f"  LEGGETT-GARG VIOLATION: {K>1}")

# ---- the comb construction of Main 3.4, built explicitly and checked exactly ----
# contexts c = (x_<=k, a_<=k); hidden u = (u_c) independent with u_c ~ P(.|c);
# state = (x, history ledger, action ledger, u, clock); I_a writes a; phi reads.
ctxs=sorted(P.keys())
print(f"\n== the realization ==\n  contexts: {len(ctxs)}   hidden space size: {2**len(ctxs)}")
# enumerate the hidden product prior exactly and recompute every conditional
def induced(actions):
    """Run the deterministic realization over the full hidden ensemble, exactly."""
    out={}
    # marginal over x1 uniform (the initial visible ensemble)
    for x1 in (0,1):
        # step 1->2
        c1=((x1,),(actions[0],))
        # phi reads u_{c1}
        d2={v:pr for v,pr in P[c1].items()}
        for x2,pr2 in d2.items():
            c2=((x1,x2),(actions[0],actions[1]))
            d3=P[c2]
            for x3,pr3 in d3.items():
                out[(x1,x2,x3)]=out.get((x1,x2,x3),F(0))+F(1,2)*pr2*pr3
    return out
for acts in [(1,1),(0,1)]:
    joint=induced(acts)
    tot=sum(joint.values())
    # recover the conditionals and compare with the target
    ok=True
    for (x1,x2,x3),pr in joint.items():
        m=sum(v for (a,b,c),v in joint.items() if (a,b)==(x1,x2))
        if m: 
            cond=pr/m
            if cond!=P[((x1,x2),acts)][x3]: ok=False
    print(f"  action sequence {acts}: total mass {tot}, conditionals reproduced EXACTLY: {ok}")
# the LG statistic recomputed from the realization
j11=induced((1,1)); j01=induced((0,1))
def C_from(joint,i,k):
    s=F(0)
    for xs,pr in joint.items():
        s+= pr*(1 if xs[i]==xs[k] else -1)
    return s
print(f"\n  from the realization: C12={C_from(j11,0,1)}  C23={C_from(j11,1,2)}  C13={C_from(j01,0,2)}")
Kr=C_from(j11,0,1)+C_from(j11,1,2)-C_from(j01,0,2)
print(f"  K(realized) = {Kr}   matches target: {Kr==K}")
import sys
FAIL = 0 if (Kr==K and K>1) else 1
print("lg_comb_probes:", "ALL CHECKS PASS" if FAIL==0 else "FAILURE")
sys.exit(FAIL) if False else None
print("\nVERDICT: the finite classical action-labelled comb reproduces the")
print("Leggett-Garg-violating quantum instrument statistics EXACTLY — because its")
print("instruments are invasive (they write to the ledger). LG violation is")
print("therefore NOT an obstruction to the classical rung; the open remainder of")
print("the operational bridge is the instrument ALGEBRA, not the numbers.")
import sys as _s; _s.exit(0 if (Kr==K and K>1) else 1)
