#!/usr/bin/env python3
"""marc_check.py -- ARP-1-MARC: the exact F_2 span check, frozen with the preregistration beside it.

  python3 -I -B marc_check.py                   the decisive computation. Writes measurements.json to stdout as
                                                canonical JSON; exit 0 when complete and every control is green at
                                                both sizes, 3 when complete and some control is red.
  python3 -I -B marc_check.py --self-test       hand cases, C-SUPP-F's law, M-PLANT at t = 0, C-STEP, C-HOR and the
                                                transport, omega-drop and v-offset mutations. Enumerates no case of
                                                variant D and evaluates C9 at t = 0 only.

Outside the default mode a guard refuses the enumeration and any case evaluation of variant D, and of C9 beyond t = 0
(C9's span is D's span: same dynamics and registrations, only the window differs). Only decisive() lifts it.
  python3 -I -B marc_check.py --fixture-output  a hand-written synthetic record in the measurement schema; computes
                                                nothing.

Model (preregistration, *The question* and *The exact method*). Ring Z_L, L = 3 + |H|, |H| in {4, 6}; window
V = {0, 1, 2}; horizon T = 4. A state is x in F_2^{2L}, coordinate u_i at bit i and v_i at bit L + i. The rule N_1:
u_i' = u_{i-1} + u_{i+1} + v_i, v_i' = u_i. A linear functional is a row vector, held as an int over the same bits.

Two independent code paths, sharing only the case list:
  the span method   (sp_*)  transports the known and registered functionals by the explicit inverse step and
                            decides exposure on a fully reduced echelon basis of S_t intersected with W_V(t);
  the cross-check   (xb_*)  simulates the dynamics on bit-sliced integers over every assignment of the unknown
                            slots, groups assignments by record branch and evaluates Q* coordinate by coordinate.

Exact arithmetic only: integers and bit operations over F_2; fractions.Fraction for C-SUPP-F's law. No floating
point, no measure in any determination statement. Imports fractions, itertools, json and sys; reads no file.
"""
from fractions import Fraction
import itertools
import json
import sys

SCHEMA = 'arp1-marc-measurements'
VERSION = 1
T = 4
WINDOW = (0, 1, 2)
SIZES = (4, 6)
SLOT_NAMES = 'uv'
PATTERNS = tuple(''.join(w) for w in itertools.product('uv', repeat=3))
ACTIONS = (None,) + tuple((c, s) for c in WINDOW for s in (0, 1))
CONTROLS = ('CC-ISO', 'C-NV', 'C-SUPP-X', 'C-SUPP-F', 'C9', 'C-DEISO', 'C-XB', 'M-PLANT', 'C-STEP', 'C-HOR')


def make_schedules():
    """Every schedule: at each t in 0..T nothing or one (site, slot) of a window cell, each cell at most once.
    itertools.product over ACTIONS gives the frozen order: tuples of per-time actions, compared from t = 0,
    with nothing < (0,u) < (0,v) < (1,u) < ... ."""
    out = []
    for tup in itertools.product(ACTIONS, repeat=T + 1):
        cells = [a[0] for a in tup if a is not None]
        if len(cells) == len(set(cells)):
            out.append(tup)
    return tuple(out)


SCHEDULES = make_schedules()
EMPTY = (None,) * (T + 1)

# Set except in the default mode (decisive() clears it): while set, the enumeration, measure_size, every case
# evaluation of variant D and every evaluation of C9 beyond t = 0 refuse before computing anything.
_GUARD = [True]


def _refuse_d(variant, tmax):
    if _GUARD[0] and (variant == 'D' or (variant == 'C9' and tmax > 0)):
        raise RuntimeError('variant %s up to t = %d refused outside the default mode' % (variant, tmax))


# =====================================================================================================================
# SHA-256 (pure Python; hashlib is outside this file's import allowlist). Checked against FIPS 180-2 vectors in the
# self-test.
# =====================================================================================================================
_K = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
      0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
      0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
      0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
      0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
      0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
      0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
      0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]
_H0 = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
_M32 = 0xffffffff


def _rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & _M32


def sha256_hex(data):
    h = list(_H0)
    ml = len(data) * 8
    data = bytes(data) + b'\x80' + b'\x00' * ((55 - len(data)) % 64) + ml.to_bytes(8, 'big')
    for off in range(0, len(data), 64):
        w = [int.from_bytes(data[off + 4 * i:off + 4 * i + 4], 'big') for i in range(16)]
        for i in range(16, 64):
            s0 = _rotr(w[i - 15], 7) ^ _rotr(w[i - 15], 18) ^ (w[i - 15] >> 3)
            s1 = _rotr(w[i - 2], 17) ^ _rotr(w[i - 2], 19) ^ (w[i - 2] >> 10)
            w.append((w[i - 16] + s0 + w[i - 7] + s1) & _M32)
        a, b, c, d, e, f, g, hh = h
        for i in range(64):
            t1 = (hh + (_rotr(e, 6) ^ _rotr(e, 11) ^ _rotr(e, 25)) + ((e & f) ^ (~e & g)) + _K[i] + w[i]) & _M32
            t2 = ((_rotr(a, 2) ^ _rotr(a, 13) ^ _rotr(a, 22)) + ((a & b) ^ (a & c) ^ (b & c))) & _M32
            hh, g, f, e, d, c, b, a = g, f, e, (d + t1) & _M32, c, b, a, (t1 + t2) & _M32
        h = [(x + y) & _M32 for x, y in zip(h, [a, b, c, d, e, f, g, hh])]
    return ''.join('%08x' % x for x in h)


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(',', ':')) + '\n'


def sched_json(sched):
    return [None if a is None else [a[0], SLOT_NAMES[a[1]]] for a in sched]


def known_slot(pattern, c):
    return 0 if pattern[c] == 'u' else 1


# =====================================================================================================================
# The span method (sp_*)
# =====================================================================================================================
def sp_unit(L, site, slot):
    return 1 << (site + L * slot)


def sp_step(L, archived, mut=frozenset()):
    """Rows of the forward step x_{t+1} = M x_t: row r is the set of state coordinates coordinate r reads.
    archived = the cells held in variant I's archive at this tick (empty in D and C9): such a cell takes the free
    tick (u, v) -> (v, u), and its neighbours' sums omit it."""
    rows = [0] * (2 * L)
    for i in range(L):
        if i in archived:
            rows[i] = 1 << (L + i)
            rows[L + i] = 1 << i
            continue
        r = 1 << (L + i)
        if 'center' in mut:
            r ^= 1 << i
        for j in ((i - 1) % L, (i + 1) % L):
            if j not in archived:
                r ^= 1 << j
        rows[i] = r
        rows[L + i] = 1 << i
    return rows


