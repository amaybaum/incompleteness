"""Build the predicted A40 execution as local commits in ../wt-a40-road (never pushed) and run the round's checks.
F = the preregistration alone; S = stages 1-2 (controls, probe, workflow edit, frozen module, wire); T = stage 3 (census
family, P0 sentence for the classified label); E = the rehearsal result note. Prints each commit and each check."""
import importlib.util, json, os, shutil, subprocess
S = os.path.dirname(os.path.abspath(__file__)) + '/'
W = S + '../wt-a40-road/'
D = 'b271b1dfe5a145d360c7c9433c81bfdf24ba0743'
TRAILER = '\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01XEQMD5kRhaU9WyeZt6dmM1'
def git(*a): return subprocess.run(('git', '-C', W) + a, capture_output=True, text=True, check=True).stdout.strip()
def commit(msg):
    git('add', '-A'); git('commit', '-q', '-m', msg + TRAILER); return git('rev-parse', 'HEAD')
spec = importlib.util.spec_from_file_location('c', S + 'rec/controls.py'); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
git('checkout', '-q', '--detach', D); git('reset', '-q', '--hard', D); git('clean', '-qfd')
os.makedirs(W + C.RDIR, exist_ok=True)
shutil.copy(S + 'rec/preregistration.md', W + C.RDIR)
F = commit('A40 pre-freeze (disposable, never landed): the draft preregistration alone')
shutil.copy(S + 'rec/controls.py', W + C.RDIR)
shutil.copy(S + 'dita_torus_locus_probe.py', W + C.PROBE)
wf = open(W + C.WORKFLOW, encoding='utf-8').read(); open(W + C.WORKFLOW, 'w', encoding='utf-8').write(C.expected_workflow(wf))
root = open(W + C.ROOT, encoding='utf-8').read(); open(W + C.ROOT, 'w', encoding='utf-8').write(root.replace(C.WIRE_AFTER, C.WIRE_AFTER + C.WIRE, 1))
shutil.copy(S + 'mod40F.lean', W + C.MODULE)
S12 = commit('A40 pre-freeze (disposable, never landed): controls, the probe in its own shard, the reference module, the wire')
cen = json.loads(open(W + C.CENSUS, encoding='utf-8').read())
fam = json.load(open(S + 'census_family40.json', encoding='utf-8'))
cen['families'].append(fam)
open(W + C.CENSUS, 'w', encoding='utf-8').write(json.dumps(cen, indent=2, ensure_ascii=False) + '\n')
road = open(W + C.ROADMAP, encoding='utf-8').read(); open(W + C.ROADMAP, 'w', encoding='utf-8').write(C.expected_roadmap(road, C.PROVED))
T3 = commit('A40 pre-freeze (disposable, never landed): census family and the P0 sentence; the predicted execution tree less the result note')
lab = C.PROVED
note = ('# Track B act 40 — result (local rehearsal only)\n\n**Outcome:** `%s`\n\n' % lab + '> ' + C.SENTENCES[lab] + '\n\n'
        + '> **' + C.MENTION + ' — the result note.**\n' + '\n'.join('> ' + l for l in C.CLAUSE.split('\n')) + '\n\n'
        + ', '.join('`%s`' % nm for nm, _ in C.REQUIRED[lab]) + '\n\nThe reference implementation is `%s`; the module at E is `%s`.\n\n' % (C.MODULE_BLOB, C.blob_id(open(W + C.MODULE, encoding='utf-8').read()))
        + 'dita_torus_locus_probe: OK -- (rehearsal)\n')
open(W + C.RDIR + 'result.md', 'w', encoding='utf-8').write(note)
E = commit('A40 local rehearsal only: a synthetic result note')
print('F  ', F, 'prereg blob', git('rev-parse', F + ':' + C.RDIR + 'preregistration.md'))
print('S12', S12); print('T3 ', T3, '(the predicted execution tree less the result note)'); print('E  ', E)
for cmd in (['python3', C.RDIR + 'controls.py', 'check', E], ['python3', C.RDIR + 'controls.py', '--self-test'],
            ['python3', 'tools/legacy_records_check.py', E], ['python3', 'tools/artifact_placement_check.py'],
            ['python3', 'tools/lean_manuscript_census.py']):
    r = subprocess.run(cmd, cwd=W, capture_output=True, text=True)
    print('$', ' '.join(cmd[1:]), '-> exit', r.returncode); print('   ', r.stdout.strip().split('\n')[-1][:200])
