"""The run's verdict from every job's .verdict file (disposable harness). argv: <dir with every artifact>.
Clean iff: the nine baseline commands and the 42 regression cases PASS; every mutant of the plan is KILLED; the
three crash-family CLI runs and the eight isolated sections PASS. A job with no verdict file is unexplained. An
infrastructure fault is NOT-RUN, listed apart, never a kill, and leaves the run not clean. Exit 1 unless clean."""
import os, re, sys

H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
import plan

got = {}
for root, _, files in os.walk(sys.argv[1]):
    for f in files:
        if f.endswith('.verdict'):
            line = open(os.path.join(root, f), encoding='utf-8').read().strip()
            m = re.match(r'(\S+) (\S+) (\S+) ', line + ' ')
            if m:
                got[(m.group(1), m.group(2))] = (m.group(3), line)
want = [(j['kind'], j['name']) for j in plan.jobs()]
rows, problems, notrun = [], [], []
for k in want:
    st, line = got.get(k, ('MISSING', '%s %s MISSING (no verdict: the job did not report)' % k))
    rows.append(line)
    good = st == ('KILLED' if k[0] == 'mutant' else 'PASS')
    if st == 'NOT-RUN':
        notrun.append(line)
    elif not good:
        problems.append(line)
extra = sorted(set(got) - set(want))
counts = {}
for k in want:
    counts.setdefault(k[0], {}).setdefault(got.get(k, ('MISSING',))[0], 0)
    counts[k[0]][got.get(k, ('MISSING',))[0]] += 1
print('## jobs (%d expected, %d reported)' % (len(want), len(got)))
for r in rows:
    print('  ' + r)
print('## counts')
for kind, c in counts.items():
    print('  %-12s %s' % (kind, ', '.join('%s %d' % kv for kv in sorted(c.items()))))
print('## infrastructure (NOT-RUN; never counted as results): %d' % len(notrun))
for r in notrun:
    print('  ' + r)
print('## unexplained or failing: %d' % (len(problems) + len(extra)))
for r in problems:
    print('  ' + r)
for k in extra:
    print('  unexpected job %s %s' % k)
clean = not problems and not notrun and not extra
print('CI SUMMARY: %s' % ('CLEAN' if clean else 'NOT CLEAN'))
sys.exit(0 if clean else 1)
