# Introductory paper: outline, revision 2 (design stage, for owner review)

Revision 3. It applies the re-check `paper/review/RECHECK-r2.md` (BLOCK, wording only: RC-1 by
option (b), RC-2, RC-3, n1, n2) on top of revision 2, which applied `paper/review/REVIEW.md`.
`OUTLINE.md` and `OUTLINE-r2.md` are kept unchanged. `CHANGES-r3.md` lists this revision's
changes.

Stage: paper design only, as approved by the owner on 2026-10-26. No paper text is drafted and no
repository file is changed. Claim IDs (`§3-a`, …) are defined in `SOURCES-r2.md`, which gives for
each claim:
- the exact file:line;
- the kernel declaration;
- the verification layer and the correctness status;
- the originality class and its evidence basis.

**Inputs**
- **Main commit:** `687e885b1cfd24d6f17eee439101afc8acf07015` (Merge #933).
  - #932 changed Main:522 and Main:610, one line for one, so Main's line numbering equals that at
    `52e2db40`, the novelty audit's base.
  - The only other changes since `52e2db40` are GR:20, glossary:39 and FULL (F29), and ch18 (PE-01).
- **Novelty classes:** from `novelty-v5/AUDIT.md`, which is r4 with the nits of its re-check (Rc4)
  applied.
  - The applied text (sha256 `eacbdd56…22ad`) was not itself re-checked. Rc4 reviewed
    `AUDIT-r4-prerecheck.md` (sha256 `b8967887…a781`).
  - Read at the audit branch head `1e9c05c7`, which is not on `main` (SOURCES-r2, "Provenance").
- **Black-hole findings:** only those of packages whose separate-agent internal review closes with
  ACCEPT count as established.
  - BH-01 at `df2ea6f5`.
  - BH-02/BH-04 at `ce7937d2` (its parent is `ee2d4e68`).
  - Everything else in the programme is cited as open. Since review, the changes outside `review/`
    are wording, the replay recipe and SHA256SUMS.
  - Not external validation or owner adoption (`bh01_access_v1/review/README.md:3`).
- **Page format (target, an owner decision):** single column, about 550 words per page, displays
  included. Under that format, 12–15 pp is about 6,600–8,250 words. Every budget below assumes it.

## Positioning

A **technical perspective with original mathematical components**, not a new derivation of quantum
mechanics. It is written for physicists and mathematicians. It is built on Main's finite
observable-law correspondence, with a bounded black-hole information illustration.

- Correctness and originality are kept in separate columns (AUDIT:37–42, :308–311).
- The register follows §A.32/§A.33.

The **working title** is *Observational Incompleteness: From Deterministic Dynamics to Quantum
Observations* (PLAN.md:3–4). Its "from … to" can read as a derivation, the same exposure as Main's
title (F4, open). That is risk R1, and the title is an owner item. Neutral alternatives:
- *Observational Incompleteness: Finite Observable Laws of Embedded Observers and Their Quantum
  Representation*;
- *Embedded Observation and the Finite Stochastic–Reversible–Unitary Correspondence*.

## Replacement objective (owner decision 7, decided 2026-10-26)

The owner has decided that this paper becomes the primary short-form scientific presentation of
OI and replaces `papers/Explainer.md`. The Explainer is retired as a legacy document preserved for
provenance. The publication structure is Introduction → Main → Book. The paper runs 12–15 pages,
with enough mathematics for expert review and without duplicating Main.

### Assessment of the outline against this objective

- **Fits the objective.**
  - The recommended scope already carries the central idea, the correspondence at its proved
    scope, the quantum-like phenomena, the bounded black-hole application and the limits.
  - Each claim has a source in a maintained document (Main, GR, ch07, the reviewed packages), not
    in the Explainer.
  - Nothing in the outline depends on Explainer text.
- **Gap in coverage, accepted by design.** The Explainer also gives an overview of the wider
  programme: the cosmological horizon, ħ, ε, S_BH and the Standard-Model sector (Explainer §§4–6
  and the tables). The paper does not carry that overview. Under Introduction → Main → Book it
  points readers to Main and the Book. The content-migration audit decides where any such material
  goes; the book already carries it (paper/explainer/REVIEW.md §1–§2).
- **Changes this decision makes to the outline.**
  - (i) Regroup the sections into the owner's six parts (table below). The section numbering of
    the claim register is kept, so that claim IDs stay stable.
  - (ii) Add the card-table illustration, in corrected technical form (§5-h below).
  - (iii) The title becomes more important, since the paper is now the entry document (R1).
  - (iv) The retirement change, not the paper, carries the Explainer's dependents. That includes
    the census anchors at Explainer lines, among them the act 11 and act 12 families cited by
    §6-b. The paper's own commit adds its own anchors (decision 4).
- **What the paper must not inherit.** None of the items in the Explainer's stale list (REVIEW.md
  §3) is carried. Each maps to the outline as follows:
  1. The every-horizon characterization: §4-e uses Main:522's binding.
  2. "C4 ✓" at the cosmological horizon: out of scope (UNTRACED-6).
  3. "Every link is either a proof or a calculation": Appendix A lists unformalized links and
     conditions instead.
  4. The unconditioned thermal-matching, ε and S_BH rows: not carried.
  5. $I \ge I_0(1-k\tau_S/\tau_B)$: not carried; §4-d uses Main:167–170.
  6. The Rigidity Test: not carried.
  7. Decompression uniqueness and "wave function resolved": not carried, and contradicted by §6-b.
  8. "No empirical inputs": not carried.
  9. The bare "universal hidden-memory theorem": §4-a carries the formalization status.
  10. Section drift and dangling citations: not carried.
  11. Subtlety 1 (RVM): not carried.
