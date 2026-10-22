"""C-SPH-1 complete-record checker, implementing CHECKER-PREREG.md as frozen at 27cbc2d7 (FREEZE.md).

Model (prereg section 3): eight stations, each with N = 1,100,000 particles; per particle an aperture arrival in
[0, 1] with probability q = Lambda/N, uniform in time. A call in slot j (start t_j = (j-1)/8, window 23/200) heralds
the first arrival strictly after t_j within the window. A station whose observed record has h heralds and observed
empty time S has density D(h, S) = (N)_h q^h (1 - qS)^(N-h); integrating its herald offsets gives the pattern
probability P(k, f) = sum_j (-1)^j C(k, j) (1 - q tau (f + j))^N for k heralds and f failed windows. The Poisson
reference uses Lambda^h e^(-Lambda S). Reads use P(s | a, w) = (1 + s a.w)/2 (read_law_checks.py).

Visible record: slots, successes, exact crossing times, reads and probe addresses; preparation addresses and coins are
hidden. Records are enumerated as branches of discrete fields; within a branch the crossing times are continuous and
enter only through each station's S. For preparation i the record density is p_i(y) = sum_w p_i(w) p(y | w), and
TV(P1, P2) = 1/2 int |p1 - p2| dy is taken after that marginalization.

For an equivalent pair, d_w = p1(w) - p2(w) and the hidden-station read factor r_w satisfy sum_w d_w r_w = 0 exactly
on every branch (asserted). Hence, with A the product of the station densities with the preparation's observations kept
separate,  p1 - p2 = c0 A sum_{w in M} d_w r_w (R_w - 1),  where M is the set of visible stations in the hidden support
and R_w = D(h_w + h_p, S_w + S_p) / (D(h_w, S_w) D(h_p, S_p)) merges the preparation into station w. Stations outside
M integrate to their pattern probabilities; the remaining integral over the preparation's and M's offset sums is
bracketed by interval arithmetic and adaptive box bisection, using monotone pieces of log R and of each density.
"""
import sys, os, math, heapq, time, json
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import mpmath as mp
iv=mp.iv; iv.dps=50; mp.mp.dps=50                       # frozen precision (prereg section 5)
import itertools
_TIE=itertools.count()
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,os.path.join(HERE,'..','instrument')); sys.path.insert(0,HERE)
import instr_bench as IB

# ---------------- frozen parameters (prereg section 2) ----------------
K=8; TAU=F(23,200); DELTA=F(1,100); NPOOL=1_100_000
assert K*(TAU+DELTA)==1
LAM=iv.mpf(200)/23*iv.log(iv.mpf(20))
Q=LAM/NPOOL
STATIONS=['X+','X-','Y+','Y-','Z+','Z-','R+','R-']
VEC={'X+':IB.AX['X'],'X-':IB.neg(IB.AX['X']),'Y+':IB.AX['Y'],'Y-':IB.neg(IB.AX['Y']),
     'Z+':IB.AX['Z'],'Z-':IB.neg(IB.AX['Z']),'R+':IB.AX['R'],'R-':IB.neg(IB.AX['R'])}
MENU=IB.MENU
def label(a,s): return a+('+' if s>0 else '-')
def rd(a,s,v): return (1+s*IB.dot(IB.AX[a],VEC[v]))/2          # analytic read law, exact rational
WORK_CELL=10**6; WORK_RUN=5*10**8; INTEGRAL_CAP=400; REL_GAP=F(1,100)   # frozen limits; per-integral cap and target chosen within them
def ivF(x): return iv.mpf(x.numerator)/x.denominator

# ---------------- pattern probabilities and densities ----------------
_PN={}; _PR={}
def PN(k,f):
    if (k,f) not in _PN:
        tq=Q*ivF(TAU); _PN[(k,f)]=sum((iv.mpf((-1)**j*math.comb(k,j))*(1-tq*(f+j))**NPOOL for j in range(k+1)),iv.mpf(0))
    return _PN[(k,f)]
def PR(k,f):
    if (k,f) not in _PR:
        x=LAM*ivF(TAU); _PR[(k,f)]=(1-iv.exp(-x))**k*iv.exp(-x*f)
    return _PR[(k,f)]
def falling(h):
    out=iv.mpf(1)
    for i in range(h): out*=NPOOL-i
    return out
def D_pt(h,S):                                   # fixed-pool density at a point S (iv point), decreasing in S
    return falling(h)*Q**h*(1-Q*S)**(NPOOL-h)
def D_ref_pt(h,S): return LAM**h*iv.exp(-LAM*S)
def D_box(h,Slo,Shi,ref=False):
    fn=D_ref_pt if ref else D_pt
    a=fn(h,Shi); b=fn(h,Slo); return iv.mpf([a.a,b.b])
def logkappa(h1,h2):
    out=iv.mpf(0)
    for i in range(h2): out+=iv.log(iv.mpf(NPOOL-h1-i)/(NPOOL-i))
    return out
