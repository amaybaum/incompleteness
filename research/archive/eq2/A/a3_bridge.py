"""EQ2-A probe A3 -- the typed IE2 bridge, exact instance checks.  Research only; base bcbc516f.
Usage: python3 -I -B a3_bridge.py

Objects (UNBUILT design, RESULT Sec. 2/T-B):
  NC S       native n-token carrier: tables idx -> R, idx in {0..3}^S (lexicographic, first token most significant)
  presentN g complexified Pauli conjugation of a real-linear table map g: X -> 2^-k sum_idx (g c(X))_idx P_idx,
             c(X)_idx = tr(X P_idx)
  idleExt    idleExt R S g = 1_{4^|R|} (x) g on NC (R + S) (R-indices first)
  chartN eps (x)_s homMap(eps_s)
  amplRef    kernel ReferenceExtension.lean:91, spectator first: (p,q) -> Phi(refBlockR M p.1 q.1) p.2 q.2

DECISION RULE (fixed before the first run): verdict `A3-BRIDGE-INSTANCES-EXACT` iff every check passes, including
  controls (the definitional identities withSpectator = transportT e e (amplRefL R .)) and countercontrols (a
  non-diagonal-preserving map is not rescued by amplification; a positive non-CP map's amplification is not
  positive).  All arithmetic exact (Rationals, Gaussian rationals, symbols).
Checks:
  B1.a presentN (idleExt R S g) = amplRef (presentN g)       |R| = 1, |S| = 1 and |R| = 1, |S| = 2 (random rational g)
  B1.b presentN (g . h) = presentN g . presentN h
  B1.c chartN (epsR + epsS) . idleExt g . chartN^-1 = idleExt (chartN epsS . g . chartN epsS^-1)
  B1.d presentN is injective (rank of g -> presentN g, as a linear map on the 256-dim space of g's at |S| = 2... done
       at |S| = 1: the 16 x 16 real maps g |-> presentN g are R-linearly independent)
  B2   instance of the pull-back step: presentN h = amplRef(presentN g) forces h = idleExt g (|R| = |S| = 1, symbolic h)
  B3.a (reading, not computed: withSpectator R e Phi = transportT e e (amplRefL R Phi) is rfl, SB:381 + TC:109)
       control of conventions: withSpectator (Fin 3) qutritIdx Phi acts as id (x) Phi on reindexed products
  B3.b PreservesDiag Phi -> PreservesDiag (amplRef R Phi): random diagonal-preserving Phi (CP and non-CP), symbolic w
  B3.c countercontrol: conj(Hadamard) does not preserve diagonals, nor does its amplification
  B3.d foil for TypedIdleExtension: the transpose map is positive; amplRef (Fin 2) transpose sends |Phi+><Phi+| to
       SWAP/2, value -1 at the singlet
  B3.e the typed Kraus theory is closed under amplification: amplRef (sum conj K_i) = sum conj (1 (x) K_i)
"""
import itertools
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq2a_lib as L  # noqa: E402

check = L.check
rng = random.Random(20261008)


def zero(M):
    return M.applyfunc(sp.expand).is_zero_matrix


def pstrings(k):
    return list(itertools.product(range(4), repeat=k))


def pmat(idx):
    return L.kron(*[L.PAULI[i] for i in idx])


def coords(X, k):
    return Matrix([sp.expand((X * pmat(idx)).trace()) for idx in pstrings(k)])


def from_coords(c, k):
    out = zeros(2 ** k, 2 ** k)
    for t, idx in enumerate(pstrings(k)):
        if c[t] != 0:
            out += c[t] * pmat(idx)
    return out / (2 ** k)


def presentN(G, k):
    return lambda X: from_coords(G * coords(X, k), k)


def rand_real(n, m=None):
    m = m or n
    return Matrix(n, m, lambda i, j: R(rng.randint(-6, 6), rng.randint(1, 5)))


def rand_gauss(n):
    return Matrix(n, n, lambda i, j: R(rng.randint(-4, 4), rng.randint(1, 3)) + I * R(rng.randint(-4, 4), rng.randint(1, 3)))


def amplRef(Phi, dR, dS):
    def f(M):
        out = zeros(dR * dS, dR * dS)
        for i in range(dR):
            for j in range(dR):
                blk = Matrix(dS, dS, lambda kk, ll: M[i * dS + kk, j * dS + ll])
                im = Phi(blk)
                for kk in range(dS):
                    for ll in range(dS):
                        out[i * dS + kk, j * dS + ll] = im[kk, ll]
        return out
    return f


# ---------------------------------------------------------------- B1.a idle extension is presented as amplification
for (r, s) in ((1, 1), (1, 2)):
    G = rand_real(4 ** s)
    Gext = L.kron(eye(4 ** r), G)
    Msym = Matrix(2 ** (r + s), 2 ** (r + s), lambda i, j: sp.Symbol(f"m{i}_{j}"))
    lhs = presentN(Gext, r + s)(Msym)
    rhs = amplRef(presentN(G, s), 2 ** r, 2 ** s)(Msym)
    check(f"B1.a presentN (idleExt R S g) = amplRef (presentN g), |R| = {r}, |S| = {s}, generic complex input",
          zero(lhs - rhs))

