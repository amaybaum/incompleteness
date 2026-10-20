"""Node 6 probe: the quantum appearance in an observer's records (A2 track).

Exact arithmetic only (fractions.Fraction, SymPy rationals/algebraics). Floating point appears in
one place, block B3's comparison of a transcendental bound, and is labelled [NUM] there.

Blocks
  A  observable ladder: a Spekkens-type toy bit built as a kappa1-kappa4 OI construction
     (bijections, configuration readout, mixed hidden prior); its records against qubit QM; the
     cone lemma on its visible carrier; the non-disturbing variant (the restriction is a choice);
     the response-table PR box (representability is too weak).
  B  Bell under OI's actual readout: exhaustive local partitioned automaton (ceiling 2);
     one long edge (PR, operational no-signalling); a tunable family S = 2 + 2w; a
     measurement-dependent local model against Main's information bound.
  C  preparation contextuality: a C4-satisfying delay line and the toy bit are preparation
     noncontextual (record map injective); exact LP gives the PNC parity-oblivious-multiplexing
     ceiling 3/4; a hidden-label (shadow-type) construction exceeds it, exactly parity-oblivious.
  K  Peres-Mermin: no noncontextual assignment; context-indexed responses satisfy it.
  D  the one emergent constraint of the uniform prior: double stochasticity (replay of Main 3.1).
"""
from fractions import Fraction as F
from itertools import product, permutations
import sympy as sp
from sympy.solvers.simplex import lpmax

RESULTS = []


def check(cid, ok, msg):
    RESULTS.append((cid, bool(ok), msg))
    print(f"{cid:5s} {'PASS' if ok else 'FAIL'}  {msg}")


# ----------------------------------------------------------------------------------------------
# Block A: the toy bit as an OI construction
# state = (a, b, p1, p2, p3, r1, r2, r3); (a, b) and r_t hidden, p_t visible pointers
# ----------------------------------------------------------------------------------------------
FK = {'Z': lambda a, b: a, 'X': lambda a, b: b, 'Y': lambda a, b: a ^ b}


def meas_step(state, t, k, disturb=True):
    a, b, p, r = state[0], state[1], list(state[2:5]), list(state[5:8])
    p[t] ^= FK[k](a, b)
    if disturb:
        if k == 'Z':
            b ^= r[t]
        elif k == 'X':
            a ^= r[t]
        else:
            a ^= r[t]
            b ^= r[t]
    return (a, b, *p, *r)


TOY_PREP = {
    'Z0': [(0, 0), (0, 1)], 'Z1': [(1, 0), (1, 1)],
    'X0': [(0, 0), (1, 0)], 'X1': [(0, 1), (1, 1)],
    'Y0': [(0, 0), (1, 1)], 'Y1': [(0, 1), (1, 0)],
}


def toy_law(prep, seq, disturb=True):
    law = {}
    ab = TOY_PREP[prep]
    w = F(1, len(ab) * 8)
    for (a, b) in ab:
        for r in product((0, 1), repeat=3):
            s = (a, b, 0, 0, 0, *r)
            for t, k in enumerate(seq):
                s = meas_step(s, t, k, disturb)
            rec = tuple(s[2:2 + len(seq)])
            law[rec] = law.get(rec, 0) + w
    return {k: v for k, v in law.items() if v != 0}


I2 = sp.eye(2)
KET = {
    'Z0': sp.Matrix([1, 0]), 'Z1': sp.Matrix([0, 1]),
    'X0': sp.Matrix([1, 1]) / sp.sqrt(2), 'X1': sp.Matrix([1, -1]) / sp.sqrt(2),
    'Y0': sp.Matrix([1, sp.I]) / sp.sqrt(2), 'Y1': sp.Matrix([1, -sp.I]) / sp.sqrt(2),
}
PROJ = {(k, o): KET[f"{k}{o}"] * KET[f"{k}{o}"].H for k in 'ZXY' for o in (0, 1)}


