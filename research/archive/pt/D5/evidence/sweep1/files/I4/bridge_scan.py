#!/usr/bin/env python3
"""I4 bridge scan -- which kernel modules at L can state, and which do state, a theorem relating the
matrix level M (FiniteOperationalTheory), the substratum objects H, or the general carriers G to the
field-neutral pair level P (W d, actC/actT, cnot, prodState, maxCone, CandidateCone).

Run from pt/I4/ as:  python3 -I -B bridge_scan.py > bridge_scan.out 2> bridge_scan.err

DECISION RULE (fixed before the first run):
 B1 Modules: every OIBridge/*.lean file plus the root OIBridge.lean under ../base/verification/lean-mathlib.
    Edges: lines 'import OIBridge.<X>' (comment-stripped).  Closure: transitive imports.
 B2 Defining sites (each must be found verbatim at the stated line, else CONTROL FAILURE):
    P: CompositeDimension.lean:97 'abbrev W (d : ℕ)', :198 'def actT', :201 'def actC', :775 'def cnot',
       K2Guard.lean:95 'def CandidateCone';
    M: OperationalAssembly.lean:594 'structure FiniteOperationalTheory';
    H: RouteB.lean:279 'abbrev substratumTheory', StructuralClosure.lean:180 'def substratumClass';
    G: TypedCompletion.lean:165 'structure TypedOperationalTheory',
       QuasilocalCharacterization.lean:168 'structure QuasilocalSystem'.
 B3 A module CAN STATE an X-P bridge iff it is, or transitively imports, a P-defining module and an
    X-defining module (X in M, H, G).  Lean admits no other way to mention both definitions.
 B4 For each module that can state an X-P bridge, every comment-stripped line mentioning a P token
    (word-boundary: actC actT prodState maxCone CandidateCone NativeGate IsNot Entangling cnot eball,
    or the patterns 'W 3', 'W d', 'W (') is listed, with whether the same declaration block (from the
    preceding column-0 declaration line to the next) also mentions an M/H/G token (FiniteOperationalTheory
    availExt withSpectator HasParallelReferenceExtension ObservationalIndependence ImplementationLocality
    StructurallyClosed LayerFlowExecutable substratumTheory substratumClass ImplementationClass
    TypedOperationalTheory QuasilocalSystem Quasilocal).  A block with both is a BRIDGE CANDIDATE.
 B5 Controls: C1 K2Guard transitively imports CompositeDimension (it states CandidateCone on W 3);
    C2 ReferenceExtension transitively imports OperationalAssembly (it uses FiniteOperationalTheory);
    C3 the import graph is acyclic; C4 the co-occurrence detector flags a synthetic block that mentions
    'actC' and 'FiniteOperationalTheory' and does not flag one that mentions only 'actC'.
 B6 Output deterministic (sorted); no clock values.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LM = os.path.normpath(os.path.join(HERE, '..', 'base', 'verification', 'lean-mathlib'))
DIR = os.path.join(LM, 'OIBridge')

SITES = {
    'P': [('CompositeDimension', 97, 'abbrev W (d : ℕ)'), ('CompositeDimension', 198, 'def actT'),
          ('CompositeDimension', 201, 'def actC'), ('CompositeDimension', 775, 'def cnot'),
          ('K2Guard', 95, 'def CandidateCone')],
    'M': [('OperationalAssembly', 594, 'structure FiniteOperationalTheory')],
    'H': [('RouteB', 279, 'abbrev substratumTheory'), ('StructuralClosure', 180, 'def substratumClass')],
    'G': [('TypedCompletion', 165, 'structure TypedOperationalTheory'),
          ('QuasilocalCharacterization', 168, 'structure QuasilocalSystem')],
}
P_TOK = re.compile(r'(?<![\w.])(actC|actT|prodState|maxCone|CandidateCone|NativeGate|IsNot|Entangling|cnot|eball)(?![\w])'
                   r'|(?<![\w.])W (3|d|\()')
X_TOK = re.compile(r'(?<![\w])(FiniteOperationalTheory|availExt|withSpectator|HasParallelReferenceExtension|'
                   r'ObservationalIndependence|ImplementationLocality|StructurallyClosed|LayerFlowExecutable|'
                   r'substratumTheory|substratumClass|ImplementationClass|TypedOperationalTheory|QuasilocalSystem|'
                   r'Quasilocal)(?![\w])')
DECL0 = re.compile(r'^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected|partial|unsafe|nonrec)\s+)*'
                   r'(axiom|opaque|structure|class|def|abbrev|inductive|instance|theorem|lemma)\b')


def strip(lines):
    out, depth = [], 0
    for line in lines:
        buf, i = [], 0
        while i < len(line):
            two = line[i:i + 2]
            if depth > 0:
                if two == '-/':
                    depth -= 1; i += 2; continue
                if two == '/-':
                    depth += 1; i += 2; continue
                i += 1; continue
            if two == '--':
                break
            if two == '/-':
                depth += 1; i += 2; continue
            buf.append(line[i]); i += 1
        out.append(''.join(buf))
    return out


def blocks(clean):
    """Map each line index to its declaration block (start index of the nearest preceding column-0 decl)."""
    owner, cur = [], -1
    for i, s in enumerate(clean):
        if DECL0.match(s):
            cur = i
        owner.append(cur)
    return owner


def cooccur(block_text):
    return bool(P_TOK.search(block_text)) and bool(X_TOK.search(block_text))


def main():
    files = sorted(f[:-5] for f in os.listdir(DIR) if f.endswith('.lean'))
    texts = {}
    for f in files:
        with open(os.path.join(DIR, f + '.lean'), encoding='utf-8') as fh:
            texts[f] = fh.read().split('\n')
    with open(os.path.join(LM, 'OIBridge.lean'), encoding='utf-8') as fh:
        texts['(root)OIBridge'] = fh.read().split('\n')
    mods = files + ['(root)OIBridge']
    clean = {m: strip(texts[m]) for m in mods}
    imp = {}
    for m in mods:
        imp[m] = sorted({mm.group(1) for s in clean[m] for mm in [re.match(r'^\s*import\s+OIBridge\.(\S+)\s*$', s)] if mm})
    # closure (iterative DFS) and cycle check
    closure, state, cyc = {}, {}, []

    def visit(m, stack):
        if state.get(m) == 2:
            return closure[m]
        if state.get(m) == 1:
            cyc.append(stack + [m])
            return set()
        state[m] = 1
        acc = set()
        for d in imp.get(m, []):
            acc.add(d)
            acc |= visit(d, stack + [m])
        state[m] = 2
        closure[m] = acc
        return acc
    for m in mods:
        visit(m, [])
    # controls on sites
    site_ok = True
    print('## DEFINING SITES (B2)')
    for lev in ('P', 'M', 'H', 'G'):
        for (mod, ln, txt) in SITES[lev]:
            line = texts[mod][ln - 1] if ln - 1 < len(texts[mod]) else ''
            ok = txt in line
            site_ok = site_ok and ok
            print('%s %s %s.lean:%d %r' % ('FOUND' if ok else 'MISSING', lev, mod, ln, line.strip()))
    defmods = {lev: sorted({s[0] for s in SITES[lev]}) for lev in SITES}

    def reaches(m, lev):
        return any(d == m or d in closure[m] for d in defmods[lev])
    c1 = 'CompositeDimension' in closure['K2Guard']
    c2 = 'OperationalAssembly' in closure['ReferenceExtension']
    c3 = not cyc
    c4 = cooccur('theorem t (T : FiniteOperationalTheory A) : actC N = actC N') and not cooccur('theorem t : actC N = actC N')
    print()
    print('## CONTROLS')
    for label, ok in [('sites found (B2)', site_ok), ('C1 K2Guard reaches CompositeDimension', c1),
                      ('C2 ReferenceExtension reaches OperationalAssembly', c2), ('C3 acyclic', c3),
                      ('C4 co-occurrence detector', c4)]:
        print('%s: %s' % ('PASS' if ok else 'FAIL', label))
    print()
    print('## MODULE COUNTS')
    print('modules scanned: %d (OIBridge/*.lean %d + root)' % (len(mods), len(files)))
    for lev in ('P', 'M', 'H', 'G'):
        r = [m for m in mods if reaches(m, lev)]
        print('modules reaching %s definitions: %d' % (lev, len(r)))
    print()
    print('## P-DEFINING MODULES: their own OIBridge imports (closure)')
    for m in defmods['P']:
        print('%s imports (transitively, %d): %s' % (m, len(closure[m]), ' '.join(sorted(closure[m]))))
    print()
    anyb = False
    for lev in ('M', 'H', 'G'):
        both = [m for m in mods if reaches(m, 'P') and reaches(m, lev)]
        print('## MODULES THAT CAN STATE A %s-P BRIDGE (B3): %d' % (lev, len(both)))
        for m in both:
            print('  ' + m)
        print()
    print('## P-TOKEN LINES IN MODULES THAT CAN STATE ANY BRIDGE (B4), with co-occurrence in the same block')
    cand = sorted({m for m in mods for lev in ('M', 'H', 'G') if reaches(m, 'P') and reaches(m, lev)})
    nb = 0
    for m in cand:
        own = blocks(clean[m])
        for i, s in enumerate(clean[m]):
            if P_TOK.search(s):
                st = own[i]
                en = i
                while en + 1 < len(clean[m]) and own[en + 1] == st:
                    en += 1
                blk = '\n'.join(clean[m][max(st, 0):en + 1]) if st >= 0 else s
                flag = cooccur(blk)
                nb += 1 if flag else 0
                anyb = anyb or flag
                print('%s %s.lean:%d | block@%d | %s' % ('BRIDGE-CANDIDATE' if flag else 'p-only', m, i + 1,
                      st + 1, s.strip()[:160]))
    print()
    print('bridge-candidate lines: %d' % nb)
    ok = site_ok and c1 and c2 and c3 and c4
    if not ok:
        print('VERDICT: CONTROL FAILURE (scan void)')
        return 1
    print('VERDICT: %s' % ('BRIDGE CANDIDATES PRESENT (inspect listed blocks)' if anyb else
                           'NO MODULE STATES A DECLARATION MENTIONING BOTH A P TOKEN AND AN M/H/G TOKEN'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
