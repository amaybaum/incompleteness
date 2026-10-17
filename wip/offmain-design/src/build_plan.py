"""Decide, for every cited off-main object and every object it depends on, how it is preserved.

Reads work/union-stage1.json (build_union.py) and the reachability lists in work/; writes work/plan.json.

Mechanisms
  commit  raw:connected       raw commit, all its trees and blobs that main lacks; every parent is on main or is a
                              retained commit that is itself connected: reconstitutes exactly, fully connected
          raw:tree            as above, but some parent is neither on main nor a connected retained commit:
                              commit id and complete tree verified, parents named only
          raw:partial-tree    commit and every tree retained, some blob of the tree withheld (raw log, build PDF):
                              commit and tree ids verified, the withheld entries named by id
          inclusion-proof     raw commit, root tree, the trees on each cited path and what lies under it
          identity-anchor     raw commit object only (no claim rests on its tree)
  tree    raw                 raw tree object (a dependency, or a cited predicted-tree root)
  blob    byte-copy           the blob's bytes, unmodified, stored by id (restores the blob id on main)
          withheld:raw-log    a raw run log or transcript (.log/.err/.out): not committed (AGENTS §A.42 item 1)
          withheld:build-pdf  a build output whose bytes no record freezes: provenance only, owner decision
          excluded:excerpt    one of R1's 194 excerpt blobs: never stored
"""
import collections, hashlib, json, os, sys, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gitobj import Store, parse_tree, parse_commit

O = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = os.path.dirname(O)
W = os.path.join(O, 'work')
src = Store(os.path.join(W, 'src.git'))
L = lambda f: set(l.strip() for l in open(os.path.join(W, f)) if l.strip())
main = L('main-objects.txt'); br = L('br-objects.txt'); pr = L('pullhead-objects.txt'); hostsrv = L('hostcheck-objects.txt')
pkg = {n: L(f'pkg-{n}-objects.txt') for n in ('b1', 'b2', 'b3')}
b3raw = set(os.listdir(os.path.join(O, 'inputs', 'b3zip', 'blobs')))
EXCERPTS = set(l.strip() for l in open(os.path.join(S, 'r1', 'excerpt-blobs.txt')) if l.strip())
U = json.load(open(os.path.join(W, 'union-stage1.json')))['objects']

INCLUSION = {  # commit -> cited paths (a trailing / means the directory and everything under it)
    '78aa5b25415cf1cd26994cb2280343ab86cd72d9': ['research/round7-channel/PREREGISTRATION.md'],
    'e7d380fcb9881e3063243aaa149e85be3cd0a914': ['research/round7-channel/', 'research/AUDITS/2026-10-11-round6/',
                                                 'research/archive/pt/R6/NOTES.md'],
    '5f4089a4500a59943c33ba13656b2530824068c5': ['research/bridge/NOTES-B4.md'],
}
ANCHOR = {  # research-archive commits whose citation rests on identity, parents and dates, not on their tree
    '4dc0321ca2aac6f6aca6f55efc90b7f51330334a': 'reference inventory "research/archive 4dc0321c, I3 and I4" names no path',
    'a163b9246a98ef100cbf256e51b00e39a1fc564a': 'chronology: "preceded the first design run"',
    '9430c4635c34ef8f252176925201737a6966235d': 'chronology: "preceded the next design run"',
    '8508d17278ea11b90fd37d137172e18a25b3835f': 'chronology: "preceded the historical predictive publication"',
}
LOG_EXT = ('.log', '.err', '.out')


def blob_policy(oid, path):
    if oid in EXCERPTS:
        return 'excluded:excerpt'
    if src.check(oid)[1] == 0:
        return 'byte-copy'          # the empty blob carries no content of any kind
    if path.endswith(LOG_EXT):
        return 'withheld:raw-log'
    if path.endswith('.pdf'):
        return 'withheld:build-pdf'
    return 'byte-copy'


P = {}  # oid -> plan record


def rec(oid, typ):
    r = P.get(oid)
    if r is None:
        t, size = src.check(oid)
        assert t == typ, (oid, t, typ)
        r = P[oid] = {'oid': oid, 'type': typ, 'size': size, 'needed_by': [], 'paths': set()}
    return r


def need(oid, typ, by, path):
    r = rec(oid, typ)
    if by:
        r['needed_by'].append((by, path))
    r['paths'].add(path)
    return r


FULL_TREES = set()   # trees retained with everything under them (as opposed to inclusion-proof path trees)


def walk(tree, prefix, by, only=None):
    """Retain tree and everything under it that main lacks. `only`: the cited paths of an inclusion proof; a tree
    above them is retained as a path tree (its other entries are named, not retained)."""
    if tree in main:
        return
    need(tree, 'tree', by, prefix or '/')
    if only is None:
        FULL_TREES.add(tree)
    for mode, name, oid in parse_tree(src.read(tree)[1]):
        p = prefix + name
        if mode == '160000':
            continue
        if only is not None:
            if mode == '40000':
                d = p + '/'
                if any(q.startswith(d) and q != d for q in only):        # a cited path lies further down
                    walk(oid, d, by, only)
                elif d in only:                                           # a cited directory: everything under it
                    walk(oid, d, by, None)
            elif p in only and oid not in main:
                need(oid, 'blob', by, p)
            continue
        if mode == '40000':
            walk(oid, p + '/', by, None)
        elif oid not in main:
            need(oid, 'blob', by, p)


