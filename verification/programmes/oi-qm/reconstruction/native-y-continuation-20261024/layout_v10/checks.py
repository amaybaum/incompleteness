#!/usr/bin/env python3
"""Exact bounded alternate-front probe. No native baseline code imported."""
import argparse,hashlib,json
from pathlib import Path
from functools import lru_cache
from itertools import product

ZERO=(0,0,0);BITS=tuple(product((0,1),repeat=3))
T=185;P=12*840**T;S=T+P;R=S+68;L=R+9

def need(ok,msg):
    if not ok:raise RuntimeError(msg)

def H(q):a,b,c=q;return b,c,a^(b&c)
def hp(q,n):
    for _ in range(n%12):q=H(q)
    return q

def xor(*vs):return tuple(__import__('functools').reduce(int.__xor__,(v[k] for v in vs),0) for k in range(3))
def odd(*coords):
    taken=0
    for q in coords:
        if taken&q:return False
        taken|=q
    return True

def dist(a,b):return sum(abs(x-y) for x,y in zip(a,b))

def front(x,W,m,rmax,kmax,jmax):
    old={(r,k):hp(W,r+m-1+k) if odd(r,m-1,k) else ZERO for r in range(rmax+1) for k in range(kmax+1)}
    result={-1:old}
    for j in range(jmax+1):
        now={}
        for r in range(rmax+1):
            for k in range(kmax+1):
                down=now[r,k-1] if k else hp((0,x,0),r+j+m-1) if odd(r,j,m-1) else ZERO
                now[r,k]=H(xor(old[r,k],now.get((r-1,k),ZERO),down))
        old=now;result[j]=now
    return result

def driven(F,x,W,m,r,j,k,deadline,payload):
    state=hp(payload,deadline-r-1)
    for a in range(r+1):
        down=F[j][a,k-1] if k else hp((0,x,0),a+j+m-1) if odd(a,j,m-1) else ZERO
        state=H(xor(state,F[j-1][a,k],down))
    return state

def cycles(perm):
    unseen=set(range(len(perm)));out=[]
    while unseen:
        start=min(unseen);path=[];v=start
        while v in unseen:unseen.remove(v);path.append(v);v=perm[v]
        need(v==start,'permutation cycle closure');out.append(path)
    return out

def geometry(path):
    raw=path.read_bytes()
    need(hashlib.sha256(raw).hexdigest()=='2642e1a68825faa5d3bb1049e8722adec1ec33bd3f56b9e4416b2c902a85ec5d','inherited source geometry digest')
    source=json.loads(raw);sources=source['sources']
    need(len(sources)==1479,'retained source census')
    ps=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0)]
    deadlines=[T,T,S,S,S,S,R]
    rays=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0)]
    added=[(0,2*S,0),(T,S+P,0),(-T,S+P,0),(4*T,S+P,0),
           (0,S,S+136),(0,S,-S-136),(0,S,S+150),(0,S,S+152),(0,S,S+154)]
    targets=[(10,S-delta,67+delta) for delta in range(11,25)]
    minus=[(q[0]-L,q[1],q[2]) for q in targets]
    count=0;bankchecks=0
    for q,B in zip(targets,minus):
        need(dist(q,(0,0,0))==dist(q,(0,-76,76))==L,'two actual first fronts')
        need(B[0]<-T,'minus source x excludes every old bank ray')
        for row in sources:
            d=dist(q,row['position'])
            need(d==L if row['owner']=='input' else d>L,'all inherited source exclusions')
            count+=1
        need(all(dist(q,p)>L for p in added),'all later control/source exclusions')
        need(all(dist(B,p)>a for p,a in zip(ps,deadlines)),'minus-x preserves public deadlines')
        need(dist(B,(0,S,76))>R+8,'minus-x preserves q8')
        for p,a,e in zip(ps,deadlines,rays):
            axis=next(i for i,b in enumerate(e) if b)
            ts={a+1,L};critical=(q[axis]-p[axis])*e[axis]
            if a+1<=critical<=L:ts.add(critical)
            for t in ts:
                f=tuple(c+t*b for c,b in zip(p,e))
                need(dist(f,q)>L,'whole frontier family outside new ready cone')
                need(f!=B,'new source does not overwrite bank')
            bankchecks+=1
        # Entire new current cone is below x=~L while the old remote programs
        # lie at x>=12R or x<=-12R. The inherited source list covers the rest.
        need(12*R-q[0]>L and q[0]+12*R>L,'old remote programs excluded')
        for other,Bother in zip(targets,minus):
            if other!=q:need(dist(Bother,q)>L,'simultaneous mask paths do not cross')
    q=targets[2];Bplus=(q[0]+L,q[1],q[2])
    slack=dist(Bplus,ps[4])-S
    need(slack==-401,'positive-x source violates old Z informative cone')
    need(all(dist(q,(0,S,76))>1 for q in targets),'late-q8 substitution cannot reach endpoints')
    return {'source_sha256':hashlib.sha256(raw).hexdigest(),'original_source_tests':count,
            'frontier_family_exclusions':bankchecks,'plus_x_old_Z_deadline_slack':slack,
            'minus_x_source_geometry':'PASS','q8_operand_socket':'EXCLUDED_BY_LIGHT_CONE'}