def logR_box(h1,S1lo,S1hi,h2,S2lo,S2hi):
    """log R for merging (h2, S2) into (h1, S1): log kappa - h2 log(1-qS1) - h1 log(1-qS2) + (N-h1-h2) log(1-eps),
    eps = q^2 S1 S2 / ((1-qS1)(1-qS2)); each piece is monotone in each S, so corners bound it."""
    def B(S): return -h2*iv.log(1-Q*S)
    def C(S): return -h1*iv.log(1-Q*S)
    def E(S1,S2):
        eps=Q*Q*S1*S2/((1-Q*S1)*(1-Q*S2)); return (NPOOL-h1-h2)*iv.log(1-eps)
    lk=logkappa(h1,h2)
    lo=lk+B(S1lo)+C(S2lo)+E(S1hi,S2hi); hi=lk+B(S1hi)+C(S2hi)+E(S1lo,S2lo)
    return lo.a,hi.b
def V_box(k,lo,hi):
    """Volume density of the sum of k offsets in (0, tau): V_1 = 1 on (0, tau); V_k piecewise polynomial. lo, hi are
    iv points inside one piece [j tau, (j+1) tau]."""
    if k==1: return iv.mpf(1)
    x=iv.mpf([lo.a,hi.b]); t=ivF(TAU); j=int(mp.floor((mp.mpf(lo.a)+mp.mpf(hi.b))/2/mp.mpf(t.a)))
    s=iv.mpf(0)
    for i in range(j+1): s+=(-1)**i*math.comb(k,i)*(x-i*t)**(k-1)
    return s/math.factorial(k-1)

# ---------------- certified box integration ----------------
def G_box(n,c,ivs,ref=False):
    """Exact integral over the box prod_i [lo_i, hi_i] of (1 - q(c + sum u))^n (fixed pool), or of e^(-Lambda(c + sum u))
    (reference): iterated antiderivatives give a signed sum over the box corners."""
    d=len(ivs)
    if d==0: return iv.exp(-LAM*c) if ref else (1-Q*c)**n
    tot=iv.mpf(0)
    for corner in product((0,1),repeat=d):
        x=c+sum((ivF(iv_[1] if e else iv_[0]) for e,iv_ in zip(corner,ivs)),iv.mpf(0))
        sgn=(-1)**sum(corner)                          # lower corner +, upper corner -, per variable
        tot+=sgn*(iv.exp(-LAM*x) if ref else (1-Q*x)**(n+d))
    if ref: return tot/LAM**d
    den=iv.mpf(1)
    for i in range(1,d+1): den*=(n+i)
    return tot/(Q**d*den)
class Integral2:
    """Bracket of int |g| over the individual herald offsets (each in (0, tau)),
    g = D_p prod_{v in M} D_v sum_w c_w (R_w - 1). On a box where the sign of sum_w c_w (R_w - 1) is certified, the
    integral is exact: |sum_w c_w (int D_merge_w prod_{v != w} D_v - int D_p prod_v D_v)|, each term a product of
    closed-form group integrals (G_box). Elsewhere the box contributes [|int g|, max|g| vol]."""
    def __init__(self,prep,Ms,ref=False):
        self.prep=prep; self.Ms=Ms; self.ref=ref; self.evals=0
        self.groups=[('p',prep[0],prep[1])]+[(i,k,f) for i,(k,f,c) in enumerate(Ms)]
        self.slots=[]                                  # variable -> group index
        for gi,(_,k,_) in enumerate(self.groups): self.slots+=[gi]*k
    def gint(self,gis,box):
        """Exact integral of the density of the union of groups gis (merged into one station) over their variables."""
        h=sum(self.groups[g][1] for g in gis); f=sum(self.groups[g][2] for g in gis)
        ivs=[box[i] for i,g in enumerate(self.slots) if g in gis]
        c=ivF(f*TAU)
        if self.ref: return LAM**h*G_box(0,c,ivs,True)
        return falling(h)*Q**h*G_box(NPOOL-h,c,ivs)
    def S_range(self,gi,box):
        f=self.groups[gi][2]; lo=f*TAU; hi=f*TAU
        for i,g in enumerate(self.slots):
            if g==gi: lo+=box[i][0]; hi+=box[i][1]
        return ivF(lo),ivF(hi)
    def bound(self,box):
        self.evals+=1
        if self.ref: return mp.mpf(0),mp.mpf(0),True  # log R_ref = 0 identically (C4): the reference integrand vanishes
        nM=len(self.Ms)
        sep=iv.mpf(1)
        for gi in range(nM+1): sep*=self.gint((gi,),box)
        sig=iv.mpf(0); rm=[]
        Splo,Sphi=self.S_range(0,box)
        for i,(k,f,c) in enumerate(self.Ms):
            mer=self.gint((0,i+1),box)
            for gj in range(1,nM+1):
                if gj!=i+1: mer*=self.gint((gj,),box)
            sig+=ivF(c)*(mer-sep)
            if self.ref: rm.append(iv.mpf(0))
            else:
                Slo,Shi=self.S_range(i+1,box)
                lo,hi=logR_box(k,Slo,Shi,self.prep[0],Splo,Sphi); rm.append(iv.exp(iv.mpf([lo,hi]))-1)
        terms=sum((ivF(c)*r for (k,f,c),r in zip(self.Ms,rm)),iv.mpf(0))
        if terms.a==0 and terms.b==0: return mp.mpf(0),mp.mpf(0),True
        absint=sig if sig.a>=0 else (-sig if sig.b<=0 else iv.mpf([0,max(-sig.a,sig.b)]))
        if terms.a>0 or terms.b<0:                     # certified sign: the box integral is exact
            return max(mp.mpf(0),mp.mpf(absint.a)),mp.mpf(absint.b),True
        # sign not certified: pointwise bound max|g| times the volume
        dmax=iv.mpf(1)
        for gi in range(nM+1):
            lo,hi=self.S_range(gi,box); dmax*=D_box(self.groups[gi][1],lo,hi,self.ref)
        vol=iv.mpf(1)
        for lo,hi in box: vol*=ivF(hi-lo)
        mx=dmax*iv.mpf([0,max(-terms.a,terms.b)])*vol
        return max(mp.mpf(0),mp.mpf(absint.a)) if absint.a>0 else mp.mpf(0),mp.mpf(mx.b),False
    def run(self):
        box=tuple((F(0),TAU) for _ in self.slots)
        lo,hi,ok=self.bound(box)
        heap=[(-(hi-lo),next(_TIE),box,lo,hi,ok)]; gap=hi-lo; est=hi
        rel=mp.mpf(REL_GAP.numerator)/REL_GAP.denominator
        while heap and self.evals<INTEGRAL_CAP and gap>rel*est:
            _,_,box,lo,hi,ok=heapq.heappop(heap)
            if ok or not box: heapq.heappush(heap,(0,next(_TIE),box,lo,hi,ok)); break
            gap-=hi-lo; est-=hi
            d=max(range(len(box)),key=lambda i:box[i][1]-box[i][0])
            a,b=box[d]; m=(a+b)/2
            for half in ((a,m),(m,b)):
                nb=tuple(half if i==d else box[i] for i in range(len(box)))
                l2,h2,ok2=self.bound(nb); gap+=h2-l2; est+=h2; heapq.heappush(heap,(-(h2-l2),next(_TIE),nb,l2,h2,ok2))
        tl=iv.mpf(0); th=iv.mpf(0)
        for item in heap: tl+=iv.mpf(item[3]); th+=iv.mpf(item[4])
        return max(mp.mpf(0),mp.mpf(tl.a)),mp.mpf(th.b)
