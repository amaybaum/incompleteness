"""o8_exclusive.py -- research/origin, round 3, node O8: the exclusive readout as a premise.

QUESTION. The single open Origin premise after round 2 is an exclusive measure-and-re-prepare readout: KB-D (read
the frame, re-randomize the memory) together with its exclusivity clause KB-D2 (no passive readout of any nontrivial
partition is available), or in continuous form the cosine re-preparation law with no conditioning readout. O5-T1a
showed on {0,1}^2 that one passive readout of any of the 14 nontrivial partitions, with the exchanges, restores the
simplex. This script (i) checks the general form proved in the design module OriginExclusive (any finite carrier,
any nontrivial cell, every permutation: every point mass reachable), replicating the module's construction exactly;
(ii) checks the kernel facts the module uses (the native Lueders readout is the block pinching of the ancilla values;
which algebras it observes passively); (iii) runs the disguise test on the knowledge-balance toy: does the premise
restate the Discrete witness, the balanced mixer, or OI+-1's clause; (iv) checks the continuous form's cost.

CHECKS.
 X1   N = 2..5 configurations, every nontrivial cell C: the closure of the uniform state under the step
      w -> push(sigma, w.1_C) + push(tau, w.1_{not C}) (read, outcome-dependent permutation, forget) contains every
      point mass; its size is recorded and compared with C(2N-1, N), the number of distributions with masses in
      (1/N)Z>=0.
 X1b  the module's construction: pi = swap(pi1(x), d) o pi1 with pi1 = swap(y, c) (c = min C, d = min of the
      complement) has pi(y) in C and pi(x) not in C, and the step with sigma = pi^-1 o swap(pi x, pi y), tau = pi^-1
      equals mergeInto(x, y, w) exactly, for all x != y, all nontrivial cells, N = 2..5, on 3 rational states each.
 X1c  collecting every y != x0 onto x0 by successive merges from the uniform state gives the point mass at x0.
 X2   control: for C = empty and C = all, the closure of the uniform state is the uniform state alone (N = 2..5).
 X3   the kernel's native readout on A = Fin 2, ancilla sizes 2 and 3 (carrier A x Fin n, entries exact): every
      Lueders branch localLuders k (OperationalAssembly:191, readout_is_localLuders :658) equals the block pinching
      P_k X P_k (P_k the projector on ancilla value k; CentralObservation blockPinch) on all matrix units;
      sum_k localLuders k X = X on every ancilla-classical matrix unit; the sum sends E_{(0,0),(0,1)} to 0;
      localLuders j o localLuders k = [j = k] localLuders k on all matrix units.
 X3b  labellings of A x Fin 2 (A = Fin 2): refining the ancilla value (Prod.snd; id; the three blocks
      {(0,0)}, {(1,0)}, {(0,1),(1,1)}): the native readout is passive on every matrix unit of the labelling's algebra
      and its outcome 0 has probability 1 on the pure state (0,0) and 0 on (0,1); straddling (one block; the system
      value): some matrix unit of the algebra is not fixed by the observe-and-forget.
 X4   disguise test on the toy (Omega = {0,1}^2, configurations (z, x), all 24 permutations; readouts by the three
      partitions Z: z, X: x, Y: z xor x):
      X4a access (S4, KB-D for Z, X, Y): the body (hull of the reachable states) has the 6 pair states as extreme
          points; some permutation maps z+ to x+, which is extreme and z-balanced; the only reachable state with
          z-mass 1 is z+; KB-D's observe-and-forget of Z equals the frame dephasing r z+ + (1-r) z- on every
          reachable state; the sandwich z+, sigma, [observe-and-forget], sigma^-1, read z gives (1, 1/2); for every
          one of the 14 nontrivial partitions P some reachable state has a P-conditioned posterior outside the body
          (no passive readout of P is compatible with the body).
      X4b for each of the 14 nontrivial partitions P, access (S4, KB-D for Z, X, Y, passive P): every point mass is
          reachable; the extreme points of the body are the 4 point masses; no extreme point is balanced for any
          partition; the sandwich from the point-mass seed (0,1) with the exchange of z and x gives (1, 1/2) when
          KB-D's observe-and-forget of Z is the 'dephasing', which moves the pure state (0,1) of the frame face z = 0
          (memory erasure); with the fresh-record dephasing (copy z into a blank bit, discard it) the visibility is 0
          for every permutation and every point-mass seed.
      X4c access (S4, passive Z): every point mass reachable, extreme points the 4 point masses, none balanced.
      Summary: exclusivity (X4a) holds exactly where a pure frame state is carried to a pure balanced state.
 X5   OI+-1's clause is about the pair: product-register composites of two toy tokens with local readouts (each
      token read once by Z, X or Y): every CHSH value over the 16 joint configurations lies in [-2, 2].
 X6   continuous form (circle substratum): the conditioning readout of half-circles on the dyadic grid
      {j pi / 2^m} together with the grid rotations reaches every elementary arc (intersection of two grid
      half-circles); the table (elementary arcs x grid half-circles; the cosine-law readout has the same
      first-outcome statistics on these preparations) has rank 2^m + 1 for m = 1..5; the cosine law alone gives rank
      3 on 12 Pythagorean directions.
DECISION RULE (fixed before the first run; the verdict is generated from the measured booleans):
  NOGO_GENERAL := X1 and X1b and X1c.   CONTROL := X2.   KERNEL_FORM := X3 and X3b.
  DISGUISE_LOCATED := X4a and X4b and X4c and X5.   CONTINUOUS := X6.
  VERDICT VOID if any countercontrol is True.
  VERDICT EXCLUSIVITY-REFUTED-AND-LOCATED iff NOGO_GENERAL and CONTROL and KERNEL_FORM and DISGUISE_LOCATED and
    CONTINUOUS; otherwise VERDICT MIXED with the failing items listed.
COUNTERCONTROLS (must be False):
  CC1 the trivial cell C = all (N = 3) reaches a point mass;
  CC2 the native readout's observe-and-forget fixes E_{(0,0),(0,1)} (coherence between ancilla values);
  CC3 in the access of X4a the z-conditioned posteriors of x+ lie in the body (a passive decomposition at x+);
  CC4 the system-value labelling (straddling) makes the native readout passive on its algebra;
  CC5 the access of X4a reaches a point mass.

Run: python3 -I -B o8_exclusive.py > o8_exclusive.out 2> o8_exclusive.err; echo "exit $?" >> o8_exclusive.err
"""

