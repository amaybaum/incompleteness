#!/usr/bin/env python3
"""Scratch: V3-12's census rule over guard.json. Never landed.

Retire (RT) a predicate when it (1) executes a git read, a host-environment read, a seal-state read
(prospective declaration, baseline, validator verdict) or a filesystem read of verification/seals/;
or (2) belongs to a whole-check retirement (R7-VIS, R7-ARCH, synthetic regressions of archive-mode
chronology); or (3) belongs to an infrastructure round whose subject is the retired machinery
(R7-SI1, R7-SI2, R7-SI3, R7-GR1, R7-GR2, R7-CV1) and does not pin that round's own record text.
Otherwise retain: RH (historical) when every path it reads is a legacy round record, RS
(substantive) when it reads the kernel, the live corpus, live notes, the workflow or computes.
Accumulator bookkeeping (the `_bad = sorted(...)` line) is structural, not a predicate."""
import json, re, sys, collections
g = json.load(open(sys.argv[1]))
WHOLE = {'R7-VIS', 'R7-ARCH'}
INFRA = {'R7-SI1', 'R7-SI2', 'R7-SI3', 'R7-GR1', 'R7-GR2', 'R7-CV1'}
RECORD = re.compile(r'(^|/)(programmes|infrastructure|audits)/|round-|act-\d|preregistration\.md|result\.md|amendment|census\.json')
LIVE = re.compile(r'\.lean|papers/|book/|README|ROADMAP|AGENTS|verify\.yml|release_gate|lean-manuscript-census|FULL\.md|_probe\.py|probes?\.py')
out = []
for c in g:
    for p in c['predicates']:
        t = p['text']
        if re.match(r'\s*_[a-z0-9]+_bad\s*=\s*sorted\(', t) or re.match(r'\s*_[a-z0-9]+_bad\s*=\s*\[name for', t) \
                or re.match(r'\s*_[a-z0-9]+_bad\s*=\s*\[k for k, v in _[a-z0-9]+_checks\.items\(\) if not v\]', t) \
                or re.fullmatch(r'ok_[a-z0-9]+ = True', t.strip()):
            cls, why = 'STRUCT', 'accumulator bookkeeping'
        elif c['check'] in WHOLE:
            cls, why = 'RT', 'whole check: synthetic regression of archive-mode chronology'
        elif p['hist']:
            cls, why = 'RT', 'executes a history/seal-state read: ' + ','.join(p['hist'])
        elif c['check'] in INFRA:
            reads = [r for r in p['reads'] if (('/' in r and len(r) > 2) or r.endswith('.md'))
                     and r not in ('/', '%s/%s', 'verification/')]
            if reads and all(RECORD.search(r) for r in reads) and 'manuscript' in p['tags'] \
                    and not set(p['tags']) & {'certificates', 'workflow-or-gate', 'seal-records'}:
                cls, why = 'RH', 'infrastructure round: pins its own record text'
            else:
                cls, why = 'RT', 'infrastructure round: tests or pins the retired machinery'
        else:
            reads = [r for r in p['reads'] if (('/' in r and len(r) > 2) or r.endswith('.md') or r.endswith('.lean'))
                     and r not in ('/', '%s/%s', 'verification/')]
            if 'lean-kernel' in p['tags'] or 'computation' in p['tags'] or 'workflow-or-gate' in p['tags'] \
                    or any(LIVE.search(r) for r in reads) or not reads or not all(RECORD.search(r) for r in reads):
                cls, why = 'RS', 'reads the kernel, live corpus/notes, workflow wiring, or computes'
            elif all(RECORD.search(r) for r in reads):
                cls, why = 'RH', 'reads legacy round records only'
            else:
                cls, why = 'RS', 'reads live notes'
        out.append({'check': c['check'], 'line': p['line'], 'class': cls, 'why': why,
                    'tags': p['tags'], 'hist': p['hist'], 'text': t.split('\n')[0][:160]})
json.dump(out, open(sys.argv[2], 'w'), indent=1)
by = collections.defaultdict(collections.Counter)
for r in out:
    by[r['check']][r['class']] += 1
tot = collections.Counter(r['class'] for r in out)
print('TOTAL', dict(tot))
for k in [c['check'] for c in g]:
    v = by[k]
    print('%-10s RS %4d  RH %4d  RT %4d  STRUCT %d' % (k, v['RS'], v['RH'], v['RT'], v['STRUCT']))
