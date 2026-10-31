## Editorial and citation re-review of the Introduction at r17 (`a79add6a`, PR #918)

**Verdict: ACCEPT WITH CHANGES.** r17 resolves nearly all of my r16 findings, but it introduces five must-fixes: an unresolved citation key, a symbol with two meanings, two statements stronger than their evidence, and one sufficient condition that is false as written.

I worked read-only: no edits, commits, pushes or comments. 23 GB were free on disk. My worktree `rev918r17` has been removed; `rev918r17-sci` belongs to another agent and was left alone.

### 1. Build and layout
- **Build:** `sh ./build.sh Introduction` gives 12 pages. The regenerated `.tex` is identical to the committed one, and the PDF text matches the committed PDF.
- **Density:** median 3,547 non-space characters per page (4,140 counting whitespace); range 2,522–4,536.
- **Boxes and glyphs:** 0 overfull boxes and 0 dropped glyphs. One underfull line remains, in the code note's 40-character hash; it is benign.
- **Page map:**
  - §1 starts on p1;
  - the main text ends at the top of p10;
  - the code note and Appendix A are on p10, and the references on pp11–12.
- **Rendered pages (80 dpi):**
  - p1: two-line title; the abstract and §1 both fit on the page.
  - p5: the Γ matrices display in full, and the card table's rules align.
  - p8: both field-equation displays sit within the margins.
  - p11: Appendix A is set `\small` and the references `\footnotesize` with 1 pt paragraph spacing. Nothing overflows, but entries run together without separation (O3).
- **Readability (owner decision):** at 10 pt with one-inch margins a line holds about 111 characters; r16 had about 79. The owner approved the margins "provided the resulting manuscript remains readable". Adding `fontsize: 11pt` to the YAML block gives about 100 characters per line and 14 pages, with the main text ending on p12, still inside 12–15. I recommend 11 pt (S9).
- **YAML block (L5–7):** the `---` here opens a YAML block closed by `...`, not a horizontal rule. It parses correctly and the page count is plausible, so no action is needed.

### 2. Status of the r16 findings
**Resolved:**
- **Must-fixes, all three:**
  - the abstract now names the rooted family;
  - the Sha79 citation is corrected (L211);
  - the layout is the Page-curve setup [GR App. A.7] (L209).
- **Should-fixes:**
  - L60 dilation is now |𝒞_V|²;
  - the recurrence result is displayed as a Corollary (L109);
  - significance sentences were added (L95, L113, but see M4);
  - the repeated limitations are consolidated (the §3.5 Born sentence and the closing line of §6 are gone);
  - the card CP/BBS24 paragraph moved to §3.1, with "measure-and-prepare" glossed;
  - "memory witness" is used, and the causal cone is glossed (L179);
  - I\* is defined (L95, but see M3);
  - one term per object;
  - g_# is defined (L40);
  - the §6 apposition is fixed;
  - μ,ν and d_G are used;
  - "constitutional" is gone.
- **Optional:** the Cal26 DOI is added (L294).
- **L89 Corollary:** byte-identical (now L93), as the owner decided.

**Departures, all sound:**
- **cut8.md reference edits.** The writer is right: my simulation's regex removed "; arXiv:1905" and left ".08762". It was a defect in my scratch script, not a proposal to keep.
- **Contributions novelty sentence.** Keeping it satisfies citation finding M3. My alternative wording would have reported a literature search that was not made.
- **§3.4 Har04.** "Montina reports Hardy's result" is the correct attribution for a source that was not read first-hand.
- **"Generic" sentence.** Declining it was correct; the replacement has its own problem (M4).
- **§3.2 and §3.3 compressions.** Declining them was correct: they would drop required structure fields and the "exactly when" equivalence.
- **Spectator-independent gloss.** "Acts on every product input as the identity on the system" matches the kernel definition better than my wording.
- **"Status ledger".** It is Main's term (Main :726 "**Status ledger (theorems and conditions)**").
- **τ_B^D.** "D-sector timescale" is GR's term.

### 3. Findings

**Must-fix**

