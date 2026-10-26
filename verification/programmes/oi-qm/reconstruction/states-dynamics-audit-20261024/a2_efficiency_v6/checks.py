"""Exact finite-menu geometric A2 envelope; standard library, no source imports."""
from fractions import Fraction as Q
from math import isqrt, lcm
from itertools import product
from collections import Counter, defaultdict
from bisect import bisect_right
import hashlib
import json


def check(x, label):
    if not x:
        raise RuntimeError(label)


def dot(x,y): return sum((a*b for a,b in zip(x,y)),Q(0))
def minus(x): return tuple(-a for a in x)
def mv(a,x): return tuple(dot(row,x) for row in a)
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def transpose(a): return tuple(zip(*a))
EYE=tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
AXES={'X':(Q(1),Q(0),Q(0)), 'Y':(Q(0),Q(1),Q(0)),
      'Z':(Q(0),Q(0),Q(1)), 'a':(Q(3,5),Q(4,5),Q(0))}
BASE=dict(AXES, p=(Q(2,3),Q(-2,3),Q(1,3)), q=(Q(2,3),Q(-2,3),Q(-1,3)))
PREP={name+sg:tuple(s*x for x in n) for name,n in BASE.items() for s,sg in [(1,'+'),(-1,'-')]}
ROT={
 'H':((Q(0),Q(0),Q(1)),(Q(0),Q(-1),Q(0)),(Q(1),Q(0),Q(0))),
 'S':((Q(0),Q(-1),Q(0)),(Q(1),Q(0),Q(0)),(Q(0),Q(0),Q(1))),
 'R':((Q(3,5),Q(-4,5),Q(0)),(Q(4,5),Q(3,5),Q(0)),(Q(0),Q(0),Q(1))),
 'r':((Q(3,5),Q(4,5),Q(0)),(Q(-4,5),Q(3,5),Q(0)),(Q(0),Q(0),Q(1)))}
ALPHA=Q(3,2)
HORIZON=3