_ICACHE={}
def integral(prep,Ms,ref=False):
    key=(prep,tuple(Ms),ref)
    if key not in _ICACHE:
        I=Integral2(prep,list(Ms),ref); lo,hi=I.run(); _ICACHE[key]=(lo,hi,I.evals)
    return _ICACHE[key]
class AbsDiff:
    """Bracket of int |D_N(k, f tau + s) - D_ref(k, f tau + s)| V_k(s) ds (diagnostic D1), log rho in monotone pieces."""
    def __init__(self,k,f): self.k=k; self.f=f; self.evals=0
    def bound(self,lo,hi):
        self.evals+=1; t=ivF(TAU); k=self.k
        Slo=self.f*t+lo; Shi=self.f*t+hi
        lk=sum((iv.log(1-iv.mpf(i)/NPOOL) for i in range(k)),iv.mpf(0))
        phi=lambda S:NPOOL*(iv.log(1-Q*S)+Q*S)        # decreasing in S
        psi=lambda S:-k*iv.log(1-Q*S)                  # increasing in S
        lr=iv.mpf([(lk+phi(Shi)+psi(Slo)).a,(lk+phi(Slo)+psi(Shi)).b])
        rm1=iv.exp(lr)-1
        dref=D_box(k,Slo,Shi,ref=True)
        g=dref*rm1
        ab=g if g.a>=0 else (-g if g.b<=0 else iv.mpf([0,max(-g.a,g.b)]))
        val=ab*(V_box(k,lo,hi) if k>0 else iv.mpf(1))*((hi-lo) if k>0 else iv.mpf(1))
        return max(mp.mpf(0),mp.mpf(val.a)),mp.mpf(val.b)
    def run(self):
        t=ivF(TAU)
        if self.k==0:
            d=PN(0,self.f)-PR(0,self.f); ab=d if d.a>=0 else -d
            return mp.mpf(max(0,ab.a)),mp.mpf(ab.b)
        heap=[]; gap=mp.mpf(0); est=mp.mpf(0)
        for j in range(self.k):
            a,b=iv.mpf(j)*t,iv.mpf(j+1)*t; l,h=self.bound(a,b); gap+=h-l; est+=h; heapq.heappush(heap,(-(h-l),next(_TIE),a,b,l,h))
        while heap and self.evals<INTEGRAL_CAP and gap>mp.mpf('0.01')*est:
            _,_,a,b,l,h=heapq.heappop(heap); gap-=h-l; est-=h
            m=iv.mpf(mp.mpf(((a+b)/2).a))
            for x,y in ((a,m),(m,b)):
                l2,h2=self.bound(x,y); gap+=h2-l2; est+=h2; heapq.heappush(heap,(-(h2-l2),next(_TIE),x,y,l2,h2))
        tl=iv.mpf(0); th=iv.mpf(0)
        for _,_,_,_,l,h in heap: tl+=iv.mpf(l); th+=iv.mpf(h)
        return max(mp.mpf(0),mp.mpf(tl.a)),mp.mpf(th.b)