from fractions import Fraction as F
from itertools import permutations, combinations, product
from math import comb

RES = {}
CC = {}
print("== o8_exclusive ==")
print()


# ---------------------------------------------------------------------------------------------------------------
# X1, X1b, X1c, X2 -- the classical carrier, any cell
# ---------------------------------------------------------------------------------------------------------------

def push(sig, w):
    """push(sig, w)(z) = w(sig^-1 z): the mass at x moves to sig(x)."""
    v = [F(0)] * len(w)
    for i, a in enumerate(w):
        v[sig[i]] += a
    return tuple(v)


def in_cell(C, w):
    return tuple(a if i in C else F(0) for i, a in enumerate(w))


def out_cell(C, w):
    return tuple(F(0) if i in C else a for i, a in enumerate(w))


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def placements(v, perms):
    return {push(s, v) for s in perms}


def closure(N, C, cap=100000):
    perms = list(permutations(range(N)))
    seed = tuple([F(1, N)] * N)
    seen = {seed}
    frontier = [seed]
    while frontier:
        new = []
        for w in frontier:
            ins = placements(in_cell(C, w), perms)
            outs = placements(out_cell(C, w), perms)
            for a in ins:
                for b in outs:
                    u = add(a, b)
                    if u not in seen:
                        seen.add(u)
                        new.append(u)
                        if len(seen) > cap:
                            raise RuntimeError("closure cap exceeded")
        frontier = new
    return seen


def point_mass(N, x):
    return tuple(F(1) if i == x else F(0) for i in range(N))


def nontrivial_cells(N):
    out = []
    for k in range(1, N):
        out.extend(frozenset(c) for c in combinations(range(N), k))
    return out


print("-- X1: any finite carrier, any nontrivial cell, every permutation")
x1 = True
for N in range(2, 6):
    cells = nontrivial_cells(N)
    sizes = set()
    ok_all = True
    for C in cells:
        R = closure(N, C)
        ok = all(point_mass(N, x) in R for x in range(N))
        ok_all = ok_all and ok
        sizes.add(len(R))
    expected = comb(2 * N - 1, N)
    x1 = x1 and ok_all and sizes == {expected}
    print(f"X1  N = {N}: {len(cells)} nontrivial cells; every point mass reachable for every cell: {ok_all}; "
          f"closure sizes {sorted(sizes)} (C(2N-1, N) = {expected})")
