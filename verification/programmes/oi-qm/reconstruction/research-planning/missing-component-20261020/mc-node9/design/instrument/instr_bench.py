"""D6 instrument benchmark: a finite single-qubit instrument experiment, exact rational arithmetic.

Menu: sharp binary measurements X, Y, Z and R (axis (4/5, 3/5, 0)). Preparations: the eight menu eigenstates and
r_plus/r_minus = +-(1/2, 1/2, 0). The quantum reference uses Bloch calculus: P(+ | r, n) = (1 + n.r)/2, with the
post-measurement state +-n. Every quantity is rational. A candidate model is a finite outcome-labelled kernel:
hidden states, a preparation distribution for each label, and for each measurement and hidden state a list of
(outcome, next hidden state, probability). Retained outcomes live in an explicit record register; feedback reads
only that register.

Tests (all exact; depth-bounded, so a PASS is evidence for the stated depth only):
  T1 first read: every preparation x every menu measurement matches the reference.
  T2 repetition: m then m gives equal outcomes with probability 1, for every m and preparation.
  T3 sequences: every fixed measurement sequence of length <= 3 over the menu gives the reference joint outcome
     distribution, for every preparation. This covers every adaptive strategy of depth <= 3: along each outcome
     path an adaptive strategy applies a fixed sequence, so its probability for that path is that sequence's.
  T4 extra reads: with the candidate's declared extra accessible reads added to the menu, the optimal adaptive
     discrimination of depth <= 3 between any two preparations does not exceed the quantum trace distance
     |r1 - r2|/2. It is computed exactly by recursion over unnormalized hidden-state measures,
     V_d(a, b) = max_m sum_o V_{d-1}(a|m,o; b|m,o) and V_0 = |mass(a) - mass(b)|/2, and compared on squares.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

AX={'X':(F(1),F(0),F(0)),'Y':(F(0),F(1),F(0)),'Z':(F(0),F(0),F(1)),'R':(F(4,5),F(3,5),F(0))}
MENU=['X','Y','Z','R']
def neg(v): return tuple(-a for a in v)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
PREPS={}
for m,n in AX.items(): PREPS[m+'+']=n; PREPS[m+'-']=neg(n)
PREPS['r_plus']=(F(1,2),F(1,2),F(0)); PREPS['r_minus']=(F(-1,2),F(-1,2),F(0))

# ---- quantum reference (Bloch formula) ----
class Quantum:
    name='quantum reference'
    extra={}
    def prep(self,label): return {PREPS[label]:F(1)}
    def meas(self,m,r):
        n=AX[m]; p=(1+dot(n,r))/2
        return [(1,n,p),(0,neg(n),1-p)]

# ---- positive control: classical label plus seed, deterministic dilation ----
SEEDS=200          # one fresh uniform seed in range(200) per measurement; a counted resource
class LabelSeed:
    """Hidden state: the current label (a rational Bloch vector) and the record register. Each measurement
    draws one fresh seed s and applies a deterministic integer threshold rule. Quantum rules are imported on
    purpose: this control shows that the checker accepts correct sequential behaviour. It is not a candidate."""
    name='positive control: label + seed dilation (imports QM)'
    extra={}
    def prep(self,label): return {PREPS[label]:F(1)}
    def meas(self,m,r):
        n=AX[m]; num=(1+dot(n,r))*SEEDS/2
        assert num.denominator==1, 'seed alphabet too small for an exact threshold'
        thr=int(num); out=defaultdict(F)
        for s in range(SEEDS):
            o,nxt=(1,n) if s<thr else (0,neg(n))
            out[(o,nxt)]+=F(1,SEEDS)
        return [(o,nx,p) for (o,nx),p in out.items()]

# ---- countercontrols ----
class NoCollapse(Quantum):
    name='countercontrol: correct first read, no state update'
    def meas(self,m,r):
        n=AX[m]; p=(1+dot(n,r))/2
        return [(1,r,p),(0,r,1-p)]
class WrongUpdate(Quantum):
    name='countercontrol: R collapses to the X eigenstate'
    def meas(self,m,r):
        n=AX[m]; p=(1+dot(n,r))/2
        if m=='R': return [(1,AX['X'],p),(0,neg(AX['X']),1-p)]
        return [(1,n,p),(0,neg(n),1-p)]
class LabelLeak(Quantum):
    name='countercontrol: correct instruments plus an accessible preparation-label read'
    def prep(self,label): return {(PREPS[label],label):F(1)}
    def meas(self,m,state):
        r,lab=state
        if m=='L':                      # reveals whether the preparation was r_plus; leaves the state alone
            return [(1 if lab=='r_plus' else 0,state,F(1))]
        n=AX[m]; p=(1+dot(n,r))/2
        return [(1,(n,lab),p),(0,(neg(n),lab),1-p)]
    extra={'L':None}
class TripleCorr:
    """The owner's triple-correlation encoding (report10): hidden signs (x, y, z); r_plus/r_minus only.
    X, Y, Z read their sign sharply; R reads h = xyz through fresh noise (1 + 7h/10)/2; nothing is disturbed."""
    name='countercontrol: triple-correlation encoding, nondisturbing reads'
    extra={}
    preps=('r_plus','r_minus')
    def prep(self,label):
        s=1 if label=='r_plus' else -1
        return {(x,y,z):(1+s*F(x+y,2))/4 for x,y,z in product((1,-1),repeat=3) if z==s*x*y}
    def meas(self,m,l):
        x,y,z=l
        if m in 'XYZ':
            v={'X':x,'Y':y,'Z':z}[m]; return [(1 if v==1 else 0,l,F(1))]
        p=(1+F(7,10)*x*y*z)/2
        return [(1,l,p),(0,l,1-p)]

# ---- engine ----
def strategies(menu,depth):
    """Adaptive strategies as nested tuples (m, {outcome: substrategy})."""
    if depth==0: return [None]
    subs=strategies(menu,depth-1)
    return [(m,{0:a,1:b}) for m in menu for a in subs for b in subs]
_cache={}
def kernel(model,m,state):
    key=(id(model),m,state)
    if key not in _cache: _cache[key]=model.meas(m,state)
    return _cache[key]
def run(model,label,strat):
    dist=defaultdict(F)
    def go(state,strat,rec,pr):
        if strat is None: dist[rec]+=pr; return
        m,nxt=strat
        for o,s2,p in kernel(model,m,state):
            if p: go(s2,nxt[o],rec+(o,),pr*p)
    for h,p in model.prep(label).items(): go(h,strat,(),p)
    return dict(dist)
def tv(a,b): return sum((abs(a.get(k,F(0))-b.get(k,F(0))) for k in set(a)|set(b)),F(0))/2
def trace_dist_sq(r1,r2): return sum((a-b)**2 for a,b in zip(r1,r2))/4

def evaluate(model,ref=Quantum()):
    preps=getattr(model,'preps',tuple(PREPS))
    res={}
    # T1
    w=None
    for lab in preps:
        for m in MENU:
            s=(m,{0:None,1:None})
            if run(model,lab,s)!=run(ref,lab,s): w=w or (lab,m,run(model,lab,s),run(ref,lab,s))
    res['T1']=w
    # T2
    w=None
    for lab in preps:
        for m in MENU:
            d=run(model,lab,(m,{0:(m,{0:None,1:None}),1:(m,{0:None,1:None})}))
            bad=sum(p for k,p in d.items() if k[0]!=k[1])
            if bad: w=w or (lab,m,bad)
    res['T2']=w
    # T3: every fixed sequence of length <= 3
    w=None
    def seq_strat(seq):
        if not seq: return None
        sub=seq_strat(seq[1:]); return (seq[0],{0:sub,1:sub})
    for L in (1,2,3):
        for seq in product(MENU,repeat=L):
            st=seq_strat(seq)
            for lab in preps:
                if run(model,lab,st)!=run(ref,lab,st): w=w or (lab,seq); break
            if w: break
        if w: break
    res['T3']=w
    # T4: optimal adaptive discrimination, depth <= 3, every pair
    menu=MENU+list(model.extra)
    def push(mu,m,o):
        out=defaultdict(F)
        for h,p in mu.items():
            for oo,h2,q in kernel(model,m,h):
                if oo==o and q: out[h2]+=p*q
        return dict(out)
    def V(d,a,b):
        if d==0: return abs(sum(a.values(),F(0))-sum(b.values(),F(0)))/2
        return max(sum(V(d-1,push(a,m,o),push(b,m,o)) for o in (0,1)) for m in menu)
    w=None
    for i_,a in enumerate(preps):
        for b in preps[i_+1:]:
            g=V(3,model.prep(a),model.prep(b))
            assert isinstance(g,F)
            if g*g>trace_dist_sq(PREPS[a],PREPS[b]): w=w or (a,b,'optimal depth-3 gap',g)
    res['T4']=w
    return res

if __name__=='__main__':
    print(__doc__.strip().splitlines()[0])
    print('preparations',len(PREPS),'| menu',MENU,'| fixed sequences of length <= 3:',sum(4**L for L in (1,2,3)))
    expect={'quantum reference':'PPPP','positive control: label + seed dilation (imports QM)':'PPPP',
            'countercontrol: correct first read, no state update':'PFFF',
            'countercontrol: R collapses to the X eigenstate':'PFFP',
            'countercontrol: correct instruments plus an accessible preparation-label read':'PPPF',
            'countercontrol: triple-correlation encoding, nondisturbing reads':'PFFF'}
    allok=True
    MODELS=(Quantum(),LabelSeed(),NoCollapse(),WrongUpdate(),LabelLeak(),TripleCorr())
    for M in MODELS:
        r=evaluate(M); got=''.join('P' if r[t] is None else 'F' for t in ('T1','T2','T3','T4'))
        ok=got==expect[M.name]; allok&=ok
        print(('ok  ' if ok else 'BAD ')+M.name+': T1..T4 = '+got)
        for t in ('T1','T2','T3','T4'):
            if r[t] is not None: print('      %s witness: %s'%(t,str(r[t])[:160]))
    print('PASS: every model classified as declared.' if allok else 'FAIL: a control is misclassified; the benchmark is void.')
