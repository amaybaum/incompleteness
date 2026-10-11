# HP-12 — one dictionary, and the transfer clause in table form

From `research/bridge`, node B15 (round 4). Proposed for the equivalence thread (owner of `EqvK2Schema`) and the
countermodels thread (pair-cone checks through the dictionary). The coordinator routes.

## Statements and labels

Every statement is an invariance statement.

1. **One dictionary** (B15-1). `BridgeConverge.lean` imports the bridge thread's `BridgeDictionary` and the
   equivalence thread's `EqvK2Schema` (`research/equivalence` @ `c10dbaee`, sha256 `0bc6da00…`, carried verbatim with
   attribution on the dev branch only). Their `pauli`, `tokMat` and `dict` are one map by `rfl`; the bridge's
   dictionary is injective (the equivalence thread's `dict_injective`), Hermitian-valued, and is `dictEquiv`. This
   closes, in design, the injectivity HP-8 left open.
2. **The transfer clause in table form** (B15-1). With `transferMap U ω := coordOf (Ad(1 ⊗ U)(dict ω))`,
   `TransferClause 𝓘 K` holds exactly when `K` is invariant under `transferMap U` for every admissible unitary `U`
   (`transferClause_iff`); the clause is antitone in the class.
3. **(b) for the phase circle, in table form** (B15-2). Under `TransferClause substratumClass K`,
   `actT (rotZ c s) K ⊆ K` for `c² + s² = 1`, hence for the kernel's flow and at `θ₀`; the clause for the stated access
   gives the NOT on the target. Label: CONDITIONAL (on the clause, which nothing at L sources).
4. **Two weaker clauses defeated** (B15-3): "the transfer clause for the stated access" (K(Z_F) satisfies it) and "a
   finite group" (the stated access with the quarter phase transfers a group of order 8 without `R_z(θ₀)`; every finite
   group with the gate leaves an exotic cone, CONDITIONAL on claim (D)).

Labels for 1–2: CONJECTURE ([D]).

## Evidence

| item | pointer |
|---|---|
| module | `research/bridge/lean/BridgeConverge.lean`, sha256 `3f7155ca…`; dev blob `d09c7050` |
| CI | run 38117986499 (`dev-bridge/r4-final` @ `bf8ba746`), Mathlib bridge job 114406679644: "Built OIBridge.BridgeConverge (2.2s)", 21/21 `#print axioms` standard, `lean-axioms` PASS (6083), gate red only on `lean-manuscript`. Dispatch 2's failure (missing `open scoped Matrix`) kept as `lean/BridgeConverge.run38115337569.lean` |
| preflight | `experiments/b15_preflight.py`, 12/12 (run 1 kept, a harness error in P7), replay byte-identical |
| notes, results | `NOTES-B15.md`; `RESULTS.md` rows B15-1 … B15-3 |

## What the recipient may assume

Items 1–4 at their labels: one dictionary for both threads' statements; the clause's table form as a Lean statement
that builds against Mathlib `v4.33.0` and the kernel at L with the standard axiom footprint.

## What the recipient may not assume

- certification, or any census disposition;
- any sourcing of the transfer clause: every statement of item 3 has it as a hypothesis;
- availability of any operation: the clause is an invariance clause (B14-8 corrects B9-1's wording).
