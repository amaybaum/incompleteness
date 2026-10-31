# PC-1 stage 1: owner disposition of the SC-1 to SC-3 deviation (two-track record)

Append-only record. It changes neither the frozen preregistration (`948b30c1`) nor PC★
(`72b4af27`) nor `stage1-log.json` (`9245d542`), and it rewrites no earlier text. Those files
keep their content. Where PC★1 or the stage-1 log says that clause 0(vi) was met, that statement
is not to be cited as a strict-compliance finding; this record states the controlling reading.

## Authority

Owner disposition, PR #1022 comment 6547077354, by `amaybaum` (OWNER), 2026-10-31T17:56:33Z.

## The deviation

The owner's stage-1 authorization (PR #1022 comment 6546845219) excluded any Python test before
the PC★ freeze. Three structural checks, SC-1 to SC-3, were nevertheless run in Python before
that freeze, under the coordinator's brief. They examined only properties of a 1-D two-neighbour
analogue of the native rule (bijectivity, additivity, translation-commutation, the zero fixed
point). They computed no candidate outcome predicate or value. They are logged in
`stage1-log.json` with their script and output, and are superseded by the independently reviewed
paper proofs P-1 to P-3 in PC★ §PC★2a.

## Two tracks

**(a) Strict frozen-rule outcome: INCONCLUSIVE (void).** Frozen preregistration §6 clause 0(vi)
makes any forbidden or unlogged computation before PC★ an `INCONCLUSIVE (void)`. Disclosure does
not turn a forbidden computation into an authorized one. Under the unmodified frozen decision
rule, the stage-1 procedural token is therefore VOID.

**(b) Scientific finding, carried only under a disclosed owner exception: no admissible
candidate (gap).** The owner accepts the independently reviewed scientific screening finding:
among the 25 candidates screened (F2-1's 13 rules and Q1 to Q12), none is admissible, and the
obstruction is G★ item 3 for native couplings, scoped as PC★ states it and not a universal
no-go. The owner grants a narrow, one-time exception for exactly SC-1 to SC-3 when this finding
is presented. The exception is a post-hoc governance decision, not a statement that the
preregistration was followed.

No other deviation is waived. No protocol text, expectation or historical record is rewritten.

## Consequences for stage 2

A controls-only stage 2 (separately authorized in the same comment) cannot turn the strict token
into a compliant `INCONCLUSIVE (gap)`. If every reference control passes, the strict token stays
VOID under 0(vi), and the scientific finding stays the scoped stage-1 gap carried under the
exception. Any other failed requirement is additional VOID evidence.

## Owner's framing for later work (not an adopted premise)

"Record not a function of configuration" must specify which configuration and which physical
access interface. In a deterministic complete-state model, a physically recorded outcome,
including apparatus, seed and history, is a function of the full prior state and dynamics. A
merely stochastic readout can often be represented by enlarging the state, and then does not
evade the Koopman-indicator baseline. A preregistration on non-functional access must first
distinguish a new physical primitive from incomplete state specification or representational
relabelling, with explicit alternatives and scoped falsifiers.
