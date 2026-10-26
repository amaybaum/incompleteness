"""Separate scalar review of masked native route; no author evaluator imports."""
from pathlib import Path
from functools import lru_cache
from itertools import product
import argparse,hashlib,json

H=(0,2,4,7,1,3,5,6)
T=185;P=12*840**185;S=P+T;R=S+68

def need(b,s):
    if not b:raise RuntimeError(s)

def dist(p,q):return sum(abs(a-b) for a,b in zip(p,q))
def hp(v,n):
    for _ in range(n%12):v=H[v]
    return v

def parity(*ds):
    acc=0
    for d in ds:
        if acc&d:return 0
        acc|=d
    return 1

def pack(v):return v[0]*4+v[1]*2+v[2]
def unpack(v):return(v>>2,(v>>1)&1,v&1)

@lru_cache(None)
def lower(t,y,z,x):
    # Both sources x=0 in the spatial first coordinate. At a first-front
    # query all transverse and old-local terms are causally zero.
    if t<0 or min(abs(y)+abs(z),abs(y+76)+abs(z-76))>t:return 0
    if t==0:return 2*x if(y,z)==(0,0) else 7 if(y,z)==(-76,76) else 0
    need(t==min(abs(y)+abs(z),abs(y+76)+abs(z-76)),'lower query stays on earliest front')
    return H[lower(t-1,y-1,z,x)^lower(t-1,y+1,z,x)^lower(t-1,y,z-1,x)^lower(t-1,y,z+1,x)]

@lru_cache(None)
def upper_direct(t,a,b,n,u,j):
    if t<0 or min(a+b+abs(n+s) for s in (0,14,16,18))>t or(t-a-b-n)%2:return 0
    if t==0:return {0:4*u+1,-14:5*u,-16:3+2*u,-18:j}.get(n,0) if a==b==0 else 0
    q=0
    for k in (0,1):
        for sg in(-1,1):
            ab=[a,b];ab[k]+=sg;aa,bb=sorted(map(abs,ab),reverse=True)
            q^=upper_direct(t-1,aa,bb,n,u,j)
    q^=upper_direct(t-1,a,b,n-1,u,j)^upper_direct(t-1,a,b,n+1,u,j)
    return upper_direct(t-2,a,b,n,u,j)^H[q]

