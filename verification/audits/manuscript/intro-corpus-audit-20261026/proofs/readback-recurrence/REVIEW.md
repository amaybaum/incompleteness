*Independent proof review (PLAN.md step 9), recorded by the coordinator verbatim from the reviewer's report. `S` in paths is the session scratch directory, not retained. The scripts and outputs beside this file are the reviewer's; the coordinator re-ran them under `python3 -I -B`, and the re-run outputs are the `.out` files.*

# Independent review: Main.md §2.3, Theorem (history readback + finite recurrence implies indivisibility) and Lemma (stochastic inverse)

Corpus at `eae01647`. Main.md L133–135 (Lemma) and L137–141 (Theorem, proof, scope). Introduction at `4a260ca9`, L12, L88–L98, L104, L120, L122.
Read-only review. All computation is exact (`fractions.Fraction`), run with `python3 -I -B`.

## VERDICT: ACCEPT WITH CHANGES

- **The mathematics is correct.** The Lemma is correct. The Theorem's proof is valid once its objects are pinned down. Under the corpus's own conventions, which are stated in the Introduction and in the Lean layer but not in Main, I found no counterexample, and the exhaustive exact search found none.
- **The changes concern four things.** They are definitions missing at the theorem's site, a sharper statement the proof already delivers, a kernel-attribution sentence, and an interpretive framing that the result does not support.
- **The step from history-level (C4) to a rooted map Γ_s that is not a permutation is proved on paper only.** The paper proof is correct. No kernel statement covers this step.

***

## 1. The statement as proved

**Data.**
- φ is a bijection of the finite set C_V × C_H.
- μ_H is a hidden prior on C_H. It is fixed and shared by every root, and it may vanish on some states.
- p_V is a visible prior. X_0 ~ p_V and H_0 ~ μ_H are drawn independently. This is Main §3.4's convention: "an initial hidden prior μ_H independent of the visible initial state", L496.

**Rooted maps.** For **every** root a ∈ C_V, whatever p_V(a) is:

  Γ_t(a, j) := μ_H{ h : π_V φ^t(a, h) = j }.

This is Lean's `rootedMap`. It is also the population map of Main §3.2's channel Φ_t(ρ) = Tr_H[U^t(ρ⊗μ_H)U^{-t}].

**P-divisible on {0,…,n}.** For every pair s < t ≤ n there is a row-stochastic Λ with Γ_t = Γ_s Λ. This is Intro L90 and Lean `PDivisible`.

