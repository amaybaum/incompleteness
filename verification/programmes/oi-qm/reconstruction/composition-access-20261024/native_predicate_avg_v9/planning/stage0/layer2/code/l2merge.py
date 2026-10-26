"""NP-AVG-1 Stage 0 Layer 2: the merge, the label generator and rule T (section 5b items 5-7;
sections 5, 7 and 12).

Usage: python3 -I -B l2merge.py --profile toy|v8 --workdir DIR
Reads only structured files in DIR (dryrun.json, preflight.json, s1a.json and s1a.O.json,
shard-<s>.json and shard-<s>.O.json) and writes DIR/result.json (result.O.json under -O),
DIR/expected-controls.json and, when survivors exist, DIR/residue.json. Labels are generated
here and nowhere else, from those files' fields and the producing steps' recorded results;
no log text is read (section A.44). Exit status 0 when a label was written.
"""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l2config as CFG    # noqa: E402
import l2manifest as MAN  # noqa: E402
import l2plan as PLAN     # noqa: E402
import l2analysis as AN   # noqa: E402

VOID_GATES = ('C0_context', 'C7', 'C8', 'C11i', 'C17', 'C18')
MISMATCH_GATES = ('C9', 'C10i', 'C11ii')


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


def read(path):
    try:
        with open(path, 'rb') as f:
            raw = f.read()
        return raw, json.loads(raw)
    except (OSError, ValueError):
        return None, None


def label(void, mismatch, incomplete, base_collapsed, surv_A, surv_G, linked_A, linked_G):
    """Section 5, first match. Inputs are lists of reasons and integers read from structured
    files. BASE_RESIDUE follows INCOMPLETE; note that a non-collapsed base also disagrees with
    C6's hand derivation, which is a MISMATCH and so takes precedence (LAYER2-PLAN.md
    section 9, finding F1)."""
    if void:
        return 'VOID'
    if mismatch:
        return 'MISMATCH'
    if incomplete:
        return 'INCOMPLETE'
    if not base_collapsed:
        return 'BASE_RESIDUE'
    if surv_A == 0 and surv_G == 0:
        return 'COLLAPSE_ALL'
    if linked_A == 0 and linked_G == 0:
        return 'RESIDUE_UNLINKED'
    return 'RESIDUE'


def coverage_ok(ranges, N, S):
    """The accepted shards' ranges are a disjoint exact cover of [0, N) by S ranges."""
    r = sorted(tuple(x) for x in ranges)
    return len(r) == S and r[0][0] == 0 and r[-1][1] == N and all(r[i][1] == r[i + 1][0] for i in range(len(r) - 1)) \
        and all(lo <= hi for lo, hi in r)


def recount_ok(weight, N, nreps, orbits):
    """Orbit weights sum to N and the representatives number the orbits (PO-L2-2)."""
    return weight == N and nreps == orbits


def minimal_witness(cands):
    """C16 order: k, then the number of even-class context quantities, then the sorted items."""
    return min(cands, key=lambda w: (w['key'][0], w['key'][1], w['key'][2])) if cands else None


def rule_T(s1a_status, L_A, L_G):
    """Rule T (section 12), exactly as frozen. Its only inputs are S1a's validity and the two
    counts; the k <= 2 label is not an argument (neutrality)."""
    T = CFG.CONFIG['rule_T']
    base = {'wording_status': T['wording_status'], 'L_A': L_A, 'L_G': L_G, 's1a_status': s1a_status,
            'cost_clause': 'not evaluable in Stage 0: the clause refers to the dry-run cost estimate of the search '
                           '(S1b or S1c), and no such dry run exists before S1b is preregistered'}
    if s1a_status != 'OK':
        return dict(base, evaluated=False, outcome='not_evaluated', S1b_S1c='not proposed', text=T['not_evaluated_text'])
    if L_A == 0 and L_G == 0:
        return dict(base, evaluated=True, outcome='L_A = L_G = 0', S1b_S1c='not undertaken', text=T['zero_text'],
                    scope_of_statement='geometric fact only; no law statement for k > 2')
    return dict(base, evaluated=True, outcome='L_A > 0 or L_G > 0', S1b_S1c='S1b put to the owner as a new '
                'preregistration', text=T['positive_text'])


