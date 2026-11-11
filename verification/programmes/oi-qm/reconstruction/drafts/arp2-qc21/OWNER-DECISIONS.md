# Q-C2-1 owner rulings and bounded implementation authority

Owner: amaybaum. Recorded 2026-11-10T20:53:48Z (UTC) at [#1169 comment 6778994857](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6778994857).
Decision baseline: accepted r14d paper checkpoint `f634f8e3f2115ef28d11616e0d195221d3ce9cb3`.

The owner answered this question in the coordinating Codex chat:

> Do you explicitly approve R1–R7 defaults, with initial S_max = 100000; R8 alternative; R9 default; and
> R10 narrowing at accepted checkpoint f634f8e3, and authorize Codex to apply them, update and independently
> review the implementation, run permitted static checks/non-scientific self-tests and ordinary PR CI,
> and prepare a separate design-run request? Scientific computation, local A3 fixture solving, design
> runs, dispatch, F/E, frozen-splice publication, merges and new physical premises would remain unauthorized.

**Owner answer: “Approve rulings and bounded implementation”.** The earlier recommendation was proposed;
this subsequent explicit answer is approval. It grants no execution or integration authority.

| Ruling | Approved selection |
| --- | --- |
| R1 | Default form/floor/nonincreasing post-red-run rule; initial S_max = 100000. |
| R2 | Default whole-round VOID on a red fixture control at S1/E. |
| R3 | Default full 1203 × W_max reported-only term. |
| R4 | Default reference selection with that whole term. |
| R5 | Default raised caps and budget for B-P alone. |
| R6 | Default fail-closed S1 measurements binding, including expiry/deletion. |
| R7 | Default imported reclassification of changed tables; no re-decision. |
| R8 | Alternative: the E designation quotes order.json and every E-entry digest; no separate ratification comment. |
| R9 | Default unresolved-completion reporting, no UPR-BC label/reclassification or Level change. |
| R10 | Narrowing: checks remain landing conditions, without enduring claims that unretained host-time checks passed. |

Preregistration r15 gives the operative definitions and dependent-site revisions. Historical r14d
decision/disposition/implementation-plan files describe their own earlier checkpoints; they do not
make the selected R1–R10 choices pending again. Unmeasured budgets, source pins, owner commitments and
other pre-F prerequisites remain pending. No stress measurement or scientific outcome is supplied here.

Codex writes the bounded implementation. A separate non-author reviewer must inspect its exact pushed
checkpoint; the paper acceptance is not script certification. Permitted static/non-scientific tests
and ordinary PR CI are distinct from future scientific/local-A3/design/stress/gate/decisive execution.
The current research branch is not a native round or workflow-splice tree. No F/E, freeze, dispatch,
merge or new premise follows. Physical source NOT PASSED; Q-C2-2 inactive; #1210/#1216 untouched.

## 2026-11-11 subsequent B1 owner decision (distinct from R1–R10)

Owner: amaybaum. Recorded 2026-11-11T02:02:14Z (UTC) at
[#1169 comment 6784808669](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6784808669).

The question put to the owner, verbatim: "The B1 amendment to Q-C2-1's checker and preregistration (#1218) needs
your decision. Which version do you approve?"

**Owner answer: "Approve, marker = skipped (Recommended)"**. The text of the chosen option, verbatim:

> A42 job and ARP-1 keep step: success on dispatch, skipped otherwise. KTRANS marker: must be skipped and the
> axiom-report step must succeed; a marker success fails. All else success. Mutation-tested both ways. I record your
> decision verbatim on #1169/#1218.

The recorded scope, verbatim: "This approves only the B1 amendment to C.7 6/6′ and the checker's expected-conclusion
rule." "Every other job and step must succeed. Every unlisted skip fails. The rule's `if:` texts must match D's
`verify.yml` byte for byte." "It authorizes nothing else: no design, gate or decisive run, no dispatch, no F/E
designation, no merge." It does not supply the unresolved D/T0, physical source, retention commitments or budgets.

## 2026-11-11 execution base D (nit N1)

Owner: amaybaum. Recorded 2026-11-11T07:19:40Z (UTC) at
[#1169 comment 6789676675](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6789676675).

The question put to the owner, verbatim: "Q-C2-1 needs an execution base D before F. Which commit should it be?"

**Owner answer: "Current main (Recommended)"**. The text of the chosen option, verbatim:

> Pin D to main as it stands when the round PR is opened (cac5d264 today, unless main moves). Code's D_SHA and
> preregistration updated to match.

The same answer selected these writer tasks, verbatim: "Remove revision notes (N9)", "Try activity-history read" and
"Request B2 gated run", with option texts:

> Delete the r14a–r14d revision notes from the preregistration so it states only current rules; ChatGPT reviews.

> One read-only attempt at the GitHub activity endpoint for the #1218 branch to see whether T0 evidence is
> retrievable; nothing inferred if it fails.

> Prepare (not run) a scoped request for you to authorize executing the gated checker self-test that contains the B2
> tests.

The recorded scope, verbatim: "This decides D only. It authorizes no round PR, F/E designation, dispatch, scientific
run or merge. The B2 item is a request to prepare, not an authorization to execute."

## Writer role (not an owner decision recorded on GitHub)

From `98582070` the writer for Q-C2-1 implementation corrections is Claude, confirmed by the owner on 2026-11-11 in
the coordinating session and stated in the writer checkpoint
[#1218 comment 6785751650](https://github.com/amaybaum/incompleteness/pull/1218#issuecomment-6785751650); ChatGPT
reviews. Codex's and ChatGPT's earlier authored work and reviews remain historical.
