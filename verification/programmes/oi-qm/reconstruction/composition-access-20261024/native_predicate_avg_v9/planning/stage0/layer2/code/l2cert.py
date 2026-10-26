"""NP-AVG-1 Stage 0 Layer 2: the fail-closed execution certificate (section 5b item 8).

startup(): run by every computing entry point (l2s1a, l2enum) before anything is computed:
  item 1  the manifest (code SHA-256 values and the configuration digest) verifies, and the
          frozen Rule's fields equal the configuration's; the running digests are then bound in
          the engine and the reference (a grant must carry them, L2-R4 d);
  item 6  for a profile that requires it, the v8 authorization is granted (l2auth);
  item 1  for a profile that requires authorization, no OWNER placeholder remains in the
          configuration. Erratum E1 filled T1, T2, T5, T6, F3 and F6, and the owner's rulings of
          2026-10-26 fixed the kappa method, the sequencing and the 24-hour ceiling; the open
          placeholders are kappa's components u_cal and u_model, the reserve, the retry allowance
          (r5, the campaign ledger), the v8 survivor cap, G_D (the Lemma G-D reference form) and O1
          (E_G as a C7 set), so the v8 profile is refused while any of them is open;
  item 2  preflight.json exists for this code_digest and profile and passed;
  item 3  mutant-campaign.json exists for this code_digest and passed ('full' for v8);
  item 7  dryrun.json exists for this configuration and computed no closure, its shard plan is the
          profile's deterministic subdivision with every accounting check true (r5); for a profile
          that requires authorization, its complete cost estimate admits the launch under kappa.
On any failure it prints {"label": "VOID", ...} and exits 2.

build (python3 -I -B l2cert.py --build --profile P --workdir DIR): assembles
DIR/certificate.json from the structured files only (items 1-8), and exits 0 iff every item
holds. It reads exit statuses and JSON files, never log text (section A.44).
"""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import l2config as CFG    # noqa: E402
import l2manifest as MAN  # noqa: E402

ALL = ('manifest', 'auth', 'preflight', 'mutants', 'dryrun')


def void(item, reason):
    print(json.dumps({'label': 'VOID', 'certificate_item': item, 'reason': reason}, sort_keys=True))
    sys.exit(2)


def _git(*a):
    p = subprocess.run(['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', '-C', HERE] + list(a),
                       capture_output=True, text=True)
    return p.returncode, p.stdout.strip()


def head_commit():
    rc, out = _git('rev-parse', 'HEAD')
    return out if rc == 0 else None


def tree_clean():
    """True iff the Layer-2 directory has no change against HEAD (tracked or untracked)."""
    rc, out = _git('status', '--porcelain', '--untracked-files=all', '--', os.path.dirname(HERE))
    return rc == 0 and out == ''


def ci_run():
    """The host's run identity, from the workflow environment (None outside CI)."""
    if not os.environ.get('GITHUB_RUN_ID'):
        return None
    return {'run_id': os.environ.get('GITHUB_RUN_ID'), 'run_attempt': os.environ.get('GITHUB_RUN_ATTEMPT'),
            'repository': os.environ.get('GITHUB_REPOSITORY'), 'workflow': os.environ.get('GITHUB_WORKFLOW')}


def _json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except (OSError, ValueError):
        return None


def rule_fields_ok():
    import s0geom as G
    return json.loads(json.dumps(vars(G.Rule()))) == CFG.CONFIG['rules']['L3prime']


