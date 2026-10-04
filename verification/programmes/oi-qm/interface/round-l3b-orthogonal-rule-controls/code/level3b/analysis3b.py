"""Level 3B analysis layer on the unchanged 3A analysis (analysis3.analyze): the cells, the job lists per stage
(the advance and Stage-C rules of preregistration section 4 applied to the cell's own artifacts), the Block-2 label
mapping of section 6, artifact paths and the frozen serialization.

Nothing here changes a criterion: rank, WELLDEF, invasiveness and the dims come from analysis3.analyze; Block 1
verdicts are analysis3's; Block 2 relabels the Stage-A record exactly as section 6 prescribes.
"""
import os
import sys
import json
import hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)
ROUND = os.path.dirname(CODE)
RESULTS = os.path.join(ROUND, 'results')
LOGS = os.path.join(ROUND, 'logs')
for sub in ('record', 'level3', 'quotient', 'level3b'):
    p = os.path.join(CODE, sub)
    if p not in sys.path:
        sys.path.insert(0, p)
os.chdir(HERE)                      # the sealed quotient modules locate ../rank relative to the working directory
import rules3b                      # noqa: E402,F401  (installs F3B)
import analysis3                    # noqa: E402
from analysis3 import INTERFACES, HORIZON, kappa_key, analyze   # noqa: E402,F401
import record3_fast                 # noqa: E402
import hsim3b                       # noqa: E402

RUN_CELLS = {'R_LS': 'LS', 'R_NL': 'NL', 'R_5': 'R5'}                      # Block 1, run
H_CELLS = {'R_LL': 'linear', 'R_LS': 'LS', 'R_NL': 'NL', 'R_5': 'R5'}     # Block 2 rule cells
RNS_CELLS = {'R_NS-n': 'nonlinear', 'R_NS-m': 'majority'}                 # positive controls (V7)
HS = ('H1', 'H2')
CONTROL_POS = (0, 71, 142)
REPLAY_POS = (0, 18, 36, 54, 72, 90, 108, 126, 142)
BLOCK1_A = ('ADVANCE', 'OVER-RANK', 'NOT-INVASIVE', 'INCONCLUSIVE')
BLOCK1_B = ('AT-RANK', 'AT-RANK(unequal)', 'OVER-RANK', 'UNDER-RANK', 'NOT-INVASIVE', 'INCONCLUSIVE')
BLOCK1_C = ('C-CONSISTENT', 'OVER-RANK', 'NOT-INVASIVE', 'INCONCLUSIVE')
BLOCK2 = ('OVER-RANK', 'NO-OVER-RANK-AT-A', 'NOT-INVASIVE', 'INCONCLUSIVE')


def head(verdict):
    """The label without its parenthesized detail, except AT-RANK(unequal), which is its own label."""
    return verdict if verdict == 'AT-RANK(unequal)' else verdict.split('(')[0]


def artifact(kind, cell=None, H=None):
    if kind in ('A', 'B', 'C'):
        return os.path.join(RESULTS, f'stage{kind}_{cell}.json')
    if kind == 'L':
        return os.path.join(RESULTS, f'layers_{cell}.json')
    if kind == 'H':
        return os.path.join(RESULTS, f'H_{cell}_{H}.json')
    if kind == 'RNS':
        return os.path.join(RESULTS, 'controls_RNS.json')
    raise ValueError(kind)


def load(path):
    return json.load(open(path))


def dump(res):
    return json.dumps(res, sort_keys=True, indent=0)


def sha(blob):
    return hashlib.sha256(blob.encode() if isinstance(blob, str) else blob).hexdigest()


def jobs_A(cell):
    rule = RUN_CELLS[cell]
    Lp, Le = HORIZON['A']
    return [(rule, k, Lp, Le, 'A') for k in INTERFACES]


def advancing(cell):
    """The advance rule of section 4 on the cell's Stage-A artifact: invasive and certified dim C_2 <= 4."""
    prev = load(artifact('A', cell))
    adv = {kappa_key(r) for r in prev if r.get('invasive') and r.get('dimC') and r['dimC'][-1] <= 4}
    return [k for k in INTERFACES if k in adv]


def jobs_B(cell):
    rule = RUN_CELLS[cell]
    Lp, Le = HORIZON['B']
    return [(rule, k, Lp, Le, 'B') for k in advancing(cell)]


