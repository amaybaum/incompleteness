#!/usr/bin/env python3
"""Exact native coupled-pool controls; no author imports."""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
import json

H=(0,2,4,7,1,3,5,6)
P=(0,0,0); Q8=(0,0,-1); Q10=(0,0,1); M=(-1,0,0)
F8=(-1,0,-1); F10=(-1,0,1); F9=(-2,0,0)
OTHER=((1,0,0),(0,1,0),(0,-1,0))
N={(0,0):5,(0,1):0,(1,0):4,(1,1):1}

def need(value,message):
    if not value: raise RuntimeError(message)

def bit(value,index): return value>>(2-index)&1

def neighbors(point):
    for a in range(3):
        for d in (-1,1):
            q=list(point); q[a]+=d; yield tuple(q)

def step(previous,current):
    points=set(previous)
    for point in current: points.update(neighbors(point))
    out={}
    for point in points:
        parity=0
        for q in neighbors(point): parity^=current.get(q,0)
        value=previous.get(point,0)^H[parity]
        if value: out[point]=value
    return out

def selected(old,q,t): return bit(old,1),bit(q,1),bit(t,2),bit(t,1)

def accept(j,q,t):
    s,y,r,z=j
    k=bit(q,0)+2*bit(q,2)+4*bit(t,0)
    return int(k<N[y^s,r^s])

def target(s,a):
    return {(s,s^y,s^r,z):F(n if a else 8-n,64)
            for (y,r),n in N.items() for z in (0,1)}

def moments(law):
    return (sum(law.values(),F()),*(sum((w*(1-2*j[i]) for j,w in law.items()),F()) for i in (0,1,3)))

def determinant(v): return (v[0]**2-sum(x*x for x in v[1:]))/4

def normalize(law):
    mass=sum(law.values(),F()); need(mass>0,'zero posterior')
    return {key:value/mass for key,value in law.items()}

def tv(a,b): return sum((abs(a.get(k,0)-b.get(k,0)) for k in a.keys()|b.keys()),F())/2

NATIVE_B_Q10_HEX='25176304741302651340256742103567251763045620314731720654421035672517630474130265134025674210356725176304562031473172065442103567276043514036275112367045213564072760435140362751210453672135640727604351364051277540163221356407276043513640512757632401213564070634512756203147317206544210356706345127741302651340256742103567063451275620314731720654421035670634512774130265134025674210356740172536157263047540163257420361401725361572630457632401574203614017253672150463123670455742036140172536721504632104536757420361'

