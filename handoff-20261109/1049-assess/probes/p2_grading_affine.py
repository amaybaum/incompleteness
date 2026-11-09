"""P2 -- exact generic check (#1049 re-assessment, WIP / UNVERIFIED, model-written).

Paper claims checked on generic graphs and generic coefficients (not on an OI mechanism):
 (A) Lemma G1 (sublattice grading, quarter-phase DESIGN node 1) holds MODULO CONSTANTS for
     affine second-order steps u' = K(t) u - v + b(t), v' = u, with arbitrary per-tick
     symmetric zero-diagonal coefficients on a bipartite graph and arbitrary per-tick,
     per-site constant offsets b(t): every slot is (linear form in variables of one type)
     + (constant).  Countercontrols: a self-term k_ii != 0, and an odd cycle, break it.
 (B) Lemma Q(i) (q = 2 conservation of Q(u,v) = sum u_i v_i) holds for b = 0 and FAILS for
     some b != 0: Q(step(z)) = Q(z) + b.u exactly (exhaustive, small graphs).
 (C) Two runs of the same affine process differing only in linear parts differ by a map
     that is linear in the state and independent of the offsets (G2 step 3 for affine steps).
Representation: a slot is a pair (coefficient vector over the 2n initial variables, constant).
"""
import itertools, random, sys
random.seed(1049)

def graph(kind, n):
    E = set()
    if kind == "cycle":
        for i in range(n):
            E.add(frozenset((i, (i + 1) % n)))
    return E

def colouring(n, E):
    col = {0: 0}
    stack = [0]
    while stack:
        i = stack.pop()
        for e in E:
            if i in e:
                (j,) = tuple(e - {i})
                if j not in col:
                    col[j] = 1 - col[i]; stack.append(j)
    return col

def run_affine(n, E, q, T, selfterm=False, offsets=True):
    # initial variables: u_i(0) -> index i ; v_i(0) -> index n+i
    u = [([1 if k == i else 0 for k in range(2*n)], 0) for i in range(n)]
    v = [([1 if k == n+i else 0 for k in range(2*n)], 0) for i in range(n)]
    hist = [(u, v)]
    for t in range(T):
        K = [[0]*n for _ in range(n)]
        for e in E:
            i, j = tuple(e)
            if random.random() < 0.8:           # per-tick, per-edge arming
                K[i][j] = K[j][i] = random.randrange(q)
        if selfterm:
            K[0][0] = 1
        b = [random.randrange(q) if offsets else 0 for _ in range(n)]
        nu = []
        for i in range(n):
            vec = [(-v[i][0][k]) % q for k in range(2*n)]
            const = (-v[i][1] + b[i]) % q
            for j in range(n):
                if K[i][j]:
                    vec = [(vec[k] + K[i][j]*u[j][0][k]) % q for k in range(2*n)]
                    const = (const + K[i][j]*u[j][1]) % q
            nu.append((vec, const))
        u, v = nu, u
        hist.append((u, v))
    return hist

def graded(hist, n, col):
    # type of u_i(0) is chi_i, of v_i(0) is chi_i + 1 (mod 2); slot u_i(t) must involve only
    # variables of type t + chi_i, v_i(t) only of type t + chi_i + 1
    typ = [col[i] for i in range(n)] + [(col[i] + 1) % 2 for i in range(n)]
    for t, (u, v) in enumerate(hist):
        for i in range(n):
            for (vec, _), need in ((u[i], (t + col[i]) % 2), (v[i], (t + col[i] + 1) % 2)):
                for k, a in enumerate(vec):
                    if a and typ[k] != need:
                        return False
    return True

ok = True
# (A) grading modulo constants
for q in (2, 3, 5):
    for trial in range(20):
        n = 6
        E = graph("cycle", n)
        col = colouring(n, E)
        h = run_affine(n, E, q, T=12)
        ok &= graded(h, n, col)
    # countercontrols
    E6 = graph("cycle", 6); col6 = colouring(6, E6)
    broke_self = not all(graded(run_affine(6, E6, q, T=12, selfterm=True), 6, col6) for _ in range(5))
    E5 = graph("cycle", 5)
    col5 = {i: i % 2 for i in range(5)}                  # not a proper colouring: edge (4,0)
    broke_odd = not all(graded(run_affine(5, E5, q, T=12), 5, col5) for _ in range(5))
    print(f"(A) q={q}: affine grading mod constants on C6 holds in 20 random runs: {ok}; "
          f"self-term breaks it: {broke_self}; odd cycle C5 breaks it: {broke_odd}")
    ok &= broke_self and broke_odd

# (B) Lemma Q(i) at q = 2: exhaustive on small graphs
def step(u, v, K, b):
    n = len(u)
    nu = tuple((sum(K[i][j]*u[j] for j in range(n)) - v[i] + b[i]) % 2 for i in range(n))
    return nu, u

def Q(u, v):
    return sum(a*c for a, c in zip(u, v)) % 2

for n in (3, 4):
    allK_ok_b0 = True; identity_ok = True; some_b_breaks = False
    pairs = [(i, j) for i in range(n) for j in range(i+1, n)]
    for bits in itertools.product((0, 1), repeat=len(pairs)):
        K = [[0]*n for _ in range(n)]
        for (i, j), x in zip(pairs, bits):
            K[i][j] = K[j][i] = x
        for b in itertools.product((0, 1), repeat=n):
            for u in itertools.product((0, 1), repeat=n):
                for v in itertools.product((0, 1), repeat=n):
                    nu, nv = step(u, v, K, b)
                    dQ = (Q(nu, nv) - Q(u, v)) % 2
                    bu = sum(x*y for x, y in zip(b, u)) % 2
                    if dQ != bu:
                        identity_ok = False
                    if not any(b) and dQ != 0:
                        allK_ok_b0 = False
                    if any(b) and dQ != 0:
                        some_b_breaks = True
    print(f"(B) n={n}, all symmetric zero-diagonal K over F2: Q conserved for b=0: {allK_ok_b0}; "
          f"Q(step z)-Q(z) = b.u exactly: {identity_ok}; some b!=0 breaks conservation: {some_b_breaks}")
    ok &= allK_ok_b0 and identity_ok and some_b_breaks

# (C) offsets cancel from the run difference
q = 5
for trial in range(50):
    n = 4
    L0 = [[random.randrange(q) for _ in range(n)] for _ in range(n)]
    L1 = [[random.randrange(q) for _ in range(n)] for _ in range(n)]
    b = [random.randrange(q) for _ in range(n)]
    x = [random.randrange(q) for _ in range(n)]
    p0 = [(sum(L0[i][j]*x[j] for j in range(n)) + b[i]) % q for i in range(n)]
    p1 = [(sum(L1[i][j]*x[j] for j in range(n)) + b[i]) % q for i in range(n)]
    lin = [(sum((L1[i][j]-L0[i][j])*x[j] for j in range(n))) % q for i in range(n)]
    ok &= all((p1[i]-p0[i]) % q == lin[i] for i in range(n))
print(f"(C) run difference of affine processes with common offsets is linear and offset-free: {ok}")
print("ALL PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
