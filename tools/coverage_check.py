#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""coverage_check.py — the meta-check on the proof-coverage ledger.

The ledger's purpose is to make one failure mode impossible: a proof added to the manuscript and
then simply never wired to anything. A ledger that is itself unchecked cannot do that — it decays
into a list of intentions. So every claim the ledger makes is verified here against the tree.

WHAT IS ENFORCED, and each rule exists because the corresponding lie is easy to tell:

  1. COMPLETENESS. Every canonical statement the census finds has a ledger entry, and every ledger
     entry corresponds to a canonical statement. A result added to a paper without a ledger row
     fails the gate.
  2. FRESHNESS. Each entry's fingerprint matches the manuscript statement it names. Editing a
     statement moves its fingerprint, so an entry certifying a sentence the manuscript no longer
     contains is caught rather than inherited.
  3. THE CHECKERS EXIST. Every referenced probe file and Lean file is present, and every named
     Lean declaration actually appears in the file named. A ledger may not point at a theorem that
     was renamed or never written.
  4. NAMED MAPPINGS ARE FALSIFIABLE. A check recorded with basis `named` carries the exact string
     by which the checker names its target, and that string must appear in the checker. Attribution
     by wishful reading is what this rule is against; a mapping that cannot survive it must be
     recorded as `section` instead, which claims less.
  5. THE LEAN IS ACTUALLY GATED. A Mathlib-side module is only checked by CI if the bridge
     library's root imports it. An unimported module is never built, and a theorem in it certifies
     nothing.
  6. LEVELS MEAN WHAT THEY SAY. K3/K2/K1 require at least one Lean check; P requires at least one
     probe; GAP must have neither claimed. AND K3 REQUIRES AN EMPTY `delta`: a recorded gap between
     the manuscript statement and the formal statement is exactly the definition of not-K3, so
     "there is some related Lean theorem" cannot be filed as an exact formalization.
  7. NOTHING IS SILENTLY DROPPED. Checkers that certify reasoning carrying no bold-headed
     statement, and research-layer results that deliberately do not propagate, are listed in
     `unattached` with what they certify — so the census gap is visible rather than invisible.

Usage:
    python3 tools/coverage_check.py            # gate mode: enforce, then report the baseline
    python3 tools/coverage_check.py --report   # the baseline table only
