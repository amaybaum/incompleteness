# Exact-head review of `QB3-EVIDENCE.md` (BORN-SEL (b), QB-3, #1059)

**Reviewed head:** `03960b69cef11cf2702409bab93ebb8a6510cce8`
- The review was done at `d48f4c63a011acaa04ab57f32fa1cb90079d9bf4` (commit A). `03960b69` is a single-parent child of A that applies this review's changes; the delta check is in §8.
- The record at the reviewed head is `verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/QB3-EVIDENCE.md`. It is blob `9dac27fe5265d6b617937953cdab004e433f5a0f`, 180 lines.
- **Base:** `main` `4f016afd943f5a3939493eab752664949e90dbbb`. Relative to the base, the reviewed head adds that one file and changes nothing else.

**Reviewer.** An independent reviewer that is model-authored, did not write the record and works read-only. It also reviewed the landing proposal but wrote no part of the record. This is not a human review.

**Method.** The mathematics is re-derived by hand from the record alone. The source text is compared mechanically against commit `e50917cab03a1c8db6fd668ecad2a04c880399db` of branch `research/born-sel-b-measure-20261104`. Every citation is checked at the base. The repository checks are re-run with `python3 -I` at the exact commit. No probe, enumeration or simulation was run.

Line numbers below are lines of the record at the reviewed head.

## 1. The mathematics, re-derived by hand

- **The two-state swap (§3, [D]).**
  - Main:78 states the map "at (2,2)": `φ(v,h) = (h,v)` on `C_V = C_H = {0,1}`. The record marks its reading of Main:60's "two-state swap" as this map as [D], which is correct, since Main:60 gives no formula.
  - `π_V φ(a,h) = h`, so `Γ_1(a,j) = μ_H{h : h = j} = μ_H(j)` for every root. The uniform prior gives `J/2`, and the point mass `δ_0` gives `[[1,0],[1,0]]`.
  - For a product law and a root with `ν(a) > 0`, `x_1 = h` with `h ~ μ_H`. So `P(x_1 = j | x_0 = a) = μ_H(j)`, which is row `a` of `Γ_1`.
  - The joint law `P(x_0 = a, x_1 = j) = ν(a) μ_H(j)` therefore differs between the two priors. Hence the rooted family, the one-step rooted matrix, the conditional prediction and the finite-horizon law all differ, as §3 concludes. Correct.
- **CE-8 (§4, Lemma B3).**
  - The two 4-cycles `O_A` on `{0,1}×{0,1}` and `O_B` on `{0,1}×{2,3}` together cover all eight states, so φ is a bijection of order 4. The visible sequences are `0101…` and `0011…`, as stated.
  - **Under β**, the next visible values are:
    - from root 0, `(1,1,0,1)` over `h = 0..3`, from `(1,0), (1,1), (0,3), (1,2)`;
    - from root 1, `(0,0,1,0)`, from `(0,1), (0,0), (1,3), (0,2)`.
    
    So `T^β = [[1/4,3/4],[3/4,1/4]]`, which is not a permutation matrix.
  - **Under `unif(O_A)`**, root 0 goes to visible 1 from both of its states and root 1 goes to visible 0, so `T^{α,A}` is the swap.
  - **Under `unif(O_B)`**, each root has one successor of each visible value, so `T^{α,B} = J/2`.
  - These are the three one-step matrices of the μ-number sentence in §1. Correct.
