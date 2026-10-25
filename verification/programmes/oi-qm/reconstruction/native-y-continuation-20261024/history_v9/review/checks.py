#!/usr/bin/env python3
"""Independent native-history controls; no author-module imports."""
from functools import lru_cache
from itertools import product
import json

def need(ok,why):
    if not ok:raise RuntimeError(why)

def manhattan(a,b):return sum(abs(x-y) for x,y in zip(a,b))

def geometry(K=8):
    T=185;P=12*840**T;S=P+T;d=68;R=S+d;L=R+K;side=64*R+64*T+1
    ps=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0)]
    starts=[T,T,S,S,S,S,R]
    dirs=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0)]
    def f(i,t):return tuple(a+t*b for a,b in zip(ps[i],dirs[i]))
    q8=(0,S,68+K); pins=[(0,-76,76),(0,S,S+136),(0,S,S+150),(0,S,S+152)]
    if K==9:pins.append((0,S,S+154))
    need(K in (8,9),'bounded audited horizons')
    cones=list(zip(ps,starts))+[((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]+[((0,S,68+k),R+k) for k in range(K+1)]
    # Each one-dimensional ray is a full integer segment. Bounding boxes are
    # sufficient and exact for intersections of these axis-aligned segments.
    boxes=[]
    for i in range(7):
        ends=[f(i,starts[i]+1),f(i,L)]
        boxes.append([(min(p[k] for p in ends),max(p[k] for p in ends)) for k in range(3)])
    for i in range(7):
        for j in range(i):need(any(a[1]<b[0] or b[1]<a[0] for a,b in zip(boxes[i],boxes[j])),'disjoint complete ray segments')
    for box in boxes:
        for pin in pins:need(not all(lo<=v<=hi for v,(lo,hi) in zip(pin,box)),'named pin is not a bank coordinate')
    if K==9:need(manhattan(pins[-1],(0,S,76))>R+8,'new J cannot change earlier q8')
    equal=set();cross=0;excluded=0
    # Construct all integer affine segments, then certify each endpoint pair.
    def segments(i,target):
        lo=starts[i]+1;hi=L
        cut={lo,hi}
        for k,e in enumerate(dirs[i]):
            if e:
                t=(target[k]-ps[i][k])*e
                if lo<=t<=hi:cut.add(t)
        ordered=sorted(cut)
        return list(zip(ordered,ordered[1:])) or [(lo,lo)]
    for i in range(7):
        for j,target in enumerate(ps):
            for lo,hi in segments(i,target):
                vals=[manhattan(f(i,t),target)-t for t in (lo,hi)]
                need(min(vals)>=0,'future bank cannot reach earlier record')
                if i!=j and 0 in vals:equal.add((i,j))
                cross+=1
        for target,radius in cones:
            for lo,hi in segments(i,target):
                need(min(manhattan(f(i,t),target)-radius for t in (lo,hi))>0,'initial bank outside complete ready cone')
            excluded+=1
        for pin in pins:
            need(manhattan(pin,ps[i])>starts[i],'all named added pins preserve informative deadlines')
        for lo,hi in segments(i,q8):
            for t in (lo,hi):
                expected=[t-T,t+8*T,t-S,t-S,t+2*T-P,t-S,12*R-t][i]
                need(manhattan(f(i,t),q8)-L==expected and expected>0,'stated endpoint slack formula')
    need(equal=={(2,5),(3,5)},'same-tick edges')
    # Every relevant center, source and bank point lies in [-14R,14R]^3;
    # so every coordinate difference is below half the torus circumference.
    need(L<=2*R and 56*R<side,'no-wrap bound')
    for center,radius in cones:
        need(max(abs(c)+radius for c in center)<=14*R,'full cone within common lift')
    for i in range(7):
        for t in (starts[i]+1,L):need(max(map(abs,f(i,t)))<=14*R,'bank within common lift')
    for pin in pins:need(max(map(abs,pin))<=14*R,'pin within common lift')
    n=sum(L-a for a in starts)
    need(n==2*P+6*d+7*K and 3*n==6*P+18*d+21*K,'entire bank count')
    return {'affine_cross_segments':cross,'ready_cone_family_pairs':excluded,
            'same_tick_edges':sorted(equal),'torus_lift_bound':'28R < side/2',
            'bank_triples':f'2P+6d+{7*K}','bank_bits':f'6P+18d+{21*K}','post_R_horizon':K}


def native():
    triples=list(product((0,1),repeat=3))
    assignments=list(product(triples,repeat=3));n=len(assignments);allbits=(1<<n)-1
    # Time-three B -> A is a genuine same-tick edge. The third record is
    # B at time four, so this block also checks chronological conditioning.
    sites=[(1,2,0),(0,3,0),(1,3,0)]
    observations=[(3,(1,-1,0)),(3,(0,0,0)),(4,(1,-1,0))]
    data={p:tuple(sum(row[i][k]<<z for z,row in enumerate(assignments)) for k in range(3)) for i,p in enumerate(sites)}
    steps=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    def xor(vs):
        out=[0,0,0]
        for v in vs:
            for k in range(3):out[k]^=v[k]
        return tuple(out)
    checked=0
    for bg in (2,7,11):
        @lru_cache(None)
        def field(t,p):
            if t==0 and p in data:return data[p]
            if t<=0:
                x,y,z=p
                v=(x*x+3*y*y+5*z*z+x*y+bg*(x+2*y+3*z)+7*t+bg)%8
                return tuple(allbits if v>>k&1 else 0 for k in range(3))
            a,b,c=xor(field(t-1,tuple(p[k]+e[k] for k in range(3))) for e in steps)
            return xor([field(t-2,p),(b,c,a^(b&c))])
        raw=[field(t,p) for t,p in observations]
        outputs=[tuple(tuple((v[k]>>i)&1 for k in range(3)) for v in raw) for i in range(n)]
        need(len(set(outputs))==512,'complete three-record native bijection')
        for prefixlen in (1,2,3):
            groups={}
            for assignment,output in zip(assignments,outputs):
                groups.setdefault(assignment[:prefixlen],set()).add(output[:prefixlen])
            need(all(len(out)==1 for out in groups.values()),'future inputs cannot affect past outputs')
            need(len({next(iter(out)) for out in groups.values()})==8**prefixlen,'prefix map bijective')
        shared=[out for row,out in zip(assignments,outputs) if row[0]==row[1]]
        pinned=[out for row,out in zip(assignments,outputs) if row[1]==(0,0,0)]
        need(len(set(shared))==64 and len(set(pinned))==64,'shared or pinned resource fails uniform 512-word law')
        checked+=512
    return {'native_assignments':checked,'backgrounds':3,'chronological_blocks':3,
            'distinct_full_words_per_background':512,'shared_or_pinned_words':64}

if __name__=='__main__':
    print(json.dumps({'schema':'history-v9-independent-review-v1','geometry':geometry(),
                      'additional_q9_geometry':geometry(9),'native_controls':native(),'controls_passed':True,'verdict':'PASS_CONDITIONAL_HISTORY_PROOF'},sort_keys=True,indent=2))
