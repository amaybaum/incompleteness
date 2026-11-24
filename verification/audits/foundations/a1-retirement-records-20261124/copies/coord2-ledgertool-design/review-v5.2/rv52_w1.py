"""W1 sentences at T1' under splitter v2 (my transcription): length, negative-literal counts
(case-sensitive as literals, and case-insensitive for reference), and the neighbour context."""
import sys, os, re, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv5_rules as r
NEG = ['A1', 'A1-A6', 'finit', 'assumption', 'axiom', 'of the substratum']
W1 = [('papers/SM.md', 1394), ('book/ch09-universality.md', 137), ('book/ch19-open-problems.md', 198),
      ('book/ch19-open-problems.md', 212), ('book/The-Incompleteness-of-Observation-FULL.md', 2554),
      ('book/The-Incompleteness-of-Observation-FULL.md', 5270), ('book/The-Incompleteness-of-Observation-FULL.md', 5284)]
def sents_of(L):
    out = []
    for lns, p in r.paragraphs(L, 2):
        for s in r.split_sentences(p, 2): out.append((s, lns))
    return out
for f, ln in W1:
    L = g.lines(g.T, f); S = sents_of(L)
    idx = [k for k, (s, lns) in enumerate(S) if ln in lns and 'six structural' in s]
    for k in idx:
        s = S[k][0]
        cnt = {n: len(re.findall(re.escape(n), s)) for n in NEG}
        ci = {n: len(re.findall(re.escape(n), s, re.I)) for n in NEG}
        dup = sum(1 for x, _ in S if x == s)
        print('%s:%d len=%d neg=%s ci=%s copies_in_file=%d sha=%s' % (f, ln, len(s), {k2: v for k2, v in cnt.items() if v}, {k2: v for k2, v in ci.items() if v}, dup, hashlib.sha256(s.encode()).hexdigest()[:12]))
