#!/usr/bin/env python3
"""Unit 5 (#941) read-only evidence check: OD-15 and EV-28 static and artifact layers.

Reads git objects from a repository and (optionally) the unpacked artifact of the fresh-build
replay run. Writes nothing to the repository. Prints one JSON document; exits 1 on any failure.

Usage: python3 -I u5_check.py <repo> <main_sha> [<artifact_dir>]
"""
import json, re, subprocess, sys, hashlib, os

REPO = sys.argv[1]
MAIN = sys.argv[2]
ART = sys.argv[3] if len(sys.argv) > 3 else None
SRC = '17b830bcd0ecc36e10eff5b9eeca03bdd7198d86'
PIN28 = '2714278a7dd9057a73610658478661065152ca97'
EXP14_C = 'f5efa7a0813218b580272f7fd80a6b0c87eb6657'
P28 = 'verification/audits/manuscript/intro-corpus-audit-20261026/introduction-repro-ext/results-121598983127-28.json'
P14 = 'verification/audits/manuscript/intro-corpus-audit-20261026/introduction-repro-14/results-121598983127.json'
P14_HIST = 'papers/introduction_repro/results-121598983127.json'
LM = 'verification/lean-mathlib'
PERMITTED = ['propext', 'Classical.choice', 'Quot.sound']
OD15 = {'PhaseSource': ['permClass_onesFixing', 'onesFixing_not_phasesAvailable'],
        'PhysicalC4StorageReadback': ['routedAtStorage_forces_indivisible_somewhere']}

fails = []


def git(*a):
    return subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, text=True, check=True).stdout


def show(c, p):
    r = subprocess.run(['git', '-C', REPO, 'show', f'{c}:{p}'], capture_output=True)
    return r.stdout.decode('utf-8') if r.returncode == 0 else None


def blob(c, p):
    r = subprocess.run(['git', '-C', REPO, 'rev-parse', f'{c}:{p}'], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else None


def fail(msg):
    fails.append(msg)


def strip_lean(text):
    """Replace comments (nested /- -/, --) and string literals by spaces, keeping newlines."""
    out, i, n, depth = [], 0, len(text), 0
    while i < n:
        c2 = text[i:i + 2]
        if depth:
            if c2 == '/-':
                depth += 1; out.append('  '); i += 2
            elif c2 == '-/':
                depth -= 1; out.append('  '); i += 2
            else:
                out.append('\n' if text[i] == '\n' else ' '); i += 1
        elif c2 == '/-':
            depth = 1; out.append('  '); i += 2
        elif c2 == '--':
            j = text.find('\n', i)
            j = n if j < 0 else j
            out.append(' ' * (j - i)); i = j
        elif text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            seg = text[i:j + 1]
            out.append(''.join('\n' if ch == '\n' else ' ' for ch in seg)); i = j + 1
        else:
            out.append(text[i]); i += 1
    return ''.join(out)


PRINT = re.compile(r'^#print axioms\s+(\S+)\s*$')
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*'
                  r'(theorem|lemma|def|abbrev|structure|instance|class|inductive|opaque|axiom)\s+'
                  r'([^\s:({\[]+)')
NS_OPEN = re.compile(r'^\s*namespace\s+(\S+)')
SEC_OPEN = re.compile(r'^\s*(?:noncomputable\s+)?section(?:\s+(\S+))?\s*$')
END = re.compile(r'^\s*end(?:\s+(\S+))?\s*$')
HAZARD = {
    'sorry': re.compile(r'\bsorry\b'), 'admit': re.compile(r'\badmit\b'),
    'native_decide': re.compile(r'\bnative_decide\b'), 'axiom_decl': re.compile(r'(?m)^\s*(?:private\s+)?axiom\s'),
    'implemented_by': re.compile(r'implemented_by'), 'extern': re.compile(r'@\[\s*extern'),
    'unsafe': re.compile(r'\bunsafe\b'), 'ofReduceBool': re.compile(r'ofReduceBool'),
    'trustCompiler': re.compile(r'trustCompiler'),
}


