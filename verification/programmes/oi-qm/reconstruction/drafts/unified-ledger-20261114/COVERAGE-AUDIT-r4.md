# Coverage audit r4: manuscript claims against the unified derivation ledger r3

**UNREVIEWED.** r4 revises `COVERAGE-AUDIT-r3.md`, which is left unchanged, as are r1, r2 and the
earlier responses. r4 applies the focused confirmation `REVIEW-AUDIT-r3.md` (verdict ACCEPT WITH
CHANGES) and changes only what that review and the coordinator name. Every item's disposition is in
`RESPONSE-AUDIT-r3.md`; earlier changes are recorded in `RESPONSE-AUDIT-r2.md` and
`RESPONSE-AUDIT-r1.md`. r4 has not been reviewed, and its review is required before acceptance.

The work is paper-only and read-only. No computation on OI rules was run and nothing was posted. No
manuscript or record file was edited; this file and `RESPONSE-AUDIT-r3.md` are the only files written for r4. The
ledger under audit, `LEDGER-r3.md`, is itself unreviewed. Inclusion of a claim here implies no
derivation of it. A complete ledger is not a complete theory.

**Authorization, quoted verbatim.**
- #914 comment 6877871344 (`amaybaum`, 2026-11-14T13:19:06Z), condition 6: "**Completeness audit:**
  Check every substantive physical claim in Main, Substratum, SM, GR and Structure against the
  ledger. Use book chapters 18–19 as additional completeness controls. Record missing entries,
  unsupported claims and mismatches explicitly rather than silently resolving them." Condition 7:
  "The resulting r3 and audit require independent review before acceptance."
- #914 comment 6877908458 (`amaybaum`, 2026-11-14T13:22:18Z). The owner's words quoted there are "Yes,
  I approve adding the QCD group to r3". The text that places "QCD vacuum energy, condensates and
  gravitational coupling" in the Level C coverage audit, "cross-referenced to GR §6.2", is the recording
  text of that comment, not the owner's verbatim words. That item is checked at G-13 (ledger
  C-QCDVAC).
- #914 comment 6878781541 (`amaybaum`, 2026-11-14T14:26:48Z) records the owner guidance for the
  coverage audit, "in the coordinating session". The owner's words, quoted verbatim:

  > The reported gaps are substantial, but reprioritization should wait for the independent review.
  >
  > Three points should be explicit in its verdict:
  >
  > - Coverage boundary: excluding appendix summary rows needs justification where those rows make substantive physical claims. Checking SM §7 only by stated status may miss unsupported intermediate derivations.
  > - Counting: distinguish genuinely covered claims from claims merely grouped under a broader row. Report whether the 28 overstatements and 13 missing discriminating tests overlap the other categories.
  > - Contradictions: separate direct contradictions from differences in assumptions, scope or manuscript revision. Each confirmed finding needs paired source passages and the supporting proof's actual scope.
  >
  > Ledger r4 should incorporate confirmed findings and retain unresolved ones explicitly. The subsequent queue proposal should distinguish manuscript corrections, missing ledger coverage, and scientific research obligations—they require different work and authorization.
  >
  > The audit does not yet justify promoting QCD or another downstream branch ahead of the shared foundational gaps.

  The comment's closing paragraph is recording text, not the owner's words. The audit applies the
  guidance through the appendix-a row audit (§5), the §7 read (§6), the separate C and CB counts and
  flag cross-tabulations (§2), the conflict classes with paired passages (§3), and the MC/LC/RO work
  labels (§1, §3). r2 and r3 cited this guidance by paraphrase, before its record was available.

This audit adopts no claim, settles no premise, and proposes no change to any Issue, tier, readiness,
authorization or scientific status. It ranks no branch. The rows in §7 are proposals for the ledger
author only.

**Base.** The papers and book chapters were read from `main` at `dfeec843`, the commit the ledger
states it holds at. Line numbers are physical lines; paragraphs in `papers/*.md` are single long lines.
Locations without a path are lines of the paper named in the section heading.

## Contents

1. Method, codes and depth
2. Summary counts and cross-tabulation
3. Findings register: conflicts, overstatements and coverage gaps, with classification and kind of work
4. Per-paper tables
5. Appendix-a row audit
6. SM §7.1–§7.5 sample
7. Proposed ledger rows (proposals only)
8. Book-control findings
9. Off-`main` references (§A.42 item 8)
10. What this pass did not do

## 1. Method, codes and depth

**How the papers were read.** Each paper was read section by section. Abstracts, introductions,
status and scope sections, conclusions and every labelled theorem, lemma, proposition, corollary and
remark were read in full or in their claim-bearing part.

**Reduced depth.** The following were read at the level of their stated result and status:
- the long proof bodies in Main §3.4 and GR §3.3;
- the derivation bodies of SM §7.1–§7.5, except the sample in §6;
- Structure §13.1.1.1 and §14.7–§14.9.

Claims inside material read at reduced depth may be missed. **Every count below is therefore a lower
bound**, and so are the counts for sections the review's sampling reached (Main §2.1–§2.2, Substratum
§1.1 and §2, GR §8, SM §2.5–§2.6, Structure §3–§5 and §9.5–§9.7).

**Grouping.** Repeated statements of one claim are grouped under one entry, with every location
found. A claim derived in one paper and restated in another is counted once, under the paper that
derives it.

**Exclusions.** Exposition, definitions and literature summaries were excluded unless they assert
something about OI.

**Coverage codes** (exactly one per entry):
- **C**: covered by a ledger row that records this claim, with matching class and evidence.
- **CB**: grouped under a broader ledger row that does not record the claim separately: a branch row,
  a premise list, or a "per row at source" entry. CB is reported separately from C.
- **CM**: covered, with a mismatch. Either the ledger's class differs from the source's own status, or
  the sources disagree in a way the ledger does not record.
- **U**: no ledger row covers the claim.

**Flags** (independent of the code):
- **O**: the source states the claim more strongly than its own proof or cited support reaches.
- **T**: no concrete discriminating test is stated for the claim.

**Kind of work** (§3, owner guidance; kept separate because each needs different work and authorization):
- **MC**: a manuscript-correction candidate: a passage that would need correcting in a separate §A.25
  correction unit. This audit makes no correction and authorizes none, so every MC passage is still in
  the manuscript as quoted.
- **LC**: missing ledger coverage.
- **RO**: a scientific research obligation.

**Conflict classes** (§3): direct contradiction; difference in assumptions; difference in scope;
manuscript-revision difference. A claim stated more strongly than its own support, with no second
passage in conflict, is classed as a **single-source overstatement**.

**Status terms** (§3). They describe the audit's handling of a finding. None of them says that a
manuscript has been corrected or that a conflict has gone away.
- **Classified; stands (no correction made).** The finding has been checked at source and classified,
  and it stands. The passages are unchanged in the manuscripts, and the conflict or overstatement
  persists until a separate correction unit addresses it. This term replaces r2's "resolved as stated",
  which could be read as "fixed".
- **Unresolved.** The audit could not decide the question at source: a derivation or computation is
  open, or the passage needed was not located.
- **No conflict (withdrawn).** On reading the qualifying passage, the apparent conflict does not exist.

## 2. Summary counts and cross-tabulation

| Count | Main | Substratum | GR | SM | Structure | Total |
|---|---|---|---|---|---|---|
| Claims found (grouped entries) | 33 | 24 | 34 | 47 | 17 | **155** |
| C: covered by a matching row | 13 | 9 | 11 | 17 | 0 | **50** |
| CB: grouped under a broader row | 6 | 2 | 7 | 12 | 3 | **30** |
| CM: covered, with mismatch | 0 | 7 | 6 | 9 | 1 | **23** |
| U: uncovered | 14 | 6 | 10 | 9 | 13 | **52** |
| Flag O (overlaps the four codes) | 1 | 10 | 6 | 10 | 9 | **36** |
| Flag T (overlaps the four codes) | 1 | 3 | 3 | 2 | 4 | **13** |

In every column, C + CB + CM + U = claims found. All counts are lower bounds (§1).

**Cross-tabulation of the flags against the codes.** The flags overlap the codes; they are not
further categories.

| Flag | C | CB | CM | U | Total |
|---|---|---|---|---|---|
| O | 0 | 2 (SM-37, T-12) | 20 | 14 | 36 |
| T | 4 (M-27, G-26, SM-23, SM-41) | 1 (G-27) | 1 (G-23) | 7 (S-1, S-10, S-17, T-3, T-5, T-6, T-15) | 13 |
| O and T together | 0 | 0 | 0 | 6 (S-1, S-10, S-17, T-3, T-5, T-6) | 6 |

What the cross-tabulation shows:
- Three CM entries carry no O: S-21, G-23 and SM-34. Each records a disagreement between documents,
  not an overstatement.
- 20 of the 23 CM entries carry O.
- No C entry carries O.

**Appendix-a rows** (§5) are counted separately, because they are a book-control surface and not one
of the five papers:
- 64 rows audited; none excluded;
- 40 rows have a ledger row; 24 have none (G13, B1–B14, F1–F4, F9–F13);
- 16 rows carry a class or placement finding: rows 1, 6 and 22, N5, the eleven S-labelled biology
  rows anchored to ch16 and ch17 (B1, B2, B6–B14), and F12. B3's S label is unchecked (F-34);
- 6 rows carry the T flag: B4, F2–F4, F8 and F12.

**Unresolved findings:** 10 (§3 status lines, the observation after §4.5, and K-9 in §8; listed in §10).

## 3. Findings register

The register below covers every CM entry and every cross-document or within-document conflict, and
classifies each one. For each finding it gives:
- the passages, quoted with lines;
- the actual scope of the supporting proof;
- whether the finding is resolved;
- the kind of work it needs.

Single-source overstatements that have no second passage are listed in §3.2.

**Scope lines.** An explicit "Scope" line appears where the proof's reach needs stating beyond the
quoted passages. In every other finding, passage B is itself the source's statement of what its proof
covers: for example SM:448 (F-21), SM:458 (F-31), SM:468 (F-32) and SM:1396 (F-18). "Scope: not
applicable" holds for F-1, F-9, F-10 and F-29, which involve no proof.

### 3.1 Conflicts and mismatches

**F-1. Structure has no ledger coverage.** The ledger cites `papers/Structure.md` at no line. Thirteen
of seventeen grouped claims are U (§4.5).
- Class: missing coverage, not a conflict.
- Status: unresolved.
- Work: LC.

**F-2. Observer genericity (T-5).**
- Passage A, `papers/Structure.md`:733: "Most arbitrary $(S, \varphi)$ pairs do not admit observers —
  random permutations on finite sets typically lack the coupled-dynamics, non-equilibrium-phase, and
  high-capacity features required for C1–C4."
