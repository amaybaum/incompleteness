"""Emit controls.py for A37 from props37.json (single source with the preregistration's Lean blocks).
usage: python3 gen_controls37.py <probe blob>"""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(S, 'props37.json')))
T36 = json.load(open(os.path.join(S, '..', 'a36', 'texts36.json')))
P36 = json.load(open(os.path.join(S, '..', 'a36', 'props36.json')))
PROBE_BLOB = sys.argv[1] if len(sys.argv) > 1 else '0' * 40
def lit(d):
    return '{\n' + ',\n'.join(' %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)) for k, v in d.items()) + '\n}'
A36_HEAD = P36['COMPONENTS']['HEAD']
assert P['COMPONENTS']['HEAD36'] == A36_HEAD and P['COMPONENTS']['HEAD'] == A36_HEAD + P['COMPONENTS']['HEAD37']

SENT = {
 "A37-EXCLUSIVITY-PROVED": "At the frozen product configuration, the arc-exclusivity package holds, at evidence level 2: the arc `Pu u = SIG ∘ u^W` through the certified rational stratum point is symmetric, so that its column and row Diţă forms coincide entry for entry; the frozen `2 × 8` factorization persists along the whole arc, at every unit `u`, in both orientations; and for each of the eight other factorization classes of the stratum point — four `4 × 4`, two `8 × 2` and two `2 × 8`, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`. Beside the package, required under both decided labels: the base point `Pu 1 = SIG` carries the Kronecker `4 × 4` factorization with flat unitary factors. By the round's exact-computation probe, and not by the kernel: the census of the stratum point's Diţă structures is exhaustive, eighteen structures in nine classes; every point of the unit circle at which any structure other than the frozen class could be admitted lies in an explicitly named candidate set of twenty points, and the exhaustive search at each of them admits only the frozen class away from `u = 1`; so the exceptional set is exactly `{1}`, and for every unit `u ≠ 1` the arc point `Pu u` is a Diţă matrix for the frozen `2 × 8` class and its transpose orientation and for no other index maps at all. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law, and it does not decide whether every realizable class near the stratum lies in some Diţă hull of some factorization: the exhaustion of the hierarchy is open.",
 "A37-EXCLUSIVITY-FAILS": "At the frozen product configuration, the arc-exclusivity package fails, at evidence level 2: the symmetry of the arc, the persistence of the frozen `2 × 8` factorization in both orientations, or the exclusion of one of the eight other factorization classes away from `u = 1` is false, and the witness is exhibited in the kernel; the base control holds. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.",
 "A37-UNDECIDED": "Neither the package nor its negation was obtained. The step at which the proof stopped is named, with what would settle it."
}
CLAUSE = "Act 37 proves statements about the exact one-parameter arc of realizable classes that act 36 ran through\nact 34's certified rational stratum point, and about the Diţă factorization classes of that point, and\nadopts none of them as anything but mathematics. The classes are mathematical objects, index maps on the\nsixteen-point carrier; the symmetry of the arc, the persistence of the frozen `2 × 8` factorization and\nthe exclusion of the eight other classes away from the base point are facts about those objects and about\nnothing else. An `EXCLUSIVITY-PROVED` verdict settles the frozen package, and an `EXCLUSIVITY-FAILS`\nverdict exhibits the failure of a named part; the exact-computation layer, and not the kernel, carries\nthe exhaustive complement, that no index maps whatever admit a Diţă form of an arc point off the base\npoint but the frozen class's; and both verdicts leave open whether every realizable class near the\nstratum lies in some Diţă hull of some factorization, which the round records as open and does not\ndecide, and both leave the product normalized set unclassified. Neither verdict establishes that any\nadmissible transition law is covariant under any isometry, selects a physical law or closes `P0`. No\nhull, family, factorization, isometry, carrier, group or principle gains physical status by appearing\nhere, and nothing here derives, recognises or approaches quantum evolution."
P0_END_D = T36['P0_CASE']['A36-HIERARCHY'] + ' ' + T36['P0_STANDING_36']
P0_CASE = {
 "A37-EXCLUSIVITY-PROVED": "Along act 36's exact arc through the certified rational stratum point, the frozen `2 × 8` Diţă factorization persists at every unit parameter in both orientations, and, by the kernel for the eight other factorization classes of the stratum point and by the round's exact-computation probe for every other index map, no other Diţă factorization exists at any unit parameter other than the base point: the exceptional set of the arc is exactly `{1}`, and the arc is exclusive to its `2 × 8` class; whether every realizable class near the stratum lies in some Diţă hull of some factorization remains open, recorded and not decided.",
 "A37-EXCLUSIVITY-FAILS": "Along act 36's exact arc, the arc-exclusivity package fails at a named part, by a witness exhibited in the kernel, while the base control holds."
}
P0_STANDING_37 = "Nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."

