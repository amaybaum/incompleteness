"""Independent exact check, part 2: EQ2-A's all-twisted results (a4c, a4d) and one consequence of IE2 for the gate
class (coordinator review; research only, base bcbc516f). Imports nothing from EQ2-A; conventions as review_eq2a_cm.py.

Decision rules, fixed before the run (rules, not expected numbers):
  F1  F = (1/2)(1 - |000><000| - |111><111|) + |000><111| + |111><000| lies in B_tw* (B_tw = K_(1,1,1), twist on the
      second copy of each pair): for each pair (i, j) and a symbolic pure state phi = (alpha, beta) on the third copy,
      PT_j of the conditional <phi|_k F |phi>_k equals the sum of squares EQ2-A's docstring states (identity checked
      here symbolically, after my own contraction routine); since tr(F (PT_j(sigma) (x) |phi><phi|)) =
      tr(PT_j(<phi|F|phi>) sigma), PSD-ness of that operator for every phi is membership in B_tw* (mixed rho by
      convexity). Same for G = Ad_{S (x) S (x) 1}(F) with its stated sum of squares.
  F2  tr(F G) = -1/2, and G is a local-unitary image of F; hence no local-unitary-invariant cone K with K inside K*
      contains F (written, one line).
  F3  x = F + 1/10: x = (3/5) 1 + (1/2) P+ - (3/2) P- with P+- the GHZ+- projectors; tr(G x) = -1/5 (so x is not in
      B_tw, G being in B_tw*); x is in B_tw* (F and 1 are); the written orbit bound 8 s^2 + 2 s tr B - 3/2 = 9/50 at
      s = 3/5, attained at U = S (x) S (x) 1.
  T   IE2 excludes the transposed gate class: for the CtrlGate T.cnot on the pair (0, 1) (T = PT_0 PT_1, a map of the
      pair cone Q onto itself), the idle extension sends |0><0| (x) Phi+_(1,2) (a product of a state and a Q-pair
      state) to an operator whose (1,2) marginal is PT_1(Phi+) (not in Q), and sends |0><0| (x) PT_2(Phi+)_(1,2) (a
      product with a Tw-pair state) to an operator whose (1,2) marginal is Phi+ (not in Tw). So with H0 and pair cones
      in {Q, Tw}, IE2 for T.cnot fails whatever the (1,2) twist bit. Controls: T.cnot maps Q onto Q at two copies
      (it is Ad CNOT followed by the transpose), and plain cnot's idle extension keeps both marginals in their cones.
  V   the review verdict prints only if every check passes.
"""
import sys
from functools import reduce
import sympy as sp

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)
    sys.stdout.flush()


I = sp.I


def kron(*Ms):
    return reduce(sp.kronecker_product, Ms)


def bits(a, n):
    return [(a >> (n - 1 - q)) & 1 for q in range(n)]


def num(bs):
    v = 0
    for b in bs:
        v = 2 * v + b
    return v


def PT(M, q, n):
    N = 2 ** n
    out = sp.zeros(N, N)
    for a in range(N):
        for b in range(N):
            ba, bb = bits(a, n), bits(b, n)
            ba2, bb2 = list(ba), list(bb)
            ba2[q], bb2[q] = bb[q], ba[q]
            out[a, b] = M[num(ba2), num(bb2)]
    return out


def contract(M, q, f, n=3):
    keep = [c for c in range(n) if c != q]
    out = sp.zeros(2 ** (n - 1), 2 ** (n - 1))
    for a in range(2 ** (n - 1)):
        for b in range(2 ** (n - 1)):
            s = 0
            for x in range(2):
                for y in range(2):
                    ba, bb = [0] * n, [0] * n
                    for idx, c in enumerate(keep):
                        ba[c] = bits(a, n - 1)[idx]
                        bb[c] = bits(b, n - 1)[idx]
                    ba[q], bb[q] = x, y
                    s += f[y, x] * M[num(ba), num(bb)]
            out[a, b] = s
    return out


