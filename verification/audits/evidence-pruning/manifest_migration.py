#!/usr/bin/env python3
"""manifest_migration.py - the evidence-retention manifest edit that accompanies the builder removal (LEDGER.md).

The edit is computed from the frozen manifest at BASE, never from the working tree, and is checked byte for byte:

    python3 -I verification/audits/evidence-pruning/manifest_migration.py           # print the migrated manifest's digest
    python3 -I verification/audits/evidence-pruning/manifest_migration.py --check   # exit 0 only when the tree's manifest
                                                                                 # is exactly the migration of BASE's
    python3 -I verification/audits/evidence-pruning/manifest_migration.py --write   # write the migrated manifest

The migration removes the manifest records of the four one-shot builders and nothing else:
  - the entries research-runs-record, tranche4-record and priority-runs-record, each of which lists only its builder;
  - build_tranche3.py from tranche3-record, whose provenance then names the files it keeps.
Each removed entry is `complete` and carries no citation, so no claim the manifest maps changes. Every other entry,
field and byte is unchanged; the serialization is the manifest's own (indent 1, sorted keys, UTF-8, final newline),
which reproduces the BASE manifest byte for byte before the edit.
"""
import hashlib
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
PATH = 'verification/audits/evidence-retention/manifest.json'
BASE = '55a0e80abc4b96e7bf211566a036ad17ea64a69e'
BASE_SHA256 = 'c5180e20e855a83c9ff63903fcbaba73fc7793bfaf0cd205b60ee498ebce46d8'
DROP_ENTRIES = {
    'research-runs-record': ['build_research_runs.py'],
    'tranche4-record': ['build_tranche4_objects.py'],
    'priority-runs-record': ['build_priority_runs.py'],
}
EDIT_ENTRY = 'tranche3-record'
DROP_FILE = 'build_tranche3.py'
KEEP_FILES = ['job_outputs.py']
OLD_SOURCE = ("written for this archive: tranche 3's extractor, reproduction tool and comparator, "
              "and the script that cut the tranche")
NEW_SOURCE = "written for this archive: tranche 3's extractor, reproduction tool and comparator"
REMOVED = sorted(sum(DROP_ENTRIES.values(), [DROP_FILE]))


def dump(m):
    return (json.dumps(m, indent=1, sort_keys=True, ensure_ascii=False) + '\n').encode('utf-8')


def migrate(raw):
    if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise SystemExit('base manifest digest differs from %s' % BASE_SHA256)
    m = json.loads(raw)
    if dump(m) != raw:
        raise SystemExit('the serialization does not reproduce the base manifest')
    ids = [e.get('id') for e in m['entries']]
    for eid, files in DROP_ENTRIES.items():
        e = m['entries'][ids.index(eid)]
        if [f['path'] for f in e['files']] != files or e.get('citations') or e.get('kind') != 'complete':
            raise SystemExit('%s is not the uncited single-builder entry expected' % eid)
    m['entries'] = [e for e in m['entries'] if e.get('id') not in DROP_ENTRIES]
    e = next(x for x in m['entries'] if x.get('id') == EDIT_ENTRY)
    if [f['path'] for f in e['files']] != KEEP_FILES + [DROP_FILE] or e.get('citations') or \
            e['provenance'].get('source') != OLD_SOURCE:
        raise SystemExit('%s is not as expected' % EDIT_ENTRY)
    e['files'] = [f for f in e['files'] if f['path'] != DROP_FILE]
    e['provenance']['source'] = NEW_SOURCE
    left = json.dumps(m)
    for rel in REMOVED:
        if rel in left:
            raise SystemExit('%s is still named in the migrated manifest' % rel)
    return dump(m)


def main(argv):
    raw = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (BASE, PATH)], capture_output=True, check=True).stdout
    new = migrate(raw)
    digest = hashlib.sha256(new).hexdigest()
    if argv == ['--write']:
        open(os.path.join(ROOT, PATH), 'wb').write(new)
    elif argv == ['--check']:
        have = open(os.path.join(ROOT, PATH), 'rb').read()
        ok = have == new
        print('manifest-migration: %s (migrated sha256 %s, tree sha256 %s)'
              % ('OK' if ok else 'FAIL', digest, hashlib.sha256(have).hexdigest()))
        return 0 if ok else 1
    elif argv:
        print(__doc__)
        return 2
    print('base %s -> migrated %s (%d -> %d bytes)' % (BASE_SHA256, digest, len(raw), len(new)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))