def startup(pname, workdir, args, need=ALL):
    prof = CFG.profile(pname)
    ok, diffs, man = MAN.verify(HERE)
    if not ok:
        void(1, 'manifest mismatch: %s' % diffs[:3])
    if not rule_fields_ok():
        void(1, 'frozen Rule fields differ from the configuration')
    code_digest = man['code_digest']
    import s0geom as G
    import s0ref as REF
    G.bind_running_digests(code_digest, CFG.config_sha256())
    REF.bind_running_digests(code_digest, CFG.config_sha256())
    st = {'grant': None, 'refgrant': None, 'echo': None, 'head': head_commit(), 'tree_clean': tree_clean(),
          'ci_run': ci_run(), 'code_digest': code_digest}
    if 'auth' in need and prof['requires_authorization']:
        import l2auth as AUTH
        art = args[args.index('--authorization') + 1] if '--authorization' in args else None
        own = args[args.index('--owner-check') + 1] if '--owner-check' in args else None
        decision, grant, refgrant, echo = AUTH.issue_grant(art, own, HERE)
        if decision != 'ok':
            void(6, decision)
        st.update(grant=grant, refgrant=refgrant, echo=echo)
    if prof['requires_authorization'] and CFG.placeholders():
        void(1, 'owner rulings unset in the configuration: %s' % CFG.placeholders())
    if 'preflight' in need:
        pf = _json(os.path.join(workdir, 'preflight.json'))
        if not pf or pf.get('code_digest') != code_digest or pf.get('profile') != pname or pf.get('pass') is not True:
            void(2, 'no passing pre-flight result for this code_digest and profile')
    if 'mutants' in need:
        mc = _json(os.path.join(workdir, 'mutant-campaign.json'))
        modes = ('full',) if prof['requires_authorization'] else ('quick', 'full')
        if not mc or mc.get('code_digest') != code_digest or mc.get('pass') is not True or mc.get('mode') not in modes:
            void(3, 'no passing mutant-campaign result (%s) for this code_digest' % '/'.join(modes))
    if 'dryrun' in need:
        dr = _json(os.path.join(workdir, 'dryrun.json'))
        if not dr or dr.get('profile') != pname or dr.get('config_sha256') != CFG.config_sha256() or \
                dr.get('closures_computed') != 0 or dr.get('pass') is not True:
            void(7, 'the dry run is mandatory before the real run')
        if (dr.get('shard_plan') or {}).get('kind') != prof['shard_plan'] or \
                not all((dr.get('shard_plan') or {}).get('accounting', {}).values() or [False]):
            void(7, 'the dry run\'s shard plan is not the profile\'s deterministic subdivision, or its accounting fails')
        if prof['requires_authorization'] and (dr.get('cost') or {}).get('launch_within_budget') is not True:
            void(7, 'the complete cost estimate does not admit the launch under kappa')
    return st


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def same_bytes(a, b):
    try:
        with open(a, 'rb') as f, open(b, 'rb') as g:
            return f.read() == g.read()
    except OSError:
        return False


def commits_consistent(workdir, auth_commit=None):
    """L2-R5: preflight.json, s1a.json (and s1a.O.json), every shard (and its -O copy) and
    result.json record one and the same commit; with auth_commit, it equals that too.
    Returns (holds, {file: commit})."""
    rec = {}
    for n in sorted(os.listdir(workdir)):
        if n in ('preflight.json', 's1a.json', 's1a.O.json', 'result.json', 'result.O.json') or \
                (n.startswith('shard-') and n.endswith('.json')):
            j = _json(os.path.join(workdir, n))
            rec[n] = (j or {}).get('commit')
    need = {'preflight.json', 's1a.json', 'result.json'}
    vals = set(rec.values())
    ok = need <= set(rec) and any(n.startswith('shard-') for n in rec) and len(vals) == 1 and None not in vals
    if auth_commit is not None:
        ok = ok and vals == {auth_commit}
    return ok, rec


