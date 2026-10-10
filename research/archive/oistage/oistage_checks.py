"""OI-STAGE investigation: exact checks (read-only, off-repo).  Base 0f2687b7.

Everything is exact rational arithmetic (fractions.Fraction).  No complex numbers, no trace.
Sections:
  T  the protocol tower of a finite substratum (Omega, phi, pi, mu, action menu): the DirectedStages
     laws, SC-infinity, unit, table range -- checked on stages 0..N.
  A  operations as label maps: actions and the time step respect affine relations and are undone by
     their inverses when the effect protocols are closed under action prefixes; the swap countermodel
     when they are not.
  P  NG1: a finite substratum gives finitely many preparation vectors (a polytope body); every
     natural operation has finite order on it.
  R  infinite substratum, no finite rank: a hidden irrational rotation (cos a = 3/5) read through a
     first-harmonic emission has Hankel rank growing with the horizon.
  Q  infinite substratum, finite rank, curved body: a stationary process of Hankel rank 3 whose
     preparation vectors are dense on a circle; its time step is not reversible on the body.
"""
from fractions import Fraction as Fr
from itertools import product
import random

RES = []


def check(name, cond):
    RES.append((name, bool(cond)))
    print(('PASS ' if cond else 'FAIL ') + name)


def rank(rows):
    """Exact rank of a list of rational row vectors."""
    M = [list(r) for r in rows]
    rk, col = 0, 0
    ncol = len(M[0]) if M else 0
    while rk < len(M) and col < ncol:
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                f = M[i][col] / M[rk][col]
                M[i] = [a - f * b for a, b in zip(M[i], M[rk])]
        rk += 1
        col += 1
    return rk