def qm_law(prep, seq):
    law = {}
    rho0 = KET[prep] * KET[prep].H

    def rec(rho, t, outs):
        if t == len(seq):
            pr = sp.nsimplify(sp.simplify(rho.trace()))
            if pr != 0:
                law[tuple(outs)] = law.get(tuple(outs), 0) + pr
            return
        for o in (0, 1):
            P = PROJ[(seq[t], o)]
            rec(sp.simplify(P * rho * P), t + 1, outs + [o])
    rec(rho0, 0, [])
    return {k: F(int(sp.fraction(v)[0]), int(sp.fraction(v)[1])) for k, v in law.items()}


def block_A():
    # A0 bijectivity of every measurement step on the full 256-state space
    states = list(product((0, 1), repeat=8))
    ok = True
    for t in range(3):
        for k in 'ZXY':
            for dist in (True, False):
                img = {meas_step(s, t, k, dist) for s in states}
                ok &= len(img) == 256
    check('A0', ok, 'every measurement step (3 slots x 3 bases x disturb on/off) is a bijection of 2^8 states')

    # A1 records against qubit QM: 6 preparations x 39 sequences
    seqs = [s for L in (1, 2, 3) for s in product('ZXY', repeat=L)]
    nmatch = 0
    total = 0
    for prep in TOY_PREP:
        for seq in seqs:
            total += 1
            nmatch += toy_law(prep, seq) == qm_law(prep, seq)
    check('A1', nmatch == total == 234,
          f'toy-bit records equal qubit Pauli-eigenstate sequential Luders records: {nmatch}/{total}')

    # A1b complementarity and order effect, exact instances
    l1 = toy_law('Z0', ('Z', 'X', 'Z'))
    l2 = toy_law('Z0', ('Z', 'Z', 'Z'))
    pz3_1 = sum(v for k, v in l1.items() if k[2] == 0)
    pz3_2 = sum(v for k, v in l2.items() if k[2] == 0)
    check('A1b', (pz3_1, pz3_2) == (F(1, 2), F(1)),
          f'P(third Z = 0 | Z0): after an intervening X {pz3_1}, without {pz3_2} (QM: 1/2, 1)')

    # A2 cone lemma on the visible pointer: Kraus operators induced on pointer p1 by one Z
    # measurement, hidden = (a, b, r1) under the Z0 prior, are 0/1 partial permutations and the
    # channel computed by Ad_U then partial trace equals the Kraus channel.
    hid = [(a, b, r) for a in (0, 1) for b in (0, 1) for r in (0, 1)]
    prior = {h: (F(1, 4) if h[0] == 0 else F(0)) for h in hid}  # a = 0, b and r uniform
    def U(p, h):
        s = meas_step((h[0], h[1], p, 0, 0, h[2], 0, 0), 0, 'Z')
        return s[2], (s[0], s[1], s[5])
    ok_pp = True
    kraus = []
    for h in hid:
        if prior[h] == 0:
            continue
        for hp in hid:
            K = sp.zeros(2, 2)
            for p in (0, 1):
                pp, hh = U(p, h)
                if hh == hp:
                    K[pp, p] = 1
            if K != sp.zeros(2, 2):
                ok_pp &= all(sum(K[i, j] for j in range(2)) <= 1 for i in range(2))
                ok_pp &= all(sum(K[i, j] for i in range(2)) <= 1 for j in range(2))
                kraus.append((prior[h], K))
    ok_ch = True
    for i in range(2):
        for j in range(2):
            E = sp.zeros(2, 2)
            E[i, j] = 1
            out_k = sum((sp.Rational(w.numerator, w.denominator) * K * E * K.T for w, K in kraus), sp.zeros(2, 2))
            # direct: Ad_U on E (x) rho_H, partial trace over hidden
            out_d = sp.zeros(2, 2)
            for h in hid:
                if prior[h] == 0:
                    continue
                pi, hi = U(i, h)
                pj, hj = U(j, h)
                if hi == hj:
                    out_d[pi, pj] += sp.Rational(prior[h].numerator, prior[h].denominator)
            ok_ch &= out_k == out_d
    check('A2', ok_pp and ok_ch,
          f'visible-pointer map of one Z measurement: {len(kraus)} Kraus terms, all 0/1 partial permutations; Kraus channel = Ad_U + partial trace on all 4 matrix units')

    # A3 the same carrier without disturbance: still bijective (A0), records leave QM
    nd = toy_law('Z0', ('Z', 'X', 'Z'), disturb=False)
    qm = qm_law('Z0', ('Z', 'X', 'Z'))
    nd2 = toy_law('X0', ('Z', 'X'), disturb=False)
    check('A3', nd != qm and nd == {(0, 0, 0): F(1, 2), (0, 1, 0): F(1, 2)} and qm == {(0, 0, 0): F(1, 4), (0, 0, 1): F(1, 4), (0, 1, 0): F(1, 4), (0, 1, 1): F(1, 4)},
          f'non-disturbing bijections on the same carrier: law(Z0; Z,X,Z) = {sorted(nd.items())} vs QM uniform on p2,p3; X0 then Z,X gives {sorted(nd2.items())}: X repeat survives an intervening Z (QM: 1/2)')

    # A4 response-table PR box: a global setting-dependent bijection gives S = 4
    S = 0
    for a, b in product((0, 1), repeat=2):
        E = 0
        for lam in (0, 1):
            q, r = lam, lam ^ (a & b)
            E += F(1, 2) * (-1) ** (q ^ r)
        S += (-1) ** (a & b) * E
    check('A4', S == 4, f'response-table box with global setting dependence: S_CHSH = {S} (representability admits non-quantum laws)')


