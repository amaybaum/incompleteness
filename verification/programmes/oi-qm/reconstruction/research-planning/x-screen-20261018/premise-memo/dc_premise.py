# Design-evidence sanity checks for PREMISE-MEMO.md (not a probe of any screen).
# Exact arithmetic only (SymPy Rational / I). Prints PASS/FAIL lines.
import sympy as sp
from sympy import Rational as R, I, Matrix, eye, zeros, sqrt, symbols, conjugate, simplify
def ket(*v): return Matrix(v)
def proj(v): return v*v.H
def kron(A,B): return sp.kronecker_product(A,B)
P0=Matrix([[1,0],[0,0]]); P1=Matrix([[0,0],[0,1]]); X=Matrix([[0,1],[1,0]])
CN=kron(P0,eye(2))+kron(P1,X)
def Gam(M):  # partial transpose on token 2, basis index 2i+j
    N=zeros(4,4)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    N[2*i+j,2*k+l]=M[2*i+l,2*k+j]
    return N
def even(M): return Matrix([[M[0,0],M[0,3]],[M[3,0],M[3,3]]])
def ok(name,c): print(("PASS " if c else "FAIL ")+name)
# 1. CN(a x P0)CN = sum a_ij |ii><jj| for generic Hermitian a
a00,a11=symbols('a00 a11',real=True); x,y=symbols('x y',real=True)
a=Matrix([[a00,x+I*y],[x-I*y,a11]])
G=CN*kron(a,P0)*CN.H
T=zeros(4,4); T[0,0]=a00; T[0,3]=x+I*y; T[3,0]=x-I*y; T[3,3]=a11
ok("CN(a(x)P0)CN = sum a_ij |ii><jj|", simplify(G-T)==zeros(4,4))
# 2. OV-ready pairing identity: Tr[CN(a(x)P0)CN X] = Tr[a * even(X)^T]
Xs=Matrix(4,4,lambda r,c: symbols(f'm{r}{c}'))
ok("Tr[G X] = Tr[a even(X)]", sp.expand((G*Xs).trace()-(a*even(Xs)).trace())==0)
ok("mutation: transposed form is NOT the identity", sp.expand((G*Xs).trace()-(a*even(Xs).T).trace())!=0)
B=proj(ket(1,0,0,1))/2; Ps=proj(ket(0,1,-1,0))/2
ok("B = CN(|+><+| (x) P0)CN", CN*kron(proj(ket(1,1))/2,P0)*CN.H==B)
# 3. Gamma(Q3) witness: Gamma(P_singlet) even block eigenvalues +-1/2; Tr(B Gamma(Ps)) = -1/2
ev=even(Gam(Ps)).eigenvals()
ok("even(Gamma(Ps)) eigenvalues {1/2,-1/2}", set(ev)=={R(1,2),R(-1,2)})
ok("Tr(B Gamma(Ps)) = -1/2", (B*Gam(Ps)).trace()==R(-1,2))
ok("Gamma(B) has eigenvalue -1/2 (B not in Gamma(Q3))", R(-1,2) in Gam(B).eigenvals())
# 4. K(Z_F) defects z = I/2 - P_m, m=(1,b,-bd,d)/2: even block PSD (eigs {0,1/2}); Tr(P_m z) = -1/2
allpsd=True; allneg=True; dets=[]
def Tcorr(M):
    S=[X,Matrix([[0,-I],[I,0]]),Matrix([[1,0],[0,-1]])]
    return Matrix(3,3,lambda i,j: sp.simplify((kron(S[i],S[j])*M).trace()))
for b in (1,-1):
    for d in (1,-1):
        m=ket(1,b,-b*d,d)/2; z=eye(4)/2-proj(m)
        e=even(z).eigenvals(); allpsd&= set(e)<= {0,R(1,2)} and all(k>=0 for k in e)
        allneg&= (proj(m)*z).trace()==R(-1,2)
        Tz=Tcorr(z); Tm=Tcorr(proj(m)); dets.append((Tm.det(),Tz.det(), Tz*Tz.T==eye(3)))
