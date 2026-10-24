"""Exact geometry and independent native frontier controls; standard library."""
from functools import lru_cache
from itertools import product
from pathlib import Path
import hashlib,json


def require(ok,label):
    if not ok: raise RuntimeError(label)


def distance(a,b): return sum(abs(x-y) for x,y in zip(a,b))


def h(v):
    a,b,c=v
    return b,c,a^(b&c)


def xor(*args):
    out=[0,0,0]
    for v in args:
        for j in range(3): out[j]^=v[j]
    return tuple(out)


def geometry():
    T=185;P=12*840**185;S=T+P;d=68;R=S+d;L=R+8
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0)]
    deadlines=[T,T,S,S,S,S,R]
    q8=(0,S,76);W=(0,-76,76)
    pins=[W,(0,S,S+136),(0,S,S+150),(0,S,S+152)]
    def block(i,t):
        if i==0:return (0,T-t,0)
        if i==1:return (0,0,-8*T-t)
        if i==6:return (12*R-t,0,0)
        q=ports[i];return(q[0],q[1]+t,0)
    # Piecewise-affine distances are checked at every absolute-value breakpoint.
    # Cross-distance to port j uses only the varying coordinate of this ray.
    directions=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0)]
    same_edges=set();count=0;endpoint_min=[];deadline_w=[]
    for i,(p,e,start) in enumerate(zip(ports,directions,deadlines)):
        a=next(j for j in range(3) if e[j])
        points={start+1,L}
        for q in ports+[q8]+pins:
            root=(q[a]-p[a])*e[a]
            points.update(t for t in (root-1,root,root+1) if start+1<=t<=L)
        mins=[]
        for t in sorted(points):
            f=block(i,t)
            require(distance(f,p)==t,'own axial distance')
            require(all(f!=pin for pin in pins),'source overwrite')
            for j,q in enumerate(ports):
                dd=distance(f,q)
                require(dd>=t,'no earlier arrival at any port')
                if i!=j and dd==t:
                    require(i<j,'same-tick edge respects order');same_edges.add((i,j))
            gap=distance(f,q8)-L
            require(gap>0,'frontier outside q8 current and previous ready balls')
            mins.append(gap);count+=1
        endpoint_min.append(str(min(mins)))
        deadline_w.append(str(distance(W,p)-start))
        require(distance(W,p)>start,'W preserves informative deadlines')
    require(same_edges=={(2,5),(3,5)},'actual same-tick edge set')
    # Pairwise ray-coordinate identity: solve all coordinates exactly for t,s.
    # Same-axis parallel rays can coincide only when their perpendicular origins agree.
    for i in range(7):
        for j in range(i+1,7):
            ei,ej=directions[i],directions[j];pi,pj=ports[i],ports[j]
            ai=next(k for k in range(3) if ei[k]);aj=next(k for k in range(3) if ej[k])
            if ai==aj:
                if any(pi[k]!=pj[k] for k in range(3) if k!=ai):continue
                a=sorted((pi[ai]+ei[ai]*(deadlines[i]+1),pi[ai]+ei[ai]*L))
                b=sorted((pj[ai]+ej[ai]*(deadlines[j]+1),pj[ai]+ej[ai]*L))
                require(a[1]<b[0] or b[1]<a[0],'collinear bank intervals distinct')
            else:
                if any(pi[k]!=pj[k] for k in range(3) if k not in (ai,aj)):continue
                ti=(pj[ai]-pi[ai])*ei[ai];tj=(pi[aj]-pj[aj])*ej[aj]
                require(not(deadlines[i]<ti<=L and deadlines[j]<tj<=L),'crossing banks distinct')
    # Original ready cones, including all earlier outward balls, are separated.
    ready=[(p,t) for p,t in zip(ports,deadlines)]
    ready += [((T,0,0),T),((-T,0,0),T),((4*T,0,0),T)]
    ready += [((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(9)]
    exclusions=0
    for i,start in enumerate(deadlines):
        # For every cone the distance is piecewise affine: its minimum over the
        # interval lies at an endpoint or at the changing-coordinate breakpoint.
        axis=next(k for k in range(3) if directions[i][k]);sign=directions[i][axis]
        for center,radius in ready:
            times={start+1,L}
            root=(center[axis]-ports[i][axis])*sign
            if start+1<=root<=L:times.add(root)
            require(min(distance(block(i,t),center) for t in times)>radius,'all ready cones excluded')
            exclusions+=1
    require(distance((0,-1,0),(0,S,75))==L,'neighbor exclusion does not hold automatically')
    # A zero isolated first-front coefficient is not an actual coupled-background witness.
    require(((S+1)&75)!=0,'isolated M1/q7 multinomial cancellation')
    return {'piecewise_affine_breakpoint_cases':count,'ready_cone_family_pairs':exclusions,
            'same_tick_edges':[list(x) for x in sorted(same_edges)],
            'q8_minimum_slacks_by_port':endpoint_min,'W_deadline_slacks_by_port':deadline_w,
            'extra_post_R_bits':7*8*3,'complete_noise_bits_formula':'6*P + 18*d + 168',
            'new_ready_current_radius':'R+8','new_ready_previous_radius':'R+7',
            'neighbor_bank_exclusion':'fails at distance test; no actual dependence asserted'}


STEPS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
TRIPLES=tuple(product((0,1),repeat=3))


def native_records(ports,time,frontiers,assignments,background):
    """Direct nonlinear wave recursion, bit-packed independent assignments."""
    full=(1<<len(assignments))-1
    packed={pos:tuple(sum(row[j][k]<<lane for lane,row in enumerate(assignments)) for k in range(3))
            for j,pos in enumerate(frontiers)}
    @lru_cache(None)
    def field(t,p):
        if t in (-1,0):
            if t==0 and p in packed:return packed[p]
            bits=hashlib.sha256(repr((background,t,p)).encode()).digest()[0]
            return tuple(full if (bits>>k)&1 else 0 for k in range(3))
        incoming=xor(*(field(t-1,tuple(a+b for a,b in zip(p,step))) for step in STEPS))
        return xor(field(t-2,p),h(incoming))
    out=[field(time,p) for p in ports]
    return [tuple(tuple((v[k]>>lane)&1 for k in range(3)) for v in out) for lane in range(len(assignments))]


def native_controls():
    # Actual algebra and dimension, but deliberately short distance controls.
    # They validate the mechanism; they do not substitute for actual geometry.
    ports=[(0,1,0),(0,0,-8),(1,2,0),(-1,2,0),(4,2,0),(0,3,0),(48,0,0)]
    cases=0
    for t in (5,6):
        fronts=[(0,1-t,0),(0,0,-8-t)]+[(p[0],p[1]+t,0) for p in ports[2:6]]+[(48-t,0,0)]
        for p,f in zip(ports,fronts):
            for background in (13,29):
                out=native_records([p],t,[f],[(v,) for v in TRIPLES],background)
                require(len(set(out))==8,'direct whole-triple axial permutation');cases+=1
    # Same-tick native triangular block, including a real forward cross-arrival.
    p=[ports[2],ports[5]];t=5;f=[(1,7,0),(0,8,0)]
    assignments=list(product(TRIPLES,repeat=2));pairs=0
    for background in (13,29):
        out=native_records(p,t,f,assignments,background)
        require(len(set(out))==64,'whole two-port block bijective')
        for i in range(8):require(len({out[8*i+j][0] for j in range(8)})==1,'no reverse dependency')
        require(all(len({out[8*i+j][1] for j in range(8)})==8 for i in range(8)),'second diagonal permutation')
        pairs+=64
        pinned=native_records(p,t,f,[(a,TRIPLES[0]) for a in TRIPLES],background)
        shared=native_records(p,t,f,[(a,a) for a in TRIPLES],background)
        require(len(set(pinned))<64,'readiness-overlap negative control detected')
        require(len(set(shared))<64,'shared-bank negative control detected')
    # Conditioning on a complement variable cannot change the uniform record
    # for any of these tested backgrounds; each produces every 6-bit word once.
    return {'single_frontier_permutation_cases':cases,'native_pair_assignments':pairs,
            'shared_source_negative_cases':2,'pinned_source_negative_cases':2,
            'conditional_uniformity_backgrounds':2}


def main():
    g=geometry();c=native_controls()
    result={'schema':'oi.native-y.history-v9.v1','geometry':g,'native_controls':c,
      'verdict':'PASS_CONDITIONAL_HISTORY_ENDPOINT',
      'scope':'Seven old raw records; supplied independent bank; q8 endpoint and bank-complement seeds. No reusable full-boundary claim.'}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))


if __name__=='__main__':main()
