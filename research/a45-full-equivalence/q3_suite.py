"""A45 Q3 regression / countercontrol suite (research, not frozen; diagnostic, not load-bearing).

Run after the bridge lemma (TrackBQfbBridge.lean). Every expected cell is fixed in EXPECT below, before any carrier is
evaluated; the suite passes iff every measured cell equals its expected cell. Exact Gaussian-rational arithmetic.

Realizations (all flat unitaries scaled by 4, trivial ancilla): q1's R0..R4, plus
  R5 = i.SIG (global phase: the R_ph countercontrol) and R6 = SIG.D (right diagonal: in R_rd, not in R_ph).
Off-slice countercontrol X = 2.(F4(1) (x) I4) (unitary after scaling, different visible slice).

Carriers, act 14's four:
  O0  visible slice |H|^2/16                         expected: equal on every realization pair; separates X
  O1  AnchoredChannel rho -> H rho H^* on every
      matrix unit E_kl (spans all rho)               expected: equal exactly on the R_ph pair (R0, R5); separates
                                                     every other pair, including the two-sided pair (R0, R1) and the
                                                     right-diagonal pair (R0, R6)
  O2  RelativeCandidate, O3 ReanchoredChannel        expected: NOT APPLICABLE to a single static slice (no time pair);
                                                     on the constant lift U_t = U_s = H/4 the relative evolution is 1
                                                     for every realization (checked), so no pair is separated
Regressions of the bridge:
  B1  Q_fb rooted family (init uniform, read id), t <= 3   equal on every realization
  B2  B1 after monomial interventions M, N (perm x diag and scaled partial perm)   equal on every realization
  B3  row-non-monomial K = F4(i) (x) I4: |K H|^2       separates at least one pair (the Q2 dichotomy countercontrol)
"""
import itertools, json, random, sys, importlib.util, io, contextlib
spec = importlib.util.spec_from_file_location('q1', __file__.replace('q3_suite.py', 'q1_probe.py'))
q1 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    sys.argv = [sys.argv[0], '/dev/null']; spec.loader.exec_module(q1)
G, ZERO, ONE, I_, Fr = q1.G, q1.ZERO, q1.ONE, q1.I_, q1.Fr
N16 = range(16)
def mm(A, B): return [[sum((A[i][k] * B[k][j] for k in N16), ZERO) for j in N16] for i in N16]
def ct(A): return [[A[j][i].conj() for j in N16] for i in N16]
rng = random.Random(4503)
units = [G(Fr(3, 5), Fr(4, 5)), G(Fr(5, 13), Fr(12, 13)), I_, G(-1), ONE]
SIG = q1.SIG
Dr = [rng.choice(units) for _ in N16]
REAL = dict(q1.REAL)
REAL['R5 i.SIG'] = [[I_ * x for x in r] for r in SIG]
REAL['R6 SIG.D'] = [[SIG[i][j] * Dr[j] for j in N16] for i in N16]
names = list(REAL)
pairs = list(itertools.combinations(names, 2))
F41 = q1.F4(ONE)
X = [[F41[i // 4][j // 4] * G(2) if i % 4 == j % 4 else ZERO for j in N16] for i in N16]   # 4 * (F4(1)/2 (x) I4)

# ---- expectations, fixed before evaluation ----------------------------------------------------------------------
RPH = {('R0 SIG', 'R5 i.SIG')}
EXPECT = {
    'O0 equal on pair': {p: True for p in pairs},
    'O0 separates off-slice X': True,
    'O1 equal on pair': {p: (p in RPH) for p in pairs},
    'O2/O3 applicable to a single slice': False,
    'O2/O3 constant-lift relative evolution is 1 on every realization': True,
    'B1 rooted equal on pair': {p: True for p in pairs},
    'B2 rooted after monomial M, N equal on pair': {p: True for p in pairs},
    'B3 row-non-monomial K separates some pair': True,
    'all realizations flat unitary': True,
    'X unitary after scaling, different slice': True,
}

# ---- carriers -----------------------------------------------------------------------------------------------------
def O0(H): return tuple(tuple(x.n2() / 16 for x in r) for r in H)
def O1(H):   # H E_kl H^* = h_k h_l^*  (columns), over all (k, l): determines H up to one global phase
    return tuple(tuple(tuple(H[i][k] * H[i2][l].conj() for i2 in N16) for i in N16) for k in N16 for l in N16)
def rooted(H, T=3):
    Bm = [[H[b2][b].n2() / 16 for b2 in N16] for b in N16]
    P = [[Fr(int(i == j)) for j in N16] for i in N16]; out = []
    for _ in range(T + 1):
        out.append(tuple(tuple(r) for r in P)); P = [[sum(P[i][k] * Bm[k][j] for k in N16) for j in N16] for i in N16]
    return tuple(out)   # init uniform and read = id: rooted t a j = bornPow t a j
def perm_diag():
    p = list(N16); rng.shuffle(p); d = [rng.choice(units) for _ in N16]
    return [[d[i] if p[i] == j else ZERO for j in N16] for i in N16]
def scaled_partial_perm():
    p = list(N16); rng.shuffle(p); keep = set(rng.sample(list(N16), 11)); c = rng.choice(units)
    return [[c if (p[i] == j and i in keep) else ZERO for j in N16] for i in N16]
def is_monomial(M): return all(sum(1 for x in r if x != ZERO) <= 1 for r in M) and all(sum(1 for r in M if r[j] != ZERO) <= 1 for j in N16)

M = {}
M['all realizations flat unitary'] = all(q1.flat_unitary(H) for H in REAL.values())
XXh = mm(X, ct(X))
M['X unitary after scaling, different slice'] = all(XXh[i][j] == (G(16) if i == j else ZERO) for i in N16 for j in N16) and O0(X) != O0(SIG)
o0 = {nm: O0(H) for nm, H in REAL.items()}
M['O0 equal on pair'] = {p: o0[p[0]] == o0[p[1]] for p in pairs}
M['O0 separates off-slice X'] = O0(X) != o0[names[0]]
o1 = {nm: O1(H) for nm, H in REAL.items()}
M['O1 equal on pair'] = {p: o1[p[0]] == o1[p[1]] for p in pairs}
M['O2/O3 applicable to a single slice'] = False   # definitional: both take a time pair (s, t) of a lift; a static slice has one time
M['O2/O3 constant-lift relative evolution is 1 on every realization'] = all(
    all(x == (G(16) if i == j else ZERO) for i, r in enumerate(mm(H, ct(H))) for j, x in enumerate(r)) for H in REAL.values())
rt = {nm: rooted(H) for nm, H in REAL.items()}
M['B1 rooted equal on pair'] = {p: rt[p[0]] == rt[p[1]] for p in pairs}
MN = [(perm_diag(), perm_diag()), (scaled_partial_perm(), scaled_partial_perm()), (perm_diag(), scaled_partial_perm())]
assert all(is_monomial(a) and is_monomial(b) for a, b in MN)
rtMN = {nm: tuple(rooted(mm(mm(a, H), b)) for a, b in MN) for nm, H in REAL.items()}
M['B2 rooted after monomial M, N equal on pair'] = {p: rtMN[p[0]] == rtMN[p[1]] for p in pairs}
F4i = q1.F4(I_)
K = [[F4i[i // 4][j // 4] if i % 4 == j % 4 else ZERO for j in N16] for i in N16]
assert not is_monomial(K)
kh = {nm: O0(mm(K, H)) for nm, H in REAL.items()}
M['B3 row-non-monomial K separates some pair'] = any(kh[a] != kh[b] for a, b in pairs)

# ---- verdict ------------------------------------------------------------------------------------------------------
def key(k): return k if isinstance(k, str) else ' | '.join(k)
report, ok = {}, True
for cell, exp in EXPECT.items():
    got = M[cell]
    if isinstance(exp, dict):
        bad = [key(p) for p in exp if exp[p] != got[p]]
        report[cell] = {'expected': {key(p): v for p, v in exp.items()}, 'measured': {key(p): v for p, v in got.items()}, 'mismatches': bad}
        match = not bad
        print('%-68s %s  (%d pairs; equal on %d)' % (cell, 'MATCH' if match else 'MISMATCH ' + str(bad), len(exp), sum(got.values())))
    else:
        report[cell] = {'expected': exp, 'measured': got}
        match = exp == got
        print('%-68s %s  (expected %s, measured %s)' % (cell, 'MATCH' if match else 'MISMATCH', exp, got))
    ok &= match
print('Q3 SUITE: ALL CELLS MATCH' if ok else 'Q3 SUITE: A CELL MISMATCHES')
json.dump({'cells': report, 'all_match': ok}, open('q3_suite.json', 'w'), indent=1, sort_keys=True)