- **Known results presented as novel.** No originality claim beyond CONTRIBUTION-r3 (b), whose
  classes are AUDIT r4's.

### Mapping onto the owner's six-part structure

Pages assume the format of decision 6 (single column, about 550 words per page). The total stays
14.25 pp. The card table (+0.5 pp) is paid for by §2 (1.0 → 0.75 pp) and §9 (0.75 → 0.5 pp).

| Owner part | Outline sections (claim IDs) | Pages | Explainer content the paper might absorb (candidates only; the content-migration audit decides) |
|---|---|---|---|
| **1. Central idea**: why observational incompleteness could make deterministic reality appear quantum | Abstract; §1 (§1-a to §1-d); §2-a and §2-b. The answer, stated at proved strength: marginalizing reversible dynamics gives stochastic laws (§5-a). Every finite such law has an exact fixed-basis Born representation (§3-a, §3-f). The quantum-like features are memory and indivisibility (§4, §5). Bare OI does not select QM (§6-d) | 0.25 + 1.25 + part of §2 | None needed. **Candidate:** the motivating register of the Explainer's introductory sections, rewritten from Main:28–30. The text is not to be copied |
| **2. Mathematical foundation**: the correspondence and its precise scope | §2-c to §2-e; §3 (E1); §4-a to §4-e; Appendix A | 0.75 (§2) + 1.75 + 1.25 + 0.5 | **Candidate:** the summary-table *form* (REVIEW.md §2: tabular form only; rows stale). It would be rebuilt as Appendix A from Main:710–722, never copied. Not a candidate: the D-gauge double-difference display. It is Main §3.1 content (Main:232–238), not Explainer-only, and phase-locking is outside this paper's scope |
| **3. Physical interpretation**: how observational restrictions produce quantum-like behaviour | §5-a, §5-c, §5-d, §5-e, §5-g; §6-a | most of §5 | **Candidate:** a short version, in technical register, of the quantum-weirdness walkthrough (Explainer:555–572; unique in register only, REVIEW.md §2). It applies only where it restates Main-supported content (for example Main:666, double slit), with no "dissolves" claims. Not candidates: the decompression section (stale, item 7) and the lineage survey (philosophical; its home, if any, is the book) |
| **4. Illustrative examples** | §5-b (Main §2.4 minimal model); §5-f (XOR); §5-h (card table, corrected form) | part of §5 (+0.5) | None. The card table comes from ch01 §1.11, not the Explainer. The Explainer's "coin-and-die" register is carried by ch01:135–155 and Main §2.4 |
| **5. Black-hole information** (bounded, independently verified only) | §7-a to §7-j, under decision 1(a) | 1.75 | None (the Explainer has no reviewed black-hole content) |
| **6. Limitations and open problems**, especially why full quantum equivalence is not established | §6-b to §6-f (E2, relating evolution, qubit obstruction, ε-gluing not used); §8 | 1.75 + 1.0 | **Candidate:** an FAQ-style list of "what the correspondence does not say", rebuilt from §6 and §8 and CONTRIBUTION-r3 (c). Explainer:659–702 is unique in register only |

**Sections that do not fit one part, and why.**
- **§9 Related work (0.5 pp).** It is cross-cutting. It is placed after part 6. Alternatively it can
  be split, with prior stochastic–quantum work in part 2 and Page/QES in part 5.
- **§10 Conclusion (0.25 pp).** A close, not a part.
- **References.** Not a part.
- **§6.** It is split between part 3 (§6-a) and part 6 (§6-b to §6-f). The paper's part 6 is where
  "why full quantum equivalence is not established" is answered. That answer is E2 with bare
  OI ⇏ QM (§6-d), the relating-evolution freedom (§6-b), the qubit obstruction (§6-e), and the
  open lifting layer (§8-a).

## Displayed equivalences and their directional witnesses (§A.34)

