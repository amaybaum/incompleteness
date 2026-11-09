# REVIEW CONTROLS for REACHABLE.md (sha256 c65a9d37...). CONTROLS ONLY, NOT EVIDENCE.
# Exact F_2 / integer / Fraction arithmetic. Run: python3 -I -B controls_review.py
# RC1  Randomized protocols in the class "affine symplectic steps + P2 supplies + P1-terminal registration,
#      conditioning on records registered so far" (a superset of QA's class N on U'): every fully conditioned
#      carrier law has Bloch image in V0 and a Q*-totally-singular determined carrier set (centre-free steps).
#      Countercontrols that must break: (a) retrodictive conditioning (carrier law at t given later records),
#      (b) registered cell coupled again (P1 terminality dropped), (c) non-symmetric K (non-symplectic),
#      (d) a supplied sharp cell (P2 dropped), (e) centre terms (must keep V0 but break Q* = 0).
# RC2  AGL(4,2): the encoded-induced maps of affine carrier bijections on all laws are exactly the 48 signed
#      permutations (24 det +1, 24 det -1), each realized 16 times (cross-check of AUDIT-C2's 384 + 384).
# RC3  Static: the four non-affine symmetric triangle rules do not conserve Q = sum u_i v_i (Lemma Q(i) fails),
#      the four affine ones do. No reachable set is computed under any non-affine rule (pre-F hygiene).
import itertools, random
from fractions import Fraction as Fr

random.seed(20261108)
results = []
def check(name, cond):
    results.append(bool(cond)); print(("PASS " if cond else "FAIL ") + name)

# ---------- F_2 linear algebra on bitmask rows ----------
def rank_insert(basis, v):
    # basis: dict pivot->row ; returns reduced v (0 if in span)
    for p in sorted(basis, reverse=True):
        if v >> p & 1: v ^= basis[p]
    return v
def add_to_basis(basis, v):
    v = rank_insert(basis, v)
    if v:
        p = v.bit_length() - 1
        # keep basis reduced w.r.t. new pivot
        for q in list(basis):
            if basis[q] >> p & 1: basis[q] ^= v
        basis[p] = v
        return True
    return False
def in_span(basis, v): return rank_insert(basis, v) == 0

# ---------- model ----------
# Global state: n cells, cell c has slots u_c (index 2c) and v_c (index 2c+1).
# Each slot value = affine function of m uniform independent unknown bits w: row (bitmask over w) + const.
# A functional f on slots is a bitmask over 2n slot indices. Its value = XOR of slot rows.
class World:
    def __init__(s): s.rows = []; s.consts = []; s.m = 0; s.terminal = set(); s.cons = {}  # cons: basis over w
    def new_unknown(s): s.m += 1; return 1 << (s.m - 1)
    def add_cell(s, kind, val=0):
        # kind: 'src' both unknown; 'ready_u' u known=val, v unknown; 'ready_v'; 'sharp' both known
        if kind == 'src':   s.rows += [s.new_unknown(), s.new_unknown()]; s.consts += [0, 0]
        if kind == 'ready_u': s.rows += [0, s.new_unknown()]; s.consts += [val, 0]
        if kind == 'ready_v': s.rows += [s.new_unknown(), 0]; s.consts += [0, val]
        if kind == 'sharp': s.rows += [0, 0]; s.consts += [val, random.randint(0, 1)]
        return len(s.rows) // 2 - 1
    def ncell(s): return len(s.rows) // 2
    def step(s, cells, K, centre=False):
        # second-order step u' = K u + v, v' = u on the listed cells (K: dict (i,j)->bit over local indices)
        U = [(s.rows[2 * c], s.consts[2 * c]) for c in cells]
        V = [(s.rows[2 * c + 1], s.consts[2 * c + 1]) for c in cells]
        for a, c in enumerate(cells):
            r, k = V[a]
            for b in range(len(cells)):
                if K.get((a, b), 0): r ^= U[b][0]; k ^= U[b][1]
            s.rows[2 * c], s.consts[2 * c] = r, k
            s.rows[2 * c + 1], s.consts[2 * c + 1] = U[a]
    def translate(s, slot): s.consts[slot] ^= 1
    def value_row(s, f):  # functional f over slots -> (row over w, const)
        r = k = 0
        for i in range(len(s.rows)):
            if f >> i & 1: r ^= s.rows[i]; k ^= s.consts[i]
        return r, k
    def register(s, slot, w_true):
        r, k = s.rows[slot], s.consts[slot]
        add_to_basis(s.cons, r)   # conditioning on the record value (branch fixed by w_true)
        return (bin(r & w_true).count('1') + k) & 1

