# SUBSTATE-2 unit F2-1 — amendment A★: stage 1, candidate selection

**Status: append-only amendment to the frozen preregistration.** Contract:
`../preregistration.md` at `66eb48ca64a79ffef98c8b086293f454a3dbeab6`, blob
`0b0c6502c84a3f8688e88d2390c91f14d446774c`, sha256
`389e7556bb2e23d165a9bcaf91b22a552bbad8dc3d1954f374add7b25bdfe17a`. Stage 1 was authorized by the
owner on 2026-10-31 ("Go ahead with stage 1"). This amendment does not change the preregistration.

No `R`, `R†`, `P`, Gate 4 or Gate 5 quantity was computed on any candidate (screen item 7). Every
computation run during selection is listed in `stage1-log.json` beside this file. Admissibility was
judged on structure only. Section references are to the preregistration unless marked A★.

***

## A★1. Outcome

**No admissible `Θ★` exists in the enumerated family or among the new candidates considered.**

- **Token.** Stage 1 ends at clause 1, `INCONCLUSIVE` (gap). The gap is named as an operator
  condition in A★4. Clause 0 still precedes it: the unit's token is `INCONCLUSIVE` (gap) only if
  the stage-2 controls of A★5 return their reference results; otherwise it is `INCONCLUSIVE` (void).
- **Clause 4 is unreachable.** No coupling `C` is frozen, so nothing can be transplanted to the
  probes C1, C2 and C10. The probes of clause 2(a) are not run.
- **F2.** The unit does not advance the F2 obligation of #914. No claim, row status or
  classification changes.

## A★2. The structural point that governs selection

This section is a paper argument about the *form* of a rule. It decides neither `R` nor `P`, nor
`N` or `O`, for any theory; stage 2 decides those for the controls.

1. **What a classical coupling records.** A coupling `C` between the register `Reg` and a classical
   sub-state space `(K, μ)` is a joint reversible process on `Reg × K`. The register value it
   records is a measurable function of the joint state. The readout projectors that `Θ_rule`
   computes from a readout process are therefore the indicator projectors of the level sets of that
   function. The computed readout basis is the indicator basis of a measurable partition: cylinder
   sets for Θ-A and Θ-K, or hemispheres for the C10 model.
2. **What a joint process induces on the register.** The canonical operator that a measure-preserving
   joint process `g` induces on the register-measurable functions is the compressed Koopman
   operator `f ↦ E[f ∘ g | 𝓡]`, or its adjoint, the transfer operator on densities. Both are
   positive and unital Markov operators (standard).
   - In the computed indicator basis their matrices are entrywise nonnegative and fix the constant
     function (AW5).
   - Changing basis, as Θ-F does, does not change the operator. It writes the same operator in a
     basis that the computed readout projectors do not diagonalize.
3. **What a candidate rule must differ by.** The preregistration designates this Koopman-indicator
   rule as the baseline (§3, "The rule's form is the hypothesis"). A candidate must state how its
   rule differs and which property of `(K, T, μ, C)` the difference depends on. For a classical
   `(K, T, μ)` and a coupling that records set membership, those data determine the joint transition
   structure and nothing finer. A rule that differs from the baseline therefore needs one of:
   - additional structure on `K` that the measure algebra does not carry (an amplitude or phase
     assignment to sub-states, or a complex line bundle);
   - a readout whose projectors are not indicator projectors.

   Either one is a posit. The question for stage 1 was whether any such posit has a physical
   justification in OI's own terms that does not build in the answer.

## A★3. Per-candidate screen record

Screen items are those of §3 (1: no target operator in the rule; 2: readout projectors computed;
3: no private decoder; 4: no assumed gate; 5: `μ`, held-out set and `E★` fixed; 6: no parameter set
from a target value; 7: no candidate computation before `A★`). The physical-justification grades
are **posited**, **motivated** and **derived**. "Extension" asks whether the candidate replaces a
premise of the §1 table, as §1 requires of a candidate.