| Display | → witness | ← witness | Where |
|---|---|---|---|
| **E1** $S \iff D \iff Q_{\mathrm{fb}}$ (finite horizon $K$, finite alphabet) | S→D `S_imp_D` (Equivalence:422); D→Q `D_imp_Qfb` (:294); Q→S `Qfb_imp_S` (:245) | D→S `Qfb_imp_S ∘ D_imp_Qfb`; Q→D `S_imp_D ∘ Qfb_imp_S`; S→Q `D_imp_Qfb ∘ S_imp_D` (compositions at Equivalence:466–468), assembled in `finite_horizon_equivalence` (:462) | §3 |
| **E2** operational-completion characterization: on a nonempty finite carrier, the available families on the system and at every positive ancilla level are exactly the normalized finite Kraus instruments ⟺ conditions (i)–(v). Carrier-general | `physical_of_exactAll` (PhysicalCharacterization:301) | `exactAll_of_physical_general` (GeneralCarrier:93), via: `krausSoundExt_of_validity_inert` (OperationalValidity:124); `compositeCompleteness_unconditional` (IsometryExtension:179), which is the conditional `compositeCompleteness` (AncillaClosure:373) with its extension premise discharged by `finiteIsometryExtensionSF_discharged` (IsometryExtension:116); `exactAll_of_levelOne` (LevelOneSeam:196). Assembled in `exactAll_iff_physical_general` (GeneralCarrier:100) | §6 |
| *Alt-X only:* **E3** a rooted family is realizable by one finite permutation with a shared prior ⟺ `PPer` | `pper_of_finiteRootedRealizable` (RootedClassification:339) | `pper_has_responseRealization` (RootedClassificationAllTime:162); assembled in `finiteRootedRealizable_iff_pper` (:192) | §5 |
| *Alt-X only:* **E4** OI⁺ ⟺ exact finite endomorphic operational QM | `qm_of_oiPlus` (CarrierGeneralOIPlus:191) | `oiPlus_of_qm` (:198); assembled in `carrier_general_oiPlus` (:213) | §6 |

The non-implication "bare finite OI ⇏ QM" (GR:222) is witnessed by `oi_alone_not_qm`
(GeneralCarrier:160). That is a **qubit** countermodel (`∃ T : FiniteOperationalTheory (Fin 2)`),
not an equivalence.

**Not to be displayed as equivalences.** Each of the following lacks a kernel witness, at the stated
scope, for at least one direction. Each is stated in prose with its directions named, or not cited.
- **The memory biconditional (§4-b).** Each direction applies `pushforward_identity`, and the
  converse also needs `S_imp_D`. Two links are not formalized: the time-$t$ joint-law reading and
  the CMI vanishing criterion (Main:99, :580(2)).
- **(ii) ⟺ (iii) (§4-e).** Both directions are prose (Main:608).
- **C8-D, the rooted recurrence dichotomy.** It rests on prose steps B3, B4 and A1, and it is not on
  `main` (SOURCES-r2 UNTRACED-3).
- **The per-witness form at Main:610.** Prose.
- **GR:226's box, "OI-compatible operational theory + (i)–(v) ⟺ finite operational QM … for every
  nonempty finite system".** `oi_compatible_classification` (GeneralCarrier:168) and
  `RealizesSealedOICore` (OIRealization:234) are typed on `Fin 2` only. `main_result` (:188) is
  carrier-general in its first clause, but that clause has no OI conjunct. So the direction
  QM ⇒ OI-compatible has a kernel witness only on the qubit (`realizesSealedOICore_of_control`,
  OIRealization:252). The paper neither displays nor cites the box. It displays E2, which carries
  no OI conjunct. GR:226 is flagged to the owner as a separate check (SOURCES-r2, decision 5).

## Section-by-section outline: the recommended scope (body 13.25 pp, references 1.0 pp, total 14.25 pp)

"Not classified" means AUDIT r4 assigns no class: either no literature was examined, or the item is
a definition or an interpretation. Originality entries are AUDIT r4's, or a source package's own
description where that is stated. No originality entry is the design's own judgment.

### Abstract (0.25 pp)

The abstract covers:
- the hypothesis (§1-a);
- E1 at its proved scope, Markov laws included (§3-a);
- where the discriminating content lies: hidden memory (§4-a) and recurrence indivisibility
  (§5-c, §5-e);
- the three statuses (§6-c);
- the bounded black-hole application (§7);
- the open problems (§8).

It makes no claim to a derivation of quantum mechanics, no paradox resolution and no novelty
statement.

### 1. Introduction: embedded observation and the OI hypothesis (1.25 pp)

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §1-a | OI hypothesis: the statistics an embedded observer records are the visible marginals of a finite reversible deterministic system of which the observer is a proper part. The physical identification is a representation choice, empirically motivated. The theorems are mathematical, and no ontology-level falsifier is established | Main:28, :62, :702, :704 | prose (statement of hypothesis) | not classified ((e), interpretation; AUDIT:1409–1460) |
| §1-b | The question: what this reduction imposes on the form of the observer's laws | Main:28 | prose | n/a |
| §1-c | What is shown: the finite observable-law correspondence, where the non-Markovian content sits, and how far the correspondence is from operational QM | Main:22, :534, :622, :758 | prose (roadmap) | n/a |
| §1-d | Incompleteness here is inaccessibility of the hidden sector, not the uncertainty relations | Main:28, :572 | prose | not classified |

