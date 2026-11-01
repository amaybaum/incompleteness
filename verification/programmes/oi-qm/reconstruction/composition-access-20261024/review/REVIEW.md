# Separate-author review: composition and observer access

**Verdict: ACCEPT within the stated conditional theorem and finite toy-control
scope.** No blocking findings remain in author commit
`a7f22c38503c710f91567628658ed627172cecdf` on draft PR #912. This is an internal
separate-author proof and computation review, not external review, Lean
certification, premise adoption, or a native instrument construction.

## Reviewed object and evidence

Directory: `verification/programmes/oi-qm/reconstruction/composition-access-20261024/`.
The substantive computation checkpoint is
`34b631c415b43fb7d9c8a3a96f22f42e92096d71`; the accepted child changes only
`REPORT.md` and its manifest. Both reports were fetched by immutable commit.
The accepted report makes the randomized-controller independence condition
explicit. Its SHA-256 is
`fe7033502df5b041d48e941f166da7e5092ec72f289d4a6059b782c689a5b350`.

The author checker and retained structured result were fetched independently.
Both normal and optimized author execution reproduce the retained result
byte-for-byte. `independent_checks.py` imports no author code and independently
computes the finite controls; normal and optimized runs agree. The script
prints the structured `independent-result.json` and exits nonzero on a failed
check. Python's standard library and exact rational arithmetic suffice.

## Proof audit

The deterministic-controller theorem is valid as stated. For each history,
the unnormalized physical branch measure stays in its next admissible cone.
The fixed decoder and branchwise intertwining identity then identify its
decoded operator with the reference branch operator. Induction, followed by
trace, gives full-history probabilities without dividing by a herald
probability, including zero-mass and failure branches. A matched terminal
effect gives the joint terminal law.

The admissible-cone restriction is material: positivity is required on those
measures, not on every physical point mass or the entire linear span. The
decoder is stage-dependent but not selected after seeing the history. The
report correctly treats this as a sufficient comparison contract and does
not require equality of latent physical states. It also keeps native
boundary compatibility as a hypothesis; a clean endpoint alone does not
establish that compatibility.

The corrected randomized-controller extension is valid. Merely matching a
controller coin's public-history marginal would be insufficient: a fair
hidden bit q, setting a=q, and output q XOR a give a deterministic zero,
whereas an independent fair setting gives a fair output. The independent
checker obtains joint setting/output TV distance 1/2. The accepted text
requires conditional independence from the residual boundary, or requires
the correlated controller to be included in the joint boundary contract.

The fresh-seed condition explicitly excludes the seed itself from the other
stage inputs. Independence conditional only on the public history can still
leave dependence on the hidden input; the herald-conditioned example proves
that distinction. Freshness is correctly described as a sufficient method
for establishing the contract, not as a necessary property of all possible
implementations.

## Independent finite recomputation

The physical toy transition was reconstructed using sixteen equiprobable
atoms: four failure atoms and twelve success atoms. The reference was
reconstructed separately as a classical transition matrix on diagonal qubit
states. Direct enumeration uses 256 physical seed pairs per two-stage case.

| Check | Independent result |
| --- | --- |
| Local decoded transition maps | All 12 agree with the reference |
| Depth-two adaptive policies and initial physical states | All 324 cases agree on full records and terminal decoded bit |
| Equal marginals, wrong record/carrier correlation | TV 1/2 |
| Initially independent seed after equality herald | Hidden-input correlation produces TV 1/2 |
| Post-Y 5:3:2 versus 5:2:3, either y | Terminal X TV 0; terminal R and full-carrier TV 1/10 |
| Altered success/failure mass | TV 1/4 |
| Revealing private garbage | TV 1 |
| Hidden-state-correlated controller coin | Joint setting/output TV 1/2 |

These controls are non-vacuous: the physical garbage fibers differ, the
declared decoder identifies them, and enlarging access separates them. The
calibration computation checks the supplied target; it does not derive that
target or demonstrate a native terminal-R instrument.

## Source and application boundary

The programme acceptance rule at #885 commit
`2d555f17c23bea31d32b3f5eb4c49d245b413a76` and the #910 handoff at
`5f6786d6f02605f8e8821a536b678495e19015da` were read independently. The report
preserves their requirements for failures, joint records, the informative
private prefix, supplied calibration and the actual two-slice neighborhood.
The review did not re-prove the inherited native transport theorem.

The induction establishes a conditional statement for every finite depth;
the bounded enumeration is only a control of its application, not its proof.
The diagonal toy sector supplies no evidence of coherent quantum dynamics.
Native reset, admissible-boundary closure, actual access policy, target
coverage, unrestricted menu, composite systems and Bell structure remain
open application obligations. The serial theorem does not imply them.

The corrected record is accepted without further changes. Before an enduring
claim lands, off-main source dependencies must satisfy AGENTS §A.42. Review
acceptance does not authorize a merge or change the programme's status.
