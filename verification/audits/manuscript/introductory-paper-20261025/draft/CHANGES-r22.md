# Introduction r22: the two r21 reviews (`d3790019`), on base `683c45de`

r22 applies two reviews of r21:

- **gate 1** (`scientific/GATE1-papers-d3790019.md`): ACCEPT, with optional items O1–O5;
- **gate 3** (`editorial/GATE3-papers-d3790019.md`): ACCEPT WITH CHANGES.

It also applies the owner's later notes: the abstract organized around four questions, the recurrence horizon, the
three terms, a concise abstract that keeps every hypothesis, and the difference between L and an observer's windows.

**What is unchanged:**

- No theorem or corollary statement changed.
- The §2.4 Corollary (L118) is byte-identical.
- Every census fingerprint is unchanged: 97ce3099c02498fb, a1abae061358524e, b596be8af06bd797, 67e2d2a4f01999ed, 603c7f6d12b01679, 106e5e6806523955.
- Only the ledger `line` fields moved (65, 103, 118, 138, 144, 216). No ID was retired.
- The recurrence scope wording in the Corollary (L144) and §6 (L300) is r21's text.
- The abstract restates it concisely, as the owner now permits (§2).
- Main was not merged.

Line numbers: r21 → r22.

## 1. Finding → change

| # | Finding | r21 → r22 | Change |
|---|---|---|---|
| 1 | Must-fix, never-occurring rows (G3 #1 against G1 F2) | L134 → L136 | Now reads "…and it can happen that the only rows keeping the table from being a permutation belong to starts that never happen [Main §2.3]". See §3 for the sense check |
| 2 | L130/L134 duplication (G3 #2) | L130 → L132; L134 → L136 | Change A stays in L132. "The property that fails is called *P-divisibility*" now comes right after "…so the chain breaks.", and the card comparison explains why the property is checked from every start. L136's abstract restatement is cut to a back-reference: "a preparation that depended on the start would give rows for different setups, as in the card comparison above". L136 keeps the independence clause, the overlap definition (O1), the two-histories step [Main §2.3], the reason for keeping never-occurring rows (item 1) and the price sentence |
| 3 | L134 close (G3 #3) | → L136 | "…; when every start has positive probability, every row is one that occurs (see the Corollary)." |
| 4 | L146 split (G3 #4) | L146 → L148, L150, L152 | (a) the plain reading, the L-versus-window sentence (owner) and the four-bit example; (b) "Precisely: …"; (c) "Recurrence-cycle indivisibility thus …". "The past predicts the observation at time 3 exactly". The example still ends "it shows no failure of chaining inside it", and every deterministic completion still keeps X₀ |
| 5 | L214 order (G3 #5, G1 O3) | L214 → L220 | Order: "…so OI alone does not imply quantum mechanics (both machine-checked) [GR §3.3]. Conditions (i) and (ii) only make the theory well formed, the well-formedness requirements of any operational theory, while (iii)–(v) are the substantive selection principles [GR §3.3]. Which of (iii)–(v) a physical substratum supplies is the open step toward full operational equivalence." The "therefore" sentence is deleted. GR §3.3 reads: "(i) and (ii) are well-formedness requirements of any operational theory; (iii)–(v) are the substantive selection principles" |
| 6 | L161 (G3 #6) | → L167 | "…that failure lies somewhere in its full cycle, not necessarily on an accessible window." |
| 7 | Terminology (G3 #7, owner) | see §4 | The record's M_t is "conditional memory" or "memory in the record"; "hidden predictive memory" is the hidden quantity; P-divisibility and accessible memory are defined in plain words at first use |
| 8 | Abstract (G3 #8, G1 O5, owner) | L17 | Reorganized and shortened from 385 to 310 words; §1 now starts on p. 1. See §2 |
| 9 | L250 (G3 #9, G1 O2) | → L256 | "the vacuum-energy estimate exceeds the observed value by some 120 orders of magnitude [Wei89, §III]" |
| 10 | O1 | L136 | "an *overlap*, two rows that are both positive in a common column (Theorem 3)" |
| 11 | O4 | L194 | "Among what is proved: accessible memory does not force …, and outside the diagonal-preserving class …" |
| 12 | G3 #10 | L140 | "A step-by-step forecast can never move two forecasts further apart, …" |
| 13 | G3 #12 | L132 | The forward reference "as in the anticorrelated deal of §2.6" is dropped; the inline description is enough |
| 14 | G3 #11, Theorem 2 split | L101 | A raw spacing hint before Theorem 2, `\par\vspace{0pt plus 14\baselineskip}\penalty-100\vspace{0pt plus -14\baselineskip}`, keeps the theorem whole (now on p. 6). It uses no package. The build's `--include-in-header` overrides YAML `header-includes`, so `\needspace` was not available |
| owner | Recurrence horizon | L142 | "the least return time. A time n with Γ_n=I is a *return horizon*, and the horizon {0,…,L} up to the world's return is its *recurrence cycle*". This defines the term used at L156 (moved verbatim) and in Appendix A. "Recurrence horizon" now appears nowhere |
| owner | L against observation windows | L148 | "Accessible windows are, by definition, short compared with the world's least return time L [Main §2.3, Scope], and the gap between the two is why memory can become detectable only later: a trace held in the hidden part can first affect what is seen at an order beyond every accessible window, though still before the return." Main §2.3 Scope: "(C4) and condition (ii) of §3.4 require an accessible order, kτ_S ≪ t_R" |

## 2. The abstract, sentence by sentence (old r21 → new r22)

Order: what OI is → what is established → why it matters → what is open.

| r21 | r22 | Meaning and hypotheses |
|---|---|---|
| "Could the randomness … reality? Put simply, every pattern of quantum records … must be stored in the hidden part of every such world." | The question is unchanged and opens the abstract. The "Put simply" sentence becomes "So stochastic, quantum-like records can arise exactly from deterministic dynamics, and any memory they show must be stored in the hidden part" (the "why it matters" step, after the results) | Preserved: Theorem 1 with the §2.4 Corollary, as before |
| "Observational incompleteness (OI) is the hypothesis … visible marginals of its dynamics." | unchanged | — |
| "At every finite horizon, all finite stochastic laws, … coincide, so stochastic, quantum-like records can arise exactly from deterministic dynamics; the known components … machine-checked theorem." | "At every finite horizon, three classes of law coincide: all finite stochastic laws, the visible marginals of finite reversible dynamics, and the records of finite unitary systems measured in one fixed basis; the known components (Egri et al.; Barandes) are stated as one machine-checked theorem." | Preserved: the same three classes, finite horizon, fixed basis and evidence class. The "so …" consequence moves to the "why it matters" sentence |
| "Because Markov laws lie in every class, … conditional memory in its hidden state." | unchanged | — |
| "On one finite reversible system with a hidden prior shared by every root and drawn independently of it, the rooted visible family, with a row for every initial visible state (root) including roots of visible probability zero, is P-indivisible somewhere in its recurrence cycle whenever some rooted transition matrix is not a permutation, which every non-deterministic visible step supplies …; with a full-support visible prior this indivisibility is equivalent to conditional memory M_k>0 at some order k below the recurrence time." | "In a finite reversible world whose hidden odds are shared by every visible start and drawn independently of it, the forecasts from every start, starts of probability zero included, are P-indivisible somewhere in the recurrence cycle whenever some rooted transition matrix is not a permutation, in particular whenever a visible step is not fully predictable from the current observation; with every start of positive probability, this is equivalent to conditional memory at some order below the recurrence time." | Preserved, with every hypothesis the owner lists: a finite reversible world; hidden odds shared and independent; the rooted family with zero-probability rows ("the forecasts from every start, starts of probability zero included"); the general non-permutation condition, with the non-deterministic step as its instance in the O5 wording; failure somewhere in the cycle; and the full-support equivalence. The r21 "In plain words …" sentence is removed, since §2.5 carries it |
| "For an operational theory with a stated minimal structure … and OI alone does not imply them." | unchanged | All of Theorem 4's hypotheses: stated minimal structure, nonempty finite system, every finite ancilla, exactly the normalized finite Kraus instruments, iff the five conditions, not implied by OI |
| "OI places the zero-point sum … from its accessible recovery; open are …" | "Applied to physics, OI places … from its accessible recovery. Open are the completion conditions a physical substratum supplies, the Born exponent and the gravitational field equations." | Preserved: the same two applications at the same status, and the same three open items |

## 3. Item 1: the sense check against Main §2.3

- **What Main says.** The proof of Theorem (history readback + finite recurrence implies indivisibility) says that "some Γ_s, 1 ≤ s ≤ min(k, L−1), is not a permutation, possibly only through a row of a root of visible probability zero; the lemma applies to the square matrix, which is why every row is kept". The sense is possibility: in some cases every row whose departure from a permutation matters is a row of a never-occurring start. It does not say that only such rows can matter.
- **Earlier wordings and their misreadings.**
  - r20: "the overlap … can sit in such a row alone". Gate 1 F2 rejected it, because an overlap involves two rows.
  - r21: "may fail to be a permutation only through such a row". Gate 3 #1 found it could be read as a false restriction.
- **The r22 wording.** "it can happen that the only rows keeping the table from being a permutation belong to starts that never happen". It states the possibility ("it can happen"). It concerns the rows that keep the matrix from being a permutation, not an overlap, which needs two rows. It does not restrict the general case.

## 4. Terminology sweep (§§1–6; line numbers at r22)

| Term | Definition at first use | Occurrences |
|---|---|---|
| conditional memory M_t | L99: "the information about the next observation that the observed past carries beyond what the observed present already tells" | L17, L99, L122, L124, L126, L148, L167, L192, L309 |
| hidden predictive memory | L99: "the information retained in the hidden state that supports the observed process's dependence on history" (I(X_<t;H_t\|X_t)) | L99, L103 (Theorem 2's title), L122, L128, L300 |
| bare "predictive memory" | — | none remains: every occurrence is "hidden predictive memory" |
| memory in the record (for M_t) | — | L126, L167, L196 |
| accessible memory (conditional memory at an order an observer can reach) | L98/L124, through (C4)'s accessible order; L194 | L148, L194 |
| P-divisibility / P-divisible | L132: "whether the forecasts from the start admit step-by-step intermediate forecasts over the interval in question"; formal definition at L134 | L132, L134, L136, L138, L144, L150, L154, L167, L194, L202 |
| P-indivisible | — | L17, L165, L178, L192, L194, L198, L300 |
| recurrence cycle / return horizon | L142 | recurrence cycle: L17, L142, L148, L192; return horizon: L142, L156 |

## 5. Not applied

| Item | Reason |
|---|---|
| G3 #8, its alternative "In plain words" clause placed inside the abstract's scope sentence | the owner reorganized the abstract instead; the plain gloss lives in §2.5 (L132, L144, L148) |
| G1 O5, a plain-sentence trigger | carried by the abstract's recurrence sentence itself ("whenever a visible step is not fully predictable from the current observation") |
| L298's "(§2.5, with its scope)" | not proposed this round; the owner's explicit-scope rule stands |

## 6. Build and checks

- **Build.** `sh ./build.sh Introduction` gives 21 pages at 11 pt with one-inch margins. The median is 3,117 non-space characters per page. §1 starts on p. 1, Theorem 2 sits whole on p. 6, and the main text ends on p. 19.
- **Typesetting.** A direct compile gives 0 overfull, 0 underfull and 0 missing characters.
- **Renders.** I looked at p. 1 (the abstract and §1) and p. 8 (the shared-prior paragraph, Theorem 3, the return horizon and the Corollary).
- **Release gate.** Every step passes except `lean-axioms`, which cannot run locally because `lake` is missing; it passes in CI. `duplicate` passes after the records fix at `bfd8b026`.
- **Other checks.**
  - `voice`, `claims`, `coverage` (134), `staleness` and `mirror` all pass.
  - `edge_rigidity_probe`: ALL CHECKS PASS.
  - Appendix A is unchanged.
- **Added-lines scans.** No hits for the §A.32/§A.33 phrase families, caps emphasis, markers, secrets, scratch paths or model identifiers.