def scan(text):
    """(prints: [(line, printed, ns)], decls: set(fullname), hazards: {k: n}) of one module."""
    st = strip_lean(text)
    lines_raw, lines = text.split('\n'), st.split('\n')
    stack, prints, decls = [], [], set()
    for ln, (raw, s) in enumerate(zip(lines_raw, lines), 1):
        m = PRINT.match(s)
        if '#print axioms' in s and not m:
            fail(f'unparsed #print axioms line {ln}: {raw!r}')
        if m:
            prints.append((ln, m.group(1), '.'.join(x for k, x in stack if k == 'ns')))
            continue
        m = NS_OPEN.match(s)
        if m:
            for part in m.group(1).split('.'):
                stack.append(('ns', part))
            continue
        m = SEC_OPEN.match(s)
        if m:
            stack.append(('sec', m.group(1) or '')); continue
        m = END.match(s)
        if m:
            name = m.group(1)
            if name is None:
                stack.pop()
            else:
                k = len(name.split('.'))
                del stack[-k:]
            continue
        m = DECL.match(s)
        if m and m.group(1) != 'instance':
            ns = '.'.join(x for k, x in stack if k == 'ns')
            nm = m.group(2)
            if nm.startswith('_root_.'):
                decls.add(nm[len('_root_.'):])
            else:
                decls.add(f'{ns}.{nm}' if ns else nm)
    hz = {k: len(r.findall(st)) for k, r in HAZARD.items()}
    return prints, decls, hz


def imports(text):
    return re.findall(r'(?m)^import\s+(\S+)', strip_lean(text))


def tree_modules(c):
    names = git('ls-tree', '-r', '--name-only', c, LM).split()
    return {n[len(LM) + 1:-5].replace('/', '.'): n for n in names if n.endswith('.lean')}


def closure(c, mods, root):
    seen, todo = set(), [root]
    while todo:
        m = todo.pop()
        if m in seen or m not in mods:
            continue
        seen.add(m)
        todo += [i for i in imports(show(c, mods[m])) if i.startswith('OIBridge')]
    return seen


report = {'main': MAIN, 'source_commit': SRC, 'pin28': PIN28}

# ---- the two expected results -----------------------------------------------------------------
b28_pin, b28_main, b14 = blob(PIN28, P28), blob(MAIN, P28), blob(EXP14_C, P14_HIST)
report['blobs'] = {'28@pin': b28_pin, '28@main': b28_main, '14@f5efa7a0': b14, '14@main': blob(MAIN, P14)}
if not (b28_pin == b28_main == '97a2377dbfc30987887dffea2b72e423feed079d'):
    fail('28-module blob differs from 97a2377d at the pin or on main')
if not (b14 == report['blobs']['14@main'] == '61cfd6ea2df4590cc2ff86f90fc8f50ab71201f7'):
    fail('14-module blob differs from 61cfd6ea')
e28, e14 = json.loads(show(MAIN, P28)), json.loads(show(MAIN, P14))
m28, m14 = e28['expected']['modules'], e14['expected']['modules']
added = sorted(set(m28) - set(m14))
rest28, rest14 = dict(e28), dict(e14)
rest28['expected'] = {k: v for k, v in e28['expected'].items() if k != 'modules'}
rest14['expected'] = {k: v for k, v in e14['expected'].items() if k != 'modules'}
report['structure'] = {
    'modules_28': len(m28), 'modules_14': len(m14), 'added': len(added),
    'shared_identical': all(m28[k] == m14[k] for k in m14), 'other_fields_identical': rest28 == rest14,
    'reports_28': sum(len(v['reports']) for v in m28.values()),
    'reports_14': sum(len(v['reports']) for v in m14.values()),
    'permitted_axioms': e28['expected']['permitted_axioms'],
    'head_sha': e28['run']['head_sha'],
}
s = report['structure']
if not (s['modules_28'] == 28 and s['modules_14'] == 14 and s['added'] == 14 and s['shared_identical']
        and s['other_fields_identical'] and s['reports_28'] == 534 and s['reports_14'] == 286
        and s['permitted_axioms'] == PERMITTED and s['head_sha'] == SRC):
    fail('expected-result structure differs from the README description')
README_ADDED = ['CanonicalMeasure', 'CausalReadback', 'FiniteEntropy', 'FrozenSourcing', 'OIRealization',
                'OperationalAssembly', 'PhaseSource', 'PhysicalC4StorageReadback', 'QuantumRepresentationT2',
                'ReadWriteControl', 'RootedClassification', 'RootedClassificationAllTime', 'StructuralClosure',
                'SubstratumInterface']
