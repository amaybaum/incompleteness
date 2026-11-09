"""p15 (reviewer, r7a confirming check): exact checks of SHARED Q4-P20's stronger conclusion
("x' - x is not constant on the c = 0 support"), its sharp-meter remark, the N1 sentence and the
N2 independence hypothesis.

Generic objects only: affine maps of F_q^4, q = 2, 3, coordinates (c, x, m, m'), pairs (c, x), (m, m'),
omega(u, v) = u_c v_x - u_x v_c + u_m v_m' - u_m' v_m.  No OI mechanism is computed.
Standard library only; imports no earlier probe.

Construction (differs from p9-p14): Sp(4, F_q) is enumerated as the set of ordered symplectic bases
(a1, b1, a2, b2) -- omega(a1, b1) = omega(a2, b2) = 1, all cross pairings 0 -- taken as the columns
M e_c, M e_x, M e_m, M e_m'.  Readability and K_null are evaluated by brute force on explicit support
states (not by linear algebra on functionals).
"""
import itertools
import random

NP = NF = 0


def check(name, cond, detail=""):
    global NP, NF
    if cond:
        NP += 1
    else:
        NF += 1
    print(("PASS " if cond else "FAIL ") + name + ("  -- " + str(detail) if detail != "" else ""))


def om(u, v, q):
    return (u[0] * v[1] - u[1] * v[0] + u[2] * v[3] - u[3] * v[2]) % q


def vecs(q):
    return list(itertools.product(range(q), repeat=4))


def sp_by_bases(q):
    V = vecs(q)
    Z = (0, 0, 0, 0)
    out = []
    for a1 in V:
        if a1 == Z:
            continue
        for b1 in V:
            if om(a1, b1, q) != 1:
                continue
            W = [v for v in V if om(a1, v, q) == 0 and om(b1, v, q) == 0]
            for a2 in W:
                if a2 == Z:
                    continue
                for b2 in W:
                    if om(a2, b2, q) == 1:
                        cols = (a1, b1, a2, b2)
                        out.append(tuple(tuple(cols[j][i] for j in range(4)) for i in range(4)))
    return out


def app(M, y, b, q):
    return tuple((M[i][0] * y[0] + M[i][1] * y[1] + M[i][2] * y[2] + M[i][3] * y[3] + b[i]) % q for i in range(4))


def is_sympl(M, q):
    E = [tuple(1 if i == j else 0 for i in range(4)) for j in range(4)]
    cols = [app(M, e, (0, 0, 0, 0), q) for e in E]
    return all(om(cols[i], cols[j], q) == om(E[i], E[j], q) for i in range(4) for j in range(4))


def meter_functionals(q):
    # nonzero functionals of (m, m'), one per projective point
    out = []
    for fm, fp in itertools.product(range(q), repeat=2):
        if (fm, fp) == (0, 0):
            continue
        # normalise: first nonzero coordinate equals 1
        lead = fm if fm else fp
        if lead == 1:
            out.append((fm, fp))
    return out


def sa1c_laws(q):
    # (l, k): line {l(m, m') = k}; l up to scale, k in F_q
    return [(l, k) for l in meter_functionals(q) for k in range(q)]


def line_pts(l, k, q):
    return [(m, mp) for m in range(q) for mp in range(q) if (l[0] * m + l[1] * mp) % q == k]


def product_support(Xs, R):
    return {c: [(c, x, m, mp) for x in Xs for (m, mp) in R] for c in (0, 1)}


def readable(M, b, S, q, F):
    for f in F:
        vals = {}
        for c in (0, 1):
            vs = {(f[0] * y[2] + f[1] * y[3]) % q for y in (app(M, s, b, q) for s in S[c])}
            if len(vs) != 1:
                break
            vals[c] = vs.pop()
        else:
            if vals[0] != vals[1]:
                return True
    return False


def disp_set(M, b, states, q):
    return {(app(M, s, b, q)[1] - s[1]) % q for s in states}


def is_lp(M, b):
    return M[0] == (1, 0, 0, 0) and b[0] == 0


# --------------------------------------------------------------------------------------------------
print("== (1) Sp(4, F_q) by symplectic-basis enumeration")
SP = {}
for q, order in ((2, 720), (3, 51840)):
    G = sp_by_bases(q)
    SP[q] = G
    check(f"(1a) q={q}: |Sp| = q^4 (q^2-1)(q^4-1) = {order}", len(G) == order and len(set(G)) == order, len(G))
    check(f"(1b) q={q}: every element preserves omega on the basis", all(is_sympl(M, q) for M in G))
