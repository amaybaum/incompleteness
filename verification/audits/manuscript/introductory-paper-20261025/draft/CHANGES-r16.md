# Introduction r16: changes against the landed r15 (`papers/Introduction.md` at `a0edb582`)

r16 is one coherent revision of `papers/Introduction.md`. It applies four sources: the consolidated scientific audit of
#942/#946 (slice 2, §D: D1–D6), Track C's Introduction items (I-1 to I-12), the editorial review
(`review/editorial/REVIEW-papers-edac91c9.md`) and the citations review (`review/references/CITATIONS-edac91c9.md`).
The owner's directions of 2026-10-27 govern it:

- state the strongest result proved, its implications, and exactly what remains open;
- lead with the established results;
- keep the title;
- keep §4 as a major application, separating the demonstrated result from the proposed resolution;
- give Bell's four hypotheses and the ±1-every-run requirement;
- define the §5 toy model before its results;
- give distinct notation to the two meanings of Λ and of h;
- stay focused, and add only the citations a referee needs for attribution;
- make the three-way distinction (established / conditional / open) the organizing frame;
- add a strength check.

Every source pointer was read at `main` `55e3217b`. The branch's `papers/Main.md`, `papers/GR.md` and `book/` are
identical to it.

## Scientific alignment (old → new)

| Id | Site (r15) | Old | New (r16) | Source |
|---|---|---|---|---|
| D1 / I-2 / I-5 / S1 | abstract | "finite recurrence turns history readback into stochastic indivisibility somewhere in the recurrence cycle (each with one step not machine-checked)" | "the observed process is stochastically indivisible somewhere in its recurrence cycle whenever a visible transition map from the initial time is not a permutation, which every non-deterministic visible step supplies"; Theorem 1 "stated here as one machine-checked theorem"; the per-step evidence classes move to §2.4–§2.5 and §6 | Main :20, :82(2), :141 |
| D2 / I-1 | L56 | "For a law with rational probabilities, a realization whose hidden prior is independent of x₀ also exists" | the rational class is the conditional kernels at positive-probability histories, the visible initial law is arbitrary, and the response-table extension covers arbitrary kernels; "Every law also has a realization whose hidden prior is independent of x₀" | Main :512–514 |
| D3 / I-4 | L86 | "(C1) and (C3) follow from it, and (C2) is a physical-regime premise" | (C1) follows from (C4); (C3) holds in every faithful realization by the capacity bound; (C2) is given in its two forms, (C2-structural) by reversibility in every bijective realization and (C2-slow) as one mechanism, with fast record-conserving dynamics another | Main :72, :76, :78 |
| D4 / I-6 / I-7 / I-8 | L90–L96 | "history readback forces indivisibility somewhere in the recurrence cycle" | Γ_t has a row for every root under one hidden prior shared by every root; a non-permutation rooted map comes from any two positive-probability histories with a common endpoint, so from a (C4) gap and from every non-deterministic visible step, Markov-on-every-window laws included; with a full-support prior, cycle indivisibility ⇔ M_k>0 below L; the paper-proof steps named; routed readback defined; `routed_forces_indivisible_somewhere` kept (App. A) | Main :137–141; `PhysicalC4Discharge.lean:122` |
| D5 | L185(4) | "(C2) necessity, which is conditional on a hidden-sector mixing hypothesis" | open problem 4: "the hidden-sector mixing hypothesis … under which observed conditional memory bounds the persistence time of (C2-slow)" | Main :76, :496 |
| D6 / I-11 | L136 | "A deterministic completion that keeps pointwise causal cones and a setting-independent pre-setting ensemble is Bell-local … must give up one of the two" | the theorem with (i)–(iv), the coupling graph and its distance defined, and "if the protocol records a ±1 outcome in every run": Bell-local, \|S_CHSH\| ≤ 2. Reproducing 2 < \|S\| ≤ 2√2 violates at least one assumption. Under the framework's constitutional determinism and every-run outcomes, the completion gives up (ii)+(iii) (ontic parameter independence) or (iv) (measurement independence), the latter retained as a posit; H-Bell open | Main :360–:402 |
| M2 / I-9 | L185(2) | open problem "(2) whether the minimal hidden predictive memory equals M_t once ledger bits … are quotiented" | deleted; §2.4 states the answer: least I(X<t;H_t\|X_t) over deterministic completions = I(X<t;X>t\|X_t), attained by the canonical predictive quotient, = M_t iff I(X<t;X>t+1\|X_t,X_t+1)=0; bijective realizations carry H(X<t\|X_t); lower bound machine-checked for bijective realizations (`c3_necessity_via_hidden`, added to App. A), on paper for non-injective ones | Main :610, :99 |
| I-10 | §6.4 | "the discriminating content lies in memory" | kept, with "faithful realization" for "deterministic completion" | Main :20 |
| CP scope ([REVISER] L106) | §3.1 | "for them (2) implies CP-indivisibility" | "For the family obtained by tracing out a permutation unitary from a diagonal hidden state" | Main :326, :330 |
| independence ([REVISER] L120) | §3.2 | "of a fixed finite observation process" | "for one fixed finite embedded-observation process satisfying (C1)–(C4)" (the sealed OI core) | GR :220; `five_way_minimality` |
| gauge lemmas ([REVISER] L124) | §3.3 | "(both machine-checked)" | the time-dependent case is "machine-checked on an exhibited pair of lifts" (GL2 is existential) and the constant case "machine-checked in general" | `CoherentLiftGauge.lean:537, :451` |
| intermediate matrix ([REVISER] L26) | §1.2 | "(where the candidate intermediate matrix exists, it has negative entries)" | "(when the earlier matrix is invertible, the unique candidate has a negative entry)" | Main §2.3 proof |
| failure of divisibility, §1.2 | §1.2 | "produces" | "can produce" (a Markov realization produces none) | Main :612–614 |
| window revival | §3.1 | — | one sentence: an in-window revival of distinguishability makes the family P-indivisible on that window | Main :153 |

