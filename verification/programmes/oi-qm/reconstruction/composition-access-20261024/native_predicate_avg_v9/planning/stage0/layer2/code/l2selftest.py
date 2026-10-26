"""NP-AVG-1 Stage 0 Layer 2: controls of the Layer-2 machinery (toy profile, synthetic
structured files and static checks only; no context of v8's class is constructed, except
the single refused construction of L2-GUARD, which raises before any context exists).

Usage: python3 -I -B l2selftest.py [--mutant NAME] [--only CASE[,CASE...]]
Prints one JSON object {case: {pass, ...}, failed, pass}; exit 0 iff every case passes, 2
otherwise. With --mutant, the named monkeypatch (MUTANTS below) is applied in this process
before the cases run; l2mutants.py counts a mutant as killed only when this exits 2 with
parseable output and its named case failed. With --only, only the named cases run (the quick
campaign runs each machinery mutant against its named case only; the full campaign runs every
case).

Toy-class passes of the shard driver (_toy_pass) run every representative of the toy class
through l2enum.Shard.rep with the representative-sampled gates switched off, so that the C7
path of erratum E1 (item E1-F3) is exercised alone; F1 and F2 are planted production faults
installed on s0geom.Context.run in this process only and removed afterwards.
"""
import ast
import hashlib
import json
import os
import shutil
import sys
import tempfile
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s0geom as G        # noqa: E402
import l2config as CFG    # noqa: E402
import l2analysis as AN   # noqa: E402
import l2plan as PLAN     # noqa: E402
import l2enum as ENUM     # noqa: E402
import l2merge as MERGE   # noqa: E402
import l2auth as AUTH     # noqa: E402
import s0ref as REF       # noqa: E402
import l2manifest as MAN  # noqa: E402
import l2cert as CERT     # noqa: E402
import l2landing as LAND  # noqa: E402
import l2s1a as S1A       # noqa: E402

PRODUCTION = ('l2enum.py', 'l2s1a.py', 'l2merge.py', 'l2preflight.py', 'l2analysis.py', 'l2plan.py', 'l2cert.py', 'l2landing.py',
              'l2calib.py', 'l2refcheck.py')
GUARDED = {'Context': 4, 'record_at': 2, 'num_records': 2, 'record_samples': 3, 'ref_context': 5}


def toy():
    return CFG.make_setup(G, 'toy')


def toy_records(setup):
    return [tuple(sorted(G.record_at(setup, i))) for i in range(G.num_records(setup))]


# ---------------------------------------------------------------------------

def t_static():
    """L2-S1: grants are constructed only in l2auth; production modules pass to the guarded
    entry points only a variable named grant or refgrant (or nothing); l2plan imports no
    engine; the reference side imports no production module."""
    bad = []
    for fn in sorted(os.listdir(HERE)):
        if not fn.endswith('.py'):
            continue
        with open(os.path.join(HERE, fn)) as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                fname = node.func.id if isinstance(node.func, ast.Name) else \
                    (node.func.attr if isinstance(node.func, ast.Attribute) else None)
                if fname in ('V8Grant', 'RefGrant') and fn != 'l2auth.py':
                    bad.append((fn, 'grant constructed', node.lineno))
                if fname == 'bind_running_digests' and fn not in ('l2cert.py', 'l2selftest.py'):
                    bad.append((fn, 'running digests bound', node.lineno))
                if fn in PRODUCTION and fname in GUARDED:
                    pos = GUARDED[fname]
                    vals = [kw.value for kw in node.keywords if kw.arg == 'authorized_v8']
                    if len(node.args) > pos:
                        vals.append(node.args[pos])
                    for v in vals:
                        nm = v.id if isinstance(v, ast.Name) else (v.attr if isinstance(v, ast.Attribute) else
                                                                  (v.slice.value if isinstance(v, ast.Subscript) and
                                                                   isinstance(v.slice, ast.Constant) else None))
                        if nm not in ('grant', 'refgrant'):
                            bad.append((fn, 'authorization argument %s' % ast.dump(v)[:40], node.lineno))
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                names = [a.name for a in node.names] if isinstance(node, ast.Import) else [node.module]
                if fn == 'l2plan.py' and any(n in ('s0geom', 's0ref', 'l2analysis', 'l2enum', 'l2s1a') for n in names):
                    bad.append((fn, 'engine import', node.lineno))
                if fn in ('s0ref.py', 's0native.py', 'l2refcheck.py') and \
                        any(n.startswith('l2') and n != 'l2refcheck' or n == 's0geom' for n in names):
                    bad.append((fn, 'reference imports production', node.lineno))
    return {'pass': not bad, 'findings': bad[:5]}


def _forged_grant():
    """A well-formed V8Grant built without l2auth (the review's forgery), with all-zero fields;
    built through __new__ so that it is not a constructor call (L2-S1)."""
    g = G.V8Grant.__new__(G.V8Grant)
    g.key, g.commit, g.manifest_sha256, g.config_sha256, g.designation = (3, 6, (0, 0, -3)), '0'*40, '0'*64, \
        '0'*64, 'forged'
    r = REF.RefGrant.__new__(REF.RefGrant)
    r.key, r.commit, r.code_digest, r.config_sha256 = (3, 6, (0, 0, -3)), '0'*40, '0'*64, '0'*64
    return g, r


def _refused(f):
    try:
        f()
        return False
    except PermissionError:
        return True


def t_guard():
    """L2-GUARD: a fresh copy of v8's setup is refused with authorized_v8=True; a forged
    well-formed grant (review section 4) is refused while no digests are bound, and still refused
    once the running digests are bound, since its digests differ (L2-R4 d); a second binding to
    other values is refused. Only the guard predicates run: no context exists."""
    fresh = G.Setup(3, 6, 4, 23, (0, 0, -3), ((-8, 0, 0), (-7, 0, -1), (-7, 0, 1)))
    g, r = _forged_grant()
    res = {'true_context': _refused(lambda: G.Context(fresh, (), 'A', authorized_v8=True)),
           'true_num_records': _refused(lambda: G.num_records(fresh, authorized_v8=True)),
           'forged_unbound': _refused(lambda: G._guard(fresh, g)),
           'forged_ref_unbound': not REF._ref_granted(r)}
    cd = MAN.load(HERE)['code_digest']
    G.bind_running_digests(cd, CFG.config_sha256())
    REF.bind_running_digests(cd, CFG.config_sha256())
    res['forged_bound'] = _refused(lambda: G._guard(fresh, g))
    res['forged_ref_bound'] = not REF._ref_granted(r)
    res['rebind_refused'] = _refused(lambda: G.bind_running_digests('1'*64, '1'*64))
    return {'pass': all(res.values()), 'refused': res}


def t_post():
    """L2-POST: post_closure(ctx, ret) equals s0geom.analyse on every toy record, A and G, L3prime
    and L3."""
    setup = toy()
    bad = 0
    for r in toy_records(setup):
        for conv in ('A', 'G'):
            for rule in (G.FROZEN, G.Rule(far=False)):
                a = G.analyse(G.Context(setup, r, conv, rule))
                b = AN.post_closure(G.Context(setup, r, conv, rule), a['retained'])
                bad += any(a[k] != b[k] for k in b)
    return {'pass': bad == 0, 'differences': bad}


def t_orbits():
    """L2-ORB: the coverage scan over the dry run's toy shard plan: orbit weights sum to N, the
    representatives number Burnside's orbit count, and each stabilizer order is |G|/|orbit|."""
    setup = toy()
    grp = AN.group(setup)
    sp = PLAN.Space(CFG.profile('toy'))
    N = sp.n_records()
    gorder, so, po = sp.orbits_burnside()
    plan = PLAN.shard_plan(N, CFG.profile('toy')['shards'])
    scanned, weight, nreps, stab_bad = 0, 0, 0, 0
    for sh in plan:
        n, reps = ENUM.scan(setup, sh['lo'], sh['hi'], grp, None)
        scanned += n
        nreps += len(reps)
        for _, r, orb in reps:
            weight += len(orb)
            stab_bad += AN.stabilizer_order(r, grp) * len(orb) != len(grp)
    ok = scanned == N and weight == N and nreps == so + po and len(grp) == gorder == 8 and stab_bad == 0
    return {'pass': ok, 'scanned': scanned, 'orbit_weight': weight, 'representatives': nreps, 'orbits': so + po}


def _art(commit='a'*40, cd='b'*64, cfg='c'*64):
    return {'schema': AUTH.SCHEMA, 'scope': AUTH.SCOPE, 'commit': commit, 'code_digest': cd, 'config_sha256': cfg,
            'owner': AUTH.OWNER, 'designation_url': AUTH.REPO_URL + 'pull/935#issuecomment-1', 'designated_at': 'x'}