# ----------------------------------------------------------------------------------------------
# Block B: Bell under OI's actual readout
# ----------------------------------------------------------------------------------------------
PERM4 = list(permutations(range(4)))


def ca_step(cells, pi, phase):
    c = list(cells)
    L = len(c)
    for i in range(phase, L, 2):
        j = (i + 1) % L
        v = pi[2 * c[i] + c[j]]
        c[i], c[j] = v >> 1, v & 1
    return c


def block_B():
    L = 8
    best = 0
    attain = 0
    cone_ok = True
    for pe in PERM4:
        for po in PERM4:
            rule_best = 0
            for om in product((0, 1), repeat=6):  # cells 1,2,3,4,6,7
                qa = {}
                rb = {}
                for a, b in product((0, 1), repeat=2):
                    cells = [a, om[0], om[1], om[2], om[3], b, om[4], om[5]]
                    c = ca_step(ca_step(cells, pe, 0), po, 1)
                    qa.setdefault(a, set()).add(c[1])
                    rb.setdefault(b, set()).add(c[4])
                if any(len(v) != 1 for v in qa.values()) or any(len(v) != 1 for v in rb.values()):
                    cone_ok = False
                    continue
                q = {a: next(iter(qa[a])) for a in (0, 1)}
                r = {b: next(iter(rb[b])) for b in (0, 1)}
                S = sum((-1) ** (a & b) * (-1) ** (q[a] ^ r[b]) for a, b in product((0, 1), repeat=2))
                rule_best = max(rule_best, abs(S))
            best = max(best, rule_best)
            attain += rule_best == 2
    check('B1', cone_ok and best == 2 and attain > 0,
          f'local partitioned automaton, ring of 8, all 576 rule pairs x 64 pre-setting microstates: cone respected at every point, max |S| = {best} (attained by {attain} rule pairs); every setting-independent prior gives |S| <= 2')

    # B1m can-fail countercontrol: two more steps (even, odd, even, odd) let the cones meet
    best3 = 0
    viol = 0
    for pe in PERM4:
        for po in PERM4:
            for om in product((0, 1), repeat=6):
                q = {}
                r = {}
                for a, b in product((0, 1), repeat=2):
                    cells = [a, om[0], om[1], om[2], om[3], b, om[4], om[5]]
                    c = ca_step(ca_step(ca_step(ca_step(cells, pe, 0), po, 1), pe, 0), po, 1)
                    q[(a, b)], r[(a, b)] = c[1], c[4]
                if q[(0, 0)] != q[(0, 1)] or q[(1, 0)] != q[(1, 1)] or r[(0, 0)] != r[(1, 0)] or r[(0, 1)] != r[(1, 1)]:
                    viol += 1
                S = sum((-1) ** (a & b) * (-1) ** (q[(a, b)] ^ r[(a, b)]) for a, b in product((0, 1), repeat=2))
                best3 = max(best3, abs(S))
    # every 2-bit bijection is affine over GF(2), so this automaton's outputs are affine in the
    # settings and |S| <= 2 pointwise even where the cones overlap; PR needs a nonaffine block (B2)
    def affine(pi):
        f = lambda v: (pi[2 * v[0] + v[1]] >> 1, pi[2 * v[0] + v[1]] & 1)
        c = f((0, 0))
        ok = True
        for u in product((0, 1), repeat=2):
            for v in product((0, 1), repeat=2):
                fu, fv = f(u), f(v)
                fuv = f((u[0] ^ v[0], u[1] ^ v[1]))
                ok &= all(fuv[i] == fu[i] ^ fv[i] ^ c[i] for i in range(2))
        return ok
    naff = sum(affine(pi) for pi in PERM4)
    check('B1m', viol > 0 and best3 == 2 and naff == 24,
          f'countercontrol, readout after four steps on the same ring: remote-setting dependence detected at {viol} (rule, microstate) points; max |S| = {best3} because all {naff}/24 two-bit bijections are affine; the PR control needs a nonaffine (Toffoli-class) block, B2')

    # B1a affine boxes with remote dependence: q, r affine in (a, b) over GF(2) (64 pairs)
    vals = set()
    remote = 0
    for cq in product((0, 1), repeat=3):
        for cr in product((0, 1), repeat=3):
            q = lambda a, b: cq[0] ^ (cq[1] & a) ^ (cq[2] & b)
            r = lambda a, b: cr[0] ^ (cr[1] & a) ^ (cr[2] & b)
            remote += (cq[2] == 1) or (cr[1] == 1)
            vals.add(sum((-1) ** (a & b) * (-1) ** (q(a, b) ^ r(a, b)) for a, b in product((0, 1), repeat=2)))
    check('B1a', vals == {2, -2} and remote == 48,
          f'pointwise boxes with q, r affine in both settings (48 of 64 with remote dependence): S values {sorted(vals)}; affine dynamics with bit readout cannot exceed 2 even across cones')

    # B2 one long edge: cells a=0 q=1 l1=2 l2=3 r=4 b=5 s=6 spare=7
    def long_edge_run(cells):
        c = list(cells)
        c[1] ^= c[2]            # local CNOT (block 1,2)
        c[4] ^= c[3]            # local CNOT (block 3,4)
        c[4] ^= c[6] & c[0] & c[5]   # long edge: block (0, 5, 6, 4)
        return c
    allst = list(product((0, 1), repeat=8))
    bij = len({tuple(long_edge_run(s)) for s in allst}) == 256

    def box(w):
        P = {}
        for a, b in product((0, 1), repeat=2):
            for lam in (0, 1):
                for s, ws in ((0, 1 - w), (1, w)):
                    cells = [a, 0, lam, lam, 0, b, s, 0]
                    c = long_edge_run(cells)
                    key = (a, b, c[1], c[4])
                    P[key] = P.get(key, 0) + F(1, 2) * ws
        return P

    def chsh(P):
        S = 0
        for a, b in product((0, 1), repeat=2):
            E = sum(P.get((a, b, q, r), 0) * (-1) ** (q ^ r) for q, r in product((0, 1), repeat=2))
            S += (-1) ** (a & b) * E
        return S

    def nosig(P):
        ok = True
        for a in (0, 1):
            for q in (0, 1):
                m = {sum(P.get((a, b, q, r), 0) for r in (0, 1)) for b in (0, 1)}
                ok &= len(m) == 1
        for b in (0, 1):
            for r in (0, 1):
                m = {sum(P.get((a, b, q, r), 0) for q in (0, 1)) for a in (0, 1)}
                ok &= len(m) == 1
        return ok
    P1 = box(F(1))
    check('B2', bij and chsh(P1) == 4 and nosig(P1),
          f'one long edge (cells 0,5,6 -> 4), setting-independent prior: bijective {bij}; S = {chsh(P1)}; operational no-signalling {nosig(P1)}')
    rows = []
    ok = True
    for w in (F(0), F(1, 5), F(2, 5), F(1, 2), F(3, 5), F(1)):
        P = box(w)
        S = chsh(P)
        ok &= S == 2 + 2 * w and nosig(P)
        rows.append(f'w={w}:S={S}:{"S>2sqrt2" if S * S > 8 else "S<=2sqrt2"}')
    check('B2b', ok, 'tunable prior weight w on the long edge gives S = 2 + 2w exactly, no-signalling throughout: ' + ', '.join(rows))

    # B3 measurement-dependent local model (lambda = (q, r) drawn from the target box given a, b)
    def mi_bits(boxp):
        # Z = (a, b) uniform; lambda = (q, r); I = H(lambda) - H(lambda | Z)
        pl = {}
        HlZ = 0
        for a, b in product((0, 1), repeat=2):
            for q, r in product((0, 1), repeat=2):
                p = boxp(a, b, q, r)
                pl[(q, r)] = pl.get((q, r), 0) + p / 4
                if p != 0:
                    HlZ += -sp.Rational(1, 4) * p * sp.log(p, 2)
        Hl = sum(-p * sp.log(p, 2) for p in pl.values() if p != 0)
        return sp.simplify(Hl - HlZ)
    pr = lambda a, b, q, r: sp.Rational(1, 2) if (q ^ r) == (a & b) else 0
    cT = (2 + sp.sqrt(2)) / 4
    ts = lambda a, b, q, r: (cT / 2) if (q ^ r) == (a & b) else ((1 - cT) / 2)
    out = []
    ok = True
    for name, bx, S in (('PR', pr, sp.Integer(4)), ('Tsirelson', ts, 2 * sp.sqrt(2))):
        I = mi_bits(bx)
        bound = 2 + 4 * sp.sqrt(2 * sp.log(2) * I)
        holds = sp.N(bound - S, 50) >= 0  # [NUM] 50-digit comparison of a transcendental bound
        ok &= bool(holds)
        out.append(f'{name}: S={sp.nsimplify(S)}, I={sp.N(I, 12)} bits, bound={sp.N(bound, 12)}')
    check('B3', ok, '[NUM comparison] measurement-dependent local models reach any S; Main bound S <= 2+4sqrt(2 ln2 I) respected: ' + '; '.join(out))