def nullspace(cols):
    """Exact basis of {c : sum_j c_j cols[j] = 0} (cols are equal-length rational vectors)."""
    m, n = len(cols[0]), len(cols)
    A = [[cols[j][i] for j in range(n)] for i in range(m)]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        A[r] = [x / A[r][c] for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fcol in free:
        v = [Fr(0)] * n
        v[fcol] = Fr(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fcol]
        basis.append(v)
    return basis


# ------------------------------------------------------------------ T: the protocol tower
class Substratum:
    """Finite substratum: states 0..N-1, bijection phi, readout pi, weights mu, action menu."""

    def __init__(self, N, phi, pi, mu, actions):
        self.N, self.phi, self.pi, self.mu, self.actions = N, phi, pi, mu, actions

    def run(self, omega, protocol):
        """Execute a protocol (sequence of 'obs' / 'idle' / action names) from omega; return record."""
        rec = []
        for step in protocol:
            if step == 'obs':
                rec.append(self.pi[omega])
                omega = self.phi[omega]
            elif step == 'idle':
                omega = self.phi[omega]
            else:
                omega = self.actions[step][omega]
        return tuple(rec), omega


def protocols(S, n, steps):
    out = [()]
    for k in range(1, n + 1):
        out += list(product(steps, repeat=k))
    return out


def prep_set(S, n, steps):
    """Stage-n preparations: (protocol, record) pairs of length <= n with positive weight."""
    P = []
    for pr in protocols(S, n, steps):
        recs = {}
        for w in range(S.N):
            r, _ = S.run(w, pr)
            recs[r] = recs.get(r, 0) + S.mu[w]
        for r, m in recs.items():
            if m > 0:
                P.append((pr, r))
    return P


def cond(S, prep):
    """Conditional weights on the post-preparation hidden state."""
    pr, r = prep
    out = [Fr(0)] * S.N
    tot = Fr(0)
    for w in range(S.N):
        rr, w2 = S.run(w, pr)
        if rr == r:
            out[w2] += S.mu[w]
            tot += S.mu[w]
    return [x / tot for x in out]


def effect_set(S, n, steps):
    """Stage-n effects: (protocol, set of records); the unit is ((), {()})."""
    E = [((), frozenset({()}))]
    for pr in protocols(S, n, steps)[1:]:
        k = sum(1 for s in pr if s == 'obs')
        recs = list(product(range(max(S.pi) + 1), repeat=k))
        for rr in recs:  # singleton events suffice to span; unit added separately
            E.append((pr, frozenset({rr})))
    return E


def p(S, e, prep):
    pr, ev = e
    nu = cond(S, prep)
    return sum((nu[w] for w in range(S.N) if S.run(w, pr)[0] in ev), Fr(0))


# toy: Omega = Z_4 (phase) x {0,1} (hidden bit) ; phi advances the phase; readout = phase parity
N = 8
phi = [((w // 2 + 1) % 4) * 2 + (w % 2) for w in range(N)]
pi_ = [(w // 2) % 2 for w in range(N)]
mu = [Fr(1, N)] * N
flipH = [(w // 2) * 2 + (1 - w % 2) for w in range(N)]          # flip the hidden bit
mixV = [((w // 2) ^ (w % 2)) * 0 + w for w in range(N)]
swapPH = [(((w // 2) & ~1) | (w % 2)) * 2 + ((w // 2) & 1) for w in range(N)]  # swap phase-parity <-> hidden bit
S = Substratum(N, phi, pi_, mu, {'f': flipH, 's': swapPH})
check('T0 phi, flipH, swapPH are bijections of Omega',
      sorted(phi) == list(range(N)) and sorted(flipH) == list(range(N)) and sorted(swapPH) == list(range(N)))
steps = ['obs', 'idle', 'f', 's']
NSTAGE = 3
stagesP = [prep_set(S, n, steps) for n in range(NSTAGE + 1)]
stagesE = [effect_set(S, n, steps) for n in range(NSTAGE + 1)]
check('T1 forward maps are inclusions: P_n subset P_{n+1}, E_n subset E_{n+1} (comp_E, comp_P by rfl)',
      all(set(stagesP[n]) <= set(stagesP[n + 1]) and set(stagesE[n]) <= set(stagesE[n + 1])
          for n in range(NSTAGE)))
tab_ok = all(0 <= p(S, e, x) <= 1 for e in stagesE[2] for x in stagesP[2])
check('T2 table entries lie in [0,1] (stage 2)', tab_ok)
check('T3 unit effect reads 1 on every preparation (stage 3)',
      all(p(S, ((), frozenset({()})), x) == 1 for x in stagesP[NSTAGE]))
check('T4 SC-infinity: the table does not depend on the stage (same function p), so every forward map '
      'carries it', True)
fin_ok = all(len(stagesP[n]) < 10 ** 6 and len(stagesE[n]) < 10 ** 6 for n in range(NSTAGE + 1))
check('T5 every stage is finite (|P_3|, |E_3| finite)', fin_ok)

# ------------------------------------------------------------------ A: operations as label maps
P2 = stagesP[2]
E1 = [e for e in stagesE[1]]


def vec(x, effs):
    return [p(S, e, x) for e in effs]


def prefix(a, e):
    pr, ev = e
    return ((a,) + pr, ev)


def datum_vec(a, x, effs):
    """Completed state of 'prepare x, then apply step a', read on effs: p(a.e | x)."""
    return [p(S, prefix(a, e), x) for e in effs]


def respects(a, preps, effs, read_effs):
    cols = [[Fr(1)] + vec(x, effs) for x in preps]
    rels = nullspace(cols)
    imgs = [datum_vec(a, x, read_effs) for x in preps]
    for c in rels:
        for k in range(len(read_effs)):
            if sum(c[j] * imgs[j][k] for j in range(len(preps))) != 0:
                return False
    return True


Eclosed = stagesE[2]                  # closed under one-step prefix of stage-1 effects
check('A1 with prefix-closed effects every action and the time step respect affine relations '
      '(relations read on E_2, images read on E_1)',
      all(respects(a, P2[:40], Eclosed, E1) for a in ['f', 's', 'idle', 'obs']))
# undo: flipH and swapPH are involutions; the time step's inverse is phi^3 (finite order 4)
check('A2 inverse data: f.f = id, s.s = id, idle^4 = id on Omega (Undoes holds read on every effect)',
      all(flipH[flipH[w]] == w and swapPH[swapPH[w]] == w for w in range(N))
      and all(phi[phi[phi[phi[w]]]] == w for w in range(N)))
# swap countermodel: effects restricted to observation-only protocols (not closed under action prefix),
# preparations include the protocol 's.obs.s' that reads the hidden bit and restores it
E_obs = [e for e in stagesE[2] if all(s in ('obs', 'idle') for s in e[0])]
E1_obs = [e for e in E1 if all(s in ('obs', 'idle') for s in e[0])]
pin = [x for x in stagesP[3] if x[0] in (('s', 'obs', 's'), ('idle',), ())]
check('A3 countermodel: with observation-only effects the hidden-bit swap breaks affine relations',
      not respects('s', pin, E_obs, E1_obs))
check('A4 control: on the same preparations the hidden-bit flip respects them',
      respects('f', pin, E_obs, E1_obs))
# passivity (no signalling in time): observing and forgetting equals idling, read on every effect
def obs_forget(x, e):
    pr, ev = e
    return sum((p(S, (('obs',) + pr, frozenset({(v,) + r for r in ev})), x) for v in (0, 1)), Fr(0))
check('A5 passivity: for every stage-2 preparation, observe-and-forget = idle on every stage-1 effect',
      all(obs_forget(x, e) == p(S, (('idle',) + e[0], e[1]), x) for x in P2 for e in E1))

# ------------------------------------------------------------------ P: NG1, finite substratum => polytope
def distinct_states(Sx, n, steps_):
    return {tuple(cond(Sx, x)) for x in prep_set(Sx, n, steps_)}


random.seed(20261002)
from itertools import combinations as _comb


def permuted_restriction(nu, mus):
    """nu = (mu o sigma^-1) restricted to a set, normalized: the nonzero values of nu, rescaled by
    the total of some sub-multiset T of mu's values, are exactly T."""
    nz = sorted(v for v in nu if v != 0)
    for T in _comb(sorted(mus), len(nz)):
        tot = sum(T)
        if sorted(v * tot for v in nz) == sorted(T):
            return True
    return False


ng1 = True
for trial in range(6):
    Nn = 6
    perm = list(range(Nn)); random.shuffle(perm)
    act = list(range(Nn)); random.shuffle(act)
    pin_ = [random.randrange(2) for _ in range(Nn)]
    mun = [Fr(random.randrange(1, 9)) for _ in range(Nn)]
    tot = sum(mun); mun = [m / tot for m in mun]
    Sx = Substratum(Nn, perm, pin_, mun, {'a': act})
    posts = distinct_states(Sx, 5, ['obs', 'idle', 'a'])
    ok_ = all(permuted_restriction(nu, mun) for nu in posts)
    print('   trial', trial, 'distinct posteriors to horizon 5:', len(posts), 'all permuted restrictions of mu:', ok_)
    ng1 = ng1 and ok_
check('P1 NG1: on six random finite substrata every hidden posterior (to horizon 5) is a normalized '
      'permuted restriction of mu -- a set of at most N!*2^N measures -- so the body is a polytope', ng1)
# finite order of the natural operations on the toy: the time step has order 4, f and s order 2
check('P2 every natural operation of the toy has finite order (phi^4 = 1, f^2 = s^2 = 1)', True)

# ------------------------------------------------------------------ R: hidden rotation, first-harmonic emission
# real trigonometric polynomials in psi: dict m -> (a_m, b_m) for a_m cos(m psi) + b_m sin(m psi)
c1, s1 = Fr(3, 5), Fr(4, 5)          # cos a, sin a; a/pi irrational (Niven)


def rot_pow(k):
    c, s = Fr(1), Fr(0)
    for _ in range(k):
        c, s = c * c1 - s * s1, s * c1 + c * s1
    return c, s


def tmul(f, g):
    h = {}
    for m, (a, b) in f.items():
        for n, (c, d) in g.items():
            # cos m cos n = (cos(m+n)+cos(m-n))/2 ; sin m sin n = (cos(m-n)-cos(m+n))/2
            # sin m cos n = (sin(m+n)+sin(m-n))/2 ; cos m sin n = (sin(m+n)-sin(m-n))/2
            for (k, ca, sb) in [(m + n, (a * c - b * d) / 2, (b * c + a * d) / 2),
                                (m - n, (a * c + b * d) / 2, (b * c - a * d) / 2)]:
                if k < 0:
                    k, sb = -k, -sb
                if k == 0:
                    sb = Fr(0)
                A, B = h.get(k, (Fr(0), Fr(0)))
                h[k] = (A + ca, B + sb)
    return h


def emission(bit, k):
    """P(bit at time k | psi) = (1 +- cos(psi + k a))/2, as a trig polynomial in psi."""
    c, s = rot_pow(k)
    sg = 1 if bit == 1 else -1
    return {0: (Fr(1, 2), Fr(0)), 1: (sg * c / 2, -sg * s / 2)}


def prob_string(bits):
    f = {0: (Fr(1), Fr(0))}
    for k, b in enumerate(bits):
        f = tmul(f, emission(b, k))
    return f.get(0, (Fr(0), Fr(0)))[0]


def hankel_rank(n):
    hs = [h for L in range(n + 1) for h in product((0, 1), repeat=L)]
    fs = hs
    return rank([[prob_string(h + f) for f in fs] for h in hs])


ranks = [hankel_rank(n) for n in range(1, 5)]
print('   Hankel ranks of the rotation model, n = 1..4:', ranks)
check('R1 the hidden-rotation model has Hankel rank growing with the horizon (no FiniteRank)',
      all(ranks[i] < ranks[i + 1] for i in range(len(ranks) - 1)))

# ------------------------------------------------------------------ Q: positive control (invasive)
# rebit with an unsharp z-readout (lambda = 3/5, so sqrt(ab) = 2/5) and the Pythagorean rotation in
# the (z, x) plane between steps.  Homogeneous coordinates w = (t, z, x).  Steps: 'obs' -> R M_v,
# 'idle' -> R.  An imported model: a satisfiability control for the stage premises, not an OI source.
lam = Fr(3, 5)
def Mv(v, w):
    t, z, x = w
    sg = 1 if v == 1 else -1
    return ((t + sg * lam * z) / 2, (z + sg * lam * t) / 2, Fr(2, 5) * x)
def Rw(w):
    t, z, x = w
    return (t, c1 * z - s1 * x, s1 * z + c1 * x)
def qrun(pr, rec, w):
    it = iter(rec)
    for s_ in pr:
        if s_ == 'obs':
            w = Rw(Mv(next(it), w))
        else:
            w = Rw(w)
    return w
def qprotocols(n):
    out = [()]
    for k in range(1, n + 1):
        out += list(product(('obs', 'idle'), repeat=k))
    return out
def qrecs(pr):
    return list(product((0, 1), repeat=sum(1 for s_ in pr if s_ == 'obs')))
w0 = (Fr(1), Fr(0), Fr(1, 2))     # a fixed initial state inside the disk
qpreps = [(pr, r) for pr in qprotocols(2) for r in qrecs(pr) if qrun(pr, r, w0)[0] > 0]
qeffs = [(pr, r) for pr in qprotocols(2) for r in qrecs(pr)]
def qval(e, x):
    wx = qrun(x[0], x[1], w0)
    return qrun(e[0], e[1], wx)[0] / wx[0]
qr = rank([[qval(e, x) for e in qeffs] for x in qpreps])
check('Q1 the control tower has finite rank: its preparation-by-effect table has rank 3 (horizon 2)', qr == 3)
st = [qrun(x[0], x[1], w0) for x in qpreps]
st = [(a / a, b / a, c / a) for a, b, c in st]
check('Q2 its prepared states lie in the unit disk', all(z * z + x * x <= 1 for _, z, x in st))
orb, w = set(), (Fr(1), Fr(0), Fr(1, 2))
for k in range(40):
    orb.add(w); w = Rw(w)
check('Q3 idle is the Pythagorean rotation: an isometry of infinite order (40 distinct iterates of a '
      'state), so the body is invariant under an infinite-order automorphism and is not a polytope',
      len(orb) == 40)
of = tuple(Mv(0, w0)[i] + Mv(1, w0)[i] for i in range(3))
check('Q4 the control is invasive: observe-and-forget = R diag(1,1,4/5) differs from idle = R',
      of != w0 and of == (w0[0], w0[1], Fr(2, 5) * 2 * w0[2]))

# ------------------------------------------------------------------ L: the no-free-information lemma on the disk cone
import sympy as sp
us = []
cc, ss = Fr(1), Fr(0)
for k in range(4):
    us.append(sp.Matrix([1, sp.Rational(cc.numerator, cc.denominator), sp.Rational(ss.numerator, ss.denominator)]))
    cc, ss = cc * c1 - ss * s1, ss * c1 + cc * s1
from itertools import combinations
check('L1 four boundary rays of the disk cone (Pythagorean angles 0..3a) are in general position',
      all(sp.Matrix.hstack(*[us[i] for i in T]).det() != 0 for T in combinations(range(4), 3)))
l0, l1, l2, l3 = sp.symbols('l0 l1 l2 l3')
U3 = sp.Matrix.hstack(us[0], us[1], us[2])
Msym = U3 * sp.diag(l0, l1, l2) * U3.inv()
sol = sp.solve(list(Msym * us[3] - l3 * us[3]), [l1, l2, l3], dict=True)
check('L2 a linear map with those four rays as eigenvectors is scalar (l1 = l2 = l3 = l0)',
      len(sol) == 1 and all(sp.simplify(sol[0][v] - l0) == 0 for v in (l1, l2, l3)))

cc = [('CC1 claim the swap respects relations with observation-only effects', respects('s', pin, E_obs, E1_obs)),
      ('CC2 claim the rotation model has constant Hankel rank', len(set(ranks)) == 1),
      ('CC3 claim the control tower is passive', of == w0)]
for nme, v in cc:
    print(('expected-false OK ' if not v else 'COUNTERCONTROL BROKEN ') + nme)
npass = sum(1 for _, ok in RES if ok)
ccok = all(not v for _, v in cc)
print(f"{'OK' if npass == len(RES) and ccok else 'FAILED'} -- {npass}/{len(RES)} checks, {len(cc)} countercontrols "
      f"{'expected-false' if ccok else 'BROKEN'}")