RES["X1"] = x1
print(f"X1  -> {x1}")
print()


def swap_fn(a, b, N):
    return tuple(b if i == a else a if i == b else i for i in range(N))


def compose(f, g):
    """(f o g)(i) = f(g(i))."""
    return tuple(f[g[i]] for i in range(len(g)))


def inverse(f):
    inv = [0] * len(f)
    for i, j in enumerate(f):
        inv[j] = i
    return tuple(inv)


def merge_into(x, y, w):
    v = list(w)
    v[x] = w[x] + w[y]
    v[y] = F(0)
    return tuple(v)


print("-- X1b: the module's construction, replicated exactly")
x1b = True
count = 0
for N in range(2, 6):
    states = [tuple(F(i + 1, 2 * N + 3) for i in range(N)),
              tuple(F((3 * i) % N, N + 1) for i in range(N)),
              tuple(F(1, N) for _ in range(N))]
    for C in nontrivial_cells(N):
        c = min(C)
        d = min(i for i in range(N) if i not in C)
        for x in range(N):
            for y in range(N):
                if x == y:
                    continue
                pi1 = swap_fn(y, c, N)
                pi2 = swap_fn(pi1[x], d, N)
                pi = compose(pi2, pi1)
                sep = pi[y] in C and pi[x] not in C
                pinv = inverse(pi)
                sigma = compose(pinv, swap_fn(pi[x], pi[y], N))
                tau = pinv
                for w in states:
                    v = push(pi, w)
                    stepped = add(push(sigma, in_cell(C, v)), push(tau, out_cell(C, v)))
                    x1b = x1b and sep and stepped == merge_into(x, y, w)
                    count += 1
RES["X1b"] = x1b
print(f"X1b {count} cases (N = 2..5, every nontrivial cell, every x != y, 3 states): pi(y) in C, pi(x) not in C, and "
      f"step = mergeInto(x, y, w) in every case: {x1b}")

x1c = True
for N in range(2, 6):
    for x0 in range(N):
        w = tuple([F(1, N)] * N)
        for y in range(N):
            if y != x0:
                w = merge_into(x0, y, w)
        x1c = x1c and w == point_mass(N, x0)
RES["X1c"] = x1c
print(f"X1c successive merges onto x0 from the uniform state give the point mass at x0 (N = 2..5, every x0): {x1c}")
print()

print("-- X2: control, the trivial cells")
x2 = True
for N in range(2, 6):
    for C in (frozenset(), frozenset(range(N))):
        R = closure(N, C)
        x2 = x2 and R == {tuple([F(1, N)] * N)}
RES["X2"] = x2
CC["CC1"] = point_mass(3, 0) in closure(3, frozenset(range(3)))
print(f"X2  C = empty and C = all, N = 2..5: the closure is the uniform state alone: {x2}")
print()


# ---------------------------------------------------------------------------------------------------------------
# X3, X3b -- the kernel's native readout on the matrix carrier
# ---------------------------------------------------------------------------------------------------------------

def carrier(nA, n):
    return [(a, k) for a in range(nA) for k in range(n)]


def unit(idx, p, q):
    M = {}
    M[(idx.index(p), idx.index(q))] = F(1)
    return M


def mat_eq(M, Nm):
    keys = set(M) | set(Nm)
    return all(M.get(k, F(0)) == Nm.get(k, F(0)) for k in keys)


def luders_by_def(idx, k, M):
    """Entry-wise from the kernel definition: (p, q) -> if p.2 = k and q.2 = k then X((p.1,k),(q.1,k)) else 0."""
    out = {}
    for i, p in enumerate(idx):
        for j, q in enumerate(idx):
            if p[1] == k and q[1] == k:
                v = M.get((idx.index((p[0], k)), idx.index((q[0], k))), F(0))
                if v != 0:
                    out[(i, j)] = v
    return out


def block_pinch(idx, blk, b, M):
    """P_b X P_b with P_b the diagonal projector on {s : blk(s) = b}."""
    out = {}
    for (i, j), v in M.items():
        if blk(idx[i]) == b and blk(idx[j]) == b and v != 0:
            out[(i, j)] = v
    return out


