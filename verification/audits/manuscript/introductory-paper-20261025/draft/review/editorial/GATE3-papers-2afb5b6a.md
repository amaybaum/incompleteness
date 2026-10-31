## Narrative-quality review (gate 3) of #918 r19 at `2afb5b6a`

**Verdict: ACCEPT WITH CHANGES.** The four steps (intuition, explanation, mathematics, implications) are present for most topics. Two things stop it reading as one continuous narrative:
- Proof-status and attribution paragraphs sit in the middle of each topic.
- Four places have no intuition step at all: §1.2, §3.1, §3.3–3.4, and the Page curve.

There is also one must-fix layout defect, one must-fix overstatement in the Summary, and four further misleading simplifications.

I worked read-only: no edits, commits, pushes or comments. My worktree has been removed. Line numbers are `papers/Introduction.md` at `2afb5b6a`.

### Build
- **Result:** `sh ./build.sh Introduction` gives 18 pages at 11 pt with one-inch margins. The `.tex` is identical to the committed one.
- **Density:** median 3,118 non-space characters per page.
- **Boxes and glyphs:** 0 overfull, 0 underfull, 0 missing characters.
- **Page map:** the main text ends on p16; Appendix A is on p16 and the references on pp17–18.
- **Renders checked:** pp1–2 (opening), pp5 and 7 (theorems), pp15 and 17 (summary and references).
  - The [Sti55] C\* entry is now fixed.
  - One layout defect, finding 1.
- **Citations:** 52 entries, every key resolves, no orphans. r19 adds no new citations.

### Must-fix

1. **L112 renders as a list item.** The paragraph begins "(b) and the first inequality of (c) are data-processing inequalities." Pandoc reads "(b) " as an ordered-list marker, so on p5 the paragraph is typeset as an indented list item labelled (b) under Theorem 2.
   - The line came in at r17; I missed it in the r17 and r18 checks.
   - Fix: "Part (b) and the first inequality of (c) are data-processing inequalities."

2. **L282 Summary overstates Theorem 4.**
   - Current: "The rest of quantum mechanics, incompatible measurements and combined systems, follows exactly when five stated conditions hold".
   - Problem: Theorem 4 characterizes the available operations (finite Kraus instruments) of an operational theory with the stated structure, on a finite system. It does not deliver "the rest of quantum mechanics".
   - Proposed: "On a finite system, the full set of quantum operations, incompatible measurements and combined systems included, is obtained exactly when five stated conditions hold".
   - Related at L208: replace "…exactly what makes the available operations those of quantum mechanics" with "…exactly what makes the available operations of a theory with the structure above those of quantum mechanics".

### Narrative (gate 3)

3. **The flow alternates between expert and beginner paragraphs** (should-fix). Within each topic, proof-status and attribution paragraphs interrupt the steps. Examples:
   - §2.2: question (L65) → Theorem 1 → plain reading (L73) → machine-check note (L75) → expert Realization paragraph (L77) → picture of the realization (L79) → L81 → Attribution (L83).
   - §2.4: L112 and L118 sit between Theorem 2's plain reading and the memory implications.
   - §2.5: L138 and L146 do the same around the Corollary.
   - Proposal: per subsection, run question → picture → statement → plain reading → implications, then close with one paragraph labelled "Proofs and sources" holding the evidence classes and attributions.
     - In §2.2, L79's picture should come before L77.
     - Moving paragraphs changes no text, and the L118 Corollary stays byte-identical.
   - This is the main thing standing between the current text and "one continuous narrative".

4. **"In plain terms" is used 11 times, plus "In words" twice** (optional). The label is formulaic. Where the reading follows directly from its setup, "So…" or "That is…" reads as continuous prose.

5. **§1.1 order** (should-fix).
   - "Bijection" is used at L27 and L31 but defined at L33.
   - L27 restates L25.
   - Proposed order: L23, L25, L29, then L33's definitions, then L31 (the formal triple), then L35. Drop L27 or fold it into L33.

6. **§1.2 (L39) is an expert-only paragraph** between the lay opening and §2 (should-fix).
   - It uses "stochastic map", "transition matrix", "invertible", "negative entry" and "stochastic–quantum correspondence" before any of them is defined (L51 onwards), and largely repeats the abstract.
   - Recast it in the paper's explanatory register as a roadmap. For example: "Hiding part of a reversible world can make what is seen random, give it memory, and make its probabilities impossible to chain step by step; §2.2 shows every such pattern arises this way, and §§2.4–2.5 show what the hidden part must then contain…". Keep the technical parenthetical for §2.5.

7. **Steps missing for some topics** (should-fix). CHANGES-r19's table omits §3.1, §3.3 and §3.4, and these have no intuition step.
   - §3.1 (L182–L190): only L186 is accessible. "Completely positive", "trace out", "diagonal hidden state" and "population" are undefined, and the card CP paragraph (L188: Pauli twirl, entanglement-breaking) is expert-only. Proposed opener: "A record can have memory, can fail to chain, or can carry quantum memory; the three can occur separately."
   - §3.3 (L218–L220): "coherent lifts", "unitary dilations" and "right action" are undefined. Proposed opener: "Two different quantum mechanisms can produce identical records at every time, so the records alone cannot tell which evolution connects two moments."
   - §3.4: needs an opener before L224 that defines "ontic configurations", "behaviour matrices" and "prepare-and-measure". Proposed: "A finite hidden world has finitely many states, while a single qubit can be prepared and measured in infinitely many ways."
   - §2.6: the minimal model and the XOR example lack a one-line intuition. For XOR: "the last bit is the parity of the first two: neither earlier bit alone predicts it, both together determine it".
   - Page curve (L278): there is no plain reading or implication after the paragraph. Proposed: "If the hidden dynamics scrambles thoroughly and the black hole is effectively isolated, the radiation's entanglement follows Page's rise and fall on average; the simplest bijective models fail the first condition, and the second is not established."

