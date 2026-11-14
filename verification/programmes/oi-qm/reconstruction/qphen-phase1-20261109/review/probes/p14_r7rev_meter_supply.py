"""p14 (reviewer, r7): independent exact checks of SHARED Q4-P20 and Q4-D8 on generic objects.

Generic objects only: affine maps of F_q^4 (q = 2, 3, and a random sample at q = 5, 7) with coordinates
(c, x, m, m'), symplectic pairs (c, x) and (m, m'), omega(u, v) = u_c v_x - u_x v_c + u_m v_m' - u_m' v_m.
No OI mechanism is computed.  Standard library only; imports no earlier probe.

Construction differs from p9-p13: Sp(4, F_q) is generated as the closure of a set of symplectic
transvections T_v(u) = u + omega(u, v) v (breadth-first), its order compared with q^4 (q^2-1)(q^4-1),
and every element checked against M^T J M = J.

Definitions (Q4-P20's hypotheses):
- support of the input law: {c in {0,1}} x X x R, a PRODUCT (meter independent of the carrier), with
  X a set of x-values (all of F_q, or any two values) and R the meter's ready set;
- SA-1(c) meter: R = the line {l = k} for a nonzero linear functional l of (m, m');
- sharp meter: R = one point;
- records readably: some nonzero linear functional f of the output (m, m') is constant on each branch
  of the support and differs between the branches;
- K_null = id (on x): x' = x on every support state with c = 0.
"""
import itertools
import random
import sys

NP = 0
NF = 0


def check(name, cond, detail=""):
    global NP, NF
    NP += bool(cond)
    NF += (not cond)
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + str(detail) if detail != "" else ""))


C, X, M_, MP = 0, 1, 2, 3


def omega(u, v, q):
    return (u[0] * v[1] - u[1] * v[0] + u[2] * v[3] - u[3] * v[2]) % q


def col(M, j):
    return tuple(M[i][j] for i in range(4))


def is_sympl_def(M, q):
    # definition on basis pairs: omega(M e_i, M e_j) = omega(e_i, e_j)
    E = [tuple(1 if k == i else 0 for k in range(4)) for i in range(4)]
    return all(omega(col(M, i), col(M, j), q) == omega(E[i], E[j], q) for i in range(4) for j in range(4))


def mm(A, B, q):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) % q for j in range(4)) for i in range(4))


def transvection(v, q):
    # T u = u + omega(u, v) v ; column j = e_j + omega(e_j, v) v
    cols = []
    for j in range(4):
        ej = tuple(1 if k == j else 0 for k in range(4))
        w = omega(ej, v, q)
        cols.append(tuple((ej[i] + w * v[i]) % q for i in range(4)))
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))


def sp_closure(q):
    gens_v = []
    for i in range(4):
        gens_v.append(tuple(1 if k == i else 0 for k in range(4)))
    for i in range(4):
        for j in range(i + 1, 4):
            for s in range(1, q):
                gens_v.append(tuple(1 if k == i else (s if k == j else 0) for k in range(4)))
    gens = [transvection(v, q) for v in gens_v]
    I = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
    seen = {I}
    frontier = [I]
    while frontier:
        nxt = []
        for A in frontier:
            for G in gens:
                B = mm(G, A, q)
                if B not in seen:
                    seen.add(B)
                    nxt.append(B)
        frontier = nxt
    return gens, sorted(seen)


def lin(M, y, q):
    return tuple(sum(M[i][j] * y[j] for j in range(4)) % q for i in range(4))


def nonzero_f(q):
    return [f for f in itertools.product(range(q), repeat=2) if f != (0, 0)]


def lines(q):
    out = []
    reps = []
    seen = set()
    for l in nonzero_f(q):
        if l in seen:
            continue
        reps.append(l)
        for s in range(1, q):
            seen.add(((s * l[0]) % q, (s * l[1]) % q))
    for l in reps:
        for k in range(q):
            out.append((l, k, [p for p in itertools.product(range(q), repeat=2)
                               if (l[0] * p[0] + l[1] * p[1]) % q == k]))
    return out


