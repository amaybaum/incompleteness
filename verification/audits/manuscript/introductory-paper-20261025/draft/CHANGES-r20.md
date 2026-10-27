# Introduction r20: the three gate reviews of r19 (`2afb5b6a`), on base `9a36ebeb`

r20 integrates three reviews of r19, together with the owner's three emphases of 2026-10-27:

- **gate 1, accuracy:** `scientific/GATE1-papers-2afb5b6a.md`;
- **gate 3, narrative:** `editorial/GATE3-papers-2afb5b6a.md`;
- **gate 2, comprehension:** `accessibility/RUN1-EVALUATION.md`, NOT MET because Q5 was only partly answered.

What did not change:

- No theorem or corollary statement changed.
- The §2.4 Corollary (L116) is byte-identical.
- The recurrence scope wording in the abstract (L17), the Corollary (L140) and §6 (L298) is r19's text.
- The census fingerprints are unchanged: 97ce3099c02498fb, a1abae061358524e, b596be8af06bd797, 67e2d2a4f01999ed, 603c7f6d12b01679 and 106e5e6806523955. Only the ledger `line` fields moved (65, 101, 116, 136, 140, 212). No ID was retired.

r20 stays on base `9a36ebeb`; reconciling it with `main` (now `0d917665`) is left to the coordinator. The accessibility
answers and the question sheet are untouched. Line numbers below are `papers/Introduction.md` at the r20 commit.

## 1. Required findings

| Finding | Change |
|---|---|
| G1-1, L238 (r19) quantifier | L238: "for any single finite pattern some finite hidden world reproduces it, but no one fixed finite hidden world reproduces everything one qubit can do across all possible experiments, which would need unlimited hidden memory." |
| G1-2, L238 (r19), H-Bell in full | L250: "…whether a coupling graph on the lattice substratum can supply that dependence without any usable signal and while keeping the gravitational continuum limit is open (H-Bell)." This matches L248 and Main §3.3. |
| G1-3 = G2-1, L130 (r19) | L130: "In a finite reversible world whose hidden part starts with the same odds whatever is visible at the start, any visible step that is not fully predictable from the current observation makes its failure, for the forecasts from every starting point, unavoidable somewhere in the world's cycle." |
| G2-2, why shared odds and why never-occurring rows | L134: one preparation defines every row and makes each row exactly the forecast the process gives from that start; the step from two histories to an overlap rests on that independence [Main §2.3]. Never-occurring rows are kept because the chain-breaking overlap can sit in such a row alone and the argument needs the full square table (Main §2.3, proof of the history-readback theorem: "possibly only through a row of a root of visible probability zero; the lemma applies to the square matrix") |
| G2-3, memoryless windows against memory before the return (owner point 1) | L144, first in plain words: what "memoryless on a window" means (M_t = 0 at every step inside it); hidden memory surfaces as conditional dependence at an order beyond the window but before the return; across the recurrence cycle it appears as the failure of chaining. Then the exact statement: the Corollary's full-support equivalence, quoted with its scope, plus the observation that a law Markov on accessible windows has M_k = 0 at accessible orders, so k lies beyond them (Main §2.3 Scope) |
| G2-4, both directions; storage against memory | L118: "Conversely, if any one hidden deterministic world reproducing the record keeps such a trace, the record has memory. Keeping the past is not the same as memory: every reversible world run from the start stores its whole visible past, even for a memoryless record, and memory is the part of that store that changes what is seen next." Sources: the §2.4 Corollary's converse; Main §1.5, "In a bijective realization run from time 0 the visible past is a function of (X_t, H_t)". The §6 Summary (L296) carries the converse too |
| G3-1, L112 (r19) rendered as a list item | L126 now begins "**Proofs and sources.** Part (b) and …"; it no longer renders as a list |
| G3-2, Theorem 4 scope (owner point 3) | L214, L200 and the Summary (L296) state Theorem 4's proved form: for an operational theory with the §3.2 structure on a nonempty finite system, the available operations on the system and at every finite helper level are exactly the normalized finite Kraus instruments if and only if (i)–(v) hold. "The rest of quantum mechanics" / "the whole of quantum mechanics" is removed at L37, L200 and L296. The abstract's r18 sentence ("Exact finite operational quantum mechanics is characterized by five completion conditions…") is unchanged |

## 2. Should-fix findings