### 2. Setting and definitions (0.75 pp)

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §2-a | Observation $(S,\varphi,V)$, $V \subsetneq S$, finitely many visible states | Main:44, :48 | definition | n/a |
| §2-b | The bijective finite substratum is the reversible representative, a reconstruction choice; total finiteness is a posit | Main:56, :62, :708 (ii) | prose | n/a |
| §2-c | The hidden prior is part of the realization datum, so the visible law depends on $(\varphi,\mathcal P,\mu_H)$; invariance alone does not select the measure | Main:60, :86; `invariance_does_not_select` (CanonicalMeasure:242) | kernel (measure clause); definition | not classified ((e), AUDIT:1416–1423) |
| §2-d | Classes $S$, $D$ (the initial law on $V\times H$ may correlate the coordinates) and $Q_{\mathrm{fb}}$ (projective readout in one fixed basis at every step, from a diagonal initial state) | Main:98–99, :526–530; `Stochastic`, `RevRealizable`, `QfbRealizable` (Equivalence:147, :182, :216) | kernel definitions | n/a |
| §2-e | (C1)–(C4) are diagnostics of a realization, not hypotheses of the correspondence | Main:72, :74–80, :596 | definition / prose | n/a |

### 3. The finite observable-law correspondence (1.75 pp)

**Display E1.**

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §3-a | E1: for every finite alphabet and horizon $K$ the three classes coincide; each is the set of all laws on $V^{K+1}$ | Main:16–18, :526–532, :580(1); `finite_horizon_equivalence` | kernel (six directions) | PARTLY KNOWN; the packaging part is PROVISIONAL (C4; AUDIT:631–709) |
| §3-b | S⇒D by a clock plus a trajectory record: one iterated bijection, with an initial law that may be correlated | Main:532, :500 (kernel scope); `S_imp_D` | kernel | PARTLY KNOWN (C1; EG Prop. 13; the "not located" part is PROVISIONAL) |
| §3-c | Remark: a realization whose hidden prior is independent of $x_0$ (uniform tape; response tables for real kernels) | Main:496–500, :498 | prose proof + exact probes (`process_dilation_probes.py`, `review4_probes.py` P-G); independence not formalized (Main:500) | PARTLY KNOWN (C1′; EG Prop. 16, LPW Prop. 1.5; packaging PROVISIONAL) |
| §3-d | D⇒$Q_{\mathrm{fb}}$ by the permutation unitary; collapse in the configuration basis does not disturb diagonal states. **Not carried:** Main:532's remark "$U_\varphi = e^{-i\hat H}$ … fixed autonomous generator at integer times" (F3, open) | Main:262–266, :532 (the construction sentences only); `D_imp_Qfb`, `permMatrix_mem_unitaryGroup` (EquivalenceChain:179), `isDiag_Phi` (:253) | kernel | KNOWN (C2; B25 v3 p.12, B23 §4.3, B26 §4) |
| §3-e | $Q_{\mathrm{fb}}$⇒S: the every-step fixed-basis record is a probability law | Main:532; `Qfb_imp_S` | kernel | REFRAMING (C3; Strasberg–García Díaz Eq. (3), FT-r4) |
| §3-f | The representation is universal. Markov laws are included, so neither a realization nor a representation discriminates. The bare form "non-Markovian ⟺ a realization exists" is false | Main:98–99, :534, :592, :596–598 | prose (from E1) | C4-old WITHDRAWN (AUDIT:697–702); the remark is not classified |
| §3-g | The Born dictionary $p=\lvert U\rvert^2$ is part of the definition of $Q_{\mathrm{fb}}$. The construction does not select the exponent: permutation entries are 0 or 1, so every $p>0$ gives the same table | Main:20, :534; check 6, `equivalence_recovery_probes.py` | prose + probe | KNOWN, non-discriminating (C2 sub-item; B26 Thm 3.1; AUDIT:588–592) |
| §3-h | No single fixed finite substratum realizes a nonperiodic law exactly for all time (finite order) | Main:618 | prose proof | not classified |

### 4. Where non-Markovian content lives (1.25 pp)

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §4-a | In every faithful deterministic realization: (a) the next-step law is $(f_x)_\#\mu_p$; (b) the next-step TV gap is at most the posterior TV gap; (c) $M_t \le I(X_{<t};H_t\mid X_t) \le \log_2\lvert\mathcal C_H\rvert$. Proved in the kernel for a joint law; reading a realization's time-$t$ law as that joint law is not formalized | Main:582–590; `unavoidable_hidden_predictive_memory` (HiddenMemory:185), `pushforward_identity` (:83), `distinguishability_floor` (:114), `capacity_floor` (:170) | kernel (with the stated gap) + exhaustive probe (`memory_probes.py`, 1,464 cases) | REFRAMING (DPI); attribution PROVISIONAL (C10) |
| §4-b | The biconditional in prose, with its directions named: $M_t>0$ exactly when every faithful realization carries readout-relevant hidden memory at $t$. Forward: the pushforward identity in each realization. Converse: the same identity in one realization, which exists by `S_imp_D`. Both unformalized links are stated | Main:99, :580(2), :592 | kernel components + prose | REFRAMING (C10-B) |
| §4-c | Capacity: $\log_2 m \ge I^*$ | Main:484–494; `c3_necessity` (C3Necessity:80), `card_hidden_ge_two_pow_Istar` (:117), `c3_necessity_and_capacity` (:130) | kernel | REFRAMING; attribution PROVISIONAL (C11) |
| §4-d | Readback lemma: a TV gap δ between two histories of probability ≥ $p_0$ gives $I \ge p_0\delta^2/\ln 2$ | Main:167–170; `c4_backflow_probes.py` | prose proof (Pinsker) + exact probe | REFRAMING; PROVISIONAL (C9) |
| §4-e | (ii) ⟺ (iii) with (iii) corrected for F29, in prose only, with its reduction: (C4) coincides with (ii) in every faithful realization, so (ii)⇒(iii) adds only the existence of a realization | Main:516–522, :596, :608, :610; F29 record `verification/audits/manuscript/f29-witness-quantifier/result.md:6–30` | prose (both directions; not formalized); finite acceptance test | REFRAMING, near-definitional (C12). **One sentence, no display** |
| §4-f | (C1)–(C3) without (C4) admit realizations with zero backflow (the tape-and-ledger coin) | Main:172; `review3_probes.py` | exact probe | not classified |

