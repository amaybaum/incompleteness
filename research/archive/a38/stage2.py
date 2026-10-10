"""Quotient the {0,1} straight-line solutions by gauge, the stabilizer (index permutations incl. transposition) and
sign; write orbit representatives (gauge normal forms, minimal in the orbit)."""
import sys, time, pickle; sys.path.insert(0, 'a38')
from lib38 import *
t0 = time.time()
sols = pickle.load(open('a38/stage1_sols.pkl', 'rb'))
print('solutions', len(sols))
# stabilizer as index arrays on the flattened 256 positions: out[perm[t]] = E[t]
PERMS = np.array([np.argsort(np.array(p)) for p, s_ in elems], dtype=np.int64)   # inverse: out = E[inv]
# out[i2*16+j2] = E[i*16+j] where p[i*16+j] = i2*16+j2  =>  out = E[argsort(p)]
def to_mat(sol):
    E = np.zeros((16, 16), dtype=np.int64)
    for i in range(1, 16):
        m = sol[i]
        for k in range(16): E[i, k] = (m >> k) & 1
    return E
def gnorm(E):
    return E - E[:, :1] - E[:1, :] + E[0, 0]
def canon(E):
    """minimal gauge normal form over the stabilizer images and the sign"""
    flat = E.reshape(256)
    imgs = flat[PERMS]                       # (1024, 256)
    imgs = np.concatenate([imgs, -imgs], 0).reshape(-1, 16, 16)
    imgs = imgs - imgs[:, :, :1] - imgs[:, :1, :] + imgs[:, :1, :1]
    flat2 = imgs.reshape(-1, 256)
    # lexicographic minimum
    order = np.lexsort(flat2.T[::-1])
    return tuple(int(x) for x in flat2[order[0]])
reps = {}
for n, sol in enumerate(sols):
    E = to_mat(sol); c = canon(E)
    if c not in reps: reps[c] = (n, E)
    if n % 50000 == 0: print(n, 'orbits so far', len(reps), '%.0fs' % (time.time() - t0), flush=True)
print('orbits (gauge x stabilizer x sign):', len(reps), '%.0fs' % (time.time() - t0))
pickle.dump(reps, open('a38/stage2_reps.pkl', 'wb'))
# sanity: W's orbit is present
Wm = np.array(W_matrix(), dtype=np.int64)
print('W canon in reps:', canon(Wm) in reps)
print('zero in reps:', tuple([0] * 256) in reps)
vals = {}
for c in reps: vals[tuple(sorted(set(c)))] = vals.get(tuple(sorted(set(c))), 0) + 1
print('value sets of gauge normal forms:', vals)
