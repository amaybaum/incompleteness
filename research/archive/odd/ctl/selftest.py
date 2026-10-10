ODDK_DEF = 'def oddK (k : ℕ) (μ : Fin (2 * k + 1 + 1)) : Bool := decide (k < (μ : ℕ))'
FRAME_HEAD = ('theorem gRev_frame (k : ℕ) (a b : Fin 2) :\n'
              '    gRev k (prodState (corner (zK k) a) (corner (zK k) b)) =\n'
              '      prodState (corner (zK k) a) (corner (zK k) (a + b)) := by')
REL_HEAD = 'theorem gateRel_gRev (k : ℕ) : GateRel (nK k) (gRev k) :='
ISNOT_HEAD = 'theorem isNot_nK (k : ℕ) : IsNot (eball (2 * k + 1)) (zK k) (nK k) where'
SECA_PROOF = '  have hμ := μ.isLt\n    have hν := ν.isLt\n    have hr : ((Fin.rev μ : Fin (2 * k + 1 + 1)) : ℕ) = ' \
             '2 * k + 1 - μ := by\n      rw [Fin.val_rev]; omega\n    simp only [gRev_apply, sgate, prodState_apply, ' \
             'hom_smul_zK'
ODD_FRAME = ('      IsNot (eball d) z N ∧\n'
             '        (∀ a b : Fin 2,\n'
             '          G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) ∧\n'
             '        GateRel N G) ↔ Odd d := by')
ODD_D1 = '      exact ⟨z1, neg1, cnot1, isNot_neg1, cnot1_frame, gateRel_of_nativeGate nativeGate_cnot1⟩'
ODD_FWD = '    exact Nat.not_even_iff_odd.mp (not_even_of_gateRel hN hR)'
VALUE_HEAD = ('theorem gRev_value (k : ℕ) (hk : 1 ≤ k) :\n'
              '    prodEffVal (sharpEff (wK k)) (sharpEff (zK k)) (gRev k (prodState (xK k) (zK k))) = -1 / 10 := by')
WK_DEF = ('noncomputable def wK (k : ℕ) : Fin (2 * k + 1) → ℝ := fun i =>\n'
          '  if (i : ℕ) = 2 * k - 1 then -3 / 5 else if (i : ℕ) = 2 * k then -4 / 5 else 0')
PF = ('theorem not_posFwd_gRev (k : ℕ) (hk : 1 ≤ k) :\n'
      '    ¬ ∀ x ∈ eball (2 * k + 1), ∀ y ∈ eball (2 * k + 1),\n'
      '      gRev k (prodState x y) ∈ maxCone (eball (2 * k + 1)) :=\n'
      '  fun h => gRev_not_mem_maxCone k hk\n'
      '    (h _ (mem_eball_of_sphere (sum_xK_sq k)) _ (mem_eball_of_sphere (sum_zK_sq k)))')
NG = ('theorem not_nativeGate_gRev (k : ℕ) (hk : 1 ≤ k) :\n'
      '    ¬ NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k) :=\n'
      '  fun hG => not_posFwd_gRev k hk hG.posFwd')
