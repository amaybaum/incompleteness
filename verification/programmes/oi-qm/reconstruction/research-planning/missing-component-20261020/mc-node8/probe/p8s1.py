"""Node 8, step 1: section 6.10 of PREREG.md (sha256 ca5f9760...) and the controls it requires first.

Phase A (controls): I-1, I-55, I-52 digests, K-9, K-C1C4 (controls and the R1 witness candidates), access classes
(I-58), K-OPSTATE (I-49), K-IF on CL, CL-C4, K-SWAP, K-PR6 (single-system parts), the I-54 fixture, the I-59 unit test,
the A-1 scope scan and the static checks. Phase B: the mutation controls assigned to these checkpoints (KM-22, KM-25,
KM-30, KM-31, KM-32, KM-34), each as a subprocess judged in the manner of tools/mutant_verdict.py. Phase C (only over a
green Phase A and B): section 6.10 on R1a, R1b, R2a, R2b, K-SWAP and CL-C4: states, pure states, transformations,
reversibles, composites, access, Pur-E and Pur-U on the preparable set and on the convex closure, generated from the
measurements. Exact arithmetic only (fractions.Fraction and integers). Run: python3 -I -B p8s1.py (from probe/).
Amendments A-1 and A-2 (amendments/AMENDMENTS.md) govern the interpretation rule, the mutant definitions, the shared
ancilla reading and the budgets.
"""
import ast
import hashlib
import inspect
import os
import re
import subprocess
import sys
from fractions import Fraction as F
from itertools import permutations, product

HERE = os.path.dirname(os.path.abspath(__file__))
PREREG = os.path.join(HERE, '..', 'PREREG.md')
AMEND = os.path.join(HERE, '..', 'amendments', 'AMENDMENTS.md')
EXPECTED_PREREG = 'ca5f976071f3dc257c0e4abefff9b782c9eca0db9c06ddffea8df69f486bf9dd'
MUTANT = None
CHECKS = []
CHECKRES = {}
GEN = []          # every generated verdict line (A-1 scope scan)
DIGESTS = {}      # class -> input digest (I-52)
HALF = F(1, 2)


def check(cid, ok, msg):
    ok = bool(ok)
    CHECKS.append((cid, ok))
    CHECKRES[cid] = ok
    print(f'{"PASS" if ok else "FAIL"}  {cid}: {msg}')
    return ok


def sha(s):
    return hashlib.sha256(s.encode()).hexdigest()


def fs(x):
    """exact printing of a Fraction or a tuple of Fractions"""
    if isinstance(x, tuple):
        return '(' + ', '.join(fs(y) for y in x) + ')'
    return str(x)


# ---------------------------------------------------------------------------------------------------------------
# exact linear algebra on tuples of Fractions
# ---------------------------------------------------------------------------------------------------------------
class Span:
    """an incrementally built basis (row echelon) of a subspace of Q^n"""

    def __init__(self, n):
        self.n = n
        self.rows = []     # list of (pivot, vector) with vector[pivot] == 1 and zero at other pivots
        self.gens = []     # the generating vectors kept (for coordinate purposes)

    def reduce(self, v):
        v = list(v)
        for p, r in self.rows:
            c = v[p]
            if c:
                v = [a - c * b for a, b in zip(v, r)]
        return v

    def add(self, v):
        w = self.reduce(v)
        p = next((i for i, a in enumerate(w) if a), None)
        if p is None:
            return False
        inv = 1 / w[p]
        w = [a * inv for a in w]
        self.rows = [(q, [a - r[p] * b for a, b in zip(r, w)]) for q, r in self.rows]
        self.rows.append((p, w))
        self.gens.append(tuple(v))
        return True

    def contains(self, v):
        return not any(self.reduce(v))

    @property
    def dim(self):
        return len(self.rows)

    def coords(self, v):
        """coordinates of v in the pivot basis (v must lie in the span)"""
        v = list(v)
        out = []
        for p, r in self.rows:
            out.append(v[p])
        return tuple(out)


def restrict(vec, idxs):
    return tuple(vec[i] for i in idxs)


# ---------------------------------------------------------------------------------------------------------------
# the realization engine: cells, configurations, steps (bijections), readout projection, priors (condition O)
# ---------------------------------------------------------------------------------------------------------------
class Sys:
    """A realization class on its core cells. vis: visible core cells; hid: hidden core cells (each (name, size)).
    vis_anc / hid_anc: declared ancilla cells, absent from every step's domain (the static certificate of A-2).
    phi: dict -> dict on the core. perms: 'all' = every permutation of the visible-core configurations.
    couplings: list of (name, func(dict, fresh_tuple) -> dict, nfresh, text). x0s: the visible initial point masses."""

    def __init__(self, name, vis, hid, phi, phi_text, couplings, x0s, vis_anc, hid_anc, prior_text, comp_text,
                 perm_alphabet=None):
        self.name = name
        self.vis = vis
        self.hid = hid
        self.core = vis + hid
        self.phi = phi
        self.phi_text = phi_text
        self.couplings = couplings
        self.x0s = x0s
        self.vis_anc = vis_anc
        self.hid_anc = hid_anc
        self.prior_text = prior_text
        self.comp_text = comp_text
        self.names = [c for c, _ in self.core]
        self.cfgs = [dict(zip(self.names, vals)) for vals in product(*[range(s) for _, s in self.core])]
        self.keys = [self.key(d) for d in self.cfgs]
        self.idx = {k: i for i, k in enumerate(self.keys)}
        self.nv = len(vis)
        vis_cfgs = sorted({k[:self.nv] for k in self.keys})
        self.vis_cfgs = vis_cfgs
        if perm_alphabet is None:
            perms = [dict(zip(vis_cfgs, p)) for p in permutations(vis_cfgs)]
        else:
            perms = perm_alphabet
        self.perms = perms
        self.ops = [('perm', i) for i in range(len(perms))] + [('cpl', i) for i in range(len(couplings))]

    def key(self, d):
        return tuple(d[c] for c in self.names)

    def vis_of(self, k):
        return k[:self.nv]

    def hid_of(self, k):
        return k[self.nv:]

    def op_name(self, op):
        kind, i = op
        if kind == 'perm':
            p = self.perms[i]
            moved = [(a, b) for a, b in sorted(p.items()) if a != b]
            return 'perm[' + ('id' if not moved else ' '.join(f'{a}->{b}' for a, b in moved)) + ']'
        return self.couplings[i][0]

    def nfresh(self, op):
        return self.couplings[op[1]][2] if op[0] == 'cpl' else 0

    def apply_op(self, op, d, fresh=()):
        kind, i = op
        d = dict(d)
        if kind == 'perm':
            p = self.perms[i]
            new_vis = p[tuple(d[c] for c, _ in self.vis)]
            for (c, _), v in zip(self.vis, new_vis):
                d[c] = v
            return d
        return self.couplings[i][1](d, fresh)

    def step(self, op, d, fresh=()):
        """one time step: the observer's op, then phi (section 6.10 timing convention)"""
        return self.phi(self.apply_op(op, d, fresh))

    def trans(self, op):
        """for each config index: list of (prob, next index), fresh bits averaged"""
        k = self.nfresh(op)
        fr = list(product((0, 1), repeat=k))
        p = F(1, len(fr))
        out = []
        for d in self.cfgs:
            out.append([(p, self.idx[self.key(self.step(op, d, f))]) for f in fr])
        return out

    def inputs_text(self):
        """the class inputs of I-52, as declared"""
        lines = [f'class {self.name}',
                 'core visible cells ' + ', '.join(f'{c}:{s}' for c, s in self.vis),
                 'core hidden cells ' + ', '.join(f'{c}:{s}' for c, s in self.hid),
                 'visible ancillas (point masses at 0, absent from every step) ' + ', '.join(
                     f'{c}:{s}' for c, s in self.vis_anc),
                 'hidden ancillas (counting measure, for mixing, absent from every step) ' + ', '.join(
                     f'{c}:{s}' for c, s in self.hid_anc),
                 f'phi: {self.phi_text}',
                 f'accessible bijections: every permutation of the visible-core configurations ({len(self.perms)})',
                 'coupling steps: ' + ('; '.join(f'{n} = {t} (fresh bits {k})' for n, _, k, t in self.couplings)
                                       or 'none'),
                 f'visible initial point masses: {self.x0s}',
                 f'priors: {self.prior_text}',
                 f'composites: {self.comp_text}',
                 'timing: one step = selected permutation or coupling step, then phi; readout after the step']
        return '\n'.join(lines)

    def derived_text(self):
        """the same inputs re-derived from the actual step functions (truth tables), for the I-52 comparison"""
        parts = []
        for d in self.cfgs:
            parts.append(f'phi {self.key(d)}->{self.key(self.phi(d))}')
        for n, f, k, _ in self.couplings:
            for d in self.cfgs:
                for fr in product((0, 1), repeat=k):
                    parts.append(f'{n} {self.key(d)} fresh{fr}->{self.key(f(d, fr))}')
        return '\n'.join(parts)


def truth_table_text(sysm):
    """a canonical textual description of each coupling step from its truth table, used to check the declared text"""
    out = {}
    for n, f, k, _ in sysm.couplings:
        rows = []
        for d in sysm.cfgs:
            for fr in product((0, 1), repeat=k):
                rows.append((sysm.key(d), fr, sysm.key(f(d, fr))))
        out[n] = rows
    return out


# --- step functions --------------------------------------------------------------------------------------------
def phi_id(d):
    return dict(d)


def phi_swap(a, b):
    def f(d):
        d = dict(d)
        d[a], d[b] = d[b], d[a]
        return d
    return f


def clean_read(x, h):
    def f(d, fresh):
        d = dict(d)
        d[x] ^= d[h]
        return d
    return f


def destructive_read(x, h):
    def f(d, fresh):
        d = dict(d)
        d[x] ^= d[h]
        d[h] ^= fresh[0]
        return d
    return f


BIT = 2
VANC = [('v1', BIT), ('v2', BIT)]
HANC = [('m1', BIT), ('m2', BIT), ('m3', BIT)]
PRIOR1 = 'realization-datum prior on h with denominator <= 8; preparable set from the hidden ancillas (A-2 budgets)'
PRIOR2 = 'realization-datum prior on (h1, h2) with denominator <= 8; preparable set from the hidden ancillas'
COMP = ('two copies A, B with own x, h, ancillas; one shared hidden counting-measure ancilla s; joint prior = product '
        'of per-copy priors, s uniform; joint accessible class = local permutations and local coupling steps; local '
        'preparations may read s and act on the copy\'s own hidden cells only (A-2)')


