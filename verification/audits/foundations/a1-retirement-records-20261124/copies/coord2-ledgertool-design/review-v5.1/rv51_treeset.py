"""Spot-check of W2's tree-defined history set: every blob at a top-level papers/<name>.md or
book/<name>.md path in the tree of any commit reachable from the local refs; compared with the
union of the two walks (path-limited and unrestricted rev-list --objects)."""
import subprocess, re, sys
REPO = '<repo>'
def run(*a): return subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, text=True, check=True).stdout
commits = run('rev-list', '--all').split()
pat = re.compile(r'^(papers|book)/[^/]*\.md$')
tree_set = set(); trees_seen = {}
for c in commits:
    out = run('ls-tree', c, 'papers/', 'book/')
    for l in out.split('\n'):
        if not l: continue
        meta, path = l.split('\t', 1)
        mode, typ, sha = meta.split()
        if typ == 'blob' and pat.match(path):
            tree_set.add(sha)
        elif typ == 'tree':
            sub = trees_seen.get(sha)
            if sub is None:
                sub = [x.split('\t') for x in run('ls-tree', sha).split('\n') if x]
                trees_seen[sha] = sub
            for m2, name in sub:
                if m2.split()[1] == 'blob' and pat.match(path + '/' + name):
                    tree_set.add(m2.split()[2])
def walk(args):
    s = set()
    for l in run('rev-list', '--all', '--objects', *args).split('\n'):
        p = l.split(' ', 1)
        if len(p) == 2 and pat.match(p[1]): s.add(p[0])
    return s
A = walk(['--', 'papers', 'book']); B = walk([])
print('commits', len(commits), 'tree-defined', len(tree_set), 'path-limited', len(A), 'unrestricted', len(B),
      'union', len(A | B), 'equal', tree_set == (A | B))
