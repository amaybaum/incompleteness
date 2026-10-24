"""Separate scalar native and closed-form geometry checks; no author imports."""
import argparse
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def distance(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))


def clamp(v,lo,hi):
    return max(lo,min(hi,v))


def gap(a,b):
    return max(0,a[0]-b[1],b[0]-a[1])


def geometric_proof(source_root):
    T=185
    P=12*840**185
    S=P+T
    R=S+68
    L=R+9
    H=2*L
    torus=256*L+64*T+1
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),
           (0,S,0),(12*R,0,0),(48*L,0,0)]
    deadlines=[T,T,S,S,S,S,R,L]
    axes=[1,2,1,1,1,1,0,0]
    signs=[-1,-1,1,1,1,1,-1,1]
    ready=list(zip(ports,deadlines))
    ready += [((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),
              ((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]
    ready += [((-48*L,0,0),L)]
    selected=[((0,S,76),L-1),((0,S,77),L),
              ((48*L,0,0),L),((-48*L,0,0),L)]
    pins=[(0,0,0),(0,-76,76),(0,S,S+136),(0,S,S+150),
          (0,S,S+152),(0,S,S+154),(1,S,S+153),(-1,S,S+153)]

    def source(i,t):
        return tuple(v+(signs[i]*t if k==axes[i] else 0)
                     for k,v in enumerate(ports[i]))

    def closest_distance(i,target):
        # All three-coordinate absolute-value terms except one are constant.
        # The unique movable coordinate is closest at the clamped axial root.
        root=signs[i]*(target[axes[i]]-ports[i][axes[i]])
        t=clamp(root,deadlines[i]+1,H)
        return distance(source(i,t),target)

    edges=set()
    chronology=ready_count=selected_count=0
    for i in range(8):
        need(distance(source(i,H),ports[i])==H,'own unique-axis distance')
        for j,target in enumerate(ports):
            # |t-r|-t is monotone nonincreasing, so the exact minimum
            # of distance(source(i,t),target)-t occurs at H.
            slack=distance(source(i,H),target)-H
            need(slack>=0,'cross-port source arrives early')
            if i!=j and slack==0:
                edges.add((i,j))
            chronology+=1
        for target,radius in ready:
            need(closest_distance(i,target)>radius,'bank consumes current readiness')
            ready_count+=1
        for target,tick in selected:
            need(closest_distance(i,target)>tick,'selected phase depends on bank')
            selected_count+=1
        for pin in pins:
            need(closest_distance(i,pin)>0,'bank aliases named local source')
    need(edges=={(2,5),(3,5)},'exact same-time edge set')
    need(all(i<j for i,j in edges),'same-time topological order')

    # A ray is a product of three coordinate intervals, only one nontrivial.
    # Manhattan distance between complete ray segments is the sum of interval
    # gaps, giving an independent exact intersection test for all family pairs.
    segments=[]
    for i in range(8):
        lo,hi=source(i,deadlines[i]+1),source(i,H)
        segments.append([tuple(sorted((lo[k],hi[k]))) for k in range(3)])
    pair_count=0
    for i in range(8):
        for j in range(i+1,8):
            need(sum(gap(a,b) for a,b in zip(segments[i],segments[j]))>0,
                 'distinct source-family segments intersect')
            pair_count+=1

    old_sources=json.loads((source_root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())['sources']
    covered=0
    for row in old_sources:
        target=tuple(row['position'])
        need(any(distance(target,c)<=r for c,r in ready),'uncovered inherited source')
        covered+=1
    need(all(any(distance(pin,c)<=r for c,r in ready) for pin in pins),
         'uncovered local source')
    need(covered==1479,'source inventory size')
    # Whole remote programs are inside their explicitly included ready balls;
    # the first rows are not materialized at enormous L.
    extremes=[source(i,t) for i in range(8) for t in (deadlines[i]+1,H)]
    extremes+=pins
    for c,r in ready:
        extremes.extend(tuple(v+(s*r if k==axis else 0) for k,v in enumerate(c))
                        for axis in range(3) for s in (-1,1))
    spans=[max(q[k] for q in extremes)-min(q[k] for q in extremes) for k in range(3)]
    need(all(2*w<torus for w in spans),'torus shortcut')
    need(2*H<torus,'own axial path wraps')
    old_triples=7*L-sum(deadlines[:7])
    need(old_triples==2*P+6*68+63,'old bank count')
    need(3*old_triples==6*P+18*68+189,'old bank bits')
    need(8*H-sum(deadlines)-old_triples==8*L,'eight-stream extension coefficient')
    return {'chronological_minima':chronology,'ready_exclusions':ready_count,
            'selected_phase_exclusions':selected_count,'distinct_family_pairs':pair_count,
            'covered_inherited_sources':covered,'same_time_edges':sorted(map(list,edges)),
            'future_bits_per_tick':24,'window':'L < t <= L+Delta, 1<=Delta<=L',
            'monotone_cross_distance_proof':True,'clamped_ready_distance_proof':True}


def native_evaluator(sources,seed):
    neighbors=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

    @lru_cache(None)
    def get(t,p):
        if t==0 and p in sources:
            return sources[p]
        if t in (-1,0):
            x,y,z=p
            return ((x*x+3*y*y+7*z+13*t+seed)^(x*y+z*z+11*seed*t))&7
        s=0
        for delta in neighbors:
            s^=get(t-1,tuple(a+b for a,b in zip(p,delta)))
        a,b,d=(s>>2)&1,(s>>1)&1,s&1
        return get(t-2,p)^((b<<2)|(d<<1)|(a^(b&d)))
    return get


def scalar_controls():
    old_points=[(1,0,0),(0,1,0)]
    old_sources=[(1,3,0),(0,4,0)]
    g=(20,0,0)
    g_sources=[(23,0,0),(24,0,0)]
    # Cross-cluster sources cannot reach any opposite output, so the global
    # four-block source map is exactly the product of these two native maps.
    need(all(distance(s,g)>4 for s in old_sources),'old bank reaches remote test')
    need(all(distance(s,p)>3 for s in g_sources for p in old_points),
         'new bank reaches old test')
    need(all(distance(p,g)>7 for p in old_points),'small test cones intersect')
    scalar_worlds=own_maps=global_worlds=prefixes=0
    for seed in (3,8):
        old_table={}
        future_table={}
        for a,b in product(range(8),repeat=2):
            old=native_evaluator(dict(zip(old_sources,(a,b))),seed)
            old_table[a,b]=tuple(old(3,p) for p in old_points)
            future=native_evaluator(dict(zip(g_sources,(a,b))),seed)
            future_table[a,b]=(future(3,g),future(4,g))
            before=tuple(future(t,g) for t in range(3))
            if not prefixes:
                reference=before
            if a==b==0:
                reference=before
            need(before==reference,'future bank changes past prefix')
            prefixes+=1
            scalar_worlds+=2
        for table in (old_table,future_table):
            need(len(set(table.values()))==64,'native two-block map not bijective')
            for a in range(8):
                need(len({table[a,b][0] for b in range(8)})==1,'later bank source affects first output')
                need(len({table[a,b][1] for b in range(8)})==8,'second diagonal is singular')
                own_maps+=1
            need(len({table[a,0][0] for a in range(8)})==8,'first diagonal is singular')
            own_maps+=1
        global_worlds+=len(set(old_table.values()))*len(set(future_table.values()))
        # Shared and pinned late resources collapse the four-block support.
        need(len({future_table[a,a] for a in range(8)})==8,'shared resource support')
        need(len({future_table[a,0] for a in range(8)})==8,'pinned resource support')
        need(len({(a,future_table[a,0][0]) for a in range(8)})==8,'extra-source read support')
    return {'direct_scalar_native_worlds':scalar_worlds,
            'factorized_four_block_worlds_proved':global_worlds,
            'conditional_diagonal_checks':own_maps,'prefix_assignments':prefixes,
            'four_block_uniform_support':4096,'pinned_four_block_support':512,
            'shared_four_block_support':512,'extra_read_joint_support':8,
            'independent_extra_read_support':64}


def find_source(here):
    for root in (here.parent,here.parent.parent,here.parent/'checkpoint_v10'):
        if (root/'parallel_v3').exists():
            return root
    raise RuntimeError('specify --source-root')


def main():
    here=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path)
    parser.add_argument('--author-root',type=Path)
    args=parser.parse_args()
    source=args.source_root or find_source(here)
    author=args.author_root or (here.parent if (here.parent/'PROVENANCE.json').exists()
                               else here.parent/'history_v11')
    inputs=json.loads((here/'INPUT-HASHES.json').read_text())
    for root,entries in [(author,inputs['author_files']),(source,inputs['source_files'])]:
        for name,expected in entries.items():
            need(hashlib.sha256((root/name).read_bytes()).hexdigest()==expected,'hash '+name)
    result={'schema':'oi.history-v11.review.v1','author_revision':inputs['author_revision'],
            'verdict':'ACCEPT_CONDITIONAL_EIGHT_PORT_EXTENSION',
            'geometry':geometric_proof(source),'native_controls':scalar_controls(),
            'tail_conditioning':'uniform given complement, informative history and earlier noise',
            'future_full_physical_boundary_independence':False}
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