_JCACHE={}
def J1(k,f):
    if (k,f) not in _JCACHE:
        A=AbsDiff(k,f); lo,hi=A.run(); _JCACHE[(k,f)]=(lo,hi,A.evals)
    return _JCACHE[(k,f)]

# ---------------- protocols and branch enumeration (prereg section 4) ----------------
class Branch:
    __slots__=('V','prep','c0','pread','complete')
    def __init__(self,V,prep,c0,pread,complete):
        self.V=V; self.prep=prep; self.c0=c0; self.pread=pread; self.complete=complete
def add(V,st,dk,df):
    V=dict(V); k,f=V.get(st,(0,0)); V[st]=(k+dk,f+df); return V
def enum_F1(reads):
    out=[]
    def rec(slot,target,ri,V,prep,c0,pread):
        if slot>K: out.append(Branch(V,prep,c0,pread,False)); return
        # failure, then retry of the same call in the next slot
        if target=='P': rec(slot+1,target,ri,V,(prep[0],prep[1]+1),c0,pread)
        else: rec(slot+1,target,ri,add(V,target,0,1),prep,c0,pread)
        # success: the carrier is read within the slot
        a=reads[ri]
        for s in (1,-1):
            if target=='P': V2,p2,c2,r2=V,(prep[0]+1,prep[1]),c0,(a,s)
            else:
                pr=rd(a,s,target)
                if pr==0: continue
                V2,p2,c2,r2=add(V,target,1,0),prep,c0*pr,pread
            if ri==len(reads)-1: out.append(Branch(V2,p2,c2,r2,True))
            else: rec(slot+1,label(a,s),ri+1,V2,p2,c2,r2)
    rec(1,'P',0,{},(0,0),F(1),None)
    return out
def enum_F2(probes):
    out=[]
    for ps in (0,1):
        prep=(ps,1-ps)
        for res in product((0,1),repeat=len(probes)):
            V={}
            for st,r in zip(probes,res): V=add(V,st,r,1-r)
            out.append(Branch(V,prep,F(1),None,True))
    return out
def enum_F3(a,w):
    out=[]
    for ps in (0,1):
        for r in (0,1):
            V=add({},w,r,1-r)
            if ps: out+= [Branch(V,(1,0),F(1),(a,s),True) for s in (1,-1)]
            else: out.append(Branch(V,(0,1),F(1),None,True))
    return out
PROTOCOLS=[]
for k in range(4):
    for seq in product(MENU,repeat=k):
        for b in MENU: PROTOCOLS.append(('F1','%s|%s'%(''.join(seq),b),list(seq)+[b]))
for w2 in STATIONS: PROTOCOLS.append(('F2',w2,[w2]))
for w2 in STATIONS:
    for w3 in STATIONS: PROTOCOLS.append(('F2',w2+','+w3,[w2,w3]))
for a in MENU:
    for w in STATIONS: PROTOCOLS.append(('F3','%s>%s'%(a,w),(a,w)))
def branches(proto):
    fam,_,arg=proto
    if fam=='F1': return enum_F1(arg)
    if fam=='F2': return enum_F2(arg)
    return enum_F3(*arg)

# ---------------- preparations (station coins) ----------------
def law(mix):
    out=defaultdict(F)
    for lab,wt in mix.items():
        if lab=='r_plus': out['X+']+=wt/2; out['Y+']+=wt/2
        elif lab=='r_minus': out['X-']+=wt/2; out['Y-']+=wt/2
        else: out[lab]+=wt
    return dict(out)
RELATIONS=[(law(l),law(r)) for l,r in IB.BASIS]
def rfac(br,w):
    if br.pread is None: return F(1)
    a,s=br.pread[:2]; return rd(a,s,w)
def configs(br,w):
    """Station patterns under hidden station w: the preparation merges into w if w is visible in the branch."""
    V=dict(br.V)
    if w in V: k,f=V[w]; V[w]=(k+br.prep[0],f+br.prep[1]); return list(V.values())
    return list(V.values())+[br.prep]
def prob(pats,ref=False):
    out=iv.mpf(1)
    for k,f in pats: out*=(PR(k,f) if ref else PN(k,f))
    return out

