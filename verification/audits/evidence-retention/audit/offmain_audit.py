"""Read-only audit: references in main's tracked text that depend on content not retained on main.

Classes:
  P  local/temporary paths (/tmp/, scratchpad, /root/, /home/user)
  B  names of branches other than main (pattern <prefix>/<name>), and whether they still exist
  C  commit ids (abbreviated or full) that resolve to a commit not reachable from main
  O  blob/tree ids that resolve to an object not reachable from main
  D  64-hex digests cited under verification/ that equal the sha256 of no file tracked at MAIN
  R  CI run and job ids: 11-digit run ids (3xxxxxxxxxx) and 12-digit job ids (1xxxxxxxxxxx) on lines that
     also say "run", "job" or "actions/"
Hex tokens of 7-40 characters that resolve to no object are not reported (they are digests or other numbers).
Paths are taken exactly as git lists them (repository-relative); no directory prefix is added to them.

Each citing file is classed by what keeps it unchanged:
  receipt         verification/receipts/*.json (kept by the V3 verifier)
  native-record   under the record-directory a receipt-holding round declares (kept by G13)
  legacy-record   listed in verification/infrastructure/legacy-records.json (kept by the legacy-records step)
  mutable         anything else
Commits are grouped by the remote branches that hold them; the grouping describes the remote at run time.

Usage: offmain_audit.py MAIN   (run from a clone with every remote branch fetched)
"""
import collections
import hashlib
import json
import re
import subprocess
import sys

MAIN = sys.argv[1]


def run(*a, inp=None):
    return subprocess.run(a, input=inp, capture_output=True, text=True, check=False).stdout


def show(path):
    return subprocess.run(['git', 'show', '%s:%s' % (MAIN, path)], capture_output=True).stdout


all_files = [f for f in run('git', 'ls-tree', '-r', '--name-only', MAIN).split('\n') if f]
skip_ext = ('.pdf', '.tex', '.olean', '.png', '.jpg', '.gz', '.zip', '.ilean')
files = [f for f in all_files if not f.endswith(skip_ext)]
reach = set(l.split()[0] for l in run('git', 'rev-list', '--objects', MAIN).split('\n') if l)
branches = set(l.strip().replace('origin/', '', 1) for l in run('git', 'branch', '-r').split('\n')
               if l.strip() and '->' not in l)

# ---------------------------------------------------------------- mutability classes
record_dirs = []
for r in [f for f in all_files if f.startswith('verification/receipts/') and f.endswith('.json')]:
    for b in json.loads(show(r)).get('control_plane_blobs', []):
        m = re.search(r'```v3-round\n(.*?)```', show(b['path']).decode('utf-8'), re.S)
        d = m and re.search(r'^record-directory (\S+)', m.group(1), re.M)
        if d:
            record_dirs.append(d.group(1).rstrip('/') + '/')
legacy = set(json.loads(show('verification/infrastructure/legacy-records.json'))['records'])


def klass(path):
    if path.startswith('verification/receipts/'):
        return 'receipt'
    if any(path.startswith(d) for d in record_dirs):
        return 'native-record'
    if path in legacy:
        return 'legacy-record'
    return 'mutable'


# ---------------------------------------------------------------- scan
hexre = re.compile(r'(?<![0-9A-Za-z])[0-9a-f]{7,40}(?![0-9A-Za-z])')
pathre = re.compile(r'(/tmp/|scratchpad|/root/|/home/user)')
brre = re.compile(r'(?<![\w/.-])((?:tmp|build|research|plan|draft|codex|docs|fix|feat|pr|exp|archive)/[A-Za-z0-9._-]+)')
runre = re.compile(r'(?<!\d)(3\d{10}|1\d{11})(?!\d)')
ctxre = re.compile(r'\brun|\bjob|actions/', re.I)
tokens = collections.defaultdict(list)
P, B, RUNREF = [], [], []
texts = {}
for f in files:
    try:
        txt = show(f).decode('utf-8')
    except UnicodeDecodeError:
        continue
    texts[f] = txt
    for i, line in enumerate(txt.split('\n'), 1):
        if pathre.search(line):
            P.append((f, i, line.strip()[:160]))
        for m in brre.finditer(line):
            name = m.group(1).rstrip('.,;:)`\'"')
            if '/' in name and not name.endswith(('.md', '.py', '.lean', '.json')) and re.search(r'\d{6,8}|[a-z]-[a-z]', name):
                B.append((f, i, name, name in branches))
        for m in hexre.finditer(line):
            tokens[m.group(0)].append((f, i))
        if ctxre.search(line):
            for m in runre.finditer(line):
                RUNREF.append((f, i, m.group(1)))

names = list(tokens)
out = run('git', 'cat-file', '--batch-check=%(objectname) %(objecttype)', inp='\n'.join(names) + '\n').split('\n')
C, O = [], []
for tok, res in zip(names, out):
    parts = res.split()
    if len(parts) != 2 or parts[1] not in ('commit', 'tree', 'blob', 'tag'):
        continue
    oid, typ = parts
    if typ == 'commit':
        if subprocess.run(['git', 'merge-base', '--is-ancestor', oid, MAIN]).returncode != 0:
            C.append((tok, oid, tokens[tok]))
    elif oid not in reach:
        O.append((tok, oid, typ, tokens[tok]))


def cont(oid):
    r = run('git', 'branch', '-r', '--contains', oid).split()
    return [x.replace('origin/', '', 1) for x in r if x != '->']


