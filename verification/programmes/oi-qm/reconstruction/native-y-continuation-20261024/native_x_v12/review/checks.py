"""Independent forward-cone and exact joint-law review of native X coupling."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path


H = (0, 2, 4, 7, 1, 3, 5, 6)
STEPS = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))


def check(ok, message):
    if not ok:
        raise RuntimeError(message)


def distance(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))


def plus(a,b):
    return tuple(x+y for x,y in zip(a,b))


def rule_controls():
    for value in range(8):
        a,b,d = ((value >> k)&1 for k in (2,1,0))
        expected = (b<<2)+(d<<1)+(a^(b&d))
        check(H[value] == expected, 'native H truth table')
        out=H[value]
        aa,bb,dd=((out>>k)&1 for k in (2,1,0))
        inverse=((dd^(aa&bb))<<2)+(aa<<1)+bb
        check(inverse==value, 'native H inverse')
    check(len(set(H))==8, 'H not a permutation')
    return 8


def geometry(source_root):
    T=185
    P=12*840**185
    S=P+T
    R=S+68
    L=R+9
    side=256*L+64*T+1
    q9=(0,S,77)
    receivers=[(0,S,76),(0,S,78),(-1,S,77)]
    sources=[(-(L+1),S,76),(-(L+1),S,78),(-(L+2),S,77)]
    excluded=[(1,S,77),(0,S+1,77),(0,S-1,77)]
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),
           (4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
    starts=[T,T,S,S,S,S,R,L]
    directions=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),
                (0,1,0),(0,1,0),(-1,0,0),(1,0,0)]
    # Reconstruct the original prepared centers, including every retained
    # local outward step, plus both remote apparatus families.
    ready=list(zip(ports,starts))
    ready.extend([(p,T) for p in ((T,0,0),(-T,0,0),(4*T,0,0))])
    ready.extend([((0,S,-68),R),((-12*R,0,0),R)])
    ready.extend([((0,S,68+j),R+j) for j in range(10)])
    ready.append(((-48*L,0,0),L))
    inventory=json.loads((source_root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())['sources']
    local_pins=[(0,0,0),(0,-76,76),(0,S,S+136),(0,S,S+150),
                (0,S,S+152),(0,S,S+154),(1,S,S+153),(-1,S,S+153)]
    expected=((1,3,1),(3,1,1),(3,3,1))
    for f,row in zip(sources,expected):
        check(tuple(distance(f,p)-L for p in receivers)==row, 'triangular frontier distances')
        check(distance(f,q9)==L+2, 'old-local field source exclusion')
        check(all(distance(f,p)==L+3 for p in excluded), 'other three neighbors source exclusion')
        check(all(distance(f,p)>r for p,r in ready), 'readiness pin conflict')
        check(all(f!=tuple(item['position']) for item in inventory), 'finite source alias')
        check(f not in local_pins, 'local source alias')
    cuts=[min(distance(f,p)-L for p in ports) for f in sources]
    check(cuts==[77,79,79], 'old public cut distances')
    check(all(distance(f,p)>L+2 for f in sources for p in ports), 'old public history changed')
    # Independently minimize point-to-ray distance by clamping each axial
    # source parameter, covering every index up to the maximal 2L horizon.
    ray_checks=0
    for f in sources:
        for p,a,e in zip(ports,starts,directions):
            axis=next(k for k in range(3) if e[k])
            root=(f[axis]-p[axis])*e[axis]
            t=max(a+1,min(2*L,root))
            bank=tuple(p[k]+e[k]*t for k in range(3))
            check(distance(f,bank)>0, 'reserved bank source collision')
            ray_checks+=1
    check(len(set(sources))==3, 'duplicated new sources')
    # One common lift covers all source, target, ready and bank extrema.
    extrema=sources+receivers+excluded+ports+local_pins
    for p,r in ready:
        extrema.extend(tuple(p[k]+(sign*r if k==axis else 0) for k in range(3))
                       for axis in range(3) for sign in (-1,1))
    for p,a,e in zip(ports,starts,directions):
        extrema.extend(tuple(p[k]+e[k]*t for k in range(3)) for t in (a+1,2*L))
    spans=[max(p[k] for p in extrema)-min(p[k] for p in extrema) for k in range(3)]
    check(all(2*x<side for x in spans) and 2*(L+2)<side, 'torus lift changes distances')
    # Initial q9-radius extension consumes the first two noise cells on
    # each of the four nearest old bank rays. Preserve all as exceptions.
    close=[]
    for i in (0,2,3,5):
        p,a,e=ports[i],starts[i],directions[i]
        for t in (a+1,a+2):
            v=tuple(p[k]+e[k]*t for k in range(3))
            check(distance(v,q9)<=L+2, 'old bank exception missing')
            close.append(v)
    active=[p for p in close if (sum(p)+sum(q9)+L+2)%2==0]
    check(len(close)==8 and len(set(close))==8 and len(active)==4, 'bank exception parity')
    check(all(distance(p,q9)==L+2 for p in active), 'active exception front')
    return {'ready_pairs':3*len(ready),'finite_source_pairs':3*len(inventory),
            'public_cut_pairs':24,'full_bank_ray_pairs':ray_checks,
            'public_minimum_offsets':cuts,'zero_shell_exceptions':8,
            'active_shell_exceptions':4,'torus_lift_checked':True}


def ball(radius):
    return [(x,y,z) for x in range(-radius,radius+1)
            for y in range(-(radius-abs(x)),radius-abs(x)+1)
            for z in range(-(radius-abs(x)-abs(y)),radius-abs(x)-abs(y)+1)]


def forward(n,seed):
    """Forward update on shrinking finite causal diamonds, 512 SIMD lanes."""
    assignments=list(product(range(8),repeat=3))
    all_bits=(1<<512)-1
    source_positions=[(-n,0,-1),(-n,0,1),(-n-1,0,0)]
    packed_sources={p:tuple(sum(((a[j]>>k)&1)<<i for i,a in enumerate(assignments))
                            for k in range(3)) for j,p in enumerate(source_positions)}

    def background(t,p):
        value=hashlib.sha256(repr((seed,t,p)).encode()).digest()[0]&7
        return tuple(all_bits if (value>>k)&1 else 0 for k in range(3))

    radius=n+1
    previous={p:background(-1,p) for p in ball(radius-1)}
    current={p:packed_sources.get(p,background(0,p)) for p in ball(radius)}
    snapshots={-1:previous,0:current}
    for t in range(1,radius+1):
        nxt={}
        for p in ball(radius-t):
            d=b=a=0
            for delta in STEPS:
                v=current[plus(p,delta)]
                d^=v[0];b^=v[1];a^=v[2]
            old=previous[p]
            nxt[p]=(old[0]^a^(b&d),old[1]^d,old[2]^b)
        previous,current=current,nxt
        snapshots[t]=current

    def unpack(t,p):
        v=snapshots[t][p]
        return [sum(((v[k]>>i)&1)<<k for k in range(3)) for i in range(512)]
    return assignments,unpack


def native_controls():
    cases=rows=diagonals=old_mutants=key_mutants=0
    old_seen=set()
    for n in (1,2,3,4):
        for seed in (19,43):
            assignments,read=forward(n,seed)
            q8=read(n,(0,0,-1));q10=read(n,(0,0,1));m=read(n,(-1,0,0))
            vs=read(n+1,(0,0,0));ps=read(n-1,(0,0,0))
            others=[read(n,p) for p in ((1,0,0),(0,1,0),(0,-1,0))]
            check(len(set(ps))==1 and all(len(set(v))==1 for v in others), 'non-new complement varies')
            old_seen.add(ps[0])
            for index,output in ((0,q8),(1,q10)):
                by_input={x:{output[i] for i,row in enumerate(assignments) if row[index]==x}
                          for x in range(8)}
                check(all(len(v)==1 for v in by_input.values()), 'pool depends on another new source')
                check(len({next(iter(v)) for v in by_input.values()})==8, 'pool own map not invertible')
                diagonals+=1
            for aa,bb in product(range(8),repeat=2):
                selected=[m[i] for i,row in enumerate(assignments) if row[:2]==(aa,bb)]
                check(len(set(selected))==8, 'third diagonal response singular')
                diagonals+=1
            check(len(set(zip(q8,q10,m)))==512, 'triangular native output loses support')
            check(Counter(zip(q8,q10,vs))==Counter(product(range(8),repeat=3)), 'ciphertext/pool joint law')
            b3=others[0][0]^others[1][0]^others[2][0]
            for i in range(512):
                total=q8[i]^q10[i]^m[i]^b3
                check(vs[i]==ps[i]^H[total], 'whole six-neighbor update')
                check(vs[i]^H[total]==ps[i], 'seven-site fixed inverse')
                check(((vs[i]>>1)&1)^(total&1)==((ps[i]>>1)&1), 'fixed X parity decoder')
                old_mutants+=int(vs[i]!=H[total])
                key_mutants+=int(vs[i]^H[q8[i]^q10[i]^b3]!=ps[i])
            for mode in (0,1):
                selected=[i for i,row in enumerate(assignments) if row[2]==(row[0] if mode else 0)]
                check(len(set((q8[i],q10[i],vs[i]) for i in selected))==64, 'pinned/shared source countercontrol')
            cases+=1;rows+=512
    check(old_mutants>0 and key_mutants>0, 'native negative controls are vacuous')
    return {'forward_native_families':cases,'forward_native_worlds':rows,
            'conditional_diagonal_checks':diagonals,'inverse_checks':rows,
            'old_local_mutant_failures':old_mutants,'missing_key_mutant_failures':key_mutants,
            'old_raw_triples_observed':sorted(old_seen),'pinned_or_shared_joint_tv':'7/8'}


def full_branch_controls():
    threshold=((5,0),(4,1))
    rows=cell_checks=negative_key_sectors=0
    determinants=set()
    for old,b3 in product(range(8),repeat=2):
        s=(old>>1)&1
        accepted=Counter();rejected=Counter();key_public=Counter();physical=Counter()
        for q,r,m in product(range(8),repeat=3):
            v=old^H[q^r^m^b3]
            check(v^H[q^r^m^b3]==old, 'local all-raw inverse')
            y,z,rr=(q>>1)&1,(r>>1)&1,r&1
            k=(q>>2)+2*(q&1)+4*(r>>2)
            flag=k<threshold[y^s][rr^s]
            state=(s,y,rr,z)
            (accepted if flag else rejected)[v,state]+=1
            if flag:key_public[v,m,state]+=1
            physical[old,q,r,m,v,flag]+=1
            rows+=1
        check(sum(physical.values())==512 and len(physical)==512, 'physical phase measure erased')
        check(sum(accepted.values())==160 and sum(rejected.values())==352, 'all abstract branches retained')
        for v in range(8):
            for aa,bb,z in product(range(2),repeat=3):
                state=(s,s^aa,s^bb,z)
                check(accepted[v,state]==threshold[aa][bb], 'full accepted mask/Z law')
                cell_checks+=1
            check(sum(c for (vv,st),c in rejected.items() if vv==v)==44, 'whole rejected raw word law')
        # Earlier terminal branches offer nothing, for all actual raw p.
        for old_flag in (0,1):
            offers=sum(count for (_,_,_,_,_,flag),count in physical.items() if old_flag and flag)
            check(offers==(160 if old_flag else 0), 'earlier terminal flag resurrected')
        # Adding a private M read changes the protocol class. On some accepted
        # sectors it biases Y/Z, yielding a nonpositive fixed Bloch decoder.
        # Only A=0 old triples are candidate offered-carrier inputs. The other
        # raw old triples remain physical failure controls without qubit output.
        if old&4:
            continue
        for v,m in product(range(8),repeat=2):
            terms=[(state,c) for (vv,mm,state),c in key_public.items() if vv==v and mm==m]
            total=sum(c for st,c in terms)
            if not total:continue
            ry=Fraction(sum((1-2*st[1])*c for st,c in terms),total)
            rz=Fraction(sum((1-2*st[3])*c for st,c in terms),total)
            determinant=-(ry*ry+rz*rz)/4
            determinants.add(str(determinant))
            negative_key_sectors+=int(determinant<0)
    check(negative_key_sectors>0, 'private-key access control vacuous')
    return {'all_raw_old_background_worlds':rows,'full_joint_carrier_cells':cell_checks,
            'acceptance':'5/16','reference_failure':'11/16','whole_cipher_symbol':'1/8',
            'private_key_exposure_negative_sectors':negative_key_sectors,
            'private_key_exposure_determinants':sorted(determinants),
            'native_acceptance_flag_claimed':False}


def locate(here,args):
    if args.author_root:
        author=args.author_root
    elif (here.parent/'PROVENANCE.json').exists():
        author=here.parent
    else:
        author=here.parent/'native_x_v12'
    if args.source_root:
        source=args.source_root
    elif (author.parent/'parallel_v3').exists():
        source=author.parent
    else:
        source=here.parent/'checkpoint_v11'
    return author,source


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--author-root',type=Path)
    parser.add_argument('--source-root',type=Path)
    args=parser.parse_args()
    here=Path(__file__).resolve().parent
    author,source=locate(here,args)
    pins=json.loads((here/'INPUT-HASHES.json').read_text())
    for name,entry in pins['author_files'].items():
        content=(author/name).read_bytes()
        check(hashlib.sha256(content).hexdigest()==entry['sha256'], 'author hash '+name)
        check(hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()==entry['git_blob'], 'author Git identity '+name)
    for name,digest in pins['scientific_inputs'].items():
        check(hashlib.sha256((source/name).read_bytes()).hexdigest()==digest, 'scientific input hash '+name)
    result={'schema':'oi.native-x-v12.independent-review.v1',
            'reviewed_author_revision':pins['reviewed_author_revision'],
            'rule_cases':rule_controls(),'geometry':geometry(source),
            'native':native_controls(),'joint_branches':full_branch_controls(),
            'verdict':'ACCEPT_SCOPED_NATIVE_MASKED_X_COUPLING',
            'scope':'Native conditional resource/ciphertext and fixed inverse code; no native predicate, physical unmasking, continuous port access or reusable instrument.'}
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
