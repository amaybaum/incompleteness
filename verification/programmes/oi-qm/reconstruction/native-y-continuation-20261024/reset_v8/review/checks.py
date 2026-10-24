"""Separate review: scalar one-path perturbation of the retained reset-v7 baseline.

Does not import reset-v8 probe.py. Run --author-dir ../ if this directory is
installed as reset_v8/review; the default is already that relative layout.
"""
import argparse,hashlib,json,sys,importlib.util
from pathlib import Path
from itertools import product
from functools import reduce
from operator import xor

def need(v,s):
    if not v: raise RuntimeError(s)

def enc(v): return 4*v[0]+2*v[1]+v[2]
def dec(v): return (v>>2,(v>>1)&1,v&1)
def H(v):
    a,b,c=dec(v)
    return 4*b+2*c+(a^(b&c))
def power(v,n):
    for _ in range(n%12):v=H(v)
    return v

def ray(x,w,j):
    # Separate scalar recurrence, with an integer-coded native H lookup.
    v=H(power(2*x,75)^power(w,75))
    for k in range(1,j+1):
        v=H(v^(power(2*x,k+75) if not k&75 else 0))
    return v

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--author-dir',type=Path,default=Path(__file__).resolve().parent.parent)
    p=ap.parse_args().author_dir.resolve()
    prior=p.parent/'reset_v7'
    sys.path.insert(0,str(prior))
    spec=importlib.util.spec_from_file_location('review_inherited_v7',prior/'probe.py')
    b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
    m=b.m
    target=json.loads((p/'results.json').read_text())
    hashes={n:hashlib.sha256((p/n).read_bytes()).hexdigest() for n in ('probe.py','results.json','../reset_v7/probe.py','../reset_v7/inherited_model.py','../reset_v7/inherited_correction_model.py')}
    need(all(reduce(lambda x,_:H(x),range(12),v)==v for v in range(8)),'native H 12-fold identity')
    need(all(power(v,12)==v for v in range(8)),'H order divides 12')
    permutations=[]
    for x in (0,1):
        perm=[]
        for start in range(8):
            v=start
            for k in range(1,385):v=H(v^(power(2*x,k+75) if not k&75 else 0))
            perm.append(v)
        need(len(set(perm))==8,'block bijection')
        order=1
        while any(reduce(lambda v,_:perm[v],range(order),start)!=start for start in range(8)):order+=1
        need(840%order==0,'permutation order divides exponent')
        permutations.append({'permutation':perm,'order':order})
        for w in range(8):need(ray(x,w,176)==ray(x,w,176+384*order),'exact cyclic ray return')
    need(m.P%(384*840)==0,'actual period divisibility')
    q8=(0,m.S,76);h=(0,-76,76)
    D=lambda a,c:sum(abs(x-y) for x,y in zip(a,c))
    entries=[]
    for shift,r in [(-1,9),(-2,8)]:
        for a,y,z in m.ball(r,(0,0,8)):
            if D(h,(a,m.S+y,68+z))<=m.R+shift:entries.append([shift,[a,y,z]])
    need(entries==[[-1,[0,-9,8]]],'unique initial entry')
    need(D(h,(0,m.S,75))==m.R+9,'q7 first arrival')
    need(D(h,q8)==m.R+8,'q8 first arrival')
    controls=[((0,-m.S,-m.d),b.XM),((0,m.S,-m.d),b.MY^b.MR),((m.T,m.P,-m.d),b.MY),((-m.T,m.P,-m.d),b.MR)]
    def base(t,v):
        val=b.upper(t,v)
        for pos,bits in controls:
            ds=tuple(abs(a-c) for a,c in zip(pos,v))
            if sum(ds)<=t:
                need(sum(ds)==t,'initial lower first front')
                if m.odd(ds):val=m.X(val,m.hp((0,bits,0),t))
        return val
    initial={v:base(m.R-1,v) for v in m.ball(9,(0,0,8))}
    neighbors=lambda v:[tuple(v[k]+(sign if k==axis else 0) for k in range(3)) for axis in range(3) for sign in (-1,1)]
    rows=0;scalar_spots=0;new_tables={};all_rows={}
    for site in ('qY','q2','q7'):
        out,rec=b.calc(site)
        # Baseline neighbor XORs on the unique W first-arrival path.
        sums=[]
        for tau in range(9):
            old=initial if tau==0 else rec[tau-1]
            v=(0,tau-8,8)
            sums.append(m.X(*(old[w] for w in neighbors(v))))
        got={}
        for i,(x,u,my,mr,inp,g) in enumerate(b.ROWS):
            for wc in range(8):
                delta=ray(x,wc,176)^enc(b.lane(initial[(0,-9,8)],i))
                for tau in range(9):
                    s=enc(b.lane(sums[tau],i));delta=H(s^delta)^H(s)
                value=enc(b.lane(out,i))^delta
                got[x,u,my,mr,inp,wc,enc(g)]=value;rows+=1
        table=[got[x,u,0,0,inp,w,g] for x,u,inp in product((0,1),repeat=3) for w,g in product(range(8),repeat=2)]
        need(table==target['q8_tables'][site],site+' complete table')
        need(all(v==got[x,u,0,0,inp,w,g] for (x,u,my,mr,inp,w,g),v in got.items()),'mask independence')
        new_tables[site]=table;all_rows[site]=got
        # Independent scalar full diamond for each native x/u and each input,
        # selected clean apparatus, no reuse of the one-path propagation.
        if site=='q7':
            for x,u,inp in product((0,1),repeat=3):
                gc=3 if u==0 else 5;g=dec(gc);i=b.ROWS.index((x,u,1,1,inp,g))
                old={v:enc(b.lane(base(m.R-2,v),i)) for v in m.ball(8,(0,0,8))}
                now={v:enc(b.lane(initial[v],i)) for v in initial};now[(0,-9,8)]=ray(x,7,176)
                for tau in range(9):
                    nxt={v:old[v]^H(reduce(xor,(now[w] for w in neighbors(v)),0)) for v in m.ball(8-tau,(0,0,8))}
                    if tau==7:nxt[(0,0,7)]=inp
                    old,now=now,nxt
                need(now[(0,0,8)]==got[x,u,1,1,inp,7,gc],'full scalar spot');scalar_spots+=1
    candidates={}
    for site in ('qY','q7'):
        got=all_rows[site];by_u=[]
        for u in (0,1):
            d={}
            for w,g in product(range(8),repeat=2):
                outputs={p:{got[x,u,0,0,p,w,g] for x in (0,1) if site!='qY' or p==x^u} for p in (0,1)}
                if all(len(v)==1 for v in outputs.values()):
                    pair=tuple(next(iter(outputs[p])) for p in (0,1))
                    if pair[0]!=pair[1]:d.setdefault(pair,[]).append([w,g])
            by_u.append(d)
        common=sorted(set(by_u[0])&set(by_u[1]))
        candidates[site]=[{'codes':list(k),'u0_WG':by_u[0][k],'u1_WG':by_u[1][k]} for k in common]
        need(candidates[site]==target['encoding_candidates'][site],'candidate census '+site)
    clean=all_rows['qY']
    need(all(clean[x,u,my,mr,x^u,7,3 if u==0 else 5]==2*(x^u) for x,u,my,mr in product((0,1),repeat=4)),'clean native witness')
    q7=all_rows['q7'];counter=[]
    for u,p in product((0,1),repeat=2):
        a=[q7[x,u,0,0,p,7,3 if u==0 else 5] for x in (0,1)]
        if a[0]!=a[1]:counter.append({'u':u,'p':p,'outputs_by_x':a})
    need(bool(counter),'late-input countercontrol')
    nonlinear=sum(ray(x,w,0)!=(power(2*x,76)^power(w,76)) for x in (0,1) for w in range(8))
    need(nonlinear>0,'isolated-superposition mutant rejected')
    result={'isolated_superposition_counterexamples':nonlinear,'schema':'oi.workspace-reset.v8.independent-review','verdict':'PASS','input_sha256':hashes,'forcing_blocks':permutations,'unique_entry':entries,'independent_scalar_path_rows':rows,'scalar_full_diamond_spots':scalar_spots,'matched_table_rows':sum(map(len,new_tables.values())),'native_common_encoding_count':len(candidates['qY']),'q7_common_encoding_count':len(candidates['q7']),'native_clean_W':7,'native_clean_G_by_u':[3,5],'late_input_counterexamples':counter,'reset':'not_constructed','public_record_law':'not_established'}
    print(json.dumps(result,sort_keys=True,indent=2))
if __name__=='__main__':main()
