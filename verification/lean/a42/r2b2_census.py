"""R2 path B(ii): L41's landed independent probe, executed whole (it replays L41's measurements.json: C0), then its
a41_census at exact points of E40's arc. Writes r2b2.json."""
import contextlib, io, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
PROBE = os.path.join(REPO, 'verification', 'lean', 'dita_index_map_independent.py')
t0 = time.time(); NS = {'__name__': 'landed_independent', '__file__': PROBE}; buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf): exec(compile(open(PROBE, encoding='utf-8').read(), PROBE, 'exec'), NS)
    code = 0
except SystemExit as e: code = e.code
last = [l for l in buf.getvalue().splitlines() if l.startswith('dita_index_map_independent:')]
C0 = code in (0, None) and len(last) == 1 and ' OK -- REPLAYED' in last[0]
print('C0 landed independent probe:', last, 'exit', code, '(%.0fs)' % (time.time() - t0), flush=True)
G, Fr, ONE, SIG, gpow, census = NS['G'], NS['Fr'], NS['ONE'], NS['SIG'], NS['gpow'], NS['a41_census']
def E40_entry(i, j):
    a, b, c, d = i // 4, i % 4, j // 4, j % 4
    return -int(b == 0 and c == 0) + int(a == 2 and b % 2 == 1 and d % 2 == 0) - int(a % 2 == 0 and c % 2 == 1 and d == 0)
E40 = [[E40_entry(i, j) for j in range(16)] for i in range(16)]
def H(u): return [[SIG[i][j] * gpow(u, E40[i][j]) for j in range(16)] for i in range(16)]
pts = [('u = 1', ONE), ('u = -1', G(-1)), ('u = (3+4i)/5', G(Fr(3, 5), Fr(4, 5))), ('u = (5+12i)/13', G(Fr(5, 13), Fr(12, 13))),
       ('u = (8+15i)/17', G(Fr(8, 17), Fr(15, 17))), ('u = i', G(0, 1))]
out = {'C0': C0, 'last': last, 'points': {}}
for nm, u in pts:
    t = time.time(); r = census(H(u))
    out['points'][nm] = {n: {'partitions': len(r[n]), 'alignments': sum(x[4] for x in r[n]), 'census': r[n]} for n in ('strict', 'relaxed')}
    print('  %-16s strict %2d (%4d)  relaxed %2d (%4d)  (%.0fs)' % (nm, len(r['strict']), sum(x[4] for x in r['strict']), len(r['relaxed']), sum(x[4] for x in r['relaxed']), time.time() - t), flush=True)
json.dump(out, open(os.path.join(HERE, 'r2b2.json'), 'w'), indent=1, sort_keys=True)
