"""Export the complete (all valid label matchings) membership conditions for the 20 Dita structures of SIG: the 18
census structures of acts 36-38 and the fifth 4x4 index structure k5 in both forms (fifth.py). Writes data41c.bin and
structures20.json. Format per rel in (strict, relaxed), per structure: nprop, prop eqs; ngroups-1; per group b: nvalid;
per valid s_b: neq, eqs. Each eq: nterms, (var, coef)*."""
import struct, json, hashlib
from lib41 import *
from matchlib import *
def mdiv(x, y): return ((x[0] - y[0]) % 4, x[1] - y[1], x[2] - y[2])
S = json.load(open('matchings.json'))
f5 = json.load(open('fifth.json'))
structs = [S[k] for k in S]                  # 18, in CENSUS9 x (column, row) order
for rec in f5:
    tr = rec['form'] == 'row'
    blocks = [tuple(b) for b in rec['blocks']]; groups = [tuple(g) for g in rec['groups']]
    H = (lambda i, j: SIGE[j][i]) if tr else (lambda i, j: SIGE[i][j])
    structs.append({'name': 'k5', 'form': rec['form'], 'shape': [4, 4], 'blocks': blocks, 'groups': groups, 'transpose': tr,
                    'strict': valid_per_group(H, blocks, groups, False, mdiv), 'relaxed': valid_per_group(H, blocks, groups, True, mdiv)})
assert len(structs) == 20
def eqbytes(e):
    items = sorted(e.items()); return struct.pack('<i', len(items)) + b''.join(struct.pack('<ii', k, c) for k, c in items)
out = bytearray(struct.pack('<i', len(structs)))
for rel in (False, True):
    for st in structs:
        P = prop_eqs(st['blocks'], st['groups'], st['transpose'])
        out += struct.pack('<i', len(P)) + b''.join(eqbytes(e) for e in P)
        V = st['relaxed' if rel else 'strict']; n = len(st['groups'])
        out += struct.pack('<i', n - 1)
        for b in range(1, n):
            out += struct.pack('<i', len(V[b]))
            for sb in V[b]:
                L = lam_eqs(st['blocks'], st['groups'], b, tuple(sb), rel, st['transpose'])
                out += struct.pack('<i', len(L)) + b''.join(eqbytes(e) for e in L)
open('data41c.bin', 'wb').write(out)
names = ['%s-%s' % (st['name'], st['form']) for st in structs]
json.dump({'names': names, 'structures': structs, 'sha256': hashlib.sha256(out).hexdigest()}, open('structures20.json', 'w'), default=list)
print('structures', names); print('bytes', len(out))