- **Narrative order (G3-3).** Each subsection now runs question → picture → statement → plain reading → implications, and closes with a **Proofs and sources** paragraph. The moved blocks are listed in section 5.
- **§1.1 order (G3-5).** The order is now L23 → L25 → L27 → L29 → L31 → L33.
  - "Bijection" is defined (L29) before the formal triple uses it (L31).
  - r19's L27 is folded, verbatim, into L29 after the definitions.
- **§1.2 (G3-6).** L37 is recast as a plain roadmap, with its claims unchanged. The technical parenthetical moves to §2.5, L134 ("when the earlier matrix is invertible the unique candidate has a negative entry").
- **Intuition openers (G3-7):**
  - §2.3 L85;
  - §3.1 L184, which also defines quantum channel, completely positive, tracing out, diagonal state, populations and Hadamard;
  - §3.3 L224 (coherent lift, dilation, right action);
  - §3.4 L234 (ontic configurations, prepare-and-measure, behaviour matrix);
  - the §2.6 minimal-model and XOR one-liners (L154, L161);
  - the card-CP reading (L194);
  - the Page-curve plain reading (L292), which includes when H-scramble fails, isolation not being established, and the single-energy-shell condition failing for an evaporating black hole (GR App. A.7; BHb).
- **Abstract (G3-8).** One plain bridging sentence follows the opening question (L17): "every pattern of quantum records obtained by measuring one fixed way over a finite time can be produced by a partly hidden deterministic world, and any memory such records show must be stored in the hidden part of every such world." Every verified sentence is kept.
- **Terms defined at first use:**
  - in §2.1 (L49): Markov, realization, the order L, recurrence;
  - amplitude (L59);
  - coherence (L200);
  - wing and pre-setting variable (L242);
  - in §4's opener (L254), before first use: stress-energy, emergent, Hubble-scale density, de Sitter entropy;
  - quantum channel and Hadamard (L184);
  - energy shell, orbit ensemble, bipartition and measure concentration (L288).
- **Clarity:**
  - (a) L25: "After the unseen deal nothing random happens";
  - (b) L130: "If the weather had no memory, …";
  - (c) L112: "what the past reveals about the hidden state … at least as different odds on the hidden state";
  - (d) L180: the three reasons numbered (1)–(3);
  - (e) L286: "In some reversible worlds (1,376 of the 40,320 toy maps)".
- **Gate 1 optional:**
  - L142: "as happens at some time whenever a visible step is not fully predictable from the current observation";
  - L93: "not, in general, forever";
  - L242: "Bell's theorem tests directly …", replacing "the sharpest test";
  - L214: (v) is glossed as "a fresh, evenly mixed helper can be added to any combined system, used and discarded".
- **Gate 2 recommended.** L93 now says why Theorem 1 matters: no record of one repeated measurement can by itself rule out a partly hidden deterministic account, and the memory results apply to every such record. It keeps "possibility, not of fact" (L71).
- **Gate 2 should-land items.** The coupling-step plain reading of (C2) necessity is at L124. The other items are covered under the gate 3 entries above.
- **Voice.** Three self-assessment phrases are neutralized:
  - L27 "The idea matters because …" becomes "Put this way, …";
  - L242 "sharpest test" becomes "tests directly";
  - L296 "These results turn the opening question …" becomes "Each of these is a statement about …".
- **"In plain terms".** The 11 occurrences are now "That is" or "So"; 0 remain.

**Not applied:**

- Gate 1 optional 8 (L25) is superseded by gate 3 (a), which is applied.
- The Einstein–Born letter citation (gate 1, optional) is not added: "usually paraphrased" needs no source, and the letter was not read first-hand.

## 3. Four steps per topic (r20 lines)

| Topic | (i) Intuition | (ii) Explanation | (iii) Mathematics | (iv) Implications / open |
|---|---|---|---|---|
| Central idea | L23, L25 | L27, L29 | L31 | L33, L37 |
| Finite-horizon correspondence | L63 | L71, L73 | L53–L59, L65–L69, L75, L77; sources L79, L81 | L85–L93 |
| Memory results | L97 | L112, L118 | L99–L110, L114, L116, L120, L122; sources L126 | L124 |
| Recurrence and indivisibility | L130 | L134, L142, L144 | L132, L136–L140; sources L148, L150 | L144, L146 |
| Route to operational QM | L180, L184, L200 | L190, L194, L214, L230, L238 | L186–L196, L202–L212, L216, L226, L228, L236; sources L220 | L218, L180, open problems 1–2 (§6) |
| Bell | L242 | L246 | L244, L248 | L250 |
| Cosmological constant | L254 | L260 | L256, L258, L262–L266 | L268–L276 |
| Black-hole information | L280 | L286, L288 | L282, L284, L290 | L292, the §6 applications list (L310) |

