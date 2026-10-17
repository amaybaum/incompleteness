#!/usr/bin/env python3
"""extract_result.py -- reads the structured result of a Mathlib bridge build and release gate from its output.

The same extraction runs on a served GitHub job log (timestamped lines, possibly only the last lines of the
log) and on the output of a fresh `lake --rehash build` plus `tools/release_gate.py` at the same commit, so an
archived expected result and a reproduction are compared on equal terms. Standard library only.

    python3 -I extract_result.py LOG            # prints the extraction as JSON
    python3 -I extract_result.py --self-test    # needs git history: it reads three sources at BG-3's E

What is read:
  build      the "Build completed successfully (N jobs)." line, or its absence;
  gate       the release-gate block: each step's name, status and summary, and the verdict line;
  reports    every `#print axioms` report lake prints with its file:line:col: prefix, by module: source line,
             declaration name (primes included, as in `sum_comp'`), and its axiom list (null for "does not
             depend on any axioms");
  direct     the reports `lean FILE` prints without that prefix, one block per Actions step ("##[group]Run")
             that printed them: the step's lean commands as its script lines show them, each with the one .lean
             file it names (null when it names none or several), the reports in printed order, and the file
             they are attributed to. A block is attributed only when its step runs lean on exactly one file;
             otherwise its file is null and its gap says why, since the log does not delimit the outputs of
             several commands. Reports outside any step are a block with step_line null, unattributed;
  built      every "Built OIBridge…" line, with its seconds;
  cache      the Actions cache lines (hit, saved, restored, not found);
  markers    counts of the lines that would fail the axiom check: sorryAx, Lean.ofReduceBool,
             "declaration uses 'sorry'", and "error:".
A wrapped axiom list is joined over the continuation lines Lean prints (" name," and " name]"); a list whose
next line is anything else, or that the text ends inside, is marked unclosed and the next line is read afresh.
Each item carries the 1-based line of the text it was read from.

check(extraction, sources) is the fail-closed report check: sources names each file whose reports must be
complete -- a module as lake prints it, or a file as a lean command names it -- with its text, or None when it
is not there. It returns (failures, gaps), each a list of "code: detail" lines, and holds only when both are
empty. The codes:
  no-input           the text has no lines;
  no-files           no file was named;
  source-absent      a named file has no text;
  no-print-commands  a named file has no #print axioms command;
  mixed-forms        a named file has both prefixed and direct reports;
  missing-report     a #print axioms command has no report (by source line, or in order for direct reports);
  extra-report       a report has no #print axioms command;
  duplicate-report   a source line is reported more than once;
  name-mismatch      a report's declaration is not the command's target;
  truncated-report   an axiom list is unclosed (any report in the text);
  sorryAx            a report depends on sorryAx (any report in the text);
  unpermitted-axiom  a report depends on an axiom outside propext, Classical.choice and Quot.sound;
  failure-marker     a failure marker occurs in the text;
  unattributed       (a gap) direct reports whose file the log does not determine.
"""
import json
import os
import re
import subprocess
import sys