NOTE_OK = ('The frame and both relations admit exactly the odd dimensions. For every odd dimension at least 3, an '
           'explicit member of this family fails forward positivity. Combined with DIM-1, the positivity assumptions '
           'are therefore collectively load-bearing for excluding the higher odd dimensions.')


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    landed = landed_at_d()
    check('T', 'the landed texts read from D are the frozen ones', landed == LANDED and len(LANDED) == 17)
    module_checks(mod, ' [reference]')
    a, b, c = verdict_of(mod)
    check('T', 'the reference module reads %s, %s and %s' % (a, b, c),
          a == [FAM_TOKENS[0]] and b == [ODD_TOKENS[0]] and c == [POS_TOKENS[0]])
    # N1-N3
    must_fail('N1', 'a renamed declaration', replace_once(mod, '\ntheorem sum_xK_sq ', '\ntheorem sum_xK_sq\' '))
    must_fail('N2', 'a changed binder context', replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {m : ℕ}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, 'CompositeDimension EffectSpace ParityNot\n',
                                                       'CompositeDimension EffectSpace\n'))
    must_fail('N3', 'a sorry', append_end(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', replace_once(mod, '#print axioms OIBridge.OddChar.gRev_value\n', ''))
    # S1 -- the family
    must_fail('S1', 'the sign classes changed', replace_once(mod, ODDK_DEF, ODDK_DEF.replace('k <', 'k ≤')))
    must_fail('S1', 'the frame changed', replace_once(mod, FRAME_HEAD, FRAME_HEAD.replace('(zK k) (a + b))', '(zK k) b)')))
    must_fail('S1', 'the relations weakened to the target relation',
              replace_once(mod, REL_HEAD, REL_HEAD.replace('GateRel (nK k) (gRev k)',
                                                           '∀ ω, actT (nK k) (gRev k (actT (nK k) ω)) = gRev k ω')))
    must_fail('S1', 'the NOT with another axis',
              replace_once(mod, ISNOT_HEAD, ISNOT_HEAD.replace('(zK k) (nK k)', '(xK k) (nK k)')))
    must_fail('S1', 'a §A proof reading positivity',
              replace_once(mod, SECA_PROOF, SECA_PROOF.replace(
                  '  have hμ := μ.isLt', '  have _hp : maxCone (eball 1) = maxCone (eball 1) := rfl\n    have hμ := μ.isLt')))
    m = replace_once(mod, FRAME_HEAD, FRAME_HEAD.replace('(zK k) (a + b))', '(zK k) b)'))
    check('M', 'decision rule: a broken family frame reads ODD-FAMILY-NOT-ESTABLISHED and '
               'HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED and leaves the characterization',
          verdict_of(m) == ([FAM_TOKENS[1]], [ODD_TOKENS[0]], [POS_TOKENS[1]]))
    m = replace_once(mod, ISNOT_HEAD, ISNOT_HEAD.replace('(zK k) (nK k)', '(xK k) (nK k)'))
    check('M', 'decision rule: a broken NOT reads ODD-FAMILY-NOT-ESTABLISHED and leaves the other cells',
          verdict_of(m) == ([FAM_TOKENS[1]], [ODD_TOKENS[0]], [POS_TOKENS[0]]))
    lm = dict(LANDED)
    lm['GateRel#relC'] = lm['GateRel#relC'].replace('actT N (G ω)', 'G ω')
    check('M', 'relations: a landed GateRel that differs from the landed NativeGate relations fails all three cells',
          verdict_of(mod, lm) == ([FAM_TOKENS[1]], [ODD_TOKENS[1]], [POS_TOKENS[1]]))
    lm = dict(LANDED)
    lm['sgate_relC'] = lm['sgate_relC'].replace('(hodd : ∀ μ, odd (p μ) = !odd μ) ', '')
    check('M', 'family: a landed sgate relation lemma that differs fails only the family cell',
          verdict_of(mod, lm) == ([FAM_TOKENS[1]], [ODD_TOKENS[0]], [POS_TOKENS[0]]))
    # S2 -- the characterization
    must_fail('S2', 'the frame dropped from the existential',
              replace_once(mod, ODD_FRAME, ODD_FRAME.replace(
                  '        (∀ a b : Fin 2,\n'
                  '          G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b))) ∧\n', '')))
    must_fail('S2', 'forward positivity added to the existential',
              replace_once(mod, ODD_FRAME, ODD_FRAME.replace(
                  '        GateRel N G) ↔', '        GateRel N G ∧ (∀ x ∈ eball d, ∀ y ∈ eball d, '
                                             'G (prodState x y) ∈ maxCone (eball d))) ↔')))
    must_fail('S2', 'the equivalence weakened to one direction',
              replace_once(mod, ODD_FRAME, ODD_FRAME.replace('GateRel N G) ↔ Odd d', 'GateRel N G) → Odd d')))
    must_fail('S2', 'the right side strengthened', replace_once(mod, ODD_FRAME, ODD_FRAME.replace('↔ Odd d', '↔ Odd d ∧ 3 ≤ d')))
    must_fail('S2', 'd = 1 through gRev 0 instead of the landed cnot1',
              replace_once(mod, ODD_D1, '      exact ⟨zK 0, nK 0, gRev 0, isNot_nK 0, gRev_frame 0, gateRel_gRev 0⟩'))
    must_fail('S2', 'the forward direction not through the landed parity theorem',
              replace_once(mod, ODD_FWD, '    exact Nat.not_even_iff_odd.mp (fun h => absurd h sorry)'))
    m = replace_once(mod, ODD_FRAME, ODD_FRAME.replace('GateRel N G) ↔ Odd d', 'GateRel N G) → Odd d'))
    check('M', 'decision rule: a broken characterization reads ODD-CHARACTERIZATION-NOT-ESTABLISHED and leaves the '
               'other cells', verdict_of(m) == ([FAM_TOKENS[0]], [ODD_TOKENS[1]], [POS_TOKENS[0]]))
    lm = dict(LANDED)
    lm['not_even_of_gateRel'] = lm['not_even_of_gateRel'].replace('¬ Even d', 'Odd d')
    check('M', 'characterization: a landed parity theorem that differs fails only the characterization cell',
          verdict_of(mod, lm) == ([FAM_TOKENS[0]], [ODD_TOKENS[1]], [POS_TOKENS[0]]))
    lm = dict(LANDED)
    lm['cnot1_frame'] = lm['cnot1_frame'].replace('(corner z1 (a + b))', '(corner z1 b)')
    check('M', 'characterization: a landed d = 1 frame that differs fails only the characterization cell',
          verdict_of(mod, lm) == ([FAM_TOKENS[0]], [ODD_TOKENS[1]], [POS_TOKENS[0]]))
    # S3 -- positivity at k >= 1
    must_fail('S3', 'the value changed to a sign', replace_once(mod, VALUE_HEAD, VALUE_HEAD.replace('= -1 / 10', '< 0')))
    must_fail('S3', 'the witness direction changed', replace_once(mod, WK_DEF, WK_DEF.replace('-4 / 5', '4 / 5')))
    must_fail('S3', 'the positivity failure weakened to one input',
              replace_once(mod, PF, 'theorem not_posFwd_gRev (k : ℕ) (hk : 1 ≤ k) :\n'
                                    '    ¬ gRev k (prodState (xK k) (zK k)) ∈ maxCone (eball (2 * k + 1)) :=\n'
                                    '  gRev_not_mem_maxCone k hk'))
    must_fail('S3', 'the range k >= 1 dropped',
              replace_once(mod, VALUE_HEAD, VALUE_HEAD.replace('(k : ℕ) (hk : 1 ≤ k)', '(k : ℕ)')))
    must_fail('S3', 'the failure read from a landed dimension corollary',
              replace_once(mod, NG, 'theorem not_nativeGate_gRev (k : ℕ) (hk : 1 ≤ k) :\n'
                                    '    ¬ NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k) :=\n'
                                    '  fun hG => by have := dim_of_nativeGate (isNot_nK k) hG; omega'))
    m = replace_once(mod, VALUE_HEAD, VALUE_HEAD.replace('= -1 / 10', '< 0'))
    check('M', 'decision rule: a broken value reads HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED and leaves the other '
               'cells', verdict_of(m) == ([FAM_TOKENS[0]], [ODD_TOKENS[0]], [POS_TOKENS[1]]))
    lm = dict(LANDED)
    lm['NativeGate#posFwd'] = lm['NativeGate#posFwd'].replace('maxCone Ω', 'jointStates Ω')
    check('M', 'positivity: a landed posFwd that differs fails only the positivity cell',
          verdict_of(mod, lm) == ([FAM_TOKENS[0]], [ODD_TOKENS[0]], [POS_TOKENS[1]]))
    lm = dict(LANDED)
    lm['NativeGate#frame'] = lm['NativeGate#frame'].replace('(corner z (a + b))', '(corner z b)')
    check('M', 'frame: a landed frame field that differs fails all three cells',
          verdict_of(mod, lm) == ([FAM_TOKENS[1]], [ODD_TOKENS[1]], [POS_TOKENS[1]]))
    # S6 -- scope
    must_fail('S6', 'inverse positivity read as a projection',
              append_end(mod, 'theorem inv_pos (k : ℕ) (hG : NativeGate (eball (2 * k + 1)) (zK k) (nK k) (gRev k)) :\n'
                              '    True := by have := hG.posInv; trivial'))
    must_fail('S6', 'a dimension conclusion', append_end(mod, 'theorem d_sel {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} '
                                                           '{G : W d ≃ₗ[ℝ] W d} (h : GateRel N G) : d ≠ 2 := sorry'))
    must_fail('S6', 'a positive native gate', append_end(mod, 'theorem pos_gate : NativeGate (eball 3) (zK 1) (nK 1) '
                                                            '(gRev 1) := sorry'))
    must_fail('S6', 'a complex field', append_end(mod, 'theorem cplx : (Complex.I : ℂ) = Complex.I := rfl'))
    # S7 -- reuse
    must_fail('S7', 'a landed definition re-declared', append_end(mod, 'def sgate : ℕ := 0'))
    must_fail('S7', 'a second import',
              replace_once(mod, 'import OIBridge.ParityNot\n', 'import OIBridge.ParityNot\nimport OIBridge.K2Guard\n'))
    # S8 -- phrases
    must_fail('S8', 'a forbidden phrase in the header',
              replace_once(mod, '  (C) Positivity.', '  Forward positivity is individually necessary. (C) Positivity.'))
    must_fail('S8', 'the design header', replace_once(mod, 'round ODD-CHAR-1:', 'design (round ODD-CHAR-1, not for landing):'))
    check('M', 'the result-note phrase test passes the frozen wording and fails each individual-necessity claim',
          not phrase_hits(NOTE_OK)
          and phrase_hits('Hence posFwd is necessary.') == ['posFwd is necessary']
          and phrase_hits('so inverse positivity alone\nexcludes them') == ['inverse positivity alone']
          and phrase_hits('Each of posFwd and posInv is individually necessary.') == ['individually necessary'])
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.OddChar.not_nativeGate_gRev\n',
                           '#print axioms OIBridge.OddChar.not_nativeGate_gRev\n'
                           '#print axioms OIBridge.OddChar.sum_xK_sq\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.OddChar.gRev_value\n',
                           '#print axioms OIBridge.OddChar.gRev_value\n#print axioms OIBridge.OddChar.gRev_value\n'))
    # V
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('ODD-FAMILY-PROVED, ODD-CHARACTERIZATION-PROVED and HIGHER-ODD-POSFWD-FAILURE-PROVED.')
          == ['ODD-FAMILY-PROVED', 'ODD-CHARACTERIZATION-PROVED', 'HIGHER-ODD-POSFWD-FAILURE-PROVED']
          and note_tokens('HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED') == ['HIGHER-ODD-POSFWD-FAILURE-NOT-ESTABLISHED'])
    # I, C
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    good = census_want(d_cen)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['modules'] == PREV_FAMILY_MODULES][0]
    bad_status = json.loads(good)
    bad_status['families'][k + 1]['status'] = 'carried'
    bad_status = json.dumps(bad_status, indent=2, ensure_ascii=False) + '\n'
    moved = json.loads(good)
    moved['families'].insert(k, moved['families'].pop(k + 1))
    moved = json.dumps(moved, indent=2, ensure_ascii=False) + '\n'
    check('M', 'census: the frozen edit passes; a changed status, a moved family, a whitespace change and the '
               'unchanged file fail',
          census_ok(d_cen, good) and not census_ok(d_cen, bad_status) and moved != good
          and not census_ok(d_cen, moved) and not census_ok(d_cen, good.replace('\n', '\n ', 1))
          and not census_ok(d_cen, d_cen))


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) == 2 and argv[0] == 'verdict':
        print_verdicts(argv[1])
    elif len(argv) >= 2 and argv[0] == 'check':
        freeze = argv[3] if len(argv) == 4 and argv[2] == '--freeze' else None
        run_check(argv[1], freeze)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
