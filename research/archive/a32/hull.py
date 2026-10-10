"""Exploration only: affine-hull dimension of the union of the nine circles, and the marked points."""
import numpy as np
from sympy import Matrix
from circles import R, circle_vectors
V = [circle_vectors(*r) for r in R]
cen = [np.array(c) for c, _, _ in V]
cos_ = [np.array(A) + np.array(B) for _, A, B in V]
sin_ = [np.array(A) - np.array(B) for _, A, B in V]
real_rows = [cen[k] - cen[0] for k in range(1, 9)] + cos_
rr = Matrix(np.array(real_rows)).rank()
ri = Matrix(np.array(sin_)).rank()
print("real-part rank", rr, "imag-part rank", ri, "affine hull dim", rr + ri)
print("radius^2 =", np.dot(cos_[0], cos_[0]) / 64**2)
# marked points: the classes at z = +-1 of each circle; group identical feature vectors
pts = {}
for k in range(9):
    for s in (1, -1):
        x = tuple(cen[k] + s * cos_[k])
        pts.setdefault(x, []).append((k, s))
print("distinct marked classes:", len(pts), "circles through each:", sorted(len(v) for v in pts.values()))
