#!/usr/bin/env python3
"""S2 / node S2.2: finite rank of a data-generated pair completion.  Exact arithmetic only (Fractions, integers).

Run:  cd pt/S2 && python3 -I -B s2_4_rank.py ../base/verification/lean-mathlib/OIBridge

Models.
 * Clock model (infinite-order gate with the certified product action): carrier V = finitely supported sums
   sum_k w_k (x) delta_k (w_k in W 3, k in Z); product preparations p (x) delta_0; gate N(w (x) delta_k) = c_k(w) (x)
   delta_{k+1}, c_k = cnot if k in S else id, S = {perfect squares} (0 in S, so N(p (x) delta_0) has table cnot p);
   product tests read sum_k w_k; tests = product tests preceded by N^m.  Preparation N^n p has table
   cnot^{sigma(n)} p, sigma(j) = #(S cap [0, j)) mod 2, and the protocol entry (n, m) is v(sigma(n + m)).
   Periodic countercontrol: S_per = {k : k = 0 mod 3}.
 * Compact padded model: preparations = products (axis list) and q_J = (E00, 2^-J e_J) (J >= 1); labels = product
   labels and reveal labels r_J(w, h) = w_00/2 + h_J/2.
 * The involutive model N_inv and the register model N_reg of s2_3_lt.py (re-built here) for the rank of a
   locally tomographic and of a finite-group non-LT completion.

DECISION RULES (fixed before the first run):
 K0 Transcription: pc/pt parsed; cnot involution; cnot pxz = phiW.  Failure: ABORT.
 K1 Clock model: all protocol values lie in [0, 1] (tables p or cnot p only, axis product effects); the exact rank of
    the L x L protocol matrix (n, m < L) for L = 8, 16, 32, 48, 64 is printed and must be strictly increasing; the run
    lengths of sigma up to j = 400 are 1, 3, 5, 7, ... (exact) -- with the written pigeonhole step this gives infinite
    rank; an exact LT-failure witness: preparations N^0 p and N^2 p have equal tables and differ at a test N^m.
    Countercontrol: with S_per the rank must stay bounded (rank at L = 64 equal to rank at L = 16).
 K2 Compact model: for L = 4, 8, 16 the prepVec matrix of {products, q_1..q_L} has rank (rank of products) + L; the
    sup-distance between prepVec(q_J) and prepVec(prodState 0 0) is exactly 2^-(J+1); all values in [0, 1].
    Countercontrol: removing the reveal labels drops the rank back to the product rank.
 K3 LT => finite rank instance: the generated label matrix of N_inv (tests up to N^1, axis data) has rank <= 16.
    Finite group => finite rank instance: the generated label matrix of N_reg (tests up to N^3) has rank <= 32 and
    > 16 (so finite rank does not give LT).
 VERDICT lines print only if K0-K3 pass and the countercontrols fail as required.
"""
import sys, os, re
from fractions import Fraction as Fr

OK = True
NPASS = 0
def check(name, cond, detail=""):
    global OK, NPASS
    if cond:
        NPASS += 1; print(f"PASS {name}" + (f"  [{detail}]" if detail else ""))
    else:
        OK = False; print(f"FAIL {name}" + (f"  [{detail}]" if detail else ""))
def control(name, should_fail_cond, detail=""):
    global OK, NPASS
    if not should_fail_cond:
        NPASS += 1; print(f"PASS countercontrol {name} fails as required" + (f"  [{detail}]" if detail else ""))
    else:
        OK = False; print(f"FAIL countercontrol {name} did not fail" + (f"  [{detail}]" if detail else ""))

IDX = [(m, n) for m in range(4) for n in range(4)]
def k(m, n): return 4 * m + n
def mmul(A, B):
    return [[sum(A[i][r] * B[r][j] for r in range(len(B)) if A[i][r] != 0) for j in range(len(B[0]))] for i in range(len(A))]
def mvec(A, v):
    return [sum(A[i][r] * v[r] for r in range(len(v)) if A[i][r] != 0) for i in range(len(A))]
def eye(n): return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
def hom(x): return (1, x[0], x[1], x[2])
def prodState(x, y):
    hx, hy = hom(x), hom(y); return [hx[m] * hy[n] for (m, n) in IDX]
def pairVal(a, b, w): return sum(a[m] * w[k(m, n)] * b[n] for (m, n) in IDX)
def sharp(b): return (Fr(1, 2), Fr(b[0], 2), Fr(b[1], 2), Fr(b[2], 2))
UNIT = (1, 0, 0, 0)
def frank(rows):
    M = [[Fr(x) for x in r] for r in rows]
    if not M: return 0
    rk = 0; ncol = len(M[0])
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        pr = M[rk]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c] / pr[c]
                M[i] = [M[i][j] - f * pr[j] for j in range(ncol)]
        rk += 1
    return rk

