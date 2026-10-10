DEF_TAIL = 'y ∈ closure ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)\n'
QN_HEAD = ('theorem boundary_qnorm_const_of_dense {Ω : Set (Fin d → ℝ)} (hc : IsCompact Ω)\n'
           '    (hi : (interior Ω).Nonempty) {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
           '    (hG : PreservesBody Ω G) (hT : DenseBoundaryOrbit Ω G) :\n'
           '    ∃ R : ℝ, 0 ≤ R ∧ ∀ x, IsBoundaryState Ω x → qnorm Ω (x - centroid Ω) = R ^ 2 := by')
CONE_HEAD = ('theorem maxConeOf_avail_eq_of_dense (hd : 0 < d) (hG : PreservesBody (eball d) G)\n'
             '    (hP1 : SharpSeed (eball d) r) (hK : DenseBoundaryOrbit (eball d) G)\n'
             '    (hV4 : SeedOrbitAvailable G r avail) (hE : EffectsOn (eball d) avail) :\n'
             '    maxConeOf avail = maxCone (eball d) := by')
ENT_HEAD = ('    {T : W d ≃ₗ[ℝ] W d} (hEnt : EntanglingOf (eball d) avail T) : Entangling (eball d) T :=\n')
WEAK_HEAD = '    {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hT : BoundaryTransitive Ω G) : DenseBoundaryOrbit Ω G := by'
NOGO_PROOF = '  not_boundaryTransitive_of_countable countable_ratRefl\n'
CHART_HEAD = 'theorem chartBody_eq_eball_of_dense {D : DirectedStages} (C : CompletionChart D) (hd : 0 < C.d)'
CONE_VARS = '  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n\n/-- **The available family'
OPEN_LINE = '  CompletionAction InvariantInnerProduct TransitiveBody CompositeDimension CompositeInterface\n'


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    landed = landed_at_d()
    check('T', 'the landed statements read from D are the frozen ones', landed == LANDED and len(LANDED) == 14)
    module_checks(mod, ' [reference]')
    a, b, c = verdict_of(mod)
    check('T', 'the reference module reads %s, %s and %s' % (a, b, c),
          a == [BALL_TOKENS[0]] and b == [CONE_TOKENS[0]] and c == [STRICT_TOKENS[0]])
    # N1-N3
    must_fail('N1', 'a renamed declaration',
              replace_once(mod, '\ntheorem countable_ratRefl :', '\ntheorem countable_ratRefl\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, CONE_VARS, '  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} {x : ℕ}\n\n/-- **The available family'))
    must_fail('N2', 'a changed open line', replace_once(mod, '\nopen EffectSpace K1Bridge K2Guard\n',
                                                       '\nopen EffectSpace K1Bridge\n'))
    must_fail('N3', 'a sorry', append_strict(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed',
              replace_once(mod, '#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense\n', ''))
    # S1
    must_fail('S1', 'the orbit closure replaced by the orbit itself',
              replace_once(mod, DEF_TAIL, 'y ∈ ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)\n'))
    must_fail('S1', 'the orbit closure replaced by the orbit\'s interior',
              replace_once(mod, DEF_TAIL, 'y ∈ interior ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)\n'))
    # S2 -- the pairing, load-bearing
    must_fail('S2', 'a ball conclusion changed (0 ≤ R to 0 < R)',
              replace_once(mod, QN_HEAD, QN_HEAD.replace('0 ≤ R ∧', '0 < R ∧')))
    must_fail('S2', 'a ball hypothesis added',
              replace_once(mod, QN_HEAD, QN_HEAD.replace('(hc : IsCompact Ω)', '(hc : IsCompact Ω) (hconv : Convex ℝ Ω)')))
    must_fail('S2', 'a dense theorem keeping exact transitivity',
              replace_once(mod, QN_HEAD, QN_HEAD.replace('DenseBoundaryOrbit Ω G', 'BoundaryTransitive Ω G')))
    must_fail('S2', 'both hypotheses carried',
              replace_once(mod, QN_HEAD, QN_HEAD.replace('(hT : DenseBoundaryOrbit Ω G)',
                                                         '(hT : DenseBoundaryOrbit Ω G) (hB : BoundaryTransitive Ω G)')))
    must_fail('S2', 'a cone hypothesis dropped',
              replace_once(mod, CONE_HEAD, CONE_HEAD.replace(' (hE : EffectsOn (eball d) avail)', '')))
    must_fail('S2', 'a cone conclusion weakened to an inclusion',
              replace_once(mod, CONE_HEAD, CONE_HEAD.replace('maxConeOf avail = maxCone', 'maxConeOf avail ⊆ maxCone')))
    must_fail('S2', 'a selector conclusion changed',
              replace_once(mod, ENT_HEAD, ENT_HEAD.replace(': Entangling (eball d) T', ': True')))
    must_fail('S2', 'a section variable changed under the cone theorems',
              replace_once(mod, CONE_VARS, '  {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} {d : ℕ}\n\n/-- **The available family'))
    must_fail('S2', 'the chart theorem\'s completion data made implicit',
              replace_once(mod, CHART_HEAD, CHART_HEAD.replace('(C : CompletionChart D)', '{C : CompletionChart D}')))
    lm = dict(LANDED)
    lm['maxConeOf_avail_eq'] = lm['maxConeOf_avail_eq'].replace('(hd : 0 < d)', '(hd : 1 < d)')
    check('M', 'pairing: a landed statement that differs from the dense one fails the pair and only the cone cell',
          not pair_ok(mod, lm, 'maxConeOf_avail_eq_of_dense', 'maxConeOf_avail_eq')
          and verdict_of(mod, lm) == ([BALL_TOKENS[0]], [CONE_TOKENS[1]], [STRICT_TOKENS[0]]))
    lm2 = dict(LANDED)
    lm2['eq_qBall_of_boundaryTransitive'] = lm2['eq_qBall_of_boundaryTransitive'].replace('BoundaryTransitive Ω G',
                                                                                        'BoundaryTransitive Ω G ∧ True')
    check('M', 'pairing: a landed statement differing outside the hypothesis fails the pair',
          not pair_ok(mod, lm2, 'eq_qBall_of_dense', 'eq_qBall_of_boundaryTransitive'))
    # S3 -- resolution
    must_fail('S3', 'an opened namespace dropped (qnorm, centroid and qBall no longer resolve as in TRB-1)',
              replace_once(mod, OPEN_LINE, OPEN_LINE.replace('InvariantInnerProduct ', '').replace('TransitiveBody ', '')))
    must_fail('S3', 'a local declaration shadowing a landed object of a paired statement',
              insert_in_section(mod, '/-! ### §B', 'def eball (d : ℕ) : Set (Fin d → ℝ) := Set.univ'))
    # S4 -- strictness
    must_fail('S4', 'the weakening reversed',
              replace_once(mod, WEAK_HEAD, '    {Ω : Set V} {G : Set (V ≃ᵃ[ℝ] V)} (hT : DenseBoundaryOrbit Ω G) : '
                                           'BoundaryTransitive Ω G := by'))
    must_fail('S4', 'the non-transitivity proved without EFF-1\'s countable no-go',
              replace_once(mod, NOGO_PROOF, '  fun h => absurd h (by exact?)\n'))
    must_fail('S4', 'the family enlarged to all reflections',
              replace_once(mod, '{q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0}',
                           '{q : Fin d → ℚ // ∑ j, ((q j : ℝ)) ^ 2 ≠ 0 ∨ True}'))
    must_fail('S4', 'the strictness witness moved to d = 2',
              replace_once(mod, 'theorem not_boundaryTransitive_ratRefl : ¬ BoundaryTransitive (eball 3) (ratRefl 3) :=',
                           'theorem not_boundaryTransitive_ratRefl : ¬ BoundaryTransitive (eball 2) (ratRefl 2) :='))
    lm3 = dict(LANDED)
    lm3['not_boundaryTransitive_of_countable'] = lm3['not_boundaryTransitive_of_countable'].replace('G.Countable',
                                                                                                    'G.Finite')
    check('M', 'strictness: a different landed no-go fails only the strictness cell',
          verdict_of(mod, lm3) == ([BALL_TOKENS[0]], [CONE_TOKENS[0]], [STRICT_TOKENS[1]]))
    # S5
    must_fail('S5', 'an exact-existence object stated',
              append_strict(mod, 'theorem sf_free : sharpFamily 3 ⊆ sharpFamily 3 := le_rfl'))
    must_fail('S5', 'the Lorentz bridge restated',
              append_strict(mod, 'theorem lz (x0 : ℝ) (v : Fin 3 → ℝ) (h : 0 ≤ conePair (sharpEff v) x0 v) : True := '
                                 'trivial'))
    must_fail('S5', 'the control family in a consumer section',
              insert_in_section(mod, '/-! ### §D', 'theorem rr_c : ratRefl 1 = ratRefl 1 := rfl'))
    # S6
    must_fail('S6', 'a landed definition re-declared', append_strict(mod, 'def fullAut : ℕ := 0'))
    must_fail('S6', 'a second import',
              replace_once(mod, 'import OIBridge.K2Guard\n', 'import OIBridge.K2Guard\nimport OIBridge.SharpTests\n'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  (A) The ball.', '  This replaces K∞-Trans. (A) The ball.'))
    must_fail('S7', 'the design header', replace_once(mod, 'round KTRANS-DENSE-1:', 'design (round C):'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('A dense boundary orbit suffices for the listed consumers; the round does not derive one, '
                          'and ratRefl is a control.')
          and phrase_hits('The operations are\nclosed under operations.') == ['closed under operations'])
    # S8
    must_fail('S8', 'a cone object in the ball section',
              insert_in_section(mod, '/-! ### §C', 'theorem mc_b : maxCone (eball 1) = maxCone (eball 1) := rfl'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.DenseOrbit.countable_seedOrbit_cone\n',
                           '#print axioms OIBridge.DenseOrbit.countable_seedOrbit_cone\n'
                           '#print axioms OIBridge.DenseOrbit.countable_ratRefl\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense\n',
                           '#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense\n'
                           '#print axioms OIBridge.DenseOrbit.eq_qBall_of_dense\n'))
    # V -- each cell reads its alternative, independently of the others
    m = replace_once(mod, QN_HEAD, QN_HEAD.replace('0 ≤ R ∧', '0 < R ∧'))
    check('M', 'decision rule: a broken ball pair reads BALL-NOT-ESTABLISHED and leaves the other cells unchanged',
          verdict_of(m) == ([BALL_TOKENS[1]], [CONE_TOKENS[0]], [STRICT_TOKENS[0]]))
    m = replace_once(mod, CONE_HEAD, CONE_HEAD.replace(' (hE : EffectsOn (eball d) avail)', ''))
    check('M', 'decision rule: a broken cone pair reads CONE-NOT-ESTABLISHED and leaves the other cells unchanged',
          verdict_of(m) == ([BALL_TOKENS[0]], [CONE_TOKENS[1]], [STRICT_TOKENS[0]]))
    m = replace_once(mod, NOGO_PROOF, '  fun h => absurd h (by exact?)\n')
    check('M', 'decision rule: a broken strictness witness reads STRICTLY-WEAKER-NOT-ESTABLISHED and leaves the other '
               'cells unchanged', verdict_of(m) == ([BALL_TOKENS[0]], [CONE_TOKENS[0]], [STRICT_TOKENS[1]]))
    m = replace_once(mod, WEAK_HEAD, WEAK_HEAD.replace('(hT : BoundaryTransitive Ω G)', '(hT : True)'))
    check('M', 'decision rule: the weakening broken reads NOT-ESTABLISHED in the two cells that read it, and leaves '
               'the cone cell unchanged', verdict_of(m) == ([BALL_TOKENS[1]], [CONE_TOKENS[0]], [STRICT_TOKENS[1]]))
    m = replace_once(mod, DEF_TAIL, 'y ∈ ((fun g : V ≃ᵃ[ℝ] V => g x) \'\' G)\n')
    check('M', 'decision rule: the definition broken reads NOT-ESTABLISHED in all three cells',
          verdict_of(m) == ([BALL_TOKENS[1]], [CONE_TOKENS[1]], [STRICT_TOKENS[1]]))
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('KTRANS-DENSE-BALL-PROVED, KTRANS-DENSE-CONE-PROVED and KTRANS-DENSE-STRICTLY-WEAKER.')
          == ['KTRANS-DENSE-BALL-PROVED', 'KTRANS-DENSE-CONE-PROVED', 'KTRANS-DENSE-STRICTLY-WEAKER']
          and note_tokens('KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED') == ['KTRANS-DENSE-STRICTLY-WEAKER-NOT-ESTABLISHED'])
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