### 5. Quantum-like behaviour from observational restriction (2.25 pp; owner parts 3 and 4)

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §5-a | Stochasticity comes from marginalization | Main:90, :105 | definition | n/a |
| §5-b | Minimal model: 2 visible × 6 hidden states, $\sigma^2=\mathrm{id}$. $T(1,0)$ has entries 2/3, 1/3, and $T(2,0)=I$, so $\Lambda(2,1)$ has negative entries. Memory witness: $P(x_2{=}0\mid x_1{=}1,x_0{=}0)=1$ against $P(x_2{=}0\mid x_1{=}1)=1/3$. The second value assumes $x_0$ uniform; for $P(x_0{=}0)=a$ it is $a/(2-a)$. Main:194 does not state the $x_0$ law, so the paper must | Main:178–196 | exact computation, in the text. Re-checked for this design by a scratch script, which is not a repository artifact and makes the uniform-$x_0$ assumption | not classified (illustration) |
| §5-c | A non-permutation one-step matrix together with finite recurrence ($\varphi^N=\mathrm{id}$) gives P-indivisibility, by TV contraction under a stochastic divisor | Main:115–129; kernel counterpart `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148), census `manuscript: []` (decision 4) | kernel (rooted form) + prose | KNOWN (C8; RHP 2014 Thm 2.4 "only if", BD Prop. 1; DO3 v3 Prop. 1 concurrent) |
| §5-d | TV monotonicity is necessary, not sufficient, for P-divisibility | Main:121; `translation_probes.py` | exact probe | not classified |
| §5-e | A stochastic matrix with a stochastic one-sided inverse is a permutation. Hence (C4) readback on a fixed finite reversible representative forces indivisibility somewhere in the recurrence cycle. The step from history-level (C4) to a non-permutation rooted map is prose; the kernel proves it from a routed-readback witness | Main:133–141; `isPermMatrix_of_stochastic_inverse` (EquivalenceChain:110), `routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122), census `manuscript: []` (decision 4) | kernel (lemma; routed level) + prose (history-level step, F11) | KNOWN (C7; mechanism C8) |
| §5-f | Scope: memory does not force short-window P-indivisibility. The XOR family ($X_1$ uniform and independent of $X_0$, $X_2=X_0\oplus X_1$) has one bit of conditional memory, and its matrix family factors through $\Lambda=I$ | Main:141, :606; `review4_probes.py` | exact probe | KNOWN: up to flipping the final bit, RHP 2014 Eq. (15) (FT-r4; AUDIT:1512–1514). DO3 v3 App. A is concurrent. No first-statement claim |
| §5-g | Stochastic P-indivisibility of populations is not quantum non-Markovianity outside the diagonal-preserving class (the Hadamard family). The framework's permutation-dilation channels are diagonal-preserving, and there P-indivisibility implies CP-indivisibility | Main:322–330, :334; `c1_cp_scope_probes.py` (exact over $\mathbb Q(\sqrt2)$) | prose proof + exact probe | not classified |
| §5-h | Card table (ch01 §1.11), in corrected technical form. The hole card is the visible bit and the burn card the hidden bit. The shuffle is the swap $\varphi(x,h)=(h,x)$, the same map as Main:286 and :702, with a uniform burn card. The matching odds are: one shuffle, 1/2 ($\Gamma_1=\tfrac12J$); two shuffles, 1 ($\Gamma_2=I$); chained through the middle street, 1/2. So the process is P-indivisible (§5-c, §5-e). With a peek in the middle, the odds are 1/2 **only if the re-burn overwrites the burn card**, the stored record. If the peek replaces only the revealed hole card and leaves the burn card, the odds are 1. ch01:271 and :280 leave this rule unspecified, and the paper must state it. Stated scope: a classical toy whose one-step channel is entanglement-breaking (Main:286); the indivisibility is classical; no Bell violation (ch01:286; Main §3.3). **Not carried:** "conditions C1–C4 … in card form" (ch01:271), because the three modifications are bijectivity, C1–C3 and an intervention rule, and C4 is the readback, not one of them; "structured incompleteness yields quantum, not classical, statistics" (ch01:269); "loses money at a rate equal to the interference term" and "phase is … where … the visible information currently resides" (ch01:282, :284), which have no Main counterpart; "not every doubly stochastic table can be dealt this way is the unistochasticity constraint" (ch01:286), which is in tension with Main:270 (every rational doubly stochastic matrix is a uniform-prior bijection marginal) and with Main:204, where the framework's own marginals fail unistochasticity; and the Schrödinger's-cat paragraphs (ch01:290–294; interpretation) | ch01:265–286; Main:286, :702 (swap); Main:115–141 (indivisibility) | exact hand computation. Re-checked for this design by the exact scratch script `probe/cards.py` over 16 cases, with re-burn rules A, B and C. Not a repository artifact; no repository probe for the card protocol was located | not classified (illustration) |

