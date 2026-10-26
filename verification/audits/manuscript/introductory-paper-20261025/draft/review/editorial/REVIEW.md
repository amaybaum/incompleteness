# Editorial review — Introduction paper draft

- **Object:** `S/paper/draft/Introduction.md`, sha256 `03c1154b…4b25` (identical to `draft/build/papers/Introduction.md`). Line numbers below refer to this file.
- **Scope:** presentation, structure, register, length, typesetting. The science is reviewed separately. Scientific points noticed in passing are marked **[SCI]** and not re-derived.
- **Read-only:** no repository file changed. Probes ran in `S/paper/ed-review/` only: a `git archive` of `687e885b` in `tree/`, and rebuilds in `tex/` and `fixed/`.

## Verdict

**ACCEPT WITH CHANGES** on editorial grounds.

The draft is well organized, its status vocabulary is disciplined, and it follows the owner's six-part structure. Three kinds of defect need fixing before it can serve as the entry point:

1. **Typesetting.** 21 lists render as run-in text, and Appendix A overprints its own columns (F1, F2).
2. **Register.** Four process-narration sentences reach the PDF (F3).
3. **Undefined terms.** Several terms of art are used without definition, which an external reader cannot recover (F7).

Landing is separately gated by items outside editorial scope: the three R11 markers, the §A.42 expected-result placeholder and the 17 VERIFY bibliography markers. This review agrees that each of these gates landing.

## Checks re-run

- **Voice and claims checks.** In a fresh `git archive` of `687e885b` with the draft at `papers/Introduction.md`:
  - `tools/voice_check.py --root .` reports OK. It scanned 41 files; without the draft it scans 40, so the draft was included.
  - `tools/claims_check.py --root .` reports OK.
  - Both tools are scoped to history narration and withdrawn results. They do not catch the process-narration sentences in F3.
- **Own grep of the §A.32/§A.33 families.**
  - Meta-commentary, reader instruction, "honest", "discipline", "throughout": no hits.
  - History phrases: one hit, line 367 "is reversed" (F3e).
  - Caps (`[A-Z]{4,}` in visible text): CHSH, HKLP, JCAP, CADE and DRAFT (status line) only. Clean.
- **Build.** pandoc + xelatex on the repository recipe: 20 pages and no dropped glyphs, but **28 overfull hboxes**, up to 150 pt (F2, F15).

## Findings

### Typesetting and build (blocking for any PDF that is distributed)

**F1. 21 lists are not rendered as lists.** Pandoc markdown needs a blank line before a list. Every list introduced by a line ending in ":" without a blank line typesets as a paragraph with literal "- " and "1." in it (see PDF p. 2, §1.2, and p. 15, the Conclusion).

- **Affected list starts:** lines 35, 40, 71, 87, 105, 114, 120, 124, 148, 159, 164, 247, 261, 280, 293, 297, 309, 322, 380 and 394. The nested list at 311–313 inherits the problem.
- **Correctly rendered:** only §6.4 (336) and §6.5 (355), which have the blank line.
- **Effect on length.** Rendering them correctly adds pages:

  | Format | As drafted | Lists rendered correctly |
  |---|---|---|
  | Default | 20 pp | **21 pp** |
  | 1-inch margins, 10 pt | 14 pp | **15 pp** |
  | 1-inch margins, 11 pt | 16 pp | **17 pp** |

  DRAFT-NOTES' length figures therefore understate the true length by one page.

**F2. Appendix A overprints itself.** On PDF pp. 16–17 the long monospace identifiers run into the Status column, and the text is visibly superimposed. 17 of the 28 overfull boxes are in this table.

- No column layout fixes it. `pIndivisible_of_rooted_identity_return_of_overlap` alone is about 270 pt in 10 pt tt, against a text width of about 345 pt. A two-column version still overflows by 90 pt (probe `fixed/Intro-cut4.md`).
- Required: set Appendix A as a list (RC2).

**F15. Other overfull lines:**

- Body:
  - line 109 (Kernel: …, 5.5 pt);
  - line 145 (9.9 pt);
  - **line 152 (121 pt)**;
  - lines 309–315 (up to 75 pt);
  - line 323 (36 pt).
- Code section: lines 406 (56 pt) and 408 (84 pt).
- References:
  - [Book] 144 pt (the long filename);
  - [BH-01] 128 pt;
  - [BH-02] 81 pt.
- Most disappear once the in-body identifiers move to Appendix A (cut C1).
- The remaining repository paths in the Code section and the references need a break point, or should be shortened, e.g. `verification/programmes/black-hole-information/` → "the repository's `black-hole-information` programme directory".

