"""Bounded native instrument under the report18 rule: exact record laws, identities, closure, native realization.

Deterministic. Exact rationals (fractions) for every probability; numpy for the native lattice runs.
Usage: python3 instrument_checks.py
"""
import sys
from fractions import Fraction as F
from itertools import product
import numpy as np

FAIL = []
def control(name, ok, detail=''):
    print('%s %s%s' % ('PASS' if ok else 'FAIL', name, (': ' + detail) if detail else ''))
    if not ok: FAIL.append(name)
    return ok

# ---------------------------------------------------------------- menu
AX = {'X': (F(1), F(0), F(0)), 'Y': (F(0), F(1), F(0)), 'Z': (F(0), F(0), F(1)), 'R': (F(4, 5), F(3, 5), F(0))}
AXES = ['X', 'Y', 'Z', 'R']
PREPS = [(s, a) for a in AXES for s in (1, -1)]           # (+X,-X,+Y,...)
def vec(prep): s, a = prep; return tuple(s * x for x in AX[a])
def dot(u, v): return sum(x * y for x, y in zip(u, v))
def p_plus(c, w): return (1 + dot(AX[c], w)) / 2        # Born probability of + along c for Bloch vector w
def name(prep): return ('+' if prep[0] > 0 else '-') + prep[1]

# ---------------------------------------------------------------- identities and witness
REL = [  # coefficients over PREPS order (+X,-X,+Y,-Y,+Z,-Z,+R,-R)
    (1, 1, -1, -1, 0, 0, 0, 0), (1, 1, 0, 0, -1, -1, 0, 0), (1, 1, 0, 0, 0, 0, -1, -1),
    (-4, 4, -3, 3, 0, 0, 5, -5)]
WIT_A = {(1, 'R'): F(13, 16), (-1, 'R'): F(3, 16)}
WIT_B = {(1, 'X'): F(1, 2), (1, 'Y'): F(3, 8), (1, 'Z'): F(1, 16), (-1, 'Z'): F(1, 16)}

def identities(K):
    """K: {prep: {atom: prob}}. Returns the largest |identity value| over atoms (exact)."""
    atoms = set().union(*[set(K[p]) for p in PREPS])
    worst = F(0)
    for r in REL:
        for at in atoms:
            v = sum(c * K[p].get(at, F(0)) for c, p in zip(r, PREPS))
            worst = max(worst, abs(v))
    return worst

def witness_tv(K):
    atoms = set().union(*[set(K[p]) for p in PREPS])
    tv = F(0)
    for at in atoms:
        pa = sum(wt * K[p].get(at, F(0)) for p, wt in WIT_A.items())
        pb = sum(wt * K[p].get(at, F(0)) for p, wt in WIT_B.items())
        tv += abs(pa - pb)
    return tv / 2

def check_rank():
    M = [[F(1)] * 8] + [[vec(p)[i] for p in PREPS] for i in range(3)]
    def rank(rows):
        rows = [list(r) for r in rows]; rk = 0
        for c in range(len(rows[0])):
            piv = next((i for i in range(rk, len(rows)) if rows[i][c] != 0), None)
            if piv is None: continue
            rows[rk], rows[piv] = rows[piv], rows[rk]
            for i in range(len(rows)):
                if i != rk and rows[i][c] != 0:
                    f = rows[i][c] / rows[rk][c]; rows[i] = [x - f * y for x, y in zip(rows[i], rows[rk])]
            rk += 1
        return rk
    innull = all(sum(F(r[j]) * M[i][j] for j in range(8)) == 0 for r in REL for i in range(4))
    return rank(M) == 4 and rank([[F(x) for x in r] for r in REL]) == 4 and innull

# ---------------------------------------------------------------- heralded preparation (rejection sampling)
U_BITS, THRESH, M_ATT = 4, 10, 2       # four fair bits per component, accept iff u < 10, at most 2 attempts
def component_sampler(p):
    """Exact law of one component from one attempt: (accept prob, P(bit=1 | accept)), by enumerating u."""
    acc = [u for u in range(2 ** U_BITS) if u < THRESH]
    k = p * THRESH
    if k.denominator != 1: raise RuntimeError('sampler threshold not integral')
    ones = [u for u in acc if u < k]
    return F(len(acc), 2 ** U_BITS), F(len(ones), len(acc))

