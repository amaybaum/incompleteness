#!/usr/bin/env python3
"""Avenue 1 (Track B, chart J1): an exact padded two-token stage table that is not locally tomographic.

Standard library only; arithmetic in Q(i) with fractions.Fraction.  Self-contained: reads no file.
Run:  python3 -I padded_pair_exact.py

Model.  Four qubits in the order (A, B, hA, hB), basis index 8a + 4b + 2hA + hB.  A and B are the
tokens; hA and hB are hidden bits with the fixed prior I/2 (x) I/2, read by no local instrument.
Instruments:
  local on A : HA = Hadamard, VA = H S^dag            local on B : HB, VB, XB = Pauli X
  joint      : CN = CNOT(A -> B), L = X_B controlled by the parity hA xor hB
  readouts   : MZB (Z on B, two outcomes), RD (Z on A and Z on B, four outcomes).
Preparations are instrument words from |00><00| (x) I/4, with selection on a readout where stated.
Effects are (test word w over {HA,VA,HB,VB,CN,L}, |w| <= 2) followed by RD with outcome (a, b).

Checks (each prints PASS/FAIL):
  ST   the table is a valid finite stage: entries in [0, 1], each test sums to 1, the unit is 1.
  PF   every effect whose word uses local instruments only is a product E_A (x) E_B (x) I_hh.
  TC   the product effects span Herm(4) on the shadow (rank 16): the product chart is the Pauli chart.
  SH   every row of a product effect equals the Born row of the shadow rho_AB = Tr_hh rho, and every
       shadow is a density matrix (exact rank-one or LDL certificate).
  NS   operational no-signalling on product tests, in both directions.
  NLT  Qe and Qo agree on every product effect and differ on the effect (L, RD = (0,1)).
  DIM  on the parity-classical sector (dimension 32) product effects have rank 16 and the depth-3
       effects strictly more (the measured rank is printed).
  DSC  HA, VA, HB, VB, XB, CN act as U (x) I_hh, so each preserves equality of shadows; L does not
       (Qe, Qo have equal shadows, L(Qe), L(Qo) do not).
  K829 finite-stage shadow clauses: product preparations have product shadows; the shadows of all
       preparations and of their images under CN and the local instruments are density matrices.
  IF   the composite of local preparations is a function of the local states (prior fixed).
A mutation self-test runs first; the verdict prints only if every mutation is detected and every
unmutated check passes.
"""
from fractions import Fraction as Fr
import itertools
import sys

MUT = set()
RESULTS = []


def check(ok, cid, text):
    RESULTS.append((bool(ok), cid, text))


class G:
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fr(re)
        self.im = Fr(im)

    def __add__(self, o):
        return G(self.re + o.re, self.im + o.im)

    def __sub__(self, o):
        return G(self.re - o.re, self.im - o.im)

    def __mul__(self, o):
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    def sc(self, f):
        return G(self.re * f, self.im * f)

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def iszero(self):
        return self.re == 0 and self.im == 0

    def __repr__(self):
        return f"({self.re}+{self.im}i)"


Z0 = G()
ONE = G(1)


def zeros(n):
    return [[G() for _ in range(n)] for _ in range(n)]


def mat_eq(a, b):
    return all(a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a)))


def tr(a):
    s = G()
    for i in range(len(a)):
        s = s + a[i][i]
    return s


def mm(a, b):
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for k in range(n):
            if a[i][k].iszero():
                continue
            aik = a[i][k]
            for j in range(n):
                if not b[k][j].iszero():
                    out[i][j] = out[i][j] + aik * b[k][j]
    return out


def dag(a):
    n = len(a)
    return [[a[j][i].conj() for j in range(n)] for i in range(n)]


