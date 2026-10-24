"""Coordinator checks of the joint-record handoff v1 (independent code; standard library and fractions only).

Station-oriented candidate: S = (x, y, z) are sums of n fair +-1 bits (n odd); station w uses V_w = x w + y u_w + z v_w
with (w, u_w, v_w) an orthonormal frame, and -w uses -V_w; the depth D is uniform on 1..M; success iff 1 <= D <= 5x,
timestamp t = D/(5x). A read along a reports sign(a . V). Only frames with rational entries are used; ties are
excluded by construction (asserted).

J1  the A/B witness at n = 63 recomputed by mixing per-station (timestamp, X read) laws, in the handoff's frames and
    in a different transverse frame for R (u, v rotated by (3/5, 4/5) about R), and for a 16-bin clock.
J2  the four record identities checked atom by atom on (timestamp, read along a) for every menu axis a, n = 15, in
    the alternative frames: the three antipodal identities hold, the fourth fails.
J3  completeness of the four identities: the 4 x 8 matrix of (1, w) has rank 4, and the four relations span its
    null space (rank 4 inside it).
J4  the finite-bin clock/velocity bound at n = 127 and B in {16, 64}: exact TV by depth counting, against B/(8 E[P+]).
J5  the bounded joint-record inequality for the single-call protocol with a B = 16 clock, n in {63, 127}:
    TV(A, B) <= 2 c [delta_n + B/(8 E[P+])], with delta_n the largest single-read error, against the Born values,
    over the eight stations and four menu reads.
"""
from fractions import Fraction as F
from math import comb, ceil
from collections import defaultdict

def M_of(n): return 1<<(9*n-1).bit_length()
def vals(n): return [(2*k-n,comb(n,k)) for k in range(n+1)]
AX={'X':(F(1),F(0),F(0)),'Y':(F(0),F(1),F(0)),'Z':(F(0),F(0),F(1)),'R':(F(4,5),F(3,5),F(0))}
def frames(kind):
    """(w, u, v) for the + stations; rational orthonormal frames."""
    fr={'X':((1,0,0),(0,1,0),(0,0,1))}
    if kind=='handoff':
        fr['Y']=((0,1,0),(-1,0,0),(0,0,1)); fr['Z']=((0,0,1),(0,1,0),(-1,0,0))
        fr['R']=((F(4,5),F(3,5),0),(F(-3,5),F(4,5),0),(0,0,1))
    else:
        fr['Y']=((0,1,0),(0,0,1),(1,0,0)); fr['Z']=((0,0,1),(1,0,0),(0,1,0))
        u0=(F(-3,5),F(4,5),F(0)); v0=(F(0),F(0),F(1)); c,s=F(3,5),F(4,5)
        u=tuple(c*a+s*b for a,b in zip(u0,v0)); v=tuple(-s*a+c*b for a,b in zip(u0,v0))
        fr['R']=((F(4,5),F(3,5),F(0)),u,v)
    for k,(w,u,v) in fr.items():
        W=[tuple(F(a) for a in e) for e in (w,u,v)]
        for i in range(3):
            for j in range(3): assert sum(a*b for a,b in zip(W[i],W[j]))==(1 if i==j else 0)
    return {k:tuple(tuple(F(a) for a in e) for e in fr[k]) for k in fr}
def read_plus_given_x(n,fr,station,a):
    """{x: weighted count over (y, z) of read + along a}, total weight per x is 4^n."""
    base=station[0]; sg=1 if station[1]=='+' else -1
    w,u,v=fr[base]; A=AX[a]
    cw=sum(p*q for p,q in zip(A,w)); cu=sum(p*q for p,q in zip(A,u)); cv=sum(p*q for p,q in zip(A,v))
    out={}
    for x,_ in vals(n):
        if x<=0: continue
        cnt=0
        for y,my in vals(n):
            for z,mz in vals(n):
                val=sg*(cw*x+cu*y+cv*z)
                assert val!=0,'read tie'
                if val>0: cnt+=my*mz
        out[x]=cnt
    return out
def joint(n,fr,station,a,bins=None):
    """unnormalized {(timestamp or bin, read): count}; normalizer M 8^n."""
    rp=read_plus_given_x(n,fr,station,a); out=defaultdict(int)
    for x,mx in vals(n):
        if x<=0: continue
        P=5*x
        for D in range(1,P+1):
            key=F(D,P) if bins is None else ceil(bins*D/P)
            out[(key,True)]+=mx*rp[x]; out[(key,False)]+=mx*(4**n-rp[x])
    return out
A={'R+':F(13,16),'R-':F(3,16)}; B={'X+':F(1,2),'Y+':F(3,8),'Z+':F(1,16),'Z-':F(1,16)}
def mixlaw(n,fr,mixw,a,bins=None):
    o=defaultdict(F)
    for st,wt in mixw.items():
        for k,v in joint(n,fr,st,a,bins).items(): o[k]+=wt*v
    return o
def success_mass(n): return sum(mx*5*x*4**n for x,mx in vals(n) if x>0)
def tvAB(n,fr,bins=None,m=256):
    la,lb=mixlaw(n,fr,A,'X',bins),mixlaw(n,fr,B,'X',bins)
    S=success_mass(n); p=F(S,M_of(n)*8**n); c=1-(1-p)**m
    return c*sum(abs(la[k]-lb[k]) for k in set(la)|set(lb))/(2*S),c