def support(Xs, R):
    return [(c, x, m, mp) for c in (0, 1) for x in Xs for (m, mp) in R]


def readable_lin(M, S, q):
    # b-independent: f(My + b) = f(My) + f(b)
    outs = [(y[0], lin(M, y, q)) for y in S]
    for f in nonzero_f(q):
        v = {0: set(), 1: set()}
        for c, o in outs:
            v[c].add((f[0] * o[2] + f[1] * o[3]) % q)
        if len(v[0]) == 1 and len(v[1]) == 1 and v[0] != v[1]:
            return True
    return False


def g_values(M, S, q):
    # values of x'-x - b_x = (x o M - x)(y) on the c = 0 support
    return {(lin(M, y, q)[1] - y[1]) % q for y in S if y[0] == 0}


def explicit(M, b, S, q):
    """explicit affine map: (readable, K_null = id on x, x'-x non-constant on the silent support)"""
    T = lambda y: tuple((lin(M, y, q)[i] + b[i]) % q for i in range(4))
    outs = [(y, T(y)) for y in S]
    rd = False
    for f in nonzero_f(q):
        v = {0: set(), 1: set()}
        for y, o in outs:
            v[y[0]].add((f[0] * o[2] + f[1] * o[3]) % q)
        if len(v[0]) == 1 and len(v[1]) == 1 and v[0] != v[1]:
            rd = True
            break
    kid = all(o[1] == y[1] for y, o in outs if y[0] == 0)
    noncst = len({(o[1] - y[1]) % q for y, o in outs if y[0] == 0}) > 1
    return rd, kid, noncst


# ------------------------------------------------------------------------------------------------
print("== 1. Sp(4, F_q) by transvection closure")
SP = {}
for q in (2, 3):
    gens, G = sp_closure(q)
    order = q ** 4 * (q * q - 1) * (q ** 4 - 1)
    check("1a q=%d generators are symplectic (definition, basis pairs)" % q, all(is_sympl_def(T, q) for T in gens))
    check("1b q=%d closure order = q^4(q^2-1)(q^4-1) = %d" % (q, order), len(G) == order, len(G))
    check("1c q=%d every element satisfies the definition" % q, all(is_sympl_def(M, q) for M in G))
    SP[q] = G
# F_2 cross-check: brute force over all 2^16 matrices
bf = [tuple(tuple(e[4 * i:4 * i + 4]) for i in range(4)) for e in itertools.product((0, 1), repeat=16)]
bf = sorted(M for M in bf if is_sympl_def(M, 2))
check("1d q=2 closure equals the brute-force filter of all 65,536 matrices", bf == SP[2], len(bf))
# bracket preservation used in the proof: {phi o M, psi o M} = {phi, psi}, for the bracket dual to omega.
# Over the dual, the bracket of row vectors phi, psi is phi Jinv psi^T with Jinv = -J for this J.
Jm = ((0, 1, 0, 0), (-1, 0, 0, 0), (0, 0, 0, 1), (0, 0, -1, 0))


def br(phi, psi, q):
    Ji = [[-a for a in r] for r in Jm]
    return sum(phi[i] * Ji[i][j] * psi[j] for i in range(4) for j in range(4)) % q


def rowM(phi, M, q):
    return tuple(sum(phi[i] * M[i][j] for i in range(4)) % q for j in range(4))


ok = True
for q in (2, 3):
    basisf = [tuple(1 if k == i else 0 for k in range(4)) for i in range(4)]
    for M in SP[q]:
        for a in basisf:
            for b in basisf:
                if br(rowM(a, M, q), rowM(b, M, q), q) != br(a, b, q):
                    ok = False
check("1e bracket of linear functionals is preserved by every M (q = 2, 3)", ok)
check("1f {x, c} != 0 and {x, f} = 0 for f in the meter pair (q = 2, 3)",
      all(br((0, 1, 0, 0), (1, 0, 0, 0), q) != 0 and br((0, 1, 0, 0), (0, 0, a, b), q) == 0
          for q in (2, 3) for a in range(q) for b in range(q)))

