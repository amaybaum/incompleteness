"""Mutation tests at the integration of #861 with #860 (disposable). argv: <worktree> <mutant> <outdir>
The 46 mutants of #860's CN-1..CN-3 harness (ci/ret-tests-20261018 at 71c9fcfe), each edit unchanged: every anchor
occurs once in the integrated files, inside a function identical to its 4e7aec44 version, so none is re-anchored.
Origin 'pr861' adds #861's regressions (R14, R15, the named extractor, the gate's extractor step, the extractor's
fail-closed reading), run against check_retention.py, reproduce.py or extract_result.py.
The author's F1 and R13 mutants (s1017/cier-o10fix/scripts/mutants_{f1,r13}.py) and the independent review's mutants
(s1018/review-860/tools/mutants.py), each applied in memory to one checker (the file on disk is never written), then
that checker's full self-test is run from the mutated module.

origin  'author-f1' / 'author-r13' / 'review' / 'new' (a mutant of code this commit adds)
edit    'verbatim' when the original edit's text still occurs once, else 'adapted': the commit restructured that code,
        and the edit restores the same old behaviour at its new place (the reason is given beside each).
Criterion: KILLED iff every named target case turns red (NOT DETECTED or FAILS for check_objects, FAIL self for
check_retention). The original scripts required exactly their targets; the suites have grown, so a mutant may now also
turn new cases red, and every red case is listed. A mutant with no named target is KILLED iff the self-test fails."""
import contextlib, io, os, re, sys, types

wt, which, outdir = sys.argv[1:4]
A = os.path.join(wt, 'verification/audits/evidence-retention')
CO, CR = 'check_objects.py', 'check_retention.py'
EX, RP = 'extract_result.py', 'reproduce.py'
L = 'lifecycle '
F1O10 = ['F1 O10: the record swaps the two full ids, keeping their eight-digit forms',
         'F1 O10: the record mistypes the full id after digit 10', 'F1 O10: the run line states another head']
F1O7 = ['F1 O7: promoted to the swapped full id and the run line beside the other',
        'F1 O7: promoted to the mistyped full id\'s line and the run line',
        'F1 O7: promoted to the run line that states another head']
