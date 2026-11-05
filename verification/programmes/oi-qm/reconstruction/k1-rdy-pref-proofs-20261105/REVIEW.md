# Independent review of `PROOFS.md` and of the K1-RDY OD-1/OD-2 evidence landing

**Reviewed head:** `6ff20b91b869ea09d432d2ae54ca8fb46cd4aa0f` on branch `evidence/k1-rdy-pref-landing-20261105`. Its history is:
- `b606ee4116e97e39d90e65a4110dc70f78b7b99d` (`main`);
- → `022ae8da3b1d6dfc4e632034b07c2e55996abb47`;
- → `17684d7798f274539f34a4e0036f726c713c1932`;
- → `6ff20b91…`.

Each of these commits has a single parent.

This review is **model-authored**: a read-only review by an agent other than the writer, not a human review. It used:
- hand derivation only, with no enumeration of states and no model computation;
- reads of the repository and of GitHub comments through the API;
- the repository's own static checks.

It records two steps:
1. an exact-head review of `17684d77`, verdict ACCEPT WITH CHANGES with three changes;
2. a delta check of `17684d77..6ff20b91`, which applies those three changes.

The mathematical review of `PROOFS.md` was done on its evidence branch before this landing. The landed file carries the same content: the blob of `PROOFS.md` at `17684d77` is `3801aba6c972668fec6ed73a9a01327691fc9018`, identical to the version reviewed there (`evidence/k1-rdy-pref-proofs-20261105` at `7c768f05`, provenance only). At `6ff20b91` the blob is `b50e23e47e107934fb5637158cd9148433d62bc9`, which differs from `3801aba6…` only in the two status lines (§3 below).

"The text" is the K1-RDY preregistration with recorded sha256 `a93f3f33f0c5a6e8b2467312d184fa2d2e915296490948938c4dd7832c64bb63` (313 lines). It is held as `PREREG-RECOVERED.md` on PR #1114 at `e18b36e3` (a provenance locator, not on `main`). Its digest was reproduced, and every statement `PROOFS.md` quotes from it was checked against it byte for byte.

## 1. `PROOFS.md`: the derivations, re-derived by hand

All arithmetic is over `ℤ/2` at the instance `Λ = ℤ/5`, `φ(x, y) = (y, Ay − x)`, `(Ay)_i = y_{i−1} + y_{i+1}`.

**§1, the region `E`.**
- `V_{t_0} = y_1`, and `V_{t_0+1} = y_1(t_0+1) = y_0 + y_2 + x_1` in the state at `t_0`.
- The cells with a nonzero coefficient at offsets 0 and 1 are `y_1, y_0, y_2, x_1`.
- Removing `Σ = {x_0, y_0}` leaves `E = {x_1, y_1, y_2}`, and `W_eq = {x_1, y_1}`.

**§2, cycle decomposition (Proposition CYC).**
- **Ring form.** Identify `𝐑^Λ` with `R = 𝔽_2[X]/(X^5 − 1)`. Then `A` is multiplication by `X + X^4`, and `φ` is `R`-linear on `R^2`.
- **Splitting.** `X^5 − 1 = (X + 1)Φ` with `Φ = X^4 + X^3 + X^2 + X + 1`.
  - `Φ` is irreducible: it has no root in `𝔽_2`, and the only irreducible quadratic squares to `X^4 + X^2 + 1 ≠ Φ`.
  - By the Chinese remainder theorem, `R ≅ 𝔽_2 × K` with `K = GF(16)`. The class `ζ` of `X` has order 5.
  - `φ` acts factorwise as `(u, v) ↦ (v, a′v + u)`, with `a′ = 0` on `𝔽_2` and `a′ = ζ + ζ^{−1}` on `K`.
- **The `𝔽_2` factor** is the swap `(u, v) ↦ (v, u)`. Two of its four states have period 1 and two have period 2.
- **The `K` factor.** `(1, ζ)` and `(1, ζ^{−1})` are eigenvectors, with the distinct eigenvalues `ζ` and `ζ^{−1}`, and they form a basis. So every nonzero vector has period exactly 5, and zero has period 1.
- **Combining.** Periods combine by least common multiple:
  - period 1: 2 states;
  - period 2: 2 states, one cycle;
  - period 5: 510 states, 102 cycles;
  - period 10: 510 states, 51 cycles.
  That is 156 cycles in all, the sizes sum to 1024, and `φ^{10} = id`.
- **The short cycles.** In `R`, `gΦ = g(1)Φ`, so the states whose `K`-component is 0 have `x, y ∈ {0, 𝟙}`. With `A𝟙 = 0`:
  - `0` and `(𝟙, 𝟙)` are the fixed points;
  - `{(0, 𝟙), (𝟙, 0)}` is the 2-cycle.