LP = {q: [M for M in SP[q] if M[0] == (1, 0, 0, 0)] for q in (2, 3)}
check("1g location-preserving linear parts: 48 at q=2 (= 720/15), 648 at q=3 (= 51,840/80)",
      (len(LP[2]), len(LP[3])) == (48, 648),
      (len(LP[2]), len(LP[3])))

# ------------------------------------------------------------------------------------------------
print("== 2. Q4-P20 by explicit affine maps (every translation b)")
for q, maps_label, Ms in ((2, "all affine-symplectic", SP[2]), (2, "location-preserving", LP[2]),
                          (3, "location-preserving", LP[3])):
    lp = maps_label == "location-preserving"
    Bs = [b for b in itertools.product(range(q), repeat=4) if (not lp or b[0] == 0)]
    for (l, k, R) in lines(q):
        S = support(range(q), R)
        nrd = nkid = nweak = 0
        for M in Ms:
            for b in Bs:
                rd, kid, nc = explicit(M, b, S, q)
                if rd:
                    nrd += 1
                    nkid += kid
                    nweak += (not nc)
        print("   q=%d %-22s l=%s k=%d: %d maps, readable %d, K_null=id %d, x'-x constant on silent support %d"
              % (q, maps_label, l, k, len(Ms) * len(Bs), nrd, nkid, nweak))
        check("2 q=%d %s l=%s k=%d: readable recorders exist; none has K_null = id; none is a known displacement"
              % (q, maps_label, l, k), nrd > 0 and nkid == 0 and nweak == 0, nrd)
# stated counts
def count_readable(q, Ms, Bs, R):
    S = support(range(q), R)
    return sum(1 for M in Ms for b in Bs if explicit(M, b, S, q)[0])


check("2c counts: 4,608 of 11,520 (q=2 all), 192 of 384 (q=2 LP), 11,664 of 17,496 (q=3 LP), per SA-1(c) law",
      count_readable(2, SP[2], list(itertools.product(range(2), repeat=4)), [(0, 0), (1, 1)]) == 4608
      and count_readable(2, LP[2], [b for b in itertools.product(range(2), repeat=4) if b[0] == 0],
                         [(0, 0), (1, 1)]) == 192
      and count_readable(3, LP[3], [b for b in itertools.product(range(3), repeat=4) if b[0] == 0],
                         [(1, 2), (2, 1), (0, 0)]) == 11664)

# carrier on only two of q values (hypothesis 'at least two values'), q = 3, location-preserving
ok = True
for Xs in ((0, 1), (0, 2), (1, 2)):
    for (l, k, R) in lines(3):
        S = support(Xs, R)
        for M in LP[3]:
            for b in [b for b in itertools.product(range(3), repeat=4) if b[0] == 0]:
                rd, kid, nc = explicit(M, b, S, 3)
                if rd and kid:
                    ok = False
check("2d q=3 LP, carrier x on two of three values: no readable recorder has K_null = id", ok)

# ------------------------------------------------------------------------------------------------
print("== 3. b-independence reduction, then every affine-symplectic map of F_3^4 (51,840 x 81)")
# reduction: readability does not depend on b; K_null = id is possible for some b iff g is constant
ok = True
for q, Ms in ((2, SP[2]), (3, LP[3][:200])):
    for (l, k, R) in lines(q)[:4]:
        S = support(range(q), R)
        for M in Ms:
            r0 = readable_lin(M, S, q)
            gc = len(g_values(M, S, q)) == 1
            for b in itertools.product(range(q), repeat=4):
                rd, kid, nc = explicit(M, b, S, q)
                if rd != r0 or (kid and not gc) or (nc == gc):
                    ok = False
check("3a reduction agrees with explicit maps (q=2 all; q=3 first 200 LP parts; four laws each)", ok)
bad = 0
nread = {}
for (l, k, R) in lines(3):
    S = support(range(3), R)
    n = 0
    for M in SP[3]:
        if readable_lin(M, S, 3):
            n += 1
            if len(g_values(M, S, 3)) == 1:
                bad += 1
    nread[(l, k)] = n
