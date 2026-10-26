# Mapping part B5: I-313 to I-385 (Appendix A, Appendix B, references BHa/BHb), with I-123 and I-124

**Objects:** `papers/Introduction.md` at `4a260ca9`. The corpus is `main` at `eae01647`, read from the `tree939` extraction. `verification/programmes/black-hole-information/**` was read with `git show eae01647:`, and `papers/introduction_repro/` with `git show 4a260ca9:` (it exists only on the Introduction branch). Rows are in `part-B5.json`.

The OIBridge sources are byte-identical at `17b830bc`, `b64919cd` and `eae01647`: `git diff` is empty and every module was compared with `cmp`.

## Counts

There are 77 rows:
- I-313 to I-385;
- the two directional sub-claims I-336.a and I-336.b;
- I-123 and I-124. The lead assigned these to B5 although they fall outside the range. They may duplicate rows from the §2.5 mapper, so drop one copy when merging.

| Verdict | Count | IDs |
|---|--:|---|
| FAITHFUL | 74 | all others |
| IMPRECISE | 2 | I-124, I-383 |
| UNSUPPORTED | 1 | I-123 |
| OVERCLAIM / UNDERCLAIM / MISCITED | 0 | — |

## Appendix A: all 28 declarations verified

- **Location.** Each declaration is a `theorem` at the stated `module:line`. The "compositions :466–468" are the proof term of `finite_horizon_equivalence`; they are not separate declarations.
- **Axioms.** The retained result `papers/introduction_repro/results-121598983127.json` holds exactly one report for each declaration, and each report reads `[propext, Classical.choice, Quot.sound]`.
  - Each report's line is the line of that declaration's `#print axioms` in the source.
  - In all 14 modules, the number of reports equals the number of `#print axioms` lines.
  - The build succeeded, the gate passed, and the counts of `sorryAx`, `Lean.ofReduceBool` and `error:` are all 0.
- **Statements.** Every statement matches the Introduction's gloss, including its hypotheses and direction.

How far each kernel declaration covers the result in the Introduction that cites it:

| Introduction result | Kernel coverage | Paper-only parts |
|---|---|---|
| Theorem 1 | **Full.** The Lean classes match the definitions of S_K, D_K and Q_K: D_K allows a correlated initial law; Q_K uses a diagonal initial law, fixed-basis Born readout with collapse at every step, and readout through a function. | The independent-prior realization (Main:496), and U = e^{-iĤ}, which is deliberately left unformalized. |
| Theorem 2 (a)–(c) | **Partial, as stated.** The kernel proves the result for an arbitrary joint law on (history, present, hidden state) with X_{t+1} defined by φ. | The identification of that joint law with a realization's time-t law (Main:582). The CMI vanishing criterion has no kernel statement. |
| Capacity bound | **Partial,** in the same form as Theorem 2. I* is the maximum over a finite family of slices that share one hidden alphabet. | The same time-t identification. |
| Stochastic-inverse lemma | **Full.** | — |
| Theorem 3 | **Full.** The rooted form is what the Introduction states. The kernel proof does not use reversibility. | — |
| Readback forces indivisibility | **Routed form only.** The conclusion is ∃n, PIndivisibleWithin n. | The history-level (C4) step, Main:137. The ledger marks it P. I re-read the proof and it is valid. |
| §3.3 relating evolution | **Full for what is asserted.** GL2 is an existential witness, a single family with \|V\| = \|A\| = 2. GL3 is general. | — |
| §3.3 fixed-basis bridge | **Full,** with trivial ancilla. `bridge_traj` is the M = N = 1 case of a more general statement. | "Acts on the quotient by visible equality" is an inference that both kernel directions support. |
| Theorem 4 | **Full in both directions,** for every nonempty finite carrier. The structure fields and conditions (i)–(v) match the Introduction's description. | — |
| Independence; OI alone does not imply QM | **Full on the qubit.** | Nothing is claimed for other carriers. |

Owner note on I-329:
- **The discrepancy.** `PhysicalC4Discharge.lean` records that the store clause of `RoutedReadback` is the frozen "seed-posterior" spelling. The module says that spelling is not the same predicate as the discovery round's storage-time clause.
- **Why the conclusion still holds.** The proof uses only the overlap consequence, and both readings supply it.
- **What the Introduction says.** It says "a routed-readback form", which is accurate. Only the frozen spelling is kernel-checked.

## Appendix B: every number re-verified exactly

`S/b5_check.py` re-checks every number with rational arithmetic and sympy. It is a scratch script, not a repository file.

- **B.1:**
  - Γ_1 = [[2/3,1/3],[1/3,2/3]], Γ_2 = I and det Γ_1 = 1/3.
  - The divisor Γ_1^{-1}Γ_2 = [[2,−1],[−1,2]] is unique and has negative entries.
  - Γ_1² = [[5/9,4/9],[4/9,5/9]].
  - The conditionals are 1 and 1/3, and a/(2−a) for general a.
- **B.2:**
  - All three two-time matrices are ½J, and I(X_0;X_2|X_1) = 1 bit.
  - RHP14 Eq. (15) is XOR with the last bit flipped (x3 = NOT(x1⊕x2)). I opened arXiv:1405.0303v2 to check this.
  - Dou26 v3 App. A is the unflipped XOR process. I read the cached text.