**Theorem (as proved).**
- *Hypothesis.* Suppose that for some k ≥ 1 there are two **distinct** visible histories (x_0,…,x_{k−1}) ≠ (x'_0,…,x'_{k−1}), each of positive probability, with x_k = x'_k. A history-level (C4) gap at order k is a special case. The differing next-step laws are never used.
- *Conclusion 1.* There is an s with 1 ≤ s ≤ min(k, L−1) such that Γ_s is not a permutation matrix. Here L is the order of φ.
- *Conclusion 2.* For every n > s with Γ_n = I, there is no stochastic Λ with Γ_n = Γ_s Λ. In particular this holds for n = L. So the rooted family is not P-divisible on {0,…,n}.
- *Refinement.*
  - If the two histories have different roots (x_0 ≠ x'_0), then s = k works. Rows x_0 and x'_0 of Γ_k, both with positive visible probability, overlap in column x_k.
  - If the two histories have the same root, then s ≤ k−1 is their first divergence time. The overlap that pigeonhole guarantees may involve a row whose root has **zero** visible probability.

**Answer to the timing question.** A gap at order k forces a Γ_s that is not a permutation at some s ≤ k. It does not force one at a later s only. The indivisibility witness is the pair (s, L): its later endpoint is the recurrence, not k+1. The short-window control below shows that this later endpoint cannot in general be brought into the window.

**Converse on the representative.** This result is new relative to the text, and it is verified exhaustively at small sizes. Assume a full-support visible prior. Then the following are equivalent on a fixed finite reversible representative:

  (C4 gap at some order k ≤ L−1) ⇔ (some Γ_s, 0 < s < L, is not a permutation) ⇔ (the family is not P-divisible on {0,…,L}).

Proof of ⇐ for the first equivalence:
1. Suppose there is no gap at any order below L. Then the law on {0,…,L} is Markov, with time-inhomogeneous kernels Q_k. Extend each Q_k arbitrarily, as a stochastic row, on states unreachable at time k.
2. With full support, Γ_t = Q_0⋯Q_{t−1} for every row.
3. Then Γ_L = I = Γ_s (Q_s⋯Q_{L−1}). By the Lemma, Γ_s is a permutation.

Proof of the second equivalence: if every Γ_s is a permutation, then Γ_s^{-1}Γ_t is a permutation divisor.

So with (C4) taken at an unrestricted order, the theorem's hypothesis is equivalent to its conclusion on the representative. Restricting (C4) to an accessible window is what makes the hypothesis strictly stronger than needed (§6).

***

## 2. Definitions check

| Object | Where defined | Finding |
|---|---|---|
| Rooted maps Γ_k | **Not defined in Main.** Intro L90 defines Γ_t as "rooted, rows indexed by x_0" and, at L92, "with a fixed hidden prior". Lean `CausalReadback.rootedMap` gives the formula. Main L86 and L60 state that T depends on (φ, partition, μ_H). | **Gap G1.** Main's theorem uses Γ_k and "rooted" with no definition anywhere in Main.md (grep: "rooted" occurs only at L20, L137, L139, L334). Rows for roots of zero visible probability are not addressed. They matter (§4, example 3). |
| History-level (C4) | Main L80, quantified by the Lemma at L167: two histories p ≠ p' of X_{<k} with a common present X_k = c, each of positive probability, with differing next-step laws, "on accessible windows". | Adequate. The proof uses only "two distinct positive-probability histories share a present". The word "genuine" at L137 is undefined. Either drop it or define it as "(C4) of §1.3". |
| P-divisibility / P-indivisibility | Not defined in Main §2.3. The first theorem defines it only through TV monotonicity, which L121 itself says is necessary, not sufficient. Defined at Intro L90 and Lean `PDivisible` / `PIndivisibleWithin`. | **Gap G1 (continued).** The conclusion "indivisible somewhere in its full recurrence cycle" needs the factorisation definition: ∃ s < t ≤ L with no stochastic Λ such that Γ_t = Γ_s Λ. The proof does use this definition correctly ("a stochastic divisor producing I"). |
| Finite recurrence / identity return | The proof uses the order L of φ, so φ^L = id and Γ_L = I. Lean uses any n with Γ_n = I, and in `routed_forces_indivisible_somewhere` it uses n = (s+1)·\|Perm(V×H)\|. | Correct. Γ_n = I can occur before φ^n = id, so the Lean hypothesis is more general. |
| "Fixed finite reversible OI representative" | Not defined (grep: the only occurrence is L137). Main L522 says the per-horizon realisation's hidden space "may grow with the horizon". | Should be stated: one fixed (φ, μ_H), not a per-horizon family. The recurrence cycle, and every Γ_t for t > K, belong to the representative, not to the accessible law. |

***

## 3. The proof, line by line

**Lemma (stochastic inverse), L133–135.**
- *Step 1: rows of B are basis vectors.* (AB)_{ij} = 0 for i ≠ j is a sum of nonnegative terms. So for every k with A_{ik} > 0, row k of B is e_i. Correct.
- *Step 2: one positive entry per row of A.* Two positive entries in a row of A give two equal rows of B. That contradicts invertibility of B, which holds because square AB = I implies BA = I. Each row of A has at least one positive entry, so it has exactly one, equal to 1. Correct.
- *Step 3: distinct columns.* "Invertibility makes the occupied columns distinct." Correct, because A is invertible.
- *Left-inverse case.* "Symmetric" is acceptable. If BA = I, apply the argument to (B, A): B is a permutation, so A = B^{-1} is a permutation. Lean derives the left case through `mul_eq_one_comm`.
- *Squareness.* Squareness is necessary. The 1×2 matrix A = [½ ½] and the 2×1 matrix B = [1; 1] are stochastic with AB = 1. The Lemma states "square", so this is not a defect.
- **Verdict: correct.**

**Theorem proof, L139.**
1. "φ has finite order L, so Γ_L = I." Correct for every μ_H, because Γ_L(a, ·) = δ_a.
2. "If every earlier Γ_k were a permutation, the current visible configuration would be a bijective deterministic function of the initial one at every time." Correct, μ_H-almost surely, for every root.
   - The step "at every time" for t ≥ L uses periodicity: Γ_{t+L} = Γ_t. This is implicit. It matters only if the (C4) order k ≥ L. **Minor gap G2:** say it.
3. "Two positive-probability histories with the same current endpoint would identify the same initial visible state and could not have different next-step laws, contradicting C4." Correct. In fact the two histories would be *identical*, which contradicts p ≠ p' already. The next-step clause of (C4) is never used.
   - Positive probability of a history requires its root to be in the support of p_V. Given the root, the hidden law is μ_H. So the argument holds for any p_V.
4. "Hence some Γ_k is non-permutation." Correct. The proof only needs Γ_1,…,Γ_k to be permutations for the contradiction, so it yields s ≤ k. **G3:** the statement should record this. As written, "some earlier Γ_k" leaves the timing implicit.
5. "Divisibility from that time to the recurrence would require a stochastic divisor producing I from Γ_k, i.e. a stochastic left or right inverse, forbidden by the lemma." Correct. With the right-multiplication convention, Γ_L = Γ_s Λ = I makes Λ a stochastic right inverse.

**Role of overlap.**
- The paper's route never mentions overlap. It goes non-permutation ⇒ no stochastic inverse (Lemma).
- The kernel's route goes overlap at s plus Γ_n = I ⇒ a TV revival (C4r) ⇒ not P-divisible (contraction). It does not use the Lemma: the docstring of `RecurrenceHorizon` says "no stochastic-inverse rigidity lemma is introduced".
- The two routes meet in an elementary pigeonhole fact: a square stochastic matrix is not a permutation iff two distinct rows overlap in a column. If every column has at most one positive entry, there are at most n positive entries. If every row has at least one and some row has two or more, there are at least n+1.
  - The pigeonhole fact is verified exactly on every Γ_s in the search (0 failures).
  - It is **not** a kernel lemma.
- Overlap may be supplied by a row of visible probability zero (§4). Lean is unaffected, because `rootedMap` has every row. A reading that keeps only realised roots would break the overlap step.

**Identity return plus a non-permutation Γ_s gives P-indivisibility at the claimed times.** It does: the pair (s, n) for every n > s with Γ_n = I. Nothing is claimed, or true in general, for any horizon below the first identity return after s.

***

## 4. Counterexample attempts (exact arithmetic)

Scripts, all in `S/proofrev/recur/`:
- `recur_probe.py`, output `recur_probe.out`: exhaustive search.
- `named_examples.py`, output `named_examples.out`: worked examples and controls.
- `equiv_check.py`, output `equiv_check.out`: the converse in §1.

Decision rules were fixed in the script docstring before running.

**Exhaustive search.**
- *Coverage.* Every bijection at (n_V, n_H) = (2,2), (2,3), (3,2), (2,4).
- *Hidden priors.* Two or three per size: uniform, priors with zero entries, and non-uniform rational priors.
- *Visible priors.* Uniform, every point mass, and, for n_V = 3, a two-point support.
- *Times.* All t ≤ L. (C4) is checked at every order k ≤ L.
- *Divisibility check for the pair (s, L).* It is decided **independently of the Lemma**. Any Λ with Γ_s Λ = I must equal Γ_s^{-1}, computed by exact Gauss–Jordan elimination. The pair is indivisible iff Γ_s is singular or Γ_s^{-1} has a negative entry.
- *Countercontrol.* Every Γ_s that is a permutation must yield a stochastic inverse.

| (n_V,n_H) | cases | with (C4) | A: (C4)@k ⇒ non-perm at s≤k | B: non-perm ⇒ no stoch. inverse | B-control (perm ⇒ stoch. inverse) | pigeonhole | theorem fails | (C4) cases whose overlap at s≤k needs a zero-prior row |
|---|---|---|---|---|---|---|---|---|
| (2,2) | 216 | 108 | 0 fail | 210 checked, 0 fail | 177, 0 fail | 0 fail | **0** | 64 |
| (2,3) | 6 480 | 5 476 | 0 fail | 19 500, 0 fail | 3 459, 0 fail | 0 fail | **0** | 3 540 |
| (3,2) | 10 800 | 7 108 | 0 fail | 30 620, 0 fail | 7 645, 0 fail | 0 fail | **0** | 3 584 |
| (2,4) | 241 920 | 231 072 | 0 fail | 1 439 310, 0 fail | 114 108, 0 fail | 0 fail | **0** | 152 808 |

- *Timing.* The first non-permutation time is strictly below k in 64/108, 3 580/5 476, 4 116/7 108 and 163 512/231 072 of the (C4) cases. It equals k in the rest. It never exceeds k.
- *Converse (`equiv_check.py`, full-support prior, (2,2), (2,3), (3,2)).* No cell (non-permutation, no (C4) below L) and no cell (all permutations, (C4)) occurs. The least (C4) order ranges up to L−1. For example, the tape shift below has its first gap at order L−1, which is the recurrence itself read back.

**Named examples** (`named_examples.out`).
1. *Main §2.4 six-hidden model (control).*
   - Γ_1 = [[2/3,1/3],[1/3,2/3]] and Γ_2 = I.
   - (C4) holds at order 1, and Γ_1^{-1} = [[2,−1],[−1,2]]. This reproduces the printed Λ(2,1).
   - The printed values P(x_2=0 | x_1=1, x_0=0) = 1 and P(x_2=0 | x_1=1) = 1/3 are reproduced.
2. *Short-window control: φ(x,u) = (u, x⊕u), uniform u, order 3.*
   - Γ = I, J/2, J/2, I.
   - (C4) holds at order 1, and its next-step time lies inside {0,1,2}.
   - The family is **P-divisible on {0,1,2}**. Exhibited stochastic witnesses, checked exactly: Λ_{01} = Λ_{02} = J/2 and Λ_{12} = I.
   - It is P-indivisible only on {0,…,3}.
   - This is a concrete instance of the Scope paragraph's claim: (C4) inside a window does not force indivisibility in that window.
3. *Zero-probability root (same φ, p_V = δ_0).*
   - (C4) holds at order 3, with histories (0,0,0) and (0,1,1), both at x_3 = 0.
   - The only overlap at s = 1 is between row 0 and row 1, and row 1 has visible probability 0.
   - If rooted maps keep only rows of realised roots, the family on {0,…,L} is P-divisible: take Λ = 1·row_t, checked exactly. **So under that reading the theorem is false.** This has 152 808 instances at (2,4) alone.
   - Under the corpus convention (all rows, fixed shared μ_H), the theorem holds, and the witness is a pair of preparations one of which the process never makes.
4. *Decoupled negative control: φ(x,h) = (1−x, h+x mod 2).* Every Γ_t is a permutation and (C4) holds at no order.
5. *Hidden influence without accessible readback: tape shift (x,(a,b)) ↦ (a,(b,x)), uniform tape.*
   - Γ_1 = Γ_2 = J/2 and L = 3.
   - No (C4) gap at order 1, so no gap inside the window {0,1,2}.
   - The first gap is at order 2 = L−1, and it predicts the recurrence time 3.
   - It is still P-indivisible on {0,…,3}.

**No counterexample exists under the corpus conventions.** In every case where (C4) holds and recurrence holds, P-indivisibility on {0,…,L} appears. Zero-probability roots break the argument **only** under a definition that drops their rows. This is why G1 matters.

***

## 5. Kernel coverage versus paper

| Step | Kernel statement (hypotheses quoted) | Status |
|---|---|---|
| Lemma | `EquivalenceChain.isPermMatrix_of_stochastic_inverse {A B : Matrix n n ℝ} (hA : A ∈ rowStochastic ℝ n) (hB : B ∈ rowStochastic ℝ n) (h : A * B = 1 ∨ B * A = 1) : ∃ σ : Equiv.Perm n, A = σ.permMatrix ℝ` ([Fintype n] [DecidableEq n]) | Exact statement, kernel-proved. **Used nowhere else in the kernel** (grep). It is never composed with `rootedMap` or `PDivisible`. |
| Γ_0 = I; finite visible period | `RootedClassification.rootedMap_zero`; `rootedMap_periodic : PeriodicFamily (fun t => rootedMap R t)`, with period \|Perm(V×H)\|, explicitly "not asserted to be the minimal visible period" | Kernel. |
| Rooted maps stochastic | `CausalReadback.rootedMap_isRowStochastic (R : RootedRealization V H) (t : ℕ)` | Kernel. `RootedRealization` has `step : V × H ≃ V × H`, `prior : H → ℝ`, `prior_nonneg`, `prior_sum`. There is no visible prior, so every row is present. |
| Overlap plus identity return ⇒ not P-divisible (Intro Theorem 3) | `RecurrenceHorizon.pIndivisible_of_rooted_identity_return_of_overlap (R : RootedRealization V H) {n s : ℕ} (hsn : s < n) (hI : rootedMap R n = 1) {a b : V} (hab : a ≠ b) {x : V} (hax : 0 < rootedMap R s a x) (hbx : 0 < rootedMap R s b x) : PIndivisibleWithin n (rootedMap R)`. Matrix-level version `pIndivisible_of_identity_return_of_overlap` with `(hstoch : IsRowStochastic (Γ s))`. Route: `c4r_of_identity_return_of_overlap` then `c4r_implies_pIndivisible`, by TV contraction (`tv_mul_le`). | Kernel. Matches Intro Theorem 3 exactly. It does not use reversibility, the prior, or the Lemma. |
| Routed readback ⇒ indivisible somewhere | `PhysicalC4Discharge.routed_forces_indivisible_somewhere {K : ℕ} {R : RootedRealization V H} (h : RoutedReadback K R) : ∃ n, PIndivisibleWithin n (rootedMap R)`. `RoutedReadback K R` requires a ≠ b, 0 < w ≤ s < t ≤ K, a write clause, a store clause (overlap at s plus differing `rootedPosterior`), a causal read leg and a rooted reappearance. Only the overlap is used (`routedReadback_overlap`). The witness is n = (s+1)·M. | Kernel. The hypothesis is the *realisation clause*, which the module states implies history-level (C4). It is a stronger hypothesis than the theorem's. |
| **History-level (C4) ⇒ some Γ_s (s ≤ k) is not a permutation, or two rows of some Γ_s overlap** | **None.** The kernel's history-level (C4) objects are `HiddenMemory.Realization` (a joint law over histories, a different structure, which `CausalReadback` keeps apart deliberately) and `IndependenceCensus.core_history_readback` (one carrier). No theorem links either to `rootedMap`. | **Paper only.** Elementary and correct (§3). |
| Non-permutation ⇔ overlapping rows (pigeonhole), which links the paper route to the kernel route | None. | Paper only, and implicit. Main's first theorem, Step 2 (L125), states one direction. |
| Non-permutation Γ_s plus Γ_L = I ⇒ ¬PDivisible, through the Lemma (the paper's last sentence) | Not composed. The Lemma exists, but no theorem combines it with `PDivisible`. | The composition is one line on paper. The kernel reaches the same conclusion by the other route. |

**Formalisation target.**
- *Definitions.* Define the path law on a `RootedRealization` with a visible prior p_V.
- *Theorem.* Prove that if `∀ s ≤ k, ∃ σ, rootedMap R s = σ.permMatrix ℝ`, then every two positive-probability length-k histories with equal x_k are equal.
- *Consequence.* The contrapositive with pigeonhole produces the hypotheses of `pIndivisible_of_rooted_identity_return_of_overlap`. Together with `rootedMap_periodic`, this would make the history-level theorem fully kernel-checked.

**The Intro's kernel claims.**
- L96 says "machine-checked, by the route of Theorem 3, from a routed-readback form of (C4) … from history-level (C4) it is proved on paper". **Accurate.**
- L12 says "(each with one step not machine-checked)". **Accurate** for this theorem.
- L96 opens "With this lemma, … history readback forces indivisibility". This sentence is accurate for the paper proof. The machine-checked route does not use the lemma (G4, wording only).

***

## 6. Proof correctness versus physical interpretation

**Correct as mathematics.**
- (C4) on a fixed finite reversible representative ⇒ not P-divisible on {0,…,L}, witnessed at (s, L) with s ≤ k.
- The Lemma.
- The Scope paragraph's negative claim (no short-window forcing), confirmed by example 2.

**Not supported by the proof, or stronger than it.**
1. **"History readback turns into indivisibility."** The proof uses only the fact that two distinct realised histories share a present: visible non-determinism.
   - On the representative with full support, the hypothesis at unrestricted order is *equivalent* to the conclusion (§1).
   - The content that (C4) restricted to an accessible window adds is not used. Example 5 has hidden influence and no accessible readback, and it reaches the same indivisibility.
   - An i.i.d. fair coin has a finite reversible realisation with Γ_1 = J/2. That realisation is P-indivisible at recurrence by Main's own first theorem in §2.3. The coin is Markov.
   - So the recurrence-cycle indivisibility **does not discriminate memory**. Intro L12 places it under "The discriminating content concerns memory". **G5:** reword, for example: "on a fixed finite reversible system, any visible non-determinism — in particular any (C4) gap — yields stochastic indivisibility somewhere in the recurrence cycle".
2. **"Information backflow."** The witness is a TV revival between two *rooted preparations*, δ_a⊗μ_H and δ_b⊗μ_H, at the recurrence time.
   - It is a property of the dynamical-map family, including counterfactual preparations. In example 3 it uses a preparation the process never makes.
   - It is not a flow of information in the realised process, and it lies at L. L is Poincaré-scale and outside every accessible window.
   - The accessible-window information measure is the conditional mutual information of the readback lemma (L167). It is a separate object. Main L334 keeps the three notions apart, correctly, and the theorem's surrounding prose should keep to that.
3. **Representative dependence.** Γ_t for t > K and L itself are properties of the chosen (φ, μ_H), not of the accessible law. Main L522 lets the hidden space grow with the horizon.
   - "The rooted visible process is indivisible somewhere in its recurrence cycle" is therefore a statement about every fixed finite reversible representative. It is a universal statement over representatives, and that is fine.
   - It is not a statement about observable statistics on the window, which can be P-divisible (example 2).
4. **Main L174.** It says "the former establishes P-indivisibility from a non-permutation one-step witness and finiteness alone". This is consistent with point 1, and it is the more accurate framing of what recurrence buys.

***

## 7. Named gaps and fixes

- **G1 (definitions, Main L137–139).**
  - *Gap.* Γ_k, "rooted", P-divisibility, "genuine" and "OI representative" are undefined at the site.
  - *Fix.* Add one sentence: "Γ_t(a,j) := μ_H{h : π_V φ^t(a,h) = j} for every a ∈ C_V, with μ_H the fixed hidden prior shared by all roots and independent of the visible prior; P-divisible on {0,…,n} means every Γ_t, t ≤ n, factors as Γ_s Λ with Λ stochastic." Replace "genuine C4" with "a (C4) gap (§1.3)".
  - *Why it matters.* Without the all-rows convention the theorem is false (example 3).
- **G2 (proof, minor).**
  - *Gap.* The periodicity step Γ_{t+L} = Γ_t is not stated, and the proof needs it when the (C4) order is at least L.
  - *Fix.* State it.
- **G3 (statement).**
  - *Gap.* The statement does not say when the witness occurs.
  - *Fix.* State the sharpened form: some s ≤ min(k, L−1) has Γ_s not a permutation, and the pair (s, n) is indivisible for every identity return n > s. Add the note that the overlap may involve a root of visible probability zero.
- **G4 (Intro L96, attribution).**
  - *Gap.* The sentence reads as if the kernel's route used the Lemma.
  - *Fix.* Say that the kernel route is overlap plus TV contraction and does not use the Lemma. The Lemma is checked separately and is not composed with `PDivisible`.
- **G5 (interpretation, Intro L12 and L96; Main L20; book glossary L119 and FULL L6719).**
  - *Gap.* The text presents the result as memory-discriminating and as readback-driven.
  - *Fix.* Present it as "visible non-determinism ⇒ recurrence-cycle indivisibility", with (C4) one sufficient source. Keep the representation-level and process-level notions apart. Under §A.25 this wording recurs in Main L20, in Substratum L136 ("genuine C4 readback … forces global indivisibility") and in the book mirrors. Those are accurate as implications but carry the same framing.

## 8. Bearing on the broader framework

- **Assumption-watch marker.** Every recurrence-scale P-indivisibility result in the corpus is about the full-row dynamical-map family under a root-independent prior. A version keeping only realised roots, or using a root-dependent (correlated) initial joint law with undefined rows for unrealised roots, loses the overlap step.
  - Applies to: Main's first §2.3 theorem, the Lemma (non-permutation witness) at L415, the CP-indivisibility theorem at L326–328, and Intro Theorem 3.
- **Structural fact (exact, small sizes; proof in §1).** On a fixed finite reversible representative with full-support prior:
  - (C4) at some order < L ⇔ some Γ_s is not a permutation ⇔ not P-divisible on the cycle.
  - So on the cycle, (C4), (C1)-type rooted influence and P-indivisibility collapse to one condition.
  - Their separation, which the corpus stresses (Main L172, L334), lives only in the accessible-window restriction.
  - This supports Main L334's "three notions, kept apart", at the window level only. It also shows that "C1 follows from C4" (L604) and "C4 ⇒ indivisible at recurrence" become equivalences at recurrence scale.
- **Correctness axis.** None of this is a confrontation with data. It is consistency only (§A.23).

***

## 9. Comparison with the audit matrix

This section was written after the verdict above.

Source: `…/scratchpad/audit/wt/verification/audits/manuscript/intro-corpus-audit-20261026/`, at worktree head `a44003a02`. Files read: `inventory/claims.json`, `matrix/part-B1.json`, `part-B2.json`, `part-B5.json`, `EVIDENCE.md`.

**Line numbers.** The task names "Intro L120 and L122". In the Introduction those lines are §3.2's independence paragraph and the §3.3 heading; neither bears on this theorem. The audit rows **I-120 and I-122** are both anchored at **Intro L96**. I compared against L96. **I-330** is anchored at Intro L212 (Appendix A): "`routed_forces_indivisible_somewhere` … for routed readback; on paper for (C4)".

| Row | Audit verdict / status | This review | Agreement |
|---|---|---|---|
| I-009 (L12 abstract) | FAITHFUL, proved-paper. "Paper proof checked and sound"; history-level step on paper. | Agree on soundness and on the kernel/paper split. **Additional finding (G5):** the abstract places this result under "the discriminating content concerns memory". On the representative the recurrence-cycle indivisibility follows from any visible non-determinism, and with (C4) at unrestricted order it is equivalent to (C4) (§1). Markov laws realised reversibly are also indivisible at recurrence. The implication is faithful; the framing as memory-discriminating is not supported. | Partial. The audit missed the framing point. |
| I-010 (L12, "each with one step not machine-checked") | IMPRECISE; fix: do not count steps. | For this theorem "one step" is accurate if the step is read as "history-level (C4) ⇒ two rows of some Γ_s, s ≤ k, overlap". That step bundles the history argument with the pigeonhole bridge (non-permutation ⇔ overlap). Neither part is a kernel lemma. I agree with IMPRECISE, for the audit's reason, which concerns Theorem 2's Corollary. | Agree. |
| I-120 (L96, "With this lemma, … history readback forces indivisibility …") | FAITHFUL, proved-paper. Chain: Main:137, `isPermMatrix_of_stochastic_inverse`, `rootedMap_periodic`. | Agree that the statement is correct. **Additional (G4):** the kernel conclusion comes from `pIndivisible_of_rooted_identity_return_of_overlap` (overlap plus TV contraction), which does not use the Lemma. The Lemma is never composed with `PDivisible` in the kernel. The row's chain omits the theorem the kernel conclusion actually rests on. Also G1: Γ_k is undefined in Main, and the all-rows convention is needed. | Agree on the verdict; chain incomplete. |
| I-122 (L96, "from history-level (C4) it is proved on paper") | FAITHFUL; "No kernel declaration derives indivisibility from history-level (C4)". | Agree, and confirmed by grep. No theorem links `HiddenMemory.Realization` or `core_history_readback` to `rootedMap`. | Agree. |
| I-330 (L212, Appendix A) | FAITHFUL. Notes: "the argument is valid for rooted rows conditioned on x_0", and "the rest of the chain is kernel". Ledger link labelled exhaustive-computation, with EVIDENCE recording "no computation item for this link". | **Disagree on two notes.** (i) "Rooted rows conditioned on x_0" is the reading under which the argument **can fail**. If rows exist only for realised roots, P(X_t \| X_0 = a) with p_V(a) > 0, the theorem is false: example 3, and 152 808 instances at (2,4). The argument is valid for rows δ_a⊗μ_H for **every** a, with a root-independent prior, which is Lean's `rootedMap`. (ii) "The rest of the chain is kernel" is too strong. The paper chain's last step, Lemma ⇒ ¬PDivisible at (s, L), is not composed in the kernel. The kernel reaches ¬PDivisible by a different route whose overlap hypothesis, from history-level (C4), also needs the paper-only pigeonhole bridge. The missing computation item is supplied here: `recur_probe.py`, exhaustive and exact, 0 failures. | **Disagree on the notes**, agree on the verdict. |

**Findings the audit rows do not record.**
- Timing: s ≤ min(k, L−1).
- The overlap witness can require a root of visible probability zero.
- The converse at the cycle level: (C4) at some order < L ⇔ some Γ_s is not a permutation ⇔ not P-divisible on {0,…,L}, with full-support prior.
- The short-window control is exhibited explicitly: φ(x,u) = (u, x⊕u) is P-divisible on {0,1,2} with (C4) at order 1 inside that window.
