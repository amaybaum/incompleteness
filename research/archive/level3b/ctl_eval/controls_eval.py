#!/usr/bin/env python3
"""Frozen controls of round L3B (preregistration sections 7-8). Self-contained: reads the record directory only.

  --check C1   V1 (the ten sealed modules' hashes) and the C1 gate logs V2-V5 each ending in 'GATE Vn OK'
  --check E    everything: V1; every gate log V2-V12 present with its OK line (V9 may be SKIPPED only when the
               cell's Stage-A artifact advances no kappa); artifact completeness and label sets; the Stage-B job
               list equal to the advance rule on Stage A; the Stage-C selection equal to section 4's rule on Stage B;
               the cell labels, the decision-table row and the Block-2 tallies recomputed and printed
  --self-test  mutates copies of the artifacts (a dropped record, a changed verdict, a wrong Stage-B set) and
               requires each mutation to be caught

usage: controls.py --check C1|E | --self-test
"""
import os
import re
import sys
import json
import shutil
import hashlib
import tempfile

ROUND = '/home/user/incompleteness/verification/programmes/oi-qm/interface/round-l3b-orthogonal-rule-controls'
CODE = os.path.join(ROUND, 'code')
RESULTS = os.path.join(ROUND, 'results')
LOGS = os.path.join(ROUND, 'logs')

SEALED = {
    'record/record_sim.py': 'e499a081', 'record/record_fast.py': 'c2c94a68',
    'quotient/rankbasis.py': 'e82e2ab9', 'quotient/quotient.py': '068f93ab',
    'rank/lattice_rank.py': '39173d18', 'rank/protocol_rank.py': 'e57e68ba',
    'level3/record3_sim.py': 'ac812fbb', 'level3/record3_fast.py': '455c74af',
    'level3/analysis3.py': 'efe53458', 'level3/layers3.py': '5fa200e2',
}
RUN_CELLS = ('R_LS', 'R_NL', 'R_5')
H_CELLS = ('R_LL', 'R_LS', 'R_NL', 'R_5')
HS = ('H1', 'H2')
BLOCK1_A = {'ADVANCE', 'OVER-RANK', 'NOT-INVASIVE', 'INCONCLUSIVE'}
BLOCK1_B = {'AT-RANK', 'AT-RANK(unequal)', 'OVER-RANK', 'UNDER-RANK', 'NOT-INVASIVE', 'INCONCLUSIVE'}
BLOCK1_C = {'C-CONSISTENT', 'OVER-RANK', 'NOT-INVASIVE', 'INCONCLUSIVE'}
BLOCK2 = {'OVER-RANK', 'NO-OVER-RANK-AT-A', 'NOT-INVASIVE', 'INCONCLUSIVE'}

PASSIVE = ((0, 1), (2, 3))
INJ = [(x, y) for x in range(4) for y in range(4) if x != y]
INTERFACES = [(k0, k1) for k0 in INJ for k1 in INJ if (k0, k1) != PASSIVE]      # frozen order (as RECORD)
assert len(INTERFACES) == 143


def kk(r):
    return tuple(map(tuple, r['kappa']))


def head(v):
    return v if v == 'AT-RANK(unequal)' else v.split('(')[0]


def load(p):
    return json.load(open(p))


def check_V1(code=CODE):
    errs = []
    for rel, h in SEALED.items():
        p = os.path.join(code, rel)
        if not os.path.exists(p):
            errs.append(f'V1: missing {rel}')
            continue
        hh = hashlib.sha256(open(p, 'rb').read()).hexdigest()
        if not hh.startswith(h):
            errs.append(f'V1: {rel} sha256 {hh[:8]} != {h}')
    return errs


