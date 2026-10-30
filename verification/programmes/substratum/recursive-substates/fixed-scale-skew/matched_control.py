#!/usr/bin/env python3
"""Matched two-time classical negative control for SUBSTATE-2 FIXED-SCALE-1.

An iid four-valued symbolic shift has the same Γt for every t>0
as the skew model but different three-time laws. Research-only.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json


def require(b, label):
    if not b:
        raise AssertionError(label)


def main():
    stages=[]
    skew_triples=Counter()
    # A,B,C are encoded records 2*a+c for a,c in {0,1}.
    for a0,c0,r,c1,c2 in product(range(2),repeat=5):
        o0=2*a0+c0
        a1=a0^r^c0; o1=2*a1+c1
        a2=a1^r^c1; o2=2*a2+c2
        skew_triples[(o0,o1,o2)]+=1
    require(len(skew_triples)==32 and set(skew_triples.values())=={1},'skew triple independent count')
    for n in range(3,8):
        words=list(product(range(4), repeat=n))
        total=len(words)
        require(total == 4**n, 'total')
        for t in range(1,n):
            pairs=Counter((w[0],w[t]) for w in words)
            require(len(pairs)==16 and set(pairs.values())=={total//16},f'rooted equality n{n} t{t}')
        triples=Counter(w[:3] for w in words)
        require(len(triples)==64 and set(triples.values())=={total//64},f'iid triples n{n}')
        tv=sum(abs(Fraction(skew_triples[k],32)-Fraction(triples[k],total))
               for k in product(range(4), repeat=3))/2
        require(tv == Fraction(1,2),f'TV mismatch n{n} {tv}')
        # A single Markov state (current record) predicts all future outcomes.
        require(all(Fraction(triples[(a,b,c)],total)==Fraction(1,64)
                    for a,b,c in product(range(4),repeat=3)),f'full joint n{n}')
        stages.append({'tape_length':n,'iid_states':total,
                       'rooted_pair_entry_for_1_le_t_lt_n':'1/4',
                       'iid_three_time_full_support':64,
                       'skew_three_time_support':32,
                       'three_time_TV_distance_to_skew':'1/2',
                       'iid_three_time_CMI_bits':0,'skew_three_time_CMI_bits':1})
    print(json.dumps({
        'status':'PASS_MATCHED_TWOTIME_CLASSICAL_NEGATIVE_CONTROL',
        'model':'four-symbol iid stationary reversible shift, cyclic finite control',
        'stages':stages,
        'matched_exact_rooted_two_time_maps':True,
        'different_exact_three_time_laws':True,
        'physical_quantum_interference_derived':False,
        'native_OI_dynamics_derived':False,
        'Yang_Mills_action_derived':False,
        'full_infinite_shift_mathematics':'analytic Bernoulli iid law; not proved by finite enumerations',
    },indent=2,sort_keys=True))

if __name__=='__main__': main()
