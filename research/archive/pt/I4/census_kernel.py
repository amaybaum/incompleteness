#!/usr/bin/env python3
"""I4 kernel census -- coverage control (a) of PROTOCOL-STAGE6.md, thread I4.

Run from pt/I4/ as:  python3 -I -B census_kernel.py > census_kernel.out 2> census_kernel.err

DECISION RULE (fixed before the first run; rules, not expected numbers):
 R1 Scope: the modules in MODULES (the I4 partition of PROTOCOL-STAGE6.md, plus the related passive
    modules PassiveIndependence.lean and PassiveQuotient.lean), read from ../base at L, read-only.
 R2 Comments: text inside /- ... -/ (nested; docstrings included) and after -- is ignored.
 R3 A declaration is a non-comment line that starts at column 0 with optional attributes @[...] and
    optional modifiers (noncomputable, private, protected, partial, unsafe, nonrec) followed by one of
    axiom, opaque, structure, class, def, abbrev, inductive, instance, theorem, lemma.
 R4 Header = text from the keyword to the first bracket-depth-0 token ':=' or 'where' or a line
    starting with '|' (comments stripped).  Declared type = header text after the FIRST depth-0
    ':' (binder colons sit inside brackets).  'Prop-valued' iff the declared type is exactly 'Prop'.
    'predicate-valued' iff the declared type ends with '-> Prop' / '→ Prop' (a family of Props).
 R5 Census (a) population = every axiom + every opaque + every class + every structure, def, abbrev
    or inductive that is Prop-valued or predicate-valued.  Everything else is listed only as counts
    (theorems/lemmas are listed by name as an auxiliary list for the inventory).
 R6 Controls (all must pass, else the VERDICT line reads CONTROL FAILURE and the census is void):
    C1 positive:  HasParallelReferenceExtension (ReferenceExtension.lean) is a census entry, Prop-valued.
    C2 negative:  withSpectator (ReferenceExtension.lean) is a def that is NOT a census entry.
    C3 positive:  StructurallyClosed (StructuralClosure.lean) is a census entry (structure, Prop-valued).
    C4 strict grep: every line matched by the protocol's strict regex '^(axiom|opaque|structure|class|def) '
       outside comments is a parsed declaration; lines it matches inside comments are counted separately.
    C5 negative:  a theorem (control_not_implies_parallelReferenceExtension) is NOT a census entry.
 R7 Output deterministic: module order as in MODULES, then line order; no clock values in stdout.
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
STRICT_RE = re.compile(r'^(axiom|opaque|structure|class|def) ')


def strip_comments(lines):
    """Return list of (line_without_comments, in_comment_at_line_start) per line (rule R2)."""
    out = []
    depth = 0
    for line in lines:
        start_depth = depth
        buf = []
        i = 0
        n = len(line)
        while i < n:
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
        out.append((''.join(buf), start_depth > 0))
    return out


def header_of(clean, idx):
    """Rule R4: accumulate the header from line idx until ':=' / 'where' / leading '|' at depth 0."""
    text = []
    depth = 0
    first = True
    for j in range(idx, len(clean)):
        s = clean[j][0]
        if not first and s.lstrip().startswith('|') and depth == 0:
            break
        k = 0
        while k < len(s):
            c = s[k]
            if c in '([{⦃⟨':
                depth += 1
            elif c in ')]}⦄⟩':
                depth -= 1
            elif depth == 0 and s[k:k + 2] == ':=':
                text.append(s[:k])
                return ' '.join(' '.join(text).split())
            elif depth == 0 and re.match(r'where\b', s[k:]) and (k == 0 or not (s[k - 1].isalnum() or s[k - 1] in '_.')):
                text.append(s[:k])
                return ' '.join(' '.join(text).split())
            k += 1
        text.append(s)
        first = False
        if j - idx > 60:
            break
    return ' '.join(' '.join(text).split())


def declared_type(header):
    depth = 0
    for k, c in enumerate(header):
        if c in '([{⦃⟨':
            depth += 1
        elif c in ')]}⦄⟩':
            depth -= 1
        elif c == ':' and depth == 0 and header[k:k + 2] != ':=':
            return header[k + 1:].strip()
    return None


def main():
    entries = []          # census (a)
    others = []           # non-census declarations (kind, module, line, name)
    strict_lines = []     # (module, line, in_comment)
    per_module = {}
    for mod in MODULES:
        path = os.path.join(ROOT, mod + '.lean')
        with open(path, encoding='utf-8') as fh:
            lines = fh.read().split('\n')
        clean = strip_comments(lines)
        counts = {'census': 0, 'theorem': 0, 'nonprop_def': 0, 'nonprop_structure': 0,
                  'instance': 0, 'other': 0, 'strict_grep': 0, 'strict_grep_in_comment': 0}
        for i, raw in enumerate(lines):
            s, in_comment = clean[i]
            if STRICT_RE.match(raw):
                if in_comment:
                    counts['strict_grep_in_comment'] += 1
                    strict_lines.append((mod, i + 1, True))
                else:
                    counts['strict_grep'] += 1
                    strict_lines.append((mod, i + 1, False))
            if in_comment:
                continue
            m = DECL_RE.match(s)
            if not m:
                continue
            kw, name = m.group(1), m.group(2)
            if raw.lstrip().startswith('class inductive') or re.match(r'^(?:@\[[^\]]*\]\s*)*class\s+inductive', s):
                kw = 'class'
            if kw in ('theorem', 'lemma'):
                counts['theorem'] += 1
                others.append(('theorem', mod, i + 1, name, ''))
                continue
            if kw == 'instance':
                counts['instance'] += 1
                others.append(('instance', mod, i + 1, name, ''))
                continue
            header = header_of(clean, i)
            ty = declared_type(header)
            tyn = (ty or '').replace('->', '→').strip()
            prop = (tyn == 'Prop')
            pred = (not prop) and tyn.endswith('→ Prop')
            if kw in ('axiom', 'opaque', 'class') or prop or pred:
                tag = 'Prop' if prop else ('predicate' if pred else ('type:' + (tyn if tyn else '(none)')))
                entries.append((mod, i + 1, kw, name, tag, header))
                counts['census'] += 1
            else:
                if kw == 'structure':
                    counts['nonprop_structure'] += 1
                elif kw in ('def', 'abbrev'):
                    counts['nonprop_def'] += 1
                else:
                    counts['other'] += 1
                others.append((kw, mod, i + 1, name, tyn))
        per_module[mod] = counts

    # controls
    def find(mod, name, pool):
        return [e for e in pool if e[0] == mod and e[3] == name]

    c1 = any(e[4] == 'Prop' for e in find('ReferenceExtension', 'HasParallelReferenceExtension', entries))
    c2 = (not find('ReferenceExtension', 'withSpectator', entries)) and any(
        o[1] == 'ReferenceExtension' and o[3] == 'withSpectator' and o[0] == 'def' for o in others)
    c3 = any(e[2] == 'structure' and e[4] == 'Prop' for e in find('StructuralClosure', 'StructurallyClosed', entries))
    parsed = {(e[0], e[1]) for e in entries} | {(o[1], o[2]) for o in others}
    c4_missing = [(m, ln) for (m, ln, inc) in strict_lines if not inc and (m, ln) not in parsed]
    c4 = not c4_missing
    c5 = not find('ReferenceExtension', 'control_not_implies_parallelReferenceExtension', entries)
    controls = [('C1 HasParallelReferenceExtension is a Prop census entry', c1),
                ('C2 withSpectator is a def and not a census entry', c2),
                ('C3 StructurallyClosed is a Prop structure census entry', c3),
                ('C4 every strict-grep hit outside comments is parsed (missing=%d)' % len(c4_missing), c4),
                ('C5 a theorem is not a census entry', c5)]

    print('# I4 kernel census (a) -- modules: %d' % len(MODULES))
    print('# root: pt/base/verification/lean-mathlib/OIBridge (L = 9f9f8257)')
    print()
    print('## CONTROLS')
    for label, ok in controls:
        print('%s: %s' % ('PASS' if ok else 'FAIL', label))
    for m, ln in c4_missing:
        print('  C4 missing: %s.lean:%d' % (m, ln))
    print()
    print('## PER-MODULE COUNTS (census = census (a) entries)')
    print('module | census | theorems | nonprop_def | nonprop_structure | instance | other | strict_grep | strict_grep_in_comment')
    tot = {}
    for mod in MODULES:
        c = per_module[mod]
        for k, v in c.items():
            tot[k] = tot.get(k, 0) + v
        print('%s | %d | %d | %d | %d | %d | %d | %d | %d' % (mod, c['census'], c['theorem'], c['nonprop_def'],
              c['nonprop_structure'], c['instance'], c['other'], c['strict_grep'], c['strict_grep_in_comment']))
    print('TOTAL | %d | %d | %d | %d | %d | %d | %d | %d' % (tot['census'], tot['theorem'], tot['nonprop_def'],
          tot['nonprop_structure'], tot['instance'], tot['other'], tot['strict_grep'], tot['strict_grep_in_comment']))
    print()
    print('## CENSUS (a) ENTRIES: module.lean:line | keyword | name | type-class | header')
    for (mod, ln, kw, name, tag, header) in entries:
        h = header if len(header) <= 300 else header[:297] + '...'
        print('%s.lean:%d | %s | %s | %s | %s' % (mod, ln, kw, name, tag, h))
    print()
    print('## NON-CENSUS DEFINITIONS (def/abbrev/structure/inductive not Prop-valued): module.lean:line | keyword | name | declared type')
    for (kw, mod, ln, name, tyn) in others:
        if kw in ('theorem', 'instance'):
            continue
        t = tyn if len(tyn) <= 160 else tyn[:157] + '...'
        print('%s.lean:%d | %s | %s | %s' % (mod, ln, kw, name, t if t else '(no type ascription)'))
    print()
    print('## THEOREMS (auxiliary list): module.lean:line | name')
    for (kw, mod, ln, name, _) in others:
        if kw == 'theorem':
            print('%s.lean:%d | %s' % (mod, ln, name))
    print()
    ok = all(v for _, v in controls)
    print('VERDICT: %s' % ('CENSUS VALID (all controls pass)' if ok else 'CONTROL FAILURE (census void)'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
