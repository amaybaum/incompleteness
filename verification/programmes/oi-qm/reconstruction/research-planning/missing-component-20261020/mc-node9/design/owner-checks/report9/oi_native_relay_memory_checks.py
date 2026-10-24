"""Exact exploratory checks: native parity relay, finite lifetime, resource controls.
Python 3 standard library; no repository writes or stochastic sampling.
The arbitrary-length claim is proved in the accompanying report, not by testing.
"""
from collections import Counter, defaultdict

CORE = ((0, 1), (1, 2), (0, 3), (1, 4), (0, 5), (2, 5))

def model(k, mode='native'):
    n = 6 + k
    edges = CORE + tuple((j-1, j) for j in range(6, n))
    clean = [n+3, n+4, 5] + [j+n if j % 2 == 0 else j for j in range(6, n)]
    if mode != 'native':
        assert k == 1
        if mode == 'v6 unknown': clean.remove(n+6)
        elif mode == 'u6 clean instead': clean[clean.index(n+6)] = 6
        elif mode == 'edge absent': edges = CORE
        elif mode == 'both6 clean': clean.append(6)
        else: raise ValueError(mode)
    return n, edges, clean

def rank(rows):
    b = {}
    for r in rows:
        while r:
            p = r.bit_length()-1
            if p in b: r ^= b[p]
            else:
                b[p] = r
                break
    return len(b)

def step(s, n, edges):
    # Independent bit-state implementation for exhaustive enumeration.
    u = [(s >> j) & 1 for j in range(n)]
    v = [(s >> (n+j)) & 1 for j in range(n)]
    for a, b in edges: v[a] ^= u[b]; v[b] ^= u[a]
    return sum(x << j for j, x in enumerate(v+u))

def rowstep(U, V, edges):
    W = V.copy()
    for a, b in edges: W[a] ^= U[b]; W[b] ^= U[a]
    return W, U

def omega(a, b, n):
    low = (1 << n)-1
    return (((a & low) & (b >> n)).bit_count() +
            ((a >> n) & (b & low)).bit_count()) % 2

def initial(n, clean):
    free = [j for j in range(2*n) if j not in clean]
    return [sum(((s >> i) & 1) << j for i, j in enumerate(free))
            for s in range(1 << len(free))]

def read(s, n):
    return tuple((s >> j) & 1 for j in range(n) if j != 1)

def audit(k, mode='native', enumerate_all=False):
    n, edges, clean = model(k, mode)
    A = [1 << j for j in clean]
    cleanmask = sum(A)
    f = (1 << 3) | (1 << n) | (1 << (n+2))
    U0 = [1 << j for j in range(n)]
    V0 = [1 << (n+j) for j in range(n)]
    U, V = U0.copy(), V0.copy()
    assert all(omega(step(1 << i, n, edges), step(1 << j, n, edges), n)
               == omega(1 << i, 1 << j, n)
               for i in range(2*n) for j in range(2*n))
    if mode != 'both6 clean':
        assert all(omega(a, b, n) == 0 for a in A for b in A)
    states0 = initial(n, clean) if enumerate_all else []
    states = states0.copy()
    table = []
    for t in range(5000):
        H = [U[j] for j in range(n) if j != 1]
        r = rank(A+H)
        fs = 1 << (rank(A+H+[f])-r)
        hs = 1 << (rank(A+H+[U[1], V[1]])-r)
        assert t != 0 or fs == 2
        if mode != 'both6 clean': assert hs >= 2
        if mode == 'native' and t == 1:
            assert (U[0] ^ U[2] ^ f) & ~cleanmask == 0
        if mode == 'native' and 2 <= t <= k+2:
            assert (U[t+3] ^ f) & ~cleanmask == 0
            assert fs == 1
        table.append((fs, hs))
        if enumerate_all:
            bf, bh = defaultdict(Counter), defaultdict(Counter)
            for x, y in zip(states0, states):
                rec = read(y, n)
                bf[rec][(x & f).bit_count() % 2] += 1
                bh[rec][((y >> 1) & 1, (y >> (n+1)) & 1)] += 1
            assert set(map(len, bf.values())) == {fs}
            assert set(map(len, bh.values())) == {hs}
            assert all(len(set(b.values())) == 1 for b in list(bf.values())+list(bh.values()))
            states = [step(s, n, edges) for s in states]
        U, V = rowstep(U, V, edges)
        if U == U0 and V == V0:
            period = t+1
            break
    else: raise AssertionError('No period found within the declared 5000-step cap')
    if enumerate_all: assert states == states0
    end = next(t-1 for t in range(2, period) if table[t][0] == 2)
    assert end >= k+2 if mode == 'native' else True
    return period, end, table, len(states0)

print('READ-ONLY EXPLORATORY DESIGN EVIDENCE; no preregistration or independent review.')
print('All native preparations are uniform products; exactly one known coordinate per memory site.')
expected = {0:(18,2), 1:(24,3), 2:(20,5), 3:(56,5), 4:(102,11),
            6:(130,17), 8:(258,16), 10:(714,83), 16:(2046,274)}
for k, result in expected.items():
    period, end, table, count = audit(k, enumerate_all=k <= 4)
    assert (period, end) == result
    print(f'k={k}: sites={6+k}, clean coordinates={3+k}, guaranteed end={2+k}, '
          f'actual initial window end={end}, exact period={period}; '
          + (f'enumerated all {count} preparations at every time.' if count
             else 'exact linear algebra, no state enumeration.'))

print('Seven-site sensitivity controls: (parity support, current hidden-pair support).')
controls = {'native':[(1,2),(1,2)], 'v6 unknown':[(2,4),(1,2)],
            'u6 clean instead':[(2,2),(1,2)], 'edge absent':[(1,2),(2,4)],
            'both6 clean':[(1,1),(1,2)]}
for mode, target in controls.items():
    _, _, table, count = audit(1, mode, True)
    assert table[2:4] == target
    print(f'{mode}: t=2 {table[2]}, t=3 {table[3]}; all {count} preparations enumerated.')

# Larger exact front checks are illustrations of the proved family, not a proof by sampling.
for k in (32, 64, 128):
    n, edges, clean = model(k)
    cleanmask = sum(1 << j for j in clean)
    f = (1 << 3) | (1 << n) | (1 << (n+2))
    U, V = [1 << j for j in range(n)], [1 << (n+j) for j in range(n)]
    for t in range(k+3):
        if 2 <= t <= k+2: assert (U[t+3] ^ f) & ~cleanmask == 0
        U, V = rowstep(U, V, edges)
    print(f'k={k}: direct native relay identities checked through t={k+2}.')
print('PASS: exact state enumeration agrees with linear algebra; all resource controls discriminate.')