def native_controls():
    # Exact direct recurrence on1024 packed assignments includes arbitrary W,
    # arbitrary previous-origin triple and all8 new source payloads.
    rows=list(product((0,1),BITS,BITS,BITS));full=(1<<len(rows))-1
    X=sum(x<<i for i,(x,w,b,old) in enumerate(rows))
    def pack(column):return tuple(sum(row[column][k]<<i for i,row in enumerate(rows)) for k in range(3))
    checks=0;nonlinear=0
    for m,r,j,k in [(2,1,2,1),(3,2,2,1),(4,2,3,2)]:
        end=(r,j,m+k);D=sum(end);Wpos=(0,-m,m);Bpos=(r-D,j,m+k)
        ini={(0,0,0):(0,X,0),Wpos:pack(1),Bpos:pack(2)};old=pack(3)
        @lru_cache(None)
        def field(t,p):
            if t==-1:return old if p==(0,0,0) else ZERO
            if t==0:return ini.get(p,ZERO)
            if min(dist(p,a) for a in ini)>t and dist(p,(0,0,0))>t+1:return ZERO
            ns=[]
            for axis in range(3):
                for direction in (-1,1):
                    w=list(p);w[axis]+=direction;ns.append(field(t-1,tuple(w)))
            return xor(field(t-2,p),H(xor(*ns)))
        got=field(D,end)
        need(field(D-1,end)==ZERO,'blank native prefix')
        Fs={(x,w):front(x,w,m,r,k,j) for x,w in product((0,1),BITS)}
        for lane,(x,w,b,previous) in enumerate(rows):
            want=driven(Fs[x,w],x,w,m,r,j,k,D,b)
            actual=tuple((z>>lane)&1 for z in got)
            need(actual==want,'independent native recurrence vs coupled axis model');checks+=1
            # A late-pulse surrogate neglects genuine earlier intersections.
            isolated=H(xor(hp(Fs[x,w][j][r,k],11),hp(b,D-1)))
            nonlinear+=actual!=isolated
    need(nonlinear>0,'isolated late-collision shortcut rejected')
    return {'direct_scalar_comparisons':checks,'late_collision_shortcut_mismatches':nonlinear}

def census():
    N=11*16
    need(P%(384*840**N)==0,'actual P divisible by proved triangular period')
    for r,j in product(range(11),range(384)):
        need(odd(r,j,75)==odd(r,j+384,75),'forcing parity period')
        need((r+j+75)%12==(r+j+384+75)%12,'forcing H phase')
    F=[front(x,(1,1,1),76,10,15,174) for x in (0,1)]
    result=[]
    for delta in range(11,25):
        j=185-delta;k=delta-9
        maps=[[driven(F[x],x,(1,1,1),76,10,j,k,L,b) for b in BITS] for x in (0,1)]
        need(all(len(set(t))==8 for t in maps),'each native payload map a permutation')
        perm=[maps[0].index(q) for q in maps[1]]
        c=cycles(perm)
        need(all(len(v) in (1,3) for v in c),'relative permutation has odd order dividing3')
        pairs=[(a,b) for a in range(8) for b in range(a+1,8) if maps[0][a]==maps[1][b] and maps[1][a]==maps[0][b] and maps[0][a]!=maps[1][a]]
        need(not pairs,'no common full-triple XOR code')
        result.append({'delta':delta,'uncontrolled_x_outputs':[F[x][j][10,k] for x in (0,1)],
                       'payload_maps':maps,'relative_cycles':c,'common_XOR_pairs':pairs})
    # Positive countercontrol: the same pair predicate accepts true XOR maps.
    a=list(BITS);b=[xor(v,(0,0,1)) for v in BITS]
    positive=[(i,j) for i in range(8) for j in range(i+1,8) if a[i]==b[j] and b[i]==a[j] and a[i]!=b[i]]
    need(len(positive)==4,'XOR-code search positive control')
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--geometry',type=Path,default=Path(__file__).resolve().parent.parent/'parallel_v3/history_control/SOURCE-GEOMETRY.json');args=ap.parse_args()
    g=geometry(args.geometry);c=native_controls();rows=census()
    print(json.dumps({'schema':'oi-alternate-front-v10-v1','geometry':g,'native_controls':c,'census':rows,
        'period_cells':176,'period_divisor':'384*840^176','controls_passed':True,
        'verdict':'PLUS_X_GEOMETRY_REJECTED; MINUS_X_FULL_LAW_XOR_ENCODING_EXCLUDED_IN14_ENDPOINT_FAMILY'},indent=2,sort_keys=True))
