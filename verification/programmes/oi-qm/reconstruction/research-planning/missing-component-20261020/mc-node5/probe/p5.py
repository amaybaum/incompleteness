"""Node 5 probe: necessity, irredundancy and insufficiency of the primitive-level clauses of P*,
the PFR flow, the O-B residue under full control, and the M1 / G6 controls.

Exact arithmetic only (SymPy rationals, Gaussian rationals, sqrt(2) as an algebraic number).
Run: python3 -I -B p5.py   (SymPy 1.14.0)
Every check prints PASS or FAIL; the run ends with the totals.
"""
import itertools
import sympy as sp

I = sp.I
R2 = sp.sqrt(2)
RES = []


def check(tag, cond, note=""):
    RES.append((tag, bool(cond)))
    print(("PASS " if cond else "FAIL ") + tag + ((" : " + note) if note else ""))


def M(rows):
    return sp.Matrix(rows)


def simp(A):
    return A.applyfunc(lambda z: sp.nsimplify(sp.simplify(sp.expand(z)), [R2]) if z != 0 else z)


def is_zero(A):
    return all(sp.simplify(z) == 0 for z in A)


def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out


def rm(A):  # row-monomial: at most one nonzero entry per row
    return all(sum(1 for j in range(A.cols) if sp.simplify(A[i, j]) != 0) <= 1 for i in range(A.rows))


def cm(A):  # column-monomial
    return rm(A.T)


def monomial(A):
    return A.rows == A.cols and rm(A) and cm(A)


def prop_scalar(A, B):
    """A = c B for some nonzero scalar c (exact)."""
    idx = [(i, j) for i in range(B.rows) for j in range(B.cols) if sp.simplify(B[i, j]) != 0]
    if not idx:
        return False
    i, j = idx[0]
    c = sp.simplify(A[i, j] / B[i, j])
    return c != 0 and is_zero(A - c * B)


def real_up_to_scalar(A):
    """exists unimodular c with c*A real (exact)."""
    idx = [(i, j) for i in range(A.rows) for j in range(A.cols) if sp.simplify(A[i, j]) != 0]
    if not idx:
        return True
    i, j = idx[0]
    a = A[i, j]
    c = sp.conjugate(a) / sp.sqrt(sp.simplify(a * sp.conjugate(a)))
    B = (c * A).applyfunc(lambda z: sp.simplify(sp.expand(z)))
    return all(sp.simplify(sp.im(z)) == 0 for z in B)


def unitary_up_to_scalar(A):
    if A.rows != A.cols:
        return False
    G = simp(A.H * A)
    return prop_scalar(G, sp.eye(A.rows)) if not is_zero(G) else False


def ones(n):
    return sp.ones(n, 1)