- **Lemma B4 (§5).**
  - *Hypotheses.* Every `κ_a` is a probability law on `C_H`, roots of visible probability zero included, so every row of every `Γ^κ_t` sums to 1. Positivity of a visible history is taken under `ν⊗κ`. This is the hypothesis correction of the QB-4 review, and it is the one step (iii) uses.
  - *(i)* `φ^L = id` gives `Γ^κ_L = I` and `L`-periodicity.
  - *(ii)* For `t ≤ k`, either `L | t` and `Γ^κ_t = I`, or `Γ^κ_t = Γ^κ_{t mod L}` with `1 ≤ t mod L ≤ min(k, L−1)`.
    - So if those matrices are all permutations, every `Γ^κ_t` with `t ≤ k` is one.
    - Because the space is finite, a positive-probability history then satisfies `x_t = σ_t(x_0)`.
    - Distinct histories therefore have distinct roots, and `σ_k(x_0) = σ_k(x′_0)` contradicts injectivity. The case `L | k`, where `σ_k = id`, is covered.
    - The degenerate cases `L = 1` and `k = 0` are vacuous.
  - *(iii)* `I = Γ^κ_s Λ`, with both factors row-stochastic, makes `Γ^κ_s` a permutation matrix. This is `isPermMatrix_of_stochastic_inverse`, whose hypotheses are both factors row-stochastic and `A·B = 1` or `B·A = 1`.
    - The conclusion is non-P-divisibility on `{0,…,n}` in Main:137's sense, which requires a stochastic `Λ_{s,t}` for every `s < t ≤ n`.
    - It holds a fortiori under step-by-step divisibility, since step factors compose.
  - *Zero-probability remark.* It is correct: the argument holds for every probability-law choice at those roots, but which rows the conclusion concerns there depends on the choice.
  - *The CE-8 part.* Correct.
    - The three laws are the stated product laws.
    - Under `unif(O_A)` the visible process is deterministic `0101…`. Every `Γ_t` is the swap or `I`, so every `Λ_{s,t}` exists as a permutation, and no two distinct positive-probability histories share an endpoint.
    - Under β and under `unif(O_B)`, `Γ_1` is not a permutation and `Γ_4 = I`, so step (iii) excludes `Γ_4 = Γ_1 Λ`.
    - `Γ_2` and `Γ_3` are not needed for these conclusions.

No gap was found in these derivations under their stated hypotheses.

## 2. Faithfulness to the source

- **§1 (lines 47–74).** Identical to `QB3-QB4.md` lines 48–75 at `e50917ca`, except for the two markers listed in §6 item 5.
- **§2, §4 and §5.** Each line was compared with its source range in `BORNSEL-B-MEASURE.md` at `e50917ca`: BSB:49–50, :66, :126, :129–136 and :147–162. Every difference is a listed §6 item:
  - the BSB:66 list label, and the capital and full stop that follow from removing it;
  - BSB:126 cut to its first two sentences;
  - "(C1 witness)" removed at BSB:133;
  - the BSB:147 bracket;
  - the added definitions of α, β, `J`, `T^β` and `T^{α,A}`/`T^{α,B}`.
- **Text outside the source ranges.** The status header, the framing sentences of §1 and §2, §3, §6 and §7 are the record's own text, as its line 149 states.
- **BSB:137–138 and the lemmas G, G2, N2.1, E and U.** Not carried. The classification does not use them.
- **The writer's three choices are acceptable.**
  - (a) BSB:147's bracket becomes `[D]`. This keeps the layer label and removes only the source's revision and reviewer note, which a record does not narrate (AGENTS.md §A.27).
  - (b) The two framing sentences of §2 are accurate. "A *branch* is a choice of the measure μ" matches the source's usage, and Main:137 does define P-divisibility on `{0,…,n}`.
  - (c) The status header cites this review file, which lands as a single-parent child of the reviewed head. Since the landing merges both commits, the reference resolves on `main`.

## 3. The QB-3 wording

- After the two markers are replaced, the wording is identical (whitespace normalized) to the "full form" of the review #1082 c.6651169194.
- "[landed record]" now reads "(§4 of this record)", and "[landed B4]" reads "Lemma B4 (§5 of this record)". Both point to the right sections.

## 4. Limitation, status and owner quotations

- **Limitation.** Line 5 carries it verbatim: "OI has not yet been shown to derive the Born rule or select the physical probability measure."
- **Layer.** Lines 8–9 state paper derivations [D], none kernel-checked, with every other input on `main` and classified in §7.
- **Owner quotations.** Each matches its source comment word for word, with author and posting time correct:
  - #1059 c.6650820790 (05:49:40Z), three quoted sentences;
  - #1059 c.6651648653 (06:45:16Z);
  - #1082 c.6652198391 (07:19:59Z);
  - #1082 c.6652561689 (07:42:07Z), three quoted sentences.

## 5. Citations at the base `4f016afd`

