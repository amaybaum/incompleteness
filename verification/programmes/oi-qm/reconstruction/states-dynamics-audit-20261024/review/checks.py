"""Independent exact resource controls; imports no author dynamics/checker."""
from fractions import Fraction as Q
from collections import Counter
import json


def need(ok, label):
    if not ok:
        raise RuntimeError(label)


def below_p(q):
    # q < (2+sqrt(2))/4, decided by rational ordering and squaring.
    v = 4*q-2
    return v <= 0 or v*v < 2


def law_counts(m):
    values = [m*Q(w, 20) for w in (5, 5, 3, 3, 2, 2)]
    return all(v.denominator == 1 for v in values)


target = {(a,b,z): Q(w,20)
          for (a,b),w in [((0,0),5),((1,0),3),((1,1),2)]
          for z in (0,1)}
feasibility=[]
for bits in range(17):
    atoms=2**bits
    successes=Q(5*atoms,16)
    feasible=successes.denominator==1 and law_counts(successes)
    need(feasible == (bits>=6), 'success-rate resource threshold')
    need(not law_counts(atoms), 'always-success obstruction')
    feasibility.append(feasible)

# Independent seed allocation interleaves the two z labels within each pair.
labels=[]
for a,b,repetitions in [(0,0,5),(1,0,3),(1,1,2)]:
    labels += [(a,b,z) for _ in range(repetitions) for z in (0,1)]
labels += [None]*44
counts=Counter(labels)
need({label:Q(n,20) for label,n in counts.items() if label is not None}==target,
     'six-cell law')
need(counts[None]==44, 'failure retained')
codes={label:i+1 for i,label in enumerate(target)}
codes[None]=0
images={(s,r^codes[labels[s]]) for s in range(64) for r in range(8)}
need(len(images)==512, 'reversible sampler bijection')
for s,r in images:
    need((r^codes[labels[s]])^codes[labels[s]]==r, 'involution')
for y in (0,1):
    actual=Counter((y^a,y,y^b,z) for label in labels if label is not None
                   for a,b,z in [label])
    expected={(y^a,y,y^b,z):p for (a,b,z),p in target.items()}
    need({v:Q(n,20) for v,n in actual.items()}==expected,'carrier law')
fixedz=Counter((a,b,0) for label in labels if label is not None for a,b,z in [label])
need({v:Q(n,20) for v,n in fixedz.items()}!=target,'fixed-z mutant rejected')
need(Counter({ab:sum(n for (a,b,z),n in fixedz.items() if (a,b)==ab)
              for ab in [(0,0),(1,0),(1,1)]})==Counter({(0,0):10,(1,0):6,(1,1):4}),
     'fixed-z mutant keeps pair marginal')

tested=0
for m in range(1,65):
    for n in range(m+1):
        q=Q(n,m)
        delta=Q(1,8*m*m)
        need(8*n*n-8*n*m+m*m != 0, 'integer polynomial nonzero')
        need(below_p(q+delta) or not below_p(q-delta), 'strict irrational error bound')
        tested+=1

brackets=[]
for bits in range(1,17):
    total=2**bits
    lo,hi=0,total
    while hi-lo>1:
        mid=(lo+hi)//2
        if below_p(Q(mid,total)): lo=mid
        else: hi=mid
    need(below_p(Q(lo,total)) and not below_p(Q(hi,total)), 'bracket')
    need(Q(hi-lo,total)==Q(1,total),'bracket width')
    brackets.append([bits,lo,hi,total])

print(json.dumps({'schema':'oi-states-review-v1','verdict':'PASS',
                  'minimum_fair_bits_at_success_5_over_16':6,
                  'sample_atoms':64,'successful_atoms':20,'failed_atoms':44,
                  'reversible_states_checked':512,
                  'rational_error_comparisons':tested,
                  'dyadic_brackets':brackets,
                  'scope':'abstract fixed-input uniform-resource sampler; not native reset'},
                 indent=2,sort_keys=True))