def sp_inverse(L, archived, mut=frozenset()):
    """Rows of the explicit second-order inverse (a, b) -> (b, a + f(b)), a = u', b = v', written from the rule and
    not by inverting sp_step (C-STEP checks the two against each other): u_i = v'_i; v_i = u'_i + sum of v'_j over
    the coupled neighbours j; for an archived cell, v_a = u'_a."""
    rows = [0] * (2 * L)
    for i in range(L):
        rows[i] = 1 << (L + i)
        if i in archived:
            rows[L + i] = 1 << i
            continue
        r = 1 << (((i + 1) % L) if 'voff' in mut else i)
        for j in ((i - 1) % L, (i + 1) % L):
            if j not in archived:
                r ^= 1 << (L + j)
        rows[L + i] = r
    return rows


class SpTransport:
    """g -> g . A for a fixed matrix A given by its rows, via 6-bit chunk tables."""
    __slots__ = ('tabs',)

    def __init__(self, rows):
        self.tabs = []
        for base in range(0, len(rows), 6):
            tab = [0] * 64
            for m in range(1, 64):
                low = m & -m
                b = low.bit_length() - 1
                tab[m] = tab[m ^ low] ^ (rows[base + b] if base + b < len(rows) else 0)
            self.tabs.append(tab)

    def __call__(self, g):
        out = 0
        i = 0
        while g:
            out ^= self.tabs[i][g & 63]
            g >>= 6
            i += 1
        return out


_SP_TRANSPORT = {}


def sp_transport_for(L, archived, mut):
    key = (L, archived, 'fwd' in mut, 'voff' in mut)
    if key not in _SP_TRANSPORT:
        rows = sp_step(L, archived) if 'fwd' in mut else sp_inverse(L, archived, mut)
        _SP_TRANSPORT[key] = SpTransport(rows)
    return _SP_TRANSPORT[key]


class SpKeying:
    """Re-encodes a functional so that the given cells come first: cell k (ascending site order) has u at bit 2k and
    v at bit 2k + 1 (the witness encoding); every other coordinate lies above bit 2n. The echelon pivot is the
    highest set bit, so the coordinates outside the cells are eliminated first."""
    __slots__ = ('n', 'tabs', 'cells', 'L')

    def __init__(self, L, cells):
        self.L, self.cells, self.n = L, tuple(cells), len(cells)
        order = []
        for c in cells:
            order += [c, L + c]
        order += [j for j in range(2 * L) if j not in order]
        pos = {j: k for k, j in enumerate(order)}
        self.tabs = []
        for base in range(0, 2 * L, 6):
            tab = [0] * 64
            for m in range(64):
                key = 0
                for b in range(6):
                    if m >> b & 1 and base + b < 2 * L:
                        key |= 1 << pos[base + b]
                tab[m] = key
            self.tabs.append(tab)

    def key(self, g):
        out = 0
        i = 0
        while g:
            out |= self.tabs[i][g & 63]
            g >>= 6
            i += 1
        return out


_SP_KEYING = {}


def sp_keying(L, cells):
    k = (L, tuple(cells))
    if k not in _SP_KEYING:
        _SP_KEYING[k] = SpKeying(L, cells)
    return _SP_KEYING[k]


def sp_rref(vecs):
    """Fully reduced row echelon basis over F_2, pivot = highest set bit."""
    rows = []
    for x in vecs:
        for r in rows:
            if x >> (r.bit_length() - 1) & 1:
                x ^= r
        if x:
            p = x.bit_length() - 1
            rows = [r ^ x if r >> p & 1 else r for r in rows]
            rows.append(x)
    return rows


def sp_even(n):
    return sum(1 << (2 * k) for k in range(n))


def sp_q(k, even):
    return (k & (k >> 1) & even).bit_count() & 1


def sp_omega(a, b, even):
    return (((a & (b >> 1)) ^ ((a >> 1) & b)) & even).bit_count() & 1


def sp_exposes(basis, even, mut=frozenset()):
    """Q* fails to vanish on span(basis) iff Q* = 1 on a basis vector or omega = 1 on a pair, since
    Q*(f + f') = Q*(f) + Q*(f') + omega(f, f'). The 'wdrop' mutation drops the pair term."""
    for i, a in enumerate(basis):
        if sp_q(a, even):
            return True
        if 'wdrop' not in mut:
            for b in basis[i + 1:]:
                if sp_omega(a, b, even):
                    return True
    return False


def sp_isotropic(basis, even):
    return not any(sp_omega(a, b, even) for i, a in enumerate(basis) for b in basis[i + 1:])


def sp_members(basis):
    """Bitmask over window codes: bit c set iff code c lies in span(basis)."""
    elems = [0]
    for b in basis:
        elems += [e ^ b for e in elems]
    m = 0
    for e in elems:
        m |= 1 << e
    return m


def sp_qmask(n, value):
    """Bitmask over window codes c < 4^n with Q*(c) = value (used by C-NV and the witness only)."""
    even = sp_even(n)
    m = 0
    for c in range(1 << (2 * n)):
        if sp_q(c, even) == value:
            m |= 1 << c
    return m


SP_QZERO = [sp_qmask(n, 0) for n in range(4)]
SP_QONE = [sp_qmask(n, 1) for n in range(4)]


