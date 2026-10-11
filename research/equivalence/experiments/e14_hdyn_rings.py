"""E14 probe -- three readings of 'H-DYN at every finite stage', on rings of 3 and 4 sites (exact, combinatorial).

Written 2026-10-11T01:29Z (date -u read at 01:29:27Z), after NOTES-E14 S0 and before the first run.

SETTING.  Q = {0, 1}; a ring of N sites; configurations x in Q^N.  The stage of a region Lam is M_Lam = Matrix(Q^Lam)
embedded in the top stage M_N; its matrix unit E^Lam_{c,c'} is the operator sum_y |c y><c' y| (y over the other sites).
An operator is stored as {(x, x'): k} meaning sum i^k |x><x'| (k mod 4), so every value is a power of i, exactly.
  (R-lit)  every matrix unit of every stage maps to a matrix unit of some stage (all k = 0 and the support is that of
           some E^Lam'_{d,d'});
  (R-top)  NOTES-E9's H-DYN: every matrix unit of the top stage maps to a matrix unit of the top stage;
  (R-01)   every matrix unit of every stage maps to a {0,1}-matrix in the configuration basis (all k = 0).
A configuration permutation P acts by |x><x'| -> |Px><Px'|.  SPR = site permutations with on-site relabelings,
(Px)_{pi(i)} = p_i(x_i).

CHECKS.
  R1  ring of 3, all 8! = 40320 configuration permutations: (R-lit) holds exactly for the 48 = 3! 2^3 members of SPR.
  R2  ring of 3, all 40320: (R-top) holds for every one (NOTES-E9's finite-level H-DYN admits every permutation).
  R3  ring of 4: every one of the 384 = 4! 2^4 members of SPR satisfies (R-lit) on all 624 units of all non-empty stages.
  R4  the CNOT update x -> (x0, x0 + x1, x2, ...) on rings of 3 and 4: a configuration permutation; (R-top) and (R-01)
      hold on every unit of every stage; (R-lit) fails, at E^{0}_{0,1}, whose image is |0><1| on site 0 times the flip
      on site 1 (no stage unit).
  R5  control, the two-site shift T^2 ((T^2 x)_i = x_{i-2}) on rings of 3 and 4: (R-lit), (R-top), (R-01) hold; the
      site-0 units go to site-2 units.
  R6  the rule x_i + x_{i+1} + x_{i+2} (mod 2): a permutation of Q^4 on the ring of 4, not of Q^3 on the ring of 3 (two
      images); on Z the configurations (110)^oo and 0^oo have the same image (every window of one period).
  R7  pair graphs of window-3 rules: the rule of R6 has a strongly connected component with a cycle through a
      non-diagonal vertex (two distinct periodic configurations with one image); T^2 as the window rule (a, b, c) -> a
      has none.
COUNTERCONTROLS (each must fail as stated).
  XR1 "the 3-cycle 000 -> 001 -> 010 -> 000 (others fixed) on the ring of 3 satisfies (R-lit)".
  XR2 "the phase automorphism, conjugation by diag(i^(x_0)), satisfies (R-01) at every stage on the ring of 3".

DECISION RULE (fixed before the first run).  VERDICT E14-HDYN-READINGS-SEPARATED iff R1 ... R7 all pass and XR1 and
XR2 both fail as stated; otherwise "VERDICT NOT RENDERED" with the failing items.  The verdict says that the instances
hold exactly; the infinite-volume statements ((R-lit) forces site permutations; (R-01) gives a ReversibleDynamics; the
one-dimensional ring criterion) are the written arguments of NOTES-E14.
"""
import itertools
import sys

RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''), flush=True)


Q = (0, 1)


def confs(N):
    return list(itertools.product(Q, repeat=N))


def unit(N, Lam, c, cp):
    rest = [i for i in range(N) if i not in Lam]
    op = {}
    for y in itertools.product(Q, repeat=len(rest)):
        x, xp = [None] * N, [None] * N
        for k, i in enumerate(Lam):
            x[i], xp[i] = c[k], cp[k]
        for k, i in enumerate(rest):
            x[i], xp[i] = y[k], y[k]
        op[(tuple(x), tuple(xp))] = 0
    return op


