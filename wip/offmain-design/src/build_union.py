"""Union of every off-main object the preservation PR must cover, with its citations and current holders.

Inputs (read only): the R2-B survey inventory, the run inventory, the three preservation packages, the R3 pair and
BG-3's off-main citations; the scratch source repository src.git (alternates onto the shared clone and the survey's
scratch repositories), host-ref mirrors under refs/host/*, and the reachability lists computed in work/.
Output: work/union.json.
"""
import collections, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitobj import Store, parse_tree, parse_commit

O = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.dirname(O)
W = os.path.join(O, 'work')
MAIN = '66a981d5a9cab35b9ebd253aa0e610c0afbfefb6'
src = Store(os.path.join(W, 'src.git'))

def lines(p):
    return set(l.strip() for l in open(p) if l.strip())

main_objs = lines(os.path.join(W, 'main-objects.txt'))
br_objs = lines(os.path.join(W, 'br-objects.txt'))
pr_objs = lines(os.path.join(W, 'pullhead-objects.txt'))
pkg = {n: lines(os.path.join(W, f'pkg-{n}-objects.txt')) for n in ('b1', 'b2', 'b3')}
b3raw = set(os.listdir(os.path.join(O, 'inputs', 'b3zip', 'blobs')))

# ---- classifier for citing files (the audit's klass, at MAIN)
def show(path):
    return subprocess.run(['git', '--git-dir', src.gitdir, 'show', f'{MAIN}:{path}'], capture_output=True).stdout
all_files = src.git('ls-tree', '-r', '--name-only', MAIN).split('\n')
record_dirs = []
for r in [f for f in all_files if f.startswith('verification/receipts/') and f.endswith('.json')]:
    for b in json.loads(show(r)).get('control_plane_blobs', []):
        m = re.search(r'```v3-round\n(.*?)```', show(b['path']).decode('utf-8'), re.S)
        d = m and re.search(r'^record-directory (\S+)', m.group(1), re.M)
        if d:
            record_dirs.append(d.group(1).rstrip('/') + '/')
legacy = set(json.loads(show('verification/infrastructure/legacy-records.json'))['records'])
def klass(path):
    if path.startswith('verification/audits/evidence-retention/'):
        return 'archive-self'
    if path.startswith('verification/receipts/'):
        return 'receipt'
    if any(path.startswith(d) for d in record_dirs):
        return 'native-record'
    if path in legacy:
        return 'legacy-record'
    return 'mutable'

U = {}
def add(oid, typ, cite):
    rec = U.setdefault(oid, {'oid': oid, 'type': typ, 'inputs': set(), 'citations': []})
    if typ and not rec['type']:
        rec['type'] = typ
    rec['inputs'].add(cite.pop('input'))
    if cite.get('location'):
        cite.setdefault('class', klass(cite['location'].rsplit(':', 1)[0]))
        rec['citations'].append(cite)
    return rec

# 1. survey U1..U5
survey = json.load(open(os.path.join(S, 'agent-r2b', 'offmain-inventory.json')))
for o in survey['objects']:
    for l in o['locations']:
        add(o['oid'], o['type'], {'input': 'survey-' + o['universe'], 'via': 'token', 'location': f"{l['file']}:{l['line']}",
                                  'class': klass(l['file']), 'role': l.get('role') or o['role'], 'tokens': l['tokens'],
                                  'text': l['text'][:200]})
    U[o['oid']]['survey'] = {k: o.get(k) for k in ('universe', 'role', 'role_basis', 'held_by', 'proposed_mechanism',
                                                   'research_archive_tree', 'drag_commits_not_on_main')}
# 2. run inventory heads, all three non-main states
inv = json.load(open(os.path.join(S, 'inv', 'inventory.json')))
range_of = {}
for rg in inv['summary']['ranges']['ranges']:
    for x in rg['inner_runs']:
        range_of[(x, rg['location'])] = rg['endpoints']
for r in inv['runs']:
    st = r['state_4_commit']
    if st['state'] == 'on-main':
        continue
    for loc in r['locations']:
        rng = range_of.get((r['run_id'], loc))
        add(st['head_sha'], 'commit', {'input': 'run-head:' + st['state'], 'via': 'run-range' if rng else 'run',
                                       'run': None if rng else r['run_id'], 'range_member': r['run_id'] if rng else None,
                                       'tokens': rng or [r['run_id']], 'location': loc,
                                       'role': 'run-head (' + ','.join(r.get('citing_roles') or []) + ')',
                                       'run_tier': r['tier'], 'event': r['event'], 'conclusion': r['conclusion'],
                                       'head_branch': r['head_branch'], 'cited_by': r['cited_by']})
    if not r['locations']:
        add(st['head_sha'], 'commit', {'input': 'run-head:' + st['state'], 'via': 'run', 'run': r['run_id']})