def group(brs):
    g = set()
    for b in brs:
        if b.startswith('research/'):
            g.add('research')
        elif 'predicted' in b or b.startswith('tmp/'):
            g.add('predicted')
        elif re.search(r'-dev\d*$', b) or b.startswith('dev-'):
            g.add('development')
        else:
            g.add('other')
    return '+'.join(sorted(g)) if g else 'no branch'


def tally(refs):
    c = collections.Counter(klass(f) for f, _ in refs)
    return ', '.join('%s %d' % (k, c[k]) for k in sorted(c))


print('== P: local/temporary paths: %d lines in %d files' % (len(P), len({f for f, _, _ in P})))
for f, i, l in P:
    print('  [%s] %s:%d  %s' % (klass(f), f, i, l))
print('== B: non-main branch names: %d mentions of %d names' % (len(B), len({n for _, _, n, _ in B})))
seen = collections.Counter((n, e) for _, _, n, e in B)
for (n, e), c in sorted(seen.items()):
    print('  %-55s %s  x%d' % (n, 'exists' if e else 'GONE', c))
for f, i, n, _ in B:
    print('      [%s] %s:%d  %s' % (klass(f), f, i, n))

c_oids = collections.defaultdict(set)
for tok, oid, locs in C:
    c_oids[oid].update(locs)
c_refs = {loc for _, _, locs in C for loc in locs}
print('== C: commits not reachable from main: %d distinct commits, cited as %d distinct tokens at %d file:line locations '
      'in %d files (%s)' % (len(c_oids), len(C), len(c_refs), len({f for f, _ in c_refs}), tally(c_refs)))
groups = collections.Counter()
for oid in sorted(c_oids):
    br = cont(oid)
    groups[group(br)] += 1
print('  held by: %s' % ', '.join('%s %d' % (k, v) for k, v in sorted(groups.items())))
for tok, oid, locs in sorted(C, key=lambda x: x[2][0]):
    br = cont(oid)
    print('  %s (%s)  on: %s' % (tok, oid[:12], ', '.join(br) if br else 'NO BRANCH (unreachable)'))
    for f, i in locs[:6]:
        print('      [%s] %s:%d' % (klass(f), f, i))
    if len(locs) > 6:
        print('      ... %d more' % (len(locs) - 6))

o_oids = {}
for tok, oid, typ, locs in O:
    o_oids[oid] = typ
o_refs = {loc for *_, locs in O for loc in locs}
print('== O: blobs/trees not reachable from main: %d distinct objects (%d blobs, %d trees), cited as %d distinct tokens '
      'at %d file:line locations (%s)' % (len(o_oids), sum(1 for t in o_oids.values() if t == 'blob'),
                                         sum(1 for t in o_oids.values() if t == 'tree'), len(O), len(o_refs), tally(o_refs)))
for tok, oid, typ, locs in sorted(O, key=lambda x: x[3][0]):
    print('  %s %s (%s)' % (typ, tok, oid[:12]))
    for f, i in locs[:4]:
        print('      [%s] %s:%d' % (klass(f), f, i))
    if len(locs) > 4:
        print('      ... %d more' % (len(locs) - 4))

ids = collections.Counter(x for _, _, x in RUNREF)
runs = sorted(x for x in ids if len(x) == 11)
jobs = sorted(x for x in ids if len(x) == 12)
r_refs = {(f, i) for f, i, _ in RUNREF}
print('== R: CI run and job ids: %d citations at %d file:line locations in %d files (%s); %d distinct run ids, '
      '%d distinct job ids; lowest run id %s' % (len(RUNREF), len(r_refs), len({f for f, _ in r_refs}), tally(r_refs),
                                                 len(runs), len(jobs), runs[0] if runs else None))
first = [(f, i) for f, i, x in RUNREF if runs and x == runs[0]]
print('  lowest run id cited at: %s' % ', '.join('%s:%d' % l for l in first))
for f, i, x in RUNREF:
    if klass(f) == 'mutable':
        print('  [mutable] %s:%d  %s' % (f, i, x))

digests = set()
for f, txt in texts.items():
    if f.startswith('verification/'):
        digests.update(re.findall(r'(?<![0-9a-f])[0-9a-f]{64}(?![0-9a-f])', txt))
tracked = {}
for f in all_files:
    tracked.setdefault(hashlib.sha256(show(f)).hexdigest(), f)
hit = sorted(d for d in digests if d in tracked)
print('== D: 64-hex digests cited under verification/: %d; equal to a tracked file at MAIN: %d; equal to none: %d'
      % (len(digests), len(hit), len(digests) - len(hit)))
for d in hit:
    print('  tracked  %s  %s' % (d[:16], tracked[d]))

clean = [f for f in files if re.match(r'(papers|book)/[^/]+\.md$', f)] + \
    ['AGENTS.md', 'verification/ROADMAP.md', 'verification/lean-manuscript-census.json'] + \
    [f for f in files if f.startswith('verification/coverage/')]
hits = collections.Counter()
c_files = {f for f, _ in c_refs} | {f for f, _ in o_refs} | {f for f, _, _ in P} | {f for f, _, _, _ in B}
url = re.compile(r'github\.com/[^/\s]+/[^/\s]+/(tree|blob)/(?!main/)')
for f in clean:
    if f in c_files or (f in texts and url.search(texts[f])):
        hits[f] += 1
print('== clean set: %d files (papers/*.md, book/*.md, AGENTS.md, ROADMAP, census registry, coverage ledger); '
      'with a P, B, C or O reference or a GitHub tree/blob URL off main: %d' % (len(clean), len(hits)))
for f in sorted(hits):
    print('  %s' % f)