**F16. The title is hyphenated.** On p. 1 the title, set as a `#` heading, breaks "Repre-sentations". This goes away with a shorter title (F12) or with `\hyphenation{representations}` in a header include.

### Register (§A.27 manuscript voice, §A.32, §A.33, §A.30)

**F3. Process narration in visible text.** None of these is caught by voice_check, because they are not history phrases.

- **(a) Line 90.** "A packaged statement of the three-way multi-time identification was not located in the literature read for this paper. The quantum-comb realization literature was not read."
  - This is drafting-process narration and self-assessment of the search, so it falls under §A.27 (manuscript voice) and §A.32.
  - For an external reader the second sentence reads as an admission that the novelty claim is unchecked.
  - **[SCI]** The process-tensor and quantum-comb literature (Chiribella–D'Ariano–Perinotti; Pollock et al.) is the obvious place where a three-way finite-horizon identification might already exist. The originality statement should rest on reading it, not on announcing it was not read.
- **(b) Line 225.** "…and passed an independent internal review [BH-01; BH-02]." An internal review is not a credential an external reader can weigh; this is self-assessment under §A.32.
- **(c) Line 240.** "The package describes the remnant bound as…". "The package" is internal jargon.
  - **[SCI]** "a known fact" and "the secret-sharing threshold" need an external citation, e.g. Shamir 1979 or Blakley 1979.
- **(d) Line 244.** "The intervals for the greybody factor and $\tau_B^D$ were fixed after the plan". This is internal preregistration vocabulary.
- **(e) Line 244 "Exact interval arithmetic reverses that ground", and line 367 "The stated support for decoupling the trans-cosmological sector is reversed".**
  - Both narrate a correction to a companion paper inside the entry paper. Line 367 is revision-history voice (§A.33) about the corpus.
  - Under §A.27 the fix is to correct GR in place (R11), after which the Introduction states the fact declaratively, without reference to GR's former ground (RC6).

**F4. Meta-commentary and reader-direction.** All are borderline, but each is cheaply fixed:

- **Line 14:** "given with its exact rule and scope". Meta; delete.
- **Line 16:** "Three statuses are kept apart." This is commentary on the paper's own discipline (§A.32 first bullet); see RC7.
- **Line 113:** "stated here in prose because one of its links is not formalized". This narrates the exposition; state it as a labelled proposition with its status (RC8).
- **Line 168:** "The physical reading of these results is a representation result, not an explanation." It is a category slip (a *reading* is not a *result*) and works as a reader instruction (RC9).
- **Line 28:** "is presently established". "Presently" is time-relative voice; delete it.
- **Line 96:** "The form 'a law is non-Markovian if and only if a finite reversible realization exists' is false…".
  - It refutes a statement no external reader holds; it is Main's "retired direction" carried over.
  - It is implicit revision history. Delete it (cut C3); the preceding sentence already makes the point.
- **Line 231:** "This is the content that bijectivity carries." Rhetorical; delete it, since the preceding sentence suffices.

**F5. §6.5 "What is not claimed" (lines 353–369).**

- Six numbered disclaimers of the framework's own claims. Under §A.30 a scope section is admissible, but every item restates something already stated declaratively where it is derived:
  - item 1: §2.3 and §1.2;
  - item 2: §6.1–6.2;
  - item 3: §2.3;
  - item 4: §3.2;
  - item 5: §5.2–5.4;
  - item 6: §1.1.
- The abstract and §8 restate the same list a third time.
- As self-assessment outside status labels it brushes §A.32's fourth bullet.
- Recommend deletion (cut C13); no distinction is lost (see the cut list).

### Structure and flow for an external expert

**F6. The abstract.** It states the proved representability and the open selection, but:

- it omits the status of Theorems 2 and 3 (machine-checked for the joint law / rooted form, with one step each on paper);
- it calls Theorem 4 "characterized only under five completion conditions". Theorem 4 is an unconditional characterization; what is conditional is *reaching* operational QM. Write "characterized exactly by five completion conditions";
- "On one finite reversible representative" and "history readback" are undefined at that point;
- the black-hole sentence says what is treated, not what is found.

A replacement is given in RC7.

**F7. Terms used before, or without, definition.** These are the main barrier for the target reader.

| Term | Line(s) | Fix |
|---|---|---|
| "kernel", "proved in the kernel", "kernel witnesses" | 70, 145, 308 | define once (RC12) |
| "proved in prose", "exact probes" | 82, 121, 131, 152, 345, App. A | define once (RC12) |
| "faithful (deterministic) realization" | 104, 113, 129 | Main:99 defines it; RC12 |
| "substratum" | 98, 256, 280, 317, 336 | RC12 |
| $\pi_V$ | 102 | "the projection onto $\mathcal C_V$" |
| $J$ | 165, 194, 213 | "the all-ones matrix" |
| "P-indivisible within $n$" | 143 | define, or "on $\{0,\dots,n\}$" |
| "routed-readback witness" | 152 | goes with cut C1 |
| "sealed finite C1–C4 observation process" | 317 | "a fixed finite observation process satisfying (C1)–(C4)" |
| "relative candidate", "strong-class element", "quotient by visible equality" | 322–324 | one-clause gloss each, or cut to the statement in 321 + 326 |
| "accessible order" | 131 | goes with cut C4 |
| "inert ledger bits" | 346 | gloss |
| "posit ledger" | 351 | goes with cut C15 |
| "H-Bell", "ontic parameter dependence" | 349 | one-clause gloss |
| "access class" | 16, 399 | define in §5 opening |
| "zero accessible advantage" | 236, 239 | define once |
| "trans-cosmological sector" | 229 | one clause, or drop $D$ if C10 is taken |
| "Main ledger" | App. A | goes with RC2 |
| "street", "hole card", "burn card", "showdown" | §4.3 | one clause |
| Conditions (iii)–(v) | §6.1 | named but never defined, so Theorem 4 cannot be understood from this paper; give one line each |

**F8. Notation clashes.**

- **$S$** is the total system (§1.1), the stochastic class (§2.1), $S_{\mathrm{BH}}$ (§5.3) and $S_{\mathrm{CHSH}}$ (§6.4). Rename the classes, e.g. $\mathsf S_K,\mathsf D_K,\mathsf Q_K$ with the horizon explicit, or $\mathcal L^{\mathrm{st}}_K$, etc.
- **$K$** is the horizon (§2) and the set of unread register values (§5.1). Use $\mathcal U$ in §5.1.
- **$M$** is $M_t$ memory (§2.4), the message set (§5.1) and the mass (§5.3). Use $\mathcal M$ for messages.
- **$H$** is the hidden subsystem, $H_t$, the entropy $H(p_0)$ (§5.2), "Hadamard" (165), and the labels H-scramble and H-Bell. At least write "conjugation by the Hadamard gate" at 165.
- **$V\subsetneq S$ with $H=S\setminus V$ (line 24) against $S=\mathcal C_V\times\mathcal C_H$.** The first is subset language, the second a product. State the product form only: "the observer's configurations $\mathcal C_V$ and the complement's $\mathcal C_H$".
- **$S\iff D\iff Q_{\mathrm{fb}}$ (line 66) relates sets with a logical connective.**
  - "coincide" means $=$. Main uses the same display, so changing the Introduction alone creates a notation difference with Main; the owner decides.
  - The editorial recommendation is $\mathsf S_K=\mathsf D_K=\mathsf Q_K$ here, with Main following.
- **"C1–C4" (317) against "(C1)–(C4)" elsewhere.** Use the parenthesized form throughout.

**F9. Section openings.**

- §5 and §6 open with their point.
- §2, §3 and §4 open with a definition ("Fix finite sets", "Write $\Gamma_t$", "Let $\mathcal C_V$").
- §3's title promises "Physical interpretation", but its body is Theorem 3, and the interpretation sentence is buried at §3.2's end.
- §4.1's intuition (line 190, the hidden record "flipped") comes after the matrices; put it first.
- Exact lead sentences are in RC13.

**F10. Placement of Theorem 4.**

- The paper's strongest carrier-general machine-checked result sits under §6.1, "Why exact operational quantum mechanics is not established". For an expert reader that undersells it and frames a theorem as a limitation.
- Option (owner's structure permitting): retitle §6.1 "Operational completion". Keep Theorem 4 there and put the limitation in the paragraph after it (lines 317).
- The cite "[GR §3.3]" points into a section titled "Gauge-fixing and the dimensional obstruction". Cite it as "[GR §3.3, Theorem (operational-completion characterization)]" so the reader can find it.
- **[SCI] / §A.25.**
  - GR:228 gives the kernel witnesses as `main_result` and `oi_compatible_classification`.
  - The draft gives `exactAll_iff_physical_general` / `exactAll_of_physical_general` / `physical_of_exactAll`.
  - Check that the two citations name the same theorem, or align the mirrors.

**F11. Cross-references to Main.**

- The form is consistent in shape, "[Main §n, Remark on X]", but the remark names are paraphrases, and some do not match Main's titles. Use Main's italic titles verbatim so a reader can search for them:

  | Line | Draft | Main |
  |---|---|---|
  | 96 | "Remark on diagnostics" | §3.4 *Remark (the conditions are diagnostics, not hypotheses)*, Main:596 |
  | 165 | "[Main §3.2, Remark]" | *Remark (scope: P-indivisibility is not quantum non-Markovianity)*, Main:330 |
  | 168 | "Remark on representation and explanation" | *Remark (representation, not explanation)*, Main:616 |
  | 321 | "Remark on representability" | *Remark (scope: representability, not selection of the relating evolution)*, Main:624 |
  | 82 | "finite-horizon process dilation" | *Theorem (finite-horizon process dilation)*, Main:496 |
  | 330 | "Proposition on the finite-substratum obstruction" | *Proposition (finite-substratum operational obstruction — classical-dimension form)*, Main:538 |
  | 26 | "[Main §1.2 Remark; §4.5]" | §1.2 has four remarks; name it, presumably *Remark (status of the early commitments)* or *(reversibility as the conservative assumption)* |
  | 117 | "[Main §1.5, …]" | §1.5 is "The four layers". **[SCI]** confirm that is where the CMI vanishing criterion is used |

- References to GR also vary:
  - "[GR App. A.7, Theorem A.7]" (244);
  - "[GR App. A.7, Theorems A.8–A.9]" (256);
  - "[GR, Theorem A.8]" (281).

  Use one form, e.g. "[GR, Thm A.8]".

**F13. No contributions statement.**

- The paper is to be "a technical perspective with original mathematical components", but nowhere states in one place which components are original. Attributions are scattered over §2.2, §3.1, §4.2 and §7.
- An expert reader expects a 3–5 line "Contributions" paragraph at the end of §1.2, separating known (cited) from new and from concurrent (Doukas).
- The content is the owner's and the science reviewer's call (AUDIT r4 originality); this is a structural gap only.

**F14. Pointer to Main.**

- The paper should direct readers to Main for complete arguments. It says so once, "The full development is [Main]" (44).
- Make it explicit in §1.2 and §8 (RC13).
- Presentation risk for the owner: [Main]'s subtitle, "The Equivalence of Quantum Mechanics and Embedded Observation" (line 444), reads against this paper's positioning (§6.5 item 1, "No derivation of quantum mechanics"). The reader goes from one directly to the other.

### Tables, displays, lists

- **Card table (206–211).**
  - Necessary; the owner requires it. Fix it (RC11):
    - "odds" is a probability, not odds;
    - row 3 is a Markov prediction mixed into a column of protocols.
  - The last paragraph of §4.3 (217) is dense and carries seven cross-references; compress it (cut C8).
- **Theorem 4 display (303–306).** A lone "$\iff$ conditions (i)–(v) hold" is displayed under an italic sentence that serves as its left side. This is awkward (PDF p. 12); state it as a sentence (RC10). §A.34 is satisfied: both directions have witnesses at 309–313.
- **Theorem 1 display (65–67).** Keep it, with $=$ (F8).
- **§4.1 permutation display (177–179).** "$(0,1\leftrightarrow1,1)$" reads as a 2-tuple. Write each transposition as $\big((0,1)\ (1,1)\big)$, or in words: "swap $(0,h)\leftrightarrow(1,h)$ for $h\in\{1,2\}$, $h=3\leftrightarrow4$ and $5\leftrightarrow6$ at fixed $x$".
- **Short lists that should be prose** (they cost vertical space once F1 is fixed, and each item is a fragment):
  - 35–37 (three features);
  - 159–161 (three notions);
  - 247–249 (three limits);
  - 261–263 (three assumptions);
  - 293–294;
  - 297–301 (five conditions, which render as "• (i)", a double label);
  - 120–121 (two bounds);
  - 394–395 (Conclusion).
- **Lists that earn their keep:**
  - Theorem 1's six directions (71–74, §A.34);
  - Theorem 2 (a)–(c);
  - §3.1's three steps;
  - §5.4 open steps;
  - §6.4.
- **Appendix A usability.**
  - The layout is broken (F2).
  - The Status column repeats the body. "Main ledger (ii)⇒(iii)" means nothing without Main open. "As above" chains three rows.
  - Two rows ("Readback bound", "CP-indivisibility") are "none" in a table called a kernel map.
  - Required layout: RC2.
- **DRAFT-NOTES' own tables** are fine (not published).

### Bibliography (formatting only)

**F17. Bibliography formatting.**

- **Key scheme mixes four styles:**
  - initials: BD, BJA, BLP, EG, GH, MO, DO, SGD, HKLP, LPW, CT, BB;
  - author+year: Bell64, CHSH69, Hardy04, Hawking76, Milz20, Page93/05/13, Pen19;
  - initial+year: B23, B25, B26, RHP10, RHP14;
  - names: Lean4, Mathlib.

  Main uses numeric keys. Choose numeric (matching Main) or one alphabetic scheme, e.g. [Bar23], [BD16], [RHP14].
- **Key–year mismatch:** [B23] has year (2026), the v2 date. Either give the original year or drop the year from the key.
- **Missing fields, visible in the PDF:**
  - [Hardy04] has no title;
  - [EG] has no initials;
  - [BB], [GH], [MO] and [Pen19] have no year or venue;
  - [GR], [Book] and the BH entries have no DOI, while [Main] has one.
- **Inconsistent journal pattern:**
  - "*Phys. Rev. Lett.* **103**, 210401 (2009)";
  - "*JCAP* **09** (2013) 028";
  - "*Philosophy of Physics* **3**(1):8 (2025)".

  Use one pattern, *Journal* **vol**, page (year).
- **Page ranges:** given in full for Bell64, CHSH69, Hawking76 and PSW, first page only elsewhere. Pick one.
- **arXiv versions:** suffixes appear on some entries and not on others (HKLP, Page93/05/13, Pen19). Pick one.
- **DOI:** only [B25] carries one.
- **[BH-01] and [BH-02]:**
  - no author;
  - internal round names ("v1", "BH-02/BH-04");
  - review-acceptance SHAs ("independent review accepted at `df2ea6f5`"), which is process detail (F3b).
  - Proposed form: `A. Maybaum, "Black-hole information: access separations in finite reversible models," repository path, commit 687e885b.`
- **Status header:** "DRAFT" against the corpus's "DRAFT PRE-PRINT" (Main, GR). Nit.

## Required changes (exact text)

**RC1 (F1).** Insert one blank line before each list start at lines 35, 40, 71, 87, 105, 114, 120, 124, 148, 159, 164, 247, 261, 280, 293, 297, 309, 322, 380 and 394. Then re-check the page count.

**RC2 (F2).** Replace the Appendix A table with a list, one entry per result. Example entries:

```
- **Theorem 1** (§2.2). `finite_horizon_equivalence` (Equivalence:462); directions `S_imp_D` (:422), `D_imp_Qfb` (:294), `Qfb_imp_S` (:245); compositions :466–468.
- **Theorem 2** (§2.4). `pushforward_identity`, `distinguishability_floor`, `capacity_floor`, `unavoidable_hidden_predictive_memory` (HiddenMemory:83, 114, 170, 185). Stated for a joint law of history, present and hidden state; the identification with a realization's time-$t$ law, and the CMI vanishing criterion, are proved on paper.
- **Theorem 3** (§3.1). `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148).
```

The other entries follow the same pattern. Notes on the conversion:

- Drop the "Main ledger" pointers.
- Drop the two "none" rows. Their status, proved on paper, is stated in the body at lines 121 and 164.
- Merge the three Theorem 2 rows into one.

**RC3 (F3a), line 90.** Replace both sentences with "We are not aware of a packaged statement of the three-way multi-time identification." This is conditional on the science reviewer's view of the comb literature. If that literature is not checked, drop the sentence altogether rather than narrate the search.

**RC4 (F3b), line 225.** Use: "Each was checked by exhaustive enumeration at small size [BH-01; BH-02]."

**RC5 (F3c), line 240.** Use: "The remnant bound is the remnant-capacity form of a known fact, and its linear case is the secret-sharing threshold [BH-01; Shamir79]." This adds an external citation (**[SCI]**).

**RC6 (F3d–e).**

- **If the owner keeps the decoupling result after R11:**
  - Replace lines 244–249 with the following (§5.4 bullet or one paragraph): "Decoupling of $D$ over the evaporation is not established by timescale ordering: at 30 solar masses $t_{\mathrm{evap}}/\tau_B^D\ge1.785\times10^{57}$ and $t_P/\tau_B^D\ge1.153\times10^{57}$ ($t_P$ the Page time at $\beta=1$), over the full intervals assumed for the greybody factor and $\tau_B^D$ [BH-01, item F]. This does not show that information reaches $D$, and does not exclude other decoupling arguments."
  - Delete line 367.
- **If the owner drops it:** delete 243–249 and 367.

**RC7 (F4, F6).** Replace lines 14–16 (abstract):

> An observer that is a proper part of a finite deterministic system records only part of its state. Observational incompleteness (OI) is the hypothesis that every physical observer is in this situation: the statistics it records are the visible marginals of a finite reversible deterministic system of which it is a proper part. At every finite horizon three classes of law on visible trajectories coincide: all finite stochastic laws, the visible marginals of finite reversible dynamics, and the fixed-basis Born records of finite unitary systems (machine-checked). Each class contains the Markov laws, so neither a reversible realization nor a quantum representation distinguishes one law from another; the Born dictionary is part of the definition of the quantum class, and its quadratic exponent is not selected. The discriminating content concerns memory. Every deterministic completion of a law with conditional memory carries that memory in its hidden state, and on a fixed finite reversible system finite recurrence turns history readback into stochastic indivisibility somewhere in the recurrence cycle (machine-checked, with one step proved on paper). Exact finite operational quantum mechanics is characterized by five completion conditions (machine-checked), none implied by OI alone. Open are which of these conditions a physical substratum supplies, the selection of the evolution relating two times, and any test of the physical hypothesis. A two-card game gives the smallest worked example. In a bounded application to black-hole information, finite toy computations separate conservation of information under bijective dynamics from its recovery by an observer with restricted access, and show that in the framework's Page-curve argument the Page entropy enters through a scrambling hypothesis rather than through bijectivity.

(About 250 words. Owner and science reviewer to confirm each status parenthesis against Appendix A.)

**RC8 (F4), lines 113–117.** Replace with:

> **Corollary** (proved on paper). $M_t>0$ holds exactly when every faithful realization carries readout-relevant hidden memory at $t$, that is, a pair of posteriors with different pushforwards. The forward direction applies (a) in each realization; the converse applies (a) in one realization, which exists by Theorem 1. Both directions use the vanishing criterion for conditional mutual information.

**RC9 (F4), line 168.** Replace with:

> Theorem 1 is a representation result. It states which laws admit realizations and quantum representations, not why a given physical system exhibits a law with memory; that requires a specific physical realization [Main §3.4, Remark (representation, not explanation)].

**RC10, lines 303–306.** Replace with:

> **Theorem 4** (operational-completion characterization [GR §3.3]). *For every nonempty finite system, the available outcome families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*

**RC11, lines 204–211.** Replace with:

```
The probability that the hole card at showdown is the hole card as dealt is, by exact enumeration:

| Protocol | Probability |
|---|---|
| one shuffle | 1/2 |
| two shuffles | 1 |
| two shuffles, with a peek between them | 1/2 |
| Markov prediction for two shuffles, $\Gamma_1^2$ | 1/2 |
```

In line 215, "the odds are 1" becomes "the probability is 1". Add one clause in 200–202: "a *street* is one shuffle step".

**RC12 (F7).** Add at the end of §1.2 (after line 44):

> *Conventions.* "Machine-checked" means proved in Lean 4/Mathlib; the declarations are listed in Appendix A. "Proved on paper" means a written proof without a machine check. An "exact probe" is an exhaustive computation in exact rational arithmetic at small size. A *faithful realization* of a law is a bijection $\varphi$ of $\mathcal C_V\times\mathcal C_H$ with an initial law under which the visible trajectory has that law; the finite reversible system $(S,\varphi)$ is called the *substratum*.

Then:

- Replace "kernel" in the body with "machine-checked".
- Define $\pi_V$ at 102: "the projection onto $\mathcal C_V$".
- Define $J$ at its first use: "the all-ones matrix".

**RC13 (F9, F14).** Lead sentences:

- **§2, before 2.1:** "This section states the three classes of finite-horizon law, proves that they coincide, and locates the content that the coincidence leaves: where the memory of a law must sit."
- **§3, before 3.1 (§3 title could become "Physical interpretation: indivisibility from recurrence"):** "The quantum-like feature that restricted observation produces on a finite reversible system is stochastic indivisibility: between some pair of times no stochastic map relates the visible transition matrices. Finite recurrence forces it whenever the law has history readback."
- **§4, before 4.1:** "Three small examples show recurrence-driven indivisibility, memory without short-window indivisibility, and the smallest realization of Theorem 3."
- **§1.2, line 44:** replace "The full development is [Main]." with "Complete proofs, the full status ledger and the probe code are in [Main], which this paper introduces."

**RC14.** Delete line 96's second sentence ("The form … as well"), and line 231's "This is the content that bijectivity carries." In line 28, delete "presently".

## Cut list: about 2,000 words, to ≤15 pages in the repository default format

### Measured, not estimated

`S/paper/ed-review/scripts/cutprobe{,2,3,4}.py` applied cuts C1–C16 approximately to a copy with lists rendered correctly (RC1), and rebuilt it with the repository recipe:

| Stage | Source words | Pages (default format) |
|---|---|---|
| draft, lists fixed | 6,604 | 21 |
| C1–C14 (`Intro-cut.md`) | 5,293 | 17 |
| + Appendix A restructured, §6.4 trimmed, two compressions (`Intro-cut2.md`) | 5,120 | 16 |
| + short lists inlined (`Intro-cut3.md`) | 5,069 | 16 |
| + C15–C16 (`Intro-cut4.md`) | 4,972 | 16 (67 words on p. 16) |

Pages 13–14 of the last stage are part-empty: the Conclusion and Code section end on p. 13, and Appendix A starts on p. 14. Setting Appendix A as a list (RC2) and a further ~150 words, for example C17, reach **15 pages**. The total needed is therefore **about 1,800–1,900 source words**, consistent with DRAFT-NOTES' "about 2,000" (which was measured with the lists collapsed).

### The cuts

None of the cuts removes an established / hypothesis / open distinction. Each removes a restatement, a process detail, or material that lives in Main.

| # | Cut | Lines | ≈ words saved | Why no distinction is lost |
|---|---|---|---|---|
| C1 | Move every in-body Lean identifier and line number to Appendix A, except the direction witnesses of Theorems 1 and 4 (§A.34 needs those beside the display). Compress 309–315 to the two direction witnesses plus the assembly identifier. Also fixes about 10 overfull lines | 54, 83, 109, 120, 145, 147, 152, 311–315, 317, 322–324 | 270 | status words ("machine-checked" / "proved on paper") stay in the text |
| C2 | §2.2 "Attribution" list → two sentences (EG Props 13/16, LPW; B25/B26), plus RC3 | 86–90 | 100 | attributions kept |
| C3 | Line 96, "The form … is false" sentence | 96 | 35 | point made by the preceding sentence |
| C4 | Per-horizon characterization paragraph. It reduces to the memory statement, as its last sentence says | 131 | 85 | the memory biconditional (RC8) remains |
| C5 | (C1)–(C4) list → one sentence defining (C4), the only condition used later, and stating that the four are diagnostics, not hypotheses | 123–129 | 60 | §3.1 needs only (C4) |
| C6 | RC8 compression of the biconditional | 113–117 | 40 | — |
| C7 | §3.2 last paragraph (RC9 shortens it; or delete, since §1.1 says it) | 168 | 30–60 | — |
| C8 | §4.3 last paragraph → "On card inputs the game is a classical stochastic process, and its P-indivisibility is notion (2) of §3.2. Under the permutation-unitary embedding the one-step channel is entanglement-breaking and the two-step map is the identity, so the family is also CP-indivisible [Main §3.2]. A card arrangement violates no Bell inequality [Main §3.3]." This drops the uniform-burn-versus-initialized-slot decomposition contrast, which is Main §4.5 material; owner decides | 217 | 75 | — |
| C9 | §5.1 access bullets → one paragraph: the two separations, the sufficient conditions and the bound. Drop "Status of the conditions" and "Nested traces" (the Fubini identity carries no recovery content, by its own statement) | 236–241 | 130 | sufficient-not-necessary kept |
| C10 | Decoupling paragraph and three-limits list → one sentence in §5.4 (RC6) | 243–249 | 110 | — |
| C11 | §5.3: drop the "Robustness" bullet; shorten "Sensitivity" to one value | 271–273 | 50 | conditionality on three inputs kept |
| C12 | §6.3 last paragraph (the ε-gluing theorems "on which no conclusion here rests") | 332 | 50 | — |
| C13 | Delete §6.5 "What is not claimed". Optionally add one sentence to §8: "Neither a derivation of quantum mechanics nor a resolution of the black-hole information problem is claimed." | 353–369 | 170 | every item is stated where derived (F5) |
| C14 | Delete §7 "Related work". Move its two items not cited elsewhere, B26 Thm 3.3 (the $n^2$ dilation) and SGD/Milz20 "does not meet that question", into §2.2's attribution sentences | 373–387 | 190 | attributions remain at point of use (§2.2, §3.1, §3.2, §4.2, §6.3) |
| C15 | §6.4: items 1–3 and 10 point back to §6.1, §6.2, §2.3 and §5.4 → one sentence. Item 4 (formalization list) → "the steps marked proved on paper in Appendix A". Item 9 duplicates §1.1 | 336–351 | 150 | every open problem is still listed once |
| C16 | §1.1 duplicate "representation choice" sentence (28); compress line 30 to one sentence; §1.2 roadmap → one sentence; §4.2 attribution → one clause | 28, 30, 44, 194 | 100 | — |
| C17 | §2.2 independent-prior paragraph (82) → one sentence; §3.1 three-step list kept, "The kernel proves…" sentence (152) → "Steps 2–3 are machine-checked; step 1 is proved on paper." | 82, 152 | 70 | — |
| | **Total** | | **≈1,800–1,900** | |

Appendix A restructured to a list (RC2) saves about half a page of whitespace and both "none" rows (about 40 words).

### The 1-inch-margin alternative

- **Measured page counts, lists rendered correctly:**

  | Format | Draft as is | After the cuts |
  |---|---|---|
  | 1 in, 10 pt | **15 pp** (at the limit, not 14) | 11 pp |
  | 1 in, 11 pt | 17 pp | **13 pp** |

- **Trade-off.** One-inch margins at 10 pt give about 95–105 characters per line, against about 75 in the default. That is well past the usual 60–75 range for comfortable reading of mathematical prose; it is common in arXiv preprints, but harder to read. 1 in at 11 pt is the conventional preprint geometry (about 90 characters per line).
- **Uniformity.** No other paper in the corpus overrides geometry; all use `build.sh`'s default. A per-paper YAML block (`geometry: margin=1in`, `fontsize: 11pt`) would make the Introduction the only paper so formatted.
  - YAML front matter needs `---` delimiters, which AGENTS.md's build recipe asks to avoid. They are harmless at the head of a file, but this departs from house practice.
  - The alternative is a repository-wide change to `build.sh`.
- **Recommendation (owner decides).** Make the cuts in any case, since they are mostly redundancy. Then either keep the default format (about 15 pp) or adopt 1 in / 11 pt (about 13 pp). Avoid 1 in / 10 pt.

## Title (owner R1)

The working title, "Observational Incompleteness: Quantum Representations of Partially Observed Deterministic Systems", is accurate. But "Quantum Representations of" leads with the quantum side and hyphenates on p. 1. Alternatives that do not read as a derivation of QM:

1. **What an Embedded Observer Can Record: Stochastic, Reversible and Quantum Laws at Finite Horizon**
2. **Observational Incompleteness: Memory, Recurrence and Indivisibility in Partially Observed Reversible Systems**
3. **Hidden Memory and Finite Recurrence in Partially Observed Reversible Dynamics**

## Nits

- Line 8, "Classification": matches corpus. Line 7: "DRAFT" against "DRAFT PRE-PRINT".
- Line 24: "An *observation* is a triple $(S,\varphi,V)$". Calling the triple an observation is Main's usage, but it surprises a reader; "An *embedded observer setting*" or "We model embedded observation by a triple" reads more naturally.
- Line 26: "a posit, not a theorem" → "is posited". The status label suffices.
- Line 37: "would-be intermediate transition maps" → "candidate intermediate transition maps".
- Line 143: "P-indivisible within $n$" (F7).
- Line 158: "kept apart" → "distinct".
- Line 186: "with entries 5/9 and 4/9" → "with diagonal entries 5/9 and off-diagonal 4/9".
- Line 225: "with written proofs" → "proved on paper" (RC12 vocabulary).
- Line 229: "Radiation is emitted from $B$ into $V$": add "modelled as".
- Line 239: "The bound is the one necessary-side fact proved." It is unclear which bound; name it ($|\mathcal U|\ge|\mathcal M|$ for zero advantage) (**[SCI]** clarity).
- Line 271: "In the quasi-stationary semiclassical regime $\beta>1$ [Page05…]." This is a verbless sentence; write "$\beta>1$ in the quasi-stationary semiclassical regime [Page05, Eqs. (5)–(10)]."
- Line 330: "This is a form of Hardy's finite-ontic-state no-go" → "This is Hardy's ontological-excess-baggage argument in finite form [Hardy04]". The Hardy04 title is missing (F17).
- Line 349: "The framework's adopted branch": "adopted" is the framework's self-description. State the hypothesis H-Bell itself.
- Line 393: "At finite observable horizon" → "At every finite horizon".
- Line 406: the commit SHA appears in full here and abbreviated elsewhere. Fine, but keep the full SHA once and the 8-character form after.
- The 17 `<!-- VERIFY -->` and 5 `<!-- OWNER -->` comments do not reach the PDF (confirmed with pdftotext), but they must be resolved before landing.

## Files

- Review: `S/paper/ed-review/REVIEW.md`.
- Probes:
  - `S/paper/ed-review/fixed/Intro-lists.md` and its `.pdf` (lists fixed, 21 pp);
  - `S/paper/ed-review/fixed/Intro-cut4.md` and its `.pdf` (cut probe, 16 pp);
  - `S/paper/ed-review/scripts/cutprobe*.py`;
  - overfull log `S/paper/ed-review/tex/Introduction.log`.