def sp_case(L, variant, pattern, sched, extra=(), tmax=T, mut=frozenset(), active=False):
    """One case on the span method. variant D: the registered cell stays on the ring (step always the ring step) and
    leaves V; I: the registered cell is archived (free ticks, decoupled site) and leaves V; C9: the registered cell
    stays on the ring and stays in V. Order at each t: registration, evaluation, tick (t < tmax).
    Returns per-time records and the per-tick archived sets the transport used."""
    _refuse_d(variant, tmax)
    leaves = variant in ('D', 'I')
    archives = variant == 'I'
    cur = list(WINDOW)
    reg = []
    I = [sp_unit(L, c, known_slot(pattern, c)) for c in WINDOW] + list(extra)
    R = []
    injections = 0
    recs = []
    ticks = []
    for t in range(tmax + 1):
        act = sched[t]
        if act is not None:
            c, s = act
            R.append(sp_unit(L, c, s))
            reg.append(c)
            if leaves:
                cur.remove(c)
        n = len(cur)
        even = sp_even(n)
        lim = 1 << (2 * n)
        kw = sp_keying(L, cur)
        S = sp_rref([kw.key(g) for g in I + R])
        B = sorted(x for x in S if x < lim)
        rec = {'expose': sp_exposes(B, even, mut), 'members': sp_members(B), 'n': n, 'window': tuple(cur),
               'registered_now': act is not None}
        BI = sorted(x for x in sp_rref([kw.key(g) for g in I]) if x < lim)
        rec['nv'] = bool(rec['members'] & ~sp_members(BI) & SP_QZERO[n])
        vmask = 0
        for c in cur:
            vmask |= (1 << c) | (1 << (L + c))
        rec['coupling'] = any(rho & vmask for rho in R)
        rec['rank_I'] = len(sp_rref(I[:3]))
        rec['records_ok'] = len(R) == len(reg) and all(R)
        if active:
            on = [c for c in range(L) if c not in reg]
            ka = sp_keying(L, on)
            evena = sp_even(len(on))
            BA = sorted(x for x in sp_rref([ka.key(g) for g in I + R]) if x < (1 << (2 * len(on))))
            rec['active_expose'] = sp_exposes(BA, evena, mut)
            rec['active_noniso'] = not sp_isotropic(BA, evena)
        recs.append(rec)
        if t < tmax:
            arch = frozenset(reg) if archives else frozenset()
            tr = sp_transport_for(L, arch, mut)
            before = len(I)
            I = [tr(g) for g in I]
            R = [tr(g) for g in R]
            if len(I) != before:
                injections += 1
            ticks.append((arch, frozenset(reg)))
    return recs, ticks, injections


def sp_in_span(L, vecs, f):
    """Membership of a raw functional in span(vecs) on the span path."""
    basis = sp_rref(vecs)
    for r in basis:
        if f >> (r.bit_length() - 1) & 1:
            f ^= r
    return f == 0


def sp_s_at(L, variant, pattern, sched, t_eval, extra=()):
    """The raw generators of S_t (I_t and R_t, transported) at one time, for C-SUPP-F's span half."""
    _refuse_d(variant, t_eval)
    archives = variant == 'I'
    reg = []
    I = [sp_unit(L, c, known_slot(pattern, c)) for c in WINDOW] + list(extra)
    R = []
    for t in range(t_eval + 1):
        act = sched[t]
        if act is not None:
            R.append(sp_unit(L, act[0], act[1]))
            reg.append(act[0])
        if t < t_eval:
            tr = sp_transport_for(L, frozenset(reg) if archives else frozenset(), frozenset())
            I = [tr(g) for g in I]
            R = [tr(g) for g in R]
    return I + R


# =====================================================================================================================
# C-XB: direct simulation (xb_*), independent of the span method; it shares only the case list
# =====================================================================================================================
def xb_varmasks(nun):
    """Bit-sliced variables: bit a of mask k is bit k of the assignment index a."""
    width = 1 << nun
    out = []
    for k in range(nun):
        blk = 1 << k
        p = ((1 << blk) - 1) << blk
        span = 2 * blk
        while span < width:
            p |= p << span
            span *= 2
        out.append(p)
    return out


_XB_VAR = {}


def xb_q(code, ncells):
    """Q* of a window functional, coordinate by coordinate: the sum over window cells of (u coefficient)(v coefficient)."""
    q = 0
    for k in range(ncells):
        q ^= (code >> (2 * k) & 1) & (code >> (2 * k + 1) & 1)
    return q


_XB_QTAB = [[xb_q(code, n) for code in range(1 << (2 * n))] for n in range(4)]


def xb_case(L, variant, pattern, sched, known_value=0, tmax=T):
    """Simulate the case over every assignment of the unknown slots at once. Returns, per time, the list of
    determined-functional bitmasks (one per non-empty record branch, over window codes) and the exposure flag."""
    _refuse_d(variant, tmax)
    leaves = variant in ('D', 'I')
    archives = variant == 'I'
    nun = 2 * L - 3
    if nun not in _XB_VAR:
        _XB_VAR[nun] = xb_varmasks(nun)
    var = _XB_VAR[nun]
    full = (1 << (1 << nun)) - 1
    u = [0] * L
    v = [0] * L
    k = 0
    for site in range(L):
        for slot in (0, 1):
            if site in WINDOW and slot == (0 if pattern[site] == 'u' else 1):
                val = full if known_value else 0
            else:
                val = var[k]
                k += 1
            if slot == 0:
                u[site] = val
            else:
                v[site] = val
    branches = [full]
    cur = list(WINDOW)
    reg = []
    out = []
    for t in range(tmax + 1):
        act = sched[t]
        if act is not None:
            c, s = act
            r = u[c] if s == 0 else v[c]
            nb = []
            for b in branches:
                for part in (b & r, b & (full ^ r)):
                    if part:
                        nb.append(part)
            branches = nb
            reg.append(c)
            if leaves:
                cur.remove(c)
        slots = []
        for c in cur:
            slots.append(u[c])
            slots.append(v[c])
        size = 1 << len(slots)
        vals = [0] * size
        for code in range(1, size):
            low = code & -code
            vals[code] = vals[code ^ low] ^ slots[low.bit_length() - 1]
        qtab = _XB_QTAB[len(cur)]
        dets = []
        expose = False
        for b in branches:
            d = 0
            for code in range(size):
                x = vals[code] & b
                if x == 0 or x == b:
                    d |= 1 << code
                    if qtab[code]:
                        expose = True
            dets.append(d)
        out.append((dets, expose))
        if t < tmax:
            arch = set(reg) if archives else set()
            nu, nv = [], []
            for i in range(L):
                if i in arch:
                    nu.append(v[i])
                    nv.append(u[i])
                    continue
                acc = v[i]
                for j in ((i - 1) % L, (i + 1) % L):
                    if j not in arch:
                        acc ^= u[j]
                nu.append(acc)
                nv.append(u[i])
            u, v = nu, nv
    return out


