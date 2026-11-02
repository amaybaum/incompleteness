# Introduction r19: the accessibility revision (against r18 + confirmation round at `61e8e140`)

r19 meets the owner's accessibility objective of 2026-10-27: the paper must be "accessible to a curious reader with no
physics background, while remaining rigorous enough for a professional physicist".

The method is to add explanatory text to the paper's own declarative voice. No verified statement is rewritten:
- every theorem and corollary, hypothesis, scope phrase and evidence-class label stays as confirmed at r18;
- the §2.4 Corollary paragraph (L118) is byte-identical;
- no coverage ID changes, and every fingerprint is unchanged (only the `line` fields move);
- the title is untouched.

The analogies are marked as analogies: the card picture at L23, the card table at L161 and the burned letter at L268.

Line numbers below are `papers/Introduction.md` at the r19 commit.

## 1. Owner items 1–8

| Item | Where |
|---|---|
| 1. Open with the question | Abstract L17 and §1.1 L23 open with it verbatim |
| 2. "God doesn't play dice; he plays cards"; illustrates, proves nothing | L23 introduces the analogy, says it proves nothing about QM, and says every result is proved without it; L25 is the two-card version; L161 states that the card game is an exact model, and an analogy as a picture of QM, because its statistics are classical |
| 3. The question before each formal result, a plain reading after | Theorem 1 L65/L73; Theorem 2 L97/L114; Corollary (memory) L120; Theorem 3 and the recurrence Corollary L130/L144; Theorem 4 L194/L208; Bell L230/L234; §4 L242/L248; §5 L268/L274 |
| 4. A concrete scenario before each result | hidden memory: the card face-down card (L97); measurement: the pre-drawn sequence (L79); chaining: weather forecasts and the card game (L130); Bell: two laboratories (L230); vacuum energy: field jitter (L242); black holes: the burned letter (L268) |
| 5. Every technical term defined at first use | bijection and visible marginal L33; law, stochastic matrix, permutation matrix, total variation and conditional mutual information L51; unitary and Born rule L61; Markov L99; hidden posterior L99; P-divisibility and root L134; quantum channel and Hadamard gate L186; ancilla and Kraus instrument L194; qubit L214; ontic parameter independence and measurement independence L236; Planck-scale cutoff L244; stress-energy L248; entanglement entropy and Page curve L276. CP-divisibility (L184), entanglement-breaking (L188), the pushforward (L49) and the spectator-independent readout (L198) were already defined |
| 6. Each section understandable on its own | each of §§2.2–2.5, 3, 3.2, 3.5, 4 and 5 opens with its own question and scenario and closes with its own plain reading; Main is cited for proofs only |
| 7. A clear closing summary | §6 opens with **Summary** (L282), followed by the established results, the conditional interpretations and the open problems |
| 8. Length | 18 pages at 11 pt with one-inch margins (r18: 15) |

**The "dice / cards" phrase.** The corpus does not use it: book §1.11 develops the card table and mentions Einstein's
hope that quantum probability would turn out to be ignorance, but does not quote him. The paper therefore writes
"Einstein's objection to quantum randomness is usually paraphrased as 'God does not play dice'". This is a statement
about the paraphrase, so no unread source is cited for it. "God plays cards" is the paper's own framing, marked at once
as an analogy.

## 2. The four steps for each topic (owner requirement 1)

Each topic runs (i) intuition → (ii) explanation → (iii) mathematics → (iv) implications in one continuous narrative.

| Topic | (i) Intuition | (ii) Explanation, and why it matters | (iii) Mathematics (exact, with evidence class) | (iv) Implications and open items |
|---|---|---|---|---|
| Central idea | L23, L25 | L27, L29 | L31, L33 | L35, L39 |
| Finite-horizon correspondence | L65 | L73, L79 | L55–L59, L67–L71, L75–L83 | L87–L93 |
| Memory results | L97 | L114, L120 | L99–L112, L116, L118, L122, L124 | L126 |
| Recurrence and indivisibility | L130 | L134, L144 | L132, L136–L146 | L148 |
| Route to operational QM and its limits | L178, L194 | L186, L208, L218, L226 | L182–L190, L198–L206, L210, L212, L220, L224 | L214, L178 (the three reasons), open problems 1–2 (§6) |
| Bell | L230 | L234 | L232 | L236, L238 |
| Cosmological constant | L242 | L248 | L244, L246, L250–L254 | L256–L264 |
| Black-hole information | L268 | L274, L276 | L270, L272, L278 | L278 (the named conditions), §6 applications list |

