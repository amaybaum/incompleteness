#!/usr/bin/env python3
"""Reference evaluator for the #1162 synthetic demonstration.

It computes the outcome a checker keyed on qualified identities and reading
Unicode identifiers must return for a synthetic source tree and log. It is the
independent check of the hand-written expectations in fixtures/expected.json.
It imports nothing from tools/ and is not a proposed replacement for
tools/lean_axiom_check.py; it handles only the single-line report layout the
fixtures use.

Identity of a print: the source file under verification/lean-mathlib and the
line of its `#print axioms` command. A report is attached to that identity by
the position lake prints before it (`info: FILE:LINE:COL: ...`), and its
fully qualified name must end, on a `.` boundary, with the name as written.
So the identity checked is (module, fully qualified name).

Rules, all fail-closed:
  SORRY    the token sorryAx anywhere in the log
  AXIOM    a parsed report with an axiom outside the permitted three
  MISSING  a print with no report at its position
  MISMATCH a report whose name does not extend the name written at its position
  ORPHAN   a report at a position with no print
  UNPARSED a line that mentions an axiom report but does not parse
  EMPTY    no report at all

Usage: python3 -I reference_checker.py --root DIR --log FILE
Prints one JSON object; exit 0 for PASS, 1 for FAIL.
"""
import json, os, re, sys

PERMITTED = {'propext', 'Classical.choice', 'Quot.sound'}
PRINT = re.compile(r'^#print axioms[ \t]+(\S+)[ \t]*$')
REPORT = re.compile(
    r"^(?:info: )?(?P<file>\S+?\.lean):(?P<line>\d+):(?P<col>\d+): "
    r"'(?P<name>[^\n]+?)' "
    r"(?:depends on axioms: \[(?P<ax>[^\]\n]*)\]|does not depend on any axioms)"
    r"[ \t]*$")
MENTION = ('depends on axioms', 'does not depend on any axioms')


def evaluate(root, log_text):
    src = os.path.join(root, 'verification', 'lean-mathlib')
    prints = {}
    findings = []
    for dp, dns, fs in os.walk(src):
        dns.sort()
        for f in sorted(fs):
            if not f.endswith('.lean'):
                continue
            path = os.path.join(dp, f)
            rel = os.path.relpath(path, src).replace(os.sep, '/')
            with open(path, encoding='utf-8') as h:
                for n, line in enumerate(h.read().split('\n'), 1):
                    if line.startswith('#print axioms'):
                        m = PRINT.match(line)
                        if m:
                            prints[(rel, n)] = m.group(1)
                        else:
                            findings.append(f'UNPARSED@{rel}:{n}')
    reports = {}
    for raw in log_text.split('\n'):
        if 'sorryAx' in raw:
            m = REPORT.match(raw)
            where = f"{m.group('file')}:{m.group('line')}" if m else 'log'
            findings.append(f'SORRY@{where}')
        if not any(t in raw for t in MENTION):
            continue
        m = REPORT.match(raw)
        if not m:
            findings.append('UNPARSED@log')
            continue
        key = (m.group('file'), int(m.group('line')))
        reports[key] = m.group('name')
        if m.group('ax') is not None:
            axioms = {a.strip() for a in m.group('ax').split(',') if a.strip()}
            if axioms - PERMITTED:
                findings.append(f'AXIOM@{key[0]}:{key[1]}')
    if not reports:
        findings.append('EMPTY@log')
    for key, written in prints.items():
        if key not in reports:
            findings.append(f'MISSING@{key[0]}:{key[1]}')
        else:
            full = reports[key]
            if not (full == written or full.endswith('.' + written)):
                findings.append(f'MISMATCH@{key[0]}:{key[1]}')
    for key in reports:
        if key not in prints:
            findings.append(f'ORPHAN@{key[0]}:{key[1]}')
    findings = sorted(set(findings))
    return ('FAIL' if findings else 'PASS'), findings


def main():
    root = sys.argv[sys.argv.index('--root') + 1]
    log = sys.argv[sys.argv.index('--log') + 1]
    with open(log, encoding='utf-8') as h:
        verdict, findings = evaluate(root, h.read())
    print(json.dumps({'verdict': verdict, 'findings': findings},
                     ensure_ascii=False, sort_keys=True))
    return 0 if verdict == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
