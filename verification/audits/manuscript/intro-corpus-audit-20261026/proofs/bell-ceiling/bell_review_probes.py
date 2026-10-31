"""Independent review probes for Main 3.3 Bell ceiling. Exact arithmetic (Fraction)."""
from fractions import Fraction as F
import itertools as it, math

SET=[(0,0),(0,1),(1,0),(1,1)]
def chsh(E): return E[(0,0)]+E[(0,1)]+E[(1,0)]-E[(1,1)]
pm=lambda x: 1-2*x   # bit -> +-1

# ---------- C0: reference: theorem's reduction on a finite lattice with read-local interventions
# Finite V, generic phi given by explicit local dependency; verify cone lemma exhaustively
# for a random bijective-ish map defined by local rules on a ring, and that responses factorize.
import random
random.seed(1)
N=8  # ring of bits
def phi(s):
    # reversible second-order-like rule: s'_i = s_i XOR (s_{i-1} AND s_{i+1}) on even then odd sublattice
    s=list(s)
    for par in (0,1):
        t=s[:]
        for i in range(par,N,2):
            t[i]=s[i]^(s[(i-1)%N]&s[(i+1)%N])
        s=t
    return tuple(s)
states=list(it.product((0,1),repeat=N))
assert len(set(map(phi,states)))==2**N   # bijection
# coupling graph by one-step dependency
dep={i:set() for i in range(N)}
for s in states:
    o=phi(s)
    for j in range(N):
        s2=list(s); s2[j]^=1; o2=phi(tuple(s2))
        for i in range(N):
            if o[i]!=o2[i]: dep[i].add(j)
adj={i:set() for i in range(N)}
for i in dep:
    for j in dep[i]:
        if i!=j: adj[i].add(j); adj[j].add(i)
def dist(i,j):
    from collections import deque
    d={i:0}; q=deque([i])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in d: d[v]=d[u]+1; q.append(v)
    return d.get(j,10**9)
def phik(s,k):
    for _ in range(k): s=phi(s)
    return s
cone_ok=True
for k in range(0,4):
    for i in range(N):
        for j in range(N):
            if dist(i,j)>k:
                for s in states:
                    s2=list(s); s2[j]^=1
                    if phik(s,k)[i]!=phik(tuple(s2),k)[i]: cone_ok=False
print("C0 cone lemma exhaustive on finite reversible ring (N=8,k<=3):",cone_ok, "graph degree", {i:len(adj[i]) for i in range(N)})

# ---------- CE2: intervention that WRITES only in B but READS A (sequential composition)
# V={1,2,3,4}, A={1,2}, B={3,4}; phi=identity => coupling graph edgeless, cones never meet.
def run_CE2(lam,a,b):
    s={1:0,2:lam,3:lam,4:0}
    s[1]=a                       # iota_a: writes/reads only A
    s[4]=b; s[3]=s[3]^(b & s[1]) # iota_b: writes only B, reads site 1 in A
    return pm(s[2]), pm(s[3])     # readouts local to A, B
E={z:sum(F(1,2)*run_CE2(l,*z)[0]*run_CE2(l,*z)[1] for l in (0,1)) for z in SET}
print("CE2 write-local / read-nonlocal intervention: CHSH =",chsh(E), " p(Omega|a,b) uniform; graph edgeless")
# same with simultaneous application (iota_b reads PRE-setting state) -> local
def run_CE2s(lam,a,b):
    s0={1:0,2:lam,3:lam,4:0}; s=dict(s0)
    s[1]=a; s[4]=b; s[3]=s0[3]^(b & s0[1])
    return pm(s[2]),pm(s[3])
E={z:sum(F(1,2)*run_CE2s(l,*z)[0]*run_CE2s(l,*z)[1] for l in (0,1)) for z in SET}
print("CE2' simultaneous (pre-setting reads): CHSH =",chsh(E))

