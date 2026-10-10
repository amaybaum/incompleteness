#!/usr/bin/env python3
"""EQ-D, node N3(d): exact check of the carrier lift

    DrivesElementary at Fin 2  +  Architecture (one, mul, block)  +  ContextStable  +  LabelInvariant
        ==>  DrivesElementary at every finite carrier R.

Every matrix is built with the Lean conventions of the base `bcbc516f`:
  tensorOf XA XB p q   = XA p.1 q.1 * XB p.2 q.2            (MonoidalCompletion.lean:193)
  reindex e e K  p q   = K (e.symm p) (e.symm q)             (Mathlib: submatrix e.symm e.symm)
  ancBlock K f e s t   = K (s, f) (t, e)                     (AncillaClosure.lean:457)
  permMatrix g i j     = if g j = i then 1 else 0            (CoherentLift.lean:92)
  transition a b       = E_ab + E_ba                          (LieRankSource.lean:199)
  phaseGate a          = diag(p => if a = p then I else 1)    (LieRankSource.lean:209)
  flow H t             = exp(-(t) I H)                        (ReachabilitySeam.lean:95)

Exactness: entries are polynomials in symbols c = cos s, sn = sin s, z = exp(-2 i t) with Gaussian-rational
coefficients; identities that need cos^2 + sin^2 = 1 are reduced modulo that polynomial (single generator, hence a
Groebner basis, so the remainder is canonical). Closed forms of the 2x2 flows are checked against sympy's matrix
exponential with a symbolic real time. No floating point is used.
"""
import itertools
import sys

import sympy as sp

I = sp.I
c, sn = sp.symbols('c sn', real=True)
z = sp.symbols('z')
s_sym, t_sym = sp.symbols('s t', real=True)
CIRCLE = c**2 + sn**2 - 1

FAILS = []


def check(name, ok):
    print(('PASS ' if ok else 'FAIL ') + name)
    if not ok:
        FAILS.append(name)
    return ok


def reduce_circle(expr):
    expr = sp.expand(expr)
    if expr == 0:
        return sp.Integer(0)
    _, r = sp.reduced(expr, [CIRCLE], c, sn, order='lex')
    return sp.expand(r)


# ---------- matrices as dicts over explicit index lists (mirrors Lean's types) ----------

class Mat:
    def __init__(self, idx, entries=None):
        self.idx = list(idx)
        self.e = dict(entries or {})

    def __getitem__(self, pq):
        return self.e.get(pq, sp.Integer(0))

    def __mul__(self, other):
        assert self.idx == other.idx
        out = {}
        for p in self.idx:
            for q in self.idx:
                acc = sp.Integer(0)
                for r in self.idx:
                    a = self[(p, r)]
                    if a != 0:
                        b = other[(r, q)]
                        if b != 0:
                            acc += a * b
                acc = sp.expand(acc)
                if acc != 0:
                    out[(p, q)] = acc
        return Mat(self.idx, out)

    def map(self, f):
        return Mat(self.idx, {k: f(v) for k, v in self.e.items()})

    def equal_mod_circle(self, other):
        assert self.idx == other.idx
        for p in self.idx:
            for q in self.idx:
                if reduce_circle(self[(p, q)] - other[(p, q)]) != 0:
                    return False
        return True

    def equal_exact(self, other):
        assert self.idx == other.idx
        return all(sp.expand(self[(p, q)] - other[(p, q)]) == 0 for p in self.idx for q in self.idx)


def ident(idx):
    return Mat(idx, {(p, p): sp.Integer(1) for p in idx})


def diag(idx, d):
    return Mat(idx, {(p, p): d(p) for p in idx if d(p) != 0})


def tensorOf(XA, XB):
    idx = [(a, b) for a in XA.idx for b in XB.idx]
    out = {}
    for p in idx:
        for q in idx:
            v = sp.expand(XA[(p[0], q[0])] * XB[(p[1], q[1])])
            if v != 0:
                out[(p, q)] = v
    return Mat(idx, out)


def reindex(e, K):
    """reindex e e K, e a bijection of K.idx given as a dict; entry (p,q) = K (e^-1 p) (e^-1 q)."""
    inv = {v: k for k, v in e.items()}
    assert sorted(inv) == sorted(K.idx)
    return Mat(K.idx, {(p, q): K[(inv[p], inv[q])] for p in K.idx for q in K.idx if K[(inv[p], inv[q])] != 0})


def ancBlock(K, R, f, e):
    return Mat(R, {(s, t): K[((s, f), (t, e))] for s in R for t in R if K[((s, f), (t, e))] != 0})


