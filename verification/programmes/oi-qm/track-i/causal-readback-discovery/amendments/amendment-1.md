# Causal readback discovery — append-only amendment 1

This amendment is committed after `verification/programmes/oi-qm/track-i/causal-readback-discovery/preregistration.md` at preregistration head
`df3e0f21b8a3493a523dd123b0979c6bd0bf46ed` and before any Lean/probe execution for the round.

It does **not** modify the frozen preregistration text, change any clause, change any target, add or remove any control, redefine any C4 predicate, or alter any admissible outcome. Where this amendment sharpens an attribution or execution expectation, this amendment governs the interpretation of the frozen text.

## Reason for amendment

Independent review instantiated mandatory control N1 on the standard b51 XOR/history-memory realization used by the earlier C4 audit (`review4_probes.py`, `build(kXOR, 2, 2, 2)`), whose hidden state contains a history ledger, randomness tape, and clock, with the hidden preparation uniform over seeds.

On that standard ledger completion, with a representative choice `w = 1`, `s = 1`, `x = 0`, the three physical clauses do **not** behave as the motivating gloss around N1 might suggest:

- **W holds.** Under the same hidden/tape seed, changing the visible root changes the post-write hidden ledger because the root is appended to that ledger.
- **S holds.** The visible state at the storage time can be root-independent while the root-conditioned hidden laws at that same visible value remain different because the ledger retains the root.
- **R(1) holds.** Holding the visible storage state fixed and propagating from the two root-conditioned hidden laws produces different later visible laws.
- **R(2) fails.** The rooted one-time marginals at the designated later time are equal (`Γ₂ = J/2` in the standard XOR control), so the parent predicate still rejects N1.

Therefore N1 remains a valid negative calibration control, but its rejection is carried by **R(2)** on the standard b51 realization, not by W.

## Attribution correction

The frozen W clause remains unchanged and retains its literal role: it excludes realizations in which the hidden state never acquires any information from the visible preparation under a same-seed comparison.

However, the standard b51 response-table/history-ledger realization is **not** such a realization. Its ledger genuinely acquires root information. Accordingly:

> The N1 control must not be reported as though W excludes the standard pre-sampled/history-ledger completion. On that completion W, S, and R(1) are expected to hold; N1 is rejected because R(2) fails.

The preregistration's hedge about ledger-writing completions is therefore promoted from a possible contingency to the **expected behavior of the standard b51 realization**.

## Load-bearing status of R(2)

R(2) is load-bearing for the current parent calibration. It is the clause that requires the hidden causal distinction to return as a separation in the rooted one-time visible law rather than merely as history-conditioned dependence.

This is deliberately stronger than W/S/R(1) alone and is close to the “later separation” half of `C4e`, but it still does **not** contain `C4e`'s earlier-collision requirement.

This must be reflected explicitly in the execution report: if a theorem or counterexample turns on R(2), that dependency is to be named rather than hidden inside the parent label.

## Consequence for T2

The preregistered hedge that

`CausalReadback -> C4e`

may fail is now structurally motivated.

The parent contains a later-separation requirement through R(2), but none of W, S, R(1), or R(2) by itself requires an earlier exact collision of rooted marginals. Hence T2 reduces to the nontrivial question of whether the parent clauses together force such a collision indirectly.

The working expectation for execution is therefore:

> **T2 is likely false unless an additional theorem unexpectedly derives the collision condition from W/S/R.**

A countermodel with W/S/R satisfied, later rooted separation present, and the earlier rooted rows merely close-but-unequal would refute T2 without threatening the physical parent.

This is an execution expectation only, not a changed target or a changed admissible outcome.

## Consequence for T3

Likewise, R(2) alone does not imply `C4r`.

R(2) requires a later rooted separation, but `C4r` is a revival/comparison statement: the later distinguishability must exceed the earlier distinguishability at the relevant times. A realization may already have equal or greater row separation at the storage time and therefore satisfy R(2) while failing revival.

Accordingly:

> **T3 remains genuinely open.** It is not to be treated as automatic from the parent merely because R(2) supplies later separation.

If T2 fails and T3 also fails, the round may proceed to the preregistered `C4cr` decision only under the original T4 discipline: any fallback predicate requires a separate preregistration amendment and may not encode P-indivisibility or the nonexistence of a propagator by definition.

## Controls unchanged

All four mandatory controls remain exactly as frozen:

1. XOR/history-memory control N1: must fail the parent while satisfying history-memory content; on the standard b51 ledger realization, expected failure mechanism is now explicitly **R(2)**.
2. Delayed-revival positive control: must satisfy the parent.
3. Uncoupled reversible-product control: recurrence alone is not readback.
4. Prior-dependence pair `φ(x,h) = (x XOR h, h)` under uniform versus `δ₀`: proves the divisibility verdict is not a property of `(φ, partition)` alone.

No control is weakened or strengthened by this amendment.

## Frozen status after amendment

The discovery round remains preregistered and falsifiable. In particular, Outcome D remains available if the parent itself fails calibration, and the parent is not to be patched after seeing results merely to preserve a desired implication.

Status: **append-only attribution amendment recorded before Lean/probe execution; original preregistration remains byte-identical and authoritative except for the interpretive corrections stated here.**
