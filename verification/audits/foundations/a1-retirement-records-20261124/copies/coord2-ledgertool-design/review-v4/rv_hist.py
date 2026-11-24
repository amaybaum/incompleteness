"""Search every historical blob of papers/*.md and book/*.md for lines/sentences matching DR-1d, DR-2, DR-3
(qualifying real-tree countercontrols, task 4). Read-only: git rev-list --objects and cat-file --batch."""
import subprocess, sys, os, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_rules as r
objs = subprocess.run(['git', '-C', g.REPO, 'rev-list', '--all', '--objects', '--', 'papers', 'book'],
                      capture_output=True, text=True, check=True).stdout.split('\n')
seen = {}
for l in objs:
    p = l.split(' ', 1)
    if len(p) == 2 and re.match(r'^(papers|book)/[^/]*\.md$', p[1]) and p[0] not in seen:
        seen[p[0]] = p[1]
proc = subprocess.Popen(['git', '-C', g.REPO, 'cat-file', '--batch'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
hits = []
targets = ('DR-1d', 'DR-2', 'DR-3')
for sha, path in seen.items():
    proc.stdin.write((sha + '\n').encode()); proc.stdin.flush()
    hdr = proc.stdout.readline().split()
    size = int(hdr[2]); data = proc.stdout.read(size); proc.stdout.read(1)
    try:
        t = data.decode('utf-8')
    except UnicodeDecodeError:
        continue
    L = t.split('\n')
    for i, l in enumerate(L, 1):
        ll = l.lower()
        if 'sixth' not in ll and 'seventh' not in ll:
            continue
        for k in r.deny_line(l):
            if k in targets:
                hits.append(('line', k, sha, path, i, l[:300]))
    for lns, ptxt in r.paragraphs(L):
        low = ptxt.lower()
        if 'finit' not in low and 'sixth' not in low and 'seventh' not in low:
            continue
        for s in r.split_sentences(ptxt):
            for k in r.deny_sentence(s):
                if k in targets:
                    hits.append(('sent', k, sha, path, lns[0], s[:300]))
print('blobs scanned', len(seen), 'hits', len(hits))
uniq = {}
for h in hits:
    uniq.setdefault((h[0], h[1], h[5]), h)
for k, h in sorted(uniq.items()):
    print(h[0], h[1], h[3], h[4], h[2][:10], '|', h[5])
json.dump(hits, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out-hist.json'), 'w'), indent=0)
