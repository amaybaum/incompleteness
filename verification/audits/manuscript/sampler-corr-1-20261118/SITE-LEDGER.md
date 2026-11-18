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

## Correction against current main

The source and artifact comparison base is `34c4b4847863db3c8efad3b0cf33d442d4c08973`, which includes #1350. The initial inventory at `9a1207cfba9b6c79f40de44ef4b0142ec3a49d73` remains in the draft's ancestry. The sampler has first use of its shared manuscript paths per the coordination on #1385. This correction supplies the source for the later release handoff. The later release build and F72 wording have their own scopes.

| Location at the comparison base | Before | Correction and evidence |
| --- | --- | --- |
| Main:80, :558, :566 | The summaries refer to arbitrary finite accuracy without the supplied data in view. | State the fixed initial state and supplied data for the envelope and finite net. The law theorem and the separately stated operational-completion conditions keep their existing scope. |
| Main:568–570 | The initial density matrix is arbitrary but the grid construction is assigned to the instruments' entry ring. | Require a conjugation-closed working ring with the initial and all Kraus entries, exact operations and exact real trace comparisons. The one-step irrational-state control above exposes the missing input. The positive grid bound keeps its magnitude and hypotheses. |
| Main:578 | The capacity expression uses the instruments' ring and a reachable set without the initial state as an argument. | Index reachable matrix labels by the initial state and distinguish label capacity from arithmetic representation and comparison cost. The fixed-point capacity is separate from accuracy. Use a positive grid even for an instrument with a single outcome. |
| Main:578, upward rescaling in clause (5) | The parenthetical says the exact-ring variant adjoins $\tfrac12$. | The stated shift multiplies by $2^s$ for a nonnegative integer $s$. A ring containing $1$ already contains that integer. The trace comparisons are invariant under this positive scaling, and the stack restores the predecessor directly. Neither step requires halving. Check 10 of §3.4's cited probe tests a wider rescaling rule with a downward branch. That branch is outside the one-sided register construction. |
| Main:580 | The raw trace-norm estimate starts with zero initial error. | Sum the existing raw branch recurrence from its own initial error. Exact initial storage removes that term only. The positive-input clipping estimate stays restricted, and the bound for the actual sampled law on potentially indefinite registers remains open. #1307 and #945 track the respective proof obligations. |
| Main:582 | The proof describes exact conditional arithmetic in the instruments' ring. Its repeated raw estimate suppresses the input norm. | State the cumulative comparison of cross-multiplied exact weights and the rational-basis control. No division in the ring is required. Repeat the raw step bound with its input norm and retain the separate clipped-law obligation. |
| Main:584, :586 | The controlled program and gluing summary inherit the grid construction. | Carry the same initial data and accuracy regime into the program construction and the realization summary. The fixed instrument maps and separate memory charge for the program are preserved. |
| Main:600, :602, :604 | The continuum net and its density summary inherit the sampler even for an arbitrary initial state in the net instruments' ring alone. | Carry the initial state and exact access conditions into the grid and label count. For supplied real net conditionals, the existing intervention dilation gives the existence route, with the slot replacement bound and no register cost guarantee. State fixed initial data at each density comparison. With no slots the instrument record is empty. |
| Main:722, :776 | The application and concluding paragraphs invoke finite accuracy without saying what data the constructions consume. | State the finite response-table result with supplied conditionals and the finite-accuracy construction under its data conditions. |
| Substratum:533 | The summary invokes the gluing and finite-net results for finite adaptive experiments. | State the supplied-conditional finite-table result and the fixed initial state for accuracy across the finite instrument net. |
| Chapter 1:195, Chapter 4:146, Chapter 19:126 | Finite experimental envelopes are realizable at finite accuracy. | Specify supplied probabilities and scope instead of implying an unqualified sampler. Exact paragraph mirrors at FULL:530, :1254 and :5271. |
| Book README:17 | The finite-accuracy claim does not state its fixed preparation or data. | State finite response-table existence with supplied probabilities and finite-net accuracy at fixed initial state. The book README is outside the consolidated chapter mirror. |
| Glossary:107 | The gluing entry gives the grid and capacity estimates without the arithmetic conditions and describes the checks generically. | State both required data sets and exact comparison, distinguish labels and sampled-law error, and restrict the exact arithmetic checks to the finite examples. Exact paragraph mirror at FULL:6686. |

The response-table proof and the finite-horizon equivalence statement and proof in Main match the base. In the grid proof the total branch mass is positive at a positive-mass history. The first strict cumulative threshold selects among the nonnegative branch weights without dividing in the working ring. The irrational-state control concerns the exact weights and comparisons used by that sampler. The uniformly weighted finite seed grid approximates even a supported irrational law. The real-prior table can represent that law exactly.

The manuscript scan can be repeated from the repository root:

```sh
rg -ni 'entry[- ]ring|instruments?.{0,30}entr(y|ies) ring|exact ring ratios|true conditionals are computed exactly in the ring' README.md papers/*.md papers/*.tex book/*.md book/*.tex
rg -ni -o 'operational gluing|uniform[- ]continuum|quantum[- ]shadow|finite-test density|opglue.probes|clipped and normalized|rounding lemma' README.md papers/*.md book/*.md
python3 -B papers/oi_lattice_code/mirror_check.py
```

Read the resulting scope references in context. The previous unconditional entry-ring wording and the exact-ring ratios wording have no live source or TeX match. Historical research and review records retain their wording.

Pandoc 3.1.3 and native XeTeX 3.141592653-2.6-0.999996 (TeX Live 2025/dev/Debian) reproduced the three tracked baseline TeX files byte for byte from an isolated export of `34c4b484`. The same toolchain and the unchanged `sh ./build.sh Main Substratum` and `sh ./build.sh --book` commands regenerated the three affected TeX/PDF pairs from the reviewed sources. The generated TeX retains the baseline heading wrappers and labels. The build reported zero dropped glyphs. The PDFs contain the corrected passages in extracted text. Page counts were Main 104 to 105, Substratum 56 to 56 and FULL 565 to 565, with stable median text per page. All three TeX source stamps match. The coverage ledger refreshes the three affected statement entries at their existing evidence levels. SC-42 tracks four updated passage prefixes and regenerated receipts with the existing predicates and controls.

The independent review checks above apply to the pushed correction. A fresh review is required for a scientific change. Physical measurement sourcing remains **NOT PASSED**.