# ----------------------------------------------------------------------------------------------
# Block C: preparation contextuality
# ----------------------------------------------------------------------------------------------
def pnc_pom_lp(n_lambda, response_sets):
    """Max POM success over preparation-noncontextual models on n_lambda ontic states.
    PNC + parity obliviousness: sum_{x parity 0} mu_x = sum_{x parity 1} mu_x as ontic
    distributions. response_sets[y] = list of deterministic functions lambda -> guess bit."""
    xs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    best = None
    arg = None
    for g0 in response_sets[0]:
        for g1 in response_sets[1]:
            mu = {(x, l): sp.Symbol(f'm_{x[0]}{x[1]}_{l}') for x in xs for l in range(n_lambda)}
            cons = [sp.Ge(v, 0) for v in mu.values()]
            for x in xs:
                cons.append(sp.Eq(sum(mu[(x, l)] for l in range(n_lambda)), 1))
            for l in range(n_lambda):
                cons.append(sp.Eq(mu[((0, 0), l)] + mu[((1, 1), l)], mu[((0, 1), l)] + mu[((1, 0), l)]))
            obj = sp.Rational(1, 8) * sum(mu[(x, l)] * ((g0[l] == x[0]) + (g1[l] == x[1]))
                                          for x in xs for l in range(n_lambda))
            val, _ = lpmax(obj, cons)
            if best is None or val > best:
                best, arg = val, (g0, g1)
    return best, arg


