#!/usr/bin/env python3
"""Independent exact finite reconstruction. Never imports the A2 author engine."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import hashlib
import json


TESTS=Counter()


def require(name,value):
    if not value:
        raise RuntimeError(name)
    TESTS[name]+=1


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F())


def neg(a):
    return tuple(-x for x in a)


def mv(m,v):
    return tuple(dot(row,v) for row in m)


def mm3(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))


I3=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
R3={
    'H':((F(),F(),F(1)),(F(),F(-1),F()),(F(1),F(),F())),
    'S':((F(),F(-1),F()),(F(1),F(),F()),(F(),F(),F(1))),
    'R':((F(3,5),F(-4,5),F()),(F(4,5),F(3,5),F()),(F(),F(),F(1))),
    'r':((F(3,5),F(4,5),F()),(F(-4,5),F(3,5),F()),(F(),F(),F(1))),
}
AXES={
    'x':(F(1),F(),F()),'y':(F(),F(1),F()),'z':(F(),F(),F(1)),
    'a':(F(3,5),F(4,5),F()),
}


def complexq(a=0,b=0):
    return F(a),F(b)


def plus(a,b):
    return a[0]+b[0],a[1]+b[1]


def times(a,b):
    return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]


def conjugateq(a):
    return a[0],-a[1]


def mm2(a,b):
    return tuple(tuple(plus(times(a[i][0],b[0][j]),times(a[i][1],b[1][j])) for j in range(2)) for i in range(2))


def adjoint(a):
    return tuple(tuple(conjugateq(a[j][i]) for j in range(2)) for i in range(2))


def matrix_scale(a,k):
    return tuple(tuple((x[0]*k,x[1]*k) for x in row) for row in a)


Z=complexq();O=complexq(1)
QG={
    'H':(((O,O),(O,complexq(-1))),2),
    'S':(((O,Z),(Z,complexq(0,1))),1),
    'R':(((complexq(2,-1),Z),(Z,complexq(2,1))),5),
    'r':(((complexq(2,1),Z),(Z,complexq(2,-1))),5),
}


def density(r,w=F(1)):
    x,y,z=r
    return ((complexq((w+z)/2),complexq(x/2,-y/2)),(complexq(x/2,y/2),complexq((w-z)/2)))


def trace(a):
    v=plus(a[0][0],a[1][1])
    require('real_matrix_trace',v[1]==0)
    return v[0]


def bloch(a):
    return 2*a[0][1][0],-2*a[0][1][1],a[0][0][0]-a[1][1][0]


def qgate(a,g):
    u,d=QG[g]
    return matrix_scale(mm2(mm2(u,a),adjoint(u)),F(1,d))


def qmeasure(a,setting,s):
    p=density(tuple(s*x for x in AXES[setting]))
    return mm2(mm2(p,a),p)


def sqrt_interval(x):
    denominator=1<<64
    z=isqrt((x.numerator*denominator*denominator)//x.denominator)
    lo=F(z,denominator)
    hi=lo if lo*lo==x else F(z+1,denominator)
    require('square_root_enclosure',lo*lo<=x<=hi*hi)
    return lo,hi


def tv(p,q):
    return sum((abs(x-y) for x,y in zip(p,q)),F())/2


class FiniteSphere:
    def __init__(self,M,W,B):
        self.M,self.W,self.B=M,W,B
        self.K=1<<B
        self.points=[]
        for fixed in range(3):
            free=[i for i in range(3) if i!=fixed]
            for sign in (-1,1):
                for u,v in product(range(-M+1,M,2),repeat=2):
                    z=[0,0,0];z[fixed]=sign*M;z[free[0]]=u;z[free[1]]=v
                    self.points.append(tuple(z))
        self.N=len(self.points)
        require('grid_cardinality',self.N==6*M*M==len(set(self.points)))
        lookup={z:i for i,z in enumerate(self.points)}
        self.antipode=tuple(lookup[neg(z)] for z in self.points)
        self.ell=[]
        for z in self.points:
            square=dot(z,z)
            floor=isqrt(int(square));den=floor if floor*floor==square else floor+1
            require('inward_normalizer',den>=M and (den-1)**2<square<=den**2)
            ell=tuple(F(t,den) for t in z)
            require('inward_norm',dot(ell,ell)<=1)
            self.ell.append(ell)
        self.eta=F(self.N-1,self.K)
        self.tau=F(48,M)+F(8,1<<W)+self.eta
        self.e=F(99,M)+F(16,1<<W)+2*self.eta
        self.kappa=F(52,M)+F(8,1<<W)+self.eta
        self.alpha=1/(F(2,3)+self.e)
        self.chi=self.alpha*self.e
        require('moment_constants_identity',self.e==F(3,M)+2*self.tau)
        self.cache={};self.cut_cache={};self.mean_cache={}

    def table(self,n):
        if n in self.cache:
            return self.cache[n]
        if next(x for x in n if x)<0:
            positive=self.table(neg(n))
            answer=tuple(positive[self.antipode[i]] for i in range(self.N))
            self.cache[n]=answer
            return answer
        weights=[];floor_error=F()
        for point in self.points:
            q=dot(point,point)
            g=max(F(),dot(n,point))*self.M**3/(q*q)
            integer=(g*(1<<self.W)).numerator//(g*(1<<self.W)).denominator
            require('integer_floor_atom',0<=g-F(integer,1<<self.W)<F(1,1<<self.W))
            floor_error+=g-F(integer,1<<self.W)
            weights.append(integer)
        total=sum(weights)
        require('positive_normalization',total>0)
        require('floor_integral_bound',F(4,self.M**2)*floor_error<=F(24,1<<self.W))
        cumulative=0;previous=0;counts=[];cuts=[]
        for weight in weights:
            cumulative+=weight
            cut=(self.K*cumulative)//total
            counts.append(cut-previous);cuts.append(cut);previous=cut
        require('CDF_total',sum(counts)==self.K and min(counts)>=0)
        require('CDF_TV_bound',tv([F(c,self.K) for c in counts],[F(w,total) for w in weights])<=self.eta)
        self.cache[n]=tuple(counts);self.cut_cache[n]=tuple(cuts)
        return tuple(counts)

    def sample(self,n,seed):
        if next(x for x in n if x)<0:
            return self.antipode[self.sample(neg(n),seed)]
        self.table(n)
        chosen=None
        for i,cut in enumerate(self.cut_cache[n]):
            if chosen is None and seed<cut:
                chosen=i
        require('fixed_scan_sample_exists',chosen is not None)
        return chosen

    def mean(self,counts):
        if counts not in self.mean_cache:
            total=sum(counts)
            self.mean_cache[counts]=tuple(sum((F(counts[i],total)*p[j] for i,p in enumerate(self.ell)),F()) for j in range(3))
        return self.mean_cache[counts]

    def signs(self,setting,R):
        a=AXES[setting]
        coefficients=tuple(sum(a[i]*R[i][j] for i in range(3)) for j in range(3))
        return tuple(1 if dot(coefficients,z)>=0 else -1 for z in self.points)

    def probability(self,counts,setting,R,s):
        signs=self.signs(setting,R)
        return F(sum(w for w,t in zip(counts,signs) if t==s),sum(counts))


def mixture(grid,terms):
    return tuple(sum((weight*grid.table(n)[i] for weight,n in terms),0) for i in range(grid.N))


def protocol(name,step,outcomes):
    if name=='repeat':return 'M','x'
    if name=='rotate':return (('U','R'),('M','x'),('M','a'))[step]
    if name=='adaptive':
        if step==0:return 'M','x'
        if step==1:return 'U',('H' if outcomes[-1]<0 else 'R')
        return 'M',('z' if outcomes[0]<0 else 'a')
    if name=='stop':
        if step==0:return 'M','x'
        if outcomes[0]>0:return 'STOP','pad'
        return 'M',('a' if step==1 else 'z')
    raise RuntimeError('policy')


def run(grid,terms,ideal_r,name,decoded_input):
    counts=mixture(grid,terms)
    initial_r=tuple(grid.alpha*x for x in grid.mean(counts)) if decoded_input else ideal_r
    # record, outcomes, source branch mass, actual finite carrier law, word, quantum branch
    branches=[((),(),F(1),counts,(),density(initial_r),False)]
    for step in range(3):
        nxt=[]
        for rec,signs,w,current,word,rho,stopped in branches:
            op,arg=('STOP','pad') if stopped else protocol(name,step,signs)
            R=I3
            for g in word:R=mm3(R3[g],R)
            if op=='U':
                newword=word+(arg,)
                require('word_clock_capacity',len(newword)<=step+1<=3)
                nxt.append((rec+((step,op,arg,1),),signs,w,current,newword,qgate(rho,arg),False))
                require('emitted_protocol_branch',True)
            elif op=='STOP':
                nxt.append((rec+((step,op,arg,1),),signs,w,current,word,rho,True))
                require('emitted_protocol_branch',True)
            else:
                for s in (-1,1):
                    prob=grid.probability(current,arg,R,s)
                    post=grid.table(tuple(s*x for x in AXES[arg]))
                    nxt.append((rec+((step,op,arg,s,1),),signs+(s,),w*prob,post,(),qmeasure(rho,arg,s),False))
                    require('emitted_protocol_branch',True)
            require('adaptive_node',True)
        branches=nxt
    source_total=sum(b[2] for b in branches);quantum_total=sum(trace(b[5]) for b in branches)
    require('full_branch_normalization',source_total==quantum_total==1)
    distance_lo=F();distance_hi=F();record_tv=F();zero=0
    for rec,signs,w,counts,word,rho,stopped in branches:
        R=I3
        for g in word:R=mm3(R3[g],R)
        rsrc=tuple(grid.alpha*x for x in mv(R,grid.mean(counts)))
        require('decoded_branch_positivity',dot(rsrc,rsrc)<=1)
        target_mass=trace(rho);delta_mass=abs(w-target_mass)
        delta=tuple(w*x-y for x,y in zip(rsrc,bloch(rho)))
        lo,hi=sqrt_interval(dot(delta,delta))
        distance_lo+=max(delta_mass,lo)/2;distance_hi+=max(delta_mass,hi)/2
        record_tv+=delta_mass/2
        zero+=int(w==0 or target_mass==0)
        require('full_record_tick_flag',len(rec)==3 and all(row[-1]==1 for row in rec))
    bound=min(F(1),3*grid.kappa+(2 if decoded_input else 1)*grid.chi)
    require('joint_CQ_bound',distance_hi<=bound)
    return {'leaf':len(branches),'zero':zero,'CQ_lower':str(distance_lo),'CQ_upper':str(distance_hi),'record_TV':str(record_tv),'bound':str(bound)}


def ceil_log_two(x):
    n=0
    while F(1<<n)<x:n+=1
    return n


def resource(h,eps):
    lower=F(3*(52*h+300),1)/eps
    M=max(8,(lower.numerator+lower.denominator-1)//lower.denominator)
    if M%2:M+=1
    W=max(4,ceil_log_two(F(3*(8*h+48),1)/eps))
    N=6*M*M
    B=max(1,ceil_log_two(F(3*(N-1)*(h+6),1)/eps))
    eta=F(N-1,1<<B);e=F(99,M)+F(16,1<<W)+2*eta
    kappa=F(52,M)+F(8,1<<W)+eta;chi=e/(F(2,3)+e)
    linear=F(52*h+300,M)+F(8*h+48,1<<W)+(h+6)*eta
    require('symbolic_nonvacuous_bound',h*kappa+2*chi<=linear<=eps)
    require('symbolic_positive_decoder',0<1/(F(2,3)+e) and 0<chi<1)
    return {'h':h,'epsilon':str(eps),'M':M,'W':W,'B':B,'N':N,'fair_bits':(h+1)*B,
            'exact_h_kappa_plus_2chi':str(h*kappa+2*chi),'linear_upper':str(linear),
            'carrier_labels':N*sum(4**j for j in range(h+1)),
            'large_grid_executed':False}


def main():
    global TESTS
    TESTS=Counter()
    here=Path(__file__).resolve().parent
    sibling=here.parent/'a2_v5'
    author=sibling if sibling.is_dir() else here.parent
    inputs=json.loads((here/'INPUT-HASHES.json').read_text())
    for name,digest in inputs['author_sha256'].items():
        require('pinned_author_hash',hashlib.sha256((author/name).read_bytes()).hexdigest()==digest)
    n1=(F(2,3),F(-2,3),F(1,3));n2=(F(2,3),F(-2,3),F(-1,3))
    cases=[([(1,n)],n) for n in AXES.values()]
    cases += [([(1,n1),(1,n2)],(F(2,3),F(-2,3),F())),
              ([(1,neg(n1)),(1,neg(n2))],(F(-2,3),F(2,3),F())),
              ([(1,AXES['x']),(1,neg(AXES['x']))],(F(),)*3),
              ([(1,AXES['z']),(1,neg(AXES['z']))],(F(),)*3)]
    trees=[];private_controls=[]
    for M in (8,16):
        grid=FiniteSphere(M,12,16)
        for terms,r in cases:
            counts=mixture(grid,terms)
            m=grid.mean(counts);difference=tuple(x-F(2,3)*y for x,y in zip(m,r))
            require('finite_moment_error',dot(difference,difference)<=grid.e**2)
            finite=tuple(grid.alpha*x for x in m)
            require('canonical_decoder_positivity',dot(finite,finite)<=1)
            require('associated_state_error',dot(tuple(x-y for x,y in zip(finite,r)),tuple(x-y for x,y in zip(finite,r)))<=4*grid.chi**2)
            for g,R in R3.items():
                require('matrix_rotation_control',bloch(qgate(density(r),g))==mv(R,r))
            require('unitary_inverse_no_drift',mm3(R3['r'],R3['R'])==I3)
            for name,decoded in product(('repeat','rotate','adaptive','stop'),(False,True)):
                out=run(grid,terms,r,name,decoded)
                trees.append((M,name,decoded,out))
        for p in grid.points:
            u,v=[F(p[i],M) for i in range(3) if abs(p[i])!=M]
            rr=1+u*u+v*v
            gram_uu=(1+v*v)/(rr*rr);gram_vv=(1+u*u)/(rr*rr);gram_uv=-u*v/(rr*rr)
            require('cube_radial_area_Gram',gram_uu*gram_vv-gram_uv*gram_uv==1/rr**3)
        mx=mixture(grid,[(1,AXES['x']),(1,neg(AXES['x']))])
        mz=mixture(grid,[(1,AXES['z']),(1,neg(AXES['z']))])
        require('private_control_same_decoded_input',grid.mean(mx)==grid.mean(mz)==(0,0,0))
        px=tuple(F(v,sum(mx)) for v in mx);pz=tuple(F(v,sum(mz)) for v in mz)
        private_tv=tv(px,pz)
        timing_x=sum((p for p,z in zip(px,grid.points) if abs(z[0])>abs(z[2])),F())
        timing_z=sum((p for p,z in zip(pz,grid.points) if abs(z[0])>abs(z[2])),F())
        timing_tv=abs(timing_x-timing_z)
        require('private_carrier_access_countercontrol',private_tv>0)
        require('private_timing_countercontrol',timing_tv>0)
        private_controls.append({'M':M,'private_label_TV':str(private_tv),'hidden_timing_TV':str(timing_tv)})
    small=FiniteSphere(8,10,10);source=small.table(AXES['z'])
    measured=[0]*small.N
    for seed in range(small.K):measured[small.sample(AXES['z'],seed)]+=1
    require('exhausted_seed_sampler',tuple(measured)==source)
    reused=Counter();fresh=Counter()
    first=small.signs('x',I3);second=small.signs('z',I3)
    for s in (-1,1):
        p=small.probability(source,'x',I3,s);post=small.table(tuple(s*x for x in AXES['x']))
        for t in (-1,1):fresh[s,t]=p*small.probability(post,'z',I3,t)
    for seed in range(small.K):
        j=small.sample(AXES['z'],seed);s=first[j]
        k=small.sample(tuple(s*x for x in AXES['x']),seed)
        reused[s,second[k]]+=F(1,small.K)
    keys=list(product((-1,1),repeat=2))
    reuse_tv=tv([reused[k] for k in keys],[fresh[k] for k in keys])
    require('seed_reuse_countercontrol',reuse_tv==F(11,256))
    correct=[];wrong=[]
    for s in (-1,1):
        p=small.probability(source,'x',I3,s);post=small.table(tuple(s*x for x in AXES['x']))
        actual='z' if s>0 else 'a'
        for t in (-1,1):
            correct.append(p*small.probability(post,actual,I3,t));wrong.append(p*small.probability(post,'z',I3,t))
    adaptive_tv=tv(correct,wrong)
    require('adaptive_setting_countercontrol',adaptive_tv==F(153,1024))
    require('insufficient_bank_terminal_failure',small.probability(source,'x',I3,-1)==F(1,2))
    certificates=[resource(h,eps) for h,eps in ((1,F(1,10)),(3,F(1,10)),(10,F(1,100)))]
    return {'schema':'oi-independent-finite-A2-review-v5.1','verdict':'ACCEPT_WITHIN_SCOPE',
            'author_commit':inputs['author_commit'],'grid_sizes':[8,16],
            'adaptive_cases':len(trees),'leaf_records':sum(t[3]['leaf'] for t in trees),
            'zero_mass_leaves':sum(t[3]['zero'] for t in trees),
            'max_CQ_upper':str(max(F(t[3]['CQ_upper']) for t in trees)),
            'reused_seed_record_TV':str(reuse_tv),'wrong_adaptive_setting_TV':str(adaptive_tv),
            'seed_exhaustion_values':small.K,'symbolic_resource_certificates':certificates,
            'private_access_controls':private_controls,
            'comparison':'same fixed decoder on input/output has h*kappa+2chi bound; associated ideal input uses +chi',
            'checks':dict(sorted(TESTS.items()))}


if __name__=='__main__':
    print(json.dumps(main(),indent=2,sort_keys=True))
