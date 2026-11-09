"""rv_p1 -- independent reviewer check for ASSESS-1049 claim 1 (WIP / UNVERIFIED, model-written).

Exact generic check of an implication on functions over Z/q. Imports nothing from probes/p1-p3.
No OI mechanism, observable or proposed rule is computed.

Checks
  A. The writer's d=3 (q=5,7), d=3 (q=2) and d=2 (q=7) functions, re-coded independently
     (own slot order, own point group built from generators, own affinity test by first
     differences along each coordinate):
       - covariance f(lam v + c) = lam f(v) + 2c for every unit lam, every c (exhaustive);
       - point-group invariance (O_h built by closure from two 90-degree rotations and the
         inversion; D4 from a 90-degree rotation and a reflection);
       - non-affinity (some coordinate first difference depends on its base point).
  B. Weak form: the kappa-general covariance f(lam v + c) = lam f(v) + kappa c with the linear
     part at alpha = 1 (kappa = 6), i.e. not tied to kappa = 2.  Non-affine and covariant.
  C. Global level, on a periodic 4x4x4 lattice at q = 5 (seeded random states, exact integers):
     translation commutation, exact uniform symmetry of the phase-space map, centre-freeness,
     explicit inverse.
  D. Control on the reading: site-dependent shifts as exact symmetries exclude the linear wave
     rule itself (so that reading cannot be the corpus's principle).
  E. d = 1 scope: solution space of covariance (with / without reflection), all functions of the
     two neighbour values, for q in {3, 5, 7, 9, 15}, by exact constraint propagation.
     Prediction from the paper proof: odd prime q -> exactly q solutions, all linear, and exactly
     one (f = a + b) with reflection; composite q -> not proved by the paper argument.
"""
import itertools, random, sys
import numpy as np

OK = True
def check(name, cond):
    global OK
    OK &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name)

def units(q):
    from math import gcd
    return [l for l in range(1, q) if gcd(l, q) == 1]

def inv(z, q):
    z %= q
    return 0 if z == 0 else pow(int(z), -1, q)

# ---------- point groups as permutations of neighbour slots ----------
def closure(gens):
    n = len(gens[0])
    ident = tuple(range(n))
    G = {ident}
    frontier = [ident]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                gh = tuple(g[h[i]] for i in range(n))
                if gh not in G:
                    G.add(gh); new.append(gh)
        frontier = new
    return sorted(G)

def perm_from_map(dirs, M):
    # slot i holds the neighbour in direction dirs[i]; after rotation M the value at direction
    # M d moves to slot of M d.  Return p with p[i] = index of M^{-1} dirs[i].
    idx = {d: i for i, d in enumerate(dirs)}
    Minv = np.linalg.inv(np.array(M)).round().astype(int)
    return tuple(idx[tuple(int(x) for x in Minv @ np.array(d))] for d in dirs)

DIRS3 = [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]   # own order: +x,+y,+z,-x,-y,-z
Rx = [[1,0,0],[0,0,-1],[0,1,0]]
Rz = [[0,-1,0],[1,0,0],[0,0,1]]
Inv3 = [[-1,0,0],[0,-1,0],[0,0,-1]]
OH = closure([perm_from_map(DIRS3, M) for M in (Rx, Rz, Inv3)])
check("O_h closure has 48 elements", len(OH) == 48)

DIRS2 = [(1,0),(0,1),(-1,0),(0,-1)]                              # E, N, W, S
R90 = [[0,-1],[1,0]]
Ref = [[1,0],[0,-1]]
D4 = closure([perm_from_map(DIRS2, M) for M in (R90, Ref)])
check("D4 closure has 8 elements", len(D4) == 8)

# ---------- exhaustive tables ----------
def grid(q, n):
    return np.array(list(itertools.product(range(q), repeat=n)), dtype=np.int64)

def index_of(P, q):
    n = P.shape[1]
    w = q ** np.arange(n - 1, -1, -1, dtype=np.int64)
    return (P % q) @ w

def covariant(T, P, q, kappa):
    for lam in units(q):
        for c in range(q):
            img = index_of(lam * P + c, q)
            if not np.array_equal(T[img] % q, (lam * T + kappa * c) % q):
                return False
    return True

def invariant(T, P, q, G):
    return all(np.array_equal(T[index_of(P[:, list(g)], q)], T) for g in G)

