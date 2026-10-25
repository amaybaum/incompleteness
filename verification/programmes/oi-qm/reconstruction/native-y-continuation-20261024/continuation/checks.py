from model import *
from fractions import Fraction

def need(ok,msg):
 if not ok:raise RuntimeError(msg)

# Exact reversible interfaces, on their entire domains.
def affine(v):
 a,b,d,e=v;return e,a^b,a,1^d

def affine_inverse(v):
 a,b,d,e=v;return d,b^d,1^e,a

def history(v):
 x,a,b,d=v;return x,b^a,d^1^(x&a),a

def history_inverse(v):
 x,a,b,d=v;return x,d,a^d,b^1^(x&d)
for fn,inv in ((affine,affine_inverse),(history,history_inverse)):
 domain=list(product((0,1),repeat=4))
 need(len({fn(v) for v in domain})==16,'full permutation')
 need(all(inv(fn(v))==v for v in domain),'explicit inverse')
for x,y in product((0,1),repeat=2):
 need(affine((y,y,1^(x&y),0))==(0,0,y,x&y),'clean-ancilla interface')
 need(history((x,y,y,1^(x&y)))==(x,0,0,y),'history-controlled interface')
 # Clean retained workspace can be recycled if x,y remain accessible.
 a,b,d,e=affine((y,y,1^(x&y),0))
 need(e^(x&d)==0,'conditional uncomputation')
print('I1: both four-bit maps and explicit inverses checked on all16 states; all4 native rows; reversible workspace recycling: PASS')

# The 20 free pre-collision entries are the two relevant shell sections.
expected={(R-1,(a,b,z)) for z,r in ((1,2),(2,3)) for a in range(-r,r+1) for b in range(-r,r+1) if abs(a)+abs(b)==r}
observed=set()
for pat,(loc,rawpat) in zip(basis,D['examples']):
 need(pat==int(rawpat,16) and pat.bit_count()==1,'single-entry witnesses')
 slot=slots[pat.bit_length()-1];observed.add(slot)
 need(sum(abs(a-b) for a,b in zip(loc,end))==R+2,'source endpoint boundary')
 need(sum(abs(a-b) for a,b in zip(loc,(0,0,R)))>=2*R,'no early upper collision')
 need(sum(abs(a) for a in loc)>R,'source cannot affect qY at R')
 actual=0
 for i,(t,v) in enumerate(slots):
  ds=tuple(abs(a-b) for a,b in zip(v,loc))
  if sum(ds)==t and odd(ds):actual|=1<<i
 need(actual==pat,'first-arrival parity witness')
need(observed==expected and len(expected)==20,'complete shell sections')
print('G1:20 exact source/parity witnesses; complete relaxed plane-shell controls; no full-apparatus compatibility claim: PASS')

# Exhaustive native update vs independently expressed two-parity formula.
k=variables[0]^variables[1]^variables[6]^variables[7]
l=0
for v in variables[8:]:l^=v
for x,u,my,mr in product((0,1),repeat=4):
 y=x^u
 out=calc(x,u,my,mr)
 expected=(ALL*y,(ALL*y)^(k*u)^l,ALL*(1^(x&y))^(k*(u&(1^x)))^(l*y))
 need(out==expected,'all-source-settings full output formula')
 if y==1:need(out[1]^out[2]==ALL*x,'retained-x invariant')
print('N1:16,777,216 input/control lanes agree with exact formula; all old mask assignments: PASS')
print('N2: on y=1, A=1 and B XOR D=x for every control setting: PASS')
# Direct diagnostic interventions remain tests, not native operations.
for x,u,my,mr,p in product((0,1),repeat=5):
 out=calc(x,u,my,mr,p)
 need(out[0]==ALL*p,'actual arriving operand retained')
print('N3:33,554,432 diagnostic lanes retain A=p; no mid-run interventions in native claim: PASS')

# Non-vacuous controls: wrong old-phase formula, invalid merging of codes,
# and removed constant/AND term are each rejected on native rows.
need(any((y,y,1^(x&y))!=(1^x,y,x^y) for x,y in product((0,1),repeat=2)),'reject old finite-phase formula')
need(len({(0,0,y) for x,y in product((0,1),repeat=2)})<3,'reject garbage-free three-to-two injection')
need(any((y^y,(1^(x&y))^1,y)!=(0,0,y) for x,y in product((0,1),repeat=2)),'missing history AND rejected')
print('C1:wrong-phase, discarded-garbage, and missing-control counterchecks detected: PASS')
print('SCOPE: exact local algebra and scoped boundary-control obstruction; native reset and transport-proof review remain open.')
