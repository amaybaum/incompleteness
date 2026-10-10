"""Exploratory float sanity check of the key lemma constants (NOT a certificate):
min over b in Lor (b0=1), y in ball of sqrt(AB) - eps_max*(|Se|+|So|), eps_max=(1-lam)/(2(1+lam))."""
import numpy as np
rng=np.random.default_rng(0)
for k in (1,2,3):
    d=2*k+1; n=d+1; lam=0.5; eps=(1-lam)/(2*(1+lam))
    s=np.array([1 if m<=k else -1 for m in range(n)])
    sig=list(range(n)); sig[0],sig[1]=1,0; sig[d],sig[k+1]=k+1,d
    worst=np.inf
    for _ in range(200000):
        b=rng.normal(size=d); b*= rng.random()**(1/d)/np.linalg.norm(b) if rng.random()<0.5 else 1/np.linalg.norm(b)
        y=rng.normal(size=d); y*= rng.random()**(1/d)/np.linalg.norm(y) if rng.random()<0.5 else 1/np.linalg.norm(y)
        bb=np.concatenate([[1],b]); w=np.concatenate([lam*y[:-1],[y[-1]]]); Y=np.concatenate([[1],w])
        A=bb@Y; B=bb@(s*Y)
        Se=sum(Y[v]*bb[sig[v]] for v in range(n) if s[v]==1); So=sum(Y[v]*bb[sig[v]] for v in range(n) if s[v]==-1)
        worst=min(worst, np.sqrt(max(A*B,0))-eps*(abs(Se)+abs(So)))
    print("k",k,"min sqrt(AB)-eps_max(|Se|+|So|) =",worst)
print("near-corner sampling (ratio test: (|Se|+|So|)/sqrt(AB) must stay <= 1/eps_max):")
for k in (1,2,3):
    d=2*k+1; n=d+1; lam=0.5; eps=(1-lam)/(2*(1+lam))
    s=np.array([1 if m<=k else -1 for m in range(n)])
    sig=list(range(n)); sig[0],sig[1]=1,0; sig[d],sig[k+1]=k+1,d
    worst=0
    for _ in range(200000):
        t,sv=10**rng.uniform(-6,0),10**rng.uniform(-6,0)
        u=rng.normal(size=d-1);u/=np.linalg.norm(u); v=rng.normal(size=d-1);v/=np.linalg.norm(v)
        sg=rng.choice([-1,1]); sz=rng.choice([-1,1])
        b=np.concatenate([t*u,[sg*np.sqrt(1-t*t)]]); y=np.concatenate([sv*v,[sz*np.sqrt(1-sv*sv)]])
        bb=np.concatenate([[1],b]); w=np.concatenate([lam*y[:-1],[y[-1]]]); Y=np.concatenate([[1],w])
        A=bb@Y; B=bb@(s*Y)
        Se=sum(Y[q]*bb[sig[q]] for q in range(n) if s[q]==1); So=sum(Y[q]*bb[sig[q]] for q in range(n) if s[q]==-1)
        worst=max(worst,(abs(Se)+abs(So))/np.sqrt(A*B))
    print(" k",k,"max ratio",worst,"bound 1/eps_max =",1/eps)
