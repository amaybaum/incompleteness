"""Independent reviewer engine (no import of g1lib or coordinator code). Exact integer/Fraction arithmetic.
QM side: stabilizer groups (signed real Paulis) with conjugation tables derived from integer matrices.
Card side: explicit probability distributions over ontic (qA,pA,qB,pB)."""
from fractions import Fraction as F
from collections import deque
from itertools import product

# ---------- integer matrices ----------
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def tr(A): return tuple(zip(*A))
def kr(A,B):
    n,m=len(A),len(B)
    return tuple(tuple(A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)) for i in range(n*m))
def sc(A,c): return tuple(tuple(c*x for x in r) for r in A)
I1=((1,0),(0,1)); X1=((0,1),(1,0)); Z1=((1,0),(0,-1)); XZ1=mm(X1,Z1); H1=((1,1),(1,-1))
P1=[I1,X1,Z1,XZ1]; NM=['I','X','Z','XZ']
PAULI=[kr(a,b) for a in P1 for b in P1]       # index 4*a+b, a on A, b on B
CN=((1,0,0,0),(0,1,0,0),(0,0,0,1),(0,0,1,0))  # basis 2*bA+bB, control A
I4=kr(I1,I1)
def ident(M):
    """M = s * PAULI[k] ; return (s,k)"""
    for k,P in enumerate(PAULI):
        for s in (1,-1):
            if M==sc(P,s): return (s,k)
    raise ValueError
# Pauli product table: P_i P_j = s P_k
PMUL={(i,j):ident(mm(PAULI[i],PAULI[j])) for i in range(16) for j in range(16)}
def comm(i,j): return PMUL[(i,j)][1]==PMUL[(j,i)][1] and PMUL[(i,j)][0]==PMUL[(j,i)][0]
def conj_table(M,c):
    """U = M/sqrt(c) real orthogonal: U P U^T = M P M^T / c"""
    t={}
    for k,P in enumerate(PAULI):
        R=mm(mm(M,P),tr(M)); assert all(x%c==0 for r in R for x in r)
        t[k]=ident(tuple(tuple(x//c for x in r) for r in R))
    return t
HA=kr(H1,I1); HB=kr(I1,H1)
def lift_tables(a,b,c):
    return {'sA':conj_table(mm(PAULI[a],HA),2),'sB':conj_table(mm(PAULI[b],HB),2),'c':conj_table(mm(PAULI[c],CN),1)}
FLIPS={'xA':conj_table(PAULI[4],1),'zA':conj_table(PAULI[8],1),'xB':conj_table(PAULI[1],1),'zB':conj_table(PAULI[2],1)}
ZA,ZB=8,2
def gmul(g,h):
    s,k=PMUL[(g[1],h[1])]; return (g[0]*h[0]*s,k)
def closure(gens):
    S={(1,0)}|set(gens); ch=True
    while ch:
        ch=False
        for g in list(S):
            for h in list(S):
                k=gmul(g,h)
                if k not in S: S.add(k); ch=True
    return frozenset(S)
QM0=closure([(1,ZA),(1,ZB)])
class QM:
    def __init__(self,tables): self.T=dict(tables); self.T.update(FLIPS)
    def init(self): return QM0
    def gate(self,op,S):
        t=self.T[op]; return frozenset((s*t[k][0],t[k][1]) for s,k in S)
    def read(self,op,S):
        z=ZA if op=='rA' else ZB
        if (1,z) in S: return {0:(F(1),S)}
        if (-1,z) in S: return {1:(F(1),S)}
        keep=[g for g in S if comm(g[1],z)]
        return {o:(F(1,2),closure(keep+[((-1)**o,z)])) for o in (0,1)}
class Cards:
    def init(self): return frozenset({((0,a,0,b),F(1,4)) for a in (0,1) for b in (0,1)})
    def gate(self,op,D):
        out={}
        for (qA,pA,qB,pB),w in D:
            s={'sA':(pA,qA,qB,pB),'sB':(qA,pA,pB,qB),'c':(qA,pA^pB,qB^qA,pB),
               'xA':(qA^1,pA,qB,pB),'zA':(qA,pA^1,qB,pB),'xB':(qA,pA,qB^1,pB),'zB':(qA,pA,qB,pB^1)}[op]
            out[s]=out.get(s,0)+w
        return frozenset(out.items())
    def read(self,op,D):
        j=0 if op=='rA' else 2
        res={}
        for s,w in D:
            o=s[j]; d=res.setdefault(o,{})
            for f in (0,1):
                t=list(s); t[j+1]=f; t=tuple(t); d[t]=d.get(t,0)+w/2
        out={}
        for o,d in res.items():
            p=sum(d.values()); out[o]=(p,frozenset((s,v/p) for s,v in d.items()))
        return out
def isread(op): return op[0]=='r'
def first_disagreement(T1,T2,alphabet,maxdepth=None,extra=None):
    """Exact: length of the shortest word over `alphabet` whose joint record distribution differs, or None.
    Pair-BFS over conditioned states; a word of length d+1 is distinguishing iff a pair reached at depth d
    has differing conditional outcome probabilities for its last read.
    extra: optional (init, step(op,x)->x or None) automaton restricting admissible words (None = forbidden)."""
    x0=extra[0] if extra else 0
    start=(T1.init(),T2.init(),x0); seen={start}; Q=deque([(start,0)])
    while Q:
        (a,b,x),d=Q.popleft()
        if maxdepth is not None and d>=maxdepth: continue
        for op in alphabet:
            if extra:
                x2=extra[1](op,x)
                if x2 is None: continue
            else: x2=0
            if isread(op):
                ra,rb=T1.read(op,a),T2.read(op,b)
                if {o:p for o,(p,_) in ra.items()}!={o:p for o,(p,_) in rb.items()}: return d+1
                nxt=[(ra[o][1],rb[o][1],x2) for o in ra]
            else: nxt=[(T1.gate(op,a),T2.gate(op,b),x2)]
            for k in nxt:
                if k not in seen: seen.add(k); Q.append((k,d+1))
    return None
FULL=['sA','sB','c','xA','zA','xB','zB','rA','rB']
TRIPLES=list(product(range(16),repeat=3))
