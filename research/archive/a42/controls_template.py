#!/usr/bin/env python3
"""controls.py -- act 42's own contracts, FROZEN with the preregistration beside it.

Imports nothing from the repository and changes nothing. Reads D and the commit under check through git, and embeds
every frozen text it compares against: the blobs of the probe and of every tool, the workflow edit, the roadmap
propagation, the outcome sentence, the clause and the per-part summary lines.

  controls.py check <commit> [--freeze F]   the execution at <commit> against D (and, with F, the preregistration
                                            unchanged from F and F = D plus the preregistration alone)
  controls.py --self-test                   constants against the preregistration beside this file; the synthetic
                                            execution that must hold; mutation controls that must fail with their
                                            named codes
"""
import hashlib, os, re, subprocess, sys

D = @D@
RDIR = @RDIR@
PROBE = @PROBE@
PROBE_BLOB = @PROBE_BLOB@
TOOLS = @TOOLS@
TOOL_BLOBS = @TOOL_BLOBS@
WORKFLOW = @WORKFLOW@
ROADMAP = @ROADMAP@
LABEL = @LABEL@
WORKFLOW_EDITS = @WORKFLOW_EDITS@
ROADMAP_EDITS = @ROADMAP_EDITS@
SENTENCE = @SENTENCE@
CLAUSE = @CLAUSE@
CLAUSE_MENTION = @CLAUSE_MENTION@
PART_CHECKS = @PART_CHECKS@
SYNTHETIC = b'# synthetic file for the self-test\n'


def blob(data):
    return hashlib.sha1(b'blob %d\0' % len(data) + data).hexdigest()


def replaced(text, edits):
    for old, new, count in edits:
        if text.count(old) != count:
            raise ValueError('anchor count')
        text = text.replace(old, new)
    return text


def expected(d_files, path):
    text = d_files[path].decode()
    if path == WORKFLOW:
        return replaced(text, [(o, n, 1) for o, n in WORKFLOW_EDITS]).encode()
    return replaced(text, ROADMAP_EDITS).encode()


def ok_line(part):
    return 'dita_support_minimality_probe %s: OK -- %d checks' % (part, PART_CHECKS[part])


# ---- the checks -------------------------------------------------------------------------------------------------
def check_note(note, probe_blob=PROBE_BLOB):
    codes = []
    lines = note.split('\n')
    if [l for l in lines if l.startswith('**Outcome:**')] != ['**Outcome:** `%s`' % LABEL]:
        codes.append('note:outcome-line')
    if note.count(SENTENCE) != 1:
        codes.append('note:sentence')
    if note.count(CLAUSE_MENTION) != 1 or note.count(CLAUSE) != 1 or note.index(CLAUSE) < note.index(CLAUSE_MENTION):
        codes.append('note:clause')
    for part in PART_CHECKS:
        pre = ok_line(part)
        if sum(1 for l in lines if l.strip().strip('`') == pre or l.strip().strip('`').startswith(pre + ' (')) != 1:
            codes.append('note:part:' + part)
    if 'dita_support_minimality_probe' in note and ': FAILED' in note:
        codes.append('note:failed')
    if '`%s`' % probe_blob not in note:
        codes.append('note:blobs')
    return codes


def check_tree(d_files, e_files, e_tools, changed, probe_blob=PROBE_BLOB, tool_blobs=TOOL_BLOBS):
    """d_files/e_files: path -> bytes (None if absent); e_tools: {file name: blob} under TOOLS at the commit;
    changed: {path: 'A'|'M'|'D'} from D."""
    codes = []
    note = e_files.get(RDIR + 'result.md')
    if note is None:
        return ['note:absent']
    codes += check_note(note.decode(), probe_blob)
    if e_files.get(PROBE) is None or blob(e_files[PROBE]) != probe_blob:
        codes.append('probe:blob')
    if set(e_tools) != set(tool_blobs):
        codes.append('tools:set')
    for f in sorted(set(e_tools) & set(tool_blobs)):
        if e_tools[f] != tool_blobs[f]:
            codes.append('tools:blob:' + f)
    for path in (WORKFLOW, ROADMAP):
        try:
            exp = expected(d_files, path)
        except ValueError:
            exp = None
        if e_files.get(path) != exp:
            codes.append('surface:' + path)
    want = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A', PROBE: 'A',
            WORKFLOW: 'M', ROADMAP: 'M'}
    for f in tool_blobs:
        want[TOOLS + f] = 'A'
    if changed != want:
        codes.append('paths')
    return codes