**Strength restorations** (owner direction 3), each at proved scope:

- Theorem 1 is called machine-checked in the abstract.
- "Every law also has a realization whose hidden prior is independent of x₀" replaces the rational-only statement.
- The least hidden predictive memory is stated as an exact value (§2.4).
- The full-support equivalence of cycle indivisibility with memory below L is stated (§2.5; Main states it at :20 and :141).
- (C3) is stated to hold in every faithful realization.
- The Bell numerical conclusion is given.

## Decisions on the [REVISER] items, by merits

- **`rooted_eq_iff_slice_eq` "forward direction".** No change needed. The Lean statement is (rooted families equal) ↔ G = G′, and its → direction is the one the paper uses.
- **Theorem 3's attribution (S2).** The citation review says [Main §2.3] states only the uniform-prior s = 1 case. Main's theorem "history readback + finite recurrence implies indivisibility" (:137) proves the general case: a non-permutation Γ_s together with Γ_n = I, via the stochastic-inverse lemma. Two rows share a positive column exactly when the matrix is not a permutation. So "[Main §2.3]" stays. S2's substance, crediting RHP14 Thm 2.4 and noting that Theorem 3 is that criterion applied once, is applied.
- **Assert-then-qualify (L142/144).** Fixed by structure. §4 now has three parts: "What OI establishes" (the descriptive distinction and the invisibility of the offset), "The proposed resolution" (conditional on the targeted field equations) and "The missing link" (G3).
- **§5 Page paragraph.** The conditions now come before the result.
- **"Title breadth".** Resolved by the owner: no change.

## Editorial

- **Must-fix, applied:**
  - X_t, H_t, X_<t, X_>t, bits and TV are defined in §2.1.
  - The §5 toy model is defined before its results: registers, message and prior, the map and emissions, observer access, P_succ, accessible advantage and 𝒰 (BH-01 `PLAN.md` §2; `REPORT.md`).
  - The divisor Λ is renamed Δ_{s,t}, so Λ is only the cosmological constant.
  - The visible hole card h is renamed x, with the encoding red = 0, black = 1.
  - The HTML comments are moved verbatim to `review/references/SOURCE-COMMENTS-edac91c9.md`.