CN1 = ['CN-1: the near-miss head promoted with the token rule and tranche %s' % x for x in ('3', "'4'", '2', 'True', '4.0')]
# name: (origin, file, edit kind, reason, [(old, new)], [targets])
M = {
    # ---- author F1 (mutants_f1.py)
    'M10': ('author-f1', CO, 'adapted', 'O10 now applies the citation rule through run_citations; the edit drops its verdict',
            [("    elif why:\n        bad.append(why)\n", "    elif False:\n        bad.append(why)\n")], F1O10),
    'M7': ('author-f1', CO, 'adapted', 'the O7 loop moved into o7_entry, and the lifecycle rule has a coverage half; both are dropped',
           [("        elif lifecycle(e):\n            r = cited_by_rule", "        elif False:\n            r = cited_by_rule"),
            ("        for r in lifecycle_coverage(oid, e['cited'], lines_of):\n", "        for r in []:\n")],
           F1O7 + ['a promoted run citation whose run is retained with another head']),
    'MN4': ('author-f1', CO, 'verbatim', '',
            [("        return False, 'ci/%s/run.json is not readable JSON' % run\n", "        return True, None\n")],
            ['a pending entry whose run is retained with a run.json that is not JSON (N4)']),
    'MN5': ('author-f1', CO, 'adapted', 'the run lines are found by run_citations, not run_word; the edit makes the run optional there',
            [("            not (isinstance(run, str) and re.fullmatch(r'[0-9]{1,20}', run)) or \\\n",
              "            not (run is None or isinstance(run, str) and re.fullmatch(r'[0-9]{1,20}', run)) or \\\n"),
             ("    ok, rhead = ci_head(root, run)\n", "    ok, rhead = ci_head(root, run) if run is not None else (True, None)\n"),
             ("    free, emb, why = run_citations(oid, run, L)\n",
              "    free, emb, why = run_citations(oid, run, L) if run is not None else ([1], [], None)\n")],
            ['a pending entry that records no run (N5)']),
    # ---- author R13 (mutants_r13.py)
    'MR-a': ('author-r13', CR, 'verbatim', '',
             [("            R13_STATES[eid] = ('pending', None)\n", "            R13_STATES[eid] = ('eligible', None)\n")],
             [L + '(a): the intended record not in the tree, the entry pending']),
    'MR-b': ('author-r13', CR, 'verbatim', '', [("        if path != rec:\n", "        if True:\n")],
             [L + '(b): the intended record lands citing the run and its head, the manifest unchanged (eligible)',
              L + '(c): the entry maps the record\'s citing line (cited)',
              L + '(d): the intended record lands naming another head beside the run (R13)',
              'the intended record lands citing the run on another line than recorded (R13)',
              'the intended record lands citing the run without its head (R13)',
              'the intended record lands with the head mistyped after digit 10 (R13)']),
    'MR-c': ('author-r13', CR, 'adapted', 'the eligible state now records the free-standing lines',
             [("    R13_STATES[eid] = ('eligible', free)\n", "    R13_STATES[eid] = ('cited', free)\n")],
             [L + '(b): the intended record lands citing the run and its head, the manifest unchanged (eligible)']),
    'MR-c2': ('author-r13', CR, 'verbatim', '',
              [("        R13_STATES[eid] = ('cited', sorted(mapped))\n", "        R13_STATES[eid] = ('eligible', sorted(mapped))\n")],
              [L + '(c): the entry maps the record\'s citing line (cited)']),
    'MR-d': ('author-r13', CR, 'adapted', 'eligibility applies the rule through run_citations; the edit drops its verdict',
             [("    if why:\n        F('R13 %s: its record %s %s' % (eid, rec, why.replace('head', 'run head')))\n",
               "    if False:\n        F('R13 %s: its record %s %s' % (eid, rec, why.replace('head', 'run head')))\n")],
             [L + '(d): the intended record lands naming another head beside the run (R13)',
              'the intended record lands citing the run without its head (R13)',
              'the intended record lands with the head mistyped after digit 10 (R13)']),
    'MR-d2': ('author-r13', CR, 'verbatim', '',
              [("    if not lines:\n        F('R13 %s: its record %s is in the tree and does not cite run %s' % (eid, rec, rid))\n        return\n",
                "    if not lines:\n        R13_STATES[eid] = ('pending', None)\n        return\n")],
              [L + '(d): the intended record lands citing another run (R13)']),
    'MR-line': ('author-r13', CR, 'verbatim', '', [("    if aw['line'] not in lines:\n", "    if False:\n")],
                ['the intended record lands citing the run on another line than recorded (R13)']),
    'MR-cited-head': ('author-r13', CR, 'adapted', 'the cited state applies the rule through run_citations; the edit drops its verdict',
                      [("            if why:\n                F('R13 %s: its citation at %s %s'",
                        "            if False:\n                F('R13 %s: its citation at %s %s'")],
                      ['a mapped citation whose line names another head (R13)']),
    'MR-e': ('author-r13', CR, 'verbatim', '',
             [("                F('R3 %s: citing file %s missing' % (eid, c.get('path')))\n", "                pass\n")],
             [L + '(e): the record removed while the entry maps it (R3)']),
    # ---- the review's mutants (mutants.py), N2 among them
    'X-r13-summary-eligible-as-cited': ('review', CR, 'adapted', 'the summary moved into r13_summary()',
        [("        n('cited'), n('pending'), n('eligible'))\n", "        n('cited') + n('eligible'), n('pending'), 0)\n")],
        ['N2: the summary counts an eligible entry apart, never as cited']),
    'X-r13-missing-runjson-pending': ('review', CR, 'verbatim', '',
        [("    if run is None or jobs is None or res is None:\n",
          "    if run is None:\n        R13_STATES[eid] = ('pending', None)\n        return\n    if run is None or jobs is None or res is None:\n")],
        ['a research entry without run.json (R13)']),
    'X-r13-cited-unmapped-ok': ('review', CR, 'adapted', 'the cited state checks unmapped free-standing citations per mapped file',
        [("            for n in free:\n                if (p, n) not in mapped:\n", "            for n in []:\n                if (p, n) not in mapped:\n")],
        ['the record cites the run on two lines and the entry maps one (R13)']),
    'X-r13-headless-pending': ('review', CR, 'verbatim', '',
        [("        if head is not None:\n            R13_STATES[eid] = ('pending', None)\n", "        R13_STATES[eid] = ('pending', None)\n")],
        []),
    'X-r13-pending-other-file-ok': ('review', CR, 'verbatim', '',
        [("    for path, line in cl:\n        if path != rec:\n", "    for path, line in cl:\n        if False:\n")],
        ['a research run that a tracked file now cites (R13)', 'the intended record lands, and another file also cites the run (R13)']),
    'X-r13-eligible-recorded-line-only': ('review', CR, 'adapted', 'eligibility applies run_citations to every line; the edit keeps the recorded line\'s head rule only',
        [("    free, emb, why = rules.run_citations(head, rid, L)\n    if aw['line'] not in free:\n",
          "    free, emb, why = rules.run_citations(head, rid, L)\n    why = rules.head_rule(head, L, aw['line'])\n    if aw['line'] not in free:\n")],
        ['CN-3 d-far: a far line of the record cites the run beside another head (R13)',
         'CN-3 d-far-nohead: a far line of the record cites the run without its head (R13)']),
    'X-o10-summary-eligible-as-cited': ('review', CO, 'adapted', 'the summary moved into citation_summary()',
        [("        count('cited'), count('pending'), count('eligible'))\n", "        count('cited') + count('eligible'), count('pending'), 0)\n")],
        ['N2: the summary counts an eligible entry apart, never as cited']),
    'X-head-prefix-for-full': ('review', CO, 'verbatim', '',
        [("    if not any(oid in HEXWORD.findall(l) for l in win):\n", "    if not any(oid.startswith(w) for l in win for w in HEXWORD.findall(l)):\n")],
        ['N2: the head stated beside the run only as its eight-digit form']),
    'X-head-ignore-short-other': ('review', CO, 'adapted', 'the same text now also occurs in embedded_rule; the edit targets head_rule',
        [("    bad = sorted({w for l in win for w in other_ids(oid, l)})\n    if bad:\n        return 'names another head beside the run on line",
          "    bad = sorted({w for l in win for w in other_ids(oid, l) if len(w) >= 8})\n    if bad:\n        return 'names another head beside the run on line")],
        ['N2: a seven-digit form of another head beside the run']),
    'X-head-ignore-below-9': ('review', CO, 'adapted', 'as above',
        [("    bad = sorted({w for l in win for w in other_ids(oid, l)})\n    if bad:\n        return 'names another head beside the run on line",
          "    bad = sorted({w for l in win for w in other_ids(oid, l) if len(w) >= 9})\n    if bad:\n        return 'names another head beside the run on line")],
        ['F1 O10: the run line states another head']),
    'X-head-window-run-line-only': ('review', CO, 'adapted', 'as above',
        [("    bad = sorted({w for l in win for w in other_ids(oid, l)})\n    if bad:\n        return 'names another head beside the run on line",
          "    bad = sorted({w for w in other_ids(oid, L[n - 1])})\n    if bad:\n        return 'names another head beside the run on line")],
        ['F1 O10: the record swaps the two full ids, keeping their eight-digit forms', 'F1 O10: the record mistypes the full id after digit 10']),
    'X-lifecycle-by-label': ('review', CO, 'adapted', 'X-lifecycle-from-5 edited LIFECYCLE_TRANCHE, which the pin replaced; this restores the base\'s label test',
        [("    return e.get('type') == 'commit' and e.get('oid') not in TRANCHE_MEMBERS[2]\n",
          "    return e.get('type') == 'commit' and type(e.get('tranche')) is int and e['tranche'] >= 4\n")], CN1),
    'X-lifecycle-from-5': ('review', CO, 'adapted', 'as above, with tranche 5 as the first lifecycle tranche',
        [("    return e.get('type') == 'commit' and e.get('oid') not in TRANCHE_MEMBERS[2]\n",
          "    return e.get('type') == 'commit' and type(e.get('tranche')) is int and e['tranche'] >= 5\n")], F1O7),
    'X-o7-no-ci-head': ('review', CO, 'verbatim', '',
        [("        ok, h = ci_head(root, str(c['run']))\n", "        ok, h = True, None\n")],
        ['a promoted run citation whose run is retained with another head']),
    'X-o7-no-run-citation-ok': ('review', CO, 'adapted', 'the check moved into o7_entry',
        [("        if not any(c.get('run') for c in e['cited']):\n", "        if False:\n")],
        ['a promoted lifecycle entry without a run citation']),
    'X-run-digit-bounded': ('review', CO, 'verbatim', '',
        [("    return re.compile(r'(?<![0-9A-Za-z])%s(?![0-9A-Za-z])' % re.escape(run))\n",
          "    return re.compile(r'(?<![0-9])%s(?![0-9])' % re.escape(run))\n")], []),
    'X-ci-head-headless-absent': ('review', CO, 'verbatim', '',
        [("        return False, 'ci/%s/run.json names no head commit' % run\n", "        return True, None\n")],
        ['a pending entry whose run is retained with a run.json naming no head (N4)']),
    # ---- new code (CN-1..CN-3)
    'N-o3-off': ('new', CO, '-', 'tranche_failures reports nothing',
        [("    for oid, e in sorted(ents.items()):\n        t = e.get('tranche')\n", "    for oid, e in []:\n        t = e.get('tranche')\n")],
        CN1 + ['a pinned tranche-2 entry relabelled tranche 4', 'an entry the pin does not hold, labelled tranche 2']),
    'N-pin-digest-off': ('new', CO, '-', 'the pin\'s own count and digest are not checked',
        [("        if len(s) != n or sha256(''.join(o + '\\n' for o in s).encode()) != d:\n", "        if False:\n")],
        ['the checker\'s tranche-2 pin edited without its count and digest']),
    'N-coverage-off': ('new', CO, '-', 'O7\'s coverage half reports nothing',
        [("        if q - mapped:\n", "        if False:\n")],
        ['CN-3 f1: a promotion that maps the run line only', 'CN-3 f5: a second correct citation in the record left unmapped',
         'CN-3 f6: the id cited again in the record, unmapped']),
    'N-twice-ok': ('new', CO, '-', 'a location mapped twice is accepted',
        [("    out += ['%s is mapped twice' % x for x in sorted({x for x in locs if locs.count(x) > 1})]\n", "")],
        ['CN-3: a location mapped twice']),
    'N-all-free': ('new', CO, '-', 'every occurrence is free-standing',
        [("        out.append('embedded' if b in LETTERS", "        out.append('free' if b in LETTERS")],
        # boundary (a)'s run line also cites the run free-standing, so this mutant cannot change it; the file-name
        # fixtures are the ones whose verdict it changes
        ['CN-3: the run named inside an evidence file name with its digest (eligible)',
         'documented limitation: another head as the last 40 digits of a 64-digit word beside a file name passes']),
    'N-all-embedded-free-ok': ('new', CO, '-', 'an embedded-only record counts as citing the run',
        [("    if not free:\n        near", "    if not free and not emb:\n        near")],
        ['CN-3: the run named only inside an identifier', 'boundary (b): a file name with a digest never establishes the citation']),
    'N-no-joiners': ('new', CO, '-', 'joiners do not embed (letters only)',
        [("    out.append('embedded' if b in LETTERS or a in LETTERS or (b in JOINERS and b2 in ALNUM) or\n                   (a in JOINERS and a2 in ALNUM) else 'free')",
          "    out.append('embedded' if b in LETTERS or a in LETTERS else 'free')")],
        ['CN-3: the run named inside an evidence file name with its digest (eligible)']),
    'N-embedded-unchecked': ('new', CO, '-', 'an embedded mention is not checked for another head',
        [("        r = head_rule(oid, L, n) if n in free else embedded_rule(oid, L, n)\n", "        r = head_rule(oid, L, n) if n in free else None\n")],
        ['CN-3: an embedded mention beside a different full head', 'N1: another head glued into a file name beside the run (a 52-digit hex word)']),
    'N-64-as-head': ('new', CO, '-', 'a 64-digit word names a head',
        [("        if len(w) < 64 and (", "        if len(w) < 999 and (")],
        ['boundary (a): a genuine 64-digit digest beside the citation and the file name passes',
         'documented limitation: another head as the last 40 digits of a 64-digit word beside a file name passes']),
    'N-41-63-ignored': ('new', CO, '-', 'a 41-63 digit word names no head',
        [("(len(w) > 40 or (lw != oid", "(False or (lw != oid")],
        # a 41-63 digit word with a hex letter still names another head by the shorter-word branch; the mutant changes
        # only an all-decimal word of that length
        ['N1: an all-decimal 45-digit word beside the run\'s file name']),
    'N-case-sensitive': ('new', CO, '-', 'uppercase hex words are not read',
        [("    for w in HEXANY.findall(line):\n        lw = w.lower()\n", "    for w in [w for w in HEXANY.findall(line) if w == w.lower()]:\n        lw = w.lower()\n")],
        ['N1: the run line states another head in uppercase']),
    'N-co-fixture-skip': ('new', CO, '-', 'CN-2: the lifecycle fixture cannot be built (as if the live state lacked it)',
        [("        fixture_ok = len(stand) == 2 and ", "        fixture_ok = False and len(stand) == 2 and ")], None),
    'N-r13-fixture-skip': ('new', CR, '-', 'CN-2: the R13 fixture cannot be built',
        [("    if len(idx) < 2:\n", "    if True:\n")], None),
    'N-r13-mapped-embedded-ok': ('new', CR, '-', 'R13 accepts a mapped line that names the run only embedded',
        [("            for ln in lns:\n                if ln not in free:\n", "            for ln in lns:\n                if ln not in free + emb:\n")],
        ['CN-3: a mapped line that names the run only inside an identifier (R13)']),
    'N-r13-twice-ok': ('new', CR, '-', 'R13 accepts a line mapped twice',
        [("        if twice:\n            F('R13 %s: its citations map", "        if False:\n            F('R13 %s: its citations map")],
        ['CN-3: a citation mapped twice (R13)']),
    'N-r13-recorded-embedded-ok': ('new', CR, '-', 'R13 accepts a recorded line that names the run only embedded',
        [("    if aw['line'] not in free:\n        F('R13 %s: its record %s names run %s on the recorded line",
          "    if aw['line'] not in free + emb:\n        F('R13 %s: its record %s names run %s on the recorded line")],
        ['CN-3: the recorded line names the run only inside an identifier (R13)']),
    # ---- #861: extractor-version tracking and reproduction (origin 'pr861'; each edit restores a fail-open)
    'P-rp-checkout-extractor': ('pr861', RP, '-', "reproduce() runs the checkout's extract_result.py, not the blob the result names",
        [("    extract, xblob, xproblem = named_extractor(man, fe)\n",
          "    extract, xblob, xproblem = named_extractor(man, fe)\n    sys.path.insert(0, HERE)\n"
          "    import extract_result as _checkout\n    extract = _checkout.extract\n")],
        ['reproduce() for ci-38855576525, its build stubbed with the retained tail, records and runs blob']),
    'P-rp-named-from-checkout': ('pr861', RP, '-', "named_extractor() loads the checkout's file under the named blob id",
        [("    p = subprocess.run(['git', 'cat-file', 'blob', b], cwd=root, capture_output=True)\n",
          "    p = __import__('types').SimpleNamespace(returncode=0, stdout=open(os.path.join(HERE, 'extract_result.py'), 'rb').read())\n")],
        ['ci-35716484185 names 05c41bce610b, not the checkout',
         'reproduce() for ci-38855576525, its build stubbed with the retained tail, records and runs blob']),
    'P-r15-history-off': ('pr861', CR, '-', "R15's history derivation accepts any named blob",
        [("            if at[c] != b:\n", "            if False:\n")],
        ['a result naming a later extractor than the one that read it, in history mode (R15)',
         'a re-extraction naming the original extractor instead of its own, in history mode (R15)']),
    'P-r15-tree-off': ('pr861', CR, '-', 'R15 in the tree accepts a file that names no extractor blob, or two',
        [("        if why:\n            F('R15 %s: %s %s' % (e.get('id'), rel, why))\n",
          "        if False:\n            F('R15 %s: %s %s' % (e.get('id'), rel, why))\n")],
        ['a result whose extractor blob is dropped from extractor_blobs (R15)', 'a result naming a malformed extractor blob (R15)',
         'a result naming one blob in its file and another in extractor_blobs (R15)']),
    'P-r14-off': ('pr861', CR, '-', 'R14 is not run on a CI entry',
        [("            check_reextractions(e, files, F)\n", "            pass\n")],
        ['the original result rewritten to the corrected count, its recorded size and digest following it, fails R14 and not R1',
         'the original result rewritten in place (R14)', 'a re-extraction that is not JSON (R14)',
         'an accounting no re-extraction names (R14)']),
    'P-gate-no-extractor': ('pr861', CR, '-', 'the gate runs no extractor self-test',
        [("GATE_SELF_TESTS = (('extractor self-test', extractor_gate),)\n", "GATE_SELF_TESTS = ()\n")],
        ["the gate runs the extractor's self-test"]),
    'P-ex-unprimed': ('pr861', EX, '-', 'the extractor before 4086f107: a primed declaration name is not read',
        [(r"\.lean):(\d+):\d+: '(.+?)' (depends", r"\.lean):(\d+):\d+: '([^']+)' (depends")],
        ['run 38450187534: primed names read with their module, line and axioms']),
    'P-ex-direct-ignored': ('pr861', EX, '-', 'the extractor before 4086f107: lake-prefixed reports only, direct lean reports ignored',
        [("DIRECT = re.compile(r\"^'(.+?)' (depends on axioms: \\[(.*)|does not depend on any axioms)\")\n",
          "DIRECT = re.compile(r'(?!)')\n")],
        ['design log: two blocks, attributed to their files, 7 and 3 reports, wrapped lists joined',
         "run 38450187534: the 4 design reports, attributed to the step's one file, with their axioms",
         'run 38454439833: all 10 design reports read with their axioms']),
    'P-ex-join-any-line': ('pr861', EX, '-', 'the extractor before 4086f107: a wrapped list absorbs any following line',
        [("    while ']' not in body and j + 1 < len(lines) and CONT.match(lines[j + 1].rstrip()):\n",
          "    while ']' not in body and j + 1 < len(lines):\n")],
        ['E tail, the second report cut to its first line: truncated, and the next report still read']),
    'P-ex-multi-file-attributed': ('pr861', EX, '-', 'a step running lean on several files is attributed to one of them',
        [("    if len(set(files)) > 1:\n        return None,", "    if False:\n        return None,")],
        ['run 38454439833: both lean commands read, the block unattributed']),
}
origin, fn, kind, reason, edits, want = M[which]
src = open(os.path.join(A, fn), encoding='utf-8').read()
for old, new in edits:
    assert src.count(old) == 1, (which, old[:80], src.count(old))
    src = src.replace(old, new)