HEADER = open(os.path.join(S, '_head_tpl.txt'), encoding='utf-8').read()
HEADER = HEADER[HEADER.index("'''") + 3:HEADER.rindex("'''")]
BODY = open(os.path.join(S, '_body.txt'), encoding='utf-8').read()
BODY = BODY[BODY.index("r'''") + 4:]

SELFTEST = r'''
def self_test():
    bad = []
    here = os.path.dirname(os.path.abspath(__file__))
    pre = os.path.join(here, 'preregistration.md')
    if not os.path.exists(pre):
        bad.append('agreement: preregistration.md not beside controls.py')
    else:
        text = open(pre, encoding='utf-8').read()
        q, n = qnorm(text), norm(text)
        for k, v in PROPS.items():
            if norm(v) not in n:
                bad.append('agreement: proposition %s not in the preregistration' % k)
        for k, v in list(SENTENCES.items()) + [('clause', CLAUSE), ('end-of-cell', P0_END_D),
                                               ('standing-37', P0_STANDING_37)] + list(P0_CASE.items()):
            if qnorm(v) not in q:
                bad.append('agreement: %s not in the preregistration' % k)
        for b in (ROADMAP_BLOB_D, GUARD_BLOB_D, WORKFLOW_BLOB_D, PROBE_BLOB, D):
            if b not in text:
                bad.append('agreement: %s not in the preregistration' % b)
        for role, nm, key in THEOREMS:
            if '`%s`' % nm not in text:
                bad.append('agreement: theorem %s not in the preregistration' % nm)
    for a, x in SENTENCES.items():
        for b, y in SENTENCES.items():
            if a != b and qnorm(x) in qnorm(y):
                bad.append('distinctness: the sentence of %s lies inside that of %s' % (a, b))
    # the duality and the single source hold of the frozen texts, and fail when either is altered
    if duality_ok(PROPS, COMPONENTS):
        bad.append('duality: the frozen texts fail: %s' % duality_ok(PROPS, COMPONENTS))
    dmuts = 0
    for nm, key, old, new in (
            ('P_R-disjunction', 'P_R', '\n  ∧ (' + COMPONENTS['PERSIST'] + ')', '\n  ∨ (' + COMPONENTS['PERSIST'] + ')'),
            ('P_R-part-dropped', 'P_R', '\n  ∧ (' + COMPONENTS['EXCL_t3'] + ')', ''),
            ('P_N-negation-dropped', 'P_N', '\n  ∨ ¬ (' + COMPONENTS['EXCL_k1'] + ')', '\n  ∨ (' + COMPONENTS['EXCL_k1'] + ')'),
            ('P_N-conjunction', 'P_N', '\n  ∨ ¬ (' + COMPONENTS['PERSIST'] + ')', '\n  ∧ ¬ (' + COMPONENTS['PERSIST'] + ')'),
            ('exclusion-drift', 'EXCL_k1', '→ u = 1)', '→ u = u)'),
            ('symmetry-drift', 'SYM', '(Pu u)ᵀ = Pu u', '(Pu u)ᵀ = (Pu u)ᵀ')):
        props = dict(PROPS)
        if props[key].count(old) < 1:
            bad.append('duality mutation %s: pattern absent' % nm)
            continue
        props[key] = props[key].replace(old, new, 1)
        dmuts += 1
        if not duality_ok(props, COMPONENTS):
            bad.append('duality mutation %s: accepted' % nm)
    comps = dict(COMPONENTS, HEAD36=COMPONENTS['HEAD36'].replace('3599 / 3601 + (120 / 3601) * Complex.I', '3599 / 3600 + (120 / 3601) * Complex.I', 1))
    dmuts += 1
    if not duality_ok(PROPS, comps):
        bad.append('duality mutation head-drift: accepted')
    comps = dict(COMPONENTS, PERSIST=COMPONENTS['PERSIST'].replace('‖D c b‖ = 1', '‖D c b‖ = 2', 1))
    dmuts += 1
    if not duality_ok(PROPS, comps):
        bad.append('duality mutation component-drift: accepted')

    fd = _synthetic_d()
    EXPECTED_PROBE_BLOB[0] = blob_id('# synthetic probe\n')
    for label in ROWS:
        fe, delta = _synthetic_e(fd, label)
        r = check_all(fd, fe, delta)
        if r:
            bad.append('positive %s: %s' % (label, r))
    PV, FL, X = ROWS
    muts = []

    def mut(name, label, fn, want):
        fe, delta = _synthetic_e(fd, label)
        fe, delta = fn(dict(fe), dict(delta))
        r = check_all(fd, fe, delta)
        muts.append(name)
        if not any(x.startswith(want) for x in r):
            bad.append('mutation %s: expected %s, got %s' % (name, want, r))

    def modstmt(label, nm, s):
        return lambda fe, dl: (dict(fe, **{MODULE: _module(label, stmt={nm: s})}), dl)
    E_ = 'end ' + NAMESPACE
    mut('definition-added', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'noncomputable def zz := 1\n' + E_)}), dl), 'module:forbidden-command')
    mut('variable-added', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a37_shared_x', '\nvariable (h : False)\ntheorem a37_shared_x')}), dl),
        'module:forbidden-command')
    mut('second-open', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a37_shared_x', '\nopen Classical in\ntheorem a37_shared_x')}), dl), 'module:open')
    mut('second-import', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '/-! synthetic -/', 'import Mathlib.GroupTheory.SemidirectProduct\n/-! synthetic -/')}), dl),
        'module:forbidden-command')
    mut('sorry', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'sorry', 1)}), dl),
        'module:forbidden-token')
    mut('native-decide', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'native_decide', 1)}), dl),
        'module:forbidden-token')
    mut('print-axioms-dropped', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '#print axioms a37_exclusivity\n', '')}), dl), 'module:no-print-axioms')
    mut('stray-theorem-name', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a37_n : True := trivial\n#print axioms a37_n\n' + E_)}), dl),
        'module:theorem-name-outside')
    mut('verdict-weakened', PV, modstmt(PV, 'a37_exclusivity', PROPS['P_R'].replace(
        '\n  ∧ (' + COMPONENTS['EXCL_t3'] + ')', '', 1)), 'module:statement-not-frozen:a37_exclusivity')
    mut('not-verdict-weakened', FL, modstmt(FL, 'a37_not_exclusivity', PROPS['P_N'].replace(
        '¬ (' + COMPONENTS['SYM'] + ')', '(' + COMPONENTS['SYM'] + ')', 1)), 'module:statement-not-frozen:a37_not_exclusivity')
    mut('exclusion-weakened', PV, modstmt(PV, 'a37_shared_excl_k1', PROPS['EXCL_k1'].replace(
        '→ u = 1)', '→ True)', 1)), 'module:statement-not-frozen:a37_shared_excl_k1')
    mut('exclusion-orientation-dropped', PV, modstmt(PV, 'a37_shared_excl_t3', PROPS['EXCL_t3'].replace(
        'ᵀ) → u = 1)', 'ᵀ) → True)', 1)), 'module:statement-not-frozen:a37_shared_excl_t3')
    mut('exclusion-unit-dropped', PV, modstmt(PV, 'a37_shared_excl_e1', PROPS['EXCL_e1'].replace(
        '∀ u : ℂ, star u * u = 1 →', '∀ u : ℂ, u = 1 →', 1)), 'module:statement-not-frozen:a37_shared_excl_e1')
    mut('symmetry-weakened', PV, modstmt(PV, 'a37_shared_symmetric', PROPS['SYM'].replace(
        '(Pu u)ᵀ = Pu u', 'Pu u = Pu u', 1)), 'module:statement-not-frozen:a37_shared_symmetric')
    mut('persistence-orientation-dropped', PV, modstmt(PV, 'a37_shared_persistence', PROPS['PERSIST'].replace(
        'Pu u = (dita28 X Y D)ᵀ', 'Pu u = dita28 X Y D', 1)), 'module:statement-not-frozen:a37_shared_persistence')
    mut('persistence-unit-dropped', PV, modstmt(PV, 'a37_shared_persistence', PROPS['PERSIST'].replace(
        '∀ u : ℂ, star u * u = 1 →', '∀ u : ℂ, u = 1 →', 1)), 'module:statement-not-frozen:a37_shared_persistence')
    mut('base-identity-dropped', FL, modstmt(FL, 'a37_control_base', PROPS['BASE'].replace(
        'Pu 1 = SIG ∧ ', '', 1)), 'module:statement-not-frozen:a37_control_base')
    mut('base-factorization-trivialized', FL, modstmt(FL, 'a37_control_base', PROPS['BASE'].replace(
        'SIG = ditak1 (F4 z) (fun _ => F4 w) (fun _ _ => (1 : ℂ))', 'SIG = SIG', 1)), 'module:statement-not-frozen:a37_control_base')
    for nm, _ in REQUIRED[PV]:
        mut('required-absent:' + nm, PV, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(PV, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    for nm, _ in REQUIRED[FL]:
        mut('required-absent-fails:' + nm, FL, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(FL, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    mut('corollary-absent', X, lambda fe, dl: (dict(fe, **{MODULE: _module(X, drop=('a37_c_exclusive',))}), dl),
        'module:required-corollary-absent')
    mut('corollary-altered', X, lambda fe, dl: (dict(fe, **{MODULE: _module(
        X, stmt={'a37_c_exclusive': corollary_statement()[2:].replace('→ ¬ (', '→ (', 1)})}), dl),
        'module:statement-not-frozen:a37_c_exclusive')
    mut('both-labels', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a37_not_exclusivity :\n    ' + PROPS['P_N'] + ' := by\n  exact test\n'
        '#print axioms a37_not_exclusivity\n' + E_)}), dl), 'module:both-labels')
    mut('note-outcome-mismatch', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '**Outcome:** `A37-EXCLUSIVITY-PROVED`', '**Outcome:** `A37-EXCLUSIVITY-FAILS`')}), dl), 'note:outcome-line')
    mut('note-second-outcome', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n**Outcome:** `A37-EXCLUSIVITY-PROVED`\n'}), dl), 'note:outcome-line')
    mut('note-sentence-altered', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        'evidence level 2', 'evidence level 3', 1)}), dl), 'note:frozen-sentence')
    mut('note-unearned-sentence', X, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + SENTENCES[PV] + '\n'}), dl), 'note:sentence-of-a-label-not-earned')
    mut('note-clause-twice', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + CLAUSE + '\n'}), dl), 'note:the-clause')
    mut('note-clause-detached', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        ' — the result note.**\n', ' — the result note.**\n' + 'x ' * 60 + '\n', 1)}), dl), 'note:the-clause')
    mut('note-control-unnamed', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a37_control_base`', 'x')}), dl), 'note:required-statement-not-named')
    mut('note-structural-unnamed', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a37_shared_persistence`', 'x')}), dl), 'note:required-statement-not-named')
    mut('note-probe-line-absent', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        'dita_arc_exclusivity_probe: OK', 'dita_arc_exclusivity_probe: ran')}), dl), 'note:probe-summary-line-absent')
    mut('roadmap-wrong-case', PV, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], FL)}), dl),
        'roadmap:')
    mut('roadmap-standing-dropped', PV, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_CASE[PV] + ' ' + P0_STANDING_37, P0_CASE[PV])}), dl), 'roadmap:')
    mut('roadmap-sentence-misplaced', PV, lambda fe, dl: (dict(fe, **{ROADMAP: fd[ROADMAP].replace(
        ' Act 25 a.', ' Act 25 a. ' + P0_CASE[PV] + ' ' + P0_STANDING_37, 1)}), dl), 'roadmap:')
    mut('roadmap-touched-when-undecided', X, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], PV)}),
        dict(dl, **{ROADMAP: 'M'})), 'roadmap:')
    mut('guard-one-byte', PV, lambda fe, dl: (dict(fe, **{GUARD: fe[GUARD] + ' '}), dict(dl, **{GUARD: 'M'})), 'guard:')
    mut('census-status-promoted', PV, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"status": "kernel-only",\n      "manuscript": [],\n      "note": "Outcome',
        '"status": "manuscript-cited",\n      "manuscript": [],\n      "note": "Outcome')}), dl),
        'census:family-disposition')
    mut('census-other-entry-changed', PV, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        '"note": "n"', '"note": "m"')}), dl), 'census:another-entry-changed')
    mut('census-outcome-wrong', PV, lambda fe, dl: (dict(fe, **{CENSUS: fe[CENSUS].replace(
        'A37-EXCLUSIVITY-PROVED.', 'A37-EXCLUSIVITY-FAILS.')}), dl), 'census:outcome')
    mut('census-entry-absent', PV, lambda fe, dl: (dict(fe, **{CENSUS: fd[CENSUS]}), dl), 'census:family-count-or-place')
    mut('wire-absent', PV, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT]}), dl), 'wire:')
    mut('wire-misplaced', PV, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT] + WIRE}), dl), 'wire:')
    mut('workflow-probe-not-wired', PV, lambda fe, dl: (dict(fe, **{WORKFLOW: fd[WORKFLOW]}), dl), 'workflow:')
    mut('workflow-extra-change', PV, lambda fe, dl: (dict(fe, **{WORKFLOW: fe[WORKFLOW] + '\n'}), dl), 'workflow:')
    mut('probe-altered', PV, lambda fe, dl: (dict(fe, **{PROBE: fe[PROBE] + '\n'}), dl), 'probe:')
    mut('path-extra', PV, lambda fe, dl: (fe, dict(dl, **{'papers/SM.md': 'M'})), 'paths:')
    mut('path-missing-note', PV, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items()
                                                         if k != RDIR + 'result.md')), 'paths:')
    mut('path-missing-probe', PV, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items() if k != PROBE)), 'paths:')
    EXPECTED_PROBE_BLOB[0] = PROBE_BLOB
    return bad, len(ROWS), dmuts, len(muts)


def main():
    if sys.argv[1:] == ['--self-test']:
        bad, rows, dmuts, muts = self_test()
        for b in bad:
            print('  FAIL', b)
        if bad:
            print('controls: self-test FAILED')
            return 1
        print('controls: the two verdict propositions are duals and every shared text has one source; '
              '%d duality mutations fail as required' % dmuts)
        print('controls: %d rows hold as frozen, %d mutation controls fail as required' % (rows, muts))
        print('controls: self-test OK')
        return 0
    if len(sys.argv) == 3 and sys.argv[1] == 'check':
        f = cmd_check(sys.argv[2])
        for x in f:
            print('  FAIL', x)
        print('controls: check %s' % ('FAILED' if f else 'OK'))
        return 1 if f else 0
    print(__doc__)
    return 2


if __name__ == '__main__':
    sys.exit(main())
'''
text = HEADER % (json.dumps(PROBE_BLOB), json.dumps(P['OPEN'], ensure_ascii=False), json.dumps(A36_HEAD, ensure_ascii=False),
                 lit(P['PROPS']), lit(P['COMPONENTS']), json.dumps(P['THEOREMS'], ensure_ascii=False, indent=1),
                 lit(SENT), json.dumps(CLAUSE, ensure_ascii=False), json.dumps(P0_END_D, ensure_ascii=False),
                 lit(P0_CASE), json.dumps(P0_STANDING_37, ensure_ascii=False)) + BODY + SELFTEST
os.makedirs(os.path.join(S, 'rec'), exist_ok=True)
open(os.path.join(S, 'rec', 'controls.py'), 'w', encoding='utf-8').write(text)
json.dump({'SENTENCES': SENT, 'CLAUSE': CLAUSE, 'P0_END_D': P0_END_D, 'P0_CASE': P0_CASE, 'P0_STANDING_37': P0_STANDING_37},
          open(os.path.join(S, 'texts37.json'), 'w'), ensure_ascii=False, indent=1)
print('controls.py written', len(text))
