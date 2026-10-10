import sympy as sp, pickle
from disc_lie import run
ns=run(3)
B=[sp.Matrix(9,9,list(v)) for v in ns]
pickle.dump(B,open('lambda3.pkl','wb'))
lab=['%s%s'%(a,b) for a in 'uxz' for b in 'uxz']
for k,M in enumerate(B):
    terms=[]
    for i in range(9):
        for j in range(9):
            if M[i,j]!=0: terms.append('%s|%s<-%s'%(M[i,j],lab[i],lab[j]))
    print(k,' '.join(terms))