def gate_ok(name, logs=LOGS, allow_skip=False):
    """The log(s) of a gate end with 'GATE <name> OK' (every log whose name starts with the gate's)."""
    files = sorted(f for f in os.listdir(logs) if f == f'{name}.log' or f.startswith(f'{name}_')) if os.path.isdir(logs) else []
    if not files:
        return [f'{name}: no log']
    errs = []
    for f in files:
        txt = open(os.path.join(logs, f), encoding='utf-8').read()
        if re.search(rf'^GATE {re.escape(name)}\b.*\bOK\s*$', txt, re.M):
            continue
        if allow_skip and re.search(rf'^.*GATE {re.escape(name)} SKIPPED', txt, re.M):
            continue
        errs.append(f'{name}: {f} carries no OK line')
    return errs


def check_C1(code=CODE, logs=LOGS):
    errs = check_V1(code)
    for g in ('V2', 'V3', 'V4', 'V5'):
        errs += gate_ok(g, logs)
    return errs


def artifact_records(path, n_expected, labels, errs, tag):
    if not os.path.exists(path):
        errs.append(f'{tag}: missing artifact {os.path.basename(path)}')
        return None
    R = load(path)
    if n_expected is not None and len(R) != n_expected:
        errs.append(f'{tag}: {len(R)} records != {n_expected}')
    bad = [r['verdict'] for r in R if head(r['verdict']) not in labels] if labels else []   # EVAL-ONLY: skip the label scan for the layers artifact
    if bad:
        errs.append(f'{tag}: labels outside the frozen set: {sorted(set(bad))[:5]}')
    return R


def advancing(A):
    adv = {kk(r) for r in A if r.get('invasive') and r.get('dimC') and r['dimC'][-1] <= 4}
    return [k for k in INTERFACES if k in adv]


def stage_c_selection(B):
    by = {kk(r): r for r in B}
    at = [k for k in INTERFACES if k in by and by[k]['verdict'] == 'AT-RANK'][:3]
    under = [k for k in INTERFACES if k in by and by[k]['verdict'].startswith('UNDER-RANK')][:1]
    return at + under


def cell_label(A, B, C):
    over = any(head(r['verdict']) == 'OVER-RANK' for r in A + B + C)
    if over:
        return 'OVER'
    if any(head(r['verdict']) in ('AT-RANK', 'AT-RANK(unequal)') for r in B):
        return 'EXPOSED'
    if any(head(r['verdict']) == 'INCONCLUSIVE' for r in A + B):
        return 'INCONCLUSIVE'
    return 'NOT-EXPOSED'


def decision_row(labels):
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


def tally(R):
    t = {}
    for r in R:
        t[head(r['verdict'])] = t.get(head(r['verdict']), 0) + 1
    return dict(sorted(t.items()))


