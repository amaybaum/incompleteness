from fractions import Fraction as Fr
import random, itertools
R = range(4)
# tables from CompositeDimension.lean (pc, pt, sgn)
pc = [[0,0,3,3],[1,1,2,2],[2,2,1,1],[3,3,0,0]]
pt = [[0,1,2,3],[1,0,3,2],[1,0,3,2],[0,1,2,3]]
def sgn(m,n): return -1 if (m==1 and n==3) or (m==2 and n==2) else 1
def cnot(w): return [[sgn(m,n)*w[pc[m][n]][pt[m][n]] for n in R] for m in R]
def hom(x): return [1]+list(x)
def prodState(x,y): hx,hy=hom(x),hom(y); return [[hx[m]*hy[n] for n in R] for m in R]
def tens(X,Y): return [[X[m]*Y[n] for n in R] for m in R]
reflYdiag=[1,1,-1,1]   # homMap reflY: (v0, v1, -v2, v3)
def actT_reflY(w): return [[w[m][n]*reflYdiag[n] for n in R] for m in R]
def actC_reflY(w): return [[w[m][n]*reflYdiag[m] for n in R] for m in R]
def cnotTw(w): return actT_reflY(cnot(actT_reflY(w)))
def tabMul(A,B): return [[sum(A[m][k]*B[k][n] for k in R) for n in R] for m in R]
def tabT(A): return [[A[n][m] for n in R] for m in R]
def ipW(E,X): return sum(E[m][n]*X[m][n] for m in R for n in R)
sgnY=[1,1,-1,1]
def transposeW(w): return [[sgnY[m]*sgnY[n]*w[m][n] for n in R] for m in R]
def dg(p,q,r,s): return [[p,0,0,0],[0,q,0,0],[0,0,r,0],[0,0,0,s]]
phiW=[[ (-1 if m==2 else 1) if m==n else 0 for n in R] for m in R]
idW=dg(1,1,1,1)
def sharpVec(b): return [Fr(1,2)]+[Fr(x)/2 for x in b]
def smul(k,w): return [[k*w[m][n] for n in R] for m in R]
xplus=[1,0,0]; z3=[0,0,1]; neg=lambda v:[-a for a in v]
def rnd(): return [[Fr(random.randint(-9,9),random.randint(1,5)) for n in R] for m in R]
ok=True
def chk(name,c):
    global ok
    print(('OK  ' if c else 'FAIL'),name); ok&=c
chk('phiW_eq_dg', phiW==dg(1,1,-1,1))
chk('cnot_prodState_xplus_z3 (base)', cnot(prodState(xplus,z3))==phiW)
chk('actT_reflY_phiW (base)', actT_reflY(phiW)==idW)
for _ in range(5):
    p,q,r,s=[Fr(random.randint(-9,9),3) for _ in range(4)]
    chk('actT_reflY_dg', actT_reflY(dg(p,q,r,s))==dg(p,q,-r,s))
    k=Fr(random.randint(-9,9),7); chk('smul_dg', smul(k,dg(p,q,r,s))==dg(k*p,k*q,k*r,k*s))
    f=rnd(); chk('phiW_tabMul', tabMul(tabMul(phiW,f),tabT(phiW))==transposeW(f))
    E,X=rnd(),rnd()
    chk('ipW_cnot', ipW(cnot(E),X)==ipW(E,cnot(X)))
    chk('ipW_actT_reflY', ipW(actT_reflY(E),X)==ipW(E,actT_reflY(X)))
    chk('ipW_cnotTw', ipW(cnotTw(E),X)==ipW(E,cnotTw(X)))
    chk('ipW_transposeW', ipW(transposeW(E),X)==ipW(E,transposeW(X)))
    chk('transposeW_transposeW', transposeW(transposeW(E))==E)
    b=[Fr(random.randint(-9,9),4) for _ in range(3)]; c=[Fr(random.randint(-9,9),4) for _ in range(3)]
    chk('tens_sharpVec', tens(sharpVec(b),sharpVec(c))==smul(Fr(1,4),prodState(b,c)))
    a=[Fr(random.randint(-9,9),2) for _ in range(16)]
    A=dg(*a[0:4]);B=dg(*a[4:8]);C=dg(*a[8:12]);F=dg(*a[12:16])
    chk('ipW_dg', ipW(A,tabMul(tabMul(B,C),tabT(F)))==sum(a[i]*a[4+i]*a[8+i]*a[12+i] for i in range(4)))
chk('cnotTw_prodState_xplus_z3', cnotTw(prodState(xplus,z3))==idW)
chk('cnot_prodState_neg', cnot(prodState(neg(xplus),neg(z3)))==dg(1,-1,-1,-1))
chk('cnotTw_prodState_neg', cnotTw(prodState(neg(xplus),neg(z3)))==dg(1,-1,1,-1))
# kt4_parity_aligned value: famI on X=gate01(ps), Y=gate23(ps), E=gate02(tens sharp xplus z3), F=gate13(tens sharp -xplus -z3)
gate={False:cnot, True:cnotTw}
sB={False:-1, True:1}
for t01,t23,t02,t13 in itertools.product([False,True],repeat=4):
    X=gate[t01](prodState(xplus,z3)); Y=gate[t23](prodState(xplus,z3))
    E=gate[t02](tens(sharpVec(xplus),sharpVec(z3))); F=gate[t13](tens(sharpVec(neg(xplus)),sharpVec(neg(z3))))
    v=ipW(X,tabMul(tabMul(E,Y),tabT(F)))
    sig=sB[t01]*sB[t02]*sB[t23]*sB[t13]
    even=(int(t01)+int(t23)+int(t02)+int(t13))%2==0
    chk(f'famI value {t01,t23,t02,t13}: {v}', v==Fr(sig-1,16) and ((v>=0)==even))
print('ALL OK' if ok else 'SOME FAIL')
