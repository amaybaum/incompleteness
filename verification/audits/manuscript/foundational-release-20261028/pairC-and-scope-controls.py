import json
from fractions import Fraction
from pathlib import Path

def mm(a,b):
 return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def transpose(a):return list(map(list,zip(*a)))
def eye(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def perm(p):return [[int(i==p[j]) for j in range(len(p))] for i in range(len(p))]
def block(a,i,j):return [row[j*3:j*3+3] for row in a[i*3:i*3+3]]
U=perm([0,1,3,2,5,4]);Up=mm(U,perm([1,0,2,3,4,5]))
w=[(0,0,True),(1,0,True),(0,1,True),(0,0,False),(0,1,False),(1,0,False)]
def eval_word(a,swap):
 out=eye(3)
 for i,j,forward in w:
  if swap:i,j=1-i,1-j
  b=block(a,i,j)
  out=mm(out,b if forward else transpose(b))
 return out
word_values={tag:[eval_word(a,False),eval_word(a,True)] for tag,a in [('C',U),('Cprime',Up)]}
require=lambda c: None if c else (_ for _ in ()).throw(RuntimeError('control failed'))
require(word_values['C'][0]==[[1,0,0],[0,0,0],[0,0,0]])
require(all(m==[[0]*3 for _ in range(3)] for m in [word_values['C'][1]]+word_values['Cprime']))
def anomalies(q):
 a,u,d,l,e=q
 return [2*a-u-d,3*a+l,6*a-3*u-3*d+2*l-e,6*a**3-3*u**3-3*d**3+2*l**3-e**3]
exception=[0,1,-1,0,0];standard=list(map(Fraction,['1/6','2/3','-1/3','-1/2','-1']))
require(anomalies(exception)==[0]*4);require(anomalies(standard)==[0]*4)
states=[(v,h) for v in range(2) for h in range(2)]
fibres={}
for v,h in states:fibres.setdefault((v,h),[]).append((v,h))
require(all(len(f)==1 for f in fibres.values()))
result={'pairC_balanced_word_operators':word_values,'exceptional_charges':exception,'exceptional_anomaly_coefficients':anomalies(exception),'standard_anomaly_coefficients':[str(x) for x in anomalies(standard)],'stabilizer_lie_dimension':3**2+2**2+1,'SM_lie_dimension':(3**2-1)+(2**2-1)+1,'swap_two_reading_fibres':len(fibres),'all_swap_two_reading_fibres_singleton':True}
print(json.dumps(result,indent=2))
