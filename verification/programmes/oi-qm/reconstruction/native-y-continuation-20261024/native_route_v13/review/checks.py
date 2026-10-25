"""Independent packed-native review; imports no author engine."""
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import combinations,product
import json
from pathlib import Path
import sys

STEPS=tuple(tuple(sign if k==axis else 0 for k in range(3)) for axis in range(3) for sign in (-1,1))
T=185
P=12*840**185
S=P+T
R=S+68
L=R+9


def need(ok,why):
    if not ok:
        raise RuntimeError(why)


def plus(a,b):
    return tuple(x+y for x,y in zip(a,b))


def md(a,b):
    return sum(abs(x-y) for x,y in zip(a,b))


def ball(c,r):
    return [plus(c,p) for p in product(range(-r,r+1),repeat=3) if sum(map(abs,p))<=r]


class Packed:
    def __init__(self,count):
        self.count=count
        self.dmask=sum(1<<(3*i) for i in range(count))
        self.bmask=self.dmask<<1
        self.amask=self.dmask<<2
    def H(self,q):
        return ((q&self.bmask)<<1)^((q&self.dmask)<<1)^((q&self.amask)>>2)^(((q&self.bmask)>>1)&q&self.dmask)
    def pow(self,q,k):
        for _ in range(k%12):q=self.H(q)
        return q
    def from_codes(self,vals):
        return sum(x<<(3*i) for i,x in enumerate(vals))
    def code(self,q,i):
        return(q>>(3*i))&7
    def xor(self,vals):
        ans=0
        for v in vals:ans^=v
        return ans


def full_native(initial,engine):
    positions=tuple(initial)
    @lru_cache(None)
    def value(t,p):
        if t<0:return 0
        if min(md(p,q) for q in positions)>t:return 0
        if (t-sum(p))%2:return 0
        if t==0:return initial.get(p,0)
        return value(t-2,p)^engine.H(engine.xor(value(t-1,plus(p,d)) for d in STEPS))
    return value


def upper_engine():
    rows=list(product((0,1),repeat=3))
    rows=[(*r,n) for r in rows for n in range(8)]
    en=Packed(64)
    source={(0,0,0):en.from_codes([4*u+1 for u,a,b,n in rows]),
            (0,0,-14):en.from_codes([4*u+u for u,a,b,n in rows]),
            (0,0,-16):en.from_codes([4*u+2*(1^u)+1 for u,a,b,n in rows]),
            (0,0,-18):en.from_codes([4*(u^b)+2*a+(u^a) for u,a,b,n in rows]),
            (1,0,-17):en.from_codes([5*(a^b) for u,a,b,n in rows]),
            (-1,0,-17):en.from_codes([7*(a^b) for u,a,b,n in rows]),
            (0,0,-20):en.from_codes([n for u,a,b,n in rows])}
    raw=full_native(source,en)
    return en,rows,raw


def lower_grid():
    # Independent full monotone two-dimensional grid; no three-level recurrence.
    en=Packed(16)
    rows=list(product((0,1),range(8)))
    origins={0:en.from_codes([2*x for x,e in rows]),76:en.from_codes([7]*16),78:en.from_codes([e for x,e in rows])}
    # Coordinates are (time,z), y=time-z. All sources start at time zero.
    now={z:origins.get(z,0) for z in range(79)}
    queried={}
    for time in range(255):
        for z in (76,77,78):
            y=time-z
            if 0<=y<=176:queried[y,z]=now[z]
        now={z:en.H(now[z]^(now[z-1] if z else 0)) for z in range(79)}
    return en,rows,queried


