"""Derive A40's self-test from A39's by explicit, asserted replacements."""
import os
S = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(S, '..', 'a39', '_selftest39.txt'), encoding='utf-8').read()
def rep(s, old, new, cnt=1):
    assert s.count(old) == cnt, (old[:80], s.count(old))
    return s.replace(old, new)
t = rep(t, """        for k, v in PROPS.items():
            if norm(v) not in n:
                bad.append('agreement: proposition %s not in the preregistration' % k)""", """        if norm(COMPONENTS['HEAD']) not in n:
            bad.append('agreement: the head not in the preregistration')
        for k, v in PROPS.items():
            if not v.startswith(COMPONENTS['HEAD']) or norm(v[len(COMPONENTS['HEAD']):]) not in n:
                bad.append('agreement: proposition %s not in the preregistration as the head followed by its body' % k)""")
t = rep(t, "('standing-39', P0_STANDING_39)", "('standing-40', P0_STANDING_40)")
t = rep(t, "for b in (ROADMAP_BLOB_D, GUARD_BLOB_D, WORKFLOW_BLOB_D, PROBE_BLOB, D):", "for b in (ROADMAP_BLOB_D, GUARD_BLOB_D, WORKFLOW_BLOB_D, PROBE_BLOB, MODULE_BLOB, D):")
i = t.index('    for nm, key, old, new in ('); j = t.index('    fd = _synthetic_d()')
t = t[:i] + '''    for nm, key, old, new in (
            ('P_R-face-weakened', 'P_R', '(' + COMPONENTS['FACE_2p'] + ')', '(True)'),
            ('P_R-exclusion-weakened', 'P_R', '(' + COMPONENTS['EXCL_mc_c'] + ')', '(True)'),
            ('P_N-negation-dropped', 'P_N', '¬ (' + COMPONENTS['FACE_1p'] + ')', '(' + COMPONENTS['FACE_1p'] + ')'),
            ('face-moved-to-the-absent-face', 'FACE_2p', 'H3 u₁ 1 u₃', 'H3 u₁ (-1) u₃'),
            ('face-orientation-dropped', 'FACE_3p', '(dita28 X Y D)ᵀ', 'dita28 X Y D'),
            ('face-flatness-dropped', 'FACE_1m', 'flg X ∧ ', ''),
            ('exclusion-conclusion-weakened', 'EXCL_k1_c', '→ u₂ = 1 ∧ u₃ = 1', '→ u₂ = 1'),
            ('exclusion-value-flipped', 'EXCL_mc_c', '→ u₁ = -1', '→ u₁ = 1'),
            ('exclusion-unit-dropped', 'EXCL_t1_c', 'star u₂ * u₂ = 1 →', 'u₂ = 1 →')):
        props = dict(PROPS)
        if props[key].count(old) < 1:
            bad.append('duality mutation %s: pattern absent' % nm)
            continue
        props[key] = props[key].replace(old, new, 1)
        dmuts += 1
        if not duality_ok(props, COMPONENTS):
            bad.append('duality mutation %s: accepted' % nm)
    for nm, comp, old, new in (
            ('head-drift-act-36', 'HEAD39', '3599 / 3601 + (120 / 3601) * Complex.I', '3599 / 3600 + (120 / 3601) * Complex.I'),
            ('head-drift-act-39', 'HEAD39', 'i.2 = 3', 'i.2 = 2'),
            ('head-drift-act-40', 'HEAD40', 'let rmc', 'let rmc '),
            ('component-drift-face', 'FACE_3m', 'H3 u₁ u₂ (-1)', 'H3 u₁ u₂ 1'),
            ('component-drift-exclusion', 'EXCL_mr_r', '→ u₃ = -1', '→ u₃ = 1')):
        if COMPONENTS[comp].count(old) < 1:
            bad.append('duality mutation %s: pattern absent' % nm)
            continue
        comps = dict(COMPONENTS, **{comp: COMPONENTS[comp].replace(old, new, 1)})
        dmuts += 1
        if not duality_ok(PROPS, comps):
            bad.append('duality mutation %s: accepted' % nm)

''' + t[j:]
t = rep(t, "    EXPECTED_PROBE_BLOB[0] = blob_id('# synthetic probe\\n')\n",
        "    EXPECTED_PROBE_BLOB[0] = blob_id('# synthetic probe\\n')\n    EXPECTED_MODULE_BLOB[0] = blob_id(_module(ROWS[0]))\n")
