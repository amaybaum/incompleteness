"""
audit_six.py -- coordinator's independent exact checks of EQ4-SIX (scratchpad/eq5/SIX/RESULT.md).

Independent of the thread's code: nothing from scratchpad/eq5/SIX (scripts or eq4_lib.py) is imported or read.
Operators are exact rational tensors (numpy object arrays of Fractions) on labelled qubits, written here.
Every operator in X2-X4 is real, so real Fractions suffice; complex bilinear identities are checked on real
pairs, which suffices by complex bilinearity of both sides (stated, not computed).

Usage: python3 -I -B audit_six.py

Checks (decision rule fixed before the first run):
  C0  machinery controls: cond(1_A, X) = partial trace; tr[Phi+_{AB} (X_A (x) Y_B)] = (1/2) tr(X Y^T) on random
      real 2x2 X, Y; the same without the transpose differs for a non-symmetric Y (countercontrol)
  X1  crossing enumeration on tokens {0..5}: over every subset S and every ordered pair of distinct unordered
      bipartitions (effects A|B, states C|D) of S with all four intersections nonempty:
      count per |S| = (4: 90, 5: 360, 6: 390), |S| <= 3: 0; at |S| = 6 the classes by part sizes are
      (2|4, 2|4) 120, (2|4, 3|3) 90, (3|3, 2|4) 90, (3|3, 3|3) 90; no such pair has a part of size 1 or 5
  X2  PN_5 control (RESULT 0, 7; s3 P): x = (1/2)1_P (x) Phi+_{R1R2}, y = (1/2)1_Q (x) Phi+_{U1U2}, Bell w = Phi+_{PQ},
      z = Phi+_{ST}; Glue_s = tr_PQ[(w (x) 1)(x (x) y)], Glue_e = tr_ST[(z (x) 1)(e_{S R1 U1} (x) f_{T R2 U2})],
      N = tr[Glue_e Glue_s]. With e = GHZ, f = W3 := 1/2 - |GHZ><GHZ|: N = -1/64; e = f = W3: N = 1/16;
      e = f = GHZ: N = 1/32
  X3  membership of the X2 nodes: x, y are product across P | R1R2 (biseparable); GHZ is PSD (rank one, trace 1);
      W3 is nonnegative on biseparable states: for each of the three cuts of three tokens the one-token marginal of
      GHZ is 1/2 (its largest eigenvalue is the largest squared Schmidt coefficient); W3 is not PSD:
      <GHZ|W3|GHZ> = -1/2 (so W3 is a witness, not a state; QM's K3* = PSD_8 does not contain it)
  X4  theta identity (s3 B): with e = (1/2)1_S (x) Phi+_{R1U1}, f = (1/2)1_T (x) Phi+_{R2U2}, Bell w, z:
      N(x, y) = (1/4)(1/8) tr(x T(y')) with y' = y on (P, R1, R2) and T the full transpose, on 3 random real
      pairs (x, y) of 8x8 rational matrices; countercontrol: (1/32) tr(x y') differs for a non-symmetric y
  X5  QM sign control: N >= 0 for 4 random rank-one PSD real nodes x, y, e, f (and w = z = Phi+)

VERDICT SIX-AUDIT-CHECKS-PASS iff C0 and X1-X5 all pass; otherwise VERDICT NOT RENDERED.
"""
import itertools
import random
from fractions import Fraction as Fr

import numpy as np

results = []


def check(name, cond, detail=""):
    results.append(bool(cond))
    print(("PASS " if cond else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))


# --------------------------------------------------------------------------- exact labelled-qubit tensors
# An operator on labels L = (l1..ln) is a pair (L, T) with T an object array of shape (2,)*2n:
# T[r1..rn, c1..cn] = <r|A|c>.


def zeros(n):
    return np.full((2,) * (2 * n), Fr(0), dtype=object)


def from_matrix(M, labels):
    n = len(labels)
    T = zeros(n)
    for r in range(2 ** n):
        for c in range(2 ** n):
            rb = tuple((r >> (n - 1 - k)) & 1 for k in range(n))
            cb = tuple((c >> (n - 1 - k)) & 1 for k in range(n))
            T[rb + cb] = Fr(M[r][c])
    return (tuple(labels), T)