def block_C():
    # C1 a C4-satisfying delay line: (x, h) -> (h, x); fixed readout of x at t = 0, 1, 2
    law = {}
    for x0, h0 in product((0, 1), repeat=2):
        xs_ = [x0]
        x, h = x0, h0
        for _ in range(2):
            x, h = h, x
            xs_.append(x)
        law[tuple(xs_)] = law.get(tuple(xs_), 0) + F(1, 4)
    def cond(x2, x1, x0):
        num = law.get((x0, x1, x2), 0)
        den = sum(law.get((x0, x1, z), 0) for z in (0, 1))
        return num / den
    c4 = cond(0, 0, 0) != cond(0, 0, 1)
    # record map mu(x0,h0) -> law(x0, x1): x1 = h0, so the map is the identity on the 4-simplex
    M = sp.Matrix([[1 if (x0, h0) == (u, v) else 0 for (x0, h0) in product((0, 1), repeat=2)]
                   for (u, v) in product((0, 1), repeat=2)])
    check('C1', c4 and M.rank() == 4,
          f'delay line satisfies C4: P(x2=0|x1=0,x0=0) = {cond(0, 0, 0)}, P(x2=0|x1=0,x0=1) = {cond(0, 0, 1)}; record map on hidden distributions has rank {M.rank()}/4, so operationally equivalent preparations have identical ontic distributions (preparation noncontextual)')

    # C2 toy-bit operational map: (P(a=0), P(b=0), P(a^b=0), 1) from mu on (a, b)
    ab = list(product((0, 1), repeat=2))
    T = sp.Matrix([[1 if a == 0 else 0 for a, b in ab],
                   [1 if b == 0 else 0 for a, b in ab],
                   [1 if (a ^ b) == 0 else 0 for a, b in ab],
                   [1 for _ in ab]])
    check('C2', T.rank() == 4,
          f'toy bit: single-measurement statistics already determine the ontic distribution (rank {T.rank()}/4): preparation noncontextual')

    # C3 PNC POM ceiling, exact LP, 4 ontic states, every deterministic response function
    allf = list(product((0, 1), repeat=4))
    best_all, _ = pnc_pom_lp(4, [allf, allf])
    # toy-restricted decodings: read a partition k and post-process
    toyf = []
    for k in range(3):
        for post in product((0, 1), repeat=2):
            toyf.append(tuple(post[[a, b, a ^ b][k]] for a, b in ab))
    toyf = sorted(set(toyf))
    best_toy, _ = pnc_pom_lp(4, [toyf, toyf])
    # can-fail countercontrol: drop the PNC constraint (only operational parity obliviousness
    # would remain, which for an injective record map is the same; here we drop it entirely)
    xs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    free_best = max(F(sum((g0[2 * x[0] + x[1]] == x[0]) + (g1[2 * x[0] + x[1]] == x[1]) for x in xs), 8)
                    for g0 in allf for g1 in allf)
    check('C3', best_all == sp.Rational(3, 4) and best_toy == sp.Rational(3, 4) and free_best == 1,
          f'exact LP: PNC parity-oblivious multiplexing ceiling {best_all} (any response functions), {best_toy} (toy decodings); without parity obliviousness {free_best} (countercontrol)')

    # C4 hidden-label (shadow-type) construction: hidden label x and uniform u in {0..N-1};
    # measuring axis m writes [u < N round_N((1 + n_x . m)/2)] into a pointer (a bijection).
    # Accessible axes: 16 directions in the XZ plane and +-Y.
    s2 = sp.sqrt(2)
    nvec = {(x0, x1): ((-1) ** x1 / s2, 0, (-1) ** x0 / s2) for x0, x1 in product((0, 1), repeat=2)}  # (X, Y, Z)
    axes = [(sp.sin(sp.pi * j / 8), 0, sp.cos(sp.pi * j / 8)) for j in range(16)] + [(0, 1, 0), (0, -1, 0)]

    def rnd(p, N):
        return sp.floor(N * p + sp.Rational(1, 2)) / N

    rows = []
    ok = True
    for N in (4, 8, 100):
        po = True
        for m in axes:
            pr = {x: rnd(sp.nsimplify((1 + sum(nvec[x][i] * m[i] for i in range(3))) / 2), N) for x in nvec}
            po &= sp.simplify(pr[(0, 0)] + pr[(1, 1)] - pr[(0, 1)] - pr[(1, 0)]) == 0
        # success: y = 0 reads Z (guess x0 = outcome), y = 1 reads X (guess x1)
        succ = 0
        for x in nvec:
            pz = rnd((1 + nvec[x][2]) / 2, N)
            px = rnd((1 + nvec[x][0]) / 2, N)
            succ += sp.Rational(1, 8) * ((pz if x[0] == 0 else 1 - pz) + (px if x[1] == 0 else 1 - px))
        succ = sp.nsimplify(succ)
        rows.append(f'N={N}: parity-oblivious on all 18 axes {po}, success {succ}')
        ok &= po
    q = (1 + 1 / s2) / 2
    ok &= rows[0].endswith('3/4') and rnd(q, 8) == sp.Rational(7, 8) and rnd(q, 100) == sp.Rational(17, 20)
    # ontic distributions of the two parity mixtures differ (labels {00,11} vs {01,10})
    check('C4', ok,
          '; '.join(rows) + f'; QM value (1+1/sqrt2)/2; parity-0 and parity-1 mixtures have disjoint hidden-label supports (preparation contextual)')


