# Compression check for PREMISE-MEMO.md §2 ("Exact witness"): the six configuration 2-subset compressions of the
# K(Z_F) defects. A verification written from the memo's definitions and the construction in dc_premise.py; it does
# not import or read dc_premise.py and is not a probe of any screen. Exact rational arithmetic only: Python's
# fractions.Fraction, no SymPy, no eigenvalues, no floating point and no tolerance.
#
# Objects:
#   |ij> = |i>(x)|j>, token 1 first, basis index 2i+j; the configurations are 00, 01, 10, 11.
#   Defects z = I/2 - P_m, m = (|00> + b|01> - bd|10> + d|11>)/2, b, d = +-1 (as in dc_premise.py). m is real, so z
#   is a real symmetric matrix with rational entries.
#   The compression of z to a 2-subset S = {a, b} of configurations is the principal submatrix z[S, S], the matrix of
#   z on span{|a>, |b>}. There are six subsets: {00,11} and {01,10} are the parity blocks read by the native UPD
#   conditionals; the other four are product subsets.
#   A real symmetric 2x2 matrix is PSD iff all its principal minors are >= 0: both diagonal entries and the determinant.
#
# Claim checked (memo §2, the witness bullet): E1  all six compressions are PSD for each of the four defects (24 cases).
# Decision rule: E1 HOLDS iff every principal minor of every one of the 24 compressions is >= 0. The verdict is printed
# only if every control K1-K5 passes, otherwise VOID. Exit status 0 iff every control and claim line is PASS.
import sys
from fractions import Fraction as Fr
from itertools import combinations

res = []
def ok(name, c):
    c = bool(c); res.append(c); print(("PASS " if c else "FAIL ") + name); return c

CONF = ("00", "01", "10", "11")
DEFECTS = [(b, d) for b in (1, -1) for d in (1, -1)]
SUBSETS = list(combinations(range(4), 2))
HALF = Fr(1, 2)

def mvec(b, d): return [HALF, Fr(b, 2), Fr(-b * d, 2), Fr(d, 2)]
def outer(u): return [[u[r] * u[s] for s in range(4)] for r in range(4)]
def matmul(A, B): return [[sum(A[r][t] * B[t][s] for t in range(4)) for s in range(4)] for r in range(4)]
def defect(b, d, c=Fr(1)):      # c = 1: the defect I/2 - P_m; other c: the perturbation I/2 - c P_m
    P = outer(mvec(b, d)); return [[(HALF if r == s else Fr(0)) - c * P[r][s] for s in range(4)] for r in range(4)]
def compress(Z, S): return [[Z[r][s] for s in S] for r in S]
def wrong_map(Z, S): return [[Z[r][s] for s in reversed(S)] for r in S]   # not a principal submatrix
def exact(M): return all(type(x) is Fr for row in M for x in row)
def minors(M): return (M[0][0], M[1][1], M[0][0] * M[1][1] - M[0][1] * M[1][0])
def psd2(M):
    if not exact(M): raise SystemExit("non-rational entry: %r" % (M,))
    return M[0][1] == M[1][0] and all(x >= 0 for x in minors(M))
def label(S): return "{%s,%s}" % (CONF[S[0]], CONF[S[1]])
def kind(S): return "parity" if S in ((0, 3), (1, 2)) else "product"

print("# controls")
# K1 the objects are the memo's: m real unit vector, maximally entangled (2 C^T C = I for C_ij = <ij|m>), P_m a
#    projector, z symmetric with Tr(P_m z) = -1/2 (z is not PSD: the defect lies outside Q3)
def k1(b, d):
    m = mvec(b, d); P = outer(m); z = defect(b, d)
    C = [[m[2 * i + j] for j in range(2)] for i in range(2)]
    ctc = [[2 * sum(C[t][i] * C[t][j] for t in range(2)) for j in range(2)] for i in range(2)]
    return (sum(x * x for x in m) == 1 and ctc == [[1, 0], [0, 1]] and matmul(P, P) == P
            and all(z[r][s] == z[s][r] for r in range(4) for s in range(4)) and exact(z)
            and sum(P[r][s] * z[s][r] for r in range(4) for s in range(4)) == -HALF)
ok("K1 objects: m unit and maximally entangled, P_m projector, z symmetric and exact, Tr(P_m z) = -1/2",
   all(k1(b, d) for b, d in DEFECTS))
# K2 the PSD predicate rejects non-PSD matrices, including one whose determinant is positive, and accepts PSD ones
# on the boundary
NEG = [[[HALF, Fr(1)], [Fr(1), HALF]], [[Fr(-1), Fr(0)], [Fr(0), Fr(-1)]], [[Fr(0), Fr(1)], [Fr(1), Fr(0)]],
       [[Fr(1), Fr(1, 3)], [Fr(1, 4), Fr(1)]]]
POS = [[[HALF, Fr(0)], [Fr(0), Fr(0)]], [[Fr(1, 4), Fr(1, 4)], [Fr(1, 4), Fr(1, 4)]]]
ok("K2 predicate: 4 non-PSD or non-symmetric matrices rejected (one with det > 0), 2 boundary PSD matrices accepted",
   not any(psd2(M) for M in NEG) and all(psd2(M) for M in POS))
# K3 countercontrol, perturbed defect: I/2 - (3/2) P_m is not PSD on any 2-subset, so every one of its 24
#    compressions must be rejected
pert = [(b, d, S) for b, d in DEFECTS for S in SUBSETS if psd2(compress(defect(b, d, Fr(3, 2)), S))]
ok("K3 countercontrol: perturbed defects I/2 - (3/2)P_m rejected in all 24 cases (accepted: %d)" % len(pert), not pert)
# K4 countercontrol, wrong subset map: rows S with columns in reversed order is not a compression; for each defect the
#    pipeline must reject it on at least one subset
rej = {(b, d): sum(1 for S in SUBSETS if not psd2(wrong_map(defect(b, d), S))) for b, d in DEFECTS}
ok("K4 countercontrol: wrong subset map rejected on at least one subset per defect (rejected per defect: %s)"
   % ", ".join("%d" % rej[k] for k in DEFECTS), all(v >= 1 for v in rej.values()))

# K5 coverage: the subsets are exactly the six 2-subsets of the four configurations, enumerated independently
ok("K5 coverage: the six 2-subsets of {00,01,10,11}, each once",
   sorted(SUBSETS) == [(a, c) for a in range(4) for c in range(4) if a < c] and len(set(SUBSETS)) == 6)

print("# compressions: b d subset kind | z_aa z_bb det | PSD")
allpsd = True; ncases = 0
for b, d in DEFECTS:
    z = defect(b, d)
    for S in SUBSETS:
        M = compress(z, S); p = psd2(M); allpsd &= p; ncases += 1
        print("b=%+d d=%+d %s %-7s | %s %s %s | %s" % (b, d, label(S), kind(S), *map(str, minors(M)), p))

print("# claims")
e1 = ok("E1 all six compressions PSD (all principal minors >= 0) for all four defects: %d of 24 cases" % ncases,
        allpsd and ncases == 24)

controls = res[:5]
print("TOTAL %d PASS %d FAIL" % (sum(res), len(res) - sum(res)))
if all(controls):
    print("VERDICT E1 %s" % ("HOLDS" if e1 else "FAILS"))
else:
    print("VERDICT VOID: a control failed")
sys.exit(0 if all(res) else 1)