- **M1. L181: `[SM]` is cited but has no entry.** It is the only unresolved key; there are no orphans.
  - Add to the Corpus list: `[SM] A. Maybaum, "The Standard Model from a Cubic Lattice," papers/SM.md.` This is the title as cited in Main :887.

- **M2. L16, abstract.**
  - Current: "OI separates the zero-point sum from the gravitational source".
  - Problem: §4 establishes only that the two belong to different levels of description. That the zero-point sum is not a gravitational source is the proposal, conditional on G3 (GR :356). This turns conditional into unconditional, against the owner's demonstrated/proposed split.
  - Proposed: "OI places the zero-point sum and the effective cosmological constant at different levels of description, and separates conservation of black-hole information from its accessible recovery".

- **M3. L97: I\* has two meanings.**
  - L95 defines I\* = max_t I(X_{<t};X_{>t}|X_t), the past–future information.
  - L97 then writes "observed conditional memory I\*>0 at an accessible order forces … ε_min(I\*,|𝒞_V|)". Main's theorem (:463) bounds the one-step conditional memory I(X_{<k};X_{k+1}|X_k), which is M_k.
  - Proposed: "observed conditional memory M_k>0 at an accessible order k forces … at least ε_min(M_k,|𝒞_V|)>0".

- **M4. L113: the sufficient condition is overstated.**
  - Current: "Recurrence-cycle indivisibility thus follows from finite reversibility and partial access alone, Markov laws included, and does not distinguish one law from another".
  - Problem: it also needs a non-permutation Γ_s. A visible sector that evolves deterministically under any hidden state is divisible, which this paper itself shows (L137, anticorrelated cards). "One law from another" is also too broad.
  - Proposed: "Recurrence-cycle indivisibility thus follows from finite reversibility and any non-deterministic visible step, Markov laws included, so it does not distinguish a law with memory from one without; what an observer can discriminate is memory at an accessible order, which (C4) asserts [Main §2.3, Scope]."

- **M5. L109, the Corollary: the sufficient condition is false as written.**
  - Current: "Two distinct positive-probability visible histories with a common endpoint … supply such a Γ_s".
  - Problem: Main :137 requires histories of the same length, (x_0..x_k)≠(x'_0..x'_k) with x_k=x'_k. Without that, the statement fails. Counterexample: σ₁ a swap, Γ₁ a permutation, histories (a) and (b, σ₁(b)=a) both have positive probability.
  - Proposed: "Two distinct positive-probability visible histories of equal length with a common endpoint, in particular a memory witness, …". The memory-witness definition at L91 is already equal-length.

**Should-fix**

- **S1. L97, the (C2) sentence (about 90 words).**
  - Problem: "accessible order", "accessible window", "coupling time" and "the model's reference prior" are undefined. "Accessible" is used undefined at L97, L109, L113 and L145.
  - Proposed: split the sentence. Define once, at L97: "an accessible order or window lies within the observer's times, short compared with the recurrence time [Main §2.3, Scope]". Gloss the reference prior: "(the hidden law π_H toward which the hidden dynamics relaxes between couplings)".

- **S2. L181, the Bell–lattice clause.**
  - Problem: the sentence ends with a dangling ", while operational no-signalling is required". "Preparation-indexed coupling graph" is undefined, and "graph cone" differs from "causal-cone property" two lines earlier.
  - Proposed: "…adopts ontic parameter dependence: one wing's microstate response may depend on the remote setting, with operational no-signalling required. The nearest-neighbour cubic update of the lattice substratum [SM] alone cannot supply it for wings outside each other's causal cone [Main §3.3, Corollary (Bell–lattice obstruction and state-dependent escape)]. That a preparation-indexed coupling graph, in which a Bell preparation adds bounded-degree long-range edges, can supply it while preserving operational no-signalling and the gravitational continuum limit is the open hypothesis H-Bell [Main §3.3]."

- **S3. L209, observer access.**
  - Current: "in the counts below the emitted radiation registers".
  - Problem: this is false for the 60 and 32 counts, which use complete access or one register read.
  - Proposed: "(for the first count below, the radiation registers as they are emitted)".

- **S4. L213: "τ_B^D∼1/H".** Here H is the Hubble rate, which clashes with H_t and Ĥ and is undefined. Proposed: "∼1/H, the Hubble time".