def block_C5():
    # classical 2-bit ontology; accessible measurements: read bit y into a fresh pointer, then the
    # other bit is overwritten by fresh hidden randomness (destructive complementary readouts)
    def run(b0, b1, seq, rs):
        bits = [b0, b1]
        rec = []
        for t, y in enumerate(seq):
            rec.append(bits[y])
            bits[1 - y] ^= rs[t]
        return tuple(rec)

    def law(prep_mix, seq):
        L = {}
        for (b0, b1), w in prep_mix.items():
            for rs in product((0, 1), repeat=len(seq)):
                k = run(b0, b1, seq, rs)
                L[k] = L.get(k, 0) + w * F(1, 2 ** len(seq))
        return {k: v for k, v in L.items() if v != 0}

    def prep(x, w):
        mix = {lam: (1 - w) * F(1, 4) for lam in product((0, 1), repeat=2)}
        mix[x] += w
        return mix

    # the bijection: pointer ^= b_y; b_(1-y) ^= r (checked on 2^4 states)
    st = list(product((0, 1), repeat=4))
    def step(s, y):
        b = [s[0], s[1]]
        p = s[2] ^ b[y]
        b[1 - y] ^= s[3]
        return (b[0], b[1], p, s[3])
    bij = all(len({step(s, y) for s in st}) == 16 for y in (0, 1))
    seqs = [q for L in (1, 2, 3) for q in product((0, 1), repeat=L)]
    rows = []
    ok = bij
    for w in (F(1), F(7, 10), F(1, 2)):
        par0 = {}
        par1 = {}
        for x in ((0, 0), (1, 1)):
            for k, v in prep(x, w).items():
                par0[k] = par0.get(k, 0) + v / 2
        for x in ((0, 1), (1, 0)):
            for k, v in prep(x, w).items():
                par1[k] = par1.get(k, 0) + v / 2
        obl = all(law(par0, q) == law(par1, q) for q in seqs)
        onticdiff = par0 != par1
        succ = sum(F(1, 8) * sum(v for k, v in law(prep(x, w), (y,)).items() if k[0] == x[y])
                   for x in product((0, 1), repeat=2) for y in (0, 1))
        ok &= obl and onticdiff and succ == (1 + w) / 2
        rows.append(f'w={w}: parity-oblivious on all {len(seqs)} sequences {obl}, ontic mixtures differ {onticdiff}, success {succ}')
    check('C5', ok, 'destructive complementary readouts on a classical 2-bit ontology (bijective ' + str(bij) + '): ' + '; '.join(rows) + '; PNC ceiling 3/4, QM (1+1/sqrt2)/2 at w = 1/sqrt2')