def kron(a, b):
    na, nb = len(a), len(b)
    return [[a[i // nb][j // nb] * b[i % nb][j % nb] for j in range(na * nb)] for i in range(na * nb)]


def bit(i, k):
    """Bit of qubit k (0 = A, 1 = B, 2 = hA, 3 = hB) in a 16-dim index."""
    return (i >> (3 - k)) & 1


def setbit(i, k, v):
    return (i & ~(1 << (3 - k))) | (v << (3 - k))


# single-qubit data: (M, scale) with U = M / sqrt(2) for H-type gates, so U X U^dag = (1/2) M X M^dag
HM = [[G(1), G(1)], [G(1), G(-1)]]
VM = [[G(1), G(0, -1)], [G(1), G(0, 1)]]     # sqrt(2) * H S^dag


def conj1(R, k, M, scale):
    """R -> scale * (M on qubit k) R (M on qubit k)^dag, structurally."""
    n = 16
    out = zeros(n)
    for i in range(n):
        bi = bit(i, k)
        for j in range(n):
            bj = bit(j, k)
            s = G()
            for x in range(2):
                mx = M[bi][x]
                if mx.iszero():
                    continue
                ix = setbit(i, k, x)
                for y in range(2):
                    my = M[bj][y]
                    if my.iszero():
                        continue
                    r = R[ix][setbit(j, k, y)]
                    if not r.iszero():
                        s = s + mx * r * my.conj()
            out[i][j] = s.sc(scale)
    return out


def perm(R, f):
    out = zeros(16)
    for i in range(16):
        for j in range(16):
            out[f(i)][f(j)] = R[i][j]
    return out


def f_XB(i):
    return i ^ 4


def f_CN(i):
    return i ^ (4 * bit(i, 0))


def f_L(i):
    return i ^ (4 * (bit(i, 2) ^ bit(i, 3)))


def apply(sym, R):
    if sym == "HA":
        return conj1(R, 0, HM, Fr(1, 2))
    if sym == "VA":
        return conj1(R, 0, VM, Fr(1, 2))
    if sym == "HB":
        if "HB_nonlocal" in MUT:
            return conj1(conj1(R, 1, HM, Fr(1, 2)), 0, HM, Fr(1, 2))
        return conj1(R, 1, HM, Fr(1, 2))
    if sym == "VB":
        return conj1(R, 1, VM, Fr(1, 2))
    if sym == "XB":
        return perm(R, f_XB)
    if sym == "CN":
        return perm(R, f_CN)
    if sym == "L":
        if "L_descends" in MUT:
            return R
        return perm(R, f_L)
    raise ValueError(sym)


def project(R, pred):
    out = zeros(16)
    for i in range(16):
        if not pred(i):
            continue
        for j in range(16):
            if pred(j):
                out[i][j] = R[i][j]
    return out


def heis(sym, E):
    """Heisenberg picture: E -> U^dag E U."""
    if sym in ("HA", "HB"):
        k = 0 if sym == "HA" else 1
        out = conj1(E, k, [[HM[j][i].conj() for j in range(2)] for i in range(2)], Fr(1, 2))
        if sym == "HB" and "HB_nonlocal" in MUT:
            out = conj1(out, 0, [[HM[j][i].conj() for j in range(2)] for i in range(2)], Fr(1, 2))
        return out
    if sym in ("VA", "VB"):
        k = 0 if sym == "VA" else 1
        return conj1(E, k, [[VM[j][i].conj() for j in range(2)] for i in range(2)], Fr(1, 2))
    if sym == "XB":
        return perm(E, f_XB)
    if sym == "CN":
        return perm(E, f_CN)
    if sym == "L":
        if "L_descends" in MUT:
            return E
        return perm(E, f_L)
    raise ValueError(sym)


def initial():
    R = zeros(16)
    for h in range(4):
        R[h][h] = G(Fr(1, 4))
    return R


def preps():
    """The preparation list; built at run time so that mutations act (not at import time)."""
    P = [
        ("P00", (), None),
        ("P+0", ("HA",), None),
        ("PPhi", ("HA", "CN"), None),
        ("Qe", ("L", "MZB"), 0),
        ("Qo", ("L", "MZB", "XB"), 1),
        ("Qe+", ("HA", "L", "MZB"), 0),
        ("Qo+", ("HA", "L", "MZB", "XB"), 1),
    ]
    if "Qo_no_fix" in MUT:
        P[4] = ("Qo", ("L", "MZB"), 1)
        P[6] = ("Qo+", ("HA", "L", "MZB"), 1)
    return P


TEST_SYMS = ["HA", "VA", "HB", "VB", "CN", "L"]
LOCAL = {"HA", "VA", "HB", "VB", "XB"}
WORDS = [()] + [(s,) for s in TEST_SYMS] + [(s, t) for s in TEST_SYMS for t in TEST_SYMS]
OUTS = [(a, b) for a in range(2) for b in range(2)]


def prepare(word, sel):
    """Run a preparation word; MZB records an outcome.  Returns the normalized state given sel."""
    R = initial()
    for sym in word:
        if sym == "MZB":
            R = project(R, lambda i: bit(i, 1) == sel)
        else:
            R = apply(sym, R)
    t = tr(R)
    assert t.im == 0 and t.re >= 0
    if t.re == 0:
        return R          # a selection of probability zero (only under a mutation): the zero matrix
    return [[R[i][j].sc(1 / t.re) for j in range(16)] for i in range(16)]


def evolve(word, R):
    for sym in word:
        R = apply(sym, R)
    return R


def rd_probs(R):
    return {(a, b): sum((R[i][i].re for i in range(16) if bit(i, 0) == a and bit(i, 1) == b), Fr(0))
            for (a, b) in OUTS}


def shadow(R):
    out = zeros(4)
    for i in range(16):
        for j in range(16):
            if (i & 3) == (j & 3):
                out[i >> 2][j >> 2] = out[i >> 2][j >> 2] + R[i][j]
    if "shadow_diag" in MUT:
        out = [[out[i][j] if i == j else G() for j in range(4)] for i in range(4)]
    return out


def is_density(M):
    """Exact certificate that a 4x4 Hermitian matrix is a density matrix: Hermitian, trace 1, and
    PSD by an exact LDL^dag pivot elimination (all pivots >= 0, zero pivots with zero columns)."""
    n = len(M)
    if not all(M[i][j] == M[j][i].conj() for i in range(n) for j in range(n)):
        return False
    if not tr(M) == ONE:
        return False
    A = [[M[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        p = A[k][k]
        if p.im != 0 or p.re < 0:
            return False
        if p.re == 0:
            if any(not A[k][j].iszero() for j in range(k, n)):
                return False
            continue
        for i in range(k + 1, n):
            f = A[i][k].sc(1 / p.re)
            for j in range(k + 1, n):
                A[i][j] = A[i][j] - f * A[k][j]
        for i in range(k + 1, n):
            A[i][k] = G()
            A[k][i] = G()
    return True


def local_op_4(sym, M):
    """The same local gate on the 4-dim AB carrier (independent code path for the shadow)."""
    def k4(i, k):
        return (i >> (1 - k)) & 1

    def s4(i, k, v):
        return (i & ~(1 << (1 - k))) | (v << (1 - k))
    if sym in ("HA", "VA", "HB", "VB"):
        k = 0 if sym[1] == "A" else 1
        U = HM if sym[0] == "H" else VM
        out = zeros(4)
        for i in range(4):
            for j in range(4):
                s = G()
                for x in range(2):
                    for y in range(2):
                        s = s + U[k4(i, k)][x] * M[s4(i, k, x)][s4(j, k, y)] * U[k4(j, k)][y].conj()
                out[i][j] = s.sc(Fr(1, 2))
        return out
    if sym in ("XB", "CN"):
        f = (lambda i: i ^ 1) if sym == "XB" else (lambda i: i ^ (i >> 1))
        out = zeros(4)
        for i in range(4):
            for j in range(4):
                out[f(i)][f(j)] = M[i][j]
        return out
    raise ValueError(sym)


def herm_vec(M):
    """Real coordinates of a Hermitian matrix: diagonal, then Re and Im of the upper triangle."""
    n = len(M)
    v = [M[i][i].re for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            v.append(M[i][j].re)
            v.append(M[i][j].im)
    return v


def rank(rows):
    rows = [list(r) for r in rows]
    rk, col = 0, 0
    ncol = len(rows[0]) if rows else 0
    while rk < len(rows) and col < ncol:
        piv = next((i for i in range(rk, len(rows)) if rows[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        p = rows[rk][col]
        for i in range(len(rows)):
            if i != rk and rows[i][col] != 0:
                f = rows[i][col] / p
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[rk])]
        rk += 1
        col += 1
    return rk


def run():
    RESULTS.clear()
    states = {name: prepare(w, s) for name, w, s in preps()}
    # ---- the stage table
    table = {}
    for name, R in states.items():
        for w in WORDS:
            p = rd_probs(evolve(w, R))
            for ab in OUTS:
                table[(name, w, ab)] = p[ab]
    ok = all(0 <= v <= 1 for v in table.values())
    ok &= all(sum(table[(n, w, ab)] for ab in OUTS) == 1 for n in states for w in WORDS)
    check(ok, "ST", f"{len(states)} preparations x {len(WORDS)} tests x 4 outcomes (+ unit): every entry in [0,1], every test sums to 1: a valid finite stage")

    # ---- product effects factorize
    prod_words = [w for w in WORDS if all(s in LOCAL for s in w)]
    joint_words = [w for w in WORDS if w not in prod_words]
    effects = {}
    for w in WORDS:
        for (a, b) in OUTS:
            E = project([[G(int(i == j)) for j in range(16)] for i in range(16)],
                        lambda i, a=a, b=b: bit(i, 0) == a and bit(i, 1) == b)
            for sym in reversed(w):
                E = heis(sym, E)
            effects[(w, (a, b))] = E

    def factor(E):
        # E = EA (x) EB (x) I_4 ?  test: E[i][j] = 0 unless hidden parts equal, independent of hidden
        for i in range(16):
            for j in range(16):
                if (i & 3) != (j & 3) and not E[i][j].iszero():
                    return False
                if (i & 3) == (j & 3) and not E[i][j] == E[i & ~3][j & ~3]:
                    return False
        E4 = [[E[4 * i][4 * j] for j in range(4)] for i in range(4)]
        # rank-one tensor structure E4[(a b),(a' b')] = EA[a][a'] EB[b][b']
        idx = [(a, b) for a in range(2) for b in range(2)]
        pa = next(((a, a2) for a in range(2) for a2 in range(2) for b in range(2) for b2 in range(2)
                   if not E4[2 * a + b][2 * a2 + b2].iszero()), None)
        if pa is None:
            return True
        for (a, b), (a2, b2) in itertools.product(idx, idx):
            for (c, d), (c2, d2) in itertools.product(idx, idx):
                lhs = E4[2 * a + b][2 * a2 + b2] * E4[2 * c + d][2 * c2 + d2]
                rhs = E4[2 * a + d][2 * a2 + d2] * E4[2 * c + b][2 * c2 + b2]
                if not lhs == rhs:
                    return False
        return True
    ok = all(factor(effects[(w, ab)]) for w in prod_words for ab in OUTS)
    check(ok, "PF", f"all {len(prod_words) * 4} effects of the {len(prod_words)} local-only words are E_A (x) E_B (x) I_hh (exact rank-one tensor identities)")

    # ---- tomographic completeness of the product chart on the shadow
    E4s = [[[effects[(w, ab)][4 * i][4 * j] for j in range(4)] for i in range(4)] for w in prod_words for ab in OUTS]
    rk = rank([herm_vec(E) for E in E4s])
    check(rk == 16, "TC", f"the product effects span Herm(4): rank {rk} = 16, so the product-coincidence chart is the full Pauli chart of the shadow")

    # ---- shadow Born rows and density certificates
    shadows = {n: shadow(R) for n, R in states.items()}
    ok = all(is_density(S) for S in shadows.values())
    okb = True
    for n in states:
        for w in prod_words:
            S = shadows[n]
            for sym in w:
                S = local_op_4(sym, S)
            for (a, b) in OUTS:
                if S[2 * a + b][2 * a + b].re != table[(n, w, (a, b))] or S[2 * a + b][2 * a + b].im != 0:
                    okb = False
    check(ok and okb, "SH", "every shadow Tr_hh rho is a density matrix (exact LDL certificate), and every product-effect row equals the Born row of the shadow under the 4-dim local gates (independent code path)")

    # ---- no-signalling on product tests
    loc_A = [w for w in prod_words if all(s.endswith("A") for s in w)]
    loc_B = [w for w in prod_words if all(s.endswith("B") for s in w)]
    okns = True
    for n in states:
        for wa in loc_A:
            margs = set()
            for wb in loc_B:
                if len(wa) + len(wb) > 2:
                    continue
                w = wa + wb
                margs.add(tuple(sum(table[(n, w, (a, b))] for b in range(2)) for a in range(2)))
            okns &= len(margs) == 1
        for wb in loc_B:
            margs = set()
            for wa in loc_A:
                if len(wa) + len(wb) > 2:
                    continue
                w = wa + wb
                margs.add(tuple(sum(table[(n, w, (a, b))] for a in range(2)) for b in range(2)))
            okns &= len(margs) == 1
    check(okns, "NS", "on every preparation, A's outcome marginal is independent of B's local word and conversely (exact)")

    # ---- non-local-tomography certificate
    same = all(table[("Qe", w, ab)] == table[("Qo", w, ab)] for w in prod_words for ab in OUTS)
    pe = table[("Qe", ("L",), (0, 1))]
    po = table[("Qo", ("L",), (0, 1))]
    diffs = sum(1 for w in joint_words for ab in OUTS if table[("Qe", w, ab)] != table[("Qo", w, ab)])
    same_sh = mat_eq(shadows["Qe"], shadows["Qo"])
    check(same and same_sh and pe != po, "NLT",
          f"Qe and Qo have the same shadow |00><00| and agree on all {len(prod_words) * 4} product effects; on (L, RD=(0,1)) they give {pe} and {po}; {diffs} joint effects separate them: the stage is not locally tomographic")
    same2 = all(table[("Qe+", w, ab)] == table[("Qo+", w, ab)] for w in prod_words for ab in OUTS)
    d2 = [(w, ab) for w in joint_words for ab in OUTS if table[("Qe+", w, ab)] != table[("Qo+", w, ab)]]
    check(same2 and len(d2) > 0 and mat_eq(shadows["Qe+"], shadows["Qo+"]), "NLT+",
          f"Qe+ and Qo+ (shadow |+0><+0|) agree on all product effects and differ on {len(d2)} joint effects")

    # ---- dimension certificate on the parity-classical sector
    def parity_pair(E):
        ev = [[E[4 * i + 0][4 * j + 0] for j in range(4)] for i in range(4)]
        od = [[E[4 * i + 1][4 * j + 1] for j in range(4)] for i in range(4)]
        return herm_vec(ev) + herm_vec(od)
    ok_cq = all(E[i][j].iszero() for E in effects.values() for i in range(16) for j in range(16) if (i & 3) != (j & 3))
    ok_par = all(E[i][j] == E[(i & ~3) | ((i & 3) ^ 3)][(j & ~3) | ((j & 3) ^ 3)]
                 for E in effects.values() for i in range(16) for j in range(16))
    rk_prod = rank([parity_pair(effects[(w, ab)]) for w in prod_words for ab in OUTS])
    rk_all = rank([parity_pair(effects[(w, ab)]) for w in WORDS for ab in OUTS])
    # depth 3 by the Heisenberg recursion E[(s,) + w] = U_s^dag E[w] U_s
    eff3 = dict(effects)
    for w in [w for w in WORDS if len(w) == 2]:
        for sym in TEST_SYMS:
            for ab in OUTS:
                eff3[((sym,) + w, ab)] = heis(sym, effects[(w, ab)])
    ok_cq &= all(E[i][j].iszero() for E in eff3.values() for i in range(16) for j in range(16) if (i & 3) != (j & 3))
    ok_par &= all(E[i][j] == E[(i & ~3) | ((i & 3) ^ 3)][(j & ~3) | ((j & 3) ^ 3)]
                  for E in eff3.values() for i in range(16) for j in range(16))
    rk_3 = rank([parity_pair(E) for E in eff3.values()])
    if "rank_short" in MUT:
        rk_3 = rank([parity_pair(effects[(w, ab)]) for w in prod_words for ab in OUTS])
    check(ok_cq and ok_par and rk_prod == 16 and rk_3 > rk_prod, "DIM",
          f"every effect (depth <= 3) is block-diagonal in hh and depends on hh only through the parity; on the pair (rho_even, rho_odd), of dimension 32, the product effects have rank {rk_prod}, all depth-2 effects rank {rk_all}, all depth-3 effects rank {rk_3} > {rk_prod}")

    # ---- descent
    def is_U_tensor_I(sym):
        # the instrument acts blockwise identically on the four hidden blocks (U (x) I_hh)
        # test on the 16 matrix units of the AB block, in every hidden block
        for i0 in range(4):
            for j0 in range(4):
                for h in range(4):
                    R = zeros(16)
                    R[4 * i0 + h][4 * j0 + h] = G(1)
                    out = apply(sym, R)
                    E4 = zeros(4)
                    E4[i0][j0] = G(1)
                    ref = local_op_4(sym, E4)
                    for i in range(16):
                        for j in range(16):
                            want = ref[i >> 2][j >> 2] if (i & 3) == h and (j & 3) == h else Z0
                            if not out[i][j] == want:
                                return False
        return True
    desc = {s: is_U_tensor_I(s) for s in ["HA", "VA", "HB", "VB", "XB", "CN"]}
    LQe, LQo = shadow(apply("L", states["Qe"])), shadow(apply("L", states["Qo"]))
    check(all(desc.values()) and not mat_eq(LQe, LQo) and mat_eq(shadows["Qe"], shadows["Qo"]), "DSC",
          "HA, VA, HB, VB, XB, CN act as U (x) I_hh on all 64 block units (hence descend to the shadow); L does not descend: Qe, Qo have equal shadows while L(Qe), L(Qo) have shadows |00><00| and |01><01|")

    # ---- finite-stage #829 shadow clauses
    ok = mat_eq(shadows["P00"], [[G(int(i == j == 0)) for j in range(4)] for i in range(4)])
    plus0 = [[G(Fr(1, 2)) if (i in (0, 2) and j in (0, 2)) else G() for j in range(4)] for i in range(4)]
    ok &= mat_eq(shadows["P+0"], plus0)
    okimg = all(is_density(local_op_4(s, S)) for S in shadows.values() for s in ["HA", "VA", "HB", "VB", "XB", "CN"])
    phi = [[G(Fr(1, 2)) if (i in (0, 3) and j in (0, 3)) else G() for j in range(4)] for i in range(4)]
    ok &= mat_eq(local_op_4("CN", plus0), phi) and mat_eq(shadows["PPhi"], phi)
    check(ok and okimg, "K829", "product preparations have product shadows (|00>, |+0>), CN maps the |+0> shadow to Phi+, and every shadow image under CN and the local gates is a density matrix (shadow images are density matrices; the #829 premises hold for the continuum shadow cone Q3 [W])")

    # ---- interface: product composite is a function of the local states
    def prod_prep(wa, wb):
        return prepare(wa + wb, None)
    okif = True
    for wa in [(), ("HA",), ("VA",)]:
        for wb in [(), ("HB",), ("VB",)]:
            R = prod_prep(wa, wb)
            S = shadow(R)
            # R = S (x) I/4 exactly
            for i in range(16):
                for j in range(16):
                    want = S[i >> 2][j >> 2].sc(Fr(1, 4)) if (i & 3) == (j & 3) else Z0
                    if not R[i][j] == want:
                        okif = False
    check(okif, "IF", "for local preparation words on A and B the composite state is shadow (x) I/4: the product state is a function of the two local states (the hidden prior is fixed)")
    return table


MUTATIONS = {
    "L_descends": "NLT",
    "Qo_no_fix": "NLT",
    "HB_nonlocal": "NS",
    "shadow_diag": "SH",
    "rank_short": "DIM",
}


def main():
    global MUT
    detected = {}
    for m, target in MUTATIONS.items():
        MUT = {m}
        run()
        failed = {cid for ok, cid, _ in RESULTS if not ok}
        detected[m] = target in failed
        print(f"mutation {m:18s} target {target:5s} {'REJECTED' if detected[m] else 'MUTATION-MISSED'} (failing: {sorted(failed)})")
    MUT = set()
    run()
    for ok, cid, text in RESULTS:
        print(f"{'PASS' if ok else 'FAIL'} {cid}: {text}")
    nfail = sum(1 for ok, _, _ in RESULTS if not ok)
    print(f"checks: {len(RESULTS)}, failures: {nfail}, mutations rejected: {sum(detected.values())}/{len(MUTATIONS)}")
    if nfail == 0 and all(detected.values()):
        print("VERDICT PADDED-PAIR-NOT-LT-EXACT")
    else:
        print("VERDICT NOT-ESTABLISHED")
        sys.exit(1)


if __name__ == "__main__":
    main()