def build(pname, workdir):
    prof = CFG.profile(pname)
    ok, diffs, man = MAN.verify(HERE)
    cd = man.get('code_digest') if man else None
    J = lambda n: _json(os.path.join(workdir, n))  # noqa: E731
    pf, mc, dr, s1, res = J('preflight.json'), J('mutant-campaign.json'), J('dryrun.json'), J('s1a.json'), \
        J('result.json')
    items = {}
    items['1_manifest'] = {'holds': ok and rule_fields_ok(), 'code_digest': cd, 'config_sha256': CFG.config_sha256(),
                           'files': man.get('files') if man else None, 'differences': diffs}
    items['2_preflight'] = {'holds': bool(pf) and pf.get('pass') is True and pf.get('code_digest') == cd,
                            'sha256': sha(os.path.join(workdir, 'preflight.json')) if pf else None,
                            'controls': pf.get('controls') if pf else None}
    items['3_mutant_campaign'] = {'holds': bool(mc) and mc.get('pass') is True and mc.get('code_digest') == cd and
                                  mc.get('mode') in (('full',) if prof['requires_authorization'] else ('quick', 'full')),
                                  'mode': mc.get('mode') if mc else None,
                                  'sha256': sha(os.path.join(workdir, 'mutant-campaign.json')) if mc else None}
    gates = res.get('in_run_gates') if res else None
    items['4_in_run_gates'] = {'holds': bool(res) and res.get('label') not in ('VOID', 'MISMATCH') and
                               not res.get('void_reasons') and not res.get('mismatch_reasons'), 'gates': gates}
    items['5_merge'] = {'holds': bool(res) and not res.get('incomplete_reasons'),
                        'coverage': res.get('coverage') if res else None}
    auth = (res or {}).get('authorization') or {}
    items['6_authorization'] = {'holds': (not prof['requires_authorization']) or
                                (auth.get('decision') == 'ok' and bool(auth.get('owner_check'))
                                 and bool(auth.get('ci_run'))),
                                'echo': res.get('authorization') if res else None,
                                'required': prof['requires_authorization'],
                                'landing_verification_required': prof['requires_authorization'],
                                'landing_verification': 'before the result lands, l2landing.py compares the '
                                'designation comment re-fetched from the host (author login, body SHA-256, '
                                'required line) with the owner check echoed in result.json (L2-R4 c)'}
    shards = sorted(n for n in os.listdir(workdir) if n.startswith('shard-') and n.endswith('.json') and '.O.' not in n)
    det = {n: same_bytes(os.path.join(workdir, n), os.path.join(workdir, n[:-5] + '.O.json')) for n in shards}
    det['s1a.json'] = same_bytes(os.path.join(workdir, 's1a.json'), os.path.join(workdir, 's1a.O.json'))
    det['result.json'] = same_bytes(os.path.join(workdir, 'result.json'), os.path.join(workdir, 'result.O.json'))
    auth_commit = ((auth.get('artifact') or {}).get('commit')) if prof['requires_authorization'] else None
    c_ok, c_rec = commits_consistent(workdir, auth_commit)
    if prof['requires_authorization'] and auth_commit is None:
        c_ok = False
    clean = {n: (_json(os.path.join(workdir, n)) or {}).get('tree_clean') for n in c_rec}
    items['2_preflight']['commit_binding'] = c_ok
    items['2_preflight']['holds'] = items['2_preflight']['holds'] and c_ok
    items['7_determinism'] = {'holds': all(det.values()) and bool(dr) and dr.get('closures_computed') == 0 and c_ok
                              and (not prof['requires_authorization'] or all(v is True for v in clean.values()
                                                                               if v is not None)),
                              'commits': c_rec, 'commits_bound': c_ok, 'tree_clean': clean,
                              'normal_vs_O_identical': det, 'dryrun_sha256': sha(os.path.join(workdir, 'dryrun.json'))
                              if dr else None}
    items['8_labels'] = {'holds': bool(res) and res.get('label_source') == 'merge of structured files',
                         'label': res.get('label') if res else None,
                         'inputs': res.get('inputs') if res else None}
    cert = {'schema': 'np-avg-1/stage0/layer2/certificate/1', 'profile': pname, 'commit': head_commit(),
            'items': items, 'holds': all(v['holds'] for v in items.values()),
            'note': 'A certificate that holds attests that the run followed Layer 2; it does not make the label '
                    'a proof. Rule T outcome and label are read from result.json.'}
    with open(os.path.join(workdir, 'certificate.json'), 'w') as f:
        f.write(json.dumps(cert, indent=1, sort_keys=True) + '\n')
    return cert


def main():
    args = sys.argv[1:]
    pname = args[args.index('--profile') + 1]
    workdir = args[args.index('--workdir') + 1]
    cert = build(pname, workdir)
    print(json.dumps({'holds': cert['holds'], 'items': {k: v['holds'] for k, v in cert['items'].items()}},
                     sort_keys=True))
    sys.exit(0 if cert['holds'] else 2)


if __name__ == '__main__':
    main()
