# NOTES-B15 — one dictionary, and the transfer clause in table form

Node B15 of `research/bridge` (round 4). Base L = `9f9f8257`. Evidence levels as in NOTES-B14: [K] kernel at L; [D]
design module built in CI; [X] exact computation (`experiments/b15_preflight.py`); [W] written here; [A] audited
record. Reading (the coordinator's third addendum): every statement of this node is an invariance statement — the
transfer clause is the preservation of a pair cone by the one-token unitaries of a class — and none is about the
operational availability of an operation.

## 0. Question

The round-4 directive: converge the two statements of the two-token dictionary into one module that imports the
equivalence thread's `EqvK2Schema` (its `dictEquiv` and `dict_injective`) and states the bridge thread's
`BridgeDictionary` results through it; prove `transfer_phase` in table form (round 3 proved it with a dictionary image
on the right, B11-2, and left the dictionary's injectivity open). The second addendum: a RESULTS row recording that an
alternative weaker than a sufficient bridge fails names the alternative in those words. The third addendum: no
statement of independence without a full model; say of every row whether it is about invariance or availability.

## S0. Design, productivity test and predictions (written 2026-10-11T05:29:31Z, before any run or dispatch)

**Design.**
- **The module** `lean/BridgeConverge.lean` imports `OIBridge.BridgeDictionary` (round 3, built in run 38099134414)
  and `OIBridge.EqvK2Schema` (the equivalence thread's module, read on the coordinator's instruction at
  2026-10-11T04:04:10Z: `research/equivalence` @ `c10dbaee`, blob `659ae36c`, sha256
  `0bc6da00d5b9ba9c4a2f9390db31c15830a19bf1e30fc2ee6889cd9211281221`, built there in run 38101580750). The equivalence
  module is carried verbatim, with attribution, on the disposable dev branch only; this branch records its hash and
  carries no copy.
- **Convergence by definitional equality.** The two threads' `pauli`, `tokMat` and `dict` are the same expressions
  (the equivalence module says "the bridge draft's … verbatim"), so `rfl` identifies them; everything else is carried
  across by rewriting. Checked textually before dispatch (preflight P1).
- **The table form.** `transferMap U ω := coordOf (Ad(1 ⊗ U)(dict ω))`; `dict (transferMap U ω) = Ad(1 ⊗ U)(dict ω)`
  by the equivalence thread's `dict_coordOf` on the Hermitian matrix `Ad(1 ⊗ U)(dict ω)`. Then
  `TransferClause 𝓘 K` is equivalent to invariance of `K` under every `transferMap U`, `U` an admissible unitary, and
  with `dict_injective` the round-3 `transfer_phase` becomes `actT (rotZ c s) ω ∈ K`.
- **Controls.** Positive: `Q3` satisfies the clause for every class (conjugation preserves positivity), so the table
  form holds non-vacuously; countercontrol: the one-table set `{e01}` fails it (the quarter-turn moves `e01`).
- **Defeated alternatives (second addendum).** Two transfer clauses weaker than the monomial one are decided against
  K(Z_F) and the exotic cones: the clause for the stated access (`permClass`), whose one-token unitaries are `c·1` and
  `c·X` (`|c| = 1`), and the clause for the stated access with the quarter phase, whose transferred group on the target
  is finite.

**Productivity test (§A.31), fixed now.** B15 is a gem iff it yields a fact strictly stronger than "the two
dictionaries agree" that constrains a bridge or exposes a hidden assumption. Closing round 3's open injectivity and
naming defeated alternatives is ELABORATING unless a defeated alternative turns out to exclude K(Z_F) or every exotic
cone.

**Predictions.**

| id | prediction | check |
|---|---|---|
| S0-1 | The two threads' `pauli`, `tokMat`, `dict` are textually the same definitions, so `pauli_converge`, `tokMat_converge`, `dict_converge` close by `rfl` | P1; D2 |
| S0-2 | The sixteen matrices `σ_μ ⊗ σ_ν` are linearly independent over `ℚ(i)`, so `dict` is injective (`dict_injective` via the equivalence thread) | P2 (rank 16, exact); D2 |
| S0-3 | `transferClause_iff` (both directions) and `transferClause_mono` | D2 |
| S0-4 | At the 3-4-5 point, `coordOf(Ad(1 ⊗ zPhase(3/5, 4/5)) dict ω) = actT (rotZ (3/5) (4/5)) ω` exactly for every table, so `transfer_phase_table`, `transfer_flow_table`, `transfer_345_table` hold | P3 (exact, 6 random rational tables); D2 |
| S0-5 | `Ad(1 ⊗ X)(dict ω) = dict (actT nflip ω)` exactly, so the clause for the stated access gives the NOT on the target, and the monomial clause too | P4; D2 |
| S0-6 | Controls: `Q3` satisfies the clause for every class; `{e01}` fails the monomial clause | P6; D2 |
| S0-7 | Defeated, as sufficient bridges for (b): (i) "the transfer clause for the stated access" — its admissible one-token unitaries are exactly `c·1`, `c·X` with `|c| = 1` (P7), whose transferred maps are the identity and `actT nflip`, which permute `Z_F` (P5) and preserve K(Z_F) (B10-1, [X]), so K(Z_F) satisfies it; (ii) "the transfer clause for the stated access with the quarter phase" — "a finite group": its transferred group on the target has order 8 and does not contain `R_z(θ₀)` (P8), and every finite group with the gate leaves an exotic cone (R6 Table A3, the dimension corollary, [A]) | P5, P7, P8; [A] |
| S0-8 | D2: `BridgeConverge` builds with `BridgeDictionary` and the carried `EqvK2Schema`; every `#print axioms` line standard; `lean-axioms` PASS | D2 job log |
| S0-9 | Gem classification: ELABORATING | §4 |

## 1. Outcome of S0 (written 2026-10-11T06:38Z)

**The runs.** `experiments/b15_preflight.py`: run 1 (05:30:57Z) failed P7 on list order only, a harness error, and is
kept as `b15_preflight.run1.*`; run 2 (05:31:04Z) 12/12 green, replay byte-identical. Dispatch 2 (run 38115337569):
`BridgeConverge` did not build — the postfix `ᴴ` did not parse at four lines because the module did not open the
`Matrix` scope; every other error was a cascade, and the 14 declarations not downstream of the four reported standard
axioms. Failed text kept as `lean/BridgeConverge.run38115337569.lean`. Fixed by `open scoped Matrix`, with
`transferClause_Q3` restated so that its positive-semidefinite step is taken over one dictionary. Dispatch 3 (run
38117986499, job 114406679644): built ("[3657/3659] Built OIBridge.BridgeConverge (2.2s)"), 21/21 `#print axioms` on
`[propext, Classical.choice, Quot.sound]`; `lean-axioms` PASS (6083, no sorry); gate red only on `lean-manuscript`.

| id | outcome |
|---|---|
| S0-1 | confirmed [X] P1 and [D] (`pauli_converge`, `tokMat_converge`, `dict_converge` by `rfl`) |
| S0-2 | confirmed [X] P2 (rank 16 over `ℚ(i)`) and [D] (`dict_injective`, through the equivalence thread's `dict_injective`) |
| S0-3 | confirmed [D] (`transferClause_iff`, both directions; `transferClause_mono`) |
| S0-4 | confirmed [X] P3 and [D] (`transfer_phase_table`, `transfer_flow_table`, `transfer_345_table`) |
| S0-5 | confirmed [X] P4 and [D] (`transfer_nflip_table`, `transfer_nflip_of_substratum`) |
| S0-6 | confirmed [X] P6 and [D] (`transferClause_Q3`, `Q3_phase_invariant`, `transfer_counter`) |
| S0-7 | confirmed [X] P5, P7, P8 and [A] (§3) |
| S0-8 | not as predicted in dispatch 2 (the module failed to build); confirmed in dispatch 3 |
| S0-9 | ELABORATING (§4) |

## 2. The statements

All of them are invariance statements.
- **One dictionary.** The bridge thread's and the equivalence thread's `pauli`, `tokMat` and `dict` are one map by
  definitional equality; hence the bridge's dictionary is injective, Hermitian-valued, and is the equivalence
  thread's linear equivalence onto the Hermitian matrices [D]. Round 3's open injectivity (B11-2) is closed in
  design.
- **The transfer clause in table form.** `TransferClause 𝓘 K` holds exactly when `K` is invariant under the
  transferred tables `transferMap U` of every admissible unitary `U` of the class [D]. The clause is antitone in the
  class [D].
- **(b) for the phase circle, in table form, CONDITIONAL on the clause.** On a pair cone `K` with
  `TransferClause substratumClass K`, `actT (rotZ c s) K ⊆ K` for every `c² + s² = 1`, so in particular the kernel's
  flow `rotLin t` for every `t` and the 3-4-5 point `R_z(θ₀)` [D]. The clause for the stated access already gives the
  NOT on the target [D]. Nothing here sources the clause.
- **Controls.** `Q3` satisfies the clause for every class (conjugation preserves positivity), so the table form is
  not vacuous; the one-table set `{e01}` fails the monomial clause [D].

## 3. Defeated alternatives (the second addendum's naming)

Neither weaker clause is a sufficient bridge for (b):
- **"the transfer clause for the stated access"** (`permClass`): its admissible one-token unitaries are exactly
  `c·1` and `c·X`, `|c| = 1` [X P7], whose transferred maps are the identity and `actT nflip`; these permute `Z_F`
  [X P5] and preserve K(Z_F) (B10-1 [X]). So K(Z_F) satisfies it.
- **"a finite group"** — the transfer clause for the stated access with the quarter phase: the transferred group on
  the target is `⟨actT nflip, actT R_z(π/2)⟩`, of order 8, without `R_z(θ₀)` [X P8]; every finite group with the gate
  leaves an exotic invariant cone (R6 Table A3; claim (D)'s dimension corollary) [A].

## 4. Gem classification (§A.31)

ELABORATING, as predicted. The productivity test's alternative — a defeated clause that excludes K(Z_F) or every exotic
cone — did not occur: both weaker clauses admit K(Z_F) or an exotic cone. What is gained is the closure of B11-2's
open injectivity in design, the clause's table form, and the two named defeats.

## 5. Manuscript obligations

None.
