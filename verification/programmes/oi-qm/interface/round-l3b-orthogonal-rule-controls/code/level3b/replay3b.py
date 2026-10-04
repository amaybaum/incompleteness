"""Replays of preregistration section 7.3 (gates V8, V9, V11), each compared field by field with the artifact record.

usage: replay3b.py A <cell>             V8: Stage-A replay on the reference simulator (record3_sim.run3 through the
                                        unchanged analysis3.analyze with RUN_ALL swapped): the nine positions
                                        0, 18, ..., 142 plus the first kappa in frozen order of each verdict class
                                        not yet covered
       replay3b.py B <cell> [procs]     V9: the complete Stage-B job for kappa ((0,1),(0,1)) if it advanced, else the
                                        first advancing kappa; reference table in resumable 2000-protocol chunks,
                                        then the unchanged analyze on it (SKIPPED if no kappa advanced)
       replay3b.py H <cell> <H1|H2>     V11: at positions 0, 71, 142: run_all_H == run_H on the full Stage-A set;
                                        both == brute force on the first 40 Stage-A protocols (lexicographic) with
                                        <= 3 leaps; the H0 record of the same kappa under the enumerator == the
                                        window-simulator record (sealed 3A entry for R_LL, given as argv[4]; the
                                        Block-1 Stage-A artifact for the other cells)
"""
import os
import sys
import json
import time
from fractions import Fraction as Fr
from itertools import product
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import analysis3b as A3B                                                        # noqa: E402
from analysis3b import INTERFACES, HORIZON, kappa_key, RESULTS, LOGS, dump    # noqa: E402
import analysis3                                                                # noqa: E402
from analysis3 import protocols, PALPH, EALPH                                   # noqa: E402
from record3_sim import run3                                                    # noqa: E402
import record3_fast                                                             # noqa: E402
import hsim3b                                                                   # noqa: E402
import validate3b                                                               # noqa: E402

CK_ROOT = os.environ.get('L3B_CKPT') or os.path.join(os.path.expanduser('~'), '.l3b_ckpt')


def log(tag, line):
    os.makedirs(LOGS, exist_ok=True)
    print(line, flush=True)
    with open(os.path.join(LOGS, f'{tag}.log'), 'a') as fh:
        fh.write(line + '\n')


def same_record(a, b):
    return json.dumps(a, sort_keys=True) == json.dumps(b, sort_keys=True)


def replay_A(cell):
    tag = f'V8_{cell}'
    rule = A3B.RUN_CELLS[cell]
    by = {kappa_key(r): r for r in A3B.load(A3B.artifact('A', cell))}
    pick = [INTERFACES[i] for i in A3B.REPLAY_POS]
    seen = {by[k]['verdict'] for k in pick}
    for k in INTERFACES:
        if by[k]['verdict'] not in seen:
            pick.append(k)
            seen.add(by[k]['verdict'])
    Lp, Le = HORIZON['A']
    analysis3.RUN_ALL = lambda ps, rule_, kappa: {p: run3(p, rule_, kappa) for p in set(ps)}
    bad = 0
    for k in pick:
        o = analysis3.analyze((rule, k, Lp, Le, 'A'))
        same = same_record(o, by[k])
        bad += not same
        log(tag, f'REPLAY-A {cell} {k} {o["verdict"]} rank {o["rank"]} {"MATCH" if same else "MISMATCH"}')
    analysis3.RUN_ALL = record3_fast.run_all3
    log(tag, f'REPLAY-A {cell} {len(pick)} jobs, mismatches {bad}; GATE V8 ' + ('OK' if bad == 0 else 'FAILED'))
    return bad == 0


def _chunk(arg):
    i, prs, rule, kappa, ck = arg
    fn = os.path.join(ck, f'ref_{i:04d}.json')
    if os.path.exists(fn):
        return i, 0.0
    t = time.time()
    out = {p: run3(p, rule, kappa) for p in prs}
    open(fn, 'w').write(json.dumps(out, sort_keys=True))
    return i, time.time() - t


