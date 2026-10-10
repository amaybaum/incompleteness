"""probe3c: faithfulness of the grid action of A33 (why 18432 on the eighth-root grid) and the
order-two stabilizer of a generic Diţă point in G_ext."""
import itertools, sys, numpy as np
src = open('probe3b.py').read()
exec(src[:src.index('gens = [a33_perm')])
seen = {}; dups = []
for nu in autos:
    for eps in itertools.product([True, False], repeat=9):
        p = a33_perm(nu, eps); kk = tuple(p.array_form)
        if kk in seen: dups.append((seen[kk], (nu, eps)))
        else: seen[kk] = (nu, eps)
print('distinct grid permutations among 72*512 pairs:', len(seen), '; duplicates:', len(dups))
print('first duplicate pairs:', dups[:2])
triv = [(nu, eps) for nu in autos for eps in itertools.product([True, False], repeat=9) if a33_perm(nu, eps).is_Identity]
print('pairs acting trivially on the grid:', triv)
# check the same with a 12th-root grid? (a bit z->z̄ acts trivially only on {±1}; so the grid action IS faithful
# unless a33_perm is not injective) -> print the two pairs of the first duplicate and where they differ symbolically
if dups:
    (nu1, e1), (nu2, e2) = dups[0]
    print('nu1', nu1, 'eps1', e1); print('nu2', nu2, 'eps2', e2)
# the stabilizer of a generic Diţă point in G_ext: identify the element(s)
rng = np.random.default_rng(353)
z, w = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
D = np.exp(1j * rng.uniform(0, 2 * np.pi, (4, 4)))
H = dita(U_circle(0, z), [U_circle(0, w)] * 4, D)
S4 = list(itertools.permutations(range(4)))
def prod_perm(p, q): return [4 * p[a] + q[b] for a in range(4) for b in range(4)]
SW = [4 * b + a for a in range(4) for b in range(4)]
c0 = np.round(dephase(H) * 4, 6).tobytes()
found = []
for sw in (False, True):
    for cj in (False, True):
        for tr in (False, True):
            H1 = H.copy()
            if sw: H1 = H1[np.ix_(SW, SW)]
            if cj: H1 = np.conj(H1)
            if tr: H1 = H1.T
            for p1 in S4:
                for p2 in S4:
                    H2 = H1[prod_perm(p1, p2), :]
                    for t1 in S4:
                        for t2 in S4:
                            if np.round(dephase(H2[:, prod_perm(t1, t2)]) * 4, 6).tobytes() == c0:
                                found.append((sw, cj, tr, p1, p2, t1, t2))
print('stabilizer elements of a generic Diţă point (swap, conj, transpose, pi1, pi2, tau1, tau2):', found)