# 3. packages
for n, f in (('b1', 'preserve-b1/manifest.json'), ('b2', 'preserve-b2/manifest.json')):
    for c in json.load(open(os.path.join(S, f)))['commits']:
        add(c['commit'], 'commit', {'input': 'package-' + n})
b3 = json.load(open(os.path.join(O, 'inputs', 'b3zip', 'MANIFEST.json')))
for o in b3['objects']:
    for loc in o['cited_at']:
        add(o['oid'], o['type'], {'input': 'package-b3', 'via': 'token', 'location': loc, 'role': 'cited-unreferenced', 'tokens': [o['oid'][:7]]})
# 4. R3 pair
for c, loc in (('78aa5b25415cf1cd26994cb2280343ab86cd72d9', 'verification/lean/oi_channel1_check.py:2'),
               ('e7d380fcb9881e3063243aaa149e85be3cd0a914', None)):
    add(c, 'commit', {'input': 'r3', 'via': 'token', 'location': loc, 'role': 'R3 frozen-source (OI-CHANNEL-1)', 'tokens': [c[:8]]} if loc
        else {'input': 'r3'})
# 5. BG-3 temporary heads and the off-main blob its records cite
bg3dir = 'verification/programmes/oi-qm/reconstruction/round-bg-3-scope-transfer-correction/'
for oid, typ, loc, role in (
        ('3218e8d052e01650baae645e7eb92355e56e7b34', 'commit', bg3dir + 'preregistration.md:293', 'BG-3 first predicted tree (superseded), tmp/bg3-predicted-20261015'),
        ('6c160ad26a9831448e6e4cfca5761efb876a1baf', 'commit', bg3dir + 'preregistration.md:307', 'BG-3 design tree; R1 bg3/results-116761232088.json holds at it'),
        ('e3ef9358d6690220c21a9b32924af9b3f70cb890', 'commit', bg3dir + 'preregistration.md:334', 'BG-3 design tree; R1 bg3/results-116805436638.json holds at it'),
        ('1b5c44893410be330d7663ab2c71abdf46446805', 'blob', bg3dir + 'preregistration.md:308', 'BG-3 previous controls.py (in 6c160ad2)')):
    add(oid, typ, {'input': 'bg3', 'via': 'token', 'location': loc, 'role': role, 'tokens': [oid[:8]]})
for oid, f in (('6c160ad26a9831448e6e4cfca5761efb876a1baf', 'bg3/results-116761232088.json'),
               ('e3ef9358d6690220c21a9b32924af9b3f70cb890', 'bg3/results-116805436638.json')):
    _t = show('verification/audits/evidence-retention/' + f).decode().split('\n')
    _ln = next(i for i, l in enumerate(_t, 1) if oid in l)
    add(oid, 'commit', {'input': 'bg3', 'via': 'r1-expected-result', 'location': 'verification/audits/evidence-retention/' + f + ':%d' % _ln,
                        'tokens': [oid],
                        'class': 'archive-self', 'role': 'R1 expected result holds at this commit; reproduce.py needs it'})

# ---- resolve, holders
gh_probe = survey['github_sha_probe']
for oid, rec in U.items():
    chk = src.check(oid)
    rec['present_locally'] = bool(chk)
    if chk:
        rec['type'], rec['size'] = chk
    stores = []
    for n in ('b1', 'b2', 'b3'):
        if oid in pkg[n]:
            stores.append(f'package-{n}-bundle')
    if oid in b3raw:
        stores.append('package-b3-rawblob')
    rec['packages'] = stores
    if oid in main_objs:
        rec['holder'] = 'on-main'
    elif oid in br_objs:
        rec['holder'] = 'branch'
    elif oid in pr_objs:
        rec['holder'] = 'pull-ref'
    elif chk:
        rec['holder'] = 'unreferenced'   # refined below with the host's by-sha answer
    else:
        rec['holder'] = 'missing'
    rec['inputs'] = sorted(rec['inputs'])

json.dump({'main': MAIN, 'objects': U}, open(os.path.join(W, 'union-stage1.json'), 'w'), indent=1, default=list)
c = collections.Counter((r['type'], r['holder']) for r in U.values())
print(len(U), sorted(c.items()))
print(collections.Counter(i for r in U.values() for i in r['inputs']))