def xb_compare(sp_recs, xb_recs):
    """(membership mismatches over (functional, branch), exposure mismatches over times, times compared)."""
    mism = 0
    emism = 0
    for rec, (dets, expose) in zip(sp_recs, xb_recs):
        for d in dets:
            mism += (d ^ rec['members']).bit_count()
        if expose != rec['expose']:
            emism += 1
    return mism, emism, min(len(sp_recs), len(xb_recs))


# =====================================================================================================================
# C-STEP, C-HOR, C-SUPP-F (no schedule enumeration)
# =====================================================================================================================
def mat_mul(A, B):
    """Rows of A.B, both given by rows."""
    out = []
    for ra in A:
        acc = 0
        j = 0
        while ra:
            if ra & 1:
                acc ^= B[j]
            ra >>= 1
            j += 1
        out.append(acc)
    return out


def mat_t(A, n):
    return [sum(((A[r] >> c) & 1) << r for r in range(n)) for c in range(n)]


def ring_reference(L):
    """The unmodified N_1 ring matrix, written directly from the rule (C-DEISO (a)'s reference and C-HOR's M_L)."""
    rows = []
    for i in range(L):
        rows.append((1 << ((i - 1) % L)) ^ (1 << ((i + 1) % L)) ^ (1 << (L + i)))
    for i in range(L):
        rows.append(1 << i)
    return rows


def raw_q(g, L):
    return (g & (g >> L) & ((1 << L) - 1)).bit_count() & 1


def raw_omega(g, h, L):
    m = (1 << L) - 1
    return (((g & (h >> L)) ^ ((g >> L) & h)) & m).bit_count() & 1


def step_violations(L, archived, mut=frozenset()):
    """C-STEP for one step matrix: inverse both ways, M^T J M = J, Q* and omega preserved on every basis pair."""
    n = 2 * L
    M = sp_step(L, archived, mut)
    Mi = sp_inverse(L, archived, mut)
    ident = [1 << i for i in range(n)]
    J = [1 << (L + i) for i in range(L)] + [1 << i for i in range(L)]
    viol = 0
    if mat_mul(M, Mi) != ident:
        viol += 1
    if mat_mul(Mi, M) != ident:
        viol += 1
    if mat_mul(mat_mul(mat_t(M, n), J), M) != J:
        viol += 1
    basis = [1 << i for i in range(n)]
    tr = [mat_mul([g], Mi)[0] for g in basis]
    for i in range(n):
        if raw_q(tr[i], L) != raw_q(basis[i], L):
            viol += 1
        for j in range(n):
            if raw_omega(tr[i], tr[j], L) != raw_omega(basis[i], basis[j], L):
                viol += 1
    return viol


def horizon(H, L):
    """C-HOR: T <= |H|, and M_L^t, M_L^{-t} vanish between sites at ring distance > t for t <= T."""
    M = ring_reference(L)
    Mi = sp_inverse(L, frozenset())
    n = 2 * L
    P = [1 << i for i in range(n)]
    Pi = list(P)
    viol = 0
    for t in range(1, T + 1):
        P = mat_mul(M, P)
        Pi = mat_mul(Mi, Pi)
        for a in range(n):
            for b in range(n):
                d = min((a % L - b % L) % L, (b % L - a % L) % L)
                if d > t and ((P[a] >> b) & 1 or (Pi[a] >> b) & 1):
                    viol += 1
    return {'T_le_H': T <= H, 'radius_violations': viol}


SUPP_F_LAW = {(0, 0): Fraction(3, 8), (1, 1): Fraction(3, 8), (0, 1): Fraction(1, 8), (1, 0): Fraction(1, 8)}


def supp_f(L):
    """C-SUPP-F: variant I, pattern uvv with known values 0, register (0, v) at t = 0, evaluate at t = 0. The law of
    (u_1, v_0) is SUPP_F_LAW, every other unknown uniform and independent; exact enumeration over every assignment
    in Fraction. Returns P(u_1 + v_1 = 0 | v_0 = r) for r = 0, 1 and the span method's membership verdict."""
    pattern = 'uvv'
    unknown = []
    for site in range(L):
        for slot in (0, 1):
            if not (site in WINDOW and slot == known_slot(pattern, site)):
                unknown.append((site, slot))
    nun = len(unknown)
    iu1, iv0 = unknown.index((1, 0)), unknown.index((0, 1))
    other = Fraction(1, 1 << (nun - 2))
    num = [Fraction(0), Fraction(0)]
    den = [Fraction(0), Fraction(0)]
    for a in range(1 << nun):
        u1 = a >> iu1 & 1
        v0 = a >> iv0 & 1
        p = SUPP_F_LAW[(u1, v0)] * other
        f = u1 ^ 0                             # u_1 + v_1, with v_1 known and 0
        den[v0] += p
        if f == 0:
            num[v0] += p
    cond = [num[r] * Fraction(den[r].denominator, den[r].numerator) for r in (0, 1)]
    sched = ((0, 1),) + (None,) * T
    gens = sp_s_at(L, 'I', pattern, sched, 0)
    target = sp_unit(L, 1, 0) | sp_unit(L, 1, 1)
    return {'law': {'pair': '(u_1, v_0)', 'P': {'%d%d' % k: str(SUPP_F_LAW[k]) for k in SUPP_F_LAW},
                    'others': 'uniform, independent'},
            'cond_v0_0': str(cond[0]), 'cond_v0_1': str(cond[1]),
            'span_determined': sp_in_span(L, gens, target)}


# =====================================================================================================================
# The enumeration (decisive mode only)
# =====================================================================================================================
def case_list_sha(cases):
    return sha256_hex(canonical([[p, sched_json(s)] for p, s in cases]).encode())


def render_functional(code, window):
    terms = []
    for k, c in enumerate(window):
        if code >> (2 * k) & 1:
            terms.append('u_%d' % c)
        if code >> (2 * k + 1) & 1:
            terms.append('v_%d' % c)
    return '+'.join(terms)