"""
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(ROOT, 'verification', 'coverage', 'LEDGER.json')
BRIDGE_ROOT = os.path.join(ROOT, 'verification', 'lean-mathlib', 'OIBridge.lean')
WORKFLOW = os.path.join(ROOT, '.github', 'workflows', 'verify.yml')

SCORED = ('K3', 'K2', 'K1', 'P', 'GAP')
UNSCORED = ('DEF', 'SUM', 'MIRROR')
NEEDS_LEAN = ('K3', 'K2', 'K1')

FAILURES = []


def fail(msg):
    FAILURES.append(msg)


def census():
    r = subprocess.run([sys.executable, os.path.join('tools', 'proof_census.py'), '--json'],
                       cwd=ROOT, capture_output=True, text=True, timeout=600)
    if r.returncode != 0:
        raise SystemExit('census failed:\n' + r.stderr[-2000:])
    return {row['id']: row for row in json.loads(r.stdout)}


def is_gated(path, txt):
    """Does CI actually run this probe?

    The workflow names the two families differently: the foundations job lists `<name>_probes` and
    the layer job lists a bare `<name>` which it expands to `<name>_probe.py`. Matching only the
    first form silently reported every layer probe as ungated, which is the opposite of the truth
    and exactly the kind of quiet miscount this file exists to prevent. Both forms are tried.
    """
    base = os.path.splitext(os.path.basename(path))[0]
    cands = {base}
    if base.endswith('_probe'):
        cands.add(base[:-len('_probe')])
    return any(re.search(r'(?<![A-Za-z0-9_])' + re.escape(c) + r'(?![A-Za-z0-9_])', txt)
               for c in cands)


def main():
    if not os.path.exists(LEDGER):
        raise SystemExit('coverage_check: verification/coverage/LEDGER.json is missing')
    led = json.load(open(LEDGER, encoding='utf-8'))
    cen = census()
    entries = {e['id']: e for e in led['entries']}

    # 1. completeness, both directions
    for cid in sorted(set(cen) - set(entries)):
        fail(f'canonical statement has NO ledger entry: {cid} ({cen[cid]["paper"]}:'
             f'{cen[cid]["line"]})')
    for eid in sorted(set(entries) - set(cen)):
        fail(f'ledger entry names no canonical statement: {eid}')

    # 2. freshness
    for eid, e in sorted(entries.items()):
        c = cen.get(eid)
        if c and c['fingerprint'] != e['fingerprint']:
            fail(f'STALE entry {eid}: the manuscript statement has changed '
                 f'({e["fingerprint"]} -> {c["fingerprint"]}); re-read it and re-affirm the '
                 f'mapping, the level and the delta')

    # 3-6. the checks themselves
    lean_cache = {}
    for eid, e in sorted(entries.items()):
        for field in ('area', 'assumptions', 'kernel'):
            if not str(e.get(field, '')).strip():
                fail(f'{eid}: empty required field `{field}`')
        lvl = e.get('kernel')
        if lvl not in SCORED + UNSCORED:
            fail(f'{eid}: unknown kernel level {lvl!r}')
        has_lean = any(c['kind'] == 'lean' for c in e.get('checks', []))
        has_probe = any(c['kind'] == 'probe' for c in e.get('checks', []))
        if lvl in NEEDS_LEAN and not has_lean:
            fail(f'{eid}: level {lvl} claims kernel coverage but names no Lean theorem')
        if lvl == 'P' and not has_probe:
            fail(f'{eid}: level P claims a probe but names none')
        if lvl == 'P' and has_lean:
            fail(f'{eid}: level P but a Lean theorem is named — grade it K1 or above, or drop it')
        if lvl == 'GAP' and (has_lean or has_probe):
            fail(f'{eid}: level GAP but a checker is named — GAP means nothing checks it')
        if lvl == 'K3' and str(e.get('delta', '')).strip():
            fail(f'{eid}: level K3 with a recorded delta ({e["delta"]!r}). K3 means the EXACT '
                 f'manuscript statement; a recorded gap makes it K2 at best')
        if lvl in ('K2', 'K1') and not str(e.get('delta', '')).strip():
            fail(f'{eid}: level {lvl} must record the delta between the manuscript statement and '
                 f'the formal statement')

        for c in e.get('checks', []):
            path = os.path.join(ROOT, c['path'])
            if not os.path.exists(path):
                fail(f'{eid}: checker does not exist: {c["path"]}')
                continue
            body = open(path, encoding='utf-8', errors='replace').read()
            if c['kind'] == 'lean':
                for nm in c.get('names', []):
                    if not re.search(r'(?<![A-Za-z0-9_.])' + re.escape(nm.split('.')[-1])
                                     + r'(?![A-Za-z0-9_])', body):
                        fail(f'{eid}: Lean declaration `{nm}` not found in {c["path"]}')
                lean_cache.setdefault(c['path'], True)
            else:
                if c.get('basis') == 'named':
                    ev = c.get('evidence', '')
                    if not ev:
                        fail(f'{eid}: check on {c["path"]} is basis=named with no evidence string')
                    elif ev.lower() not in body.lower():
                        fail(f'{eid}: {c["path"]} does not contain the naming evidence {ev!r}; '
                             f'either fix the string or downgrade the basis to `section`')
                elif c.get('basis') not in ('section', 'named'):
                    fail(f'{eid}: check on {c["path"]} has basis {c.get("basis")!r}')

    # 5. Mathlib-side modules must be reachable from the gated root
    root_txt = open(BRIDGE_ROOT, encoding='utf-8').read()
    for path in sorted(lean_cache):
        if 'lean-mathlib/OIBridge/' in path:
            module = ('OIBridge.' +
                      os.path.splitext(path.split('lean-mathlib/OIBridge/')[1])[0].replace('/', '.'))
            if f'import {module}' not in root_txt:
                fail(f'{path} is not imported by OIBridge.lean, so CI never builds it and any '
                     f'theorem in it certifies nothing')

    # 7. unattached artifacts must say what they certify
    for u in led.get('unattached', []):
        p = os.path.join(ROOT, u['path'])
        if not os.path.exists(p):
            fail(f'unattached checker does not exist: {u["path"]}')
        if not u.get('certifies', '').strip():
            fail(f'unattached {u["path"]}: no `certifies` recorded')

    # ------------------------------------------------------------------ the baseline report
    wf = open(WORKFLOW, encoding='utf-8').read()
    scored = [e for e in led['entries'] if e['kernel'] in SCORED]
    counts = {k: sum(1 for e in scored if e['kernel'] == k) for k in SCORED}
    areas = sorted({e['area'] for e in scored})
    print('proof-coverage baseline')
    print('=' * 68)
    print(f'{"area":<20}' + ''.join(f'{k:>6}' for k in SCORED) + f'{"total":>8}')
    for a in areas:
        rs = [e for e in scored if e['area'] == a]
        print(f'{a:<20}' + ''.join(f'{sum(1 for e in rs if e["kernel"] == k):>6}' for k in SCORED)
              + f'{len(rs):>8}')
    print('-' * 68)
    print(f'{"TOTAL":<20}' + ''.join(f'{counts[k]:>6}' for k in SCORED) + f'{len(scored):>8}')
    unscored = {k: sum(1 for e in led['entries'] if e['kernel'] == k) for k in UNSCORED}
    print(f'excluded from the denominator: ' +
          ', '.join(f'{k} {v}' for k, v in unscored.items() if v))
    kernel_covered = counts['K3'] + counts['K2'] + counts['K1']
    print(f'kernel coverage: {kernel_covered}/{len(scored)} '
          f'({100.0 * kernel_covered / len(scored):.1f}%)   '
          f'machine coverage: {kernel_covered + counts["P"]}/{len(scored)} '
          f'({100.0 * (kernel_covered + counts["P"]) / len(scored):.1f}%)')
    named = {c['path'] for e in led['entries'] for c in e['checks'] if c['kind'] == 'probe'}
    named |= {u['path'] for u in led.get('unattached', []) if u['kind'] == 'probe'}
    ungated = sorted(p for p in named if not is_gated(p, wf))
    print(f'probes named by the ledger: {len(named)}, of which {len(ungated)} are NOT run by CI')
    for p in ungated:
        print(f'    ungated: {p}')

    if FAILURES:
        print()
        print(f'coverage_check: FAIL ({len(FAILURES)})')
        for f in FAILURES:
            print(f'  - {f}')
        return 1
    print()
    print(f'coverage_check: OK ({len(led["entries"])} canonical statements, '
          f'{len(led.get("unattached", []))} unattached checkers)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
