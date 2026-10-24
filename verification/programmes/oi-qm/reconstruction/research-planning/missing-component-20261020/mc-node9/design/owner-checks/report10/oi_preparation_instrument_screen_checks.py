"""Exact exploratory checks; no repository writes or OI implementation claim.
Python 3 standard library only. Coordinates below are signs, not lattice sites.
"""
from fractions import Fraction as F
from itertools import product, combinations

def tv(p, q):
    return sum(abs(a-b) for a,b in zip(p,q))/2

def expectation(mu, values):
    return sum(a*b for a,b in zip(mu,values))

print('EXPLORATORY; not preregistered or independently reviewed.')

# Recap 1: K1 and the fixed four-state three-parity correspondence.
signs=list(product((1,-1), repeat=2))
a,b,c=F(3,5),F(4,5),F(0)
w=[(1+s*a+t*b+s*t*c)/4 for s,t in signs]
assert w==[F(3,5),F(1,5),F(3,10),F(-1,10)]
ap,bp,cp=F(7,15),F(2,3),F(2,15)
wp=[(1+s*ap+t*bp+s*t*cp)/4 for s,t in signs]
assert min(wp)>=0 and sum(wp)==1
assert max(abs(a-ap),abs(b-bp),abs(c-cp))/2==F(1,15)
print('Four-state fixed-parity obstruction: negative weight -1/10; optimal three-probability error 1/15.')

# Recap 2: possible one-pair marginals of pure full-K composites.
target=(F(2,5),F(2,5),F(1,10),F(1,10))
marginals=[(F(1,4),)*4]+[tuple(F(1,2) if j in pair else F(0) for j in range(4)) for pair in combinations(range(4),2)]
assert min(tv(target,m) for m in marginals)==F(1,5)
print('Full-K purification diagnostic: closest allowed pure-composite marginal has TV error 1/5.')

lam=list(product((1,-1), repeat=3))
r=(F(1,2),F(1,2),F(0))
def product_encoding(vec):
    ans=[]
    for l in lam:
        val=F(1)
        for x,y in zip(vec,l): val*=(1+x*y)/2
        ans.append(val)
    return ans

prod_plus=product_encoding(r)
prod_minus=product_encoding(tuple(-x for x in r))
assert tv(prod_plus,prod_minus)==F(1,2)
quantum=(F(17,20),F(3,20))
assert (quantum[0]-quantum[1]-tv(prod_plus,prod_minus))/2==F(1,10)
print('Independent eight-state encoding: TV=1/2; rotated-outcome best error 1/10.')

# Correlation repair: XY expectations c+=1, c-=0; Z remains independent fair.
def correlated_encoding(sign,corr):
    return [(1+sign*l[0]/F(2)+sign*l[1]/F(2)+corr*l[0]*l[1])/8 for l in lam]
mu=correlated_encoding(1,F(1))
nu=correlated_encoding(-1,F(0))
assert min(mu+nu)>=0 and sum(mu)==sum(nu)==1
for j in range(3):
    assert expectation(mu,[l[j] for l in lam])==r[j]
    assert expectation(nu,[l[j] for l in lam])==-r[j]
assert tv(mu,nu)==F(3,4)>quantum[0]-quantum[1]
# Exact dual certificate for all bounded measurement responses.
support_bound=sum(max(F(0),x-y/2) for x,y in zip(mu,nu))
assert support_bound==F(3,4)
target_lhs=quantum[0]-quantum[1]/2
assert target_lhs==F(31,40)>support_bound
error=(target_lhs-support_bound)/F(3,2)
assert error==F(1,60)
effect=[F(1) if l[:2]==(1,1) else F(1,3) if l[:2]==(-1,-1) else F(0) for l in lam]
actual=(expectation(mu,effect),expectation(nu,effect))
assert actual==(F(5,6),F(1,6))
assert max(abs(x-y) for x,y in zip(actual,quantum))==error
print('Correlated repair: TV=3/4 passes; measurement target fails alpha-beta/2<=3/4.')
print('Target lhs=31/40; exact optimal probability error=1/60, attained at (5/6,1/6).')

# Positive finite-table control: put the preparation sign in a triple correlation.
def tagged_encoding(sign):
    return [(1+sign*l[0]/F(2)+sign*l[1]/F(2))/4 if l[2]==sign*l[0]*l[1] else F(0) for l in lam]
tag_plus=tagged_encoding(1)
tag_minus=tagged_encoding(-1)
h=[l[0]*l[1]*l[2] for l in lam]
assert min(tag_plus+tag_minus)>=0 and sum(tag_plus)==sum(tag_minus)==1
for j in range(3):
    assert expectation(tag_plus,[l[j] for l in lam])==r[j]
    assert expectation(tag_minus,[l[j] for l in lam])==-r[j]
assert expectation(tag_plus,h)==1 and expectation(tag_minus,h)==-1
assert tv(tag_plus,tag_minus)==1
noisy=[(1+F(7,10)*x)/2 for x in h]
assert (expectation(tag_plus,noisy),expectation(tag_minus,noisy))==quantum
assert (expectation(tag_plus,[(1+x)/2 for x in h]),expectation(tag_minus,[(1+x)/2 for x in h]))==(1,0)
print('Triple-correlation encoding: all three axes and rotated read fit exactly; direct triple-parity read perfectly distinguishes the preparations.')

# Even prohibiting the sharp read is insufficient for a nondisturbing noisy instrument.
p=F(17,20)
majority=3*p*p-2*p*p*p
gap=2*majority-1
assert majority==F(3757,4000) and gap==F(1757,2000)
assert gap*gap>F(1,2)
print('Three independent noisy reads with retained outcomes and unchanged hidden sign: majority success=3757/4000; outcome gap=1757/2000.')
print('Quantum bound for these same-copy preparations is 1/sqrt(2) on any binary outcome gap; exact squared comparison violates it.')
assert min(noisy)==F(3,20) and max(noisy)==F(17,20)
print('Fixed noisy response cannot be a repeatable sharp instrument on this carrier: every posterior gives repeat probability <=17/20 for either recorded outcome.')
print('PASS: all exact checks. No native preparation, apparatus coupling, or composite completion supplied.')
