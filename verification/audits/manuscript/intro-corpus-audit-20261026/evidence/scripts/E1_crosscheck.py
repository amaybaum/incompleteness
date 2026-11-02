#!/usr/bin/env python3
"""E1_crosscheck.py - compare the retained expected result of the Introduction
(papers/introduction_repro/results-121598983127.json, run at 17b830bc) with the
`#print axioms` reports of later "Mathlib bridge" job logs, module by module, and
with the `#print axioms` lines of the module sources.

For each of the result's modules it checks:
  C1  the source's `#print axioms` line numbers equal the result's print lines;
  C2  every report in the result appears in each log with the same declaration,
      line and axiom list, and the log has no other report for that module;
  C3  every report's axioms lie within {propext, Classical.choice, Quot.sound}.
A countercontrol then perturbs one retained report (drops Quot.sound from the
first report) and one source print line (shifts it by one) and requires that
C2 and C1 each fail on exactly that case.

Usage:
    python3 -I E1_crosscheck.py <results.json> <lean-mathlib dir> <job.log> [<job.log> ...]

Reading only; prints a JSON verdict to stdout; exit 1 on any failure.
"""
import copy
import json
import os
import re
import sys

TS = re.compile(r'^\d{4}-\d\d-\d\dT[0-9:.]+Z ?')
REPORT = re.compile(r"info: (OIBridge/[A-Za-z0-9_/]+\.lean):(\d+):\d+: '(.+?)' "
                    r"(?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)")
PRINT = re.compile(r"^#print axioms\s+\S+\s*$")
PERMITTED = {'propext', 'Classical.choice', 'Quot.sound'}


def log_reports(path):
    lines = [TS.sub('', l) for l in open(path, encoding='utf-8', errors='replace').read().split('\n')]
    end = next(i for i, l in enumerate(lines) if 'Build completed successfully' in l)
    build = '\n'.join(lines[:end + 1])
    by_mod = {}
    for m in REPORT.finditer(build):
        ax = [] if m.group(4) is None else [a.strip() for a in m.group(4).split(',') if a.strip()]
        by_mod.setdefault(m.group(1), []).append((m.group(3), int(m.group(2)), tuple(ax)))
    return by_mod


def source_prints(root, module):
    lines = open(os.path.join(root, module), encoding='utf-8').read().split('\n')
    return [i for i, l in enumerate(lines, 1) if PRINT.match(l)]


def check(result, root, logs):
    fails = []
    mods = result['expected']['modules']
    for mod, entry in sorted(mods.items()):
        want_lines = []
        for a, b in entry['print_lines']:
            want_lines += list(range(a, b + 1))
        got = source_prints(root, mod)
        if got != want_lines:
            fails.append(('C1', mod, 'source print lines %s != result %s' % (got[:5], want_lines[:5])))
        want = sorted((r['name'], r['line'], tuple(r['axioms'])) for r in entry['reports'])
        for r in entry['reports']:
            if not set(r['axioms']) <= PERMITTED:
                fails.append(('C3', mod, r['name']))
        for lp, rep in logs.items():
            have = sorted(rep.get(mod, []))
            if have != want:
                fails.append(('C2', mod, '%s: %d log reports vs %d retained; first diff %s' % (
                    os.path.basename(lp), len(have), len(want),
                    next(((x, y) for x, y in zip(have, want) if x != y), None))))
    return fails


def main():
    res_path, root, log_paths = sys.argv[1], sys.argv[2], sys.argv[3:]
    result = json.load(open(res_path))
    logs = {p: log_reports(p) for p in log_paths}
    fails = check(result, root, logs)
    # countercontrols
    mut = copy.deepcopy(result)
    first_mod = sorted(mut['expected']['modules'])[0]
    mut['expected']['modules'][first_mod]['reports'][0]['axioms'] = ['propext', 'Classical.choice']
    cc1 = check(mut, root, logs)
    cc1_ok = bool(cc1) and all(f[0] == 'C2' and f[1] == first_mod for f in cc1)
    mut2 = copy.deepcopy(result)
    a, b = mut2['expected']['modules'][first_mod]['print_lines'][0]
    mut2['expected']['modules'][first_mod]['print_lines'][0] = [a + 1, b + 1]
    cc2 = check(mut2, root, logs)
    cc2_ok = bool(cc2) and all(f[0] == 'C1' and f[1] == first_mod for f in cc2)
    out = {
        'modules': len(result['expected']['modules']),
        'reports': sum(len(e['reports']) for e in result['expected']['modules'].values()),
        'logs': list(logs),
        'failures': fails,
        'countercontrol_axiom_drop_caught': cc1_ok,
        'countercontrol_print_shift_caught': cc2_ok,
        'holds': not fails and cc1_ok and cc2_ok,
    }
    json.dump(out, sys.stdout, indent=1)
    print()
    sys.exit(0 if out['holds'] else 1)


if __name__ == '__main__':
    main()