# ----------------------------------------------------------------------------------------------
# Block K: Peres-Mermin
# ----------------------------------------------------------------------------------------------
def block_K():
    rows = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    cols = [(0, 3, 6), (1, 4, 7), (2, 5, 8)]
    target = [1, 1, 1, 1, 1, -1]
    nc = 0
    for v in product((1, -1), repeat=9):
        prods = [v[i] * v[j] * v[k] for (i, j, k) in rows + cols]
        nc += prods == target
    # context-indexed responses: each context gets its own triple
    ctx_ok = all(any(t[0] * t[1] * t[2] == tg for t in product((1, -1), repeat=3)) for tg in target)
    X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    kron = sp.kronecker_product
    grid = [kron(X, I2), kron(I2, X), kron(X, X), kron(I2, Z), kron(Z, I2), kron(Z, Z),
            kron(X, Z), kron(Z, X), kron(Y, Y)]
    qprods = [sp.simplify(grid[i] * grid[j] * grid[k]) for (i, j, k) in rows + cols]
    qok = all(qprods[n] == target[n] * sp.eye(4) for n in range(6))
    check('K1', nc == 0 and ctx_ok and qok,
          f'Peres-Mermin: noncontextual assignments satisfying all six contexts {nc}/512; context-indexed deterministic responses exist {ctx_ok}; operator identities hold {qok}')


