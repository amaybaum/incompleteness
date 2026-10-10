#!/usr/bin/env python3
"""I4 inventory renderer -- builds INVENTORY.md text from records.txt, quoting every kernel statement
verbatim from pt/base at L (docstring + signature) and every Markdown statement verbatim by line range.

Run from pt/I4/ as:  python3 -I -B render_inventory.py > render_inventory.out 2> render_inventory.err
INVENTORY.md is then a byte copy of render_inventory.out (recorded in NOTES.md and RESULT.md section 4).

DECISION RULE (fixed before the first run):
 V1 records.txt: one record per non-comment line, 12 fields separated by ' ¦ ' (U+00A6 with spaces):
    id, src, name, kind, status, level, depends_on, yields, bridge, bearing, flag, note.
    src is 'lean:<Module>.lean:<line>' (OIBridge/ under ../base/verification/lean-mathlib) or
    'md:<path under ../base or ..>:<L1>-<L2>'.
 V2 Kernel quote: the docstring ending just above the declaration (attributes / 'variable ... in' /
    'omit ... in' lines skipped) and the declaration: for theorem/lemma up to the line holding the first
    bracket-depth-0 ':=' ; for other keywords the whole declaration (to the line before the first blank
    line or column-0 line starting a docstring, '#', end, section, namespace, variable, open, omit, '@['
    or a declaration keyword; at most 60 lines).
 V3 Control (per record): the declaration line of a lean src must contain the record's name as a whole
    word after the keyword; an md src's range must be within the file.  Any failure: the record is
    printed with 'SOURCE CHECK FAILED' and the final VERDICT line reads CONTROL FAILURE.
 V4 Codes expanded verbatim from the CODES table below (bridge/bearing/status shorthands).
 V5 Countercontrol: a synthetic record whose src line does not hold its name must fail V3 (run on a
    deliberately wrong pair, ReferenceExtension.lean:422 with name HasParallelReferenceExtension).
 V6 Deterministic output; ids must be unique and of the form I4.<n>; no clock values.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, '..', 'base'))
PT = os.path.normpath(os.path.join(HERE, '..'))
OIB = os.path.join(BASE, 'verification', 'lean-mathlib', 'OIBridge')

CODES = {
    'NB-M': ('none at L. `bridge_scan.out` (rule B3): the only module that imports both the pair-level '
             'definitions (CompositeDimension.lean:97 `W`, :198 `actT`, :201 `actC`, :775 `cnot`; K2Guard.lean:95 '
             '`CandidateCone`) and the matrix-level carrier (OperationalAssembly.lean:594 `FiniteOperationalTheory`) '
             'is the root aggregator `OIBridge.lean`, which states no declaration mentioning a pair token '
             '(0 bridge-candidate lines); `bridge_scan3.out`: no module but the root reaches both M and the '
             'single-token level O (KInfFoundations.lean:264 `ElementaryDrivability`, :425 `cyc3`).'),
    'NB-H': ('none at L. `bridge_scan.out` (B3, H = RouteB.lean:279 `substratumTheory`, StructuralClosure.lean:180 '
             '`substratumClass`): only the root aggregator `OIBridge.lean` reaches both H and the pair carrier, and '
             'it states no pair-token declaration; `bridge_scan3.out`: no H-O link module but the root.'),
    'NB-HP': ('none at L. PassiveQuotient.lean is in the import closure of the pair carrier (CompositeDimension -> '
              'TransitiveBody -> CompletionAction -> StageCompletion -> OrbitNormalization -> OrbitGeneration -> '
              'KInfFoundations -> CoherentExtension -> ControlledQuotient -> PassiveQuotient, `bridge_scan2.out`), but '
              'no pair-level module (`bridge_scan2.out`, 12 modules) and no module of that single-token chain '
              '(`bridge_scan4.out`, 23 modules) uses any of the 85 names declared in PassiveQuotient, '
              'ControlledQuotient or ObservabilityQuotient, and none opens or qualifies those namespaces (NOTES N5).'),
    'NB-G': ('none at L. `bridge_scan.out` (B3, G = TypedCompletion.lean:165 `TypedOperationalTheory`, '
             'QuasilocalCharacterization.lean:168 `QuasilocalSystem`): only the root aggregator `OIBridge.lean` '
             'reaches both G and the pair carrier, and it states no pair-token declaration; `bridge_scan3.out`: no '
             'G-O link module but the root.'),
    'none': 'none at L (no bridge theorem at L; see `bridge`).',
    'K': 'proved [K] (kernel theorem of the certified build at L)',
    'DNA': 'do not assume',
    '-': '-',
}
DECL = re.compile(r'^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected|partial|unsafe|nonrec)\s+)*'
                  r'(axiom|opaque|structure|class|def|abbrev|inductive|instance|theorem|lemma)\b\s*'
                  r'(?:inductive\s+)?([^\s:({\[⦃]*)')
STOP = re.compile(r'^(/--|/-|#|end\b|section\b|namespace\b|variable\b|open\b|omit\b|@\[|'
                  r'(?:(?:noncomputable|private|protected|partial|unsafe|nonrec)\s+)*'
                  r'(axiom|opaque|structure|class|def|abbrev|inductive|instance|theorem|lemma)\b)')


def expand(v):
    out = []
    for part in v.split(' ;; '):
        out.append(CODES.get(part.strip(), part.strip()))
    return ' '.join(out)


def strip_line(s):
    i = s.find('--')
    return s if i < 0 else s[:i]


def sig_end(lines, idx):
    depth = 0
    for j in range(idx, min(len(lines), idx + 40)):
        s = strip_line(lines[j])
        for k, c in enumerate(s):
            if c in '([{⦃⟨':
                depth += 1
            elif c in ')]}⦄⟩':
                depth -= 1
            elif depth == 0 and s[k:k + 2] == ':=':
                return j
    return min(len(lines), idx + 40) - 1


def body_end(lines, idx):
    for j in range(idx + 1, min(len(lines), idx + 60)):
        if lines[j].strip() == '' or STOP.match(lines[j]):
            return j - 1
    return min(len(lines), idx + 60) - 1


def doc_before(lines, idx):
    j = idx - 1
    while j >= 0 and (lines[j].lstrip().startswith('@[')
                      or re.match(r'^(variable|omit|include)\b.*\bin\s*$', lines[j].strip())):
        j -= 1
    if j < 0 or not lines[j].rstrip().endswith('-/'):
        return []
    end = j
    while j >= 0 and '/--' not in lines[j]:
        j -= 1
    return list(range(j, end + 1)) if j >= 0 else []


def lean_quote(module_file, line, name):
    path = os.path.join(OIB, module_file)
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    i = line - 1
    if i < 0 or i >= len(lines):
        return False, ['(line out of range)'], None
    m = DECL.match(lines[i])
    ok = bool(m) and m.group(2).split('.')[-1] == name.split('.')[-1]
    kw = m.group(1) if m else '?'
    end = sig_end(lines, i) if kw in ('theorem', 'lemma') else body_end(lines, i)
    out = [lines[d] for d in doc_before(lines, i)] + [lines[k] for k in range(i, end + 1)]
    return ok, out, (i + 1, end + 1)


def md_quote(rel, l1, l2):
    for root in (BASE, PT):
        path = os.path.join(root, rel)
        if os.path.isfile(path):
            with open(path, encoding='utf-8') as fh:
                lines = fh.read().split('\n')
            if 1 <= l1 <= l2 <= len(lines):
                return True, lines[l1 - 1:l2], path
            return False, ['(range out of file)'], path
    return False, ['(file not found)'], None


def main():
    recs = []
    with open(os.path.join(HERE, 'records.txt'), encoding='utf-8') as fh:
        for n, raw in enumerate(fh.read().split('\n'), 1):
            if not raw.strip() or raw.startswith('#'):
                continue
            f = [x.strip() for x in raw.split(' ¦ ')]
            if len(f) != 12:
                print('RECORD FORMAT ERROR at records.txt:%d (%d fields)' % (n, len(f)))
                print('VERDICT: CONTROL FAILURE')
                return 1
            recs.append((n, f))
    ids = [f[0] for _, f in recs]
    uniq = len(ids) == len(set(ids)) and all(re.fullmatch(r'I4\.\d+', x) for x in ids)
    cc_ok, _, _ = lean_quote('ReferenceExtension.lean', 422, 'HasParallelReferenceExtension')
    countercontrol = not cc_ok
    fails = 0
    body = []
    for n, f in recs:
        rid, src, name, kind, status, level, dep, yields, bridge, bearing, flag, note = f
        if src.startswith('lean:'):
            _, mf, ln = src.split(':')
            ok, q, rng = lean_quote(mf, int(ln), name)
            prov = '`verification/lean-mathlib/OIBridge/%s:%s`' % (mf, ln) + (
                ' (quoted lines %d-%d)' % rng if rng else '')
            lang = 'lean'
        else:
            _, rel, rr = src.split(':')
            l1, l2 = (int(x) for x in rr.split('-'))
            ok, q, path = md_quote(rel, l1, l2)
            prov = '`%s:%d-%d`' % (rel, l1, l2)
            lang = 'text'
        if not ok:
            fails += 1
        body.append('### %s — `%s`%s' % (rid, name, '' if ok else '  SOURCE CHECK FAILED'))
        body.append('')
        body.append('- **kind:** %s' % kind)
        body.append('- **provenance:** %s' % prov)
        body.append('- **statement (verbatim):**')
        body.append('')
        body.append('```' + lang)
        body.extend(q)
        body.append('```')
        body.append('')
        body.append('- **status:** %s' % expand(status))
        body.append('- **level:** %s' % level)
        body.append('- **depends_on:** %s' % expand(dep))
        body.append('- **yields:** %s' % expand(yields))
        body.append('- **bridge:** %s' % expand(bridge))
        body.append('- **bearing:** %s' % expand(bearing))
        body.append('- **flag:** %s' % expand(flag))
        if note.strip() and note.strip() != '-':
            body.append('- **note:** %s' % expand(note))
        body.append('')
    with open(os.path.join(HERE, 'INVENTORY-HEADER.md'), encoding='utf-8') as fh:
        header = fh.read().rstrip('\n').split('\n')
    for h in header:
        print(h)
    print('')
    for b in body:
        print(b)
    print('***')
    print('')
    print('Render controls: records %d; ids unique and well-formed: %s; source checks failed: %d; '
          'countercontrol (wrong name at ReferenceExtension.lean:422 must fail): %s.'
          % (len(recs), 'yes' if uniq else 'NO', fails, 'PASS' if countercontrol else 'FAIL'))
    ok = uniq and fails == 0 and countercontrol
    print('')
    print('VERDICT: %s' % ('INVENTORY RENDERED (all controls pass)' if ok else 'CONTROL FAILURE'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