def carrier_image(W, carrier):
    c1, c2 = carrier
    z1, x1, z2, x2 = 2 * c1, 2 * c1 + 1, 2 * c2, 2 * c2 + 1
    F = {'x': 1 << x1, 'y': (1 << z1) | (1 << x1) | (1 << z2) | (1 << x2), 'z': 1 << z1}
    img = []
    for a in 'xyz':
        r, _ = W.value_row(F[a])
        img.append(1 if in_span(W.cons, r) else 0)  # 1 = determined (sign irrelevant for the test)
    # determined carrier functionals: test Q* on all 15 nonzero carrier functionals
    ts = True
    for bits in range(1, 16):
        f = 0
        for i, sl in enumerate((z1, x1, z2, x2)):
            if bits >> i & 1: f |= 1 << sl
        r, _ = W.value_row(f)
        if in_span(W.cons, r):
            qs = ((bits & 1) * (bits >> 1 & 1) + (bits >> 2 & 1) * (bits >> 3 & 1)) & 1
            if qs: ts = False
    return sum(img), ts

def rand_sym_K(k, centre=False, nonsym=False):
    K = {}
    for a in range(k):
        for b in range(a + 1, k):
            x = random.randint(0, 1); K[(a, b)] = x; K[(b, a)] = x
            if nonsym and random.random() < 0.5: K[(b, a)] ^= 1
        if centre: K[(a, a)] = random.randint(0, 1)
    return K

def run(mode, trials=3000):
    worst_det = 0; ts_ok = True
    for _ in range(trials):
        W = World(); carrier = (W.add_cell('src'), W.add_cell('src'))
        anc = []
        for _ in range(random.randint(1, 5)):
            kind = random.choice(['ready_u', 'ready_v'])
            anc.append(W.add_cell(kind, random.randint(0, 1)))
        if mode == 'sharp': anc.append(W.add_cell('sharp'))
        hidden = [W.add_cell('src') for _ in range(random.randint(0, 2))]
        w_true = random.getrandbits(max(W.m, 1))
        active = list(carrier) + anc + hidden
        snapshot = None
        for t in range(random.randint(1, 6)):
            cells = [c for c in active if c not in W.terminal or mode == 'nonterminal']
            sub = random.sample(cells, random.randint(2, min(4, len(cells))))
            W.step(sub, rand_sym_K(len(sub), centre=(mode == 'centre'), nonsym=(mode == 'nonsym')))
            if random.random() < 0.3: W.translate(random.randrange(len(W.rows)))
            if random.random() < 0.6:
                cand = [c for c in anc + hidden if c not in W.terminal]
                if cand:
                    c = random.choice(cand); W.register(2 * c + random.randint(0, 1), w_true); W.terminal.add(c)
            if mode == 'retro' and snapshot is None and t == 0:
                snapshot = (list(W.rows), list(W.consts))
        if mode == 'retro':
            # one more read of a carrier slot via the register of its meter = register carrier slot copy
            # (a native minimal read registers a meter slot equal to the carrier slot): condition the
            # carrier law at the snapshot time on all records, including the later ones.
            m = W.add_cell('ready_u', 0); W.step([carrier[0], m], {(0, 1): 1, (1, 0): 1})
            W.register(2 * m, w_true); W.terminal.add(m)
            W.rows, W.consts = snapshot[0] + W.rows[len(snapshot[0]):], snapshot[1] + W.consts[len(snapshot[1]):]
        d, ts = carrier_image(W, carrier)
        worst_det = max(worst_det, d); ts_ok = ts_ok and ts
    return worst_det, ts_ok

d, ts = run('native')
check(f"RC1 symplectic+P1+P2, forward conditioning: at most one f_a determined (max {d}) => image in V0", d <= 1)
check("RC1 centre-free symmetric steps: determined carrier set Q*-totally singular", ts)
d, ts = run('retro');       check(f"RC1(a) countercontrol retrodictive conditioning breaks V0 (max {d})", d >= 2)
d, ts = run('nonterminal'); check(f"RC1(b) countercontrol registered cell re-coupled breaks V0 (max {d})", d >= 2)
d, ts = run('nonsym');      check(f"RC1(c) countercontrol non-symmetric K breaks V0 (max {d})", d >= 2)
d, ts = run('sharp');       check(f"RC1(d) countercontrol sharp supplied cell breaks V0 (max {d})", d >= 2)
d, ts = run('centre');      check(f"RC1(e) centre terms keep V0 (max {d}) but break Q*=0 (ts={ts})", d <= 1 and not ts)

