## Review of PR #956 at head `533cdeb2`, base `55e3217b`

**Verdict: ACCEPT WITH CHANGES.** Three changes are required (findings 1–3). They concern the third result in Medicine :25 and one scope phrase in Explainer :707. The rest of the PR is supported, consistent across sites and mirrored correctly.

**Setup.** Disk had 23 GB free. I made a detached worktree at `533cdeb2`. Before the head, `papers/Main.md` is identical to base, so all source line numbers are base lines. The worktree has been removed.

### Answers to the two questions
- **(a) Is every substantive claim supported by its stated evidence and assumptions?** Almost every one. The exceptions are all in the third result of Medicine :25 and in Explainer :707:
  - "the visible process" in Medicine should be "the rooted visible family".
  - Medicine drops the shared-hidden-prior hypothesis, which defines the rooted maps.
  - "Markov laws as well" drops Main's qualifier "Markov on every accessible window".
  - "registers as memory" folds the indivisibility into memory and drops the full-support condition.
  - Explainer :707's "the quantum algorithm … whatever the law" goes beyond what the fixed-basis equivalence supports.
- **(b) Is any established result unnecessarily weakened?** No serious weakening. Medicine gives only the forward half of the memory biconditional, which Main §3.4 :596(2) and :608 list as a maximum-strength result. It also states only "M_t = 0" where Main :172 proves zero conditional past–future information I(X_{<t};X_{>t}|X_t) at every time. Both are optional fixes (findings 4 and 5).

### Per-clause check, Medicine :25
- **(a) "C4 holds exactly when M_t > 0 at some accessible time".** Supported. This is Main's abstract (:20) verbatim, and Main :99, :608 and :612 support it; the mediation clause is automatic in any faithful realization (:612). Two hypotheses are implicit: positive-probability histories and a finite horizon K ≥ t+1. Main carries two caveats that Medicine drops:
  - the vanishing criterion for conditional mutual information is not formalized (:99, :596);
  - reading a realization's time-t law as the kernel's joint law is not formalized (:99, :604).
  
  Both are verification-layer caveats, not hypotheses, and Medicine makes no kernel claim, so dropping them is acceptable.
- **(b) "every faithful deterministic realization … carries readout-relevant hidden predictive memory".** Supported by Main :598–:608 (`unavoidable_hidden_predictive_memory`, `pushforward_identity`, `distinguishability_floor` in `OIBridge/HiddenMemory.lean`; all exist). Main says "at t", which Medicine omits. The converse is also omitted.
- **(c) Readback bound M_k ≥ p_0δ²/ln 2.** Hypotheses match Main :167 exactly: two distinct length-k histories, a common present c, each with Pr[X_{<k}=p, X_k=c] ≥ p_0, next-step laws at total-variation distance ≥ δ. The units (bits) are left implicit.
- **(d) "coupling, persistence and capacity without readback admit realizations with M_t = 0".** True (Main :172, :80). As worded it is near-tautological, because the preceding sentence already makes "without readback" equivalent to M_t = 0. The content Main proves is that C1–C3 do not imply C4, and the zero it proves is stronger.
- **(e) Recurrence-cycle P-indivisibility clause.** Partly unsupported; see findings 1–3.
- **(f) Universality and (T).** "Universal, Markov laws included" matches Main :20, :99 and :550. Medicine now omits (T) and the compressed form entirely. Every propagated site keeps them, which is acceptable because that form is imported and conditional.
- **(g) New C4 entry (Medicine :33).** Faithful to Main :80. Main §2.3's "positive-probability" is absent here, as it is from Main :80 itself.

### Findings

1. **Required. Medicine :25, third result: missing hypothesis and wrong object.**
   - *Current:* "on one fixed finite reversible realization the visible process is P-indivisible somewhere in its recurrence cycle whenever some rooted visible map is not a permutation".
   - *Problem:* Main's theorem (:137) assumes a hidden prior μ_H shared by every root and drawn independently of the root. It defines P-divisibility for the rooted family Γ_t, rows for zero-probability roots included. In Main §3.4 (:99, :598) a "realization" may correlate the hidden and visible initial coordinates. Under such a law the rooted maps are undefined at zero-probability roots.
   - *Why it matters:* Main :141 notes that a non-permutation row may belong to an unrealized root while the realized law has no gap. So "the visible process" names the wrong object.
   - *Replace with:* "on one fixed finite reversible representative, with a hidden prior shared by every root and drawn independently of it, the rooted visible family is P-indivisible somewhere in its recurrence cycle whenever some rooted visible map is not a permutation".

2. **Required. Medicine :25: "so recurrence-scale indivisibility occurs in Markov laws as well".**
   - *Problem:* Main's qualifier is "laws that are Markov on every accessible window" (:20, :82, :141). Under the full-support prior named in the preceding clause, a law that is Markov over the whole cycle makes every Γ_s a permutation (:141, the "Without a gap below L" step). So the unqualified phrase contradicts the clause before it, and it holds only through zero-probability roots.
   - *Replace with:* "so recurrence-scale indivisibility occurs also in laws that are Markov on every accessible window".

3. **Required. Medicine :25: "it registers as memory on accessible timescales only when that order is accessible, which recurrence does not guarantee and C4 asserts".**
   - *Problem:* "It" is the indivisibility, which this sentence turns into memory. The equivalence to memory holds only with a full-support prior, so the sentence inherits a condition it does not state. "That order" has no antecedent in its own sentence.
   - *Source:* Main :141 ("on them the memory is witnessed only by a gap at an accessible order") and :153 (accessible memory does not make the rooted family P-indivisible on those windows).
   - *Replace with:* "Under a full-support prior the memory obstruction it is equivalent to may lie at any order below the recurrence time; accessible statistics witness it only through a readback gap at an accessible order, which recurrence does not guarantee and C4 asserts."
   - This keeps "backflow" unused, as the owner rule requires.

