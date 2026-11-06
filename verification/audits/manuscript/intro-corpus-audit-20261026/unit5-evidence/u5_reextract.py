#!/usr/bin/env python3
"""Unit 5 (#941) owner-standard re-extraction (#1031 c.6678672357 section 3).

Independently re-extracts every `#print axioms` report of the 14 modules that the 28-module expected
result adds over the 14-module one, from (H) the pinned historical log of job 121598983127 and (F) the
archived fresh-build log of run 40457712855, and compares each report by (module, fully qualified name)
with (S) the `#print axioms` commands of the source at 17b830bc and (J) the retained JSON on `main`.
It imports nothing from the evidence-retention archive, the gate or the earlier u5_check.py.

Usage: python3 -I u5_reextract.py <repo> <main_sha> <hist_log> <fresh_log> <out_tsv>
Prints one JSON summary; writes the per-report TSV; exits 1 on any mismatch or failed control.
"""
import hashlib, json, re, subprocess, sys

REPO, MAIN, HLOG, FLOG, OUT = sys.argv[1:6]
SRC = '17b830bcd0ecc36e10eff5b9eeca03bdd7198d86'
PIN28 = '2714278a7dd9057a73610658478661065152ca97'
P28 = 'verification/audits/manuscript/intro-corpus-audit-20261026/introduction-repro-ext/results-121598983127-28.json'
P14 = 'verification/audits/manuscript/intro-corpus-audit-20261026/introduction-repro-14/results-121598983127.json'
LM = 'verification/lean-mathlib'
PERM = ['propext', 'Classical.choice', 'Quot.sound']
OD15 = ['OIBridge.PhaseSource.permClass_onesFixing', 'OIBridge.PhaseSource.onesFixing_not_phasesAvailable',
        'OIBridge.PhysicalC4StorageReadback.routedAtStorage_forces_indivisible_somewhere']
fails = []


def show(c, p):
    return subprocess.run(['git', '-C', REPO, 'show', f'{c}:{p}'], capture_output=True, check=True).stdout


def revparse(x):
    return subprocess.run(['git', '-C', REPO, 'rev-parse', x], capture_output=True, text=True).stdout.strip()


