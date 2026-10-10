"""Deeper analysis of the first witness: pieces, orbit canonical form, and the exact exceptional set over all index maps."""
import sys, time, pickle, itertools; sys.path.insert(0, 'a38')
from lib38c import *
t0 = time.time()
found = pickle.load(open('a38/first_wit.pkl', 'rb'))
def support(E): return sum(1 for r in gauge_normal(as_list(E)) for x in r if x)
found.sort(key=lambda E: (support(E), as_list(E)))
E = as_list(found[0])
pickle.dump(E, open('a38/witness1.pkl', 'wb'))
# pieces
A = [[1 if ((i // 4) % 2 == 1 and i % 4 == 3 and (j // 4) % 2 == 1) else 0 for j in range(16)] for i in range(16)]
B = [[1 if (i // 4 == 2 and j % 4 == 1) else 0 for j in range(16)] for i in range(16)]
Cc = [[1 if (((i // 4) + i % 4) % 2 == 1 and j in (2, 8)) else 0 for j in range(16)] for i in range(16)]
print('E == A + B + Cc:', all(E[i][j] == A[i][j] + B[i][j] + Cc[i][j] for i in range(16) for j in range(16)))
for nm, M in (('A', A), ('B', B), ('Cc', Cc), ('A+B', [[A[i][j] + B[i][j] for j in range(16)] for i in range(16)]), ('A+Cc', [[A[i][j] + Cc[i][j] for j in range(16)] for i in range(16)]), ('B+Cc', [[B[i][j] + Cc[i][j] for j in range(16)] for i in range(16)])):
    st = straight_line_direct(M)
    cls = [(NAMES9[s], 'row' if tr else 'column') for s in CENSUS9 for tr in (False, True) if in_structure([sum(M, [])], s, False, tr)] if st else None
    clr = [(NAMES9[s], 'row' if tr else 'column') for s in CENSUS9 for tr in (False, True) if in_structure([sum(M, [])], s, True, tr)] if st else None
    print('piece %-5s straight %s  strict classes %s  relaxed classes %s' % (nm, st, cls, clr))
# orbit canonical form (gauge normal, min over stabilizer and sign)
PERMS = np.array([np.argsort(np.array(p)) for p, s_ in elems], dtype=np.int64)
def canon(Em):
    flat = np.array(Em, dtype=np.int64).reshape(256); imgs = flat[PERMS]
    imgs = np.concatenate([imgs, -imgs], 0).reshape(-1, 16, 16)
    imgs = imgs - imgs[:, :, :1] - imgs[:, :1, :] + imgs[:, :1, :1]
    flat2 = imgs.reshape(-1, 256); order = np.lexsort(flat2.T[::-1])
    return flat2[order[0]].reshape(16, 16).tolist(), len(set(map(tuple, flat2.tolist())))
Ec, orbit_size = canon(E)
print('orbit size (stabilizer x sign, gauge-normalized images):', orbit_size)
print('canonical representative (lexicographically minimal gauge normal form):'); print(show(Ec))
print('canonical rep straight:', straight_line_direct(Ec), 'support', sum(1 for r in Ec for x in r if x), 'values', sorted(set(x for r in Ec for x in r)))
# also the minimal-support member of the orbit among {0,1}-valued images, if any
flat = np.array(E, dtype=np.int64).reshape(256); imgs = flat[PERMS]; imgs = np.concatenate([imgs, -imgs], 0).reshape(-1, 16, 16)
imgs = imgs - imgs[:, :, :1] - imgs[:, :1, :] + imgs[:, :1, :1]
sup = np.abs(imgs).sum(axis=(1, 2)); print('orbit gauge-normal supports: min', int(sup.min()), 'max', int(sup.max()))
print('%.0fs' % (time.time() - t0), flush=True)
# exact exceptional set over all index maps (probe sections 4-5 with E's entries)
ent = entry_fn(E)
def cond(i, i2, j, j0): return gen_div(gen_div(ent(i, j), ent(i2, j)), gen_div(ent(i, j0), ent(i2, j0)))
ET = [list(c) for c in zip(*E)]; entT = entry_fn(ET)
def condT(i, i2, j, j0): return gen_div(gen_div(entT(i, j), entT(i2, j)), gen_div(entT(i, j0), entT(i2, j0)))
E_cand = {}
for form, cf in (('column', cond), ('row', condT)):
    for n in (4, 2, 8):
        for Bk in itertools.combinations(range(16), n):
            j0 = Bk[0]
            for i, i2 in itertools.combinations(range(16), 2):
                sets = None; generic = True
                for j in Bk[1:]:
                    s_ = solutions(cf(i, i2, j, j0))
                    if s_ == 'all': continue
                    generic = False
                    if s_ == 'none': sets = frozenset(); break
                    sets = s_ if sets is None else (sets & s_)
                    if not sets: break
                if not generic and sets:
                    for pt in sets: E_cand[pt] = E_cand.get(pt, 0) + 1
E_all = sorted(E_cand, key=lambda p: (p[1], p[2], p[0]))
print('candidate exceptional points (where some row pair becomes proportional on some block):', len(E_all), '%.0fs' % (time.time() - t0), flush=True)
print([show_pt(p) for p in E_all])
exact_E = []
for pt in E_all:
    res = {}
    for form, M in (('column', E), ('row', ET)):
        for mn in SHAPES:
            c_, x_ = search_point(M, pt, *mn); res[(form, mn)] = (len(c_), len(x_))
    tot = sum(v[1] for v in res.values())
    if tot: exact_E.append((show_pt(pt), res))
print('points admitting a Diţă structure (exact set):', exact_E, '%.0fs' % (time.time() - t0))
pickle.dump({'E': E, 'E_all': [show_pt(p) for p in E_all], 'exact_E': exact_E, 'canon': Ec}, open('a38/deep_wit.pkl', 'wb'))
