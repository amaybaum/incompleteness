"""Layer-2 design evidence: the production entry points refuse v8's configuration class without
a valid authorization. Each attempt runs a production command for profile v8 in a fresh
work directory and must exit 2 with a VOID object naming certificate item 6, before any
context is constructed. Forged artifacts carry one defect that holds whatever the state of the
checkout (another commit; or, at HEAD, a designation not written by the owner), so the
outcome does not depend on whether the tree is clean. No valid authorization is constructed.
The review's in-process forgeries (review/LAYER2-REVIEW.md section 4) are run as controls on
the guard predicates only (no context, no record): a well-formed V8Grant and RefGrant built
directly without l2auth must be refused, both before and after the running digests are bound
in this process, since their digests are not the running ones (L2-R4 d). The pure decide() is
also run on a fabricated artifact and owner check against fabricated facts; it returns ok, which
is the documented limit that the host re-verification at landing (l2landing) addresses.
The dry run (l2plan) is also run for v8: it imports no engine, constructs no context and
computes no closure, and must report closures_computed = 0. Its record-enumerating option
--shared-tips (the shared-tip and F_G counts of C7's scope) must be refused for v8 before anything
is computed (exit 2, a refusal object); each enumerating function also refuses v8 at entry, so a
broken command-line check would end in that refusal, not in an enumeration. r5: the count-only
site-pair count (l2sitepairs.py) must refuse v8 without its own authorization (exit 2, no file), and
the dry run must refuse a forged v8 count file (exit 2).
Usage: python3 -I -B refusal_probe.py <layer2/code> <scratch dir>. Prints JSON; exit 0 iff
every attempt is refused and the dry run computed no closure."""
import json
import os
import subprocess
import sys

code, scratch = sys.argv[1], sys.argv[2]
sys.path.insert(0, code)
import l2auth as AUTH      # noqa: E402
import l2config as CFG     # noqa: E402
import l2manifest as MAN   # noqa: E402

py = sys.executable
head = subprocess.run(['git', '-c', 'gc.auto=0', '-c', 'maintenance.auto=false', '-C', code, 'rev-parse', 'HEAD'],
                      capture_output=True, text=True).stdout.strip()
cd = MAN.load(code)['code_digest']
url = AUTH.REPO_URL + 'pull/935#issuecomment-0'


def art(commit):
    return {'schema': AUTH.SCHEMA, 'scope': AUTH.SCOPE, 'commit': commit, 'code_digest': cd,
            'config_sha256': CFG.config_sha256(), 'owner': AUTH.OWNER, 'designation_url': url, 'designated_at': 'probe'}


def own(commit, author):
    return {'schema': AUTH.OWNER_SCHEMA, 'comment_url': url, 'author_login': author, 'body_sha256': '0'*64,
            'body_contains_required_line': True, 'commit': commit}


other = 'f'*40 if head != 'f'*40 else 'e'*40
variants = {
    'no_artifact': None,
    'other_commit': (art(other), own(other, AUTH.OWNER)),
    'not_owner': (art(head), own(head, 'not-the-owner')),
}
entry = {'l2enum': ['l2enum.py', '--profile', 'v8', '--shard', '0'],
         'l2s1a': ['l2s1a.py', '--profile', 'v8'],
         'l2preflight': ['l2preflight.py', '--profile', 'v8']}
results = {}
ok = True
for vname, v in variants.items():
    for ename, cmd in entry.items():
        wd = os.path.join(scratch, 'refusal-%s-%s' % (vname, ename))
        os.makedirs(wd, exist_ok=True)
        extra = []
        if v is not None:
            for nm, obj in (('authorization.json', v[0]), ('owner-check.json', v[1])):
                with open(os.path.join(wd, nm), 'w') as f:
                    json.dump(obj, f)
            extra = ['--authorization', os.path.join(wd, 'authorization.json'),
                     '--owner-check', os.path.join(wd, 'owner-check.json')]
        p = subprocess.run([py, '-I', '-B', os.path.join(code, cmd[0])] + cmd[1:] + ['--workdir', wd] + extra,
                           capture_output=True, text=True)
        try:
            o = json.loads(p.stdout)
        except ValueError:
            o = None
        refused = p.returncode == 2 and bool(o) and o.get('label') == 'VOID' and o.get('certificate_item') == 6
        written = sorted(n for n in os.listdir(wd) if n not in ('authorization.json', 'owner-check.json'))
        results['%s/%s' % (vname, ename)] = {'exit': p.returncode, 'label': o.get('label') if o else None,
                                             'certificate_item': o.get('certificate_item') if o else None,
                                             'refused': refused, 'files_written': written}
        ok &= refused and not written
# the review's forgeries, on the guard predicates only
import s0geom as G         # noqa: E402
import s0ref as REF        # noqa: E402
v8 = CFG.make_setup(G, 'v8')


def refused(f):
    try:
        f()
        return False
    except PermissionError:
        return True
    except TypeError:
        return True


forged = G.V8Grant('0'*40, '0'*64, '0'*64, 'forged')
forged_ref = REF.RefGrant('0'*40, '0'*64, '0'*64)
forge = {'V8Grant_direct_guard_unbound': refused(lambda: G._guard(v8, forged)),
         'V8Grant_direct_num_records_unbound': refused(lambda: G.num_records(v8, 2, forged)),
         'V8Grant_direct_record_at_unbound': refused(lambda: G.record_at(v8, 0, forged)),
         'RefGrant_direct_unbound': not REF._ref_granted(forged_ref),
         'RefGrant_r1_signature': refused(lambda: REF.RefGrant('0'*40))}
