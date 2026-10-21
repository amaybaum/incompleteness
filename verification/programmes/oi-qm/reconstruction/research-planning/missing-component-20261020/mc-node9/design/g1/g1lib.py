"""G1 design probe (node 9, exploratory, NOT preregistered): shared exact library.

Conventions (fixed once for every script here; integer / Fraction arithmetic only, no floats):
  * n systems, j = 0 (A), 1 (B).
  * Relation label u in V = F2^{2n} (bitmask): x_j at bit 2j, z_j at bit 2j+1.
    Pauli correspondence: x <-> X (the card's hidden card p), z <-> Z (the card's visible card q).
  * Card ontic state s (bitmask): p_j at bit 2j, q_j at bit 2j+1.  <u, s> = popcount(u & s) mod 2,
    i.e. relation u reads the functional  sum_j x_j p_j + z_j q_j.
  * omega(u, v) = sum_j x_j z'_j + z_j x'_j  (mod 2).
  * Card ops on ontic states: swap_j (q_j <-> p_j), couple (q_B ^= q_A, p_A ^= p_B),
    flipq_j (q_j ^= 1), flipp_j (p_j ^= 1); read q_j = record q_j and replace p_j by a fresh fair bit.
  * QM dictionary (calibration only): swap_j <-> H_j, couple <-> CNOT(A->B), flipq_j <-> X_j,
    flipp_j <-> Z_j, read q_j <-> Z_j measurement;  initial |00>  <->  q_A = q_B = 0, p uniform.
"""
from fractions import Fraction as Fr
from itertools import product
from collections import deque

def popc(x): return bin(x).count("1")
def XB(j): return 1 << (2*j)        # x_j bit / p_j bit
def ZB(j): return 1 << (2*j+1)      # z_j bit / q_j bit
def omega(u, v, n):
    r = 0
    for j in range(n):
        r ^= (((u >> 2*j) & 1) & ((v >> (2*j+1)) & 1)) ^ (((u >> (2*j+1)) & 1) & ((v >> 2*j) & 1))
    return r
def pair(u, s): return popc(u & s) & 1

# ---------------- card ontic linear maps -----------------
def onticmap(name, n):
    """returns f: s -> s' (linear bijection on F2^{2n}) for swap_j / couple."""
    if name.startswith("swap"):
        j = int(name[-1])
        def f(s, j=j):
            p = (s >> 2*j) & 1; q = (s >> (2*j+1)) & 1
            s &= ~(XB(j) | ZB(j))
            return s | (q << 2*j) | (p << (2*j+1))
        return f
    if name == "couple":   # A=0 control, B=1 target: q_B ^= q_A, p_A ^= p_B
        def f(s):
            qA = (s >> 1) & 1; pB = (s >> 2) & 1
            return s ^ (qA << 3) ^ (pB << 0)
        return f
    if name == "phase0":   # gem test only: p_A ^= q_A (symplectic shear, the S-gate analogue)
        def f(s):
            return s ^ ((s >> 1) & 1)
        return f
    raise ValueError(name)

def relpush(f, n):
    """Schroedinger push-forward of relation labels: u' with <u', f(s)> = <u, s> for all s."""
    N = 1 << (2*n); out = {}
    for u in range(N):
        c = [v for v in range(N) if all(pair(v, f(s)) == pair(u, s) for s in range(N))]
        assert len(c) == 1
        out[u] = c[0]
    return out

