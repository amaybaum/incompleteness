"""Emit controls.py for A38 from props38.json (single source with the preregistration's Lean blocks).
usage: python3 gen_controls38.py <probe blob>"""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P = json.load(open(os.path.join(S, 'props38.json')))
T37 = json.load(open(os.path.join(S, '..', 'a37', 'texts37.json')))
P37 = json.load(open(os.path.join(S, '..', 'a37', 'props37.json')))
PROBE_BLOB = sys.argv[1] if len(sys.argv) > 1 else '0' * 40
def lit(d):
    return '{\n' + ',\n'.join(' %s: %s' % (json.dumps(k, ensure_ascii=False), json.dumps(v, ensure_ascii=False)) for k, v in d.items()) + '\n}'
A37_HEAD = P37['COMPONENTS']['HEAD']
assert P['COMPONENTS']['HEAD36'] + P['COMPONENTS']['HEAD37'] == A37_HEAD and P['COMPONENTS']['HEAD'] == A37_HEAD + P['COMPONENTS']['HEAD38']

SENT = {
 "A38-NON-DITA-WITNESS-PROVED": "At the frozen product configuration, the local-escape package holds, at evidence level 2: for the explicit exponent matrix `E = A + B + C` on the sixteen-point carrier and the arc `Hu u = SIG ∘ u^E` through the certified rational stratum point, `Hu u` is a flat unitary — a complex Hadamard matrix, realizable — at every unit `u`; and for each of the nine Diţă factorization classes of the stratum point — four `4 × 4`, two `8 × 2` and three `2 × 8`, the complete census of its Diţă structures modulo its stabilizer — a Diţă form of `Hu u` at that class's index maps, in either orientation, forces `u = 1`; so, as the corollary, every neighbourhood of `SIG` contains a realizable matrix admitting none of the eighteen forms. Beside the package, required under both decided labels: the base point `Hu 1 = SIG` carries the Kronecker `4 × 4` factorization with flat unitary factors. By the round's exact-computation probe, and not by the kernel: at a generic `u` no index maps whatever pass the proportionality test in either orientation; every unit at which any structure could be admitted lies in an explicitly named candidate set of forty points; the exhaustive search at each of them finds a Diţă structure at `u = 1` and at `u = −1` only, and the same up to diagonal equivalence; so the exceptional set is exactly `{1, −1}`, and for every unit `u ∉ {1, −1}` the arc point `Hu u` admits no Diţă structure of any admissible shape, index map or orientation, including up to the allowed diagonal equivalences. The local Diţă hulls of the stratum point's factorizations do not exhaust the realizable geometry near `SIG`: realizable points in no such hull lie arbitrarily close to it. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.",
 "A38-WITNESS-FAILS": "At the frozen product configuration, the local-escape package fails, at evidence level 2: the realizability of the arc at some unit, or the exclusion of one of the nine factorization classes away from `u = 1` in some orientation, is false, and the witness is exhibited in the kernel; the base control holds. This is a statement about the frozen mathematical objects; it adopts no family, factorization or isometry as a symmetry, a principle or a law.",
 "A38-UNDECIDED": "Neither the package nor its negation was obtained. The step at which the proof stopped is named, with what would settle it."
}
CLAUSE = "Act 38 proves statements about one exact one-parameter arc of realizable classes through act 34's certified\nrational stratum point, given by an explicit exponent matrix, and about the Diţă factorization classes of that\npoint, and adopts none of them as anything but mathematics. The classes are mathematical objects, index maps on\nthe sixteen-point carrier; the realizability of the arc, the exclusion of the nine classes away from the base\npoint and the local escape are facts about those objects and about nothing else. A `NON-DITA-WITNESS-PROVED`\nverdict settles the frozen package, and a `WITNESS-FAILS` verdict exhibits the failure of a named part; the\nexact-computation layer, and not the kernel, carries the exhaustive complement, that no index maps whatever\nadmit a Diţă form of an arc point off the two exceptional units, strictly or up to diagonal equivalence; and\nboth verdicts leave the product normalized set unclassified. Neither verdict establishes that any admissible\ntransition law is covariant under any isometry, selects a physical law or closes `P0`. No hull, family,\nfactorization, isometry, carrier, group or principle gains physical status by appearing here, and nothing here\nderives, recognises or approaches quantum evolution."
P0_END_D = T37['P0_CASE']['A37-EXCLUSIVITY-PROVED'] + ' ' + T37['P0_STANDING_37']
P0_CASE = {
 "A38-NON-DITA-WITNESS-PROVED": "For an explicit exponent matrix `E = A + B + C`, the arc `SIG ∘ u^E` through the certified rational stratum point is realizable at every unit parameter, by the kernel; each of the nine Diţă factorization classes of the stratum point is admitted along it only at the base point, in either orientation, by the kernel; and, by the round's exact-computation probe for every other index map, the arc point admits no Diţă structure of any shape, index map or orientation at any unit parameter outside `{1, −1}`, strictly or up to diagonal equivalence: the local Diţă hulls of the stratum point's factorizations do not exhaust the realizable geometry near it, and realizable points in no such hull lie arbitrarily close to it. The tangent space at the stratum point is spanned by the eighteen Diţă tangent subspaces, so the escape is a nonlinear compatibility obstruction and not a missing tangent direction.",
 "A38-WITNESS-FAILS": "Along the explicit arc `SIG ∘ u^E`, the local-escape package fails at a named part, by a witness exhibited in the kernel, while the base control holds."
}
P0_STANDING_38 = "Nothing here classifies the product normalized set or its isometries or establishes that any admissible law is covariant under any isometry or reaches any class, `P0`'s threading part is untouched, no hull, family, factorization or isometry is adopted as a physical symmetry, principle or law, and nothing here names, endorses or excludes a selection principle."

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
                                               ('standing-38', P0_STANDING_38)] + list(P0_CASE.items()):
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
            ('P_R-disjunction', 'P_R', '\n  ∧ (' + COMPONENTS['EXCL_k1'] + ')', '\n  ∨ (' + COMPONENTS['EXCL_k1'] + ')'),
            ('P_R-part-dropped', 'P_R', '\n  ∧ (' + COMPONENTS['EXCL_t3'] + ')', ''),
            ('P_N-negation-dropped', 'P_N', '\n  ∨ ¬ (' + COMPONENTS['EXCL_k1'] + ')', '\n  ∨ (' + COMPONENTS['EXCL_k1'] + ')'),
            ('P_N-conjunction', 'P_N', '\n  ∨ ¬ (' + COMPONENTS['EXCL_k2'] + ')', '\n  ∧ ¬ (' + COMPONENTS['EXCL_k2'] + ')'),
            ('exclusion-drift', 'EXCL_k1', '→ u = 1)', '→ u = u)'),
            ('realizability-drift', 'REAL', '‖Hu u i j‖ = 1 / 4', '‖Hu u i j‖ = 1 / 2')):
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
    comps = dict(COMPONENTS, HEAD38=COMPONENTS['HEAD38'].replace('i.2 = 3', 'i.2 = 2', 1))
    dmuts += 1
    if not duality_ok(PROPS, comps):
        bad.append('duality mutation head-drift: accepted')
    comps = dict(COMPONENTS, ESCAPE=COMPONENTS['ESCAPE'].replace('‖u - 1‖ < ε', '‖u - 1‖ < 2 * ε', 1))
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
        '\ntheorem a38_shared_x', '\nvariable (h : False)\ntheorem a38_shared_x')}), dl),
        'module:forbidden-command')
    mut('second-open', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '\ntheorem a38_shared_x', '\nopen Classical in\ntheorem a38_shared_x')}), dl), 'module:open')
    mut('second-import', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '/-! synthetic -/', 'import Mathlib.GroupTheory.SemidirectProduct\n/-! synthetic -/')}), dl),
        'module:forbidden-command')
    mut('sorry', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'sorry', 1)}), dl),
        'module:forbidden-token')
    mut('native-decide', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('exact test', 'native_decide', 1)}), dl),
        'module:forbidden-token')
    mut('print-axioms-dropped', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        '#print axioms a38_witness\n', '')}), dl), 'module:no-print-axioms')
    mut('stray-theorem-name', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a38_n : True := trivial\n#print axioms a38_n\n' + E_)}), dl),
        'module:theorem-name-outside')
    mut('verdict-weakened', PV, modstmt(PV, 'a38_witness', PROPS['P_R'].replace(
        '\n  ∧ (' + COMPONENTS['EXCL_t3'] + ')', '', 1)), 'module:statement-not-frozen:a38_witness')
    mut('not-verdict-weakened', FL, modstmt(FL, 'a38_not_witness', PROPS['P_N'].replace(
        '¬ (' + COMPONENTS['REAL'] + ')', '(' + COMPONENTS['REAL'] + ')', 1)), 'module:statement-not-frozen:a38_not_witness')
    mut('exclusion-weakened', PV, modstmt(PV, 'a38_shared_excl_k1', PROPS['EXCL_k1'].replace(
        '→ u = 1)', '→ True)', 1)), 'module:statement-not-frozen:a38_shared_excl_k1')
    mut('exclusion-orientation-dropped', PV, modstmt(PV, 'a38_shared_excl_t3', PROPS['EXCL_t3'].replace(
        'ᵀ) → u = 1)', 'ᵀ) → True)', 1)), 'module:statement-not-frozen:a38_shared_excl_t3')
    mut('exclusion-unit-dropped', PV, modstmt(PV, 'a38_shared_excl_e1', PROPS['EXCL_e1'].replace(
        '∀ u : ℂ, star u * u = 1 →', '∀ u : ℂ, u = 1 →', 1)), 'module:statement-not-frozen:a38_shared_excl_e1')
    mut('frozen-class-exclusion-weakened', PV, modstmt(PV, 'a38_shared_excl_t1', PROPS['EXCL_t1'].replace(
        'Hu u = dita28 X Y D) → u = 1)', 'Hu u = dita28 X Y D) → u = u)', 1)), 'module:statement-not-frozen:a38_shared_excl_t1')
    mut('realizability-flatness-dropped', PV, modstmt(PV, 'a38_shared_realizable', PROPS['REAL'].replace(
        ' ∧ (∀ i j, ‖Hu u i j‖ = 1 / 4)', '', 1)), 'module:statement-not-frozen:a38_shared_realizable')
    mut('realizability-unit-dropped', PV, modstmt(PV, 'a38_shared_realizable', PROPS['REAL'].replace(
        '∀ u : ℂ, star u * u = 1 →', '∀ u : ℂ, u = 1 →', 1)), 'module:statement-not-frozen:a38_shared_realizable')
    mut('escape-neighbourhood-dropped', PV, modstmt(PV, 'a38_c_local_escape', PROPS['ESCAPE'].replace(
        ' ∧ ‖u - 1‖ < ε ∧ (∀ i j, ‖Hu u i j - SIG i j‖ < ε)', '', 1)), 'module:statement-not-frozen:a38_c_local_escape')
    mut('escape-nontriviality-dropped', PV, modstmt(PV, 'a38_c_local_escape', PROPS['ESCAPE'].replace(
        ' ∧ u ≠ 1 ∧ ', ' ∧ ', 1)), 'module:statement-not-frozen:a38_c_local_escape')
    mut('escape-form-dropped', PV, modstmt(PV, 'a38_c_local_escape', PROPS['ESCAPE'].replace(
        '\n    ∧ ¬ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Hu u = ditat3 X Y D)', '', 1)), 'module:statement-not-frozen:a38_c_local_escape')
    mut('base-identity-dropped', FL, modstmt(FL, 'a38_control_base', PROPS['BASE'].replace(
        'Hu 1 = SIG ∧ ', '', 1)), 'module:statement-not-frozen:a38_control_base')
    mut('base-factorization-trivialized', FL, modstmt(FL, 'a38_control_base', PROPS['BASE'].replace(
        'SIG = ditak1 (F4 z) (fun _ => F4 w) (fun _ _ => (1 : ℂ))', 'SIG = SIG', 1)), 'module:statement-not-frozen:a38_control_base')
    for nm, _ in REQUIRED[PV]:
        mut('required-absent:' + nm, PV, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(PV, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    for nm, _ in REQUIRED[FL]:
        mut('required-absent-fails:' + nm, FL, lambda fe, dl, nm=nm: (dict(fe, **{MODULE: _module(FL, drop=(nm,))}), dl),
            'module:required-statement-absent:' + nm)
    mut('corollary-absent', X, lambda fe, dl: (dict(fe, **{MODULE: _module(X, drop=('a38_c_exclusive',))}), dl),
        'module:required-corollary-absent')
    mut('corollary-altered', X, lambda fe, dl: (dict(fe, **{MODULE: _module(
        X, stmt={'a38_c_exclusive': corollary_statement()[2:].replace('→ ¬ (', '→ (', 1)})}), dl),
        'module:statement-not-frozen:a38_c_exclusive')
    mut('both-labels', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a38_not_witness :\n    ' + PROPS['P_N'] + ' := by\n  exact test\n'
        '#print axioms a38_not_witness\n' + E_)}), dl), 'module:both-labels')
    mut('note-outcome-mismatch', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '**Outcome:** `A38-NON-DITA-WITNESS-PROVED`', '**Outcome:** `A38-WITNESS-FAILS`')}), dl), 'note:outcome-line')
    mut('note-second-outcome', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n**Outcome:** `A38-NON-DITA-WITNESS-PROVED`\n'}), dl), 'note:outcome-line')
    mut('note-sentence-altered', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        'evidence level 2', 'evidence level 3', 1)}), dl), 'note:frozen-sentence')
    mut('note-unearned-sentence', X, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + SENTENCES[PV] + '\n'}), dl), 'note:sentence-of-a-label-not-earned')
    mut('note-clause-twice', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md']
        + '\n' + CLAUSE + '\n'}), dl), 'note:the-clause')
    mut('note-clause-detached', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        ' — the result note.**\n', ' — the result note.**\n' + 'x ' * 60 + '\n', 1)}), dl), 'note:the-clause')
    mut('note-control-unnamed', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a38_control_base`', 'x')}), dl), 'note:required-statement-not-named')
    mut('note-structural-unnamed', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a38_c_local_escape`', 'x')}), dl), 'note:required-statement-not-named')
    mut('note-probe-line-absent', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        'dita_local_escape_probe: OK', 'dita_local_escape_probe: ran')}), dl), 'note:probe-summary-line-absent')
    mut('roadmap-wrong-case', PV, lambda fe, dl: (dict(fe, **{ROADMAP: expected_roadmap(fd[ROADMAP], FL)}), dl),
        'roadmap:')
    mut('roadmap-standing-dropped', PV, lambda fe, dl: (dict(fe, **{ROADMAP: fe[ROADMAP].replace(
        P0_CASE[PV] + ' ' + P0_STANDING_38, P0_CASE[PV])}), dl), 'roadmap:')
    mut('roadmap-sentence-misplaced', PV, lambda fe, dl: (dict(fe, **{ROADMAP: fd[ROADMAP].replace(
        ' Act 25 a.', ' Act 25 a. ' + P0_CASE[PV] + ' ' + P0_STANDING_38, 1)}), dl), 'roadmap:')
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
        'A38-NON-DITA-WITNESS-PROVED.', 'A38-WITNESS-FAILS.')}), dl), 'census:outcome')
    mut('census-entry-absent', PV, lambda fe, dl: (dict(fe, **{CENSUS: fd[CENSUS]}), dl), 'census:family-count-or-place')
    mut('wire-absent', PV, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT]}), dl), 'wire:')
    mut('wire-misplaced', PV, lambda fe, dl: (dict(fe, **{ROOT: fd[ROOT] + WIRE}), dl), 'wire:')
    mut('workflow-probe-not-wired', PV, lambda fe, dl: (dict(fe, **{WORKFLOW: fd[WORKFLOW]}), dl), 'workflow:')
    mut('workflow-extra-change', PV, lambda fe, dl: (dict(fe, **{WORKFLOW: fe[WORKFLOW] + '\n'}), dl), 'workflow:')
    mut('workflow-shard-not-required', PV, lambda fe, dl: (dict(fe, **{WORKFLOW: fe[WORKFLOW].replace('          test "${A38_RESULT}" = success\n', '', 1)}), dl), 'workflow:')
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
text = HEADER % (json.dumps(PROBE_BLOB), json.dumps(P['OPEN'], ensure_ascii=False), json.dumps(A37_HEAD, ensure_ascii=False),
                 lit(P['PROPS']), lit(P['COMPONENTS']), json.dumps(P['THEOREMS'], ensure_ascii=False, indent=1),
                 lit(SENT), json.dumps(CLAUSE, ensure_ascii=False), json.dumps(P0_END_D, ensure_ascii=False),
                 lit(P0_CASE), json.dumps(P0_STANDING_38, ensure_ascii=False)) + BODY + SELFTEST
os.makedirs(os.path.join(S, 'rec'), exist_ok=True)
open(os.path.join(S, 'rec', 'controls.py'), 'w', encoding='utf-8').write(text)
json.dump({'SENTENCES': SENT, 'CLAUSE': CLAUSE, 'P0_END_D': P0_END_D, 'P0_CASE': P0_CASE, 'P0_STANDING_38': P0_STANDING_38},
          open(os.path.join(S, 'texts38.json'), 'w'), ensure_ascii=False, indent=1)
print('controls.py written', len(text))
