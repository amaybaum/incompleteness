"""E3: for every kernel-layer link in matrix.json, find its declaration's `#print axioms` report in a job log's
extraction, and say whether the retained expected result also carries it.

Usage:
    python3 -I E3_kernel_coverage.py MATRIX.json EXPECTED.json EXTRACTION.json

MATRIX.json      the audit's matrix.json
EXPECTED.json    papers/introduction_repro/results-121598983127.json (at 4a260ca9)
EXTRACTION.json  the frozen extractor's output on a digest-checked job log (e.g. job 121598983127 cut at the gate verdict)

A kernel link's source is `lean:<Module>.lean:<line>:<decl>` (optionally `OIBridge/`-prefixed, possibly several joined
by `; `). Prints, per declaration: reports in the log, its axioms, and whether the retained result carries it; then the
claim ids whose kernel evidence lies only in the log. Definitions and structure fields have no report and are listed
separately. Exit status 1 if any declaration with a report has an axiom outside the three.
"""
import json
import re
import sys

ALLOWED = ['propext', 'Classical.choice', 'Quot.sound']


def main():
    matrix = json.load(open(sys.argv[1], encoding='utf-8'))
    exp = json.load(open(sys.argv[2], encoding='utf-8'))['expected']['modules']
    ext = json.load(open(sys.argv[3], encoding='utf-8'))['reports']
    decls = {}
    for row in matrix['rows']:
        for link in row['chain']:
            if link['layer'] != 'kernel':
                continue
            for m in re.finditer(r'lean:(?:OIBridge/)?([A-Za-z0-9]+)\.lean:(\d+):([A-Za-z0-9_.\']+)', link['source']):
                mod, line, name = m.group(1), int(m.group(2)), m.group(3).split('.')[-1]
                decls.setdefault((mod, name), set()).add(row['id'])
    bad = 0
    log_only_claims = set()
    no_report = []
    for (mod, name), ids in sorted(decls.items()):
        key = 'OIBridge/%s.lean' % mod
        reps = [r for r in ext.get(key, []) if r['name'].split('.')[-1] == name]
        kept = [r for r in exp.get(key, {}).get('reports', []) if r['name'].split('.')[-1] == name]
        if not reps:
            no_report.append((mod, name, sorted(ids)))
            continue
        if any(r['axioms'] != ALLOWED for r in reps):
            bad += 1
        status = 'retained' if kept else 'LOG ONLY'
        if not kept:
            log_only_claims |= ids
        print('%-8s %-28s %-55s reports=%d axioms=%s claims=%s' % (status, mod, name, len(reps), reps[0]['axioms'],
                                                                   ','.join(sorted(ids))))
    print('\nno #print axioms report in the log (definition, field or unreported):')
    for mod, name, ids in no_report:
        print('  %s.%s  claims=%s' % (mod, name, ','.join(ids)))
    print('\nclaims with kernel evidence only in the job log: %d' % len(log_only_claims))
    print(json.dumps(sorted(log_only_claims)))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
