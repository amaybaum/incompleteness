#!/usr/bin/env python3
"""Separate engine for immutable composition author1cb224db; no author imports."""
from argparse import ArgumentParser
from collections import Counter,defaultdict
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

COUNTS=Counter()

def check(name,ok):
    COUNTS[name]+=1
    if not ok: raise RuntimeError(name)

# Different wire order from author: six old neighbors, then current V.
TRIPLES=('L','R','M','C0','C1','C2','V')
NAMES=[p+'.'+c for p in TRIPLES for c in 'ABD']
NAMES+=['sx','aa','bb','acc','j0','j1','j2','pa','pb','pd']
INDEX={n:i for i,n in enumerate(NAMES)}
WS=('sx','aa','bb','acc','j0','j1','j2')
SWIRES=('V.B','L.D','R.D','M.D','C0.D','C1.D','C2.D')
UNUSED=set(range(21))-set(INDEX[n] for n in SWIRES+('L.B','L.A','R.A'))

def instruction(controls,target): return (tuple(INDEX[x] for x in controls),INDEX[target])

def conjunction(controls,negatives,target='acc'):
    # Build a five-input AND into a target with a clean three-bit ladder.
    flips=[instruction((),x) for x in negatives]
    if len(controls)==2:
        middle=[instruction(controls,target)]
    else:
        a,b,c,d,e=controls
        ladder=[instruction((a,b),'j0'),instruction(('j0',c),'j1'),instruction(('j1',d),'j2')]
        middle=ladder+[instruction(('j2',e),target)]+ladder[::-1]
    return flips+middle+flips[::-1]


def program():
    compute=[instruction((n,),'sx') for n in SWIRES]
    compute+=[instruction(('L.B',),'aa'),instruction(('sx',),'aa'),instruction(('R.D',),'bb'),instruction(('sx',),'bb')]
    compute+=conjunction(('bb','R.A'),('bb','R.A'))
    compute+=conjunction(('aa','bb','R.A','L.D','L.A'),('aa','bb','L.D','L.A'))
    compute+=conjunction(('aa','bb','R.A','L.D','L.A'),('R.A','L.D','L.A'))
    return compute,compute+[instruction(('acc',),'pb')]+compute[::-1]

COMP,CIRCUIT=program()

def step(bits,g):
    controls,target=g
    if all(bits[c] for c in controls): bits[target]^=1


def execute(bits,gates=CIRCUIT,trace=False):
    out=list(bits)
    def raw(): return 4*out[INDEX['pa']]+2*out[INDEX['pb']]+out[INDEX['pd']]
    history=[raw()] if trace else []
    for g in gates:
        step(out,g)
        if trace: history.append(raw())
    return out,tuple(history)


def logical(bits):
    s=sum(bits[INDEX[n]] for n in SWIRES)%2
    y=bits[INDEX['L.B']];r=bits[INDEX['R.D']];z=bits[INDEX['R.B']]
    k=bits[INDEX['L.A']]+2*bits[INDEX['L.D']]+4*bits[INDEX['R.A']]
    a=y^s;b=r^s
    limits=5 if a==b==0 else 0 if (a,b)==(0,1) else 4 if (a,b)==(1,0) else 1
    return int(k<limits),(s,y,r,z)


def analytic_prefix(flag,pa,pd,length=89,copy=45):
    return tuple(4*pa+pd+(2*flag if t>=copy else 0) for t in range(length+1))


def arrays(values):
    out=[0]*31
    for label,value in zip(TRIPLES,values):
        for j,c in enumerate('ABD'): out[INDEX[label+'.'+c]]=value[j]
    return out


def bits3(n): return ((n>>2)&1,(n>>1)&1,n&1)
def num3(v): return 4*v[0]+2*v[1]+v[2]
def xor3(*vectors): return tuple(sum(v[i] for v in vectors)%2 for i in range(3))
def H(v): return (v[1],v[2],v[0]^(v[1]&v[2]))


