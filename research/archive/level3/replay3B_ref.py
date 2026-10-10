"""PREREG-3A section 6 item 5, resumable form: the complete Stage-B job for kappa ((0,1),(0,1)) on the REFERENCE
simulator. Phase 1 evaluates record3_sim.run3 on the job's full protocol set in fixed chunks, each saved to
ckpt/refB_<i>.json (resumable). Phase 2 feeds the assembled reference table to the unchanged analysis3.analyze
(RUN_ALL swapped for a table lookup) and compares the record field by field with fast3_stageB_linear.json.

usage: replay3B_ref.py [procs]
"""
import sys
import os
import json
import time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
CK = os.path.join(HERE, 'ckpt')
import analysis3                                                     # noqa: E402
from analysis3 import protocols, HORIZON, PALPH, EALPH, kappa_key    # noqa: E402
from record3_sim import run3                                         # noqa: E402

KAPPA = ((0, 1), (0, 1))
Lp, Le = HORIZON['B']
PS = sorted({a + b for a in protocols(PALPH, Lp) for b in protocols(EALPH, Le)})
CH = 2000
chunks = [PS[i:i + CH] for i in range(0, len(PS), CH)]


def do(i):
    fn = os.path.join(CK, f'refB_{i:04d}.json')
    if os.path.exists(fn):
        return i, 0.0
    t = time.time()
    out = {p: run3(p, 'linear', KAPPA) for p in chunks[i]}
    open(fn, 'w').write(json.dumps(out, sort_keys=True))
    return i, time.time() - t


if __name__ == '__main__':
    procs = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    todo = [i for i in range(len(chunks)) if not os.path.exists(os.path.join(CK, f'refB_{i:04d}.json'))]
    print(f'REPLAY3B-REF: {len(PS)} protocols, {len(chunks)} chunks, {len(todo)} to run, {procs} procs', flush=True)
    if todo:
        with Pool(procs) as pool:
            n = 0
            for i, dt in pool.imap_unordered(do, todo, chunksize=1):
                n += 1
                print(f'[{time.strftime("%H:%M:%S")}] chunk {i} {dt:.0f}s ({n}/{len(todo)})', flush=True)
    J = {}
    for i in range(len(chunks)):
        J.update({p: tuple(v) for p, v in json.load(open(os.path.join(CK, f'refB_{i:04d}.json'))).items()})
    assert set(J) == set(PS)
    analysis3.RUN_ALL = lambda ps, rule, kappa: {p: (list(J[p][0]), J[p][1]) for p in set(ps)}
    R = json.load(open(os.path.join(HERE, 'fast3_stageB_linear.json')))
    ref = {kappa_key(r): r for r in R}[KAPPA]
    o = analysis3.analyze(('linear', KAPPA, Lp, Le, 'B'))
    same = json.dumps(o, sort_keys=True) == json.dumps(ref, sort_keys=True)
    print('REPLAY3-B', KAPPA, o['verdict'], 'rank', o['rank'], 'dims', o['dimC'], 'MATCH' if same else 'MISMATCH', flush=True)
    print('REPLAY3-B', 'OK' if same else 'FAILED')
