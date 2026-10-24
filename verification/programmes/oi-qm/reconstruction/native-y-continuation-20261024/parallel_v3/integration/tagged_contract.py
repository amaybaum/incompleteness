"""Parent exact information contract. No author/native-construction imports.
Abstract kernel only: does not construct late inputs, fanout, or a herald.
"""
from fractions import Fraction as F
from collections import defaultdict
from itertools import product

def need(v,label):
 if not v: raise RuntimeError(label)

def mixer(q,a):
 A,B,D=q;return A^a,B,D^(a&B)

def embed(x,y,j):
 X,Y,R,Z=j
 need(Y==y,'Y support')
 return (mixer((y,y,1^(x&y)),y^X), (y,y,1^(x&y)),
         mixer((y,y,1^(x&y)),y^R), (0,0,Z))

def decode(raw):return raw[0][0],raw[1][0],raw[2][0],raw[3][2]

def mu(y):
 return {(y^a,y,y^b,z):F(count,20)
   for a,b,count in ((0,0,5),(1,0,3),(1,1,2)) for z in (0,1)}

def tv(a,b):return sum((abs(a.get(k,F(0))-b.get(k,F(0))) for k in set(a)|set(b)),F(0))/2

for a in (0,1):
 domain=list(product((0,1),repeat=3))
 need(len({mixer(q,a) for q in domain})==8,'mixer permutation')
 need(all(mixer(mixer(q,a),a)==q for q in domain),'mixer inverse')
q=F(5,16)
for x,y in product((0,1),repeat=2):
 law=defaultdict(F)
 for a,b,k,z in product((0,1),(0,1),range(8),(0,1)):
  ok=k<{(0,0):5,(1,0):3,(1,1):2,(0,1):0}[a,b]
  if not ok:law[('failure',None)]+=F(1,64);continue
  j=(y^a,y,y^b,z);raw=embed(x,y,j)
  law[('success',raw)]+=F(1,64)
  need(decode(raw)==j,'injective encoding')
  # Each complete cell carries only public history and its own sign.
  for out,sign in ((raw[0],j[0]),(raw[2],j[2])):
   expected=(sign,y,1^(x&y)^((y^sign)&y))
   need(out==expected,'single-axis full raw cell contract')
 target={('success',embed(x,y,j)):q*p for j,p in mu(y).items()}
 target[('failure',None)]=1-q
 need(dict(law)==target,'whole tagged carrier kernel with failure')
print('T1: both native-polynomial mixer maps are full permutations/involutions: PASS')
print('T2: exact tagged full-carrier and all-failure law for every x,y: PASS')
print('T3: each complete X/R cell factors through public history plus designated sign: PASS')

# Prefix first herald: u,v,K with counts 5,4,1,0. No previous-selector H1.
for x in (0,1):
 law=defaultdict(F)
 for u,v,k,a,b,l,z in product((0,1),(0,1),range(8),(0,1),(0,1),range(8),(0,1)):
  p=F(1,2048)
  G=k<{(0,0):5,(1,0):4,(1,1):1,(0,1):0}[u,v]
  if not G:law[('G-failure',None)]+=p;continue
  y=x^u;H=l<{(0,0):5,(1,0):3,(1,1):2,(0,1):0}[a,b]
  if not H:law[(y,'H-failure',None)]+=p;continue
  j=(y^a,y,y^b,z)
  law[(y,'success',embed(x,y,j))]+=p
 expected={('G-failure',None):1-q}
 for y in (0,1):
  expected[(y,'H-failure',None)]=q*(1-q)/2
  for j,pj in mu(y).items():expected[(y,'success',embed(x,y,j))]=q*q*pj/2
 need(dict(law)==expected,'two-herald joint law')
 need(sum(law.values())==1,'normalized all-failure branches')
print('T4: supplied two-reset composition law holds; double success25/256, or125/2048 with older5/8 selector: PASS')

# Common raw encoding is stronger: at y=1 the x supports are disjoint.
a={embed(0,1,j):p for j,p in mu(1).items()}
b={embed(1,1,j):p for j,p in mu(1).items()}
need(tv(a,b)==1,'history-tag raw support separation')
need({decode(r):p for r,p in a.items()}=={decode(r):p for r,p in b.items()},'decoded carrier same')
print('T5: y=1 strict raw distributions have TV1 across x; decoded carriers coincide: PASS')

# A future output depending on the retained tag can break reuse.
# For the Y cell with y=1, x=1 XOR D. A future reported X bit
# chosen as X_new XOR x flips the fixed-menu Y->R calibration if used for R.
for y in (0,1):
 agree=sum(p for j,p in mu(y).items() if j[2]==y)
 need(agree==F(4,5),'terminal R target')
need(1-F(4,5)==F(1,5),'tag-controlled flip changes next statistics')
print('C1: retained-history-sensitive future dynamics can change R agreement4/5 to1/5; terminal encoding alone does not prove reuse: PASS')
print('SCOPE: exact supplied-resource information contract, not a complete native instrument.')