- **Should-fix, applied:**
  - Appendix B is promoted to §2.6 "Three examples". The card table illustrates deterministic information versus access, and §5 and §6 refer back to it.
  - §6.1/6.2/6.4 are merged into one §6: established results with their evidence classes, conditional interpretations, and open problems stated as research objectives, closed by one sentence.
  - The abstract is cut from 279 to 216 words.
  - Lean names move from the body to Appendix A. The one exception is `S_imp_D` inside the Corollary paragraph, which is kept byte-identical so that its coverage ID `INTRODUCTION:C-unnamed-b596be8a`, derived from the statement's hash, is not retired.
  - Theorem 2(b) and the §4 field equations are displayed.
  - The five completion conditions are an enumerated display.
  - "routed" is defined.
  - "memory witness" is defined (§2.4).
  - CP, CHSH, unistochastic, δ_a, n and "ancilla level" are defined.
  - "Q_K" is called "fixed-basis Born records" throughout, and "faithful realization" is used for the realization object.
  - §3.4's title is "No fixed finite realization reproduces a qubit".
  - The \begingroup of Appendix A is closed after its list, and the references get their own group in \footnotesize. This is the layout option recorded at RECHECK-r4: a smaller font in the approved raw group, with identical text.
  - The sentence "What the paper states are the cited theorems and their scopes" is deleted.
  - "internally reviewed" is dropped from [BHa]/[BHb], and the two titles are given in one style.
  - The item labels of unpublished records ("item F", "C6(a)–(d)") are replaced by content.
  - The Born exponent is written |U|^q, so p is no longer overloaded.
  - The full 40-character Lean hash is put in code font, with the short hash.
- **Not applied:**
  - The geometry is unchanged, per the brief.
  - Locator punctuation and key style are left as they are (optional).
  - The B.3 table caption is not added (optional).

## Citations

- **M1, applied.** The corpus is repinned to `55e3217b`. Every Main/GR/Book locator the paper cites was checked there, and the
  Lean sources are identical at `17b830bc` and `55e3217b` (`git diff` empty). The Code section says why the two pins
  differ. `papers/introduction_repro/` is unchanged.
- **M2, applied.** See above.
- **M3, applied.** Theorem 4's sufficiency ingredients are attributed [Sti55; Kra83; Oza84], the operational reconstructions
  [Har01; CDP11; MM11] are cited, and the novelty of the §3.2–§3.3 results is stated as not assessed.
- **Applied should-fixes:**
  - S2, as decided above;
  - PSW06/HLW06 for the measure-concentration step, which stays;
  - the island/QES references [AEMM19; AMMZ20] beside [Pen20];
  - [HP07] for recovery from accessible radiation;
  - line 64's target, retargeted to Main's Remark (what this equivalence does and does not say), Main :550;
  - Cal26's journal version;
  - HKLP24's unread "Thm 4" pinpoint, dropped;
  - "p. 12 of arXiv v3" stated for Bar25;
  - "Main §3.1, §3.4" for the Born exponent;
  - the Pinsker lemma named.
- **Recorded, not applied** (owner direction 8: only attribution-required citations):
  - S3, Stinespring uniqueness for the lift freedom;
  - S4, SEDPH19 and MKPM19 for the Hadamard example;
  - S5, PRFPM18 in the minimal model;
  - SC01;
  - Martin 2012 and Padmanabhan 2003;
  - Spekkens and Harrigan–Spekkens;
  - Jarrett/Shimony/Hall/Bohm;
  - CDP09 combs;
  - Capela et al.;
  - Leggett–Garg;
  - Pimenta;
  - Blakley;
  - the tH14 book version.

  None is needed for attributing a result the paper states.
- **New references, metadata-verified, not read first-hand:** Sti55, Kra83, Oza84, Har01, CDP11, MM11, PSW06, HLW06,
  AEMM19, AMMZ20, HP07, and Cal26's journal record. Sti55, CDP11, MM11, PSW06, HLW06 and AEMM19 match the entries
  already in [Main] or [GR].
- **CT06, Har04 and Sha79** remain not read first-hand (`SOURCE-COMMENTS-edac91c9.md`).

## Track C items

| Item | Disposition |
|---|---|
| I-1 to I-11 | Applied as mapped above |
| I-3 | Supplied by the new memory-witness definition placed before the Corollary; the Corollary itself is unchanged (ledger ID) |
| I-12 | No change: the paper has no ε-realization text, and R-07's register sentence does not occur |

## Open units checked against the paper

- **Not cited by the paper:** SC-22 (book-only 𝒩), SC-24 (Medicine), SC-25 (rest frame), SC-28 (Poincaré, type II, SM :1211,
  Main :176), the SC-29 continuity sites, and the SC-23 fast-bath and one-step-thermalization claims. The paper states no
  fast-bath or thermalization result.
- **SC-26:** none of the listed residual sites is a source of a statement here. The paper's recurrence and divisibility
  statements are Main §2.3's, at its scope.
- **SC-27:** the two C2 forms are stated from Main :76, and C3 as holding in every faithful realization, not under a mixing
  conditional.
