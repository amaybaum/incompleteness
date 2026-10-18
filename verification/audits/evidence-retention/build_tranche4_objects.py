#!/usr/bin/env python3
"""build_tranche4_objects.py -- how archive tranche 4 of the retained off-main objects was cut (AGENTS §A.42).

By the owner's instructions of 2026-10-17 it retains, in the form of archive tranche 2, four commits that main does
not reach and that records not yet on main cite:
  - #831's research sources e684897d and febfe5e2 (runs 38450187534 and 38454439833), as raw:partial-tree commits.
    Each tree holds two non-empty captured outputs, exact-output.txt and independent-output.txt, which the owner
    approved for withholding on 2026-10-17 for exactly these paths and commits; they are named by id, size and
    sha256, and the values they carry are recorded as structured expected results with the recipe that regenerates
    them;
  - #829's KTOKEN-MAXCONE-1 design-run heads 1ab0fd9d (dev-equivalence/ktoken-maxcone) and 6959ced4
    (dev-equivalence/ktoken-maxcone-r2), as raw:tree commits; their trees hold no captured raw output.
Each commit is stored with every tree and blob that main (at the tranche's base, b96662e6) lacks, except its
withheld blobs; its parent, off main, is named and not retained. No ref, branch or remote is changed.

It reads the objects from a local clone that holds them; nothing it reads is retained beyond the objects
themselves. Usage: build_tranche4_objects.py REPO ARCHIVE
"""
import hashlib
import json
import os
import subprocess
import sys
import zlib

REPO, ARCH = sys.argv[1:3]
OBJ = os.path.join(ARCH, 'objects')
BASE4 = 'b96662e6be4f537502c772db369ea32a35b213a8'
DESIGN = 'verification/programmes/oi-qm/reconstruction/preservation-induction-design/'
P831 = 'verification/programmes/oi-qm/reconstruction/round-preserve-induct-1/preregistration.md'
P829 = 'verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/preregistration.md'
COMMITS = {
    'e684897da41b1c3d066b880194c9beb87a19b7ad': {
        'mechanism': 'raw:partial-tree', 'branch': 'research/preservation-induction-design-20261013',
        'awaiting_citation': {'pull_request': 831, 'round': 'PRESERVE-INDUCT-1', 'record': P831,
                              'run': '38450187534',
                              'note': 'the source commit of research run 38450187534, which the record is to cite '
                                      'beside the run'}},
    'febfe5e2668d3c000ec1d4ce7e4041f4feabd3c3': {
        'mechanism': 'raw:partial-tree', 'branch': 'research/preservation-induction-design-20261013',
        'awaiting_citation': {'pull_request': 831, 'round': 'PRESERVE-INDUCT-1', 'record': P831,
                              'run': '38454439833',
                              'note': 'the source commit of research run 38454439833, which the record is to cite '
                                      'beside the run'}},
    '1ab0fd9dd2c6701197f2e0ab18401cafb76a090d': {
        'mechanism': 'raw:tree', 'branch': 'dev-equivalence/ktoken-maxcone',
        'awaiting_citation': {'pull_request': 829, 'round': 'KTOKEN-MAXCONE-1', 'record': P829,
                              'run': '39043849411',
                              'note': 'the head of KTOKEN-MAXCONE-1\'s design run 1, run 39043849411, which the record '
                                      'is to cite beside the run'}},
    '6959ced4c327ebb800cf6d463a049e4066e37288': {
        'mechanism': 'raw:tree', 'branch': 'dev-equivalence/ktoken-maxcone-r2',
        'awaiting_citation': {'pull_request': 829, 'round': 'KTOKEN-MAXCONE-1', 'record': P829,
                              'run': '39056982958',
                              'note': 'the head of KTOKEN-MAXCONE-1\'s design run 2, run 39056982958, which the record '
                                      'is to cite beside the run'}},
}
WITHHOLD = {
    'c697b82b8a7d6719d78dfc74bc8183c85fa12255': {
        'path': DESIGN + 'exact-output.txt',
        'carries': {'sample_manifest_sha256': 'a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9',
                    'exact_controls': 107, 'mutations_rejected': 7,
                    'checked': 'finite constructor examples and named countercontrols only'},
        'lines': ['SAMPLE-MANIFEST-SHA256 a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9',
                  'EXACT-CONTROLS 107', 'MUTATIONS-REJECTED 7',
                  'CHECKED: finite constructor examples and named countercontrols only'],
        'script': DESIGN + 'exact_check.py', 'requires': 'sympy 1.14.0, which the workflow installs'},
    '8cdf3a83f78059d81a701c2e4951e54f3a2b06bd': {
        'path': DESIGN + 'independent-output.txt',
        'carries': {'sample_manifest_sha256': 'a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9',
                    'independent_controls': 43, 'checked': 'rational Kraus-path calculation, finite examples only'},
        'lines': ['SAMPLE-MANIFEST-SHA256 a1f82e289ba07a4c60dd6b56396dcdf7c0c217b2ff49a8d779f1c4e923842ea9',
                  'INDEPENDENT-CONTROLS 43', 'CHECKED: rational Kraus-path calculation, finite examples only'],
        'script': DESIGN + 'independent_check.py', 'requires': 'the standard library'},
}
REASON = ('a non-empty captured raw output of a computation (AGENTS §A.42 item 1); its withholding at exactly this path in '
          'these two commits was approved by the owner on 2026-10-17')


