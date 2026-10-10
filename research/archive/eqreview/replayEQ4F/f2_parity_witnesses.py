"""EQ4-F exact witnesses for the cheap (aligned) parity lemma and its chart reduction (design only; base bcbc516f).

Own code: imports nothing from scratchpad/eq2, eq3, eqreview, nor from f1_package_identities.py.  Kernel tables are
typed by hand and re-parsed from the base text (transcription control).
Usage:  python3 -I -B f2_parity_witnesses.py <base>/verification/lean-mathlib/OIBridge

Conventions as in f1_package_identities.py: W 3 tables are 4 x 4 matrices (row = first token, index 0 = unit);
actT N w = w . homMap(N)^T, actC N w = homMap(N) . w; cnot' = actT reflY . cnot . actT reflY; pairs ordered
(01, 23, 02, 13); gate-supplied states S_t[k] = cnot^t(prodState(s_k xplus, u_k z3)) and effects
E_t[k] = cnot^t(sharpVec(s_k xplus) sharpVec(u_k z3)^T), (s_k, u_k) = (1,1), (1,-1), (-1,1), (-1,-1) for k = 0..3.

DECISION RULE (fixed before the first run; rules, not expected numbers):
  K  parsed sgn/pc/pt (CompositeDimension:741-755), phiW (CD:1220), reflY (K2Guard:46-47) equal the hand
     transcriptions, and cnot(prodState xplus z3) = phiW (CD:1222) reproduces.
  X1 a reflection chart at the FIRST token also turns cnot into cnot': actC reflY . cnot . actC reflY = cnot'
     (symbolic); countercontrol: the rotation chart nflip at the first token does not (nonzero symbolic difference).
  X2 per-token reflection charts realize every even pattern: for each tau in {0,1}^4 with even 4-cycle parity there is
     eps in {0,1}^4 (tokens 0..3) with tau_ij = eps_i + eps_j mod 2 on the four pairs, and for that eps the chart
     maps actC reflY^eps_i . actT reflY^eps_j . cnot^tau_ij . (same chart) equal cnot on every pair (symbolic);
     for odd tau no eps exists (exhaustive over the 16 eps).
  X3 explicit witnesses: for each odd tau the lexicographically first (iX, iY, iE, iF) in {0..3}^4 with
     <S_t01[iX], E_t02[iE] . S_t23[iY] . E_t13[iF]^T> < 0 (family (i)) exists, and likewise for family (ii)
     <E_t01[ie], S_t02[iL] . E_t23[if] . S_t13[iL']^T> < 0; for each even tau no negative value exists in either family
     (control).  The witnesses and values are printed.
VERDICT F2-PARITY-WITNESSES-EXACT iff every check passes; otherwise VERDICT NOT RENDERED.  Exact arithmetic only
(sympy symbols for identities; fractions.Fraction for values); no solver calls.
"""
import itertools
import re
import sys
from fractions import Fraction as Fr

import sympy as sp
from sympy import Matrix, Rational as R, eye

BASE = sys.argv[1]
CHECKS = []


def check(name, cond, detail=None):
    ok = bool(cond)
    CHECKS.append((name, ok))
    line = ("PASS " if ok else "FAIL ") + name
    if detail is not None:
        line += "  [" + str(detail) + "]"
    print(line)
    sys.stdout.flush()
    return ok


def Z(M):
    return M.applyfunc(sp.expand).is_zero_matrix


HAND_NEG = [(1, 3), (2, 2)]
HAND_PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
HAND_PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
cd = open(BASE + "/CompositeDimension.lean", encoding="utf-8").read()
k2 = open(BASE + "/K2Guard.lean", encoding="utf-8").read()
i_s = cd.index("def sgn (μ ν : Fin 4) : ℝ :=")
sgn_line = cd[i_s:cd.index("\n", i_s)]


def parse_idx_table(name):
    i = cd.index("def " + name + " : Fin 4 → Fin 4 → Fin 4")
    tab = [[None] * 4 for _ in range(4)]
    for m, n, v in re.findall(r"\|\s*(\d),\s*(\d)\s*=>\s*(\d)", cd[i:i + 400])[:16]:
        tab[int(m)][int(n)] = int(v)
    return tab


i_p = cd.index("def phiW : W 3 :=")
i_r = k2.index("def reflY : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) where")
refl_parsed = [int(v) for v in re.search(r"toFun x := fun i => \(!\[([-\d, ]+)\] : Fin 3 → ℝ\) i \* x i",
                                         k2[i_r:i_r + 300]).group(1).split(",")]
REFLY = sp.diag(1, -1, 1)
NFLIP = sp.diag(1, -1, -1)
DELTA = sp.diag(1, 1, -1, 1)


def sgn(m, n):
    return -1 if (m, n) in HAND_NEG else 1


def cnot(w):
    return Matrix(4, 4, lambda m, n: sgn(m, n) * w[HAND_PC[m][n], HAND_PT[m][n]])


def H(N):
    M = eye(4)
    M[1:, 1:] = Matrix(N)
    return M


def actT(N, w):
    return w * H(N).T


def actC(N, w):
    return H(N) * w


def prodState(x, y):
    return Matrix([1] + list(x)) * Matrix([1] + list(y)).T


def sharpVec(b):
    return Matrix([R(1, 2)] + [sp.S(v) / 2 for v in b])


def cnotp(w):
    return actT(REFLY, cnot(actT(REFLY, w)))


