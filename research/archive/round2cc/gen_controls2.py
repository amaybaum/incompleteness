import ast
src = open('/home/user/incompleteness/verification/audits/manuscript/round-cc-1-corpus-correction/controls.py', encoding='utf-8').read()
def rep(s, old, new):
    assert s.count(old) == 1, (old[:60], s.count(old))
    return s.replace(old, new)
s = src
s = rep(s, "D_COMMIT = '0f2687b7b87925b53c6e3d8c6d1a233f36624dea'",
        "D_COMMIT = 'D-CC-2-PLACEHOLDER'  # the CC-1 halted landing on main; filled at drafting")
s = rep(s, "SOURCES = [f'papers/{p}.md' for p in PAPERS] + CHAPTERS + [FULL]",
        "SOURCES = [f'papers/{p}.md' for p in PAPERS] + CHAPTERS + [FULL]\n"
        "LEDGER = 'verification/coverage/LEDGER.json'\n"
        "PROBE = 'verification/lean/edge_rigidity_probe.py'\n"
        "VERIF = [LEDGER, PROBE]   # the two verification surfaces this round governs")
i = s.index('EDITS = [')
j = s.index('\n]\n', i) + 3
v3_old = "\n".join([
 '    {', '      "id": "SM:T-unnamed-f1d3c661",', '      "paper": "papers/SM.md",', '      "line": 140,',
 '      "kind": "Theorem",', '      "label": "",', '      "fingerprint": "f1d3c6619bfdb644",', '      "area": "sm",',
 '      "assumptions": "see the statement",', '      "checks": [],', '      "kernel": "GAP",',
 '      "delta": "not formalized",', '      "note": ""', '    },', ''])
v5_old = ('    the word is absent from the gauge passage (the heading through the Wilson action "now derived\n'
          '    rather than postulated"), and no proof-kernel language appears anywhere in the section. The')
v5_new = ('    the word is absent from the gauge passage (the heading through the plaquette functional, up to\n'
          '    its closing sentence), and no proof-kernel language appears anywhere in the section. The')
verif = '''
# Verification-surface instances (section 3.2): the consequences of the manuscript substitutions on the
# two files the release gate reads against them. V-1..V-3 are the coverage ledger; V-4, V-5 the probe.
VERIF_EDITS = [
 dict(item='V-1', disp='LEDGER', file=LEDGER, source='T-A1-1: the corollary at Substratum.md:262 re-fingerprinted by the census',
  old='      "fingerprint": "9330e1f409e986c0",',
  new='      "fingerprint": "f7e912991de09137",'),
 dict(item='V-2', disp='LEDGER', file=LEDGER, source='T-A3-1: the unnamed area-law lemma at SM.md:118; its id follows its body',
  old='      "id": "SM:L-unnamed-332dde89",',
  new='      "id": "SM:L-unnamed-ff7b7d06",'),
 dict(item='V-2', disp='LEDGER', file=LEDGER, source='T-A3-1: the same lemma, fingerprint',
  old='      "fingerprint": "332dde89a60f07d3",',
  new='      "fingerprint": "ff7b7d068e326e1f",'),
 dict(item='V-3', disp='LEDGER', file=LEDGER, source='T-A6-2: the Theorem header at SM.md:140 is removed, so the statement leaves the census (kernel GAP, no checks, no backlog row)',
  old=%r,
  new=''),
 dict(item='V-4', disp='PROBE', file=PROBE, source='T-A6-1: guard R7-A6P sub-check P5 delimits SM.md section 3.1 by the phrase the correction removes',
  old="    _end = _31.find('now derived rather than postulated.')",
  new="    _end = _31.find('That the link dynamics is governed by this functional is not derived here.')"),
 dict(item='V-5', disp='PROBE', file=PROBE, source='T-A6-1: the docstring of the same sub-check names the old delimiter',
  old=%r,
  new=%r),
]
ALL_EDITS = EDITS + VERIF_EDITS
# predicted census facts at E (tools/proof_census.py): id -> (paper, line, fingerprint); removed ids are absent
CENSUS_AT_E = {
 'SUBSTRATUM:C-effective-finiteness-gauge-class-transfer': ('papers/Substratum.md', 262, 'f7e912991de09137'),
 'SM:L-unnamed-ff7b7d06': ('papers/SM.md', 118, 'ff7b7d068e326e1f'),
}
CENSUS_ABSENT_AT_E = ['SM:T-unnamed-f1d3c661', 'SM:L-unnamed-332dde89']
CANONICAL_AT_D, CANONICAL_AT_E = 130, 129
PROBE_SENTINEL = 'That the link dynamics is governed by this functional is not derived here.'
''' % (v3_old, v5_old, v5_new)
s = s[:j] + verif + s[j:]
s = rep(s, "    for i, e in enumerate(EDITS):\n        s = read(os.path.join(base, e['file']))\n        if s.count(e['old']) != 1:",
        "    for i, e in enumerate(ALL_EDITS):\n        s = read(os.path.join(base, e['file']))\n        if s.count(e['old']) != 1:")
