# Coordinator review: native-flag-boundary handoff v1

> **DRAFT — research record.** The owner's read-only session produced this exploratory result. It is recorded here
> with the coordinator's verification and independent checks. It adopts no premise and states no OI no-go.

## Verification

- **Archive.** The archive's sha256 is `87ae6fe31dc405e12c35ceffb55c8da58c4557ce1bcee3b897f8b1bb4183c2ed`, as
  stated. The files in `handoff/` are its contents, unchanged. Their `SHA256SUMS` verifies.
- **Code review before running.** `flag_checks.py` uses only the standard library and a seeded pseudo-random
  generator, and writes only to stdout.
- **Replay.** Run from a separate directory with `python3 -I`, normally and with `-O`, the output is byte-identical
  to `flag_checks.out`.

## The handoff's corrections to report16: accepted and applied

1. **Finding 3's distance.**
   - At w = 2, the full-state distance between conditioning on W = w and on E_w is 2^−117 + 2^−174 − 2^−234. That
     is slightly larger than 2^−117. The S3 table had the exact values, but the finding's prose did not.
   - The payload, source and receiver record has the same law under both conditionings, so its distance is zero.
   - Finding 3 now states both.
2. **Finding 1** now names the census filters in succession:
   - a quiescent background, a pulse response and a balanced truth table leave six rules;
   - exact three-tick freshness then selects XOR.
3. **Finding 3's extension to prepared priors** was the coordinator's unchecked reading. It is now the handoff's
   branchwise lemma, including the record condition, and finding 3 cites it.

## Independent checks (`coordinator_flag_checks.py`; separate code, numpy)

| Check | Result |
|---|---|
| F1 | **Degree of the repaired raw rule, measured.** On a 7³ torus over ticks 1–10, with many wrap-arounds, 40 random 5-bit subcubes were tested. The bits can lie in any field, in either slice, anywhere on the torus, over dense random backgrounds. A Möbius transform over the 32 assignments gives the algebraic normal form of every output bit. The maximum degree is 1 for A and B and 2 for D |
| F2 | **Countercontrol.** A reversible variant with feedback from D into A, A′ = SA ⊕ (SB)(SD) ⊕ A_old, reaches degree 4 under the same measurement. So the measurement can detect higher degree, and the bound comes from the conjugate-linear structure |
| F3 | **The three-bit subcube on the actual apparatus** (K = 3, L = 25). The three bits are current A at (−1,0,0), current B at (1,0,0) and current D at the receiver. Every other readiness bit is zero, and the rest of the torus is dense and random (three backgrounds). On this subcube E_K is three-bit zero detection, and every raw output bit at ticks 0–5 has degree at most 2 in the tested bits |
| F4 | **The parity argument for the 1/8 bound.** Every one of the 128 functions of degree at most 2 on three bits sums to 0 over the cube, while the readiness indicator sums to 1. Each quadratic table therefore errs on at least one input. The uniform mixture of the eight single-error tables errs with probability exactly 1/8 at every input |

## Findings

1. **The prepared-prior lemma holds (CONFIRMING).**
   - For each w, the stopped law is exactly uniform if three conditions hold:
     - the reserved frontier bits are fair and independent of everything else;
     - the event W = w and the entire preparatory record depend only on the other bits;
     - the outputs are bijective in the reserved bits.
   - The proof conditions on the other bits and is two lines long.
   - The copy countercontrol is the important qualification. A bit can be left unchanged, still be fair, and yet be
     fully revealed by a visible record. The requirement is conditional freshness after every record, not an
     untouched marginal.
2. **The single-flag obstruction holds (CONFIRMING; NEW for the thread).**
   - Under the repaired rule, every raw A and B output is linear in the initial raw bits. Every raw D output has
     algebraic degree at most 2, at every tick and on every finite torus. F1 measures this on dense backgrounds, and
     F2 confirms the measurement can see higher degree.
   - Exact zero detection of J ≥ 3 freely varying bits has degree J. So no single raw register can carry a
     universally correct readiness flag at a predetermined deadline, given the following:
     - prepared resources that do not depend on the input;
     - an affine encoding of the inputs into the initial state;
     - an affine readout.
   - With randomized resources that do not depend on the input, some input errs with probability at least 1/8.
3. **The bound extends to the whole construction family (ELABORATING).**
   - Suppose a rule is conjugate to a linear map by a pointwise bijection G, where G has algebraic degree g and its
     inverse has degree g′. Then every output bit has degree at most g·g′ at every tick. This is the coordinator's
     observation and is not separately checked.
   - It covers the 16-predicate family of report15: D = C ⊕ g(A,B) with linear A, B and C waves gives degree at most
     2. Every member of that family therefore inherits the obstruction.
   - Composable logic of unbounded degree needs a rule that is not conjugate to a linear map in this bounded-degree
     sense. F2's feedback term is an example.
   - **Assumption-watch marker.** The linear-wave freshness proof does not survive feedback into the source fields,
     which composable logic of this kind needs. Freshness itself can survive: report18 proves bounded freshness for
     a rule with nonlinear feedback, from local permutivity along the frontier.
4. **Scope.** The obstruction is narrow: one raw register, a fixed deadline, inputs that vary freely, and resources
   and encoding that do not depend on the input. It does not exclude:
   - restricted prepared inputs;
   - distributed records read through an explicit decoder, although the decoder then performs the conjunction and
     must be counted;
   - nonlinear input encodings;
   - a different reversible update.

   It does not affect the two-input AND, which has degree 2.

## Relevance to the next target

The next step is a choice:
- keep the repaired rule and specify a distributed record or limited-domain detector, with a stated decoder; or
- find a different native reversible update that supports composable computation and carries its own proof that the
  source stays fresh.

Finding 3 makes the trade-off concrete. The first option moves the conjunction into an interface that must be
accounted for. The second gives up the linear-wave freshness proof, which then has to be replaced; report18 supplies one
replacement. Angular-law
selection remains a separate obligation, and the four record identities still have no station-indexed preparations
to test. The C-SPH-1 checkpoint stays closed.
