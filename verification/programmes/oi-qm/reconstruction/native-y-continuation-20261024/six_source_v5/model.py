"""Assemble all 256 diagnostic assignments from exact lower slices and upper pulse."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'parallel_v3/new_geometry'))
from third_step import upper, R
from inherited_core import ball, native_second

NAMES = ['x', 'mA', 'mB', 'mD', 'mY', 'mR', 'u', 'p']
ALL = (1 << 256) - 1
VARIABLES = [sum(((j >> i) & 1) << j for j in range(256)) for i in range(8)]
NATIVE_Y = VARIABLES[0] ^ VARIABLES[6]


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def xor(*values):
    result = [0, 0, 0]
    for value in values:
        for i in range(3):
            result[i] ^= value[i]
    return tuple(result)


def h(v):
    a, b, d = v
    return b, d, a ^ (b & d)


def replicate64(v):
    return v | (v << 64) | (v << 128) | (v << 192)


def assemble(rows):
    pre = {-2: {}, -1: {}}
    for tau, position, low in rows:
        v = tuple(position)
        need(tau in pre and v not in pre[tau], 'duplicate or invalid slice row')
        pulses = [upper((u, 0, 1), R+tau, (v[0], v[1], R-v[2])) for u in (0, 1)]
        up = tuple((ALL if pulses[0][i] else 0) ^
                   (VARIABLES[6] if pulses[0][i] ^ pulses[1][i] else 0)
                   for i in range(3))
        pre[tau][v] = xor(tuple(replicate64(int(a, 16)) for a in low), up)
    for tau, radius in ((-2, 3), (-1, 4)):
        need(set(pre[tau]) == set(ball(radius, (0, -1, 2))), 'slice coverage')
    old, now = pre[-2], pre[-1]
    records = {}
    for tau in range(4):
        nxt = {}
        for v in ball(3-tau, (0, -1, 2)):
            neighbors = []
            for axis in range(3):
                for sign in (-1, 1):
                    w = list(v)
                    w[axis] += sign
                    neighbors.append(now[tuple(w)])
            nxt[v] = xor(old[v], h(xor(*neighbors)))
        if tau == 0:
            need(nxt[(0, 0, 0)] == (VARIABLES[0], ALL, NATIVE_Y),
                 'inherited qY changed under proposed extension')
            # Diagnostic only: native cases are selected by p=x XOR u below.
            nxt[(0, 0, 0)] = (VARIABLES[0], ALL, VARIABLES[7])
        records[tau] = nxt
        old, now = now, nxt
    need(records[1][(0, -1, 2)] == (0, ALL ^ NATIVE_Y, VARIABLES[0]),
         'inherited sidecar changed')
    return now[(0, -1, 2)], records


def lane(value, index):
    return tuple((word >> index) & 1 for word in value)


def anf(word):
    coefficients = [(word >> j) & 1 for j in range(256)]
    for i in range(8):
        for j in range(256):
            if j >> i & 1:
                coefficients[j] ^= coefficients[j ^ (1 << i)]
    return [j for j, value in enumerate(coefficients) if value]


def result(rows):
    out, records = assemble(rows)
    table = [sum(bit << (2-i) for i, bit in enumerate(lane(out, j))) for j in range(256)]
    counts = {}
    for x in (0, 1):
        for u in (0, 1):
            selected = [j for j in range(256) if (j & 1) == x and
                        ((j >> 6) & 1) == u and ((j >> 7) & 1) == (x ^ u)]
            counts[str(x)+str(u)] = [sum(table[j] == code for j in selected) for code in range(8)]
    raw = [field for field in range(3) if out[field] in (VARIABLES[7], VARIABLES[7] ^ ALL)]
    return {'variables_lsb_first': NAMES, 'output_code': '4*A+2*B+D',
            'diagnostic_table': table, 'output_anf': [anf(word) for word in out],
            'native_counts_per_32_by_xu': counts,
            'raw_p_fields_or_complements': raw,
            'fixed_background_p_pairs_distinct': all(table[j] != table[j | 128] for j in range(128)),
            'native_overlap_witnesses': [[0, 216, table[0]], [129, 87, table[129]]]}, records
