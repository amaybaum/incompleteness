"""Export exact tables for the C enumerator: vanishing tables, group, H_dom, membership equations. Writes data41.bin
and data41.json (structure names, sha256 of the binary)."""
import struct, hashlib, json
from lib41 import *
out = bytearray()
# 1. vanishing tables for all ordered-unordered pairs i<i2 (0..15), 2^16 bytes each
for i in range(16):
    for i2 in range(i + 1, 16):
        out += vanishing_table(i, i2).tobytes()
# 2. group: 2048 elements, perm (256 uint16) + sign (int8 as int16)
for p, s in GROUP:
    out += struct.pack('<256H', *p) + struct.pack('<h', s)
# 3. membership equations: 18 structures x {strict, relaxed}: count, then per equation nterms + (idx, coef) pairs
names = []
for rel in (False, True):
    for nm, form, s, tr in STRUCTS18:
        eqs = EQS[(nm, form, rel)]
        out += struct.pack('<i', len(eqs))
        for eq in eqs:
            nz = [(t, c) for t, c in enumerate(eq) if c]
            out += struct.pack('<i', len(nz))
            for t, c in nz: out += struct.pack('<ii', t, c)
        if not rel: names.append('%s-%s' % (nm, form))
open('data41.bin', 'wb').write(out)
json.dump({'structures': names, 'sha256': hashlib.sha256(out).hexdigest(), 'bytes': len(out)}, open('data41.json', 'w'), indent=1)
print('wrote', len(out), 'bytes', hashlib.sha256(out).hexdigest())
# sizes
V0 = [None] + [vanishing_table(0, i) for i in range(1, 16)]
full = (1 << 16) - 1
sizes = []
for i in range(1, 16):
    ok = [m for m in range(1 << 16) if V0[i][m] and V0[i][full ^ m]]
    sizes.append(len(ok))
print('adm sizes rows 1..15:', sizes)
tot = sum(a * b for x, a in enumerate(sizes) for y, b in enumerate(sizes) if x != y)
print('ordered-pair compat bits', tot, 'MB', tot / 8 / 2 ** 20)
print('eq counts strict', [len(EQS[(nm, f, False)]) for nm, f, s, tr in STRUCTS18])
print('eq counts relaxed', [len(EQS[(nm, f, True)]) for nm, f, s, tr in STRUCTS18])
