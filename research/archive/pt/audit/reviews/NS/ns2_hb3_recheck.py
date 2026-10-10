#!/usr/bin/env python3
"""ns2_hb3_recheck.py -- thread NS, node N2.2 (exact; stdlib only; deterministic output).

PURPOSE. Independent exact re-evaluation -- NOT a replay: no probe script for HB3-a exists at L -- of
round H-B's kernel witness HB3-a (HexLatticeGas.lean:875-997) and of round H-A's H3a witness and closing
control (HydroSourceAudit.lean:804-890), from the Lean definitions transcribed by hand, plus countercontrols
that locate what the H-B witness depends on.

DEFINITIONS transcribed from HexLatticeGas.lean (line numbers at L = 9f9f8257):
  hexDir (L127): c0=(1,0) c1=(0,1) c2=(-1,1) c3=(-1,0) c4=(0,-1) c5=(1,-1).
  hexCollide (L162-170): s -> swap(A,B)(swap(B,C)(swap(D,E)(s))), A={0,3}, B={1,4}, C={2,5},
    D={0,2,4}, E={1,3,5} (occupation sets of the 6 Boolean channels).
  hexGas (L261-262): (gas c) i k = hexCollide(c(i - c_k)) k ; inverse (L264-265):
    (gas^-1 c) i = hexCollide^-1(k -> c(i + c_k) k).  Sites Z_4 x Z_4 for L = 4.
  blocks at b = 2 (L897): block(i) = (i0 // 2, i1 // 2).  hexSum (L357): sum over block, sum_k n_k w_k.
H-A (HydroSourceAudit.lean): leap (prev, cur) -> (cur, F(cur) - prev); F(c)_j = alpha (c_{j+1} + c_{j-1})
  (waveF_one_dim, L770-773); blockSum over blocks of side b; values in Z_q.

CHECKS (each prints PASS or FAIL; exact integer arithmetic):
  A1  hexCollide moves exactly A->B->C->A and D<->E and fixes the other 59 states (hexCollide_moved, _of_ne).
  A2  the four gas values of hb3a_gas_values (L875-889).
  A3  for every block and every channel (hence every integer weight w) the block counts of c and c' agree at t
      and at t-1 (L947-954).
  A4  at t+1, P1 (weight k -> c_k[0]) on block (0,0) is 1 for c and 0 for c' (L955-958).
  A5  equal (M,P1,P2) two-time block states and different next states (the content of hb3a_no_closure).
  CC1 collision removed (identity collision = pure streaming): the same pair has equal block counts at t+1
      too, so it no longer witnesses non-closure.
  CC2 resolution b = 1 (blocks = sites): c and c' differ already at t.
  C3  pure streaming at L = 4, b = 2: the block of i + 2c_k depends only on the block of i (exhaustive over
      16 sites x 6 channels), hence hist_{t+1}(beta,k) = hist_{t-1}(beta - c_k, k); verified on EVERY
      configuration of mass <= 2 (4657 configurations).
  CC3 the same histogram rule fails for the gas on c' (and the two-time histograms of c, c' coincide).
  H1  H-A witness at d=1, L=6, b=3, alpha=1, q in {2,3,4,5,7}: block states equal at t and t-1, differ at t+1
      (block {0,1,2} of the y-trajectory sums to 1).
  H2  H-A closing control at d=1, L=4, b=2: Phi(u,v)(beta) = alpha(u0+u1) - v(beta) reproduces the next block
      state for EVERY phase-space configuration, q in {2,3}, every alpha in Z_q (exhaustive).
  CC4 the perturbed rule alpha(u0+u1) + v(beta) fails on some configuration, q = 3, every alpha.

DECISION RULE (fixed before the first run).
  VERDICT-HB3: "HB3-a re-evaluated exactly at L=4, b=2; the separating information is collision-dependent"
    iff A1-A5, CC1, CC2, C3, CC3 all PASS; "HB3-a re-evaluated; not collision-dependent" iff A1-A5 PASS and
    CC1 FAILS; otherwise "NO VERDICT (control failed)".
  VERDICT-H3A: "H-A non-closure witness and closing control re-evaluated" iff H1, H2, CC4 all PASS, else
    "NO VERDICT (control failed)".
  Scope: the instances named; a re-evaluation of kernel statements, never evidence above them.
"""
from itertools import combinations, product

L = 4
DIRS = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
SITES = [(a, b) for a in range(L) for b in range(L)]
ZERO = (0,) * 6
results = {}


def state(chs):
    return tuple(1 if k in chs else 0 for k in range(6))


