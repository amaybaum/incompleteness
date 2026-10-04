"""Resumable driver for the Level-3B sweeps (orchestration only; the criteria live in analysis3.analyze and
analysis3b). Checkpoints are written outside the repository (L3B_CKPT, default ~/.l3b_ckpt); a job whose
checkpoint exists is skipped, so a run stopped by a time limit resumes without loss. When every job of a sweep has
a checkpoint the artifact is assembled in the frozen job order with the 3A serialization and its sha256 and the
tally are printed and appended to the sweep's log.

usage: driver3b.py A|B|C <cell> [procs]      Block 1 stages for a run cell (R_LS, R_NL, R_5)
       driver3b.py H <cell> <H1|H2> [procs]  Block 2 cell (R_LL, R_LS, R_NL, R_5), Stage A, all 143 kappa
       driver3b.py L <cell> [procs]          gate V10: G identities on all 143 kappa (layers3.check)
       driver3b.py RNS [procs]               gate V7: OVER-RANK controls, R_NS-n and R_NS-m at positions 0, 71, 142
       driver3b.py V6 <sealed-3A-stageA.json> gate V6: R_LL instrument replay against the sealed 3A Stage-A artifact
"""
import os
import sys
import json
import time
import hashlib
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analysis3b as A3B                                                 # noqa: E402
from analysis3b import INTERFACES, kappa_key, RESULTS, LOGS, dump, head  # noqa: E402

CK_ROOT = os.environ.get('L3B_CKPT') or os.path.join(os.path.expanduser('~'), '.l3b_ckpt')


def kstr(k):
    return f'{k[0][0]}{k[0][1]}_{k[1][0]}{k[1][1]}'


def log(tag, line):
    os.makedirs(LOGS, exist_ok=True)
    print(line, flush=True)
    with open(os.path.join(LOGS, f'{tag}.log'), 'a') as fh:
        fh.write(line + '\n')


def sweep(tag, jobs, work, kap, artifact, procs, resumptions_note=True):
    ck = os.path.join(CK_ROOT, tag)
    os.makedirs(ck, exist_ok=True)
    os.makedirs(RESULTS, exist_ok=True)
    path = lambda j: os.path.join(ck, f'{kstr(kap(j))}.json')
    todo = [j for j in jobs if not os.path.exists(path(j))]
    log(tag, f'[{time.strftime("%Y-%m-%d %H:%M:%S")}] DRIVER {tag}: {len(jobs)} jobs, {len(jobs) - len(todo)} checkpointed, '
             f'{len(todo)} to run, {procs} procs')
    if todo:
        with Pool(procs) as pool:
            done = 0
            for j, r, dt in pool.imap_unordered(_run, [(work, j) for j in todo], chunksize=1):
                open(path(j), 'w').write(json.dumps(r, sort_keys=True))
                done += 1
                log(tag, f'[{time.strftime("%H:%M:%S")}] {done}/{len(todo)} {kap(j)} {dt:.0f}s {r.get("verdict", r.get("G2"))}')
    res = [json.load(open(path(j))) for j in jobs]
    blob = dump(res)
    open(artifact, 'w').write(blob)
    h = hashlib.sha256(blob.encode()).hexdigest()
    log(tag, f'ARTIFACT {os.path.relpath(artifact, RESULTS)}: {len(res)} records; sha256 {h}')
    return res, h


def _run(arg):
    work, j = arg
    t = time.time()
    return j, work(j), time.time() - t


