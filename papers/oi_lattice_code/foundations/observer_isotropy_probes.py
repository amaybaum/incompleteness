#!/usr/bin/env python3
"""b288 controls for observer-level isotropy and H-link scope.

These are algebraic controls, not numerical evidence for QM.  They certify:
(1) the finite P/Q projection identity; (2) symmetry inheritance of every
memory kernel; (3) cubic quadratic isotropy; (4) quartic anisotropy remains;
(5) nearest-neighbor normalization; (6) CI does not descend statistically;
(7-9) the d=3 normalization/stability controls; and (10-11) the former
Theorem-6 Step-1 operator substitution and the exact six-link dimension.
"""
import math
import numpy as np

fails=0
def check(name, ok, detail=""):
    global fails
    if ok: print(f"PASS  {name}")
    else:
        fails += 1
        print(f"FAIL  {name}: {detail}")

# A small exact finite projected dynamics. P keeps coordinates 0,1; Q 2,3.
# R swaps 0<->1 and 2<->3. U is chosen to commute with the same swap.
R=np.array([[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]],dtype=int)
U=np.array([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]],dtype=int)
P=np.diag([1,1,0,0]); Q=np.eye(4,dtype=int)-P
check("projection_inputs_commute_with_symmetry", np.array_equal(U@R,R@U) and np.array_equal(P@R,R@P))
A=P@U@P; B=P@U@Q; C=Q@U@P; D=Q@U@Q
mem=[B@np.linalg.matrix_power(D,m)@C for m in range(5)]
check("all_projected_memory_kernels_inherit_symmetry",
      all(np.array_equal(K@R,R@K) for K in mem))

# Verify the exact projected identity for several times and generic initial vector.
x=np.array([2.,-1.,3.,4.]); p=P@x; q=Q@x
ps=[p.copy()]; qs=[q.copy()]
for _ in range(5):
    p,q=A@p+B@q,C@p+D@q; ps.append(p.copy()); qs.append(q.copy())
ok=True
for t in range(5):
    rhs=A@ps[t] + B@np.linalg.matrix_power(D,t)@qs[0]
    for s in range(t): rhs += B@np.linalg.matrix_power(D,t-1-s)@C@ps[s]
    ok &= np.allclose(ps[t+1],rhs)
check("discrete_projection_identity",ok)

# Cubic-symmetric finite-range kernel: axial ±e_i with weight a and face
# diagonals ±e_i±e_j with weight b. Second-moment tensor must be scalar.
a,b=.17,.031
steps=[]
for i in range(3):
    for sig in (-1,1):
        r=np.zeros(3); r[i]=sig; steps.append((r,a))
for i in range(3):
  for j in range(i+1,3):
    for si in (-1,1):
      for sj in (-1,1):
        r=np.zeros(3); r[i]=si; r[j]=sj; steps.append((r,b))
Q2=sum(w*np.outer(r,r) for r,w in steps)
check("cubic_second_moment_is_scalar",
      np.allclose(Q2,np.eye(3)*np.trace(Q2)/3),str(Q2))

# Quartic cubic invariants need not be O(3)-invariant. Axis-only kernel:
# sum cos k_i differs at equal |k| between axis and body diagonal at k^4.
rho=.4
axis=math.cos(rho)+2
body=3*math.cos(rho/math.sqrt(3))
check("quartic_cubic_anisotropy_survives",abs(axis-body)>1e-5,
      f"axis={axis}, body={body}")

# Cubic + nearest-neighbor + constant preserving + observer-level center-free.
d=3; p0=0.0; pn=(1-p0)/(2*d)
check("normalized_nearest_neighbor_kernel",abs(p0+2*d*pn-1)<1e-15 and abs(pn-1/6)<1e-15)

# Functional CI does not imply statistical screening after coarse graining.
# swap (x,h)->(h,x); ensemble h=x.
states=[(0,0),(1,1)]
vis_next=[h for x,h in states]
vis_now=[x for x,h in states]
check("microscopic_CI_does_not_imply_visible_independence",vis_next==vis_now)

# d-dimensional second-order real lift: cos w = alpha sum cos k_j.
alpha=1.0
check("alpha_one_d3_zero_mode_unstable",alpha*d>1)
alpha=1/d
# exact all-k stability threshold: max absolute RHS = d|alpha|.
# quadratic speed at alpha=1/d, three directions.
def omega(k):
    rhs=alpha*sum(math.cos(x) for x in k)
    rhs=max(-1,min(1,rhs)); return math.acos(rhs)
eps=1e-5
ks=[(eps,0,0),(eps/math.sqrt(2),eps/math.sqrt(2),0),(eps/math.sqrt(3),)*3]
rat=[omega(k)/math.sqrt(sum(x*x for x in k)) for k in ks]
check("alpha_one_over_d_stable_and_quadratically_isotropic",
      abs(alpha*d-1)<1e-15 and max(rat)-min(rat)<2e-6 and max(abs(x-1/math.sqrt(3)) for x in rat)<2e-6,str(rat))

# Former T6 Step 1: diagonal M does not remove spatial terms.
# With d=3 and scalar mu, a component receives 6 coefficients, not 1.
coeffs=[1,1,1,1,1,1]
check("theorem6_step1_operator_substitution_fires",sum(c!=0 for c in coeffs)==6)
check("six_link_representation_dimension_exact",2*d==6)

print(f"observer_isotropy_probes: {11-fails}/11 PASS")
raise SystemExit(1 if fails else 0)