- **B.3:**
  - The protocol values are 1/2, 1, 1/2 and 1/2. The reveal-only and replace-hole controls both give 1.
  - Anticorrelated cards give a permutation Γ_1.
  - The swap channel gives tr(ρ)I/2 in one step and the identity in two. With a fixed hidden slot, the one-step map is tr(ρ)|0⟩⟨0|.
  - The identity Σ_o σ_o X σ_o = 2tr(X)I holds.
  - The Pauli instrument sums to the one-step map, and the conditioned corrections give the identity.
  - Main §4.5's no-decomposition argument for the fixed slot checks out.

## Non-FAITHFUL rows, by severity

1. **I-123, UNSUPPORTED (low, expository): "a minimal model of Theorem 3 with six hidden states".**
   - **Where the label comes from.** It is inherited from the title of Main §2.4 ("A Minimal Model") and from ch01:135. No measure is stated and no proof exists anywhere in the corpus.
   - **No measure makes it true:**
     - The 2-hidden-state card game realizes Theorem 3.
     - A 3-hidden-state model reproduces every B.1 number exactly: h=1 flips x, and h=2↔3 swap.
     - At \|C_V\| = 2 and \|C_H\| = 3, all 648 Theorem-3 witnesses have an invertible Γ_s, so the "unique negative divisor" feature does not need six states either.
   - **Fix:**
     - At line 98, replace the phrase with "the six-hidden-state model of [Main §2.4]".
     - Retitle B.1 "A six-hidden-state model".
2. **I-124, IMPRECISE (low): "the smallest realization of Theorem 3".**
   - **It is true under natural measures:** configuration count, each alphabet's size, and return time. The proof takes two lines:
     - with one hidden state, every Γ_t is a permutation matrix, so no two rows overlap;
     - Γ_0 = I, so s ≥ 1 and n ≥ 2.
   - Exhaustive check: there is no witness below (2,2), and 16 of the 24 bijections at (2,2) are witnesses.
   - **The corpus has no such proof.**
   - **"The" is wrong:** other 2×2 realizations exist, for example φ(v,h) = (v⊕h, h) at Main:421.
   - **Fix:** "a two-card game, which realizes Theorem 3 with two visible and two hidden states, the fewest possible".
3. **I-383, IMPRECISE (low): "A card arrangement violates no Bell inequality".**
   - **When it holds:** only for local card moves with settings independent of the deal. This is Main:360's Bell-ceiling theorem, and the book's "local classical toy" qualifier.
   - **Why the bare statement fails:** Main §3.3, the very section cited, says at :356 that unrestricted finite reversible dynamics realizes PR-box behaviour.
   - **Fix:** "A card arrangement whose moves act only on each player's own cards, with settings chosen independently of the deal, violates no Bell inequality [Book §1.11; Main §3.3, Theorem (Bell ceiling for a screened local completion)]."

## References BHa and BHb (I-384, I-385): FAITHFUL

**BH-01:**
- The review of `587d4196` was BLOCK (wording only).
- The re-check of `95458016` was ACCEPT WITH NITS.
- The re-check of `df2ea6f5` was ACCEPT, with no remaining findings.

**BH-02/04:**
- The review of `1739f4e0` was ACCEPT WITH NITS.
- The re-checks gave `91e2230a` ACCEPT WITH NITS, `1f1aec6f` ACCEPT and `ce7937d2` ACCEPT.

**Both packages:**
- Both retain their reviews under `review/`, and each `README.md` says "separate-agent internal review … not external validation or owner adoption".
- Changes after the last review (`606c98d8`, `84aca6b0`) are wording and record retention. They went through a scoped landing audit that is recorded in the commit messages and in BH-02's PROVENANCE, but its text is not retained.
- BHb's title is quoted verbatim from its REPORT.
- **Optional:** add "not adopted" to both entries, to mirror the records.

## Attention items resolved

- **I-320:** Theorem 2's parts map one to one: (a) is `pushforward_identity`, (b) is `distinguishability_floor`, (c) is `capacity_floor`, and the combined statement is `unavoidable_hidden_predictive_memory`.
- **I-336:** the iff is literally `⟨physical_of_exactAll T, exactAll_of_physical_general T⟩` (GeneralCarrier:102). Each direction has its own witness, as §A.34 requires.
- **I-345:** the model is in Main §2.4 (:178–198), so the citation is correct.
- **I-383:** read as "any card arrangement". See item 3 above.
- **I-123 and I-124:** see items 1 and 2 above.

## Corpus findings outside the Introduction

These go for separate correction.

- **`book/ch01-observation.md:273` (FULL:617):** "The minimal such game is the coin-and-die model of §1.5 dealt onto a table". It gives no measure, and it identifies a game with two burn-card states with the six-state die model.
- **`book/appendix-b-derivations.md:92`:** Theorem B.2.5 says "(under C1–C4)", where Main:326 scopes the result to the permutation-dilation family. This is signal S3. The Introduction follows Main correctly.
- **Possible understatement in §2.2, for the §2.2 mapper:** the Introduction restricts the independent-prior realization to rational laws. Main:498's response-table extension gives an independent product prior for arbitrary real kernels; it is argued in the text and probed in `review4_probes.py` P-G.

## For the owner to decide

- Whether to keep a minimality claim for the card game at all. If it stays, the sentence needs the measure and its one-line reason.
- Whether Appendix A should note that the routed-readback predicate is the frozen spelling (I-329). The current wording, "a routed-readback form", is accurate as it stands.