# independent cross-check at q=2: brute-force filter over all 2^16 matrices
cnt = sum(1 for e in itertools.product(range(2), repeat=16)
          if is_sympl(tuple(tuple(e[4 * i:4 * i + 4]) for i in range(4)), 2))
check("(1c) q=2: brute-force filter of 65,536 matrices gives 720", cnt == 720, cnt)

# --------------------------------------------------------------------------------------------------
print("== (2) Q4-P20 stronger conclusion under SA-1(c) (product support): readable => x'-x non-constant on c=0")


def p20_scan(q, Ms, Bs, Xs, laws, tag, lp_only=False):
    F = meter_functionals(q)
    per_law = []
    viol = 0
    weak_viol = 0
    for (l, k) in laws:
        S = product_support(Xs, line_pts(l, k, q))
        n = 0
        for M in Ms:
            for b in Bs:
                if lp_only and not is_lp(M, b):
                    continue
                if not readable(M, b, S, q, F):
                    continue
                n += 1
                D = disp_set(M, b, S[0], q)
                if len(D) == 1:
                    viol += 1
                if D == {0}:
                    weak_viol += 1
        per_law.append(n)
    return per_law, viol, weak_viol


V2 = vecs(2)
pl, v, w = p20_scan(2, SP[2], V2, range(2), sa1c_laws(2), "F2 all")
check("(2a) q=2, all 720x16 affine-symplectic maps, 6 SA-1(c) laws: readable count 4,608 per law",
      set(pl) == {4608}, pl)
check("(2b) q=2, all maps: no readable map has x'-x constant on the c=0 support", v == 0 and w == 0, (v, w))
LP2 = [M for M in SP[2] if M[0] == (1, 0, 0, 0)]
pl, v, w = p20_scan(2, LP2, V2, range(2), sa1c_laws(2), "F2 LP", lp_only=True)
check("(2c) q=2, location-preserving (384 maps): readable count 192 per law, no constant x'-x",
      set(pl) == {192} and v == 0, (pl, v))
LP3 = [M for M in SP[3] if M[0] == (1, 0, 0, 0)]
V3 = vecs(3)
nLP3 = sum(1 for M in LP3 for b in V3 if is_lp(M, b))
check("(2d) q=3: 17,496 location-preserving affine-symplectic maps", nLP3 == 17496, nLP3)
pl, v, w = p20_scan(3, LP3, V3, range(3), sa1c_laws(3), "F3 LP", lp_only=True)
check("(2e) q=3, location-preserving, 12 SA-1(c) laws: readable 11,664 per law, no constant x'-x",
      set(pl) == {11664} and v == 0, (pl, v))
viol_pairs = 0
for Xs in itertools.combinations(range(3), 2):
    pl, v, w = p20_scan(3, LP3, V3, Xs, sa1c_laws(3)[:4], "F3 LP pair", lp_only=True)
    viol_pairs += v
check("(2f) q=3, location-preserving, x restricted to each pair of values: no constant x'-x", viol_pairs == 0,
      viol_pairs)

# full group at q=3: b only shifts f(T y) and x'-x by constants on the whole support, so readability and
# constancy depend on the linear part alone.  Validate that on a random sample with explicit b, then scan
# all 51,840 linear parts with b = 0.
rng = random.Random(15)
F3 = meter_functionals(3)
mism = 0
for _ in range(300):
    M = rng.choice(SP[3])
    l, k = rng.choice(sa1c_laws(3))
    S = product_support(range(3), line_pts(l, k, 3))
    r0 = readable(M, (0, 0, 0, 0), S, 3, F3)
    c0 = len(disp_set(M, (0, 0, 0, 0), S[0], 3)) == 1
    for b in rng.sample(V3, 10):
        if readable(M, b, S, 3, F3) != r0 or (len(disp_set(M, b, S[0], 3)) == 1) != c0:
            mism += 1
check("(2g) q=3: readability and constancy of x'-x independent of b (300 random M x 10 b)", mism == 0, mism)
pl, v, w = p20_scan(3, SP[3], [(0, 0, 0, 0)], range(3), sa1c_laws(3), "F3 all lin")
check("(2h) q=3, all 51,840 linear parts, 12 laws: no readable part has constant x'-x", v == 0, (pl, v))
check("(2i) q=3, readable linear parts per law = 15,552 (matches p14 (3))", set(pl) == {15552}, pl)

# --------------------------------------------------------------------------------------------------
print("== (3) proof steps on every readable map (q=2 all; q=3 LP): f o M in span{c, l} with alpha != 0")