def enumerate_variant(L, variant, extra=(), xb_values=(), active=False, deiso=False, witness=False, used=None,
                      hash_cases=False):
    """Every case of one variant at one size, in the frozen order. Decisive mode only."""
    if _GUARD[0]:
        raise RuntimeError('enumeration refused under --self-test')
    st = {'cases': 0, 'exposing_V': 0, 'no_reg_at_T': 0, 'reg_in_1_to_Tm1': 0, 'nv': 0, 'coupling': 0,
          'active_expose': 0, 'active_noniso': 0, 'at_registration': 0, 'records_kept_violations': 0,
          'min_rank_I': None, 'knowledge_injections': 0, 'step_is_ring_violations': 0,
          'd_i_diff_outside_archived': 0, 'witness': None, 'empty_t0_all': True}
    xb = {kv: {'checked_cases': 0, 'checked_times': 0, 'mismatches': 0, 'exposure_mismatches': 0, 'exposing_V': 0}
          for kv in xb_values}
    ring = ring_reference(L)
    cases = []
    for pattern in PATTERNS:
        for sched in SCHEDULES:
            cases.append((pattern, sched))
            recs, ticks, inj = sp_case(L, variant, pattern, sched, extra=extra, active=active)
            st['cases'] += 1
            st['knowledge_injections'] += inj
            for arch, regset in ticks:
                if used is not None:
                    used.add(arch)
                if deiso:
                    M = sp_step(L, arch)
                    if M != ring:
                        st['step_is_ring_violations'] += 1
                    MI = sp_step(L, regset)
                    amask = 0
                    for c in regset:
                        amask |= (1 << c) | (1 << (L + c))
                    for r in range(2 * L):
                        if amask >> r & 1:
                            continue
                        if (M[r] ^ MI[r]) & ~amask:
                            st['d_i_diff_outside_archived'] += 1
                            break
            exp = any(r['expose'] for r in recs)
            if exp:
                st['exposing_V'] += 1
                if sched[T] is None:
                    st['no_reg_at_T'] += 1
                    if sched[0] is None:
                        st['reg_in_1_to_Tm1'] += 1
                if witness and st['witness'] is None:
                    t = next(i for i, r in enumerate(recs) if r['expose'])
                    rec = recs[t]
                    low = rec['members'] & SP_QONE[rec['n']]
                    code = (low & -low).bit_length() - 1
                    st['witness'] = {'pattern': pattern, 'schedule': sched_json(sched), 't': t,
                                     'window': list(rec['window']), 'code': code,
                                     'functional': render_functional(code, rec['window']),
                                     'uses_t_eq_T': sched[T] is not None}
            if sched == EMPTY and not recs[0]['expose']:
                st['empty_t0_all'] = False
            if recs[0]['expose'] and recs[0]['registered_now']:   # exposure at t = 0 from a registration at t = 0
                st['at_registration'] += 1
            if any(r['nv'] for r in recs):
                st['nv'] += 1
            if any(r['coupling'] for r in recs):
                st['coupling'] += 1
            if active:
                st['active_expose'] += any(r['active_expose'] for r in recs)
                st['active_noniso'] += any(r['active_noniso'] for r in recs)
            st['records_kept_violations'] += sum(1 for r in recs if not r['records_ok'])
            mr = min(r['rank_I'] for r in recs)
            st['min_rank_I'] = mr if st['min_rank_I'] is None else min(st['min_rank_I'], mr)
            for kv in xb_values:
                xrecs = xb_case(L, variant, pattern, sched, known_value=kv)
                m, e, n = xb_compare(recs, xrecs)
                x = xb[kv]
                x['checked_cases'] += 1
                x['checked_times'] += n
                x['mismatches'] += m
                x['exposure_mismatches'] += e
                x['exposing_V'] += any(ex for _, ex in xrecs)
    st['case_list_sha256'] = case_list_sha(cases) if hash_cases else None
    return st, xb


def flags(s, size_key):
    """The checker's own green flags, per the frozen field -> predicate table."""
    D, I, xb = s['D'], s['I'], s['xb']
    f = {
        'CC-ISO': I['exposing_V'] == 0 and I['exposing_active'] == 0 and I['nonisotropic'] == 0,
        'C-NV': D['nv_cases'] > 0 and I['nv_cases'] > 0,
        'C-SUPP-X': s['supp_x']['exposing_V'] > 0,
        'C-SUPP-F': (s['supp_f']['cond_v0_0'] == '3/4' and s['supp_f']['cond_v0_1'] == '1/4'
                     and s['supp_f']['span_determined'] is False),
        'C9': s['c9']['exposing_V'] > 0,
        'C-DEISO': (D['step_is_ring_violations'] == 0 and s['d_i_diff_outside_archived'] == 0
                    and D['coupling_cases'] > 0 and I['coupling_cases'] == 0
                    and s['case_list_sha256']['D'] == s['case_list_sha256']['I']
                    and D['records_kept_violations'] == 0 and D['min_rank_I'] == 3
                    and D['knowledge_injections'] == 0),
        'C-XB': (all(xb['checked_cases'][v] == 6008 for v in ('D', 'I', 'C9'))
                 and all(xb['checked_times'][v] == 5 * 6008 for v in ('D', 'I', 'C9'))
                 and xb['mismatches'] == 0 and xb['exposure_mismatches'] == 0
                 and xb['exposing_V']['D'] == D['exposing_V'] and xb['exposing_V']['I'] == I['exposing_V']
                 and xb['exposing_V']['C9'] == s['c9']['exposing_V']),
        'M-PLANT': (s['plant']['D']['empty_t0'] is True and s['plant']['I']['empty_t0'] is True
                    and s['plant']['D']['exposing_V'] > 0 and s['plant']['I']['exposing_V'] > 0),
        'C-STEP': s['step']['violations'] == 0,
        'C-HOR': s['horizon']['T_le_H'] is True and s['horizon']['radius_violations'] == 0,
    }
    if size_key == '4':
        a = xb['all1']
        f['C-XB'] = (f['C-XB'] and a['checked_cases']['D'] == 6008 and a['checked_cases']['I'] == 6008
                     and a['mismatches'] == 0 and a['exposure_mismatches'] == 0)
    return f


