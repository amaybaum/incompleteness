import sympy as sp, pickle
B=pickle.load(open('lambda3.pkl','rb'))
T1,T2=B[5],B[6]; N=B[:5]
Lam=sp.Matrix([list(M) for M in B]).T      # 81 x 7
def coords(M):
    sol=Lam.gauss_jordan_solve(sp.Matrix(list(M)))
    return sol[0].T
def inLam(M):
    try: Lam.gauss_jordan_solve(sp.Matrix(list(M))); return True
    except ValueError: return False
br=lambda a,b:a*b-b*a
print('ad T1, ad T2 on the nonlocal part (coords in basis 0..6):')
for k,M in enumerate(N):
    print(k, coords(br(T1,M)), coords(br(T2,M)))
print('brackets among nonlocal elements, in Lambda?')
for i in range(5):
    for j in range(i+1,5):
        C=br(N[i],N[j]); print(i,j,inLam(C), 'zero' if C==sp.zeros(9) else '')