def _own(commit='a'*40):
    return {'schema': AUTH.OWNER_SCHEMA, 'comment_url': AUTH.REPO_URL + 'pull/935#issuecomment-1',
            'author_login': AUTH.OWNER, 'body_sha256': 'd'*64, 'body_contains_required_line': True, 'commit': commit}


def t_auth():
    """L2-AUTH: decide() refuses each single defect and accepts only the all-valid case (the
    decision only; no grant is minted)."""
    facts = {'head_commit': 'a'*40, 'tree_clean': True, 'manifest_ok': True, 'code_digest': 'b'*64,
             'config_sha256': 'c'*64}
    cases = {
        'none': (None, None, facts),
        'fields': (dict(_art(), extra=1), _own(), facts),
        'schema': (dict(_art(), schema='x'), _own(), facts),
        'scope': (dict(_art(), scope='x'), _own(), facts),
        'short_commit': (_art(commit='a'*7), _own(), facts),
        'commit_not_head': (_art(commit='e'*40), _own(commit='e'*40), facts),
        'tree_dirty': (_art(), _own(), dict(facts, tree_clean=False)),
        'manifest_failed': (_art(), _own(), dict(facts, manifest_ok=False)),
        'code_digest': (_art(cd='f'*64), _own(), facts),
        'config': (_art(cfg='f'*64), _own(), facts),
        'owner': (dict(_art(), owner='someone'), _own(), facts),
        'url': (dict(_art(), designation_url='https://example.com/x'), _own(), facts),
        'no_owner_check': (_art(), None, facts),
        'author': (_art(), dict(_own(), author_login='someone'), facts),
        'other_comment': (_art(), dict(_own(), comment_url=AUTH.REPO_URL + 'x'), facts),
        'owner_check_commit': (_art(), _own(commit='e'*40), facts),
        'line_absent': (_art(), dict(_own(), body_contains_required_line=False), facts),
    }
    wrong = sorted(k for k, (a, o, f) in cases.items() if AUTH.decide(a, o, f) == 'ok')
    valid = AUTH.decide(_art(), _own(), facts)
    return {'pass': not wrong and valid == 'ok', 'accepted_defects': wrong, 'valid_case': valid,
            'refusal_cases': len(cases)}


def t_manifest():
    """L2-MAN: a changed byte, an added file and a removed file each fail manifest verification;
    the unmodified copy passes."""
    tmp = tempfile.mkdtemp(prefix='l2man-')
    try:
        for fn in os.listdir(HERE):
            if fn.endswith('.py') or fn == MAN.NAME:
                shutil.copy(os.path.join(HERE, fn), tmp)
        res = {'clean': MAN.verify(tmp)[0]}
        p = os.path.join(tmp, 's0native.py')
        with open(p, 'ab') as f:
            f.write(b'\n')
        res['changed_byte'] = MAN.verify(tmp)[0]
        shutil.copy(os.path.join(HERE, 's0native.py'), p)
        with open(os.path.join(tmp, 'extra.py'), 'w') as f:
            f.write('x = 1\n')
        res['added_file'] = MAN.verify(tmp)[0]
        os.remove(os.path.join(tmp, 'extra.py'))
        os.remove(os.path.join(tmp, 's0s6.py'))
        res['removed_file'] = MAN.verify(tmp)[0]
    finally:
        shutil.rmtree(tmp)
    ok = res['clean'] is True and not res['changed_byte'] and not res['added_file'] and not res['removed_file']
    return {'pass': ok, 'verify': res}


# --- synthetic structured files for the merge, the labels and rule T --------------------------

def _write(d, name, obj, canonical=True):
    text = CFG.canonical(obj) if canonical else json.dumps(obj, sort_keys=True)
    with open(os.path.join(d, name), 'w') as f:
        f.write(text + '\n')
    return text + '\n'


def _s1a_synthetic(mods, cd):
    """A synthetic s1a.json with every field sigma reads, valid unless mods change it."""
    chk = {conv: {r: {'C0_context_equal': True, 'C17_free_tips': 0, 'C18_unjustified': 0} for r in ('L3prime', 'L3')}
           for conv in ('A', 'G')}
    L_A, L_G = mods.get('L_A', 0), mods.get('L_G', 0)
    s1a = {'bound': {}, 'L_A': L_A, 'L_G': L_G, 'L_bound_rule': 'L3prime',
           'L_reported_L3': mods.get('L3', {'L_A': L_A, 'L_G': L_G}),
           'L_reference': {'L3prime': {'L_A': L_A, 'L_G': L_G}, 'L3': mods.get('L3', {'L_A': L_A, 'L_G': L_G})},
           'checks': chk, 'fixed_in_log': [], 'L3prime_within_L3': {'A': True, 'G': True},
           'code_digest': cd, 'config_sha256': CFG.config_sha256(), 'status': 'OK', 'status_reasons': []}
    sig = mods.get('sigma')
    if sig == '1c':
        s1a['code_digest'] = 'f'*64
    elif sig == '2a':
        chk['A']['L3prime']['C0_context_equal'] = False
    elif sig == '2b':
        chk['G']['L3']['C17_free_tips'] = 1
    elif sig == '2c':
        chk['A']['L3']['C18_unjustified'] = 2
    elif sig == '2d':
        s1a['L_reference']['L3prime']['L_A'] = L_A + 1
    elif sig == '3a':
        s1a['fixed_in_log'] = ['G:L3prime']
    elif sig == '3b':
        s1a['L3prime_within_L3']['G'] = False
    return s1a


def _c7cov():
    return {conv: {st: {'records_checked': 0, 'records_failed': 0, 'orbits_touched': 0, 'sum_touched_orbit_sizes': 0,
                        'skipped_beyond_survivor_cap': 0} for st in ENUM.C7_SETS} for conv in ('A', 'G')}


def _case(mods):
    """Build a toy workdir from a valid synthetic run, apply mods, merge in-process."""
    d = tempfile.mkdtemp(prefix='l2merge-')
    try:
        prof = CFG.profile('toy')
        sp = PLAN.Space(prof)
        N = sp.n_records()
        gorder, so, po = sp.orbits_burnside()
        plan = PLAN.shard_plan(N, prof['shards'])
        if 'overlap' in mods:
            plan[1]['lo'] -= 5
        dry = {'schema': 'np-avg-1/stage0/layer2/dryrun/2', 'profile': 'toy', 'records': N, 'orbits': so + po,
               'shards': plan, 'closures_computed': 0, 'config_sha256': CFG.config_sha256(), 'pass': True}
        draw = _write(d, 'dryrun.json', dry)
        cd = MAN.load(HERE)['code_digest']
        s1a = _s1a_synthetic(mods, cd)
        sraw = _write(d, 's1a.json', s1a)
        if mods.get('sigma') == '1a':
            os.remove(os.path.join(d, 's1a.json'))
        if mods.get('sigma') != '1b':
            _write(d, 's1a.O.json', s1a)
        pf = {'code_digest': cd, 'controls': {'X': {'pass': True, 'class': 'VOID'}},
              'base_collapsed': {'A': True, 'G': 'base' not in mods}, 'pass': True, 'profile': 'toy'}
        if 'preflight_mismatch' in mods:
            pf['controls']['C12_universe'] = {'pass': False, 'class': 'MISMATCH'}
        _write(d, 'preflight.json', pf)
        keys = [k for k in AN.reported_count_keys() if k.split(':')[-1] not in AN.CLASS_KEYS
                and k != 'masking_equivalent_records']
        for s, pl in enumerate(plan):
            if mods.get('missing') == s:
                continue
            counts = {k: 0 for k in keys}
            gates = {g: {'checked': 1, 'failed': 0} for g in ('C0_context', 'C7', 'C8', 'C9', 'C10i', 'C11i', 'C11ii',
                                                              'C17', 'C18')}
            for g in mods.get('gate_fail', ()):
                gates[g]['failed'] = 1
            if s == 0:
                counts['A:survivors'] = mods.get('surv_A', 0)
                counts['G:survivors'] = mods.get('surv_G', 0)
                counts['A:survivors_J_linked'] = mods.get('linked_A', 0)
                counts['G:survivors_G_linked'] = mods.get('linked_G', 0)
            sh = {'schema': ENUM_SHARD_SCHEMA, 'profile': 'toy', 'shard': s, 'shards': len(plan),
                  'range': [pl['lo'], pl['hi']], 'records': N, 'scanned': pl['hi'] - pl['lo'],
                  'representatives': (so + po) if s == 0 else 0,
                  'orbit_weight': (N + mods.get('weight_off', 0)) if s == 0 else 0, 'group_order': 8,
                  'code_digest': cd if mods.get('digest') != s else 'f'*64, 'config_sha256': CFG.config_sha256(),
                  'commit': 'a'*40, 'dryrun_sha256': hashlib.sha256(draw.encode()).hexdigest(),
                  's1a_sha256': hashlib.sha256(sraw.encode()).hexdigest(), 'authorization': None,
                  'base_retained': {}, 'counts_additive': counts, 'class_keys': {},
                  'base_relative_survivor_records': {'A': 0, 'G': 0}, 'L3_only_survivor_records': {'A': 0, 'G': 0},
                  'gates': gates, 'gate_failures_first': [], 'witness_min': None, 'witness_candidates_seen': 0,
                  'survivors': [{'index': 0}]*(mods.get('listed', 1) if s == 0 and 'surv_rep' in mods else 0),
                  'survivor_representatives': mods.get('surv_rep', 0) if s == 0 else 0,
                  'survivor_cap': 10, 'survivor_cap_exceeded': bool(mods.get('cap_exceeded')) and s == 0,
                  'tree_clean': False, 'ci_run': None, 'C7_scope_coverage': _c7cov()}
            sh['sha256'] = hashlib.sha256(CFG.canonical(sh).encode()).hexdigest()
            if mods.get('tamper') == s:
                sh['counts_additive']['A:survivors'] += 1
            _write(d, 'shard-%d.json' % s, sh)
            if mods.get('O_differs') == s:
                sh = dict(sh, commit='b'*40)
            _write(d, 'shard-%d.O.json' % s, sh)
        res, _, _ = MERGE.merge('toy', d)
        return res
    finally:
        shutil.rmtree(d)


