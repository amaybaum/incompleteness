# A42 research: is support 48 minimal for a non-Diţă straight line through SIG?

Read-only, disposable research thread (Track B, OI→QM). Branch `claude/a42-support-research`, base D41 =
`78ea3c39004e97aad027ee6153051c6d372bdd55`. Nothing here is a certificate or a governed round.

## Verdict

**No.** Support 48 is not minimal. There is a non-Diţă straight line through SIG whose orbit-minimal support is
**40**, and the act-38 witness itself has orbit-minimal support **44**, not 48. (48 is the support of act 38's
{0,1} representative; the minimum over the gauge orbit is lower.)

What is established, and at which layer:

| support s (orbit-minimal) | status | domain | layer |
|---|---|---|---|
| 1–15 | excluded | all integer E | proof (Lemma U) + exact table check |
| 16–19 | excluded | all integer E | proof (Lemmas CV, RS, M1) + exhaustive exact check over every row set |
| 20–39 | RESULT_20_39 | RESULT_DOMAIN_20_39 | exhaustive exact search in the domain |
| 40 | **found** | min representative in {−1,0,1} | exact straightness, generic structure search, exact min-support |
| 41–47 | RESULT_41_47 | | |
| 44 | the act-38 witness's class | min representative has an entry −2 | integer programme (HiGHS certificate) + explicit representative |
| any s < 48 | excluded | classes with a {0,1} representative of support s | proof (Lemma P) + exhaustive exact enumeration |

The last row is why act 38 saw nothing below 48: its census ran over {0,1} matrices, and a {0,1} straight line has
support 16·rank(SIG∘E) (Lemma P), so the {0,1} supports are 16, 32, 48, …; all 16- and 32-support {0,1} straight
lines are Diţă. The support-40 line and the act-38 witness's support-44 representative both need entries outside
{0,1} (the first −1 and +1; the second −2).

RESULTS_PLACEHOLDER

## Objects, domain, group action, support

- SIG = F4(z) ⊗ F4(w), z = (3+4i)/5, w = (5+12i)/13, index (a,b) ↦ 4a+b, entries unimodular (scaled by 4). Loaded
  verbatim from the landed probe head `verification/lean/dita_arc_exclusivity_probe.py` (`lib42.py`).
- **Straight line**: E ∈ Z^{16×16} with H(u) = SIG ∘ u^E complex Hadamard for every unit u. Equivalently (coefficient
  extraction in the Laurent identity H H* = 16 I), for every row pair (i, i′) and every integer d,
  Σ_{k : E_ik − E_i′k = d} SIG_ik conj(SIG_i′k) = 0 — every level set of every row difference vanishes. Tested with
  exact subset tables (Gaussian integers ×65) and, independently, with exact Gaussian rationals (`straight_direct`).
- **Group** G acting on exponent matrices: gauge E ↦ E + α1ᵀ + 1βᵀ (α, β ∈ Z¹⁶); the 1024-element stabilizer of SIG
  from act 36, acting as signed position permutations (σE)[p(t)] = s·E[t] (s = −1 exactly for the elements that
  conjugate; 512 elements transpose); and the global sign E ↦ −E. All preserve straightness (checked: every element
  fixes SIG up to dephasing, `lemmas42.py` L3).
- **Support**: s(E) = min over the G-orbit of the number of nonzero entries. **Lemma O**: s(E) = min over gauge
  alone, min_{α,β} #{(i,j) : E_ij + α_i + β_j ≠ 0}, because stabilizer elements and the sign are signed permutations
  of the 256 positions (support-preserving) that map the gauge subspace to itself. A representative attaining s(E) is
  a *min representative*; in it 0 is a most frequent value of every row and every column (else shifting that line
  lowers the support) — the **mode-0** condition used as a necessary filter.
- **Domains searched**: D1 = classes having a min representative with entries in {−1,0,1}; D01 = classes having a
  {0,1} representative (of the stated support; act 38's census domain); general integers where a lemma closes.

## The Diţă notion (and a census finding)

Three membership tests appear; the relations between them decide how each result reads:

- **N18** — act 38's test: E lies in one of the 18 relaxed census subspaces L_S (strict ⊂ relaxed, checked; the
  relaxed equations annihilate gauge, checked). Every L_S is a genuine Diţă structure of SIG, so N18-membership ⇒ Diţă.
- **Ncomplete** — the parallel census thread's complete test: 20 structures (the 18 and a fifth 4×4 structure in
  both forms) under every valid label matching (`complete42.py`, reusing `matchlib41.py` and `fifth41.json` verbatim
  from the census thread; the valid relaxed matchings are recomputed here exactly at SIG: 8, 64, 8, 8, 4, 4, 128,
  128, 128, 8 per structure).
- **Ngeneric** — act 37's `structures` search on the monomial entries of SIG ∘ u^E at a free u: the *candidate*
  count (column partitions whose blocks split the rows into proportionality classes of the right size) does not
  depend on the label matching and covers every index map; zero candidates in every shape and form means no Diţă
  structure holds identically under any notion.

Hence: an exclusion proved with N18 (every line in the set is N18-Diţă) holds under every notion; a witness certified
by Ngeneric is non-Diţă under every notion. All exclusions below are N18 exclusions; all witnesses are Ngeneric
witnesses (and also checked outside Ncomplete).

**Finding (independently of the census thread): the 18 subspaces are not closed under the stabilizer.** Transporting
the 18 relaxed subspaces by all 1024 elements gives 34 distinct subspaces (deduplicated by reduced echelon form mod two
primes, `closure.py`); 768 of the 1024 elements move some L_S off the list. The extra 16 are the census partitions
with a different label matching, each an exact relaxed Diţă structure of SIG (`matching.py`). Consequence for method:
under N18 the non-Diţă property is not orbit-invariant, so every N18 search here runs over all row sets without
symmetry reduction; under Ncomplete (invariant) orbit representatives suffice.

LEMMAS_PLACEHOLDER
