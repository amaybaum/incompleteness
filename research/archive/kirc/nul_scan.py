import sys, numpy as np
from ball_nogo import sphere_pts, constraint_rows, rank_modp
d=int(sys.argv[1])
for K in map(int, sys.argv[2:]):
    pts=sphere_pts(d,K); M,_=constraint_rows(d,pts); N=(d+1)**2
    print(d,K,M.shape, 'nullity', N*N-rank_modp(M % 2147483647), flush=True)
