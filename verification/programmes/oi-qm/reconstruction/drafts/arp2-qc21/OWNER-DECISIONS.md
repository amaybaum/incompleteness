# Q-C2-1 owner rulings and bounded implementation authority

Owner: amaybaum. Recorded 2026-11-10 at [#1169 comment 6778994857](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6778994857).
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