# ---- the log parser (own implementation) ----------------------------------------------------------
TS = re.compile(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ')
HEAD = re.compile(r"^info: (?:\./)*((?:OIBridge/)?[^:\s]+\.lean):(\d+):(\d+): '(.+?)' "
                  r"(?:depends on axioms: \[(.*)|does not depend on any axioms\s*$)")


def parse(lines):
    """[(module_path, line, fqn, axioms)] from log lines; wrapped axiom lists are joined."""
    out, i, n = [], 0, len(lines)
    while i < n:
        s = TS.sub('', lines[i], count=1)
        m = HEAD.match(s)
        i += 1
        if not m:
            if "depends on axioms" in s or "does not depend on any axioms" in s:
                fails.append(f'unparsed report-like line: {s[:160]!r}')
            continue
        path, ln, _, name, rest = m.groups()
        if rest is None:
            out.append((path, int(ln), name, []))
            continue
        buf = rest
        while ']' not in buf:
            if i >= n:
                fails.append(f'unterminated axiom list for {name}'); break
            cont = TS.sub('', lines[i], count=1)
            if not cont.startswith(' '):
                fails.append(f'bad continuation for {name}: {cont[:80]!r}'); break
            buf += cont; i += 1
        body = buf[:buf.index(']')]
        if buf[buf.index(']') + 1:].strip():
            fails.append(f'trailing text after axiom list for {name}')
        out.append((path, int(ln), name, [a.strip() for a in body.split(',') if a.strip()]))
    return out


# ---- source: #print axioms commands and their fully qualified names ----------------------------------
def strip_lean(t):
    out, i, n, d = [], 0, len(t), 0
    while i < n:
        c2 = t[i:i + 2]
        if d:
            if c2 == '/-': d += 1; out.append('  '); i += 2
            elif c2 == '-/': d -= 1; out.append('  '); i += 2
            else: out.append('\n' if t[i] == '\n' else ' '); i += 1
        elif c2 == '/-': d = 1; out.append('  '); i += 2
        elif c2 == '--':
            j = t.find('\n', i); j = n if j < 0 else j; out.append(' ' * (j - i)); i = j
        else: out.append(t[i]); i += 1
    return ''.join(out)


def ns_join(stack):
    return '.'.join(x for x in stack if x)


# sections push None, namespaces push their components; the namespace joins the non-None entries
def source_prints2(text):
    stack, res = [], []
    for ln, s in enumerate(strip_lean(text).split('\n'), 1):
        m = re.match(r'^#print axioms\s+(\S+)\s*$', s)
        if m:
            p = m.group(1); ns = ns_join(stack)
            res.append((ln, p if p.startswith('OIBridge.') else (f'{ns}.{p}' if ns else p))); continue
        if '#print axioms' in s:
            fails.append(f'unparsed source print: {s!r}')
        m = re.match(r'^\s*namespace\s+(\S+)', s)
        if m: stack += m.group(1).split('.'); continue
        if re.match(r'^\s*(?:noncomputable\s+)?section\b', s): stack.append(None); continue
        m = re.match(r'^\s*end(?:\s+(\S+))?\s*$', s)
        if m:
            k = 1 if m.group(1) is None else len(m.group(1).split('.'))
            del stack[-k:]
    return res


# ---- inputs ------------------------------------------------------------------------------------------
summary = {'main': MAIN}
pin_blob = revparse(f'{PIN28}:{P28}')
main_blob = revparse(f'{MAIN}:{P28}')
summary['expected28'] = {'pin': PIN28, 'blob_at_pin': pin_blob, 'blob_on_main': main_blob}
if not (pin_blob == main_blob == '97a2377dbfc30987887dffea2b72e423feed079d'):
    fails.append('expected-28 blob mismatch')
J = json.loads(show(MAIN, P28))
J14 = json.loads(show(MAIN, P14))
added = sorted(set(J['expected']['modules']) - set(J14['expected']['modules']))
src = J['source']
summary['expected28_source_record'] = {'run': J['run']['id'], 'job': J['run']['job_id'], 'head_sha': J['run']['head_sha'],
                                       'served_lines': src['served_lines'], 'served_sha256': src['served_sha256'],
                                       'original_lines': src['original_lines']}

hraw = open(HLOG, 'rb').read()
htext = hraw.decode('utf-8')
hl = htext.split('\n')
served = '\n'.join(hl[:src['served_lines']])
summary['hist_log'] = {'sha256_full': hashlib.sha256(hraw).hexdigest(), 'lines': len(hl) - (hl[-1] == ''),
                       'served_sha256': hashlib.sha256(served.encode()).hexdigest()}
if summary['hist_log']['served_sha256'] != src['served_sha256']:
    fails.append('historical log served text does not match the retained served_sha256')
if summary['hist_log']['sha256_full'] != 'bc2291bc57d952779f27282211b588321618bf503d39d192840c777074cd0c81':
    fails.append('historical log full digest differs from the README record')
H = parse(hl[:src['served_lines']])
fraw = open(FLOG, 'rb').read()
F = parse(fraw.decode('utf-8', errors='strict').split('\n'))
summary['fresh_log'] = {'sha256': hashlib.sha256(fraw).hexdigest()}
summary['reports_parsed'] = {'hist_served': len(H), 'fresh': len(F)}


def index(reports):
    by = {}
    for path, ln, name, ax in reports:
        by.setdefault((path, name), []).append((ln, ax))
    return by


HI, FI = index(H), index(F)
H_by_name, F_by_name = {}, {}
for path, ln, name, ax in H:
    H_by_name.setdefault(name, set()).add(path)
for path, ln, name, ax in F:
    F_by_name.setdefault(name, set()).add(path)

rows, per_mod, mism = [], {}, []
for path in added:
    S = source_prints2(show(SRC, f'{LM}/{path}').decode('utf-8'))
    Smain = source_prints2(show(MAIN, f'{LM}/{path}').decode('utf-8'))
    je = {r['name']: r for r in J['expected']['modules'][path]['reports']}
    cnt = {'source': len(S), 'json': len(je), 'hist': 0, 'fresh': 0, 'mismatch': 0}
    if len(je) != len(J['expected']['modules'][path]['reports']):
        mism.append((path, 'duplicate FQN in JSON'))
    s_names = [n for _, n in S]
    if len(set(s_names)) != len(s_names):
        mism.append((path, 'duplicate FQN in source prints'))
    # reports in this module's file that the source does not print, in either log
    for lab, idx in (('hist', HI), ('fresh', FI)):
        extra = sorted(n for (p, n) in idx if p == path and n not in s_names)
        for n in extra:
            mism.append((path, f'{lab}: report without a source print: {n}'))
    if set(je) != set(s_names):
        mism.append((path, f'JSON names != source names: {sorted(set(je) ^ set(s_names))}'))
    for ln, fqn in S:
        row = {'module': path, 'fqn': fqn, 'src_line': ln}
        h, f = HI.get((path, fqn), []), FI.get((path, fqn), [])
        j = je.get(fqn)
        row['hist'] = h; row['fresh'] = f; row['json'] = (j['line'], j['axioms']) if j else None
        row['main_line'] = next((l for l, n in Smain if n == fqn), None)
        bad = []
        if len(h) != 1: bad.append(f'hist reports {len(h)}')
        if len(f) != 1: bad.append(f'fresh reports {len(f)}')
        if j is None: bad.append('absent from JSON')
        if not bad:
            (hl_, hax), (fl_, fax) = h[0], f[0]
            if not (hl_ == fl_ == j['line'] == ln): bad.append(f'line S{ln} H{hl_} F{fl_} J{j["line"]}')
            if not (hax == fax == j['axioms']): bad.append(f'axioms H{hax} F{fax} J{j["axioms"]}')
            if hax != PERM: bad.append(f'axioms not exactly the permitted three: {hax}')
            if not set(hax) <= set(PERM): bad.append('axiom outside the permitted set')
        if H_by_name.get(fqn, set()) - {path}: bad.append(f'hist: same FQN reported from {sorted(H_by_name[fqn] - {path})}')
        if F_by_name.get(fqn, set()) - {path}: bad.append(f'fresh: same FQN reported from {sorted(F_by_name[fqn] - {path})}')
        if row['main_line'] != ln: bad.append(f'print line on main {row["main_line"]}')
        cnt['hist'] += len(h); cnt['fresh'] += len(f)
        if bad:
            cnt['mismatch'] += 1; mism.append((path, fqn, bad))
        row['ok'] = not bad
        rows.append(row)
    per_mod[path] = cnt

summary['per_module'] = per_mod
summary['totals'] = {k: sum(v[k] for v in per_mod.values()) for k in ('source', 'json', 'hist', 'fresh', 'mismatch')}
summary['mismatches'] = mism

# per-report table, deterministic
lines = ['module\tfqn\tsrc_line_17b830bc\tsrc_line_main\thist_line\thist_axioms\tfresh_line\tfresh_axioms\tjson_line\tjson_axioms\tok']
for r in sorted(rows, key=lambda r: (r['module'], r['fqn'])):
    h = r['hist'][0] if len(r['hist']) == 1 else (None, None)
    f = r['fresh'][0] if len(r['fresh']) == 1 else (None, None)
    j = r['json'] or (None, None)
    fmt = lambda a: ','.join(a) if a is not None else '-'
    lines.append('\t'.join(map(str, [r['module'], r['fqn'], r['src_line'], r['main_line'], h[0], fmt(h[1]), f[0],
                                     fmt(f[1]), j[0], fmt(j[1]), 'ok' if r['ok'] else 'MISMATCH'])))
tsv = '\n'.join(lines) + '\n'
open(OUT, 'w').write(tsv)
summary['table'] = {'rows': len(rows), 'sha256': hashlib.sha256(tsv.encode()).hexdigest()}

summary['od15'] = {q: next(({k: r[k] for k in ('module', 'src_line', 'hist', 'fresh', 'json', 'ok')}
                            for r in rows if r['fqn'] == q), None) for q in OD15}
if any(v is None or not v['ok'] for v in summary['od15'].values()):
    fails.append('OD-15 declaration not matched')

# ---- controls ------------------------------------------------------------------------------------------
C = {}
t1 = ["2026-10-26T13:29:14.1Z info: OIBridge/X.lean:5:0: 'OIBridge.X.a' depends on axioms: [propext,",
      "2026-10-26T13:29:14.2Z  Classical.choice,", "2026-10-26T13:29:14.3Z  Quot.sound]",
      "info: ././OIBridge/Y.lean:7:0: 'OIBridge.Y.b' does not depend on any axioms",
      "info: OIBridge/Z.lean:9:0: 'OIBridge.Z.G₀_apply' depends on axioms: [propext, Lean.ofReduceBool]",
      "info: OIBridge/P.lean:3:0: 'OIBridge.P.f'' depends on axioms: [propext]",
      "info: OIBridge.lean:4:0: 'OIBridge.R.g' does not depend on any axioms"]
p = parse(t1)
C['wrapped_joined'] = p[0] == ('OIBridge/X.lean', 5, 'OIBridge.X.a', PERM)
C['no_axiom_form'] = p[1] == ('OIBridge/Y.lean', 7, 'OIBridge.Y.b', [])
C['unicode_name_and_forbidden_axiom_read'] = p[2] == ('OIBridge/Z.lean', 9, 'OIBridge.Z.G₀_apply', ['propext', 'Lean.ofReduceBool'])
C['primed_name'] = p[3] == ('OIBridge/P.lean', 3, "OIBridge.P.f'", ['propext'])
C['root_module_path'] = p[4] == ('OIBridge.lean', 4, 'OIBridge.R.g', [])
C['source_ns'] = source_prints2('namespace OIBridge\nnamespace Q\nsection S\ntheorem t : True := trivial\nend S\n'
                                '#print axioms t\nend Q\nend OIBridge\n#print axioms OIBridge.Q.t\n') == \
    [(6, 'OIBridge.Q.t'), (9, 'OIBridge.Q.t')]
# the real comparison must reject planted defects: re-run the row test on a mutated copy of one module
def row_bad(path, mutate):
    hi = {k: list(v) for k, v in HI.items()}
    mutate(hi)
    S = source_prints2(show(SRC, f'{LM}/{path}').decode('utf-8'))
    je = {r['name']: r for r in J['expected']['modules'][path]['reports']}
    for ln, fqn in S:
        h = hi.get((path, fqn), [])
        if len(h) != 1 or h[0][0] != ln or h[0][1] != je[fqn]['axioms']:
            return True
    return False
mp = 'OIBridge/PhaseSource.lean'; key = (mp, OD15[0])
C['missing_report_caught'] = row_bad(mp, lambda hi: hi.pop(key))
C['wrong_module_caught'] = row_bad(mp, lambda hi: hi.__setitem__(('OIBridge/Other.lean', OD15[0]), hi.pop(key)))
C['axiom_change_caught'] = row_bad(mp, lambda hi: hi.__setitem__(key, [(hi[key][0][0], ['propext'])]))
C['line_change_caught'] = row_bad(mp, lambda hi: hi.__setitem__(key, [(hi[key][0][0] + 1, hi[key][0][1])]))
C['duplicate_caught'] = row_bad(mp, lambda hi: hi[key].append(hi[key][0]))
C['unmutated_clean'] = not row_bad(mp, lambda hi: None)
summary['controls'] = C
if not all(C.values()):
    fails.append(f'control failed: {C}')
if mism:
    fails.append(f'{len(mism)} mismatch(es)')
summary['failures'] = fails
summary['verdict'] = 'PASS' if not fails else 'FAIL'
print(json.dumps(summary, indent=1, ensure_ascii=False))
sys.exit(1 if fails else 0)
