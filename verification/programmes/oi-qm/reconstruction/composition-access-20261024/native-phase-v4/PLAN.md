# Native-phase composition and operational equivalence

Research plan fixed before the new diagnostic, 24 October 2026. No physical
access rule, initialization premise, extension or equivalence is adopted.
Root publishes this work under the existing #912 guiding draft.

## Inputs and scope

- #910 at `71d291297d0a662cbb9377ab48eef7aa4b839e77`, with combined-law
  author `9b334367864c39e969072d9fbd46b0c049584963`.
- #912 at `69540662b234e37c6805ded244962a80f15f63a2`: conditional composition
  theorem, tagged-interface and post-read controls remain unchanged.
- Actual successful selected phase is previous q8=(0,y,0), current
  q9=(0,X,R), current remote Z=(0,0,Z). The entire two-slice neighborhood,
  resource bank, old records, terminal failures and flags are retained.
- The calibrated post-Y weights are 5:3:2 on (X,R)=(y,y),(1-y,y),(1-y,1-y),
  with independently fair Z and success 5/16. They are supplied targets.

## Productivity test

A useful result must specify a fixed operational equivalence relation on
full phase measures and expose a native response-relevant field omitted by
the selected-coordinate comparison, or supply a concrete closure certificate.
Merely restating the abstract composition induction is insufficient.

## Fixed probes and decisions

1. Derive the one-step native response at q8 from the actual update rule,
   keeping the five-neighbor XOR C outside q9 as an explicit variable. Check
   the formula against direct six-neighbor updates on all finite local
   assignments of the two-slice boundary used in the diagnostic.
2. Compare two private boundary completions with identical selected phase,
   herald and current whole-q9 record but different C_A. Compute the entire
   next-q8 raw-record laws exactly, including success and terminal failure.
   These are a boundary-space noncongruence control; do not assert both are
   reachable from the retained original-time source family.
3. Positive control: a sufficient native boundary invariant fixing the
   response-relevant C must remove that discrepancy for the stated one-step
   continuation. A difference in an irrelevant distant field must not matter
   at this horizon. Test the second-order previous-slice contribution
   independently. Detect mutants that drop the omitted neighbor or old slice.
4. Define depth-d operational equivalence by all permitted future complete
   record distributions, with stopping/failure flags included. State the
   recursive branch-closure obligation and the stronger instrument-decoder
   condition sufficient for arbitrary finite adaptive composition. Distinguish
   operational equivalence, equality of selected marginals and hidden-state
   equality, with a nontrivial positive control showing hidden identity is
   unnecessary.
5. Specialize the outgoing-X reset target to every public whole-q9 branch.
   Any illustrative fresh reset is an abstract positive control only. It must
   preserve the conditional old history and the extra R field, restore a
   valid X eigenstate carrier, and include failures. No cold apparatus splice,
   history-selected decoder or arbitrary late-q8 socket is allowed.

Use exact finite arithmetic, explicit exceptions and structured deterministic
output. Run normal and optimized Python and require byte-identical output.
No broad search, new Lean certificate or general native closure is claimed.
