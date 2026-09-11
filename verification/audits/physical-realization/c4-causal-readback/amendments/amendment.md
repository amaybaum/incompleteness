# C4 causal-readback audit — post-preregistration amendment

This amendment is binding and additions-only. It sits one commit over preregistration
`ada7ccfcd02f0505aedae41b91eaf46b22c0a769` and leaves
`verification/audits/physical-realization/c4-causal-readback/preregistration.md` byte-for-byte untouched. Where the preregistration's
provisional wording conflicts with the clarifications below, this amendment controls execution and
reporting. No Lean proof, probe mutation, manuscript edit, stochastic-to-quantum correspondence, or
new physical condition is introduced here.

## A1 — `C4e` / `C4r` are candidate causal-readback forms, not yet proved strengthenings of C4w

The preregistration's title, section heading **Candidate strengthened C4**, outcome labels using
“strengthened/strong C4”, and prediction language prejudge T7. For execution they are read neutrally:

- `C4w` is the manuscript condition on history-sensitive visible conditionals;
- `C4e` and `C4r` are **candidate causal-readback forms** defined on rooted one-time visible marginals;
- T7 decides their logical relationship to C4w, including every support/prior hypothesis required.

Accordingly, M-A means **candidate causal-readback succeeds mathematically**, M-B means the frozen
candidate fails, S-A means the existing architecture sources the successful candidate, and S-B/S-C
retain their conditional/gap readings. The word *strengthening* may be used in the outcome only if T7
actually proves the relevant implication to C4w under the stated hypotheses. If T7 finds the predicates
incomparable or only conditionally related, report that rather than forcing an ordering.

The motivation for studying `C4e`/`C4r` remains unchanged: current C4w explicitly permits a pre-sampled
response table and therefore does not itself require a causal visible-originating write-then-read cycle.

## A2 — row-stochastic composition convention is frozen now

Rows of `Gamma_t` are indexed by the rooted initial visible preparation and columns by the visible
outcome at time `t`. A stochastic propagator from time `s` to time `t` acts on the **outcome** index by
right multiplication. Therefore the definition used in T3 and every theorem is

> `Gamma_t = Gamma_s * Lambda_(t,s)`

with `Lambda_(t,s)` row-stochastic. Equivalently, for row probability vectors,
`p_t = p_s * Lambda_(t,s)`.

This supersedes the preregistration's deferred notation
`Gamma_t = Lambda_(t,s) o Gamma_s` and the same order in core target 2. The data-processing target is:

> if `Gamma_t = Gamma_s * Lambda` with stochastic `Lambda`, then total variation between any two
> corresponding rooted rows cannot increase from `s` to `t`.

The exact row-collision obstruction is tied to this convention: equal rows of `Gamma_s` remain equal
after right multiplication by every stochastic `Lambda`, so they cannot become unequal rows of
`Gamma_t`. Left multiplication by `Lambda` mixes over the root index and is **not** the divisibility
notion of this audit. No proof may switch orientation after seeing a control.

The existing P-D control already uses this convention (`T1 * ID = T2`), and the existing P-E symbolic
obstruction is to be compared against this exact factorization direction.

## A3 — layer construction and abstract no-go theorems are separate

Only core target 1 is intrinsically about the frozen finite visible/hidden realization layer: it
constructs each rooted `Gamma_t` from finite `V`, finite `H`, reversible `phi`, one fixed hidden prior,
and projection to `V`, and proves the resulting map stochastic.

Once a finite rooted stochastic family `Gamma_0,...,Gamma_K` is given, core targets 2–5 are
**layer-independent**. Their statements and proofs require neither reversibility, nor a hidden carrier,
nor a common prior:

- stochastic right-factorization implies TV contraction;
- `C4r(K)` forbids P-divisibility;
- `C4e(K)` implies `C4r(K)` and hence P-indivisibility;
- equal rows at `s` followed by unequal corresponding rows at `t` directly forbid right-factorization.

The fixed realization is needed to *source and interpret* a rooted family as an OI observer law and to
instantiate the controls on the intended layer. Reversibility supports the interpretation that total
information is not destroyed; it does no work in the abstract factorization no-go itself. Execution and
later citations must not attribute targets 2–5 to reversibility or hidden-memory hypotheses they do not
use.

## A4 — “left the visible description” means the one-time marginal only

The preregistration's phrases “lost from the visible description” and “information that actually left
the visible description” are narrowed as follows:

> At time `s`, the distinction between roots `a` and `b` is absent from the **one-time visible
> marginal** represented by the corresponding rows of `Gamma_s`.

This does **not** imply that an observer retaining the visible history up to `s` has lost the root
distinction. The history record may still contain it. This is exactly why C4w and `C4e`/`C4r` probe
different observables: C4w concerns history-sensitive future conditionals, whereas `C4e`/`C4r` concern
one-time rooted marginal distinguishability.

Therefore `C4e`/`C4r` by themselves are marginal-revival signatures, not proofs that hidden degrees of
freedom causally stored and returned the information. On a fixed reversible visible/hidden realization
they are candidates for the operational signature of causal readback; T7 and the T8 sourcing census
must decide whether the architecture earns that interpretation. No outcome may infer a causal hidden
write/store/read mechanism from marginal revival alone.

## A5 — execution guard for the audit-local C4 vocabulary

`C4w`, `C4e`, and `C4r` are verification-local labels. They do not rename the manuscript's C4 in this
round. Before and after adding any Lean module or guard surface, execution must run the existing
architecture/edge guards, including the live C4 statement pins such as R7-AUDB, and confirm that the
audit-local vocabulary has not accidentally triggered or weakened a manuscript guard.

If a guard needs a mechanical accommodation for the audit-local labels, make the narrowest change that
preserves the existing manuscript prohibition and record it explicitly; do not edit the manuscript C4
or loosen the guard's substantive claim merely to admit the new verification vocabulary.

The four frozen controls, the two-verdict separation, the Barandes boundary, and the conservative S-B
prediction are otherwise unchanged. Stop before Lean until this amended head is independently reviewed
and approved.