## 3. Comprehension points, matched to QUESTION-SHEET.md questions 1–6 (owner requirement 2)

| Sheet question | Where the paper answers it (Level 1 or 2) | Key-answer elements present |
|---|---|---|
| 1. The basic idea | L35: "a part of a finite, reversible, deterministic world that sees only part of it … the hidden sector is inaccessible to the observer, not merely unknown to it so far"; a situation: the card player, L23–L25 | partial description; inaccessible, not merely unknown |
| 2. Randomness from hidden information | L25 ("Nothing random happened; the uncertainty is the player's, and it comes from what the player cannot see"); L27 ("hidden states compatible with the same visible state can send it to different futures") | hidden states with the same visible state lead to different futures |
| 3. The main result; what "finite horizon" adds | L73 ("any pattern at all can be produced by a hidden deterministic world, and also by a quantum system measured the same way at every step … possibility, not of fact"); L87 (Markov laws included); L93 ("one such world reproduces a pattern over a chosen finite stretch of time, not forever") | three classes coincide on every finite horizon; Markov included, so this is a representation, not a test |
| 4. What it does not show | L178: fixed measurement only; selects nothing, neither the squared form nor the relating evolution; represents the statistics without deriving a mechanism; five conditions OI does not imply. Also L214 ("whether a physical substratum supplies the missing conditions is the central open question") and §6 L282 | fixed-basis only; completion conditions open; relating evolution not selected; Born exponent not derived; representation, not mechanism |
| 5. Memory | L97, L114, L120 ("the record has memory exactly when every hidden deterministic world that reproduces it keeps … a trace of the past that changes what is seen next"); L122 (hidden-sector size bound, least memory); L126 ("Coupling, persistence and capacity without readback produce no memory") | memory ⇔ readout-relevant hidden memory; lower bound on hidden size; coupling without readback gives zero memory |
| 6. The two applications | §4: L242 (why it matters), L246/L248 (established: two levels), L250–L262 (proposal conditional on G3). §5: L268 (why it matters), L272/L274 (established: conservation ≠ recovery), L278 (Page curve on named conditions) | the CC result is conditional on G3, not demonstrated; the BH distinction is established and the Page curve rests on named hypotheses |

Three passages were added for the sheet's key answers:
- "not merely unknown to it so far" (Q1, L35);
- the coupling-without-readback sentence (Q5, L126), from Main §2.3, Remark (why (C4) is a separate condition);
- the relating-evolution and mechanism clauses (Q4, L178).

## 4. Each new explanatory passage beside the exact statement it explains

Every passage restates nothing more strongly or more loosely than the exact statement next to it, and keeps each
hypothesis that matters.