def affine(T, P, q):
    n = P.shape[1]
    for k in range(n):
        e = np.zeros(n, dtype=np.int64); e[k] = 1
        D = (T[index_of(P + e, q)] - T) % q
        if not np.all(D == D[0]):
            return False
    return True

def f3_table(q, alpha, P):
    xp, yp, zp, xm, ym, zm = (P[:, i] for i in range(6))
    px, py, pz = xp + xm, yp + ym, zp + zm
    a1, b1, c1 = 2*px - py - pz, 2*py - pz - px, 2*pz - px - py
    C = (a1 * b1 % q) * c1 % q
    Pq = (a1*a1 + b1*b1 + c1*c1) % q
    Pinv = np.array([inv(z, q) for z in Pq], dtype=np.int64)
    return (alpha * P.sum(axis=1) + C * Pinv) % q

print("== A. writer's functions, recoded ==")
for q in (5, 7):
    P = grid(q, 6)
    a = inv(3, q)
    T = f3_table(q, a, P)
    check(f"d=3 q={q}: covariance kappa=2", covariant(T, P, q, 2))
    check(f"d=3 q={q}: O_h invariance", invariant(T, P, q, OH))
    check(f"d=3 q={q}: non-affine", not affine(T, P, q))
    L = (a * P.sum(axis=1)) % q
    check(f"d=3 q={q}: control linear alpha=1/3 covariant and affine",
          covariant(L, P, q, 2) and affine(L, P, q))
    check(f"d=3 q={q}: countercontrol alpha/3 sum + 1 not covariant", not covariant((L + 1) % q, P, q, 2))
    print("== B. weak kappa-general form, alpha = 1 ==")
    T1 = f3_table(q, 1, P)
    check(f"d=3 q={q}: alpha=1 variant covariant with kappa=6", covariant(T1, P, q, 6))
    check(f"d=3 q={q}: alpha=1 variant not covariant with kappa=2", not covariant(T1, P, q, 2))
    check(f"d=3 q={q}: alpha=1 variant O_h-invariant and non-affine",
          invariant(T1, P, q, OH) and not affine(T1, P, q))

q = 2
P = grid(2, 6)
T = (P.sum(axis=1) + (P.min(axis=1) == P.max(axis=1))) % 2
check("d=3 q=2: s + [all equal] shift-invariant (kappa=2=0)", covariant(T, P, 2, 2))
check("d=3 q=2: O_h invariant", invariant(T, P, 2, OH))
check("d=3 q=2: non-affine", not affine(T, P, 2))

q = 7
P = grid(7, 4)
E, N, W, S = (P[:, i] for i in range(4))
y1, y2, y3 = E - W, N - S, E + W - N - S
z = (y1*y1 - y2*y2) % q
chi = np.where(z == 0, 0, np.where(np.isin(z, [1, 2, 4]), 1, -1))      # squares mod 7: 1,2,4
T2 = (inv(2, q) * P.sum(axis=1) + y3 * chi) % q
check("d=2 q=7: covariance", covariant(T2, P, q, 2))
check("d=2 q=7: D4 invariance", invariant(T2, P, q, D4))
check("d=2 q=7: non-affine", not affine(T2, P, q))

print("== C. global checks on a periodic 4x4x4 lattice, q = 5 ==")
q, Lside = 5, 4
a = inv(3, q)
def F(x):
    nb = [np.roll(x, -s, axis=ax) if True else None for ax in range(3) for s in (1,)]  # +dirs
    xp, yp, zp = (np.roll(x, -1, axis=ax) for ax in range(3))
    xm, ym, zm = (np.roll(x, 1, axis=ax) for ax in range(3))
    px, py, pz = xp + xm, yp + ym, zp + zm
    a1, b1, c1 = 2*px - py - pz, 2*py - pz - px, 2*pz - px - py
    C = (a1 * b1 % q) * c1 % q
    Pq = (a1*a1 + b1*b1 + c1*c1) % q
    Pinv = np.vectorize(lambda z: inv(z, q))(Pq)
    return (a * (px + py + pz) + C * Pinv) % q
def Phi(u, v):
    return v, (F(v) - u) % q
def Phi_inv(v, w):
    return (F(v) - w) % q, v