def det(count):
    w=sum(count.values())
    means=[sum(Q(n,w)*(1-2*j[i]) for j,n in count.items()) for i in (0,1,3)]
    return (1-sum(t*t for t in means))/4


def variation(p,q):
    return sum((abs(p.get(k,Q())-q.get(k,Q())) for k in p.keys()|q.keys()),Q())/2


def source_inputs(directory):
    spec=json.loads((Path(__file__).parent/'INPUT-HASHES.json').read_text())
    for row in spec['files']:
        b=(directory/row['name']).read_bytes()
        actual=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        check('immutable_git_blob',actual==row['remote_blob_sha']==row['git_blob'])
        check('immutable_sha256',hashlib.sha256(b).hexdigest()==row['sha256'])
    return spec


def primitive_and_truth():
    for controls,target in CIRCUIT:
        check('elementary_gate_valid',len(controls)<=2 and len(set(controls))==len(controls) and target not in controls)
        for values in product((0,1),repeat=len(controls)+1):
            b=[0]*31
            for n,x in zip(controls+(target,),values): b[n]=x
            c=list(b);step(c,(controls,target));step(c,(controls,target))
            check('primitive_involution',c==b)
    cache={}
    relevant=sorted(set(INDEX[n] for n in SWIRES+('L.B','L.A','R.A')))
    check('ten_relevant_phase_bits',len(relevant)==10)
    for value in range(1024):
        b=[0]*31
        for j,i in enumerate(relevant): b[i]=(value>>j)&1
        # Irrelevant phase bits are varied too; they cannot influence the gate.
        for j,i in enumerate(sorted(UNUSED)): b[i]=(value>>(j%10))&1
        flag,carrier=logical(b)
        mid,_=execute(b,COMP)
        cache[tuple(b[i] for i in relevant)]=(flag,tuple(mid[INDEX[n]] for n in WS))
        for pa,pd in product((0,1),repeat=2):
            b[INDEX['pa']]=pa;b[INDEX['pd']]=pd
            out,history=execute(b,trace=True)
            check('threshold_boolean_truth',out[INDEX['pb']]==flag)
            check('phase_restored',out[:21]==b[:21])
            check('workspace_clean',all(out[INDEX[n]]==0 for n in WS))
            check('all_padding_complete_prefix',history==analytic_prefix(flag,pa,pd))
    # Arbitrary dirty states and full reversed program, independent deterministic samples.
    for v in range(512):
        seed=int.from_bytes(hashlib.sha512(('dirty:'+str(v)).encode()).digest(),'big')
        b=[(seed>>i)&1 for i in range(31)]
        c,_=execute(b);d,_=execute(c,CIRCUIT[::-1])
        check('dirty_global_inverse',d==b)
    # Independently partition the threshold, exhaust all five predicate operands.
    for a,b,k in product(range(2),range(2),range(8)):
        case=(b==0 and k<4)+(a==b==0 and k==4)+(a==b==1 and k==0)
        limit=((5,0),(4,1))[a][b]
        check('disjoint_threshold_partition',case in (0,1) and case==int(k<limit))
    # Missing the first scratch Toffoli must change the five-control circuit.
    five=conjunction(('aa','bb','R.A','L.D','L.A'),())
    changes=0
    for assignment in range(64):
        b=[0]*31
        controls=('aa','bb','R.A','L.D','L.A','acc')
        for j,n in enumerate(controls): b[INDEX[n]]=(assignment>>j)&1
        wanted=b[INDEX['acc']]^(int(all(b[INDEX[n]] for n in controls[:5])))
        good,_=execute(b,five);bad,_=execute(b,five[1:])
        check('five_control_decomposition',good[INDEX['acc']]==wanted and all(good[INDEX[n]]==0 for n in ('j0','j1','j2')))
        changes+=int(bad!=good)
    check('broken_ladder_nonvacuous',changes==16)
    return relevant,cache