def mat_add(M, Nm):
    out = dict(M)
    for k, v in Nm.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def observe_forget(idx, n, M):
    S = {}
    for k in range(n):
        S = mat_add(S, luders_by_def(idx, k, M))
    return S


print("-- X3: the kernel's native readout")
x3 = True
for n in (2, 3):
    idx = carrier(2, n)
    eq_pinch = all(mat_eq(luders_by_def(idx, k, unit(idx, p, q)), block_pinch(idx, lambda s: s[1], k, unit(idx, p, q)))
                   for k in range(n) for p in idx for q in idx)
    passive = all(mat_eq(observe_forget(idx, n, unit(idx, p, q)), unit(idx, p, q))
                  for p in idx for q in idx if p[1] == q[1])
    coh = observe_forget(idx, n, unit(idx, (0, 0), (0, 1)))
    killed = coh == {}
    rep = all(mat_eq(luders_by_def(idx, j, luders_by_def(idx, k, unit(idx, p, q))),
                     luders_by_def(idx, k, unit(idx, p, q)) if j == k else {})
              for j in range(n) for k in range(n) for p in idx for q in idx)
    if n == 2:
        CC["CC2"] = mat_eq(coh, unit(idx, (0, 0), (0, 1)))
    x3 = x3 and eq_pinch and passive and killed and rep
    print(f"X3  ancilla size {n}: localLuders k = blockPinch(snd, k) on all matrix units: {eq_pinch}; observe-and-forget "
          f"fixes every ancilla-classical matrix unit: {passive}; sends E_((0,0),(0,1)) to 0: {killed}; repeatable: {rep}")
RES["X3"] = x3

idx = carrier(2, 2)
LABELS = {
    "Prod.snd (refines)": (lambda s: s[1], True),
    "id (refines)": (lambda s: s, True),
    "three blocks (refines)": (lambda s: s if s[1] == 0 else "b1", True),
    "one block (straddles)": (lambda s: 0, False),
    "system value (straddles)": (lambda s: s[0], False),
}
x3b = True
for name, (blk, refines) in LABELS.items():
    alg_units = [(p, q) for p in idx for q in idx if blk(p) == blk(q)]
    fixed = all(mat_eq(observe_forget(idx, 2, unit(idx, p, q)), unit(idx, p, q)) for p, q in alg_units)
    pure00 = unit(idx, (0, 0), (0, 0))
    pure01 = unit(idx, (0, 1), (0, 1))

    def prob0(M):
        L = luders_by_def(idx, 0, M)
        return sum(v for (i, j), v in L.items() if i == j)

    law = (prob0(pure00), prob0(pure01))
    if refines:
        ok = fixed and law == (1, 0)
    else:
        ok = not fixed
    if name.startswith("system value"):
        CC["CC4"] = fixed
    x3b = x3b and ok
    print(f"X3b {name}: observe-and-forget fixes every matrix unit of the algebra: {fixed}; outcome-0 probability on "
          f"the pure states (0,0), (0,1): {law[0]}, {law[1]}  -> as expected: {ok}")
RES["X3b"] = x3b
print()


# ---------------------------------------------------------------------------------------------------------------
# X4, X5 -- the disguise test on the knowledge-balance toy
# ---------------------------------------------------------------------------------------------------------------

OMEGA = [(0, 0), (0, 1), (1, 0), (1, 1)]   # (z, x)
N4 = 4
S4 = list(permutations(range(N4)))
READ = {"Z": lambda c: c[0], "X": lambda c: c[1], "Y": lambda c: c[0] ^ c[1]}


def unif(cells):
    cells = list(cells)
    return tuple(F(1, len(cells)) if i in cells else F(0) for i in range(N4))


UNIFORM = unif(range(N4))
PM = [unif([i]) for i in range(N4)]


def cells_of(name):
    return [tuple(i for i in range(N4) if READ[name](OMEGA[i]) == v) for v in (0, 1)]


def set_partitions(items):
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in set_partitions(rest):
        for k in range(len(p)):
            yield p[:k] + [[first] + p[k]] + p[k + 1:]
        yield [[first]] + p


ALLPART = [[tuple(sorted(c)) for c in p] for p in set_partitions(range(N4))]
NONTRIV = [p for p in ALLPART if len(p) > 1]


