# NOTES-O8 — the exclusive readout as a premise

Thread `research/origin`, round 3, node O8. Base L = `9f9f8257`; kernel paths under
`verification/lean-mathlib/OIBridge/` at L. Evidence levels as in NOTES-O1 ([K] kernel at L, [D] design module on a
dev branch, [W] written argument, [X] exact computation, [A] audited archive record, [L] literature named, not
checked here). Script: `experiments/o8_exclusive.py`. Design module: `OIBridge/OriginExclusive.lean` on
`dev-origin/exclusive` (cut from L).

**Productivity test, fixed before starting (§A.31).** A finding counts only if it is strictly stronger than O5-T1a's
"one passive readout of any of the 14 partitions of {0,1}² restores the simplex" and either (i) states the premise in
the kernel's own vocabulary with a kernel-checked refutation on the stated access that names the landed declaration
it contradicts, or (ii) locates, by an exact check, what the premise restates (the Discrete witness, the balanced
mixer, or OI⁺-1's clause). A restatement of O5 in new words is a non-gem.

## S0 — predictions, written before the first run of `o8_exclusive.py` (2026-10-11T00:26:17Z)

The script's checks and the outcome expected for each, recorded before any run:

- **X1 (any finite carrier, any nontrivial cell).** For N = 2, 3, 4, 5 configurations and every cell size
  1 ≤ |C| ≤ N − 1, the closure of the uniform state under "read the cell, apply an outcome-dependent permutation,
  forget" reaches every point mass. Expected: yes in every case, and the reachable set is exactly the set of
  distributions with masses in (1/N)ℤ≥0 — C(2N−1, N) states: 3, 10, 35, 126 — since a step moves whole point masses
  and merges of any two points generate every grouping of the N atoms.
- **X1b (the Lean construction, replicated).** For every x ≠ y the explicit permutation of `exists_perm_sep` and the
  step of `reach_mergeInto` reproduce `mergeInto x y` exactly on random rational states. Expected: equal in every case.
- **X1c.** Collecting every configuration onto x₀ by successive merges from the uniform state gives the point mass at
  x₀. Expected: yes for every x₀.
- **X2 (control).** For the trivial cells C = ∅ and C = Ω the reachable set is the uniform state alone. Expected: yes.
- **X3 (the kernel's native readout).** On A = Fin 2 with ancilla sizes 2 and 3: every Lüders branch `localLuders k`
  equals the block pinching `blockPinch Prod.snd k` on all matrix units; the native readout is passive on every
  ancilla-classical matrix and not on a matrix with coherence between ancilla values; it is repeatable. Expected: all
  four hold.
- **X3b (which algebras the native readout observes passively).** For labellings refining the ancilla value
  (`Prod.snd`, `id`, a three-block refinement) the native readout is passive on the labelling's algebra with a
  state-dependent outcome law; for labellings with a block straddling two ancilla values (constant; the system
  value) it is not passive there. Expected: exactly so.
- **X4 (disguise test on the knowledge-balance toy {0,1}², all 24 permutations).** (a) KB-D readouts only: the body
  is the octahedron; a pure frame state is carried to a pure balanced state (x⁺) by a permutation; the frame face
  z = 0 is the single state z⁺, so KB-D's observe-and-forget is the body's frame dephasing; witness (1, 1/2).
  (b) KB-D plus one passive readout of any of the 14 nontrivial partitions: the body is the simplex, no pure state is
  balanced for any partition; the owner's numbers (1, 1/2) still appear from a point-mass seed when KB-D's
  observe-and-forget is used as the "dephasing", because it moves a pure state of the frame face (memory erasure,
  O1-T7a), and visibility is 0 with the passive (fresh-record) dephasing. (c) passive readouts only: simplex, no
  balanced pure state, visibility 0. Expected: exclusivity holds exactly in (a), and on this family exclusivity ⟺ a
  balanced pure state reachable from a pure frame state by a permutation.
- **X5 (OI⁺-1's clause).** Product-register composites of two toy tokens with local readouts: every CHSH value in
  [−2, 2]. Expected: yes (as O5-SRC2).
- **X6 (the continuous form).** On the circle tower with the cosine re-preparation law, adding one passive
  half-circle readout (conditioning) together with the rotations of the dyadic grid gives single-readout tables of
  rank 2^m + 1 (m = 1 … 5), growing; the cosine law alone gives rank 3. Expected: exactly so.

Run 1 of `o8_exclusive.py` (2026-10-11T00:29:53Z): `VERDICT EXCLUSIVITY-REFUTED-AND-LOCATED`, every prediction above met,
five countercontrols expected-false; replay byte-identical. One pre-run cleanup (an unused helper removed) before any run.

## 0. Verdict

1. **The premise, exactly.** In the kernel's operational vocabulary the exclusive readout has two clauses.
   - *KB-D1, the instrument* (sourced, O5-KB1): branch k = forget_memory ∘ `localLuders k`, the native Lüders selector of
     the frame register (`readout_is_localLuders` [K OperationalAssembly.lean:658]) followed by discarding the memory and
     attaching it uniformly (`uniformAttach` [K :492], discard [K :649]).
   - *KB-D2, the exclusivity*, relative to the algebra ⊕ᵢ M_{dᵢ} of a block labelling `blk` of the extended carrier
     A × Fin n: `ExclusiveOn blk T` — every available outcome family that is a passive instrument on the algebra
     (`CentralObservation.IsBlockPassiveInstrument` [K CentralObservation.lean:164]) has a state-independent outcome law
     there [D, definition]. On the classical carrier (O5's vocabulary) it is: no passive repeatable readout of any
     nontrivial cell on the body; there a passive repeatable readout of a cell *is* the restriction to the cell
     (`passive_repeatable_eq` [D]).
   - *Continuous form* (O6-I): the frame readout along u records sgn(u·λ) and re-samples λ from (a u·λ)⁺/π (sphere) or
     cos(λ − u)/2 on the outcome's half-circle (circle); exclusivity: no conditioning readout of any half-sphere (any
     nontrivial cell) is available.
2. **The no-go over the native readout.** In every `FiniteOperationalTheory` over a nonempty system the native readout
   *is* the kernel's block pinching of the ancilla values (`localLuders_eq_blockPinch`, `nativeReadout_eq_blockPinch`
   [D]), a passive instrument (`blockPinch_passive` [K CentralObservation.lean:486]) on every algebra whose blocks do not
   straddle two ancilla values, with a state-dependent outcome law (probability 1 on the pure state (a, 0), 0 on (a, 1)).
   So KB-D2 fails on every such algebra (`not_exclusiveOn_of_refines`; cases `not_exclusiveOn_ancilla`,
   `not_exclusiveOn_diagonal` [D]); in the substratum theory the ancilla exchanges are monomial, hence available, and
   `pureSeedPrep_available_of_swap` [K :675] makes every ancilla point mass preparable (`substratumTheory_pureSeed`,
   `substratumTheory_exclusivity_false` [D]). On the classical carrier, with every permutation, the passive readout of
   **any one** cell that is neither empty nor everything reaches every point mass from the uniform state
   (`reach_pointMass` [D]; exact replica X1, X1b, X1c for 2 ≤ N ≤ 5, every cell) — the generalization of O5-T1a's 14/14
   to every finite carrier and every nontrivial cell. Control: on a factor (the full matrix algebra, one block) KB-D2
   holds in every theory, by OI-N1 (`exclusiveOn_factor` [D], from `branch_scalar_on_block` [K :392]).
3. **What the premise costs.** On every algebra refining the ancilla value it contradicts `readout_is_localLuders`
   [K OperationalAssembly.lean:658] together with the structure field `FiniteOperationalTheory.readout_avail`
   [K :642] (and `readout_local` [K :643], from which :658 is derived): a theory with KB-D2 there is not a
   `FiniteOperationalTheory`. In state form ("no point mass is reachable") it contradicts `pureSeedPrep_available_of_swap`
   [K :675] as soon as the ancilla exchanges are available, as they are in the substratum theory (`substratumTheory`
   [K RouteB.lean:279], `substratumTheory_avail_conj` [K :284], `monomial_permMatrix` [K SubstratumInterface.lean:85],
   `ancSwap_unitary` [K OperationalAssembly.lean:566]). In continuous form it removes OI-STAGE's conditioning readout
   (A5 [A]); one conditioning readout of a half-circle restores growing rank (X6: 3, 5, 9, 17, 33).
4. **Disguise test.**
   - *Letter:* no non-monomial operator, no complex structure, no balanced state is named; it passes the owner's letter.
   - *Matrix carrier (kernel vocabulary): it presupposes the coherence.* KB-D2 relative to an algebra forces a block
     that straddles two ancilla values (`exists_straddle_of_exclusiveOn` [D]), i.e. coherence between ancilla values in
     the observed algebra; on a factor it is OI-N1. The substratum theory's reachable states are configuration-diagonal
     (O1-T3 [D] at its status), and only a non-monomial operation creates such coherence. So, transcribed to the kernel's
     carrier, the premise presupposes the output of the mixer it was meant to source: it **fails** the disguise test
     there.
   - *Field-neutral (the knowledge-balance toy):* on the family (exchanges, KB-D instruments, optional passive readouts)
     exclusivity holds exactly where a pure frame state is carried to a pure balanced state (X4a–X4c): it is the
     observation-side equivalent of the balanced mixer, relative to the exchanges and the KB-D instrument; it does not
     restate the Discrete witness's numbers, which KB-D alone reproduces from a point-mass seed by memory erasure when
     a passive readout is present (X4b).
   - *OI⁺-1's clause* (availability of a token operation in the pair context) is neither restated nor supplied: the
     premise is single-token, and product-register composites of its tokens are Bell-local (X5; O5-SRC2).
   Net: the premise is not a source of SRC inside the kernel's operational structure — there it is false on the stated
   access and, where it holds, presupposes the coherence; its realizations on classical substrata (the KB-D toy, the
   Kochen–Specker towers) are token-level models outside `FiniteOperationalTheory`'s native readout.

## 1. The kernel facts, and why the native readout is the obstruction

`readout_is_localLuders` [K :658] derives the native readout's form from its spectator independence: branch k is
`localLuders k`, which keeps the k-th ancilla block with all system coherence. On a matrix X its value at (p, q) is
X(p, q) when p.2 = q.2 = k and 0 otherwise — exactly the kernel's `blockPinch Prod.snd k` (`blockPart`, `blockProj`
[K CentralObservation.lean:79, :75]); this is `localLuders_eq_blockPinch` [D] (checked entrywise on all matrix units
for ancilla sizes 2 and 3 [X X3]). OI-N3's control `blockPinch_passive` [K :486] then says the native readout is a
passive instrument on the algebra of the ancilla values, and on any subalgebra of it (the configuration algebra, any
refinement [X X3b]); `blockPart_blockPart` [D] gives repeatability. OI-N1/N3 say what this means: a passive instrument
on ⊕ᵢ M_{dᵢ} reads only the block weights (`central_classification` [K :433]); complete passive observation exists
iff the algebra is commutative (`complete_passive_iff_commutative` [K :620]). KB-D2 is the statement that *no*
available passive instrument reads anything — true on a factor for every theory (`exclusiveOn_factor` [D]), false on
every algebra the native readout pinches with two nonempty blocks (`not_exclusiveOn_of_refines` [D]).

## 2. The classical carrier: any cell (the general form of O5-T1a)

`Reach C` [D] is the set of distributions reachable from the uniform one by the kernel's pure-seed pattern with every
permutation and the readout of the cell C (read the cell, apply an outcome-dependent permutation, forget the outcome).
`exists_perm_sep` permutes so that the cell holds y and not x; the step corrected by the exchange of the two images (and
the permutation back) moves the mass of y onto x (`step_eq_mergeInto`, `reach_mergeInto`); merging every configuration
into x₀ (`mergeInto_collectAt`, `reach_collectAt`) and the sum of the uniform state (`sum_uniform`) give the point mass
at x₀ (`reach_pointMass`). The construction is replicated exactly on 2424 cases (N = 2 … 5, every nontrivial cell, every
x ≠ y, three states each) [X X1b], and the closures computed by exhaustive search have exactly C(2N−1, N) states (3, 10,
35, 126: every distribution with masses in (1/N)ℤ≥0) [X X1]; the trivial cells reach only the uniform state [X X2]. A
passive repeatable readout of a cell is the restriction to the cell (`passive_repeatable_eq` [D]), so the theorem
applies to any passive repeatable readout of any nontrivial partition (coarse-grain it to one cell).

## 3. The continuous form

On the circle with grid rotations, one conditioning readout of half-circles reaches every elementary arc and the table
of first outcomes has rank 2^m + 1 (m = 1 … 5) — the cosine-law readouts have the same first-outcome statistics on these
preparations — while the cosine law alone gives rank 3 [X X6; O6 P1, K2]. The exclusivity is what keeps O6-I's tower at
finite rank; with it removed the tower is OI-STAGE's passive one.

## 4. Classification (§A.31)

- **NEW, O8-N1.** In the kernel's vocabulary the exclusivity clause is OI-N1's factor property: it holds on a factor
  for every theory and fails on every algebra whose blocks do not straddle two ancilla values, because the native
  readout is the block pinching of the ancilla values. Hidden assumption exposed: "an exclusive readout" on the kernel's
  carrier is not a readout law that could be added to the substratum; it is a statement that the observed algebra
  carries coherence between ancilla values (`exists_straddle_of_exclusiveOn`).
- **NEW, O8-N2.** The general form of O5-T1a: on every finite carrier, one passive readout of any nontrivial cell with
  every permutation reaches every point mass (design module, with the construction replicated exactly).
- **NEW, O8-N3 (disguise located).** On the knowledge-balance toy the exclusivity is the observation-side equivalent of
  the balanced mixer relative to the exchanges and the KB-D instrument; the owner's numbers alone are reproducible
  without it by memory erasure, so the witness's numbers do not detect the premise.
- **CONFIRMING, O8-C1.** O5-T1a, O5-KB1, O5-SRC2, O6 P1 (recomputed in X4, X5, X6).
