# Causal readback discovery — result amendment 1: T1 preparation scope

This is an append-only correction to `verification/CAUSAL-READBACK-DISCOVERY-RESULT.md` on PR #542.
It does not alter either frozen preregistration file, any W/S/R clause, any mandatory control, the T2/T3 countermodels, the same-window P-divisibility countermodel, or the T4 closure.

Where the execution result states unqualifiedly that

`CausalReadback -> C4w`,

this amendment controls the scope.

## Correction

`CausalReadback` was frozen on a rooted realization

`R = (V, H, phi, mu_H)`

and does not contain a standalone visible initial distribution `p_0` on `V`. By contrast, manuscript C4w is a property of a visible **process law**: positive-probability visible histories sharing a current visible state must induce different next-step laws.

The T1 argument in the execution result conditions on two different rooted preparations `X_0=a` and `X_0=b`. Therefore it implicitly forms a process in which both witness roots occur with positive probability. That support hypothesis must be named.

The earned statement is:

> **T1, preparation-scoped.** If a declared realization satisfies `CausalReadback` with witness roots `a != b`, and the standalone visible initial distribution satisfies `p_0(a) > 0` and `p_0(b) > 0`, then the induced visible process satisfies C4w on the corresponding accessible window.

In particular, any full-support visible initial distribution supplies the required root support.

The proof is the first-separation argument already recorded in the execution result. The only correction is that the two rooted storage histories have positive probability in the same process only after the visible-root support hypothesis is supplied.

## Per-root refutation

The unqualified implication is false if it is read as applying to every standalone visible preparation, and in particular to each fixed-root law.

Use the exact finite reversible T3 realization already in the result, whose rooted family is

`Gamma_0 = I`, `Gamma_1 = B_(3/4)`, `Gamma_2 = B_(5/8)`

and which satisfies the full frozen W/S/R parent with witness roots `0` and `1`, storage time `s=1`, and read time `t=2`.

Under a mixed visible initial law with positive mass on both roots, the two positive-probability histories `(0,0)` and `(1,0)` share current visible state `0` at time 1 and have different time-2 laws (`B_(5/8)` row 0 versus row 1). Thus C4w is present, exactly as the corrected T1 theorem predicts.

Under the fixed-root preparation `p_0 = delta_0`, every positive-probability time-1 history has initial root `0`; for each current visible value there is only the single visible history `(0,x)`. Hence there are no two positive-probability visible histories with the same current value and different pasts, and C4w is absent on this two-step window. The same holds for `p_0 = delta_1`.

Therefore:

> A parent-positive rooted realization does **not** force C4w under every standalone visible initial preparation. C4w is preparation-support sensitive even when the rooted transition family and hidden prior are held fixed.

This is distinct from the hidden-prior dependence already recorded in the round. Here `mu_H` and the entire rooted family are unchanged; only the standalone visible root law `p_0` changes.

The exact mixed-root positive witness and both fixed-root negative controls are machine-checked by
`verification/lean/causal_readback_t1_scope_probe.py`, which is included in the required Numerical probes gate.

## Consequences for the round headline

The T2, T3 and T4 conclusions are unchanged:

- `CausalReadback -> C4e` is false;
- `CausalReadback -> C4r` is false;
- same-window `CausalReadback -> PIndivisibleWithin K` is false;
- no universal same-window `C4cr` can both follow from the parent and suffice for P-indivisibility.

The T1 entry in the final classification is corrected to:

- `CausalReadback + witness-root support in p_0 -> C4w`: **TRUE**;
- unqualified `CausalReadback -> C4w` for arbitrary standalone visible preparations: **FALSE**;
- fixed-root `delta_a` laws can be C4w-negative even when the same rooted realization is parent-positive.

Accordingly the headline is best read as **Outcome C on the audited accessible window conditional on witness-root preparation support**, together with the already-recorded E-type hidden-prior qualification and this additional visible-preparation support qualification.

Strictly, the frozen A–E taxonomy did not include a separate label for “parent calibration passes but T1 needs visible-root support.” This amendment does not invent a new outcome class after execution; it records the exact support condition under which the frozen Outcome C statement is earned and leaves the unqualified T1 implication marked false.

No manuscript edit is made here. No stronger physical preparation principle is inferred. The separate recurrence-scale route remains a distinct next audit.