# ---------------- the main TV computation ----------------
def tv_cell(d,brs,ref=False):
    lo=iv.mpf(0); hi=iv.mpf(0); used=set(); ok_sum=True
    for br in brs:
        r={w:rfac(br,w) for w in d}
        if sum((d[w]*r[w] for w in d),F(0))!=0: ok_sum=False
        M=[w for w in d if d[w]*r[w]!=0 and w in br.V]
        if not M: continue
        pnon=prob([br.V[v] for v in br.V if v not in M],ref)
        Ms=tuple(sorted((br.V[w][0],br.V[w][1],d[w]*r[w]) for w in M))
        ilo,ihi,_=integral(br.prep,Ms,ref); used.add((br.prep,Ms,ref))
        pre=ivF(br.c0)*pnon/2
        blo=(iv.mpf(pre.a)*iv.mpf(ilo)).a; bhi=(iv.mpf(pre.b)*iv.mpf(ihi)).b
        # an exact lower bound: |int (p1 - p2)| over the branch, from closed-form pattern probabilities
        ex=ivF(br.c0)*sum((ivF(d[w]*r[w])*prob(configs(br,w),ref) for w in d),iv.mpf(0))/2
        exlo=mp.mpf(max(0,ex.a)) if ex.a>=0 else (mp.mpf(max(0,-ex.b)) if ex.b<=0 else mp.mpf(0))
        lo+=iv.mpf(max(blo,exlo)); hi+=iv.mpf(bhi)
    work=sum(_ICACHE[u][2] for u in used)
    return mp.mpf(lo.a),mp.mpf(hi.b),work,ok_sum
def d1_cell(p,brs):
    """Diagnostic D1: TV(fixed pool, Poisson reference) for one preparation; hi by telescoping over stations."""
    hi=iv.mpf(0); lo=iv.mpf(0); used=set(); comp=iv.mpf(0); compR=iv.mpf(0); mass=iv.mpf(0)
    for br in brs:
        c0=ivF(br.c0); diff=iv.mpf(0)
        for w,pw in p.items():
            rw=rfac(br,w)
            if rw==0: continue
            pats=configs(br,w); coef=c0*ivF(pw*rw)
            A=[PN(*x) for x in pats]; B=[PR(*x) for x in pats]
            tel=iv.mpf(0)
            for s_,x in enumerate(pats):
                jl,jh,_=J1(*x); used.add(x)
                pa=iv.mpf(1)
                for t_ in range(s_): pa*=A[t_]
                for t_ in range(s_+1,len(pats)): pa*=B[t_]
                tel+=iv.mpf(pa.b)*iv.mpf(jh)
            hi+=iv.mpf((iv.mpf(coef.b)*iv.mpf(tel.b)/2).b)
            pA=prob(pats); pB=prob(pats,True)
            diff+=coef*(pA-pB); mass+=coef*pA
            if br.complete: comp+=coef*pA; compR+=coef*pB
        dl=(diff.a if diff.a>=0 else (-diff.b if diff.b<=0 else 0))
        lo+=iv.mpf((iv.mpf(max(0,dl))/2).a)
    work=sum(_JCACHE[u][2] for u in used)
    return mp.mpf(lo.a),mp.mpf(hi.b),work,comp,compR,mass

# ---------------- controls ----------------
def C1():
    import read_law_checks as RL           # prints its own lines
    return bool(RL.ok)
def C2():
    import sympy as sp
    q,T=sp.symbols('q T',positive=True); ok=True; n=0
    for N in (1,2,3,4):
        for L in (1,2,3):
            for pat in product((1,0),repeat=L):
                t=sp.symbols('t1:%d'%(L+1),positive=True); tau=sp.symbols('tau1:%d'%(L+1),positive=True)
                u=sp.symbols('u1:%d'%(L+1),positive=True)
                e=[u[i] if pat[i] else tau[i] for i in range(L)]
                # complement of the observed empty set, as ordered segments [0,t1], [t1+e1, t2], ..., [tL+eL, T]
                cuts=[0]+[x for i in range(L) for x in (t[i],t[i]+e[i])]+[T]
                comp=sum(cuts[2*i+1]-cuts[2*i] for i in range(L+1))
                avoid=(1-q)+q/T*comp
                h=sum(pat)
                dens=0
                for assign in product(range(N),repeat=h):
                    if len(set(assign))<h: continue
                    term=(q/T)**h*avoid**(N-h)
                    dens+=term
                closed=sp.ff(N,h)*(q/T)**h*(1-q*sum(e)/T)**(N-h)
                ok&= sp.simplify(sp.expand(dens-closed))==0; n+=1
    print('C2  station closed form = particle-level enumeration, symbolic over call times, windows, offsets and q: %d cases (N <= 4, 14 patterns): %s'%(n,ok))
    # implementation identity used by logR_box: (1 - eps)(1 - qS1)(1 - qS2) = 1 - q(S1 + S2)
    S1,S2=sp.symbols('S1 S2',positive=True)
    eps=q**2*S1*S2/((1-q*S1)*(1-q*S2))
    ok2=sp.simplify((1-eps)*(1-q*S1)*(1-q*S2)-(1-q*(S1+S2)))==0
    print('    merge identity behind log R: (1 - eps)(1 - qS1)(1 - qS2) = 1 - q(S1 + S2): %s'%ok2)
    return ok and ok2
