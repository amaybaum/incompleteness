"""Reviewer's independent check (exact rationals) for PR #938 item 1 and item 2.
Process P: stationary GF(2) shift register X_{n+1} = X_{n-2} xor X_n, realized by the fixed bijection
phi(x,(a,b)) = (a^x, (b,x)) on {0,1} x {0,1}^2 with uniform prior (time-homogeneous, stationary).
Control M: X_{n+1} = X_n xor c_n with a 6-cell ring of uniform coins; Markov through horizon 6."""
from fractions import Fraction as F
from itertools import product
from math import log2, log
LN2 = log(2)

def traj_law(phi, states, K):
    out = {}
    w = F(1, len(states))
    for s in states:
        tr = [s[0]]
        for _ in range(K):
            s = phi(s); tr.append(s[0])
        out[tuple(tr)] = out.get(tuple(tr), F(0)) + w
    return out

def tab(law, k):  # (past X_<k, present X_k, next X_{k+1})
    t = {}
    for tr, p in law.items():
        key = (tr[:k], tr[k], tr[k+1]); t[key] = t.get(key, F(0)) + p
    return t

def cmi(t):
    pc, pac, pcb, I = {}, {}, {}, 0.0
    for (a,c,b),p in t.items():
        pc[c]=pc.get(c,0)+p; pac[(a,c)]=pac.get((a,c),0)+p; pcb[(c,b)]=pcb.get((c,b),0)+p
    for (a,c,b),p in t.items():
        if p: I += float(p)*log2(float(p*pc[c]/(pac[(a,c)]*pcb[(c,b)])))
    return I

def gap(t):  # exact best (p0*delta^2) over past pairs with common present; p0 = joint weight Pr[X_<k=p, X_k=c]
    laws = {}
    for (a,c,b),p in t.items():
        laws.setdefault((a,c),{}); laws[(a,c)][b]=laws[(a,c)].get(b,F(0))+p
    best=(F(0),F(0),F(0)); ks=sorted(laws)
    for i,u in enumerate(ks):
        for v in ks[i+1:]:
            if u[1]!=v[1]: continue
            wu,wv=sum(laws[u].values()),sum(laws[v].values())
            tv=sum(abs(laws[u].get(b,0)/wu-laws[v].get(b,0)/wv) for b in set(laws[u])|set(laws[v]))/2
            p0=min(wu,wv)
            if p0*tv*tv>best[0]: best=(p0*tv*tv,p0,tv)
    return best

phiP = lambda s: (s[1]^s[0], s[2], s[0])
phiM = lambda s: (s[0]^s[1],) + tuple(s[2:]) + (s[1],)   # x^=fresh coin; 6-cell coin ring, Markov through K=6
states = list(product((0,1),repeat=3))
statesM = list(product((0,1),repeat=7))
assert len({phiP(s) for s in states})==8 and len({phiM(s) for s in statesM})==128, "bijections"
ok=True
def chk(name,c):
    global ok; ok&=bool(c); print(("PASS " if c else "FAIL ")+name)

# stationarity: law of (X_1..X_K) equals law of (X_0..X_{K-1})
L6=traj_law(phiP,states,6)
m0={};m1={}
for tr,p in L6.items():
    m0[tr[:6]]=m0.get(tr[:6],0)+p; m1[tr[1:]]=m1.get(tr[1:],0)+p
chk("P stationary (shift-invariant 6-window)", m0==m1)
chk("P first three iid uniform, X3 = X0^X2", all(p==F(1,8) for p in traj_law(phiP,states,2).values()) and all(tr[3]==tr[0]^tr[2] for tr in traj_law(phiP,states,3)))
# memory profile
for t in range(0,6):
    T=tab(L6,t); I=cmi(T); g=gap(T)
    print(f"  P order {t}: M_t={I:.6f}  best p0={g[1]} delta={g[2]}  bound={float(g[0])/LN2:.6f}")
    if t<2: chk(f"P order {t}: no witness (M=0, no gap)", abs(I)<1e-12 and g[2]==0)
    else: chk(f"P order {t}: witness, bound holds", I>0 and g[2]==1 and I>=float(g[0])/LN2-1e-12)
# unrestricted every-horizon form: horizon K must carry a gap at some order k<=K-1
for K in range(1,7):
    LK=traj_law(phiP,states,K)
    has=any(gap(tab(LK,k))[2]>0 for k in range(0,K))
    print(f"  P horizon K={K}: some (C4) gap within horizon: {has}")
    if K<=2: chk(f"unrestricted form fails at K={K} for non-Markov P", not has)
    else: chk(f"anchored form holds at K={K} (k=2)", gap(tab(LK,2))[2]==1)
# non-vacuity control: Markov M has no witness and no gap at any order, any horizon
LM=traj_law(phiM,statesM,6)
chk("M Markov: M_t=0 and no gap at every order t<=5", all(abs(cmi(tab(LM,t)))<1e-12 and gap(tab(LM,t))[2]==0 for t in range(6)))
# item 2: suffix-window reading (length-k window ending at present) misses the order-2 gap of P
T=tab(L6,2); suf={}
for (a,c,b),p in T.items(): suf[((a[1:]),c,b)]=suf.get((a[1:],c,b),0)+p
chk("P order 2: full past X_<2 gap=1; length-2 window (X1,X2) gap=0", gap(T)[2]==1 and gap(suf)[2]==0)
# fastbath convention: X3=X0 shift register (Main:165 'order-2' gap) is order 2 under X_<k convention
phiR=lambda s:(s[1],s[2],s[0])   # x'=a, h'=(b,x): X_{n+1}=X_{n-2}  -> X3=X0
LR=traj_law(phiR,states,4)
chk("X3=X0 register: first gap at order k=2 under X_<k, X_k convention", gap(tab(LR,1))[2]==0 and gap(tab(LR,2))[2]==1)
print("VERDICT", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