def permMatrix(idx, g):
    return Mat(idx, {(i, j): sp.Integer(1) for j in idx for i in idx if g[j] == i})


def transition(idx, a, b):
    m = Mat(idx)
    m.e[(a, b)] = m.e.get((a, b), 0) + 1
    m.e[(b, a)] = m.e.get((b, a), 0) + 1
    return m


def phaseGate(idx, a):
    return diag(idx, lambda p: I if p == a else sp.Integer(1))


def swap_perm(idx, pairs):
    g = {p: p for p in idx}
    for x, y in pairs:
        g[x], g[y] = y, x
    return g


# ---------- the qubit data (DrivesElementary at Fin 2), closed forms checked against exp ----------

F2 = [0, 1]
rot = Mat(F2, {(0, 0): c, (1, 1): c, (0, 1): -I * sn, (1, 0): -I * sn})        # flow (transition 0 1) s
ph0 = phaseGate(F2, 0)                                                            # diag(I, 1)
zph = Mat(F2, {(0, 0): z, (1, 1): sp.Integer(1)})                                 # flow (transition 0 0) t
mone = ph0 * ph0                                                                  # diag(-1, 1), by `mul` at Fin 2

X2 = sp.Matrix([[0, 1], [1, 0]])
exp_rot = sp.simplify((-I * s_sym * X2).exp())
check('closed form: flow (transition 0 1) s = [[cos s, -i sin s], [-i sin s, cos s]]',
      sp.simplify(exp_rot - sp.Matrix([[sp.cos(s_sym), -I * sp.sin(s_sym)],
                                       [-I * sp.sin(s_sym), sp.cos(s_sym)]])) == sp.zeros(2, 2))
E00x2 = sp.Matrix([[2, 0], [0, 0]])
exp_z = sp.simplify((-I * t_sym * E00x2).exp())
check('closed form: flow (transition 0 0) t = diag(exp(-2 i t), 1)',
      sp.simplify(exp_z - sp.Matrix([[sp.exp(-2 * I * t_sym), 0], [0, 1]])) == sp.zeros(2, 2))
check('mul at Fin 2: phaseGate 0 * phaseGate 0 = diag(-1, 1)',
      mone.equal_exact(diag(F2, lambda p: -1 if p == 0 else 1)))
check('double angle: rot_s^2 = flow (transition 0 1) (2s) (cos 2s = c^2 - sn^2, sin 2s = 2 c sn)',
      sp.simplify(sp.cos(2 * s_sym) - (sp.cos(s_sym)**2 - sp.sin(s_sym)**2)) == 0
      and sp.simplify(sp.sin(2 * s_sym) - 2 * sp.cos(s_sym) * sp.sin(s_sym)) == 0)


def rot2_on(R, a, b):
    """flow (transition a b) (2s) on carrier R, written with c, sn (rot_s squared on the pair)."""
    m = ident(R)
    m.e[(a, a)] = c**2 - sn**2
    m.e[(b, b)] = c**2 - sn**2
    m.e[(a, b)] = -2 * I * c * sn
    m.e[(b, a)] = -2 * I * c * sn
    return m


def lift_checks(k):
    R = list(range(k))
    RF = [(r, j) for r in R for j in F2]
    oneR = ident(R)
    ok_all = True
    # phases and the a = b flows
    for a in R:
        sig = swap_perm(RF, [((r, 0), (r, 1)) for r in R if r != a])
        Kp = reindex(sig, tensorOf(oneR, ph0))       # ContextStable, then LabelInvariant
        ok_all &= ancBlock(Kp, R, 0, 0).equal_exact(phaseGate(R, a))
        ok_all &= ancBlock(Kp, R, 0, 1).equal_exact(Mat(R)) and ancBlock(Kp, R, 1, 0).equal_exact(Mat(R))
        Kz = reindex(sig, tensorOf(oneR, zph))
        ok_all &= ancBlock(Kz, R, 0, 0).equal_exact(diag(R, lambda p: z if p == a else sp.Integer(1)))
    # the a != b flows: M * (D M D), then block (0,0); swaps from flows and phases at R
    for a, b in itertools.permutations(R, 2):
        sig = swap_perm(RF, [((a, 1), (b, 0))])
        M = reindex(sig, tensorOf(oneR, rot))
        tau = swap_perm(RF, [((a, 0), (a, 1)), ((b, 0), (b, 1))])
        D = reindex(tau, tensorOf(oneR, mone))
        P = M * (D * (M * D))
        ok_all &= ancBlock(P, R, 0, 0).equal_mod_circle(rot2_on(R, a, b))
        ok_all &= ancBlock(P, R, 0, 1).equal_mod_circle(Mat(R)) and ancBlock(P, R, 1, 0).equal_mod_circle(Mat(R))
        # unitarity of the composite (so the GPT reading is deterministic: attach |0>, apply, discard)
        Pd = Mat(RF, {(q, p): sp.expand(sp.conjugate(v)) for (p, q), v in P.e.items()})
        ok_all &= (Pd * P).equal_mod_circle(ident(RF))
        # swap a b = phaseGate a * phaseGate b * flow (transition a b) (pi/2), by `mul` at R
        flow_half = rot2_on(R, a, b).map(lambda v: v.subs({c: sp.sqrt(2) / 2, sn: sp.sqrt(2) / 2}))
        sw = phaseGate(R, a) * (phaseGate(R, b) * flow_half)
        ok_all &= sw.map(sp.nsimplify).equal_exact(permMatrix(R, swap_perm(R, [(a, b)])))
    return ok_all


