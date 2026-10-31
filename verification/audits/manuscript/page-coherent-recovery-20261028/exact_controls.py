#!/usr/bin/env python3
"""Bounded rational controls for the coherent-subspace candidate; no numpy/asserts."""
from collections import Counter
from fractions import Fraction
from itertools import product
import json

checks = 0

def require(ok, label):
    global checks
    checks += 1
    if not ok:
        raise SystemExit('FAIL: ' + label)

def subspaces(n):
    levels = [{(0,)}]
    for k in range(n):
        nxt = set()
        for v in levels[-1]:
            old = set(v)
            for x in range(1, 1 << n):
                if x not in old:
                    nxt.add(tuple(sorted(old | {y ^ x for y in v})))
        levels.append(nxt)
    return levels

def gaussian(n, k):
    if not 0 <= k <= n:
        return 0
    value = Fraction(1)
    for t in range(k):
        value *= Fraction((1 << n) - (1 << t), (1 << k) - (1 << t))
    require(value.denominator == 1, 'Gaussian coefficient integral')
    return value.numerator

def gl(s):
    x = 1
    for t in range(s):
        x *= (1 << s) - (1 << t)
    return x

def formula_distribution(n, k, r):
    out = Counter()
    for i in range(r + 1):
        for j in range(n - r + 1):
            s = k - i - j
            if s >= 0:
                count = gaussian(r, i) * gaussian(n-r, j) * gaussian(r-i, s) * gaussian(n-r-j, s) * gl(s)
                out[s] += count
    return +out

def dimensions(v, r):
    mask = (1 << r) - 1
    a = sum(x >> r == 0 for x in v)
    b = sum(x & mask == 0 for x in v)
    require(a & (a-1) == 0 and b & (b-1) == 0, 'intersection cardinalities are powers of two')
    return a.bit_length()-1, b.bit_length()-1

def amplitude_purity(v, n, r):
    # Direct contraction of the real amplitude table; no intersection/rank input.
    coeff = [[0] * (1 << (n-r)) for _ in range(1 << r)]
    for x in v:
        coeff[x & ((1 << r)-1)][x >> r] = 1
    gram = [[sum(a*b for a,b in zip(row,col)) for col in coeff] for row in coeff]
    trace_square = sum(x*x for row in gram for x in row)
    require(sum(gram[i][i] for i in range(len(gram))) == len(v), 'reduced trace normalization')
    return Fraction(trace_square, len(v)**2), gram

def predicted_purity(n, k, r):
    p = Fraction((1 << k)-1, (1 << n)-1)
    p2 = Fraction(((1 << k)-1)*((1 << k)-2), ((1 << n)-1)*((1 << n)-2))
    return Fraction(1, 1 << k) * (1 + ((1 << r)+(1 << (n-r))-2)*p + ((1 << r)-1)*((1 << (n-r))-1)*p2)

cases = 0
summary = []
for n in range(2, 6):
    for k, level in enumerate(subspaces(n)):
        require(len(level) == gaussian(n,k), 'independent subspace census')
        profiles = []
        for v in sorted(level):
            profile = []
            for r in range(n+1):
                i,j = dimensions(v,r)
                s = k-i-j
                h = min(k,n-k,r,n-r)
                require(0 <= s <= h, 'Schmidt capacity bounds')
                purity, gram = amplitude_purity(v,n,r)
                require(purity == Fraction(1,1 << s), 'direct contraction versus entropy formula')
                # Flat-spectrum polynomial identity rho^2=2^-s rho, in integer Gram coordinates.
                factor = 1 << (i+j)
                require(all(sum(gram[a][c]*gram[c][b] for c in range(len(gram))) == factor*gram[a][b]
                            for a in range(len(gram)) for b in range(len(gram))), 'flat reduced spectrum')
                profile.append(s)
                cases += 1
            profiles.append(profile)
        for r in range(n+1):
            measured = Counter(p[r] for p in profiles)
            predicted = formula_distribution(n,k,r)
            require(measured == predicted, 'exact entropy distribution versus direct states')
            avg = sum((Fraction(count,1 << s) for s,count in measured.items()), Fraction()) / len(level)
            require(avg == predicted_purity(n,k,r), 'independent mean purity incidence formula')
            h = min(k,n-k,r,n-r)
            require(avg <= Fraction(4,1 << h), 'purity tent bound')
        for d in range(n+3):
            bad = sum(any(p[r] <= min(k,n-k,r,n-r)-d for r in range(n+1)) for p in profiles)
            require(Fraction(bad,len(level)) <= min(Fraction(1), Fraction(4*(n+1),1 << d)), 'shared-state simultaneous cut bound')
        summary.append({'n':n,'k':k,'subspaces':len(level)})

