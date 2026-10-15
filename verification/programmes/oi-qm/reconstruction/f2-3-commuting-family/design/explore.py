# Design exploration (floating point, not a measurement): search for non-diagonal coupling
# generators G(m), e^{2 pi i G(m)} = Delta(m), with [G(a)_12, G(b)_23] = 0 for all a, b.
import numpy as np, itertools, sys
from scipy.optimize import minimize
from scipy.linalg import expm
q=int(sys.argv[1]); seed=int(sys.argv[2]); trials=int(sys.argv[3])
rng=np.random.default_rng(seed)
states=[(a,b) for a in range(q) for b in range(q)]
classes={p:[i for i,(a,b) in enumerate(states) if (a*b)%q==p] for p in range(q)}
def lift(k):
    t=(-k/q)%1.0
    return t-1 if t>0.5 else t
ms=list(range(1,q))
def herm(params,d):
    H=np.zeros((d,d),complex); idx=0
    for i in range(d):
        H[i,i]=params[idx]; idx+=1
    for i in range(d):
        for j in range(i+1,d):
            H[i,j]=params[idx]+1j*params[idx+1]; H[j,i]=np.conj(H[i,j]); idx+=2
    return H
def nparams(d): return d*d
def build(params,ints):
    G={}; idx=0
    for m in ms:
        M=np.zeros((q*q,q*q),complex)
        for p in range(q):
            cl=classes[p]; d=len(cl)
            U=expm(1j*herm(params[idx:idx+nparams(d)],d)); idx+=nparams(d)
            blk=lift(m*p)*np.eye(d)+U@np.diag(ints[m][p])@U.conj().T
            M[np.ix_(cl,cl)]=blk
        G[m]=M
    return G
I=np.eye(q)
def loss(params,ints):
    G=build(params,ints); s=0.0
    for a in ms:
        for b in ms:
            A=np.kron(G[a],I); B=np.kron(I,G[b]); C=A@B-B@A; s+=np.vdot(C,C).real
    return s
def offdiag(G): return max(np.abs(M-np.diag(np.diag(M))).max() for M in G.values())
P=sum(nparams(len(classes[p])) for p in range(q))*len(ms)
best=[]
for t in range(trials):
    ints={m:{p:rng.integers(-1,2,size=len(classes[p])) for p in range(q)} for m in ms}
    if all(len(set(ints[m][p]))==1 for m in ms for p in range(q)): continue
    x0=rng.normal(scale=1.0,size=P)
    r=minimize(loss,x0,args=(ints,),method='BFGS',options={'maxiter':3000,'gtol':1e-12})
    G=build(r.x,ints)
    best.append((r.fun,offdiag(G)))
    if r.fun<1e-14 and offdiag(G)>1e-4:
        print("FOUND", t, r.fun, offdiag(G)); np.save(f"./found_q{q}_s{seed}_t{t}.npy", r.x); 
        import json; json.dump({str(m):{str(p):ints[m][p].tolist() for p in range(q)} for m in ms}, open(f"./found_q{q}_s{seed}_t{t}.json","w"))
best.sort()
print("min losses:", [f"{a:.2e}/{b:.2e}" for a,b in best[:8]])