### 6. Reproduced behaviour versus a derivation of quantum mechanics (1.75 pp; the tightest section)

**Display E2.**

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §6-a | Representation, not explanation | Main:616 | prose | not classified ((e)) |
| §6-b | Representability does not select the relating evolution. Carried at its kernel scope only: (1) two coherent lifts of one visible family, related by a time-dependent strong-class element, have different relative candidates; (2) a constant deformation preserves the relative candidate; (3) the fixed-basis correspondence acts on the quotient by visible equality. The fibre-Gram classification and the ancilla-separation remark are not carried (SOURCES-r2 UNTRACED-1) | Main:624 (the site names identifiers only for (3)); (1) `gl2_strong_gauge_moves_relative_candidate` (CoherentLiftGauge:537); (2) `gl3_constant_gauge_preserves_relative` (CoherentLiftGauge:451); both anchored to this Main paragraph by the census family "the coherent-lift stabilizer no-go (act 11, Track B)"; (3) `bridge_traj` (TrackBQfbBridge:276), `rooted_eq_iff_slice_eq` (:180), `realData_traj_stochastic` (:286), `padData_rooted` (OperationalSourcing:476) | kernel | not classified |
| §6-c | Three statuses kept apart: finite observable-law representability is established; exact finite operational QM is characterized conditionally; selection of a unique relating evolution is open | Main:624 (closing sentences) | prose | n/a |
| §6-d | E2 (carrier-general). Then, **on the qubit**: each of (i)–(v) is independent of the other four and of the sealed C1–C4 core (`five_way_minimality`, `Fin 2`); `oi_alone_not_qm` is a qubit countermodel (a theory that never creates coherence realizes the core and is not quantum); every theory with full reversible control realizes the core. So bare finite OI does not select QM. Which of (iii)–(v) a physical substratum supplies is open (§8-a) | GR:216–222, :228; Main:352, :542; `five_way_minimality` (RankGapTheory:702), `oi_alone_not_qm` (GeneralCarrier:160), `realizesSealedOICore_of_control` (OIRealization:252) | kernel | not classified (AUDIT r4 does not examine it) |
| §6-e | Classical-dimension obstruction: no fixed finite ontic carrier reproduces a qubit's full prepare-and-measure behaviour exactly. The elementary factorization is proved; the unbounded nonnegative rank is imported | Main:538, :540, :580(3); `nogo_probes.py` | prose + imported result | REFRAMING of the Hardy-type no-go; PROVISIONAL (C14; Hardy 2004 and [55] unread) |
| §6-f | Cited, not used: Main states finite-accuracy ε-realization and gluing theorems for bounded quantum instrument families. These are realization theorems, not uniqueness theorems: the same machinery realizes non-quantum families. The paper does not describe them as "proved unconditionally" | Main:544–562 (:562), :578, :580(4) | prose proof + exact probes (`opglue_probes.py`); no kernel anchor (F7 open) | not classified (C15). **The paper relies on no conclusion from them** |

### 7. Bounded application: black-hole information as an access problem (1.75 pp)

Every computational item is a finite toy model, not a statement about physical black holes (BH01
REPORT:285–302; BH02 REPORT:203).

