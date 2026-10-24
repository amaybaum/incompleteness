# A bounded native instrument under the report18 rule (coordinator-authored, independently reviewed)

> **Research record.** The coordinator's session produced this at the owner's instruction. It is the next deliverable
> named in report20 §6. Its independent review is `review/REVIEW.md`, with verdict *accept with corrections*. It
> adopts no premise.

- `PREREG.md`: the questions, decision rules and controls. `PREREG.sha256` holds its digest and the timestamp on
  which its precedence over the code rests; the two were first committed together.
- `REPORT.md`: the instrument, the exact results and the findings.
- `instrument_checks.py`: the deterministic checker (numpy and fractions). Its saved output is
  `instrument_checks.out`. Replayed normally and with `-O`, the output is byte-identical; a run takes about 10 s.

**Outcome.**
- The four record identities, the Born values and closure all hold exactly at the register level. Under the fixed
  rule, the native part is the single read's transport to the record receiver at tick 2 and the re-preparation
  registers at the outgoing receivers at the same tick. The preparation, its copies, the heralds, the fresh bits, the second read and closure in the
  prepared format are register-level or supplied.
- The quantum statistics are supplied, not native. The supplied ingredients are:
  - a product hidden-register preparation;
  - fresh biased bits;
  - an ideal herald;
  - the tick;
  - the access stipulation.
- Exact R-menu values need an acceptance event that is not an affine subspace. This instrument's threshold sampler
  has a joint acceptance flag of degree 12; any exact sampler needs degree at least 2, and lower-degree flags
  suffice.
- In the three widenings tested, for this layout, widening access breaks the identities or closure, with exact
  witnesses.
