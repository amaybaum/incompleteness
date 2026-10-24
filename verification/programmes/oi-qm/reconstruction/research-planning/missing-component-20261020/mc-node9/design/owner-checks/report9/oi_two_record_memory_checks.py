"""Read-only exploratory design: connected two-record acquisition and masked conjugate attempt.
Exact F2 arithmetic and rational weights; Python standard library only.
"""
from collections import Counter, defaultdict
from fractions import Fraction

BASE = ((0,1),(1,2),(0,3),(1,4),(0,5),(2,5),(5,6))

def step(s, n, edges):
    u = [(s >> j) & 1 for j in range(n)]
    v = [(s >> (n+j)) & 1 for j in range(n)]
    for a,b in edges: v[a] ^= u[b]; v[b] ^= u[a]
    return sum(z << j for j,z in enumerate(v+u))

def rows_next(U,V,edges):
    W = V.copy()
    for a,b in edges: W[a] ^= U[b]; W[b] ^= U[a]
    return W,U

def basis(rows):
    b = {}
    for r in rows:
        while r:
            j = r.bit_length()-1
            if j in b: r ^= b[j]
            else: b[j] = r; break
    return list(b.values())

def rank(rows): return len(basis(rows))

def omega(a,b,n):
    low = (1 << n)-1
    return (((a & low) & (b >> n)).bit_count() +
            ((a >> n) & (b & low)).bit_count()) % 2

def initial(n,clean):
    free = [j for j in range(2*n) if j not in clean]
    for z in range(1 << len(free)):
        yield sum(((z >> j) & 1) << p for j,p in enumerate(free))

def output_counts(rows,n,clean):
    # Enumerate the exact image, with its equal fiber multiplicity.
    free = [j for j in range(2*n) if j not in clean]
    columns = [sum(((r >> j) & 1) << i for i,r in enumerate(rows)) for j in free]
    bs = basis(columns)
    image = [0]
    for b in bs: image += [x ^ b for x in image]
    return {x:1 << (len(free)-len(bs)) for x in image}

print('EXPLORATORY DESIGN EVIDENCE; not preregistered or independently reviewed.')
print('POSITIVE CONTROL: two connected seven-site devices; bridge (0,7).')
n = 14
edges = BASE + tuple((a+7,b+7) for a,b in BASE) + ((0,7),)
clean = [n+3,n+4,5,n+6,n+10,n+11,12,n+13]
A = [1 << j for j in clean]
cm = sum(A)
assert all(omega(a,b,n) == 0 for a in A for b in A)
assert all(omega(step(1 << i,n,edges),step(1 << j,n,edges),n) == omega(1 << i,1 << j,n)
           for i in range(2*n) for j in range(2*n))
U = [1 << j for j in range(n)]; V = [1 << (n+j) for j in range(n)]
f = None
for t in range(5):
    if t == 1:
        f = [U[0]^U[2],U[7]^U[9]]
        assert (f[0] ^ ((1<<3)|(1<<n)|(1<<(n+2))|(1<<7))) & ~cm == 0
        assert (f[1] ^ ((1<<10)|(1<<(n+7))|(1<<(n+9))|(1<<0))) & ~cm == 0
        assert rank(A+f)-rank(A) == 2
    H = [U[j] for j in range(n) if j not in (1,8)]
    T = [U[1],V[1],U[8],V[8]]
    if t in (2,3):
        indices = (5,12) if t == 2 else (6,13)
        assert all((U[j]^ff) & ~cm == 0 for j,ff in zip(indices,f))
        assert rank(A+H+f) == rank(A+H)
        assert rank(A+H+T)-rank(A+H) == 2
        counts = output_counts(H+T+f,n,clean)
        branches = defaultdict(Counter)
        pair_counts = Counter()
        for z,w in counts.items():
            rec = z & ((1 << len(H))-1)
            hidden = (z >> len(H)) & 15
            pair = z >> (len(H)+4)
            branches[rec][hidden] += w
            pair_counts[pair] += w
        assert sum(counts.values()) == 1 << 20
        assert pair_counts == Counter({j:1 << 18 for j in range(4)})
        assert set(map(len,branches.values())) == {4}
        assert all(len(set(b.values())) == 1 for b in branches.values())
        print(f't={t}: 2 independent retained bits; {len(branches)} complete position records; '
              f'4 equally likely joint hidden states per record; image count={len(counts)}.')
    if t == 4:
        assert rank(A+H+f)-rank(A+H) == 2
        print('t=4: both historical bits become unreadable from the complete position record.')
    U,V = rows_next(U,V,edges)

