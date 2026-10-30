#!/usr/bin/env python3
"""Exact internal two-slice packet controls, not an observer read or gate."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path


def need(ok, reason):
    if not ok: raise RuntimeError(reason)


def h(c):
    a,b,d=c>>2,(c>>1)&1,c&1
    return 4*b+2*d+(a^(b&d))


DIRS=tuple(tuple(sign if j==axis else 0 for j in range(3))
           for axis in range(3) for sign in (-1,1))
ZERO=(0,0,0)


def add(a,b): return tuple(x+y for x,y in zip(a,b))


def xor(values):
    value=0
    for x in values: value^=x
    return value


def idx(values,sizes):
    out=0
    for value,size in zip(values,sizes): out=size*out+value
    return out


def distance(a,b): return sum(abs(x-y) for x,y in zip(a,b))


def geometry(sources):
    T=185; P=12*840**185; S=P+T; R=S+68; L=R+9
    q=(0,S,78); horizon=L+79
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
    deadlines=[T,T,S,S,S,S,R,L]
    ready=list(zip(ports,deadlines))+[((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]+[((-48*L,0,0),L),(q,L+1)]
    directions=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0),(1,0,0)]
    need(len(ready)==25 and len(sources)==1479,'complete input inventory counts')
    result=[]
    for j in (2,3,5):
        key=(0,S+L+j,78)
        need(min(distance(key,c)-r for c,r in ready)==j-1,'key outside all ready regions')
        need(all(tuple(x['position'])!=key for x in sources),'key not an old source')
        need(key not in [(0,-78,78),(0,S,S+156),(4*T,P+S,0),(0,S,-S-136)],'key not an added source')
        for port,d in zip(ports,directions):
            axis=next(i for i in range(3) if d[i])
            need(any(key[i]!=port[i] for i in range(3) if i!=axis),'key outside full bank line')
        need(min(distance(key,p) for p in ports)==L+j+78>horizon,'key absent permitted ports through H')
        need(distance(key,(0,S,77))>L+2,'key absent old q9 and V read')
        need(distance(key,q)==L+j,'unique axial arrival at q')
        if j==5:
            need(all(distance(key,add(q,v))>L+3 for v in (ZERO,)+DIRS),'closure key absent entire input packet')
            need(distance(key,add(q,(0,1,0)))==L+4,'closure key reaches output boundary')
        side=256*L+64*T+1
        need(max(abs(a-b) for p in ports+[key,q] for r in ports+[key,q] for a,b in zip(p,r))<side//2,'no torus shortcut')
        result.append({'key_depth':j,'ready_slack':j-1,'first_public_arrival_over_L':j+78})
    return result


def world(q,p,seed,alpha,beta,gamma=0):
    # Time zero here is the L+1 cut. Dirty fixtures check universal local
    # identities; they are not an adopted preparation or a large-L replay.
    cache={}
    def value(t,v):
        key=t,v
        if key in cache: return cache[key]
        if t==0:
            overrides={ZERO:q,(0,1,0):alpha,(0,2,0):beta,(0,4,0):gamma}
            result=overrides.get(v,(v[0]*v[1]+3*v[2]+5*seed+v[1])%8)
        elif t==-1:
            result=p if v==(0,0,-1) else (v[1]*v[2]+5*v[0]+3*seed+v[2])%8
        else:
            result=value(t-2,v)^h(xor(value(t-1,add(v,d)) for d in DIRS))
        cache[key]=result
        return result
    return value


def packet(value,t):
    # All three fields of every site in the radius-one ball, on both slices.
    return tuple(value(k,v) for k in (t,t-1) for v in (ZERO,)+DIRS)


def encoded(value,t):
    return (value(t,ZERO)>>2)^xor((value(t-1,d)>>1)&1 for d in DIRS)


def run(root):
    route=json.loads((root/'native_route_v13/result.json').read_text())
    old=json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())
    raw=(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes()
    qt,pt=route['q10_table_hex'],old['q9_table_hex']
    pins=[(qt.encode(),'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc'),
          (pt.encode(),'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf'),
          (raw,'2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d')]
    need(all(hashlib.sha256(data).hexdigest()==pin for data,pin in pins),'retained input pins')
    need([h(c) for c in range(8)]==[0,2,4,7,1,3,5,6],'native h truth table')
    geo=geometry(json.loads(raw)['sources'])
    rows=accepted=terminal=closures=encoding_failures=0
    for bits in itertools.product(range(2),repeat=6):
        x,u,my,mr,a,b=bits; s=x^u^a; is_terminal=(a,b)==(0,1)
        e,n=4+2*(1^my)+1,4*my+2+(1^my)
        q=int(qt[idx(bits+(e,n),(2,)*6+(8,8))],16)
        p=int(pt[idx(bits+(4,5,7),(2,)*6+(8,)*3)],16)
        if not is_terminal: need(q>>2==s and p==2*s+(s^a^b),'actual accepted source phase')
        for seed in (0,1):
            pairs=Counter(); shared=Counter()
            for alpha,beta in itertools.product(range(8),repeat=2):
                v=world(q,p,seed,alpha,beta)
                pair=v(2,ZERO),v(1,ZERO)
                pairs[pair]+=1
                need(encoded(v,2)==q>>2,'complete parity retains actual input A')
                need(encoded(v,3)==v(1,ZERO)>>2,'one-step parity shift identity')
                if not is_terminal: need(encoded(v,2)==s,'encoded actual sign')
                if (v(2,ZERO)>>2)!=(q>>2): encoding_failures+=1
                if alpha==beta: shared[pair]+=1
                rows+=1
            need(pairs==Counter({pair:1 for pair in itertools.product(range(8),repeat=2)}),'full same-site pair uniform on 64 values')
            for i in (0,1):
                need([sum(n for pair,n in shared.items() if pair[i]==v) for v in range(8)]==[1]*8,'shared-key marginals remain uniform')
            tv=Fraction(1,2)*sum(abs(Fraction(shared[k],8)-Fraction(1,64)) for k in pairs)
            need(tv==Fraction(7,8),'shared-key countercontrol: fair marginals do not imply fair pair')
            if is_terminal: terminal+=1
            else: accepted+=1
        # Complete input packet is unchanged by a distant current-site fixture,
        # while the next native output boundary permutes all eight values.
        inputs=[]; outputs=[]
        for gamma in range(8):
            v=world(q,p,0,1,2,gamma)
            inputs.append(packet(v,2)); outputs.append(v(3,(0,1,0)))
        need(len(set(inputs))==1,'closure countercontrol fixes all 42 input bits')
        need(sorted(outputs)==list(range(8)),'next boundary depends on omitted environment')
        closures+=1
    need(rows==8192 and accepted==96 and terminal==32 and closures==64,'nonvacuous source and branch coverage')
    need(encoding_failures>0,'dropping neighboring mask loses sign')
    return {'status':'PASS','same_site_pair_values':64,'packet_raw_bits':42,
            'pair_control_worlds':rows,'accepted_phase_families':accepted,
            'terminal_microscopic_families':terminal,'closure_fixture_families':closures,
            'shared_key_TV':'7/8','geometry':geo,
            'encoded_sign':'EXACT_ON_ACCEPTED_PHASE',
            'raw_packet_deterministic_closure':False,'new_reads':0,'reusable_gate':'NOT_ESTABLISHED',
            'scope':'conditional joint prior and internal packet; no observer decoder or operational closure verdict'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2]/'oi-qm/reconstruction/native-y-continuation-20261024')
    args=parser.parse_args()
    try: result=run(args.source_root)
    except (RuntimeError,ValueError,KeyError,OSError) as exc:
        print(json.dumps({'status':'VOID','reason':str(exc)},sort_keys=True));raise SystemExit(2)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