# ---------------------------------------------------------------- B1.b composition
G1, G2 = rand_real(16), rand_real(16)
Msym = Matrix(4, 4, lambda i, j: sp.Symbol(f"n{i}_{j}"))
check("B1.b presentN (g . h) = presentN g . presentN h (|S| = 2)",
      zero(presentN(G1 * G2, 2)(Msym) - presentN(G1, 2)(presentN(G2, 2)(Msym))))

# ---------------------------------------------------------------- B1.c chart naturality
skews = [Matrix([[0, R(1, 2), R(-1, 3)], [R(-1, 2), 0, R(2, 5)], [R(1, 3), R(-2, 5), 0]]),
         Matrix([[0, 3, 1], [-3, 0, R(-7, 4)], [-1, R(7, 4), 0]])]
epsR = L.hom_map(L.cayley(skews[0]) * L.REFLY)
epsS = L.hom_map(L.cayley(skews[1]))
G = rand_real(4)
chR_S = L.kron(epsR, epsS)
lhs = chR_S * L.kron(eye(4), G) * chR_S.inv()
rhs = L.kron(eye(4), epsS * G * epsS.inv())
check("B1.c chartN (epsR + epsS) . idleExt g . chartN^-1 = idleExt (chartN epsS . g . chartN epsS^-1)", zero(lhs - rhs))

# ---------------------------------------------------------------- B1.d injectivity of presentN at |S| = 1
basis_imgs = []
Mgen = Matrix(2, 2, lambda i, j: sp.Symbol(f"q{i}_{j}"))
for a in range(16):
    E = zeros(4, 4)
    E[a // 4, a % 4] = 1
    img = presentN(E, 1)(Mgen)
    row = []
    for e in img:
        poly = sp.Poly(sp.expand(e), *list(Mgen))
        for mono in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]:
            cf = poly.coeff_monomial(mono)
            row += [sp.re(cf), sp.im(cf)]
    basis_imgs.append(row)
check("B1.d g |-> presentN g is injective on the 16-dim space of real 4x4 table maps (rank 16)",
      Matrix(basis_imgs).rank() == 16)

# ---------------------------------------------------------------- B2 pull-back step
H = Matrix(16, 16, lambda i, j: sp.Symbol(f"h{i}_{j}", real=True))
G = rand_real(4)
Msym = Matrix(4, 4, lambda i, j: sp.Symbol(f"k{i}_{j}"))
diff = (presentN(H, 2)(Msym) - amplRef(presentN(G, 1), 2, 2)(Msym)).applyfunc(sp.expand)
eqs = []
for e in diff:
    poly = sp.Poly(e, *list(Msym))
    for cf in poly.coeffs():
        eqs += [sp.re(cf), sp.im(cf)]
sol = sp.solve(eqs, list(H), dict=True)
check("B2 presentN h = amplRef (presentN g) has the unique solution h = idleExt g = 1 (x) g",
      len(sol) == 1 and zero(H.subs(sol[0]) - L.kron(eye(4), G)))

# ---------------------------------------------------------------- B3.a withSpectator on reindexed products
# The identity withSpectator R e Phi = transportT e e (amplRefL R Phi) is DEFINITIONAL and landed as two rfl lemmas
# (SpectatorBridge.lean:381, TypedCompletion.lean:109); it is a reading, not a computation.  The non-vacuous control
# here checks my conventions (spectator first; Matrix.reindex e e M = M.submatrix e.symm e.symm) through the kernel's
# withSpectator_reindex + amplRef_tensorOf: withSpectator R e Phi (reindex e e (XR (x) X)) = reindex e e (XR (x) Phi X),
# with reindex implemented from the index map e directly (no permutation matrix).
# qutritIdx (ReferenceExtension.lean:458): (r, (a, e)) |-> (a, finProdFinEquiv (r, e)) = (a, 2 r + e)
src = [(r_, (a_, e_)) for r_ in range(3) for a_ in range(2) for e_ in range(2)]
e_map = {t: (t[1][0], 2 * t[0] + t[1][1]) for t in src}
e_inv = {v: k for k, v in e_map.items()}
check("B3.a control: qutritIdx is a bijection Fin 3 x (Fin 2 x Fin 2) -> Fin 2 x Fin 6",
      len(set(e_map.values())) == 12 and set(e_map.values()) == {(a_, m_) for a_ in range(2) for m_ in range(6)})
src_pos = {t: i for i, t in enumerate(src)}
dst_list = [(a_, m_) for a_ in range(2) for m_ in range(6)]


def reindex_e(M):          # Matrix.reindex e e : M_src -> M_dst, entry (x, y) = M (e.symm x) (e.symm y)
    return Matrix(12, 12, lambda i, j: M[src_pos[e_inv[dst_list[i]]], src_pos[e_inv[dst_list[j]]]])


def reindex_einv(N):       # Matrix.reindex e.symm e.symm : M_dst -> M_src
    dpos = {t: i for i, t in enumerate(dst_list)}
    return Matrix(12, 12, lambda i, j: N[dpos[e_map[src[i]]], dpos[e_map[src[j]]]])