| Candidate | Screen | Extension? | Justification | Verdict |
|---|---|---|---|---|
| Θ-A, cylinder access | passes 1–7 | no: the access is configuration-level and bijection-level, the premise retained; NATIVE-PADIC-1 option (c) | derived (it is the stated access, applied to digits) | not a candidate F2 extension; it stays the stage-2 control C1/C2 |
| Θ-K, Koopman compression | passes 1–7 formally | weakly: it replaces bijection-level operators with nonnegative contractions | posited. Reading a compressed Koopman operator as an implementation amplitude (a Kraus operator in `conjChannel`) is stated nowhere in OI. The coupling transports distributions (the projected observer operator, `lift-source-audit.md` T3), and the Kraus reading of its compression is a lift choice. It is also the designated baseline that a candidate must differ from | rejected as `Θ★`; it stays a stage-2 control |
| Θ-F, character relabelling | fails 2: the character basis is declared, and the computed projectors are cylinder indicators | no | — | rejected; it stays control C6 |
| Θ-D, dual access | fails 2 and 4 | would be | posited | rejected (below) |
| N1, amplitude embedding (register states sent to non-indicator functions on `K`, e.g. degree-one harmonics of a circle or sphere flow) | fails 2: the embedding is a declared basis in `L²(K)`, not computed from `C`; risks 1 (a representation selected for its rotations) | would be | posited; no OI process identifies a register value with a signed or complex function of sub-states | rejected |
| N2, √μ amplitudes with phase digits (deeper digits encode a phase, measures encode moduli) | fails 6: builds in `p = 2` (AW3); the phase encoding is declared (1, 2) | would be | posited | rejected |
| N3, rule change with level mixing (NATIVE-PADIC-1 option (b)) | passes 1–7 | no at the interface: it changes `T`, not `Θ`. With computed indicator projectors its images are baseline images (A★2) | not sourced: the only level-mixing coupling on record is the explicitly non-native mutant | rejected as `Θ★`; its depth coupling is control C9 |
| N4, continuous-time generator lift (`i log` of the Koopman group) | passes 1–7 | no: its exponentials are the Koopman group again, in the baseline class; the generator reading is representational (`lift-source-audit.md`, L4) | posited | rejected |
| N5, SU(2) lift of a hidden rotation (Kochen–Specker/Bloch type) | fails 1: a unitary representation selected to match a target | would be | posited | rejected; the model is probe C10 |
| N6, unistochastic lift (a unitary `U` with `|U_ij|²` equal to the transition probabilities) | fails 6 and 1: `|U|² = P` builds in `p = 2`; the phases of `U` are free and must be chosen | would be | representational: the fixed-basis representation `Q_fb` (`phase-source-audit.md` P6) | rejected |
| N7, polar factor of the compressed Koopman operator | passes 1–7 formally (it is a fixed function of the baseline image, and the polar factor of a projector is the projector) | would be | posited; no process of the observer architecture executes a polar decomposition: representation is not availability (`phase-source-audit.md` D2; `lift-source-audit.md` L1) | rejected for lack of physical justification |
| N8, linear-field (wave-operator) lift: the α-rule acting linearly on the field-amplitude vector, register carrier = sites or modes | fails 2: no classical readout process computes site or mode projectors with intensity statistics; such a readout and its `|u|²` weights are declared (AW3). Also unsourced on the native carrier: values in `ℤ/2^n` or `ℤ_2` carry no modulus, and the real α=1/3 operator is not asserted to be the substratum update (NATIVE-PADIC-1 REPORT) | would be | posited; this is L3 itself | rejected; it is the content of the gap |

**Θ-D in detail.** In a classical joint dynamics, a readout process copies a measurable function
of `K` into the register. Its computed projectors are indicators of level sets, never projectors
onto a character function. A projector onto characters is therefore either declared, which fails
item 2, or obtained by phase estimation. Phase estimation uses controlled shifts and a Fourier
transform on the register, an assumed coherent gate (item 4; AW2). The structural fact used here
was checked exactly and logged: the characters of `ℤ/2^m` span the same space as the depth-`m`
cylinder indicators, for `m = 1, 2`, and those of `ℤ/2` are real. So Θ-F and Θ-D add no operator
on that space: they only change basis.

