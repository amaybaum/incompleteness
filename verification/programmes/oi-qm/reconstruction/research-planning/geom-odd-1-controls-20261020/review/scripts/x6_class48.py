"""Size of R's class under local signed permutations fixing the z3 line (16 per factor), within F; and how many are sign twists."""
import sys, itertools
import numpy as np
sys.path.insert(0, sys.argv[1]); import controls_verify as cv
body = cv.Body('eball3')
R = np.array([[int(c) for c in r] for r in body.reference], dtype=np.int64)
H = np.array([[int(c) for c in r] for r in body.H]); T = np.kron(np.eye(4, dtype=np.int64), H); C = np.kron(H, np.eye(4, dtype=np.int64))
cor = {0: np.array([1, 0, 0, 1]), 1: np.array([1, 0, 0, -1])}
def inF(M):
    return (np.array_equal(T @ M @ T, M) and np.array_equal(C @ M @ C, T @ M)
            and all(np.array_equal(M @ np.kron(cor[a], cor[b]), np.kron(cor[a], cor[(a + b) % 2])) for a in (0, 1) for b in (0, 1)))
locs = []
for p in itertools.permutations(range(3)):
    if p[2] != 2: continue
    for s in itertools.product((1, -1), repeat=3):
        M = np.zeros((4, 4), dtype=np.int64); M[0, 0] = 1
        for i in range(3): M[1 + i, 1 + p[i]] = s[i]
        locs.append(M)
print('local maps per factor (signed perms keeping the z3 line):', len(locs))
seen = set(); tw = 0
for A, B in itertools.product(locs, repeat=2):
    L1R = np.kron(A, B) @ R
    for Cc, D in itertools.product(locs, repeat=2):
        M = L1R @ np.kron(Cc, D)
        k = M.tobytes()
        if k in seen: continue
        if inF(M):
            seen.add(k)
print('distinct class members in F:', len(seen))
