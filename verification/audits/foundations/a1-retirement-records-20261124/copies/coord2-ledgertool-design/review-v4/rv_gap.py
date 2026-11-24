"""Lines at H that carry \\bA1\\b or a count-grep literal, are absent at T1' (retired by the ledger),
and are matched by no deny rule at line or sentence level: candidate deny gaps (REVIEW only)."""
import sys, os, re, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_rules as r
cnt = collections.Counter(); out = []
for f in g.corpus(g.H):
    LH = g.lines(g.H, f); LT = set(g.lines(g.T, f))
    sent_hit = set()
    for lns, ptxt in r.paragraphs(LH):
        if any(r.deny_sentence(s) for s in r.split_sentences(ptxt)):
            # attribute to lines of the paragraph containing a matching sentence (coarse)
            for s in r.split_sentences(ptxt):
                if r.deny_sentence(s):
                    for j in lns:
                        if LH[j - 1] and any(part in LH[j - 1] for part in [s[:40], s[-40:]]): sent_hit.add(j)
    for i, l in enumerate(LH, 1):
        if not (re.search(r'\bA1\b', l) or any(x in l for x in ('Fourteen', 'six structural', 'sixth of'))):
            continue
        retired = l not in LT
        dl = r.deny_line(l)
        cnt[(retired, bool(dl) or i in sent_hit)] += 1
        if retired and not dl and i not in sent_hit:
            ms = [m.start() for m in re.finditer(r'\bA1\b', l)] or [0]
            out.append('%s:%d | %s' % (f, i, ' ... '.join(l[max(0, m - 70): m + 70] for m in ms[:2])))
print(cnt)
for o in out: print(o)