**§3, P3's image.**
- From `φ^{−1}(x, y) = (Ax − y, x)`, the window values `y_1(t_0 − k)` for `k = 0, 1, 2, 3` are `y_1`, `x_1`, `x_0 + x_2 + y_1` and `x_1 + x_3 + x_4 + y_0 + y_2`.
- `W(t) = (y_1(t−1), y_1(t))`. So three equal `W`-configurations on `[t_0 − 2, t_0]` is the same as four equal values. That gives the equations `x_1 + y_1 = 0`, `x_0 + x_2 = 0` and `x_3 + x_4 + y_0 + y_2 = 0`.
- The equations are independent: each contains a variable absent from the other two (`y_1`, `x_0`, `x_3`).
- So `O` is a subgroup of index 8 with 128 states, `π_0(O) = 1/8` and `D(μ_O) = 3 log 2`.

**§4, Proposition IND (replaces TA (c4)).**
- `π_0` is invariant under every bijection.
- Counting the states fixed on disjoint cell sets shows that `X_t` and `Y_t` are independent and uniform.
- `π_0(E_t = 0 | W_t = w)` is `q^{−|E∖W|}` when `w` vanishes on `W ∩ E`, and 0 otherwise.
- This covers the three uses:
  - CC-ABS (`W` disjoint from `E`): `r(w) = 1/8`;
  - P0's B-eq row (`W_eq ⊆ E`): `r(0) = 1/2`, and `r(w) = 0` otherwise;
  - P0's B-pl row: `1/8`.

**§5, Proposition EN.**
- (a) For symmetric `A`, expanding `ℰ(y, Ay − x)` and using `⟨Ay, Ay⟩ = ⟨y, A^2 y⟩` and `⟨y, Ax⟩ = ⟨Ay, x⟩` returns `ℰ(x, y)`. This holds over any `ℤ/q`, and it is the form stated at SM:296, whose lines 294–296 are unchanged on `main`.
- (b) Each shell is a union of cycles, so each `μ_e` belongs to `𝓘`.
- (c) Translating by `(𝟙, 0)` changes `ℰ` by `5 − ⟨A𝟙, y⟩ = 1`. So the two shells have 512 states each, and `D(μ_e) = log 2`.

**§6, the class rule (CR-1 to CR-6).**
- **CR-1:** each member of `𝓘` is `μ_λ` for exactly one support `C` and one weighting `λ` whose positive entries are exactly the cycles of `C`. This is proved in both directions, from Lemma P1.
- **CR-2:** `w` is sharp for `μ` iff `∅ ≠ C ∩ B_w ⊆ Z`. Proved in both directions.
- **CR-3:** the positive clause, of form ∀C∃w∀λ, is sufficient for "every member of `𝓘` has a sharp `w` with `NB`", of form ∀C∀λ∃w.
- **CR-4:** the ABSENT clause is exact, proved in both directions.
- **CR-5:** the converse of CR-3 is not established. The two forms coincide when `|Sh(C)| ≤ 1`, and otherwise differ by the order of the quantifiers. No counterexample is claimed. This is a gap in the claimed equivalence, recorded as such.
- **CR-6:** at the instance, `δ_0` is a member of `𝓘` (`{0}` is a cycle).
  - In B-pl, B-eq and B-ct, only `w = 0` has positive mass under `δ_0`. It is sharp, and `δ_0(· | B_0) = δ_0`.
  - `NB(δ_0)` fails, trivially (only one value of `σ` has positive mass) and by the blindness lemma.
  - So `δ_0`'s row is never positive, the union clause is never reached, and line 158's first sentence decides the class token in every branch, as line 236 states.
- The reading of "every weighting supported on `C`" is marked as a reading and is sound.

**§7, Proposition LEDGER.**
- (a) `D_KL(μ ‖ π_0) = log|S| − H(μ)`.
- (b), (c1), as in `LEMMAS.md` §2.3: `supp μ ⊆ Z`, `|Z| = |S|q^{−|E|}`, and `H(μ) ≤ log|supp μ|`. Hence `D(μ) ≥ |E| log q`.
- (c), (c2):
  - The chain rule over the partition `{B_v}` at `t_0` gives `D(μ) ≥ p · D_KL(μ(· | B_w) ‖ π_0(· | B_w))`. Every term is nonnegative because `π_0` has full support.
  - Sharpness puts `μ(· | B_w)` on `B_w ∩ Z`, so `D_KL ≥ log(|B_w| / |B_w ∩ Z|)`.
  - IND at the same tick gives `|E∖W| log q`.
  - The bound holds for any `μ`, and at equal time only.