def merge(pname, workdir):
    prof = CFG.profile(pname)
    void, mism, inc = [], [], []
    ok, diffs, man = MAN.verify(HERE)
    if not ok:
        void.append('certificate item 1: manifest mismatch')
    cd = man.get('code_digest') if man else None
    draw, dry = read(os.path.join(workdir, 'dryrun.json'))
    praw, pf = read(os.path.join(workdir, 'preflight.json'))
    sraw, s1a = read(os.path.join(workdir, 's1a.json'))
    sOraw, _ = read(os.path.join(workdir, 's1a.O.json'))
    inputs = {}
    if dry is None:
        inc.append('dryrun.json missing')
    else:
        inputs['dryrun.json'] = sha_bytes(draw)
    # pre-flight (certificate item 2)
    base_collapsed = False
    if pf is None:
        void.append('preflight.json missing')
    else:
        inputs['preflight.json'] = sha_bytes(praw)
        if pf.get('code_digest') != cd:
            void.append('preflight code_digest differs')
        for name, c in sorted(pf.get('controls', {}).items()):
            if not c.get('pass'):
                (mism if c.get('class') == 'MISMATCH' else void).append('preflight:' + name)
        bc = pf.get('base_collapsed', {})
        base_collapsed = bc.get('A') is True and bc.get('G') is True
    # S1a
    if s1a is None:
        s1a_status = 'INCOMPLETE'
        inc.append('s1a.json missing')
    else:
        inputs['s1a.json'] = sha_bytes(sraw)
        s1a_status = s1a.get('status', 'INCOMPLETE')
        if sOraw != sraw:
            s1a_status = 'INCOMPLETE'
            inc.append('s1a: normal and -O outputs differ or -O output missing')
        if s1a.get('code_digest') != cd or s1a.get('config_sha256') != CFG.config_sha256():
            s1a_status = 'INCOMPLETE'
            inc.append('s1a: digests differ from the manifest')
        if s1a.get('status') == 'VOID':
            void.append('S1a reference checks: %s' % s1a.get('status_reasons'))
        elif s1a.get('status') == 'MISMATCH':
            mism.append('S1a: %s' % s1a.get('status_reasons'))
    # shards (certificate item 5)
    S = len(dry['shards']) if dry else prof['shards']
    N = dry['records'] if dry else None
    shards, commits = [], set()
    for s in range(S):
        raw, sh = read(os.path.join(workdir, 'shard-%d.json' % s))
        rawO, _ = read(os.path.join(workdir, 'shard-%d.O.json' % s))
        if sh is None:
            inc.append('shard %d missing or unreadable' % s)
            continue
        body = dict(sh)
        claimed = body.pop('sha256', None)
        why = []
        if claimed != sha_bytes(CFG.canonical(body).encode()):
            why.append('self-digest')
        if sh.get('schema') != 'np-avg-1/stage0/layer2/shard/1' or sh.get('profile') != pname or sh.get('shard') != s:
            why.append('identity')
        if sh.get('code_digest') != cd or sh.get('config_sha256') != CFG.config_sha256():
            why.append('code or configuration digest')
        if dry and sh.get('dryrun_sha256') != sha_bytes(draw):
            why.append('dry-run digest')
        if s1a is not None and sh.get('s1a_sha256') != sha_bytes(sraw):
            why.append('S1a digest')
        if dry and sh.get('range') != [dry['shards'][s]['lo'], dry['shards'][s]['hi']]:
            why.append('range differs from the plan')
        if sh.get('range') and sh.get('scanned') != sh['range'][1] - sh['range'][0]:
            why.append('scanned count')
        if rawO != raw:
            why.append('normal and -O outputs differ or -O output missing')
        if why:
            inc.append('shard %d refused: %s' % (s, ', '.join(why)))
            continue
        commits.add(sh.get('commit'))
        shards.append(sh)
        inputs['shard-%d.json' % s] = claimed
    if len(commits) > 1:
        inc.append('shards from different commits')
    # coverage: disjoint, exact union, recount by orbit weight and by Burnside's orbit count
    cov = {'records': N, 'shards_expected': S, 'shards_accepted': len(shards)}
    if dry:
        union_ok = bool(shards) and coverage_ok([sh['range'] for sh in shards], N, S)
        weight = sum(sh['orbit_weight'] for sh in shards)
        nreps = sum(sh['representatives'] for sh in shards)
        cov.update(exact_disjoint_union=union_ok, orbit_weight_sum=weight, representatives=nreps,
                   orbits_burnside=dry['orbits'])
        if not union_ok:
            inc.append('coverage: shard ranges are not a disjoint exact cover of [0, N)')
        if not recount_ok(weight, N, nreps, dry['orbits']):
            inc.append('recount: orbit weight %d (N = %d), representatives %d (orbits = %d)' %
                       (weight, N, nreps, dry['orbits']))
    # counts
    counts = {k: 0 for k in AN.count_keys()}
    classes = {}
    gates = {}
    base_rel = {'A': 0, 'G': 0}
    l3only = {'A': 0, 'G': 0}
    witnesses, survivors, auth = [], [], None
    for sh in shards:
        for k, v in sh['counts_additive'].items():
            counts[k] += v
        for k, lst in sh['class_keys'].items():
            d = classes.setdefault(k, {})
            for key, osz in lst:
                d[tuple(key)] = osz
        for g, t in sh['gates'].items():
            acc = gates.setdefault(g, {})
            for kk, vv in t.items():
                acc[kk] = acc.get(kk, 0) + vv
        for conv in ('A', 'G'):
            base_rel[conv] += sh['base_relative_survivor_records'][conv]
            l3only[conv] += sh['L3_only_survivor_records'][conv]
        witnesses += sh['witness_candidates']
        survivors += sh['survivors']
        auth = sh.get('authorization')
    for conv in ('A', 'G'):
        for cat, key in (('all', 'observer_classes'), ('survivors', 'observer_classes_survivors'),
                         ('collapsed', 'observer_classes_collapsed')):
            counts['%s:%s' % (conv, key)] = sum(classes.get('%s:%s' % (conv, cat), {}).values())
    sp = PLAN.Space(prof)
    counts['masking_equivalent_records'] = PLAN.masking_equivalent(sp, True)
    for g in VOID_GATES:
        if gates.get(g, {}).get('failed'):
            void.append('in-run gate %s failed on %d representatives' % (g, gates[g]['failed']))
    for g in MISMATCH_GATES:
        if gates.get(g, {}).get('failed'):
            mism.append('in-run gate %s failed on %d' % (g, gates[g]['failed']))
    if gates.get('C9', {}).get('failed') and s1a_status == 'OK':
        s1a_status = 'MISMATCH'
    if prof['requires_authorization'] and (auth or {}).get('decision') != 'ok':
        void.append('certificate item 6: no authorization echoed by the shards')
    surv_A, surv_G = counts['A:survivors'], counts['G:survivors']
    linked_A = counts['A:survivors_J_linked'] + counts['A:survivors_phi_linked_not_J']
    linked_G = counts['G:survivors_G_linked']
    lab = label(void, mism, inc, base_collapsed, surv_A, surv_G, linked_A, linked_G)
    witness = minimal_witness(witnesses)
    T = rule_T(s1a_status, s1a.get('L_A') if s1a else None, s1a.get('L_G') if s1a else None)
    res = {'schema': 'np-avg-1/stage0/layer2/result/1', 'profile': pname, 'label': lab,
           'label_source': 'merge of structured files',
           'void_reasons': void, 'mismatch_reasons': mism, 'incomplete_reasons': inc,
           'base_precondition': {'collapsed': base_collapsed, 'source': 'preflight.json base_collapsed'},
           'base_relative_survivor_records': base_rel if lab == 'BASE_RESIDUE' else None,
           'counts': counts, 'n_counts': len(counts),
           'masking_equivalent_records_record_sample_reading': PLAN.masking_equivalent(sp, False),
           'structure': {'L3_only_survivor_records': l3only},
           'in_run_gates': gates, 'minimal_witness': witness, 'coverage': cov,
           'S1a': {'status': s1a_status, 'L_A': s1a.get('L_A') if s1a else None, 'L_G': s1a.get('L_G') if s1a else None,
                   'L_reported_L3': s1a.get('L_reported_L3') if s1a else None,
                   'bound_sizes': s1a.get('sizes') if s1a else None, 'n_lines': s1a.get('n_lines') if s1a else None},
           'rule_T': T, 'authorization': auth, 'code_digest': cd, 'config_sha256': CFG.config_sha256(),
           'commit': sorted(c for c in commits if c)[0] if commits - {None} else None,
           'coverage_limits': CFG.CONFIG['coverage_limits'], 'inputs': inputs,
           'residue_file': 'residue.json' if survivors else None,
           'statement_scope': 'Survivor counts are counts of configurations; collapse established by the exact '
                              'closure computation under the frozen rule, with the required controls green; '
                              'see section 5 of the Layer-1 plan for what each label licenses.'}
    if lab == 'COLLAPSE_ALL':
        res['label_text'] = ('Every record is collapsed under A and under G, by the exact closure computation, with '
                             'every required control green; Law_A fails for every record of the class by C_A and '
                             'Law_G fails on v8\'s seventeen frames by C_G (proved corollaries). A consistency-axis '
                             'result.') if pname == 'v8' else 'toy profile: design evidence only, no statement'
    return res, survivors, pf


