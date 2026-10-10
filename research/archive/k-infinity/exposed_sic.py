"""Which pure states of the SIC-embedded Bloch ball (Main.md:540) admit a point-exposing valid classical effect?
Exact arithmetic in Q(sqrt3): a number is (a, b) = a + b*sqrt3.  Embedding p_i(r) = (1 + a_i.r)/4 with UNIT a_i =
(+-1,+-1,+-1)/sqrt3 (tetrahedral), so a_i.r = q/sqrt3 = (q/3) sqrt3 for rational unit r with integer-combination q.
A valid effect on N ontic states is e(p) = sum c_i p_i with 0 <= c_i <= 1.  e(p(r)) = 1 with p_i >= 0, sum p_i = 1 and
c_i <= 1 forces c_i = 1 wherever p_i(r) > 0; so r is point-exposable iff some p_i(r) = 0, iff r = -a_i."""
from fractions import Fraction as Fr
A=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
def four_p(r):                                   # 4 p_i = 1 + (a.r)/sqrt3, a.r rational = q  ->  (1, q/3)
    return [(Fr(1), sum(Fr(a[k])*r[k] for k in range(3))/3) for a in A]
def is_zero(x): return x[0]==0 and x[1]==0
def positive(x):                                 # a + b sqrt3 > 0, exactly
    a,b=x
    if b==0: return a>0
    if a==0: return b>0
    if a>0 and b>0: return True
    if a<0 and b<0: return False
    return (a*a > 3*b*b) if a>0 else (3*b*b > a*a)
samples=[(Fr(3,5),Fr(4,5),Fr(0)),(Fr(0),Fr(3,5),Fr(4,5)),(Fr(1),Fr(0),Fr(0)),(Fr(2,3),Fr(2,3),Fr(1,3)),(Fr(2,7),Fr(3,7),Fr(6,7)),(Fr(1,3),Fr(2,3),Fr(2,3))]
for r in samples:
    assert sum(x*x for x in r)==1
    fp=four_p(r); assert all(positive(x) for x in fp), fp
    print('r =',tuple(map(str,r)),' all 4 p_i > 0 -> NOT point-exposable')
# the four tangency points r = -a_i (irrational): p_i = 0 there, and e = 1 - p_i is a valid exposing effect
for i,a in enumerate(A):
    fp=[(Fr(1), -Fr(sum(x*y for x,y in zip(a,b)))/3) for b in A]   # 4 p_j at r = -a_i/sqrt3: 1 - (a_i.a_j)/3
    print('r = -a_%d: 4p =' % i, [str(x[0]+x[1]) if x[1]==0 or True else '' for x in [(Fr(1)-Fr(sum(x*y for x,y in zip(a,b)))/3,0) for b in A]], ' p_%d = 0 -> exposed by e = 1 - p_%d' % (i,i))
print('theorem: in a classical realization on N ontic states, a strictly convex state body has at most N point-exposed boundary states (each lies on a facet; a strictly convex body meets a facet in <= 1 point). Here N = 4.')
