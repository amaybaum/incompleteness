#!/usr/bin/env python3
"""Independent exact review: no import of the author audit/checker."""
import ast
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def require(condition, label):
    if not condition:
        raise RuntimeError(label)

def main():
    fragments=json.loads((ROOT.parent/'SOURCE-EXCERPTS.json').read_text())
    literals={}
    for item in fragments['checks.py']['fragments']:
        node=ast.parse(item['text']).body[0]
        literals[node.targets[0].id]=ast.literal_eval(node.value)
    env={}
    for item in fragments['candidate.py']['fragments']:
        exec(compile(ast.parse(item['text']),'<retained source>','exec'),env)
    planes=literals['planes']
    points=[p+(z,) for p in planes for z in (0,1)]
    counts={(0,0):5,(1,0):4,(1,1):1,(0,1):0}
    phase=185+12*840**185
    branch_checks=0
    failures=Counter()
    for u,v,k in product((0,1),(0,1),range(8)):
        require(bool(env['accept'](u,v,k)) == (k<counts[u,v]),'herald source truth table')
        if k>=counts[u,v]: failures[u,v]+=1
    require([failures[x] for x in [(0,0),(0,1),(1,0),(1,1)]]==[3,8,4,7], 'failure counts')
    for old in points:
        x,y,r,z0=old
        for cipher in product((0,1),repeat=3):
            law=Counter()
            fail=0
            for pads in product((0,1),repeat=3):
                if (y^pads[0],r^pads[1],z0^pads[2]) != cipher: continue
                for u,v,k,z in product((0,1),(0,1),range(8),(0,1)):
                    # Native collision H applied directly to (u,x,1).
                    raw=(x,1,u^x)
                    require(raw==env['output'](phase,x,u),'actual collision function')
                    if k<counts[u,v]: law[(raw[0],raw[2],x^v,z)]+=1
                    else: fail+=1
            expected=Counter()
            for (u,v),n in counts.items():
                if n:
                    for z in (0,1): expected[(x,x^u,x^v,z)]=n
            require(law==expected,'pointwise record and entire carrier law')
            require(fail==44 and sum(law.values())==20,'512-assignment herald branch totals')
            branch_checks+=1
    reference={'X':(Q(1),Q(0),Q(0)), 'Y':(Q(0),Q(1),Q(0)),
               'R':(Q(4,5),Q(3,5),Q(0)), 'Z':(Q(0),Q(0),Q(1))}
    prepchecks=0
    for axis,s in product(reference,(0,1)):
        idx=literals['indices'][axis]
        mu={}
        for i,p in enumerate(planes):
            for z in (0,1):
                j=p+(z,)
                if j[idx]==s:
                    mu[j]=Q(1,6) if axis=='Z' else Q(literals['weights'][axis][i],20)
        mass=sum(mu.values())
        b=tuple(sum(w*(-1)**j[k] for j,w in mu.items()) for k in (0,1,3))
        require(mass==1 and b==tuple((-1)**s*c for c in reference[axis]),'calibrated decoder')
        require(sum(c*c for c in b)==1,'pure-state positivity')
        for x in (0,1):
            weight=sum(w for j,w in mu.items() if j[0]==x)
            require(weight==(1+(-1)**x*b[0])/2,'projector outcome mass')
        prepchecks+=1
    # Independent enumeration of the source-success seed pairs for the extension.
    extension=[]
    for x in (0,1):
        samples=[]
        for u,v,k,z in product((0,1),(0,1),range(8),(0,1)):
            if k<counts[u,v]: samples.append((x,x^u,x^v,z))
        reuse=Counter((j[1],j[1]) for j in samples)
        fresh=Counter((j[1],h[1]) for j in samples for h in samples)
        tv=sum(abs(Q(reuse[k],20)-Q(fresh[k],400)) for k in product((0,1),repeat=2))/2
        require(tv==Q(1,2),'reuse joint law')
        for y in (0,1):
            subset=[j for j in samples if j[1]==y]
            b=tuple(sum(Q((-1)**j[k],len(subset)) for j in subset) for k in (0,1,3))
            det=(1-sum(v*v for v in b))/4
            require(det==Q(-1,4),'conditional decoder positivity failure')
            extension.append({'x':x,'metadata_y':y,'determinant':str(det)})
        require(tv*Q(5,16)==Q(5,32),'failure-retaining joint distance')
    # Both mutant kernels preserve total success yet violate full distribution.
    mutated={(0,0):4,(1,0):5,(1,1):1,(0,1):0}
    distance=sum(abs(Q(counts[k],10)-Q(mutated[k],10)) for k in counts)/2
    require(distance==Q(1,10),'same-mass wrong-kernel control')
    require((1,0,0) != env['output'](phase,1,0),'missing constant field control')
    return {'schema':'native-x-independent-review-v1','pointwise_full_carrier_branches':branch_checks,
            'calibrated_pure_preparations':prepchecks,'source_herald_assignments':32,
            'failure_counts':[3,8,4,7],'source_success_mass':'5/16',
            'source_failure_mass':'11/16','conditional_reuse_tv':'1/2',
            'failure_retaining_reuse_tv':'5/32','posterior_cases':extension,
            'same_mass_wrong_kernel_tv':str(distance),'controls_passed':True,'verdict':'PASS_SCOPED_ALGEBRA'}

if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