# ---------------------------------------------------------------- K0
oib = sys.argv[1] if len(sys.argv) > 1 else "../base/verification/lean-mathlib/OIBridge"
src = open(os.path.join(oib, "CompositeDimension.lean"), encoding="utf-8").read()
PC = [[0, 0, 3, 3], [1, 1, 2, 2], [2, 2, 1, 1], [3, 3, 0, 0]]
PT = [[0, 1, 2, 3], [1, 0, 3, 2], [1, 0, 3, 2], [0, 1, 2, 3]]
def SGN(m, n): return -1 if ((m == 1 and n == 3) or (m == 2 and n == 2)) else 1
def parse_table(name):
    body = re.search(r"def " + name + r" : Fin 4 → Fin 4 → Fin 4\n(.*?)\n\n", src, re.S).group(1)
    T = [[None] * 4 for _ in range(4)]
    for a, b, c in re.findall(r"\|\s*(\d),\s*(\d)\s*=>\s*(\d)", body):
        T[int(a)][int(b)] = int(c)
    return T
check("K0.pc/pt transcription", parse_table("pc") == PC and parse_table("pt") == PT)
CNOT = [[0] * 16 for _ in range(16)]
for (m, n) in IDX:
    CNOT[k(m, n)][k(PC[m][n], PT[m][n])] = SGN(m, n)
check("K0.cnot involution", mmul(CNOT, CNOT) == eye(16))
xplus, z3 = (1, 0, 0), (0, 0, 1)
phiW = [(1 if m != 2 else -1) if m == n else 0 for (m, n) in IDX]
pxz = prodState(xplus, z3)
check("K0.cnot pxz = phiW", mvec(CNOT, pxz) == phiW)
if not OK:
    print("ABORT"); sys.exit(1)

AX = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
EFFS = [(sharp(e), sharp(f)) for e in AX for f in AX] + [(UNIT, UNIT)]

# ---------------------------------------------------------------- K1 clock model
def sigma_seq(inS, J):
    out, cnt = [], 0
    for j in range(J):
        out.append(cnt % 2)
        if inS(j): cnt += 1
    return out
from math import isqrt
def is_sq(j): return isqrt(j) ** 2 == j
JMAX = 400
sig = sigma_seq(is_sq, JMAX + 1)
v0 = pairVal(sharp(xplus), sharp(z3), pxz)
v1 = pairVal(sharp(xplus), sharp(z3), phiW)
check("K1.distinguishing product effect: v0 != v1", v0 != v1, f"v0={v0}, v1={v1}")
tabs = [pxz, phiW]
allvals = all(0 <= pairVal(e, f, tabs[b]) <= 1 for b in (0, 1) for (e, f) in EFFS)
check("K1.every clock table (p or cnot p) has all axis product values in [0,1]", allvals)
ranks = []
for L in (8, 16, 32, 48, 64):
    M = [[(v1 if sig[n + m] else v0) for m in range(L)] for n in range(L)]
    ranks.append(frank(M))
print(f"INFO clock protocol ranks at L = 8,16,32,48,64: {ranks}")
check("K1.clock ranks strictly increasing", all(ranks[i] < ranks[i + 1] for i in range(len(ranks) - 1)))
runs, cur, ln = [], sig[1], 0
for j in range(1, JMAX + 1):
    if sig[j] == cur: ln += 1
    else:
        runs.append(ln); cur = sig[j]; ln = 1
runs_ok = runs[:15] == [2 * i + 1 for i in range(15)]
check("K1.sigma run lengths are 1,3,5,... (first 15 runs, exact)", runs_ok, f"{runs[:15]}")
# LT failure witness: N^0 p and N^2 p have table p (sigma(0) = sigma(2) = 0); find m with sigma(m) != sigma(2+m)
wit = next((m for m in range(50) if sig[m] != sig[2 + m]), None)
check("K1.LT failure: equal tables at n=0,2 and a separating test N^m", sig[0] == sig[2] == 0 and wit is not None,
      f"m={wit}")
sig_per = sigma_seq(lambda j: j % 3 == 0, JMAX + 1)
rp = []
for L in (16, 64):
    M = [[(v1 if sig_per[n + m] else v0) for m in range(L)] for n in range(L)]
    rp.append(frank(M))
control("K1.periodic clock rank grows from L=16 to L=64", rp[1] != rp[0], f"ranks {rp}")