def all_units(N, nonempty=True):
    out = []
    for r in range(1 if nonempty else 0, N + 1):
        for Lam in itertools.combinations(range(N), r):
            for c in itertools.product(Q, repeat=r):
                for cp in itertools.product(Q, repeat=r):
                    out.append(((Lam, c, cp), unit(N, Lam, c, cp)))
    return out


UNITS = {N: all_units(N) for N in (3, 4)}
STAGE_SUPPORTS = {N: {frozenset(op) for _, op in all_units(N, nonempty=False)} for N in (3, 4)}
TOP = {N: [(lab, op) for lab, op in UNITS[N] if len(lab[0]) == N] for N in (3, 4)}


def conj_perm(op, P):
    return {(P[x], P[xp]): k for (x, xp), k in op.items()}


def conj_phase(op):
    return {(x, xp): (k + x[0] - xp[0]) % 4 for (x, xp), k in op.items()}


def is_stage_unit(op, N):
    return all(k == 0 for k in op.values()) and frozenset(op) in STAGE_SUPPORTS[N]


def is_top_unit(op, N):
    return all(k == 0 for k in op.values()) and len(op) == 1


def is_01(op):
    return all(k == 0 for k in op.values())


def r_lit(P, N):
    return all(is_stage_unit(conj_perm(op, P), N) for _, op in UNITS[N])


def spr(N):
    maps = set()
    for pi in itertools.permutations(range(N)):
        for rel in itertools.product([(0, 1), (1, 0)], repeat=N):
            P = {}
            for x in confs(N):
                y = [None] * N
                for i in range(N):
                    y[pi[i]] = rel[i][x[i]]
                P[x] = tuple(y)
            maps.add(tuple(sorted(P.items())))
    return maps


# ---------------------------------------------------------------- R1, R2
C3 = confs(3)
single3 = [(lab, op) for lab, op in UNITS[3] if len(lab[0]) == 1]
passing = set()
top_all = True
for img in itertools.permutations(C3):
    P = dict(zip(C3, img))
    if all(is_stage_unit(conj_perm(op, P), 3) for _, op in single3) and r_lit(P, 3):
        passing.add(tuple(sorted(P.items())))
    if top_all and not all(is_top_unit(conj_perm(op, P), 3) for _, op in TOP[3]):
        top_all = False
SPR3 = spr(3)
check('R1 ring of 3: (R-lit) holds for exactly the %d site permutations with relabelings' % len(SPR3),
      passing == SPR3 and len(SPR3) == 48, '%d of 40320 pass' % len(passing))
check('R2 ring of 3: NOTES-E9 H-DYN (top stage) holds for all 40320 configuration permutations', top_all)

# ---------------------------------------------------------------- R3
SPR4 = spr(4)
ok3 = len(SPR4) == 384 and len(UNITS[4]) == 624
for m in SPR4:
    if not r_lit(dict(m), 4):
        ok3 = False
        break
check('R3 ring of 4: all 384 site permutations with relabelings satisfy (R-lit) on all 624 units', ok3)


# ---------------------------------------------------------------- R4
def cnot(N):
    return {x: (x[0], (x[0] + x[1]) % 2) + x[2:] for x in confs(N)}


ok4 = True
detail4 = ''
for N in (3, 4):
    P = cnot(N)
    ok4 &= len(set(P.values())) == 2 ** N
    ok4 &= all(is_top_unit(conj_perm(op, P), N) for _, op in TOP[N])
    ok4 &= all(is_01(conj_perm(op, P)) for _, op in UNITS[N])
    img = conj_perm(unit(N, (0,), (0,), (1,)), P)
    flips = all(x[0] == 0 and xp[0] == 1 and x[1] != xp[1] and x[2:] == xp[2:] for (x, xp) in img)
    ok4 &= (not is_stage_unit(img, N)) and flips and not r_lit(P, N)
    detail4 += 'N=%d image of E^0_01 has %d pairs, each flipping site 1; ' % (N, len(img))
check('R4 CNOT: a permutation; (R-top) and (R-01) hold at every stage; (R-lit) fails at E^{0}_{0,1}', ok4, detail4)