def passive_inst(P):
    def br(c):
        return lambda w: tuple(w[i] if i in c else F(0) for i in range(N4))
    return [br(c) for c in P]


def kbd_inst(P):
    def br(c):
        def f(w):
            m = sum(w[i] for i in c)
            return tuple(m / len(c) if i in c else F(0) for i in range(N4))
        return f
    return [br(c) for c in P]


def normalize(v):
    s = sum(v)
    return tuple(a / s for a in v)


def reach(perms, insts, seed=UNIFORM, cap=5000):
    seen = {seed}
    frontier = [seed]
    while frontier:
        new = []
        for w in frontier:
            outs = [push(s, w) for s in perms]
            for inst in insts:
                for br in inst:
                    v = br(w)
                    if sum(v) > 0:
                        outs.append(normalize(v))
            for u in outs:
                if u not in seen:
                    seen.add(u)
                    new.append(u)
                    if len(seen) > cap:
                        raise RuntimeError("reach cap exceeded")
        frontier = new
    return seen


def rank(rows):
    M = [list(r) for r in rows]
    if not M:
        return 0
    rk = 0
    for col in range(len(M[0])):
        piv = None
        for r in range(rk, len(M)):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col] / M[rk][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rk])]
        rk += 1
    return rk


def aff_indep(R):
    if len(R) == 1:
        return True
    return rank([tuple(a - b for a, b in zip(r, R[0])) for r in R[1:]]) == len(R) - 1


def solve_bary(p, R):
    k = len(R)
    M = [[R[j][i] for j in range(k)] + [p[i]] for i in range(N4)] + [[F(1)] * k + [F(1)]]
    rk = 0
    pivcols = []
    for col in range(k):
        piv = None
        for r in range(rk, len(M)):
            if M[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][col]
        M[rk] = [a / pv for a in M[rk]]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[rk])]
        pivcols.append(col)
        rk += 1
    for r in range(rk, len(M)):
        if M[r][k] != 0:
            return None
    if rk < k:
        return None
    lam = [F(0)] * k
    for r, col in enumerate(pivcols):
        lam[col] = M[r][k]
    return lam


def in_hull(p, T):
    T = list(T)
    for k in range(1, 5):
        for R in combinations(T, k):
            if not aff_indep(list(R)):
                continue
            lam = solve_bary(p, list(R))
            if lam is not None and all(l >= 0 for l in lam):
                return True
    return False


def extreme_points(S):
    S = list(S)
    return [p for p in S if not in_hull(p, [q for q in S if q != p])]


def mass(w, c):
    return sum(w[i] for i in c)


def fmt(w):
    return "(" + ", ".join(str(a) for a in w) + ")"


ZC0, ZC1 = cells_of("Z")
ZP, ZM = unif(ZC0), unif(ZC1)
XP = unif(cells_of("X")[0])
KBD_ALL = [kbd_inst(cells_of(nm)) for nm in "ZXY"]


def kbd_forget_z(w):
    out = [F(0)] * N4
    for br in kbd_inst(cells_of("Z")):
        v = br(w)
        for i in range(N4):
            out[i] += v[i]
    return tuple(out)


def frame_dephase(w):
    r = mass(w, ZC0)
    return tuple(r * a + (1 - r) * b for a, b in zip(ZP, ZM))


def fresh_record_z(w):
    """Copy z into a blank bit r (joint over (z, x, r)), then discard r: the marginal on (z, x)."""
    joint = {}
    for i, (z, x) in enumerate(OMEGA):
        joint[(z, x, z)] = joint.get((z, x, z), F(0)) + w[i]
    out = [F(0)] * N4
    for (z, x, r), p in joint.items():
        out[OMEGA.index((z, x))] += p
    return tuple(out)


def sandwich(seed, sig, deph):
    inv = tuple(sig.index(i) for i in range(N4))
    mid = push(sig, seed)
    coh = mass(push(inv, mid), ZC0)
    dep = mass(push(inv, deph(mid)), ZC0)
    return coh, dep