ENUM_SHARD_SCHEMA = 'np-avg-1/stage0/layer2/shard/3'


def t_merge():
    """L2-MRG: a valid synthetic run, and one with a complete residue, merge with no incomplete
    reason; a missing shard, an overlapping plan, a code-digest mismatch, a tampered shard, a
    normal/-O difference, a wrong orbit weight, a truncated residue and an exceeded survivor cap
    (L2-R3) each give INCOMPLETE."""
    out = {'valid': _case({})}
    exp = {'valid': None}
    out['residue_complete'] = _case({'surv_rep': 2, 'listed': 2})
    exp['residue_complete'] = None
    for name, mods in (('missing', {'missing': 2}), ('overlap', {'overlap': 1}), ('digest', {'digest': 1}),
                       ('tamper', {'tamper': 3}), ('O_differs', {'O_differs': 0}), ('weight', {'weight_off': -1}),
                       ('residue_truncated', {'surv_rep': 3, 'listed': 1}),
                       ('survivor_cap_exceeded', {'surv_rep': 1, 'listed': 1, 'cap_exceeded': 1})):
        out[name] = _case(mods)
        exp[name] = 'INCOMPLETE'
    got = {k: v['label'] for k, v in out.items()}
    ok = not out['valid']['incomplete_reasons'] and not out['residue_complete']['incomplete_reasons'] and \
        all(got[k] == e for k, e in exp.items() if e)
    return {'pass': ok, 'labels': got, 'valid_incomplete_reasons': out['valid']['incomplete_reasons'][:3]}


def t_labels():
    """L2-LBL: section 5's precedence on synthetic runs."""
    table = [({}, 'COLLAPSE_ALL'),
             ({'gate_fail': ['C7']}, 'VOID'),
             ({'gate_fail': ['C11ii']}, 'MISMATCH'),
             ({'gate_fail': ['C7', 'C11ii']}, 'VOID'),
             ({'gate_fail': ['C9'], 'missing': 1}, 'MISMATCH'),
             ({'preflight_mismatch': 1}, 'MISMATCH'),
             ({'missing': 1, 'base': 1}, 'INCOMPLETE'),
             ({'base': 1}, 'BASE_RESIDUE'),
             ({'surv_A': 3}, 'RESIDUE_UNLINKED'),
             ({'surv_A': 3, 'linked_A': 1}, 'RESIDUE'),
             ({'surv_G': 2, 'linked_G': 2}, 'RESIDUE')]
    got = [(_case(m)['label'], e) for m, e in table]
    return {'pass': all(a == b for a, b in got), 'cases': len(table), 'wrong': [g for g in got if g[0] != g[1]]}


def t_rule_t():
    """L2-RT: rule T's partition and its neutrality: the outcome depends on (S1a status, L_A, L_G)
    only. Checked directly and through the merge with labels varied."""
    cases = [('OK', 0, 0, 'L_A = L_G = 0'), ('OK', 1, 0, 'L_A > 0 or L_G > 0'), ('OK', 0, 3, 'L_A > 0 or L_G > 0'),
             ('OK', 2, 2, 'L_A > 0 or L_G > 0'), ('VOID', 0, 0, 'not_evaluated'), ('MISMATCH', 0, 0, 'not_evaluated'),
             ('INCOMPLETE', 5, 0, 'not_evaluated')]
    wrong = [c for c in cases if MERGE.rule_T(c[0], c[1], c[2])['outcome'] != c[3]]
    import inspect
    params = list(inspect.signature(MERGE.rule_T).parameters)
    via = {}
    for m in ({}, {'surv_A': 3, 'linked_A': 1}, {'surv_A': 3}, {'base': 1}):
        r = _case(dict(m, L_A=0, L_G=0))
        via[r['label']] = r['rule_T']['outcome']
    via_c9 = _case({'gate_fail': ['C9']})['rule_T']['outcome']
    neutral = len(set(via.values())) == 1 and set(via.values()) == {'L_A = L_G = 0'}
    return {'pass': not wrong and params == ['s1a_status', 'L_A', 'L_G'] and neutral and via_c9 == 'not_evaluated',
            'wrong': wrong, 'through_merge': via, 'C9_failure_outcome': via_c9}


def t_witness():
    """L2-C16: the minimal witness under the C16 order, against an independent sort."""
    import random
    rng = random.Random(7)
    ok = True
    for _ in range(20):
        cands = [{'key': [rng.randint(1, 2), rng.randint(5, 9), [[[rng.randint(-1, 1), 0, 0], rng.randint(-1, 6)]]]}
                 for _ in range(8)]
        w = MERGE.minimal_witness(cands)

        def tk(c):
            return (c['key'][0], c['key'][1], tuple((tuple(x), t) for x, t in c['key'][2]))
        best = cands[0]
        for c in cands[1:]:
            if tk(c) < tk(best):
                best = c
        ok &= w['key'] == best['key']
    return {'pass': ok}


def t_witness_running():
    """L2-WIT (L2-R1): the shard keeps the running minimum by the C16 key over every candidate,
    whatever their order and number, and counts them."""
    import random
    rng = random.Random(11)
    sh = ENUM.Shard.__new__(ENUM.Shard)
    sh.witness_min, sh.witness_seen = None, 0
    cands = [{'key': [rng.randint(1, 2), rng.randint(5, 40), [[[rng.randint(-3, 3), rng.randint(-3, 3), 0],
                                                               rng.randint(-1, 23)]]], 'i': i} for i in range(300)]
    for c in cands:
        sh.add_witness(c)
    best = min(cands, key=lambda c: (c['key'][0], c['key'][1], tuple((tuple(x), t) for x, t in c['key'][2])))
    return {'pass': sh.witness_min is best and sh.witness_seen == 300, 'seen': sh.witness_seen}


def _planted_block():
    setup = toy()
    pairA = G.Pair(setup.n + 1)
    c0, L = (5, 0, 0), pairA.L
    return setup, tuple(sorted([(c0, L + 1)] + [(G.vadd(c0, e), L) for e in G.axes(3)]))


def t_survivor_gates():
    """L2-SURV (L2-R2): on a planted survivor orbit (the constraint-block record of the toy
    geometry), C0, C7, C11 (i), C17 and C18 run on every member, in both conventions, each with
    the member's own reference context; C8 closes every member directly."""
    setup, blk = _planted_block()
    grp = AN.group(setup)
    orb = AN.orbit(blk, grp)
    bound = {}
    for conv in ('A', 'G'):
        qs = set()
        for m in orb:
            qs |= G.Context(setup, m, conv).quants
        bound[(conv, 'L3prime')] = set(qs)
        bound[(conv, 'L3')] = set(qs)
    base = {conv: set(G.Context(setup, (), conv).run()) for conv in ('A', 'G')}
    sh = ENUM.Shard(setup, CFG.profile('toy'), bound, base, None, None)
    sh.rep(-1, blk, orb)
    n = 2*len(orb)
    g = sh.gates
    # C7 runs per record (E1-F3, set 1) and carries its own C0 check, beside the member gates' C0
    ok = all(g[k]['checked'] == n for k in ('C7', 'C11i', 'C17', 'C18')) and g['C0_context']['checked'] == 2*n and \
        all(v['failed'] == 0 for v in g.values()) and g['C8']['checked'] == 1 and sh.survivor_reps == 1 and \
        len(sh.survivors) == 1
    return {'pass': ok, 'orbit_size': len(orb), 'checked': {k: g[k]['checked'] for k in ('C0_context', 'C7', 'C11i',
                                                                                         'C17', 'C18', 'C8')}}


