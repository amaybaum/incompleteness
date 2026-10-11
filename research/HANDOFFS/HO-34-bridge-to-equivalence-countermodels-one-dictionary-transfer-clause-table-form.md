# HO-34 (v1) — bridge → equivalence, countermodels: the two dictionaries are one map; the transfer clause in table form; two weaker clauses defeated as sufficient bridges

**From** `research/bridge` (round 4, node B15; the bridge's proposal HP-12). **To** `research/equivalence` (owner of
`EqvK2Schema`; S6) and `research/countermodels` (pair-cone checks through the dictionary). Written by the coordinator
from the source thread's committed record; version 1, 2026-10-11. Every statement is an invariance statement.

## Statements and labels

1. **One dictionary** (B15-1). `BridgeConverge.lean` imports the bridge's `BridgeDictionary` (round 3) and the
   equivalence thread's `EqvK2Schema` (`research/equivalence` @ `c10dbaee`, blob 659ae36c, carried verbatim with
   attribution on the dev branch only). `pauli`, `tokMat` and `dict` converge by `rfl`; hence the bridge's dictionary
   is injective (the equivalence thread's `dict_injective`), Hermitian-valued, and is `dictEquiv` onto the Hermitian
   matrices. Round 3's open injectivity (HO-21 / HP-8) is closed in design. Label: CONJECTURE ([D]: run 38117986499,
   21/21 standard).
2. **The transfer clause in table form** (B15-1). With `transferMap U ω := coordOf (Ad(1 ⊗ U)(dict ω))`,
   `TransferClause 𝓘 K` (BridgeDictionary.lean:343, the existential form) holds exactly when `K` is invariant under
   `transferMap U` for every admissible unitary `U` of the class (`transferClause_iff`, both directions); the clause is
   antitone in the class (`transferClause_mono`). Label: CONJECTURE ([D]).
3. **(b) for the phase circle, in table form** (B15-2). On a pair cone with `TransferClause substratumClass K`,
   `actT (rotZ c s) K ⊆ K` for every `c² + s² = 1`, hence for the kernel's flow `rotLin t` and at the 3-4-5 point; the
   clause for the stated access gives the NOT on the target (`transfer_nflip_table`). Controls: `Q3` satisfies the
   clause for every class (`transferClause_Q3`), `{e01}` fails it (`transfer_counter`). Label: CONDITIONAL (on the
   clause, which nothing at L sources) — [D].
4. **Two weaker clauses defeated** (B15-3), in the owner's words. *"The transfer clause for the stated access"*: its
   admissible one-token unitaries are exactly `c·1` and `c·X`, `|c| = 1`, whose transferred maps are the identity and
   `actT nflip`, which permute `Z_F`; so K(Z_F) satisfies it — FAILED as a sufficient bridge (K(Z_F) is not excluded).
   *"A finite group"* — the transfer clause for the stated access with the quarter phase: the transferred group on the
   target is `⟨actT nflip, actT R_z(π/2)⟩`, of order 8, without `R_z(θ₀)`; every finite group with the gate leaves an
   exotic cone (R6 Table A3; claim (D)) — FAILED, CONDITIONAL on claim (D) [A]. **Coordinator's check (X5):** the
   order 8, the absence of `R_z(θ₀)`, the unitary scaled partial permutations of one token, and the permutation of
   `Z_F` by `nflip`, all exact.

**Assumption-watch marker.** "The dictionary was the same in both threads" was a textual coincidence until B15:
`rfl` now certifies it in design; results stated through either module transfer without re-proof.

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `a34d20b5` (B15 closed at `1e2b6bc3`) |
| proposal | `research/bridge/handoff-proposals/HP-12-one-dictionary.md` |
| module | `research/bridge/lean/BridgeConverge.lean` (sha256 3f7155ca…; dev blob d09c7050 on `dev-bridge/r4-final` @ `bf8ba746`); dispatch 2's failure (`open scoped Matrix` missing: `ᴴ` unparsed at 79, 85, 96, 151, with cascades) kept as `lean/BridgeConverge.run38115337569.lean` (1e4cbb86…) |
| CI | run 38117986499, job 114406679644: "Built OIBridge.BridgeConverge (2.2s)", 21/21 `#print axioms` on `[propext, Classical.choice, Quot.sound]`, `lean-axioms` PASS 6083; verified at the step level — `CI-RUNS-R4.md` |
| preflight | `experiments/b15_preflight.py` 12/12 (run 1 kept, a list-order harness error in P7), replayed byte-identically by the coordinator |
| coordinator audit | `AUDIT-BRIDGE-R4.md` (method 7); `bridge/indep_checkB4.py` run 1 (X5) |

## What the receiving threads may assume

Items 1–4 at their labels: one dictionary for both threads' statements (the equivalence thread's `dict_injective`,
`dict_coordOf`, `coordOf_dict` are available to the bridge's results and conversely); the clause's table form as a
Lean statement that builds against the kernel at L and Mathlib v4.33.0 with the standard axiom footprint; the two
defeats as exact facts.

## What they may not assume

- certification, or any census disposition;
- any sourcing of the transfer clause: every statement of item 3 has it as a hypothesis;
- availability of any operation: the clause is an invariance clause (HO-33 item 6 corrects B9-1's wording).

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-34 v1` and records in its `LOG.md`
whether and how it relies on it.
