"""Exact exploratory checks; stdlib only. No repository access or changes."""
from collections import defaultdict, Counter
from itertools import product

N = 5
EDGES = ((0, 1), (1, 2), (0, 3), (1, 4))
VISIBLE = (0, 2, 3, 4, 5, 7, 8, 9)
INITIAL = tuple(s for s in range(1024) if s & 24 == 0)
A = [8, 16]

def step(s, edges=EDGES):
    u = [(s >> i) & 1 for i in range(N)]
    v = [(s >> (N+i)) & 1 for i in range(N)]
    w = v[:]
    for a, b in edges:
        w[a] ^= u[b]
        w[b] ^= u[a]
    return sum(x << i for i, x in enumerate(w+u))

def evolve(s, t=3, edges=EDGES):
    for _ in range(t):
        s = step(s, edges)
    return s

def rank(rows):
    pivots = {}
    for x in rows:
        while x:
            j = x.bit_length()-1
            if j in pivots:
                x ^= pivots[j]
            else:
                pivots[j] = x
                break
    return len(pivots)

def basis(space):
    out = []
    for v in sorted(space):
        if rank(out+[v]) > len(out):
            out.append(v)
    return out

def omega(a, b, n=5):
    mask = (1 << n)-1
    return (((a & mask) & (b >> n)).bit_count()
            + ((a >> n) & (b & mask)).bit_count()) % 2

def matrix_rows(edges=EDGES):
    cols = [evolve(1 << j, edges=edges) for j in range(10)]
    return [sum(((cols[j] >> i) & 1) << j for j in range(10))
            for i in range(10)]

def read(s, indices):
    return tuple((s >> i) & 1 for i in indices)

def check_records(indices, edges=EDGES):
    records = defaultdict(list)
    for initial in INITIAL:
        final = evolve(initial, edges=edges)
        records[read(final, indices)].append((initial, read(final, (1, 6))))
    support = sorted({len({h for _, h in values}) for values in records.values()})
    fibers = sorted({len(values) for values in records.values()})
    rows = matrix_rows(edges)
    h = [rows[i] for i in indices]
    unknown = rank(A+h+[rows[1], rows[6]])-rank(A+h)
    assert support == [2**unknown]
    return len(records), support, fibers

assert len(INITIAL) == 256
assert rank(A) == 2 and all(omega(a, b) == 0 for a in A for b in A)
assert len({step(s) for s in range(1024)}) == 1024
assert all(omega(step(1 << i), step(1 << j)) == omega(1 << i, 1 << j)
           for i in range(10) for j in range(10))
period = next(t for t in range(1, 33)
              if all(evolve(1 << j, t) == 1 << j for j in range(10)))
assert period == 16
assert all(evolve(s, period) == s for s in range(1024))
print('Native five-site model: 256 admissible states; symplectic; exact period 16.')

expected_rows = [[5, 7, 9], [2, 4, 8], [1, 3, 5, 9], [2, 4, 6],
                 [1, 3, 5, 7], [0, 2, 4, 6, 8], [3, 5, 7, 9],
                 [0, 4, 6], [1, 5], [0, 2, 6]]
rows = matrix_rows()
assert rows == [sum(1 << i for i in entry) for entry in expected_rows]
for s in range(1024):
    assert evolve(s) == sum(((s & row).bit_count() % 2) << i
                            for i, row in enumerate(rows))
for s in INITIAL:
    f = evolve(s)
    assert ((f >> 1) & 1) == (((f >> 5) ^ (f >> 7)) & 1)
    assert ((f >> 6) & 1) == (f & 1)
    U0, U2, U3, U4, V0, V2, V3, V4 = read(f, VISIBLE)
    s4 = U2 ^ V3
    f2 = U4 ^ V3
    d = U0 ^ f2 ^ s4
    b = V3 ^ d
    c = V4 ^ V2
    e = U3 ^ c
    a = V2 ^ e
    p = V0 ^ V4
    decoded = sum(x << i for i, x in enumerate((a, b, c, 0, 0, d, e, f2, p, s4)))
    assert decoded == s
print('All 1024 states satisfy the displayed three-step linear formulas.')
print('All admissible states: hidden u1 = V0 XOR V2; hidden v1 = U0.')
print('Explicit decoder recovers all eight initially unknown bits in every branch.')

for label, edges, expected in [
    ('both memories', EDGES, (256, [1], [1])),
    ('memory 3 only', EDGES[:-1], (128, [2], [2])),
    ('memory 4 only', EDGES[:2]+EDGES[3:], (128, [2], [2])),
    ('neither memory', EDGES[:2], (64, [4], [4])),
]:
    actual = check_records(VISIBLE, edges)
    assert actual == expected
    print(label+': records, hidden support, initial fibers = '+str(actual))

for label, indices, expected in [
    ('original endpoint pairs only', (0, 2, 5, 7), (16, [1], [16])),
    ('three sufficient record bits', (0, 5, 7), (8, [1], [32])),
    ('visible u coordinates only', (0, 2, 3, 4), (16, [2], [16])),
    ('visible v coordinates only', (5, 7, 8, 9), (16, [2], [16])),
]:
    actual = check_records(indices)
    assert actual == expected
    print(label+': '+str(actual))

coordinate_counts = Counter()
for choices in product((0, 5), repeat=4):
    indices = tuple(i+c for i, c in zip((0, 2, 3, 4), choices))
    _, support, _ = check_records(indices)
    coordinate_counts[support[0]] += 1
assert coordinate_counts == {2: 12, 4: 4}
print('One coordinate per visible site: support histogram '+str(dict(sorted(coordinate_counts.items()))))
assert omega((1 << 5) ^ (1 << 7), 1 << 0) == 1
print('The two sufficient hidden-inference record functions have pairing 1.')

# Exhaust all maximal isotropic spaces of linear records on four visible pairs.
spaces = {frozenset([0])}
counts = [1]
for dimension in range(4):
    next_spaces = set()
    for space in spaces:
        for v in range(1, 256):
            if v not in space and all(omega(v, w, 4) == 0 for w in space):
                next_spaces.add(space | frozenset(w ^ v for w in space))
    spaces = next_spaces
    counts.append(len(spaces))
assert counts == [1, 255, 5355, 11475, 2295]
histogram = Counter()
for space in spaces:
    h = []
    for v in basis(space):
        pulled = 0
        for j, i in enumerate(VISIBLE):
            if v >> j & 1:
                pulled ^= rows[i]
        h.append(pulled)
    unknown = rank(A+h+[rows[1], rows[6]])-rank(A+h)
    histogram[2**unknown] += 1
    # Independent direct enumeration of every record branch.
    branches = defaultdict(set)
    for s in INITIAL:
        record = tuple((s & row).bit_count() % 2 for row in h)
        branches[record].add(read(evolve(s), (1, 6)))
    assert {len(values) for values in branches.values()} == {2**unknown}
assert histogram == {2: 405, 4: 1890}
print('Isotropic-space counts by dimension: '+str(counts))
print('All 2295 maximal isotropic record spaces, rank AND enumeration: '+str(dict(sorted(histogram.items()))))
print('PASS: every asserted finite check; no floating-point arithmetic.')
