"""Common specification for the disputed n = 3 learning witnesses (linear F2 model, Main.md:290 update).
State s = (u_0,u_1,u_2, v_0,v_1,v_2). One step: u'_x = sum_{z~x} u_z + v_x, v'_x = u_x.
A s0 = 0 : initial constraints = both coordinates of the FULL site are 0 (clean); all other coordinates uniform.
H s0     : retained memory = the CURRENT visible cells only (both coords of every visible site) at time t; no history.
T s0     : target = the toy site's (u, v) at time t.
Support of T given (A, H) = 2^(rank[A;H;T] - rank[A;H]); learned iff the difference is 0.
Checked against explicit enumeration of all branches."""
import itertools
def rank(rows,n):
    rows=[r for r in rows]; rk=0
    for c in range(n):
        piv=next((i for i in range(rk,len(rows)) if rows[i]>>c&1),None)
        if piv is None: continue
        rows[rk],rows[piv]=rows[piv],rows[rk]
        for i in range(len(rows)):
            if i!=rk and rows[i]>>c&1: rows[i]^=rows[rk]
        rk+=1
    return rk
def step_matrix(adj,n):   # rows as bitmasks over 2n input coords (u_0..u_{n-1}, v_0..v_{n-1})
    R=[]
    for x in range(n):   # u'_x
        m=0
        for z in adj[x]: m|=1<<z
        m|=1<<(n+x); R.append(m)
    for x in range(n): R.append(1<<x)   # v'_x = u_x
    return R
def compose(R,S,n):  # rows of R applied after S : (R∘S) row i = sum_j R_ij S_j
    out=[]
    for r in R:
        m=0
        for j in range(2*n):
            if r>>j&1: m^=S[j]
        out.append(m)
    return out
def run(name,adj,toy,full,none,tmax=8):
    n=3; M=step_matrix(adj,n); P=[1<<i for i in range(2*n)]
    vis=[full,none]; print(f'== {name}: edges {sorted({tuple(sorted((a,b))) for a in adj for b in adj[a]})}, toy {toy}, FULL {full}, NONE {none}')
    A=[1<<full,1<<(n+full)]
    for t in range(1,tmax+1):
        P=compose(M,P,n)
        H=[P[x] for x in vis]+[P[n+x] for x in vis]; T=[P[toy],P[n+toy]]
        d=rank(A+H+T,2*n)-rank(A+H,2*n); dprior=rank(A+T,2*n)-rank(A,2*n)
        # enumeration
        br={}; pri=set()
        for bits in itertools.product((0,1),repeat=2*n):
            s=sum(b<<i for i,b in enumerate(bits))
            if any(bin(a&s).count('1')%2 for a in A): continue
            h=tuple(bin(r&s).count('1')%2 for r in H); tt=tuple(bin(r&s).count('1')%2 for r in T)
            br.setdefault(h,set()).add(tt); pri.add(tt)
        sup=min(len(v) for v in br.values()); assert all(len(v)==2**d for v in br.values()), 'rank formula mismatch'
        assert len(pri)==2**dprior
        print(f'  t={t}: d_prior = rank[A;T]-rank[A] = {dprior}, d_posterior = rank[A;H;T]-rank[A;H] = {d} '
              f'(support {2**d}, enumerated {sup}); information from retained memory = {dprior-d} bit(s); '
              + ('LEARNED' if d==0 and dprior>0 else ('determined without reading memory (overwrite)' if dprior==0 else '')))
path_012={0:[1],1:[0,2],2:[1]}
print('Path 0-1-2 (centre = site 1).')
run("re-review's 'NONE in centre' reading", path_012, toy=2, full=0, none=1)
for toy,full,none in [(0,1,2),(1,0,2),(1,2,0),(2,1,0)]:
    run('coordinator placement', path_012, toy, full, none, tmax=4)
print('Path 1-0-2 (centre = site 0), the re-review witness.')
run("re-review witness", {0:[1,2],1:[0],2:[0]}, toy=2, full=0, none=1)
# Owner's correlated-preparation control: support {(0,0),(1,1)} has no clean coordinate but a known relation x^y = 0;
# the reversible map (x,y) -> (x, x^y) produces a known-zero coordinate. Clean-coordinate counting misses it; rank(A) does not.
sup={(0,0),(1,1)}; img={(x,x^y) for x,y in sup}
print('== correlated preparation: clean coordinates in', sorted(sup), ':', [i for i in (0,1) if len({s[i] for s in sup})==1],
      '; after (x,y)->(x,x^y):', sorted(img), 'clean coordinates', [i for i in (0,1) if len({s[i] for s in img})==1],
      '; rank(A) of the constraint x^y=0 is 1 before and after')
# Owner's nonlinear control: (x, y, z) = (x, y, xy), x, y fair. No nontrivial affine constraint holds (rank A = 0),
# yet retaining x, y determines z. rank(A) counts affine constraint information only.
sup2={(x,y,x*y) for x in (0,1) for y in (0,1)}
aff=[m for m in range(1,8) if len({bin(m & (s[0]|s[1]<<1|s[2]<<2)).count('1')%2 for s in sup2})==1]
det=all(len({s[2] for s in sup2 if s[:2]==xy})==1 for xy in {s[:2] for s in sup2})
print('== nonlinear correlation: support', sorted(sup2), '; nonzero affine constraints holding:', aff,
      '; z determined by (x, y):', det)
