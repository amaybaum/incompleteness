#!/usr/bin/env python3
"""Main §2.4 — minimal explicit model: exact verification by enumeration.
Visible x∈{0,1}, hidden h∈{1..6}; involution σ per the paper. Checks:
  (1) T(1,0) = [[2/3,1/3],[1/3,2/3]]
  (2) T(2,0) = I  (σ² = id: complete un-mixing; Markov would give [[5/9,4/9],[4/9,5/9]])
  (3) Λ(2,1) = T(2,0)·T(1,0)^{-1} has negative entries  => P-INDIVISIBLE
  (4) process-tensor check (no invertibility needed): P(x₂=0|x₁=1,x₀=0)=1 vs P(x₂=0|x₁=1)=1/3
"""
import numpy as np, itertools
S=[(x,h) for x in (0,1) for h in range(1,7)]
pairs=[((0,1),(1,1)),((0,2),(1,2)),((0,3),(0,4)),((0,5),(0,6)),((1,3),(1,4)),((1,5),(1,6))]
sig={}
for a,b in pairs: sig[a]=b; sig[b]=a
assert all(sig[sig[s]]==s for s in S)                       # involution
def T(t):
    M=np.zeros((2,2))
    for x0 in (0,1):
        for h in range(1,7):
            s=(x0,h)
            for _ in range(t): s=sig[s]
            M[s[0],x0]+=1/6
    return M
T1,T2=T(1),T(2)
ok1=np.allclose(T1,[[2/3,1/3],[1/3,2/3]]); ok2=np.allclose(T2,np.eye(2))
L21=T2@np.linalg.inv(T1)
ok3=(L21<-1e-12).any() and np.allclose(L21,[[2,-1],[-1,2]])
print(f"(1) T(1,0)=[[2/3,1/3],[1/3,2/3]]        -> {'PASS' if ok1 else 'FAIL'}")
print(f"(2) T(2,0)=I (un-mixing)                -> {'PASS' if ok2 else 'FAIL'}")
print(f"(3) Λ(2,1)={L21.tolist()} negative entries -> {'PASS: P-INDIVISIBLE' if ok3 else 'FAIL'}")
# (4) multi-time conditionals by exact enumeration, x0 uniform over {0,1}, h uniform
traj={}
for x0,h in S:
    s=(x0,h); path=[s[0]]
    for _ in range(2): s=sig[s]; path.append(s[0])
    traj[(x0,h)]=path
num_a=sum(1 for k,p in traj.items() if p[0]==0 and p[1]==1 and p[2]==0)
den_a=sum(1 for k,p in traj.items() if p[0]==0 and p[1]==1)
num_b=sum(1 for k,p in traj.items() if p[1]==1 and p[2]==0)
den_b=sum(1 for k,p in traj.items() if p[1]==1)
ok4=(num_a/den_a==1.0) and abs(num_b/den_b-1/3)<1e-12
print(f"(4) P(x2=0|x1=1,x0=0)={num_a/den_a} vs P(x2=0|x1=1)={num_b/den_b:.4f} -> {'PASS: memory effect' if ok4 else 'FAIL'}")
print("ALL PASS" if all([ok1,ok2,ok3,ok4]) else "FAILURE")
