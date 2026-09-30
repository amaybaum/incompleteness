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

D = '0e87c4a129d91276c10f0438d03c1bcca3a0a3b8'
RDIR = 'verification/programmes/oi-qm/track-b/act-42-support-minimality/'
PROBE = 'verification/lean/dita_support_minimality_probe.py'
PROBE_BLOB = 'f65ec4fd66f6a50d62cb231734889817aaf68187'
TOOLS = 'verification/lean/a42/'
TOOL_BLOBS = {'Rle13_39.txt': 'cb40df5fbe9f2aa6cb88e61ffb4989bb66772c21', 'c6_control.py': 'b532a9fe275443975c10d0d3e6c5fdf0ca78d53e', 'classify42.py': 'b29549361ae74a35029bbc1c77659aac85abd402', 'ctrl16.py': 'bef4ab5c2d6f4db3452962473ac61c207695f490', 'cvsize.py': 'c0e30682e76c77116d03a6507f1fe3c6ab433bb7', 'dfs01.py': 'cb6d0d03ff639586549da424ec6d59708a9147b1', 'dfs42.py': 'c7052346d472de34f29566dde7bee2ede5a27707', 'dfsR.py': 'adadda4f3ae438ed9a580db803cf57c036d46888', 'dfsR2.py': '67cd77161476adfeda38f475e0c955d467ad1b55', 'lemmas42.py': 'de7d3f39e03c58b745dc537aa759aa8764192c60', 'lib42.py': '0d9a80f5467cc9690b78aed3c094a2a8a57dcc73', 'minsupp_exact.py': '390243fd8f540e33749ebf5df17adad278bb42a8', 'pairtypes.py': '1a31f1d9de73922e63b5e5882b8ce79bb1b7c88a', 'r2a_landed.py': '3e71d33dd14edd926a55258d062f832979146ba0', 'r2b2_census.py': 'bd5bfcc4d5fe0974fbf1c00c16c411fc5377fc61', 'r2b_independent.py': 'c4a4cf3eea048f25248f9b9023c3ea8e6271eb98', 'r3_run.py': 'f7e318ddb5a891b87866baff07f5ed345a385864', 'r5_family.py': 'c7cd1ab4fe7c705c48f7a9272a3b6d5aa4db263c', 'sat42.py': '3c0f700a27ab0e3856fb82057479c3e1abaebfc7', 'sat_hr.py': 'f233b115791e3a1b82e1ff5092c06e1debcf9299', 'spanAll.py': '51e1fcfb81a0f66909c3dfe0caf2d88cab254132', 'triples.py': 'bc881bd2040538296af255107d8469141303efce'}
WORKFLOW = '.github/workflows/verify.yml'
ROADMAP = 'verification/ROADMAP.md'
LABEL = 'A42-D1-MINIMUM-40'
WORKFLOW_EDITS = [('  probes_foundations:\n    name: Numerical probes / foundations\n', "  # Act 42. Two shards run on every event; the exclusion shards, about six CPU-hours between them,\n  # run only on workflow_dispatch, which is how the exact-head attestations are taken (section A.39).\n  # On any other event the matrix job is skipped and the aggregate below requires exactly that.\n  probes_a42_witness:\n    name: Numerical probes / A42 witness\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n\n      - name: Install dependencies\n        run: pip install numpy==2.4.6 python-sat==1.9.dev15\n\n      - name: A42 witness, class supports, controls, lemmas and case-split ingredients\n        working-directory: verification/lean\n        run: |\n          python3 dita_support_minimality_probe.py --part witness\n          python3 dita_support_minimality_probe.py --part wlog\n\n  probes_a42_census01:\n    name: Numerical probes / A42 census01\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n\n      - name: Install dependencies\n        run: pip install numpy==2.4.6 python-sat==1.9.dev15\n\n      - name: A42 {0,1} census and the zero-row span lemma\n        working-directory: verification/lean\n        run: python3 dita_support_minimality_probe.py --part d01span\n\n  probes_a42_exclusion:\n    name: Numerical probes / A42 exclusion (${{ matrix.part }})\n    if: ${{ github.event_name == 'workflow_dispatch' }}\n    runs-on: ubuntu-latest\n    strategy:\n      fail-fast: false\n      matrix:\n        part: ['paths', 'r5', 'n18:0', 'n18:1', 'n18:2', 'dfs:0', 'dfs:1', 'dfs:2', 'dfs:3', 'dfs:4', 'dfs:5',\n               'sathr', 'cubes:0', 'cubes:1', 'cubes:2']\n    steps:\n      - uses: actions/checkout@v4\n\n      - uses: actions/setup-python@v5\n        with:\n          python-version: '3.11'\n\n      - name: Install dependencies\n        run: pip install numpy==2.4.6 python-sat==1.9.dev15\n\n      - name: A42 exclusion shard\n        working-directory: verification/lean\n        run: python3 dita_support_minimality_probe.py --part '${{ matrix.part }}'\n\n  probes_foundations:\n    name: Numerical probes / foundations\n"), ('probes_a45, probes_foundations]', 'probes_a45, probes_a42_witness, probes_a42_census01, probes_a42_exclusion, probes_foundations]'), ('          A45_RESULT: ${{ needs.probes_a45.result }}\n', '          A45_RESULT: ${{ needs.probes_a45.result }}\n          A42W_RESULT: ${{ needs.probes_a42_witness.result }}\n          A42C_RESULT: ${{ needs.probes_a42_census01.result }}\n          A42X_RESULT: ${{ needs.probes_a42_exclusion.result }}\n'), ('          echo "a45=${A45_RESULT}"\n', '          echo "a45=${A45_RESULT}"\n          echo "a42_witness=${A42W_RESULT}"\n          echo "a42_census01=${A42C_RESULT}"\n          echo "a42_exclusion=${A42X_RESULT} (event ${GITHUB_EVENT_NAME})"\n'), ('          test "${A45_RESULT}" = success\n', '          test "${A45_RESULT}" = success\n          test "${A42W_RESULT}" = success\n          test "${A42C_RESULT}" = success\n          if [ "${GITHUB_EVENT_NAME}" = workflow_dispatch ]; then\n            test "${A42X_RESULT}" = success\n          else\n            test "${A42X_RESULT}" = skipped\n          fi\n')]
ROADMAP_EDITS = [('Which points of the family admit a Diţă structure, the census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open,', 'Which points of the family admit a Diţă structure and the census of exponent matrices with entries in `{0, 1}` stay open,', 1), ('The census of exponent matrices with entries in `{0, 1}` and the minimality of support 48 stay open,', 'The census of exponent matrices with entries in `{0, 1}` stays open,', 2), ("`P0`'s cross-time parts are untouched, no relation is adopted as the physical one, and nothing here names, endorses or excludes a selection principle. |", "`P0`'s cross-time parts are untouched, no relation is adopted as the physical one, and nothing here names, endorses or excludes a selection principle. Among straight lines through the certified rational stratum point, with class support the least number of nonzero exponent entries over the orbit under the gauge, the point's stabilizer and sign, and among the classes that have a least-support representative with entries in `{−1, 0, 1}`, the least class support of a line lying identically in no Diţă structure of the point is exactly 40, attained by act 42's `E40`, and act 38's witness has class support 44 (act 42: exact computation over a case split stated in its record, with the no-zero-line case and the zero-row case with at least fourteen nonzero rows closed by SAT verdicts carried without proof logs); classes outside that domain and the class supports 41 to 43 and 45 to 47 are not determined, and no line or support value is adopted as a physical symmetry, principle or law. |", 1), ("**Future classification, not an A38 result, and independent of the census and of the three-parameter\nfamily.** Act 38's witness `E = A + B + C` has 48 nonzero entries. Whether a straight line through the\ncertified stratum point that lies identically in none of the Diţă structures of the point can have smaller\nsupport, in any gauge and after the stabilizer action, is open. The question is a minimisation over\nstabilizer orbits of straight exponent matrices; an answer would say whether act 38 found a smallest\nescape direction or one among escapes of several sizes. A minimality statement requires either an\nexhaustive search below a stated support bound, which does not presuppose the full census, or a\nstructural lower bound.\n", "**Future classification beyond act 42's domain, independent of the census and of the three-parameter\nfamily.** The class support of a straight line through the certified stratum point is the least number of\nnonzero entries of its exponent matrix over the orbit under the gauge, the stabilizer of the point and\nsign. Among the classes that have a least-support representative with entries in `{−1, 0, 1}`, the least\nclass support of a line lying identically in none of the Diţă structures of the point is exactly 40,\nattained by act 42's exponent matrix `E40`, whose entries lie in `{−1, 0, 1}`; act 38's witness\n`E = A + B + C`, with 48 nonzero entries, has class support 44. Open: whether a class all of whose\nleast-support representatives have an entry of absolute value at least 2 has class support below 40, and\nwhich of the class supports 41 to 43 and 45 to 47 occur. A minimality statement beyond that domain\nrequires either an exhaustive search below a stated support bound, which does not presuppose the full\ncensus, or a structural lower bound.\n", 1)]
SENTENCE = "Within D1, the least class support of a non-Diţă straight line is exactly 40. Here a straight line is an integer exponent matrix `E` with `SIG ∘ u^E` complex Hadamard for every unit `u`; its class is its orbit under the gauge, the stabilizer of `SIG` and sign; its class support is the least number of nonzero entries over the class; D1 is the set of classes having a least-support representative with entries in {−1, 0, 1}; and non-Diţă means lying identically in no Diţă structure of `SIG` under act 41's semantics. The value is attained by `E40 = −P + Q − T`, straight by two exact methods, of class support exactly 40 by exact enumeration, and non-Diţă by two independent paths. No class of D1 has class support at most 39 and is non-Diţă: in the zero-row case with at most thirteen nonzero rows by an exact exhaustive search whose every leaf lies in one of eighteen subspaces, each equal by exact rank to the relaxed identity subspace of one of act 41's 976 realizing triples; in the zero-row case with at least fourteen nonzero rows and in the case with no zero line by SAT verdicts (UNSAT) carried without proof logs. Act 38's witness has class support 44. The lemmas of the case split are stated and argued in the preregistration and are not kernel-checked, the general-integer exclusions of the pre-freeze analysis are not re-derived, and nothing is claimed outside D1 or about the class supports 41 to 43 and 45 to 47."
CLAUSE = 'Act 42 settles, by exact computation, a case split stated in its preregistration and SAT verdicts carried without proof logs, the least class support of a straight line through the certified rational stratum point that lies identically in no Diţă structure of the point, within the domain D1 of classes having a least-support representative with entries in {−1, 0, 1}; the value is 40. It says nothing about classes outside D1, determines none of the class supports 41 to 43 and 45 to 47, re-derives none of the general-integer exclusions of the pre-freeze analysis, revises no earlier verdict, adopts no line, family or support value as a physical symmetry, principle or law, and leaves `P0` open; nothing here names, endorses or excludes a selection principle.'
CLAUSE_MENTION = '**THE CLAUSE, carried at this mention — the result.**'
PART_CHECKS = {'witness': 11, 'wlog': 9, 'd01span': 6, 'paths': 9, 'r5': 2, 'n18:0': 7, 'n18:1': 7, 'n18:2': 7, 'dfs:0': 4, 'dfs:1': 4, 'dfs:2': 4, 'dfs:3': 4, 'dfs:4': 4, 'dfs:5': 4, 'sathr': 1, 'cubes:0': 10, 'cubes:1': 10, 'cubes:2': 9}
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
