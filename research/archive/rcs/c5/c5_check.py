"""RELC-SELECT-1 design, C5 at d = 5: exact checks of every identity and inequality step the Lean draft
RelcSelectC5.lean relies on.  Exact sympy / Fraction arithmetic only; the random rational sampling in (G) is a
sanity check, not a certificate.

Lean conventions (OIBridge.CompositeDimension): HVec 5 indices 0..5, index 0 the unit, index j+1 coordinate j;
W 5 entries w[mu][nu] (mu control, nu target); prodState x y = hom x hom y^T; pairVal a b w = a^T w b;
actT N w = w homMap(N)^T; actC N w = homMap(N) w; frame: G(prod(c_a, c_b)) = prod(c_a, c_{a+b}), c_0 = z, c_1 = -z.

(A) the tables pcC5 / ptC5 are PARSED from the Lean file and sgnC5 is transcribed from its condition; the gate
    they define equals NB-1's frozen J/K map (native_gate_ball_probe.jk_map, read at L) and REL-T's jk_gate(5).
(B) decide-lemmas: pc_pc, pt_pt, sgn*sgn = 1, oddC5(pt) = oddC5.
(C) IsNot(eball 5, z5, nC5), frame, relT, G^2 = I, relC fails; the witness entries 1 and -1.
(D) the value identity of prodEffVal_gC5_prodState (polynomial identity).
(E) the SOS / ring identities behind selC5_cs, selC5_cauchy2, selC5_besselJ, selC5_besselK, selC5_mix,
    selC5_target, selC5_ctrl, selC5_core.
(F) countercontrols: the same evaluator reproduces gJ5_value = -1/10; a one-sign mutation breaks the value
    identity; the mutation J := id keeps frame, relT and G^2 = I; the Bessel bound fails for a non-complex-structure
    (symmetric swap) second term.
(G) exact rational sampling of the value on products of sphere points and boundary effects (sanity only), and a
    sampled exact negative value for the J := id mutation (the evaluator sees non-positivity).
(H) every `have ... := by ring` identity in the Lean text, parsed and checked as a polynomial identity.
"""
import ast, os, re, sys, random
from fractions import Fraction as Fr
from sympy import symbols, expand, Matrix, Rational, zeros, eye, diag

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(os.path.dirname(HERE))
LEAN = os.path.join(HERE, "RelcSelectC5.lean")
NB1 = os.path.join(SCR, "wt-L", "verification", "lean", "native_gate_ball_probe.py")
RELT = os.path.join(SCR, "relt")

checks = []


def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name, flush=True)


# ------------------------------------------------------------------ (A) tables from the Lean text
src = open(LEAN).read()


def parse_table(name):
    m = re.search(r"def %s : Fin 6 → Fin 6 → Fin 6\n((?:  \|.*\n)+)" % name, src)
    arms = re.findall(r"\|\s*(\d),\s*(\d)\s*=>\s*(\d)", m.group(1))
    tab = {(int(a), int(b)): int(c) for a, b, c in arms}
    assert len(tab) == 36 and len(arms) == 36
    return tab


PC = parse_table("pcC5")
PT = parse_table("ptC5")
check("A Lean sgnC5 condition text is the transcribed one",
      "if ((μ = 1 ∨ μ = 3) ∧ (ν = 4 ∨ ν = 5)) ∨ ((μ = 2 ∨ μ = 4) ∧ (ν = 2 ∨ ν = 3)) then -1 else 1" in src)


def SG(mu, nu):
    return -1 if ((mu in (1, 3)) and (nu in (4, 5))) or ((mu in (2, 4)) and (nu in (2, 3))) else 1


ODD = [False, False, True, True, True, True]
check("A Lean oddC5 text", "| 0 => false | 1 => false | 2 => true | 3 => true | 4 => true | 5 => true" in src)
n = 6