def t_cert_commits():
    """L2-CERT (L2-R5): the certificate's commit binding. Files with one commit hold; a pre-flight
    at another commit (the r1 toy certificate's case) fails; a shard at another commit fails; an
    authorization naming another commit fails."""
    d = tempfile.mkdtemp(prefix='l2cert-')
    try:
        def write(c_pf, c_s1a, c_sh, c_res):
            for n, c in (('preflight.json', c_pf), ('s1a.json', c_s1a), ('s1a.O.json', c_s1a), ('shard-0.json', c_sh),
                         ('shard-0.O.json', c_sh), ('shard-1.json', c_sh), ('result.json', c_res)):
                with open(os.path.join(d, n), 'w') as f:
                    json.dump({'commit': c}, f)
        a, b = 'a'*40, 'b'*40
        write(a, a, a, a)
        same = CERT.commits_consistent(d)[0]
        same_auth = CERT.commits_consistent(d, a)[0]
        other_auth = CERT.commits_consistent(d, b)[0]
        write(b, a, a, a)
        pf_other = CERT.commits_consistent(d)[0]
        write(a, a, b, a)
        sh_other = CERT.commits_consistent(d)[0]
        write(None, None, None, None)
        nulls = CERT.commits_consistent(d)[0]
    finally:
        shutil.rmtree(d)
    res = {'same': same, 'same_auth': same_auth, 'other_auth': other_auth, 'preflight_other': pf_other,
           'shard_other': sh_other, 'all_null': nulls}
    return {'pass': same and same_auth and not other_auth and not pf_other and not sh_other and not nulls,
            'cases': res}


def t_landing():
    """L2-LAND (L2-R4 c): the post-hoc designation check accepts the echoed designation re-fetched
    unchanged, and refuses another author, a changed body, another comment, a missing required
    line, a missing CI run identity and a result with no owner check."""
    url = AUTH.REPO_URL + 'pull/935#issuecomment-1'
    res = {'commit': 'a'*40, 'authorization': {'decision': 'ok', 'ci_run': {'run_id': '1'},
           'artifact': {'commit': 'a'*40, 'designation_url': url},
           'owner_check': {'comment_url': url, 'author_login': 'amaybaum', 'body_sha256': 'd'*64, 'commit': 'a'*40}}}
    good = {'schema': LAND.FETCH_SCHEMA, 'comment_url': url, 'author_login': 'amaybaum', 'body_sha256': 'd'*64,
            'body_contains_required_line': True}
    bad = {'author': dict(good, author_login='x'), 'body': dict(good, body_sha256='e'*64),
           'comment': dict(good, comment_url=url + '2'), 'line': dict(good, body_contains_required_line=False)}
    ok = LAND.verify(res, good) == []
    wrong = [k for k, f in bad.items() if not LAND.verify(res, f)]
    no_run = dict(res, authorization=dict(res['authorization'], ci_run=None))
    no_own = dict(res, authorization=dict(res['authorization'], owner_check=None))
    return {'pass': ok and not wrong and bool(LAND.verify(no_run, good)) and bool(LAND.verify(no_own, good)),
            'accepted_defects': wrong}


def t_sample():
    """L2-SAMPLE: the sampler is deterministic, rate 1 takes everything, and rate 10 over 0..9,999
    takes exactly the indices an independent hash computation selects."""
    salt = CFG.CONFIG['sampling_salt']
    exp = {i for i in range(10000)
           if int.from_bytes(hashlib.sha256(('%s|%s|%d' % (salt, 'C7', i)).encode()).digest()[:8], 'big') % 10 == 0}
    got = {i for i in range(10000) if ENUM.sampled('C7', i, 10)}
    other = {i for i in range(10000) if ENUM.sampled('C17', i, 10)}
    allk = all(ENUM.sampled('C7', i, 1) for i in range(100))
    return {'pass': got == exp and allk and got != other and 800 < len(got) < 1200, 'selected_of_10000': len(got)}


def t_mask():
    """L2-MASK: the analytic masking-equivalence count equals brute force, in both readings:
    contexts with E1 merges (the plan's) and record samples alone (code-r5's). On the toy class
    (k = 2 and k = 1) the readings coincide; on the toy geometry with last slice 4 (k = 1) they
    differ, since (q9, 4)'s samples above slice 0 are p and V in clear. E1-F6: the per-record
    predicate l2plan.Space.masking_equivalent_record equals brute force on every record of each
    variant (some other record of the space has an equal context)."""
    res = {}
    ok = True
    per_record_bad = 0
    for tag, tlast, k in (('toy_k2', 6, 2), ('toy_k1', 6, 1), ('toy_t4_k1', 4, 1)):
        base = CFG.profile('toy')
        prof = dict(base, k=k, setup=dict(base['setup'], tlast=tlast))
        sp = PLAN.Space(prof)
        st = prof['setup']
        setup = G.Setup(st['dim'], st['n'], st['rho'], tlast, tuple(st['port']), tuple(tuple(x) for x in st['sources']))
        recs = toy_records(setup) if k == 2 else [r for r in toy_records(setup) if len(r) == 1]
        for reading, merge_fixed in (('context', True), ('record_samples', False)):
            keys = Counter()
            kof = {}
            for r in recs:
                if merge_fixed:
                    ctx = G.Context(setup, r, 'A')
                    kof[r] = tuple(sorted(ctx.quants | ctx.fixed))
                else:
                    kof[r] = tuple(sorted(G.record_samples(setup, r)))
                keys[kof[r]] += 1
            brute = sum(v for v in keys.values() if v > 1)
            ana = PLAN.masking_equivalent(sp, merge_fixed)
            res['%s_%s' % (tag, reading)] = [ana, brute]
            ok &= ana == brute
            if merge_fixed:
                per_record_bad += sum(1 for r in recs if sp.masking_equivalent_record(r) != (keys[kof[r]] > 1))
    differ = res['toy_t4_k1_context'][1] != res['toy_t4_k1_record_samples'][1]
    return {'pass': ok and differ and per_record_bad == 0, 'analytic_vs_brute': res, 'readings_differ_on_t4': differ,
            'per_record_disagreements': per_record_bad}


def t_plan():
    """L2-PLAN: the dry run's N, orbit count and context-size histogram equal the engine's on the
    toy class."""
    setup = toy()
    sp = PLAN.Space(CFG.profile('toy'))
    recs = toy_records(setup)
    grp = AN.group(setup)
    orbits = len({AN.canon(r, grp) for r in recs})
    singles, pairs = PLAN.context_histogram(sp)
    hs, hp = Counter(), Counter()
    for r in recs:
        n = len(G.Context(setup, r, 'A').quants)
        (hs if len(r) == 1 else hp)[n] += 1
    ok = sp.n_records() == G.num_records(setup) == len(recs) and orbits == sum(sp.orbits_burnside()[1:]) and \
        hs == singles and hp == pairs
    return {'pass': ok, 'records': len(recs), 'orbits': orbits}


def t_shared_tips():
    """L2-SHTIP: the dry run's shared-tip record count equals l2analysis.shared_near_tip over the
    engine's toy contexts, per convention."""
    setup = toy()
    sp = PLAN.Space(CFG.profile('toy'))
    got = PLAN.shared_tip_records(sp)
    eng = {}
    for conv in ('A', 'G'):
        n = 0
        for r in toy_records(setup):
            ctx = G.Context(setup, r, conv)
            n += AN.shared_near_tip(ctx.quants, ctx.pair, setup.dim)
        eng[conv] = n
    return {'pass': got == eng, 'plan': got, 'engine': eng}


def t_gates():
    """L2-GATES: the in-run gate predicates fail on planted violations: C9 (a retained quantity
    outside the bound; L3prime not within L3) and C10 (i) (a fixed quantity in the log)."""
    q, r = (((0, 0, 0), 1)), (((1, 0, 0), 2))
    bound = {('A', 'L3prime'): {q}, ('A', 'L3'): {q, r}}
    c9 = [ENUM.c9_ok([q], [q, r], bound, 'A'), not ENUM.c9_ok([q, r], [q, r], bound, 'A'),
          not ENUM.c9_ok([r], [q], bound, 'A')]

    class Fake:
        fixed = {q}
        log = [(q, q, {})]
    c10 = [not ENUM.c10i_ok(Fake())]
    return {'pass': all(c9) and all(c10), 'C9': c9, 'C10i': c10}