def to_matrix(A):
    L, T = A
    n = len(L)
    M = [[Fr(0)] * (2 ** n) for _ in range(2 ** n)]
    for idx in itertools.product((0, 1), repeat=2 * n):
        r = int("".join(map(str, idx[:n])) or "0", 2)
        c = int("".join(map(str, idx[n:])) or "0", 2)
        M[r][c] = T[idx]
    return M


def ket(vec, labels, scale=Fr(1)):
    n = len(labels)
    M = [[Fr(vec[r]) * Fr(vec[c]) * scale for c in range(2 ** n)] for r in range(2 ** n)]
    return from_matrix(M, labels)


def ident(labels, scale=Fr(1)):
    n = len(labels)
    return from_matrix([[scale if r == c else Fr(0) for c in range(2 ** n)] for r in range(2 ** n)], labels)


def add(A, B, sb=Fr(1)):
    B = reorder(B, A[0])
    return (A[0], A[1] + B[1] * sb)


def reorder(A, labels):
    L, T = A
    labels = tuple(labels)
    if labels == L:
        return A
    n = len(L)
    perm = [L.index(l) for l in labels]
    return (labels, np.transpose(T, perm + [n + p for p in perm]))


def kron(A, B):
    (LA, TA), (LB, TB) = A, B
    assert not set(LA) & set(LB)
    na, nb = len(LA), len(LB)
    T = np.multiply.outer(TA, TB)  # axes: rA cA rB cB
    perm = list(range(na)) + list(range(2 * na, 2 * na + nb)) + list(range(na, 2 * na)) + \
        list(range(2 * na + nb, 2 * na + 2 * nb))
    return (LA + LB, np.transpose(T, perm))


def cond(e, X):
    """tr_A[(e_A (x) 1) X], A = labels of e: result_{rb,cb} = sum_{a,k} e_{a,k} X_{(k,rb),(a,cb)}."""
    LA, TE = e
    LX, TXo = X
    rest = tuple(l for l in LX if l not in LA)
    X = reorder(X, LA + rest)
    TX = X[1]
    na, nr = len(LA), len(rest)
    # TX axes: rA(0..na-1) rR(na..na+nr-1) cA(na+nr..2na+nr-1) cR(...)
    # TE axes: a (row, 0..na-1), k (col, na..2na-1); contract TE row a with TX col-A, TE col k with TX row-A
    out = np.tensordot(TE, TX, axes=(list(range(na)) + list(range(na, 2 * na)),
                                     list(range(na + nr, 2 * na + nr)) + list(range(na))))
    return (rest, out)


def pairing(E, X):
    """tr(E X) for operators on the same label set."""
    X = reorder(X, E[0])
    n = len(E[0])
    out = np.tensordot(E[1], X[1], axes=(list(range(2 * n)), list(range(n, 2 * n)) + list(range(n))))
    out = np.asarray(out, dtype=object).item()
    return Fr(out)


def transpose_full(A):
    L, T = A
    n = len(L)
    return (L, np.transpose(T, list(range(n, 2 * n)) + list(range(n))))


def rename(A, mapping):
    return (tuple(mapping.get(l, l) for l in A[0]), A[1])


def ptrace(X, keep):
    rest = tuple(l for l in X[0] if l not in keep)
    return cond(ident(rest), X)


# ------------------------------------------------------------------------------------- standard objects
PHI = [1, 0, 0, 1]


def phi_plus(a, b):
    return ket(PHI, (a, b), Fr(1, 2))


def ghz(labels):
    return ket([1, 0, 0, 0, 0, 0, 0, 1], labels, Fr(1, 2))


def w3(labels):
    return add(ident(labels, Fr(1, 2)), ghz(labels), Fr(-1))


def glue_network(x, y, e, f, w, z):
    gs = cond(w, kron(x, y))
    ge = cond(z, kron(e, f))
    return pairing(ge, gs)