def C4_symbolic():
    import sympy as sp
    L_,S1,S2=sp.symbols('Lambda S1 S2',positive=True); ok=True
    for h1 in range(5):
        for h2 in range(2):
            lr=sp.log(L_**(h1+h2)*sp.exp(-L_*(S1+S2)))-sp.log(L_**h1*sp.exp(-L_*S1))-sp.log(L_**h2*sp.exp(-L_*S2))
            ok&= sp.simplify(sp.expand_log(lr,force=True))==0
    print('C4  reference merge: log R_ref = 0 identically for h1 <= 4, h2 <= 1 (pointwise agreement): %s'%ok)
    return ok
def C5():
    import sympy as sp
    N=3; a=F(1,16)
    def P(k,f): return sum((F((-1)**j*math.comb(k,j))*(1-a*(f+j))**N for j in range(k+1)),F(0))
    def ev(p):
        tot=F(0)
        for w,pw in p.items():
            for s in (1,-1):
                r=rd('Z',s,w)
                if r==0: continue
                sig=label('Z',s)
                tot+=pw*r*(P(1,1) if sig==w else P(1,0)*P(0,1))
        return tot
    dz=ev(law({'Z+':F(1,2),'Z-':F(1,2)}))-ev(law({'X+':F(1,2),'X-':F(1,2)}))
    x=sp.symbols('x',positive=True); Pr=lambda k,f:(1-sp.exp(-x))**k*sp.exp(-x*f)
    dref=sp.simplify(Pr(1,1)-Pr(1,0)*Pr(0,1))
    ok=dz==F(151201,16777216) and dref==0
    print('C5  herald-history regression through the checker\'s merge rule: fixed pool %s; Poisson reference %s: %s'%(dz,dref,ok))
    return ok
def enclose_sqrt2(c):
    """Interval enclosure of a number p + r sqrt(2) with p, r rational (asserted exactly)."""
    import sympy as sp
    c=sp.expand(sp.nsimplify(c)); p_=c.subs(sp.sqrt(2),0); r_=sp.expand((c-p_)/sp.sqrt(2))
    assert p_.is_Rational and r_.is_Rational and sp.simplify(p_+r_*sp.sqrt(2)-c)==0
    return ivF(F(int(p_.p),int(p_.q)))+ivF(F(int(r_.p),int(r_.q)))*iv.sqrt(iv.mpf(2))
def C6():
    import sympy as sp
    x,y=sp.symbols('x y',real=True)
    # mu_w is uniform on the unit disk normal to w, lifted (flux law). For w = Z: E = [2x^2 + y^2 < 1] on the disk.
    aZ=sp.integrate(2*sp.sqrt(1-2*x**2),(x,-1/sp.sqrt(2),1/sp.sqrt(2)))/sp.pi
    # for w = X with disk coordinates (y, z): E = [y^2 + 2 z^2 > 1]; the ellipse lies inside the disk
    aX=1-sp.integrate(2*sp.sqrt(1-2*x**2),(x,-1/sp.sqrt(2),1/sp.sqrt(2)))/sp.pi
    aZ=sp.nsimplify(sp.simplify(aZ)); aX=sp.nsimplify(sp.simplify(aX))
    # joint (s, E) for a read along Z: +Z gives s = +; -Z gives s = -; +-X split s evenly (z -> -z symmetry)
    def rjoint(w,s,E):
        pe=aZ if w[0]=='Z' else aX; pE=pe if E else 1-pe
        if w[0]=='Z': return pE if (s>0)==(w[1]=='+') else 0
        return pE/2
    dz=law({'Z+':F(1,2),'Z-':F(1,2)}); dx=law({'X+':F(1,2),'X-':F(1,2)})
    sup=set(dz)|set(dx); dd={w:dz.get(w,F(0))-dx.get(w,F(0)) for w in sup}
    worst=None
    for w in STATIONS:
        lo=iv.mpf(0)
        for br in enum_F3('Z',w):
            for E in ((True,False) if br.pread else (None,)):
                tot=iv.mpf(0)
                for v,dv in dd.items():
                    if br.pread: rv=enclose_sqrt2(rjoint(v,br.pread[1],E))
                    else: rv=iv.mpf(1)
                    tot+=ivF(dv)*rv*prob(configs(br,v))
                lo+=iv.mpf(max(0,(tot.a if tot.a>=0 else (-tot.b if tot.b<=0 else 0))))/2
        worst=mp.mpf(lo.a) if worst is None else min(worst,mp.mpf(lo.a))
    ok=worst>mp.mpf('0.02')
    print('C6  impact-read control (absorber privacy): P(E | Z-mix) = %s, P(E | X-mix) = %s; F3 a = Z, all 8 probes: min lo = %s > 0.02: %s'%(aZ,aX,mp.nstr(worst,6),ok))
    return ok
def C8():
    dz=law({'Z+':F(1,2),'Z-':F(1,2)}); dx=law({'X+':F(1,2),'X-':F(1,2)})
    disjoint=not (set(dz)&set(dx)); masses=[]
    for w in STATIONS:
        for p in (dz,dx):
            m=iv.mpf(0)
            for br in enum_F2([w]):
                for v,pv in p.items(): m+=ivF(pv)*prob(configs(br,v))
            masses.append(m)
    ok=disjoint and all(m.a<=1<=m.b for m in masses)
    print('C8  address-exposure control: supports disjoint %s and every record mass contains 1, so TV = 1 exactly on all 8 single-probe F2 protocols: %s'%(disjoint,ok))
    return ok

