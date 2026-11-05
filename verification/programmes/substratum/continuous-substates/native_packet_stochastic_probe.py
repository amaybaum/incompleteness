#!/usr/bin/env python3
"""Two passive native packet steps under retained original product-key laws."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path


def need(ok, why):
    if not ok: raise RuntimeError(why)


def h(c):
    a,b,d=c>>2,(c>>1)&1,c&1
    return 4*b+2*d+(a^(b&d))


def hinv(c):
    a,b,d=c>>2,(c>>1)&1,c&1
    return 4*(d^(a&b))+2*a+b


D=tuple(tuple(s if j==a else 0 for j in range(3)) for a in range(3) for s in (-1,1))
Z=(0,0,0);BALL=(Z,)+D;ORDER=(1,2,4,0,3,5)
LAUNCH=(D[0],D[3],D[0],D[3],D[3],D[5])


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def scale(n,v): return tuple(n*x for x in v)
def dist(a,b): return sum(abs(x-y) for x,y in zip(a,b))


def xor(values):
    r=0
    for v in values:r^=v
    return r


def idx(values,sizes):
    r=0
    for v,n in zip(values,sizes):r=n*r+v
    return r


def rank(rows):
    pivots={}
    for r in rows:
        while r:
            b=r.bit_length()-1
            if b not in pivots:pivots[b]=r;break
            r^=pivots[b]
    return len(pivots)


def boundary_keys(q,t): return [add(add(q,d),scale(t,a)) for d,a in zip(D,LAUNCH)]


def geometry(sources):
    T=185;P=12*840**185;S=P+T;R=S+68;L=R+9;q=(0,S,78)
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
    deadlines=[T,T,S,S,S,S,R,L]
    banks=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0),(1,0,0)]
    ready=list(zip(ports,deadlines))+[((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]+[((-48*L,0,0),L),(q,L+1)]
    need(len(ready)==25 and len(sources)==1479,'complete declared inventory counts')
    old={tuple(s['position']) for s in sources}
    extra={(0,-78,78),(0,S,S+156),(4*T,P+S,0),(0,S,-S-136)}
    stages=[];allkeys=[];blocks=[]
    for stage in (1,2):
        t=L+3+stage;bk=boundary_keys(q,t);nk=[add(p,scale(t,a)) for p,a in zip(ports,banks)]
        need([min(dist(k,c)-r for c,r in ready) for k in bk]==[stage+3]*6,'boundary keys outside every ready region')
        need([min(dist(k,p) for p in ports)-L for k in bk]==[stage+82,stage+82,stage+80,stage+82,stage+80,stage+82],'boundary keys absent all records through H')
        cross=[]
        for i,k in enumerate(bk):
            need(dist(k,add(q,D[i]))==t,'own straight axial first arrival')
            need(all(dist(k,add(q,v))>t-1 for v in BALL),'key absent entire earlier packet')
            need(dist(k,(0,S,77))>L+2,'key absent stipulated q9/V reads')
            for j,d in enumerate(D):
                if i!=j and dist(k,add(q,d))<=t:cross.append((i,j))
            for p,a in zip(ports,banks):
                axis=next(j for j in range(3) if a[j])
                need(any(k[j]!=p[j] for j in range(3) if j!=axis),'boundary key outside bank line')
        need(cross==[(1,3),(2,0),(4,3)],'triangular six-boundary cross graph')
        need(all(ORDER.index(i)<ORDER.index(j) for i,j in cross),'boundary inversion order')
        bankcross=[]
        for i,k in enumerate(nk):
            need(dist(k,ports[i])==t and all(dist(k,p)>=t for p in ports),'bank chronological first arrival')
            bankcross.extend((i,j) for j,p in enumerate(ports) if i!=j and dist(k,p)==t)
            need(min(dist(k,add(q,v)) for v in BALL)>L+5,'bank excluded from both packet steps')
            need(min(dist(k,c)-r for c,r in ready)>0,'bank key unpinned')
        need(bankcross==[(2,5),(3,5)],'triangular eight-port cross graph')
        for k in bk+nk:
            need(k not in old and k not in extra,'key outside old and added source inventories')
            side=256*L+64*T+1
            need(max(abs(a-b) for p in ports+[k,q] for r in ports+[k,q] for a,b in zip(p,r))<side//2,'no torus shortcut')
        allkeys.extend(bk+nk);blocks.append((t,bk,nk))
        stages.append({'step':stage,'boundary_ready_slack':stage+3,'earliest_boundary_public_over_L':stage+80})
    need(len(set(allkeys))==28,'all two-stage original key blocks distinct')
    # Future keys cannot reach any earlier packet or record. Earlier-stage
    # dependence is retained by chronological inversion, not erased.
    t,bk,nk=blocks[1]
    need(all(min(dist(k,add(q,v)) for v in BALL)>L+4 for k in bk+nk),'future keys absent first outgoing packet')
    need(all(min(dist(k,p) for p in ports)>L+4 for k in bk+nk),'future keys absent first new record')
    return stages


def evaluator(overrides,seed,old_p=None):
    cache={}
    def value(t,v):
        if (t,v) not in cache:
            if t==0:r=overrides.get(v,(v[0]*v[1]+3*v[2]+5*seed+v[1])%8)
            elif t==-1:r=old_p if old_p is not None and v==(0,0,-1) else (v[1]*v[2]+5*v[0]+3*seed+v[2])%8
            else:r=value(t-2,v)^h(xor(value(t-1,add(v,d)) for d in D))
            cache[t,v]=r
        return cache[t,v]
    return value


def packet(v,t):return tuple(v(k,x) for k in (t,t-1) for x in BALL)


def reduced(k,e):
    c,p=k[:7],k[7:]
    return (p[0]^h(xor(c[1:])),)+tuple(p[i+1]^h(c[0]^e[i]) for i in range(6))+c


def run(root):
    qt=json.loads((root/'native_route_v13/result.json').read_text())['q10_table_hex']
    pt=json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    raw=(root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_bytes()
    pins=[(qt.encode(),'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc'),
          (pt.encode(),'dcb150b528926e6fa7f8eb2f4e3d36f5a60742090df63fc899db97d9a365cbcf'),
          (raw,'2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d')]
    need(all(hashlib.sha256(a).hexdigest()==b for a,b in pins),'input pins')
    need([h(c) for c in range(8)]==[0,2,4,7,1,3,5,6],'native truth table')
    need(all(hinv(h(c))==c for c in range(8)),'inverse h')
    geo=geometry(json.loads(raw)['sources'])
    shell=sorted({add(d,e) for d in D for e in D}-{Z})
    rows=[sum(1<<j for j,v in enumerate(shell) if dist(v,d)==1) for d in D]
    need(len(shell)==18 and all(r.bit_count()==5 for r in rows) and rank(rows)==6,'six incoming triples from eighteen-site shell')
    for i,d in enumerate(D):
        column=shell.index(scale(2,d))
        need([int(bool(r&(1<<column))) for r in rows]==[int(i==j) for j in range(6)],'private axial incidence columns')
    accepted=terminal=stage_rows=0
    for bits in itertools.product(range(2),repeat=6):
        x,u,my,mr,a,b=bits;s=x^u^a;stop=(a,b)==(0,1)
        e,n=4+2*(1^my)+1,4*my+2+(1^my)
        q=int(qt[idx(bits+(e,n),(2,)*6+(8,8))],16)
        p=int(pt[idx(bits+(4,5,7),(2,)*6+(8,)*3)],16)
        if not stop:need(q>>2==s and p==2*s+(s^a^b),'actual accepted phase')
        v=evaluator({Z:q},0,p)
        for t in (2,3):
            k=packet(v,t);out=packet(v,t+1)
            env=tuple(xor(v(t,x) for x in shell if dist(x,d)==1) for d in D)
            need(reduced(k,env)==out,'complete two-stage raw packet update')
            need(tuple(k[0]^hinv(k[8+i]^out[i+1]) for i in range(6))==env,'incoming-kernel inverse')
            stage_rows+=1
        if stop:terminal+=1
        else:accepted+=1
    # Small dense original-time controls for the unrolled triangular map.
    labels=[(t,i) for t in (3,4) for i in ORDER]
    keys=[boundary_keys(Z,t)[i] for t,i in labels]
    need(len(set(keys))==12,'small two-stage source keys distinct')
    worlds=0
    for seed in range(3):
        fixed={k:(j+3*seed)%8 for j,k in enumerate(keys)}
        for j,key in enumerate(keys):
            own=[];past=[];inputs=[]
            for value in range(8):
                original=dict(fixed);original[key]=value
                v=evaluator(original,seed)
                own.append(v(labels[j][0],D[labels[j][1]]))
                past.append(tuple(v(t,D[i]) for t,i in labels[:j]))
                inputs.append(packet(v,2));worlds+=1
            need(sorted(own)==list(range(8)),'each native diagonal block permutes all values')
            need(len(set(past))==len(set(inputs))==1,'future block leaves earlier outputs and initial packet fixed')
    # Native joint-control: a shared original key keeps both marginals fair
    # but loses the independent two-output law.
    pair=Counter();shared=Counter();k0=boundary_keys(Z,3)[0];k1=boundary_keys(Z,3)[1]
    for a,b in itertools.product(range(8),repeat=2):
        v=evaluator({k0:a,k1:b},0);out=v(3,D[0]),v(3,D[1]);pair[out]+=1
        if a==b:shared[out]+=1
    need(len(pair)==64 and all(n==1 for n in pair.values()),'independent native key pair')
    need(all([sum(n for p,n in shared.items() if p[i]==v) for v in range(8)]==[1]*8 for i in (0,1)),'shared-key fair marginals')
    tv=Fraction(1,2)*sum(abs(Fraction(shared[p],8)-Fraction(1,64)) for p in pair)
    need(tv==Fraction(7,8),'shared-key joint countercontrol')
    bankworlds=0
    for n in (2,3,4):
        for seed in (0,1):
            pairs=set()
            for a,b in itertools.product(range(8),repeat=2):
                v=evaluator({(1,n,0):a,(0,n+1,0):b},seed)
                pairs.add((v(n,(1,0,0)),v(n,(0,1,0))));bankworlds+=1
            need(len(pairs)==64,'native bank cross-arrival block')
    need(accepted==48 and terminal==16 and stage_rows==128 and worlds==288 and bankworlds==384,'nonvacuous source and terminal coverage')
    return {'status':'PASS','verdict':'TWO_PASSIVE_STEPS_CONDITIONAL',
            'scope':'internal packet and existing public record; no accessible measurement gate',
            'packet_bits':42,'outer_shell_triples':18,'incoming_bit_rank':18,
            'source_rows':64,'accepted_rows':accepted,'terminal_microscopic_rows':terminal,
            'raw_stage_checks':stage_rows,'native_triangular_control_worlds':worlds,
            'native_bank_control_worlds':bankworlds,'shared_key_TV':'7/8',
            'original_fresh_triples':28,'free_output_bits_per_step':42,
            'new_packet_reads':0,'measurement_reuse':'NOT_ESTABLISHED','geometry':geo}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,default=Path(__file__).resolve().parents[2]/'oi-qm/reconstruction/native-y-continuation-20261024')
    args=parser.parse_args()
    try:result=run(args.source_root)
    except (RuntimeError,ValueError,KeyError,OSError) as exc:
        print(json.dumps({'status':'VOID','reason':str(exc)},sort_keys=True));raise SystemExit(2)
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
