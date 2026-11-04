#!/usr/bin/env python3
"""Bounded geometry/algebra for native-port5-cone-reduction.md, not a 78-tick replay."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path

PIN = "2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d"

def require(ok, reason):
    if not ok:
        raise AssertionError(reason)

def h(v):
    a,b,d=(v>>2)&1,(v>>1)&1,v&1
    return (b<<2)|(d<<1)|(a^(b&d))

def distance(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))

def parity_cone_count(r):
    return sum(4*d*d+2 if d else 1 for d in range(r%2,r+1,2))

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--source-inventory",type=Path,required=True)
    args=parser.parse_args()
    raw=args.source_inventory.read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PIN,"source inventory hash")
    sources=json.loads(raw)["sources"]
    require(len(sources)==1479,"source inventory count")
    T=185; P=12*840**185; S=P+T; R=S+68; L=R+9
    horizon=L+79; t0=L+1; side=256*L+64*T+1
    q=(0,S,78)
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
    deadlines=[T,T,S,S,S,S,R,L]
    key=(0,S+horizon,0)
    ready=list(zip(ports,deadlines))
    ready += [((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]+[((-48*L,0,0),L),(q,L+1)]
    require(len(ready)==25,"24 inherited ready balls plus q10")
    require(horizon-t0==distance(q,ports[5])==78,"port5 first-arrival distance")
    require(all(distance(q,p)>78 for i,p in enumerate(ports) if i!=5),"other declared ports farther")
    # These coordinates and the initial backward balls lie inside one no-wrap chart.
    require(max(abs(x-y) for a in [key,q]+ports for b in [key,q]+ports for x,y in zip(a,b))<side//2,"no torus shortcut")
    require(distance(key,ports[5])==horizon,"own bank axial first arrival")
    require(all(distance(key,p)>horizon for i,p in enumerate(ports) if i!=5),"key absent all other ports through horizon")
    require(distance(key,q)-t0==156,"key absent q10 at L+1")
    require(distance(key,(0,S,77))-(L+2)==154,"key absent old q9 and V")
    require(min(distance(key,c)-r for c,r in ready)==156,"key outside all readiness")
    require(all(tuple(r["position"])!=key for r in sources),"key not an old source")
    require(key not in [(0,-78,78),(0,S,S+156),(4*T,P+S,0),(0,S,-S-136)],"key not added E/N or indexed sources")
    require(S<horizon<=2*L,"candidate bank horizon range")
    # On each unique axial path old-local and off-path terms are source-independent.
    require(len({h(k) for k in range(8)})==8,"H permutation")
    families=0
    for a,b in itertools.product(range(8),repeat=2):
        out=[a^h(k^b) for k in range(8)]
        require(len(set(out))==8,"one-step translated permutation")
        families+=1
    for seed in range(3):
        values=list(range(8))
        for tick in range(78):
            a=(3*tick+seed)%8;b=(tick*tick+5*seed)%8
            values=[a^h(v^b) for v in values]
        require(len(set(values))==8,"78 translated-permutation composition")
    # A uniform independent initial key gives every raw endpoint symbol once
    # for each fixed operand/background. Pinning the key destroys this mask.
    mask_rows=0
    for a,b,operand in itertools.product(range(8),repeat=3):
        values=[a^h(operand^b^k) for k in range(8)]
        require(sorted(values)==list(range(8)),"uniform-key conditional endpoint law")
        mask_rows+=1
    require(len({h(operand) for operand in range(8)})==8,"fixed-key positive operand control")
    require(parity_cone_count(78)==328719 and parity_cone_count(77)==316394,"late-cut two-slice cone counts")
    print(json.dumps({"status":"PASS","transport_ticks":78,
       "late_current_structural_cone":328719,"late_previous_structural_cone":316394,
       "initial_key":"(0,S+L+79,0)=f5(L+79)",
       "key_q10_cone_slack":156,"minimum_ready_slack":156,
       "source_rows":len(sources),"translated_permutation_families":families,
       "uniform_key_local_laws":mask_rows,
       "scope":"conditional geometry/first-arrival pad; no full-history/carrier replay or second setting"},sort_keys=True))

if __name__=="__main__":
    main()
