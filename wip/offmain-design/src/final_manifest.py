"""Assemble the deliverable manifest.json: every object to preserve, with why, holder, mechanism and size, plus counts,
sizes, controls and what is unrecoverable. Reads work/*.json produced by the other scripts."""
import collections, datetime, json, os, subprocess, sys

O = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.dirname(O)
W = os.path.join(O, 'work')
G = ['git', '--git-dir', os.path.join(W, 'src.git')]
MAIN = '66a981d5a9cab35b9ebd253aa0e610c0afbfefb6'
st = json.load(open(os.path.join(W, 'layout-stage.json')))
D = st['deliv']
PL = json.load(open(os.path.join(W, 'plan.json')))
U = json.load(open(os.path.join(W, 'union-stage1.json')))['objects']
ext = json.load(open(os.path.join(W, 'extras.json')))


def run(*a, inp=None):
    return subprocess.run(G + list(a), input=inp, capture_output=True, text=True).stdout

# holding refs of the cited objects (host refs mirrored under refs/host/ at host-refs.time)
offrefs = [r for r in run('for-each-ref', '--format=%(refname)', 'refs/host/heads', 'refs/host/pull').split()
           if not r.endswith('/main') and subprocess.run(G + ['merge-base', '--is-ancestor', r, MAIN]).returncode]
cited_nc = {d['oid'] for d in D if d.get('cited') and d['type'] != 'commit'}
holds = collections.defaultdict(list)
for r in offrefs:
    objs = set(l.split()[0] for l in run('rev-list', '--objects', r, '--not', MAIN).split('\n') if l)
    for o in objs & cited_nc:
        holds[o].append(r.replace('refs/host/', ''))
for d in D:
    if d.get('cited') and d['type'] == 'commit' and d['holder']['state'] in ('branch', 'pull-ref'):
        refs = run('for-each-ref', '--contains', d['oid'], '--format=%(refname)', 'refs/host/heads', 'refs/host/pull').split()
        holds[d['oid']] = [r.replace('refs/host/', '') for r in refs]
for d in D:
    if d['oid'] in holds:
        h = sorted(holds[d['oid']])
        d['holder']['branches'] = [x[len('heads/'):] for x in h if x.startswith('heads/')]
        d['holder']['pull_refs'] = [x for x in h if x.startswith('pull/')]

C = collections.Counter
counts = {
    'objects': len(D),
    'cited': sum(1 for d in D if d.get('cited')),
    'dependencies': sum(1 for d in D if not d.get('cited')),
    'by_type': dict(C(d['type'] for d in D)),
    'by_mechanism': dict(sorted(C(d['mechanism'] for d in D).items())),
    'by_holder': dict(sorted(C(d['holder']['state'] for d in D).items())),
    'by_mechanism_and_holder': {m: dict(sorted(C(d['holder']['state'] for d in D if d['mechanism'] == m).items()))
                                for m in sorted({d['mechanism'] for d in D})},
    'cited_by_type_and_holder': {t: dict(sorted(C(d['holder']['state'] for d in D if d.get('cited') and d['type'] == t).items()))
                                 for t in ('commit', 'tree', 'blob')},
    'by_tranche': {str(t): {'objects': sum(1 for d in D if d['tranche'] == t),
                            'stored': sum(1 for d in D if d['tranche'] == t and d.get('file')),
                            'stored_bytes': sum(d.get('bytes', 0) for d in D if d['tranche'] == t and d.get('file')),
                            'content_bytes': sum(d.get('content_bytes', 0) for d in D if d['tranche'] == t and d.get('file'))}
                   for t in (1, 2, 3)},
    'inputs': dict(C(i for o in U.values() for i in o['inputs'])),
}
# input reconciliation: each input set is wholly in the manifest
inputs_check = {}
survey = json.load(open(os.path.join(S, 'agent-r2b', 'offmain-inventory.json')))['objects']
inv = json.load(open(os.path.join(S, 'inv', 'inventory.json')))['runs']
ids = {d['oid'] for d in D}
for name, members in (
        ('survey U5 (292)', {o['oid'] for o in survey}),
        ('run heads host-unreferenced', {r['state_4_commit']['head_sha'] for r in inv if r['state_4_commit']['state'] == 'host-unreferenced'}),
        ('run heads branch-only', {r['state_4_commit']['head_sha'] for r in inv if r['state_4_commit']['state'] == 'branch-only'}),
        ('run heads pull-ref-only', {r['state_4_commit']['head_sha'] for r in inv if r['state_4_commit']['state'] == 'pull-ref-only'}),
        ('package b1 (84)', {c['commit'] for c in json.load(open(os.path.join(S, 'preserve-b1', 'manifest.json')))['commits']}),
        ('package b2 (23)', {c['commit'] for c in json.load(open(os.path.join(S, 'preserve-b2', 'manifest.json')))['commits']}),
        ('package b3 (13 commits, 6 blobs)', {o['oid'] for o in json.load(open(os.path.join(O, 'inputs', 'b3zip', 'MANIFEST.json')))['objects']}),
        ('R3 pair', {'78aa5b25415cf1cd26994cb2280343ab86cd72d9', 'e7d380fcb9881e3063243aaa149e85be3cd0a914'}),
        ('BG-3 temporary heads and blob', {'3218e8d052e01650baae645e7eb92355e56e7b34', '6c160ad26a9831448e6e4cfca5761efb876a1baf',
                                           'e3ef9358d6690220c21a9b32924af9b3f70cb890', '1b5c44893410be330d7663ab2c71abdf46446805'})):
    inputs_check[name] = {'members': len(members), 'in_manifest': len(members & ids), 'missing': sorted(members - ids)}

out = {
    'schema': 'r2b-offmain-preservation-manifest', 'version': 1, 'generated': datetime.date.today().isoformat(),
    'main': MAIN,
    'host_state': {'refs_listed_at': open(os.path.join(W, 'host-refs.time')).read().strip(),
                   'by_sha_fetch_at': open(os.path.join(W, 'hostcheck.time')).read().strip(),
                   'by_sha_fetch_result': '144 of 144 cited objects that no host ref reaches were served by sha; '
                                          'their closure came back as 1080 objects, every one hash-verified by git'},
    'scope': 'the union of the R2-B survey (U5: 202 commits, 90 blobs/trees), every cited run head not on main in '
             'the run inventory (host-unreferenced, branch-only, pull-ref-only), the three preservation packages, '
             'the R3 pair and BG-3\'s off-main citations; plus every tree and blob those objects need that main lacks',
    'holder_states': {'on-main': 'reachable from main', 'branch': 'reachable from a host branch',
                      'pull-ref': 'reachable from a host pull head ref only',
                      'host-unreferenced': 'reachable from no host ref; the host still serves it by sha',
                      'local-only': 'not served by the host; a local copy exists'},
    'local_copy_names': {'shared-clone': 'the session clone\'s object store', 'package-b1': 'preserve-b1 bundle (84)',
                         'package-b2': 'preserve-b2 bundle (23 + 9 ancestors)', 'package-b3': 'preserve-b3 bundle (13)',
                         'package-b3-rawblob': 'preserve-b3 raw blob file'},
    'input_reconciliation': inputs_check,
    'counts': counts,
    'sizes': ext['sizes'],
    'controls': ext['controls'],
    'not_retained': ext['not_retained'],
    'unrecoverable': ext['unrecoverable'],
    'objects': D,
}
json.dump(out, open(os.path.join(O, 'manifest.json'), 'w'), indent=1)
print(json.dumps(counts, indent=1)[:4000])
print(json.dumps(inputs_check, indent=1))