def controls(k):
    R = list(range(k))
    RF = [(r, j) for r in R for j in F2]
    oneR = ident(R)
    res = {}
    # C1: without the relabelling the extracted block is I * 1_R, not phaseGate a (for k >= 2)
    blk = ancBlock(tensorOf(oneR, ph0), R, 0, 0)
    res['C1 relabelling load-bearing'] = (k < 2) or not blk.equal_exact(phaseGate(R, 0))
    # C2: without the D-conjugation (M*M) the block is not the single-pair flow (for k >= 3)
    if k >= 2:
        a, b = 0, 1
        sig = swap_perm(RF, [((a, 1), (b, 0))])
        M = reindex(sig, tensorOf(oneR, rot))
        blk2 = ancBlock(M * M, R, 0, 0)
        res['C2 D-conjugation load-bearing'] = (k < 3) or not blk2.equal_mod_circle(rot2_on(R, a, b))
    # C3: a single relabelled tensor never gives the single-pair flow at generic angle (k >= 3):
    #     entry (r, r) for r outside the pair is c, not 1
    if k >= 3:
        sig = swap_perm(RF, [((0, 1), (1, 0))])
        M = reindex(sig, tensorOf(oneR, rot))
        res['C3 one tensor insufficient'] = reduce_circle(ancBlock(M, R, 0, 0)[(2, 2)] - 1) != 0
    return res


def checker_selftest():
    """Mutation test: the comparison must reject wrong targets, so a PASS above is not vacuous."""
    R = [0, 1, 2]
    RF = [(r, j) for r in R for j in F2]
    oneR = ident(R)
    sig = swap_perm(RF, [((0, 1), (1, 0))])
    M = reindex(sig, tensorOf(oneR, rot))
    tau = swap_perm(RF, [((0, 0), (0, 1)), ((1, 0), (1, 1))])
    D = reindex(tau, tensorOf(oneR, mone))
    blk = ancBlock(M * (D * (M * D)), R, 0, 0)
    wrong_pair = not blk.equal_mod_circle(rot2_on(R, 0, 2))
    wrong_angle = not blk.equal_mod_circle(rot2_on(R, 0, 1).map(lambda v: v.subs({c: 1, sn: 0})))
    perturbed = rot2_on(R, 0, 1)
    perturbed.e[(2, 2)] = sp.Integer(1) + c * sn
    wrong_entry = not blk.equal_mod_circle(perturbed)
    ph_wrong = not ancBlock(reindex(swap_perm(RF, [((r, 0), (r, 1)) for r in R if r != 0]),
                                    tensorOf(oneR, ph0)), R, 0, 0).equal_exact(phaseGate(R, 1))
    return wrong_pair and wrong_angle and wrong_entry and ph_wrong


if __name__ == '__main__':
    kmax = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    check('SELFTEST the comparison rejects a wrong pair, a wrong angle, a perturbed entry, a wrong phase site',
          checker_selftest())
    for k in range(1, kmax + 1):
        check(f'lift at carrier Fin {k}: phases, a=a flows, a!=b flows, swaps (exact)', lift_checks(k))
        for name, ok in controls(k).items():
            check(f'control at Fin {k}: {name}', ok)
    print()
    if FAILS:
        print('VERDICT  VOID — failed:', FAILS)
        sys.exit(1)
    print(f'VERDICT  the lift identities hold exactly at every carrier Fin 1 .. Fin {kmax}; all controls green')