commit_info = {}
for oid, u in U.items():
    if u['type'] == 'commit':
        tree, parents, hdr, msg = parse_commit(src.read(oid)[1])
        commit_info[oid] = (tree, parents)
        r = rec(oid, 'commit')
        r['cited'] = True
        if oid in INCLUSION:
            r['mechanism'] = 'inclusion-proof'
            r['inclusion_paths'] = INCLUSION[oid]
            walk(tree, '', oid, INCLUSION[oid])
        elif oid in ANCHOR:
            r['mechanism'] = 'identity-anchor'
            r['anchor_reason'] = ANCHOR[oid]
        else:
            walk(tree, '', oid)
    elif u['type'] == 'tree':
        r = rec(oid, 'tree'); r['cited'] = True
        walk(oid, '', None)
    else:
        r = rec(oid, 'blob'); r['cited'] = True
        r['paths'].add('(cited by id)')

for oid, r in P.items():
    if r['type'] == 'blob':
        pols = {blob_policy(oid, p) for p in r['paths'] if p != '(cited by id)'} or {blob_policy(oid, '')}
        r['mechanism'] = sorted(pols, key=lambda x: ('excluded' not in x, 'withheld' not in x))[0]
    elif r['type'] == 'tree':
        r['mechanism'] = 'raw' if oid in FULL_TREES or r.get('cited') else 'raw:proof-path'

# completeness and connectivity of the commits retained with their trees
def stored(oid):
    return oid in P and P[oid]['mechanism'] in ('raw', 'byte-copy') or P.get(oid, {}).get('type') == 'commit'

def tree_complete(tree, seen=None):
    if tree in main:
        return True, []
    missing = []
    for mode, name, oid in parse_tree(src.read(tree)[1]):
        if mode == '160000':
            continue
        if mode == '40000':
            ok, m = tree_complete(oid); missing += m
        elif oid not in main and P.get(oid, {}).get('mechanism') != 'byte-copy':
            missing.append(oid)
    return not missing, missing

memo = {}
def connected(c):
    if c in main:
        return True
    if c in memo:
        return memo[c]
    memo[c] = False
    r = P.get(c)
    if not r or r['type'] != 'commit' or r.get('mechanism') in ('inclusion-proof', 'identity-anchor'):
        return False
    tree, parents = commit_info.get(c) or parse_commit(src.read(c)[1])[:2]
    ok = tree_complete(tree)[0] and all(connected(p) for p in parents)
    memo[c] = ok
    return ok

for c, r in P.items():
    if r['type'] != 'commit' or r.get('mechanism'):
        continue
    tree, parents = commit_info[c]
    ok, missing = tree_complete(tree)
    r['parents'] = parents
    if not ok:
        r['mechanism'] = 'raw:partial-tree'
        r['withheld_blobs'] = sorted(set(missing))
    elif connected(c):
        r['mechanism'] = 'raw:connected'
    else:
        r['mechanism'] = 'raw:tree'
for c, r in P.items():
    if r['type'] == 'commit':
        r.setdefault('parents', commit_info[c][1])
        # named only: parents neither on main nor retained
        r['parents_not_retained'] = [p for p in r['parents'] if p not in main and p not in P]

# holders and local copies
for oid, r in P.items():
    if oid in main:
        r['holder'] = 'on-main'
    elif oid in br:
        r['holder'] = 'branch'
    elif oid in pr:
        r['holder'] = 'pull-ref'
    elif oid in hostsrv:
        r['holder'] = 'host-unreferenced'
    else:
        r['holder'] = 'local-only'
    r['local_copies'] = ['shared-clone' if src.git('cat-file', '-e', oid, check=False) == '' else None]
    r['local_copies'] = [x for x in r['local_copies'] if x] + \
        [f'package-{n}' for n in ('b1', 'b2', 'b3') if oid in pkg[n]] + (['package-b3-rawblob'] if oid in b3raw else [])
    t, data = src.read(oid)
    full = t.encode() + b' %d\0' % len(data) + data
    assert hashlib.sha1(full).hexdigest() == oid
    r['raw_bytes'] = len(data)
    r['zlib_bytes'] = len(zlib.compress(full, 6))
    r['sha256'] = hashlib.sha256(data).hexdigest()
    r['paths'] = sorted(r['paths'])

# uncited off-main ancestors of the raw:tree commits (the parent chain to main; not retained)
chain = set()
for c, r in P.items():
    if r.get('mechanism') == 'raw:tree':
        for x in src.git('rev-list', c, '--not', 'refs/heads/main').split():
            if x not in P:
                chain.add(x)
chain_bytes = sum(src.check(x)[1] for x in chain)

json.dump({'objects': P, 'chain_commits_not_retained': sorted(chain), 'chain_commit_bytes': chain_bytes},
          open(os.path.join(W, 'plan.json'), 'w'), indent=1, default=list)
c = collections.Counter((r['type'], r['mechanism']) for r in P.values())
for k, v in sorted(c.items()):
    print(k, v)
print('objects', len(P), 'cited', sum(1 for r in P.values() if r.get('cited')))
print('chain commits not retained', len(chain), chain_bytes)
print(collections.Counter((r['holder']) for r in P.values()))
