#!/usr/bin/env python3
"""I4 declaration dump -- exact docstrings and signatures for the inventory (thread I4, stage 6).

Run from pt/I4/ as:  python3 -I -B decl_dump.py > decl_dump.out 2> decl_dump.err

DECISION RULE (fixed before the first run):
 D1 Same module list, comment handling and declaration recognition as census_kernel.py (rules R1-R3).
 D2 For every declaration of keyword axiom/opaque/structure/class/def/abbrev/inductive/theorem/lemma,
    print a block:  '=== <Module>.lean:<line> <keyword> <name>' ; 'DOC:' + the docstring lines that end
    on the nearest preceding non-blank line that is not an attribute, 'variable ... in' or 'omit ... in'
    line (verbatim, file line numbers prefixed); 'SIG:' + the verbatim source lines from the declaration
    line up to and including the line holding the first depth-0 ':=' or 'where' (at most 40 lines).
 D3 'HEADLINE' marks a declaration whose docstring's first non-space text after '/--' begins with '**'.
 D4 Control: the block for HasParallelReferenceExtension must contain its docstring line 444 and its
    signature lines 447-451; the block for withSpectator must start at line 422.  Else CONTROL FAILURE.
 D5 Deterministic output; no clock values.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', 'base', 'verification', 'lean-mathlib', 'OIBridge'))
MODULES = [
    'GeneralCarrier', 'CompletedOI', 'CarrierGeneralOIPlus', 'ImplementationLocality',
    'MinimalRepertoire', 'PositivePackage', 'MicroscopicReversibility', 'PositiveReachability',
    'StructuralClosure', 'SubstratumSource', 'SubstratumInterface', 'PhaseSource',
    'ReadWriteControl', 'DerivedQ3', 'LiftAudit', 'ExecSource', 'LiftSource', 'FlowEndpoint',
    'C5Discovery', 'StateMixingCoupling', 'PairFlowEquivalence', 'CoherentContinuumSource',
    'EmbeddedObservation', 'ReferenceExtension', 'SpectatorBridge', 'TypedCompletion',
    'TypedPositive', 'QuasilocalAlgebra', 'QuasilocalCharacterization', 'SecondOrderDrive',
    'JordanClassification', 'OperationalRigidity', 'PassiveObservation', 'PassiveIndependence',
    'PassiveQuotient',
]
DECL_RE = re.compile(
    r'^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected|partial|unsafe|nonrec)\s+)*'
    r'(axiom|opaque|structure|class|def|abbrev|inductive|instance|theorem|lemma)\b\s*'
    r'(?:inductive\s+)?([^\s:({\[⦃]*)')


def comment_state(lines):
    """in_comment_at_line_start and the comment-stripped text per line (nested /- -/, and --)."""
    out = []
    depth = 0
    for line in lines:
        start = depth
        buf = []
        i = 0
        while i < len(line):
            two = line[i:i + 2]
            if depth > 0:
                if two == '-/':
                    depth -= 1
                    i += 2
                    continue
                if two == '/-':
                    depth += 1
                    i += 2
                    continue
                i += 1
                continue
            if two == '--':
                break
            if two == '/-':
                depth += 1
                i += 2
                continue
            buf.append(line[i])
            i += 1
        out.append((''.join(buf), start > 0))
    return out


def sig_end(clean, idx):
    depth = 0
    for j in range(idx, min(len(clean), idx + 40)):
        s = clean[j][0]
        k = 0
        while k < len(s):
            c = s[k]
            if c in '([{⦃⟨':
                depth += 1
            elif c in ')]}⦄⟩':
                depth -= 1
            elif depth == 0 and s[k:k + 2] == ':=':
                return j
            elif depth == 0 and re.match(r'where\b', s[k:]) and (k == 0 or not (s[k - 1].isalnum() or s[k - 1] in '_.')):
                return j
            k += 1
    return min(len(clean), idx + 40) - 1


def doc_before(lines, idx):
    j = idx - 1
    while j >= 0 and (lines[j].strip() == '' or lines[j].lstrip().startswith('@[')
                      or re.match(r'^(variable|omit|include)\b.*\bin\s*$', lines[j].strip())):
        if lines[j].strip() == '':
            return []
        j -= 1
    if j < 0 or not lines[j].rstrip().endswith('-/'):
        return []
    end = j
    while j >= 0 and '/--' not in lines[j]:
        j -= 1
    if j < 0:
        return []
    return list(range(j, end + 1))


def main():
    ok1 = ok2 = False
    for mod in MODULES:
        with open(os.path.join(ROOT, mod + '.lean'), encoding='utf-8') as fh:
            lines = fh.read().split('\n')
        clean = comment_state(lines)
        for i in range(len(lines)):
            s, inc = clean[i]
            if inc:
                continue
            m = DECL_RE.match(s)
            if not m or m.group(1) == 'instance':
                continue
            kw, name = m.group(1), m.group(2)
            doc = doc_before(lines, i)
            head = False
            if doc:
                first = lines[doc[0]].split('/--', 1)[1].strip()
                head = first.startswith('**')
            end = sig_end(clean, i)
            print('=== %s.lean:%d %s %s%s' % (mod, i + 1, kw, name, '  HEADLINE' if head else ''))
            for d in doc:
                print('DOC %d: %s' % (d + 1, lines[d]))
            for k in range(i, end + 1):
                print('SIG %d: %s' % (k + 1, lines[k]))
            if mod == 'ReferenceExtension' and name == 'HasParallelReferenceExtension':
                ok1 = (doc and doc[0] + 1 == 444) and (i + 1 == 447) and (end + 1 >= 451)
            if mod == 'ReferenceExtension' and name == 'withSpectator':
                ok2 = (i + 1 == 422)
    print()
    print('CONTROL D4a (HasParallelReferenceExtension doc 444, sig 447-451): %s' % ('PASS' if ok1 else 'FAIL'))
    print('CONTROL D4b (withSpectator at 422): %s' % ('PASS' if ok2 else 'FAIL'))
    print('VERDICT: %s' % ('DUMP VALID' if (ok1 and ok2) else 'CONTROL FAILURE'))
    return 0 if (ok1 and ok2) else 1


if __name__ == '__main__':
    sys.exit(main())