def build_classes():
    C = {}
    C['R1a'] = Sys('R1a', [('x', BIT)], [('h', BIT)], phi_id, 'identity',
                   [('read', clean_read('x', 'h'), 0, 'x ^= h (clean)')], [(0,)], VANC, HANC, PRIOR1, COMP)
    cpl_b = clean_read('x', 'h') if MUTANT == 'KM-30' else destructive_read('x', 'h')
    C['R1b'] = Sys('R1b', [('x', BIT)], [('h', BIT)], phi_id, 'identity',
                   [('dread', cpl_b, 1, 'x ^= h; h ^= r, r a fresh hidden counting-measure bit per use')],
                   [(0,)], VANC, HANC, PRIOR1, COMP)
    C['R2a1'] = Sys('R2a1', [('x', BIT)], [('h1', BIT), ('h2', BIT)], phi_swap('h1', 'h2'), 'swap(h1, h2)',
                    [('read1', clean_read('x', 'h1'), 0, 'x ^= h1 (clean)')], [(0,)], VANC, HANC, PRIOR2, COMP)
    C['R2b1'] = Sys('R2b1', [('x', BIT)], [('h1', BIT), ('h2', BIT)], phi_swap('h1', 'h2'), 'swap(h1, h2)',
                    [('dread1', destructive_read('x', 'h1'), 1, 'x ^= h1; h1 ^= r (fresh bit)')], [(0,)], VANC, HANC,
                    PRIOR2, COMP)
    C['R2a2'] = Sys('R2a2', [('x1', BIT), ('x2', BIT)], [('h1', BIT), ('h2', BIT)], phi_swap('h1', 'h2'),
                    'swap(h1, h2)', [('read1', clean_read('x1', 'h1'), 0, 'x1 ^= h1 (clean)'),
                                     ('read2', clean_read('x2', 'h2'), 0, 'x2 ^= h2 (clean)')],
                    [(0, 0)], VANC, HANC, PRIOR2, COMP)
    C['R2b2'] = Sys('R2b2', [('x1', BIT), ('x2', BIT)], [('h1', BIT), ('h2', BIT)], phi_swap('h1', 'h2'),
                    'swap(h1, h2)', [('dread1', destructive_read('x1', 'h1'), 1, 'x1 ^= h1; h1 ^= r (fresh bit)'),
                                     ('dread2', destructive_read('x2', 'h2'), 1, 'x2 ^= h2; h2 ^= r (fresh bit)')],
                    [(0, 0)], VANC, HANC, PRIOR2, COMP)
    C['KSWAP'] = Sys('KSWAP', [('x', BIT)], [('h', BIT)], phi_swap('x', 'h'), 'swap(x, h)', [], [(0,)], VANC, HANC,
                     PRIOR1, COMP)
    C['CLC4'] = Sys('CLC4', [('x', BIT)], [('h', BIT)], phi_swap('x', 'h'), 'swap(x, h)', [], [(0,), (1,)], VANC,
                    HANC, PRIOR1 + ' (as K-SWAP; A-2)', COMP + ' (as R1; A-2)')
    return C


# ---------------------------------------------------------------------------------------------------------------
# K-9: condition O (bijectivity of every step on the core x fresh bits; readout = projection; prior normalized)
# ---------------------------------------------------------------------------------------------------------------
O_LOG = []


def k9(sysm):
    ok = True
    imgs = {sysm.key(sysm.phi(d)) for d in sysm.cfgs}
    ok &= len(imgs) == len(sysm.cfgs)
    for i in range(len(sysm.perms)):
        imgs = {sysm.key(sysm.apply_op(('perm', i), d)) for d in sysm.cfgs}
        ok &= len(imgs) == len(sysm.cfgs)
    for n, f, k, _ in sysm.couplings:
        dom = [(d, fr) for d in sysm.cfgs for fr in product((0, 1), repeat=k)]
        imgs = {(sysm.key(f(d, fr)), fr) for d, fr in dom}
        ok &= len(imgs) == len(dom)
    O_LOG.append((sysm.name, ok))
    return ok


# ---------------------------------------------------------------------------------------------------------------
# I-58: the access class, composed protocols with feed-forward, exact spans
# ---------------------------------------------------------------------------------------------------------------
def access(sysm, x0, Tmax, zero_step_only=False):
    """A_total(T) = span of the functionals omega_H -> P(readout sequence | omega_H, protocol) over all protocols of
    length <= T (adaptive ones add nothing: along one readout sequence an adaptive protocol is a fixed op sequence).
    Computed by the level recursion G <- span{ 1[vis = r] * E_fresh g(step_op(.)) }, seeded with the indicators of
    the final readout (so depth d = d steps, each followed by a readout; depth 0 = the readout of x0 alone); the
    d-level functions restricted to vis = x0 give the hidden functionals. Returns the per-depth dimensions, the final Span
    on the hidden configurations, and the Span on full configurations (for I-38)."""
    n = len(sysm.cfgs)
    tr = {op: sysm.trans(op) for op in sysm.ops}
    hid_keys = sorted({sysm.hid_of(k) for k in sysm.keys})
    hidx = [sysm.idx[tuple(x0) + h] for h in hid_keys]
    A = Span(len(hid_keys))
    A_full = Span(n)
    vis_vals = sysm.vis_cfgs
    # depth 0: the readout of the initial configuration alone (a zero-step protocol, A-2 D1)
    G = [tuple(F(1) if sysm.vis_of(sysm.keys[i]) == r else F(0) for i in range(n)) for r in vis_vals]
    dims = []
    depth_limit = 0 if zero_step_only else Tmax
    for depth in range(0, depth_limit + 1):
        if depth > 0:
            newG = Span(n)
            for g in G:
                for op in sysm.ops:
                    t = tr[op]
                    eg = [sum((p * g[j] for p, j in t[i]), F(0)) for i in range(n)]
                    for r in vis_vals:
                        v = tuple(eg[i] if sysm.vis_of(sysm.keys[i]) == r else F(0) for i in range(n))
                        newG.add(v)
            G = [tuple(v) for _, v in newG.rows]
        for g in G:
            A.add(restrict(g, hidx))
            for r in vis_vals:
                A_full.add(tuple(g[i] if sysm.vis_of(sysm.keys[i]) == r else F(0) for i in range(n)))
        dims.append(A.dim)
    return dims, A, A_full, hid_keys


def access_report(sysm, x0, Tmax=3, zero_step_only=False):
    dims, A, A_full, hid_keys = access(sysm, x0, Tmax, zero_step_only)
    full = A.dim == len(hid_keys)
    if full:
        kind = 'full on cells {' + ', '.join(c for c, _ in sysm.hid) + '}'
    elif A.dim == 1:
        kind = 'none (constants only)'
    else:
        kind = f'partial (dim {A.dim} of {len(hid_keys)})'
    first = next((t for t, d in enumerate(dims) if d == A.dim), None)
    text = (f'access class of {sysm.name} (x0 = {x0}): dim per depth {dims}; {kind}; reached at depth {first}; '
            f'ancilla cells {[c for c, _ in sysm.vis_anc + sysm.hid_anc]} absent from every step (invisible by the '
            f'A-2 certificate)')
    return dict(dims=dims, A=A, A_full=A_full, hid_keys=hid_keys, full=full, kind=kind, text=text)


# ---------------------------------------------------------------------------------------------------------------
# preparable sets (section 2.2's mixture rule), pure sets (preparable-weight rule), convex closure
# ---------------------------------------------------------------------------------------------------------------
def D8():
    return sorted({F(a, n) for n in range(1, 9) for a in range(0, n + 1)})


def weights(m):
    return [F(k, 2 ** m) for k in range(1, 2 ** m)]


def S_onebit(m):
    """P(h = 1) of the preparable states of a one-hidden-bit class with m hidden ancilla bits: the pushforward of
    p x uniform(m) through any permutation of the (h, m) configurations has h-marginal (k p + (2^m - k)(1 - p))/2^m,
    k the number of p-mass configurations placed in the h = 1 block (0..2^m)"""
    out = set()
    for p in D8():
        for k in range(2 ** m + 1):
            out.add((k * p + (2 ** m - k) * (1 - p)) / 2 ** m)
    return sorted(out)


def S_onebit_enumerated(m, priors):
    """the same set by explicit enumeration of all permutations of the 2^(m+1) configurations (control)"""
    cfgs = list(product((0, 1), repeat=m + 1))      # (h, m1..mm)
    out = set()
    for p in priors:
        mass = {c: (p if c[0] == 1 else 1 - p) / 2 ** m for c in cfgs}
        for perm in permutations(range(len(cfgs))):
            tot = F(0)
            for i, j in enumerate(perm):
                if cfgs[j][0] == 1:
                    tot += mass[cfgs[i]]
            out.add(tot)
    return sorted(out)


def pure_set(states, W, hints=None, convex_mutant=False):
    """states: list of tuples of Fractions (distributions); W: mixing weights (0 < w < 1).
    A state is pure iff it is not w s1 + (1 - w) s2 with w in W and s1 != s2 in states (section 2.2).
    Returns (pure list, witnesses dict state -> (w, s1, s2)). Every witness is verified exactly."""
    S = set(states)
    wit = {}
    if convex_mutant:
        # KM-32: real convex combination (extreme points of the convex hull): a witness w is then any real in (0,1)
        ext = convex_extreme(list(S))
        for s in S:
            if s not in ext:
                a, b = hull_witness(s, ext)
                wit[s] = (F(1, 3), a, b)   # a real weight that is not checked against W
        return sorted(ext), wit
    for s in sorted(S):
        found = None
        if hints and s in hints:
            for (w, s1, s2) in hints[s]:
                if w in W and s1 in S and s2 in S and s1 != s2 and all(
                        w * a + (1 - w) * b == c for a, b, c in zip(s1, s2, s)):
                    found = (w, s1, s2)
                    break
        if found is None:
            for w in W:
                for s1 in S:
                    s2 = tuple((c - w * a) / (1 - w) for a, c in zip(s1, s))
                    if min(s2) < 0:
                        continue
                    if s2 in S and s2 != s1:
                        found = (w, s1, s2)
                        break
                if found:
                    break
        if found:
            wit[s] = found
    pure = [s for s in sorted(S) if s not in wit]
    return pure, wit


def convex_extreme(points):
    """extreme points of the convex hull of finitely many points in the simplex, decided exactly: a point is extreme
    iff it is not a convex combination of the others; for our use the hull is a simplex spanned by point masses
    whenever every point mass is present, which is checked by the caller; here a direct test for dimension <= 2"""
    pts = sorted(set(points))
    if all(len(p) == 2 for p in pts):
        lo, hi = min(pts), max(pts)
        return sorted({lo, hi})
    raise NotImplementedError('convex_extreme is used for the one-dimensional fixture only')


def hull_witness(s, ext):
    return ext[0], ext[-1]


def verify_witnesses(S, W, wit):
    """I-54's exact re-check: every witness has w in W, s1 != s2 both preparable, and the identity holds"""
    S = set(S)
    for s, (w, s1, s2) in wit.items():
        if w not in W or s1 not in S or s2 not in S or s1 == s2:
            return False, s
        if any(w * a + (1 - w) * b != c for a, b, c in zip(s1, s2, s)):
            return False, s
    return True, None


# ---------------------------------------------------------------------------------------------------------------
# R2's preparable set: the (h1, h2)-marginal of the pushforward of q x uniform(m) through a permutation of the
# 4 * 2^m configurations is N q / 2^m with N a 4x4 nonnegative integer matrix with all line sums 2^m, i.e. a sum of
# 2^m permutation matrices (Koenig), so the set is the set of sums of 2^m elements of {P_sigma q}; built by dynamic
# programming on packed integers (entries < 2^16, base 2^16), with one representation kept for the witnesses.
# ---------------------------------------------------------------------------------------------------------------
SH = 28
BASE = 1 << SH


def pack(v):
    out = 0
    for a in reversed(v):
        out = out * BASE + a
    return out


def unpack(x, n=4):
    out = []
    for _ in range(n):
        out.append(x % BASE)
        x //= BASE
    return tuple(out)


def priors_R2():
    out = set()
    for n in range(1, 9):
        for a in product(range(n + 1), repeat=4):
            if sum(a) == n:
                out.add(tuple(F(x, n) for x in a))
    return sorted(out)