def rowmul(phi, M, q):
    return tuple(sum(phi[i] * M[i][j] for i in range(4)) % q for j in range(4))


def br(phi, psi, q):
    # bracket dual to omega: {phi, psi} = phi J^{-1} psi^T, J^{-1} = -J for this J;
    # sign convention irrelevant for the zero/non-zero tests
    return (phi[0] * psi[1] - phi[1] * psi[0] + phi[2] * psi[3] - phi[3] * psi[2]) % q


bad = 0
tested = 0
for q, Ms, Bs, lp in ((2, SP[2], [(0, 0, 0, 0)], False), (3, LP3, [(0, 0, 0, 0)], True)):
    F = meter_functionals(q)
    for (l, k) in sa1c_laws(q):
        S = product_support(range(q), line_pts(l, k, q))
        lfun = (0, 0, l[0], l[1])
        for M in Ms:
            for f in F:
                fun = (0, 0, f[0], f[1])
                vals = []
                ok = True
                for c in (0, 1):
                    vs = {(f[0] * y[2] + f[1] * y[3]) % q for y in (app(M, s, (0, 0, 0, 0), q) for s in S[c])}
                    if len(vs) != 1:
                        ok = False
                        break
                    vals.append(vs.pop())
                if not ok or vals[0] == vals[1]:
                    continue
                tested += 1
                fM = rowmul(fun, M, q)
                # fM = alpha c + lambda l ?
                found = any(tuple((a * (1 if j == 0 else 0) + lam * lfun[j]) % q for j in range(4)) == fM
                            for a in range(1, q) for lam in range(q))
                xM = rowmul((0, 1, 0, 0), M, q)
                if not found or br(xM, fM, q) != 0:
                    bad += 1
check("(3a) every readable (M, f): f o M = alpha c + lambda l, alpha != 0, and {x o M, f o M} = 0",
      bad == 0 and tested > 0, (tested, bad))

# --------------------------------------------------------------------------------------------------
print("== (4) sharp meters: every readable LP recorder acts on x by a known displacement on each branch")
for q, cnts in ((2, (288, 144)), (3, (15552, 5184))):
    F = meter_functionals(q)
    res = []
    alldisp = True
    for pt in itertools.product(range(q), repeat=2):
        S = product_support(range(q), [pt])
        nr = nid = 0
        for M in (LP2 if q == 2 else LP3):
            for b in vecs(q):
                if not is_lp(M, b) or not readable(M, b, S, q, F):
                    continue
                nr += 1
                for c in (0, 1):
                    if len(disp_set(M, b, S[c], q)) != 1:
                        alldisp = False
                if disp_set(M, b, S[0], q) == {0}:
                    nid += 1
        res.append((nr, nid))
    check(f"(4a) q={q}: per sharp state, readable LP recorders / K_null = id = {cnts}", set(res) == {cnts}, res)
    check(f"(4b) q={q}: every readable LP recorder: x'-x constant on each branch (known displacement)", alldisp)
    check(f"(4c) q={q}: the rest ({cnts[0] - cnts[1]}) have K_null != id by a nonzero known displacement",
          all(r - i == cnts[0] - cnts[1] > 0 for r, i in res))
# coefficient-1 argument: c o M = c forces x o M to have coefficient 1 on x
check("(4d) every LP symplectic linear part (q=2,3) has (x o M)_x = 1",
      all(M[1][1] == 1 for M in LP2) and all(M[1][1] == 1 for M in LP3))

# --------------------------------------------------------------------------------------------------
print("== (5) N1: the reciprocal coupling with a sharp meter; identity iff the conjugate slot m' is 0")
for q in (2, 3):
    # (c, x, m, m') -> (c, x - m', m + c, m') is symplectic over any F_q (equals x + m' at q = 2)
    R = ((1, 0, 0, 0), (0, 1, 0, q - 1), (1, 0, 1, 0), (0, 0, 0, 1))
    check(f"(5a) q={q}: reciprocal coupling symplectic and location-preserving", is_sympl(R, q) and R[0] == (1, 0, 0, 0))
    F = meter_functionals(q)
    ok = True
    for (m, mp) in itertools.product(range(q), repeat=2):
        S = product_support(range(q), [(m, mp)])
        rd = readable(R, (0, 0, 0, 0), S, q, F)
        D = disp_set(R, (0, 0, 0, 0), S[0], q)
        known = len(D) == 1
        ident = D == {0}
        if not (rd and known and ident == (mp == 0)):
            ok = False
    check(f"(5b) q={q}: every sharp state records readably, displacement known, identity iff m' = 0", ok)
