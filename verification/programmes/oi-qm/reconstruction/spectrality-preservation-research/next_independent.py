"""Separate stdlib rational-complex certificate checker; no checker imports."""
from fractions import Fraction as F
from itertools import permutations, product


def z(a=0,b=0): return F(a),F(b)
def plus(a,b): return a[0]+b[0],a[1]+b[1]
def minus(a,b): return a[0]-b[0],a[1]-b[1]
def times(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def bar(a): return a[0],-a[1]
zero = z()
def mat(n): return [[zero for _ in range(n)] for _ in range(n)]
def identity(n): return [[z(int(i==j)) for j in range(n)] for i in range(n)]
def adj(x): return [[bar(x[j][i]) for j in range(len(x))] for i in range(len(x[0]))]
def trsp(x): return [list(col) for col in zip(*x)]
def mm(x,y):
    return [[sumz(times(x[i][k],y[k][j]) for k in range(len(y)))
             for j in range(len(y[0]))] for i in range(len(x))]
def sumz(seq):
    a=zero
    for b in seq: a=plus(a,b)
    return a
def add(x,y): return [[plus(a,b) for a,b in zip(r,t)] for r,t in zip(x,y)]
def scale(x,a): return [[times(z(a),b) for b in r] for r in x]
def kron(x,y):
    return [[times(x[i//len(y)][j//len(y[0])],y[i%len(y)][j%len(y[0])])
             for j in range(len(x[0])*len(y[0]))] for i in range(len(x)*len(y))]
def ad(u,x): return mm(mm(u,x),adj(u))
def gamma(x):
    y=mat(4)
    for a,b,c,d in product(range(2),repeat=4):
        y[2*a+d][2*c+b]=x[2*a+b][2*c+d]
    return y
def determinant(x):
    ans=zero
    for p in permutations(range(len(x))):
        term=z(-1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1)
        for i in range(len(p)): term=times(term,x[i][p[i]])
        ans=plus(ans,term)
    return ans
def proj(v): return [[times(a,bar(b)) for b in v] for a in v]
count=0
def require(ok,name):
    global count
    if not ok: raise AssertionError(name)
    count+=1

D=[[z(1),zero],[zero,z(F(3,5),F(4,5))]]
Db=[[bar(a) for a in r] for r in D]
A=[[z(F(3,5)),z(F(-4,5))],[z(F(4,5)),z(F(3,5))]]
L=kron(identity(2),D); Lb=kron(identity(2),Db)
U=kron(A,D); V=kron(A,Db)
S=mat(4)
for i,p in enumerate([0,2,1,3]): S[i][p]=z(1)
def phi(x): return add(scale(ad(L,x),F(5,8)),scale(x,F(3,8)))
require(mm(adj(U),U)==identity(4),'local unitary')
require(mm(S,S)==identity(4),'swap involution')
for i,j in product(range(4),repeat=2):
    X=mat(4); X[i][j]=z(1)
    require(gamma(gamma(X))==X,'transpose involution')
    require(gamma(ad(U,gamma(X)))==ad(V,X),'local covariance')
    require(gamma(ad(mm(U,S),gamma(X)))==ad(mm(V,S),trsp(X)),'swap covariance')
    require(gamma(phi(gamma(X)))==add(scale(ad(Lb,X),F(5,8)),scale(X,F(3,8))),
            'actual map covariance')

# An independent finite certificate for the symbolic subspace identity.
vectors=[[z(1),zero],[zero,z(1)],[z(1),z(1)],[z(1),z(0,1)]]
for x,y,r,t in product(vectors,repeat=4):
    M=[[plus(times(x[i],y[j]),times(r[i],t[j])) for j in range(2)] for i in range(2)]
    dx=minus(times(x[0],r[1]),times(x[1],r[0]))
    dy=minus(times(y[0],t[1]),times(y[1],t[0]))
    require(determinant(M)==times(dx,dy),'product-subspace identity')

for w in [[z(1),z(2),z(3),z(4,1)], [z(0,1),z(2,1),z(3,-1),z(-2,2)],
          [z(1),zero,zero,z(1)], [z(1),z(1),z(1),z(1)]]:
    d=minus(times(w[0],w[3]),times(w[1],w[2]))
    d2=times(d,bar(d))
    require(determinant(gamma(proj(w)))==times(z(-1),times(d2,d2)),
            'complex pure-projector partial-transpose determinant')
E=identity(4); E[3][3]=D[1][1]
p=[z(F(1,2))]*4
bad=gamma(ad(adj(E),proj(p)))
require(determinant(bad)==z(F(-1,400)),'entangling domain rejection')
require(mm(adj(E),E)==identity(4),'entangling tilt unitary')
for ms in [(F(1,4),)*4,(F(1),F(0),F(0),F(0)),(F(-2),F(3),F(1,7),F(-1,7))]:
    require(sum(ms)==1 and sum(2*m-1 for m in ms)==-2,'center normalization')
B=scale(proj([z(1),zero,zero,z(1)]),F(1,2))
out=phi(B)
require(determinant([[out[i][j] for j in (0,3)] for i in (0,3)])==z(F(3,64)),
        'quantum positive comparison')
require(determinant(gamma(B))==z(F(-1,16)),'Q3 inclusion gate')
for j in range(4):
    X=mat(4); X[j][j]=z(1)
    require(phi(X)==X,'classical actual-map comparison')
preimage=mm(adj(E),[[a] for a in p])
coefficient=[[preimage[2*i+j][0] for j in range(2)] for i in range(2)]
mutations=[gamma(ad(L,gamma(B)))!=ad(L,B),gamma(B)!=B,
           determinant(coefficient)!=zero,
           sum(scale(identity(4),F(1,2))[j][j][0] for j in range(4))!=1]
for i,bad_control in enumerate(mutations): require(bad_control,f'mutation {i+1}')
print(f'controls: {count}; mutations rejected: {len(mutations)}')
print('entangling phase product preimage determinant: -1/400')
print('four-outcome reflection pairing sum: -2')
print('certificate controls pass; generic SP implication remains open')
