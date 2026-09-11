# Barandes indivisibility and correspondence bridge audit — Amendment 3: the referent of the BD axis

Base: `main` at `958cf8862efb6c6eb8b536bfd5acffbf69dc62b4` (post-PR #558, the bridge audit frozen).

Amends `verification/BARANDES-INDIVISIBILITY-BRIDGE-AUDIT.md`, frozen at blob
`b6727fa8df616e1a3f98e45d69b99b13554cda3e`, merged to `main` by PR #558.

This is an **append-only, execution-affecting amendment**, committed before the work it affects, as the frozen execution discipline requires. The preregistration itself is immutable and is not edited.

It is numbered 3 because Amendments 1 and 2 belong to other control-plane documents in this programme; this is the first amendment to *this* preregistration, and the number is kept globally sequential so that amendment references are unambiguous across the corpus.

## The defect

The frozen BD axis does not say **which** predicate on Barandes's side it classifies against, and the two candidates are not the same object:

- the **divisibility factorization equation** — the relation `Γ(t←t₀) = Γ̃(t←t′) Γ(t′←t₀)` with the intermediate factor required stochastic; and
- the **named class predicate** — membership in what the accepted text calls an *indivisible stochastic process*.

Q4 asks about the first. BD, as frozen, reads as though it classified the second, and its BD1 label — "exact definitional match" — could be reached from a Q4 equation match alone. That conflation matters precisely when the two come apart, and there is reason to think they do: `BD2` as frozen absorbs differences of "matching conditioning times, orientation, horizon, time domain", which would let a reviewer record `BD2` on the strength of a quantifier-domain difference while the named class predicate and `PIndivisibleWithin` are in fact predicates of different kinds.

The defect is in the preregistration, not in the execution. It was surfaced by a first primary-source pass before any answer was recorded.

## The repair

**1. Q4 is recorded separately and never folded into BD.** Q4 records whether the factorization equation matches after the stated transposition and time-index identification. Its answer stands on its own in the report and is not a BD verdict.

**2. BD classifies one thing only.** BD classifies whether `PIndivisibleWithin` matches Barandes's **actual notion of an indivisible stochastic process** — the named class predicate, as the accepted text defines it.

**3. An exact Q4 equation match does not imply BD1.** If membership in Barandes's named class can hold of processes that *satisfy* the corresponding divisibility factorization — a Markov chain being the salient candidate — then the class predicate and `PIndivisibleWithin` are predicates of different kinds, and the verdict is **BD3**, whatever Q4 returns.

**4. BD2 is narrowed.** `BD2` is reserved for the case where the two are genuinely the **same kind of failure predicate** and differ only by domain, horizon, or conditioning-time restriction. It is not available for a difference in kind.

The other labels are unchanged: `BD1` exact match of the class predicate with `PIndivisibleWithin`; `BD4` undetermined.

## What this amendment does not do

- **It records no answer.** Neither Q4 nor Q5 nor the BD verdict is settled here. The Markov-chain observation above is stated as the *reason the taxonomy needed fixing*, not as a finding; it reached the drafting session as a relay rather than as a citation that session could verify, and under the frozen evidence hierarchy a relay is not admissible evidence for a verdict. The determination still requires the executing round, with pinpoint source locations for each answer.
- **It does not change the nine questions.** They stand verbatim.
- **It does not change the recorded prediction.** `BR2` on the role axis, no prediction on the definition axis, both as frozen. In particular this amendment does not convert the prediction into `BR3` or into any BD label.
- **It does not change the BR axis.**
- **It does not relax the primary-source restriction, the controls, the evidence hierarchy, the non-doings, or the execution precondition.**

## Source-access practice

The frozen execution precondition lists three routes to primary-source access. This amendment records a constraint on the second of them without removing it: **whole copyrighted papers are not to be committed to this repository.** Where the repository route is used at all, it is limited to the short definitional and theorem excerpts an answer actually cites, carried with their provenance record. The cleaner routes are locally supplied source files, or executing the round in an environment that has access.

This is a constraint on practice, not a change to which routes the freeze admits.

## Execution hold

**No execution of the bridge audit occurs until this amendment is frozen and merged.** That includes the Lean transpose bridge: the frozen preregistration gates the round as a whole rather than target by target, and although the transpose theorem uses only this programme's own definitions and needs no primary source, starting it before this amendment is on `main` would break the freeze discipline for no gain.

**Ancestry, not chronology.** After this amendment is frozen and merged, every execution commit of the round descends from that merge, so the ordering is checkable from the history rather than attested.

## Provenance

Surfaced in review of the frozen preregistration against a first primary-source pass, after PR #558 merged and before any execution commit existed.

Status: **draft amendment; nothing here is frozen until the reviewer approves an exact commit and blob, and no execution begins until it is merged.**