def replay_B(cell, procs):
    tag = f'V9_{cell}'
    rule = A3B.RUN_CELLS[cell]
    adv = A3B.advancing(cell)
    if not adv:
        log(tag, f'REPLAY-B {cell}: no kappa advanced from Stage A; GATE V9 SKIPPED (recorded)')
        return True
    kappa = ((0, 1), (0, 1)) if ((0, 1), (0, 1)) in adv else adv[0]
    Lp, Le = HORIZON['B']
    PS = sorted({a + b for a in protocols(PALPH, Lp) for b in protocols(EALPH, Le)})
    chunks = [PS[i:i + 2000] for i in range(0, len(PS), 2000)]
    ck = os.path.join(CK_ROOT, tag)
    os.makedirs(ck, exist_ok=True)
    todo = [i for i in range(len(chunks)) if not os.path.exists(os.path.join(ck, f'ref_{i:04d}.json'))]
    log(tag, f'REPLAY-B {cell} {kappa}: {len(PS)} protocols, {len(chunks)} chunks, {len(todo)} to run, {procs} procs')
    if todo:
        with Pool(procs) as pool:
            n = 0
            for i, dt in pool.imap_unordered(_chunk, [(i, chunks[i], rule, kappa, ck) for i in todo], chunksize=1):
                n += 1
                log(tag, f'[{time.strftime("%H:%M:%S")}] chunk {i} {dt:.0f}s ({n}/{len(todo)})')
    J = {}
    for i in range(len(chunks)):
        J.update({p: tuple(v) for p, v in json.load(open(os.path.join(ck, f'ref_{i:04d}.json'))).items()})
    assert set(J) == set(PS)
    analysis3.RUN_ALL = lambda ps, rule_, kappa_: {p: (list(J[p][0]), J[p][1]) for p in set(ps)}
    ref = {kappa_key(r): r for r in A3B.load(A3B.artifact('B', cell))}[kappa]
    o = analysis3.analyze((rule, kappa, Lp, Le, 'B'))
    analysis3.RUN_ALL = record3_fast.run_all3
    same = same_record(o, ref)
    log(tag, f'REPLAY-B {cell} {kappa} {o["verdict"]} rank {o["rank"]} dims {o["dimC"]} {"MATCH" if same else "MISMATCH"}; '
             'GATE V9 ' + ('OK' if same else 'FAILED'))
    return same


def norm(counts, mass):
    return tuple(Fr(c, mass) for c in counts)


def replay_H(cell, H, sealed=None):
    tag = f'V11_{cell}_{H}'
    rule = A3B.H_CELLS[cell]
    Lp, Le = HORIZON['A']
    pps, pes = protocols(PALPH, Lp), protocols(EALPH, Le)
    allp = [a + b for a in pps for b in pes]
    small = [p for p in sorted(allp) if sum(1 for s in p if s in 'oim') <= 3][:40]
    if cell == 'R_LL':
        ref_by = {kappa_key(r): r for r in json.load(open(sealed))}
    else:
        ref_by = {kappa_key(r): r for r in A3B.load(A3B.artifact('A', cell))}
    ok = True
    for pos in A3B.CONTROL_POS:
        k = INTERFACES[pos]
        J = hsim3b.run_all_H(allp, rule, k, H)
        m1 = sum(1 for p in allp if norm(*J[p]) != norm(*hsim3b.run_H(p, rule, k, H)))
        m2 = sum(1 for p in small if norm(*J[p]) != validate3b.brute(p, rule, k, H))
        analysis3.RUN_ALL = hsim3b.make_run_all('H0')
        r0 = analysis3.analyze((rule, k, Lp, Le, 'A'))
        analysis3.RUN_ALL = record3_fast.run_all3
        m3 = not same_record(r0, ref_by[k])
        ok &= (m1 == 0 and m2 == 0 and not m3)
        log(tag, f'REPLAY-H {cell} {H} {k}: trie-vs-single mismatches {m1}/{len(allp)}; brute mismatches {m2}/{len(small)}; '
                 f'H0 record {"MATCH" if not m3 else "MISMATCH"}')
    log(tag, f'GATE V11 ({cell}, {H}) ' + ('OK' if ok else 'FAILED'))
    return ok


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'A':
        ok = replay_A(sys.argv[2])
    elif mode == 'B':
        ok = replay_B(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 2)
    elif mode == 'H':
        ok = replay_H(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
    else:
        raise SystemExit(__doc__)
    sys.exit(0 if ok else 1)