def main():
    for value in range(8):
        a,b,d=(bit(value,i) for i in range(3))
        need(H[value]==4*b+2*d+(a^(b&d)),'Boolean H control')
    repaired=defaultdict(list); base=defaultdict(list); worlds=0
    for old,left,right,mask in product(range(8),repeat=4):
        initial={p:v for p,v in ((P,old),(F8,left),(F10,right),(F9,mask)) if v}
        first=step({},initial); second=step(initial,first)
        q,t,m=(first.get(p,0) for p in (Q8,Q10,M)); raw=second.get(P,0)
        need((q,t,m)==(H[old^left],H[old^right],H[old^left^right^mask]),'actual source response')
        need(all(first.get(p,0)==H[old] for p in OTHER),'other three dirty neighbors')
        need(raw==old^H[q^t^m^H[old]],'native full joint gate')
        parity=0
        for p in neighbors(P): parity^=first.get(p,0)
        recovered=raw^H[parity]; need(recovered==old,'fixed seven-site inverse')
        j=selected(recovered,q,t)
        repaired[old].append((q,t,m,raw,j,mask))
        if mask==0:
            polar=(bit(left,1)&bit(right,2))^(bit(right,1)&bit(left,2))
            need(raw==old^(2*polar),'bilinear finite difference')
            base[old].append((q,t,m,raw,j))
        worlds+=1
    pair_controls=0; bad=[]
    for old,rows in base.items():
        triple=Counter(row[:3] for row in rows)
        need(len(triple)==64 and set(triple.values())=={1},'base triple support')
        for a,b in ((0,1),(0,2),(1,2)):
            pairs=Counter((row[a],row[b]) for row in rows)
            need(len(pairs)==64 and set(pairs.values())=={1},'pairwise freshness')
            pair_controls+=1
        actual={k:F(v,64) for k,v in triple.items()}
        need(tv(actual,{k:F(1,512) for k in product(range(8),repeat=3)})==F(7,8),'triple dependence')
        raw={k:F(v,64) for k,v in Counter(row[3] for row in rows).items()}
        need(raw=={old:F(5,8),old^2:F(3,8)},'base raw gate law')
        need(tv(raw,{k:F(1,8) for k in range(8)})==F(3,4),'missing-neighbor mutant')
        if bit(old,0)==0:
            pooled=defaultdict(F); post=defaultdict(lambda:defaultdict(F))
            for q,t,m,raw,j in rows:
                if accept(j,q,t): pooled[j]+=F(1,64); post[raw][j]+=F(1,64)
            need(pooled=={j:w for j,w in target(bit(old,1),1).items() if w},'base pooled target')
            for raw,law in sorted(post.items()):
                det=determinant(moments(normalize(law))); need(det<0,'raw port leakage')
                bad.append({'s':bit(old,1),'old_R':bit(old,2),'raw':raw,
                            'mass_given_accept':str(sum(law.values())/F(5,16)),
                            'determinant':str(det)})
    success=failure=rejectcells=flagcases=recordcells=0
    for old,rows in repaired.items():
        triples=Counter(row[:3] for row in rows)
        need(len(triples)==512 and set(triples.values())=={1},'F9 triangular bijection')
        pairs=Counter((q,t,raw) for q,t,m,raw,j,mask in rows)
        need(len(pairs)==512 and set(pairs.values())=={1},'full raw/pool independence')
        for complement in range(8):
            counts=Counter((q,t,old^H[q^t^m^complement]) for q,t,m in triples)
            need(len(counts)==512 and set(counts.values())=={1},'arbitrary complement joint uniformity')
        if bit(old,0): continue
        s=bit(old,1); joint=defaultdict(F)
        for q,t,m,raw,j,mask in rows: joint[accept(j,q,t),raw,j]+=F(1,512)
        for raw in range(8):
            laws=[]
            for a in (0,1):
                law={}
                for j,weight in target(s,a).items():
                    actual=joint.get((a,raw,j),F()); need(actual==weight/8,'complete raw/flag/carrier law')
                    law[j]=actual
                    if not a: rejectcells+=int(actual>0)
                laws.append(law)
            need(sum(laws[0].values())==F(11,128) and sum(laws[1].values())==F(5,128),'retained failure mass')
            vec=moments(normalize(laws[1]))
            need(vec==(1,1-2*s,0,0) and determinant(vec)==0,'positive state per whole raw record')
            success+=1; failure+=1
        for oldflag in (0,1):
            records=Counter(); offer=F()
            for q,t,m,raw,j,mask in rows:
                a=accept(j,q,t); outgoing=j if oldflag and a else None
                records[oldflag,a,raw,outgoing is not None]+=1
                offer+=F(int(outgoing is not None),512)
                if not oldflag: need(outgoing is None,'previous failure resurrected')
            need(offer==(F(5,16) if oldflag else 0) and sum(records.values())==512,'full flag convention')
            flagcases+=1; recordcells+=len(records)
    best=min(F(mask.bit_count(),8)*F(11,16)+F(8-mask.bit_count(),8)*F(5,16) for mask in range(256))
    need(best==F(5,16),'masked raw port is not physical acceptance')
    best_marginal=min(abs(F(k,8)-F(5,16)) for k in range(9))
    need(best_marginal==F(1,16),'flag marginal-only countercontrol')
    for s in (0,1):
        proper=normalize(target(s,1))
        independent={(s,s^a,s^b,z):F(1,8) for a,b,z in product((0,1),repeat=3)}
        need(tv(proper,independent)==F(2,5),'independent flag carrier defect')
        intended=defaultdict(F); fake=defaultdict(F)
        for raw in range(8):
            intended[0,raw,None]=fake[0,raw,None]=F(11,128)
            for j,p in proper.items(): intended[1,raw,j[2]]+=F(5,128)*p
            for j,p in independent.items(): fake[1,raw,j[2]]+=F(5,128)*p
        need(tv(intended,fake)==F(1,8),'flag-only full terminal-R law defect')
    def native_b(x,u,my,mr,a,b,n):
        index=((((((x*2+u)*2+my)*2+mr)*2+a)*2+b)*8+n)
        return int(NATIVE_B_Q10_HEX[index],16)
    native_b_permutations=0
    for context in product((0,1),repeat=6):
        need({native_b(*context,n) for n in range(8)}==set(range(8)),'nativeB source permutation')
        native_b_permutations+=1
    native_b_witness=[native_b(0,0,my,mr,1,0,0) for my,mr in product((0,1),repeat=2)]
    need(native_b_witness==[1,3,1,3],'nativeB selected-boundary witness')
    native_b_pad_rows=sum(native_b(x,u,my,mr,a,b,n)!=native_b(x,u,0,0,a,b,n)
                         for x,u,my,mr,a,b in product((0,1),repeat=6) for n in range(8))
    need(native_b_pad_rows==144,'nativeB omitted-pad dependency')
    native_b_sign_pairs=0
    for my,mr in product((0,1),repeat=2):
        for n in range(8):
            need(native_b(0,0,my,mr,1,1,n)==native_b(1,0,my,mr,1,1,n),
                 'nativeB current q10 cannot carry s on this branch')
            need(native_b(0,0,my,mr,1,1,n)==(4,2,1,0,3,5,6,7)[n],
                 'nativeB identical sign-fibre permutation')
            native_b_sign_pairs+=1
    print(json.dumps({'schema':'oi-coupled-native-pool-composition-v5.1',
        'scope':'source-reachable n=1 controls and conditional actual-phase F9 kernel',
        'actual_astronomical_stage_simulated':False,'physical_acceptance_computed':False,
        'full_two_tick_source_worlds':worlds,'fixed_seven_site_inverse_cases':worlds,
        'base_pairwise_independence_controls':pair_controls,'base_triple_vs_product_tv':'7/8',
        'base_raw_vs_missing_neighbor_tv':'3/4','base_accepted_raw_nonpositive_branches':bad,
        'F9_bijection_worlds_per_old_triple':512,'F9_success_raw_record_branches':success,
        'F9_failure_raw_record_branches':failure,'F9_rejected_selected_physical_cells':rejectcells,
        'F9_old_flag_cases':flagcases,'F9_full_flag_raw_record_cells':recordcells,
        'F9_success_posterior_determinant':'0','F9_raw_port_best_boolean_acceptance_error':str(best),
        'F9_raw_port_best_marginal_acceptance_error':str(best_marginal),
        'independent_flag_full_offered_carrier_tv':'1/8',
        'independent_flag_conditional_carrier_tv':'2/5',
        'native_B_input_table_rows':len(NATIVE_B_Q10_HEX),
        'native_B_fixed_context_source_permutations':native_b_permutations,
        'native_B_pad_witness':native_b_witness,'native_B_pad_sensitive_rows':native_b_pad_rows,
        'native_B_opposite_sign_identical_current_port_pairs':native_b_sign_pairs,
        'native_B_complete_public_history_equality_claimed':False,
        'all_controls_pass':True},indent=2,sort_keys=True))

if __name__=='__main__': main()
