"""Print the mutant names of mutants_all.py as a GitHub Actions output line (names=<json list>), filtered by plan.json."""
import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(here, 'mutants_all.py'), encoding='utf-8').read()
src = src.split('origin, fn, kind, reason, edits, want = M[which]')[0]
src = src.replace('wt, which, outdir = sys.argv[1:4]', "wt, which, outdir = '/nonexistent', None, None")
ns = {}
exec(src, ns)
names = list(ns['M'])
plan = json.load(open(os.path.join(here, 'plan.json'), encoding='utf-8'))
if plan.get('run') != 'all':
    want = plan['run']
    missing = [n for n in want if n not in names]
    if missing:
        sys.exit('plan names unknown mutants: %s' % missing)
    names = [n for n in names if n in want]
print('names=' + json.dumps(names))
print('count=%d' % len(names))