def geometry(root):
    target=(0,S,78);e=(0,-78,78);n=(0,S,S+156);deadline=L+1
    inventory=json.loads((root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())['sources']
    need(len(inventory)==1479,'inventory count')
    need(all(md(tuple(r['position']),target)>=deadline for r in inventory),'new ready ball overwrites source')
    need(all(tuple(r['position']) not in(e,n) for r in inventory),'new source coincidence')
    ports=[(0,T,0),(0,0,-8*T),(T,P,0),(-T,P,0),(4*T,P,0),(0,S,0),(12*R,0,0),(48*L,0,0)]
    times=[T,T,S,S,S,S,R,L]
    ready=list(zip(ports,times))+[((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]+[((0,S,68+k),R+k) for k in range(10)]+[((-48*L,0,0),L)]
    for source in(e,n):
        need(md(source,target)==deadline,'new source first arrival')
        need(md(source,(0,S,77))==L+2,'q9 causal protection')
        for c,r in ready:need(md(source,c)>r,'source enters old ready cone')
        for c,t in zip(ports,times):need(md(source,c)>t,'old informative record changed')
    directions=[(0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0),(1,0,0)]
    bank_slacks=[]
    for port,d,start in zip(ports,directions,times):
        axis=next(k for k in range(3) if d[k])
        kink=(target[axis]-port[axis])*d[axis]
        clamped=max(start+1,min(deadline,kink))
        candidates={start+1,deadline,clamped}
        minimum=min(md(plus(port,tuple(t*x for x in d)),target) for t in candidates)
        need(minimum>deadline,'bank intersects new ready pins')
        bank_slacks.append(minimum-deadline)
        for source in(e,n):
            t=(source[axis]-port[axis])*d[axis]
            if start+1<=t<=deadline:
                need(plus(port,tuple(t*x for x in d))!=source,'new source on bank ray')
    arrivals=[]
    for dt,radius in((-2,10),(-1,11)):
        for p in ball((0,0,10),radius):
            absolute=(p[0],S+p[1],68+p[2])
            if md(e,absolute)<=R+dt:arrivals.append([dt,list(p),md(e,absolute)-(R+dt)])
    need(arrivals==[[-1,[0,-11,10],0]],'E diamond entry')
    need(P%(12*840**20)==0 and P%(384*840**3)==0,'period divisibility')
    need(256*L+64*T+1>2*(51*L+S+8*T+200),'no-wrap envelope')
    return {'source_rows':1479,'ready_exclusions':2*len(ready),'informative_deadline_exclusions':16,'bank_rays':8,'minimum_bank_slack':min(bank_slacks),'E_entry':arrivals,'period_divisibility':True}


def reconstruction():
    ue,ur,upper=upper_engine()
    le,lr,front=lower_grid()
    allrows=list(product((0,1),repeat=6))
    allrows=[(*r,e,n) for r in allrows for e,n in product(range(8),repeat=2)]
    en=Packed(4096)
    upper_index={row:i for i,row in enumerate(ur)}
    def expand_upper(v):
        return en.from_codes([ue.code(v,upper_index[u,a,b,n]) for x,u,my,mr,a,b,e,n in allrows])
    def expand_lower(v):
        return en.from_codes([le.code(v,8*x+e) for x,u,my,mr,a,b,e,n in allrows])
    signals=[((0,-S,-68),en.from_codes([2*x for x,u,my,mr,a,b,e,n in allrows])),
             ((0,S,-68),en.from_codes([2*(my^mr) for x,u,my,mr,a,b,e,n in allrows])),
             ((T,P,-68),en.from_codes([2*my for x,u,my,mr,a,b,e,n in allrows])),
             ((-T,P,-68),en.from_codes([2*mr for x,u,my,mr,a,b,e,n in allrows]))]
    def lucas(displacements):
        acc=0
        for q in displacements:
            if acc&q:return False
            acc|=q
        return True
    entries={(0,-9,8):(176,76),(0,-10,9):(175,77),(0,-11,10):(174,78)}
    upper_requests=set()
    @lru_cache(None)
    def base(dt,p):
        time=R+dt
        nsmall=253-p[2]
        reduced_time=253+dt
        upper_requests.add((reduced_time,p[0],p[1],nsmall))
        out=expand_upper(upper(reduced_time,(p[0],p[1],nsmall)))
        for source,bits in signals:
            displacements=tuple(abs(v-q) for v,q in zip(source,p))
            if sum(displacements)<=time:
                need(sum(displacements)==time,'lower outside first-front region')
                if lucas(displacements):out^=en.pow(bits,time)
        if dt==-1 and p in entries:
            j,z=entries[p]
            original_signal=en.pow(signals[0][1],time) if lucas((0,S+p[1],68+p[2])) else 0
            need(out==original_signal,'coupled entry contains extra upper/selector term')
            out=expand_lower(front[j,z])
        return out
    old={p:base(-2,p) for p in ball((0,0,10),10)}
    now={p:base(-1,p) for p in ball((0,0,10),11)}
    records={}
    for tick in range(11):
        nxt={p:old[p]^en.H(en.xor(now[plus(p,d)] for d in STEPS)) for p in ball((0,0,10),10-tick)}
        records[tick]=nxt
        old,now=now,nxt
    return en,allrows,now[(0,0,10)],records,front,upper,ue,upper_requests


def source_pins(here,author_root,source_root):
    pins=json.loads((here/'INPUT-HASHES.json').read_text())
    for name,entry in pins['author_files'].items():
        data=(author_root/name).read_bytes()
        need(hashlib.sha256(data).hexdigest()==entry['sha256'],'pinned author SHA256 '+name)
        need(hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==entry['git_blob'],'pinned Git blob '+name)
    for name,entry in pins['input_files'].items():
        need(hashlib.sha256((source_root/name).read_bytes()).hexdigest()==entry['sha256'],'pinned prior input '+name)
    return {'pinned_author_git_blobs':len(pins['author_files']),'pinned_prior_inputs':len(pins['input_files'])}


def lower_controls(front):
    en=Packed(16)
    rows=list(product((0,1),range(8)))
    initial={(0,0,0):en.from_codes([2*x for x,e in rows]),(0,-76,76):en.from_codes([7]*16),(0,-78,78):en.from_codes([e for x,e in rows])}
    native=full_native(initial,en)
    full_comparisons=0
    for j in (0,2,5):
        for z in (76,77,78):
            need(native(j+z,(0,j,z))==front[j,z],'independent actual-gap full native/lower grid')
            full_comparisons+=16
    levels=[front[0,z] for z in (76,77,78)]
    origin=initial[(0,0,0)]
    layer_comparisons=3
    for j in range(1,177):
        force=en.pow(origin,j+75) if not j&75 else 0
        levels[0]=en.H(levels[0]^force)
        levels[1]=en.H(levels[1]^levels[0])
        levels[2]=en.H(levels[2]^levels[1])
        for ell,z in enumerate((76,77,78)):
            need(levels[ell]==front[j,z],'coupled three-layer recurrence/full monotone grid')
            layer_comparisons+=1
    small_initial={(0,0,0):initial[(0,0,0)],(0,-3,3):initial[(0,-76,76)],(0,-5,5):initial[(0,-78,78)]}
    small_native=full_native(small_initial,en)
    now={z:small_initial.get((0,-z,z),0) for z in range(6)}
    small=0
    for time in range(10):
        for z in range(6):
            need(small_native(time,(0,time-z,z))==now[z],'small full3D source/front comparison')
            small+=16
        now={z:en.H(now[z]^(now[z-1] if z else 0)) for z in range(6)}
    return {'actual_gap_full_native_scalar_comparisons':full_comparisons,
            'coupled_layer_queries_checked':layer_comparisons,'small_gap_full3D_scalar_comparisons':small,
            'actual_gap_full_native_nodes':native.cache_info().currsize}


def affine_decision(en,rows,out,author):
    index={r:i for i,r in enumerate(rows)}
    contexts=[k for k in product((0,1),repeat=5) if k[3:]!=(0,1)]
    features=[1+sum(b<<(j+1) for j,b in enumerate(k)) for k in contexts]
    patterns=[sum(((c&f).bit_count()%2)<<j for j,f in enumerate(features)) for c in range(64)]
    def val(s,k,e,n):
        u,my,mr,a,b=k
        return en.code(out,index[s^u^a,u,my,mr,a,b,e,n])
    lookups=[]
    common=None;old_common=None
    for k in contexts:
        pairs={}
        for e,n in product(range(8),repeat=2):
            pair=(val(0,k,e,n),val(1,k,e,n))
            if pair[0]!=pair[1]:pairs.setdefault(pair,{})[e]=n
        lookups.append(pairs)
        common=set(pairs) if common is None else common&set(pairs)
        old={(val(0,k,0,n),val(1,k,0,n)) for n in range(8)}
        old={p for p in old if p[0]!=p[1]}
        old_common=old if old_common is None else old_common&old
    need(sorted(map(list,common))==author['controller']['common_raw_pairs'],'common native pair intersection')
    need(not old_common,'old E0 exclusion')
    # A different exhaustive representation: one bit for each of all 64^3
    # coefficient triples, then intersect full-map masks at every context.
    count=64**3;universe=(1<<count)-1
    repeat64=universe//((1<<64)-1)
    repeat4096=universe//((1<<4096)-1)
    masks=[]
    for f in features:
        truth=[(c&f).bit_count()%2 for c in range(64)]
        aa=sum(v<<c for c,v in enumerate(truth))*repeat64
        bb=sum(((1<<64)-1)<<(64*c) for c,v in enumerate(truth) if v)*repeat4096
        dd=sum(((1<<4096)-1)<<(4096*c) for c,v in enumerate(truth) if v)
        masks.append([((aa if code&4 else universe^aa)&(bb if code&2 else universe^bb)&(dd if code&1 else universe^dd)) for code in range(8)])
    def restrict(allowed):
        survivors=universe
        for j,codes in enumerate(allowed):
            mask=0
            for code in codes:mask|=masks[j][code]
            survivors&=mask
            if not survivors:break
        return survivors
    def ecodes(ca,cb,cd):
        return [4*((ca&f).bit_count()%2)+2*((cb&f).bit_count()%2)+((cd&f).bit_count()%2) for f in features]
    known=(9,23,50)
    need(restrict([{v} for v in ecodes(*known)])==1<<(known[0]+64*known[1]+4096*known[2]),'full-map filter positive control')
    mutated=ecodes(*known);mutated[0]^=1
    need(restrict([{v} for v in mutated])==0,'full-map filter negative control')
    valid_patterns=set(patterns)
    def n_affine(values):
        return all(sum(((v>>field)&1)<<j for j,v in enumerate(values)) in valid_patterns for field in (0,1,2))
    need(n_affine(ecodes(37,12,55)),'independent affine membership positive control')
    need(not n_affine([k[0]&k[1] for k in contexts]),'independent affine membership nonlinear control')
    per_pair=[];total_e=total_both=0;witnesses=[]
    for pair in sorted(common):
        options=[lookup[pair] for lookup in lookups]
        surviving=restrict([set(opt) for opt in options])
        es=surviving.bit_count();both=0
        for_record=[]
        while surviving:
            bit=surviving&-surviving;candidate=bit.bit_length()-1;surviving^=bit
            ca=candidate&63;cb=(candidate>>6)&63;cd=candidate>>12
            evalues=ecodes(ca,cb,cd)
            nvalues=[opt[e] for opt,e in zip(options,evalues)]
            is_affine=n_affine(nvalues)
            both+=is_affine
            coefficients=[4*((ca>>i)&1)+2*((cb>>i)&1)+((cd>>i)&1) for i in range(6)]
            witness=None
            if not is_affine:
                for js in combinations(range(24),4):
                    f=0;v=0
                    for j in js:f^=features[j];v^=nvalues[j]
                    if not f and v:
                        witness={'contexts':[list(contexts[j]) for j in js],'required_N':[nvalues[j] for j in js],'N_xor':v}
                        break
                need(witness is not None,'nonaffine source lacks explicit dependency witness')
            for_record.append({'E_coefficients':coefficients,'N_affine':is_affine,'dependency_witness':witness})
        expected=next(r for r in author['controller']['per_pair_affine_results'] if tuple(r['raw_pair'])==pair)
        need(es==expected['affine_E_maps_after_constraints'] and both==expected['joint_affine_E_N_maps'],'affine decision differs')
        for_record.sort(key=lambda r:r['E_coefficients'])
        if for_record:witnesses.append({'raw_pair':list(pair),'survivors':for_record})
        total_e+=es;total_both+=both
        per_pair.append([list(pair),es,both])
    # Verify every author's explicit rejection directly on independently computed native table.
    stated=0
    for entry in author['controller']['per_pair_affine_results']:
        rejection=entry['first_N_rejection']
        if rejection is None:continue
        coeff=rejection['E_coeff_constant_u_mY_mR_a_b'];pair=tuple(entry['raw_pair']);proof=rejection['N_affine_inconsistency']
        f_xor=n_xor=0
        for k,n in zip(proof['contexts_u_mY_mR_a_b'],proof['required_N_codes']):
            k=tuple(k);e=coeff[0]
            for b,c in zip(k,coeff[1:]):
                if b:e^=c
            need((val(0,k,e,n),val(1,k,e,n))==pair,'reported required-N native witness')
            f_xor^=features[contexts.index(k)];n_xor^=n
        need(f_xor==0 and n_xor==proof['required_N_code_xor']!=0,'reported affine dependency witness')
        stated+=1
    return {'accepted_contexts':24,'common_injective_pairs':len(common),'affine_E_maps_exhaustively_represented_per_pair':count,
            'affine_E_survivors':total_e,'joint_affine_E_N_survivors':total_both,'per_pair_counts':per_pair,
            'independent_N_dependency_witnesses':witnesses,'author_N_dependency_witnesses_checked':stated,
            'affine_solver_controls':4,'arbitrary_redundant_decoder':'not tested'}


def main():
    here=Path(__file__).resolve().parent
    native_default=here.parent.parent if(here.parent.parent/'parallel_v3').exists() else here.parent/'checkpoint_v12'
    author_default=here.parent if(here.parent/'PLAN.md').exists() else here.parent/'native_route_v13'
    parser=argparse.ArgumentParser();parser.add_argument('--source-root',type=Path,default=native_default);parser.add_argument('--author-root',type=Path,default=author_default);args=parser.parse_args()
    pins=source_pins(here,args.author_root,args.source_root)
    geo=geometry(args.source_root)
    en,rows,out,records,front,upper,ue,requests=reconstruction()
    lower=lower_controls(front)
    table=''.join(format(en.code(out,i),'x') for i in range(len(rows)))
    author=json.loads((args.author_root/'result.json').read_text())
    need(table==author['q10_table_hex'],'independent complete q10 table differs')
    old=json.loads((args.source_root/'native_seed_v12/result.json').read_text())
    old_table=''.join(format(en.code(out,i),'x') for i,row in enumerate(rows) if row[6]==0)
    need(old_table==old['q10_table_hex'],'old E0 512-row reference')
    q9=json.loads((args.source_root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    q9_checked=0
    for i,(x,u,my,mr,a,b,e,n) in enumerate(rows):
        reference_index=0
        for v,size in zip((x,u,my,mr,a,b,4,5,7),(2,2,2,2,2,2,8,8,8)):reference_index=size*reference_index+v
        need(en.code(records[9][(0,0,9)],i)==int(q9[reference_index],16),'old full q9 raw table')
        need(en.code(records[0][(0,0,0)],i)==4*x+2+(x^u),'qY preservation')
        need(en.code(records[7][(0,0,7)],i)==x^u,'q7 preservation')
        need(en.code(records[8][(0,0,8)],i)==2*(x^u),'q8 preservation')
        q9_checked+=1
    index={r:i for i,r in enumerate(rows)}
    permutations=0
    for context in product((0,1),repeat=6):
        for held in range(8):
            need(len({en.code(out,index[*context,e,held]) for e in range(8)})==8,'own-E permutation')
            need(len({en.code(out,index[*context,held,n]) for n in range(8)})==8,'own-N permutation')
            permutations+=2
    changed=sum(en.code(out,i)!=en.code(out,index[*row[:6],0,row[7]]) for i,row in enumerate(rows))
    need(changed==author['checks']['omitted_E_changed_rows']>0,'nonvacuous E deletion control')
    affine=affine_decision(en,rows,out,author)
    # H exponent and the full eight-symbol conditional gate maps used in period induction.
    tiny=Packed(1)
    for q in range(8):
        v=q
        for _ in range(12):v=tiny.H(v)
        need(v==q,'H exponent by twelve actual native H applications')
    for shift in range(8):need(len({tiny.H(q^shift) for q in range(8)})==8,'forced one-coordinate permutation')
    result={'schema':'oi-native-route-v13-independent-review-1','reviewed_author':'753fe4f69392ca940754489468e8c8235f6aa583','pins':pins,
            'independent_native_table':{'rows':4096,'sha256':hashlib.sha256(table.encode()).hexdigest(),'upper_native_cached_nodes':upper.cache_info().currsize,'upper_reduced_requests':len(requests),
              'E0_old_rows_checked':512,'qY_q7_q8_q9_rows_each':q9_checked,'own_E_and_N_permutation_contexts':permutations,'omitted_E_changed_rows':changed},
            'geometry':geo,'lower_controls':lower,'affine_decision':affine,
            'all_controls_passed':True,'verdict':'ACCEPT_WITHIN_STATED_SCOPE','blockers':[],
            'limits':['large-time proof reviewed separately from finite controls','no native flag, reusable instrument, access adoption or general no-go','redundant arbitrary decoder untested','separate-agent internal review, not external or kernel certification']}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))


if __name__=='__main__':
    sys.setrecursionlimit(2000)
    main()
