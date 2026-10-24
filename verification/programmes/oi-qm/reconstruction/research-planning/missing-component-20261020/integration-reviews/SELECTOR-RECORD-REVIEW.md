# Independent review: selector-record boundary (handoff of 23 October 2026)

**Reviewed:** `OI_selector_session_handoff_v1.zip`, sha256 `3d18fe9c…1d33`:
- `SELECTOR-RECORD.md`;
- `SESSION-HANDOFF.md`, byte-identical to the uploaded report;
- `selector_checks.py` and its output.

**Not reviewed:** the five dependency archives. Their hashes were checked; their contents and earlier results were not re-audited.

**Repository:** unchanged. Nothing was posted.

## Verdict

**HOLDS as stated.** All seven claims of the note were reproduced by independent code: the census, the partition tables, the sharp-read rigidity theorem, the counterexample, the pair distances and the pad countercontrol. I found no overclaim. The note confines itself throughout to:
- the supplied 12-state calibration;
- deterministic records;
- no native selector.

Classification: CONFIRMING (census and theorem), with two ELABORATING scope points (F1, F2). This is internal work on the consistency axis (§A.23); it moves no correctness band.

## What was run

1. **Integrity.**
   - `sha256sum -c SHA256SUMS`: all 10 files OK.
   - The five dependency hashes equal the handoff's table.
   - The zip has no absolute or `..` paths.
