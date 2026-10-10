"""Resumable driver for the Level-3A sweeps (orchestration only; analysis3.analyze and layers3.check are unchanged).

usage: driver3.py B|C|CC [procs]
  Runs the stage's frozen job list (analysis3.jobs_for for B/C; the 143-kappa linear census for CC) with
  imap_unordered, writing each job's result to ckpt/<stage>_<kappa>.json as it completes; jobs whose checkpoint
  exists are skipped, so a run stopped by a time limit resumes without loss. When every job has a checkpoint the
  artifact is assembled in the frozen job order with the same serialization analysis3.py / layers3.py use
  (json.dumps(sort_keys=True, indent=0)), and the same STAGE/TALLY (or CC3-CENSUS) summary lines are printed.
"""
import sys
import os
import json
import time
import hashlib
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
CK = os.path.join(HERE, 'ckpt')
os.makedirs(CK, exist_ok=True)
stage = sys.argv[1]
procs = int(sys.argv[2]) if len(sys.argv) > 2 else 4

if stage == 'CC':
    sys.argv = ['layers3.py', '--cc']
    import layers3
    from analysis3 import INTERFACES
    jobs = [('linear', k, 'oifsc', 'oimfsc', 3) for k in INTERFACES]
    work = layers3.check
    kap = lambda j: j[1]
    artifact = os.path.join(HERE, 'cc3_census.json')
else:
    import analysis3
    jobs = analysis3.jobs_for(stage, 'linear')
    work = analysis3.analyze
    kap = lambda j: j[1]
    artifact = os.path.join(HERE, f'fast3_stage{stage}_linear.json')


def ck(j):
    k = kap(j)
    return os.path.join(CK, f'{stage}_{k[0][0]}{k[0][1]}_{k[1][0]}{k[1][1]}.json')


todo = [j for j in jobs if not os.path.exists(ck(j))]
print(f'DRIVER {stage}: {len(jobs)} jobs, {len(jobs) - len(todo)} checkpointed, {len(todo)} to run, {procs} procs',
      flush=True)


def run(j):
    t = time.time()
    r = work(j)
    return j, r, time.time() - t


if todo:
    with Pool(procs) as pool:
        done = 0
        for j, r, dt in pool.imap_unordered(run, todo, chunksize=1):
            open(ck(j), 'w').write(json.dumps(r, sort_keys=True))
            done += 1
            print(f'[{time.strftime("%H:%M:%S")}] {done}/{len(todo)} {kap(j)} {dt:.0f}s {r.get("verdict", r.get("G2"))}',
                  flush=True)

res = [json.load(open(ck(j))) for j in jobs]
blob = json.dumps(res, sort_keys=True, indent=0)
open(artifact, 'w').write(blob)
h = hashlib.sha256(blob.encode()).hexdigest()
if stage == 'CC':
    A = json.load(open(os.path.join(HERE, 'fast3_stageA_linear.json')))
    inv = {tuple(map(tuple, r['kappa'])): r.get('invasive') for r in A}
    import collections
    cnt = collections.Counter((inv[tuple(map(tuple, r['kappa']))], r['G2']) for r in res)
    print(f'CC3-CENSUS: {len(res)} runs; sha256 {h}')
    print(f'CC3-CENSUS linear: G2 {sum(r["G2"] for r in res)}/{len(res)}, G3norm {sum(r["G3norm"] for r in res)}/{len(res)}, '
          f'G3idle {sum(r["G3idle"] for r in res)}/{len(res)}')
    print('CC3-CENSUS (invasive, G2 under mutation):', dict(cnt), '; bites on', sum(1 for r in res if not r['G2']), 'of', len(res))
else:
    print(f'STAGE {stage} linear: {len(res)} runs; sha256 {h}')
    tally = {}
    for r in res:
        tally[r['verdict']] = tally.get(r['verdict'], 0) + 1
    for k, v in sorted(tally.items()):
        print(f'TALLY {stage} linear: {k}: {v}')
