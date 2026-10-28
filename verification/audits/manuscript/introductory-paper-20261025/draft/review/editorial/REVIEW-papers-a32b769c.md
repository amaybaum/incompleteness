## Re-review of `papers/Introduction.md` at a32b769c (PR #918): editorial and citations

**Verdict: ACCEPT WITH CHANGES.** All must-fixes from both earlier reviews are resolved. The citations are clean, and every internal locator exists. What remains is three must-fixes (findings 1–3), several notation and order defects, repeated limitation statements, and length.


### 1. Build (`sh ./build.sh Introduction`)
- **Result:** OK, 18 pages, US letter, default geometry.
  - The rebuilt `.tex` is byte-identical to the committed one, and its source-sha256 matches the `.md`. The PDF text matches the committed PDF; only the bytes differ.
- **Density:** median 2,765 characters per page; pages range from about 2,400 to 3,200. There is no table collapse.
- **Boxes and glyphs:** 0 overfull boxes and 0 dropped glyphs. There are 2 benign underfull lines, in the Attribution paragraph and the §2.6 "only candidate divisor" paragraph.
- **Page map:**
  - p1 holds the title and abstract only; the two-line §1 heading does not fit, which leaves about 10 lines empty.
  - The main text (§§1–6) runs p2–p14 and ends about 60% down p14.
  - Code note p14–15, Appendix A p15, references p15–18 (about 3.3 pages).