- Passage A′, Structure:717 (definition): "*Coupled dynamics:* $\varphi$ does not decompose as
  $\varphi_V \times \varphi_H$ for any candidate partition."
- Mirrors: `book/ch03-structural-realism.md`:26 and its FULL mirror
  (`book/The-Incompleteness-of-Observation-FULL.md`:891): "Random permutations on finite sets typically
  lack this structure: their cycle decompositions are wrong for the persistence condition …, their
  internal correlations are wrong for the capacity condition, or their coupling is too uniform or too
  sparse for the non-trivial-coupling condition."
- Passage B, `papers/Main.md`:147–151. A bijection produces a permutation one-step matrix "if and only
  if $\varphi$ has the form $\varphi(x_i, h) = (\varphi_V(x_i), \sigma_{x_i}(h))$", and "the fraction of
  bijections failing C1 at the $T$-level decays exponentially in the hidden-sector capacity $n_H$".
- Scope of B's proof: exact counting over all bijections of $\mathcal{C}_V \times \mathcal{C}_H$ for a
  fixed product partition with $|\mathcal{C}_V| \ge 2$. Its factorizing class is wider than A′'s
  $\varphi_V \times \varphi_H$, so B a fortiori makes A′'s factorizing class a vanishing fraction.
- Class:
  - **direct contradiction** for the coupling clause of A and its book mirrors;
  - **unresolved** for the persistence, capacity and readback clauses. The corpus proves neither that
    random permutations fail C2–C4 generically nor that they satisfy them. A's conclusion ("most do not
    admit observers") is therefore unsupported, not refuted.
- (r1 also cited SM Theorem 22. That was wrong: its hypothesis is "the wave equation (or any
  energy-conserving dynamics)" (`papers/SM.md`:1376), not random permutations, and the citation is
  withdrawn.)
- Status: coupling clause classified; stands (no correction made). C2–C4 clauses unresolved.
- Work: MC (Structure:733, ch03:26, FULL:891); LC (B-QM-18, C-STR-1); RO (whether C2 and C4 fail for
  typical bijections).

**F-3. Substratum Stage 2 states SM outputs without SM's conditions (S-7).**
- Passage A, `papers/Substratum.md`:
  - :151: "Three generations of chiral fermions in the SM representations";
  - :152: "One Higgs doublet $(\mathbf{1}, \mathbf{2}, +1/2)$";
  - :165: "Partition-spinor identification (Theorem 12) and trace-out (Theorem 13) give chirality.";
  - :169: "Each step (a)–(f) is a uniqueness statement";
  - :173: "Status: Theorem for the local lattice sector";
  - :201: the theorem returns "the generation count exactly three, one Higgs doublet";
  - :203: "the generation count" is among the invariants "*forced by representation theory given the
    lattice*".
- Passage B, `papers/SM.md`:
  - :543: Theorem 13 "(Chirality — conditional identification; minimal embedding certified vector-like;
    H-χ' sharpened, open)";
  - :468: "This theorem does **not** derive the existence of a Higgs doublet, nor its hypercharge";
  - :448: Theorem 9 "free-kernel identification refuted; H-spin' open".
- Same paper, qualified: Substratum:161 ("three physical generations only under H-spin'"), :193
  (Theorem 23 carries H-link, H-cust, H-spin′, H-χ′ and the $Y_Q = 0$ branch), and :199 (Higgs "taken
  as input").
- Scope of the proof: Theorem 23's own statement (:193) carries the conditions; the Stage 2 text and the
  remarks at :201 and :203 omit them.
- Class:
  - **direct contradiction** on chirality (:165 against SM:543);
  - **difference in assumptions** on generations and the Higgs (:151–152, :201, :203 against :161,
    :193, :199 and SM:468).
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC; LC (B-SUB-1).

**F-4. "No model-building choices" (S-8).**
- Passage A, Substratum:199: "no fitted parameters, no model-building choices, no landscape of
  alternatives at the level of the gauge sector".
- Passage B, `papers/SM.md`:1424: "the simple-cubic Bravais structure itself (Theorem 7b selects it
  *because* $\mathrm{SU}(3) \times \mathrm{SU}(2) \times \mathrm{U}(1)$ is observed …)"; and "'the
  Standard Model from a cubic lattice' and 'the lattice is cubic because $\mathrm{SU}(3)$ is observed'
  are the same fact stated in two directions".
- Scope: A is true given the lattice. B shows that the lattice input is selected by the structure A
  counts as evidence.
- Class: **difference in scope**. The overstatement is that A does not state that its lattice input is
  selected by the gauge structure it presents as evidence. Substratum:203 concedes part of this.
- Status: classified; stands (no correction made).
- Work: MC.

**F-5. Prediction counts (S-21).**
- Passage A, Substratum:525: "**1 is structural with no open link of its own** (B-S), **2 are
  conditional structural** (B-C), **6 are layered conditional** …".
- Passage B, `papers/SM.md`:1269–1316: 2 S and 5 C among 22 observables.
- Substratum:199 quotes B and attributes it to [SM §7.6], so :199 and :525 count different units and
  do not contradict each other.
- Mapping. Substratum's stated rule excludes inheritors: sin²θ₁₃ is "not counted separately in Class
  B" (:506), and |V_cb| is likewise an inheritor. The remaining residue has no stated mapping:
  - Koide Q (C in SM) appears only inside the B-M lepton entry (:513);
  - λ(M_Pl) = 0 (S in SM) appears only inside the B-M m_H entry (:514);
  - B-L lists a₀ (:507) where SM's L rows include m_b via Q_down.
- Class: **difference in scope**, with an unexplained residue.
- Status: classified; stands (no correction made).
- Work: MC (state the mapping).

**F-6. λ(M_Pl) = 0 classed S (SM-30).**
- Passage A: `papers/SM.md`:1293 (table row "composite Higgs … **S**");
  `book/appendix-a-prediction-status.md`:91 (row 22, S).
- Passage B:
  - SM:1116: "The Higgs is the $A_1$ taste — a composite scalar";
  - SM:468: Theorem 11 does not derive the Higgs doublet;
  - ledger B-SM-HIER-3: CD[composite Higgs, A₁ taste].
- Scope: the S definition (`book/appendix-a-prediction-status.md`:28) allows only H-spin′ and H-χ′ as
  the shared matter-sector conditions. The composite A₁ hosting of an input doublet is an additional
  link specific to this entry.
- Class: **difference in assumptions**.
- Status: classified; stands (no correction made).
- Work: MC; LC (the ledger is the more careful statement).

**F-7. Σm_ν "prediction" and neutrino–dark-energy coupling (G-15).** Re-anchored per the review.
- Passage A, `papers/GR.md`:410: "all three results match the OI predictions of normal ordering with
  $\Sigma m_\nu$ near the oscillation minimum of 0.059 eV"; and "both follow from the same lattice
  structure".
- Passage B:
  - `papers/SM.md`:1464: "The framework naturally produces $\Sigma m_\nu$ near the minimum allowed by the
    mass splittings", item (iv), a genericity heuristic (":1456 … two from genericity heuristics");
  - SM:1460: normal ordering "generically";
  - `book/appendix-a-prediction-status.md`:87 and :130 class Σm_ν L, Layer 3, "(oscillation inputs)".
- Scope: B is a heuristic for a hierarchical spectrum plus measured splittings. No derivation in any
  paper connects the neutrino sector to the running-vacuum coefficient.
- The internal SM pair :1464 / :1468 (absolute scale solution-specific) is a **difference in
  assumptions**, not a contradiction: the 0.059 eV figure uses measured splittings and a
  lightest-mass-near-zero heuristic.
- Class: **difference in assumptions**, plus a **single-source overstatement** in A's coupling
  sentence.
- Status: classified; stands (no correction made).
- Work: MC; LC (anchor to B-SM-NU-2, PE).

**F-8. PMNS forward commitments (SM-37, SM-33).**
- Passage A:
  - SM:1353: "The same construction forces the following";
  - SM:1360: "forced by the same cubic-group structure that produces the retrodictions, with no free
    parameter to adjust".
- Passage B:
  - SM:1290–1291 and footnote ᶠ: θ₁₂ and θ₂₃ classed L, "The values follow given Condition 2";
  - SM:1048: "The natural-normalization choice $b_{23} = 1$" (see F-29).
- Scope: the sum rule rests on Cond 2 alone (SM:1026, :1068); the individual values of θ₁₂ and θ₂₃ also
  rest on the normalization choice b₂₃ = 1; sin²θ₁₃ rests on the Cabibbo identification. SM:1112 states
  a concrete falsifier: "A lower-octant determination excludes the prediction." The second-order
  substrate route to Cond 2 is excluded (F-37).
- Class: **difference in assumptions**.
- Coverage: the values are covered by C-PRED-1 (appendix-a rows 12–14 and 19, N1–N3 and N6); the
  forward-test status (octant, the 0.005-level sum-rule measurement, θ₁₃ tightening) is not.
- Status: classified; stands (no correction made).
- Work: MC; LC.

**F-9. m_H statements (SM-34).**
- Passages:
  - SM:1118: "$\lambda(M_{\text{Pl}}) = 0$ gives $m_H \approx 129$–$132$ GeV … The observed
    $m_H = 125.10 \pm 0.14$ GeV is $4$–$7$ GeV below"; "consistent with observation within the current
    $m_t$ uncertainty";
  - SM:1126: "predicts $m_H \approx 128$–$132$ GeV … consistent with the observed … to $\sim 2$–$3\sigma$
    (reduced to $\lesssim 1\sigma$ for the CMS $m_t$)";
  - SM:1294 table: "$m_t$-consistent".
- The prediction lies above the observed value. (r1 inverted this; corrected.)
- Class: **manuscript-revision difference**: the same comparison is stated three ways, with different
  ranges.
- Status: classified; stands (no correction made).
- Work: MC.

