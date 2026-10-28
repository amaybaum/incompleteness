# Independent evaluation of frozen r32-v1 reader answers

**Gate NOT MET.** Eleven graded items PASS; Q9 is PARTIAL because the answer omits the required **uniform** preparation measure. Q7 is diagnostic. This applies only to cc04/r32-v1 and does not erase historical r31 verdicts or judge a future corrected PDF.

Paper under test: candidate `cc04e3f694932f58f9839e83827e561a9567ce55`, PDF SHA256 `ad559f3134473f045ef9ded503f27d2d10066afbe115e9aae37d13def4f74edc`, 24 pages. Protocol and questions were prospectively present in that candidate. Complete answers were captured by the separate reader before the coordinator authorized this evaluator to see them. The answer bytes, protocol, question sheet, original input manifest and all digests are retained beside this evaluation. Reader freshness/isolation are coordinator/reader provenance; I am an evaluator of those recorded answers, not a fresh reader or an independent reconstruction of its tool history.

The criteria applied are exactly `READER-PROTOCOL-r32-v1.md`, including its explicit inherited historical criteria. No author explanation, intended-answer supplement, response repair or retrospective criterion relaxation was used. I fixed the source-review findings before accessing these answers.

| Item | Verdict | Evidence and criterion |
|---|---|---|
| Q1 | PASS | Describes a finite reversible world with partial instantaneous readout; explicitly says this need not prevent inference from earlier observations. No permanent-opacity claim. |
| Q2 | PASS | Fair independent hidden card determines the swap outcome but is not observed; randomness arises from the hidden preparation, not the subsequent deterministic rule. |
| Q3 | PASS | Gives equality of finite stochastic laws, reversible hidden realizations and fixed-basis quantum records; includes Markov laws, the per-law/per-horizon construction, and the all-time recurrence obstruction. |
| Q4 | PASS | Separates representability from mechanism, incompatible/composite operations, unproved completion assumptions, Born exponent and nonselected relating evolution. Also preserves Bell and fixed-finite-qubit limitations. |
| Q5 | PASS | Defines next-step history dependence at a common present; requires hidden information in every realization, gives the TV/information/capacity bounds, distinguishes storage from readback and denies permanent-opacity inference. |
| Q6 | PASS | Keeps emergent zero-point energy separate from gravitational source, leaves field equations/coupling and Lambda value open; separates conservation from recovery, recognizes the configuration-state no-instance obstruction and lists missing physical Page ingredients. |
| Q5a | PASS | Explains why changing the hidden setup changes the experiment and can account for forecast differences, rather than revealing one rule started differently. |
| Q5b | PASS | Distinguishes an unobserved but well-defined possible start from actual samples, explains whole-table return/overlap and that the obstruction may come only from an unused row. Explicitly places full support on the actual-law memory equivalence. |
| Q5c | PASS | Explains whole-cycle versus short accessible windows, a delayed trace that changes no obtainable pre-effect record, and the watched-step contrast. The stated-hypothesis reference is resolved by Q5a's common preparation and Q5b's full-support qualification; the complete recorded answer preserves both. |
| Q8 | PASS | Two retained swap readings identify both cards despite predictive memory; known preparation/model/record determines the compatible-state set and constancy criterion. A retained observed record supplies compatible candidates; no claim is made about inference from an empty or impossible fibre. Embedding alone does not decide inferability. |
| Q9 | PARTIAL | Correct coherent seed, sampled binary map, fixed state/cuts, actual clocked release, written proof/exact controls, return and physical limits; omits that the map/subspace ensemble is sampled **uniformly**, which the prospective rubric explicitly requires. |
| Q10 | PASS | Distinguishes all finite blocks/all times from literal infinite-tail certification; gives a lower bound on hidden capacity and rejects permanent uncertainty. |

## Q9: exact omission and diagnosis

The protocol requires: “Q9 PASS requires stipulated coherent preparation and **uniform invertible-binary ensemble**”. It explicitly assigns PARTIAL to omitting a scope premise without overclaiming.

The reader says: “It then samples an invertible binary linear map, whose reversible permutation produces a coherent uniform state on a subspace.” These are two different uniformities. A uniform amplitude within a chosen subspace does **not** say the subspace/map is sampled uniformly across the ensemble. The answer later refers to ensemble means, but does not specify that measure anywhere. I cannot fill that omission from the author's source or infer it from the word “samples”.

The paper itself states the premise plainly in §5: “choose one uniformly random invertible binary linear map”, followed by “a uniformly chosen k-dimensional subspace”. Thus this is neither an ambiguous source sentence nor a missing explanatory premise. It is a scope-premise reconstruction/retention gap in this recorded answer. Under the protocol's inherited three-way taxonomy it belongs to conceptual reconstruction, without establishing that the reader has a deeper substantive misunderstanding. No false physical/Lean/Haar claim appears. The narrow disposition is PARTIAL, not FAIL.

There is no additional required scientific rewrite inferred from this answer: the premise is already explicit. Any new test must remain fresh, paper-only and prospectively pinned; the present answers cannot be supplemented to turn this run into a PASS.

## Q5(c): why it passes

The recorded answer gives the necessary reason, not merely the conclusion: a hidden trace may affect visible output only after every available window ends, so it appears in none of the accessible records. It explicitly contrasts the case “If the observer reaches and retains that step, it can witness the dependence.” Whole-cycle scope and lack of a guaranteed early location are present. Q5a supplies the shared preparation, and Q5b explicitly states “The paper adds a full-support qualification when equating whole-cycle failure with conditional memory in the actual law.” This is evaluating the complete answer's ordinary-language understanding, not waiving a missing hypothesis.

## Diagnostic Q7 and separate source defect

Q7 reports difficulty reconstructing the operational-completion independence arguments and identifies gravitational source selection and physical realization of the entropy example as the main uncertainties. It does not claim to have verified those proofs and does not confuse their open physical status. Q7 has no gate threshold.

Separately, the frozen source review requires correcting §1.2's blanket old Lean pin. That provenance defect is independent of this comprehension result. Correcting it does not retroactively make this run pass, and a comprehension PASS would not excuse the source defect. Neither verdict constitutes integrated CI, physical acceptance, release or merge approval.
