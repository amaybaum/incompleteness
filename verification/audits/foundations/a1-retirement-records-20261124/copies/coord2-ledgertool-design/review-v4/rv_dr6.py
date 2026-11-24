"""Illustration only (not a proposal reviewed by anyone): a bare-label deny form, \\bA1\\b not written as
the parenthesized label (A1), and the extra count forms; counts at E, H and T1'."""
import re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g
C = {'bareA1': re.compile(r'(?<!\()\bA1\b|\bA1\b(?!\))'),
     'cnt-of-substratum': re.compile(r"(?i)\b(?:six|seven|sixth|seventh)\s+(?:structural\s+)?(?:assumptions?|axioms?|posits?|premises?|conditions?|hypothes[ie]s)\s+(?:of|on|about|for)\s+the\s+substratum\b"),
     'fourteen-item': re.compile(r'(?i)\b(?:fourteen|14)[- ](?:item|entry|posit)\b'),
     'A1-subscript-range': re.compile(r'A_\{?1\}?\$?\s*(?:-{1,3}|–|—|\\text\{--\})\s*\$?A_\{?6')}
for n, c in (('E', g.E), ('H', g.H), ('T1p', g.T)):
    out = {}
    for k, rx in C.items():
        out[k] = [(f, i) for f in g.corpus(c) for i, l in enumerate(g.lines(c, f), 1) if rx.search(l)]
    print(n, {k: len(v) for k, v in out.items()})
    if n == 'T1p':
        for k, v in out.items():
            for f, i in v: print('   ', k, f, i, g.lines(c, f)[i - 1][:160])