def herald_law(n_comp, thresh_extra=None):
    """Attempt-index law for a sampler that needs all n_comp components accepted in the same attempt."""
    q = F(THRESH, 2 ** U_BITS) ** n_comp
    if thresh_extra is not None: q *= thresh_extra
    law = {}
    for j in range(1, M_ATT + 1): law[j] = (1 - q) ** (j - 1) * q
    law['fail'] = (1 - q) ** M_ATT
    return law

def prepared_law(w):
    """mu_w: exact joint law of the hidden register lambda = (l_X,l_Y,l_Z,l_R), from the sampler."""
    law = {}
    for bits in product((0, 1), repeat=4):
        pr = F(1)
        for c, b in zip(AXES, bits):
            _, p1 = component_sampler(p_plus(c, w))
            pr *= p1 if b else 1 - p1
        law[bits] = pr
    return law

def fresh_law(a):
    """r: fresh bits for re-preparation with setting a, r_c ~ Bern((1+a.c)/2) (r_a = 1 surely)."""
    return prepared_law(AX[a])

# ---------------------------------------------------------------- register-level instrument
def reprepare(lam, r, a):
    ia = AXES.index(a)
    return tuple(lam[ia] ^ 1 ^ rc for rc in r)   # lambda'_c = lambda_a xor 1 xor r_c

def single_read_law(prep, a, variant='instrument'):
    w = vec(prep)
    H1 = herald_law(4, F(1, 2) if (variant == 'herald-w' and prep[1] == 'R') else None)
    H2 = herald_law(4)
    mu, rl = prepared_law(w), fresh_law(a)
    ia = AXES.index(a)
    K = {('pfail',): H1['fail']}
    for j in (1, 2):
        for lam, pl in mu.items():
            o = lam[ia]
            for j2 in (1, 2, 'fail'):
                if variant == 'junk':          # record also shows the unread hidden components
                    at = (j, o, j2) + tuple(lam[i] for i in range(4) if i != ia)
                else:
                    at = (j, o, j2)
                if variant == 'fresh' and j2 != 'fail':
                    for r, prr in rl.items():
                        at2 = at + r
                        K[at2] = K.get(at2, F(0)) + H1[j] * pl * H2[j2] * prr
                    continue
                K[at] = K.get(at, F(0)) + H1[j] * pl * H2[j2]
    return K

def two_read_law(prep, a, c, variant='instrument'):
    w = vec(prep)
    H = herald_law(4)
    mu, rl, rl2 = prepared_law(w), fresh_law(a), fresh_law(c)
    ia, ic = AXES.index(a), AXES.index(c)
    K = {('pfail',): H['fail']}
    for j in (1, 2):
        for lam, pl in mu.items():
            o = lam[ia]
            K[(j, o, 'fail')] = K.get((j, o, 'fail'), F(0)) + H[j] * pl * H['fail']
            for j2 in (1, 2):
                for r, prr in rl.items():
                    lam2 = lam if variant == 'nondisturbing' else reprepare(lam, r, a)
                    o2 = lam2[ic]
                    for j3 in (1, 2, 'fail'):
                        at = (j, o, j2, o2, j3)
                        K[at] = K.get(at, F(0)) + H[j] * pl * H[j2] * prr * H[j3]
    return K

def quantum_single(prep, a):
    w = vec(prep); H1 = herald_law(4); H2 = herald_law(4)
    K = {('pfail',): H1['fail']}
    for j in (1, 2):
        for o in (0, 1):
            po = p_plus(a, w) if o else 1 - p_plus(a, w)
            for j2 in (1, 2, 'fail'):
                K[(j, o, j2)] = H1[j] * po * H2[j2]
    return K

def quantum_two(prep, a, c):
    w = vec(prep); H = herald_law(4)
    K = {('pfail',): H['fail']}
    for j in (1, 2):
        for o in (0, 1):
            po = p_plus(a, w) if o else 1 - p_plus(a, w)
            K[(j, o, 'fail')] = H[j] * po * H['fail']
            s = 1 if o else -1
            post = tuple(s * x for x in AX[a])
            for j2 in (1, 2):
                for o2 in (0, 1):
                    p2 = p_plus(c, post) if o2 else 1 - p_plus(c, post)
                    for j3 in (1, 2, 'fail'):
                        K[(j, o, j2, o2, j3)] = H[j] * po * H[j2] * p2 * H[j3]
    return K