# ---------------------------------------------------------------- R5
def shift2(N):
    return {x: tuple(x[(i - 2) % N] for i in range(N)) for x in confs(N)}


ok5 = True
for N in (3, 4):
    P = shift2(N)
    ok5 &= r_lit(P, N) and all(is_top_unit(conj_perm(op, P), N) for _, op in TOP[N])
    ok5 &= all(is_01(conj_perm(op, P)) for _, op in UNITS[N])
    for a, b in itertools.product(Q, Q):
        ok5 &= set(conj_perm(unit(N, (0,), (a,), (b,)), P)) == set(unit(N, (2,), (a,), (b,)))
check('R5 control T^2 on rings of 3 and 4: (R-lit), (R-top), (R-01); site 0 -> site 2', ok5)


# ---------------------------------------------------------------- R6
def xor3(N):
    return {x: tuple((x[i] + x[(i + 1) % N] + x[(i + 2) % N]) % 2 for i in range(N)) for x in confs(N)}


per = (1, 1, 0)
windows = [tuple(per[(i + k) % 3] for k in range(3)) for i in range(3)]
z_ok = all(sum(w) % 2 == 0 for w in windows) and per != (0, 0, 0)
n4, n3 = len(set(xor3(4).values())), len(set(xor3(3).values()))
check('R6 rule x_i+x_{i+1}+x_{i+2}: permutation on the ring of 4, not on the ring of 3; (110)^oo and 0^oo collide on Z',
      n4 == 16 and n3 == 2 and z_ok, 'images: ring 4 %d, ring 3 %d' % (n4, n3))


# ---------------------------------------------------------------- R7
def pair_graph(f):
    words = list(itertools.product(Q, repeat=2))
    V = [(u, v) for u in words for v in words]
    E = {vtx: [] for vtx in V}
    for (u, v) in V:
        for a, b in itertools.product(Q, Q):
            if f(u + (a,)) == f(v + (b,)):
                E[(u, v)].append((u[1:] + (a,), v[1:] + (b,)))
    return V, E


def sccs(V, E):
    index, low, onstack, stack, out = {}, {}, set(), [], []
    counter = [0]

    def strong(v):
        index[v] = low[v] = counter[0]
        counter[0] += 1
        stack.append(v)
        onstack.add(v)
        for w in E[v]:
            if w not in index:
                strong(w)
                low[v] = min(low[v], low[w])
            elif w in onstack:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack.discard(w)
                comp.append(w)
                if w == v:
                    break
            out.append(comp)

    for v in V:
        if v not in index:
            strong(v)
    return out


def nondiag_cycle(f):
    V, E = pair_graph(f)
    for comp in sccs(V, E):
        cyc = len(comp) > 1 or comp[0] in E[comp[0]]
        if cyc and any(u != v for (u, v) in comp):
            return True
    return False


xr = nondiag_cycle(lambda w: (w[0] + w[1] + w[2]) % 2)
sh = nondiag_cycle(lambda w: w[0])
check('R7 pair graphs: the rule of R6 has a cycle through a non-diagonal vertex; T^2 (window rule a) has none',
      xr and not sh)

# ---------------------------------------------------------------- countercontrols
P_cyc = {x: x for x in C3}
P_cyc[(0, 0, 0)], P_cyc[(0, 0, 1)], P_cyc[(0, 1, 0)] = (0, 0, 1), (0, 1, 0), (0, 0, 0)
xr1_holds = r_lit(P_cyc, 3)
print('COUNTER XR1 ' + ('DID NOT FAIL' if xr1_holds else 'fails as stated'), flush=True)
xr2_holds = all(is_01(conj_phase(op)) for _, op in UNITS[3])
bad = [lab for lab, op in UNITS[3] if not is_01(conj_phase(op))][:1]
print('COUNTER XR2 ' + ('DID NOT FAIL' if xr2_holds else 'fails as stated') + ' -- first unit with a phase: %s' % bad,
      flush=True)

failures = [n for n, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(failures)), flush=True)
if not failures and not xr1_holds and not xr2_holds:
    print('VERDICT E14-HDYN-READINGS-SEPARATED', flush=True)
else:
    print('VERDICT NOT RENDERED -- failing: %s' % failures, flush=True)
sys.exit(0)
