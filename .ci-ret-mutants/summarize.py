"""Rebuild the mutation table from the per-mutant logs and compare with the local run. argv: <logdir> <local-expected.txt>.
Classes: KILLED, SURVIVED, CRASH (self-test raised; its targets were never evaluated), MISSING (no log: infrastructure).
Exit 0 iff the baseline is clean and every mutant run here agrees with the local class."""
import os, re, sys
logdir, expf = sys.argv[1:3]
exp = dict(l.split() for l in open(expf, encoding='utf-8') if l.strip())
base = os.path.join(logdir, 'baseline.log')
base_ok = os.path.isfile(base) and 'BASELINE CLEAN' in open(base, encoding='utf-8').read()
print('baseline: %s' % ('CLEAN' if base_ok else 'NOT CLEAN OR MISSING'))
ran = sorted(f[:-4] for f in os.listdir(logdir) if f.endswith('.log') and f != 'baseline.log')
counts, disagree = {}, []
for name in sorted(set(ran) | set(exp)):
    if name not in ran:
        continue
    t = open(os.path.join(logdir, name + '.log'), encoding='utf-8', errors='replace').read()
    m = re.search(r'^%s: (KILLED|SURVIVED)$' % re.escape(name), t, re.M)
    if 'self-test rc crash' in t:
        c = 'CRASH'
    elif m:
        c = m.group(1)
    else:
        c = 'MISSING'
    counts[c] = counts.get(c, 0) + 1
    e = exp.get(name, '?')
    flag = 'agree' if c == e else 'DISAGREE (local %s)' % e
    if c != e:
        disagree.append(name)
    print('%-40s %-9s %s' % (name, c, flag))
print('totals: ' + ', '.join('%s %d' % kv for kv in sorted(counts.items())) + '; ran %d of %d' % (len(ran), len(exp)))
print('disagreements: %s' % (disagree or 'none'))
sys.exit(0 if base_ok and not disagree else 1)
