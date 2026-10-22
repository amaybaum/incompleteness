"""Candidate C-SPH-1 (COLLECTOR.md): exact checks.

Part 1  conditional two-emission law of one station's reservoir, exact rationals (three particles, the 30-direction
        rational sphere, continuous depths, L = v = 1, windows of 1/4): the second herald's direction law given the
        complete accessible record of the first emission (window index, so failures, and outcome) and the second's
        own window or exact crossing time. Paired countercontrols: the absorbed system recycled into the reservoir,
        and a reservoir sharing one direction.
Part 2  the finite realization in D6 format (menu XYZR, the ten preparations): bounded errors of T1-T3, exact T2, and
        preparation equivalence at depth <= 3, with paired controls (an impact-location read; a depleted station).
Part 3  the preregistered apparatus prediction (COLLECTOR.md section 2), decided by its fixed rule.
"""
import sys, os
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
sys.path.insert(0,os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','instrument'))
import instr_bench as IB
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import collector_predict as CP

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def rational_sphere(N):
    out=[]
    for a in range(-N,N+1):
        for b in range(-N,N+1):
            c2=N*N-a*a-b*b
            if c2<0: continue
            c=int(round(c2**0.5))
            if c*c==c2:
                for cc in sorted({c,-c}): out.append((F(a,N),F(b,N),F(cc,N)))
    return out

# ---------------- Part 1: exact piecewise integration ----------------
# Every integrand below is a product of at most three factors, each linear on the pieces between breakpoints, so it
# is a polynomial of degree <= 3 on every piece; the open four-point rule on nodes j/5 (j = 1..4) is exact for it.
def _weights():
    nodes=[F(j,5) for j in range(1,5)]
    # solve sum_j w_j x_j^p = 1/(p+1), p = 0..3, exactly
    A=[[x**p for x in nodes]+[F(1,p+1)] for p in range(4)]
    for c in range(4):
        piv=next(r for r in range(c,4) if A[r][c]!=0); A[c],A[piv]=A[piv],A[c]
        A[c]=[v/A[c][c] for v in A[c]]
        for r in range(4):
            if r!=c and A[r][c]!=0: f=A[r][c]; A[r]=[a-f*b for a,b in zip(A[r],A[c])]
    return nodes,[A[r][4] for r in range(4)]
NODES,WTS=_weights()
def integrate(fns,lo,hi,breaks):
    pts=sorted({lo,hi}|{b for b in breaks if lo<b<hi}); tot=F(0)
    for p,q in zip(pts,pts[1:]):
        h=q-p; s=F(0)
        for x,w in zip(NODES,WTS):
            t=p+h*x; v=F(1)
            for f in fns: v*=f(t)
            s+=w*v
        tot+=h*s
    return tot
U=(F(0),F(0),F(1))                        # station normal (Z+); L = v = 1
TAU=F(1,4)
AR=(F(4,5),F(3,5),F(0))                   # first-emission readout axis R
def cz(d): return dot(d,U)
def f_(d): c=cz(d); return (lambda t: c if (c>0 and 0<=t<1/c) else F(0))
def Fc(d): c=cz(d); return (lambda t: min(c*t,F(1)) if c>0 else F(0))
def g_(d,t0): c=cz(d); return (lambda t: c if (c>0 and t0<=t<t0+1/c) else F(0))
def Gc(d,t0): c=cz(d); return (lambda t: min(c*(t-t0),F(1)) if (c>0 and t>=t0) else F(0))
def sgn(d): v=dot(AR,d); return 1 if v>0 else (-1 if v<0 else 0)
def one(t): return F(1)
D3=rational_sphere(3)
BRK=sorted({1/cz(d) for d in D3 if cz(d)>0})
def joint(k1,s1,k2,mode,tp=None):
    """Unnormalized P(record, lambda_2 = d) for every d; record = (first herald in window k1 with outcome s1, second
    herald in window k2, or at exact time tp if given, a density). mode: 'iid', 'recycle' or 'shared'."""
    lo1,hi1=(k1-1)*TAU,k1*TAU; tc=k1*TAU; lo2,hi2=k2 if isinstance(k2,tuple) else ((k2-1)*TAU,k2*TAU)
    br=BRK+[tc+b for b in BRK]
    def I2(fns):                                      # second-emission factor: window integral or density at tp
        if tp is None: return integrate(fns,lo2,hi2,br)
        v=F(1)
        for f in fns: v*=f(tp)
        return v
    def I1(fns): return integrate(fns,lo1,hi1,br)
    def alpha(d): Fd=Fc(d); a0=Fd(tc); return (lambda t:1-Fd(t)+a0)
    out=defaultdict(F)
    if mode=='shared':
        for d in D3:
            if sgn(d)!=s1 or cz(d)<=0: continue
            out[d]+=I1([f_(d),alpha(d)])*I2([f_(d)])-I1([f_(d)])*I2([f_(d),Fc(d)])
        return out
    for di in D3:
        if sgn(di)!=s1 or cz(di)<=0: continue
        fi=f_(di); A_i=I1([fi])
        rec=(mode=='recycle'); nGi=(lambda t,G=Gc(di,tc):1-G(t)) if rec else one
        for dj in D3:
            if cz(dj)<=0: continue
            fj=f_(dj)
            for dl in D3:
                Fl=Fc(dl)
                # second herald = a non-first particle j (two labelled choices)
                pj=I1([fi,alpha(dl)])*I2([fj,nGi])-A_i*I2([fj,Fl,nGi])
                out[dj]+=2*pj
                if rec:                                   # second herald = the recycled first particle itself
                    gi=g_(di,tc); Fj=Fc(dj)
                    pi=(I1([fi,alpha(dj),alpha(dl)])*I2([gi])-I1([fi,alpha(dj)])*I2([gi,Fl])
                        -I1([fi,alpha(dl)])*I2([gi,Fj])+A_i*I2([gi,Fj,Fl]))
                    out[di]+=pi
        if rec:   # the loops above count the recycled-second term once per (dj, dl) with dj having c > 0 only;
            pass  # particles with c <= 0 never cross, so for them S_j = 1 - F_j(t) + F_j(tc) - F_j(t') = 1 exactly
    return out
def joint_full(k1,s1,k2,mode,tp=None):
    """As joint(), but the recycled-second term also sums over companions moving away (c <= 0), which never cross."""
    out=joint(k1,s1,k2,mode,tp)
    if mode!='recycle': return out
    lo1,hi1=(k1-1)*TAU,k1*TAU; tc=k1*TAU; lo2,hi2=k2 if isinstance(k2,tuple) else ((k2-1)*TAU,k2*TAU)
    br=BRK+[tc+b for b in BRK]
    def I2(fns):
        if tp is None: return integrate(fns,lo2,hi2,br)
        v=F(1)
        for f in fns: v*=f(tp)
        return v
    def I1(fns): return integrate(fns,lo1,hi1,br)
    def alpha(d): Fd=Fc(d); a0=Fd(tc); return (lambda t:1-Fd(t)+a0)
    for di in D3:
        if sgn(di)!=s1 or cz(di)<=0: continue
        fi=f_(di); gi=g_(di,tc); A_i=I1([fi])
        for dj in D3:
            if cz(dj)>0: continue                       # dj moves away: S_j = 1
            for dl in D3:
                Fl=Fc(dl)
                out[di]+=I1([fi,alpha(dl)])*I2([gi])-A_i*I2([gi,Fl])
    return out
def normalize(m):
    t=sum(m.values(),F(0)); return {k:v/t for k,v in m.items() if v} if t else None
def tvd(a,b): return sum((abs(a.get(k,F(0))-b.get(k,F(0))) for k in set(a)|set(b)),F(0))/2
FLUX={d:cz(d) for d in D3 if cz(d)>0}; FLUX={k:v/sum(FLUX.values()) for k,v in FLUX.items()}
def trunc(tp):
    w={d:cz(d) for d in D3 if cz(d)>0 and tp<1/cz(d)}; t=sum(w.values()); return {k:v/t for k,v in w.items()}

def factorized_iid(D,k1,s1,w2):
    """iid law of the second herald, computed through the factorization law(d) ~ A I2(f_d) - B I2(f_d SF), with
    SF = sum_l F_l, A = sum_i I1(f_i (|D| - SF(t) + SF(tc))) and B = sum_i I1(f_i), over first heralds i with
    outcome s1. Checked against the brute-force triple sum on the 30-direction set before it is used."""
    lo1,hi1=(k1-1)*TAU,k1*TAU; tc=k1*TAU; lo2,hi2=w2
    br=sorted({1/cz(d) for d in D if cz(d)>0}); br=br+[tc+b for b in br]
    FL=[Fc(d) for d in D]
    def SF(t): return sum((f(t) for f in FL),F(0))
    sf_tc=SF(tc); nD=len(D)
    heads=[d for d in D if cz(d)>0 and sgn(d)==s1]
    A=sum((integrate([f_(d),(lambda t:nD-SF(t)+sf_tc)],lo1,hi1,br) for d in heads),F(0))
    B=sum((integrate([f_(d)],lo1,hi1,br) for d in heads),F(0))
    out={d:2*(A*integrate([f_(d)],lo2,hi2,br)-B*integrate([f_(d),SF],lo2,hi2,br)) for d in D if cz(d)>0}
    return out
def part1():
    print('Part 1: conditional two-emission law (3 particles, %d directions, exact)'%len(D3))
    ok=True
    # A. iid reservoir, fast band: law given the complete record equals the flux law, for every record value
    nrec=0; worst=F(0)
    for k1 in (1,2):
        for s1 in (1,0,-1):
            for k2 in range(k1+1,5):
                law=normalize(joint_full(k1,s1,k2,'iid'))
                if law is None: continue
                nrec+=1; worst=max(worst,tvd(law,FLUX))
    print('  A  iid, windows <= L/v: %d record values; max TV(law | record, flux law) = %s'%(nrec,worst))
    ok&= worst==0 and nrec>0
    # B. iid, exact crossing time: law given (record, T2 = t') is c 1[c < 1/t'] / Z, fast and late
    worstB=F(0); n=0
    for tp in (F(5,8),F(7,8),F(9,8),F(3,2),F(7,4)):
        for k1 in (1,2):
            for s1 in (1,-1):
                law=normalize(joint_full(k1,s1,9,'iid',tp=tp))
                if law is None: continue
                n+=1; worstB=max(worstB,tvd(law,trunc(tp)))
    print('  B  iid, exact crossing time t\' in {5/8, 7/8, 9/8, 3/2, 7/4}: %d cases; max TV(law, c 1[c < 1/t\']) = %s'%(n,worstB))
    ok&= worstB==0 and n>0
    # C. iid, late windows with only the window index recorded: does the law depend on the first record?
    for k2 in (5,6):
        laws={(k1,s1):normalize(joint_full(k1,s1,k2,'iid')) for k1 in (1,2) for s1 in (1,-1)}
        laws={k:v for k,v in laws.items() if v}
        dep=max(tvd(a,b) for a in laws.values() for b in laws.values())
        print('  C  iid, window %d (past L/v), window index only: max TV across first records = %s (%.2e); TV to flux law up to %.4f'%(k2,dep,float(dep),max(float(tvd(v,FLUX)) for v in laws.values())))
    # C'. the windows above contain no breakpoint 1/c of this direction set, so the herald density is constant on
    # them for every direction; a recorded interval that straddles a breakpoint tests the binned record properly
    for w2 in ((F(7,8),F(11,8)),(F(5,4),F(7,4))):
        laws={(k1,s1):normalize(joint_full(k1,s1,w2,'iid')) for k1 in (1,2) for s1 in (1,-1)}
        laws={k:v for k,v in laws.items() if v}
        dep=max(tvd(a,b) for a in laws.values() for b in laws.values())
        print("  C' iid, recorded interval [%s, %s) straddling a breakpoint: max TV across first records = %s (%.2e)"%(w2[0],w2[1],dep,float(dep)))
    # C''. first emission also past L/v, richer direction set: the factorization is checked against the brute-force
    # sum on the 30-direction set, then used on the 102-direction set
    same=all(normalize(factorized_iid(D3,k1,s1,w2))==normalize(joint_full(k1,s1,w2,'iid'))
             for k1,s1,w2 in ((1,1,(F(7,8),F(11,8))),(2,-1,(F(5,4),F(7,4))),(5,1,(F(3,2),F(5,2)))))
    print("  C'' factorized iid law equals the brute-force sum on 3 records (30 directions): %s"%same)
    ok&=same
    D9=rational_sphere(9)
    for w2 in ((F(13,8),F(17,8)),(F(2),F(3))):
        laws={(k1,s1):normalize(factorized_iid(D9,k1,s1,w2)) for k1 in (1,5,6) for s1 in (1,-1)}
        laws={k:v for k,v in laws.items() if v}
        dep=max(tvd(a,b) for a in laws.values() for b in laws.values())
        print("  C'' iid, 102 directions, first window k1 in {1, 5, 6}, second interval [%s, %s): max TV across first records = %.3e"%(w2[0],w2[1],float(dep)))
    # D, E. countercontrols must show dependence on the first outcome inside the fast band
    for mode,name in (('recycle','absorbed system recycled into the reservoir'),('shared','reservoir sharing one direction')):
        a=normalize(joint_full(1,1,2,mode)); b=normalize(joint_full(1,-1,2,mode))
        gap=tvd(a,b)
        print('  %s  countercontrol, %s: TV(law | s1 = +, law | s1 = -) = %s (%.4f) -> %s'%('D' if mode=='recycle' else 'E',name,gap,float(gap),'caught' if gap>0 else 'MISSED'))
        ok&= gap>0
    return ok

# ---------------- Part 2: finite realization in D6 format ----------------
WSET={'X+':IB.AX['X'],'X-':IB.neg(IB.AX['X']),'Y+':IB.AX['Y'],'Y-':IB.neg(IB.AX['Y']),
      'Z+':IB.AX['Z'],'Z-':IB.neg(IB.AX['Z']),'R+':IB.AX['R'],'R-':IB.neg(IB.AX['R'])}
def tie_free(N):
    return [d for d in rational_sphere(N) if all(dot(IB.AX[m],d)!=0 for m in IB.MENU)]
def window_law(D,w,k):
    out={}
    for d in D:
        c=dot(d,w)
        if c<=0: continue
        out[d]=min(k*c*TAU,F(1))-min((k-1)*c*TAU,F(1))
    t=sum(out.values()); return {d:v/t for d,v in out.items() if v}
class FluxKS:
    """C-SPH-1, finite: hidden state = the system's direction in a tie-free rational sphere; preparation w = its
    station's herald law in window k (k <= 4: the flux law); readout s = sign(a.lambda); update = herald of S_{sa}."""
    extra={}
    def __init__(self,N,k=1):
        self.D=tie_free(N); self.k=k; self.name='C-SPH-1 finite, N=%d, window %d'%(N,k)
        self.law={l:window_law(self.D,w,k) for l,w in WSET.items()}
    def prep(self,label):
        if label in self.law: return dict(self.law[label])
        a,b=('X+','Y+') if label=='r_plus' else ('X-','Y-')
        out=defaultdict(F)
        for l in (a,b):
            for h,p in self.law[l].items(): out[h]+=p/2
        return dict(out)
    def meas(self,m,lam):
        a=IB.AX[m]; s=dot(a,lam)>0
        nxt=self.law[m+('+' if s else '-')]
        return [(1 if s else 0,h,p) for h,p in nxt.items()]
    def push(self,mu,m,o):
        a=IB.AX[m]; mass=sum((p for h,p in mu.items() if (dot(a,h)>0)==(o==1)),F(0))
        return {h:mass*q for h,q in self.law[m+('+' if o else '-')].items()} if mass else {}
class FluxKSImpact(FluxKS):
    """Paired control: the collector's coarse impact record (is lambda_z^2 > lambda_x^2 for the absorbed system?) is
    readable by a declared extra read I, which disturbs nothing."""
    extra={'I':None}
    def __init__(self,N): super().__init__(N); self.name='control: impact-location read, N=%d'%N
    def prep(self,label): return {(h,0):p for h,p in super().prep(label).items()}
    def meas(self,m,st):
        lam,b=st
        if m=='I': return [(b,st,F(1))]
        a=IB.AX[m]; s=dot(a,lam)>0; bit=1 if lam[2]**2>lam[0]**2 else 0
        return [(1 if s else 0,(h,bit),p) for h,p in self.law[m+('+' if s else '-')].items()]
    def push(self,mu,m,o):
        if m=='I': return {st:p for st,p in mu.items() if st[1]==o}
        a=IB.AX[m]; mass=defaultdict(F)
        for (h,b),p in mu.items():
            if (dot(a,h)>0)==(o==1): mass[1 if h[2]**2>h[0]**2 else 0]+=p
        return {(h,bit):ms*q for bit,ms in mass.items() if ms for h,q in self.law[m+('+' if o else '-')].items()}
def push(model,mu,m,o):
    if hasattr(model,'push'): return model.push(mu,m,o)
    out=defaultdict(F)
    for h,p in mu.items():
        for oo,h2,q in IB.kernel(model,m,h):
            if oo==o and q: out[h2]+=p*q
    return dict(out)
def seq_dist(model,mu,seq):
    branches={():mu}
    for m in seq:
        nb={}
        for rec,ms in branches.items():
            for o in (0,1):
                x=push(model,ms,m,o)
                if x: nb[rec+(o,)]=x
        branches=nb
    return {r:sum(ms.values(),F(0)) for r,ms in branches.items()}
def V(model,menu,d,a,b,memo):
    key=(d,frozenset(a.items()),frozenset(b.items()))
    if key in memo: return memo[key]
    if d==0: r=abs(sum(a.values(),F(0))-sum(b.values(),F(0)))/2
    else: r=max(sum(V(model,menu,d-1,push(model,a,m,o),push(model,b,m,o),memo) for o in (0,1)) for m in menu)
    memo[key]=r; return r
def part2():
    print('Part 2: finite realization in D6 format (menu XYZR, ten preparations, depth <= 3)')
    REF=IB.Quantum(); ok=True; rows={}
    for N in (9,15,45):
        M=FluxKS(N); e1=e3=F(0); bad2=F(0)
        for lab in IB.PREPS:
            mu=M.prep(lab); ref=IB.REF.prep(lab)
            for L_ in (1,2,3):
                for seq in product(IB.MENU,repeat=L_):
                    got=seq_dist(M,mu,seq); want=seq_dist(REF,ref,seq)
                    err=max(abs(got.get(k,F(0))-want.get(k,F(0))) for k in set(got)|set(want))
                    if L_==1: e1=max(e1,err)
                    e3=max(e3,err)
            for m in IB.MENU:
                d=seq_dist(M,mu,(m,m)); bad2+=sum(p for k,p in d.items() if k[0]!=k[1])
        rows[N]=(len(M.D),e1,e3,bad2)
        print('  N=%3d |D|=%3d  T1 max error %s (%.4f)  T3 max error %s (%.4f)  T2 disagreement mass %s'%(N,len(M.D),e1,float(e1),e3,float(e3),bad2))
        ok&= bad2==0
    # the model's own push (used above for speed) must agree with the generic kernel push on every reachable state
    M=FluxKSImpact(9); menu=IB.MENU+['I']; agree=True
    for lab in IB.PREPS:
        mu=M.prep(lab)
        for m in menu:
            for o in (0,1):
                x=M.push(mu,m,o); out=defaultdict(F)
                for h,p in mu.items():
                    for oo,h2,q in M.meas(m,h):
                        if oo==o and q: out[h2]+=p*q
                if x!={k:v for k,v in out.items() if v}: agree=False
    print('  fast push equals the generic kernel push (impact model, N=9, all preparations, menu + I): %s'%agree)
    ok&=agree
    for M in (FluxKS(9),FluxKSImpact(9)):
        menu=IB.MENU+list(M.extra); H=IB.reachable(M,menu,tuple(IB.PREPS))
        print('  depth-free outcome-functional span, %s: %d reachable states, span dimension %d'%(M.name,len(H),len(IB.functional_span(M,menu,H))))
    print('  T5 at depth <= 3: optimal bias between the two sides of each D6 basis relation (quantum value 0)')
    for N in (9,15):
        for M in (FluxKS(N),FluxKSImpact(N),FluxKS(N,k=8)):
            menu=IB.MENU+list(M.extra); memo={}; bias=[]
            for lhs,rhs in IB.BASIS:
                a=IB.law_of(M,lhs); b=IB.law_of(M,rhs)
                bias.append(V(M,menu,3,dict(a),dict(b),memo))
            mx=max(bias); rows[(M.name,)]=mx
            print('    %-38s max %s (%.4f)  per relation %s'%(M.name,mx,float(mx),' '.join('%.4f'%float(x) for x in bias)))
    return ok,rows

# ---------------- Part 3: the preregistered prediction ----------------
def part3():
    print('Part 3: preregistered apparatus prediction (COLLECTOR.md section 2; ties counted 1/2)')
    import mpmath as mp
    cases=CP.CASES; AXp={'X':IB.AX['X'],'Y':IB.AX['Y'],'Z':IB.AX['Z'],'R':IB.AX['R']}
    W={'X+':IB.AX['X'],'Y+':IB.AX['Y'],'Z+':IB.AX['Z'],'R+':IB.AX['R'],'X-':IB.neg(IB.AX['X'])}
    cont={(w,n,k):CP.P_window(ca,k) for w,n,ca in cases for k in range(1,9)}
    def Pfin(D,wv,n,k):
        law=window_law(D,wv,k); nv=AXp[n]
        return sum((p*(F(1) if dot(nv,d)>0 else (F(1,2) if dot(nv,d)==0 else F(0))) for d,p in law.items()),F(0))
    control=True; clauses={'a':True,'b':True,'c':True}; detail=[]
    for N in (45,105):
        D=rational_sphere(N)
        for wv in W.values():                       # control: windows 1-4 equal the finite flux law exactly
            flux={d:dot(d,wv) for d in D if dot(d,wv)>0}; t=sum(flux.values()); flux={d:v/t for d,v in flux.items()}
            for k in range(1,5):
                if window_law(D,wv,k)!=flux: control=False
        fin={(w,n,k):Pfin(D,W[w],n,k) for w,n,ca in cases for k in range(1,9)}
        eN=max(abs(mp.mpf(fin[(w,n,k)].numerator)/fin[(w,n,k)].denominator-cont[(w,n,k)]) for w,n,ca in cases for k in range(1,5))
        za=all(fin[('Z+','R',k)]==F(1,2) for k in range(1,9))
        clauses['a']&=za
        worst=mp.mpf(0)
        for w,n,ca in cases:
            if w=='Z+': continue
            for k in range(5,9):
                dv=abs(mp.mpf(fin[(w,n,k)].numerator)/fin[(w,n,k)].denominator-cont[(w,n,k)]); worst=max(worst,dv)
        clauses['b']&= worst<=3*eN
        res={n:(Pfin(D,W['X+'],n,8)+Pfin(D,W['Y+'],n,8))/2-F(5,6)*Pfin(D,W['R+'],n,8)-Pfin(D,W['X-'],n,8)/6 for n in AXp}
        sg=res['X']>0 and res['Y']>0 and res['R']<0
        clauses['c']&=sg
        detail.append((N,len(D),eN,worst,za,res))
        print('  N=%3d |D|=%4d  e_N = %s  max late |P_N - P_cont| = %s (bound 3e_N = %s)  Z+/R = 1/2 at all windows: %s'%(N,len(D),mp.nstr(eN,4),mp.nstr(worst,4),mp.nstr(3*eN,4),za))
        print('        window-8 relation-6 residual: '+'  '.join('%s %.4f'%(n,float(v)) for n,v in res.items()))
        print('        late windows (finite vs continuum): '+'; '.join('%s/%s k=%d %.4f vs %.4f'%(w,n,k,float(fin[(w,n,k)]),float(cont[(w,n,k)])) for w,n,ca in cases[:2] for k in (5,7,8)))
    if not control:
        print('  VOID: the fast-band control failed; no verdict is printed.'); return False,None
    failed=[c for c,v in clauses.items() if not v]
    verdict='SUPPORTED at N = 45 and 105' if not failed else 'NOT SUPPORTED at these N; failing clause(s): '+', '.join(failed)
    print('  control (windows 1-4 equal the finite flux law exactly): green')
    print('  verdict: '+verdict)
    return True,verdict

if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    ok1=part1()
    ok2,_=part2()
    ok3,v=part3()
    print('Part 1 controls and countercontrols:','green' if ok1 else 'RED')
    print('Part 2 exact T2 and fast-push agreement:','green' if ok2 else 'RED')
    print('Part 3 control:','green' if ok3 else 'RED (void)')
