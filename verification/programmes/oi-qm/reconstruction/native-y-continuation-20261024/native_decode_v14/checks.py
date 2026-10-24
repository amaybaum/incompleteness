"""Fixed redundant q10 readouts of the retained two-front native table.

Reads the reviewed native_route_v13 q10 table and decides, for every
nonconstant Boolean readout of the q10 raw triple, the exact number of
jointly affine known-seed E,N source laws under which that readout returns
the old sign s on all 24 accepted contexts. Two independently written exact
solvers must agree; every control must pass before verdict text is emitted.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent.parent
ROUTE = ROOT / 'native_route_v13'
PIN_ROUTE_RESULT = '762b9799db7448c4eecf2c994c8c68ff94e1be83a7f6884b4a36385505df5a02'
PIN_REVIEW_RESULT = '73780def8505d68d1967936116a88a49d471eb32aeb83d528ff3cd41025ae6e4'
PIN_TABLE = 'b2f32466113dede2fa9e43469f5c209fde5d610180ed748dcd025d4cd2a4b3cc'
PIN_PLAN_BASE = '94a4e6ccf18845af6c2d37cd797da1082f575d65'

CONTEXTS = tuple(k for k in product((0, 1), repeat=5) if (k[3], k[4]) != (0, 1))
FEATURE_NAMES = ('1', 'u', 'mY', 'mR', 'a', 'b')
READOUTS = tuple(range(1, 255))   # bit c of D is the readout of raw code c


def need(ok, label):
    if not ok:
        raise RuntimeError('control failed: ' + label)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def row_index(x, k, e, n):
    u, my, mr, a, b = k
    i = 0
    for v in (x, u, my, mr, a, b):
        i = 2 * i + v
    return (i * 8 + e) * 8 + n


def kernel_from_table(table):
    """q[s][j][w]: raw q10 code for sign s, context j, w=8*Ecode+Ncode."""
    q = [[[0] * 64 for _ in CONTEXTS] for _ in (0, 1)]
    for s in (0, 1):
        for j, k in enumerate(CONTEXTS):
            x = s ^ k[0] ^ k[3]
            for w in range(64):
                q[s][j][w] = table[row_index(x, k, w >> 3, w & 7)]
    return q


def features(chosen):
    """Feature vector of each context as an int over the chosen features."""
    out = []
    for k in CONTEXTS:
        full = (1,) + k
        out.append(sum(full[f] << i for i, f in enumerate(chosen)))
    return tuple(out)


def readout_sets(q, d):
    """G_j: the (E,N) pairs whose raw outputs read back s=0 and s=1."""
    g = []
    for j in range(len(CONTEXTS)):
        mask = 0
        for w in range(64):
            if not (d >> q[0][j][w]) & 1 and (d >> q[1][j][w]) & 1:
                mask |= 1 << w
        g.append(mask)
    return g


def pair_sets(q, o0, o1):
    return [sum(1 << w for w in range(64) if q[0][j][w] == o0 and q[1][j][w] == o1)
            for j in range(len(CONTEXTS))]


def distinct_sets(q):
    return [sum(1 << w for w in range(64) if q[0][j][w] != q[1][j][w])
            for j in range(len(CONTEXTS))]


# ---------------------------------------------------------------- solver A
# Six source fields (E.A,E.B,E.D,N.A,N.B,N.D) = bits 5..0 of w. Each field is
# affine: field value at context j is parity(coefficient & feature_j). The
# coefficient of each field ranges over all 2^m values; a bit set over those
# values is intersected context by context.

FIELD = tuple(tuple(sum(1 << w for w in range(64) if ((w >> (5 - i)) & 1) == b)
                    for b in (0, 1)) for i in range(6))


class SolverA:
    """Fields are eliminated `group` at a time over bit sets of coefficient tuples."""

    def __init__(self, feats, order=(0, 1, 2, 3, 4, 5), group=1):
        self.feats = feats
        self.order = order
        self.group = group
        size = 1 << max(1, max(f.bit_length() for f in feats))
        self.size = size
        tuples = size ** group
        self.all = (1 << tuples) - 1
        nv = 1 << group
        self.val = []
        maskv = [[0] * nv for _ in feats]
        for t in range(tuples):
            parts = [(t // size ** i) % size for i in range(group)]
            row = []
            for j, f in enumerate(feats):
                v = 0
                for c in parts:
                    v = 2 * v + ((c & f).bit_count() & 1)
                row.append(v)
                maskv[j][v] |= 1 << t
            self.val.append(row)
        self.allow = [[0] * (1 << nv) for _ in feats]
        for j in range(len(feats)):
            for sub in range(1 << nv):
                for v in range(nv):
                    if sub >> v & 1:
                        self.allow[j][sub] |= maskv[j][v]
        self.full = (1 << nv) - 1
        self.levels = [order[i:i + group] for i in range(0, 6, group)]
        self.levelmask = []
        for fields in self.levels:
            masks = []
            for v in range(nv):
                m = 0
                for w in range(64):
                    if all(((w >> (5 - f)) & 1) == ((v >> (group - 1 - i)) & 1)
                           for i, f in enumerate(fields)):
                        m |= 1 << w
                masks.append(m)
            self.levelmask.append(tuple(masks))

    def run(self, g, collect=0, stop_first=False):
        """Count all laws; with group=1, prefix3 counts laws consistent on the first three fields."""
        self.count = 0
        self.prefix3 = 0
        self.found = []
        self.stop = stop_first
        if all(g):
            self._go(0, list(g), [], collect)
        return self.count

    def _decode(self, t):
        return [(t // self.size ** i) % self.size for i in range(self.group)]

    def _canonical(self, coeffs):
        out = [0] * 6
        for f, c in zip(self.order, coeffs):
            out[f] = c
        return tuple(out)

    def _go(self, level, r, coeffs, collect):
        possible = self.all
        masks = self.levelmask[level]
        full = self.full
        allow = self.allow
        if self.group == 2:
            m0, m1, m2, m3 = masks
            for j, rj in enumerate(r):
                sub = ((rj & m0 and 1) | (rj & m1 and 2) | (rj & m2 and 4) | (rj & m3 and 8))
                if sub != 15:
                    possible &= allow[j][sub]
                    if not possible:
                        return
        else:
            for j, rj in enumerate(r):
                sub = 0
                for v, m in enumerate(masks):
                    if rj & m:
                        sub |= 1 << v
                if sub != full:
                    possible &= allow[j][sub]
                    if not possible:
                        return
        if self.group == 1 and level == 2:
            self.prefix3 += possible.bit_count()
        if level == len(self.levels) - 1:
            self.count += possible.bit_count()
            while possible and len(self.found) < collect:
                bit = possible & -possible
                self.found.append(self._canonical(coeffs + self._decode(bit.bit_length() - 1)))
                possible ^= bit
            return
        while possible:
            bit = possible & -possible
            t = bit.bit_length() - 1
            possible ^= bit
            row = self.val[t]
            self._go(level + 1, [rj & masks[row[j]] for j, rj in enumerate(r)],
                     coeffs + self._decode(t), collect)
            if self.stop and self.count:
                return


def evaluate(coeffs, feat):
    """Source value w=8*E+N of the affine law with field coefficients coeffs."""
    w = 0
    for c in coeffs:
        w = 2 * w + ((c & feat).bit_count() & 1)
    return w


# ---------------------------------------------------------------- solver B
# An affine law is a linear map C from feature space to six-bit values. Fix a
# basis of the context features; C is determined by its values there, and
# every other context's value is the XOR of the basis values in its expansion.

def reduce(v, rows):
    e = 0
    for rv, pivot, re in rows:
        if (v >> pivot) & 1:
            v ^= rv
            e ^= re
    return v, e


def add_row(rows, v, e):
    rows.append((v, v.bit_length() - 1, e))
    rows.sort(key=lambda t: -t[1])


class SolverB:
    def __init__(self, feats):
        self.feats = feats
        width = max(f.bit_length() for f in feats)
        # Greedy basis: each new basis context maximizes the number of
        # contexts already determined by the basis chosen so far.
        basis, rows = [], []
        while True:
            best = None
            for j, f in enumerate(feats):
                v, e = reduce(f, rows)
                if not v:
                    continue
                trial = list(rows)
                add_row(trial, v, e)
                covered = sum(1 for h in feats if not reduce(h, trial)[0])
                if best is None or covered > best[0]:
                    best = (covered, j)
            if best is None:
                break
            j = best[1]
            v, e = reduce(feats[j], rows)
            add_row(rows, v, e ^ (1 << len(basis)))
            basis.append(j)
        self.basis = basis
        self.free = 6 * (width - len(basis))
        self.checks = [[] for _ in basis]
        for j, f in enumerate(feats):
            if j in basis:
                continue
            v, e = reduce(f, rows)
            if v:
                raise RuntimeError('basis does not span the context features')
            self.checks[e.bit_length() - 1].append((j, e))
        self.width = width

    def run(self, g, collect=0, stop_first=False):
        self.leaves = 0
        self.found = []
        self.stop = stop_first
        self._go(0, [], g, collect)
        return self.leaves << self.free

    def _go(self, d, values, g, collect):
        if d == len(self.basis):
            self.leaves += 1
            if len(self.found) < collect:
                self.found.append(tuple(values))
            return
        mask = g[self.basis[d]]
        while mask:
            bit = mask & -mask
            mask ^= bit
            vals = values + [bit.bit_length() - 1]
            ok = True
            for j, e in self.checks[d]:
                w = 0
                for t in range(d + 1):
                    if (e >> t) & 1:
                        w ^= vals[t]
                if not (g[j] >> w) & 1:
                    ok = False
                    break
            if ok:
                self._go(d + 1, vals, g, collect)
                if self.stop and self.leaves:
                    return


# ---------------------------------------------------------------- brute force

def brute_force(q, chosen):
    """All 64^m column choices; returns per-readout counts and diagnostic count."""
    feats = features(chosen)
    m = len(chosen)
    zo = Counter()
    distinct = 0
    for cols in product(range(64), repeat=m):
        zmask = omask = 0
        dist = True
        for j, f in enumerate(feats):
            w = 0
            for t in range(m):
                if (f >> t) & 1:
                    w ^= cols[t]
            a0, a1 = q[0][j][w], q[1][j][w]
            zmask |= 1 << a0
            omask |= 1 << a1
            dist = dist and a0 != a1
        distinct += dist
        if not zmask & omask:
            zo[zmask, omask] += 1
    counts = Counter()
    for (zmask, omask), mult in zo.items():
        for d in READOUTS:
            if not d & zmask and omask & ~d == 0:
                counts[d] += mult
    return [counts[d] for d in READOUTS], distinct


PLANTED_READOUT = 0b11110000       # reads 1 exactly on raw codes with A=1


def plant(table, coeffs, feats):
    """Synthetic table: the law coeffs gives raw 2 (reads 0) and 5 (reads 1)."""
    synth = list(table)
    for j, k in enumerate(CONTEXTS):
        w = evaluate(coeffs, feats[j])
        for s, code in ((0, 2), (1, 5)):
            synth[row_index(s ^ k[0] ^ k[3], k, w >> 3, w & 7)] = code
    return synth


def anf_degree(d):
    """Algebraic degree of the readout as a Boolean function of (A,B,D)."""
    f = [(d >> c) & 1 for c in range(8)]
    for i in range(3):
        for c in range(8):
            if c >> i & 1:
                f[c] ^= f[c ^ (1 << i)]
    return max((c.bit_count() for c in range(8) if f[c]), default=0)


def affine_readouts(every, table, feats):
    """Post-hoc: readouts of algebraic degree one (a raw field or a parity of fields)."""
    out = []
    by = {}
    for d, c in every:
        by.setdefault(d, []).append(c)
    for d in sorted(by):
        if anf_degree(d) != 1:
            continue
        sols = by[d]
        best = None
        for c in sols:
            used = 0
            for x in c:
                used |= x >> 1
            names_used = [FEATURE_NAMES[i + 1] for i in range(5) if used >> i & 1]
            if best is None or len(names_used) < len(best[0]):
                best = (names_used, c)
        # Linear part of the readout over the raw fields A,B,D (constant dropped).
        linear = [f for f, bit in (('A', 4), ('B', 2), ('D', 1)) if ((d >> bit) & 1) != (d & 1)]
        residual_sign_free = 0
        if len(linear) == 1:
            keep = 7 ^ {'A': 4, 'B': 2, 'D': 1}[linear[0]]
            for c in sols:
                ok = True
                for j, k in enumerate(CONTEXTS):
                    w = evaluate(c, feats[j])
                    r = [table[row_index(s ^ k[0] ^ k[3], k, w >> 3, w & 7)] & keep for s in (0, 1)]
                    ok = ok and r[0] == r[1]
                residual_sign_free += ok
        out.append({'readout_bits': d, 'raw_fields_xored': linear, 'complemented': bool(d & 1),
                    'solutions': len(sols), 'E_constant': sum(all(x <= 1 for x in c[:3]) for c in sols),
                    'fewest_seeds': best[0],
                    'fewest_seed_law_field_coefficients_EA_EB_ED_NA_NB_ND': list(best[1]),
                    'single_field_laws_with_sign_free_other_fields':
                        residual_sign_free if len(linear) == 1 else None})
    return out


def fresh_bit_pairs(every, table, feats, d1=0b11110000, d0=0b00001111):
    """Post-hoc: law pairs for q10.A and its complement that differ only in
    constant coefficients, so one independent initial bit c on those
    constants would give q10.A = s XOR c. Also checks whether the whole
    triple then hides s given the known seeds (equal multisets over c)."""
    by = {}
    for d, c in every:
        by.setdefault(d, []).append(c)
    zero = {}
    for c in by.get(d0, []):
        zero.setdefault(tuple(x >> 1 for x in c), []).append(c)
    pairs = [(a, b) for a in by.get(d1, []) for b in zero.get(tuple(x >> 1 for x in a), [])]
    deltas = Counter(tuple((x ^ y) & 1 for x, y in zip(a, b)) for a, b in pairs)
    hidden = Counter()
    for a, b in pairs:
        good = 0
        for j, k in enumerate(CONTEXTS):
            wa, wb = evaluate(a, feats[j]), evaluate(b, feats[j])
            m = [sorted(table[row_index(s ^ k[0] ^ k[3], k, w >> 3, w & 7)] for w in (wa, wb))
                 for s in (0, 1)]
            good += m[0] == m[1]
        hidden[good] += 1
    return {'pairs': len(pairs),
            'constant_coefficient_deltas_EA_EB_ED_NA_NB_ND': sorted([list(k), v] for k, v in deltas.items()),
            'contexts_with_whole_triple_sign_hidden_counts': sorted([k, v] for k, v in hidden.items()),
            'pairs_hiding_sign_in_all_contexts': hidden[len(CONTEXTS)]}


def solution_structure(every, table, feats):
    """Post-hoc description of all solutions; it does not enter the verdict."""
    e_zero = e_const = n_const = both_const = 0
    support = Counter()
    raw_used = Counter()
    min_raw = None
    for d, c in every:
        ec, nc = c[:3], c[3:]
        e_zero += all(x == 0 for x in ec)
        ek = all(x <= 1 for x in ec)
        nk = all(x <= 1 for x in nc)
        e_const += ek
        n_const += nk
        both_const += ek and nk
        used = 0
        for x in c:
            used |= x >> 1
        support[tuple(FEATURE_NAMES[i + 1] for i in range(5) if used >> i & 1)] += 1
        codes = set()
        for j, k in enumerate(CONTEXTS):
            w = evaluate(c, feats[j])
            for s in (0, 1):
                codes.add((s, table[row_index(s ^ k[0] ^ k[3], k, w >> 3, w & 7)]))
        size = len(codes)
        raw_used[size] += 1
        if min_raw is None or size < min_raw[0]:
            min_raw = (size, d, c)
    return {'solutions': len(every), 'E_identically_000': e_zero, 'E_constant': e_const,
            'N_constant': n_const, 'E_and_N_constant': both_const,
            'seed_support_counts': sorted([list(k), v] for k, v in support.items()),
            'distinct_sign_raw_pairs_used_counts': sorted([k, v] for k, v in raw_used.items()),
            'fewest_sign_raw_pairs': {'count': min_raw[0], 'readout_bits': min_raw[1],
                                      'field_coefficients_EA_EB_ED_NA_NB_ND': list(min_raw[2])}
            if min_raw else None}


# ---------------------------------------------------------------- main

def main():
    route_bytes = (ROUTE / 'result.json').read_bytes()
    need(sha(route_bytes) == PIN_ROUTE_RESULT, 'route result pin')
    route = json.loads(route_bytes)
    review_bytes = (ROUTE / 'review/result.json').read_bytes()
    need(sha(review_bytes) == PIN_REVIEW_RESULT, 'route review result pin')
    review = json.loads(review_bytes)
    table_hex = route['q10_table_hex']
    need(len(table_hex) == 4096, 'table length')
    need(route['table_sha256'] == PIN_TABLE, 'author table digest field')
    need(sha(table_hex.encode()) == PIN_TABLE, 'recomputed table digest')
    need(review['independent_native_table']['sha256'] == PIN_TABLE, 'review table digest')
    need(review['all_controls_passed'] is True, 'review controls recorded green')
    table = [int(ch, 16) for ch in table_hex]
    q = kernel_from_table(table)

    full = tuple(range(6))
    feats = features(full)
    sa_e = SolverA(feats)                          # E fields first: raw-pair reproduction
    sa = SolverA(feats, group=2)                   # primary: two fields per level
    sb = SolverB(feats)
    need(len(sb.basis) == 6 and sb.free == 0, 'context features have full affine rank')

    def basis_values(coeffs, solver, fs):
        return tuple(evaluate(coeffs, fs[j]) for j in solver.basis)

    # Control 2: planted positive control on a synthetic table.
    planted_coeffs = (37, 12, 55, 41, 22, 7)
    synth = plant(table, planted_coeffs, feats)
    gs = readout_sets(kernel_from_table(synth), PLANTED_READOUT)
    count_a = sa.run(gs, collect=1 << 20)
    found_a = set(sa.found)
    count_b = sb.run(gs, collect=1 << 20)
    need(count_a == count_b and count_a >= 1, 'planted counts agree and are positive')
    need(len(found_a) == count_a, 'planted enumeration complete')
    need(planted_coeffs in found_a, 'solver A recovers planted law')
    need({basis_values(c, sb, feats) for c in found_a} == set(sb.found), 'planted solution sets agree')
    planted = {'readout_bits': PLANTED_READOUT, 'field_coefficients': list(planted_coeffs),
               'solutions': count_a}

    # Control 3: brute force under restricted features, on the real table and,
    # so that nonzero readout counts are compared, on a planted synthetic table.
    brute = []
    for label, base, chosen, plant_coeffs in (('real', table, (0, 1), None),
                                              ('real', table, (0, 1, 4), None),
                                              ('planted', table, (0, 1, 4), (5, 3, 6, 1, 7, 2))):
        rf = features(chosen)
        tab = plant(base, plant_coeffs, rf) if plant_coeffs else base
        qq = kernel_from_table(tab)
        bf_counts, bf_distinct = brute_force(qq, chosen)
        ra, rb = SolverA(rf, group=2), SolverB(rf)
        need(len(rb.basis) == len(chosen), 'restricted rank')
        ca = [ra.run(readout_sets(qq, d)) for d in READOUTS]
        cb = [rb.run(readout_sets(qq, d)) for d in READOUTS]
        need(ca == bf_counts and cb == bf_counts, 'brute force per-readout counts %s %s' % (label, chosen))
        dg = distinct_sets(qq)
        need(ra.run(dg) == bf_distinct and rb.run(dg) == bf_distinct,
             'brute force diagnostic %s %s' % (label, chosen))
        if plant_coeffs:
            need(sum(bf_counts) > 0, 'planted brute force is nonvacuous')
        brute.append({'table': label, 'features': [FEATURE_NAMES[f] for f in chosen],
                      'maps': 64 ** len(chosen),
                      'readouts_with_solutions': sum(1 for c in bf_counts if c),
                      'total_readout_solutions': sum(bf_counts), 'known_seed_readout_maps': bf_distinct})

    # Control 4: singleton partial readouts reproduce the retained raw-pair decision.
    author = {tuple(p['raw_pair']): p for p in route['controller']['per_pair_affine_results']}
    need(len(author) == 32, 'author pair list')
    e_total = joint_total = 0
    for o0, o1 in product(range(8), repeat=2):
        if o0 == o1:
            continue
        joint = sa_e.run(pair_sets(q, o0, o1))
        ref = author.get((o0, o1))
        need(sa_e.prefix3 == (ref['affine_E_maps_after_constraints'] if ref else 0),
             'E prefix count %d%d' % (o0, o1))
        need(joint == (ref['joint_affine_E_N_maps'] if ref else 0), 'joint raw-pair count %d%d' % (o0, o1))
        need(sa.run(pair_sets(q, o0, o1)) == joint and sb.run(pair_sets(q, o0, o1)) == joint,
             'raw-pair joint count agreement %d%d' % (o0, o1))
        e_total += sa_e.prefix3
        joint_total += joint
    need(e_total == 16 and joint_total == 0, 'retained raw-pair totals')

    # Control 5: sign-erased countercontrol.
    erased = [q[0], q[0]]
    need(all(sa.run(readout_sets(erased, d)) == 0 for d in READOUTS), 'erased readouts A')
    need(all(sb.run(readout_sets(erased, d)) == 0 for d in READOUTS), 'erased readouts B')
    need(sa.run(distinct_sets(erased), stop_first=True) == 0, 'erased diagnostic A')
    need(sb.run(distinct_sets(erased), stop_first=True) == 0, 'erased diagnostic B')

    # Primary decision and control 6: complete solution sets must agree, and
    # every solution is checked directly against the native table.
    per_readout = []
    witnesses = []
    every = []
    for d in READOUTS:
        g = readout_sets(q, d)
        ca = sa.run(g, collect=1 << 20)
        sols = sorted(sa.found)
        cb = sb.run(g, collect=1 << 20)
        need(ca == cb == len(sols), 'solver count agreement readout %d' % d)
        need({basis_values(c, sb, feats) for c in sols} == set(sb.found),
             'solver solution-set agreement readout %d' % d)
        for c in sols:
            for j, k in enumerate(CONTEXTS):
                w = evaluate(c, feats[j])
                for s in (0, 1):
                    need((d >> table[row_index(s ^ k[0] ^ k[3], k, w >> 3, w & 7)]) & 1 == s,
                         'solution direct table check')
            every.append((d, c))
        per_readout.append(ca)
        if ca:
            witnesses.append({'readout_bits': d, 'solutions': ca, 'ones': d.bit_count(),
                              'anf_degree': anf_degree(d),
                              'first_field_coefficients_EA_EB_ED_NA_NB_ND': list(sols[0])})

    dg = distinct_sets(q)
    diag_a = sa.run(dg, collect=1, stop_first=True)
    diag_wit = sa.found[0] if sa.found else None
    diag_b = sb.run(dg, stop_first=True)
    need(bool(diag_a) == bool(diag_b), 'solver agreement diagnostic')
    diagnostic = {'exists': bool(diag_a)}
    if diag_a:
        rows = []
        for j, k in enumerate(CONTEXTS):
            w = evaluate(diag_wit, feats[j])
            r = [table[row_index(s ^ k[0] ^ k[3], k, w >> 3, w & 7)] for s in (0, 1)]
            need(r[0] != r[1], 'diagnostic witness direct table check')
            rows.append(r)
        diagnostic['field_coefficients_EA_EB_ED_NA_NB_ND'] = list(diag_wit)
        diagnostic['raw_codes_s0_s1_per_context'] = rows
        diagnostic['distinct_raw_pairs_used'] = len({tuple(r) for r in rows})

    structure = solution_structure(every, table, feats)
    linear_readouts = affine_readouts(every, table, feats)
    fresh_pairs = fresh_bit_pairs(every, table, feats)
    positive = witnesses
    verdict = ('fixed redundant q10 readout with jointly affine E,N exists in this geometry'
               if positive else
               'no fixed q10 readout, redundant or not, decodes s under jointly affine E,N in this geometry')
    result = {
        'schema': 'oi.native-redundant-q10-readout.v14',
        'plan_base': PIN_PLAN_BASE,
        'inputs': {'native_route_v13/result.json': PIN_ROUTE_RESULT,
                   'native_route_v13/review/result.json': PIN_REVIEW_RESULT,
                   'q10_table_sha256': PIN_TABLE, 'review_table_sha256_agrees': True},
        'contexts_u_mY_mR_a_b': [list(k) for k in CONTEXTS],
        'feature_order': list(FEATURE_NAMES),
        'source_field_order': 'w=8*Ecode+Ncode; fields EA,EB,ED,NA,NB,ND are bits 5..0 of w',
        'readout_encoding': 'bit c of readout_bits is the readout of raw code c=4A+2B+D',
        'controls': {
            'input_pins': 5,
            'solution_sets_compared_and_table_checked': 'all readouts, both solvers',
            'planted_positive': planted,
            'restricted_brute_force': brute,
            'raw_pair_reproduction': {'ordered_pairs': 56, 'affine_E_prefixes': e_total,
                                      'joint_maps': joint_total},
            'sign_erased_countercontrol': 'zero for all 254 readouts and the diagnostic, both solvers',
            'solver_agreement_readouts': len(READOUTS),
        },
        'affine_maps_per_readout': 2 ** 36,
        'readout_solution_counts': per_readout,
        'readouts_with_solutions': len(positive),
        'total_readout_solutions': sum(per_readout),
        'positive_readouts': positive,
        'post_hoc_solution_structure': structure,
        'post_hoc_degree_one_readouts': linear_readouts,
        'post_hoc_fresh_bit_on_q10A': fresh_pairs,
        'known_seed_readout_diagnostic': diagnostic,
        'verdict': {
            'fixed_q10_readout': verdict,
            'single_raw_field_readouts': ['q10.%s%s under %d jointly affine laws' % (
                r['raw_fields_xored'][0], ' complemented' if r['complemented'] else '', r['solutions'])
                for r in linear_readouts if len(r['raw_fields_xored']) == 1] or 'none',
            'second_front_required': ('every solution has nonzero E' if not structure['E_identically_000']
                                      else 'some solution has E identically 000'),
            'known_seed_dependent_readout': ('exists (not a fixed-readout delivery)' if diag_a
                                             else 'none under jointly affine E,N'),
            'downstream_native_gate_on_readout_classes': 'not tested',
            'acceptance_predicate': 'not constructed',
            'other_layouts_fresh_seed_multicell_readouts': 'not tested',
        },
    }
    print(json.dumps(result, sort_keys=True, separators=(',', ':')))


if __name__ == '__main__':
    main()
