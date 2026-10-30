#!/usr/bin/env python3
"""SUBSTATE-2 FIXED-SCALE-1 exhaustive rational finite controls.

Single fixed skew-product model: T(a,r,tape)=(a XOR r XOR tape[0],r, shift tape).
Cyclic n-bit finite approximations; the infinite bi-infinite shift is a
separate mathematical argument, not computationally proved by these runs.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
import json


def step(x, n, feedback=True):
    a,r,b=x
    mask=(1<<n)-1
    assert 0<=b<=mask
    return (a ^ (r if feedback else 0) ^ (b & 1), r,
            (b>>1) | ((b&1)<<(n-1)))


def undo(x, n, feedback=True):
    a,r,b=x
    mask=(1<<n)-1
    old_b=((b<<1)&mask) | (b>>(n-1))
    return (a ^ (r if feedback else 0) ^ (old_b&1),r,old_b)


def obs(x):
    a,r,b=x
    return 2*a+(b&1)


def states(n):
    return list(product((0,1),(0,1),range(1<<n)))


def trajectories(n, feedback=True):
    out=[]
    for x in states(n):
        rec=[obs(x)]
        y=x
        for _ in range(2*n):
            y=step(y,n,feedback)
            rec.append(obs(y))
        out.append((x,tuple(rec),y))
    return out


def rooted(traces,t):
    joint=Counter((v[0],v[t]) for _,v,_ in traces)
    n=len(traces)
    return tuple(tuple(F(4*joint[(i,j)],n) for j in range(4)) for i in range(4))


def cmi_3(traces):
    # I(O0;O2 | O1), exact rational via power-of-two ratios.
    triples=Counter((v[0],v[1],v[2]) for _,v,_ in traces)
    mid=Counter(v[1] for _,v,_ in traces)
    left=Counter((v[0],v[1]) for _,v,_ in traces)
    right=Counter((v[1],v[2]) for _,v,_ in traces)
    ratios={F(n*mid[b],left[(a,b)]*right[(b,c)])
            for (a,b,c),n in triples.items()}
    # all nonzero triples have ratio 2 or 1 in these model branches
    if ratios=={F(2)}: return 1
    if ratios=={F(1)}: return 0
    raise AssertionError(f'Unexpected nontrivial CMI ratios: {ratios}')


def main():
    summaries=[]
    j4=tuple(tuple(F(1,4) for j in range(4)) for i in range(4))
    eye=tuple(tuple(F(int(i==j)) for j in range(4)) for i in range(4))
    for n in range(3,10):
        S=states(n)
        for fb in (True,False):
            assert all(undo(step(x,n,fb),n,fb)==x and step(undo(x,n,fb),n,fb)==x for x in S)
            assert len({step(x,n,fb) for x in S})==len(S)
        traces=trajectories(n)
        baseline=trajectories(n,False)
        assert all(y==x for x,_,y in traces), f'full cycle 2n n={n}'
        assert all(y==x for x,_,y in baseline), f'baseline cycle 2n n={n}'
        assert rooted(traces,0)==eye
        for t in range(1,n):
            assert rooted(traces,t)==j4,(n,t,'skew rooted')
        assert rooted(traces,n)!=j4,('finite boundary',n)
        assert rooted(traces,2*n)==eye,('cycle return',n)
        triples=Counter(tuple(v[:3]) for _,v,_ in traces)
        assert len(triples)==32 and set(triples.values())=={len(S)//32},(n,triples)
        assert cmi_3(traces)==1
        assert cmi_3(baseline)==0
        # Markov decoupled control a_next=a xor c_t, fresh c_next.
        for a in range(2):
            for c in range(2):
                rows=Counter((v[0],v[1]) for _,v,_ in baseline)
                for a2 in range(2):
                    for c2 in range(2):
                        v0=2*a+c;v1=2*a2+c2
                        expected = len(S)//8 if a2 == (a^c) else 0
                        assert rows[(v0,v1)]==expected,(n,v0,v1)
        # A distinction at arbitrarily chosen initial depth m in finite tape:
        # the two source states agree on positions 0..m-1 but at t=m
        # have different public tape bits; at t=m+1 their public a differ.
        for m in range(1,n):
            x=(0,0,0);y=(0,0,1<<m)
            a=x;b=y
            for _ in range(m):
                a=step(a,n);b=step(b,n)
            assert a[0]==b[0] and obs(a)!=obs(b),(n,m,'initial depth')
            a=step(a,n);b=step(b,n)
            assert a[0]!=b[0],(n,m,'backflow')
        summaries.append({'tape_length':n,'full_states':len(S),'prewrap_rooted_uniform_times':n-1,
                          'exact_return_time_upper_bound':2*n,
                          'supported_three_time_words':len(triples),
                          'word_probability':str(F(1,32)),
                          'predictive_conditional_memory_bits':cmi_3(traces),
                          'no_feedback_conditional_memory_bits':cmi_3(baseline),
                          'earliest_wrap_time':n})
    out={'status':'PASS_FIXED_RULE_CLASSICAL_MEMORY_CONTROL',
         'state_model':'a visible bit, r persistent hidden bit, invertible bi-infinite fair tape shift',
         'single_rule':'T(a,r,c)=(a XOR r XOR c0,r,shift c)',
         'observable':'O_t=(a_t,c_t), four visible outcomes',
         'finite_stages':summaries,
         'infinite_mathematical_prediction':{
           'rooted_Gamma_t_for_all_positive_t':'all rows 1/4',
           'P_divisible':True,
           'three_time_conditional_memory_bits':1,
           'exact_common_visible_return':False,
           'growing_initial_depth_with_time':True},
         'negative_controls':{
           'disable_static_feedback':'Markov; one_step_a=a XOR c0; three-time CMI zero',
           'observe_tape_alone':'iid fair',
           'finite_wraparound':'at t=n rooted matrix not uniform and at 2n identity'},
         'continuous_time_dynamics_derived':False,
         'native_OI_update_derived':False,
         'quantum_interference_derived':False,
         'Yang_Mills_action_derived':False,
         'physical_log_periodicity_derived':False,
         'finite_boundary_entropy_derived':False}
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=='__main__': main()