if added != [f'OIBridge/{x}.lean' for x in README_ADDED]:
    fail(f'added modules differ from README list: {added}')

# ---- source-tree facts at the source commit and on main ----------------------------------------
mods_src, mods_main = tree_modules(SRC), tree_modules(MAIN)
gated_src = closure(SRC, mods_src, 'OIBridge')
gated_main = closure(MAIN, mods_main, 'OIBridge')
report['gated'] = {'src_modules': len(mods_src), 'src_closure': len(gated_src),
                   'main_modules': len(mods_main), 'main_closure': len(gated_main)}
decls_src = set()
scan_src = {}
for m, p in mods_src.items():
    scan_src[m] = scan(show(SRC, p))
    decls_src |= scan_src[m][1]
decls_main, scan_main = set(), {}
for m, p in mods_main.items():
    scan_main[m] = scan(show(MAIN, p))
    decls_main |= scan_main[m][1]

# tool-level properties of lean_axiom_check on main: ASCII-only print names and short-name collisions
allprints_main = [(m, ln, nm) for m, (pr, _, _) in scan_main.items() for ln, nm, _ in pr]
nonascii = [(m, ln, nm) for m, ln, nm in allprints_main if not re.fullmatch(r"[A-Za-z0-9_.']+", nm)]
short = {}
for m, ln, nm in allprints_main:
    short.setdefault(nm.split('.')[-1], set()).add(m)
collide = {k: sorted(v) for k, v in short.items() if len(v) > 1}
report['axiom_tool_on_main'] = {'prints': len(allprints_main), 'non_ascii_print_names': nonascii,
                                'short_name_collisions_across_modules': len(collide)}

def check_entry(path, e, record=True):
    mod = path[:-5].replace('/', '.')
    v = {}
    src = show(SRC, f'{LM}/{path}')
    v['exists_src'] = src is not None
    v['in_gated_build_src'] = mod in gated_src
    v['blob_src'], v['blob_pin'], v['blob_main'] = (blob(SRC, f'{LM}/{path}'), blob(PIN28, f'{LM}/{path}'),
                                                     blob(MAIN, f'{LM}/{path}'))
    v['in_gated_build_main'] = mod in gated_main
    prints, _, hz = scan_src[mod]
    exp_lines = sorted(r['line'] for r in e['reports'])
    rng = sorted(x for a, b in e['print_lines'] for x in range(a, b + 1))
    v['prints_src'] = len(prints)
    v['print_lines_match'] = [ln for ln, _, _ in prints] == exp_lines == rng
    v['count_match'] = e['prints'] == len(prints) == len(e['reports'])
    v['status'] = e['status']
    by_line = {ln: (nm, ns) for ln, nm, ns in prints}
    names_ok, decl_ok, unresolved = True, True, []
    for r in e['reports']:
        nm, ns = by_line.get(r['line'], (None, None))
        if nm is None:
            names_ok = False; continue
        want = nm if nm.startswith('OIBridge.') else (f'{ns}.{nm}' if ns else nm)
        if r['name'] != want:
            # resolution through `open` is legitimate: accept only a suffix match, and log it
            if not r['name'].endswith('.' + nm):
                names_ok = False
            unresolved.append((r['line'], nm, r['name']))
        if r['name'] not in decls_src:
            decl_ok = False
            unresolved.append(('nodecl', r['name']))
    v['report_names_match_source'] = names_ok
    v['every_report_names_a_declaration_at_src'] = decl_ok
    v['name_notes'] = unresolved
    axsets = sorted({tuple(r['axioms']) for r in e['reports']})
    v['axiom_sets'] = [list(a) for a in axsets]
    v['axioms_within_permitted'] = all(set(a) <= set(PERMITTED) for a in axsets)
    # hazards in the module's whole OIBridge import closure at the source commit
    cl = closure(SRC, mods_src, mod)
    v['import_closure_size_src'] = len(cl)
    hzc = {}
    for m in cl:
        for k, n in scan_src[m][2].items():
            if n:
                hzc.setdefault(k, []).append((m, n))
    v['closure_hazards_src'] = hzc
    # main: the same print lines and names, and the declarations still present
    if v['blob_main']:
        pm = [(ln, nm) for ln, nm, _ in scan_main[mod][0]]
        v['main_prints_identical'] = pm == [(ln, nm) for ln, nm, _ in prints]
        v['main_decls_present'] = all(r['name'] in decls_main for r in e['reports'])
    ok = (v['exists_src'] and v['in_gated_build_src'] and v['print_lines_match'] and v['count_match']
          and v['status'] == 'complete' and names_ok and decl_ok and v['axioms_within_permitted']
          and not hzc)
    v['static_ok'] = ok
    if record and not ok:
        fail(f'{path}: static check failed')
    return v