def t_rule_config():
    """L2-CFG: the frozen Rule's fields equal the configuration's."""
    import l2cert as CERT
    return {'pass': CERT.rule_fields_ok()}


# --- r3: erratum E1 (C7 per record, sigma, rule T, 58 counts) ------------------------------------

_TOYPASS = {}


def _quiet_prof():
    """The toy profile with the representative-sampled gates off (rate far above the toy class), so
    that a toy pass exercises the per-record C7 path alone."""
    off = 10**12
    return dict(CFG.profile('toy'), sampling={'C8_orbits': off, 'C11i': off, 'C17': off, 'C18': off})


def _toy_pass(tag):
    """Every toy representative through l2enum.Shard.rep (bound from l2s1a on the toy class)."""
    if tag in _TOYPASS:
        return _TOYPASS[tag]
    setup = toy()
    s1a = S1A.run('toy', None, None)
    bound = ENUM.load_bound(s1a, setup, None)
    base = {c: set(G.Context(setup, (), c).run()) for c in ('A', 'G')}
    sh = ENUM.Shard(setup, _quiet_prof(), bound, base, None, None)
    _, reps = ENUM.scan(setup, 0, G.num_records(setup), sh.grp, None)
    for i, r, o in reps:
        sh.rep(i, r, o)
    if tag == 'clean':
        _TOYPASS[tag] = sh
    return sh


def _install_fault(only_nonrep):
    """F1 (E1-check part I): the production closure under G drops every retained in-frame quantity
    whose near tip is shared with another retained quantity. F2: the same on non-representative
    records only. Installed on s0geom.Context.run; returns the original to restore."""
    orig = G.Context.run
    grp = AN.group(toy())

    def run(self):
        ret = orig(self)
        if self.conv != 'G' or self.rule is not G.FROZEN:
            return ret
        rec = tuple(sorted(self.record))
        if only_nonrep and AN.canon(rec, grp) == rec:
            return ret
        dim = self.setup.dim
        inn = {q for q in ret if not any(self.eligible(u) for u in G.tips(q, self.pair, dim))}
        tips = {}
        for q in ret:
            for lab, u in G.tip_labels(q, self.pair, dim):
                if lab[1] == 'near':
                    tips.setdefault((lab[0], u), set()).add(q)
        drop = set()
        for qs in tips.values():
            if len(qs) > 1:
                drop |= qs & inn
        self.retained = set(ret) - drop
        return self.retained
    G.Context.run = run
    return orig


def _fault_case(only_nonrep):
    setup = toy()
    recs = toy_records(setup)
    grp = AN.group(setup)
    true = {r: frozenset(G.Context(setup, r, 'G').run()) for r in recs}
    orig = _install_fault(only_nonrep)
    try:
        faulty = {r: frozenset(G.Context(setup, r, 'G').run()) for r in recs}
        sh = _toy_pass('fault')
    finally:
        G.Context.run = orig
    affected = [r for r in recs if faulty[r] != true[r]]
    nonrep = sum(1 for r in affected if AN.canon(r, grp) != r)
    return sh, len(affected), nonrep


def t_f1():
    """L2-F1 (E1-F3): a planted equivariant fault that removes retained in-frame tied quantities (F1)
    is caught by C7 on every affected record of set 2, because set 2 under G is F_G, computed from
    Q0(R) without any closure. (A set 2 defined by the computed closure loses these records: the
    fault destroys the tie; mutant M_C7_set2_computed.)"""
    sh, n_aff, _ = _fault_case(False)
    s2 = sh.c7['G']['2_set2']
    return {'pass': n_aff > 0 and s2['records_failed'] == n_aff and s2['records_checked'] >= n_aff,
            'affected_records': n_aff, 'set2_G': s2}


def t_f2():
    """L2-F2 (E1-F3): a fault on non-representative members only (F2) changes no carried result; it is
    caught by C7's direct per-record check on every affected record of set 2, in both of its
    comparisons (direct against reference, carried against direct)."""
    sh, n_aff, nonrep = _fault_case(True)
    s2 = sh.c7['G']['2_set2']
    g = sh.gates['C7']
    return {'pass': n_aff > 0 and nonrep == n_aff and s2['records_failed'] == n_aff and
            g['direct_vs_reference_failed'] >= n_aff and g['carried_vs_direct_failed'] >= n_aff,
            'affected_records': n_aff, 'affected_non_representative': nonrep, 'set2_G': s2,
            'C7_failures': {k: g[k] for k in ('direct_vs_reference_failed', 'carried_vs_direct_failed')}}


def _ref_sets():
    """An independent computation of C7's sets on the toy class: s0ref contexts, full reference
    closures, s0ref tips; record indices from s0geom.record_at's order; samples by an independent
    hash; orbits by l2plan's own group action."""
    if 'ref' in _TOYPASS:
        return _TOYPASS['ref']
    setup = toy()
    prof = CFG.profile('toy')
    sp = PLAN.Space(prof)
    grp = sp.group()
    salt = CFG.CONFIG['sampling_salt']

    def hs(stream, rate, i):
        return int.from_bytes(hashlib.sha256(('%s|%s|%d' % (salt, stream, i)).encode()).digest()[:8], 'big') % rate == 0

    def canon(r):
        return min(tuple(sorted((g(x), t) for x, t in r)) for g in grp)
    port = tuple(setup.port)
    out = {'A': {}, 'G': {}}
    per = {}
    recs = toy_records(setup)
    for i, r in enumerate(recs):
        per[r] = {'index': i, 'canon': canon(r)}
        for conv in ('A', 'G'):
            fixed, quants, geo, elig = REF.ref_context(setup.dim, setup.n, port, r, conv)
            ret, _ = REF.greatest(fixed, quants, geo, elig, CFG.CONFIG['C7_brute_limit'])

            def near(q):
                _, d, nr, _ = geo.kind(q)
                return {(REF.unit(geo.dim, a, sg), (REF.shift(q[0], REF.unit(geo.dim, a, sg), d), nr))
                        for a in range(geo.dim) for sg in (1, -1)}

            def shared(qs, el=None):
                seen = {}
                for q in sorted(qs):
                    for k in near(q):
                        if el is not None and not el(k[1]):
                            continue
                        if k in seen and seen[k] != q:
                            return True
                        seen[k] = q
                return False
            seed = {q for q in quants if any(elig(u) for u in geo.tipset(q))}
            surv = bool(ret) if conv == 'A' else bool(ret & seed)
            inn = set(quants) - seed
            f = {'I': shared(quants), 'F_G': shared(inn) if conv == 'G' else False,
                 'E_G': shared(seed, elig) if conv == 'G' else False}
            s2 = shared(ret) if conv == 'A' else (f['F_G'] or (surv and shared(ret)))
            per[r][conv] = dict(f, surv=surv)
            out[conv][r] = {'1_Surv': surv, '2_set2': s2, '3_I_and_H100': f['I'] and hs('C7_H100', 100, i),
                            '4_H1000': hs('C7_H1000', 1000, i)}
    _TOYPASS['ref'] = (out, per)
    return out, per


def t_c7_coverage():
    """L2-C7COV (E1-F3): on the toy class, the shard driver's per-set C7 coverage (records checked,
    orbits touched, sum of their sizes) equals an independent computation (_ref_sets); the samples
    are drawn over every record index and include non-representative records; no C7 failure."""
    sh = _toy_pass('clean')
    sets, per = _ref_sets()
    exp, nonrep = {}, {}
    for conv in ('A', 'G'):
        exp[conv] = {}
        for st in ENUM.C7_SETS:
            X = [r for r, v in sets[conv].items() if v[st]]
            orbs = {per[r]['canon'] for r in X}
            size = {o: sum(1 for r in per if per[r]['canon'] == o) for o in orbs}
            exp[conv][st] = {'records_checked': len(X), 'orbits_touched': len(orbs),
                             'sum_touched_orbit_sizes': sum(size.values())}
            nonrep['%s:%s' % (conv, st)] = sum(1 for r in X if per[r]['canon'] != r)
    got = {conv: {st: {k: sh.c7[conv][st][k] for k in ('records_checked', 'orbits_touched',
                                                       'sum_touched_orbit_sizes')} for st in ENUM.C7_SETS}
           for conv in ('A', 'G')}
    fails = sum(sh.c7[c][st]['records_failed'] for c in ('A', 'G') for st in ENUM.C7_SETS)
    samples_nonrep = nonrep['A:3_I_and_H100'] + nonrep['G:3_I_and_H100'] + nonrep['A:4_H1000'] + nonrep['G:4_H1000']
    return {'pass': got == exp and fails == 0 and sh.gates['C7']['failed'] == 0 and samples_nonrep > 0,
            'coverage': got, 'independent': exp if got != exp else 'equal',
            'sampled_non_representative_records': nonrep}


