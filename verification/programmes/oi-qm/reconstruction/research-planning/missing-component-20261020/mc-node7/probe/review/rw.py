import sys; sys.path.insert(0, sys.argv[1])
from hb3a_indep import torus, W1, Fr
for L in (8,10):
    Gg,A,B=torus(L,True)
    for w in (Fr(1,100),Fr(1,2),Fr(1)):
        def m(x,y):
            d={u:Fr(1)/(6+w) for u in Gg[x] if u!=y}; d[y]=w/(6+w); return d
        x=W1(m(A,B),m(B,A),Gg); print(L,w,x,(18-w)/(6+w), 1-x)
