## Re-review of PR #959 at head `8d8ca8c678db3711d1ec7e0456f0ab39bcc0aeb8`

**Verdict: ACCEPT WITH CHANGES.** All eight required and six optional findings from the review at `7c117827` were applied correctly. The GR and SM derivations are sound. Two required issues remain, both about the same thing: the edits made some claims conditional, while other text in the same documents still states those claims unconditionally.
- Bioinformatics and ch17 now contradict themselves on the information-theoretic ceiling (findings 1 and 2).
- ch15 still carries numbers and magnitude claims where the same chapter says none are derived (finding 3).

I also flag one tension left by my own earlier ch03 suggestion (finding 4, required, minor).

**What I ran.** I used a new detached worktree, now removed; disk had 23 GB free.
- **Diffs.** I reviewed `git diff 7c117827 8d8ca8c6` and re-checked the full `55e3217b..8d8ca8c6` diff over the `.md` files.
- **Release gate.** Every step passes except `lean-axioms`, which fails only because there is no lake locally.
- **`edge_rigidity_probe.py`:** ALL CHECKS PASS.
- **Mirrors.** The chapter edits and the FULL.md edits are the same set of lines, both against base (27 removed and 27 added) and against `7c117827` (16 and 16). No chapter line is missing from FULL.
- **Regenerated files.** For every paper and for FULL, fresh pandoc output matches the committed `.tex` apart from the source-sha256 stamp, and the stamp matches the `.md`.
  - The PDFs were regenerated and contain the new text.
  - Page counts: GR 88, Complexity 35, book 558.
  - Computation is untouched and correctly stays at `7c117827`.
- **Voice scan of added paper lines.** No caps hits and no history phrases.

### Required

**1. Bioinformatics contradicts itself (§A.25, §A.30).**
- **What changed.** :138 now states the correct conditional result. The attribution is right: the hidden-memory theorem plus the canonical-predictive-quotient theorem with `fiber_freedom`. It ends "Whether the causal structure of a given GRN lies in those fibers is open."
- **What it contradicts.** The same paper still asserts that GRN structure lies under the ceiling:
  - :142, the next paragraph: "This is the information-theoretic ceiling in action … the ceiling is structural, not computational." This is assert-then-qualify within §3.4.
  - :463–:467 (§9.2): "no method using only scRNA-seq data … can recover certain quantities"; "The quantities subject to the ceiling include: the cell's causal regulatory network structure (§3) …"; "The ceiling is empirically demonstrated in the foundation-model literature." These directly contradict :138.
  - :18 (summary): "a ceiling that no transcriptome-only model can exceed."
  - (P4) :148, (P6) :152 and (P7) :198 state it unconditionally.
- **Why it cannot be deferred.** Before this PR the paper overclaimed consistently. After it, the paper says "open" in §3.4 and "subject to" in §9.2. Because the PR created the contradiction, the fix belongs in this PR.
- **Proposed text:**
  - :142: "Where the GRN's causal structure lies in the hidden fibers, this is the ceiling at work: scaling transcriptome-only models cannot break through it."
  - :463: "…: where a quantity differs between hidden-sector completions that share the scRNA-seq law, no method using only scRNA-seq data … can recover it."
  - :465: "The quantities proposed as subject to the ceiling include: … For each, whether it lies in the hidden fibers is open."
  - :467: "The foundation-model literature [6, 7] is consistent with the ceiling: …"
  - :18: "…identifies a conditional information-theoretic ceiling: transcriptome-only models cannot recover quantities that differ between hidden-sector completions sharing the transcriptome-level law."
  - Prefix (P4), (P6) and (P7) with "Where the relevant structure lies in the hidden fibers, …". They may stay as predictions; they rest on that open premise.

**2. ch17 contradicts itself (mirror FULL as well).**
- **What changed.** :14 now opens "rests on a conditional theorem … where a quantity differs between hidden-sector completions …".
- **What it contradicts.**
  - The same paragraph continues "This bounds the achievable performance … explaining the well-documented persistent failure", which asserts the condition holds.
  - :20 says "The framework's structural commitment is that this hidden-sector content carries information that no amount of transcriptome data can recover."
  - §17.2 :30, :36 ("The framework's content is that $I(\text{phenotype}|T)$ is strictly less than $I(\text{phenotype}|T,S)$"), :40 and :42 are all unconditional.
- **Fix.** Restate them conditionally, as in finding 1. For example, at :14: "Where the relevant quantities lie in those fibers, this bounds … and explains …". At :20, :36 and :42, make the strict-gap claim the framework's hypothesis and state that whether it holds for a given task is open.

**3. ch15 numbers and magnitude claims (mirror FULL as well).** You asked me to confirm that no number survives where a section says none is derived. That is not yet true.
- **Done correctly.**
  - The NV and coherence numbers are gone from ch15 :18, :130, :132 and :244, and from Complexity :488 and :490.
  - The :128 rewrite (memory first, revival as a further signature that C1–C4 do not supply) is correct.
  - §15.9 item 2 is correct.
  - appendix-a F2 and F3 ("gain/factor not quantified") are consistent with the new text.
- **Still surviving.**
  - ch15 :134 ends "This would make NV sensors competitive with … SQUIDs …". That is a magnitude claim, and it immediately follows "no numerical improvement factor is claimed here". Delete the sentence, or reduce it to "If the gain were large enough, NV sensors would compete with SQUIDs at room temperature."
  - ch15 :260: "specific quantitative predictions … NV sensing at SQUID-competitive sensitivity". Change to "testable predictions … backflow-aware NV sensing, engineered-bath coherence extension".
  - ch15 :16 ("could reduce overhead by factors of three to ten, with concrete numerical predictions") and :87 ("The framework's estimate … a factor of three to ten … 3,000 → 300–1,000 physical qubits"). These contradict §15.9 item 1 (:240, "The framework does not supply the size of that gain"), appendix-a F2 and Complexity :486/:496.
