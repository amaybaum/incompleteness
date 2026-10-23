# Coordinator review: nonlinear-frontier handoff v1

> **DRAFT — research record.** The owner's read-only session produced this exploratory construction. It is recorded
> here with the coordinator's verification and independent checks. The rule is an engineered candidate: it adopts no
> premise, and OI has not selected it.

## Verification

- **Archive.** The archive's sha256 is `404ad74113c8454da8150144aec4cf476e4fda7986510a79919036df03be45d2`, as
  stated. The files in `handoff/` are its contents, unchanged. Their `SHA256SUMS` verifies.
- **Code review before running.** `frontier_checks.py` uses only the standard library and seeded pseudo-random
  generators, and writes only to stdout.
- **Replay.** Run from a separate directory with `python3 -I`, normally and with `-O`, the output is byte-identical
  to `frontier_checks.out`.

## The rule

The update is U′ = H(SU) ⊕ U_old, where U = (A, B, D), S is the six-neighbour XOR, and H(a, b, d) = (b, d, a ⊕ bd)
is a permutation of the eight triples. Componentwise:

- A′ = SB ⊕ A_old
- B′ = SD ⊕ B_old
- D′ = SA ⊕ (SB)(SD) ⊕ D_old

The rule is reversible for any H: the previous slice is U_old = U′ ⊕ H(SU). The fields feed back into one another
nonlinearly. The internal cyclic order of the fields is supplied; the rule's symmetry is spatial (cubic) only.

## Independent checks (`coordinator_frontier_checks.py`; separate code, numpy)

| Check | Result |
|---|---|
| G1 | H permutes the eight triples. The explicit inverse recovers the previous slice on random 7³ and 6×5×4 tori over 12 ticks |
| G2 | **Source freshness on dense full-torus backgrounds.** Every unreserved bit of both slices is random, and the frontier runs along −y, whereas the handoff uses +x. On an 11³ torus with K = 2, 3, 4 and four backgrounds each (12 cases), every one of the 8^K source words occurs exactly once. For every prefix of every length, the next triple is exactly uniform |
| G3 | **The joint apparatus on dense full-torus backgrounds** (K = 2, L = 17, q = (8,0,0)). Three backgrounds, each with all 8 inputs × 64 frontier assignments, were run for both AND3 and the complemented zero test. Every run gives the receiver record ((0,0,0), (c, ab, abc)). For each input the 64 source words are distinct and form the same set for every input |
| G4 | **Degree growth with more variables** (7³ torus, ticks 1–10, three random choices each). With 8 free initial bits the maximum output degree reaches 8 by tick 7. With 10 free bits it reaches 10 by tick 7 |
| G5 | The joint apparatus's readiness, recounted from its definition, is 3·25 − 3 + 3·7 + 6 = 99 bits |

G2 and G3 are stronger than the handoff's own checks. Those enumerate the frontier either over a cone-only background
or on a zero background, and run dense backgrounds only with the frontier fixed.

## Findings

1. **The permutive-frontier lemma holds (CONFIRMING).**
   - The lemma: for any bijection H, the map from the reserved frontier symbols to the bounded source word is
     triangular with bijective diagonal maps.
   - The proof does not use linearity. Along the unique extreme path, each frontier symbol enters through one
     neighbour term, as z ↦ H(z + c) + d.
   - G2 checks this on dense backgrounds, in a different direction, for K up to 4, including freshness conditional on
     every prefix.
   - The non-bijective countercontrol keeps the rule globally reversible but loses freshness. Freshness therefore
     comes from local permutivity, not from global reversibility.
2. **This resolves report17's open question (POSITIVE).** Nonlinear feedback among the fields does not by itself
   destroy bounded freshness. Report17's finding 3 now records that.
3. **The two-stage AND holds (CONFIRMING).**
   - Three inputs give (c, ab, abc) at the receiver at tick 2, with ab formed at (1,0,0) on tick 1.
   - The affine encoding 1 + x gives an exact three-input zero flag. That is beyond the old rule's degree-2 bound,
     under the new rule.
   - The joint law with the source holds on dense backgrounds (G3).
   - Output degree grows to the number of free variables within a few ticks (G4). This is finite evidence that the
     rule is not conjugate to a linear one by any bounded-degree map. It is not a proof of unbounded degree or of
     universal computation.
4. **Workspace accounting (proposed; assumption-watch).**
   - The gate evaluates 3 inputs only on a 99-bit readiness event, 96 of whose fixed bits form its clean workspace.
   - A readiness detector assembled from such gates therefore carries its own clean-workspace and reset requirement.
     That requirement belongs in the entropy budget of report16.
   - Detection is worth building only if its total clean resources cost less than preparing the readiness event
     directly. That comparison must be made for any scaled circuit; this report does not make it.
5. **Scope.** The following are supplied, not constructed:
   - the rule and its internal field order;
   - the readiness event (2^−99);
   - the preloaded inputs;
   - the tick as time.

   The receiver record also exposes c and ab. The freshness lemma covers records that depend only on the
   complement of the reserved coordinates. Not constructed: a scaled aggregation circuit, a readiness detector, a
   clock, angular emission, and station-indexed preparations.

## Relevance to the next target

The owner's next test is whether AND aggregation under this rule scales without unwanted wave interference, keeping
the source separated and accounting for every returned signal. Finding 4 adds a fifth item to that test:
- routing;
- interference;
- side records;
- source separation;
- the clean-workspace budget per detected bit.

The C-SPH-1 checkpoint stays closed.
