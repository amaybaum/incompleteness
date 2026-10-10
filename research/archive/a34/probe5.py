"""A34 probe 5: the combinatorial incidence structure of the 81 tori and its automorphisms.
Tori are indexed by (r, s), r, s edges of K3,3 = cells of a 3x3 grid (rook's graph R = K3 □ K3 is the line graph).
Circle-adjacency:  (r,s) ~1 (r',s')  iff  r = r' and s ~ s', or s = s' and r ~ r'   (share a circle)   -> R □ R = K3^□4
Point-adjacency:   (r,s) ~0 (r',s')  iff  r ~ r' and s ~ s'                          (share exactly one point)
Aut(K3^□4) = S3 wr S4 (Sabidussi–Vizing: K3 prime, connected). Count those preserving ~0 as well.
Expect (S3 wr S2) wr S2, order 72^2 * 2 = 10368."""
import itertools
cells = list(itertools.product(range(3), repeat=4))          # (a,b,c,d): r=(a,b), s=(c,d)
idx = {c: i for i, c in enumerate(cells)}
def adj0(x, y):
    return (x[0] != y[0]) + (x[1] != y[1]) == 1 and (x[2] != y[2]) + (x[3] != y[3]) == 1
A0 = {(i, j) for i, x in enumerate(cells) for j, y in enumerate(cells) if i < j and adj0(x, y)}
perms3 = list(itertools.permutations(range(3)))
count = 0; product_form = 0
for fperm in itertools.permutations(range(4)):             # factor permutation
    for ps in itertools.product(perms3, repeat=4):         # per-factor S3
        img = {}
        for c in cells:
            y = [0]*4
            for k in range(4): y[fperm[k]] = ps[k][c[k]]
            img[idx[c]] = idx[tuple(y)]
        if all(((min(img[i], img[j]), max(img[i], img[j])) in A0) for (i, j) in A0):
            count += 1
            if {fperm[0], fperm[1]} in ({0, 1}, {2, 3}): product_form += 1
print('automorphisms of (circle-adjacency, point-adjacency) inside S3 wr S4:', count, '| of product-or-swap form:', product_form, '| expected 10368')
print('|S3 wr S4| =', 6**4 * 24, '| circle-adjacency alone admits factor-mixing automorphisms:', 6**4 * 24 > count)