def kernel(relevant,cache):
    trace_cache={(f,pa,pd):analytic_prefix(f,pa,pd) for f,pa,pd in product(range(2),repeat=3)}
    worlds=padded=cells=negative=positive=reject=dirty=guards=old_revived=0
    key_min=Q();work_min=Q();leak_witness=None
    digest=hashlib.sha256()
    for pnum,cnum in product(range(8),repeat=2):
        p=bits3(pnum);c=bits3(cnum);s=p[1]
        law=Counter();bykey=defaultdict(Counter);bywork=defaultdict(Counter)
        counts_per_flag=Counter()
        for ln,rn,mn in product(range(8),repeat=3):
            l=bits3(ln);r=bits3(rn);m=bits3(mn)
            v=xor3(p,H(xor3(l,r,m,c)))
            phase=arrays((l,r,m,c,(0,0,0),(0,0,0),v))
            computed,j=logical(phase)
            cacheflag,workspace=cache[tuple(phase[i] for i in relevant)]
            check('native_conditional_operand',j==(s,l[1],r[2],r[1]))
            check('kernel_uses_verified_gate_table',computed==cacheflag)
            dirty+=int(any(workspace))
            if computed:
                bykey[num3(v),mn][j]+=1
                bywork[l[1]^s][j]+=1
            for pa,pd in product((0,1),repeat=2):
                raw=trace_cache[computed,pa,pd]
                law[num3(v),raw,computed,j]+=1
                padded+=1
            digest.update(bytes((pnum,cnum,ln,rn,mn,num3(v),computed)))
            counts_per_flag[computed]+=1
            worlds+=1
        check('both_physical_flag_masses',counts_per_flag=={0:352,1:160})
        for vn,pa,pd,flag,j in product(range(8),range(2),range(2),range(2),product(range(2),repeat=4)):
            # Reference mask counts are5,0,4,1; this loop retains every zero cell.
            a=j[1]^s;b=j[2]^s
            n=5 if (a,b)==(0,0) else 0 if (a,b)==(0,1) else 4 if (a,b)==(1,0) else 1
            expected=(n if flag else 8-n) if j[0]==s else 0
            count=law[vn,trace_cache[flag,pa,pd],flag,j]
            check('complete_joint_kernel_including_zeros',count==expected)
            reject+=int(flag==0 and expected>0)
            cells+=1
        if p[0]==0:
            for vn,pa,pd in product(range(8),range(2),range(2)):
                samples={j:law[vn,trace_cache[1,pa,pd],1,j] for j in product(range(2),repeat=4)}
                check('accepted_whole_record_positive',sum(samples.values())==20 and det(samples)==0)
                check('accepted_full_post_X_mask',sorted(n for n in samples.values() if n)==[1,1,4,4,5,5])
                positive+=1
            for (vn,mn),counts in bykey.items():
                value=det(counts)
                if value<0:
                    negative+=1
                    if value<key_min:
                        key_min=value;leak_witness={'old':pnum,'complement':cnum,'V':vn,'M':mn}
            for counts in bywork.values():
                value=det(counts)
                check('public_workspace_leak',value==Q(-1,4))
                work_min=min(work_min,value)
        # No-offer is a separate interface guard; every actual source row has
        # the same physical pointer regardless of an already terminal old flag.
        for oldflag in range(2):
            if oldflag and p[0]: continue
            offered_mass=Q(counts_per_flag[1],512) if oldflag else Q()
            actual_offers=Counter()
            for (vn,tr,f,j),n in law.items():
                offer=j if oldflag and f else None
                actual_offers[offer]+=n
                if not oldflag and f: old_revived+=n
            check('terminal_and_valid_offer_guard',sum(v for j,v in actual_offers.items() if j is not None)==2048*offered_mass)
            if not oldflag: check('all_prior_terminal_records_have_no_offer',set(actual_offers)=={None})
            guards+=1
    check('private_key_leak_exact',negative==1024 and key_min==Q(-1,18))
    check('workspace_uncompute_countercontrol',dirty==31232)
    return {'phase_worlds':worlds,'padded_worlds':padded,'kernel_cells':cells,
        'positive_accepted_complete_records':positive,'rejected_cells':reject,
        'terminal_guard_contexts':guards,'uncompute_omission_dirty_worlds':dirty,
        'private_key_negative_posteriors':negative,'private_key_min_det':str(key_min),
        'private_key_witness':leak_witness,'workspace_leak_det':str(work_min),
        'hypothetical_guard_omission_offered_padded_worlds':old_revived,
        'phase_kernel_sha256':digest.hexdigest()}


