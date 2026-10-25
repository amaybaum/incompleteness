#!/usr/bin/env python3
"""Independent finite source-law assembly; no author evaluator imported."""
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path

INPUTS={'branch_v10/local-controller/symmetric-result.json':'d8e7c1f5841192165beefb3fe35b069cc14cc93f2faa2bd68619aa7748b3db2f',
        'parallel_v3/direct_reset/herald.json':'406befa2c8d1f663856a78ca6cb632e9c61d1233b02a9d532c7cb43d6261ce64'}

def need(ok,label):
    if not ok: raise RuntimeError(label)
def bits(v): return ((v>>2)&1,(v>>1)&1,v&1)
def h(t): a,b,c=t;return b,c,a^(b&c)
def xor(a,b): return tuple(x^y for x,y in zip(a,b))
def decoder(phase): previous,current,z=phase;return current[1],previous[1],current[2],z[2]
def bloch(mu):
    return (sum(mu.values()),)+tuple(sum(w*(-1)**j[k] for j,w in mu.items()) for k in (0,1,3))
def tv(a,b): return sum(abs(a.get(k,0)-b.get(k,0)) for k in a.keys()|b.keys())/2
def distance(a,b): return sum(abs(x-y) for x,y in zip(a,b))

def run(root):
    values={}
    for path,digest in INPUTS.items():
        raw=(root/path).read_bytes();need(hashlib.sha256(raw).hexdigest()==digest,'pinned input '+path)
        values[path]=json.loads(raw)
    local=values['branch_v10/local-controller/symmetric-result.json']
    # Reconstruct tuple keys from the full published lexicographic enumeration.
    keys=product(range(2),range(2),range(2),range(2),range(2),range(2),range(8),range(8),range(8))
    table={key:bits(int(value,16)) for key,value in zip(keys,local['q9_table_hex'])}
    need(len(table)==32768,'complete table size')
    word=values['parallel_v3/direct_reset/herald.json']['program'][:2684]
    flags={}
    for a,b,k in product((0,1),(0,1),range(8)):
        vector=(a,b,k&1,(k>>1)&1,(k>>2)&1);state=(0,0,0)
        for constant,terms in word:
            injection=bits(constant)
            for index,mask in terms:
                if vector[index]: injection=xor(injection,bits(mask))
            state=h(xor(state,injection))
        need(state in ((0,0,0),(1,0,0)),'predicate before phase rotation')
        state=h(h(state));flags[a,b,k]=state[1]
        need(state==(0,int(k<{(0,0):5,(0,1):0,(1,0):3,(1,1):2}[a,b]),0),'complete herald predicate')
    for start in product((0,1),repeat=3):
        v=start
        for control in (2,3,3,3,3,7): v=h(xor(v,bits(control)))
        need(v==start,'all-state padding identity')
    worlds=0; raw_cells=0; records=[]; posteriors=[]; common={};refinement_cases=0
    for x,u,my,mr in product((0,1),repeat=4):
        y=x^u; success=Counter();failed=Counter()
        for a,b,k,z in product((0,1),(0,1),range(8),(0,1)):
            current=table[x,u,my,mr,a,b,4,5,7]
            phase=((0,y,0),current,(0,0,z))
            (success if flags[a,b,k] else failed)[phase]+=1
            worlds+=1
        expected_success=Counter();expected_failure=Counter()
        for (a,b),accept in {(0,0):5,(0,1):0,(1,0):3,(1,1):2}.items():
            physical=(u,y,x*(1-u)) if (a,b)==(0,1) else (0,y^a,y^b)
            for z in (0,1):
                phase=((0,y,0),physical,(0,0,z))
                if accept: expected_success[phase]+=accept
                expected_failure[phase]+=8-accept
        need(success==expected_success and failed==expected_failure,'full selected physical success/failure laws')
        need(sum(success.values())==20 and sum(failed.values())==44,'64-world normalization')
        raw_cells+=len(success)+len(failed)
        mu={decoder(phase):Q(n,20) for phase,n in success.items()}
        need(bloch(mu)==(1,0,(-1)**y,0),'fixed calibrated post-Y Bloch state')
        need(sum(w*(-1)**j[2] for j,w in mu.items())==Q(3,5)*(-1)**y,'terminal R marginal')
        need(mu==common.setdefault(y,mu),'same selected-phase law at fixed y')
        # Compare complete raw q9 records, never a selected field alone.
        raw_record={}
        for phase,n in success.items():raw_record[phase[1]]=raw_record.get(phase[1],Q(0))+Q(n,20)
        for axis,xx,rr in product(('X','R'),(0,1),(0,1)):
            if axis=='X':
                outcome=xx; quantum_probability=Q(1,2)
                refinement=(Q(int(rr==y)) if xx==y else Q(3,5) if rr==y else Q(2,5))
            else:
                outcome=rr; quantum_probability=Q(4,5) if rr==y else Q(1,5)
                refinement=(Q(5,8) if xx==y else Q(3,8)) if rr==y else Q(int(xx!=y))
            need(raw_record.get((0,xx,rr),Q(0))==quantum_probability*refinement,
                 'whole-port terminal projector/refinement law')
            refinement_cases+=1
        records.append({'x':x,'u':u,'mY':my,'mR':mr,'success_worlds':20,'failure_worlds':44,
                        'physical_raw_cells':len(success)+len(failed)})
        if my==mr==0:
            # A whole q9 read fixes both X and R; retain that exact record.
            for raw in sorted({phase[1] for phase in success}):
                chosen={decoder(phase):Q(n,20) for phase,n in success.items() if phase[1]==raw}
                mass=sum(chosen.values());conditional={j:w/mass for j,w in chosen.items()}
                t,bx,by,bz=bloch(conditional)
                determinant=(t*t-bx*bx-by*by-bz*bz)/4
                need(determinant==Q(-1,4),'unchanged carrier after whole q9 read not positive')
                posteriors.append({'x':x,'u':u,'raw_q9':list(raw),'probability':str(mass),
                                   'unchanged_decoder_determinant':str(determinant)})
    need(worlds==1024 and raw_cells==208,'assembly counts')
    correct={(a,b,z):Q(n,20) for a,b,n in ((0,0,5),(1,0,3),(1,1,2)) for z in (0,1)}
    swapped={(a,b,z):Q(n,20) for a,b,n in ((0,0,5),(1,0,2),(1,1,3)) for z in (0,1)}
    shared={(a,b,a):Q(n,10) for a,b,n in ((0,0,5),(1,0,3),(1,1,2))}
    need(tv(correct,swapped)==Q(1,10) and tv(correct,shared)==Q(1,2),'full-law countercontrols')
    T=185;P=12*840**185;S=T+P;R=S+68;L=R+9
    need((P-2424)%6==0 and 2684+6*((P-2424)//6)+2==L,'actual native schedule')
    need(L%3==1 and h((1,0,0))==(0,0,1),'fair-z phase')
    q8=(0,S,76);q9=(0,S,77)
    controls=[(0,S,S+154),(1,S,S+153),(-1,S,S+153)]
    ports=[((0,T,0),T,(0,-1,0)),((0,0,-8*T),T,(0,0,-1)),((T,P,0),S,(0,1,0)),
           ((-T,P,0),S,(0,1,0)),((4*T,P,0),S,(0,1,0)),((0,S,0),S,(0,1,0)),((12*R,0,0),R,(-1,0,0))]
    cone_tests=0
    for port,deadline,direction in ports:
        axis=next(i for i,v in enumerate(direction) if v)
        for center,radius in ((q8,L-1),(q9,L)):
            t=max(deadline+1,min(L,(center[axis]-port[axis])*direction[axis]))
            nearest=tuple(p+t*v for p,v in zip(port,direction))
            need(distance(nearest,center)>radius,'entire old-bank ray excludes selected phase cone')
            cone_tests+=1
        for control in controls:
            need(distance(control,port)>L,'new controls cannot change old public history')
            t=(control[axis]-port[axis])*direction[axis]
            point=tuple(p+t*v for p,v in zip(port,direction))
            need(point!=control or not deadline<t<=L,'no local source pins a bank coordinate')
    need(all(distance(c,q9)==L and distance(c,q8)>L-1 for c in controls),'local source exceptions')
    need(47*L>13*R and 48*L-13*R>L and 96*L>2*L,'remote/current/old cone disjointness')
    need(196*L<256*L+64*T+1,'enlarged no-wrap lift bound')
    return {'schema':'oi-joint-phase-independent-review-v1','verdict':'PASS',
            'seed_worlds':worlds,'success_failure_branches':32,'physical_raw_cells':raw_cells,
            'old_rows':records,'success_mass':'5/16','terminal_failure_mass':'11/16',
            'calibrated_post_Y_Bloch_check':'PASS','whole_q9_read_posteriors':posteriors,
            'complete_terminal_refinement_cases_including_zeros':refinement_cases,
            'bank_ray_selected_cone_tests':cone_tests,
            'scope':'conditional native-family selected phase law; inherited native dynamics and arbitrary-noise proof; readout/reuse open'}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2])
    args=parser.parse_args();print(json.dumps(run(args.source_root),indent=2,sort_keys=True))
