"""Resolve the 4657/4671 blob-count difference: list the corpus blobs found by an unrestricted
rev-list --all --objects but not by the path-limited one used in the v4 review, and scan them
(and, for completeness, all 4671) with DR-1d, DR-2 and DR-3 (prefilters exact, as in v4)."""
import sys, os, subprocess, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv5_rules as r
def blobs(args):
    out = subprocess.run(['git', '-C', g.REPO, 'rev-list', '--all', '--objects'] + args, capture_output=True, text=True, check=True).stdout
    d = {}
    for l in out.split('\n'):
        p = l.split(' ', 1)
        if len(p) == 2 and re.match(r'^(papers|book)/[^/]*\.md$', p[1]): d.setdefault(p[0], p[1])
    return d
A = blobs(['--', 'papers', 'book']); B = blobs([])
extra = sorted(set(B) - set(A)); print('path-limited', len(A), 'unrestricted', len(B), 'only unrestricted', len(extra), 'only path-limited', len(set(A) - set(B)))
proc = subprocess.Popen(['git', '-C', g.REPO, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
def scan(sha):
    proc.stdin.write((sha + '\n').encode()); proc.stdin.flush()
    hdr = proc.stdout.readline().split(); d = proc.stdout.read(int(hdr[2])); proc.stdout.read(1)
    t = d.decode('utf-8', 'replace'); L = t.split('\n'); hits = []
    for i, l in enumerate(L, 1):
        ll = l.lower()
        if 'sixth' in ll or 'seventh' in ll:
            hits += [('line', k, i) for k in r.deny_line(l, True) if k in ('DR-1d', 'DR-2')]
    for v in (1, 2):
        for lns, p in r.paragraphs(L, v):
            lo = p.lower()
            if 'finit' not in lo and 'sixth' not in lo and 'seventh' not in lo: continue
            for s in r.split_sentences(p, v):
                hits += [('sent-v%d' % v, k, lns[0]) for k in r.deny_sentence(s, True) if k in ('DR-1d', 'DR-2', 'DR-3')]
    return hits
for sha in extra:
    print('  extra', sha[:10], B[sha], scan(sha))
tot = 0
for sha in B:
    h = scan(sha)
    if h: tot += 1; print('HIT', sha, B[sha], h)
print('blobs with a DR-1d/DR-2/DR-3 match among all', len(B), ':', tot)