2. **Replay.** The checker was read in full first. It uses only the standard library, writes nothing, makes no network calls and uses no randomness. `python3 -I -B` and `python3 -I -B -O`, run from another directory, both reproduce `selector_checks.out` byte for byte (Python 3.13).
3. **Independent re-derivation** (`indep.py`, shares no code with the author's checker).
   - Rebuilds the hidden states and preparations from the note's §1 table and re-checks all 32 calibrations.
   - Obtains each event's affine effect by exact Gaussian elimination over the eight preparations, rather than the author's closed-form α, β.
   - Tests positivity of E and I−E as 2×2 Hermitian matrices (trace ≥ 0, det ≥ 0).
   - Counts partitions by brute force over all set partitions of the 12 states with at most four blocks, rather than the author's recursion.
   - Results:

   | Quantity | Reproduced value |
   |---|---|
   | events satisfying the identities, by size | 346: {0:1, 3:64, 6:216, 9:64, 12:1} |
   | positive events, by size | 238: {0:1, 3:12, 6:212, 9:12, 12:1} |
   | identity-compatible partitions | (1, 172, 864, 576) |
   | positive partitions | (1, 118, 42, 9) |
   | each of the 8 sharp halves | effect exactly P_(a,s); its only nonempty positive sub-event is itself; 9 sub-events satisfy the identities |
   | XZ(++) effect | (1/4)(I + σ_X + σ_Z); value −1/10 at (−3/5, 0, −4/5) |
   | pair TV | XY 1/6, XZ 0, XR 7/30, YZ 0, YR 1/15, ZR 0 |

4. **Mutations of the author's checker.** All five tried are killed:
   - dropping the I−E condition;
   - a strict inequality in place of ≤;
   - β without its Y component;
   - positivity without affinity;
   - an unfair pad.

5. **By hand.**
   - The antipodal coefficients per group are (5, 2, −7) for X and (5, −4, −1) for Y.
   - R's coefficients (11, −4, −7) equal 4/5 times X's plus 7/5 times Y's. This is consistent with the relation rank of 2 and forces n0 = n1 = n2.
   - The fourth identity vanishes pointwise; for example, at +++ it is 5·7 − 4·5 − 3·5 = 0.
   - The Z-half system: subtracting the two equations gives 6e1 + 4e2 = 0, which has no ±1 solution.
   - The positivity criterion follows from the eigenvalues α ± |β| of E and of I−E.

## Findings

**F1 — scope premise of the positivity test (ELABORATING; should state).**
- Requiring every record effect to be a qubit effect is necessary when two things hold: the record's quantum counterpart acts on the input qubit, and the apparatus state is independent of that input. Tracing out an independent apparatus preserves positivity, so under this premise the criterion is right for the stated full-qubit target.
- It is not necessary for a model whose preparations carry accessible side information correlated with the input, such as a qubit plus a classical register. S6 shows the hidden carrier holds exactly such information: two preparations of I/2 differ by TV 7/30 on a stored pair.
- Suggest stating the premise explicitly in §3 and §5: the input represents a qubit state with no unmodelled preparation label or other accessible correlate, and the apparatus is prepared independently of it. This also makes clear that S5/S6 are two views of the same preparation contextuality.

**F2 — which test is operative for the native construction (ELABORATING; minor).**
- The deterministic rigidity theorem (S2–S4) assumes fixed apparatus data. The native constructions draw random resources (reserved uniform coordinates), so the theorem does not apply to them directly.
- The operative acceptance test is the factorization P(s,h | a,ρ) = κ_(a,s,h) Tr(P_(a,s) ρ). Here κ may depend on the setting a and the outcome s, but not on the input ρ: given the setting and the outcome, the extra record is independent of the input. Unconditional independence of h would be stronger than necessary. h must include every accessible field.
- §5 says this already. The handoff's executive summary and item 3 lead with the deterministic result, which a reader could take for the native test.
- Suggest that the next contract preregister the factorization as the primary decision rule. It should be checked on all eight menu preparations, and on the reachable post-instrument family for reuse. Deterministic rigidity is then a supporting obstruction.
- In that rule, failures, timing and auxiliary records enter h explicitly. Unsuccessful runs are not conditioned away.
- The outgoing state is checked separately, against the instrument identity of §5. Correct record probabilities alone do not establish a correct instrument.

**F3 — an unstated step in the §4 proof (minor).**
- The argument "positive refinements of a sharp outcome are proportional to it" uses the fact that a sign half's effect is exactly P_(a,s). That fact follows from the read calibration. It is checked by S1 and by `indep.py`, but it is not stated in the proof.
- Suggest one sentence: the half's event has response (1 + s t a·b)/2 on preparation (b, t), which is Tr(P_(a,s) ρ_(b,t)). The menu is tomographically complete (its Bloch rows have rank 4), so the half's unique effect is P_(a,s).

**F4 — independence of the positive counts (control adequacy; closed by this review).**
- In the package, the counts 238 and (1, 118, 42, 9) are compared only to numbers hard-coded beside the code that produces them. The identity-compatible row has an independent combinatorial formula; the positive row has none.
- The brute-force recount above supplies the independent check. If the note is to stand alone, cite an independent recount for the positive row.
- S7, the pad, holds by construction; the note correctly calls it a supplied channel and a countercontrol, not evidence.

**F5 — wording (nit).** In §4, "a proper three-state cell contains an odd number of Z signs" means that its Z+ and Z− counts are unequal, since there are three states. Suggest saying that directly.

## Claim and evidence boundary

No promotion was found:
- not from the calibration to OI;
- not from deterministic to all records;
- not from necessary to sufficient;
- not from the menu to a native construction.

The negative result is stated for the class it rules out: deterministic carrier-only records on this calibration. The handoff's governance boundary is consistent with the session's state: read-only, no posting, #824 and #880 out of scope.

## Reconciliation with the author's response

- **Factorization (F2):** the author's response requires the extra record to be independent of the input conditional on setting and outcome, with κ_(a,s,h) free to vary with the outcome. That is the reading the formula above encodes, and F2 now states it in words.
- **Specification:** the response adds three requirements, now carried into F1 and F2:
  - the explicit qubit and independent-apparatus premise;
  - failures, timing and auxiliary records in h, with no silent conditioning on success;
  - a separate outgoing-state check.
- **Missing proof step (F3):** the response supplies it — tomographic completeness of the menu makes the half's effect exactly P_(a,s). This review agrees.
- **Next task:** this review also agrees that a further record census would add little. The next substantive task is the native interface.

## For the receiving session

The next target in handoff §6 is well posed: the actually transported four signs, an input-independent setting, a complete public record, and no copies of unknown carrier bits. Two changes from this review:
1. Adopt F2's factorization as the preregistered acceptance rule.
2. Carry F1's premise into the record specification. Any accessible field correlated with the preparation beyond the selected sign must either be masked under a stated access class or counted as a failure of the qubit interpretation.

The independent checker `indep.py` accompanies this review. It is standard-library only, takes about 3 s, and prints the values tabulated above.