def measure_size(H, L=None):
    """Every enumeration at one size. Decisive mode only (L defaults to 3 + |H|; decisive() never passes it)."""
    if _GUARD[0]:
        raise RuntimeError('decisive computation refused under --self-test')
    L = 3 + H if L is None else L
    used = set()
    xbv = (0, 1) if H == 4 else (0,)
    d, xd = enumerate_variant(L, 'D', xb_values=xbv, deiso=True, witness=True, used=used, hash_cases=True)
    i, xi = enumerate_variant(L, 'I', xb_values=xbv, active=True, used=used, hash_cases=True)
    c9, xc = enumerate_variant(L, 'C9', xb_values=(0,), used=used)
    relation = sp_unit(L, 1, 0) | sp_unit(L, 0, 1)
    plant = sp_unit(L, 1, 0) | sp_unit(L, 1, 1)
    sx, _ = enumerate_variant(L, 'I', extra=(relation,), used=used)
    pd, _ = enumerate_variant(L, 'D', extra=(plant,), used=used)
    pi, _ = enumerate_variant(L, 'I', extra=(plant,), used=used)
    s = {
        'D': {'cases': d['cases'], 'exposing_V': d['exposing_V'], 'exposing_V_no_reg_at_T': d['no_reg_at_T'],
              'exposing_V_reg_in_1_to_Tm1': d['reg_in_1_to_Tm1'], 'witness': d['witness'], 'nv_cases': d['nv'],
              'coupling_cases': d['coupling'], 'step_is_ring_violations': d['step_is_ring_violations'],
              'records_kept_violations': d['records_kept_violations'], 'min_rank_I': d['min_rank_I'],
              'knowledge_injections': d['knowledge_injections']},
        'I': {'cases': i['cases'], 'exposing_V': i['exposing_V'], 'exposing_active': i['active_expose'],
              'nonisotropic': i['active_noniso'], 'nv_cases': i['nv'], 'coupling_cases': i['coupling']},
        'd_i_diff_outside_archived': d['d_i_diff_outside_archived'],
        'case_list_sha256': {'D': d['case_list_sha256'], 'I': i['case_list_sha256']},
        'supp_x': {'cases': sx['cases'], 'exposing_V': sx['exposing_V']},
        'supp_f': supp_f(L),
        'c9': {'cases': c9['cases'], 'exposing_V': c9['exposing_V'], 'exposing_at_registration': c9['at_registration']},
        'plant': {'D': {'empty_t0': pd['empty_t0_all'], 'exposing_V': pd['exposing_V']},
                  'I': {'empty_t0': pi['empty_t0_all'], 'exposing_V': pi['exposing_V']}},
        'xb': {'checked_cases': {'D': xd[0]['checked_cases'], 'I': xi[0]['checked_cases'],
                                 'C9': xc[0]['checked_cases']},
               'checked_times': {'D': xd[0]['checked_times'], 'I': xi[0]['checked_times'],
                                 'C9': xc[0]['checked_times']},
               'exposing_V': {'D': xd[0]['exposing_V'], 'I': xi[0]['exposing_V'], 'C9': xc[0]['exposing_V']},
               'mismatches': xd[0]['mismatches'] + xi[0]['mismatches'] + xc[0]['mismatches'],
               'exposure_mismatches': (xd[0]['exposure_mismatches'] + xi[0]['exposure_mismatches']
                                       + xc[0]['exposure_mismatches'])},
        'step': {'violations': sum(step_violations(L, a) for a in sorted(used, key=sorted))},
        'horizon': horizon(H, L),
    }
    if H == 4:
        s['xb']['all1'] = {'checked_cases': {'D': xd[1]['checked_cases'], 'I': xi[1]['checked_cases']},
                           'mismatches': xd[1]['mismatches'] + xi[1]['mismatches'],
                           'exposure_mismatches': xd[1]['exposure_mismatches'] + xi[1]['exposure_mismatches']}
    s['flags'] = flags(s, str(H))
    return s


def parameters():
    return {'q': 2, 'w': len(WINDOW), 'T': T, 'H': list(SIZES), 'L': [3 + h for h in SIZES],
            'rule': "N_1: u_i' = u_{i-1} + u_{i+1} + v_i, v_i' = u_i",
            'registration_times': list(range(T + 1)), 'patterns': len(PATTERNS), 'schedules': len(SCHEDULES),
            'cases': len(PATTERNS) * len(SCHEDULES)}


def decisive():
    _GUARD[0] = False
    out = {'schema': SCHEMA, 'version': VERSION, 'parameters': parameters(), 'complete': False}
    for H in SIZES:
        out[str(H)] = measure_size(H)
    out['complete'] = True
    sys.stdout.write(canonical(out))
    sys.stdout.flush()
    green = all(all(out[str(H)]['flags'][c] for c in CONTROLS) for H in SIZES)
    return 0 if green else 3


# =====================================================================================================================
# --fixture-output: a hand-written synthetic record (design run only). It computes nothing and is not a result:
# complete is false, every count is 0 and every flag is false.
# =====================================================================================================================
_FIXTURE_SIZE = {
    'D': {'cases': 0, 'exposing_V': 0, 'exposing_V_no_reg_at_T': 0, 'exposing_V_reg_in_1_to_Tm1': 0,
          'witness': None, 'nv_cases': 0, 'coupling_cases': 0, 'step_is_ring_violations': 0,
          'records_kept_violations': 0, 'min_rank_I': 0, 'knowledge_injections': 0},
    'I': {'cases': 0, 'exposing_V': 0, 'exposing_active': 0, 'nonisotropic': 0, 'nv_cases': 0,
          'coupling_cases': 0},
    'd_i_diff_outside_archived': 0,
    'case_list_sha256': {'D': '0000000000000000000000000000000000000000000000000000000000000000',
                         'I': '0000000000000000000000000000000000000000000000000000000000000000'},
    'supp_x': {'cases': 0, 'exposing_V': 0},
    'supp_f': {'law': {'pair': '(u_1, v_0)', 'P': {'00': '3/8', '01': '1/8', '10': '1/8', '11': '3/8'},
                       'others': 'uniform, independent'},
               'cond_v0_0': '0', 'cond_v0_1': '0', 'span_determined': False},
    'c9': {'cases': 0, 'exposing_V': 0, 'exposing_at_registration': 0},
    'plant': {'D': {'empty_t0': False, 'exposing_V': 0}, 'I': {'empty_t0': False, 'exposing_V': 0}},
    'xb': {'checked_cases': {'D': 0, 'I': 0, 'C9': 0}, 'checked_times': {'D': 0, 'I': 0, 'C9': 0},
           'exposing_V': {'D': 0, 'I': 0, 'C9': 0}, 'mismatches': 0, 'exposure_mismatches': 0},
    'step': {'violations': 0},
    'horizon': {'T_le_H': False, 'radius_violations': 0},
    'flags': {'CC-ISO': False, 'C-NV': False, 'C-SUPP-X': False, 'C-SUPP-F': False, 'C9': False,
              'C-DEISO': False, 'C-XB': False, 'M-PLANT': False, 'C-STEP': False, 'C-HOR': False},
}
_FIXTURE_ALL1 = {'checked_cases': {'D': 0, 'I': 0}, 'mismatches': 0, 'exposure_mismatches': 0}


