"""Reviewer-constructed false negatives derived from real H lines: the 'under A1' qualifier removed so that the
sentence asserts finiteness of the substratum outright. Evaluated against deny rules, resid and review profiles."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv_rules as r, rv_prof as pr
REV = ('p0-core', 'p0-para', 'ledger-ext', 'ptr', 'repo', 'count-grep')
src = [('book/ch02-substratum.md', 212, 'a set (finite under A1) with a deterministic bijection on it', 'a finite set with a deterministic bijection on it'),
       ('papers/SM.md', 30, 'uses a set (finite under A1) with a deterministic bijection', 'uses a finite set with a deterministic bijection'),
       ('book/ch07-gravity.md', 118, 'acting on a configuration space $S$, finite under A1.', 'acting on a finite configuration space $S$.'),
       ('papers/Substratum.md', 44, 'is a lossless memory, finite under A1.', 'is a lossless memory, and it is finite.'),
       ('book/ch02-substratum.md', 136, 'the substratum is a set (finite under A1) with a bijection on it', 'the substratum is a finite set with a bijection on it')]
for f, ln, old, new in src:
    l = g.lines(g.H, f)[ln - 1]
    assert old in l, (f, ln)
    m = l.replace(old, new)
    dl = r.deny_line(m); ds = sorted({k for p in [m] for s in r.split_sentences(p) for k in r.deny_sentence(s)})
    print('%s:%d deny=%s/%s resid=%d review=%s' % (f, ln, dl, ds, bool(r.RESID.search(m)), pr.hits(m, REV)), '|', new)
