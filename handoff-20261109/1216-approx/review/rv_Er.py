#!/usr/bin/env python3
"""Reviewer's exact generic check for #1216 unit 1, route E_r ("register encoding"): a literal
finite shuffle-only realization in the form of Main:566/:580, built here from scratch for a 2-qubit
experiment whose instruments have complex entries.  Imports nothing from earlier probes or the repo.

Configuration = (t, visible record, hidden unnormalized branch matrix rho~ over Q(i), predecessor
stack, K seeds in {0..G-1}).  One fixed step map phi_a per instrument a: outcome-free instruments
apply their Kraus map; measuring instruments compute q_o = tr(I_o(rho~)) exactly, pick o by the exact
cumulative threshold r * sum q < G * q_{<=o} on the t-th seed, write o, set rho~ <- I_o(rho~), push
the predecessor.  Kraus operators are rescaled by constants common to all outcomes of an instrument
(H' = sqrt2 H, X/Y projectors times 2), which leaves every threshold unchanged: all data are Gaussian
integers, so all arithmetic is exact.

E1  injectivity: each phi_a is injective on the whole reachable set (all protocols, all seeds), and
    the union map extends to an explicit bijection of a finite set (constructed and verified).
E2  closure: every reachable register is Hermitian PSD (all principal minors >= 0, exact).
E3  validity + accuracy: the realized outcome law (exact enumeration over the seeds read by the
    measuring steps; outcome-free steps read none) is a probability law, and its TV distance from the
    exact quantum law is positive (a 3-4-5 rotation makes the law non-dyadic) and at most
    (#measuring steps)(|O|-1)/G <= K(|O_max|-1)/G, for a non-adaptive protocol (complex entangled
    pair, Y and X reads) and an adaptive one (G = 12, K = 6).
E4  complex structure is data: the register reaches entries with nonzero imaginary part.
Countercontrols: (i) replacing CNOT by a partial transpose (positive, not CP) makes E2 fail;
(ii) dropping the predecessor push makes E1 fail on a domain with two coherence-differing registers; (iii) comparing against a wrong law makes E3 fail.
Run: python3 -I -B rv_Er.py   (exit 0 iff all checks and countercontrols behave as stated)
"""
import itertools
import sys
from fractions import Fraction as Fr

FAIL = []


def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAIL.append(name)


