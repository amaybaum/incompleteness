"""Independent bounded check: RREF census + exact amplitude contraction.

Does not import/execute candidate source. Only Python standard library.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import gcd
import json
from pathlib import Path

checks = 0
def check(value, label):
    global checks
    checks += 1
    if not value:
        raise RuntimeError(label)

@lru_cache(None)
def qbin(n, k):
    # Gaussian Pascal recurrence, independent of candidate's product implementation.
    if k < 0 or k > n: return 0
    if k == 0 or k == n: return 1
    return qbin(n-1, k) + (1 << (n-k))*qbin(n-1, k-1)

def subspaces_rref(n, k):
    for pivots in combinations(range(n), k):
        slots = [(i,j) for i,p in enumerate(pivots) for j in range(p+1,n) if j not in pivots]
        for bits in product((0,1), repeat=len(slots)):
            rows = [1 << p for p in pivots]
            for bit,(i,j) in zip(bits,slots): rows[i] |= bit << j
            vectors = [0]
            for row in rows: vectors += [x ^ row for x in vectors]
            yield tuple(sorted(vectors))

def exact_rank(a):
    a = [list(row) for row in a]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[rank],a[pivot] = a[pivot],a[rank]
        for i in range(rank+1,len(a)):
            if not a[i][col]: continue
            x,y = a[rank][col],a[i][col]
            a[i] = [x*v-y*w for v,w in zip(a[i],a[rank])]
            g = 0
            for v in a[i]: g = gcd(g,v)
            if g: a[i] = [v//g for v in a[i]]
        rank += 1
        if rank == len(a): break
    return rank

def amplitude(v,n,r):
    a = [[0]*(1 << (n-r)) for _ in range(1 << r)]
    for x in v: a[x % (1 << r)][x >> r] = 1
    gram = [[sum(x*y for x,y in zip(row,col)) for col in a] for row in a]
    rank = exact_rank(a)
    trace2 = sum(x*x for row in gram for x in row)
    check(rank & (rank-1) == 0, 'Schmidt rank is a power of two')
    check(all(rank*sum(gram[i][t]*gram[t][j] for t in range(len(gram))) == len(v)*gram[i][j]
              for i in range(len(gram)) for j in range(len(gram))), 'flat nonzero spectrum directly from amplitudes')
    return rank.bit_length()-1, Fraction(trace2,len(v)**2)

def joint_formula(n,k,r,i,j):
    s = k-i-j
    if s < 0: return 0
    iso = 1
    for t in range(s): iso *= (1 << s)-(1 << t)
    return qbin(r,i)*qbin(n-r,j)*qbin(r-i,s)*qbin(n-r-j,s)*iso

def incidence(n,k,r):
    a,b,c = 1 << r,1 << (n-r),1 << k
    p = Fraction(c-1,(1 << n)-1)
    p2 = Fraction((c-1)*(c-2),((1 << n)-1)*((1 << n)-2))
    return (1+(a+b-2)*p+(a-1)*(b-1)*p2)/c

state_cuts = 0
ensembles = []
small_dist = None
for n in range(2,6):
    for k in range(n+1):
        spaces = list(subspaces_rref(n,k))
        check(len(set(spaces)) == len(spaces) == qbin(n,k), 'RREF census')
        profiles = []
        joints = [Counter() for _ in range(n+1)]
        purities = [Fraction() for _ in range(n+1)]
        for v in spaces:
            profile = []
            for r in range(n+1):
                s,p = amplitude(v,n,r)
                i = sum(x < (1 << r) for x in v).bit_length()-1
                j = sum(x % (1 << r) == 0 for x in v).bit_length()-1
                check(s == k-i-j and p == Fraction(1,1 << s),'independent amplitude rank and purity versus intersection law')
                check(0 <= s <= min(k,n-k,r,n-r),'capacity')
                joints[r][(i,j)] += 1
                purities[r] += p
                profile.append(s)
                state_cuts += 1
            profiles.append(profile)
        for r in range(n+1):
            predicted = Counter({(i,j):joint_formula(n,k,r,i,j) for i in range(r+1) for j in range(n-r+1)})
            check(+predicted == joints[r], 'entire joint intersection distribution')
            check(purities[r]/len(spaces) == incidence(n,k,r), 'direct amplitude mean purity versus incidence')
            mean_s = Fraction(sum(p[r] for p in profiles),len(spaces))
            check(mean_s >= min(k,n-k,r,n-r)-2,'mean entropy deficit')
        for d in range(n+7):
            bad = sum(any(s <= min(k,n-k,r,n-r)-d for r,s in enumerate(profile)) for profile in profiles)
            check(Fraction(bad,len(spaces)) <= min(Fraction(1),Fraction(4*(n+1),1 << d)), 'same-state union bound')
        if (n,k) == (4,2):
            small_dist = dict(sorted(Counter(p[2] for p in profiles).items()))
            check(small_dist == {0:11,1:18,2:6},'independently enumerated small counts')
            check(purities[2]/len(spaces) == Fraction(43,70),'independently contracted small moment')
        ensembles.append({'n':n,'k':k,'spaces':len(spaces)})

larger_moments = 0
for n in (6,8,12,16,24,32):
    k=n//2
    for r in range(n+1):
        dist = Counter()
        for i in range(r+1):
            for j in range(n-r+1):
                c=joint_formula(n,k,r,i,j)
                if c: dist[k-i-j] += c
        total=sum(dist.values())
        check(total == qbin(n,k),'large classification total')
        mean_p = sum((Fraction(c,1 << s) for s,c in dist.items()),Fraction())/total
        mean_s = Fraction(sum(s*c for s,c in dist.items()),total)
        h=min(k,n-k,r,n-r)
        check(mean_p == incidence(n,k,r),'large independent formulas')
        check(mean_p <= Fraction(4,1 << h) and mean_s >= h-2,'large nonvacuous entropy bound')
        for d in range(n+4):
            tail = Fraction(sum(c for s,c in dist.items() if s <= h-d),total)
            check(tail <= min(Fraction(1),Fraction(4,1 << d)),'pointwise tail')
        larger_moments += 1

cn = lambda x: x ^ ((x & 1) << 1)
orbit = [(0,1),(0,3),(0,1)]
check(tuple(sorted(map(cn,orbit[0]))) == orbit[1] and tuple(sorted(map(cn,orbit[1]))) == orbit[2],'CNOT orbit')
check([amplitude(v,2,1)[0] for v in orbit] == [0,1,0],'CNOT entropy return')
check(incidence(2,1,1) == Fraction(5,6),'small ensemble purity')
check(sum(amplitude(v,2,1)[0] for v in subspaces_rref(2,1)) == 1,'small ensemble entropy sum gives 1/3')
for n in range(2,6):
    check(all(amplitude((x,),n,r)[0] == 0 for x in range(1 << n) for r in range(n+1)),'all configuration states')
    for k in range(n+1):
        check(all(amplitude(tuple(range(1 << k)),n,r)[0] == 0 for r in range(n+1)),'all unmixed coherent seeds')
for m in range(1,5):
    n=2*m
    rows=[(1 << i)|(1 << (n-1-i)) for i in range(m)]
    v=[0]
    for row in rows: v += [x^row for x in v]
    check([amplitude(v,n,r)[0] for r in range(n+1)] == [min(r,n-r) for r in range(n+1)],'mirror Bell tent')

result={'status':'PASS','predicates':checks,'independent_enumerator':'binary RREF bases',
        'state_cut_cases':state_cuts,'larger_exact_moments':larger_moments,
        'n4_k2_r2_counts':small_dist,'n4_k2_r2_purity':'43/70','ensembles':ensembles,
        'scope':'Exact finite controls only; universal statements evaluated separately by written proof.'}
Path(__file__).with_name('independent-results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