- **SC-17/SC-19:** the Bell text is Main §3.3's theorem, not a summary, and C3 is not placed under any conditional.
- **SC-29 ledger levels:** the paper already states that Theorem 2's time-t identification is proved on paper.
- **SC-30 A-5:** the paper does not say "as late as one step before recurrence".

## For the owner (not changed here)

- GR §6's heading, "Dissolution of the Cosmological Constant Problem", while GR :356 calls the dissolution conditional on G3. This is an outside status finding for the audit.

## Strength check

| Established result | Where stated | At full proved strength? |
|---|---|---|
| S_K = D_K = Q_K, every finite horizon (machine-checked) | abstract; §1.2; Theorem 1, §2.2; §6 | yes |
| Independent-prior realization for every law (paper, exact probes) | §2.2 | yes (was rational-only) |
| Theorem 2(a)–(c) (machine-checked in joint-law form; time-t form on paper) | §2.4; abstract | yes |
| Corollary: M_t > 0 ⇔ readout-relevant hidden memory in every faithful realization (paper) | §2.4 | yes |
| Capacity bound \|C_H\| ≥ 2^{I*} (machine-checked in joint-law form) | §2.4; App. A | yes |
| Least hidden predictive memory = I(X<t;X>t\|X_t), with the M_t condition (paper; lower bound machine-checked for bijective) | §2.4 | yes (was listed as open) |
| Pinsker floor M_t ≥ p₀δ²/ln 2 (paper, exact probes) | §2.4 | yes |
| (C1) from (C4); (C3) in every faithful realization; C2-structural by reversibility | §2.4 | yes |
| Theorem 3, rooted form (machine-checked) | §2.5 | yes |
| Cycle indivisibility from every non-permutation rooted map, hence every non-deterministic step (paper) | abstract; §2.5; §6 | yes |
| Full-support equivalence with M_k > 0 below L (paper) | §2.5; §6 | yes (newly stated) |
| In-window revival ⇒ window P-indivisibility | §3.1 | yes |
| CP-indivisibility from (2) for the permutation-dilation family | §3.1 | yes |
| Theorem 4, both directions, every nonempty finite system (machine-checked) | §3.2 | yes |
| Five-way independence; OI alone does not imply QM (machine-checked) | §3.2 | yes |
| Non-selection of the relating evolution (machine-checked: instance and general) | §3.3 | yes |
| Qubit obstruction (factorization proved; unboundedness imported) | §3.4 | yes |
| Bell ceiling \|S_CHSH\| ≤ 2 under (i)–(iv) with every-run outcomes (paper) | §3.5 | yes |
| Offset invisible to every visible transition probability | §4 | yes |
| Conservation neither implies nor is necessary for recovery; the 1/\|𝒰\| floor (exact enumeration, proofs) | §5 | yes |

## Measurements

- **Build:** `sh ./build.sh Introduction` gives 18 pages: the main text (§§1–6) is about 13.5 pages and ends on p. 14, and the code note, Appendix A and the references take pp. 14–18. There are no overfull boxes and no dropped glyphs. Text density is roughly 2,200–2,700 characters per page, with no table-collapse artefact.
- **Page count against r15 and the target:**
  - r15 had 17 pages, of which 11.9 were main text.
  - r16's main text is within the 12–15 page target.
  - The total exceeds 15 pages, for three reasons: the examples moved from the small-font appendix into the body, there are eleven new references, and the geometry is unchanged.
  - The `margin=1in` option, an owner decision recorded in the editorial review, would reduce the total to about 14.
- **Checks:**
  - `voice_check`, `claims_check`, `duplicate_check` and `coverage_check` are OK.
  - The release gate passes every step except `lean-axioms`, which is environmental locally (no `lake`) and passes in CI.
  - `verification/lean/edge_rigidity_probe.py`: ALL CHECKS PASS.
- **Lean identifiers:** all 29 declarations of Appendix A resolve at their stated lines at `17b830bc` and at the branch head.
- **Coverage:** `INTRODUCTION:T-3` is re-affirmed. Its fingerprint moves from 3322c5b34de8cf79 to c4966493d9cb60a2 (the theorem names "one hidden prior shared by every root" and "a positive entry in a common column") and its line from 92 to 99; it remains a MIRROR of the kernel's rooted form. T-1, T-2, T-4 and the Corollary are unchanged.
- **Added-lines scans:**
  - the §A.32/§A.33 phrase families and caps emphasis: no hits;
  - markers: no hits;
  - secrets: no hits (the only matches are "secret-sharing" and Shamir's title).