def main():
    mode = sys.argv[1]
    if mode in ('A', 'B', 'C'):
        cell = sys.argv[2]
        procs = int(sys.argv[3]) if len(sys.argv) > 3 else 4
        jobs = {'A': A3B.jobs_A, 'B': A3B.jobs_B, 'C': A3B.jobs_C}[mode](cell)
        tag = f'stage{mode}_{cell}'
        if mode == 'B':
            log(tag, f'STAGE B {cell}: {len(jobs)} advancing kappa (advance rule on stageA_{cell}.json)')
        if mode == 'C':
            log(tag, f'STAGE C {cell}: selection {[j[1] for j in jobs]}')
        res, h = sweep(tag, jobs, A3B.analyze_A, lambda j: j[1], A3B.artifact(mode, cell), procs)
        for k, v in A3B.tally(res).items():
            log(tag, f'TALLY {mode} {cell}: {k}: {v}')
    elif mode == 'H':
        cell, H = sys.argv[2], sys.argv[3]
        procs = int(sys.argv[4]) if len(sys.argv) > 4 else 2
        tag = f'H_{cell}_{H}'
        res, h = sweep(tag, A3B.jobs_H(cell, H), A3B.analyze_H, lambda j: j[1], A3B.artifact('H', cell, H), procs)
        for k, v in A3B.tally(res).items():
            log(tag, f'TALLY H {cell} {H}: {k}: {v}')
        ninv_over = sum(1 for r in res if head(r['verdict']) == 'NOT-INVASIVE' and r.get('over_rank'))
        log(tag, f'TALLY H {cell} {H}: non-invasive kappa with rank > 4: {ninv_over}')
    elif mode == 'L':
        cell = sys.argv[2]
        procs = int(sys.argv[3]) if len(sys.argv) > 3 else 4
        import layers3
        rule = A3B.RUN_CELLS[cell]
        jobs = [(rule, k, 'oifsc', 'oimfsc', 3) for k in INTERFACES]
        tag = f'V10_{cell}'
        res, h = sweep(tag, jobs, layers3.check, lambda j: j[1], A3B.artifact('L', cell), procs)
        g2, g3n, g3i = (sum(r[f] for r in res) for f in ('G2', 'G3norm', 'G3idle'))
        log(tag, f'LAYERS {cell}: G2 {g2}/{len(res)}, G3norm {g3n}/{len(res)}, G3idle {g3i}/{len(res)}')
        log(tag, 'GATE V10 ' + ('OK' if g2 == g3n == g3i == len(res) == 143 else 'FAILED'))
    elif mode == 'RNS':
        procs = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        jobs = A3B.jobs_RNS()
        tag = 'V7'
        res, h = sweep(tag, jobs, A3B.analyze_A, lambda j: (j[0], j[1]), A3B.artifact('RNS'), procs)
        ok = True
        for j, r in zip(jobs, res):
            over = r.get('certified') and r['rank'] > 4
            ok &= bool(over)
            log(tag, f'CONTROL {j[0]} {j[1]}: rank {r.get("rank")} certified {r.get("certified")} dims {r.get("dimC")} '
                     f'{"OVER-RANK" if over else "NOT OVER-RANK"}')
        log(tag, 'GATE V7 ' + ('OK' if ok else 'FAILED'))
    elif mode == 'V6':
        sealed = sys.argv[2]
        tag = 'V6'
        blob = open(sealed, 'rb').read()
        hs = hashlib.sha256(blob).hexdigest()
        log(tag, f'sealed 3A Stage-A artifact {os.path.basename(sealed)} sha256 {hs}')
        ok = hs.startswith('9b88a7cc')
        if not ok:
            log(tag, 'GATE V6 FAILED (sealed artifact hash)')
            sys.exit(1)
        by = {kappa_key(r): r for r in json.loads(blob)}
        picks = [INTERFACES[p] for p in A3B.REPLAY_POS] + [((0, 1), (0, 1))]
        picks = list(dict.fromkeys(picks))
        kept = []
        for k in picks:
            r = A3B.analyze_A(('linear', k, 3, 3, 'A'))
            same = json.dumps(r, sort_keys=True) == json.dumps(by[k], sort_keys=True)
            ok &= same
            kept.append(by[k])
            log(tag, f'V6 {k} {r["verdict"]} rank {r["rank"]} dims {r.get("dimC")} {"MATCH" if same else "MISMATCH"}')
        os.makedirs(RESULTS, exist_ok=True)
        open(os.path.join(RESULTS, 'v6_sealed_entries.json'), 'w').write(dump(kept))
        log(tag, f'V6 {len(picks)} jobs; GATE V6 ' + ('OK' if ok else 'FAILED'))
    else:
        raise SystemExit(__doc__)


if __name__ == '__main__':
    main()