# ---------- Gaussian rationals as (re, im) pairs of Fractions; matrices as tuples of tuples
def cm(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def ca(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cc(a):
    return (a[0], -a[1])


Z0 = (Fr(0), Fr(0))


def C(x, y=0):
    return (Fr(x), Fr(y))


def mat(rows):
    return tuple(tuple(C(*e) if isinstance(e, tuple) else C(e) for e in r) for r in rows)


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return tuple(tuple(
        _sum(cm(A[i][k], B[k][j]) for k in range(m)) for j in range(p)) for i in range(n))


def _sum(it):
    s = Z0
    for x in it:
        s = ca(s, x)
    return s


def dag(A):
    return tuple(tuple(cc(A[j][i]) for j in range(len(A))) for i in range(len(A[0])))


def kron(A, B):
    return tuple(tuple(cm(A[i // len(B)][j // len(B[0])], B[i % len(B)][j % len(B[0])])
                       for j in range(len(A[0]) * len(B[0]))) for i in range(len(A) * len(B)))


def tr(A):
    return _sum(A[i][i] for i in range(len(A)))


def conj_by(K, R):
    return mmul(mmul(K, R), dag(K))


def det(M):
    """Exact determinant over Q(i) by cofactor expansion (n <= 4)."""
    n = len(M)
    if n == 1:
        return M[0][0]
    s = Z0
    for j in range(n):
        minor = tuple(tuple(M[i][k] for k in range(n) if k != j) for i in range(1, n))
        term = cm(M[0][j], det(minor))
        s = ca(s, term if j % 2 == 0 else (-term[0], -term[1]))
    return s


def is_psd(M):
    n = len(M)
    if any(M[i][j] != cc(M[j][i]) for i in range(n) for j in range(n)):
        return False
    for k in range(1, n + 1):
        for S in itertools.combinations(range(n), k):
            d = det(tuple(tuple(M[i][j] for j in S) for i in S))
            if d[1] != 0 or d[0] < 0:
                return False
    return True


I2 = mat([[1, 0], [0, 1]])
Hs = mat([[1, 1], [1, -1]])                     # sqrt2 * H
Sg = mat([[1, 0], [0, (0, 1)]])                 # phase gate S = diag(1, i)
CNOT = mat([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
P0 = mat([[1, 0], [0, 0]]); P1 = mat([[0, 0], [0, 1]])
Xp = mat([[1, 1], [1, 1]]); Xm = mat([[1, -1], [-1, 1]])                  # 2 * (I +- X)/2
Yp = mat([[1, (0, -1)], [(0, 1), 1]]); Ym = mat([[1, (0, 1)], [(0, -1), 1]])  # 2 * (I +- Y)/2

# instrument -> list of (Kraus list) per outcome; outcome-free instruments have one "outcome" None
INSTR = {
    'H1': [[kron(Hs, I2)]],
    'S1': [[kron(Sg, I2)]],
    'CX': [[CNOT]],
    'R2': [[kron(I2, mat([[4, -3], [3, 4]]))]],      # 5 * (3-4-5 rotation) on qubit 2
    'Z1': [[kron(P0, I2)], [kron(P1, I2)]],
    'X2': [[kron(I2, Xp)], [kron(I2, Xm)]],
    'Y1': [[kron(Yp, I2)], [kron(Ym, I2)]],
    'Y2': [[kron(I2, Yp)], [kron(I2, Ym)]],
}
MEAS = {a for a, br in INSTR.items() if len(br) > 1}


def apply_branch(a, o, R):
    out = None
    for Kr in INSTR[a][o]:
        t = conj_by(Kr, R)
        out = t if out is None else tuple(tuple(ca(x, y) for x, y in zip(r1, r2)) for r1, r2 in zip(out, t))
    return out


def make_phi(a, G, push=True, override=None):
    def phi(cfg):
        t, rec, R, stack, seeds = cfg
        if override is not None:
            R2 = override(R)
            o = None
        elif a not in MEAS:
            R2 = apply_branch(a, 0, R)
            o = None
        else:
            q = [tr(apply_branch(a, oo, R))[0] for oo in range(len(INSTR[a]))]
            tot = sum(q)
            r = seeds[t]
            cum = Fr(0)
            o = None
            for oo, qo in enumerate(q):
                cum += qo
                if r * tot < G * cum:
                    o = oo
                    break
            R2 = apply_branch(a, o, R)
        new_stack = stack + (R,) if push else stack
        return (t + 1, rec + ((a, o),), R2, new_stack, seeds)
    return phi


def run(protocol, G, K, phis, mpos):
    """protocol: function(record) -> instrument label. Returns realized law, reachable cfgs.
    Seeds are enumerated exactly at the measuring positions mpos; outcome-free steps never read
    their seed, so fixing those seeds at 0 leaves the realized law unchanged."""
    rho0 = kron(P0, P0)
    law = {}
    reach = []
    for sm in itertools.product(range(G), repeat=len(mpos)):
        seeds = [0] * K
        for pos, r in zip(mpos, sm):
            seeds[pos] = r
        seeds = tuple(seeds)
        cfg = (0, (), rho0, (), seeds)
        reach.append(cfg)
        for _ in range(K):
            a = protocol(cfg[1])
            cfg = phis[a](cfg)
            reach.append((a, cfg))
        outs = tuple(o for (_, o) in cfg[1] if o is not None)
        law[outs] = law.get(outs, Fr(0)) + Fr(1, G ** len(mpos))
    return law, reach


def quantum_law(protocol, K):
    """Exact quantum law by branching over outcomes with exact conditionals."""
    law = {}

    def rec_(R, record, p):
        if len(record) == K:
            outs = tuple(o for (_, o) in record if o is not None)
            law[outs] = law.get(outs, Fr(0)) + p
            return
        a = protocol(record)
        if a not in MEAS:
            rec_(apply_branch(a, 0, R), record + ((a, None),), p)
            return
        bs = [apply_branch(a, o, R) for o in range(len(INSTR[a]))]
        q = [tr(B)[0] for B in bs]
        tot = sum(q)
        for o, B in enumerate(bs):
            if q[o] != 0:
                rec_(B, record + ((a, o),), p * q[o] / tot)
    rec_(kron(P0, P0), (), Fr(1))
    return law


def tv(P, Q):
    keys = set(P) | set(Q)
    return sum(abs(P.get(k, Fr(0)) - Q.get(k, Fr(0))) for k in keys) / 2


G, K = 12, 6
phis = {a: make_phi(a, G) for a in INSTR}
prot_fixed = lambda rec: ['H1', 'S1', 'CX', 'R2', 'Y1', 'X2'][len(rec)]


def prot_adapt(rec):
    seq = ['H1', 'S1', 'CX', 'R2', 'Z1']
    if len(rec) < 5:
        return seq[len(rec)]
    return 'X2' if rec[4][1] == 0 else 'Y2'


MPOS = (4, 5)
bound = Fr(len(MPOS) * (2 - 1), G)     # chain rule over the measuring steps; <= Main's K(|O|-1)/G
check("E3 the per-measuring-step bound is no weaker than Main's K(|O_max|-1)/G", bound <= Fr(K, G))
all_reach = []
for nm, prot in (("fixed", prot_fixed), ("adaptive", prot_adapt)):
    law, reach = run(prot, G, K, phis, MPOS)
    all_reach += reach
    Q = quantum_law(prot, K)
    d = tv(law, Q)
    print(f"     {nm}: quantum law {dict(sorted(Q.items()))}; TV = {d} (bound {bound})")
    check(f"E3 {nm}: realized law is a probability law", sum(law.values()) == 1 and all(v >= 0 for v in law.values()))
    check(f"E3 {nm}: 0 < TV(realized, quantum) <= (#measuring steps)(|O|-1)/G (non-dyadic law, grid error present)",
          0 < d <= bound)
    kmin = min(itertools.product(range(2), repeat=2), key=lambda k: Q.get(k, Fr(0)))
    wrong = {kmin: Fr(1)}
    check(f"E3 countercontrol {nm}: a wrong target law violates the bound", tv(law, wrong) > bound)

# E1 injectivity of each phi_a on the reachable set (domain = every reachable cfg)
cfgs = set()
for item in all_reach:
    cfgs.add(item if len(item) == 5 else item[1])
cfgs = {c for c in cfgs if c[0] < K}
ok_inj = True
for a in INSTR:
    imgs = {}
    for c in cfgs:
        im = phis[a](c)
        if im in imgs and imgs[im] != c:
            ok_inj = False
        imgs[im] = c
check(f"E1 each of the {len(INSTR)} step maps is injective on all {len(cfgs)} reachable pre-horizon configurations", ok_inj)
# explicit bijective extension of one map (CX) on the finite set D u phi(D)
dom = sorted(cfgs, key=repr)
img = {phis['CX'](c): c for c in dom}
U = set(dom) | set(img)
free_dom = sorted(set(img) - set(dom), key=repr)      # points of U not yet in the domain
free_img = sorted(set(dom) - set(img), key=repr)      # points of U not yet hit
bij = {c: phis['CX'](c) for c in dom}
bij.update(dict(zip(free_dom, free_img)))
check("E1 the CX step map extends to an explicit bijection of the finite set D u phi(D)",
      len(free_dom) == len(free_img) and set(bij) == U and set(bij.values()) == U)

# E2 closure: every reachable register PSD; E4 complex entries appear
regs = {c[2] for c in (it if len(it) == 5 else it[1] for it in all_reach)}
check(f"E2 all {len(regs)} distinct reachable registers are Hermitian PSD", all(is_psd(R) for R in regs))
check("E4 some reachable register has an entry with nonzero imaginary part",
      any(e[1] != 0 for R in regs for row in R for e in row))

# countercontrol (i): partial transpose on qubit 2 in place of CNOT, applied after H1, S1, CX
def ptrans2(R):
    out = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            a1, b1 = divmod(i, 2); a2, b2 = divmod(j, 2)
            out[i][j] = R[2 * a1 + b2][2 * a2 + b1]
    return tuple(tuple(r) for r in out)


phis_pt = dict(phis); phis_pt['PT'] = make_phi('PT', G, override=ptrans2)
cfg = (0, (), kron(P0, P0), (), (0,) * K)
for a in ('H1', 'S1', 'CX', 'PT'):
    cfg = phis_pt[a](cfg)
check("E2 countercontrol: a partial-transpose step (positive, not CP) yields a non-PSD register", not is_psd(cfg[2]))
# countercontrol (ii): the same injectivity test, on a domain that adds two configurations differing
# only in the coherence of qubit 1 (|+><+| (x) |0><0| vs I/2 (x) |0><0|, both scaled by 2), detects
# that the Z1 step map without the predecessor push is not injective, and passes it with the push.
Rplus = kron(Xp, P0)
Rmix = kron(mat([[1, 0], [0, 1]]), P0)
extra = {(0, (), Rplus, (), (0,) * K), (0, (), Rmix, (), (0,) * K)}


def injective(phi, dom):
    imgs = {}
    for c in dom:
        im = phi(c)
        if im in imgs and imgs[im] != c:
            return False
        imgs[im] = c
    return True


phi_np = make_phi('Z1', G, push=False)
check("E1 countercontrol: without the predecessor stack the Z1 step map is not injective (caught)",
      not injective(phi_np, cfgs | extra))
check("E1 control: with the stack the same Z1 map is injective on that domain", injective(phis['Z1'], cfgs | extra))

print("RESULT", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