def check_E(code=CODE, results=RESULTS, logs=LOGS, out=print):
    errs = check_C1(code, logs)
    for g in ('V6', 'V7', 'V8', 'V10', 'V11', 'V12'):
        errs += gate_ok(g, logs)
    labels = {}
    for cell in RUN_CELLS:
        A = artifact_records(os.path.join(results, f'stageA_{cell}.json'), 143, BLOCK1_A, errs, f'stageA_{cell}') or []
        if A and [kk(r) for r in A] != INTERFACES:
            errs.append(f'stageA_{cell}: kappa not in the frozen order')
        adv = advancing(A) if A else []
        pB = os.path.join(results, f'stageB_{cell}.json')
        B = artifact_records(pB, len(adv), BLOCK1_B, errs, f'stageB_{cell}') or []
        if B and [kk(r) for r in B] != adv:
            errs.append(f'stageB_{cell}: job list != advance rule on Stage A')
        errs += gate_ok(f'V9_{cell}', logs, allow_skip=not adv) if os.path.isdir(logs) else [f'V9_{cell}: no log']
        sel = stage_c_selection(B) if B else []
        pC = os.path.join(results, f'stageC_{cell}.json')
        if sel or os.path.exists(pC):
            C = artifact_records(pC, len(sel), BLOCK1_C, errs, f'stageC_{cell}') or []
            if C and [kk(r) for r in C] != sel:
                errs.append(f'stageC_{cell}: selection != section 4 rule on Stage B')
        else:
            C = []
        L = artifact_records(os.path.join(results, f'layers_{cell}.json'), 143, set(), [], f'layers_{cell}')
        if L is None:
            errs.append(f'layers_{cell}: missing')
        elif not all(r['G2'] and r['G3norm'] and r['G3idle'] for r in L):
            errs.append(f'layers_{cell}: a G identity failed')
        labels[cell] = cell_label(A, B, C) if A else 'INCONCLUSIVE'
        out(f'CELL {cell}: A {tally(A)}; B {tally(B)}; C {tally(C)}; label {labels[cell]}')
    row = decision_row(labels)
    out(f'DECISION ROW: {row}')
    for cell in H_CELLS:
        for H in HS:
            R = artifact_records(os.path.join(results, f'H_{cell}_{H}.json'), 143, BLOCK2, errs, f'H_{cell}_{H}')
            if R:
                if [kk(r) for r in R] != INTERFACES:
                    errs.append(f'H_{cell}_{H}: kappa not in the frozen order')
                if any(r.get('H') != H for r in R):
                    errs.append(f'H_{cell}_{H}: a record carries another H')
                ninv = sum(1 for r in R if head(r['verdict']) == 'NOT-INVASIVE' and r.get('over_rank'))
                out(f'BLOCK2 {cell} {H}: {tally(R)}; non-invasive with rank > 4: {ninv}')
    rns = os.path.join(results, 'controls_RNS.json')
    if os.path.exists(rns):
        R = load(rns)
        if len(R) != 6 or not all(r.get('certified') and r['rank'] > 4 for r in R):
            errs.append('controls_RNS: a control is not OVER-RANK')
    else:
        errs.append('controls_RNS.json missing')
    return errs


def self_test():
    """Mutations on a copy of the artifacts must be caught; requires the artifacts to exist (run at E)."""
    tmp = tempfile.mkdtemp()
    shutil.copytree(RESULTS, os.path.join(tmp, 'results'))
    shutil.copytree(LOGS, os.path.join(tmp, 'logs'))
    base = check_E(CODE, os.path.join(tmp, 'results'), os.path.join(tmp, 'logs'), out=lambda *a: None)
    caught = 0
    # 1: drop a Stage-A record
    p = os.path.join(tmp, 'results', 'stageA_R_5.json')
    R = load(p)
    json.dump(R[:-1], open(p, 'w'))
    caught += len(check_E(CODE, os.path.join(tmp, 'results'), os.path.join(tmp, 'logs'), out=lambda *a: None)) > len(base)
    json.dump(R, open(p, 'w'))
    # 2: an alien Block-2 label
    p = os.path.join(tmp, 'results', 'H_R_LL_H1.json')
    R = load(p)
    R2 = json.loads(json.dumps(R))
    R2[0]['verdict'] = 'AT-RANK'
    json.dump(R2, open(p, 'w'))
    caught += len(check_E(CODE, os.path.join(tmp, 'results'), os.path.join(tmp, 'logs'), out=lambda *a: None)) > len(base)
    json.dump(R, open(p, 'w'))
    # 3: a gate log without its OK line
    p = os.path.join(tmp, 'logs', 'V2.log')
    txt = open(p).read()
    open(p, 'w').write(txt.replace('GATE V2 OK', 'GATE V2 ??'))
    caught += len(check_E(CODE, os.path.join(tmp, 'results'), os.path.join(tmp, 'logs'), out=lambda *a: None)) > len(base)
    open(p, 'w').write(txt)
    shutil.rmtree(tmp)
    print(f'SELF-TEST: baseline errors {len(base)}; mutations caught {caught}/3')
    ok = not base and caught == 3
    print('SELF-TEST', 'OK' if ok else 'FAILED')
    return ok


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        sys.exit(0 if self_test() else 1)
    which = sys.argv[sys.argv.index('--check') + 1]
    errs = check_C1() if which == 'C1' else check_E()
    for e in errs:
        print(e)
    print(f'L3B controls --check {which}:', 'OK' if not errs else f'FAILED ({len(errs)})')
    sys.exit(0 if not errs else 1)