**F-10. Lemma 1 status (M-29).** Withdrawn as a mismatch.
- Passages: `papers/Main.md`:700 (visible finiteness "stipulated"; holographic bounds "compatible …
  and are not premises"); `papers/GR.md`:585 ("Lemma 1 (independent in Part I; consequence of geometry
  in Part II)"); GR:90; `papers/SM.md`:46.
- Class: **difference in scope** (foundational layer against realization layer). GR:585 states the
  reconciliation.
- Status: no conflict (withdrawn).
- Work: none required. Optional MC: GR:90's "Lemma 1 is a consequence of partition geometry" is looser
  than GR:585.

**F-11. C2 "Satisfied" at the horizon (G-4).**
- Passage A, GR:48: "$\tau_B \gtrsim 1/H$ … **Satisfied.**"
- Passage B, GR:456: "the timescale ordering $\tau_B \gtrsim 1/H$ … which is not derived from the
  substratum dynamics".
- Class: **difference in scope** (a timescale identification against a derivation), with A worded
  more strongly.
- Status: classified; stands (no correction made).
- Work: MC; LC (§9 QM–Cosmology already records it).

**F-12. GR summary-table preamble (G-25).**
- Passage A, GR:536: "Each follows from partition geometry …; no predictions are fit to the quantities
  they predict."
- Passage B, GR:539–545: "factor imported", "partly definitional ($1-\Omega_B$)", two "in tension".
- Class: **difference in scope**. The preamble omits qualifications that its own table states.
- Status: classified; stands (no correction made).
- Work: MC.

**F-13. "No particle dark matter" (G-17; book K-3).**
- Passage A:
  - GR:454: "The corollary's prediction is that no particle dark matter exists";
  - `book/ch19-open-problems.md`:46: "Dark matter is not a particle — it is entropy displacement".
- Passage B:
  - GR:458: "The corollary is a consistency check for the total dark sector budget, not a derivation of
    its internal structure";
  - GR:530: "its effective density is taken as $\rho_E \approx \Omega_{\text{CDM}}\,\rho_{\text{crit}}$ —
    an input".
- Class: **difference in scope**, with A stronger than its support.
- Status: classified; stands (no correction made).
- Work: MC.

**F-14. Relaxation kernel (G-23).**
- Passages:
  - GR:524: "the same uncomputed kernel";
  - GR:526: "mode-by-mode relaxation is not computed";
  - GR:530: "a direct Boltzmann run implementing the displacement kernel explicitly … is the remaining
    numerical check";
  - GR:532 posits the epoch-local equation $d\delta_E/dt = (\delta_m - \delta_E)/\tau_{\rm relax}$ with
    $\tau_{\rm relax}(z) \sim 1/H(z)$ and reports a numerical check of that equation;
  - ledger B-COS-5: UO.
- Class: **difference in scope**. The microscopic kernel is uncomputed; an effective relaxation law is
  posited (PE).
- Status: classified; stands (no correction made).
- Work: LC; RO (the kernel).

**F-15. CMB initial conditions against "inflation not addressed" (G-24; book K-10).**
- Passage A, GR:530(iii): "it grows under its own gravity from adiabatic initial conditions set by
  inflation".
- Passage B, `book/ch19-open-problems.md`:194: "**Framework status.** Not addressed."
- Class: **difference in assumptions**. GR uses standard inflationary initial conditions as an
  unstated input.
- Status: classified; stands (no correction made).
- Work: MC (state it as an input); LC.

**F-16. A displayed bidirectional correspondence (§A.34) (S-24).**
- Passage, Substratum:231–233: "The reconstruction establishes a bidirectional correspondence for the
  **local reconstructed residue**", displayed as (E1–E7) + (A1–A6) ⟷ $[(S,\varphi)]_{\rm loc}/\mathcal{G}_{\text{sub}}$.
- The two directions:
  - data and assumptions → class: Theorem 23 (:193), a uniqueness and reconstruction statement under its
    conditions;
  - class → data: no separate witness. This would need a forward derivation of E1–E7 from the class,
    and the corpus has none:
    - E1 (QM) is an input (ledger A-QM, UO);
    - E2 needs H-Bell (open);
    - E5 (propagating gravity) needs G3 (open);
    - the SM-side forward chain is conditional (H-link, H-cust, H-spin′, H-χ′).
- Under §A.34, uniqueness is not a converse.
- Class: **single-source overstatement of directionality**.
- Status: classified; stands (no correction made).
- Work: MC; LC.
- Search for other displays: the five papers were searched for "longleftrightarrow", "⟷", "⟺",
  "\iff" and "bidirectional". The other equivalence displays found are:
  - Main's S ⟺ D ⟺ Q_fb, with directional kernel witnesses named at Main:97;
  - Main's (ii) ⟺ (iii), both directions proved in-house (Main:628);
  - GR's boxed operational equivalences: GR:222 ("(i)–(v) ⟺ finite operational QM", ledger B-QM-3),
    GR:236 ("OI⁺ ⟺ …", B-QM-6), and GR:252, 258, 264 and 274, each citing kernel biconditionals or
    directional pairs;
  - Main:586, a display of the OI⁺ equivalence (B-QM-6);
  - Main:617, "accessible non-Markovianity ⟺ a per-horizon finite reversible deterministic realization
    exists", which Main:618 itself declares false (Markov laws are realized too); it is displayed in
    order to be rejected, not asserted;
  - Substratum:112 and :127, which restate Main.

  SM and Structure contain no displayed equivalence. SM's inline theorem biconditionals (for example
  Theorems 3 and 16) are carried by ledger rows B-SM-10 and B-SM-11.

  The kernel statements were not opened (§10).

**F-17. Structure on the gauge group and the level of the dark sector (T-17, T-6).**
- Passage A:
  - Structure:703: "OI's substratum produces $SU(3) \times SU(2) \times U(1)$ uniquely";
  - Structure:179: dark-sector phenomenology at Level G3 × D, "forced by OI's specific" structure.
- Passage B:
  - SM:14 and :1424 (lattice selected by the observed group; H-link and H-cust);
  - Structure:191: "*[SM]:* Level D × Levels G1–G2", against :179's placement of Cabibbo and Koide at
    G3 × D;
  - Structure:192: "*[GR]:* Level D × Levels G1–G2";
  - GR:30.
- Class: **difference in assumptions** (:703 omits H-link, H-cust and the selection);
  **direct contradiction** within Structure (:179 against :191 and :192).
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC.

**F-18. "No fundamental moduli … parameters derived" (T-3).**
- Passage A, Structure:417: "the emergent QFT's parameters are derived from the cubic-lattice
  structure rather than being moduli to be selected".
- Passage B:
  - SM:1396: solution-specific properties include "gauge couplings at $M_Z$ (set by the threshold
    $\delta_0$ and the resummation parameters $A, B$, matched …)";
  - SM:1440: Layer 3 "absolute fermion mass scales … CP".
- Class: **direct contradiction**.
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC.

**F-19. Majorana neutrinos stated without the branch condition (T-3, T-16).**
- Passage A:
  - Structure:403: "OI's [SM §8.4] predicts Majorana neutrinos";
  - Structure:1317: "predicts Majorana neutrinos, so $0\nu\beta\beta$ should be observed".
- Passage B, SM:1452: "On the branch where the singlet taste hosts the Higgs (Theorem 11, taken as
  input) and no gauge-singlet fermion …".
- Class: **difference in assumptions**.
- Status: classified; stands (no correction made).
- Work: MC. The missing sensitivity target (T flag, SM-41) is RO.

**F-20. Scope of the matrix-model negative (T-1, T-2).**
- Passage A:
  - Structure:13: "The substratum-level equivalence reading does not hold.";
  - Structure:369: "both programs cannot be foundational descriptions of the same physics
    simultaneously".
- Passage B:
  - Structure:351: "do not satisfy OI's structural conditions A1–A6 in their standard formulation";
  - Structure:242: "The provisional conclusion is (c)";
  - Structure:337–347: five partial recoveries.
- Scope: a paper-level argument about BFSS and IKKT in their standard formulation.
- Class: **difference in scope**.
- Status: classified; stands (no correction made).
- Work: MC; LC (B-STR-1).

**F-21. Doublers as generations (SM-21).**
- Passage A, SM:567: "the 'wrong-chirality' doublers that NN forces upon a fermionic lattice action
  become, in OI, the physical generations (Theorem 9)".
- Passage B, SM:448: Theorem 9, "free-kernel identification refuted; H-spin' open".
- Class: **direct contradiction**.
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC.

**F-22. Mass gap "does not affect any prediction" (SM-40, S-9).**
- Passage A:
  - SM:1448: "it does not affect any prediction of the OI framework";
  - SM:1448: "the structural predictions are exact theorems at the lattice level";
  - Substratum:225: structural results "are exact".
- Passage B:
  - SM:801: whether the induced theory "is in the deconfined phase required for the perturbative
    matching to be valid";
  - SM:803–811: the Haar-measure theory confines; the identification of the measure is open;
  - the named conditions (H-link, H-cust, H-spin′, H-χ′).
- Class: **difference in scope**. A is stated for the lattice's structural results; B bears on the
  validity of the coupling matching. Whether the nonperturbative phase affects the coupling predictions
  is **unresolved**.
