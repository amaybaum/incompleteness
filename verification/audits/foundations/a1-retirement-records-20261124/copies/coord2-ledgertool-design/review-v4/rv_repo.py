"""Repo scan at T1' using P's frozen classify() (edits_check.py blob, sha256 verified), over every
tracked file at T1'. Counts by class and by kind of explaining entry."""
import sys, os, subprocess, collections, importlib.util, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g
src = os.path.join(g.DATA, 'edits_check.py')
assert hashlib.sha256(open(src, 'rb').read()).hexdigest().startswith('2856e58c')
spec = importlib.util.spec_from_file_location('p_edits_check', src)
ec = importlib.util.module_from_spec(spec); spec.loader.exec_module(ec)
files = g.ls(g.T)
proc = subprocess.Popen(['git', '-C', g.REPO, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
tree = {l.split('\t')[1]: l.split()[2] for l in g.git('ls-tree', '-r', g.T).split('\n') if l}
cls = collections.Counter(); kinds = collections.Counter()
for f in files:
    proc.stdin.write((tree[f] + '\n').encode()); proc.stdin.flush()
    hdr = proc.stdout.readline().split(); data = proc.stdout.read(int(hdr[2])); proc.stdout.read(1)
    try: t = data.decode('utf-8')
    except UnicodeDecodeError: continue
    for line in t.split('\n'):
        if ec.REPO_PAT.search(line):
            c, why = ec.classify(f, line); cls[c] += 1
            if c in ('historical record', 'generated artifact', 'manuscript', 'unexplained'): continue
            if c == 'kernel identifier': kinds['IDENT'] += 1; continue
            pathwide = any((f == p or (p.endswith('/') and f.startswith(p))) and s is None for p, s, _, _ in ec.EXPLAINED)
            kinds[('path-wide ' if pathwide else 'substring ') + c] += 1
print(dict(cls)); print(dict(kinds))
# diagnostic: IDENT-classified lines by file, and whether a substring entry of that path occurs in the line
proc2 = subprocess.Popen(['git', '-C', g.REPO, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
byf = collections.Counter(); withsub = 0
for f in files:
    proc2.stdin.write((tree[f] + '\n').encode()); proc2.stdin.flush()
    hdr = proc2.stdout.readline().split(); data = proc2.stdout.read(int(hdr[2])); proc2.stdout.read(1)
    try: t = data.decode('utf-8')
    except UnicodeDecodeError: continue
    for line in t.split('\n'):
        if ec.REPO_PAT.search(line) and ec.classify(f, line)[0] == 'kernel identifier':
            byf[f] += 1
            if any(f == p and s and s in line for p, s, _, _ in ec.EXPLAINED): withsub += 1
print('IDENT by file', dict(byf), 'IDENT lines containing a substring entry of their path:', withsub)
