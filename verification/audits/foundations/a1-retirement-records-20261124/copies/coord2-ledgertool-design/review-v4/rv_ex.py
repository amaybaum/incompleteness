"""Control strings: V-controls of sec. 10.2, the v3 review's list, and reviewer-constructed paraphrases,
against deny rules (line and sentence), resid and the review profiles."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rv_rules as r, rv_prof as pr
REV = ('p0-core', 'p0-para', 'ledger-ext', 'ptr', 'repo', 'count-grep')
cases = [
 ('V1', 'The six structural properties of the substratum are listed in Chapter 2.'),
 ('V2', 'Its six structural properties, one of which is total finiteness, are independent.'),
 ('V3', '(A1) the substratum is finite in total'),
 ('V4', "the framework's sixth structural property, finiteness of the bijection"),
 ('V5', '**(A1) Finiteness.** The configuration space is finite.'),
 ('V6', 'the six structural properties of the substratum, including finiteness'),
 ('V9', 'Six structural assumptions define the substratum.'),
 ('V10', 'the six structural conditions on the substratum'),
 ('V11', 'six structural premises of the framework'),
 ('V12', 'the six substratum posits'),
 ('V13', 'the structural assumptions A1 through A6'),
 ('V14a', 'A1--A6'), ('V14b', 'A1—A6'), ('V14c', '(A1)–(A6)'), ('V14d', 'A1, ..., A6'),
 ('V15', "the substratum's sixth axiom, finiteness"),
 ('V16', 'posit A1 (finiteness) holds'),
 ('V17', 'A1 (Finiteness): the configuration space is finite'),
 ('V18', '(A1) Finiteness. The configuration space S is finite.'),
 ('V19', 'The posit ledger has 14 items.'),
 ('V20', 'the six structural properties of the bijection, the first being finiteness of S'),
 ('V21', 'one of the posits is that the configuration space is finite'),
 ('V22', 'Fourteen items, of unequal weight, and not fourteen independent physical assumptions.'),
 ('rv14', 'A1 to A6'),
 # reviewer-constructed forms
 ('X-a', 'the structural assumptions A1, A2, \\ldots, A6'),
 ('X-b', 'the structural assumptions $A_1$–$A_6$'),
 ('X-c', 'assumptions A1–A6'.replace('A6', 'A 6')),
 ('X-d', 'the structural assumptions (A1–A6)'),
 ('X-e', 'the six posits of the substratum'),
 ('X-f', 'six assumptions about the substratum'),
 ('X-g', 'the first structural assumption, finiteness of the configuration space'),
 ('X-h', 'Assumption A1 (finiteness of S) is retained.'),
 ('X-i', 'the finiteness assumption'),
 ('X-j', 'We take the substratum to be finite.'),
 ('X-k', 'The substratum is assumed to have a finite number of states.'),
 ('X-l', 'the universe is assumed finite'),
 ('X-m', 'The posit ledger lists fourteen.'),
 ('X-n', 'the fourteen-item posit ledger'),
 ('X-o', 'Structural assumption (A1): finiteness.'),
 ('X-p', 'six structural hypotheses'),
 ('X-q', 'A1 – A6'),
 ('X-r', 'A1 – A6'),
 ('X-s', 'A1−A6'),
 ('X-t', 'axioms A1–A6'),
 ('X-u', 'among the posits is the finiteness of the total configuration space'),
 ('X-v', 'The configuration space is finite by assumption.'),
 ('X-w', 'one of the posits is that there are only finitely many configurations'),
 ('X-x', 'the six structural properties of the substratum'),
 ('X-y', 'Finiteness (A1)'),
 ('X-z', 'S is finite, as the first posit requires'),
]
for cid, s in cases:
    dl = r.deny_line(s); ds = [k for sent in r.split_sentences(s) for k in r.deny_sentence(sent)]
    rv = pr.hits(s, REV); rs = bool(r.RESID.search(s))
    print('%-5s deny_line=%-22s deny_sent=%-26s resid=%d review=%s | %s' % (cid, ','.join(dl), ','.join(sorted(set(ds))), rs, ','.join(rv), s))