Phi = presentN(rand_real(16), 2)
withSpectator = lambda N: reindex_e(amplRef(Phi, 3, 4)(reindex_einv(N)))  # noqa: E731  (RE:422 body)
XR = Matrix(3, 3, lambda i, j: sp.Symbol(f"r{i}_{j}"))
Xs = Matrix(4, 4, lambda i, j: sp.Symbol(f"s{i}_{j}"))
lhs = withSpectator(reindex_e(L.kron(XR, Xs)))
rhs = reindex_e(L.kron(XR, Phi(Xs)))
check("B3.a withSpectator (Fin 3) qutritIdx Phi (reindex e e (XR (x) X)) = reindex e e (XR (x) Phi X) (symbolic)",
      zero(lhs - rhs))
check("B3.a control: reindex e.symm e.symm is inverse to reindex e e (symbolic)",
      zero(reindex_einv(reindex_e(Matrix(12, 12, lambda i, j: sp.Symbol(f"t{i}_{j}")))) - Matrix(12, 12, lambda i, j: sp.Symbol(f"t{i}_{j}"))))


# ---------------------------------------------------------------- B3.b PreservesDiag stable under amplification
def rand_diag_preserving(d, cp_like):
    """A random linear map on d x d matrices sending every diagonal matrix to a diagonal matrix."""
    imgs = {}
    for i in range(d):
        for j in range(d):
            if i == j:
                imgs[(i, j)] = sp.diag(*[R(rng.randint(-3, 3), rng.randint(1, 3)) for _ in range(d)])
            else:
                imgs[(i, j)] = rand_gauss(d)
    if cp_like == "transpose":
        return lambda X: X.T
    return lambda X: sum((X[i, j] * imgs[(i, j)] for i in range(d) for j in range(d)), zeros(d, d))


wsym = sp.symbols("w0:8")
for name, kind, dS, dR in (("random", None, 2, 2), ("random", None, 4, 2), ("transpose (non-CP)", "transpose", 2, 3)):
    Phi = rand_diag_preserving(dS, kind)
    Dw = sp.diag(*wsym[:dS])
    img1 = Phi(Dw).applyfunc(sp.expand)
    pre = all(img1[i, j] == 0 for i in range(dS) for j in range(dS) if i != j)
    Dw2 = sp.diag(*wsym[:dS * dR])
    img = amplRef(Phi, dR, dS)(Dw2).applyfunc(sp.expand)
    post = all(img[i, j] == 0 for i in range(dS * dR) for j in range(dS * dR) if i != j)
    check(f"B3.b {name} Phi on dim {dS}: PreservesDiag Phi and PreservesDiag (amplRef (dim {dR}) Phi) (symbolic w)",
          pre and post)
Hd = Matrix([[1, 1], [1, -1]])
conjH = lambda X: Hd * X * Hd.T / 2  # noqa: E731
imgH = conjH(sp.diag(1, 0))
check("B3.c countercontrol: conj(Hadamard) does not preserve diagonals", imgH[0, 1] != 0)
imgH2 = amplRef(conjH, 2, 2)(sp.diag(1, 0, 0, 0))
check("B3.c countercontrol: nor does its amplification", imgH2[0, 1] != 0)

# ---------------------------------------------------------------- B3.d foil: transpose
transpose = lambda X: X.T  # noqa: E731
phi = Matrix([1, 0, 0, 1])
out = amplRef(transpose, 2, 2)(phi * phi.H / 2)
SWAP = L.swap_matrix([2, 2], [1, 0])
sv = Matrix([0, 1, -1, 0])
check("B3.d instance: the transpose of one Bloch state is PSD (general fact: Mathlib PosSemidef.transpose)",
      L.is_psd_exact((L.rho1([R(1, 3), R(-2, 3), R(2, 3)])).T))
check("B3.d amplRef (Fin 2) transpose (|Phi+><Phi+|) = SWAP/2, singlet value -1 (|v|^2 = 2): not positive",
      zero(out - SWAP / 2) and (sv.H * out * sv)[0, 0] == -1)

# ---------------------------------------------------------------- B3.e Kraus closure under amplification
K1, K2 = rand_gauss(2), rand_gauss(2)
Phi = lambda X: K1 * X * K1.H + K2 * X * K2.H  # noqa: E731
Msym = Matrix(4, 4, lambda i, j: sp.Symbol(f"y{i}_{j}"))
I2 = eye(2)
rhs = L.kron(I2, K1) * Msym * L.kron(I2, K1).H + L.kron(I2, K2) * Msym * L.kron(I2, K2).H
check("B3.e amplRef (conj K1 + conj K2) = conj (1 (x) K1) + conj (1 (x) K2) (kernel amplRef_conjChannel RE:170)",
      zero(amplRef(Phi, 2, 2)(Msym) - rhs))

ok = L.summary("a3_bridge")
print("VERDICT " + ("A3-BRIDGE-INSTANCES-EXACT" if ok else "A3-NOT-RENDERED"))
sys.exit(0 if ok else 1)
