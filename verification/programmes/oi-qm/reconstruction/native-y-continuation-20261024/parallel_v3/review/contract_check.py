"""Independent exact review of proposed history-tagged reset contract."""
from itertools import product
from collections import Counter
from fractions import Fraction

def need(v,s):
 if not v:raise RuntimeError(s)

def raw(x,y,a,b,z):
 d=1^(x&y)
 return ((y^a,y,d^(a&y)),(y,y,d),(y^b,y,d^(b&y)),(0,0,z))

def decode(r):return r[0][0],r[1][0],r[2][0],r[3][2]

accepted={(0,0):5,(1,0):3,(1,1):2,(0,1):0}
for x,y in product((0,1),repeat=2):
 counts=Counter()
 for a,b,k,z in product((0,1),(0,1),range(8),(0,1)):
  if k>=accepted[a,b]:counts[('fail',)]+=1
  else:
   r=raw(x,y,a,b,z);counts[('success',r)]+=1
   need(decode(r)==(y^a,y,y^b,z),'decoding')
 need(counts[('fail',)]==44,'failure mass11/16')
 for (a,b),n in accepted.items():
  for z in (0,1):need(counts[('success',raw(x,y,a,b,z))]==n,'full output multiplicity')
 need(sum(counts.values())==64,'normalization')
print('LAW1: tagged full carrier per-history multiplicities5,3,2; herald5/16, failure11/16; all4 x,y: PASS')

for x in (0,1):
 complete=Counter()
 for u,v,k,a,b,l,z in product((0,1),(0,1),range(8),(0,1),(0,1),range(8),(0,1)):
  if k>={(0,0):5,(1,0):4,(1,1):1,(0,1):0}[u,v]:complete[('first-fail',)]+=1;continue
  y=x^u
  if l>=accepted[a,b]:complete[(y,'second-fail')]+=1;continue
  complete[(y,'success',raw(x,y,a,b,z))]+=1
 need(complete[('first-fail',)]==1408,'first failure')
 for y in (0,1):
  need(complete[(y,'second-fail')]==220,'second failure')
  for (a,b),n in accepted.items():
   for z in (0,1):need(complete[(y,'success',raw(x,y,a,b,z))]==5*n,'success full joint')
 need(sum(complete.values())==2048,'two-reset normalization')
 need(sum(n for k,n in complete.items() if len(k)==3)==200,'double success25/256')
print('LAW2: supplied independent-seed composition retains all failures and complete record; double success25/256: PASS')

support=[]
for x in (0,1):
 support.append({raw(x,1,a,b,z) for a,b in accepted if accepted[a,b] for z in (0,1)})
need(support[0].isdisjoint(support[1]),'disjoint tagged supports')
need({decode(r) for r in support[0]}=={decode(r) for r in support[1]},'same decoded support')
for x in (0,1):
 for a,b,z in product((0,1),(0,1),(0,1)):
  r=raw(x,1,a,b,z)
  need(r[0][0]^r[0][2]==x and r[2][0]^r[2][2]==x,'history retrievable from full X/R cells')
print('LAW3: strict common raw-carrier law FAILS: conditional y=1 supports for x0,x1 are disjoint (TV1); histories encoded in complete cells: CONFIRMED')
print('SCOPE: per-history tagged law accepted only as candidate interface; unchanged strict acceptance not met, no encoding relaxation adopted.')