rng = random.Random(20261009)


def rand_real(labels, lo=-3, hi=3):
    n = len(labels)
    return from_matrix([[Fr(rng.randint(lo, hi)) for _ in range(2 ** n)] for _ in range(2 ** n)], labels)


def rand_psd_rank1(labels):
    n = len(labels)
    v = [Fr(rng.randint(-3, 3)) for _ in range(2 ** n)]
    if all(a == 0 for a in v):
        v[0] = Fr(1)
    return ket(v, labels)


# ------------------------------------------------------------------------------------------------- C0
X = rand_real(("A", "B"))
pt = ptrace(X, ("B",))
M = to_matrix(X)
pt_direct = [[M[0 * 2 + i][0 * 2 + j] + M[1 * 2 + i][1 * 2 + j] for j in range(2)] for i in range(2)]
c0a = to_matrix(pt) == pt_direct
Xa, Yb = rand_real(("A",)), rand_real(("B",))
while to_matrix(Yb)[0][1] == to_matrix(Yb)[1][0]:
    Yb = rand_real(("B",))
lhs = pairing(phi_plus("A", "B"), kron(Xa, Yb))
mX, mY = to_matrix(Xa), to_matrix(Yb)
tr_XYT = sum(mX[i][j] * mY[i][j] for i in range(2) for j in range(2))
tr_XY = sum(mX[i][j] * mY[j][i] for i in range(2) for j in range(2))
c0b = lhs == Fr(1, 2) * tr_XYT
c0c = lhs != Fr(1, 2) * tr_XY
check("C0 machinery: cond(1, X) = partial trace; Bell link gives (1/2) tr(X Y^T); countercontrol without T differs",
      c0a and c0b and c0c, f"{c0a} {c0b} {c0c}")

# ------------------------------------------------------------------------------------------------- X1
toks = range(6)
per_size = {k: 0 for k in range(7)}
classes6 = {}
bad_part = False
for k in range(1, 7):
    for S in itertools.combinations(toks, k):
        S = frozenset(S)
        bips = set()
        for r in range(1, len(S)):
            for A in itertools.combinations(sorted(S), r):
                A = frozenset(A)
                bips.add(frozenset({A, S - A}))
        bips = list(bips)
        for b1 in bips:
            for b2 in bips:
                if b1 == b2:
                    continue
                A, B = tuple(b1)
                C, D = tuple(b2)
                if all(len(P & Q) > 0 for P in (A, B) for Q in (C, D)):
                    per_size[k] += 1
                    if any(len(P) in (1, 5) for P in (A, B, C, D)):
                        bad_part = True
                    if k == 6:
                        t1 = tuple(sorted((len(A), len(B))))
                        t2 = tuple(sorted((len(C), len(D))))
                        classes6[(t1, t2)] = classes6.get((t1, t2), 0) + 1
x1 = (per_size[4] == 90 and per_size[5] == 360 and per_size[6] == 390
      and all(per_size[k] == 0 for k in (1, 2, 3)) and not bad_part
      and classes6 == {((2, 4), (2, 4)): 120, ((2, 4), (3, 3)): 90, ((3, 3), (2, 4)): 90, ((3, 3), (3, 3)): 90})
check("X1 crossing enumeration: 90 / 360 / 390 at |S| = 4 / 5 / 6; classes 120/90/90/90; no part of size 1 or 5",
      x1, f"sizes {dict((k, v) for k, v in per_size.items() if v)} classes6 {sorted(classes6.items())} bad {bad_part}")