- **S5. L193: the de Sitter sentence.** It has no locator and sits under "The proposed resolution", although it is a dimensional identity rather than part of the proposal. Proposed: move it to §4's opening paragraph and cite [GR §6.3], which exists at 4449b0d9 (:364).

- **S6. L147: one paragraph of about 2,100 characters.** Split it into three: the notions and CP-divisibility; the card embedding and BBS24; backflow and representation/Calvo.

- **S7. L16, abstract (233 words).**
  - Problem: the recurrence sentence nests three qualifiers, and "root" is undefined in the abstract.
  - Proposed, keeping every scope element: "On one finite reversible system, the rooted transition matrices from the initial time, one row per initial visible state under a common hidden prior drawn independently of it, are P-indivisible somewhere in the recurrence cycle whenever one is not a permutation, which every non-deterministic visible step supplies; with a full-support visible prior this indivisibility is equivalent to conditional memory M_k>0 at some order k below the recurrence time."

- **S8. L64: grammar.**
  - Current: "…[SGD19, Eq. (3)], whose consistency under omitted measurements [SGD19; Milz20] Q_K, measuring at every step, does not meet".
  - Proposed: "…[SGD19, Eq. (3)]; whether such records remain consistent when measurements are omitted [SGD19; Milz20] does not arise for Q_K, which measures at every step."

- **S9. Font size (owner decision).** Use `fontsize: 11pt` (section 1 above).

**Optional**

- **O1. L217, §6:** the full recurrence scope is copied verbatim a third time. "(§2.5, with its scope)" would do, if the scientific reviewer's S2 permits.
- **O2. L109:** match the Corollary label style to the others: "**Corollary** (recurrence-cycle indivisibility [Main §2.3])."
- **O3. References:** a hanging indent would separate entries now that paragraph spacing is 1 pt.
- **O4. L171:** "each such trajectory law is a fixed-basis Born record and stochastic" adds little.

### 4. Notation in the r17 additions
- **§2.5 Corollary:** M5 above; everything else is defined.
- **(C2) persistence sentence:** M3 and S1.
- **Bell–lattice clause:** M1 and S2.
- **Significance sentences:** L95 is accurate; L113 is M4.

### 5. Voice (§A.32/§A.33) on added lines
- The scan finds no meta-commentary, reader instruction, history voice, self-assessment or caps emphasis, and there are no HTML comments.
- The kept novelty sentence (L32) has a sound recorded reason.

### 6. Citations
- **Keys:** 51 entries, no orphans; one unresolved key, `[SM]` (M1).
- **Cal26 DOI:** doi:10.1007/s40509-026-00415-9 is present and matched Crossref in my r16 check.
- **Sha79:** used correctly now.
- **Locators at main `4449b0d9`:** every one exists.
  - #958 changed exactly four single lines in Main (:99, :109, :336, :652), adding none, so every cited Main item keeps its title and line:
    - §1.2 Remarks (:60, :62);
    - Main §1.5 (:99), whose edit concerns the (C2) forms and agrees with the paper's L97;
    - the §2.3 theorem (:137) and Scope (:141);
    - the readback lemma (:167);
    - §2.4 (:178);
    - the §3.2 Remarks and Theorem (:326–:334), untouched by the :336 change;
    - the Bell ceiling (:360) and its Corollary (:410);
    - the physical-memory theorem (:463);
    - the §3.4 items (:512–:640);
    - §4.5 (:714).
  - GR: §2.2, §3.3 (:218), §6.2, §6.3, §8.5, App. A.1/A.5/A.6/A.7 and Thms A.7–A.9 are intact.
  - Book: §1.11 and §7.6 are intact.

### 7. Owner direction
- **Correspondence first:** the paper leads with it (§1.2, §2.2).
- **Significance before the challenges:** §2.4 and §2.5 explain why the results matter before §3 (fix M4).
- **Limitations:** consolidated, apart from O1.
- **Cosmological constant:** the body separates the demonstrated result from the proposal; the abstract does not (M2).
- **Examples:** the card table and the black-hole toy model are concrete, with exact counts that match the BH-01 records.