def git(*a, inp=None):
    return subprocess.run(['git', '-C', REPO] + list(a), input=inp, capture_output=True, check=True).stdout


def sha(b):
    return hashlib.sha256(b).hexdigest()


main_objs = set(git('rev-list', '--objects', BASE4).decode().split('\n'))
main_objs = {l.split()[0] for l in main_objs if l}
man_path = os.path.join(OBJ, 'manifest.json')
man = json.load(open(man_path, encoding='utf-8'))
man['objects'] = [e for e in man['objects'] if e.get('tranche') != 4]
have = {e['oid'] for e in man['objects']}
new, needed = {}, {}
for c, spec in COMMITS.items():
    body = git('cat-file', 'commit', c)
    head = body.split(b'\n\n', 1)[0].decode().split('\n')
    tree = head[0][5:]
    parents = [l[7:] for l in head if l.startswith('parent ')]
    assert all(p not in main_objs for p in parents) and c not in main_objs and c not in have
    listing = git('ls-tree', '-r', '-t', '-z', c).decode('utf-8', 'surrogateescape').split('\0')
    items = [(tree, 'tree', '/')]
    for l in listing:
        if not l:
            continue
        meta, path = l.split('\t', 1)
        mode, typ, oid = meta.split()
        if typ == 'commit':
            continue
        items.append((oid, typ, path + '/' if typ == 'tree' else path))
    withheld = sorted(o for o, t, p in items if o in WITHHOLD)
    assert (spec['mechanism'] == 'raw:partial-tree') == bool(withheld)
    for oid, typ, path in items:
        if oid in main_objs or oid in WITHHOLD:
            continue
        needed.setdefault(oid, []).append({'object': c, 'path': path})
        if oid in have or oid in new:
            continue
        content = git('cat-file', typ, oid)
        data = zlib.compress(typ.encode() + b' %d\0' % len(content) + content, 9)
        rel = 'loose/%s/%s' % (oid[:2], oid[2:])
        os.makedirs(os.path.join(OBJ, os.path.dirname(rel)), exist_ok=True)
        open(os.path.join(OBJ, rel), 'wb').write(data)
        new[oid] = {'oid': oid, 'type': typ, 'mechanism': 'raw' if typ == 'tree' else 'byte-copy', 'form': 'zlib',
                    'file': rel, 'bytes': len(data), 'sha256': sha(data), 'content_bytes': len(content),
                    'content_sha256': sha(content), 'tranche': 4}
    rel = 'commit/%s/%s' % (c[:2], c)
    os.makedirs(os.path.join(OBJ, os.path.dirname(rel)), exist_ok=True)
    open(os.path.join(OBJ, rel), 'wb').write(body)
    e = {'oid': c, 'type': 'commit', 'mechanism': spec['mechanism'], 'form': 'raw', 'file': rel, 'bytes': len(body),
         'sha256': sha(body), 'content_bytes': len(body), 'content_sha256': sha(body), 'parents': parents,
         'parents_not_retained': parents, 'awaiting_citation': spec['awaiting_citation'],
         'held_by': {'branch': spec['branch'], 'listed_at': '2026-10-17'}, 'tranche': 4}
    if withheld:
        e['withheld_blobs'] = withheld
    new[c] = e