check("3b q=3, all 51,840 linear parts x 81 translations, 12 SA-1(c) laws: no readable map with K_null = id",
      bad == 0, "readable linear parts per law: %s" % sorted(set(nread.values())))

# ------------------------------------------------------------------------------------------------
print("== 4. random sample, q = 5 and 7 (not exhaustive)")
rng = random.Random(14)
for q in (5, 7):
    gens = [transvection(v, q) for v in itertools.product(range(q), repeat=4) if any(v)]
    I = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
    nread = nbad = 0
    LS = lines(q)
    for t in range(1500):
        M = I
        for _ in range(12):
            M = mm(rng.choice(gens), M, q)
        if t % 2 == 0:
            # force location preservation half the time by conjugating nothing: just filter below
            pass
        assert is_sympl_def(M, q)
        for (l, k, R) in rng.sample(LS, 4):
            S = support(range(q), R)
            if readable_lin(M, S, q):
                nread += 1
                if len(g_values(M, S, q)) == 1:
                    nbad += 1
    check("4 q=%d: 1,500 random symplectic M x 4 random SA-1(c) lines: readable cases found, none admits K_null = id"
          % q, nread > 0 and nbad == 0, nread)

# ------------------------------------------------------------------------------------------------
print("== 5. countercontrols")
# 5a sharp meters: some readable LP recorder has K_null = id; counts; every readable LP map is a known displacement
for q in (2, 3):
    Bs = [b for b in itertools.product(range(q), repeat=4) if b[0] == 0]
    for p in itertools.product(range(q), repeat=2):
        S = support(range(q), [p])
        res = [explicit(M, b, S, q) for M in LP[q] for b in Bs]
        nrd = sum(1 for r in res if r[0])
        nkid = sum(1 for r in res if r[0] and r[1])
        nnc = sum(1 for r in res if r[0] and r[2])
        exp = {2: (288, 144), 3: (15552, 5184)}[q]
        check("5a q=%d sharp %s: readable %d, K_null = id %d (expect %s); all known displacements"
              % (q, p, nrd, nkid, exp), (nrd, nkid) == exp and nnc == 0)
# 5b the 288 readable-under-sharp LP maps at q=2 are exactly the 288 whose meter write depends on c
Bs2 = [b for b in itertools.product(range(2), repeat=4) if b[0] == 0]
A = {(M, b) for M in LP[2] for b in Bs2 if explicit(M, b, support((0, 1), [(0, 0)]), 2)[0]}
D = {(M, b) for M in LP[2] for b in Bs2 if (M[2][0], M[3][0]) != (0, 0)}
check("5b q=2: readable under sharp (0,0) = meter write depends on c (288 maps)", A == D and len(D) == 288, len(D))
# 5c both meter slots unknown: no LP map records readably (q = 2, 3)
check("5c both slots unknown: no location-preserving linear part records readably (q = 2, 3)",
      all(not readable_lin(M, support(range(q), list(itertools.product(range(q), repeat=2))), q)
          for q in (2, 3) for M in LP[q]))
# 5d copy coupling (not symplectic) under an SA-1(c) meter: readable and K_null = id
Mc = ((1, 0, 0, 0), (0, 1, 0, 0), (1, 0, 1, 0), (0, 0, 0, 1))
r = explicit(Mc, (0, 0, 0, 0), support((0, 1), [(0, 0), (0, 1)]), 2)
check("5d copy coupling: not symplectic; under SA-1(c) (m known) readable with K_null = id",
      (not is_sympl_def(Mc, 2)) and r[0] and r[1])
# 5e the independence (product-support) hypothesis is load-bearing.  Meter supplied with m known (= 0) and
# m' = s x + t c (s != 0): the meter's marginal on each branch is uniform on the line {m = 0}, but it is
# correlated with the carrier.  Search every symplectic linear part; an affine map with that linear part
# fixes (c, x) on the silent support for a suitable translation iff (c o M - c) and (x o M - x) are constant
# there (for a location-preserving part, b_c = 0 and c o M - c = 0 already).
res5e = {}
for q in (2, 3):
    for s_ in range(1, q):
        for t_ in range(q):
            S = [(c, x, 0, (s_ * x + t_ * c) % q) for c in (0, 1) for x in range(q)]
            n_all = n_lp = 0
            for M in SP[q]:
                if not readable_lin(M, S, q):
                    continue
                outs = [(y, lin(M, y, q)) for y in S if y[0] == 0]
                if len({(o[1] - y[1]) % q for y, o in outs}) == 1 and len({(o[0] - y[0]) % q for y, o in outs}) == 1:
                    n_all += 1
                    n_lp += (M[0] == (1, 0, 0, 0))
            res5e[(q, s_, t_)] = (n_all, n_lp)
