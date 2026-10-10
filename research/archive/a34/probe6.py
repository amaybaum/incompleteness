"""A34 probe 6: exact 2x2 minor of the paired feature matrix (Gaussian integers, entries scaled by 4).
Dita twist H[(i,a),(j,b)] = F4(i)[i,j] * F4(z_j)[a,b]; control: all z_j = i."""
import itertools, random
def f4(z):  # 4 F4(z) as Gaussian integers (complex with integer parts)
    return [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]
def H(zs):
    F = f4(1j); M = {}
    for i,a,j,b in itertools.product(range(4), repeat=4):
        M[(4*i+a, 4*j+b)] = complex(F[i][j]) * complex(f4(zs[j])[a][b])
    return M
def P(M, i, j, k): return M[(i,j)].conjugate() * M[(i,k)]
def fvP(M, a, b, c, d, e, f): return P(M,a,d,e) * P(M,b,e,f) * P(M,c,f,d)
def idx(x1, x2): return 4*x1 + x2
def paired(M, row, col):   # row = (a1,b1,c1,d1,e1,f1), col = (a2,...,f2)
    return fvP(M, *[idx(r, c) for r, c in zip(row, col)])
random.seed(5)
Mt, Mc = H([1j,-1j,1j,-1j]), H([1j]*4)
found = None
for _ in range(20000):
    r1, r2 = [tuple(random.randrange(4) for _ in range(6)) for _ in range(2)]
    c1, c2 = [tuple(random.randrange(4) for _ in range(6)) for _ in range(2)]
    mt = paired(Mt,r1,c1)*paired(Mt,r2,c2) - paired(Mt,r1,c2)*paired(Mt,r2,c1)
    if mt != 0:
        mc = paired(Mc,r1,c1)*paired(Mc,r2,c2) - paired(Mc,r1,c2)*paired(Mc,r2,c1)
        found = (r1, r2, c1, c2, mt, mc); break
print('witness minor rows', found[0], found[1], 'cols', found[2], found[3])
print('twisted minor (x 4^12):', found[4], '| untwisted control minor:', found[5])
# how many of the sampled minors are nonzero for the control? (must be 0 for all)
bad = 0
for _ in range(20000):
    r1, r2 = [tuple(random.randrange(4) for _ in range(6)) for _ in range(2)]
    c1, c2 = [tuple(random.randrange(4) for _ in range(6)) for _ in range(2)]
    if paired(Mc,r1,c1)*paired(Mc,r2,c2) - paired(Mc,r1,c2)*paired(Mc,r2,c1) != 0: bad += 1
print('control: nonzero minors among 20000 random ones:', bad)