SA, SB, SC, SD, SE = (state({0, 3}), state({1, 4}), state({2, 5}),
                      state({0, 2, 4}), state({1, 3, 5}))


def swap(a, b, s):
    return b if s == a else (a if s == b else s)


def collide(s):
    return swap(SA, SB, swap(SB, SC, swap(SD, SE, s)))


def collide_inv(s):
    return swap(SD, SE, swap(SB, SC, swap(SA, SB, s)))


def ident(s):
    return s


def add(i, v, sign=1):
    return ((i[0] + sign * v[0]) % L, (i[1] + sign * v[1]) % L)


def gas(c, coll=collide):
    pre = {i: coll(c.get(i, ZERO)) for i in SITES}
    out = {}
    for i in SITES:
        s = tuple(pre[add(i, DIRS[k], -1)][k] for k in range(6))
        if s != ZERO:
            out[i] = s
    return out


def gas_inv(c, coll_inv=collide_inv):
    out = {}
    for i in SITES:
        s = coll_inv(tuple(c.get(add(i, DIRS[k]), ZERO)[k] for k in range(6)))
        if s != ZERO:
            out[i] = s
    return out


def hist(c, b=2):
    h = {}
    for i, s in c.items():
        beta = (i[0] // b, i[1] // b)
        for k in range(6):
            if s[k]:
                h[(beta, k)] = h.get((beta, k), 0) + 1
    return h


def charges(c, b=2):
    w = [[1] * 6, [d[0] for d in DIRS], [d[1] for d in DIRS]]
    out = {}
    for (beta, k), n in hist(c, b).items():
        for j in range(3):
            out[(beta, j)] = out.get((beta, j), 0) + n * w[j][k]
    return {key: v for key, v in out.items() if v != 0}


def record(name, ok, detail=""):
    results[name] = bool(ok)
    print(f"{name}: {'PASS' if ok else 'FAIL'}{(' -- ' + detail) if detail else ''}")


# A1
all_states = list(product((0, 1), repeat=6))
moved = {s: collide(s) for s in all_states if collide(s) != s}
want = {SA: SB, SB: SC, SC: SA, SD: SE, SE: SD}
inv_ok = all(collide_inv(collide(s)) == s for s in all_states)
record("A1", moved == want and inv_ok, f"moved states: {len(moved)}; inverse explicit on all 64: {inv_ok}")

# the witness (H-B result L272-273)
c = {(0, 0): state({0}), (0, 1): state({3})}
cp = {(0, 0): state({0, 3})}

# A2 (hb3a_gas_values)
g1 = gas(c) == {(1, 0): state({0}), (3, 1): state({3})}
g2 = gas_inv(c) == {(1, 1): state({3}), (3, 0): state({0})}
g3 = gas(cp) == {(0, 1): state({1}), (0, 3): state({4})}
g4 = gas_inv(cp) == {(1, 0): state({3}), (3, 0): state({0})}
record("A2", g1 and g2 and g3 and g4, f"[{g1},{g2},{g3},{g4}]")

# A3, A4, A5
eq_t = hist(c) == hist(cp)
eq_tm1 = hist(gas_inv(c)) == hist(gas_inv(cp))
record("A3", eq_t and eq_tm1, f"t: {sorted(hist(c).items())}; t-1: {sorted(hist(gas_inv(c)).items())}")
p1 = [charges(gas(x)).get(((0, 0), 1), 0) for x in (c, cp)]
record("A4", p1 == [1, 0], f"P1 on block (0,0) at t+1: c -> {p1[0]}, c' -> {p1[1]}")
two_eq = charges(c) == charges(cp) and charges(gas_inv(c)) == charges(gas_inv(cp))
record("A5", two_eq and charges(gas(c)) != charges(gas(cp)),
       f"next (M,P1,P2): c -> {sorted(charges(gas(c)).items())}; c' -> {sorted(charges(gas(cp)).items())}")

# CC1: pure streaming
fc, fcp = gas(c, ident), gas(cp, ident)
same_two = hist(gas_inv(c, ident)) == hist(gas_inv(cp, ident)) and hist(c) == hist(cp)
record("CC1", same_two and hist(fc) == hist(fcp),
       f"pure streaming t+1 histograms equal: {hist(fc) == hist(fcp)}")

# CC2: b = 1
record("CC2", hist(c, 1) != hist(cp, 1), "site-level states of c and c' differ at t")

# C3: pure-streaming histogram closure at L = 4, b = 2
def blk(i):
    return (i[0] // 2, i[1] // 2)


lemma = True
for k, d in enumerate(DIRS):
    image = {}
    for i in SITES:
        j = add(i, (2 * d[0], 2 * d[1]))
        image.setdefault(blk(i), set()).add(blk(j))
        if blk(j) != ((blk(i)[0] + d[0]) % 2, (blk(i)[1] + d[1]) % 2):
            lemma = False
    if any(len(v) != 1 for v in image.values()):
        lemma = False
slots = [(i, k) for i in SITES for k in range(6)]
n_conf, rule_ok = 0, True
for m in range(3):
    for chosen in combinations(slots, m):
        conf = {}
        for (i, k) in chosen:
            s = list(conf.get(i, ZERO))
            s[k] = 1
            conf[i] = tuple(s)
        n_conf += 1
        hm, hp = hist(gas_inv(conf, ident)), hist(gas(conf, ident))
        shifted = {(((beta[0] + DIRS[k][0]) % 2, (beta[1] + DIRS[k][1]) % 2), k): n
                   for (beta, k), n in hm.items()}
        if hp != shifted:
            rule_ok = False
record("C3", lemma and rule_ok and n_conf == 4657,
       f"block-shift lemma: {lemma}; rule on {n_conf} configurations of mass <= 2: {rule_ok}")

# CC3: the histogram rule fails for the gas on c'
hm = hist(gas_inv(cp))
shifted = {(((beta[0] + DIRS[k][0]) % 2, (beta[1] + DIRS[k][1]) % 2), k): n for (beta, k), n in hm.items()}
record("CC3", hist(gas(cp)) != shifted and hist(gas_inv(c)) == hist(gas_inv(cp)),
       f"gas t+1 histogram of c': {sorted(hist(gas(cp)).items())}; shift rule gives: {sorted(shifted.items())}")


# H-A wave representative, d = 1
def wave_next(prev, cur, alpha, q):
    n = len(cur)
    return [(alpha * (cur[(j + 1) % n] + cur[(j - 1) % n]) - prev[j]) % q for j in range(n)]


def bsum(x, b, q):
    return tuple(sum(x[j] for j in range(B * b, B * b + b)) % q for B in range(len(x) // b))


h1 = True
for q in (2, 3, 4, 5, 7):
    zero, y = [0] * 6, [(-1) % q, 1, 0, 0, 0, 0]
    ok = (bsum(zero, 3, q) == bsum(y, 3, q) == (0, 0)
          and bsum(wave_next(zero, zero, 1, q), 3, q) == (0, 0)
          and bsum(wave_next(zero, y, 1, q), 3, q)[0] == 1)
    h1 = h1 and ok
record("H1", h1, "q in {2,3,4,5,7}: equal two-time block states, block {0,1,2} at t+1: 0 vs 1")

h2, count = True, 0
for q in (2, 3):
    for alpha in range(q):
        for prev in product(range(q), repeat=4):
            for cur in product(range(q), repeat=4):
                u, v = bsum(cur, 2, q), bsum(prev, 2, q)
                pred = tuple((alpha * (u[0] + u[1]) - v[B]) % q for B in range(2))
                count += 1
                if bsum(wave_next(list(prev), list(cur), alpha, q), 2, q) != pred:
                    h2 = False
record("H2", h2, f"closing rule exact on all {count} (q, alpha, configuration) cases")

cc4 = True
q = 3
for alpha in range(q):
    fails = False
    for prev in product(range(q), repeat=4):
        cur = (0, 0, 0, 0)
        u, v = bsum(cur, 2, q), bsum(prev, 2, q)
        pred = tuple((alpha * (u[0] + u[1]) + v[B]) % q for B in range(2))
        if bsum(wave_next(list(prev), list(cur), alpha, q), 2, q) != pred:
            fails = True
            break
    cc4 = cc4 and fails
record("CC4", cc4, "perturbed rule refuted for every alpha in Z_3")

hb = ["A1", "A2", "A3", "A4", "A5", "CC1", "CC2", "C3", "CC3"]
if all(results[n] for n in hb):
    print("VERDICT-HB3: HB3-a re-evaluated exactly at L=4, b=2; the separating information is collision-dependent")
elif all(results[n] for n in hb[:5]) and not results["CC1"]:
    print("VERDICT-HB3: HB3-a re-evaluated; not collision-dependent")
else:
    print("VERDICT-HB3: NO VERDICT (control failed)")
if all(results[n] for n in ("H1", "H2", "CC4")):
    print("VERDICT-H3A: H-A non-closure witness and closing control re-evaluated")
else:
    print("VERDICT-H3A: NO VERDICT (control failed)")
print(f"checks: {sum(results.values())}/{len(results)} PASS")
