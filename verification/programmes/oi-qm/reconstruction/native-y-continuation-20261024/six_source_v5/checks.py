"""Bounded solver replay, exact controls, and scoped endpoint classification."""
from pathlib import Path
from functools import lru_cache
import json
import subprocess
import tempfile
from model import result, need, xor, h, lane, VARIABLES, native_second, R, ball

HERE = Path(__file__).resolve().parent
STEPS = tuple(tuple(sign if j == axis else 0 for j in range(3))
              for axis in range(3) for sign in (-1, 1))


def add(p, q):
    return tuple(a+b for a, b in zip(p, q))


def check_small(rows, T, d):
    variables = [sum(((j >> i) & 1) << j for j in range(64)) for i in range(6)]
    sources = {(0, 0, 0): (0, variables[0], 0),
               (0, -2, 0): tuple(variables[1:4]),
               (0, 2*T, 0): (0, variables[4] ^ variables[5], 0),
               (T, T, 0): (0, variables[4], 0),
               (-T, T, 0): (0, variables[5], 0)}

    @lru_cache(None)
    def direct(t, v):
        if t < 0 or all(sum(abs(a-b) for a, b in zip(v, s)) > t for s in sources):
            return (0, 0, 0)
        if t == 0:
            return sources.get(v, (0, 0, 0))
        return xor(direct(t-2, v), h(xor(*(direct(t-1, add(v, e)) for e in STEPS))))

    need(len(rows) == 192, 'small complete slice count')
    for tau, p, encoded in rows:
        need(tuple(int(v, 16) for v in encoded) ==
             direct(T+d+tau, (p[0], T+p[1], d+p[2])), 'independent small lower dynamics')


with tempfile.TemporaryDirectory(prefix='six-source-check-') as directory:
    executable = str(Path(directory) / 'lower')
    compiled = subprocess.run(['g++', '-std=c++17', '-O2', '-Wall', '-Wextra', '-Werror',
                               '-pedantic', str(HERE / 'lower.cpp'), '-o', executable],
                              capture_output=True, timeout=30)
    need(compiled.returncode == 0, 'C++ compilation: ' + compiled.stderr.decode(errors='replace'))
    computed = subprocess.run([executable], capture_output=True, timeout=30)
    need(computed.returncode == 0, 'lower solver: ' + computed.stderr.decode(errors='replace'))
    need(computed.stdout == (HERE / 'lower-slices.json').read_bytes(), 'actual lower-slice bytes')
    rows = json.loads(computed.stdout)
    for T, d in ((8, 2), (11, 3)):
        small = subprocess.run([executable, '--small', str(T), str(d)], capture_output=True, timeout=30)
        need(small.returncode == 0, 'small solver exit')
        check_small(json.loads(small.stdout), T, d)
print('S1: exact reduced lower solver reproduces192 rows; independent direct controls384 rows x64 assignments: PASS')

# Verify the large-coordinate parity reduction separately using full Python integers.
T = 185
P = 12 * 840 ** T
S = T + P
controls = ((0, 2*S, 0), (T, P+S, 0), (-T, P+S, 0))
center = (0, S-1, 70)
count = 0
for dx, dy, dz in ball(72, (0, 0, 0)):
    j = dy-1
    z = 70+dz
    v = (dx, S+j, z)
    for k, c in enumerate(controls):
        parts = tuple(abs(a-b) for a, b in zip(v, c))
        need(sum(parts) >= S-1, 'control cannot be behind front')
        if sum(parts) == S-1:
            exact = not (parts[0] & parts[1] or parts[0] & parts[2] or parts[1] & parts[2])
            low_y = (T-j) if k == 0 else ((-j) & 1023)
            reduced = not (parts[0] & low_y or parts[0] & parts[2] or low_y & parts[2])
            need(exact == reduced, 'actual giant no-carry parity')
            need(parts[0] < 1024 and parts[2] < 1024 and P % 1024 == 0, 'low-bit sufficiency')
            count += 1
print('S2: actual giant-coordinate control parity matches low-bit reduction on%d boundary contributions: PASS' % count)

data, records = result(rows)
need(data == json.loads((HERE / 'RESULT.json').read_text()), 'complete truth table / ANF / distribution changed')
for j in range(256):
    x, my, mr, u, p = ((j >> i) & 1 for i in (0, 4, 5, 6, 7))
    expected, _ = native_second(T, P, 68, x, my, mr, u, p)
    need(lane(records[2][(0, 0, 2)], j) == expected, 'retained q2 diagnostic changed')
need(records[2][(0, 0, 2)][0] == VARIABLES[7], 'positive control must recognize raw p at q2')
print('S3: upper/lower assembly preserves qY, sidecar and all256 q2 diagnostic assignments; positive raw-p control: PASS')

table = data['diagnostic_table']
need(data['raw_p_fields_or_complements'] == [], 'endpoint classification changed')
need(data['fixed_background_p_pairs_distinct'], 'fixed-background diagnostic information changed')
for first, second, code in data['native_overlap_witnesses']:
    need((first & 1) == (second & 1), 'witness x must agree')
    for j in (first, second):
        need(((j >> 7) & 1) == ((j & 1) ^ ((j >> 6) & 1)), 'witness must be native')
    need(((first >> 7) & 1) != ((second >> 7) & 1), 'witness Y must differ')
    need(table[first] == table[second] == code, 'native overlap')
for counts in data['native_counts_per_32_by_xu'].values():
    need(sum(counts) == 32, 'all masks/M2 retained')
print('S4: exact128 native cases; opposite-Y supports overlap at fixed x; no raw-p field; all128 fixed-background diagnostic pairs remain distinct: PASS')
print('VERDICT: this prepared junction is not a clean Y transfer; history-aware decoding, other apparatuses and integrated reset remain OPEN.')
