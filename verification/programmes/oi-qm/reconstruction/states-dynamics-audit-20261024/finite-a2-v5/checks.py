"""Exact finite geometric qubit-controller controls; standard library only."""
from bisect import bisect_right
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import isqrt, lcm
import json


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


ZERO = (F(0), F(0))
ONE = (F(1), F(0))
I = (F(0), F(1))


def ca(a,b): return (a[0]+b[0],a[1]+b[1])
def cm(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cc(a): return (a[0],-a[1])
def cs(a,x): return (a[0]*x,a[1]*x)


def mm(a,b):
    return tuple(tuple(ca(cm(a[i][0],b[0][j]),cm(a[i][1],b[1][j]))
                       for j in range(2)) for i in range(2))


def adj(a): return tuple(tuple(cc(a[j][i]) for j in range(2)) for i in range(2))
def tr(a):
    v=ca(a[0][0],a[1][1]); require(v[1]==0,'real trace'); return v[0]


def density(r):
    x,y,z=r
    return (((F(1+z,2),F(0)),(x/2,-y/2)),
            ((x/2,y/2),(F(1-z,2),F(0))))


def bloch(a):
    require(a[0][0][1]==a[1][1][1]==0,'real diagonal')
    return (2*a[0][1][0],-2*a[0][1][1],a[0][0][0]-a[1][1][0])


def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def neg(a): return tuple(-x for x in a)
def mv(a,v): return tuple(dot(row,v) for row in a)
def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3))
                 for i in range(3))


IDENT = tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
AXES = {'x':(F(1),F(0),F(0)), 'y':(F(0),F(1),F(0)),
        'z':(F(0),F(0),F(1)), 'a':(F(3,5),F(4,5),F(0))}
ROT = {
    'H':((F(0),F(0),F(1)),(F(0),F(-1),F(0)),(F(1),F(0),F(0))),
    'S':((F(0),F(-1),F(0)),(F(1),F(0),F(0)),(F(0),F(0),F(1))),
    'R':((F(3,5),F(-4,5),F(0)),(F(4,5),F(3,5),F(0)),(F(0),F(0),F(1))),
    'r':((F(3,5),F(4,5),F(0)),(F(-4,5),F(3,5),F(0)),(F(0),F(0),F(1)))}
UNITARY = {
    'H':((((F(1),F(0)),(F(1),F(0))),((F(1),F(0)),(F(-1),F(0)))),F(2)),
    'S':(((ONE,ZERO),(ZERO,I)),F(1)),
    'R':((((F(2),F(-1)),ZERO),(ZERO,(F(2),F(1)))),F(5)),
    'r':((((F(2),F(1)),ZERO),(ZERO,(F(2),F(-1)))),F(5))}


def gate(a,name):
    u,d=UNITARY[name]
    b=mm(mm(u,a),adj(u))
    return tuple(tuple(cs(x,1/d) for x in row) for row in b)


@lru_cache(None)
def projector(axis,s):
    return density(tuple(s*x for x in AXES[axis]))


def project(a,axis,s):
    p=projector(axis,s)
    return mm(mm(p,a),p)


def ceil_log2_fraction(x):
    k=0
    while F(1<<k)<x: k+=1
    return k


