# A bounded native instrument under the report18 rule (coordinator-authored, unreviewed)

> **WIP / UNVERIFIED — research record.** The coordinator's session produced this at the owner's instruction. It is
> the next deliverable named in report20 §6. Independent review is pending. It adopts no premise.

- `PREREG.md`: the questions, decision rules and controls, written before any code. `PREREG.sha256` holds its digest.
- `REPORT.md`: the instrument, the exact results and the findings.
- `instrument_checks.py`: the deterministic checker (numpy and fractions). Its saved output is
  `instrument_checks.out`. Replayed normally and with `-O`, the output is byte-identical; a run takes about 10 s.

**Outcome.**
- The four record identities, the Born values and closure all hold exactly, under a native realization of the
  fixed rule.
- The quantum statistics are supplied, not native. The supplied ingredients are:
  - a product hidden-register preparation;
  - fresh biased bits;
  - an ideal herald;
  - the tick;
  - the access stipulation.
- Exact R-menu values need a non-subspace (rejection) event.
- Widening access breaks the identities or closure, with exact witnesses.
