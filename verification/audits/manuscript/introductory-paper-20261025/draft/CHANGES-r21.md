# Introduction r21: the three r20 reviews (`10c629ea`), on base `542b1d9c`

r21 applies three reviews, with the final wording of the third and the owner's brief:

- `scientific/GATE1-papers-10c629ea.md`: findings F1–F4;
- `editorial/GATE3-papers-10c629ea.md`: findings 1–15;
- `accessibility/RUN2-EVALUATION.md`, changes A, 1, B, C and R1–R4, using its "Final wording" section.

**Preserved:**

- No theorem or corollary statement changed.
- The §2.4 Corollary (L116) is byte-identical.
- The recurrence scope wording is r20's text in the abstract (L17), the Corollary (L142) and §6 (L294).
- Every census fingerprint is unchanged: 97ce3099c02498fb, a1abae061358524e, b596be8af06bd797, 67e2d2a4f01999ed, 603c7f6d12b01679 and 106e5e6806523955.
- Only the ledger `line` fields moved (65, 101, 116, 136, 142, 210). No ID was retired.
- `main` was not merged.

Line numbers are `papers/Introduction.md` at r20 → r21.

## 1. Finding → change

| # | Finding | r20 → r21 | Change |
|---|---|---|---|
| 1 | G1 F1, abstract | L17 → L17 | The Theorem 4 sentence now carries its hypotheses: "For an operational theory with a stated minimal structure on a nonempty finite system, the available operations, on the system and with every finite ancilla attached, are exactly the normalized finite Kraus instruments if and only if five completion conditions hold, and OI alone does not imply them." See the consistency table (§3) |
| 2 | G3 must-fix 1 + G1 F4 | L230 → L226 | "So the fixed-basis records cannot distinguish two quantum descriptions with trivial ancilla that agree on everything visible, and choosing the evolution between two times needs a principle that the records do not supply." |
| 3 | G2 run-2 gate-1 finding, L188 | L188 → L188 | "no unconditional implication among them is asserted [Main §3.2, Remark (three notions, kept apart)]", followed by "What is proved is that accessible memory does not force P-indivisibility on a window (§2.6), and that outside the diagonal-preserving class P-indivisibility does not force CP-indivisibility (below)." The proved implication for the permutation-dilation family is kept in the same paragraph. Main: "No unconditional implication among the three is asserted here" |
| 4 | G2 change A | L130 → L130 | The card example is inserted after "…so the chain breaks.", with one adjustment (§2) |
| 5 | G2 change 1 + G1 F2 + G3 should-fix 4 | L134 → L134 | The final wording, with three amendments: (a) the reason for keeping never-occurring rows is "the table may fail to be a permutation only through such a row" (F2); (b) the "price" sentence is included; (c) "overlap" is defined at first use as "two rows sharing a positive entry (Theorem 3)", and the failure is stated "for some earlier and later time" |
| 6 | G2 change B + tightening | L144 → L146 | "Predictive memory can exist all the same, at a later order, …"; the four-bit example ending "The example shows memory beyond the window; it shows no failure of chaining inside it." |
| 7 | G2 change C, with the optional second sentence | L161 → L161 | The final wording, then: "A reversible world that reproduces this law, with the hidden odds independent of the visible start, still fails to chain somewhere in its full cycle (§2.5), because its visible steps are not fully predictable; that failure lies on the recurrence horizon, not necessarily on an accessible window." Only the proved coexistence on the window is stated; nothing says the properties are independent in general |
| 8 | G1 F3 | L49 → L49 | "its order L is the *least* number of steps after which every configuration has returned to itself" |
| 9 | G3 should-fix 2 | L214 → L212 | Shortened to the reviewer's sentence. It keeps the §3.2 structure, a nonempty finite system, any finite helper, the normalized finite Kraus instruments, and all five requirements |
| 10 | G3 should-fix 3 | L296 → L292 | "conversely, if the hidden part of any one such world holds a trace of the past that changes what is seen next, the record has memory." The Summary's Theorem 4 clause now also names the normalized finite Kraus instruments (§3) |
| 11 | G3 should-fix 5 | L126 → L126 | "**Proofs and sources.** *Theorem 2.* Part (b)…" |
| 12 | G3 should-fix 6 | — → L138 | After Theorem 3: "A step-by-step forecast can only bring forecasts closer, so two forecasts that overlap at time s can never become the two distinct certainties of Γ_n=I." L148 keeps the full paragraph |
| 13 | G3 should-fix 7 | L200, L216, L218 → L200, L214 | "Qubit" is defined at first use (L200). r20 L218 is merged into L216 (now L214); its repeated first sentence and its open-question restatement (already the last sentence of L216) are dropped |
| 14 | G3 should-fix 8 | L288 → L284 | "measure concentration is the fact that in very large state spaces almost every state gives nearly the same value of a smooth quantity such as the entanglement entropy" |
| 15 | G3 should-fix 9 | L292 → L288 | "…and for an evaporating black hole whose radiation carries away its energy, not every configuration of black hole and radiation has the same energy." |
| 16 | G2 R3 | → L214 | "Conditions (i) and (ii) are well-formedness requirements of any operational theory, and (iii)–(v) are the substantive selection principles [GR §3.3]." This is GR §3.3's own wording. The reviewer's "that any operational theory meets" is not used, because GR does not say it |
| 17 | G2 R2 | L250 → L246 | "So, given determinism and an outcome in every run, …". Glosses added: "the coupling graph records which parts of the substratum directly affect which" (Main §3.3 coupling graph: site i joined to j when φ's i-th output depends on the j-th input), and "H-Bell is the named hypothesis that suitable extra links can be added for a Bell preparation with those two properties", the two being no usable signal and the continuum limit (Main §3.3, H-Bell: "the prepared graph family must preserve operational no-signaling and satisfy a curvature/metric convergence condition") |
| 18 | G2 R4 | L17 | The bridging sentence stays second. A plain gloss follows the verified recurrence sentence: "In plain words: when the hidden part starts with the same odds whatever is visible, any visible step that is not fully predictable means that the forecasts from the start, including those from starts that never occur, cannot all be chained step by step somewhere in the world's cycle." The scope sentence itself is unchanged |
| 19a | G3 optional 10 | r20 L202, L142, L146 | Deleted r20 L202, which repeats L180 and L200. Dropped the last sentence of r20 L142, now carried by L134 and L146. Folded r20 L146 into the end of L146 (r21); its text is unchanged |
| 19b | G3 optional 12 | L27 | "Put this way" becomes "So framed"; "Put simply" in the abstract is kept |
| 19c | G3 optional 13 | L254 → L250 | "the mismatch is some 120 orders of magnitude [Wei89]". Wei89 is in the references, and §4 already cites it for this figure (§I; §III, Eqs. (3.4)–(3.6)) |
| 19d | G3 optional 15 | L41 | Convention note: "Where a subsection's evidence classes and attributions are long, they close it in a paragraph labelled *Proofs and sources*; elsewhere they are given inline." |

## 2. Checks of changes A, 1, B and C against §2.6 and Main

**A, the card example (L130).**

- §2.6's card table deals the burn card b "uniform and independent of x". Main §2.3's theorem draws "the root … from a visible prior and the hidden state from μ_H, independently". So "the face-down card dealt the same way, at even odds, whichever card is face up" is exactly the hidden prior shared by every root and drawn independently of it.
- A dealer who always deals red face up is a visible prior with zero weight on black; the black row is a root of visible probability zero, which the paper keeps (L102 definition).
- The contrast case, a root-dependent deal, is named only to exclude it.
- **Adjustment.** The final wording said "as in the deal at the end of §2.6". The anticorrelated deal (b = 1−x) is in the card table's commentary paragraph, which is not §2.6's last paragraph. It now reads "as in the anticorrelated deal of §2.6".
- The example explains why an absent start belongs to the comparison. It states no recurrence conclusion and is not offered as a proof.

**1, the L134 rewrite.**

- **Independence.** "The step from two observed histories with a common endpoint to an overlap … uses that every row comes from the same preparation [Main §2.3]" is the proof's inference "the visible configuration at each time t ≤ k would be σ_t of the root, μ_H-almost surely", which needs the hidden state to have law μ_H given every root (Gate 1 §2).
- **Never-occurring rows.** Rows for starts that never occur are "computed from the same preparation", not forecasts the process gives. "The table may fail to be a permutation only through such a row" is Main's "possibly only through a row of a root of visible probability zero; the lemma applies to the square matrix, which is why every row is kept".
- **The price sentence.** With full support, failure on {0,…,L} is equivalent to M_k > 0 for some k < L, which is the Corollary under its hypotheses.

**B, the four-bit example (L146).**

- M₁ = 0 because X₂ is independent of (X₀, X₁), and M₂ = H(X₀) = 1 bit.
- Every deterministic completion keeps X₀ at time 2: I(X_<2;H₂|X₂) ≥ I(X_<2;X_>2|X₂) = 1 (L120; `c3_necessity_via_hidden`).
- Main §3.4, Remark (a variational question), uses this same law.
- On {0,1,2}, Γ₁ = Γ₂ = ½J, which is P-divisible, so the example shows no chaining failure on the window, as its last sentence says.

**C, after the XOR example (L161).**

- XOR has M₁ = 1 bit and is P-divisible on {0,1,2} (Main §2.3 Scope: "the XOR control remains a counterexample"). By the §2.4 Corollary, every faithful realization carries readout-relevant hidden memory.
- The second sentence applies the §2.5 Corollary under its hypotheses: a hidden prior independent of the visible start, and a non-deterministic visible step. It places the failure on the recurrence horizon, not necessarily on an accessible window.
- Nothing claims independence of the two properties in general.

## 3. Theorem 4 at every site

| Site | Line | Hypotheses carried | Conclusion |
|---|---|---|---|
| Statement | L210 | every nonempty finite system; the §3.2 structure (setup at L202); every positive ancilla level | exactly the normalized finite Kraus instruments iff (i)–(v) |
| Abstract | L17 | "an operational theory with a stated minimal structure on a nonempty finite system … on the system and with every finite ancilla attached" | "exactly the normalized finite Kraus instruments if and only if five completion conditions hold" |
| §3.2 question | L200 | "on a finite system, with helper systems attached … for a theory with the structure described below" | the question that Theorem 4 answers |
| Plain reading | L212 | "for a theory with the structure above … a nonempty finite system, with any finite helper attached" | "exactly the quantum ones (the normalized finite Kraus instruments) if and only if all five requirements hold" |
| Summary | L292 | "for an operational theory with the structure of §3.2 on a nonempty finite system … on the system and with every finite ancilla attached" | "exactly the normalized finite Kraus instruments … if and only if five stated conditions hold" |
| Roadmap | L37 | — | no Theorem 4 formulation ("how far the correspondence reaches toward operational quantum mechanics") |
| §3 opener and established list | L180, L294 | — | references only ("five conditions that OI does not imply"; "Theorem 4 and the independence of its conditions") |

## 4. Not applied, with reasons

- **G3 optional 10, L298 → "(§2.5, with its scope)".** Not applied: the owner requires an explicit, consistent scope.
- **G3 optional 10, dropping L75's first sentence.** Not applied: that sentence carries the Realization attributions [Main §3.4; EGGH26, Prop. 13], so dropping it loses sources.
- **G3 optional 11, defining each term inside the sentence that first uses it (L184, L254).** Not applied: the terms are first used inside verified statement paragraphs (L188; L252–L254), and defining them in place would edit those paragraphs. The definitions stay in the openers immediately before them.
- **G3 optional 14, the page break.** Not separately applied, since the edits moved it. Theorem 3 now sits whole on p. 8.
- **G2 R3, the reviewer's wording "that any operational theory meets".** Replaced by GR §3.3's own wording (item 16).

## 5. Build and checks

- **Build:** `sh ./build.sh Introduction` gives 21 pages at 11 pt with one-inch margins (r20: 20). This is within the brief's limit. The last page is about two-thirds full. The main text (§§1–6) ends on p. 19.
- **Density and typesetting:** median 3,155 non-space characters per page. A direct compile gives 0 overfull, 0 underfull and 0 missing characters.
- **Renders checked:** p. 1, the abstract; p. 7, the card example; p. 8, the shared-prior paragraph, Theorem 3 and its one-line reason; p. 12.
- **Release gate:** every step passes except `lean-axioms`, which needs `lake`, and `duplicate`.
  - The `duplicate` failure is in `review/accessibility/RUN2-EVALUATION.md`, a record committed at the base `542b1d9c`. Its three reports repeat headings and quoted wordings. It fails identically at the base without this revision.
  - This revision does not edit that record, under the instruction not to edit the accessibility records. It needs a records-side fix before CI passes.
- **Other checks:**
  - `voice`, `claims`, `coverage` (134), `staleness` and `mirror` all pass.
  - `edge_rigidity_probe`: ALL CHECKS PASS.
  - Appendix A is unchanged from r20, where all 29 declarations resolved at `17b830bc`.
- **Added-lines scans:** no hits for the §A.32/§A.33 phrase families, caps emphasis, markers, secrets, scratch paths or model identifiers.