ok("defects: even block PSD", allpsd)
ok("defects: Tr(P_m z) = -1/2 (ME-valid excludes K(Z_F))", allneg)
ok("defects: T(m) det -1, T(z) orthogonal with det +1", all(dm==-1 and dz==1 and o for dm,dz,o in dets))
# 5. chirality: T(B)=diag(1,-1,1), T(Gamma(B))=I, T(singlet)=-I
ok("T(B)=diag(1,-1,1)", Tcorr(B)==sp.diag(1,-1,1))
ok("T(Gamma(B))=I (det +1)", Tcorr(Gam(B))==eye(3))
ok("T(singlet)=-I (det -1)", Tcorr(Ps)==-eye(3))
# 6. K_Gamma = Q3 + R+ Gamma(B): even(Gamma(B)) = I/2 (OV-ready holds on generator)
ok("even(Gamma(B)) = I/2", even(Gam(B))==eye(2)/2)
# 7. ME-valid does not imply OV-ready: X = I/2 - c P_v, v=(4|00>+|11>)/sqrt17, c=53/100
v=ket(4,0,0,1); Pv=proj(v)/17; c=R(53,100); Xc=eye(4)/2-c*Pv
ok("X not PSD (min eig 1/2-c<0)", min(Xc.eigenvals())==R(1,2)-c)
ok("product bound 1/2-c*16/17 > 0 (block positivity via Schmidt [W])", R(1,2)-c*R(16,17)>0)
ok("ME bound 1/2-c*25/34 > 0 (ME-validity via Schmidt [W])", R(1,2)-c*R(25,34)>0)
ok("ME maximizer: |<Phi+|v>|^2 = 25/34", (proj(ket(1,0,0,1))/2*Pv).trace()==R(25,34))
ok("Tr(P_v X) < 0 with P_v in G (fails OV-ready)", (Pv*Xc).trace()<0)
# 8. countercontrol: OV-ready test must NOT exclude Q3 generators / products
ok("even block of B PSD", all(k>=0 for k in even(B).eigenvals()))
ok("countercontrol: identity map in place of Gamma gives no witness", all(k>=0 for k in even(Ps).eigenvals()))
# 9. UPD (both native readout outcomes): conditional token state = even / odd parity block
def odd(M): return Matrix([[M[1,1],M[1,2]],[M[2,1],M[2,2]]])
def cond(M,k):  # Tr_2[(I x P_k) CN M CN], as a 2x2 matrix on token 1
    Y=CN*M*CN.H; Pk=[P0,P1][k]; Z=kron(eye(2),Pk)*Y
    return Matrix(2,2,lambda i,j: sum(Z[2*i+t,2*j+t] for t in range(2)))
ok("cond(X,0) = even(X)", simplify(cond(Xs,0)-even(Xs))==zeros(2,2))
odd_perm=Matrix([[Xs[2,2],Xs[2,1]],[Xs[1,2],Xs[1,1]]])  # outcome 1: |i,1> -> |i,1-i> : configurations 10 (i=1? ) ordered by i
ok("cond(X,1) = odd block (configs 01,10, ordered by control)", simplify(cond(Xs,1)-Matrix([[Xs[1,1],Xs[1,2]],[Xs[2,1],Xs[2,2]]]))==zeros(2,2))
okodd=True
for b in (1,-1):
    for d in (1,-1):
        m=ket(1,b,-b*d,d)/2; z=eye(4)/2-proj(m)
        okodd&= all(k>=0 for k in odd(z).eigenvals())
ok("defects: odd block PSD (K(Z_F) satisfies UPD)", okodd)
ok("Gamma(B) odd block eigenvalues {1/2,-1/2} (UPD excludes K_Gamma)", set(odd(Gam(B)).eigenvals())=={R(1,2),R(-1,2)})
ok("X_c even block min eigenvalue 1/2-c < 0", min(even(Xc).eigenvals())==R(1,2)-c)
# 10. drop-one control: with Gamma re-identification of CNOT, Gamma(Q3) satisfies UPD:
#     Tr_2[(I x P_k) Gamma(Y)] = Tr_2[(I x P_k) Y] for diagonal P_k
def tr2k(M,k):
    Pk=[P0,P1][k]; Z=kron(eye(2),Pk)*M
    return Matrix(2,2,lambda i,j: sum(Z[2*i+t,2*j+t] for t in range(2)))
ok("Tr_2[(I x P_k)Gamma(Y)] = Tr_2[(I x P_k)Y]", all(simplify(tr2k(Gam(Xs),k)-tr2k(Xs,k))==zeros(2,2) for k in (0,1)))
