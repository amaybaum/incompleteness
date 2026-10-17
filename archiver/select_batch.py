"""Write the batch a push asks for, as a CSV the fetcher reads, to stdout.

batch.json is either {"source": "<csv in archiver/>", "ranks": [first, last]} (inclusive, from a ranked list) or
{"source": "<csv>", "run_ids": ["<id>", ...]}, with an optional "job_logs": "cited" (the default: each run's cited
jobs) or "all" (every job that ran), and an optional "retention_days" for the staged artifact, 1 to 90 (default 14).
Every requested run must be in the source, the ids must be distinct, and a batch holds 1 to MAX_RUNS runs; anything
else fails.
Usage: python3 -I select_batch.py archiver/batch.json                  # the batch CSV
       python3 -I select_batch.py archiver/batch.json --job-logs       # the job-log mode
       python3 -I select_batch.py archiver/batch.json --retention-days # the artifact's retention"""
import csv, json, os, sys

MAX_RUNS = 25

spec = json.load(open(sys.argv[1]))
mode = spec.get('job_logs', 'cited')
if mode not in ('cited', 'all'):
    sys.exit('select_batch: job_logs is "cited" or "all", not %r' % mode)
days = spec.get('retention_days', 14)
if type(days) is not int or not 1 <= days <= 90:
    sys.exit('select_batch: retention_days is a whole number of days from 1 to 90, not %r' % (days,))
if sys.argv[2:] == ['--job-logs']:
    print(mode)
    sys.exit(0)
if sys.argv[2:] == ['--retention-days']:
    print(days)
    sys.exit(0)
if sys.argv[2:]:
    sys.exit('select_batch: unknown option %s' % ' '.join(sys.argv[2:]))
src = os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), spec['source'])
rows = list(csv.DictReader(open(src, newline='')))
if 'ranks' in spec:
    a, b = (int(x) for x in spec['ranks'])
    pick = sorted((r for r in rows if a <= int(r['rank']) <= b), key=lambda r: int(r['rank']))
    want = b - a + 1
else:
    ids = [str(x) for x in spec['run_ids']]
    if len(set(ids)) != len(ids):
        sys.exit('select_batch: a run id is repeated')
    by = {r['run_id']: r for r in rows}
    missing = [i for i in ids if i not in by]
    if missing:
        sys.exit('select_batch: not in %s: %s' % (spec['source'], ', '.join(missing)))
    pick = [dict(by[i], rank=str(n)) for n, i in enumerate(ids, 1)]
    want = len(ids)
if not pick or len(pick) != want:
    sys.exit('select_batch: %d of %d requested runs found' % (len(pick), want))
if len(pick) > MAX_RUNS:
    sys.exit('select_batch: %d runs requested; a batch holds at most %d' % (len(pick), MAX_RUNS))
cols = ['rank'] + [k for k in pick[0].keys() if k != 'rank']
w = csv.DictWriter(sys.stdout, fieldnames=cols, extrasaction='ignore')
w.writeheader()
w.writerows(pick)
print('select_batch: %d run(s) from %s, job logs: %s' % (len(pick), spec['source'], mode), file=sys.stderr)