# CNOT's amplitude supports directly exhibit 0→1→0 at one fixed cut.
seed = (0,1)
cn = lambda x: x ^ (((x & 1) << 1))
trajectory = [seed, tuple(sorted(map(cn,seed))), tuple(sorted(cn(cn(x)) for x in seed))]
require([amplitude_purity(v,2,1)[0] for v in trajectory] == [Fraction(1),Fraction(1,2),Fraction(1)], 'CNOT coherent return')
require(predicted_purity(2,1,1) == Fraction(5,6), 'small ensemble is distinct from the CNOT orbit')
for m in range(1,5):
    n=2*m
    v=tuple(sorted(sum(((x >> i)&1)*((1 << i)|(1 << (n-1-i))) for i in range(m)) for x in range(1 << m)))
    require([m-sum(dimensions(v,r)) for r in range(n+1)] == [min(r,n-r) for r in range(n+1)], 'mirror Bell-pair exact tent')
for n in range(2,6):
    require(all(amplitude_purity((0,),n,r)[0] == 1 for r in range(n+1)), 'configuration countercontrol')
    product_seed=tuple(range(1 << (n//2)))
    require(all(amplitude_purity(product_seed,n,r)[0] == 1 for r in range(n+1)), 'coherence without mixing countercontrol')
diagonal = [Fraction(1,2) if x in (0,3) else Fraction() for x in range(4)]
reduced = [sum(diagonal[x] for x in range(4) if (x & 1)==a) for a in range(2)]
require(sum(p*p for p in diagonal) == Fraction(1,2), 'incoherent mixture global purity')
require(sum(p*p for p in reduced) == Fraction(1,2), 'incoherent mixture same reduced purity as Bell')
require(amplitude_purity((0,3),2,2)[0] == 1, 'coherent Bell global purity distinguishes mixture')
small = formula_distribution(2,1,1)
require(Fraction(sum(s*c for s,c in small.items()),sum(small.values())) == Fraction(1,3), 'small ensemble exact mean entropy')
require(Fraction(1,3) != Fraction(1,2), 'ensemble mean differs from repeated-CNOT cycle mean')
large_moments = 0
for n in (6,8,12,16,24,32):
    k=n//2
    for r in sorted(set((0,1,n//4,n//2,n-1,n))):
        dist=formula_distribution(n,k,r);total=gaussian(n,k)
        require(sum(dist.values()) == total, 'larger dimension subspace classification count')
        moment=sum((Fraction(c,1 << s) for s,c in dist.items()),Fraction())/total
        require(moment == predicted_purity(n,k,r), 'larger dimension independently derived moments')
        h=min(k,n-k,r,n-r)
        for d in range(13):
            tail=Fraction(sum(c for s,c in dist.items() if s<=h-d),total)
            require(tail <= min(Fraction(1),Fraction(4,1 << d)), 'nontrivial pointwise deficit bound')
        large_moments += 1

print(json.dumps({'status':'PASS','explicit_predicates':checks,'state_cut_cases':cases,'larger_exact_moment_cases':large_moments,'ensembles':summary,
                  'n4_k2_r2_distribution':dict(formula_distribution(4,2,2)),
                  'n4_k2_r2_mean_purity':str(predicted_purity(4,2,2)),
                  'n2_k1_r1_mean_purity':str(predicted_purity(2,1,1)),
                  'scope':'Finite exact controls, not a universal proof, Lean certificate, physical scrambling or evaporation model.'},sort_keys=True,indent=2))
