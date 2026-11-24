"""Every constructed string of v4 that DR-1d or DR-2 matched (v4 controls and mutants, the v4 review's
strings), and its outcome under the v5 active set, item 7's final profiles and widened resid."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_git as g, rv5_rules as r, rv_prof as pr
S = [('v4 V4', "the framework's sixth structural property, finiteness of the bijection"),
     ('v4 V15', "the substratum's sixth axiom, finiteness"),
     ('v4 M-DR1d line', g.lines(g.H, 'book/glossary.md')[10].replace('The open hypothesis, not adopted,', "The substratum's sixth axiom,")),
     ('v4 M-DR2 line', g.lines(g.H, 'book/glossary.md')[12].replace("The sixth of the framework's structural assumptions A1–A6:", "The framework's sixth structural property is finiteness of the substratum:")),
     ('M-DR2 text alone', "The framework's sixth structural property is finiteness of the substratum:"),
     ('M-DR1d text alone', "The substratum's sixth axiom, the substratum has a finite total configuration space."),
     ('v4 rv14/X-g-like', 'the structural sixth assumption, finiteness')]
for sid, s in S:
    ret = [k for k in r.deny_line(s, True) if k in ('DR-1d', 'DR-2')]
    act = r.deny_line(s) + (['DR-3'] if 'DR-3' in r.deny_sentence(s) else [])
    rev = pr.hits(s, ('p0-core', 'p0-para', 'ledger-ext', 'ptr', 'repo', 'count-grep'))
    i7 = 'FAIL deny' if act else ('FAIL final' if set(rev) & {'ptr', 'count-grep'} else ('REVIEW' if (rev or r.resid(s)) else 'PASS'))
    print('%-18s retired=%s active=%s review=%s resid=%s -> item7: %s' % (sid, ret, act, rev, r.resid(s), i7))