S01 = product_support(range(2), [(0, 1)])
R2 = ((1, 0, 0, 0), (0, 1, 0, 1), (1, 0, 1, 0), (0, 0, 0, 1))
check("(5c) the r7 sentence 'sharp meter => K_null = id' is false: meter (0,1) readable, x -> x+1 on c=0",
      readable(R2, (0, 0, 0, 0), S01, 2, meter_functionals(2)) and disp_set(R2, (0, 0, 0, 0), S01[0], 2) == {1})
# under SA-1(c) with known functional m (m' unknown): reciprocal coupling readable, x'-x non-constant
Sm = product_support(range(2), line_pts((1, 0), 0, 2))
check("(5d) reciprocal coupling under SA-1(c) (m known): readable, x'-x non-constant on c=0",
      readable(R2, (0, 0, 0, 0), Sm, 2, meter_functionals(2)) and len(disp_set(R2, (0, 0, 0, 0), Sm[0], 2)) == 2)

# --------------------------------------------------------------------------------------------------
print("== (6) N2: independence is load-bearing (a correlated family different from p14 (5e))")
# meter: m' known (= k0), m = s x + t c + u (s != 0): on each branch uniform on the line {m' = k0},
# but a function of the carrier.  Search linear parts (b = 0 suffices for constancy and readability).
for q in (2, 3):
    F = meter_functionals(q)
    found_all = []
    lp_found = 0
    for s in range(1, q):
        for t in range(q):
            S = {c: [(c, x, (s * x + t * c) % q, 0) for x in range(q)] for c in (0, 1)}
            n = 0
            for M in SP[q]:
                if readable(M, (0, 0, 0, 0), S, q, F) and len(disp_set(M, (0, 0, 0, 0), S[0], q)) == 1:
                    n += 1
                    if M[0] == (1, 0, 0, 0):
                        lp_found += 1
            found_all.append(n)
    check(f"(6a) q={q}: with the correlated meter some readable symplectic part has constant x'-x (Q4-P20 "
          f"fails without independence)", all(n > 0 for n in found_all), found_all)
    print(f"     q={q}: location-preserving parts among them: {lp_found}")
    # control: the independent (product) law on the same line {m' = 0}, same search
    S = product_support(range(q), line_pts((0, 1), 0, q))
    nprod = sum(1 for M in SP[q] if readable(M, (0, 0, 0, 0), S, q, F)
                and len(disp_set(M, (0, 0, 0, 0), S[0], q)) == 1)
    check(f"(6b) q={q}: control, product law on the same line: no readable part with constant x'-x", nprod == 0,
          nprod)

# --------------------------------------------------------------------------------------------------
print("== (7) countercontrol: copy coupling (not symplectic) under SA-1(c) records with K_null = id")
CP = ((1, 0, 0, 0), (0, 1, 0, 0), (1, 0, 1, 0), (0, 0, 0, 1))
Sm = product_support(range(2), line_pts((1, 0), 0, 2))
check("(7a) copy coupling not symplectic; readable; x'-x = 0 on c=0",
      (not is_sympl(CP, 2)) and readable(CP, (0, 0, 0, 0), Sm, 2, meter_functionals(2))
      and disp_set(CP, (0, 0, 0, 0), Sm[0], 2) == {0})

# --------------------------------------------------------------------------------------------------
print("== (8) assumption-watch: non-LP readable recorders under SA-1(c) whose x'-x depends only on x")
# x'-x non-constant on c=0 can come from (x o M)_x != 1 rather than from the unknown meter slot.
for q in (2, 3):
    F = meter_functionals(q)
    only_x = 0
    total = 0
    for (l, k) in sa1c_laws(q)[:1]:
        S = product_support(range(q), line_pts(l, k, q))
        for M in SP[q]:
            if not readable(M, (0, 0, 0, 0), S, q, F):
                continue
            total += 1
            # x'-x as a function on the c=0 support: does it depend on the meter point at fixed x?
            dep_meter = False
            for x in range(q):
                vals = {(app(M, s, (0, 0, 0, 0), q)[1] - s[1]) % q for s in S[0] if s[1] == x}
                if len(vals) > 1:
                    dep_meter = True
            if not dep_meter:
                only_x += 1
    print(f"     q={q}, first law: readable parts {total}; x'-x independent of the meter point at fixed x: {only_x}")

print(f"\nTOTAL: {NP} passed, {NF} failed")
raise SystemExit(0 if NF == 0 else 1)
