#!/usr/bin/env python3
"""Separate forward-cone engine for the pinned native short-window gate author."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import hashlib
import json

PAYLOADS=list(product(range(8),repeat=4))
ONE=(1<<4096)-1
ZERO=(0,0,0)
ORIGIN=(0,0,0)
Q8=(0,0,-1)
Q10=(0,0,1)
MASK=(-1,0,0)
DIRECTIONS=((0,0,1),(0,0,-1),(0,1,0),(0,-1,0),(1,0,0),(-1,0,0))
SITES=sorted(p for p in product(range(-2,3),repeat=3) if sum(abs(z) for z in p)<=2)

def require(x,msg):
    if not x:raise RuntimeError(msg)

def hash_json(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def adj(p):
    return [tuple(a+b for a,b in zip(p,d)) for d in DIRECTIONS]

def sites(radius):
    return [p for p in product(range(-radius,radius+1),repeat=3)
            if sum(abs(z) for z in p)<=radius]

def background(seed,t,p):
    if seed is None:return 0
    x,y,z=p
    u=x*x+3*y*y+7*z+13*t+seed
    w=x*y+z*z+11*seed*t
    return (u^w)%8

def value_planes(value):
    return tuple(ONE*int(bool(value&(1<<(2-i)))) for i in range(3))

def values(planes):
    # Decompose whole Boolean columns into byte buffers, rather than call the
    # author's recursive field evaluator or reuse any author implementation.
    columns=[x.to_bytes(512,'little') for x in planes]
    return [sum(((columns[c][lane//8]>>(lane%8))&1)<<(2-c) for c in range(3))
            for lane in range(4096)]

def forward(n,seed,nonlinear=True,oldlocal=True):
    final=n+3
    sources=(-(n-1),0,0),(-n,0,-1),(-n,0,1),(-n-1,0,0)
    radius=final+2
    current={p:value_planes(background(seed,0,p)) for p in sites(radius)}
    previous={p:value_planes(background(seed,-1,p)) for p in sites(radius-1)}
    for column,p in enumerate(sources):
        current[p]=tuple(sum(((row[column]>>(2-c))&1)<<i for i,row in enumerate(PAYLOADS))
                         for c in range(3))
    slices={0:current}
    for t in range(1,final+1):
        nxt={}
        for p in sites(radius-t):
            x=y=z=0
            for q in adj(p):
                qx,qy,qz=current[q]
                x^=qx;y^=qy;z^=qz
            old=previous[p] if oldlocal else ZERO
            nxt[p]=(old[0]^y,old[1]^z,old[2]^x^((y&z) if nonlinear else 0))
        previous,current=current,nxt
        slices[t]=current
    cache={}
    def fetch(t,p):
        if (t,p) not in cache:cache[t,p]=values(slices[t][p])
        return cache[t,p]
    return fetch,sources

def decode_flag(p,left,right):
    sx=(p//2)%2
    y=(left//2)%2
    r=right%2
    k=left//4+2*(left%2)+4*(right//4)
    # Deliberately evaluate explicit four cases, independently of the author's
    # indexed two-dimensional threshold table.
    a,b=y^sx,r^sx
    if a==0 and b==0:return int(k<=4)
    if a==0 and b==1:return 0
    if a==1 and b==0:return int(k<=3)
    return int(k==0)

def pointer_profile(raw,flags,chosen):
    pairs=Counter((raw[i],flags[i]) for i in chosen)
    counts=[[pairs[v,0],pairs[v,1]] for v in range(8)]
    bayes=sum(min(v) for v in counts)
    # Each of the 256 functions is evaluated on full label masks. The error
    # array is generated independently from its source truth labels.
    errors=[]
    for function in range(256):
        errors.append(sum(pairs[v,1] if ((function>>v)&1)==0 else pairs[v,0] for v in range(8)))
    require(min(errors)==bayes,'readout enumeration/Bayes discrepancy')
    mixed=[v for v in range(8) if pairs[v,0] and pairs[v,1]]
    require((bayes>0)==bool(mixed),'collision equivalence')
    witness=None
    if mixed:
        v=mixed[0]
        i=next(i for i in chosen if raw[i]==v and flags[i]==0)
        j=next(i for i in chosen if raw[i]==v and flags[i]==1)
        witness={'raw':v,'A0_payloads':list(PAYLOADS[i]),'A1_payloads':list(PAYLOADS[j])}
        require(PAYLOADS[i]!=PAYLOADS[j],'collision witness identical worlds')
    return counts,bayes,witness

def one_family(n,seed,reference):
    field,sources=forward(n,seed)
    p=field(n-1,ORIGIN)
    left=field(n,Q8);right=field(n,Q10);mask=field(n,MASK);cipher=field(n+1,ORIGIN)
    old_image=[]
    for old in range(8):
        indices=list(range(512*old,512*(old+1)))
        require(len({p[i] for i in indices})==1,'old not independent of apparatus')
        old_image.append(p[512*old])
        require(len({(left[i],right[i],mask[i]) for i in indices})==512,'joint source triangle')
        require(len({(left[i],right[i],cipher[i]) for i in indices})==512,'pool/ciphertext product')
        for a in range(8):
            require(len({left[512*old+64*a+8*b+g] for b,g in product(range(8),repeat=2)})==1,
                    'Q8 non-triangular dependence')
        for b in range(8):
            require(len({right[512*old+64*a+8*b+g] for a,g in product(range(8),repeat=2)})==1,
                    'Q10 non-triangular dependence')
        for a,b in product(range(8),repeat=2):
            require(len({mask[512*old+64*a+8*b+g] for g in range(8)})==8,'M missing final permutation')
        require(sum(decode_flag(p[i],left[i],right[i]) for i in indices)==160,'per-old acceptance mass')
    require(len(set(old_image))==8,'old-image permutation')
    require(old_image==reference['old_source_image'],'published old source image')
    for i in range(4096):
        total=0
        for q in adj(ORIGIN):total^=field(n,q)[i]
        a,b,d=total//4,(total//2)%2,total%2
        inv=cipher[i]^(4*b+2*d+(a^(b*d)))
        require(inv==p[i],'fixed phase inverse')
    flags=[decode_flag(p[i],left[i],right[i]) for i in range(4096)]
    sectors={'all':list(range(4096)),'prepared':[i for i in range(4096) if p[i]<4]}
    require(len(sectors['prepared'])==2048 and sum(flags[i] for i in sectors['prepared'])==640,
            'prepared sector normalization')
    dist=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
    require(dist(sources[0],ORIGIN)==n-1 and all(dist(q,ORIGIN)==n+1 for q in sources[1:]),
            'input/source arrival distances')
    require([[dist(q,t)-n for t in (Q8,Q10,MASK)] for q in sources[1:]]==[[0,2,0],[2,0,0],[2,2,0]],
            'triangular source distances')
    details=[]
    measured=[]
    candidate_count=0
    prefix_count=0
    all_pooled=[]
    for delay in (1,2,3):
        profiles=[]
        for site in SITES:
            raw=field(n+delay,site)
            prefix=list(zip(*(field(t,site) for t in range(n,n+delay+1))))
            entry={'position':list(site),'delay':delay,'raw_counts':None,'prepared_raw_counts':None}
            stats={}
            for label,chosen in sectors.items():
                counts,error,witness=pointer_profile(raw,flags,chosen)
                prefixes=Counter((prefix[i],flags[i]) for i in chosen)
                trace_counts={k:[prefixes[k,0],prefixes[k,1]] for k,a in prefixes}
                prefix_error=sum(min(c) for c in trace_counts.values())
                # Directly retain and verify an opposite-label prefix witness;
                # no target verdict is baked into the collision mechanism.
                mixed=[k for k,c in trace_counts.items() if min(c)>0]
                require((prefix_error>0)==bool(mixed),'prefix collision test')
                candidate_count+=1;prefix_count+=1
                entry['raw_counts' if label=='all' else 'prepared_raw_counts']=counts
                entry[label+'_prefix_support']=len(trace_counts)
                entry[label+'_prefix_Bayes_errors']=prefix_error
                entry[label+'_prefix_counts_sha256']=hash_json(sorted((list(k),v) for k,v in trace_counts.items()))
                stats[label]={'error':error,'prefix':prefix_error,'witness':witness}
            details.append(entry)
            profiles.append((site,stats))
            all_pooled.append((delay,site,entry['raw_counts']))
        ref=reference['deadlines'][delay-1]
        row={'delay':delay}
        for label,chosen in sectors.items():
            minimum=min(x[label]['error'] for site,x in profiles)
            best=[site for site,x in profiles if x[label]['error']==minimum]
            exact=sum(x[label]['error']==0 for site,x in profiles)
            prefix_exact=sum(x[label]['prefix']==0 for site,x in profiles)
            min_prefix=min(x[label]['prefix'] for site,x in profiles)
            require(str(F(minimum,len(chosen)))==ref['minimum_terminal_flag_error_'+label],
                    'terminal minimum differs from author')
            require(str(F(min_prefix,len(chosen)))==ref['minimum_full_prefix_flag_error_'+label],
                    'prefix minimum differs from author')
            require(exact==ref['exact_terminal_site_counts'][label], 'exact terminal count differs')
            require(prefix_exact==ref['exact_prefix_decoder_site_counts'][label], 'exact prefix count differs')
            require(len(best)==ref['best_terminal_site_counts'][label] and
                    [list(z) for z in best[:2]]==ref['best_terminal_site_examples'][label], 'best pointer site differs')
            witness=next(x[label]['witness'] for site,x in profiles if site==best[0])
            require(witness==ref['best_terminal_collision_witnesses'][label], 'collision witness differs')
            row[label]={'minimum_terminal_error':str(F(minimum,len(chosen))),
                        'minimum_prefix_error':str(F(min_prefix,len(chosen))),
                        'exact_terminal':exact,'exact_prefix':prefix_exact}
        relevant_rows=[item for item in details if item['delay']==delay]
        terminal_support=[sum(bool(sum(c)) for c in item['raw_counts']) for item in relevant_rows]
        prefix_support=[item['all_prefix_support'] for item in relevant_rows]
        require([min(terminal_support),max(terminal_support)]==ref['terminal_raw_support_range'],
                'published terminal support range differs')
        require([min(prefix_support),max(prefix_support)]==ref['full_prefix_support_range'],
                'published full prefix support range differs')
        measured.append(row)
    require(hash_json(details)==reference['complete_pointer_tables_sha256'],'full pointer/prefix count fingerprint')
    for label,chosen in sectors.items():
        require(pointer_profile([f*4 for f in flags],flags,chosen)[1]==0,
                'synthetic true pointer rejected')
    return {'n':n,'background':'zero' if seed is None else seed,'deadlines':measured,
            'complete_counts_sha256':hash_json(details),'old_source_image':old_image},all_pooled,field

def mobius(table):
    # Subset inclusion inversion via paired blocks, with reverse truth check.
    output=list(table)
    stride=1
    while stride<len(output):
        for start in range(0,len(output),2*stride):
            for offset in range(stride):output[start+stride+offset]^=output[start+offset]
        stride*=2
    terms={i for i,c in enumerate(output) if c}
    for x,answer in enumerate(table):
        require(answer==(sum(1 for term in terms if term&x==term)%2),'polynomial inverse truth check')
    return terms

def named(terms,names):
    return ['*'.join(names[i] for i in range(len(names)) if term&(1<<i)) or '1' for term in sorted(terms)]

def algebra_check(zero_field,reference):
    v=zero_field(2,ORIGIN)
    q8=zero_field(1,Q8);q10=zero_field(1,Q10);m=zero_field(1,MASK)
    original_tables=[[0]*4096 for _ in range(3)]
    logical_d=[None]*4096
    nonlinear_count=oldlocal_count=0
    linear,_=forward(1,None,nonlinear=False)
    without_old,_=forward(1,None,oldlocal=False)
    for lane,(p,x,y,g) in enumerate(PAYLOADS):
        bits=[(z>>(2-k))&1 for z in (p,x,y,g) for k in range(3)]
        pa,pb,pd,xa,xb,xd,ya,yb,yd,ga,gb,gd=bits
        j=ga^(pb*gd)^(pd*gb)^(xb*yd)^(yb*xd)^(gb*(xd^yd))^(gd*(xb^yb))^(gb*gd)
        formula=4*(pa^gd)+2*(pb^j)+(pd^gb^(gd*j))
        require(formula==v[lane],'original-payload native polynomial')
        mask=sum(z<<i for i,z in enumerate(bits))
        for k in range(3):original_tables[k][mask]=(v[lane]>>(2-k))&1
        logical_bits=[(z>>(2-k))&1 for z in (p,q8[lane],q10[lane],m[lane]) for k in range(3)]
        logical_mask=sum(z<<i for i,z in enumerate(logical_bits))
        require(logical_d[logical_mask] is None,'logical native table collision')
        logical_d[logical_mask]=v[lane]&1
        if p in (1,3):
            e=q8[lane]//4^q10[lane]//4^m[lane]//4
            b=(q8[lane]//2)%2^(q10[lane]//2)%2^(m[lane]//2)%2
            d=q8[lane]%2^q10[lane]%2^m[lane]%2
            s=(p//2)%2
            require(v[lane]==4*(b^1)+2*d+(1^e^d^(b*d)^(s*b)),
                    'actual prepared logical-pool native polynomial')
        nonlinear_count+=v[lane]!=linear(2,ORIGIN)[lane]
        oldlocal_count+=v[lane]!=without_old(2,ORIGIN)[lane]
    original_terms=[mobius(t) for t in original_tables]
    names=reference['native_two_tick_variables']
    require({k:named(t,names) for k,t in zip(('A','B','D'),original_terms)}==reference['native_two_tick_ANF'],
            'native original ANF differs')
    logical_terms=mobius(logical_d)
    prepared=set()
    for term in logical_terms:
        if term&1:continue
        t=term&~4
        prepared.symmetric_difference_update({t})
    require(named(prepared,reference['native_logical_basis_variables'])==reference['native_prepared_P_0_s_1_D_ANF'],
            'native logical prepared ANF differs')
    products=[t for t in prepared if t&2 and t!=2]
    require(set(named(products,reference['native_logical_basis_variables']))=={'s*q8B','s*q10B','s*mB'},
            'actual logical X/pool interaction products')
    logical=[]
    for x in range(128):
        b=[(x>>i)&1 for i in range(7)]
        logical.append(decode_flag(2*b[0],4*b[1]+2*b[2]+b[3],4*b[4]+2*b[5]+b[6]))
    terms=mobius(logical)
    require(named(terms,reference['logical_variables'])==reference['logical_A_ANF'],'acceptance ANF differs')
    phase=[]
    for x in range(2048):
        b=[(x>>i)&1 for i in range(11)]
        s=b[0]^b[3]^b[6]^b[7]^b[8]^b[9]^b[10]
        phase.append(decode_flag(2*s,4*b[1]+2*b[2]+b[3],4*b[4]+2*b[5]+b[6]))
    phase_terms=mobius(phase)
    require(max(t.bit_count() for t in terms)==4 and len(terms)==28,'logical degree/count')
    require(max(t.bit_count() for t in phase_terms)==4 and len(phase_terms)==72,'phase degree/count')
    require(nonlinear_count==reference['nonlinear_term_removed_changed_worlds'] and
            oldlocal_count==reference['old_local_term_removed_changed_worlds'],'native mutant counts differ')
    return {'original_payload_worlds':4096,'original_coordinate_ANF_term_counts':[len(z) for z in original_terms],
            'original_coordinate_ANF_degrees':[max(t.bit_count() for t in z) for z in original_terms],
            'logical_A_term_count':len(terms),'logical_A_degree':4,
            'substituted_phase_term_count':len(phase_terms),'substituted_phase_degree':4,
            'native_logical_prepared_D_terms':len(prepared),
            'native_old_X_pool_products':sorted(named(products,reference['native_logical_basis_variables'])),
            'nonlinear_removed_changed_worlds':nonlinear_count,'oldlocal_removed_changed_worlds':oldlocal_count}

def main():
    here=Path(__file__).resolve().parent
    default_author=here.parent if (here.parent/'PLAN.md').is_file() else here.parent/'native_gate_v13'
    parser=argparse.ArgumentParser()
    parser.add_argument('--author-root',type=Path,default=default_author)
    args=parser.parse_args()
    pins=json.loads((Path(__file__).with_name('INPUT-HASHES.json')).read_text())
    for row in pins['files']:
        b=(args.author_root/row['name']).read_bytes()
        sha=hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
        require(sha==row['git_blob'] and len(b)==row['bytes'],'pinned Git input mismatch: '+row['name'])
    author=json.loads((args.author_root/'result.json').read_text())
    review=[];pooled=defaultdict(Counter);zero_field=None
    configs=[(n,s) for n in (1,2,3) for s in (0,3)]+[(1,None)]
    for reference,(n,seed) in zip(author['families'],configs):
        require(reference['n']==n and reference['background']==('zero' if seed is None else seed),'family ordering')
        data,counts,field=one_family(n,seed,reference)
        review.append(data)
        for delay,site,matrix in counts:
            for raw in range(8):
                for flag in range(2):pooled[delay,site][raw,flag]+=matrix[raw][flag]
        if seed is None:zero_field=field
    pooled_summary=[]
    for delay in (1,2,3):
        all_errors=[]
        for site in SITES:
            c=pooled[delay,site]
            bayes=sum(min(c[v,0],c[v,1]) for v in range(8))
            exhaust=min(sum(c[v,1-((f>>v)&1)] for v in range(8)) for f in range(256))
            require(bayes==exhaust,'pooled direct readout mismatch')
            all_errors.append(F(bayes,7*4096))
        require(min(all_errors)==F(author['pooled_common_readout'][delay-1]['minimum_common_terminal_error']),
                'pooled minimum differs')
        pooled_summary.append(str(min(all_errors)))
    algebra=algebra_check(zero_field,author['algebra'])
    report={'schema':'native-gate-v13-independent-review-1','author_commit':pins['author_commit'],
            'verdict':'ACCEPT_WITHIN_STATED_SCOPE','review_level':'separate-agent internal',
            'pinned_git_blobs_verified':len(pins['files']),
            'author_engine_imported':False,'engine':'independent iterative forward shrinking cones with4096-bit columns',
            'families':review,'all_source_worlds':7*4096,
            'terminal_pointer_cases':7*25*3,'full_prefix_cases':7*25*3,
            'old_P_sectors_per_case':2,'readout_functions_per_terminal_case_and_sector':256,
            'full_pointer_and_prefix_count_fingerprints_match':True,
            'source_triangle_old_input_sectors':56,
            'pooled_common_readout_minima':pooled_summary,'algebra':algebra,
            'huge_L_or_universal_no_go_claimed':False,'native_observer_access_adopted':False,
            'all_required_controls_pass':True}
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__':main()
