"""Base-metric premises only (no re-costed metric is evaluated): the n=2 local tuples with full-alphabet
first disagreement 5, and whether the reordered word sB sA c sA rA also distinguishes them from the cards."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from eng import *
from fractions import Fraction as F
C=Cards()
def dist(T,word):
    br=[((),F(1),T.init())]
    for op in word:
        nb=[]
        for rec,p,s in br:
            if isread(op):
                for o,(q,s2) in T.read(op,s).items(): nb.append((rec+(o,),p*q,s2))
            else: nb.append((rec,p,T.gate(op,s)))
        br=nb
    d={}
    for rec,p,_ in br: d[rec]=d.get(rec,0)+p
    return d
loc=[4*a for a in range(4)]; locB=list(range(4))
nm=[]
for a in loc:
    for b in locB:
        for c in range(16):
            th=QM(lift_tables(a,b,c)); fd=first_disagreement(C,th,FULL)
            if fd is not None and fd>=5: nm.append(((a,b,c),fd))
print('local triples with full-alphabet ell>=5:',nm)
for t,fd in nm:
    if fd==5:
        th=QM(lift_tables(*t))
        w1=['sA','sB','c','sA','rA']; w2=['sB','sA','c','sA','rA']
        print(t,'sA sB c sA rA distinguishes:',dist(th,w1)!=dist(C,w1),' sB sA c sA rA distinguishes:',dist(th,w2)!=dist(C,w2),
              ' same dist:',dist(th,w1)==dist(th,w2))