print("-- X4: disguise test on the knowledge-balance toy")
Ra = reach(S4, KBD_ALL)
Ea = extreme_points(Ra)
pairs = sorted(unif(c) for c in combinations(range(N4), 2))
a_oct = sorted(Ea) == pairs
mixers = [s for s in S4 if push(s, ZP) == XP]
a_bal = XP in Ea and mass(XP, ZC0) == F(1, 2) and len(mixers) > 0
a_face = [w for w in Ra if mass(w, ZC0) == 1] == [ZP]
a_deph = all(kbd_forget_z(w) == frame_dephase(w) for w in Ra)
a_wit = sandwich(ZP, mixers[0], kbd_forget_z) == (1, F(1, 2)) if mixers else False
excl = []
for P in NONTRIV:
    found = False
    for w in Ra:
        for c in P:
            m = mass(w, c)
            if 0 < m < 1:
                post = normalize(tuple(w[i] if i in c else F(0) for i in range(N4)))
                if not in_hull(post, Ea):
                    found = True
                    break
        if found:
            break
    excl.append(found)
a_excl = all(excl)
postxp = [normalize(tuple(XP[i] if i in c else F(0) for i in range(N4))) for c in (ZC0, ZC1)]
CC["CC3"] = all(in_hull(q, Ea) for q in postxp)
CC["CC5"] = any(w in Ra for w in PM)
RES["X4a"] = a_oct and a_bal and a_face and a_deph and a_wit and a_excl
print(f"X4a access (S4, KB-D Z, X, Y): {len(Ra)} reachable states; extreme points = the 6 pair states: {a_oct}; "
      f"permutations mapping z+ to x+ (extreme, z-balanced): {len(mixers)}; reachable states with z-mass 1 = {{z+}}: "
      f"{a_face}; KB-D observe-and-forget = frame dephasing on every reachable state: {a_deph}; sandwich "
      f"{sandwich(ZP, mixers[0], kbd_forget_z) if mixers else None}; a P-conditioned posterior outside the body "
      f"for each of the 14 partitions: {sum(excl)}/14  -> {RES['X4a']}")

b_all = []
SWAP_ZX = tuple(OMEGA.index((c[1], c[0])) for c in OMEGA)
for P in NONTRIV:
    Rb = reach(S4, KBD_ALL + [passive_inst(P)])
    Eb = extreme_points(Rb)
    pm_ok = all(w in Rb for w in PM)
    ext_ok = sorted(Eb) == sorted(PM)
    nobal = not any(0 < mass(w, c) < 1 for w in Eb for Q in NONTRIV for c in Q)
    seed = PM[OMEGA.index((0, 1))]
    fake = sandwich(seed, SWAP_ZX, kbd_forget_z) == (1, F(1, 2))
    erase = kbd_forget_z(seed) != seed and mass(seed, ZC0) == 1
    v0 = all(sandwich(PM[i], s, fresh_record_z)[0] == sandwich(PM[i], s, fresh_record_z)[1]
             for s in S4 for i in range(N4))
    b_all.append(pm_ok and ext_ok and nobal and fake and erase and v0)
RES["X4b"] = all(b_all)
print(f"X4b access (S4, KB-D Z, X, Y, passive P), for each of the 14 nontrivial partitions P: every point mass "
      f"reachable, extreme points = the 4 point masses, none balanced, sandwich from (0,1) with the z-x exchange and "
      f"KB-D's observe-and-forget = (1, 1/2) while that map moves the pure state (0,1) of the face z = 0, visibility 0 "
      f"with the fresh-record dephasing for all 24 x 4 sandwiches: {sum(b_all)}/14  -> {RES['X4b']}")

Rc = reach(S4, [passive_inst([ZC0, ZC1])])
Ec = extreme_points(Rc)
c_ok = all(w in Rc for w in PM) and sorted(Ec) == sorted(PM) and \
    not any(0 < mass(w, c) < 1 for w in Ec for Q in NONTRIV for c in Q)
RES["X4c"] = c_ok
print(f"X4c access (S4, passive Z): {len(Rc)} reachable states; point masses reachable, extreme points the 4 point "
      f"masses, none balanced: {c_ok}")

JOINT = list(product(OMEGA, OMEGA))
chsh_vals = set()
for a0, a1, b0, b1 in product("ZXY", repeat=4):
    for cA, cB in JOINT:
        def E(sa, sb):
            ra = 1 if READ[sa](cA) == 0 else -1
            rb = 1 if READ[sb](cB) == 0 else -1
            return ra * rb
        chsh_vals.add(E(a0, b0) + E(a0, b1) + E(a1, b0) - E(a1, b1))
