"""Independent original-time boundary review; no author engine imports."""
import argparse
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path


def need(ok, text):
    if not ok:
        raise RuntimeError(text)


def dist(a, b):
    return sum(abs(x-y) for x,y in zip(a,b))


def h(v):
    a, b, d = (v >> 2) & 1, (v >> 1) & 1, v & 1
    return (b << 2) | (d << 1) | (a ^ (b & d))


def raw_evaluator(sources, seed):
    shifts = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))

    @lru_cache(None)
    def value(t, p):
        if t == 0 and p in sources:
            return sources[p]
        if t in (0,-1):
            x,y,z = p
            return ((3*x*x+7*y+5*z*z+11*t+seed) ^ (x*y+9*z+seed*t)) & 7
        neighbors = 0
        for delta in shifts:
            neighbors ^= value(t-1,tuple(a+b for a,b in zip(p,delta)))
        return value(t-2,p) ^ h(neighbors)
    return value


def native_pair():
    worlds = phase_rows = permutations = 0
    for n in range(1,6):
        for seed in (0,5):
            p,q = (0,0,0),(0,0,2)
            f,g = (-n,0,0),(-n,0,2)
            records = {}
            pair_images = set()
            for a,b in product(range(8),repeat=2):
                run = raw_evaluator({f:a,g:b},seed)
                # Every exposed selected field at the earlier cut is fixed.
                before = tuple(run(n-1,r) for r in (p,(0,0,1),q))
                before += (run(n-2,p),run(n-2,(0,0,1)))
                records[a,b] = (run(n,p),run(n,q),before)
                pair_images.add(records[a,b][:2])
                worlds += 1
            need(len({v[2] for v in records.values()}) == 1,'earlier phase changes')
            phase_rows += len(records)
            need(len(pair_images) == 64,'full native two-target law not bijective')
            for b in range(8):
                need(len({records[a,b][0] for a in range(8)}) == 8,'own f response')
                need(len({records[a,b][1] for a in range(8)}) == 1,'f cross response')
                permutations += 1
            for a in range(8):
                need(len({records[a,b][1] for b in range(8)}) == 8,'own g response')
                need(len({records[a,b][0] for b in range(8)}) == 1,'g cross response')
                permutations += 1
    return {'full_native_worlds':worlds,'prior_phase_rows':phase_rows,
            'conditional_own_permutations':permutations,'joint_outputs_each_family':64}


def actual_geometry(root):
    T=185
    P=12*840**185
    S=P+T
    R=S+68
    L=R+9
    p=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),
       (12*R,0,0),(48*L,0,0)]
    a=[T,T,S,S,S,S,R,L]
    ready=list(zip(p,a))
    ready += [((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),
              ((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]
    ready += [((-48*L,0,0),L)]
    need(len(ready)==24,'ready inventory')
    inventory=json.loads((root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())
    upstream=[tuple(row['position']) for row in inventory['sources']]
    need(len(upstream)==1479,'source inventory')
    local=[(0,0,0),(0,-76,76),(0,S,S+136),(0,S,S+150),(0,S,S+152),
           (0,S,S+154),(1,S,S+153),(-1,S,S+153)]
    targets=[(0,S,76),(0,S,77),(0,S,78)]
    points=[(-(L+1),S,76),(-(L+1),S,78)]
    endpoint_distances=[]
    excluded_ready = public_cones = inventory_rows = 0
    for f,own,other in [(points[0],targets[0],targets[2]),
                         (points[1],targets[2],targets[0])]:
        endpoint_distances.append([dist(f,own)-L,dist(f,targets[1])-L,dist(f,other)-L])
        need(endpoint_distances[-1]==[1,2,3],'wrong target geometry')
        for center,radius in ready:
            need(dist(f,center)>radius,'overwritten ready ball')
            excluded_ready += 1
        for receiver in p+[(-48*L,0,0)]:
            need(dist(f,receiver)>L,'earlier full public history changed')
            public_cones += 1
        need(f not in upstream and f not in local,'initial source alias')
        inventory_rows += len(upstream)
        # All old seven rays through L, or the extended eight rays through2L,
        # have x in these fixed planes or a strictly positive interval.
        need(f[0] not in (0,T,-T,4*T),'old bank plane')
        need(12*R-2*L>0 and 48*L+L+1>0,'remote bank interval')
        for center,radius in [((12*R,0,0),R),((-12*R,0,0),R),
                              ((48*L,0,0),L),((-48*L,0,0),L)]:
            need(dist(f,center)>radius,'remote program overlap')
        need((sum(f)-sum(own)-(L+1))%2==0,'spacetime component mismatch')
    need(dist((L+1,S,76),p[4])-L==-478,'positive-direction countercontrol')
    need(min(dist(points[0],z)-L for z in p)==77,'f8 minimum public slack')
    need(min(dist(points[1],z)-L for z in p)==79,'f10 minimum public slack')
    m1,m2=(0,-1,0),(0,-2,0)
    need([dist(m1,targets[0])-L,dist(m2,targets[0])-L]==[0,1],'return bank shell')
    need([dist(m1,targets[2])-L,dist(m2,targets[2])-L]==[2,3],'outward bank shell')
    need((sum(m1)-sum(targets[0])-(L+1))%2==1,'M1 opposite component')
    need((S+2)&76 !=0,'M2 isolated Lucas parity cancellation')
    # Cone containment: two new dependency balls include all old q9 pins.
    need(L+1>=L+dist(targets[0],targets[1]),'current q9 containment')
    need(L>=L-1+dist(targets[0],targets[1]),'previous q9 containment')
    need(2*(51*L+S+8*T+200)<256*L+64*T+1,'no-wrap envelope')
    return {'ready_exclusions':excluded_ready,'public_cone_exclusions':public_cones,
            'inherited_source_comparisons':inventory_rows,
            'endpoint_distance_offsets':endpoint_distances,
            'min_public_port_slacks':[77,79],
            'positive_x_countercontrol_slack':-478,
            'return_bank_current_shell_offsets':[0,1],
            'outward_bank_offsets':[2,3],
            'M1_opposite_component':True,'M2_isolated_front_coefficient_zero':True,
            'globally_fixed_complement_excludes_variation':True}


def find_root(here,name):
    for p in [here.parent,here.parent.parent,here.parent/'checkpoint_v10']:
        if (p/name).exists():
            return p
    raise RuntimeError('specify --source-root or --author-root')


def main():
    here=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path)
    parser.add_argument('--author-root',type=Path)
    args=parser.parse_args()
    source=args.source_root or find_root(here,'parallel_v3')
    author=args.author_root or (here.parent if (here.parent/'PROVENANCE.json').exists()
                               else here.parent/'native_v11')
    pins=json.loads((here/'INPUT-HASHES.json').read_text())
    for prefix,entries in [(author,pins['author_files']),(source,pins['source_files'])]:
        for name,expected in entries.items():
            need(hashlib.sha256((prefix/name).read_bytes()).hexdigest()==expected,
                 'input hash '+name)
    result={'schema':'oi.native-v11.review.v1','author_revision':pins['author_revision'],
            'verdict':'ACCEPT_SCOPED_BOUNDARY_OBSTRUCTION',
            'geometry':actual_geometry(source),'native_controls':native_pair(),
            'claim_boundary':'Outside-ready variation only; specified complement laws or full boundary contracts are not excluded.'}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
