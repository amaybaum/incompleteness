"""Controlled excerpt check with the real R1 excerpt blobs: the deny-list in the layout manifest (sha256 of ids) must
find all 194 excerpts on the R1 drafting branches (positive control), none on main or the R1 branches that hold none
(negative controls), and none reachable from the simulated PR commit (main + layout)."""
import hashlib, json, os, subprocess, sys
O = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(O, 'work')
man = json.load(open(os.path.join(O, 'layout/verification/audits/evidence-retention/objects/manifest.json')))
deny = set(man['excerpt_denylist_sha256_of_id'])
def hits(gitdir, ref):
    out = subprocess.run(['git', '--git-dir', gitdir, 'rev-list', '--objects', ref], capture_output=True, text=True)
    if out.returncode:
        return 'ref missing'
    return sum(1 for l in out.stdout.split('\n') if l and hashlib.sha256(l.split()[0].encode()).hexdigest() in deny)
src = os.path.join(W, 'src.git')
res = {}
for ref in ('archive/r1-evidence-retention-drafting-20261016', 'tmp/r1-reproduce-proof-20261016',
            'tmp/r1-reproduce-proof-20261016-2', 'tmp/r1-reproduce-proof-20261016-3', 'tmp/r1-reproduce-proof-20261016-4',
            'tmp/r1-reproduce-proof-20261016-5', 'draft/evidence-retention-r1-20261016',
            'draft/evidence-retention-r1-hardening-20261017'):
    res['host branch ' + ref] = hits(src, 'refs/host/heads/' + ref)
res['main 66a981d5'] = hits(src, 'refs/heads/main')
res['simulated PR commit (main + layout), ' + sys.argv[1][:8]] = hits(os.path.join(W, 'pr-sim.git'), sys.argv[1])
print(json.dumps({'deny_list_entries': len(deny), 'hits': res}, indent=1))
json.dump({'deny_list_entries': len(deny), 'hits': res}, open(os.path.join(W, 'excerpt-controls.json'), 'w'), indent=1)