def root_interval(x,bits=64):
    require(x>=0,'nonnegative square root')
    d=1<<bits
    lo=isqrt((x.numerator*d*d)//x.denominator)
    l=F(lo,d)
    u=l if l*l==x else F(lo+1,d)
    require(l*l<=x<=u*u,'rational square-root certificate')
    return l,u


class Grid:
    def __init__(self,M,W,B):
        require(M>=8 and M%2==0 and W>=4 and B>=1,'parameter domain')
        self.M,self.W,self.B=M,W,B
        self.K=1<<B
        self.z=[];self.ell=[];self.q=[]
        for face in range(3):
            free=[k for k in range(3) if k!=face]
            for sign in (-1,1):
                for a,b in product(range(-M+1,M,2),repeat=2):
                    z=[0,0,0];z[face]=sign*M;z[free[0]]=a;z[free[1]]=b
                    z=tuple(z);q=sum(x*x for x in z)
                    s=isqrt(q)+(isqrt(q)**2!=q)
                    self.z.append(z);self.q.append(q)
                    self.ell.append(tuple(F(x,s) for x in z))
                    require(dot(self.ell[-1],self.ell[-1])<=1,'inward rational point')
                    require(s>=M and s*s>=q and (s-1)**2<q,'upward normalization')
        self.N=len(self.z)
        require(self.N==6*M*M and len(set(self.z))==self.N,'six-face labels')
        lookup={z:i for i,z in enumerate(self.z)}
        self.anti=tuple(lookup[neg(z)] for z in self.z)
        require(all(self.anti[self.anti[i]]==i for i in range(self.N)), 'antipodal involution')
        self.eta=F(self.N-1,self.K)
        self.e=F(99,M)+F(16,1<<W)+2*self.eta
        self.alpha=1/(F(2,3)+self.e)
        self.kappa=F(52,M)+F(8,1<<W)+self.eta
        self.chi=self.e/(F(2,3)+self.e)
        self.count_cache={};self.weight_cache={};self.sign_cache={};self.mean_cache={}

    def counts(self,n):
        n=tuple(F(x) for x in n)
        require(dot(n,n)==1,'pure direction norm')
        if n in self.count_cache:return self.count_cache[n]
        negative=next(x for x in n if x)!=abs(next(x for x in n if x))
        if negative:
            c=self.counts(neg(n))
            out=tuple(c[self.anti[i]] for i in range(self.N))
            self.count_cache[n]=out
            return out
        weights=[]
        for z,q in zip(self.z,self.q):
            x=dot(n,z)
            weights.append(0 if x<=0 else ((1<<self.W)*self.M**3*x.numerator)//(x.denominator*q*q))
        total=sum(weights);require(total>0,'positive integer normalization')
        counts=[];past=0;cum=0
        for w in weights:
            cum+=w;cut=(self.K*cum)//total
            counts.append(cut-past);past=cut
        require(past==self.K and min(counts)>=0,'finite fair-CDF law')
        tv=sum((abs(F(c,self.K)-F(w,total)) for c,w in zip(counts,weights)),F(0))/2
        require(tv<=self.eta,'CDF rounding bound')
        out=tuple(counts);self.count_cache[n]=out;self.weight_cache[n]=(tuple(weights),total,tv)
        return out

    def mean(self,counts):
        if counts in self.mean_cache:return self.mean_cache[counts]
        total=sum(counts);require(total>0,'normalized carrier law')
        numer=defaultdict(lambda:[0,0,0])
        for c,z,q in zip(counts,self.z,self.q):
            if not c:continue
            s=isqrt(q)+(isqrt(q)**2!=q)
            for k in range(3):numer[s][k]+=c*z[k]
        out=tuple(sum((F(v[k],s*total) for s,v in numer.items()),F(0)) for k in range(3))
        self.mean_cache[counts]=out
        return out

    def signs(self,axis,R):
        key=(axis,R)
        if key in self.sign_cache:return self.sign_cache[key]
        coeff=tuple(sum(AXES[axis][i]*R[i][j] for i in range(3)) for j in range(3))
        d=lcm(*(x.denominator for x in coeff));v=tuple(int(d*x) for x in coeff)
        out=tuple(1 if sum(a*b for a,b in zip(v,z))>=0 else -1 for z in self.z)
        self.sign_cache[key]=out
        return out

    def probability(self,counts,axis,R,s):
        signs=self.signs(axis,R)
        return F(sum(c for c,t in zip(counts,signs) if t==s),sum(counts))

    def index(self,n,r):
        n=tuple(n)
        if next(x for x in n if x)<0:return self.anti[self.index(neg(n),r)]
        c=self.counts(n);cum=0;cuts=[]
        for x in c: cum+=x;cuts.append(cum)
        return bisect_right(cuts,r)


def mix_counts(grid,terms):
    # Terms have nonnegative integer multiplicities; no unknown label is passed
    # to any later read/rotation controller.
    out=[0]*grid.N
    for mult,n in terms:
        for i,c in enumerate(grid.counts(n)):out[i]+=mult*c
    return tuple(out)


def preparation_cases():
    cases=[]
    for name,n in AXES.items():
        cases.append((name,[(1,n)],n))
    n1=(F(2,3),F(-2,3),F(1,3));n2=(F(2,3),F(-2,3),F(-1,3))
    cases.append(('mixed+',[(1,n1),(1,n2)],(F(2,3),F(-2,3),F(0))))
    cases.append(('mixed-',[(1,neg(n1)),(1,neg(n2))],(F(-2,3),F(2,3),F(0))))
    cases.append(('mixedX',[(1,AXES['x']),(1,neg(AXES['x']))],(F(0),)*3))
    cases.append(('mixedZ',[(1,AXES['z']),(1,neg(AXES['z']))],(F(0),)*3))
    return cases


def policy(name,step,outcomes):
    if name=='XXX':return ('M','x')
    if name=='RXa':return [('U','R'),('M','x'),('M','a')][step]
    if name=='adaptive':
        if step==0:return ('M','x')
        if step==1:return ('U','R' if outcomes[-1]==1 else 'H')
        return ('M','a' if outcomes[0]==1 else 'z')
    if name=='stop':
        if step==0:return ('M','x')
        if outcomes[0]==1:return ('STOP','stop')
        return ('M','a' if step==1 else 'z')
    raise RuntimeError(name)


def run_tree(grid,terms,r,name,h=3,decoder_input=False):
    # Source uses grid-response signs and normalized reset tables. Target uses
    # direct rational complex projector/unitary multiplication.
    initial_counts=mix_counts(grid,terms)
    initial_r=(tuple(grid.alpha*x for x in grid.mean(initial_counts))
               if decoder_input else r)
    branches=[((),(),F(1),initial_counts,IDENT,(),density(initial_r),False)]
    nodes=0;zero=0
    for step in range(h):
        nxt=[]
        for rec,outs,w,counts,R,word,rho,stopped in branches:
            op,arg=('STOP','stop') if stopped else policy(name,step,outs)
            if op=='U':
                RR=matmul(ROT[arg],R);ww=word+(arg,)
                require(len(ww)<=h,'finite rotation word')
                nxt.append((rec+((step,'U',arg,1),),outs,w,counts,RR,ww,gate(rho,arg),False));nodes+=1
            elif op=='STOP':
                nxt.append((rec+((step,'STOP','stop',1),),outs,w,counts,R,word,rho,True));nodes+=1
            else:
                for s in (1,-1):
                    p=grid.probability(counts,arg,R,s)
                    rr=project(rho,arg,s)
                    nxt.append((rec+((step,'M',arg,s,1),),outs+(s,),w*p,
                                grid.counts(tuple(s*x for x in AXES[arg])),IDENT,(),rr,False))
                    nodes+=1
                    if w*p==0 or tr(rr)==0:zero+=1
        branches=nxt
    require(sum(b[2] for b in branches)==1,'source complete tree mass')
    require(sum(tr(b[6]) for b in branches)==1,'target complete tree mass')
    tv=F(0);lo=F(0);hi=F(0)
    for rec,outs,w,counts,R,word,rho,stopped in branches:
        require(len(rec)==h and all(x[-1]==1 for x in rec),'fixed ticks and success flags')
        checkR=IDENT
        for g in word:checkR=matmul(ROT[g],checkR)
        require(checkR==R,'word/matrix agreement')
        m=mv(R,grid.mean(counts));rdec=tuple(grid.alpha*x for x in m)
        require(dot(rdec,rdec)<=1,'decoded outgoing positivity')
        wt=tr(rho);v=tuple(w*rdec[i]-bloch(rho)[i] for i in range(3))
        l,u=root_interval(dot(v,v))
        d=abs(w-wt)
        lo+=max(d,l)/2;hi+=max(d,u)/2;tv+=d/2
    bound=min(F(1),h*grid.kappa+(2 if decoder_input else 1)*grid.chi)
    require(hi<=bound,'joint classical-quantum bound')
    return {'branches':len(branches),'nodes':nodes,'zero_mass_nodes':zero,
            'record_tv':tv,'cq_lower':lo,'cq_upper':hi,'bound':bound}


def tv(a,b):return sum((abs(x-y) for x,y in zip(a,b)),F(0))/2


def controls():
    stats=Counter();records=[];principal=[]
    cases=preparation_cases()
    for M in (8,16):
        grid=Grid(M,12,16)
        for name,terms,r in cases:
            rho=density(r)
            for g,R in ROT.items():
                require(bloch(gate(rho,g))==mv(R,r),'independent rational unitary')
                require(tr(gate(rho,g))==1,'unitary trace')
                stats['matrix_rotation_controls']+=1
            for pol in ('XXX','RXa','adaptive','stop'):
                for decoder_input in (False,True):
                    out=run_tree(grid,terms,r,pol,decoder_input=decoder_input)
                    stats['fixed_decoder_input_cases' if decoder_input else 'preparation_target_cases']+=1
                    stats['adaptive_cases']+=1;stats['adaptive_nodes']+=out['nodes']
                    stats['adaptive_leaf_records']+=out['branches'];stats['zero_mass_nodes']+=out['zero_mass_nodes']
                    records.append(out['record_tv']);principal.append(out['cq_upper'])
        # Exact inverse word adds no geometric drift or stochastic draw.
        Rback=matmul(ROT['r'],ROT['R']);require(Rback==IDENT,'inverse rational rotation')
        for name,terms,r in cases:
            c=mix_counts(grid,terms)
            require(grid.mean(c)==mv(Rback,grid.mean(c)),'no unitary-rounding drift')
            require(grid.signs('a',Rback)==grid.signs('a',IDENT),'inverse-word record equality')
            stats['exact_word_inverse_controls']+=1
        # Current-grid mixtures with equal decoded I/2 differ if private carrier
        # or an artificial completion-time label becomes public.
        cx=mix_counts(grid,[(1,AXES['x']),(1,neg(AXES['x']))])
        cz=mix_counts(grid,[(1,AXES['z']),(1,neg(AXES['z']))])
        require(grid.mean(cx)==grid.mean(cz)==(F(0),)*3,'equal decoded mixed preparations')
        private=tv([F(x,sum(cx)) for x in cx],[F(x,sum(cz)) for x in cz])
        require(private>0,'private carrier exposure detects contextual preparation')
        late=lambda z:1 if abs(z[0])>abs(z[2]) else 2
        px=sum(c for c,z in zip(cx,grid.z) if late(z)==1)
        pz=sum(c for c,z in zip(cz,grid.z) if late(z)==1)
        timing=abs(F(px,sum(cx))-F(pz,sum(cz)))
        require(timing>0,'private-dependent completion time detected')
        stats['private_access_controls']+=1;stats['timing_label_controls']+=1
        records.append(private);records.append(timing)

    # Exhaust one finite fair sampler with an independent fixed full scan.
    small=Grid(8,10,10);n=AXES['z'];c=small.counts(n);cum=[];s=0
    for x in c:s+=x;cum.append(s)
    measured=[0]*small.N
    for r in range(small.K):
        chosen=-1
        for j,cut in enumerate(cum):
            if chosen<0 and r<cut:chosen=j
        require(chosen==small.index(n,r),'fixed-scan/binary-reference sampler')
        measured[chosen]+=1
    require(tuple(measured)==c,'all initial fair seeds retained')
    stats['exhausted_fair_seed_values']=small.K

    # A used preparation seed is not fresh for reset, even when its marginal
    # remains uniform. Use the same actual integer in both source functions.
    fresh=Counter();reuse=Counter()
    for sx in (1,-1):
        p=small.probability(c,'x',IDENT,sx)
        ccx=small.counts(tuple(sx*x for x in AXES['x']))
        for sz in (1,-1):fresh[(sx,sz)]=p*small.probability(ccx,'z',IDENT,sz)
    signx=small.signs('x',IDENT);signz=small.signs('z',IDENT)
    for r in range(small.K):
        i=small.index(n,r);sx=signx[i]
        j=small.index(tuple(sx*x for x in AXES['x']),r)
        reuse[(sx,signz[j])]+=F(1,small.K)
    reused_tv=tv([fresh[k] for k in product((1,-1),repeat=2)],
                 [reuse[k] for k in product((1,-1),repeat=2)])
    require(reused_tv>0,'reset-seed reuse countercontrol')

    # A controller ignoring the requested adaptive branch uses a wrong kernel.
    actual=[];wrong=[]
    for sx in (1,-1):
        p=small.probability(c,'x',IDENT,sx);post=small.counts(tuple(sx*x for x in AXES['x']))
        axis='z' if sx==1 else 'a'
        for s2 in (1,-1):
            actual.append(p*small.probability(post,axis,IDENT,s2))
            wrong.append(p*small.probability(post,'z',IDENT,s2))
    adaptive_tv=tv(actual,wrong);require(adaptive_tv>0,'omitted adaptive branch detected')
    # Fixed B-bit blocks per slot: an insufficient final block yields a real
    # terminal failure on the continuing half of this adaptive protocol.
    insufficient_failure=small.probability(c,'x',IDENT,-1)
    require(insufficient_failure>0,'insufficient-bank failure branch')

    # Physical D is positive on the declared cone, not on arbitrary conditioned
    # ontic atoms under an unshrunk3/2moment map.
    require(any(F(9,4)*dot(x,x)>1 for x in small.ell),'unrestricted raw-atom positivity mutant')
    stats['raw_atom_positivity_countercontrols']=1
    return {'counts':dict(sorted(stats.items())),
            'max_checked_record_tv_including_access_mutants':str(max(records)),
            'max_checked_principal_cq_upper':str(max(principal)),
            'reused_reset_seed_record_tv':str(reused_tv),
            'omitted_adaptive_branch_record_tv':str(adaptive_tv),
            'insufficient_bank_terminal_failure_mass':str(insufficient_failure)}


def resources():
    out=[]
    for h,eps in ((1,F(1,10)),(3,F(1,10)),(10,F(1,100))):
        req=3*F(52*h+300)/eps
        M=max(8,int(req)+(req.denominator!=1))
        if M%2:M+=1
        W=max(4,ceil_log2_fraction(3*F(8*h+48)/eps))
        N=6*M*M
        B=max(1,ceil_log2_fraction(3*F((N-1)*(h+6))/eps))
        eta=F(N-1,1<<B)
        E=F(52*h+300,M)+F(8*h+48,1<<W)+(h+6)*eta
        require(E<=eps,'explicit nonvacuous resource/error choice')
        labels=N*sum(4**j for j in range(h+1))
        codebits=ceil_log2_fraction(F(labels))
        out.append({'horizon':h,'epsilon':str(eps),'M':M,'W':W,'B':B,
                    'grid_labels':N,'carrier_word_label_upper_bound':labels,
                    'carrier_label_bits_upper_bound':codebits,
                    'initial_fair_bits_excluding_mixture':(h+1)*B,
                    'comparison':'fixed decoder on input and output',
                    'certified_error_upper':str(E),
                    'large_grid_executed':False})
    return out


def main():
    result={'schema':'oi.finite-geometric-a2-v5.v1','controls':controls(),
            'nonvacuous_resource_certificates':resources(),
            'scope':'Supplied KS single-qubit finite rational-menu controller; adaptive full record and positive fixed decoded input/output states. Not native availability, probability selection, composites or full A1.',
            'verdict':'PASS_CONDITIONAL_FINITE_GEOMETRIC_A2_BOUND'}
    print(json.dumps(result,sort_keys=True,separators=(',',':')))


if __name__=='__main__':main()