def S_R2(m):
    """returns (set of states as Fraction 4-tuples, hints for the pure-set search, orbit representatives used)"""
    reps = sorted({tuple(sorted(q, reverse=True)) for q in priors_R2()})
    L = 8 * 840   # common denominator: 2^m | 8 and denom(q) | 840 = lcm(1..8)
    states = {}
    hints = {}
    for q in reps:
        qi = [int(x * L) for x in q]
        units = sorted({pack([qi[i] for i in perm]) for perm in permutations(range(4))})
        # dynamic programming with back pointers (one representation per sum)
        level = {0: None}
        levels = [level]
        for _ in range(2 ** m):
            nxt = {}
            for s in level:
                for u in units:
                    t = s + u
                    if t not in nxt:
                        nxt[t] = (s, u)
            level = nxt
            levels.append(level)
        for s in level:
            vals = unpack(s)
            st = tuple(F(v, L * 2 ** m) for v in vals)
            states.setdefault(st, s)
            # the multiset of units of this representation
            us = []
            cur = s
            for lv in range(2 ** m, 0, -1):
                prev, u = levels[lv][cur]
                us.append(u)
                cur = prev
            distinct = sorted(set(us))
            hs = []
            if len(distinct) >= 2:
                u1, u2 = distinct[0], distinct[1]
                a = tuple(F(v, L * 2 ** m) for v in unpack(s - u1 + u2))
                b = tuple(F(v, L * 2 ** m) for v in unpack(s + u1 - u2))
                hs.append((HALF, a, b))
            else:
                # s is a permuted prior q' (all units equal): neighbours (a_i + 1, a_j - 1)/n of the prior
                den = 1
                for v in st:
                    den = den * v.denominator // _gcd(den, v.denominator)
                for i in range(4):
                    for j in range(4):
                        if i != j and st[j] >= F(1, den):
                            a = list(st)
                            b = list(st)
                            a[i] += F(1, den)
                            a[j] -= F(1, den)
                            b[i] -= F(1, den)
                            b[j] += F(1, den)
                            if min(b) >= 0:
                                hs.append((HALF, tuple(a), tuple(b)))
            if hs:
                hints.setdefault(st, []).extend(hs)
    return sorted(states), hints, reps


# ---------------------------------------------------------------------------------------------------------------
# transformations (I-38): maps on pre-states (distributions on core configurations) induced by protocol steps;
# well-definedness on classes = A_full invariance; reversibility on the quotient
# ---------------------------------------------------------------------------------------------------------------
def op_matrix(sysm, op):
    """column j = distribution of the step applied to configuration j"""
    n = len(sysm.cfgs)
    t = sysm.trans(op)
    M = [[F(0)] * n for _ in range(n)]
    for j in range(n):
        for p, i in t[j]:
            M[i][j] += p
    return M


def matmul(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n) if A[i][k]), F(0)) for j in range(n)] for i in range(n)]


def diag_vis(sysm, r):
    n = len(sysm.cfgs)
    return [[F(1) if (i == j and sysm.vis_of(sysm.keys[i]) == r) else F(0) for j in range(n)] for i in range(n)]


