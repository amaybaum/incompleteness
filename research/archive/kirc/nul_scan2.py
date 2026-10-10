"""Exact upper bound on the sampled first-order nullity (mod p, random row compression -- rank can only drop)."""
import sys, numpy as np
from ball_nogo import sphere_pts, constraint_rows, rank_modp, P
d=int(sys.argv[1])
for K in map(int, sys.argv[2:]):
    pts=sphere_pts(d,K); M,_=constraint_rows(d,pts); N=(d+1)**2; U=N*N
    R=np.random.default_rng(7).integers(0,1000,size=(U+100,M.shape[0]),dtype=np.int64)
    Mm=M%P; Mc=np.zeros((U+100,U),dtype=np.int64)
    for s in range(0,M.shape[0],256): Mc=(Mc+(R[:,s:s+256]@Mm[s:s+256])%P)%P
    print(d,K,M.shape,'nullity bound',U-rank_modp(Mc),flush=True)