def t_scope():
    """L2-SCOPE (E1-F3): l2plan's closure-free predicates (I_A, I_G, F_G, E_G) equal the same
    predicates computed with s0ref's contexts, tips and frame, and I_c equals the production
    context's shared near tip, on every toy record; the populations are the erratum's (E1-check
    parts H and J: I_A 1,071, I_G 667, F_G 595 in 283 orbits, E_G 12)."""
    setup = toy()
    sp = PLAN.Space(CFG.profile('toy'))
    _, per = _ref_sets()
    bad = []
    for r in toy_records(setup):
        f = sp.c7_flags(r)
        ref = {'I_A': per[r]['A']['I'], 'I_G': per[r]['G']['I'], 'F_G': per[r]['G']['F_G'], 'E_G': per[r]['G']['E_G']}
        prod = {}
        for conv in ('A', 'G'):
            ctx = G.Context(setup, r, conv)
            prod['I_' + conv] = AN.shared_near_tip(ctx.quants, ctx.pair, setup.dim)
        if f != ref or any(f[k] != v for k, v in prod.items()) or sp.q0(r) != G.Context(setup, r, 'A').quants:
            bad.append([[list(x), t] for x, t in r])
    pops = PLAN.c7_populations(sp)
    exp = {'I_A': 1071, 'I_G': 667, 'F_G': 595, 'E_G': 12}
    ok = not bad and all(pops[k]['records'] == v for k, v in exp.items()) and pops['F_G']['orbits'] == 283
    return {'pass': ok, 'disagreeing_records': bad[:3], 'populations': pops}


def t_index():
    """L2-INDEX: l2plan.Space.index_of inverts s0geom.record_at on every toy index (k = 2 and k = 1),
    so that C7's samples are drawn over each record's own index."""
    ok = True
    for k in (2, 1):
        prof = dict(CFG.profile('toy'), k=k)
        sp = PLAN.Space(prof)
        setup = toy()
        n = G.num_records(setup, k)
        ok &= all(sp.index_of(G.record_at(setup, i)) == i and sp.in_space(G.record_at(setup, i)) for i in range(n))
    _, blk = _planted_block()
    return {'pass': ok and not PLAN.Space(CFG.profile('toy')).in_space(blk)}


def t_sigma():
    """L2-SIGMA (E1-T2): each of sigma's conditions 1 (a)-(c), 2 (a)-(d), 3 (a)-(c) on a synthetic run
    gives sigma = its case, enters the run label as a reason of that class, and leaves rule T
    'not_evaluated'; the valid run gives sigma = OK and rule T evaluated."""
    exp = {'1a': 'INCOMPLETE', '1b': 'INCOMPLETE', '1c': 'INCOMPLETE', '2a': 'VOID', '2b': 'VOID', '2c': 'VOID',
           '2d': 'VOID', '3a': 'MISMATCH', '3b': 'MISMATCH'}
    got = {}
    for k in exp:
        r = _case({'sigma': k})
        got[k] = [r['S1a']['status'], r['rule_T']['outcome'], r['label']]
    r = _case({'gate_fail': ['C9']})
    got['3c'] = [r['S1a']['status'], r['rule_T']['outcome'], r['label']]
    exp['3c'] = 'MISMATCH'
    ok_case = _case({})
    wrong = {k: v for k, v in got.items() if v[0] != exp[k] or v[1] != 'not_evaluated' or v[2] != exp[k]}
    ok = not wrong and ok_case['S1a']['status'] == 'OK' and ok_case['rule_T']['evaluated'] is True
    return {'pass': ok, 'cases': len(got), 'wrong': wrong}


def t_precedence():
    """L2-PREC (E1-T2): sigma never overrides the run label. With sigma = OK, a failing VOID gate,
    MISMATCH pre-flight control or missing shard gives that label; rule T is still evaluated and
    its outcome is recorded beside the label, with no S1b proposal. A clean run with L_A > 0 puts
    S1b to the owner."""
    rows = {'void_gate': ({'gate_fail': ['C7'], 'L_A': 2}, 'VOID'),
            'mismatch_preflight': ({'preflight_mismatch': 1, 'L_A': 2}, 'MISMATCH'),
            'incomplete_shard': ({'missing': 2, 'L_A': 2}, 'INCOMPLETE')}
    bad = {}
    for name, (mods, lab) in rows.items():
        r = _case(mods)
        T = r['rule_T']
        if not (r['S1a']['status'] == 'OK' and r['label'] == lab and T['evaluated'] and T.get('beside_label') == lab
                and T['S1b_S1c'].startswith('no proposal')):
            bad[name] = [r['S1a']['status'], r['label'], T.get('beside_label'), T['S1b_S1c']]
    clean = _case({'L_A': 2})
    ok = not bad and clean['label'] == 'COLLAPSE_ALL' and clean['rule_T']['S1b_S1c'].startswith('S1b put') and \
        'beside_label' not in clean['rule_T']
    return {'pass': ok, 'wrong': bad, 'clean_run_rule_T': clean['rule_T']['S1b_S1c']}


def t_rule_t_l3():
    """L2-T1 (E1-T1): rule T reads L_A and L_G from the L3prime bound. A run whose L3prime values are
    0 and whose L3 values are positive gives the L3prime outcome; the L3 values are recorded in a
    separate field."""
    r = _case({'L_A': 0, 'L_G': 0, 'L3': {'L_A': 4, 'L_G': 1}})
    T = r['rule_T']
    return {'pass': T['outcome'] == 'L_A = L_G = 0' and T['L_reported_L3'] == {'L_A': 4, 'L_G': 1} and
            T['bound_rule'] == 'L3prime', 'outcome': T['outcome']}


def t_t5():
    """L2-T5 (E1-T5): on a planted bound (the toy class's L3prime global bound) L_G, counted by the
    quantity's own cone, is nonzero and equals its s0ref recomputation; the tip-cone reading would
    give 0 (mutant M_LG_tip_reading)."""
    o = S1A.run('toy', None, None)
    return {'pass': o['L_G'] > 0 and o['L_G'] == o['L_reference']['L3prime']['L_G'] and o['status'] == 'OK',
            'L_G': o['L_G'], 'L_G_reference': o['L_reference']['L3prime']['L_G']}


def t_2d():
    """L2-2D (E1-T2 case 2 (d)): on the toy bound, l2s1a's s0ref recomputation of L_A and L_G equals
    the production values; a perturbed production count makes l2s1a's status VOID, and a synthetic
    s1a.json whose recorded reference differs from its production values makes sigma VOID in the
    merge, which then does not evaluate rule T."""
    o = S1A.run('toy', None, None)
    agree = [o['L_A'], o['L_G']] == [o['L_reference']['L3prime']['L_A'], o['L_reference']['L3prime']['L_G']]
    orig = S1A.linked_counts

    def plus_one(ctx, ret, setup):
        n, sel = orig(ctx, ret, setup)
        return n + 1, sel
    S1A.linked_counts = plus_one
    try:
        p = S1A.run('toy', None, None)
    finally:
        S1A.linked_counts = orig
    m = _case({'sigma': '2d'})
    ok = agree and o['status'] == 'OK' and p['status'] == 'VOID' and 'reference_L:L3prime' in p['status_reasons'] \
        and m['S1a']['status'] == 'VOID' and m['label'] == 'VOID' and m['rule_T']['outcome'] == 'not_evaluated'
    return {'pass': ok, 'toy': [o['L_A'], o['L_G']], 'perturbed_status': p['status'], 'merge_sigma': m['S1a']['status']}


def t_counts58():
    """L2-COUNTS (E1-F6): the reported list has 58 keys, the r5 54 and the four survivor cells; with
    the plain counts n(6) and n(9) every section 3 degeneracy has rank 3 per convention; a planted
    survivor orbit with a nontrivial stabilizer contributes to N_ST under A and G through the shard;
    the merge reports 58 counts."""
    keys = AN.reported_count_keys()
    added = [k for k in keys if k not in AN.count_keys()]
    degs = list(AN.DEGENERACIES) + ['masking_equivalent', 'nontrivial_stabilizer']
    marg = {'masking_equivalent': 'masking_equivalent_records', 'nontrivial_stabilizer': 'nontrivial_stabilizer'}
    ks = set(keys)
    open_cells = []
    for d in degs:
        for c in ('A', 'G'):
            t, f = '%s:deg:%s:survivor=True' % (c, d) in ks, '%s:deg:%s:survivor=False' % (c, d) in ks
            if not ((t and f) or (marg.get(d) in ks and (t or f))):
                open_cells.append([d, c])
    setup, blk = _planted_block()
    grp = AN.group(setup)
    orb = AN.orbit(blk, grp)
    bound = {}
    for conv in ('A', 'G'):
        qs = set()
        for m in orb:
            qs |= G.Context(setup, m, conv).quants
        bound[(conv, 'L3prime')] = bound[(conv, 'L3')] = qs
    base = {conv: set(G.Context(setup, (), conv).run()) for conv in ('A', 'G')}
    sh = ENUM.Shard(setup, CFG.profile('toy'), bound, base, None, None)
    sh.rep(-1, blk, orb)
    nst = [sh.counts['%s:deg:nontrivial_stabilizer:survivor=True' % c] for c in ('A', 'G')]
    merged = _case({})
    ok = len(keys) == 58 == len(set(keys)) and len(AN.count_keys()) == 54 and sorted(added) == sorted(AN.ADDED_E1_F6) \
        and not open_cells and all(v == len(orb) for v in nst) and merged['n_counts'] == 58
    return {'pass': ok, 'n_keys': len(keys), 'open_cells': open_cells, 'N_ST_planted': nst, 'orbit_size': len(orb)}


