S = '/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/v313/'
p = S + 'preregistration.md'
t = open(p).read()
for old, new in (
("""   code is removed, the headers of the 14 emptied checks, the twenty orphaned descriptions of the
   base and seal constants round `SI-3` removed, and six drift-control comment lines;""",
"""   code is removed, the headers of the 14 emptied checks, the nineteen orphaned descriptions of the
   base and seal constants round `SI-3` removed, and six drift-control comment lines;"""),
("""- **`C9`** (`E`): every string literal of the stage 2 guard that occurs in a file the round edits
  at `D` occurs in it at `E`; the README slices `R7-A6P` and `R7-A6I` read carry no over-reading, by
  their own scanner functions.""",
"""- **`C9`** (`E`): the files this round edits still carry what the retained predicates require of
  them: `verification/README.md` every string literal of the stage 2 guard that it carries at `D`,
  the anchor "`.github/workflows/verify.yml` runs" among them, and no over-reading in the slices
  `R7-A6P` and `R7-A6I` scan, by those checks' own scanner functions; `.github/workflows/verify.yml`
  `repertoire_lie` and no `lake build OIBridge.` or `lake env lean OIBridge/` line; `AGENTS.md` the
  §A.35 heading and "updates the registry in the same commit"; `tools/release_gate.py`
  `"lean-manuscript"`."""),
("""| 4. retained anchors | no edited file loses a string a retained predicate reads; `verification/README.md` keeps "`.github/workflows/verify.yml` runs" (control `C9`) |""",
"""| 4. retained anchors | no edited file loses a string a retained predicate requires of it; `verification/README.md` keeps "`.github/workflows/verify.yml` runs" (checkpoint `C9`) |"""),
):
    assert t.count(old) == 1, old[:50]
    t = t.replace(old, new)
open(p, 'w').write(t)

p = S + 'sim313.py'
t = open(p).read()
old = """    E = commit('E', {RD + 'result.md': b'# V3-13 result (rehearsal placeholder)\\n'})
"""
new = """    E = commit('E', {RD + 'result.md': b'# V3-13 result (rehearsal placeholder)\\n'})
    # C9: what the retained predicates require of the edited files
    import ast
    g = ast.parse(open(os.path.join(WT, GUARD), encoding='utf-8').read())
    lits = {n.value for n in ast.walk(g) if isinstance(n, ast.Constant) and isinstance(n.value, str)
            and len(n.value) >= 6}
    rd0 = git('show', D + ':verification/README.md')
    rd1 = open(os.path.join(WT, 'verification/README.md'), encoding='utf-8').read()
    f0, f1 = ' '.join(rd0.split()), ' '.join(rd1.split())
    lost = [s for s in lits if (s in rd0 and s not in rd1) or
            (' '.join(s.split()) in f0 and ' '.join(s.split()) not in f1)]
    report('C9 README: %d guard literals lost; anchor present' % len(lost),
           not lost and '`.github/workflows/verify.yml` runs' in rd1)
    wf = open(os.path.join(WT, '.github/workflows/verify.yml'), encoding='utf-8').read()
    report('C9 workflow: repertoire_lie, no lake build or lake env lean of an OIBridge module',
           'repertoire_lie' in wf and not re.search(r'lake build\\s+OIBridge\\.', wf)
           and not re.search(r'lake env lean\\s+OIBridge/', wf))
    ag = ' '.join(open(os.path.join(WT, 'AGENTS.md'), encoding='utf-8').read().split())
    report('C9 AGENTS: the A.35 heading and the registry sentence',
           '## §A.35 Registry contract for the Lean-to-manuscript census' in ag
           and 'updates the registry in the same commit' in ag)
    report('C9 release gate: lean-manuscript',
           '"lean-manuscript"' in open(os.path.join(WT, 'tools/release_gate.py')).read())
"""
assert t.count(old) == 1
t = t.replace(old, new)
open(p, 'w').write(t)
