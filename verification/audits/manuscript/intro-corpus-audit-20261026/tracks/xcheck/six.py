from fractions import Fraction as F
p=[0,3,4,1,5,2]
def it(s,t):
    for _ in range(t): s=p[s]
    return s
G={}
for t in range(0,7):
    G[t]=[[sum(F(1,3) for h in range(3) if it(3*a+h,t)//3==j) for j in range(2)] for a in range(2)]
def div(A,B):  # exists stochastic L with B = A L ?  (2x2, A invertible or rank1)
    det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    if det==0: return all(B[0][j]==B[1][j] for j in range(2)) and A[0]==A[1] and B[0]==B[1] or None
    inv=[[A[1][1]/det,-A[0][1]/det],[-A[1][0]/det,A[0][0]/det]]
    L=[[sum(inv[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    return all(x>=0 for r in L for x in r)
for K in (5,6):
    print(K, all(div(G[s],G[t]) for t in range(K+1) for s in range(t)))
print({t:G[t] for t in G})
