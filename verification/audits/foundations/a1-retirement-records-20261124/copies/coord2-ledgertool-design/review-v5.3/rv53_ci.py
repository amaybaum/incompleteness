"""O1/WB15: case-sensitive vs case-insensitive negative-literal counts on every W1 and W2 sentence at T1'
(splitter v2, my transcription)."""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv5_rules as r
W1N = ['A1', 'A1-A6', 'finit', 'assumption', 'axiom', 'of the substratum']
W2N = ['Finiteness', 'finit', 'posit', 'substratum', 'configuration space']
FULL = 'book/The-Incompleteness-of-Observation-FULL.md'
W1 = [('papers/SM.md', 1394), ('book/ch09-universality.md', 137), ('book/ch19-open-problems.md', 198), ('book/ch19-open-problems.md', 212), (FULL, 2554), (FULL, 5270), (FULL, 5284)]
W2 = [('book/appendix-b-derivations.md', 235), ('book/appendix-b-derivations.md', 246), (FULL, 5914), (FULL, 5925)]
for name, sites, neg in (('W1', W1, W1N), ('W2', W2, W2N)):
    for f, ln in sites:
        L = g.lines(g.T, f)
        ss = [s for lns, p in r.paragraphs(L, 2) if ln in lns for s in r.split_sentences(p, 2)]
        ss = [s for s in ss if ('six structural' in s if name == 'W1' else '(A1)' in s)]
        for s in ss:
            cs = {n: len(re.findall(re.escape(n), s)) for n in neg}
            ci = {n: len(re.findall(re.escape(n), s, re.I)) for n in neg}
            print(name, '%s:%d' % (f, ln), 'equal' if cs == ci else 'DIFFER', {k: v for k, v in ci.items() if v})