def recording():
    gates=[]
    for t in range(90):
        gates.extend((((INDEX[n],),31+3*t+j) for j,n in enumerate(('pa','pb','pd'))))
        if t<89: gates.append(CIRCUIT[t])
    check('recording_resource_count',len(gates)==359 and max(g[1] for g in gates)+1==301)
    for v in range(64):
        seed=int.from_bytes(hashlib.sha512(('record:'+str(v)).encode()).digest(),'big')
        phase=[(seed>>i)&1 for i in range(21)]
        for pa,pd in product((0,1),repeat=2):
            initial=phase+[0]*280
            initial[INDEX['pa']]=pa;initial[INDEX['pd']]=pd
            flag,_=logical(initial)
            out,tr=execute(initial,gates,trace=True)
            check('recorded_complete_pointer_prefix',tr==analytic_prefix(flag,pa,pd,359,180))
            expected=analytic_prefix(flag,pa,pd)
            bank=[4*out[31+3*t]+2*out[31+3*t+1]+out[31+3*t+2] for t in range(90)]
            check('all_270_record_bits',bank==list(expected))
            restored,_=execute(out,gates[::-1])
            check('recording_ready_inverse',restored==initial and out[:21]==phase and all(out[INDEX[n]]==0 for n in WS))
    for v in range(64):
        seed=int.from_bytes(hashlib.sha512(('record-dirty:'+str(v)).encode()).digest(),'big')
        b=[(seed>>i)&1 for i in range(301)]
        c,_=execute(b,gates);d,_=execute(c,gates[::-1])
        check('recording_dirty_inverse',d==b)
    return Counter(len(g[0]) for g in gates)


def flag_and_padding_controls():
    failures=[]
    for s in range(2):
        intended=defaultdict(Q);fake=defaultdict(Q)
        for ln,rn in product(range(8),repeat=2):
            l=bits3(ln);r=bits3(rn);j=(s,l[1],r[2],r[1])
            k=l[0]+2*l[2]+4*r[0]
            bound=((5,0),(4,1))[j[1]^s][j[2]^s]
            flag=int(k<bound)
            intended[flag,j if flag else None]+=Q(1,64)
            for w in range(16):
                other=int(w in (0,1,2,3,4))
                fake[other,j if other else None]+=Q(1,1024)
        check('matched_success_rate',sum(v for (a,j),v in intended.items() if a)==sum(v for (a,j),v in fake.items() if a)==Q(5,16))
        delta=variation(intended,fake);check('unrelated_flag_wrong_joint_law',delta==Q(1,8));failures.append(str(delta))
    fresh=Counter({(a,b):Q(1,16) for a,b in product(range(4),repeat=2)})
    reused=Counter({(a,a):Q(1,4) for a in range(4)})
    check('padding_only_reference_difference',variation(fresh,reused)==Q(3,4))
    return failures


def six_neighbors(p):
    for i in range(3):
        for d in (-1,1):
            q=list(p);q[i]+=d;yield tuple(q)


