#!/usr/bin/env python3
"""Availability controls for a specified native interface menu, not a gate."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path


def need(ok, why):
    if not ok: raise RuntimeError(why)


def index(values,sizes):
    r=0
    for v,n in zip(values,sizes):r=n*r+v
    return r


def distance(a,b):return sum(abs(x-y) for x,y in zip(a,b))


DIRS=tuple(tuple(s if j==a else 0 for j in range(3)) for a in range(3) for s in (-1,1))
ORDER=(1,2,4,0,3,5)
LAUNCH=(DIRS[0],DIRS[3],DIRS[0],DIRS[3],DIRS[3],DIRS[5])


def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(n,v):return tuple(n*x for x in v)


def selector_geometry(sources):
    T=185;P=12*840**185;S=P+T;R=S+68;L=R+9;q=(0,S,78)
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
    banks=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0),(1,0,0)]
    ready=list(zip(ports,[T,T,S,S,S,S,R,L]))+[((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+j),R+j) for j in range(10)]+[((-48*L,0,0),L),(q,L+1)]
    ball=(q,)+tuple(add(q,d) for d in DIRS)
    old={tuple(s['position']) for s in sources}
    extra={(0,-78,78),(0,S,S+156),(4*T,P+S,0),(0,S,-S-136)}
    need(len(old)==1479 and len(ready)==25,'declared original inventory')
    time=S+2;gkey=add(ports[5],scale(time,banks[5]))
    need(time==L-75,'existing early selector time')
    need(distance(gkey,ports[5])==time and all(distance(gkey,p)>time for i,p in enumerate(ports) if i!=5),'selector own first public arrival')
    need(min(distance(gkey,v) for v in ball)==L+2,'selector key excluded complete L+1 input packet')
    need(min(distance(gkey,c)-r for c,r in ready)==2,'selector source remains original bank')
    need(gkey not in old and gkey not in extra,'selector not a competing prepared source')
    need(time+77==L+2 and time+78==L+3,'earlier selector causally fits input adapter')
    # Input-adapter steps L+1->L+2->L+3 and the already accepted successor
    # L+3->L+4->L+5. This tests a particular recorded-selector candidate.
    allkeys=[gkey];stages=[]
    for offset in (2,3,4,5):
        t=L+offset
        bk=[add(add(q,d),scale(t,a)) for d,a in zip(DIRS,LAUNCH)]
        nk=[add(p,scale(t,a)) for p,a in zip(ports,banks)]
        need([min(distance(k,c)-r for c,r in ready) for k in bk]==[offset]*6,'adapter/future boundary ready slacks')
        cross=[]
        for i,k in enumerate(bk):
            need(distance(k,add(q,DIRS[i]))==t,'straight own boundary path')
            need(all(distance(k,v)>t-1 for v in ball),'future boundary block absent earlier packet')
            need(min(distance(k,p) for p in ports)>L+offset,'future boundary block absent earlier records')
            for j,d in enumerate(DIRS):
                if i!=j and distance(k,add(q,d))<=t:cross.append((i,j))
            for p,a in zip(ports,banks):
                axis=next(j for j in range(3) if a[j])
                need(any(k[j]!=p[j] for j in range(3) if j!=axis),'boundary key off bank line')
        need(cross==[(1,3),(2,0),(4,3)] and all(ORDER.index(i)<ORDER.index(j) for i,j in cross),'same triangular boundary map')
        bankcross=[]
        for i,k in enumerate(nk):
            need(distance(k,ports[i])==t and all(distance(k,p)>=t for p in ports),'bank chronological first arrival')
            need(min(distance(k,v) for v in ball)>L+5,'bank excluded entire tested packet window')
            need(min(distance(k,c)-r for c,r in ready)>0,'new bank stays unpinned')
            bankcross.extend((i,j) for j,p in enumerate(ports) if i!=j and distance(k,p)==t)
        need(bankcross==[(2,5),(3,5)],'public bank cross graph')
        for k in bk+nk:
            need(k not in old and k not in extra,'key outside old/additional source inventories')
            need(distance(k,(0,S,77))>L if offset==2 else distance(k,(0,S,77))>L+2,'earlier q9 records excluded')
        allkeys.extend(bk+nk)
        stages.append({'output_time_over_L':offset,'minimum_boundary_ready_slack':offset})
    need(len(set(allkeys))==57,'selector plus adapter and accepted future source blocks distinct')
    side=256*L+64*T+1
    need(max(abs(a-b) for p in ports+allkeys+[q] for r in ports+[q] for a,b in zip(p,r))<side//2,'no torus shortcut')
    # The first newly observed packet-window public bit would be too late.
    late=L+4
    need(min(distance(p,q) for p in ports)==78 and min(distance(p,v) for p in ports for v in ball)==77,'nearest existing public port')
    need(late+77==L+81 and late+78==L+82,'late-selector obstruction')
    return {'early_selector_time':'S+2=L-75','earliest_packet_boundary':'L+2',
            'earliest_center':'L+3','early_selector_input_packet_slack':1,
            'tracked_original_triples':57,'stages':stages}


def run(root):
    table=json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    need(len(table)==32768,'retained complete q9 table size')
    need(hashlib.sha256(table.encode()).hexdigest()=='dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf','native q9 table pin')
    equal=accepted=terminal=0;failure_codes=set();counter_changed=0
    for bits in itertools.product(range(2),repeat=6):
        x,u,my,mr,a,b=bits;stop=(a,b)==(0,1)
        outputs=[]
        for coeffs in ((4,5,7),(4,7,5)):
            outputs.append(int(table[index(bits+coeffs,(2,)*6+(8,)*3)],16))
        need(outputs[0]==outputs[1],'swapped controllers have identical complete q9 output')
        equal+=1
        if stop:
            terminal+=1;failure_codes.add(outputs[0])
        else:
            accepted+=1
            y=x^u
            need(outputs[0]==2*(y^a)+(y^b),'preserved native accepted phase code')
        # An actual different retained preparation must be noticed; this is
        # a sensitivity control, not an available setting or a proposed fix.
        other=int(table[index(bits+(0,0,0),(2,)*6+(8,)*3)],16)
        counter_changed+=other!=outputs[0]
    need(equal==64 and accepted==48 and terminal==16,'complete source/failure row coverage')
    need(len(failure_codes)>1 and counter_changed>0,'nonvacuous dirty failure and changed-preparation controls')
    raw=(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes()
    need(hashlib.sha256(raw).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','source inventory pin')
    geo=selector_geometry(json.loads(raw)['sources'])

    # Representative factor of the derived full joint law: retain the whole
    # selector G, a complete boundary V and its identical public V record,
    # plus one raw port triple. This is arithmetic, not a large-L replay.
    passive={a:Counter() for a in (0,1)}
    active={a:Counter() for a in (0,1)}
    for record,output,newraw in itertools.product(range(8),repeat=3):
        setting=record>>2
        vrecord=output
        need(vrecord==output,'stipulated V record copies the actual carrier field')
        passive[setting][(output,vrecord,newraw)]+=Fraction(1,512)
    for setting in (0,1):
        need(sum(passive[setting].values())==Fraction(1,2),'selector raw branch mass')
        need({v:2*p for v,p in passive[setting].items()}=={(v,v,r):Fraction(1,64) for v,r in itertools.product(range(8),repeat=2)},'selector-conditioned joint carrier/record factor identical')
    # Deliberately supplied classical reversible actuator, only to ensure
    # the test detects a real conditional change when one is present.
    for setting in (0,1):
        active[setting][0^(4*setting)]=Fraction(1)
    tv=Fraction(1,2)*sum(abs(active[0][v]-active[1][v]) for v in range(8))
    need(tv==1,'classical actuator positive countercontrol')
    selector_tv=sum(abs(passive[0][v]-passive[1][v]) for v in set(passive[0])|set(passive[1]))
    same_kernel=passive[0]==passive[1]
    need(same_kernel,'passive selector countercontrol')
    return {'status':'PASS','verdict':('NO_DISTINCT_KERNELS_FOR_PASSIVE_SELECTOR_CANDIDATE' if same_kernel else 'DISTINCT_CONDITIONAL_FACTORS_NEED_NATIVE_ACTUATION'),
            'scope':'conditional recorded-selector test, not programmable interventions or a general no-go',
            'equal_controller_raw_rows':equal,'accepted_rows':accepted,'terminal_microscopic_rows':terminal,
            'changed_preparation_control_rows':counter_changed,
            'public_feedback_boundary_ticks':77,'public_feedback_center_ticks':78,
            'first_boundary_feedback_over_L':81,'first_center_feedback_over_L':82,
            'selector_branch_mass':'1/2','selector_conditioned_joint_factor_TV':str(selector_tv),
            'classical_actuator_countercontrol_TV':str(tv),
            'selector_geometry':geo,'native_measurement_interface':'NOT_ESTABLISHED',
            'new_access_or_preparation_adopted':False,'quantum_benchmark_runs':0}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2]/'oi-qm/reconstruction/native-y-continuation-20261024')
    args=parser.parse_args()
    try:result=run(args.source_root)
    except (RuntimeError,ValueError,KeyError,OSError) as exc:
        print(json.dumps({'status':'VOID','reason':str(exc)},sort_keys=True));raise SystemExit(2)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