4. **Optional. Medicine :25, second result: state the biconditional and the time.**
   - *Current:* "…every faithful deterministic realization of such a law then carries readout-relevant hidden predictive memory".
   - *Replace with:* "…carries readout-relevant hidden predictive memory at that time, and conversely such memory in any one faithful realization forces M_t > 0" (Main :596(2), :608).

5. **Optional. Medicine :25: the C1–C3 separation clause.**
   - *Replace with:* "coupling, persistence and capacity do not imply readback: they admit realizations whose visible law has I(X_{<t};X_{>t}|X_t) = 0 at every time on arbitrarily long accessible horizons [1, §2.3]".
   - This removes the tautology and states the stronger zero Main :172 proves. Adding "(in bits)" after the readback bound would also help.

6. **Optional. Medicine :25, first result: name the representing object.**
   - *Current:* "a unitary system read out by Born-rule measurement in one fixed basis".
   - *Problem:* Main :546 also specifies "measured projectively in that basis at every step from an initial state diagonal in it". Without that, a reader may take it for a coherent representation.
   - "Markov laws are included, so the representation is universal" reverses the inference. Main's form is "it is universal, Markov laws included, so representability alone does not distinguish…".

7. **Required (scope). Explainer :707.**
   - *Current:* "so the quantum algorithm for prediction is available whatever the law".
   - *Problem:* What Main proves is a fixed-basis unitary/Born representation of the fixed-basis record (:546). Main declines operational quantum mechanics entire (:20, :550), as Explainer :948 itself says. Yet the next paragraph (:709) attributes interference and entanglement to "the algorithm", and a permutation unitary acting on diagonal states produces neither.
   - *Replace with:* "so a fixed-basis unitary/Born algorithm reproduces those statistics whatever the law".
   - The per-order biconditional that follows is supported: a gap at order k implies M_k > 0 by the readback lemma (:167), and the converse holds by the vanishing criterion (:99).

8. **Optional. Complexity :27.**
   - The PR edited the parenthetical "(coupling, slow bath, sufficient capacity, history readback)". Under Main :76, C2 is memory persistence and a slow bath is only one mechanism; make it "record persistence", matching Methodology :107.
   - "in a deterministic system" should read "in a finite deterministic system", since the representation is a finite-law result.
   - The rest is faithful.

9. **Optional (missed residual). Explainer :856.** "the universal representation ([Main §3.4]) supplies every such observer's self-consistent quantum description, under (T)" attaches the internal universal representation to (T). This is the pattern the PR corrects elsewhere.
   - *Replace with:* "the universal fixed-basis representation ([Main §3.4]) is internal, its compressed form under (T)".
   - The "self-consistent quantum description" there also leans on the unresolved operational-lifting question, which predates this PR.

10. **Optional (outside the hunks, same paragraph block).** These lines predate the PR, but Medicine's restated conditions list now sits beside the new text:
    - Medicine :27 builds "bidirectional interactions" into C1; Main :74 says bidirectionality is a realization property, not C1's content.
    - Medicine :31 builds "many more accessible states" into C3; Main :78 says that hierarchy belongs to the realization clause.
    - Medicine :35 says history-dependence strength is "controlled by τ_S/τ_B"; Main :76 has a fast shift-register bath giving a maximal gap.

### Propagated sites
- **Explainer :294.** Faithful (Main :524, :530, :624). "Holds across its recurrence cycle" is Main's own phrasing (:153).
- **Explainer :948.** Faithful.
- **Methodology :110.** Faithful.
- **Complexity :27.** Faithful apart from finding 8.
- **ch00 :59 / FULL :295.** Faithful. "Conditional memory" is used per notion.
- **ch05 :11 / FULL :1340.** Faithful.
- **ch14 :107 / FULL :3785.** Faithful: C4 alone suffices, and the readback gap is named.
- **ch19 :28 / FULL :5188.** Faithful.

All sites keep the three notions apart: conditional memory (M_t, factorization), P-indivisibility, and representation. No added line uses "backflow" or "revival". All sites are consistent with Medicine once findings 1–3 are applied.

### Mirrors and residuals
- **Mirrors.** The added and deleted line sets of the four chapters are byte-identical to FULL's hunks, and `mirror_check` passes.
- **Residual grep.** No remaining "necessarily non-Markovian / memory-bearing / quantum" in `papers/`, `book/` or the repo's other .md/.tex files, nor any "quantum for processes in the correspondence's class". The surviving hits are correctly scoped: FULL :5863 and appendix-b :96 ("the C1–C4/readback sector is necessarily memory-bearing") and ch05 :11 ("under conditions C1–C4 must use a memory-bearing formalism").
- **Representation conditioned on (T).** The only residual is Explainer :856 (finding 9). Every other "under (T)" hit attaches only to the compressed form.

### Voice
The papers' added lines pass §A.32/§A.33: no caps emphasis, no revision-history or reader-instruction phrases. The gate's `voice` and `claims` steps pass.

### Gate and builds
- `python3 tools/release_gate.py` passed 21 of 22 steps. The only failure is `lean-axioms`, expected without lake.
- For Medicine, Explainer, Methodology, Complexity and FULL, the committed .tex matches a fresh pandoc regeneration apart from the `source-sha256` stamp, and every stamp equals the source .md's sha256.
- The committed PDFs contain the new text. Page counts are plausible: 30, 69, 54, 35 and 557.
- The book chapters have no separate artifacts; only FULL is built, and it is rebuilt.
- CI on the head was still queued when checked.