# ----------------------------------------------------------------------------------------------
# Block D: double stochasticity under the uniform prior (replay of Main 3.1)
# ----------------------------------------------------------------------------------------------
def triangle_ok(l2):
    # l2: squared lengths (rationals); triangle inequality for each side, exact
    for i in range(3):
        a2, b2, c2 = l2[i], l2[(i + 1) % 3], l2[(i + 2) % 3]
        d = a2 - b2 - c2
        if d > 0 and d * d > 4 * b2 * c2:
            return False
    return True


def block_D():
    nV, nH = 3, 2
    st = [(v, h) for v in range(nV) for h in range(nH)]
    mats = set()
    for perm in permutations(range(len(st))):
        T = [[F(0)] * nV for _ in range(nV)]
        for idx, (v, h) in enumerate(st):
            v2, _ = st[perm[idx]]
            T[v][v2] += F(1, nH)
        mats.add(tuple(tuple(r) for r in T))
    ds = all(all(sum(r) == 1 for r in m) and all(sum(m[i][j] for i in range(nV)) == 1 for j in range(nV)) for m in mats)
    fail = 0
    for m in mats:
        ok = True
        for i, j in ((0, 1), (0, 2), (1, 2)):
            ok &= triangle_ok([m[i][k] * m[j][k] for k in range(3)])
        fail += not ok
    witness = ((F(1, 2), F(1, 2), F(0)), (F(1, 2), F(0), F(1, 2)), (F(0), F(1, 2), F(1, 2)))
    wfails = not all(triangle_ok([witness[i][k] * witness[j][k] for k in range(3)]) for i, j in ((0, 1), (0, 2), (1, 2)))
    check('D1', len(mats) == 21 and ds and fail == 6 and wfails,
          f'uniform-prior marginals of all 720 bijections at (nV, nH) = (3, 2): {len(mats)} distinct one-step matrices, all doubly stochastic {ds}; {fail} fail the row-pair triangle condition necessary for unistochasticity (Main 3.1: 21 and 6)')


if __name__ == '__main__':
    block_A()
    block_B()
    block_C()
    block_C5()
    block_K()
    block_D()
    npass = sum(ok for _, ok, _ in RESULTS)
    print(f'TOTAL {npass} PASS, {len(RESULTS) - npass} FAIL')