## A★4. The gap, as an operator condition (§3, "If stage 1 fails")

**G★.** A coupling `C` and a rule `Θ_rule` such that all of the following hold:

1. **Computed readout.** Every readout projector is computed by `Θ_rule` from a stated physical
   readout process of `C`.
2. **Leaving both invariants.** Some process `g ∈ Proc` has an image `Θ_rule(g)` that, in the
   computed readout basis, is neither entrywise nonnegative up to a scalar nor fixing the all-ones
   ray up to a scalar. This is necessary for `R` (§2: `R ⇒ ¬N ∧ ¬O`; the Kraus bridge).
3. **Beyond the baseline.** `Θ_rule` differs from the Koopman-indicator baseline through a stated
   structure on `K`, or a stated readout, that has a physical justification in OI's terms. Since
   classical `(K, T, μ)` with set-membership coupling supplies only the baseline (A★2), this means
   one of:
   - an amplitude or phase structure on sub-states that the measure does not determine;
   - a readout whose computed projectors are not indicator projectors.
4. **No answer built in.** The rule neither builds in `p = 2` nor selects a representation by its
   target.
5. **Probes not certified.** Transplanted unchanged to C1, C2 and C10, the rule does not yield `R`
   or `P`.

**Relation to L3.** G★ restates L3's open entry: a map `Θ` into the carrier with its admissibility
(`lift-source-audit.md:299-305`), sharpened by items 1, 4 and 5. Nothing in the corpus, the
SUBSTATE-1 or SUBSTATE-2 records, or the candidates above supplies items 1 and 3 together without
failing item 4.

**Scope.** This is not a no-go. It concerns this family and the candidates considered, judged on
structure. A future candidate meeting G★ would be a new stage 1, under a new amendment reviewed
before any computation.

## A★5. Items fixed at A★

**Θ★, `Θ_rule`, `C`, `Proc`:** none.

**Transplant to the probes:** none possible, since no `C` exists. Clause 4 is unreachable, and the
probes of clause 2(a) are not run. The self-test case "`¬R ∧ ¬P` with a non-transplantable coupling"
is unaffected.

**Exhibit list `E★`:** `∅`, since there is no candidate. The control exhibit lists are those of §6,
including C6: the `ℤ/4` character-basis matrix `diag(1, i, −1, −i)` and one Fourier mode of the
α=1 wave map with a relative phase in the mode basis. The reviewer of `A★` may extend them before
the freeze.

**Measures for the stage-2 controls (Gate 3 form).**
- Odometer (C1, C6): Haar measure on `ℤ_2`, selected by unique ergodicity of `x ↦ x + 1`
  (standard; to be cited in stage 2).
- B1, B2, FIXED-SCALE skew (C2): the product-fair measures pinned by their SUBSTATE-2
  preregistrations at `c811e876`.
- SUBSTATE-1 infinite XOR (C2): the product measure of its note.
- Kochen–Specker model (C10): the normalized rotation-invariant surface measure on `S²`, unique by
  rotation invariance. The model's state-dependent hidden density is part of the model as published.

**Gate 5 held-out set:** none for a candidate. Control C7 uses the trace-rule values of §5: `rot`
16/25, `rot²` 576/625, and `rot · phaseGate a · phaseGate a · rot` 0. Gate 5b is not used.

**Stage-2 scope (controls only; needs its own owner authorization, and nothing runs under this
amendment).** These are the clause-0 controls that determine whether the gap token stands. With no
`Θ★`, the mutations that act on `Θ★` (M2, M5, M8, M10) are run on the screen and decision function
with stand-ins, so that each still changes its outcome as stated:
- M2 is applied to the C3 generator set.
- M10 is a constant rule `:= rot` applied to a C2 model. It must be flagged by screen item 1.
- M5 and M8 are run on synthetic results in the decision-function self-test.