All cited lines and declarations say what the record uses them for.
- **Main.md:**
  - Main:56 (Lemma 3's selection principle);
  - Main:60 (different visible laws; the two-state swap);
  - Main:78 (the swap map at (2,2));
  - Main:133 (the stochastic-inverse lemma);
  - Main:137 (the shared-prior theorem and the definition of P-divisibility);
  - Main:290 (the Born-form `T_ij`);
  - Main:556 (exponent insensitivity);
  - Main:640 (`L`-periodicity);
  - Main:726 (posit (iv), "not derived").
- **Lean:**
  - `D_imp_Qfb` at `Equivalence.lean`:294, with its proof term at :297–299 (`U := permMatrix step.symm`, `read := Prod.fst`);
  - `finite_horizon_equivalence` at `Equivalence.lean`:462;
  - `isPermMatrix_of_stochastic_inverse` at `EquivalenceChain.lean`:110.
- **Other files:** `PROGRAMME.md` line 96 (§3.4), and `ROADMAP.md`:80 (row P1, the obligation text, in a file marked frozen historical).

The §7 classifications (AGENTS.md §A.42 item 8) are correct.
- Every manuscript line, Lean declaration and file is support on `main`. The reading of the proof term is marked as a reading, not a theorem.
- The swap computation is marked [D].
- Commit `e50917ca`, its branch and PR #1082, the four owner records, the model-authored reviews and the Issues are each classified, by the claim they are attached to, as provenance.

## 6. Register and scope

- The register is neutral and technical.
- The record does not narrate its own revision history, and it does not assert a claim and then qualify it (AGENTS.md §A.27, §A.30).
- No sentence claims beyond the record's scope:
  - no manuscript claim is promoted, and no file under `papers/` or `book/` changes;
  - no physical measure is sourced;
  - nothing is inferred for the native wave substratum;
  - no other lemma of the source assessment is made a premise.

## 7. Checks at the reviewed head

Run with `python3 -I` in a detached checkout of `03960b69`:
- `tools/legacy_records_check.py 03960b69…`: 303 records in 75 closed namespaces intact, exit 0.
- `tools/citation_roles_check.py 03960b69…`: self-test OK, all hold, exit 0.
- `tools/duplicate_check.py`: OK, exit 0.
- `tools/staleness_check.py`: OK (13 matched, 0 unstamped), exit 0.
- `tools/artifact_placement_check.py`: OK, exit 0.

The added text was also scanned for secrets and sensitive data under AGENTS.md §A.42 item 4: tokens, keys, signed URLs, IP and e-mail addresses. None was found. The file contains no bare `---` line. The same checks also passed at `d48f4c63`.

## 8. Changes required at A, and the delta check of `03960b69`

The review of `d48f4c63` returned ACCEPT WITH CHANGES.

**Required:**
- **C1.** Remove a planning sentence (a Lean-formalization ranking) from the status header. It was planning content in a record, and it used an off-`main` review for a claim that §7 did not trace.
- **C2.** Correct the status header's input list, which omitted the two non-manuscript files cited in §7.

**Optional:**
- **O1.** Cite `ROADMAP.md`:80 as row P1.
- **O2.** Define `T^β`, `T^{α,A}` and `T^{α,B}`.
- **O3.** Repair the list-item fragment left by the BSB:66 label.

`git diff d48f4c63 03960b69` touches only the record (+9/−8) in six hunks. Each maps to one of these items:
- **C2:** lines 8–9, "a manuscript line, a Lean declaration or another file on `main`";
- **C1:** line 17, which now reads only "#1059. The remaining work is planned there, not here.";
- **O1:** line 45, "(`verification/ROADMAP.md`:80, row P1)";
- **O3:** line 82, capitalized and ending with "."; recorded in §6 item 4;
- **O2:** line 86, the new definition line; recorded in §6 item 6.

No other line changed. §1's wording and the verbatim passages of §4 and §5 are unchanged, so §1–§3 of this review apply unchanged to the reviewed head.

**Verdict: ACCEPT** — `QB3-EVIDENCE.md` at `03960b69cef11cf2702409bab93ebb8a6510cce8`.
