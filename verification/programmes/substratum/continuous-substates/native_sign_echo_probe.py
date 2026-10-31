#!/usr/bin/env python3
"""Exact two-tick native sign-echo controls; not a later-cut measurement."""
import argparse
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path

PINS = {'q10': 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc',
        'q9': 'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf',
        'inventory': '2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d'}


def need(ok, why):
    if not ok:
        raise RuntimeError(why)


def h(code):
    a, b, d = code >> 2, (code >> 1) & 1, code & 1
    return 4*b + 2*d + (a ^ (b & d))


DIRS = tuple(tuple(sign if i == axis else 0 for i in range(3))
             for axis in range(3) for sign in (-1, 1))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def xor(values):
    out = 0
    for value in values:
        out ^= value
    return out


def distance(a, b):
    return sum(abs(x-y) for x, y in zip(a, b))


def idx(values, sizes):
    out = 0
    for value, size in zip(values, sizes):
        out = out*size + value
    return out


def geometry(sources):
    T=185; P=12*840**185; S=P+T; R=S+68; L=R+9
    q=(0,S,78); key=(0,S+L+3,78); end=L+3; horizon=L+79
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
    deadlines=[T,T,S,S,S,S,R,L]
    ready=list(zip(ports,deadlines))
    ready += [((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]+[((-48*L,0,0),L),(q,L+1)]
    need(len(ready)==25 and min(distance(key,c)-r for c,r in ready)==2, 'key outside all declared ready balls')
    need(len(sources)==1479 and all(tuple(x['position'])!=key for x in sources), 'key outside old sources')
    need(key not in [(0,-78,78),(0,S,S+156),(4*T,P+S,0),(0,S,-S-136)], 'key outside additional sources')
    banks=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0),(1,0,0)]
    for port, direction in zip(ports,banks):
        axis=next(i for i in range(3) if direction[i])
        need(any(key[i]!=port[i] for i in range(3) if i!=axis), 'key outside complete bank line')
    need(min(distance(key,p) for p in ports)-L==81, 'first public arrival L+81')
    need(all(distance(key,p)>horizon for p in ports), 'all prospective public records unaffected')
    need(distance(key,(0,S,77))-(L+2)==2, 'stipulated V read unaffected')
    need(distance(key,q)==end and distance(key,q)-(L+1)==2, 'exact two-tick first arrival beyond q10 deadline')
    outer=[add(q,tuple(2*x for x in d)) for d in DIRS]
    hit=[i for i,v in enumerate(outer) if distance(key,v)<=L+1]
    need(hit==[3] and distance(key,outer[3])==L+1, 'only positive-y outer site affected at input cut')
    need(all(distance(key,add(q,d))>L for d in DIRS), 'previous-neighbor mask inputs unaffected')
    side=256*L+64*T+1
    need(max(abs(a-b) for p in ports+[key,q] for r in ports+[key,q] for a,b in zip(p,r))<side//2, 'no torus shortcut')
    return {'ready_slack':2,'first_public_arrival_over_L':81,'public_horizon_slack':2}


def run(root):
    route=json.loads((root/'native_route_v13/result.json').read_text())
    old=json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())
    raw=(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes()
    qtable, ptable=route['q10_table_hex'],old['q9_table_hex']
    need(len(qtable)==4096 and len(ptable)==32768, 'input table lengths')
    for name, data in [('q10',qtable.encode()),('q9',ptable.encode()),('inventory',raw)]:
        need(hashlib.sha256(data).hexdigest()==PINS[name], 'input pin '+name)
    geo=geometry(json.loads(raw)['sources'])
    need([h(k) for k in range(8)]==[0,2,4,7,1,3,5,6], 'complete native h truth table')
    origin=(0,0,0); keysite=(0,2,0)
    sites={origin}|set(DIRS)|{add(d,e) for d in DIRS for e in DIRS}
    oldsites={origin}|set(DIRS)
    rows=accepted=terminal=omission_changes=leak_controls=0
    echo_laws=[]
    for values in itertools.product(range(2),repeat=6):
        x,u,my,mr,a,b=values; s=x^u^a
        e,n=4+2*(1^my)+1,4*my+2+(1^my)
        q=int(qtable[idx(values+(e,n),(2,)*6+(8,8))],16)
        p=int(ptable[idx(values+(4,5,7),(2,)*6+(8,)*3)],16)
        is_terminal=(a,b)==(0,1)
        if not is_terminal:
            need(q>>2==s and p==2*s+(s^a^b), 'accepted actual phase fields')
        for seed in (0,1):
            # Dirty phase fixtures validate the universal stencil algebra.
            # They are not an adopted original-time prior or a large-L replay.
            current={v:(v[0]*v[1]+3*v[2]+5*seed+u+2*my+mr)%8 for v in sites}
            previous={v:(v[1]*v[2]+5*v[0]+3*seed+a+2*b)%8 for v in oldsites}
            current[origin]=q; previous[(0,0,-1)]=p
            outputs=[]; midvalues=[]
            for keyvalue in range(8):
                current[keysite]=keyvalue
                middle={v:previous[v]^h(xor(current[add(v,d)] for d in DIRS)) for v in oldsites}
                sigma=xor(middle[d] for d in DIRS)
                result=current[origin]^h(sigma)
                mask=xor((previous[d]>>1)&1 for d in DIRS)^xor(current[tuple(2*c for c in d)]&1 for d in DIRS)
                need((result>>2)==(q>>2)^mask, 'exact twelve-bit two-tick A identity')
                omission_changes += (h(sigma)>>2)!=(result>>2)
                # Keep the complete triples in the physical packet; no B/D reset.
                outputs.append(result); midvalues.append(middle[origin])
                need(is_terminal or q>>2==s, 'accepted sign operand')
                rows+=1
            need(sorted(outputs)==list(range(8)), 'full current raw triple permutes outer key')
            need(len(set(midvalues))==1, 'previous local slice independent of outer key')
            need(Counter(v>>2 for v in outputs)=={0:4,1:4}, 'raw A remains balanced')
            # Only a microscopic evolution was evaluated, including on terminal
            # trajectories. No new read or offered carrier is part of this test.
            if is_terminal: terminal+=1
            else:
                accepted+=1
                echo_laws.append(all(v>>2==s for v in outputs))
            need(len(set(outputs))>1, 'fixed-key versus variable-key countercontrol')
            leak_controls+=1
    need(rows==1024 and accepted==96 and terminal==32, 'nonvacuous raw-branch coverage')
    need(omission_changes>0 and leak_controls==128, 'old-local and free-key controls')
    # Verdict after controls, computed from the measured complete-key laws.
    return {'status':'PASS','geometry':geo,'native_patch_worlds':rows,
            'accepted_phase_families':accepted,'terminal_microscopic_families':terminal,
            'new_reads':0,'offered_reusable_carriers':0,
            'clean_raw_A_echo':all(echo_laws),
            'verdict': 'CLEAN_RAW_ECHO' if all(echo_laws) else 'MASKED_RAW_ECHO',
            'scope':'two-tick q10 feedback only; encoded/distributed gates and measurement remain open'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2]/'oi-qm/reconstruction/native-y-continuation-20261024')
    args=parser.parse_args()
    try: result=run(args.source_root)
    except (RuntimeError,ValueError,KeyError,OSError) as exc:
        print(json.dumps({'status':'VOID','reason':str(exc)},sort_keys=True));raise SystemExit(2)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
