"""DR-1d, DR-2, DR-3 over every text file of the H and W trees (outside the corpus too)."""
import sys, os, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_rules as r
W = '413b0bb88f39cad901befcf4684355c7ee39480b'
for name, c in (('H', g.H), ('W', W)):
    tree = [l.split('\t') for l in g.git('ls-tree', '-r', c).split('\n') if l]
    proc = subprocess.Popen(['git', '-C', g.REPO, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    hits = []
    for meta, path in tree:
        sha = meta.split()[2]
        proc.stdin.write((sha + '\n').encode()); proc.stdin.flush()
        hdr = proc.stdout.readline().split(); d = proc.stdout.read(int(hdr[2])); proc.stdout.read(1)
        try: t = d.decode('utf-8')
        except UnicodeDecodeError: continue
        low = t.lower()
        if 'sixth' not in low and 'seventh' not in low and 'finit' not in low: continue
        L = t.split('\n')
        for i, l in enumerate(L, 1):
            for k in r.deny_line(l):
                if k in ('DR-1d', 'DR-2'): hits.append((k, path, i, l[:200]))
        for lns, p in r.paragraphs(L):
            if 'finit' not in p.lower() and 'sixth' not in p.lower() and 'seventh' not in p.lower(): continue
            if len(p) > 200000: continue
            for s in r.split_sentences(p):
                for k in r.deny_sentence(s):
                    if k in ('DR-1d', 'DR-2', 'DR-3'): hits.append((k, path, lns[0], s[:200]))
    print(name, len(hits))
    for h in hits[:40]: print('  ', h)