def matadd(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def row_times(a, M):
    """the functional a composed with M (a row vector times M)"""
    n = len(M)
    return tuple(sum((a[i] * M[i][j] for i in range(n) if a[i]), F(0)) for j in range(n))


def quotient_matrix(A_full, M, skip_check=False):
    """the induced map on the quotient by A_full^perp, in A_full's pivot coordinates; None if not well defined.
    With skip_check (KM-22) the class check is not performed and the flag is reported as None."""
    rows = []
    for _, a in A_full.rows:
        aM = row_times(a, M)
        if not skip_check and not A_full.contains(aM):
            return None, False
        rows.append(A_full.coords(aM) if A_full.contains(aM) else None)
    return tuple(rows), (None if skip_check else True)


def transformations(sysm, A_full, depth=2, adaptive=True):
    """all distinct induced maps from op sequences of length <= depth (and adaptive depth-2 protocols for alphabets
    of size <= 4); returns list of dicts with name, matrix, quotient matrix, well-defined flag, reversible flag"""
    singles = {op: op_matrix(sysm, op) for op in sysm.ops}
    n = len(sysm.cfgs)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    cand = [('id (no step)', I)]
    for op in sysm.ops:
        cand.append((sysm.op_name(op), singles[op]))
    if depth >= 2:
        for o1 in sysm.ops:
            for o2 in sysm.ops:
                cand.append((f'{sysm.op_name(o1)} ; {sysm.op_name(o2)}', matmul(singles[o2], singles[o1])))
    if depth >= 3:
        for o1 in sysm.ops:
            for o2 in sysm.ops:
                for o3 in sysm.ops:
                    cand.append((f'{sysm.op_name(o1)} ; {sysm.op_name(o2)} ; {sysm.op_name(o3)}',
                                 matmul(singles[o3], matmul(singles[o2], singles[o1]))))
    if adaptive and len(sysm.ops) <= 4:
        D = {r: diag_vis(sysm, r) for r in sysm.vis_cfgs}
        for o1 in sysm.ops:
            for choice in product(sysm.ops, repeat=len(sysm.vis_cfgs)):
                M = None
                for r, o2 in zip(sysm.vis_cfgs, choice):
                    part = matmul(singles[o2], matmul(D[r], singles[o1]))
                    M = part if M is None else matadd(M, part)
                cand.append((f'{sysm.op_name(o1)} ; then by readout ' +
                             ', '.join(f'{r}:{sysm.op_name(o2)}' for r, o2 in zip(sysm.vis_cfgs, choice)), M))
    skip = (MUTANT == 'KM-22')
    seen = {}
    out = []
    for name, M in cand:
        Q, flag = quotient_matrix(A_full, M, skip_check=skip)
        key = Q if Q is not None else ('ILL', tuple(tuple(r) for r in M))
        if key in seen:
            continue
        seen[key] = True
        out.append(dict(name=name, M=M, Q=Q, wd=flag))
    # reversibility on the quotient: the exact inverse of the quotient matrix must itself be a collected map
    by_Q = {}
    for t in out:
        if t['Q'] is not None and all(r is not None for r in t['Q']):
            by_Q.setdefault(t['Q'], t['name'])
    for t in out:
        t['rev'] = False
        if t['Q'] is None or any(r is None for r in t['Q']):
            continue
        inv = mat_inv(t['Q'])
        if inv is not None and inv in by_Q:
            t['rev'] = True
            t['inv'] = by_Q[inv]
    return out


def mat_inv(Q):
    """exact inverse of a square matrix given as a tuple of row tuples, or None if singular"""
    d = len(Q)
    M = [list(r) + [F(1) if i == j else F(0) for j in range(d)] for i, r in enumerate(Q)]
    for c in range(d):
        piv = next((r for r in range(c, d) if M[r][c]), None)
        if piv is None:
            return None
        M[c], M[piv] = M[piv], M[c]
        inv = 1 / M[c][c]
        M[c] = [a * inv for a in M[c]]
        for r in range(d):
            if r != c and M[r][c]:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return tuple(tuple(r[d:]) for r in M)


def state_coords(A_full, vec):
    """the operational state (coordinates on A_full) of a pre-state vector"""
    return tuple(sum((a * v for a, v in zip(arow, vec)), F(0)) for _, arow in A_full.rows)


# ---------------------------------------------------------------------------------------------------------------
# K-C1C4: C1..C4 on a realization process (exact), as PREREG section 3 states them (Main.md:74-80)
# ---------------------------------------------------------------------------------------------------------------
def process_law(cells, vis_names, init, steps, T):
    """cells: list of (name, size); init: dict cfg-key -> prob (full configurations); steps: list (per time t) of
    functions key -> list of (prob, key'). Returns list over t of dict (visible history tuple, key) -> prob."""
    names = [c for c, _ in cells]
    vis_idx = [names.index(v) for v in vis_names]

    def vis(k):
        return tuple(k[i] for i in vis_idx)
    layer = {}
    for k, p in init.items():
        if p:
            layer[((vis(k),), k)] = layer.get(((vis(k),), k), F(0)) + p
    layers = [layer]
    for t in range(T):
        nxt = {}
        for (hist, k), p in layer.items():
            for q, k2 in steps[t](k):
                key = (hist + (vis(k2),), k2)
                nxt[key] = nxt.get(key, F(0)) + p * q
        layer = nxt
        layers.append(layer)
    return layers, vis


def c1c4(cells, vis_names, hid_size, init, steps, T):
    layers, vis = process_law(cells, vis_names, init, steps, T)
    # C1: at some step t, two configurations with the same visible value and positive weight have different
    # next-visible laws
    c1 = None
    for t in range(T):
        by_cfg = {}
        for (hist, k), p in layers[t].items():
            by_cfg[k] = by_cfg.get(k, F(0)) + p
        laws = {}
        for k, p in by_cfg.items():
            law = {}
            for q, k2 in steps[t](k):
                law[vis(k2)] = law.get(vis(k2), F(0)) + q
            laws[k] = tuple(sorted(law.items()))
        groups = {}
        for k in laws:
            groups.setdefault(vis(k), set()).add(laws[k])
        for v, s in groups.items():
            if len(s) > 1:
                c1 = (t, v)
                break
        if c1:
            break
    # C4: two visible histories with positive weight, the same current value, different next-step laws
    c4 = None
    for t in range(T):
        hist_p = {}
        hist_next = {}
        for (hist, k), p in layers[t].items():
            hist_p[hist] = hist_p.get(hist, F(0)) + p
            d = hist_next.setdefault(hist, {})
            for q, k2 in steps[t](k):
                d[vis(k2)] = d.get(vis(k2), F(0)) + p * q
        laws = {}
        for hist in hist_p:
            law = tuple(sorted((v, pr / hist_p[hist]) for v, pr in hist_next[hist].items()))
            laws.setdefault(hist[-1], {}).setdefault(law, []).append(hist)
        for cur, d in laws.items():
            if len(d) > 1:
                hs = [v[0] for v in d.values()]
                c4 = (t, hs[0], hs[1], [k for k in d])
                break
        if c4:
            break
    # C3 certificate: I(X_<t; X_>t | X_t) <= log2(#distinct conditional future laws given the history, at fixed
    # X_t) <= log2 |C_H| whenever that count is <= |C_H| (the index of the conditional law screens the past)
    worst = 0
    for t in range(1, T):
        fut = {}
        hist_p = {}
        for (hist, k), p in layers[T].items():
            pre, post = hist[:t + 1], hist[t + 1:]
            d = fut.setdefault(pre, {})
            d[post] = d.get(post, F(0)) + p
            hist_p[pre] = hist_p.get(pre, F(0)) + p
        laws = {}
        for pre, d in fut.items():
            law = tuple(sorted((post, pr / hist_p[pre]) for post, pr in d.items()))
            laws.setdefault(pre[-1], set()).add(law)
        worst = max(worst, max(len(s) for s in laws.values()))
    c3 = worst <= hid_size
    return dict(C1=c1 is not None, C1w=c1, C4=c4 is not None, C4w=c4, C3=c3, C3count=worst, C3m=hid_size)


def c2_report(order_text):
    return f'C2 (structural, node reading): every step is a bijection (K-9), so no hidden record is destroyed; {order_text}'


def perm_order(f, cfgs, key):
    """order of the bijection f on the configurations"""
    order = 1
    for d in cfgs:
        k0 = key(d)
        k = key(f(d))
        n = 1
        while k != k0:
            k = key(f(dict(zip([c for c in d], k))))
            n += 1
            if n > 10 ** 4:
                return None
        order = order * n // _gcd(order, n)
    return order


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def sys_process(sysm, x0, prior_h, opseq):
    """the realization process of class sysm under the fixed op sequence opseq (one op per time step) from the
    visible point mass x0 and the hidden prior prior_h (dict hidden-key -> prob)"""
    names = sysm.names
    init = {}
    for hk, p in prior_h.items():
        init[tuple(x0) + hk] = p
    tr = {op: sysm.trans(op) for op in set(opseq)}

    def mk(op):
        t = tr[op]
        return lambda k: [(p, sysm.keys[j]) for p, j in t[sysm.idx[k]]]
    steps = [mk(op) for op in opseq]
    hid_size = 1
    for _, s in sysm.hid:
        hid_size *= s
    return c1c4(sysm.core, [c for c, _ in sysm.vis], hid_size, init, steps, len(opseq))


def k_c1c4_class(sysm, T=4, restrict_ops=None):
    """the class passes K-C1C4 iff some protocol (op sequence of length T) with some nondegenerate prior passes C1, C3
    and C4 (C2 by the structural reading); returns the witnessing protocol"""
    ops = sysm.ops if restrict_ops is None else restrict_ops
    hid_keys = sorted({sysm.hid_of(k) for k in sysm.keys})
    priors = []
    nh = len(hid_keys)
    priors.append(('uniform', {h: F(1, nh) for h in hid_keys}))
    biased = {h: F(1, nh) for h in hid_keys}
    biased[hid_keys[0]] = F(1, nh) + F(1, 3) * (1 - F(1, nh)) if nh > 1 else F(1)
    rest = (1 - biased[hid_keys[0]]) / (nh - 1) if nh > 1 else F(0)
    for h in hid_keys[1:]:
        biased[h] = rest
    priors.append(('biased', biased))
    results = []
    for x0 in sysm.x0s:
        for pname, pr in priors:
            for seq in product(ops, repeat=T):
                r = sys_process(sysm, x0, pr, seq)
                if r['C1'] and r['C3'] and r['C4']:
                    return True, (x0, pname, [sysm.op_name(o) for o in seq], r)
                results.append(r)
    return False, results


# ---------------------------------------------------------------------------------------------------------------
# the K-C1C4 controls (section 14): coin-die, Markov chain, zero coupling, tape-and-ledger
# ---------------------------------------------------------------------------------------------------------------
def coin_die():
    cells = [('x', 2), ('h', 6)]
    sigma = {(0, 1): (1, 1), (1, 1): (0, 1), (0, 2): (1, 2), (1, 2): (0, 2), (0, 3): (0, 4), (0, 4): (0, 3),
             (0, 5): (0, 6), (0, 6): (0, 5), (1, 3): (1, 4), (1, 4): (1, 3), (1, 5): (1, 6), (1, 6): (1, 5)}
    assert len(set(sigma.values())) == 12

    def step(k):
        x, h = k
        return [(F(1), tuple(v - (1 if i == 1 else 0) for i, v in enumerate(sigma[(x, h + 1)])))]
    init = {(0, h): F(1, 6) for h in range(6)}
    return c1c4(cells, ['x'], 6, init, [step] * 4, 4)


def markov_chain(T=4):
    """x flips iff the tape cell at the clock reads 0 (tape cells of size 4, uniform): P(flip) = 1/4, Markov"""
    cells = [('x', 2)] + [(f't{i}', 4) for i in range(T)] + [('c', T + 1)]

    def step(k):
        x, tape, c = k[0], k[1:T + 1], k[T + 1]
        x2 = x ^ (1 if tape[c] == 0 else 0)
        return [(F(1), (x2,) + tape + ((c + 1) % (T + 1),))]
    init = {}
    for tape in product(range(4), repeat=T):
        init[(0,) + tape + (0,)] = F(1, 4 ** T)
    return c1c4(cells, ['x'], 4 ** T * (T + 1), init, [step] * T, T)


def zero_coupling(T=4):
    cells = [('x', 2), ('h', 2)]

    def step(k):
        return [(F(1), (k[0], 1 - k[1]))]
    init = {(0, 0): F(1, 2), (0, 1): F(1, 2)}
    return c1c4(cells, ['x'], 2, init, [step] * T, T)


def tape_ledger(T=4):
    """x' = L[c] xor tape[c]; L'[c] = x; c' = c + 1 (a bijection); L initialized 0: the visible process is the fair
    coin from the tape, the ledger records x and is never read back (Main.md:172)"""
    cells = [('x', 2)] + [(f'L{i}', 2) for i in range(T)] + [(f't{i}', 2) for i in range(T)] + [('c', T + 1)]

    def step(k):
        x, L, tape, c = k[0], list(k[1:T + 1]), k[T + 1:2 * T + 1], k[2 * T + 1]
        x2 = L[c] ^ tape[c]
        L[c] = x
        return [(F(1), (x2,) + tuple(L) + tape + ((c + 1) % (T + 1),))]
    init = {}
    for tape in product((0, 1), repeat=T):
        init[(0,) + (0,) * T + tape + (0,)] = F(1, 2 ** T)
    return c1c4(cells, ['x'], 2 ** (2 * T) * (T + 1), init, [step] * T, T)


# ---------------------------------------------------------------------------------------------------------------
# K-PR6 (section 4.2): replay through the engine, records q; r, CHSH = 4, no signalling on the wing records
# ---------------------------------------------------------------------------------------------------------------
def kpr6():
    cells = [('a', 2), ('b', 2), ('q', 2), ('r', 2), ('p1', 2), ('p2', 2), ('lam', 2)]
    names = [c for c, _ in cells]

    def mk(fn):
        def st(k):
            d = dict(zip(names, k))
            fn(d)
            return [(F(1), tuple(d[c] for c in names))]
        return st

    def s1(d):
        d['p1'] ^= d['lam']

    def s2(d):
        d['p2'] ^= d['lam']

    def s3(d):
        d['q'] ^= d['p1']

    def s4(d):
        d['r'] ^= d['p2']

    def s5(d):
        d['r'] ^= d['a'] & d['b']
    steps = [mk(f) for f in (s1, s2, s3, s4, s5)]
    # bijectivity of each step on the full configuration space
    allk = list(product(*[range(s) for _, s in cells]))
    bij = all(len({st(k)[0][1] for k in allk}) == len(allk) for st in steps)
    box = {}
    c14 = {}
    for a in (0, 1):
        for b in (0, 1):
            init = {(a, b, 0, 0, 0, 0, lam): F(1, 2) for lam in (0, 1)}
            layers, vis = process_law(cells, ['a', 'b', 'q', 'r'], init, steps, 5)
            dist = {}
            for (hist, k), p in layers[5].items():
                qr = (k[2], k[3])
                dist[qr] = dist.get(qr, F(0)) + p
            box[(a, b)] = dist
            c14[(a, b)] = c1c4(cells, ['a', 'b', 'q', 'r'], 2, init, steps, 5)
    E = {}
    for (a, b), dist in box.items():
        E[(a, b)] = sum(((1 if q == r else -1) * p for (q, r), p in dist.items()), F(0))
    S = E[(0, 0)] + E[(0, 1)] + E[(1, 0)] - E[(1, 1)]
    margA = {(a, b): sum((p for (q, r), p in d.items() if q == 1), F(0)) for (a, b), d in box.items()}
    margB = {(a, b): sum((p for (q, r), p in d.items() if r == 1), F(0)) for (a, b), d in box.items()}
    nosig = all(margA[(a, 0)] == margA[(a, 1)] for a in (0, 1)) and all(margB[(0, b)] == margB[(1, b)] for b in (0, 1))
    uniform = all(v == HALF for v in list(margA.values()) + list(margB.values()))
    return dict(bij=bij, S=S, E=E, nosig=nosig, uniform=uniform, c14=c14)


# ---------------------------------------------------------------------------------------------------------------
# I-59: the two purification readings, rendered by one generator; A-1 scope
# ---------------------------------------------------------------------------------------------------------------
A1_FORBIDDEN = ('OI ', 'OI.', 'OI,', 'observational incompleteness', 'in general', 'universally', 'quantum mechanics',
                'quantum reconstruction', 'QM', 'CDP purification')


def pur_line(cls, reading, text):
    """the only function that prints a purification verdict line (A-1): class and reading are mandatory"""
    if not cls or not reading:
        raise ValueError('class and reading are mandatory')
    line = f'[{cls} | {reading}] {text}'
    GEN.append(line)
    print(line)
    return line


def render_pur(cls, grid, closure):
    """grid: dict with the preparable-set results (per budget and across the theory); closure: dict with the
    convex-closure results and Lemma K's hypothesis status. Both are printed, always (I-59)."""
    if closure is None and MUTANT != 'KM-34':
        raise ValueError('closure line required: a grid pass alone cannot print a purification verdict (I-59)')
    out = []
    for budget, r in grid:
        out.append(pur_line(cls, f'preparable set, {budget}', r))
    if closure is not None:
        out.append(pur_line(cls, 'convex closure', closure))
    return out


def i59_unit_test():
    """feeding a grid pass alone must not print any purification line"""
    before = len(GEN)
    try:
        render_pur('UNIT', [('budget m=3', 'Pur-E: holds for every state (fixture)')], None)
        printed = len(GEN) - before
        ok = False
        why = f'a grid pass alone printed {printed} line(s) without the closure line'
    except ValueError as e:
        ok = len(GEN) == before
        why = f'refused: {e}'
    del GEN[before:]
    return ok, why


def a1_scope_scan():
    bad = [l for l in GEN if any(w in l for w in A1_FORBIDDEN)]
    return bad


# ---------------------------------------------------------------------------------------------------------------
# static checks: I-4 (no floats on the verdict path), I-49 (the state code quantifies over protocols), A-1 (the
# only prints of purification lines are inside pur_line)
# ---------------------------------------------------------------------------------------------------------------
def static_checks():
    src = open(os.path.abspath(__file__), encoding='utf-8').read()
    tree = ast.parse(src)
    floats = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, float)]
    calls = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
             and n.func.id in ('float', 'round')]
    check('I-4', not floats and not calls and ('import ' + 'math') not in src,
          f'AST scan: float literals at lines {floats}, float()/round() calls at {calls}, math not imported')
    s_access = inspect.getsource(access)
    ok49 = ('for op in sysm.ops' in s_access and 'for depth in range' in s_access and 'tr[op]' in s_access)
    s_eq = inspect.getsource(kopstate)
    uses_access = 'access_report' in s_eq and 'state_coords' in s_eq
    check('I-49-static', ok49 and uses_access,
          'the state-equivalence code quantifies over the protocol class (every op, every depth) and K-OPSTATE uses it')
    # A-1: the only print of a line containing Pur-E / Pur-U is inside pur_line
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'print':
            text = ast.get_source_segment(src, node) or ''
            if ('Pur-E' in text or 'Pur-U' in text) and 'pur_line' not in text:
                hits.append(node.lineno)
    pl_line = inspect.getsourcelines(pur_line)[1]
    pl_end = pl_line + len(inspect.getsourcelines(pur_line)[0])
    hits = [h for h in hits if not (pl_line <= h < pl_end)]
    check('A1-PRINT', not hits, f'prints of purification text outside pur_line: {hits}')


# ---------------------------------------------------------------------------------------------------------------
# K-OPSTATE (I-49)
# ---------------------------------------------------------------------------------------------------------------
def kopstate(C):
    s = C['R1a']
    x0 = (0,)
    acc = access_report(s, x0, Tmax=3)
    A_full = acc['A_full']
    # passive record laws (op = identity permutation, phi = identity) at horizons 1..4
    idp = next(op for op in s.ops if op[0] == 'perm' and all(a == b for a, b in s.perms[op[1]].items()))
    read = next(op for op in s.ops if op[0] == 'cpl')
    passive_equal = True
    for T in range(1, 5):
        laws = []
        for hval in (0, 1):
            layers, vis = process_law(s.core, ['x'], {(0, hval): F(1)},
                                      [lambda k, op=idp: [(p, s.keys[j]) for p, j in s.trans(op)[s.idx[k]]]] * T, T)
            law = {}
            for (hist, k), p in layers[T].items():
                law[hist] = law.get(hist, F(0)) + p
            laws.append(tuple(sorted(law.items())))
        passive_equal &= laws[0] == laws[1]
    # the intervention x ^= h then readout
    outs = []
    for hval in (0, 1):
        d = {'x': 0, 'h': hval}
        outs.append(s.step(read, d)['x'])
    intervention_differs = outs[0] != outs[1]
    # operational states (coordinates on A_full)
    vec0 = tuple(F(1) if k == (0, 0) else F(0) for k in s.keys)
    vec1 = tuple(F(1) if k == (0, 1) else F(0) for k in s.keys)
    if MUTANT == 'KM-25':
        # equivalence from passive records only
        same_state = passive_equal
    else:
        same_state = state_coords(A_full, vec0) == state_coords(A_full, vec1)
    # C1 under the passive dynamics
    r = sys_process(s, x0, {(0,): HALF, (1,): HALF}, [idp] * 4)
    return dict(passive_equal=passive_equal, outs=outs, intervention_differs=intervention_differs,
                same_state=same_state, c1_passive=r['C1'])