# ---------------------------------------------------------------- native realization (report18 rule)
KT = 2                      # read tick
SP, OFF, L = 8, 6, 44       # spacing of copy sites, offset, torus side

def S(X):
    o = np.zeros_like(X)
    for ax in (-3, -2, -1): o ^= np.roll(X, 1, ax) ^ np.roll(X, -1, ax)
    return o
def step(p, c):
    sa, sb, sd = S(c[0]), S(c[1]), S(c[2])
    return (p[0] ^ sb, p[1] ^ sd, p[2] ^ sa ^ (sb & sd))

def copy_site(b, k): return (SP * k + OFF, SP * b + OFF, OFF)
def receiver(a, k):  x, y, z = copy_site(AXES.index(a), k); return (x - KT, y, z)
def l1(L, centre):
    r = [np.minimum((np.arange(L) - c) % L, (c - np.arange(L)) % L) for c in centre]
    return r[0][:, None, None] + r[1][None, :, None] + r[2][None, None, :]

def native_layout(a):
    """Device k=0: record (lambda_a copy only). Device k=1..4: outgoing component c_k, with lambda_a copy at +x,
    fresh r_c at +y and constant 1 at +z, all in field A, all at L1 distance KT from the receiver."""
    devs = []
    for k in range(5):
        rc = receiver(a, k)
        srcs = [(copy_site(AXES.index(a), k), 'lam')]
        if k >= 1:
            srcs.append(((rc[0], rc[1] + KT, rc[2]), ('r', k - 1)))
            srcs.append(((rc[0], rc[1], rc[2] + KT), 'one'))
        devs.append((rc, srcs))
    return devs

def native_run(a, assignments, seed, ticks=KT, release=None, record_radius=None):
    """assignments: list of (lam(4), r(4)). Returns {k: array (N, ticks+1, 3)} of receiver triples per tick
    (index t = 0..ticks)."""
    N = len(assignments); rng = np.random.default_rng(seed)
    p = [np.repeat(rng.integers(0, 2, (1, L, L, L), dtype=np.uint8), N, 0) for _ in range(3)]
    c = [np.repeat(rng.integers(0, 2, (1, L, L, L), dtype=np.uint8), N, 0) for _ in range(3)]
    devs = native_layout(a)
    # hidden copies of every component at every device slot (setting-independent preparation)
    lam = np.array([x[0] for x in assignments], dtype=np.uint8); rr = np.array([x[1] for x in assignments], dtype=np.uint8)
    for k, (rc, srcs) in enumerate(devs):
        rad = KT if (k != 0 or record_radius is None) else record_radius
        d = l1(L, rc)
        for f in range(3):
            c[f][:, d <= rad] = 0; p[f][:, d <= rad - 1] = 0
    for b in range(4):
        for k in range(5):
            s = copy_site(b, k)
            for f in range(3): c[f][(slice(None),) + s] = 0; p[f][(slice(None),) + s] = 0
            c[0][(slice(None),) + s] = lam[:, b]
    for k, (rc, srcs) in enumerate(devs):
        for pos, kind in srcs:
            pos = tuple(v % L for v in pos)
            if kind == 'one': c[0][(slice(None),) + pos] = 1
            elif kind != 'lam': c[0][(slice(None),) + pos] = rr[:, kind[1]]
            # if record_radius is extended, other devices' sources stay as prepared (they are not pins)
    if release is not None:
        f, pos = release; c[f][(slice(None),) + pos] ^= 1
    out = {k: np.zeros((N, ticks + 1, 3), np.uint8) for k in range(5)}
    P, C = tuple(p), tuple(c)
    for k, (rc, _) in enumerate(devs): out[k][:, 0, :] = np.stack([C[f][(slice(None),) + rc] for f in range(3)], 1)
    for t in range(1, ticks + 1):
        P, C = C, step(P, C)
        for k, (rc, _) in enumerate(devs): out[k][:, t, :] = np.stack([C[f][(slice(None),) + rc] for f in range(3)], 1)
    return out

def arrival_field():
    f = 0                    # sources in field A; H maps A -> D -> B -> A
    for _ in range(KT): f = {0: 2, 2: 1, 1: 0}[f]
    return f