def fixture():
    s4 = json.loads(json.dumps(_FIXTURE_SIZE))
    s4['xb']['all1'] = dict(_FIXTURE_ALL1)
    s6 = json.loads(json.dumps(_FIXTURE_SIZE))
    rec = {'schema': SCHEMA, 'version': VERSION,
           'parameters': {'q': 2, 'w': 3, 'T': 4, 'H': [4, 6], 'L': [7, 9],
                          'rule': "N_1: u_i' = u_{i-1} + u_{i+1} + v_i, v_i' = u_i",
                          'registration_times': [0, 1, 2, 3, 4], 'patterns': 8, 'schedules': 751, 'cases': 6008},
           'complete': False, '4': s4, '6': s6}
    sys.stdout.write(canonical(rec))
    return 0


# =====================================================================================================================
# --self-test. No call below reaches enumerate_variant, measure_size or decisive, and no case of variant D is
# evaluated: every hand case runs in variant I, or in C9 at t = 0, and M-PLANT at t = 0 runs before any tick, where D
# and I coincide. _GUARD (set outside the default mode) makes any other call raise; the guard checks below call D and
# C9 beyond t = 0 only to see them refused at the first statement.
# =====================================================================================================================
def self_test():
    _GUARD[0] = True
    results = []

    def check(name, cond, detail=''):
        results.append(bool(cond))
        print(('PASS ' if cond else 'FAIL ') + name + (('  [' + detail + ']') if detail else ''))

    # combinatorics of the case list (no dynamics)
    check('751 schedules; 361 with no registration at t = T; 139 registering only at t in 1..T-1',
          len(SCHEDULES) == 751 and sum(1 for s in SCHEDULES if s[T] is None) == 361
          and sum(1 for s in SCHEDULES if s[T] is None and s[0] is None) == 139)
    check('patterns in the frozen order', PATTERNS == ('uuu', 'uuv', 'uvu', 'uvv', 'vuu', 'vuv', 'vvu', 'vvv'))
    check('schedules in the frozen order', list(SCHEDULES) == sorted(
        SCHEDULES, key=lambda s: tuple(0 if a is None else 1 + 2 * a[0] + a[1] for a in s)))
    # SHA-256 against FIPS 180-2 vectors
    check('sha256 vectors', sha256_hex(b'') == 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
          and sha256_hex(b'abc') == 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
          and sha256_hex(b'abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq')
          == '248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1'
          and sha256_hex(b'a' * 1000) == '41edece42d63e8d9bf515a9ba6932e1c20cbc9f5a5d134645adb5db1b9737ea3')
    # C-STEP on every step matrix either variant can use, at both sizes
    for L in (7, 9):
        tot = 0
        for k in range(8):
            arch = frozenset(c for c in WINDOW if k >> c & 1)
            tot += step_violations(L, arch)
        check('C-STEP L=%d: the ring step and every archive step: 0 violations' % L, tot == 0, 'violations %d' % tot)
        check('C-STEP L=%d detects a center term' % L, step_violations(L, frozenset(), frozenset({'center'})) > 0)
        check('ring step equals the reference ring matrix at L=%d' % L,
              sp_step(L, frozenset()) == ring_reference(L))
    # C-HOR
    for H in SIZES:
        h = horizon(H, 3 + H)
        check('C-HOR |H|=%d: T <= |H| and 0 radius violations' % H, h['T_le_H'] is True and h['radius_violations'] == 0,
              str(h))
    check('C-HOR toy |H|=2 (L=5): T <= |H| fails', horizon(2, 5)['T_le_H'] is False)
    # C-DEISO (c) arithmetic: a registered u_1, transported two ticks
    for L in (7, 9):
        ring_tr = sp_transport_for(L, frozenset(), frozenset())
        r2 = ring_tr(ring_tr(sp_unit(L, 1, 0)))
        check('L=%d: u_1 transported two coupled ticks has omega = 1 with u_0 and u_2' % L,
              raw_omega(r2, sp_unit(L, 0, 0), L) == 1 and raw_omega(r2, sp_unit(L, 2, 0), L) == 1)
        arch_tr = sp_transport_for(L, frozenset({1}), frozenset())
        a2 = arch_tr(arch_tr(sp_unit(L, 1, 0)))
        cell1 = sp_unit(L, 1, 0) | sp_unit(L, 1, 1)
        check('L=%d: u_1 transported two archived ticks stays on cell 1' % L, a2 & ~cell1 == 0 and a2 != 0)

    L = 7
    # C-NV hand case: pattern vvv, register (1, u) at t = 1; v_0 + v_2 at t = 1 (variant I; t <= 1)
    cnv = ('vvv', (None, (1, 0), None, None, None))
    recs, _, _ = sp_case(L, 'I', cnv[0], cnv[1], tmax=1)
    code_v0v2 = (1 << 1) | (1 << 3)            # window (0, 2): v_0 is bit 1, v_2 is bit 3
    check('C-NV hand case: v_0 + v_2 in S_1 and window (0, 2)',
          recs[1]['window'] == (0, 2) and recs[1]['members'] >> code_v0v2 & 1 == 1)
    check('C-NV hand case: determined by registration (nv at t = 1)', recs[1]['nv'] is True)
    # C-SUPP-X hand case: pattern uvv, register (0, v) at t = 0; u_1 + v_1 (variant I; t = 0)
    sx = ('uvv', ((0, 1), None, None, None, None))
    rel = sp_unit(L, 1, 0) | sp_unit(L, 0, 1)
    with_rel, _, _ = sp_case(L, 'I', sx[0], sx[1], extra=(rel,), tmax=0)
    without, _, _ = sp_case(L, 'I', sx[0], sx[1], tmax=0)
    code_u1v1 = 0b11                           # window (1, 2): u_1 bit 0, v_1 bit 1
    check('C-SUPP-X hand case: with the relation u_1 + v_1 is in S_0 and exposes',
          with_rel[0]['window'] == (1, 2) and with_rel[0]['members'] >> code_u1v1 & 1 and with_rel[0]['expose'])
    check('C-SUPP-X hand case: without the relation u_1 + v_1 is not in S_0',
          not (without[0]['members'] >> code_u1v1 & 1) and not without[0]['expose'])
    # C9 hand case: v_1 known, u_1 registered at t = 0, the cell stays in V (variant C9; t = 0)
    c9 = ('uvv', ((1, 0), None, None, None, None))
    rc9, _, _ = sp_case(L, 'C9', c9[0], c9[1], tmax=0)
    code_c9 = 0b1100                           # window (0, 1, 2): u_1 bit 2, v_1 bit 3
    check('C9 hand case: u_1 + v_1 in S_0, exposing at the registration time',
          rc9[0]['window'] == (0, 1, 2) and rc9[0]['members'] >> code_c9 & 1 and rc9[0]['expose']
          and rc9[0]['registered_now'])
    # M-PLANT at t = 0: the empty schedule exposes before any tick (no step is applied, so D and I coincide here)
    plant = sp_unit(L, 1, 0) | sp_unit(L, 1, 1)
    ok = all(sp_case(L, 'I', p, EMPTY, extra=(plant,), tmax=0)[0][0]['expose'] for p in PATTERNS)
    ok0 = not any(sp_case(L, 'I', p, EMPTY, tmax=0)[0][0]['expose'] for p in PATTERNS)
    check('M-PLANT at t = 0: the planted u_1 + v_1 exposes for every pattern; without it nothing does', ok and ok0)
    # C-SUPP-F's law
    sf = supp_f(L)
    check('C-SUPP-F: "3/4", "1/4", span_determined false', sf['cond_v0_0'] == '3/4' and sf['cond_v0_1'] == '1/4'
          and sf['span_determined'] is False, '%s %s %s' % (sf['cond_v0_0'], sf['cond_v0_1'], sf['span_determined']))
    # C-XB, unmutated, on the hand cases
    m, e, n = xb_compare(sp_case(L, 'I', cnv[0], cnv[1], tmax=1)[0], xb_case(L, 'I', cnv[0], cnv[1], tmax=1))
    check('C-XB on the C-NV hand case: 0 mismatches, 0 exposure mismatches', (m, e, n) == (0, 0, 2), str((m, e, n)))
    m1, e1, n1 = xb_compare(sp_case(L, 'I', cnv[0], cnv[1], tmax=1)[0],
                            xb_case(L, 'I', cnv[0], cnv[1], known_value=1, tmax=1))
    check('C-XB on the C-NV hand case, known values 1: 0, 0', (m1, e1) == (0, 0), str((m1, e1, n1)))
    m, e, n = xb_compare(rc9, xb_case(L, 'C9', c9[0], c9[1], tmax=0))
    check('C-XB on the C9 hand case: 0 mismatches, 0 exposure mismatches', (m, e) == (0, 0), str((m, e, n)))
    # mutation: transport by M in place of M^{-1}
    m, e, n = xb_compare(sp_case(L, 'I', cnv[0], cnv[1], tmax=1, mut=frozenset({'fwd'}))[0],
                         xb_case(L, 'I', cnv[0], cnv[1], tmax=1))
    check('transport mutation (M for M^-1): C-XB fails on the C-NV hand case', m > 0, 'mismatches %d' % m)
    # mutation: the omega pair term dropped from the span detector
    m, e, n = xb_compare(sp_case(L, 'C9', c9[0], c9[1], tmax=0, mut=frozenset({'wdrop'}))[0],
                         xb_case(L, 'C9', c9[0], c9[1], tmax=0))
    check('omega-drop mutation: C-XB reports an exposure mismatch on the C9 hand case', e > 0,
          'exposure mismatches %d' % e)
    # mutation: a v-index offset at L = 9
    L9 = 9
    sv = step_violations(L9, frozenset(), frozenset({'voff'}))
    m, e, n = xb_compare(sp_case(L9, 'I', cnv[0], cnv[1], tmax=1, mut=frozenset({'voff'}))[0],
                         xb_case(L9, 'I', cnv[0], cnv[1], tmax=1))
    check('v-offset mutation at L=9: C-STEP or C-XB fails on the C-NV hand case', sv > 0 or m > 0 or e > 0,
          'C-STEP violations %d, C-XB mismatches %d, exposure mismatches %d' % (sv, m, e))
    m, e, n = xb_compare(sp_case(L9, 'I', cnv[0], cnv[1], tmax=1)[0], xb_case(L9, 'I', cnv[0], cnv[1], tmax=1))
    check('C-XB on the C-NV hand case at L=9, unmutated: 0, 0', (m, e) == (0, 0), str((m, e, n)))
    # the C-NV hand case in variant I through t = T: three archived ticks after the registration
    for LL in (7, 9):
        m, e, n = xb_compare(sp_case(LL, 'I', cnv[0], cnv[1])[0], xb_case(LL, 'I', cnv[0], cnv[1]))
        check('C-XB on the C-NV hand case through t = T in variant I at L=%d: 0, 0 over 5 times' % LL,
              (m, e, n) == (0, 0, 5), str((m, e, n)))
    # the guard (I-N1): each call below raises at its first statement, before anything is computed
    for name, call in (('variant D', lambda: sp_case(L, 'D', 'uuu', EMPTY, tmax=0)),
                       ('C9 beyond t = 0 (span path)', lambda: sp_case(L, 'C9', 'uuu', EMPTY, tmax=1)),
                       ('C9 beyond t = 0 (C-XB path)', lambda: xb_case(L, 'C9', 'uuu', EMPTY, tmax=1))):
        try:
            call()
            refused = False
        except RuntimeError:
            refused = True
        check('guard: %s is refused outside the default mode' % name, refused)
    # the fixture's shape matches what the decisive mode writes
    ok = sorted(_FIXTURE_SIZE['flags']) == sorted(CONTROLS)
    check('fixture flags name every control', ok)
    good = all(results)
    print('marc_check: self-test %s (%d checks)' % ('OK' if good else 'FAILED', len(results)))
    return 0 if good else 1


if __name__ == '__main__':
    args = sys.argv[1:]
    if args == ['--self-test']:
        sys.exit(self_test())
    if args == ['--fixture-output']:
        sys.exit(fixture())
    if args == []:
        sys.exit(decisive())
    sys.stderr.write(__doc__)
    sys.exit(2)