def ptrace_keep(M, keep, n=3):
    m = len(keep)
    rest = [q for q in range(n) if q not in keep]
    out = sp.zeros(2 ** m, 2 ** m)
    for a in range(2 ** m):
        for b in range(2 ** m):
            s = 0
            for r in range(2 ** len(rest)):
                ba, bb = [0] * n, [0] * n
                for idx, q in enumerate(keep):
                    ba[q] = bits(a, m)[idx]
                    bb[q] = bits(b, m)[idx]
                for idx, q in enumerate(rest):
                    ba[q] = bits(r, len(rest))[idx]
                    bb[q] = bits(r, len(rest))[idx]
                s += M[num(ba), num(bb)]
            out[a, b] = s
    return out


def zero(M):
    return M.applyfunc(sp.expand).is_zero_matrix


def ket(s):
    v = sp.zeros(2 ** len(s), 1)
    v[int(s, 2)] = 1
    return v


k000, k111 = ket("000"), ket("111")
F = (sp.eye(8) - k000 * k000.T - k111 * k111.T) / 2 + k000 * k111.T + k111 * k000.T
Sg = sp.diag(1, I)
US = kron(Sg, Sg, sp.eye(2))
G = US * F * US.H
PAIRS = [(0, 1), (0, 2), (1, 2)]

a1, a2, b1, b2 = sp.symbols("a1 a2 b1 b2", real=True)
al, be = a1 + I * a2, b1 + I * b2
phi = sp.Matrix([al, be])
Pphi = phi * phi.H


def pair_ket(s):
    return ket(s)


def sos(sign):
    u = sp.conjugate(al) * pair_ket("01") + sign * sp.conjugate(be) * pair_ket("10")
    w = be * pair_ket("01") + sign * al * pair_ket("10")
    return (sp.Rational(1, 2) * (be * sp.conjugate(be)) * pair_ket("00") * pair_ket("00").T
            + sp.Rational(1, 2) * (al * sp.conjugate(al)) * pair_ket("11") * pair_ket("11").T
            + sp.Rational(1, 2) * (u * u.H + w * w.H))


ok_F, ok_G = True, True
for (i, j) in PAIRS:
    k = [c for c in range(3) if c not in (i, j)][0]
    for X, sgn, flag in ((F, 1, "F"), (G, -1, "G")):
        cond = contract(X, k, Pphi)                         # <phi|_k X |phi>_k on the copies (i, j)
        jj = 1                                              # j is the second of the remaining two copies (i < j)
        lhs = PT(cond, jj, 2)
        good = zero(lhs - sos(sgn))
        if flag == "F":
            ok_F &= good
        else:
            ok_G &= good
check("F1 for each pair, PT_j(<phi|_k F |phi>_k) equals the stated sum of squares (symbolic phi): F is in B_tw*", ok_F)
check("F1 for each pair, PT_j(<phi|_k G |phi>_k) equals the stated sum of squares (symbolic phi): G is in B_tw*", ok_G)
check("F1 control: the identity contraction tr(X (PT_j(sigma) (x) |phi><phi|)) = tr(PT_j(<phi|X|phi>) sigma) "
      "(symbolic sigma, pair (0,1))",
      sp.expand((F * kron(PT(sp.Matrix(4, 4, lambda u, v: sp.Symbol(f"s{u}{v}")), 1, 2), Pphi)).trace()
                - (PT(contract(F, 2, Pphi), 1, 2) * sp.Matrix(4, 4, lambda u, v: sp.Symbol(f"s{u}{v}"))).trace()) == 0)
check("F2 G = Ad_{S (x) S (x) 1}(F) is a local-unitary image of F (S = diag(1, i) unitary)", zero(Sg * Sg.H - sp.eye(2)))
check("F2 tr(F G) = -1/2", sp.simplify((F * G).trace()) == sp.Rational(-1, 2))
gp = (k000 + k111) / sp.sqrt(2)
gm = (k000 - k111) / sp.sqrt(2)
Pp, Pm = gp * gp.T, gm * gm.T
t = sp.Rational(1, 10)
x = F + t * sp.eye(8)
check("F3 x = F + 1/10 = (3/5) 1 + (1/2) P+ - (3/2) P-",
      zero(x - (sp.Rational(3, 5) * sp.eye(8) + Pp / 2 - sp.Rational(3, 2) * Pm)))