def main():
    args = sys.argv[1:]
    pname = args[args.index('--profile') + 1]
    workdir = args[args.index('--workdir') + 1]
    res, survivors, pf = merge(pname, workdir)
    O = '.O' if sys.flags.optimize else ''
    if survivors:
        text = CFG.canonical({'schema': 'np-avg-1/stage0/layer2/residue/1', 'survivor_representatives': survivors})
        with open(os.path.join(workdir, 'residue%s.json' % O), 'w') as f:
            f.write(text + '\n')
        res['residue_sha256'] = sha_bytes((text + '\n').encode())
    with open(os.path.join(workdir, 'result%s.json' % O), 'w') as f:
        f.write(json.dumps(res, indent=1, sort_keys=True) + '\n')
    exp = {'schema': 'np-avg-1/stage0/layer2/expected-controls/1', 'profile': pname,
           'expected': CFG.CONFIG['expected'].get(pname), 'expected_controls_full': CFG.CONFIG['expected']['controls_full'],
           'observed_preflight': (pf or {}).get('controls')}
    if not O:
        with open(os.path.join(workdir, 'expected-controls.json'), 'w') as f:
            f.write(json.dumps(exp, indent=1, sort_keys=True) + '\n')
    print(json.dumps({'label': res['label'], 'rule_T': res['rule_T']['outcome'], 'incomplete': res['incomplete_reasons'],
                      'void': res['void_reasons'], 'mismatch': res['mismatch_reasons']}, sort_keys=True))


if __name__ == '__main__':
    main()