s = rep(s, "        if e['new'] in s:\n            errs.append(f'D: instance {i} ({e[\"item\"]}) new already present')",
        "        if e['new'] and e['new'] in s:\n            errs.append(f'D: instance {i} ({e[\"item\"]}) new already present')")
s = rep(s, "    for f in SOURCES:\n        s = read(os.path.join(base, f))\n        for e in EDITS:\n            if e['file'] == f:",
        "    for f in SOURCES + VERIF:\n        s = read(os.path.join(base, f))\n        for e in ALL_EDITS:\n            if e['file'] == f:")
s = rep(s, "    exp = expected_E(base)\n    for f in SOURCES:\n        s = read(os.path.join(repo, f))\n        if s != exp[f]:",
        "    exp = expected_E(base)\n    for f in SOURCES + VERIF:\n        s = read(os.path.join(repo, f))\n        if s != exp[f]:")
s = rep(s, "    for i, e in enumerate(EDITS):\n        s = read(os.path.join(repo, e['file']))\n        if e['old'] in s:\n            errs.append(f'E: instance {i} ({e[\"item\"]}) old still present')\n        if e['new'] not in s:",
        "    for i, e in enumerate(ALL_EDITS):\n        s = read(os.path.join(repo, e['file']))\n        if e['old'] in s:\n            errs.append(f'E: instance {i} ({e[\"item\"]}) old still present')\n        if e['new'] and e['new'] not in s:")
census_block = '''    # the census at E: the re-affirmed entries, the removed one, the canonical count, and the gate step itself
    if not skip_census:
        try:
            rows = json.loads(subprocess.run([sys.executable, 'tools/proof_census.py', '--json'], cwd=repo,
                                             capture_output=True, text=True, timeout=600).stdout)
            byid = {r['id']: r for r in rows}
            for cid, (paper, line, fp) in CENSUS_AT_E.items():
                r = byid.get(cid)
                if not r or (r['paper'], r['line'], r['fingerprint']) != (paper, line, fp):
                    errs.append(f'E: census {cid}: {None if not r else (r["paper"], r["line"], r["fingerprint"])} != {(paper, line, fp)}')
            for cid in CENSUS_ABSENT_AT_E:
                if cid in byid:
                    errs.append(f'E: census still carries {cid}')
            if len(rows) != CANONICAL_AT_E:
                errs.append(f'E: canonical statements {len(rows)} != {CANONICAL_AT_E}')
            led = json.load(open(os.path.join(repo, LEDGER), encoding='utf-8'))
            if len(led['entries']) != CANONICAL_AT_E:
                errs.append(f'E: ledger entries {len(led["entries"])} != {CANONICAL_AT_E}')
            cov = subprocess.run([sys.executable, 'tools/coverage_check.py'], cwd=repo, capture_output=True, text=True, timeout=900)
            if cov.returncode != 0:
                errs.append('E: coverage_check fails: ' + cov.stdout.strip().splitlines()[-1][:160])
        except Exception as ex:  # the census tools are part of the check; their absence is a failure
            errs.append(f'E: census/coverage tools failed: {ex}')
    sm = ' '.join(read(os.path.join(repo, 'papers/SM.md')).split())
    a = sm.find('### 3.1 Background independence'); b = sm.find('### 3.2 Why d = 3', a)
    if not (0 <= a < b) or sm[a:b].count(PROBE_SENTINEL) != 1:
        errs.append('E: the probe sentinel does not occur exactly once in SM.md section 3.1')
    # staleness stamps
'''
s = rep(s, "    # staleness stamps\n", census_block)
s = rep(s, "def check_E(repo, base):", "def check_E(repo, base, skip_census=False):")
s = rep(s, "    errs += scan_added([(e['file'], e['new']) for e in EDITS], base)",
        "    errs += scan_added([(e['file'], e['new']) for e in EDITS], base)   # manuscript text only; V-instances are code and data")
s = rep(s, "    for d in ('papers', 'book'):\n        shutil.copytree(os.path.join(base, d), os.path.join(tmp, d))",
        "    for d in ('papers', 'book', 'verification'):\n        shutil.copytree(os.path.join(base, d), os.path.join(tmp, d))")
s = rep(s, "    e2 = [x for x in check_E(tmp, base) if 'stale .tex' not in x]",
        "    e2 = [x for x in check_E(tmp, base, skip_census=True) if 'stale .tex' not in x]")
s = rep(s, "    m1 = [x for x in check_E(tmp, base) if 'stale .tex' not in x]",
        "    m1 = [x for x in check_E(tmp, base, skip_census=True) if 'stale .tex' not in x]")
s = s.replace('CC-1', 'CC-2')
if 'import json' not in s:
    s = s.replace('import re\n', 'import json\nimport re\n', 1)
if 'import subprocess' not in s:
    s = s.replace('import re\n', 'import re\nimport subprocess\n', 1)
open('controls2.py', 'w', encoding='utf-8').write(s)
ast.parse(s)
print('controls2.py written:', len(s.splitlines()), 'lines; parses; CC-1 mentions left:', s.count('CC-1'))
