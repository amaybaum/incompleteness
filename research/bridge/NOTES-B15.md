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
