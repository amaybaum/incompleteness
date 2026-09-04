#!/usr/bin/env python3
"""claims_check.py - are withdrawn results still asserted locally?

A file-level scope note does not rescue a later sentence that states the
withdrawn result as established: a referee reads each claim where it sits.
Both classes below shipped past a green gate.

  K=2d       coupling-degree minimization does not fix the internal component
             count. What holds is the exact six-link representation theorem
             plus the CONDITIONAL link count under H-link.
  OI/QM      the kernel proves CONTAINMENT (`qm_implies_oiCore`) and forward REDUNDANCY
             (`completedOI_iff_physical`). It does not prove that quantum mechanics
             requires observational incompleteness, or a hidden sub-quantum level.

  b_m = 0    cubic equivariance FORBIDS quadratic anisotropy; it does not
             produce a metric, because b_m may vanish. "Forces a Euclidean
             quadratic symbol" overstates it.

A mention is accepted when a conditionality marker appears within the same
paragraph. Paragraph scope, not a character window: windows produce false
positives on long paragraphs and false negatives across headings.

Usage:  python3 tools/claims_check.py [--root DIR]
Exit 1 if a withdrawn result is asserted without a local marker.
"""
import os, re, sys

# A mention is fine when the paragraph either scopes it (H-link etc.) or talks
# about it NEGATIVELY -- "no framework derives m=1 from ... coupling-degree
# minimization" and "coupling-degree minimization as the DEFINITION of a site"
# are both correct usages, not assertions of the withdrawn proof.
MARKERS = ('H-link', 'H-spin', 'H-balance', 'H-Hawking', 'H-spectrum', 'H-cust', 'H-blind',
           'H-frame', 'H-scramble', 'H-shell', 'H-slope', 'kinematic in its parameter', 'conditional', 'CONDITIONAL', 'not establish',
           'does not answer', 'does not close', 'premise', 'withdrawn',
           'is not a proof', 'No framework derives', 'no framework derives',
           'definition*', 'assumption', 'does not', 'cannot', 'not a proof',
           'link count', 'rather than facts')
CLAIMS = [
    (re.compile(r'coupling-degree minimi\w*'), "K=2d: coupling-degree minimization"),
    (re.compile(r"framework's answer is \$K = 2d"), "K=2d asserted as the answer"),
    (re.compile(r'forcing an Euclidean|forces an Euclidean'),
     "b_m: 'forces a Euclidean quadratic symbol'"),
    (re.compile(r'leading scalar propagation geometry is Euclidean'),
     "b_m: leading geometry asserted Euclidean"),
    # GR layer. Each phrase asserts unconditionally something the manuscript
    # marks conditional elsewhere. All six shipped past a green gate at least
    # once, because an added correction and the statement it supersedes both
    # pass every other check.
    (re.compile(r'state-independent'),
     "GR: T_Q asserted state-independent (H-balance)"),
    (re.compile(r'purely kinematic'),
     "GR: thermality asserted purely kinematic (H-balance)"),
    (re.compile(r'must therefore be periodic|must be KMS|any QFT on this background'),
     "GR: unconditional KMS periodicity (H-Hawking)"),
    (re.compile(r'any QFT on a bifurcate|exact free-level cone per channel'),
     "GR: paraphrase of a superseded unconditional claim"),
    (re.compile(r'free-level cone is exact'),
     "GR: exact free-level cone (false on the normalized d=3 branch)"),
    (re.compile(r'(\\v?arepsilon|\\epsilon)\s*\\kappa\s*/\s*c\b(?!\^)'),
     "GR: epsilon*kappa/c should be epsilon*kappa/c^2"),
]

# ---------------------------------------------------------------- OI necessity
# A separate class with its OWN marker list, because the general MARKERS above include
# "cannot" and "does not" -- which would let "QM cannot exist without OI" escape through the
# very word that makes it dangerous.
#
# What the kernel proves is `qm_implies_oiCore`: every theory in the characterized quantum class
# realizes the sealed OI core, by way of full composite unitary control. That is a CONTAINMENT
# statement. `completedOI_iff_physical` proves the OI conjunct is redundant in the forward
# derivation, so the core does no work in producing quantum mechanics; coherent controllability
# does. Nothing proves that quantum mechanics requires a hidden sub-quantum level, and the
# standard reading does not need one. Sentences of the forms below therefore need the
# core-containment qualification in the same paragraph.
OI_MARKERS = ('core-containment', 'core containment', 'containment', 'qm_implies_oiCore',
              'completedOI_iff_physical', 'forward redundancy', 'forward-redundancy',
              'redundant', 'does no work', 'not explanatory', 'not an explanatory',
              'in the narrow', 'unsupported', 'is not proved', 'not a theorem')
OI_CLAIMS = [
    (re.compile(r'(?i)\b(QM|quantum mechanics) (requires|needs|presupposes) '
                r'(bare )?(OI\b|observation(al)? incompleteness)'),
     "OI necessity: QM asserted to require OI (only core-containment is proved)"),
    (re.compile(r'(?i)\b(QM|quantum mechanics) cannot exist without'),
     "OI necessity: 'quantum mechanics cannot exist without ...' (not proved)"),
    (re.compile(r'(?i)\b(QM|quantum mechanics) (requires|needs) hidden '
                r'(information|variables?|states?|ontology)'),
     "OI necessity: QM asserted to require a hidden sub-quantum level (not a QM consequence)"),
    (re.compile(r'(?i)\b(OI|observation(al)? incompleteness|ignorance) '
                r'(causes|produces|explains|generates|gives rise to) '
                r'(QM|quantum|quantum mechanics)'),
     "OI necessity: OI asserted to explain quantum structure (the core is forward-redundant)"),
    (re.compile(r'(?i)\bwithout (OI|observation(al)? incompleteness) there (is|would be) no '
                r'(QM|quantum)'),
     "OI necessity: contrapositive form of the same unproved claim"),
]


def main():
    root = '.'
    if '--root' in sys.argv:
        root = sys.argv[sys.argv.index('--root') + 1]
    hits = 0
    for dp, _, fs in os.walk(root):
        for f in sorted(fs):
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            text = open(p, encoding='utf-8', errors='replace').read()
            pos = 0
            for para in text.split('\n\n'):
                for rx, why, marks in ([(a, b, MARKERS) for a, b in CLAIMS]
                                      + [(a, b, OI_MARKERS) for a, b in OI_CLAIMS]):
                    m = rx.search(para)
                    if m and not any(k in para for k in marks):
                        ln = text.count('\n', 0, pos + m.start()) + 1
                        print(f"  CLAIM {p}:{ln}  {why}")
                        print(f"        ...{para[max(0,m.start()-70):m.start()+70]}...")
                        hits += 1
                pos += len(para) + 2
    if hits:
        print(f"\nclaims_check: FAILED ({hits} withdrawn result(s) asserted "
              f"without a local conditionality marker)")
        return 1
    print("claims_check: OK (no withdrawn result asserted unconditionally)")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
