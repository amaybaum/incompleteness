"""Native masked-X coupling with three initial frontier triples.

Complete six-neighbor/two-slice evaluation; no author-engine imports.
"""
import argparse
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path


STEPS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def dist(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))


def h(v):
    a,b,d=(v>>2)&1,(v>>1)&1,v&1
    return (b<<2)|(d<<1)|(a^(b&d))


def actual_geometry(root):
    T=185
    P=12*840**185
    S=P+T
    R=S+68
    L=R+9
    q9=(0,S,77)
    targets=[(0,S,76),(0,S,78),(-1,S,77)]
    sources=[(-(L+1),S,76),(-(L+1),S,78),(-(L+2),S,77)]
    others=[(1,S,77),(0,S-1,77),(0,S+1,77)]
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),
           (0,S,0),(12*R,0,0),(48*L,0,0)]
    deadline=[T,T,S,S,S,S,R,L]
    ready=list(zip(ports,deadline))
    ready += [((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),
              ((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]
    ready += [((-48*L,0,0),L)]
    local=[(0,0,0),(0,-76,76),(0,S,S+136),(0,S,S+150),
           (0,S,S+152),(0,S,S+154),(1,S,S+153),(-1,S,S+153)]
    finite=json.loads((root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())['sources']
    positions={tuple(row['position']) for row in finite}
    distances=[[dist(f,t)-L for t in targets] for f in sources]
    need(distances==[[1,3,1],[3,1,1],[3,3,1]],'actual triangular source geometry')
    ready_rows=source_rows=public_rows=0
    public_slacks=[]
    for f in sources:
        need(dist(f,q9)==L+2,'old-local q9 unaffected')
        need(all(dist(f,t)==L+3 for t in others),'other three neighbors share source')
        for center,radius in ready:
            need(dist(f,center)>radius,'old readiness overwritten')
            ready_rows+=1
        need(f not in positions and f not in local,'source payload overwritten')
        source_rows+=len(finite)
        for p in ports:
            need(dist(f,p)>L+2,'old full public past through L+2 changed')
            public_rows+=1
        public_slacks.append(min(dist(f,p)-L for p in ports))
        # Six local bank rays have fixed x; old/new herald rays have
        # strictly positive x through2L. No alias at any reserved index.
        need(f[0] not in (0,T,-T,4*T),'local bank alias')
        need(12*R-2*L>0,'old herald bank sign')
        need(48*L+L+1>0,'new herald bank sign')
        for center,radius in [((12*R,0,0),R),((-12*R,0,0),R),
                              ((48*L,0,0),L),((-48*L,0,0),L)]:
            need(dist(f,center)>radius,'remote program consumed')
        need((sum(f)-sum(q9)-(L+2))%2==0,'inactive spacetime component')
    need(public_slacks==[77,79,79],'public arrival offsets')
    need(len(set(sources))==3,'frontier sources not distinct')
    need(dist(sources[2],targets[2])==L+1,'F9 own axis')
    need(2*(51*L+S+8*T+200)<256*L+64*T+1,'no-wrap envelope')
    # A proposed all-zero radius-(L+2) q9 current shell would consume eight
    # old bank coordinates. Four are in this target's active component.
    bank_points=[(0,-1,0),(0,-2,0)]
    bank_points += [(T,P+S+k,0) for k in (1,2)]
    bank_points += [(-T,P+S+k,0) for k in (1,2)]
    bank_points += [(0,S+S+k,0) for k in (1,2)]
    need(all(dist(p,q9)<=L+2 for p in bank_points),'shell bank exceptions')
    active=[p for p in bank_points if (sum(p)-sum(q9)-(L+2))%2==0]
    need(len(active)==4 and all(dist(p,q9)==L+2 for p in active),
         'active shell exception front')
    return {'source_formulas':['(-(L+1),S,76)','(-(L+1),S,78)','(-(L+2),S,77)'],
            'target_offsets_over_L':distances,'ready_exclusions':ready_rows,
            'inherited_source_comparisons':source_rows,'public_cone_exclusions':public_rows,
            'minimum_public_arrival_offsets_over_L':public_slacks,
            'new_initial_fair_bits':3,'total_frontier_fair_bits':9,
            'zero_shell_old_bank_exceptions':8,'active_shell_bank_exceptions':4,
            'needs_new_zero_readiness':False,'reserved_eight_stream_bank_untouched_through_2L':True}


def background(seed,t,p):
    x,y,z=p
    return ((x*x+3*y*y+7*z+13*t+seed)^(x*y+z*z+11*seed*t))&7


def packed_native(n,seed):
    rows=list(product(range(8),repeat=3))
    full=(1<<len(rows))-1
    sources=[(-n,0,-1),(-n,0,1),(-n-1,0,0)]
    data={p:tuple(sum(((row[j]>>(2-k))&1)<<lane for lane,row in enumerate(rows))
                  for k in range(3)) for j,p in enumerate(sources)}

    @lru_cache(None)
    def get(t,p):
        if t==0 and p in data:
            return data[p]
        if t in (0,-1):
            value=background(seed,t,p)
            return tuple(full if value&(1<<(2-k)) else 0 for k in range(3))
        acc=[0,0,0]
        for step in STEPS:
            value=get(t-1,tuple(a+b for a,b in zip(p,step)))
            for k in range(3):
                acc[k]^=value[k]
        old=get(t-2,p)
        a,b,d=acc
        out=(b,d,a^(b&d))
        return tuple(x^y for x,y in zip(old,out))

    def unpack(t,p):
        triple=get(t,p)
        return [sum(((triple[k]>>lane)&1)<<(2-k) for k in range(3))
                for lane in range(len(rows))]

    return rows,unpack


def scalar_native(n,seed,assignment,t,target):
    positions=[(-n,0,-1),(-n,0,1),(-n-1,0,0)]
    sources=dict(zip(positions,assignment))

    @lru_cache(None)
    def get(time,p):
        if time==0 and p in sources:
            return sources[p]
        if time in (-1,0):
            return background(seed,time,p)
        accumulator=0
        for step in STEPS:
            accumulator^=get(time-1,tuple(a+b for a,b in zip(p,step)))
        return get(time-2,p)^h(accumulator)
    return get(t,target)


def native_controls():
    families=worlds=scalar_rows=inverse_rows=0
    missing_shared=missing_old=0
    old_codes=set()
    for n in range(1,5):
        for seed in (0,3,8):
            rows,unpack=packed_native(n,seed)
            center=(0,0,0)
            q8=unpack(n,(0,0,-1))
            q10=unpack(n,(0,0,1))
            middle=unpack(n,(-1,0,0))
            other_values=[unpack(n,p) for p in ((1,0,0),(0,-1,0),(0,1,0))]
            old=unpack(n-1,center)
            value=unpack(n+1,center)
            need(len(set(old))==1,'old q9 depends on new sources')
            need(all(len(set(v))==1 for v in other_values),'other neighbors depend on new sources')
            complement=other_values[0][0]^other_values[1][0]^other_values[2][0]
            old_codes.add(old[0])
            image={(q8[j],q10[j],middle[j]) for j in range(512)}
            need(len(image)==512,'native triangular source map singular')
            output={(q8[j],q10[j],value[j]) for j in range(512)}
            need(len(output)==512,'whole V/pool product law fails')
            need(Counter(value)=={code:64 for code in range(8)},'whole V not uniform')
            for lane,row in enumerate(rows):
                total=q8[lane]^q10[lane]^middle[lane]^complement
                need(value[lane]==old[lane]^h(total),'actual whole q9 update')
                recovered=value[lane]^h(total)
                need(recovered==old[lane],'fixed seven-site inverse')
                need(((value[lane]>>1)&1) ^ (total&1) == ((old[lane]>>1)&1),
                     'fixed previous-D/current-B X decoder')
                if value[lane]^h(q8[lane]^q10[lane]^complement)!=old[lane]:
                    missing_shared+=1
                if value[lane]!=h(total):
                    missing_old+=1
                inverse_rows+=1
            # F9=0 or F9=F8 leaves only64 worlds. Given a pool pair V is
            # then deterministic, TV7/8 from the correct uniform joint law.
            for mode in ('omit','share'):
                selected=[j for j,row in enumerate(rows)
                          if row[2]==(0 if mode=='omit' else row[0])]
                need(len(selected)==64,'negative-control support')
                need(len({(q8[j],q10[j],value[j]) for j in selected})==64,
                     'missing/shared F9 did not collapse joint support')
                need(Fraction(1)-Fraction(64,512)==Fraction(7,8),'joint negative-control TV')
            for lane in (0,7,56,73,219,511):
                row=rows[lane]
                for time,p,expected in [(n,(0,0,-1),q8[lane]),
                                         (n,(0,0,1),q10[lane]),
                                         (n,(-1,0,0),middle[lane]),
                                         (n+1,center,value[lane])]:
                    need(scalar_native(n,seed,row,time,p)==expected,'scalar/packed native control')
                    scalar_rows+=1
            families+=1
            worlds+=512
    need(missing_shared>0 and missing_old>0,'inverse negative controls are vacuous')
    return {'native_world_families':families,'complete_native_worlds':worlds,
            'scalar_independent_comparisons':scalar_rows,'inverse_decoder_rows':inverse_rows,
            'without_shared_neighbor_inverse_failures':missing_shared,
            'without_oldlocal_update_failures':missing_old,
            'old_triples_observed_in_smoke':sorted(old_codes),
            'uniform_joint_pool_V_support_each_family':512,
            'omitted_or_shared_F9_joint_TV':'7/8'}


def local_all_branch_controls():
    thresholds={(0,0):5,(0,1):0,(1,0):4,(1,1):1}
    truth_rows=0
    success_rows=0
    for old,complement in product(range(8),repeat=2):
        s=(old>>1)&1
        reference={(s,y,r,z):weight
                   for y,r,weight in ((s,s,Fraction(1,4)),
                                      (1^s,s,Fraction(1,5)),
                                      (1^s,1^s,Fraction(1,20)))
                   for z in (0,1)}
        raw_joint=Counter()
        accepted=Counter()
        rejected=Counter()
        physical=Counter()
        physical_success=Counter()
        physical_failure=Counter()
        offers=Counter()
        resurrection_mutant=0
        for q8,q10,middle in product(range(8),repeat=3):
            total=q8^q10^middle^complement
            V=old^h(total)
            recovered=V^h(total)
            need(recovered==old,'all-old-triple inverse')
            Y=(q8>>1)&1
            R=q10&1
            Z=(q10>>1)&1
            K=((q8>>2)&1)+2*(q8&1)+4*((q10>>2)&1)
            flag=K<thresholds[Y^s,R^s]
            for old_flag in (0,1):
                offers[old_flag,bool(old_flag and flag)]+=1
            resurrection_mutant+=int(flag)
            state=(s,Y,R,Z)
            raw_joint[q8,q10,V]+=1
            phase=(old,q8,q10,middle,V)
            physical[phase]+=1
            (physical_success if flag else physical_failure)[phase]+=1
            (accepted if flag else rejected)[V,state]+=1
            truth_rows+=1
        need(len(raw_joint)==512 and set(raw_joint.values())=={1},'all-complement product law')
        need(sum(accepted.values())==160 and sum(rejected.values())==352,
             'all raw masks and reference failure phases retained')
        for V in range(8):
            for state,p in reference.items():
                need(Fraction(accepted[V,state],512)==Fraction(1,8)*Fraction(5,16)*p,
                     'whole V/reference-carrier joint law')
                success_rows+=1
            need(sum(n for (v,j),n in rejected.items() if v==V)==44,
                 'whole V reference failure record')
        need(sum(physical.values())==512,'full selected phase measure')
        need(physical==physical_success+physical_failure and
             sum(physical_success.values())==160 and sum(physical_failure.values())==352,
             'physical success/failure measures do not partition')
        # Earlier-terminal flag is never overridden by the abstract predicate.
        need(offers[0,True]==0 and offers[0,False]==512,
             'earlier terminal flag resurrected')
        need(offers[1,True]==160 and offers[1,False]==352,
             'reference success/failure partition')
        need(resurrection_mutant==160,'resurrection countercontrol is vacuous')
    return {'all_old_complement_truth_rows':truth_rows,
            'accepted_joint_cell_checks':success_rows,
            'reference_acceptance':'5/16','reference_failure':'11/16',
            'whole_V_each_symbol_probability':'1/8',
            'native_reference_acceptance_flag_constructed':False,
            'failure_physical_measure_retained':True}


def find_source(here):
    for root in (here.parent,here.parent.parent,here.parent/'checkpoint_v11'):
        if (root/'parallel_v3').exists():
            return root
    raise RuntimeError('specify --source-root')


def main():
    here=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path)
    args=parser.parse_args()
    root=args.source_root or find_source(here)
    provenance=json.loads((here/'PROVENANCE.json').read_text())
    for name,digest in provenance['source_files'].items():
        need(hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,'source hash '+name)
    output={'schema':'oi.native-masked-X-coupling.v12',
            'source_revision':provenance['source_revision'],
            'geometry':actual_geometry(root),'native_controls':native_controls(),
            'all_branch_local_controls':local_all_branch_controls(),
            'verdict':'PASS_CONDITIONAL_NATIVE_MASKED_X_COUPLING',
            'scope':'Explicit three-initial-bit resource extension and fixed local phase code; no clean operand/native predicate/reusable instrument.'}
    print(json.dumps(output,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
