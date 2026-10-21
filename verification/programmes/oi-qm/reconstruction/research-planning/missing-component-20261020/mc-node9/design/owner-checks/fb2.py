import itertools, numpy as np
# (5) card version: (qA,pA,qB,pB); swapA; coupling qB^=qA, pA^=pB
res=set()
for pA,pB in itertools.product((0,1),repeat=2):
    qA,qB=0,0
    for _ in range(3):
        qA,pA=pA,qA
        qB^=qA; pA^=pB
    res.add(qB)
print('(5) card final q_B values:',res)
I=np.eye(2); H=np.array([[1,1],[1,-1]])/np.sqrt(2); X=np.array([[0,1],[1,0]]); Z=np.diag([1,-1])
CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
U=CNOT@np.kron(H,I); U3=np.linalg.matrix_power(U,3)
psi=U3@np.array([1,0,0,0])
pB1=sum(abs(psi[i])**2 for i in (1,3))
print('(5) QM P(Z_B=1) =',round(pB1,12),'; U3^dag Z_B U3 == -Z_A Z_B:',np.allclose(U3.conj().T@np.kron(I,Z)@U3,-np.kron(Z,Z)))
# (5b) seven ops: add final swap A (=H_A): card returns to start? QM P(Z_B=1)
psi7=np.kron(H,I)@psi; print('(5b) QM after extra H_A, P(Z_B=1)=',round(sum(abs(psi7[i])**2 for i in (1,3)),12))
# (6) reachable states with H_A,H_B,CNOT_AB,X_A,X_B and Z-measurement post-states (both qubits), from |00>
gates=[np.kron(H,I),np.kron(I,H),CNOT,np.kron(X,I),np.kron(I,X)]
P0A=np.kron(np.diag([1,0]),I);P1A=np.kron(np.diag([0,1]),I);P0B=np.kron(I,np.diag([1,0]));P1B=np.kron(I,np.diag([0,1]))
def key(v):
    v=v/np.linalg.norm(v); k=next(i for i in range(4) if abs(v[i])>1e-9); v=v*abs(v[k])/v[k]
    return tuple(np.round(v,9))
start=np.array([1,0,0,0],dtype=complex); seen={key(start):start}; frontier=[start]
while frontier:
    nf=[]
    for s in frontier:
        outs=[g@s for g in gates]+[P@s for P in (P0A,P1A,P0B,P1B)]
        for o in outs:
            if np.linalg.norm(o)<1e-9: continue
            k=key(o)
            if k not in seen: seen[k]=o/np.linalg.norm(o); nf.append(seen[k])
    frontier=nf
def red(v):  # reduced state of A
    m=v.reshape(2,2); return m@m.conj().T
mm=sum(1 for v in seen.values() if np.allclose(red(v),I/2))
print('(6) reachable pure states',len(seen),'with both marginals maximally mixed',mm)
vals=set()
for v in seen.values():
    r=red(v)
    for O in (Z,X,np.array([[0,-1j],[1j,0]])): vals.add(round(float(np.real(np.trace(r@O))),9))
print('(6b) single-qubit Bloch components over the 24 reachable states:',sorted(vals))