def J1():
    n=63; out={}
    for kind in ('handoff','alt'):
        fr=frames(kind)
        tv,c=tvAB(n,fr); tvb,_=tvAB(n,fr,bins=16); tvblind,_=tvAB(n,fr,bins=1)
        out[kind]=(tv,tvb,tvblind)
    ok='%.8f'%float(out['handoff'][0])=='0.04377046' and '%.8f'%float(out['handoff'][2])=='0.00063982'
    print('J1  n=63, m=256, X read: handoff frames: exact-time TV %.8f, 16-bin %.8f, time-blind %.8f; alternative R frame: %.8f, %.8f, %.8f; reproduces the handoff: %s'%(*[float(v) for v in out['handoff']],*[float(v) for v in out['alt']],ok))
    return ok,out
def J2():
    n=15; fr=frames('alt'); ok=True; fourth={}
    st=['X+','X-','Y+','Y-','Z+','Z-','R+','R-']
    rel=((1,1,-1,-1,0,0,0,0),(1,1,0,0,-1,-1,0,0),(1,1,0,0,0,0,-1,-1),(-4,4,-3,3,0,0,5,-5))
    for a in 'XYZR':
        L={s:joint(n,fr,s,a) for s in st}
        keys=set().union(*L.values())
        for i,r in enumerate(rel):
            nz=sum(1 for k in keys if k[1] and sum(c*L[s].get(k,0) for c,s in zip(r,st))!=0)
            if i<3: ok&= nz==0
            else: fourth[a]=(nz,sum(1 for k in keys if k[1]))
    print('J2  n=15, alternative frames, atom by atom on (timestamp, read), per read axis: antipodal identities hold on every axis %s; fourth identity, nonzero positive-read atoms / timestamps: %s'%(ok,', '.join('%s %d/%d'%(a,*fourth[a]) for a in 'XYZR')))
    return ok and fourth['Z'][0]==0 and all(fourth[a][0]>0 for a in 'XYR')
def J3():
    st=['X+','X-','Y+','Y-','Z+','Z-','R+','R-']
    vec={s:tuple((1 if s[1]=='+' else -1)*c for c in AX[s[0]]) for s in st}
    Mx=[[F(1)]*8]+[[vec[s][i] for s in st] for i in range(3)]
    rel=[(1,1,-1,-1,0,0,0,0),(1,1,0,0,-1,-1,0,0),(1,1,0,0,0,0,-1,-1),(-4,4,-3,3,0,0,5,-5)]
    def rank(rows):
        rows=[[F(x) for x in r] for r in rows]; rk=0
        for c in range(len(rows[0])):
            p=next((i for i in range(rk,len(rows)) if rows[i][c]!=0),None)
            if p is None: continue
            rows[rk],rows[p]=rows[p],rows[rk]
            for i in range(len(rows)):
                if i!=rk and rows[i][c]!=0:
                    f=rows[i][c]/rows[rk][c]; rows[i]=[a-f*b for a,b in zip(rows[i],rows[rk])]
            rk+=1
        return rk
    innull=all(sum(r[j]*Mx[i][j] for j in range(8))==0 for r in rel for i in range(4))
    ok=rank(Mx)==4 and rank(rel)==4 and innull
    print('J3  rank of (1, w) columns = %d; four relations in the null space %s with rank %d = 8 - 4: %s'%(rank(Mx),innull,rank(rel),ok))
    return ok
def J4():
    rows=[]; ok=True
    for n in (127,):
        Epos=F(sum(mx*5*x for x,mx in vals(n) if x>0),2**n)
        for Bn in (16,64):
            num=0; den=0
            for x,mx in vals(n):
                if x<=0: continue
                P=5*x; den+=mx*P
                cnt=defaultdict(int)
                for D in range(1,P+1): cnt[ceil(Bn*D/P)]+=1
                num+=mx*sum(abs(F(cnt[j])-F(P,Bn)) for j in range(1,Bn+1))
            tv=num/(2*den); bound=F(Bn,1)/(8*Epos)
            ok&= tv<=bound; rows.append((n,Bn,float(tv),float(bound)))
    print('J4  clock/velocity TV vs B/(8 E[P+]): %s: %s'%(['n=%d B=%d TV %.6f bound %.6f'%r for r in rows],ok))
    return ok
def J5():
    ok=True; rows=[]
    fr=frames('handoff'); st=['X+','X-','Y+','Y-','Z+','Z-','R+','R-']
    for n in (63,127):
        S=success_mass(n); Bn=16
        tv,c=tvAB(n,fr,bins=Bn)
        delta=F(0)
        for s in st:
            sg=1 if s[1]=='+' else -1; w=tuple(sg*q for q in AX[s[0]])
            for a in 'XYZR':
                rp=read_plus_given_x(n,fr,s,a)
                plus=sum(mx*5*x*rp[x] for x,mx in vals(n) if x>0)
                prob=F(plus,S); born=(1+sum(p*q for p,q in zip(AX[a],w)))/2
                delta=max(delta,abs(prob-born))
        Epos=F(sum(mx*5*x for x,mx in vals(n) if x>0),2**n)
        bound=2*c*(delta+F(Bn,1)/(8*Epos))
        ok&= tv<=bound; rows.append((n,float(tv),float(delta),float(bound)))
    print('J5  single call, 16-bin clock, A vs B: (n, TV, delta_n, bound 2c[delta_n + B/(8E[P+])]) %s; TV <= bound: %s'%(['(%d, %.6f, %.6f, %.6f)'%r for r in rows],ok))
    return ok
if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    a,_=J1(); r=[a,J2(),J3(),J4(),J5()]
    print('coordinator checks:','green' if all(r) else 'RED')