**Lean: fixed-statement declarations** for a new module `OIBridge/F2CoherenceControls.lean`.
- Each enters the results only through the CI step conclusion of its build, plus a `#print axioms`
  check turned into a step conclusion (§9).
- Statement texts are fixed here and recorded by sha256 at stage 2 from this file.
- Names in `OIBridge` scope; existing modules are untouched (G2a).
- If a statement fails to elaborate as written, it is corrected by a further append-only amendment,
  reviewed at an exact SHA before any stage-2 build is used as evidence.

```lean
def OnesBounded {A : Type} [Fintype A] [DecidableEq A] (T : FiniteOperationalTheory A) : Prop :=
  ∀ (n : ℕ) (U : Matrix (A × Fin n) (A × Fin n) ℂ), Uᴴ * U = 1 →
    T.availExt n Unit (fun _ => conjChannel U) →
      ∃ z : ℂ, U *ᵥ InstrumentRealization.ones (A × Fin n) = z • InstrumentRealization.ones (A × Fin n)
theorem rot_not_preservesNonneg : ¬ PreservesNonneg (conjChannel DiagonalTheory.rot)
theorem rot_moves_ones :
    ¬ ∃ z : ℂ, DiagonalTheory.rot *ᵥ InstrumentRealization.ones (Fin 2 × Fin 1)
      = z • InstrumentRealization.ones (Fin 2 × Fin 1)
theorem falsifierUnavailable_of_nonnegBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : FrozenSourcing.NonnegBounded T) : RouteB.FalsifierUnavailable T
theorem falsifierUnavailable_of_onesBounded {T : FiniteOperationalTheory (Fin 2)}
    (h : OnesBounded T) : RouteB.FalsifierUnavailable T
theorem onesBounded_of_onesFixing {𝓘 : ImplementationClass} (arch : Architecture 𝓘)
    (hf : InstrumentRealization.OnesFixing 𝓘) {A : Type} [Fintype A] [DecidableEq A] :
    OnesBounded (genTheory 𝓘 arch A)
theorem permTheory_onesBounded : OnesBounded (SubstratumInterfaceAudit.permTheory (Fin 2))
theorem onesTheory_falsifierUnavailable : RouteB.FalsifierUnavailable (FlowEndpoint.onesTheory (Fin 2))
def nonnegClass : ImplementationClass := fun _ _ _ K =>
  ∃ (a : ℂ) (M : Matrix _ _ ℂ), ‖a‖ ≤ 1 ∧ (∀ i j, (0 : ℂ) ≤ M i j) ∧ K = a • M
theorem nonnegClass_arch : Architecture nonnegClass
theorem nonnegClass_nonnegBounded {A : Type} [Fintype A] [DecidableEq A] :
    FrozenSourcing.NonnegBounded (genTheory nonnegClass nonnegClass_arch A)
theorem nonnegClass_onesFixing : InstrumentRealization.OnesFixing nonnegClass
def realClass : ImplementationClass := fun _ _ _ K =>
  ∃ (a : ℂ) (M : Matrix _ _ ℝ), ‖a‖ ≤ 1 ∧ K = a • M.map (fun x => (x : ℂ))
theorem realClass_arch : Architecture realClass
theorem realTheory_rot : ¬ RouteB.FalsifierUnavailable (genTheory realClass realClass_arch (Fin 2))
theorem realTheory_not_phases : ¬ RouteB.PhasesAvailable (genTheory realClass realClass_arch (Fin 2))
theorem fullTheory_rot : ¬ RouteB.FalsifierUnavailable (genTheory fullClass fullClass_arch (Fin 2))
theorem fullTheory_rotDagger :
    (genTheory fullClass fullClass_arch (Fin 2)).availExt 1 Unit
      (fun _ => conjChannel DiagonalTheory.rotᴴ)
theorem fullTheory_phases : RouteB.PhasesAvailable (genTheory fullClass fullClass_arch (Fin 2))
```

The kernel facts the controls also use are cited, not restated: `permTheory_falsifierUnavailable`,
`permTheory_phase_ceiling`, `permTheory_nonnegBounded`, `substratumTheory_falsifierUnavailable`,
`onesTheory_not_phasesAvailable`, `nonnegBounded_verdict`, `onesFixing_not_phasesAvailable`,
`genTheory_mono`.