G.bind_running_digests(cd, CFG.config_sha256())
REF.bind_running_digests(cd, CFG.config_sha256())
forge.update({'V8Grant_direct_guard_bound': refused(lambda: G._guard(v8, forged)),
              'V8Grant_direct_num_records_bound': refused(lambda: G.num_records(v8, 2, forged)),
              'RefGrant_direct_bound': not REF._ref_granted(forged_ref),
              'rebind_other_digests': refused(lambda: G.bind_running_digests('1'*64, '1'*64))})
ok &= all(forge.values())
fab_head, fab_cd = 'f'*40, 'd'*64
fab_art = dict(art(fab_head), code_digest=fab_cd)
fab_own = own(fab_head, AUTH.OWNER)
fab_own['comment_url'] = fab_art['designation_url']
decide_fabricated = AUTH.decide(fab_art, fab_own, {'head_commit': fab_head, 'tree_clean': True, 'manifest_ok': True,
                                                   'code_digest': fab_cd, 'config_sha256': CFG.config_sha256()})
p = subprocess.run([py, '-I', '-B', os.path.join(code, 'l2plan.py'), '--profile', 'v8'], capture_output=True, text=True)
dr = json.loads(p.stdout)
dry = {k: dr[k] for k in ('records', 'orbits', 'single_orbits', 'pair_orbits', 'group_order', 'closures_computed',
                          'contexts_constructed', 'max_context_quantities', 'max_context_with_fixed', 'expected_checks')}
dry['shards'] = [[s['shard'], s['lo'], s['hi']] for s in dr['shards']]
dry['exit'] = p.returncode
ok &= p.returncode == 0 and dr['closures_computed'] == 0
dry['C7_populations'] = dr['C7_populations']
# the command-line attempt runs only after the function-level refusal is confirmed in this process,
# so that no attempt here can reach an enumeration of v8's record space
import l2plan as PLAN      # noqa: E402
try:
    PLAN.refuse_v8_enumeration(PLAN.Space(CFG.profile('v8')))
    fn_refused = False
except PermissionError:
    fn_refused = True
st, code_st = None, None
if fn_refused:
    p = subprocess.run([py, '-I', '-B', os.path.join(code, 'l2plan.py'), '--profile', 'v8', '--shared-tips'],
                       capture_output=True, text=True, timeout=60)
    code_st = p.returncode
    try:
        st = json.loads(p.stdout)
    except ValueError:
        st = None
shared_refused = fn_refused and code_st == 2 and bool(st) and st.get('label') == 'VOID' and bool(st.get('refused'))
ok &= shared_refused
# r5: the count-only site-pair count (l2sitepairs) on v8 without its own authorization; the command-line
# attempt runs only after the pure decision is confirmed to refuse, so no attempt can reach a count
import l2sitepairs as SPC  # noqa: E402
spc = {'decide_refuses': SPC.decide(None, None, {}).startswith('refused')}
if spc['decide_refuses']:
    outp = os.path.join(scratch, 'v8-site-pair-counts.json')
    p = subprocess.run([py, '-I', '-B', os.path.join(code, 'l2sitepairs.py'), '--profile', 'v8', '--out', outp],
                       capture_output=True, text=True, timeout=60)
    spc.update(exit=p.returncode, output=p.stdout.strip(), file_written=os.path.exists(outp))
    # a forged count file (internally consistent toy-shaped numbers claiming an authorization) is refused by
    # the dry run: it does not match v8's index space, or this module's digest
    forged = os.path.join(scratch, 'forged-counts.json')
    with open(forged, 'w') as f:
        json.dump({'schema': SPC.SCHEMA, 'profile': 'v8', 'setup': {'dim': 3, 'rho': 4, 'tlast': 23, 'port': [0, 0, -3]},
                   'nt': 25, 'sites': 1, 'site_pairs': 0, 'singles_representatives': [25], 'pairs_representatives': [],
                   'records_total': 25, 'representatives_total': 25, 'burnside_orbits': 25,
                   'module_sha256': '0'*64, 'authorization': 'ok'}, f)
    p = subprocess.run([py, '-I', '-B', os.path.join(code, 'l2plan.py'), '--profile', 'v8', '--site-pair-counts', forged],
                       capture_output=True, text=True, timeout=60)
    spc.update(forged_file_exit=p.returncode, forged_file_output=p.stdout.strip()[:200])
spc['refused'] = spc['decide_refuses'] and spc.get('exit') == 2 and '"refused"' in spc.get('output', '') and \
    not spc.get('file_written') and spc.get('forged_file_exit') == 2
ok &= spc['refused']
print(json.dumps({'attempts': len(results), 'refused': sum(r['refused'] for r in results.values()),
                  'v8_site_pair_count_refused': spc,
                  'v8_shared_tips_refused': {'function_refuses': fn_refused, 'exit': code_st, 'output': st,
                                             'refused': shared_refused},
                  'results': results, 'forgeries_refused': forge,
                  'forgeries': '%d of %d refused' % (sum(forge.values()), len(forge)),
                  'decide_on_fabricated_inputs_documented_limit': decide_fabricated,
                  'v8_dry_run_plan': dry, 'pass': ok}, indent=1, sort_keys=True))
sys.exit(0 if ok else 2)
