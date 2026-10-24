# A1 candidate: an infinite fair reservoir with almost-sure stopping

Research draft. This examines one explicit change to availability; it does
not adopt that change. No native implementation, new premise, manuscript
status change, or full-equivalence claim follows.

## Candidate and first result

Replace a fixed finite fair-bit bank and fixed deadline by a countably
infinite initially independent fair reservoir. Admit a finitely described
algorithm that reads finitely many bits on almost every run, with no finite
worst-case bound. This changes an actual hypothesis of the preceding resource
diagnostic, rather than merely renaming a limit point as an operation.

For the fixed number p=(2+sqrt(2))/4, the following algorithm is exact at the
level of its eventual binary record. Compute the binary digits p_n of p,
read independent fair digits U_n, and stop at the first different digit.
Return Y=1 when U_n<p_n and Y=0 otherwise. All earlier digits agree.
The exceptional input U=p has probability zero; it never terminates.

After n reads the surviving event is one length-n cylinder, of probability
2^-n. Therefore P(T=n)=2^-n, P(T>n)=2^-n, and the expected number of
coin queries is 2. The stopping events with Y=1 have probabilities
p_n*2^-n, whose sum is p. Computing digits uses finite integer arithmetic
at each depth; coin-query expectation is not an assertion that each digit
costs constant physical time. Here T is stopping depth, not a constructed
native clock. The timing diagnostic applies when the public completion
record reveals T, or an injective function of T.

Thus finite fair randomness at a fixed deadline and fair randomness with
almost-sure unbounded access have different exact expressive power. The
earlier rationality obstruction does not apply to this sampler. The chosen
p is supplied in the algorithm; its emergence from native dynamics or a
physical setting is not established.

## Why this does not yet supply A1

1. A native implementation would have to source the infinite initial bank,
   reversible computation/workspace, clock, stopping rule, and output access.
   A bounded approximation does not itself supply the almost-sure operation.
2. Finite program descriptions still form a countable set. Even if each
   program defines an exact almost-sure channel, their image under a fixed
   realization map is countable. An uncountable family of arbitrary real
   thresholds requires an additional oracle/setting resource, not this one
   computable constant. This is the reviewed countability argument applied
   to a changed protocol class, not a claim that stopping programs produce
   only rational probabilities.
3. Under the fixed G3 identification and the pointwise mixed-hidden-state
   model, enlarging the reservoir does not change the kind of induced
   operation. Configuration bijections, configuration readout, classical
   control and discard give nonnegative sums of partial-permutation Kraus
   maps. Stopping-time sums and their convergent finite-dimensional limits
   keep entrywise nonnegativity. A Hadamard sends |1><1| to
   (1/2)*[[1,-1],[-1,1]], so it remains excluded. A negative off-diagonal
   entry cannot be obtained by changing the scalar sampling weights.

The third point is conditional on the stated operational identification.
The reviewed mc-node3 cone lemma explicitly takes the pointwise integral
as the model for infinite hidden spaces; this is not a kernel theorem for
an infinite native substratum. Main's `FrozenSourcing.lean` proves the
finite architecture's nonnegativity bound and a unitary-limit ceiling.
Here the extension to stopping-time maps is a written argument: sum the
CP branches that terminate by depth n; every entry on a nonnegative input
is nonnegative, and any finite-dimensional limit of these entries is still
nonnegative. Almost-sure termination on every relevant input ensures the
completed instrument has total probability one; that condition must be
proved, not inferred from termination on one calibration state.

This does not rule out record-level reproduction by a different operational
quotient. Node 6 distinguishes that target from G3-level operation
availability. A proposed quotient must identify states using **all** permitted
continuations and must make each transformation and composition well-defined
on those classes. A match of one binary record does not construct that map.

## A joint-record obstruction inside the candidate

Although T has the same geometric marginal for every non-dyadic p,

    P(Y=1,T=n) = p_n*2^-n,
    P(Y=0,T=n) = (1-p_n)*2^-n.

The stopping-depth record and output are correlated. For the two supplied thresholds
p and 1-p, their binary digits are complementary. At every stopping depth
the two joint laws put mass on opposite Y values. Their full (T,Y) laws
therefore have total variation distance 1, while their Y marginals have
distance |2p-1|=sqrt(2)/2 and their T marginals have distance 0.

This is a concrete warning against promoting a correct outcome marginal
and a state-independent timing marginal into a correct joint instrument.
If a proposed implementation uses these thresholds for different input
preparations at a common setting, the desired factorization
P(Y=s,T=n|rho)=kappa(s,n)*P(Y=s|rho) cannot have kappa independent of rho:
at n=1 the conditional factor for s=1 is positive for p and zero for 1-p.
Supplying a sampler with the unknown state's probability is itself an
unsourced operation; the calculation is an abstract candidate diagnostic,
not a claim that the native Y apparatus does this.

If stopping time is private, that specific extra record is absent, but the
access restriction and a physical delivery/read schedule become obligations.
At a fixed cutoff K, retaining timeout as an outcome gives mass 2^-K to it.
The two censored joint laws have distance 1-2^-K. Suppressing the time labels
and assigning timeout a fixed output instead gives a Bernoulli approximation
with error at most 2^-K by coupling on the timeout event. This is a bounded
record approximation, not full A2 instrument equivalence.

## Check planned for this published milestone

The written claims above precede their computational check. A bounded exact
checker will enumerate prefix trees for p and 1-p, verify timeout and joint
laws, reject timing-independence and flipped-output mutants, and check all
qubit partial-permutation shapes against the fixed-identification witness.
It will use integer/Fraction arithmetic and Q(sqrt(2)) comparisons, write
structured evidence, and fail before printing a pass if any control fails.
Finite prefixes test implementation; the geometric-tail and cone arguments
establish the unbounded statements at the written-proof level.

## Primary sources and relation to existing results

- Main `de6fe29324ade8a0826c18f7829786086dd590da`,
  `verification/lean-mathlib/OIBridge/FrozenSourcing.lean`:
  `nonnegBounded_of_bijectionLevel`, `obsTheory_nonnegBounded`,
  `preservesNonneg_of_approx`, `mixImage_not_preservesNonneg`.
  Source declarations read; no Lean build or new formal theorem asserted.
- Programme `2d555f17c23bea31d32b3f5eb4c49d245b413a76`, prefix
  `verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/`:
  `mc-node3/NODE.md` section 2 and its applied final review, `mc-node6/NODE.md`
  record-versus-operation distinction, and the reviewed countability material
  cited by the preceding states/dynamics report. Off-main sources remain WIP
  provenance; a dependent enduring claim requires their evidence on main.
- P. Flajolet, M. Pelletier and M. Soria, *On Buffon Machines and Numbers*,
  <https://arxiv.org/abs/0906.5560>. The primary-source abstract establishes
  existing exact irrational-probability sampling from fair coins; novelty is
  not claimed for that phenomenon or for the threshold algorithm.

The closed-invariant obstruction is an application of existing research.
The concrete deliverable here is the explicit separation between a working
almost-sure irrational sampler, its additional resource/availability cost,
and the exact joint-timing law that a proposed instrument must handle.
