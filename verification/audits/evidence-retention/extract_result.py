#!/usr/bin/env python3
"""extract_result.py -- reads the structured result of a Mathlib bridge build and release gate from its output.

The same extraction runs on a served GitHub job log (timestamped lines, possibly only the last lines of the
log) and on the output of a fresh `lake --rehash build` plus `tools/release_gate.py` at the same commit, so an
archived expected result and a reproduction are compared on equal terms. Standard library only.

    python3 -I extract_result.py LOG            # prints the extraction as JSON

What is read:
  build      the "Build completed successfully (N jobs)." line, or its absence;
  gate       the release-gate block: each step's name, status and summary, and the verdict line;
  reports    every `#print axioms` report, by module: source line, declaration name, and its axiom list
             (null for "does not depend on any axioms"); a list wrapped over several lines is joined;
  built      every "Built OIBridge…" line, with its seconds;
  cache      the Actions cache lines (hit, saved, restored, not found);
  markers    counts of the lines that would fail the axiom check: sorryAx, Lean.ofReduceBool,
             "declaration uses 'sorry'", and "error:".
Each item carries the 1-based line of the text it was read from.
"""
import json
import re
import sys

TS = re.compile(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ')
GATE_START = re.compile(r'^release gate$')
GATE_END = re.compile(r'^release gate: (.*)$')
GATE_STEP = re.compile(r'^  (PASS|FAIL|SKIP)  (\S+)\s*(.*)$')
BUILD_OK = re.compile(r'^Build completed successfully \((\d+) jobs\)\.')
REPORT = re.compile(r"^info: ((?:OIBridge/)?[A-Za-z0-9_/]+\.lean):(\d+):\d+: '([^']+)' (depends on axioms: \[(.*)|does not depend on any axioms)")
BUILT = re.compile(r'^\S* ?\[\d+/\d+\] Built (OIBridge(?:\.[A-Za-z0-9_]+)*) \(([\d.]+)s\)')
CACHE = re.compile(r'Cache (saved with key|hit occurred on the primary key|restored from key|not found for input keys)|Failed to (save|restore)')
MARKERS = {'sorryAx': re.compile(r'sorryAx'), 'Lean.ofReduceBool': re.compile(r'Lean\.ofReduceBool'),
           "declaration uses 'sorry'": re.compile(r"declaration uses .sorry."), 'error:': re.compile(r'error:')}


def strip(line):
    return TS.sub('', line, count=1)


def extract(text):
    raw = text.split('\n')
    if raw and raw[-1] == '':
        raw.pop()
    lines = [strip(l) for l in raw]
    out = {'lines': len(lines), 'build': None, 'gate': None, 'reports': {}, 'built': [], 'cache': [],
           'markers': {k: 0 for k in MARKERS}}
    i = 0
    while i < len(lines):
        l = lines[i]
        n = i + 1
        m = BUILD_OK.match(l)
        if m:
            out['build'] = {'success': True, 'jobs': int(m.group(1)), 'line': n}
        m = REPORT.match(l)
        if m:
            mod, src_line, name, kind, axioms = m.group(1), int(m.group(2)), m.group(3), m.group(4), m.group(5)
            if kind.startswith('depends'):
                body, j = axioms, i
                while ']' not in body and j + 1 < len(lines):
                    j += 1
                    body += ' ' + lines[j].strip()
                closed = ']' in body
                ax = [a.strip() for a in body.split(']')[0].split(',') if a.strip()]
                rep = {'line': src_line, 'name': name, 'axioms': ax, 'served_line': n}
                if not closed:
                    rep['unclosed'] = True
                i = j
            else:
                rep = {'line': src_line, 'name': name, 'axioms': None, 'served_line': n}
            out['reports'].setdefault(mod, []).append(rep)
        m = BUILT.match(l)
        if m:
            out['built'].append({'module': m.group(1), 'seconds': float(m.group(2)), 'served_line': n})
        if CACHE.search(l):
            out['cache'].append({'text': l, 'served_line': n})
        for k, rx in MARKERS.items():
            if rx.search(l):
                out['markers'][k] += 1
        if GATE_START.match(l):
            steps, verdict, j = [], None, i + 1
            while j < len(lines):
                e = GATE_END.match(lines[j])
                if e:
                    verdict = {'text': e.group(1), 'pass': e.group(1).startswith('PASS'), 'served_line': j + 1}
                    break
                s = GATE_STEP.match(lines[j])
                if s:
                    steps.append({'status': s.group(1), 'name': s.group(2), 'summary': s.group(3).rstrip(), 'served_line': j + 1})
                j += 1
            out['gate'] = {'steps': steps, 'verdict': verdict, 'start_line': n}
            i = j
        i += 1
    for mod in out['reports']:
        out['reports'][mod].sort(key=lambda r: (r['line'], r['served_line']))
    return out


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    print(json.dumps(extract(open(sys.argv[1], encoding='utf-8', errors='replace').read()), indent=1, sort_keys=True))
