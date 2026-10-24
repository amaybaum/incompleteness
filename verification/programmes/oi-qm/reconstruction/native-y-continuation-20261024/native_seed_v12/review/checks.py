#!/usr/bin/env python3
"""Independent signed native evaluator and monotone origin/W front review."""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path
import argparse,hashlib,json

ROWS=tuple(product((0,1),(0,1),(0,1),(0,1),(0,1),(0,1),range(8)))
INDEX={row:i for i,row in enumerate(ROWS)}
LOW=sum(1<<(3*i) for i in range(512))
T=185; DELAY=12*840**185; S=DELAY+T; R=S+68; L=R+9; BASE=253; BUDGET=20
HSCALAR=(0,2,4,7,1,3,5,6)

def need(ok,message):
    if not ok: raise RuntimeError(message)

def pack(function): return sum(function(*row)<<(3*i) for i,row in enumerate(ROWS))
def item(value,index): return value>>(3*index)&7
def hb(value):
    return ((value&(LOW<<1))<<1)|((value&LOW)<<1)|(((value>>2)&LOW)^(((value>>1)&LOW)&value&LOW))
def hp(value,t):
    for _ in range(t%12): value=hb(value)
    return value
def xor(values):
    out=0
    for v in values: out^=v
    return out
def distance(a,b): return sum(abs(x-y) for x,y in zip(a,b))
def adjacent(p):
    for axis in range(3):
        for sign in (-1,1):
            q=list(p);q[axis]+=sign;yield tuple(q)
def ball(r,center):
    for x in range(-r,r+1):
        for y in range(-r+abs(x),r-abs(x)+1):
            for z in range(-r+abs(x)+abs(y),r-abs(x)-abs(y)+1):
                yield center[0]+x,center[1]+y,center[2]+z

UPPER={
 (0,0,0):pack(lambda x,u,my,mr,a,b,n:4*u+1),
 (0,0,-14):pack(lambda x,u,my,mr,a,b,n:5*u),
 (0,0,-16):pack(lambda x,u,my,mr,a,b,n:4*u+2*(1^u)+1),
 (0,0,-18):pack(lambda x,u,my,mr,a,b,n:4*(u^b)+2*a+(u^a)),
 (1,0,-17):pack(lambda x,u,my,mr,a,b,n:5*(a^b)),
 (-1,0,-17):pack(lambda x,u,my,mr,a,b,n:7*(a^b)),
 (0,0,-20):pack(lambda x,u,my,mr,a,b,n:n),
}

@lru_cache(None)
def short_upper(t,x,y,z):
    if t<0 or (t-x-y-z)%2: return 0
    if min(distance((x,y,z),source) for source in UPPER)>t:return 0
    if t==0:return UPPER.get((x,y,z),0)
    p=(x,y,z)
    return short_upper(t-2,*p)^hb(xor(short_upper(t-1,*q) for q in adjacent(p)))