for oid, e in new.items():
    if e['type'] != 'commit':
        e['needed_by'] = sorted(needed[oid], key=lambda n: (n['object'], n['path']))
for w, spec in WITHHOLD.items():
    content = git('cat-file', 'blob', w)
    assert content.decode().rstrip('\n').split('\n') == spec['lines'], w
    occ = sorted((c, spec['path']) for c in COMMITS if w in new[c].get('withheld_blobs', []))
    assert git('rev-parse', '%s:%s' % (occ[0][0], spec['path'])).decode().strip() == w
    new[w] = {'oid': w, 'type': 'blob', 'mechanism': 'withheld:raw-output', 'bytes': len(content),
              'content_sha256': sha(content), 'paths': [spec['path']],
              'needed_by': [{'object': c, 'path': p} for c, p in occ],
              'instances': [{'commit': c, 'path': p, 'bytes': len(content), 'blob': w, 'sha256': sha(content),
                             'reason': REASON} for c, p in occ],
              'carries': spec['carries'],
              'reproduce': {'recipe': ['git show <commit>:%s > <dir>/check.py (the commit is retained here; '
                                       'check_objects.py --materialize writes it into a clone)' % spec['script'],
                                       'python3 -I -B <dir>/check.py > <out>; requires %s' % spec['requires'],
                                       'the exit code is 0, nothing is written to stderr, and the sha256 of <out> is '
                                       'content_sha256'],
                            'note': 'carries holds the values the output states, read from its bytes; the recipe '
                                    'regenerates the output byte for byte'},
              'tranche': 4}
man['objects'] += [new[k] for k in sorted(new)]
man['tranche_bases'] = {'4': BASE4}
man['tranche4'] = {
    'base': BASE4,
    'scope': 'archive tranche 4: #831\'s research sources e684897d and febfe5e2 and #829\'s KTOKEN-MAXCONE-1 design-run '
             'heads 1ab0fd9d and 6959ced4, which records not yet on main cite or are to cite; each commit with every tree '
             'and blob main lacks at this base, its off-main parent named, not retained; two captured outputs withheld '
             'as approved',
    'host_state': {'branches': {'research/preservation-induction-design-20261013': '468e0f79cabb01c215a252721ee65a1ad1301a2f',
                                'dev-equivalence/ktoken-maxcone': '1ab0fd9dd2c6701197f2e0ab18401cafb76a090d',
                                'dev-equivalence/ktoken-maxcone-r2': '6959ced4c327ebb800cf6d463a049e4066e37288'},
                   'listed_at': '2026-10-17'}}
open(man_path, 'w', encoding='utf-8').write(json.dumps(man, indent=1, sort_keys=True, ensure_ascii=False) + '\n')
by = {}
for e in new.values():
    by[e['mechanism']] = by.get(e['mechanism'], 0) + 1
print('tranche 4: %d entries %s; files %d, %d bytes' % (len(new), by, sum(1 for e in new.values() if e.get('file')),
                                                        sum(e.get('bytes', 0) for e in new.values() if e.get('file'))))
