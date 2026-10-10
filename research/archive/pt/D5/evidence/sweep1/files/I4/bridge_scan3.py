#!/usr/bin/env python3
"""I4 bridge scan 3 -- the single-token level O (the K-infinity foundations) against M, H, G.
Run from pt/I4/ as:  python3 -I -B bridge_scan3.py > bridge_scan3.out 2> bridge_scan3.err

DECISION RULE (fixed before the first run):
 F1 Import graph as in bridge_scan.py (OIBridge/*.lean + root OIBridge.lean; comment-stripped imports).
 F2 Defining sites (verified verbatim, else CONTROL FAILURE): O: KInfFoundations.lean:264
    'structure ElementaryDrivability', KInfFoundations.lean:425 'def cyc3'; M: OperationalAssembly.lean:594;
    H: RouteB.lean:279, StructuralClosure.lean:180; G: TypedCompletion.lean:165, QuasilocalCharacterization.lean:168.
 F3 A module can state an X-O link iff it is or transitively imports an O-defining and an X-defining module.
    Listed per X; the in-scope I4 modules (I4MODS) that reach O are listed separately.
 F4 Controls: C1 CompositeDimension reaches KInfFoundations; C2 ReferenceExtension reaches
    OperationalAssembly; C3 the root reaches every defining module.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LM = os.path.normpath(os.path.join(HERE, '..', 'base', 'verification', 'lean-mathlib'))
DIR = os.path.join(LM, 'OIBridge')
SITES = {'O': [('KInfFoundations', 264, 'structure ElementaryDrivability'), ('KInfFoundations', 425, 'def cyc3')],
         'M': [('OperationalAssembly', 594, 'structure FiniteOperationalTheory')],
         'H': [('RouteB', 279, 'abbrev substratumTheory'), ('StructuralClosure', 180, 'def substratumClass')],
         'G': [('TypedCompletion', 165, 'structure TypedOperationalTheory'),
               ('QuasilocalCharacterization', 168, 'structure QuasilocalSystem')]}
I4MODS = ['GeneralCarrier', 'CompletedOI', 'CarrierGeneralOIPlus', 'ImplementationLocality', 'MinimalRepertoire',
          'PositivePackage', 'MicroscopicReversibility', 'PositiveReachability', 'StructuralClosure',
          'SubstratumSource', 'SubstratumInterface', 'PhaseSource', 'ReadWriteControl', 'DerivedQ3', 'LiftAudit',
          'ExecSource', 'LiftSource', 'FlowEndpoint', 'C5Discovery', 'StateMixingCoupling', 'PairFlowEquivalence',
          'CoherentContinuumSource', 'EmbeddedObservation', 'ReferenceExtension', 'SpectatorBridge',
          'TypedCompletion', 'TypedPositive', 'QuasilocalAlgebra', 'QuasilocalCharacterization',
          'SecondOrderDrive', 'JordanClassification', 'OperationalRigidity', 'PassiveObservation',
          'PassiveIndependence', 'PassiveQuotient']


def strip_imports(lines):
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
        mm = re.match(r'^\s*import\s+OIBridge\.(\S+)\s*$', ''.join(buf))
        if mm:
            out.append(mm.group(1))
    return sorted(set(out))


def main():
    mods = sorted(f[:-5] for f in os.listdir(DIR) if f.endswith('.lean'))
    raw = {}
    for m in mods:
        with open(os.path.join(DIR, m + '.lean'), encoding='utf-8') as fh:
            raw[m] = fh.read().split('\n')
    with open(os.path.join(LM, 'OIBridge.lean'), encoding='utf-8') as fh:
        raw['(root)OIBridge'] = fh.read().split('\n')
    mods.append('(root)OIBridge')
    imp = {m: strip_imports(raw[m]) for m in mods}
    clo = {}

    def close(m):
        if m in clo:
            return clo[m]
        clo[m] = set()
        acc = set()
        for d in imp.get(m, []):
            acc.add(d)
            acc |= close(d)
        clo[m] = acc
        return acc
    for m in mods:
        close(m)
    site_ok = all(txt in raw[mod][ln - 1] for lev in SITES for (mod, ln, txt) in SITES[lev])
    defm = {lev: sorted({s[0] for s in SITES[lev]}) for lev in SITES}

    def reaches(m, lev):
        return any(d == m or d in clo[m] for d in defm[lev])
    c1 = 'KInfFoundations' in clo['CompositeDimension']
    c2 = 'OperationalAssembly' in clo['ReferenceExtension']
    c3 = all(reaches('(root)OIBridge', lev) for lev in SITES)
    print('## CONTROLS')
    for lab, ok in [('sites found', site_ok), ('C1 CompositeDimension reaches KInfFoundations', c1),
                    ('C2 ReferenceExtension reaches OperationalAssembly', c2), ('C3 root reaches all levels', c3)]:
        print('%s: %s' % ('PASS' if ok else 'FAIL', lab))
    print()
    ro = [m for m in mods if reaches(m, 'O')]
    print('modules reaching O definitions: %d' % len(ro))
    for lev in ('M', 'H', 'G'):
        both = [m for m in mods if reaches(m, 'O') and reaches(m, lev)]
        print('modules that can state an %s-O link (F3): %d : %s' % (lev, len(both), ' '.join(both)))
    print('I4 modules reaching O: %s' % (' '.join(m for m in I4MODS if reaches(m, 'O')) or '(none)'))
    print('I4 modules NOT reaching M: %s' % (' '.join(m for m in I4MODS if not reaches(m, 'M')) or '(none)'))
    ok = site_ok and c1 and c2 and c3
    print('VERDICT: %s' % ('CONTROL FAILURE' if not ok else 'SCAN VALID'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
