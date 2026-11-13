# Reviewer probe r7 (exact; controls, not evidence). Two checks.
# (1) Stabilizer QM under P's protocol: path qubit S (|+> or |0>,|1>), phase Z^phi, an "arm" interaction with an
#     environment E, then an X read of S (port 0 = '+'). V from the two phases; D = trace distance of E's state
#     given path |0> vs |1>. Arms: off; CNOT marker; null sham (X on E only); kick-matched sham with classical
#     noise (E holds w, S gets Z^w); purified dephasing (E in |+>, CZ). Also the S-channel each arm induces.
# (2) C-R60-ODD: the fixed-slot linear part P*R60 (P = x<->z) and R60 itself: characteristic polynomials.
from fractions import Fraction as F
import itertools, math
def kron(A,B):
    n,m=len(A),len(B); return [[A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)] for i in range(n*m)]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def T(A): return [list(r) for r in zip(*A)]
def outer(v): return [[a*b for b in v] for a in v]
I2=[[1,0],[0,1]]; X=[[0,1],[1,0]]; Z=[[1,0],[0,-1]]
CNOT=[[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]        # control S (first), target E
CZ=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,-1]]
h=F(1,2)
def rho_path(src):
    return {'X+':[[h,h],[h,h]],'Z+':[[1,0],[0,0]],'Z-':[[0,0],[0,1]]}[src]
def run(src,phi,arm):
    s=rho_path(src)
    if phi: s=mm(mm(Z,s),Z)
    if arm=='off':      e=[[1,0],[0,0]]; U=kron(I2,I2); rho=mm(mm(U,kron(s,e)),T(U))
    elif arm=='cnot':   e=[[1,0],[0,0]]; rho=mm(mm(CNOT,kron(s,e)),T(CNOT))
    elif arm=='null':   e=[[1,0],[0,0]]; U=kron(I2,X); rho=mm(mm(U,kron(s,e)),T(U))
    elif arm=='noise':  # classical noise bit w recorded in E; S gets Z^w
        rho=[[0]*4 for _ in range(4)]
        for w in (0,1):
            sw=mm(mm(Z,s),Z) if w else s
            ew=[[1,0],[0,0]] if w==0 else [[0,0],[0,1]]
            t=kron(sw,ew); rho=[[rho[i][j]+h*t[i][j] for j in range(4)] for i in range(4)]
    elif arm=='cz+':    e=[[h,h],[h,h]]; rho=mm(mm(CZ,kron(s,e)),T(CZ))
    return rho
def ptrace_E(rho): return [[rho[2*i][2*j]+rho[2*i+1][2*j+1] for j in range(2)] for i in range(2)]   # -> S
def ptrace_S(rho): return [[rho[i][j]+rho[2+i][2+j] for j in range(2)] for i in range(2)]           # -> E
def p_plus(s): return (s[0][0]+s[0][1]+s[1][0]+s[1][1])/2
def tdist(a,b):
    d=[[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]   # real symmetric, traceless
    q=d[0][0]**2+d[0][1]**2; r=math.isqrt(q.numerator)
    return F(r,math.isqrt(q.denominator)) if r*r==q.numerator else ('sqrt',q)
for arm in ('off','cnot','null','noise','cz+'):
    V=abs(p_plus(ptrace_E(run('X+',0,arm)))-p_plus(ptrace_E(run('X+',1,arm))))
    D=tdist(ptrace_S(run('Z+',0,arm)),ptrace_S(run('Z-',0,arm)))
    chan=ptrace_E(run('X+',0,arm))
    print(f"{arm:6s} V={V} D={D}  S-state after arm (X+ input)={[[str(x) for x in r] for r in chan]}")
# (2) C-R60-ODD
R60=[[F(2,3),F(-1,3),F(2,3)],[F(2,3),F(2,3),F(-1,3)],[F(-1,3),F(2,3),F(2,3)]]   # 60 deg about (1,1,1)
P=[[0,0,1],[0,1,0],[1,0,0]]
def charpoly(A):  # lambda^3 - tr lambda^2 + c2 lambda - det
    tr=sum(A[i][i] for i in range(3))
    c2=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i,j in ((0,1),(0,2),(1,2)))
    det=(A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
    return [1,-tr,c2,-det]
print('R60 orthogonal:', mm(R60,T(R60))==[[1,0,0],[0,1,0],[0,0,1]], 'charpoly', [str(c) for c in charpoly(R60)], '(= (l-1)(l^2-l+1): {1, e^{+-i pi/3}})')
PR=mm(P,R60)
print('P*R60 charpoly', [str(c) for c in charpoly(PR)], '(= (l+1)(l-1)^2: {-1,1,1}, a signed-permutation spectrum: fixed frame alone misses)')
