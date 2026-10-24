"""Exact (sympy) probe: does OI's permutation-unitary representation with a
diagonal hidden prior force BBS classical memory for the two-step process?

Definition used (owner report 2, tagged [rec]; paper unreadable here -> [Q]):
  {E1, E2} has classical memory iff E2 = sum_i Phi_i o I_i for an instrument
  {I_i} and CPTP maps Phi_i.  Read literally this holds for EVERY E2 (one
  outcome, I = id, Phi = E2); the non-vacuous reading adds sum_i I_i = E1
  (the instrument implements the first step; its outcome is the memory).
  Both readings are checked.

All arithmetic exact. No floating point decides anything.
"""
import itertools
import sympy as sp

half = sp.Rational(1, 2)
I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Z = sp.Matrix([[1, 0], [0, -1]])
Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
ket = lambda i, n=2: sp.Matrix([1 if k == i else 0 for k in range(n)])
E = lambda i, j, n=2: ket(i, n) * ket(j, n).T
plus = (ket(0) + ket(1)) / sp.sqrt(2)
minus = (ket(0) - ket(1)) / sp.sqrt(2)
P_plus, P_minus = plus * plus.T, minus * minus.T

def kron(*ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out

def ptrace_H(R, dv, dh):
    """Trace out the second (hidden) factor of a (dv*dh)x(dv*dh) matrix."""
    out = sp.zeros(dv, dv)
    for a in range(dv):
        for b in range(dv):
            out[a, b] = sum(R[a * dh + k, b * dh + k] for k in range(dh))
    return out

def ptrace_V(R, dv, dh):
    out = sp.zeros(dh, dh)
    for a in range(dh):
        for b in range(dh):
            out[a, b] = sum(R[k * dh + a, k * dh + b] for k in range(dv))
    return out

def perm_unitary(phi, dv, dh):
    """U|x,h> = |phi(x,h)>, phi a bijection on range(dv) x range(dh)."""
    D = dv * dh
    U = sp.zeros(D, D)
    imgs = set()
    for x in range(dv):
        for h in range(dh):
            y, g = phi(x, h)
            U[y * dh + g, x * dh + h] = 1
            imgs.add((y, g))
    assert len(imgs) == D, "phi is not a bijection"
    assert sp.simplify(U.T * U - sp.eye(D)) == sp.zeros(D, D)
    return U

def channel_from_dilation(steps, mu, dv, dh):
    """rho -> Tr_H[ W (rho (x) mu) W^dag ], W = product of steps (applied in order)."""
    W = sp.eye(dv * dh)
    for S in steps:
        W = S * W
    return lambda rho: sp.simplify(ptrace_H(W * kron(rho, mu) * W.H, dv, dh))

def joint_after(steps, mu, rho, dv, dh):
    W = sp.eye(dv * dh)
    for S in steps:
        W = S * W
    return sp.simplify(W * kron(rho, mu) * W.H)

def superop_equal(F, G, d=2):
    return all(sp.simplify(F(E(i, j, d)) - G(E(i, j, d))) == sp.zeros(d, d)
               for i in range(d) for j in range(d))

def choi(F, d=2):
    """Unnormalized Choi matrix sum_ij |i><j| (x) F(|i><j|)."""
    return sp.simplify(sum((kron(E(i, j, d), F(E(i, j, d))) for i in range(d) for j in range(d)),
                           sp.zeros(d * d, d * d)))

def partial_transpose_first(C, d=2):
    out = sp.zeros(d * d, d * d)
    for i, j, a, b in itertools.product(range(d), repeat=4):
        out[j * d + a, i * d + b] = C[i * d + a, j * d + b]
    return out

def eigs(M):
    return sorted(sp.Matrix(M).eigenvals(multiple=True), key=lambda v: sp.N(v))

Ad = lambda A: (lambda rho: sp.simplify(A * rho * A.H))
ident = lambda rho: rho
Delta = lambda rho: sp.diag(rho[0, 0], rho[1, 1])
Repl0 = lambda rho: sp.simplify(rho.trace() * E(0, 0))

CNOT = perm_unitary(lambda x, h: (x, h ^ x), 2, 2)       # S control, H target
SWAP = perm_unitary(lambda x, h: (h, x), 2, 2)
HS = kron(Hd, I2)                                          # intermediate system Hadamard
mu_unif = sp.eye(2) * half                                 # classical mixture 1/2(|0><0|+|1><1|)
mu_blank = E(0, 0)                                         # point mass (initialized slot)

report = []
def rec(tag, ok, detail=""):
    report.append((tag, bool(ok), detail))
    print(("PASS " if ok else "FAIL ") + tag + ((" :: " + detail) if detail else ""))

# ---------------- Controls (must be green before any verdict) ----------------
rec("C1 Delta = 1/2(id + Ad Z)  (Delta mixed-unitary)",
    superop_equal(Delta, lambda r: half * r + half * Z * r * Z))
rec("C2 PT(Choi(id)) has eigenvalue -1 (id not entanglement-breaking)",
    eigs(partial_transpose_first(choi(ident)))[0] == -1, str(eigs(partial_transpose_first(choi(ident)))))
rec("C3 PT(Choi(Delta)) >= 0 (Delta entanglement-breaking: Choi is separable diag)",
    all(v >= 0 for v in eigs(partial_transpose_first(choi(Delta)))), str(eigs(partial_transpose_first(choi(Delta)))))
rec("C4 Choi(Repl0) = I (x) |0><0|",
    choi(Repl0) == kron(I2, E(0, 0)))
# Countercontrol: the decision rule used for case B must REJECT a pair known to
# be classical-memory and ACCEPT a pair known to be quantum-memory; rule:
#   E1 = Repl0  =>  every admissible I_i = Tr(F_i .)|0><0|  =>  E2 must be EB.
#   decide 'quantum memory' iff PT(Choi(E2)) has a negative eigenvalue.
rule = lambda E2: eigs(partial_transpose_first(choi(E2)))[0] < 0
rec("C5 rule rejects {Repl0, Delta} (classical: I_x=<x|.|x>|0><0|, Phi_x=prep |x>)", not rule(Delta))
rec("C6 rule accepts {Repl0, id}", rule(ident))

# -------- Case A: CNOT, hidden uniform diagonal, coherent input |+> ----------
for mu, mname in ((mu_unif, "uniform"), (mu_blank, "point-mass")):
    E1 = channel_from_dilation([CNOT], mu, 2, 2)
    E2 = channel_from_dilation([CNOT, CNOT], mu, 2, 2)
    E2H = channel_from_dilation([CNOT, HS, CNOT], mu, 2, 2)
    rec(f"A[{mname}] E1 = Delta", superop_equal(E1, Delta))
    rec(f"A[{mname}] E2 (no intermediate) = id", superop_equal(E2, ident))
    rec(f"A[{mname}] E2 on |+> = |+><+|", sp.simplify(E2(P_plus) - P_plus) == sp.zeros(2, 2))
    rec(f"A[{mname}] E2H (Hadamard between steps) on |+>", True, str(E2H(P_plus).tolist()))
    rec(f"A[{mname}] E2H = Delta o Ad(H) o Delta ... i.e. maps rho -> I/2 + ?", True,
        str([E2H(E(i, j)).tolist() for i in range(2) for j in range(2)]))
    # explicit BBS decomposition with first-step constraint, both E2 and E2H
    Iinst = [lambda r: half * r, lambda r: half * Z * r * Z]
    for E2x, nm in ((E2, "E2"), (E2H, "E2H")):
        Phis = [E2x, lambda r, E2x=E2x: E2x(Z * r * Z)]
        rec(f"A[{mname}] {nm}: sum I_a = E1",
            superop_equal(lambda r: Iinst[0](r) + Iinst[1](r), E1))
        rec(f"A[{mname}] {nm}: sum Phi_a o I_a = {nm}  (classical memory, variable a = Z-kick label)",
            superop_equal(lambda r: sp.simplify(Phis[0](Iinst[0](r)) + Phis[1](Iinst[1](r))), E2x))
    # conditioning on the HIDDEN CONFIGURATION h after step 1
    J = lambda r: joint_after([CNOT], mu, r, 2, 2)
    Ih = [lambda r, h=h: sp.simplify(ptrace_H(kron(I2, E(h, h)) * J(r) * kron(I2, E(h, h)), 2, 2))
          for h in range(2)]
    fac = all(superop_equal(lambda r, f=f: f(r), lambda r, f=f: f(Delta(r))) for f in Ih)
    rec(f"A[{mname}] instrument 'read hidden config h' factors through Delta (I_h = I_h o Delta)", fac)
    rec(f"A[{mname}] => no Phi_h with sum Phi_h o I_h = E2=id: |+>,|-> give equal I_h-branches",
        all(sp.simplify(f(P_plus) - f(P_minus)) == sp.zeros(2, 2) for f in Ih) and
        sp.simplify(E2(P_plus) - E2(P_minus)) != sp.zeros(2, 2))
    Jp = J(P_plus)
    rec(f"A[{mname}] joint state after step 1 on |+>", True, str(Jp.tolist()))
    rec(f"A[{mname}] joint state has coherence between hidden configs (not cq in config basis)",
        any(Jp[a * 2 + h, b * 2 + g] != 0 for a in range(2) for b in range(2)
            for h in range(2) for g in range(2) if h != g))
    pt = eigs(partial_transpose_first(Jp))
    rec(f"A[{mname}] PT spectrum of joint S:H state", True, str(pt))

# -------- Case B: SWAP, point-mass (initialized) hidden slot ----------------
E1 = channel_from_dilation([SWAP], mu_blank, 2, 2)
E2 = channel_from_dilation([SWAP, SWAP], mu_blank, 2, 2)
rec("B E1 = Repl0 (rho -> |0><0|)", superop_equal(E1, Repl0))
rec("B E2 = id", superop_equal(E2, ident))
rec("B classical visible law on configurations: X1=0, X2=X0",
    all(E1(E(x, x)) == E(0, 0) and E2(E(x, x)) == E(x, x) for x in range(2)))
# Exactness argument: any CP I_i <= Repl0 has Choi C_i with 0 <= C_i <= I(x)|0><0|,
# so supp C_i in C^2 (x) |0>, C_i = F_i^T (x) |0><0|, I_i(rho) = Tr(F_i rho)|0><0|.
# Then sum Phi_i o I_i (rho) = sum Tr(F_i rho) Phi_i(|0><0|): entanglement-breaking.
rec("B (with sum I_i = E1) quantum memory: E2=id is not EB  [decided by rule, controls C5/C6]", rule(E2))
Jp = joint_after([SWAP], mu_blank, P_plus, 2, 2)
rec("B hidden marginal after step 1 on |+> is |+><+| (coherent, not diagonal)",
    ptrace_V(Jp, 2, 2) == P_plus, str(ptrace_V(Jp, 2, 2).tolist()))
# literal (unconstrained) owner form: holds trivially
rec("B literal form E2 = sum Phi_i(M_i rho M_i^dag) holds with M=I, Phi=E2 (vacuous)",
    superop_equal(lambda r: E2(I2 * r * I2), E2))

# -------- Case B': SWAP with uniform hidden prior ---------------------------
E1u = channel_from_dilation([SWAP], mu_unif, 2, 2)
E2u = channel_from_dilation([SWAP, SWAP], mu_unif, 2, 2)
paulis = [I2, X, sp.Matrix([[0, -sp.I], [sp.I, 0]]), Z]
rec("B' E1 = constant I/2", superop_equal(E1u, lambda r: r.trace() * I2 * half))
rec("B' E2 = id", superop_equal(E2u, ident))
rec("B' sum_P 1/4 Ad P = E1 (Pauli twirl, 2-bit label)",
    superop_equal(lambda r: sp.simplify(sum((P * r * P.H for P in paulis), sp.zeros(2, 2)) / 4), E1u))
rec("B' sum_P Phi_P o I_P = id with Phi_P = Ad P^dag  (classical memory, 2 bits > 1 hidden bit)",
    superop_equal(lambda r: sp.simplify(sum((P.H * (P * r * P.H / 4) * P for P in paulis), sp.zeros(2, 2))), ident))
Jh = lambda r: joint_after([SWAP], mu_unif, r, 2, 2)
Ihu = [lambda r, h=h: sp.simplify(ptrace_H(kron(I2, E(h, h)) * Jh(r) * kron(I2, E(h, h)), 2, 2)) for h in range(2)]
rec("B' reading hidden config h after step 1 kills input coherence (I_h(|+>) = I_h(|->))",
    all(sp.simplify(f(P_plus) - f(P_minus)) == sp.zeros(2, 2) for f in Ihu))

# -------- Case C: the paper's ledger-type realization of the same law --------
# visible x in {0,1}; hidden = ledger (l1,l2) in {B,0,1}^2 and clock c in {0,1,2}.
# step c=0: (x,(B,B),0) -> (0,(x,B),1); step c=1: (y,(x,B),1) -> (x,(x,y),2).
# Injective on the reachable set; completed to a bijection of the finite product.
syms = ['B', 0, 1]
Hs = [(l1, l2, c) for l1 in syms for l2 in syms for c in range(3)]
hidx = {h: i for i, h in enumerate(Hs)}
dh = len(Hs)
partial = {}
for x in range(2):
    partial[(x, ('B', 'B', 0))] = (0, (x, 'B', 1))
    for y in range(2):
        partial[(y, (x, 'B', 1))] = (x, (x, y, 2))
dom = [(x, h) for x in range(2) for h in Hs]
assert len(set(partial.values())) == len(partial)
rest_dom = [s for s in dom if s not in partial]
rest_img = [s for s in dom if s not in set(partial.values())]
full = dict(partial); full.update(zip(rest_dom, rest_img))
phiC = lambda x, h: (lambda r: (r[0], hidx[r[1]]))(full[(x, Hs[h])])
UC = perm_unitary(phiC, 2, dh)
muC = E(hidx[('B', 'B', 0)], hidx[('B', 'B', 0)], dh)
E1c = channel_from_dilation([UC], muC, 2, dh)
E2c = channel_from_dilation([UC, UC], muC, 2, dh)
rec("C E1 = Repl0", superop_equal(E1c, Repl0))
rec("C E2 = Delta (ledger keeps x0: coherence not restored)", superop_equal(E2c, Delta))
rec("C same configuration law as B (X1=0, X2=X0)",
    all(E1c(E(x, x)) == E(0, 0) and E2c(E(x, x)) == E(x, x) for x in range(2)))
IC = [lambda r, x=x: r[x, x] * E(0, 0) for x in range(2)]
PhiC = [lambda s, x=x: s.trace() * E(x, x) for x in range(2)]
rec("C sum I_x = E1", superop_equal(lambda r: IC[0](r) + IC[1](r), E1c))
rec("C sum Phi_x o I_x = E2 (classical memory, variable = recorded x0)",
    superop_equal(lambda r: PhiC[0](IC[0](r)) + PhiC[1](IC[1](r)), E2c))
rec("C rule says classical for {Repl0, Delta}", not rule(E2c))

# -------- Case D: configuration (diagonal) inputs only, any process ---------
# Lemma: for ANY channels E1,E2 and diagonal rho, I_x(rho)=<x|rho|x>E1(|x><x|),
# Phi_x(s)=Tr(s)E2(|x><x|) satisfy sum I_x = E1 and sum Phi_x o I_x = E2.
def diag_lemma(E1x, E2x):
    t0, t1 = sp.symbols('t0 t1', nonnegative=True)
    rho = sp.diag(t0, t1)
    lhs1 = sum((rho[x, x] * E1x(E(x, x)) for x in range(2)), sp.zeros(2, 2))
    lhs2 = sum(((rho[x, x] * E1x(E(x, x))).trace() * E2x(E(x, x)) for x in range(2)), sp.zeros(2, 2))
    return sp.simplify(lhs1 - E1x(rho)) == sp.zeros(2, 2) and sp.simplify(lhs2 - E2x(rho)) == sp.zeros(2, 2)
rec("D diagonal-input lemma holds on case B (the quantum-memory pair)", diag_lemma(E1, E2))
rec("D diagonal-input lemma holds on Hadamard-process {Ad H, id} (generic quantum)", diag_lemma(Ad(Hd), ident))

n_fail = sum(1 for _, ok, _ in report if not ok)
print(f"\n{len(report)} checks, {n_fail} failed")
controls_green = all(ok for t, ok, _ in report if t.startswith("C") and t[1].isdigit())
print("controls green:", controls_green)
if controls_green and n_fail == 0:
    print("VERDICT (generated): case A classical-memory for both priors and both E2; "
          "case B {Repl0,id} not classical-memory under the constrained definition; "
          "case C (same configuration law as B) classical-memory; "
          "diagonal inputs: decomposition exists for every process.")
else:
    print("VERDICT VOID: a control or check failed")