def mpf_fraction(x):
    """Exact value of a binary mpf as a Fraction."""
    m,e=mp.mpf(x).man_exp
    return F(int(m))*F(2)**int(e) if e>=0 else F(int(m),2**int(-e))
def dec_out(x,up):
    import decimal
    fr=mpf_fraction(x)
    if fr==0: return '0'
    ctx=decimal.Context(prec=8,rounding=decimal.ROUND_CEILING if up else decimal.ROUND_FLOOR)
    return str(ctx.divide(decimal.Decimal(fr.numerator),decimal.Decimal(fr.denominator)))
def encloses(a,b,lo,hi):
    return F(a)<=mpf_fraction(lo) and F(b)>=mpf_fraction(hi)
def I3():
    """G_box against direct values: positive volume, and quadrature in 1, 2 and 3 dimensions (numerical evidence)."""
    ok=True
    v=G_box(0,iv.mpf(0),[(F(0),TAU)])
    ok&= v.a>0 and v.a<=ivF(TAU).b and ivF(TAU).a<=v.b
    q=mp.mpf(Q.a); n=NPOOL-1; c=mp.mpf(1)/10
    for ivs in ([(F(0),F(1,20))],[(F(0),F(1,20)),(F(1,40),F(1,10))],[(F(0),F(1,20)),(F(1,40),F(1,10)),(F(1,100),F(1,30))]):
        g=G_box(n,ivF(F(1,10)),ivs); gr=G_box(0,ivF(F(1,10)),ivs,True)
        rng=[[mp.mpf(x.numerator)/x.denominator for x in iv_] for iv_ in ivs]
        num=mp.quad(lambda *u:(1-q*(c+sum(u)))**n,*rng); numr=mp.quad(lambda *u:mp.exp(-mp.mpf(LAM.a)*(c+sum(u))),*rng)
        ok&= abs(mp.mpf(g.a)-num)<mp.mpf('1e-12')*abs(num) and abs(mp.mpf(gr.a)-numr)<mp.mpf('1e-12')*abs(numr) and g.a>0 and gr.a>0
    print('I3  box antiderivatives: int_0^(23/200) 1 du = %s (positive); fixed-pool and reference box integrals match quadrature in 1, 2 and 3 dimensions: %s'%(mp.nstr(mp.mpf(v.a),12),ok))
    return ok

def _work(key):
    I=Integral2(key[0],list(key[1])); lo,hi=I.run(); return (lo,hi,I.evals)

