# SAMPLER-CORR-1 manuscript site ledger

Source main `192bbf29402d23fd49acc1a6d1a65c8cd0ff41b7`. The line anchors in the initial inventory refer to that revision. [Accountable issue and paper-only authorization](https://github.com/amaybaum/incompleteness/issues/1375) · [A1 Main roots audit, R5](https://github.com/amaybaum/incompleteness/blob/192bbf29402d23fd49acc1a6d1a65c8cd0ff41b7/verification/audits/foundations/a1-main-roots-20261118/AUDIT.md#L70)

## Initial inventory

| Site at the source pin | Statement before correction | Required disposition |
| --- | --- | --- |
| `papers/Main.md` §3.4, lines 566–570, operational boundary and gluing clause (1) | The branch-matrix grid bound is assigned to registers over the instruments' entry ring. The initial state is arbitrary and the finite-bit sampled-law bound is open. | Include the supplied initial matrix and Kraus data in the working domain. Require exact arithmetic and exact real threshold comparisons. Distinguish finite labels and a compiled table from the arithmetic needed to supply those labels and comparisons. |
| `papers/Main.md` §3.4, lines 578, 582, capacity and construction | The reachability count uses the instrument ring, and the proof places normalized conditionals in that ring. The register is initialized from the input state. | Index the finite set by the initial state. State what the counted labels measure and show why cross-multiplied thresholds need exact compare operations without requiring ring division. |
| `papers/Main.md` §3.4, lines 580–582, fixed-point lemma and proof | The raw trace-norm telescope has a zero initial error, and the proof leaves the sampled-law step open. | Account separately for the initial approximation and raw step errors. Retain the restricted positive-input estimate and the open clipped, normalized sampled-law bound for the actual Hermitian simulator. |
| `papers/Main.md` §3.4, lines 584–586 and 598–604, and §5 line 776 | The controlled-map, net/density and summary claims inherit the grid construction or the finite-table existence result. | Tie the inherited grid claim to fixed, supplied initial and instrument data and exact comparisons. Keep the finite-law equivalence, real-prior existence and net existence with finite labels. |
| `papers/Substratum.md` §6.4, line 533 | Finite adaptive experiments have finite deterministic realizations at finite accuracy by the gluing and net theorems. | Carry the supplied-data scope of the finite-table result into the summary. |
| `book/ch01-observation.md` line 195, `book/ch04-methodology.md` line 146, `book/ch19-open-problems.md` line 126, `book/README.md` line 17 | The summaries state finite-menu realizability at requested finite accuracy. | Identify the supplied-data finite realization and distinguish it from a numerical sampler where the summary speaks to implementation. |
| `book/glossary.md` line 107 | The operational gluing entry gives the grid error, context-fixed maps and capacity bounds without the arithmetic qualification. | Attach the exact-data and threshold condition and carry the open finite-precision sampled-law bound. |
| `book/The-Incompleteness-of-Observation-FULL.md` lines 530, 1254, 5271, 6686 | The four affected chapter and glossary passages are mirrored in the consolidated source. | Apply each source change to the matching paragraph and verify paragraph equality. |
| `papers/{Main,Substratum}.{tex,pdf}` and `book/The-Incompleteness-of-Observation-FULL.{tex,pdf}` | The maintained publication artifacts carry the source claims. | Rebuild only these three publications with `build.sh` and verify source–TeX digests, page counts and the affected content. |

The neighboring claims about fixed-basis finite laws, real-prior response tables, exact operational completion, conditional BQP and the Bell interface were checked as separate claims. The correction leaves those results intact. Historical audit records document the source pin and retain their historical wording.

## Review checks

1. **Exact input arithmetic.** For the rational projectors $|0\rangle\langle 0|$ and $|1\rangle\langle 1|$ and $\rho_0=\operatorname{diag}(\alpha,1-\alpha)$ with irrational $0<\alpha<1$, one raw outcome weight is $\alpha$. The instrument-generated rational ring cannot contain that weight. A finite table can still carry the supplied real law. A uniform finite grid alone assigns rational masses.
2. **Finite precision.** Follow the initial-state trace-norm term through exact instruments separately from any error in the raw digitized branches. Check the hypotheses on the clipped and normalized law and the scope of the positive-input estimate.
3. **Equivalence and mirrors.** Compare the finite-horizon theorem and real-prior response-table construction to the pinned source. Check the placement of every correction in the manuscript sources and the regenerated TeX/PDF mirrors. Claude reviews the exact scientific commit independently.

The scientific question is an arithmetic qualification of one mathematical construction. Physical measurement sourcing remains **NOT PASSED**.
