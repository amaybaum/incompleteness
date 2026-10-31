#!/usr/bin/env python3
"""Actual port-5 randomized setting, existing two-step record/carrier window."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

D=((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))
ORDER=(1,2,4,0,3,5)
LAUNCH=(D[0],D[3],D[0],D[3],D[3],D[5])


def need(ok,why):
    if not ok: raise RuntimeError(why)


def pinned(path,digest):
    raw=path.read_bytes()
    need(hashlib.sha256(raw).hexdigest()==digest,'input pin '+str(path))
    return raw


def h(code):
    a,b,d=code>>2,(code>>1)&1,code&1
    return 4*b+2*d+(a^(b&d))


def tv(left,right):
    nl,nr=sum(left.values()),sum(right.values())
    need(nl>0 and nr>0,'positive-mass branch comparator')
    return sum(abs(Fraction(left[k],nl)-Fraction(right[k],nr))
               for k in set(left)|set(right))/2


def view(r,x,y):
    return (r&3,x,y)


def run(root,contract):
    path=root/'native_vread_v15/checks.py'
    pinned(path,'93b4161f32e02874769d57d8a670d1a460d26fa2c953d517db5c6564fb649824')
    pinned(contract,'1a0b34ebb0c7115dd5faae11d2ab20c25ecf8a6f091ea292eb184e4311be7633')
    raw=pinned(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json',
               '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d')
    sources=json.loads(raw)['sources']
    need(len(sources)==1479,'entire compiled-source inventory')
    inventory={tuple(s['position']) for s in sources}
    spec=importlib.util.spec_from_file_location('retained_preparation',path)
    v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
    need(all(h(c)==v.h(c) for c in range(8)),'unchanged nonlinear native rule')
    _,balls=v.ready_balls();q=v.Q10;tau=v.L+3
    setting_time=v.S+4
    port,axis,deadline=v.PORTS[5]
    bank=v.add(port,axis,setting_time)
    rows=[('R',setting_time,port,bank,'BANK'),
          ('N',v.L+2,q,v.add(q,D[3],v.L+2),'FREE')]
    for off in (2,3,4,5):
        t=v.L+off
        rows += [('B%d:%d'%(off,i),t,v.add(q,D[i]),
                  v.add(v.add(q,D[i]),LAUNCH[i],t),'FREE') for i in ORDER]
        if off>=4:
            rows += [('W%d:%d'%(off,i),t,p,v.add(p,d,t),'BANK')
                     for i,(p,d,_) in enumerate(v.PORTS)]
    need(len(rows)==42 and len({r[3] for r in rows})==42,'42 distinct original triples')
    edges=[];classes=Counter()
    for i,(name,t,site,key,kind) in enumerate(rows):
        need(v.classify(key,inventory,balls)[0]==kind,'original key class '+name)
        need(key not in inventory and key not in v.local_sources().values(),'no source exception overwritten')
        need(v.dist(key,site)==t and sum(a!=b for a,b in zip(key,site))==1,
             'own uniquely axial diagonal '+name)
        affected=[j for j,(_,tt,ss,_,_) in enumerate(rows) if v.dist(key,ss)<=tt]
        need(i in affected and min(affected)==i,'chronological triangular map '+name)
        need(v.dist(key,q)>v.L+1,'all keys excluded original Q')
        if kind=='FREE':
            need(all(any(key[j]!=p[j] for j in range(3) if d[j]==0)
                     for p,d,_ in v.PORTS),'packet key off complete bank lines')
        edges.append(affected);classes[kind]+=1
    footprint=[q]+[v.add(q,d) for d in D]
    need(min(v.dist(bank,s) for s in footprint)>tau,'setting source absent both incoming slices at use')
    need(v.bank_index(bank)==(5,4),'existing S+4 selector bank block')
    need(all(v.dist(bank,p)>setting_time for i,(p,_,_) in enumerate(v.PORTS) if i!=5),
         'own selector diagonal absent every earlier public record')
    old_core=[((0,v.S,68+k),v.R+k) for k in range(10)]
    need(all(v.dist(bank,s)>t for s,t in old_core),'setting key cannot alter old source-phase flags')
    incoming_keys=[r[3] for r in rows[1:14]]
    need(all(min(v.dist(k,p) for p,_,_ in v.PORTS)>tau and
             v.dist(k,v.Q9)>v.L for k in incoming_keys),
         'incoming witnesses absent old raw-port history and q9 phase')
    need([i for i,r in enumerate(rows[:14]) if i>0 and v.dist(r[3],v.Q9)<=v.L+2]==[4],
         'optional V retained as incoming packet label, not independent history')
    future_keys=[r[3] for r in rows[14:]]
    need(len(future_keys)==28 and all(min(v.dist(k,s) for s in footprint)>tau for k in future_keys)
         and all(min(v.dist(k,p) for p,_,_ in v.PORTS)>tau for k in future_keys),
         'future original blocks absent incoming packet and complete past ports')
    need(all(v.dist(k,v.Q9)>v.L+2 for k in future_keys),'future blocks absent stipulated V')
    side=256*v.L+64*v.T+1
    points=[r[3] for r in rows]+[r[2] for r in rows]+list(inventory)+list(v.local_sources().values())
    need(all(max(p[j] for p in points)-min(p[j] for p in points)<side//2 for j in range(3)),
         'no torus shortcut')
    possible={}
    for off in (4,5):
        t=v.L+off
        possible['L+%d'%off]={'current_boundary_directions':[
            i for i,d in enumerate(D) if v.dist(bank,v.add(q,d))<=t and
            (t-v.dist(bank,v.add(q,d)))%2==0],
            'center':v.dist(bank,q)<=t and (t-v.dist(bank,q))%2==0}
    need(possible['L+4']=={'current_boundary_directions':[3,4],'center':False}
         and possible['L+5']=={'current_boundary_directions':[],'center':True},
         'actual original-bank causal/parity trace, not an isolated port write')
    # Every native first-front map is bijective in arbitrary fixed backgrounds.
    for old,bg in itertools.product(range(8),repeat=2):
        need(len({old^h(c^bg) for c in range(8)})==8,'all diagonal background maps')
    # Small exact triangular controls; these are arithmetic, not native replays.
    factors={r:Counter() for r in range(8)}
    for r in range(8):
        for a,b,c in itertools.product(range(8),repeat=3):
            x=h(a^r)^((r+3)%8)
            y=h(b^x)^((r+5)%8)
            z=h(c^y)^((r+7)%8)
            factors[r][(x,y,z)]+=1
    all_words=set(itertools.product(range(8),repeat=3))
    need(all(set(f)==all_words and set(f.values())=={1} for f in factors.values()),
         'joint triangular product control for every whole raw setting')
    grouped={c:Counter() for c in (0,1)}
    for r,factor in factors.items():
        for (x,y,z),mass in factor.items():grouped[r>>2][(r&3,x,y,z)]+=mass
    comparison=tv(grouped[0],grouped[1])
    # A joint-only leak must be detected even when coarse marginals agree.
    leak={c:Counter() for c in (0,1)};coarse={c:Counter() for c in (0,1)}
    for r,u in itertools.product(range(8),repeat=2):
        c=r>>2;y=u^(4*(c^(r&1)))
        leak[c][view(r,u,y)]+=1;coarse[c][(u,y)]+=1
    need(tv(leak[0],leak[1])==1 and tv(coarse[0],coarse[1])==0,
         'whole R.B/D joint leakage control, no marginal-only comparator')
    active_tvs=[]
    for old,total in itertools.product(range(8),repeat=2):
        center=old^h(total)
        active_tvs.append(tv(Counter({center:1}),Counter({center^4:1})))
    need(min(active_tvs)==1,'supplied center-actuator detected at fixed incoming state')
    # Original context/failure coverage; no success probability inferred from rows.
    contexts=list(itertools.product((0,1),repeat=6))
    terminal=sum((a,b)==(0,1) for x,u,my,mr,a,b in contexts)
    need(len(contexts)==64 and terminal==16,'all legacy microscopic terminal contexts retained')
    return {'schema':'oi.native-random-setting.v1','status':'PASS',
            'verdict':('NO_DISTINCT_JOINT_KERNELS_FOR_S4_SETTING_IN_L4_L5_WINDOW'
                       if comparison==0 else 'JOINT_COMPARISON_REQUIRES_REVIEW'),
            'parent':'4095d98564c835de4a1d4584af5275e3b91d668b',
            'setting_record':'whole U_(S+4)(port5), bit=A; B/D retained',
            'original_joint_product_triples':len(rows),'key_classes':dict(classes),
            'conservative_dependency_edges':edges,'original_bank_possible_influence':possible,
            'use_cut_independence':'raw R independent of incoming K on fixed original continuing preparation',
            'optional_V':'incoming packet coordinate; not an independent extra factor',
            'full_conditional_label_path_mass':'8^-42',
            'two_step_future_kernel_mass_given_input_and_setting':'8^-28 times both shape constraints',
            'future_output_triples_per_step':{'boundary':6,'raw_public':8},
            'representative_joint_setting_TV':str(comparison),
            'joint_only_leak_TV':'1','leak_after_discarding_R_tail_TV':'0',
            'supplied_actuator_min_TV':str(min(active_tvs)),
            'terminal_diagnostic_rows':terminal,'continuing_diagnostic_rows':64-terminal,
            'terminal_new_reads_or_offers':0,'native_field_simulations':0,
            'new_sources_writes_resets':0,'prior_or_access_adoption':False,
            'outgoing_environment':'full original-key native pushforward retained, not asserted setting-independent',
            'scope':'fixed passive read dictionary and two existing ticks; no general randomized-control no-go'}


if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2] /
                    'oi-qm/reconstruction/native-y-continuation-20261024')
    ap.add_argument('--contract',type=Path);args=ap.parse_args()
    try:result=run(args.source_root,args.contract or args.source_root/'shared_v12/INTERFACE-CONTRACT.md')
    except (RuntimeError,ValueError,KeyError,OSError,TypeError) as exc:
        print(json.dumps({'status':'VOID','reason':str(exc)},sort_keys=True));raise SystemExit(2)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