# ---------------------------------------------------------------- main
def main():
    print(__doc__.strip().splitlines()[0])
    # controls on the linear algebra and samplers
    control('C-RANK (1,w) rank 4; the four relations span its null space', check_rank())
    ok = all(component_sampler(p_plus(c, vec(w))) == (F(10, 16), p_plus(c, vec(w))) for c in AXES for w in PREPS)
    control('sampler: one attempt accepts with 10/16 per component and gives P(1|accept) = (1+c.w)/2 exactly', ok)
    dy = [p_plus('R', vec(w)) for w in PREPS]
    nondy = [x for x in dy if (x.denominator & (x.denominator - 1))]
    control('non-dyadic Born values on the R read', bool(nondy), 'e.g. %s; a subspace readiness event (power-of-two count) cannot give them' % nondy[:2])

    # C-QM and C-AFF
    qs = max(identities({p: quantum_single(p, a) for p in PREPS}) for a in AXES)
    q2 = max(identities({p: quantum_two(p, a, c) for p in PREPS}) for a in AXES for c in AXES)
    control('C-QM quantum record laws satisfy the identities (single and two reads)', qs == 0 and q2 == 0)
    beta = (F(1, 4), F(1, 2), F(0))
    Kaff = {p: {(o,): (F(1, 2) + dot(beta, vec(p))) if o else 1 - (F(1, 2) + dot(beta, vec(p))) for o in (0, 1)} for p in PREPS}
    born_ok = all(Kaff[p][(1,)] == p_plus('R', vec(p)) for p in PREPS)
    control('C-AFF an affine non-Born law passes the identities (identities do not test Born)', identities(Kaff) == 0 and not born_ok)

    # Q1, Q3 single read
    q1 = {a: identities({p: single_read_law(p, a) for p in PREPS}) for a in AXES}
    born1 = all(sum(v for at, v in single_read_law(p, a).items() if len(at) == 3 and at[1] == 1)
                / sum(v for at, v in single_read_law(p, a).items() if len(at) == 3) == p_plus(a, vec(p))
                for p in PREPS for a in AXES)
    # Q2, Q3 two reads
    q2v = {(a, c): identities({p: two_read_law(p, a, c) for p in PREPS}) for a in AXES for c in AXES}
    eq_quantum = all(two_read_law(p, a, c) == quantum_two(p, a, c) for p in PREPS for a in AXES for c in AXES)
    eq_quantum1 = all(single_read_law(p, a) == quantum_single(p, a) for p in PREPS for a in AXES)

    # C-ND, C-HER
    nd = {(a, c): identities({p: two_read_law(p, a, c, 'nondisturbing') for p in PREPS}) for a in AXES for c in AXES}
    nd_fail = [k for k, v in nd.items() if v != 0]
    nd_tv = max(witness_tv({p: two_read_law(p, a, c, 'nondisturbing') for p in PREPS}) for a, c in nd_fail)
    control('C-ND non-disturbing instrument fails the sequential identities', len(nd_fail) > 0,
            '%d of 16 setting pairs fail; largest witness TV %s' % (len(nd_fail), nd_tv))
    her = {a: identities({p: single_read_law(p, a, 'herald-w') for p in PREPS}) for a in AXES}
    her_tv = max(witness_tv({p: single_read_law(p, a, 'herald-w') for p in PREPS}) for a in AXES)
    control('C-HER w-dependent herald fails the single-read identities', all(v != 0 for v in her.values()),
            'witness TV up to %s' % her_tv)

    # Q4 closure (register level): conditional on (j, o, j2 success), lambda' ~ mu_{s a}
    clos = True
    for a in AXES:
        for p in PREPS:
            mu, rl = prepared_law(vec(p)), fresh_law(a)
            ia = AXES.index(a)
            for o in (0, 1):
                po = sum(v for lam, v in mu.items() if lam[ia] == o)
                if po == 0: continue
                cond = {}
                for lam, pl in mu.items():
                    if lam[ia] != o: continue
                    for r, prr in rl.items():
                        l2 = reprepare(lam, r, a); cond[l2] = cond.get(l2, F(0)) + pl * prr / po
                s = 1 if o else -1
                target = prepared_law(tuple(s * x for x in AX[a]))
                clos &= all(cond.get(k, F(0)) == v for k, v in target.items())
    # Q6 (a) junk, (b) fresh access
    junk = {a: identities({p: single_read_law(p, a, 'junk') for p in PREPS}) for a in AXES}
    junk_tv = {a: witness_tv({p: single_read_law(p, a, 'junk') for p in PREPS}) for a in AXES}
    fresh_id = {a: identities({p: single_read_law(p, a, 'fresh') for p in PREPS}) for a in AXES}
    # closure given a record that also shows the fresh bits r: for each setting, compare the conditional law of
    # lambda' given (o, r) with the prepared law of P_{s a}, as for Q4
    fresh_clos = {}
    for a in AXES:
        ok = True; ia = AXES.index(a)
        for p in PREPS:
            mu, rl = prepared_law(vec(p)), fresh_law(a)
            for o in (0, 1):
                for r, prr in rl.items():
                    if prr == 0: continue
                    po = sum(v for lam, v in mu.items() if lam[ia] == o)
                    if po == 0: continue
                    cond = {}
                    for lam, pl in mu.items():
                        if lam[ia] != o: continue
                        l2 = reprepare(lam, r, a); cond[l2] = cond.get(l2, F(0)) + pl / po
                    target = prepared_law(tuple((1 if o else -1) * x for x in AX[a]))
                    ok &= all(cond.get(k, F(0)) == v for k, v in target.items())
        fresh_clos[a] = ok
    fresh_closure_fails = {a: not v for a, v in fresh_clos.items()}

    # ---------------- native realization
    fA = arrival_field()
    assigns = list(product(product((0, 1), repeat=4), [None]))
    nat_ok = True; nat_cases = 0
    for a in AXES:
        ia = AXES.index(a)
        lst = []
        for lam in product((0, 1), repeat=4):
            for rbits in product((0, 1), repeat=3):
                r = list(rbits); r.insert(ia, 1)        # r_a = 1 surely
                lst.append((lam, tuple(r)))
        for seed in (101, 202):
            out = native_run(a, lst, seed)
            for n_, (lam, r) in enumerate(lst):
                rec = out[0][n_, KT]; want = [0, 0, 0]; want[fA] = lam[ia]
                nat_ok &= list(rec) == want
                lp = reprepare(lam, r, a)
                for k in range(1, 5):
                    v = out[k][n_, KT]; want = [0, 0, 0]; want[fA] = lp[k - 1]
                    nat_ok &= list(v) == want
                # silent before the read tick
                nat_ok &= all(int(out[k][n_, t].sum()) == 0 for k in range(5) for t in range(KT))
                nat_cases += 1
    # C-NAT: release a load-bearing pin (current field A at the record receiver + 2y, even distance) -> output changes.
    # Observation: a current-slice pin at odd distance (receiver + y, field B) cannot affect the tick-2 value (parity).
    a = 'X'; rc = receiver(a, 0)
    lst = [(lam, (1, 1, 1, 1)) for lam in product((0, 1), repeat=4)]
    base = native_run(a, lst, 101)
    rel = native_run(a, lst, 101, release=(0, (rc[0], rc[1] + 2, rc[2])))
    odd = native_run(a, lst, 101, release=(1, (rc[0], rc[1] + 1, rc[2])))
    control('C-NAT releasing one load-bearing readiness pin (even distance) changes an accessible register',
            not np.array_equal(base[0][:, KT], rel[0][:, KT]))
    print('observation: releasing an odd-distance current-slice pin leaves the tick-%d record unchanged: %s'
          ' (parity: such pins are not load-bearing, so the readiness count is not minimal)'
          % (KT, np.array_equal(base[0][:, KT], odd[0][:, KT])))
    pins_record = 3 * (25 + 7) - 1; pins_out = 3 * (25 + 7) - 3
    control('Q5 native realization: record and outgoing registers equal the register-level map', bool(nat_ok),
            '%d runs (%d input assignments x 2 dense full-torus backgrounds); arrival field %s; receivers silent'
            ' before tick %d' % (nat_cases, nat_cases // 2, 'ABD'[fA], KT))

    # Q6 (c) native time-extended record access at the record site
    win = {}
    for a in AXES:
        ia = AXES.index(a)
        lst = []; wts = {}
        for lam in product((0, 1), repeat=4):
            for rbits in product((0, 1), repeat=3):
                r = list(rbits); r.insert(ia, 1); lst.append((lam, tuple(r)))
        TT = 12
        out = native_run(a, lst, 303, ticks=TT, record_radius=TT)
        mus = {p: prepared_law(vec(p)) for p in PREPS}; rl = fresh_law(a)
        for D in range(0, TT - KT + 1):
            K = {}
            for p in PREPS:
                law = {}
                for n_, (lam, r) in enumerate(lst):
                    at = tuple(out[0][n_, KT:KT + D + 1].reshape(-1).tolist())
                    law[at] = law.get(at, F(0)) + mus[p][lam] * rl[r]
                K[p] = law
            win[(a, D)] = (identities(K), witness_tv(K))
    first_leak = {a: min([D for D in range(0, 11) if win[(a, D)][0] != 0], default=None) for a in AXES}
    # which unread hidden components the widened record depends on (direct dependence test at each window)
    dep = {}
    for a in AXES:
        ia = AXES.index(a)
        lst = []
        for lam in product((0, 1), repeat=4):
            for rbits in product((0, 1), repeat=3):
                r = list(rbits); r.insert(ia, 1); lst.append((lam, tuple(r)))
        out = native_run(a, lst, 303, ticks=12, record_radius=12)
        first = {}
        for b in range(4):
            if b == ia: continue
            for D in range(0, 11):
                rec = {}
                varies = False
                for n_, (lam, r) in enumerate(lst):
                    key = tuple(v for i, v in enumerate(lam) if i != b) + r
                    val = tuple(out[0][n_, KT:KT + D + 1].reshape(-1).tolist())
                    if key in rec and rec[key] != val: varies = True
                    rec[key] = val
                if varies: first[AXES[b]] = D; break
        dep[a] = first

    # ---------------- results
    print()
    print('Q1 single-read identities (exact, complete record = prep herald, outcome, re-prep herald):',
          {a: str(v) for a, v in q1.items()})
    print('Q2 two-read identities, 16 setting pairs, largest |identity|:', max(q2v.values()))
    print('Q3 Born: single-read outcome probabilities exact:', born1, '; complete single-read law = quantum law:', eq_quantum1,
          '; complete two-read law = quantum law (all w, a, c):', eq_quantum)
    print('Q4 closure: outgoing law given (herald, outcome) equals the prepared law of P_{s a}, jointly:', clos)
    print('Q6a record also shows unread hidden components: identities', {a: str(v) for a, v in junk.items()},
          'witness TV', {a: str(v) for a, v in junk_tv.items()})
    print('Q6b record also shows the fresh re-preparation bits: identities', {a: str(v) for a, v in fresh_id.items()},
          '; closure given that record fails, by setting (conditional law of the outgoing state vs P_{s a}):',
          fresh_closure_fails)
    print('Q6c record site read natively at ticks KT..KT+D (readiness extended): first D with an identity violation',
          first_leak, '; witness TV at D=10:', {a: '%.6f' % float(win[(a, 10)][1]) for a in AXES})
    print('Q6c the widened record depends on unread hidden components from window D:', dep,
          '(a dependence the identities do not flag is invisible to this menu, not protected)')
    print('Resources: herald acceptance per attempt (10/16)^4 = %s; readiness pins per record device %d, per outgoing'
          ' device %d (5 devices: %d); hidden copies 5 per component (16 copy equalities); fresh biased bits 3 per read'
          % (F(10, 16) ** 4, pins_record, pins_out, pins_record + 4 * pins_out))
    green = not FAIL
    print()
    if green:
        q1ok = all(v == 0 for v in q1.values()); q2ok = max(q2v.values()) == 0
        print('VERDICT (generated): identities %s on the complete single-read record and %s on the complete two-read'
              ' record; Born values %s; closure %s; native realization %s. Widening access to the unread hidden'
              ' components %s the identities (settings failing: %s); exposing the fresh bits %s the identities and %s'
              ' closure given the record (settings where closure fails: %s); reading the native record site at later'
              ' ticks gives a first identity violation by setting of %s, for this layout.'
              % ('HOLD exactly' if q1ok else 'FAIL', 'HOLD exactly' if q2ok else 'FAIL',
                 'exact' if (born1 and eq_quantum and eq_quantum1) else 'NOT exact', 'HOLDS' if clos else 'FAILS',
                 'HOLDS' if nat_ok else 'FAILS',
                 'breaks' if any(v != 0 for v in junk.values()) else 'keeps',
                 [a for a in AXES if junk[a] != 0],
                 'keeps' if all(v == 0 for v in fresh_id.values()) else 'breaks',
                 'breaks' if any(fresh_closure_fails.values()) else 'keeps',
                 [a for a in AXES if fresh_closure_fails[a]], first_leak))
    else:
        print('NO VERDICT: controls failed:', FAIL)
    return 0 if green else 1

if __name__ == '__main__':
    sys.exit(main())
