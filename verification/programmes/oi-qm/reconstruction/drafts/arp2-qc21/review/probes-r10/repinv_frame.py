# Reviewer probe r10 (exact; supplied matrices only, C-R60-ODD's fixture). Does REP-INV's L-CAL recalibration by a
# signed permutation S preserve W-CL's either-frame verdict when the encoded transposition P (x<->z) is kept fixed
# rather than transported (P' = S P S^-1)? Coordinates (x, y, z).
from fractions import Fraction as F
import itertools
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def inv_sp(S): return [list(r) for r in zip(*S)]          # signed permutations are orthogonal
def charpoly(A):
    tr=sum(A[i][i] for i in range(3)); c2=sum(A[i][i]*A[j][j]-A[i][j]*A[j][i] for i,j in ((0,1),(0,2),(1,2)))
    det=(A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
    return (1,-tr,c2,-det)
# signed-permutation spectra (as charpolys over Q): products of (l-1),(l+1),(l^2+1),(l^2+l+1),(l^2-l+1) of total degree 3 that occur
def pm(a,b):
    return tuple(sum(a[i]*b[k-i] for i in range(len(a)) if 0<=k-i<len(b)) for k in range(len(a)+len(b)-1))
L1,Lm1,Q4,Q3,Q6=(1,-1),(1,1),(1,0,1),(1,1,1),(1,-1,1)
OK={pm(pm(a,b),c) for a in (L1,Lm1) for b in (L1,Lm1) for c in (L1,Lm1)} | {pm(Q4,L1),pm(Q4,Lm1),pm(Q3,L1),pm(Q6,Lm1)}
def wcl_fires(A):  # exact for these rational orthogonal cases: not a signed-permutation characteristic polynomial
    return tuple(F(x) for x in charpoly(A)) not in {tuple(F(x) for x in p) for p in OK}
R60=[[F(2,3),F(-1,3),F(2,3)],[F(2,3),F(2,3),F(-1,3)],[F(-1,3),F(2,3),F(2,3)]]
P=[[0,0,1],[0,1,0],[1,0,0]]
beta=mm(P,R60)                                            # fixed-slot beta of an encoded R60 with k odd
print('reference: W-CL(beta)=',wcl_fires(beta),' W-CL(P beta)=',wcl_fires(mm(P,beta)))
perms=[]
for p in itertools.permutations(range(3)):
    for s in itertools.product((1,-1),repeat=3):
        perms.append([[s[i] if j==p[i] else 0 for j in range(3)] for i in range(3)])
miss_fixed=0; miss_transported=0
for S in perms:
    b2=mm(mm(S,beta),inv_sp(S))
    fixedP = wcl_fires(b2) or wcl_fires(mm(P,b2))
    P2=mm(mm(S,P),inv_sp(S))
    transP = wcl_fires(b2) or wcl_fires(mm(P2,b2))
    miss_fixed += (not fixedP); miss_transported += (not transP)
print('of 48 recalibrations S: either-frame W-CL lost with P kept fixed:',miss_fixed,'; with P transported (SPS^-1):',miss_transported)
