"""Proposed item-7 amendment check (sec. 11 note 1) with no records, at H and T1':
deny lines (line level, plus lines of any sentence a deny rule matches), and final-unclassified lines
(ptr or count-grep hit lines with no deny match). The 95 retired lines must all be FAIL."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv5_rules as r, rv_prof as pr
def run(c):
    deny, final = set(), set()
    for f in g.corpus(c):
        L = g.lines(c, f)
        for i, l in enumerate(L, 1):
            if r.deny_line(l): deny.add((f, i))
        for lns, p in r.paragraphs(L):
            for s in r.split_sentences(p):
                if r.deny_sentence(s):
                    # attribute to the paragraph lines whose stripped text occurs in the sentence
                    for j in lns:
                        t = L[j - 1].strip()
                        if t and t in s: deny.add((f, j))
        for i, l in enumerate(L, 1):
            if (f, i) not in deny and pr.hits(l, ('ptr', 'count-grep')): final.add((f, i))
    return deny, final
dH, fH = run(g.H); dT, fT = run(g.T)
print('H deny', len(dH), 'final-unclassified', len(fH), 'FAIL lines', len(dH | fH))
print('T1p deny', len(dT), 'final-unclassified', len(fT))
for x in sorted(fT): print('   ', x)
# the 95: lines at H with \bA1\b or a count-grep literal, absent at T1', no deny match (line or sentence)
n95 = []
for f in g.corpus(g.H):
    LT = set(g.lines(g.T, f))
    for i, l in enumerate(g.lines(g.H, f), 1):
        if (re.search(r'\bA1\b', l) or any(x in l for x in ('Fourteen', 'six structural', 'sixth of'))) and l not in LT and (f, i) not in dH:
            n95.append((f, i))
print('retired-undenied lines', len(n95), 'all in final-unclassified:', set(n95) <= fH)
# which profile
print(collections.Counter(tuple(pr.hits(g.lines(g.H, f)[i - 1], ('ptr', 'count-grep'))) for f, i in n95))
# reverse: the final-unclassified lines at H that are not among the 95
rest = sorted(fH - set(n95)); print('final at H not in 95:', len(rest))
for f, i in rest: print('   ', f, i, g.lines(g.H, f)[i - 1][:110])
json.dump(n95, open('out5-95.json', 'w'))
