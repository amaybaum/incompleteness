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

  Design modules of this thread (EqvKnDesc, EqvOmega4, EqvLevel3, StageSeed, CopyCovariance, EqvSeams,
  EqvSeamsControl) are not kernel files at L; a citation of one (a design-run error location) is resolved against its
  byte-identical copy under research/equivalence/lean/ (the `.run38090924005` copy for EqvOmega4) by C1 only.
  C3 applies only when the backticked token is the name of some declaration of the kernel at L (so hypothesis names
  such as `hP1` written beside the line of the theorem that has them are not read as declaration names).
COUNTERCONTROLS.  X1: a synthetic citation `TransitiveBody.lean:603` (one line past `exists_affine_image_eq_eball`) must
  fail C2.  X2: a synthetic pair "`eball` (TransitiveBody.lean:602" must fail C3.  X3: a synthetic citation of a missing
  file `NoSuchModule.lean:1` must fail C1.
RUN HISTORY.  Run 1 (kept: e8_cite_check.run1.{py,out,err}) did not render: its floor of 40 distinct citations was
above the 37 found, a design-module error location (EqvOmega4.lean:157) was read as a kernel citation, and the
hypothesis name `hP1` was read as the declaration at K1Bridge.lean:128.  All three were defects of the checker, not of
the documents; the scope rules above and the countercontrols X1-X3 replace the floor, which becomes a non-vacuity
floor of 20.
DECISION RULE (fixed before run 2).  VERDICT CITATIONS-RESOLVE iff C1, C2 and C3 hold for every citation found, at least
20 distinct citations are found, and X1, X2, X3 each fail exactly as stated.  Otherwise "VERDICT NOT RENDERED" followed by
each failing citation or countercontrol.
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

DESIGN = {'EqvKnDesc': 'EqvKnDesc.lean', 'EqvOmega4': 'EqvOmega4.run38090924005.lean', 'EqvLevel3': 'EqvLevel3.lean',
          'StageSeed': 'StageSeed.lean', 'CopyCovariance': 'CopyCovariance.lean', 'EqvSeams': 'EqvSeams.lean',
          'EqvSeamsControl': 'EqvSeamsControl.lean'}
cache = {}


def file_lines(f):
    if f not in cache:
        p = os.path.join(HERE, 'lean', DESIGN[f]) if f in DESIGN else os.path.join(OIB, f + '.lean')
        cache[f] = open(p, encoding='utf-8').read().split('\n') if os.path.exists(p) else None
    return cache[f]


KERNEL_NAMES = set()
for fn in os.listdir(OIB):
    if fn.endswith('.lean'):
        for line in open(os.path.join(OIB, fn), encoding='utf-8'):
            m = DECL.match(line)
            if m:
                KERNEL_NAMES.add(m.group(2).split('.')[-1])


def check_all(found, named):
    fails = []
    decl_at = {}
    for doc, f, ln in sorted(set(found)):
        L = file_lines(f)
        if L is None or ln > len(L):
            fails.append('C1 %s: %s.lean:%d (file missing or too short)' % (doc, f, ln))
            continue
        if f in DESIGN:
            continue
        m = DECL.match(L[ln - 1])
        if not m:
            fails.append('C2 %s: %s.lean:%d does not begin a declaration: %r' % (doc, f, ln, L[ln - 1][:80]))
            continue
        decl_at[(f, ln)] = m.group(2)
    for doc, name, f, ln in sorted(set(named)):
        d = decl_at.get((f, ln))
        if d is None or name.split('.')[-1] not in KERNEL_NAMES:
            continue
        if d.split('.')[-1] != name.split('.')[-1]:
            fails.append('C3 %s: `%s` cited at %s.lean:%d, which declares %s' % (doc, name, f, ln, d))
    return fails, decl_at


fails, decl_at = check_all(found, named)
x1, _ = check_all([('X1', 'TransitiveBody', 603)], [])
x2, _ = check_all([('X2', 'TransitiveBody', 602)], [('X2', 'eball', 'TransitiveBody', 602)])
x3, _ = check_all([('X3', 'NoSuchModule', 1)], [])
ok_x = (len(x1) == 1 and x1[0].startswith('C2') and len(x2) == 1 and x2[0].startswith('C3')
        and len(x3) == 1 and x3[0].startswith('C1'))
print('countercontrols: X1 %s; X2 %s; X3 %s' % (x1, x2, x3))
if not ok_x:
    fails.append('countercontrol X1/X2/X3 did not fail as stated')

cites = sorted(set((f, ln) for _, f, ln in found))
for f, ln in cites:
    print('cite %s.lean:%d -> %s' % (f, ln, decl_at.get((f, ln), '??')))
print('citations: %d distinct (%d occurrences), named pairs: %d' % (len(cites), len(found), len(set(named))))
for x in fails:
    print('FAIL ' + x)
if not fails and len(cites) >= 20:
    print('VERDICT CITATIONS-RESOLVE')
else:
    print('VERDICT NOT RENDERED -- %d failing item(s)%s' % (len(fails), '' if len(cites) >= 20 else '; fewer than 20 citations'))
sys.exit(0)
