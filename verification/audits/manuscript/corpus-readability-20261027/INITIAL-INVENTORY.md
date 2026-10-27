# Initial corpus inventory and pilot selection

**Status:** read-only sampling, preliminary — not a complete readability audit.
**Inspected source baseline:** `main` at `7a7a654d13ebb21d426ccb3a02daa2a5b126cdac` (2026-10-27). No manuscript edits.
**Sampling:** repository paths and file sizes; first ~110 lines of Juno, Medicine, Computation, book ch01, ch03 and readers-guide. The latest open source-correction and Introduction branches were not treated as baseline truth.

## Inventory
- `papers/`: eleven active standalone Markdown papers (Bioinformatics, Complexity, Computation, GR, Juno, Main, Medicine, Methodology, SM, Structure, Substratum; the Introduction is still pending in #918), plus `Explainer.md` pending controlled retirement. Do not call Explainer an active final manuscript.
- `book/`: Chapters 00–19 (20 chapters), preface, readers-guide, glossary, appendices A–C, acknowledgments and bibliography; generated `The-Incompleteness-of-Observation-FULL.md` plus TeX/PDF.
- Generated `.tex` and `.pdf` are distinct build artifacts, not separately authored sources. Mirror parity is a release gate.

## First-pass observed issues (sample only)
| Source | Observation | Constraint on revision |
| --- | --- | --- |
| Main opening and theorem sections | Foundational mathematical results, model definitions and scope qualifications require accessible conceptual entry points | Add intuition and examples alongside the existing formal results; preserve all theorem hypotheses, proofs, exact evidence levels, and cross-references |
| Medicine abstract | A very long sentence tries to distinguish representation, memory, recurrence, several conditions and biological application at once; followed by a long catalogue of applications | Separate theorem, conditional biological application and experimental proposals. **Do not change live science before SC-24 corrections are integrated** |
| Computation abstract | Nested assumptions for the conditional BQP model occupy an extended sentence | Provide an intuitive setup and a concise assumptions summary while preserving the full exact hypothesis list and caveats near the theorem |
| Book ch01 | Opens with dense symbolic equivalence, rooted memory and Bell hypotheses before the embedded-observer example | Introduce the embedded-observer example before or adjacent to formal notation; preserve exact equivalence and the distinction between Markov memory, rooted indivisibility and backflow |
| Book ch03 | Several nested structural realism axes and gauge equivalence classes appear before a plain example | Explain the two axes with a simple concrete instance, then show precise formal distinctions, without eliminating philosophy or substantive explanations |
| Readers' guide | Useful separate reading paths already exist, with estimates and source references | Preserve this navigation. Validate references and conditional-status wording; simplify only where necessary |

## Recommended two pilots
1. **Standalone paper: `papers/Main.md` (owner-selected).** The foundational technical reference and the best pilot for improving the explanation of central OI results without reducing proof strength. Map theorem-by-theorem dependencies, formal hypotheses, proof status and examples; improve the explanations around the mathematics rather than replacing it. Start only after active source corrections have been reconciled.
2. **Book chapter: `book/ch01-observation.md`.** The foundational explanation many readers encounter first, good for testing intuition → explanation → mathematics → implications and mirror-preserving edits. Wait for #959 and related memory-scope corrections to land before drafting text.

## Plan for pilot deliverables
- Annotated section map; glossary-first-use inventory; example/analogy preservation map.
- Before/after claim matrix: exact theorem, hypotheses, evidence level, citations, numerics and open questions, plus the educational purpose of important explanations.
- One short *proposed* passage per pilot in a separate plan/review record, not replacing source text until dependencies settle.
- Independent scientific and comprehension review, including raw paper-only reader responses before evaluation.
- Dedicated small PRs for eventual manuscript edits; do not turn this planning PR into a giant rewrite.

## Caveats
The inventory lists files on the pinned baseline, not a census of all active scientific results. SC-24, SC-25, SC-26, SC-27 and #918 were evolving at the time of inspection. Rebase and rescan affected text before making any edit.
