## Confirmation of PR #959 at `72eece11fba970e9613593f2d52a4d86bf043eff` (single parent `8d8ca8c6`)

**Verdict: ACCEPT WITH CHANGES.** Two short unconditional ceiling claims survive in Bioinformatics, and two in ch17 (finding 1). Everything else is confirmed.

**1. Required: unconditional ceiling claims that remain.** Each asserts that the open premise holds.
- **Bioinformatics :56.** Current: "The information-theoretic ceiling identified here has practical consequences: it explains why scaling foundation models has not produced the expected improvements…". Proposed: "Where the relevant structure lies in the hidden fibers, the information-theoretic ceiling explains why…".
- **Bioinformatics :186.** Current: "The 'deep learning fails to beat baselines' puzzle is the framework's information-theoretic ceiling made empirically manifest." Proposed: "…puzzle is what the ceiling predicts where the relevant structure lies in the hidden fibers."
- **ch17 :22 (mirror FULL).** Current: "…domains where the framework's ceiling predicts and explains observed failures". Proposed: "…where the conditional ceiling would explain observed failures".
- **ch17 :78 (mirror FULL).** Current: "The transcriptome's information about regulatory structure is bounded by what correlation methods recover." This is unconditional and unsupported. The same paragraph's "structurally calculable amount" is claimed but never computed. Proposed: "Where the strict gap holds, the transcriptome's information about regulatory structure bounds what any method recovers; multi-modal methods raise the ceiling by the conditional information each substratum modality adds."
- **Optional, ch17 :76.** "producing causal predictions that exceed transcriptome-only ceilings" could read "…that outperform transcriptome-only methods".

**2. The diff contains only the listed changes.** `git diff 8d8ca8c6 72eece11 -- '*.md'` touches:
- **ch03:** :36, :102, :114 and :240.
- **ch15:** :16, :49, :87, :134 and :260.
- **ch17:** :14, :20, :30, :34, :36, :40, :42, :70, :72, :206 and :218. Of these, :36, :40 and :42 were in my earlier finding 2.
- **Bioinformatics:** :18, :48, :142, :148, :152, :198, :459, :463, :465, :467 and :469.
- **GR:** :591.
- **FULL:** each book edit is mirrored there.

Nothing else changed.

**3. Each item is correct against its source.**
- **ch03.** It now reads "accessible memory where the hidden sector reads back its record (C4), and, on any finite reversible substratum, recurrence-cycle P-indivisibility …". This is consistent with Structure :1025.
- **ch15.** :16, :87 and :260 now match §15.9 item 1, appendix-a F2/F3 and Complexity :486/:496/:498.
- **Bioinformatics.** :463 states the conditional result at full strength, and :465 and :467 cast the GRN as "proposed as subject" and "consistent with".
- **ch17.** :14, :20, :30, :36, :42, :70, :72 and (P1) attach the strict gap as an open hypothesis.

**4. ch15 :134 counterfactual: acceptable.** "If the gain were large enough, NV sensors would compete with … SQUIDs …" follows directly after "no numerical improvement factor is claimed". It states what a large gain would mean, not that one occurs.
- **Optional, same class: ch15 :91.** "A factor-of-three improvement … would have substantial commercial impact" is also a counterfactual. But it repeats the deleted 3–10 figure, and "a specific commercial design target" implies a quantitative target. Drop "factor-of-three", for example "A sizeable improvement…".
- **Optional, pre-existing: ch15 :103 and Complexity :488.** The per-cycle revival amplitude "O(τ_S/τ_B) … ~0.1% … ~10%" is an underived heuristic. No "none derived" statement contradicts it, so it is not a defect under your criterion. It fits with the SC-22 heuristics.

**5. GR :591, the K_{mL} step: correct.**
- K_t is periodic with period L, so K_{mL} = I.
- Taking mL > s turns K_sΛ = K_{mL} = I into a stochastic right inverse of K_s, which the lemma forbids unless K_s is a permutation. This is how the Lean `routed_forces_indivisible_somewhere` does it.
- "finite representative of the constraint surface" is good wording.
- **Cosmetic, optional.** "for every integer m" should be "for every m ≥ 0", since K_t is defined only for t ≥ 0.

**6. Mirrors, regenerated files, gate.**
- **Mirrors.** The chapter and FULL edits are the same set of lines against `8d8ca8c6` (40 lines) and against base (84 lines). No chapter line is missing from FULL.
- **Regenerated files.** For GR, Bioinformatics and FULL, fresh pandoc output matches the committed `.tex` apart from the source-sha256 stamp, and the stamp matches the `.md`. The PDFs contain the new text.
- **Release gate.** Every step passes except `lean-axioms`, which fails only because there is no lake locally.
- **Edge probe.** `edge_rigidity_probe.py` reports ALL CHECKS PASS.

**Answers**
- **(a) Is every claim supported?** All except the four sites in finding 1: Bioinformatics :56 and :186, ch17 :22 and :78. Each still asserts the open premise unconditionally.
- **(b) Is any established result unnecessarily weakened?** No. The :138 conditional theorem and its restatements at :463 and ch17 :14 are at full strength. (P1), (P4), (P6) and (P7) are now conditioned on an open premise, which is the right strength for them.

I removed the worktree.