| New passage (line) | Exact statement it sits beside (line) | Scope check |
|---|---|---|
| L23 question, dice and cards (analogy) | — (motivation) | marked as an analogy; "proves nothing about quantum mechanics" |
| L25 two-card version | card table, L161–L172 | 1/2 after one shuffle and certainty after two, as in the table; classical statistics stated |
| L29 why the idea matters | — | poses questions; claims nothing |
| L33 bijection and visible marginal | L31 | definitions |
| L35 added clause "a part of … sees only part of it" | L35 | restates the hypothesis; "not merely unknown so far" is the meaning of "inaccessible" |
| L51 vocabulary | L49 | TV equals the maximum event difference; CMI is zero exactly at conditional independence |
| L61 informal reading of S, D, Q | L57–L59 | "measured in the same way at every step" keeps the fixed basis |
| L65 / L73 | Theorem 1, L67–L71 | "over any fixed number of steps"; Q to D stated; "possibility, not of fact" |
| L79 picture of the realization | L77 | the pre-drawn sequence and clock as in L77; a bijection |
| L93 implications | L87–L91 | finite stretch of time, as in L91 |
| L97 memory scenario | Theorem 2, L101–L110 | "every hidden deterministic world that reproduces a record" means a faithful realization |
| L99 added glosses of M_t, Markov and the posterior | L99 | Markov ⇔ M_t = 0 at every t |
| L114 plain reading of (a)–(c) | L103–L110 | "at least as differently prepared" is (b); "never exceeds … capacity" is (c) |
| L120 | Corollary, L118 (byte-identical) | the same "exactly when" |
| L126 checklist; no memory without readback; what memory establishes | L124; Main §2.3, Remark (why (C4) is a separate condition) | the conditions are diagnostics; memory separates laws with memory from memoryless ones |
| L130 chaining scenario | L132–L134 definition; L142 | failure "unavoidable somewhere in the world's cycle" only "with any visible step that is not fully predictable" |
| L134 P-divisibility in words; root | L132 | definitions |
| L144 plain reading | Corollary, L142 | keeps the same starting odds (hidden prior shared and independent), rows for starting points that never occur, the return, any non-deterministic step, and the full-support equivalence |
| L161 added sentence | the card table | an exact model, and an analogy for QM |
| L178 §3 opening | §§3.1–3.5 | three reasons, each a stated result (L87–L89, §3.3, Theorem 4 independence) |
| L186 | L184 | the Hadamard example as at L184 |
| L194 | L196–L206 | definitions |
| L208 | Theorem 4, L206 | each of (i)–(v) paraphrased; "exactly … no more and no less" is the iff |
| L214 | L212 | independence and `oi_alone_not_qm`; "imply" as at L212 |
| L218 added clause | L218 | the same non-selection |
| L226 | L224 | "unlimited hidden memory" is "classical memory unbounded over finite experiments" |
| L230 Bell scenario | L232 | the standard CHSH bound; the quantum value 2√2 as at L232 |
| L234 | L232 | keeps no influence within the experiment's time (ii, iii), independent settings (iv) and an outcome in every run |
| L236 added definitions | L236 | definitions |
| L238 | L236 | "one or the other", as at L236; the framework's choice and the no-signalling requirement; H-Bell open |
| L242 | §4 | the jitter of the vacuum energy; why the question matters |
| L244 added gloss | L244 | definition |
| L248 | L246, L250–L262 | the two levels established; "gravity responds only to the underlying world" is labelled the proposal; G3 named |
| L268 added analogy and why it matters | L268 | marked as an analogy |
| L274 | L272 | "possible only when the unread registers have at least as many joint values" is the floor; "many reversible worlds" is the 1,376 |
| L276 | L278 | definitions; "if the information comes out" |
| L282 Summary | L284–L290 | the recurrence sentence keeps the starting odds (shared, independent hidden prior) and any unpredictable step; the substratum is "not shown to meet" the five conditions; the applications are conditional |

**Verified statements unchanged.** T-1 (L67), T-2 (L101), T-3 (L136), the recurrence Corollary (L142), T-4 (L206), the
§2.4 Corollary (L118), and the abstract's, §2.5's and §6's scope wording keep their r18 text. The census fingerprints are
identical: 97ce3099c02498fb, a1abae061358524e, b596be8af06bd797, 67e2d2a4f01999ed, 603c7f6d12b01679 and
106e5e6806523955. Only the ledger `line` fields move (67, 101, 118, 136, 142, 206).

One existing sentence was reworded, at L214, after a guard flagged it. The `architecture_check` invariant reserves
"yield quantum mechanics" for embedding statements, so "do not by themselves yield quantum mechanics" became "… imply
quantum mechanics", matching L212's "does not imply".

## 5. Layout and checks

- **Build:** `sh ./build.sh Introduction` gives 18 pages at 11 pt with one-inch margins. Median line length is 96 characters, and there are about 3,100 non-space characters per page. The main text (§§1–6) ends on p. 16. Appendix A is set in `\footnotesize` with 1pt paragraph skip, like the references, to hold 18 pages.
- **Boxes and glyphs:** a direct compile gives 0 overfull, 0 underfull and 0 missing characters.
- **Spot-checked renders:**
  - p. 1 and p. 2: the opening question, the analogy and the model;
  - p. 8: the end of the recurrence argument, the Γ matrices and the card table;
  - p. 16: the open problems, the code note and Appendix A.
- **Release gate:** every step passes except `lean-axioms`, which needs `lake` and cannot run locally; it passes in CI.
- **Other checks:**
  - `architecture` passes after the L214 rewording.
  - `voice`, `claims`, `duplicate`, `coverage` (134), `staleness` and `mirror` all pass.
  - `edge_rigidity_probe`: ALL CHECKS PASS.
  - Appendix A: all 29 declarations resolve at their stated lines at `17b830bc` and at the head.
- **Added-lines scans:** no caps emphasis, no reader instruction ("the reader", "note that"), no markers and no secrets. The words "now" and "no longer" occur only inside the card-game narration ("the colour now showing", "no longer shows it"), describing the game, not the document's history.
- **Records:** `review/accessibility/QUESTION-SHEET.md`, the owner-approved comprehension sheet, is included unchanged and added to `SHA256SUMS`.