rng = random.Random(1049)
glob_ok = True
for trial in range(40):
    u = np.array([rng.randrange(q) for _ in range(Lside**3)]).reshape((Lside,)*3)
    v = np.array([rng.randrange(q) for _ in range(Lside**3)]).reshape((Lside,)*3)
    v2, w2 = Phi(u, v)
    # inverse
    glob_ok &= all(np.array_equal(A_, B_) for A_, B_ in zip(Phi_inv(v2, w2), (u, v)))
    # translations
    for ax in range(3):
        tu, tv = np.roll(u, 1, axis=ax), np.roll(v, 1, axis=ax)
        glob_ok &= np.array_equal(Phi(tu, tv)[1], np.roll(w2, 1, axis=ax))
    # uniform symmetry
    lam, c = rng.choice(units(q)), rng.randrange(q)
    glob_ok &= np.array_equal(Phi((lam*u + c) % q, (lam*v + c) % q)[1], (lam*w2 + c) % q)
    # centre-free: change v at one site, F at that site unchanged
    s = tuple(rng.randrange(Lside) for _ in range(3))
    vv = v.copy(); vv[s] = (vv[s] + 1 + rng.randrange(q - 1)) % q
    glob_ok &= F(vv)[s] == F(v)[s]
check("global: inverse, translation commutation, uniform symmetry, centre-free (40 seeded states)", glob_ok)

print("== D. site-dependent shifts as exact symmetries ==")
# Required locally: shifting one neighbour slot k by c must leave f unchanged (target != k).
q = 5; P = grid(q, 6); a = inv(3, q)
L = (a * P.sum(axis=1)) % q
e0 = np.zeros(6, dtype=np.int64); e0[0] = 1
check("site-dependent shift symmetry fails for the linear wave rule itself",
      not np.array_equal(L[index_of(P + e0, q)], L))

print("== E. d = 1 solution spaces (f of the two neighbour values) ==")
def solutions_d1(q, reflect):
    pts = list(itertools.product(range(q), repeat=2))
    gens = [(lam, c) for lam in units(q) for c in range(q)]
    # constraint graph: f(g v) = lam f(v) + 2c ; reflection: f(b,a) = f(a,b)
    seen, orbit_counts, sols_per_orbit = set(), [], []
    for v0 in pts:
        if v0 in seen:
            continue
        good = []
        for val in range(q):
            assign = {v0: val}; stack = [v0]; ok = True
            while stack and ok:
                v = stack.pop(); fv = assign[v]
                imgs = [(((lam*v[0] + c) % q, (lam*v[1] + c) % q), (lam*fv + 2*c) % q) for lam, c in gens]
                if reflect:
                    imgs.append(((v[1], v[0]), fv))
                for w, fw in imgs:
                    if w in assign:
                        if assign[w] != fw: ok = False; break
                    else:
                        assign[w] = fw; stack.append(w)
            if ok:
                good.append(assign)
        orb = set(good[0].keys()) if good else {v0}
        seen |= orb
        sols_per_orbit.append(good)
    return sols_per_orbit

def is_linear(fd, q):
    # f(a,b) = m a + n b for some m, n
    m, n = fd[(1, 0)], fd[(0, 1)]
    return all(fd[(x, y)] == (m*x + n*y) % q for (x, y) in fd)

for q in (3, 5, 7, 9, 15):
    for reflect in (False, True):
        orbs = solutions_d1(q, reflect)
        total = 1
        for g in orbs: total *= len(g)
        all_lin = None
        if total <= 5000 and total > 0:
            all_lin = True
            for combo in itertools.product(*orbs):
                fd = {}
                for d in combo: fd.update(d)
                all_lin &= is_linear(fd, q)
        print(f"   q={q:2d} reflection={reflect!s:5}: #solutions={total}  all linear={all_lin}")
        from sympy import isprime
        if isprime(q):
            check(f"d=1 q={q} reflect={reflect}: solution count {'1' if reflect else 'q'}, all linear",
                  total == (1 if reflect else q) and all_lin)
        elif not reflect:
            check(f"d=1 q={q} reflect=False: composite q admits non-linear solutions",
                  all_lin is False)
        else:
            # Revised expectation (first run): with reflection, lam = -1 makes G odd and the
            # reflection makes it even, so 2G = 0 and G = 0 at every odd q, prime or not.
            check(f"d=1 q={q} reflect=True: unique solution f = a + b at composite odd q",
                  total == 1 and all_lin)

print("ALL PASS" if OK else "SOME FAIL")
sys.exit(0 if OK else 1)