mod = types.ModuleType('mut_' + re.sub(r'\W', '_', which))
mod.__file__ = os.path.join(A, fn)
exec(compile(src, '<%s %s>' % (fn, which), 'exec'), mod.__dict__)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    try:
        rc = mod.self_test(mod.ROOT) if fn == CO else mod.self_test() if fn in (EX, RP) else \
            mod.self_test(A, os.path.abspath(os.path.join(A, '..', '..', '..')))
    except Exception as exc:                                   # a crash counts as red, and is reported
        rc = 'crash %r' % exc
out = buf.getvalue()
if fn == CO:
    red = [l.strip() for l in out.split('\n') if re.search(r'\s(NOT DETECTED|FAILS)(\s|$)', l) and 'as required' not in l]
    names = [re.split(r'\s{2,}', r)[0] for r in red]
else:
    red = [l for l in out.split('\n') if l.startswith('FAIL self: ')]
    names = [r[len('FAIL self: '):] for r in red]
open(os.path.join(outdir, which + '.out'), 'w').write(out)
crashed = isinstance(rc, str) and rc.startswith('crash')
if want is None:
    killed = bool(red) or rc not in (0,)
else:
    killed = bool(names) and all(any(n == t or n.startswith(t) for n in names) for t in want)
print('%s [%s, %s%s]: self-test rc %s; red cases %d; targets %s' % (which, origin, kind, (': ' + reason) if reason else '',
                                                                   rc, len(red), want))
for n in names:
    print('    red: ' + n[:170])
# a crash evaluates no target: it is INCONCLUSIVE, never SURVIVED or KILLED
print('%s: %s' % (which, 'INCONCLUSIVE (crash)' if crashed and want is not None else 'KILLED' if killed else 'SURVIVED'))