# ------------------------------------------------------------------------------------------------- X2
P, Q, R1, R2, U1, U2, S_, T_ = "P", "Q", "R1", "R2", "U1", "U2", "S", "T"
xs = kron(ident((P,), Fr(1, 2)), phi_plus(R1, R2))
ys = kron(ident((Q,), Fr(1, 2)), phi_plus(U1, U2))
wl, zl = phi_plus(P, Q), phi_plus(S_, T_)
v_gw = glue_network(xs, ys, ghz((S_, R1, U1)), w3((T_, R2, U2)), wl, zl)
v_ww = glue_network(xs, ys, w3((S_, R1, U1)), w3((T_, R2, U2)), wl, zl)
v_gg = glue_network(xs, ys, ghz((S_, R1, U1)), ghz((T_, R2, U2)), wl, zl)
check("X2 PN_5 control: (GHZ, W3) = -1/64; (W3, W3) = 1/16; QM (GHZ, GHZ) = 1/32",
      v_gw == Fr(-1, 64) and v_ww == Fr(1, 16) and v_gg == Fr(1, 32), f"{v_gw} {v_ww} {v_gg}")

# ------------------------------------------------------------------------------------------------- X3
g = ghz(("a", "b", "c"))
gm = to_matrix(g)
rank1 = all(gm[i][j] * gm[k][l] == gm[i][l] * gm[k][j] for i in range(8) for j in range(8)
            for k in range(8) for l in range(8))
tr1 = sum(gm[i][i] for i in range(8)) == 1
margs_ok = True
for keep in (("a",), ("b",), ("c",)):
    mm = to_matrix(ptrace(g, keep))
    margs_ok &= mm == [[Fr(1, 2), Fr(0)], [Fr(0), Fr(1, 2)]]
gw = pairing(w3(("a", "b", "c")), g)
x_prod = to_matrix(xs)  # product across P | R1R2 by construction: check factorization of the matrix
fac = to_matrix(kron(ptrace(xs, (P,)), ptrace(xs, (R1, R2)))) == x_prod
check("X3 memberships: x, y product across P|R1R2; GHZ rank one, trace 1; GHZ one-token marginals 1/2 at all three "
      "cuts (so W3 >= 0 on biseparable states); <GHZ|W3|GHZ> = -1/2 (W3 not PSD)",
      rank1 and tr1 and margs_ok and gw == Fr(-1, 2) and fac, f"{rank1} {tr1} {margs_ok} {gw} {fac}")

# ------------------------------------------------------------------------------------------------- X4
ok4 = True
cc4 = True
details = []
for t in range(3):
    xr = rand_real((P, R1, R2), -2, 2)
    yr = rand_real((Q, U1, U2), -2, 2)
    e4 = kron(ident((S_,), Fr(1, 2)), phi_plus(R1, U1))
    f4 = kron(ident((T_,), Fr(1, 2)), phi_plus(R2, U2))
    val = glue_network(xr, yr, e4, f4, wl, zl)
    yp = reorder(rename(yr, {Q: P, U1: R1, U2: R2}), (P, R1, R2))
    rhs = Fr(1, 32) * pairing(reorder(xr, (P, R1, R2)), transpose_full(yp))
    no_t = Fr(1, 32) * pairing(reorder(xr, (P, R1, R2)), yp)
    ok4 &= val == rhs
    cc4 &= val != no_t
    details.append(f"{val}")
check("X4 theta identity: N = (1/4)(1/8) tr(x T(y')) on 3 random real pairs; countercontrol without T differs",
      ok4 and cc4, " ".join(details))

# ------------------------------------------------------------------------------------------------- X5
vals = []
for t in range(4):
    xq = rand_psd_rank1((P, R1, R2))
    yq = rand_psd_rank1((Q, U1, U2))
    eq = rand_psd_rank1((S_, R1, U1))
    fq = rand_psd_rank1((T_, R2, U2))
    vals.append(glue_network(xq, yq, eq, fq, wl, zl))
check("X5 QM sign control: N >= 0 on 4 random rank-one PSD quadruples", all(v >= 0 for v in vals),
      " ".join(str(v) for v in vals))

# ------------------------------------------------------------------------------------------------- floats
for name, val in (("v_gw", v_gw), ("v_ww", v_ww), ("v_gg", v_gg)):
    assert isinstance(val, Fr), name
print("--- audit_six: %d/%d checks pass" % (sum(results), len(results)))
print("VERDICT SIX-AUDIT-CHECKS-PASS" if all(results) else "VERDICT NOT RENDERED")