- Work: MC; RO (#1063 records the planning; ledger Q14).

**F-23. "Forced … no parameters fit" and "six masses from one input" (SM-44, SM-31).**
- Passage A:
  - SM:14: "These predictions are forced by the cubic-lattice geometry and contain no parameters fit to
    the predicted quantities";
  - SM:847: "All predictions follow from the cubic-lattice geometry";
  - SM:14 and :1588: "six fermion masses from a single empirical input";
  - SM:989: "The structural relations link all light fermion masses through a single input ($m_s$)".
- Passage B:
  - SM:971: "Taking $Q_{\text{down}}$ … as a phenomenological input";
  - SM:887: GST "an external empirical relation … the conversion to $m_d/m_s$ inherits GST's empirical
    status";
  - SM:1215: K = 1/2 by "empirical fitting on a moderately-restricted set rather than a first-principles
    derivation";
  - SM:1276–1296 table: E, R and P rows.
- Class: **single-source overstatement within SM**. The chain has additional empirical and
  phenomenological inputs.
- Status: classified; stands (no correction made).
- Work: MC.

**F-24. GST relation: corollary or external (SM-29).**
- Passage A, SM:863: "the GST relation [21] follows as a corollary".
- Passage B, SM:887: "The GST relation [21] is an external empirical relation in flavor physics … the
  conversion to $m_d/m_s$ inherits GST's empirical status."
- Scope: :863 gives a scaling argument (two propagator insertions), not a derivation.
- Class: **direct contradiction** within one section.
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC.

**F-25. Wolfenstein A: identification asserted, class S (SM-29, SM-30).**
- Passage A:
  - SM:871: "The CKM mixing is driven by the perpendicular component: $A = \sin\theta$";
  - SM:1279: class **S**.
- Passage B, SM:881: "identifying the measured Wolfenstein $A$ with the geometric value is a
  leading-order statement whose correction is the same open object as the Condition-2 ratio".
- Scope: the geometric angle is exact; its identification with the CKM parameter has no derivation, as
  with the Cabibbo identification (SM:865, a "hypothesis, not a derivation").
- Class: **difference in assumptions**. Ledger B-SM-FLAV-1 (CD, one named open link) is the more
  careful statement.
- Status: classified; stands (no correction made).
- Work: MC; LC.

**F-26. Koide angle: normalization selected by match (SM-31).**
- Passage A:
  - SM:936: "Only 2/9 matches";
  - SM:940: "the unique match to observation".
- Passage B:
  - SM:944: "A first-principles derivation of the specific $1/d$ amplitude scaling … remains an open
    task";
  - SM:946–952: the resolving computation is specified and not performed.
- Class: **difference in assumptions**. The selection among enumerated ratios by observation is an EF
  element that the C class does not record.
- Status: **unresolved** (the computation is open).
- Work: LC; RO.

**F-27. Reactor-angle route uses its own target (SM-33).**
- Passage A, SM:1036: three constraints, including "the correct $\sin^2\theta_{13} = 4\lambda^2/9$
  coefficient — uniquely determine" $A_1$.
- Passage B, SM:1034: $\sin\theta_{13} = A^2\lambda$, derived by a path sum with
  $\alpha = \sqrt{C_2}/d$. α is the natural amplitude whose $1/d$ normalization is open (SM:944).
- Class: **difference in assumptions**. One route takes the target as input; the other rests on the
  open normalization.
- Status: **unresolved**: which route is load-bearing for "independent of Condition 2" (SM:1026) is
  not stated.
- Work: MC; LC.

**F-28. An unflagged PMNS normalization premise (SM-33).**
- Passage A, SM:1048: "The natural-normalization choice $b_{23} = 1$ — corresponding to $A_2$ entering
  the perturbation series at unit strength". Together with Cond 2 it yields
  $b_{12} + b_{13} = \tfrac34$ (SM:1056), which fixes θ₁₂ and θ₂₃.
- Passage B: SM table footnote ᶠ and `book/appendix-a-prediction-status.md`:96 name only Condition 2
  as the open link.
- Class: **difference in assumptions** between the derivation and its classification.
- Status: **unresolved** (the normalization is not derived).
- Work: LC; MC; RO.

**F-29. m_u/m_d data values (SM-31).**
- Passages:
  - SM:981: "The PDG value [20] is $m_u/m_d = 0.474 \pm 0.056$. Match: $0.05\sigma$";
  - SM:1289 table: "0.465 ± 0.024 | 0.27σ";
  - SM:1335: "0.474";
  - `book/appendix-a-prediction-status.md`:86: "Within 1σ".
- Class: **manuscript-revision difference**.
- Status: classified; stands (no correction made).
- Work: MC.

**F-30. m_b/m_τ matching mass: "derived" against "empirical fitting" (SM-35).**
- Passage A, SM:1152: "The matching scale is derived in the taste-decomposed Coleman–Weinberg
  potential".
- Passage B:
  - SM:1160: $m_{\text{match}} = 2K\lambda g_0^2$ with K unknown;
  - SM:1215: "This is empirical fitting on a moderately-restricted set rather than a first-principles
    derivation";
  - SM:1219: "the analytical residual is a controlled derivation of $m_{\text{match}} = \lambda g_0^2$";
  - SM:1172 calls $K = 1/2$ "a representation-theoretic structural identity, not a numerical
    happenstance", while SM:1196 says the Layer 1 components fix $K = 1/2$ only "as the value the loop
    calculation *must* yield for the framework's matching prediction to hold";
  - the MC uses the standard Haar measure (SM:813; ledger B-SM-NP-1).
- Scope: the form is argued; the coefficient comes from data selection and MC.
- Class: **difference in scope**, with A worded more strongly.
- Status: **unresolved** (the analytical K is open).
- Work: MC; LC; RO.

**F-31. Book: anomaly cancellation "forces" three sectors (K-1).**
- Passage A, `book/ch19-open-problems.md`:106: "anomaly cancellation forces exactly three candidate
  matter sectors".
- Passage B, SM:458: "anomaly cancellation fixes charges given the sector pattern; the selection of the
  observed family pattern … is not supplied by either".
- Class: **direct contradiction**.
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC.

**F-32. Book: "derives exactly one scalar doublet" (K-2).**
- Passage A, ch19:196: "The framework derives exactly one scalar doublet".
- Passage B, SM:468: "This theorem does **not** derive the existence of a Higgs doublet".
- Class: **direct contradiction**.
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC.

**F-33. Book: "derives the total budget" (K-4).**
- Passage A, ch19:118: "The framework derives the total budget".
- Passage B:
  - ch19:116: "the total fraction is partly definitional, equal to $1-\Omega_B$ by construction";
  - GR:541: "partly definitional".
- Class: **direct contradiction** within the chapter.
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC.

**F-34. Appendix-a biology rows classed S against the chapters' conjectural status (§5).**
- Passage A, `book/appendix-a-prediction-status.md`:145–158: eleven rows S, Layer 1 (B1, B2,
  B6–B14). B3 (ch13 §13.6) is moved out of this finding: chapter 13 carries no "conjectural extension"
  notice, and the conjecture at ch13:140 concerns distinguishability revival, not B3's enzyme kinetics.
  B3's S label was not checked against ch13 §13.6, which was not read (§10).
- Passage A′, :28: S means "no fitted input and no open link specific to the entry".
- Passage B:
  - `book/ch16-medicine.md`:6: "**Status — conjectural extension.** … offered as a *conjecture*, not an
    established result";
  - `book/ch17-bioinformatics.md`:6: the same notice;
  - ch17:172: the prediction is that $R(t)$ "must exceed 1"; the value $R(t) \approx 5$ (ch17:174) is
    the observed value, which row B6 lists as the quantitative content.
- Class: **direct contradiction** between the label and the chapters' own status (ch16, ch17).
- Status: classified; stands (no correction made). The individual derivations were not audited (§10).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC; LC.

**F-35. Appendix-a row 1: 1/α₀ classed S (§5).**
- Passage A, `book/appendix-a-prediction-status.md`:70: "S | 0".
- Passage B, SM:793: "it depends on $N_f=6$ (conditional on single-copy H-link, Theorem 6)"; ledger
  B-SM-GAUGE-1: CD.
- Class: **difference in assumptions**.
- Status: classified; stands (no correction made).
- Work: MC.

**F-36. Appendix-a N5 classed C (§5).**
- Passage A, :131: "Normal mass ordering | structural … | C".
- Passage B, :135: "the ordering a heuristic consequence of taste-breaking rather than a theorem";
  SM:1460.
- Class: **direct contradiction** between the label and the row's own note.
- Status: classified; stands (no correction made).
- Manuscript-correction candidate: the direct contradiction is still in the manuscript as quoted.
- Work: MC.

**F-37. Excluded routes to Cond 2: a negative result missing from the ledger (SM-47).** (r3)
- Passages, SM:
  - :1026: the substrate calculation "excluded the second-order route — demoting it to Layer 2(b)";
  - :1076: "The second-order substrate route to it is excluded …, so the ratio is Layer 2(b), with the
    $7/6$ sum rule as its direct experimental test and the $O(\lambda^3)$ interference route recorded,
    not pursued";
  - :1084: the same exclusion;
  - :1088–1094: the natural-form Yukawa gives $b_{12} : b_{13} : b_{23} = m_\tau/m_\mu : 1 : 1$;
    Cond 2's symmetric split needs "a different scaling";
  - :1108: "The projection $\rho$ is therefore not small but exactly zero …: the substrate dressing chain
    is retired. Condition 2 accordingly stands as what the construction always declared it to be — a
    stated condition"; "first-order-squared effects are excluded by the spectrum-dominance computation,
    and the geometric second-order route is excluded by monomial orthogonality"; "The second-order route
    is thereby closed in the negative".
- Appendix-a footnote ᶠ (:96) records the Layer 2(b) status.
- Scope: a paper-level computation within the hop model, with declared inputs: the hop model, the
  projection ρ and the neglect of the $O(\lambda^3)$ interference. SM:1108 adds that the substrate
  form of Cond 2 "holds as a $\lambda \to 0$ statement, and a test at physical $\lambda$ requires exact
  diagonalization rather than the strict second-order extraction". The negative is therefore scoped to
  the strict second-order extraction in that model. It is not a no-go for Cond 2: the $O(\lambda^3)$
  route is untried.
- Ledger r3 cites no line in SM:1026–1112.
- Class: missing coverage of a negative result (condition 3 requires negative results to be recorded).
  There is no conflict between documents.
- Status: classified; stands. Whether any route derives Cond 2 is **unresolved** (an RO, as in F-28).
- Work: LC (proposed B-SM-FLAV-10); RO (the $O(\lambda^3)$ route, or exact diagonalization).

**F-38. The sum-rule match read as evidence of the mechanism (SM-33).** (r3)
- Passage A:
  - SM:1110: "the match indicates the framework's bijection has the alignment property required by
    Cond 2 — equivalently, that the substrate-level mechanism producing the $4(d-1)/(2d)$ amplitude
    ratio is realized in the bijection";
  - SM:1100: "the empirical match indicates this is realized in the framework's bijection";
  - SM:1092: "The framework's bijection therefore has structure beyond the natural cubic-symmetric
    form".
- Passage B:
  - SM:1108: the mechanisms examined are excluded, and Cond 2 "stands as … a stated condition";
  - SM:1349: the values were known before the framework, so the matches are retrodictions;
  - SM:1084: the match "tests the bijection's specific operator structure … conditional on the
    atmospheric octant".
- Scope: the match of 1.178 ± 0.020 to 7/6 is a retrodiction, and the source supplies no mechanism.
  The inference from match to realized mechanism holds only if Cond 2 is taken as true, and SM:1108
  leaves it a stated condition.
- Class: **single-source overstatement** within SM (an unsupported intermediate inference).
- Status: classified; stands (no correction made).
- Work: MC.

### 3.2 Single-source overstatements (flag O, no conflicting second passage)

Each line gives the claim, then what supports it at source.

| Entry | Claim (location) | Actual support at source | Work |
|---|---|---|---|
| M-33 | "quantitative predictions" (Main:704) | none in Main | MC |
| S-1 | "Both are derived rather than fundamental" (Substratum:389) | Einstein equations imported (GR:162); recasting conditional on G3 (Substratum:423) | MC |
| S-2 | "does establish … derived from the same object by the same procedure under the same conditions" (Substratum:421) | ledger §9 GR–SM undetermined; geometry order open (Q4) | MC |
| S-3 | "The dark sector is the gravitational effect of the unreadable storage" (Substratum:46) | conditional, partly definitional (GR:452, :540) | MC |
| S-10 | weak ER=EPR recovered "as a structural consequence of the framework's holographic architecture" (Substratum:239) | no holographic dictionary is supplied; Structure:463 assesses that OI "does not naturally produce full AdS/CFT-style correspondence" | MC |
| S-17 | "generates every concept in fundamental physics" (Substratum:459) | G3 open | MC |
| S-19 | Class A "structural theorems" (Substratum:475–479) | generations on H-spin′; gauge reading on H-link, H-cust | MC |
| G-2 | "the counting $S = \sigma A/\epsilon^2$ itself unconditional" (GR:12) | the partition presupposes GR causal structure (GR:40) | MC (ledger B-GR-1 records it) |
| G-30 | "(a) *Unconditional.*" (GR:615) | (U1) uses Jacobson and H-count; S1 presupposes a horizon | MC |
| SM-36 | "strong evidence for the underlying $C_2/d$ identity" (SM:1339) | one row "via Cond 2"; values known beforehand (SM:1349) | MC |
| T-4 | "any horizon entropy in OI's framework is bounded by $A/4$ under the conditions of the horizon calibration" (Structure:453) | calibration equality only; GSL open (GR:781) | MC |
| T-9 | pair "captures … gauge couplings at $M_Z$, Yukawa structure producing CKM/PMNS" (Structure:813) | fitted thresholds; solution-specific Yukawas (SM:1396, :1440) | MC |
| T-12 | "moderately favors the no-GUT universality class" (Structure:970) | not unique to OI (SM:841) | MC |
| T-5, T-6, T-3 | see F-2, F-17, F-18 and F-19 | | |

## 4. Per-paper tables

The columns and codes are as in §1. Entries changed from r1 are marked "(r2)".

### 4.1 `papers/Main.md`

| ID | Location | Claim (paraphrase) | Ledger row | Code | Notes |
|---|---|---|---|---|---|
| M-1 | 14–18, 97, 546–552, 600(1), 642, 764–768 | S ⟺ D ⟺ Q_fb on every finite horizon; exact and universal | B-QM-1 | C | Kernel, directional witnesses at :97 |
| M-2 | 16, 600(2), 602–618 | C4 ⟺ M_t > 0; unavoidable hidden predictive memory | B-QM-2 | C | |
| M-3 | 171–174, 536–542, 628–636, 696, 731–733 | Characterization (ii) ⟺ (iii); readback lemma | B-QM-2 | CB | |
| M-4 | 486, 492–496, 638 | Three negatives: no uniform finite realization; no horizon-independent intervened representation at fixed d; no exact all-time realization | none | U | NEG; LC |
| M-5 | 109–143, 157 | Recurrence P-indivisibility; stochastic inverse; rooted and overlap-and-return theorems | B-QM-16 | C | |
| M-6 | 147–151 | The C1 witness is generic among bijections | none | U | LC; bears on F-2 |
| M-7 | 159–169, 443–476, 498–502, 736 | Fast-bath lemma; C2 necessity in mixing and process forms | input (v) | U | LC |
| M-8 | 76, 504–512, 737 | C3 necessity m ≥ 2^{I*}; horizon realization numbers | input "C1–C4" | U | LC |
| M-9 | 182–200 | Six-hidden-state model | B-QM-16 | CB | |
| M-10 | 206–216, 352–356, 526–534, 656, 730 | Barandes ≤ n³ compression under (T); ancilla dilation | none | U | LC |
| M-11 | 226–260, 716 | Phase-locking under (G1)–(G4); ancilla-marginal phase-locking for listed blocks | §2.3 lists (G1)–(G4) | U | LC |
| M-12 | 262–290, 342–352 | Stinespring route; C1 alone gives measure-and-prepare | B-QM-1 | CB | |
| M-13 | 292–324, 778 | Separability threshold; non-entanglement-breaking iff w < κ | B-P4-QCB-3 (reading only) | U | LC |
| M-14 | 326–340, 734 | CP-indivisibility for the permutation-dilation family; approximate unitarity | none | U | LC |
| M-15 | 356, 562, 584–588, 646–650 | Operational completion; (iv) not supplied; OI⁺ | B-QM-3 to B-QM-6 | C | |
| M-16 | 358–427, 770 | Cone; CHSH ≤ 2; lattice obstruction; measurement-dependence bound; PR laws | B-BELL-1 to B-BELL-6 | C | |
| M-17 | 478–484, 556, 682 | Intervention-dilation comb; double-slit family realized | B-P4-MEAS-5 (other part) | U | LC |
| M-18 | 558–560, 600(3) | Classical-dimension obstruction | B-QM-8 | C | |
| M-19 | 564–582, 594–598, 772 | Gluing ε-form; mutual ε-density | B-QM-7 | C | |
| M-20 | 590–592 | Passive observation complete iff commutative; non-discriminating | none | U | LC |
| M-21 | 620–622 | Canonical predictive quotient | none | U | LC |
| M-22 | 20, 644 | Relating evolution not selected | B-QM-10 | C | |
| M-23 | 18, 286, 554 | Born exponent not selected | B-QM-11 | C | |
| M-24 | 660–674 | Rest-frame selection by a horizon partition | none | U | LC |
| M-25 | 684–692 | Wigner's friend | B-P4-MEAS-2, B-P4-MEAS-3 | C | |
| M-26 | 652, 692 | Measurement as conditioning | B-P4-MEAS-1 | C | |
| M-27 | 718–722 | No memory-witness falsifier at present | C-PRED-9 | C, T | RO (a test) |
| M-28 | 740–758 | Observer selection under (EM) | B-P4-AOT-2, C-OBS | C | |
| M-29 (r2) | 46, 700, 712 | Lemma 1: visible finiteness stipulated at the foundational layer | §1 (ii)/A1; §2.2 | CB | F-10: no conflict |
| M-30 | 44 | Map form from composition | §1 (A2) | CB | |
| M-31 | 64 | Reversibility orthodox | §1 (iii)/A2 | CB | |
| M-32 | 84–90 | Partition-relativity lemma | none | U | LC |
| M-33 | 704 | "quantitative predictions" | none | U, O | §3.2 |

### 4.2 `papers/Substratum.md`

| ID | Location | Claim (paraphrase) | Ledger row | Code | Notes |
|---|---|---|---|---|---|
| S-1 | 14, 22–26, 371–397, 417–423, 548–550 | QM and GR are two projections; the unification problem is a category error | none | U, O, T | §3.2; LC (B-SUB-3) |
| S-2 | 421 | The synthesis "does establish" a common derivation | none | U, O | §3.2 |
| S-3 | 46 | Storage identifications of the 10¹²² ratio, dark sector and ħ | B-CC-1, B-COS-3, B-GR-2 | CM, O | §3.2 |
| S-4 | 76–104, 205–223 | Inputs E1–E7, A1–A6 | §1 | C | |
| S-5 | 121–141 | Stage 1 | B-BELL-8, §1 | CB | |
| S-6 | 131–135, 171 | H-Bell; mixing hypothesis open | B-BELL-7, input (v) | C | |
| S-7 (r2) | 147–173, 189–195, 201, 203 | Stage 2, Lemma 23.0, Theorem 23 | B-BELL-8; B-SM-1 to B-SM-8 | CM, O | F-3 (locations :201, :203 added; :161 qualified) |
| S-8 | 199 | "no fitted parameters, no model-building choices" | B-SM-4 | CM, O | F-4 |
| S-9 | 225–227 | Structural results "exact"; mass gap set aside | B-QCD-6 | CM, O | F-22 |
| S-10 (r2) | 237–243 | ER=EPR weak form recovered; strong form "predicted *false*" | none | U, O, T | §3.2 (O added) |
| S-11 | 247–300, 429 | Theorem 24 generators; completeness open | none | U | LC |
| S-12 | 278–284, 302–361 | Props 24.2–24.5 | none | U | LC |
| S-13 | 270–274 | Amplitude-scale gauge adjoined | §1 (vii)/A5 | C | |
| S-14 | 175–185 | Stage 3 ħ relation | B-GR-2 | C | |
| S-15 | 56, 399–413 | Arrow-of-time projection | B-P4-AOT-1 to B-P4-AOT-5 | C | |
| S-16 | 415 | Flavour CP phases solution-specific | B-SM-FLAV-4 | C | |
| S-17 | 459 | "generates every concept" | none | U, O, T | §3.2 |
| S-18 | 461–467 | Measurement; no branching | B-P4-MEAS-1, B-P4-MEAS-4 | C | |
| S-19 | 475–480 | Class A falsifiers for gauge group and generations | C-PRED-1 | CM, O | §3.2 |
| S-20 | 481 | Bell/Tsirelson falsifier | A-BELL, B-BELL-1 | C | |
| S-21 (r2) | 486–527 | Class B counts | B-SM-FLAV-5, C-PRED-1 | CM | F-5 (re-classed: scope, residue) |
| S-22 | 529 | BH coefficient a consistency relation | B-GR-2, C-PRED-7 | C | |
| S-23 | 54, 92, 533–542 | Effective finiteness; Class C; deliberate silence | §1, B-COS-3, C-OBS, C-EARLY-1, C-EARLY-4 | CB | |
| S-24 (r2, new) | 231–235 | "bidirectional correspondence" display | §1 (Theorem 23 "uniqueness"), B-BELL-8 | CM, O | F-16 (§A.34) |

The form lemma (Substratum:48, 159) and Jordan–Chevalley (Substratum:62) are counted under SM-2 and
SM-43.

### 4.3 `papers/GR.md`

| ID | Location | Claim (paraphrase) | Ledger row | Code | Notes |
|---|---|---|---|---|---|
| G-1 | 12, 24, 78–82, 102, 108–160, 300–306, 625–627, 651 | ħ relation by thermal self-consistency | B-GR-2 | C | |
| G-2 | 12, 28, 156, 310–316, 619, 629, 653 | Count "unconditional"; S = A/(4l_p²) | B-GR-1, B-GR-2 | CM, O | §3.2 |
| G-3 | 38–42, 340–348 | Horizon as the partition; ħ observer-universal; geometry first | B-GR-1, B-CC-1, Q4 | CB | |
| G-4 (r2) | 44–52, 456, 661–663 | C1–C3 "Satisfied"; C4 not discharged | §1, §9, M7 | CM, O | F-11 |
| G-5 | 58–92 | Selection conditions H-count, H-balance, H-slope | §4.3, B-GR-7 | CB | |
| G-6 | 112–138 | Boundary-only dependence; deep-sector cardinality gauge | none | U | LC |
| G-7 | 162, 691 | Einstein equations imported | B-GR-3 | C | |
| G-8 | 166–210, 292–296 | Bohr-frequency, D-gauge (H-BG), classification, orientation no-go | none | U | LC |
| G-9 | 212–276 | Completion, OI⁺, source, layer-flow and typed forms | B-QM-3, B-QM-5, B-QM-6, B-QM-15 | CB | |
| G-10 | 278–290 | Quasilocal completion; continuous extension not unique | B-QM-9 | C | |
| G-11 | 326–336 | H-local-lift locality | §6.3, M1 | CB | |
| G-12 | 338–362 | CC distinction; decoupling on G3 | B-CC-1 to B-CC-3 | C | |
| G-13 | 567–581 | Higgs and QCD vacuum; binding gravitates | B-CC-4, C-QCDVAC | C | QCD-group check |
| G-14 | 372–408, 412 | RVM reading; \|ν\|; DESI tests | B-COS-1, B-COS-2, C-PRED-5 | C | |
| G-15 (r2) | 410, 524 | Σm_ν "OI predictions"; coupling to RVM | B-SM-NU-2 | CM, O | F-7 (re-anchored) |
| G-16 | 414–452, 458–460 | Dark-sector corollary | B-COS-3, D5 | C | |
| G-17 | 454 | "no particle dark matter exists" | B-COS-3 | CM, O | F-13 |
| G-18 | 462–486, 506 | a₀ = cH/6; BTFR | B-COS-4 | C | |
| G-19 | 488–504 | Interpolation constraints | none | U | LC |
| G-20 | 508–522, 536–545 | a₀(z) evolution; tensions | C-PRED-6 | CB | |
| G-21 | 512 | Tully–Fisher evolution tension | none | U | NEG; LC |
| G-22 | 524 | Rich-cluster residual | none | U | NEG; LC |
| G-23 | 524–532 | Bullet; epoch-local kernel | B-COS-5 | CM, T | F-14 |
| G-24 | 528–530 | CMB match given ρ_E input | none | U | F-15; LC |
| G-25 (r2) | 536 | "no predictions are fit" | B-COS-3, B-COS-4 | CM, O | F-12 |
| G-26 | 318, 547, 597 | GW250114; no echoes | C-PRED-7 | C, T | |
| G-27 | 589–595, 607 | Falsifiability notes; analogue tests | C-PRED-9 | CB, T | |
| G-28 | 599–605, 709–751, 769–866 | Nested trace-outs; GSL; Page curve | B-GR-9, B-BH-3 to B-BH-7 | C | |
| G-29 | 753–767, 785–795 | Theorems A.5, A.7 | none | U | LC |
| G-30 | 609–679 | Universality theorem | none | U, O | §3.2; LC |
| G-31 | 689–697 | Kinematic emergence; Newtonian limit | B-GR-5 | C | |
| G-32 | 104 | K = 6 against one mode per cell "forced" | none | U | rides H-link; LC |
| G-33 (r2, new) | 551 | A DESI detection of \|ν\| ~ 10⁻⁴ would need emergent non-locality and so a correlated Lorentz-violation signature | ledger §7.3, §7.5 (GR:400) | CB | A cross-sector test claim; conditional on the locality analysis |
| G-34 (r2, new) | 587 | Recurrence P-indivisibility carries over to a finite representative of the constraint surface | none | U | LC |

### 4.4 `papers/SM.md`

| ID | Location | Claim (paraphrase) | Ledger row | Code | Notes |
|---|---|---|---|---|---|
| SM-1 | 12, 26, 32, 218, 242–282 | Theorem 1a; Cors 1a and 1b; Theorem 1 | B-SM-9 only | U | LC |
| SM-2 | 224–232; Substratum:48, 159 | Wave-equation form lemma | none | U | LC |
| SM-3 | 104–118 | Graph G(x); local gauge invariance from A6 | §1, §9 | CB | |
| SM-4 | 120–124, 150, 160–164 | Area-law lemma; thermality corrections | B-GR-4 | CB | |
| SM-5 | 126–138, 1448; Substratum:482–484; GR:639–649 | Emergent Lorentz; LIV 4σ/45; rotational sector open | none | U | LC; RO (radiative protection) |
| SM-6 | 132 | Leptoquark sector; M_X window | none | U | LC |
| SM-7 | 140–142 | Lattice BW | B-GR-8 | C | |
| SM-8 | 144–158 | Discrete Einstein target form | B-GR-4 | C | |
| SM-9 | 170–212 | d = 3 filters | B-SM-5 | C | |
| SM-10 | 198, 601–607 | Theorem 16 | B-SM-11, B-QCD-4 | C | |
| SM-11 | 284–298 | Theorem 2; measure gap; cycle structure | input (v), B-SM-FLAV-3 | CB | |
| SM-12 | 300–308 | Theorem 3 | B-SM-10 | C | |
| SM-13 | 310–344 | Theorems 4, 5; Lemma 4a; Prop 4b | B-SM-2, B-SM-3 | CB | |
| SM-14 | 346–370, 64–74 | H-link; Lemma 6a; Theorem 6 | B-SM-2 | C | |
| SM-15 | 372–388 | Theorem 7 | B-SM-1 | C | |
| SM-16 | 390–416 | Theorem 7b | B-SM-4 | C | |
| SM-17 | 418–426 | Irrep catalogue "accounted for" | none | U | LC |
| SM-18 | 430–456 | Theorems 8–10; H-spin′ | B-SM-6 | C | |
| SM-19 | 464–470 | Theorem 11: Higgs taken as input | B-SM-12 | CB | |
| SM-20 | 472–533 | Gauge bosons from the Schur complement; matter on links | B-QCD-2 | C | |
| SM-21 | 535–571 | Theorems 12, 13; NN "bypassed"; doublers as generations | B-SM-7 | CM, O | F-21 |
| SM-22 | 573–599 | Theorems 14, 15; Cor 15b | B-SM-8 | CB | |
| SM-23 | 609–613, 1538–1582 | Higgs mechanism; chiral protection | B-SM-12, B-SM-HIER-1, B-SM-HIER-2 | C, T | |
| SM-24 | 621–671 | Strong CP | B-SM-CP-1 to B-SM-CP-3 | C | |
| SM-25 | 675–717, 769–797, 815–817 | Induced coupling; δ₀; non-unification | B-SM-GAUGE-1, B-SM-GAUGE-2 | C | |
| SM-26 | 717–767 | A·B | B-SM-GAUGE-2 | C | |
| SM-27 | 799–813 | Confinement question | B-SM-GAUGE-3, B-SM-GAUGE-4, B-SM-NP-1, B-SM-NP-2 | C | |
| SM-28 | 819–841 | No GUT | C-EARLY-3, C-PRED-3 | C | |
| SM-29 (r2) | 849–903 | CKM: Cabibbo (named hypothesis); A; m_d/m_s; J | B-SM-FLAV-1, B-SM-FLAV-5 | CM, O | F-24, F-25 (§6 sample) |
| SM-30 | 1269–1316 | λ(M_Pl) = 0 and A classed S | B-SM-HIER-3, B-SM-FLAV-5 | CM, O | F-6, F-25 |
| SM-31 (r2) | 905–1003 | Koide Q and θ₀; mass chain; m_b via Q_down; m_u/m_d | B-SM-FLAV-1, B-SM-FLAV-2, B-SM-FLAV-5 | CM, O | F-23, F-26, F-29 |
| SM-32 | 1004–1008, 1126 | y_t(M_Pl) = 1 gives m_t ≈ 207 GeV | B-SM-FLAV-5 | CB | NEG not recorded; LC |
| SM-33 (r3) | 1010–1112 | PMNS; Cond 2; JUNO; the sum-rule match read as showing that the mechanism "is realized in the bijection" (1092, 1100, 1110) | B-SM-NU-1, B-SM-FLAV-5, C-PRED-1 | CM, O | F-27, F-28, F-38 |
| SM-34 (r2) | 1114–1128 | λ(M_Pl) = 0 gives m_H ≈ 129–132 GeV; observed is 4–7 GeV below | C-PRED-2 | CM | F-9 (direction corrected) |
| SM-35 (r3) | 1130–1267 | m_b/m_τ; K by data and MC; bridge theorem | B-SM-FLAV-3 | CM, O | F-30. The bridge theorem's γ₀ part is Level 2 with sign conventions "not separately verified" (1237, 1249), while :1229 calls the gaps "**Closed at Level 1 framework-essentially via the explicit theorem below**" and :1257 says γ₀ is "derived rather than independent"; parts (b, γ₀) and (d) are Level 2 (1249, 1253) |
| SM-36 | 1324–1346 | Casimir table "strong evidence" | none | U, O | §3.2 |
| SM-37 (r2) | 1347–1362, 1590, 1112 | Forward PMNS commitments "forced … no free parameter"; a lower octant "excludes the prediction" (1112) | C-PRED-1 | CB, O | F-8 (values covered; forward status not) |
| SM-38 (r2) | 1374–1388 | Theorem 22 (wave or energy-conserving dynamics on connected bounded-degree graphs) | none | U | Does not bear on F-2; LC |
| SM-39 | 1390–1446 | Structural against solution-specific; tiers | §5.1 | CB | |
| SM-40 | 1448 | "exact theorems"; mass gap irrelevant | B-QCD-6 | CM, O | F-22 |
| SM-41 | 1450–1468 | Neutrino expectations on the branch | B-SM-NU-1 to B-SM-NU-3 | C, T | F-19; RO (sensitivity) |
| SM-42 | 1484–1536 | B conservation; operator distinction | B-SM-BARY-1, B-SM-NP-3 | CB | |
| SM-43 | 1596–1654 | Appendix A spectral structure | none | U | LC |
| SM-44 (r2) | 14, 847, 1588 | "forced … no parameters fit"; "All predictions follow from the cubic-lattice geometry" | §5.1 | CM, O | F-23 (SM:847 added) |
| SM-45 | 88–96 | Alphabet-size hypothesis | §5.3 | CB | |
| SM-46 | 1470–1482 | Pattern against output | §5.1 | CB | |
| SM-47 (r3, new) | 1026, 1076, 1084, 1086–1094, 1100, 1108 | Routes to Cond 2 tried and excluded: the natural-form Yukawa gives $b_{12}:b_{13}:b_{23} = m_\tau/m_\mu : 1 : 1$, not Cond 2's symmetric split (1088–1094); first-order-squared effects are excluded by spectrum dominance; the geometric second-order route is excluded by monomial orthogonality (projection ρ "exactly zero"); one $O(\lambda^3)$ interference route is "recorded, not pursued"; Cond 2 "stands as … a stated condition" (1108) | none | U | NEG; F-37; LC |

### 4.5 `papers/Structure.md`

| ID | Location | Claim (paraphrase) | Ledger row | Code | Notes |
|---|---|---|---|---|---|
| T-1 | 13, 33, 256–353, 359, 514 | Matrix models fail A2 and A5 | none | U, O | F-20; NEG; LC |
| T-2 | 361–389 | Independence; "cannot be foundational … simultaneously" | none | U, O | F-20 |
| T-3 | 391–435 | Swampland consistency; "parameters are derived" | none | U, O, T | F-18, F-19 |
| T-4 (r2) | 443–510 | Horizon holography; A/4 bound "under the conditions of the horizon calibration" | none | U, O | §3.2 (conditional clause quoted) |
| T-5 (r2) | 120–122, 516–576, 709–735 | Observer admission; landscape | none | U, O, T | F-2 (Theorem 22 removed) |
| T-6 (r2) | 98–198, 892–954 | Hierarchy; level placements; Born test | none | U, O, T | F-17 (Structure:179 against :192 and GR:30); the Born form is in the definition of Q_fb (Main:14) |
| T-7 | 620–655 | Defs 9.1–9.4; Prop 9.5; Cor 9.6 | none | U | LC |
| T-8 | 656–687 | Props 9.7a, 9.7b; Cor 9.8 | none | U | LC |
| T-9 | 761–825 | Algebra-channel pair "captures" couplings | none | U, O | §3.2 |
| T-10 | 829–862, 978–1062 | OI-string class open; protocol not executed | none | U | UO; LC |
| T-11 | 1028–1042 | LQG, causal sets, asymptotic safety fail A2 | none | U | NEG; LC |
| T-12 | 956–974 | No-GUT empirical lean | C-EARLY-3, C-PRED-3 | CB, O | §3.2 |
| T-13 | 1064–1084 | Q8–Q12 | B-SM-HIER-2, B-SM-NU-3, B-SM-BARY-2, B-SM-NP-3 | CB | |
| T-14 | 1086–1096 | Limit 4 | none | U | LC |
| T-15 | 1106–1261 | Four-feature audit | none | U, T | LC |
| T-16 | 1265–1329 | Empirical anchors | C-PRED-1, B-SM-NU-1 | CB | F-19 |
| T-17 (r2, new) | 703 | "OI's substratum produces $SU(3) \times SU(2) \times U(1)$ uniquely" | B-SM-3, B-SM-4 | CM, O | F-17 |

**Observation for the parallel review: Main's independence.** Four Main passages draw on content that
the companion papers develop:
- Main:76: the C3 horizon numbers;
- Main:660–674: the rest-frame lemma, which takes a causal horizon as given;
- Main:20: the "specific SM/GR branch" and the [Substratum §3.3] citation;
- Main:704: the "quantitative predictions" sentence.

They are recorded, not traced. Whether each is an illustration, a stated input or a dependency is
**unresolved**. The kind of work is MC or LC, depending on that trace.

## 5. Appendix-a row audit

`book/appendix-a-prediction-status.md` A.4 and A.5 contain 64 rows. Each is audited at row level:
- its ledger coverage;
- its class against the paper or chapter that carries it;
- whether a discriminating test is stated.

No row is excluded. The derivation bodies of the biology and engineering rows live in book chapters
13–17, which this audit did not read beyond their status notices (§10).

| Rows | Content | Ledger | Maps to | Row-level finding |
|---|---|---|---|---|
| 1 | 1/α₀ = 23.25, S, Layer 0 | B-SM-GAUGE-1 (CD) | SM-25 | F-35: S against SM:793 "conditional on single-copy H-link" |
| 2–4 | A·B (C); δ₀ (E); α₂, α₃ (R) | B-SM-GAUGE-1, B-SM-GAUGE-2 | SM-25, SM-26 | matches |
| 5, 7, 8, 9 | Cabibbo (C); \|V_cb\| (C); m_d/m_s (L); J (E) | B-SM-FLAV-1, B-SM-FLAV-5 | SM-29 | matches, apart from F-24 at source |
| 6 | A, S | B-SM-FLAV-1 (CD) | SM-30 | F-25 |
| 10, 11, 15, 21 | Koide Q, θ₀ (C); m_e, m_μ (M); m_b via Q_down (L) | B-SM-FLAV-1, B-SM-FLAV-2, B-SM-FLAV-5 | SM-31 | F-26 |
| 12–14, 19 | PMNS angles; sum rule | C-PRED-1 | SM-33, SM-37 | F-27, F-28 |
| 16 | m_b/m_τ (L, 2(a)) | B-SM-FLAV-3 | SM-35 | F-30 |
| 17 | m_u/m_d (L), "Within 1σ" | B-SM-FLAV-5 | SM-31 | F-29 |
| 18 | Σm_ν (L, Layer 3, oscillation inputs) | B-SM-NU-2, B-SM-NU-3 | G-15 | matches SM:1464; GR's wording is F-7 |
| 20 | m_t (R) | B-SM-FLAV-5 | SM-32 | matches |
| 22 | λ(M_Pl) = 0, S | B-SM-HIER-3 (CD) | SM-30 | F-6 |
| 23 | a₀ (C) | B-COS-4 | G-18 | matches |
| G2, G5, G6, G8, G9, G11 | Bekenstein bound; Hawking radiation; a₀; ν; dark budget; Page curve | C-PRED-4, B-COS-1 to B-COS-4, B-BH-5 | G-1, G-14, G-16, G-18, G-28 | match their GR anchors |
| G12 | Σm_ν (L) | B-SM-NU-2 | G-15 | as row 18 |
| G13 | Lorentz violation (C) | none | SM-5 | LC (C-LIV) |
| N1–N3, N6 | PMNS angles; sum rule | C-PRED-1 | SM-33 | F-27, F-28 |
| N4 | Σm_ν | B-SM-NU-2 | G-15 | as row 18 |
| N5 | normal ordering, C | B-SM-NU-2 (PE) | SM-41 | F-36 |
| N7 | δ_CP identified with b₁₂ − b₁₃ (L, 2(b)) | B-SM-NU-3 (EF) | SM-33 (SM:1046(ii)) | consistent: the value is bijection-specific |
| B1–B14 | Biology and medicine; 12 rows S, 2 rows C | none (r3 leaves them unclassified) | none in the five papers | U (LC). F-34: the S labels of B1, B2 and B6–B14 conflict with "conjectural extension" (ch16:6, ch17:6). B3's S label (ch13 §13.6) was not checked; ch13:140's conjecture concerns revival, not B3. B6 lists the observed R(t) ≈ 5 as content where ch17:172 predicts R(t) > 1. B4 notes it "does not discriminate" (T). Derivations not audited |
| F1 | BEC analogue-gravity F(r) = 2r − r², "proposed model form; derivation unpackaged" | none | none | U (LC); PE; testable (stated) |
| F2–F4 | Engineering gains, "not quantified" | none | none | U (LC); PE; T (no quantity to test) |
| F6 | DESI running-vacuum test | C-PRED-5 | G-14 | matches |
| F7 | Born-rule transients | C-EARLY-2 | (ch18) | matches |
| F8 | Cosmic recurrence | C-PRED-8 | (ch18) | matches; logically falsifiable only (T) |
| F9–F11 | Medicine and biology forward items | none | none | U (LC); PE (conjectural chapters) |
| F12 | Hurst exponent; the row itself says "retrodiction, not a forward bet" and "does not discriminate" | none | none | U (LC); T. Listed under forward predictions although the row denies it is one (MC) |
| F13 | Cross-charged boost-LV decoupling | none | SM-5, SM-6 (SM:130–134) | U (LC; C-LIV, C-LQ) |

Row tally: 64 rows audited, none excluded. 40 have a ledger row; 24 have none (G13, B1–B14, F1–F4,
F9–F13). The class, placement and T findings are counted in §2.

## 6. SM §7.1–§7.5 sample

**What was read.**
- In full, in r2: SM:849–903 (§7.1 CKM); SM:905–1002, including :936, except the ratio-table rows
  :922–935 (§7.2); SM:1010–1060 (the opening of §7.3 and the determination of A₁ and A₂);
  SM:1114–1128 (§7.4); SM:1132–1160 and :1206–1227 (§7.5: tree level, Z_S, matching mass, K selection,
  the bridge-gap list); SM:1269–1362 (§7.6–§7.8).
- In full, added in r3:
  - SM:1062–1112, the Cond 2 block (with SM:1026). This yields F-37 and F-38;
  - the ratio-table rows SM:922–935;
  - SM:1162–1205 (the K structural form and its arguments). These add only material already in F-30
    (SM:1172, :1196);
  - SM:1228–1267 (the bridge theorem and the prediction), adding the SM-35 note on γ₀.
- Not read: the predicted-mass table rows SM:960–966, which are numerical outputs of the Koide relation
  already tabulated at SM:1285–1286; and §6.2.1, which is outside §7.

**Check for other unsampled blocks** (r3). r2 left a §7 block unread when it was a derivation body
behind a stated status rather than a stated result. With SM:1062–1112, :1162–1205 and :1228–1267 now
read, no §7.1–§7.5 block of that kind remains unread. The only unread lines are SM:960–966 (data rows).

**Unsupported or under-recorded intermediate steps found** (each is entered in §3.1):
1. GST as "a corollary" against "an external empirical relation" (F-24).
2. The Wolfenstein-A identification asserted, with class S (F-25).
3. The Koide normalization selected by match to observation; the resolving computation is open (F-26).
4. The reactor-angle derivation takes its own target as a constraint, while a second route rests on
   the open normalization (F-27).
5. The PMNS normalization b₂₃ = 1 is a choice not listed among the open links (F-28).
6. The m_u/m_d data values are inconsistent within SM (F-29).
7. The m_b/m_τ matching mass is called "derived", while its coefficient is fixed by data and by MC
   with the standard measure (F-30).
8. "Six masses from one input", while the chain also takes Q_down, GST and the K selection (F-23).
9. (r3) The routes to Cond 2 that were tried are excluded, a negative result missing from the ledger
   (F-37).
10. (r3) The sum-rule match is read as showing that the mechanism is realized, although the mechanisms
    examined are excluded and the match is a retrodiction (F-38).

With the r3 additions, §7.1–§7.5 has been read in full, apart from SM:960–966.

## 7. Proposed ledger rows (proposals only)

These are proposals for the ledger author, under identifiers not used in r3. None is adopted here, and
no branch is ranked. Classes follow r3's definitions:
- DM only for a result that holds for every model of the bare finite class (r3:54–58). REVIEW-r3 S1's
  further question about finite carriers is unresolved and applies to each DM below.
- Results tied to the SM branch's lattice model, or to one displayed update, are CD (condition 4).
- S/C/L labels map as REVIEW-r3 S2 proposes: S → CD[cubic commitment, B-SM-4 (EF)], not DM; C, L and
  M → CD; R, E and P → EF. (r2 wrote "S → EF", which misstated REVIEW-r3 S2. No proposed row uses the
  S mapping, so only this line changes.)

**QM branch.**
- **B-QM-17**: C2 and C3 necessity. CD[the coupling-step model of the physical-memory theorem,
  Main:736] for the persistence form; CD[that model; mixing hypothesis (EM)] for the timescale form; DM
  for m ≥ 2^{I*} (data processing for any bijective realization).
- **B-QM-18**: genericity of the C1 witness among bijections (M-6). DM (exact counting).
- **B-QM-19**: Hamiltonian reconstruction from transition data (M-11, G-8). CD[(G1)–(G4); H-BG]; NEG
  for orientation selection.
- **B-QM-20**: separability threshold; CP-indivisibility; approximate unitarity (M-13, M-14).
  CD[the displayed nearest-neighbour update over 𝔽₂ (prime q stated)] for the threshold; CD[the
  permutation-dilation family] for CP-indivisibility.
- **B-QM-21**: intervention dilation and its three negatives (M-4, M-17). DM; NEG.
- **B-QM-22**: passive observation (M-20). DM (a statement about every finite operational theory);
  NEG as a scope limit.
- **B-QM-23**: predictive quotients; Props 24.3–24.5 (M-21, S-12). DM (any finite permutation with a
  passive readout).
- **B-QM-24**: Barandes compression (M-10). CD[translation hypothesis (T); the imported external theorem].
- **B-QM-25**: partition-relativity (M-32). CD[Lemma 3's selected measure; prior as a third datum].
- **B-QM-26**: rest-frame selection (M-24). CD[horizon partition selects n; T fixes the foliation].
- **B-QM-27**: P-indivisibility on a finite representative of the constraint surface (G-34).
  CD[finite φ-invariant representative of the constraint surface].

**Substratum and Structure.**
- **B-SUB-1**: Theorem 23 (S-7, S-24). CD[E1–E7, M1-T, A1–A6, mixing hypothesis, nearest-neighbour
  premise, H-link, H-cust, H-spin′, H-χ′, H-slope]. Bell-inclusive existence CD[H-Bell];
  Bell-inclusive uniqueness UO. The converse direction of the :233 display is UO.
- **B-SUB-2**: Theorem 24 with Prop 24.2, Structure Prop 9.5 and Cor 9.6, and GR's deep-sector
  corollary (S-11, T-7, G-6). DM for (i) and (iii) at a fixed finite interface; CD[alphabet-size
  hypothesis] for (ii); completeness UO; CD[H-BD] for GR part (b).
- **B-SUB-3**: QM and GR as projections (S-1, S-2, S-17). PE; conditional on G3.
- **B-STR-1**: matrix models fail A2 and A5 in standard formulation (T-1, T-2). CD[BFSS and IKKT in
  their standard formulation]; NEG.
- **B-STR-2**: LQG, causal sets and asymptotic safety fail A2 (T-11). CD[the formulations cited]; NEG.
- **B-STR-3**: Props 9.7a, 9.7b and Cor 9.8 (T-8). DM (general operator theory).

**GR, cosmology and black holes.**
- **B-GR-10**: universality theorem (G-30). CD[S1–S4]; for (b) CD[H-count, H-slope, H-frame,
  H-Hawking, local boost structure].
- **B-GR-11**: H-local-lift locality (G-11). CD[H-local-lift].
- **B-COS-6**: interpolation constraints (G-19). PE; steepness bijection-specific (EF-type).
- **B-BH-8**: Theorems A.5 and A.7 (G-29). CD[frozen deep sector; D initially a configuration].

**SM branch.**
- **B-SM-13**: Theorem 1a and Cor 1a (SM-1). CD[cubic reference lattice; finite equivariant
  projection]. Cor 1b and Theorem 1: CD[that, plus an observer-level center-free kernel].
- **B-SM-14**: form lemma (SM-2). CD[CI, E4, A5, nearest-neighbour premise].
- **B-SM-15**: Theorem 22 (SM-38). CD[wave-equation or energy-conserving dynamics on a connected
  bounded-degree graph]; C2 and C4 as hypotheses.
- **B-SM-16**: Appendix A (SM-43). CD[A5 linear rule on the ring lattice; prime q, gcd(L, q) = 1].
- **B-SM-FLAV-6**: forward PMNS commitments (SM-37). CD[Cond 2] for the sum rule; CD[Cond 2; b₂₃ = 1]
  for θ₁₂ and θ₂₃ individually; CD[Cabibbo identification] for θ₁₃. Concrete discriminating tests,
  including the lower-octant exclusion (SM:1112).
- **B-SM-FLAV-7**: y_t(M_Pl) = 1 gives m_t ≈ 207 GeV (SM-32). CD[unit compositeness normalization];
  NEG.
- **B-SM-FLAV-8**: the six-observable Casimir table (SM-36). PE (the claim that one identity explains
  six retrodicted values); the individual values keep their own classes. The 1/d normalization behind
  the identity is selected by match (B-SM-FLAV-9, EF).
- **B-SM-FLAV-9**: Koide normalization and the reactor-angle route (F-26, F-27). EF for the selection by
  match; UO for the 1/d derivation.
- **B-SM-FLAV-10** (r3): routes to Cond 2 (SM-47, F-37). NEG with P support, for the natural-form
  Yukawa, first-order-squared effects and the geometric second-order route. The negative is scoped to the
  hop model with its declared inputs (hop model, projection ρ, neglect of the $O(\lambda^3)$
  interference) and to the strict second-order extraction (SM:1108). UO for Cond 2 itself, which stands
  as a stated condition, and for the recorded, unpursued $O(\lambda^3)$ route. Test: the 7/6 sum rule.

**Level C.**
- **C-LIV** (SM-5, appendix-a G13). CD[observer-level branch; tree level]; UO for interacting and
  rotational-radiative protection.
- **C-LQ** (SM-6, appendix-a F13). CD[H-link, H-cust, condensate]; M_X EF (solution-level).
- **C-ERP** (S-10). PE; no test.
- **C-PRED-10**: Tully–Fisher evolution tension (G-21). CD (the tested law, B-COS-4); NEG.
- **C-PRED-11**: rich-cluster residual (G-22). CD (the tested law with the simple interpolation, B-COS-6);
  NEG.
- **C-PRED-12**: CMB match (G-24). CD[ρ_E ≈ Ω_CDM ρ_crit input; inflationary initial conditions]; EF for
  the input; the ΛCDM reproduction is a cross-check (XC).
- **C-PRED-13**: Bullet Cluster and the epoch-local kernel (G-23). PE.
- **C-STR-1**: observer admission (T-5). PE; its coupling clause conflicts with B-QM-18; no test.
- **C-STR-2**: swampland consistency (T-3). PE.
- **C-STR-3**: horizon holography (T-4). CD[H-slope and the §8.5(b) conditions]; a bound on "any horizon
  entropy" is not established beyond the calibration's conditions.
- **C-STR-4**: four-feature audit (T-15). PE.
- **C-STR-5**: Limit 4 (T-14). PE (the source's own assessment that the bare thesis is not falsifiable;
  a scope statement).
- **C-QG-1**: non-renormalizability as an artifact of treating the lattice as a regulator (K-6). PE;
  conditional on G3.
- **B-BELL-9**: Bell realization by cosmological-boundary modes (K-7). PE.
- **C-BIO**: appendix-a B1–B14 and F1–F4, F9–F12 (§5). PE (conjectural chapters); the row classes per
  §5.

**Proposed additions to ledger §11, as questions, not corrections.** F-2, F-3, F-5, F-6, F-7, F-8,
F-9, F-11 to F-13, F-15 to F-36 and F-38. F-37 is a coverage item for the registry, not a
disagreement. F-10 is withdrawn.

## 8. Book-control findings

Already recorded in ledger §11, and confirmed here: D1 (ch19:20), D6 (ch19:178), D7 (ch18:256), D9
(ch19:88). The ch18 and ch19 entries on the arrow of time, topology, consciousness, inflation, the
Hubble tension and anomalies match ledger rows B-P4-AOT-6, C-TOPO, C-CONJ-1, C-EARLY-1, C-HUBBLE and
C-ANOM. The counts at ch19:362 match SM's table and appendix-a.

| ID | Location | Finding | Register | Work |
|---|---|---|---|---|
| K-1 | ch19:106 | anomaly cancellation "forces exactly three candidate matter sectors" | F-31 | MC |
| K-2 | ch19:196 | "derives exactly one scalar doublet" | F-32 | MC |
| K-3 | ch19:46 | dark matter "not a particle", stated flatly | F-13 | MC |
| K-4 | ch19:118 | "derives the total budget" | F-33 | MC |
| K-5 | ch19:356 | "The framework derives the fundamental laws" against A-GR (Einstein equations imported) and SM:14, :1428 ("compression") | single-source overstatement | MC |
| K-6 | ch18:144–152; ch19:28–32 | Non-renormalizability "dissolution" (conditional on G3); no paper row | coverage | LC (C-QG-1) |
| K-7 | ch18:104 | Candidate Bell realization by boundary modes | coverage | LC (B-BELL-9) |
| K-8 | ch18:56–58 | Late-time history-dependent Born corrections | coverage | LC |
| K-9 | ch19:226–248 | Rotational radiative stability open; a "direct computation" R ≈ ε with no record cited at that line | coverage; unresolved (computation not located) | LC; RO |
| K-10 | ch19:194 against GR:530 | Inflation "Not addressed" against inflationary initial conditions | F-15 | MC; LC |
| K-11 (r2) | ch03:26; FULL:891 (outside ch18–19; needed under §A.25 for F-2) | Mirror of Structure:733 | F-2 | MC |

## 9. Off-`main` references (§A.42 item 8)

| Reference | Attached to | Classification |
|---|---|---|
| #914 comments 6877871344 and 6877908458 | The audit's mandate and the QCD-group check | Provenance and authorization only; no claim rests on them |
| #914 comment 6878781541 (owner guidance) | Scope of r2 onward (header) | Provenance and authorization only; quoted verbatim in the header; no claim rests on it |
| `REVIEW-AUDIT-r1.md`, `REVIEW-AUDIT-r2.md`, `REVIEW-r3.md`, `LEDGER-r3.md`, `COVERAGE-AUDIT-r2.md` (drafts, not on `main`) | Dispositions; class mapping; the ledger under audit | Provenance only; every manuscript statement here cites a file on `main` |
| PR #1292 (r1 at `edc50055`, r2 at `70748aad`, per the reviews) | Where the drafts are kept | Provenance |
| #1063 | Planning record named in F-22 | Provenance (planning, §A.45 rule 1) |

Every scientific statement in this audit cites a file on `main` at `dfeec843`.

## 10. What this pass did not do

- **Book chapters 13–17** were read only at their status notices (ch13:138–140; ch16:6; ch17:6, 16,
  170–174). The derivations behind appendix-a B1–B14 and F1–F12 were not audited; only the rows'
  classes against those notices were.
- **SM §7.1–§7.5** were read as stated in §6. Only SM:960–966 (data rows) remain unread.
- **Chapter 13 §13.6** was not read, so B3's S label is unchecked (F-34).
- **Kernel and census.** No kernel identifier was checked against `verification/lean-manuscript-census.json`
  or the Lean modules. That includes the directional witnesses of the equivalence displays in F-16 and
  the question at G-9.
- **Records.** No script, probe or record under `verification/` was run.
- **Main's independence** (the observation after §4.5) was recorded and not traced.
- **Unresolved findings.** Ten findings remain unresolved and are reported as such:
  - F-1 (Structure coverage);
  - F-2 (the C2–C4 clauses);
  - F-22 (does the nonperturbative phase affect the coupling predictions);
  - F-26, F-27, F-28, F-30 (open derivations);
  - F-37 (whether any route derives Cond 2; F-28's open item, the b₂₃ = 1 normalization, is separate);
  - K-9 (computation not located);
  - the Main-independence trace.
