import math, itertools
lam, sd = 0.22500, 0.00067
target = 1/(math.pi*math.sqrt(2))
def fam(N):
    out={}
    for a,b in itertools.product(range(1,N+1),repeat=2):
        if math.gcd(a,b)!=1: continue
        for k in (-2,-1,0,1):
            for r in (1,2,3,5,6):
                for s in ((1,) if r==1 else (-1,1)):
                    v=a/b*math.pi**k*math.sqrt(r)**s
                    key=round(v,12)
                    cplx=a+b+abs(k)+(0 if r==1 else r)
                    if key not in out or cplx<out[key][0]: out[key]=(cplx,f"{a}/{b}*pi^{k}*sqrt{r}^{s}")
    return out
for N in (12,4,2,1):
    F=fam(N); vals=sorted(F)
    hits=[v for v in vals if abs(v-lam)<=sd]
    glob=[v for v in vals if 0.1<=v<=0.5]
    loc=[v for v in vals if abs(v-lam)<=0.03]       # local density window +-0.03
    exp_glob=len(glob)*2*sd/0.4; exp_loc=len(loc)*2*sd/0.06
    tight=[v for v in vals if abs(v-lam)<=abs(target-lam)]
    print(f"N={N}: distinct in[0.1,0.5]={len(glob)} hits(1sig)={len(hits)} exp(global)={exp_glob:.2f} exp(local +-0.03)={exp_loc:.2f} within |d|<=0.12sig: {len(tight)}")
# complexity-ranked: how many forms at most as simple as 1/(pi sqrt2) exist, and P(one lands within 1 sigma)
F=fam(12)
c0=F[round(target,12)][0]
simple=[v for v,(c,_) in F.items() if c<=c0 and 0.1<=v<=0.5]
print("complexity of 1/(pi sqrt2):",c0," forms in [0.1,0.5] at most as simple:",len(simple), " expected 1sig hits (global density):", round(len(simple)*2*sd/0.4,3))
print("hits among them:", [F[round(v,12)][1] for v in simple if abs(v-lam)<=sd])
# p-value style: chance that the simplest-complexity set contains a hit, by placing lam uniformly in [0.1,0.5]
import random
random.seed(1); S_=sorted(simple); n=0; T=200000
for _ in range(T):
    x=random.uniform(0.1,0.5)
    if any(abs(v-x)<=sd for v in S_): n+=1
print("P(some form of that simplicity within 1 sigma of a random target):", n/T)