TS = re.compile(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ')
GATE_START = re.compile(r'^release gate$')
GATE_END = re.compile(r'^release gate: (.*)$')
GATE_STEP = re.compile(r'^  (PASS|FAIL|SKIP)  (\S+)\s*(.*)$')
BUILD_OK = re.compile(r'^Build completed successfully \((\d+) jobs\)\.')
REPORT = re.compile(r"^info: ((?:OIBridge/)?[A-Za-z0-9_/]+\.lean):(\d+):\d+: '(.+?)' (depends on axioms: \[(.*)|does not depend on any axioms)")
DIRECT = re.compile(r"^'(.+?)' (depends on axioms: \[(.*)|does not depend on any axioms)")
CONT = re.compile(r'^ +[^\s,\[\]]+(?:, [^\s,\[\]]+)*[,\]]$')
STEP = re.compile(r'^##\[group\]Run ')
SCRIPT = re.compile(r'^\x1b?\[36;1m(.*?)\x1b?\[0m$')
BUILT = re.compile(r'^\S* ?\[\d+/\d+\] Built (OIBridge(?:\.[A-Za-z0-9_]+)*) \(([\d.]+)s\)')
CACHE = re.compile(r'Cache (saved with key|hit occurred on the primary key|restored from key|not found for input keys)|Failed to (save|restore)')
MARKERS = {'sorryAx': re.compile(r'sorryAx'), 'Lean.ofReduceBool': re.compile(r'Lean\.ofReduceBool'),
           "declaration uses 'sorry'": re.compile(r"declaration uses .sorry."), 'error:': re.compile(r'error:')}
PERMITTED = ('propext', 'Classical.choice', 'Quot.sound')
PRINT = re.compile(r'^#print axioms\s+(\S+)')


def strip(line):
    return TS.sub('', line, count=1)


def axiom_list(lines, i, body):
    """The axiom list opened on line i with body, joined over continuation lines: (axioms, closed, last line)."""
    j = i
    while ']' not in body and j + 1 < len(lines) and CONT.match(lines[j + 1].rstrip()):
        j += 1
        body += ' ' + lines[j].strip()
    closed = ']' in body
    return [a.strip() for a in body.split(']')[0].split(',') if a.strip()], closed, j


def lean_files(script_line):
    """For each lean command on a script line, the one .lean file it names, or None."""
    out = []
    for seg in re.split(r'\|\|?|;|&&', script_line):
        toks = [t.strip('\'"') for t in seg.split()]
        if toks[:2] == ['lake', 'env']:
            toks = toks[2:]
        if toks and toks[0] == 'lean':
            files = [t for t in toks[1:] if t.endswith('.lean')]
            out.append(files[0] if len(files) == 1 else None)
    return out


def attribute(block):
    files = [c['file'] for c in block['commands']]
    if block['step_line'] is None:
        return None, 'no Actions step precedes these reports, so no command line names their file'
    if not files:
        return None, 'the step that printed these reports shows no lean command'
    if None in files:
        return None, 'a lean command of the step names no single .lean file'
    if len(set(files)) > 1:
        return None, ('the step runs lean on %d files (%s) and the log does not delimit their outputs'
                      % (len(set(files)), ', '.join(sorted(set(files)))))
    return files[0], None


def extract(text):
    raw = text.split('\n')
    if raw and raw[-1] == '':
        raw.pop()
    lines = [strip(l) for l in raw]
    out = {'lines': len(lines), 'build': None, 'gate': None, 'reports': {}, 'direct': [], 'built': [], 'cache': [],
           'markers': {k: 0 for k in MARKERS}}
    step, in_script, blocks = None, False, {}
    i = 0
    while i < len(lines):
        l = lines[i]
        n = i + 1
        if STEP.match(l):
            step, in_script = {'step_line': n, 'commands': []}, True
        elif in_script:
            s = SCRIPT.match(l)
            if s:
                step['commands'] += [{'file': f, 'served_line': n} for f in lean_files(s.group(1))]
            else:
                in_script = False
        m = BUILD_OK.match(l)
        if m:
            out['build'] = {'success': True, 'jobs': int(m.group(1)), 'line': n}
        m = REPORT.match(l)
        if m:
            mod, src_line, name, kind, axioms = m.group(1), int(m.group(2)), m.group(3), m.group(4), m.group(5)
            if kind.startswith('depends'):
                ax, closed, j = axiom_list(lines, i, axioms)
                rep = {'line': src_line, 'name': name, 'axioms': ax, 'served_line': n}
                if not closed:
                    rep['unclosed'] = True
                i = j
            else:
                rep = {'line': src_line, 'name': name, 'axioms': None, 'served_line': n}
            out['reports'].setdefault(mod, []).append(rep)
        m = DIRECT.match(l)
        if m:
            rep = {'name': m.group(1), 'axioms': None, 'served_line': n}
            if m.group(2).startswith('depends'):
                ax, closed, j = axiom_list(lines, i, m.group(3))
                rep['axioms'] = ax
                if not closed:
                    rep['unclosed'] = True
                i = j
            key = step['step_line'] if step else None
            if key not in blocks:
                blocks[key] = {'step_line': key, 'commands': list(step['commands']) if step else [], 'reports': []}
            blocks[key]['reports'].append(rep)
        m = BUILT.match(l)
        if m:
            out['built'].append({'module': m.group(1), 'seconds': float(m.group(2)), 'served_line': n})
        if CACHE.search(l):
            out['cache'].append({'text': l, 'served_line': n})
        for k, rx in MARKERS.items():
            if rx.search(l):
                out['markers'][k] += 1
        if GATE_START.match(l):
            steps, verdict, j = [], None, i + 1
            while j < len(lines):
                e = GATE_END.match(lines[j])
                if e:
                    verdict = {'text': e.group(1), 'pass': e.group(1).startswith('PASS'), 'served_line': j + 1}
                    break
                s = GATE_STEP.match(lines[j])
                if s:
                    steps.append({'status': s.group(1), 'name': s.group(2), 'summary': s.group(3).rstrip(), 'served_line': j + 1})
                j += 1
            out['gate'] = {'steps': steps, 'verdict': verdict, 'start_line': n}
            i = j
        i += 1
    for mod in out['reports']:
        out['reports'][mod].sort(key=lambda r: (r['line'], r['served_line']))
    for b in sorted(blocks.values(), key=lambda b: (b['step_line'] is not None, b['step_line'] or 0)):
        b['file'], b['gap'] = attribute(b)
        out['direct'].append(b)
    return out


def check(x, sources):
    """The fail-closed report check (module docstring). Returns (failures, gaps)."""
    fails, gaps = [], []
    F = fails.append
    if not x.get('lines'):
        F('no-input: the text has no lines')
    if not sources:
        F('no-files: no file was named, so no report is required')
    direct = x.get('direct', [])
    for key in sorted(sources):
        text = sources[key]
        if text is None:
            F('source-absent: %s' % key)
            continue
        prints = [(k + 1, m.group(1).lstrip('@')) for k, m in enumerate(PRINT.match(l) for l in text.split('\n')) if m]
        if not prints:
            F('no-print-commands: %s' % key)
            continue
        lake = x.get('reports', {}).get(key, [])
        seq = [r for b in direct if b.get('file') == key for r in b['reports']]
        if lake and seq:
            F('mixed-forms: %s has %d prefixed and %d direct report(s)' % (key, len(lake), len(seq)))
            continue
        pairs = []
        if seq:
            pairs = list(zip(prints, seq))
            for line, target in prints[len(seq):]:
                F('missing-report: %s:%d #print axioms %s' % (key, line, target))
            for r in seq[len(prints):]:
                F('extra-report: %s reports %s (served line %d) beyond its %d command(s)' % (key, r['name'], r['served_line'], len(prints)))
        else:
            at = {}
            for r in lake:
                at.setdefault(r['line'], []).append(r)
            for line, target in prints:
                got = at.pop(line, [])
                if not got:
                    F('missing-report: %s:%d #print axioms %s' % (key, line, target))
                elif len(got) > 1:
                    F('duplicate-report: %s:%d is reported %d times' % (key, line, len(got)))
                else:
                    pairs.append(((line, target), got[0]))
            for line in sorted(at):
                F('extra-report: %s:%d has no #print axioms command' % (key, line))
        for (line, target), r in pairs:
            t = target[len('_root_.'):] if target.startswith('_root_.') else target
            if r['name'] != t and not r['name'].endswith('.' + t):
                F('name-mismatch: %s:%d #print axioms %s is reported as %s' % (key, line, target, r['name']))
    every = [(m, r) for m, rs in sorted(x.get('reports', {}).items()) for r in rs] + \
            [(b.get('file') or 'step at line %s' % b['step_line'], r) for b in direct for r in b['reports']]
    for where, r in every:
        if r.get('unclosed'):
            F('truncated-report: %s %s (served line %d) has an unclosed axiom list' % (where, r['name'], r['served_line']))
        ax = r['axioms'] or []
        if 'sorryAx' in ax:
            F('sorryAx: %s %s depends on sorryAx' % (where, r['name']))
        bad = sorted(set(ax) - set(PERMITTED) - {'sorryAx'})
        if bad:
            F('unpermitted-axiom: %s %s depends on %s' % (where, r['name'], ', '.join(bad)))
    for k, c in sorted((x.get('markers') or {}).items()):
        if c:
            F('failure-marker: %d line(s) with %s' % (c, k))
    for b in direct:
        if not b.get('file'):
            gaps.append('unattributed: %d direct report(s) of the step at line %s: %s' % (len(b['reports']), b['step_line'], b['gap']))
    return fails, gaps


# ---------------------------------------------------------------------------------------------------- self-test
# Verbatim served lines of the two research builds of 2026-10-13, each with its line in the served job log:
# run 38450187534, job 115478781754, served text sha256 814d820bb2ea2cd8726979e7881b4bc5a6734ae286913960bb8aec2fcbdfab5f;
# run 38454439833, job 115493410133, served text sha256 b8fde0612483687da594460dde87c6f86115a5c5a8f68b0d4ca0ad75491caf14.
# They are test inputs, not evidence: a subsequence of lines keeps each line's shape, which is all the extractor reads.
RUN_A = [
    '2026-10-13T18:52:38.8564169Z ##[group]Run lake exe cache get',  # 572
    '2026-10-13T18:52:38.8564500Z \x1b[36;1mlake exe cache get\x1b[0m',  # 573
    '2026-10-13T18:52:38.8564852Z \x1b[36;1mlake --rehash build OIBridge.ImplementationLocality\x1b[0m',  # 574
    '2026-10-13T18:52:38.8565484Z \x1b[36;1mlake env lean ../programmes/oi-qm/reconstruction/preservation-induction-design/PreservationInduction.lean\x1b[0m',  # 575
    '2026-10-13T18:52:38.8630063Z shell: /usr/bin/bash -e {0}',  # 576
    "2026-10-13T18:55:00.4858887Z info: OIBridge/ImplementationLocality.lean:1102:0: 'OIBridge.InterventionLocality.sum_comp'' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3078
    "2026-10-13T18:55:00.4859768Z info: OIBridge/ImplementationLocality.lean:1103:0: 'OIBridge.InterventionLocality.comp_sum'' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3079
    "2026-10-13T18:55:00.4947033Z info: OIBridge/ImplementationLocality.lean:1158:0: 'OIBridge.InterventionLocality.implementationLocality_independent' depends on axioms: [propext,",  # 3152
    '2026-10-13T18:55:00.4947123Z  Classical.choice,',  # 3153
    '2026-10-13T18:55:00.4947209Z  Quot.sound]',  # 3154
    "2026-10-13T18:55:00.4947777Z info: OIBridge/ImplementationLocality.lean:1159:0: 'OIBridge.InterventionLocality.oiPlusEmbedded_of_oiPlusLocal' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3155
    '2026-10-13T18:55:00.4970644Z Build completed successfully (3114 jobs).',  # 3163
    "2026-10-13T18:55:03.2336782Z 'OIBridge.PreservationInductionDesign.instAvail_preserves' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3164
    "2026-10-13T18:55:03.2337639Z 'OIBridge.PreservationInductionDesign.instAvail_sum_preserves' depends on axioms: [propext,",  # 3165
    '2026-10-13T18:55:03.2338135Z  Classical.choice,',  # 3166
    '2026-10-13T18:55:03.2338571Z  Quot.sound]',  # 3167
    "2026-10-13T18:55:03.2339333Z 'OIBridge.PreservationInductionDesign.instAvail_spectator_preserves' depends on axioms: [propext,",  # 3168
    '2026-10-13T18:55:03.2340249Z  Classical.choice,',  # 3169
    '2026-10-13T18:55:03.2340614Z  Quot.sound]',  # 3170
    "2026-10-13T18:55:03.2341362Z 'OIBridge.PreservationInductionDesign.instAvail_transport_preserves' depends on axioms: [propext,",  # 3171
    '2026-10-13T18:55:03.2342507Z  Classical.choice,',  # 3172
    '2026-10-13T18:55:03.2342862Z  Quot.sound]',  # 3173
    '2026-10-13T18:55:03.3694200Z ##[group]Run revision=$(git rev-parse HEAD)',  # 3174
]
RUN_B = [
    '2026-10-13T19:24:02.6255597Z ##[group]Run lake exe cache get',  # 573
    '2026-10-13T19:24:02.6255933Z \x1b[36;1mlake exe cache get\x1b[0m',  # 574
    '2026-10-13T19:24:02.6256366Z \x1b[36;1mlake --rehash build OIBridge.ImplementationLocality OIBridge.StructuralClosure\x1b[0m',  # 575
    '2026-10-13T19:24:02.6256828Z \x1b[36;1mmkdir -p ResearchDesign\x1b[0m',  # 576
    '2026-10-13T19:24:02.6257493Z \x1b[36;1mcp ../programmes/oi-qm/reconstruction/preservation-induction-design/PreservationInduction.lean ResearchDesign/PreservationInduction.lean\x1b[0m',  # 577
    '2026-10-13T19:24:02.6258485Z \x1b[36;1mcp ../programmes/oi-qm/reconstruction/preservation-induction-design/ResearchInstances.lean ResearchDesign/ResearchInstances.lean\x1b[0m',  # 578
    "2026-10-13T19:24:02.6259120Z \x1b[36;1mlake env bash -c '\x1b[0m",  # 579
    '2026-10-13T19:24:02.6259363Z \x1b[36;1m  set -e\x1b[0m',  # 580
    '2026-10-13T19:24:02.6259622Z \x1b[36;1m  export LEAN_PATH="$LEAN_PATH:$PWD"\x1b[0m',  # 581
    '2026-10-13T19:24:02.6260383Z \x1b[36;1m  lean -o ResearchDesign/PreservationInduction.olean ResearchDesign/PreservationInduction.lean\x1b[0m',  # 582
    '2026-10-13T19:24:02.6260962Z \x1b[36;1m  lean ResearchDesign/ResearchInstances.lean\x1b[0m',  # 583
    "2026-10-13T19:24:02.6261291Z \x1b[36;1m'\x1b[0m",  # 584
    '2026-10-13T19:24:02.6330765Z shell: /usr/bin/bash -e {0}',  # 585
    '2026-10-13T19:25:48.1009848Z Build completed successfully (3121 jobs).',  # 3591
    "2026-10-13T19:25:51.2556153Z 'OIBridge.PreservationInductionDesign.instAvail_preserves' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3592
    "2026-10-13T19:25:51.2557196Z 'OIBridge.PreservationInductionDesign.instAvail_sum_preserves' depends on axioms: [propext,",  # 3593
    '2026-10-13T19:25:51.2557699Z  Classical.choice,',  # 3594
    '2026-10-13T19:25:51.2557925Z  Quot.sound]',  # 3595
    "2026-10-13T19:25:51.2558373Z 'OIBridge.PreservationInductionDesign.instAvail_spectator_preserves' depends on axioms: [propext,",  # 3596
    '2026-10-13T19:25:51.2558874Z  Classical.choice,',  # 3597
    '2026-10-13T19:25:51.2559086Z  Quot.sound]',  # 3598
    "2026-10-13T19:25:51.2559500Z 'OIBridge.PreservationInductionDesign.instAvail_transport_preserves' depends on axioms: [propext,",  # 3599
    '2026-10-13T19:25:51.2560271Z  Classical.choice,',  # 3600
    '2026-10-13T19:25:51.2560486Z  Quot.sound]',  # 3601
    "2026-10-13T19:25:53.7856393Z 'OIBridge.PreservationInductionDesign.quantum_instAvail' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3602
    "2026-10-13T19:25:53.7857357Z 'OIBridge.PreservationInductionDesign.classical_instAvail' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3603
    "2026-10-13T19:25:53.7858228Z 'OIBridge.PreservationInductionDesign.quantum_attach' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3604
    "2026-10-13T19:25:53.7859015Z 'OIBridge.PreservationInductionDesign.quantum_discard' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3605
    "2026-10-13T19:25:53.7860101Z 'OIBridge.PreservationInductionDesign.classical_readProj' depends on axioms: [propext, Classical.choice, Quot.sound]",  # 3606
    "2026-10-13T19:25:53.7860876Z 'OIBridge.PreservationInductionDesign.classical_native_readout' depends on axioms: [propext,",  # 3607
    '2026-10-13T19:25:53.7861362Z  Classical.choice,',  # 3608
    '2026-10-13T19:25:53.7861583Z  Quot.sound]',  # 3609
    '2026-10-13T19:25:53.9249083Z ##[group]Run revision=$(git rev-parse HEAD)',  # 3610
]
# The design file's #print axioms commands at the run's source e684897d (blob 952ef0b5), at their own lines.
DESIGN_A = '../programmes/oi-qm/reconstruction/preservation-induction-design/PreservationInduction.lean'
DESIGN_A_SRC = '\n'.join({9: 'namespace OIBridge.PreservationInductionDesign', 114: '#print axioms instAvail_preserves',
                          115: '#print axioms instAvail_sum_preserves', 116: '#print axioms instAvail_spectator_preserves',
                          117: '#print axioms instAvail_transport_preserves', 119: 'end OIBridge.PreservationInductionDesign'}
                         .get(k, '') for k in range(1, 120)) + '\n'
# BG-3's E (on main): its bridge tail and design-run log are retained in bg3/, and its sources are read from git.
BG3_E = '194eb3fd0c0a58ee843a574d93d4a0fa94f6cb79'
BG3_TAILS = ('116826161407', '116805436638', '116761232088')
SCOPE = 'OIBridge/TurnpikeScopeTransfer.lean'
BG2 = '../programmes/oi-qm/reconstruction/bekir-golomb-orientation-design/'


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.normpath(os.path.join(here, '..', '..', '..'))
    ok = True

    def read(rel):
        return open(os.path.join(here, rel), encoding='utf-8').read()

    def at_e(path):
        p = subprocess.run(['git', '-C', root, 'show', '%s:%s' % (BG3_E, path)], capture_output=True)
        return p.stdout.decode('utf-8') if p.returncode == 0 else None

    def codes(res):
        return sorted({f.split(':', 1)[0] for f in res[0] + res[1]})

    def case(name, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print('%s self: %s' % ('PASS' if good else 'FAIL', name))
        if not good:
            print('      got %r, want %r' % (got, want))

    def edit(lines, fn):
        ls = list(lines)
        fn(ls)
        return '\n'.join(ls)

    def sub(ls, k, old, new):
        assert old in ls[k], (k, old)
        ls[k] = ls[k].replace(old, new)

    # the prefixed format: BG-3's three retained bridge tails reproduce their archived expected results
    for job in BG3_TAILS:
        x = extract(read('bg3/bridge-%s-tail.log' % job))
        res = json.loads(read('bg3/results-%s.json' % job))
        mods = res['expected']['modules']
        got = {'modules': {m: [{'line': r['line'], 'name': r['name'], 'axioms': r['axioms']} for r in x['reports'].get(m, [])] for m in mods},
               'markers': x['markers'], 'reports_in_served_text': sum(len(v) for v in x['reports'].values()),
               'report_served_lines': {m: {r['name']: r['served_line'] for r in x['reports'].get(m, [])} for m in mods},
               'verdict': x['gate']['verdict']['text'] if x['gate'] and x['gate']['verdict'] else None, 'direct': x['direct']}
        want = {'modules': {m: em['reports'] for m, em in mods.items()}, 'markers': res['expected']['markers'],
                'reports_in_served_text': res['observed']['reports_in_served_text'],
                'report_served_lines': res['observed']['report_served_lines'], 'verdict': res['expected']['gate']['verdict'],
                'direct': []}
        case('bridge tail %s reproduces bg3/results-%s.json' % (job, job), got, want)
    tail = read('bg3/bridge-116826161407-tail.log').split('\n')
    scope_src = at_e('verification/lean-mathlib/' + SCOPE)
    if scope_src is None:
        print('FAIL self: git history with %s is needed' % BG3_E[:12])
        return 1
    k_rep = next(k for k, l in enumerate(tail) if "info: %s:" % SCOPE in l and l.endswith(']'))
    # a one-line report followed by another report: cut to its first line, it must not swallow the next one
    k_two = next(k for k in range(k_rep + 1, len(tail) - 1) if "info: %s:" % SCOPE in tail[k] and tail[k].endswith(']')
                 and "info: %s:" % SCOPE in tail[k + 1])
    case('E tail: the governed module holds against its source at E', codes(check(extract('\n'.join(tail)), {SCOPE: scope_src})), [])
    case('E tail, a report line removed: missing report', codes(check(extract(edit(tail, lambda ls: ls.pop(k_rep))), {SCOPE: scope_src})),
         ['missing-report'])
    case('E tail, a report line repeated: duplicate report',
         codes(check(extract(edit(tail, lambda ls: ls.insert(k_rep, ls[k_rep]))), {SCOPE: scope_src})), ['duplicate-report'])
    case('E tail, a report at a line with no command: extra report',
         codes(check(extract(edit(tail, lambda ls: ls.insert(k_rep, re.sub(r'\.lean:\d+:', '.lean:1:', ls[k_rep])))), {SCOPE: scope_src})),
         ['extra-report'])
    case('E tail, a declaration renamed at its own line: name mismatch',
         codes(check(extract(edit(tail, lambda ls: sub(ls, k_rep, "' depends", "_renamed' depends"))), {SCOPE: scope_src})),
         ['name-mismatch'])
    case('E tail, an axiom outside the permitted three', codes(check(extract(edit(tail, lambda ls: sub(ls, k_rep, 'propext', 'OIBridge.extraAxiom'))),
                                                                 {SCOPE: scope_src})), ['unpermitted-axiom'])
    case('E tail, a report on sorryAx', codes(check(extract(edit(tail, lambda ls: sub(ls, k_rep, 'propext', 'sorryAx'))), {SCOPE: scope_src})),
         ['failure-marker', 'sorryAx'])
    case('E tail, an error line: failure marker', codes(check(extract(edit(tail, lambda ls: ls.append('error: x'))), {SCOPE: scope_src})),
         ['failure-marker'])
    case('E tail, the governed module absent from the source', codes(check(extract('\n'.join(tail)), {SCOPE: None})), ['source-absent'])
    case('E tail, a source with no #print axioms', codes(check(extract('\n'.join(tail)), {SCOPE: '-- no commands\n'})), ['no-print-commands'])
    case('E tail, no file named', codes(check(extract('\n'.join(tail)), {})), ['no-files'])
    case('an empty text', codes(check(extract(''), {SCOPE: scope_src})), ['missing-report', 'no-input'])
    case('E tail, the second report cut to its first line: truncated, and the next report still read',
         (codes(check(extract(edit(tail, lambda ls: sub(ls, k_two, ls[k_two][ls[k_two].index('[') + 1:], 'propext,'))), {SCOPE: scope_src})),
          len(extract(edit(tail, lambda ls: sub(ls, k_two, ls[k_two][ls[k_two].index('[') + 1:], 'propext,')))['reports'][SCOPE])),
         (['truncated-report'], len(extract('\n'.join(tail))['reports'][SCOPE])))

    # the direct format, retained: BG-3's design-run log, two steps each running lean on one file
    dlog = read('bg3/design-116831668411.log')
    xd = extract(dlog)
    srcs = {BG2 + f: at_e('verification/programmes/oi-qm/reconstruction/bekir-golomb-orientation-design/' + f)
            for f in ('OrientationDesign.lean', 'SignedRepairDesign.lean')}
    case('design log: two blocks, attributed to their files, 7 and 3 reports, wrapped lists joined',
         [(b['file'], len(b['reports']), b['reports'][0]['axioms']) for b in xd['direct']],
         [(BG2 + 'OrientationDesign.lean', 7, list(PERMITTED)), (BG2 + 'SignedRepairDesign.lean', 3, list(PERMITTED))])
    case('design log: both files hold against their sources at E', codes(check(xd, srcs)), [])
    signed = 'lake env lean ' + BG2 + 'SignedRepairDesign.lean'
    for name, new, gap in (('a lean command naming no file', 'lake env lean "$f"', 'a lean command of the step names no single .lean file'),
                           ('a lean command naming two files', signed + ' ' + BG2 + 'OrientationDesign.lean',
                            'a lean command of the step names no single .lean file'),
                           ('no lean command', 'lake env bash run.sh', 'the step that printed these reports shows no lean command')):
        xg = extract(dlog.replace(signed, new))
        case('design log, the second step with %s: unattributed' % name, (codes(check(xg, srcs)), [b['gap'] for b in xg['direct']]),
             (['missing-report', 'unattributed'], [None, gap]))

    # the direct format, run 38450187534: one lean command, primed prefixed names, wrapped lists
    xa = extract('\n'.join(RUN_A))
    case('run 38450187534: primed names read with their module, line and axioms',
         [(r['line'], r['name'], r['axioms']) for r in xa['reports']['OIBridge/ImplementationLocality.lean'][:2]],
         [(1102, "OIBridge.InterventionLocality.sum_comp'", list(PERMITTED)), (1103, "OIBridge.InterventionLocality.comp_sum'", list(PERMITTED))])
    case('run 38450187534: a wrapped prefixed list joined', xa['reports']['OIBridge/ImplementationLocality.lean'][2]['axioms'], list(PERMITTED))
    case('run 38450187534: the 4 design reports, attributed to the step\'s one file, with their axioms',
         [(b['step_line'], b['file'], b['gap'], [(r['name'].rsplit('.', 1)[1], r['axioms'], r['served_line']) for r in b['reports']]) for b in xa['direct']],
         [(1, DESIGN_A, None, [('instAvail_preserves', list(PERMITTED), 13), ('instAvail_sum_preserves', list(PERMITTED), 14),
                               ('instAvail_spectator_preserves', list(PERMITTED), 17), ('instAvail_transport_preserves', list(PERMITTED), 20)])])
    case('run 38450187534: the design file holds against its commands', codes(check(xa, {DESIGN_A: DESIGN_A_SRC})), [])
    k_one = next(k for k, l in enumerate(RUN_A) if 'instAvail_preserves' in l)
    k_last = next(k for k, l in enumerate(RUN_A) if 'instAvail_transport_preserves' in l)
    case('run 38450187534, the last design report removed with its wrapped lines: missing report',
         codes(check(extract(edit(RUN_A, lambda ls: ls.__delitem__(slice(k_last, k_last + 3)))), {DESIGN_A: DESIGN_A_SRC})), ['missing-report'])
    case('run 38450187534, the first design report removed: missing report, and the rest out of step',
         codes(check(extract(edit(RUN_A, lambda ls: ls.pop(k_one))), {DESIGN_A: DESIGN_A_SRC})), ['missing-report', 'name-mismatch'])
    case('run 38450187534, a design report repeated: extra report',
         codes(check(extract(edit(RUN_A, lambda ls: ls.insert(k_last + 3, ls[k_one]))), {DESIGN_A: DESIGN_A_SRC})), ['extra-report'])
    case('run 38450187534, the tail cut inside the last wrapped list: truncated',
         codes(check(extract('\n'.join(RUN_A[:k_last + 2])), {DESIGN_A: DESIGN_A_SRC})), ['truncated-report'])
    case('run 38450187534, the tail cut after the last report\'s first line: truncated',
         codes(check(extract('\n'.join(RUN_A[:k_last + 1])), {DESIGN_A: DESIGN_A_SRC})), ['truncated-report'])
    case('run 38450187534, a design report on an unpermitted axiom',
         codes(check(extract(edit(RUN_A, lambda ls: sub(ls, k_last + 2, 'Quot.sound', 'OIBridge.extraAxiom'))), {DESIGN_A: DESIGN_A_SRC})),
         ['unpermitted-axiom'])
    case('run 38450187534, a design report on sorryAx',
         codes(check(extract(edit(RUN_A, lambda ls: sub(ls, k_one, 'Quot.sound', 'sorryAx'))), {DESIGN_A: DESIGN_A_SRC})),
         ['failure-marker', 'sorryAx'])
    case('run 38450187534, a primed prefixed report on sorryAx',
         codes(check(extract(edit(RUN_A, lambda ls: sub(ls, 5, 'Quot.sound', 'sorryAx'))), {DESIGN_A: DESIGN_A_SRC})),
         ['failure-marker', 'sorryAx'])
    case('run 38450187534, a design report renamed: name mismatch',
         codes(check(extract(edit(RUN_A, lambda ls: sub(ls, k_one, "_preserves'", "_kept'"))), {DESIGN_A: DESIGN_A_SRC})), ['name-mismatch'])
    xn = extract('\n'.join(RUN_A[k_one:k_last + 3]))
    case('run 38450187534, the design reports without their step: unattributed',
         (codes(check(xn, {DESIGN_A: DESIGN_A_SRC})), [b['gap'] for b in xn['direct']]),
         (['missing-report', 'unattributed'], ['no Actions step precedes these reports, so no command line names their file']))
    case('run 38450187534, lean run directly on a module lake also reports: mixed forms',
         codes(check(extract(edit(RUN_A, lambda ls: sub(ls, 3, DESIGN_A, 'OIBridge/ImplementationLocality.lean'))),
                     {'OIBridge/ImplementationLocality.lean': DESIGN_A_SRC})), ['mixed-forms'])

    # the direct format, run 38454439833: two lean commands in one step, so the log does not attribute the reports
    xb = extract('\n'.join(RUN_B))
    case('run 38454439833: all 10 design reports read with their axioms',
         [(r['name'].rsplit('.', 1)[1], r['axioms']) for b in xb['direct'] for r in b['reports']],
         [(n, list(PERMITTED)) for n in ('instAvail_preserves', 'instAvail_sum_preserves', 'instAvail_spectator_preserves',
                                         'instAvail_transport_preserves', 'quantum_instAvail', 'classical_instAvail', 'quantum_attach',
                                         'quantum_discard', 'classical_readProj', 'classical_native_readout')])
    case('run 38454439833: both lean commands read, the block unattributed',
         [([c['file'] for c in b['commands']], b['file'], b['gap']) for b in xb['direct']],
         [(['ResearchDesign/PreservationInduction.lean', 'ResearchDesign/ResearchInstances.lean'], None,
           'the step runs lean on 2 files (ResearchDesign/PreservationInduction.lean, ResearchDesign/ResearchInstances.lean) '
           'and the log does not delimit their outputs')])
    case('run 38454439833: the check records the gap', codes(check(xb, {DESIGN_A: DESIGN_A_SRC})), ['missing-report', 'unattributed'])
    print('extractor self-test: %s' % ('OK' if ok else 'FAILED'))
    return 0 if ok else 1


if __name__ == '__main__':
    if sys.argv[1:] == ['--self-test']:
        sys.exit(self_test())
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    print(json.dumps(extract(open(sys.argv[1], encoding='utf-8', errors='replace').read()), indent=1, sort_keys=True))