# ---------------------------------------------------------------------------------------------------------------
# composites under A-2's shared-ancilla reading: psi = 1/2 (alpha_0 x beta_0 + alpha_1 x beta_1)
# ---------------------------------------------------------------------------------------------------------------
L1 = 8 * 840


def composite_onebit(S_single, W):
    """S_single: list of P(h=1) values (Fractions). Returns the set of composite states as packed ints in units of
    1/(2 L1^2) over the 4 cells (h_A, h_B) = (0,0),(0,1),(1,0),(1,1), the lookup set, and the pure set with witnesses.
    The A-side pairs (alpha_0, alpha_1) range over S_single x S_single since both conditional preparations come
    from the same copy (any prior p: alpha_s in S_h is realizable for each s separately only when both lie in
    one prior's grid G_p; this is enforced below by grouping per prior)."""
    # per-prior grids: alpha_s must both come from the same prior p (one realization datum per copy)
    grids = {}
    for p in D8():
        grids[p] = sorted({(k * p + (8 - k) * (1 - p)) / 8 for k in range(9)})
    pairs = set()
    for p, g in grids.items():
        for a0 in g:
            for a1 in g:
                pairs.add((a0, a1))
    pairs = sorted(pairs)
    pi = [(int(a0 * L1), int(a1 * L1)) for a0, a1 in pairs]
    SJ = set()
    for a0, a1 in pi:
        a0c, a1c = L1 - a0, L1 - a1
        for b0, b1 in pi:
            b0c, b1c = L1 - b0, L1 - b1
            # cells (hA,hB): 00, 01, 10, 11  (packed little-endian)
            v00 = a0c * b0c + a1c * b1c
            v01 = a0c * b0 + a1c * b1
            v10 = a0 * b0c + a1 * b1c
            v11 = a0 * b0 + a1 * b1
            SJ.add(v00 + (v01 << SH) + (v10 << (2 * SH)) + (v11 << (3 * SH)))
    return pairs, pi, SJ