t = rep(t, '\\ntheorem a39_shared_x', '\\ntheorem a40_shared_x', 4)
t = rep(t, "'#print axioms a39_realizable\\n'", "'#print axioms a40_locus_kernel\\n'")
t = rep(t, "E_, 'theorem a39_n : True := trivial\\n#print axioms a39_n\\n' + E_", "E_, 'theorem a40_n : True := trivial\\n#print axioms a40_n\\n' + E_")
i = t.index("    mut('verdict-weakened', PV,"); j = t.index("    for nm, _ in REQUIRED[PV]:")
t = t[:i] + '''    mut('note-module-blobs-absent', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`' + EXPECTED_MODULE_BLOB[0] + '`', 'x')}), dl), 'note:module-blobs-not-reported')
    mut('module-departure-unreported', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace('/-! synthetic -/', '/-! synthetic, repaired -/'),
        RDIR + 'result.md': fe[RDIR + 'result.md'].replace('`' + EXPECTED_MODULE_BLOB[0] + '`.', '`' + EXPECTED_MODULE_BLOB[0] + '`; the module at E is `'
        + blob_id(fe[MODULE].replace('/-! synthetic -/', '/-! synthetic, repaired -/')) + '`.')}), dl),
        'note:departure-from-the-reference-implementation-not-reported')
    mut('verdict-weakened', PV, modstmt(PV, 'a40_locus_kernel', PROPS['P_R'].replace(
        '(' + COMPONENTS['EXCL_k2_r'] + ')', '(True)', 1)), 'module:statement-not-frozen:a40_locus_kernel')
    mut('not-verdict-weakened', FL, modstmt(FL, 'a40_not_locus_kernel', PROPS['P_N'].replace(
        '¬ (' + COMPONENTS['FACE_3m'] + ')', '(' + COMPONENTS['FACE_3m'] + ')', 1)), 'module:statement-not-frozen:a40_not_locus_kernel')
    mut('face-at-one-point', PV, modstmt(PV, 'a40_shared_face_2p', PROPS['FACE_2p'].replace(
        '∀ u₁ u₃ : ℂ, star u₁ * u₁ = 1 → star u₃ * u₃ = 1 →', '∀ u₁ u₃ : ℂ, u₁ = 1 → u₃ = 1 →', 1)), 'module:statement-not-frozen:a40_shared_face_2p')
    mut('face-moved-to-the-absent-face', PV, modstmt(PV, 'a40_shared_face_2p', PROPS['FACE_2p'].replace(
        'H3 u₁ 1 u₃', 'H3 u₁ (-1) u₃', 1)), 'module:statement-not-frozen:a40_shared_face_2p')
    mut('face-map-changed', PV, modstmt(PV, 'a40_shared_face_1m', PROPS['FACE_1m'].replace(
        'ditamc X Y D', 'ditat2 X Y D', 1)), 'module:statement-not-frozen:a40_shared_face_1m')
    mut('exclusion-weakened', PV, modstmt(PV, 'a40_shared_excl_k3_r', PROPS['EXCL_k3_r'].replace(
        '→ u₁ = 1 ∧ u₂ = 1 ∧ u₃ = 1', '→ u₁ = 1', 1)), 'module:statement-not-frozen:a40_shared_excl_k3_r')
    mut('exclusion-relaxed-to-true', PV, modstmt(PV, 'a40_shared_excl_mr_r', PROPS['EXCL_mr_r'].replace(
        '→ u₃ = -1', '→ True', 1)), 'module:statement-not-frozen:a40_shared_excl_mr_r')
''' + t[j:]
i = t.index("    mut('corollary-absent', X,"); j = t.index("    mut('note-outcome-mismatch', PV,")
t = t[:i] + '''    mut('corollary-absent', X, lambda fe, dl: (dict(fe, **{MODULE: _module(X, drop=('a40_c_exclusive',))}), dl),
        'module:required-corollary-absent')
    mut('corollary-altered', X, lambda fe, dl: (dict(fe, **{MODULE: _module(
        X, stmt={'a40_c_exclusive': corollary_statement()[2:].replace('→ ¬ (', '→ (', 1)})}), dl),
        'module:statement-not-frozen:a40_c_exclusive')
    mut('both-labels', PV, lambda fe, dl: (dict(fe, **{MODULE: fe[MODULE].replace(
        E_, 'theorem a40_not_locus_kernel :\\n    ' + PROPS['P_N'] + ' := by\\n  exact test\\n'
        '#print axioms a40_not_locus_kernel\\n' + E_)}), dl), 'module:both-labels')
''' + t[j:]
t = rep(t, "'**Outcome:** `A39-REALIZABLE-PROVED`', '**Outcome:** `A39-REALIZABLE-FAILS`'", "'**Outcome:** `A40-LOCUS-CLASSIFIED`', '**Outcome:** `A40-LOCUS-FAILS`'")
t = rep(t, "+ '\\n**Outcome:** `A39-REALIZABLE-PROVED`\\n'", "+ '\\n**Outcome:** `A40-LOCUS-CLASSIFIED`\\n'")
i = t.index("    mut('note-control-unnamed', PV,"); j = t.index("    mut('note-probe-line-absent', PV,")
t = t[:i] + '''    mut('note-face-unnamed', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a40_shared_face_3m`', 'x')}), dl), 'note:required-statement-not-named')
    mut('note-exclusion-unnamed', PV, lambda fe, dl: (dict(fe, **{RDIR + 'result.md': fe[RDIR + 'result.md'].replace(
        '`a40_shared_excl_mc_c`', 'x')}), dl), 'note:required-statement-not-named')
''' + t[j:]
t = rep(t, "'dita_torus_probe: OK', 'dita_torus_probe: ran'", "'dita_torus_locus_probe: OK', 'dita_torus_locus_probe: ran'")
t = rep(t, "P0_CASE[PV] + ' ' + P0_STANDING_39, P0_CASE[PV]", "P0_CASE[PV] + ' ' + P0_STANDING_40, P0_CASE[PV]")
t = rep(t, "' Act 25 a. ' + P0_CASE[PV] + ' ' + P0_STANDING_39", "' Act 25 a. ' + P0_CASE[PV] + ' ' + P0_STANDING_40")
t = rep(t, "'A39-REALIZABLE-PROVED.', 'A39-REALIZABLE-FAILS.'", "'A40-LOCUS-CLASSIFIED.', 'A40-LOCUS-FAILS.'")
i = t.index("    mut('workflow-probe-misplaced', PV,"); j = t.index("    mut('probe-altered', PV,")
t = t[:i] + '''    mut('workflow-shard-not-required', PV, lambda fe, dl: (dict(fe, **{WORKFLOW: fe[WORKFLOW].replace(
        '          test "${A40_RESULT}" = success\\n', '')}), dl), 'workflow:')
    mut('workflow-shard-not-in-needs', PV, lambda fe, dl: (dict(fe, **{WORKFLOW: fe[WORKFLOW].replace(
        'probes_a38, probes_a40, probes_foundations', 'probes_a38, probes_foundations')}), dl), 'workflow:')
    mut('workflow-probe-in-the-a38-shard', PV, lambda fe, dl: (dict(fe, **{WORKFLOW: fe[WORKFLOW].replace(
        '  probes_a40:\\n', '  probes_a38b:\\n')}), dl), 'workflow:')
''' + t[j:]
t = rep(t, "    EXPECTED_PROBE_BLOB[0] = PROBE_BLOB\n", "    EXPECTED_PROBE_BLOB[0] = PROBE_BLOB\n    EXPECTED_MODULE_BLOB[0] = MODULE_BLOB\n")
t = rep(t, "mut('path-missing-probe', PV, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items() if k != PROBE)), 'paths:')",
        "mut('path-missing-probe', PV, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items() if k != PROBE)), 'paths:')\n"
        "    mut('path-missing-module', PV, lambda fe, dl: (fe, dict((k, v) for k, v in dl.items() if k != MODULE)), 'paths:')")
t = rep(t, "    PV, FL, X = ROWS\n", """    # a proof-only departure from the reference implementation, reported in the note, holds
    fe, delta = _synthetic_e(fd, ROWS[0])
    m2 = fe[MODULE].replace('/-! synthetic -/', '/-! synthetic, repaired -/')
    r = check_all(fd, dict(fe, **{MODULE: m2, RDIR + 'result.md': _note(ROWS[0], blob_id(m2))}), delta)
    if r:
        bad.append('positive reported departure: %s' % r)
    PV, FL, X = ROWS
""")
assert 'a39' not in t and 'A39' not in t and 'dita_torus_probe' not in t and '_39' not in t, [l for l in t.split('\n') if 'a39' in l or 'A39' in l or '_39' in l]
open(os.path.join(S, '_selftest40.txt'), 'w', encoding='utf-8').write(t)
print('ok')