# ---------- RC2: AGL(4,2) induced maps ----------
# carrier coords (z1,x1,z2,x2) bits 0..3; functional f_a as row vector; pullback f∘A = f M (+ f t)
fz, fx, fy = 0b0001, 0b0010, 0b1111
FA = [fx, fy, fz]  # order x, y, z
def matvec_row(f, M):  # f (row bitmask) times M (list of 4 column bitmasks? use rows): (fM)_j = sum_i f_i M[i][j]
    out = 0
    for i in range(4):
        if f >> i & 1: out ^= M[i]
    return out
from collections import Counter
maps = Counter()
for rows in itertools.product(range(16), repeat=4):
    # invertibility
    b = {}; ok = all(add_to_basis(b, r) for r in rows)
    if not ok: continue
    pulls = [matvec_row(f, rows) for f in FA]
    if all(p in FA for p in pulls) and len(set(pulls)) == 3:
        perm = tuple(FA.index(p) for p in pulls)
        for t in range(16):
            signs = tuple((-1) ** (bin(f & t).count('1') & 1) for f in FA)
            maps[(perm, signs)] += 1
def det_sp(perm, signs):
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
    s = (-1) ** inv
    for x in signs: s *= x
    return s
check(f"RC2 AGL(4,2): {sum(maps.values())} inducing bijections, {len(maps)} distinct maps, each x16",
      sum(maps.values()) == 768 and len(maps) == 48 and set(maps.values()) == {16})
check("RC2 24 of det +1 and 24 of det -1",
      sum(1 for k in maps if det_sp(*k) == 1) == 24 and sum(1 for k in maps if det_sp(*k) == -1) == 24)

# ---------- RC3: Q conservation of triangle rules ----------
gs = {'0': lambda a, b: 0, '1': lambda a, b: 1, 'XOR': lambda a, b: a ^ b, 'XNOR': lambda a, b: 1 ^ a ^ b,
      'AND': lambda a, b: a & b, 'NAND': lambda a, b: 1 ^ (a & b), 'OR': lambda a, b: a | b, 'NOR': lambda a, b: 1 ^ (a | b)}
def step3(g, s):
    u, v = s[:3], s[3:]
    return tuple((g(u[(i - 1) % 3], u[(i + 1) % 3]) + v[i]) % 2 for i in range(3)) + tuple(u)
def Q(s): return sum(s[i] * s[3 + i] for i in range(3)) % 2
cons = {n: sum(Q(step3(g, s)) != Q(s) for s in itertools.product((0, 1), repeat=6)) for n, g in gs.items()}
print("RC3 configurations (of 64) changing Q:", cons)
# constant offset c: u' = c + ..., Q' = sum (c + ...) u_i  -> adds c*sum u_i ; so '1','XNOR' also break Q
check("RC3 linear rules 0 and XOR conserve Q", cons['0'] == 0 and cons['XOR'] == 0)
check("RC3 every non-affine rule (AND, NAND, OR, NOR) changes Q on some configuration",
      all(cons[n] > 0 for n in ('AND', 'NAND', 'OR', 'NOR')))
print("affine-with-offset rules 1, XNOR change Q on", cons['1'], cons['XNOR'], "configs (offset = translation)")

# ---------- RC4: arithmetic ----------
# 3/4 herald: three equiprobable V0 branches -> l1 <= 1 ; (2/3,2/3,-1/3) has l1 5/3.
V0 = [(0, 0, 0)] + [tuple(s * (i == j) for j in range(3)) for i in range(3) for s in (1, -1)]
best = max(sum(abs(sum(Fr(1, 3) * v[i] for v in tri)) for i in range(3)) for tri in itertools.product(V0, repeat=3))
check(f"RC4 any 1/3,1/3,1/3 mixture of V0 points has l1 <= 1 (max {best})", best <= 1)

print("ALL PASS" if all(results) else "SOME FAIL", f"({sum(results)}/{len(results)})")