print('CONJUGATE ATTEMPT: seven sites; final time 2; complete visible position record.')
n = 7; clean = [10,11,5,13]
I = list(initial(n,clean)); assert len(I) == 1024
branches = defaultdict(Counter); pair_counts = Counter()
triples = Counter()
for s in I:
    z = step(s,n,BASE); y = step(z,n,BASE)
    f = (y >> 5) & 1
    g = (y >> 8) & 1
    r = (s >> 6) & 1
    m = ((y >> 0) ^ (y >> 6)) & 1
    assert ((y >> 1) & 1) == f
    assert m == g ^ r
    rec = tuple((y >> j) & 1 for j in (0,2,3,4,5,6))
    branches[rec][r] += 1
    pair_counts[f,m] += 1
    triples[f,g,r] += 1
assert len(branches) == 64
assert all(c == Counter({0:8,1:8}) for c in branches.values())
assert set(pair_counts.values()) == {256} and len(pair_counts) == 4
assert set(triples.values()) == {128} and len(triples) == 8
print('Exact identity: f=u1(2)=u5(2), g=v1(2), m=u0(2) XOR u6(2)=g XOR r, r=u6(0).')
print('All four (f,m) pairs occur 256 times; f,g,r are independent fair bits.')
print('Every complete record leaves r fair (8/8), hence leaves g fair.')

# Relaxations: known mask, readable conjugate, and deliberately cancelled back-action.
for mode in ('both6 clean','read v5','cancel core kick'):
    obs = defaultdict(set)
    selected = [s for s in I if mode != 'both6 clean' or not ((s >> 6) & 1)]
    for s in selected:
        z = step(s,n,BASE); y = step(z,n,BASE)
        if mode == 'cancel core kick': y ^= ((z >> 5) & 1)*5
        rec = tuple((y >> j) & 1 for j in (0,2,3,4,5,6))
        if mode == 'read v5': rec += ((y >> 12) & 1,)
        obs[rec].add(((y >> 1) & 1,(y >> 8) & 1))
    assert set(map(len,obs.values())) == {1}
    print(f'{mode}: hidden pair fully determined on every branch ({len(selected)} inputs).')
def bad(s): return step(s,7,BASE)^(((s >> 5) & 1)*5)
assert any(omega(bad(1 << i),bad(1 << j),7) != omega(1 << i,1 << j,7)
           for i in range(14) for j in range(14))
print('Kick cancellation is not symplectic; other two controls violate preparation/read compatibility.')

print('BIAS SENSITIVITY: P(r=0)=p, all other free initial bits fair and independent.')
for p in (Fraction(0),Fraction(1,100),Fraction(1,4),Fraction(1,2),Fraction(99,100),Fraction(1)):
    obs = defaultdict(Counter)
    for s in I:
        y = step(step(s,n,BASE),n,BASE)
        rec = tuple((y >> j) & 1 for j in (0,2,3,4,5,6))
        g = (y >> 8) & 1
        w = p if not ((s >> 6) & 1) else 1-p
        if w: obs[rec][g] += w
    assert len(obs) == 64
    assert set(sum(b.values()) for b in obs.values()) == {Fraction(8)}
    expected = sorted(x for x in (p,1-p) if x)
    assert all(sorted(w/sum(b.values()) for w in b.values()) == expected for b in obs.values())
    print(f'p={p}: hidden-pair support={len(expected)}; optimal g prediction={max(p,1-p)}; '
          'visible record distribution unchanged.')

# Equal present statistics do not imply equivalence under future native protocols.
A = [1 << j for j in clean]
U = [1 << j for j in range(n)]; V = [1 << (n+j) for j in range(n)]
reveals = []
for t in range(13):
    H = [U[j] for j in range(n) if j != 1]
    if rank(A+H+[1 << 6]) == rank(A+H): reveals.append(t)
    if t == 12: assert (U[4] ^ (1 << 6)) & ~sum(A) == 0
    U,V = rows_next(U,V,BASE)
assert reveals == [0,12]
for s in I:
    y = s
    for _ in range(12): y = step(y,n,BASE)
    assert ((y >> 4) & 1) == ((s >> 6) & 1)
print('FUTURE READ: u4(12)=u6(0)=r on all 1024 inputs; P(u4(12)=0)=p.')
print('No single current-position read at times 2 through 11 distinguishes p; time 12 does.')
print('These preparations agree at time 2 but are not equivalent across future protocols.')
print('PASS: exact identities, full seven-site enumeration, connected image counts and rational biases.')