entries = {path: check_entry(path, m28[path]) for path in added}
report['ev28_entries'] = entries
# mutation controls on the entry check: each planted defect must turn static_ok false
import copy
mut = {}
base = 'OIBridge/PhaseSource.lean'
def mutated(f):
    e = copy.deepcopy(m28[base]); f(e); return check_entry(base, e, record=False)['static_ok']
mut['forbidden_axiom'] = not mutated(lambda e: e['reports'][0]['axioms'].append('Lean.ofReduceBool'))
mut['report_dropped'] = not mutated(lambda e: e['reports'].pop())
mut['line_shifted'] = not mutated(lambda e: e['reports'][0].__setitem__('line', e['reports'][0]['line'] + 1))
mut['name_changed'] = not mutated(lambda e: e['reports'][0].__setitem__('name', 'OIBridge.PhaseSource.nonexistent'))
mut['wrong_namespace'] = not mutated(lambda e: e['reports'][1].__setitem__('name', 'OIBridge.Other.permClass_onesFixing'))
mut['prints_count'] = not mutated(lambda e: e.__setitem__('prints', e['prints'] + 1))
mut['status'] = not mutated(lambda e: e.__setitem__('status', 'partial'))
mut['unmutated_passes'] = mutated(lambda e: None)
report['entry_mutation_controls'] = mut
if not all(mut.values()):
    fail(f'entry mutation control failed: {mut}')

# changed modules since the source commit: comment-only?
changed = git('diff', '--name-only', SRC, MAIN, '--', LM).split()
cm = {}
for p in changed:
    a, b = show(SRC, p), show(MAIN, p)
    if a is None:
        cm[p] = 'added'
    elif b is None:
        cm[p] = 'deleted'
    else:
        norm = lambda t: re.sub(r'\s+', ' ', strip_lean(t)).strip()
        cm[p] = 'comment-only' if norm(a) == norm(b) else 'code-changed'
report['lean_changes_src_to_main'] = cm
# reverse dependents: does any added module import (transitively) a code-changed module?
code_changed = {p[len(LM) + 1:-5].replace('/', '.') for p, k in cm.items() if k == 'code-changed'}
report['added_modules_depending_on_code_changes'] = {
    path: sorted(closure(SRC, mods_src, path[:-5].replace('/', '.')) & code_changed) for path in added}

# ---- OD-15 ---------------------------------------------------------------------------------------
od = {}
for mod, names in OD15.items():
    full = f'OIBridge.{mod}'
    prints, decls, hz = scan_main[full]
    for nm in names:
        fq = f'OIBridge.{mod}.{nm}'
        pl = [ln for ln, p, ns in prints if p.split('.')[-1] == nm]
        e = m28[f'OIBridge/{mod}.lean']
        er = [r for r in e['reports'] if r['name'] == fq]
        od[fq] = {
            'declared_on_main': fq in decls_main,
            'print_lines_on_main': pl,
            'module_in_gated_build_main': full in gated_main,
            'module_blob_src_eq_main': blob(SRC, f'{LM}/OIBridge/{mod}.lean') == blob(MAIN, f'{LM}/OIBridge/{mod}.lean'),
            'short_name_print_modules_main': sorted(short.get(nm, [])),
            'expected28_report': er,
            'closure_hazards_main': {k: n for m in closure(MAIN, mods_main, full)
                                     for k, n in scan_main[m][2].items() if n},
        }
        x = od[fq]
        if not (x['declared_on_main'] and len(pl) == 1 and x['module_in_gated_build_main']
                and len(er) == 1 and er[0]['axioms'] == PERMITTED and not x['closure_hazards_main']
                and x['short_name_print_modules_main'] == [full]):
            fail(f'OD-15 {fq} check failed')
