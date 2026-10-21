"""Coordinator checks for owner report 4, written without importing the report's checker.
Integer / Fraction arithmetic only."""
from fractions import Fraction as F
from itertools import product

# 1. Six-qubit preparation (a,b,c,t,w,f) from a state vector, amplitudes scaled by sqrt(8).
amp={}
for a,b,c in product((0,1),repeat=3):
    t=a^(b&c); w=a&b; f=w&c; w^=a&b          # CNOT a->t; Toffoli b,c->t; Toffoli a,b->w; Toffoli w,c->f; uncompute w
    amp[(a,b,c,t,w,f)]=amp.get((a,b,c,t,w,f),0)+1
assert all(k[4]==0 for k in amp)                 # work qubit clean
# select f=0, project a,b,c on |+++> (adds a further 1/sqrt(8)): target amplitudes over 8
tgt=[sum(v for k,v in amp.items() if k[5]==0 and k[3]==t) for t in (0,1)]
print('target numerators over 8:',tgt,' success:',F(tgt[0]**2+tgt[1]**2,64))
# control: no uncompute of w -> w = ab stays entangled
amp2={}
for a,b,c in product((0,1),repeat=3):
    t=a^(b&c); w=a&b; f=w&c
    amp2[(a,b,c,t,w,f)]=1
rho=[[0,0],[0,0]]
for w in (0,1):
    vec=[sum(v for k,v in amp2.items() if k[5]==0 and k[3]==t and k[4]==w) for t in (0,1)]
    for i in (0,1):
        for j in (0,1): rho[i][j]+=vec[i]*vec[j]
print('omit-uncompute target numerators:',rho,' success:',F(rho[0][0]+rho[1][1],64))

# 2. Stabilizer octahedron: closest point to (24/25,0,-7/25) by KKT on the face x - z = 1 (x>=0, z<=0).
r=(F(24,25),F(0),F(-7,25)); n=(1,0,-1)
lam=(r[0]-r[2]-1)/2
p=tuple(r[i]-lam*n[i] for i in range(3))
assert lam>0 and p[0]>=0 and p[2]<=0 and p[0]-p[2]==1 and p[1]==0
d2=sum((r[i]-p[i])**2 for i in range(3))
print('closest point',p,' Bloch dist^2',d2,' trace dist^2',d2/4)
# global check: the face's supporting inequality x - z <= 1 holds on all 6 vertices, so dist >= lam*|n|
verts=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
assert all(v[0]-v[2]<=1 for v in verts)

# 3. Injection Kraus: <+-| (3|0> I + 4|1> J)/5 with J = -iY = [[0,-1],[1,0]]
J=[[0,-1],[1,0]]; I=[[1,0],[0,1]]
for s in (1,-1):
    K=[[3*I[i][j]+s*4*J[i][j] for j in range(2)] for i in range(2)]
    print('branch',s,'5*sqrt2*Kraus =',K)

# 4. Nonlinear leapfrog -> Toffoli, by algebra replayed on all 64 inputs.
def F_(u): return (u[1]^u[2]^(u[1]&u[2]), u[0], u[0])
def L_(u): return (u[1]^u[2], u[0], u[0])
ok=0
for bits in product((0,1),repeat=6):
    u,v=bits[:3],bits[3:]
    U,V=tuple(x^y for x,y in zip(v,F_(u))),u            # phi
    U,V=V,U                                              # swap blocks
    V=tuple(x^y for x,y in zip(V,L_(U)))                 # undo linear shear
    ok+= (U==u and V==(v[0]^(u[1]&u[2]),v[1],v[2]))
print('Toffoli inputs passing:',ok)

# 5. PR program: a=r, b=r^xy.
E=lambda x,y: sum((-1)**((r)^(r^(x&y))) for r in (0,1))/F(2)
print('CHSH:',E(0,0)+E(0,1)+E(1,0)-E(1,1))
