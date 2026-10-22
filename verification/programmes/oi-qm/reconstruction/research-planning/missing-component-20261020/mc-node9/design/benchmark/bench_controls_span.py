"""Exact local-tomography diagnostic for the benchmark's control rows (premise L4).
For a two-system theory, compare the real span of product effects with the real dimension of the
joint Hermitian operators the theory's states occupy. Integer arithmetic only; complex entries are
pairs (re, im); a Hermitian matrix is flattened to its real and imaginary parts."""
from itertools import product
I=[[(1,0),(0,0)],[(0,0),(1,0)]]; X=[[(0,0),(1,0)],[(1,0),(0,0)]]
Y=[[(0,0),(0,-1)],[(0,1),(0,0)]]; Z=[[(1,0),(0,0)],[(0,0),(-1,0)]]
def cm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def kron(A,B): return [[cm(A[i//2][j//2],B[i%2][j%2]) for j in range(4)] for i in range(4)]
def flat(M): return [x for r in M for e in r for x in e]
def rank(rows):
    from fractions import Fraction as F
    m=[[F(x) for x in r] for r in rows]; rk=0; cols=len(m[0]) if m else 0
    for c in range(cols):
        p=next((i for i in range(rk,len(m)) if m[i][c]!=0),None)
        if p is None: continue
        m[rk],m[p]=m[p],m[rk]
        for i in range(len(m)):
            if i!=rk and m[i][c]!=0:
                f=m[i][c]/m[rk][c]; m[i]=[a-f*b for a,b in zip(m[i],m[rk])]
        rk+=1
    return rk
rows=[]
cases={
 'complex qubit (local effects I,X,Y,Z)':        ([I,X,Y,Z],16),
 'qubit stabilizer theory (Pauli effects)':      ([I,X,Y,Z],16),
 'real qubit / rebit (local effects I,X,Z)':     ([I,X,Z],10),
 'real Clifford class (test-8 N2; I,X,Z)':       ([I,X,Z],10),
}
for name,(loc,joint_dim) in cases.items():
    r=rank([flat(kron(A,B)) for A,B in product(loc,repeat=2)])
    verdict='holds' if r==joint_dim else 'fails (product span %d < joint %d)'%(r,joint_dim)
    print('%-44s product-effect span %2d, joint state dimension %2d: L4 %s'%(name,r,joint_dim,verdict))
# joint dimension for the real theories: real symmetric 4x4 matrices = 10 (contains Y(x)Y, which is real)
YY=kron(Y,Y); assert all(e[1]==0 for r_ in YY for e in r_)
print('Y(x)Y is a real symmetric matrix outside the real product span:',
      rank([flat(kron(A,B)) for A,B in product([I,X,Z],repeat=2)]+[flat(YY)])==10)