def native_delay():
    # Independent4096-world bit-sliced full3D evolution, no scalar H lookup.
    points=((0,0,0),(-1,0,-1),(-1,0,1),(-2,0,0));mask=(1<<4096)-1
    fields={}
    for variable,p in enumerate(points):
        fields[p]=tuple(sum(1<<n for n in range(4096) if ((n>>(9-3*variable+2-c))&1)) for c in range(3))
    # Above each3-bit source is ordered by its own integer bit positions; only
    # the independent source ensemble and response counts matter.
    def update(old,now):
        touched=set(old)
        for p in now: touched.update(six_neighbors(p))
        out={}
        for p in touched:
            ns=[0,0,0]
            for q in six_neighbors(p):
                w=now.get(q,(0,0,0))
                for c in range(3): ns[c]^=w[c]
            prev=old.get(p,(0,0,0))
            value=(prev[0]^ns[1],prev[1]^ns[2],prev[2]^ns[0]^(ns[1]&ns[2]))
            if any(value): out[p]=value
        return out
    first=update({},fields);second=update(fields,first);third=update(first,second)
    q=(0,0,0);L=(0,0,-1);R=(0,0,1)
    def phase(now,previous):
        s=now.get(q,(0,0,0))[1]
        for n in six_neighbors(q): s^=previous.get(n,(0,0,0))[2]
        return (s,previous.get(L,(0,0,0))[1],previous.get(R,(0,0,0))[2],previous.get(R,(0,0,0))[1])
    a=phase(second,first);b=phase(third,second)
    check('native_inverse_at_intended_cut',a[0]==fields[q][1])
    check('wrong_cut_all_zero',b==(0,0,0,0))
    wrong=(a[0]^b[0]).bit_count();pool=0
    for i in (1,2,3): pool|=a[i]^b[i]
    check('delay_changes_sign',wrong==2048)
    check('delay_changes_pool',pool.bit_count()==3584)
    check('off_axis_propagation_retained',any(p[1]!=0 for p in second))
    return {'worlds':4096,'changed_sign':wrong,'changed_pool':pool.bit_count(),
        'actual_L_delay_claimed':False}


def main(author):
    spec=source_inputs(author)
    relevant,cache=primitive_and_truth()
    kinds=Counter(len(g[0]) for g in CIRCUIT)
    check('core_resource_counts',len(NAMES)==31 and len(COMP)==44 and len(CIRCUIT)==89 and kinds=={0:36,1:23,2:30})
    law=kernel(relevant,cache)
    recorded=recording()
    flags=flag_and_padding_controls();delay=native_delay()
    check('hypothetical_latency_only',2+len(CIRCUIT)==91 and 2+sum(recorded.values())==361 and 77<91 and 79<91)
    return {'schema':'oi-composition-flag-v6-independent-review.1','verdict':'ACCEPT_WITHIN_STATED_SCOPE',
        'author_commit':spec['author_commit'],'remote_git_blobs_verified':len(spec['files']),
        'engine_imports_author_code':False,'core':{'ticks':len(CIRCUIT),'bits':31,'NOT':kinds[0],'CNOT':kinds[1],'Toffoli':kinds[2],'pointer_copy_tick':45},
        'explicit_recording':{'ticks':sum(recorded.values()),'bits':301,'additional_clean_record_bits':270,'NOT':recorded[0],'CNOT':recorded[1],'Toffoli':recorded[2],'pointer_copy_tick':180},
        'conditional_kernel':law,'wrong_rate_matched_flags_TV':flags,'padding_reference_TV':'3/4','native_delay_control':delay,
        'native_availability_established':False,'native_delay_protected':False,'access_contract_adopted':False,
        'blockers':[],'checks':dict(sorted(COUNTS.items()))}


if __name__=='__main__':
    ap=ArgumentParser();ap.add_argument('--author-root',type=Path);ap.add_argument('--output',type=Path);a=ap.parse_args()
    candidates=[Path(__file__).parent.parent/'composition_flag_v6',Path(__file__).parent.parent]
    author=a.author_root or next((p for p in candidates if (p/'PLAN.md').exists() and (p/'checks.py').exists()),None)
    if author is None: raise RuntimeError('supply --author-root')
    out=json.dumps(main(author),indent=2,sort_keys=True)+'\n'
    if a.output: a.output.write_text(out)
    else: print(out,end='')