if __name__=='__main__':
    t0=time.time()
    print(__doc__.strip().splitlines()[0])
    print('protocols: F1 %d, F2 %d, F3 %d, total %d; cases %d'%(sum(p[0]=='F1' for p in PROTOCOLS),sum(p[0]=='F2' for p in PROTOCOLS),sum(p[0]=='F3' for p in PROTOCOLS),len(PROTOCOLS),6*len(PROTOCOLS)))
    ctrl={}
    ctrl['I3']=I3(); ctrl['C1']=C1(); ctrl['C2']=C2(); ctrl['C4s']=C4_symbolic(); ctrl['C5']=C5(); ctrl['C6']=C6(); ctrl['C8']=C8()
    BR={p[1]+'@'+p[0]:branches(p) for p in PROTOCOLS}
    keys=set()
    for fam,name,arg in PROTOCOLS:
        for (l,r) in RELATIONS:
            d={w:l.get(w,F(0))-r.get(w,F(0)) for w in set(l)|set(r)}
            for br in BR[name+'@'+fam]:
                rr={w:rfac(br,w) for w in d}
                M=[w for w in d if d[w]*rr[w]!=0 and w in br.V]
                if M: keys.add((br.prep,tuple(sorted((br.V[w][0],br.V[w][1],d[w]*rr[w]) for w in M))))
    keys=sorted(keys,key=repr)
    print('distinct integrals: %d (cap %d evaluations each, target relative gap %s)'%(len(keys),INTEGRAL_CAP,REL_GAP),flush=True)
    import multiprocessing as mpr
    with mpr.get_context('fork').Pool(4) as pool:
        res=pool.map(_work,keys,chunksize=16)
    for k,v in zip(keys,res): _ICACHE[(k[0],k[1],False)]=v
    print('integrals done at %.0f s'%(time.time()-t0),flush=True)
    rows=[]; c3=True; c4=True; sum_ok=True; run_work=0; cell_work_max=0
    for fam,name,arg in PROTOCOLS:
        brs=BR[name+'@'+fam]
        for ri,(l,r) in enumerate(RELATIONS):
            d={w:l.get(w,F(0))-r.get(w,F(0)) for w in set(l)|set(r)}
            lo,hi,work,ok=tv_cell(d,brs); sum_ok&=ok
            rlo,rhi,_,_=tv_cell(d,brs,ref=True)
            c4&= rhi<=mp.mpf('1e-30')
            if ri==4: c3&= hi==0
            cell_work_max=max(cell_work_max,work)
            rows.append((fam,name,ri+1,lo,hi))
    run_work=sum(v[2] for v in _ICACHE.values())
    ctrl['C3']=c3; ctrl['C4']=c4 and ctrl['C4s']
    print('C3  identity relation 5: hi = 0 on every protocol: %s'%c3)
    print('C4  Poisson reference: hi <= 1e-30 on every pair and protocol: %s'%c4)
    print('implementation: sum_w d_w r_w = 0 exactly on every branch: %s; distinct integrals %d; box evaluations per cell max %d (limit %d); run %d (limit %d)'%(sum_ok,len(_ICACHE),cell_work_max,WORK_CELL,run_work,WORK_RUN))
    green=all(ctrl.values()) and sum_ok and cell_work_max<=WORK_CELL and run_work<=WORK_RUN
    # D1 and completion, per preparation procedure appearing in the relations
    procs={}
    for ri,(l,r) in enumerate(RELATIONS):
        for side,p in (('lhs',l),('rhs',r)): procs[tuple(sorted(p.items()))]=p
    d1_hi=mp.mpf(0); d1_lo=mp.mpf(0); comp={}; massok=True; d1_rows=[]
    for key,p in procs.items():
        for fam,name,arg in PROTOCOLS:
            lo,hi,work,c,cR,m=d1_cell(p,BR[name+'@'+fam])
            d1_hi=max(d1_hi,hi); d1_lo=max(d1_lo,lo); massok&= m.a<=1<=m.b
            comp.setdefault(fam,[]).append((mp.mpf(c.a),mp.mpf(c.b),mp.mpf(cR.a),mp.mpf(cR.b)))
            d1_rows.append((fam,name,'+'.join('%s:%s'%(w,v) for w,v in key),lo,hi))
    B=8*LAM**2/NPOOL
    print('D1  coupling diagnostic: max over preparations and protocols of hi(TV(fixed pool, Poisson)) = %s; bound m Lambda^2/N = %s; largest lower bracket %s'%(mp.nstr(d1_hi,6),mp.nstr(mp.mpf(B.b),6),mp.nstr(d1_lo,6)))
    print('    record masses contain 1 for every preparation and protocol: %s'%massok)
    for fam in ('F1','F2','F3'):
        v=comp[fam]
        print('    completion %s: fixed pool in [%s, %s]; Poisson reference in [%s, %s]'%(fam,mp.nstr(min(x[0] for x in v),8),mp.nstr(max(x[1] for x in v),8),mp.nstr(min(x[2] for x in v),8),mp.nstr(max(x[3] for x in v),8)))
    # per-family summary and verdict
    for fam in ('F1','F2','F3'):
        rs=[x for x in rows if x[0]==fam]
        top=max(rs,key=lambda x:x[4])
        print('TV  %s: %d cases; max hi %s (%s, relation %d; lo %s); cells with hi = 0: %d'%(fam,len(rs),mp.nstr(top[4],6),top[1],top[2],mp.nstr(top[3],6),sum(1 for x in rs if x[4]==0)))
    n_acc=sum(1 for x in rows if x[4]<=mp.mpf('0.01')); n_rej=sum(1 for x in rows if x[3]>mp.mpf('0.01'))
    n_und=len(rows)-n_acc-n_rej
    import csv
    enc=True
    with open(os.path.join(HERE,'record_checker_cells.csv'),'w',newline='') as fh:
        cw=csv.writer(fh,lineterminator='\n'); cw.writerow(['family','protocol','relation','lo','hi'])
        for fam,name,ri,lo,hi in rows:
            a,b=dec_out(lo,False),dec_out(hi,True); enc&=encloses(a,b,lo,hi); cw.writerow([fam,name,ri,a,b])
    with open(os.path.join(HERE,'record_checker_d1.csv'),'w',newline='') as fh:
        cw=csv.writer(fh,lineterminator='\n'); cw.writerow(['family','protocol','preparation','lo','hi'])
        for fam,name,pk,lo,hi in d1_rows:
            a,b=dec_out(lo,False),dec_out(hi,True); enc&=encloses(a,b,lo,hi); cw.writerow([fam,name,pk,a,b])
    print('export: every CSV endpoint is rounded outward to 8 significant digits (lo down, hi up), checked exactly: %s'%enc)
    green&=enc
    print('cells: %d; hi <= 0.01: %d; lo > 0.01: %d; undecided: %d'%(len(rows),n_acc,n_rej,n_und))
    if not green:
        print('VOID: a control or a work limit failed; no verdict is printed.')
    else:
        verdict='ACCEPT' if n_acc==len(rows) else ('REJECT' if n_rej else 'UNDECIDED')
        print('controls green; verdict on P* (pool allocation 0.01; total with the aperture bound <= 0.02): %s'%verdict)
    print('elapsed %.0f s'%(time.time()-t0))