def roots(q,bits=64):
    check(q>=0,'nonnegative root')
    d=1<<bits
    k=isqrt(q.numerator*d*d//q.denominator)
    lo=Q(k,d); hi=lo if lo*lo==q else Q(k+1,d)
    check(lo*lo<=q<=hi*hi,'squared root enclosure')
    return lo,hi


def integer_direction(n):
    den=lcm(*(x.denominator for x in n))
    out=tuple(int(x*den) for x in n)
    return out,den


def words(h):
    out=[((),EYE)]
    for length in range(1,h+1):
        for w in product(ROT,repeat=length):
            a=EYE
            for k in w:a=mm(ROT[k],a)
            check(mm(transpose(a),a)==EYE,'exact proper-word orthogonality')
            out.append((w,a))
    return out


class Geometry:
    def __init__(self,M,W=16,B=24):
        self.M,self.W,self.B=M,W,B;self.K=1<<B
        self.z=[];self.norm=[];self.ell_den=[]
        for face in range(3):
            free=[j for j in range(3) if j!=face]
            for s in (-1,1):
                for u,v in product(range(-M+1,M,2),repeat=2):
                    z=[0,0,0];z[face]=s*M;z[free[0]]=u;z[free[1]]=v
                    z=tuple(z);q=sum(x*x for x in z);t=isqrt(q)+(isqrt(q)**2<q)
                    check(t*t>=q and (t-1)**2<q,'inward norm integer')
                    self.z.append(z);self.norm.append(q);self.ell_den.append(t)
        self.N=len(self.z);check(self.N==6*M*M and len(set(self.z))==self.N,'full six-face alphabet')
        index={z:i for i,z in enumerate(self.z)};self.anti=tuple(index[minus(z)] for z in self.z)
        self.counts_cache={};self.mean_cache={};self.prob_cache={};self.weight_cache={}

    def counts(self,n):
        n=tuple(n)
        if n in self.counts_cache:return self.counts_cache[n]
        check(dot(n,n)==1,'pure prep/reset direction')
        if next(x for x in n if x)<0:
            c=self.counts(minus(n));out=tuple(c[i] for i in self.anti)
        else:
            v,d=integer_direction(n)
            weights=[]
            factor=(1<<self.W)*self.M**3
            for z,q in zip(self.z,self.norm):
                a=sum(x*y for x,y in zip(v,z))
                weights.append(0 if a<=0 else factor*a//(d*q*q))
            total=sum(weights);check(total>0,'positive rational-geometric weights')
            counts=[];cum=0;last=0
            for x in weights:
                cum+=x;cut=self.K*cum//total;counts.append(cut-last);last=cut
            check(last==self.K and min(counts)>=0,'complete fair CDF mass')
            err=sum((abs(Q(c,self.K)-Q(w,total)) for c,w in zip(counts,weights)),Q(0))/2
            check(err<=Q(self.N-1,self.K),'independent CDF rounding certificate')
            self.weight_cache[n]=(tuple(weights),total,err)
            out=tuple(counts)
        check(sum(out)==self.K and min(out)>=0,'normalized sampler')
        self.counts_cache[n]=out
        return out

    def mean(self,n):
        n=tuple(n)
        if n in self.mean_cache:return self.mean_cache[n]
        counts=self.counts(n);group=defaultdict(lambda:[0,0,0])
        for c,z,t in zip(counts,self.z,self.ell_den):
            for k in range(3):group[t][k]+=c*z[k]
        mean=tuple(sum((Q(x[k],t*self.K) for t,x in group.items()),Q(0)) for k in range(3))
        self.mean_cache[n]=mean
        return mean

    def probability(self,n,R,axis,s=1):
        coeff=mv(transpose(R),AXES[axis]);key=(tuple(n),coeff)
        if key not in self.prob_cache:
            v,d=integer_direction(coeff);counts=self.counts(n)
            total=sum(c for c,z in zip(counts,self.z) if sum(a*b for a,b in zip(v,z))>=0)
            self.prob_cache[key]=Q(total,self.K)
        p=self.prob_cache[key]
        return p if s==1 else 1-p

    def index(self,n,seed):
        if next(x for x in n if x)<0:
            return self.anti[self.index(minus(n),seed)]
        counts=self.counts(n);cum=[];x=0
        for c in counts:x+=c;cum.append(x)
        return bisect_right(cum,seed)


def envelope(grid):
    ws=words(HORIZON);maxnorm=Q(0);maxchi=Q(0);chi_witness=None
    maxk=Q(0);k_witness=None;positive=0;readcases=0
    for name,n in PREP.items():
        m=grid.mean(n);rr=tuple(ALPHA*x for x in m)
        q=dot(rr,rr);check(q<=1,'fixed 3/2 decoder positive on every ray')
        maxnorm=max(maxnorm,q)
        diff=tuple(rr[i]-n[i] for i in range(3));squared=dot(diff,diff)
        lo,hi=roots(squared);ch=hi/2
        if ch>maxchi:maxchi=ch;chi_witness={'ray':name,'squared_bloch_error':str(squared)}
        for word,R in ws:
            check(dot(mv(R,rr),mv(R,rr))==q,'all-word positivity by exact rotation')
            positive+=1
            if len(word)==HORIZON:continue
            rn=mv(R,n)
            for axis,a in AXES.items():
                actual=grid.probability(n,R,axis)
                target=(1+dot(a,rn))/2
                err=abs(actual-target)
                if err>maxk:
                    maxk=err;k_witness={'ray':name,'word':list(word),'axis':axis,'actual_plus':str(actual),'quantum_plus':str(target)}
                readcases+=1
    E=HORIZON*maxk+2*maxchi
    digest=hashlib.sha256(json.dumps({name:grid.counts(n) for name,n in PREP.items()},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    return {'M':grid.M,'W':grid.W,'B':grid.B,'grid_labels':grid.N,
      'decoder_alpha':str(ALPHA),'maximum_decoded_ray_norm_squared':str(maxnorm),
      'kappa':str(maxk),'kappa_witness':k_witness,'chi_upper':str(maxchi),'chi_witness':chi_witness,
      'fixed_decoder_CQ_bound_upper':str(E),'within_one_tenth':E<=Q(1,10),
      'positive_ray_word_cases':positive,'ray_word_axis_read_cases':readcases,
      'distinct_direction_probability_cases':len(grid.prob_cache),
      'cdf_count_vectors_sha256':digest,'grid_executed':True}


# An independent rational-complex 2x2 reference, as pairs of real/imaginary fractions.
def ca(a,b):return (a[0]+b[0],a[1]+b[1])
def cm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conj(a):return (a[0],-a[1])
def scale(a,r):return (a[0]*r,a[1]*r)
def mul2(a,b):return tuple(tuple(ca(cm(a[i][0],b[0][j]),cm(a[i][1],b[1][j])) for j in range(2)) for i in range(2))
def adj2(a):return tuple(tuple(conj(a[j][i]) for j in range(2)) for i in range(2))
def density(n,mass=Q(1)):
    x,y,z=n
    return (((Q(mass+z,2),Q(0)),(x/2,-y/2)),((x/2,y/2),(Q(mass-z,2),Q(0))))
def trace(a):return a[0][0][0]+a[1][1][0]
def bloch(a):return (2*a[0][1][0],-2*a[0][1][1],a[0][0][0]-a[1][1][0])
Z=(Q(0),Q(0));O=(Q(1),Q(0));I=(Q(0),Q(1))
U2={'H':((((Q(1),Q(0)),(Q(1),Q(0))),((Q(1),Q(0)),(Q(-1),Q(0)))),Q(2)),
    'S':(((O,Z),(Z,I)),Q(1)),
    'R':((((Q(2),Q(-1)),Z),(Z,(Q(2),Q(1)))),Q(5)),
    'r':((((Q(2),Q(1)),Z),(Z,(Q(2),Q(-1)))),Q(5))}
def rotate2(rho,g):
    u,d=U2[g];a=mul2(mul2(u,rho),adj2(u))
    return tuple(tuple(scale(x,1/d) for x in row) for row in a)
def project2(rho,a,s):
    p=density(tuple(s*x for x in AXES[a]))
    return mul2(mul2(p,rho),p)


def policy(kind,t,outcomes):
    if kind=='XXX':return ('M','X')
    if kind=='RXa':return [('U','R'),('M','X'),('M','a')][t]
    if kind=='adaptive':
        if t==0:return ('M','X')
        if t==1:return ('U','R' if outcomes[-1]==1 else 'H')
        return ('M','a' if outcomes[0]==1 else 'Z')
    if kind=='stop':
        if t==0:return ('M','X')
        if outcomes[0]==1:return ('STOP','stop')
        return ('M','a' if t==1 else 'Z')
    if kind=='RRr':return ('U',['R','R','r'][t])
    raise RuntimeError(kind)


def cq_tree(grid,terms,kind,kappa,chi):
    # Every term's preparation label is confined to this mathematical source
    # decomposition. Reads use only its actual geometric law and common setting.
    total=sum(w for w,n in terms)
    mean=tuple(sum((Q(w,total)*grid.mean(n)[j] for w,n in terms),Q(0)) for j in range(3))
    initial=density(tuple(ALPHA*x for x in mean))
    branches=[((),(),Q(1),terms,EYE,initial,False)]
    nodes=0;zeros=0
    for t in range(HORIZON):
        nxt=[]
        for record,outs,p,source,R,rho,stopped in branches:
            op,arg=('STOP','stop') if stopped else policy(kind,t,outs)
            if op=='U':
                nxt.append((record+((t,op,arg,1),),outs,p,source,mm(ROT[arg],R),rotate2(rho,arg),False));nodes+=1
            elif op=='STOP':
                nxt.append((record+((t,op,arg,1),),outs,p,source,R,rho,True));nodes+=1
            else:
                den=sum(w for w,n in source)
                for s in (1,-1):
                    prob=sum((Q(w,den)*grid.probability(n,R,arg,s) for w,n in source),Q(0))
                    target=project2(rho,arg,s)
                    reset=[(1,tuple(s*x for x in AXES[arg]))]
                    nxt.append((record+((t,op,arg,s,1),),outs+(s,),p*prob,reset,EYE,target,False));nodes+=1
                    if p*prob==0 or trace(target)==0:zeros+=1
        branches=nxt
    check(sum(b[2] for b in branches)==1,'all source branches retained')
    check(sum(trace(b[5]) for b in branches)==1,'all quantum branches retained')
    lo=Q(0);hi=Q(0);recordtv=Q(0)
    for record,outs,p,source,R,rho,stopped in branches:
        check(len(record)==HORIZON,'total public tick budget')
        den=sum(w for w,n in source)
        m=tuple(sum((Q(w,den)*grid.mean(n)[i] for w,n in source),Q(0)) for i in range(3))
        rr=tuple(ALPHA*x for x in mv(R,m));check(dot(rr,rr)<=1,'outgoing fixed decoder positive')
        diff=tuple(p*rr[i]-bloch(rho)[i] for i in range(3))
        dl,du=roots(dot(diff,diff));mass=abs(p-trace(rho))
        lo+=max(mass,dl)/2;hi+=max(mass,du)/2;recordtv+=mass/2
    bound=min(Q(1),HORIZON*kappa+2*chi)
    check(hi<=bound,'complete fixed-decoder adaptive CQ certificate')
    return {'nodes':nodes,'leaf_records':len(branches),'zero_mass_nodes':zeros,
      'record_tv':str(recordtv),'cq_lower':str(lo),'cq_upper':str(hi)}


def controls(grid,cert):
    count=Counter();maxcq=Q(0);maxrecord=Q(0)
    for name,n in PREP.items():
        for g,R in ROT.items():
            check(bloch(rotate2(density(n),g))==mv(R,n),'independent complex rotation control')
            count['independent_matrix_rotation_cases']+=1
    mixtures=[[(1,n)] for n in PREP.values()]
    mixtures.extend([[(1,AXES['X']),(1,minus(AXES['X']))],
                     [(1,AXES['Z']),(1,minus(AXES['Z']))],
                     [(1,BASE['p']),(1,BASE['q'])],
                     [(1,minus(BASE['p'])),(1,minus(BASE['q']))]])
    for terms in mixtures:
        for kind in ('XXX','RXa','adaptive','stop','RRr'):
            x=cq_tree(grid,terms,kind,Q(cert['kappa']),Q(cert['chi_upper']))
            maxcq=max(maxcq,Q(x['cq_upper']));maxrecord=max(maxrecord,Q(x['record_tv']))
            count['adaptive_protocol_input_cases']+=1
            for k in ['nodes','leaf_records','zero_mass_nodes']:count[k]+=x[k]
    inverse=mm(ROT['r'],ROT['R']);check(inverse==EYE,'inverse exact words')
    for n in PREP.values():
        check(mv(inverse,grid.mean(n))==grid.mean(n),'no geometric unitary drift')
        count['inverse_word_cases']+=1

    # Separate small finite sampler for independently affordable seed exhaustion.
    small=Geometry(8,10,10);n=AXES['Z'];counts=small.counts(n);cuts=[];cum=0
    for c in counts:cum+=c;cuts.append(cum)
    actual=[0]*small.N
    for seed in range(small.K):
        i=next(j for j,cut in enumerate(cuts) if seed<cut)
        check(i==small.index(n,seed),'full scan versus binary sampler')
        check(small.index(minus(n),seed)==small.anti[i],'pointwise antipodal sampler mirror')
        actual[i]+=1
    check(tuple(actual)==counts,'all small fair seeds exhausted')
    count['exhausted_small_fair_seeds']=small.K
    fresh=Counter();reused=Counter()
    for sx in (1,-1):
        p=small.probability(n,EYE,'X',sx);post=tuple(sx*x for x in AXES['X'])
        for sz in (1,-1):fresh[sx,sz]=p*small.probability(post,EYE,'Z',sz)
    for seed in range(small.K):
        i=small.index(n,seed);sx=1 if small.z[i][0]>=0 else -1
        j=small.index(tuple(sx*x for x in AXES['X']),seed);sz=1 if small.z[j][2]>=0 else -1
        reused[sx,sz]+=Q(1,small.K)
    reuse=sum((abs(fresh[k]-reused[k]) for k in product((1,-1),repeat=2)),Q(0))/2
    check(reuse>0,'reset-seed reuse detected')
    adapt=Q(0)
    for sx in (1,-1):
        p=small.probability(n,EYE,'X',sx);post=tuple(sx*x for x in AXES['X']);a='Z' if sx==1 else 'a'
        for s in (1,-1):adapt+=abs(p*small.probability(post,EYE,a,s)-p*small.probability(post,EYE,'Z',s))/2
    check(adapt>0,'ignored adaptive setting detected')
    failure=small.probability(n,EYE,'X',-1);check(failure>0,'missing reset block gives real failure')
    cx=tuple(a+b for a,b in zip(grid.counts(AXES['X']),grid.counts(minus(AXES['X']))))
    cz=tuple(a+b for a,b in zip(grid.counts(AXES['Z']),grid.counts(minus(AXES['Z']))))
    check(tuple(grid.mean(AXES['X'])[j]+grid.mean(minus(AXES['X']))[j] for j in range(3))==(Q(0),)*3,'antipodal X zero mean')
    check(tuple(grid.mean(AXES['Z'])[j]+grid.mean(minus(AXES['Z']))[j] for j in range(3))==(Q(0),)*3,'antipodal Z zero mean')
    private=sum((abs(Q(a,2*grid.K)-Q(b,2*grid.K)) for a,b in zip(cx,cz)),Q(0))/2
    px=sum(c for c,z in zip(cx,grid.z) if abs(z[0])>abs(z[2]))
    pz=sum(c for c,z in zip(cz,grid.z) if abs(z[0])>abs(z[2]))
    timing=abs(Q(px-pz,2*grid.K))
    check(private>0 and timing>0,'private access/timing countercontrols')
    return {'counts':dict(sorted(count.items())), 'maximum_checked_CQ_upper':str(maxcq),
      'maximum_checked_record_TV':str(maxrecord),'reused_seed_TV':str(reuse),
      'ignored_adaptive_setting_TV':str(adapt),'insufficient_bank_failure_mass':str(failure),
      'private_carrier_TV':str(private),'private_timing_TV':str(timing)}


def resources(grid):
    h=HORIZON;words=sum(len(ROT)**j for j in range(h+1));labels=grid.N*words
    return {'horizon':h,'preparation_rays':len(PREP),'measurement_axes':len(AXES),
      'rotation_generators':len(ROT),'formal_words_through_h':words,
      'carrier_word_label_upper_bound':labels,'carrier_label_bits_upper_bound':(labels-1).bit_length(),
      'clock_bits':h.bit_length(),'initial_fair_bits_excluding_mixture':(h+1)*grid.B,
      'distinct_source_CDFs':len(PREP),'CDF_table_bits_upper_bound':len(PREP)*grid.N*(grid.B+1),
      'response_table_bits_upper_bound':len(AXES)*labels,
      'retained_old_carrier_registers_upper_bound':h,
      'native_implementation':False,'finite_menu_horizon_certificate':True}


def main():
    attempts=[];selected=None;cert=None
    for M in (8,16,32,64):
        g=Geometry(M);c=envelope(g);attempts.append(c);selected=g;cert=c
        if c['within_one_tenth']:break
    check(selected is not None,'bounded parameter sequence executed')
    out={'schema':'oi.finite-menu-a2-envelope-v6.v1','attempts':attempts,
      'selected':cert,'resources':resources(selected),'controls':controls(selected,cert),
      'scope':'Specified finite rational qubit menus and total h=3 horizon; one fixed positive decoder, supplied geometric probabilities/private reset/clock. No native sourcing, arbitrary-menu theorem or full OI equivalence.',
      'verdict':'PASS_EXECUTED_FINITE_MENU_A2_ONE_TENTH' if cert['within_one_tenth'] else 'PASS_SCOPED_FINITE_MENU_TRADEOFF_THRESHOLD_NOT_REACHED'}
    print(json.dumps(out,sort_keys=True,separators=(',',':')))


if __name__=='__main__':main()
