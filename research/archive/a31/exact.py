# Exact check with Gaussian integers (entries scaled by 16 at product level; h entries scaled by 2).
import itertools
I=complex(0,1)
h1=[[1,1,1,1],[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]]
hi=[[1,1,1,1],[1,I,-1,-I],[1,-1,1,-1],[1,-I,-1,I]]
def g4(h): return lambda i,j,k: complex(h[i][j]).conjugate()*h[i][k]   # = 4*FibreGram entry (exact small ints)
X=g4(h1); Y=g4(hi)
s=[0,1,3,2]
Ys=lambda i,j,k: Y(s[i],s[j],s[k])
def prod(A,B): return lambda i,j,k: A(i[0],j[0],k[0])*B(i[1],j[1],k[1])  # = 16*entry
def t0(x): return (1,0) if x==(0,1) else ((0,1) if x==(1,0) else x)
def rel(t,G): return lambda i,j,k: G(t(i),t(j),t(k))
W=rel(t0,prod(X,Y)); W2=rel(t0,prod(X,Ys))
ps=lambda x:(s[x[0]],x[1]); p2=lambda x:(x[0],s[x[1]])
idx=list(itertools.product(range(4),range(4)))
allidx=lambda: itertools.product(idx,idx,idx)
print("R(1xσ)W == W2 exactly:", all(rel(p2,W)(i,j,k)==W2(i,j,k) for i,j,k in allidx()))
print("R(σx1)W == W exactly:", all(rel(ps,W)(i,j,k)==W(i,j,k) for i,j,k in allidx()))
print("R(σx1)W2 == W2 exactly:", all(rel(ps,W2)(i,j,k)==W2(i,j,k) for i,j,k in allidx()))
print("off-locus W  at a28 idx (x16):", W((0,1),(2,0),(2,1)), W((1,1),(2,0),(2,1)))
print("off-locus W2 at a28 idx (x16):", W2((0,1),(2,0),(2,1)), W2((1,1),(2,0),(2,1)))
print("sep idx fibres (0,0),(0,2) j=(0,0) k=(0,2): W:", W((0,0),(0,0),(0,2)), W((0,2),(0,0),(0,2)), " W2:", W2((0,0),(0,0),(0,2)), W2((0,2),(0,0),(0,2)))
print("factor entries: X000,Y002,Y202,Ys202=Y303:", X(0,0,0),Y(0,0,2),Y(2,0,2),Ys(2,0,2))
