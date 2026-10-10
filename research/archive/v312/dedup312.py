#!/usr/bin/env python3
"""Scratch: which retained guard predicates are redundant with legacy-records. Never landed as is.

A retained predicate is redundant iff every file it reads resolves statically, it reads at least
one, and every path it reads lies in the legacy-records population: under a closed namespace, or
one of the individually pinned paths. The migration manifest, read only to locate an artifact, is a
lookup and not a protected read."""
import collections, json, sys
reads = json.load(open('reads.json'))
classes = json.load(open('guard_classes.json'))
REPO = '/home/user/incompleteness'
rd = [l.strip() for l in open('rounddirs.txt') if l.strip()]
NATIVE = ('verification/infrastructure/round-v3-10-native-pilot',
          'verification/infrastructure/round-v3-11-authority-cutover')
CLOSED = ['verification/certificates', 'verification/seals'] + [r for r in rd if r not in NATIVE]
EXCLUDED = ['verification/certificates/conformance']
PINNED = {'verification/audits/foundations/a6-covariance-propagation-audit.md',
          'verification/audits/foundations/act11-scope-propagation-audit.md',
          'verification/audits/foundations/act11-scope-propagation-open-frontier-amendment.md',
          'verification/audits/foundations/act12-scope-propagation-audit.md',
          'verification/audits/operational/stochastic-observer-interface-audit.md'}
LOOKUP = {'verification/migration-manifest.json'}
def under(p, d): return p == d or p.startswith(d + '/')
def covered(p):
    if any(under(p, e) for e in EXCLUDED): return False
    return p in PINNED or any(under(p, d) for d in CLOSED)
# Read by hand: sites the resolver leaves open, each of which reads legacy records only.
_DRIFT = 'the drift control of a redundant freeze pin: the pin run with a reader that appends one byte ' \
         'to the pinned record, which reads only that record'
ADJUDICATED = {
    ('R7-HYE', 19931): 'compares the seal records of HYA, HYB and HYE, read from verification/seals/ '
                       'through the record reader, with constants, and reads HYE\'s preregistration',
    ('R7-HYE', 20098): 'the mutation control of the HYE seal comparison on a fabricated state',
    ('R7-HYE', 20103): 'the mutation control of the HYE seal comparison on a fabricated state',
    ('R7-NLV', 27682): _DRIFT, ('R7-SI1', 29616): _DRIFT, ('R7-SI2', 30823): _DRIFT,
    ('R7-SI2', 30824): _DRIFT, ('R7-SI2', 30827): _DRIFT, ('R7-SI2', 30901): _DRIFT,
    ('R7-SI3', 31601): _DRIFT, ('R7-SI3', 31602): _DRIFT, ('R7-SI3', 31605): _DRIFT,
    ('R7-SI3', 31606): _DRIFT,
}
out = []
cnt = collections.Counter()
for r in classes:
    k = '%s %d' % (r['check'], r['line'])
    rs = [p for p in reads[k] if p not in LOOKUP]
    cls = r['class']
    new, why = cls, r['why']
    if cls in ('RS', 'RH'):
        if (r['check'], r['line']) in ADJUDICATED:
            new, why2 = 'RD', 'redundant, adjudicated: ' + ADJUDICATED[(r['check'], r['line'])]
        elif 'UNRESOLVED' in rs:
            why2 = 'kept: a read site does not resolve statically'
        elif not rs:
            why2 = 'kept: reads no file' 
        elif all(covered(p) for p in rs):
            new, why2 = 'RD', 'redundant: every file it reads is pinned by legacy-records'
        else:
            live = sorted(p for p in rs if not covered(p))
            why2 = 'kept: reads %d file(s) outside legacy-records, e.g. %s' % (len(live), live[0])
        r = dict(r, dedup=why2)
    cnt[(cls, new)] += 1
    out.append(dict(r, new_class=new, files=rs))
json.dump(out, open('dedup.json', 'w'), indent=0)
for k in sorted(cnt): print(k, cnt[k])
assert all(any(o['check'] == c and o['line'] == l and o['class'] in ('RS', 'RH') for o in out)
           for c, l in ADJUDICATED), 'an adjudication names no retained predicate'
fin = collections.Counter(o['new_class'] for o in out)
print('final', dict(fin))
chk = collections.defaultdict(collections.Counter)
for o in out:
    chk[o['check']][o['new_class']] += 1
disp = collections.Counter()
for c, v in chk.items():
    n = v['RS'] + v['RH'] + v['RD'] + v['RT']
    keep = v['RS'] + v['RH']
    disp['retained whole' if keep == n else 'removed whole' if keep == 0 else 'split'] += 1
print('checks', dict(disp))
print('removed whole:', sorted(c for c, v in chk.items() if v['RS'] + v['RH'] == 0))
