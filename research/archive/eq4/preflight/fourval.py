from fractions import Fraction as Fr
import random
exec(open('identities.py').read().split("ok=True")[0])
def fourVal(X,Y,E,F): return sum(X[a][b]*Y[c][d]*E[a][c]*F[b][d] for a in R for b in R for c in R for d in R)
def prodA(X,Y): return {(a,b,c,d):X[a][b]*Y[c][d] for a in R for b in R for c in R for d in R}
def prodB(L,Lp): return {(a,b,c,d):L[a][c]*Lp[b][d] for a in R for b in R for c in R for d in R}
def effA(e,f,O): return sum(e[a][b]*f[c][d]*O[(a,b,c,d)] for a in R for b in R for c in R for d in R)
def effB(E,F,O): return sum(E[a][c]*F[b][d]*O[(a,b,c,d)] for a in R for b in R for c in R for d in R)
ok=True
for _ in range(3):
    X,Y,E,F=rnd(),rnd(),rnd(),rnd()
    v=fourVal(X,Y,E,F)
    t=[v==ipW(X,tabMul(tabMul(E,Y),tabT(F))), v==ipW(Y,tabMul(tabMul(tabT(E),X),F)),
       v==ipW(E,tabMul(tabMul(X,F),tabT(Y))), v==ipW(F,tabMul(tabMul(tabT(X),E),Y)),
       effA(X,Y,prodA(E,F))==ipW(X,E)*ipW(Y,F), effB(X,Y,prodB(E,F))==ipW(X,E)*ipW(Y,F),
       effB(E,F,prodA(X,Y))==fourVal(X,Y,E,F), effA(X,Y,prodB(E,F))==fourVal(X,Y,E,F)]
    print(t); ok &= all(t)
print('ALL OK' if ok else 'FAIL')
