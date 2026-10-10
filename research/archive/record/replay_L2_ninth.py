"""Gate 3, ninth distinct job. Rule (fixed before this replay ran, after Stage-A output existed; outcome-blind):
the first Level-2 Stage-A job in the frozen global job order (record_analysis2.jobs_for('A', 2)) not already
replayed by replay_L2_sample.py. Recomputed with the ORIGINAL simulator; compared field-by-field."""
import json, re
from record_analysis2 import jobs_for
from record_analysis import analyze
done = set()
for line in open('replay_L2_sample.log'):
    m = re.match(r"REPLAY-L2 (\w+) (\(\(.*\)\)) ", line)
    if m:
        done.add((m.group(1), eval(m.group(2))))
job = next(j for j in jobs_for('A', 2) if (j[0], j[1]) not in done)
print('NINTH selected', job[0], job[1], '| already replayed:', len(done), flush=True)
R = json.load(open('fast_stageA_L2.json'))
ref = next(r for r in R if r['rule'] == job[0] and r['kappa'] == [list(job[1][0]), list(job[1][1])])
o = analyze(job)
o['kappa'] = [list(job[1][0]), list(job[1][1])]
same = json.dumps(o, sort_keys=True) == json.dumps(ref, sort_keys=True)
print('REPLAY-L2', job[0], job[1], o['verdict'], 'rank', o['rank'], 'MATCH' if same else 'MISMATCH')
print('NINTH', 'OK' if same else 'FAILED')