**Exact Python** (`python3 -I`; `fractions` or exact Gaussian or cyclotomic rationals; CI beyond a
smoke check):
- C1: the odometer's depth-`m` cylinder dynamics are permutations. The Θ-K compressions are entrywise
  nonnegative, so the class lies inside `permClass` or `nonnegClass`, for `m ≤ 6`.
- C2: the same containment for B1, B2, FIXED-SCALE and infinite XOR at their pinned finite stages.
  G4d: return 1 with and without readout.
- C6: the exhibits.
- C7: the trace-rule numerics (1, 337/625, 16/25, 576/625, 0).
- C9: the mutant's backflow, reusing the `c811e876` probe read-only.
- C10: Kochen–Specker exact reproduction of 1, 337/625 and the C7 frequencies. The outcome
  probabilities are `(1 + cos θ)/2` with `cos θ` rational for these operations.
- M1, M3, M4, M6, M7, M9; the decision-function self-test over every row of §4.

**Paper:** the C2 and C10 containments where they are not finite; unique ergodicity and the
invariance argument for the measures; this amendment's A★2 argument.

**Results-file schema** (`results.json`, schema id `f2-1-results/1`). The token is computed from
this file only:

```json
{
  "schema": "f2-1-results/1",
  "prereg": {"commit": "66eb48ca…", "sha256": "389e7556…"},
  "amendment": {"commit": "<A★ commit>", "sha256": "<A-star.md sha256>", "stage1_log_sha256": "…"},
  "stage1": {"candidate": null, "gap": "G★", "clause4_reachable": false},
  "kernel": {"<declaration>": {"statement_sha256": "…", "ci_run": "…", "build_step": "success|failure",
             "axiom_check_step": "success|failure"}},
  "exact": {"<check id>": {"value": "<exact string>", "expected": "<exact string>", "pass": true}},
  "controls": {"C1": {"reference_pass": true, "token": "COUNTEREXAMPLE"}, "…": {}},
  "probes": {"C1": null, "C2": null, "C10": null},
  "mutations": {"M1": {"as_stated": true}, "…": {}},
  "selftest": {"<row id>": true},
  "labels": {"G4b_dephasing": "n/a"},
  "review": {"grade": null, "reviewer": null, "time": null, "quote": null},
  "token": "<computed>"
}
```

## A★6. Borderline judgements

- **Θ-K.** It passes the screen formally. Freezing it as `Θ★` would give stage 2 a definite token,
  probably `COUNTEREXAMPLE` (row 8). It is rejected as `Θ★` for two reasons: it is the baseline
  that §3 says a candidate must differ from, and its implementation-amplitude reading is posited
  with no OI source. Selecting a candidate expected to fail is the mirror image of selecting one
  expected to succeed. Its outcome is obtained anyway as a control. The reviewer of `A★` may
  overrule this.
- **N7 (polar factor).** It passes items 1–7 formally and is rejected only for lacking a physical
  justification. Mathematical functions of the baseline image can therefore pass the screen as
  written. The screen's physical-justification requirement is what excludes them, and a reviewer
  may wish to test N7 as a posited candidate under a new amendment.
- **N8 (wave-operator lift).** It is the closest candidate to the corpus: SM's real observer-level
  wave operator acts on amplitudes. It fails on the readout and on the native carrier, not on its
  dynamics. This is where L3 stays open.
- **A★2 scope.** The argument covers rules of the induced-operator form for classical `(K, T, μ)`
  with set-membership couplings. It is not a theorem about every conceivable rule.

## A★7. What this amendment does not do

It changes no frozen file, kernel module, manuscript, ROADMAP row or SUBSTATE-2 record. It runs no
`R`, `R†`, `P`, Gate 4 or Gate 5 computation and no Lean build. It does not authorize stage 2. It
does not establish that no extension can source coherence. It records that none of the candidates
above does so with a physical justification that leaves the answer unassumed.