def strip():
    data={}
    def at(ell,x,y,n):
        radius=abs(x)+abs(y)
        if ell<0 or radius>ell or (ell-radius)%2 or ell+radius>BUDGET:return 0
        return data[ell,x,y][n]
    for ell in range(BUDGET+1):
        for x in range(-ell,ell+1):
            for y in range(-ell+abs(x),ell-abs(x)+1):
                if (ell-abs(x)-abs(y))%2 or ell+abs(x)+abs(y)>BUDGET:continue
                values=[short_upper(ell,x,y,0)];data[ell,x,y]=values
                for n in range(1,BASE+(BUDGET-ell)//2+1):
                    forced=at(ell-2,x,y,n+1)^at(ell-1,x-1,y,n)^at(ell-1,x+1,y,n)^at(ell-1,x,y-1,n)^at(ell-1,x,y+1,n)
                    values.append(at(ell-2,x,y,n)^hb(values[-1]^forced))
    checks=0
    for (ell,x,y),values in data.items():
        for n in (1,2):
            need(values[n]==short_upper(n+ell,x,y,n),'signed full-x/full-y native strip')
            checks+=1
    return data,checks

ORIGIN=pack(lambda x,u,my,mr,a,b,n:2*x)
WVALUE=7*LOW

def monotone_front(gap,last_y,max_ell,origin,wvalue,operation):
    data={}
    for y in range(-gap,last_y+1):
        for z in range(gap+max_ell+1):
            if y+z<0:continue
            if y+z==0:
                value=origin if (y,z)==(0,0) else wvalue if (y,z)==(-gap,gap) else 0
            else:value=operation(data.get((y-1,z),0)^data.get((y,z-1),0))
            data[y,z]=value
    return data

def lower_front():
    grid=monotone_front(76,176,2,ORIGIN,WVALUE,hb)
    layers=[hb(hp(ORIGIN,75)^hp(WVALUE,75))]
    layers.extend((hb(layers[0]),hb(hb(layers[0]))))
    checks=0
    for j in range(177):
        if j:
            layers[0]=hb(layers[0]^(hp(ORIGIN,j+75) if j&75==0 else 0))
            layers[1]=hb(layers[1]^layers[0]);layers[2]=hb(layers[2]^layers[1])
        for ell in range(3):
            need(layers[ell]==grid[j,76+ell],'actual-gap independent monotone lower front')
            checks+=1
    scalar_controls=0
    for x in (0,1):
        small=monotone_front(4,4,2,2*x,7,lambda v:HSCALAR[v])
        previous={};current={p:v for p,v in (((0,0,0),2*x),((0,-4,4),7)) if v}
        histories=[current]
        for time in range(1,11):
            points=set(previous)
            for p in current:points.update(adjacent(p))
            out={}
            for p in points:
                value=previous.get(p,0)^HSCALAR[xor(current.get(q,0) for q in adjacent(p))]
                if value:out[p]=value
            histories.append(out);previous,current=current,out
        for j,ell in product(range(5),range(3)):
            need(histories[j+4+ell].get((0,j,4+ell),0)==small[j,4+ell],
                 'unreflected six-neighbor scalar lower-front control')
            scalar_controls+=1
    return grid,checks,scalar_controls

CONTROLS=((0,-S,-68),(0,S,-68),(T,DELAY,-68),(-T,DELAY,-68))
PAYLOADS=(ORIGIN,pack(lambda x,u,my,mr,a,b,n:2*(my^mr)),
          pack(lambda x,u,my,mr,a,b,n:2*my),pack(lambda x,u,my,mr,a,b,n:2*mr))
ENTRIES={(0,-9,8):(176,0),(0,-10,9):(175,1),(0,-11,10):(174,2)}

def native_kernel(data,lower,drop_layer=None):
    def upper(time,p):
        x,y,z=p;n=R-z;ell=time-n;rad=abs(x)+abs(y)
        if ell<0 or rad>ell or (ell-rad)%2:return 0
        need(ell+rad<=BUDGET,'upper signed budget coverage')
        return data[ell,x,y][n-DELAY]
    def baseline(time,p):
        up=upper(time,p);terms=[]
        for source,payload in zip(CONTROLS,PAYLOADS):
            delta=tuple(abs(a-b) for a,b in zip(source,p));term=0
            if sum(delta)<=time:
                need(sum(delta)==time,'old lower wave only first front')
                if not ((delta[0]&delta[1])|(delta[0]&delta[2])|(delta[1]&delta[2])):
                    term=hp(payload,time)
            terms.append(term)
        if time==R-1 and p in ENTRIES:
            need(up==0 and not xor(terms[1:]),'W entry has no upper/selector background')
            j,ell=ENTRIES[p]
            if drop_layer=='all' or ell==drop_layer:return terms[0]
            return lower[j,76+ell]
        return up^xor(terms)
    target=(0,0,10)
    old={p:baseline(R-2,p) for p in ball(10,target)}
    now={p:baseline(R-1,p) for p in ball(11,target)}
    records={}
    for offset in range(11):
        new={p:old[p]^hb(xor(now[q] for q in adjacent(p))) for p in ball(10-offset,target)}
        records[offset]=new;old,now=now,new
    return tuple(item(now[target],i) for i in range(512)),records

def geometry(source_root):
    q=(0,S,78);source=(0,S,S+156);deadline=L+1
    need(distance(source,q)==deadline,'N current first arrival')
    need(distance(source,(0,S,77))==L+2 and distance(source,(0,S,76))==L+3,'old q9/q8 preserved causally')
    old_sources=json.loads((source_root/'parallel_v3/history_control/SOURCE-GEOMETRY.json').read_text())['sources']
    need(len(old_sources)==1479,'compiled source inventory')
    need(all(distance(tuple(row['position']),q)>=deadline for row in old_sources),'new zero pins retain old source exceptions')
    need(all(tuple(row['position'])!=source for row in old_sources),'new source does not overwrite compiled source')
    ports=((0,T,0),(0,0,-8*T),(T,DELAY,0),(-T,DELAY,0),(4*T,DELAY,0),(0,S,0),(12*R,0,0),(48*L,0,0))
    times=(T,T,S,S,S,S,R,L)
    ready=list(zip(ports,times))+[((T,0,0),T),((-T,0,0),T),((4*T,0,0),T),((0,S,-68),R),((-12*R,0,0),R)]
    ready += [((0,S,68+k),R+k) for k in range(10)]+[((-48*L,0,0),L)]
    need(all(distance(source,c)>r for c,r in ready),'all previous ready prescriptions exclude N')
    directions=((0,-1,0),(0,0,-1),(0,1,0),(0,1,0),(0,1,0),(0,1,0),(-1,0,0),(1,0,0))
    slacks=[]
    for port,direction,start in zip(ports,directions,times):
        axis=next(i for i,d in enumerate(direction) if d)
        lo,hi=start+1,deadline
        ideal=(q[axis]-port[axis])*direction[axis]
        closest=max(lo,min(hi,ideal))
        point=tuple(port[i]+closest*direction[i] for i in range(3))
        slack=distance(point,q)-deadline
        need(slack>0,'entire bank interval excludes new ready cone')
        need(point!=source,'new source not a reserved bank coordinate')
        slacks.append(slack)
    need(min(slacks)==1,'bank boundary control')
    need(distance((-(L+1),S,76),q)==deadline+2,'F8 factor preserved')
    need(distance((-(L+1),S,78),q)==deadline,'F10 optional factor replaced')
    need(min(distance(source,p) for p in ports)>L,'old public prefix N-causal exclusion')
    entries=[]
    for time,radius in ((R-2,10),(R-1,11)):
        for p in ball(radius,(0,0,10)):
            absolute=(p[0],S+p[1],68+p[2])
            if distance((0,-76,76),absolute)<=time:entries.append((time-R,p))
    need(set(entries)=={(-1,p) for p in ENTRIES},'exact three W-front entries and no old-slice entry')
    upper_absolute=[(x,S+y,S+136-z) for x,y,z in UPPER]
    lower_absolute=[(x,S+y,68+z) for x,y,z in CONTROLS]+[(0,-76,76)]
    separation=min(distance(a,b) for a in upper_absolute for b in lower_absolute)
    need(separation>=2*R,'upper/lower pre-collision separation')
    half=(256*L+64*T)//2
    need(half>50*L+1,'retained remote/source horizon does not wrap')
    return {'compiled_sources':1479,'earlier_ready_regions':len(ready),'bank_ray_intervals':8,
            'minimum_bank_slack':1,'W_front_entries':len(entries),'upper_lower_minimum_separation_minus_2R':separation-2*R}

def audit_table(table):
    def at(x,u,my,mr,a,b,n):return table[INDEX[x,u,my,mr,a,b,n]]
    permutations=0
    for context in product((0,1),repeat=6):
        need(sorted(at(*context,n) for n in range(8))==list(range(8)),'own N permutation')
        permutations+=1
    padpairs=0
    for x,u,my,n in product((0,1),(0,1),(0,1),range(8)):
        need((at(x,u,my,0,1,0,n)^at(x,u,my,1,1,0,n))&2==2,'old mR toggles current B')
        padpairs+=1
    contexts=[k for k in product((0,1),repeat=5) if (k[3],k[4])!=(0,1)]
    common=None;sizes=[];derivatives=0
    for u,my,mr,a,b in contexts:
        pairs=set()
        for n in range(8):
            pair=(at(u^a,u,my,mr,a,b,n),at(1^u^a,u,my,mr,a,b,n))
            need((pair[0]>>2)^(pair[1]>>2)==u,'unknown sign derivative in A')
            derivatives+=1
            if pair[0]!=pair[1]:pairs.add(pair)
        common=pairs if common is None else common&pairs;sizes.append(len(common))
    need(not common and sizes[2]==0,'arbitrary known-context common-pair intersection')
    lost=0
    for my,mr,n in product((0,1),(0,1),range(8)):
        zero=at(1,0,my,mr,1,1,n);one=at(0,0,my,mr,1,1,n)
        need(zero==one==(4,2,1,0,3,5,6,7)[n],'current-only accepted sign-loss branch')
        lost+=1
    family_survivors=[]
    for extended in (False,True):
        survivors=[];count=0
        for B,C,V in product(range(8) if extended else (0,),range(8),range(8)):
            codes={(s,c):set() for s,c in product((0,1),repeat=2)}
            for u,my,mr,a,b in contexts:
                for s,c in product((0,1),repeat=2):
                    n=(B if u^a else 0)^(C if a^b else 0)^(V if c else 0)
                    codes[s,c].add(at(s^u^a,u,my,mr,a,b,n))
            if all(len(v)==1 for v in codes.values()) and all(codes[0,c]!=codes[1,c] for c in (0,1)):
                survivors.append((B,C,V))
            count+=1
        need(not survivors,'affine family survivor countercontrol')
        family_survivors.append({'tested':count,'common_injective_s_codes':len(survivors)})
    pad_rows=sum(at(x,u,my,mr,a,b,n)!=at(x,u,0,0,a,b,n) for x,u,my,mr,a,b,n in ROWS)
    accepted_pad_rows=sum(at(x,u,my,mr,a,b,n)!=at(x,u,0,0,a,b,n)
                          for x,u,my,mr,a,b,n in ROWS if (a,b)!=(0,1))
    need(pad_rows==144 and accepted_pad_rows==80,'retained pad dependency counts')
    return {'own_N_permutation_contexts':permutations,'pad_flip_pairs':padpairs,
            'accepted_derivative_pairs':derivatives,'accepted_sign_loss_pairs':lost,
            'known_contexts':len(contexts),'pair_intersection_prefix_sizes':sizes,
            'affine_families':family_survivors,'pad_sensitive_rows':pad_rows,
            'accepted_pad_sensitive_rows':accepted_pad_rows}

def main():
    here=Path(__file__).resolve().parent
    default_source=next((p for p in here.parents if (p/'parallel_v3').is_dir()),here.parent/'checkpoint_v11')
    default_author=here.parent if here.parent.name=='native_seed_v12' else here.parent/'native_seed_v12'
    parser=argparse.ArgumentParser()
    parser.add_argument('--source-root',type=Path,default=default_source)
    parser.add_argument('--author-root',type=Path,default=default_author)
    args=parser.parse_args()
    pins=json.loads((here/'INPUT-HASHES.json').read_text())
    for name,digest in pins['author_sha256'].items():
        need(hashlib.sha256((args.author_root/name).read_bytes()).hexdigest()==digest,'pinned author '+name)
    for name,digest in pins['inherited_sha256'].items():
        need(hashlib.sha256((args.source_root/name).read_bytes()).hexdigest()==digest,'pinned inherited '+name)
    for value in range(8):
        state=value
        for _ in range(12):state=HSCALAR[state]
        need(state==value,'native H exponent twelve')
        packed=value*LOW
        need(hb(packed)==HSCALAR[value]*LOW,'independent interleaved bit lanes')
    need(DELAY%(12*840**20)==0,'actual upper period divisibility')
    need(DELAY%(384*840**3)==0,'actual lower period divisibility')
    geo=geometry(args.source_root)
    data,upper_checks=strip()
    need(all(values==data[ell,x,-y] for (ell,x,y),values in data.items()),'unfolded y reflection control')
    broken_x=sum(values[0]!=data[ell,-x,y][0] for (ell,x,y),values in data.items())
    need(broken_x>0,'incorrect x reflection mutant is detectable')
    lower,lower_checks,scalar_controls=lower_front()
    table,records=native_kernel(data,lower)
    retained=json.loads((args.author_root/'result.json').read_text())
    encoded=''.join(format(value,'x') for value in table)
    need(encoded==retained['q10_table_hex'],'all512 independently derived native q10 rows')
    source_table=json.loads((args.source_root/'branch_v10/local-controller/symmetric-result.json').read_text())['q9_table_hex']
    preserved=0
    for i,(x,u,my,mr,a,b,n) in enumerate(ROWS):
        need(item(records[0][0,0,0],i)==4*x+2+(x^u),'old qY')
        need(item(records[7][0,0,7],i)==x^u,'old q7')
        need(item(records[8][0,0,8],i)==2*(x^u),'old q8')
        index=0
        for value,size in zip((x,u,my,mr,a,b,4,5,7),(2,2,2,2,2,2,8,8,8)):index=index*size+value
        need(item(records[9][0,0,9],i)==int(source_table[index],16),'old q9 including raw failures')
        preserved+=1
    damaged,_=native_kernel(data,lower,drop_layer=2)
    third_layer_mismatches=sum(a!=b for a,b in zip(table,damaged))
    need(third_layer_mismatches==0 and lower[174,78]==0,'third entry vanishes in this candidate')
    no_w,_=native_kernel(data,lower,drop_layer='all')
    all_w_mismatches=sum(a!=b for a,b in zip(table,no_w))
    need(all_w_mismatches>0,'coupled W background omission is nonvacuous')
    facts=audit_table(table)
    need(facts['pair_intersection_prefix_sizes']==retained['pad_aware_single_N']['pair_intersection_sizes_after_context'],
         'retained arbitrary known-seed intersection')
    print(json.dumps({'schema':'oi-native-seed-v12-review-1','author_commit':'1c91d3158e13eaa69c7fd1710932c9995d0288d7',
        'verdict':'ACCEPT_WITHIN_SCOPE','blockers':[],'all_controls_pass':True,
        'signed_upper_nodes':len(data),'independent_upper_packed_native_checks':upper_checks,
        'upper_distinct_parameter_assignments_per_packed_check':64,
        'broken_x_reflection_witnesses':broken_x,'actual_gap76_lower_front_checks':lower_checks,
        'small_full_3D_lower_controls':scalar_controls,'independent_q10_rows':len(table),
        'q10_table_sha256':hashlib.sha256(encoded.encode()).hexdigest(),
        'old_qY_q7_q8_q9_preserved_rows':preserved,'third_lower_layer_omission_q10_mismatches':third_layer_mismatches,
        'all_coupled_W_entries_omission_q10_mismatches':all_w_mismatches,
        'geometry':geo,'table_obstructions':facts,
        'complete_public_history_equality_claimed':False,'native_instrument_or_full_boundary_no_go_claimed':False},
        indent=2,sort_keys=True))

if __name__=='__main__':main()
