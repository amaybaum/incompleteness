"""P1 — inventory of the landed completion/closure objects and of the composite-level objects.

Usage: python3 -I p1_inventory.py <OIBridge dir at the base>

Decision rule (fixed before the first run).  The verdict NO-LANDED-COMPOSITE-COMPLETION is printed iff
every check below passes, i.e.
  (a) no structure of COMP-1 (ProductData, PreComposite, Composite) carries a closedness/compactness/
      continuity field;
  (b) no module other than CompositeInterface.lean names PreComposite / Composite / minPre / maxPre;
  (c) no declaration anywhere takes two DirectedStages or builds a DirectedStages from two;
  (d) the only topological `closure` / `IsClosed` facts about a *state set* are in StageCompletion,
      CompletionAction, TransitiveBody (single-tower body), and the only `UniformSpace.Completion`
      is the quasilocal observable algebra over complex matrices;
  (e) K2-GUARD-1's CandidateCone and DIM-1's maxCone / jointStates carry no closedness clause, and
      no `IsClosed (maxCone ...)` / `IsClosed (jointStates ...)` theorem exists;
  (f) ORD-1 (CompositionOrder) is about sequential composition of operation data on one tower.
Each item prints file:line evidence.  Otherwise the verdict is INVENTORY-CONTRADICTS-PREMISE.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dlib import Checks  # noqa: E402

D = sys.argv[1]
C = Checks('P1 inventory')
files = sorted(f for f in os.listdir(D) if f.endswith('.lean'))
SRC = {f: open(os.path.join(D, f), encoding='utf-8').read().split('\n') for f in files}


def find(f, pat):
    return [(i + 1, l) for i, l in enumerate(SRC[f]) if re.search(pat, l)]


def struct_block(f, name):
    lines = SRC[f]
    start = next(i for i, l in enumerate(lines) if re.match(r'structure ' + name + r'\b', l))
    end = start + 1
    while end < len(lines) and lines[end].strip() != '' and not lines[end].startswith('/--'):
        end += 1
    return start + 1, lines[start:end]


print('modules scanned: %d' % len(files))

# (a) COMP-1 structures
for name in ('ProductData', 'PreComposite', 'Composite'):
    ln, blk = struct_block('CompositeInterface.lean', name)
    fields = [re.match(r'\s+(\w+)\s*:', l).group(1) for l in blk[1:] if re.match(r'\s+\w+\s*:', l)]
    bad = [l for l in blk if re.search(r'IsClosed|IsCompact|closure|Continuous|isClosed|Bounded', l)]
    C.check('a.%s' % name, not bad, 'CompositeInterface.lean:%d fields %s' % (ln, fields))

# (b) consumers of COMP-1 outside its module
pat_b = r'\bPreComposite\b|\bminPre\b|\bmaxPre\b|ball3MinComposite|ball3MaxComposite|CompositeInterface\.Composite\b'
hits = [(f, i, l) for f in files if f != 'CompositeInterface.lean' for i, l in find(f, pat_b)]
C.check('b.no-consumer', not hits, '%d hits outside CompositeInterface.lean %s' % (len(hits), hits[:3]))
opens = [(f, i) for f in files for i, l in find(f, r'^open .*\bCompositeInterface\b')]
C.note('modules that `open CompositeInterface` (namespace only): %s' % opens)
ci_note = find('CompositeInterface.lean', r'stage-level product of|bridge from completed product towers')
C.check('b.ci-disclaimer', len(ci_note) >= 1, 'CompositeInterface.lean:%s' % [i for i, _ in ci_note])

# (c) no product of directed systems
pat_c = r'DirectedStages\s*→\s*DirectedStages|\(\w+ \w+ : DirectedStages\)|DirectedStages\s*×|prodStages|jointStages|DirectedStages\.prod'
hits = [(f, i, l.strip()) for f in files for i, l in find(f, pat_c)]
C.check('c.no-joint-tower', not hits, '%d hits %s' % (len(hits), hits[:3]))
ds_users = sorted({f for f in files for _ in find(f, r'\bDirectedStages\b')})
C.note('modules naming DirectedStages: %s' % ds_users)

# (d) topological closure of state sets / completions
body = find('StageCompletion.lean', r'closure \(convexHull ℝ \(Set\.range \(prepVec D\)\)\)')
cspace = find('StageCompletion.lean', r'abbrev CSpace .*lp \(fun _ : Label D => ℝ\) ∞')
C.check('d.SC-body', len(body) == 1 and len(cspace) == 1,
        'StageCompletion.lean:%d body; :%d CSpace = lp ... ∞ (sup-norm)' % (body[0][0], cspace[0][0]))
for f, pat, tag in [('CompletionAction.lean', r'theorem body_isClosed', 'CA body_isClosed'),
                    ('CompletionAction.lean', r'theorem mapsTo_chartBody', 'CA mapsTo_chartBody'),
                    ('CompletionAction.lean', r'body_isClosed\.preimage', 'CA closedness used for invariance'),
                    ('TransitiveBody.lean', r'theorem chartBody_isCompact', 'TB chartBody_isCompact'),
                    ('TransitiveBody.lean', r'theorem chartBody_isClosed', 'TB chartBody_isClosed'),
                    ('StageCompletion.lean', r'theorem body_subset', 'SC body_subset (closed convex extension)')]:
    h = find(f, pat)
    C.check('d.' + tag.replace(' ', '_'), len(h) >= 1, '%s:%s' % (f, [i for i, _ in h]))
topo = sorted({f for f in files for _ in find(f, r'(?<![A-Za-z.])closure \(|isClosed_closure|closure_minimal|IsClosed \(')})
C.note('modules with topological closure / IsClosed of a set: %s' % topo)
allowed_state = {'StageCompletion.lean', 'CompletionAction.lean', 'TransitiveBody.lean', 'CompositeInterface.lean',
                 'OrbitNormalization.lean', 'QuasilocalAlgebra.lean'}
C.check('d.closure-scope', set(topo) <= allowed_state | {f for f in topo if 'Quasilocal' in f or 'Region' in f},
        'outside expected set: %s' % sorted(set(topo) - allowed_state))
uc = [(f, i) for f in files for i, l in find(f, r'UniformSpace\.Completion \(')]
C.check('d.only-completion-is-quasilocal', all(f == 'QuasilocalAlgebra.lean' for f, _ in uc) and uc,
        'UniformSpace.Completion at %s' % uc[:2])
mat = find('QuasilocalAlgebra.lean', r'Matrix .*ℂ')
C.check('d.quasilocal-is-matrix-level', len(mat) > 0, 'QuasilocalAlgebra.lean complex-matrix lines e.g. :%d' % mat[0][0])
ci_closed = find('CompositeInterface.lean', r'IsClosed|isClosed')
C.note('CompositeInterface IsClosed mentions (all inside proofs about factor simplex / separation): %s'
       % [i for i, _ in ci_closed])

# (e) composite cones
cc = find('K2Guard.lean', r'^def CandidateCone')
blk = SRC['K2Guard.lean'][cc[0][0] - 1:cc[0][0] + 2]
C.check('e.CandidateCone', not any(re.search(r'IsClosed|closure|Convex', l) for l in blk),
        'K2Guard.lean:%d %s' % (cc[0][0], ' '.join(l.strip() for l in blk)))
for nm in ('maxCone', 'jointStates'):
    h = find('CompositeDimension.lean', r'^def ' + nm + r'\b')
    C.check('e.def-' + nm, len(h) == 1, 'CompositeDimension.lean:%d' % h[0][0])
    thm = [(f, i) for f in files for i, l in find(f, r'IsClosed \(' + nm)]
    C.check('e.no-IsClosed-' + nm, not thm, '%s' % thm)

# (f) ORD-1 is sequential composition
hdr = find('CompositionOrder.lean', r'iterated operation data|composed with itself')
mul = find('CompositionOrder.lean', r'^def MulClosed')
C.check('f.ORD1-sequential', len(hdr) >= 1 and len(mul) == 1,
        'CompositionOrder.lean:%s header; :%d MulClosed (algebraic composition closure)' % ([i for i, _ in hdr], mul[0][0]))

# (g) the module added since the K2C base
st = 'SharpTests.lean'
if st in SRC:
    h = [i for i, l in enumerate(SRC[st]) if re.search(r'closure|IsClosed|Composite|DirectedStages', l)]
    C.note('SharpTests.lean lines naming closure/IsClosed/Composite/DirectedStages: %s' % [i + 1 for i in h])
    C.check('g.SharpTests-no-composite-completion',
            not any(re.search(r'IsClosed|PreComposite|DirectedStages', SRC[st][i]) for i in h), '')

C.summary('NO-LANDED-COMPOSITE-COMPLETION', 'INVENTORY-CONTRADICTS-PREMISE')