def apply_lean(w):
    """gC5Fun w mu nu = sgnC5 mu nu * w (pcC5 mu nu) (ptC5 mu nu)"""
    return Matrix(n, n, lambda mu, nu: SG(mu, nu) * w[PC[(mu, nu)], PT[(mu, nu)]])


def as_matrix(fun):
    cols = []
    for k in range(n * n):
        E = zeros(n, n); E[k // n, k % n] = 1
        out = fun(E)
        cols.append(Matrix([out[i, j] for i in range(n) for j in range(n)]))
    return Matrix.hstack(*cols)


G = as_matrix(apply_lean)

# NB-1's frozen J/K map: extract the needed function definitions with ast (no execution of the probe's checks)
nb1_tree = ast.parse(open(NB1).read())
want = {"zeros", "eye", "kron", "corners", "jk_map"}
mod = ast.Module(body=[nd for nd in nb1_tree.body if isinstance(nd, ast.FunctionDef) and nd.name in want], type_ignores=[])
ns = {"Fr": Fr}
exec(compile(mod, NB1, "exec"), ns)
G5nb, Nd5nb, _, _ = ns["jk_map"]()
Gnb = Matrix(36, 36, lambda i, j: Rational(G5nb[i][j].numerator, G5nb[i][j].denominator))
check("A Lean tables define NB-1's frozen d = 5 J/K map (native_gate_ball_probe.jk_map at L)", Gnb == G)
check("A NB-1's N = diag(1,1,-1,-1,-1,-1) is homMap nC5", list(Nd5nb) == [1 if not o else -1 for o in ODD])

# REL-T jk_gate(5): extract from relt_pos_exact.py with ast; relt_common is side-effect free
sys.path.insert(0, RELT)
import relt_common  # noqa: E402
rtree = ast.parse(open(os.path.join(RELT, "relt_pos_exact.py")).read())
rmod = ast.Module(body=[nd for nd in rtree.body if isinstance(nd, ast.FunctionDef) and nd.name == "jk_gate"], type_ignores=[])
rns = dict(vars(relt_common))
exec(compile(rmod, "relt_pos_exact.py", "exec"), rns)
Grt = rns["jk_gate"](5)[0]
check("A Lean tables define REL-T's C_5 (relt_pos_exact.jk_gate(5))", Grt == G)

# ------------------------------------------------------------------ (B) decide lemmas
check("B pcC5_pcC5", all(PC[(PC[(a, b)], PT[(a, b)])] == a for a in range(6) for b in range(6)))
check("B ptC5_ptC5", all(PT[(PC[(a, b)], PT[(a, b)])] == b for a in range(6) for b in range(6)))
check("B sgnC5_mul_sgnC5", all(SG(a, b) * SG(PC[(a, b)], PT[(a, b)]) == 1 for a in range(6) for b in range(6)))
check("B oddC5_ptC5", all(ODD[PT[(a, b)]] == ODD[b] for a in range(6) for b in range(6)))

# ------------------------------------------------------------------ (C) IsNot, frame, relations
cC5 = [(-1 if ODD[j + 1] else 1) for j in range(5)]
N = diag(*cC5)
z5 = Matrix([0, 0, 0, 0, 1])
check("C nC5 = diag(1,-1,-1,-1,-1)", cC5 == [1, -1, -1, -1, -1])
check("C IsNot: unit, involution, orthogonal (preserves eball), flips",
      sum(v ** 2 for v in z5) == 1 and N * N == eye(5) and N.T * N == eye(5) and N * z5 == -z5)
check("C relt_common.isNot agrees", all(relt_common.isNot(z5, N).values()))
check("C frame", relt_common.frame(G, z5))
check("C relT", relt_common.relT(G, N))
check("C relC fails", not relt_common.relC(G, N))
check("C G^2 = I (gC5.symm = gC5)", G * G == eye(36))
check("C eigenspaces of homMap nC5: (2, 4) (unbalanced)", relt_common.eig_dims(N) == (2, 4))
Nh = relt_common.homMap(N)
E33 = zeros(6, 6); E33[3, 3] = 1
lhs = Nh * apply_lean(Nh * E33)        # actC N (G (actC N w))
rhs = apply_lean(E33) * Nh.T           # actT N (G w)
check("C witness: actC nC5 (gC5 (actC nC5 (entW 3 3))) 4 4 = 1", lhs[4, 4] == 1)
check("C witness: actT nC5 (gC5 (entW 3 3)) 4 4 = -1", rhs[4, 4] == -1)

# ------------------------------------------------------------------ (D) the value identity
e = symbols("e0:6"); f = symbols("f0:6"); x = symbols("x0:5"); y = symbols("y0:5")
hx = Matrix([1] + list(x)); hy = Matrix([1] + list(y))
W_ = apply_lean(hx * hy.T)
val = expand((Matrix([e]) * W_ * Matrix(f))[0, 0])
p = f[0] + f[1] * y[0]
m = f[2] * y[1] + f[3] * y[2] + f[4] * y[3] + f[5] * y[4]
al = f[0] * y[0] + f[1]
be = f[5] * y[1] + f[4] * y[2] - f[3] * y[3] - f[2] * y[4]
s1 = e[1] * x[0] + e[2] * x[1] + e[3] * x[2] + e[4] * x[3]
s2 = e[2] * x[0] - e[1] * x[1] + e[4] * x[2] - e[3] * x[3]
rhsV = (e[0] + x[4] * e[5]) * p + (e[5] + x[4] * e[0]) * m + s1 * al + s2 * be
check("D prodEffVal_gC5_prodState: value = (e0+x4 e5)p + (e5+x4 e0)m + s1 al + s2 be", expand(val - rhsV) == 0)
check("D p + m = <f, hom y>, p - m = <f, homMap nC5 (hom y)>",
      expand(p + m - (Matrix([f]) * hy)[0, 0]) == 0 and expand(p - m - (Matrix([f]) * Nh * hy)[0, 0]) == 0)
check("D the Lean statement text carries this RHS",
      "(ehom e 2 * x 0 - ehom e 1 * x 1 + ehom e 4 * x 2 - ehom e 3 * x 3)" in src
      and "(ehom f 5 * y 1 + ehom f 4 * y 2 - ehom f 3 * y 3 - ehom f 2 * y 4)" in src
      and "(ehom e 0 + x 4 * ehom e 5) * (ehom f 0 + ehom f 1 * y 0)" in src
      and "(ehom f 0 * y 0 + ehom f 1)" in src)

# ------------------------------------------------------------------ (E) identities behind the real lemmas
a = symbols("a0:5"); b = symbols("b0:5")
lag = sum((a[i] * b[j] - a[j] * b[i]) ** 2 for i in range(5) for j in range(i + 1, 5))
check("E selC5_cs: (sum a^2)(sum b^2) - (a.b)^2 = sum_{i<j} (a_i b_j - a_j b_i)^2",
      expand(sum(t ** 2 for t in a) * sum(t ** 2 for t in b) - sum(a[i] * b[i] for i in range(5)) ** 2 - lag) == 0)
S1, S2, A_, B_ = symbols("s1 s2 al be")
check("E selC5_cauchy2: (s1^2+s2^2)(a^2+b^2) - (s1 a + s2 b)^2 = (s1 b - s2 a)^2",
      expand((S1 ** 2 + S2 ** 2) * (A_ ** 2 + B_ ** 2) - (S1 * A_ + S2 * B_) ** 2 - (S1 * B_ - S2 * A_) ** 2) == 0)
a0, a1, a2, a3 = a[:4]; b0, b1, b2, b3 = b[:4]
A4 = a0 ** 2 + a1 ** 2 + a2 ** 2 + a3 ** 2; B4 = b0 ** 2 + b1 ** 2 + b2 ** 2 + b3 ** 2
dot4 = a0 * b0 + a1 * b1 + a2 * b2 + a3 * b3
Jt = a1 * b0 - a0 * b1 + a3 * b2 - a2 * b3
J1 = -a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1
J2 = -a0 * b3 - a1 * b2 + a2 * b1 + a3 * b0
check("E selC5_besselJ: A4 B4 - dot^2 - (a.Jb)^2 = J1^2 + J2^2", expand(A4 * B4 - dot4 ** 2 - Jt ** 2 - J1 ** 2 - J2 ** 2) == 0)
Kt = a3 * b0 + a2 * b1 - a1 * b2 - a0 * b3
K1 = -a0 * b1 + a1 * b0 - a2 * b3 + a3 * b2
K2 = -a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1
check("E selC5_besselK: A4 B4 - dot^2 - (a.Kb)^2 = K1^2 + K2^2", expand(A4 * B4 - dot4 ** 2 - Kt ** 2 - K1 ** 2 - K2 ** 2) == 0)
check("E the Lean besselJ/besselK texts carry these terms",
      "(a1 * b0 - a0 * b1 + a3 * b2 - a2 * b3)" in src and "sq_nonneg (-a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1)" in src
      and "sq_nonneg (-a0 * b3 - a1 * b2 + a2 * b1 + a3 * b0)" in src
      and "(a3 * b0 + a2 * b1 - a1 * b2 - a0 * b3)" in src and "sq_nonneg (-a0 * b1 + a1 * b0 - a2 * b3 + a3 * b2)" in src)
check("E s2 is besselJ's second term at a = (e1..e4), b = (x0..x3)",
      expand(Jt.subs({a0: e[1], a1: e[2], a2: e[3], a3: e[4], b0: x[0], b1: x[1], b2: x[2], b3: x[3]}, simultaneous=True) - s2) == 0)
check("E be is besselK's second term at a = (f2..f5), b = (y1..y4)",
      expand(Kt.subs({a0: f[2], a1: f[3], a2: f[4], a3: f[5], b0: y[1], b1: y[2], b2: y[3], b3: y[4]}, simultaneous=True) - be) == 0)
Am, Bm, U = symbols("A B u")
check("E selC5_mix: (A+B)^2 - (2u)^2 = (A-B)^2 + 4(AB - u^2)",
      expand((Am + Bm) ** 2 - (2 * U) ** 2 - (Am - Bm) ** 2 - 4 * (Am * Bm - U ** 2)) == 0)
f0, f1 = f[0], f[1]
check("E selC5_target hid: (f0+f1 y0)^2 - (f0 y0+f1)^2 = (f0^2-f1^2)(1-y0^2)",
      expand((f0 + f1 * y[0]) ** 2 - (f0 * y[0] + f1) ** 2 - (f0 ** 2 - f1 ** 2) * (1 - y[0] ** 2)) == 0)
# selC5_target's minus branch: cs with b = (y0, -y1, ...) has the same sum of squares and the sum is f1 y0 - m'
check("E selC5_target hminus: the cs instance at (y0,-y1,..,-y4) has LHS (f1 y0 - (f2y1+..))^2 and the same norm",
      expand((f1 * y[0] + sum(f[i + 1] * (-y[i]) for i in range(1, 5))) ** 2 - (f1 * y[0] - m) ** 2) == 0)
E0, E5, X4, P, M, AL, BE, s1s, s2s = symbols("e0 e5 x4 p m al be s1 s2")
Aexp = (1 + X4) * (E0 + E5) * (P + M); Bexp = (1 - X4) * (E0 - E5) * (P - M)
check("E selC5_ctrl hprod: (e0^2-e5^2)(1-x4^2)(p^2-m^2) = A B",
      expand((E0 ** 2 - E5 ** 2) * (1 - X4 ** 2) * (P ** 2 - M ** 2) - Aexp * Bexp) == 0)
check("E selC5_ctrl hsum: A + B + 2u = 2 * value",
      expand(Aexp + Bexp + 2 * (s1s * AL + s2s * BE)
             - 2 * ((E0 + X4 * E5) * P + (E5 + X4 * E0) * M + s1s * AL + s2s * BE)) == 0)

# ------------------------------------------------------------------ (F) countercontrols
# gJ5 (landed ParityNot) at its witness: -1/10, with the same pairing evaluator
odd5 = [False, False, False, True, True, True]; perm5 = [5, 3, 4, 1, 2, 0]
gJ5 = lambda w: Matrix(n, n, lambda mu, nu: w[perm5[mu], nu] if odd5[nu] else w[mu, nu])
x5 = [1, 0, 0, 0, 0]; w5 = [0, 0, Rational(-3, 5), 0, Rational(-4, 5)]; zz5 = [0, 0, 0, 0, 1]
sharp = lambda v: Matrix([Rational(1, 2)] + [Rational(t, 1) / 2 for t in v])
hom_ = lambda v: Matrix([1] + list(v))
vJ5 = (sharp(w5).T * gJ5(hom_(x5) * hom_(zz5).T) * sharp(zz5))[0, 0]
check("F countercontrol: gJ5_value = -1/10 reproduced", vJ5 == Rational(-1, 10))
# mutation 1: flip the sign of one entry -> relT may survive but the value identity fails
SGm = lambda mu, nu: -SG(mu, nu) if (mu, nu) == (1, 4) else SG(mu, nu)
apply_m = lambda w: Matrix(n, n, lambda mu, nu: SGm(mu, nu) * w[PC[(mu, nu)], PT[(mu, nu)]])
valm = expand((Matrix([e]) * apply_m(hx * hy.T) * Matrix(f))[0, 0])
check("F countercontrol: a one-sign mutation breaks the value identity", expand(valm - rhsV) != 0)
# mutation 2: replace J by the identity on the control (pc := mu on every column, signs dropped): still a frame +
# relT gate, so only positivity can reject it
PCm = {(mu, nu): (PC[(mu, nu)] if mu in (0, 5) else mu) for mu in range(6) for nu in range(6)}
SGm2 = lambda mu, nu: 1
apply_m2 = lambda w: Matrix(n, n, lambda mu, nu: SGm2(mu, nu) * w[PCm[(mu, nu)], PT[(mu, nu)]])
Gm2 = as_matrix(apply_m2)
check("F mutation J := id keeps frame, relT and G^2 = I (so the evaluator, not the relations, must catch it)",
      relt_common.frame(Gm2, z5) and relt_common.relT(Gm2, N) and Gm2 * Gm2 == eye(36))
# the second Bessel term must come from a complex structure: with the symmetric swap it is false
Sw = a1 * b0 + a0 * b1 + a3 * b2 + a2 * b3
pt_ = {a0: 1, a1: 1, a2: 0, a3: 0, b0: 1, b1: 1, b2: 0, b3: 0}
check("F countercontrol: (a.b)^2 + (a.Sb)^2 <= |a|^2|b|^2 fails for the symmetric swap S (value 8 > 4)",
      (dot4 ** 2 + Sw ** 2).subs(pt_) == 8 and (A4 * B4).subs(pt_) == 4)

# ------------------------------------------------------------------ (G) sampling (sanity only, not a certificate)
rng = random.Random(20261007)


def sphere(d):
    t = [Fr(rng.randint(-9, 9), rng.randint(1, 9)) for _ in range(d - 1)]
    s2_ = sum(v * v for v in t)
    return [2 * v / (1 + s2_) for v in t] + [(s2_ - 1) / (1 + s2_)]


def evalW(apply_fun, xv, yv, ev, fv):
    w = Matrix([1] + xv) * Matrix([1] + yv).T
    out = apply_fun(w)
    return sum(ev[i] * out[i, j] * fv[j] for i in range(6) for j in range(6))


apply_fast = lambda w: [[SG(mu, nu) * w[PC[(mu, nu)], PT[(mu, nu)]] for nu in range(6)] for mu in range(6)]
apply_fast_m2 = lambda w: [[w[PCm[(mu, nu)], PT[(mu, nu)]] for nu in range(6)] for mu in range(6)]


def evalF(apply_fun, xv, yv, ev, fv):
    hxv = [Fr(1)] + xv; hyv = [Fr(1)] + yv
    w = Matrix(6, 6, lambda i, j: Rational(hxv[i].numerator, hxv[i].denominator) * Rational(hyv[j].numerator, hyv[j].denominator))
    out = apply_fun(w)
    return sum(Rational(ev[i].numerator, ev[i].denominator) * out[i][j] * Rational(fv[j].numerator, fv[j].denominator)
               for i in range(6) for j in range(6))


worst = None
for _ in range(400):
    xv = sphere(5); yv = sphere(5)
    ev = [Fr(1)] + sphere(5); fv = [Fr(1)] + sphere(5)
    v = evalF(apply_fast, xv, yv, ev, fv)
    worst = v if worst is None or v < worst else worst
check("G sampled exact values of gC5 on sphere products / boundary effects >= 0 (min %s)" % worst, worst >= 0)
# targeted sampling for the J := id mutation: x tangent and unit, control effect (1, -x_T, 0) so s1 = s2 = -1
worst_m2 = None; witness = None
for _ in range(400):
    xt = sphere(4); xv = xt + [Fr(0)]
    ev = [Fr(1)] + [-t for t in xt] + [Fr(0)]
    yv = sphere(5); fv = [Fr(1)] + sphere(5)
    vm = evalF(apply_fast_m2, xv, yv, ev, fv)
    if worst_m2 is None or vm < worst_m2:
        worst_m2, witness = vm, (xv, yv, ev, fv)
check("G countercontrol: the J := id mutation takes a negative exact value (min %s)" % worst_m2, worst_m2 < 0)
xv, yv, ev, fv = witness
check("G the same witness is nonnegative for gC5 (value %s)" % evalF(apply_fast, xv, yv, ev, fv),
      evalF(apply_fast, xv, yv, ev, fv) >= 0)


# ------------------------------------------------------------------ (H) every `:= by ring` identity in the Lean text
from sympy import sympify
ring_ids = re.findall(r"have (\w+) : ((?:(?!:=).)*?) :=\s*by\s*ring\b", src, re.S)
ok_all = True
for name, body in ring_ids:
    txt = " ".join(body.split())
    lhs_t, rhs_t = txt.split(" = ")
    conv = lambda t: sympify(t.replace("^", "**"))
    okk = expand(conv(lhs_t) - conv(rhs_t)) == 0
    ok_all &= okk
    print("   ring identity %-6s %s" % (name, "ok" if okk else "FAILS"))
selftest = expand(sympify("(a+b)**2") - sympify("a**2 + b**2")) != 0
check("H parser self-test: a false identity is rejected", selftest)
check("H all %d `have ... := by ring` identities of the Lean draft hold as polynomial identities" % len(ring_ids),
      ok_all and len(ring_ids) >= 10)
# the abstract lemmas' hypotheses -> conclusions on random rational instances (sanity, not a certificate)
def qr():
    return Fr(rng.randint(-20, 20), rng.randint(1, 7))
bad = 0
for _ in range(3000):
    A_v, B_v = abs(qr()), abs(qr())
    u_v = qr()
    if u_v * u_v <= A_v * B_v and not (A_v + B_v + 2 * u_v >= 0):
        bad += 1
check("H selC5_mix: no rational counterexample in 3000 samples", bad == 0)

npass = sum(1 for _, c in checks if c)
print("c5_check: %d/%d checks pass" % (npass, len(checks)))
sys.exit(0 if npass == len(checks) else 1)
