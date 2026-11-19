# Reviewer probe (exact, not evidence). Independent re-implementation of r6's model of P
# (no code shared with probes-r6/p_native.py). Purpose: (1) reproduce the four arms;
# (2) measure the native DISTURBANCE of each arm: the law of the kick dx = x_after(t2) - x_before(t2)
# on the carrier's encoded x; (3) sham variants; (4) eraser sorting on the marker AND on the dephasing
# arm; (5) a composite fixture (P2-departure sharp marker + hidden-sector cell) through decide-p.
# Model: F_2 cells (u,v); armed: u_i' = sum_{j armed with i} u_j + v_i, v_i' = u_i; unarmed: swap.
# Schedule: t0 c-p; t1 free; t2 c-arm cells (unless off); t3 c-s; port = u_s. Encoded frame:
# (z,x) = (u,v) at even t, (v,u) at odd t. Supplies are stated AT their coupling tick.
import itertools
from fractions import Fraction as Fr
U='?'
def run(src, phi, arm_cells, armed=True):
    # arm_cells: list of (u,v) supplies at t2; U = unknown uniform
    cz,cx = {'X+':(U,0),'X-':(U,1),'Z+':(0,U),'Z-':(1,U),'L':(U,U)}[src]
    slots=[cz,cx, phi,U]               # carrier (u,v)=(z,x) at t0; phase cell (phi, ?) at t0
    for (a,b) in arm_cells: slots+=[a,b]   # given at t2; two free ticks before t2 = identity
    slots+=[0,U]                       # screen: (w_s,0) at t3 -> three free ticks before -> (0,w_s) at t0
    unk=[i for i,s in enumerate(slots) if s==U]
    out={}
    for bits in itertools.product((0,1),repeat=len(unk)):
        s=list(slots)
        for i,b in zip(unk,bits): s[i]=b
        c=[s[0],s[1]]; p=[s[2],s[3]]; A=[[s[4+2*k],s[5+2*k]] for k in range(len(arm_cells))]
        sc=[s[-2],s[-1]]
        # t0: c-p armed; others free
        c,p = [(p[0]+c[1])%2, c[0]], [(c[0]+p[1])%2, p[0]]
        sc=[sc[1],sc[0]]; A=[[a[1],a[0]] for a in A]
        # t1: all free
        c=[c[1],c[0]]; p=[p[1],p[0]]; sc=[sc[1],sc[0]]; A=[[a[1],a[0]] for a in A]
        x_before=c[1]; z_before=c[0]          # even tick t2: encoded (z,x)=(u,v)
        if armed and A:
            ku=sum(a[0] for a in A)%2
            A=[[(c[0]+a[1])%2, a[0]] for a in A]
            c=[(ku+c[1])%2, c[0]]
        else:
            c=[c[1],c[0]]; A=[[a[1],a[0]] for a in A]
        p=[p[1],p[0]]; sc=[sc[1],sc[0]]
        x_after=c[0]; z_after=c[1]            # odd tick t3: encoded (z,x)=(v,u)
        # t3: c-s armed
        port=(c[0]+sc[1])%2
        c=[(sc[0]+c[1])%2, c[0]]
        A=[[a[1],a[0]] for a in A]           # held arm cells tick freely
        key=(port, tuple(tuple(a) for a in A), (x_after-x_before)%2, z_after==z_before)
        out[key]=out.get(key,0)+Fr(1,2**len(unk))
    return out
def P0(src,phi,cells,armed=True): return sum(w for k,w in run(src,phi,cells,armed).items() if k[0]==0)
def V(cells,armed=True): return abs(P0('X+',0,cells,armed)-P0('X+',1,cells,armed))
def held(src,cells,armed=True):
    d={}
    for k,w in run(src,0,cells,armed).items(): d[k[1]]=d.get(k[1],0)+w
    return d
def tv(a,b): return sum(abs(a.get(k,0)-b.get(k,0)) for k in set(a)|set(b))/2
def D(cells,armed=True): return tv(held('Z+',cells,armed),held('Z-',cells,armed))
def kick(cells,armed=True):
    d={}
    for k,w in run('X+',0,cells,armed).items(): d[k[2]]=d.get(k[2],0)+w
    return {k:str(v) for k,v in sorted(d.items())}
def nonabs(cells,armed=True): return all(k[3] for src in ('Z+','Z-') for k in run(src,0,cells,armed))
def spi(cells,armed=True): return all(P0(s,f,cells,armed)==P0(s,f,[(U,0)],False) for s in ('Z+','Z-') for f in (0,1))
ARMS={'off':([(U,0)],False),'marker (U,0)':([(U,0)],True),'sham (0,U)':([(0,U)],True),
      'sham1 (1,U) known kick':([(1,U)],True),'dephasing (U,U)':([(U,U)],True),'sharp (0,0)':([(0,0)],True),
      'composite sharp+deph':([(0,0),(U,U)],True),'two markers':([(U,0),(U,0)],True),'marker+sham':([(U,0),(0,U)],True)}
print('arm | V | D | kick law (dx) | s(X+,0) s(X+,1) | NONABS | SPI')
for n,(cells,ar) in ARMS.items():
    print(n,'|',V(cells,ar),'|',D(cells,ar),'|',kick(cells,ar),'|',P0('X+',0,cells,ar),P0('X+',1,cells,ar),'|',nonabs(cells,ar),'|',spi(cells,ar))
# exhaustive: every single fresh supply of one cell at t2 (each slot in {0,1,U})
print('\nall single-cell supplies (u,v): V, D, kick')
for a in (0,1,U):
    for b in (0,1,U):
        print((a,b), V([(a,b)]), D([(a,b)]), kick([(a,b)]))
# eraser: sort the screen on each held slot, for the marker and the dephasing arm
print('\neraser sorting (X+): conditional V per held-slot value; unsorted V')
for n,cells in (('marker',[(U,0)]),('dephasing',[(U,U)])):
    for slot,sn in ((0,'held u'),(1,'held v')):
        res=[]
        for val in (0,1):
            p=[]
            for phi in (0,1):
                L=run('X+',phi,cells); tot=sum(w for k,w in L.items() if k[1][0][slot]==val)
                p.append(sum(w for k,w in L.items() if k[1][0][slot]==val and k[0]==0)/tot)
            res.append(abs(p[0]-p[1]))
        print(n,sn,'conditional V =',[str(r) for r in res],'unsorted V =',V(cells))
# decide-p (r6 rule, first match) on the composite fixture as the 'on' arm, with r6's sham and dephasing arms
def decide(on):
    off=([(U,0)],False); sham=[(0,U)]; deph=[(U,U)]
    if not (nonabs(on) and spi(on) and nonabs(sham) and spi(sham) and nonabs(deph) and spi(deph)): return 'P-VOID'
    if D(sham)!=0 or D(deph)!=0: return 'P-VOID'
    Voff=V(*off)
    if Voff==0: return 'P-NO-FRINGES'
    if D(on)==0: return 'P-NO-RECORD'
    if V(on)==Voff: return 'P-NO-SUPPRESSION'
    if V(sham)<Voff: return 'P-SUPPRESSION-UNATTRIBUTED'
    if V(on)**2+D(on)**2>1: return 'P-COMPLEMENTARITY-FAIL'
    return 'P-TRANSITION'
print('\ndecide-p: marker ->',decide([(U,0)]),'; composite sharp+deph ->',decide([(0,0),(U,U)]),'; sharp ->',decide([(0,0)]))