# ---- git access -------------------------------------------------------------------------------------------------
def git(*args):
    return subprocess.run(('git',) + args, capture_output=True, check=True).stdout


def show(commit, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (commit, path)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def consulted():
    return [RDIR + 'result.md', RDIR + 'preregistration.md', PROBE, WORKFLOW, ROADMAP]


def tools_at(commit):
    out = {}
    for line in git('ls-tree', '-r', commit, '--', TOOLS).decode().splitlines():
        meta, path = line.split('\t', 1)
        out[path[len(TOOLS):]] = meta.split()[2]
    return out


def cmd_check(commit, freeze=None):
    d_files = {p: show(D, p) for p in consulted()}
    e_files = {p: show(commit, p) for p in consulted()}
    changed = {}
    for line in git('diff', '--no-renames', '--name-status', D, commit).decode().splitlines():
        st, path = line.split('\t', 1)
        changed[path] = st
    codes = check_tree(d_files, e_files, tools_at(commit), changed)
    if freeze:
        if git('diff', '--no-renames', '--name-status', D, freeze).decode().split() != ['A', RDIR + 'preregistration.md']:
            codes.append('freeze:delta')
        if show(freeze, RDIR + 'preregistration.md') != e_files[RDIR + 'preregistration.md']:
            codes.append('freeze:preregistration')
    if codes:
        print('controls: check FAILED: ' + '; '.join(codes))
        return 1
    print('controls: check OK')
    return 0


# ---- self-test --------------------------------------------------------------------------------------------------
def synthetic_row(d_files):
    e = dict(d_files)
    e[PROBE] = SYNTHETIC
    e[WORKFLOW] = expected(d_files, WORKFLOW)
    e[ROADMAP] = expected(d_files, ROADMAP)
    e[RDIR + 'preregistration.md'] = b'frozen'
    note = ['# result', '', '**Outcome:** `%s`' % LABEL, '', SENTENCE, '', CLAUSE_MENTION, '', CLAUSE, '',
            'probe `%s`' % blob(SYNTHETIC), '']
    note += ['`%s (1s)`' % ok_line(p) for p in PART_CHECKS]
    e[RDIR + 'result.md'] = '\n'.join(note).encode()
    tools = {f: blob(SYNTHETIC + f.encode()) for f in TOOL_BLOBS}
    changed = {RDIR + 'preregistration.md': 'A', RDIR + 'controls.py': 'A', RDIR + 'result.md': 'A', PROBE: 'A',
               WORKFLOW: 'M', ROADMAP: 'M'}
    for f in TOOL_BLOBS:
        changed[TOOLS + f] = 'A'
    return e, tools, changed


def self_test():
    here = os.path.dirname(os.path.abspath(__file__))
    prereg = open(os.path.join(here, 'preregistration.md'), encoding='utf-8').read()
    bad = []
    for name, text in (('sentence', SENTENCE), ('clause', CLAUSE)):
        if text not in prereg:
            bad.append('prereg:' + name)
    for old, new, count in ROADMAP_EDITS:
        if new.strip() not in prereg:
            bad.append('prereg:roadmap-edit')
    for f, b in sorted(TOOL_BLOBS.items()):
        if '`%s`' % b not in prereg:
            bad.append('prereg:tool-blob:' + f)
    if '`%s`' % PROBE_BLOB not in prereg:
        bad.append('prereg:probe-blob')
    for part in PART_CHECKS:
        if ok_line(part) not in prereg:
            bad.append('prereg:part:' + part)
    if bad:
        print('controls: self-test FAILED (constants): ' + '; '.join(bad))
        return 1
    print('controls: the frozen constants match the preregistration beside this file')

    d_files = {p: show(D, p) for p in consulted()}
    syn_tools = synthetic_row(d_files)[1]
    e, tools, ch = synthetic_row(d_files)
    codes = check_tree(d_files, e, tools, ch, probe_blob=blob(SYNTHETIC), tool_blobs=syn_tools)
    if codes:
        print('controls: self-test FAILED: the synthetic execution: %s' % codes)
        return 1
    print('controls: the synthetic execution holds as frozen')

    muts = []

    def mut(name, code, fn):
        muts.append((name, code, fn))

    def edit(path, old, new):
        def f(e, t, ch):
            e[path] = e[path].replace(old.encode(), new.encode(), 1)
        return f
    first_tool = sorted(TOOL_BLOBS)[0]
    part0, partx = list(PART_CHECKS)[0], list(PART_CHECKS)[-1]
    mut('a tool changed', 'tools:blob:' + first_tool, lambda e, t, ch: t.__setitem__(first_tool, '0' * 40))
    mut('an extra tool', 'tools:set', lambda e, t, ch: t.__setitem__('extra.py', '0' * 40))
    mut('a tool missing', 'tools:set', lambda e, t, ch: t.pop(first_tool))
    mut('the probe changed', 'probe:blob', lambda e, t, ch: e.__setitem__(PROBE, b'# not the frozen probe\n'))
    mut('the workflow edited beyond the frozen edit', 'surface:' + WORKFLOW,
        lambda e, t, ch: e.__setitem__(WORKFLOW, e[WORKFLOW] + b'# extra\n'))
    mut('the dispatch-only condition dropped', 'surface:' + WORKFLOW,
        edit(WORKFLOW, "    if: ${{ github.event_name == 'workflow_dispatch' }}\n", ''))
    mut('the workflow left as at D', 'surface:' + WORKFLOW, lambda e, t, ch: e.__setitem__(WORKFLOW, d_files[WORKFLOW]))
    mut('the roadmap sentence altered', 'surface:' + ROADMAP, edit(ROADMAP, 'is exactly 40, attained', 'is 40, attained'))
    mut('the roadmap left as at D', 'surface:' + ROADMAP, lambda e, t, ch: e.__setitem__(ROADMAP, d_files[ROADMAP]))
    mut('one support-48 clause left standing', 'surface:' + ROADMAP,
        edit(ROADMAP, 'The census of exponent matrices with entries in `{0, 1}` stays open,',
             'The census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open,'))
    mut('an extra path changed', 'paths', lambda e, t, ch: ch.__setitem__('papers/Main.md', 'M'))
    mut('a governed path missing', 'paths', lambda e, t, ch: ch.pop(WORKFLOW))
    mut('two outcome lines', 'note:outcome-line',
        lambda e, t, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'] + b'\n**Outcome:** `A42-OTHER`\n'))
    mut('the sentence missing', 'note:sentence', edit(RDIR + 'result.md', SENTENCE, ''))
    mut('the sentence strengthened', 'note:sentence',
        edit(RDIR + 'result.md', 'SAT verdicts (UNSAT) carried without proof logs', 'SAT verdicts (UNSAT)'))
    mut('the clause missing', 'note:clause', edit(RDIR + 'result.md', CLAUSE, ''))
    mut('the clause before its mention', 'note:clause',
        lambda e, t, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md'].replace(CLAUSE.encode(), b'', 1)
                                       .replace(CLAUSE_MENTION.encode(), (CLAUSE + '\n\n' + CLAUSE_MENTION).encode(), 1)))
    mut('a part line missing', 'note:part:' + partx, edit(RDIR + 'result.md', ok_line(partx), 'absent'))
    mut('a part line with another count', 'note:part:' + part0,
        edit(RDIR + 'result.md', ok_line(part0), ok_line(part0).replace('OK -- %d' % PART_CHECKS[part0],
                                                                        'OK -- %d' % (PART_CHECKS[part0] + 1))))
    mut('a failed part reported', 'note:failed',
        lambda e, t, ch: e.__setitem__(RDIR + 'result.md', e[RDIR + 'result.md']
                                       + b'\ndita_support_minimality_probe dfs:0: FAILED (1 of 4 checks)\n'))
    mut('the probe blob missing', 'note:blobs', edit(RDIR + 'result.md', blob(SYNTHETIC), 'x'))
    mut('no result note', 'note:absent', lambda e, t, ch: e.__setitem__(RDIR + 'result.md', None))
    failed = 0
    for name, code, fn in muts:
        e, t, ch = synthetic_row(d_files)
        fn(e, t, ch)
        got = check_tree(d_files, e, t, ch, probe_blob=blob(SYNTHETIC), tool_blobs=syn_tools)
        if code not in got:
            print('controls: self-test FAILED: mutation "%s" did not fail with %s (got %s)' % (name, code, got))
            failed += 1
    if failed:
        return 1
    print('controls: %d mutation controls fail as required' % len(muts))
    print('controls: self-test OK')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if a == ['--self-test']:
        sys.exit(self_test())
    if len(a) in (2, 4) and a[0] == 'check' and (len(a) == 2 or a[2] == '--freeze'):
        sys.exit(cmd_check(a[1], a[3] if len(a) == 4 else None))
    print(__doc__)
    sys.exit(2)
