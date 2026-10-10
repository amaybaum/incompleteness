# Analytic re-check (§A.21) of suspicious survivors of the d=3 scan: is a_11 = 1/2 really two-sided product-positive?
# The family (from dim1_probe_fast Q1), with b_02 = a_32 = b_31 = 0:
#   G~(u⊗t) = u⊗(t+Nt)/2 + z⊗(t−Nt)/2 ; G~(z⊗t) = u⊗(t−Nt)/2 + z⊗(t+Nt)/2   (N = diag(1,1,-1,-1))
#   G~(x⊗u) = a11 x⊗x ; G~(x⊗x) = a11 x⊗u ; G~(x⊗y) = b21 y⊗z ; G~(x⊗z) = -b21 y⊗y
#   G~(y⊗u) = a22 y⊗x ; G~(y⊗x) = a22 y⊗u ; G~(y⊗y) = b12 x⊗z ; G~(y⊗z) = -b12 x⊗y
import numpy as np, itertools
U,X,Y,Z=0,1,2,3; n=4
def build(a11,a22,b12,b21):
    G=np.zeros((16,16)); idx=lambda i,j:i*n+j
    Nv=[1,1,-1,-1]
    for b in range(n):
        p=(1+Nv[b])/2; m=(1-Nv[b])/2
        G[idx(U,b),idx(U,b)]+=p; G[idx(Z,b),idx(U,b)]+=m; G[idx(U,b),idx(Z,b)]+=m; G[idx(Z,b),idx(Z,b)]+=p
    G[idx(X,X),idx(X,U)]=a11; G[idx(X,U),idx(X,X)]=a11; G[idx(Y,Z),idx(X,Y)]=b21; G[idx(Y,Y),idx(X,Z)]=-b21
    G[idx(Y,X),idx(Y,U)]=a22; G[idx(Y,U),idx(Y,X)]=a22; G[idx(X,Z),idx(Y,Y)]=b12; G[idx(X,Y),idx(Y,Z)]=-b12
    return G
def minval(G, m=400, seed=3):
    rng=np.random.default_rng(seed)
    def pts(k):
        v=rng.standard_normal((k,3)); v/=np.linalg.norm(v,axis=1)[:,None]; return np.concatenate([np.ones((k,1)),v],1)
    S=pts(m); E=pts(m)
    PS=np.array([np.kron(s,t) for s in S for t in S]); PE=np.array([np.kron(f,g) for f in E for g in E])
    return float((PE@(G@PS.T)).min())
# also an exact-ish local optimizer: minimize over four unit vectors by random restarts + coordinate descent
def opt_min(G, restarts=60, seed=5):
    rng=np.random.default_rng(seed)
    best=1e9
    def val(v):
        s,t,f,g=[np.concatenate(([1.0],x/np.linalg.norm(x))) for x in v]
        return np.kron(f,g)@G@np.kron(s,t)
    for _ in range(restarts):
        v=[rng.standard_normal(3) for _ in range(4)]
        cur=val(v); step=0.5
        for it in range(400):
            improved=False
            for i in range(4):
                for _ in range(6):
                    w=[x.copy() for x in v]; w[i]=w[i]+step*rng.standard_normal(3)
                    nv=val(w)
                    if nv<cur: v,cur,improved=w,nv,True
            if not improved: step*=0.5
            if step<1e-7: break
        best=min(best,cur)
    return best
for params in [(1,1,-1,1),(0.5,1,-1,0.5),(0.5,0.5,1,0.5),(1,-1,-1,-1),(1,1,1,-1),(1,0.5,0.5,0.5)]:
    G=build(*params); Gi=np.linalg.inv(G)
    print('params a11,a22,b12,b21 =',params,
          '| sample min G: %.3e  G^-1: %.3e | optimized min G: %.3e  G^-1: %.3e'
          % (minval(G), minval(Gi), opt_min(G), opt_min(Gi)))
# analytic: product state s⊗t with s=(1,sx,sy,sz), effect f⊗g; the a11 block contributes a11*(fx*gx*sx*1 + fx*1*sx*tx)...
# closed form of the value for the family (b02=a32=b31=0):
def value(a11,a22,b12,b21,s,t,f,g):
    sx,sy,sz=s; tx,ty,tz=t; fx,fy,fz=f; gx,gy,gz=g
    # S1 part: control u,z components; target via (t+Nt)/2 and (t-Nt)/2 with N=diag(1,1,-1,-1) on (u,x,y,z)
    v  = (1+fz*sz)*(1+gx*tx) + (sz+fz)*(gy*ty+gz*tz)
    v += a11*fx*sx*(gx + tx) + a22*fy*sy*(gx+tx)
    v += b21*fy*sx*(gz*ty - gy*tz) + b12*fx*sy*(gz*ty - gy*tz)
    return v
# check the closed form against the matrix on random points
rng=np.random.default_rng(1)
G=build(0.5,1,-1,0.5)
for _ in range(3):
    s,t,f,g=[x/np.linalg.norm(x) for x in rng.standard_normal((4,3))]
    lhs=np.kron(np.r_[1,f],np.r_[1,g])@G@np.kron(np.r_[1,s],np.r_[1,t]); rhs=value(0.5,1,-1,0.5,s,t,f,g)
    print('closed form check: %.6f %.6f'%(lhs,rhs))
# hand analysis at a11=1/2: take sz=fz=0 (equator), s=(1,0,0),f=(1,0,0) => v = (1+gx tx) + a11 (gx+tx) ; with gx=tx=-1: 2 - 2 a11 = 1 >= 0;  gx=-1,tx=1: 0 ; fine.
# and the inverse: G^-1 has a11 -> 1/a11 = 2 (the block is a scaled swap) => value (1+gx tx) + 2(gx+tx) at gx=tx=-1: 2-4 = -2 < 0 !!
Gi=np.linalg.inv(build(0.5,1,-1,0.5))
s=np.r_[1,1,0,0]; t=np.r_[1,-1,0,0]; f=np.r_[1,1,0,0]; g=np.r_[1,-1,0,0]
print('explicit witness for G^-1 at a11=1/2 (s=+x,t=-x,f=+x,g=-x):', np.kron(f,g)@Gi@np.kron(s,t))