RES["X5"] = max(chsh_vals) == 2 and min(chsh_vals) == -2
print(f"X5  product-register composites, all 81 setting choices, 16 joint configurations: CHSH values "
      f"{sorted(chsh_vals)}  -> {RES['X5']}")
print()


# ---------------------------------------------------------------------------------------------------------------
# X6 -- the continuous form
# ---------------------------------------------------------------------------------------------------------------

print("-- X6: the continuous form (circle substratum)")


def half_contains(u_idx, arc_idx, M):
    """grid with 2M = 2^(m+1) cells of length pi/2^m; the half-circle centred at grid point u covers the cells
    u - M/2 .. u + M/2 - 1 (mod 2M); returns 1 if the elementary arc is inside, else 0."""
    L = 2 * M
    lo = (u_idx - M // 2) % L
    return F(1) if (arc_idx - lo) % L < M else F(0)


x6_ranks = []
x6_reach = True
for m in range(1, 6):
    M = 2 ** m           # cells per half-circle
    L = 2 * M            # cells on the circle
    halves = [frozenset(a for a in range(L) if half_contains(u, a, M) == 1) for u in range(L)]
    arcs_reached = {h1 & h2 for h1 in halves for h2 in halves if h1 & h2}
    singles = {frozenset([a]) for a in range(L)}
    x6_reach = x6_reach and singles <= arcs_reached
    table = [[half_contains(u, a, M) for u in range(L)] for a in range(L)]
    x6_ranks.append(rank(table))
pyth = [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)), (F(4, 5), F(3, 5)), (F(5, 13), F(12, 13)),
        (F(12, 13), F(5, 13)), (F(8, 17), F(15, 17)), (F(-3, 5), F(4, 5)), (F(-4, 5), F(-3, 5)),
        (F(7, 25), F(-24, 25)), (F(-1), F(0)), (F(0), F(-1))]
cos_table = [[(1 + psi[0] * u[0] + psi[1] * u[1]) / 2 for u in pyth] for psi in pyth]
cos_rank = rank(cos_table)
RES["X6"] = x6_reach and x6_ranks == [2 ** m + 1 for m in range(1, 6)] and cos_rank == 3
print(f"X6  conditioning on grid half-circles reaches every elementary arc (m = 1..5): {x6_reach}; table ranks "
      f"{x6_ranks} (2^m + 1: {[2 ** m + 1 for m in range(1, 6)]}); cosine law alone, 12 Pythagorean directions: rank "
      f"{cos_rank}  -> {RES['X6']}")
print()

print("-- countercontrols (must be False)")
for k in sorted(CC):
    print(f"{k}  {'CC-OK (False as required)' if not CC[k] else 'CC-FAILED (True)'}")
print()
for k in sorted(RES):
    print(f"  {k}: {RES[k]}")

NOGO_GENERAL = RES["X1"] and RES["X1b"] and RES["X1c"]
CONTROL = RES["X2"]
KERNEL_FORM = RES["X3"] and RES["X3b"]
DISGUISE_LOCATED = RES["X4a"] and RES["X4b"] and RES["X4c"] and RES["X5"]
CONTINUOUS = RES["X6"]
if any(CC.values()):
    print("VERDICT VOID: a countercontrol is True: " + ", ".join(k for k in sorted(CC) if CC[k]))
elif NOGO_GENERAL and CONTROL and KERNEL_FORM and DISGUISE_LOCATED and CONTINUOUS:
    print("VERDICT EXCLUSIVITY-REFUTED-AND-LOCATED: on every finite carrier with every permutation, one passive")
    print("  readout of any nontrivial cell reaches every point mass (the module's construction replicated); the")
    print("  kernel's native readout is the block pinching of the ancilla values, passive exactly on the algebras")
    print("  refining the ancilla value; on the knowledge-balance toy the exclusivity holds exactly where a pure")
    print("  frame state is carried to a pure balanced state, the owner's numbers alone being reproducible by memory")
    print("  erasure without it, and the premise says nothing about the pair (CHSH in [-2, 2]); in continuous form one")
    print("  conditioning readout restores growing rank.")
else:
    failing = [k for k in sorted(RES) if not RES[k]]
    print("VERDICT MIXED: failing items " + ", ".join(failing))
