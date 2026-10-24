"""Independent finite assembly of the native-pool abstract-X target."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def fields(word):
    bits=tuple((word >> i)&1 for i in range(6))
    return (bits[1],bits[5],bits[4],bits[0]+2*bits[2]+4*bits[3]),(bits[:3],bits[3:])


def reference(s):
    # Explicit six-cell probability measure, independent of the sampler's
    # threshold loop or moment calculations.
    patterns=((s,s,5),(1^s,s,4),(1^s,1^s,1))
    return {(s,y,r,z):Fraction(weight,20)
            for y,r,weight in patterns for z in range(2)}


def measure(s,variant='correct',reused_r=None):
    counts=Counter()
    threshold={(0,0):5,(0,1):0,(1,0):4,(1,1):1}
    if variant=='swap':
        threshold[1,0],threshold[1,1]=1,4
    if variant=='forbidden':
        threshold[0,1]=1
    for word in range(64):
        (y,r,z,k),raw=fields(word)
        if reused_r is not None:
            r=reused_r
        if variant=='shared_z':
            z=y^s
        chosen=s^(variant=='stale')
        if k<threshold[y^chosen,r^chosen]:
            counts[s,y,r,z]+=1
    rate=Fraction(sum(counts.values()),64)
    return {state:Fraction(n,sum(counts.values())) for state,n in counts.items()},rate


def tv(a,b):
    return sum((abs(a.get(k,0)-b.get(k,0)) for k in a.keys()|b.keys()),Fraction())/2


def sampler_checks():
    decoded={fields(w)[0] for w in range(64)}
    need(len(decoded)==64,'six-bit field extraction not bijective')
    target_cells=set()
    pool_phases=0
    mutant_tvs={}
    for s in (0,1):
        wanted=reference(s)
        actual,rate=measure(s)
        need(actual==wanted and rate==Fraction(5,16),'full target law')
        need(len(actual)==6,'conditional support size')
        target_cells.update(actual)
        need(all(actual[s,y,r,0]==actual[s,y,r,1] for _,y,r,_ in actual),'Z joint law')
        accepted=sum(1 for w in range(64)
                     if fields(w)[0][3] < {(0,0):5,(0,1):0,(1,0):4,(1,1):1}
                     [fields(w)[0][0]^s,fields(w)[0][1]^s])
        need(accepted==20,'accepted pool raw phases')
        pool_phases+=64
        for variant,expected in [('swap',Fraction(3,10)),('stale',Fraction(4,5)),
                                 ('shared_z',Fraction(1,2))]:
            bad,bad_rate=measure(s,variant)
            need(tv(bad,wanted)==expected,'negative-control TV '+variant)
            need(bad_rate==Fraction(5,16),'negative-control rate '+variant)
            if variant=='shared_z':
                need(sum(p for j,p in bad.items() if j[3]==0)==Fraction(1,2),
                     'shared Z marginal is no longer fair')
            mutant_tvs[variant]=str(expected)
        forbidden,rate01=measure(s,'forbidden')
        need(rate01==Fraction(11,32),'forbidden mask rate')
        need(any((j[1]^s,j[2]^s)==(0,1) for j in forbidden),'forbidden code absent')
        for old_r,expected in [(s,Fraction(1,10)),(s^1,Fraction(9,10))]:
            bad,bad_rate=measure(s,reused_r=old_r)
            need(tv(bad,wanted)==expected,'old R reuse TV')
            mutant_tvs['reused_r_equal_s' if old_r==s else 'reused_r_opposite_s']=str(expected)
    need(len(target_cells)==12,'union full calibrated codebook')
    return {'pool_raw_phases_both_signs':pool_phases,'codebook_cells':12,
            'accepted_raw_phases_each_sign':20,'rejected_raw_phases_each_sign':44,
            'negative_control_tvs':mutant_tvs,'forbidden_mask_rate':'11/32'}


def h(value):
    a,b,d=(value>>2)&1,(value>>1)&1,value&1
    return (b<<2)|(d<<1)|(a^(b&d))


def reconstruct_parent(root):
    words=json.loads((root/'parallel_v3/direct_reset/herald.json').read_text())['program']
    flags={}
    for a,b,k in product(range(2),range(2),range(8)):
        seed=a|(b<<1)|(k<<2)
        state=0
        for constant,terms in words[:2684]:
            force=constant
            for bit,mask in terms:
                if seed & (1<<bit):
                    force^=mask
            state=h(state^force)
        final=h(h(state))
        need(final in (0,2),'parent raw herald phase')
        flags[a,b,k]=final>>1
        need(flags[a,b,k]==int(k<[[5,0],[3,2]][a][b]),'parent native predicate')
    old=json.loads((root/'branch_v10/local-controller/symmetric-result.json').read_text())
    table=old['q9_table_hex']
    need(len(table)==32768,'parent source payload table length')
    rows={}
    for x,u,my,mr,a,b in product(range(2),repeat=6):
        # Independent six-binary-selector packing, then fixed witness4,5,7.
        row=(x<<5)|(u<<4)|(my<<3)|(mr<<2)|(a<<1)|b
        code=int(table[(row<<9)|(4<<6)|(5<<3)|7],16)
        raw=((code>>2)&1,(code>>1)&1,code&1)
        y=x^u
        expected=(u,y,x*(1^u)) if (a,b)==(0,1) else (0,y^a,y^b)
        need(raw==expected,'native old success/failure raw table')
        rows[x,u,my,mr,a,b]=raw
    return flags,rows


def branch_assembly(root):
    flags,rows=reconstruct_parent(root)
    worlds=joint_equalities=old_failed_raw01=0
    rejected_phase_cells=0
    for x,u,my,mr in product(range(2),repeat=4):
        record=Counter()
        success=Counter()
        rejected=Counter()
        terminal=Counter()
        all_physical=Counter()
        offered_physical=Counter()
        rejected_physical=Counter()
        resurrected=0
        for a,b,k,z in product(range(2),range(2),range(8),range(2)):
            old_g=flags[a,b,k]
            raw=rows[x,u,my,mr,a,b]
            s=raw[1]
            for word in range(64):
                (yn,rn,zn,selector),pool=fields(word)
                new_flag=selector < [[5,0],[4,1]][yn^s][rn^s]
                physical=(raw,(0,0,z),(0,old_g,0),pool)
                all_physical[physical]+=1
                offered=old_g and new_flag
                if offered:
                    success[raw,(s,yn,rn,zn)]+=1
                    offered_physical[physical]+=1
                else:
                    rejected_physical[physical]+=1
                if old_g:
                    record[raw]+=1
                    if not new_flag:
                        rejected[raw]+=1
                else:
                    terminal[raw]+=1
                    resurrected+=int(new_flag)
                    if (a,b)==(0,1):
                        old_failed_raw01+=1
                        need(raw==(u,x^u,x*(1^u)),'old G0 mask01 raw overwritten')
                worlds+=1
        need(sum(success.values())==400,'combined success count')
        need(sum(rejected.values())==880,'new failure count')
        need(sum(terminal.values())==2816,'parent failure count')
        need(Fraction(resurrected,4096)==Fraction(55,256),'resurrection countercontrol')
        need(all_physical==offered_physical+rejected_physical,'selected phase partition')
        need(sum(rejected_physical.values())==3696,'rejected phase mass')
        rejected_phase_cells+=len(rejected_physical)
        y=x^u
        expected={(0,y,y):Fraction(1,2),(0,1^y,y):Fraction(3,10),
                  (0,1^y,1^y):Fraction(1,5)}
        need({raw:Fraction(n,1280) for raw,n in record.items()}==expected,'old whole raw record')
        for raw,count in record.items():
            for state,p in reference(raw[1]).items():
                need(Fraction(success[raw,state],4096)==Fraction(count,4096)*Fraction(5,16)*p,
                     'joint old-record/outgoing-carrier factor')
                joint_equalities+=1
            need(Fraction(rejected[raw],4096)==Fraction(count,4096)*Fraction(11,16),
                 'joint old-record/failure factor')
    return {'parent_source_table_rows':64,'parent_native_word_truth_rows':32,
            'parent_seed_assignments_including_z':64,'finite_worlds':worlds,
            'old_history_rows':16,'joint_success_cell_equalities':joint_equalities,
            'old_mask01_failed_physical_worlds':old_failed_raw01,
            'rejected_selected_phase_cells_sum':rejected_phase_cells,
            'branch_counts_per_4096':[400,880,2816],
            'branch_probabilities':['25/256','55/256','11/16'],
            'resurrection_false_offer_probability':'55/256'}


def find_source(here):
    for root in (here.parent,here.parent.parent,here.parent/'checkpoint_v10'):
        if (root/'parallel_v3').exists():
            return root
    raise RuntimeError('specify --source-root')


def public_cut():
    T=185
    P=12*840**185
    S=P+T
    R=S+68
    L=R+9
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),
           (0,S,0),(12*R,0,0),(48*L,0,0)]
    distances=[]
    for z in (76,78):
        source=(-(L+1),S,z)
        slack=min(sum(abs(a-b) for a,b in zip(source,p)) for p in ports)-L
        distances.append(slack)
        need(slack>1,'witness source changes public past through L+1')
    need(distances==[77,79],'exact public arrival lower bounds')
    return distances


def main():
    here=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path)
    parser.add_argument('--author-root',type=Path)
    parser.add_argument('--native-author-root',type=Path)
    args=parser.parse_args()
    source=args.source_root or find_source(here)
    author=args.author_root or (here.parent if (here.parent/'PROVENANCE.json').exists()
                               else here.parent/'native_pool_v11')
    native=args.native_author_root or (source/'native_v11' if (source/'native_v11').exists()
                                      else here.parent/'native_v11')
    pins=json.loads((here/'INPUT-HASHES.json').read_text())
    for folder,entries in [(author,pins['author_files']),(native,pins['native_files']),
                            (source,pins['source_files'])]:
        for name,expected in entries.items():
            need(hashlib.sha256((folder/name).read_bytes()).hexdigest()==expected,'input hash '+name)
    retained=json.loads((native/'result.json').read_text())
    need(retained['conditional_law']['next_q8_q10_joint_cell_probability']=='1/64',
         'native resource contract changed')
    public_slacks=public_cut()
    result={'schema':'oi.native-pool-v11.review.v1','author_revision':pins['author_revision'],
            'verdict':'ACCEPT_NATIVE_RESOURCE_AND_ABSTRACT_FULL_LAW',
            'sampler':sampler_checks(),'assembly':branch_assembly(source),
            'native_pool_conditional_prior':'independent fair original-time witness triples',
            'minimum_public_arrival_slacks_over_L':public_slacks,
            'public_past_cut':'L+1; source arrival lower bounds L+77 and L+79',
            'native_predicate_or_reusable_instrument_constructed':False}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