- **One-inch margins (owner's choice):** 12 pages as the text stands, with the main text ending on p10. With the cut package below, 11 pages.

### 2. Cut list to 15 pages, default geometry
I measured each cut in scratch builds. Savings are in pages; each line number is the paragraph.

| # | Cut | Est. saving |
|---|---|---|
| K1 | Tighten reference spacing: `\setlength{\parskip}{1pt}` inside the existing `\begingroup\footnotesize` (L255). Text unchanged. | 0.5 |
| K2 | §2.4: compress L91 (define I\* once; keep every result) and L93 (C1–C4) | 0.4 |
| K3 | §6: compress L211 to one list of established results, no restatement; tighten L213; delete L225 (repeats the abstract) | 0.35 |
| K4 | §2.6: move L129 (CP/BBS24 paragraph) into §3.1 as one sentence, keeping the Bell sentence in §2.6. This also fixes finding 9. | 0.2 |
| K5 | §5 L207: cut "The research objectives are…" and merge those items (GSL, QES/islands) into §6's applications list (L223) | 0.15 |
| K6 | L28 Contributions and L60 Attribution: attribute once each | 0.25 |
| K7 | §3.5: delete L171 (the Born exponent repeats §2.3 and §6); retitle "3.5 Bell structure"; compress L175 | 0.2 |
| K8 | §2.5 L103: recast as a displayed Corollary (finding 6); drop the duplicated RHP14/BD16 sentence (L97) and the "monotone distance" sentence (L101) | 0.15 |
| K9 | Smaller tightenings (see below) | 0.6 |
| K10 | Shorten the §1 heading to "1. Introduction" and the abstract to about 190 words, so §1 starts on p1 | 0.15 |

- **K9 detail:** compress L56 (Realization), L145 (operational-theory setup), §3.3 (L161, L163) and §3.4; merge L38 into the D_K definition; merge L139 into L137; turn the code-section bullets into one sentence; set Appendix A in `\footnotesize`.
- **Result:** exactly 15 pages, with the last page full, so there is no slack. No established result is removed.
- **Ledger caveat for K8 and K6:** rewriting the Corollary paragraph (L89) retires its coverage ID. CHANGES-r16 kept that paragraph byte-identical for that reason, so this is the owner's call.

### 3. Earlier must-fixes
- **Editorial, all resolved:**
  - the random variables and TV are defined (L36);
  - the HTML comments are gone (none remain in the source);
  - Λ is now only the cosmological constant (L181, L187);
  - h is only the hidden configuration; the card is x/b;
  - the §5 toy model is set up before its results, with one residual mislabel (finding 3).
- **Citations, all resolved:**
  - M1: the corpus is repinned to 55e3217b at L229 and L257;
  - M2: the open problem is deleted and the answer stated at L91;
  - M3: [Sti55; Kra83; Oza84] and [Har01; CDP11; MM11] are cited at L155, with the novelty sentence at L28.
- **Earlier should-fixes still open:**
  - "spectator-independent local readout" is still unglossed (L145);
  - I\* is defined only by "reaches" (L91);
  - Lean names: only `S_imp_D` (L89) remains in the body, kept deliberately for its coverage ID.

### 4. Findings

**Must-fix**

1. **L12, abstract.**
   - Current: "the observed process is stochastically indivisible somewhere in its recurrence cycle whenever a visible transition map from the initial time is not a permutation".
   - Problem: the indivisible object is the rooted family Γ_t, whose rows include roots of visible probability zero (L97). Main's abstract (:20) says "the full rooted visible process"; "observed process" is stronger than the evidence.
   - Proposed: "…every non-deterministic visible step makes the rooted visible process stochastically indivisible somewhere in its recurrence cycle".

2. **L205.**
   - Current: "…its linear case is the secret-sharing threshold [Sha79]".
   - Problem: Shamir constructs a threshold scheme. The bound that a hidden remnant must have at least |ℳ| values is the share-size and perfect-secrecy bound, which Sha79 does not establish. Sha79 is also recorded as not read first-hand.
   - Proposed: "…so hiding the message completely needs at least as many hidden values as messages, as in perfect secret sharing, of which Shamir's threshold scheme is the standard example [Sha79]". Alternatively, delete the clause.

3. **L203.**
   - Current: "The layout is the framework's nested-partition construction [GR App. A] at small size."
   - Problem: the quoted 1,376/40,320 result is from the *moving-partition* layout. BH-01's REPORT reports 2,688 for the nested V/B/D layout.
   - Proposed: "The layout is that of the Page-curve setup [GR App. A.7], in which registers pass from the interior to the radiation, at small size."

**Should-fix**

4. **L207: τ_B^D is undefined.**
   - Proposed: "valid on times short compared with the B–D coupling time τ_B^D, of order the Hubble time [GR App. A.5]".

5. **L60 vs L97–99: n has two meanings.** It is |𝒞_V| at L60 and a time in "P-divisible on {0,…,n}" and in Theorem 3.
   - Proposed: write "one-step |𝒞_V|²-dimensional ancilla dilation" and drop the n there.

6. **L103: the headline result is buried.** The abstract's indivisibility result sits mid-paragraph, between evidence-class qualifiers.
   - Proposed: display it as "**Corollary** (indivisibility from any non-deterministic step; proved on paper [Main §2.3, Theorem (history readback…)]). *Any two distinct positive-probability visible histories with a common endpoint, in particular a memory witness or any non-deterministic visible step, make some Γ_s, s<L, a non-permutation, so the family is not P-divisible on {0,…,L}, also for laws that are Markov on every accessible window. With a full-support visible prior this is equivalent to M_k>0 for some k<L.*"
   - Follow it with the accessible-order sentence and the routed-form machine-check sentence.

7. **Owner direction ("explain why they are interesting"): there is no significance sentence before §2.4 or §2.5.**
   - Proposed, for §2.4: "Observed memory thus bounds an inaccessible quantity: a measurable conditional information fixes the minimum size and content of the hidden sector."
   - Proposed, for §2.5: "Indivisibility, the feature the stochastic–quantum correspondence ties to quantum behaviour, is therefore generic for embedded observers of finite reversible systems."

8. **Limitations are repeated (owner direction).**
   - "Represents, does not derive the mechanism" appears at L26, L139 and L211.
   - Born-exponent non-selection appears at L66, L171 and L219.
   - G3 is open at L195, L213, L223 and L225.
   - The Page-curve open items appear at L207 and again at L223.
   - The evidence class of the Theorem 2 vanishing criterion appears at L85, L89 and L243.
   - Fix: keep each in its derivation site plus §6 (cuts K3, K5, K7).

9. **L129: forward references.** "CP-indivisible", "notion (2) of §3.1" and "entanglement-breaking" are used before CP-divisibility is defined at L137, and "entanglement-breaking" is never defined. The decomposition sentence is also garbled: "the second map is an instrument realizing the first…".
   - Proposed: move it to §3.1 (cut K4) as: "the two-step map is the one-step channel realized as a Pauli twirl, ρ↦¼σ_oρσ_o, followed by the outcome-conditioned σ_o".

10. **L103, L175: terms the paper does not define.**
    - "(C4) gap" (L103): use the paper's own term, "memory witness".
    - "the graph's causal-cone lemma" (L175): add the gloss "(an intervention on A changes, k updates later, only components within graph distance k of A)".

11. **L145: "spectator-independent local readout of the ancilla" is still unglossed.**
    - Proposed: "a local readout of the ancilla that does not depend on untouched systems".

12. **L91: I\* is defined only implicitly ("information … reaches I\*").**
    - Proposed: "With I\*=max_t I(X_{<t};X_{>t}|X_t), every realization has |𝒞_H|≥2^{I\*}".
    - Also give (C3) its content at L93: "(C3) capacity, log₂|𝒞_H|≥I\*".

13. **One term per object.**
    - Γ_t is called "rooted visible transition matrix" (L97), "rooted map" (L103) and "visible transition map from the initial time" (abstract). Use "rooted transition matrix".
    - L20 "observer/complement configurations" vs "visible/hidden" elsewhere: use "visible configurations 𝒞_V … hidden configurations 𝒞_H".
    - L38 "initial law" vs "prior": say "initial law (the prior)".
    - L116 "street" is defined and never used again: delete it.

14. **L72: the pushforward notation (f_x)_# is undefined.** Add "(the pushforward of μ_ω under f_x)".

15. **L213: the apposition is ambiguous.**
    - Current: "If OI holds as physics, a representation choice motivated empirically, …".
    - Proposed: "If OI holds as physics (with the bijective substratum an empirically motivated representation choice, §1.1), …".

16. **L203: observer access is vague.** "reads fixed registers on a fixed schedule" does not say what is read in the quoted result.
    - Proposed: "reads each register as it is emitted, on a schedule fixed in advance, and keeps every read".

**Optional**

17. **Voice (§A.32/§A.33).**
    - The scans found no caps emphasis, no history phrases, no reader instructions and no HTML comments.
    - Remaining borderline items:
      - L28 "the novelty of neither has been assessed" is process voice. Alternative: "no earlier statement of them is identified".
      - L26 "status ledger": use "status tables".
      - L175 "determinism is constitutional": use "determinism is part of OI".
      - L225 "…the research objectives the framework poses": delete (cut K3).
18. **Lean name in the body:** L89 still has `S_imp_D` (coverage-ID tradeoff).
19. **Overloaded symbols:**
    - d is a dimension (L137, §5) and a graph distance (§3.5);
    - q is the TV argument (L36) and the Born exponent (L66);
    - suggested fixes: use μ,ν for the TV arguments and d_G for the distance.
20. **Cal26 (L293):** add doi:10.1007/s40509-026-00415-9.

### 5. Clarity and notation, the remaining checks
- **Λ and h:** each now has one meaning.
- **§2.6 toy models:** all three are self-contained, and their numbers check by hand:
  - Γ₁⁻¹ = [[2,−1],[−1,2]];
  - P(x₂=0 | x₁=1, x₀=0) = 1 and P(x₂=0 | x₁=1) = 1/3;
  - the XOR process gives ½J at every step and 1 bit of memory;
  - the card rows hold, and so does the anticorrelated variant.
- **§5 toy model:** self-contained apart from findings 3 and 16. Every BH-01 number matches `REPORT.md`/`result.json`: 1,376/40,320, 60, 32.

### 6. Citations
- **Key resolution:** all 51 entries are cited, every in-text key resolves, and there are no orphans or duplicates.
- **New references, checked against Crossref and arXiv metadata:** Sti55, Kra83, Oza84, Har01, CDP11, MM11, PSW06, HLW06, HP07, AEMM19, AMMZ20 and Pen20 all match as cited.
  - Cal26's journal record matches: *Quantum Stud. Math. Found.* **14**, 2, issued 2026-10-24.
- **Use:** each new citation is used at abstract or standard-knowledge level (dilation and measurement models, operational reconstructions, measure concentration, HP07 recovery, QES/islands). Calvo's abstract supports "derives the textbook axioms".
- **Pinpoints:** none was added for a new reference. The only added pinpoint is a reuse of the existing [RHP14, Thm 2.4]. Sha79 is the one misuse (finding 2).
- **Internal locators at 55e3217b:** every [Main §…], [GR …] and Book locator exists and matches its content. Main, GR and the book are identical between the branch and 55e3217b.
  - Main examples: §1.2 Remarks (:60, :62), Theorem (Bell ceiling for a screened local completion) (:360), Remark (a variational question) (:610), §4.5 (:718), §2.3 Scope (:141), and the in-window revival (:153).
  - GR examples: §3.3 Theorem (:218–220), §6.2 and Level G3 (:356), App. A.1, A.5–A.7, and Thms A.7–A.9.
  - Book: §1.11 (ch01:265) and §7.6 (ch07:108).
- **Lean:** the Appendix A line numbers I spot-checked (11 declarations) resolve at 17b830bc. The Lean sources are identical between 17b830bc and 55e3217b.

### 7. Typesetting
- **`\begingroup` scope:** correct. Appendix A has `\small\raggedright` (L240–251) and the references have `\footnotesize\raggedright` (L255–363); §2.6 is no longer inside a group.
- **Long formulas:** Theorem 2(b), the Γ matrices and both §4 field-equation displays are displayed, and no inline formula breaks badly.
- **Abstract:** 217 words, and it fits on p1. At about 190 words, together with a shorter §1 heading, §1 would also start on p1 (cut K10).