check("F3 tr(G x) = -1/5, so x is not in B_tw (G is in B_tw*); x is in B_tw* (F is, and tr g >= 0 on generators)",
      sp.simplify((G * x).trace()) == sp.Rational(-1, 5))
s_ = sp.Rational(1, 2) + t
Bm = Pp / 2 - sp.Rational(3, 2) * Pm
bound = 8 * s_ ** 2 + 2 * s_ * Bm.trace() - sp.Rational(3, 2)
check(f"F3 written orbit bound 8 s^2 + 2 s tr B - 3/2 = {bound} = 9/50 (tr B = {Bm.trace()})", bound == sp.Rational(9, 50))
check("F3 tightness: tr(x U x U^dag) = 9/50 at U = S (x) S (x) 1",
      sp.simplify((x * US * x * US.H).trace()) == sp.Rational(9, 50))

# ---------- T: IE2 excludes the transposed gate class ----------
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
s0 = sp.eye(2)
phip = (ket("00") + ket("11")) / sp.sqrt(2)
Phip = phip * phip.T


def is_psd(M):
    M = M.applyfunc(sp.nsimplify)
    return M == M.H and all(sp.re(ev) >= 0 for ev in M.eigenvals())


def T_cnot_2(X):
    """T . Ad CNOT on a two-copy operator (T = full transpose = PT_0 PT_1)"""
    return PT(PT(CNOT * X * CNOT.H, 0, 2), 1, 2)


Ssym = sp.Matrix(4, 4, lambda u, v: sp.Symbol(f"s{u}{v}"))
check("T control: T.cnot = (Ad CNOT)^T on two copies, so it maps Q onto Q (transpose and unitary conjugation preserve "
      "PSD) (symbolic)", zero(T_cnot_2(Ssym) - (CNOT * Ssym * CNOT.H).T))


def T_cnot_ext(X):
    C3 = kron(CNOT, s0)
    return PT(PT(C3 * X * C3.H, 0, 3), 1, 3)


def cnot_ext(X):
    C3 = kron(CNOT, s0)
    return C3 * X * C3.H


z0 = ket("0") * ket("0").T
inQ = kron(z0, Phip)                        # |0><0| (x) Phi+ on (1,2): a product of a state and a Q-pair state
inTw = kron(z0, PT(Phip, 1, 2))             # |0><0| (x) PT_2(Phi+) on (1,2): a product with a Tw-pair state
m12_Q = ptrace_keep(T_cnot_ext(inQ), [1, 2])
m12_Tw = ptrace_keep(T_cnot_ext(inTw), [1, 2])
check("T (pair (1,2) in Q) the idle extension of T.cnot sends |0><0| (x) Phi+ to an operator with (1,2) marginal "
      "PT_1(Phi+), which is not PSD (eigenvalue -1/2): not in Q",
      zero(m12_Q - PT(Phip, 0, 2)) and not is_psd(m12_Q))
check("T (pair (1,2) in Tw) the idle extension of T.cnot sends |0><0| (x) PT_2(Phi+) to an operator with (1,2) "
      "marginal Phi+, and PT_2(Phi+) is not PSD, so Phi+ is not in Tw = PT_2(Q)",
      zero(m12_Tw - Phip) and not is_psd(PT(Phip, 1, 2)))
check("T control: plain cnot's idle extension keeps the (1,2) marginals of both inputs in their cones "
      "(Phi+ in Q, PT_2(Phi+) in Tw)",
      zero(ptrace_keep(cnot_ext(inQ), [1, 2]) - Phip) and zero(ptrace_keep(cnot_ext(inTw), [1, 2]) - PT(Phip, 1, 2)))

npass = sum(1 for _, c in checks if c)
print(f"review_eq2a_cm2: {npass}/{len(checks)} checks pass")
if npass == len(checks):
    print("VERDICT TWISTED-AND-GATE-CLASS-CONFIRMED: F, G lie in B_tw* with tr(FG) = -1/2 (B_tw not self-dual); the "
          "one-orbit bound for F + 1/10 is 9/50 and tight; IE2 with H0 excludes the transposed gate class T.cnot")
else:
    print("VERDICT NOT RENDERED")
sys.exit(0 if npass == len(checks) else 1)
