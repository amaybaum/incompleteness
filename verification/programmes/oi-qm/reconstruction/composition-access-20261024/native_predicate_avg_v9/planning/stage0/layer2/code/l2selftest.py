"""NP-AVG-1 Stage 0 Layer 2: controls of the Layer-2 machinery (toy profile, synthetic
structured files and static checks only; no context of v8's class is constructed, except
the single refused construction of L2-GUARD, which raises before any context exists).

Usage: python3 -I -B l2selftest.py [--mutant NAME]
Prints one JSON object {case: {pass, ...}, failed, pass}; exit 0 iff every case passes, 2
otherwise. With --mutant, the named monkeypatch (MUTANTS below) is applied in this process
before the cases run; l2mutants.py counts a mutant as killed only when this exits 2 with
parseable output and its named case failed.
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
        dry = {'schema': 'np-avg-1/stage0/layer2/dryrun/1', 'profile': 'toy', 'records': N, 'orbits': so + po,
               'shards': plan, 'closures_computed': 0, 'config_sha256': CFG.config_sha256(), 'pass': True}
        draw = _write(d, 'dryrun.json', dry)
        cd = MAN.load(HERE)['code_digest']
        s1a = {'status': mods.get('s1a_status', 'OK'), 'L_A': mods.get('L_A', 0), 'L_G': mods.get('L_G', 0),
               'code_digest': cd, 'config_sha256': CFG.config_sha256(), 'status_reasons': []}
        sraw = _write(d, 's1a.json', s1a)
        _write(d, 's1a.O.json', s1a)
        pf = {'code_digest': cd, 'controls': {'X': {'pass': True, 'class': 'VOID'}},
              'base_collapsed': {'A': True, 'G': 'base' not in mods}, 'pass': True, 'profile': 'toy'}
        if 'preflight_mismatch' in mods:
            pf['controls']['C12_universe'] = {'pass': False, 'class': 'MISMATCH'}
        _write(d, 'preflight.json', pf)
        keys = [k for k in AN.count_keys() if k.split(':')[-1] not in AN.CLASS_KEYS
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
            sh = {'schema': 'np-avg-1/stage0/layer2/shard/2', 'profile': 'toy', 'shard': s, 'shards': len(plan),
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
                  'tree_clean': False, 'ci_run': None}
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
    ok = all(g[k]['checked'] == n for k in ('C0_context', 'C7', 'C11i', 'C17', 'C18')) and \
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
    differ, since (q9, 4)'s samples above slice 0 are p and V in clear."""
    res = {}
    ok = True
    for tag, tlast, k in (('toy_k2', 6, 2), ('toy_k1', 6, 1), ('toy_t4_k1', 4, 1)):
        base = CFG.profile('toy')
        prof = dict(base, k=k, setup=dict(base['setup'], tlast=tlast))
        sp = PLAN.Space(prof)
        st = prof['setup']
        setup = G.Setup(st['dim'], st['n'], st['rho'], tlast, tuple(st['port']), tuple(tuple(x) for x in st['sources']))
        recs = toy_records(setup) if k == 2 else [r for r in toy_records(setup) if len(r) == 1]
        for reading, merge_fixed in (('context', True), ('record_samples', False)):
            keys = Counter()
            for r in recs:
                if merge_fixed:
                    ctx = G.Context(setup, r, 'A')
                    keys[tuple(sorted(ctx.quants | ctx.fixed))] += 1
                else:
                    keys[tuple(sorted(G.record_samples(setup, r)))] += 1
            brute = sum(v for v in keys.values() if v > 1)
            ana = PLAN.masking_equivalent(sp, merge_fixed)
            res['%s_%s' % (tag, reading)] = [ana, brute]
            ok &= ana == brute
    differ = res['toy_t4_k1_context'][1] != res['toy_t4_k1_record_samples'][1]
    return {'pass': ok and differ, 'analytic_vs_brute': res, 'readings_differ_on_t4': differ}


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


CASES = [('L2-S1_static', t_static), ('L2-GUARD', t_guard), ('L2-POST', t_post), ('L2-ORB', t_orbits),
         ('L2-AUTH', t_auth), ('L2-MAN', t_manifest), ('L2-MRG', t_merge), ('L2-LBL', t_labels), ('L2-RT', t_rule_t),
         ('L2-C16', t_witness), ('L2-WIT', t_witness_running), ('L2-SURV', t_survivor_gates),
         ('L2-CERT', t_cert_commits), ('L2-LAND', t_landing), ('L2-SAMPLE', t_sample), ('L2-MASK', t_mask), ('L2-PLAN', t_plan),
         ('L2-SHTIP', t_shared_tips), ('L2-GATES', t_gates), ('L2-CFG', t_rule_config)]


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
}


def main():
    args = sys.argv[1:]
    out = {}
    if '--mutant' in args:
        m = args[args.index('--mutant') + 1]
        MUTANTS[m][0]()
        out['mutant'] = m
    for name, fn in CASES:
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