def composite_onebit_pure(pairs, pi, SJ, S_single, pure_single, wit_single, W):
    """pure set of the composite by witnesses verified in SJ; fallback exhaustive for the undecided"""
    decided = set()
    pure_cands = set()
    single_mix = {}
    for s, (w, s1, s2) in wit_single.items():
        single_mix[int(s * L1)] = (w, int(s1 * L1), int(s2 * L1))

    def prod(a, b):
        ac, bc = L1 - a, L1 - b
        return 2 * (ac * bc + ((ac * b) << SH) + ((a * bc) << (2 * SH)) + ((a * b) << (3 * SH)))

    def psi(a0, a1, b0, b1):
        a0c, a1c, b0c, b1c = L1 - a0, L1 - a1, L1 - b0, L1 - b1
        return ((a0c * b0c + a1c * b1c) + ((a0c * b0 + a1c * b1) << SH) + ((a0 * b0c + a1 * b1c) << (2 * SH))
                + ((a0 * b0 + a1 * b1) << (3 * SH)))
    nwit = {'half-mixture of two products': 0, 'product with a mixed factor': 0}
    for a0, a1 in pi:
        for b0, b1 in pi:
            s = psi(a0, a1, b0, b1)
            if s in decided:
                continue
            if (a0, b0) != (a1, b1):
                s1, s2 = prod(a0, b0), prod(a1, b1)
                if s1 in SJ and s2 in SJ and s1 != s2 and s1 + s2 == 2 * s:
                    decided.add(s)
                    nwit['half-mixture of two products'] += 1
                    continue
            else:
                if a0 in single_mix:
                    w, x1, x2 = single_mix[a0]
                    if w == HALF:
                        s1, s2 = prod(x1, b0), prod(x2, b0)
                        if s1 in SJ and s2 in SJ and s1 != s2 and s1 + s2 == 2 * s:
                            decided.add(s)
                            nwit['product with a mixed factor'] += 1
                            continue
                if b0 in single_mix:
                    w, y1, y2 = single_mix[b0]
                    if w == HALF:
                        s1, s2 = prod(a0, y1), prod(a0, y2)
                        if s1 in SJ and s2 in SJ and s1 != s2 and s1 + s2 == 2 * s:
                            decided.add(s)
                            nwit['product with a mixed factor'] += 1
                            continue
            pure_cands.add(s)
    pure_cands -= decided
    # exhaustive fallback over w in W, s1 in SJ for the candidates, in packed arithmetic (w = k/8); s2 >= 0 needs
    # supp(s1) within supp(s), which prunes almost every s1 for a point mass
    pure = []
    fallback_mixed = 0
    SJu = [(x, unpack(x)) for x in sorted(SJ)]
    for s in sorted(pure_cands):
        sv = unpack(s)
        zero = [i for i, c in enumerate(sv) if c == 0]
        found = False
        for s1, s1v in SJu:
            if any(s1v[i] for i in zero):
                continue
            for w in W:
                k, den = w.numerator, w.denominator
                if any(den * c < k * a for a, c in zip(s1v, sv)):
                    continue
                num = [den * c - k * a for a, c in zip(s1v, sv)]
                if any(x % (den - k) for x in num):
                    continue
                s2 = pack([x // (den - k) for x in num])
                if s2 in SJ and s2 != s1:
                    found = True
                    break
            if found:
                break
        if found:
            fallback_mixed += 1
        else:
            pure.append(s)
    return pure, nwit, fallback_mixed


def packed_to_dist(s):
    v = unpack(s)
    tot = sum(v)
    return tuple(F(x, tot) for x in v)


# ---------------------------------------------------------------------------------------------------------------
# phase C: section 6.10 per class
# ---------------------------------------------------------------------------------------------------------------
def budgets_onebit():
    return {m: S_onebit(m) for m in range(4)}


def pur_grid_text(n_states, pure, purifs, puru, budget_label):
    k = len(pure)
    txt = (f'Pur-E: holds for {k} of {n_states} preparable states (the pure states {", ".join(pure)}; purifications '
           f'{purifs}); fails for {n_states - k} states (no pure composite state has their marginal). '
           f'Pur-U: {puru}')
    return txt


def phase_c_onebit(name, sysm, acc, trans, SJ_data, S_by_m, pure_by_m, wit_by_m, across_pure):
    """the generated lines for a one-hidden-bit class"""
    pairs, pi, SJ, pure_comp, nwit, fb = SJ_data
    pure_dists = [packed_to_dist(s) for s in pure_comp]
    point_masses = [tuple(F(1) if i == j else F(0) for i in range(4)) for j in range(4)]
    comp_is_pm = sorted(pure_dists) == sorted(point_masses)
    # per budget m = 3 (the class's declared budget) and across the theory
    S3 = S_by_m[3]
    pure3 = pure_by_m[3]
    # purifications of each pure single state: pure composite states with that A-marginal
    purif = {}
    for st in S3:
        purif[st] = [d for d in pure_dists if d[2] + d[3] == st]   # P(h_A = 1) = cells 10 + 11
    # Pur-U: for states with >= 2 purifications, a reversible transformation of B alone connecting each pair
    revs = [t for t in trans if t['rev']]
    hkeys = sorted({sysm.hid_of(k) for k in sysm.keys})
    x0 = sysm.x0s[0]

    def b_state_of(hb):
        vec = tuple(F(1) if k == tuple(x0) + (hb,) else F(0) for k in sysm.keys)
        return vec
    A_full = acc['A_full']
    coords = {hb: state_coords(A_full, b_state_of(hb)) for hb in (0, 1)}

    def connected(hb, hb2):
        target = coords[hb2]
        src = b_state_of(hb)
        for t in revs:
            img = tuple(sum((t['M'][i][j] * src[j] for j in range(len(src))), F(0)) for i in range(len(src)))
            if state_coords(A_full, img) == target:
                return t['name']
        return None
    puru_lines = []
    puru_all = True
    for st in S3:
        ps = purif[st]
        if len(ps) >= 2:
            # purifications of a point mass delta_a are delta_a x delta_b over b; need U_B: delta_b -> delta_b'
            c01 = connected(0, 1)
            c10 = connected(1, 0)
            okU = c01 is not None and c10 is not None
            puru_all &= okU
            puru_lines.append(f'state P(h=1)={fs(st)}: {len(ps)} purifications; connected on B alone: '
                              f'{"yes (" + c01 + " / " + c10 + ")" if okU else "no (no reversible transformation of B among " + str(len(revs)) + " maps delta_0 to delta_1 and back)"}')
    has_two = any(len(purif[st]) >= 2 for st in S3)
    puru_txt = ('holds for every state with two or more purifications' if (has_two and puru_all) else
                ('fails: ' + '; '.join(puru_lines) if has_two else 'vacuous (no state has two purifications)'))
    grid_lines = []
    pure_names = [f'delta_{int(p)}' if p in (0, 1) else fs(p) for p in pure3]
    purifs_txt = '; '.join(f'{fs(st)} -> {len(purif[st])}' for st in S3 if purif[st])
    grid_lines.append((f'budget m=3 (weights k/8), composite pure states = {len(pure_comp)} '
                       f'{"point masses" if comp_is_pm else "states"}',
                       pur_grid_text(len(S3), pure_names, purifs_txt, puru_txt, 'm=3')))
    for m in (0, 1, 2):
        grid_lines.append((f'budget m={m} (weights k/{2 ** m})',
                           f'preparable states {len(S_by_m[m])}, pure under the budget\'s weights {len(pure_by_m[m])}'
                           f' (the composite purification test is stated at the class budget m=3)'))
    grid_lines.append(('across the declared theory (union of the one-hidden-bit classes at m=3, weights k/8)',
                       f'preparable states {len(S3)} (identical for R1a, R1b, K-SWAP, CL-C4), pure {len(across_pure)}'
                       f': {", ".join(fs(p) for p in across_pure)}; Pur-E and Pur-U as the budget m=3 line'))
    # convex closure
    all_pm = all(pm in {packed_to_dist(s) for s in pure_comp} or
                 pack([int(c * 2 * L1 * L1) for c in pm]) in SJ for pm in point_masses)
    closure_txt = (f'convex closure of the preparable set = [0,1] (0 and 1 preparable); closure of the composite = the '
                   f'full simplex on 4 points (every point mass preparable: {all_pm}), extreme points = the 4 point '
                   f'masses, each with point-mass marginals; transformations extend affinely (every induced map is a '
                   f'pushforward, hence affine: {len(trans)} maps); Pur-E on the closure: holds for the 2 extreme states, '
                   f'fails for every non-extreme state. Lemma K hypotheses on this closure: (i) holds (delta_0, delta_1 '
                   f'perfectly distinguished: access {acc["kind"]}; every real mixture preparable by definition of the '
                   f'closure), (ii) holds (one additional system type declared), (iii) holds (4 pure states in the '
                   f'composite closure): Lemma K\'s instance.')
    lines = render_pur(name, grid_lines, closure_txt)
    return lines, comp_is_pm, all_pm, (has_two and puru_all)


def main():
    print('=== Node 8, step 1 probe (PREREG section 6.10 and its controls) ===')
    h = sha(open(PREREG, encoding='utf-8').read())
    print(f'PREREG sha256 {h}')
    check('I-1', h == EXPECTED_PREREG, 'preregistration digest equals the frozen digest')
    ha = sha(open(AMEND, encoding='utf-8').read())
    print(f'AMENDMENTS sha256 {ha} (A-1 interpretation rule; A-2 confirmatory review, readings and budgets)')
    print(f'python {sys.version.split()[0]}; exact arithmetic: fractions.Fraction and int only')
    try:
        import sympy  # noqa: F401
        print('sympy present (not used by any step-1 control)')
    except ImportError:
        print('sympy absent: no step-1 control depends on it (K-LEM is step 6; I-37 applies there)')
    if MUTANT:
        print(f'MUTANT RUN {MUTANT}: phase A only')

    C = build_classes()
    order = ['R1a', 'R1b', 'R2a1', 'R2b1', 'R2a2', 'R2b2', 'KSWAP', 'CLC4']

    # I-55: the equivalence domain, declared before section 6.10
    dom = ('equivalence domain (I-55, A-2): fixed finite carrier and finite horizon; carriers = the core cells plus the '
           'declared ancillas of the classes ' + ', '.join(order) + '; protocol depth T <= 3 for access, T = 4 for C1-C4, '
           'transformations from sequences of length <= 2 (adaptive depth 2 where the alphabet has <= 4 ops)')
    print('\n' + dom)
    print('I-55 digest ' + sha(dom))
    check('I-55', True, 'the equivalence domain is declared with digest before section 6.10 runs')

    # I-52: class inputs with digests, before any class computation
    print('\n=== I-52: class inputs (declared), digests ===')
    for n in order:
        s = C[n]
        txt = s.inputs_text()
        DIGESTS[n] = sha(txt)
        print(f'--- {n}\n{txt}\nI-52 digest {DIGESTS[n]}')
    # the declared coupling text must agree with the truth tables of the actual step functions
    mismatch = []
    for n in order:
        s = C[n]
        tt = truth_table_text(s)
        for cname, rows in tt.items():
            text = next(t for c, _, _, t in s.couplings if c == cname)
            destructive_declared = 'fresh' in text
            # a clean read leaves the hidden cell unchanged; a destructive read xors the fresh bit into it
            hid_changed = any(k[len(s.vis):] != k2[len(s.vis):] for k, fr, k2 in rows)
            if destructive_declared != hid_changed:
                mismatch.append((n, cname))
    check('I-52', not mismatch, f'declared coupling steps agree with the truth tables of the step functions '
                                f'(mismatches: {mismatch}); digests printed above')

    # K-9
    print('\n=== K-9: condition O ===')
    for n in order:
        ok = k9(C[n])
        print(f'  {n}: every permutation, coupling step (with its fresh bits) and phi bijective on the core: {ok}')
    pr6 = kpr6()
    O_LOG.append(('K-PR6', pr6['bij']))
    check('K-9', all(ok for _, ok in O_LOG), f'condition O holds for all {len(O_LOG)} realizations checked')

    # K-C1C4 controls
    print('\n=== K-C1C4: the checker on the controls of section 14 ===')
    cd = coin_die()
    mc = markov_chain()
    zc = zero_coupling()
    tl = tape_ledger()
    for nm, r in (('coin-die (book ch01 1.5)', cd), ('Markov chain (tape-driven, P(flip)=1/4)', mc),
                  ('zero coupling (phi flips h only)', zc), ('tape-and-ledger fair coin (Main.md:172)', tl)):
        print(f'  {nm}: C1 {r["C1"]} (witness {r["C1w"]}); C3 certificate {r["C3"]} (distinct conditional future laws '
              f'{r["C3count"]} <= |C_H| = {r["C3m"]}); C4 {r["C4"]} (witness {r["C4w"]})')
    check('K-C1C4', cd['C1'] and cd['C4'] and cd['C3'] and mc['C1'] and not mc['C4'] and not zc['C1']
          and tl['C1'] and tl['C3'] and not tl['C4'],
          'coin-die satisfies C1, C4; the Markov chain fails C4; zero coupling fails C1; tape-and-ledger satisfies '
          'C1, C3 and fails C4 (C2 by the structural reading: every step is a bijection)')

    # K-PR6 replay
    print('\n=== K-PR6 replay ===')
    print(f'  correlators {dict((k, fs(v)) for k, v in sorted(pr6["E"].items()))}; CHSH S = {fs(pr6["S"])}; '
          f'uniform marginals {pr6["uniform"]}; no operational signalling on (q; r) {pr6["nosig"]}')
    for ab, r in sorted(pr6['c14'].items()):
        print(f'  K-C1C4 on K-PR6 at (a,b)={ab}: C1 {r["C1"]}, C3 {r["C3"]} ({r["C3count"]} <= {r["C3m"]}), C4 {r["C4"]}')
    check('K-PR6', pr6['bij'] and pr6['S'] == 4 and pr6['nosig'] and pr6['uniform'],
          'K-PR6 replays: CHSH = 4, uniform marginals, no signalling on the wing records, all steps bijective')
    pr6_c1c4 = all(r['C1'] and r['C3'] and r['C4'] for r in pr6['c14'].values())
    print(f'  K-PR6 passes K-C1C4 (as a 5-step realization at each setting pair): {pr6_c1c4}; '
          f'{"an R1 witness candidate" if pr6_c1c4 else "not an R1 witness (fails C4 under its own 5-step dynamics: every next visible value is a function of the current visible record)"}')

    # K-C1C4 on the R1 witness candidates (the section 6.10 classes, K-SWAP, CL-C4)
    print('\n=== K-C1C4 on the R1 witness candidates ===')
    c14_class = {}
    for n in order:
        s = C[n]
        rops = None
        if len(s.ops) > 6:
            idp = next(op for op in s.ops if op[0] == 'perm' and all(a == b for a, b in s.perms[op[1]].items()))
            rops = [idp] + [op for op in s.ops if op[0] == 'cpl']
        ok, w = k_c1c4_class(s, T=4, restrict_ops=rops)
        c14_class[n] = ok
        if ok:
            x0, pn, seq, r = w
            print(f'  {n}: passes (x0 {x0}, prior {pn}, protocol {seq}); C1 witness {r["C1w"]}; C3 '
                  f'{r["C3count"]} <= {r["C3m"]}; C4 witness (t, history, history\') {r["C4w"][:3]}'
                  + (f'; op alphabet restricted to identity + coupling steps ({len(rops)} ops)' if rops else ''))
        else:
            print(f'  {n}: no protocol of length 4 over its op alphabet ({len(s.ops)} ops), uniform or biased prior, '
                  f'passes C1, C3 and C4 together -> not an R1 witness candidate (section 6.2 admits only classes that '
                  f'pass K-C1C4)')
    passing = [n for n in order if c14_class[n]]
    print(f'  R1 witness candidates among the classes (K-C1C4 passed, printout above): {passing}; '
          f'failing: {[n for n in order if not c14_class[n]]}')
    check('K-C1C4-classes', c14_class['KSWAP'] and c14_class['CLC4'],
          f'K-SWAP and CL-C4 pass K-C1C4 as section 6.5 requires (must-hold); section 6.10 classes passing: {passing}')

    # I-58: access classes
    print('\n=== I-58: access classes over composed protocols ===')
    ACC = {}
    for n in order:
        s = C[n]
        for x0 in s.x0s:
            a = access_report(s, x0, Tmax=3, zero_step_only=(MUTANT == 'KM-31' and n == 'KSWAP'))
            ACC[(n, x0)] = a
            print('  ' + a['text'])
    check('I-58', ACC[('KSWAP', (0,))]['full'],
          f'K-SWAP\'s access class prints full hidden access: {ACC[("KSWAP", (0,))]["kind"]} (dims '
          f'{ACC[("KSWAP", (0,))]["dims"]})')
    # composite access for the one-bit classes by the direct recursion on the composite core, and the tensor rule
    print('  composite access (two copies, shared ancilla s in the core, local ops only):')
    comp_acc = {}
    for n in ('R1a', 'R1b', 'KSWAP', 'CLC4'):
        s = C[n]
        comp = composite_sys(s)
        a = access_report(comp, tuple(s.x0s[0]) * 2, Tmax=2)
        comp_acc[n] = a
        single = ACC[(n, s.x0s[0])]['A'].dim
        print(f'    {n}: dim {a["dims"]} of {len(a["hid_keys"])} hidden configurations (h_A, h_B, s); tensor rule '
              f'dim_A * dim_B = {single * single}; agree {a["A"].dim == single * single}; s invisible: '
              f'{a["A"].dim == single * single and a["A"].dim * 2 == len(a["hid_keys"])}')
    check('K-TENSOR', all(comp_acc[n]['A'].dim == ACC[(n, C[n].x0s[0])]['A'].dim ** 2 for n in comp_acc),
          'composite access = tensor product of the local access classes on the one-bit composites (s invisible)')

    # K-OPSTATE
    print('\n=== K-OPSTATE (I-49) ===')
    ko = kopstate(C)
    print(f'  passive record laws equal at horizons 1..4: {ko["passive_equal"]}; intervention x ^= h then readout: '
          f'{ko["outs"]}; different operational states: {not ko["same_state"]}; C1 under the passive dynamics: '
          f'{ko["c1_passive"]} (fails, as fixed: a control for the state definition)')
    check('I-49', ko['passive_equal'] and ko['intervention_differs'] and not ko['same_state'] and not ko['c1_passive'],
          'identical passive records, different operational states (P0 != P1), C1 fails under the passive dynamics')

    # I-38 transformations on the single systems
    print('\n=== I-38: transformations well defined on classes, reversibles ===')
    TR = {}
    for n in order:
        s = C[n]
        a = ACC[(n, s.x0s[0])]
        depth = 2
        tr = transformations(s, a['A_full'], depth=depth, adaptive=True)
        TR[n] = tr
        nwd = sum(1 for t in tr if t['wd'] is True)
        nrev = sum(1 for t in tr if t['rev'])
        unchecked = sum(1 for t in tr if t['wd'] is None)
        ill = sum(1 for t in tr if t['Q'] is None)
        names_rev = [t['name'] for t in tr if t['rev']][:8]
        print(f'  {n}: {len(tr)} distinct induced maps (sequences <= {depth}{", adaptive depth 2" if len(s.ops) <= 4 else ""}); '
              f'well defined on classes {nwd}, not well defined {ill}, unchecked {unchecked}; reversible {nrev}; '
              f'e.g. {names_rev}')
    check('I-38', all(t['wd'] is True for n in order for t in TR[n]),
          'every listed transformation carries its class check and is well defined on equivalence classes')

    # I-54: the preparable-set rule and the pure set; the A-2 fixture
    print('\n=== I-54: preparable sets and pure sets (section 2.2 rule) ===')
    priors = D8()
    enum2 = S_onebit_enumerated(2, [F(1, 3), F(1, 7), F(1, 8)])
    formula2 = sorted({(k * p + (4 - k) * (1 - p)) / 4 for p in (F(1, 3), F(1, 7), F(1, 8)) for k in range(5)})
    check('K-PREPSET', S_onebit(0) == S_onebit_enumerated(0, priors) and S_onebit(1) == S_onebit_enumerated(1, priors)
          and enum2 == formula2,
          'the preparable-set formula agrees with explicit enumeration of every permutation at m = 0, 1 (all priors) '
          'and m = 2 (priors 1/3, 1/7, 1/8)')
    S_by_m = budgets_onebit()
    pure_by_m = {}
    wit_by_m = {}
    for m in range(4):
        W = weights(m)
        pr, wit = pure_set([(1 - q, q) for q in S_by_m[m]], W)
        okw, bad = verify_witnesses([(1 - q, q) for q in S_by_m[m]], W, wit)
        pure_by_m[m] = sorted(p[1] for p in pr)
        wit_by_m[m] = {s[1]: (w, s1[1], s2[1]) for s, (w, s1, s2) in wit.items()}
        print(f'  one hidden bit, budget m={m}: preparable P(h=1) set size {len(S_by_m[m])}, weights {len(W)}, pure '
              f'{[fs(p) for p in pure_by_m[m]]}; witnesses verified {okw}; closed under real convex combination: '
              f'{len(S_by_m[m]) == 0}')
    print(f'  one hidden bit, m=3 preparable set: {[fs(q) for q in S_by_m[3]]}')
    print(f'  m=3 digest {sha(",".join(fs(q) for q in S_by_m[3]))}')
    # the A-2 fixture: {delta_0, delta_1, (1/3, 2/3)} with weights {1/2}: three pure under the rule, two under hull
    fixture = [(F(1), F(0)), (F(0), F(1)), (F(1, 3), F(2, 3))]
    prf, witf = pure_set(fixture, [HALF], convex_mutant=(MUTANT == 'KM-32'))
    okf, _ = verify_witnesses(fixture, [HALF], witf)
    check('I-54', len(prf) == 3 and okf,
          f'A-2 fixture: pure states under the preparable-weight rule = {len(prf)} (expected 3; real convex '
          f'combination would give 2); witnesses verified {okf}')

    # K-IF on CL, CL-C4, K-SWAP, K-PR6 (single-system parts; composites in phase C)
    print('\n=== K-IF: the interface on the control classes (single-system parts) ===')
    for n in ('CLC4', 'KSWAP'):
        s = C[n]
        a = ACC[(n, s.x0s[0])]
        print(f'  {n}: states = preparable set under access {a["kind"]}: {len(S_by_m[3])} (m=3); pure '
              f'{[fs(p) for p in pure_by_m[3]]}; transformations {len(TR[n])}, reversible '
              f'{sum(1 for t in TR[n] if t["rev"])}; composites: phase C')
    S_cl = {m: sorted({F(k, 2 ** m) for k in range(2 ** m + 1)}) for m in range(4)}
    pr_cl, wit_cl = pure_set([(1 - q, q) for q in S_cl[3]], weights(3))
    print(f'  CL (uncoupled, fails C1): states = P(x=1) in {[fs(q) for q in S_cl[3]]} (m=3); pure '
          f'{[fs(p[1]) for p in pr_cl]}; transformations: the 2 permutations of x, both reversible; composites: phase C')
    print('  K-PR6: one declared preparation (lambda uniform) per setting pair; the mixture/pure structure of a '
          'single-preparation class is not defined by section 2.2 -> Parked (per K-IF); records and C1-C4 above')
    check('K-IF', all(t['wd'] is True for n in ('CLC4', 'KSWAP') for t in TR[n]) and len(pure_by_m[3]) >= 2
          and len(pr_cl) == 2, 'the interface is well defined on CL, CL-C4 and K-SWAP (states, pure, transformations)')

    # I-59 unit test and A-1 scans
    print('\n=== I-59 unit test, A-1 scope, static checks ===')
    ok59, why = i59_unit_test()
    check('I-59', ok59, f'a grid pass alone cannot print a purification verdict: {why}')
    static_checks()

    nf = sum(1 for _, ok in CHECKS if not ok)
    if MUTANT:
        failed = [c for c, ok in CHECKS if not ok]
        print(f'\nP8S1  {"FAILS" if nf else "HOLDS"} ({nf} checks failed: {failed})' if nf else '\nP8S1  HOLDS (mutant survived)')
        sys.exit(1 if nf else 0)

    # phase B: mutation controls
    print('\n=== Phase B: mutation controls (judged in the manner of tools/mutant_verdict.py) ===')
    mutants = [('KM-22', 'I-38', 'a transformation defined on preparations and not checked on equivalence classes'),
               ('KM-25', 'I-49', 'state equivalence computed from passive records only (K-OPSTATE P0 = P1)'),
               ('KM-30', 'I-52', 'R1b run with the clean coupling substituted, printed inputs unchanged'),
               ('KM-31', 'I-58', 'K-SWAP access from zero-step protocols only (A-2 D1)'),
               ('KM-32', 'I-54', 'the A-2 fixture pure set computed by real convex combination (A-2 D2)'),
               ('KM-34', 'I-59', 'a grid Pur-E pass printing without the convex-closure line')]
    all_caught = True
    for km, target, case in mutants:
        r = subprocess.run([sys.executable, '-I', '-B', os.path.abspath(__file__), '--mutant', km],
                           capture_output=True, text=True)
        verdict, why = classify_mutant(target, r.returncode, r.stdout + r.stderr)
        all_caught &= verdict == 'KILLED'
        print(f'  {km} (target {target}; case: {case}): {verdict}: {why}')
    check('KM-ALL', all_caught, 'every step-1 mutant is caught (the named check fails cleanly on the named case)')

    gate_ok = all(ok for _, ok in CHECKS)
    print('\nI-6 gate for section 6.10: controls I-1, I-55, I-52, K-9, K-C1C4, K-PR6, I-58, K-TENSOR, I-49, I-38, '
          'K-PREPSET, I-54, K-IF, I-59, static checks, mutants: ' + ('all green' if gate_ok else 'failed'))
    if not gate_ok:
        print('\nsection 6.10: VOID (a control failed; no verdict is printed)')
        print(f'\nP8S1  FAILS ({nf} checks failed)')
        sys.exit(1)

    phase_c(C, order, ACC, TR, S_by_m, pure_by_m, wit_by_m, S_cl, pr_cl, wit_cl, comp_acc)
    bad = a1_scope_scan()
    check('A1-SCOPE', not bad, f'no generated purification line names OI, QM or a general claim: offending {bad}')
    nf = sum(1 for _, ok in CHECKS if not ok)
    print(f'\nchecks: {len(CHECKS) - nf} PASS, {nf} FAIL')
    print(f'P8S1  {"HOLDS" if nf == 0 else "FAILS (" + str(nf) + " checks failed)"}')
    sys.exit(1 if nf else 0)


def composite_sys(s):
    """two copies of a one-bit class with the shared hidden ancilla s in the core; local ops only (product alphabet)"""
    vis = [(c + '_A', sz) for c, sz in s.vis] + [(c + '_B', sz) for c, sz in s.vis]
    hid = [(c + '_A', sz) for c, sz in s.hid] + [(c + '_B', sz) for c, sz in s.hid] + [('s', 2)]

    def split(d):
        dA = {c: d[c + '_A'] for c, _ in s.core}
        dB = {c: d[c + '_B'] for c, _ in s.core}
        return dA, dB

    def join(dA, dB, sval):
        d = {c + '_A': v for c, v in dA.items()}
        d.update({c + '_B': v for c, v in dB.items()})
        d['s'] = sval
        return d

    def phi(d):
        dA, dB = split(d)
        return join(s.phi(dA), s.phi(dB), d['s'])
    couplings = []
    for oa in s.ops:
        for ob in s.ops:
            ka, kb = s.nfresh(oa), s.nfresh(ob)

            def f(d, fresh, oa=oa, ob=ob, ka=ka):
                dA, dB = split(d)
                return join(s.apply_op(oa, dA, fresh[:ka]), s.apply_op(ob, dB, fresh[ka:]), d['s'])
            couplings.append((f'{s.op_name(oa)} x {s.op_name(ob)}', f, ka + kb, 'local x local'))
    comp = Sys(s.name + 'xx', vis, hid, phi, 'phi_A x phi_B', couplings, [tuple(s.x0s[0]) * 2], [], [], '', '',
               perm_alphabet=[])
    return comp


def classify_mutant(target, rc, text):
    lines = [l for l in text.splitlines() if l.strip()]
    if rc == 0:
        return 'SURVIVED', 'the probe passed on the mutant'
    if rc < 0 or rc >= 124:
        return 'INFRA', f'did not finish (status {rc})'
    if any(l.startswith('Traceback (most recent call last):') or re.match(r'^\s*File "[^"]*", line \d+', l)
           for l in lines):
        return 'CRASHED', 'a Python traceback or stack frame was printed'
    last = lines[-1] if lines else ''
    if rc != 1 or not re.match(r'^P8S1  FAILS\b', last):
        return 'CRASHED', f'exited {rc} without the failing verdict line; last line: {last[:120]}'
    hits = [l for l in lines if l.startswith('FAIL  ') and l[len('FAIL  '):].startswith(target + ':')]
    if not hits:
        return 'NOT-TARGETED', f'failed, but not on {target}'
    return 'KILLED', hits[0][:140]


def phase_c(C, order, ACC, TR, S_by_m, pure_by_m, wit_by_m, S_cl, pr_cl, wit_cl, comp_acc):
    print('\n=== Phase C: section 6.10 outputs (every line generated from the measurements; A-1 scoping) ===')
    W3 = weights(3)
    # composites of the one-hidden-bit classes (identical preparable sets, so one enumeration)
    print('\n--- composites of the one-hidden-bit classes under the A-2 reading ---')
    pairs, pi, SJ = composite_onebit(S_by_m[3], W3)
    pure_single = pure_by_m[3]
    pure_comp, nwit, fb = composite_onebit_pure(pairs, pi, SJ, S_by_m[3], pure_single, wit_by_m[3], W3)
    print(f'  A-side conditional pairs (alpha_0, alpha_1) from one prior: {len(pairs)}; composite preparable states '
          f'{len(SJ)}; digest {sha(",".join(str(x) for x in sorted(SJ)))}')
    print(f'  pure composite states {len(pure_comp)}: {[fs(packed_to_dist(s)) for s in pure_comp]} '
          f'(cells (hA,hB) = 00, 01, 10, 11); mixedness witnesses: {nwit}; exhaustive fallback decided mixed: {fb}')
    point_masses = [tuple(F(1) if i == j else F(0) for i in range(4)) for j in range(4)]
    comp_pm = sorted(packed_to_dist(s) for s in pure_comp) == sorted(point_masses)
    # the composite lemma K-CL: predicted pure set = {delta x delta'} when the single pure set = point masses
    check('K-CL', comp_pm and sorted(pure_single) == [F(0), F(1)],
          'composite lemma instance: with the single pure set = {delta_0, delta_1}, the exhaustive composite pure set '
          'equals the 4 point masses (validates the lemma used for the R2 composites)')
    # SHARED-ALT sensitivity row (decides nothing)
    pA, pB = F(1, 7), F(1, 5)
    u0 = (8 * pB + 0 * (1 - pB)) / 8
    u1 = (4 * pB + 4 * (1 - pB)) / 8
    beta_alt = pA * u0 + (1 - pA) * u1
    # B-marginals under the A-2 reading: (beta_0 + beta_1)/2 with both from one prior's grid (one realization datum)
    b_marg_ro = {(x + y) / 2 for p in D8() for x in {(k * p + (8 - k) * (1 - p)) / 8 for k in range(9)}
                 for y in {(k * p + (8 - k) * (1 - p)) / 8 for k in range(9)}}
    print(f'  SHARED-ALT (sensitivity, A-2): under the alternative reading where copy A\'s preparation writes s, the '
          f'B-marginal {fs(beta_alt)} (p_A={fs(pA)}, p_B={fs(pB)}, c_1=(8,0 | 4,4)) is reachable; it is a B-marginal '
          f'of the A-2 reading: {beta_alt in b_marg_ro}; the two readings give different preparable sets')
    across_pure = pure_single
    results = {}
    for n in ('R1a', 'R1b', 'KSWAP', 'CLC4'):
        s = C[n]
        acc = ACC[(n, s.x0s[0])]
        print(f'\n--- {n} (I-52 digest {DIGESTS[n]}) ---')
        print('  ' + acc['text'])
        print(f'  states (equivalence classes of preparations under every protocol): {len(S_by_m[3])} = the preparable '
              f'P(h=1) set at m=3 (access {acc["kind"]}, so the class is the h-marginal); digest '
              f'{sha(",".join(fs(q) for q in S_by_m[3]))}')
        print(f'  pure states (preparable-weight rule, m=3): {[fs(p) for p in pure_by_m[3]]}; Q-PREP data: the '
              f'preparable mixtures are the grid {{(k p + (8-k)(1-p))/8 : p in D8, k = 0..8}}, not closed under real '
              f'convex combination')
        tr = TR[n]
        print(f'  transformations: {len(tr)} distinct induced maps, all well defined on classes; reversible '
              f'{sum(1 for t in tr if t["rev"])}: {[t["name"] for t in tr if t["rev"]]}')
        print(f'  composites: {len(SJ)} preparable joint states on (h_A, h_B), shared ancilla s invisible (composite '
              f'access dim {comp_acc[n]["A"].dim} of {len(comp_acc[n]["hid_keys"])}); joint accessible class = local ops '
              f'({len(s.ops) ** 2} pairs); beyond local compositions and shared randomness: none declared')
        lemmaA = (f'  Lemma A instance (A1 grid reading: preparable set is the grid; A2 access {acc["kind"]}; A3 '
                  f'composites of product form with local operations, by construction): the operational theory of {n} '
                  f'is classical probability on its preparable priors; pure = extreme preparable (measured: '
                  f'{[fs(p) for p in pure_by_m[3]]}); a pure composite state has point-mass marginals (measured: '
                  f'{comp_pm})')
        print(lemmaA)
        lines, cpm, allpm, puru_ok = phase_c_onebit(n, s, acc, tr, (pairs, pi, SJ, pure_comp, nwit, fb), S_by_m,
                                                    pure_by_m, wit_by_m, across_pure)
        results[n] = dict(n_states=len(S_by_m[3]), pure=[fs(p) for p in pure_by_m[3]], n_pure_e=len(pure_by_m[3]),
                          puru=puru_ok, full=acc['full'])
    # CL composite (uncoupled classical): same enumeration with S_cl
    print('\n--- CL (uncoupled classical control) composites ---')
    pairs_cl = sorted({(a, b) for a in S_cl[3] for b in S_cl[3]})
    SJ_cl = set()
    pi_cl = [(int(a * L1), int(b * L1)) for a, b in pairs_cl]
    for a0, a1 in pi_cl:
        for b0, b1 in pi_cl:
            a0c, a1c, b0c, b1c = L1 - a0, L1 - a1, L1 - b0, L1 - b1
            SJ_cl.add((a0c * b0c + a1c * b1c) + ((a0c * b0 + a1c * b1) << SH) + ((a0 * b0c + a1 * b1c) << (2 * SH))
                      + ((a0 * b0 + a1 * b1) << (3 * SH)))
    wit_cl1 = {s[1]: (w, s1[1], s2[1]) for s, (w, s1, s2) in wit_cl.items()}
    pure_cl_comp, nwit_cl, fb_cl = composite_onebit_pure(pairs_cl, pi_cl, SJ_cl, S_cl[3], [p[1] for p in pr_cl],
                                                         wit_cl1, W3)
    print(f'  CL composite preparable states {len(SJ_cl)}; pure {len(pure_cl_comp)}: '
          f'{[fs(packed_to_dist(s)) for s in pure_cl_comp]}; witnesses {nwit_cl}; fallback {fb_cl}')
    cl_pure_d = [packed_to_dist(s) for s in pure_cl_comp]
    cl_pm = sorted(cl_pure_d) == sorted(point_masses)
    # CL as a class: one visible bit, no hidden cell; its transformations are the permutations of x
    CL = Sys('CL', [('x', BIT)], [], phi_id, 'identity', [], [(0,)], VANC, HANC, 'none (no hidden cell)',
             'two copies with the shared ancilla s (A-2 reading)')
    accCL = access_report(CL, (0,), Tmax=2)
    trCL = transformations(CL, accCL['A_full'], depth=2, adaptive=True)
    revCL = [t for t in trCL if t['rev']]

    def cl_vec(x):
        return tuple(F(1) if k == (x,) else F(0) for k in CL.keys)
    cl_conn = all(any(state_coords(accCL['A_full'], tuple(sum((t['M'][i][j] * cl_vec(a)[j] for j in range(2)), F(0))
                                                              for i in range(2))) == state_coords(accCL['A_full'],
                                                                                                  cl_vec(b))
                      for t in revCL) for a in (0, 1) for b in (0, 1) if a != b)
    cl_with_pur = sorted({d[2] + d[3] for d in cl_pure_d})   # P(x_A = 1) marginals of the pure composite states
    render_pur('CL', [('budget m=3, weights k/8',
                       f'Pur-E: holds for {len(cl_with_pur)} of {len(S_cl[3])} preparable states (P(x=1) in '
                       f'{[fs(q) for q in cl_with_pur]}; pure composite states = {len(pure_cl_comp)}, point masses: '
                       f'{cl_pm}), fails for {len(S_cl[3]) - len(cl_with_pur)}. Pur-U: '
                       f'{"holds" if cl_conn else "fails"} on the states with purifications ({len(revCL)} reversible '
                       f'transformations of B alone, permutations of x). A calibration: CL fails C1')],
               f'closure = full simplex (every point mass preparable: {cl_pm}); extreme = the point masses; Pur-E on '
               f'the closure holds for the 2 extreme states and fails for every non-extreme state (Lemma K instance: '
               f'(i) holds, (ii) holds, (iii) holds with {len(pure_cl_comp)} pure composite states)')

    # R2 classes
    print('\n--- R2 classes: preparable set on (h1, h2) ---')
    S2, hints2, reps = S_R2(3)
    pr2, wit2 = pure_set(S2, W3, hints=hints2)
    okw2, bad2 = verify_witnesses(S2, W3, wit2)
    n_hint = sum(1 for s in wit2 if s in hints2)
    print(f'  priors on (h1,h2) with denominator <= 8: {len(priors_R2())} ({len(reps)} up to relabeling); preparable '
          f'set at m=3: {len(S2)} states; digest {sha(",".join(fs(s) for s in S2))}')
    print(f'  pure (preparable-weight rule, weights k/8): {len(pr2)}: {[fs(p) for p in pr2]}; witnesses verified '
          f'{okw2}; states decided by constructive hints {n_hint}, by exhaustive search {len(wit2) - n_hint}')
    point4 = [tuple(F(1) if i == j else F(0) for i in range(4)) for j in range(4)]
    check('I-54-R2', okw2 and sorted(pr2) == sorted(point4),
          'R2 preparable set: every witness verified exactly; the pure set is the 4 point masses')
    for m in (0, 1, 2):
        Sm, hm, _ = S_R2(m)
        prm, witm = pure_set(Sm, weights(m), hints=hm) if m > 0 else (Sm, {})
        print(f'  budget m={m}: preparable {len(Sm)}, pure {len(prm)}' + (' (no mixing operation at m=0)' if m == 0 else ''))
    for n in ('R2a1', 'R2b1', 'R2a2', 'R2b2'):
        s = C[n]
        acc = ACC[(n, s.x0s[0])]
        tr = TR[n]
        print(f'\n--- {n} (I-52 digest {DIGESTS[n]}) ---')
        print('  ' + acc['text'])
        print(f'  states: {len(S2)} = the preparable set on (h1, h2) at m=3 (access {acc["kind"]}); pure '
              f'{[fs(p) for p in pr2]}')
        print(f'  transformations: {len(tr)} distinct induced maps, all well defined; reversible '
              f'{sum(1 for t in tr if t["rev"])}: {[t["name"] for t in tr if t["rev"]][:6]}{"..." if sum(1 for t in tr if t["rev"]) > 6 else ""}')
        print(f'  composites: two copies with shared s (A-2 reading): preparable joint states are 1/2(alpha_0 x beta_0 '
              f'+ alpha_1 x beta_1), alpha_s, beta_s in the per-prior grids; not enumerated (the set exceeds the local '
              f'bound of A.40: >= {len(S2)}^2 product states); pure set by the composite lemma (K-CL, validated on the '
              f'one-bit composites): the {len(pr2) ** 2} products of point masses; composite access by the tensor rule '
              f'(local ops, s untouched)')
        # Pur-U on B alone: reversible maps of B sending delta_(x0, h) to delta_(x0, h') for every pair
        revs = [t for t in tr if t['rev']]
        A_full = acc['A_full']
        hkeys = sorted({s.hid_of(k) for k in s.keys})

        def vec(hk):
            return tuple(F(1) if k == tuple(s.x0s[0]) + hk else F(0) for k in s.keys)
        conn = True
        for h1 in hkeys:
            for h2 in hkeys:
                if h1 == h2:
                    continue
                tgt = state_coords(A_full, vec(h2))
                src = vec(h1)
                ok = any(state_coords(A_full, tuple(sum((t['M'][i][j] * src[j] for j in range(len(src))), F(0))
                                                    for i in range(len(src)))) == tgt for t in revs)
                conn &= ok
        puru = ('holds for every point mass (each pair of purifications connected by a reversible transformation of B)'
                if conn else f'fails: no reversible transformation of B among {len(revs)} maps one point mass of B to another '
                             f'(the hidden cells are never written by any op or phi)')
        grid = [(f'budget m=3 (weights k/8), composite pure states = {len(pr2) ** 2} products of point masses (K-CL)',
                 f'Pur-E: holds for {len(pr2)} of {len(S2)} preparable states (the point masses; purifications: the '
                 f'{len(pr2)} products with a point mass of B); fails for {len(S2) - len(pr2)} states. Pur-U: {puru}'),
                ('across the declared theory (the R2 classes share the preparable set; weights k/8)',
                 f'preparable {len(S2)}, pure {len(pr2)}; Pur-E and Pur-U as the budget line')]
        closure = (f'convex closure of the preparable set = the full simplex on (h1, h2) (every point mass preparable); '
                   f'closure of the composite = full simplex on 16 points, extreme = the 16 products of point masses '
                   f'with point-mass marginals; transformations extend affinely ({len(tr)} pushforward maps); Pur-E on '
                   f'the closure: holds for the 4 extreme states, fails for every non-extreme state. Lemma K: (i) holds '
                   f'(point masses distinguished: access {acc["kind"]}; every real mixture preparable in the closure), '
                   f'(ii) holds (one additional system type), (iii) holds (16 pure states): Lemma K\'s instance.')
        render_pur(n, grid, closure)
        results[n] = dict(n_states=len(S2), pure=[fs(p) for p in pr2], n_pure_e=len(pr2), puru=conn, full=acc['full'])
        print(f'  Lemma A instance: (A1) grid reading, (A2) access {acc["kind"]}, (A3) local product composites; the '
              f'operational theory of {n} is classical probability on its preparable priors (measured pure set: '
              f'{[fs(p) for p in pr2]})')
    print('\n--- section 6.10 summary (generated from the measurements above) ---')
    for n in order:
        acc = ACC[(n, C[n].x0s[0])]
        r = results[n]
        pur_line(n, 'summary of the two reading lines above',
                 f'access {acc["kind"]}; states {r["n_states"]}; pure {r["pure"]}; existence holds for {r["n_pure_e"]} '
                 f'states on the preparable set and for the extreme states on the closure; uniqueness on the pure '
                 f'states: {"holds" if r["puru"] else "fails"}; nothing is decided beyond the class {n}')
    # the live content under option (B), generated: access of the destructive classes and reversibility of the read
    for n in ('R1b', 'R2b1', 'R2b2'):
        s = C[n]
        acc = ACC[(n, s.x0s[0])]
        dread = next(t for t in TR[n] if t['name'] == s.couplings[0][0])
        twin = {'R1b': 'R1a', 'R2b1': 'R2a1', 'R2b2': 'R2a2'}[n]
        print(f'  live content under option (B), {n}: access {acc["kind"]} (full: {acc["full"]}); its state set '
              f'{"coincides with" if results[n]["n_states"] == results[twin]["n_states"] else "differs from"} {twin}\'s; '
              f'the destructive read is reversible on states: {dread["rev"]}')


if __name__ == '__main__':
    if len(sys.argv) >= 3 and sys.argv[1] == '--mutant':
        MUTANT = sys.argv[2]
    main()
