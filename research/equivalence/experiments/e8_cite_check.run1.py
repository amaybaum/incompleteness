"""E8-E10 citation check -- every kernel citation `File.lean:NNN` in the round-2 documents resolves at L.  (exact; text)

QUESTION.  The round-2 documents of this thread cite kernel declarations as `File.lean:NNN` (paths under
verification/lean-mathlib/OIBridge/), often next to the declaration's name.  At L the thread checkout's verification/
tree equals L's (`git diff --stat 9f9f8257 HEAD -- verification` is empty), so the citations can be read from it.

CHECKS.
  C1  every cited file exists under verification/lean-mathlib/OIBridge/ and has at least NNN lines;
  C2  every cited line NNN begins a declaration (after optional attributes/modifiers: theorem, lemma, def, abbrev,
      structure, class, instance, noncomputable def), and the script prints the declared name;
  C3  where a citation is written directly after a backticked name -- "`name` (File.lean:NNN" or "`name`, File.lean:NNN"
      or "`name` File.lean:NNN" -- the declared name at that line equals `name` (its last dotted component).
  Documents scanned: preregistration-drafts/S1..S4, NOTES-E9.md, NOTES-E10.md, the RESULTS rows R-AUDIT.1, R-E8.*, R-E9.*,
  R-E10.*, the LEDGER section "Round-2 notes", handoff-proposals/HP-5..HP-7.  A citation with a line range or a slash list
  (":106/:110") is expanded to each listed line.

DECISION RULE (fixed before run 1).  VERDICT CITATIONS-RESOLVE iff C1, C2 and C3 hold for every citation found, and at
least 40 citations are found.  Otherwise "VERDICT NOT RENDERED" followed by each failing citation.
"""
import os
import re
import sys

ROOT = '../../..'
OIB = os.path.join(ROOT, 'verification/lean-mathlib/OIBridge')
HERE = '..'
DOCS = ['preregistration-drafts/S1-kinf-seed.md', 'preregistration-drafts/S2-kinf-copy-type-covariance.md',
        'preregistration-drafts/S3-kn-descent.md', 'preregistration-drafts/S4-kinf-trans-separation.md',
        'NOTES-E9.md', 'NOTES-E10.md',
        'handoff-proposals/HP-5-coordinator-level3-wording-and-s6-cost.md',
        'handoff-proposals/HP-6-bridge-origin-two-rotations-suffice.md',
        'handoff-proposals/HP-7-countermodels-finite-octahedral-group.md']


def text_of(doc):
    return open(os.path.join(HERE, doc), encoding='utf-8').read()


texts = [(d, text_of(d)) for d in DOCS]
res = text_of('RESULTS.md')
rows = '\n'.join(l for l in res.split('\n') if re.match(r'\| R-(AUDIT\.1|E8\.|E9\.|E10\.)', l))
texts.append(('RESULTS.md (round-2 rows)', rows))
led = text_of('LEDGER.md')
texts.append(('LEDGER.md (round-2 notes)', led[led.index('## Round-2 notes'):]))

DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)*(?:private\s+|protected\s+|noncomputable\s+)*'
                  r'(theorem|lemma|def|abbrev|structure|class|instance)\s+([^\s(:{\[]+)')
CITE = re.compile(r'([A-Za-z0-9]+)\.lean:(\d+)((?:/:\d+|, :\d+)*)')
NAMED = re.compile(r'`([A-Za-z0-9_.\'’]+)`\s*(?:\(|,)?\s*([A-Za-z0-9]+)\.lean:(\d+)')

found = []
named = []
for doc, t in texts:
    for m in CITE.finditer(t):
        f, first, rest = m.group(1), int(m.group(2)), m.group(3)
        lines = [first] + [int(x) for x in re.findall(r':(\d+)', rest)]
        for ln in lines:
            found.append((doc, f, ln))
    for m in NAMED.finditer(t):
        named.append((doc, m.group(1), m.group(2), int(m.group(3))))

cache = {}


def file_lines(f):
    if f not in cache:
        p = os.path.join(OIB, f + '.lean')
        cache[f] = open(p, encoding='utf-8').read().split('\n') if os.path.exists(p) else None
    return cache[f]


fails = []
decl_at = {}
for doc, f, ln in sorted(set(found)):
    L = file_lines(f)
    if L is None or ln > len(L):
        fails.append('C1 %s: %s.lean:%d (file missing or too short)' % (doc, f, ln))
        continue
    m = DECL.match(L[ln - 1])
    if not m:
        fails.append('C2 %s: %s.lean:%d does not begin a declaration: %r' % (doc, f, ln, L[ln - 1][:80]))
        continue
    decl_at[(f, ln)] = m.group(2)
for doc, name, f, ln in sorted(set(named)):
    d = decl_at.get((f, ln))
    if d is None:
        continue
    if d.split('.')[-1] != name.split('.')[-1]:
        fails.append('C3 %s: `%s` cited at %s.lean:%d, which declares %s' % (doc, name, f, ln, d))

cites = sorted(set((f, ln) for _, f, ln in found))
for f, ln in cites:
    print('cite %s.lean:%d -> %s' % (f, ln, decl_at.get((f, ln), '??')))
print('citations: %d distinct (%d occurrences), named pairs: %d' % (len(cites), len(found), len(set(named))))
for x in fails:
    print('FAIL ' + x)
if not fails and len(cites) >= 40:
    print('VERDICT CITATIONS-RESOLVE')
else:
    print('VERDICT NOT RENDERED -- %d failing citation(s)%s' % (len(fails), '' if len(cites) >= 40 else '; fewer than 40 citations'))
sys.exit(0)