report['od15'] = od

# ---- the fresh-build replay artifact (structured files only) ----------------------------------
if ART:
    a = {}
    sums = {}
    for line in open(os.path.join(ART, 'SHA256SUMS')):
        h, f = line.split(None, 1)
        sums[f.strip()] = h
    a['sha256sums_ok'] = all(hashlib.sha256(open(os.path.join(ART, f), 'rb').read()).hexdigest() == h
                             for f, h in sums.items())
    run = json.load(open(os.path.join(ART, 'run.json')))
    el = json.load(open(os.path.join(ART, 'elaboration.txt')))
    rep = json.load(open(os.path.join(ART, 'reproduced.json')))
    exp28_art = open(os.path.join(ART, 'expected-28.json'), 'rb').read()
    a['run'] = {k: run[k] for k in ('run_id', 'commit', 'workflow_sha', 'activity')}
    a['expected28_blob_in_artifact'] = hashlib.sha1(b'blob %d\0' % len(exp28_art) + exp28_art).hexdigest()
    a['exit'] = {f: open(os.path.join(ART, f)).read().strip() for f in ('build.exit', 'gate.exit')}
    a['elaboration'] = {k: el[k] for k in ('built', 'replayed', 'source_modules', 'governed', 'checks')}
    a['build_success'] = rep['build']['success']
    a['markers'] = rep['markers']
    a['gate_pass'] = rep['gate']['verdict']['pass']
    a['gate_lean_steps'] = {s_['name']: s_['status'] for s_ in rep['gate']['steps']
                            if s_['name'] in ('lean-axioms', 'lean-manuscript')}
    per = {}
    for path in added:
        got = [{k: r[k] for k in ('name', 'line', 'axioms')} for r in rep['reports'].get(path, [])]
        want = [{k: r[k] for k in ('name', 'line', 'axioms')} for r in m28[path]['reports']]
        per[path] = {'reproduced_reports': len(got), 'identical': sorted(got, key=lambda r: r['line'])
                     == sorted(want, key=lambda r: r['line'])}
        if not per[path]['identical']:
            fail(f'artifact: {path} reports differ')
    a['per_module'] = per
    ok = (a['sha256sums_ok'] and run['commit'] == SRC and a['expected28_blob_in_artifact']
          == '97a2377dbfc30987887dffea2b72e423feed079d' and a['exit'] == {'build.exit': '0', 'gate.exit': '0'}
          and el['replayed'] == 0 and all(el['checks'].values()) and a['build_success'] and a['gate_pass']
          and not any(rep['markers'].values()))
    a['ok'] = ok
    if not ok:
        fail('artifact checks failed')
    report['artifact'] = a

# ---- controls: the checks must catch planted defects ---------------------------------------------
ctrl = {}
t = 'namespace OIBridge\nnamespace X\ntheorem foo : True := trivial\nend X\nend OIBridge\n#print axioms OIBridge.X.foo\n'
ctrl['clean_scan'] = scan(t)[2] == {k: 0 for k in HAZARD} and scan(t)[1] == {'OIBridge.X.foo'}
ctrl['sorry_caught'] = scan(t.replace(':= trivial', ':= by sorry'))[2]['sorry'] == 1
ctrl['sorry_in_comment_ignored'] = scan(t + '-- sorry\n/- native_decide -/\n')[2]['sorry'] == 0
ctrl['axiom_decl_caught'] = scan(t + 'axiom bad : False\n')[2]['axiom_decl'] == 1
ctrl['native_decide_caught'] = scan(t.replace(':= trivial', ':= by native_decide'))[2]['native_decide'] == 1
ctrl['comment_only_equal'] = (re.sub(r'\s+', ' ', strip_lean(t + '/-- doc -/\n')).strip()
                              == re.sub(r'\s+', ' ', strip_lean(t)).strip())
ctrl['code_change_detected'] = strip_lean(t) != strip_lean(t.replace('True', 'False'))
report['controls'] = ctrl
if not all(ctrl.values()):
    fail(f'control failed: {ctrl}')

report['failures'] = fails
report['verdict'] = 'PASS' if not fails else 'FAIL'
print(json.dumps(report, indent=1, default=list))
sys.exit(1 if fails else 0)