| ID | Claim | Source | Layer | Class |
|---|---|---|---|---|
| §7-a | Setting: the nested partition $S=\mathcal C_V\times\mathcal C_B\times\mathcal C_D$, with radiation registers emitted from $B$ into $V$ | ch07:120–122; GR:721 | definition | n/a |
| §7-b | Bijectivity conserves global information. This is the part of ch07's resolution sentence that is supported | ch07:118 (first sentence); BH01 MANUSCRIPT-AUDIT:91 ("supports") | definition-level | n/a |
| §7-c | Bijectivity of the global map neither implies recovery from the accessible records nor is necessary for it. In a bijective instance, zero accessible advantage requires $\lvert K\rvert \ge \lvert M\rvert$; 32 non-injective maps violate the corresponding bound | BH01 REPORT:17–18, :21, :35–47 | exhaustive exact enumeration + written proof; reviewed ACCEPT (`df2ea6f5`) | not classified (C16-S; AUDIT r4 did not read the #917 records, AUDIT:1397–1398) |
| §7-d | Sufficient conditions. Bijective dynamics with complete endpoint access gives exact recovery. An inaccessible endpoint set $K$ gives $P_{\mathrm{succ}} \ge 1/\lvert K\rvert$, the one necessary-side fact proved. The conditions are sufficient, not necessary | BH01 REPORT:20–21, :49–58, :66–86, :98–112 | written proof + exhaustive check; reviewed | covered in kind, per the package's own description of C2 and C4 (BH01 REPORT:110–112, :131–132); not literature-mapped |
| §7-e | The direct and sequential nested trace-outs agree for every map (a Fubini identity), so nested-trace consistency carries no recovery content | BH01 REPORT:29, :139–142; GR:731; ch07:124 | written proof + exhaustive check; reviewed | not classified |
| §7-f | GR A.7's stated support for decoupling ($\tau_{\mathrm{evap}}\ll\tau_B^D$) is reversed at 30 $M_\odot$: $t_{\mathrm{evap}}/\tau_B^D \ge 1.785\times10^{57}$, and $t_P/\tau_B^D \ge 1.153\times10^{57}$ ($t_P$ at β = 1). The Γ and $\tau_B^D$ intervals were chosen after the plan, and the margin makes the conclusion insensitive to them. The finding does **not** show that information reaches $D$, that A.7 is false within $t\ll\tau_B^D$, or that no other decoupling argument exists | BH01 REPORT:30, :211–245 (:228, :231, :234–235, :241–245); BH01 review REVIEW.md:3; GR:811, :813 | exact interval arithmetic; independently recomputed in review | audit observation (BH01 REPORT:257) |
| §7-g | A permutation acting on a configuration state generates no entanglement across configuration-aligned cuts. From any state, $S(R)\le H(p_0)$, and the overlap with $\lvert+^n\rangle$ is conserved | BH02 REPORT:14–15, :26–42 | one-line proofs + exhaustive exact sweeps; reviewed ACCEPT (`ce7937d2`) | not classified (no literature examined) |
| §7-h | In the setting GR Appendix A uses, H-scramble fails for every bijection (from §7-g). The Page value enters only through the Haar ensemble that H-scramble posits, not through bijectivity or the cycle decomposition | BH02 REPORT:18–19, :77–102; GR:817, :833 | proof (from §7-g); reviewed | not classified (no literature examined) |
| §7-i | Page-time fraction $t_P/t_{\mathrm{evap}} = 1-(\beta/(1+\beta))^{3/2}$, conditional on a constant coefficient in $dM/dt=-\alpha/M^2$, constant β, and $S_{\mathrm{BH}}\propto M^2$. It is 0.646 at β = 1 and about 0.538 at Page's β ≈ 1.485. A constant greybody or species factor cancels. An M-dependent coefficient moves the fraction (0.7027 for the power law $p=1/2$, up to 0.8707 in the step model). β > 1 in the quasi-stationary semiclassical regime | ch07:137–143; GR:859–865; BH02 REPORT:22, :118–134 (:123–127) | exact algebra + literature; reviewed | KNOWN (C16a, Page 2013 Eq. (8); C16b, Page 2005 Eqs. (5)–(10)) |
| §7-j | Open: H-scramble (ch07:126; GR:833); the step from the A.8 time average to A.9 pointwise in $t$ (BH02 REPORT:21, :112–114); the generalized second law (ch07:155–157; GR:805); QES agreement on the Page time (ch07:147); the island correspondence, conjectured (ch07:147–151); BH-03 and BH-05–BH-07, not run (PROGRAMME.md:3) | as listed | — | C16d WITHDRAWN items stay out (AUDIT:1362–1371) |

The paper must not carry:
- ch07:110 / FULL:1987, "resolves the paradox … because $\varphi$ is bijective" (BH01
  MANUSCRIPT-AUDIT:56–60, "contradicts" claim A);
- the falsification framing of ch07:159–161 / FULL:2036–2038 (BH01 MANUSCRIPT-AUDIT:143–160, the
  L155 entries at `809fac52`);
- any "derivation of the Page curve" without H-scramble.

**Live corpus sites the §7 claims contradict (R11).**
- §7-c contradicts ch07:110 / FULL:1987.
- §7-f contradicts GR:811.
- §7-h contradicts two sites: ch07:126 sentence 1 / FULL:2003 ("The framework's derivation of the
  Page curve runs through the *combinatorial* structure of the bijection $\varphi$ …"; BH02
  MANUSCRIPT-AUDIT:70–73), and GR:869 ("invokes only Popescu-Short-Winter … no ergodicity
  assumption"; BH02 MANUSCRIPT-AUDIT:256–259).

Every scope that carries §7-c or §7-h meets these sites. The recommended scope and Alt-L carry
both, and the BH-01-conflict-free variant carries §7-h. See R11 and decision 1(a).

Two parts of §7 agree with the live text:
- §7-g: BH02 MANUSCRIPT-AUDIT:78 marks ch07:126 sentence 3 "supports, understated".
- §7-i: it agrees with ch07:137–143 and GR:855–865.

### 8. Open problems and limitations (1.0 pp)

| ID | Item | Source | Status |
|---|---|---|---|
| §8-a | The coherent-instrument and composite (operational-lifting) layer: which of (iii)–(v) a physical substratum supplies | Main:22, :542, :758; GR:228 | open |
| §8-b | Selection of the relating evolution | Main:624 | open |
| §8-c | Origin of the quadratic Born exponent | Main:20, :534 | open (frontier item) |
| §8-d | Formalization gaps: history-level (C4) ⇒ non-permutation rooted map (F11); the time-$t$ joint-law reading; the CMI vanishing criterion; prior independence in C1′; the proof of (ii) ⟺ (iii) | Main:99, :139, :500, :580(2), :608 | stated as not formalized |
| §8-e | The variational identity $\inf_{\mathcal R} I = M_t$, false in its naive fixed-dimension form | Main:594 | open |
| §8-f | Recurrent-family gluing; approximation on windows $t\ll t_R$ | Main:618 | open |
| §8-g | C2 necessity is conditional on the hidden-sector mixing hypothesis, with ETH as motivation | Main:433–451, :480, :720 | conditional |
| §8-h | Bell: a deterministic completion with pointwise cones and a setting-independent ensemble is Bell-local (Bell's theorem applied). The adopted branch needs H-Bell | Main:360–377 (check 11, `equivalence_recovery_probes.py`), :392–394 | ceiling proved; H-Bell open |
| §8-i | No ontology-level falsifier is established; the posit ledger has twelve items | Main:702–704, :708 | stated |
| §8-j | The black-hole items of §7-j | §7-j | open |

### 9. Related work (0.5 pp)

Built from AUDIT §7's list (AUDIT:2047–2076), with the descriptions it requires:
- Barandes B23, B25 and B26, with [11] and [12] correctly assigned (F17);
- EG for the trajectory-labelling realization;
- RHP 2014 Thm 2.4 and BD Prop. 1;
- DO3 v3 Prop. 1 and App. A, as concurrent;
- Milz et al. 2020 and Strasberg–García Díaz 2019, as studies of Kolmogorov consistency of
  projective records;
- BLP 2009 as a one-way witness; BJA for the bijective distinguishability characterization;
- GO, SCH, JDM, LPW, SC (the ε-machine contrast), GH and MO;
- Page 1993, 2005 and 2013, and Penington 2019.

Pending before any positioning sentence: 't Hooft 2016, Spekkens 2007, Hardy 2004, HKLP [55],
Rutten, the comb-realization theorem, Popescu–Short–Winter and Hayden–Preskill.

Not imported:
- the ≤ n³ bound, the Main:210 contrast and the Main:504 definition (F13);
- Main's descriptions of Calvo, Pimenta and Doukas (F14–F16);
- the [11]/[12] swap (F17);
- the Born-equilibrium sentence (F18);
- the stale [24] (F19).

### 10. Conclusion (0.25 pp)

Restates E1 at its scope, §4-a and §5-e, §6-c, and §7-c and §7-h. Under the BH-01-conflict-free
variant it carries only §7-b, §7-h and §7-i from §7. No new claim.

### Appendix A. Kernel map (0.5 pp; scope is decision 6)

**Default: kernel-backed claims only**, about 15 rows. Each row gives the claim ID, its declaration
(module:line at the drafting commit), its unformalized links, and the recipe that checks it
(`lake build` + `tools/lean_axiom_check.py`). "Machine-checked" covers only these rows
(AUDIT:2040–2045), and only once decision 2 is met.

Alternative: the full claim map, about 55 rows, at about 1.5 pp. That would raise the recommended
total to about 15.25 pp, which needs a cut elsewhere (for example §9 to 0.5 pp and §8 to 0.75 pp).

### References (1.0 pp)

## Alternative scopes (owner decision 1)

| Scope | Content of §7 and other changes | Pages |
|---|---|---|
| **Alt-L (lean)** | §7 cut to 1.0 pp: §7-b, §7-c, §7-d, §7-g (one sentence, since §7-h depends on it), §7-h, §7-i. Drops §7-e and §7-f. §6-f and §8-h dropped; Appendix A folded into §3 as a kernel table. **Still carries §7-c and §7-h**, so it meets ch07:110/FULL:1987, ch07:126 s1/FULL:2003 and GR:869 (R11) | ≈ 12.25 |
| **Recommended** | as above | ≈ 14.25 |
| **Alt-X (expanded)** | adds: C8-R with display E3 as new manuscript content, a candidate with no priority sentence (+0.5); OI⁺ (E4) and `readWriteSourced_not_qm` (+0.25); the Leggett–Garg comb (Main:460–464; not classified) (+0.25). §8 trimmed to 0.75 | ≈ 15.0 |
| **BH-01-conflict-free §7 (variant, combinable with any of the above)** | §7 carries only §7-a, §7-b, §7-g, §7-h, §7-i and §7-j, and drops claim A (§7-c, §7-d) and item F (§7-f). It removes the BH-01 conflicts (ch07:110/FULL:1987; GR:811). It is **not** free of corpus conflict: §7-h contradicts ch07:126 sentence 1 / FULL:2003 and GR:869 (BH02 MANUSCRIPT-AUDIT:70–73, :256–259), so those sites must be corrected first (decision 1(a)). The alternative is to drop §7-h as well (decision 1(a), option (ii)). Under this variant, the contribution paragraph's black-hole sentence and §10 carry only §7-b, §7-h and §7-i. §7 becomes about 1.0 pp | −0.75 |

Kept out of every scope:
- C5, C6 and C13;
- C8-D and C12 as displays;
- GR:226's box;
- the cosmological posits;
- PE-01, which concerns a book sentence on unpredictability (ch18:114) and is covered in kind by
  prior work. If the owner wants it, it is one optional sentence in §8.
