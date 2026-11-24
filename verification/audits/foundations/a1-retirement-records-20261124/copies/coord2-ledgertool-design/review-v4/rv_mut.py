"""Mutant countercontrols M-DR1d, M-DR2, M-DR3 (sec. 6.4): one substring replaced in a named H line."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_rules as r
M = [('M-DR1d', 'book/glossary.md', 11, 'The open hypothesis, not adopted,', "The substratum's sixth axiom,", 'DR-1d'),
     ('M-DR2', 'book/glossary.md', 13, "The sixth of the framework's structural assumptions A1–A6:", "The framework's sixth structural property is finiteness of the substratum:", 'DR-2'),
     ('M-DR3', 'book/ch19-open-problems.md', 212, 'six structural properties', 'six structural properties, one of which is total finiteness,', 'DR-3')]
for mid, f, ln, old, new, rule in M:
    L = g.lines(g.H, f); l = L[ln - 1]
    n = l.count(old)
    L2 = list(L); L2[ln - 1] = l.replace(old, new)
    def sent_rules(LL):
        out = set()
        for lns, p in r.paragraphs(LL):
            if ln in lns:
                for s in r.split_sentences(p): out |= set(r.deny_sentence(s))
        return out
    print(mid, 'occurrences', n, 'orig line', r.deny_line(l), 'orig sent', sorted(sent_rules(L)),
          '| mut line', r.deny_line(L2[ln - 1]), 'mut sent', sorted(sent_rules(L2)), '| target', rule)
