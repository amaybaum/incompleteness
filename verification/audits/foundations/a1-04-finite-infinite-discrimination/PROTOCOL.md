# A1-04 · Finite-resource tests of total carrier cardinality

**Paper-only protocol. Assessment pending.** [Accountable issue #1330](https://github.com/amaybaum/incompleteness/issues/1330) · [Owner authorization](https://github.com/amaybaum/incompleteness/issues/1330#issuecomment-6916731773) · [Worker plan #1320](https://github.com/amaybaum/incompleteness/pull/1320). The source snapshot is [main at 0283ba31](https://github.com/amaybaum/incompleteness/tree/0283ba315e8c8a8f1465a91eea8613f9aa213ab5). The goal under [#1169](https://github.com/amaybaum/incompleteness/issues/1169) is to identify what evidence about total finiteness a bounded observer can obtain. [SUBSTATE-1 #1007](https://github.com/amaybaum/incompleteness/issues/1007) and [A1-NECESSITY #1055](https://github.com/amaybaum/incompleteness/issues/1055) give the relationship to observer-relative finiteness and recurrence.

## 1. Carrier classes

Both classes specify an autonomous discrete-time reversible update, a normalized preparation law and a measurable one-bit readout. Here a carrier is the space of total microscopic states of the model, including the rest of the system outside the readout. A physical interpretation must account for any clock, controller, preparation source and record store that can feed back into that dynamics. Membership is defined by microscopic state space and dynamics before comparing record distributions.

| Class | Admission independently of a record law |
| --- | --- |
| \(\mathcal F\), finite total carriers | A finite nonempty state space \(\Omega\), a permutation of it and a probability law for preparation. Each member has a size bound \(|\Omega|\). The class has no independently specified common size ceiling. |
| \(\mathcal I\), infinite total carriers | One genuinely infinite state space \((\Omega,\Sigma)\), a measurable bijection with measurable inverse, and a countably additive normalized preparation law. For example, an unbounded site set with a finite alphabet can supply an infinite product carrier. The one-bit readout remains local to the specified interface. |

An unbounded family of finite approximants lies in \(\mathcal F\) member by member. Exact record-law equality is compatible with different preparation measures on the two microscopic spaces. When invoking a stationary spectral calculation, the reference measure for that calculation must also be invariant. A finite instantaneous alphabet is available at the model interface by stipulation. Its all-time record capacity is a separate question. [Main §1.2](https://github.com/amaybaum/incompleteness/blob/0283ba315e8c8a8f1465a91eea8613f9aa213ab5/papers/Main.md#L40-L60)

## 2. Protocol and resource budget

Fix the following budget for the paper comparison. The two settings give short and long read schedules under the same preparation and free dynamics. The recording budget is sufficient to keep the full record at either setting.

| Component | Shared rule and bound |
| --- | --- |
| Preparation | One attempt to arm the readout and obtain the preparation ensemble for that model. Use the same declared preparation label at both settings, with one bounded preparation slot \(T_{\rm prep}\). Record ready, rejected or deadline. The paper controls specify the ensemble and ideal status explicitly. |
| Setting | Choose \(K=4\) or \(K=8\) before preparation. The setting fixes only the number of scheduled updates and is kept in the record. Compare laws at the same setting. |
| Intervention | Leave the state to its autonomous update, with the identity as the sole state intervention. A read schedule gates the recorder. The paper protocol assumes a passive readout of the bit. Physical passivity and timing are source requirements. |
| Readout and precision | At ticks \(0,\ldots,K\), resolve one binary value of \(b_t\), at a fixed step resolution \(\Delta t\). Record any ambiguous, absent or late reading as a failure, then stop. Every tick slot carries one of \(0,1,\mathsf{failure},\mathsf{padding}\). |
| Complete outcome | Keep the setting, preparation status, all scheduled bit or failure records, stop reason and stop tick. Encode run termination as scheduled, preparation failure, read failure or deadline. A failed attempt stays in the comparison. |
| Time and storage | At most eight free updates and nine timed reads, with deadline \(T_{\rm prep}+8\Delta t\), and at most 32 retained bits for the complete log. The setting uses one bit, the preparation status two, nine slots use 18, the stop reason uses two, and the stop tick uses four. A preparation failure can use tick zero and a separate stop reason. No reset, repeated trial or unbounded external setting stream is used. |
| Precision for probabilities | Use \(\eta=1/16\) in total variation as the maximum calibration error per model's complete-log law when considering a physical separation. This is a tolerance for evaluating a stated law and would need a separate calibration source. It is independent of the one-bit read resolution and supplies no empirical estimate from one attempt. |

For each setting let \(P_M\) be the model's law on complete attempted logs, including failures. A sufficient class separator at this precision is a log event \(E\) with
\[
\inf_{I\in\mathcal I}P_I(E)-\sup_{F\in\mathcal F}P_F(E)>2\eta
\]
or the reversed inequality. The two deviations of at most \(\eta\) then leave a strictly positive probability gap for \(E\). For the identifiability check, one pair that agrees exactly at both settings rules out a uniform discriminator for these two classes under this protocol. Contrasts on a narrower pair must identify the extra model restrictions used.
