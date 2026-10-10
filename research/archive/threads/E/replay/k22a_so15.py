exec(open('k22a_closure.py').read().split("surv={0:")[0])
import itertools
for i in (2,3,4,5,8,9,14,15):
    G=M(Gs[cs[i][0]])
    fix0 = G[0][0]==1 and all(G[0][j]==0 for j in range(1,16)) and all(G[j][0]==0 for j in range(1,16))
    orth = mul(G,[list(r) for r in zip(*G)])==[[int(a==b) for b in range(16)] for a in range(16)]
    print('failing SO-class %2d: fixes u(x)u and preserves its complement: %s; orthogonal: %s' % (i,fix0,orth))
print('local generators antisymmetric with zero u(x)u row/column:', all(all(x[a][b]==-x[b][a] for a in range(16) for b in range(16)) and not any(x[0]) for x in local))
# SO(15)-invariant cones are Lorentz cones {x0 >= |w|/c}: product pure states have |w|^2 = 3 (need c >= sqrt3),
# while containment in max against product pure effects needs |w| <= x0/sqrt3 (c <= 1/sqrt3)
from fractions import Fraction as Fr
a=[Fr(1),0,0]; b=[0,Fr(3,5),Fr(4,5)]
w2=sum(x*x for x in a)+sum(x*x for x in b)+sum(x*x for x in a)*sum(y*y for y in b)
print('|w|^2 of a pure product state (x0 = 1):', w2)
