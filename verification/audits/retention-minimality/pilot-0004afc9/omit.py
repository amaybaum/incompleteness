#!/usr/bin/env python3
"""omit.py -- apply one omission variant to a disposable clone of main (never to a shared or real checkout).

Usage: python3 -I -B omit.py <clone-root> <oid> <variant>

  N1  delete the object's stored file only;
  N2  N1, and delete the object's entry from objects/manifest.json;
  N3  N2, and record the new objects/manifest.json size and sha256 in the evidence manifest (manifest.json),
      i.e. a coordinated omission that also updates the archive's manifest pin. The checkers are never edited.

Each manifest is rewritten only after checking that its serialization round-trips byte-for-byte, so the edit
is exactly the stated removal or pin update.
"""
import hashlib
import json
import os
import sys

root, oid, variant = sys.argv[1], sys.argv[2], sys.argv[3]
assert variant in ('N1', 'N2', 'N3')
A = os.path.join(root, 'verification', 'audits', 'evidence-retention')
OM = os.path.join(A, 'objects', 'manifest.json')
EM = os.path.join(A, 'manifest.json')


def dump(obj):
    return (json.dumps(obj, indent=1, sort_keys=True, ensure_ascii=False) + '\n').encode()


ob = open(OM, 'rb').read()
om = json.loads(ob)
assert dump(om) == ob, 'object manifest does not round-trip'
(entry,) = [e for e in om['objects'] if e['oid'] == oid]
path = os.path.join(A, 'objects', entry['file'])
os.remove(path)
print('removed file', os.path.relpath(path, root))
if variant in ('N2', 'N3'):
    om['objects'] = [e for e in om['objects'] if e['oid'] != oid]
    nb = dump(om)
    open(OM, 'wb').write(nb)
    print('removed manifest entry', oid, '; objects/manifest.json now', len(nb), 'bytes',
          hashlib.sha256(nb).hexdigest())
if variant == 'N3':
    eb = open(EM, 'rb').read()
    em = json.loads(eb)
    assert dump(em) == eb, 'evidence manifest does not round-trip'
    n = 0
    for x in em['entries']:
        for f in x['files']:
            if f['path'] == 'objects/manifest.json':
                f['bytes'] = len(nb)
                f['sha256'] = hashlib.sha256(nb).hexdigest()
                n += 1
    assert n == 1, n
    open(EM, 'wb').write(dump(em))
    print('updated the evidence manifest pin of objects/manifest.json')
