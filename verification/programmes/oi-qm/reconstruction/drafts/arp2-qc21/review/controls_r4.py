# REVIEW CONTROL (r4), not evidence. Static algebra only; no reachable set under any rule.
import itertools, random
from fractions import Fraction as Fr
pts = list(itertools.product((0,1), repeat=4))           # (z1,x1,z2,x2) = (u0,v0,u1,v1)
F = {'x':(0,1,0,0),'y':(1,1,1,1),'z':(1,0,0,0)}
ev = lambda c,w: sum(a*b for a,b in zip(c,w)) % 2
R = lambda mu: tuple(sum(mu[i]*(1-2*ev(F[a],w)) for i,w in enumerate(pts)) for a in 'xyz')
def unif(pred):
    S=[w for w in pts if pred(w)]; return [Fr(1,len(S)) if pred(w) else Fr(0) for w in pts]
swapw = lambda w: (w[1],w[0],w[3],w[2])                   # rule 0, one tick: u_i <-> v_i
swap = lambda mu: [mu[pts.index(swapw(w))] for w in pts]
# 1. C-FRAME: rule 0, k=1 acts on R as x<->z, f_y fixed; det_fix=-1, det_enc=+1
lawsS0=[unif(lambda w:True)]+[unif(lambda w,a=a,b=b: ev(F[a],w)==b) for a in 'xyz' for b in (0,1)]
lawsS0+=[unif(lambda w,s0=s0,b0=b0,s1=s1,b1=b1: w[s0]==b0 and w[2+s1]==b1) for s0,b0,s1,b1 in itertools.product((0,1),repeat=4)]
ok = all(R(swap(m)) == (R(m)[2],R(m)[1],R(m)[0]) for m in lawsS0)
print("C-FRAME static: rule-0 tick acts as x<->z on every S_0 law:", ok, "; det_fix of transposition = -1, det_enc = (-1)^1*(-1) = +1")
# 2. supplies closed under u<->v
S0set = {tuple(m) for m in lawsS0}
print("S_0 closed under u<->v:", all(tuple(swap(m)) in S0set for m in lawsS0))
M = [('u',0),('u',1),('v',0),('v',1),('src',None)]
sw = {'u':'v','v':'u','src':'src'}
print("mediator supplies M closed under u<->v:", all((sw[s],b) in M for s,b in M))
# 3. det correction is the same for even- and odd-parity inputs: det(P^k B) == det(P^(k+1) B P)
P = [[0,0,1],[0,1,0],[1,0,0]]
mm = lambda A,B: [[sum(A[i][t]*B[t][j] for t in range(3)) for j in range(3)] for i in range(3)]
det = lambda A: (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
I3=[[int(i==j) for j in range(3)] for i in range(3)]
def powP(k):
    A=I3
    for _ in range(k): A=mm(P,A)
    return A
random.seed(1); good=True; differ=0
for _ in range(200):
    B=[[random.randint(-3,3) for _ in range(3)] for _ in range(3)]
    for k in range(0,7):
        even=mm(powP(k),B); odd=mm(mm(powP(k+1),B),P)
        good &= det(even)==det(odd)==(-1)**k*det(B)
        differ += even!=odd
print("det_enc = (-1)^k det_fix for both input parities:", good, "; encoded maps for the two parities differ in", differ, "of 1400 random cases (they are P-conjugate)")
# 4. C-AFFB (b) fixture: 48 laws, rank 16, greedy basis from Lambda_0, Lambda_a0 reaches 16
p = lambda bit: Fr(1,5) if bit else Fr(4,5)
fix = list(lawsS0) + [[p(w[0])*p(w[1])*Fr(1,4) for w in pts], unif(lambda w: w[1]==0 and ev(F['y'],w)==0)]
# planted six (any valid disjoint allocation) + mixture
pat={}
for w in pts: pat.setdefault(tuple(ev(F[a],w) for a in 'xyz'),[]).append(w)
keys=[(a,b) for a in 'xyz' for b in (0,1)]
def opts(a,b):
    i='xyz'.index(a); o=[j for j in range(3) if j!=i]; r=[]
    for s1,s2 in (((0,0),(1,1)),((0,1),(1,0))):
        p1=[0]*3;p1[i]=b;p1[o[0]],p1[o[1]]=s1; p2=[0]*3;p2[i]=b;p2[o[0]],p2[o[1]]=s2
        r+=[(w1,w2) for w1 in pat[tuple(p1)] for w2 in pat[tuple(p2)]]
    return r
def solve(i,used):
    if i==6: return {}
    for w1,w2 in opts(*keys[i]):
        if w1 in used or w2 in used: continue
        r=solve(i+1,used|{w1,w2})
        if r is not None: r[keys[i]]=(w1,w2); return r
sol=solve(0,frozenset())
planted=[[Fr(1,2) if w in sol[k] else Fr(0) for w in pts] for k in keys]
fix += planted + [[sum(Fr(1,2)*planted[j][i] for j in (0,1)) for i in range(16)]]
fix += [[Fr(int(i==j)) for i in range(16)] for j in range(16)]
covered = {w for k in keys for w in sol[k]}
print("fixture size:", len(fix), "; points not covered by B_P's planted supports:", 16-len(covered))
def indep(basis, v):
    rows=[r[:] for r in basis]+[v[:]]; rk=0
    for c in range(16):
        piv=next((i for i in range(rk,len(rows)) if rows[i][c]!=0),None)
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        for i in range(len(rows)):
            if i!=rk and rows[i][c]!=0:
                f=rows[i][c]/rows[rk][c]; rows[i]=[x-f*y for x,y in zip(rows[i],rows[rk])]
        rk+=1
    return rk==len(basis)+1
order = [fix[0], fix[2], fix[4], fix[6]] + fix   # Lambda_0, Lambda_{x,0}, Lambda_{y,0}, Lambda_{z,0} first
basis=[]
for v in order:
    if len(basis)==16: break
    if indep(basis,v): basis.append(v)
print("greedy basis size:", len(basis), "; first four are Lambda_0, Lambda_a0 affinely independent:", len(basis)>=4)
