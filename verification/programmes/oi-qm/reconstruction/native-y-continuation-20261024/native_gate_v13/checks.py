"""Bounded original-time native gate/pointer audit; no author-engine imports."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
import hashlib
from itertools import product
import json
from pathlib import Path

STEPS=((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1))
CENTER=(0,0,0)
POSITIONS=sorted(p for p in product(range(-2,3),repeat=3) if sum(map(abs,p))<=2)
ROWS=list(product(range(8),repeat=4))
FULL=(1<<len(ROWS))-1


def need(ok,message):
    if not ok:
        raise RuntimeError(message)


def ratio(a,b):
    return str(Fraction(a,b))


def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def h(x):
    a,b,d=(x>>2)&1,(x>>1)&1,x&1
    return (b<<2)|(d<<1)|(a^(b&d))


def bg(seed,t,p):
    if seed is None:
        return 0
    x,y,z=p
    return ((x*x+3*y*y+7*z+13*t+seed)^(x*y+z*z+11*seed*t))&7


def source_positions(n):
    return [(-(n-1),0,0),(-n,0,-1),(-n,0,1),(-n-1,0,0)]


def packed(n,seed,nonlinear=True,oldlocal=True):
    points=source_positions(n)
    initial={p:tuple(sum(((row[j]>>(2-k))&1)<<i for i,row in enumerate(ROWS))
                     for k in range(3)) for j,p in enumerate(points)}
    @lru_cache(None)
    def get(t,p):
        if t==0 and p in initial:
            return initial[p]
        if t in (-1,0):
            val=bg(seed,t,p)
            return tuple(FULL if (val>>(2-k))&1 else 0 for k in range(3))
        acc=[0,0,0]
        for step in STEPS:
            q=tuple(x+y for x,y in zip(p,step))
            val=get(t-1,q)
            for k in range(3):
                acc[k]^=val[k]
        a,b,d=acc
        out=(b,d,a^(b&d) if nonlinear else a)
        old=get(t-2,p) if oldlocal else (0,0,0)
        return tuple(x^y for x,y in zip(old,out))
    @lru_cache(None)
    def unpack(t,p):
        vals=get(t,p)
        return tuple(sum(((vals[k]>>i)&1)<<(2-k) for k in range(3)) for i in range(4096))
    return get,unpack


def scalar(n,seed,assignment,t,target):
    initial=dict(zip(source_positions(n),assignment))
    @lru_cache(None)
    def evaluate(time,p):
        if time==0 and p in initial:
            return initial[p]
        if time in (-1,0):
            return bg(seed,time,p)
        acc=0
        for step in STEPS:
            acc^=evaluate(time-1,tuple(x+y for x,y in zip(p,step)))
        return evaluate(time-2,p)^h(acc)
    return evaluate(t,target)


def event(s,q8,q10):
    y=(q8>>1)&1
    r=q10&1
    k=((q8>>2)&1)+2*(q8&1)+4*((q10>>2)&1)
    return int(k<((5,0),(4,1))[y^s][r^s])


def anf(values,names):
    coeff=list(values)
    need(len(coeff)==1<<len(names),'ANF table shape')
    for k in range(len(names)):
        for mask in range(len(coeff)):
            if mask&(1<<k):
                coeff[mask]^=coeff[mask^(1<<k)]
    terms=[mask for mask,x in enumerate(coeff) if x]
    for x,v in enumerate(values):
        need(v==sum(1 for m in terms if x&m==m)%2,'ANF reconstruction')
    return terms


def describe_terms(terms,names):
    return ['*'.join(names[i] for i in range(len(names)) if m&(1<<i)) or '1' for m in terms]


def algebra():
    names=['s','b0','b1','b2','b3','b4','b5']
    values=[]
    for x in range(128):
        b=[(x>>i)&1 for i in range(7)]
        values.append(event(b[0],4*b[1]+2*b[2]+b[3],4*b[4]+2*b[5]+b[6]))
    logical=anf(values,names)
    physical_names=['vB','q8A','q8B','q8D','q10A','q10B','q10D','mD','xpD','ymD','ypD']
    physical=[]
    for x in range(1<<len(physical_names)):
        b=[(x>>i)&1 for i in range(len(physical_names))]
        s=b[0]^b[3]^b[6]^b[7]^b[8]^b[9]^b[10]
        physical.append(event(s,4*b[1]+2*b[2]+b[3],4*b[4]+2*b[5]+b[6]))
    substituted=anf(physical,physical_names)
    need(sum(values)==40,'logical threshold mass')
    need(all(values[x]==values[x^(1<<5)] for x in range(128)),'unused Z enters flag')

    native_names=['pA','pB','pD','xA','xB','xD','yA','yB','yD','gA','gB','gD']
    _,native=packed(1,None)
    actual=native(2,CENTER)
    q8zero=native(1,(0,0,-1))
    q10zero=native(1,(0,0,1))
    mzero=native(1,(-1,0,0))
    logical_native_by_mask=[None]*4096
    _,linear=packed(1,None,nonlinear=False)
    linear_values=linear(2,CENTER)
    _,without_old=packed(1,None,oldlocal=False)
    no_old_values=without_old(2,CENTER)
    tables=[[] for _ in range(3)]
    # Our source-row convention uses integer triples MSB first. ANF input
    # convention uses names ordered by increasing subset bit. Relabel explicitly.
    native_by_mask=[0]*4096
    nonlinear_count=oldlocal_count=0
    witnesses=[]
    for lane,(p,x,y,g) in enumerate(ROWS):
        pa,pb,pd=(p>>2)&1,(p>>1)&1,p&1
        xb,xd=(x>>1)&1,x&1
        yb,yd=(y>>1)&1,y&1
        ga,gb,gd=(g>>2)&1,(g>>1)&1,g&1
        interaction=ga^(pb&gd)^(pd&gb)^(xb&yd)^(yb&xd)^(gb&(xd^yd))^(gd&(xb^yb))^(gb&gd)
        expected=((pa^gd)<<2)|((pb^interaction)<<1)|(pd^gb^(gd&interaction))
        need(actual[lane]==expected,'closed native nonlinear polynomial')
        need(linear_values[lane]==(p^((gd<<2)|(ga<<1)|gb)),'linear-rule control')
        nonlinear_count+=actual[lane]!=linear_values[lane]
        oldlocal_count+=actual[lane]!=no_old_values[lane]
        bits=[(v>>(2-k))&1 for v in (p,x,y,g) for k in range(3)]
        mask=sum(bit<<i for i,bit in enumerate(bits))
        native_by_mask[mask]=actual[lane]
        logical_bits=[(v>>(2-k))&1 for v in (p,q8zero[lane],q10zero[lane],mzero[lane]) for k in range(3)]
        logical_mask=sum(bit<<i for i,bit in enumerate(logical_bits))
        need(logical_native_by_mask[logical_mask] is None,'logical source map not bijective')
        logical_native_by_mask[logical_mask]=actual[lane]
        if actual[lane]!=linear_values[lane] and len(witnesses)<2:
            witnesses.append({'initial_payloads':[p,x,y,g],'native':actual[lane],'linear_mutant':linear_values[lane]})
    for x in range(4096):
        for k in range(3):
            tables[k].append((native_by_mask[x]>>(2-k))&1)
    native_terms=[anf(v,native_names) for v in tables]
    logical_native_names=['pA','s','r','q8A','q8B','q8D','q10A','q10B','q10D','mA','mB','mD']
    logical_native_terms=anf([v&1 for v in logical_native_by_mask],logical_native_names)
    # Prepared old P=(0,s,1) is an actual affine original-time input sector.
    # Substitute this restriction in the measured complete logical polynomial.
    prepared_terms=set()
    for term in logical_native_terms:
        if term&1:
            continue
        reduced=term&~4
        if reduced in prepared_terms:
            prepared_terms.remove(reduced)
        else:
            prepared_terms.add(reduced)
    prepared_terms=sorted(prepared_terms)
    s_products=[t for t in prepared_terms if t&2 and t&~2]
    need(set(describe_terms(s_products,logical_native_names))=={'s*q8B','s*q10B','s*mB'},'old-X/pool products not isolated')
    old_fresh_terms=sorted({term for terms in native_terms for term in terms
                            if term&7 and term&~7 and term.bit_count()>=2})
    need(old_fresh_terms,'no actual old/fresh nonlinear term isolated')
    need(nonlinear_count>0 and oldlocal_count>0,'native countercontrol vacuous')
    return {'logical_variables':names,'logical_A_ANF':describe_terms(logical,names),
            'logical_A_degree':max(t.bit_count() for t in logical),
            'logical_success_truth_rows':sum(values),'logical_total_truth_rows':128,
            'substituted_phase_variables':physical_names,
            'substituted_A_degree':max(t.bit_count() for t in substituted),
            'substituted_A_monomials':len(substituted),
            'substituted_truth_rows':len(physical),
            'native_two_tick_variables':native_names,
            'native_two_tick_ANF':dict(zip(['A','B','D'],[describe_terms(t,native_names) for t in native_terms])),
            'native_old_fresh_product_terms':describe_terms(old_fresh_terms,native_names),
            'native_logical_basis_variables':logical_native_names,
            'native_prepared_P_0_s_1_D_ANF':describe_terms(prepared_terms,logical_native_names),
            'native_prepared_X_pool_products':describe_terms(s_products,logical_native_names),
            'native_polynomial_worlds':4096,'nonlinear_term_removed_changed_worlds':nonlinear_count,
            'old_local_term_removed_changed_worlds':oldlocal_count,
            'nonlinear_mutant_witnesses':witnesses,
            'degree_scope':'formal diagnostics only; no actual huge-L exclusion inferred'}


def pointer_stats(raw,flags,indices,check_functions=True):
    counts=[[0,0] for _ in range(8)]
    lanes=[[None,None] for _ in range(8)]
    for i in indices:
        value,flag=raw[i],flags[i]
        counts[value][flag]+=1
        if lanes[value][flag] is None:
            lanes[value][flag]=i
    errors=sum(min(c) for c in counts)
    if check_functions:
        exhaustive=min(sum(c[1-((f>>v)&1)] for v,c in enumerate(counts)) for f in range(256))
        need(errors==exhaustive,'Bayes error/readout exhaustion disagree')
    witness=None
    for value,(i,j) in enumerate(lanes):
        if i is not None and j is not None:
            witness={'raw':value,'A0_payloads':list(ROWS[i]),'A1_payloads':list(ROWS[j])}
            break
    need((errors==0)==(witness is None),'collision decision mismatch')
    return errors,counts,witness


def family(n,seed):
    get,unpack=packed(n,seed)
    p=unpack(n-1,CENTER)
    q8=unpack(n,(0,0,-1))
    q10=unpack(n,(0,0,1))
    m=unpack(n,(-1,0,0))
    v=unpack(n+1,CENTER)
    source=source_positions(n)
    distance=lambda a,b:sum(abs(x-y) for x,y in zip(a,b))
    need(len(set(source))==4,'source collision')
    need(distance(source[0],CENTER)==n-1,'old axial source')
    need(all(distance(f,CENTER)==n+1 for f in source[1:]),'fresh reaches old input too early')
    qtargets=[(0,0,-1),(0,0,1),(-1,0,0)]
    expected=[[0,2,0],[2,0,0],[2,2,0]]
    need([[distance(f,t)-n for t in qtargets] for f in source[1:]]==expected,'fresh triangle geometry')
    old_values=[]
    for old_input in range(8):
        indices=range(old_input*512,(old_input+1)*512)
        need(len({p[i] for i in indices})==1,'old depends on fresh source')
        old_values.append(p[old_input*512])
        need(len({(q8[i],q10[i],m[i]) for i in indices})==512,'fresh triangle loses bijectivity')
        need(len({(q8[i],q10[i],v[i]) for i in indices})==512,'pool/ciphertext product fails')
    need(len(set(old_values))==8,'old source not bijective')
    flags=[event((p[i]>>1)&1,q8[i],q10[i]) for i in range(4096)]
    need(sum(flags)==1280,'flag total mass')
    valid=[i for i in range(4096) if not p[i]&4]
    need(len(valid)==2048 and sum(flags[i] for i in valid)==640,'prepared-shape flag mass')
    for i in range(4096):
        total=0
        for step in STEPS:
            total^=unpack(n,step)[i]
        need(v[i]^h(total)==p[i],'native fixed inverse fails')
    scalar_comparisons=0
    for i in (0,31,511,1279,2048,4095):
        for t,target in ((n-1,CENTER),(n,(0,0,-1)),(n,(0,0,1)),(n+3,(1,-1,0))):
            need(scalar(n,seed,ROWS[i],t,target)==unpack(t,target)[i],'scalar/packed native mismatch')
            scalar_comparisons+=1
    details=[]
    summary=[]
    all_indices=range(4096)
    for d in (1,2,3):
        minimum={'all':4097,'prepared':2049}
        best={'all':[],'prepared':[]}
        exact={'all':[],'prepared':[]}
        prefix_exact={'all':[],'prepared':[]}
        witnesses={}
        min_prefix={'all':4097,'prepared':2049}
        raw_support=[]
        prefix_support=[]
        for pos in POSITIONS:
            raw=unpack(n+d,pos)
            prefix=[tuple(unpack(t,pos)[i] for t in range(n,n+d+1)) for i in range(4096)]
            row={'position':list(pos),'delay':d,'raw_counts':None,'prepared_raw_counts':None}
            for label,indices in (('all',all_indices),('prepared',valid)):
                error,counts,witness=pointer_stats(raw,flags,indices)
                if error<minimum[label]:
                    minimum[label]=error
                    best[label]=[list(pos)]
                    witnesses[label]=witness
                elif error==minimum[label]:
                    best[label].append(list(pos))
                if error==0:
                    exact[label].append(list(pos))
                by_prefix={}
                for i in indices:
                    c=by_prefix.setdefault(prefix[i],[0,0])
                    c[flags[i]]+=1
                pe=sum(min(c) for c in by_prefix.values())
                min_prefix[label]=min(min_prefix[label],pe)
                if pe==0:
                    prefix_exact[label].append(list(pos))
                row['raw_counts' if label=='all' else 'prepared_raw_counts']=counts
                row[label+'_prefix_support']=len(by_prefix)
                row[label+'_prefix_Bayes_errors']=pe
                row[label+'_prefix_counts_sha256']=digest(sorted((list(k),v) for k,v in by_prefix.items()))
            details.append(row)
            raw_support.append(len(set(raw)))
            prefix_support.append(len(set(prefix)))
        summary.append({'delay_after_pool':d,'candidate_sites':len(POSITIONS),
                        'minimum_terminal_flag_error_all':ratio(minimum['all'],4096),
                        'minimum_terminal_flag_error_prepared':ratio(minimum['prepared'],2048),
                        'best_terminal_site_counts':{k:len(v) for k,v in best.items()},
                        'best_terminal_site_examples':{k:v[:2] for k,v in best.items()},
                        'exact_terminal_site_counts':{k:len(v) for k,v in exact.items()},
                        'exact_prefix_decoder_site_counts':{k:len(v) for k,v in prefix_exact.items()},
                        'minimum_full_prefix_flag_error_all':ratio(min_prefix['all'],4096),
                        'minimum_full_prefix_flag_error_prepared':ratio(min_prefix['prepared'],2048),
                        'best_terminal_collision_witnesses':witnesses,
                        'terminal_raw_support_range':[min(raw_support),max(raw_support)],
                        'full_prefix_support_range':[min(prefix_support),max(prefix_support)]})
    # A positive synthetic record checks that the classification can accept.
    synthetic=[2*f for f in flags]
    need(pointer_stats(synthetic,flags,range(4096))[0]==0,'synthetic true pointer rejected')
    return {'n':n,'background':'zero' if seed is None else seed,
            'initial_worlds':4096,'prepared_shape_worlds':2048,
            'source_positions':[list(x) for x in source],
            'old_source_image':old_values,'scalar_native_comparisons':scalar_comparisons,
            'source_triangle_and_pool_ciphertext_bijections':8,
            'deadlines':summary,'complete_pointer_tables_sha256':digest(details)},details


def main():
    results=[]
    details=[]
    for n,seed in [(n,s) for n in (1,2,3) for s in (0,3)]+[(1,None)]:
        data,table=family(n,seed)
        results.append(data)
        details.extend(table)
    pooled=[]
    for d in (1,2,3):
        errors=[]
        for pos in POSITIONS:
            rows=[r for r in details if r['delay']==d and r['position']==list(pos)]
            counts=[[sum(r['raw_counts'][v][a] for r in rows) for a in (0,1)] for v in range(8)]
            total=sum(map(sum,counts))
            err=sum(min(c) for c in counts)
            independent=min(sum(c[1-((f>>v)&1)] for v,c in enumerate(counts)) for f in range(256))
            need(err==independent,'pooled readout exhaustion')
            errors.append((Fraction(err,total),list(pos)))
        best=min(x[0] for x in errors)
        pooled.append({'delay_after_pool':d,'minimum_common_terminal_error':str(best),
                       'best_site_count':sum(e==best for e,p in errors),
                       'best_site_examples':[p for e,p in errors if e==best][:2]})
    result={'schema':'native-short-window-gate-v13-1',
            'scope':'seven explicit small original-time families; no actual huge-L or universal native-gate claim',
            'algebra':algebra(),'families':results,'pooled_common_readout':pooled,
            'counts':{'families':7,'complete_native_worlds':7*4096,'pointer_sites_per_deadline':len(POSITIONS),
                      'terminal_pointer_cases':7*3*len(POSITIONS),
                      'readout_functions_checked_per_case_and_sector':256,
                      'sectors':2,'scalar_independent_comparisons':7*24},
            'all_controls_passed':True}
    exact_count=sum(sum(d['exact_terminal_site_counts'].values()) for f in results for d in f['deadlines'])
    prefix_count=sum(sum(d['exact_prefix_decoder_site_counts'].values()) for f in results for d in f['deadlines'])
    result['measured_exact_terminal_cases_both_sectors']=exact_count
    result['measured_exact_prefix_cases_both_sectors']=prefix_count
    result['verdict']='NO_EXACT_SINGLE_CELL_FLAG_IN_FIXED_WINDOW' if exact_count==0 else 'BOUNDED_EXACT_READOUT_CANDIDATE_FOUND'
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':
    main()
