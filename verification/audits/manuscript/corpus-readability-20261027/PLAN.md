# Corpus-wide readability programme (draft plan)

Status: **PLANNING ONLY — unreviewed; no manuscript changes in this PR.**
Date: 2026-10-27
Scope: all active scientific papers, companion papers, the book and FULL mirror, and reader-facing documentation. The Introduction (#918) has its own publication gate and is not to be overwritten or blocked by this programme.

## Objective
Make every work as comprehensible as possible to scientifically curious nonspecialists, students, and experts, without loss of any critical scientific **or explanatory** content. State the strongest established result, its significance and exact hypotheses, and what remains open. A readability improvement must not silently narrow or strengthen the science.

## Work phases
1. **Inventory and baseline.** Freeze a main commit after the active scientific-correction PRs settle. Inventory every active paper/chapter, length, terminology, definitions, illustrations, cross-references, proof references, all explanatory passages, and intended audience. Map dependencies and the book/FULL mirrors. Record ambiguous and repeated passages; repetition is not automatically expendable.
2. **Style guide and pilot.** Review the Introduction's tested accessibility lessons. Choose one companion paper and one book chapter as pilots before touching the whole corpus. For each topic use intuition → explanation → precise mathematics → implications when useful. Introduce specialist terms on first use; place plain-language meaning beside every substantial theorem; use concrete examples, analogies explicitly labelled as analogies, and explain figures/equations. Preserve helpful detail, historical context and distinct pedagogical routes.
3. **Independent per-document revisions.** Separate reviewed PRs (or small batches of independent chapters). Shorten opaque prose and unnecessary repetition while retaining every theorem, proof hypothesis, counterexample, quantitative claim, caveat, citation, open question and substantive explanatory insight. Never remove content merely to meet page targets. Treat the technical Main paper as a full technical reference, not a popular rewrite.
4. **Comprehension testing.** Paper-only fresh-reader AI tests for nonspecialist and undergraduate understanding, plus a technical scientific reviewer to check the answers and scope. Save raw responses before judging. Classify misunderstanding, legitimate objection and presentation problem separately; human reader testing is desirable but not a publication blocker unless separately authorized.
5. **Verification and integration.** On exact reviewed commits check claim-to-proof mapping, Lean references and assumptions, equations, numerics, references, coverage census/fingerprints, build outputs/PDF legibility, the book/FULL mirror and CI. Check corpus-wide terminology and cross-references. No proof claim, citation status, ledger ID, theorem or experimental result changes silently.

## Acceptance gates
- **Scientific fidelity:** a before/after claim ledger, including hypotheses, scope and evidence level; independent scientific ACCEPT.
- **Explanatory fidelity:** an inventory of critical explanations and examples with preservation or explicit reviewed reason for relocation/condensation.
- **Readability:** fresh paper-only comprehension review plus independent editorial review; explanatory paragraphs read naturally without dependence on another manuscript for essentials.
- **Reproducibility:** manuscript/mirror guards, Lean/CI, citations and artifact rebuilds pass on the final SHA.

## Governance
- **No corpus-wide blind rewrites.** This PR owns the plan and audit trail. Actual edits should be split into reviewed, tractable PRs to prevent interleaved conflicts.
- **Dependencies:** finish #918's current scientific/publication work and ongoing source corrections (#959 and other open SC units) before bulk edits or publication claims. Inventory/pilot plans may proceed read-only in parallel; do not block #918's merge on this programme.
- **Merging:** draft by default, no merge until independent review, green CI and explicit owner approval at the exact SHA. Maintain immutable historical receipts and explicit retirements if ever warranted.
- **Progress:** report document-level status, readability gains, evidence of comprehension, preserved science and any newly found scientific defects separately.