- **Scope note.** The error-correction numbers belong to the memory class, not backflow. They are still a same-chapter contradiction of the kind your check targets, and the fix is a few sentences. For :16, use "…could reduce the effective error rate; the size of the gain is not derived (§15.4, §15.9)". For :87, use "The size of the reduction is not derived: converting the correlation length into an overhead requires a code, decoder and noise spectrum (§15.9)".
- **Complexity is clean.** :17 quotes timescale ratios, not gains, and is fine.

**4. ch03 :36, :102, :114, :240 (mirror FULL as well).** The writer applied my earlier suggestion exactly: "memory/divisibility — on any finite reversible substratum, recurrence-cycle P-indivisibility …". That suggestion was incomplete.
- **The remaining tension.** The P-indivisibility clause is now correctly scoped. But "memory/divisibility" itself still appears among features "any partial-trace observation must produce" (:36) and that are "universal across observer-admitting systems" (:114). Structure :1025 says "The third is not necessary: a memoryless hidden sector yields a Markovian reduced law."
- **Fix:** "memory/divisibility — accessible memory where the hidden sector reads back its record (C4), and, on any finite reversible substratum, recurrence-cycle P-indivisibility wherever a rooted visible map is not a permutation". Mirror the same wording at :102, :114 and :240.

### Checked and correct

**5. GR :591, the extension argument.** I checked each step independently; it is a correct paper proof with no hidden gap.
- **Finite order.** On a finite φ-invariant Γ_phys (a stated hypothesis), φ restricted to the surface is a permutation of a finite set, so it has finite order L.
- **K_t is square.** For visible values a ∈ V′ = π_V(Γ_phys), the fibers F_a are nonempty. φ^t maps Γ_phys into itself, so every visible value reached lies in V′. K_t is therefore V′×V′.
- **K_t is row-stochastic.** K_t(a,j) = μ_a{h ∈ F_a : π_V φ^t(a,h) = j}, and each per-fiber prior μ_a is normalized.
- **K_L = I.** φ^L = id on the surface.
- **The lemma applies as stated.** `isPermMatrix_of_stochastic_inverse` takes any finite square row-stochastic A and B with A·B = 1. Main's version covers the same case.
- **No visible prior or full support is needed.** This matches Main :139.
- **One-line precision gap (optional).** If the non-permutation K_s has s ≥ L, compare it with K_{mL} = I for some mL > s; that is how the Lean `routed_forces_indivisible_somewhere` handles it. Suggested wording: "…with $K_s\Lambda = K_{mL}$ for $mL > s$…".
- **Minor optional point.** The paragraph calls Γ_phys a "submanifold" and then assumes a finite surface. That reads acceptably as a hypothesis on a finite representative; "on a finite representative of the constraint surface" would be smoother.
- **C1 sentence.** It matches Main :74 ("ADM boundary Hamiltonian and the constraint structure supply a bidirectional coupling stronger than $H_{\rm int}\neq0$"). Dropping "non-perturbatively" is fine, and so is the K_t naming.

**6. SM :112.** Correct against the state space and update rule in SM :106 and :112.
- **State space.** It is (x(t−1), x(t)) ∈ (ℤ_q)^{2L}. The visible sector is (x_0(t−1), x_0(t)) and the hidden sector is the other 2L−2 coordinates, so the product structure Main §2.3 requires holds, with |C_V| = q² ≥ 2.
- **Update.** The update is x_0(t+1) = x_{L(0)}(t) + x_{R(0,x)}(t) − x_0(t−1), with L(0) = L−1. R(0,x) ∈ {1,2}, which differs from L−1 because L ≥ 4. Under the uniform prior, x_{L−1}(t) is uniform and independent of the coordinate that fixes R(0,x).
- **Conclusion.** The second visible coordinate is therefore uniform over ℤ_q while the first is fixed, so the row has q > 1 positive entries and the map is not a permutation.
- **Enumeration.** My earlier exact enumeration at (L,q) = (4,2), (4,3), (5,2) agrees. The writer's two countercontrols are also the right ones.
- **Notation (optional).** "L" names both the ring size and the left-neighbour map; this predates the PR.

**7. The other findings and the writer's departures.** All applied correctly:
- Complexity :484 now separates the memory cases from the revival cases. Complexity :370 says "lower bound".
- Main :730: "bears only on whether …; (i) does not imply (ii)".
- Preface: "fixed finite reversible representative".
- Explainer :135: "reversible (bijective)", with the grammar fixed.
- ch01 :163 is rewritten correctly.
- Structure :903 and :1041 are correct; §14.7–§14.8 exist and cover LQG and causal sets.
- ch15 :116, :122, :138 and :18 now use "proposes" or the memory-first form.
- The departures are acceptable: no "(§15.6 below)", the K_t naming, dropping "non-perturbatively", and leaving ch01 :201 unchanged (its wording follows Main :532).

### Explicit answers
- **(a) Is every claim supported?** Not yet. The unconditional ceiling claims in Bioinformatics :18, :142, :463–:467 and (P4)/(P6)/(P7), and in ch17 :14, :20 and §17.2, are not supported now that :138 states the result as conditional. The remaining ch15 magnitude claims (:16, :87, :134, :260) are not derived. ch03's must-produce framing of memory/divisibility overstates. Everything else is supported, including both new derivations in GR :591 and SM :112.
- **(b) Is any result unnecessarily weakened?** No. SM :112 now states the result at full strength, and Bioinformatics :138 states the strongest conditional result that is proved.