## 4. The six comprehension points (QUESTION-SHEET questions 1–6)

| Question | Where answered (Level 1 or 2) |
|---|---|
| 1. The basic idea | L33 ("a part of a finite, reversible, deterministic world that sees only part of it … inaccessible to the observer, not merely unknown to it so far"); the situation is the card player, L23–L25 |
| 2. Randomness from hidden information | L25 ("After the unseen deal nothing random happens; the uncertainty is the player's …"); L29 ("hidden states compatible with the same visible state can send it to different futures") |
| 3. The main result; finite horizon | L17 (bridging sentence); L71 ("any pattern at all … possibility, not of fact"); L87 (Markov included); L93 ("over a chosen finite stretch of time, not, in general, forever"; why it matters) |
| 4. What it does not show | L180 (reasons (1)–(3)); L218 (the open completion conditions); L230 (the relating evolution); L296 |
| 5. Memory | L97; L118 (both directions; storage is not memory); L120 (hidden-size bound, least memory); L124 (no memory without readback; the coupling-step reading); recurrence: L130, L134 (why shared odds; why never-occurring rows), L142, L144 (memoryless windows against memory before the return) |
| 6. The two applications | §4: L254 (why it matters), L258/L260 (established: two levels), L262–L274 (the proposal, conditional on G3). §5: L280 (why it matters), L284/L286 (established: conservation is not recovery), L290/L292 (the Page curve on named conditions) |

## 5. Moved paragraphs: text unchanged

Each block was moved verbatim. The only additions are a run-in label in front of some blocks. The SHA-256 of each block
equals the SHA-256 of the r20 line with the label removed. Digests are the first 16 hex digits.

| Move | Label added | Block | SHA-256 at r19 | SHA-256 at r20, label removed |
|---|---|---|---|---|
| r19 L75 → r20 L79 | `**Proofs and sources.**` | Theorem 1 is machine-checked: the three inclusio… | add493450d2eebb2 | add493450d2eebb2 |
| r19 L83 → r20 L81 | (none) | **Attribution.** The trajectory-labelling realiz… | 6a2b78a22228052a | 6a2b78a22228052a |
| r19 L112 → r20 L126 | `**Proofs and sources.** Part` | (b) and the first inequality of (c) are data-pro… | d2844cca59e4bf4f | d2844cca59e4bf4f |
| r19 L138 → r20 L148 | `**Proofs and sources.** *Theorem 3.*` | Two such rows are at total-variation distance be… | 5726bd77250e3e10 | 5726bd77250e3e10 |
| r19 L146 → r20 L150 | `*The Corollary.*` | This is [Main §2.3, Theorem (history readback + … | 9643e76e4ba7c345 | 9643e76e4ba7c345 |
| r19 L210 → r20 L220 | `**Proofs and sources.**` | Both directions are machine-checked (Appendix A)… | ce4aefee0e87cc83 | ce4aefee0e87cc83 |

Also moved without change:

- the §2.2 picture (r19 L79 → r20 L73). Its first words, "The first construction", became "One construction", because it now precedes the Realization paragraph.
- r19 L27, folded verbatim into r20 L29.

## 6. Layout and checks

- **Length: 20 pages** at 11 pt with one-inch margins (r19: 18). This is over 18, within the brief's limit of about 20.
  The main text (§§1–6) ends on p. 18, followed by the code note and Appendix A on p. 18 and the references on pp. 18–20.
  The growth is the explanatory additions above.
- **Typesetting:** a direct compile gives 0 overfull, 0 underfull and 0 missing characters.
- **Renders checked:** p. 1, the abstract; p. 6, memory and the two directions; p. 7, §2.5's opener and the shared-odds paragraph; p. 18, the code note and Appendix A.
- **Checks:**
  - The release gate passes every step except `lean-axioms`. That step needs `lake`, which is missing here; it passes in CI.
  - `voice`, `claims`, `duplicate`, `coverage` (134), `staleness`, `mirror` and `architecture` all pass.
  - `edge_rigidity_probe`: ALL CHECKS PASS.
  - Appendix A: all 29 declarations resolve at their lines at `17b830bc` and at the head.
- **Added-lines scans:** no hits for the §A.32/§A.33 phrase families, caps emphasis, markers, secrets, scratch paths or model identifiers.