- **Consequence.** An equal-time row whose sharp readiness actually holds meets its G3 bound. So G4's VOID[row] is reached only by a row that asserts readiness which does not hold, as in CC-LEDGER. There the `ℰ = 0` shell has `μ(E = 0) = 9/64`, and `3 log 2 > log 2`.

**Scope.** `PROOFS.md` decides no gate or token and changes no statement of the text. CR-5 remains an open point in the class rule, and whether to restate the rule is an owner decision.

## 2. `k1-rdy-proofs-20261105/REVIEW.md` (the record of the #1119 review)

- The two quoted blocks equal the API bodies of PR #1119 comments 6651717259 (2026-11-05T06:49:41Z) and 6653737476 (2026-11-05T08:49:14Z) byte for byte. Neither comment was edited after posting.
- **Comment 6651717259** is the coordinating session's condensed posting of the reviewer's delivered report on `1901063504f649bd453d7b5f87add395d6974ec7`. Its verdicts and findings match that report: the per-lemma outcomes, items C1–C4, the locators and the hygiene results. The file now says so, citing PR #1119 comment 6653843874 (2026-11-05T08:55:04Z).
- **Comment 6653737476.**
  - Between its BEGIN and END markers it is the reviewer's delta check of `d8bfd07bf591eeeeb107ef9842547dc53e195bef`, word for word. That check was delivered before `6525ad34b5fc4bd6f25c1c07de4482e35d69ec3c`, which applies exactly its two count fixes.
  - The dated statement after the END marker condenses the reviewer's statement made at posting time; its substance matches. The file states both points.
- **Commit ids.** All three full commit ids in the file exist and are reachable from `main` through `4f016afd`. `e18b36e3` appears only abbreviated, inside the quoted text, as a provenance locator.

## 3. Status lines and READMEs

- **`k1-rdy-proofs-20261105/LEMMAS.md`.** Only its five status lines change (the header and §1–§4). They now read "written proof, independently reviewed (`REVIEW.md`)", with "model-authored" in the header. That is accurate: the four proofs were reviewed, the reviewer's changes and the delta check's two count fixes are applied, and the review record is in the same directory.
- **`k1-rdy-proofs-20261105/README.md`.** The status line is corrected in place. The limit that waited on a review recorded on `main` is replaced by "The independent review is model-authored and read-only (`REVIEW.md`)". This is accurate and minimal.
- **`k1-rdy-pref-proofs-20261105/PROOFS.md`.** Only its two status lines change (the header and §7), in the same form. With this file landed beside it, they are accurate.
- **`k1-rdy-pref-proofs-20261105/README.md`.** The status line is changed and the same limit is replaced. Accurate and minimal.
- **Register.** Every edit is a correction in place (`AGENTS.md` §A.27, §A.30). The provenance notes in the review records are status content, not manuscript narration.
- **`AGENTS.md` §A.42.**
  - Item 2: the #1119 comments are quoted on `main`, so they are no longer the sole support.
  - Item 7: author and time are given for each quoted record.
  - Item 8: the locators inside quotations (#1114 c.6653656756, `e18b36e3`) are provenance, and the cited commits are support on `main`.

## 4. Checks at `6ff20b91b869ea09d432d2ae54ca8fb46cd4aa0f`

These were run with `python3 -I` in a detached worktree at the exact commit, and also at `17684d77`. All exit 0:

| Check | Result |
|---|---|
| `tools/legacy_records_check.py <head>` | 303 records in 75 closed namespaces, all intact |
| `tools/citation_roles_check.py <head>` | self-test OK; all hold |
| `tools/duplicate_check.py` | OK |
| `tools/artifact_placement_check.py` | OK |
| `tools/staleness_check.py` | OK, 13 matched |
| `tools/v3_verifier.py --self-test` | OK |
| `tools/v3_verifier.py --corpus` | 140 vectors, exact and as expected |
| `tools/v3_verifier.py --receipts <head>` | 52 receipts, all hold |
| `tools/build_migration_manifest.py --check` | OK |

## 5. The review of `17684d77` and the delta check

- **Exact-head review of `17684d77`: ACCEPT WITH CHANGES.** It required three changes:
  1. state that comment 6651717259 is a condensed posting;
  2. correct the authorship of the dated statement in comment 6653737476;
  3. update the status lines of `PROOFS.md` and its README.
- **Delta check of `17684d77..6ff20b91`:** each hunk is one of those three changes, and nothing else changed.

**Verdict: ACCEPT** (`6ff20b91b869ea09d432d2ae54ca8fb46cd4aa0f`).