XPLUS, Z3 = [1, 0, 0], [0, 0, 1]
neg_parsed = sorted((int(a), int(b)) for a, b in re.findall(r"μ = (\d) ∧ ν = (\d)", sgn_line))
check("K transcription: sgn, pc, pt, phiW, reflY as transcribed; cnot(prodState xplus z3) = phiW (CD:1222)",
      neg_parsed == HAND_NEG and parse_idx_table("pc") == HAND_PC and parse_idx_table("pt") == HAND_PT
      and cd[i_p:cd.index("\n", i_p)].strip()
      == "def phiW : W 3 := fun μ ν => if μ = ν then (if μ = 2 then -1 else 1) else 0"
      and refl_parsed == [1, -1, 1] and cnot(prodState(XPLUS, Z3)) == DELTA)

w = Matrix(4, 4, lambda m, n: sp.Symbol("w%d%d" % (m, n), real=True))
check("X1 first-token reflection chart: actC reflY . cnot . actC reflY = cnot' (symbolic); countercontrol: with the "
      "rotation nflip in place of reflY the identity fails (symbolic)",
      Z(actC(REFLY, cnot(actC(REFLY, w))) - cnotp(w)) and not Z(actC(NFLIP, cnot(actC(NFLIP, w))) - cnotp(w)))

PAIRS = [(0, 1), (2, 3), (0, 2), (1, 3)]
GATES = {0: cnot, 1: cnotp}


def chart_pair(eps_i, eps_j, v):
    out = v
    if eps_j:
        out = actT(REFLY, out)
    if eps_i:
        out = actC(REFLY, out)
    return out


ok_x2, x2_log = True, []
for tau in itertools.product((0, 1), repeat=4):
    even = (tau[0] + tau[3] + tau[1] + tau[2]) % 2 == 0      # tau_01 + tau_13 + tau_23 + tau_02
    sols = [eps for eps in itertools.product((0, 1), repeat=4)
            if all((eps[i] + eps[j]) % 2 == tau[k] for k, (i, j) in enumerate(PAIRS))]
    if even:
        if not sols:
            ok_x2 = False
            continue
        eps = sols[0]
        for k, (i, j) in enumerate(PAIRS):
            conj = chart_pair(eps[i], eps[j], GATES[tau[k]](chart_pair(eps[i], eps[j], w)))
            ok_x2 &= Z(conj - cnot(w))
        x2_log.append("%d%d%d%d:eps=%d%d%d%d" % (tau + eps))
    else:
        ok_x2 &= (sols == [])
check("X2 every even pattern is a coboundary tau_ij = eps_i + eps_j and the per-token reflection chart eps conjugates "
      "every aligned gate cnot^tau_ij to cnot (symbolic); no eps exists for odd patterns  [" + " ".join(x2_log) + "]",
      ok_x2)

SIGNS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def to_fr(M):
    return [[Fr(int(sp.numer(M[i, j])), int(sp.denom(M[i, j]))) for j in range(4)] for i in range(4)]


def fmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def ftr(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def fip(A, B):
    return sum(A[i][j] * B[i][j] for i in range(4) for j in range(4))


ST = {t: [to_fr(GATES[t](prodState([s * v for v in XPLUS], [u * v for v in Z3]))) for s, u in SIGNS] for t in (0, 1)}
EF = {t: [to_fr(GATES[t](sharpVec([s * v for v in XPLUS]) * sharpVec([u * v for v in Z3]).T)) for s, u in SIGNS]
      for t in (0, 1)}
ok_x3, x3_log = True, []
for tau in itertools.product((0, 1), repeat=4):
    t01, t23, t02, t13 = tau
    odd = (t01 + t13 + t23 + t02) % 2 == 1
    w1 = next(((ix, iy, ie, jf, fip(ST[t01][ix], fmul(fmul(EF[t02][ie], ST[t23][iy]), ftr(EF[t13][jf]))))
               for ix, iy, ie, jf in itertools.product(range(4), repeat=4)
               if fip(ST[t01][ix], fmul(fmul(EF[t02][ie], ST[t23][iy]), ftr(EF[t13][jf]))) < 0), None)
    w2 = next(((ie, jf, il, jl, fip(EF[t01][ie], fmul(fmul(ST[t02][il], EF[t23][jf]), ftr(ST[t13][jl]))))
               for ie, jf, il, jl in itertools.product(range(4), repeat=4)
               if fip(EF[t01][ie], fmul(fmul(ST[t02][il], EF[t23][jf]), ftr(ST[t13][jl]))) < 0), None)
    if odd:
        ok_x3 &= (w1 is not None) and (w2 is not None)
        x3_log.append("%d%d%d%d:(i)X%dY%dE%dF%d=%s,(ii)e%df%dL%dL'%d=%s" % (tau + w1[:4] + (w1[4],) + w2[:4] + (w2[4],)))
    else:
        ok_x3 &= (w1 is None) and (w2 is None)
check("X3 explicit gate-supplied witnesses for every odd pattern in both families, none for even patterns  ["
      + " ".join(x3_log) + "]", ok_x3)

npass = sum(1 for _, c in CHECKS if c)
print("--- f2_parity_witnesses: %d/%d checks pass" % (npass, len(CHECKS)))
print("VERDICT F2-PARITY-WITNESSES-EXACT" if npass == len(CHECKS) else "VERDICT NOT RENDERED")