# ---------- CE3: nonlocal readout map (readout of B reads A's setting register)
def run_CE3(lam,a,b):
    s={1:a,2:lam,3:lam,4:b}
    return pm(s[2]), pm(s[3]^(s[1]&s[4]))
E={z:sum(F(1,2)*run_CE3(l,*z)[0]*run_CE3(l,*z)[1] for l in (0,1)) for z in SET}
print("CE3 readout function not localized: CHSH =",chsh(E))

# ---------- CE4: post-selection (no-click) with local deterministic tables, MI holds
# outcomes in {-1,0,+1}; 0 = no detection.  Classic: A always clicks only for a==lam_bit etc.
tables=[]
best=None
vals=(-1,0,1)
# search over mixtures of point tables of the form (q0,q1,r0,r1) with uniform weight over a small family
fam=list(it.product(vals,repeat=4))
def coinc_chsh(weights):
    E={}
    for (a,b) in SET:
        num=sum(w*t[a]*t[2+b] for t,w in weights)
        den=sum(w for t,w in weights if t[a]!=0 and t[2+b]!=0)
        if den==0: return None
        E[(a,b)]=F(num)/den
    return chsh(E)
# explicit known construction: each lambda clicks on exactly one setting per wing
fam2=[t for t in fam if (t[0]==0)!=(t[1]==0) and (t[2]!=0 and t[3]!=0)]
best=F(0)
for combo in it.combinations(fam2,2):
    v=coinc_chsh([(t,F(1,2)) for t in combo])
    if v is not None and v>best: best=v
for combo in it.combinations(fam2,3):
    v=coinc_chsh([(t,F(1,3)) for t in combo])
    if v is not None and v>best: best=v
print("CE4 post-selected on coincidences, MI + local deterministic tables (A detection eff 1/2): max CHSH found =",best)
# unconditioned S with 0 allowed: bound 2
worst=max(abs(t[0]*(t[2]+t[3])+t[1]*(t[2]-t[3])) for t in fam)
print("CE4' unconditioned pointwise max with outcomes in {-1,0,1}:",worst)

# ---------- control (b): explicit setting-dependent ensemble of local tables reaching 4, exact I
target={(0,0):1,(0,1):1,(1,0):1,(1,1):-1}
T={}
for z in SET:
    for t in it.product((-1,1),repeat=4):
        if t[z[0]]*t[2+z[1]]==target[z]:
            T[z]=t; break
E={z:F(T[z][z[0]]*T[z][2+z[1]]) for z in SET}
marg={}
for z in SET: marg[T[z]]=marg.get(T[z],0)+F(1,4)
I=sum(F(1,4)*math.log2(1/float(marg[T[z]])) for z in SET)
print("control(b) setting-dependent ensemble: CHSH =",chsh(E),"I(Omega;Z) bits =",I, "distinct tables",len(marg))
# minimal-information explicit: tables chosen to coincide where possible
# all 4 settings can share the 3-of-4 table? Find model where Omega|z is a mixture minimizing I with CHSH=4 is impossible below 2 bits? quick LP-free check:
print("bound at I=2 bits:",min(4,2+4*math.sqrt(2*math.log(2)*2)))

# ---------- bearing: graph cone speed vs emergent wave speed on cubic lattice, alpha=1/d
d=3
best=0.0
import numpy as np
ks=np.linspace(1e-4,math.pi-1e-4,121)
for kx in ks:
    for ky in ks[::4]:
        for kz in ks[::4]:
            c=(math.cos(kx)+math.cos(ky)+math.cos(kz))/3
            w=math.acos(c); sw=math.sin(w)
            if sw<1e-9: continue
            vg=math.sqrt(math.sin(kx)**2+math.sin(ky)**2+math.sin(kz)**2)/(3*sw)
            best=max(best,vg)
print("cubic alpha=1/3: long-wavelength speed 1/sqrt3 =",1/math.sqrt(3)," max group speed (sampled) =",best," graph cone speed = 1 edge/step")