print("   correlated meter m' = s x + t c: (q, s, t) -> (readable linear parts admitting K_null = id, of which LP)")
print("   " + str(res5e))
check("5e countercontrol: with the meter correlated with the carrier (not independent), readable symplectic "
      "recorders with K_null = id on (c, x) exist at q = 2 and 3", all(v[0] > 0 for v in res5e.values()))
check("5f in the tested correlations none of them is location-preserving", all(v[1] == 0 for v in res5e.values()))

# ------------------------------------------------------------------------------------------------
print("== 6. Q4-D8 membership, by hand-form matrix")
Mr = ((1, 0, 0, 0), (0, 1, 0, 1), (1, 0, 1, 0), (0, 0, 0, 1))  # (c, x, m, m') -> (c, x + m', m + c, m')
cols = {n: col(Mr, j) for j, n in enumerate(("c", "x", "m", "m'"))}
check("6a M e_c = e_c + e_m, M e_x = e_x, M e_m = e_m, M e_m' = e_x + e_m'",
      cols == {"c": (1, 0, 1, 0), "x": (0, 1, 0, 0), "m": (0, 0, 1, 0), "m'": (0, 1, 0, 1)})
pairs = {(a, b): omega(cols[a], cols[b], 2) for a, b in itertools.combinations(("c", "x", "m", "m'"), 2)}
check("6b over F_2: omega(Mc,Mx) = omega(Mm,Mm') = 1, the other four pairings 0",
      pairs == {("c", "x"): 1, ("c", "m"): 0, ("c", "m'"): 0, ("x", "m"): 0, ("x", "m'"): 0, ("m", "m'"): 1})
r = explicit(Mr, (0, 0, 0, 0), support((0, 1), [(0, 0)]), 2)
check("6c sharp (0,0): location-preserving, readable (output m = c), K_null = id", Mr[0] == (1, 0, 0, 0) and r[0] and r[1])
r = explicit(Mr, (0, 0, 0, 0), support((0, 1), [(0, 0), (0, 1)]), 2)
check("6d SA-1(c) (m known 0): readable and K_null != id", r[0] and not r[1])

# ------------------------------------------------------------------------------------------------
print("== 7. the sharp-meter sentence of R4.9, A4.4 and T2 ('a known displacement and K_null = id')")
for p in itertools.product((0, 1), repeat=2):
    S = support((0, 1), [p])
    rd, kid, nc = explicit(Mr, (0, 0, 0, 0), S, 2)
    disp = {(apply_x - y[1]) % 2 for y in S if y[0] == 0
            for apply_x in [(lin(Mr, y, 2)[1])]}
    print("   reciprocal coupling, sharp meter %s: readable %s, K_null = id %s, silent displacement %s"
          % (p, rd, kid, sorted(disp)))
r01 = explicit(Mr, (0, 0, 0, 0), support((0, 1), [(0, 1)]), 2)
check("7a sharp meter (0, 1): the reciprocal coupling records readably, its silent kick is the known "
      "displacement x -> x + 1, so K_null != id", r01[0] and (not r01[1]) and (not r01[2]))
# the known functional m' (m unknown) is also SA-1(c): the reciprocal coupling then does not record readably
r = explicit(Mr, (0, 0, 0, 0), support((0, 1), [(0, 0), (1, 0)]), 2)
check("7b SA-1(c) with m' known and m unknown: the reciprocal coupling does not record readably", not r[0])

print("== %d of %d checks pass" % (NP, NP + NF))
sys.exit(0 if NF == 0 else 1)
