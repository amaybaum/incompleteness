#!/usr/bin/env python3
"""Independent coefficient-wise affine census of the retained native q9 table."""
import argparse
from collections import Counter
import hashlib
from itertools import product
import json
from pathlib import Path

EXPECTED='4bddbbeec267c831f31d8d578e9768e18f64c1319388bf9512563cae35aa6ac4'

def need(test,label):
    if not test: raise RuntimeError(label)

def run(root):
    raw=(root/'reset_v9/result.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest()==EXPECTED,'pinned source input')
    rows=json.loads(raw)['q9_tables']['native']
    def out(x,u,p,j): return rows[32*x+16*u+8*p+j]
    need(len(rows)==64,'table length')
    for x,u in product((0,1),repeat=2):
        need(all(out(x,u,0,j)==out(x,u,1,j) for j in range(8)),'native intervention ignored')
        need(len({out(x,u,0,j) for j in range(8)})==8,'each J map bijective')
    masks=((0,0),(0,1),(1,0),(1,1)); accepted=((0,0),(1,0),(1,1))
    # Each component has an independent four-bit coefficient vector for 1,u,a,b.
    def value(coeff,u,a,b):
        monomials=1+2*u+4*a+8*b
        return ((coeff&monomials).bit_count()%2)
    counts=Counter(); max_accepted=0; max_global=0; two_sign_solutions=0
    for coeffs in product(range(16),repeat=3):
        family={}
        for a,b in masks:
            outputs=[]
            for u in (0,1):
                j=4*value(coeffs[0],u,a,b)+2*value(coeffs[1],u,a,b)+value(coeffs[2],u,a,b)
                outputs.append(tuple(out(y^u,u,0,j) for y in (0,1)))
            family[a,b]=outputs[0] if outputs[0]==outputs[1] else None
        accepted_valid=all(family[m] is not None for m in accepted)
        if accepted_valid:
            counts['accepted_only_common']+=1
            capacity=min(len({family[m][y] for m in accepted}) for y in (0,1))
            max_accepted=max(max_accepted,capacity)
            two_sign_solutions += capacity==3
        if all(family[m] is not None for m in masks):
            counts['all_masks_common']+=1
            max_global=max(max_global,min(len({family[m][y] for m in masks}) for y in (0,1)))
    need(counts['all_masks_common']==32 and max_accepted==2 and max_global==2 and two_sign_solutions==0,
         'affine census')
    truth=[]; quadratic_success=0; failure_extensions=[]
    for u,a,b in product((0,1),repeat=3):
        target=lambda y:2*(y^a)+(y^b)
        candidates=[j for j in range(8) if all(out(y^u,u,0,j)==target(y) for y in (0,1))]
        need(len(candidates)==1,'unique two-sign J')
        cubic=((u+u*a+b+u*a*b)%2,(a+u*a+b+u*b+a*b)%2,(u+u*b+a*b+u*a*b)%2)
        need(candidates[0]==4*cubic[0]+2*cubic[1]+cubic[2],'reported cubic ANF')
        quadratic=((u+b+u*(a+b))%2,(a+u*(a+b))%2,(u+b)%2)
        if (a,b) in accepted:
            need(quadratic==cubic,'degree-two success extension')
            quadratic_success+=1
        else:
            failure_extensions.append({'u':u,'cubic':list(cubic),'quadratic':list(quadratic)})
        truth.append({'u':u,'a':a,'b':b,'J':candidates[0]})
    # Unique multilinear degree from parity over subcubes, independent of the author's transform.
    degree=0; anf=[]
    for field_bit in (2,1,0):
        terms=[]
        for subset in range(8):
            parity=0
            for u,a,b in product((0,1),repeat=3):
                point=u+2*a+4*b
                if point&~subset==0:
                    j=next(row['J'] for row in truth if (row['u'],row['a'],row['b'])==(u,a,b))
                    parity ^= (j>>field_bit)&1
            if parity:
                terms.append(subset); degree=max(degree,subset.bit_count())
        anf.append(terms)
    need(degree==3,'exact algebraic degree')
    for x,u,a in product((0,1),repeat=3):
        j=5*(u^a)+2*a
        need(out(x,u,0,j)==3*(x^u^a),'one-mask positive control')
    groups=Counter()
    for j0,j1 in product(range(8),repeat=2):
        if all(out(y,0,0,j0)==out(y^1,1,0,j1) for y in (0,1)):
            groups[j0^j1]+=1
    need(sorted(groups.values())==[2,2,2,2],'fixed-u-coefficient group bound')
    T=185; P=12*840**185; S=T+P; N=S+77
    dist=lambda x,y:sum(abs(a-b) for a,b in zip(x,y))
    targets=[(-1,S,76),(0,S-1,76),(0,S,77)]
    sources=[(-S-78,S,76),(0,-78,76),(0,S,S+154)]
    slacks=[[dist(s,t)-N for t in targets] for s in sources]
    need(slacks==[[0,2,2],[2,0,2],[2,2,0]],'fork own/cross arrival')
    need(dist((S+78,S,76),(4*T,P,0))-S==-401,'positive-x ready conflict')
    need([dist((-T,P+S+i,0),targets[0])-N for i in range(3)]==[-2,-1,0],
         'old R source and frontier enter A')
    need(dist((0,0,0),targets[1])-N==dist((0,-76,76),targets[1])-N==-2,
         'origin/W enter B early')
    return {'schema':'oi-branch-v10-independent-review-v1','verdict':'PASS',
            'source_sha256':EXPECTED,'affine_functions':4096,'common_counts':dict(counts),
            'accepted_only_max_codes':max_accepted,'all_mask_max_codes':max_global,
            'three_accepted_mask_solutions':two_sign_solutions,'unique_J':truth,
            'anf_bitmasks_u_a_b':anf,'degree':degree,'quadratic_success_inputs':quadratic_success,
            'unspecified_physical_failure_extensions':failure_extensions,
            'u_coefficient_group_sizes':dict(groups),'spatial_arrival_slacks':slacks,
            'scope':'finite table deduction; nonlinear prior, previous-field access and spatial fork not supplied'}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2])
    args=parser.parse_args()
    print(json.dumps(run(args.source_root),indent=2,sort_keys=True))
