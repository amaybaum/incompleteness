#!/usr/bin/env python3
"""E1_logreports.py - read `#print axioms` reports for named declarations from
a "Mathlib bridge" job log, and the gate verdict lines.

The log is the text of GitHub's `actions/jobs/<id>/logs` endpoint (every line
prefixed by an ISO timestamp). Only the Build step is read for reports: from
the start of the log to the first `Build completed successfully` line, which
excludes the later round-specific steps of the job. Multi-line reports
(lake wraps long axiom lists) are joined.

Usage:
    python3 -I E1_logreports.py <job.log> <decls.json from E1_decls.py> > out.json

Reading only; writes to stdout.
"""
import json
import re
import sys

TS = re.compile(r'^\d{4}-\d\d-\d\dT[0-9:.]+Z ?')
REPORT = re.compile(r"info: (OIBridge/[A-Za-z0-9_/]+\.lean):(\d+):\d+: '(.+?)' "
                    r"(?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)")
PERMITTED = {'propext', 'Classical.choice', 'Quot.sound'}


def main():
    log_path, decls_path = sys.argv[1], sys.argv[2]
    lines = [TS.sub('', l) for l in open(log_path, encoding='utf-8', errors='replace')
             .read().split('\n')]
    end = next(i for i, l in enumerate(lines) if 'Build completed successfully' in l)
    build = '\n'.join(lines[:end + 1])
    gate = [l.strip() for l in lines[end:end + 80]
            if re.match(r'\s*(PASS|FAIL)\s+\S', l) or 'VERDICT' in l or l.startswith('PASS  (')
            or l.strip().startswith('PASS  (') or l.strip().startswith('FAIL  (')]
    reports = {}
    for m in REPORT.finditer(build):
        axioms = None if m.group(4) is None else \
            [a.strip() for a in m.group(4).replace('\n', ' ').split(',') if a.strip()]
        reports.setdefault(m.group(3), []).append(
            {'file': m.group(1), 'line': int(m.group(2)), 'axioms': axioms or []})
    decls = json.load(open(decls_path))['declarations']
    out = []
    for d in decls:
        full = d.get('full_name')
        reps = reports.get(full, [])
        out.append({
            'name': d['name'], 'module': d['module'], 'full_name': full,
            'print_lines': [p['line'] for p in d.get('print_axioms', [])],
            'reports': reps,
            'within_allow_list': bool(reps) and all(set(r['axioms']) <= PERMITTED for r in reps),
            'report_lines_match_prints': sorted(r['line'] for r in reps)
            == sorted(p['line'] for p in d.get('print_axioms', [])),
        })
    markers = {k: build.count(k) for k in
               ('sorryAx', 'Lean.ofReduceBool', "declaration uses 'sorry'", 'error:')}
    whole = '\n'.join(lines)
    markers_whole_log = {k: whole.count(k) for k in markers}
    json.dump({'log': log_path, 'build_end_line': end + 1,
               'build_success_line': lines[end].strip(),
               'total_reports_in_build': sum(len(v) for v in reports.values()),
               'gate_lines': gate, 'markers_build': markers,
               'markers_whole_log': markers_whole_log,
               'declarations': out}, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == '__main__':
    main()