# ---------------------------------------------------------------- K2 compact padded model
PRODS = [prodState(x, y) for x in AX + [(0, 0, 0)] for y in AX + [(0, 0, 0)]]
prod_rank = frank([[pairVal(e, f, p) for (e, f) in EFFS] for p in PRODS])
k2ok = True; distok = True; valok = True; ccok = True
for L in (4, 8, 16):
    rows = []
    for p in PRODS:
        rows.append([pairVal(e, f, p) for (e, f) in EFFS] + [Fr(1, 2)] * L)
    E00 = prodState((0, 0, 0), (0, 0, 0))
    base = [pairVal(e, f, E00) for (e, f) in EFFS]
    qrows = []
    for J in range(1, L + 1):
        r = base + [Fr(1, 2) + (Fr(1, 2 ** (J + 1)) if JJ == J else 0) for JJ in range(1, L + 1)]
        qrows.append(r)
        d = max(abs(r[i] - (base + [Fr(1, 2)] * L)[i]) for i in range(len(r)))
        if d != Fr(1, 2 ** (J + 1)): distok = False
    allrows = rows + qrows
    if any(not (0 <= x <= 1) for r in allrows for x in r): valok = False
    rk = frank(allrows)
    if rk != prod_rank + L: k2ok = False
    rk_noreveal = frank([r[:len(EFFS)] for r in allrows])
    if rk_noreveal != prod_rank: ccok = False
print(f"INFO compact model: product rank {prod_rank}")
check("K2.rank = product rank + L for L = 4, 8, 16", k2ok)
check("K2.sup-distance prepVec(q_J) to prepVec(E00) = 2^-(J+1)", distok)
check("K2.all values in [0,1]", valok)
control("K2.rank without reveal labels exceeds the product rank", not ccok)

# ---------------------------------------------------------------- K3 instances
def block(A, B, C, D):
    n1, n2 = len(A), len(D)
    M = [[0] * (n1 + n2) for _ in range(n1 + n2)]
    for i in range(n1):
        for j in range(n1): M[i][j] = A[i][j]
        for j in range(n2): M[i][n1 + j] = B[i][j]
    for i in range(n2):
        for j in range(n1): M[n1 + i][j] = C[i][j]
        for j in range(n2): M[n1 + i][n1 + j] = D[i][j]
    return M
delta = [0] * 16; delta[k(0, 3)] = 1; delta[k(3, 3)] = 1
Cinv = [[0] * 16 for _ in range(2)]; Cinv[0][k(1, 0)] = 1; Cinv[0][k(1, 1)] = 1
Ninv = block(CNOT, [[0, delta[i]] for i in range(16)], Cinv, [[-1, 0], [0, -1]])
PR = [prodState(x, y) for x in AX for y in AX]
def label_matrix(N, nh, maxw, maxt):
    rows = []
    for p in PR:
        s = list(p) + [0] * nh
        for _ in range(maxw + 1):
            row = []
            for t in range(maxt + 1):
                u = list(s)
                for _ in range(t): u = mvec(N, u)
                row += [pairVal(e, f, u[:16]) for (e, f) in EFFS]
            rows.append(row)
            s = mvec(N, s)
    return rows
r_inv = frank(label_matrix(Ninv, 2, 1, 1))
check("K3.LT model: generated label matrix rank <= 16", r_inv <= 16, f"rank {r_inv}")
I16 = eye(16)
Nreg = block(CNOT, [[I16[i][j] - CNOT[i][j] for j in range(16)] for i in range(16)], CNOT,
             [[-CNOT[i][j] for j in range(16)] for i in range(16)])
r_reg = frank(label_matrix(Nreg, 16, 3, 3))
check("K3.register model: 16 < rank <= 32 (finite rank, not LT)", 16 < r_reg <= 32, f"rank {r_reg}")

print(f"SUMMARY checks passed={NPASS} all_ok={OK}")
if OK:
    print(f"VERDICT CLOCK: a reversible gate with the certified product action, test generation and valid tables, but "
          f"of infinite order, gives protocol ranks {ranks} (strictly increasing); with the written pigeonhole step "
          "(finite Hankel rank => eventually periodic sigma) the pair completion has infinite rank, and it is not LT")
    print("VERDICT COMPACT: a compact completion of infinite rank exists (exact finite sections); compactness does not "
          "give finite rank (it suffices for closedness of the read-out cone, written)")
    print(f"VERDICT GROUP: finite operation group => finite rank (register model rank {r_reg}, not LT); LT => rank <= 16 "
          f"(involutive model rank {r_inv})")
else:
    print("NO VERDICT")
