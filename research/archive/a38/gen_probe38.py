"""Assemble the A38 probe from act 37's probe head (verbatim, from D) and the A38 body; the frozen expectations are computed
here from the pre-freeze toolkit (lib38*) and embedded as literals."""
import json, os, pickle, sys
S = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, S)
p37 = open(os.path.join(S, 'probe37_landed.py'), encoding='utf-8').read()
body = open(os.path.join(S, 'probe38_body.py'), encoding='utf-8').read()
import importlib.util
spec = importlib.util.spec_from_file_location('build38', os.path.join(S, 'build38.py')); B38 = importlib.util.module_from_spec(spec); spec.loader.exec_module(B38)
from lib38c import *
E = pickle.load(open(os.path.join(S, 'witness1.pkl'), 'rb'))
WIT = json.load(open(os.path.join(S, 'witness38.json')))
deep = pickle.load(open(os.path.join(S, 'deep_wit.pkl'), 'rb'))
CLASSES = [[nm, m, n, [list(b) for b in cp], [list(r) for r in rows]] for nm, m, n, cp, rows in B38.CLASSES]
NAMES = [c[0] for c in CLASSES]
BYNAME = {NAMES9[s]: s for s in CENSUS9}
# expectations
nlev = sum(len(level_masks([E[i][k] - E[i2][k] for k in range(16)])) for i in range(16) for i2 in range(i + 1, 16))
nonid = []
for nm in NAMES:
    (m, n), cp, rows = BYNAME[nm]
    for tr in (False, True):
        nonid.append(sum(1 for x in conditions_E(E, m, n, cp, rows, tr) if x[2] != GEN_ONE))
T = defect_rows(SIG)
tdims = [256 - rank_int(T + struct_eqs(BYNAME[nm][0], BYNAME[nm][1], BYNAME[nm][2], False, False)) for nm in NAMES]
A_ = [[1 if ((i // 4) % 2 == 1 and i % 4 == 3 and (j // 4) % 2 == 1) else 0 for j in range(16)] for i in range(16)]
B_ = [[1 if (i // 4 == 2 and j % 4 == 1) else 0 for j in range(16)] for i in range(16)]
C_ = [[1 if (((i // 4) + i % 4) % 2 == 1 and j in (2, 8)) else 0 for j in range(16)] for i in range(16)]
def add(*Ms): return [[sum(M[i][j] for M in Ms) for j in range(16)] for i in range(16)]
def identical_in(M):
    return sorted((nm, 'row' if tr else 'column') for nm in NAMES for tr in (False, True) if all(x[2] == GEN_ONE for x in conditions_E(M, *BYNAME[nm][0], BYNAME[nm][1], BYNAME[nm][2], tr)))
pieces = {'A': A_, 'B': B_, 'C': C_, 'A+B': add(A_, B_), 'A+C': add(A_, C_), 'B+C': add(B_, C_), 'A+B+C': E}
PIECES = {k: (straight_line_direct(M), identical_in(M)) for k, M in pieces.items()}
assert PIECES['A+B+C'] == (True, []) and E == add(A_, B_, C_)
OKLINE = ("dita_local_escape_probe: OK -- along the arc H(u) = SIG o u^E through the certified stratum point, E = A + B + C the frozen "
          "exponent matrix: H(u) is a complex Hadamard matrix at every unit u; each of the eighteen census structures is admitted only at "
          "u = 1; at a generic u no index maps pass the proportionality test; the candidate exceptional set has forty points and the "
          "exhaustive search at each of them finds a Dita structure at u = 1 and u = -1 only, strictly and up to diagonal equivalence: "
          "for every unit u outside {1, -1}, H(u) admits no Dita structure of any shape, index map or orientation")
NULLSPACE = '''
def nullspace_int(rows):
    """an integer basis of the rational nullspace of the rows (fraction-free echelon form, then back-substitution)"""
    M = [r[:] for r in rows if any(r)]; m = len(M); n = 256; piv = []; r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if M[i][c] != 0: p = i; break
        if p is None: continue
        M[r], M[p] = M[p], M[r]; pv = M[r][c]
        for i in range(r + 1, m):
            if M[i][c] != 0:
                f = M[i][c]; M[i] = [pv * x - f * y for x, y in zip(M[i], M[r])]
                g = 0
                for x in M[i]:
                    if x: g = gcd(g, x)
                if g > 1: M[i] = [x // g for x in M[i]]
        piv.append(c); r += 1
        if r == m: break
    free = [c for c in range(n) if c not in piv]; out = []
    for fc in free:
        v = [Fr(0)] * n; v[fc] = Fr(1)
        for k in range(len(piv) - 1, -1, -1):
            row = M[k]; c = piv[k]
            s = sum((row[j] * v[j] for j in range(c + 1, n) if row[j] and v[j]), Fr(0))
            v[c] = -s / row[c]
        den = 1
        for x in v: den = den * x.denominator // gcd(den, x.denominator)
        out.append([int(x * den) for x in v])
    return out
'''
rep = {'@@E_TABLE@@': json.dumps(E), '@@NLEV@@': str(nlev), '@@CLASSES@@': json.dumps(CLASSES), '@@NONID@@': json.dumps(nonid),
       '@@WITNESSES@@': repr(dict(sorted(WIT.items()))), '@@E_CAND@@': json.dumps(deep['E_all'], ensure_ascii=False),
       '@@PIECES@@': repr(PIECES), '@@TDIMS@@': json.dumps(tdims), '@@OKLINE@@': repr(OKLINE)}
for k, v in rep.items():
    assert body.count(k) >= 1, k; body = body.replace(k, v)
assert '@@' not in body
body = body.replace("print('== 8. the tangent space", NULLSPACE + "\nprint('== 8. the tangent space", 1)
DOC = '''"""Track B act 38 -- the exact-computation probe of the local-escape round (frozen with the control plane).

Everything asserted is exact arithmetic: Gaussian rationals in Python integers and fractions for the numeric searches, an
exact monomial calculus for the symbolic ones, in which every entry of SIG o u^E is a monomial i^p z^q w^r u^k and every point
of the unit circle that the analysis singles out is named canonically as zeta z^s w^t, and exact integer ranks for the
tangent-space interpretation. The probe asserts the preregistered values and exits 1 on any mismatch; it certifies nothing on
its own beyond the arithmetic it replays. Its first part is act 37's probe head, verbatim: act 36's objects and exhaustive
structure search, act 36's stabilizer, and act 37's monomial calculus.

Objects (acts 24-38, numbers as in the landed Lean):
  F4(z)      (1/2) [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]           (scaled by 2 here)
  SIG        F4(z) ⊗ F4(w), z = (3+4i)/5, w = (5+12i)/13, index (a,b) -> 4a+b (scaled by 4: unimodular entries)
  E          A + B + C on the entry ((a,b),(c,d)): [a odd][b = 3][c odd] + [a = 2][d = 1] + [a+b odd][(c,d) in {(0,2),(2,0)}]
  H(u)       SIG o u^E, the witness arc; act 37's W and Pu(u) = SIG o u^W are kept in the head as the classifier's control
"""
'''
head = p37[p37.index('import itertools, json, sys, time'):p37.index("print('== 1. the census")]
text = DOC + head + body
open(os.path.join(S, 'dita_local_escape_probe.py'), 'w', encoding='utf-8').write(text)
print('probe written', len(text.encode()), 'bytes; nlev', nlev, 'nonid', nonid, 'tdims', tdims)
print('PIECES', PIECES)