def t_v8_counts():
    """L2-V8COUNTS: the record-enumerating counts (--shared-tips, F_G and the other C7 populations)
    are refused on v8's configuration class before any record is enumerated: by the dry run's
    command line and by each function. A sentinel replaces the record generator while this runs,
    so that a missing refusal is detected without enumerating anything."""
    v8 = PLAN.Space(CFG.profile('v8'))
    orig = PLAN._records

    def sentinel(sp):
        raise RuntimeError('record enumeration reached')
    PLAN._records = sentinel
    res = {}
    try:
        for name, fn in (('shared_tip_records', PLAN.shared_tip_records), ('c7_populations', PLAN.c7_populations)):
            try:
                fn(v8)
                res[name] = 'returned'
            except PermissionError:
                res[name] = 'refused'
            except RuntimeError:
                res[name] = 'reached'
        import io
        import contextlib
        argv = sys.argv
        sys.argv = ['l2plan.py', '--profile', 'v8', '--shared-tips']
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                PLAN.main()
            res['cli'] = 'returned'
        except SystemExit as e:
            out = json.loads(buf.getvalue() or '{}')
            res['cli'] = 'refused' if e.code == 2 and out.get('refused') else 'exit %s' % e.code
        except PermissionError:
            res['cli'] = 'refused by function'
        except RuntimeError:
            res['cli'] = 'reached'
        finally:
            sys.argv = argv
    finally:
        PLAN._records = orig
    return {'pass': res == {'shared_tip_records': 'refused', 'c7_populations': 'refused', 'cli': 'refused'},
            'attempts': res}


def t_statement_scope():
    """L2-T6 (E1-T6): rule T's statement scope is the erratum's text, verbatim, and is recorded in
    result.json's rule_T.statement_scope; the zero branch's text is the same."""
    path = os.path.join(HERE, '..', '..', 'amendments', 'E1-LAYER1-ERRATUM.md')
    with open(path, encoding='utf-8') as f:
        er = ' '.join(f.read().split())
    text = CFG.CONFIG['rule_T']['zero_text']
    r = _case({})
    return {'pass': ' '.join(text.split()) in er and r['rule_T']['statement_scope'] == text and
            MERGE.rule_T('OK', 0, 0)['text'] == text}


def t_placeholders():
    """L2-PLACEHOLDER: the open owner decisions are exactly kappa, G_D and O1, with no value for kappa
    anywhere in the configuration; the C7 reference form is the full s0ref closure (the G-D form is
    not implemented); and l2cert.startup refuses the v8 profile at certificate item 1 while any is
    open, even when the authorization step passes (simulated here by a decision that constructs no
    grant; no context exists)."""
    paths = CFG.placeholders()
    want = ['/budget/kappa', '/owner_rulings/G_D/ruling', '/owner_rulings/O1/ruling', '/owner_rulings/kappa/ruling']
    kap = [CFG.CONFIG['budget']['kappa'], CFG.CONFIG['owner_rulings']['kappa']['ruling']]
    orig = AUTH.issue_grant
    AUTH.issue_grant = lambda art, own, here: ('ok', None, None, {'decision': 'ok', 'artifact': None,
                                                                 'owner_check': None})
    d = tempfile.mkdtemp(prefix='l2ph-')
    import io
    import contextlib
    buf = io.StringIO()
    item = None
    try:
        with contextlib.redirect_stdout(buf):
            CERT.startup('v8', d, [])
    except SystemExit:
        item = json.loads(buf.getvalue() or '{}').get('certificate_item')
    finally:
        AUTH.issue_grant = orig
        shutil.rmtree(d)
    ok = paths == want and all(k == CFG.OWNER for k in kap) and CFG.CONFIG['C7']['reference_form'] == 'full_s0ref' \
        and item == 1
    return {'pass': ok, 'placeholders': paths, 'v8_startup_refused_at_item': item}


CASES = [('L2-S1_static', t_static), ('L2-GUARD', t_guard), ('L2-POST', t_post), ('L2-ORB', t_orbits),
         ('L2-AUTH', t_auth), ('L2-MAN', t_manifest), ('L2-MRG', t_merge), ('L2-LBL', t_labels), ('L2-RT', t_rule_t),
         ('L2-C16', t_witness), ('L2-WIT', t_witness_running), ('L2-SURV', t_survivor_gates),
         ('L2-CERT', t_cert_commits), ('L2-LAND', t_landing), ('L2-SAMPLE', t_sample), ('L2-MASK', t_mask), ('L2-PLAN', t_plan),
         ('L2-SHTIP', t_shared_tips), ('L2-GATES', t_gates), ('L2-CFG', t_rule_config),
         ('L2-INDEX', t_index), ('L2-SCOPE', t_scope), ('L2-C7COV', t_c7_coverage), ('L2-F1', t_f1), ('L2-F2', t_f2),
         ('L2-SIGMA', t_sigma), ('L2-PREC', t_precedence), ('L2-T1', t_rule_t_l3), ('L2-T5', t_t5), ('L2-2D', t_2d),
         ('L2-COUNTS', t_counts58), ('L2-V8COUNTS', t_v8_counts), ('L2-T6', t_statement_scope),
         ('L2-PLACEHOLDER', t_placeholders)]


# --- machinery mutants (monkeypatches in this process only) --------------------------------

def _m_skip_index():
    orig = ENUM.iter_indices
    ENUM.iter_indices = lambda lo, hi: [i for i in orig(lo, hi) if i != lo + 3]


def _m_every_rep():
    AN.canon = lambda r, grp: tuple(sorted(r))


def _m_no_coverage():
    MERGE.coverage_ok = lambda ranges, N, S: True
    MERGE.recount_ok = lambda *a: True


def _m_label_order():
    orig = MERGE.label

    def lab(void, mismatch, *rest):
        if mismatch:
            return 'MISMATCH'
        return orig(void, mismatch, *rest)
    MERGE.label = lab


def _m_rule_t_or():
    orig = MERGE.rule_T

    def rt(st, a, b):
        r = orig(st, a, b)
        if st == 'OK' and (a == 0 or b == 0):
            r = orig(st, 0, 0)
        return r
    MERGE.rule_T = rt


def _m_auth_commit():
    orig = AUTH.decide
    AUTH.decide = lambda a, o, f: orig(a, o, dict(f, head_commit=a.get('commit')) if isinstance(a, dict) else f)


def _m_manifest_blind():
    orig = MAN.verify

    def v(d=HERE):
        ok, diffs, rec = orig(d)
        return True, [], rec
    MAN.verify = v


def _m_post_no_in_clear():
    orig = AN.post_closure

    def pc(ctx, ret):
        out = orig(ctx, ret)
        out['public_retained'] = [q for q in out['public_retained'] if q not in ctx.in_clear]
        return out
    AN.post_closure = pc


def _m_sampler_never():
    ENUM.sampled = lambda name, idx, rate: False


def _m_mask_no_merge():
    orig = PLAN.masking_equivalent
    PLAN.masking_equivalent = lambda sp, merge_fixed=True: orig(sp, False)


def _m_c9_off():
    ENUM.c9_ok = lambda *a: True


def _m_witness_max():
    MERGE.minimal_witness = lambda c: max(c, key=lambda w: (w['key'][0], w['key'][1], w['key'][2])) if c else None


def _m_guard_truthy():
    G._granted = lambda a: bool(a)


def _m_witness_first():
    def add(self, cand):
        self.witness_seen += 1
        if self.witness_min is None:
            self.witness_min = cand
    ENUM.Shard.add_witness = add


def _m_survivor_rep_only():
    ENUM.Shard.member_ref_gates = lambda self, idx, m, d: None


def _m_residue_ignored():
    MERGE.residue_complete = lambda sh: True


