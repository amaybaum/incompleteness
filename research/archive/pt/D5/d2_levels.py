# d2_levels.py -- thread D5, stage 5: the matrix-level level-lifting identity behind node N1c.
# Run: python3 -I -B d2_levels.py from pt/D5/.  Exact (sympy; c is a symbol standing for exp(i pi t)).
#
# Kernel definitions transcribed (L = 9f9f8257):
#   gateFlow g t = unit (permMat g) t                                  (LiftAudit.lean:47-48)
#   unit g t = 1 + (exp(pi i t) - 1) * proj g,  proj g = (1/2)(1 - g)  (SecondOrderCircuit.lean:352-357)
#   permMat s x y = if s y = x then 1 else 0                           (SecondOrderCircuit.lean:710-711)
#   levelPerm s n = s x id_(Fin n)                                     (LiftAudit.lean:51-52)
#   tensorOf A B p q = A p.1 q.1 * B p.2 q.2 ; reindex e e M x y = M (e^-1 x) (e^-1 y)  (Mathlib)
#   withSpectator R e (conjChannel V) = conjChannel (reindex e e (1_R (x) V))  (ReferenceSufficiency.lean:754)
# Claim tested: with e_n : Fin n x (S x Fin 1) -> S x Fin n, (r,(s,0)) |-> (s,r),
#   reindex e_n e_n (1_n (x) gateFlow(levelPerm s 1) t) = gateFlow(levelPerm s n) t.
#
# DECISION RULES (fixed before the first run): every line prints PASS/FAIL; countercontrols (ids ending 'c')
# PASS when the tested identity FAILS on them.  VERDICT only if every line is PASS, else NO VERDICT.
#   L1  the identity holds exactly (polynomial in c) for S = Fin 2 (s = swap 0 1) and S = Fin 3 (s = swap 0 1,
#       a fixed point present), every n in {1, 2, 3}.
#   L1c the identity must FAIL for the wrong reindexing e'(r,(s,0)) = (r,s) (spectator put in the system
#       slot) at S = Fin 2, n = 2, and for the non-involution-respecting choice "flow of s on the ancilla".
#   L2  sanity: at c = 1 the flow is the identity; at c = -1 it is permMat(levelPerm s n) (gateFlow_one).
#   L3  unitarity at |c| = 1: with c = (1-u^2+2iu)/(1+u^2), G G^dag = 1 exactly, every instance.
import itertools
from sympy import Matrix, symbols, I, simplify, expand, eye, zeros, Rational as Q
lines = []
def rep(ok, cid, msg=''):
    lines.append(('PASS' if ok else 'FAIL') + ' ' + cid + ((' ' + msg) if msg else ''))
    print(lines[-1])
c = symbols('c'); u = symbols('u', real=True)
def permMat(perm, idx):
    n = len(idx); M = zeros(n, n)
    for j, y in enumerate(idx):
        M[idx.index(perm(y)), j] = 1          # entry (x, y) = 1 iff perm y = x
    return M
def unit(P):
    return eye(P.shape[0]) + (c - 1) * (eye(P.shape[0]) - P) / 2
def levelIdx(Sn, n):
    return [(s, k) for s in range(Sn) for k in range(n)]
def levelPerm(sig, n):
    return lambda p: (sig(p[0]), p[1])
def gateFlowLevel(Sn, sig, n):
    idx = levelIdx(Sn, n)
    return unit(permMat(levelPerm(sig, n), idx)), idx
def tensor_one(n, B, idxB):
    idx = [(r, x) for r in range(n) for x in idxB]
    M = zeros(len(idx), len(idx))
    for i, (r, x) in enumerate(idx):
        for j, (r2, y) in enumerate(idx):
            if r == r2:
                M[i, j] = B[idxB.index(x), idxB.index(y)]
    return M, idx
def reindex(M, idxFrom, e, idxTo):
    # (reindex e e M) x y = M (e^-1 x) (e^-1 y)
    inv = {e(p): p for p in idxFrom}
    N = zeros(len(idxTo), len(idxTo))
    for i, x in enumerate(idxTo):
        for j, y in enumerate(idxTo):
            N[i, j] = M[idxFrom.index(inv[x]), idxFrom.index(inv[y])]
    return N
def clean(M):
    return M.applyfunc(lambda z: simplify(expand(z)))
cases = []
for Sn in (2, 3):
    sig = lambda s: {0: 1, 1: 0}.get(s, s)
    for n in (1, 2, 3):
        G1, idx1 = gateFlowLevel(Sn, sig, 1)
        Gn, idxn = gateFlowLevel(Sn, sig, n)
        T, idxT = tensor_one(n, G1, idx1)
        e = lambda p: (p[1][0], p[0])                 # (r,(s,0)) |-> (s,r)
        R = reindex(T, idxT, e, idxn)
        cases.append((Sn, n, clean(R - Gn) == zeros(len(idxn), len(idxn))))
rep(all(ok for _, _, ok in cases), 'L1', 'reindex e_n (1_n x gateFlow(levelPerm s 1) t) = gateFlow(levelPerm s n) t for %s'
    % [(Sn, n) for Sn, n, _ in cases])
sig = lambda s: {0: 1, 1: 0}.get(s, s)
G1, idx1 = gateFlowLevel(2, sig, 1); G2, idx2 = gateFlowLevel(2, sig, 2)
T, idxT = tensor_one(2, G1, idx1)
ebad = lambda p: (p[0], p[1][0])                    # spectator index put in the system slot
Rbad = reindex(T, idxT, ebad, idx2)
rep(clean(Rbad - G2) != zeros(4, 4), 'L1c', 'wrong reindexing (spectator in the system slot) does not give the level-2 flow')
anc = unit(permMat(lambda p: (p[0], 1 - p[1]), idx2))   # the flow of the swap acting on the ancilla instead
rep(clean(anc - G2) != zeros(4, 4), 'L1c2', 'the flow of the same swap on the ancilla is a different operator')
ok2 = True; ok3 = True
cu = (1 - u ** 2 + 2 * I * u) / (1 + u ** 2)
for Sn in (2, 3):
    for n in (1, 2, 3):
        Gn, idxn = gateFlowLevel(Sn, sig, n)
        P = permMat(levelPerm(sig, n), idxn)
        if clean(Gn.subs(c, 1) - eye(len(idxn))) != zeros(len(idxn), len(idxn)): ok2 = False
        if clean(Gn.subs(c, -1) - P) != zeros(len(idxn), len(idxn)): ok2 = False
        Gu = Gn.subs(c, cu)
        if clean(Gu * Gu.H - eye(len(idxn))) != zeros(len(idxn), len(idxn)): ok3 = False
rep(ok2, 'L2', 'c = 1 gives the identity; c = -1 gives permMat(levelPerm s n) (gateFlow_one), all instances')
rep(ok3, 'L3', 'unitary for |c| = 1 (rational parametrization), all instances')
nf = sum(1 for l in lines if l.startswith('FAIL'))
print('SUMMARY %d lines, %d FAIL' % (len(lines), nf))
print('VERDICT D2-LEVELS-EXACT: the level-n layer flow is the reindexed spectator extension of the level-1 flow'
      if nf == 0 else 'NO VERDICT')