X = M([[0, 1], [1, 0]]); Z = M([[1, 0], [0, -1]]); Id2 = sp.eye(2)
CNOT12 = M([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])  # control first factor
SWAP = M([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
CNOT21 = SWAP * CNOT12 * SWAP
ket0 = M([1, 0]); ket1 = M([0, 1])

# ---------------------------------------------------------------------------------------------
print("== Block P: the PFR transition flow at level two carries U, M, O and R in one family")
t, s = sp.symbols('t s', real=True)
Xab = sp.zeros(4); Xab[0, 1] = Xab[1, 0] = 1
Pab = sp.diag(1, 1, 0, 0)
F = lambda tt: sp.eye(4) + (sp.cos(tt) - 1) * Pab - I * sp.sin(tt) * Xab   # exp(-i t X_ab)
# exp check: generator and group law
check("P0a flow(t) is exp(-itX_ab): F(0)=1, F'(0)=-iX_ab, F(t)F(s)=F(t+s)",
      is_zero(F(0) - sp.eye(4)) and is_zero(sp.diff(F(t), t).subs(t, 0) + I * Xab)
      and is_zero(sp.simplify(sp.expand_trig(sp.expand(F(t) * F(s) - F(t + s))))))
check("P0b flow(t) unitary for all real t", is_zero(sp.simplify(F(t).H * F(t) - sp.eye(4))))
Fq = F(sp.pi / 4); Fh = F(sp.pi / 2)
check("P1 (M) flow(pi/4) is not monomial (not RM, not CM)", (not rm(Fq)) and (not cm(Fq)))
check("P2 (O) flow(pi/2) moves the all-ones ray (third point present)", not prop_scalar(Fh * ones(4), ones(4)),
      str(list(Fh * ones(4))))
check("P3 (R) flow(pi/4) is not a scalar multiple of a real matrix", not real_up_to_scalar(Fq))
check("P4 (U) distinct times give distinct rays: flow(pi/4) not prop. flow(pi/6)",
      not prop_scalar(Fq, F(sp.pi / 6)))
F1 = sp.eye(2) * sp.cos(t) - I * sp.sin(t) * X
check("P5 level one (two states): the same flow fixes the all-ones ray for every t",
      is_zero(sp.simplify(F1 * ones(2) - (sp.cos(t) - I * sp.sin(t)) * ones(2))))

# ---------------------------------------------------------------------------------------------
print("== Block M: the row/column-monomial criterion (clause M)")
# M1: pattern-level closure, exhaustive over all 0/1 3x3 column-monomial and row-monomial patterns
cols = [tuple(1 if r == k else 0 for r in range(3)) for k in range(3)] + [(0, 0, 0)]
CMpats = [sp.Matrix(3, 3, lambda i, j, c=c: c[j][i]) for c in itertools.product(cols, repeat=3)]
ok_cm = all(cm(A * B) for A in CMpats for B in CMpats)
RMpats = [A.T for A in CMpats]
ok_rm = all(rm(A * B) for A in RMpats for B in RMpats)
check("M1a CM patterns closed under products (all 64x64 3x3 pairs)", ok_cm and len(CMpats) == 64)
check("M1b RM patterns closed under products (all 64x64 3x3 pairs)", ok_rm)
check("M1c tensoring with the identity keeps CM and RM (all 64 patterns, I_2)",
      all(cm(kron(A, Id2)) and cm(kron(Id2, A)) and rm(kron(A.T, Id2)) for A in CMpats))
check("M1d an invertible CM (or RM) square matrix is monomial: all 64 patterns",
      all((A.det() == 0) or monomial(A) for A in CMpats))

# M2: the CM countermodel. It satisfies every PLAN form clause (non-configuration tests: k4 dropped;
# a non-OnesNormal primitive; an uncountable non-monomial family of test Kraus operators; non-real)
w = lambda c, s_: M([[c, s_]])                      # bra <w| for real w = (c, s)
yb = M([[1, -I]]) / R2                              # <+i|
u = (3 + 4 * I) / 5
destr = [w(sp.Rational(3, 5), sp.Rational(4, 5)), w(sp.Rational(5, 13), sp.Rational(12, 13)),
         w(1 / R2, 1 / R2), yb, w(-sp.Rational(4, 5), sp.Rational(3, 5))]
phases = [sp.diag(1, u), sp.diag(1, I), Z]
# primitive Kraus operators as maps between the 1-token (dim 2) and 2-token (dim 4) spaces
prims = []
for d in destr:   # destructive test on token 1 of a 2-token register: dim 4 -> dim 2
    prims.append(("destr", kron(d, Id2)))
for p in phases:
    prims.append(("phase1", kron(p, Id2))); prims.append(("phase2", kron(Id2, p))); prims.append(("phase", p))
for name, g in [("CNOT12", CNOT12), ("CNOT21", CNOT21), ("SWAP", SWAP), ("X1", kron(X, Id2)), ("X", X)]:
    prims.append((name, g))
prims.append(("attach0", kron(ket0, Id2)))          # dim 2 -> dim 4 (configuration attach)
prims.append(("proj0", kron(ket0 * ket0.T, Id2)))   # configuration readout branch
check("M2a every primitive of the CM alphabet is CM", all(cm(K) for _, K in prims))
check("M2b the alphabet meets PLAN's clauses: a non-monomial test Kraus, a ray-moving Z, a non-real phase",
      (not rm(kron(destr[0], Id2))) and (not prop_scalar(Z * ones(2), ones(2))) and not real_up_to_scalar(sp.diag(1, u)))
# BFS over words up to length 4 (compatible dimensions), on both spaces
by_dom = {2: [K for _, K in prims if K.cols == 2], 4: [K for _, K in prims if K.cols == 4]}
frontier = [sp.eye(2), sp.eye(4)]
seen = 0; allcm = True; uni_nonmono = 0; uni_count = 0
for depth in range(3):
    nxt = []
    for W in frontier:
        for K in by_dom[W.rows]:
            P_ = simp(K * W)
            if is_zero(P_):
                continue
            seen += 1
            allcm &= cm(P_)
            if P_.rows == P_.cols and unitary_up_to_scalar(P_):
                uni_count += 1
                if not monomial(P_):
                    uni_nonmono += 1
            nxt.append(P_)
    frontier = nxt
check("M2c every word (depth <= 3) over the CM alphabet is CM", allcm, f"{seen} words")
check("M2d every unitary-up-to-scalar word is monomial (no Hadamard-type channel)", uni_nonmono == 0 and uni_count > 0,
      f"{uni_count} unitary words")
# M3: positive control (can fail): a coherent preparation |+> (RM, not CM) with the destructive Y test
plus = M([1, 1]) / R2
Kb = {}
for sgn in (+1, -1):
    bra = M([[1, -sgn * I]]) / R2                       # <+-i|
    # data token = factor 1, ancilla = factor 2; attach |+>, CNOT anc->data, destructive test on data
    K_ = kron(bra, Id2) * CNOT21 * kron(Id2, plus)      # dim 2 (data) -> dim 2 (ancilla carries output)
    Kb[sgn] = simp(K_)
check("M3a the attach of |+> is RM and not CM; the destructive Y test is CM and not RM",
      rm(kron(Id2, plus)) and not cm(kron(Id2, plus)) and cm(kron(yb, Id2)) and not rm(kron(yb, Id2)))
Rp = (Id2 - I * X) / R2; Rm = (Id2 + I * X) / R2
check("M3b branches are prop. to exp(-i pi/4 X) and exp(+i pi/4 X): non-monomial unitaries",
      prop_scalar(Kb[1], Rp) and prop_scalar(Kb[-1], Rm) and not monomial(Rp))
corr = simp(X * Kb[-1])
check("M3c native X on outcome -i makes both branches prop. to the same unitary (a deterministic channel)",
      prop_scalar(corr, Kb[1]) and is_zero(simp(Kb[1].H * Kb[1] + corr.H * corr - Id2)))
check("M3d the composite channel is complete (sum K^H K = 1 over both branches)",
      is_zero(simp(Kb[1].H * Kb[1] + Kb[-1].H * Kb[-1] - Id2)))

# ---------------------------------------------------------------------------------------------
print("== Block R: the reality clause")
Ry = lambda c, s_: M([[c, -s_], [s_, c]])
R35 = Ry(sp.Rational(3, 5), sp.Rational(4, 5)); R513 = Ry(sp.Rational(5, 13), sp.Rational(12, 13))
check("R1 the real rotation family meets U-type, M and O: non-monomial, moves the all-ones ray",
      (not monomial(R35)) and not prop_scalar(R35 * ones(2), ones(2)), str(list(R35 * ones(2))))
realprims = [kron(R35, Id2), kron(Id2, R513), kron(Z, Id2), CNOT12, CNOT21, SWAP,
             kron(M([1, 1]) * M([[1, 1]]) / 2, Id2), kron(ket0 * ket0.T, Id2)]
frontier = [sp.eye(4)]; allreal = True; nw = 0
for depth in range(3):
    nxt = []
    for W in frontier:
        for K in realprims:
            P_ = simp(K * W); nw += 1
            allreal &= all(sp.simplify(sp.im(z)) == 0 for z in P_)
            nxt.append(P_)
    frontier = nxt
check("R2 every word (depth <= 3) over the real alphabet is real", allreal, f"{nw} words")
S = sp.diag(1, I)
check("R3 the quarter phase S is not a scalar multiple of a real matrix", not real_up_to_scalar(S))
check("R4 (can fail) the M3 gadget output exp(-i pi/4 X) is not real up to scalar", not real_up_to_scalar(Rp))
check("R5 Choi of a real-Kraus channel is real symmetric (instance: Ad R35)",
      all(sp.im(z) == 0 for z in (lambda v: v * v.T)(sp.Matrix([R35[i, j] for i in range(2) for j in range(2)]))))

# ---------------------------------------------------------------------------------------------
print("== Block O: OnesNormal of the primitives")
Pw = lambda v: (v * v.H) / sp.simplify((v.H * v)[0])
vw = M([sp.Rational(3, 5), sp.Rational(4, 5)]); vwp = M([-sp.Rational(4, 5), sp.Rational(3, 5)])
vy = M([1, I]); vyp = M([1, -I])
check("O1 Lueders tests in a real basis and in the Y basis: sum K^H 1 = 1",
      is_zero(simp(Pw(vw).H * ones(2) + Pw(vwp).H * ones(2) - ones(2)))
      and is_zero(simp(Pw(vy).H * ones(2) + Pw(vyp).H * ones(2) - ones(2))))
check("O2 Z and diag(1,u), u != 1, have K^H 1 off the all-ones ray (non-OnesNormal unitaries)",
      (not prop_scalar(Z.H * ones(2), ones(2))) and not prop_scalar(sp.diag(1, u).H * ones(2), ones(2)))
check("O3 the real rotation R35 is a non-OnesNormal unitary", not prop_scalar(R35.H * ones(2), ones(2)))

# ---------------------------------------------------------------------------------------------
print("== Block B: the O-B residue under full control")
def Gamma2(A):  # partial transpose on the second token of a 4x4 matrix
    B = sp.zeros(4)
    for a, b, c, d in itertools.product(range(2), repeat=4):
        B[2 * a + b, 2 * c + d] = A[2 * a + d, 2 * c + b]
    return B
bell = M([1, 0, 0, 1]) / R2
Pbell = bell * bell.H
Xg = Gamma2(Pbell)
sx = X; sy = M([[0, -I], [I, 0]]); sz = Z
zF = (sp.eye(4) + kron(sx, sz) + kron(sy, sy) - kron(sz, sx)) / 4
fixtures = {"Gamma(Bell) in Gamma(Q3)": Xg, "z_{1,1} in K(Z_F)": zF, "SWAP in maxCone": SWAP}
def householder_to_e0(psi):
    """exact unitary U with U psi = e0 (psi unit, first entry real >= 0 after phase fix)."""
    n = psi.rows
    e0 = sp.zeros(n, 1); e0[0] = 1
    a = psi[0]
    ph = sp.Integer(1) if sp.simplify(a) == 0 else sp.simplify(a / sp.sqrt(sp.simplify(a * sp.conjugate(a))))
    v = simp(psi / ph - e0)       # psi/ph has real nonnegative first entry
    if is_zero(v):
        return sp.eye(n) / ph
    Hh = sp.eye(n) - 2 * v * v.H / sp.simplify((v.H * v)[0])
    return simp(Hh / ph)
for name, A in fixtures.items():
    ev = A.eigenvects()
    neg = [(val, vecs) for val, mult, vecs in ev if sp.simplify(val) < 0]
    val, vecs = neg[0]
    psi = vecs[0]; psi = simp(psi / sp.sqrt(sp.simplify((psi.H * psi)[0])))
    U = householder_to_e0(psi)
    okU = is_zero(simp(U.H * U - sp.eye(4))) and is_zero(simp(U * psi - M([1, 0, 0, 0])))
    img = simp(U * A * U.H)
    test = img[0, 0]   # product test |0><0| x |0><0|
    check(f"B1 {name}: exact unitary U maps the negative eigenvector to |00>; product test on U X U^H = {sp.simplify(test)} < 0",
          okU and sp.simplify(test - val) == 0 and sp.simplify(test) < 0)
# negative control: PSD elements are never driven negative by the same unitaries
Us = []
for name, A in fixtures.items():
    ev = A.eigenvects(); neg = [vecs for val, m, vecs in ev if sp.simplify(val) < 0][0]
    psi = neg[0]; psi = simp(psi / sp.sqrt(sp.simplify((psi.H * psi)[0]))); Us.append(householder_to_e0(psi))
psd = [Pbell, sp.eye(4) / 4, kron(M([[2, 1], [1, 1]]), M([[1, I], [-I, 2]]))]
check("B2 (control) PSD elements stay nonnegative on every product test of the form |ab><ab|, a,b in {0,1,+,+i}",
      all(sp.simplify((kron(a, b).H * simp(U * Pp * U.H) * kron(a, b))[0]) >= 0
          for U in Us for Pp in psd for a in [ket0, ket1, plus, M([1, I]) / R2] for b in [ket0, ket1, plus, M([1, I]) / R2]))
# availability does not imply preservation: CNOT maps SWAP (block-positive) to a non-block-positive element
img = simp(CNOT12 * SWAP * CNOT12.H)
vals = [sp.simplify((kron(a, b).H * img * kron(a, b))[0]) for a in [ket0, ket1, plus, M([1, -1]) / R2, M([1, I]) / R2]
        for b in [ket0, ket1, plus, M([1, -1]) / R2, M([1, I]) / R2]]
check("B3 (P*_A without X-4) CNOT maps SWAP in maxCone outside maxCone: some product test negative", min(vals) < 0,
      f"min {min(vals)}")
check("B4 (X-4 without P*_A) every native pair permutation preserves PSD: spectra of P A P^T equal (Bell instance)",
      all(sp.simplify((Pm * Pbell * Pm.T).charpoly().as_expr() - Pbell.charpoly().as_expr()) == 0
          for Pm in [sp.Matrix(4, 4, lambda i, j, p=p: 1 if p[j] == i else 0) for p in itertools.permutations(range(4))]))
check("B5 Fact B control: CNOT maps Gamma(Bell) outside Gamma(Q3) (its partial transpose is not PSD)",
      min(sp.simplify(e) for e in Gamma2(simp(CNOT12 * Xg * CNOT12.T)).eigenvals()) < 0)

# ---------------------------------------------------------------------------------------------
print("== Block G: M1 negative control and the A1/A2 inertness instance")
# a 1-bit visible + 1-bit hidden substratum; phi = CNOT(h -> v) then SWAP-free; uniform hidden prior
phi = CNOT21  # visible = factor 1, hidden = factor 2: v <- v xor h
proj = [kron(ket0 * ket0.T, Id2), kron(ket1 * ket1.T, Id2)]
mm = lambda v: v * v.H
xproj = [kron(mm(plus), Id2), kron(mm(M([1, -1]) / R2), Id2)]
rho0 = {x0: kron(mm(ket0 if x0 == 0 else ket1), Id2 / 2) for x0 in (0, 1)}
def law(mid):
    out = {}
    for x0 in (0, 1):
        for k1 in (0, 1):
            r1 = phi * rho0[x0] * phi.H
            r1 = mid[k1] * r1 * mid[k1]
            r2 = phi * r1 * phi.H
            for x2 in (0, 1):
                out[(x0, k1, x2)] = sp.simplify((proj[x2] * r2).trace() / 2)
    return out
Lc = law(proj); Lx = law(xproj)
m02 = lambda L: {(a, c): sp.simplify(sum(L[(a, b, c)] for b in (0, 1))) for a in (0, 1) for c in (0, 1)}
check("G1 (can fail) replacing the configuration readout by an X-basis Lueders test changes P(x0, x2)",
      m02(Lc) != m02(Lx), f"{m02(Lc)} vs {m02(Lx)}")
check("G2 configuration readout is non-disturbing on this law: P(x0,x2) with readout equals P(x0,x2) without",
      m02(Lc) == {(a, c): sp.simplify(sum((proj[c] * phi * phi * rho0[a] * phi.H * phi.H).trace() for _ in [0]) / 2)
                   for a in (0, 1) for c in (0, 1)})
n = sp.symbols('n', positive=True, integer=True)
rho = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(1, 2)]])
E = mm(plus)
pn = (1 - 2 ** (-n)) * (Z * rho * Z) + 2 ** (-n) * rho
check("G3 a finite experiment separates Phi_n from Ad Z by exactly 2^-n (|+> prepared, X test)",
      sp.simplify((E * pn).trace() - (E * Z * rho * Z).trace() - 2 ** (-n)) == 0)

print()
npass = sum(1 for _, ok in RES if ok)
print(f"TOTAL {len(RES)} checks: {npass} PASS, {len(RES) - npass} FAIL")
