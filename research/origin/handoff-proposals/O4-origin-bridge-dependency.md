# Handoff proposal O4-1 — Origin ↔ composite-action bridge: one shared object, two open propositions

From: `research/origin` (thread branch, commit of this file). To: the coordinator, for the bridge thread.
Status: proposal only; nothing here is adopted, governed or certified. Evidence: `NOTES-O3.md` §4, `NOTES-O4.md`,
`experiments/o3_continuous.py` (C1, C6), `experiments/o4_dependency.py` (D1–D5), all exact and replayed.

## 1. The shared object

The bridge's isolated missing assumption A_miss (archive `pt/INTEGRATION-NOTE-STAGE6.md` §5) is the spectator
stability (b), on one token, of `ball3Drive`'s flow R_z(t) — the substratum phase flow about the frame axis — and of
its J-conjugate R_x(t). With J = `cyc3` (`KInfFoundations.lean:425`, `cyc3_apply` :427):

- J = R_z(π/2)·R_x(π/2) and J·R_z(t)·J⁻¹ = R_x(t) (exact, `o4_dependency` D1–D2);
- hence **A_miss ⟺ (b) for R_z(t) for all t, together with (b) for the single discrete operation J** (written proof,
  NOTES-O4 §1, identity I-1);
- J maps the pure frame state e_z to the pure balanced state e_x and carries the owner's interference witness
  (1, 1/2) with J⁻¹ (D3); its unitary lift is a non-monomial balanced mixer of order 3 (D4). **J is the Discrete
  Origin target, stated in the bridge's vocabulary.**

## 2. The two propositions

| proposition | content | owner | status |
|---|---|---|---|
| SRC(J) | J (or any balanced mixer) is available on one token from a premise that passes the disguise test | Origin | OPEN; impossible on the stated access (NOTES-O1 T3, T5, T6); every known instance fails the disguise test or changes the observation law (NOTES-O2) |
| SPEC(J), SPEC(φ) | (b) for J and for the phase flow φ on one token; matrix form: context stability / all-level availability | bridge | OPEN; independent of everything at L (stage 6) |

**The bridge needs SRC from Origin:** (b) for J asks that the cone be invariant under an operation that, at L,
nothing makes available (stage 5's L1).
**Origin needs SPEC from the bridge:** once a mixer is sourced at level one, what remains for `oiPlusMin_iff_qm`
is exactly its spectator stability (NOTES-O3 §4; kernel `derivedOI_qm_iff_phaseFree` RouteB.lean:161,
`oiPlusMin_iff_qm` MinimalRepertoire.lean:569).
**Neither discharges the other** (stage 5: every principle yielding (b) contains a spectator clause; stage 6:
K(Z_F) satisfies every item at L and fails (b); NOTES-O2: no spectator principle sources an operation).

## 3. Proposed joint statement (for the coordinator to adopt, amend or reject)

> Over the substratum class (monomial, with its phase continuum), exact finite quantum mechanics follows from two
> propositions about one discrete operation B, balanced on a moved pair: SRC(B), its availability at level one,
> and SPEC_M(B), its spectator form at every level. At the pair level the bridge's missing assumption is
> SPEC_P(φ) ∧ SPEC_P(J) with J = cyc3 a balanced mixer. Origin owns SRC; the bridge owns SPEC.

Supporting pieces: SPEC_M of the phase flow is a theorem (`substratumClass_contextStable`,
StructuralClosure.lean:261); SRC(B) + SPEC_M(B) + the phase continuum give the drive at every level by exact
conjugation (`o3_continuous` C1, `o4_dependency` D5) and then phase-free richness.

## 4. Two constraints Origin hands over

1. **Lemma P** (NOTES-O3 §3): if single-token observation in a composite model is passive and repeatable, every
   pure state of a token is outcome-deterministic for that readout, so no balanced mixer and no drive through the
   native NOT exist on a token. A bridge construction that wants the drive cannot assume passive token-level
   observation.
2. **The pair-level phase-flow half is not free.** Its matrix-level counterpart is a theorem, but no theorem at L
   connects the matrix carrier to `W 3` (stage 6, NO-MEET). A transfer for the monomial class would reduce the
   bridge's target to SPEC_P(J) alone — the spectator stability of exactly the operation Origin is trying to source.

## 5. What would refute this proposal

- an exact model satisfying SPEC_P(φ) ∧ SPEC_P(J) and failing (b) for R_x(t) (it would contradict I-1, whose
  (⇐) direction is the homomorphism property of `actτ`);
- a premise at L that yields SRC(J) without a non-monomial operator in its interface (it would contradict
  NOTES-O1 T3/T5 on the stated access);
- a theory satisfying `DerivedOI ∧ SubstratumAvail`, SRC(B) and SPEC_M(B) that is not exact finite QM (it would
  contradict O3-T1 together with `derivedOI_qm_iff_phaseFree`).
