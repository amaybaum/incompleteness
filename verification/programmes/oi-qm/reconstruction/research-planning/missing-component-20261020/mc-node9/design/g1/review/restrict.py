"""Reviewer check (exact; lift algebra only, no n=3 word or distribution is computed).
Claim tested: among the n=3 B1-local tuples (sA,sB,sC,cAB,cBC), those whose AB-restriction (sA,sB,cAB) and
BC-restriction (sB,sC,cBC) both lie in the n=2 QM class {Ad(W) std Ad(W)^-1 : W in <Z_A,Z_B>} (d_witness.out,
review/exact_e.out) are exactly the 8 conjugates Ad(W) std3 Ad(W)^-1, W in <Z_A,Z_B,Z_C>."""
from itertools import product
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lifts_b1 import make, enumerate_lifts
def key(table,n,bits):
    # restriction of a lift table to the subgroup on `bits` (list of system indices), relabelled to 0..len-1
    m=len(bits); out=[]
    for k,x,z in sorted(table):
        if any(((x>>j)&1 or (z>>j)&1) for j in range(n) if j not in bits): continue
        if k not in (0,2): continue
        kk,xx,zz=table[(k,x,z)]
        def rl(v): return sum(((v>>b)&1)<<i for i,b in enumerate(bits))
        assert all(not((xx>>j)&1 or (zz>>j)&1) for j in range(n) if j not in bits), 'not local'
        out.append(((k,rl(x),rl(z)),(kk,rl(xx),rl(zz))))
    return tuple(out)
def std_table(n,op,mul,elems):
    gens=[(0,1<<j,0) for j in range(n)]+[(0,0,1<<j) for j in range(n)]
    from lifts_b1 import cardmap
    f=cardmap(n,op)
    img=[(0,)+f(g[1],g[2]) for g in gens]
    def phi(e):
        k,x,z=e; r=(k,0,0)
        for j in range(n):
            if (x>>j)&1: r=mul(r,img[j])
        for j in range(n):
            if (z>>j)&1: r=mul(r,img[n+j])
        return r
    return {e:phi(e) for e in elems}
def conjW(table,W,mul,elems):
    # Ad(W) o L o Ad(W)^-1 ; W a Z-type Pauli (0,0,zw), self-inverse up to sign
    def ad(e): return mul(mul(W,e),W)  # W^-1 = W for Z-type real Pauli (W^2=1)
    return {e:ad(table[ad(e)]) for e in elems}
C=2
# n=2 QM class
mul2,el2=make(2,C)
ops2=[('s',0),('s',1),('c',0,1)]
std2={op:std_table(2,op,mul2,el2) for op in ops2}
qm2=set()
for zw in range(4):
    W=(0,0,zw)
    qm2.add(tuple(key(conjW(std2[op],W,mul2,el2),2,[0,1]) for op in ops2))
print('n=2 QM class size (Z-frame conjugates):',len(qm2))
# n=3 local lifts
mul3,el3=make(3,C)
ops3=[('s',0),('s',1),('s',2),('c',0,1),('c',1,2)]
loc={}
for op in ops3:
    _,_,lifts=enumerate_lifts(3,C,op)
    touched={op[1]} if op[0]=='s' else {op[1],op[2]}
    loc[op]=[t for t,inv in lifts if all(t[e]==e for e in el3 if not any(((e[1]>>j)&1 or (e[2]>>j)&1) for j in touched))]
    print(op,'local lifts',len(loc[op]))
AB=[0,1]; BC=[1,2]
cnt=0; hits=[]
for sA,sB,sC,cAB,cBC in product(loc[('s',0)],loc[('s',1)],loc[('s',2)],loc[('c',0,1)],loc[('c',1,2)]):
    cnt+=1
    rab=(key(sA,3,AB),key(sB,3,AB),key(cAB,3,AB))
    if rab not in qm2: continue
    rbc=(key(sB,3,BC),key(sC,3,BC),key(cBC,3,BC))
    if rbc not in qm2: continue
    hits.append((sA,sB,sC,cAB,cBC))
print('n=3 local tuples enumerated:',cnt)
print('tuples with both 2-system restrictions in the n=2 QM class:',len(hits))
std3={op:std_table(3,op,mul3,el3) for op in ops3}
conj3=set()
for zw in range(8):
    W=(0,0,zw)
    conj3.add(tuple(tuple(sorted(conjW(std3[op],W,mul3,el3).items())) for op in ops3))
hs=set(tuple(tuple(sorted(t.items())) for t in h) for h in hits)
print('equal to the 8 Z-frame conjugates of std3:',hs==conj3,len(conj3))