def stage_c_selection(cell):
    """Section 4: the first three AT-RANK kappa and the first UNDER-RANK kappa (if any), frozen order, from Stage B."""
    by = {kappa_key(r): r for r in load(artifact('B', cell))}
    at = [k for k in INTERFACES if k in by and by[k]['verdict'] == 'AT-RANK'][:3]
    under = [k for k in INTERFACES if k in by and by[k]['verdict'].startswith('UNDER-RANK')][:1]
    return at + under


def jobs_C(cell):
    rule = RUN_CELLS[cell]
    Lp, Le = HORIZON['C']
    return [(rule, k, Lp, Le, 'C') for k in stage_c_selection(cell)]


def jobs_H(cell, H):
    rule = H_CELLS[cell]
    Lp, Le = HORIZON['A']
    return [(rule, k, Lp, Le, 'A', H) for k in INTERFACES]


def jobs_RNS():
    Lp, Le = HORIZON['A']
    return [(rule, INTERFACES[p], Lp, Le, 'A') for cell, rule in RNS_CELLS.items() for p in CONTROL_POS]


def analyze_A(job):
    """Block 1 (and V6/V7): the unchanged analysis on the window simulator."""
    analysis3.RUN_ALL = record3_fast.run_all3
    return analyze(job)


def label_H(rec, H):
    """Section 6: the Block-2 label on analysis3's Stage-A record; the original Stage-A verdict is kept as verdict_A."""
    rec = dict(rec)
    rec['H'] = H
    rec['verdict_A'] = rec['verdict']
    if not rec.get('certified'):
        rec['verdict'] = 'INCONCLUSIVE(rank)'
    elif not rec['invasive']:
        rec['verdict'] = f'NOT-INVASIVE(rank {rec["rank"]})'
    elif rec['over_rank']:
        rec['verdict'] = f'OVER-RANK(rank {rec["rank"]}, dims {rec["dimC"]})'
    else:
        rec['verdict'] = f'NO-OVER-RANK-AT-A(dims {rec["dimC"]})'
    return rec


def analyze_H(job):
    rule, k, Lp, Le, stage, H = job
    analysis3.RUN_ALL = hsim3b.make_run_all(H)
    rec = analyze((rule, k, Lp, Le, stage))
    analysis3.RUN_ALL = record3_fast.run_all3
    return label_H(rec, H)


def over_rank_kappas(cell):
    """Kappa OVER-RANK at any stage of the cell (Stage-A dims > 4, Stage-B or Stage-C verdict OVER-RANK)."""
    over = set()
    for kind in ('A', 'B', 'C'):
        p = artifact(kind, cell)
        if os.path.exists(p):
            for r in load(p):
                if head(r['verdict']) == 'OVER-RANK':
                    over.add(kappa_key(r))
    return over


def cell_label(cell):
    """Section 5's cell label from the cell's artifacts."""
    A = load(artifact('A', cell))
    B = load(artifact('B', cell)) if os.path.exists(artifact('B', cell)) else []
    over = over_rank_kappas(cell)
    if over:
        return 'OVER'
    at = [r for r in B if head(r['verdict']) in ('AT-RANK', 'AT-RANK(unequal)')]
    inc = [r for r in A + B if head(r['verdict']) == 'INCONCLUSIVE']
    if at:
        return 'EXPOSED'
    if inc:
        return 'INCONCLUSIVE'
    return 'NOT-EXPOSED'


def decision_row(labels):
    """Section 3.2 read in order; labels: dict cell -> label."""
    ls, nl, r5 = labels['R_LS'], labels['R_NL'], labels['R_5']
    if 'INCONCLUSIVE' in (ls, nl, r5):
        return None
    no = lambda x: x in ('EXPOSED', 'NOT-EXPOSED')
    if no(ls) and nl == 'OVER' and no(r5):
        return 1
    if no(ls) and nl == 'OVER' and r5 == 'OVER':
        return 2
    if ls == 'OVER':
        return 3
    if no(nl):
        return 4
    return None


def tally(records):
    t = {}
    for r in records:
        t[head(r['verdict'])] = t.get(head(r['verdict']), 0) + 1
    return dict(sorted(t.items()))