def _m_commits_unbound():
    CERT.commits_consistent = lambda workdir, auth_commit=None: (True, {})


def _m_grant_unbound():
    G._granted = lambda a: (type(a) is G.V8Grant and getattr(a, 'key', None) == (3, 6, (0, 0, -3))
                            and G._hex(getattr(a, 'commit', None), 40))


def _m_c7_set2_computed():
    def set2(conv, flags, carried, pair_E):
        return PLAN.shared_near(carried['retained'], pair_E)
    ENUM.c7_set2 = set2


def _m_c7_carried_only():
    def c7_record(self, idx, m, conv, carried, dcache):
        fixed, quants, geo, elig = ENUM.ref_ctx(self.setup, m, conv, self.refgrant)
        self.gates['C7']['checked'] += 1
        same, _ = ENUM.RC.c7(fixed, quants, carried['retained'], geo, elig, CFG.CONFIG['C7_brute_limit'])
        if not same:
            self.gates['C7']['direct_vs_reference_failed'] += 1
            self.fail('C7', idx, conv)
        return same
    ENUM.Shard.c7_record = c7_record


def _m_c7_sample_rep_index():
    orig = ENUM.Shard.c7_orbit

    def c7_orbit(self, idx, orb, member_views, gated, dcache):
        keep = self.sp.index_of
        self.sp.index_of = lambda m: idx
        try:
            return orig(self, idx, orb, member_views, gated, dcache)
        finally:
            self.sp.index_of = keep
    ENUM.Shard.c7_orbit = c7_orbit


def _m_ruleT_ignores_sigma():
    orig = MERGE.rule_T
    MERGE.rule_T = lambda st, a, b: orig('OK', a, b)


def _m_sigma_overrides_label():
    orig = MERGE.label

    def lab(void, mismatch, incomplete, *rest):
        only = [w for w in void + mismatch + incomplete if w.startswith('S1a ')]
        return orig([w for w in void if w in only], [w for w in mismatch if w in only],
                    [w for w in incomplete if w in only], *rest)
    MERGE.label = lab


def _m_proposal_on_failed_label():
    MERGE.rule_T_record = lambda T, label_, L3: dict(T, run_label=label_, L_reported_L3=L3)


def _m_sigma_no_2d():
    orig = MERGE.sigma

    def sig(s1a, *a):
        if s1a is not None and 'L_reference' in s1a:
            s1a = dict(s1a, L_reference=dict(s1a['L_reference'], L3prime={'L_A': s1a.get('L_A'),
                                                                           'L_G': s1a.get('L_G')}))
        return orig(s1a, *a)
    MERGE.sigma = sig


def _m_ruleT_reads_L3():
    MERGE.rule_T_inputs = lambda s1a: ((s1a.get('L_reported_L3') or {}).get('L_A'),
                                       (s1a.get('L_reported_L3') or {}).get('L_G')) if s1a else (None, None)


def _m_LG_tip_reading():
    orig = S1A.linked_counts

    def lc(ctx, ret, setup):
        if ctx.conv == 'A':
            return orig(ctx, ret, setup)
        src = [(x, 0) for x in setup.sources]
        sel = [q for q in sorted(ret) if any(ctx.eligible(u) and any(G.in_cone(c, u, ctx.pair) for c in src)
                                             for u in G.tips(q, ctx.pair, setup.dim))]
        return len(sel), sel
    S1A.linked_counts = lc


def _m_counts_54():
    AN.reported_count_keys = AN.count_keys


def _m_v8_counts_unrefused():
    PLAN.refuse_v8_enumeration = lambda sp: None


def _m_placeholders_ignored():
    CFG.placeholders = lambda *a, **k: []


MUTANTS = {
    'M_skip_index': (_m_skip_index, 'L2-ORB', 'coverage scan misses one index'),
    'M_every_record_rep': (_m_every_rep, 'L2-ORB', 'orbit reduction off: representatives exceed orbits'),
    'M_merge_no_coverage': (_m_no_coverage, 'L2-MRG', 'overlapping or short coverage accepted'),
    'M_label_mismatch_first': (_m_label_order, 'L2-LBL', 'MISMATCH ranked above VOID'),
    'M_ruleT_or': (_m_rule_t_or, 'L2-RT', 'rule T zero branch on L_A = 0 or L_G = 0'),
    'M_auth_no_commit': (_m_auth_commit, 'L2-AUTH', 'authorization for another commit accepted'),
    'M_manifest_blind': (_m_manifest_blind, 'L2-MAN', 'changed code passes the manifest'),
    'M_post_no_in_clear': (_m_post_no_in_clear, 'L2-POST', 'carried public set drops Phi in clear'),
    'M_sampler_never': (_m_sampler_never, 'L2-SAMPLE', 'deterministic sample empty'),
    'M_mask_no_merge': (_m_mask_no_merge, 'L2-MASK', 'masking equivalence ignores E1 merges'),
    'M_c9_off': (_m_c9_off, 'L2-GATES', 'C9 gate never fails'),
    'M_witness_max': (_m_witness_max, 'L2-C16', 'witness selection not minimal'),
    'M_guard_truthy': (_m_guard_truthy, 'L2-GUARD', 'engine accepts a truthy authorization'),
    'M_witness_first': (_m_witness_first, 'L2-WIT', 'shard keeps the first candidate, not the minimum (R1)'),
    'M_survivor_rep_only': (_m_survivor_rep_only, 'L2-SURV', 'reference gates on the representative only (R2)'),
    'M_residue_ignored': (_m_residue_ignored, 'L2-MRG', 'truncated residue or exceeded cap accepted (R3)'),
    'M_commits_unbound': (_m_commits_unbound, 'L2-CERT', 'certificate ignores differing commits (R5)'),
    'M_grant_unbound': (_m_grant_unbound, 'L2-GUARD', 'grant accepted without the running digests (R4 d)'),
    'M_C7_set2_computed': (_m_c7_set2_computed, 'L2-F1', 'C7 set 2 under G defined by the computed closure (E1-F3)'),
    'M_C7_carried_only': (_m_c7_carried_only, 'L2-F2', 'C7 compares the carried result with the reference, '
                                                      'no direct per-record closure (E1-F3)'),
    'M_C7_sample_rep_index': (_m_c7_sample_rep_index, 'L2-C7COV', 'C7 samples drawn over representative '
                                                                  'indices, not record indices (E1-F3)'),
    'M_ruleT_ignores_sigma': (_m_ruleT_ignores_sigma, 'L2-SIGMA', 'rule T evaluated on a non-OK sigma (E1-T2)'),
    'M_sigma_overrides_label': (_m_sigma_overrides_label, 'L2-PREC', 'the label ignores every failing check but '
                                                                     'sigma\'s (E1-T2)'),
    'M_proposal_on_failed_label': (_m_proposal_on_failed_label, 'L2-PREC', 'S1b proposed from a VOID, MISMATCH or '
                                                                           'INCOMPLETE run (E1-T2)'),
    'M_sigma_no_2d': (_m_sigma_no_2d, 'L2-2D', 'sigma ignores the reference recomputation of L_A and L_G (E1-T2 '
                                               '2 (d))'),
    'M_ruleT_reads_L3': (_m_ruleT_reads_L3, 'L2-T1', 'rule T reads the L3 bound\'s values (E1-T1)'),
    'M_LG_tip_reading': (_m_LG_tip_reading, 'L2-T5', 'L_G counted by the tip\'s cone (E1-T5)'),
    'M_counts_54': (_m_counts_54, 'L2-COUNTS', 'the four added counts dropped (E1-F6)'),
    'M_v8_counts_unrefused': (_m_v8_counts_unrefused, 'L2-V8COUNTS', 'v8 shared-tip and F_G enumeration not '
                                                                     'refused (caught before any enumeration)'),
    'M_placeholders_ignored': (_m_placeholders_ignored, 'L2-PLACEHOLDER', 'the v8 profile starts with kappa, G_D '
                                                                          'and O1 open'),
}


def main():
    args = sys.argv[1:]
    out = {}
    if '--mutant' in args:
        m = args[args.index('--mutant') + 1]
        MUTANTS[m][0]()
        out['mutant'] = m
    only = set(args[args.index('--only') + 1].split(',')) if '--only' in args else None
    for name, fn in CASES:
        if only is not None and name not in only:
            continue
        try:
            out[name] = fn()
        except Exception as e:      # a case that raises fails cleanly, with its exception type
            out[name] = {'pass': False, 'exception': type(e).__name__}
    out['failed'] = sorted(k for k, v in out.items() if isinstance(v, dict) and not v.get('pass'))
    out['pass'] = not out['failed']
    print(json.dumps(out, sort_keys=True, default=list))
    sys.exit(0 if out['pass'] else 2)


if __name__ == '__main__':
    main()