8. **The abstract is unchanged and expert-only after its opening question** (should-fix, under the owner's objective). Keep the verified scoped sentences and add one plain bridging sentence after the question. For example: "In plain terms, every pattern of fixed-measurement quantum records over a finite time can be produced by a partly hidden deterministic world, and any memory such records show must be stored in the hidden part."

9. **Self-containedness without Main.**
   - The topics that open and close in plain language can be followed without Main: §§2.2, 2.4, 2.5, 3.2, 3.5, 4 and §5's toy model.
   - Several cannot: §3.1, §3.3, §3.4, the (C2) paragraph (L124: coupling-step model, slow-bath form) and the Page-curve paragraph.

### Terms not defined at first use (should-fix, beyond finding 7)
- **Markov:** used at L17 and L87, defined at L99. Define it in §2.1's vocabulary (L51).
- **Stochastic map and transition matrix:** L39, before L51.
- **Emergent** ("emergent quantum description", "emergent Hamiltonian", L246–L254): never defined, although it is a key term. Gloss: "the quantum description of the visible statistics".
- **Realization:** used from L49; only "faithful realization" is defined (L43). Add the plain gloss "a hidden deterministic world reproducing the law".
- **Order L of a bijection** (L91): "the number of steps after which every configuration has returned".
- **Amplitude** (L61).
- **Coherence** ("never creates coherence", L212).
- **Wing** and **pre-setting variable** (L232): "wing" is the paper's word for a laboratory.
- **Stress-energy:** used at L246, defined at L248.
- **Quantum channel and Hadamard gate:** used at L184, defined at L186.
- **De Sitter entropy and Hubble-scale density** (L244).
- **Energy shell, orbit ensemble, bipartition and measure concentration** (L278).
- **Already defined well:** P-divisibility (L130/L132/L134), conditional mutual information (L51), total variation (L49/L51), stochastic and permutation matrix (L51), unitary and Born rule (L61), ontic parameter and measurement independence (L236), ancilla and Kraus instrument (L194), qubit (L214).

### The five worst clarity defects
Beyond finding 2:

- **(a) L25, "Nothing random happened".** The face-down card was dealt at random and unseen. The uncertainty comes from that unseen initial deal combined with deterministic rules, which is the paper's central idea. Proposed: "After the unseen deal nothing random happens; the uncertainty is the player's, and it comes from what the player cannot see."
- **(b) L130, the weather analogy and its conclusion.**
  - "A weather forecast from Monday to Wednesday can be built from one from Monday to Tuesday and one from Tuesday to Wednesday" is asserted as fact, but it holds only for weather without memory, which is the very point at issue.
  - The final clause also drops the shared hidden prior.
  - Proposed: "If the weather had no memory, a forecast from Monday to Wednesday could be built from…" and "…in a finite reversible world whose hidden part starts with the same odds whatever is visible, with any visible step that is not fully predictable, its failure is unavoidable somewhere in the world's cycle."
- **(c) L114, plain reading of Theorem 2.** "depends on the past only through what the hidden state holds" confuses the hidden state with the posterior. Proposed: "…only through what the past reveals about the hidden state (a); two pasts can lead to different predictions only if they leave at least as different odds on the hidden state (b)".
- **(d) L178, the "three reasons" list is hard to follow.** The second reason swallows two further clauses through "and" and semicolons. Proposed: "(1) it covers only records of one fixed measurement repeated at every step; (2) it holds for every law, so it selects neither the squared form of quantum probabilities nor the evolution relating two times (§3.3), and it represents the statistics without deriving a mechanism; (3) the further ingredients are five conditions that OI does not imply (§3.2)."
- **(e) L274, "In many reversible worlds".** The supporting count is 1,376 of 40,320 in the smallest class. Proposed: "In some reversible worlds (1,376 of the 40,320 smallest ones)…".

Also hard to follow, though accurate: L124 (the (C2) paragraph), L198 (operational-theory setup), L232 (Bell assumptions) and L284 (the established-results sentence).

### Owner items 1–8
- **1. Opening question:** done (L17, L23). The abstract and §1.1 open with the identical sentence; optional to vary.
- **2. Card analogy:** early and marked as an analogy (L23, L25, L161). Good.
- **3. Explained before, read in plain language after:** yes for Theorems 1–4, the Corollaries, Bell, §4 and §5's toy model. Missing as in finding 7.
- **4. Examples throughout:** yes (cards, the pre-drawn sequence, weather, two laboratories, vacuum jitter, the burned letter).
- **5. Terms defined at first use:** largely yes; exceptions are listed above.
- **6. Each section stands alone:** see finding 9.
- **7. Closing summary:** present (L282). Fix finding 2.
- **8. Length:** 18 pages is justified by explanatory text, but there is no slack left. To offset the additions above, delete L27 and recast L39 shorter (finding 6).

### Voice (§A.32/§A.33)
- The added lines contain no reader instruction and no history voice; "now" and "no longer" occur only inside the card narration.
- Borderline self-assessment, all optional:
  - L29: "The idea matters because it turns a question about interpretation into questions that can be settled mathematically";
  - L230: "the sharpest test of what partial access can and cannot explain";
  - L282: "These results turn the opening question into precise statements…".
  - Each could be made neutral, for example L230 as "Bell's theorem tests exactly this".
- L23 "every result below is stated and proved without it" is acceptable: it marks the analogy, as the owner asked.