@lru_cache(None)
def strip(u,j):
    v={}
    def get(e,a,b,n):
        a,b=sorted((abs(a),abs(b)),reverse=True)
        if e<0 or a+b>e or(e-a-b)%2 or e+a+b>18:return 0
        return v[e,a,b,n]
    for e in range(19):
        for a in range(e+1):
            for b in range(a+1):
                if a+b>e or(e-a-b)%2 or e+a+b>18:continue
                v[e,a,b,0]=upper_direct(e,a,b,0,u,j)
                for n in range(1,254+(18-e)//2):
                    inputs=get(e,a,b,n-1)^get(e-2,a,b,n+1)
                    for da,db in((-1,0),(1,0),(0,-1),(0,1)):
                        inputs^=get(e-1,a+da,b+db,n)
                    v[e,a,b,n]=get(e-2,a,b,n)^H[inputs]
    return v

def ball(r,c=(0,0,9)):
    for a in range(-r,r+1):
        for b in range(-r+abs(a),r-abs(a)+1):
            for d in range(-r+abs(a)+abs(b),r-abs(a)-abs(b)+1):
                yield(c[0]+a,c[1]+b,c[2]+d)

@lru_cache(None)
def diamond(x,u,my,mr,j,intervention=-1):
    table=strip(u,j)
    def initial(t,v):
        a,b=sorted(map(abs,v[:2]),reverse=True);n=R-v[2];e=t-n
        val=table[e,a,b,n-P] if e>=a+b and(e-a-b)%2==0 else 0
        for q,z in [((0,-S,-68),x),((0,S,-68),my^mr),((T,P,-68),my),((-T,P,-68),mr)]:
            ds=[abs(a-b) for a,b in zip(v,q)]
            if sum(ds)<=t:
                need(sum(ds)==t,'lower first arrival');val^=hp(2*z,t) if parity(*ds) else 0
        if t==R-1 and v in ((0,-9,8),(0,-10,9)):
            need(val==0 or val==2*x,'entry excludes upper sources')
            yy,zz=S+v[1]-P,68+v[2]
            val=lower(yy+zz,yy,zz,x)
        return val
    old={v:initial(R-2,v) for v in ball(9)};cur={v:initial(R-1,v) for v in ball(10)};record={}
    for k in range(10):
        nxt={}
        for v in ball(9-k):
            ns=0
            for axis in range(3):
                for d in(-1,1):
                    w=list(v);w[axis]+=d;ns^=cur[tuple(w)]
            nxt[v]=old[v]^H[ns]
        if k in(0,7,8):
            want={0:4*x+2+(x^u),7:x^u,8:2*(x^u)}[k]
            need(nxt[0,0,k]==want,'earlier endpoint preserved')
        if k==8 and intervention>=0:nxt[0,0,8]=2*intervention
        record[k]=nxt;old,cur=cur,nxt
    return cur[0,0,9],record

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--author',type=Path,default=Path(__file__).resolve().parent.parent);ar=ap.parse_args().author
    expected=json.loads((Path(__file__).resolve().parent/'INPUT-HASHES.json').read_text())
    need(all(hashlib.sha256((ar/name).read_bytes()).hexdigest()==digest for name,digest in expected.items()),'reviewed author hashes')
    published=json.loads((ar/'result.json').read_text())
    masked=0
    for x,u,my,mr,a in product((0,1),repeat=5):
        j=pack((u^a,a,u^a));ans,rec=diamond(x,u,my,mr,j)
        need(ans==3*(x^u^a),'independent masked route');masked+=1
        F=lambda mask:pack((u^mask,1^mask,1^u^mask^(u&mask)))
        boundary={(-1,0,8):F(mr),(1,0,8):F(my),
                  (0,-1,8):pack((x^u^(x&u),0,1)),(0,1,8):F(my^mr),
                  (0,0,7):x^u,(0,0,9):pack((1^u,u,1^u))}
        need(all(rec[7][pos]==want for pos,want in boundary.items()),'displayed q8 incoming formulas')
        need(rec[6][0,0,8]==pack((1^u,1,0)),'displayed q8 old local')
        row=next(z for z in published['native_masked_route']['boundary'] if(z['x'],z['u'],z['mY'],z['mR'],z['a'])==(x,u,my,mr,a))
        need(rec[7][0,0,9]==pack(row['old_local']),'masked old-local')
        for key,v in row['incoming'].items():need(rec[8][tuple(map(int,key.split(',')))]==pack(v),'masked incoming')
    compare=0;native_by_u=[];late_by_u=[]
    for mode in('native','q8_intervention'):
        by_u=[]
        for u in(0,1):
            candidates={}
            for j in range(8):
                bins={0:set(),1:set()}
                for x,p in product((0,1),repeat=2):
                    ans,_=diamond(x,u,0,0,j,p if mode!='native' else -1)
                    idx=((x*2+u)*2+p)*8+j
                    need(ans==published['q9_tables'][mode][idx],'scalar author table');compare+=1
                    bins[x^u if mode=='native' else p].add(ans)
                if all(len(s)==1 for s in bins.values()):
                    key=tuple(next(iter(bins[k])) for k in(0,1))
                    if key[0]!=key[1]:candidates.setdefault(key,[]).append(j)
            by_u.append(candidates)
        common=sorted(set(by_u[0])&set(by_u[1]))
        need(common==[tuple(z['codes']) for z in published['q9_common_codes'][mode]],'independent common-code census')
        if mode=='native':native_by_u=common
        else:late_by_u=common
    # Independent first-front grid checks the full reduced indices used by
    # the giant-delay proof, without importing the author's ray recurrence.
    front_rows=0
    for x in(0,1):
        f0=hp(2*x,75)^hp(7,75);f0=H[f0];f1=H[f0]
        for y in range(177):
            if y:
                f0=H[f0^(hp(2*x,y+75) if not y&75 else 0)];f1=H[f1^f0]
            need(f0==lower(y+76,y,76,x) and f1==lower(y+77,y,77,x),'full reduced two-layer front')
            front_rows+=2
    # Source geometry, seed rank, and existing endpoint/frontier separation.
    q9=(0,S,77);J=(0,S,S+154);W=(0,-76,76)
    need(dist(J,q9)==R+9 and dist(W,q9)==R+9,'new boundary source distances')
    need(dist(J,(0,S,76))==R+10,'q8 no influence')
    need(dist((0,0,0),q9)>R+8,'previous unknown outside')
    need(len({pack((u^a,a,u^a)) for u,a in product((0,1),repeat=2)})==4,'rank two affine u,a map')
    need(all(len({pack((u^a,a,u^a)) for a in(0,1)})==2 for u in(0,1)),'one new independent seed dimension')
    need(P%(384*840**2)==0 and P%(12*840**18)==0,'actual period divisibility')
    result={'schema':'oi.masked-route.separate-review.v1','verdict':'PASS_SCOPED',
      'author_commit':'328b74b88eaeddc798bf4693af78a571bf429787','masked_scalar_diamonds':masked,
      'q8_boundary_assignments':16,
      'scalar_table_entries':compare,'independent_reduced_front_entries':front_rows,
      'common_native_code_pairs':[list(z) for z in native_by_u],'common_late_socket_codes':late_by_u,
      'source_geometry_and_affine_rank':'PASS','scope':'Pointwise native-family masked route; no full reset or conditional freshness claim'}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))

if __name__=='__main__':main()