# ---------------- central extensions E = Z_m x V -----------------
class Ext:
    """E = Z_m x V with (a,u)(b,v) = (a+b+beta(u,v), u^v). Elements encoded as a*N + u."""
    def __init__(self, n, m, beta):
        self.n, self.m = n, m; self.N = 1 << (2*n); N = self.N
        self.beta = beta  # beta[u][v] in Z_m
        self.size = m*N
        self.mul = [[0]*self.size for _ in range(self.size)]
        for g in range(self.size):
            a, u = divmod(g, N)
            for h in range(self.size):
                b, v = divmod(h, N)
                self.mul[g][h] = ((a+b+beta[u][v]) % m)*N + (u ^ v)
        self.inv = [next(h for h in range(self.size) if self.mul[g][h] == 0) for g in range(self.size)]
        self.z = (m//2)*N   # the central element carrying the commutator (order 2)
    def el(self, a, u): return (a % self.m)*self.N + u
    def proj(self, g): return g % self.N
    def cval(self, g): return g // self.N
    def is_cocycle(self):
        b, N, m = self.beta, self.N, self.m
        return all((b[u][v] + b[u ^ v][w] - b[v][w] - b[u][v ^ w]) % m == 0
                   for u in range(N) for v in range(N) for w in range(N))
    def commutator_is(self, form):  # form(u,v) in Z_m
        return all((self.beta[u][v]-self.beta[v][u]-form(u, v)) % self.m == 0
                   for u in range(self.N) for v in range(self.N))
    def sq(self, g): return self.mul[g][g]
    def order(self, g):
        k, h = 1, g
        while h != 0: h = self.mul[h][g]; k += 1
        return k
    def closure(self, gens):
        S = {0}; frontier = list(gens)
        S |= set(gens)
        changed = True
        while changed:
            changed = False
            for g in list(S):
                for h in list(S):
                    k = self.mul[g][h]
                    if k not in S: S.add(k); changed = True
        return frozenset(S)
    def involution_lifts(self, u):
        return [self.el(a, u) for a in range(self.m) if self.sq(self.el(a, u)) == 0]
    def is_hom(self, phi):
        mul = self.mul
        return all(phi[mul[g][h]] == mul[phi[g]][phi[h]] for g in range(self.size) for h in range(self.size)) \
            and len(set(phi)) == self.size
    def inner(self, w):
        return tuple(self.mul[self.mul[w][g]][self.inv[w]] for g in range(self.size))
    def extend(self, S, gen_images, cact=1):
        """Automorphism candidate covering the linear map S (dict u->Su) with (0,e_i) -> gen_images[i].
        cact = +1 (trivial on C) or -1 (inversion on C)."""
        n2 = 2*self.n; N = self.N
        phi = [0]*self.size
        for g in range(self.size):
            a, u = divmod(g, N)
            P = 0; img = 0
            for i in range(n2):
                if (u >> i) & 1:
                    P = self.mul[P][1 << i]          # (0, e_i) encoded as e_i (a=0)
                    img = self.mul[img][gen_images[i]]
            t = self.cval(P)
            assert self.proj(P) == u
            c = (cact*(a - t)) % self.m
            phi[g] = self.mul[self.el(c, 0)][img]
        return tuple(phi)
    def lifts(self, Smap, cact=1):
        """All automorphisms of E covering Smap, acting on C by cact. Brute force over generator images."""
        n2 = 2*self.n; out = []
        for imgs in product(range(self.m), repeat=n2):
            gi = [self.el(imgs[i], Smap[1 << i]) for i in range(n2)]
            phi = self.extend(Smap, gi, cact)
            if self.is_hom(phi) and all(phi[self.el(a, 0)] == self.el(cact*a, 0) for a in range(self.m)):
                out.append(phi)
        return out

def bilinear_beta(n, m, coeff):
    """beta(u,v) = sum_{i,k} coeff[i][k] u_i v_k  (mod m), bits as integers."""
    N = 1 << (2*n)
    return [[sum(coeff[i][k] for i in range(2*n) for k in range(2*n) if (u >> i) & 1 and (v >> k) & 1) % m
             for v in range(N)] for u in range(N)]

def real_pauli_coeff(n, scale=1):
    """beta0(u,v) = scale * z.x'  (s(u) = X^x Z^z, X first): coeff[z_j][x_j] = scale."""
    c = [[0]*(2*n) for _ in range(2*n)]
    for j in range(n): c[2*j+1][2*j] = scale
    return c

# ---------------- extension engine (states = stabilizer-type record groups) -----------------
class ExtTheory:
    """Records: abelian subgroup S of E, |S| = 2^n, S cap C = {0}, projecting onto a Lagrangian.
    Dictionary d: generator relation -> its value-0 lift (an involution).
    Read rule (fixed before testing, same for every extension):
       read relation u: if d(u) in S -> 0; if d(u) z in S -> 1; else outcome o w.p. 1/2 and
       S' = < {g in S : omega(pi g, u) = 0} , d(u) z^o >   (fix u's sign, randomize the conjugate)."""
    def __init__(self, E, dic, ops):
        self.E, self.dic, self.ops = E, dic, ops    # ops: name -> automorphism tuple; reads: 'read_j'
        n = E.n
        self.init_state = E.closure([dic[ZB(j)] for j in range(n)])
        assert self.valid(self.init_state)
    def valid(self, S):
        E = self.E
        return len(S) == 1 << E.n and all(E.cval(g) == 0 for g in S if E.proj(g) == 0) and \
            all(E.mul[g][h] == E.mul[h][g] for g in S for h in S)
    def init(self): return self.init_state
    def step(self, op, S):
        E = self.E
        if op.startswith("read"):
            j = int(op[-1]); u = ZB(j); d0 = self.dic[u]; d1 = E.mul[d0][E.z]
            if d0 in S: return [(0, Fr(1), S)]
            if d1 in S: return [(1, Fr(1), S)]
            keep = [g for g in S if omega(E.proj(g), u, E.n) == 0]
            res = []
            for o, d in ((0, d0), (1, d1)):
                S2 = E.closure(keep + [d]); assert self.valid(S2); res.append((o, Fr(1, 2), S2))
            return res
        phi = self.ops[op]
        S2 = frozenset(phi[g] for g in S); assert self.valid(S2)
        return S2

# ---------------- card theory (direct ontic simulation) -----------------
class CardTheory:
    def __init__(self, n=2, maps=None, hbit=False, init_h=None, read_refresh_h=False):
        """Uniform-support epistemic states over ontic s.  maps: op name -> function on ontic ints.
        Optional appended hidden cell h (bit 2n) for the OI realizability search."""
        self.n = n; self.hbit = hbit; self.rrh = read_refresh_h
        self.maps = maps if maps is not None else default_card_maps(n)
        nb = 2*n + (1 if hbit else 0)
        base = [s for s in range(1 << nb) if all(((s >> (2*j+1)) & 1) == 0 for j in range(n))]
        if hbit and init_h is not None:
            base = [s for s in base if ((s >> (2*n)) & 1) == init_h]
        self.init_state = frozenset(base)
    def init(self): return self.init_state
    def step(self, op, S):
        if op.startswith("read"):
            j = int(op[-1]); res = []
            for o in (0, 1):
                part = [s for s in S if ((s >> (2*j+1)) & 1) == o]
                if not part: continue
                post = set()
                for s in part:
                    for b in (0, 1):
                        t = (s & ~XB(j)) | (b << 2*j)
                        if self.rrh:
                            for c in (0, 1): post.add((t & ~(1 << 2*self.n)) | (c << 2*self.n))
                        else: post.add(t)
                res.append((o, Fr(len(part), len(S)), frozenset(post)))
            return res
        f = self.maps[op]
        return frozenset(f(s) for s in S)

def default_card_maps(n=2):
    m = {}
    for j in range(n):
        m["swap%d" % j] = onticmap("swap%d" % j, n)
        m["flipq%d" % j] = (lambda s, j=j: s ^ ZB(j))
        m["flipp%d" % j] = (lambda s, j=j: s ^ XB(j))
    if n == 2: m["couple"] = onticmap("couple", n)
    return m

# ---------------- exact QM (Gaussian-integer amplitudes, projective) -----------------
def cmul(a, b): return (a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def cadd(a, b): return (a[0]+b[0], a[1]+b[1])
def n2(a): return a[0]*a[0]+a[1]*a[1]
I2 = [[(1, 0), (0, 0)], [(0, 0), (1, 0)]]
H2 = [[(1, 0), (1, 0)], [(1, 0), (-1, 0)]]          # sqrt(2) H, normalization tracked projectively
X2 = [[(0, 0), (1, 0)], [(1, 0), (0, 0)]]
Z2 = [[(1, 0), (0, 0)], [(0, 0), (-1, 0)]]
S2 = [[(1, 0), (0, 0)], [(0, 0), (0, 1)]]
def kron(A, B):
    return [[cmul(A[i//len(B)][k//len(B)], B[i % len(B)][k % len(B)]) for k in range(len(A)*len(B))]
            for i in range(len(A)*len(B))]
def matvec(M, v):
    out = []
    for row in M:
        acc = (0, 0)
        for a, x in zip(row, v): acc = cadd(acc, cmul(a, x))
        out.append(acc)
    return out
def matmul(A, B):
    return [[(sum(cmul(A[i][k], B[k][j])[0] for k in range(len(B))),
              sum(cmul(A[i][k], B[k][j])[1] for k in range(len(B)))) for j in range(len(B[0]))] for i in range(len(A))]
CNOT4 = [[(1 if (r == c and c < 2) or (c >= 2 and r == (c ^ 1)) else 0, 0) for c in range(4)] for r in range(4)]
# basis index = 2*bA + bB ; CNOT A->B flips bB when bA=1

def dm_key(v):
    nrm = sum(n2(a) for a in v)
    key = []
    for a in v:
        for b in v:
            p = cmul(a, (b[0], -b[1]))
            key.append((Fr(p[0], nrm), Fr(p[1], nrm)))
    return tuple(key)

class QMTheory:
    """Exact projective state vectors; key = normalized density matrix (Fractions)."""
    def __init__(self, n=2, gates=None):
        self.n = n; d = 1 << n
        self.gates = gates if gates is not None else default_qm_gates(n)
        self.init_state = tuple([(1, 0)] + [(0, 0)]*(d-1))
    def init(self): return self.init_state
    def canon(self, v):
        # canonical projective representative: divide by gcd content is unnecessary; use dm key for equality
        return v
    def step(self, op, v):
        if op.startswith("read"):
            j = int(op[-1]); d = 1 << self.n; res = []
            nrm = sum(n2(a) for a in v)
            shift = self.n - 1 - j      # qubit j is bit (n-1-j) of the basis index
            for o in (0, 1):
                w = tuple(a if ((i >> shift) & 1) == o else (0, 0) for i, a in enumerate(v))
                p = sum(n2(a) for a in w)
                if p: res.append((o, Fr(p, nrm), w))
            return res
        return tuple(matvec(self.gates[op], v))

def default_qm_gates(n=2):
    g = {}
    if n == 1:
        g["swap0"] = H2; g["flipq0"] = X2; g["flipp0"] = Z2
        return g
    g["swap0"] = kron(H2, I2); g["swap1"] = kron(I2, H2); g["couple"] = CNOT4
    g["flipq0"] = kron(X2, I2); g["flipq1"] = kron(I2, X2)
    g["flipp0"] = kron(Z2, I2); g["flipp1"] = kron(I2, Z2)
    return g

# ---------------- generic exact comparison: product automaton BFS -----------------
def keyof(th, s):
    return dm_key(s) if isinstance(th, QMTheory) else s

def equivalent(T1, T2, alphabet, maxpairs=200000):
    """Exact operational equivalence on every word over `alphabet` (reads included, outcomes branched).
    Returns (True, npairs, ntrans) or (False, word, detail)."""
    s1, s2 = T1.init(), T2.init()
    start = (keyof(T1, s1), keyof(T2, s2))
    seen = {start: ()}; Q = deque([(s1, s2, ())]); ntr = 0
    while Q:
        a, b, w = Q.popleft()
        for op in alphabet:
            ra, rb = T1.step(op, a), T2.step(op, b)
            if op.startswith("read"):
                da = {o: (p, s) for o, p, s in ra}; db = {o: (p, s) for o, p, s in rb}
                if {o: p for o, (p, s) in da.items()} != {o: p for o, (p, s) in db.items()}:
                    return (False, w + (op,), ({o: str(p) for o, (p, s) in da.items()}, {o: str(p) for o, (p, s) in db.items()}))
                nxt = [(da[o][1], db[o][1], w + (op + "=%d" % o,)) for o in da]
            else:
                nxt = [(ra, rb, w + (op,))]
            for x, y, w2 in nxt:
                ntr += 1
                k = (keyof(T1, x), keyof(T2, y))
                if k not in seen:
                    seen[k] = w2; Q.append((x, y, w2))
                    if len(seen) > maxpairs: raise RuntimeError("cap")
    return (True, len(seen), ntr)

def reachable(T, alphabet):
    s = T.init(); seen = {keyof(T, s): s}; Q = deque([s]); ntr = 0; nbr = 0
    while Q:
        a = Q.popleft()
        for op in alphabet:
            r = T.step(op, a)
            outs = [x for _, _, x in r] if op.startswith("read") else [r]
            if op.startswith("read"): nbr += len(r)
            else: ntr += 1
            for x in outs:
                k = keyof(T, x)
                if k not in seen: seen[k] = x; Q.append(x)
    return seen, ntr, nbr

def run_word(T, word, final_read):
    """Deterministic gate word then a read; returns outcome distribution {o: Fraction}."""
    s = T.init()
    for op in word: s = T.step(op, s)
    return {o: p for o, p, _ in T.step(final_read, s)}

W6 = ["swap0", "couple"]*3
W7 = W6 + ["swap0"]

# ---------------- helpers for lifts relative to a dictionary -----------------
def lift_from_dict_images(E, Smap, dic, imgs, cact=1):
    """Automorphism with phi(dic[e_i]) = imgs[i]; returns tuple or None if not an automorphism."""
    gi = []
    for i in range(2*E.n):
        e = 1 << i; a = E.cval(dic[e])
        gi.append(E.mul[imgs[i]][E.el(-cact*a, 0)])
    phi = E.extend(Smap, gi, cact)
    if E.is_hom(phi) and all(phi[E.el(a, 0)] == E.el(cact*a, 0) for a in range(E.m)):
        return phi
    return None

def ert_lift(E, Smap, dic):
    """Elementary-record transport (ERT): each elementary record d(e_i) is carried to the product of the
    elementary records of S e_i, with the card's value (no sign).  Returns (phi or None, status)."""
    imgs = []
    for i in range(2*E.n):
        su = Smap[1 << i]; facs = [dic[1 << k] for k in range(2*E.n) if (su >> k) & 1]
        for x in facs:
            for y in facs:
                if E.mul[x][y] != E.mul[y][x]:
                    return None, "ambiguous (image of e_%d is a product of non-commuting elementary records)" % i
        p = 0
        for x in facs: p = E.mul[p][x]
        imgs.append(p)
    phi = lift_from_dict_images(E, Smap, dic, imgs)
    return (phi, "ok") if phi is not None else (None, "not an automorphism")

def default_dict(E):
    """value-0 lift of each generator: the involution lift with smallest central coordinate."""
    d = {}
    for i in range(2*E.n):
        L = E.involution_lifts(1 << i)
        d[1 << i] = min(L) if L else None
    return d

def card_relmaps(n=2):
    names = ["swap%d" % j for j in range(n)] + (["couple"] if n == 2 else [])
    return {nm: relpush(onticmap(nm, n), n) for nm in names}

def ext_theory_ops(E, dic, lifts):
    """lifts: dict name->automorphism for swap/couple; flips added as the inner automorphisms that change
    record values exactly as the card flips do (flipq_j = conj by d(X_j), flipp_j = conj by d(Z_j))."""
    ops = dict(lifts)
    for j in range(E.n):
        ops["flipq%d" % j] = value_twist(E, XB(j))
        ops["flipp%d" % j] = value_twist(E, ZB(j))
    return ops

def value_twist(E, w):
    """(a,u) -> (a + (m/2) omega(w,u), u): flips the value of every record u with omega(w,u) = 1, exactly as the
    card translation does.  An automorphism of every extension; equal to conjugation by any lift of w when
    the commutator is omega (checked in controls.py)."""
    return tuple(E.el(E.cval(g) + (E.m//2)*omega(w, E.proj(g), E.n), E.proj(g)) for g in range(E.size))

ALPH_FULL = ["swap0", "swap1", "couple", "flipq0", "flipq1", "flipp0", "flipp1", "read0", "read1"]
